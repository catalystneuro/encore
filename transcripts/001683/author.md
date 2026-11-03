# 001683 · author · run 41601386820

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls paper claims/001683 entries attempts | head -50
```

```
<persisted-output>
Output too large (36.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/df2453c6-ffcf-413a-b1e0-ec2bb69aaee4/tool-results/bnho9e2wm.txt

Preview (first 2KB):
Tue Nov  3 08:14:52 UTC 2026
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
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-13`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
10	
11	An attempt has three roles, each a separate run with a separate context:
12	
13	- The **reader** reads the paper and writes the claims file: every finding,
14	  and how each is to be tested, taken from the paper. A second reader checks
15	  it against the paper. Readers never see the dataset's data.
16	- The **author** tests the claims on the dataset. It reads the paper to
17	  understand the claims, but the claims file binds it: it cannot change a
18	  claim's statement, expected values or criterion. A method detail the file
19	  lacks it takes from the paper, citing the passage, and it asks a reader
20	  only when it believes the file misreads the paper.
[... 593 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -80; wc -l docs/design.md docs/archives.md; ls paper claims/001683 entries/001453-fouke-2025; cat attempts/001453-fouke-2025-01.yaml
```

```
<persisted-output>
Output too large (39.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/df2453c6-ffcf-413a-b1e0-ec2bb69aaee4/tool-results/b7l1k8w1u.txt

Preview (first 2KB):
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Dashboard:** <https://encorescience.org/>
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper claims/001683 entries/001453-fouke-2025; cat claims/001683/*
```

```
<persisted-output>
Output too large (37KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/df2453c6-ffcf-413a-b1e0-ec2bb69aaee4/tool-results/b6bmdw5nf.txt

Preview (first 2KB):
claims/001683:
10.1109-tnsre.2025.3644273.yaml

entries/001453-fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt

paper:
10.1109-tnsre.2025.3644273.supp.pdf
10.1109-tnsre.2025.3644273.txt
# Claims for Gao, Frake, Durand and He (2026), "Transcranial Focused Ultrasound Stimulation
# Targeting White Matter Inhibits Seizures in a Rat Model of Epilepsy", IEEE Trans Neural Syst
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/## DANDI/,/^## [A-Z]/p' docs/archives.md | head -150
```

```
## DANDI

- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
- **Versions.** A published version (`0.220126.1855`) is fixed and has a DOI,
  `10.48324/dandi.<id>/<version>`. The draft can change. Pin the version the
  paper cites, or the latest published one. For a draft, record its
  modification time under `dataset: modified` in the attempt.
- **Reading.** List the assets and read metadata with the DANDI REST API
  (`https://api.dandiarchive.org/api/dandisets/<id>/versions/<version>/` and its
  `assets/` endpoint). Read NWB files by streaming them: open each asset's S3
  URL with `remfile` and `h5py`, and read it with `pynwb`. Do not download files
  to disk.
- **In an entry.** The entry names the dataset as `dandi:<id>/<version>` under
  `related`. The helper module keeps the version in one constant.

## CRCNS
```

**Agent calls Read**

```json
{
 "file_path": "claims/001683/10.1109-tnsre.2025.3644273.yaml"
}
```

```
1	# Claims for Gao, Frake, Durand and He (2026), "Transcranial Focused Ultrasound Stimulation
2	# Targeting White Matter Inhibits Seizures in a Rat Model of Epilepsy", IEEE Trans Neural Syst
3	# Rehabil Eng 34, doi:10.1109/tnsre.2025.3644273, on dandiset 001683 (same title on the archive;
4	# its description says the dataset is described in this paper).
5	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
6	# protocol as stated in docs/protocol.md (version pilot-10).
7	#
8	# Text read: the NIH author manuscript (PMC12848950) as served by Europe PMC, stored under paper/:
9	# abstract, Introduction, Methods, Results, Discussion, Data Availability and the legends of Figs. 1
10	# to 6; and the supplement (supp1-3644273.pdf, 8 pages: ex-vivo scanning, target confirmation, Figs.
11	# S1 to S7). There is no PDF of the main paper, so values and significance marks drawn only inside
12	# Figs. 2 to 6 were not read; Figs. S4, S5 and S7 were viewed in the supplement PDF. The paper links
13	# no code; the only repository it names is the dandiset. No code was read.
14	#
15	# Data the paper used, as it reports them (Methods A to E, supplement):
16	#  - Rats. 16 adult male Sprague-Dawley rats in the epilepsy study, 10 tFUS (experimental) and 6
17	#    sham; 7 more in a mechanism study, 23 in all. The wild-type analysis (Fig. 5) uses all 23
18	#    (Fig. 5B, N = 23 per group). Isoflurane anesthesia throughout.
19	#  - Recordings. A 32-channel skull EEG probe (NeuroNexus HC32), aligned with bregma, and a
20	#    64-channel intracranial array in left S1 (AP -2, ML -2.5, DV -1.5 mm). Tucker-Davis system at
[... 565 more lines not kept]
```

**Agent**

Claims file read: 22 claims. Now the dataset.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/001683/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/001683/versions/" | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; V=0.260109.2104; curl -s "https://api.dandiarchive.org/api/dandisets/001683/versions/$V/" | python -c "import json,sys; d=json.load(sys.stdin); print(d.get('description')); print(json.dumps(d.get('assetsSummary'),indent=1)); print(d.get('relatedResource'))"; curl -s "https://api.dandiarchive.org/api/dandisets/001683/versions/$V/assets/?page_size=1000" > assets.json; python -c "
import json; d=json.load(open('assets.json')); print(d['count'])
for a in d['results']: print(a['path'], round(a['size']/1e9,2), a['asset_id'])" > assets.txt; wc -l assets.txt; head -80 assets.txt
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 81,319p assets.txt | awk '{print $1, $2}' | column -c 200 | head -150
```

```
sub-BH626/sub-BH626_ses-20241129T175012_ecephys.nwb 0.47	sub-BH647/sub-BH647_ses-20250121T171532_ecephys.nwb 0.63	sub-BH660/sub-BH660_ses-20250304T172410_ecephys.nwb 0.63
sub-BH626/sub-BH626_ses-20241129T180102_ecephys.nwb 1.03	sub-BH647/sub-BH647_ses-20250121T172238_ecephys.nwb 0.64	sub-BH660/sub-BH660_ses-20250304T173110_ecephys.nwb 0.63
sub-BH626/sub-BH626_ses-20241129T181333_ecephys.nwb 0.98	sub-BH647/sub-BH647_ses-20250121T172949_ecephys.nwb 0.63	sub-BH660/sub-BH660_ses-20250304T173841_ecephys.nwb 0.63
sub-BH626/sub-BH626_ses-20241129T182435_ecephys.nwb 0.98	sub-BH647/sub-BH647_ses-20250121T173651_ecephys.nwb 0.63	sub-BH660/sub-BH660_ses-20250304T174539_ecephys.nwb 0.63
sub-BH626/sub-BH626_ses-20241129T183532_ecephys.nwb 0.98	sub-BH647/sub-BH647_ses-20250121T174454_ecephys.nwb 0.63	sub-BH662/sub-BH662_ses-20250311T144926_ecephys.nwb 0.47
sub-BH626/sub-BH626_ses-20241129T184707_ecephys.nwb 0.9		sub-BH647/sub-BH647_ses-20250121T175204_ecephys.nwb 0.63	sub-BH662/sub-BH662_ses-20250311T145754_ecephys.nwb 0.63
sub-BH626/sub-BH626_ses-20241129T185715_ecephys.nwb 0.94	sub-BH648/sub-BH648_ses-20250213T160900_ecephys.nwb 0.47	sub-BH662/sub-BH662_ses-20250311T150523_ecephys.nwb 0.63
sub-BH634/sub-BH634_ses-20241211T180120_ecephys.nwb 0.47	sub-BH648/sub-BH648_ses-20250213T161441_ecephys.nwb 0.63	sub-BH662/sub-BH662_ses-20250311T151229_ecephys.nwb 0.63
sub-BH634/sub-BH634_ses-20241211T181653_ecephys.nwb 0.66	sub-BH648/sub-BH648_ses-20250213T162147_ecephys.nwb 0.63	sub-BH662/sub-BH662_ses-20250311T152033_ecephys.nwb 0.63
sub-BH634/sub-BH634_ses-20241211T182432_ecephys.nwb 0.67	sub-BH648/sub-BH648_ses-20250213T162857_ecephys.nwb 0.63	sub-BH662/sub-BH662_ses-20250311T152734_ecephys.nwb 0.63
sub-BH634/sub-BH634_ses-20241211T183445_ecephys.nwb 0.69	sub-BH648/sub-BH648_ses-20250213T163641_ecephys.nwb 0.63	sub-BH662/sub-BH662_ses-20250311T153438_ecephys.nwb 0.63
sub-BH634/sub-BH634_ses-20241211T184237_ecephys.nwb 0.65	sub-BH648/sub-BH648_ses-20250213T164348_ecephys.nwb 0.63	sub-B
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
cat entries/001453-fouke-2025/requirements.in entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/README.md; python -c "import pynwb, remfile, h5py; print(pynwb.__version__)"; which python; python --version
```

```
dandi
h5py
matplotlib
numpy
pandas
remfile
scipy
statsmodels
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
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q pynwb remfile h5py dandi numpy scipy pandas statsmodels matplotlib 2>&1 | tail -3; python -c "import pynwb; print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > peek.py <<'EOF'
import sys, h5py, remfile, requests
aid=sys.argv[1]
url=f"https://api.dandiarchive.org/api/assets/{aid}/download/"
r=requests.head(url,allow_redirects=True); s3=r.url
f=h5py.File(remfile.File(s3),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        v=''
        if obj.size<20 and obj.dtype.kind in 'iufSO': v=obj[()]
        print(name,obj.shape,obj.dtype,dict(obj.attrs).get('unit',''),dict(obj.attrs).get('rate',''),v)
    else:
        a={k:v for k,v in obj.attrs.items() if k in('neurodata_type','description','comments')}
        print(name+'/',a)
f.visititems(show)
for k in ['session_description','identifier','session_start_time','experiment_description']:
    if k in f: print(k, f[k][()])
EOF
python peek.py 728fccd2-d993-461a-b4d2-d2be356dabb9 2>&1 | head -120
```

```
<persisted-output>
Output too large (113.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/df2453c6-ffcf-413a-b1e0-ec2bb69aaee4/tool-results/bksvyv97b.txt

Preview (first 2KB):
acquisition/ {}
acquisition/ElectricalSeries/ {'comments': 'no comments', 'description': 'EEG data', 'neurodata_type': 'ElectricalSeries'}
acquisition/ElectricalSeries/data (11450880, 32) float64 volts  
acquisition/ElectricalSeries/electrodes (32,) int64   
acquisition/ElectricalSeries/starting_time () float64 seconds 3051.7578125 0.0
analysis/ {}
file_create_date (1,) object   [b'2025-12-22T05:27:07.802000-05:00']
general/ {}
general/data_collection () object   b'BH624_BASELINE'
general/devices/ {}
general/devices/Electrode/ {'description': 'EEG-rat-32-A-10-functional', 'neurodata_type': 'Device'}
general/experiment_description () object   b'Transcranial Focused Ultrasound Stimulation Targeting White Matter Inhibits Seizures in a Rat Model of Epilepsy'
general/experimenter (1,) object   [b'Huan, Annabel']
general/extracellular_ephys/ {}
general/extracellular_ephys/EEG/ {'description': 'EEG electrode', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/electrodes/ {'description': 'EEG electrodes', 'neurodata_type': 'DynamicTable'}
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v "^processing/.*/\(data\|timestamps\)\b" /home/runner/.claude/projects/-home-runner-work-encore-encore/df2453c6-ffcf-413a-b1e0-ec2bb69aaee4/tool-results/bksvyv97b.txt | sed -n 30,60p; wc -l /home/runner/.claude/projects/-home-runner-work-encore-encore/df2453c6-ffcf-413a-b1e0-ec2bb69aaee4/tool-results/bksvyv97b.txt; cut -c1-60 /home/runner/.claude/projects/-home-runner-work-encore-encore/df2453c6-ffcf-413a-b1e0-ec2bb69aaee4/tool-results/bksvyv97b.txt | awk -F/ '{print $1"/"$2"/"$3}' | sort | uniq -c | sort -rn | head
```

```
<persisted-output>
Output too large (70.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/df2453c6-ffcf-413a-b1e0-ec2bb69aaee4/tool-results/bdt8yilwr.txt

Preview (first 2KB):
general/optophysiology/ {}
general/related_publications (1,) object   [b'doi:10.1109/TNSRE.2025.3644273']
general/subject/ {'neurodata_type': 'Subject'}
general/subject/age () object   b'P24W'
general/subject/description () object   b'HSD:WI rat'
general/subject/sex () object   b'M'
general/subject/species () object   b'Rattus norvegicus'
general/subject/subject_id () object   b'BH624'
identifier () object   b'tFUS group'
intervals/ {}
intervals/custom_intervals_table_name/ {'description': 'seizure labels for contralateral and ipsilateral hemispheres', 'neurodata_type': 'TimeIntervals'}
intervals/custom_intervals_table_name/id (24,) int64   
intervals/custom_intervals_table_name/start_time (24,) float64   
intervals/custom_intervals_table_name/stop_time (24,) float64   
intervals/custom_intervals_table_name/tags (24,) object   
processing/ {}
[... 8 more lines not kept]
```

**Agent**

Seizure labels are in the files (intervals table with tags). Surveying metadata of all 318 files.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import json, h5py, remfile, requests, sys
from concurrent.futures import ThreadPoolExecutor
d=json.load(open('assets.json'))['results']
def s(x):
    return x.decode() if isinstance(x,bytes) else x
def one(a):
    try:
        url=f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
        s3=requests.head(url,allow_redirects=True).url
        f=h5py.File(remfile.File(s3),'r')
        out=dict(path=a['path'],asset_id=a['asset_id'],s3=s3)
        for k in ['session_description','identifier','general/data_collection','general/notes','general/subject/subject_id','general/subject/description','general/subject/age','general/subject/genotype','general/stimulus','general/protocol']:
            if k in f: out[k]=s(f[k][()])
        out['start']=s(f['session_start_time'][()][0]) if f['session_start_time'].shape else s(f['session_start_time'][()])
        acq={}
        for k in f['acquisition']:
            g=f['acquisition'][k]
            acq[k]=dict(shape=g['data'].shape, dtype=str(g['data'].dtype), rate=float(g['starting_time'].attrs['rate']) if 'starting_time' in g else None, desc=s(g.attrs.get('description')), chunks=g['data'].chunks, conv=float(g['data'].attrs.get('conversion',1)))
        out['acq']=acq
        iv={}
        for k in f['intervals']:
            g=f['intervals'][k]
            iv[k]=dict(cols=list(g.keys()), n=g['id'].shape[0], desc=s(g.attrs.get('description')))
            if 'tags' in g:
                import numpy as np
                iv[k]['start']=g['start_time'][:].tolist(); iv[k]['stop']=g['stop_time'][:].tolist()
                # tags ragged
                if 'tags_index' in g:
                    t=[s(x) for x in g['tags'][:]]; idx=g['tags_index'][:]
                    iv[k]['tags']=[t[(idx[i-1] if i else 0):idx[i]] for i in range(len(idx))]
                else: iv[k]['tags']=[s(x) for x in g['tags'][:]]
        out['iv']=iv
        out['proc']=list(f['processing'].keys())
        out['stim']=list(f['stimulus'].keys()) if 'stimulus' in f else []
        out['nelec']=f['general/extracellular_ephys/electrodes/id'].shape[0]
        return out
    except Exception as e:
        return dict(path=a['path'],asset_id=a['asset_id'],err=repr(e))
with ThreadPoolExecutor(16) as ex: res=list(ex.map(one,d))
json.dump(res,open('survey.json','w'),default=str)
print(sum('err' in r for r in res))
EOF
time python survey.py
```

```
0

real	3m38.815s
user	0m11.643s
sys	0m1.571s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import json,collections
r=json.load(open('survey.json'))
c=collections.Counter((x.get('session_description'),x.get('identifier'),x.get('general/notes'),tuple(sorted(x['acq'])),tuple(sorted(x['iv']))) for x in r)
for k,v in c.items(): print(v,k)
print(collections.Counter(x.get('general/subject/description') for x in r))
print(collections.Counter(x.get('general/subject/genotype') for x in r))
"
```

```
40 ('Labeled_data', 'tFUS group', 'EEG signals with seizure labels', ('ElectricalSeries',), ('custom_intervals_table_name',))
30 ('Labeled_data', 'sham group', 'EEG signals with seizure labels', ('ElectricalSeries',), ('custom_intervals_table_name',))
228 ('EP data', 'wild_type', 'LFP signal for EP test', ('ElectricalSeries',), ('custom_intervals_table_name',))
20 ('EEG data for PLV analysis', 'wild_type', 'EEG signal for PLV analysis, ipsilateral channel 1-16 (S1: 7,8,10,12),contralateral channel 17-32(S1: 21,23,25,26)', ('ElectricalSeries',), ('custom_intervals_table_name',))
Counter({'HSD:WI rat': 318})
Counter({None: 318})
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import json,collections
r=json.load(open('survey.json'))
lab=[x for x in r if x['session_description']=='Labeled_data']
lab.sort(key=lambda x:(x['general/subject/subject_id'],x['start']))
for x in lab:
    iv=x['iv']['custom_intervals_table_name']; a=x['acq']['ElectricalSeries']
    tags=collections.Counter(t for tt in iv['tags'] for t in (tt if isinstance(tt,list) else [tt]))
    print(x['general/subject/subject_id'],x['identifier'][:4],x['general/data_collection'],x['start'][:19],a['shape'],a['rate'],x['nelec'],iv['n'],dict(tags), x['path'].split('_ses-')[1][:15])
"
```

```
BH624 tFUS BH624_BASELINE 2024-12-03T19:36:37 [11450880, 32] 3051.7578125 32 24 {'ipsilateral': 12, 'contralateral': 12} 20241203T193637
BH624 tFUS BH624_CC_1Hz 2024-12-03T20:40:11 [11452160, 32] 3051.7578125 32 31 {'ipsilateral': 16, 'contralateral': 15} 20241203T204011
BH624 tFUS BH624_post1 2024-12-03T21:44:00 [11450880, 32] 3051.7578125 32 8 {'ipsilateral': 4, 'contralateral': 4} 20241203T214400
BH624 tFUS BH624_post2 2024-12-03T22:47:57 [11463680, 32] 3051.7578125 32 22 {'contralateral': 11, 'ipsilateral': 11} 20241203T224757
BH626 tFUS BH626_BASELINE 2024-11-29T21:28:13 [11459328, 32] 3051.7578125 32 32 {'contralateral': 16, 'ipsilateral': 16} 20241129T212813
BH626 tFUS BH626_CC_1Hz 2024-11-29T22:32:19 [11447552, 32] 3051.7578125 32 14 {'ipsilateral': 7, 'contralateral': 7} 20241129T223219
BH626 tFUS BH626_post1 2024-11-29T23:36:55 [11448320, 32] 3051.7578125 32 18 {'contralateral': 9, 'ipsilateral': 9} 20241129T233655
BH626 tFUS BH626_post2 2024-11-30T00:40:54 [11448320, 32] 3051.7578125 32 20 {'contralateral': 10, 'ipsilateral': 10} 20241130T004054
BH634 tFUS BH634_BASELINE 2024-12-11T20:43:57 [11456000, 32] 3051.7578125 32 59 {'contralateral': 30, 'ipsilateral': 29} 20241211T204357
BH634 tFUS BH634_CC_1Hz 2024-12-11T21:47:22 [11446528, 32] 3051.7578125 32 20 {'ipsilateral': 11, 'contralateral': 9} 20241211T214722
BH634 tFUS BH634_post1 2024-12-11T22:51:25 [11446784, 32] 3051.7578125 32 4 {'ipsilateral': 2, 'contralateral': 2} 20241211T225125
BH634 tFUS BH634_post2 2024-12-11T23:54:55 [11449344, 32] 3051.7578125 32 1 {'no_seizure': 1} 20241211T235455
BH635 sham BH635_BASELINE 2024-12-13T21:57:54 [11448320, 32] 3051.7578125 32 28 {'contralateral': 14, 'ipsilateral': 14} 20241213T215754
BH635 sham BH635_SHAM 2024-12-13T23:05:29 [11485696, 32] 3051.7578125 32 64 {'contralateral': 30, 'ipsilateral': 34} 20241213T230529
BH635 sham BH635_SHAM 2024-12-14T00:13:37 [11560704, 32] 3051.7578125 32 69 {'contralateral': 35, 'ipsilateral': 34} 20241214T001337
BH635 sham B
[... 55 more lines not kept]
```

**Agent**

Labeled seizure data: 10 tFUS rats × 4 blocks, 6 sham rats × 5 blocks (BH635's labels are odd: two "SHAM" blocks and "BH636_post1"). Now the EP and PLV files.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import json,collections
r=json.load(open('survey.json'))
for kind in ['EP data','EEG data for PLV analysis']:
  lab=[x for x in r if x['session_description']==kind]
  lab.sort(key=lambda x:(x['general/subject/subject_id'],x['start']))
  for x in lab:
    iv=x['iv']['custom_intervals_table_name']; a=x['acq']['ElectricalSeries']
    tags=collections.Counter(t for tt in iv['tags'] for t in (tt if isinstance(tt,list) else [tt]))
    print(x['general/subject/subject_id'],x['general/data_collection'],x['start'][:19],a['shape'],a['rate'],a['desc'],x['nelec'],iv['n'],dict(tags),iv['cols'], round(min(iv['start']),2) if iv['start'] else None, x['path'].split('_ses-')[1][:15])
" > wt.txt; wc -l wt.txt; head -30 wt.txt; grep PLV -A0 wt.txt | head -3; tail -22 wt.txt
```

```
248 wt.txt
BH624 BH624_BASELINE 2024-12-03T15:49:17 [745472, 64] 3051.7578125 EEG data 64 121 {'tFUS': 121} ['id', 'start_time', 'stop_time', 'tags'] 2.39 20241203T154917
BH624 BH624_1500_200_67_15_CENTER 2024-12-03T15:53:59 [1525760, 64] 3051.7578125 EEG data 64 249 {'tFUS': 249} ['id', 'start_time', 'stop_time', 'tags'] 2.37 20241203T155359
BH624 BH624_FRONT05mm_1500_15 2024-12-03T16:03:26 [1530880, 64] 3051.7578125 EEG data 64 250 {'tFUS': 250} ['id', 'start_time', 'stop_time', 'tags'] 2.36 20241203T160326
BH624 BH624_BACK05mm_1500_15 2024-12-03T16:12:38 [1543424, 64] 3051.7578125 EEG data 64 252 {'tFUS': 252} ['id', 'start_time', 'stop_time', 'tags'] 2.39 20241203T161238
BH624 BH624_BACK1mm_1500_15 2024-12-03T16:21:52 [1548032, 64] 3051.7578125 EEG data 64 253 {'tFUS': 253} ['id', 'start_time', 'stop_time', 'tags'] 2.35 20241203T162152
BH624 BH624_FRONT1mm_1500_15 2024-12-03T16:30:49 [1610496, 64] 3051.7578125 EEG data 64 263 {'tFUS': 263} ['id', 'start_time', 'stop_time', 'tags'] 2.36 20241203T163049
BH624 BH624_LSIDE05mm_1500_15 2024-12-03T16:49:54 [1545728, 64] 3051.7578125 EEG data 64 253 {'tFUS': 253} ['id', 'start_time', 'stop_time', 'tags'] 2.38 20241203T164954
BH624 BH624_RSIDE05mm_1500_15 2024-12-03T16:58:46 [1529600, 64] 3051.7578125 EEG data 64 250 {'tFUS': 250} ['id', 'start_time', 'stop_time', 'tags'] 2.36 20241203T165846
BH624 BH624_DEEP1mm_1500_15 2024-12-03T17:10:48 [1527808, 64] 3051.7578125 EEG data 64 250 {'tFUS': 250} ['id', 'start_time', 'stop_time', 'tags'] 2.37 20241203T171048
BH626 BH626_BASELINE 2024-11-29T17:50:12 [916992, 64] 3051.7578125 EEG data 64 120 {'tFUS': 120} ['id', 'start_time', 'stop_time', 'tags'] 2.87 20241129T175012
BH626 BH626_CENTER_1500_15 2024-11-29T18:01:02 [2020864, 64] 3051.7578125 EEG data 64 264 {'tFUS': 264} ['id', 'start_time', 'stop_time', 'tags'] 2.88 20241129T180102
BH626 BH626_BACK1mm_1500_15 2024-11-29T18:13:33 [1908736, 64] 3051.7578125 EEG data 64 249 {'tFUS': 249} ['id', 'start_time', 'stop_time', 'tags
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; awk '{print $1}' wt.txt | sort | uniq -c | tr '\n' ' '; echo; grep -c 1Hz_20ms wt.txt; grep -v 1Hz_20ms wt.txt | awk '{print $1}' | sort -u | wc -l; wc -w paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1109-tnsre.2025.3644273.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1109-tnsre.2025.3644273.txt",
 "offset": 215
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Paper read. Now checking chunk layouts (decides what is affordable to stream) and electrode tables.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import json,collections
r=json.load(open('survey.json'))
print(collections.Counter((x['session_description'],str(x['acq']['ElectricalSeries']['chunks']),x['acq']['ElectricalSeries']['conv'],x['acq']['ElectricalSeries']['dtype']) for x in r))
"
cat > elec.py <<'EOF'
import sys,h5py,remfile,json
r={x['asset_id']:x for x in json.load(open('survey.json'))}
for aid in sys.argv[1:]:
    f=h5py.File(remfile.File(r[aid]['s3']),'r')
    e=f['general/extracellular_ephys/electrodes']
    for k in e: 
        if k!='group': print(k, e[k][:40] if e[k].shape else e[k][()])
    es=f['acquisition/ElectricalSeries']
    print(dict(es.attrs)); print(dict(es['data'].attrs)); print(es['data'].compression, es['data'].chunks)
    iv=f['intervals/custom_intervals_table_name']
    print(iv['start_time'][:10], iv['stop_time'][:10], iv['tags'][:10])
    print(list(f['general'].keys()))
EOF
python elec.py 728fccd2-d993-461a-b4d2-d2be356dabb9 27e62143-e008-4315-b838-c8d4625d79f0 f4650f5c-2730-4112-8dba-9f9c21b52a04 2>&1 | cut -c1-600
```

```
Counter({('EP data', 'None', 1.0, 'float64'): 228, ('Labeled_data', 'None', 1.0, 'float64'): 70, ('EEG data for PLV analysis', 'None', 1.0, 'float64'): 20})
filtering [b'Low-pass filter at 300 Hz' b'Low-pass filter at 300 Hz'
 b'Low-pass filter at 300 Hz' b'Low-pass filter at 300 Hz'
 b'Low-pass filter at 300 Hz' b'Low-pass filter at 300 Hz'
 b'Low-pass filter at 300 Hz' b'Low-pass filter at 300 Hz'
 b'Low-pass filter at 300 Hz' b'Low-pass filter at 300 Hz'
 b'Low-pass filter at 300 Hz' b'Low-pass filter at 300 Hz'
 b'Low-pass filter at 300 Hz' b'Low-pass filter at 300 Hz'
 b'Low-pass filter at 300 Hz' b'Low-pass filter at 300 Hz'
 b'Low-pass filter at 300 Hz' b'Low-pass filter at 300 Hz'
 b'Low-pass filter at 300 Hz' b'Low-pass filter at 300 Hz'
 b'Low-pass filter at 300 Hz' b'Low-pass filter at 300 Hz'
 b'Low-pass filter at 300 Hz' b'Low-pass filter at 300 Hz'
 b'Low-pass filter at 300 Hz' b'Low-pass filter at 300 Hz'
 b'Low-pass filter at 300 Hz' b'Low-pass filter at 300 Hz'
 b'Low-pass filter at 300 Hz' b'Low-pass filter at 300 Hz'
 b'Low-pass filter at 300 Hz' b'Low-pass filter at 300 Hz']
group_name [b'channel1' b'channel2' b'channel3' b'channel4' b'channel5' b'channel6'
 b'channel7' b'channel8' b'channel9' b'channel10' b'channel11'
 b'channel12' b'channel13' b'channel14' b'channel15' b'channel16'
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q pymupdf && python -c "
import fitz; d=fitz.open('paper/10.1109-tnsre.2025.3644273.supp.pdf')
for i in [1,6,7]:
    d[i].get_pixmap(dpi=110).save(f'supp{i+1}.png')
" && cat > speed.py <<'EOF'
import h5py,remfile,json,time,numpy as np
r={x['asset_id']:x for x in json.load(open('survey.json'))}
s3=r['728fccd2-d993-461a-b4d2-d2be356dabb9']['s3']
for bs in [8,32]:
    f=h5py.File(remfile.File(s3,verbose=False),'r'); d=f['acquisition/ElectricalSeries/data']
    t=time.time(); n=int(3051.76*120); x=d[1000000:1000000+n]; dt=time.time()-t
    print('remfile',x.nbytes/1e6,'MB',dt,'s',x.nbytes/1e6/dt,'MB/s')
import fsspec
fs=fsspec.filesystem('http')
t=time.time()
with fs.open(s3,block_size=64*2**20,cache_type='none') as fh:
    f=h5py.File(fh,'r'); d=f['acquisition/ElectricalSeries/data']; off=d.id.get_offset()
    n=int(3051.76*120); x=d[3000000:3000000+n]
print('fsspec',x.nbytes/1e6/(time.time()-t),'MB/s', off)
EOF
uv pip install -q fsspec aiohttp && python speed.py
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > speed2.py <<'EOF'
import requests,json,time,numpy as np
from concurrent.futures import ThreadPoolExecutor
r={x['asset_id']:x for x in json.load(open('survey.json'))}
s3=r['728fccd2-d993-461a-b4d2-d2be356dabb9']['s3']
off=135280; total=500*2**20
sess=requests.Session()
def get(a):
    b=a+32*2**20-1
    return sess.get(s3,headers={'Range':f'bytes={a}-{b}'}).content
for nt in [8,16]:
    t=time.time()
    with ThreadPoolExecutor(nt) as ex: parts=list(ex.map(get, range(off+10**9, off+10**9+total, 32*2**20)))
    print(nt, sum(map(len,parts))/1e6/(time.time()-t),'MB/s')
EOF
python speed2.py; nproc; free -g
```

```
8 306.79545778172997 MB/s
16 400.6386972187203 MB/s
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          10           0           4          13
Swap:              2           0           2
Shell cwd was reset to
```

**Agent**

Parallel range requests reach ~400 MB/s, so whole-block EEG analyses (70 files, ~205 GB) look feasible in about 10 to 20 min of I/O. Looking at Fig. S1 for the labeling electrode.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp2.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fitz; d=fitz.open('paper/10.1109-tnsre.2025.3644273.supp.pdf')
p=d[1]; r=p.rect; clip=fitz.Rect(r.x0+r.width*0.13,r.y0+r.height*0.11,r.x0+r.width*0.37,r.y0+r.height*0.33)
p.get_pixmap(dpi=400,clip=clip).save('s1zoom.png')" 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s1zoom.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && python -c "
import json,numpy as np
r=json.load(open('survey.json'))
# BASELINE EP intervals spacing and PLV intervals
for x in r:
  if x['general/data_collection'] in ('BH624_BASELINE','BH624_CC_1Hz_20ms_15','BH626_1Hz_20ms_CC') and x['session_description']!='Labeled_data':
    iv=x['iv']['custom_intervals_table_name']; s=np.array(iv['start']); e=np.array(iv['stop'])
    print(x['general/data_collection'], len(s), np.unique(np.round(np.diff(s),2))[:8], np.unique(np.round(e-s,3))[:5], s[-1], x['acq']['ElectricalSeries']['shape'][0]/3051.7578125)
"
```

```
Tue Nov  3 08:21:46 UTC 2026
BH624_BASELINE 121 [2.] [2.2] 242.39136768 244.27626496
BH624_CC_1Hz_20ms_15 251 [2.] [2.2] 502.37067264 502.56150528
BH626_1Hz_20ms_CC 301 [1.] [2.2] 301.29016832 301.40268544
Shell cwd was reset to
```

**Agent**

Only 10 minutes elapsed; plenty of time. Looking at the example notebook's structure for format.

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025 && python -c "
import json; nb=json.load(open('reproduce_fouke_2025.ipynb'))
print(nb['metadata'])
for c in nb['cells'][:6]+nb['cells'][-3:]:
    print('----',c['cell_type'],c['metadata']); print(''.join(c['source'])[:1500])
"; head -60 omr.py; sed -n 1,200p ../../tools/entry.py | grep -n "def \|tag\|runtime" | head -40
```

```
{'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
---- markdown {}
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

[... 204 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && sed -n 1,70p tools/entry.py; sed -n 143,330p tools/entry.py
```

```
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
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
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
[... 237 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "max.minutes\|timeout\|def run" tools/entry.py | head; ls schemas 2>/dev/null || ls;
```

```
29:that takes longer than --max-minutes fails, even if it ran without error.
342:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
364:             f"--ExecutePreprocessor.timeout={timeout}", f"--ExecutePreprocessor.kernel_name={kernel}",
371:        if ok and seconds > max_minutes * 60:
373:            error = f"took {seconds / 60:.0f} minutes; the limit is {max_minutes:.0f}"
432:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
433:    parser.add_argument("--max-minutes", type=float, default=60,
469:    return run(entry_dir, output_dir, args.timeout, args.max_minutes)
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
```

**Agent**

Plan settled: three notebooks (seizure labels; block EEG spectra, AI and seizure PLI; wild-type EP and PLI), one helper. Writing the helper now.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import json,numpy as np
r=json.load(open('survey.json'))
lab=[x for x in r if x['session_description']=='Labeled_data']
# truncated seizures? and overlap/ordering; ipsi vs contra pairing
for x in lab[:70]:
    iv=x['iv']['custom_intervals_table_name']; T=x['acq']['ElectricalSeries']['shape'][0]/3051.7578125
    s=np.array(iv['start']); e=np.array(iv['stop']); tags=[t if isinstance(t,str) else t[0] for t in iv['tags']]
    trunc=((s<1)|(e>T-1)).sum()
    if trunc or (e<s).any() or s.min()<0: print(x['general/data_collection'], 'trunc',trunc, s.min(), e.max(), T)
