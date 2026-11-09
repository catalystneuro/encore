# 001260 · author · run 41306856088

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls claims/001260 paper entries | head -50
```

```
<persisted-output>
Output too large (36.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/2a1918e7-9167-4006-bb17-a781d9ea2a7c/tool-results/bfpuq7shl.txt

Preview (first 2KB):
Sun Nov  1 12:35:33 UTC 2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/2a1918e7-9167-4006-bb17-a781d9ea2a7c/tool-results/bfpuq7shl.txt"
}
```

```
1	Sun Nov  1 12:35:33 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-13`. Record this version in the attempt's provenance.
5	
6	This is what agents, or people, do to attempt a target and deposit the
7	result. A target is a dataset in a public archive and a paper it names. How
8	each archive's datasets are named, versioned and read is in
9	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
10	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
11	
12	An attempt has three roles, each a separate run with a separate context:
13	
14	- The **reader** reads the paper and writes the claims file: every finding,
15	  and how each is to be tested, taken from the paper. A second reader checks
16	  it against the paper. Readers never see the dataset's data.
17	- The **author** tests the claims on the dataset. It reads the paper to
18	  understand the claims, but the claims file binds it: it cannot change a
19	  claim's statement, expected values or criterion. A method detail the file
20	  lacks it takes from the paper, citing the passage, and it asks a reader
[... 669 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001260/*.yaml; ls paper; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/2a1918e7-9167-4006-bb17-a781d9ea2a7c/tool-results/b4g2egtiu.txt"
}
```

```
1	# Claims for Le Merre, Heining et al. (2026), "A prefrontal cortex map based on single-neuron
2	# activity", Nature Neuroscience, doi:10.1038/s41593-025-02190-z, on dandiset 001260.
3	#
4	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
5	# protocol pilot-10 as stated in docs/protocol.md.
6	#
7	# Text read. The version of record (publisher HTML, open access, stored as
8	# paper/10.1038-s41593-025-02190-z.txt) in full: main text, figure legends, Methods, Data and
9	# Code availability, and the legends of Extended Data Figs. 1 to 9. No PDF was stored, so the
10	# figures themselves (values shown only in panels, such as correlation coefficients of Fig. 3
11	# and Fig. 4g) were not seen. Missing from the text read is the Supplementary Information file
12	# (Supplementary Methods, which describe the behavioral settings, Supplementary Figs. 1 and 2,
13	# and Supplementary Tables 1 to 7, which give the E-score p-values and the within-PFC
14	# hierarchy correlations of Supplementary Table 5), and the Source Data files. The main
15	# findings rest on the main and Extended Data figures, whose legends are in the text; the
16	# claims that cite a supplementary table say so. The bioRxiv preprint (10.1101/2024.11.06.622308
17	# v1, also under paper/) was read only to compare; it reports earlier unit counts (23,386 in the
18	# Results, 23,667 in the figure legends) and no IBL task analysis, and no claim is taken from it.
19	#
20	# Code read. https://github.com/hejDMC/pfcmap at commit 9ae52eddc47fbb590ef4e1b1949507334707a0f1
[... 712 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/2a1918e7-9167-4006-bb17-a781d9ea2a7c/tool-results/b4g2egtiu.txt",
 "offset": 733
}
```

```
733	    hierarchy score (R = 0.48, P = 0.002), while correlations are weak for visual tuning and absent
734	    for feedback tuning.
735	  source: Figure 5h; Extended Data Fig. 9d,f,g; Results, Mapping task variables during goal-directed
736	    behavior, paragraph 4
737	  quote: Enrichment in choice-tuned units correlated strongly with intra-PFC hierarchy score ( R =
738	    0.48, P = 0.002; Fig. 5h and Extended Data Fig. 9d ), whereas correlations were weak for visual
739	    tuning and absent for feedback tuning
740	  data: elsewhere
741	  where: IBL Brain Wide Map, https://registry.opendata.aws/ibl-brain-wide-map/ (release accessed
742	    February 2024), with the Gao et al. GaoROIs and hierarchy scores (Zenodo 14205018)
743	  statistics:
744	  - about: choice-tuned enrichment against intra-PFC hierarchy across GaoROIs
745	    test: Pearson correlation, two-sided
746	    statistic: R = 0.48
747	    p: 0.002
748	    n: 39 GaoROIs
749	  expected:
750	  - quantity: Pearson R, choice-tuned enrichment against hierarchy
751	    value: 0.48
752	    tolerance: 0.048
[... 133 more lines not kept]
```

**Agent**

Big claims file (about 38 claims). Reading the docs and the example entry next.

**Agent calls Bash**

```bash
sed -n 1,200p docs/archives.md | head -120; wc -l README.md docs/design.md
```

```
# Archives

The registry tests papers against data in public archives. It began with one,
the DANDI Archive. The protocol is written for any archive. What is particular
to an archive (how its datasets are named, versioned and read) is here, and an
agent is pointed to its archive's section.

A dataset is keyed as `<archive>:<id>` and shown as `<LABEL>:<id>`, for example
`DANDI:000003`. Its files in this repository (`claims/`, `questions/`,
`transcripts/`, the `attempt/` branch, the paper store) are under its folder
name: the identifier alone for DANDI, which the registry began with, and
`<archive>-<id>` for any other archive. Each archive is an adapter, a module in `tools/archives/` ("Adding an archive",
below), and `tools/datasets.py` turns one form of a dataset's name into another.
The workflows take a dataset in any of these forms.

## DANDI

- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md; sed -n 1,400p docs/design.md
```

```
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

## Reading the outcomes

An outcome says what one attempt could recover from the data in a dandiset,
[... 390 more lines not kept]
```

**Agent calls Bash**

```bash
ls entries/001453-fouke-2025/; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; cat attempts/001453-fouke-2025-01.yaml; ls questions | head;
```

```
<persisted-output>
Output too large (36.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/2a1918e7-9167-4006-bb17-a781d9ea2a7c/tool-results/ba49ocz4a.txt

Preview (first 2KB):
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt
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
[... 47 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/2a1918e7-9167-4006-bb17-a781d9ea2a7c/tool-results/ba49ocz4a.txt",
 "offset": 40,
 "limit": 400
}
```

```
40	  id: "001453"
41	  version: 0.250518.1950
42	  doi: 10.48324/dandi.001453/0.250518.1950
43	paper: doi:10.1016/j.cub.2025.04.027
44	date: 2026-10-14
45	entry: 001453-fouke-2025
46	provenance:
47	  kind: agent
48	  accountable:
49	    name: CatalystNeuro
50	  agent:
51	    harness: Claude Code (GitHub Actions)
52	    model: claude-opus-5-5
53	    protocol: pilot-5
54	  runner:
55	    platform: GitHub Actions
56	    url: https://github.com/catalystneuro/reproduction-registry/actions/runs/38574152687
57	inputs:
58	- what: Names of the stimulus codes (the conversion of stimulus names to codes, its printed list of
59	    codes, and its own labels for codes 9 to 13), the trial processing parameters, the spatial
[... 380 more lines not kept]
```

**Agent**

Now the dataset.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/001260/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/001260/versions/" | python -m json.tool | grep -E '"version"|"modified"|"status"|asset_count|size'
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/001260/versions/0.250911.0744/" > meta.json; python -c "
import json;m=json.load(open('meta.json'));print(m['description']);print(m.get('relatedResource'));print(json.dumps(m.get('assetsSummary'),indent=0)[:1500]); print(m.get('citation'))"; curl -s "https://api.dandiarchive.org/api/dandisets/001260/versions/0.250911.0744/assets/?page_size=200" > assets.json; python -c "
import json;a=json.load(open('assets.json'));print(a['count'])
for x in a['results']: print(x['path'], round(x['size']/1e9,2))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
python -c "import pynwb, remfile, h5py, dandi; print(pynwb.__version__)" 2>&1; which uv python; python --version
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb, remfile, h5py, dandi; print(pynwb.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
/opt/hostedtoolcache/Python/3.13.17/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
Python 3.13.17
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q pynwb remfile h5py numpy pandas scipy statsmodels matplotlib requests scikit-learn 2>&1 | tail -2; python -c "import pynwb;print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > probe.py <<'EOF'
import json, h5py, remfile, requests, time
a=json.load(open('assets.json'))['results']
x=[r for r in a if 'PL062' in r['path'] and 'probe0' in r['path']][0]
url=f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/"
s3=requests.head(url,allow_redirects=True).url
print(s3)
t=time.time()
f=h5py.File(remfile.File(s3),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset): print(name,obj.shape,obj.dtype, dict((k,str(v)[:80]) for k,v in obj.attrs.items() if k in ('unit','description','conversion','rate')))
    else: 
        if 'neurodata_type' in obj.attrs: print(name, '<',obj.attrs['neurodata_type'],'>', str(obj.attrs.get('description',''))[:200])
f.visititems(show)
print(time.time()-t)
EOF
python probe.py 2>&1 | grep -v "^acquisition/ElectricalSeries.*\|^$" | head -300
```

```
https://dandiarchive.s3.amazonaws.com/blobs/261/1a9/2611a969-fca5-4613-bb8b-67de975ce5ae?response-content-disposition=attachment%3B%20filename%3D%22sub-PL062_ses-PL062-20200420-probe0_behavior%2Becephys.nwb%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=[removed: an AWS key]%2F20261101%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20261101T123605Z&X-Amz-Expires=21600&X-Amz-SignedHeaders=host&X-Amz-Signature=11be64bf79fa5c96d0091d7e0053f80f00736c21825d19284ec4f46110db970d
analysis/LFP saturation start < TimeSeries > start times of the LFP saturation epoch
analysis/LFP saturation start/data (50,) float64 {'conversion': '1.0', 'unit': 'none'}
analysis/LFP saturation start/timestamps (50,) float64 {'unit': 's'}
analysis/LFP saturation stop < TimeSeries > stop times of the LFP saturation epoch
analysis/LFP saturation stop/data (50,) float64 {'conversion': '1.0', 'unit': 'none'}
analysis/LFP saturation stop/timestamps (50,) float64 {'unit': 's'}
analysis/spike saturation start < TimeSeries > start times of the spike saturation epoch
analysis/spike saturation start/data (19,) float64 {'conversion': '1.0', 'unit': 'none'}
analysis/spike saturation start/timestamps (19,) float64 {'unit': 's'}
analysis/spike saturation stop < TimeSeries > stop times of the spike saturation epoch
analysis/spike saturation stop/data (19,) float64 {'conversion': '1.0', 'unit': 'none'}
analysis/spike saturation stop/timestamps (19,) float64 {'unit': 's'}
file_create_date (1,) object {}
general/devices/array < Device > Neuropixels 3B1
general/experiment_description () object {}
general/experimenter (1,) object {}
general/extracellular_ephys/electrodes < DynamicTable > all electrodes
general/extracellular_ephys/electrodes/AP (383,) float64 {'description': 'my description'}
general/extracellular_ephys/electrodes/DV (383,) float64 {'description': 'my description'}
[... 122 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > probe2.py <<'EOF'
import json, h5py, remfile, requests, time, numpy as np, sys
a=json.load(open('assets.json'))['results']
pat=sys.argv[1]
x=[r for r in a if pat in r['path']][0]
print(x['path'])
url=f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/"
s3=requests.head(url,allow_redirects=True).url
t=time.time()
f=h5py.File(remfile.File(s3),'r')
for k in ['session_description','general/session_id','general/experiment_description','general/stimulus','general/keywords','general/subject/age','general/subject/sex','general/subject/genotype','general/subject/subject_id','general/subject/description','general/surgery','session_start_time']:
    try: print(k, f[k][()])
    except Exception as e: print(k,'--',e)
print(list(f['units'].keys()))
print(list(f['intervals'].keys()) if 'intervals' in f else None)
e=f['general/extracellular_ephys/electrodes']
loc=np.array([s.decode() if isinstance(s,bytes) else s for s in e['location'][:]])
print(np.unique(loc,return_counts=True))
print('label',e['label'][:5], 'AP', e['AP'][:3], e['DV'][:3], e['ML'][:3])
u=f['units']
el=u['electrodes'][:]; print('unit el range',el.min(),el.max(), len(el))
for c in ['Peak_to_Trough','duration','HW','FS','RS']:
    if c in u: v=u[c][:]; print(c, np.nanpercentile(v.astype(float),[0,5,50,95,100]), np.isnan(v.astype(float)).sum())
if 'quality' in u: q=u['quality'][:]; print('quality', np.nanpercentile(q,[0,50,95,100],axis=0))
t0=time.time(); st=u['spike_times'][:]; print('spikes',len(st), st[:3], st[-1], 'read s', time.time()-t0)
idx=u['spike_times_index'][:]; print(np.all(np.diff(st[:idx[0]])>=0))
if 'trials' in f['intervals']:
    tr=f['intervals/trials']
    for k in tr: 
        v=tr[k][:]; print(k, v[:8], len(v), np.unique(v)[:10] if v.dtype!=float else '')
for k in f['stimulus/presentation']: print(k, f['stimulus/presentation'][k]['data'][:10], f['stimulus/presentation'][k]['timestamps'][:5])
print(time.time()-t)
EOF
python probe2.py PL062_ses-PL062-20200420-probe0 2>&1
```

```
sub-PL062/sub-PL062_ses-PL062-20200420-probe0_behavior+ecephys.nwb
session_description b'Neuropixelsrecording in mPFC during contextual pavlovian conditioning task'
general/session_id b'PL062_20200420-probe0'
general/experiment_description b'Neuropixelsrecording in mPFC during contextual pavlovian conditioning task'
general/stimulus [b'pure tone, white noise, reward']
general/keywords [b'Prefrontal Cortex' b'Auditory Processing' b'Context']
general/subject/age b'P3M2D'
general/subject/sex b'F'
general/subject/genotype b'C57BL/6J (JAX\xe2\x84\xa2 Mice Strain)'
general/subject/subject_id b'PL062'
general/subject/description b'Mouse implanted with a chamber for acute recordings'
general/surgery b'Mice were prepared for electrophysiology with a recording chamber and a headpost.The scalp and periosteum over the dorsal surface of the skull were removed.A layer of cyanoacrylate adhesive (Locite) was directly applied to the intact skull.A custom made headpost was placed on the skull (approximately over cerebellum and right hemisphere) and cemented in place with Palavit/Paladur.'
session_start_time b'2020-04-20T17:20:44.000000+02:00'
['FS', 'HW', 'PTR', 'Peak_to_Trough', 'PeaktoBaseline', 'PeaktoBaselineArea', 'PeaktoOnset', 'PeaktoOnsetTime', 'RS', 'TroughSize', 'dVdT', 'duration', 'electrodes', 'height', 'id', 'quality', 'spike_times', 'spike_times_index', 'waveform_means']
['trials']
(array(['ACAd5', 'AON', 'ILA6a', 'MOs2/3', 'MOs5', 'OLF', 'ORBl2/3',
       'ORBl5', 'ORBm6a', 'ORBvl2/3', 'ORBvl5', 'ORBvl6a', 'PL5', 'PL6a',
       'aco'], dtype='<U8'), array([42, 22, 22,  1,  1, 98,  8, 18, 16,  2, 22, 29, 32, 54, 16]))
label [b'probe1elec1' b'probe1elec2' b'probe1elec3' b'probe1elec4'
 b'probe1elec5'] AP [-2.17370967 -2.17127109 -2.17127109] [-5.11880075 -5.09952605 -5.09952605] [-1.39239879 -1.39524733 -1.38765122]
[... 29 more lines not kept]
```

**Agent**

Files open in about 3 s each when only the needed arrays are read. Units carry `Peak_to_Trough` and electrode locations with layers (for example `PL5`). Next I'll survey all 74 files.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import json, h5py, remfile, requests, time, numpy as np, pandas as pd
from concurrent.futures import ThreadPoolExecutor
a=json.load(open('assets.json'))['results']
def dec(v): return v.decode() if isinstance(v,bytes) else v
def one(x):
    url=f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/"
    s3=requests.head(url,allow_redirects=True).url
    f=h5py.File(remfile.File(s3),'r')
    d=dict(path=x['path'])
    d['sess']=dec(f['general/session_id'][()]); d['desc']=dec(f['session_description'][()])[:60]
    d['subj']=dec(f['general/subject/subject_id'][()]); d['sex']=dec(f['general/subject/sex'][()]); d['age']=dec(f['general/subject/age'][()])
    d['start']=dec(f['session_start_time'][()])
    u=f['units']; d['units_cols']=','.join(sorted(u.keys()))
    d['n_units']=len(u['id'])
    d['n_spk']=u['spike_times'].shape[0]
    e=f['general/extracellular_ephys/electrodes']
    d['n_el']=len(e['id']); d['el_cols']=','.join(sorted(e.keys()))
    d['groups']=','.join(f['general/extracellular_ephys'].keys())
    d['intervals']=','.join(f['intervals'].keys()) if 'intervals' in f else ''
    d['analysis']=','.join(f['analysis'].keys()) if 'analysis' in f else ''
    d['stim']=','.join(f['stimulus/presentation'].keys()) if 'stimulus/presentation' in f else ''
    d['beh']=','.join(f['processing/behavior'].keys()) if 'processing/behavior' in f else ''
    d['ecephys']=','.join(f['processing/ecephys'].keys()) if 'processing/ecephys' in f else ''
    d['acq']=','.join(f['acquisition'].keys()) if 'acquisition' in f else ''
    d['keywords']=','.join(dec(k) for k in f['general/keywords'][:]) if 'general/keywords' in f else ''
    if 'stimulus/presentation/AudStim_10kHz' in f:
        ts=f['stimulus/presentation/AudStim_10kHz/timestamps'][:]; d['n_tone']=len(ts); d['tone_dt_med']=np.median(np.diff(ts)) if len(ts)>1 else np.nan
    return d
t=time.time()
with ThreadPoolExecutor(12) as ex: rows=list(ex.map(one,a))
df=pd.DataFrame(rows); df.to_pickle('survey.pkl'); print(time.time()-t)
pd.set_option('display.width',250); pd.set_option('display.max_columns',30); pd.set_option('display.max_colwidth',60)
print(df[['sess','subj','sex','age','n_units','n_tone','tone_dt_med','desc']].to_string())
for c in ['units_cols','el_cols','groups','intervals','analysis','stim','beh','ecephys','acq','keywords']:
    print(c); print(df[c].value_counts().to_string())
EOF
python survey.py 2>&1
```

```
86.64807033538818
                      sess      subj sex     age  n_units  n_tone  tone_dt_med                                                          desc
0   249939_20200611-probe0    249939   F  P2M25D      376   200.0     8.883158  Neuropixels recording in mPFC during aversive conditioning t
1   250252_20200609-probe0    250252   M  P2M21D      164   200.0     8.214505  Neuropixels recording in mPFC during aversive conditioning t
2   249940_20200610-probe0    249940   F  P2M24D      426   200.0     8.694114  Neuropixels recording in mPFC during aversive conditioning t
3   250253_20200609-probe0    250253   M  P2M21D      502   200.0     8.754077  Neuropixels recording in mPFC during aversive conditioning t
4   242820_20200526-probe0    242820   M  P3M14D      407   200.0     8.412192  Neuropixels recording in mPFC during aversive conditioning t
5   534133_20220302-probe0    534133   F  P2M18D      325   180.0    10.355939  Neuropixels recording in mPFC during auditory detection task
6   518804_20220228-probe0  518804_1   F  P2M17D      266   274.0    10.374431  Neuropixels recording in mPFC during auditory detection task
7   518804_20220301-probe0  518804_2   F  P2M17D      394   308.0    10.626720  Neuropixels recording in mPFC during auditory detection task
8   560169_20220506-probe0    560169   F   P2M5D      264   302.0    10.507573  Neuropixels recording in mPFC during auditory detection task
9   560171_20220505-probe0  560171_2   F   P2M5D      191   235.0    10.044683  Neuropixels recording in mPFC during auditory detection task
10  560171_20220504-probe0  560171_1   F   P2M5D      129   246.0    10.589739  Neuropixels recording in mPFC during auditory detection task
11  708078_20231002-probe0    708078   F   P6M2D      130     NaN          NaN    Neuropixels recording in HPC during passive listening task
12  250256_20200610-probe0    250256   F  P2M22D      235   300.0     8.208373  Neuropixels recording in mPFC during aversive conditioning t
13  7327
[... 110 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "^(Methods|Unit quality|Waveform classification|Epoch selection|Detection of sleep|Enrichment|Group-bias|Self-organiz|Hierarch|Stability|Habituation|Neuropixels|Spike sorting|Histolog|Statistic|Data availability|Code availability|Linear mixed|Firing metric|Tone resp|ZETA|Parcellation|Projection)" 10.1038-s41593-025-02190-z.txt | head -60; wc -l 10.1038-s41593-025-02190-z.txt
```

```
219 10.1038-s41593-025-02190-z.txt
```

**Agent calls Bash**

```bash
cd paper; awk '{print NR": "length($0)": "substr($0,1,100)}' 10.1038-s41593-025-02190-z.txt | head -219
```

```
1: 31: DOI: 10.1038/s41593-025-02190-z
2: 30: Version: as served by crossref
3: 52: Source: crossref+publisher_html (paper-text-fetcher)
4: 18: Stored: 2026-10-21
5: 21: Extracted: as fetched
6: 72: ------------------------------------------------------------------------
7: 55: A prefrontal cortex map based on single-neuron activity
8: 0: 
9: 8: Abstract
10: 1063: The intrinsic organization underlying the central cognitive role of the prefrontal cortex (PFC) is p
11: 0: 
12: 34: 10.1016/B978-0-12-407815-4.00002-7
13: 0: 
14: 53: Fuster, J. M. The Prefrontal Cortex (Elsevier, 2015).
15: 0: 
16: 23: 10.1126/science.aan8868
17: 0: 
18: 80: Carlen, M. What constitutes the prefrontal cortex?. Science 358, 478–482 (2017).
19: 0: 
20: 23: 10.1126/science.aat5691
[... 199 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 -c "
t=open('10.1038-s41593-025-02190-z.txt').read(); print(len(t)); print(t.count('\n'), t.count('\r'))
import re
for m in re.finditer(r'(Unit quality|Waveform classification|Epoch selection|Detection of sleep|Enrichment statistics|Group-bias|Self-organizing|Stability analyses|Habituation and behavioral|Linear mixed|Firing metrics|ZETA test|Methods|Statistics and reproducibility|Data availability)', t): print(m.start(), m.group())
"
```

```
138156
219 0
7911 Methods
14813 Methods
19144 Methods
21368 Methods
22813 Methods
22866 Methods
41449 Methods
41459 ZETA test
44314 Methods
45639 Methods
54769 Methods
56727 Habituation and behavioral
57050 Methods
63666 Unit quality
65671 Statistics and reproducibility
66214 ZETA test
66306 ZETA test
68429 Detection of sleep
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 -c "
t=open('10.1038-s41593-025-02190-z.txt').read(); print(t[54700:78000])"
```

```
orward, with broad applicability to other brain regions and species. Methods Animals All procedures and experiments on animals were performed according to the guidelines of the Stockholm Municipal Committee for animal experiments and the Karolinska Institutet in Sweden (approval numbers 7362-2019 and 1535-2024). Adult wild-type mice (C57BL/6J, Charles River; 27 male and 39 female) aged 3–6 months were used. Animals were group-housed, up to five per cage, in a temperature-controlled (23 °C) and humidity-controlled (55%) environment in standard cages on a 12:12-h reversed light/dark cycle with ad libitum access to food and water, unless placed on a water restriction schedule. All water-restricted mice were restricted to 85–90% of their initial body weight by administering 1 ml of water per day. Surgery Adult mice were anesthetized with isoflurane (3% for induction, then 1–2%). Buprenorphine (0.1 mg per kg body weight, subcutaneous (s.c.)), carprofen (5 mg per kg body weight, s.c.) and lidocaine (4 mg per kg body weight, s.c.) were administered. The body temperature was maintained at 37 °C by a heating pad. An ocular ointment (Viscotears, Alcon) was applied over the eyes. The head of the mouse was fixed in a stereotaxic apparatus (Kopf). Lidocaine (2%) was injected locally before skin incision. The skin overlying the cortex was removed; the skull was first cleaned with chlorhexidine and then gently scratched with a scalpel blade. A thin layer of glue was applied on the exposed skull. A lightweight metal head-post was fixed with lightcuring dental adhesive (OptiBond FL, Kerr) and cement (Tetric EvoFlow, Invoclar Vivadent). For extracellular recordings, a chamber was constructed by building a wall with dental cement along the coronal suture and the front of the skull. Brain regions were targeted using stereotaxic coordinates. After the surgery, the animal was returned to its home cage, and carprofen (5 mg per kg body weight, s.c.) was provided for postoperative pain reli
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 -c "
t=open('10.1038-s41593-025-02190-z.txt').read(); i=t.find('SOM analysis',78000); print(t[i-200:99400])"
```

```
mutual enrichment between spontaneous activity and task variables shown in Fig. 5k is of necessity based on the dataset IBL Passive, for which spontaneous activity was available along with task data. SOM analysis A SOM is an unsupervised machine learning algorithm 42 used here to summarize a set of n -dimensional feature vectors into a two-dimensional grid of nodes. Each node represents an n -dimensional prototype vector (visualized as a hexagon). After training the SOM, similar prototype vectors become neighbors on the SOM grid. Separate SOMs were constructed for the following data selections of the dataset KI: (i) spontaneous activity of ww units, (ii) spontaneous activity of nw units (iii) and tone responses of ww units. Input features To obtain input for training the SOM, each unit j was represented by a feature vector. For spontaneous activity (i and ii), the feature vector x j consisted of the three spontaneous firing metrics: x j = [log 10 FR, burstiness, memory]; see ‘Extraction of spontaneous activity metrics’. For tone response activity (iii), the feature vector comprised eight principal component scores (PCSs) summarizing the tone response trace of each unit: x j = [PCS j, 1 , PCS j ,2 ,… PCS j ,8 ]; see ‘Extraction and post-processing of tone responses’. Feature vectors were collected from all units in the respective data selection. Each feature was standardized by subtracting the mean and dividing by the standard deviation across all included units. SOM architecture and initialization The number of nodes in the SOM was manually determined to balance a detailed representation of the input space (requiring more nodes) with preservation of neighborhood relationships and a compact visualization (requiring fewer nodes). The shape ( x – y dimensions) of the SOM and initialization of nodes were determined using the linear initialization method suggested by Kohonen 43 . This involved performing a PCA on the input feature vectors and setting the height and width
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 -c "
t=open('10.1038-s41593-025-02190-z.txt').read(); print(t[99300:100600]); i=t.find('Extended Data Fig. 1 ',100000); print(t[i-100:i+3000])"; date -u
```

```
re Portfolio Reporting Summary linked to this article. Data availability The data from the 99 recorded Neuropixels sessions used to generate all main and supplementary figures is available for download in NWB format on the DANDI Archive via https://dandiarchive.org/dandiset/000473/ and https://dandiarchive.org/dandiset/001260/ . Source data are provided with this paper. Code availability The code used to preprocess the data and generate all manuscript figures is available at GitHub via https://github.com/hejDMC/pfcmap/ and Zenodo via https://doi.org/10.5281/zenodo.17559037 (ref. 54 ). The following open-source software and toolboxes were used: Python: matplotlib, netgraph, numpy, scipy, shapely, sklearn, SOMz; Julia: LightXML, MixedModels, Statistics, StatsBase, StatsModels, StatsPlots; R: emmeans, lme4, MuMIn, pbkrtest. References Fuster, J. M. The Prefrontal Cortex (Elsevier, 2015). Carlen, M. What constitutes the prefrontal cortex?. Science 358 , 478–482 (2017). Article PubMed CAS Google Scholar Wang, X. et al. Three-dimensional intact-tissue sequencing of single-cell transcriptional states. Science 361 , eaat5691 (2018). Article PubMed PubMed Central Google Scholar Ortiz, C. et al. Molecular atlas of the adult mouse brain. Sci. Adv. 6 , eabb3446 (2020). Article PubMed PubMed 
ith regard to jurisdictional claims in published maps and institutional affiliations. Extended data Extended Data Fig. 1 The dataset KI, with description of data selection and correlations between spontaneous firing metrics. a, b Count, per brain region ( a ) and per PFC subregion ( b ), of all high-quality, manually sorted, single units included in the dataset KI. c , Excluding ‘sleep-like’ periods. Gray horizontal bars indicate 3 s epochs of spontaneous activity directly preceding tone presentation (200 ms, orange bar); black vertical line: tone onset. The left side exemplifies spontaneous epochs included in analysis; the right side exemplifies spontaneous sleep-like epochs excluded from 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000473/ | python -c "import json,sys;d=json.load(sys.stdin);print(d['most_recent_published_version'])"; curl -s "https://api.dandiarchive.org/api/dandisets/000473/versions/draft/assets/?page_size=200" | python -c "
import json,sys;a=json.load(sys.stdin);print(a['count'])
for x in a['results']: print(x['path'], round(x['size']/1e9,2))" | head -60; git clone -q https://github.com/hejDMC/pfcmap pfcmap && cd pfcmap && git checkout -q 9ae52eddc47fbb590ef4e1b1949507334707a0f1 && git log -1 --format=%H && ls
```

Result: the fetched text is not kept.

**Agent**

000473 holds 25 aversion recordings (a dandiset named for another paper); 74 + 25 = 99, the paper's recording count. Looking at the paper's code next.

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap; find . -type f | grep -v "\.git/" | sed 's|/[^/]*$||' | sort | uniq -c | sort -rn | head -30; ls python; ls python/config 2>/dev/null | head
```

```
27 ./python/utils
     20 ./python/callers
     13 ./python/enrichments
     11 ./python/goalDirectedBehavior_IBL
      9 ./python/flatmaps
      8 ./python/preprocessing/quiet_extraction
      8 ./python/SOM/clusterSOM
      7 ./python/connectivity_correlations
      7 ./python/config/stimplotstyles
      6 ./python/preprocessing/lick_extraction
      6 ./python/PATHS
      6 ./julia
      5 ./python/quiet_active_stats
      5 ./python/dataset_general
      5 ./python/SOM
      5 ./python
      4 ./python/metrics_extraction/spontaneous
      4 ./python/config/somsettings
      4 ./python/config
      3 ./python/utils/ica_tools
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap/python; cat settings.py | head -150; ls config/datatables config/somsettings SOM SOM/clusterSOM metrics_extraction/spontaneous preprocessing/quiet_extraction stability enrichments utils
```

```
import numpy as np
from glob import glob
import os
import pandas as pd
import re

ctx_regions = ['AUD','MO','SS','VIS']#append if you use more!!!

runsets = {'wwspont':'runC00dMP3_brain','nwspont':'runC00dMI3_brain',\
           'wwresp':'runCrespZP_brain','nwresp':'runCrespZI_brain',\
           'wwIBL':'runIBLPasdMP3_brain_pj','nwIBL':'runIBLPasdMI3_brain_pj'}

cmethod = 'ward'
nclust_dict = {'wwspont':8,'nwspont':5,'wwresp':8,'nwresp':5,'wwIBL':8,'nwIBL':5}

task_replacer = {'Opto':'Passive'}

enr_fn = lambda sdict: ((sdict['matches']-sdict['meanshuff'])/sdict['stdshuff'])
frac_fn = lambda sdict: sdict['matches']/sdict['matches'].sum(axis=1)[:,None]

[... 225 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap/python; . $TMPDIR/dev/bin/activate; uv pip install -q openpyxl; python -c "
import pandas as pd; x=pd.read_excel('config/datatables/allrecs_allprobes.xlsx',sheet_name=None)
for k,v in x.items(): print(k,v.shape); print(v.columns.tolist()); print(v.head(3).to_string())
"; grep -n "parent_dict" -A30 settings.py | head -50
```

```
sheet0 (114, 17)
['#', 'recid', 'usable_gen', 'lickdet_src', 'lickdet_done', 'lickdet_quality', 'quietdet_region', 'offdet_src', 'offdet_done', 'offdet_q', 'quietdet_src', 'quietdet_quality', 'use_quiet', 'datasetlab', 'exptype', 'probetype', 'locs']
     #                  recid usable_gen lickdet_src lickdet_done lickdet_quality quietdet_region offdet_src offdet_done offdet_q quietdet_src quietdet_quality use_quiet datasetlab  exptype probetype locs
0  NaN   #### EXPTYPE Passive        NaN         NaN          NaN             NaN             NaN        NaN         NaN      NaN          NaN              NaN       NaN        NaN      NaN       NaN  NaN
1  1.0  PL026_20190430-probe0        NaN          na           na              na             PFC        NaN         NaN        +         self              NaN       NaN       mPFC  Passive       NPX  NaN
2  2.0  PL027_20190511-probe0        NaN          na           na              na             PFC        NaN         NaN        +         self              NaN       NaN       mPFC  Passive       NPX  NaN
lick_selection (51, 21)
['recid', 'run_tag', 'usable_gen', 'lickdet_src', 'lickdet_done', 'lickdet_quality', 'lickdet_comment', 'lick: info_exp update', 'examp_plot', 'lick-alignm. checked', 'quietdet_regions', 'offdet_src', 'offdet done', 'offdet_q', 'quietdet_src', 'quietdet_quality', 'use_quiet', 'datasetlab', 'exptype', 'probetype', 'regions']
                    recid  run_tag  usable_gen          lickdet_src lickdet_done lickdet_quality                                                                                                                                      lickdet_comment lick: info_exp update examp_plot lick-alignm. checked quietdet_regions offdet_src offdet done offdet_q quietdet_src quietdet_quality use_quiet datasetlab    exptype probetype       regions
0  #### EXPTYPE Detection      NaN         NaN                  NaN          NaN             NaN                                                
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap/python; . $TMPDIR/dev/bin/activate; python -c "
import pandas as pd; x=pd.read_excel('config/datatables/allrecs_allprobes.xlsx',sheet_name='sheet0')
x=x[x.recid.astype(str).str.contains('probe')]
print(len(x)); print(x[['recid','usable_gen','exptype','probetype','use_quiet','quietdet_src','datasetlab']].to_string())
"
```

```
100
                      recid usable_gen    exptype probetype use_quiet       quietdet_src datasetlab
1     PL026_20190430-probe0        NaN    Passive       NPX       NaN               self       mPFC
2     PL027_20190511-probe0        NaN    Passive       NPX       NaN               self       mPFC
3     PL028_20190517-probe0        NaN    Passive       NPX       NaN               self       mPFC
4     PL030_20190518-probe0        NaN    Passive       NPX       NaN               self       mPFC
5     PL031_20190524-probe0        NaN    Passive       NPX       NaN               self       mPFC
6     PL032_20190524-probe0        NaN    Passive       NPX       NaN               self       mPFC
8    128514_20191215-probe0        NaN   Aversion       NPX       NaN               self       mPFC
9    128515_20191216-probe0        NaN   Aversion       NPX       NaN               self       mPFC
10   128516_20191215-probe0        NaN   Aversion       NPX       NaN               self       mPFC
11   147463_20191113-probe0        NaN   Aversion       NaN       NaN               self       mPFC
12   147465_20191113-probe0        NaN   Aversion       NaN       NaN               self       mPFC
13   152414_20191023-probe0        NaN   Aversion       NPX       NaN               self       mPFC
14   152417_20191023-probe0        NaN   Aversion       NPX       NaN               self       mPFC
15   152419_20191106-probe0        NaN   Aversion       NPX       NaN               self       mPFC
16   156130_20191112-probe0        NaN   Aversion       NPX       NaN               self       mPFC
17   156131_20191112-probe0        NaN   Aversion       NPX       NaN               self       mPFC
18   216300_20200518-probe0        NaN   Aversion       NPX       NaN               self       mPFC
19   216301_20200521-probe0        NaN   Aversion       NPX       NaN               self       mPFC
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap/python; grep -rn -i "isi_viol\|amplitude_cutoff\|presence_ratio\|quality" --include=*.py . | grep -v "lickdet_quality\|quietdet_quality" | head -30; grep -rn "def get_metricsfiles" -A40 settings.py | head -60
```

```
./SOM/plot_SOM.py:316:                                     ,scalefree=True,return_scale=False,alphahex=1,idcolor='k',quality_map=dcolors)#rankvec
./SOM/plot_SOM.py:451:                                             ,scalefree=True,return_scale=False,alphahex=1,idcolor='k',quality_map=dcolors)#rankvec
./SOM/plot_SOM_brain.py:195:                                     ,scalefree=True,return_scale=False,alphahex=1,idcolor='k',quality_map=dcolors)#rankvec
./SOM/clusterSOM/identify_nclust_SOM.py:113:                           , scalefree=True, return_scale=False, alphahex=1, idcolor='k', quality_map=dcolors)  # rankvec
./SOM/clusterSOM/identify_nclust_SOM.py:133:        flist = cfns.plot_clustquality(evaldict,nclustvec,show_rand=randbool)#,scoredict=scoredict
./SOM/clusterSOM/identify_nclust_SOM.py:138:            figsaver(f,'%s/quality/%s%s'%(cmethod,evalkey,randtag))
./SOM/clusterSOM/clusterplot_SOM.py:207:                                     ,scalefree=True,return_scale=False,alphahex=1,idcolor='k',quality_map=dcolors)#rankvec
./goalDirectedBehavior_IBL/extract_taskresp.py:52:    Units, somfeats, weightvec = uloader.load_all_units_for_som(metricsfiles, rundict, check_pfc=True,check_wavequality=False)
./goalDirectedBehavior_IBL/flatmap_tessellationIBL.py:49:                                                           rois_from_path=False,check_wavequality=False)
./goalDirectedBehavior_IBL/calc_statsdict_gaoRois_tuning.py:45:Units, somfeats, weightvec = uloader.load_all_units_for_som(metricsfiles, rundict, check_pfc=True,check_wavequality=False, \
./goalDirectedBehavior_IBL/plot_tuning_flatmaps.py:246:    nvec_quality = np.arange(1, int(len(X) / 2))
./goalDirectedBehavior_IBL/plot_tuning_flatmaps.py:248:    f = cfns.plot_thorndike(nvec_quality, distbaseMat, linkage_method=S.cmethod)
./goalDirectedBehavior_IBL/plot_tuning_flatmaps.py:251:    evaldict = cfns.eval_asfn_nclust(distbaseMat, nvec_quality[nvec_quality > 1], clustfn, evalfns)
./goalDirectedBehavior_IBL/plot_tuning_fl
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pandas as pd; d=pd.read_pickle('survey.pkl'); print(d.n_units.sum(), len(d))"; sed -n 1,200p pfcmap/python/metrics_extraction/spontaneous/extract_prepost_quietactive.py
```

```
20374 74
import sys
import yaml
import os
import numpy as np
import h5py
import git
import pandas as pd

precut = 3.
ttags = ['prestim']
postcut = 0
block_licking = True
savepattern = '%s__TSEL%s{}__STATE%s%s.h5'.format(int(precut)) #% (aRec.id, ttag, statetag,reftag)

active_buff = np.array([-1,1])
quiet_buff = np.array([0,0])
#on_files = 'all'

badtimesdir = 'ZENODOPATH/preprocessing/bad_times_manual'
[... 182 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap/python; cat config/somsettings/somsettings_carlenSpont.yml | head -80; grep -n "refkeydict" -A15 utils/tint_funcs.py | head -40
```

```
runC00dMP3_brain:
    state: 'active'
    tsel: 'prestim'
    layerlist: 'all'
    reftag: 'all'
    spec: 'dur3'
    datasets: ['Carlen']
    tasks: ['Passive','Aversion','Opto','Detection','Context','Attention']#
    imetrics:
      features: ['B_mean','M_mean','rate_mean']
      weights: [1,1,1]
    wmetrics:
      features: []#['peak2Trough','abRatio','p2tRatio']
      weights: []#[1,1,1]
    utypes: ['ww']
    nnodes: 400
    clustering:
      ward: [6,7,8,9]


[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap/python; sed -n 1,200p metrics_extraction/spontaneous/extract_quantities_meanvar.py | grep -v "^\s*#" | head -150
```

```
import sys
from matplotlib import pyplot as plt
import yaml
import os
import numpy as np
import h5py
import git

n_tints_min = 6 #minimum number of tints needed to calculate mean and std
nmin_per_block = 3 #minimal number of tints per block to calculate quantity
mininput_ifn = 4 #min_nspike_per_trial = mininput_ifn+2#n-spikes = n_intervals +1; if intervals are paired you need +1 to make the pairing; so with 3 mininput you have at least 5 spikes/trial
full_estimate_trials_only = False


plot_on = True
save_on = True


plotvars = ['rate','B','LvR','M']
varselection = ['M', 'B', 'Lv', 'LvR', 'CV2', 'IR', 'Rho']
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap/python; date -u; grep -n "def \|ratio\|eig\|sqrt\|sigma\|alpha\|exp(" utils/my_somz.py | head -60; grep -n "shape\|kshape\|nnodes\|ratio" SOM/calc_SOM.py utils/som_helpers.py | head -30
```

```
Sun Nov  1 12:41:10 UTC 2026
20:def get_index(ix, iy, nx, ny):
24:def get_pair(ii, nx, ny):
30:def get_ns(ix, iy, nx, ny, index=False):
32:    Get neighbors for rectangular grid given its
40:    :return: Array of indexes for direct neighbors
63:def get_ns_hex(ix, iy, nx, ny, index=False):
65:    Get neighbors for hexagonal grid given its coordinates
90:def geometry(top, Ntop, periodic='no'):
133:                    distLib[i, j] = numpy.sqrt((bX[i] - bX[j]) ** 2 + (bY[i] - bY[j]) ** 2)
138:                    s0 = numpy.sqrt((bX[i] - bX[j]) ** 2 + (bY[i] - bY[j]) ** 2)
139:                    s1 = numpy.sqrt((bX[i] - (bX[j] + 1. + dx)) ** 2 + (bY[i] - bY[j]) ** 2)
140:                    s2 = numpy.sqrt((bX[i] - (bX[j] + 1. + dx)) ** 2 + (bY[i] - (bY[j] + 1. + dy)) ** 2)
141:                    s3 = numpy.sqrt((bX[i] - (bX[j] + 0.)) ** 2 + (bY[i] - (bY[j] + 1. + dy)) ** 2)
142:                    s4 = numpy.sqrt((bX[i] - (bX[j] - 1. - dx)) ** 2 + (bY[i] - (bY[j] + 1. + dy)) ** 2)
143:                    s5 = numpy.sqrt((bX[i] - (bX[j] - 1. - dx)) ** 2 + (bY[i] - (bY[j] + 0.)) ** 2)
144:                    s6 = numpy.sqrt((bX[i] - (bX[j] - 1. - dx)) ** 2 + (bY[i] - (bY[j] - 1. - dy)) ** 2)
145:                    s7 = numpy.sqrt((bX[i] - (bX[j] + 0.)) ** 2 + (bY[i] - (bY[j] - 1. - dy)) ** 2)
146:                    s8 = numpy.sqrt((bX[i] - (bX[j] + 1. + dx)) ** 2 + (bY[i] - (bY[j] - 1. - dy)) ** 2)
173:                    distLib[i, j] = numpy.sqrt((bX[i] - bX[j]) ** 2 + (bY[i] - bY[j]) ** 2)
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap/python; sed -n 90,130p utils/my_somz.py; sed -n 300,380p utils/my_somz.py; grep -n "def getInitialMap_pca" -A25 utils/som_helpers.py; grep -n "def get_kshape" -A9 utils/som_helpers.py
```

```
def geometry(top, Ntop, periodic='no'):
    """
    Pre-compute distances between cells in a given topology
    and store it on a distLib array

    :param str top: Topology ('grid','hex','sphere')
    :param int Ntop: Size of map,  for grid Size=Ntop*Ntop,
        for hex Size=Ntop*(Ntop+1[2]) if Ntop is even[odd] and for sphere
        Size=12*Ntop*Ntop and top must be power of 2
    :param str periodic: Use periodic boundary conditions ('yes'/'no'), valid for 'hex' and 'grid' only
    :return: 2D array with distances pre computed between cells and total number of units
    :rtype: 2D float array, int
    """
    '''try:
        #import healpy as hpx
    except:
        print 'Error: healpy module not found, use grid or hex topologies'
        sys.exit(0)'''
    if top == 'sphere':
        nside = Ntop
[... 139 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap/python; sed -n 867,885p utils/som_helpers.py; sed -n 150,175p utils/my_somz.py; grep -n "def get_sigma" -B2 -A5 utils/my_somz.py | head; grep -n "NT\b\|self.np\b" utils/my_somz.py | head
```

```
pca.fit(data)
    eigvec = pca.components_
    eigval = pca.explained_variance_
    norms = np.sqrt(np.einsum('ij,ij->i', eigvec, eigvec))
    eigvec = ((eigvec.T/norms)*eigval).T; eigvec.shape
    for j in range(nnodes):
        for i in range(eigvec.shape[0]):
            codebook[j,:] = codebook[j, :] + coord[j,i]*eigvec[i,:]
            
    initcode = np.around(codebook, decimals = 6)
    return initcode.T

def get_quantisationError(roimat,weights):
    error = 0
    bmus = get_bmus(roimat,weights)
    for bmu,roi in zip(bmus,roimat): error += np.linalg.norm(roi-weights[:,bmu])
    return error/roimat.shape[0]

def get_topologicalError(roimat,weights,kshape):
        nx = Ntop[0]
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap/python; grep -v "^\s*#" SOM/clusterSOM/relabel_clusters.py | grep -v "^\s*$" | head -80; grep -n "linkage\|fcluster\|sort\|median" SOM/clusterSOM/cluster_SOM.py utils/clustering.py | head -30
```

```
import yaml
import os
import sys
import h5py
import numpy as np
from numpy import array
pathpath = 'PATHS/filepaths_carlen.yml'
myrun = 'runCrespZI_brain'
cmethod = 'ward'
label_sorter = {'runC00dMP3_brain':{9:np.array([5,1,7,2,3,4,8,9,6])-1,\
                                    8:np.array([4,1,6,2,3,7,8,5])-1,\
                                    7:np.array([3,1,5,2,6,7,4])-1,\
                                    6:np.array([4,1,2,5,6,3])-1},\
                'runC00dMI3_brain':{9:np.array([1,5,6,2,3,7,9,8,4])-1,\
                                    8:np.array([1,5,6,2,3,8,7,4])-1,\
                                    7:np.array([1,4,5,2,7,6,3])-1,\
                                    6:np.array([1,2,4,6,5,3])-1,\
                                    5:np.array([1,2,4,5,3])-1},\
                'runCrespZP_brain':{10: array([3, 6, 7, 9, 8, 1, 2, 5, 4, 0]),\
                                    9: array([3, 5, 6, 8, 7, 1, 4, 2, 0]),\
[... 73 more lines not kept]
```

**Agent**

Plan settled: the core analysis runs on 001260 alone. I'm writing the helper now: per-file loading, per-epoch metrics, sleep-like detection, the SOM and E-scores.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > q.py <<'EOF'
import json, h5py, remfile, requests, numpy as np
a=json.load(open('assets.json'))['results']
for pat in ['PL026_','249939','PL079_20230620-probe0','708078_20231002-probe0','PL027_20190511-probe1']:
    x=[r for r in a if pat in r['path']][0]
    s3=requests.head(f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/",allow_redirects=True).url
    f=h5py.File(remfile.File(s3),'r')
    q=f['units/quality'][:]; print(pat, 'q0 pct', np.percentile(q[:,0],[10,50,90]).round(3), 'q1', np.percentile(q[:,1],[10,50,90]).round(3), 'frac q0<0.1',(q[:,0]<0.1).mean().round(2),'q1<0.1',(q[:,1]<0.1).mean().round(2))
    an=f['analysis']
    for k in an: print(' ',k, an[k]['data'][:3], an[k]['timestamps'][:3])
    print(' stim', {k:(f['stimulus/presentation'][k]['timestamps'].shape, f['stimulus/presentation'][k]['data'][:4]) for k in f['stimulus/presentation']})
    tr=f['intervals/trials']; print(' trials', list(tr.keys()), len(tr['start_time']))
    if 'Block' in tr: b=tr['Block'][:]; print(' Block runs', np.sum(np.diff(b.astype(int))!=0)+1, np.unique(b))
    if 'processing/behavior/LickOnset' in f: lo=f['processing/behavior/LickOnset/lick_onset_data/timestamps'][:]; lf=f['processing/behavior/LickOffset/lick_offset_data/timestamps'][:]; print(' licks',len(lo), np.median(lf-lo))
EOF
python q.py
```

```
Exit code 1
PL026_ q0 pct [ 0.  0. 11.] q1 [0.    0.    0.281] frac q0<0.1 0.5 q1<0.1 0.8
  LFP saturation start [1. 1. 1.] [17.1284 19.706  21.3104]
  LFP saturation stop [0. 0. 0.] [17.7072 20.7936 22.99  ]
  spike saturation start [1. 1. 1.] [20.79352447 34.98888041 50.98364766]
  spike saturation stop [0. 0. 0.] [21.49329554 35.48871689 51.58345143]
 stim {'passive_10kHz': ((36,), array([2., 2., 2., 1.])), 'passive_1kHz': ((61,), array([3. , 0.5, 0.3, 0.3])), 'passive_2kHz': ((49,), array([0.3, 2. , 3. , 1. ])), 'passive_5kHz': ((42,), array([0.3, 0.3, 0.1, 2. ])), 'passive_bluenoise': ((53,), array([1. , 0.3, 0.1, 0.3])), 'passive_brownnoise': ((54,), array([0.1, 0.3, 0.3, 2. ]))}
 trials ['Block', 'id', 'sound', 'sound_amp', 'sound_bluenoise', 'sound_freq', 'sound_puretone', 'start_time', 'stop_time'] 295
 Block runs 1 [1.]
249939 q0 pct [ 0.   2.  32.5] q1 [0.    0.017 0.323] frac q0<0.1 0.32 q1<0.1 0.8
  LFP saturation start [1. 1. 1.] [64.248  67.1252 68.9092]
  LFP saturation stop [0. 0. 0.] [64.6016 67.2544 69.1628]
  spike saturation start [1. 1. 1.] [1154.40358312 1789.89536314 3517.80111239]
  spike saturation stop [0. 0. 0.] [1155.30342988 1790.69522692 3519.00090808]
 stim {'AudStim_10kHz': ((200,), array([1., 1., 1., 1.])), 'OptogeneticSeries': ((6664,), array([0.78828793, 0.78808103, 0.78708448, 0.78765   ])), 'air_puff': ((50,), array([5., 5., 5., 5.])), 'passive_bluenoise': ((50,), array([1., 1., 1., 1.]))}
 trials ['Block', 'airpuff', 'airpuff_amp', 'airpuff_duration', 'id', 'opto_freq', 'opto_power', 'opto_pulse_duration', 'opto_pulse_ts', 'optogenetics', 'sound', 'sound_amp', 'sound_bluenoise', 'sound_freq', 'sound_puretone', 'start_time', 'stop_time'] 570
 Block runs 12 [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.]
Traceback (most recent call last):
  File "/tmp/claude-1001/q.py", line 4, in <module>
    x=[r for r in a if pat in r['path']][0]
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && sed -i "s/for pat in .*/for pat in ['PL079-20230620-probe0','708078-20231002-probe0','PL027-20190511-probe1','PL062-20200420-probe0','518804-20220228','PL066-20200514-probe0']:/" q.py && python q.py
```

```
PL079-20230620-probe0 q0 pct [ 0.  0. 12.] q1 [0.    0.    0.882] frac q0<0.1 0.51 q1<0.1 0.72
  LFP saturation start [1.] [nan]
  LFP saturation stop [0.] [nan]
  spike saturation start [1.] [nan]
  spike saturation stop [0.] [nan]
 stim {'AudStim_first': ((408,), array([3., 3., 3., 3.])), 'AudStim_second': ((408,), array([3., 3., 3., 3.])), 'valve_opening': ((117,), array([5., 5., 5., 5.]))}
 trials ['id', 'lick', 'match_mismatch', 'perf', 'sound', 'sound_amp1', 'sound_amp2', 'sound_freq1', 'sound_freq2', 'start_time', 'stop_time', 'valve'] 408
 licks 2641 0.0873005115399792
708078-20231002-probe0 q0 pct [ 0.   3.  30.3] q1 [0.    0.024 0.333] frac q0<0.1 0.32 q1<0.1 0.72
  LFP saturation start [1.] [nan]
  LFP saturation stop [0.] [nan]
  spike saturation start [1.] [nan]
  spike saturation stop [0.] [nan]
 stim {'passive_10kHz': ((236,), array([0., 0., 0., 0.]))}
 trials ['Block', 'id', 'sound', 'sound_amp', 'sound_freq', 'sound_puretone', 'start_time', 'stop_time'] 236
 Block runs 1 [0.]
PL027-20190511-probe1 q0 pct [  0.   14.  116.2] q1 [0.    0.081 0.575] frac q0<0.1 0.24 q1<0.1 0.52
  LFP saturation start [1.] [nan]
  LFP saturation stop [0.] [nan]
  spike saturation start [1.] [nan]
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/001260-le-merre-2026 && date -u
```

```
Sun Nov  1 12:42:16 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/001260-le-merre-2026/pfcki.py",
 "content": "\"\"\"Loading and measures for dandiset 001260 (dataset KI of Le Merre, Heining et al., 2026).\n\nLe Merre, Heining et al., \"A prefrontal cortex map based on single-neuron activity\",\nNature Neuroscience, doi:10.1038/s41593-025-02190-z. Claims file:\nclaims/001260/10.1038-s41593-025-02190-z.yaml (\"claims header\" below). The paper's code is\nhttps://github.com/hejDMC/pfcmap at commit 9ae52eddc47fbb590ef4e1b1949507334707a0f1 (\"code\").\n\nWhere each parameter comes from:\n\n- Spontaneous epochs, [onset - 3 s, onset]: Methods, Epoch selection. Which stimulus series give\n  the onsets per behavioral setting (all stimuli in Passive, the 10-kHz tone in Context,\n  Detection and Opto, tone and blue noise in Aversion, trial starts in the working-memory\n  setting the code calls \"Attention\"): code, extract_prepost_quietactive.py, stimdict.\n- Epochs overlapping licking or spike-band saturation are dropped: Methods, Epoch selection.\n  Licking is read from LickOnset/LickOffset in the files; saturation from the \"spike saturation\n  start/stop\" series.\n- Sleep-like periods: Methods, Detection of sleep-like periods (10-ms bins of all cortical\n  spikes, Savitzky-Golay 11 points order 3, troughs below 0.2 of the geometric mean for longer\n  than 5 ms, extended to the geometric mean, merged within 1.5 s, padded by 1 s around merged\n  and 0.3 s around single off periods). The geometric mean is taken over the bins with a\n  positive smoothed rate (assumption: the geometric mean of a vector with zeros is zero, which\n  would make the threshold meaningless). The probe whose cortical units are used for a probe\n  without enough of them is the code's table (config/datatables/allrecs_allprobes.xlsx,\n  quietdet_src, \"from-other\"); hippocampal recordings are not checked (\"ignore\" in that table).\n  Active epochs lie at least 1 s from a sleep-like period (Methods; code active_buff = [-1, 1]);\n  sleep-like epochs overlap one.\n- Per-epoch metrics: log10 FR of the count over 3 s, B and M from ISIs (Methods, equations 2\n  and 3), B and M only in epochs with at least 6 spikes; units need at least 12 such active\n  epochs; log10 FR averaged over epochs with at least one spike (claims header, from the code).\n  The s.d. of ISIs is the population s.d. (ddof 0, numpy's default, as in the code's\n  interval_fns): a standard choice.\n- Region and layer from the location of the unit's electrode, split at the first digit (code,\n  settings.py decompose_area_layer); PFC subregions and parent regions as code settings.py\n  (pfc_set, parent_dict). Deep layers: a layer label containing 5 or 6 (claims header).\n- Waveform classes: Peak_to_Trough < 0.38 ms nw, > 0.43 ms ww (Methods, Waveform\n  classification).\n- SOM: hexagonal grid, shape from the ratio of the two largest eigenvalues of the feature\n  covariance, linear PCA initialization, batch training for 200 iterations with Gaussian\n  neighborhood exp(-d^2/sigma^2), sigma decaying from the largest to the smallest node distance\n  (Methods, SOM analysis; code utils/som_helpers.py get_kshape, getInitialMap_pca and\n  utils/my_somz.py, batch branch). Deterministic, so no seed.\n- Categories: Ward linkage of node prototypes standardized across nodes (Methods, Hierarchical\n  clustering analyses), cut at 8 (ww) or 5 (nw) clusters (code settings.py nclust_dict).\n- E-scores: Methods, Enrichment statistics, equation 5, shuffling the population labels within\n  each group; P = 1 - max(f-, f+), significant at P < 0.05 (claims header). 1,000 shuffles.\n\"\"\"\nimport json\nimport re\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\nfrom scipy.signal import savgol_filter\n\nDANDISET = \"001260\"\nVERSION = \"0.250911.0744\"\nAPI = \"https://api.dandiarchive.org/api\"\n\nPFC_SUBREGIONS = [\"MOs\", \"ACAd\", \"ACAv\", \"PL\", \"ILA\", \"ORBm\", \"ORBvl\", \"ORBl\", \"AId\", \"AIv\", \"FRP\"]\n# code settings.py, parent_dict\nPARENT = {\n    \"PFC\": [\"MOs\", \"ACAd\", \"ACAv\", \"PL\", \"ILA\", \"FRP\", \"ACA\", \"ORBl\", \"ORBvl\", \"ORBm\", \"ORB\", \"AId\", \"AIv\"],\n    \"DP\": [\"DP\"], \"TT\": [\"TTd\", \"TTv\"], \"LS\": [\"LSr\", \"SH\", \"LSv\", \"LSc\"], \"CP\": [\"CP\"],\n    \"ACB\": [\"ACB\"], \"HPF\": [\"CA1\", \"CA2\", \"CA3\", \"DG-mo\", \"DG-po\", \"DG-sg\", \"HPF\"], \"MO\": [\"MOp\"],\n    \"AON\": [\"AON\"], \"PIR\": [\"PIR\"],\n    \"SS\": [\"SSp-bfd\", \"SSp-m\", \"SSs\", \"SSp-tr\", \"SSp-n\", \"SSp-ul\", \"SSp-ll\", \"SSp-un\"],\n    \"VIS\": [\"VISa\", \"VISal\", \"VISli\", \"VISp\", \"VISpm\", \"VISam\", \"VISpor\", \"VISpl\", \"VISl\", \"VISrl\"],\n    \"AUD\": [\"AUDpo\", \"AUDd\", \"AUDp\"], \"EPd\": [\"EPd\"],\n    \"TH\": [\"RT\", \"VPM\", \"LP\", \"LGv\", \"LD\", \"VPL\", \"Eth\", \"PO\", \"LGd-co\"],\n}\nAREA2PARENT = {a: p for p, areas in PARENT.items() for a in areas}\n# isocortical areas, whose spikes enter the sleep-like detection (\"all cortical spikes\")\nCORTICAL = set(PARENT[\"PFC\"] + PARENT[\"MO\"] + PARENT[\"SS\"] + PARENT[\"VIS\"] + PARENT[\"AUD\"]) | {\n    \"MOs\", \"SSp\", \"AUDv\", \"VISC\", \"GU\", \"AIp\", \"RSPv\", \"RSPd\", \"RSPagl\", \"PTLp\", \"TEa\", \"ECT\", \"PERI\"}\nNUMBERED = {\"CA1\", \"CA2\", \"CA3\"}\n\n# code, config/datatables/allrecs_allprobes.xlsx, column quietdet_src: probes whose sleep-like\n# periods are taken from another probe of the same session, and probes not checked.\nQUIET_FROM_OTHER = {\n    \"PL062_20200420-probe0\": \"probe1\", \"PL064_20200422-probe0\": \"probe1\",\n    \"PL079_20230621-probe1\": \"probe0\", \"PL081_20230621-probe1\": \"probe0\",\n    \"PL082_20230912-probe0\": \"probe1\", \"PL027_20190511-probe1\": \"probe0\",\n    \"PL028_20190517-probe1\": \"probe0\", \"PL030_20190518-probe1\": \"probe0\",\n    \"PL031_20190524-probe1\": \"probe0\", \"PL032_20190524-probe1\": \"probe0\",\n    \"PL051_20191121-probe1\": \"probe0\", \"PL062_20200420-probe2\": \"probe1\",\n    \"PL055_20200302-probe1\": \"probe0\", \"PL056_20200303-probe1\": \"probe0\",\n    \"PL057_20200203-probe1\": \"probe0\", \"PL080_20230621-probe1\": \"probe0\",\n    \"PL081_20230620-probe1\": \"probe0\", \"PL082_20230911-probe1\": \"probe0\",\n}\nQUIET_IGNORE = {\"711179_20230907-probe0\", \"708078_20231002-probe0\", \"708078_20231002-probe1\",\n                \"708078_20231003-probe0\"}\n\nEPOCH = 3.0          # s, Methods\nMIN_SPIKES = 6       # Methods\nMIN_EPOCHS = 12      # Methods\nNW_MAX, WW_MIN = 0.38, 0.43  # ms, Methods\n\n\ndef dec(v):\n    return v.decode() if isinstance(v, bytes) else v\n\n\ndef list_assets():\n    url = f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200\"\n    out = []\n    while url:\n        r = requests.get(url).json()\n        out += r[\"results\"]\n        url = r[\"next\"]\n    return out\n\n\ndef version_metadata():\n    return requests.get(f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/\").json()\n\n\ndef s3_url(asset_id):\n    return requests.head(f\"{API}/assets/{asset_id}/download/\", allow_redirects=True).url\n\n\ndef open_asset(asset_id):\n    return h5py.File(remfile.File(s3_url(asset_id)), \"r\")\n\n\ndef split_area_layer(loc):\n    \"\"\"code settings.py decompose_area_layer\"\"\"\n    m = re.search(r\"\\d\", loc)\n    if loc in NUMBERED or m is None:\n        return loc, \"NA\"\n    return loc[: m.start()], loc[m.start():]\n\n\ndef setting_from_metadata(desc, keywords):\n    \"\"\"Behavioral setting from the session description and keywords, named as the code names it.\"\"\"\n    d = desc.lower()\n    if \"aversive\" in d:\n        return \"Aversion\"\n    if \"detection\" in d:\n        return \"Detection\"\n    if \"contextual\" in d:\n        return \"Context\"\n    if \"working memory\" in d:\n        return \"Attention\"\n    if \"Optotagging\" in keywords:\n        return \"Opto\"\n    return \"Passive\"\n\n\nSTIMS = {\"Context\": [\"AudStim_10kHz\"], \"Opto\": [\"AudStim_10kHz\"], \"Detection\": [\"AudStim_10kHz\"],\n         \"Aversion\": [\"AudStim_10kHz\", \"passive_bluenoise\"]}\n\n\ndef onset_times(f, setting):\n    pres = f[\"stimulus/presentation\"]\n    if setting == \"Attention\":\n        return np.sort(f[\"intervals/trials/start_time\"][:])\n    names = list(pres.keys()) if setting == \"Passive\" else [n for n in STIMS[setting] if n in pres]\n    return np.sort(np.concatenate([pres[n][\"timestamps\"][:] for n in names]))\n\n\ndef tone_times(f):\n    \"\"\"10-kHz tone onsets (Methods: 10-kHz pure tones), None when a file has no such series.\"\"\"\n    pres = f[\"stimulus/presentation\"]\n    for n in [\"AudStim_10kHz\", \"passive_10kHz\"]:\n        if n in pres:\n            return np.sort(pres[n][\"timestamps\"][:])\n    return None\n\n\ndef intervals(f, start, stop):\n    if start not in f or stop not in f:\n        return np.empty((0, 2))\n    a, b = f[start][\"timestamps\"][:], f[stop][\"timestamps\"][:]\n    ok = np.isfinite(a) & np.isfinite(b)\n    return np.c_[a[ok], b[ok]]\n\n\ndef overlaps(ep, iv, pad=0.0):\n    \"\"\"for each epoch [s, e], whether it overlaps any interval of iv widened by pad.\"\"\"\n    if len(iv) == 0:\n        return np.zeros(len(ep), bool)\n    iv = iv[np.argsort(iv[:, 0])]\n    lo, hi = iv[:, 0] - pad, iv[:, 1] + pad\n    cmax = np.maximum.accumulate(hi)\n    k = np.searchsorted(lo, ep[:, 1], side=\"left\") - 1  # last interval starting before epoch end\n    out = np.zeros(len(ep), bool)\n    ok = k >= 0\n    out[ok] = cmax[k[ok]] > ep[ok, 0]\n    return out\n\n\ndef epoch_metrics(st, idx_end, ep):\n    \"\"\"Per unit and epoch: spike count, burstiness B and memory M (NaN below 6 spikes).\n\n    st: concatenated spike times, idx_end: spike_times_index, ep: (n, 2) epochs.\"\"\"\n    nu, ne = len(idx_end), len(ep)\n    cnt = np.zeros((nu, ne), np.int32)\n    B = np.full((nu, ne), np.nan, np.float32)\n    M = np.full((nu, ne), np.nan, np.float32)\n    start = 0\n    for u in range(nu):\n        s = np.sort(st[start: idx_end[u]])\n        start = idx_end[u]\n        i0 = np.searchsorted(s, ep[:, 0])\n        i1 = np.searchsorted(s, ep[:, 1])\n        n = i1 - i0\n        cnt[u] = n\n        if len(s) < 2:\n            continue\n        isi = np.diff(s)\n        c1 = np.r_[0, np.cumsum(isi)]\n        c2 = np.r_[0, np.cumsum(isi ** 2)]\n        x, y = isi[:-1], isi[1:]\n        cx, cy = np.r_[0, np.cumsum(x)], np.r_[0, np.cumsum(y)]\n        cxx, cyy, cxy = np.r_[0, np.cumsum(x * x)], np.r_[0, np.cumsum(y * y)], np.r_[0, np.cumsum(x * y)]\n        ok = n >= MIN_SPIKES\n        a, b = i0[ok], i1[ok] - 1          # ISIs a .. b-1 lie inside the epoch\n        k = (b - a).astype(float)\n        mu = (c1[b] - c1[a]) / k\n        sd = np.sqrt(np.maximum((c2[b] - c2[a]) / k - mu ** 2, 0))\n        B[u, ok] = (sd - mu) / (sd + mu)\n        pb = b - 1                         # pairs a .. b-2\n        kp = (pb - a).astype(float)\n        sx, sy = cx[pb] - cx[a], cy[pb] - cy[a]\n        sxx, syy, sxy = cxx[pb] - cxx[a], cyy[pb] - cyy[a], cxy[pb] - cxy[a]\n        cov = sxy / kp - sx * sy / kp ** 2\n        vx, vy = sxx / kp - (sx / kp) ** 2, syy / kp - (sy / kp) ** 2\n        with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n            r = cov / np.sqrt(vx * vy)\n        r[(vx <= 1e-15) | (vy <= 1e-15)] = np.nan\n        M[u, ok] = r\n    return cnt, B, M\n\n\ndef offperiod_sleep(st_cortical, n_units, t0, t1, binw=0.01):\n    \"\"\"Sleep-like periods from the pooled spikes of cortical units (Methods).\"\"\"\n    if n_units == 0 or len(st_cortical) == 0:\n        return np.empty((0, 2))\n    edges = np.arange(t0, t1 + binw, binw)\n    fr = np.histogram(st_cortical, edges)[0] / n_units / binw\n    frs = savgol_filter(fr.astype(float), 11, 3)\n    pos = frs[frs > 0]\n    gmean = np.exp(np.mean(np.log(pos)))\n    thr = 0.2 * gmean\n    below = frs < thr\n    # troughs: runs below thr longer than 5 ms (any run of >= 1 bin of 10 ms)\n    above_g = frs >= gmean\n    offs = []\n    d = np.diff(np.r_[0, below.astype(int), 0])\n    for a, b in zip(np.where(d == 1)[0], np.where(d == -1)[0]):\n        # extend to where FR reaches the geometric mean\n        lo = a\n        while lo > 0 and not above_g[lo - 1]:\n            lo -= 1\n        hi = b\n        while hi < len(frs) and not above_g[hi]:\n            hi += 1\n        offs.append((edges[lo], edges[hi]))\n    if not offs:\n        return np.empty((0, 2))\n    offs = np.array(sorted(set(offs)))\n    # merge off periods closer than 1.5 s\n    groups = [[offs[0][0], offs[0][1], 1]]\n    for a, b in offs[1:]:\n        if a - groups[-1][1] < 1.5:\n            groups[-1][1] = max(groups[-1][1], b)\n            groups[-1][2] += 1\n        else:\n            groups.append([a, b, 1])\n    out = np.array([[a - (1.0 if n > 1 else 0.3), b + (1.0 if n > 1 else 0.3)] for a, b, n in groups])\n    # merge overlapping padded periods\n    res = [list(out[0])]\n    for a, b in out[1:]:\n        if a <= res[-1][1]:\n            res[-1][1] = max(res[-1][1], b)\n        else:\n            res.append([a, b])\n    return np.array(res)\n\n\ndef blocks_for(f, onsets):\n    \"\"\"Block index of each epoch (Methods, Stability analyses). Inherent blocks are runs of the\n    trials table's Block column, matched to each onset by the nearest trial start; runs of more\n    than 75 epochs are split in two. When the column is constant or alternates (median run below\n    20 epochs) the epochs are cut into consecutive blocks of 50. Assumption, see the notebook.\"\"\"\n    tr = f[\"intervals/trials\"]\n    blk = None\n    if \"Block\" in tr:\n        bv = tr[\"Block\"][:].astype(float)\n        ts = tr[\"start_time\"][:]\n        j = np.clip(np.searchsorted(ts, onsets), 1, len(ts) - 1)\n        j = np.where(np.abs(ts[j - 1] - onsets) < np.abs(ts[j] - onsets), j - 1, j)\n        v = bv[j]\n        run = np.r_[0, np.cumsum(np.diff(v) != 0)]\n        lens = np.bincount(run)\n        if len(lens) > 1 and np.median(lens) >= 20:\n            blk = []\n            nb = 0\n            for r in range(len(lens)):\n                n = lens[r]\n                if n > 75:\n                    h = n // 2\n                    blk += [nb] * h + [nb + 1] * (n - h)\n                    nb += 2\n                else:\n                    blk += [nb] * n\n                    nb += 1\n            return np.array(blk), \"inherent\"\n    return np.arange(len(onsets)) // 50, \"fifty\"\n\n\ndef load_file(asset):\n    \"\"\"Read one NWB file and reduce it to what the analyses use.\"\"\"\n    f = open_asset(asset[\"asset_id\"])\n    sess = dec(f[\"general/session_id\"][()])\n    desc = dec(f[\"session_description\"][()])\n    kw = [dec(k) for k in f[\"general/keywords\"][:]]\n    setting = setting_from_metadata(desc, kw)\n    subj = dec(f[\"general/subject/subject_id\"][()]).split(\"_\")[0]\n    e = f[\"general/extracellular_ephys/electrodes\"]\n    loc = np.array([dec(x) for x in e[\"location\"][:]])\n    ap, dv, ml = e[\"AP\"][:], e[\"DV\"][:], e[\"ML\"][:]\n    u = f[\"units\"]\n    el = u[\"electrodes\"][:]\n    q = u[\"quality\"][:]\n    units = pd.DataFrame({\n        \"session\": sess, \"subject\": subj, \"setting\": setting, \"unit_id\": u[\"id\"][:],\n        \"ptt\": u[\"Peak_to_Trough\"][:], \"location\": loc[el], \"AP\": ap[el], \"DV\": dv[el], \"ML\": ml[el],\n        \"q_isi\": q[:, 0], \"q_fp\": q[:, 1],\n    })\n    al = units.location.map(split_area_layer)\n    units[\"area\"] = [a for a, _ in al]\n    units[\"layer\"] = [l for _, l in al]\n    st = u[\"spike_times\"][:]\n    idx = u[\"spike_times_index\"][:].astype(np.int64)\n    units[\"n_spikes\"] = np.diff(np.r_[0, idx])\n    t0, t1 = float(np.nanmin(st)), float(np.nanmax(st))\n    onsets = onset_times(f, setting)\n    ep = np.c_[onsets - EPOCH, onsets]\n    lick = intervals(f, \"processing/behavior/LickOnset/lick_onset_data\",\n                     \"processing/behavior/LickOffset/lick_offset_data\")\n    sat = intervals(f, \"analysis/spike saturation start\", \"analysis/spike saturation stop\")\n    cnt, B, M = epoch_metrics(st, idx, ep)\n    # cortical spikes for the sleep-like detection\n    cort = units.area.isin(CORTICAL).values\n    starts = np.r_[0, idx[:-1]]\n    cst = np.concatenate([st[a:b] for a, b, c in zip(starts, idx, cort) if c]) if cort.any() else np.empty(0)\n    sleep = offperiod_sleep(np.sort(cst), int(cort.sum()), t0, t1)\n    blk, blkmode = blocks_for(f, onsets)\n    tones = tone_times(f)\n    tone_psth = None\n    if tones is not None:\n        tone_psth = tone_counts(st, idx, tones)\n    out = dict(path=asset[\"path\"], session=sess, subject=subj, setting=setting, desc=desc,\n               units=units, onsets=onsets, epochs=ep, lick=lick, sat=sat, cnt=cnt, B=B, M=M,\n               sleep_own=sleep, n_cortical=int(cort.sum()), t0=t0, t1=t1, blocks=blk,\n               blockmode=blkmode, tones=tones, tone=tone_psth,\n               n_trials=len(f[\"intervals/trials/start_time\"]))\n    f.close()\n    return out\n\n\nPSTH_BIN = 0.0005  # s, Methods (0.5 ms)\nPRE, POST = 2.0, 0.7\n\n\ndef tone_counts(st, idx, tones):\n    \"\"\"Spike times relative to each tone, as per-unit histograms of 0.5-ms bins over [-2, 0.7] s,\n    one row per tone epoch kept as a sparse list (unit, tone, bin).\"\"\"\n    edges = np.arange(-PRE, POST + PSTH_BIN / 2, PSTH_BIN)\n    nb = len(edges) - 1\n    out = []\n    start = 0\n    for u in range(len(idx)):\n        s = np.sort(st[start: idx[u]])\n        start = idx[u]\n        i0 = np.searchsorted(s, tones - PRE)\n        i1 = np.searchsorted(s, tones + POST)\n        rows = []\n        for k in range(len(tones)):\n            if i1[k] > i0[k]:\n                b = ((s[i0[k]:i1[k]] - tones[k] + PRE) / PSTH_BIN).astype(int)\n                b = b[(b >= 0) & (b < nb)]\n                rows.append(np.c_[np.full(len(b), k), b])\n        out.append(np.vstack(rows).astype(np.int32) if rows else np.empty((0, 2), np.int32))\n    return out\n\n\ndef load_all(assets, workers=12):\n    with ThreadPoolExecutor(workers) as ex:\n        recs = list(ex.map(load_file, assets))\n    return sorted(recs, key=lambda r: r[\"path\"])\n\n\ndef classify_epochs(recs):\n    \"\"\"Adds to each record its sleep-like periods (own or from the probe the code's table names)\n    and the epoch states: 'active', 'sleep', or 'excluded' (licking or saturation).\"\"\"\n    by_sess = {r[\"session\"]: r for r in recs}\n    for r in recs:\n        sid = r[\"session\"]\n        if sid in QUIET_IGNORE:\n            r[\"sleep\"] = None\n        elif sid in QUIET_FROM_OTHER:\n            other = sid.rsplit(\"-\", 1)[0] + \"-\" + QUIET_FROM_OTHER[sid]\n            r[\"sleep\"] = by_sess[other][\"sleep_own\"] if other in by_sess else r[\"sleep_own\"]\n        else:\n            r[\"sleep\"] = r[\"sleep_own\"]\n        ep = r[\"epochs\"]\n        bad = overlaps(ep, r[\"lick\"]) | overlaps(ep, r[\"sat\"])\n        if r[\"sleep\"] is None or len(r[\"sleep\"]) == 0:\n            sl = np.zeros(len(ep), bool)\n            near = np.zeros(len(ep), bool)\n        else:\n            sl = overlaps(ep, r[\"sleep\"])\n            near = overlaps(ep, r[\"sleep\"], pad=1.0)\n        state = np.where(bad, \"excluded\", np.where(sl, \"sleep\", np.where(near, \"near_sleep\", \"active\")))\n        r[\"state\"] = state\n    return recs\n\n\ndef unit_metrics(r, mask):\n    \"\"\"Mean metrics over the epochs in mask; returns DataFrame with n_valid (epochs >= 6 spikes).\"\"\"\n    cnt, B, M = r[\"cnt\"][:, mask], r[\"B\"][:, mask], r[\"M\"][:, mask]\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        lfr = np.where(cnt > 0, np.log10(cnt / EPOCH), np.nan)\n        out = pd.DataFrame({\n            \"log10FR\": np.nanmean(lfr, axis=1) if lfr.shape[1] else np.nan,\n            \"B\": np.nanmean(B, axis=1) if B.shape[1] else np.nan,\n            \"M\": np.nanmean(M, axis=1) if M.shape[1] else np.nan,\n            \"n_valid\": (cnt >= MIN_SPIKES).sum(axis=1),\n            \"n_epochs\": mask.sum(),\n        })\n    return out\n\n\ndef unit_table(recs):\n    rows = []\n    for r in recs:\n        u = r[\"units\"].copy()\n        act = unit_metrics(r, r[\"state\"] == \"active\")\n        slp = unit_metrics(r, r[\"state\"] == \"sleep\")\n        for c in act:\n            u[c] = act[c].values\n            u[c + \"_sleep\"] = slp[c].values\n        rows.append(u)\n    U = pd.concat(rows, ignore_index=True)\n    U[\"utype\"] = np.where(U.ptt < NW_MAX, \"nw\", np.where(U.ptt > WW_MIN, \"ww\", \"na\"))\n    U[\"parent\"] = U.area.map(AREA2PARENT).fillna(\"other\")\n    U[\"is_pfc\"] = U.area.isin(PFC_SUBREGIONS)\n    U[\"deep\"] = U.layer.str.contains(\"5|6\")\n    U[\"cortical\"] = U.area.isin(CORTICAL)\n    # region unit for enrichment: PFC subregions, other areas by parent (code parent_dict)\n    U[\"region\"] = np.where(U.is_pfc, U.area, U.parent)\n    return U\n\n\n# ---------------------------------------------------------------- SOM\ndef hex_coords(nx, ny):\n    \"\"\"code utils/my_somz.py geometry('hex'): node k = jj*nx + ii.\"\"\"\n    dy = 0.8660254\n    xs, ys = [], []\n    for jj in range(ny):\n        for ii in range(nx):\n            xs.append(ii + (0.5 if jj % 2 == 1 else 0.0))\n            ys.append(jj * dy)\n    return np.c_[xs, ys]\n\n\ndef kshape(X, nnodes):\n    \"\"\"code utils/som_helpers.py get_kshape\"\"\"\n    ev = np.sort(np.linalg.eigvalsh(np.cov(X.T)))\n    er = ev[-2] / ev[-1]\n    x = np.sqrt(nnodes / er)\n    return int(np.ceil(x * er)), int(np.ceil(x))\n\n\ndef pca_init(X, rows, cols):\n    \"\"\"code utils/som_helpers.py getInitialMap_pca (exact PCA in place of randomized PCA).\"\"\"\n    n = rows * cols\n    coord = np.c_[np.arange(n) // cols, np.arange(n) % cols].astype(float)\n    coord = (coord - coord.min(0)) / (coord.max(0) - coord.min(0))\n    coord = (coord - 0.5) * 2\n    me = X.mean(0)\n    Xc = X - me\n    w, V = np.linalg.eigh(np.cov(Xc.T))\n    order = np.argsort(w)[::-1][:2]\n    eigvec = V[:, order].T * w[order][:, None]  # unit eigenvectors scaled by eigenvalue\n    return me + coord @ eigvec  # (n, d)\n\n\ndef train_som(X, nnodes, niter=200):\n    \"\"\"Batch SOM as code utils/my_somz.py (batch branch). X standardized (n, d).\"\"\"\n    nx, ny = kshape(X, nnodes)\n    pos = hex_coords(nx, ny)\n    D = np.sqrt(((pos[:, None, :] - pos[None, :, :]) ** 2).sum(-1))\n    W = pca_init(X, ny, nx)\n    s0, sf = D.max(), D[D > 0].min()\n    for it in range(niter):\n        sigma = s0 * (sf / s0) ** (it / niter)\n        bmu = bmus(X, W)\n        H = np.exp(-(D[bmu] ** 2) / sigma ** 2)  # (n, nodes)\n        W = (H.T @ X) / H.sum(0)[:, None]\n    return dict(W=W, pos=pos, shape=(nx, ny), D=D)\n\n\ndef bmus(X, W):\n    d = (X ** 2).sum(1)[:, None] - 2 * X @ W.T + (W ** 2).sum(1)[None, :]\n    return np.argmin(d, axis=1)\n\n\ndef ward_clusters(W, k):\n    from scipy.cluster.hierarchy import fcluster, linkage\n    Z = (W - W.mean(0)) / W.std(0)\n    return fcluster(linkage(Z, method=\"ward\"), k, \"maxclust\") - 1\n\n\n# ---------------------------------------------------------------- enrichment\ndef escore(pop, attr, group, n_shuffle=1000, seed=0, pops=None, attrs=None):\n    \"\"\"E-scores (Methods, equation 5): counts of attribute in population against counts after\n    shuffling the population labels within each group. Returns E, P, counts (pops x attrs).\"\"\"\n    rng = np.random.default_rng(seed)\n    pops = np.array(sorted(pd.unique(pop))) if pops is None else np.asarray(pops)\n    attrs = np.array(sorted(pd.unique(attr))) if attrs is None else np.asarray(attrs)\n    pi = pd.Index(pops).get_indexer(pop)\n    ai = pd.Index(attrs).get_indexer(attr)\n    keep = (pi >= 0) & (ai >= 0)\n    pi, ai, g = pi[keep], ai[keep], np.asarray(group)[keep]\n    npop, nat = len(pops), len(attrs)\n    X = np.bincount(pi * nat + ai, minlength=npop * nat).reshape(npop, nat)\n    gidx = [np.where(g == gv)[0] for gv in pd.unique(g)]\n    S = np.zeros((n_shuffle, npop, nat), np.int32)\n    for s in range(n_shuffle):\n        pp = pi.copy()\n        for ix in gidx:\n            pp[ix] = pp[ix][rng.permutation(len(ix))]\n        S[s] = np.bincount(pp * nat + ai, minlength=npop * nat).reshape(npop, nat)\n    mu, sd = S.mean(0), S.std(0)\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        E = (X - mu) / sd\n    fm, fp = (S < X[None]).mean(0), (S > X[None]).mean(0)\n    P = 1 - np.maximum(fm, fp)\n    return (pd.DataFrame(E, pops, attrs), pd.DataFrame(P, pops, attrs), pd.DataFrame(X, pops, attrs))\n"
}
```

```
File created successfully at: entries/001260-le-merre-2026/pfcki.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/001260-le-merre-2026 && python - <<'EOF'
p='pfcki.py'; s=open(p).read()
old=s[s.index("    offs = []\n    d = np.diff"):s.index("    offs = np.array(sorted(set(offs)))")]
new='''    d = np.diff(np.r_[0, below.astype(int), 0])
    a_idx, b_idx = np.where(d == 1)[0], np.where(d == -1)[0]
    if len(a_idx) == 0:
        return np.empty((0, 2))
    # extend each trough backward and forward to where FR reaches the geometric mean
    n = len(frs)
    ii = np.arange(n)
    last_above = np.maximum.accumulate(np.where(above_g, ii, -1))
    next_above = np.minimum.accumulate(np.where(above_g, ii, n)[::-1])[::-1]
    lo = last_above[a_idx] + 1
    hi = next_above[np.minimum(b_idx, n - 1)]
    hi = np.where(b_idx >= n, n, hi)
    offs = list(zip(edges[lo], edges[np.minimum(hi, n)]))
'''
s=s.replace(old,new)
s=s.replace('''    tones = tone_times(f)
    tone_psth = None
    if tones is not None:
        tone_psth = tone_counts(st, idx, tones)
''','''    tones = tone_times(f)
''').replace("blockmode=blkmode, tones=tones, tone=tone_psth,","blockmode=blkmode, tones=tones, asset_id=asset[\"asset_id\"],")
open(p,'w').write(s)
EOF
grep -n "tone_psth\|offs = list" pfcki.py
```

```
263:    offs = list(zip(edges[lo], edges[np.minimum(hi, n)]))
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import time, numpy as np, pfcki as P
A=P.list_assets(); print(len(A))
sub=[a for a in A if 'PL062-20200420' in a['path']]
t=time.time(); recs=P.load_all(sub, workers=3); print('load', time.time()-t)
recs=P.classify_epochs(recs)
for r in recs:
    print(r['session'], r['setting'], len(r['onsets']), r['n_cortical'], len(r['sleep_own']), np.unique(r['state'],return_counts=True), r['blockmode'], np.bincount(r['blocks']))
    sl=r['sleep']; 
    if sl is not None and len(sl): print(' sleep frac', (sl[:,1]-sl[:,0]).sum()/(r['t1']-r['t0']))
U=P.unit_table(recs)
print(U.groupby('session').size()); print(U.utype.value_counts()); print((U.n_valid>=12).sum())
print(U[['log10FR','B','M']].describe())
print(U.region.value_counts().head(20))
EOF
```

```
entries/001260-le-merre-2026/pfcki.py:428: RuntimeWarning: Mean of empty slice
  "B": np.nanmean(B, axis=1) if B.shape[1] else np.nan,
entries/001260-le-merre-2026/pfcki.py:429: RuntimeWarning: Mean of empty slice
  "M": np.nanmean(M, axis=1) if M.shape[1] else np.nan,
74
load 12.220765590667725
PL062_20200420-probe0 Context 443 236 59 (array(['active', 'excluded', 'near_sleep', 'sleep'], dtype='<U10'), array([287, 111,  11,  34])) inherent [61 32 65 55 73 44 54 55  4]
 sleep frac 0.05899339155901158
PL062_20200420-probe1 Context 443 139 165 (array(['active', 'excluded', 'near_sleep', 'sleep'], dtype='<U10'), array([287, 111,  11,  34])) inherent [61 32 65 55 73 44 54 55  4]
 sleep frac 0.058993124063621026
PL062_20200420-probe2 Context 443 0 0 (array(['active', 'excluded', 'near_sleep', 'sleep'], dtype='<U10'), array([287, 111,  11,  34])) inherent [61 32 65 55 73 44 54 55  4]
 sleep frac 0.05899317569248165
session
PL062_20200420-probe0    394
PL062_20200420-probe1    422
PL062_20200420-probe2    124
dtype: int64
utype
ww    748
nw    162
[... 28 more lines not kept]
```

**Agent**

Two-file test works (12 s for 3 files). Loading all 74 files now and saving a dev cache.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warning | grep -v nanmean
import time, pickle, numpy as np, pfcki as P
A=P.list_assets()
t=time.time(); recs=P.load_all(A, workers=16); print('load', time.time()-t)
pickle.dump(recs, open('/tmp/claude-1001/recs.pkl','wb'))
EOF
ls -la $TMPDIR/recs.pkl
```

```
load 210.7033941745758
-rw-r--r-- 1 runner runner 91943509 Nov  1 12:47 /tmp/claude-1001/recs.pkl
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF' 2>&1 | grep -v "Warning\|nanmean\|np.nan"
import pickle, numpy as np, pandas as pd, pfcki as P
recs=pickle.load(open('/tmp/claude-1001/recs.pkl','rb'))
recs=P.classify_epochs(recs)
U=P.unit_table(recs)
print(len(U))
print(U[U.region=='other'].area.value_counts().to_string())
print(U.area.value_counts().to_string())
EOF
```

```
20374
area
OLF             1326
STR              657
fa               439
aco              214
or               139
ccg              123
VL               104
alv               87
ccb               75
cing              67
GPe               39
root              28
scwm              28
fiber tracts      27
GU                24
ccs               23
IG                23
TEa               20
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF' 2>&1 | grep -v "Warning\|nanmean\|np.nan"
import pickle, numpy as np, pandas as pd, pfcki as P
recs=pickle.load(open('/tmp/claude-1001/recs.pkl','rb'))
recs=P.classify_epochs(recs)
U=P.unit_table(recs)
ok12=U.n_valid>=12
for name,q in [('all',np.ones(len(U),bool)),('q_isi<0.1',U.q_isi<0.1),('q_fp<0.1',U.q_fp<0.1)]:
    s=U[q&ok12]; print(name, (q).sum(), (q&ok12).sum(), 'pfc%', round(100*s.is_pfc.mean(),1), s.utype.value_counts().to_dict())
st=pd.DataFrame([dict(s=r['session'],set=r['setting'],act=(r['state']=='active').sum(),sl=(r['state']=='sleep').sum(),ex=(r['state']=='excluded').sum(),nb=(r['state']=='near_sleep').sum(), frac=(0 if r['sleep'] is None or len(r['sleep'])==0 else (r['sleep'][:,1]-r['sleep'][:,0]).sum()/(r['t1']-r['t0'])), ncort=r['n_cortical'], bm=r['blockmode'], nblk=len(np.unique(r['blocks']))) for r in recs])
print(st.to_string()); print(st[['act','sl','frac','nblk']].describe())
EOF
```

```
all 20374 14564 pfc% 48.4 {'ww': 11209, 'nw': 2752, 'na': 603}
q_isi<0.1 7331 3781 pfc% 50.6 {'ww': 3087, 'nw': 542, 'na': 152}
q_fp<0.1 14010 10008 pfc% 47.1 {'ww': 7508, 'nw': 2070, 'na': 430}
                         s        set  act   sl   ex  nb      frac  ncort        bm  nblk
0   242820_20200526-probe0   Aversion   32  211    0   7  0.554207    219  inherent     5
1   249939_20200611-probe0   Aversion  122  106    1  21  0.182398    161  inherent     5
2   249940_20200610-probe0   Aversion   73  163    0  14  0.342107    165  inherent     5
3   250252_20200609-probe0   Aversion    0  248    0   2  0.947881     59  inherent     5
4   250253_20200609-probe0   Aversion  121  107    0  22  0.246316    241  inherent     5
5   250256_20200610-probe0   Aversion   16  320    0  14  0.752721    108  inherent     5
6   518804_20220228-probe0  Detection  138   90   27  19  0.147285     97     fifty     6
7   518804_20220301-probe0  Detection  175   84   30  19  0.133848    323     fifty     7
8   534133_20220302-probe0  Detection   82   60   25  13  0.145898    140     fifty     4
9   560169_20220506-probe0  Detection   26  248   23   5  0.618054    207     fifty     7
10  560171_20220504-probe0  Detection   73  127   27  19  0.315225     47     fifty     5
11  560171_20220505-probe0  Detection   39  169   15  12  0.555000     85     fifty     5
12  708078_20231002-probe0    Passive  236    0    0   0  0.000000     37     fifty     5
13  708078_20231002-probe1    Passive  236    0    0   0  0.000000     10     fifty     5
14  708078_20231003-probe0    Passive  308    0    0   0  0.000000     14     fifty     7
15  711179_20230907-probe0    Passive  299    0    0   0  0.000000      0     fifty     6
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap/python; ls config/config_statedet; cat config/config_statedet/* | head -80; grep -v "^\s*#" preprocessing/quiet_extraction/run_offperiod_detection.py | grep -v "^\s*$" | head -120
```

```
offdetection_defaultparams.yaml
paramfuncs_offperiod_det.py
bw: 0.01 #for rate smoothing

gauss_bw: 0.025 #seconds
savgol_params: [11,3]

mindur_trough: 0.05 #seconds
maxdur_off: 0.6 #maximal duration of off episode

ratethr_frac: 0.2
maxint_between_off_sec: 1.5 #otherwise merged into a quiet period,seconds

nmin_super: 3 #minimum number of off periods closer than maxint_between_off_sec to be considered superburst

marg_super_sec: [-1.,1] #seconds
marg_nonsuper_sec: [-0.3,0.3] #seconds

mindur_free: 1.5 #seconds

[... 129 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap/python; grep -n "def get_detdict" -A80 utils/statedet_helpers.py | head -120; grep -n "mindur_trough_pts\|maxpts_off\|minpts_free" config/config_statedet/paramfuncs_offperiod_det.py
```

```
78:def get_detdict(rvec,recdur,ratethr_frac=0.2,mindur_trough_pts=5,maxint_between_off=0,bw=0.01, \
79-                nmin_super=3, marg_super=0, marg_nonsuper=0, minpts_free=1, maxpts_off=100,print_on=False):
80-    tintpts = (np.array([0, recdur]) / bw).astype(int)
81-
82-    rate_gmean = get_zeroline(rvec)
83-    rate_thr = ratethr_frac * rate_gmean
84-
85-    troughpints0, peakamps = get_halfwaves(rvec, rate_gmean, rate_thr, mindur_pts=mindur_trough_pts, mode='trough')
86-
87-    troughpints = troughpints0[(np.diff(troughpints0) <= maxpts_off).flatten()]
88-
89-
90-    if print_on:
91-        troughtimes = troughpints*bw
92-
93-        print('off/min', troughtimes.shape[0] / recdur * 60.)
94-        print('% spent in off', np.sum(np.diff(troughtimes)) / recdur * 100)
95-
96-
97-    # superbursts
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap/python; grep -n "def get_zeroline\|def get_halfwaves\|def get_superbursts\|def get_events_per_super\|def make_bordermat" -A28 utils/statedet_helpers.py | head -170
```

```
8:def get_halfwaves(vals,rolldownthr,minpeakheight,mindur_pts=0,mode='trough'):
9-    starts0 = np.where(np.diff(np.sign(vals-rolldownthr))<0)[0]#start of a potential trough interval interval
10-    stops0 = np.where(np.diff(np.sign(vals-rolldownthr))>0)[0]#stop of a potential trough interval
11-
12-    stops = stops0[stops0>starts0[0]] #excluding the first if it is an open interval being finished
13-    starts = starts0[starts0<stops0[-1]]#excluding the last if it the interval remains to be finished
14-    #print(len(starts), len(stops))
15-    cross_ints = np.vstack([starts,stops]).T
16-    myfn,compfn = [np.min,np.less_equal] if mode == 'trough' else [np.max,np.greater_equal]
17-    peaks_temp = np.array([myfn(vals[p0:p1]) for p0,p1 in cross_ints])
18-    cond = compfn(peaks_temp,minpeakheight)
19-    cond2 = np.diff(cross_ints)[:,0] > mindur_pts
20-    return cross_ints[cond & cond2],peaks_temp[cond & cond2]
21-
22-def make_spikehist(spikes,bw,tint,**kwargs):
23-    spikebins = np.arange(tint[0],tint[1],bw)
24-    spikehist,_ = np.histogram(spikes,spikebins)
25-    spikebins_plot = spikebins[:-1] +bw*0.5
26-    if 'n_units' in kwargs:
27-        ratevec = spikehist/(bw*kwargs['n_units'])
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001260-le-merre-2026 && python - <<'EOF'
p='pfcki.py'; s=open(p).read()
add='''

def offperiod_sleep_code(st_cortical, n_units, t0, t1, binw=0.01):
    """Variant: the code's detector (utils/statedet_helpers.py get_detdict with
    config/config_statedet/offdetection_defaultparams.yaml): off periods are runs below the
    geometric mean whose minimum is at most 0.2 of it, lasting more than 50 ms (mindur_trough
    0.05 s, where the Methods say 5 ms) and at most 0.6 s (maxdur_off); merged within 1.5 s;
    groups of at least 3 off periods padded by 1 s, others by 0.3 s; free gaps of 1.5 s or less
    filled. The Savitzky-Golay output is clipped at 0."""
    if n_units == 0 or len(st_cortical) == 0:
        return np.empty((0, 2))
    edges = np.arange(0, t1, binw)
    fr = np.histogram(st_cortical, edges)[0] / n_units / binw
    v = np.clip(savgol_filter(fr.astype(float), 11, 3), 0, None)
    gm = np.exp(np.mean(np.log(v[v > 0])))
    sg = np.diff(np.sign(v - gm))
    starts0, stops0 = np.where(sg < 0)[0], np.where(sg > 0)[0]
    if len(starts0) == 0 or len(stops0) == 0:
        return np.empty((0, 2))
    stops = stops0[stops0 > starts0[0]]
    starts = starts0[starts0 < stops0[-1]]
    ci = np.c_[starts, stops]
    mins = np.array([v[a:b].min() for a, b in ci])
    dur = ci[:, 1] - ci[:, 0]
    tr = ci[(mins <= 0.2 * gm) & (dur > 5) & (dur <= 60)]
    if len(tr) == 0:
        return np.empty((0, 2))
    # merge within 1.5 s (150 points)
    gaps = tr[1:, 0] - tr[:-1, 1]
    si = np.r_[0, np.where(gaps >= 150)[0] + 1]
    ei = np.r_[np.where(gaps >= 150)[0], len(tr) - 1]
    sb = np.c_[tr[si, 0], tr[ei, 1]]
    nev = ei - si + 1
    pad = np.where(nev >= 3, 100, 30)
    bm = np.c_[sb[:, 0] - pad, sb[:, 1] + pad]
    # merge overlapping, then fill free gaps of 1.5 s or less
    res = [list(bm[0])]
    for a, b in bm[1:]:
        if a - res[-1][1] <= 150:
            res[-1][1] = max(res[-1][1], b)
        else:
            res.append([a, b])
    return np.array(res) * binw
'''
s=s.replace("\n\ndef blocks_for(", add+"\n\ndef blocks_for(",1)
s=s.replace("    sleep = offperiod_sleep(np.sort(cst), int(cort.sum()), t0, t1)\n",
 "    sleep = offperiod_sleep(np.sort(cst), int(cort.sum()), t0, t1)\n    sleep_code = offperiod_sleep_code(np.sort(cst), int(cort.sum()), t0, t1)\n")
s=s.replace("sleep_own=sleep, ","sleep_own=sleep, sleep_own_code=sleep_code, ")
open(p,'w').write(s)
EOF
. $TMPDIR/dev/bin/activate && python - <<'EOF' 2>&1 | grep -v "Warn\|nanmean"
import numpy as np, pfcki as P
A=P.list_assets()
sub=[a for a in A if any(k in a['path'] for k in ['PL028-20190517-probe0','560169','250252','PL082-20230911-probe0'])]
recs=P.load_all(sub,4)
for r in recs:
    for k in ['sleep_own','sleep_own_code']:
        sl=r[k]; print(r['session'],k, len(sl), round((sl[:,1]-sl[:,0]).sum()/(r['t1']-r['t0']),3) if len(sl) else 0, P.overlaps(r['epochs'],sl).sum() if len(sl) else 0, len(r['epochs']))
EOF
```

```
250252_20200609-probe0 sleep_own 206 0.948 248 250
250252_20200609-probe0 sleep_own_code 92 0.938 246 250
560169_20220506-probe0 sleep_own 402 0.618 268 302
560169_20220506-probe0 sleep_own_code 301 0.525 251 302
PL028_20190517-probe0 sleep_own 400 0.327 215 398
PL028_20190517-probe0 sleep_own_code 289 0.31 202 398
PL082_20230911-probe0 sleep_own 21 0.009 9 379
PL082_20230911-probe0 sleep_own_code 19 0.005 9 379
```

**Agent**

The code's detector gives nearly the same fractions, so the over-detection is not a parameter issue. Some sessions are mostly sleep-like (one is 94%). Re-loading all files with both detectors.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF' 2>&1 | grep -v "Warning\|nanmean"
import time, pickle, numpy as np, pfcki as P
A=P.list_assets()
t=time.time(); recs=P.load_all(A, workers=16); print('load', time.time()-t)
pickle.dump(recs, open('/tmp/claude-1001/recs.pkl','wb'))
EOF
date -u
```

```
load 175.42148351669312
Sun Nov  1 12:52:06 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/001260-le-merre-2026 && python - <<'EOF'
p='pfcki.py'; s=open(p).read()
s=s.replace('''def classify_epochs(recs):
    """Adds to each record its sleep-like periods (own or from the probe the code's table names)
    and the epoch states: 'active', 'sleep', or 'excluded' (licking or saturation)."""
    by_sess = {r["session"]: r for r in recs}
    for r in recs:''','''def classify_epochs(recs, detector="methods"):
    """Adds to each record its sleep-like periods (own or from the probe the code's table names)
    and the epoch states: 'active', 'sleep', 'near_sleep' (within 1 s of a sleep-like period) or
    'excluded' (licking or saturation). detector 'methods' (main) or 'code' (variant)."""
    key = "sleep_own" if detector == "methods" else "sleep_own_code"
    by_sess = {r["session"]: r for r in recs}
    for r in recs:''')
s=s.replace('''            r["sleep"] = by_sess[other]["sleep_own"] if other in by_sess else r["sleep_own"]
        else:
            r["sleep"] = r["sleep_own"]''','''            r["sleep"] = by_sess[other][key] if other in by_sess else r[key]
        else:
            r["sleep"] = r[key]''')
open(p,'w').write(s)
EOF
grep -n "key" pfcki.py | head
```

```
/bin/bash: line 1: cd: entries/001260-le-merre-2026: No such file or directory
136:def setting_from_metadata(desc, keywords):
137:    """Behavioral setting from the session description and keywords, named as the code names it."""
147:    if "Optotagging" in keywords:
160:    names = list(pres.keys()) if setting == "Passive" else [n for n in STIMS[setting] if n in pres]
363:    kw = [dec(k) for k in f["general/keywords"][:]]
436:    return sorted(recs, key=lambda r: r["path"])
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='pfcki.py'; s=open(p).read()
a='''def classify_epochs(recs):
    """Adds to each record its sleep-like periods (own or from the probe the code's table names)
    and the epoch states: 'active', 'sleep', or 'excluded' (licking or saturation)."""
    by_sess = {r["session"]: r for r in recs}
    for r in recs:'''
assert a in s
s=s.replace(a,'''def classify_epochs(recs, detector="methods"):
    """Adds to each record its sleep-like periods (own or from the probe the code's table names)
    and the epoch states: 'active', 'sleep', 'near_sleep' (within 1 s of a sleep-like period) or
    'excluded' (licking or saturation). detector 'methods' (main) or 'code' (variant)."""
    key = "sleep_own" if detector == "methods" else "sleep_own_code"
    by_sess = {r["session"]: r for r in recs}
    for r in recs:''')
b='''            r["sleep"] = by_sess[other]["sleep_own"] if other in by_sess else r["sleep_own"]
        else:
            r["sleep"] = r["sleep_own"]'''
assert b in s
s=s.replace(b,'''            r["sleep"] = by_sess[other][key] if other in by_sess else r[key]
        else:
            r["sleep"] = r[key]''')
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import requests, h5py, remfile, numpy as np
from concurrent.futures import ThreadPoolExecutor
r=requests.get("https://api.dandiarchive.org/api/dandisets/000473/versions/0.230417.1502/assets/?page_size=200").json()['results']
def one(a):
    s3=requests.head(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/",allow_redirects=True).url
    f=h5py.File(remfile.File(s3),'r'); n=len(f['units/id']); sid=f['general/session_id'][()]; ks=list(f['units'].keys()); st=list(f['stimulus/presentation'].keys()) if 'stimulus/presentation' in f else []
    return a['path'], n, sid, len(ks), st
with ThreadPoolExecutor(12) as ex: out=list(ex.map(one,r))
for o in out: print(o)
print(sum(o[1] for o in out))
EOF
```

```
('sub-128514/sub-128514_ses-128514-20191215-probe0_behavior+ecephys+ogen.nwb', 758, b'128514_20191215-probe0', 19, ['AudStim_10kHz', 'OptogeneticSeries', 'air_puff', 'passive_bluenoise'])
('sub-128515/sub-128515_ses-128515-20191216-probe0_ecephys+ogen.nwb', 293, b'128515_20191216-probe0', 19, ['AudStim_10kHz', 'OptogeneticSeries', 'air_puff', 'passive_bluenoise'])
('sub-128516/sub-128516_ses-128516-20191215-probe0_ecephys+ogen.nwb', 521, b'128516_20191215-probe0', 19, ['AudStim_10kHz', 'OptogeneticSeries', 'air_puff', 'passive_bluenoise'])
('sub-147463/sub-147463_ses-147463-20191113-probe0_ecephys+ogen.nwb', 328, b'147463_20191113-probe0', 19, ['AudStim_10kHz', 'OptogeneticSeries', 'air_puff', 'passive_bluenoise'])
('sub-152414/sub-152414_ses-152414-20191023-probe0_ecephys+ogen.nwb', 447, b'152414_20191023-probe0', 19, ['AudStim_10kHz', 'OptogeneticSeries', 'air_puff', 'passive_bluenoise'])
('sub-152417/sub-152417_ses-152417-20191023-probe0_ecephys+ogen.nwb', 696, b'152417_20191023-probe0', 19, ['AudStim_10kHz', 'OptogeneticSeries', 'air_puff', 'passive_bluenoise'])
('sub-156131/sub-156131_ses-156131-20191112-probe0_ecephys+ogen.nwb', 420, b'156131_20191112-probe0', 19, ['AudStim_10kHz', 'OptogeneticSeries', 'air_puff', 'passive_bluenoise'])
('sub-156130/sub-156130_ses-156130-20191112-probe0_ecephys+ogen.nwb', 400, b'156130_20191112-probe0', 19, ['AudStim_10kHz', 'OptogeneticSeries', 'air_puff', 'passive_bluenoise'])
('sub-216300/sub-216300_ses-216300-20200518-probe0_ecephys+ogen.nwb', 405, b'216300_20200518-probe0', 19, ['AudStim_10kHz', 'OptogeneticSeries', 'air_puff', 'passive_bluenoise'])
('sub-216301/sub-216301_ses-216301-20200521-probe0_ecephys+ogen.nwb', 542, b'216301_20200521-probe0', 19, ['AudStim_10kHz', 'OptogeneticSeries', 'air_puff', 'passive_bluenoise'])
('sub-225757/sub-225757_ses-225757-20200519-probe0_ecephys+ogen.nwb', 518, b'225757_20200519-probe0', 19, ['AudStim_10kHz', 'OptogeneticSeries', 'air_puff', 'passive_bluenoise'])
('sub-225759/sub-22575
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001260-le-merre-2026 && python - <<'EOF'
p='pfcki.py'; s=open(p).read()
s=s.replace('''def list_assets():
    url = f"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200"''','''# The other dandiset the paper names for dataset KI (Data availability); used for counts only.
OTHER_DANDISET, OTHER_VERSION = "000473", "0.230417.1502"


def list_assets(dandiset=DANDISET, version=VERSION):
    url = f"{API}/dandisets/{dandiset}/versions/{version}/assets/?page_size=200"''')
s=s.replace('''def version_metadata():
    return requests.get(f"{API}/dandisets/{DANDISET}/versions/{VERSION}/").json()''','''def version_metadata(dandiset=DANDISET, version=VERSION):
    return requests.get(f"{API}/dandisets/{dandiset}/versions/{version}/").json()''')
open(p,'w').write(s)
EOF
. $TMPDIR/dev/bin/activate && python - <<'EOF' 2>&1 | grep -v "Warning\|nanmean"
import time, pickle, numpy as np, pfcki as P
A=P.list_assets(P.OTHER_DANDISET, P.OTHER_VERSION)
t=time.time(); recs=P.load_all(A, workers=16); print('load', time.time()-t)
print(set(r['desc'] for r in recs), set(r['setting'] for r in recs))
pickle.dump(recs, open('/tmp/claude-1001/recs473.pkl','wb'))
EOF
```

```
load 88.38718819618225
{'Neuropixels recording in mPFC during aversive conditioning task'} {'Aversion'}
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cat > $TMPDIR/dev1.py <<'EOF'
import pickle, numpy as np, pandas as pd, pfcki as P, warnings, time
warnings.filterwarnings('ignore')
recs=pickle.load(open('/tmp/claude-1001/recs.pkl','rb')); r473=pickle.load(open('/tmp/claude-1001/recs473.pkl','rb'))
recs=P.classify_epochs(recs); r473=P.classify_epochs(r473)
U=P.unit_table(recs); U2=P.unit_table(r473); UK=pd.concat([U,U2])
for nm,D in [('001260',U),('KI',UK)]:
  for q in ['all','fp','isi']:
    m={'all':np.ones(len(D),bool),'fp':D.q_fp<0.1,'isi':D.q_isi<0.1}[q]
    k=D[m&(D.n_valid>=12)]
    print(nm,q,len(D),m.sum(),len(k),'pfc',k.is_pfc.sum(),round(100*k.is_pfc.mean(),1),k.utype.value_counts().to_dict(), 'ww%',round(100*(k.utype=='ww').mean(),1),'nw%',round(100*(k.utype=='nw').mean(),1))
# 5 spike variant count
for r in recs: pass
# epochs
rows=[]
for r in recs+r473:
    st=r['state']; sl=r['sleep']
    rows.append(dict(s=r['session'],act=(st=='active').sum(),sl=(st=='sleep').sum(),frac=0 if sl is None or len(sl)==0 else (sl[:,1]-sl[:,0]).sum()/(r['t1']-r['t0'])))
E=pd.DataFrame(rows); print(E[['act','sl','frac']].quantile([.25,.5,.75]))
print(E.iloc[:74][['act','sl','frac']].quantile([.25,.5,.75]))
ww=U[(U.utype=='ww')]
print('ww with >=12 sleep valid', (ww.n_valid_sleep>=12).sum(), 'ww active ok',(ww.n_valid>=12).sum())
import statsmodels.formula.api as smf
k=U[(U.n_valid>=12)&U.utype.isin(['ww','nw'])].dropna(subset=['log10FR','B','M'])
for m in ['log10FR','B','M']:
    t=time.time(); fit=smf.mixedlm(f'{m} ~ C(utype, Treatment("ww"))',k,groups=k.subject).fit(reml=True)
    print(m, fit.params.iloc[1], fit.pvalues.iloc[1], k.groupby('utype')[m].median().to_dict(), time.time()-t)
EOF
python $TMPDIR/dev1.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dev1.py", line 1, in <module>
    import pickle, numpy as np, pandas as pd, pfcki as P, warnings, time
ModuleNotFoundError: No module named 'pfcki'
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && PYTHONPATH=. python $TMPDIR/dev1.py
```

```
/tmp/claude-1001/dev1.py:25: ConvergenceWarning: The MLE may be on the boundary of the parameter space.
  t=time.time(); fit=smf.mixedlm(f'{m} ~ C(utype, Treatment("ww"))',k,groups=k.subject).fit(reml=True)
/tmp/claude-1001/dev1.py:25: ConvergenceWarning: The MLE may be on the boundary of the parameter space.
  t=time.time(); fit=smf.mixedlm(f'{m} ~ C(utype, Treatment("ww"))',k,groups=k.subject).fit(reml=True)
001260 all 20374 20374 14564 pfc 7042 48.4 {'ww': 11209, 'nw': 2752, 'na': 603} ww% 77.0 nw% 18.9
001260 fp 20374 14010 10008 pfc 4710 47.1 {'ww': 7508, 'nw': 2070, 'na': 430} ww% 75.0 nw% 20.7
001260 isi 20374 7331 3781 pfc 1915 50.6 {'ww': 3087, 'nw': 542, 'na': 152} ww% 81.6 nw% 14.3
KI all 29782 29782 20354 pfc 10900 53.6 {'ww': 15894, 'nw': 3698, 'na': 762} ww% 78.1 nw% 18.2
KI fp 29782 20042 13917 pfc 7268 52.2 {'ww': 10579, 'nw': 2790, 'na': 548} ww% 76.0 nw% 20.0
KI isi 29782 9910 4820 pfc 2639 54.8 {'ww': 3975, 'nw': 672, 'na': 173} ww% 82.5 nw% 13.9
        act     sl      frac
0.25   73.0   58.0  0.099116
0.50  158.0  126.0  0.211177
0.75  224.0  212.5  0.346541
         act      sl      frac
0.25   84.25   49.75  0.083574
0.50  180.50  125.50  0.202180
0.75  240.00  210.00  0.329634
ww with >=12 sleep valid 10381 ww active ok 11209
log10FR 0.2354325834636172 1.2115622674948977e-156 {'nw': 0.6858537397826104, 'ww': 0.3679580264589436} 0.15973854064941406
[... 2 more lines not kept]
```

**Agent**

Mixed models put nw above ww on all three metrics (p < 1e-76). Next: SOM training, categories and E-scores.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cat > $TMPDIR/dev2.py <<'EOF'
import pickle, numpy as np, pandas as pd, pfcki as P, warnings, time
warnings.filterwarnings('ignore')
recs=pickle.load(open('/tmp/claude-1001/recs.pkl','rb'))
recs=P.classify_epochs(recs)
U=P.unit_table(recs)
U['setting5']=U.setting.replace({'Opto':'Passive'})
ww=U[(U.utype=='ww')&(U.n_valid>=12)].dropna(subset=['log10FR','B','M']).copy()
F=['log10FR','B','M']
X=ww[F].values; mu,sd=X.mean(0),X.std(0); Z=(X-mu)/sd
t=time.time(); som=P.train_som(Z,400); print('som',time.time()-t, som['shape'], som['W'].shape)
W=som['W']; Wd=W*sd+mu
lab=P.ward_clusters(W,8)
# reading a: order by decreasing median memory (de-standardized? code sorts on X used for clustering)
med_M=np.array([np.median(W[lab==c,2]) for c in range(8)])
rank=(-med_M).argsort().argsort()  # 0 = highest memory
perm=np.array([4,1,6,2,3,7,8,5])-1
a_lab=np.zeros(8,int)
for new,old in enumerate(perm): a_lab[np.where(rank==old)[0][0]]=new+1
# reading b
medFR=np.array([np.median(Wd[lab==c,0]) for c in range(8)]); medB=np.array([np.median(Wd[lab==c,1]) for c in range(8)]); medMd=np.array([np.median(Wd[lab==c,2]) for c in range(8)])
hi=np.argsort(medFR)[-3:]; lo=np.argsort(medFR)[:5]
b_lab=np.zeros(8,int)
for i,c in enumerate(hi[np.argsort(medB[hi])]): b_lab[c]=4+i
lob=lo[np.argsort(medB[lo])]
for i,c in enumerate(lob[:3]): b_lab[c]=1+i
for i,c in enumerate(lob[3:]): b_lab[c]=7+i
bm=P.bmus(Z,W); ww['node']=bm; ww['clu']=lab[bm]; ww['cat_a']=a_lab[lab[bm]]; ww['cat_b']=b_lab[lab[bm]]
tab=pd.DataFrame({'a':a_lab,'b':b_lab,'medFR':medFR,'medB':medB,'medM':medMd,'nodes':np.bincount(lab),'units':np.bincount(lab[bm],minlength=8)})
print(tab.sort_values('a').round(3))
pickle.dump(dict(ww=ww,som=som,mu=mu,sd=sd,lab=lab,a_lab=a_lab,b_lab=b_lab),open('/tmp/claude-1001/som.pkl','wb'))
# enrichment regions
sel=ww[(~ww.cortical)|ww.deep]
cnt=sel.region.value_counts(); regs=cnt[cnt>20].index
t=time.time()
for cat in ['cat_a','cat_b']:
  for g in ['setting5','setting']:
    E,Pv,Xc=P.escore(sel.region.values,sel[cat].values,sel[g].values,1000,seed=1,pops=regs,attrs=range(1,9))
    print(cat,g,time.time()-t)
    print(E.round(1).loc[[r for r in ['ILA','PL','ACAd','ACAv','ORBm','ORBvl','ORBl','MOs','AIv','TH','HPF'] if r in E.index]].to_string())
    print((Pv<0.05).astype(int).loc[[r for r in ['ILA','PL','ACAd','ACAv','ORBm','ORBvl','ORBl','MOs','AIv','TH','HPF'] if r in E.index]].to_string())
EOF
PYTHONPATH=. python $TMPDIR/dev2.py
```

```
som 15.796364784240723 (17, 25) (425, 3)
   a  b  medFR   medB   medM  nodes  units
3  1  5  0.717 -0.095 -0.002     82   2354
4  2  4  1.058 -0.142  0.127     39    881
1  3  1  0.224 -0.206 -0.043     29    869
7  4  3  0.356 -0.017  0.077     55   1326
6  5  7  0.092  0.090  0.004     44   1182
2  6  2  0.061 -0.077 -0.088     80   2078
0  7  8  0.091  0.111 -0.160     54   1398
5  8  6  0.831  0.087 -0.023     42   1121
cat_a setting5 0.20131587982177734
         1    2    3    4    5    6    7    8
ILA   -3.1  3.2  8.7  0.7 -3.9  6.2 -6.1 -4.9
PL    -0.9  2.6  6.1  5.2 -2.6  0.8 -5.0 -5.3
ACAd  -3.3  0.7 -1.9  6.4  3.5 -0.6 -1.9 -1.7
ACAv  -2.9  1.3  0.1  6.3 -0.2  0.5 -2.1 -1.9
ORBm  -0.5  2.2  2.0  2.7 -0.1  0.5 -3.4 -2.5
ORBvl  2.2  2.8  1.8  6.5  0.7 -2.6 -6.6 -3.8
ORBl  -5.1 -0.8 -0.9 -0.6  6.1 -1.2  3.7  0.4
MOs   -1.7  1.8  0.5 -0.5  0.9 -1.8  4.1 -2.1
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://zenodo.org/api/records/14205018 | python -c "
import json,sys; d=json.load(sys.stdin); print(d.get('metadata',{}).get('title'), d.get('metadata',{}).get('version'), d.get('doi'))
for f in d.get('files',[]): print(f['key'], f['size'], f['links']['self'])" | head -20; date -u
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import requests, zipfile, io, h5py, pandas as pd
b=requests.get('https://zenodo.org/api/records/14205018/files/metrics_files.zip/content').content
z=zipfile.ZipFile(io.BytesIO(b)); names=z.namelist(); print(len(names)); print(names[:5])
n=[x for x in names if x.endswith('.h5')][0]
f=h5py.File(io.BytesIO(z.read(n)),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset): print(name,obj.shape,obj.dtype)
f.visititems(show)
open('metrics.zip','wb').write(b)
b2=requests.get('https://zenodo.org/api/records/14205018/files/flatmaps.zip/content').content
z2=zipfile.ZipFile(io.BytesIO(b2)); print(z2.namelist())
open('flatmaps.zip','wb').write(b2)
x=pd.read_excel(io.BytesIO(requests.get('https://zenodo.org/api/records/14205018/files/hierarchy_summary_CreConf.xlsx/content').content),sheet_name=None)
for k,v in x.items(): print(k, v.shape, v.columns.tolist()[:12]); print(v.head(3).to_string()[:600])
print(requests.get('https://zenodo.org/api/records/14205018/files/ROI_Gao_hierarchy_index.csv/content').text[:400])
EOF
```

```
417
['metrics_files/', 'metrics_files/metric_files_Carlen/', 'metrics_files/metric_files_IBL_Passive/', 'metrics_files/.DS_Store', '__MACOSX/metrics_files/._.DS_Store']
Dataset () |S6
Task () |S7
anatomy/U (426,) float64
anatomy/V (426,) float64
anatomy/ap (426,) float64
anatomy/dv (426,) float64
anatomy/location (426,) object
anatomy/main channel (426,) float64
anatomy/ml (426,) float64
anatomy/roi (426,) float64
quality/quality (426,) int64
uids (426,) int64
unit_type/nw (426,) int64
unit_type/ww (426,) int64
waveform_metrics/abRatio (426,) float64
waveform_metrics/amplitude (426,) float64
waveform_metrics/depolSlope (426,) float64
waveform_metrics/duration (426,) float64
[... 94 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap/python; grep -n "read_excel\|sheet\|CC+TC+CT\|Aid\|replace\|ctx\|Cortex" connectivity_correlations/*.py | head -30; ls connectivity_correlations
```

```
connectivity_correlations/gao_module_hierarchy.py:87:            df = pd.read_excel(srcfile, sheet_name=None)#reads alll sheets
connectivity_correlations/gao_module_hierarchy.py:88:            ncvec = np.sort(np.array([int(val.replace('ncl','')) for val in df.keys()]))
connectivity_correlations/harris_vs_enrichment.py:23:ctx_only = True
connectivity_correlations/harris_vs_enrichment.py:132:df = pd.read_excel(tablepath_hierarchy, sheet_name='hierarchy_all_regions')
connectivity_correlations/harris_vs_enrichment.py:134:hvec = np.array([el for el in df['CC+TC+CT iterated']])
connectivity_correlations/harris_vs_enrichment.py:135:ctx_bool = np.array([el=='C' for el in  df['CortexThalamus']])
connectivity_correlations/harris_vs_enrichment.py:136:ctx_avec = avec[ctx_bool]
connectivity_correlations/harris_vs_enrichment.py:146:                    'AId':'Aid','AIp':'Aip','AIv':'Aiv'}
connectivity_correlations/harris_vs_enrichment.py:163:    if U.areaH in ctx_avec and layercheck(U.layer):
connectivity_correlations/harris_vs_enrichment.py:184:if ctx_only:
connectivity_correlations/harris_vs_enrichment.py:186:    subfolder = 'ctx_only'
connectivity_correlations/harris_vs_enrichment.py:220:cdict_ext = dict(S.cdict_pfc,**{newkey:S.cdict_pfc[oldkey] for newkey,oldkey in zip(['Aid','Aiv'],['AId','AIv'])})
connectivity_correlations/harris_vs_enrichment.py:623:            df.to_excel(writer, sheet_name=dskey)
connectivity_correlations/harris_vs_enrichment_ENHequalaxes.py:22:ctx_only = True
connectivity_correlations/harris_vs_enrichment_ENHequalaxes.py:44:df = pd.read_excel(tablepath_hierarchy, sheet_name='hierarchy_all_regions')
connectivity_correlations/harris_vs_enrichment_ENHequalaxes.py:46:hvec = np.array([el for el in df['CC+TC+CT iterated']])
connectivity_correlations/harris_vs_enrichment_ENHequalaxes.py:47:ctx_bool = np.array([el=='C' for el in  df['CortexThalamus']])
connectivity_correlations/harris_vs_enrichment_ENHequalaxes.py:48:ctx_avec = avec[ctx_bool]
connectivity_correl
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap/python; sed -n 140,200p connectivity_correlations/harris_vs_enrichment.py
```

```
solitary_uareas = [area for area in uareas if not area in avec]


areaIBL_to_areaH = {'AMd':'AM','AMv':'AM',\
                  'LGd-co':'LGd','LGd-ip':'LGd','LGd-sh':'LGd',\
                  'MGd':'MG','MGm':'MG','MGv':'MG',\
                    'AId':'Aid','AIp':'Aip','AIv':'Aiv'}

areaH_to_areaIBL = {val:[key for key in areaIBL_to_areaH.keys() if areaIBL_to_areaH[key]==val] for val in np.unique(list(areaIBL_to_areaH.values()))}
#N.B: 'PF' is unmatched

for U in Units:
    if U.area in areaIBL_to_areaH.keys():
        areaH =  areaIBL_to_areaH[U.area]
    elif U.area in avec:
        areaH = str(U.area)
    else:
        areaH = 'NA'
    U.set_feature('areaH', areaH)

[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && PYTHONPATH=entries/001260-le-merre-2026 python - <<'EOF'
import zipfile, h5py, io, numpy as np, pickle, pandas as pd
z=zipfile.ZipFile('metrics.zip'); n=[x for x in z.namelist() if 'Carlen' in x and x.endswith('.h5') and 'MACOSX' not in x]; print(len(n), n[:3])
recs=pickle.load(open('recs.pkl','rb'))
r=recs[40]; print(r['session'])
m=[x for x in n if r['session'].replace('-','_') in x or r['session'] in x]; print(m)
f=h5py.File(io.BytesIO(z.read(m[0])),'r')
uid=f['uids'][:]; print(len(uid), len(r['units']), uid[:10], r['units'].unit_id.values[:10])
print(f['Task'][()], f['Dataset'][()], f['anatomy/location'][:5], r['units'].location.values[:5], f['quality/quality'][:].mean(), f['waveform_metrics/waveform_quality'][:].mean(), f['waveform_metrics/peak2Trough'][:5], r['units'].ptt.values[:5])
print(f['anatomy/U'][:5], f['anatomy/roi'][:10])
EOF
```

```
108 ['metrics_files/metric_files_Carlen/metrics_732713_20230831-probe0.h5', 'metrics_files/metric_files_Carlen/metrics_732713_20230831-probe1.h5', 'metrics_files/metric_files_Carlen/metrics_732714_20230829-probe1.h5']
PL057_20200203-probe0
['metrics_files/metric_files_Carlen/metrics_PL057_20200203-probe0.h5']
259 259 [0 1 2 3 4 5 6 7 8 9] [0 1 2 3 4 5 6 7 8 9]
b'Detection' b'Carlen' [b'aco' b'aco' b'ACB' b'ACB' b'ACB'] <StringArray>
['aco', 'aco', 'aco', 'aco', 'aco']
Length: 5, dtype: str 0.9575289575289575 1.0 [0.00066593 0.00060253 0.00055533 0.0006452  0.00068343] [0.66593333 0.60253333 0.55533333 0.6452     0.68343333]
[0. 0. 0. 0. 0.] [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  python -c "
import json; nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:6]: print(c['cell_type'], c['metadata'], ''.join(c['source'])[:700]); print('-----')
print(nb['metadata'])
"; sed -n 1,80p tools/entry.py | head -80; cat entries/001453-fouke-2025/README.md | head -30
```

```
markdown {} # Reproducing Fouke et al. (2025) from dandiset 001453

**Paper.** Fouke KE, He Z, Loring MD, Naumann EA (2025). Neural circuits underlying divergent
visuomotor strategies of zebrafish and *Danionella cerebrum*. *Current Biology*.
[doi:10.1016/j.cub.2025.04.027](https://doi.org/10.1016/j.cub.2025.04.027). This attempt used the
full text of the accepted author manuscript in PubMed Central (PMC12218792); the version of record
is not open access.

**Dandiset.** [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), version
0.250518.1950. The paper cites no DANDI version (its data statement points to a GitLab repository
that holds code only). This is the only published version. 
-----
code {} import time
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats
[... 157 more lines not kept]
```

**Agent**

Now adding the remaining helper functions: Zenodo inputs, category readings, block stability, mixed models and gradients.

**Agent calls Bash**

```bash
cd entries/001260-le-merre-2026 && cat >> pfcki.py <<'EOF'


# ---------------------------------------------------------------- categories
# code SOM/clusterSOM/relabel_clusters.py label_sorter (8 ww and 5 nw clusters), applied to Ward
# clusters first ranked by decreasing median memory of their node prototypes (cluster_SOM.py).
CODE_SORTER = {8: np.array([4, 1, 6, 2, 3, 7, 8, 5]) - 1, 5: np.array([1, 2, 4, 5, 3]) - 1}


def category_maps(W, lab, mu, sd, k):
    """Category number (1..k) of each Ward cluster under the two readings of G2.

    (a) the code's: clusters ranked by decreasing median memory of their (standardized)
        prototypes, then the code's fixed permutation.
    (b) matching the text's descriptions (ww only): the three clusters with the highest median
        log10FR are 4 to 6 in order of increasing median B; of the other five, the three with
        the lowest median B are 1 to 3 and the other two 7 and 8, each in order of increasing B.
        For nw (5 clusters) reading (b) is not defined by the text and returns None."""
    Wd = W * sd + mu
    med = pd.DataFrame({c: [np.median(Wd[lab == c, j]) for c in range(k)] for j, c in
                        zip(range(3), ["log10FR", "B", "M"])})
    rank = (-np.array([np.median(W[lab == c, 2]) for c in range(k)])).argsort().argsort()
    a = np.zeros(k, int)
    for new, old in enumerate(CODE_SORTER[k]):
        a[np.where(rank == old)[0][0]] = new + 1
    b = None
    if k == 8:
        b = np.zeros(k, int)
        hi = np.argsort(med.log10FR.values)[-3:]
        lo = np.argsort(med.log10FR.values)[:5]
        for i, c in enumerate(hi[np.argsort(med.B.values[hi])]):
            b[c] = 4 + i
        lob = lo[np.argsort(med.B.values[lo])]
        for i, c in enumerate(lob):
            b[c] = [1, 2, 3, 7, 8][i]
    med["n_nodes"] = np.bincount(lab, minlength=k)
    return a, b, med


def fit_categories(units, nnodes, k):
    """Standardize, train the SOM, cluster its nodes; returns a dict with everything."""
    F = ["log10FR", "B", "M"]
    X = units[F].values
    mu, sd = X.mean(0), X.std(0)
    Z = (X - mu) / sd
    som = train_som(Z, nnodes)
    lab = ward_clusters(som["W"], k)
    a, b, med = category_maps(som["W"], lab, mu, sd, k)
    node = bmus(Z, som["W"])
    return dict(som=som, mu=mu, sd=sd, lab=lab, map_a=a, map_b=b, med=med, node=node,
                cat_a=a[lab[node]], cat_b=None if b is None else b[lab[node]])


# ---------------------------------------------------------------- stability
def block_categories(recs, units, fit, min_valid=MIN_EPOCHS):
    """Per unit and block: metrics over the block's active epochs, standardized to the full-data
    SOM, and the block's category under both readings (Methods, Stability analyses)."""
    rows = []
    key = units.set_index(["session", "unit_id"]).index
    for r in recs:
        u = r["units"]
        sel = key.get_indexer(pd.MultiIndex.from_arrays([u.session, u.unit_id]))
        for b in np.unique(r["blocks"]):
            m = (r["state"] == "active") & (r["blocks"] == b)
            if m.sum() == 0:
                continue
            met = unit_metrics(r, m)
            ok = (sel >= 0) & (met.n_valid.values >= min_valid) & met[["log10FR", "B", "M"]].notna().all(1).values
            if not ok.any():
                continue
            Z = (met.loc[ok, ["log10FR", "B", "M"]].values - fit["mu"]) / fit["sd"]
            node = bmus(Z, fit["som"]["W"])
            cl = fit["lab"][node]
            rows.append(pd.DataFrame({"session": r["session"], "unit_id": u.unit_id.values[ok], "block": b,
                                      "cat_a": fit["map_a"][cl],
                                      "cat_b": fit["map_b"][cl] if fit["map_b"] is not None else 0,
                                      "n_epochs": met.n_valid.values[ok]}))
    return pd.concat(rows, ignore_index=True)


def transitions(bc, cat, k):
    """Transition count matrices M_t (t = 1 for block 1 to block 2, ...) summed over units;
    a transition is counted between consecutive blocks of a recording where the unit has both."""
    Ms = {}
    for (s, u), g in bc.sort_values("block").groupby(["session", "unit_id"]):
        bl, c = g.block.values, g[cat].values
        for i in range(len(bl) - 1):
            if bl[i + 1] == bl[i] + 1:
                t = int(bl[i]) + 1
                Ms.setdefault(t, np.zeros((k, k), int))[c[i] - 1, c[i + 1] - 1] += 1
    return dict(sorted(Ms.items()))


def stability(M):
    n = M.sum()
    E = np.outer(M.sum(1), M.sum(0)) / n
    return np.trace(M) / n, np.trace(E) / n


def coincidence(M):
    """Methods, equation 4."""
    n = M.sum()
    R, C = M.sum(1), M.sum(0)
    E = np.outer(R, C) / n
    X = np.where(M >= E, (M - E) / (np.minimum(R[:, None], C[None, :]) - E), (M - E) / E)
    return X


# ---------------------------------------------------------------- statistics
def mixed(df, formula, group="subject"):
    """Linear mixed model with a random intercept per mouse (statsmodels MixedLM, REML).
    Returns the fit and the marginal R2 (Nakagawa and Schielzeth): variance of the fixed-effect
    prediction over itself plus the random-intercept and residual variances."""
    import statsmodels.formula.api as smf
    fit = smf.mixedlm(formula, df, groups=df[group]).fit(reml=True)
    fe = fit.model.exog @ fit.fe_params.values
    vf = np.var(fe)
    r2m = vf / (vf + float(fit.cov_re.iloc[0, 0]) + fit.scale)
    return fit, r2m


def gradient_angle(pos, v1, v2):
    """Angle (degrees) between the directions of steepest increase of two node values, from a
    linear fit of each on the node coordinates."""
    A = np.c_[pos, np.ones(len(pos))]
    g1 = np.linalg.lstsq(A, v1, rcond=None)[0][:2]
    g2 = np.linalg.lstsq(A, v2, rcond=None)[0][:2]
    c = g1 @ g2 / np.linalg.norm(g1) / np.linalg.norm(g2)
    return float(np.degrees(np.arccos(np.clip(c, -1, 1)))), g1, g2


# ---------------------------------------------------------------- outside inputs
ZENODO_RECORD = "14205018"  # doi:10.5281/zenodo.14205018, the paper's intermediate files


def zenodo_bytes(name):
    r = requests.get(f"https://zenodo.org/api/records/{ZENODO_RECORD}/files/{name}/content")
    r.raise_for_status()
    return r.content


def paper_unit_table():
    """The paper's per-unit metrics files (Zenodo metrics_files.zip, dataset KI): recording,
    unit id, flatmap (U, V), location, quality flags and ww/nw labels."""
    import io
    import zipfile
    z = zipfile.ZipFile(io.BytesIO(zenodo_bytes("metrics_files.zip")))
    rows = []
    for n in z.namelist():
        if "metric_files_Carlen/metrics_" not in n or not n.endswith(".h5") or "MACOSX" in n:
            continue
        rec = n.split("metrics_")[-1][:-3]
        with h5py.File(io.BytesIO(z.read(n)), "r") as f:
            rows.append(pd.DataFrame({
                "session": rec, "unit_id": f["uids"][:], "U": f["anatomy/U"][:], "V": f["anatomy/V"][:],
                "z_location": [dec(x) for x in f["anatomy/location"][:]],
                "z_quality": f["quality/quality"][:], "z_wquality": f["waveform_metrics/waveform_quality"][:],
                "z_ww": f["unit_type/ww"][:], "z_nw": f["unit_type/nw"][:],
                "z_p2t_ms": f["waveform_metrics/peak2Trough"][:] * 1000, "z_task": dec(f["Task"][()])}))
    return pd.concat(rows, ignore_index=True)


def harris_table():
    """Harris et al. 2019 hierarchy scores as the code reads them (connectivity_correlations/
    harris_vs_enrichment.py: sheet hierarchy_all_regions, column 'CC+TC+CT iterated', cortex rows;
    AId, AIp, AIv are spelled Aid, Aip, Aiv in the table)."""
    import io
    df = pd.read_excel(io.BytesIO(zenodo_bytes("hierarchy_summary_CreConf.xlsx")), sheet_name="hierarchy_all_regions")
    df = df[df["CortexThalamus"] == "C"]
    ren = {"Aid": "AId", "Aip": "AIp", "Aiv": "AIv"}
    return pd.Series(df["CC+TC+CT iterated"].values, index=[ren.get(a, a) for a in df["areas"]])
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cat > $TMPDIR/dev3.py <<'EOF'
import pickle, numpy as np, pandas as pd, pfcki as P, warnings, time
warnings.filterwarnings('ignore')
recs=pickle.load(open('/tmp/claude-1001/recs.pkl','rb')); recs=P.classify_epochs(recs)
U=P.unit_table(recs)
ww=U[(U.utype=='ww')&(U.n_valid>=12)].dropna(subset=['log10FR','B','M']).copy()
t=time.time(); fit=P.fit_categories(ww,400,8); print('fit',time.time()-t); print(fit['med'].assign(a=fit['map_a'],b=fit['map_b']).round(3))
ww['cat_a'],ww['cat_b']=fit['cat_a'],fit['cat_b']
t=time.time(); bc=P.block_categories(recs,ww,fit); print('blocks',time.time()-t, len(bc), bc.groupby(['session','unit_id']).ngroups)
for cat in ['cat_a','cat_b']:
    Ms=P.transitions(bc,cat,8); st=[P.stability(M) for M in Ms.values()]; print(cat, [ (t,M.sum()) for t,M in Ms.items()])
    print(np.round(st,3)); Msum=sum(Ms.values()); print('pooled',np.round(P.stability(Msum),3), 'mean', np.round(np.mean(st,0),3))
    Pm=Msum/Msum.sum(1,keepdims=True); print(np.round(np.diag(Pm),3)); print(np.round(np.diag(P.coincidence(Msum)),3))
bc3=P.block_categories(recs,ww,fit,min_valid=3); Ms=P.transitions(bc3,'cat_b',8); print('min3', np.round(P.stability(sum(Ms.values())),3))
# extfig1d
fitm,r2=P.mixed(ww,'B ~ M'); print('B~M',fitm.params['M'],fitm.pvalues['M'],r2)
a=ww[['subject','log10FR','B','M']].assign(et='active')
s=U[(U.utype=='ww')&(U.n_valid_sleep>=12)][['subject','log10FR_sleep','B_sleep','M_sleep']].rename(columns=lambda c:c.replace('_sleep','')).assign(et='sleep')
L=pd.concat([a,s]).dropna()
for m in ['log10FR','B','M']:
    f,_=P.mixed(L,f'{m} ~ C(et)'); print(m, f.params.iloc[1], f.pvalues.iloc[1], L.groupby('et')[m].median().to_dict())
W=fit['som']['W']*fit['sd']+fit['mu']; ang=P.gradient_angle(fit['som']['pos'],W[:,1],W[:,0]); print('angle',ang[0])
for q in [0.9,0.75]:
    top=W[:,2]>=np.quantile(W[:,2],q); print(q, top.sum(), (W[top,1]>=np.quantile(W[:,1],0.75)).sum())
EOF
PYTHONPATH=. python $TMPDIR/dev3.py
```

```
entries/001260-le-merre-2026/pfcki.py:706: ConvergenceWarning: The MLE may be on the boundary of the parameter space.
  fit = smf.mixedlm(formula, df, groups=df[group]).fit(reml=True)
entries/001260-le-merre-2026/pfcki.py:706: ConvergenceWarning: The MLE may be on the boundary of the parameter space.
  fit = smf.mixedlm(formula, df, groups=df[group]).fit(reml=True)
entries/001260-le-merre-2026/pfcki.py:706: ConvergenceWarning: The MLE may be on the boundary of the parameter space.
  fit = smf.mixedlm(formula, df, groups=df[group]).fit(reml=True)
entries/001260-le-merre-2026/pfcki.py:706: ConvergenceWarning: The MLE may be on the boundary of the parameter space.
  fit = smf.mixedlm(formula, df, groups=df[group]).fit(reml=True)
fit 14.418761968612671
   log10FR      B      M  n_nodes  a  b
0    0.091  0.111 -0.160       54  7  8
1    0.224 -0.206 -0.043       29  3  1
2    0.061 -0.077 -0.088       80  6  2
3    0.717 -0.095 -0.002       82  1  5
4    1.058 -0.142  0.127       39  2  4
5    0.831  0.087 -0.023       42  8  6
6    0.092  0.090  0.004       44  5  7
7    0.356 -0.017  0.077       55  4  3
blocks 1.0078489780426025 35992 8768
cat_a [(1, np.int64(1826)), (2, np.int64(2450)), (3, np.int64(3519)), (4, np.int64(4198)), (5, np.int64(3812)), (6, np.int64(2848)), (7, np.int64(2788)), (8, np.int64(1202)), (9, np.int64(721)), (10, np.int64(445)), (11, np.int64(186)), (12, np.int64(204)), (13, np.int64(199))]
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && uv pip install -q k-means-constrained shapely 2>&1 | tail -2; PYTHONPATH=. python - <<'EOF'
import io, zipfile, h5py, pfcki as P
z=zipfile.ZipFile(io.BytesIO(P.zenodo_bytes('flatmaps.zip')))
for n in z.namelist():
    if n.endswith('.h5'):
        f=h5py.File(io.BytesIO(z.read(n)),'r'); print(n)
        f.visititems(lambda name,o: print('  ',name, getattr(o,'shape',''), getattr(o,'dtype','')) if isinstance(o,h5py.Dataset) or len(name.split('/'))<3 else None)
EOF
```

```
flatmaps/flatmap_PFC_ntesselated_obeyRegions_res100.h5
   1 (6, 2) float32
   10 (7, 2) float32
   11 (7, 2) float32
   12 (6, 2) float32
   13 (5, 2) float32
   14 (7, 2) float32
   15 (12, 2) float32
   16 (6, 2) float32
   17 (7, 2) float32
   18 (9, 2) float32
   19 (6, 2) float32
   2 (5, 2) float32
   20 (6, 2) float32
   21 (7, 2) float32
   22 (7, 2) float32
   23 (5, 2) float32
   24 (7, 2) float32
   25 (6, 2) float32
   26 (8, 2) float32
[... 184 more lines not kept]
```

**Agent**

Zenodo also holds the paper's 42-polygon dataROI tessellation and the 60 GaoROI polygons, so the flatmap claims can run once units are linked. Writing the notebook builder.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nexec(open(\"/tmp/claude-1001/nb_cells.py\").read())\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata = {\"kernelspec\": {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"}}\nnbf.write(nb, \"entries/001260-le-merre-2026/reproduce_le_merre_2026.ipynb\")\nprint(len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_cells.py",
 "content": "md(r'''\n# Reproducing Le Merre, Heining et al. (2026) from dandiset 001260\n\n**Paper.** Le Merre P, Heining K, Slashcheva M, Jung F, Moysiadou E, Guyon N, Yahya R, Park H,\nWernstal F, Carlén M. A prefrontal cortex map based on single-neuron activity. *Nature\nNeuroscience* (2026). [doi:10.1038/s41593-025-02190-z](https://doi.org/10.1038/s41593-025-02190-z).\nThe claims file (`claims/001260/10.1038-s41593-025-02190-z.yaml`) was written from the version of\nrecord (publisher HTML: main text, legends, Methods and Extended Data legends); the Supplementary\nInformation was not available to it.\n\n**Dandiset.** [DANDI:001260](https://dandiarchive.org/dandiset/001260/0.250911.0744), version\n0.250911.0744. The paper cites no version. This is the only published version, and the draft\nhas the same 74 assets and size, so it is pinned.\n\n**Other data.** The paper deposits its dataset KI in two dandisets, 000473 and 001260 (Data\navailability). Dandiset 000473 (version 0.230417.1502, the only published one; its metadata\nnames another paper) holds 25 more recordings; it is read here only for the unit counts of\n`dataset-ki-counts` and `fig1h-waveform-classes`. From the paper's Zenodo record\n[10.5281/zenodo.14205018](https://doi.org/10.5281/zenodo.14205018) this attempt reads the\nHarris et al. hierarchy table (`hierarchy_summary_CreConf.xlsx`), the per-unit metrics files\n(`metrics_files.zip`, for each unit's flatmap position), the flatmap polygons\n(`flatmaps.zip`) and the Gao et al. ROI hierarchy table (`ROI_Gao_hierarchy_index.csv`).\n\n**Methods.** The helper module `pfcki.py` says where every parameter comes from. Units are not\nfiltered by a quality label, as the files carry none (see the data check); every analysis\nkeeps units with at least 12 active spontaneous epochs of at least 6 spikes.\n\n**Claims.** Tested here: the claims on dataset KI's spontaneous activity (Figs. 1 and 2,\nExtended Data Figs. 1, 3 and 5), the Harris hierarchy correlations (Fig. 3a,c, Supplementary\nTable 5) with the Harris table, and, through the Zenodo flatmap positions, the PFC flatmap\nclaims (Fig. 4) after a link claim. Blocked: every claim on dataset IBL (Figs. 2i, 3b, 5g,\n5h, 5k) and the tone-response claims (Fig. 5b to 5f, 5i, 5j, Extended Data Fig. 9e), for\nthe time of this run; `methods-settings-no-difference`, whose test the paper does not name.\nThe table of outcomes is in the summary.\n''')\n\ncode(r'''\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport pfcki as P\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nwarnings.filterwarnings(\"ignore\")\n\nt_start = time.time()\nassets = P.list_assets()\nrecs = P.classify_epochs(P.load_all(assets))\nU = P.unit_table(recs)\nprint(f\"dandiset {P.DANDISET} version {P.VERSION}: {len(assets)} assets, {len(recs)} files read, \"\n      f\"{len(U)} units, in {time.time() - t_start:.0f} s\")\nassets473 = P.list_assets(P.OTHER_DANDISET, P.OTHER_VERSION)\nrecs473 = P.classify_epochs(P.load_all(assets473))\nU473 = P.unit_table(recs473)\nprint(f\"dandiset {P.OTHER_DANDISET} version {P.OTHER_VERSION}: {len(recs473)} files, {len(U473)} units, \"\n      f\"total {time.time() - t_start:.0f} s\")\n''')\n\nmd(r'''\n## Data check\n''')\n\ncode(r'''\nmeta = P.version_metadata()\nprint(\"Archive summary:\", meta[\"assetsSummary\"][\"numberOfFiles\"], \"files,\",\n      meta[\"assetsSummary\"][\"numberOfSubjects\"], \"subjects\")\ninfo = pd.DataFrame([{\"session\": r[\"session\"], \"subject\": r[\"subject\"], \"setting\": r[\"setting\"],\n                      \"units\": len(r[\"units\"]), \"onsets\": len(r[\"onsets\"]), \"cortical_units\": r[\"n_cortical\"],\n                      \"duration_min\": round((r[\"t1\"] - r[\"t0\"]) / 60, 1), \"blocks\": r[\"blockmode\"],\n                      \"description\": r[\"desc\"][:58]} for r in recs])\nprint(info.to_string(index=False))\nprint(\"\\nFiles, subjects and units by behavioral setting (setting from the session description and keywords):\")\nprint(info.groupby(\"setting\").agg(files=(\"session\", \"size\"), subjects=(\"subject\", \"nunique\"), units=(\"units\", \"sum\")).to_string())\nprint(\"Distinct subjects:\", info.subject.nunique(), \"| sessions (subject and date):\",\n      info.session.str.split(\"-\").str[0].nunique())\n''', [\"sanity\"])\n\nmd(r'''\nThe archive counts 43 subjects; the files name 41 distinct mice once the suffixes `-1` and `-2`\nof two subject ids (518804 and 560171, two days each) are removed, and 43 as written. The\nsetting read from each file's description agrees with the setting the paper's code assigns to\nthe same recording (`config/datatables/allrecs_allprobes.xlsx`) for every file: Aversion 6,\nDetection 15, Context 14, working memory (\"Attention\" in the code) 15, Opto 4, Passive 20.\nFive auditory-cortex probes are described as Neuronexus recordings; the paper pools them as\nprobes of dataset KI.\n''')\n\ncode(r'''\ndef rng_str(x):\n    x = np.asarray(x, float)\n    return f\"{np.nanmin(x):.3g} to {np.nanmax(x):.3g} (median {np.nanmedian(x):.3g})\"\n\nprint(\"Peak_to_Trough (ms):\", rng_str(U.Peak_to_Trough if \"Peak_to_Trough\" in U else U.ptt))\nprint(\"quality column 0, 'ISI violation':\", rng_str(U.q_isi), \"| fraction < 0.1:\", round((U.q_isi < 0.1).mean(), 3))\nprint(\"quality column 1, 'false positive rate':\", rng_str(U.q_fp), \"| fraction < 0.1:\", round((U.q_fp < 0.1).mean(), 3))\nprint(\"spikes per unit:\", rng_str(U.n_spikes))\nprint(\"unit locations: \", U.location.nunique(), \"labels;\", (U.layer != \"NA\").mean().round(3), \"of units have a layer\")\nprint(\"units per parent region:\"); print(U.parent.value_counts().to_string())\nprint(\"\\nAll units in both dandisets:\", len(U), \"+\", len(U473), \"=\", len(U) + len(U473),\n      \"| paper: 34,642 sorted, 29,782 after excluding 24 recordings, 24,248 after quality control\")\n''', [\"sanity\"])\n\nmd(r'''\nThe two dandisets hold 29,782 units together, exactly the paper's count after it excluded 24\nrecordings and before its unit quality control, so the files hold every sorted unit of the 99\nrecordings and no label says which units passed. The units table has a two-column `quality`\n(ISI violation, false positive rate). The first column runs to hundreds, so it is not the ISI\nviolation ratio below 0.1 of the Methods in the same units; fewer than half of the units are\nbelow 0.1 on it. Its meaning is not described. The peak-to-trough durations are in ms, as\nstated, and agree with the paper's Zenodo metrics files (shown in the link claim).\n''')\n\ncode(r'''\nep = pd.DataFrame([{\"session\": r[\"session\"], \"setting\": r[\"setting\"], \"epochs\": len(r[\"epochs\"]),\n                    **pd.Series(r[\"state\"]).value_counts().to_dict(),\n                    \"lick_periods\": len(r[\"lick\"]), \"saturation_periods\": len(r[\"sat\"]),\n                    \"sleep_source\": (\"none (code: ignore)\" if r[\"session\"] in P.QUIET_IGNORE else\n                                     (\"other probe\" if r[\"session\"] in P.QUIET_FROM_OTHER else \"own\"))} for r in recs]).fillna(0)\nprint(ep.to_string(index=False))\nprint(\"\\nEpoch length is 3 s for every epoch:\", all(np.allclose(np.diff(r[\"epochs\"], axis=1), 3) for r in recs))\nprint(\"Onsets per file:\", rng_str(ep.epochs), \"| active:\", rng_str(ep.active))\ngaps = np.concatenate([np.diff(r[\"onsets\"]) for r in recs if r[\"setting\"] != \"Attention\"])\nprint(\"Intervals between successive onsets outside the working-memory setting (s):\",\n      np.percentile(gaps, [1, 5, 50, 95, 99]).round(2), \"(Methods: tones at random intervals of 5 to 10 s)\")\n''', [\"sanity\"])\n\nmd(r'''\nLicking is marked in 44 files (LickOnset and LickOffset series), saturation of the spike band in\nmost. Sleep-like periods are detected from each probe's cortical units, or from the probe the\npaper's code names for probes with few cortical units, and not for the four hippocampal probes,\nas in the code. Onsets come at intervals of about 5 to 10 s outside the working-memory setting,\nas the Methods state; in the working-memory setting the code's onsets are trial starts.\n\nClock check. The spike times and the stimulus onsets must share a clock: below, the population\nrate of PFC units in 25-ms bins around the 10-kHz tone onsets of each file, against the same\nwith the onsets shifted by 1.5 s (a time with no tone). A response locked to the true onsets, and\nnot to the shifted ones, shows the clocks agree.\n''')\n\ncode(r'''\ndef onset_response(r, shift=0.0):\n    if r[\"tones\"] is None:\n        return np.nan, np.nan\n    rec_units = r[\"units\"]\n    return r[\"tones\"] + shift, len(rec_units)\n\ndef tone_contrast(r, shift):\n    \"\"\"Mean rate of all units 0 to 100 ms after the onsets minus 100 to 0 ms before, in Hz per unit.\"\"\"\n    if r[\"tones\"] is None:\n        return np.nan\n    f = P.open_asset(r[\"asset_id\"])\n    st = f[\"units/spike_times\"][:]\n    f.close()\n    t = r[\"tones\"] + shift\n    st.sort()\n    post = np.searchsorted(st, t + 0.1) - np.searchsorted(st, t)\n    pre = np.searchsorted(st, t) - np.searchsorted(st, t - 0.1)\n    return (post.sum() - pre.sum()) / len(t) / 0.1 / len(r[\"units\"])\n\nsample = [r for r in recs if r[\"tones\"] is not None][::6]\ncc = pd.DataFrame([{\"session\": r[\"session\"], \"true onsets\": tone_contrast(r, 0.0),\n                    \"shifted 1.5 s\": tone_contrast(r, 1.5)} for r in sample])\nprint(\"Post minus pre rate (Hz per unit) around 10-kHz tone onsets, every sixth file with tones:\")\nprint(cc.round(3).to_string(index=False))\nprint(\"files with a larger change at the true onsets than at the shifted ones:\",\n      int((cc[\"true onsets\"].abs() > cc[\"shifted 1.5 s\"].abs()).sum()), \"of\", len(cc))\n''', [\"sanity\"])\n\nmd(r'''\n## dataset-ki-counts\n\n> Dataset KI holds 24,248 single units from 99 Neuropixels recordings in awake head-fixed mice,\n> 52% of them in the PFC and 48% in other brain regions.\n\nReadings of the unit selection (claims file, G3): (a) the dataset's own quality metrics under\nthe Methods criteria, read as column 0 (ISI violation) below 0.1 or column 1 (false positive\nrate) below 0.1; (b) all units. Each also needs at least 12 active epochs with at least 6\nspikes (Methods); counting epochs with at least 5 spikes (the \"≥4 ISIs\" of the Methods' unit\nquality control) and over all spontaneous epochs, active or sleep-like, are shown as variants.\n''')\n\ncode(r'''\ndef count_table(D, label):\n    rows = []\n    for g3, m in [(\"(a) ISI violation < 0.1\", D.q_isi < 0.1), (\"(a) false positive rate < 0.1\", D.q_fp < 0.1),\n                  (\"(b) all units\", np.ones(len(D), bool))]:\n        k = D[m & (D.n_valid >= P.MIN_EPOCHS)]\n        rows.append({\"data\": label, \"reading\": g3, \"units\": len(k), \"PFC units\": int(k.is_pfc.sum()),\n                     \"PFC %\": round(100 * k.is_pfc.mean(), 1)})\n    return rows\n\nUK = pd.concat([U, U473], ignore_index=True)\nrec_counts = {\"001260\": len(recs), \"001260 + 000473\": len(recs) + len(recs473)}\nct = pd.DataFrame(count_table(U, \"001260\") + count_table(UK, \"001260 + 000473\"))\nprint(ct.to_string(index=False))\nprint(\"recordings (probes):\", rec_counts, \"| expected 24,248 ± 2,425 units, 52 ± 5.2 % PFC, 99 recordings, 12,674 ± 1,267 PFC units\")\n\ndef n_valid_with(recs_, min_spikes, states):\n    out = []\n    for r in recs_:\n        m = np.isin(r[\"state\"], states)\n        out.append((r[\"cnt\"][:, m] >= min_spikes).sum(1))\n    return np.concatenate(out)\n\nvar = []\nfor lab, rr, D in [(\"001260\", recs, U), (\"001260 + 000473\", recs + recs473, UK)]:\n    for ms in [6, 5]:\n        for states, sl in [([\"active\"], \"active\"), ([\"active\", \"near_sleep\", \"sleep\"], \"all spontaneous\")]:\n            nv = n_valid_with(rr, ms, states)\n            k = D[nv >= P.MIN_EPOCHS]\n            var.append({\"data\": lab, \"min spikes\": ms, \"epochs\": sl, \"units\": len(k),\n                        \"PFC %\": round(100 * k.is_pfc.mean(), 1), \"PFC units\": int(k.is_pfc.sum())})\nprint(\"\\nVariants of the 12-epoch rule, reading (b):\")\nprint(pd.DataFrame(var).to_string(index=False))\n''', [\"claim:dataset-ki-counts\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## fig1h-waveform-classes\n\n> Peak-to-trough durations are bimodal, splitting units into 19,186 ww units (81.1%) and 4,200\n> nw units (17.7%), with 862 intermediate units left unclassified.\n''')\n\ncode(r'''\nwf = []\nfor lab, D in [(\"001260\", U), (\"001260 + 000473\", UK)]:\n    for g3, m in [(\"(a) false positive rate < 0.1\", D.q_fp < 0.1), (\"(b) all units\", np.ones(len(D), bool))]:\n        k = D[m & (D.n_valid >= P.MIN_EPOCHS)]\n        n = k.utype.value_counts()\n        tot, cls = len(k), n.get(\"ww\", 0) + n.get(\"nw\", 0)\n        wf.append({\"data\": lab, \"reading\": g3, \"ww\": n.get(\"ww\", 0), \"nw\": n.get(\"nw\", 0), \"unclassified\": n.get(\"na\", 0),\n                   \"ww % of all\": round(100 * n.get(\"ww\", 0) / tot, 1), \"nw % of all\": round(100 * n.get(\"nw\", 0) / tot, 1),\n                   \"ww % of ww+nw\": round(100 * n.get(\"ww\", 0) / cls, 1), \"nw % of ww+nw\": round(100 * n.get(\"nw\", 0) / cls, 1)})\nprint(pd.DataFrame(wf).to_string(index=False))\nprint(\"expected: ww 19,186 ± 1,919, nw 4,200 ± 420, unclassified 862 ± 86, ww 81.1 ± 8.1 %, nw 17.7 ± 1.8 %\")\nk = UK[UK.n_valid >= P.MIN_EPOCHS]\nh, e = np.histogram(k.ptt, np.arange(0, 1.6, 0.02))\nprint(\"\\nHistogram of peak-to-trough (ms, 0.02-ms bins), 001260 + 000473, reading (b); units beyond 1.6 ms:\",\n      int((k.ptt >= 1.6).sum()))\nlo_peak = e[np.argmax(h[e[:-1] < 0.38])]; hi_peak = e[e[:-1] >= 0.43][np.argmax(h[e[:-1] >= 0.43])]\nvalley = e[(e[:-1] >= 0.3) & (e[:-1] < 0.5)][np.argmin(h[(e[:-1] >= 0.3) & (e[:-1] < 0.5)])]\nprint(f\"mode below 0.38 ms at {lo_peak:.2f}, mode above 0.43 ms at {hi_peak:.2f}, minimum between 0.30 and 0.50 ms at {valley:.2f} ms;\"\n      f\" counts at the modes {h.max()} and {h[e[:-1] < 0.38].max()}, at the minimum {h[(e[:-1] >= 0.3) & (e[:-1] < 0.5)].min()}\")\nfig, ax = plt.subplots(figsize=(6, 3))\nax.bar(e[:-1], h, width=0.02, align=\"edge\", color=\"0.4\")\nax.axvline(0.38, color=\"tab:blue\"); ax.axvline(0.43, color=\"tab:red\")\nax.set_xlabel(\"peak-to-trough (ms)\"); ax.set_ylabel(\"units\"); ax.set_title(\"001260 + 000473, units with >= 12 active epochs\")\nplt.show()\n''', [\"claim:fig1h-waveform-classes\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## fig1i-nw-higher-metrics\n\n> Narrow-waveform units have significantly higher firing rates, burstiness and memory than\n> wide-waveform units.\n\nMixed model Metric ~ 1 + Unittype + (1|Mouse) per metric (Methods, equation 6), fitted with\nstatsmodels (REML). The paper's Kenward-Roger F test is not available there; the Wald test of the\nunit-type coefficient is used (with thousands of units and 40 mice the degrees of freedom are\nlarge either way). With one comparison per metric Tukey's correction changes nothing.\n''')\n\ncode(r'''\ncl = U[(U.n_valid >= P.MIN_EPOCHS) & U.utype.isin([\"ww\", \"nw\"])].dropna(subset=[\"log10FR\", \"B\", \"M\"])\nrows = []\nfor m in [\"log10FR\", \"B\", \"M\"]:\n    f, r2 = P.mixed(cl, f'{m} ~ C(utype, Treatment(\"ww\"))')\n    rows.append({\"metric\": m, \"nw - ww estimate\": f.params.iloc[1], \"p\": f.pvalues.iloc[1],\n                 \"median ww\": cl[cl.utype == \"ww\"][m].median(), \"median nw\": cl[cl.utype == \"nw\"][m].median(),\n                 \"n ww\": int((cl.utype == \"ww\").sum()), \"n nw\": int((cl.utype == \"nw\").sum())})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"mice:\", cl.subject.nunique())\nprint(\"\\nPer setting (median nw minus median ww):\")\nprint(cl.groupby([\"setting\", \"utype\"])[[\"log10FR\", \"B\", \"M\"]].median().unstack().pipe(\n    lambda d: pd.DataFrame({m: d[(m, \"nw\")] - d[(m, \"ww\")] for m in [\"log10FR\", \"B\", \"M\"]})).round(3).to_string())\n# variant: the code drops units with log10FR < 0.1\ncv = cl[cl.log10FR >= 0.1]\nprint(\"\\nVariant, units with log10FR >= 0.1 only:\")\nfor m in [\"log10FR\", \"B\", \"M\"]:\n    f, _ = P.mixed(cv, f'{m} ~ C(utype, Treatment(\"ww\"))')\n    print(f\"  {m}: nw - ww = {f.params.iloc[1]:.4f}, p = {f.pvalues.iloc[1]:.2g}, n = {len(cv)}\")\n''', [\"claim:fig1i-nw-higher-metrics\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## extfig1d-sleep-like-differ\n\n> Firing metrics in sleep-like epochs differ from those in active spontaneous epochs, which is\n> why sleep-like epochs are excluded.\n\nww units with at least 12 active epochs (active sample) and ww units with at least 12 sleep-like\nepochs of at least 6 spikes (sleep-like sample), Metric ~ 1 + EpochType + (1|Mouse) (Methods,\nequation 7). Sleep-like periods from the Methods' detector; the code's detector as a variant.\n''')\n\ncode(r'''\ndef epoch_type_models(Ux):\n    ww_ = Ux[Ux.utype == \"ww\"]\n    a = ww_[ww_.n_valid >= P.MIN_EPOCHS][[\"subject\", \"log10FR\", \"B\", \"M\"]].assign(epoch=\"active\")\n    s = ww_[ww_.n_valid_sleep >= P.MIN_EPOCHS][[\"subject\", \"log10FR_sleep\", \"B_sleep\", \"M_sleep\"]]\n    s = s.rename(columns=lambda c: c.replace(\"_sleep\", \"\")).assign(epoch=\"sleep\")\n    L = pd.concat([a, s]).dropna()\n    rows = []\n    for m in [\"log10FR\", \"B\", \"M\"]:\n        f, _ = P.mixed(L, f\"{m} ~ C(epoch)\")\n        rows.append({\"metric\": m, \"sleep - active\": f.params.iloc[1], \"p\": f.pvalues.iloc[1],\n                     \"median active\": a[m].median(), \"median sleep\": s[m].median()})\n    return pd.DataFrame(rows), len(a), len(s)\n\nres, na_, ns_ = epoch_type_models(U)\nprint(f\"Methods detector: {na_} ww units with >= 12 active epochs, {ns_} with >= 12 sleep-like epochs \"\n      \"(paper, all of dataset KI: 19,186 and 11,599)\")\nprint(res.to_string(index=False))\nrecs_code = P.classify_epochs([dict(r) for r in recs], detector=\"code\")\nU_code = P.unit_table(recs_code)\nres_c, na_c, ns_c = epoch_type_models(U_code)\nprint(f\"\\nVariant, the code's detector: {na_c} and {ns_c} units\")\nprint(res_c.to_string(index=False))\n''', [\"claim:extfig1d-sleep-like-differ\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## extfig1-epoch-counts\n\n> Sleep-like episodes occupy a median 6% (IQR 0 to 18%) of recording time; sessions hold a median\n> 227 (IQR 172 to 284) spontaneous active epochs and 19 (IQR 1 to 84) sleep-like epochs.\n\nReadings of \"recording session\": one probe recording (file), or one session of up to three\nprobes (subject and date; time fraction and epochs from the session's first probe, as all\nprobes of a session share onsets). The recording time is from the first to the last spike.\n''')\n\ncode(r'''\ndef epoch_table(recs_):\n    rows = []\n    for r in recs_:\n        sl = r[\"sleep\"]\n        frac = 0.0 if sl is None or len(sl) == 0 else (np.minimum(sl[:, 1], r[\"t1\"]) - np.maximum(sl[:, 0], r[\"t0\"])).clip(0).sum() / (r[\"t1\"] - r[\"t0\"])\n        rows.append({\"session\": r[\"session\"], \"day\": r[\"session\"].split(\"-\")[0], \"sleep %\": 100 * frac,\n                     \"active epochs\": int((r[\"state\"] == \"active\").sum()), \"sleep-like epochs\": int((r[\"state\"] == \"sleep\").sum())})\n    return pd.DataFrame(rows)\n\ndef iqr_str(x):\n    q = np.percentile(x, [25, 50, 75])\n    return f\"{q[1]:.1f} (IQR {q[0]:.1f} to {q[2]:.1f})\"\n\nfor det, rr in [(\"Methods detector\", recs), (\"code's detector\", recs_code)]:\n    et = epoch_table(rr)\n    per_day = et.groupby(\"day\").first()\n    print(det)\n    for nm, d in [(\"per probe recording (n=%d)\" % len(et), et), (\"per session (n=%d)\" % len(per_day), per_day)]:\n        print(f\"  {nm}: sleep-like time {iqr_str(d['sleep %'])} %, active epochs {iqr_str(d['active epochs'])}, \"\n              f\"sleep-like epochs {iqr_str(d['sleep-like epochs'])}\")\n    print(\"  ww units with >= 12 sleep-like epochs of >= 6 spikes:\",\n          int(((U if det.startswith('M') else U_code).query(\"utype == 'ww'\").n_valid_sleep >= P.MIN_EPOCHS).sum()))\nprint(\"expected: 6 ± 0.6 %, 227 ± 22.7 active, 19 ± 1.9 sleep-like epochs, 11,599 ± 1,160 ww units (all of dataset KI)\")\net = epoch_table(recs)\nprint(\"\\nRecordings with more than half of their time sleep-like:\", int((et[\"sleep %\"] > 50).sum()), \"of\", len(et))\nprint(et.sort_values(\"sleep %\", ascending=False).head(12).round(1).to_string(index=False))\net473 = epoch_table(recs473)\nprint(\"\\n000473 (25 aversion recordings), Methods detector:\", \"sleep-like time\", iqr_str(et473[\"sleep %\"]),\n      \"%, active epochs\", iqr_str(et473[\"active epochs\"]), \", sleep-like epochs\", iqr_str(et473[\"sleep-like epochs\"]))\n''', [\"claim:extfig1-epoch-counts\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## extfig1f-burstiness-memory-uncorrelated\n\n> Across ww units, a linear correlation does not reveal a dependence between burstiness and memory.\n\nA claim of absence, judged on the paper's test: B ~ 1 + M + (1|Mouse) across all ww units\n(Methods, equation 8), p < 0.05.\n''')\n\ncode(r'''\nww_all = U[(U.utype == \"ww\") & (U.n_valid >= P.MIN_EPOCHS)].dropna(subset=[\"log10FR\", \"B\", \"M\"]).copy()\nfor form in [\"B ~ M\", \"M ~ B\", \"B ~ log10FR\", \"M ~ log10FR\"]:\n    f, r2 = P.mixed(ww_all, form)\n    print(f\"{form}: slope {f.params.iloc[1]:.4f}, p = {f.pvalues.iloc[1]:.3g}, marginal R2 = {r2:.4f}, n = {len(ww_all)}\")\nprint(\"Pearson r(B, M) across ww units:\", round(stats.pearsonr(ww_all.B, ww_all.M)[0], 3))\n''', [\"claim:extfig1f-burstiness-memory-uncorrelated\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## The ww and nw SOMs and their categories\n\nTrained on all ww (or nw) units with at least 12 active epochs, all regions and layers (code\n`somsettings_carlenSpont.yml`: layerlist all). The two readings of which retrained cluster is\nwhich category (claims file, G2) are shown with each cluster's median metrics.\n''')\n\ncode(r'''\nfit_ww = P.fit_categories(ww_all, 400, 8)\nww_all[\"cat_a\"], ww_all[\"cat_b\"], ww_all[\"node\"] = fit_ww[\"cat_a\"], fit_ww[\"cat_b\"], fit_ww[\"node\"]\nprint(\"ww SOM grid\", fit_ww[\"som\"][\"shape\"], \"=\", fit_ww[\"som\"][\"W\"].shape[0], \"nodes (code's get_kshape rounds up from 400)\")\ntab = fit_ww[\"med\"].assign(reading_a=fit_ww[\"map_a\"], reading_b=fit_ww[\"map_b\"],\n                           units=np.bincount(fit_ww[\"lab\"][fit_ww[\"node\"]], minlength=8))\nprint(tab.sort_values(\"reading_b\").round(3).to_string())\nprint(\"\\nText: 1-3 low rate regular (1 most regular), 4-6 high rate (4 Poissonian, 6 bursty), 7-8 low rate bursty\")\nprint(\"Clusters given the same number by both readings:\", int((fit_ww[\"map_a\"] == fit_ww[\"map_b\"]).sum()), \"of 8\")\nnw_all = U[(U.utype == \"nw\") & (U.n_valid >= P.MIN_EPOCHS)].dropna(subset=[\"log10FR\", \"B\", \"M\"]).copy()\nfit_nw = P.fit_categories(nw_all, 220, 5)\nnw_all[\"cat_a\"] = fit_nw[\"cat_a\"]\nprint(\"\\nnw SOM grid\", fit_nw[\"som\"][\"shape\"], \"| clusters with the code's numbering (reading a):\")\nprint(fit_nw[\"med\"].assign(reading_a=fit_nw[\"map_a\"], units=np.bincount(fit_nw[\"lab\"][fit_nw[\"node\"]], minlength=5)).round(3).to_string())\n''')\n\nmd(r'''\n## fig2a-som-memory-burstiness\n\n> On the ww SOM, burstiness and firing rate vary along perpendicular gradients, while high memory\n> occurs only with medium to low burstiness, so high memory and high burstiness are mutually\n> exclusive.\n''')\n\ncode(r'''\nWd = fit_ww[\"som\"][\"W\"] * fit_ww[\"sd\"] + fit_ww[\"mu\"]\npos = fit_ww[\"som\"][\"pos\"]\nang, gB, gF = P.gradient_angle(pos, Wd[:, 1], Wd[:, 0])\nprint(f\"angle between the B and log10FR gradients: {ang:.1f} degrees (criterion 60 to 120)\")\nprint(\"node prototypes: log10FR\", rng_str(Wd[:, 0]), \"| B\", rng_str(Wd[:, 1]), \"| M\", rng_str(Wd[:, 2]))\nq75B = np.quantile(Wd[:, 1], 0.75)\nfor q, lab in [(0.9, \"(a) top 10%\"), (0.75, \"(b) top 25%\")]:\n    top = Wd[:, 2] >= np.quantile(Wd[:, 2], q)\n    print(f\"{lab} memory nodes: {top.sum()}, of which in the top quartile of node B: {(Wd[top, 1] >= q75B).sum()} \"\n          f\"(their B {np.round(np.sort(Wd[top, 1])[-3:], 3)}, top-quartile threshold {q75B:.3f})\")\nprint(\"Spearman r of node M and node B:\", round(stats.spearmanr(Wd[:, 2], Wd[:, 1])[0], 3))\nfig, axs = plt.subplots(1, 3, figsize=(12, 3.5))\nfor ax, j, nm in zip(axs, range(3), [\"log10FR\", \"B\", \"M\"]):\n    sc = ax.scatter(pos[:, 0], pos[:, 1], c=Wd[:, j], marker=\"h\", s=60, cmap=\"viridis\"); ax.set_title(nm); plt.colorbar(sc, ax=ax)\n    ax.set_aspect(\"equal\"); ax.axis(\"off\")\nplt.show()\n''', [\"claim:fig2a-som-memory-burstiness\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## fig2b-pfc-regular-territory\n\n> PFC ww units are widely spread on the SOM, with many matching regular-firing (low burstiness)\n> nodes and few in anti-memory territory, while units from other regions populate different\n> territories.\n''')\n\ncode(r'''\npfc, oth = ww_all[ww_all.is_pfc], ww_all[~ww_all.is_pfc]\nprint(f\"PFC share of the ww SOM units: {100 * ww_all.is_pfc.mean():.1f} % ({len(pfc)} of {len(ww_all)}); expected 54 ± 5.4\")\nmw = stats.mannwhitneyu(pfc.B, oth.B, alternative=\"two-sided\")\nprint(f\"median B: PFC {pfc.B.median():.4f}, other {oth.B.median():.4f}, Mann-Whitney p = {mw.pvalue:.3g}\")\ntabm = np.array([[(pfc.M < 0).sum(), (pfc.M >= 0).sum()], [(oth.M < 0).sum(), (oth.M >= 0).sum()]])\nchi = stats.chi2_contingency(tabm)\nprint(f\"fraction M < 0: PFC {(pfc.M < 0).mean():.3f}, other {(oth.M < 0).mean():.3f}, chi-square p = {chi[1]:.3g}\")\nprint(\"nodes hit by PFC units:\", pfc.node.nunique(), \"of\", fit_ww[\"som\"][\"W\"].shape[0], \"| by other units:\", oth.node.nunique())\nprint(\"\\nPer setting:\")\nprint(ww_all.groupby([\"setting\", \"is_pfc\"]).agg(medB=(\"B\", \"median\"), fracMneg=(\"M\", lambda x: (x < 0).mean()), n=(\"B\", \"size\")).round(3).unstack().to_string())\n''', [\"claim:fig2b-pfc-regular-territory\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## fig2e-category-stability\n\n> About 57% of ww units keep their category from one block of about 50 spontaneous epochs to the\n> next, far above the 18% expected by chance from the marginal distributions.\n\nBlocks: where the trials table's `Block` column marks runs of trials (Aversion, Context, Opto\nand part of Passive), each run is a block, runs of more than 75 epochs split in two; elsewhere\nconsecutive blocks of 50 onsets (assumption, as the files do not say which recordings had an\ninherent block structure). Block metrics need at least 12 active epochs of at least 6 spikes\n(Methods); the code's minimum of 3 is a variant. Stability does not depend on which cluster is\ngiven which number, so G2 does not apply.\n''')\n\ncode(r'''\nprint(\"Block structure per file:\", pd.Series([r[\"blockmode\"] for r in recs]).value_counts().to_dict(),\n      \"| blocks per file:\", rng_str([len(np.unique(r[\"blocks\"])) for r in recs]))\nbc = P.block_categories(recs, ww_all, fit_ww)\nprint(\"unit-blocks:\", len(bc), \"| units with at least one block:\", bc.groupby([\"session\", \"unit_id\"]).ngroups,\n      \"| epochs per analysed block (median, IQR):\", np.percentile(bc.n_epochs, [50, 25, 75]))\nMs = P.transitions(bc, \"cat_b\", 8)\nst_t = pd.DataFrame([{\"transition\": t, \"units\": int(M.sum()), \"stability\": P.stability(M)[0], \"chance\": P.stability(M)[1]}\n                     for t, M in Ms.items()])\nprint(st_t.round(3).to_string(index=False))\nMsum = sum(Ms.values())\nprint(f\"(a) mean over transitions: stability {st_t.stability.mean():.3f}, chance {st_t.chance.mean():.3f}\")\nprint(f\"(b) pooled matrix: stability {P.stability(Msum)[0]:.3f}, chance {P.stability(Msum)[1]:.3f}\")\nprint(\"expected 0.57 ± 0.057 and 0.18 ± 0.018\")\nbc3 = P.block_categories(recs, ww_all, fit_ww, min_valid=3)\nMs3 = P.transitions(bc3, \"cat_b\", 8)\ns3 = [P.stability(M) for M in Ms3.values()]\nprint(f\"\\nVariant, blocks with >= 3 valid epochs: mean {np.mean([s[0] for s in s3]):.3f} (chance {np.mean([s[1] for s in s3]):.3f}),\"\n      f\" pooled {P.stability(sum(Ms3.values()))[0]:.3f}\")\nbcs = bc.merge(ww_all[[\"session\", \"unit_id\", \"setting\"]], on=[\"session\", \"unit_id\"])\nprint(\"\\nPooled stability by setting:\")\nfor sname, g in bcs.groupby(\"setting\"):\n    Mg = sum(P.transitions(g, \"cat_b\", 8).values())\n    if np.sum(Mg) > 0:\n        print(f\"  {sname}: {P.stability(Mg)[0]:.3f} (chance {P.stability(Mg)[1]:.3f}, {int(Mg.sum())} transitions)\")\n''', [\"claim:fig2e-category-stability\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## fig2f-low-rate-less-stable\n\n> Block-wise category assignment is less stable for low-rate categories (1 to 3, 7 and 8) than\n> for high-rate categories, and low-rate regular categories 1 to 3 mostly transition among\n> themselves, as do the low-rate bursty categories 7 and 8.\n''')\n\ncode(r'''\ndef fig2f_parts(bc_, cat):\n    M = sum(P.transitions(bc_, cat, 8).values())\n    Pm = M / M.sum(1, keepdims=True)\n    X = P.coincidence(M)\n    low, high = [0, 1, 2, 6, 7], [3, 4, 5]\n    d, dx = np.diag(Pm), np.diag(X)\n    part1 = d[low].mean() < d[high].mean()\n    part1x = dx[low].mean() < dx[high].mean()\n    part2 = []\n    for grp in ([0, 1, 2], [6, 7]):\n        for i in grp:\n            others = [j for j in grp if j != i]\n            out = [j for j in range(8) if j not in grp]\n            part2.append(Pm[i, others].sum() > Pm[i, out].max())\n    return Pm, X, d, dx, part1, part1x, part2\n\nfor cat in [\"cat_a\", \"cat_b\"]:\n    Pm, X, d, dx, p1, p1x, p2 = fig2f_parts(bc, cat)\n    print(f\"G2 reading {cat[-1]}: diagonal of P by category 1..8: {np.round(d, 3)}\")\n    print(f\"   mean diagonal low-rate (1-3,7,8) {d[[0,1,2,6,7]].mean():.3f} vs high-rate (4-6) {d[[3,4,5]].mean():.3f} -> part 1 {p1};\"\n          f\" coincidence diagonal {np.round(dx, 3)} -> {p1x}\")\n    print(f\"   part 2 (within-group probability above any single outside category), categories 1,2,3,7,8: {p2}\")\n    print(pd.DataFrame(Pm, index=range(1, 9), columns=range(1, 9)).round(2).to_string())\n''', [\"claim:fig2f-low-rate-less-stable\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## Region enrichment of ww categories\n\nDeep-layer units for cortical regions and all units elsewhere, against all such units\n(the code's refall), PFC subregions and the code's parent regions, regions with more than 20\nunits, 1,000 shuffles within each behavioral setting. G1: (a) five groups, Opto merged into\nPassive (code); (b) six settings. Both G2 readings.\n''')\n\ncode(r'''\nww_all[\"setting5\"] = ww_all.setting.replace({\"Opto\": \"Passive\"})\nsel = ww_all[(~ww_all.cortical) | ww_all.deep]\ncnt = sel.region.value_counts()\nregs = cnt[(cnt > 20) & (cnt.index != \"other\")].index\nprint(\"units:\", len(sel), \"| regions with more than 20 units:\", len(regs))\nprint(cnt[regs].to_string())\nENR = {}\nfor g1, gcol in [(\"a\", \"setting5\"), (\"b\", \"setting\")]:\n    for g2 in [\"a\", \"b\"]:\n        E, Pv, Xc = P.escore(sel.region.values, sel[\"cat_\" + g2].values, sel[gcol].values, 1000, seed=11,\n                             pops=list(regs) + [\"other\"], attrs=range(1, 9))\n        ENR[(g1, g2)] = (E.loc[regs], Pv.loc[regs])\nshow = [\"ILA\", \"PL\", \"ACAd\", \"ACAv\", \"ORBm\", \"ORBvl\", \"ORBl\", \"MOs\", \"AIv\", \"AId\", \"FRP\", \"TH\", \"HPF\"]\nfor key, (E, Pv) in ENR.items():\n    print(f\"\\nG1 {key[0]}, G2 {key[1]}: E-scores (* P < 0.05)\")\n    print(E.loc[[r for r in show if r in E.index]].round(1).astype(str).where(Pv.loc[[r for r in show if r in E.index]] >= 0.05,\n          E.loc[[r for r in show if r in E.index]].round(1).astype(str) + \"*\").to_string())\n''')\n\nmd(r'''\n## fig2g-pfc-regular-enrichment\n\n> Most PFC subregions (ILA, PL, ACAd, ACAv, ORBm and ORBvl) are enriched in low-rate,\n> regular-firing ww units (categories 1 to 3).\n''')\n\ncode(r'''\nsix = [\"ILA\", \"PL\", \"ACAd\", \"ACAv\", \"ORBm\", \"ORBvl\"]\nrows = []\nfor (g1, g2), (E, Pv) in ENR.items():\n    ra = (E.loc[six, [1, 2, 3]].sum(1) > 0)\n    rb = ((E.loc[six, [1, 2, 3]] > 0) & (Pv.loc[six, [1, 2, 3]] < 0.05)).any(axis=1)\n    rows.append({\"G1\": g1, \"G2\": g2, **{f\"(a) {r}\": bool(ra[r]) for r in six}, \"(a) n\": int(ra.sum()),\n                 **{f\"(b) {r}\": bool(rb[r]) for r in six}, \"(b) n\": int(rb.sum())})\nres2g = pd.DataFrame(rows)\nprint(res2g.to_string(index=False))\nfor (g1, g2), (E, Pv) in ENR.items():\n    print(f\"G1 {g1} G2 {g2}: sum of E-scores of categories 1-3:\", E.loc[six, [1, 2, 3]].sum(1).round(1).to_dict())\n''', [\"claim:fig2g-pfc-regular-enrichment\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## fig2g-ila-pl-category1\n\n> ILA and PL are both strongly and significantly enriched in the most regular-firing category 1.\n''')\n\ncode(r'''\nfor (g1, g2), (E, Pv) in ENR.items():\n    print(f\"G1 {g1} G2 {g2}: category 1 E-score ILA {E.loc['ILA', 1]:.2f} (P {Pv.loc['ILA', 1]:.3f}), \"\n          f\"PL {E.loc['PL', 1]:.2f} (P {Pv.loc['PL', 1]:.3f})\")\n''', [\"claim:fig2g-ila-pl-category1\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## fig2g-bursty-orbl-mos-aiv\n\n> ORBl, MOs and AIv are significantly enriched in bursty category 8 units, setting them apart\n> from the activity-defined prefrontal entity.\n''')\n\ncode(r'''\nfor (g1, g2), (E, Pv) in ENR.items():\n    print(f\"G1 {g1} G2 {g2}: category 8 E-score \" + \", \".join(\n        f\"{r} {E.loc[r, 8]:.2f} (P {Pv.loc[r, 8]:.3f})\" if r in E.index else f\"{r} not analysed\" for r in [\"ORBl\", \"MOs\", \"AIv\"]))\n''', [\"claim:fig2g-bursty-orbl-mos-aiv\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## fig2g-th-hpf-bursty\n\n> Thalamus and hippocampal formation are strongly and significantly enriched in bursty units\n> (categories 6 to 8), unlike the PFC.\n''')\n\ncode(r'''\nfor (g1, g2), (E, Pv) in ENR.items():\n    for r in [\"TH\", \"HPF\"]:\n        sig = [(E.loc[r, c] > 0) & (Pv.loc[r, c] < 0.05) for c in [6, 7, 8]]\n        print(f\"G1 {g1} G2 {g2} {r}: E-scores 6-8 {E.loc[r, [6, 7, 8]].round(2).tolist()}, P {Pv.loc[r, [6, 7, 8]].round(3).tolist()};\"\n              f\" (a) all three {all(sig)}, (b) at least one {any(sig)}\")\n''', [\"claim:fig2g-th-hpf-bursty\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## extfig3f-layer-enrichment\n\n> Superficial cortical layers (L2/3) are enriched in bursty ww units, while deep layers (L5 to 6)\n> are enriched in regular-firing ww units.\n\nAll cortical ww units with a layer, groups = region × setting (Methods, Group-bias control).\n''')\n\ncode(r'''\ncx = ww_all[ww_all.cortical & (ww_all.layer != \"NA\")].copy()\ncx[\"L\"] = cx.layer.str.replace(r\"^6[ab]$\", \"6\", regex=True)\nprint(\"layer labels:\", cx.L.value_counts().to_dict())\nfor g1, gcol in [(\"a\", \"setting5\"), (\"b\", \"setting\")]:\n    grp = cx.region + \"|\" + cx[gcol]\n    for g2 in [\"a\", \"b\"]:\n        E, Pv, Xc = P.escore(cx.L.values, cx[\"cat_\" + g2].values, grp.values, 1000, seed=12, attrs=range(1, 9))\n        sigpos = (E > 0) & (Pv < 0.05)\n        ok23 = sigpos.loc[\"2/3\", [6, 7, 8]].any() if \"2/3\" in E.index else False\n        ok5 = sigpos.loc[\"5\", [1, 2, 3]].any(); ok6 = sigpos.loc[\"6\", [1, 2, 3]].any()\n        print(f\"\\nG1 {g1}, G2 {g2}: L2/3 enriched in 6-8: {ok23}; L5 in 1-3: {ok5}; L6 in 1-3: {ok6}\")\n        print(E.round(1).astype(str).where(Pv >= 0.05, E.round(1).astype(str) + \"*\").to_string())\n''', [\"claim:extfig3f-layer-enrichment\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## extfig5g-nw-enrichment\n\n> Among nw units, ILA, PL and ACAd/v are significantly enriched in high-rate, regular-firing units\n> with high memory, and ORBl in high-rate, bursty units.\n\nThe regular high-memory nw category is the one with median log10FR above the median over all nw\nunits and the lowest median B; the bursty one has median log10FR above that median and the\nhighest median B (claims file, by category medians).\n''')\n\ncode(r'''\nmed_nw = fit_nw[\"med\"].copy()\nmed_nw[\"cat\"] = fit_nw[\"map_a\"]\nmed_nw = med_nw.set_index(\"cat\").sort_index()\nhi_rate = med_nw[med_nw.log10FR > nw_all.log10FR.median()]\nreg_cat, burst_cat = hi_rate.B.idxmin(), hi_rate.B.idxmax()\nprint(med_nw.round(3).to_string())\nprint(f\"median log10FR of nw units {nw_all.log10FR.median():.3f}; regular high-memory category {reg_cat} \"\n      f\"(M {med_nw.loc[reg_cat, 'M']:.3f}), bursty category {burst_cat}\")\nnw_all[\"setting5\"] = nw_all.setting.replace({\"Opto\": \"Passive\"})\nseln = nw_all[(~nw_all.cortical) | nw_all.deep]\ncntn = seln.region.value_counts()\nregs_n = cntn[(cntn > 20) & (cntn.index != \"other\")].index\nprint(\"nw regions with more than 20 units:\", len(regs_n), cntn[regs_n].to_dict())\nENRN = {}\nfor g1, gcol in [(\"a\", \"setting5\"), (\"b\", \"setting\")]:\n    E, Pv, _ = P.escore(seln.region.values, seln.cat_a.values, seln[gcol].values, 1000, seed=13,\n                        pops=list(regs_n) + [\"other\"], attrs=range(1, 6))\n    ENRN[g1] = (E.loc[regs_n], Pv.loc[regs_n])\n    sp = (E > 0) & (Pv < 0.05)\n    g = lambda r, c: bool(sp.loc[r, c]) if r in sp.index else False\n    p1 = g(\"ILA\", reg_cat) and g(\"PL\", reg_cat) and (g(\"ACAd\", reg_cat) or g(\"ACAv\", reg_cat))\n    p2 = g(\"ORBl\", burst_cat)\n    print(f\"\\nG1 {g1}: part 1 (ILA, PL, ACAd or ACAv in category {reg_cat}) {p1}; part 2 (ORBl in {burst_cat}) {p2}\")\n    print(E.loc[regs_n].round(1).astype(str).where(Pv.loc[regs_n] >= 0.05, E.loc[regs_n].round(1).astype(str) + \"*\").to_string())\n''', [\"claim:extfig5g-nw-enrichment\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## fig2j-nw-ww-correspondence\n\n> Brain (sub)regions enriched in low-rate, regular-firing ww units are enriched in high-rate,\n> regular-firing nw units, and regions enriched in low-rate bursty ww units are enriched in\n> high-rate bursty nw units.\n''')\n\ncode(r'''\nfor g1 in [\"a\", \"b\"]:\n    En = ENRN[g1][0]\n    for g2 in [\"a\", \"b\"]:\n        Ew = ENR[(g1, g2)][0]\n        common = [r for r in En.index if r in Ew.index]\n        R = pd.DataFrame([[stats.pearsonr(Ew.loc[common, cw], En.loc[common, cn])[0] for cn in range(1, 6)] for cw in range(1, 9)],\n                         index=[f\"ww{c}\" for c in range(1, 9)], columns=[f\"nw{c}\" for c in range(1, 6)])\n        r_reg = R.loc[[\"ww1\", \"ww2\", \"ww3\"], f\"nw{reg_cat}\"].mean()\n        r_bur = R.loc[[\"ww7\", \"ww8\"], f\"nw{burst_cat}\"].mean()\n        print(f\"G1 {g1}, G2 {g2}: {len(common)} regions (paper 9); mean r ww1-3 vs nw{reg_cat} = {r_reg:.3f}; \"\n              f\"mean r ww7-8 vs nw{burst_cat} = {r_bur:.3f}\")\n        if g2 == \"b\":\n            print(R.round(2).to_string())\n''', [\"claim:fig2j-nw-ww-correspondence\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## Harris hierarchy (Fig. 3)\n\nThe Harris et al. 2019 scores as the code reads them. Populations are the cortical areas with a\nscore (deep layers), all other units form one rest population (code\n`harris_vs_enrichment.py`); E-scores grouped by setting (Methods), and without groups as the\ncode's Fig. 3 script does (variant). Areas with more than 20 units.\n''')\n\ncode(r'''\nharris = P.harris_table()\nprint(\"Harris cortical areas in the table:\", len(harris))\nhsel = ww_all.copy()\nhsel[\"areaH\"] = np.where(hsel.area.isin(harris.index) & hsel.deep, hsel.area, \"NA\")\nhc = hsel.areaH.value_counts()\nareasH = [a for a in hc.index if a != \"NA\" and hc[a] > 20]\nprint(\"areas with a score and more than 20 deep ww units:\", len(areasH), \"(paper 17)\")\nprint(pd.DataFrame({\"units\": hc[areasH], \"harris\": harris[areasH]}).sort_values(\"harris\").round(3).to_string())\nHAR = {}\nfor lab, grp in [(\"G1 a\", hsel.setting.replace({\"Opto\": \"Passive\"}).values), (\"G1 b\", hsel.setting.values),\n                 (\"no groups\", np.zeros(len(hsel)))]:\n    for g2 in [\"a\", \"b\"]:\n        E, Pv, _ = P.escore(hsel.areaH.values, hsel[\"cat_\" + g2].values, grp, 1000, seed=14, pops=areasH + [\"NA\"], attrs=range(1, 9))\n        E = E.loc[areasH]\n        HAR[(lab, g2)] = (E, Pv.loc[areasH])\n        rr = [stats.pearsonr(harris[areasH], E[c]) for c in range(1, 9)]\n        print(f\"{lab}, G2 {g2}: r by category \" + \", \".join(f\"{c}: {r[0]:.2f} (p {r[1]:.3f})\" for c, r in zip(range(1, 9), rr)))\n''')\n\nmd(r'''\n## fig3a-harris-regular-positive\n\n> In dataset KI, enrichment of cortical (sub)regions in low-rate, regular-firing units\n> (categories 1 to 3, category 2 shown) correlates positively with the Harris cortical hierarchy\n> score, driven by the split between low-hierarchy sensory regions and high-hierarchy PFC\n> subregions.\n''')\n\ncode(r'''\ndef harris_r(E, cats, areas=None):\n    a = areasH if areas is None else areas\n    return {c: stats.pearsonr(harris[a], E.loc[a, c]) for c in cats}\n\nfor key, (E, Pv) in HAR.items():\n    rr = harris_r(E, [1, 2, 3])\n    ok = rr[2][0] > 0 and rr[2][1] < 0.05 and rr[1][0] > 0 and rr[3][0] > 0\n    part = rr[2][0] > 0 and rr[2][1] < 0.05\n    print(f\"{key}: r1 {rr[1][0]:.2f} (p {rr[1][1]:.3f}), r2 {rr[2][0]:.2f} (p {rr[2][1]:.3f}), r3 {rr[3][0]:.2f} (p {rr[3][1]:.3f})\"\n          f\" -> all {ok}, category 2 alone {part}\")\nE, _ = HAR[(\"G1 a\", \"b\")]\npf = [a for a in areasH if a in P.PFC_SUBREGIONS]\nprint(\"\\nG1 a, G2 b: mean category 2 E-score, PFC areas\", round(E.loc[pf, 2].mean(), 2), \"| other areas\",\n      round(E.loc[[a for a in areasH if a not in pf], 2].mean(), 2), \"| Harris score PFC\", round(harris[pf].mean(), 3),\n      \"other\", round(harris[[a for a in areasH if a not in pf]].mean(), 3))\n''', [\"claim:fig3a-harris-regular-positive\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## fig3c-harris-bursty-negative\n\n> Cortical hierarchy correlates even more strongly, and negatively, with enrichment in bursty,\n> low-memory units (categories 6 to 8), in both datasets.\n''')\n\ncode(r'''\nfor key, (E, Pv) in HAR.items():\n    rb, rr = harris_r(E, [6, 7, 8]), harris_r(E, [1, 2, 3])\n    neg = all(rb[c][0] < 0 for c in [6, 7, 8]) and any(rb[c][1] < 0.05 for c in [6, 7, 8])\n    stronger = max(abs(rb[c][0]) for c in [6, 7, 8]) > max(abs(rr[c][0]) for c in [1, 2, 3])\n    print(f\"{key}: r6 {rb[6][0]:.2f} (p {rb[6][1]:.3f}), r7 {rb[7][0]:.2f} (p {rb[7][1]:.3f}), r8 {rb[8][0]:.2f} (p {rb[8][1]:.3f});\"\n          f\" all negative, one significant: {neg}; largest |r| 6-8 above 1-3: {stronger}\")\n''', [\"claim:fig3c-harris-bursty-negative\"])\n\nmd(r'''\n**Result: pending.**\n''')\n\nmd(r'''\n## supptable5-no-hierarchy-within-pfc\n\n> Restricted to PFC subregions, enrichment in unit categories shows no relationship to cortical\n> hierarchy.\n\nA claim of absence: Pearson correlation across the PFC subregions among the areas above, per\ncategory, p < 0.05, no correction.\n''')\n\ncode(r'''\nprint(\"PFC subregions with a Harris score and more than 20 units:\", pf)\nfor key, (E, Pv) in HAR.items():\n    rr = harris_r(E, range(1, 9), pf)\n    sig = [c for c in range(1, 9) if rr[c][1] < 0.05]\n    print(f\"{key}: \" + \", \".join(f\"{c}: {rr[c][0]:.2f} (p {rr[c][1]:.3f})\" for c in range(1, 9)) + f\" -> significant: {sig}\")\n''', [\"claim:supptable5-no-hierarchy-within-pfc\"])\n\nmd(r'''\n**Result: pending.**\n''')\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_cells.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && uv pip install -q nbconvert ipykernel nbformat 2>&1|tail -1; python - <<'EOF'
s=open('/tmp/claude-1001/nb_cells.py').read()
a=s.index("def onset_response"); b=s.index("def tone_contrast")
s=s[:a]+s[b:]
open('/tmp/claude-1001/nb_cells.py','w').write(s)
EOF
python $TMPDIR/build_nb.py && cat > $TMPDIR/devrun.py <<'EOF'
import nbformat, sys
nb=nbformat.read('entries/001260-le-merre-2026/reproduce_le_merre_2026.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code' and 'P.load_all(assets)' in c.source:
        c.source=c.source.replace('recs = P.classify_epochs(P.load_all(assets))',"import pickle; recs = P.classify_epochs(pickle.load(open('/tmp/claude-1001/recs.pkl','rb')))").replace('recs473 = P.classify_epochs(P.load_all(assets473))',"recs473 = P.classify_epochs(pickle.load(open('/tmp/claude-1001/recs473.pkl','rb')))")
nbformat.write(nb,'/tmp/claude-1001/dev.ipynb')
EOF
python $TMPDIR/devrun.py && cd entries/001260-le-merre-2026 && time jupyter nbconvert --to notebook --execute $TMPDIR/dev.ipynb --output $TMPDIR/dev_out.ipynb --ExecutePreprocessor.timeout=1800 2>&1 | tail -5
```

```
76 cells
[32m     11[39m pd.set_option([33m"display.width"[39m, [32m220[39m)
[32m     12[39m pd.set_option([33m"display.max_columns"[39m, [32m40[39m)

[31mModuleNotFoundError[39m: No module named 'pfcki'


real	0m5.854s
user	0m5.351s
sys	0m0.386s
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cd entries/001260-le-merre-2026 && cp $TMPDIR/dev.ipynb ./_dev.ipynb && time jupyter nbconvert --to notebook --execute _dev.ipynb --output $TMPDIR/dev_out.ipynb --ExecutePreprocessor.timeout=1800 2>&1 | tail -5; rm -f _dev.ipynb
```

```
[32m     18[39m print(f"mode below 0.38 ms at {lo_peak:.2f}, mode above 0.43 ms at {hi_peak:.2f}, minimum between 0.30 and 0.50 ms at {valley:.2f} ms;"
[32m     19[39m       f" counts at the modes {h.max()} and {h[e[:-[32m1[39m] < [32m0.38[39m].max()}, at the minimum {h[(e[:-[32m1[39m] >= [32m0.3[39m) & (e[:-[32m1[39m] < [32m0.5[39m)].min()}")

[31mIndexError[39m: boolean index did not match indexed array along axis 0; size of axis is 80 but size of corresponding boolean axis is 79


real	0m54.957s
user	0m8.119s
sys	0m2.195s
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
p='/tmp/claude-1001/nb_cells.py'; s=open(p).read()
old=s[s.index("lo_peak = e[np.argmax"):s.index('fig, ax = plt.subplots(figsize=(6, 3))')]
new='''left = e[:-1]
m_lo, m_hi, m_mid = left < 0.38, left >= 0.43, (left >= 0.3) & (left < 0.5)
lo_peak, hi_peak = left[m_lo][np.argmax(h[m_lo])], left[m_hi][np.argmax(h[m_hi])]
valley = left[m_mid][np.argmin(h[m_mid])]
print(f"mode below 0.38 ms at {lo_peak:.2f} ms ({h[m_lo].max()} units), mode above 0.43 ms at {hi_peak:.2f} ms ({h[m_hi].max()}),"
      f" minimum between 0.30 and 0.50 ms at {valley:.2f} ms ({h[m_mid].min()})")
'''
s=s.replace(old,new); open(p,'w').write(s)
EOF
python $TMPDIR/build_nb.py && python $TMPDIR/devrun.py && cd entries/001260-le-merre-2026 && cp $TMPDIR/dev.ipynb ./_dev.ipynb && time jupyter nbconvert --to notebook --execute _dev.ipynb --output $TMPDIR/dev_out.ipynb --ExecutePreprocessor.timeout=1800 2>&1 | tail -5; rm -f _dev.ipynb
```

```
76 cells
[NbConvertApp] Converting notebook _dev.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 452454 bytes to /tmp/claude-1001/dev_out.ipynb

real	1m24.669s
user	1m22.264s
sys	0m8.679s
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude-1001/dev_out.ipynb',4)
for c in nb.cells[2:]:
    if c.cell_type!='code': continue
    print('=====', c.metadata.get('tags'))
    for o in c.outputs:
        if o.output_type=='stream': print(o.text[:6000])
        elif o.output_type=='error': print('ERROR', o.ename, o.evalue)
EOF
date -u
```

```
<persisted-output>
Output too large (45KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/2a1918e7-9167-4006-bb17-a781d9ea2a7c/tool-results/b3ir3iisd.txt

Preview (first 2KB):
===== ['sanity']
Archive summary: 74 files, 43 subjects
               session subject   setting  units  onsets  cortical_units  duration_min   blocks                                                description
242820_20200526-probe0  242820  Aversion    407     250             219          90.3 inherent Neuropixels recording in mPFC during aversive conditioning
249939_20200611-probe0  249939  Aversion    376     250             161          88.1 inherent Neuropixels recording in mPFC during aversive conditioning
249940_20200610-probe0  249940  Aversion    426     250             165          90.0 inherent Neuropixels recording in mPFC during aversive conditioning
250252_20200609-probe0  250252  Aversion    164     250              59          86.2 inherent Neuropixels recording in mPFC during aversive conditioning
250253_20200609-probe0  250253  Aversion    502     250             241          87.3 inherent Neuropixels recording in mPFC during aversive conditioning
250256_20200610-probe0  250256  Aversion    235     350             108          97.7 inherent Neuropixels recording in mPFC during aversive conditioning
518804_20220228-probe0  518804 Detection    266     274              97          48.6    fifty Neuropixels recording in mPFC during auditory detection ta
518804_20220301-probe0  518804 Detection    394     308             323          55.8    fifty Neuropixels recording in mPFC during auditory detection ta
534133_20220302-probe0  534133 Detection    325     180             140          32.7    fifty Neuropixels recording in mPFC during auditory detection ta
560169_20220506-probe0  560169 Detection    264     302             207          54.9    fifty Neuropixels recording in mPFC during auditory detection ta
560171_20220504-probe0  560171 Detec
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 80,400p /home/runner/.claude/projects/-home-runner-work-encore-encore/2a1918e7-9167-4006-bb17-a781d9ea2a7c/tool-results/b3ir3iisd.txt | grep -v "^ *[0-9A-Z_]*_20[0-9]*-probe[0-9] " | head -260
```

```
===== ['sanity']
Post minus pre rate (Hz per unit) around 10-kHz tone onsets, every sixth file with tones:
               session  true onsets  shifted 1.5 s
files with a larger change at the true onsets than at the shifted ones: 10 of 10

===== ['claim:dataset-ki-counts']
           data                       reading  units  PFC units  PFC %
         001260       (a) ISI violation < 0.1   3781       1915   50.6
         001260 (a) false positive rate < 0.1  10008       4710   47.1
         001260                 (b) all units  14564       7042   48.4
001260 + 000473       (a) ISI violation < 0.1   4820       2639   54.8
001260 + 000473 (a) false positive rate < 0.1  13917       7268   52.2
001260 + 000473                 (b) all units  20354      10900   53.6
recordings (probes): {'001260': 74, '001260 + 000473': 99} | expected 24,248 ± 2,425 units, 52 ± 5.2 % PFC, 99 recordings, 12,674 ± 1,267 PFC units

Variants of the 12-epoch rule, reading (b):
           data  min spikes          epochs  units  PFC %  PFC units
         001260           6          active  14564   48.4       7042
         001260           6 all spontaneous  17205   47.3       8134
         001260           5          active  15303   48.3       7394
[... 240 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 400,700p /home/runner/.claude/projects/-home-runner-work-encore-encore/2a1918e7-9167-4006-bb17-a781d9ea2a7c/tool-results/b3ir3iisd.txt | grep -v "ConvergenceWarning\|fit = smf"
```

```
ORBvl     642
ILA       616
TT        459
ACB       436
ORBl      416
ACAv      329
DP        271
HPF       251
SS        163
TH        157
AId       151
CP        149
ORBm      140
MO        120
FRP        85
AIv        77
PIR        63
EPd        53
AUD        24

[... 279 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap/python; ls flatmaps; grep -n "KMeansConstrained\|size_min\|size_max\|marg\|int(\|200\|nmin\|FRP" flatmaps/*.py utils/tessellation_tools.py | head -40
```

```
calc_flatmap_statsdict.py
compare_flatmap_enrichments.py
compare_flatmaps_spont_resp_task.py
flatmap_rasterization.py
flatmap_tessellation.py
plot_flat_zeta_responder_and_hierarchy.py
plot_flatmap_countstats.py
plot_flatmap_enrichments.py
write_flatmap_enrichment_tables.py
flatmaps/calc_flatmap_statsdict.py:30:get_rois_bool = bool(int(get_rois_bool_str))
flatmaps/calc_flatmap_statsdict.py:37:ncl = int(ncluststr)
flatmaps/calc_flatmap_statsdict.py:101:print('pfc: areas',np.unique([U.area for U in Units_pfc]))
flatmaps/calc_flatmap_statsdict.py:102:print('no pfc areas',np.unique([U.area for U in Units if not S.check_pfc(U.area)]))
flatmaps/calc_flatmap_statsdict.py:103:print('ctx areas',np.unique([U.area for U in Units_ctx]))
flatmaps/compare_flatmap_enrichments.py:87:ncl = int(ncluststr)
flatmaps/compare_flatmap_enrichments.py:181:        ncl = int(ncluststr)
flatmaps/compare_flatmap_enrichments.py:228:x_bounds = np.array([np.nanmin(allX),np.nanmax(allX)])
flatmaps/compare_flatmap_enrichments.py:316:    hdict = {int(float(el[0])): float(el[1]) for el in hdata}
flatmaps/compare_flatmap_enrichments.py:320:    alabs2 = np.array([int(val) for val in alabs])
flatmaps/compare_flatmaps_spont_resp_task.py:24:dpi_png = 200
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap/python; sed -n 30,200p flatmaps/flatmap_tessellation.py
```

```
fig.savefig(figname)
    if closeit: plt.close(fig)


sys.path.append(pathdict['code']['workspace'])
from pfcmap.python.utils import unitloader as uloader
from pfcmap.python import settings as S
from pfcmap.python.utils import tessellation_tools as ttools


rundict_folder = os.path.dirname(rundict_path)
rundict = uloader.get_myrun(rundict_folder,myrun)
#reftag,layerlist,datasets,tasks,tsel,statetag,utypes,nnodes = [rundict[key] for key in ['reftag','layerlist','datasets','tasks','tsel','state','utypes','nnodes']]
#wmetrics,imetrics,wmetr_weights,imetr_weights = [rundict[metrtype][mytag] for mytag in ['features','weights'] for metrtype in ['wmetrics','imetrics']]#not strictly necessary: gets called in uloader



metricsfiles = S.get_metricsfiles_auto(rundict,srcdir,tablepath=pathdict['tablepath'])

Units,somfeats,weightvec =  uloader.load_all_units_for_som(metricsfiles,rundict,check_pfc= (not myrun.count('_brain')),rois_from_path=False)
[... 152 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pfcmap/python; grep -n "def get_clusters" -A25 utils/tessellation_tools.py
```

```
9:def get_clusters(X,NperPatch=100,frac_range=[0.8,1.2]):
10-    n_clusters = int(len(X) / NperPatch)
11-    minsize = NperPatch*frac_range[0]
12-    maxsize = NperPatch*frac_range[1]
13-    if len(X)<=maxsize:
14-        return X.mean(axis=0)[None,:],np.array([0])
15-    if n_clusters * maxsize < len(X):
16-        maxsize = int(np.ceil(len(X)/n_clusters))
17-    clf = KMeansConstrained(n_clusters, size_min=minsize,
18-                            size_max=maxsize)
19-    clf.fit(X)
20-    #cluster_centers_ = clf.cluster_centers_
21-    #labels_ = clf.labels_
22-    return clf.cluster_centers_, clf.labels_
23-
24-def get_voronoi_polygons_outbounded(midpoints,outcoords,print_on=False):
25-    #outcoords = outcoords * np.array([1, v_fac])
26-    outline_pg = shapely.Polygon(outcoords)
27-    centerpts = shapely.MultiPoint(midpoints)
28-    vor_polygons = shapely.voronoi_polygons(centerpts, extend_to=outline_pg)  #
[... 7 more lines not kept]
```

**Agent**

The code's tessellation (`get_clusters`) settles the parcellation details. Writing the link and flatmap cells.

**Agent calls Bash**

```bash
cat >> entries/001260-le-merre-2026/pfcki.py <<'EOF'


def flatmap_polygons(name):
    """Polygons from the Zenodo flatmaps.zip: 'flatmap_PFCregions.h5' (subregions),
    'flatmap_PFCrois.h5' (the 60 GaoROIs), 'flatmap_PFC_ntesselated_obeyRegions_res200.h5'
    (the paper's dataROIs)."""
    import io
    import zipfile
    z = zipfile.ZipFile(io.BytesIO(zenodo_bytes("flatmaps.zip")))
    with h5py.File(io.BytesIO(z.read("flatmaps/" + name)), "r") as f:
        return {k: f[k][()] for k in f.keys()}


def gao_hierarchy():
    import io
    t = pd.read_csv(io.BytesIO(zenodo_bytes("ROI_Gao_hierarchy_index.csv")))
    return pd.Series(t["hierarchy index"].values, index=t["roi"].astype(int))


def in_polygons(uv, polys):
    """Name of the polygon containing each point (first match), or None."""
    import shapely
    out = np.array([None] * len(uv), dtype=object)
    pts = [shapely.Point(p) for p in uv]
    for k, c in polys.items():
        pg = shapely.Polygon(c)
        m = np.array([pg.contains(p) for p in pts])
        out[(out == None) & m] = k  # noqa: E711
    return out


def parcellate(uv, region, per=200, bounds=(160, 240), seed=0):
    """Methods, Parcellation into ROIs of similar unit count: n = int(count / 200) ROIs per
    subregion by constrained k-means of the flatmap positions, FRP not split; a subregion with no
    more units than the upper bound is one ROI, and the upper bound is raised when n ROIs cannot
    hold the units (code utils/tessellation_tools.py get_clusters). Units take the ROI of the
    nearest cluster center in their subregion (the Voronoi cell). Returns ROI labels."""
    from k_means_constrained import KMeansConstrained
    lab = np.array([None] * len(uv), dtype=object)
    for reg in pd.unique(region):
        idx = np.where(region == reg)[0]
        X = uv[idx]
        n = int(len(X) / per)
        lo, hi = bounds
        if reg == "FRP" or len(X) <= hi or n <= 1:
            lab[idx] = f"{reg}-1"
            continue
        if n * hi < len(X):
            hi = int(np.ceil(len(X) / n))
        km = KMeansConstrained(n_clusters=n, size_min=lo, size_max=hi, random_state=seed).fit(X)
        d = ((X[:, None, :] - km.cluster_centers_[None]) ** 2).sum(-1)
        lab[idx] = [f"{reg}-{k + 1}" for k in d.argmin(1)]
    return lab
EOF
cat >> $TMPDIR/nb_cells.py <<'EOF'

md(r'''
## zenodo-unit-link

> Link claim (the registry's): the paper's per-unit metrics files on Zenodo can be matched to the
> dataset's units, and the matched records agree on what both describe.

Records are matched by recording id and unit id. Agreement is checked on the location (area
and layer), the peak-to-trough duration, and the ww/nw label against the Methods thresholds
applied to the dataset's `Peak_to_Trough`. The files' quality flags are compared with the
paper's count of units kept.
''')

code(r'''
Z = P.paper_unit_table()
print("Zenodo metrics files:", Z.session.nunique(), "recordings,", len(Z), "units")
L = U.merge(Z, on=["session", "unit_id"], how="left", indicator=True)
print("dataset units matched:", int((L._merge == "both").sum()), "of", len(L), "| recordings matched:",
      L[L._merge == "both"].session.nunique(), "of", U.session.nunique())
Lm = L[L._merge == "both"].copy()
zal = Lm.z_location.map(P.split_area_layer)
Lm["z_area"], Lm["z_layer"] = [a for a, _ in zal], [l for _, l in zal]
print("same location label:", round((Lm.location == Lm.z_location).mean(), 4), "| same area:", round((Lm.area == Lm.z_area).mean(), 4))
print("peak-to-trough equal within 0.001 ms:", round((np.abs(Lm.ptt - Lm.z_p2t_ms) < 1e-3).mean(), 4))
lab = np.where(Lm.z_ww == 1, "ww", np.where(Lm.z_nw == 1, "nw", "na"))
print("ww/nw label agreement:", round((lab == Lm.utype).mean(), 4)); print(pd.crosstab(Lm.utype, lab, rownames=["dataset thresholds"], colnames=["Zenodo label"]).to_string())
diff = Lm[Lm.location != Lm.z_location]
print(f"\nunits whose location differs: {len(diff)}; examples:")
print(diff[["session", "unit_id", "location", "z_location"]].head(10).to_string(index=False))
print("by recording (units with a different location):"); print(diff.session.value_counts().head(10).to_string())
print("\nZenodo quality flags among the matched units: quality == 1:", int((Lm.z_quality == 1).sum()),
      "| waveform quality == 1:", int((Lm.z_wquality == 1).sum()), "| both:", int(((Lm.z_quality == 1) & (Lm.z_wquality == 1)).sum()))
both_ok = (Lm.z_quality == 1) & (Lm.z_wquality == 1)
print("units with both flags and >= 12 active epochs:", int((both_ok & (Lm.n_valid >= P.MIN_EPOCHS)).sum()),
      "| with both flags and >= 12 spontaneous epochs (active or sleep-like):",
      int((both_ok & (n_valid_with(recs, 6, ['active', 'near_sleep', 'sleep']) [L._merge.values == 'both'] >= P.MIN_EPOCHS)).sum()))
print("flatmap positions: PFC units with U > 0:", int(((Lm.U > 0) & Lm.is_pfc).sum()), "of", int(Lm.is_pfc.sum()), "PFC units")
Z473 = Z[Z.session.isin(U473.session)]
print("\n000473 recordings in the Zenodo files:", Z473.session.nunique(), "| units:", len(Z473), "of", len(U473))
''', ["claim:zenodo-unit-link"])

md(r'''
**Result: pending.**
''')

md(r'''
## fig4b-dataroi-parcellation

> The PFC flatmap is parcellated into 42 dataROIs that respect subregion boundaries, each holding
> about 200 deep-layer ww units.

Deep-layer PFC ww units with at least 12 active epochs and a flatmap position, assigned to a
subregion by the subregion polygon that contains them (code `flatmap_tessellation.py`); the
dataset's location label is shown as a check. Size bounds 160 to 240 (Methods), 180 to 220 as a
variant (code).
''')

code(r'''
regpolys = P.flatmap_polygons("flatmap_PFCregions.h5")
uvmap = Z.set_index(["session", "unit_id"])[["U", "V"]]
def attach_uv(D):
    D = D.join(uvmap, on=["session", "unit_id"])
    return D

ww_all = attach_uv(ww_all)
fm = ww_all[ww_all.is_pfc & ww_all.deep & (ww_all.U > 0)].copy()
fm["polyreg"] = P.in_polygons(fm[["U", "V"]].values, regpolys)
print("deep PFC ww units with a flatmap position:", len(fm), "| inside a subregion polygon:", int(fm.polyreg.notna().sum()),
      "| polygon agrees with the location label:", round((fm.polyreg == fm.area).mean(), 3))
fm = fm[fm.polyreg.notna()]
print("units per subregion:", fm.polyreg.value_counts().to_dict())
fm["droi"] = P.parcellate(fm[["U", "V"]].values, fm.polyreg.values, bounds=(160, 240))
fm["droi_code"] = P.parcellate(fm[["U", "V"]].values, fm.polyreg.values, bounds=(180, 220))
sz = fm.droi.value_counts()
print(f"\n001260: dataROIs (160-240) {fm.droi.nunique()}, (180-220) {fm.droi_code.nunique()}; units per dataROI {rng_str(sz)}")
# all of dataset KI (001260 + 000473): counts only
ww473 = U473[(U473.utype == "ww") & (U473.n_valid >= P.MIN_EPOCHS) & U473.is_pfc & U473.deep]
ww473 = attach_uv(ww473)
k473 = ww473[ww473.U > 0].copy()
k473["polyreg"] = P.in_polygons(k473[["U", "V"]].values, regpolys)
kk = pd.concat([fm[["U", "V", "polyreg"]], k473[k473.polyreg.notna()][["U", "V", "polyreg"]]])
nk = P.parcellate(kk[["U", "V"]].values, kk.polyreg.values, bounds=(160, 240))
nk2 = P.parcellate(kk[["U", "V"]].values, kk.polyreg.values, bounds=(180, 220))
print(f"001260 + 000473: {len(kk)} units, dataROIs (160-240) {len(set(nk))}, (180-220) {len(set(nk2))}; per subregion",
      kk.polyreg.value_counts().to_dict())
paper_drois = P.flatmap_polygons("flatmap_PFC_ntesselated_obeyRegions_res200.h5")
print("the paper's own dataROI tessellation on Zenodo has", len(paper_drois), "polygons; expected 42 ± 4")
''', ["claim:fig4b-dataroi-parcellation"])

md(r'''
**Result: pending.**
''')

md(r'''
## fig4cd-dataroi-enrichment

> Low-rate, regular-firing categories 1 and 3 are significantly enriched in dataROIs in ILA and PL,
> while low-rate, bursty categories 7 and 8 are enriched in dataROIs in MOs and ORBl, the ORBl
> enrichment pinpointed to its most ventral dataROI.

Reference (a) all deep PFC ww units of the parcellation; (b) all units as for regions (the
dataROIs plus one rest population of every other unit of the region analysis). Groups by
setting (G1 a and b), both G2 readings, dataROIs from the 160-240 parcellation.
''')

code(r'''
def droi_escores(fm_, roicol, ref, g1, g2, seed):
    if ref == "a":
        pops, cats = fm_[roicol].values, fm_["cat_" + g2].values
        grp = fm_.setting.replace({"Opto": "Passive"}).values if g1 == "a" else fm_.setting.values
        plist = sorted(pd.unique(pops))
    else:
        rest = sel[~sel.set_index(["session", "unit_id"]).index.isin(fm_.set_index(["session", "unit_id"]).index)]
        both = pd.concat([fm_.assign(pp=fm_[roicol]), rest.assign(pp="rest")])
        pops, cats = both.pp.values, both["cat_" + g2].values
        grp = both.setting.replace({"Opto": "Passive"}).values if g1 == "a" else both.setting.values
        plist = sorted(pd.unique(fm_[roicol])) + ["rest"]
    E, Pv, _ = P.escore(pops, cats, grp, 1000, seed=seed, pops=plist, attrs=range(1, 9))
    keep = [p for p in plist if p != "rest"]
    return E.loc[keep], Pv.loc[keep]

DROI = {}
for ref in ["a", "b"]:
    for g1 in ["a", "b"]:
        for g2 in ["a", "b"]:
            E, Pv = droi_escores(fm, "droi", ref, g1, g2, seed=21)
            DROI[(ref, g1, g2)] = (E, Pv)
            sp = (E > 0) & (Pv < 0.05)
            sub = lambda r, cs: any(sp.loc[i, cs].any() for i in E.index if i.startswith(r + "-"))
            ok = sub("ILA", [1, 3]) and sub("PL", [1, 3]) and sub("MOs", [7, 8]) and sub("ORBl", [7, 8])
            orbl = [i for i in E.index if i.startswith("ORBl-")]
            best = E.loc[orbl, [7, 8]].sum(1).idxmax() if orbl else None
            print(f"reference {ref}, G1 {g1}, G2 {g2}: ILA 1/3 {sub('ILA', [1, 3])}, PL 1/3 {sub('PL', [1, 3])}, "
                  f"MOs 7/8 {sub('MOs', [7, 8])}, ORBl 7/8 {sub('ORBl', [7, 8])} -> {ok}; ORBl dataROI with the highest 7+8 E-score: {best}")
E, Pv = DROI[("a", "a", "b")]
print("\nreference a, G1 a, G2 b (* P < 0.05):")
print(E.round(1).astype(str).where(Pv >= 0.05, E.round(1).astype(str) + "*").to_string())
''', ["claim:fig4cd-dataroi-enrichment"])

md(r'''
**Result: pending.**
''')

md(r'''
## fig4e-activity-modules

> Clustering dataROIs by enrichment profile gives activity modules; ILA forms a homogeneous
> ILA-specific module bordering a similar module in adjacent PL and ACAd, while other modules
> cross cytoarchitectural boundaries and occur in several places.
''')

code(r'''
from scipy.cluster.hierarchy import fcluster, linkage
for key, (E, Pv) in DROI.items():
    Zs = (E - E.mean(0)) / E.std(0)
    mod = pd.Series(fcluster(linkage(Zs.values, "ward"), 5, "maxclust"), index=E.index)
    subr = mod.index.str.split("-").str[0]
    ila = mod[subr == "ILA"]
    one = ila.nunique() == 1
    m_ila = ila.iloc[0] if one else None
    rd_a = one and (subr[mod == m_ila] == "ILA").all()
    rd_b = one and (subr[mod == m_ila] == "ILA").mean() > 0.5
    multi = sum(len(set(subr[mod == m])) > 1 for m in mod.unique() if m != m_ila)
    print(f"ref {key[0]} G1 {key[1]} G2 {key[2]}: ILA dataROIs {len(ila)} in one module {one}; ILA-only (a) {rd_a}, "
          f"mostly ILA (b) {rd_b}; other modules spanning subregions {multi}")
    if key == ("a", "a", "b"):
        print(pd.DataFrame({"module": mod, "subregion": subr}).groupby("module").subregion.apply(lambda s: dict(s.value_counts())).to_string())
''', ["claim:fig4e-activity-modules"])

md(r'''
**Result: pending.**
''')

md(r'''
## GaoROIs and the intra-PFC hierarchy (Fig. 4g,h, Extended Data Fig. 7n)

Units are assigned to the 60 GaoROI polygons (Zenodo `flatmap_PFCrois.h5`); GaoROIs with at
least 20 deep ww units (Extended Data Fig. 7i; more than 20 as a variant) and a hierarchy score.
E-scores as for dataROIs (both references, G1, G2), Pearson correlation with the Gao hierarchy
index.
''')

code(r'''
gpolys = P.flatmap_polygons("flatmap_PFCrois.h5")
gh = gao_h = P.gao_hierarchy()
fm["groi"] = P.in_polygons(fm[["U", "V"]].values, gpolys)
fm["groi"] = fm.groi.astype("float").astype("Int64")
gcount = fm.groi.value_counts()
print("deep PFC ww units in a GaoROI:", int(fm.groi.notna().sum()), "of", len(fm), "| GaoROIs with units:", len(gcount),
      "| with >= 20:", int((gcount >= 20).sum()), "| with >= 20 and a score:", int(((gcount >= 20) & gcount.index.isin(gh.dropna().index)).sum()),
      "| with > 20 and a score:", int(((gcount > 20) & gcount.index.isin(gh.dropna().index)).sum()), "(paper 30)")
GAO = {}
for nmin_lab, keep in [(">= 20", gcount[gcount >= 20].index), ("> 20", gcount[gcount > 20].index)]:
    keep = [int(k) for k in keep if k in gh.dropna().index]
    fg = fm[fm.groi.isin(keep)].copy()
    fg["groi_s"] = fg.groi.astype(int).astype(str)
    for ref in ["a", "b"]:
        for g1 in ["a", "b"]:
            for g2 in ["a", "b"]:
                E, Pv = droi_escores(fg, "groi_s", ref, g1, g2, seed=31)
                E.index = E.index.astype(int); Pv.index = Pv.index.astype(int)
                GAO[(nmin_lab, ref, g1, g2)] = (E, Pv)
for key, (E, Pv) in GAO.items():
    h = gh[E.index]
    r1, r6 = stats.pearsonr(h, E[1]), stats.pearsonr(h, E[6])
    print(f"n {key[0]}, ref {key[1]}, G1 {key[2]}, G2 {key[3]}: {len(E)} GaoROIs; category 1 r = {r1[0]:.2f} (p {r1[1]:.3f}),"
          f" category 6 r = {r6[0]:.2f} (p {r6[1]:.3f})")
''')

md(r'''
## fig4g-gao-category1

> Across GaoROIs, enrichment in low-rate, regular-firing category 1 units correlates positively
> with the intra-PFC hierarchy score of Gao et al.
''')

code(r'''
for key, (E, Pv) in GAO.items():
    r = stats.pearsonr(gh[E.index], E[1])
    print(f"n {key[0]}, ref {key[1]}, G1 {key[2]}, G2 {key[3]}: r = {r[0]:.3f}, p = {r[1]:.4f}, n = {len(E)} -> {r[0] > 0 and r[1] < 0.05}")
''', ["claim:fig4g-gao-category1"])

md(r'''
**Result: pending.**
''')

md(r'''
## extfig7n-gao-category6

> Across GaoROIs, enrichment in high-rate, bursty category 6 units correlates negatively with
> intra-PFC hierarchy.
''')

code(r'''
for key, (E, Pv) in GAO.items():
    r = stats.pearsonr(gh[E.index], E[6])
    print(f"n {key[0]}, ref {key[1]}, G1 {key[2]}, G2 {key[3]}: r = {r[0]:.3f}, p = {r[1]:.4f} -> {r[0] < 0 and r[1] < 0.05}")
''', ["claim:extfig7n-gao-category6"])

md(r'''
**Result: pending.**
''')

md(r'''
## fig4g-pl-orbl-extremes

> GaoROIs 19, 20 and 41 in PL have exceptionally high hierarchy scores and the strongest category 1
> enrichment, while GaoROI 23 in ventral ORBl has the lowest hierarchy score and the strongest
> category 1 depletion.
''')

code(r'''
print("Gao table: highest hierarchy scores", gh.dropna().sort_values().index[-4:].tolist()[::-1], "| lowest", gh.dropna().sort_values().index[:2].tolist())
for key, (E, Pv) in GAO.items():
    s = E[1].sort_values()
    top3, low = s.index[-3:].tolist()[::-1], s.index[0]
    n_top = len({19, 20, 41} & set(top3))
    print(f"n {key[0]}, ref {key[1]}, G1 {key[2]}, G2 {key[3]}: top three category 1 {top3}, lowest {low};"
          f" 19/20/41 in top three: {n_top}; 23 analysed: {23 in E.index}; 23 lowest: {low == 23}")
''', ["claim:fig4g-pl-orbl-extremes"])

md(r'''
**Result: pending.**
''')
EOF
python $TMPDIR/build_nb.py && python $TMPDIR/devrun.py && cd entries/001260-le-merre-2026 && cp $TMPDIR/dev.ipynb ./_dev.ipynb && . $TMPDIR/dev/bin/activate && time jupyter nbconvert --to notebook --execute _dev.ipynb --output $TMPDIR/dev_out.ipynb --ExecutePreprocessor.timeout=1800 2>&1 | grep -v Warn | tail -5; rm -f _dev.ipynb
```

```
99 cells
[NbConvertApp] Converting notebook _dev.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 488676 bytes to /tmp/claude-1001/dev_out.ipynb

real	2m0.307s
user	1m31.769s
sys	0m8.451s
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF' | grep -v "ConvergenceWarning\|fit = smf"
import nbformat
nb=nbformat.read('/tmp/claude-1001/dev_out.ipynb',4)
on=False
for c in nb.cells:
    if c.cell_type!='code': continue
    t=c.metadata.get('tags') or []
    if 'claim:zenodo-unit-link' in t: on=True
    if not on: continue
    print('=====', t)
    for o in c.outputs:
        if o.output_type=='stream': print(o.text[:5000])
        elif o.output_type=='error': print('ERROR', o.ename, o.evalue)
EOF
```

```
===== ['claim:zenodo-unit-link']
Zenodo metrics files: 108 recordings, 30634 units
dataset units matched: 20374 of 20374 | recordings matched: 74 of 74
same location label: 0.9861 | same area: 0.9892
peak-to-trough equal within 0.001 ms: 0.9514
ww/nw label agreement: 0.9703
Zenodo label         na    nw     ww
dataset thresholds                  
na                  683    33     98
nw                    9  3126    219
ww                   59   188  15959

units whose location differs: 283; examples:
              session  unit_id location z_location
PL051_20191121-probe0       46      ACB        OLF
PL051_20191121-probe0       93      OLF         DP
PL054_20191122-probe0       39      OLF      ORBl5
PL054_20191122-probe0       40      OLF      ORBl5
PL054_20191122-probe0       41      OLF      ORBl5
PL054_20191122-probe0       88   ORBl6b         fa
[... 214 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> pfcki.py <<'EOF'


# ---------------------------------------------------------------- tone responses
def tone_epoch_ok(r):
    """Tone response epochs [-2, 0.7] s around 10-kHz tones, dropping those with licking,
    sleep-like periods or spike-band saturation (Methods, Epoch selection)."""
    t = r["tones"]
    ep = np.c_[t - PRE, t + POST]
    bad = overlaps(ep, r["lick"]) | overlaps(ep, r["sat"])
    if r["sleep"] is not None and len(r["sleep"]):
        bad |= overlaps(ep, r["sleep"])
    return ~bad


def tone_traces(r):
    """Per unit: smoothed PSTH (0.5-ms bins, Gaussian kernel s.d. 10 ms over an 80-ms window),
    overall and prestimulus rates, z-scored trace 0 to 0.65 s (Methods, Extraction of PSTHs).
    Also returns the relative spike times of each unit (for the ZETA test)."""
    ok = tone_epoch_ok(r)
    tones = r["tones"][ok]
    f = open_asset(r["asset_id"])
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:].astype(np.int64)
    f.close()
    edges = np.arange(-PRE, POST + PSTH_BIN / 2, PSTH_BIN)
    nb = len(edges) - 1
    x = np.arange(-80, 81) * PSTH_BIN
    ker = np.exp(-0.5 * (x / 0.01) ** 2)
    ker /= ker.sum()
    pre = edges[:-1] < 0
    post = (edges[:-1] >= 0) & (edges[:-1] < 0.65 - 1e-9)
    out = np.full((len(idx), int(post.sum())), np.nan, np.float32)
    rate_all = np.zeros(len(idx))
    rate_pre = np.zeros(len(idx))
    start = 0
    for u in range(len(idx)):
        s = np.sort(st[start: idx[u]])
        start = idx[u]
        if len(tones) == 0:
            continue
        i0 = np.searchsorted(s, tones - PRE)
        i1 = np.searchsorted(s, tones + POST)
        n = i1 - i0
        if n.sum() == 0:
            continue
        rep = np.repeat(np.arange(len(tones)), n)
        pos = np.concatenate([np.arange(a, b) for a, b in zip(i0, i1) if b > a])
        rel = s[pos] - tones[rep]
        h = np.histogram(rel, edges)[0] / len(tones) / PSTH_BIN
        rate_all[u] = h.mean()
        rate_pre[u] = h[pre].mean()
        sm = np.convolve(h, ker, mode="same")
        mu, sd = sm[pre].mean(), sm[pre].std()
        if sd > 0:
            out[u] = (sm[post] - mu) / sd
    return dict(trace=out, rate_all=rate_all, rate_pre=rate_pre, n_tones=len(tones))
EOF
. $TMPDIR/dev/bin/activate && PYTHONPATH=. python - <<'EOF'
import pickle, time, numpy as np, pfcki as P
recs=pickle.load(open('/tmp/claude-1001/recs.pkl','rb')); recs=P.classify_epochs(recs)
tr=[r for r in recs if r['tones'] is not None]; print(len(tr), 'files with tones')
t=time.time(); o=P.tone_traces(tr[10]); print(time.time()-t, o['n_tones'], o['trace'].shape, np.nanmax(o['trace']), (o['rate_all']>=0.1).mean())
EOF
```

```
59 files with tones
2.1623919010162354 69 (129, 1299) 23.044504 0.9844961240310077
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && uv pip install -q zetapy 2>&1 | tail -1; PYTHONPATH=. python - <<'EOF'
import time, numpy as np, zetapy, inspect
print(zetapy.__version__ if hasattr(zetapy,'__version__') else '')
print(inspect.signature(zetapy.zetatest))
rng=np.random.default_rng(0); ev=np.sort(rng.uniform(10,2000,250)); sp=np.sort(np.r_[rng.uniform(0,2010,8000), (ev[:,None]+rng.uniform(0.02,0.05,(250,3))).ravel()])
t=time.time(); out=zetapy.zetatest(sp, ev, dblUseMaxDur=0.7); print(time.time()-t); print(out[0], list(out[1].keys())[:30])
EOF
```

```
Exit code 1

(spike_times, event_times, max_duration=None, resampling_number=100, plot_enabled=False, jitter_size=2.0, restrict_range=(-inf, inf), stitch_enabled=True, direct_quantile=False, return_rate=False)
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
TypeError: zetatest() got an unexpected keyword argument 'dblUseMaxDur'
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && PYTHONPATH=. python - <<'EOF'
import time, numpy as np, zetapy
from importlib.metadata import version; print(version('zetapy'))
rng=np.random.default_rng(0); ev=np.sort(rng.uniform(10,2000,250)); sp=np.sort(np.r_[rng.uniform(0,2010,8000), (ev[:,None]+rng.uniform(0.02,0.05,(250,3))).ravel()])
t=time.time(); out=zetapy.zetatest(sp, ev, max_duration=0.7); print(time.time()-t); print(out[0]); print({k:(v if np.size(v)<3 else np.shape(v)) for k,v in out[1].items()})
EOF
```

```
Exit code 1
4.1
0.2021181583404541
8.392100783147705e-27
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/_core/fromnumeric.py", line 3606, in size
    return a.size
           ^^^^^^
AttributeError: 'list' object has no attribute 'size'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/_core/fromnumeric.py", line 3608, in size
    return asarray(a).size
           ~~~~~~~^^^
ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (100,) + inhomogeneous part.
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && PYTHONPATH=. python - <<'EOF' 2>&1 | tail -5
import numpy as np, zetapy
rng=np.random.default_rng(0); ev=np.sort(rng.uniform(10,2000,250)); sp=np.sort(np.r_[rng.uniform(0,2010,8000), (ev[:,None]+rng.uniform(0.02,0.05,(250,3))).ravel()])
out=zetapy.zetatest(sp, ev, max_duration=0.7)
print(list(out[1].keys()))
print({k:out[1][k] for k in out[1] if 'Laten' in k or 'Onset' in k or 'Peak' in k and np.size(out[1][k])<3})
EOF
```

```
['zeta_p_value', 'zeta_score', 'ttest_z_score', 'ttest_p_value', 'zeta_deviation', 'latency_zeta', 'zeta_index', 'mu_duration', 'mu_pre', 'deviation_inv_sign', 'latency_inv_zeta', 'index_inv_sign', 'spike_time_vector', 'real_deviation', 'real_fraction', 'real_fraction_linear', 'random_times', 'random_deviations', 'max_duration']
{}
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && PYTHONPATH=. python - <<'EOF' 2>&1 | tail -5
import numpy as np, zetapy, time
rng=np.random.default_rng(0); ev=np.sort(rng.uniform(10,2000,250)); sp=np.sort(np.r_[rng.uniform(0,2010,8000), (ev[:,None]+rng.uniform(0.02,0.05,(250,3))).ravel()])
t=time.time(); out=zetapy.zetatest(sp, ev, max_duration=0.7, return_rate=True); print(time.time()-t, len(out))
print(list(out[2].keys())); print({k:out[2][k] for k in out[2] if np.size(out[2][k])<3})
EOF
```

```
0.3381083011627197 3
['rate_vector', 'timestamps', 'mean_derivative', 'scales', 'msd_matrix', 'values', 'smooth_sd', 'mean_rate']
{'smooth_sd': 2.0, 'mean_rate': np.float64(8.554285714285715)}
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && grep -rn "def get_onset\|def getOnset\|def get_peak\|half" $TMPDIR/dev/lib/python3.13/site-packages/zetapy/*.py | head
```

```
/tmp/claude-1001/dev/lib/python3.13/site-packages/zetapy/main.py:974:                4) Onset time, defined as the first crossing of peak half-height (same as rate_data['peak_onset_latency'])
/tmp/claude-1001/dev/lib/python3.13/site-packages/zetapy/plot_dependencies.py:571:        # half (causal) gaussian filter
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && sed -n 940,1000p $TMPDIR/dev/lib/python3.13/site-packages/zetapy/main.py; grep -n "^def " $TMPDIR/dev/lib/python3.13/site-packages/zetapy/main.py
```

```
switch to use the empirical null-distribution rather than the Gumbel approximation (default: False)
         [Note: requires many resamplings!]
    return_rate : boolean
        switch to return dictionary with spiking rate features [note: return-time is much faster if this is False]

    Returns
    -------
    zeta_p : float
        p-value based on Zenith of Event-based Time-locked Anomalies
    zeta_data : dict
        additional information of ZETA test
            zeta_p; p-value based on Zenith of Event-based Time-locked Anomalies (same as above)
            zeta_score; responsiveness z-score (i.e., >2 is significant)
            mean_z_score; z-score for mean-rate stim/base difference (i.e., >2 is significant)
            mean_p_value; p-value based on mean-rate stim/base difference
            zeta_deviation; temporal deviation value underlying ZETA
            latency_zeta; time corresponding to ZETA
            zeta_index; entry corresponding to ZETA
            mu_duration; spiking rate per trial during stim (used for mean-rate test)
            mu_pre; spiking rate per trial during baseline (used for mean-rate test)
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && grep -rln "onset" $TMPDIR/dev/lib/python3.13/site-packages/zetapy/ ; grep -n "def get_onset\|def getOnset" -A40 $TMPDIR/dev/lib/python3.13/site-packages/zetapy/dependencies.py | head -60
```

```
/tmp/claude-1001/dev/lib/python3.13/site-packages/zetapy/ts_dependencies.py
/tmp/claude-1001/dev/lib/python3.13/site-packages/zetapy/__pycache__/main.cpython-313.pyc
/tmp/claude-1001/dev/lib/python3.13/site-packages/zetapy/__pycache__/ts_dependencies.cpython-313.pyc
/tmp/claude-1001/dev/lib/python3.13/site-packages/zetapy/main.py
/tmp/claude-1001/dev/lib/python3.13/site-packages/zetapy/dependencies.py
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && grep -n "onset" $TMPDIR/dev/lib/python3.13/site-packages/zetapy/dependencies.py | head; grep -n "onset\|get_peak" $TMPDIR/dev/lib/python3.13/site-packages/zetapy/main.py | sed -n 1,40p
```

```
304:        # Calculate jittered stimulus onset times for this iteration
38:        window length for calculating ZETA: ignore all entries beyond this duration after event onset
39:        (default: minimum of event onset to event onset)
390:        window length for calculating ZETA: ignore all spikes beyond this duration after event onset
391:        (default: minimum of event onset to event onset)
633:        window length for calculating ZETA: ignore all entries beyond this duration after event onset
634:        (default: minimum of event onset to event onset)
926:        window length for calculating ZETA: ignore all spikes beyond this duration after event onset
927:        (default: minimum of event onset to event onset)
936:        temporal range within which to restrict onset/peak latencies (default: [-inf inf])
974:                4) Onset time, defined as the first crossing of peak half-height (same as rate_data['peak_onset_latency'])
975:               For true onset latencies, we recommend using LatenZy
977:            latency_values; values corresponding to above latencies (ZETA, -ZETA, rate at peak, rate at onset)
987:        Data on the peak and onset:
993:            peak_onset_latency: latency for peak onset [latencies entry #4]
995:            For true onset latencies, we recommend using LatenZy
1225:        Event onset times (s), or [T x 2] including event off times.
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
nproc; free -g | head -2; cat >> pfcki.py <<'EOF'


def zeta_unit(args):
    """ZETA test on the 700 ms after tone onset (Methods, ZETA test); zetapy defaults (100
    resamplings), seeded. The onset is the first crossing of half the peak height of the
    instantaneous rate, above its value at the first time point, as older zetapy versions
    computed it (zetapy 4 no longer returns it): a standard choice."""
    import zetapy
    spikes, tones, seed = args
    np.random.seed(seed)
    if len(spikes) < 3:
        return np.nan, np.nan
    try:
        p, d, rate = zetapy.zetatest(spikes, tones, max_duration=0.7, return_rate=True)
        v, t = np.asarray(rate["rate_vector"]), np.asarray(rate["timestamps"])
        if len(v) < 2:
            return p, np.nan
        k = int(np.argmax(v))
        thr = v[0] + (v[k] - v[0]) / 2
        onset = t[np.argmax(v[: k + 1] >= thr)]
        return p, float(onset)
    except Exception:
        return np.nan, np.nan


def zeta_for(r, unit_ids, seed=0):
    """ZETA p and onset for the given units of one recording, over its kept tone epochs."""
    f = open_asset(r["asset_id"])
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:].astype(np.int64)
    ids = f["units/id"][:]
    f.close()
    tones = r["tones"][tone_epoch_ok(r)]
    starts = np.r_[0, idx[:-1]]
    pos = pd.Index(ids).get_indexer(unit_ids)
    return [(np.sort(st[starts[i]: idx[i]]), tones, seed + int(ids[i])) for i in pos]
EOF
echo ok
```

```
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          11           0           3          14
ok
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cat > $TMPDIR/dev5.py <<'EOF'
import pickle, time, numpy as np, pandas as pd, pfcki as P, warnings
from concurrent.futures import ThreadPoolExecutor
warnings.filterwarnings('ignore')
recs=pickle.load(open('/tmp/claude-1001/recs.pkl','rb')); recs=P.classify_epochs(recs)
U=P.unit_table(recs)
tr=[r for r in recs if r['tones'] is not None]
t=time.time()
with ThreadPoolExecutor(8) as ex: TT=list(ex.map(P.tone_traces, tr))
print('traces', time.time()-t)
rows=[]; traces=[]
for r,o in zip(tr,TT):
    rows.append(pd.DataFrame({'session':r['session'],'unit_id':r['units'].unit_id.values,'rate_all':o['rate_all'],'rate_pre':o['rate_pre'],'n_tone_epochs':o['n_tones']}))
    traces.append(o['trace'])
T=pd.concat(rows,ignore_index=True); X=np.vstack(traces)
T=T.merge(U[['session','unit_id','utype','is_pfc','deep','area','setting','subject','n_valid','cortical']],on=['session','unit_id'])
ok=(T.rate_all>=0.1)&(T.rate_pre>=0.1)&np.isfinite(X).all(1)&T.utype.isin(['ww','nw'])
print(len(T), ok.sum(), T[ok].utype.value_counts().to_dict(), 'pfc deep ww', (ok&(T.utype=='ww')&T.is_pfc&T.deep).sum())
pickle.dump((T,X),open('/tmp/claude-1001/tone.pkl','wb'))
EOF
PYTHONPATH=. python $TMPDIR/dev5.py
```

```
traces 106.8423011302948
15906 14219 {'ww': 11737, 'nw': 2482} pfc deep ww 5232
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cat > $TMPDIR/dev6.py <<'EOF'
import pickle, time, numpy as np, pandas as pd, pfcki as P, warnings
warnings.filterwarnings('ignore')
T,X=pickle.load(open('/tmp/claude-1001/tone.pkl','rb'))
ok=((T.rate_all>=0.1)&(T.rate_pre>=0.1)&np.isfinite(X).all(1)&T.utype.isin(['ww','nw'])).values
T=T[ok].reset_index(drop=True); X=X[ok]
Xc=X-X.mean(0); w,V=np.linalg.eigh(np.cov(Xc.T)); o=np.argsort(w)[::-1][:8]; pcs=V[:,o].T
print('var explained 8 PCs', w[o].sum()/w.sum())
S=X@pcs.T
for rd,m in [('a',(T.utype=='ww')&((~T.cortical)|T.deep)),('b',T.utype=='ww')]:
    m=m.values; Z0=S[m]; mu,sd=Z0.mean(0),Z0.std(0); Z=(Z0-mu)/sd
    t=time.time(); som=P.train_som(Z,400); lab=P.ward_clusters(som['W'],8); node=P.bmus(Z,som['W']); print(rd,'som',time.time()-t, m.sum())
    cl=lab[node]
    tt=np.arange(X.shape[1])*0.0005
    mt=np.array([X[m][cl==c].mean(0) for c in range(8)])
    peak=mt.max(1); lat=tt[mt.argmax(1)]
    flat=np.argmin(peak)
    order=[c for c in np.argsort(lat) if c!=flat]+[flat]
    num=np.zeros(8,int)
    for i,c in enumerate(order): num[c]=i+1
    sub=(T[m].is_pfc&T[m].deep).values
    n=np.bincount(num[cl][sub],minlength=9)[1:]
    print(pd.DataFrame({'cat':num,'peak':peak.round(2),'lat_ms':(lat*1000).round(1),'n_all':np.bincount(cl,minlength=8)}).sort_values('cat').to_string(index=False))
    print('PFC deep ww per category', n, 'flat largest', n.argmax()==7)
EOF
PYTHONPATH=. python $TMPDIR/dev6.py
```

```
var explained 8 PCs 0.9405476936751627
a som 14.880369186401367 11172
 cat      peak  lat_ms  n_all
   1 18.889999    21.0    417
   2 24.340000    37.5    284
   3 19.590000    69.5    377
   4 13.260000    96.0    543
   5  8.200000   171.0    389
   6  3.680000   312.0    846
   7  1.960000   578.5   1189
   8  0.640000    27.5   7127
PFC deep ww per category [ 241  144  255  329  157  364  628 3114] flat largest True
b som 15.264707088470459 11737
 cat      peak  lat_ms  n_all
   1 22.900000    18.5    180
   2 41.950001    32.5    122
   3 22.870001    65.0    335
   4 32.720001    94.0     86
   5  3.950000   176.5   1082
   6  3.410000   309.0    994
[... 3 more lines not kept]
```

**Agent**

Category 8 (flat or negative) is the largest under both training readings. Timing ZETA on a sample.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cat > $TMPDIR/dev7.py <<'EOF'
import pickle, time, numpy as np, pandas as pd, pfcki as P, warnings
from concurrent.futures import ProcessPoolExecutor
warnings.filterwarnings('ignore')
recs=pickle.load(open('/tmp/claude-1001/recs.pkl','rb')); recs=P.classify_epochs(recs)
r=[r for r in recs if r['session']=='PL062_20200420-probe1'][0]
args=P.zeta_for(r, r['units'].unit_id.values[:40])
t=time.time()
with ProcessPoolExecutor(4) as ex: out=list(ex.map(P.zeta_unit,args))
print(time.time()-t, out[:8], np.mean([len(a[0]) for a in args]))
EOF
PYTHONPATH=. python $TMPDIR/dev7.py 2>&1 | tail -3
```

```
7.274793386459351 [(np.float64(0.0015348218566580973), 0.03213837240502926), (np.float64(4.09256374467315e-06), 0.037755162500701545), (np.float64(4.091243645976128e-06), 0.039897936200304684), (np.float64(1.1624381646146986e-07), 0.034204751505058084), (np.float64(0.0006847363951942853), 0.0415908229060733), (np.float64(0.00019243878712771334), 0.31374818387894265), (np.float64(2.9330532436144807e-07), 0.03601440013699175), (np.float64(0.0035299872875147464), 0.007655162500697088)] 31027.825
```

**Agent**

ZETA takes about 0.18 s per unit on 4 processes, so roughly 7 minutes for the responsive PFC units. Adding the fig5b and fig5j cells.

**Agent calls Bash**

```bash
cat >> $TMPDIR/nb_cells.py <<'EOF'

md(r'''
## Tone responses (Fig. 5b, 5j)

Tone response traces as in the Methods (pfcki.tone_traces): 10-kHz tones only (the
working-memory recordings have none and are left out), epochs with licking, sleep-like periods
or saturation dropped, units below 0.1 Hz overall or before the tone dropped, PCA over ww and nw
units pooled, 8 components. A SOM of 400 nodes on ww units, trained on (a) deep-layer ww units of
all regions (Results) or (b) all ww units (code); Ward into 8 categories numbered by the peak
latency of their mean trace, the category with the lowest mean peak last (Methods: "the flat or
negative category last").
''')

code(r'''
from concurrent.futures import ThreadPoolExecutor
trecs = [r for r in recs if r["tones"] is not None]
with ThreadPoolExecutor(8) as ex:
    TT = list(ex.map(P.tone_traces, trecs))
T = pd.concat([pd.DataFrame({"session": r["session"], "unit_id": r["units"].unit_id.values, "rate_all": o["rate_all"],
                             "rate_pre": o["rate_pre"], "n_tone_epochs": o["n_tones"]}) for r, o in zip(trecs, TT)], ignore_index=True)
X = np.vstack([o["trace"] for o in TT])
T = T.merge(U[["session", "unit_id", "utype", "is_pfc", "deep", "area", "region", "setting", "subject", "cortical"]], on=["session", "unit_id"])
print("files with 10-kHz tones:", len(trecs), "| tone response epochs per file:", rng_str([o["n_tones"] for o in TT]),
      "(paper: 188, IQR 86 to 228)")
okT = ((T.rate_all >= 0.1) & (T.rate_pre >= 0.1) & np.isfinite(X).all(1) & T.utype.isin(["ww", "nw"])).values
print("units:", len(T), "| kept (rates >= 0.1 Hz, ww or nw):", int(okT.sum()))
T, X = T[okT].reset_index(drop=True), X[okT]
Xc = X - X.mean(0)
w, V = np.linalg.eigh(np.cov(Xc.T))
o = np.argsort(w)[::-1][:8]
pcs = V[:, o].T
print(f"variance explained by 8 components: {w[o].sum() / w.sum():.3f} (Methods: over 95%)")
Sc = X @ pcs.T
tt = np.arange(X.shape[1]) * P.PSTH_BIN
TONE = {}
for rd, m in [("a", ((T.utype == "ww") & ((~T.cortical) | T.deep)).values), ("b", (T.utype == "ww").values)]:
    Z0 = Sc[m]
    Zs = (Z0 - Z0.mean(0)) / Z0.std(0)
    som_t = P.train_som(Zs, 400)
    lab = P.ward_clusters(som_t["W"], 8)
    cl = lab[P.bmus(Zs, som_t["W"])]
    mt = np.array([X[m][cl == c].mean(0) for c in range(8)])
    peak, lat = mt.max(1), tt[mt.argmax(1)]
    flat = int(np.argmin(peak))
    order = [c for c in np.argsort(lat) if c != flat] + [flat]
    num = np.zeros(8, int)
    for i, c in enumerate(order):
        num[c] = i + 1
    D = T[m].copy()
    D["tcat"] = num[cl]
    TONE[rd] = D
    pf = D[D.is_pfc & D.deep]
    print(f"\nreading {rd}: {m.sum()} ww units trained, {len(pf)} PFC deep ww units (paper 7,184 for all of dataset KI)")
    print(pd.DataFrame({"category": num, "mean peak (z)": peak.round(2), "peak latency (ms)": (lat * 1000).round(1),
                        "units": np.bincount(cl, minlength=8), "PFC deep ww": [int((pf.tcat == num[c]).sum()) for c in range(8)]}
                       ).sort_values("category").to_string(index=False))
fig, axs = plt.subplots(1, 2, figsize=(11, 3))
for ax, rd in zip(axs, ["a", "b"]):
    D = TONE[rd]
    for c in range(1, 9):
        sel_ = (T.set_index(["session", "unit_id"]).index.isin(D[D.tcat == c].set_index(["session", "unit_id"]).index))
        ax.plot(tt * 1000, X[sel_].mean(0), label=str(c))
    ax.set_title(f"reading {rd}: mean trace per category"); ax.set_xlabel("ms after tone"); ax.set_ylabel("z")
axs[1].legend(ncol=4, fontsize=7)
plt.show()
''')

md(r'''
## fig5b-tone-categories

> Deep-layer PFC ww tone responses cluster into eight categories ordered by peak delay; most
> units have flat or negative responses (category 8), categories 1 to 4 have sharp peaks with
> consistent onsets, and categories 5 to 7 have variable onsets and persistent responses.

ZETA test (pfcki.zeta_unit) on the PFC deep ww units of categories 1 to 7 under either reading;
the spread of onsets is the IQR over units with P < 0.01.
''')

code(r'''
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor
need = pd.concat([TONE[rd][(TONE[rd].tcat <= 7) & TONE[rd].is_pfc & TONE[rd].deep][["session", "unit_id"]] for rd in "ab"]).drop_duplicates()
by_s = {r["session"]: r for r in trecs}
args, keys = [], []
for s, g in need.groupby("session"):
    a = P.zeta_for(by_s[s], g.unit_id.values, seed=5)
    args += a
    keys += [(s, u) for u in g.unit_id.values]
t0 = time.time()
with ProcessPoolExecutor(4, mp_context=mp.get_context("fork")) as ex:
    zres = list(ex.map(P.zeta_unit, args, chunksize=8))
ZT = pd.DataFrame(keys, columns=["session", "unit_id"]).assign(zeta_p=[z[0] for z in zres], onset=[z[1] for z in zres])
print(f"ZETA on {len(ZT)} units in {time.time() - t0:.0f} s; failed or empty: {int(ZT.zeta_p.isna().sum())}")
for rd in "ab":
    D = TONE[rd][TONE[rd].is_pfc & TONE[rd].deep].merge(ZT, on=["session", "unit_id"], how="left")
    cnt = D.tcat.value_counts().sort_index()
    largest = cnt.idxmax() == 8
    rows = []
    for c in range(1, 8):
        g = D[(D.tcat == c) & (D.zeta_p < 0.01)]
        q = np.percentile(g.onset.dropna(), [25, 50, 75]) * 1000 if len(g.onset.dropna()) >= 3 else [np.nan] * 3
        rows.append({"category": c, "units": int((D.tcat == c).sum()), "ZETA P < 0.01": len(g),
                     "onset median (ms)": round(q[1], 1), "onset IQR (ms)": round(q[2] - q[0], 1)})
    R = pd.DataFrame(rows)
    iqr = R.set_index("category")["onset IQR (ms)"]
    part2 = iqr.loc[1:4].max() < iqr.loc[5:7].min()
    print(f"\nreading {rd}: category 8 is the largest: {largest} ({cnt.get(8, 0)} of {len(D)} units)")
    print(R.to_string(index=False))
    print(f"largest IQR in 1-4: {iqr.loc[1:4].max():.1f} ms, smallest IQR in 5-7: {iqr.loc[5:7].min():.1f} ms -> part 2 {part2}")
''', ["claim:fig5b-tone-categories"])

md(r'''
**Result: pending.**
''')

md(r'''
## fig5j-tone-responsive-high-rate

> At the single-unit level, tone-responsive units (tone categories 1 to 7) are more often than
> expected high-rate spontaneous units (categories 4 to 6), and units without clear positive tone
> responses (category 8) tend to have low spontaneous rates (categories 1 to 3, 7 and 8).

Mutual enrichment: spontaneous category as population, tone category as attribute, PFC deep ww
units with both, 1,000 shuffles grouped by setting (G1 a, b); the code's grouping by region and
setting as a variant. Both tone readings and both G2 readings.
''')

code(r'''
for rd in "ab":
    D = TONE[rd][TONE[rd].is_pfc & TONE[rd].deep].merge(ww_all[["session", "unit_id", "cat_a", "cat_b"]], on=["session", "unit_id"])
    print(f"tone reading {rd}: PFC deep ww units with both categories: {len(D)} (expected 6,681 ± 668 for all of dataset KI)")
    for g2 in "ab":
        for glab, grp in [("G1 a", D.setting.replace({"Opto": "Passive"}).values), ("G1 b", D.setting.values),
                          ("region x setting", (D.area + "|" + D.setting).values)]:
            E, Pv, _ = P.escore(D["cat_" + g2].values, D.tcat.values, grp, 1000, seed=41, pops=range(1, 9), attrs=range(1, 9))
            s17 = E[list(range(1, 8))].sum(1)
            sig = ((E[list(range(1, 8))] > 0) & (Pv[list(range(1, 8))] < 0.05)).loc[[4, 5, 6]].any(axis=1).any()
            p1 = (s17.loc[[4, 5, 6]] > 0).all() and sig
            n8 = int((E.loc[[1, 2, 3, 7, 8], 8] > 0).sum())
            print(f"  G2 {g2}, {glab}: summed E 1-7 in spont 4/5/6 {s17.loc[[4, 5, 6]].round(1).tolist()} (one significant {sig});"
                  f" tone-8 E-score positive in {n8} of spont 1,2,3,7,8 {E.loc[[1, 2, 3, 7, 8], 8].round(1).tolist()} -> {p1 and n8 >= 4}")
''', ["claim:fig5j-tone-responsive-high-rate"])

md(r'''
**Result: pending.**
''')

md(r'''
## methods-settings-no-difference (variant only)

> Firing metric distributions do not differ significantly across behavioral settings.

The paper names no test; the claim is blocked. As a variant only, a mixed model
Metric ~ 1 + Setting + (1|Mouse) per metric for ww units, with the size of the setting effects.
''')

code(r'''
for m in ["log10FR", "B", "M"]:
    f, r2 = P.mixed(ww_all, f'{m} ~ C(setting, Treatment("Passive"))')
    eff = f.params[[k for k in f.params.index if k.startswith("C(")]]
    pv = f.pvalues[eff.index]
    print(f"{m}: setting effects vs Passive " + ", ".join(f"{k.split('T.')[-1][:-1]} {v:.3f} (p {p:.2g})" for (k, v), p in zip(eff.items(), pv)),
          f"| marginal R2 {r2:.4f}")
print("medians by setting:"); print(ww_all.groupby("setting")[["log10FR", "B", "M"]].median().round(3).to_string())
''')

md(r'''
## Summary

Pending.
''')
EOF
python - <<'EOF'
p='entries/001260-le-merre-2026/pfcki.py'; s=open(p).read()
s=s.replace('''    import statsmodels.formula.api as smf
    fit = smf.mixedlm(formula, df, groups=df[group]).fit(reml=True)''','''    import warnings

    import statsmodels.formula.api as smf
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        fit = smf.mixedlm(formula, df, groups=df[group]).fit(reml=True)''')
open(p,'w').write(s)
s=open('/tmp/claude-1001/nb_cells.py').read()
s=s.replace('''    print(pd.DataFrame({"module": mod, "subregion": subr}).groupby("module").subregion.apply(lambda s: dict(s.value_counts())).to_string())''','''    print(pd.crosstab(mod.values, subr, rownames=["module"], colnames=["subregion"]).to_string())''')
open('/tmp/claude-1001/nb_cells.py','w').write(s)
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py && python $TMPDIR/devrun.py && cp $TMPDIR/dev.ipynb ./_dev.ipynb && time jupyter nbconvert --to notebook --execute _dev.ipynb --output $TMPDIR/dev_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | grep -v Warn | tail -3; rm -f _dev.ipynb; date -u
```

```
110 cells
[NbConvertApp] Converting notebook _dev.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 591659 bytes to /tmp/claude-1001/dev_out.ipynb

real	9m46.875s
user	15m22.704s
sys	0m25.274s
Sun Nov  1 13:23:20 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude-1001/dev_out.ipynb',4)
on=False
for c in nb.cells:
    if c.cell_type!='code': continue
    if 'TONE = {}' in c.source: on=True
    if not on: continue
    print('=====', c.metadata.get('tags'))
    for o in c.outputs:
        if o.output_type=='stream': print(o.text[:5000])
        elif o.output_type=='error': print('ERROR', o.ename, o.evalue)
EOF
```

```
===== None
files with 10-kHz tones: 59 | tone response epochs per file: 1 to 329 (median 80) (paper: 188, IQR 86 to 228)
units: 15906 | kept (rates >= 0.1 Hz, ww or nw): 14219

variance explained by 8 components: 0.941 (Methods: over 95%)


reading a: 11172 ww units trained, 5232 PFC deep ww units (paper 7,184 for all of dataset KI)
 category  mean peak (z)  peak latency (ms)  units  PFC deep ww
        1      18.889999               21.0    417          241
        2      24.340000               37.5    284          144
        3      19.590000               69.5    377          255
        4      13.260000               96.0    543          329
        5       8.200000              171.0    389          157
        6       3.680000              312.0    846          364
        7       1.960000              578.5   1189          628
        8       0.640000               27.5   7127         3114


reading b: 11737 ww units trained, 5232 PFC deep ww units (paper 7,184 for all of dataset KI)
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude-1001/dev_out.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    if any(k in c.source for k in ['tone_contrast(r, 1.5)','rng_str(U.q_isi)','from scipy.cluster.hierarchy import fcluster','ep = pd.DataFrame']):
        for o in c.outputs:
            if o.output_type=='stream': print(o.text[-3500:])
EOF
date -u
```

```
Peak_to_Trough (ms): 0.0001 to 2.05 (median 0.625)
quality column 0, 'ISI violation': 0 to 1.15e+05 (median 2) | fraction < 0.1: 0.36
quality column 1, 'false positive rate': 0 to 1 (median 0.0223) | fraction < 0.1: 0.688
spikes per unit: 17 to 5e+05 (median 7.06e+03)
unit locations:  129 labels; 0.518 of units have a layer
units per parent region:
parent
PFC      9704
other    3549
LS       1191
AON      1119
TT        888
ACB       797
DP        623
HPF       554
CP        534
SS        438
TH        407
MO        219
PIR       114
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/nb_cells.py'; s=open(p).read()
old='''need = pd.concat([TONE[rd][(TONE[rd].tcat <= 7) & TONE[rd].is_pfc & TONE[rd].deep][["session", "unit_id"]] for rd in "ab"]).drop_duplicates()'''
new='''# all PFC deep ww units with a tone trace (needed for fig5e as well)
need = TONE["b"][TONE["b"].is_pfc & TONE["b"].deep][["session", "unit_id"]].drop_duplicates()'''
assert old in s; s=s.replace(old,new)
i=s.index("md(r'''\n## fig5j-tone-responsive-high-rate")
add='''md(r\'\'\'
## fig5cd-tone-maps-cross-subregions

> Tone-response enrichment maps of the PFC do not follow cytoarchitectural boundaries; the
> earliest-responding units (category 1) are enriched in anterior ACAd and ORBvl and parts of PL,
> and tone response modules reveal heterogeneity within subregions.

dataROIs of fig4b; units are the PFC deep ww units with a tone category; E-scores of tone
category per dataROI grouped by setting, reference (a) these units, (b) all ww units with a
tone category in the region analysis (deep cortical and all non-cortical); Ward of the
standardized profiles into 4 modules (Extended Data Fig. 8e). Both tone readings.
\'\'\')

code(r\'\'\'
for rd in "ab":
    D = TONE[rd]
    ft = fm.merge(D[["session", "unit_id", "tcat"]], on=["session", "unit_id"])
    reg_all = D[(~D.cortical) | D.deep]
    for ref in "ab":
        for g1 in "ab":
            if ref == "a":
                pops, cats, sett, plist = ft.droi.values, ft.tcat.values, ft.setting, sorted(ft.droi.unique())
            else:
                rest = reg_all[~reg_all.set_index(["session", "unit_id"]).index.isin(ft.set_index(["session", "unit_id"]).index)]
                both = pd.concat([ft.assign(pp=ft.droi), rest.assign(pp="rest")])
                pops, cats, sett, plist = both.pp.values, both.tcat.values, both.setting, sorted(ft.droi.unique()) + ["rest"]
            grp = sett.replace({"Opto": "Passive"}).values if g1 == "a" else sett.values
            E, Pv, _ = P.escore(pops, cats, grp, 1000, seed=51, pops=plist, attrs=range(1, 9))
            E, Pv = E.loc[sorted(ft.droi.unique())], Pv.loc[sorted(ft.droi.unique())]
            sp1 = (E[1] > 0) & (Pv[1] < 0.05)
            subr = E.index.str.split("-").str[0]
            hit = {r: bool(sp1[subr == r].any()) for r in ["ACAd", "ORBvl", "PL"]}
            Zs = (E - E.mean(0)) / E.std(0).replace(0, 1)
            mod = pd.Series(fcluster(linkage(Zs.fillna(0).values, "ward"), 4, "maxclust"), index=E.index)
            split = [r for r in pd.unique(subr) if mod[subr == r].nunique() > 1]
            print(f"tone {rd}, ref {ref}, G1 {g1}: {len(ft)} units; category 1 enriched dataROI in ACAd/ORBvl/PL {hit};"
                  f" subregions whose dataROIs fall in more than one module: {split} -> {all(hit.values()) and len(split) >= 2}")
            if rd == "a" and ref == "a" and g1 == "a":
                print(E.round(1).astype(str).where(Pv >= 0.05, E.round(1).astype(str) + "*").assign(module=mod.values).to_string())
\'\'\', ["claim:fig5cd-tone-maps-cross-subregions"])

md(r\'\'\'
**Result: pending.**
\'\'\')

md(r\'\'\'
## fig5e-tone-responsive-patches

> Tone-responsive ww units (ZETA test) are enriched in spatial patches distributed across the PFC.

Responsive at ZETA P < 0.01 (Methods); dataROI E-scores of responsive against nonresponsive PFC
deep ww units with a tone trace, grouped by setting (G1 a, b), references as above.
\'\'\')

code(r\'\'\'
fz = fm.merge(ZT, on=["session", "unit_id"])
fz = fz[fz.zeta_p.notna()].copy()
fz["resp"] = np.where(fz.zeta_p < 0.01, "responsive", "non")
print(f"PFC deep ww units with a flatmap position and a ZETA result: {len(fz)}; responsive: {int((fz.resp == 'responsive').sum())}"
      f" ({100 * (fz.resp == 'responsive').mean():.1f} %)")
ZETAE = {}
for g1 in "ab":
    grp = fz.setting.replace({"Opto": "Passive"}).values if g1 == "a" else fz.setting.values
    E, Pv, _ = P.escore(fz.droi.values, fz.resp.values, grp, 1000, seed=61, attrs=["responsive", "non"])
    ZETAE[g1] = (E, Pv)
    e, p = E["responsive"], Pv["responsive"]
    subr = e.index.str.split("-").str[0]
    enr, dep = (e > 0) & (p < 0.05), (e < 0) & (p < 0.05)
    both = [r for r in pd.unique(subr) if enr[subr == r].any() and dep[subr == r].any()]
    print(f"G1 {g1}: enriched dataROIs {list(e.index[enr])} in {subr[enr].nunique()} subregions; depleted {list(e.index[dep])};"
          f" subregions with both: {both} -> {subr[enr].nunique() >= 3 and len(both) >= 1}")
print(pd.DataFrame({"E": ZETAE["a"][0]["responsive"].round(2), "P": ZETAE["a"][1]["responsive"].round(3),
                    "units": fz.droi.value_counts()}).to_string())
\'\'\', ["claim:fig5e-tone-responsive-patches"])

md(r\'\'\'
**Result: pending.**
\'\'\')

md(r\'\'\'
## extfig9e-tone-responsive-no-hierarchy

> Enrichment in tone-responsive units does not correlate with intra-PFC hierarchy across GaoROIs.

A claim of absence: Pearson correlation of the GaoROI E-scores of ZETA-responsive units with the
Gao hierarchy index, GaoROIs with at least 20 units and a score, p < 0.05.
\'\'\')

code(r\'\'\'
gzc = fz.groi.value_counts()
for nmin_lab, keepg in [(">= 20", gzc[gzc >= 20].index), ("> 20", gzc[gzc > 20].index)]:
    keepg = [int(k) for k in keepg if k in gh.dropna().index]
    fg = fz[fz.groi.isin(keepg)]
    for g1 in "ab":
        grp = fg.setting.replace({"Opto": "Passive"}).values if g1 == "a" else fg.setting.values
        E, Pv, _ = P.escore(fg.groi.astype(int).values, fg.resp.values, grp, 1000, seed=71, attrs=["responsive", "non"])
        r = stats.pearsonr(gh[E.index], E["responsive"])
        print(f"n {nmin_lab}, G1 {g1}: {len(E)} GaoROIs (paper 29), r = {r[0]:.3f}, p = {r[1]:.3f} -> absence {r[1] >= 0.05}")
\'\'\', ["claim:extfig9e-tone-responsive-no-hierarchy"])

md(r\'\'\'
**Result: pending.**
\'\'\')

'''
s=s[:i]+add+s[i:]
open(p,'w').write(s)
p2='entries/001260-le-merre-2026/pfcki.py'; t=open(p2).read()
t=t.replace('''    import zetapy
    spikes, tones, seed = args''','''    import logging

    import zetapy
    logging.getLogger().setLevel(logging.ERROR)
    spikes, tones, seed = args''')
open(p2,'w').write(t)
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py && python $TMPDIR/devrun.py && cp $TMPDIR/dev.ipynb ./_dev.ipynb && time jupyter nbconvert --to notebook --execute _dev.ipynb --output $TMPDIR/dev_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | grep -v Warn | tail -3; rm -f _dev.ipynb; date -u
```

```
119 cells
[NbConvertApp] Converting notebook _dev.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 604793 bytes to /tmp/claude-1001/dev_out.ipynb

real	10m47.279s
user	21m27.538s
sys	0m26.196s
Sun Nov  1 13:35:25 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude-1001/dev_out.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    t=c.metadata.get('tags') or []
    if any(x in str(t) for x in ['fig5cd','fig5e-','extfig9e','fig5b-']):
        print('=====', t)
        for o in c.outputs:
            if o.output_type=='stream': print(o.text[:3500])
            elif o.output_type=='error': print('ERROR', o.ename, o.evalue)
EOF
```

```
===== ['claim:fig5b-tone-categories']
ZETA on 5232 units in 268 s; failed or empty: 57

reading a: category 8 is the largest: True (3114 of 5232 units)
 category  units  ZETA P < 0.01  onset median (ms)  onset IQR (ms)
        1    241            222               14.4             4.7
        2    144            133               28.6            11.2
        3    255            235               50.8            20.7
        4    329            270               64.8            35.8
        5    157            125              102.0            90.7
        6    364            152               73.7           129.9
        7    628            192              105.3           284.4
largest IQR in 1-4: 35.8 ms, smallest IQR in 5-7: 90.7 ms -> part 2 True

reading b: category 8 is the largest: True (3788 of 5232 units)
 category  units  ZETA P < 0.01  onset median (ms)  onset IQR (ms)
        1    124            120               13.5             3.9
        2     68             68               23.5            10.5
        3    224            215               47.1            24.6
        4     60             60               63.4            26.3
[... 77 more lines not kept]
```

**Agent**

fig5e reproduces, and extfig9e reproduces as an absence (r = 0.05, p = 0.83). fig5cd fails on ORBvl. Adding the dataset part of fig5i (map similarity) by rasterising the dataROI maps.

**Agent calls Bash**

```bash
cat >> pfcki.py <<'EOF'


def raster_rois(uv, region, roi, regpolys, step=2.0):
    """Pixels of the PFC flatmap (grid of `step` flatmap units: a standard choice), each given
    the dataROI of the nearest unit-weighted ROI center within its subregion polygon (the
    Voronoi cells of the parcellation). Returns pixel coordinates and ROI labels."""
    import shapely
    allc = np.vstack(list(regpolys.values()))
    xs = np.arange(allc[:, 0].min(), allc[:, 0].max(), step)
    ys = np.arange(allc[:, 1].min(), allc[:, 1].max(), step)
    gx, gy = np.meshgrid(xs, ys)
    gx, gy = gx.ravel(), gy.ravel()
    lab = np.array([None] * len(gx), dtype=object)
    cen = pd.DataFrame({"u": uv[:, 0], "v": uv[:, 1], "roi": roi, "reg": region}).groupby(["reg", "roi"])[["u", "v"]].mean()
    for reg, c in regpolys.items():
        inside = shapely.contains_xy(shapely.Polygon(c), gx, gy)
        if reg not in cen.index.get_level_values(0) or not inside.any():
            continue
        cc = cen.loc[reg]
        d = (gx[inside, None] - cc.u.values[None]) ** 2 + (gy[inside, None] - cc.v.values[None]) ** 2
        lab[inside] = cc.index.values[d.argmin(1)]
    keep = lab != None  # noqa: E711
    return np.c_[gx[keep], gy[keep]], lab[keep]
EOF
python - <<'EOF'
p='/tmp/claude-1001/nb_cells.py'; s=open(p).read()
i=s.index("md(r'''\n## fig5j-tone-responsive-high-rate")
add='''md(r\'\'\'
## fig5i-map-similarity

> No pair of PFC maps is strongly congruent, but the choice-tuning map is most similar to the
> spontaneous category 1 map, the feedback-tuning map to the category 6 map, and the
> tone-responsiveness map to the category 8 map.

Dataset part only (the choice and feedback maps need dataset IBL, not tested). Each map is
rasterized on the flatmap (pixels of 2 flatmap units, a standard choice), each pixel taking the
E-score of its dataROI; cosine similarity between the tone-responsiveness map (fig5e, G1 a and b)
and each spontaneous category map (fig4cd, reference a, same G1), both G2 readings.
\'\'\')

code(r\'\'\'
pix, plab = P.raster_rois(fm[["U", "V"]].values, fm.polyreg.values, fm.droi.values, regpolys, step=2.0)
print(f"pixels: {len(pix)} (paper 311,563 at its own resolution), dataROIs covered: {len(set(plab))}")
for g1 in "ab":
    tmap = ZETAE[g1][0]["responsive"].reindex(plab).values
    for g2 in "ab":
        E = DROI[("a", g1, g2)][0]
        cos = {c: float(np.dot(tmap, E[c].reindex(plab).values) / np.linalg.norm(tmap) / np.linalg.norm(E[c].reindex(plab).values)) for c in range(1, 9)}
        best = max(cos, key=cos.get)
        print(f"G1 {g1}, G2 {g2}: cosine of the tone-responsiveness map with categories 1-8: "
              + ", ".join(f"{c}: {v:.2f}" for c, v in cos.items()) + f" -> highest {best}")
\'\'\', ["claim:fig5i-map-similarity"])

md(r\'\'\'
**Result: pending.**
\'\'\')

'''
s=s[:i]+add+s[i:]
open(p,'w').write(s)
EOF
. $TMPDIR/dev/bin/activate && PYTHONPATH=. python - <<'EOF'
import pfcki as P, numpy as np, time
rp=P.flatmap_polygons("flatmap_PFCregions.h5")
allc=np.vstack(list(rp.values())); print(allc.min(0), allc.max(0))
uv=np.random.default_rng(0).uniform(allc.min(0),allc.max(0),(3000,2))
reg=P.in_polygons(uv,rp); m=reg!=None
t=time.time(); pix,lab=P.raster_rois(uv[m],reg[m],np.array([r+'-1' for r in reg[m]]),rp); print(time.time()-t, len(pix), len(set(lab)))
EOF
```

```
[355.6   17.85] [1213.05  754.65]
0.07281208038330078 77740 11
```

**Agent**

Rasterisation works (77,740 pixels at 2-unit steps, about 311k at 1-unit, matching the paper). Writing the conclusion for each claim from the dev-run numbers.

**Agent calls Bash**

```bash
cat > $TMPDIR/results.py <<'EOF'
R = []
R.append("""**Result: partially reproduced.** On 001260 alone, 14,564 units meet the 12-epoch rule (reading b), 48.4% in the PFC, from 74 recordings: the dandiset holds 74 of the 99 recordings. With 000473 the recordings are the paper's 99 and the PFC share is 53.6% (expected 52 ± 5.2), but the unit count is 20,354 (expected 24,248 ± 2,425) and the PFC units 10,900 (12,674 ± 1,267). Counting all spontaneous epochs, active or sleep-like, gives 24,898 units and 13,040 PFC units, both within tolerance; the shortfall under the active-epoch rule follows from the larger share of sleep-like epochs found here (extfig1-epoch-counts). Under reading (a) the counts are far lower (4,820 or 13,917).""")
R.append("""**Result: partially reproduced.** The fractions match: on 001260 + 000473 (reading b) 78.1% ww and 18.2% nw of all units (81.1% and 18.9% of ww plus nw units), within 81.1 ± 8.1 and 17.7 ± 1.8. The counts are below the expected ones: 15,894 ww (19,186 ± 1,919), 3,698 nw (4,200 ± 420) and 762 unclassified (862 ± 86), as the unit total is (dataset-ki-counts). The histogram has a mode at 0.26 ms and one at 0.64 ms with a minimum at 0.36 ms (258 units against 410 at the lower mode).""")
R.append("""**Result: reproduced.** nw units have a higher log10FR (+0.235), B (+0.052) and M (+0.042) than ww units, p below 1e-76 for each, in 11,209 ww and 2,752 nw units from 38 mice; the difference has the same sign in every setting and when units with log10FR < 0.1 are dropped.""")
R.append("""**Result: reproduced.** In ww units, sleep-like epochs differ from active epochs in all three metrics: log10FR -0.027 (p = 6.4e-07), B +0.029 (p = 5.3e-64), M -0.013 (p = 2.6e-18), from 11,209 active and 10,381 sleep-like samples. With the code's detector all three also differ (p ≤ 0.0012), though log10FR changes sign (+0.018).""")
R.append("""**Result: not reproduced.** Per probe recording, sleep-like periods take a median 20.2% of the time (IQR 8.4 to 33.0%), against 6% (0 to 18%); recordings hold a median 180.5 active epochs (227 expected) and 125.5 sleep-like epochs (19 expected); 12 of 74 recordings are more than half sleep-like. Per session the values are similar. The code's detector gives 8.7%, 203 and 83.5. The count of ww units with at least 12 sleep-like epochs, 10,381, is just below 11,599 ± 1,160 although it covers 74 of 99 recordings.""")
R.append("""**Result: not reproduced.** By the paper's test burstiness depends on memory: slope -0.19, p = 1.7e-66, across 11,209 ww units. The effect is small: marginal R2 = 0.024 (Pearson r = -0.17).""")
R.append("""**Result: partially reproduced.** The gradients of B and log10FR over the node grid are at 110 degrees, within 60 to 120, so part 1 holds. Part 2 does not: of the top 10% memory nodes 3 of 43 lie in the top quartile of node B, and of the top 25% 23 of 107, where the criterion asks for none.""")
R.append("""**Result: reproduced.** PFC units are 50.5% of the ww SOM units (54 ± 5.4) and hit all 425 nodes. Compared with ww units of other regions they have a lower median burstiness (-0.055 against -0.023, Mann-Whitney p = 2.4e-32) and fewer anti-memory units (M < 0 in 54.1% against 68.2%, chi-square p = 3.6e-53). The burstiness difference is reversed in the Aversion setting (-0.105 against -0.111).""")
R.append("""**Result: reproduced.** Units keep their category from one block to the next in 57.3% of transitions on average over 13 transitions (59.4% for the pooled matrix), against 18.4% expected from the marginals; expected 57 ± 5.7 and 18 ± 1.8. Each transition lies between 46.2% and 61.1%. With the code's minimum of 3 epochs per block, stability is 49.0% (chance 14.7%).""")
R.append("""**Result: blocked (methods underspecified).** The outcome depends on which retrained cluster is given which category number (G2). Under the text-matched numbering (b) low-rate categories are less stable (mean diagonal 0.430 against 0.691, the coincidence diagonal agrees), but part 2 holds for 2 of 5 categories: partially reproduced. Under the code's numbering (a) neither part holds (0.613 against 0.387). The claims file blocks a claim whose outcome differs between the two.""")
R.append("""**Result: blocked (methods underspecified).** Under the text-matched numbering (G2 b) all six subregions are enriched in categories 1 to 3 under both readings and both groupings (sums of E-scores 3.9 to 16.2, each with a significant positive E-score): reproduced. Under the code's numbering (G2 a) ACAd and ACAv are not (sums -4.8 to -1.4): 4 of 6, partially reproduced. The claims file blocks a claim whose outcome differs under G2.""")
R.append("""**Result: blocked (methods underspecified).** Under G2 b, ILA and PL are significantly enriched in category 1 (E = 8.7 to 9.1 and 6.0, P < 0.001); under G2 a, ILA is depleted (E = -3.0 to -3.1) and PL not enriched. The outcome differs under G2.""")
R.append("""**Result: blocked (methods underspecified).** Under G2 b, ORBl (E = 3.6 to 3.7) and MOs (4.0 to 4.1) are significantly enriched in category 8 and AIv is not (1.4 to 1.6, P 0.07 to 0.11): partially reproduced. Under G2 a, none of the three is enriched (MOs is depleted). The outcome differs under G2.""")
R.append("""**Result: blocked (methods underspecified).** Under both G2 readings TH and HPF each have one significant positive E-score among categories 6 to 8 (TH 7.1 to 7.3, HPF 3.8 to 4.0), so the claim's reading (b), at least one, holds; reading (a), all three, holds for neither. The claims file blocks the claim when its two readings disagree.""")
R.append("""**Result: blocked (methods underspecified).** Under G2 b, L2/3 is enriched in bursty category 6 and 8 units (E = 3.5 to 3.7 and 6.4 to 7.0) and L5 (category 2) and L6 (categories 1 and 4 to 5) in regular categories: reproduced. Under G2 a, L5 has no significant positive E-score in categories 1 to 3. The outcome differs under G2.""")
R.append("""**Result: not reproduced.** The nw categories as numbered by the code put the high-rate, lowest-burstiness category at 5 (median M 0.018) and the high-rate bursty one at 1. ILA (E = -0.5 to -0.6) and PL (-2.0 to -2.1, depleted) are not enriched in category 5, and ORBl is not enriched in category 1 (E = 1.5, not significant), under both groupings.""")
R.append("""**Result: partially reproduced.** Across 21 regions with more than 20 nw units (9 in the paper), the mean correlation between the E-scores of ww categories 1 to 3 and of the regular nw category is -0.077 to -0.001, not positive, under every reading. The mean correlation between ww categories 7 and 8 and the bursty nw category is positive but small, 0.040 to 0.115.""")
R.append("""**Result: not reproduced.** Across 15 cortical areas with a Harris score and more than 20 deep ww units (17 in the paper), category 2 enrichment does not correlate significantly with hierarchy under any reading: r = 0.30 to 0.40 (p 0.14 to 0.28) under G2 b, and r = -0.17 to 0.05 under G2 a. Categories 1 and 3 are positive (r 0.28 to 0.50, p ≥ 0.057) only under G2 b. PFC areas have higher category 2 E-scores (0.28) and Harris scores (0.26) than the other areas (-2.51 and -0.16).""")
R.append("""**Result: blocked (methods underspecified).** Under G2 b, categories 6 to 8 all correlate negatively with hierarchy (r = -0.57 to -0.53 for 6, p 0.027 to 0.040), more strongly than any of 1 to 3: reproduced for dataset KI. Under G2 a, category 6 correlates positively (r = 0.30 to 0.40). The outcome differs under G2. The IBL Passive part was not tested.""")
R.append("""**Result: reproduced.** Within the 11 PFC subregions with a Harris score, no category's E-scores correlate with hierarchy at p < 0.05 under any reading (|r| ≤ 0.35, p ≥ 0.29).""")
R.append("""**Result: reproduced.** Every one of the 20,374 units of 001260 has a record in the Zenodo metrics files, matched by recording and unit id. The records agree on the location label for 98.6% of units (283 differ, 207 of them in one recording) and on the ww/nw label for 97.0%; peak-to-trough agrees within 0.001 ms for 95.1%. The paper's own quality flags pass 19,808 units; with the 12-epoch rule 14,256 remain.""")
R.append("""**Result: reproduced.** On dataset KI (001260 + 000473), 7,867 deep PFC ww units with flatmap positions give 38 dataROIs under either size bound, within 42 ± 4; the paper's own tessellation on Zenodo has 42. On 001260 alone, which holds 4,906 such units, the same rule gives 22 dataROIs. 87.7% of units fall in the subregion polygon that matches their location label.""")
R.append("""**Result: reproduced.** On the 22 dataROIs of 001260, at least one dataROI in ILA and in PL is significantly enriched in category 1 or 3, and at least one in MOs and in ORBl in category 7 or 8, under both references, both groupings and both G2 readings. ORBl is a single dataROI here (380 units), so whether the enrichment is in its most ventral part is not tested.""")
R.append("""**Result: partially reproduced.** The two ILA dataROIs of 001260 fall in one module under every reading, and three or four other modules hold dataROIs of more than one subregion. The ILA module is not ILA-specific: it also holds two PL, one MOs and one ORBm dataROI, so it is neither ILA-only (a) nor mostly ILA (b). Both readings agree that this part fails.""")
R.append("""**Result: not reproduced.** Across 29 GaoROIs (30 in the paper), category 1 enrichment correlates positively but not significantly with the Gao hierarchy index under every reading: r = 0.20 to 0.33, p = 0.086 to 0.31.""")
R.append("""**Result: blocked (methods underspecified).** Under G2 b, category 6 enrichment correlates negatively with hierarchy (r = -0.62 to -0.54, p ≤ 0.0023, 29 GaoROIs): reproduced. Under G2 a, r = 0.03 to 0.11. The outcome differs under G2.""")
R.append("""**Result: blocked (methods underspecified).** The Gao table itself gives GaoROI 23 the lowest score, but 5, 24, 3 and 2 the highest, not 19, 20 and 41. Under G2 b, GaoROIs 20 and 41 are among the three with the highest category 1 E-scores (with 56) and the lowest is 6, not 23: partially reproduced. Under G2 a, none of 19, 20 and 41 is in the top three, and 23 is the lowest in 5 of 8 readings. The outcome differs between readings.""")
R.append("""**Result: reproduced.** Under both training readings the flat or negative category 8 is the largest among the 5,232 PFC deep ww units (3,114 and 3,788). The across-unit IQR of ZETA onsets of responsive units is 3.9 to 35.8 ms in categories 1 to 4, and 90.7 to 284.4 ms in categories 5 to 7. Category peaks fall at 13.5 to 112 ms after onset in order of category number. Recordings keep a median 80 tone epochs (188 in the paper), because more epochs are sleep-like here.""")
R.append("""**Result: partially reproduced.** Under every reading, ACAd and PL each have a dataROI significantly enriched in tone category 1, but ORBvl has none. The dataROIs of three to five subregions fall in more than one tone module, so tone maps do not follow subregion boundaries.""")
R.append("""**Result: reproduced.** 1,746 of 3,839 PFC deep ww units are tone-responsive (45.5%). Significantly enriched dataROIs lie in 5 (G1 a) or 6 (G1 b) subregions, and ACAd and MOs (and PL under G1 a) each hold both an enriched and a depleted dataROI.""")
R.append("""**Result: reproduced.** Across 25 GaoROIs (29 in the paper), enrichment in tone-responsive units does not correlate with the Gao hierarchy: r = 0.046 (p = 0.83) or -0.002 (p = 0.99).""")
R.append("""FIG5I""")
R.append("""**Result: not reproduced.** Tone category 8 has a positive E-score in only 2 or 3 of the five low-rate spontaneous categories under every reading (four required). The summed E-score of tone categories 1 to 7 is positive in spontaneous categories 4, 5 and 6 only under G2 b with tone reading a; under G2 a it is negative in category 6 (-10.4 to -8.4). 3,921 PFC deep ww units have both categories (6,681 ± 668 expected for all of dataset KI).""")
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/results.py'; s=open(p).read()
reps=[("and L5 (category 2) and L6 (categories 1 and 4 to 5) in regular categories: reproduced.","and L5 (category 2, E = 1.9 to 2.2) and L6 (category 1, E = 1.8 to 2.0) in regular categories: reproduced."),
("Categories 1 and 3 are positive (r 0.28 to 0.50, p ≥ 0.057) only under G2 b.","Under G2 b categories 1 and 3 are positive as well (r 0.28 to 0.50, p ≥ 0.057)."),
("(|r| ≤ 0.35, p ≥ 0.29)","(|r| ≤ 0.35, p ≥ 0.28)"),
("and 23 is the lowest in 5 of 8 readings.","and 23 is the lowest in 6 of 8 readings."),
("Category peaks fall at 13.5 to 112 ms after onset in order of category number.","The mean traces of categories 1 to 7 peak at 18.5 to 578.5 ms after onset, in order of category number.")]
for a,b in reps:
    assert a in s, a; s=s.replace(a,b)
open(p,'w').write(s)
exec(s)
n=open('/tmp/claude-1001/nb_cells.py').read()
print(n.count("**Result: pending.**"), len(R))
parts=n.split("**Result: pending.**")
out=parts[0]
for i,r in enumerate(R):
    out+= (r if r!="FIG5I" else "**Result: pending.**") + parts[i+1]
open('/tmp/claude-1001/nb_cells.py','w').write(out)
EOF
grep -n "Result: pending" $TMPDIR/nb_cells.py
```

```
33 33
1386:**Result: pending.**
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude-1001/dev_out.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code' and 'Distinct subjects' in c.source:
        for o in c.outputs:
            if o.output_type=='stream': print(o.text[-900:])
EOF
```

```
ovian c
 PL084_20231220-probe1   PL084   Context    318     422             159          75.7 inherent Neuropixelsrecording in mPFC during contextual pavlovian c
 PL086_20231222-probe0   PL086   Context    164     434              96          62.0 inherent Neuropixelsrecording in mPFC during contextual pavlovian c
 PL086_20231222-probe1   PL086   Context    333     434             157          62.0 inherent Neuropixelsrecording in mPFC during contextual pavlovian c

Files, subjects and units by behavioral setting (setting from the session description and keywords):
           files  subjects  units
setting                          
Attention     15         4   4468
Aversion       6         6   2110
Context       14         8   3237
Detection     15        10   2976
Opto           4         3   1308
Passive       20        10   6275
Distinct subjects: 41 | sessions (subject and date): 50
```

**Agent**

001260 holds 41 mice and 000473 holds 25, which gives the paper's 66. Updating the header, data-check notes and summary.

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/nb_cells.py'; s=open(p).read()
old=s[s.index("**Claims.** Tested here:"):s.index("The table of outcomes is in the summary.")]
new='''**Claims.** Tested here: the claims on dataset KI's spontaneous activity (Figs. 1 and 2,
Extended Data Figs. 1, 3 and 5), the Harris hierarchy correlations (Fig. 3a,c, Supplementary
Table 5) with the Harris table, the PFC flatmap claims (Fig. 4) through the Zenodo flatmap
positions after a link claim, and the tone-response claims on dataset KI (Fig. 5b to 5f, the
dataset part of 5i, 5j, Extended Data Fig. 9e). Blocked: every claim on dataset IBL (Figs. 2i,
3b, 5g, 5h, 5k), not attempted in this run's time, and `methods-settings-no-difference`, whose
test the paper does not name. Many enrichment claims are blocked by the claims file's own rule
because their outcome depends on which retrained cluster takes which category number (G2).
'''
s=s.replace(old,new)
old2='''The archive counts 43 subjects; the files name 41 distinct mice once the suffixes `-1` and `-2`
of two subject ids (518804 and 560171, two days each) are removed, and 43 as written.'''
new2='''The archive counts 43 subjects, as the subject ids of two mice recorded on two days carry the
suffixes `-1` and `-2` (518804 and 560171); without the suffixes the files hold 41 mice, which with
the 25 mice of 000473 make the paper's 66.'''
assert old2 in s; s=s.replace(old2,new2)
old3='''as in the code. Onsets come at intervals of about 5 to 10 s outside the working-memory setting,
as the Methods state; in the working-memory setting the code's onsets are trial starts.'''
new3='''as in the code. Outside the working-memory setting the intervals between onsets have a median of
8.5 s (5th to 95th percentile 5.2 to 16.3 s), close to the Methods' 5 to 10 s; 1% are below 4.1 s.
In the working-memory setting the code's onsets are trial starts. The 3-s epochs are 3 s long.'''
assert old3 in s; s=s.replace(old3,new3)
open(p,'w').write(s)
EOF
echo done
```

```
done
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/nb_cells.py'; s=open(p).read()
i=s.index("md(r'''\n## dataset-ki-counts")
add='''md(r\'\'\'
In every sampled file the rate change at the true onsets is larger than at onsets shifted by
1.5 s (an increase in nine, a decrease in one somatosensory recording), so spikes and onsets
share a clock there. The other files with tones are consistent with it: their units enter the
tone categories of fig5b, whose responses peak tens of ms after the onsets.
\'\'\')

'''
s=s[:i]+add+s[i:]
old=s[s.index("## Summary\n\nPending."):]
new='''## Summary

| Claim | Outcome |
|---|---|
| dataset-ki-counts | partially reproduced (99 recordings and 53.6% PFC with 000473; 20,354 units) |
| fig1h-waveform-classes | partially reproduced (fractions match, counts low) |
| fig1i-nw-higher-metrics | reproduced |
| extfig1d-sleep-like-differ | reproduced |
| extfig1-epoch-counts | not reproduced (20% sleep-like time, 6% expected) |
| extfig1f-burstiness-memory-uncorrelated | not reproduced (p = 1.7e-66, marginal R2 0.024) |
| fig2a-som-memory-burstiness | partially reproduced |
| fig2b-pfc-regular-territory | reproduced |
| fig2e-category-stability | reproduced (57.3%, chance 18.4%) |
| fig2f-low-rate-less-stable | blocked: methods underspecified (G2) |
| extfig3f-layer-enrichment | blocked: methods underspecified (G2) |
| fig2g-pfc-regular-enrichment | blocked: methods underspecified (G2) |
| fig2g-ila-pl-category1 | blocked: methods underspecified (G2) |
| fig2g-bursty-orbl-mos-aiv | blocked: methods underspecified (G2) |
| fig2g-th-hpf-bursty | blocked: methods underspecified (the claim's two readings) |
| fig2i-ibl-replication | blocked: too large (dataset IBL, not attempted) |
| extfig5g-nw-enrichment | not reproduced |
| fig2j-nw-ww-correspondence | partially reproduced |
| fig3a-harris-regular-positive | not reproduced |
| fig3b-harris-regular-positive-ibl | blocked: too large (dataset IBL) |
| fig3c-harris-bursty-negative | blocked: methods underspecified (G2) |
| supptable5-no-hierarchy-within-pfc | reproduced |
| zenodo-unit-link (link claim) | reproduced |
| fig4b-dataroi-parcellation | reproduced (38 dataROIs with 000473; 22 on 001260 alone) |
| fig4cd-dataroi-enrichment | reproduced |
| fig4e-activity-modules | partially reproduced |
| fig4g-gao-category1 | not reproduced |
| extfig7n-gao-category6 | blocked: methods underspecified (G2) |
| fig4g-pl-orbl-extremes | blocked: methods underspecified |
| fig5b-tone-categories | reproduced |
| fig5cd-tone-maps-cross-subregions | partially reproduced |
| fig5e-tone-responsive-patches | reproduced |
| fig5g-tuned-unit-counts | blocked: too large (dataset IBL) |
| fig5g-tuning-maps | blocked: too large (dataset IBL) |
| fig5h-choice-gao-hierarchy | blocked: too large (dataset IBL) |
| extfig9e-tone-responsive-no-hierarchy | reproduced |
| fig5i-map-similarity | FIG5I_SUMMARY |
| fig5j-tone-responsive-high-rate | not reproduced |
| fig5k-task-tuning-category4 | blocked: too large (dataset IBL) |
| methods-settings-no-difference | blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

**How the analysis differs from the paper's.** The analyses run on 001260, which holds 74 of the
99 recordings; 000473 is added only for the counts and the number of dataROIs. Units are not
filtered by the paper's quality flags, which the files lack (the flags on Zenodo pass 97% of
units). Sleep-like periods follow the Methods and flag far more time than the paper reports, so
fewer active epochs and units enter every analysis. The SOM, the clustering and the E-scores are
re-implemented from the Methods and the code; the SOM grid has 425 nodes, as the code's shape rule
gives. Mixed models are fitted with statsmodels and tested by Wald tests, not Kenward-Roger F
tests. The retrained clusters cannot be tied to the paper's category numbers, and the two
readings of the claims file (G2) often disagree. Blocks for the stability analysis are taken
from the trials table's `Block` column or cut into 50 onsets. The ZETA onset is computed from
zetapy's rate as the first half-peak crossing.

**What was found about the dataset.** The two dandisets together hold exactly the 29,782 units
the paper had before its unit quality control, and the 66 mice; 001260 alone holds 74
recordings, 41 mice and 20,374 units. It carries no label of which units the paper kept, its
`quality` columns are undescribed, and its unit locations, flatmap positions and ww/nw labels
need the paper's Zenodo files to be matched to the paper's. The other 25 recordings are in
000473, whose metadata names another paper. The trials tables carry `sound` columns that are
False for every trial in some files that hold tone presentations.
'''
s=s.replace(old,new)
open(p,'w').write(s)
EOF
grep -n "sound" /tmp/claude-1001/nb_cells.py | head -3
```

```
1517:000473, whose metadata names another paper. The trials tables carry `sound` columns that are
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/nb_cells.py'; s=open(p).read()
a=''' The trials tables carry `sound` columns that are
False for every trial in some files that hold tone presentations.
'''
assert a in s; s=s.replace(a,"\n"); open(p,'w').write(s)
EOF
cd entries/001260-le-merre-2026 && . $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py && python $TMPDIR/devrun.py && cp $TMPDIR/dev.ipynb ./_dev.ipynb && time jupyter nbconvert --to notebook --execute _dev.ipynb --output $TMPDIR/dev_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | grep -v Warn | tail -2; rm -f _dev.ipynb; python - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude-1001/dev_out.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    for o in c.outputs:
        if o.output_type=='error': print('ERROR', c.source[:80], o.ename, o.evalue)
    if 'claim:fig5i-map-similarity' in str(c.metadata.get('tags')):
        for o in c.outputs:
            if o.output_type=='stream': print(o.text)
EOF
date -u
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/build_nb.py", line 20, in <module>
    exec(open("/tmp/claude-1001/nb_cells.py").read())
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 1451
    md(r'''
       ^
SyntaxError: unterminated triple-quoted string literal (detected at line 1517)
Sun Nov  1 13:37:57 UTC 2026
```

**Agent calls Bash**

```bash
printf "''')\n" >> $TMPDIR/nb_cells.py; tail -4 $TMPDIR/nb_cells.py; cd entries/001260-le-merre-2026 && . $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py && python $TMPDIR/devrun.py && cp $TMPDIR/dev.ipynb ./_dev.ipynb && time jupyter nbconvert --to notebook --execute _dev.ipynb --output $TMPDIR/dev_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | grep -v Warn | tail -2; rm -f _dev.ipynb; python - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude-1001/dev_out.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    for o in c.outputs:
        if o.output_type=='error': print('ERROR', c.source[:80], o.ename, o.evalue)
    if 'claim:fig5i-map-similarity' in str(c.metadata.get('tags')):
        for o in c.outputs:
            if o.output_type=='stream': print(o.text)
EOF
date -u
```

```
`quality` columns are undescribed, and its unit locations, flatmap positions and ww/nw labels
need the paper's Zenodo files to be matched to the paper's. The other 25 recordings are in
000473, whose metadata names another paper.
''')
123 cells
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 624896 bytes to /tmp/claude-1001/dev_out.ipynb

real	10m55.964s
user	21m9.843s
sys	0m26.617s
pixels: 77740 (paper 311,563 at its own resolution), dataROIs covered: 22
G1 a, G2 a: cosine of the tone-responsiveness map with categories 1-8: 1: 0.34, 2: 0.04, 3: 0.01, 4: -0.43, 5: 0.00, 6: -0.01, 7: 0.01, 8: -0.02 -> highest 1

G1 a, G2 b: cosine of the tone-responsiveness map with categories 1-8: 1: 0.01, 2: -0.01, 3: -0.43, 4: 0.04, 5: 0.34, 6: -0.02, 7: 0.00, 8: 0.01 -> highest 5
G1 b, G2 a: cosine of the tone-responsiveness map with categories 1-8: 1: 0.46, 2: 0.19, 3: -0.14, 4: -0.44, 5: -0.01, 6: -0.18, 7: 0.06, 8: 0.07 -> highest 1

G1 b, G2 b: cosine of the tone-responsiveness map with categories 1-8: 1: -0.14, 2: -0.18, 3: -0.44, 4: 0.19, 5: 0.46, 6: 0.07, 7: -0.01, 8: 0.06 -> highest 5

Sun Nov  1 13:48:59 UTC 2026
```

**Agent**

fig5i (dataset part) fails: the tone-responsiveness map is most similar to category 1 (G2 a) or 5 (G2 b), never 8. Writing the entry files and running the official lock and run.

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/nb_cells.py'; s=open(p).read()
s=s.replace("**Result: pending.**","**Result: not reproduced.** For the dataset part, the tone-responsiveness map is most similar to spontaneous category 1 (G2 a, cosine 0.34 or 0.46) or 5 (G2 b, the same cluster), never to category 8 (cosine -0.02 to 0.07), under both groupings. No pair is strongly congruent: the largest cosine is 0.46. The choice and feedback parts need dataset IBL and were not tested.")
s=s.replace("| fig5i-map-similarity | FIG5I_SUMMARY |","| fig5i-map-similarity | not reproduced (dataset part; IBL parts not tested) |")
open(p,'w').write(s)
EOF
cd entries/001260-le-merre-2026 && . $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py
cat > requirements.in <<'EOF'
h5py
k-means-constrained
matplotlib
numpy
openpyxl
pandas
remfile
requests
scipy
shapely
statsmodels
zetapy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 001260-le-merre-2026
type: reproduction
title: A prefrontal cortex map from single-neuron activity (Le Merre, Heining et al. 2026)
description: Tests the findings of Le Merre, Heining et al. (2026) on dandiset 001260, which holds 74
  of the 99 Neuropixels recordings of the paper's dataset KI (the other 25 are in dandiset 000473).
  It recomputes the spontaneous firing metrics, the self-organizing map categories, their stability
  and their enrichment across brain regions, layers and the PFC flatmap, the Harris and Gao hierarchy
  correlations and the tone-response categories. The claims on the International Brain Laboratory
  data are not tested.
license: Apache-2.0
notebooks:
- path: reproduce_le_merre_2026.ipynb
  title: Reproducing Le Merre, Heining et al. (2026) from dandiset 001260
  runtime_minutes: 20
helpers:
- pfcki.py
related:
- id: dandi:001260/0.250911.0744
  relation: uses_data
- id: doi:10.1038/s41593-025-02190-z
  relation: reproduces
EOF
cd  && pip list 2>/dev/null | grep -i -E "^(pyyaml|jsonschema|nbformat) " ; python tools/entry.py lock entries/001260-le-merre-2026 2>&1 | tail -3
```

```
123 cells
jsonschema                4.26.0
nbformat                  5.11.1
PyYAML                    6.0.3
  File "tools/entry.py", line 55, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && uv pip install -q pyyaml jsonschema nbformat && python tools/entry.py lock entries/001260-le-merre-2026 2>&1 | tail -3 && python tools/entry.py check entries/001260-le-merre-2026 2>&1 | tail -15
```

```
wrote entries/001260-le-merre-2026/requirements.lock.txt
0 error(s)
```

**Agent**

Lock and check pass. Before the full run I'll add the link claim to the claims file and mark the flatmap claims as using outside inputs. Checking the schema first.

**Agent calls Bash**

```bash
ls schemas; python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));c=s['properties']['claims']['items'];print(json.dumps(c.get('properties',{}),indent=0)[:2500]); print(c.get('required'))" 2>/dev/null || ls schemas
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
{
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
"description": "Where the paper shows it, precise enough to find without searching: a figure panel, e.g. 'Figure 2B', or a section and paragraph, e.g. 'Results, Place fields, paragraph 3'.",
"type": "string"
},
"kind": {
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rn "kind: link" -A14 claims/ | head -40
```

```
claims/000351/10.1126-science.abq6740.yaml:87:  kind: link
claims/000351/10.1126-science.abq6740.yaml-88-  statement: The subjects and "Day" numbers that the paper's analysis code names for each
claims/000351/10.1126-science.abq6740.yaml-89-    experiment are sessions of the dandiset, so that the code's selection of sessions can be
claims/000351/10.1126-science.abq6740.yaml-90-    applied to it.
claims/000351/10.1126-science.abq6740.yaml-91-  source: Data and materials availability; README.md and functions/load.py of
claims/000351/10.1126-science.abq6740.yaml-92-    github.com/namboodirilab/ANCCR at commit cff4414; dandiset description (related resource
claims/000351/10.1126-science.abq6740.yaml-93-    "Subject and session information")
claims/000351/10.1126-science.abq6740.yaml-94-  data: with_labels
claims/000351/10.1126-science.abq6740.yaml-95-  criterion: Subject names are matched with "_" read as "-" (HJ_FP_M2 as HJ-FP-M2), and sessions
claims/000351/10.1126-science.abq6740.yaml-96-    by the number after "Day" in the file path, as load_dandi_url does. The link holds
claims/000351/10.1126-science.abq6740.yaml-97-    (reproduced) when every subject of the Matlab scripts' lists exists in the dandiset and every
claims/000351/10.1126-science.abq6740.yaml-98-    Day number from startday to endday (and each learnedday) of analysis/fig4/cumsum_pavlovian.m,
claims/000351/10.1126-science.abq6740.yaml-99-    analysis/fig4/cumsum_bgdrw_vs_extinction.m, analysis/fig5/intermediate_rsp_trialless.m,
claims/000351/10.1126-science.abq6740.yaml-100-    analysis/fig6/backpropagation_pavlovian.m, analysis/figS10/cue_acquisition.m and
claims/000351/10.1126-science.abq6740.yaml-101-    analysis/figS10/omission.m is a session of that subject of the task the script names
--
claims/001750/10.1038-s41556-026-02009-4.yaml:72:  kind: link
claims/001750/10.1038-s41556-026-02009-4.yaml-73-  statement: The dandiset's recordings are the 35 outside-out patches of the paper's code table
claims/
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import re, yaml
p='claims/001260/10.1038-s41593-025-02190-z.yaml'; s=open(p).read()
targets=['fig4b-dataroi-parcellation','fig4cd-dataroi-enrichment','fig4e-activity-modules','fig4g-gao-category1','extfig7n-gao-category6','fig4g-pl-orbl-extremes','fig5cd-tone-maps-cross-subregions','fig5e-tone-responsive-patches','extfig9e-tone-responsive-no-hierarchy','fig5i-map-similarity']
lines=s.split('\n')
out=[]; i=0
# split into claim blocks
starts=[k for k,l in enumerate(lines) if l.startswith('- id: ')]
ck=[k for k,l in enumerate(lines) if l.startswith('checks:')][0]
blocks=[]
prev=0
res=lines[:starts[0]]
for j,st in enumerate(starts):
    en=starts[j+1] if j+1<len(starts) else ck
    b=lines[st:en]
    cid=b[0][6:].strip()
    if cid in targets:
        if not any(l.startswith('  data:') for l in b):
            b.insert(1,'  data: with_inputs')
        if any(l.startswith('  depends_on:') for l in b):
            k=[n for n,l in enumerate(b) if l.startswith('  depends_on:')][0]
            b.insert(k+1,'  - zenodo-unit-link')
        else:
            b.insert(2,'  depends_on:\n  - zenodo-unit-link')
    res+=b
link='''- id: zenodo-unit-link
  kind: link
  statement: The paper's per-unit metrics files on Zenodo (record 14205018) can be matched to the
    dandiset's units, and the matched records agree on what both describe, so that the flatmap
    position of each unit can be taken from them.
  source: Code availability; github.com/hejDMC/pfcmap at commit 9ae52eddc47fbb590ef4e1b1949507334707a0f1,
    which reads metrics_files from Zenodo record 14205018 (doi 10.5281/zenodo.14205018)
  inferred: Added by the author (protocol, Author, step 1.4) because the flatmap claims need each
    unit's flatmap position, which the dandiset lacks and the Zenodo metrics files hold.
  data: with_inputs
  criterion: Written by the author for the registry's check. Records are matched by recording id
    (metrics_<recording>.h5) and unit id (uids). The link holds (reproduced) when at least 95% of
    the dandiset's units are matched and, among them, at least 95% agree on the location label and
    on the ww/nw label (Zenodo unit_type against the Methods thresholds on the dataset's
    Peak_to_Trough); partially reproduced when the match holds but agreement is lower; not
    reproduced when fewer than 95% are matched.'''
res=res[:len(res)]  # claims end before checks
idx=[k for k,l in enumerate(res) if l.startswith('checks:')]
s2='\n'.join(res+[link]+lines[ck:])
open(p,'w').write(s2)
d=yaml.safe_load(open(p)); print(len(d['claims']), [ (c['id'],c.get('data'),c.get('depends_on')) for c in d['claims'] if c['id'] in targets+['zenodo-unit-link']])
EOF
git diff --stat
```

```
40 [('fig4b-dataroi-parcellation', 'with_inputs', ['zenodo-unit-link']), ('fig4cd-dataroi-enrichment', 'with_inputs', ['zenodo-unit-link', 'fig4b-dataroi-parcellation']), ('fig4e-activity-modules', 'with_inputs', ['zenodo-unit-link', 'fig4cd-dataroi-enrichment']), ('fig4g-gao-category1', 'with_inputs', ['zenodo-unit-link', 'fig4cd-dataroi-enrichment']), ('extfig7n-gao-category6', 'with_inputs', ['zenodo-unit-link', 'fig4g-gao-category1']), ('fig4g-pl-orbl-extremes', 'with_inputs', ['zenodo-unit-link', 'fig4g-gao-category1']), ('fig5cd-tone-maps-cross-subregions', 'with_inputs', ['zenodo-unit-link', 'fig5b-tone-categories', 'fig4b-dataroi-parcellation']), ('fig5e-tone-responsive-patches', 'with_inputs', ['zenodo-unit-link', 'fig4b-dataroi-parcellation']), ('extfig9e-tone-responsive-no-hierarchy', 'with_inputs', ['zenodo-unit-link', 'fig5e-tone-responsive-patches', 'fig4g-gao-category1']), ('fig5i-map-similarity', 'with_inputs', ['zenodo-unit-link', 'fig4cd-dataroi-enrichment', 'fig5e-tone-responsive-patches', 'fig5g-tuned-unit-counts']), ('zenodo-unit-link', 'with_inputs', None)]
 claims/001260/10.1038-s41593-025-02190-z.yaml | 32 +++++++++++++++++++++++++++
 1 file changed, 32 insertions(+)
```

**Agent calls Bash**

```bash
grep -n "depends_on" tools/*.py | head -20
```

```
tools/entry.py:222:            for other in c.get("depends_on", []):
```

**Agent calls Bash**

```bash
sed -n 200,330p tools/entry.py
```

```
if dandiset not in code and dandiset not in helper_code:
                report.error(rel / name, f"neither the notebook nor a helper names dataset {dandiset}")
            version = versions[dandiset]
            if version and version not in code and version not in helper_code:
                report.error(rel / name, f"neither the notebook nor a helper names version {version} "
                                         f"of dataset {dandiset}, which entry.yaml pins")
        _derivation_checks(report, rel / name, code)
    for name in helpers:
        if (entry_dir / name).is_file():
            _derivation_checks(report, rel / name, (entry_dir / name).read_text())

    # Claims and attempts that go with this entry.
    claims_by_target, labels_used, kinds_by_target = {}, {}, {}
    for path in sorted((ROOT / "claims").glob("*/*.yaml")):
        data = validate(report, path, "claims") or {}
        ids = {c["id"] for c in data.get("claims", [])}
        claims_by_target[(dataset_id(data), data.get("paper"))] = ids
        kinds_by_target[(dataset_id(data), data.get("paper"))] = {
            c["id"]: c.get("data", "dataset") for c in data.get("claims", [])}
        labels_used[(dataset_id(data), data.get("paper"))] = any(
[... 110 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/nb_cells.py'; s=open(p).read()
reps=[("**Result: not reproduced.** Across 15 cortical areas with a Harris score","**Result: blocked (methods underspecified),** because the claim depends on fig2g-pfc-regular-enrichment, which is blocked (protocol: a claim that depends on a blocked claim is blocked for the same reason). As computed it would be not reproduced: across 15 cortical areas with a Harris score"),
("**Result: reproduced.** Within the 11 PFC subregions with a Harris score","**Result: blocked (methods underspecified),** because the claim depends on fig3a-harris-regular-positive, which is blocked. As computed the absence holds: within the 11 PFC subregions with a Harris score"),
("**Result: not reproduced.** For the dataset part, the tone-responsiveness map","**Result: blocked (too large),** because the claim depends on fig5g-tuned-unit-counts (dataset IBL), which is blocked. The dataset part, as computed, is not reproduced: the tone-responsiveness map"),
("| fig3a-harris-regular-positive | not reproduced |","| fig3a-harris-regular-positive | blocked: methods underspecified (depends on fig2g-pfc-regular-enrichment; not reproduced as computed) |"),
("| supptable5-no-hierarchy-within-pfc | reproduced |","| supptable5-no-hierarchy-within-pfc | blocked: methods underspecified (depends on fig3a; the absence holds as computed) |"),
("| fig5i-map-similarity | not reproduced (dataset part; IBL parts not tested) |","| fig5i-map-similarity | blocked: too large (depends on fig5g-tuned-unit-counts; the dataset part is not reproduced as computed) |")]
for a,b in reps:
    assert a in s, a[:50]; s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n "blocked (methods underspecified),\*\* because\|blocked (too large),\*\*" $TMPDIR/nb_cells.py | cut -c1-120; cd entries/001260-le-merre-2026 && . $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py && cd ../.. && python tools/entry.py check entries/001260-le-merre-2026 | tail -3; date -u
```

```
842:**Result: blocked (methods underspecified),** because the claim depends on fig2g-pfc-regular-enrichment, which is bl
884:**Result: blocked (methods underspecified),** because the claim depends on fig3a-harris-regular-positive, which is b
1397:**Result: blocked (too large),** because the claim depends on fig5g-tuned-unit-counts (dataset IBL), which is block
123 cells
error: claims/001260/10.1038-s41593-025-02190-z.yaml: claims/39: {'id': 'zenodo-unit-link', 'kind': 'link', 'statement': "The paper's per-unit metrics files on Zenodo (record 14205018) can be matched to the dandiset's units, and the matched records agree on what both describe, so that the flatmap position of each unit can be taken from them.", 'source': 'Code availability; github.com/hejDMC/pfcmap at commit 9ae52eddc47fbb590ef4e1b1949507334707a0f1, which reads metrics_files from Zenodo record 14205018 (doi 10.5281/zenodo.14205018)', 'inferred': "Added by the author (protocol, Author, step 1.4) because the flatmap claims need each unit's flatmap position, which the dandiset lacks and the Zenodo metrics files hold.", 'data': 'with_inputs', 'criterion': "Written by the author for the registry's check. Records are matched by recording id (metrics_<recording>.h5) and unit id (uids). The link holds (reproduced) when at least 95% of the dandiset's units are matched and, among them, at least 95% agree on the location label and on the ww/nw label (Zenodo unit_type against the Methods thresholds on the dataset's Peak_to_Trough); partially reproduced when the match holds but agreement is lower; not reproduced when fewer than 95% are matched."} should not be valid under {'required': ['inferred']}
1 error(s)
Sun Nov  1 13:50:18 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
p='claims/001260/10.1038-s41593-025-02190-z.yaml'; s=open(p).read()
a='''  inferred: Added by the author (protocol, Author, step 1.4) because the flatmap claims need each
    unit's flatmap position, which the dandiset lacks and the Zenodo metrics files hold.
'''
b='''  quote: The code used to preprocess the data and generate all manuscript figures is available at
    GitHub via https://github.com/hejDMC/pfcmap/
'''
assert a in s; s=s.replace(a,b); open(p,'w').write(s)
EOF
python tools/entry.py check entries/001260-le-merre-2026 | tail -2; python tools/claims_check.py --help 2>&1 | head -5
```

```
0 error(s)
Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python tools/claims_check.py claims/001260/10.1038-s41593-025-02190-z.yaml paper/10.1038-s41593-025-02190-z.txt 2>&1 | tail -5; date -u; time python tools/entry.py all entries/001260-le-merre-2026 2>&1 | tail -15
```

Result: not kept, because it reads the paper's text.

**Agent**

The full run passed in 905 s. Comparing its outputs with the dev run.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && ls executed/001260-le-merre-2026/ && python - <<'EOF'
import nbformat, re
a=nbformat.read('/tmp/claude-1001/dev_out.ipynb',4); b=nbformat.read('executed/001260-le-merre-2026/reproduce_le_merre_2026.ipynb',4)
def txt(c): return ''.join(o.get('text','') for o in c.get('outputs',[]) if o.output_type=='stream')
nd=0
for x,y in zip(a.cells,b.cells):
    if x.cell_type!='code': continue
    tx,ty=txt(x),txt(y)
    if tx!=ty:
        lx,ly=tx.splitlines(),ty.splitlines()
        d=[(p,q) for p,q in zip(lx,ly) if p!=q]
        nd+=1; print('---', y.metadata.get('tags'), len(d)); 
        for p,q in d[:4]: print(' dev:',p[:150]); print(' run:',q[:150])
    for o in y.get('outputs',[]):
        if o.output_type=='error': print('ERROR',o.ename)
print('cells differing', nd)
EOF
```

```
reproduce_le_merre_2026.ipynb
result.json
--- None 2
 dev: dandiset 001260 version 0.250911.0744: 74 assets, 74 files read, 20374 units, in 1 s
 run: dandiset 001260 version 0.250911.0744: 74 assets, 74 files read, 20374 units, in 177 s
 dev: dandiset 000473 version 0.230417.1502: 25 files, 9408 units, total 1 s
 run: dandiset 000473 version 0.230417.1502: 25 files, 9408 units, total 257 s
--- ['claim:fig5b-tone-categories'] 1
 dev: ZETA on 5232 units in 260 s; failed or empty: 57
 run: ZETA on 5232 units in 270 s; failed or empty: 57
cells differing 2
```

**Agent**

The full run reproduces the dev numbers exactly; only the load timings differ. Writing the entry README and the attempt record.

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required')); 
o=s['properties']['outcomes']['items']; print('outcome props', list(o.get('properties',{}).keys()), o.get('required'))
print(json.dumps(s['properties']['provenance'],indent=0)[:1500])
print(list(s['properties'].keys()))
print(json.dumps(s['properties']['findings']['items'],indent=0)[:800])
print(json.dumps(s['properties']['inputs'],indent=0)[:600])
EOF
```

```
['schema_version', 'id', 'dataset', 'paper', 'date', 'provenance', 'outcomes']
outcome props ['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'proposed'] ['claim', 'outcome']
{
"type": "object",
"additionalProperties": false,
"required": [
"kind",
"accountable"
],
"properties": {
"kind": {
"enum": [
"agent",
"person"
]
},
"accountable": {
"description": "The person or organisation responsible for this attempt.",
"type": "object",
"additionalProperties": false,
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; grep -n "description" $TMPDIR/probe2.py | head -2; . $TMPDIR/dev/bin/activate && cd $TMPDIR && python - <<'EOF'
import json,h5py,remfile,requests,numpy as np
a=json.load(open('assets.json'))['results']
x=[r for r in a if 'PL062-20200420-probe0' in r['path']][0]
f=h5py.File(remfile.File(requests.head(f"https://api.dandiarchive.org/api/assets/{x['asset_id']}/download/",allow_redirects=True).url),'r')
tr=f['intervals/trials']
for k in tr: print(k, dict(tr[k].attrs).get('description'))
print(f['general/extracellular_ephys/electrodes/location'].attrs.get('description'))
EOF
```

```
Sun Nov  1 14:06:16 UTC 2026
10:for k in ['session_description','general/session_id','general/experiment_description','general/stimulus','general/keywords','general/subject/age','general/subject/sex','general/subject/genotype','general/subject/subject_id','general/subject/description','general/surgery','session_start_time']:
Block Block number
id None
lick sound amplitude
sound bolean for sound
sound_amp sound amplitude
sound_freq sound frequency
sound_puretone bolean for pure tone
start_time start time of trial
stop_time end of each trial
valve sound amplitude
my description
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/nb_cells.py'; s=open(p).read()
i=s.index("code(r'''\nep = pd.DataFrame(")
add='''code(r\'\'\'
# Column descriptions of the trials and electrodes tables, one file per setting
first = {}
for r in recs:
    first.setdefault(r["setting"], r)
for sname, r in first.items():
    f = P.open_asset(r["asset_id"])
    tr = f["intervals/trials"]
    desc = {k: P.dec(tr[k].attrs.get("description", "")) for k in tr.keys() if k != "id"}
    sound = tr["sound"][:] if "sound" in tr else None
    el = f["general/extracellular_ephys/electrodes"]
    eld = sorted({P.dec(el[k].attrs.get("description", "")) for k in el.keys() if k != "id"})
    f.close()
    print(f"{sname} ({r['session']}): trials {len(r['onsets'])} onsets; trial columns: {desc}")
    if sound is not None:
        print(f"   'sound' True in {int(np.sum(sound))} of {len(sound)} trials; 10-kHz tones in the file: "
              f"{0 if r['tones'] is None else len(r['tones'])}")
    print(f"   electrode column descriptions: {eld}")
\'\'\', ["sanity"])

md(r\'\'\'
In these files the trials columns `lick` and `valve` are described as "sound amplitude", and the
electrode columns (including `location`, `AP`, `DV`, `ML`) as "my description". The values were
read as their names say: `location` agrees with the paper's Zenodo files for 98.6% of units
(zenodo-unit-link).
\'\'\')

'''
s=s[:i]+add+s[i:]
open(p,'w').write(s)
EOF
cd entries/001260-le-merre-2026 && . $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py && python $TMPDIR/devrun.py && python - <<'EOF'
# run only the new cell quickly in dev, with cached recs
import pickle, numpy as np, pfcki as P
recs=P.classify_epochs(pickle.load(open('/tmp/claude-1001/recs.pkl','rb')))
src=[c for c in __import__('nbformat').read('reproduce_le_merre_2026.ipynb',4).cells if 'Column descriptions' in c.source][0].source
exec(src)
EOF
```

```
125 cells
Aversion (242820_20200526-probe0): trials 250 onsets; trial columns: {'Block': 'Block number', 'airpuff': 'bolean for airpuff', 'airpuff_amp': 'Airpuff volatge control amplitude (V)', 'airpuff_duration': 'Airpuff duration (s)', 'opto_freq': 'pulse train frequency', 'opto_power': 'laser power', 'opto_pulse_duration': 'pulse duration (s)', 'opto_pulse_ts': 'individual pulses timestamps', 'optogenetics': 'bolean for optogenetics', 'sound': 'bolean for sound', 'sound_amp': 'sound amplitude', 'sound_bluenoise': 'bolean for blue noise', 'sound_freq': 'sound frequency', 'sound_puretone': 'bolean for sound', 'start_time': 'start time of trial', 'stop_time': 'end of each trial'}
   'sound' True in 250 of 570 trials; 10-kHz tones in the file: 200
   electrode column descriptions: ['my description']
Detection (518804_20220228-probe0): trials 274 onsets; trial columns: {'Block': 'trial type (0=miss, 1 =hit, 2=cr, 3 =facls)', 'lick': 'sound amplitude', 'sound': 'bolean for sound', 'sound_amp': 'sound amplitude', 'sound_freq': 'sound frequency', 'sound_puretone': 'bolean for pure tone', 'start_time': 'start time of trial', 'stop_time': 'end of each trial', 'valve': 'sound amplitude'}
   'sound' True in 274 of 274 trials; 10-kHz tones in the file: 274
   electrode column descriptions: ['my description']
Passive (708078_20231002-probe0): trials 236 onsets; trial columns: {'Block': 'Block number', 'sound': 'bolean for sound', 'sound_amp': 'sound amplitude', 'sound_freq': 'sound frequency', 'sound_puretone': 'bolean for pure tone', 'start_time': 'start time of trial', 'stop_time': 'end of each trial'}
   'sound' True in 236 of 236 trials; 10-kHz tones in the file: 236
   electrode column descriptions: ['my description']
Context (PL051_20191121-probe0): trials 524 onsets; trial columns: {'Block': 'Block number', 'lick': 'sound amplitude', 'sound': 'bolean for sound', 'sound_amp': 'sound amplitude', 'sound_freq': 'sound frequency', 'sound_puretone': 'bolean for pure tone', 's
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='/tmp/claude-1001/nb_cells.py'; s=open(p).read()
a='''In these files the trials columns `lick` and `valve` are described as "sound amplitude", and the
electrode columns (including `location`, `AP`, `DV`, `ML`) as "my description". The values were
read as their names say: `location` agrees with the paper's Zenodo files for 98.6% of units
(zenodo-unit-link).'''
b='''In the Detection and Context files the trials columns `lick` and `valve` are described as "sound
amplitude"; in the Detection file the `Block` column is described as the trial type (miss, hit,
correct rejection, false alarm), not a block. In the Context file `sound` is False for all 524
trials though the file holds 524 10-kHz tones. The electrode columns (including `location`, `AP`,
`DV`, `ML`) are all described as "my description". The values were read as their names say;
`location` agrees with the paper's Zenodo files for 98.6% of units (zenodo-unit-link). Because the
Detection `Block` column alternates, those recordings are cut into blocks of 50 onsets
(fig2e-category-stability).'''
assert a in s; s=s.replace(a,b); open(p,'w').write(s)
EOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py && cd ../.. && date -u && python tools/entry.py all entries/001260-le-merre-2026 2>&1 | tail -3; date -u
```

```
125 cells
Sun Nov  1 14:06:46 UTC 2026
Installed kernelspec registry-001260-le-merre-2026 in executed/001260-le-merre-2026/.venv/share/jupyter/kernels/registry-001260-le-merre-2026
0 error(s)
pass  reproduce_le_merre_2026.ipynb  (970 s)
Sun Nov  1 14:23:03 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import nbformat
a=nbformat.read('/tmp/claude-1001/dev_out.ipynb',4); b=nbformat.read('executed/001260-le-merre-2026/reproduce_le_merre_2026.ipynb',4)
def txt(c): return ''.join(o.get('text','') for o in c.get('outputs',[]) if o.output_type=='stream')
A={c.source:txt(c) for c in a.cells if c.cell_type=='code'}
nd=0
for y in b.cells:
    if y.cell_type!='code': continue
    for o in y.get('outputs',[]):
        if o.output_type=='error': print('ERROR',o.ename)
    if y.source in A and A[y.source]!=txt(y):
        nd+=1; print('diff in', y.metadata.get('tags'), y.source[:60].replace('\n',' '))
print('differing', nd)
EOF
```

```
diff in ['claim:fig5b-tone-categories'] import multiprocessing as mp from concurrent.futures import 
differing 1
```

**Agent**

Final run passed (970 s) with the same numbers. Writing the README and the attempt record.

**Agent calls Write**

```json
{
 "file_path": "entries/001260-le-merre-2026/README.md",
 "content": "# Le Merre, Heining et al. (2026) from dandiset 001260\n\nTests the findings of [Le Merre, Heining et al. (2026)](https://doi.org/10.1038/s41593-025-02190-z)\non [DANDI:001260](https://dandiarchive.org/dandiset/001260/0.250911.0744). The dandiset holds 74\nof the 99 Neuropixels and Neuronexus recordings of the paper's dataset KI (41 of 66 mice, 20,374\nunits). The other 25 recordings are in dandiset 000473, which is read here for the counts only.\nEach unit's flatmap position, the Harris and Gao hierarchy tables and the flatmap polygons come\nfrom the paper's Zenodo record 10.5281/zenodo.14205018.\n\n| Claim | Outcome |\n|---|---|\n| Unit and recording counts of dataset KI | Partially reproduced |\n| Waveform classes, ww and nw counts and fractions | Partially reproduced |\n| nw units have higher rate, burstiness and memory | Reproduced |\n| Sleep-like epochs differ from active epochs | Reproduced |\n| Sleep-like time and epoch counts | Not reproduced |\n| No linear dependence of burstiness on memory | Not reproduced |\n| SOM gradients; high memory excludes high burstiness | Partially reproduced |\n| PFC units occupy regular, low anti-memory territory | Reproduced |\n| Block-to-block category stability 57% against 18% | Reproduced |\n| Spontaneous region, layer and hierarchy enrichments (Fig. 2f,g, 3c, Extended Data Figs. 3f, 7n) | Blocked: methods underspecified (category numbering) |\n| nw enrichment in ILA, PL, ACAd/v and ORBl | Not reproduced |\n| ww and nw enrichment correspondence | Partially reproduced |\n| Harris hierarchy correlations (Fig. 3a, Supplementary Table 5) | Blocked: depend on a blocked claim |\n| Zenodo metrics files match the dataset's units (link) | Reproduced |\n| 42 dataROIs | Reproduced (with 000473) |\n| dataROI enrichment in ILA, PL, MOs, ORBl | Reproduced |\n| Activity modules, ILA-specific module | Partially reproduced |\n| Category 1 enrichment correlates with Gao hierarchy | Not reproduced |\n| GaoROIs 19, 20, 41 and 23 | Blocked: methods underspecified |\n| Tone response categories | Reproduced |\n| Tone maps cross subregions | Partially reproduced |\n| Tone-responsive patches; no correlation with Gao hierarchy | Reproduced |\n| Tone-responsive units have high spontaneous rates | Not reproduced |\n| Claims on the IBL data (Figs. 2i, 3b, 5g, 5h, 5i, 5k) | Blocked: too large |\n| Firing metrics do not differ across settings | Blocked: methods underspecified |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe files hold every sorted unit of the 99 recordings (with 000473, the 29,782 units the paper\nhad before its quality control) and no label of which units the paper kept. The sleep-like\ndetection of the Methods flags a median 20% of each recording, against 6% in the paper, which\nleaves fewer active epochs and units for every analysis. Which retrained cluster is which of the\npaper's numbered categories is not settled by the paper, and many enrichment claims change\noutcome with it. The attempt record, with the reasons and the differences from the paper's\nmethod, is [`attempts/001260-le-merre-2026-01.yaml`](../../attempts/001260-le-merre-2026-01.yaml).\n"
}
```

```
File created successfully at: entries/001260-le-merre-2026/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u
```

```
Sun Nov  1 14:23:20 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "attempts/001260-le-merre-2026-01.yaml",
 "content": "schema_version: 2\nid: 001260-le-merre-2026-01\ndataset:\n  archive: dandi\n  id: \"001260\"\n  version: 0.250911.0744\n  doi: 10.48324/dandi.001260/0.250911.0744\npaper: doi:10.1038/s41593-025-02190-z\ndate: 2026-11-01\nentry: 001260-le-merre-2026\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-13\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/41306856088\ninputs:\n- what: Dandiset 000473, the 25 aversion recordings of dataset KI that 001260 lacks (the paper's Data\n    availability names both dandisets), read for the unit and recording counts of dataset-ki-counts\n    and fig1h-waveform-classes and the dataROI count of fig4b-dataroi-parcellation.\n  source: doi:10.48324/dandi.000473/0.230417.1502\n- what: The paper's per-unit metrics files (metrics_files.zip, for each unit's flatmap position, the\n    paper's quality flags and ww/nw labels), the flatmap polygons of the PFC subregions, the paper's\n    dataROIs and the 60 GaoROIs (flatmaps.zip), the Harris et al. 2019 hierarchy table\n    (hierarchy_summary_CreConf.xlsx) and the Gao et al. ROI hierarchy index (ROI_Gao_hierarchy_index.csv).\n  source: doi:10.5281/zenodo.14205018\n- what: Method details read from the paper's code (stimulus series per setting, the probe that gives\n    the sleep-like periods of each probe, SOM shape and training, Ward clustering and the cluster\n    relabelling, Harris table columns, tessellation size rule), as cited in the helper module.\n  source: https://github.com/hejDMC/pfcmap at commit 9ae52eddc47fbb590ef4e1b1949507334707a0f1\noutcomes:\n- claim: dataset-ki-counts\n  outcome: partially_reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:dataset-ki-counts\n  measured:\n  - 20354\n  - 53.6\n  - 99\n  - 10900\n  notes: With 000473, dataset KI has the paper's 99 recordings and 53.6% of units in the PFC (52 ± 5.2\n    expected), but under reading (b) and the 12-epoch rule over active epochs 20,354 units (24,248 ±\n    2,425) and 10,900 PFC units (12,674 ± 1,267), both below tolerance. Counting all spontaneous\n    epochs gives 24,898 and 13,040, both within tolerance; the shortfall follows from the larger\n    share of sleep-like epochs found here. Reading (a) gives 4,820 (ISI violation column) or 13,917\n    (false positive column). 001260 alone holds 74 recordings and 14,564 such units, 48.4% PFC.\n  deviations:\n  - The counts use dandiset 000473 as well, as the criterion allows; 001260 alone holds 74 of the 99\n    recordings.\n  - The files carry no quality label; reading (b), all units with at least 12 active epochs of at\n    least 6 spikes, is the main one, as the paper's own flags on Zenodo pass 97% of units.\n- claim: fig1h-waveform-classes\n  outcome: partially_reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig1h-waveform-classes\n  measured:\n  - 15894\n  - 3698\n  - 762\n  - 78.1\n  - 18.2\n  notes: On 001260 + 000473 (reading b) the fractions match (78.1% ww and 18.2% nw of all units, 81.1%\n    and 18.9% of ww plus nw), but the counts are below tolerance (15,894 ww, 3,698 nw, 762\n    unclassified), as the unit total is. The peak-to-trough histogram has modes at 0.26 and 0.64 ms\n    and a minimum at 0.36 ms.\n  deviations:\n  - Peak-to-trough durations are the dataset's Peak_to_Trough column; they agree within 0.001 ms with\n    the paper's Zenodo values for 95.1% of units.\n- claim: fig1i-nw-higher-metrics\n  outcome: reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig1i-nw-higher-metrics\n  notes: nw minus ww is +0.235 in log10FR, +0.052 in B and +0.042 in M, p below 1e-76 for each, 11,209\n    ww and 2,752 nw units from 38 mice. Same sign in every setting and without units of log10FR < 0.1.\n  deviations:\n  - Mixed models fitted by REML in statsmodels and tested by the Wald test of the unit-type\n    coefficient; the paper's Kenward-Roger F test is not available there.\n  - Data of 001260 only (74 of 99 recordings).\n- claim: extfig1d-sleep-like-differ\n  outcome: reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:extfig1d-sleep-like-differ\n  notes: Sleep-like minus active in ww units is -0.027 in log10FR (p = 6.4e-07), +0.029 in B (p =\n    5.3e-64) and -0.013 in M (p = 2.6e-18), from 11,209 active and 10,381 sleep-like samples. With\n    the code's detector all three also differ (p ≤ 0.0012), log10FR with the opposite sign.\n  deviations:\n  - Sleep-like periods detected as the Methods state, from each probe's cortical units or the probe\n    the code's table names; the geometric mean is taken over bins with a positive rate. The code's\n    detector (troughs of 50 ms to 0.6 s, padding of 1 s only for groups of at least 3) is a variant.\n- claim: extfig1-epoch-counts\n  outcome: not_reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:extfig1-epoch-counts\n  measured:\n  - 20.2\n  - 180.5\n  - 125.5\n  - 10381\n  notes: Per probe recording, sleep-like time has a median 20.2% (IQR 8.4 to 33.0%), active epochs\n    180.5 and sleep-like epochs 125.5; per session 21.2%, 160 and 127.5. 12 of 74 recordings are more\n    than half sleep-like. The code's detector gives 8.7%, 203 and 83.5. 10,381 ww units have at least\n    12 sleep-like epochs, just below 11,599 ± 1,160, from 74 of the 99 recordings. In 000473 the\n    median sleep-like time is 23.9%.\n  deviations:\n  - Recording time is from the first to the last spike.\n- claim: extfig1f-burstiness-memory-uncorrelated\n  outcome: not_reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:extfig1f-burstiness-memory-uncorrelated\n  notes: By the paper's test, B ~ M + (1|Mouse) across 11,209 ww units, the slope is -0.19 with p =\n    1.7e-66. The effect is small, marginal R2 0.024 (Pearson r -0.17); with thousands of units a\n    small dependence is significant.\n  deviations:\n  - Wald test in statsmodels in place of the paper's test as implemented in Julia.\n- claim: fig2a-som-memory-burstiness\n  outcome: partially_reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig2a-som-memory-burstiness\n  notes: The gradients of B and log10FR across the ww SOM are at 110 degrees (part 1 holds). Of the top\n    10% memory nodes 3 of 43, and of the top 25% 23 of 107, lie in the top quartile of node B, where\n    the criterion asks for none (part 2 fails under both readings). The criterion defines no partial\n    outcome; partially reproduced is used as the claim holds in part, with both readings agreeing.\n  deviations:\n  - The SOM grid is 17 by 25 (425 nodes), as the code's shape rule gives from 400.\n- claim: fig2b-pfc-regular-territory\n  outcome: reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig2b-pfc-regular-territory\n  measured: 50.5\n  notes: PFC units are 50.5% of the 11,209 ww SOM units and hit all 425 nodes. Median B is -0.055 in\n    PFC against -0.023 elsewhere (Mann-Whitney p = 2.4e-32); M < 0 in 54.1% against 68.2% (chi-square\n    p = 3.6e-53). In the Aversion setting the B difference reverses (-0.105 against -0.111).\n- claim: fig2e-category-stability\n  outcome: reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig2e-category-stability\n  assumed: true\n  measured:\n  - 57.3\n  - 18.4\n  notes: Stability is 57.3% averaged over 13 transitions (59.4% for the pooled matrix), against 18.4%\n    from the marginals; each transition lies between 46.2% and 61.1%. With the code's minimum of 3\n    valid epochs per block it is 49.0% (chance 14.7%). Stability does not depend on the category\n    numbering.\n  deviations:\n  - Assumption. Inherent blocks are runs of the trials table's Block column (20 recordings, where its\n    runs have a median of at least 20 trials), runs of more than 75 epochs split in two; elsewhere\n    consecutive blocks of 50 onsets. The files do not say which settings had blocks, and in Detection\n    files the column holds the trial outcome. Blocks have a median of 25 valid epochs (paper 36).\n- claim: fig2f-low-rate-less-stable\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig2f-low-rate-less-stable\n  notes: The outcome depends on which retrained cluster takes which category number (claims file,\n    G2), and the claims file blocks such a claim. Under the text-matched numbering (b) the mean\n    diagonal of P is 0.430 for categories 1 to 3, 7 and 8 against 0.691 for 4 to 6 (coincidence\n    diagonal agrees), while part 2 holds for 2 of 5 categories, so partially reproduced; under the\n    code's numbering (a) neither part holds (0.613 against 0.387). The question is for the paper's\n    authors (see findings).\n- claim: extfig3f-layer-enrichment\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:extfig3f-layer-enrichment\n  notes: Under G2 b, L2/3 is significantly enriched in categories 6 and 8, L5 in category 2 and L6 in\n    category 1 (reproduced); under G2 a, L5 has no significant positive E-score in categories 1 to 3.\n    Blocked by the claims file's rule on G2.\n- claim: fig2g-pfc-regular-enrichment\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig2g-pfc-regular-enrichment\n  notes: Under G2 b all six subregions are enriched in categories 1 to 3 under both readings and both\n    groupings (reproduced); under G2 a ACAd and ACAv are not (sums of E-scores -4.8 to -1.4), 4 of 6\n    (partially reproduced). Blocked by the claims file's rule on G2.\n- claim: fig2g-ila-pl-category1\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig2g-ila-pl-category1\n  notes: Under G2 b, ILA (E = 8.7 to 9.1) and PL (6.0) are significantly enriched in category 1; under\n    G2 a, ILA is depleted (-3.0 to -3.1). Blocked as its outcome differs under G2, and as it depends on\n    fig2g-pfc-regular-enrichment.\n- claim: fig2g-bursty-orbl-mos-aiv\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig2g-bursty-orbl-mos-aiv\n  notes: Under G2 b, ORBl (E = 3.6 to 3.7) and MOs (4.0 to 4.1) are enriched in category 8, AIv not\n    (P 0.07 to 0.11); under G2 a none is. Blocked as its outcome differs under G2.\n- claim: fig2g-th-hpf-bursty\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig2g-th-hpf-bursty\n  notes: TH and HPF each have one significant positive E-score among categories 6 to 8 under both G2\n    readings (TH 7.1 to 7.3, HPF 3.8 to 4.0), so the criterion's reading (b) holds and reading (a),\n    all three, does not. The criterion blocks the claim when they differ.\n- claim: fig2i-ibl-replication\n  outcome: blocked\n  blocked_by: too_large\n  notes: Needs the spontaneous blocks of the 303 IBL Passive recordings from the IBL Brain Wide Map,\n    spike-sorted per probe, to be fetched and processed. Not started in this run; fetching them would\n    not fit the run's five hours alongside the dataset KI analyses or the notebook's 60-minute limit.\n    It also depends on fig2g-pfc-regular-enrichment, which is blocked.\n- claim: extfig5g-nw-enrichment\n  outcome: not_reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:extfig5g-nw-enrichment\n  notes: The high-rate, lowest-burstiness nw category is 5 (median M 0.018) and the high-rate bursty\n    one 1. ILA (E = -0.5 to -0.6) and PL (-2.0 to -2.1) are not enriched in category 5, and ORBl is not\n    enriched in category 1 (E = 1.5, not significant), under both groupings. 21 regions have more than\n    20 nw units.\n- claim: fig2j-nw-ww-correspondence\n  outcome: partially_reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig2j-nw-ww-correspondence\n  notes: Across 21 regions (9 in the paper) the mean r between ww categories 1 to 3 and the regular nw\n    category is -0.077 to -0.001, not positive, under every reading; the mean r between ww 7 and 8 and\n    the bursty nw category is positive but small (0.040 to 0.115). The criterion defines no partial\n    outcome; partially reproduced is used as one part holds under every reading, weakly.\n  deviations:\n  - More than 20 nw units per region (code's Nmin_maps) gives 21 regions, not 9.\n- claim: fig3a-harris-regular-positive\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig3a-harris-regular-positive\n  notes: Blocked because it depends on fig2g-pfc-regular-enrichment, which is blocked (protocol, Author,\n    step 1.5). As computed it is not reproduced under every reading. Across 15 cortical areas (17 in\n    the paper) category 2 correlates with the Harris score at r = 0.30 to 0.40 (p 0.14 to 0.28) under\n    G2 b and r = -0.17 to 0.05 under G2 a; without groups as the code does, r = 0.30 or 0.05.\n- claim: fig3b-harris-regular-positive-ibl\n  outcome: blocked\n  blocked_by: too_large\n  notes: Needs dataset IBL Passive projected on the SOM (see fig2i-ibl-replication), not started in\n    this run's time; also depends on fig2i-ibl-replication.\n- claim: fig3c-harris-bursty-negative\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig3c-harris-bursty-negative\n  notes: Under G2 b, categories 6 to 8 all correlate negatively with the Harris score (category 6 r =\n    -0.57 to -0.53, p 0.027 to 0.040), more strongly than 1 to 3 (reproduced for dataset KI); under G2\n    a category 6 is positive (r = 0.30 to 0.40). Blocked under G2 and as it depends on fig3a. The IBL\n    part was not tested.\n- claim: supptable5-no-hierarchy-within-pfc\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:supptable5-no-hierarchy-within-pfc\n  notes: Blocked because it depends on fig3a-harris-regular-positive, which is blocked. As computed the\n    absence holds under every reading; within the 11 PFC subregions no category correlates with the\n    Harris score at p < 0.05 (|r| ≤ 0.35, p ≥ 0.28).\n- claim: zenodo-unit-link\n  outcome: reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:zenodo-unit-link\n  notes: All 20,374 units of 001260 match a record of the Zenodo metrics files by recording and unit\n    id. The location label agrees for 98.6% (283 differ, 207 of them in PL064_20200422-probe0) and the\n    ww/nw label for 97.0%; peak-to-trough agrees within 0.001 ms for 95.1%. The paper's quality flags\n    pass 19,808 units. All 9,408 units of 000473 have records too.\n- claim: fig4b-dataroi-parcellation\n  outcome: reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig4b-dataroi-parcellation\n  measured: 38\n  notes: On dataset KI (001260 + 000473), 7,867 deep PFC ww units with a flatmap position give 38\n    dataROIs under either size bound (42 ± 4); the paper's tessellation on Zenodo has 42 polygons. On\n    001260 alone, 4,906 such units give 22 dataROIs, which the dataROI claims below use.\n  deviations:\n  - Uses 000473 for the count, as dataset KI is split across the two dandisets; the Zenodo flatmap\n    positions are an outside input (zenodo-unit-link).\n  - Units are assigned to subregions by the subregion polygons (code), which agree with the location\n    label for 87.7% of units; within a subregion, to the nearest cluster center. The k-means seed is\n    fixed (a standard choice).\n- claim: fig4cd-dataroi-enrichment\n  outcome: reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig4cd-dataroi-enrichment\n  notes: Under both references, both groupings and both G2 readings, a dataROI in ILA and in PL is\n    significantly enriched in category 1 or 3, and one in MOs and in ORBl in category 7 or 8. ORBl is a\n    single dataROI (380 units), so the most ventral part is not tested.\n  deviations:\n  - 22 dataROIs from 001260 alone, against the paper's 42 from all of dataset KI.\n- claim: fig4e-activity-modules\n  outcome: partially_reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig4e-activity-modules\n  notes: The two ILA dataROIs fall in one module under every reading, and three or four other modules\n    hold dataROIs of several subregions. The ILA module also holds two PL, one MOs and one ORBm\n    dataROI, so it is ILA-specific under neither reading. The criterion blocks the claim when the\n    ILA-specific part does not hold under both readings; it fails under both, so the readings agree,\n    and partially reproduced is recorded as the claim holds in part.\n  deviations:\n  - Only 2 ILA dataROIs in 001260.\n- claim: fig4g-gao-category1\n  outcome: not_reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig4g-gao-category1\n  notes: Across 29 GaoROIs (30 in the paper), category 1 enrichment correlates with the Gao hierarchy\n    index at r = 0.20 to 0.33 (p 0.086 to 0.31) under every reading, positive but not significant.\n  deviations:\n  - Data of 001260 only.\n- claim: extfig7n-gao-category6\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:extfig7n-gao-category6\n  notes: Under G2 b category 6 enrichment correlates negatively with the Gao hierarchy (r = -0.62 to\n    -0.54, p ≤ 0.0023, 29 GaoROIs); under G2 a r = 0.03 to 0.11. Blocked by the claims file's rule on G2.\n- claim: fig4g-pl-orbl-extremes\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig4g-pl-orbl-extremes\n  notes: The Gao table gives GaoROI 23 the lowest score and 5, 24, 3 and 2 the highest, not 19, 20 and\n    41. Under G2 b, 20 and 41 are among the three highest category 1 E-scores and the lowest is 6\n    (partially reproduced); under G2 a none of 19, 20 and 41 is in the top three and 23 is the lowest\n    in 6 of 8 readings. The outcome differs between readings.\n- claim: fig5b-tone-categories\n  outcome: reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig5b-tone-categories\n  notes: Under both training readings the flat or negative category 8 is the largest among 5,232 PFC\n    deep ww units (3,114 and 3,788). The IQR of ZETA onsets of responsive units is 3.9 to 35.8 ms in\n    categories 1 to 4 and 90.7 to 284.4 ms in 5 to 7. Recordings keep a median 80 tone epochs (188 in\n    the paper), as more epochs are sleep-like here.\n  deviations:\n  - zetapy 4.1 no longer returns the onset latency; it is computed from zetapy's instantaneous rate as\n    the first crossing of half the peak height, as older zetapy versions did (a standard choice).\n    Seeds are fixed per unit; 57 of 5,232 units had too few tone epochs for ZETA.\n  - Working-memory recordings have no 10-kHz tones and are left out; 8 principal components explain\n    94.1% of the variance (Methods, over 95%).\n- claim: fig5cd-tone-maps-cross-subregions\n  outcome: partially_reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig5cd-tone-maps-cross-subregions\n  notes: Under every reading ACAd and PL each have a dataROI significantly enriched in tone category 1,\n    ORBvl none; the dataROIs of three to five subregions fall in more than one of 4 tone modules. The\n    criterion defines no partial outcome; partially reproduced is used as the claim holds in part under\n    every reading.\n- claim: fig5e-tone-responsive-patches\n  outcome: reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig5e-tone-responsive-patches\n  notes: 1,746 of 3,839 PFC deep ww units are responsive (ZETA P < 0.01). Enriched dataROIs lie in 5 (G1\n    a) or 6 (G1 b) subregions; ACAd and MOs (and PL under G1 a) hold both an enriched and a depleted\n    dataROI.\n- claim: fig5g-tuned-unit-counts\n  outcome: blocked\n  blocked_by: too_large\n  notes: Needs the task data of 66 IBL recordings (16,148 PFC units) from the IBL Brain Wide Map and\n    2,000 within-condition shuffles per unit and variable. Not started in this run's time.\n- claim: fig5g-tuning-maps\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig5g-tuned-unit-counts (dataset IBL), not started.\n- claim: fig5h-choice-gao-hierarchy\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig5g-tuned-unit-counts (dataset IBL), not started.\n- claim: extfig9e-tone-responsive-no-hierarchy\n  outcome: reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:extfig9e-tone-responsive-no-hierarchy\n  notes: Across 25 GaoROIs (29 in the paper), enrichment in responsive units does not correlate with\n    the Gao hierarchy (r = 0.046, p = 0.83, or r = -0.002, p = 0.99).\n- claim: fig5i-map-similarity\n  outcome: blocked\n  blocked_by: too_large\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig5i-map-similarity\n  notes: Blocked because it depends on fig5g-tuned-unit-counts (dataset IBL). The dataset part was\n    computed and is not reproduced; the tone-responsiveness map is most similar to spontaneous category\n    1 (G2 a) or 5 (G2 b, the same cluster), cosine 0.34 or 0.46, never to category 8 (-0.02 to 0.07).\n- claim: fig5j-tone-responsive-high-rate\n  outcome: not_reproduced\n  notebook: reproduce_le_merre_2026.ipynb\n  output: claim:fig5j-tone-responsive-high-rate\n  measured: 3921\n  notes: Tone category 8 has a positive E-score in only 2 or 3 of the five low-rate spontaneous\n    categories under every reading (four required). The summed E-score of tone categories 1 to 7 is\n    positive in spontaneous 4, 5 and 6 only under G2 b with tone reading a; under G2 a it is negative in\n    category 6. 3,921 units have both categories (6,681 for all of dataset KI).\n- claim: fig5k-task-tuning-category4\n  outcome: blocked\n  blocked_by: too_large\n  notes: Depends on fig5g-tuned-unit-counts and fig2i-ibl-replication (dataset IBL), not started.\n- claim: methods-settings-no-difference\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notes: The paper names no test. As a variant in the notebook, Metric ~ Setting + (1|Mouse) for ww\n    units finds Aversion and Detection different from Passive in log10FR (p 0.002 and 0.041), Aversion\n    in B (p 9e-05), Context and Detection in M (p 0.0062 and 1.1e-05); marginal R2 0.019 to 0.043.\nfindings:\n- kind: other\n  statement: Dataset KI is split across two dandisets. 001260 holds 74 recordings, 41 mice and 20,374\n    units; the other 25 recordings (25 mice, 9,408 units) are in 000473, whose title and metadata name\n    a different paper (Esr1+ hypothalamic-habenula neurons). Neither dandiset says it holds part of\n    dataset KI.\n- kind: selection_undocumented\n  statement: The two dandisets hold 29,782 units, the paper's count before its unit quality control,\n    and no field marks the 24,248 units the paper kept. The paper's quality flags are only in its\n    Zenodo metrics files.\n- kind: metadata_insufficient\n  statement: The units table's two-column `quality` is described only as \"ISI violation, false\n    positive rate\". Column 0 runs from 0 to 1.15e5 (median 2), so it is not the ISI violation ratio of\n    the Methods' threshold of 0.1, and its definition is not given.\n- kind: metadata_insufficient\n  statement: The behavioral setting of a recording is not a field; it can be read only from the\n    session description and keywords. The flatmap position of each unit and the paper's ww/nw labels\n    are not in the files and come from the paper's Zenodo record.\n- kind: metadata_error\n  statement: In Detection and Context files the trials columns `lick` and `valve` are described as\n    \"sound amplitude\"; in Detection files `Block` holds the trial outcome (miss, hit, correct\n    rejection, false alarm), not a block. In a Context file `sound` is False for all 524 trials though\n    524 tones were played. Every electrodes column is described as \"my description\".\n- kind: metadata_error\n  statement: For 283 of 20,374 units the location label in the files differs from the paper's Zenodo\n    metrics files (207 of them in PL064_20200422-probe0), and the ww/nw label from the paper's differs\n    for 3.0% of units when the Methods' thresholds are applied to the files' Peak_to_Trough.\n- kind: code_mismatch\n  statement: The Methods detect sleep-like troughs below 0.2 of the geometric mean for longer than 5 ms;\n    the code requires off periods of more than 50 ms and at most 0.6 s, pads only groups of at least 3\n    off periods by 1 s, fills free gaps of 1.5 s or less, and uses only PFC units with at least 75 of\n    them. Both give far more sleep-like time here (median 20.2% or 8.7%) than the paper's 6%.\n- kind: other\n  statement: Following the Methods, sleep-like periods take a median 20.2% of each recording of 001260\n    (6% in the paper), and 12 of 74 recordings are more than half sleep-like, although the paper says\n    recordings dominated by sleep-like states were excluded. Recordings keep a median 180.5 active\n    epochs against the paper's 227.\n- kind: paper_inconsistency\n  statement: The Methods require \"≥4 ISIs in at least 12 separate 3-s epochs\" for unit quality and\n    compute burstiness and memory in epochs \"with at least six spikes (corresponding to at least four\n    ISIs)\", though six spikes give five ISIs. The Methods also say 99 probes were lowered and 24\n    recordings excluded, while Data availability gives 99 recorded sessions, the number the two\n    dandisets hold.\n- kind: methods_unavailable\n  statement: Question for the authors. The paper numbers its spontaneous categories by its own Ward\n    clusters (code, a memory ranking and a fixed permutation) and describes them in words; it gives no\n    rule that carries the numbering to a retrained SOM. Under the code's rule and under a match to the\n    text's descriptions, the outcomes of 9 enrichment claims differ, and they are blocked. Which rule\n    should a reanalysis use, or should units be projected on the trained SOM from Zenodo?\n- kind: methods_unavailable\n  statement: Question for the authors. Which test supports \"firing metric distributions were not\n    significantly different across behavioral settings\"? A mixed model with setting as a fixed effect\n    finds differences here (for example Aversion against Passive in B, p = 9e-05).\n- kind: methods_unavailable\n  statement: Question for the authors. Which recordings had an inherent block structure for the\n    stability analysis, and how is it stored in the files? The Block column holds block numbers in some\n    settings and the trial outcome in Detection.\n"
}
```

```
File created successfully at: attempts/001260-le-merre-2026-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import yaml
d=yaml.safe_load(open('attempts/001260-le-merre-2026-01.yaml'))
def walk(x,path=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,path+'/'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,path+f'[{i}]')
    elif isinstance(x,str):
        if ': ' in x or ' #' in x or '—' in x or 'rather' in x: print('BAD',path,x[:80])
walk(d)
c=yaml.safe_load(open('claims/001260/10.1038-s41593-025-02190-z.yaml'))
ids=[x['id'] for x in c['claims']]; got=[o['claim'] for o in d['outcomes']]
print(set(ids)-set(got), set(got)-set(ids), len(got))
from collections import Counter; print(Counter(o['outcome'] for o in d['outcomes']))
EOF
python tools/entry.py check entries/001260-le-merre-2026 | tail -5; date -u
```

```
set() set() 40
Counter({'blocked': 19, 'reproduced': 10, 'partially_reproduced': 6, 'not_reproduced': 5})
0 error(s)
Sun Nov  1 14:24:54 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
p='attempts/001260-le-merre-2026-01.yaml'; s=open(p).read()
a="text's descriptions, the outcomes of 9 enrichment claims differ, and they are blocked."
assert a in s; s=s.replace(a,"text's descriptions, the outcomes of 8 stability and enrichment claims differ, and they are blocked.")
open(p,'w').write(s)
p='entries/001260-le-merre-2026/README.md'; s=open(p).read()
a="| Spontaneous region, layer and hierarchy enrichments (Fig. 2f,g, 3c, Extended Data Figs. 3f, 7n) |"
assert a in s; s=s.replace(a,"| Category stability and enrichment claims that change with the category numbering (Figs. 2f, 2g, 3c, 4g, Extended Data Figs. 3f, 7n) |")
s=s.replace("| GaoROIs 19, 20, 41 and 23 | Blocked: methods underspecified |\n","")
open(p,'w').write(s)
EOF
grep -n "numbering" entries/001260-le-merre-2026/README.md | head -3; python tools/entry.py check entries/001260-le-merre-2026 | tail -1; python tools/entry.py handover entries/001260-le-merre-2026 2>&1 | tail -5; ls executed/001260-le-merre-2026/handover/
```

```
21:| Category stability and enrichment claims that change with the category numbering (Figs. 2f, 2g, 3c, 4g, Extended Data Figs. 3f, 7n) | Blocked: methods underspecified (category numbering) |
0 error(s)
wrote executed/001260-le-merre-2026/handover
10.1038-s41593-025-02190-z.yaml
pfcki.py
reproduce_le_merre_2026.ipynb
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='entries/001260-le-merre-2026/README.md'; s=open(p).read()
a="| nw enrichment in ILA, PL, ACAd/v and ORBl | Not reproduced |"
s=s.replace(a,"| TH and HPF enriched in bursty categories | Blocked: methods underspecified (the claim's two readings) |\n"+a)
open(p,'w').write(s)
EOF
git status --short; ls entries/001260-le-merre-2026; date -u
```

```
M claims/001260/10.1038-s41593-025-02190-z.yaml
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
?? attempts/001260-le-merre-2026-01.yaml
?? entries/001260-le-merre-2026/
?? scripts
README.md
__pycache__
entry.yaml
pfcki.py
reproduce_le_merre_2026.ipynb
requirements.in
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
rm -rf entries/001260-le-merre-2026/__pycache__; . $TMPDIR/dev/bin/activate && python tools/entry.py check entries/001260-le-merre-2026 | tail -1; python -c "
import nbformat; nb=nbformat.read('entries/001260-le-merre-2026/reproduce_le_merre_2026.ipynb',4); print(sum(len(c.get('outputs',[])) for c in nb.cells if c.cell_type=='code'))"; git diff claims/ | head -60; date -u
```

```
0 error(s)
0
diff --git a/claims/001260/10.1038-s41593-025-02190-z.yaml b/claims/001260/10.1038-s41593-025-02190-z.yaml
index 02e4e111b..8ec671adc 100644
--- a/claims/001260/10.1038-s41593-025-02190-z.yaml
+++ b/claims/001260/10.1038-s41593-025-02190-z.yaml
@@ -515,6 +515,9 @@ claims:
     read, so whether a multiple-comparison correction was applied is unknown; none is applied.
     Reproduced when no category has p < 0.05; not reproduced when any does; r per category given.
 - id: fig4b-dataroi-parcellation
+  data: with_inputs
+  depends_on:
+  - zenodo-unit-link
   statement: The PFC flatmap is parcellated into 42 dataROIs that respect subregion boundaries,
     each holding about 200 deep-layer ww units.
   source: Figure 4b; Extended Data Fig. 7a; Methods, Parcellation into ROIs of similar unit count
@@ -533,6 +536,7 @@ claims:
     positions blocks this and the dataROI and GaoROI claims as data_missing unless those files are
     used as an input (then data with_inputs).
 - id: fig4cd-dataroi-enrichment
[... 43 more lines not kept]
```

**Agent**

I ran steps 1 to 5 of the Author protocol on DANDI:001260 (version 0.250911.0744, the only published version) and ran the handover (step 6). `tools/entry.py check` reports 0 errors and `all` passed, with the notebook running in 970 s. Nothing is committed.

The main finding about the dataset: the paper's dataset KI is split across two dandisets. 001260 holds 74 of the 99 recordings, and the other 25 are in 000473, a dandiset whose metadata names a different paper.

## 1. Outcomes (40 claims, including one link claim I added)

| Claim | Outcome |
|---|---|
| dataset-ki-counts | partially reproduced (99 recordings and 53.6% PFC; 20,354 units against 24,248) |
| fig1h-waveform-classes | partially reproduced (fractions match, counts low) |
| fig1i-nw-higher-metrics | reproduced |
| extfig1d-sleep-like-differ | reproduced |
| extfig1-epoch-counts | not reproduced (20.2% sleep-like time against 6%) |
| extfig1f-burstiness-memory-uncorrelated | not reproduced (p = 1.7e-66, R²m 0.024) |
| fig2a-som-memory-burstiness | partially reproduced |
| fig2b-pfc-regular-territory | reproduced |
| fig2e-category-stability | reproduced (57.3% against 18.4%; rests on an assumption) |
| fig2f, extfig3f, fig2g ×3, fig3c, extfig7n, fig4g-pl-orbl | blocked: methods underspecified (category numbering G2) |
| fig2g-th-hpf-bursty | blocked: methods underspecified (the claim's own two readings disagree) |
| extfig5g-nw-enrichment | not reproduced |
| fig2j-nw-ww-correspondence | partially reproduced |
| fig3a, supptable5 | blocked: depend on a blocked claim (computed: not reproduced; the absence holds) |
| zenodo-unit-link (link) | reproduced |
| fig4b-dataroi-parcellation | reproduced (38 dataROIs with 000473; 22 on 001260 alone) |
| fig4cd-dataroi-enrichment | reproduced |
| fig4e-activity-modules | partially reproduced |
| fig4g-gao-category1 | not reproduced |
| fig5b-tone-categories | reproduced |
| fig5cd-tone-maps-cross-subregions | partially reproduced |
| fig5e-tone-responsive-patches | reproduced |
| extfig9e-tone-responsive-no-hierarchy | reproduced |
| fig5j-tone-responsive-high-rate | not reproduced |
| fig2i, fig3b, fig5g ×2, fig5h, fig5k (IBL data) | blocked: too large, not started |
| fig5i-map-similarity | blocked: too large, through its IBL dependency (the dataset part was computed and is not reproduced) |
| methods-settings-no-difference | blocked: methods underspecified |

Totals: 10 reproduced, 6 partially reproduced, 5 not reproduced, 19 blocked.

## 2. Dataset

**What it holds.**
- 001260 has 74 recordings, 41 mice and 20,374 units.
- With 000473 (25 recordings, 9,408 units, 25 mice) the total is exactly the paper's 29,782 units before its unit quality control, and its 66 mice.
- No field marks which units the paper kept.
- The two-column `quality` field is undescribed; its first column runs up to 1.15e5, so it is not the ISI violation ratio the Methods threshold at 0.1.
- The behavioral setting is only in the free-text session description.

**What has to come from the paper's Zenodo record (10.5281/zenodo.14205018).**
- The flatmap positions and the paper's own quality flags and ww/nw labels are not in the files.
- The Zenodo metrics files match all 20,374 units by recording and unit id.
- Location labels agree for 98.6% of units; 283 differ, 207 of them in one recording.

**Metadata errors.**
- In Detection and Context files, the `lick` and `valve` trial columns are described as "sound amplitude".
- In Detection files, `Block` holds the trial outcome (miss, hit, correct rejection, false alarm), not a block.
- In one Context file, `sound` is False for all 524 trials although 524 tones were played.
- Every electrodes column is described as "my description".

**Sleep-like periods.**
- Following the Methods, sleep-like periods take a median 20.2% of each recording (the paper says 6%).
- 12 of 74 recordings are more than half sleep-like.
- The paper's code uses different parameters (50 ms minimum trough instead of 5 ms, among others), recorded as a code mismatch. It still gives 8.7%.
- This leaves fewer active epochs and units for every analysis, which explains most of the low counts.

**Assumptions.**
- The geometric mean for sleep detection is taken over bins with a positive rate.
- Blocks for the stability analysis come from runs of the `Block` column, or from cuts of 50 onsets.
- Units are not filtered by quality (claims-file reading b), since the paper's own flags pass 97% of units.
- The ZETA onset is computed from zetapy's rate as the first half-peak crossing, because zetapy 4.1 no longer returns it.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
1. What rule carries the category numbering to a retrained SOM?
2. Which test supports "no difference across behavioral settings"?
3. Which recordings had an inherent block structure, and where is it stored?

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. **"A claim that depends on a blocked claim is blocked for the same reason."** Applied literally, this blocks fig3a and supptable5 even though their outcome is the same under both category numberings. It also blocks fig5i as too_large because of its IBL part, although the dataset part ran. I followed the rule and kept the computed results in the notes.
2. **"The criterion decides the outcome," but some criteria define no partial outcome** (fig2a, fig2j, fig4e, fig5cd). I recorded partially reproduced when part of the claim held under every reading, and said so in the notes.
3. **No case for a paper's dataset split across two dandisets, one filed under another paper.** I used 000473 as a pinned input for the counts and the dataROI count only; everything else runs on 001260.
4. **Adding a link claim.** The schema forbids `inferred` on a link claim, so I used a quote from the paper's Code availability. I also set `data: with_inputs` and added the link claim to `depends_on` on 10 reader claims, as the fig4b criterion instructs. The protocol does not say whether the author may edit those fields.
5. **too_large is defined for a computation that was stopped part-way.** It does not fit IBL claims that were never started for lack of time; I used it and said "not started".
6. **The claims file's rule to block when the two category numberings disagree overrides step 1.6**, which would let me adopt the better-supported numbering as an assumption. I followed the claims file. This blocked 8 claims.
7. **The fig4e criterion says "must hold under both [readings], else blocked".** It is ambiguous when both readings fail; I treated agreement on failure as a result, not a block.
8. **Clock check.** I used the post-minus-pre spike rate at true tone onsets against onsets shifted by 1.5 s, on 10 files, in place of decoding.

## 4. Runtime and failures

About 1 h 55 min of the 5 h (12:31 to about 14:26 UTC). The final notebook runs in 970 s; ZETA on 5,232 units takes about 270 s of that. Nothing failed in the final runs. Two dev-run bugs (a histogram index and a missing quote in a cell) were fixed before them.

Unexplained untracked files appeared in the repository root (`.bashrc`, `.profile`, `.idea`, `.vscode`, `scripts` and others). The run's start status was clean and I did not create them, so I left them alone. They should be checked before the workflow commits.

Everything is in `entries/001260-le-merre-2026/` and `attempts/001260-le-merre-2026-01.yaml`. The only change to the claims file is the added link claim and the `data`/`depends_on` fields above. The handover is in `executed/001260-le-merre-2026/handover/`.

## End of run

128 turns, 111 minutes, result: success.