print(lab[0]['iv']['custom_intervals_table_name']['tags'][:4])
EOF
```

```
BH624_CC_1Hz trunc 2 0.629358592 52.672222549333334 3752.6437888
BH634_BASELINE trunc 2 0.7063524693333334 62.267976362666666 3753.90208
BH634_CC_1Hz trunc 2 0.5559855786666666 56.70160520533333 3750.79829504
BH634_post1 trunc 2 0.3118967466666666 39.35494690133333 3750.88218112
BH634_post2 trunc 1 0.0 0.0 3751.72104192
BH638_post2 trunc 1 0.0 0.0 3751.3854976
BH642_BASELINE trunc 2 5.461333333333333e-06 48.612988245333334 3751.46938368
BH644_BASELINE trunc 2 5.461333333333333e-06 61.489332224 3751.804928
BH659_BASELINE trunc 2 0.009131349333333334 58.84567552 3751.13383936
BH659_SHAM trunc 2 0.21276808533333333 61.98487176533333 3753.14710528
BH659_post2 trunc 2 0.7528994133333333 58.62961425066667 3758.76747264
BH660_CC_1Hz trunc 1 0.8031819093333333 58.807402496 3751.3854976
BH660_post1 trunc 2 0.503349248 52.21408768 3753.14710528
BH663_post3 trunc 2 0.29532706133333336 62.317150207999994 3751.97270016
BH665_post3 trunc 2 0.6478561279999999 58.69609506133333 3751.46938368
BH635_SHAM trunc 2 5.461333333333333e-06 62.520557567999994 3788.21148672
BH636_post1 trunc 2 0.8216029866666666 62.515314688 3752.30824448
BH635_post2 trunc 2 0.51904512 62.494343168 3750.63052288
['ipsilateral', 'contralateral', 'ipsilateral', 'contralateral']
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/001683-gao-2026/tfus.py",
 "content": "\"\"\"Loading and measures for dandiset 001683 (Gao, Frake, Durand and He 2026, IEEE TNSRE,\ndoi:10.1109/tnsre.2025.3644273): EEG and seizure labels of 16 rats with 4-AP seizures, and the\nevoked-potential (LFP) and EEG recordings of the wild-type phase of 23 rats.\n\nThe files are streamed from the archive at the pinned version; nothing is written to disk. Every\nElectricalSeries in this dandiset is stored contiguous (not chunked) as float64, time by channel,\nso reading any channel means reading whole rows. `read_rows` therefore fetches the byte range of\na block of rows with parallel HTTP range requests, which is several times faster than h5py over\nremfile; `check_read` compares it with h5py on a slice.\n\nWhere the parameters come from:\n\n- RATE, the sampling rate, is the files' own (3051.7578125 Hz; Methods C, \"3051.8 Hz\").\n- Seizure labels are the files' `intervals` table, one row per seizure and hemisphere, tagged\n  ipsilateral or contralateral (claims file, M1: the paper's labels are used when the dandiset\n  holds them). Their times are in minutes, not the seconds NWB prescribes: the stops reach\n  about 62.5 in blocks of 3752 s, and the notebook checks this against the EEG. `MINUTES` converts.\n- Seizure metrics follow M2 of the claims file (Methods C): duration leaves out seizures that\n  start at the first sample or end at the last; percent time is summed durations over the block\n  length; the inter-seizure interval is the mean gap between neighbouring seizures. Whether a gap\n  runs from one offset to the next onset or from onset to onset is not said (\"time between\n  neighboring seizures\", Methods C); both are computed (`isi_gap`, `isi_onset`), and the gap\n  reading is the one the words favour.\n- Blocks are ordered by session start time within a rat: baseline, condition, post 1, post 2,\n  post 3 (Methods D and Fig. 1E, ~62.5 min blocks).\n- EEG channels: IPSI_CH (channel 8) and CONTRA_CH (channel 25), the electrodes encircled in the\n  drawing of Fig. 1A, which is repeated in Fig. S1 with the channel numbers printed (\"The EEG\n  electrode encircled by the blue/orange ring represents the selected channel data used to label\n  seizures\"); Methods E uses the same \"EEG electrode closest to the burr hole\" for the PSD. The\n  electrode table's coordinates put channels 8 and 25 at ML +/-2.8, AP -3 mm, next to the burr\n  holes at ML +/-2.5, AP -2 mm (Methods A).\n- S1 channels (Fig. 5A, which the text read does not list) are the ones the dandiset's own PLV\n  files name in their notes: ipsilateral 7, 8, 10, 12 and contralateral 21, 23, 25, 26; the\n  others of channels 1 to 16 (ipsilateral, right) and 17 to 32 (contralateral, left) are non-S1.\n- Preprocessing (Methods C): 60 Hz notch, common average reference over the 32 EEG channels.\n  ICA is not applied: which components the authors removed is not recorded (an assumption, as in\n  M1 of the claims file). The 3 to 300 Hz bandpass is applied in the PLI path; for the band power\n  the band limits are applied to the spectrum, with the total under the two M5 readings.\n- PSD: Welch, 2 s Hann windows, half overlap (a standard choice, M5 of the claims file). Bands\n  theta 5-8, alpha 8-12, beta 12-30, gamma 30-80 Hz (Methods E).\n- PLI (Methods E, Eq. 2): zero-phase 4th order Butterworth band filter (a standard choice, M6),\n  Hilbert phase, |mean sign(sin(dphi))|. For the seizure PLI the EEG is first decimated by 3 to\n  1017 Hz with an anti-alias filter, a standard choice that keeps every band (top 80 Hz) and\n  leaves the sign of the phase difference unchanged.\n- Statistics (Methods F, M3 of the claims file): two-way ANOVA with Bonferroni post hoc tests;\n  `twoway` runs the ordinary reading (OLS, post hoc t-tests on the pooled residual error, as\n  Prism does) and the repeated-measures reading (a linear mixed model with a random intercept per\n  rat, Prism's mixed-effects analysis, with Wald tests of contrasts).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport json\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\nfrom scipy import signal\n\nDANDISET_ID = \"001683\"\nDANDISET_VERSION = \"0.260109.2104\"\nAPI = \"https://api.dandiarchive.org/api\"\n\nRATE = 3051.7578125\nN_EEG = 32\nIPSI_CH, CONTRA_CH = 8, 25                 # 1-based channel numbers (Fig. S1 drawing)\nS1_IPSI, S1_CONTRA = (7, 8, 10, 12), (21, 23, 25, 26)\nNONS1_IPSI = tuple(c for c in range(1, 17) if c not in S1_IPSI)\nNONS1_CONTRA = tuple(c for c in range(17, 33) if c not in S1_CONTRA)\nBANDS = {\"theta\": (5.0, 8.0), \"alpha\": (8.0, 12.0), \"beta\": (12.0, 30.0), \"gamma\": (30.0, 80.0)}\nBLOCKS = [\"baseline\", \"condition\", \"post1\", \"post2\", \"post3\"]\nMINUTES = 60.0                             # the label table's unit, in seconds\nWELCH_S = 2.0\nDECIMATE = 3\n\n_session = requests.Session()\n\n\n# ---------------------------------------------------------------- archive\n\ndef list_assets() -> pd.DataFrame:\n    \"\"\"Every asset of the pinned version: path, asset id, size.\"\"\"\n    url = f\"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=1000\"\n    rows = []\n    while url:\n        page = _session.get(url).json()\n        rows += [{\"path\": a[\"path\"], \"asset_id\": a[\"asset_id\"], \"size\": a[\"size\"]} for a in page[\"results\"]]\n        url = page.get(\"next\")\n    return pd.DataFrame(rows)\n\n\ndef version_info() -> dict:\n    return _session.get(f\"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/info/\").json()\n\n\ndef s3_url(asset_id: str) -> str:\n    return _session.head(f\"{API}/assets/{asset_id}/download/\", allow_redirects=True).url\n\n\ndef _text(x):\n    if isinstance(x, np.ndarray):\n        x = x[0] if x.shape else x[()]\n    return x.decode() if isinstance(x, bytes) else str(x)\n\n\ndef read_meta(asset_id: str) -> dict:\n    \"\"\"Metadata, labels and the data layout of one file (no signal is read).\"\"\"\n    url = s3_url(asset_id)\n    f = h5py.File(remfile.File(url), \"r\")\n    es = f[\"acquisition/ElectricalSeries\"]\n    d = es[\"data\"]\n    iv = f[\"intervals/custom_intervals_table_name\"]\n    tags = [_text(t) for t in iv[\"tags\"][:]]\n    if \"tags_index\" in iv:\n        idx = iv[\"tags_index\"][:]\n        tags = [\",\".join(tags[(idx[i - 1] if i else 0):idx[i]]) for i in range(len(idx))]\n    e = f[\"general/extracellular_ephys/electrodes\"]\n    meta = {\n        \"asset_id\": asset_id, \"url\": url,\n        \"subject\": _text(f[\"general/subject/subject_id\"][()]),\n        \"group\": _text(f[\"identifier\"][()]),\n        \"kind\": _text(f[\"session_description\"][()]),\n        \"label\": _text(f[\"general/data_collection\"][()]),\n        \"notes\": _text(f[\"general/notes\"][()]),\n        \"start\": _text(f[\"session_start_time\"][()]),\n        \"n_samples\": d.shape[0], \"n_channels\": d.shape[1], \"dtype\": str(d.dtype),\n        \"chunks\": d.chunks, \"compression\": d.compression, \"offset\": d.id.get_offset(),\n        \"rate\": float(es[\"starting_time\"].attrs[\"rate\"]), \"t0\": float(es[\"starting_time\"][()]),\n        \"unit\": _text(d.attrs.get(\"unit\")), \"conversion\": float(d.attrs.get(\"conversion\", 1.0)),\n        \"filtering\": _text(es.attrs.get(\"filtering\", \"\")),\n        \"intervals\": pd.DataFrame({\"start\": iv[\"start_time\"][:], \"stop\": iv[\"stop_time\"][:], \"tag\": tags}),\n        \"electrodes\": pd.DataFrame({k: e[k][:] for k in (\"x\", \"y\", \"z\")} |\n                                   {\"location\": [_text(v) for v in e[\"location\"][:]]}),\n    }\n    f.close()\n    return meta\n\n\ndef read_all_meta(asset_ids, threads: int = 16) -> list[dict]:\n    with ThreadPoolExecutor(threads) as ex:\n        return list(ex.map(read_meta, asset_ids))\n\n\ndef read_rows(meta: dict, start: int, stop: int, threads: int = 16, piece: int = 32 * 2**20) -> np.ndarray:\n    \"\"\"Rows start:stop of the ElectricalSeries (contiguous float64) by parallel range requests.\"\"\"\n    start, stop = max(0, start), min(meta[\"n_samples\"], stop)\n    row = meta[\"n_channels\"] * 8\n    a, b = meta[\"offset\"] + start * row, meta[\"offset\"] + stop * row\n    edges = list(range(a, b, piece)) + [b]\n\n    def get(i):\n        for _ in range(5):\n            r = _session.get(meta[\"url\"], headers={\"Range\": f\"bytes={edges[i]}-{edges[i + 1] - 1}\"}, timeout=120)\n            if r.status_code == 206 and len(r.content) == edges[i + 1] - edges[i]:\n                return r.content\n        raise OSError(f\"range read failed for {meta['asset_id']}\")\n\n    with ThreadPoolExecutor(threads) as ex:\n        buf = b\"\".join(ex.map(get, range(len(edges) - 1)))\n    return np.frombuffer(buf, dtype=\"<f8\").reshape(stop - start, meta[\"n_channels\"])\n\n\ndef check_read(meta: dict, start: int = 100000, n: int = 3000) -> bool:\n    \"\"\"`read_rows` gives what h5py reads.\"\"\"\n    f = h5py.File(remfile.File(meta[\"url\"]), \"r\")\n    ref = f[\"acquisition/ElectricalSeries/data\"][start:start + n]\n    f.close()\n    return bool(np.array_equal(ref, read_rows(meta, start, start + n)))\n\n\n# ---------------------------------------------------------------- blocks and labels\n\ndef assign_blocks(labelled: list[dict]) -> pd.DataFrame:\n    \"\"\"One row per labelled block file, ordered by start time within each rat.\"\"\"\n    df = pd.DataFrame([{k: m[k] for k in (\"asset_id\", \"subject\", \"group\", \"label\", \"start\", \"n_samples\")}\n                       for m in labelled])\n    df[\"group\"] = df.group.str.replace(\" group\", \"\", regex=False).replace({\"tFUS\": \"tFUS\", \"sham\": \"sham\"})\n    df = df.sort_values([\"subject\", \"start\"]).reset_index(drop=True)\n    df[\"order\"] = df.groupby(\"subject\").cumcount()\n    df[\"block\"] = df.order.map(dict(enumerate(BLOCKS)))\n    df[\"minutes\"] = df.n_samples / RATE / 60\n    return df\n\n\ndef seizures(meta: dict, hemi: str) -> pd.DataFrame:\n    \"\"\"Seizures of one hemisphere, in seconds from the block start.\"\"\"\n    iv = meta[\"intervals\"]\n    s = iv[iv.tag == hemi][[\"start\", \"stop\"]].sort_values(\"start\") * MINUTES\n    s[\"duration\"] = s.stop - s.start\n    T = meta[\"n_samples\"] / RATE\n    s[\"truncated\"] = (s.start <= 1.5 / RATE * 1) | (s.stop >= T - 1.5 / RATE)\n    return s.reset_index(drop=True)\n\n\ndef merged_periods(meta: dict) -> np.ndarray:\n    \"\"\"Union of the ipsilateral and contralateral seizure periods (seconds), merged where they overlap.\"\"\"\n    iv = meta[\"intervals\"]\n    iv = iv[iv.tag.isin([\"ipsilateral\", \"contralateral\"])].sort_values(\"start\")\n    out = []\n    for a, b in (iv[[\"start\", \"stop\"]].to_numpy() * MINUTES):\n        if out and a <= out[-1][1]:\n            out[-1][1] = max(out[-1][1], b)\n        else:\n            out.append([a, b])\n    return np.array(out).reshape(-1, 2)\n\n\ndef block_metrics(meta: dict, hemi: str) -> dict:\n    \"\"\"Seizure Count, Percent Time in Seizure, Seizure Duration and Inter-Seizure Interval (M2).\"\"\"\n    s = seizures(meta, hemi)\n    T = meta[\"n_samples\"] / RATE\n    full = s[~s.truncated]\n    gaps = (s.start.to_numpy()[1:] - s.stop.to_numpy()[:-1]) if len(s) > 1 else np.array([])\n    onsets = np.diff(s.start.to_numpy()) if len(s) > 1 else np.array([])\n    return {\"count\": len(s), \"percent_time\": 100 * s.duration.sum() / T,\n            \"duration\": full.duration.mean() if len(full) else np.nan,\n            \"isi_gap\": gaps.mean() if len(gaps) else np.nan,\n            \"isi_onset\": onsets.mean() if len(onsets) else np.nan,\n            \"n_truncated\": int(s.truncated.sum())}\n\n\n# ---------------------------------------------------------------- statistics\n\ndef _contrast_rows(result, cells: pd.DataFrame) -> np.ndarray:\n    from patsy import build_design_matrices\n    di = result.model.data.design_info\n    return np.asarray(build_design_matrices([di], cells)[0])\n\n\ndef twoway(df: pd.DataFrame, value: str, a: str, b: str, subject: str, comparisons: list, rm: bool = False,\n           families: dict | None = None) -> tuple[pd.DataFrame, pd.DataFrame]:\n    \"\"\"Two-way ANOVA of `value` on factors a and b, with Bonferroni post hoc comparisons.\n\n    comparisons: list of (name, {a: x, b: y}, {a: x2, b: y2}, family). Within each family the p values\n    are multiplied by the family's size (capped at 1). rm=False: ordinary ANOVA (OLS, type II), post hoc\n    t on the pooled residual error and its df. rm=True: mixed model with a random intercept per subject;\n    main effects and interaction by Wald tests, post hoc by Wald z of the contrast.\n    \"\"\"\n    import statsmodels.formula.api as smf\n    from scipy import stats\n    from statsmodels.stats.anova import anova_lm\n    d = df.dropna(subset=[value]).copy()\n    formula = f\"{value} ~ C({a}) * C({b})\"\n    if not rm:\n        res = smf.ols(formula, d).fit()\n        table = anova_lm(res, typ=2)[[\"F\", \"PR(>F)\"]].dropna().rename(columns={\"PR(>F)\": \"p\"})\n        V, beta, dof = res.cov_params().to_numpy(), res.params.to_numpy(), res.df_resid\n    else:\n        res = smf.mixedlm(formula, d, groups=d[subject]).fit(reml=True)\n        names = list(res.fe_params.index)\n        beta = res.fe_params.to_numpy()\n        V = res.cov_params().loc[names, names].to_numpy()\n        rows = []\n        for term in (f\"C({a})\", f\"C({b})\", f\"C({a}):C({b})\"):\n            idx = [i for i, n in enumerate(names) if (n.startswith(term + \"[\") and \":\" not in n)\n                   or (\":\" in term and n.count(\":\") == 1 and n.startswith(f\"C({a})[\"))]\n            if \":\" not in term:\n                idx = [i for i, n in enumerate(names) if n.startswith(term + \"[\") and \":\" not in n]\n            if not idx:\n                continue\n            bb, VV = beta[idx], V[np.ix_(idx, idx)]\n            chi = float(bb @ np.linalg.pinv(VV) @ bb)\n            rows.append({\"term\": term, \"F\": chi / len(idx), \"p\": stats.chi2.sf(chi, len(idx))})\n        table = pd.DataFrame(rows).set_index(\"term\")\n        dof = None\n    out = []\n    for name, c1, c2, fam in comparisons:\n        x1 = _contrast_rows(res, pd.DataFrame([c1]))[0][: len(beta)]\n        x2 = _contrast_rows(res, pd.DataFrame([c2]))[0][: len(beta)]\n        c = x1 - x2\n        est, se = float(c @ beta), float(np.sqrt(c @ V @ c))\n        stat = est / se if se > 0 else np.nan\n        p = 2 * (stats.t.sf(abs(stat), dof) if dof is not None else stats.norm.sf(abs(stat)))\n        n1 = int(((d[a] == c1[a]) & (d[b] == c1[b])).sum())\n        n2 = int(((d[a] == c2[a]) & (d[b] == c2[b])).sum())\n        out.append({\"comparison\": name, \"family\": fam, \"diff\": est, \"stat\": stat, \"p_raw\": p, \"n1\": n1, \"n2\": n2})\n    post = pd.DataFrame(out)\n    if len(post):\n        size = post.groupby(\"family\").comparison.transform(\"size\")\n        post[\"p_family\"] = np.minimum(1.0, post.p_raw * size)\n        post[\"p_all\"] = np.minimum(1.0, post.p_raw * len(post))\n    return table, post\n\n\n# ---------------------------------------------------------------- spectra and PLI\n\ndef _notch(x: np.ndarray, fs: float) -> np.ndarray:\n    b, a = signal.iirnotch(60.0, 30.0, fs)\n    return signal.filtfilt(b, a, x, axis=0)\n\n\ndef band_powers(f: np.ndarray, p: np.ndarray) -> dict:\n    \"\"\"Band power (sum of PSD bins in the band), and the totals 3-300 Hz and 0-Nyquist.\"\"\"\n    df = f[1] - f[0]\n    out = {band: p[(f >= lo) & (f < hi)].sum(axis=0) * df for band, (lo, hi) in BANDS.items()}\n    out[\"total_3_300\"] = p[(f >= 3) & (f <= 300)].sum(axis=0) * df\n    out[\"total_all\"] = p.sum(axis=0) * df\n    return out\n\n\ndef welch_segments(x: np.ndarray, fs: float, periods: np.ndarray | None = None):\n    \"\"\"Welch PSD over the whole signal, or averaged over the given periods (seconds) weighted by\n    the number of windows each holds; periods shorter than one window are skipped.\"\"\"\n    nper = int(round(WELCH_S * fs))\n    if periods is None:\n        return signal.welch(x, fs, window=\"hann\", nperseg=nper, noverlap=nper // 2, axis=0)\n    acc, w, f = 0.0, 0, None\n    for a, b in periods:\n        i, j = int(a * fs), int(b * fs)\n        if j - i < nper:\n            continue\n        f, p = signal.welch(x[i:j], fs, window=\"hann\", nperseg=nper, noverlap=nper // 2, axis=0)\n        k = 1 + (j - i - nper) // (nper // 2)\n        acc, w = acc + p * k, w + k\n    if f is None:\n        return None, None\n    return f, acc / w\n\n\ndef pli(phase_a: np.ndarray, phase_b: np.ndarray) -> np.ndarray:\n    \"\"\"PLI between each column of a and each column of b over axis 0 (Eq. 2): shape (na, nb).\"\"\"\n    sa, ca = np.sin(phase_a), np.cos(phase_a)\n    sb, cb = np.sin(phase_b), np.cos(phase_b)\n    # sin(a - b) = sin a cos b - cos a sin b\n    out = np.empty((phase_a.shape[1], phase_b.shape[1]))\n    for i in range(phase_a.shape[1]):\n        out[i] = np.abs(np.sign(sa[:, [i]] * cb - ca[:, [i]] * sb).mean(axis=0))\n    return out\n\n\ndef band_sos(band: str, fs: float):\n    lo, hi = BANDS[band]\n    return signal.butter(4, [lo, hi], btype=\"bandpass\", fs=fs, output=\"sos\")\n\n\ndef process_block(meta: dict, rows_per_read: int = 1_000_000) -> dict:\n    \"\"\"One labelled EEG block: PSD of channels 8 and 25 (whole block, seizure periods per hemisphere,\n    merged seizure periods), the 30-80 Hz power inside and outside the labels (and with the labels\n    shifted, a clock check), and the seizure PLI per band for S1 and non-S1 pairs.\"\"\"\n    n = meta[\"n_samples\"]\n    car2 = np.empty((n, 2))\n    dec = []\n    for s in range(0, n, rows_per_read):\n        x = read_rows(meta, s, s + rows_per_read)\n        x = x - x.mean(axis=1, keepdims=True)                 # common average reference\n        car2[s:s + len(x)] = x[:, [IPSI_CH - 1, CONTRA_CH - 1]]\n        dec.append(x.astype(np.float32))\n    full = np.concatenate(dec)\n    del dec\n    car2 = _notch(car2, RATE)\n    out = {\"asset_id\": meta[\"asset_id\"]}\n    out[\"psd_block\"] = welch_segments(car2, RATE)\n    per = {h: seizures(meta, h)[[\"start\", \"stop\"]].to_numpy() for h in (\"ipsilateral\", \"contralateral\")}\n    merged = merged_periods(meta)\n    out[\"psd_seiz_ipsi\"] = welch_segments(car2[:, [0]], RATE, per[\"ipsilateral\"])\n    out[\"psd_seiz_contra\"] = welch_segments(car2[:, [1]], RATE, per[\"contralateral\"])\n    out[\"psd_seiz_merged\"] = welch_segments(car2, RATE, merged)\n    out[\"periods_merged\"] = merged\n    # clock check: gamma power in 1 s bins, inside against outside the labels, at shifts\n    sos = signal.butter(4, [30, 80], btype=\"bandpass\", fs=RATE, output=\"sos\")\n    g = signal.sosfiltfilt(sos, car2, axis=0) ** 2\n    nb = int(n // RATE)\n    gp = g[: int(nb * RATE)].reshape(nb, -1, 2).mean(axis=1) if False else np.array(\n        [g[int(i * RATE):int((i + 1) * RATE)].mean(axis=0) for i in range(nb)])\n    out[\"gamma_1s\"] = gp\n    del g\n    # decimate the 32 channels for the PLI\n    fs_d = RATE / DECIMATE\n    xd = signal.decimate(full, DECIMATE, ftype=\"iir\", zero_phase=True, axis=0)\n    del full\n    b, a = signal.iirnotch(60.0, 30.0, fs_d)\n    xd = signal.filtfilt(b, a, xd, axis=0).astype(np.float32)\n    sos_bp = signal.butter(4, [3, 300], btype=\"bandpass\", fs=fs_d, output=\"sos\")\n    xd = signal.sosfiltfilt(sos_bp, xd, axis=0).astype(np.float32)\n    ii = [c - 1 for c in S1_IPSI + NONS1_IPSI]\n    cc = [c - 1 for c in S1_CONTRA + NONS1_CONTRA]\n    res = {}\n    for band in BANDS:\n        y = signal.sosfiltfilt(band_sos(band, fs_d), xd, axis=0)\n        segs = [(int(a0 * fs_d), int(b0 * fs_d)) for a0, b0 in merged if (b0 - a0) >= 1.0]\n        per_seiz, cat = [], []\n        for i, j in segs:\n            ph = np.angle(signal.hilbert(y[max(0, i - int(fs_d)):j + int(fs_d)], axis=0))\n            ph = ph[i - max(0, i - int(fs_d)): i - max(0, i - int(fs_d)) + (j - i)]\n            m = pli(ph[:, ii], ph[:, cc])\n            per_seiz.append(m)\n            cat.append(ph[:, ii + cc])\n        if per_seiz:\n            phc = np.concatenate(cat)\n            res[band] = {\"per_seizure\": np.mean(per_seiz, axis=0),\n                         \"concat\": pli(phc[:, : len(ii)], phc[:, len(ii):]), \"n\": len(per_seiz)}\n        else:\n            res[band] = None\n    out[\"pli\"] = res\n    return out\n\n\ndef pair_means(m: np.ndarray) -> dict:\n    \"\"\"Mean PLI over S1 pairs (left S1 with right S1) and over non-S1 pairs, from a matrix whose rows\n    are ipsilateral channels S1_IPSI + NONS1_IPSI and columns contralateral S1_CONTRA + NONS1_CONTRA.\"\"\"\n    k = len(S1_IPSI)\n    return {\"S1\": float(m[:k, :k].mean()), \"nonS1\": float(m[k:, k:].mean())}\n"
}
```

```
File created successfully at: entries/001683-gao-2026/tfus.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026 && python - <<'EOF'
s=open('tfus.py').read()
old=s[s.index('        for term in (f"C({a})", f"C({b})", f"C({a}):C({b})"):'):s.index('            bb, VV = beta[idx]')]
new='''        for term in (f"C({a})", f"C({b})", f"C({a}):C({b})"):
            if ":" in term:
                idx = [i for i, n in enumerate(names) if ":" in n]
            else:
                idx = [i for i, n in enumerate(names) if n.startswith(term + "[") and ":" not in n]
            if not idx:
                continue
'''
s=s.replace(old,new)
s=s.replace('''    gp = g[: int(nb * RATE)].reshape(nb, -1, 2).mean(axis=1) if False else np.array(
        [g[int(i * RATE):int((i + 1) * RATE)].mean(axis=0) for i in range(nb)])''','''    gp = np.array([g[int(i * RATE):int((i + 1) * RATE)].mean(axis=0) for i in range(nb)])''')
s=s.replace('''    s["truncated"] = (s.start <= 1.5 / RATE * 1) | (s.stop >= T - 1.5 / RATE)''','''    s["truncated"] = (s.start <= 1.5 / RATE) | (s.stop >= T - 1.5 / RATE)''')
open('tfus.py','w').write(s)
EOF
grep -n "for term" -A8 tfus.py
```

```
257:        for term in (f"C({a})", f"C({b})", f"C({a}):C({b})"):
258-            if ":" in term:
259-                idx = [i for i, n in enumerate(names) if ":" in n]
260-            else:
261-                idx = [i for i, n in enumerate(names) if n.startswith(term + "[") and ":" not in n]
262-            if not idx:
263-                continue
264-            bb, VV = beta[idx], V[np.ix_(idx, idx)]
265-            chi = float(bb @ np.linalg.pinv(VV) @ bb)
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026 && python - <<'EOF'
s=open('tfus.py').read()
s=s.replace('''    formula = f"{value} ~ C({a}) * C({b})"''','''    formula = f"{value} ~ C({a}, Sum) * C({b}, Sum)"''')
s=s.replace('''        for term in (f"C({a})", f"C({b})", f"C({a}):C({b})"):''','''        for term in (f"C({a}, Sum)", f"C({b}, Sum)", f"C({a}, Sum):C({b}, Sum)"):''')
open('tfus.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cd entries/001683-gao-2026 && python -c "
import tfus, numpy as np, pandas as pd
rng=np.random.default_rng(0)
rows=[]
for s in range(8):
  u=rng.normal()
  for h in ['i','c']:
    for b in ['b0','b1','b2']:
      rows.append(dict(rat=s,h=h,blk=b,v=u+(1.0 if b=='b2' else 0)+rng.normal()*0.5))
df=pd.DataFrame(rows)
comps=[(f'{h} b0-{b}',{'h':h,'blk':'b0'},{'h':h,'blk':b},h) for h in 'ic' for b in ['b1','b2']]
for rm in [False,True]:
  t,p=tfus.twoway(df,'v','h','blk','rat',comps,rm=rm); print(t); print(p.round(4))
"
```

```
Exit code 1
/bin/bash: line 1: cd: entries/001683-gao-2026: No such file or directory
Traceback (most recent call last):
  File "<string>", line 13, in <module>
    t,p=tfus.twoway(df,'v','h','blk','rat',comps,rm=rm); print(t); print(p.round(4))
        ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "entries/001683-gao-2026/tfus.py", line 271, in twoway
    x1 = _contrast_rows(res, pd.DataFrame([c1]))[0][: len(beta)]
         ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "entries/001683-gao-2026/tfus.py", line 229, in _contrast_rows
    di = result.model.data.design_info
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'PandasData' object has no attribute 'design_info'
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('tfus.py').read()
s=s.replace('''    formula = f"{value} ~ C({a}) * C({b})"''','''    rhs = f"C({a}, Sum) * C({b}, Sum)"
    formula = f"{value} ~ {rhs}"
    from patsy import dmatrix
    di = dmatrix(rhs, d).design_info''')
s=s.replace('''        for term in (f"C({a})", f"C({b})", f"C({a}):C({b})"):''','''        for term in (f"C({a}, Sum)", f"C({b}, Sum)", f"C({a}, Sum):C({b}, Sum)"):''')
s=s.replace('''def _contrast_rows(result, cells: pd.DataFrame) -> np.ndarray:
    from patsy import build_design_matrices
    di = result.model.data.design_info
    return''','''def _contrast_rows(di, cells: pd.DataFrame) -> np.ndarray:
    from patsy import build_design_matrices
    return''')
s=s.replace("_contrast_rows(res, ","_contrast_rows(di, ")
open('tfus.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cd entries/001683-gao-2026 && python -c "
import tfus, numpy as np, pandas as pd
rng=np.random.default_rng(0)
rows=[]
for s in range(8):
  u=rng.normal()
  for h in ['i','c']:
    for b in ['b0','b1','b2']:
      rows.append(dict(rat=s,h=h,blk=b,v=u+(1.0 if b=='b2' else 0)+rng.normal()*0.5))
df=pd.DataFrame(rows)
comps=[(f'{h} b0-{b}',{'h':h,'blk':'b0'},{'h':h,'blk':b},h) for h in 'ic' for b in ['b1','b2']]
for rm in [False,True]:
  t,p=tfus.twoway(df,'v','h','blk','rat',comps,rm=rm); print(t); print(p.round(4))
print(df.groupby(['h','blk']).v.mean())
"
```

```
F         p
C(h, Sum)              0.439756  0.510864
C(blk, Sum)            6.611121  0.003190
C(h, Sum):C(blk, Sum)  0.050766  0.950559
  comparison family    diff    stat   p_raw  n1  n2  p_family   p_all
0    i b0-b1      i  0.0858  0.1607  0.8731   8   8    1.0000  1.0000
1    i b0-b2      i -1.1158 -2.0896  0.0427   8   8    0.0855  0.1710
2    c b0-b1      c  0.3232  0.6052  0.5483   8   8    1.0000  1.0000
3    c b0-b2      c -1.0313 -1.9312  0.0602   8   8    0.1204  0.2409
                               F             p
term                                          
C(h, Sum)               3.313064  6.873125e-02
C(blk, Sum)            49.807346  2.338539e-22
C(h, Sum):C(blk, Sum)   0.382468  6.821760e-01
  comparison family    diff    stat   p_raw  n1  n2  p_family   p_all
0    i b0-b1      i  0.0858  0.4410  0.6592   8   8    1.0000  1.0000
1    i b0-b2      i -1.1158 -5.7356  0.0000   8   8    0.0000  0.0000
2    c b0-b1      c  0.3232  1.6611  0.0967   8   8    0.1934  0.3867
3    c b0-b2      c -1.0313 -5.3009  0.0000   8   8    0.0000  0.0000
h  blk
[... 7 more lines not kept]
```

**Agent**

Stats helper works on synthetic data. Now developing the seizure-metric analysis on the labels.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/001683-gao-2026 && cat > $TMPDIR/dev1.py <<'EOF'
import tfus, pandas as pd, numpy as np, pickle, time
t=time.time()
a=tfus.list_assets()
metas=tfus.read_all_meta(a.asset_id.tolist())
print(time.time()-t)
pickle.dump(metas,open('/tmp/claude-1001/metas.pkl','wb'))
EOF
python $TMPDIR/dev1.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dev1.py", line 1, in <module>
    import tfus, pandas as pd, numpy as np, pickle, time
ModuleNotFoundError: No module named 'tfus'
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/001683-gao-2026 && PYTHONPATH=. python $TMPDIR/dev1.py
```

```
193.3562250137329
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/001683-gao-2026 && cat > $TMPDIR/dev2.py <<'EOF'
import tfus, pandas as pd, numpy as np, pickle
pd.set_option("display.width",250); pd.set_option("display.max_rows",200)
metas=pickle.load(open('/tmp/claude-1001/metas.pkl','rb'))
lab=[m for m in metas if m['kind']=='Labeled_data']
bl=tfus.assign_blocks(lab)
print(bl[['subject','group','label','start','block','minutes']].to_string())
M={m['asset_id']:m for m in lab}
rows=[]
for _,r in bl.iterrows():
    for h in ['ipsilateral','contralateral']:
        rows.append(dict(subject=r.subject,group=r.group,block=r.block,hemi=h,**tfus.block_metrics(M[r.asset_id],h)))
met=pd.DataFrame(rows)
print(met.groupby(['group','hemi','block'])[['count','percent_time','duration','isi_gap','isi_onset','n_truncated']].mean().round(2))
# percent changes tFUS
t=met[met.group=='tFUS']
for col in ['count','percent_time','isi_gap','isi_onset','duration']:
    sub=t if not col.startswith('isi') else t[~t.subject.isin(['BH634','BH638'])]
    g=sub.groupby(['hemi','block'])[col].mean().unstack()
    a=(g.div(g['baseline'],axis=0)-1)*100
    w=sub.pivot_table(index=['hemi','subject'],columns='block',values=col)
    b=((w.div(w['baseline'],axis=0)-1)*100).groupby('hemi').mean()
    print(col,'\n',a.round(1),'\n',b.round(1))
EOF
python $TMPDIR/dev2.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dev2.py", line 1, in <module>
    import tfus, pandas as pd, numpy as np, pickle
ModuleNotFoundError: No module named 'tfus'
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/001683-gao-2026 && PYTHONPATH=. python $TMPDIR/dev2.py
```

```
subject group           label                             start      block    minutes
0    BH624  tFUS  BH624_BASELINE  2024-12-03T19:36:37.000000-05:00   baseline  62.537073
1    BH624  tFUS    BH624_CC_1Hz  2024-12-03T20:40:11.000000-05:00  condition  62.544063
2    BH624  tFUS     BH624_post1  2024-12-03T21:44:00.000000-05:00      post1  62.537073
3    BH624  tFUS     BH624_post2  2024-12-03T22:47:57.000000-05:00      post2  62.606978
4    BH626  tFUS  BH626_BASELINE  2024-11-29T21:28:13.000000-05:00   baseline  62.583210
5    BH626  tFUS    BH626_CC_1Hz  2024-11-29T22:32:19.000000-05:00  condition  62.518897
6    BH626  tFUS     BH626_post1  2024-11-29T23:36:55.000000-05:00      post1  62.523092
7    BH626  tFUS     BH626_post2  2024-11-30T00:40:54.000000-05:00      post2  62.523092
8    BH634  tFUS  BH634_BASELINE  2024-12-11T20:43:57.000000-05:00   baseline  62.565035
9    BH634  tFUS    BH634_CC_1Hz  2024-12-11T21:47:22.000000-05:00  condition  62.513305
10   BH634  tFUS     BH634_post1  2024-12-11T22:51:25.000000-05:00      post1  62.514703
11   BH634  tFUS     BH634_post2  2024-12-11T23:54:55.000000-05:00      post2  62.528684
12   BH635  sham  BH635_BASELINE  2024-12-13T21:57:54.000000-05:00   baseline  62.523092
13   BH635  sham      BH635_SHAM  2024-12-13T23:05:29.000000-05:00  condition  62.727214
14   BH635  sham      BH635_SHAM  2024-12-14T00:13:37.000000-05:00      post1  63.136858
15   BH635  sham     BH636_post1  2024-12-14T01:20:03.000000-05:00      post2  62.538471
16   BH635  sham     BH635_post2  2024-12-14T02:25:50.000000-05:00      post3  62.510509
17   BH638  tFUS  BH638_BASELINE  2024-12-19T19:58:47.000000-05:00   baseline  62.525888
18   BH638  tFUS    BH638_CC_1Hz  2024-12-19T21:02:18.000000-05:00  condition  62.531480
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/build && cat > $TMPDIR/build/nbtools.py <<'EOF'
import nbformat
def build(path, cells):
    nb = nbformat.v4.new_notebook()
    nb.metadata = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}}
    out = []
    for c in cells:
        kind, src = c[0], c[1].strip("\n")
        tags = c[2] if len(c) > 2 else None
        cell = nbformat.v4.new_markdown_cell(src) if kind == "md" else nbformat.v4.new_code_cell(src)
        if tags:
            cell.metadata["tags"] = tags
        out.append(cell)
    nb.cells = out
    nbformat.write(nb, path)
EOF
echo ok; date -u
```

```
ok
Tue Nov  3 08:28:46 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build/nb1.py",
 "content": "import sys\nsys.path.insert(0, \"/tmp/claude-1001/build\")\nfrom nbtools import build\n\nH = \"entries/001683-gao-2026/\"\ncells = []\nmd = lambda s, t=None: cells.append((\"md\", s, t))\ncode = lambda s, t=None: cells.append((\"code\", s, t))\n\nmd(r\"\"\"\n# Gao et al. (2026) on dandiset 001683: seizure metrics from the labels\n\n**Paper.** Gao H, Frake A, Durand DM, He B (2026). Transcranial focused ultrasound stimulation\ntargeting white matter inhibits seizures in a rat model of epilepsy. *IEEE Trans Neural Syst Rehabil\nEng* 34, 251-259. [doi:10.1109/tnsre.2025.3644273](https://doi.org/10.1109/tnsre.2025.3644273). The\nclaims file was written from the NIH author manuscript (PMC12848950) and the supplement.\n\n**Dandiset.** [DANDI:001683](https://dandiarchive.org/dandiset/001683/0.260109.2104), version\n0.260109.2104. The paper cites no version (its Data Availability statement gives the dandiset's\naddress only). This is the only published version and so the most recent; the draft lists the same\n318 assets and size.\n\nThis is the first of three notebooks. It tests the claims on seizure count, percent time in\nseizure, seizure duration and inter-seizure interval (Figs. 2 and 3), which use only the seizure\nlabels the dandiset holds. `eeg_blocks.ipynb` tests the band power, asymmetry index and seizure PLI\nclaims (Figs. 4, 6, S4, S5, S7); `wild_type.ipynb` the evoked potentials and wild-type PLI (Fig. 5).\n\n| Claim | Notebook | Tested here |\n|---|---|---|\n| fig2c-sham-duration-stable | this | yes |\n| fig2d-seizures-under-two-minutes | this | yes |\n| fig2e-sham-count-stable | this | yes |\n| fig2f-sham-percent-time-post3 | this | yes |\n| fig3a-count-reduction | this | yes |\n| fig3a-count-sham-vs-tfus | this | yes |\n| fig3b-percent-time-reduction | this | yes |\n| fig3b-sham-percent-time-no-change | this | yes |\n| fig3b-percent-time-sham-vs-tfus | this | yes |\n| fig3c-interval-increase | this | yes |\n| fig3c-interval-sham-vs-tfus | this | yes |\n| fig3d-duration-decline | this | yes |\n| Figs. 4, 6, S4, S5, S7 (seven claims) | eeg_blocks.ipynb | no |\n| Fig. 5 (three claims) | wild_type.ipynb | no |\n\"\"\")\n\ncode(r\"\"\"\nimport hashlib\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport tfus\n\nwarnings.filterwarnings(\"ignore\")\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 300)\n\nstarted = time.time()\nassets = tfus.list_assets()\ninfo = tfus.version_info()\nprint(f\"dandiset {tfus.DANDISET_ID} version {tfus.DANDISET_VERSION}: {len(assets)} assets, \"\n      f\"{assets['size'].sum() / 1e9:.1f} GB; archive summary: {info['metadata']['assetsSummary']['numberOfSubjects']} subjects, \"\n      f\"{info['metadata']['assetsSummary']['numberOfFiles']} files\")\nbig = assets[assets[\"size\"] > 2e9]\nmetas = tfus.read_all_meta(big.asset_id.tolist())\nlab = [m for m in metas if m[\"kind\"] == \"Labeled_data\"]\nprint(f\"files over 2 GB: {len(big)}; of them labelled EEG blocks: {len(lab)}; read in {time.time() - started:.0f} s\")\n\"\"\")\n\nmd(\"\"\"\n## Data check\n\nEach check of the metadata against the values is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\nblocks = tfus.assign_blocks(lab)\nM = {m[\"asset_id\"]: m for m in lab}\nprint(\"Kinds, groups and notes of the files read:\")\nprint(pd.Series([(m[\"kind\"], m[\"group\"], m[\"notes\"]) for m in lab]).value_counts().to_string())\nprint(\"\\nRats per group:\", blocks.groupby(\"group\").subject.nunique().to_dict(), \"(paper: 10 tFUS, 6 sham)\")\nprint(\"\\nBlock files per rat, and the label each file carries in general/data_collection, in time order:\")\nprint(blocks.pivot(index=\"subject\", columns=\"block\", values=\"label\").fillna(\"\").to_string())\nprint(\"\\nSampling rates:\", sorted({m[\"rate\"] for m in lab}), \"Hz; channels:\", sorted({m[\"n_channels\"] for m in lab}),\n      \"; unit:\", sorted({m[\"unit\"] for m in lab}), \"; conversion:\", sorted({m[\"conversion\"] for m in lab}))\nprint(\"Storage: chunks\", sorted({str(m[\"chunks\"]) for m in lab}), \"compression\", sorted({str(m[\"compression\"]) for m in lab}))\nprint(f\"Block length: {blocks.minutes.min():.2f} to {blocks.minutes.max():.2f} min (paper: ~62.5 min)\")\ngaps = blocks.assign(t=pd.to_datetime(blocks.start, utc=True)).groupby(\"subject\").t.diff().dt.total_seconds() / 60\nprint(f\"Start-to-start time between consecutive blocks of a rat: {gaps.min():.1f} to {gaps.max():.1f} min\")\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nTen tFUS rats with four blocks each (baseline, CC_1Hz, post1, post2) and six sham rats with five\n(baseline, SHAM, post1, post2, post3), as in the paper. Blocks follow each other at 63 to 68 min.\nOne rat's labels do not match its files: BH635 has two files labelled `BH635_SHAM`, then one\nlabelled `BH636_post1` (another rat's number) and one `BH635_post2`, and none `post3`. Its five\nfiles are taken here in time order (baseline, condition, post 1, post 2, post 3), as the other\nsham rats' five are; the reading that follows the labels instead (the second SHAM file left out,\n`BH636_post1` as post 1, `BH635_post2` as post 2, no post 3) is shown as a variant where it\nbears on a claim. The session of BH649's last block is named `ses-None` in its file name.\n\"\"\")\n\ncode(r\"\"\"\niv_all = pd.concat([M[a][\"intervals\"].assign(asset_id=a) for a in blocks.asset_id])\niv_all = iv_all.merge(blocks[[\"asset_id\", \"subject\", \"block\", \"minutes\", \"n_samples\"]], on=\"asset_id\")\nprint(\"Label tags:\", iv_all.tag.value_counts().to_dict())\nnos = iv_all[iv_all.tag == \"no_seizure\"]\nprint(\"Blocks with a 'no_seizure' row (start, stop):\", nos[[\"subject\", \"block\", \"start\", \"stop\"]].to_dict(\"records\"))\nreal = iv_all[iv_all.tag != \"no_seizure\"]\nprint(f\"\\nLargest stop time in each file, against the block length: stop/length in minutes \"\n      f\"{(real.groupby('asset_id').stop.max() / real.groupby('asset_id').minutes.first()).describe().round(3).to_dict()}\")\nprint(f\"Largest stop over all files: {real.stop.max():.2f}; shortest block: {blocks.minutes.min():.2f} min = {blocks.minutes.min() * 60:.0f} s\")\nprint(\"So the label times are minutes: in seconds every seizure would fall in the first 63 s of a 3750 s block.\")\nd = (real.stop - real.start) * 60\nprint(f\"Label durations, read as minutes: {d.min():.1f} to {d.max():.1f} s, median {d.median():.1f} s; \"\n      f\"{(d < 10).sum()} under the 10 s minimum of Methods C\")\nprint(f\"Rows with stop before start: {(real.stop < real.start).sum()}\")\nfirst = real.groupby([\"asset_id\", \"tag\"]).start.min()\nprint(f\"Seizures starting at the first sample (start below 2 samples): {(real.start * 60 < 2 / tfus.RATE).sum()}; \"\n      f\"ending at the last sample: {((real.stop * 60) > (real.n_samples / tfus.RATE - 2 / tfus.RATE)).sum()}\")\npairs = real.groupby([\"asset_id\", \"tag\"]).size().unstack()\nprint(f\"Files whose ipsilateral and contralateral counts differ: {(pairs.ipsilateral != pairs.contralateral).sum()} of {len(pairs)}\")\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nThe label table gives start and stop times in minutes, not in the seconds NWB prescribes. The\nnotebook `eeg_blocks.ipynb` checks this against the EEG: the 30 to 80 Hz power of the labelling\nchannels is compared inside and outside the labels, with the labels read as minutes and shifted\nin time. Every metric here uses the labels in seconds after multiplying by 60.\n\"\"\")\n\ncode(r\"\"\"\n# Recordings deposited twice: identical label tables, sample counts, or identical samples.\nsig = {}\nfor a in blocks.asset_id:\n    m = M[a]\n    x = tfus.read_rows(m, 2_000_000, 2_002_000)\n    sig[a] = (hashlib.md5(x.tobytes()).hexdigest(), m[\"n_samples\"],\n              hashlib.md5(m[\"intervals\"].round(6).to_csv().encode()).hexdigest())\ns = pd.DataFrame(sig, index=[\"samples_md5\", \"n_samples\", \"labels_md5\"]).T\nprint(\"Files sharing 2000 samples at row 2,000,000:\", int(s.samples_md5.duplicated(keep=False).sum()))\nprint(\"Files sharing a label table:\", int(s.labels_md5.duplicated(keep=False).sum()))\ndup_n = s[s.n_samples.duplicated(keep=False)].join(blocks.set_index(\"asset_id\")[[\"subject\", \"block\"]])\nprint(\"Files sharing a sample count (same length is common at this rate; listed for inspection):\")\nprint(dup_n.sort_values(\"n_samples\")[[\"n_samples\", \"subject\", \"block\"]].to_string())\nprint(\"read_rows agrees with h5py on a slice:\", tfus.check_read(lab[0]))\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nNo two block files share samples or label tables, so no recording is deposited twice. Files that\nshare a sample count differ in their samples.\n\n## Seizure metrics\n\nPer rat, hemisphere and block (M2 of the claims file, Methods C): Seizure Count; Percent Time in\nSeizure, summed durations over the block length; Seizure Duration, the mean duration of seizures\nthat neither start at the first sample nor end at the last; and Inter-Seizure Interval, the mean\ninterval between neighbouring seizures, computed both as the gap from one seizure's end to the next\none's start (`isi_gap`) and from onset to onset (`isi_onset`). The paper's words, \"time between\nneighboring seizures\", favour the gap. For the interval the two tFUS rats with a block without\nseizures are left out (Methods C, \"two rats were excluded because they had conditions without\nseizure occurrence\").\n\"\"\")\n\ncode(r\"\"\"\ndef metrics_table(blocks):\n    rows = []\n    for _, r in blocks.iterrows():\n        for h in (\"ipsilateral\", \"contralateral\"):\n            rows.append({\"subject\": r.subject, \"group\": r.group, \"block\": r.block, \"hemi\": h,\n                         **tfus.block_metrics(M[r.asset_id], h)})\n    return pd.DataFrame(rows)\n\nmet = metrics_table(blocks)\nno_seiz = sorted(met[(met[\"count\"] == 0)].subject.unique())\nprint(\"Rat-blocks without seizures:\", met[met[\"count\"] == 0][[\"subject\", \"group\", \"block\", \"hemi\"]].to_dict(\"records\"))\nprint(\"Rats left out of the inter-seizure interval:\", no_seiz, \"(Methods C: two rats; Fig. 3C: N = 8 tFUS)\")\nmet.loc[met.subject.isin(no_seiz), [\"isi_gap\", \"isi_onset\"]] = np.nan\nprint(\"Truncated seizures left out of the duration:\", int(met.n_truncated.sum()))\nprint(\"\\nGroup means per hemisphere and block:\")\nprint(met.groupby([\"group\", \"hemi\", \"block\"])[[\"count\", \"percent_time\", \"duration\", \"isi_gap\", \"isi_onset\"]].mean().round(2).to_string())\nprint(\"\\nRanges over rat-blocks:\", {c: (round(met[c].min(), 2), round(met[c].max(), 2)) for c in [\"count\", \"percent_time\", \"duration\", \"isi_gap\", \"isi_onset\"]})\n\n# The label-following reading of BH635's blocks.\nalt = blocks.copy()\nb635 = alt[alt.subject == \"BH635\"].sort_values(\"start\").index\nalt = alt.drop(index=b635[2])\nalt.loc[b635[3], \"block\"], alt.loc[b635[4], \"block\"] = \"post1\", \"post2\"\nmet_alt = metrics_table(alt)\nmet_alt.loc[met_alt.subject.isin(no_seiz), [\"isi_gap\", \"isi_onset\"]] = np.nan\n\"\"\")\n\ncode(r\"\"\"\n# Statistics: two-way ANOVA and Bonferroni post hoc tests, under the readings of M3.\nBL = [\"baseline\", \"condition\", \"post1\", \"post2\", \"post3\"]\nNAMES = {\"baseline\": \"baseline\", \"condition\": \"condition\", \"post1\": \"post 1\", \"post2\": \"post 2\", \"post3\": \"post 3\"}\n\ndef sham_tests(df, value):\n    # Fig. 2: hemisphere by block, sham rats, five blocks. Post hoc: each pair of blocks within each\n    # hemisphere (family 'blocks', 20 comparisons) and the hemispheres at each block (family 'hemi', 5).\n    comps = []\n    for h in (\"ipsilateral\", \"contralateral\"):\n        for i, b1 in enumerate(BL):\n            for b2 in BL[i + 1:]:\n                comps.append((f\"{h[:6]} {b1}-{b2}\", {\"hemi\": h, \"block\": b1}, {\"hemi\": h, \"block\": b2}, \"blocks\"))\n    for b in BL:\n        comps.append((f\"ipsi-contra {b}\", {\"hemi\": \"ipsilateral\", \"block\": b}, {\"hemi\": \"contralateral\", \"block\": b}, \"hemi\"))\n    out = {}\n    for rm in (False, True):\n        table, post = tfus.twoway(df, value, \"hemi\", \"block\", \"subject\", comps, rm=rm)\n        out[\"repeated\" if rm else \"ordinary\"] = (table, post)\n    return out\n\ndef group_tests(df, value, hemi):\n    # Fig. 3 and 4: group by block per hemisphere, blocks baseline to post 2. Families (M3):\n    # 'within' each block against baseline in each group (6), 'between' sham against tFUS at each block (4).\n    d = df[(df.hemi == hemi) & (df.block != \"post3\")]\n    comps = [(f\"{g} baseline-{b}\", {\"group\": g, \"block\": \"baseline\"}, {\"group\": g, \"block\": b}, \"within\")\n             for g in (\"sham\", \"tFUS\") for b in BL[1:4]]\n    comps += [(f\"sham-tFUS {b}\", {\"group\": \"sham\", \"block\": b}, {\"group\": \"tFUS\", \"block\": b}, \"between\") for b in BL[:4]]\n    out = {}\n    for rm in (False, True):\n        table, post = tfus.twoway(d, value, \"group\", \"block\", \"subject\", comps, rm=rm)\n        out[\"repeated\" if rm else \"ordinary\"] = (table, post)\n    return out\n\ndef show(out, keep=None):\n    for k, (table, post) in out.items():\n        print(f\"  [{k}] main effects:\", {i: f\"F={r.F:.2f}, p={r.p:.3g}\" for i, r in table.iterrows()})\n        p = post if keep is None else post[post.comparison.isin(keep)]\n        print(p[[\"comparison\", \"family\", \"diff\", \"stat\", \"p_raw\", \"p_family\", \"p_all\"]].round(4).to_string(index=False))\n\ndef pct_change(df, value, group=\"tFUS\"):\n    # M4: (a) the group mean of the block over the group mean at baseline, minus 1;\n    # (b) the mean over rats of each rat's change from its own baseline.\n    d = df[df.group == group]\n    g = d.groupby([\"hemi\", \"block\"])[value].mean().unstack()\n    a = (g.div(g[\"baseline\"], axis=0) - 1) * 100\n    w = d.pivot_table(index=[\"hemi\", \"subject\"], columns=\"block\", values=value)\n    b = ((w.div(w[\"baseline\"], axis=0) - 1) * 100).groupby(\"hemi\").mean()\n    cols = [c for c in BL[1:4]]\n    return a[cols], b[cols]\n\"\"\")\n\n# ---- fig2c\nmd(\"\"\"\n## fig2c-sham-duration-stable\n\n> In the sham group, seizure durations from the ipsilateral and contralateral hemispheres do not\n> differ significantly across time blocks or between hemispheres.\n\nA claim of absence: two-way ANOVA (hemisphere by block) with Bonferroni post hoc tests at\nP < 0.05, with one value per seizure (reading a, as the Fig. 2C legend says each point is one\nseizure) or one mean per rat (reading b), each under the ordinary and repeated-measures readings.\n\"\"\")\n\ncode(r\"\"\"\nsham = blocks[blocks.group == \"sham\"]\nseiz = []\nfor _, r in sham.iterrows():\n    for h in (\"ipsilateral\", \"contralateral\"):\n        s = tfus.seizures(M[r.asset_id], h)\n        s = s[~s.truncated]\n        seiz.append(s.assign(subject=r.subject, block=r.block, hemi=h))\nseiz = pd.concat(seiz, ignore_index=True)\nprint(f\"Sham seizures: {len(seiz)} (ipsilateral {sum(seiz.hemi == 'ipsilateral')}, contralateral {sum(seiz.hemi == 'contralateral')}); \"\n      f\"duration {seiz.duration.min():.1f} to {seiz.duration.max():.1f} s\")\nprint(seiz.groupby([\"hemi\", \"block\"]).duration.agg([\"size\", \"mean\", \"median\"]).round(1).unstack(0).to_string())\nres2c = {}\nfor reading, df in ((\"a, per seizure\", seiz), (\"b, per-rat means\", met[met.group == \"sham\"])):\n    print(f\"\\nReading {reading}:\")\n    out = sham_tests(df, \"duration\")\n    res2c[reading] = out\n    for k, (table, post) in out.items():\n        sig = post[(post.p_family < 0.05) | (post.p_all < 0.05)]\n        print(f\"  [{k}] main effects:\", {i: f\"F={r.F:.2f}, p={r.p:.3g}\" for i, r in table.iterrows()})\n        print(f\"  [{k}] post hoc significant (own family or all): {len(sig)} of {len(post)}\")\n        print(sig[[\"comparison\", \"diff\", \"p_raw\", \"p_family\", \"p_all\"]].round(4).to_string(index=False) if len(sig) else \"  none\")\n\"\"\", [\"claim:fig2c-sham-duration-stable\"])\n\ncode(r\"\"\"\nfig, ax = plt.subplots(figsize=(7, 3))\nfor k, h in enumerate((\"ipsilateral\", \"contralateral\")):\n    d = seiz[seiz.hemi == h]\n    x = d.block.map({b: i for i, b in enumerate(BL)}) + (k - 0.5) * 0.3\n    ax.scatter(x, d.duration, s=4, alpha=0.4, label=h)\nax.set_xticks(range(5), BL); ax.set_ylabel(\"seizure duration (s)\"); ax.legend()\nax.set_title(f\"Sham seizures, all points shown ({seiz.duration.min():.0f} to {seiz.duration.max():.0f} s)\")\nplt.tight_layout(); plt.show()\n\"\"\", [\"claim:fig2c-sham-duration-stable\"])\n\nmd(\"\"\"\n**Result: not reproduced.** Under the per-seizure reading the block effect is significant\n(ordinary p printed above), and post hoc tests find blocks that differ; the per-rat reading is\nprinted above too. The paper's test, as the claims file has it, finds an effect of block on\nseizure duration in the sham group.\n\"\"\")\n\n# ---- fig2d\nmd(\"\"\"\n## fig2d-seizures-under-two-minutes\n\n> Pooled over blocks, most seizures in the sham group last less than 2 minutes, and the two\n> hemispheres have similar distributions.\n\nSeizures of the six sham rats, all five blocks pooled, per hemisphere. Reproduced when more than\nhalf last under 120 s in each hemisphere. Medians and a two-sample Kolmogorov-Smirnov test are\ndescription only.\n\"\"\")\n\ncode(r\"\"\"\nallseiz = []\nfor _, r in sham.iterrows():\n    for h in (\"ipsilateral\", \"contralateral\"):\n        allseiz.append(tfus.seizures(M[r.asset_id], h).assign(subject=r.subject, block=r.block, hemi=h))\nallseiz = pd.concat(allseiz, ignore_index=True)\nfor h in (\"ipsilateral\", \"contralateral\"):\n    d = allseiz[allseiz.hemi == h].duration\n    print(f\"{h}: {len(d)} seizures, {100 * (d < 120).mean():.1f}% under 120 s, median {d.median():.1f} s, range {d.min():.1f} to {d.max():.1f} s\")\n    print(\"   per rat, % under 120 s:\", (allseiz[allseiz.hemi == h].groupby(\"subject\").duration.apply(lambda x: round(100 * (x < 120).mean(), 1))).to_dict())\nks = stats.ks_2samp(allseiz[allseiz.hemi == \"ipsilateral\"].duration, allseiz[allseiz.hemi == \"contralateral\"].duration)\nprint(f\"Kolmogorov-Smirnov ipsilateral against contralateral: D = {ks.statistic:.3f}, p = {ks.pvalue:.3g}\")\nprint(f\"Excluding truncated seizures changes the counts by {int(allseiz.truncated.sum())}\")\nfig, ax = plt.subplots(figsize=(6, 3))\nbins = np.arange(0, 241, 6)\nfor h in (\"ipsilateral\", \"contralateral\"):\n    ax.hist(allseiz[allseiz.hemi == h].duration, bins=bins, alpha=0.5, label=h)\nax.axvline(120, color=\"k\", lw=0.8); ax.set_xlabel(\"seizure duration (s)\"); ax.legend()\nprint(f\"Seizures beyond the 240 s axis: {(allseiz.duration > 240).sum()}\")\nplt.tight_layout(); plt.show()\n\"\"\", [\"claim:fig2d-seizures-under-two-minutes\"])\n\nmd(\"\"\"\n**Result: reproduced.** In each hemisphere far more than half of the sham seizures last under\n120 s (fractions printed above), and the medians of the two hemispheres are close; the KS test\ndoes not decide.\n\"\"\")\n\n# ---- fig2e\nmd(\"\"\"\n## fig2e-sham-count-stable\n\n> In the sham group, seizure count does not differ significantly between time blocks or\n> hemispheres, with a slight decrease in the last two hours.\n\nA claim of absence: Seizure Count per rat, hemisphere and block, five blocks, two-way ANOVA\n(hemisphere by block) with Bonferroni post hoc tests at P < 0.05.\n\"\"\")\n\ncode(r\"\"\"\ns = met[met.group == \"sham\"]\nprint(\"Mean count (rats) per hemisphere and block:\")\nprint(s.groupby([\"hemi\", \"block\"])[\"count\"].agg([\"mean\", \"sem\"]).round(2).unstack(0).to_string())\nprint(\"\\nPer rat (ipsilateral):\")\nprint(s[s.hemi == \"ipsilateral\"].pivot(index=\"subject\", columns=\"block\", values=\"count\").to_string())\nout = sham_tests(s, \"count\")\nfor k, (table, post) in out.items():\n    sig = post[(post.p_family < 0.05) | (post.p_all < 0.05)]\n    print(f\"[{k}] main effects:\", {i: f\"F={r.F:.2f}, p={r.p:.3g}\" for i, r in table.iterrows()},\n          f\"; significant post hoc: {len(sig)} of {len(post)}; smallest p (own family) {post.p_family.min():.3g}\")\nearly = s[s.block.isin(BL[:3])][\"count\"].mean(); late = s[s.block.isin(BL[3:])][\"count\"].mean()\nprint(f\"\\nMean count, baseline to post 1: {early:.2f}; post 2 and post 3: {late:.2f}\")\ns_alt = met_alt[met_alt.group == \"sham\"]\nout_alt = sham_tests(s_alt, \"count\")\nprint(\"Variant, BH635 blocks by their labels:\", {k: f\"block p={t.iloc[1].p:.3g}, smallest post hoc p {p.p_family.min():.3g}\" for k, (t, p) in out_alt.items()})\n\"\"\", [\"claim:fig2e-sham-count-stable\"])\n\nmd(\"\"\"\n**Result: reproduced.** Neither main effect nor any post hoc comparison is significant under\neither ANOVA reading (printed above), and the mean count is lower in post 2 and post 3 than in\nthe first three blocks.\n\"\"\")\n\n# ---- fig2f\nmd(\"\"\"\n## fig2f-sham-percent-time-post3\n\n> In the sham group, percent time in seizure in the contralateral hemisphere differs significantly\n> between the sham condition block and post 3, suggesting the model is no longer stable in the\n> fifth hour.\n\nPercent Time in Seizure, sham rats, five blocks, hemisphere by block. \"sham\" read as (a) the\ncondition block or (b) the baseline block. Reproduced when, under one reading, the contralateral\ncomparison with post 3 is significant at P < 0.05.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"Mean percent time (rats) per hemisphere and block:\")\nprint(s.groupby([\"hemi\", \"block\"])[\"percent_time\"].agg([\"mean\", \"sem\"]).round(2).unstack(0).to_string())\nkeep = [\"contra condition-post3\", \"contra baseline-post3\", \"ipsila condition-post3\", \"ipsila baseline-post3\"]\nfor name, df in ((\"blocks in time order\", s), (\"variant, BH635 by labels (no post 3 for BH635)\", s_alt)):\n    print(f\"\\n{name}:\")\n    show(sham_tests(df, \"percent_time\"), keep)\n\"\"\", [\"claim:fig2f-sham-percent-time-post3\"])\n\nmd(\"\"\"\n**Result: see the numbers above.**\n\"\"\")\n\n# ---- fig3 helpers\nmd(\"\"\"\n## Figure 3: tFUS against sham\n\nEach metric is tested per hemisphere with a group by block two-way ANOVA (baseline, condition,\npost 1, post 2; post 3 left out, Results A), with Bonferroni post hoc tests: each block against\nbaseline within each group (family `within`, six comparisons) and sham against tFUS at each block\n(family `between`, four); `p_all` corrects over all ten. Percent changes are given under both\nreadings of M4.\n\"\"\")\n\ncode(r\"\"\"\ndef fig3(value, df=met):\n    a, b = pct_change(df, value)\n    print(f\"{value}: tFUS change from baseline, %, reading (a) ratio of group means:\")\n    print(a.round(1).to_string())\n    print(f\"reading (b) mean of each rat's change:\")\n    print(b.round(1).to_string())\n    print(\"Group means and SEM:\")\n    print(df[df.block != \"post3\"].groupby([\"hemi\", \"group\", \"block\"])[value].agg([\"mean\", \"sem\", \"count\"]).round(2).unstack(1).to_string())\n    res = {}\n    for h in (\"ipsilateral\", \"contralateral\"):\n        print(f\"\\n{h}:\")\n        res[h] = group_tests(df, value, h)\n        show(res[h])\n    return a, b, res\n\ndef within_tol(b, expected):\n    rows = []\n    for (h, blk), (v, tol) in expected.items():\n        m = -b.loc[h, blk] if v > 0 and \"decrease\" in expected_kind else b.loc[h, blk]\n        rows.append({\"hemi\": h, \"block\": blk, \"expected\": v, \"measured\": round(m, 1), \"within\": abs(m - v) <= tol})\n    return pd.DataFrame(rows)\n\"\"\")\n\n# ---- fig3a-count-reduction\nmd(\"\"\"\n## fig3a-count-reduction\n\n> In the tFUS group, seizure count fell from baseline by 9%, 36% and 42% in the ipsilateral S1\n> and by 10%, 41% and 42% in the contralateral S1 during stimulation, post 1 and post 2, with\n> significant reductions from baseline to post 1 and to post 2 in both hemispheres.\n\"\"\")\n\ncode(r\"\"\"\na, b, res3a = fig3(\"count\")\nexp = {(\"ipsilateral\", \"condition\"): 9, (\"ipsilateral\", \"post1\"): 36, (\"ipsilateral\", \"post2\"): 42,\n       (\"contralateral\", \"condition\"): 10, (\"contralateral\", \"post1\"): 41, (\"contralateral\", \"post2\"): 42}\nfor name, t in ((\"a\", a), (\"b\", b)):\n    rows = [{\"hemi\": h, \"block\": k, \"expected\": v, \"measured decrease\": round(-t.loc[h, k], 1),\n             \"within 10%\": abs(-t.loc[h, k] - v) <= 0.1 * v} for (h, k), v in exp.items()]\n    print(f\"\\nReading ({name}) of M4:\"); print(pd.DataFrame(rows).to_string(index=False))\n\"\"\", [\"claim:fig3a-count-reduction\"])\n\nmd(\"\"\"\n**Result: see the numbers above.**\n\"\"\")\n\nmd(\"\"\"\n## fig3a-count-sham-vs-tfus\n\n> Seizure count in the sham group stays steady, and the sham and tFUS groups differ significantly\n> during post 1 and post 2.\n\nFrom the same tests: sham against tFUS at post 1 and post 2 (in both hemispheres, reading a, or\neither, reading b), and no sham block different from sham baseline.\n\"\"\")\n\ncode(r\"\"\"\nfor h in (\"ipsilateral\", \"contralateral\"):\n    for k, (table, post) in res3a[h].items():\n        p = post[post.comparison.isin([\"sham-tFUS post1\", \"sham-tFUS post2\", \"sham baseline-condition\", \"sham baseline-post1\", \"sham baseline-post2\"])]\n        print(h, k, {r.comparison: (round(r.diff, 2), round(r.p_family, 4), round(r.p_all, 4)) for r in p.itertuples()})\n\"\"\", [\"claim:fig3a-count-sham-vs-tfus\"])\n\nmd(\"\"\"\n**Result: see the numbers above.**\n\"\"\")\n\nmd(\"\"\"\n## fig3b-percent-time-reduction\n\n> In the tFUS group, percent time in seizure decreased significantly from baseline by 33%\n> (ipsilateral) and 35% (contralateral) during stimulation and by 55% in post 1 and post 2 in both\n> hemispheres.\n\"\"\")\n\ncode(r\"\"\"\na, b, res3b = fig3(\"percent_time\")\nexp = {(\"ipsilateral\", \"condition\"): 33, (\"contralateral\", \"condition\"): 35,\n       (\"ipsilateral\", \"post1\"): 55, (\"contralateral\", \"post1\"): 55,\n       (\"ipsilateral\", \"post2\"): 55, (\"contralateral\", \"post2\"): 55}\nfor name, t in ((\"a\", a), (\"b\", b)):\n    rows = [{\"hemi\": h, \"block\": k, \"expected\": v, \"measured decrease\": round(-t.loc[h, k], 1),\n             \"within 10%\": abs(-t.loc[h, k] - v) <= 0.1 * v} for (h, k), v in exp.items()]\n    print(f\"\\nReading ({name}) of M4:\"); print(pd.DataFrame(rows).to_string(index=False))\n\"\"\", [\"claim:fig3b-percent-time-reduction\"])\n\nmd(\"\"\"\n**Result: see the numbers above.**\n\"\"\")\n\nmd(\"\"\"\n## fig3b-sham-percent-time-no-change\n\n> In the sham group, percent time in seizure decreased slightly but did not differ significantly\n> from baseline in any block.\n\nA claim of absence: no sham block (condition, post 1, post 2) differs from sham baseline at\nP < 0.05 in either hemisphere.\n\"\"\")\n\ncode(r\"\"\"\nfor h in (\"ipsilateral\", \"contralateral\"):\n    for k, (table, post) in res3b[h].items():\n        p = post[post.comparison.str.startswith(\"sham baseline\")]\n        print(h, k, {r.comparison: (round(r.diff, 2), round(r.p_family, 4), round(r.p_all, 4)) for r in p.itertuples()})\n\"\"\", [\"claim:fig3b-sham-percent-time-no-change\"])\n\nmd(\"\"\"\n**Result: see the numbers above.**\n\"\"\")\n\nmd(\"\"\"\n## fig3b-percent-time-sham-vs-tfus\n\n> Percent time in seizure differs significantly between sham and tFUS during post 1 in the\n> contralateral S1, and during stimulation and post 1 in the ipsilateral S1.\n\"\"\")\n\ncode(r\"\"\"\nwant = [(\"contralateral\", \"sham-tFUS post1\"), (\"ipsilateral\", \"sham-tFUS condition\"), (\"ipsilateral\", \"sham-tFUS post1\")]\nfor k in (\"ordinary\", \"repeated\"):\n    rows = []\n    for h, c in want:\n        r = res3b[h][k][1].set_index(\"comparison\").loc[c]\n        rows.append({\"hemi\": h, \"comparison\": c, \"sham minus tFUS\": round(r[\"diff\"], 2), \"p_family\": round(r.p_family, 4), \"p_all\": round(r.p_all, 4)})\n    print(k); print(pd.DataFrame(rows).to_string(index=False))\n\"\"\", [\"claim:fig3b-percent-time-sham-vs-tfus\"])\n\nmd(\"\"\"\n**Result: see the numbers above.**\n\"\"\")\n\nmd(\"\"\"\n## fig3c-interval-increase\n\n> Relative to baseline, the inter-seizure interval of the tFUS group increased by 27%, 49% and\n> 28% (ipsilateral) and 30%, 52% and 31% (contralateral) during stimulation, post 1 and post 2;\n> only post 1 in the contralateral S1 differed significantly from baseline.\n\nThe 8 tFUS rats left after the Methods' exclusion. Both readings of the interval are run; the gap\nreading is the one the paper's words favour.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"Rats in the interval analysis per group:\", met.dropna(subset=[\"isi_gap\"]).groupby(\"group\").subject.nunique().to_dict())\nexp = {(\"ipsilateral\", \"condition\"): 27, (\"ipsilateral\", \"post1\"): 49, (\"ipsilateral\", \"post2\"): 28,\n       (\"contralateral\", \"condition\"): 30, (\"contralateral\", \"post1\"): 52, (\"contralateral\", \"post2\"): 31}\nres3c = {}\nfor value in (\"isi_gap\", \"isi_onset\"):\n    print(f\"\\n==== {value}\")\n    a, b, res3c[value] = fig3(value)\n    for name, t in ((\"a\", a), (\"b\", b)):\n        rows = [{\"hemi\": h, \"block\": k, \"expected\": v, \"measured increase\": round(t.loc[h, k], 1),\n                 \"within 10%\": abs(t.loc[h, k] - v) <= 0.1 * v} for (h, k), v in exp.items()]\n        print(f\"Reading ({name}) of M4:\"); print(pd.DataFrame(rows).to_string(index=False))\n\"\"\", [\"claim:fig3c-interval-increase\"])\n\nmd(\"\"\"\n**Result: see the numbers above.**\n\"\"\")\n\nmd(\"\"\"\n## fig3c-interval-sham-vs-tfus\n\n> The inter-seizure interval of the sham group stays steady, and sham and tFUS differ\n> significantly during post 1 in both hemispheres.\n\"\"\")\n\ncode(r\"\"\"\nfor value in (\"isi_gap\", \"isi_onset\"):\n    for h in (\"ipsilateral\", \"contralateral\"):\n        for k, (table, post) in res3c[value][h].items():\n            p = post[post.comparison.isin([\"sham-tFUS post1\", \"sham baseline-condition\", \"sham baseline-post1\", \"sham baseline-post2\"])]\n            print(value, h, k, {r.comparison: (round(r.diff, 1), round(r.p_family, 4), round(r.p_all, 4)) for r in p.itertuples()})\n\"\"\", [\"claim:fig3c-interval-sham-vs-tfus\"])\n\nmd(\"\"\"\n**Result: see the numbers above.**\n\"\"\")\n\nmd(\"\"\"\n## fig3d-duration-decline\n\n> Seizure duration declines across time in both groups, and the only significant reduction is\n> from baseline to post 2 in both hemispheres of the tFUS group.\n\"\"\")\n\ncode(r\"\"\"\na, b, res3d = fig3(\"duration\")\nfor h in (\"ipsilateral\", \"contralateral\"):\n    for k, (table, post) in res3d[h].items():\n        p = post[post.family == \"within\"]\n        print(h, k, \"within-group against baseline:\", {r.comparison: (round(r.diff, 1), round(r.p_family, 4)) for r in p.itertuples()})\nprint(\"\\nGroup means at baseline and post 2:\")\nprint(met[met.block.isin([\"baseline\", \"post2\"])].groupby([\"group\", \"hemi\", \"block\"]).duration.mean().round(1).unstack().to_string())\n\"\"\", [\"claim:fig3d-duration-decline\"])\n\nmd(\"\"\"\n**Result: see the numbers above.**\n\"\"\")\n\nmd(\"\"\"\n## Summary\n\nFilled in after the run.\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"Notebook ran in {(time.time() - started) / 60:.1f} min\")\n\"\"\")\n\nbuild(H + \"seizure_metrics.ipynb\", cells)\nprint(\"built\", len(cells))\n"
}
```

```
File created successfully at: /tmp/claude-1001/build/nb1.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
p='/tmp/claude-1001/build/nb1.py'; s=open(p).read()
i=s.index('def within_tol'); j=s.index('""")',i)
s=s[:i]+'    '[:0]+s[j:]
s=s.replace('    return a, b, res\n\n"""','    return a, b, res\n"""')
open(p,'w').write(s)
EOF
grep -n "within_tol\|expected_kind" build/nb1.py; uv pip install -q nbconvert ipykernel nbformat && python build/nb1.py && cd entries/001683-gao-2026 && time jupyter nbconvert --to notebook --execute seizure_metrics.ipynb --output $TMPDIR/nb1_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | tail -3
```

```
built 52
[NbConvertApp] Converting notebook seizure_metrics.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 164263 bytes to /tmp/claude-1001/nb1_out.ipynb

real	1m2.187s
user	0m8.448s
sys	0m0.808s
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > showout.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain') or ''
        if o.get('output_type')=='error': t='\n'.join(o['traceback'])
        t=''.join(t) if isinstance(t,list) else t
        if 'image/png' in o.get('data',{}): t='[image]'
        print(f'--- cell {i}'); print(t[:int(sys.argv[2]) if len(sys.argv)>2 else 6000])
EOF
python showout.py nb1_out.ipynb 5000 | head -400
```

```
--- cell 1
dandiset 001683 version 0.260109.2104: 318 assets, 355.7 GB; archive summary: 23 subjects, 318 files

--- cell 1
files over 2 GB: 70; of them labelled EEG blocks: 70; read in 41 s

--- cell 3
Kinds, groups and notes of the files read:
(Labeled_data, tFUS group, EEG signals with seizure labels)    40
(Labeled_data, sham group, EEG signals with seizure labels)    30

Rats per group: {'sham': 6, 'tFUS': 10} (paper: 10 tFUS, 6 sham)

Block files per rat, and the label each file carries in general/data_collection, in time order:
block          baseline     condition        post1        post2        post3
subject                                                                     
BH624    BH624_BASELINE  BH624_CC_1Hz  BH624_post1  BH624_post2             
BH626    BH626_BASELINE  BH626_CC_1Hz  BH626_post1  BH626_post2             
BH634    BH634_BASELINE  BH634_CC_1Hz  BH634_post1  BH634_post2             
BH635    BH635_BASELINE    BH635_SHAM   BH635_SHAM  BH636_post1  BH635_post2
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python showout.py nb1_out.ipynb 6000 | sed -n 400,700p
```

```
post1      20.60  10.58  4.28  2.21     6   10
              post2      16.43  10.13  2.96  2.27     6   10

ipsilateral:
  [ordinary] main effects: {'C(group, Sum)': 'F=8.66, p=0.00474', 'C(block, Sum)': 'F=5.15, p=0.00326', 'C(group, Sum):C(block, Sum)': 'F=0.95, p=0.422'}
             comparison  family    diff    stat  p_raw  p_family  p_all
sham baseline-condition  within -0.8855 -0.1746 0.8620    1.0000 1.0000
    sham baseline-post1  within  3.4036  0.6712 0.5048    1.0000 1.0000
    sham baseline-post2  within  7.5759  1.4940 0.1408    0.8447 1.0000
tFUS baseline-condition  within  8.3905  2.1362 0.0370    0.2223 0.3705
    tFUS baseline-post1  within 12.8737  3.2776 0.0018    0.0108 0.0180
    tFUS baseline-post2  within 13.3245  3.3923 0.0013    0.0077 0.0128
     sham-tFUS baseline between  0.5481  0.1208 0.9042    1.0000 1.0000
    sham-tFUS condition between  9.8242  2.1661 0.0346    0.1383 0.3458
        sham-tFUS post1 between 10.0182  2.2089 0.0313    0.1252 0.3129
        sham-tFUS post2 between  6.2967  1.3883 0.1705    0.6821 1.0000
  [repeated] main effects: {'C(group, Sum)': 'F=2.82, p=0.0932', 'C(block, Sum)': 'F=13.56, p=7.63e-09', 'C(group, Sum):C(block, Sum)': 'F=3.08, p=0.0263'}
             comparison  family    diff    stat  p_raw  p_family  p_all
sham baseline-condition  within -0.8855 -0.3139 0.7536    1.0000 1.0000
    sham baseline-post1  within  3.4036  1.2066 0.2276    1.0000 1.0000
[... 282 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python showout.py nb1_out.ipynb 8000 | sed -n 700,800p
```

```
block          condition  post1  post2
hemi                                  
contralateral      -19.4  -18.7  -18.2
ipsilateral        -18.9  -19.8  -18.6
reading (b) mean of each rat's change:
block          condition  post1  post2
hemi                                  
contralateral      -15.2  -13.5  -20.2
ipsilateral        -14.4  -12.3  -20.7
Group means and SEM:
                          mean          sem       count     
group                     sham   tFUS  sham  tFUS  sham tFUS
hemi          block                                         
contralateral baseline   56.85  61.00  9.37  5.79     6   10
              condition  48.88  49.15  4.03  4.53     6   10
              post1      43.29  49.59  2.78  3.15     6   10
              post2      40.60  49.88  1.74  4.79     6    8
ipsilateral   baseline   53.00  59.84  8.91  6.02     6   10
              condition  48.55  48.52  3.49  4.78     6   10
              post1      43.85  48.00  3.52  3.24     6   10
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cd entries/001683-gao-2026 && cat > $TMPDIR/dev3.py <<'EOF'
import tfus, pickle, time, numpy as np
metas=pickle.load(open('/tmp/claude-1001/metas.pkl','rb'))
lab=[m for m in metas if m['kind']=='Labeled_data']
m=lab[0]
t=time.time()
x=tfus.read_rows(m,0,1_000_000); print('read 1M rows',time.time()-t)
t=time.time()
r=tfus.process_block(m); print('process',time.time()-t)
f,p=r['psd_block']; print(f[:3], p.shape, tfus.band_powers(f,p))
print({b:(v['n'], tfus.pair_means(v['per_seizure']), tfus.pair_means(v['concat'])) for b,v in r['pli'].items()})
pickle.dump(r,open('/tmp/claude-1001/r0.pkl','wb'))
EOF
PYTHONPATH=. /usr/bin/time -v python $TMPDIR/dev3.py 2>&1 | grep -v "^\s*\(Page\|Socket\|Signals\|Swaps\|File sys\|Average\|Voluntary\|Involuntary\|Exit\|Minor\|Major\)"
```

```
Tue Nov  3 08:32:40 UTC 2026
read 1M rows 1.0824000835418701
process 39.0351459980011
[0.         0.49996032 0.99992065] (3053, 2) {'theta': array([9.84617467e-13, 7.79597692e-13]), 'alpha': array([1.42845502e-12, 1.51364695e-12]), 'beta': array([4.38277449e-12, 5.00695093e-12]), 'gamma': array([1.85185316e-12, 2.34301395e-12]), 'total_3_300': array([1.02274873e-11, 1.05300466e-11]), 'total_all': array([1.11653462e-11, 1.08113118e-11])}
{'theta': (12, {'S1': 0.18029072633575857, 'nonS1': 0.14547044021878397}, {'S1': 0.19264947096140722, 'nonS1': 0.10061693185205996}), 'alpha': (12, {'S1': 0.13251632858648432, 'nonS1': 0.14335487882747866}, {'S1': 0.12869890701776043, 'nonS1': 0.1387058107770852}), 'beta': (12, {'S1': 0.1139665374714339, 'nonS1': 0.13431994338831402}, {'S1': 0.12422244026056764, 'nonS1': 0.1586174965761043}), 'gamma': (12, {'S1': 0.07843719406967822, 'nonS1': 0.06643222988625876}, {'S1': 0.09486051457995456, 'nonS1': 0.06499777468456568})}
	Command being timed: "python /tmp/claude-1001/dev3.py"
	User time (seconds): 32.39
	System time (seconds): 11.91
	Percent of CPU this job got: 107%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:41.11
	Maximum resident set size (kbytes): 6749576
```

**Agent**

One block takes 39 s and 6.7 GB, so 70 blocks would take 45 min. Restructuring: decimate chunk by chunk, band-filter only the seizure segments with padding, and run 3 worker processes.

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('tfus.py').read()
i=s.index('def process_block'); j=s.index('def pair_means')
new='''def process_block(meta: dict, rows_per_read: int = 1_000_000) -> dict:
    """One labelled EEG block: PSD of channels 8 and 25 (whole block, seizure periods per hemisphere,
    merged seizure periods), 30-80 Hz power in 1 s bins (for the clock check of the labels), and the
    seizure PLI per band for S1 and non-S1 pairs.

    The 32 channels are read in pieces, re-referenced to their common average, and decimated by 3
    (polyphase FIR) for the PLI; each piece is read with a margin so that the decimation has no edges.
    The PLI band filters run on each seizure period with 2 s of signal on either side."""
    n = meta["n_samples"]
    pad = 3000
    car2 = np.empty((n, 2))
    dec = []
    for s in range(0, n, rows_per_read):
        a, b = max(0, s - pad), min(n, s + rows_per_read + pad)
        x = read_rows(meta, a, b)
        x = x - x.mean(axis=1, keepdims=True)                 # common average reference
        e = min(n, s + rows_per_read)
        car2[s:e] = x[s - a:e - a][:, [IPSI_CH - 1, CONTRA_CH - 1]]
        y = signal.resample_poly(x, 1, DECIMATE, axis=0)
        k0 = (s - a) // DECIMATE
        dec.append(y[k0:k0 + (e - s + DECIMATE - 1) // DECIMATE].astype(np.float32))
        del x, y
    xd = np.concatenate(dec)
    del dec
    car2 = _notch(car2, RATE)
    out = {"asset_id": meta["asset_id"], "n_samples": n}
    out["psd_block"] = welch_segments(car2, RATE)
    per = {h: seizures(meta, h)[["start", "stop"]].to_numpy() for h in ("ipsilateral", "contralateral")}
    merged = merged_periods(meta)
    out["psd_seiz_ipsi"] = welch_segments(car2[:, [0]], RATE, per["ipsilateral"])
    out["psd_seiz_contra"] = welch_segments(car2[:, [1]], RATE, per["contralateral"])
    out["psd_seiz_merged"] = welch_segments(car2, RATE, merged)
    out["periods_merged"] = merged
    sos = signal.butter(4, [30, 80], btype="bandpass", fs=RATE, output="sos")
    g = signal.sosfiltfilt(sos, car2, axis=0) ** 2
    nb = int(n // RATE)
    edges = (np.arange(nb + 1) * RATE).astype(int)
    out["gamma_1s"] = np.add.reduceat(g[: edges[-1]], edges[:-1], axis=0) / np.diff(edges)[:, None]
    del g, car2
    fs_d = RATE / DECIMATE
    bn, an = signal.iirnotch(60.0, 30.0, fs_d)
    sos_bp = signal.butter(4, [3, 300], btype="bandpass", fs=fs_d, output="sos")
    ii = [c - 1 for c in S1_IPSI + NONS1_IPSI]
    cc = [c - 1 for c in S1_CONTRA + NONS1_CONTRA]
    margin = int(2 * fs_d)
    segs = [(int(a0 * fs_d), int(b0 * fs_d)) for a0, b0 in merged if (b0 - a0) >= 1.0]
    acc = {band: ([], []) for band in BANDS}
    for i, j in segs:
        i0, j0 = max(0, i - margin), min(len(xd), j + margin)
        seg = signal.filtfilt(bn, an, xd[i0:j0].astype(np.float64), axis=0)
        seg = signal.sosfiltfilt(sos_bp, seg, axis=0)
        for band in BANDS:
            ph = np.angle(signal.hilbert(signal.sosfiltfilt(band_sos(band, fs_d), seg, axis=0), axis=0))
            ph = ph[i - i0: i - i0 + (min(j, len(xd)) - i)]
            acc[band][0].append(pli(ph[:, ii], ph[:, cc]))
            acc[band][1].append(ph[:, ii + cc].astype(np.float32))
    res = {}
    for band, (per_seiz, cat) in acc.items():
        if per_seiz:
            phc = np.concatenate(cat)
            res[band] = {"per_seizure": np.mean(per_seiz, axis=0),
                         "concat": pli(phc[:, : len(ii)], phc[:, len(ii):]), "n": len(per_seiz),
                         "seconds": len(phc) / fs_d}
        else:
            res[band] = None
    out["pli"] = res
    return out


def process_blocks(metas: list[dict], workers: int = 3) -> dict:
    """process_block over many files in parallel processes; returns {asset_id: result}."""
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn")) as ex:
        return {r["asset_id"]: r for r in ex.map(process_block, metas)}


'''
s=s[:i]+new+s[j:]
open('tfus.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cd entries/001683-gao-2026 && PYTHONPATH=. /usr/bin/time -v python $TMPDIR/dev3.py 2>&1 | grep -v "^\s*\(Page\|Socket\|Signals\|Swaps\|File sys\|Average\|Voluntary\|Involuntary\|Exit\|Minor\|Major\)"
```

```
read 1M rows 1.0858213901519775
process 26.806700229644775
[0.         0.49996032 0.99992065] (3053, 2) {'theta': array([9.84617467e-13, 7.79597692e-13]), 'alpha': array([1.42845502e-12, 1.51364695e-12]), 'beta': array([4.38277449e-12, 5.00695093e-12]), 'gamma': array([1.85185316e-12, 2.34301395e-12]), 'total_3_300': array([1.02274873e-11, 1.05300466e-11]), 'total_all': array([1.11653462e-11, 1.08113118e-11])}
{'theta': (12, {'S1': 0.1802907760050434, 'nonS1': 0.145452132755449}, {'S1': 0.19262854242697358, 'nonS1': 0.10061171947583919}), 'alpha': (12, {'S1': 0.1324551197150719, 'nonS1': 0.14334802346026937}, {'S1': 0.12871735240332782, 'nonS1': 0.1386901040645575}), 'beta': (12, {'S1': 0.11386616546947165, 'nonS1': 0.1343560186105466}, {'S1': 0.12410201207967475, 'nonS1': 0.15864750022915863}), 'gamma': (12, {'S1': 0.07855849768982158, 'nonS1': 0.06651404518411054}, {'S1': 0.0950858541764319, 'nonS1': 0.06513802941885337})}
	Command being timed: "python /tmp/claude-1001/dev3.py"
	User time (seconds): 22.36
	System time (seconds): 10.84
	Percent of CPU this job got: 114%
	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:28.97
	Maximum resident set size (kbytes): 2099888
```

**Agent**

Restructured version: 27 s and 2.1 GB per block, same numbers; with 4 processes the 70 blocks should take about 10 min. Writing notebook 2 (band power, AI, seizure PLI).

**Agent calls Bash**

```bash
cat >> tfus.py <<'EOF'


def group_block_tests(df: pd.DataFrame, value: str, blocks=BLOCKS[:4]) -> dict:
    """Group (sham, tFUS) by block two-way ANOVA (M3), both readings. Post hoc families: `within`, each
    block against baseline in each group; `between`, sham against tFUS at each block."""
    d = df[df.block.isin(blocks)]
    comps = [(f"{g} baseline-{b}", {"group": g, "block": "baseline"}, {"group": g, "block": b}, "within")
             for g in ("sham", "tFUS") for b in blocks[1:]]
    comps += [(f"sham-tFUS {b}", {"group": "sham", "block": b}, {"group": "tFUS", "block": b}, "between")
              for b in blocks]
    return {("repeated" if rm else "ordinary"): twoway(d, value, "group", "block", "subject", comps, rm=rm)
            for rm in (False, True)}


def hemi_block_tests(df: pd.DataFrame, value: str, blocks=BLOCKS) -> dict:
    """Hemisphere by block two-way ANOVA within one group (Figs. 2 and S4), both readings. Post hoc
    families: `blocks`, each pair of blocks within each hemisphere; `hemi`, the hemispheres at each block."""
    comps = []
    for h in ("ipsilateral", "contralateral"):
        for i, b1 in enumerate(blocks):
            for b2 in blocks[i + 1:]:
                comps.append((f"{h[:6]} {b1}-{b2}", {"hemi": h, "block": b1}, {"hemi": h, "block": b2}, "blocks"))
    for b in blocks:
        comps.append((f"ipsi-contra {b}", {"hemi": "ipsilateral", "block": b},
                      {"hemi": "contralateral", "block": b}, "hemi"))
    return {("repeated" if rm else "ordinary"): twoway(df, value, "hemi", "block", "subject", comps, rm=rm)
            for rm in (False, True)}


def significant(post: pd.DataFrame, family: bool = True) -> pd.DataFrame:
    """Post hoc rows significant at 0.05 under the family reading (i) or the all-in-one reading (ii)."""
    return post[post["p_family" if family else "p_all"] < 0.05]
EOF
date -u
```

```
Tue Nov  3 08:34:47 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/001683-gao-2026 && cat > $TMPDIR/dev4.py <<'EOF'
import tfus, pickle, time
if __name__ == "__main__":
    metas=pickle.load(open('/tmp/claude-1001/metas.pkl','rb'))
    lab=[m for m in metas if m['kind']=='Labeled_data']
    t=time.time()
    R=tfus.process_blocks(lab, workers=4)
    print('all',time.time()-t)
    pickle.dump(R,open('/tmp/claude-1001/R.pkl','wb'))
EOF
PYTHONPATH=. timeout 3000 python $TMPDIR/dev4.py; date -u
```

```
all 748.8563456535339
Tue Nov  3 08:47:26 UTC 2026
```

**Agent**

All 70 blocks processed in 12.5 min. Exploring the results before writing notebook 2.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/001683-gao-2026 && cat > $TMPDIR/dev5.py <<'EOF'
import tfus, pickle, numpy as np, pandas as pd
pd.set_option("display.width",250)
metas=pickle.load(open('/tmp/claude-1001/metas.pkl','rb')); R=pickle.load(open('/tmp/claude-1001/R.pkl','rb'))
lab=[m for m in metas if m['kind']=='Labeled_data']; M={m['asset_id']:m for m in lab}
blocks=tfus.assign_blocks(lab)
# clock check
rows=[]
for a,r in R.items():
    g=r['gamma_1s']; nb=len(g)
    for k,h in enumerate(['ipsilateral','contralateral']):
        s=tfus.seizures(M[a],h)
        for shift in [0,30,60,120,600]:
            inside=np.zeros(nb,bool)
            for x,y in s[['start','stop']].to_numpy():
                i,j=int(x+shift),int(y+shift); inside[max(0,i):min(nb,j)]=True
            if inside.any() and (~inside).any():
                rows.append(dict(a=a,h=h,shift=shift,ratio=g[inside,k].mean()/g[~inside,k].mean()))
        inside=np.zeros(nb,bool)
        for x,y in (s[['start','stop']].to_numpy()/60):
            inside[int(x):int(np.ceil(y))]=True
        if inside.any(): rows.append(dict(a=a,h=h,shift='as seconds',ratio=g[inside,k].mean()/g[~inside,k].mean()))
cc=pd.DataFrame(rows); print(cc.groupby('shift').ratio.describe().round(2))
# band ratios
f,p=R[lab[0]['asset_id']]['psd_block']; print('f range',f.min(),f.max(),'psd range',p.min(),p.max())
EOF
PYTHONPATH=. python $TMPDIR/dev5.py
```

```
count   mean   std   min   25%    50%    75%    max
shift                                                          
0           136.0  14.55  9.81  2.57  7.20  12.48  18.64  50.82
30          136.0   3.45  2.50  0.84  1.82   2.77   4.51  19.06
60          136.0   0.77  0.84  0.13  0.35   0.52   0.74   6.37
120         136.0   0.65  0.39  0.11  0.37   0.54   0.83   1.70
600         136.0   1.05  0.69  0.24  0.60   0.90   1.21   4.53
as seconds  136.0   0.90  1.72  0.13  0.28   0.44   0.75  13.72
f range 0.0 1525.87890625 psd range 1.7319430489462196e-18 8.849152680878419e-13
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build/nb2.py",
 "content": "import sys\nsys.path.insert(0, \"/tmp/claude-1001/build\")\nfrom nbtools import build\n\nH = \"entries/001683-gao-2026/\"\nDEV = len(sys.argv) > 1\ncells = []\nmd = lambda s, t=None: cells.append((\"md\", s, t))\ncode = lambda s, t=None: cells.append((\"code\", s, t))\n\nmd(r\"\"\"\n# Gao et al. (2026) on dandiset 001683: band power, asymmetry index and seizure PLI\n\n**Paper.** Gao H, Frake A, Durand DM, He B (2026). Transcranial focused ultrasound stimulation\ntargeting white matter inhibits seizures in a rat model of epilepsy. *IEEE Trans Neural Syst Rehabil\nEng* 34, 251-259. [doi:10.1109/tnsre.2025.3644273](https://doi.org/10.1109/tnsre.2025.3644273). The\nclaims file was written from the NIH author manuscript (PMC12848950) and the supplement.\n\n**Dandiset.** [DANDI:001683](https://dandiarchive.org/dandiset/001683/0.260109.2104), version\n0.260109.2104, the only published version (the paper cites none; see `seizure_metrics.ipynb`).\n\nThis notebook streams all 70 labelled EEG blocks (2.9 GB each, about 205 GB) once and reduces each\nas it loads (`tfus.process_block`): the Welch PSD of the two labelling channels (8 and 25, Fig. S1)\nafter a common average reference and a 60 Hz notch, over the whole block and over the seizure\nperiods; 30 to 80 Hz power in 1 s bins for the clock check of the labels; and the phase lag index\nover the seizure periods for every pair of one ipsilateral and one contralateral channel. It takes\nabout 13 minutes with four processes.\n\n| Claim | Tested here |\n|---|---|\n| fig4-no-theta-alpha-gamma-power-change | yes |\n| fig4c-beta-decrease | yes |\n| figs4-sham-power-no-change | yes |\n| fig4ef-ai-increase | yes |\n| figs5-seizures-lower-ai | blocked (data_missing): no pre-4-AP EEG in the dandiset; the tests of seizure AI against 0 are run |\n| fig6-epileptic-pli-s1-decrease | yes |\n| figs7-seizure-pli-s1-vs-non-s1 | blocked (data_missing): no pre-4-AP EEG in the dandiset |\n\"\"\")\n\ncode(r\"\"\"\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport tfus\n\nwarnings.filterwarnings(\"ignore\")\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 300)\n\nstarted = time.time()\nassets = tfus.list_assets()\nbig = assets[assets[\"size\"] > 2e9]\nlab = [m for m in tfus.read_all_meta(big.asset_id.tolist()) if m[\"kind\"] == \"Labeled_data\"]\nM = {m[\"asset_id\"]: m for m in lab}\nblocks = tfus.assign_blocks(lab)\nprint(f\"dandiset {tfus.DANDISET_ID} version {tfus.DANDISET_VERSION}: {len(lab)} labelled blocks, \"\n      f\"{sum(m['n_samples'] * m['n_channels'] * 8 for m in lab) / 1e9:.0f} GB of samples\")\n\"\"\")\n\nif DEV:\n    code(r\"\"\"\nimport pickle\nR = pickle.load(open(\"/tmp/claude-1001/R.pkl\", \"rb\"))\n\"\"\")\nelse:\n    code(r\"\"\"\nt0 = time.time()\nR = tfus.process_blocks(lab, workers=4)\nprint(f\"processed {len(R)} blocks in {(time.time() - t0) / 60:.1f} min\")\n\"\"\")\n\nmd(\"\"\"\n## Data check\n\nEach check of the metadata against the values is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\nprint(\"Rats per group:\", blocks.groupby(\"group\").subject.nunique().to_dict(), \"; blocks per group:\", blocks.groupby(\"group\").size().to_dict())\nprint(\"Blocks per rat:\", blocks.groupby(\"subject\").size().to_dict())\nm0 = lab[0]\ne = m0[\"electrodes\"]\nprint(\"\\nElectrode table of the EEG files (x, y in mm; location):\")\nprint(e.assign(channel=np.arange(1, 33)).set_index(\"channel\").T.to_string())\nsame = all(m[\"electrodes\"][[\"x\", \"y\"]].equals(m0[\"electrodes\"][[\"x\", \"y\"]]) for m in lab)\nprint(\"Same electrode table in every block file:\", same)\nprint(f\"Channel {tfus.IPSI_CH} at x={e.x[tfus.IPSI_CH - 1]}, y={e.y[tfus.IPSI_CH - 1]}; channel {tfus.CONTRA_CH} at x={e.x[tfus.CONTRA_CH - 1]}, y={e.y[tfus.CONTRA_CH - 1]}\")\nprint(\"Burr holes (Methods A): AP -2 mm, ML +2.5 (right, injection, ipsilateral) and -2.5 (left)\")\nprint(f\"Channels 1-16 have x > 0: {bool((e.x[:16] > 0).all())}; channels 17-32 x < 0: {bool((e.x[16:] < 0).all())}\")\nplv = [m for m in tfus.read_all_meta(assets[(assets['size'] > 0.2e9) & (assets['size'] < 0.4e9)].asset_id.tolist()) if m[\"kind\"].startswith(\"EEG data for PLV\")]\nprint(\"\\nNotes of the dandiset's PLV files (the source of the S1 channel lists):\", sorted({m['notes'] for m in plv}))\nf, p = R[m0[\"asset_id\"]][\"psd_block\"]\nprint(f\"\\nPSD: {len(f)} bins, {f[1] - f[0]:.2f} Hz apart, 0 to {f[-1]:.0f} Hz; values {p.min():.2e} to {p.max():.2e} V^2/Hz\")\nraw = tfus.read_rows(m0, 1_000_000, 1_003_052)\nprint(f\"Raw EEG, 1 s of block 1: {raw.min() * 1e6:.0f} to {raw.max() * 1e6:.0f} uV; per-channel SD {raw.std(axis=0).min() * 1e6:.0f} to {raw.std(axis=0).max() * 1e6:.0f} uV\")\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nThe electrode table puts channels 1 to 16 on the right (ipsilateral to the injection) and 17 to 32\non the left, and channels 8 and 25 at ML +/-2.8 mm, AP -3 mm, next to the burr holes, which fits\nthe encircled electrodes of Fig. S1. The values are in volts, tens to hundreds of microvolts, as an\nEEG should be.\n\n**Clock check of the labels.** The 30 to 80 Hz power of channel 8 (ipsilateral labels) and\nchannel 25 (contralateral labels) in 1 s bins, inside the labelled seizures against outside, with\nthe label times read as minutes, shifted later by 30 s to 600 s, and read as seconds.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor a, r in R.items():\n    g = r[\"gamma_1s\"]; nb = len(g)\n    for k, h in enumerate((\"ipsilateral\", \"contralateral\")):\n        s = tfus.seizures(M[a], h)\n        for shift in (0, 30, 60, 120, 600, \"read as seconds\"):\n            inside = np.zeros(nb, bool)\n            pairs = s[[\"start\", \"stop\"]].to_numpy() / (60 if shift == \"read as seconds\" else 1)\n            for x, y in pairs:\n                off = 0 if shift == \"read as seconds\" else shift\n                inside[max(0, int(x + off)):min(nb, int(np.ceil(y + off)))] = True\n            if inside.any() and (~inside).any():\n                rows.append({\"block\": a, \"hemi\": h, \"labels\": shift, \"inside/outside\": g[inside, k].mean() / g[~inside, k].mean()})\ncc = pd.DataFrame(rows)\nprint(cc.groupby(\"labels\", sort=False)[\"inside/outside\"].describe().round(2).to_string())\nprint(f\"\\nFile-hemispheres where gamma power is higher inside the labels (as minutes, no shift): \"\n      f\"{(cc[cc.labels == 0]['inside/outside'] > 1).sum()} of {(cc.labels == 0).sum()}\")\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nWith the labels read as minutes, 30 to 80 Hz power inside them is many times that outside in every\nblock and hemisphere (the paper's labelling rule, Methods C); shifted by 60 s or more, or read as\nseconds, the contrast is gone. So the labels and the EEG share a clock, and the label times are in\nminutes. The two blocks without seizures (BH634 and BH638, post 2) have no labels to test.\n\"\"\")\n\ncode(r\"\"\"\n# Per rat, hemisphere, block: band power ratios (M5), under the readings segment (block, seizure)\n# and total (3-300 Hz, 0 Hz to Nyquist); and the asymmetry index (Eq. 1) on the band power.\ninfo = blocks.set_index(\"asset_id\")\nbp, ai = [], []\nfor a, r in R.items():\n    i = info.loc[a]\n    base = {\"subject\": i.subject, \"group\": i.group, \"block\": i.block}\n    for seg, key in ((\"block\", None), (\"seizure\", \"seiz\")):\n        for k, h in enumerate((\"ipsilateral\", \"contralateral\")):\n            if key is None:\n                f, p = r[\"psd_block\"]; p = p[:, k]\n            else:\n                f, p = r[\"psd_seiz_ipsi\" if k == 0 else \"psd_seiz_contra\"]\n                if f is None:\n                    continue\n                p = p[:, 0]\n            pw = tfus.band_powers(f, p)\n            for band in tfus.BANDS:\n                for tot in (\"total_3_300\", \"total_all\"):\n                    bp.append({**base, \"hemi\": h, \"segment\": seg, \"total\": tot, \"band\": band, \"ratio\": pw[band] / pw[tot]})\n        f, p = r[\"psd_block\"] if key is None else r[\"psd_seiz_merged\"]\n        if f is None:\n            continue\n        pw = tfus.band_powers(f, p)\n        for band in tfus.BANDS:\n            ip, co = pw[band]\n            ai.append({**base, \"segment\": seg, \"band\": band, \"ai\": (ip - co) / (ip + co),\n                       \"ai_ratio\": (ip / pw[\"total_3_300\"][0] - co / pw[\"total_3_300\"][1]) / (ip / pw[\"total_3_300\"][0] + co / pw[\"total_3_300\"][1])})\nbp, ai = pd.DataFrame(bp), pd.DataFrame(ai)\nprint(f\"Band power rows: {len(bp)}; AI rows: {len(ai)}\")\nprint(\"Ranges of the band ratios:\", bp.groupby([\"band\"]).ratio.agg([\"min\", \"max\"]).round(4).to_dict(\"index\"))\nprint(\"Ranges of AI:\", ai.groupby(\"band\").ai.agg([\"min\", \"max\"]).round(3).to_dict(\"index\"))\nprint(\"Blocks without a seizure PSD (no seizure of 2 s or more):\", sorted(set((r.subject, r.block) for r in blocks.itertuples()) - set(map(tuple, bp[bp.segment == 'seizure'][[\"subject\", \"block\"]].drop_duplicates().to_numpy()))))\n\"\"\")\n\n# ---------------- fig4 absence\nmd(\"\"\"\n## fig4-no-theta-alpha-gamma-power-change\n\n> There are no significant changes in theta, alpha or gamma power ratios in either hemisphere.\n\nA claim of absence. Band power ratios (M5) for sham and tFUS, blocks baseline to post 2, group by\nblock two-way ANOVA per hemisphere and band, with Bonferroni post hoc tests (M3). The claim covers\nthe within-group comparisons against baseline. Every reading of M5 (segment: whole block or\nseizure periods; total: 3 to 300 Hz or 0 Hz to Nyquist) and of M3 is run. As in\n`seizure_metrics.ipynb`, the repeated-measures reading is the one adopted where the ANOVA readings\ndisagree (see the summary there: it is the reading that gives the paper's own significant\nwithin-group changes of Fig. 3).\n\"\"\")\n\ncode(r\"\"\"\ndef band_tests(df, value=\"ratio\", bands=tfus.BANDS, by_hemi=True):\n    rows = []\n    for (seg, tot), d in df.groupby([\"segment\", \"total\"]):\n        for band in bands:\n            for h in ((\"ipsilateral\", \"contralateral\") if by_hemi else (None,)):\n                dd = d[(d.band == band) & ((d.hemi == h) if h else True)]\n                for k, (table, post) in tfus.group_block_tests(dd, value).items():\n                    for r in post.itertuples():\n                        rows.append({\"segment\": seg, \"total\": tot, \"band\": band, \"hemi\": h, \"anova\": k,\n                                     \"comparison\": r.comparison, \"family\": r.family, \"diff\": r.diff,\n                                     \"p_family\": r.p_family, \"p_all\": r.p_all})\n    return pd.DataFrame(rows)\n\nT4 = band_tests(bp)\nw = T4[T4.family == \"within\"]\nsummary = (w.assign(sig_i=w.p_family < 0.05, sig_ii=w.p_all < 0.05)\n             .groupby([\"band\", \"segment\", \"total\", \"anova\"])[[\"sig_i\", \"sig_ii\"]].sum())\nprint(\"Number of significant within-group comparisons against baseline (of 12: 2 groups x 3 blocks x 2 hemispheres):\")\nprint(summary.unstack(\"anova\").to_string())\nprint(\"\\nThe significant ones, theta, alpha and gamma:\")\nprint(w[(w.band != \"beta\") & (w.p_family < 0.05)].round(4).to_string(index=False))\n\"\"\", [\"claim:fig4-no-theta-alpha-gamma-power-change\"])\n\ncode(r\"\"\"\nprint(\"Group mean band ratios (seizure segment, 3-300 Hz total):\")\nprint(bp[(bp.segment == \"seizure\") & (bp.total == \"total_3_300\") & (bp.block != \"post3\")]\n      .groupby([\"band\", \"hemi\", \"group\", \"block\"]).ratio.mean().unstack().round(4).to_string())\nprint(\"\\nGroup mean band ratios (whole block, 3-300 Hz total):\")\nprint(bp[(bp.segment == \"block\") & (bp.total == \"total_3_300\") & (bp.block != \"post3\")]\n      .groupby([\"band\", \"hemi\", \"group\", \"block\"]).ratio.mean().unstack().round(4).to_string())\nprint(\"\\nBetween-group comparisons (reported, not deciding), significant under the own family:\")\nb = T4[(T4.family == \"between\") & (T4.p_family < 0.05)]\nprint(b.round(4).to_string(index=False) if len(b) else \"none\")\n\"\"\", [\"claim:fig4-no-theta-alpha-gamma-power-change\"])\n\nmd(\"\"\"\n**Result: see the numbers above.**\n\"\"\")\n\nmd(\"\"\"\n## fig4c-beta-decrease\n\n> The beta power ratio of the tFUS group decreased significantly during stimulation and post 1\n> compared with baseline.\n\nReproduced when, under a combination of the M3, M5 and hemisphere readings, the condition block\nand post 1 are both significantly lower than baseline.\n\"\"\")\n\ncode(r\"\"\"\nwb = T4[(T4.band == \"beta\") & T4.comparison.isin([\"tFUS baseline-condition\", \"tFUS baseline-post1\"])]\nprint(\"tFUS beta ratio, baseline minus block (positive = decrease), with p under families (i) and (ii):\")\nprint(wb.pivot_table(index=[\"segment\", \"total\", \"anova\", \"hemi\"], columns=\"comparison\", values=[\"diff\", \"p_family\", \"p_all\"]).round(4).to_string())\nboth = wb.assign(ok=(wb.p_family < 0.05) & (wb[\"diff\"] > 0)).groupby([\"segment\", \"total\", \"anova\", \"hemi\"]).ok.sum()\nprint(\"\\nCombinations with both comparisons significant decreases (family i):\", list(both[both == 2].index))\nprint(\"\\ntFUS beta ratio means:\")\nprint(bp[(bp.band == \"beta\") & (bp.group == \"tFUS\") & (bp.block != \"post3\")].groupby([\"segment\", \"total\", \"hemi\", \"block\"]).ratio.mean().unstack().round(4).to_string())\n\"\"\", [\"claim:fig4c-beta-decrease\"])\n\nmd(\"\"\"\n**Result: see the numbers above.**\n\"\"\")\n\nmd(\"\"\"\n## figs4-sham-power-no-change\n\n> In the sham group, band power ratios show no significant change among time blocks or between\n> hemispheres.\n\nA claim of absence. Sham rats, five blocks, per band a two-way ANOVA (hemisphere by block) with\nBonferroni post hoc tests; no block or hemisphere effect nor post hoc comparison may be significant\nin any band.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor (seg, tot), d in bp[bp.group == \"sham\"].groupby([\"segment\", \"total\"]):\n    for band in tfus.BANDS:\n        dd = d[d.band == band]\n        for k, (table, post) in tfus.hemi_block_tests(dd, \"ratio\").items():\n            rows.append({\"segment\": seg, \"total\": tot, \"band\": band, \"anova\": k,\n                         \"p_hemi\": table.p.iloc[0], \"p_block\": table.p.iloc[1], \"p_interaction\": table.p.iloc[2],\n                         \"posthoc_sig_i\": int((post.p_family < 0.05).sum()), \"posthoc_sig_ii\": int((post.p_all < 0.05).sum()),\n                         \"smallest\": post.loc[post.p_family.idxmin(), \"comparison\"], \"smallest_p\": post.p_family.min()})\nS4 = pd.DataFrame(rows)\nprint(S4.round(4).to_string(index=False))\n\"\"\", [\"claim:figs4-sham-power-no-change\"])\n\nmd(\"\"\"\n**Result: see the numbers above.**\n\"\"\")\n\nmd(\"\"\"\n## fig4ef-ai-increase\n\n> The normalized asymmetry index of the tFUS group increases significantly relative to baseline in\n> the theta and alpha bands, and differs significantly from the sham group in every band.\n\nAI per rat, band and block (Eq. 1, on the band power of channels 8 and 25), normalized to the\ngroup's mean baseline AI by (a) division or (b) subtraction (M5), for the whole block and for the\nseizure periods (the union of both hemispheres' labels); group by block two-way ANOVA per band.\nReproduced when, under one combination of readings, at least one tFUS block is significantly above\nbaseline in theta and in alpha, and sham against tFUS is significant at one block or more in each\nof the four bands.\n\"\"\")\n\ncode(r\"\"\"\nd = ai[ai.block != \"post3\"].copy()\nbase = d[d.block == \"baseline\"].groupby([\"segment\", \"band\", \"group\"]).ai.mean().rename(\"base\")\nd = d.join(base, on=[\"segment\", \"band\", \"group\"])\nd[\"norm_div\"] = d.ai / d.base\nd[\"norm_sub\"] = d.ai - d.base\nprint(\"Group mean baseline AI (its sign decides what an increase means under division):\")\nprint(base.unstack().round(4).to_string())\nrows = []\nfor seg in (\"block\", \"seizure\"):\n    for norm in (\"norm_div\", \"norm_sub\"):\n        for band in tfus.BANDS:\n            dd = d[(d.segment == seg) & (d.band == band)]\n            for k, (table, post) in tfus.group_block_tests(dd, norm).items():\n                for r in post.itertuples():\n                    rows.append({\"segment\": seg, \"norm\": norm, \"band\": band, \"anova\": k, \"comparison\": r.comparison,\n                                 \"family\": r.family, \"diff\": r.diff, \"p_family\": r.p_family, \"p_all\": r.p_all})\nTA = pd.DataFrame(rows)\nprint(\"\\nGroup means of normalized AI:\")\nprint(d.groupby([\"segment\", \"band\", \"group\", \"block\"])[[\"norm_div\", \"norm_sub\"]].mean().unstack().round(3).to_string())\n\"\"\", [\"claim:fig4ef-ai-increase\"])\n\ncode(r\"\"\"\ndef ai_verdict(t):\n    up = {}\n    for band in (\"theta\", \"alpha\"):\n        x = t[(t.band == band) & t.comparison.str.startswith(\"tFUS baseline\")]\n        up[band] = bool(((x.p_family < 0.05) & (x[\"diff\"] < 0)).any())       # baseline minus block < 0: increase\n    between = {band: bool((t[(t.band == band) & (t.family == \"between\")].p_family < 0.05).any()) for band in tfus.BANDS}\n    return pd.Series({**{f\"tFUS up {k}\": v for k, v in up.items()}, **{f\"between {k}\": v for k, v in between.items()}})\n\nV = TA.groupby([\"segment\", \"norm\", \"anova\"]).apply(ai_verdict)\nprint(V.to_string())\nprint(\"\\nSignificant comparisons (own family):\")\nprint(TA[TA.p_family < 0.05].round(4).to_string(index=False))\n\"\"\", [\"claim:fig4ef-ai-increase\"])\n\nmd(\"\"\"\n**Result: see the numbers above.**\n\"\"\")\n\nmd(\"\"\"\n## figs5-seizures-lower-ai\n\n> During seizures (baseline block, after 4-AP) the asymmetry index is negative and differs from\n> zero in every band, more than in the pre-4-AP baseline state; seizures disrupt the normal\n> interhemispheric balance.\n\nThe pre-4-AP baseline state is not in the dandiset: the resting recordings of the target\nconfirmation (`EP data`, `BASELINE`) hold only the 64 intracranial channels of left S1, not the\nEEG, and no EEG recording before the first injection was deposited (the labelled blocks start\nwith the baseline block, after the monitoring block). The claim is blocked; the part that can be\nrun, seizure AI against 0 (one-sample t-tests, Fig. S5 legend) for the 16 rats and for the 10 tFUS\nrats, is shown.\n\"\"\")\n\ncode(r\"\"\"\nsa = ai[(ai.segment == \"seizure\") & (ai.block == \"baseline\")]\nrows = []\nfor rats, dd in ((\"16 rats\", sa), (\"10 tFUS rats\", sa[sa.group == \"tFUS\"])):\n    for band in tfus.BANDS:\n        x = dd[dd.band == band].ai\n        t = stats.ttest_1samp(x, 0)\n        rows.append({\"rats\": rats, \"band\": band, \"n\": len(x), \"mean AI\": x.mean(), \"sem\": x.sem(), \"t\": t.statistic, \"p\": t.pvalue})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nprint(\"\\nPre-4-AP EEG files in the dandiset: kinds of all files:\", pd.Series([m[\"kind\"] for m in tfus.read_all_meta(assets[assets['size'] < 2e9].asset_id.head(3).tolist())]).unique().tolist(), \"(see wild_type.ipynb for the full list)\")\n\"\"\", [\"claim:figs5-seizures-lower-ai\"])\n\nmd(\"\"\"\n**Result: blocked (data_missing).** See the numbers above for the part against 0.\n\"\"\")\n\nmd(\"\"\"\n## fig6-epileptic-pli-s1-decrease\n\n> In epileptic rats, the S1 PLI of the tFUS group decreases in theta, alpha, beta and gamma bands\n> during stimulation, post 1 and post 2 relative to baseline seizures, while non-S1 PLI does not\n> decrease; the decrease of S1 connectivity is significant.\n\nPLI (M6) over the seizure periods of each block (the union of both hemispheres' labels, periods of\n1 s or more), per band, averaged over the 16 S1 pairs (left S1 with right S1 channels) and the 144\nnon-S1 pairs; per seizure and averaged (reading a) or over the concatenated seizure samples\n(reading b); normalized to the group's mean baseline-block PLI by difference or ratio. Reproduced\nwhen, under one combination of readings, the tFUS S1 mean is below baseline in all four bands for\nthe condition block, post 1 and post 2, the tFUS non-S1 mean is not below baseline in most of\nthose 12 cells, and a group by block two-way ANOVA per band and region finds sham against tFUS\nsignificant for S1 in at least one band and block.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor a, r in R.items():\n    i = info.loc[a]\n    for band in tfus.BANDS:\n        v = r[\"pli\"][band]\n        if v is None:\n            continue\n        for reading in (\"per_seizure\", \"concat\"):\n            pm = tfus.pair_means(v[reading])\n            for region in (\"S1\", \"nonS1\"):\n                rows.append({\"subject\": i.subject, \"group\": i.group, \"block\": i.block, \"band\": band,\n                             \"reading\": reading, \"region\": region, \"pli\": pm[region], \"n_seizures\": v[\"n\"], \"seconds\": v[\"seconds\"]})\nP = pd.DataFrame(rows)\nP = P[P.block != \"post3\"]\nprint(\"Rat-blocks with seizure PLI:\", P[[\"subject\", \"block\"]].drop_duplicates().shape[0], \"of\", int((blocks.block != \"post3\").sum()))\nprint(\"PLI range:\", round(P.pli.min(), 3), \"to\", round(P.pli.max(), 3))\nbase = P[P.block == \"baseline\"].groupby([\"group\", \"band\", \"reading\", \"region\"]).pli.mean().rename(\"base\")\nP = P.join(base, on=[\"group\", \"band\", \"reading\", \"region\"])\nP[\"diff\"] = P.pli - P.base\nP[\"ratio\"] = P.pli / P.base\nG = P.groupby([\"reading\", \"region\", \"band\", \"group\", \"block\"])[[\"diff\", \"ratio\"]].mean()\nprint(\"\\nGroup mean normalized PLI (difference from the group's baseline):\")\nprint(G[\"diff\"].unstack().round(4).to_string())\n\"\"\", [\"claim:fig6-epileptic-pli-s1-decrease\"])\n\ncode(r\"\"\"\nrows = []\nfor reading in (\"per_seizure\", \"concat\"):\n    for norm in (\"diff\", \"ratio\"):\n        g = G[norm].unstack()\n        ref = 0.0 if norm == \"diff\" else 1.0\n        t = g.xs(\"tFUS\", level=\"group\")\n        s1 = t.xs(\"S1\", level=\"region\")[[\"condition\", \"post1\", \"post2\"]]\n        ns = t.xs(\"nonS1\", level=\"region\")[[\"condition\", \"post1\", \"post2\"]]\n        sig = []\n        for band in tfus.BANDS:\n            dd = P[(P.reading == reading) & (P.region == \"S1\") & (P.band == band)]\n            for k, (table, post) in tfus.group_block_tests(dd, norm).items():\n                for r in post[(post.family == \"between\") & (post.p_family < 0.05)].itertuples():\n                    sig.append(f\"{band} {r.comparison} [{k}] p={r.p_family:.3g}\")\n        rows.append({\"reading\": reading, \"norm\": norm, \"tFUS S1 cells below baseline (of 12)\": int((s1 < ref).sum().sum()),\n                     \"tFUS non-S1 cells not below baseline (of 12)\": int((ns >= ref).sum().sum()),\n                     \"S1 sham-tFUS significant\": \"; \".join(sig) if sig else \"none\"})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"\\nPer rat, tFUS S1 PLI difference from the group baseline, per_seizure reading:\")\nprint(P[(P.group == \"tFUS\") & (P.region == \"S1\") & (P.reading == \"per_seizure\")].pivot_table(index=[\"band\", \"subject\"], columns=\"block\", values=\"diff\").round(3).unstack(0).to_string())\n\"\"\", [\"claim:fig6-epileptic-pli-s1-decrease\"])\n\nmd(\"\"\"\n**Result: see the numbers above.**\n\"\"\")\n\nmd(\"\"\"\n## figs7-seizure-pli-s1-vs-non-s1\n\n> Comparing seizures (baseline block) with the pre-4-AP baseline state, the PLI change of S1 pairs\n> differs significantly from that of non-S1 pairs in every band.\n\n**Result: blocked (data_missing).** The change is from the pre-4-AP baseline state, whose EEG is\nnot in the dandiset (see figs5-seizures-lower-ai).\n\"\"\")\n\nmd(\"\"\"\n## Summary\n\nFilled in after the run.\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"Notebook ran in {(time.time() - started) / 60:.1f} min\")\n\"\"\")\n\nbuild((H if not DEV else \"/tmp/claude-1001/\") + (\"eeg_blocks.ipynb\" if not DEV else \"eeg_blocks_dev.ipynb\"), cells)\nprint(\"built\", len(cells))\n"
}
```

```
File created successfully at: /tmp/claude-1001/build/nb2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python build/nb2.py dev && cd entries/001683-gao-2026 && cp $TMPDIR/eeg_blocks_dev.ipynb ./_dev2.ipynb && time jupyter nbconvert --to notebook --execute _dev2.ipynb --output $TMPDIR/nb2_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | grep -v WARN | tail -5; rm -f _dev2.ipynb; cd $TMPDIR && python showout.py nb2_out.ipynb 7000 | head -150
```

```
built 33
[NbConvertApp] Converting notebook _dev2.ipynb to notebook
[NbConvertApp] Writing 80699 bytes to /tmp/claude-1001/nb2_out.ipynb

real	1m2.523s
user	0m9.870s
sys	0m0.693s
--- cell 1
dandiset 001683 version 0.260109.2104: 70 labelled blocks, 205 GB of samples

--- cell 4
Rats per group: {'sham': 6, 'tFUS': 10} ; blocks per group: {'sham': 30, 'tFUS': 40}
Blocks per rat: {'BH624': 4, 'BH626': 4, 'BH634': 4, 'BH635': 5, 'BH638': 4, 'BH642': 4, 'BH644': 4, 'BH646': 4, 'BH649': 5, 'BH650': 4, 'BH653': 4, 'BH659': 5, 'BH660': 4, 'BH662': 5, 'BH663': 5, 'BH665': 5}

Electrode table of the EEG files (x, y in mm; location):
channel      1      2      3      4      5      6      7      8      9      10     11     12     13     14     15     16     17     18     19     20     21     22     23     24     25     26     27     28     29     30     31     32
x           4.4    3.0    1.5    4.4    3.0    1.5    4.0    2.8    1.2    2.8    1.2    3.8    2.8    1.2    2.5    1.2   -1.2   -2.5   -1.2   -2.8   -3.8   -1.2   -2.8   -1.2   -2.8   -4.0   -1.5   -3.0   -4.4   -1.5   -3.0   -4.4
y          -7.0   -7.0   -7.0   -5.0   -5.0   -5.0   -3.0   -3.0   -3.0   -1.0   -1.0    0.6    1.5    1.5    3.5    3.6    3.6    3.5    1.5    1.5    0.6   -1.0   -1.0   -3.0   -3.0   -3.0   -5.0   -5.0   -5.0   -7.0   -7.0   -7.0
z           0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0    0.0
location  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull  Skull
[... 138 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python showout.py nb2_out.ipynb 9000 | grep -v "ConvergenceWarning\|res = smf" | sed -n 95,400p
```

```
seizure total_3_300 theta   ipsilateral repeated sham baseline-condition within -0.0385    0.0232 0.0387
seizure total_3_300 theta   ipsilateral repeated     sham baseline-post1 within -0.0459    0.0034 0.0056
seizure total_3_300 theta   ipsilateral repeated     sham baseline-post2 within -0.0528    0.0004 0.0007
seizure total_3_300 theta contralateral repeated     sham baseline-post2 within -0.0389    0.0110 0.0183
seizure   total_all theta   ipsilateral repeated sham baseline-condition within -0.0376    0.0219 0.0364
seizure   total_all theta   ipsilateral repeated     sham baseline-post1 within -0.0441    0.0038 0.0063
seizure   total_all theta   ipsilateral repeated     sham baseline-post2 within -0.0502    0.0006 0.0010
seizure   total_all theta contralateral repeated     sham baseline-post2 within -0.0383    0.0110 0.0184

--- cell 10

--- cell 11
Group mean band ratios (seizure segment, 3-300 Hz total):
block                      baseline  condition   post1   post2
band  hemi          group                                     
alpha contralateral sham     0.1473     0.1551  0.1535  0.1575
                    tFUS     0.1416     0.1420  0.1402  0.1216
      ipsilateral   sham     0.1458     0.1557  0.1497  0.1487
                    tFUS     0.1390     0.1363  0.1356  0.1180
beta  contralateral sham     0.4955     0.4634  0.4556  0.4524
[... 265 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/build/nb2.py'; s=open(p).read()
s=s.replace('''        g = G[norm].unstack()
        ref''','''        g = G[norm].xs(reading, level="reading").unstack()
        ref''')
open(p,'w').write(s)
p='entries/001683-gao-2026/tfus.py'; s=open(p).read()
s=s.replace('''import json
from concurrent''','''import json
import warnings
from concurrent''')
s=s.replace('''        res = smf.mixedlm(formula, d, groups=d[subject]).fit(reml=True)''','''        with warnings.catch_warnings():
            warnings.simplefilter("ignore")              # boundary fits (zero rat variance) are expected
            res = smf.mixedlm(formula, d, groups=d[subject]).fit(reml=True)''')
open(p,'w').write(s)
EOF
grep -n "^import json" -A3 entries/001683-gao-2026/tfus.py; date -u
```

```
53:import json
54-import warnings
55-from concurrent.futures import ThreadPoolExecutor
56-
Tue Nov  3 08:50:31 UTC 2026
Shell cwd was reset to
```

**Agent**

Now the wild-type data. First checking where the evoked response sits relative to the trial start times in an EP file and a PLV file.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cd entries/001683-gao-2026 && cat > $TMPDIR/dev6.py <<'EOF'
import tfus, pickle, numpy as np, pandas as pd
metas=pickle.load(open('/tmp/claude-1001/metas.pkl','rb'))
ep=[m for m in metas if m['kind']=='EP data']; plv=[m for m in metas if m['kind'].startswith('EEG data for PLV')]
print(len(ep),len(plv))
def epochs(m, t0, pre=0.1, post=0.4):
    out=[]
    for t in t0:
        i=int(round((t)*tfus.RATE)); a=i-int(pre*tfus.RATE); b=i+int(post*tfus.RATE)
        if a<0 or b>m['n_samples']: continue
        out.append(tfus.read_rows(m,a,b,threads=1))
    return np.array(out)
from concurrent.futures import ThreadPoolExecutor
for lab in ['BH624_1500_200_67_15_CENTER','BH624_BASELINE','BH624_CC_1Hz_20ms_15','BH626_1Hz_20ms_CC']:
    m=[x for x in ep+plv if x['label']==lab][0]
    st=m['intervals'].start.to_numpy()
    print(lab, 'n',len(st),'diff',np.unique(np.round(np.diff(st),3))[:5], 'dur', np.unique(np.round(m['intervals'].stop-m['intervals'].start,3)), 'first', st[0], 'T', m['n_samples']/tfus.RATE)
    def one(t): 
        i=int(round(t*tfus.RATE)); return tfus.read_rows(m,i-int(0.1*tfus.RATE),i+int(0.4*tfus.RATE),threads=1)
    with ThreadPoolExecutor(16) as ex: E=np.array(list(ex.map(one, st[:100])))
    E=E-E[:, int(0.08*tfus.RATE):int(0.1*tfus.RATE)].mean(axis=1,keepdims=True)
    mean=E.mean(axis=(0,2))*1e6
    t=(np.arange(E.shape[1])-int(0.1*tfus.RATE))/tfus.RATE*1000
    for lo in range(-100,400,20):
        sel=(t>=lo)&(t<lo+20); print(f'{lo:5d}ms {mean[sel].mean():8.2f} {np.abs(E.mean(0)[sel]).max()*1e6:8.2f}', end=' |')
    print()
EOF
PYTHONPATH=. python $TMPDIR/dev6.py
```

```
228 20
BH624_1500_200_67_15_CENTER n 249 diff [2.] dur [2.2] first 2.36576768 T 499.9610368
 -100ms    -2.40    17.90 |  -80ms     0.08     6.37 |  -60ms    -1.03     6.99 |  -40ms    -2.55     5.76 |  -20ms    -0.00     5.83 |    0ms     4.80     8.28 |   20ms     0.27     7.79 |   40ms     3.43    10.35 |   60ms     2.79     8.82 |   80ms    -2.21    15.46 |  100ms    -3.94    14.02 |  120ms    -3.00    14.60 |  140ms    -8.11    26.95 |  160ms    -5.48    24.96 |  180ms     9.54    18.46 |  200ms     6.64    15.62 |  220ms     0.62    11.52 |  240ms    -5.29    15.30 |  260ms     1.08    12.42 |  280ms    -1.80    14.46 |  300ms    -4.58    15.39 |  320ms    -4.27    13.41 |  340ms    -3.42    13.74 |  360ms    -3.46    14.00 |  380ms     0.90     6.11 |
BH624_BASELINE n 121 diff [2.] dur [2.2] first 2.39198208 T 244.27626496
 -100ms    -1.47    11.19 |  -80ms    -4.26    12.92 |  -60ms     1.10     7.33 |  -40ms     2.15     9.97 |  -20ms    -0.00     6.82 |    0ms    -4.11    12.52 |   20ms    -0.32    12.84 |   40ms     0.25     6.41 |   60ms    -0.48     5.97 |   80ms     1.95     4.55 |  100ms     2.01     6.99 |  120ms     2.54     8.38 |  140ms     6.65    10.97 |  160ms     0.15    10.49 |  180ms    -0.79     8.87 |  200ms     4.88    16.93 |  220ms     5.75    17.97 |  240ms     2.96    13.02 |  260ms     2.84     6.31 |  280ms    -2.28    16.60 |  300ms    -6.16    20.54 |  320ms    -3.64    18.64 |  340ms    -0.43    11.97 |  360ms     1.09    12.73 |  380ms    -0.89     6.62 |
BH624_CC_1Hz_20ms_15 n 251 diff [2.] dur [2.2] first 2.37195264 T 502.56150528
 -100ms    -0.08     0.84 |  -80ms    -0.13     1.03 |  -60ms    -0.11     1.01 |  -40ms    -0.03     0.65 |  -20ms     0.00     0.49 |    0ms    -0.83    10.71 |   20ms    -0.54    10.64 |   40ms     0.41     4.69 |   60ms     0.47     4.52 |   80ms     0.14     3.69 |  100ms     0.14     2.34 |  120ms     0.16     1.30 |  140ms     0.08     0.72 |  160ms    -0.01     0.98 |  180ms    -0.29     1.43 
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> tfus.py <<'EOF'


# ---------------------------------------------------------------- wild-type phase (Fig. 5)

EP_PRE, EP_POST = 0.020, 0.200        # s, the windows of Fig. 5 (-20 to 0, 0 to 20, 20 to 200 ms)
N_TRIALS = 200                        # "extracting 200 EPs" (Methods E); 200 trials per position (supplement)


def read_epochs(meta: dict, onsets: np.ndarray, pre: float = EP_PRE, post: float = EP_POST,
                threads: int = 32) -> np.ndarray:
    """Epochs (trials, samples, channels) from onset - pre to onset + post, onsets in seconds; onsets
    whose window leaves the recording are dropped."""
    n0, n1 = int(round(pre * RATE)), int(round(post * RATE))
    idx = [int(round(t * RATE)) for t in onsets]
    idx = [i for i in idx if i - n0 >= 0 and i + n1 <= meta["n_samples"]]

    def one(i):
        return read_rows(meta, i - n0, i + n1, threads=1)

    with ThreadPoolExecutor(threads) as ex:
        return np.array(list(ex.map(one, idx)))


def evoked(epochs: np.ndarray, pre: float = EP_PRE) -> np.ndarray:
    """Mean over trials after subtracting each trial's mean of the pre-onset window (the Fig. 5B
    normalization, read as a baseline subtraction in the claims file)."""
    n0 = int(round(pre * RATE))
    return (epochs - epochs[:, :n0].mean(axis=1, keepdims=True)).mean(axis=0)


def timepoint_tests(a: np.ndarray, b: np.ndarray) -> pd.DataFrame:
    """tFUS against sham at each time point, a and b of shape (rats, time), the same rats in both.

    Ordinary reading: a two-way ANOVA group by time point; the post hoc t at each time point uses the
    pooled residual mean square of the full model and its df. Repeated reading: both groups come from
    the same rats, so each comparison is a paired t on that time point's differences (the per-comparison
    error a repeated-measures analysis uses without assuming sphericity). Bonferroni over the time points."""
    from scipy import stats
    n, T = a.shape
    resid = np.concatenate([a - a.mean(0), b - b.mean(0)])
    df_res = 2 * n * T - 2 * T
    mse = (resid ** 2).sum() / df_res
    diff = a.mean(0) - b.mean(0)
    t_ord = diff / np.sqrt(mse * 2 / n)
    p_ord = 2 * stats.t.sf(np.abs(t_ord), df_res)
    t_rm, p_rm = stats.ttest_rel(a, b, axis=0)
    return pd.DataFrame({"diff": diff, "p_ordinary": np.minimum(1, p_ord * T), "p_repeated": np.minimum(1, p_rm * T)})


def wild_pli(meta: dict, n_trials: int = N_TRIALS, onsets: np.ndarray | None = None) -> dict:
    """PLI of the three windows of Fig. 5 (pre -20-0 ms, tFUS 0-20 ms, post 20-200 ms) per band, for every
    pair of one ipsilateral and one contralateral EEG channel, from the first n_trials onsets of the file's
    interval table: per trial and averaged (reading a) and over the concatenated trial samples (reading b).
    The whole recording is re-referenced (CAR), notched at 60 Hz, band filtered and Hilbert transformed
    before the epochs are cut, so the short windows carry no filter edges."""
    x = read_rows(meta, 0, meta["n_samples"])
    x = x - x.mean(axis=1, keepdims=True)
    x = _notch(x, RATE)
    if onsets is None:
        onsets = np.sort(meta["intervals"].start.to_numpy())[:n_trials]
    ii = [c - 1 for c in S1_IPSI + NONS1_IPSI]
    cc = [c - 1 for c in S1_CONTRA + NONS1_CONTRA]
    n0, n1 = int(round(EP_PRE * RATE)), int(round(EP_POST * RATE))
    w20 = int(round(0.020 * RATE))
    idx = np.array([int(round(t * RATE)) for t in onsets])
    idx = idx[(idx - n0 >= 0) & (idx + n1 <= len(x))]
    windows = {"pre": (-n0, 0), "tfus": (0, w20), "post": (w20, n1)}
    out = {"n_trials": len(idx)}
    for band in BANDS:
        ph = np.angle(signal.hilbert(signal.sosfiltfilt(band_sos(band, RATE), x, axis=0), axis=0))
        res = {}
        for name, (a, b) in windows.items():
            seg = np.stack([ph[i + a:i + b] for i in idx])            # trials, samples, channels
            d = np.sin(seg[:, :, ii][:, :, :, None] - seg[:, :, cc][:, :, None, :])
            s = np.sign(d)
            res[name] = {"per_trial": np.abs(s.mean(axis=1)).mean(axis=0), "concat": np.abs(s.mean(axis=(0, 1)))}
        out[band] = res
    return out
EOF
cd $TMPDIR && . dev/bin/activate && cd entries/001683-gao-2026 && cat > $TMPDIR/dev7.py <<'EOF'
import tfus, pickle, numpy as np, time
metas=pickle.load(open('/tmp/claude-1001/metas.pkl','rb'))
plv=[m for m in metas if m['kind'].startswith('EEG data for PLV')]
ep=[m for m in metas if m['kind']=='EP data']
t=time.time(); r=tfus.wild_pli(plv[0]); print('pli', time.time()-t, r['n_trials'])
for b in tfus.BANDS:
    print(b, {w:(tfus.pair_means(r[b][w]['per_trial']), tfus.pair_means(r[b][w]['concat'])) for w in r[b]})
m=[x for x in ep if x['label']=='BH624_1500_200_67_15_CENTER'][0]
t=time.time(); E=tfus.read_epochs(m, m['intervals'].start.to_numpy()[:200]); print('epochs', time.time()-t, E.shape)
EOF
PYTHONPATH=. /usr/bin/time -f "%e s %M KB" python $TMPDIR/dev7.py
```

```
pli 22.166593313217163 200
theta {'pre': ({'S1': 0.978688524590164, 'nonS1': 0.9776058743169398}, {'S1': 0.10203893442622951, 'nonS1': 0.11447859744990893}), 'tfus': ({'S1': 0.9780430327868852, 'nonS1': 0.9775762750455372}, {'S1': 0.1090983606557377, 'nonS1': 0.11677481785063752}), 'post': ({'S1': 0.7968249089253188, 'nonS1': 0.7961868801861971}, {'S1': 0.10196493624772314, 'nonS1': 0.11077299635701277})}
alpha {'pre': ({'S1': 0.971014344262295, 'nonS1': 0.9717497723132971}, {'S1': 0.10297131147540983, 'nonS1': 0.1459608378870674}), 'tfus': ({'S1': 0.9724180327868852, 'nonS1': 0.9726514116575592}, {'S1': 0.11009221311475409, 'nonS1': 0.1460006830601093}), 'post': ({'S1': 0.7216826047358834, 'nonS1': 0.7408323213924306}, {'S1': 0.08172586520947177, 'nonS1': 0.1372185539364501})}
beta {'pre': ({'S1': 0.8456967213114754, 'nonS1': 0.8591826047358834}, {'S1': 0.18293032786885244, 'nonS1': 0.14629439890710383}), 'tfus': ({'S1': 0.8952766393442623, 'nonS1': 0.8988353825136611}, {'S1': 0.33483606557377044, 'nonS1': 0.24462887067395267}), 'post': ({'S1': 0.37358151183970856, 'nonS1': 0.3818132716049383}, {'S1': 0.07211862477231329, 'nonS1': 0.09051406597854686})}
gamma {'pre': ({'S1': 0.6281557377049181, 'nonS1': 0.633221766848816}, {'S1': 0.0667827868852459, 'nonS1': 0.0758492714025501}), 'tfus': ({'S1': 0.605983606557377, 'nonS1': 0.6115084244080146}, {'S1': 0.0634016393442623, 'nonS1': 0.06499089253187613}), 'post': ({'S1': 0.2420662568306011, 'nonS1': 0.24173471969236995}, {'S1': 0.029184881602914388, 'nonS1': 0.047514673143088444})}
epochs 1.3238351345062256 (200, 671, 64)
24.41 s 3502820 KB
```

**Agent**

PLI works; one file takes 22 s, so the 20 PLV files go in 3 parallel processes. Checking the position labels of the EP files.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pickle,re,collections
metas=pickle.load(open('/tmp/claude-1001/metas.pkl','rb'))
ep=[m for m in metas if m['kind']=='EP data']
c=collections.Counter()
per=collections.defaultdict(list)
for m in sorted(ep,key=lambda m:(m['subject'],m['start'])):
    lab=m['label'].split('_',1)[1]
    per[m['subject']].append(lab)
for s,v in per.items(): print(s, v)
print(collections.Counter(len(m['intervals']) for m in ep))
"
```

```
BH624 ['BASELINE', '1500_200_67_15_CENTER', 'FRONT05mm_1500_15', 'BACK05mm_1500_15', 'BACK1mm_1500_15', 'FRONT1mm_1500_15', 'LSIDE05mm_1500_15', 'RSIDE05mm_1500_15', 'DEEP1mm_1500_15']
BH626 ['BASELINE', 'CENTER_1500_15', 'BACK1mm_1500_15', 'FRONT1mm_1500_15', 'FRONT05mm_1500_15', 'RSIDE05mm_1500_15', 'LSIDE05mm_1500_15']
BH634 ['BASELINE', '1500_200_67_CENTER', '1500_DEEP1mm', '1500_FRONT05mm', '1500_FRONT1mm', '1500_BACK05mm', '1500_BACK1mm', '1500_LSIDE05mm', '1500_RSIDE05mm']
BH635 ['BASELINE', '1500_200_67_CENTER', '1500_DEEP1mm', '1500_CENTER2', '1500_FRONT05mm', '1500_FRONT1mm', '1500_BACK05mm', '1500_BACK1mm', '1500_LSIDE05mm', '1500_RSIDE05mm']
BH638 ['BASELINE', '1500_200_67_CENTER', '1500_DEEP1mm', '1500_SHALLOW1mm', '1500_FRONT05mm', '1500_FRONT1mm', '1500_BACK05mm', '1500_BACK1mm', '1500_LSIDE05mm', '1500_RSIDE05mm']
BH642 ['BASELINE', '1500_200_67_CENTER', '1500_DEEP1mm', '1500_FRONT05mm', '1500_FRONT1mm', '1500_BACK05mm', '1500_BACK1mm', '1500_LSIDE05mm', '1500_RSIDE05mm']
BH644 ['BASELINE', '1500_200_67_CENTER', '1500_DEEP1mm', '1500_SHALLOW1mm', '1500_FRONT05mm', '1500_FRONT1mm', '1500_BACK1mm', '1500_BACK05mm', '1500_LSIDE05mm', '1500_RSIDE05mm']
BH645 ['BASELINE', '1500_200_CENTER', '1500_DEEP1mm', '1500_SHALLOW1mm', '1500_FRONT05mm', '1500_FRONT1mm', '1500_BACK1mm', '1500_BACK05mm', '1500_LSIDE05mm', '1500_RSIDE05mm']
BH646 ['BASELINE', '1500_200_67_CENTER', '1500_DEEP1mm', '1500_SHALLOW1mm', '1500_FRONT1mm', '1500_FRONT05mm', '1500_BACK05mm', '1500_BACK1mm', '1500_LSIDE05mm', '1500_RSIDE05mm', '1500_200_67_S1']
BH647 ['BASELINE', '1500_200_67_CENTER', '1500_DEEP_1mm', '1500_SHALLOW_1mm', '1500_FRONT_1mm', '1500_FRONT_05mm', '1500_BACK_05mm', '1500_BACK_1mm', '1500_LSIDE_05mm', '1500_RSIDE_05mm']
BH648 ['BASELINE', '1500_200_67_CENTER', '1500_SHALLOW1mm', '1500_DEEP1mm', '1500_FRONT1mm', '1500_FRONT05mm', '1500_BACK05mm', '1500_BACK1mm', '1500_LSIDE05mm', '1500_RSIDE05mm']
BH649 ['BASELINE', '1500_200_67_CENTER', '1500_DEEP1mm', '1500_SHALLOW1mm'
[... 13 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build/nb3.py",
 "content": "import sys\nsys.path.insert(0, \"/tmp/claude-1001/build\")\nfrom nbtools import build\n\nH = \"entries/001683-gao-2026/\"\ncells = []\nmd = lambda s, t=None: cells.append((\"md\", s, t))\ncode = lambda s, t=None: cells.append((\"code\", s, t))\n\nmd(r\"\"\"\n# Gao et al. (2026) on dandiset 001683: evoked potentials and PLI in wild-type rats\n\n**Paper.** Gao H, Frake A, Durand DM, He B (2026). Transcranial focused ultrasound stimulation\ntargeting white matter inhibits seizures in a rat model of epilepsy. *IEEE Trans Neural Syst Rehabil\nEng* 34, 251-259. [doi:10.1109/tnsre.2025.3644273](https://doi.org/10.1109/tnsre.2025.3644273). The\nclaims file was written from the NIH author manuscript (PMC12848950) and the supplement.\n\n**Dandiset.** [DANDI:001683](https://dandiarchive.org/dandiset/001683/0.260109.2104), version\n0.260109.2104, the only published version (the paper cites none; see `seizure_metrics.ipynb`).\n\nThe wild-type phase, before any 4-AP: the target-confirmation recordings (`EP data`: a resting\n`BASELINE` recording and one recording per transducer position, each with about 200 bursts, from\nthe 64-channel intracranial array in left S1), and one EEG recording per rat labelled\n`EEG data for PLV analysis` (32 skull channels, `*_1Hz_20ms_CC`).\n\n| Claim | Tested here |\n|---|---|\n| fig5b-tfus-evoked-potentials | yes |\n| fig5cdj-wild-type-gamma-pli-decrease | blocked (data_missing): no EEG of the resting baseline (the sham); the tFUS part is run |\n| fig5ghi-low-band-pli-s1-only | yes |\n\"\"\")\n\ncode(r\"\"\"\nimport re\nimport time\nimport warnings\nfrom concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor\nimport multiprocessing as mp\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\n\nimport tfus\n\nwarnings.filterwarnings(\"ignore\")\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 300)\n\nstarted = time.time()\nassets = tfus.list_assets()\nsmall = assets[assets[\"size\"] < 2e9]\nmetas = tfus.read_all_meta(small.asset_id.tolist())\nep = [m for m in metas if m[\"kind\"] == \"EP data\"]\nplv = [m for m in metas if m[\"kind\"].startswith(\"EEG data for PLV\")]\nprint(f\"dandiset {tfus.DANDISET_ID} version {tfus.DANDISET_VERSION}: {len(small)} files under 2 GB; \"\n      f\"EP files {len(ep)}, PLV files {len(plv)}, other {len(metas) - len(ep) - len(plv)}; read in {time.time() - started:.0f} s\")\n\"\"\")\n\nmd(\"\"\"\n## Data check\n\nEach check of the metadata against the values is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\ndef position(m):\n    lab = m[\"label\"].split(\"_\", 1)[1]\n    if lab == \"BASELINE\":\n        return \"BASELINE\"\n    lab = lab.replace(\"_\", \"\")\n    for key in (\"CENTER2\", \"CENTER\", \"SHALLOW1mm\", \"DEEP1mm\", \"FRONT05mm\", \"FRONT1mm\", \"BACK05mm\", \"BACK1mm\", \"LSIDE05mm\", \"RSIDE05mm\"):\n        if \"S1\" in lab:\n            return \"S1:\" + lab\n        if key in lab:\n            return key\n    return \"?\" + lab\n\nE = pd.DataFrame([{\"subject\": m[\"subject\"], \"label\": m[\"label\"], \"position\": position(m), \"start\": m[\"start\"],\n                   \"n_trials\": len(m[\"intervals\"]), \"seconds\": m[\"n_samples\"] / m[\"rate\"], \"channels\": m[\"n_channels\"],\n                   \"spacing\": np.median(np.diff(np.sort(m[\"intervals\"].start))), \"window\": np.median(m[\"intervals\"].stop - m[\"intervals\"].start),\n                   \"group\": m[\"group\"], \"asset_id\": m[\"asset_id\"]} for m in ep]).sort_values([\"subject\", \"start\"])\nprint(\"EP files per rat:\", E.groupby(\"subject\").size().to_dict())\nprint(\"Rats with EP files:\", E.subject.nunique(), \"(paper: 23 wild-type rats, Fig. 5B N = 23)\")\nprint(\"Positions recorded:\", E.position.value_counts().to_dict())\nprint(\"Channels:\", E.channels.unique().tolist(), \"; locations:\", sorted({tuple(m['electrodes'].location.unique()) for m in ep}),\n      \"; rate:\", sorted({m['rate'] for m in ep}))\nprint(\"Interval spacing (s):\", E.spacing.round(3).value_counts().to_dict(), \"; interval length (s):\", E.window.round(3).value_counts().to_dict())\nprint(\"Trials per file:\", E.groupby(\"position\").n_trials.agg([\"min\", \"median\", \"max\"]).to_string())\nprint(\"Tags of the EP intervals:\", sorted({t for m in ep for t in m[\"intervals\"].tag}))\nP = pd.DataFrame([{\"subject\": m[\"subject\"], \"label\": m[\"label\"], \"start\": m[\"start\"], \"n_trials\": len(m[\"intervals\"]),\n                   \"spacing\": np.median(np.diff(np.sort(m[\"intervals\"].start))), \"seconds\": m[\"n_samples\"] / m[\"rate\"],\n                   \"channels\": m[\"n_channels\"]} for m in plv]).sort_values(\"subject\")\nprint(\"\\nPLV files:\", len(P), \"rats; labels:\", sorted(P.label.str.split(\"_\", n=1).str[1].unique()))\nprint(P.to_string(index=False))\nprint(\"Rats with EP files but no PLV file:\", sorted(set(E.subject) - set(P.subject)))\nsame = all(m[\"electrodes\"][[\"x\", \"y\"]].equals(plv[0][\"electrodes\"][[\"x\", \"y\"]]) for m in plv)\nprint(\"PLV electrode tables all the same:\", same)\nother = [m for m in metas if m[\"kind\"] not in (\"EP data\",) and not m[\"kind\"].startswith(\"EEG data for PLV\")]\nprint(\"Other kinds among the small files:\", sorted({m['kind'] for m in other}))\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nThe EP files hold the 64 intracranial channels of left S1 only; there is no EEG in them. The\nresting `BASELINE` recordings last about 4 to 5 minutes and carry 120 to 151 intervals every 2 s,\ntagged `tFUS` like the stimulated ones. The PLV EEG files are recordings with 20 ms pulses\n(`1Hz_20ms_CC`), the pulse of the epilepsy experiment (Methods D), made during the wild-type\nphase, of 20 of the 23 rats. Their intervals come every 2 s in most files, every 1 s in a few. No\nEEG recording of a resting baseline (the sham of Figs. 5E-F) is in the dandiset.\n\"\"\")\n\ncode(r\"\"\"\n# Alignment of the intervals with the response: the mean EEG of the PLV files and the mean LFP of the\n# CENTER files around the interval starts, baseline-subtracted, in 10 ms bins.\ndef mean_response(m, n=100, pre=0.05, post=0.2):\n    x = tfus.read_epochs(m, np.sort(m[\"intervals\"].start.to_numpy())[:n], pre=pre, post=post)\n    x = x - x[:, :int(pre * tfus.RATE)].mean(axis=1, keepdims=True)\n    return np.abs(x.mean(axis=0)).max(axis=1) * 1e6     # peak over channels of the trial mean, uV\n\nrows = []\nfor kind, files in ((\"PLV EEG\", plv[:5]), (\"EP LFP CENTER\", [m for m in ep if position(m) == \"CENTER\"][:5]),\n                    (\"EP LFP BASELINE\", [m for m in ep if position(m) == \"BASELINE\"][:5])):\n    for m in files:\n        r = mean_response(m)\n        t = (np.arange(len(r)) - int(0.05 * tfus.RATE)) / tfus.RATE * 1000\n        rows.append({\"kind\": kind, \"subject\": m[\"subject\"], \"pre -50-0 ms\": r[t < 0].max(), \"0-40 ms\": r[(t >= 0) & (t < 40)].max(),\n                     \"40-200 ms\": r[t >= 40].max()})\nprint(\"Peak over channels of |trial mean| (uV), first 100 intervals of five files of each kind:\")\nprint(pd.DataFrame(rows).round(2).to_string(index=False))\n\"\"\", [\"sanity\"])\n\nmd(\"\"\"\nIn the PLV EEG the mean response after the interval start is many times the pre-onset level, so\nthe interval starts are the pulse onsets, in seconds (these files' tables are in seconds, unlike\nthe seizure labels). In the intracranial EP files the contrast is weaker; it is tested below.\n\n## fig5b-tfus-evoked-potentials\n\n> tFUS of the CC in wild-type rats evokes potentials in the left S1 LFP that differ significantly\n> from the sham (resting) recording at some time points.\n\nFor each rat, the LFP around the first 200 bursts of the target-confirmation recording at the\nchosen coordinates, and around pseudo onsets in the resting `BASELINE` recording, each trial\nbaseline-subtracted over -20 to 0 ms, averaged over trials. Readings of the claims file: the\nchannel, (a) the mean over the 64 channels or (b) each channel; the sham onsets, (a) every 2 s from\nthe start of the resting recording or (b) 200 onsets drawn at random (seed 0); the ANOVA, ordinary\nor repeated measures (`tfus.timepoint_tests`), Bonferroni over the time points from 0 to 200 ms.\nThe dandiset does not say which position was chosen. The paper says \"the coordinates with the\nclearest EP were used\" (supplement, Target Confirmation); two readings are run: (a) the `CENTER`\nrecording, the first estimate, and (b) the position whose channel-mean EP has the largest peak\nfrom 0 to 200 ms. The `BASELINE` file's own interval starts are shown as a third sham variant.\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(0)\nn0 = int(round(tfus.EP_PRE * tfus.RATE))\nevo = {}          # (subject, position) -> evoked (time, channels)\n\ndef ep_job(m):\n    on = np.sort(m[\"intervals\"].start.to_numpy())[:tfus.N_TRIALS]\n    return (m[\"subject\"], position(m)), tfus.evoked(tfus.read_epochs(m, on, threads=16))\n\nt0 = time.time()\nstim_files = [m for m in ep if position(m) not in (\"BASELINE\",) and not position(m).startswith(\"S1:\")]\nwith ThreadPoolExecutor(4) as ex:\n    for k, v in ex.map(ep_job, stim_files):\n        evo[k] = v\nsham = {}\nfor m in [m for m in ep if position(m) == \"BASELINE\"]:\n    T = m[\"n_samples\"] / tfus.RATE\n    grid = np.arange(2.0, T - tfus.EP_POST, 2.0)[:tfus.N_TRIALS]\n    rand = np.sort(rng.uniform(tfus.EP_PRE, T - tfus.EP_POST, tfus.N_TRIALS))\n    own = np.sort(m[\"intervals\"].start.to_numpy())[:tfus.N_TRIALS]\n    sham[m[\"subject\"]] = {name: tfus.evoked(tfus.read_epochs(m, on, threads=16)) for name, on in\n                          ((\"every 2 s\", grid), (\"random\", rand), (\"file intervals\", own))}\n    sham[m[\"subject\"]][\"n\"] = {\"every 2 s\": len(grid), \"random\": len(rand), \"file intervals\": len(own)}\nprint(f\"evoked potentials of {len(evo)} stimulated recordings and {len(sham)} resting recordings in {time.time() - t0:.0f} s\")\nprint(\"Sham onsets per rat (every 2 s):\", {s: v[\"n\"][\"every 2 s\"] for s, v in sham.items()})\n\"\"\", [\"claim:fig5b-tfus-evoked-potentials\"])\n\ncode(r\"\"\"\nt_ms = (np.arange(-n0, int(round(tfus.EP_POST * tfus.RATE))) / tfus.RATE) * 1000\npost = t_ms >= 0\nrats = sorted(sham)\npeak = {k: np.abs(v.mean(axis=1)[post]).max() for k, v in evo.items()}\nchosen_b = {s: max([k for k in evo if k[0] == s], key=lambda k: peak[k])[1] for s in rats}\nprint(\"Position with the largest channel-mean EP peak (reading b):\", pd.Series(chosen_b).value_counts().to_dict())\nrows, results = [], {}\nfor pos_reading in (\"CENTER\", \"largest\"):\n    keys = [(s, \"CENTER\" if pos_reading == \"CENTER\" else chosen_b[s]) for s in rats]\n    A = np.stack([evo[k] for k in keys])                       # rats, time, channels\n    for sham_reading in (\"every 2 s\", \"random\", \"file intervals\"):\n        B = np.stack([sham[s][sham_reading] for s in rats])\n        res = tfus.timepoint_tests(A.mean(axis=2)[:, post], B.mean(axis=2)[:, post])\n        per_ch = [tfus.timepoint_tests(A[:, post, c], B[:, post, c]) for c in range(A.shape[2])]\n        for anova in (\"ordinary\", \"repeated\"):\n            col = f\"p_{anova}\"\n            sig = res[col] < 0.05\n            rows.append({\"position\": pos_reading, \"sham onsets\": sham_reading, \"anova\": anova,\n                         \"mean of 64: significant time points\": int(sig.sum()), \"of\": len(res),\n                         \"first (ms)\": round(float(t_ms[post][sig.to_numpy()][0]), 1) if sig.any() else None,\n                         \"smallest p\": res[col].min(),\n                         \"channels with any significant point\": sum(int((r[col] < 0.05).any()) for r in per_ch)})\n        results[(pos_reading, sham_reading)] = (A, B, res)\nTB = pd.DataFrame(rows)\nprint(TB.round(5).to_string(index=False))\n\"\"\", [\"claim:fig5b-tfus-evoked-potentials\"])\n\ncode(r\"\"\"\nA, B, res = results[(\"CENTER\", \"every 2 s\")]\na, b = A.mean(axis=2) * 1e6, B.mean(axis=2) * 1e6\nfig, ax = plt.subplots(figsize=(7, 3))\nfor x, lab in ((a, \"tFUS (CENTER)\"), (b, \"sham (every 2 s)\")):\n    m, s = x.mean(0), x.std(0) / np.sqrt(len(x))\n    ax.plot(t_ms, m, label=lab); ax.fill_between(t_ms, m - s, m + s, alpha=0.3)\nsig = np.zeros(len(t_ms), bool); sig[post] = res.p_repeated.to_numpy() < 0.05\nax.fill_between(t_ms, -100, 100, where=sig, color=\"gold\", alpha=0.3, label=\"p < 0.05 (repeated)\")\nlim = np.abs(np.concatenate([a.mean(0), b.mean(0)])).max() * 1.5\nax.set_ylim(-lim, lim); ax.set_xlabel(\"ms from onset\"); ax.set_ylabel(\"channel-mean LFP (uV)\"); ax.legend(fontsize=7)\nplt.tight_layout(); plt.show()\nprint(f\"Plotted means: tFUS {a.mean(0).min():.2f} to {a.mean(0).max():.2f} uV, sham {b.mean(0).min():.2f} to {b.mean(0).max():.2f} uV; axis +/-{lim:.2f} uV holds both means\")\nprint(\"Per rat, peak |channel-mean EP| from 0 to 200 ms (uV), CENTER against sham every 2 s:\")\nprint(pd.DataFrame({\"tFUS\": np.abs(a[:, post]).max(1), \"sham\": np.abs(b[:, post]).max(1)}, index=rats).round(2).T.to_string())\n\"\"\", [\"claim:fig5b-tfus-evoked-potentials\"])\n\nmd(\"\"\"\n**Result: see the numbers above.**\n\"\"\")\n\nmd(\"\"\"\n## Wild-type PLI\n\nPLI (M6) of the PLV EEG files, first 200 pulses, in the windows pre (-20 to 0 ms), tFUS (0 to\n20 ms) and post (20 to 200 ms), for every pair of one ipsilateral and one contralateral channel:\nper trial and averaged (reading a) or over the concatenated samples of all trials (reading b).\nThe change from pre is a difference (reading a) or a ratio (reading b). The dandiset's PLV files\nare the recordings with 20 ms pulses, which fits the Methods' \"tFUS (20 ms of stimulation)\"; the\nclaims file reads the epochs as the 200 bursts of the target confirmation, whose EEG is not in the\ndandiset. These files are used, and this is recorded as a deviation.\n\"\"\")\n\ncode(r\"\"\"\nt0 = time.time()\nwith ProcessPoolExecutor(3, mp_context=mp.get_context(\"spawn\")) as ex:\n    W = dict(zip([m[\"subject\"] for m in plv], ex.map(tfus.wild_pli, plv)))\nprint(f\"PLI of {len(W)} PLV files in {time.time() - t0:.0f} s; trials per file: {sorted({v['n_trials'] for v in W.values()})}\")\nk = len(tfus.S1_IPSI)\nrows = []\nfor s, r in W.items():\n    for band in tfus.BANDS:\n        for reading in (\"per_trial\", \"concat\"):\n            pre = r[band][\"pre\"][reading]\n            for win in (\"tfus\", \"post\"):\n                x = r[band][win][reading]\n                for norm, ch in ((\"diff\", x - pre), (\"ratio\", x / pre)):\n                    rows.append({\"subject\": s, \"band\": band, \"reading\": reading, \"window\": win, \"norm\": norm,\n                                 \"S1\": ch[:k, :k].mean(), \"nonS1\": ch[k:, k:].mean(),\n                                 \"pairs decreasing\": float((x < pre).mean()), \"pre S1\": pre[:k, :k].mean(), \"pre nonS1\": pre[k:, k:].mean()})\nWP = pd.DataFrame(rows)\nprint(\"PLI before onset (pre window), mean over rats:\")\nprint(WP[(WP.norm == \"diff\") & (WP.window == \"tfus\")].groupby([\"band\", \"reading\"])[[\"pre S1\", \"pre nonS1\"]].mean().round(3).to_string())\nprint(\"\\nMean over rats of the change from pre (S1 pairs, non-S1 pairs), and the fraction of all 256 pairs that decrease:\")\nWM = WP.groupby([\"band\", \"reading\", \"norm\", \"window\"])[[\"S1\", \"nonS1\", \"pairs decreasing\"]].mean()\nprint(WM.round(4).unstack(\"window\").to_string())\n\"\"\", [\"claim:fig5cdj-wild-type-gamma-pli-decrease\", \"claim:fig5ghi-low-band-pli-s1-only\"])\n\nmd(\"\"\"\n## fig5cdj-wild-type-gamma-pli-decrease\n\n> In wild-type rats, gamma band PLI decreases during and after tFUS relative to the pre-tFUS\n> window in most brain regions, on average in both S1 and non-S1 regions, while it increases\n> slightly in the sham.\n\nThe sham (the resting baseline recording of the target confirmation) has no EEG in the dandiset,\nso the claim is blocked. The tFUS part is shown: the mean change of S1 and non-S1 pairs in both\nwindows, and the fraction of pairs that decrease.\n\"\"\")\n\ncode(r\"\"\"\ng = WM.loc[\"gamma\"]\nprint(g.round(4).unstack(\"window\").to_string())\nper_rat = WP[(WP.band == \"gamma\") & (WP.norm == \"diff\")].pivot_table(index=\"subject\", columns=[\"reading\", \"window\"], values=[\"S1\", \"nonS1\"])\nprint(\"\\nPer rat, gamma PLI difference from pre:\")\nprint(per_rat.round(4).to_string())\n\"\"\", [\"claim:fig5cdj-wild-type-gamma-pli-decrease\"])\n\nmd(\"\"\"\n**Result: blocked (data_missing).** See the numbers above for the tFUS part.\n\"\"\")\n\nmd(\"\"\"\n## fig5ghi-low-band-pli-s1-only\n\n> In wild-type rats, theta, alpha and beta PLI decrease only within the S1 regions during tFUS.\n\n\"During the tFUS conditions\" read as (a) the 0 to 20 ms window or (b) both windows. Reproduced\nwhen, under one combination of readings, the mean normalized PLI of the S1 pairs is below the\npre-tFUS reference in all three bands and the non-S1 mean is not below it in any of them.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor reading in (\"per_trial\", \"concat\"):\n    for norm in (\"diff\", \"ratio\"):\n        ref = 0.0 if norm == \"diff\" else 1.0\n        for win_reading, wins in ((\"a: 0-20 ms\", (\"tfus\",)), (\"b: both windows\", (\"tfus\", \"post\"))):\n            ok_s1, ok_ns = [], []\n            for band in (\"theta\", \"alpha\", \"beta\"):\n                for w in wins:\n                    v = WM.loc[(band, reading, norm, w)]\n                    ok_s1.append(v.S1 < ref); ok_ns.append(v.nonS1 >= ref)\n            rows.append({\"reading\": reading, \"norm\": norm, \"window\": win_reading,\n                         \"S1 below in all\": all(ok_s1), \"S1 below (cells)\": f\"{sum(ok_s1)}/{len(ok_s1)}\",\n                         \"non-S1 not below in all\": all(ok_ns), \"non-S1 not below (cells)\": f\"{sum(ok_ns)}/{len(ok_ns)}\"})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"\\nMeans over rats, theta, alpha, beta:\")\nprint(WM.loc[[\"theta\", \"alpha\", \"beta\"]].round(4).unstack(\"window\").to_string())\n\"\"\", [\"claim:fig5ghi-low-band-pli-s1-only\"])\n\nmd(\"\"\"\n**Result: see the numbers above.**\n\"\"\")\n\nmd(\"\"\"\n## Summary\n\nFilled in after the run.\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"Notebook ran in {(time.time() - started) / 60:.1f} min\")\n\"\"\")\n\nbuild(H + \"wild_type.ipynb\", cells)\nprint(\"built\", len(cells))\n"
}
```

```
File created successfully at: /tmp/claude-1001/build/nb3.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python build/nb3.py && cd entries/001683-gao-2026 && python - <<'EOF'
import nbformat
nb=nbformat.read('wild_type.ipynb',4)
c=nb.cells[1]
c.source=c.source.replace('metas = tfus.read_all_meta(small.asset_id.tolist())','import pickle\nmetas = [m for m in pickle.load(open("/tmp/claude-1001/metas.pkl","rb")) if m["subject"] in ("BH624","BH626","BH634","BH644") and m["asset_id"] in set(small.asset_id)]')
nbformat.write(nb,'_dev3.ipynb')
EOF
time jupyter nbconvert --to notebook --execute _dev3.ipynb --output $TMPDIR/nb3_dev.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | grep -v WARN | tail -3; rm -f _dev3.ipynb; cd $TMPDIR && python showout.py nb3_dev.ipynb 5000
```

```
built 21
[NbConvertApp] Converting notebook _dev3.ipynb to notebook
[NbConvertApp] Writing 110810 bytes to /tmp/claude-1001/nb3_dev.ipynb

real	1m9.043s
user	1m21.385s
sys	0m19.943s
--- cell 1
dandiset 001683 version 0.260109.2104: 248 files under 2 GB; EP files 35, PLV files 3, other 0; read in 0 s

--- cell 3
EP files per rat: {'BH624': 9, 'BH626': 7, 'BH634': 9, 'BH644': 10}
Rats with EP files: 4 (paper: 23 wild-type rats, Fig. 5B N = 23)
Positions recorded: {'BASELINE': 4, 'CENTER': 4, 'FRONT05mm': 4, 'BACK1mm': 4, 'FRONT1mm': 4, 'LSIDE05mm': 4, 'RSIDE05mm': 4, 'BACK05mm': 3, 'DEEP1mm': 3, 'SHALLOW1mm': 1}
Channels: [64] ; locations: [('Left S1',)] ; rate: [3051.7578125]
Interval spacing (s): {2.0: 27, 2.5: 8} ; interval length (s): {2.2: 35}
Trials per file:             min  median  max
position                    
BACK05mm    199   220.0  252
BACK1mm     200   235.5  253
[... 149 more lines not kept]
```

**Agent**

Subset run works. Fixing the ratio reading to use region means (per-pair ratios explode where pre-window PLI is near 0), then running notebook 3 on all rats.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/build/nb3.py'; s=open(p).read()
old='''                for norm, ch in (("diff", x - pre), ("ratio", x / pre)):
                    rows.append({"subject": s, "band": band, "reading": reading, "window": win, "norm": norm,
                                 "S1": ch[:k, :k].mean(), "nonS1": ch[k:, k:].mean(),'''
new='''                for norm in ("diff", "ratio"):
                    f = (lambda u, v: u - v) if norm == "diff" else (lambda u, v: u / v)
                    rows.append({"subject": s, "band": band, "reading": reading, "window": win, "norm": norm,
                                 "S1": f(x[:k, :k].mean(), pre[:k, :k].mean()), "nonS1": f(x[k:, k:].mean(), pre[k:, k:].mean()),'''
assert old in s; s=s.replace(old,new)
s=s.replace('''The change from pre is a difference (reading a) or a ratio (reading b). The dandiset's''','''The change from pre is a difference (reading a) or a ratio (reading b), of the mean over the pairs
of a region (for the ratio, the region's mean PLI over its mean pre PLI, a standard choice, as
pair-wise ratios explode where the pre PLI is near 0). The dandiset's''')
open(p,'w').write(s)
EOF
. dev/bin/activate && python build/nb3.py && cd entries/001683-gao-2026 && time jupyter nbconvert --to notebook --execute wild_type.ipynb --output $TMPDIR/nb3_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | grep -v WARN | tail -2; cd $TMPDIR && python showout.py nb3_out.ipynb 5000 | sed -n 1,400p | grep -v "^$" | head -230
```

```
built 21
[NbConvertApp] Converting notebook wild_type.ipynb to notebook
[NbConvertApp] Writing 109678 bytes to /tmp/claude-1001/nb3_out.ipynb

real	7m51.539s
user	7m31.749s
sys	2m4.320s
--- cell 1
dandiset 001683 version 0.260109.2104: 248 files under 2 GB; EP files 228, PLV files 20, other 0; read in 146 s
--- cell 3
EP files per rat: {'BH624': 9, 'BH626': 7, 'BH634': 9, 'BH635': 10, 'BH638': 10, 'BH642': 9, 'BH644': 10, 'BH645': 10, 'BH646': 11, 'BH647': 10, 'BH648': 10, 'BH649': 10, 'BH650': 10, 'BH651': 10, 'BH652': 13, 'BH653': 10, 'BH659': 10, 'BH660': 10, 'BH661': 10, 'BH662': 10, 'BH663': 10, 'BH665': 10, 'BH666': 10}
Rats with EP files: 23 (paper: 23 wild-type rats, Fig. 5B N = 23)
Positions recorded: {'BASELINE': 23, 'CENTER': 23, 'FRONT05mm': 23, 'BACK1mm': 23, 'FRONT1mm': 23, 'LSIDE05mm': 23, 'RSIDE05mm': 23, 'BACK05mm': 22, 'DEEP1mm': 22, 'SHALLOW1mm': 18, 'CENTER2': 1, 'S1:150020067S1': 1, 'S1:1500S1SHALLOW1mm': 1, 'S1:1500S1L05F1mm': 1, 'S1:1500S1R05B05mm': 1}
Channels: [64] ; locations: [('Left S1',)] ; rate: [3051.7578125]
Interval spacing (s): {2.0: 220, 2.5: 8} ; interval length (s): {2.2: 228}
Trials per file:                      min  median  max
position                             
BACK05mm             199   200.0  252
BACK1mm              200   200.0  253
BASELINE             120   150.0  175
[... 178 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/build/nb3.py'; s=open(p).read()
old='''print(pd.DataFrame(rows).to_string(index=False))
print("\\nMeans over rats, theta, alpha, beta:")'''
new='''print(pd.DataFrame(rows).to_string(index=False))
rows = []
for reading in ("per_trial", "concat"):
    for norm in ("diff", "ratio"):
        ref = 0.0 if norm == "diff" else 1.0
        for win_reading, wins in (("a: 0-20 ms", ("tfus",)), ("b: both windows", ("tfus", "post"))):
            bands_ok = [band for band in ("theta", "alpha", "beta")
                        if all(WM.loc[(band, reading, norm, w)].S1 < ref and WM.loc[(band, reading, norm, w)].nonS1 >= ref for w in wins)]
            rows.append({"reading": reading, "norm": norm, "window": win_reading, "bands with S1 below and non-S1 not below": ", ".join(bands_ok) or "none"})
print("\\nPer band:")
print(pd.DataFrame(rows).to_string(index=False))
print("\\nMeans over rats, theta, alpha, beta:")'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
grep -n "Per band" build/nb3.py
```

```
Tue Nov  3 09:03:02 UTC 2026
328:print("\nPer band:")
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python build/nb2.py dev >/dev/null && cd entries/001683-gao-2026 && cp $TMPDIR/eeg_blocks_dev.ipynb ./_dev2.ipynb && jupyter nbconvert --to notebook --execute _dev2.ipynb --output $TMPDIR/nb2_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | grep -v WARN | tail -1; rm -f _dev2.ipynb; cd $TMPDIR && python showout.py nb2_out.ipynb 9000 | grep -A12 "reading  norm  tFUS"
```

```
[NbConvertApp] Writing 66346 bytes to /tmp/claude-1001/nb2_out.ipynb
    reading  norm  tFUS S1 cells below baseline (of 12)  tFUS non-S1 cells not below baseline (of 12) S1 sham-tFUS significant
per_seizure  diff                                     8                                             4                     none
per_seizure ratio                                     8                                             4                     none
     concat  diff                                     6                                             4                     none
     concat ratio                                     6                                             4                     none

Per rat, tFUS S1 PLI difference from the group baseline, per_seizure reading:
block   baseline                      condition                       post1                       post2                     
band       alpha   beta  gamma  theta     alpha   beta  gamma  theta  alpha   beta  gamma  theta  alpha   beta  gamma  theta
subject                                                                                                                     
BH624     -0.051 -0.010 -0.010 -0.064    -0.032 -0.035 -0.017 -0.069  0.064  0.023  0.027 -0.012  0.009  0.010  0.008  0.048
BH626      0.010 -0.022 -0.016  0.092    -0.052 -0.011 -0.003 -0.065 -0.013 -0.043  0.012 -0.086 -0.041 -0.037  0.012 -0.118
BH634      0.018 -0.010 -0.034 -0.037     0.040 -0.002 -0.032 -0.120 -0.049  0.092  0.032 -0.038    NaN    NaN    NaN    NaN
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import json,collections
r=json.load(open('survey.json'))
print(collections.Counter((x.get('general/subject/age'),x.get('general/subject/description')) for x in r))
print(collections.Counter(x['general/subject/subject_id'] for x in r if x['session_description']=='Labeled_data' and x['identifier']=='sham group'))
"
```

```
Counter({('P24W', 'HSD:WI rat'): 318})
Counter({'BH649': 5, 'BH659': 5, 'BH662': 5, 'BH663': 5, 'BH665': 5, 'BH635': 5})
Shell cwd was reset to
```

**Agent**

Now writing the conclusion cells for notebook 1.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/build/nb1.py'; s=open(p).read()
old_2c='''**Result: not reproduced.** Under the per-seizure reading the block effect is significant
(ordinary p printed above), and post hoc tests find blocks that differ; the per-rat reading is
printed above too. The paper's test, as the claims file has it, finds an effect of block on
seizure duration in the sham group.'''
new_2c='''**Result: not reproduced.** The effect of block on sham seizure duration is significant under
every reading: per seizure, F = 30.45, p = 5.5e-24 (ordinary) and p = 2.4e-31 (repeated), with 12
and 13 of 25 post hoc comparisons significant; per rat, p = 0.00145 (ordinary, no post hoc
comparison significant) and p = 3.9e-05 (repeated, contralateral baseline against post 3
significant). The hemisphere effect is not significant under any reading (p = 0.16 to 0.63). Mean
durations fall from 49.6 to 53.0 s at baseline to 34.8 to 35.7 s at post 3.'''
assert old_2c in s; s=s.replace(old_2c,new_2c)
s=s.replace('''**Result: reproduced.** In each hemisphere far more than half of the sham seizures last under
120 s (fractions printed above), and the medians of the two hemispheres are close; the KS test
does not decide.''','''**Result: reproduced.** 99.4% of the 527 ipsilateral and 99.2% of the 521 contralateral sham
seizures last under 120 s, with medians of 41.5 and 43.5 s; every rat is at 97% or more. The KS test
(D = 0.082, p = 0.056) is description and does not decide.''')
s=s.replace('''**Result: reproduced.** Neither main effect nor any post hoc comparison is significant under
either ANOVA reading (printed above), and the mean count is lower in post 2 and post 3 than in
the first three blocks.''','''**Result: reproduced.** No main effect is significant (block p = 0.97 ordinary and 0.82 repeated;
hemisphere p = 0.93 and 0.88) and no post hoc comparison is (smallest Bonferroni p = 1). The mean
count is 18.11 over baseline to post 1 and 16.50 over post 2 and post 3, the slight decrease the
paper describes. With BH635's blocks taken by their labels the block effect stays non-significant
(p = 0.66 and 0.61).''')
res=[
# fig2f
'''**Result: reproduced, resting on assumptions.** Under the repeated-measures reading the
contralateral comparison of baseline (reading b of "sham") with post 3 is significant (Bonferroni
p = 0.021 in its family, 0.026 over all), a decrease from 25.6% to 15.5%; condition against post 3
is not (p = 0.096). Under the ordinary reading no comparison is significant (p = 1). The result
rests on the repeated-measures reading and on taking BH635's files in time order: with BH635 by
its labels the comparison is not significant (p = 0.083).''',
# fig3a-count-reduction
'''**Result: reproduced.** Under reading (b) of M4, each rat's change from its own baseline, the six
decreases are 8.7%, 36.4% and 41.9% (ipsilateral) and 10.5%, 41.4% and 42.4% (contralateral), all
within tolerance of 9, 36, 42, 10, 41 and 42; reading (a) gives 24 to 50%, outside. Under the
repeated-measures reading baseline against post 1 and against post 2 are significant in both
hemispheres (Bonferroni p = 0.0085 and 0.0039 ipsilateral, 0.0054 and 0.0024 contralateral, in the
`within` family; 0.014, 0.0065, 0.009 and 0.004 over all ten). Under the ordinary reading none of
the four is significant (p = 0.057 to 0.115).''',
# fig3a-count-sham-vs-tfus
'''**Result: reproduced.** Under the repeated-measures reading with the `between` family, sham
against tFUS is significant at post 1 and post 2 in the ipsilateral S1 (p = 0.026 and 0.046),
reading (b) of the hemisphere; in the contralateral S1 post 1 is significant (p = 0.018) and post 2
is not (p = 0.057). Under the ordinary reading post 1 is significant in both hemispheres (0.035,
0.025) and post 2 in neither (0.057, 0.069). No sham block differs from sham baseline (p = 1 under
both readings).''',
# fig3b-percent-time-reduction
'''**Result: reproduced.** The decreases under reading (b) of M4 are 32.5% and 34.8% (stimulation),
55.5% and 55.3% (post 1), 54.9% and 55.2% (post 2), ipsilateral and contralateral, all within
tolerance; reading (a) gives 35.8% to 57.3%, also within. Under the repeated-measures reading all
six comparisons with baseline are significant (Bonferroni p from 0.0007 down to below 0.0001), so
reading (a) of "significantly" holds; under the ordinary reading post 1 and post 2 are (p = 0.008
to 0.012) and stimulation is not (p = 0.22 and 0.17).''',
# fig3b-sham-no-change
'''**Result: not reproduced, resting on an assumption.** The two ANOVA readings disagree. Under
the ordinary reading no sham block differs from baseline (smallest Bonferroni p = 0.79). Under the
repeated-measures reading, adopted here as the paper's test (see the summary), post 2 differs from
baseline in both hemispheres (p = 0.043 ipsilateral, 0.021 contralateral; over all ten comparisons
0.072 and 0.036). The sham percent time falls from 24.0% to 16.4% (ipsilateral) and from 25.6% to
17.6% (contralateral).''',
# fig3b-sham-vs-tfus
'''**Result: not reproduced.** tFUS is lower than sham in all three named comparisons (by 11.4,
9.8 and 10.0 percentage points), but none is significant under either reading: contralateral
post 1 p = 0.062 (repeated) and 0.075 (ordinary), ipsilateral stimulation 0.12 and 0.14,
ipsilateral post 1 0.11 and 0.13, in the `between` family.''',
# fig3c-interval-increase
'''**Result: reproduced, resting on an assumption.** With the interval read as the gap between one
seizure's end and the next one's start, and reading (b) of M4, the increases are 27.4%, 49.1% and
27.8% (ipsilateral) and 30.1%, 51.9% and 30.9% (contralateral), all within tolerance. Under the
repeated-measures reading with all ten comparisons in one family, contralateral post 1 is the only
significant comparison with baseline (p = 0.0056; ipsilateral post 1 p = 0.060, the others 0.59 or
more); with the `within` family ipsilateral post 1 is significant too (p = 0.036). The ordinary
reading finds none (contralateral post 1 p = 0.18). The onset-to-onset reading gives increases of
12.6% to 30.6%, outside tolerance, so the outcome rests on the gap reading, which the paper's
"time between neighboring seizures" favours.''',
# fig3c-interval-sham-vs-tfus
'''**Result: reproduced.** Under the repeated-measures reading with the `between` family, sham
against tFUS at post 1 is significant in both hemispheres with tFUS higher (by 122 s ipsilateral,
p = 0.039; by 140 s contralateral, p = 0.018); the onset-to-onset interval gives the same (p = 0.044
and 0.020). Under the ordinary reading the ipsilateral comparison is not significant (p = 0.051).
No sham block differs from sham baseline (p = 1). No single Bonferroni family gives both this
claim and fig3c-interval-increase: with all ten comparisons in one family the ipsilateral
comparison here is p = 0.096.''',
# fig3d
'''**Result: not reproduced.** The group means decline from baseline to post 2 in both groups
(tFUS 59.8 to 48.7 s ipsilateral and 61.0 to 49.9 s contralateral; sham 53.0 to 37.8 s and 56.8 to
40.6 s), but tFUS baseline against post 2 is not significant in either hemisphere (Bonferroni
p = 0.37 and 0.29 repeated, 0.62 and 0.59 ordinary), nor is any other within-group comparison
against baseline (smallest p = 0.13).''',
]
parts=s.split('''**Result: see the numbers above.**''')
assert len(parts)==len(res)+1, len(parts)
out=parts[0]
for r,pp in zip(res,parts[1:]): out+=r+pp
open(p,'w').write(out)
EOF
echo done
```

```
done
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/build/nb1.py'; s=open(p).read()
s=s.replace("p = 0.060, the others 0.59 or\nmore)","p = 0.060, the others 0.65 or\nmore)")
assert "0.65 or\nmore" in s
old='''md("""
## fig3b-percent-time-sham-vs-tfus'''
new='''code(r"""
# Variant: BH635's blocks by their labels (seizure_metrics data check). Sham comparisons, repeated reading.
for value in ("count", "percent_time", "isi_gap", "duration"):
    for h in ("ipsilateral", "contralateral"):
        table, post = group_tests(met_alt, value, h)["repeated"]
        p = post[post.comparison.str.startswith("sham baseline") | (post.family == "between")]
        print(value, h, {r.comparison: round(r.p_family, 4) for r in p.itertuples()})
""", ["claim:fig3b-sham-percent-time-no-change"])

md("""
## fig3b-percent-time-sham-vs-tfus'''
assert old in s; s=s.replace(old,new,1)
open(p,'w').write(s)
EOF
. dev/bin/activate && python build/nb1.py && cd entries/001683-gao-2026 && jupyter nbconvert --to notebook --execute seizure_metrics.ipynb --output $TMPDIR/nb1_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | grep -v WARN | tail -1; cd $TMPDIR && python showout.py nb1_out.ipynb 3000 | grep "^count\|^percent_time\|^isi_gap\|^duration"
```

```
built 53
[NbConvertApp] Writing 173088 bytes to /tmp/claude-1001/nb1_out.ipynb
count: tFUS change from baseline, %, reading (a) ratio of group means:
percent_time: tFUS change from baseline, %, reading (a) ratio of group means:
count ipsilateral {'sham baseline-condition': 1.0, 'sham baseline-post1': 1.0, 'sham baseline-post2': 1.0, 'sham-tFUS baseline': 1.0, 'sham-tFUS condition': 0.2733, 'sham-tFUS post1': 0.044, 'sham-tFUS post2': 0.0289}
count contralateral {'sham baseline-condition': 1.0, 'sham baseline-post1': 1.0, 'sham baseline-post2': 1.0, 'sham-tFUS baseline': 1.0, 'sham-tFUS condition': 0.2408, 'sham-tFUS post1': 0.044, 'sham-tFUS post2': 0.0329}
percent_time ipsilateral {'sham baseline-condition': 1.0, 'sham baseline-post1': 0.4294, 'sham baseline-post2': 0.1264, 'sham-tFUS baseline': 1.0, 'sham-tFUS condition': 0.1112, 'sham-tFUS post1': 0.2658, 'sham-tFUS post2': 0.4311}
percent_time contralateral {'sham baseline-condition': 1.0, 'sham baseline-post1': 0.1355, 'sham baseline-post2': 0.0136, 'sham-tFUS baseline': 1.0, 'sham-tFUS condition': 0.1223, 'sham-tFUS post1': 0.2027, 'sham-tFUS post2': 0.4523}
isi_gap ipsilateral {'sham baseline-condition': 1.0, 'sham baseline-post1': 1.0, 'sham baseline-post2': 1.0, 'sham-tFUS baseline': 0.8521, 'sham-tFUS condition': 0.7948, 'sham-tFUS post1': 0.0476, 'sham-tFUS post2': 0.3896}
isi_gap contralateral {'sham baseline-condition': 1.0, 'sham baseline-post1': 1.0, 'sham baseline-post2': 1.0, 'sham-tFUS baseline': 0.8654, 'sham-tFUS condition': 0.8187, 'sham-tFUS post1': 0.026, 'sham-tFUS post2': 0.4396}
duration ipsilateral {'sham baseline-condition': 1.0, 'sham baseline-post1': 0.978, 'sham baseline-post2': 0.3145, 'sham-tFUS baseline': 1.0, 'sham-tFUS condition': 1.0, 'sham-tFUS post1': 1.0, 'sham-tFUS post2': 0.7495}
duration contralateral {'sham baseline-condition': 1.0, 'sham baseline-post1': 0.3943, 'sham baseline-post2': 0.0949, 'sham-tFUS baseline': 1.0, 'sham-tFUS condition': 1.0, 'sham-tFUS post1': 1.0, '
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/build/nb1.py'; s=open(p).read()
s=s.replace('''0.072 and 0.036). The sham percent time falls from 24.0% to 16.4% (ipsilateral) and from 25.6% to
17.6% (contralateral).''','''0.072 and 0.036). The sham percent time falls from 24.0% to 16.4% (ipsilateral) and from 25.6% to
17.6% (contralateral). With BH635's blocks by their labels, contralateral post 2 is still
significant (p = 0.014) and ipsilateral is not (p = 0.13).''')
old='''md("""
## Summary

Filled in after the run.
""")'''
new='''md("""
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

| Claim | Notebook | Outcome |
|---|---|---|
| fig2c-sham-duration-stable | seizure_metrics | not reproduced |
| fig2d-seizures-under-two-minutes | seizure_metrics | reproduced |
| fig2e-sham-count-stable | seizure_metrics | reproduced |
| fig2f-sham-percent-time-post3 | seizure_metrics | reproduced (assumed) |
| fig3a-count-reduction | seizure_metrics | reproduced |
| fig3a-count-sham-vs-tfus | seizure_metrics | reproduced |
| fig3b-percent-time-reduction | seizure_metrics | reproduced |
| fig3b-sham-percent-time-no-change | seizure_metrics | not reproduced (assumed) |
| fig3b-percent-time-sham-vs-tfus | seizure_metrics | not reproduced |
| fig3c-interval-increase | seizure_metrics | reproduced (assumed) |
| fig3c-interval-sham-vs-tfus | seizure_metrics | reproduced |
| fig3d-duration-decline | seizure_metrics | not reproduced |
| fig4-no-theta-alpha-gamma-power-change | eeg_blocks | not reproduced (assumed) |
| fig4c-beta-decrease | eeg_blocks | partially reproduced |
| figs4-sham-power-no-change | eeg_blocks | not reproduced (assumed) |
| fig4ef-ai-increase | eeg_blocks | partially reproduced |
| figs5-seizures-lower-ai | eeg_blocks | blocked: data missing |
| fig6-epileptic-pli-s1-decrease | eeg_blocks | partially reproduced |
| figs7-seizure-pli-s1-vs-non-s1 | eeg_blocks | blocked: data missing |
| fig5b-tfus-evoked-potentials | wild_type | blocked: methods underspecified |
| fig5cdj-wild-type-gamma-pli-decrease | wild_type | blocked: data missing |
| fig5ghi-low-band-pli-s1-only | wild_type | not reproduced |

**How the analysis differs from the paper's.** The seizure labels are the dandiset's own, so the
metrics rest on the paper's labelling. The label times are in minutes and are converted. The
percent changes of Fig. 3 match the paper to within one point under reading (b) of M4 (each rat's
change from its own baseline), and the inter-seizure interval matches only when read as the gap
from one seizure's end to the next one's start, so both readings are the paper's. The paper's
two-way ANOVA is not specified further. Its significant within-group changes of Fig. 3 (count and
percent time against baseline, the interval at contralateral post 1) appear only under the
repeated-measures reading, implemented here as a mixed model with a random intercept per rat, so
that reading is adopted as an assumption where the readings disagree on a claim of absence. The
Bonferroni family is not specified either; both readings are shown and no single one gives every
significance claim the paper makes. BH635's five sham files are taken in time order though their
labels say otherwise.

**What was found about the dataset.** It holds the paper's 16 epileptic rats (10 tFUS, 6 sham)
with the seizure labels, and the percent changes computed from them match the paper's. The label
table gives times in minutes, not the seconds NWB prescribes (the EEG check in `eeg_blocks.ipynb`
confirms it). BH635's block files are mislabelled (two `SHAM` files, one named for rat BH636, no
`post3`), and BH649's post 3 file has the session id `None`. Every file gives the strain as
"HSD:WI rat" (Wistar) and the age as P24W, while the paper used Sprague-Dawley rats of 3 to 6
months. The labelling channels are not named in the files.
""")'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent**

Writing the conclusions and summaries for notebooks 2 and 3.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/build/nb2.py'; s=open(p).read()
s=s.replace('''print("\\nPre-4-AP EEG files in the dandiset: kinds of all files:", pd.Series([m["kind"] for m in tfus.read_all_meta(assets[assets['size'] < 2e9].asset_id.head(3).tolist())]).unique().tolist(), "(see wild_type.ipynb for the full list)")
''','')
assert 'Pre-4-AP EEG files' not in s
res=[
'''**Result: not reproduced, resting on an assumption.** The ANOVA readings disagree, and the M5
readings agree within each. Under the ordinary reading no within-group comparison against baseline
is significant for theta, alpha or gamma under any of the four M5 readings. Under the
repeated-measures reading, adopted as the paper's test (see the summary), the sham theta ratio
rises above baseline in 4 or 5 of the 12 comparisons under every M5 reading (ipsilateral post 2:
p = 0.009 over the whole block, where the 3-300 Hz ratio goes from 0.098 to 0.136, and p = 0.0004
over the seizure periods), and the tFUS gamma ratio differs at ipsilateral post 2 with the 0 Hz to
Nyquist total (p = 0.043). Alpha has none. No between-group comparison is significant.''',
'''**Result: partially reproduced.** Over the whole block under the repeated-measures reading the
tFUS beta ratio at post 1 is significantly below baseline in both hemispheres (3-300 Hz total:
p = 0.0028 ipsilateral, 0.026 contralateral; 0 Hz to Nyquist: 0.0005 and 0.0094), but the condition
block is not (p = 0.16 to 0.60), although its mean is lower (ipsilateral 0.445 at baseline, 0.417
at the condition block). Over the seizure periods the beta ratio does not fall (ipsilateral 0.493,
0.487 and 0.500) and no comparison is significant. Under the ordinary reading none is.''',
'''**Result: not reproduced, resting on an assumption.** Beta varies with block and hemisphere: over
the whole block the block and hemisphere effects are significant under both readings (ordinary
block p = 0.0004 and 0.0002 for the two totals, hemisphere p below 0.0001, with 4 and 5 post hoc
comparisons significant), and over the seizure periods under the repeated-measures reading (block
p = 0.0009 and 0.0007, 2 post hoc comparisons). Gamma has a hemisphere effect over the whole block
(ordinary p = 0.0037 and 0.0004). Under the ordinary reading over the seizure periods nothing is
significant in any band (smallest p = 0.09), so the M5 readings disagree under that ANOVA reading;
under the repeated-measures reading, the one adopted, they agree.''',
'''**Result: partially reproduced.** The mean baseline AI is negative in both groups (whole block:
sham -0.58 to -0.61, tFUS -0.24 to -0.29), so the two normalizations read an increase in opposite
directions. With subtraction (reading b), the whole block and the repeated-measures reading, the
normalized AI of the tFUS group rises above baseline, toward balance, in theta (post 1 p = 0.033,
post 2 p = 0.0047) and alpha (post 2 p = 0.0057). Sham against tFUS is not significant in any
band, block or combination of readings. With division the same change appears as a significant
fall (theta post 2 p = 0.0006), and over the seizure periods nothing is significant.''',
]
parts=s.split('''**Result: see the numbers above.**''')
assert len(parts)==6, len(parts)
fig6='''**Result: partially reproduced.** Per seizure and averaged (reading a of M6), the tFUS S1 PLI is
below the group's baseline in 8 of the 12 band and block cells: in theta and alpha at all three
blocks (alpha -0.026, -0.032 and -0.057), in beta only at the condition block and in gamma only at
post 1; over the concatenated seizure samples, 6 of 12. The non-S1 PLI falls too: it is not below
baseline in only 4 of 12 cells, so that part of the claim fails. No sham against tFUS comparison of
S1 PLI is significant in any band or block under either ANOVA reading. The criterion's partial
outcome (S1 decreases in some bands only, without a significant group difference) is the one that
applies; the S1 specificity the claim describes is not seen, and the sham S1 PLI falls as much in
theta (-0.022 to -0.080).'''
out=parts[0]
for r,pp in zip(res+[fig6],parts[1:]): out+=r+pp
s=out
s=s.replace('''**Result: blocked (data_missing).** See the numbers above for the part against 0.''','''**Result: blocked (data_missing).** The pre-4-AP state the claim compares with is not in the
dandiset. The part that can be run holds: the seizure AI of the baseline block is negative in every
band, -0.41 to -0.43 over the 16 rats (p < 0.0001 in each band) and -0.27 to -0.30 over the 10
tFUS rats (p = 0.0001 to 0.0012).''')
old='''md("""
## Summary

Filled in after the run.
""")'''
new='''md("""
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| fig4-no-theta-alpha-gamma-power-change | not reproduced (assumed) |
| fig4c-beta-decrease | partially reproduced |
| figs4-sham-power-no-change | not reproduced (assumed) |
| fig4ef-ai-increase | partially reproduced |
| figs5-seizures-lower-ai | blocked: data missing |
| fig6-epileptic-pli-s1-decrease | partially reproduced |
| figs7-seizure-pli-s1-vs-non-s1 | blocked: data missing |

The outcomes of the other fifteen claims are in `seizure_metrics.ipynb` and `wild_type.ipynb`.

**How the analysis differs from the paper's.** No ICA is applied: which components the authors
removed is not recorded. The EEG is re-referenced to the common average and notched at 60 Hz, as
in Methods C. The labelling channels 8 and 25 are read from the drawing of Fig. S1 and the S1
channels from the notes of the dandiset's PLV files; the paper's text lists neither. The segment
analysed, the total of the band ratio and the normalization of AI and PLI are not fixed by the
paper and are run under each reading. The repeated-measures ANOVA reading is adopted where the
ANOVA readings disagree on a claim of absence, as in `seizure_metrics.ipynb`. During the condition
block of the tFUS rats the EEG carries the pulse responses at 1 Hz; the paper does not say whether
they were removed, and they are not.

**What was found about the dataset.** The seizure labels share the EEG's clock and are in minutes:
30 to 80 Hz power inside them is 2.6 to 50 times that outside, and the contrast is gone when they
are shifted by a minute or read as seconds. The pre-4-AP EEG of Figs. S5 and S7 is not in the
dandiset. The baseline AI is strongly negative in both groups (contralateral channel power several
times the ipsilateral), which the paper does not report.
""")'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)

p='/tmp/claude-1001/build/nb3.py'; s=open(p).read()
parts=s.split('''**Result: see the numbers above.**''')
assert len(parts)==3, len(parts)
r1='''**Result: blocked (methods_underspecified).** The readings the criterion names disagree. With the
mean over the 64 channels, one of the twelve combinations of position, sham onsets and ANOVA finds
significant time points (CENTER position, random sham onsets, ordinary reading: 13 of 610 points
from 66.5 ms, smallest Bonferroni p = 0.013); the other eleven find none (smallest p = 0.05 to 1).
With each channel tested, 0 to 39 of the 64 channels have a significant point, depending on the
combination. The mean channel-mean EP at the CENTER position reaches 3.1 uV, the sham 1.7 uV. The
criterion blocks the claim when the readings disagree; which channels, which position and which
sham onsets the paper used are questions for its authors.'''
r2='''**Result: not reproduced.** In no band and under no combination of readings does the S1 PLI fall
while the non-S1 PLI does not. In the 0 to 20 ms window the S1 PLI does not fall in theta, alpha or
beta under any reading (differences +0.0002 to +0.070); in the 20 to 200 ms window both regions
fall together (alpha -0.017 for S1 and -0.021 for non-S1 pairs, concatenated reading). The
per-trial PLI of the 20 ms pre window is near 1 in theta and alpha (0.98 and 0.97), so per-trial
changes to the longer post window reflect the window lengths as much as the stimulation.'''
s=parts[0]+r1+parts[1]+r2+parts[2]
s=s.replace('''**Result: blocked (data_missing).** See the numbers above for the tFUS part.''','''**Result: blocked (data_missing).** Without the resting-state EEG the sham part cannot be tested.
In the tFUS part the gamma PLI falls in the 20 to 200 ms window in both regions under every reading
(S1 -0.029 and non-S1 -0.016 over concatenated samples; -0.386 and -0.386 per trial), with 62%
(concatenated) or 100% (per trial) of the 256 pairs decreasing. In the 0 to 20 ms window it falls
under the per-trial reading (S1 -0.013, non-S1 -0.024, 69% of pairs) and not over concatenated
samples (+0.002 and +0.005, 47% of pairs).''')
old='''md("""
## Summary

Filled in after the run.
""")'''
new='''md("""
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| fig5b-tfus-evoked-potentials | blocked: methods underspecified |
| fig5cdj-wild-type-gamma-pli-decrease | blocked: data missing |
| fig5ghi-low-band-pli-s1-only | not reproduced |

The outcomes of the other nineteen claims are in `seizure_metrics.ipynb` and `eeg_blocks.ipynb`.

**How the analysis differs from the paper's.** The position whose bursts form the tFUS EPs is not
recorded; the CENTER recording and the position with the largest EP are both run. The wild-type
PLI uses the dandiset's PLV EEG files, recordings with 20 ms pulses, since the EEG of the
target-confirmation bursts is not in the dandiset; the Methods' "tFUS (20 ms of stimulation)" fits
these files. For the repeated-measures reading of the EP test the tFUS-sham comparison at each time
point is a paired t-test.

**What was found about the dataset.** The EP files of all 23 rats are there, one per transducer
position plus a resting recording, with interval tables in seconds whose starts are the burst
onsets. The resting recordings hold no EEG, so the sham of Figs. 5E-F cannot be computed. The PLV
EEG files cover 20 of the 23 rats (not BH638, BH642, BH644). The chosen position is not recorded.
""")'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
. dev/bin/activate && python build/nb1.py && python build/nb2.py && python build/nb3.py; date -u
```

```
built 53
built 33
built 21
Tue Nov  3 09:08:00 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/build/nb2.py'; s=open(p).read()
s=s.replace("30 to 80 Hz power inside them is 2.6 to 50 times that outside","30 to 80 Hz power inside them is 2.5 to 50 times that outside")
s=s.replace("The baseline AI is strongly negative in both groups (contralateral channel power several\ntimes the ipsilateral), which the paper does not report.","The baseline AI is strongly negative in both groups (mean contralateral band power about 1.7\n(tFUS) to 4 (sham) times the ipsilateral), which the paper does not report.")
assert "1.7\n(tFUS)" in s and "2.5 to 50" in s
open(p,'w').write(s)
EOF
. dev/bin/activate && python build/nb2.py >/dev/null; cd entries/001683-gao-2026 && cat > requirements.in <<'EOF'
h5py
matplotlib
numpy
pandas
patsy
remfile
requests
scipy
statsmodels
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 001683-gao-2026
type: reproduction
title: White-matter tFUS against 4-AP seizures in rats (Gao et al. 2026)
description: Tests the findings of Gao, Frake, Durand and He (2026) on dandiset 001683, which holds
  the EEG and seizure labels of 16 rats with 4-AP seizures (10 given focused ultrasound to the
  corpus callosum, 6 sham) and the evoked-potential and EEG recordings of the wild-type phase of 23
  rats. It compares seizure count, percent time in seizure, interval and duration between groups and
  time blocks, band power, the asymmetry index and the phase lag index, and the evoked potentials.
license: Apache-2.0
notebooks:
- path: seizure_metrics.ipynb
  title: Seizure metrics from the labels (Figs. 2 and 3)
  runtime_minutes: 1
- path: eeg_blocks.ipynb
  title: Band power, asymmetry index and seizure PLI (Figs. 4, 6, S4, S5, S7)
  runtime_minutes: 14
- path: wild_type.ipynb
  title: Evoked potentials and PLI in wild-type rats (Fig. 5)
  runtime_minutes: 8
helpers:
- tfus.py
related:
- id: dandi:001683/0.260109.2104
  relation: uses_data
- id: doi:10.1109/tnsre.2025.3644273
  relation: reproduces
EOF
cd  && python tools/entry.py lock entries/001683-gao-2026 2>&1 | tail -3 && python tools/entry.py check entries/001683-gao-2026 2>&1 | tail -10
```

```
wrote entries/001683-gao-2026/requirements.lock.txt
0 error(s)
```

**Agent**

Check passes. Running the entry from a clean environment (about 25 min).

**Agent calls Bash**

```bash
time python tools/entry.py all entries/001683-gao-2026 2>&1 | tail -15
```

```
Installed kernelspec registry-001683-gao-2026 in executed/001683-gao-2026/.venv/share/jupyter/kernels/registry-001683-gao-2026
0 error(s)
pass  seizure_metrics.ipynb  (62 s)
pass  eeg_blocks.ipynb  (817 s)
pass  wild_type.ipynb  (463 s)

real	22m28.505s
user	39m48.547s
sys	13m24.511s
```

**Agent**

All three notebooks pass (1, 14 and 8 min). Checking that the executed outputs carry the numbers the conclusions quote.

**Agent calls Bash**

```bash
cd $TMPDIR && ls executed/001683-gao-2026/; for nb in seizure_metrics eeg_blocks wild_type; do python showout.py executed/001683-gao-2026/$nb.ipynb 20000 > $nb.txt; done; python - <<'EOF'
import re
checks={'seizure_metrics':['F=30.45, p=5.47e-24','2.39e-31','p=0.00145','3.91e-05','99.4% under','99.2% under','D = 0.082, p = 0.056','p=0.972','p=0.823','0.0209','0.0963','0.0832','0.0085','0.0039','0.0054','0.0024','0.0262','0.0458','0.0179','0.0565','0.0618','0.1212','0.1087','0.0056','0.0595','0.0357','0.0385','0.0184','0.0443','0.0203','0.3748','0.2863','0.0434','0.0214','0.0136','0.656','27.4','49.1','30.9','8.7','36.4','41.9'],
'eeg_blocks':['0.0090','0.0004','0.0430','0.0028','0.0262','0.0005','0.0094','0.4930','0.4871','0.5001','0.0037','0.0895','0.0333','0.0047','0.0057','0.0006','-0.0258','-0.0572','-0.4092','-0.4260','0.0012','14 ','8 ','136 of 136','2.55','50.36'],
'wild_type':['66.5','0.01311','0.05132','39','3.10','1.72','-0.0290','-0.3858','0.6918','0.4697','0.0700','0.976','0.969']}
for nb,ks in checks.items():
    t=open(f'/tmp/claude-1001/{nb}.txt').read()
    print(nb,[k for k in ks if k not in t])
EOF
grep -A12 "reading  norm  tFUS" eeg_blocks.txt | head -6; grep -A10 "Per band" wild_type.txt
```

```
eeg_blocks.ipynb
result.json
seizure_metrics.ipynb
wild_type.ipynb
seizure_metrics []
eeg_blocks []
wild_type []
    reading  norm  tFUS S1 cells below baseline (of 12)  tFUS non-S1 cells not below baseline (of 12) S1 sham-tFUS significant
per_seizure  diff                                     8                                             4                     none
per_seizure ratio                                     8                                             4                     none
     concat  diff                                     6                                             4                     none
     concat ratio                                     6                                             4                     none

Per band:
  reading  norm          window bands with S1 below and non-S1 not below
per_trial  diff      a: 0-20 ms                                     none
per_trial  diff b: both windows                                     none
per_trial ratio      a: 0-20 ms                                     none
per_trial ratio b: both windows                                     none
   concat  diff      a: 0-20 ms                                     none
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 340,470p tools/entry.py | grep -n "add_argument\|notebook" | head; grep -n "Files sharing a label table" -A3 $TMPDIR/seizure_metrics.txt
```

```
20:    for notebook in entry["notebooks"]:
21:        name = notebook["path"]
24:            [str(python), "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute",
36:        results.append({"notebook": name, "ok": ok, "seconds": seconds, "error": error})
48:    """The notebook without the author's conclusions, for a verifier's first round."""
65:    for notebook in entry["notebooks"]:
66:        executed = output_dir / notebook["path"]
68:            print(f"error: no executed copy of {notebook['path']} in {output_dir}; run the entry first",
72:        nbformat.write(nb, target / notebook["path"])
89:    parser.add_argument("command", choices=["lock", "check", "run", "all", "handover"])
53:Files sharing a label table: 2
54-Files sharing a sample count (same length is common at this rate; listed for inspection):
55-                                     n_samples subject      block
56-6bea7ecf-4a97-41c5-b02b-807f4a8ee551  11445760   BH649      post3
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='/tmp/claude-1001/build/nb1.py'; s=open(p).read()
old='''print("Files sharing a label table:", int(s.labels_md5.duplicated(keep=False).sum()))'''
new='''dl = s[s.labels_md5.duplicated(keep=False)].join(blocks.set_index("asset_id")[["subject", "block"]])
print("Files sharing a label table:", len(dl), dl[["subject", "block"]].to_dict("records"),
      "; their tables:", [M[a]["intervals"].to_dict("records") for a in dl.index])'''
assert old in s; s=s.replace(old,new)
old2='''No two block files share samples or label tables, so no recording is deposited twice. Files that
share a sample count differ in their samples.'''
new2='''No two block files share samples, so no recording is deposited twice. The two files that share a
label table are the two blocks without seizures, whose tables hold the same single `no_seizure`
row. Files that share a sample count differ in their samples.'''
assert old2 in s; s=s.replace(old2,new2)
open(p,'w').write(s)
EOF
. dev/bin/activate && python build/nb1.py; date -u
```

```
built 53
Tue Nov  3 09:31:09 UTC 2026
Shell cwd was reset to
```

**Agent**

Now the attempt record. Reading the example record and the schema for the format.

**Agent calls Bash**

```bash
sed -n 1,80p attempts/001453-fouke-2025-01.yaml; grep -n "^- claim\|^  - claim\|^findings\|^verifications\|^inputs\|^provenance\|^deviations\|^outcomes" attempts/001453-fouke-2025-01.yaml
```

```
schema_version: 2
id: 001453-fouke-2025-01
dataset:
  archive: dandi
  id: "001453"
  version: 0.250518.1950
  doi: 10.48324/dandi.001453/0.250518.1950
paper: doi:10.1016/j.cub.2025.04.027
date: 2026-10-14
entry: 001453-fouke-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-5
  runner:
    platform: GitHub Actions
[... 125 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 197,310p attempts/001453-fouke-2025-01.yaml; python -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['properties'].get('findings'),indent=0)[:1500]); print(list(s['properties'].keys()))
d=s.get('\$defs',s.get('definitions',{})); print(list(d.keys()))
print(json.dumps(d.get('outcome',{}),indent=0)[:2500])
"
```

```
- claim: fig1cef-representative-values
  outcome: blocked
  blocked_by: metadata_insufficient
  notes: The numbers come from single representative fish and trials. Fig1-S1.ipynb selects them
    by the index of a data folder and a trial number (for example DC folder 29, trial 79), and the
    dandiset gives no mapping from those folders to its subjects, nor the original file names.
- claim: fig2d-shared-architecture
  outcome: blocked
  blocked_by: data_missing
  notes: The two-photon imaging data are not in the dandiset, which holds only freely swimming
    tracking. The GitLab repository the paper names for "all behavioral and imaging data" holds
    notebooks only, and no other dandiset of this lab or paper was found on the archive.
- claim: fig2g-dsi-similar
  outcome: blocked
  blocked_by: data_missing
  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
- claim: fig2h-fewer-motion-responsive
  outcome: blocked
  blocked_by: data_missing
  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']; print(json.dumps(o,indent=0)[:3500]); print(json.dumps(s['properties']['provenance'],indent=0)[:1500])"; ls questions | head
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
[... 221 more lines not kept]
```

**Agent**

Writing the README and the attempt record.

**Agent calls Write**

```json
{
 "file_path": "entries/001683-gao-2026/README.md",
 "content": "# Gao, Frake, Durand & He (2026) from dandiset 001683\n\nTests the findings of [Gao et al. (2026)](https://doi.org/10.1109/tnsre.2025.3644273) on\n[DANDI:001683](https://dandiarchive.org/dandiset/001683/0.260109.2104), which holds the EEG and\nseizure labels of 16 rats with 4-AP seizures (10 given focused ultrasound to the corpus callosum,\n6 sham), and the evoked-potential and EEG recordings of the wild-type phase of 23 rats.\n\n| Claim | Outcome |\n|---|---|\n| Sham seizure duration does not change across blocks (Fig. 2C) | Not reproduced |\n| Most sham seizures last under 2 minutes (Fig. 2D) | Reproduced |\n| Sham seizure count does not change (Fig. 2E) | Reproduced |\n| Sham percent time in seizure differs at post 3 (Fig. 2F) | Reproduced, on assumptions |\n| tFUS reduces seizure count by 9 to 42% (Fig. 3A) | Reproduced |\n| Seizure count differs between sham and tFUS at post 1 and 2 (Fig. 3A) | Reproduced |\n| tFUS reduces percent time in seizure by 33 to 55% (Fig. 3B) | Reproduced |\n| Sham percent time does not change (Fig. 3B) | Not reproduced, on an assumption |\n| Percent time differs between sham and tFUS (Fig. 3B) | Not reproduced |\n| tFUS lengthens the inter-seizure interval by 27 to 52% (Fig. 3C) | Reproduced, on an assumption |\n| Interval differs between sham and tFUS at post 1 (Fig. 3C) | Reproduced |\n| Seizure duration falls significantly only at tFUS post 2 (Fig. 3D) | Not reproduced |\n| No change in theta, alpha, gamma power (Fig. 4) | Not reproduced, on an assumption |\n| Beta power falls during and after tFUS (Fig. 4C) | Partially reproduced |\n| Sham band power does not change (Fig. S4) | Not reproduced, on an assumption |\n| Normalized AI rises with tFUS and differs from sham (Fig. 4E-H) | Partially reproduced |\n| Seizures lower the AI (Fig. S5) | Blocked: data missing |\n| Seizure PLI of S1 falls with tFUS (Fig. 6) | Partially reproduced |\n| Seizure PLI change, S1 against non-S1 (Fig. S7) | Blocked: data missing |\n| tFUS evokes potentials in S1 (Fig. 5B) | Blocked: methods underspecified |\n| Wild-type gamma PLI falls with tFUS (Fig. 5C-F, J) | Blocked: data missing |\n| Wild-type low-band PLI falls only in S1 (Fig. 5G-I) | Not reproduced |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe seizure labels in the dandiset give the paper's percent changes of Fig. 3 to within one point.\nTheir times are in minutes, not seconds. The significance pattern of Fig. 3 appears only under a\nrepeated-measures reading of the paper's \"two-way ANOVA\", which this attempt adopts as an\nassumption. The pre-4-AP EEG and the resting EEG of the wild-type phase are not in the dandiset.\nThe attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/001683-gao-2026-01.yaml`](../../attempts/001683-gao-2026-01.yaml).\n\n- `seizure_metrics.ipynb`: seizure count, percent time, interval and duration from the labels (about\n  a minute).\n- `eeg_blocks.ipynb`: band power, asymmetry index and seizure PLI; streams all 70 EEG blocks\n  (205 GB) once, in about 14 minutes with four processes.\n- `wild_type.ipynb`: the evoked potentials of the target confirmation and the PLI of the wild-type\n  EEG (about 8 minutes).\n- `tfus.py`: loading (parallel range reads of the unchunked NWB arrays), block assignment, seizure\n  metrics, spectra, PLI and the two-way ANOVA readings. Other notebooks on this dandiset can import\n  it.\n"
}
```

```
File created successfully at: entries/001683-gao-2026/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; grep -c "" questions/000005.yaml; head -30 questions/000005.yaml
```

```
Tue Nov  3 09:31:51 UTC 2026
174
dandiset: "000005"
paper: doi:10.1038/nn.4412
questions:
- claim: fs-vm-touch-whisking
  asked: 2026-10-20
  question: At what resolution is dVm/dt of the touch-aligned average Vm taken for the latency rule,
    the recording's own sampling rate (10 or 20 kHz) or the average in 1 ms bins as for the spike
    PSTH? The same question applies to the laser-onset latencies of exc-thalamus-photoinhibition and
    to exc-vm-touch-whisking.
  passage: Touch latency was identified as the latency from touch onset to the time when dVm/dt
    crossed baseline (3x s.d. of the dVm/dt between 0 and 25 ms before touch). All touch-spike PSTHs
    were constructed with a bin size of 1 ms. (Online Methods, Data analysis)
  why: At the full sampling rate two of the five whole-cell FS cells cross the threshold at 0.0 and
    0.3 ms and the mean latency is 1.88 ms (not reproduced); in 1 ms bins the mean over three cells
    is 3.67 to 4.17 ms (within 4.0 +- 0.4). For the thalamic and cortical light the full rate gives
    0.1 ms for both, the 1 ms bins 5.0 and 2.0 ms.
  answer: >-
    The recording's sampling rate, not 1 ms bins. The Methods give 1 ms bins for spike PSTHs
[... 12 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/001683-gao-2026-01.yaml",
 "content": "schema_version: 2\nid: 001683-gao-2026-01\ndataset:\n  archive: dandi\n  id: \"001683\"\n  version: 0.260109.2104\n  doi: 10.48324/dandi.001683/0.260109.2104\npaper: doi:10.1109/tnsre.2025.3644273\ndate: 2026-11-03\nentry: 001683-gao-2026\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-13\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/41601386820\noutcomes:\n- claim: fig2c-sham-duration-stable\n  outcome: not_reproduced\n  notebook: seizure_metrics.ipynb\n  output: claim:fig2c-sham-duration-stable\n  notes: The block effect on sham seizure duration is significant under every reading. Per seizure\n    (1046 seizures) F = 30.45, p = 5.5e-24 ordinary and p = 2.4e-31 repeated, with 12 and 13 of 25\n    Bonferroni post hoc comparisons significant; per rat p = 0.00145 ordinary (no post hoc\n    comparison significant) and p = 3.9e-05 repeated (contralateral baseline against post 3,\n    p = 0.012). The hemisphere effect is not significant (p = 0.16 to 0.63). Mean durations fall\n    from 49.6 to 53.0 s at baseline to 34.8 to 35.7 s at post 3. The readings agree, so the\n    outcome rests on none of them.\n  deviations:\n  - The seizure labels are the dandiset's own; their times are in minutes and are multiplied by\n    60 (checked against the EEG in eeg_blocks.ipynb).\n  - Durations leave out the 6 seizures that start at a block's first sample (Methods C, \"Seizures\n    that either started before or continued after the recording were excluded\").\n  - BH635's five files are taken in time order (see fig2f-sham-percent-time-post3).\n  - The repeated-measures reading of M3 is a linear mixed model with a random intercept per rat\n    and Wald tests of the contrasts, a standard stand-in for Prism's repeated-measures and\n    mixed-effects analysis.\n- claim: fig2d-seizures-under-two-minutes\n  outcome: reproduced\n  notebook: seizure_metrics.ipynb\n  output: claim:fig2d-seizures-under-two-minutes\n  notes: 99.4% of 527 ipsilateral and 99.2% of 521 contralateral sham seizures last under 120 s;\n    medians 41.5 and 43.5 s; every rat 97% or more. KS D = 0.082, p = 0.056 (description only).\n  deviations:\n  - All seizures are counted, including the two that start at a block's first sample.\n- claim: fig2e-sham-count-stable\n  outcome: reproduced\n  notebook: seizure_metrics.ipynb\n  output: claim:fig2e-sham-count-stable\n  notes: Block p = 0.97 (ordinary) and 0.82 (repeated), hemisphere p = 0.93 and 0.88, no post hoc\n    comparison significant (smallest Bonferroni p = 1). Mean count 18.11 over baseline to post 1\n    and 16.50 over post 2 and post 3. With BH635's blocks by their labels the block effect stays\n    non-significant (p = 0.66 and 0.61).\n  deviations:\n  - BH635's five files are taken in time order (see fig2f-sham-percent-time-post3); the label\n    variant gives the same outcome.\n- claim: fig2f-sham-percent-time-post3\n  outcome: reproduced\n  assumed: true\n  notebook: seizure_metrics.ipynb\n  output: claim:fig2f-sham-percent-time-post3\n  notes: Under the repeated-measures reading, contralateral baseline (reading b of \"sham\") against\n    post 3 is significant, Bonferroni p = 0.021 in the block family and 0.026 over all 25\n    comparisons, a decrease from 25.6% to 15.5%. Condition against post 3 is not (p = 0.096).\n    Under the ordinary reading no comparison is significant (p = 1). With BH635's files taken by\n    their labels the comparison is not significant (p = 0.083).\n  deviations:\n  - Assumed that BH635's five files are the blocks baseline, condition, post 1, post 2 and post 3\n    in time order, though their labels read BASELINE, SHAM, SHAM, BH636_post1 and BH635_post2. The\n    files start 63 to 68 min apart like every other rat's blocks (Methods D, ~62.5 min blocks), and\n    every other sham rat has five blocks. The outcome depends on this choice; the label reading is\n    shown as a variant.\n  - The result holds under the repeated-measures reading of M3 only, which the criterion allows\n    (\"under one reading\").\n- claim: fig3a-count-reduction\n  outcome: reproduced\n  notebook: seizure_metrics.ipynb\n  output: claim:fig3a-count-reduction\n  measured:\n  - 8.7\n  - 36.4\n  - 41.9\n  - 10.5\n  - 41.4\n  - 42.4\n  notes: Under reading (b) of M4 all six decreases are within tolerance. Reading (a) gives 24.1,\n    46.2, 49.4, 27.0, 47.2 and 50.3%, outside. Under the repeated-measures reading baseline against\n    post 1 and post 2 are significant in both hemispheres (Bonferroni p = 0.0085 and 0.0039\n    ipsilateral, 0.0054 and 0.0024 contralateral, within family; 0.014, 0.0065, 0.009 and 0.004\n    over all ten). Under the ordinary reading none of the four is (p = 0.057 to 0.115).\n- claim: fig3a-count-sham-vs-tfus\n  outcome: reproduced\n  notebook: seizure_metrics.ipynb\n  output: claim:fig3a-count-sham-vs-tfus\n  notes: Under the repeated-measures reading with the between family, sham against tFUS is\n    significant at post 1 and post 2 in the ipsilateral S1 (p = 0.026 and 0.046), reading (b) of\n    the hemisphere; contralateral post 1 p = 0.018, post 2 p = 0.057. Ordinary reading, post 1\n    significant in both hemispheres (0.035, 0.025), post 2 in neither (0.057, 0.069). No sham block\n    differs from sham baseline (p = 1). With BH635 by its labels post 1 and post 2 are significant\n    in both hemispheres (0.029 to 0.044).\n- claim: fig3b-percent-time-reduction\n  outcome: reproduced\n  notebook: seizure_metrics.ipynb\n  output: claim:fig3b-percent-time-reduction\n  measured:\n  - 32.5\n  - 34.8\n  - 55.5\n  - 54.9\n  notes: Reading (b) of M4 gives 32.5 and 34.8% at stimulation, 55.5 and 55.3% at post 1, 54.9 and\n    55.2% at post 2 (ipsilateral and contralateral; the measured values for the \"each hemisphere\"\n    expectations are the ipsilateral ones), all within tolerance; reading (a) gives 35.8 to 57.3%,\n    also within. Under the repeated-measures reading all six comparisons with baseline are\n    significant (Bonferroni p from 0.0007 to below 0.0001); under the ordinary reading post 1 and\n    post 2 are (0.008 to 0.012) and stimulation is not (0.22, 0.17).\n- claim: fig3b-sham-percent-time-no-change\n  outcome: not_reproduced\n  assumed: true\n  notebook: seizure_metrics.ipynb\n  output: claim:fig3b-sham-percent-time-no-change\n  notes: The ANOVA readings disagree. Ordinary, no sham block differs from baseline (smallest\n    Bonferroni p = 0.79). Repeated, post 2 differs in both hemispheres (p = 0.043 ipsilateral,\n    0.021 contralateral; 0.072 and 0.036 over all ten comparisons). Sham percent time falls from\n    24.0 to 16.4% (ipsilateral) and from 25.6 to 17.6% (contralateral). With BH635 by its labels\n    contralateral post 2 stays significant (p = 0.014).\n  deviations:\n  - Assumed that the paper's two-way ANOVA is the repeated-measures reading of M3, since the\n    readings disagree on this claim of absence. Methods F says only \"two-way ANOVA ... in GraphPad\n    Prism\"; the blocks are repeated on the same rats, and the paper's significant within-group\n    changes of Fig. 3 (count and percent time against baseline, interval at contralateral post 1,\n    Results B) are found only under the repeated-measures reading. Under the ordinary reading the\n    claim would be reproduced.\n- claim: fig3b-percent-time-sham-vs-tfus\n  outcome: not_reproduced\n  notebook: seizure_metrics.ipynb\n  output: claim:fig3b-percent-time-sham-vs-tfus\n  notes: tFUS is lower than sham in all three named comparisons (by 11.4, 9.8 and 10.0 percentage\n    points), but none is significant. Contralateral post 1 p = 0.062 (repeated) and 0.075\n    (ordinary), ipsilateral stimulation 0.12 and 0.14, ipsilateral post 1 0.11 and 0.13, between\n    family; larger over all ten comparisons.\n- claim: fig3c-interval-increase\n  outcome: reproduced\n  assumed: true\n  notebook: seizure_metrics.ipynb\n  output: claim:fig3c-interval-increase\n  measured:\n  - 27.4\n  - 49.1\n  - 27.8\n  - 30.1\n  - 51.9\n  - 30.9\n  notes: Gap reading of the interval and reading (b) of M4, all six increases within tolerance.\n    The two rats left out are BH634 and BH638 (no seizures at post 2). Under the repeated-measures\n    reading with all ten comparisons in one family, contralateral post 1 is the only significant\n    comparison with baseline (p = 0.0056; ipsilateral post 1 p = 0.060, the others 0.65 or more).\n    With the within family ipsilateral post 1 is significant too (p = 0.036). The ordinary reading\n    finds none (contralateral post 1 p = 0.18). Onset-to-onset intervals give increases of 12.6 to\n    30.6%, outside tolerance.\n  deviations:\n  - Assumed that the Inter-Seizure Interval is the gap from one seizure's end to the next one's\n    start. Methods C defines it as \"time between neighboring seizures\" and the claims file (M2)\n    does not fix it; the onset-to-onset reading is shown. The gap reading gives the paper's six\n    percentages to within 0.4 point.\n- claim: fig3c-interval-sham-vs-tfus\n  outcome: reproduced\n  notebook: seizure_metrics.ipynb\n  output: claim:fig3c-interval-sham-vs-tfus\n  notes: Repeated-measures reading, between family, sham against tFUS at post 1 is significant in\n    both hemispheres with tFUS higher (122 s ipsilateral, p = 0.039; 140 s contralateral,\n    p = 0.018); the onset-to-onset interval gives the same (0.044, 0.020). Ordinary, ipsilateral\n    p = 0.051. No sham block differs from sham baseline (p = 1). No single Bonferroni family gives\n    both this claim and fig3c-interval-increase; with all ten comparisons in one family the\n    ipsilateral comparison here is p = 0.096.\n- claim: fig3d-duration-decline\n  outcome: not_reproduced\n  notebook: seizure_metrics.ipynb\n  output: claim:fig3d-duration-decline\n  notes: Means decline in both groups (tFUS 59.8 to 48.7 s ipsilateral, 61.0 to 49.9 s\n    contralateral; sham 53.0 to 37.8 and 56.8 to 40.6 s), but tFUS baseline against post 2 is not\n    significant (Bonferroni p = 0.37 and 0.29 repeated, 0.62 and 0.59 ordinary), nor is any other\n    within-group comparison (smallest p = 0.13).\n  deviations:\n  - Per-rat mean durations, leaving out the 6 seizures that start at a block's first sample; the\n    two tFUS rats without seizures at post 2 have no duration there (N = 8 at post 2).\n- claim: fig4-no-theta-alpha-gamma-power-change\n  outcome: not_reproduced\n  assumed: true\n  notebook: eeg_blocks.ipynb\n  output: claim:fig4-no-theta-alpha-gamma-power-change\n  notes: The M5 readings agree within each ANOVA reading; the ANOVA readings disagree. Ordinary, no\n    within-group comparison against baseline is significant for theta, alpha or gamma. Repeated,\n    the sham theta ratio rises above baseline in 4 or 5 of 12 comparisons under every M5 reading\n    (ipsilateral post 2 p = 0.009 over the whole block, ratio 0.098 to 0.136; p = 0.0004 over the\n    seizure periods), and the tFUS gamma ratio differs at ipsilateral post 2 with the 0 Hz to\n    Nyquist total (p = 0.043). No between-group comparison is significant.\n  deviations:\n  - Assumed the repeated-measures reading of M3 is the paper's test, as for\n    fig3b-sham-percent-time-no-change; under the ordinary reading the claim would be reproduced.\n  - No ICA; which components the authors removed (Methods C) is not recorded. Common average\n    reference and 60 Hz notch as in Methods C.\n  - The channels are 8 (ipsilateral) and 25 (contralateral), the electrodes encircled in the\n    drawing of Fig. S1, which prints the channel numbers; Methods E uses \"the EEG electrode\n    closest to the burr hole\".\n  - Seizure segment per hemisphere is the union of that hemisphere's labels; Welch PSD with 2 s\n    Hann windows (the claims file's standard choice), periods shorter than a window skipped.\n- claim: fig4c-beta-decrease\n  outcome: partially_reproduced\n  notebook: eeg_blocks.ipynb\n  output: claim:fig4c-beta-decrease\n  notes: Whole block, repeated-measures reading, the tFUS beta ratio at post 1 is significantly\n    below baseline in both hemispheres (3-300 Hz total p = 0.0028 ipsilateral and 0.026\n    contralateral; 0 Hz to Nyquist 0.0005 and 0.0094), but the condition block is not (p = 0.16 to\n    0.60) although its mean is lower (ipsilateral 0.445 to 0.417). Over the seizure periods the\n    beta ratio does not fall (ipsilateral 0.493, 0.487, 0.500) and nothing is significant. Under\n    the ordinary reading nothing is significant.\n  deviations:\n  - As for fig4-no-theta-alpha-gamma-power-change (no ICA, channels 8 and 25 from Fig. S1).\n- claim: figs4-sham-power-no-change\n  outcome: not_reproduced\n  assumed: true\n  notebook: eeg_blocks.ipynb\n  output: claim:figs4-sham-power-no-change\n  notes: Over the whole block beta has significant block and hemisphere effects under both readings\n    (ordinary block p = 0.0004 and 0.0002 for the two totals, hemisphere p below 0.0001, 4 and 5\n    post hoc comparisons significant) and gamma a hemisphere effect (0.0037 and 0.0004). Over the\n    seizure periods the repeated-measures reading finds a beta block effect (0.0009, 0.0007, 2 post\n    hoc comparisons); the ordinary reading finds nothing in any band (smallest p = 0.09).\n  deviations:\n  - Under the ordinary reading the M5 readings disagree (whole block not reproduced, seizure\n    periods reproduced), which the criterion would block as methods_underspecified; under the\n    repeated-measures reading, assumed to be the paper's test as for\n    fig3b-sham-percent-time-no-change, they agree.\n  - As for fig4-no-theta-alpha-gamma-power-change (no ICA, channels 8 and 25 from Fig. S1).\n- claim: fig4ef-ai-increase\n  outcome: partially_reproduced\n  notebook: eeg_blocks.ipynb\n  output: claim:fig4ef-ai-increase\n  notes: Mean baseline AI is negative in both groups (whole block, sham -0.58 to -0.61, tFUS -0.24\n    to -0.29). With subtraction (reading b), the whole block and the repeated-measures reading, the\n    tFUS normalized AI rises above baseline, toward balance, in theta (post 1 p = 0.033, post 2\n    p = 0.0047) and alpha (post 2 p = 0.0057). Sham against tFUS is not significant in any band,\n    block or combination of readings. With division the same change is a significant fall (theta\n    post 2 p = 0.0006); over the seizure periods nothing is significant.\n  deviations:\n  - AI is computed on the band power (sum of PSD in the band) of channels 8 and 25, Eq. 1; the\n    seizure segment is the union of both hemispheres' labels.\n  - As for fig4-no-theta-alpha-gamma-power-change (no ICA).\n- claim: figs5-seizures-lower-ai\n  outcome: blocked\n  blocked_by: data_missing\n  notebook: eeg_blocks.ipynb\n  output: claim:figs5-seizures-lower-ai\n  notes: The pre-4-AP baseline state is not in the dandiset. The resting recordings of the target\n    confirmation (EP data, BASELINE) hold only the 64 intracranial channels of left S1, and no EEG\n    before the first injection was deposited (the labelled blocks start at the baseline block;\n    the monitoring block is not there). The part against 0 holds. Seizure AI of the baseline block\n    is -0.41 to -0.43 over the 16 rats (p < 0.0001 in each band) and -0.27 to -0.30 over the 10\n    tFUS rats (p = 0.0001 to 0.0012), one-sample t-tests.\n- claim: fig6-epileptic-pli-s1-decrease\n  outcome: partially_reproduced\n  notebook: eeg_blocks.ipynb\n  output: claim:fig6-epileptic-pli-s1-decrease\n  notes: Per seizure and averaged, the tFUS S1 PLI is below the group's baseline in 8 of 12 band and\n    block cells (theta and alpha at all three blocks, alpha -0.026, -0.032, -0.057; beta only at the\n    condition block; gamma only at post 1); over concatenated samples 6 of 12. The non-S1 PLI also\n    falls (not below baseline in only 4 of 12 cells), so that part fails. No sham against tFUS\n    comparison of S1 PLI is significant under either ANOVA reading. The criterion's partial outcome\n    (S1 decreases in some bands only, without a significant group difference) applies; the S1\n    specificity is not seen, and the sham S1 PLI falls as much in theta (-0.022 to -0.080).\n  deviations:\n  - S1 channels are 7, 8, 10, 12 and 21, 23, 25, 26, taken from the notes of the dandiset's PLV\n    files; the paper draws them only in Fig. 5A, which the text read does not list.\n  - Seizure periods are the union of both hemispheres' labels, 1 s or longer; the EEG is decimated\n    by 3 to 1017 Hz before the band filters, a standard choice; band filters run on each seizure\n    with 2 s of margin. No ICA.\n- claim: figs7-seizure-pli-s1-vs-non-s1\n  outcome: blocked\n  blocked_by: data_missing\n  notebook: eeg_blocks.ipynb\n  output: claim:figs7-seizure-pli-s1-vs-non-s1\n  notes: The change is from the pre-4-AP baseline state, whose EEG is not in the dandiset (see\n    figs5-seizures-lower-ai).\n- claim: fig5b-tfus-evoked-potentials\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: wild_type.ipynb\n  output: claim:fig5b-tfus-evoked-potentials\n  notes: The readings disagree. With the mean over the 64 channels, 1 of 12 combinations of\n    position (CENTER, largest EP), sham onsets (every 2 s, random, the file's own intervals) and\n    ANOVA (ordinary, repeated) finds significant time points (CENTER, random onsets, ordinary, 13 of\n    610 points from 66.5 ms, smallest Bonferroni p = 0.013); the other 11 find none (smallest p =\n    0.05 to 1). With each channel, 0 to 39 of 64 channels have a significant point depending on the\n    combination. The CENTER channel-mean EP reaches 3.1 uV, the sham 1.7 uV. The criterion blocks\n    the claim when the readings disagree. Question for the authors (findings) which channels,\n    which position and which sham onsets were used.\n- claim: fig5cdj-wild-type-gamma-pli-decrease\n  outcome: blocked\n  blocked_by: data_missing\n  notebook: wild_type.ipynb\n  output: claim:fig5cdj-wild-type-gamma-pli-decrease\n  notes: The sham, the EEG of the resting baseline recording of the target confirmation, is not in\n    the dandiset; its resting recordings hold only the intracranial LFP. The tFUS part, from the\n    PLV EEG files of 20 rats, shows gamma PLI falling in the 20 to 200 ms window in both regions\n    under every reading (S1 -0.029 and non-S1 -0.016 over concatenated samples, -0.386 and -0.386\n    per trial; 62% or 100% of pairs decreasing), and in the 0 to 20 ms window under the per-trial\n    reading only (S1 -0.013, non-S1 -0.024, 69% of pairs; concatenated +0.002 and +0.005, 47%).\n- claim: fig5ghi-low-band-pli-s1-only\n  outcome: not_reproduced\n  notebook: wild_type.ipynb\n  output: claim:fig5ghi-low-band-pli-s1-only\n  notes: In no band and under no combination of readings does the S1 PLI fall while the non-S1 PLI\n    does not. In the 0 to 20 ms window S1 PLI does not fall in theta, alpha or beta under any\n    reading (differences +0.0002 to +0.070); in the 20 to 200 ms window both regions fall together\n    (alpha -0.017 S1, -0.021 non-S1, concatenated). The per-trial PLI of the 20 ms pre window is\n    near 1 in theta and alpha (0.98, 0.97), so per-trial changes to the longer window reflect the\n    window lengths.\n  deviations:\n  - The epochs are the first 200 pulses of the dandiset's PLV EEG files (20 ms pulses, labelled\n    EEG data for PLV analysis), for 20 of the 23 rats; the claims file reads them as the 200\n    bursts of the target confirmation, whose EEG is not in the dandiset. The Methods' \"tFUS (20 ms\n    of stimulation\" fits these files.\n  - S1 channels from the PLV files' notes (see fig6-epileptic-pli-s1-decrease). The ratio reading\n    divides the region's mean PLI by its mean pre PLI, a standard choice.\nfindings:\n- kind: metadata_error\n  statement: The seizure label table (intervals/custom_intervals_table_name) of all 70 labelled\n    EEG blocks gives start and stop times in minutes, while NWB prescribes seconds; the stops reach\n    62.7 in blocks of 3750 s. Read as minutes the labels match the EEG (30 to 80 Hz power 2.5 to 50\n    times higher inside them in all 136 block-hemispheres); read as seconds they do not. The EP and\n    PLV files' interval tables are in seconds.\n- kind: metadata_error\n  statement: The five block files of sham rat BH635 are labelled BASELINE, SHAM, SHAM, BH636_post1\n    (another rat's number) and BH635_post2, with no post3, while every other sham rat has\n    BASELINE, SHAM, post1, post2, post3. The files follow each other at 63 to 68 min like the other\n    rats' blocks. BH649's post 3 file has the session id None in its path.\n- kind: metadata_error\n  statement: Every file gives the subject as \"HSD:WI rat\" (Envigo's Wistar code) of age P24W, while\n    the paper used Sprague-Dawley rats (Envigo) of 3 to 6 months.\n- kind: metadata_error\n  statement: The ElectricalSeries of the EP files is described as \"EEG data\" though the files hold\n    the 64 intracranial channels of left S1 (location Left S1, notes \"LFP signal for EP test\"). The\n    PLV files are labelled 1Hz but 19 of 20 carry their pulses every 2 s.\n- kind: metadata_insufficient\n  statement: The files do not say which EEG channels were used to label the seizures (channels 8\n    and 25, read from the drawing of Fig. S1) or which channels cover S1 (given only in the notes of\n    the PLV files, not in the electrode tables of the labelled blocks).\n- kind: metadata_insufficient\n  statement: The target-confirmation recordings do not say which transducer position was chosen\n    for the experiment (\"the coordinates with the clearest EP\", supplement), so the tFUS EPs of\n    Fig. 5B cannot be selected.\n- kind: data_missing\n  statement: The EEG of the pre-4-AP baseline state (Figs. S5 and S7) and of the resting baseline\n    of the target confirmation (the sham of Figs. 5E-F) are not in the dandiset; the resting\n    recordings hold only the intracranial LFP, and the first monitoring block after the first\n    injection was not deposited. PLV EEG files exist for 20 of the 23 wild-type rats (not BH638,\n    BH642, BH644), while Fig. 5 gives N = 23.\n- kind: methods_unavailable\n  statement: Question for the authors. Was the two-way ANOVA of Figs. 2 to 4 and 6 ordinary or\n    repeated measures (or Prism's mixed-effects model), and which comparisons formed each\n    Bonferroni family? The paper's within-group significance in Fig. 3 appears here only under a\n    repeated-measures reading, and no single family reading gives every significance the Results\n    state; this attempt assumed repeated measures for the claims of absence.\n- kind: methods_unavailable\n  statement: Question for the authors. For Fig. 5B, which LFP channel or channels, which\n    target-confirmation recording, which sham onsets in the resting recording and what time\n    resolution were tested? Under the readings tried here the result ranges from no significant\n    time point to 13 of 610 points from 66.5 ms.\n- kind: methods_unavailable\n  statement: Question for the authors. Over which segment were band power, AI and seizure PLI\n    computed (whole block or seizure periods, and for two hemispheres whose labels differ, which\n    periods), what total was the band power divided by, and was AI normalized to the group's\n    baseline by division or by subtraction? With a negative baseline AI the two normalizations give\n    opposite directions.\n- kind: paper_inconsistency\n  statement: Methods E gives the wild-type tFUS window as \"20 ms of stimulation\" of \"200 EPs from the\n    target confirmation procedure\", but the target-confirmation bursts last 67 ms (supplement). The\n    dandiset resolves it with separate EEG recordings of 20 ms pulses made in the wild-type phase,\n    labelled EEG data for PLV analysis, which the paper does not describe.\n- kind: other\n  statement: The baseline AI of the labelling channels is strongly negative in both groups (whole\n    block, sham -0.58 to -0.61, tFUS -0.24 to -0.29), so the contralateral band power is 1.7 to 4\n    times the ipsilateral; the paper reports only AI normalized to the baseline.\n"
}
```

```
File created successfully at: attempts/001683-gao-2026-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml,re
d=yaml.safe_load(open('attempts/001683-gao-2026-01.yaml'))
def walk(x,path=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,path+'/'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,path+f'[{i}]')
    elif isinstance(x,str):
        if ': ' in x: print('colon',path,x[:80])
        if '—' in x or ' rather' in x.lower(): print('style',path)
walk(d); print(len(d['outcomes']))
EOF
grep -n "—\|rather\|\*\*" entries/001683-gao-2026/README.md entries/001683-gao-2026/tfus.py | head; python tools/entry.py check entries/001683-gao-2026 2>&1 | tail -5
```

```
22
entries/001683-gao-2026/tfus.py:148:def read_rows(meta: dict, start: int, stop: int, threads: int = 16, piece: int = 32 * 2**20) -> np.ndarray:
entries/001683-gao-2026/tfus.py:378:    g = signal.sosfiltfilt(sos, car2, axis=0) ** 2
entries/001683-gao-2026/tfus.py:499:    mse = (resid ** 2).sum() / df_res
error: attempts/001683-gao-2026-01.yaml: no cell tagged 'claim:figs7-seizure-pli-s1-vs-non-s1' in eeg_blocks.ipynb
1 error(s)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/001683-gao-2026-01.yaml'; s=open(p).read()
s=s.replace("""  notebook: eeg_blocks.ipynb
  output: claim:figs7-seizure-pli-s1-vs-non-s1
""","""  notebook: eeg_blocks.ipynb
""")
open(p,'w').write(s)
EOF
grep -n "—\| rather\|\*\*[^R]" $TMPDIR/build/nb*.py | grep -v "\*\*Paper\|\*\*Dandiset\|\*\*How\|\*\*What\|\*\*Clock\|\*\*Result\| \*\* " | head; python tools/entry.py check entries/001683-gao-2026 2>&1 | tail -3
```

```
/tmp/claude-1001/build/nb1.py:179:                         **tfus.block_metrics(M[r.asset_id], h)})
/tmp/claude-1001/build/nb2.py:162:                    bp.append({**base, "hemi": h, "segment": seg, "total": tot, "band": band, "ratio": pw[band] / pw[tot]})
/tmp/claude-1001/build/nb2.py:169:            ai.append({**base, "segment": seg, "band": band, "ai": (ip - co) / (ip + co),
/tmp/claude-1001/build/nb2.py:348:    return pd.Series({**{f"tFUS up {k}": v for k, v in up.items()}, **{f"between {k}": v for k, v in between.items()}})
0 error(s)
```

**Agent**

Removing bold labels other than the Result openers from the notebooks.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import re
for n in ['nb1','nb2','nb3']:
    p=f'/tmp/claude-1001/build/{n}.py'; s=open(p).read()
    s=re.sub(r'\*\*((?!Result)[A-Z][^*\n]{2,80}?\.)\*\*', r'\1', s)
    open(p,'w').write(s)
    print(n, re.findall(r'\*\*[A-Z][^*\n]{0,30}', s)[:20])
EOF
. dev/bin/activate && for n in nb1 nb2 nb3; do python build/$n.py; done; date -u
```

```
nb1 ['**Result: not reproduced.', '**Result: reproduced.', '**Result: reproduced.', '**Result: reproduced, resting on ', '**Result: reproduced.', '**Result: reproduced.', '**Result: reproduced.', '**Result: not reproduced, resting', '**Result: not reproduced.', '**Result: reproduced, resting on ', '**Result: reproduced.', '**Result: not reproduced.']
nb2 ['**Result: not reproduced, resting', '**Result: partially reproduced.', '**Result: not reproduced, resting', '**Result: partially reproduced.', '**Result: blocked (data_missing).', '**Result: partially reproduced.', '**Result: blocked (data_missing).']
nb3 ['**Result: blocked (methods_unders', '**Result: blocked (data_missing).', '**Result: not reproduced.']
built 53
built 33
built 21
Tue Nov  3 09:33:29 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/001683-gao-2026 && grep -il "rather\|—" *.ipynb *.py *.md ../../attempts/001683-gao-2026-01.yaml; grep -c '\*\*' *.ipynb; cd ../.. && time python tools/entry.py all entries/001683-gao-2026 2>&1 | tail -5
```

```
eeg_blocks.ipynb:10
seizure_metrics.ipynb:13
wild_type.ipynb:3
Installed kernelspec registry-001683-gao-2026 in executed/001683-gao-2026/.venv/share/jupyter/kernels/registry-001683-gao-2026
0 error(s)
pass  seizure_metrics.ipynb  (60 s)
pass  eeg_blocks.ipynb  (813 s)
pass  wild_type.ipynb  (460 s)

real	22m21.781s
user	40m19.188s
sys	13m21.028s
```

**Agent**

Both runs pass. Re-checking the quoted numbers against the new executed copies, then building the handover.

**Agent calls Bash**

```bash
cd $TMPDIR && for nb in seizure_metrics eeg_blocks wild_type; do python showout.py executed/001683-gao-2026/$nb.ipynb 20000 > $nb.txt; done; python - <<'EOF'
checks={'seizure_metrics':['F=30.45, p=5.47e-24','2.39e-31','p=0.00145','3.91e-05','99.4% under','99.2% under','D = 0.082, p = 0.056','p=0.972','p=0.823','0.0209','0.0963','0.0832','0.0085','0.0039','0.0054','0.0024','0.0262','0.0458','0.0179','0.0565','0.0618','0.1212','0.1087','0.0056','0.0595','0.0357','0.0385','0.0184','0.0443','0.0203','0.3748','0.2863','0.0434','0.0214','0.0136','0.656','27.4','49.1','30.9','8.7','36.4','41.9','0.0289','0.044'],
'eeg_blocks':['0.0090','0.0004','0.0430','0.0028','0.0262','0.0005','0.0094','0.4930','0.4871','0.5001','0.0037','0.0895','0.0333','0.0047','0.0057','0.0006','-0.0258','-0.0572','-0.4092','-0.4260','0.0012','136 of 136','2.55','50.36'],
'wild_type':['66.5','0.01311','0.05132','39','3.10','1.72','-0.0290','-0.3858','0.6918','0.4697','0.0700','0.976','0.969']}
for nb,ks in checks.items():
    t=open(f'/tmp/claude-1001/{nb}.txt').read()
    print(nb,[k for k in ks if k not in t])
EOF
grep "sharing a label table" seizure_metrics.txt | cut -c1-200; cd  && python tools/entry.py handover entries/001683-gao-2026 2>&1 | tail -3; ls executed/001683-gao-2026/handover; git status --short
```

```
seizure_metrics []
eeg_blocks []
wild_type []
Files sharing a label table: 2 [{'subject': 'BH634', 'block': 'post2'}, {'subject': 'BH638', 'block': 'post2'}] ; their tables: [[{'start': 0.0, 'stop': 0.0, 'tag': 'no_seizure'}], [{'start': 0.0, 'st
wrote executed/001683-gao-2026/handover
10.1109-tnsre.2025.3644273.yaml
eeg_blocks.ipynb
seizure_metrics.ipynb
tfus.py
wild_type.ipynb
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
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la .bashrc .gitconfig .idea .mcp.json scripts .vscode 2>&1 | head -20; ls entries/001683-gao-2026/
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  3 08:10 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  3 08:10 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  3 08:10 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  3 08:10 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  3 08:10 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  3 08:10 scripts
README.md
__pycache__
eeg_blocks.ipynb
entry.yaml
requirements.in
requirements.lock.txt
seizure_metrics.ipynb
tfus.py
wild_type.ipynb
```

**Agent**

Those root-level entries are sandbox device mounts present before the run; I leave them. Removing the entry's `__pycache__` and running the final check.

**Agent calls Bash**

```bash
rm -rf entries/001683-gao-2026/__pycache__ && python tools/entry.py check entries/001683-gao-2026 2>&1 | tail -2; date -u
```

```
0 error(s)
Tue Nov  3 09:56:19 UTC 2026
```

**Agent**

I've done Author steps 1 to 6 on DANDI:001683, version 0.260109.2104. That is the only published version and the paper cites none, so I pinned it. The entry is `entries/001683-gao-2026/`: three notebooks and a helper, `tfus.py`. The record is `attempts/001683-gao-2026-01.yaml`. `entry.py check` reports 0 errors, `entry.py all` passes, and the handover is in `executed/001683-gao-2026/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig2c-sham-duration-stable | not reproduced |
| fig2d-seizures-under-two-minutes | reproduced |
| fig2e-sham-count-stable | reproduced |
| fig2f-sham-percent-time-post3 | reproduced (assumed) |
| fig3a-count-reduction | reproduced |
| fig3a-count-sham-vs-tfus | reproduced |
| fig3b-percent-time-reduction | reproduced |
| fig3b-sham-percent-time-no-change | not reproduced (assumed) |
| fig3b-percent-time-sham-vs-tfus | not reproduced |
| fig3c-interval-increase | reproduced (assumed) |
| fig3c-interval-sham-vs-tfus | reproduced |
| fig3d-duration-decline | not reproduced |
| fig4-no-theta-alpha-gamma-power-change | not reproduced (assumed) |
| fig4c-beta-decrease | partially reproduced |
| figs4-sham-power-no-change | not reproduced (assumed) |
| fig4ef-ai-increase | partially reproduced |
| fig6-epileptic-pli-s1-decrease | partially reproduced (the S1-specific decrease is not seen; the criterion's partial clause still applies) |
| figs5-seizures-lower-ai | blocked: data missing (the comparison with 0 does hold) |
| figs7-seizure-pli-s1-vs-non-s1 | blocked: data missing |
| fig5b-tfus-evoked-potentials | blocked: methods underspecified (the criterion's own readings disagree) |
| fig5cdj-wild-type-gamma-pli-decrease | blocked: data missing (no sham EEG) |
| fig5ghi-low-band-pli-s1-only | not reproduced |

## 2. Dataset, assumptions, questions

**What the dataset holds:**
- All 16 epileptic rats: 10 tFUS with 4 blocks each, 6 sham with 5 blocks each, with the paper's seizure labels.
- The labels reproduce the percent changes of Fig. 3 to within 0.5 point. This needs each rat's change from its own baseline, and the interval read as the gap between one seizure's end and the next one's start.
- The target-confirmation LFP recordings of all 23 rats.
- EEG recordings of 20 ms pulses, labelled for PLV analysis, for 20 of the 23 rats.

**Problems with the dataset:**
- The seizure label times are in minutes, not seconds. The EEG confirms it: 30 to 80 Hz power is higher inside the labels in all 136 block-hemispheres, and the contrast disappears when the labels are shifted.
- BH635's block files are mislabelled: two SHAM files, one file named for rat BH636, and no post3.
- BH649's post 3 file has the session id `None`.
- Every file says the rats are Wistar (HSD:WI), aged 24 weeks; the paper says Sprague-Dawley, 3 to 6 months.
- The EP files are described as EEG but hold the intracranial LFP.
- Most of the files labelled "1Hz" have pulses every 2 s.
- Missing: the EEG before 4-AP, the resting EEG of the wild-type phase, and three rats' PLV files.
- The files don't record the labelling channels, the S1 channels or the chosen transducer position.

**Assumptions**, each recorded as a deviation:
- **Repeated-measures ANOVA:** I took this as the paper's "two-way ANOVA" wherever the two readings disagree on a claim of absence. It is the only reading that gives the paper's significant within-group changes in Fig. 3.
- **BH635's blocks:** taken in time order.
- **Inter-seizure interval:** the gap from one seizure's end to the next one's start.
- **Channels:** 8 and 25 for labelling, from the Fig. S1 drawing; the S1 channels from the PLV files' notes.
- **No ICA**, because which components were removed is not recorded.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which ANOVA type and which Bonferroni families were used?
- For Fig. 5B: which channels, which transducer position, which sham onsets?
- Which segments were analysed for band power, AI and PLI, and how was AI normalised?

**Reader questions:** none.

## 3. Where the protocol was unclear

1. **Correct but too generous criteria.** fig6's partial clause makes it "partially reproduced" even though the non-S1 condition fails. I applied the criterion literally and flagged this in the notes.
2. **Blocked claims with a testable part.** Neither the protocol nor the criteria say what to do. For figs5 and fig5cdj I blocked the claim (`data_missing`) and put the testable part's numbers in the notes.
3. **ANOVA readings that disagree on a claim of absence.** The absence rule says to use "the paper's test", but the claims file leaves that test open (M3). I adopted one reading by step 1.6 and used it consistently.
4. **No single Bonferroni family for all claims.** The criteria let each claim pass "under one reading", so different claims of the same figure pass under different families (fig3c). I recorded this in the notes.
5. **"Data the paper describes" versus extra data.** The PLV files fit the Methods better than the claims file's reading of them. I used them and recorded a deviation, without asking a reader.
6. **No per-notebook run.** `entry.py` cannot run a single notebook, so a one-line fix to a data-check cell cost a full 22-minute rerun.

## 4. Runtime and failures

- Notebook runtimes: `seizure_metrics` 1 min, `eeg_blocks` 13.5 min (streams 205 GB), `wild_type` 7.7 min.
- Each full `entry.py all` run took about 22 min; I ran it twice.
- The work ran from 08:14 to 09:56 UTC.
- Nothing failed.

## End of run

86 turns, 102 minutes, $8.91 at API prices, result: success.
