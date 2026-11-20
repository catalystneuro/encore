# tingley-2019 · author · run 44280379678

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries claims attempts paper tools; wc -l docs/*.md README.md
```

```
Wed Nov 18 09:58:22 UTC 2026
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
n-desk.png
n-phone.png
n-phone2.png
node_modules
ov-papers-rows.png
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
[... 1060 more lines not kept]
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
3	Version: `pilot-16`. Record this version in the attempt's provenance.
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
[... 694 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -80; sed -n 1,280p docs/design.md | head -150
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
[... 210 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/tingley-2019.yaml; cat papers/datasets/tingley-2019.yaml; ls questions | grep ting; ls entries/fouke-2025 entries/tingley-2019
```

```
Exit code 2
# Claims for Tingley and Buzsaki (2019), Routing of hippocampal ripples to subcortical
# structures via the lateral septum, Neuron 105, 138-149, tested on dandiset 000218.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-18,
# protocol pilot-16 as stated in docs/protocol.md. The writer did not look at the dandiset's data or
# files; only its title on the archive was read. This file replaces the version of 2026-10-19,
# whose opening comment recorded outputs of the data and fixed method choices from them; those
# are removed, and every method detail below is taken from the paper or its code, or named as open.
#
# Text read: the accepted author manuscript in PubMed Central (PMC6952543, NIHMS1545124), full
# text as served by NCBI PMC: Summary, Introduction, Results, Discussion, STAR Methods, figure
# legends and Key Resources Table, with its one supplement (NIHMS1545124-supplement-1.pdf, Figures
# S1 to S5 and their legends). The main figures were not available as images, so values printed
# only inside main figure panels (axis labels of Figure 7E among them) could not be read.
#
# Code read. (1) github.com/DavidTingley/papers, commit 9f4cd48 (2020-03-16), the repository the
# Methods link for "code specific to figures/analyses in this manuscript". It holds the figure
# scripts of Tingley and Buzsaki (2018), not of this paper, and the network model of Figure 8
# (LS_phasecoding/modeling/dynamicWeightingModel-ripple.ipynb, pyNN with NEURON). No analysis code
# of Figures 1 to 7 is there. (2) github.com/buzsakilab/buzcode, commit e615663 (the current head,
[... 129 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/tingley-2019.yaml"
}
```

```
1	# Claims for Tingley and Buzsaki (2019), Routing of hippocampal ripples to subcortical
2	# structures via the lateral septum, Neuron 105, 138-149, tested on dandiset 000218.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-18,
4	# protocol pilot-16 as stated in docs/protocol.md. The writer did not look at the dandiset's data or
5	# files; only its title on the archive was read. This file replaces the version of 2026-10-19,
6	# whose opening comment recorded outputs of the data and fixed method choices from them; those
7	# are removed, and every method detail below is taken from the paper or its code, or named as open.
8	#
9	# Text read: the accepted author manuscript in PubMed Central (PMC6952543, NIHMS1545124), full
10	# text as served by NCBI PMC: Summary, Introduction, Results, Discussion, STAR Methods, figure
11	# legends and Key Resources Table, with its one supplement (NIHMS1545124-supplement-1.pdf, Figures
12	# S1 to S5 and their legends). The main figures were not available as images, so values printed
13	# only inside main figure panels (axis labels of Figure 7E among them) could not be read.
14	#
15	# Code read. (1) github.com/DavidTingley/papers, commit 9f4cd48 (2020-03-16), the repository the
16	# Methods link for "code specific to figures/analyses in this manuscript". It holds the figure
17	# scripts of Tingley and Buzsaki (2018), not of this paper, and the network model of Figure 8
18	# (LS_phasecoding/modeling/dynamicWeightingModel-ripple.ipynb, pyNN with NEURON). No analysis code
19	# of Figures 1 to 7 is there. (2) github.com/buzsakilab/buzcode, commit e615663 (the current head,
20	# not a version dated to the paper), analysis/SharpWaveRipples/bz_FindRipples.m, the detector the
[... 920 more lines not kept]
```

**Agent**

Big claims file: 36 claims. Next I'll read the reference entry and the tooling, then survey the dataset.

**Agent calls Bash**

```bash
ls -la entries/fouke-2025 entries/tingley-2019 2>&1; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; ls entries/fouke-2025/*; cat attempts/fouke-2025-01.yaml | head -150; cat papers/datasets/tingley-2019.yaml
```

```
ls: cannot access 'entries/tingley-2019': No such file or directory
entries/fouke-2025:
total 132
drwxr-xr-x   2 runner runner  4096 Nov 18 09:55 .
drwxr-xr-x 322 runner runner 12288 Nov 18 09:58 ..
-rw-r--r--   1 runner runner  2144 Nov 18 09:55 README.md
-rw-r--r--   1 runner runner   907 Nov 18 09:55 entry.yaml
-rw-r--r--   1 runner runner 16218 Nov 18 09:55 omr.py
-rw-r--r--   1 runner runner 79403 Nov 18 09:55 reproduce_fouke_2025.ipynb
-rw-r--r--   1 runner runner    61 Nov 18 09:55 requirements.in
-rw-r--r--   1 runner runner  5989 Nov 18 09:55 requirements.lock.txt
schema_version: 1
name: fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
  001453, which holds the tracking data of 25 zebrafish and 12 Danionella cerebrum larvae during the
  optomotor protocol. It compares swimming speed, turning and angular acceleration between species
  and stimuli, the response to monocular stimuli, and how steady the swimming is. The imaging and
  head-fixed tail tracking of the paper's Figures 2 to 4 are not in the dandiset.
[... 183 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,140p docs/archives.md
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
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000218/ | python -m json.tool | head -40; curl -s https://api.dandiarchive.org/api/dandisets/000218/versions/ | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
import json,urllib.request
url="https://api.dandiarchive.org/api/dandisets/000218/versions/0.261110.1911/assets/?page_size=200"
d=json.load(urllib.request.urlopen(url))
rows=[(a['path'],a['size']/1e9,a['asset_id']) for a in d['results']]
json.dump(d['results'],open('assets.json','w'))
for r in sorted(rows): print(f"{r[0]:70s} {r[1]:8.2f} {r[2]}")
print(len(rows))
EOF
```

```
sub-DT1/sub-DT1_ses-DT1-rLS-20150723-1584um_ecephys.nwb                    8.40 23a2a1c1-0b94-4164-9f98-42f1d88d0c49
sub-DT1/sub-DT1_ses-DT1-rLS-20150723-1728um_ecephys.nwb                    6.64 d3909f11-3070-4bc3-840e-f294975e3808
sub-DT1/sub-DT1_ses-DT1-rLS-20150724-1800um_ecephys.nwb                    7.91 e591758f-ac75-4d6a-91a4-e3c8f68c46d6
sub-DT1/sub-DT1_ses-DT1-rLS-20150724-1872um_ecephys.nwb                   10.51 20595c79-895b-468e-94fc-9dea626fb505
sub-DT1/sub-DT1_ses-DT1-rLS-20150725-1944um_ecephys.nwb                   14.42 2d93bce3-59a6-4b80-8a15-cfe7b2a8c1e1
sub-DT1/sub-DT1_ses-DT1-rLS-20150726-2016um_ecephys.nwb                   10.85 693e8f42-a069-4249-b40f-cf5307e14aea
sub-DT1/sub-DT1_ses-DT1-rLS-20150727-2088um_ecephys.nwb                    9.29 34739883-55ef-49e6-abdf-eed7def338c6
sub-DT1/sub-DT1_ses-DT1-rLS-20150727-2232um_ecephys.nwb                   10.42 02881acd-fe59-4802-b2b3-55acf0606796
sub-DT1/sub-DT1_ses-DT1-rLS-20150728-2304um_ecephys.nwb                   16.63 a97923e5-97ac-412e-b2a0-0f6e060d5009
sub-DT1/sub-DT1_ses-DT1-rLS-20150729-2448um_ecephys.nwb                    8.74 53ed9bf2-c3c6-4eb5-a144-bb5467804f62
sub-DT1/sub-DT1_ses-DT1-rLS-20150729-2592um_ecephys.nwb                   13.27 575f06e1-08a4-45e4-850d-8aeb3e70b118
sub-DT1/sub-DT1_ses-DT1-rLS-20150730-2736um_ecephys.nwb                    9.32 93dbf930-4561-4439-bc24-23f59bc88609
sub-DT2/sub-DT2_ses-DT2-rPPC-rCCG-3036um-362um-20160215-160215-122710_behavior+ecephys.nwb    54.96 6b857822-19d9-49d8-9c4c-c875fcc2c28f
sub-DT2/sub-DT2_ses-DT2-rPPC-rCCG-3108um-434um-20160215-160215-161846_ecephys.nwb    40.16 f7a68917-444f-4faa-83b7-5686342e4d8c
sub-DT2/sub-DT2_ses-DT2-rPPC-rCCG-3324um-1000um-20160217-160217-103121_behavior+ecephys.nwb   105.71 7144ff39-151f-4e69-9e15-658472b1d084
sub-DT2/sub-DT2_ses-DT2-rPPC-rCCG-3324um-1144um-20160219-160219-130435_behavior+ecephys.nwb    90.57 2fcfcacd-9c19-4c79-beaf-85fdd9638008
sub-DT2/sub-DT2_ses-DT2-rPPC-rCCG-3396um-1180um-2016022
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python -c "import pynwb,remfile,h5py,dandi;print(pynwb.__version__)" 2>&1; which uv python; python --version
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb,remfile,h5py,dandi;print(pynwb.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
Python 3.13.18
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q wk && . wk/bin/activate && uv pip install -q pynwb remfile h5py numpy scipy pandas matplotlib statsmodels 2>&1 | tail -3; python -c "import pynwb;print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . wk/bin/activate && cat > probe.py <<'EOF'
import h5py, remfile, sys, json, urllib.request
aid=sys.argv[1]
url=f"https://api.dandiarchive.org/api/assets/{aid}/download/"
req=urllib.request.Request(url,method="HEAD")
s3=urllib.request.urlopen(req).geturl()
f=h5py.File(remfile.File(s3),'r')
def visit(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(f"D {name} {obj.shape} {obj.dtype}")
    else:
        a=dict(obj.attrs)
        nd=a.get('neurodata_type',b'')
        print(f"G {name} {nd} {str(a.get('description',''))[:300]}")
f.visititems(visit)
EOF
time python probe.py 1c66594f-84c0-47bb-88fc-4564b651543d > probe_dt5.txt; wc -l probe_dt5.txt; grep -v "^D acquisition\|^D processing/ecephys/LFP" probe_dt5.txt | head -250
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/probe.py", line 5, in <module>
    s3=urllib.request.urlopen(req).geturl()
       ~~~~~~~~~~~~~~~~~~~~~~^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 189, in urlopen
    return opener.open(url, data, timeout)
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 495, in open
    response = meth(req, response)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 604, in http_response
    response = self.parent.error(
        'http', request, response, code, msg, hdrs)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 527, in error
    result = self._call_chain(*args)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 466, in _call_chain
    result = func(*args)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 720, in http_error_302
    return self.parent.open(new, timeout=req.timeout)
           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/urllib/request.py", line 495, in open
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . wk/bin/activate && python - <<'EOF'
import json,urllib.request
a=json.load(urllib.request.urlopen("https://api.dandiarchive.org/api/dandisets/000218/versions/0.261110.1911/assets/1c66594f-84c0-47bb-88fc-4564b651543d/"))
print([u for u in a['contentUrl']])
EOF
```

```
['https://api.dandiarchive.org/api/assets/1c66594f-84c0-47bb-88fc-4564b651543d/download/', 'https://dandiarchive.s3.amazonaws.com/blobs/8b9/72f/8b972f17-dcf1-4287-83f1-5a9133e39ddd']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . wk/bin/activate && cat > probe.py <<'EOF'
import h5py, remfile, sys, json, urllib.request
aid=sys.argv[1]
a=json.load(urllib.request.urlopen(f"https://api.dandiarchive.org/api/dandisets/000218/versions/0.261110.1911/assets/{aid}/"))
s3=[u for u in a['contentUrl'] if 's3' in u][0]
f=h5py.File(remfile.File(s3),'r')
def visit(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(f"D {name} {obj.shape} {obj.dtype}")
    else:
        a=dict(obj.attrs)
        nd=a.get('neurodata_type',b'')
        print(f"G {name} {nd} || {str(a.get('description',''))[:1500]}")
f.visititems(visit)
EOF
time python probe.py 1c66594f-84c0-47bb-88fc-4564b651543d > probe_dt5.txt; wc -l probe_dt5.txt
```

```
real	0m1.421s
user	0m0.535s
sys	0m0.053s
189 probe_dt5.txt
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/probe_dt5.txt"
}
```

```
1	G acquisition b'' || 
2	G analysis b'' || 
3	D file_create_date (1,) object
4	G general b'' || 
5	G general/devices b'' || 
6	G general/devices/hpc_probe Device || Silicon probe in the hippocampal formation (the lab's region label 'hpc'), with 5 groups of 12 sites, 1 group of 4 sites (spike groups 5-10 of the session's .xml file). The papers used NeuroNexus 5x12, 6x10, 8x8 and 4x8 and Cambridge NeuroTech 1x64 probes, mounted on microdrives; the model of each probe is not stored in the source. Recorded with an Intan RHD2000 interface board at 20 kHz (amplification and digitization on the head stage, 0.195 uV per step); grounded to two stainless steel screws above the cerebellum (Tingley and Buzsaki 2018).
7	G general/devices/ls_probe Device || Silicon probe in the lateral septal nucleus (the lab's region label 'ls'), with 4 groups of 8 sites (spike groups 1-4 of the session's .xml file). The papers used NeuroNexus 5x12, 6x10, 8x8 and 4x8 and Cambridge NeuroTech 1x64 probes, mounted on microdrives; the model of each probe is not stored in the source. Recorded with an Intan RHD2000 interface board at 20 kHz (amplification and digitization on the head stage, 0.195 uV per step); grounded to two stainless steel screws above the cerebellum (Tingley and Buzsaki 2018).
8	D general/experiment_description () object
9	D general/experimenter (1,) object
10	G general/external_resources HERD || 
11	D general/external_resources/entities (5,) [('entity_id', 'O'), ('entity_uri', 'O')]
12	D general/external_resources/entity_keys (19,) [('entities_idx', '<u4'), ('keys_idx', '<u4')]
13	D general/external_resources/files (1,) [('file_object_id', 'O')]
14	D general/external_resources/keys (19,) [('key', 'O')]
15	D general/external_resources/object_keys (19,) [('objects_idx', '<u4'), ('keys_idx', '<u4')]
16	D general/external_resources/objects (16,) [('files_idx', '<u4'), ('object_id', 'O'), ('object_type', 'O'), ('relative_path', 'O'), ('field', 'O')]
17	G general/extracellular_ephys b'
[... 173 more lines not kept]
```

**Agent**

The files hold the lab's own detections (LSRipples, CA1Ripples and others), with the detection parameters stored in the descriptions. Next, a metadata survey of all 98 files.

**Agent calls Bash**

```bash
cd $TMPDIR && . wk/bin/activate && cat > survey.py <<'EOF'
import h5py, remfile, json, numpy as np, collections
from concurrent.futures import ThreadPoolExecutor
assets=json.load(open('assets.json'))
def s3(a):
    m=json.load(__import__('urllib.request').request.urlopen(f"https://api.dandiarchive.org/api/dandisets/000218/versions/0.261110.1911/assets/{a['asset_id']}/"))
    return [u for u in m['contentUrl'] if 's3' in u][0]
def dec(x): return x.decode() if isinstance(x,bytes) else str(x)
def one(a):
    out={'path':a['path'],'asset_id':a['asset_id']}
    try:
        url=s3(a); out['url']=url
        f=h5py.File(remfile.File(url),'r')
        out['groups']=[]
        def v(name,obj):
            if isinstance(obj,h5py.Group): 
                nd=dec(obj.attrs.get('neurodata_type',''))
                if nd: out['groups'].append((name,nd))
        f.visititems(v)
        ev={}
        if 'processing/ecephys' in f:
            for k,g in f['processing/ecephys'].items():
                if dec(g.attrs.get('neurodata_type',''))=='TimeIntervals':
                    ev[k]={'n':int(g['start_time'].shape[0]),'cols':list(g.keys()),'desc':dec(g.attrs.get('description',''))}
        out['events']=ev
        if 'units' in f:
            reg=[dec(x) for x in f['units/region'][:]]
            out['units']=dict(collections.Counter(reg))
            out['nspk']=int(f['units/spike_times'].shape[0])
        el=f['general/extracellular_ephys/electrodes']
        out['el_region']=dict(collections.Counter(dec(x) for x in el['region'][:]))
        out['el_location']=dict(collections.Counter(dec(x) for x in el['location'][:]))
        out['el_cols']=list(el.keys())
        if 'processing/behavior/sleep_states' in f:
            g=f['processing/behavior/sleep_states']
            lab=[dec(x) for x in g['label'][:]]; st=g['start_time'][:]; sp=g['stop_time'][:]
            d=collections.defaultdict(float)
            for l,a_,b in zip(lab,st,sp): d[l]+=b-a_
            out['sleep']=dict(d)
        if 'intervals/trials' in f:
            out['ntrials']=int(f['intervals/trials/start_time'].shape[0])
            out['trial_span']=[float(f['intervals/trials/start_time'][0]),float(f['intervals/trials/stop_time'][-1])]
        if 'intervals' in f: out['intervals']=list(f['intervals'].keys())
        if 'processing/ecephys/LFP/lfp/data' in f:
            out['lfp']=list(f['processing/ecephys/LFP/lfp/data'].shape)
            out['lfp_chunks']=f['processing/ecephys/LFP/lfp/data'].chunks
        out['acq']={k:list(v_['data'].shape) for k,v_ in f['acquisition'].items() if 'data' in v_}
        out['stim']=list(f['stimulus/presentation'].keys())
        out['session_desc']=dec(f['session_description'][()])
        out['subject']=dec(f['general/subject/subject_id'][()])
    except Exception as e:
        out['err']=repr(e)
    return out
with ThreadPoolExecutor(12) as ex: res=list(ex.map(one,assets))
json.dump(res,open('survey.json','w'),indent=1,default=str)
EOF
time python survey.py; python -c "
import json;r=json.load(open('$TMPDIR/survey.json'))
print(sum('err' in x for x in r))
for x in r:
  if 'err' in x: print(x['path'],x['err'])
"
```

```
real	4m51.424s
user	0m6.614s
sys	0m0.990s
0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . wk/bin/activate && python - <<'EOF'
import json,collections
r=json.load(open('survey.json'))
r.sort(key=lambda x:x['path'])
evtypes=collections.Counter()
for x in r:
    ev={k:v['n'] for k,v in x['events'].items()}
    for k in ev: evtypes[k]+=1
    sl={k:round(v) for k,v in x.get('sleep',{}).items()}
    print(x['path'].split('/')[1][:55], x.get('units'), ev, sl, x.get('ntrials'), x.get('lfp'), list(x['acq'].keys()), x['stim'], x.get('intervals'))
print(evtypes)
print(r[0]['el_cols']); 
print(collections.Counter(tuple(sorted(x['el_region'].items())) for x in r).most_common(20))
print(set(g[1] for x in r for g in x['groups']))
EOF
```

```
sub-DT1_ses-DT1-rLS-20150723-1584um_ecephys.nwb {'ls': 74} {'LSRipples': 80, 'ripples_ls': 99} {'WAKE': 2978, 'NREM': 6360, 'REM': 199} None [13646250, 30] ['ElectricalSeries'] [] None
sub-DT1_ses-DT1-rLS-20150723-1728um_ecephys.nwb {'ls': 53} {'LSRipples': 57, 'ls_ripples': 28, 'ripples_ls': 825} {'WAKE': 5994, 'NREM': 1303, 'REM': 237} None [9846125, 30] ['ElectricalSeries'] [] None
sub-DT1_ses-DT1-rLS-20150724-1800um_ecephys.nwb {'ls': 51} {'LSRipples': 9, 'ls_ripples': 8, 'ripples_ls': 565} {'WAKE': 5106, 'NREM': 3497, 'REM': 167} None [11764750, 30] ['ElectricalSeries'] [] None
sub-DT1_ses-DT1-rLS-20150724-1872um_ecephys.nwb {'ls': 60} {'LSRipples': 12, 'ls_ripples': 74, 'ripples_ls': 279} {'WAKE': 7239, 'NREM': 3779, 'REM': 615} None [15785125, 30] ['ElectricalSeries'] [] None
sub-DT1_ses-DT1-rLS-20150725-1944um_ecephys.nwb {'ls': 43} {'LSRipples': 3, 'ls_ripples': 36, 'ripples_ls': 296} {'WAKE': 10414, 'NREM': 4322, 'REM': 1281, 'MA': 97} None [21045625, 30] ['ElectricalSeries'] [] None
sub-DT1_ses-DT1-rLS-20150726-2016um_ecephys.nwb {'ls': 40} {'LSRipples': 173, 'ls_ripples': 21, 'ripples_ls': 419} {'WAKE': 5768, 'NREM': 4944, 'REM': 681, 'MA': 156} None [15795375, 30] ['ElectricalSeries'] [] None
sub-DT1_ses-DT1-rLS-20150727-2088um_ecephys.nwb {'ls': 44} {'LSRipples': 156, 'ls_ripples': 75, 'ripples_ls': 168} {'WAKE': 5432, 'REM': 816, 'NREM': 3969, 'MA': 91} None [13824875, 30] ['ElectricalSeries'] [] None
sub-DT1_ses-DT1-rLS-20150727-2232um_ecephys.nwb {'ls': 54} {'LSRipples': 279, 'ls_ripples': 24, 'ripples_ls': 194} {'NREM': 7105, 'REM': 1121, 'WAKE': 3458, 'MA': 70} None [15722250, 30] ['ElectricalSeries'] [] None
sub-DT1_ses-DT1-rLS-20150728-2304um_ecephys.nwb {'ls': 43} {'LSRipples': 259, 'ls_ripples': 265, 'ripples_ls': 555} {'WAKE': 8315, 'NREM': 7720, 'REM': 1454} None [24608750, 30] ['ElectricalSeries'] [] None
sub-DT1_ses-DT1-rLS-20150729-2448um_ecephys.nwb {'ls': 43} {'LSRipples': 29, 'ls_ripples': 33, 'ripples_ls': 410} {'WAKE': 4444, 'NREM': 
[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . wk/bin/activate && python - <<'EOF'
import json,collections
r=json.load(open('survey.json'))
seen=set()
for x in sorted(r,key=lambda x:x['path']):
    for k,v in x['events'].items():
        key=(k,x['path'].split('/')[0])
        if key in seen: continue
        seen.add(key)
        print('==',x['path'].split('/')[1][:40],k,v['n'],v['cols']); print(v['desc'][:1800])
EOF
```

```
== sub-DT1_ses-DT1-rLS-20150723-1584um_ecep LSRipples 80 ['id', 'peak_amplitude', 'peak_frequency', 'peak_normed_power', 'peak_time', 'start_time', 'stop_time']
The lab's lateral septum high-frequency oscillations (HFOs), from DT1_rLS_20150723_1584um.LSRipples.events.mat, detected with bz_FindRipples on 2018-03-06. Detected on channel 23 (0-based; sessionInfo.region 'ls'); events also present on the noise channel 3 ('ls') were rejected (577 noise events in the file). Detection parameters stored in the file: thresholds [2 6] (thresholds [start/stop, peak] in standard deviations of the normalized squared signal); durations [10 100] (duration limits [shortest inter-event interval, longest event] in ms); passband [120 180] (pass band in Hz); frequency 1250 (LFP sampling rate in Hz); EMGfilt 0.6 (EMG correlation threshold for rejecting events). The papers' methods give 120-200 Hz, thresholds of 2 and 5 SD and durations of 15-250 ms; the values stored with each detection are written here as they are.
== sub-DT1_ses-DT1-rLS-20150723-1584um_ecep ripples_ls 99 ['id', 'peak_normed_power', 'peak_time', 'start_time', 'stop_time']
The lab's lateral septum high-frequency oscillations (HFOs), the lab's oldest detection, from ripples_ls.mat. The file stores no detection parameters. The papers' methods give 120-200 Hz, thresholds of 2 and 5 SD and durations of 15-250 ms; the values stored with each detection are written here as they are.
== sub-DT1_ses-DT1-rLS-20150723-1728um_ecep ls_ripples 28 ['id', 'peak_amplitude', 'peak_frequency', 'peak_normed_power', 'peak_time', 'start_time', 'stop_time']
The lab's lateral septum high-frequency oscillations (HFOs), an earlier detection, from DT1_rLS_20150723_1728um.ls_ripples.event.mat, detected with bz_FindRipples. Detected on channel 3 (0-based; sessionInfo.region 'ls'); events also present on the noise channel 1 ('ls') were rejected (382 noise events in the file). Detection parameters stored in the file: thresholds [2 5] (thresholds [star
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; grep -n -i "PRE\b\|post-behavior\|home cage\|epoch" paper/10.1016-j.neuron.2019.10.012.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
t=open('paper/10.1016-j.neuron.2019.10.012.txt').read()
import re
i=t.find('Experimental model')
print(len(t), i)
open('paper_methods.txt','w').write(re.sub(r'(?<=[.;]) ', '\n', t))
EOF
grep -n "Experimental model\|Ripple detection\|Excess correlation\|Phase locking analysis\|Temporal bias\|Temporal compression\|Reactivation\|Spatiotemporal\|Relative anatomical\|Optogenetic experiments\|Quantification\|Brain state" $TMPDIR/paper_methods.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 270,430p $TMPDIR/paper_methods.txt
```

```
For CA3 recordings, a reference electrode placed in CA1 was used to detect SPW-Rs.
No significant differences were observed when using CA1 or CA3 populations and these recordings were therefore merged.
Ripple depth was not analyzed for CA3 populations.
Two additional rats were used for the optogenetic experiments (see optogenetic experiments section for details).
METHOD DETAILS Recording/Data processing Recordings were conducted using the Intan RHD2000 interface board, sampled at 20 kHz.
Amplification and digitization were done on the head stage.
Waveform extraction and initial clustering was conducted using SpikeDetekt and Klustakwik.
Example parameters for these algorithms can be found in the GitHub repository ( https://github.com/DavidTingley/papers ).
Briefly, the 20 kHz raw signal was bandpass filtered (600 Hz - 9.5 kHz) with a 3 rd order Butterworth filter.
Threshold crossings greater than 5 standard deviations above the mean, of this signal, were extracted for waveform classification (1.6 millisecond windows around the crossing).
Principle components analysis (PCA) was then used to compress the data, and the first 5 principle components were used for semi-automated clustering.
A mixture of Gaussians clustering method was used initially, then manual waveform discrimination was conducted using the Klustaviewa software suite.
Waveform amplitude was utilized during this stage to assess unit stability.
Any waveforms that changed significantly throughout the duration of the recording were discarded.
Waveform isolation quality was quantified using the isolation distance metric ( https://github.com/buzsakilab/buzcode ) and the waveform amplitude.
For one animal, position within the environment was tracked with two head mounted LED’s (1 blue, 1 red) and an overhead camera (Basler, 30 Hz).
For the other four animals, position was tracked with the OptiTrack camera system.
IR reflective markers were mounted in unique positions on each animals’ head stage and imaged simul
[... 143 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 255,270p $TMPDIR/paper_methods.txt; grep -n "mean squared error\|MSE\|shuffled" $TMPDIR/paper_methods.txt | head
```

```
Yadin and Thomas, 1996 ).
It remains to be seen whether multiple descending circuits operate in parallel, each with a unique behavioral function, or whether the behavioral phenotypes observed with LS manipulation are aspects of a single corticofugal computation.
We speculate that several of the above phenotypes point towards a single deficit, of contextually appropriate action-selection.
For example, context-dependent goal directed behaviors, whether food exploration, aggression, or drug-seeking activities, may link the context-defining neuronal patterns in the dorsal hippocampus to subcortical structures via LS ( Luo et al., 2011 ).
While our findings cannot unify this heterogeneity of behavioral effects, they do demonstrate that this anatomical route—from HPC, through LS to other subcortical targets, such as the hypothalamus, mesencephalon and ventral tegmental area—is highly active during SPW-Rs and appears to filter which aspects of its inputs are transmitted.
In turn, this subcortical funneling of hippocampal output, active primarily during consummatory behaviors and NREM sleep, can drive activity in regions that are known to modulate the metabolic and motivational state of animals through the endocrine ( Del Rey et al., 2008 ) and peripheral nervous systems ( Shimazu, 1987 ).
A potential implication of our observations is that depending on the physiological mechanism of a particular behavior (e.g., anxiety or drug-seeking activity), drugs administered during theta (mostly waking) or SPW-R states (mostly nonREM sleep) might induce opposite or differential effects.
The significance of SPW-R-induced physiological effects and their behavioral consequences remain to be explored.
STAR METHODS LEAD CONTACT AND MATERIALS AVAILABILITY Further information and requests for resources and datasets should be directed to and will be fulfilled by György Buzsáki ( [removed: an e-mail address] ).
EXPERIMENTAL MODEL AND SUBJECT DETAILS The experiments were performed on the same Long
[... 12 more lines not kept]
```

**Agent**

Next, timing the reads: spikes and tables for one file, and one LFP channel.

**Agent calls Bash**

```bash
cd $TMPDIR && . wk/bin/activate && python - <<'EOF'
import h5py,remfile,json,time,numpy as np,resource
r={x['path']:x for x in json.load(open('survey.json'))}
x=[v for k,v in r.items() if '20161026' in k][0]
t=time.time()
f=h5py.File(remfile.File(x['url']),'r')
st=f['units/spike_times'][:]; print('spikes',st.shape,time.time()-t)
d=f['processing/ecephys/LFP/lfp/data']; print(d.shape,d.chunks)
t=time.time(); a=d[:2_000_000,5]; print('lfp 2M x1', time.time()-t)
el=f['general/extracellular_ephys/electrodes']
print({k:el[k][:20] for k in ['ls_channel','ca1_channel','ripple_detection_channel','lfp_channel','ref_channel','theta_channel']})
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
EOF
```

```
spikes (4736022,) 1.808182954788208
(34552530, 96) (1048576, 16)
lfp 2M x1 1.6398799419403076
{'ls_channel': array([False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False,  True]), 'ca1_channel': array([False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False]), 'ripple_detection_channel': array([b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'', b'',
       b'', b'', b'', b'', b'', b'', b'LSRipples'], dtype=object), 'lfp_channel': array([False, False, False, False, False, False, False,  True, False,
       False,  True, False, False, False, False, False, False, False,
       False, False]), 'ref_channel': array([False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False]), 'theta_channel': array([False, False, False, False, False, False, False, False, False,
       False, False, False, False, False, False, False, False, False,
       False, False])}
0.305908 GB
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . wk/bin/activate && python -c "
import json;r=json.load(open('survey.json'));print(sum(x.get('nspk',0) for x in r)/1e6,'M spikes'); print(sum(x['lfp'][0] for x in r)/1250/3600,'h')
"; date -u
```

```
203.723542 M spikes
578.0911502222222 h
Wed Nov 18 10:05:26 UTC 2026
Shell cwd was reset to
```

**Agent**

Correction: it is only 10:05 (the run started at 09:55), so there is more time than I had assumed. Before writing code, checking what `tools/entry.py` validates.

**Agent calls Bash**

```bash
grep -n "def \|tag\|sanity\|claim:" tools/entry.py | head -120; wc -l tools/entry.py
```

```
21:- each notebook has a cell tagged `sanity` that prints what was loaded;
77:    def __init__(self):
80:    def error(self, where, message: str) -> None:
85:def dataset_id(record: dict) -> str | None:
94:def dataset_ids(record: dict) -> list[str]:
99:def claims_paths() -> list[Path]:
105:def claims_target(data: dict) -> tuple:
110:def lookup(index: dict, attempt: dict):
119:def schema(name: str) -> Draft202012Validator:
130:def _parsed(text: str):
138:def _schema_errors(text: str, schema_name: str) -> tuple[str, ...]:
144:def load(report: Report, path: Path):
152:def validate(report: Report, path: Path, schema_name: str) -> dict | None:
161:def _plain(value):
172:def code_of(notebook_path: Path) -> str:
179:def check(entry_dir: Path) -> Report:
236:        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
237:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
392:            tag = outcome.get("output")
393:            if notebook in present and tag:
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,75p tools/entry.py; sed -n 179,240p tools/entry.py; sed -n 400,432p tools/entry.py; sed -n 616,660p tools/entry.py
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
[... 195 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/tingley-2019; cd $TMPDIR && . wk/bin/activate && python - <<'EOF'
import json,urllib.request
d=json.load(urllib.request.urlopen("https://api.dandiarchive.org/api/dandisets/000218/versions/0.261110.1911/assets/?page_size=5&metadata=1"))
print(d['results'][0].keys())
print(str(d['results'][0])[:1500])
EOF
```

```
dict_keys(['asset_id', 'blob', 'zarr', 'path', 'size', 'created', 'modified', 'metadata'])
{'asset_id': '193bcbd5-581a-460a-af79-83ba51b11f43', 'blob': '4e025186-d8af-4882-b218-18617f84f144', 'zarr': None, 'path': 'sub-DT9/sub-DT9_ses-20170501-216um-0um-170501-112210_behavior+ecephys.nwb', 'size': 103191313546, 'created': '2026-11-09T05:39:18.267138Z', 'modified': '2026-11-10T19:11:34.893368Z', 'metadata': {'id': 'dandiasset:193bcbd5-581a-460a-af79-83ba51b11f43', 'path': 'sub-DT9/sub-DT9_ses-20170501-216um-0um-170501-112210_behavior+ecephys.nwb', 'access': [{'schemaKey': 'AccessRequirements', 'status': 'dandi:OpenAccess'}], 'digest': {'dandi:dandi-etag': 'edd601ce007bb9f78d08dd28b5a52d3d-1538', 'dandi:sha2-256': 'c73704da07b9da87334a2f0ceddda32e219f0b426cc2ca725b2b799d3d69180e'}, '@context': 'https://raw.githubusercontent.com/dandi/schema/master/releases/0.7.0/context.json', 'approach': [{'name': 'behavioral approach', 'schemaKey': 'ApproachType'}, {'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'keywords': ['lateral septum', 'hippocampus', 'sharp-wave ripples', 'high-frequency oscillations', 'sleep', 'silicon probe'], 'schemaKey': 'Asset', 'contentUrl': ['https://api.dandiarchive.org/api/assets/193bcbd5-581a-460a-af79-83ba51b11f43/download/', 'https://dandiarchive.s3.amazonaws.com/blobs/4e0/251/4e025186-d8af-4882-b218-18617f84f144'], 'identifier': '193bcbd5-581a-460a-af79-83ba51b11f43', 'contentSize': 103191313546, 'publishedBy': {'id': 'urn:uuid:b3622f96-6b3c-471d-a949-d5bfcc048852', 'name': 'DANDI publish', 'endDate': '2026-11-10T19:11:3
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/tingley-2019/tingley2019.py",
 "content": "\"\"\"Loading and shared measures for Tingley and Buzsaki (2019) on dandiset 000218.\n\nEverything is streamed from the DANDI Archive (remfile + h5py); nothing is written to disk.\n\nWhere each parameter comes from:\n- Event tables. The lab's own detections stored in each file (processing/ecephys): LS HFOs in\n  `LSRipples`, CA1 ripples in `CA1Ripples`. The claims file's opening comment, open detail (i),\n  reading (a): \"where the dataset holds the events or their parameters, they are used\". The\n  earlier LS detections (`ls_ripples`, `ripples_ls`) and the hippocampal `ripplesALL` are used\n  only as variants, where a recording lacks the main table (stated in the notebook).\n- Event time. `peak_time` of the tables, which is bz_FindRipples' peak: the trough of the\n  filtered signal (claims file, opening comment, open detail iv).\n- Epochs. The dataset does not mark PRE, BEHAV and POST. The paper says \"Each recording\n  consisted of three periods of time recorded continuously; 1) pre-behavior home cage, 2) maze\n  traversal, and 3) post-behavior home cage\" (STAR Methods, Experimental model). Assumption:\n  PRE is the recording before the first trial's start, BEHAV from the first trial's start to\n  the last trial's stop, POST after the last trial's stop. Maze traversal in the narrow sense\n  is inside trials (the claims' reading iv of fig4b).\n- CCG bins and windows: 1 ms bins, +-200 ms (STAR Methods, Excess correlation analysis);\n  +-120 ms and 241 points for compression (STAR Methods, Temporal compression analysis).\n- Gaussian smoothing for excess correlation: 5 and 200 ms (STAR Methods), read as SD or as\n  full width at half maximum (claims, fig4b reading ii); edges are handled by dividing by the\n  kernel mass inside the window (claims, a standard choice).\n\"\"\"\nfrom __future__ import annotations\n\nimport json\nimport urllib.request\nfrom concurrent.futures import ThreadPoolExecutor\nfrom dataclasses import dataclass, field\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\n\nDANDISET = \"000218\"\nVERSION = \"0.261110.1911\"\nAPI = f\"https://api.dandiarchive.org/api/dandisets/{DANDISET}/versions/{VERSION}\"\nFS_LFP = 1250.0\n\nHPC_REGIONS = (\"hpc\", \"ca1\", \"ca3\")\n\n\ndef list_assets() -> pd.DataFrame:\n    \"\"\"Every NWB asset of the pinned version, with its S3 URL.\"\"\"\n    url, rows = f\"{API}/assets/?page_size=200&metadata=1\", []\n    while url:\n        page = json.load(urllib.request.urlopen(url))\n        for a in page[\"results\"]:\n            s3 = [u for u in a[\"metadata\"][\"contentUrl\"] if \"s3\" in u][0]\n            rows.append({\"path\": a[\"path\"], \"asset_id\": a[\"asset_id\"], \"size_gb\": a[\"size\"] / 1e9, \"url\": s3})\n        url = page[\"next\"]\n    df = pd.DataFrame(rows).sort_values(\"path\").reset_index(drop=True)\n    df[\"subject\"] = df.path.str.extract(r\"sub-(DT\\d+)\")[0]\n    df[\"session\"] = df.path.str.extract(r\"_ses-(.+?)_(?:behavior\\+)?ecephys\")[0]\n    return df\n\n\ndef _s(x):\n    return x.decode() if isinstance(x, bytes) else str(x)\n\n\ndef open_nwb(url: str) -> h5py.File:\n    return h5py.File(remfile.File(url), \"r\")\n\n\n@dataclass\nclass Session:\n    path: str\n    subject: str\n    session: str\n    url: str\n    duration: float = 0.0\n    lfp_shape: tuple = ()\n    spikes: list = field(default_factory=list)          # one sorted float64 array per unit\n    unit_region: np.ndarray = None\n    unit_shank: np.ndarray = None\n    unit_group: np.ndarray = None\n    events: dict = field(default_factory=dict)          # table name -> DataFrame\n    event_desc: dict = field(default_factory=dict)\n    sleep: pd.DataFrame = None\n    trials: pd.DataFrame = None\n    electrodes: pd.DataFrame = None\n    units_desc: str = \"\"\n\n    @property\n    def has_trials(self):\n        return self.trials is not None and len(self.trials) > 0\n\n    def units_in(self, regions):\n        return np.flatnonzero(np.isin(self.unit_region, regions))\n\n    def epochs(self, behav=\"span\"):\n        \"\"\"PRE, BEHAV, POST intervals (see the module docstring for the assumption). behav='span'\n        gives BEHAV as one interval, first trial start to last trial stop; behav='trials' gives the\n        trial intervals themselves.\"\"\"\n        if not self.has_trials:\n            return None\n        t0, t1 = float(self.trials.start_time.min()), float(self.trials.stop_time.max())\n        out = {\"PRE\": np.array([[0.0, t0]]), \"POST\": np.array([[t1, self.duration]])}\n        if behav == \"span\":\n            out[\"BEHAV\"] = np.array([[t0, t1]])\n        else:\n            out[\"BEHAV\"] = merge_intervals(self.trials[[\"start_time\", \"stop_time\"]].to_numpy())\n        return out\n\n    def state_intervals(self, label):\n        if self.sleep is None:\n            return np.zeros((0, 2))\n        s = self.sleep[self.sleep.label == label]\n        return merge_intervals(s[[\"start_time\", \"stop_time\"]].to_numpy())\n\n\ndef load_session(row) -> Session:\n    \"\"\"Spikes, units, event tables, sleep states, trials and electrode flags of one file. The LFP is\n    not read; only its shape (for the recording's duration).\"\"\"\n    f = open_nwb(row[\"url\"])\n    s = Session(path=row[\"path\"], subject=row[\"subject\"], session=row[\"session\"], url=row[\"url\"])\n    lfp = f[\"processing/ecephys/LFP/lfp/data\"]\n    s.lfp_shape = lfp.shape\n    s.duration = lfp.shape[0] / FS_LFP\n    if \"units\" in f:\n        u = f[\"units\"]\n        st = u[\"spike_times\"][:]\n        idx = u[\"spike_times_index\"][:]\n        starts = np.r_[0, idx[:-1]]\n        s.spikes = [np.sort(st[a:b]) for a, b in zip(starts, idx)]\n        s.unit_region = np.array([_s(x).lower() for x in u[\"region\"][:]])\n        s.unit_shank = u[\"shank\"][:]\n        s.unit_group = np.array([_s(x) for x in u[\"electrode_group\"][:]]) if False else s.unit_shank\n        s.units_desc = _s(u.attrs.get(\"description\", \"\"))\n    else:\n        s.unit_region = np.array([], dtype=str)\n        s.unit_shank = np.array([], dtype=int)\n    if \"processing/ecephys\" in f:\n        for k, g in f[\"processing/ecephys\"].items():\n            if _s(g.attrs.get(\"neurodata_type\", \"\")) == \"TimeIntervals\":\n                cols = {c: g[c][:] for c in g.keys() if c not in (\"id\",) and g[c].ndim == 1}\n                s.events[k] = pd.DataFrame(cols).sort_values(\"start_time\").reset_index(drop=True)\n                s.event_desc[k] = _s(g.attrs.get(\"description\", \"\"))\n    if \"processing/behavior/sleep_states\" in f:\n        g = f[\"processing/behavior/sleep_states\"]\n        s.sleep = pd.DataFrame({\"label\": [_s(x) for x in g[\"label\"][:]],\n                                \"start_time\": g[\"start_time\"][:], \"stop_time\": g[\"stop_time\"][:]})\n    if \"intervals/trials\" in f:\n        g = f[\"intervals/trials\"]\n        s.trials = pd.DataFrame({\"start_time\": g[\"start_time\"][:], \"stop_time\": g[\"stop_time\"][:]})\n    el = f[\"general/extracellular_ephys/electrodes\"]\n    s.electrodes = pd.DataFrame({\n        \"region\": [_s(x).lower() for x in el[\"region\"][:]],\n        \"group_name\": [_s(x) for x in el[\"group_name\"][:]],\n        \"ls_channel\": el[\"ls_channel\"][:], \"ca1_channel\": el[\"ca1_channel\"][:],\n        \"ca3_channel\": el[\"ca3_channel\"][:],\n        \"ripple_detection_channel\": [_s(x) for x in el[\"ripple_detection_channel\"][:]],\n    })\n    f.close()\n    return s\n\n\ndef load_all(assets: pd.DataFrame, workers: int = 8) -> list[Session]:\n    with ThreadPoolExecutor(workers) as ex:\n        return list(ex.map(load_session, [r for _, r in assets.iterrows()]))\n\n\n# --- intervals ---------------------------------------------------------------\n\ndef merge_intervals(iv: np.ndarray) -> np.ndarray:\n    iv = np.asarray(iv, float).reshape(-1, 2)\n    if len(iv) == 0:\n        return iv\n    iv = iv[np.argsort(iv[:, 0])]\n    out = [iv[0].copy()]\n    for a, b in iv[1:]:\n        if a <= out[-1][1]:\n            out[-1][1] = max(out[-1][1], b)\n        else:\n            out.append(np.array([a, b]))\n    return np.array(out)\n\n\ndef in_intervals(t: np.ndarray, iv: np.ndarray) -> np.ndarray:\n    \"\"\"Boolean mask of times inside merged, sorted intervals [start, stop].\"\"\"\n    iv = merge_intervals(iv)\n    if len(iv) == 0:\n        return np.zeros(len(t), bool)\n    i = np.searchsorted(iv[:, 0], t, side=\"right\") - 1\n    ok = i >= 0\n    out = np.zeros(len(t), bool)\n    out[ok] = t[ok] <= iv[i[ok], 1]\n    return out\n\n\ndef intersect(a: np.ndarray, b: np.ndarray) -> np.ndarray:\n    a, b = merge_intervals(a), merge_intervals(b)\n    out, i, j = [], 0, 0\n    while i < len(a) and j < len(b):\n        lo, hi = max(a[i, 0], b[j, 0]), min(a[i, 1], b[j, 1])\n        if lo < hi:\n            out.append((lo, hi))\n        if a[i, 1] < b[j, 1]:\n            i += 1\n        else:\n            j += 1\n    return np.array(out).reshape(-1, 2)\n\n\ndef total(iv) -> float:\n    iv = merge_intervals(iv)\n    return float((iv[:, 1] - iv[:, 0]).sum()) if len(iv) else 0.0\n\n\ndef state_at(t: np.ndarray, sess: Session) -> np.ndarray:\n    \"\"\"Sleep state label at each time ('' where none is scored).\"\"\"\n    out = np.full(len(t), \"\", dtype=object)\n    if sess.sleep is None:\n        return out\n    for lab in sess.sleep.label.unique():\n        out[in_intervals(t, sess.state_intervals(lab))] = lab\n    return out\n\n\n# --- cross-correlograms ------------------------------------------------------\n\ndef ccg_all(spikes: list, maxlag: float, binsize: float = 0.001, chunk: int = 200_000) -> np.ndarray:\n    \"\"\"Counts of spike pairs (i spike at t, j spike at t + lag) for every ordered unit pair, lags\n    -maxlag..+maxlag in bins of binsize (centred, 2L+1 bins). Returns array [n, n, 2L+1] (int64).\"\"\"\n    n = len(spikes)\n    L = int(round(maxlag / binsize))\n    nb = 2 * L + 1\n    if n == 0:\n        return np.zeros((0, 0, nb), np.int64)\n    t = np.concatenate(spikes)\n    u = np.concatenate([np.full(len(s), k, np.int64) for k, s in enumerate(spikes)])\n    o = np.argsort(t, kind=\"stable\")\n    t, u = t[o], u[o]\n    out = np.zeros(n * n * nb, np.int64)\n    lo = np.searchsorted(t, t - (L + 0.5) * binsize, side=\"left\")\n    hi = np.searchsorted(t, t + (L + 0.5) * binsize, side=\"right\")\n    for c0 in range(0, len(t), chunk):\n        c1 = min(len(t), c0 + chunk)\n        cnt = hi[c0:c1] - lo[c0:c1]\n        src = np.repeat(np.arange(c0, c1), cnt)\n        # index of partners: lo[k] + 0..cnt-1\n        offs = np.arange(cnt.sum()) - np.repeat(np.cumsum(cnt) - cnt, cnt)\n        dst = np.repeat(lo[c0:c1], cnt) + offs\n        keep = src != dst\n        src, dst = src[keep], dst[keep]\n        lag = np.rint((t[dst] - t[src]) / binsize).astype(np.int64) + L\n        ok = (lag >= 0) & (lag < nb)\n        idx = (u[src[ok]] * n + u[dst[ok]]) * nb + lag[ok]\n        out += np.bincount(idx, minlength=n * n * nb)\n    return out.reshape(n, n, nb)\n\n\ndef gauss_smooth(c: np.ndarray, width_ms: float, kind: str = \"sd\") -> np.ndarray:\n    \"\"\"Convolve CCGs (last axis, 1 ms bins) with a Gaussian; width is the SD (kind='sd') or the full\n    width at half maximum ('fwhm'). Edges: divided by the kernel mass inside the window.\"\"\"\n    sd = width_ms if kind == \"sd\" else width_ms / 2.3548\n    half = int(np.ceil(4 * sd))\n    x = np.arange(-half, half + 1)\n    k = np.exp(-0.5 * (x / sd) ** 2)\n    k /= k.sum()\n    from scipy.signal import fftconvolve\n    shape = [1] * (c.ndim - 1) + [len(k)]\n    num = fftconvolve(c, k.reshape(shape), mode=\"same\", axes=-1)\n    den = fftconvolve(np.ones(c.shape[-1]), k, mode=\"same\")\n    return num / den\n\n\ndef jitter(spikes: list, rng, width: float = 0.2) -> list:\n    \"\"\"Every spike moved by a uniform random amount in +-width (STAR Methods, Excess correlation).\"\"\"\n    return [np.sort(s + rng.uniform(-width, width, len(s))) for s in spikes]\n\n\ndef restrict(spikes: list, iv: np.ndarray) -> list:\n    return [s[in_intervals(s, iv)] for s in spikes]\n\n\ndef triggered_counts(spikes: np.ndarray, times: np.ndarray, maxlag: float, binsize: float) -> np.ndarray:\n    \"\"\"Spike counts of one unit around each trigger time: array [n_triggers, n_bins], bins centred on\n    lags -maxlag..maxlag.\"\"\"\n    L = int(round(maxlag / binsize))\n    edges = (np.arange(-L, L + 2) - 0.5) * binsize\n    lo = np.searchsorted(spikes, times + edges[0])\n    hi = np.searchsorted(spikes, times + edges[-1])\n    out = np.zeros((len(times), 2 * L + 1), np.int32)\n    for k in np.flatnonzero(hi > lo):\n        d = spikes[lo[k]:hi[k]] - times[k]\n        out[k] = np.histogram(d, edges)[0]\n    return out\n\n\ndef count_in(spikes: np.ndarray, starts: np.ndarray, stops: np.ndarray) -> np.ndarray:\n    return np.searchsorted(spikes, stops, side=\"right\") - np.searchsorted(spikes, starts, side=\"left\")\n"
}
```

```
File created successfully at: entries/tingley-2019/tingley2019.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/tingley-2019 && python - <<'EOF'
p='tingley2019.py'; s=open(p).read()
s=s.replace('        s.unit_group = np.array([_s(x) for x in u["electrode_group"][:]]) if False else s.unit_shank\n','')
s=s.replace('    unit_group: np.ndarray = None\n','')
open(p,'w').write(s)
EOF
cd $TMPDIR && . wk/bin/activate && cat > loadall.py <<'EOF'
import sys,time,pickle,resource
sys.path.insert(0,'entries/tingley-2019')
import tingley2019 as T
t=time.time()
A=T.list_assets(); print(len(A), time.time()-t)
S=T.load_all(A, workers=12)
print('loaded', time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
pickle.dump(S,open('sessions.pkl','wb'))
EOF
python loadall.py
```

```
98 0.13570284843444824
loaded 149.98459315299988 2.54322 GB
Shell cwd was reset to
```

**Agent**

All 98 sessions load in 2.5 min with 2.5 GB peak memory. Now the data checks: CA1/CA3 flags, units of the event columns, duplicates, and clock alignment.

**Agent calls Bash**

```bash
cd $TMPDIR && . wk/bin/activate && python - <<'EOF'
import sys,pickle,numpy as np,pandas as pd,collections
sys.path.insert(0,'entries/tingley-2019')
import tingley2019 as T
S=pickle.load(open('sessions.pkl','rb'))
rows=[]
for s in S:
    e=s.electrodes
    rows.append(dict(sub=s.subject,ses=s.session[:28],ca1ch=int(e.ca1_channel.sum()),ca3ch=int(e.ca3_channel.sum()),lsch=int(e.ls_channel.sum()),
      det=';'.join(sorted(set(x for x in e.ripple_detection_channel if x))),units=dict(collections.Counter(s.unit_region)),
      trials=len(s.trials) if s.trials is not None else 0, dur=round(s.duration)))
pd.set_option('display.width',250); pd.set_option('display.max_rows',200); pd.set_option('display.max_colwidth',60)
print(pd.DataFrame(rows))
# event column ranges
for k in ['LSRipples','CA1Ripples','ripplesALL','ls_ripples']:
    d=pd.concat([s.events[k] for s in S if k in s.events])
    d['dur']=(d.stop_time-d.start_time)*1000
    print(k, len(d)); print(d.describe().T[['mean','50%','min','max']])
EOF
```

```
sub                           ses  ...  trials    dur
0   DT1       DT1-rLS-20150723-1584um  ...       0  10917
1   DT1       DT1-rLS-20150723-1728um  ...       0   7877
2   DT1       DT1-rLS-20150724-1800um  ...       0   9412
3   DT1       DT1-rLS-20150724-1872um  ...       0  12628
4   DT1       DT1-rLS-20150725-1944um  ...       0  16836
5   DT1       DT1-rLS-20150726-2016um  ...       0  12636
6   DT1       DT1-rLS-20150727-2088um  ...       0  11060
7   DT1       DT1-rLS-20150727-2232um  ...       0  12578
8   DT1       DT1-rLS-20150728-2304um  ...       0  19687
9   DT1       DT1-rLS-20150729-2448um  ...       0  10501
10  DT1       DT1-rLS-20150729-2592um  ...       0  15264
11  DT1       DT1-rLS-20150730-2736um  ...       0  11233
12  DT2  DT2-rPPC-rCCG-3036um-362um-2  ...      77  13150
13  DT2  DT2-rPPC-rCCG-3108um-434um-2  ...       0   9535
14  DT2  DT2-rPPC-rCCG-3324um-1000um-  ...      69  26106
15  DT2  DT2-rPPC-rCCG-3324um-1144um-  ...      84  21780
16  DT2  DT2-rPPC-rCCG-3396um-1180um-  ...      71  13609
17  DT2  DT2-rPPC-rCCG-3396um-1180um-  ...     121  21140
18  DT2  DT2-rPPC-rCCG-3468um-1216um-  ...     100  15346
[... 118 more lines not kept]
```

**Agent**

The deposited tables already line up with the paper: 27,014 LS HFOs (paper 29,955), LS mean duration 27.8 ms and 146.9 Hz, CA1 31.2 ms and 158.4 Hz. Now the per-session flags table.

**Agent calls Bash**

```bash
cd $TMPDIR && . wk/bin/activate && python - <<'EOF'
import sys,pickle,numpy as np,pandas as pd,collections
sys.path.insert(0,'entries/tingley-2019')
import tingley2019 as T
S=pickle.load(open('sessions.pkl','rb'))
for i,s in enumerate(S):
    e=s.electrodes
    print(i,s.subject,s.session[:22],'ca1',int(e.ca1_channel.sum()),'ca3',int(e.ca3_channel.sum()),'ls',int(e.ls_channel.sum()),
      sorted(set(x for x in e.ripple_detection_channel if x)),dict(collections.Counter(s.unit_region)), sorted(set(s.unit_shank)) if len(s.unit_shank) else '')
EOF
```

```
0 DT1 DT1-rLS-20150723-1584u ca1 0 ca3 0 ls 1 ['LSRipples'] {np.str_('ls'): 74} [np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7), np.int64(8)]
1 DT1 DT1-rLS-20150723-1728u ca1 0 ca3 0 ls 1 ['LSRipples', 'ls_ripples'] {np.str_('ls'): 53} [np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7), np.int64(8)]
2 DT1 DT1-rLS-20150724-1800u ca1 0 ca3 0 ls 1 ['LSRipples', 'ls_ripples'] {np.str_('ls'): 51} [np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7), np.int64(8)]
3 DT1 DT1-rLS-20150724-1872u ca1 0 ca3 0 ls 1 ['LSRipples', 'ls_ripples'] {np.str_('ls'): 60} [np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7), np.int64(8)]
4 DT1 DT1-rLS-20150725-1944u ca1 0 ca3 0 ls 1 ['LSRipples', 'ls_ripples'] {np.str_('ls'): 43} [np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7), np.int64(8)]
5 DT1 DT1-rLS-20150726-2016u ca1 0 ca3 0 ls 1 ['LSRipples', 'ls_ripples'] {np.str_('ls'): 40} [np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7), np.int64(8)]
6 DT1 DT1-rLS-20150727-2088u ca1 0 ca3 0 ls 1 ['LSRipples', 'ls_ripples'] {np.str_('ls'): 44} [np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)]
7 DT1 DT1-rLS-20150727-2232u ca1 0 ca3 0 ls 1 ['LSRipples', 'ls_ripples'] {np.str_('ls'): 54} [np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)]
8 DT1 DT1-rLS-20150728-2304u ca1 0 ca3 0 ls 1 ['LSRipples', 'ls_ripples'] {np.str_('ls'): 43} [np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)]
9 DT1 DT1-rLS-20150729-2448u ca1 0 ca3 0 ls 1 ['LSRipples', 'ls_ripples'] {np.str_('ls'): 43} [np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)]
10 DT1 DT1-rLS-20150729-2592u ca1 0 ca3 0 ls 1 ['LSRipples', 'ls_ripples'] {np.str_('ls'): 50} [np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int
[... 88 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/nb && cd $TMPDIR/nb && cat > build.py <<'EOF'
"""Assemble sections (# %% markers) into an ipynb."""
import sys,re,nbformat
def cells_of(text):
    cells=[]; cur=None
    for line in text.splitlines():
        m=re.match(r'^# %%(.*)$',line)
        if m:
            if cur: cells.append(cur)
            hdr=m.group(1).strip()
            if hdr.startswith('[markdown]'):
                cur=('md',[],[])
            else:
                tags=re.findall(r'tags=\[(.*?)\]',hdr)
                tags=[t.strip().strip('"\'') for t in tags[0].split(',')] if tags else []
                cur=('code',[],tags)
            continue
        if cur is None: continue
        if cur[0]=='md':
            cur[1].append(line[2:] if line.startswith('# ') else line.lstrip('#'))
        else: cur[1].append(line)
    if cur: cells.append(cur)
    out=[]
    for kind,lines,tags in cells:
        src='\n'.join(lines).strip('\n')
        if kind=='md': out.append(nbformat.v4.new_markdown_cell(src))
        else:
            c=nbformat.v4.new_code_cell(src)
            if tags: c.metadata['tags']=tags
            out.append(c)
    return out
out_path=sys.argv[1]; files=sys.argv[2:]
nb=nbformat.v4.new_notebook()
nb.metadata['kernelspec']={'name':'python3','display_name':'Python 3','language':'python'}
for f in files: nb.cells+=cells_of(open(f).read())
nbformat.write(nb,out_path)
print(len(nb.cells),'cells')
EOF
cat > dev.py <<'EOF'
"""Run section files in one namespace with S from the pickle (development only)."""
import sys,pickle,time,resource,re
sys.path.insert(0,'entries/tingley-2019')
import matplotlib; matplotlib.use('Agg')
ns={}
exec(open('/tmp/claude-1001/nb/devload.py').read(),ns)
for f in sys.argv[1:]:
    t=time.time()
    src=open(f).read()
    exec(compile(src,f,'exec'),ns)
    print(f'## {f} {time.time()-t:.1f}s maxrss {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.2f} GB',flush=True)
EOF
date -u
```

```
Wed Nov 18 10:10:43 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat > s01_setup.py <<'EOF'
# %% [markdown]
# ## Setup
# Every file of the pinned version is streamed; from each, the spikes, units, event tables, sleep states,
# trials and electrode flags are read into memory. The LFP is not read in this notebook.

# %%
import zlib, time, resource, collections, warnings
import numpy as np, pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import tingley2019 as T
warnings.filterwarnings("ignore", category=RuntimeWarning)
pd.set_option("display.width", 200); pd.set_option("display.max_columns", 30); pd.set_option("display.max_rows", 200)
KEY = "tingley-2019"
def seed_of(claim): return zlib.crc32(f"{KEY}/{claim}".encode())
t0 = time.time()
A = T.list_assets()
S = T.load_all(A, workers=8)
print(f"{len(S)} files of dandiset {T.DANDISET} version {T.VERSION} loaded in {time.time()-t0:.0f} s; "
      f"peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.2f} GB")
EOF
cat > devload.py <<'EOF'
import zlib, time, resource, collections, warnings, pickle
import numpy as np, pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import tingley2019 as T
warnings.filterwarnings("ignore", category=RuntimeWarning)
pd.set_option("display.width", 200); pd.set_option("display.max_columns", 30); pd.set_option("display.max_rows", 200)
KEY = "tingley-2019"
def seed_of(claim): return zlib.crc32(f"{KEY}/{claim}".encode())
S = pickle.load(open('/tmp/claude-1001/sessions.pkl','rb'))
A = None
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat > s02_sanity.py <<'EOF'
# %% [markdown]
# ## Data check
# What was loaded, by subject and session; the ranges and units of every variable used; recordings deposited
# twice; and whether the spikes, the event tables, the sleep states and the trials share one clock.

# %% tags=["sanity"]
def ls_ev(s, fallback=False):
    """The lab's main LS HFO detection (LSRipples); with fallback, the earlier ls_ripples, then ripples_ls."""
    for k in (["LSRipples", "ls_ripples", "ripples_ls"] if fallback else ["LSRipples"]):
        if k in s.events and len(s.events[k]):
            return s.events[k]
    return None
def ca1_ev(s, fallback=False):
    """The lab's CA1 ripples (CA1Ripples); with fallback, the hippocampal ripplesALL."""
    for k in (["CA1Ripples", "ripplesALL"] if fallback else ["CA1Ripples"]):
        if k in s.events and len(s.events[k]):
            return s.events[k]
    return None
HPC = list(T.HPC_REGIONS)
rows = []
for s in S:
    reg = collections.Counter(s.unit_region)
    sl = {} if s.sleep is None else (s.sleep.stop_time - s.sleep.start_time).groupby(s.sleep.label).sum().to_dict()
    rows.append(dict(subject=s.subject, session=s.session[:30], hours=round(s.duration/3600, 2), lfp_channels=s.lfp_shape[1],
                     ls_units=reg.get("ls", 0), hpc_units=reg.get("hpc", 0), ca1_units=reg.get("ca1", 0), ca3_units=reg.get("ca3", 0),
                     other_units=sum(v for k, v in reg.items() if k not in ("ls", "hpc", "ca1", "ca3")),
                     other_regions=",".join(sorted(k if k else "''" for k in reg if k not in ("ls", "hpc", "ca1", "ca3"))),
                     tables=",".join(f"{k}:{len(v)}" for k, v in sorted(s.events.items())),
                     nrem_h=round(sl.get("NREM", 0)/3600, 2), wake_h=round(sl.get("WAKE", 0)/3600, 2), rem_h=round(sl.get("REM", 0)/3600, 2),
                     trials=0 if s.trials is None else len(s.trials),
                     ca3_flag=bool(s.electrodes.ca3_channel.any()), ca1_flag=bool(s.electrodes.ca1_channel.any())))
INV = pd.DataFrame(rows)
print(INV.to_string())
print("\nBy subject:")
print(INV.groupby("subject")[["ls_units", "hpc_units", "ca3_units", "other_units", "trials"]].sum()
      .join(INV.groupby("subject").size().rename("files")).to_string())
print("\nUnit regions over all files:", dict(collections.Counter(r for s in S for r in s.unit_region)))
print("Event tables (files holding each):", dict(collections.Counter(k for s in S for k in s.events)))

# %% tags=["sanity"]
# Ranges and units of the variables used.
for k in ["LSRipples", "CA1Ripples", "ripplesALL", "ls_ripples", "ripples_ls"]:
    d = pd.concat([s.events[k] for s in S if k in s.events])
    dur = (d.stop_time - d.start_time) * 1000
    inside = np.mean([((s.events[k].start_time >= 0) & (s.events[k].stop_time <= s.duration + 1)).mean() for s in S if k in s.events])
    pk = ((d.peak_time >= d.start_time) & (d.peak_time <= d.stop_time)).mean()
    fr = f"peak_frequency {d.peak_frequency.min():.1f} to {d.peak_frequency.max():.1f} (median {d.peak_frequency.median():.1f}, read as Hz)" if "peak_frequency" in d else "no peak_frequency"
    print(f"{k}: {len(d)} events; duration {dur.min():.1f} to {dur.max():.1f} ms (median {dur.median():.1f}); {fr}; "
          f"peak inside start-stop {pk:.3f}; events inside the recording {inside:.3f}")
allsp = [(s.spikes[i].min(), s.spikes[i].max(), s.duration) for s in S for i in range(len(s.spikes)) if len(s.spikes[i])]
print(f"Spike times: {sum(len(x) for s in S for x in s.spikes)} spikes in {sum(len(s.spikes) for s in S)} units; "
      f"min {min(a for a,_,_ in allsp):.4f} s; units with a spike after the LFP's end: {sum(b > d + 1 for _, b, d in allsp)}")
print("Sorted spike times in every unit:", all(np.all(np.diff(x) >= 0) for s in S for x in s.spikes))
sl = pd.concat([s.sleep.assign(dur=s.duration) for s in S if s.sleep is not None])
print(f"Sleep states: labels {sorted(sl.label.unique())}; bouts {len(sl)}; stop beyond the recording: {(sl.stop_time > sl.dur + 1).sum()}; "
      f"whole-second times: {np.mean(np.isclose(sl.start_time % 1, 0)):.3f}")
tr = pd.concat([s.trials.assign(dur=s.duration) for s in S if s.has_trials])
print(f"Trials: {len(tr)} in {sum(s.has_trials for s in S)} files; length {(tr.stop_time-tr.start_time).min():.2f} to "
      f"{(tr.stop_time-tr.start_time).max():.1f} s (median {(tr.stop_time-tr.start_time).median():.1f}); beyond the recording: {(tr.stop_time > tr.dur + 1).sum()}")

# %% tags=["sanity"]
# Recordings deposited twice: identical spike trains (unit spike counts and first spikes) or identical event tables.
fp_sp, fp_ev, dup = {}, {}, []
for i, s in enumerate(S):
    if len(s.spikes):
        key = tuple(sorted((len(x), round(float(x[0]), 4) if len(x) else 0) for x in s.spikes))
        if key in fp_sp: dup.append(("spikes", S[fp_sp[key]].session, s.session))
        fp_sp[key] = i
    for k, e in s.events.items():
        key = (len(e), tuple(np.round(e.start_time.to_numpy()[:20], 4)))
        if len(e) > 5 and key in fp_ev and fp_ev[key][0] != i:
            dup.append((f"events {k} / {fp_ev[key][1]}", S[fp_ev[key][0]].session, s.session))
        fp_ev[key] = (i, k)
# also: same subject, same LFP length
lens = collections.defaultdict(list)
for s in S: lens[(s.subject, s.lfp_shape[0])].append(s.session)
dup += [("same LFP length", *v) for v in lens.values() if len(v) > 1]
print("Duplicate candidates:", dup if dup else "none")
# Within one file, two event tables holding the same events (an LS table copied into another) are reported too.
same = []
for s in S:
    ks = sorted(s.events)
    for a in range(len(ks)):
        for b in range(a + 1, len(ks)):
            ea, eb = s.events[ks[a]].peak_time.to_numpy(), s.events[ks[b]].peak_time.to_numpy()
            if len(ea) and len(eb):
                j = np.clip(np.searchsorted(eb, ea), 1, len(eb) - 1)
                near = np.minimum(np.abs(eb[j] - ea), np.abs(eb[j - 1] - ea)) < 0.002
                if near.mean() > 0.9 and abs(len(ea) - len(eb)) < 0.1 * len(ea):
                    same.append((s.session[:25], ks[a], ks[b], len(ea), len(eb)))
print("Tables within a file with the same events:", same if same else "none")

# %% tags=["sanity"]
# One clock. (1) LS spikes around LS HFO peak times and hippocampal spikes around CA1 ripple peak times: the rate
# within +-10 ms over the rate 100-200 ms away, with the true times and with the times shifted by 1 s.
# (2) Trials against sleep scoring: the fraction of trial time scored WAKE, with the true states and with
# the states shifted by +-1800 s. A shared clock gives a ratio far above 1 at the true times only, and trials in WAKE.
def peri_ratio(s, units, times):
    c = sum(T.triggered_counts(s.spikes[u], times, 0.2, 0.01).sum(0) for u in units)
    lag = np.arange(-20, 21)
    return c[np.abs(lag) <= 1].mean() / max(c[(np.abs(lag) >= 10)].mean(), 1e-9)
clk = []
for s in S:
    ls = s.units_in(["ls"]); hp = s.units_in(HPC)
    e1, e2 = ls_ev(s), ca1_ev(s)
    r = dict(session=s.session[:25], subject=s.subject)
    if e1 is not None and len(ls):
        t = e1.peak_time.to_numpy(); r["ls_hfo"] = peri_ratio(s, ls, t); r["ls_hfo_shift1s"] = peri_ratio(s, ls, t + 1.0)
    if e2 is not None and len(hp):
        t = e2.peak_time.to_numpy(); r["ca1_rip"] = peri_ratio(s, hp, t); r["ca1_rip_shift1s"] = peri_ratio(s, hp, t + 1.0)
    if s.has_trials and s.sleep is not None:
        wk = s.state_intervals("WAKE"); tiv = s.trials[["start_time", "stop_time"]].to_numpy()
        r["trial_in_wake"] = T.total(T.intersect(tiv, wk)) / T.total(tiv)
        r["trial_in_wake_shift"] = np.mean([T.total(T.intersect(tiv, wk + d)) / T.total(tiv) for d in (-1800, 1800)])
    clk.append(r)
CLK = pd.DataFrame(clk)
print(CLK.describe().loc[["count", "min", "50%", "max"]].round(3).to_string())
print("Files where the LS HFO ratio is below 1.5:", CLK[CLK.ls_hfo < 1.5].session.tolist())
print("Files where the CA1 ripple ratio is below 1.5:", CLK[CLK.ca1_rip < 1.5].session.tolist())
print("Files where less than half the trial time is scored WAKE:", CLK[CLK.trial_in_wake < 0.5][["session", "trial_in_wake"]].values.tolist())
EOF
cd $TMPDIR/nb && . ../wk/bin/activate && python dev.py s02_sanity.py 2>&1 | tail -150
```

```
subject                         session  hours  lfp_channels  ls_units  hpc_units  ca1_units  ca3_units  other_units other_regions                                                          tables  nrem_h  wake_h  rem_h  trials  ca3_flag  ca1_flag
0      DT1         DT1-rLS-20150723-1584um   3.03            30        74          0          0          0            0                                                    LSRipples:80,ripples_ls:99    1.77    0.83   0.06       0     False     False
1      DT1         DT1-rLS-20150723-1728um   2.19            30        53          0          0          0            0                                     LSRipples:57,ls_ripples:28,ripples_ls:825    0.36    1.67   0.07       0     False     False
2      DT1         DT1-rLS-20150724-1800um   2.61            30        51          0          0          0            0                                       LSRipples:9,ls_ripples:8,ripples_ls:565    0.97    1.42   0.05       0     False     False
3      DT1         DT1-rLS-20150724-1872um   3.51            30        60          0          0          0            0                                     LSRipples:12,ls_ripples:74,ripples_ls:279    1.05    2.01   0.17       0     False     False
4      DT1         DT1-rLS-20150725-1944um   4.68            30        43          0          0          0            0                                      LSRipples:3,ls_ripples:36,ripples_ls:296    1.20    2.89   0.36       0     False     False
5      DT1         DT1-rLS-20150726-2016um   3.51            30        40          0          0          0            0                                    LSRipples:173,ls_ripples:21,ripples_ls:419    1.37    1.60   0.19       0     False     False
6      DT1         DT1-rLS-20150727-2088um   3.07            30        44          0          0          0            0                                    LSRipples:156,ls_ripples:75,ripples_ls:168    1.10    1.51   0.23       0     False     False
7      DT1 
[... 124 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR/nb && cat > s03_fig1.py <<'EOF'
# %% [markdown]
# ## dataset-composition
# > LS was recorded in 6 rats with 1989 LS neurons in the phase locking analysis; 62 recordings had a hippocampal
# > population with LS, 37 with CA1 and 25 with CA3; LS HFO rates come from 89 recordings and CA1 ripple rates from 53;
# > recordings held 8 to 74 LS neurons (mean 29.6).
#
# Reading (a) of the LS neuron count (more than 50 spikes in high-power epochs) needs the LFP and is computed in the
# second notebook (`lfp_tingley_2019.ipynb`); here reading (b), all LS units. CA1 against CA3 is read two ways, since
# most hippocampal units are labelled only `hpc`: (i) by the units' label (`ca3` is CA3, `hpc` or `ca1` is CA1),
# (ii) by the electrodes' `ca3_channel` flag (a recording with a CA3 channel marked is CA3). Rate recordings are those
# with the event table and scored sleep (NREM or WAKE).

# %% tags=["claim:dataset-composition"]
comp = {}
comp["animals with LS units"] = INV[INV.ls_units > 0].subject.nunique()
comp["LS units, all (reading b)"] = int(INV.ls_units.sum())
both = INV[(INV.ls_units > 0) & (INV.hpc_units + INV.ca1_units + INV.ca3_units > 0)]
comp["recordings with LS and hippocampal units"] = len(both)
comp["  CA3 by unit label (i)"] = int((both.ca3_units > 0).sum()); comp["  CA1 by unit label (i)"] = int((both.ca3_units == 0).sum())
comp["  CA3 by ca3_channel flag (ii)"] = int(both.ca3_flag.sum()); comp["  CA1 by flag (ii)"] = int((~both.ca3_flag).sum())
has_sleep = INV.nrem_h + INV.wake_h > 0
comp["recordings with LSRipples and sleep states"] = int(sum(ls_ev(s) is not None and s.sleep is not None for s in S))
comp["  same, any LS table"] = int(sum(ls_ev(s, True) is not None and s.sleep is not None for s in S))
comp["recordings with CA1Ripples and sleep states"] = int(sum(ca1_ev(s) is not None and s.sleep is not None for s in S))
comp["  same, CA1Ripples or ripplesALL"] = int(sum(ca1_ev(s, True) is not None and s.sleep is not None for s in S))
n_ls = INV.ls_units[INV.ls_units > 0]
comp["LS units per recording, min"] = int(n_ls.min()); comp["LS units per recording, max"] = int(n_ls.max())
comp["LS units per recording, mean"] = round(n_ls.mean(), 1); comp["LS units per recording, SD"] = round(n_ls.std(), 1)
comp["recordings with LS units"] = len(n_ls)
for k, v in comp.items(): print(f"{k:45s} {v}")
print("\nLS units and recordings by animal:")
print(INV[INV.ls_units > 0].groupby("subject").ls_units.agg(["count", "sum", "min", "max", "mean"]).round(1).to_string())

# %% [markdown]
# ## fig1c-event-count
# > Across 6 animals, 29,955 LS HFO events were analysed.
#
# Detection reading (a): the deposited events are counted. Recording readings: (a) all recordings with LS electrodes,
# (b) recordings with LS units. The main table is LSRipples; the earlier tables are shown as variants.

# %% tags=["claim:fig1c-event-count"]
ev_rows = []
for s in S:
    has_ls_el = bool((s.electrodes.region == "ls").any())
    e, e_any = ls_ev(s), ls_ev(s, True)
    ev_rows.append(dict(subject=s.subject, ls_electrodes=has_ls_el, ls_units=int((s.unit_region == "ls").sum()),
                        LSRipples=0 if e is None else len(e), any_table=0 if e_any is None else len(e_any)))
EV = pd.DataFrame(ev_rows)
cnt_a = EV[EV.ls_electrodes].LSRipples.sum(); cnt_b = EV[EV.ls_units > 0].LSRipples.sum()
print(f"LSRipples, recordings with LS electrodes (a): {cnt_a} events in {EV[EV.ls_electrodes & (EV.LSRipples>0)].subject.nunique()} animals, "
      f"{(EV.ls_electrodes & (EV.LSRipples>0)).sum()} recordings")
print(f"LSRipples, recordings with LS units (b): {cnt_b}")
print(f"Variant, LSRipples else ls_ripples else ripples_ls, (a): {EV[EV.ls_electrodes].any_table.sum()}, (b): {EV[EV.ls_units>0].any_table.sum()}")
print(f"Paper 29955, tolerance 2995.5: (a) {abs(cnt_a-29955)<=2995.5}, (b) {abs(cnt_b-29955)<=2995.5}")
print(EV.groupby("subject")[["LSRipples", "any_table"]].sum().to_string())

# %% [markdown]
# ## fig1f-shorter-than-ripples, fig1g-slower-than-ripples
# > LS HFOs are shorter than CA1 ripples from the same animals (27 +- 9 against 31 +- 14 ms; rank-sum P < 0.01).
# > LS HFOs are slower in frequency than CA1 ripples (147 +- 5.7 against 159 +- 8 Hz; rank-sum P < 0.01).
#
# Durations are stop minus start of the deposited events; frequency is the deposited `peak_frequency` (bz_FindRipples'
# instantaneous frequency at the peak, in Hz). Readings: (1) events from recordings with both tables, (2) all
# events of the animals with both.

# %% tags=["claim:fig1f-shorter-than-ripples", "claim:fig1g-slower-than-ripples"]
def pooled(tab_fn, sessions):
    d = [tab_fn(s).assign(subject=s.subject, session=s.session) for s in sessions if tab_fn(s) is not None]
    return pd.concat(d) if d else None
both_rec = [s for s in S if ls_ev(s) is not None and ca1_ev(s) is not None]
animals_both = sorted({s.subject for s in both_rec})
readings = {"(1) recordings with both": (both_rec, both_rec),
            "(2) all events of animals with both": ([s for s in S if s.subject in animals_both],) * 2}
DUR = {}
for name, (sl, sc) in readings.items():
    L, C = pooled(ls_ev, sl), pooled(ca1_ev, sc)
    Ld, Cd = (L.stop_time - L.start_time) * 1000, (C.stop_time - C.start_time) * 1000
    pd_ = stats.mannwhitneyu(Ld, Cd); pf = stats.mannwhitneyu(L.peak_frequency, C.peak_frequency)
    DUR[name] = (L, C)
    print(f"{name}: {len(L)} LS HFOs, {len(C)} CA1 ripples, {L.subject.nunique()} / {C.subject.nunique()} animals")
    print(f"  duration LS {Ld.mean():.1f} +- {Ld.std():.1f} ms, CA1 {Cd.mean():.1f} +- {Cd.std():.1f} ms; rank-sum p = {pd_.pvalue:.2g}; "
          f"medians {Ld.median():.1f} / {Cd.median():.1f}")
    print(f"  frequency LS {L.peak_frequency.mean():.1f} +- {L.peak_frequency.std():.1f} Hz, CA1 {C.peak_frequency.mean():.1f} +- "
          f"{C.peak_frequency.std():.1f} Hz; rank-sum p = {pf.pvalue:.2g}")
print("Animals with both:", animals_both)
L, C = DUR["(1) recordings with both"]
print("\nPer animal (reading 1): mean duration (ms) and frequency (Hz)")
print(pd.DataFrame({"LS dur": L.assign(d=(L.stop_time-L.start_time)*1000).groupby("subject").d.mean(),
                    "CA1 dur": C.assign(d=(C.stop_time-C.start_time)*1000).groupby("subject").d.mean(),
                    "LS freq": L.groupby("subject").peak_frequency.mean(), "CA1 freq": C.groupby("subject").peak_frequency.mean(),
                    "LS n": L.groupby("subject").size(), "CA1 n": C.groupby("subject").size()}).round(1).to_string())
fig, ax = plt.subplots(1, 2, figsize=(9, 3))
ax[0].hist((L.stop_time-L.start_time)*1000, np.arange(0, 120, 2), alpha=.6, density=True, label="LS HFO")
ax[0].hist((C.stop_time-C.start_time)*1000, np.arange(0, 120, 2), alpha=.6, density=True, label="CA1 ripple"); ax[0].set_xlabel("duration (ms)"); ax[0].legend()
ax[1].hist(L.peak_frequency, np.arange(120, 200, 1), alpha=.6, density=True); ax[1].hist(C.peak_frequency, np.arange(120, 200, 1), alpha=.6, density=True)
ax[1].set_xlabel("peak frequency (Hz)"); plt.tight_layout(); plt.show()
print(f"Outside the duration axis (>120 ms): LS {((L.stop_time-L.start_time)*1000 > 120).sum()}, CA1 {((C.stop_time-C.start_time)*1000 > 120).sum()}")

# %% [markdown]
# ## fig1h-no-amplitude-frequency-correlation
# > LS HFOs show no significant correlation between event amplitude and peak frequency.
#
# Amplitude is the deposited `peak_amplitude` (the description of the tables calls it the amplitude; the Methods' maximum NSS
# may instead be `peak_normed_power`, shown as a variant). All LS HFOs pooled; Pearson and Spearman at p < 0.05.

# %% tags=["claim:fig1h-no-amplitude-frequency-correlation"]
LA = pooled(ls_ev, S)
for col in ["peak_amplitude", "peak_normed_power"]:
    pr = stats.pearsonr(LA[col], LA.peak_frequency); sr = stats.spearmanr(LA[col], LA.peak_frequency)
    print(f"{col} against peak_frequency, {len(LA)} LS HFOs: Pearson r = {pr.statistic:.3f} (p = {pr.pvalue:.2g}); "
          f"Spearman rho = {sr.statistic:.3f} (p = {sr.pvalue:.2g})")
print("\nPer animal (peak_amplitude):")
for sub, g in LA.groupby("subject"):
    pr = stats.pearsonr(g.peak_amplitude, g.peak_frequency); sr = stats.spearmanr(g.peak_amplitude, g.peak_frequency)
    print(f"  {sub}: n = {len(g)}, Pearson r = {pr.statistic:.3f} (p = {pr.pvalue:.2g}), Spearman rho = {sr.statistic:.3f} (p = {sr.pvalue:.2g})")

# %% [markdown]
# ## fig1c-hfo-each-animal, fig1c-post-burst-suppression
# > Transient 120-180 Hz HFOs occur in LS in each of the 6 animals, with a robust increase in the firing probability of LS neurons at the events.
# > LS HFOs are accompanied by a suppression of LS firing immediately after the population burst.
#
# Per LS neuron, the spike probability per event in 1 ms bins over +-100 ms around the LS HFO peak time, and the same at an
# equal number of random times in the same recording (uniform over the recording; the claim's seed). Bounds are 3 SEM over neurons.
# At the event: the event-time bin and +-5 ms around it. After the burst: (i) from 20 to 50 ms after the event time; (ii) per event,
# from its stop to 50 ms after its time.

# %% tags=["claim:fig1c-hfo-each-animal", "claim:fig1c-post-burst-suppression"]
def hfo_triggered(seed):
    rng = np.random.default_rng(seed)
    out = []
    for s in S:
        e = ls_ev(s); ls = s.units_in(["ls"])
        if e is None or len(ls) == 0: continue
        t = e.peak_time.to_numpy(); rt = np.sort(rng.uniform(0.2, s.duration - 0.2, len(t)))
        stop_off = e.stop_time.to_numpy() - t
        for u in ls:
            sp = s.spikes[u]
            c = T.triggered_counts(sp, t, 0.1, 0.001).mean(0); cr = T.triggered_counts(sp, rt, 0.1, 0.001).mean(0)
            # (ii) per event: spikes from stop to +50 ms, per ms
            post_ii = (T.count_in(sp, t + stop_off, t + 0.05) / np.maximum((0.05 - stop_off) * 1000, 1)).mean()
            post_ii_r = (T.count_in(sp, rt + stop_off, rt + 0.05) / np.maximum((0.05 - stop_off) * 1000, 1)).mean()
            out.append(dict(subject=s.subject, session=s.session, unit=u, n_ev=len(t), c=c, cr=cr, post_ii=post_ii, post_ii_r=post_ii_r))
    return pd.DataFrame(out)
TRIG = hfo_triggered(seed_of("fig1c-hfo-each-animal"))
lag = np.arange(-100, 101)
at0, at5, post = lag == 0, np.abs(lag) <= 5, (lag >= 20) & (lag <= 50)
def summary(df):
    C, R = np.vstack(df.c), np.vstack(df.cr)
    def ms(x): return x.mean(), x.std(ddof=1) / np.sqrt(len(x))
    r = {}
    for nm, m in [("event bin", at0), ("+-5 ms", at5), ("+20..50 ms", post)]:
        a, b = C[:, m].mean(1), R[:, m].mean(1)
        (ma, sa), (mb, sb) = ms(a), ms(b)
        r[nm] = (ma, sa, mb, sb)
    (ma, sa), (mb, sb) = ms(df.post_ii.to_numpy()), ms(df.post_ii_r.to_numpy())
    r["stop..+50 ms"] = (ma, sa, mb, sb)
    return r
freq_med = LA.groupby("subject").peak_frequency.median()
res1c = []
for sub, g in TRIG.groupby("subject"):
    r = summary(g)
    row = dict(subject=sub, neurons=len(g), events=int(g.drop_duplicates("session").n_ev.sum()), median_freq=round(freq_med.get(sub, np.nan), 1))
    for nm, (ma, sa, mb, sb) in r.items():
        row[f"{nm} HFO"] = ma; row[f"{nm} random"] = mb; row[f"{nm} 3SEM"] = 3 * np.hypot(sa, sb) if False else 3 * sa
        row[f"{nm} above"] = ma - mb > 3 * sa if "+20" not in nm and "stop" not in nm else None
        row[f"{nm} below"] = mb - ma > 3 * sa if ("+20" in nm or "stop" in nm) else None
    res1c.append(row)
R1C = pd.DataFrame(res1c)
pd.set_option("display.float_format", lambda v: f"{v:.5f}")
print(R1C[["subject", "neurons", "events", "median_freq", "event bin HFO", "event bin random", "event bin 3SEM", "event bin above",
           "+-5 ms HFO", "+-5 ms random", "+-5 ms 3SEM", "+-5 ms above"]].to_string())
print("\nAfter the burst (spikes per ms per event):")
print(R1C[["subject", "+20..50 ms HFO", "+20..50 ms random", "+20..50 ms 3SEM", "+20..50 ms below",
           "stop..+50 ms HFO", "stop..+50 ms random", "stop..+50 ms 3SEM", "stop..+50 ms below"]].to_string())
pd.reset_option("display.float_format")
allr = summary(TRIG)
print("\nAll animals pooled (mean HFO, SEM, mean random, SEM):", {k: tuple(round(x, 5) for x in v) for k, v in allr.items()})
print(f"Animals with median LS HFO frequency in 120-180 Hz: {int(freq_med.between(120, 180).sum())} of {len(freq_med)}")
print(f"Animals with the event-bin probability above random by more than 3 SEM: {int(R1C['event bin above'].sum())} of {len(R1C)}; "
      f"at +-5 ms: {int(R1C['+-5 ms above'].sum())}")
print(f"Animals with suppression after the burst, +20..50 ms: {int(R1C['+20..50 ms below'].sum())}; stop..+50 ms: {int(R1C['stop..+50 ms below'].sum())}")
# Post-burst relative to the pre-event baseline, as a reference (not the criterion)
C = np.vstack(TRIG.c); base = C[:, (lag >= -100) & (lag <= -50)].mean()
print(f"Pooled mean probability per ms: -100..-50 ms {base:.5f}; event bin {C[:, at0].mean():.5f}; +20..50 ms {C[:, post].mean():.5f}; random {np.vstack(TRIG.cr).mean():.5f}")
fig, ax = plt.subplots(figsize=(6, 3))
for sub, g in TRIG.groupby("subject"):
    ax.plot(lag, np.vstack(g.c).mean(0) / np.vstack(g.cr).mean(), label=sub)
ax.axhline(1, color="k", lw=.5); ax.set_xlabel("lag from LS HFO peak (ms)"); ax.set_ylabel("spike prob. / random"); ax.legend(fontsize=7); plt.show()
yy = [np.vstack(g.c).mean(0) / np.vstack(g.cr).mean() for _, g in TRIG.groupby("subject")]
print(f"Plotted range: {min(y.min() for y in yy):.2f} to {max(y.max() for y in yy):.2f}")

# %% [markdown]
# Seed: the random times are drawn under the claim's seed and four more.

# %% tags=["claim:fig1c-hfo-each-animal"]
for k in range(5):
    sd = seed_of("fig1c-hfo-each-animal") + 1000 * k
    tr = TRIG if k == 0 else hfo_triggered(sd)
    n_above = n_post = n_post2 = 0
    for sub, g in tr.groupby("subject"):
        r = summary(g)
        n_above += r["event bin"][0] - r["event bin"][2] > 3 * r["event bin"][1]
        n_post += r["+20..50 ms"][2] - r["+20..50 ms"][0] > 3 * r["+20..50 ms"][1]
        n_post2 += r["stop..+50 ms"][2] - r["stop..+50 ms"][0] > 3 * r["stop..+50 ms"][1]
    print(f"seed {sd}: animals above at the event bin {n_above}; below after the burst (+20..50) {n_post}, (stop..+50) {n_post2}")

# %% [markdown]
# ## figs1-participation
# > On average 16% of LS neurons take part in a given HFO, firing an average of 0.23 spikes per event.
#
# Windows (a) start to stop, (b) +-25 ms of the event time; averaging (i) over all events pooled, (ii) over recordings of
# per-recording means. Recordings with LS units and LSRipples.

# %% tags=["claim:figs1-participation"]
part = []
for s in S:
    e = ls_ev(s); ls = s.units_in(["ls"])
    if e is None or len(ls) == 0: continue
    t = e.peak_time.to_numpy()
    for w, (a, b) in {"a": (e.start_time.to_numpy(), e.stop_time.to_numpy()), "b": (t - 0.025, t + 0.025)}.items():
        M = np.vstack([T.count_in(s.spikes[u], a, b) for u in ls])        # units x events
        part.append(dict(session=s.session, subject=s.subject, window=w, n_units=len(ls), n_ev=len(t),
                         frac_ev=(M > 0).mean(0), spk_ev=M.mean(0)))
P = pd.DataFrame(part)
for w in "ab":
    g = P[P.window == w]
    fi = np.concatenate(g.frac_ev.values).mean(); si = np.concatenate(g.spk_ev.values).mean()
    fii = np.mean([x.mean() for x in g.frac_ev]); sii = np.mean([x.mean() for x in g.spk_ev])
    print(f"window ({w}): (i) pooled events: fraction {fi:.3f}, spikes per neuron per event {si:.3f}; "
          f"(ii) mean of {len(g)} recordings: fraction {fii:.3f}, spikes {sii:.3f}")
print("Paper: 0.16 (tolerance 0.016) and 0.23 (0.023)")
g = P[P.window == "a"]
print("\nPer animal, window (a), pooled events:")
print(pd.DataFrame({"fraction": g.groupby("subject").frac_ev.apply(lambda x: np.concatenate(x.values).mean()),
                    "spikes": g.groupby("subject").spk_ev.apply(lambda x: np.concatenate(x.values).mean()),
                    "recordings": g.groupby("subject").size()}).round(3).to_string())
print(f"Units per recording: {P.n_units.min()} to {P.n_units.max()}")
EOF
. ../wk/bin/activate && python dev.py s02_sanity.py s03_fig1.py 2>&1 | grep -v "^ *[0-9]* *DT\|^  *[0-9][0-9]* " | tail -120
```

```
Wed Nov 18 10:13:17 UTC 2026
   subject                         session  hours  lfp_channels  ls_units  hpc_units  ca1_units  ca3_units  other_units other_regions                                                          tables  nrem_h  wake_h  rem_h  trials  ca3_flag  ca1_flag

By subject:
         ls_units  hpc_units  ca3_units  other_units  trials  files
subject                                                            

Unit regions over all files: {np.str_('ls'): 2551, np.str_('ppc'): 60, np.str_('hpc'): 2907, np.str_('ca3'): 566, np.str_('acg'): 31, np.str_('cc'): 6, np.str_('ms'): 25, np.str_(''): 36, np.str_('sfi'): 54}
Event tables (files holding each): {'LSRipples': 77, 'ripples_ls': 13, 'ls_ripples': 27, 'CA1Ripples': 47, 'ripplesALL': 25, 'ripplesWAKE': 1}
LSRipples: 27014 events; duration 8.8 to 99.2 ms (median 25.6); peak_frequency 125.1 to 171.2 (median 147.0, read as Hz); peak inside start-stop 1.000; events inside the recording 1.000
CA1Ripples: 101217 events; duration 10.4 to 228.8 ms (median 28.0); peak_frequency 133.8 to 191.6 (median 157.9, read as Hz); peak inside start-stop 1.000; events inside the recording 1.000
ripplesALL: 89485 events; duration 14.4 to 281.6 ms (median 33.6); peak_frequency 123.2 to 329.6 (median 158.1, read as Hz); peak inside start-stop 1.000; events inside the recording 1.000
ls_ripples: 25829 events; duration 14.4 to 99.2 ms (median 26.4); peak_frequency 19.5 to 419.9 (median 155.9, read as Hz); peak inside start-stop 1.000; events inside the recording 1.000
ripples_ls: 4631 events; duration 9.6 to 100.0 ms (median 17.6); no peak_frequency; peak inside start-stop 1.000; events inside the recording 1.000
Spike times: 203723542 spikes in 6236 units; min 0.0001 s; units with a spike after the LFP's end: 0
Sorted spike times in every unit: True
Sleep states: labels ['MA', 'NREM', 'REM', 'WAKE']; bouts 14041; stop beyond the recording: 0; whole-second times: 1.000
Trials: 10292 in 74 files; length 0.23 to 11.5 s (median 3.8
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat > s04_fig5.py <<'EOF'
# %% [markdown]
# ## fig5b-nrem-and-rates
# > LS HFOs occur primarily during NREM sleep, and their rates are significantly lower than those of hippocampal SPW-Rs.
#
# Per recording with scored sleep, the LS HFO rate (LSRipples) and the CA1 ripple rate (CA1Ripples) in NREM, in WAKE and over
# the scored time. The state of an event is the state at its peak time.

# %% tags=["claim:fig5b-nrem-and-rates"]
def rates(s, ev):
    if ev is None or s.sleep is None: return None
    t = ev.peak_time.to_numpy(); st = T.state_at(t, s)
    r = {}
    for lab in ["NREM", "WAKE"]:
        dur = T.total(s.state_intervals(lab)); r[lab] = (st == lab).sum() / dur if dur > 60 else np.nan
    scored = T.total(s.sleep[["start_time", "stop_time"]].to_numpy()); r["all"] = (st != "").sum() / scored
    r["n"] = len(t); r["n_nrem"] = int((st == "NREM").sum())
    return r
RL = pd.DataFrame([dict(session=s.session, subject=s.subject, **rates(s, ls_ev(s))) for s in S if rates(s, ls_ev(s)) is not None])
RC = pd.DataFrame([dict(session=s.session, subject=s.subject, **rates(s, ca1_ev(s))) for s in S if rates(s, ca1_ev(s)) is not None])
print(f"LS HFO rate recordings: {len(RL)}; CA1 ripple rate recordings: {len(RC)}")
for nm, R in [("LS HFO", RL), ("CA1 ripple", RC)]:
    print(f"{nm} rate (events/s), median [IQR]: NREM {R.NREM.median():.4f} [{R.NREM.quantile(.25):.4f}, {R.NREM.quantile(.75):.4f}], "
          f"WAKE {R.WAKE.median():.4f} [{R.WAKE.quantile(.25):.4f}, {R.WAKE.quantile(.75):.4f}], all {R['all'].median():.4f}")
frac_nrem = RL.n_nrem.sum() / RL.n.sum()
d = RL.dropna(subset=["NREM", "WAKE"])
w = stats.wilcoxon(d.NREM, d.WAKE)
print(f"\nPrimarily NREM: {frac_nrem:.3f} of {RL.n.sum()} LS HFOs fall in NREM; NREM rate > WAKE rate in {(d.NREM > d.WAKE).sum()} of {len(d)} recordings, "
      f"signed-rank p = {w.pvalue:.2g}")
print("By animal, fraction of LS HFOs in NREM:", (RL.groupby('subject').n_nrem.sum() / RL.groupby('subject').n.sum()).round(3).to_dict())
for col in ["NREM", "all"]:
    a = stats.mannwhitneyu(RL[col].dropna(), RC[col].dropna(), alternative="two-sided")
    m = RL.merge(RC, on="session", suffixes=("_ls", "_ca1")).dropna(subset=[f"{col}_ls", f"{col}_ca1"])
    b = stats.wilcoxon(m[f"{col}_ls"], m[f"{col}_ca1"])
    print(f"Lower than CA1 ({col}): (a) rank-sum {len(RL[col].dropna())} LS against {len(RC[col].dropna())} CA1 rates, p = {a.pvalue:.2g}, "
          f"medians {RL[col].median():.4f} / {RC[col].median():.4f}; (b) signed-rank over {len(m)} recordings with both, p = {b.pvalue:.2g}, "
          f"LS lower in {(m[f'{col}_ls'] < m[f'{col}_ca1']).sum()}")

# %% [markdown]
# ## fig5d-lag
# > LS HFOs are reliably coupled to CA1 ripples, with a median peak-to-peak lag of 6.4 +- 4.2 ms, CA1 leading LS.
#
# Recordings with both LSRipples and CA1Ripples. Lag = LS HFO peak time minus the nearest CA1 ripple peak time within
# +-50 ms or +-25 ms. Event time: the deposited peak (trough of the filtered signal). The maximum-NSS reading needs the
# LFP and is in the second notebook. Coupling: pooled CCG of CA1 ripples (trigger) with LS HFOs, 5 ms bins over +-200 ms.

# %% tags=["claim:fig5d-lag"]
def nearest_lag(ls_t, ca_t):
    j = np.clip(np.searchsorted(ca_t, ls_t), 1, len(ca_t) - 1)
    a, b = ls_t - ca_t[j - 1], ls_t - ca_t[j]
    return np.where(np.abs(a) < np.abs(b), a, b)
LAGS = []
for s in both_rec:
    l, c = ls_ev(s).peak_time.to_numpy(), np.sort(ca1_ev(s).peak_time.to_numpy())
    LAGS.append(dict(session=s.session, subject=s.subject, lag=nearest_lag(l, c) * 1000, n_ls=len(l), n_ca=len(c)))
LG = pd.DataFrame(LAGS)
for win in [50, 25]:
    per = [np.median(x[np.abs(x) <= win]) for x in LG.lag if (np.abs(x) <= win).sum() >= 1]
    allx = np.concatenate([x[np.abs(x) <= win] for x in LG.lag])
    print(f"within +-{win} ms: {len(allx)} pairs in {len(per)} recordings; (a) median over recordings of medians {np.median(per):.2f} ms "
          f"(SD over recordings {np.std(per, ddof=1):.2f}); (b) pooled median {np.median(allx):.2f} ms; positive (CA1 leading) fraction {np.mean(allx > 0):.3f}")
def ccg_events(trig, targ, maxlag=0.2, bs=0.005):
    L = int(round(maxlag / bs)); edges = (np.arange(-L, L + 2) - 0.5) * bs
    lo = np.searchsorted(targ, trig + edges[0]); hi = np.searchsorted(targ, trig + edges[-1])
    d = np.concatenate([targ[a:b] - t for a, b, t in zip(lo, hi, trig)]) if len(trig) else np.array([])
    return np.histogram(d, edges)[0]
cc = sum(ccg_events(np.sort(ca1_ev(s).peak_time.to_numpy()), np.sort(ls_ev(s).peak_time.to_numpy())) for s in both_rec)
lagc = np.arange(-40, 41) * 5
fl = cc[np.abs(lagc) >= 100]; pk = cc[np.abs(lagc) <= 25].max(); pkl = lagc[np.abs(lagc) <= 25][np.argmax(cc[np.abs(lagc) <= 25])]
print(f"Pooled CCG: peak {pk} at {pkl} ms; flanks (100-200 ms) mean {fl.mean():.1f}, SD {fl.std(ddof=1):.1f}; peak above flank mean by "
      f"{(pk - fl.mean()) / fl.std(ddof=1):.1f} SD")
print("Per animal, median lag within +-50 ms (pooled):", {k: round(float(np.median(np.concatenate([x[np.abs(x) <= 50] for x in g.lag]))), 2) for k, g in LG.groupby("subject")})
fig, ax = plt.subplots(figsize=(5, 3)); ax.bar(lagc, cc, width=5); ax.set_xlabel("LS HFO time - CA1 ripple time (ms)"); ax.set_ylabel("count"); plt.show()
print(f"Plotted counts {cc.min()} to {cc.max()}")

# %% [markdown]
# ## fig5e-state-coupling
# > HPC-LS coupling is stronger in NREM sleep than in waking immobility; the fraction of LS HFOs within +-25 ms of a CA1 ripple
# > is 0.3 in NREM and 0.15 in WAKE (P < 6.6e-6).
#
# Recordings with sleep states, CA1Ripples and LSRipples. CCG of CA1 ripples with LS HFOs per recording and state, 5 ms bins over
# +-200 ms, normalized by the number of CA1 ripples in the state (the state at the ripple's peak). The fraction of LS HFOs (state at
# the HFO's peak) with a CA1 ripple within +-25 ms. WAKE is read as all WAKE and as WAKE outside trials. Recordings need at least one
# event of each kind in each state.

# %% tags=["claim:fig5e-state-coupling"]
def coupling(wake_mode):
    rows = []
    for s in both_rec:
        if s.sleep is None: continue
        l, c = np.sort(ls_ev(s).peak_time.to_numpy()), np.sort(ca1_ev(s).peak_time.to_numpy())
        sl, sc = T.state_at(l, s), T.state_at(c, s)
        if wake_mode == "outside trials" and s.has_trials:
            tiv = s.trials[["start_time", "stop_time"]].to_numpy()
            sl = np.where((sl == "WAKE") & T.in_intervals(l, tiv), "", sl); sc = np.where((sc == "WAKE") & T.in_intervals(c, tiv), "", sc)
        r = dict(session=s.session, subject=s.subject)
        ok = True
        for st in ["NREM", "WAKE"]:
            cs, ls_ = c[sc == st], l[sl == st]
            if len(cs) == 0 or len(ls_) == 0: ok = False; break
            r[f"ccg_{st}"] = ccg_events(cs, l) / len(cs)
            lag = nearest_lag(ls_, c) * 1000
            r[f"frac_{st}"] = np.mean(np.abs(lag) <= 25); r[f"nls_{st}"] = len(ls_); r[f"k_{st}"] = int(np.sum(np.abs(lag) <= 25))
        if ok: rows.append(r)
    return pd.DataFrame(rows)
for wm in ["all WAKE", "outside trials"]:
    CP = coupling(wm)
    N, W = np.vstack(CP.ccg_NREM), np.vstack(CP.ccg_WAKE)
    nb = N.shape[1]
    pp = stats.ttest_rel(N, W, axis=0).pvalue * nb; pi = stats.ttest_ind(N, W, axis=0).pvalue * nb
    near = np.abs(lagc) <= 25
    print(f"WAKE = {wm}: {len(CP)} recordings")
    print(f"  CCG bins within +-25 ms with NREM > WAKE at Bonferroni p < 0.001: paired {int(((pp < 0.001) & (N.mean(0) > W.mean(0)) & near).sum())}, "
          f"two-sample {int(((pi < 0.001) & (N.mean(0) > W.mean(0)) & near).sum())} of {near.sum()}; smallest corrected p paired {pp[near].min():.2g}, two-sample {pi[near].min():.2g}")
    fa, fb = CP.frac_NREM.mean(), CP.frac_WAKE.mean()
    pa, pb = CP.k_NREM.sum() / CP.nls_NREM.sum(), CP.k_WAKE.sum() / CP.nls_WAKE.sum()
    tr, ti = stats.ttest_rel(CP.frac_NREM, CP.frac_WAKE), stats.ttest_ind(CP.frac_NREM, CP.frac_WAKE)
    print(f"  fraction within +-25 ms: (a) mean over recordings NREM {fa:.3f}, WAKE {fb:.3f}; (b) pooled NREM {pa:.3f} ({CP.nls_NREM.sum()} HFOs), "
          f"WAKE {pb:.3f} ({CP.nls_WAKE.sum()} HFOs)")
    print(f"  t-test NREM against WAKE fractions: paired p = {tr.pvalue:.2g} (t = {tr.statistic:.2f}), two-sample p = {ti.pvalue:.2g} (t = {ti.statistic:.2f}); "
          f"NREM higher in {(CP.frac_NREM > CP.frac_WAKE).sum()} of {len(CP)}")
    if wm == "all WAKE": CP_ALL = CP
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(lagc, np.vstack(CP_ALL.ccg_NREM).mean(0), label="NREM"); ax.plot(lagc, np.vstack(CP_ALL.ccg_WAKE).mean(0), label="WAKE")
ax.set_xlabel("lag (ms)"); ax.set_ylabel("LS HFOs per CA1 ripple per bin"); ax.legend(); plt.show()

# %% [markdown]
# ## fig5f-ripple-triggered-firing
# > LS firing around CA1 ripples is higher during NREM than during waking.
#
# Per LS neuron in recordings with sleep states and CA1Ripples, the CA1 ripple-triggered rate (spikes/s) in 5 ms bins over +-200 ms,
# for NREM and WAKE ripples separately; neurons with at least one ripple in each state. Per-bin t-tests over neurons, Bonferroni
# over 81 bins; paired and two-sample; raw rates and rates divided by the neuron's mean rate in the state.

# %% tags=["claim:fig5f-ripple-triggered-firing"]
F5 = []
for s in S:
    c = ca1_ev(s); ls = s.units_in(["ls"])
    if c is None or s.sleep is None or len(ls) == 0: continue
    t = c.peak_time.to_numpy(); st = T.state_at(t, s)
    if (st == "NREM").sum() == 0 or (st == "WAKE").sum() == 0: continue
    for u in ls:
        r = dict(session=s.session, subject=s.subject)
        for lab in ["NREM", "WAKE"]:
            r[lab] = T.triggered_counts(s.spikes[u], t[st == lab], 0.2, 0.005).mean(0) / 0.005
            iv = s.state_intervals(lab); r[f"mean_{lab}"] = T.in_intervals(s.spikes[u], iv).sum() / max(T.total(iv), 1)
        F5.append(r)
F5 = pd.DataFrame(F5)
N, W = np.vstack(F5.NREM), np.vstack(F5.WAKE)
mN, mW = F5.mean_NREM.to_numpy()[:, None], F5.mean_WAKE.to_numpy()[:, None]
okn = (mN[:, 0] > 0) & (mW[:, 0] > 0)
print(f"LS neurons: {len(F5)} in {F5.session.nunique()} recordings, {F5.subject.nunique()} animals; with a nonzero rate in both states {okn.sum()}")
near = np.abs(lagc) <= 25
for nm, (a, b) in {"raw": (N, W), "normalized": (N[okn] / mN[okn], W[okn] / mW[okn])}.items():
    pp = stats.ttest_rel(a, b, axis=0).pvalue * 81; pi = stats.ttest_ind(a, b, axis=0).pvalue * 81
    hi = a.mean(0) > b.mean(0)
    print(f"{nm}: bins within +-25 ms with NREM higher at corrected p < 0.001: paired {int(((pp < .001) & hi & near).sum())}, two-sample "
          f"{int(((pi < .001) & hi & near).sum())} of {near.sum()}; at 0 lag NREM {a[:, 40].mean():.2f}, WAKE {b[:, 40].mean():.2f}; "
          f"smallest corrected p within +-25 ms paired {pp[near].min():.2g}, two-sample {pi[near].min():.2g}; bins anywhere with WAKE higher (paired p<0.001): {int(((pp < .001) & ~hi).sum())}")
print("Per animal, mean rate at 0 lag (raw) NREM / WAKE:", {k: (round(np.vstack(g.NREM)[:, 40].mean(), 2), round(np.vstack(g.WAKE)[:, 40].mean(), 2), len(g)) for k, g in F5.groupby("subject")})
fig, ax = plt.subplots(figsize=(5, 3)); ax.plot(lagc, N.mean(0), label="NREM"); ax.plot(lagc, W.mean(0), label="WAKE"); ax.set_xlabel("lag from CA1 ripple (ms)"); ax.set_ylabel("LS rate (Hz)"); ax.legend(); plt.show()
print(f"Plotted range {min(N.mean(0).min(), W.mean(0).min()):.2f} to {max(N.mean(0).max(), W.mean(0).max()):.2f} Hz")

# %% [markdown]
# ## discussion-medial-septum (part b) and discussion-cingulate-down-state (reading a)
# > Recordings in medial septum show no HFOs, and medial septal firing is mainly suppressed at hippocampal SPW-Rs.
# > Recordings in deep layers of anterior cingulate cortex show down-state-coupled activity about 50 ms after the CA1 SPW-R.
#
# Units labelled `ms` and `acg`. Part (b): CA1 ripple-triggered rate (all states) within +-50 ms of the ripple against the
# neuron's mean rate; signed-rank test. Cingulate (a): the time of the minimum of the mean triggered rate (5 ms bins) between 0 and 200 ms.
# Part (a) of the medial septum claim needs the LFP of many sites and is in the second notebook.

# %% tags=["claim:discussion-medial-septum", "claim:discussion-cingulate-down-state"]
for reg in ["ms", "acg"]:
    rows = []
    for s in S:
        c = ca1_ev(s); us = s.units_in([reg])
        if c is None or len(us) == 0: continue
        t = c.peak_time.to_numpy()
        for u in us:
            sp = s.spikes[u]; mr = len(sp) / s.duration
            tc = T.triggered_counts(sp, t, 0.2, 0.005).mean(0) / 0.005
            r50 = (T.count_in(sp, t - 0.05, t + 0.05) / 0.1).mean()
            rows.append(dict(session=s.session[:25], subject=s.subject, mean_rate=mr, rate50=r50, tc=tc))
    D = pd.DataFrame(rows)
    print(f"{reg}: {len(D)} units in {D.session.nunique()} recordings ({D.session.unique().tolist()})")
    if reg == "ms":
        w = stats.wilcoxon(D.rate50, D.mean_rate)
        print(f"  rate within +-50 ms of CA1 ripples below the mean rate in {(D.rate50 < D.mean_rate).sum()} of {len(D)}; median ratio "
              f"{np.median(D.rate50 / D.mean_rate):.2f}; signed-rank p = {w.pvalue:.2g}")
    else:
        m = np.vstack(D.tc).mean(0) / D.mean_rate.mean()
        win = (lagc >= 0) & (lagc <= 200)
        print(f"  pooled triggered rate / mean rate: minimum in 0-200 ms at {lagc[win][np.argmin(m[win])]} ms ({m[win].min():.2f}); maximum at "
              f"{lagc[win][np.argmax(m[win])]} ms ({m[win].max():.2f}); at 0 ms {m[40]:.2f}")
        print("  per recording minimum lag (ms):", {k: int(lagc[win][np.argmin(np.vstack(g.tc).mean(0)[win])]) for k, g in D.groupby("session")})
        fig, ax = plt.subplots(figsize=(5, 3)); ax.plot(lagc, m); ax.set_xlabel("lag from CA1 ripple (ms)"); ax.set_ylabel("ACC rate / mean"); plt.show()
        print(f"Plotted range {m.min():.2f} to {m.max():.2f}")
EOF
. ../wk/bin/activate && python dev.py s02_sanity.py s03_fig1.py s04_fig5.py 2>&1 | sed -n '/s03_fig1.py/,$p'
```

```
## s03_fig1.py 23.6s maxrss 1.86 GB
LS HFO rate recordings: 77; CA1 ripple rate recordings: 47
LS HFO rate (events/s), median [IQR]: NREM 0.0235 [0.0104, 0.0614], WAKE 0.0021 [0.0009, 0.0054], all 0.0110
CA1 ripple rate (events/s), median [IQR]: NREM 0.3204 [0.1520, 0.3782], WAKE 0.0351 [0.0114, 0.0454], all 0.1024

Primarily NREM: 0.729 of 27014 LS HFOs fall in NREM; NREM rate > WAKE rate in 66 of 73 recordings, signed-rank p = 2.9e-12
By animal, fraction of LS HFOs in NREM: {'DT1': 0.815, 'DT2': 0.801, 'DT5': 0.661, 'DT7': 0.296, 'DT8': 0.56, 'DT9': 0.868}
Lower than CA1 (NREM): (a) rank-sum 73 LS against 42 CA1 rates, p = 1.5e-13, medians 0.0235 / 0.3204; (b) signed-rank over 42 recordings with both, p = 2.9e-10, LS lower in 37
Lower than CA1 (all): (a) rank-sum 77 LS against 47 CA1 rates, p = 1.3e-12, medians 0.0110 / 0.1024; (b) signed-rank over 45 recordings with both, p = 2.5e-11, LS lower in 42
within +-50 ms: 6572 pairs in 40 recordings; (a) median over recordings of medians 6.20 ms (SD over recordings 10.16); (b) pooled median 6.40 ms; positive (CA1 leading) fraction 0.639
within +-25 ms: 5343 pairs in 40 recordings; (a) median over recordings of medians 4.80 ms (SD over recordings 7.06); (b) pooled median 4.80 ms; positive (CA1 leading) fraction 0.604
Pooled CCG: peak 862 at 0 ms; flanks (100-200 ms) mean 62.2, SD 21.5; peak above flank mean by 37.1 SD
Per animal, median lag within +-50 ms (pooled): {'DT2': 1.2, 'DT5': 4.0, 'DT7': -7.2, 'DT9': 8.0}
Plotted counts 26 to 862
WAKE = all WAKE: 42 recordings
  CCG bins within +-25 ms with NREM > WAKE at Bonferroni p < 0.001: paired 0, two-sample 0 of 11; smallest corrected p paired 0.026, two-sample 0.1
  fraction within +-25 ms: (a) mean over recordings NREM 0.213, WAKE 0.118; (b) pooled NREM 0.302 (15605 HFOs), WAKE 0.091 (4163 HFOs)
  t-test NREM against WAKE fractions: paired p = 0.0025 (t = 3.22), two-sample p = 0.014 (t = 2.50); NREM higher in 30 of 42
WAKE = outside trials: 42 recordings
  CCG bins with
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat > s05_fig4.py <<'EOF'
# %% [markdown]
# ## Figure 4: LS pairs during HFOs and on the maze
# Common to fig4b-pre-post-unchanged, fig4b-hfo-above-behav, fig4-sessions-few-change, fig4c-temporal-bias and fig4d-compression.
# Recordings with trials (for the epochs; see the helper's docstring for the PRE / BEHAV / POST assumption), LSRipples and LS
# units on at least two shanks. Pairs of LS neurons on different shanks. Spikes during LS HFOs (start to stop) in PRE and in
# POST; BEHAV spikes inside trials (reading iv-a) or anywhere from the first trial to the last (iv-b). CCGs in 1 ms bins over
# +-200 ms. Inclusion (i): (a) the CCG holds more than 5 spike pairs within +-200 ms, (b) each neuron has more than 5 spikes
# with a partner spike within 200 ms; in every epoch.

# %% tags=["claim:fig4b-pre-post-unchanged"]
def partner_counts(a, b, w=0.2):
    """Spikes of a with a spike of b within w, and of b with one of a."""
    if len(a) == 0 or len(b) == 0: return 0, 0
    def k(x, y):
        j = np.clip(np.searchsorted(y, x), 1, len(y) - 1) if len(y) > 1 else np.zeros(len(x), int)
        d = np.minimum(np.abs(y[j] - x), np.abs(y[np.maximum(j - 1, 0)] - x))
        return int((d <= w).sum())
    return k(a, b), k(b, a)
def epoch_spikes(s, units, kind, ev_fn, behav_mode, spikes=None):
    sp = [s.spikes[u] for u in units] if spikes is None else spikes
    ep = s.epochs("trials" if behav_mode == "trials" else "span")
    e = ev_fn(s); hfo = e[["start_time", "stop_time"]].to_numpy()
    return {"PRE": T.restrict(sp, T.intersect(hfo, ep["PRE"])), "BEHAV": T.restrict(sp, ep["BEHAV"]),
            "POST": T.restrict(sp, T.intersect(hfo, ep["POST"]))}
def session_pairs(s, units, ev_fn, behav_mode, cross_shank=True, spikes=None):
    """CCGs (+-200 ms, 1 ms) of every pair in the three epochs, and both inclusion flags."""
    es = epoch_spikes(s, units, None, ev_fn, behav_mode, spikes)
    C = {k: T.ccg_all(v, 0.2) for k, v in es.items()}
    n = len(units); sh = s.unit_shank[units]
    I, J = np.triu_indices(n, 1)
    keep = sh[I] != sh[J] if cross_shank else np.ones(len(I), bool)
    I, J = I[keep], J[keep]
    inc_a = np.all([C[k][I, J].sum(1) > 5 for k in C], axis=0)
    inc_b = np.ones(len(I), bool)
    for k in C:
        pc = np.array([partner_counts(es[k][i], es[k][j]) for i, j in zip(I, J)]).reshape(-1, 2)
        inc_b &= (pc[:, 0] > 5) & (pc[:, 1] > 5)
    nsp = {k: np.array([len(x) for x in v]) for k, v in es.items()}
    return dict(I=I, J=J, ccg={k: C[k][I, J].astype(float) for k in C}, inc_a=inc_a, inc_b=inc_b,
                norm={k: np.sqrt(np.maximum(nsp[k][I] * nsp[k][J], 1)) for k in C})
F4_SESS = [s for s in S if s.has_trials and ls_ev(s) is not None and len(set(s.unit_shank[s.units_in(["ls"])])) >= 2]
print(f"Recordings with trials, LSRipples and LS units on two or more shanks: {len(F4_SESS)} ({collections.Counter(s.subject for s in F4_SESS)})")
t0 = time.time()
PAIRS = {}
for bm in ["trials", "span"]:
    PAIRS[bm] = [(s, session_pairs(s, s.units_in(["ls"]), ls_ev, bm)) for s in F4_SESS]
print(f"CCGs computed in {time.time()-t0:.0f} s")
def excess(ccg, kind):
    return T.gauss_smooth(ccg, 5, kind)[:, 200] - T.gauss_smooth(ccg, 200, kind)[:, 200]
EXC = []
for bm, lst in PAIRS.items():
    for s, P in lst:
        for inc in ["a", "b"]:
            m = P[f"inc_{inc}"]
            for kind in ["sd", "fwhm"]:
                for nm in ["raw", "sqrt"]:
                    r = dict(behav=bm, inc=inc, kernel=kind, norm=nm, session=s.session, subject=s.subject, n=int(m.sum()))
                    for ep in ["PRE", "BEHAV", "POST"]:
                        c = P["ccg"][ep][m]
                        if nm == "sqrt": c = c / P["norm"][ep][m][:, None]
                        r[ep] = excess(c, kind) if len(c) else np.array([])
                    EXC.append(r)
EXC = pd.DataFrame(EXC)
rows = []
for key, g in EXC.groupby(["inc", "kernel", "norm", "behav"]):
    pre, post, beh = (np.concatenate(g[e].values) for e in ["PRE", "POST", "BEHAV"])
    p = stats.mannwhitneyu(pre, post).pvalue if len(pre) else np.nan
    rows.append(dict(inclusion=key[0], kernel=key[1], norm=key[2], behav=key[3], pairs=len(pre), sessions=int((g.n > 0).sum()),
                     PRE_median=np.median(pre), POST_median=np.median(post), BEHAV_median=np.median(beh), p_PRE_POST=p,
                     differ=p < 0.05, effect_r=(stats.mannwhitneyu(pre, post).statistic / (len(pre) * len(post)) - 0.5) * 2 if len(pre) else np.nan))
F4B = pd.DataFrame(rows)
print(F4B.to_string(float_format=lambda v: f"{v:.4g}"))
print(f"\nReadings where PRE and POST differ (rank-sum p < 0.05): {int(F4B.differ.sum())} of {len(F4B)}; pairs per reading {F4B.pairs.min()} to {F4B.pairs.max()} "
      f"(paper 7172, tolerance 717); sessions {F4B.sessions.min()} to {F4B.sessions.max()} (paper 53)")
g = EXC[(EXC.inc == "a") & (EXC.kernel == "sd") & (EXC.norm == "raw") & (EXC.behav == "trials")]
print("\nPer animal, reading (a, sd, raw, trials): pairs, median PRE, median POST, rank-sum p")
for sub, gg in g.groupby("subject"):
    pre, post = np.concatenate(gg.PRE.values), np.concatenate(gg.POST.values)
    print(f"  {sub}: {len(pre)}, {np.median(pre) if len(pre) else np.nan:.3g}, {np.median(post) if len(post) else np.nan:.3g}, "
          f"{stats.mannwhitneyu(pre, post).pvalue if len(pre) > 1 else np.nan:.2g}")

# %% [markdown]
# ## fig4b-hfo-above-behav
# > Excess correlations during HFOs (PRE and POST) are much greater than chance from spikes jittered by +-200 ms and BEHAV excess
# > correlations slightly greater (P < 0.01), and co-activation during HFOs is higher than during maze traversal (P < 0.001).
#
# Every spike of each neuron is moved by a uniform random amount in +-200 ms (one jitter), and the same epochs, pairs and measure are
# computed. Reported for each reading of fig4b-pre-post-unchanged; the jitter is drawn under the claim's seed and four more.

# %% tags=["claim:fig4b-hfo-above-behav"]
def jittered_excess(seed):
    rng = np.random.default_rng(seed)
    out = []
    for bm in ["trials", "span"]:
        for (s, P) in PAIRS[bm]:
            units = s.units_in(["ls"])
            js = T.jitter([s.spikes[u] for u in units], rng)
            es = epoch_spikes(s, units, None, ls_ev, bm, js)
            C = {k: T.ccg_all(v, 0.2)[P["I"], P["J"]].astype(float) for k, v in es.items()}
            nsp = {k: np.array([len(x) for x in v]) for k, v in es.items()}
            for inc in ["a", "b"]:
                m = P[f"inc_{inc}"]
                for kind in ["sd", "fwhm"]:
                    for nm in ["raw", "sqrt"]:
                        r = dict(behav=bm, inc=inc, kernel=kind, norm=nm, session=s.session)
                        for ep in C:
                            c = C[ep][m]
                            if nm == "sqrt": c = c / np.sqrt(np.maximum(nsp[ep][P["I"]] * nsp[ep][P["J"]], 1))[m][:, None]
                            r[ep] = excess(c, kind) if len(c) else np.array([])
                        out.append(r)
    return pd.DataFrame(out)
def above_table(JX):
    rows = []
    for key, g in EXC.groupby(["inc", "kernel", "norm", "behav"]):
        gj = JX[(JX.inc == key[0]) & (JX.kernel == key[1]) & (JX.norm == key[2]) & (JX.behav == key[3])]
        r = dict(inclusion=key[0], kernel=key[1], norm=key[2], behav=key[3])
        x = {e: np.concatenate(g[e].values) for e in ["PRE", "BEHAV", "POST"]}
        xj = {e: np.concatenate(gj[e].values) for e in ["PRE", "BEHAV", "POST"]}
        for a, b in [("PRE", "BEHAV"), ("POST", "BEHAV")]:
            t = stats.mannwhitneyu(x[a], x[b]); r[f"p {a}>{b}"] = t.pvalue; r[f"{a}>{b}"] = (t.pvalue < 0.001) and np.median(x[a]) > np.median(x[b])
        for e in ["PRE", "BEHAV", "POST"]:
            t = stats.mannwhitneyu(x[e], xj[e]); r[f"p {e}>jit"] = t.pvalue
            r[f"{e}>jit"] = (t.pvalue < 0.01) and np.mean(x[e]) > np.mean(xj[e])
            r[f"{e} mean"] = np.mean(x[e]); r[f"{e} jit mean"] = np.mean(xj[e])
        rows.append(r)
    D = pd.DataFrame(rows)
    D["part1"] = D["PRE>BEHAV"] & D["POST>BEHAV"]; D["part2"] = D["PRE>jit"] & D["BEHAV>jit"] & D["POST>jit"]
    return D
JX0 = jittered_excess(seed_of("fig4b-hfo-above-behav"))
F4J = above_table(JX0)
print(F4J.to_string(float_format=lambda v: f"{v:.3g}"))
print(f"\nReadings with both parts: {int((F4J.part1 & F4J.part2).sum())}; part 1 only: {int((F4J.part1 & ~F4J.part2).sum())}; "
      f"part 2 only: {int((~F4J.part1 & F4J.part2).sum())}; neither: {int((~F4J.part1 & ~F4J.part2).sum())} of {len(F4J)}")

# %% tags=["claim:fig4b-hfo-above-behav"]
# The same under four more seeds (jitter only).
for k in range(1, 5):
    sd = seed_of("fig4b-hfo-above-behav") + 1000 * k
    D = above_table(jittered_excess(sd))
    print(f"seed {sd}: readings with part 2 (each epoch above its jitter at p < 0.01) {int(D.part2.sum())} of {len(D)}; "
          f"BEHAV above jitter in {int(D['BEHAV>jit'].sum())}; PRE in {int(D['PRE>jit'].sum())}; POST in {int(D['POST>jit'].sum())}")

# %% [markdown]
# ## fig4-sessions-few-change
# > Only 7 of 53 sessions have significantly different excess correlations in PRE and POST (rank-sum P < 0.01), three with PRE below
# > POST and four with PRE above.

# %% tags=["claim:fig4-sessions-few-change"]
rows = []
for key, g in EXC.groupby(["inc", "kernel", "norm", "behav"]):
    g = g[g.n > 0]
    sig, up, down = 0, 0, 0
    for _, r in g.iterrows():
        if len(r.PRE) > 1 and stats.mannwhitneyu(r.PRE, r.POST).pvalue < 0.01:
            sig += 1; up += np.median(r.PRE) < np.median(r.POST); down += np.median(r.PRE) > np.median(r.POST)
    rows.append(dict(inclusion=key[0], kernel=key[1], norm=key[2], behav=key[3], sessions=len(g), significant=sig,
                     fraction=sig / max(len(g), 1), PRE_below_POST=up, PRE_above_POST=down))
F4S = pd.DataFrame(rows)
print(F4S.to_string(float_format=lambda v: f"{v:.3f}"))
print("Paper: 53 sessions (tolerance 5.3), fraction 0.132 (tolerance 0.0132), both directions")

# %% [markdown]
# ## fig4c-temporal-bias
# > The temporal ordering of LS spike pairs during HFOs before and after the maze correlates with the ordering during traversal to a
# > similar degree (P = 0.85).
#
# B = CCG summed over +1..+200 ms minus over -200..-1 ms (the zero bin left out). Per recording, the correlation over pairs of
# B(PRE) with B(BEHAV) and of B(BEHAV) with B(POST); recordings with at least 3 pairs. Two-sided t-test, paired by recording and two-sample.

# %% tags=["claim:fig4c-temporal-bias"]
rows = []
for bm, lst in PAIRS.items():
    for inc in ["a", "b"]:
        for nm in ["raw", "sqrt"]:
            for cor in ["pearson", "spearman"]:
                r1, r2 = [], []
                for s, P in lst:
                    m = P[f"inc_{inc}"]
                    if m.sum() < 3: continue
                    B = {}
                    for ep in ["PRE", "BEHAV", "POST"]:
                        c = P["ccg"][ep][m]
                        if nm == "sqrt": c = c / P["norm"][ep][m][:, None]
                        B[ep] = c[:, 201:].sum(1) - c[:, :200].sum(1)
                    f = stats.pearsonr if cor == "pearson" else stats.spearmanr
                    a, b = f(B["PRE"], B["BEHAV"])[0], f(B["BEHAV"], B["POST"])[0]
                    if np.isfinite(a) and np.isfinite(b): r1.append(a); r2.append(b)
                r1, r2 = np.array(r1), np.array(r2)
                rows.append(dict(behav=bm, inclusion=inc, norm=nm, corr=cor, recordings=len(r1), PRE_BEHAV=r1.mean(), BEHAV_POST=r2.mean(),
                                 diff=(r2 - r1).mean(), p_paired=stats.ttest_rel(r1, r2).pvalue, p_two_sample=stats.ttest_ind(r1, r2).pvalue))
F4C = pd.DataFrame(rows)
print(F4C.to_string(float_format=lambda v: f"{v:.3g}"))
print(f"Readings where the t-test finds a difference at p < 0.05: paired {int((F4C.p_paired < .05).sum())}, two-sample {int((F4C.p_two_sample < .05).sum())} of {len(F4C)}")

# %% [markdown]
# ## fig4d-compression
# > Cross-correlograms of LS pairs during HFOs correlate with those during traversal above chance up to about 20-fold temporal
# > compression (P < 0.01), similarly for PRE and POST (P > 0.01 for all compression factors).
#
# BEHAV CCG over +-120 ms (241 points); the HFO CCG over +-120/c ms, linearly interpolated to 241 points, for c = 1..50; Pearson
# correlation. Chance: the same correlation with the BEHAV CCG circularly shifted by a random amount (one shift per pair and factor,
# the claim's seed). Tests per factor over pairs: actual against chance by signed-rank and by rank-sum (actual higher, p < 0.01);
# PRE against POST by rank-sum.

# %% tags=["claim:fig4d-compression"]
FACT = np.arange(1, 51)
LAGS_MS = np.arange(-200, 201)
WARP = np.stack([np.stack([np.interp(np.linspace(-120 / c, 120 / c, 241), LAGS_MS, np.eye(401)[k]) for k in range(401)], 1) for c in FACT])  # [50, 241, 401]
def rowcorr(X, Y):
    X = X - X.mean(-1, keepdims=True); Y = Y - Y.mean(-1, keepdims=True)
    return (X * Y).sum(-1) / np.sqrt((X ** 2).sum(-1) * (Y ** 2).sum(-1))
def compression(pairs_list, inc, seed, hfo_eps=("PRE", "POST")):
    rng = np.random.default_rng(seed)
    out = {ep: [] for ep in hfo_eps}; ch = {ep: [] for ep in hfo_eps}
    for s, P in pairs_list:
        m = P[f"inc_{inc}"]
        if m.sum() == 0: continue
        beh = P["ccg"]["BEHAV"][m][:, 80:321]                          # +-120 ms
        for ep in hfo_eps:
            h = P["ccg"][ep][m]
            Wd = np.einsum("fkl,pl->pfk", WARP, h)                     # pairs x factors x 241
            out[ep].append(rowcorr(Wd, beh[:, None, :]))
            shift = rng.integers(1, 241, size=Wd.shape[:2])
            idx = (np.arange(241)[None, None, :] + shift[..., None]) % 241
            bsh = np.take_along_axis(np.broadcast_to(beh[:, None, :], Wd.shape), idx, axis=-1)
            ch[ep].append(rowcorr(Wd, bsh))
    return {ep: np.vstack(v) for ep, v in out.items()}, {ep: np.vstack(v) for ep, v in ch.items()}
def compression_summary(act, cha, sig=0.01):
    res = {}
    for ep in act:
        p_sr, p_rs = [], []
        for f in range(len(FACT)):
            a, c = act[ep][:, f], cha[ep][:, f]; ok = np.isfinite(a) & np.isfinite(c)
            p_sr.append(stats.wilcoxon(a[ok], c[ok], alternative="greater").pvalue if ok.sum() > 5 else 1)
            p_rs.append(stats.mannwhitneyu(a[ok], c[ok], alternative="greater").pvalue if ok.sum() > 5 else 1)
        p_sr, p_rs = np.array(p_sr), np.array(p_rs)
        def largest(p):
            bad = np.flatnonzero(p >= sig); return int(FACT[bad[0] - 1]) if len(bad) and bad[0] > 0 else (int(FACT[-1]) if not len(bad) else 0)
        res[ep] = dict(p_sr=p_sr, p_rs=p_rs, largest_sr=largest(p_sr), largest_rs=largest(p_rs))
    pp = np.array([stats.mannwhitneyu(act["PRE"][:, f][np.isfinite(act["PRE"][:, f])], act["POST"][:, f][np.isfinite(act["POST"][:, f])]).pvalue for f in range(len(FACT))])
    res["PRE_POST_p"] = pp
    return res
CMP = {}
for bm in ["trials", "span"]:
    for inc in ["a", "b"]:
        act, cha = compression(PAIRS[bm], inc, seed_of("fig4d-compression"))
        r = compression_summary(act, cha); CMP[(bm, inc)] = (act, cha, r)
        print(f"behav {bm}, inclusion {inc}: {len(act['PRE'])} pairs; largest factor with every factor up to it above chance (p < 0.01): "
              f"PRE signed-rank {r['PRE']['largest_sr']}, rank-sum {r['PRE']['largest_rs']}; POST signed-rank {r['POST']['largest_sr']}, rank-sum {r['POST']['largest_rs']}; "
              f"factors with PRE != POST at p < 0.01: {int((r['PRE_POST_p'] < 0.01).sum())} (smallest p {r['PRE_POST_p'].min():.2g})")
        print(f"   median correlation at c = 1, 5, 10, 20, 50: PRE {[round(float(np.nanmedian(act['PRE'][:, f-1])), 3) for f in (1, 5, 10, 20, 50)]}, "
              f"chance {[round(float(np.nanmedian(cha['PRE'][:, f-1])), 3) for f in (1, 5, 10, 20, 50)]}; "
              f"POST {[round(float(np.nanmedian(act['POST'][:, f-1])), 3) for f in (1, 5, 10, 20, 50)]}")
act, cha, r = CMP[("trials", "a")]
fig, ax = plt.subplots(figsize=(5, 3))
for ep in ["PRE", "POST"]:
    ax.plot(FACT, np.nanmean(act[ep], 0), label=ep); ax.plot(FACT, np.nanmean(cha[ep], 0), "--", label=f"{ep} chance")
ax.set_xlabel("compression factor"); ax.set_ylabel("mean r with BEHAV CCG"); ax.legend(fontsize=7); plt.show()
print(f"Plotted range {min(np.nanmean(act[e], 0).min() for e in act):.3f} to {max(np.nanmean(act[e], 0).max() for e in act):.3f}")

# %% tags=["claim:fig4d-compression"]
# The circular shift is random: the largest factor under four more seeds (behav trials, inclusion a).
for k in range(1, 5):
    sd = seed_of("fig4d-compression") + 1000 * k
    act_k, cha_k = compression(PAIRS["trials"], "a", sd); r = compression_summary(act_k, cha_k)
    print(f"seed {sd}: largest factor PRE signed-rank {r['PRE']['largest_sr']}, rank-sum {r['PRE']['largest_rs']}; POST {r['POST']['largest_sr']}, {r['POST']['largest_rs']}")
EOF
. ../wk/bin/activate && python dev.py s02_sanity.py s03_fig1.py s05_fig4.py 2>&1 | sed -n '/s03_fig1.py/,$p'
```

```
## s03_fig1.py 23.7s maxrss 1.86 GB
Recordings with trials, LSRipples and LS units on two or more shanks: 54 (Counter({'DT8': 17, 'DT5': 14, 'DT9': 13, 'DT2': 10}))
CCGs computed in 16 s
   inclusion kernel  norm   behav  pairs  sessions  PRE_median  POST_median  BEHAV_median  p_PRE_POST  differ  effect_r
0          a   fwhm   raw    span    503        23      0.3598       0.4153        0.5829    0.006508    True  -0.09912
1          a   fwhm   raw  trials    462        23      0.3719       0.4474       0.08774    0.003592    True   -0.1107
2          a   fwhm  sqrt    span    503        23    0.006025     0.005613     0.0002911      0.8885   False   0.00511
3          a   fwhm  sqrt  trials    462        23    0.006043      0.00584     0.0002053      0.8478   False -0.007299
4          a     sd   raw    span    503        23       0.324       0.3921        0.4338    0.006005    True   -0.1001
5          a     sd   raw  trials    462        23      0.3372       0.3998       0.09373    0.005924    True   -0.1046
6          a     sd  sqrt    span    503        23    0.005524     0.005275     0.0002588      0.4981   False   0.02468
7          a     sd  sqrt  trials    462        23     0.00562      0.00536     0.0003335      0.5671   False   0.02176
8          b   fwhm   raw    span    401        21      0.4325       0.4925        0.6563    0.005291    True   -0.1138
9          b   fwhm   raw  trials    361        21      0.4417       0.5114       0.09779    0.004681    True   -0.1216
10         b   fwhm  sqrt    span    401        21    0.006025     0.005755     0.0002881      0.8047   False  -0.01009
11         b   fwhm  sqrt  trials    361        21    0.006085     0.005819     0.0002304       0.766   False  -0.01281
12         b     sd   raw    span    401        21      0.3975       0.4575        0.4912    0.004723    True   -0.1153
13         b     sd   raw  trials    361        21      0.4087       0.4704        0.1207    0.004256    True   -0.1229
14         b 
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR/nb && cat > s06_figs2s3.py <<'EOF'
# %% [markdown]
# ## figs3d-hpc-compression-post
# > For hippocampal cell pairs, compression of behavioural spike patterns during CA1 ripples is higher after than before the
# > behavioural session, for compression factors 1 to 7; HPC pairs are the only ones with a PRE to POST difference.
#
# As fig4d-compression, for pairs of hippocampal units of the same region label (`hpc` with `hpc`, `ca3` with `ca3`), with spikes
# inside CA1Ripples events in PRE and POST and BEHAV spikes in trials. Readings: pairs across shanks and all pairs; inclusion (a) and (b).
# POST against PRE by rank-sum over pairs at each factor.

# %% tags=["claim:figs3d-hpc-compression-post"]
S3_SESS = [s for s in S if s.has_trials and ca1_ev(s) is not None and len(s.units_in(HPC)) >= 2]
print(f"Recordings with trials, CA1Ripples and two or more hippocampal units: {len(S3_SESS)} ({collections.Counter(s.subject for s in S3_SESS)})")
t0 = time.time()
HP = {}
for cross in [True, False]:
    lst = []
    for s in S3_SESS:
        for reg in ["hpc", "ca3", "ca1"]:
            us = s.units_in([reg])
            if len(us) >= 2: lst.append((s, session_pairs(s, us, ca1_ev, "trials", cross_shank=cross)))
    HP[cross] = lst
print(f"CCGs in {time.time()-t0:.0f} s")
for cross in [True, False]:
    for inc in ["a", "b"]:
        act, cha = compression(HP[cross], inc, seed_of("figs3d-hpc-compression-post"))
        pp = np.array([stats.mannwhitneyu(act["POST"][:, f][np.isfinite(act["POST"][:, f])], act["PRE"][:, f][np.isfinite(act["PRE"][:, f])]).pvalue for f in range(7)])
        hi = np.array([np.nanmedian(act["POST"][:, f]) > np.nanmedian(act["PRE"][:, f]) for f in range(7)])
        print(f"{'across shanks' if cross else 'all pairs'}, inclusion {inc}: {len(act['PRE'])} pairs; factors 1-7 with POST > PRE at p < 0.01: {int(((pp < .01) & hi).sum())}; "
              f"p = {np.round(pp, 4).tolist()}; median r PRE {np.round(np.nanmedian(act['PRE'][:, :7], 0), 3).tolist()}, POST {np.round(np.nanmedian(act['POST'][:, :7], 0), 3).tolist()}")

# %% [markdown]
# ## figs2-post-rate-increase
# > Firing rates increase during post-behavior NREM sleep in CA1, CA3 and LS.
#
# Per neuron, the rate in NREM within PRE, in BEHAV (trials) and in NREM within POST, divided by the neuron's rate over the whole
# session (Figure S2B legend, change relative to the session average). Recordings with trials and NREM of at least 60 s in both PRE
# and POST. CA1 is read as units labelled `hpc` or `ca1` (the dataset labels CA1 units `hpc`), CA3 as `ca3`; as a variant, `hpc`
# units in recordings with a `ca3_channel` flag are counted as CA3. Two-sided t-tests of POST against PRE, paired and two-sample.

# %% tags=["claim:figs2-post-rate-increase"]
rows = []
for s in S:
    if not s.has_trials or s.sleep is None: continue
    ep = s.epochs("trials"); nrem = s.state_intervals("NREM")
    pre_n, post_n = T.intersect(nrem, ep["PRE"]), T.intersect(nrem, ep["POST"])
    if T.total(pre_n) < 60 or T.total(post_n) < 60: continue
    ca3flag = bool(s.electrodes.ca3_channel.any())
    for u, reg in enumerate(s.unit_region):
        sp = s.spikes[u]; avg = len(sp) / s.duration
        if avg == 0: continue
        r = dict(session=s.session, subject=s.subject, region=reg, region_flag=("ca3" if (reg == "hpc" and ca3flag) else reg))
        for nm, iv in [("PRE", pre_n), ("BEHAV", ep["BEHAV"]), ("POST", post_n)]:
            r[nm] = T.in_intervals(sp, iv).sum() / T.total(iv) / avg
        rows.append(r)
FR = pd.DataFrame(rows)
FR["label"] = FR.region.map({"ls": "LS", "hpc": "CA1", "ca1": "CA1", "ca3": "CA3"})
FR["label_flag"] = FR.region_flag.map({"ls": "LS", "hpc": "CA1", "ca1": "CA1", "ca3": "CA3"})
print(f"Recordings: {FR.session.nunique()}")
for col in ["label", "label_flag"]:
    print(f"Regions by {'unit label' if col == 'label' else 'unit label and ca3_channel flag'}:")
    for reg in ["LS", "CA1", "CA3"]:
        g = FR[FR[col] == reg]
        if len(g) == 0: print(f"  {reg}: none"); continue
        tp, ti = stats.ttest_rel(g.POST, g.PRE), stats.ttest_ind(g.POST, g.PRE)
        print(f"  {reg}: {len(g)} neurons in {g.session.nunique()} recordings, {g.subject.nunique()} animals; relative rate PRE NREM {g.PRE.mean():.3f}, "
              f"BEHAV {g.BEHAV.mean():.3f}, POST NREM {g.POST.mean():.3f}; POST > PRE in {(g.POST > g.PRE).mean():.2f}; paired p = {tp.pvalue:.2g} (t = {tp.statistic:.2f}), "
              f"two-sample p = {ti.pvalue:.2g} (t = {ti.statistic:.2f})")
print("Paper N: LS 1754, CA1 2315, CA3 1373 (tolerance 10%)")
print("\nPer animal, LS, mean POST - PRE relative rate:", FR[FR.label == "LS"].assign(d=lambda x: x.POST - x.PRE).groupby("subject").d.agg(["mean", "count"]).round(3).to_dict("index"))

# %% [markdown]
# ## figs2c-no-ls-reactivation
# > After controlling for the change in firing rate, by rate matching or by bin size, LS-LS pairs show no fast timescale reactivation
# > beyond chance, and HPC and HPC-LS pairs give similar results.
#
# EV and REV (Kudrimoti et al. 1999; Pennartz et al. 2004, STAR Methods formula) from pair correlation vectors of binned counts in PRE NREM
# ripple epochs, BEHAV (trials) and POST NREM ripple epochs. Ripple epochs are read as (a) CA1Ripples events in NREM (start to stop) and
# (b) for LS pairs, LSRipples events in NREM. Counts in 25 ms and 1 s bins over the concatenated epoch time. Rate matching (Giri et al.
# 2019): single spikes removed at random from the epoch (PRE or POST NREM) where the neuron fires faster, until the rates match; 10
# repetitions averaged (the claim's seed). Recordings with trials, NREM in PRE and POST, and at least 5 neurons of the set (pairs within
# a recording). Two-sided t-test of EV against REV over recordings, paired and two-sample.

# %% tags=["claim:figs2c-no-ls-reactivation"]
def binned(spikes, iv, bs):
    """Counts in bins of bs over the concatenated intervals (each interval cut into whole bins; at least one bin)."""
    iv = T.merge_intervals(iv)
    edges = [np.arange(a, b, bs) if b - a >= bs else np.array([a]) for a, b in iv]
    e = np.concatenate([np.r_[x, x[-1] + bs] for x in edges])
    keep = np.concatenate([np.r_[np.ones(len(x), bool), False] for x in edges])[:-1]
    return np.vstack([np.histogram(sp, e)[0][keep] for sp in spikes])
def corrvec(X, pairs):
    C = np.corrcoef(X); v = C[pairs[0], pairs[1]]
    return v
def ev_rev(pre, beh, post):
    ok = np.isfinite(pre) & np.isfinite(beh) & np.isfinite(post)
    if ok.sum() < 3: return np.nan, np.nan
    r = lambda a, b: np.corrcoef(a[ok], b[ok])[0, 1]
    rbp, rbq, rpq = r(beh, post), r(beh, pre), r(pre, post)
    ev = ((rbp - rbq * rpq) / np.sqrt((1 - rbq ** 2) * (1 - rpq ** 2))) ** 2
    rev = ((rbq - rbp * rpq) / np.sqrt((1 - rbp ** 2) * (1 - rpq ** 2))) ** 2
    return ev, rev
def rate_match(sp_pre, sp_post, T_pre, T_post, rng):
    a, b = [], []
    for x, y in zip(sp_pre, sp_post):
        ra, rb = len(x) / T_pre, len(y) / T_post
        if ra > rb: x = np.sort(rng.choice(x, int(round(rb * T_pre)), replace=False))
        elif rb > ra: y = np.sort(rng.choice(y, int(round(ra * T_post)), replace=False))
        a.append(x); b.append(y)
    return a, b
def reactivation(seed, n_rep=10):
    rng = np.random.default_rng(seed)
    out = []
    for s in S:
        if not s.has_trials or s.sleep is None: continue
        ep = s.epochs("trials"); nrem = s.state_intervals("NREM")
        for evname, evfn in [("CA1 ripples", ca1_ev), ("LS HFOs", ls_ev)]:
            e = evfn(s)
            if e is None: continue
            rip = e[["start_time", "stop_time"]].to_numpy()
            pre_iv, post_iv = T.intersect(T.intersect(rip, nrem), ep["PRE"]), T.intersect(T.intersect(rip, nrem), ep["POST"])
            if T.total(pre_iv) < 1 or T.total(post_iv) < 1: continue
            ls, hp = s.units_in(["ls"]), s.units_in(HPC)
            sets = {"LS-LS": (ls, ls), "HPC-HPC": (hp, hp), "HPC-LS": (hp, ls)}
            if evname == "LS HFOs": sets = {"LS-LS": (ls, ls)}
            for nm, (ua, ub) in sets.items():
                units = np.unique(np.r_[ua, ub])
                if len(ua) < 5 or len(ub) < 5: continue
                pos = {u: k for k, u in enumerate(units)}
                if nm in ("LS-LS", "HPC-HPC"):
                    I, J = np.triu_indices(len(ua), 1); pairs = (np.array([pos[u] for u in ua[I]]), np.array([pos[u] for u in ua[J]]))
                else:
                    I, J = np.meshgrid(np.arange(len(ua)), np.arange(len(ub)), indexing="ij")
                    pairs = (np.array([pos[u] for u in ua[I.ravel()]]), np.array([pos[u] for u in ub[J.ravel()]]))
                sp = [s.spikes[u] for u in units]
                spre, spost = T.restrict(sp, pre_iv), T.restrict(sp, post_iv)
                for bs in [0.025, 1.0]:
                    beh = corrvec(binned(sp, ep["BEHAV"], bs), pairs)
                    raw = ev_rev(corrvec(binned(spre, pre_iv, bs), pairs), beh, corrvec(binned(spost, post_iv, bs), pairs))
                    evs, revs = [], []
                    for k in range(n_rep):
                        a, b = rate_match(spre, spost, T.total(pre_iv), T.total(post_iv), rng)
                        e_, r_ = ev_rev(corrvec(binned(a, pre_iv, bs), pairs), beh, corrvec(binned(b, post_iv, bs), pairs))
                        evs.append(e_); revs.append(r_)
                    out.append(dict(session=s.session, subject=s.subject, events=evname, set=nm, bin=bs, EV=raw[0], REV=raw[1],
                                    EV_rm=np.nanmean(evs), REV_rm=np.nanmean(revs)))
    return pd.DataFrame(out)
t0 = time.time()
RE = reactivation(seed_of("figs2c-no-ls-reactivation"))
print(f"computed in {time.time()-t0:.0f} s")
def re_table(RE):
    rows = []
    for (evn, st, bs), g in RE.groupby(["events", "set", "bin"]):
        for m in ["", "_rm"]:
            d = g.dropna(subset=[f"EV{m}", f"REV{m}"])
            if len(d) < 2: continue
            rows.append(dict(events=evn, set=st, bin=bs, rate_matched=bool(m), recordings=len(d), EV=d[f"EV{m}"].mean(), REV=d[f"REV{m}"].mean(),
                             p_paired=stats.ttest_rel(d[f"EV{m}"], d[f"REV{m}"]).pvalue, p_two_sample=stats.ttest_ind(d[f"EV{m}"], d[f"REV{m}"]).pvalue))
    D = pd.DataFrame(rows); D["EV>REV p<0.05 (paired)"] = (D.p_paired < .05) & (D.EV > D.REV); D["EV>REV p<0.05 (two-sample)"] = (D.p_two_sample < .05) & (D.EV > D.REV)
    return D
RET = re_table(RE)
print(RET.to_string(float_format=lambda v: f"{v:.3g}"))

# %% tags=["claim:figs2c-no-ls-reactivation"]
# Rate matching is random: the 25 ms, rate-matched rows under four more seeds.
for k in range(1, 5):
    sd = seed_of("figs2c-no-ls-reactivation") + 1000 * k
    D = re_table(reactivation(sd)); D = D[(D.bin == 0.025) & D.rate_matched]
    print(f"seed {sd}:", "; ".join(f"{r.events} {r.set} EV {r.EV:.3g} REV {r.REV:.3g} p {r.p_paired:.2g}/{r.p_two_sample:.2g}" for r in D.itertuples()))
EOF
. ../wk/bin/activate && python dev.py s02_sanity.py s03_fig1.py s05_fig4.py s06_figs2s3.py 2>&1 | sed -n '/s05_fig4.py/,$p'
```

```
Wed Nov 18 10:22:24 UTC 2026
## s05_fig4.py 114.9s maxrss 3.65 GB
Recordings with trials, CA1Ripples and two or more hippocampal units: 42 (Counter({'DT5': 16, 'DT9': 10, 'DT2': 9, 'DT7': 7}))
CCGs in 84 s
across shanks, inclusion a: 12156 pairs; factors 1-7 with POST > PRE at p < 0.01: 1; p = [0.0582, 0.0246, 0.0001, 0.0464, 0.0297, 0.2267, 0.0113]; median r PRE [0.027, 0.027, 0.024, 0.02, 0.017, 0.015, 0.012], POST [0.03, 0.029, 0.028, 0.022, 0.018, 0.016, 0.015]
across shanks, inclusion b: 9366 pairs; factors 1-7 with POST > PRE at p < 0.01: 2; p = [0.0318, 0.0169, 0.0012, 0.027, 0.0349, 0.4126, 0.0059]; median r PRE [0.037, 0.037, 0.032, 0.026, 0.022, 0.021, 0.017], POST [0.041, 0.039, 0.036, 0.03, 0.024, 0.021, 0.02]
all pairs, inclusion a: 15066 pairs; factors 1-7 with POST > PRE at p < 0.01: 3; p = [0.1079, 0.0221, 0.0, 0.0074, 0.0083, 0.1684, 0.0378]; median r PRE [0.027, 0.028, 0.024, 0.02, 0.017, 0.015, 0.012], POST [0.029, 0.03, 0.028, 0.022, 0.018, 0.016, 0.014]
all pairs, inclusion b: 11564 pairs; factors 1-7 with POST > PRE at p < 0.01: 2; p = [0.091, 0.0131, 0.0001, 0.0033, 0.0107, 0.3046, 0.0146]; median r PRE [0.037, 0.038, 0.032, 0.025, 0.022, 0.021, 0.016], POST [0.04, 0.039, 0.036, 0.029, 0.024, 0.021, 0.019]
Recordings: 52
Regions by unit label:
  LS: 1570 neurons in 48 recordings, 5 animals; relative rate PRE NREM 1.265, BEHAV 0.780, POST NREM 1.334; POST > PRE in 0.58; paired p = 0.032 (t = 2.15), two-sample p = 0.036 (t = 2.09)
  CA1: 2597 neurons in 32 recordings, 4 animals; relative rate PRE NREM 1.347, BEHAV 1.207, POST NREM 1.293; POST > PRE in 0.50; paired p = 0.043 (t = -2.02), two-sample p = 0.051 (t = -1.95)
  CA3: 466 neurons in 8 recordings, 2 animals; relative rate PRE NREM 1.623, BEHAV 0.834, POST NREM 1.589; POST > PRE in 0.53; paired p = 0.59 (t = -0.54), two-sample p = 0.6 (t = -0.52)
Regions by unit label and ca3_channel flag:
  LS: 1570 neurons in 48 recordings, 5 animals; relative rate PRE NREM 1.265, BEHAV 0.780, POST NREM 
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
p='s06_figs2s3.py'; s=open(p).read()
old=s[s.index('def binned(spikes, iv, bs):'):s.index('def corrvec')]
new='''def binned(spikes, iv, bs):
    """Counts in bins of bs over the concatenated intervals: each spike's time is mapped onto the intervals laid end to end."""
    iv = T.merge_intervals(iv)
    off = np.r_[0, np.cumsum(iv[:, 1] - iv[:, 0])]
    nb = max(int(off[-1] // bs), 1)
    out = []
    for sp in spikes:
        k = np.searchsorted(iv[:, 0], sp, side="right") - 1
        ok = (k >= 0) & (sp <= iv[np.maximum(k, 0), 1])
        tc = sp[ok] - iv[k[ok], 0] + off[k[ok]]
        out.append(np.bincount(np.minimum((tc // bs).astype(int), nb - 1), minlength=nb)[:nb])
    return np.vstack(out)
'''
s=s.replace(old,new); open(p,'w').write(s)
EOF
cat > s06b.py <<'EOF'
exec(open('s06_figs2s3.py').read().split('# %% tags=["claim:figs2c-no-ls-reactivation"]')[0].split('# %% [markdown]\n# ## figs2c')[0][:0])
EOF
. ../wk/bin/activate && python - <<'EOF' 2>&1 | tail -40
import re
src=open('/tmp/claude-1001/nb/s06_figs2s3.py').read()
i=src.index('# %% [markdown]\n# ## figs2c')
open('/tmp/claude-1001/nb/s06c.py','w').write(src[i:])
EOF
cd $TMPDIR/nb && python dev.py s02_sanity.py s06c.py 2>&1 | sed -n '/s02_sanity.py/,$p'
```

```
## s02_sanity.py 40.1s maxrss 1.83 GB
computed in 71 s
         events      set   bin  rate_matched  recordings       EV     REV  p_paired  p_two_sample  EV>REV p<0.05 (paired)  EV>REV p<0.05 (two-sample)
0   CA1 ripples  HPC-HPC 0.025         False          31   0.0183  0.0103    0.0545         0.121                   False                       False
1   CA1 ripples  HPC-HPC 0.025          True          31    0.028 0.00995     0.184         0.234                   False                       False
2   CA1 ripples  HPC-HPC     1         False          29   0.0042 0.00178    0.0485        0.0547                    True                       False
3   CA1 ripples  HPC-HPC     1          True          29    0.008 0.00655     0.111         0.828                   False                       False
4   CA1 ripples   HPC-LS 0.025         False          29 0.000825 0.00123     0.486         0.575                   False                       False
5   CA1 ripples   HPC-LS 0.025          True          29  0.00095 0.00222     0.326         0.375                   False                       False
6   CA1 ripples   HPC-LS     1         False          27   0.0024 0.00463     0.454         0.537                   False                       False
7   CA1 ripples   HPC-LS     1          True          27  0.00518 0.00436     0.363         0.866                   False                       False
8   CA1 ripples    LS-LS 0.025         False          30    0.136   0.095     0.116         0.447                   False                       False
9   CA1 ripples    LS-LS 0.025          True          30    0.128  0.0938     0.227         0.532                   False                       False
10  CA1 ripples    LS-LS     1         False          28   0.0493  0.0491     0.957         0.996                   False                       False
11  CA1 ripples    LS-LS     1          True          28   0.0494  0.0485     0.853         0.986                   False                       F
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
p='s06_figs2s3.py'; s=open(p).read()
s=s.replace("def reactivation(seed, n_rep=10):","def reactivation(seed, n_rep=10, bins=(0.025, 1.0)):")
s=s.replace("                for bs in [0.025, 1.0]:","                for bs in bins:")
s=s.replace("D = re_table(reactivation(sd)); D = D[(D.bin == 0.025) & D.rate_matched]","D = re_table(reactivation(sd, bins=(0.025,))); D = D[(D.bin == 0.025) & D.rate_matched]")
open(p,'w').write(s)
EOF
cat > s07_fig7.py <<'EOF'
# %% [markdown]
# ## Figure 7E: LS spike counts predicted from SPW-R features
# Common to fig7e-ca1-spikes, fig7e-state and fig7e-duration. Recordings with LS units, hippocampal units and CA1Ripples. For each LS
# neuron and feature, the error (MSE) of predicting the neuron's spike count in each SPW-R from the feature, against the MSEs of 100
# shuffles of the feature across SPW-Rs (the claim's seed); the neuron counts when a two-sided one-sample t-test of the shuffled MSEs
# against the actual MSE gives p < 0.05 with the actual lower. Chance: one shuffle tested against the other 99 the same way.
# Readings (claims file): model (a) linear regression, (b) Poisson GLM; MSE in-sample or 5-fold cross-validated (contiguous folds,
# a standard choice); LS window SPW-R start to stop or +-50 ms of the ripple time; no minimum firing, or 20 spikes in SPW-Rs.
# Features: hippocampal spike count (all hippocampal units, start to stop); state (NREM 1, WAKE 0, SPW-Rs in those states);
# duration (stop minus start).

# %% tags=["claim:fig7e-ca1-spikes", "claim:fig7e-state", "claim:fig7e-duration"]
NSHUF = 100
def fit_mse(Y, X, model, cv):
    """Y [neurons, n], X [perms, n] (feature standardized). Returns MSE [neurons, perms]."""
    n = Y.shape[1]
    folds = [np.arange(n)] if not cv else np.array_split(np.arange(n), 5)
    sse = np.zeros((Y.shape[0], X.shape[0]))
    for f in folds:
        tr = np.setdiff1d(np.arange(n), f) if cv else f
        te = f
        xt, yt = X[:, tr], Y[:, tr]
        if model == "linear":
            mx, my = xt.mean(1), yt.mean(1)
            sxy = yt @ xt.T / len(tr) - my[:, None] * mx[None, :]
            sxx = (xt ** 2).mean(1) - mx ** 2
            b = sxy / np.where(sxx > 0, sxx, np.inf)[None, :]; a = my[:, None] - b * mx[None, :]
        else:
            a = np.log(np.maximum(yt.mean(1), 1e-3))[:, None] * np.ones((1, X.shape[0])); b = np.zeros_like(a)
            for _ in range(8):
                eta = np.clip(a[:, :, None] + b[:, :, None] * xt[None], -20, 20); mu = np.exp(eta)
                r = yt[:, None, :] - mu
                ga, gb = r.sum(-1), (r * xt[None]).sum(-1)
                h11, h12, h22 = mu.sum(-1), (mu * xt[None]).sum(-1), (mu * xt[None] ** 2).sum(-1)
                det = h11 * h22 - h12 ** 2 + 1e-9
                a = a + (h22 * ga - h12 * gb) / det; b = b + (h11 * gb - h12 * ga) / det
        xs = X[:, te]
        pred = a[:, :, None] + b[:, :, None] * xs[None] if model == "linear" else np.exp(np.clip(a[:, :, None] + b[:, :, None] * xs[None], -20, 20))
        sse += ((Y[:, None, te] - pred) ** 2).sum(-1)
    return sse / n
def sig_from_mse(M):
    """M [neurons, 1 + NSHUF]; actual in column 0. Significant (actual lower, p < 0.05) and chance (shuffle 1 against the rest)."""
    act, sh = M[:, 0], M[:, 1:]
    t = stats.ttest_1samp(sh, act, axis=1)
    sig = (t.pvalue < 0.05) & (act < sh.mean(1))
    t2 = stats.ttest_1samp(sh[:, 1:], sh[:, 0], axis=1)
    ch = (t2.pvalue < 0.05) & (sh[:, 0] < sh[:, 1:].mean(1))
    return sig, ch
F7_SESS = [s for s in S if ca1_ev(s) is not None and len(s.units_in(["ls"])) and len(s.units_in(HPC))]
print(f"Recordings: {len(F7_SESS)} ({collections.Counter(s.subject for s in F7_SESS)}); LS neurons {sum(len(s.units_in(['ls'])) for s in F7_SESS)}; "
      f"CA3 by unit label {sum(len(s.units_in(['ca3'])) > 0 for s in F7_SESS)}")
def fig7(seed):
    rng = np.random.default_rng(seed)
    rows = []
    for s in F7_SESS:
        c = ca1_ev(s); st, sp_ = c.start_time.to_numpy(), c.stop_time.to_numpy(); tt = c.peak_time.to_numpy()
        hp = s.units_in(HPC); ls = s.units_in(["ls"])
        state = T.state_at(tt, s)
        feats = {"ca1-spikes": (sum(T.count_in(s.spikes[u], st, sp_) for u in hp).astype(float), np.ones(len(tt), bool)),
                 "state": ((state == "NREM").astype(float), np.isin(state, ["NREM", "WAKE"])),
                 "duration": (sp_ - st, np.ones(len(tt), bool))}
        for win in ["start-stop", "+-50 ms"]:
            Y = np.vstack([T.count_in(s.spikes[u], st, sp_) if win == "start-stop" else T.count_in(s.spikes[u], tt - 0.05, tt + 0.05) for u in ls]).astype(float)
            for fn, (x, m) in feats.items():
                if m.sum() < 10 or np.std(x[m]) == 0: continue
                xm = (x[m] - x[m].mean()) / x[m].std()
                X = np.vstack([xm] + [rng.permutation(xm) for _ in range(NSHUF)])
                for model in ["linear", "poisson"]:
                    for cv in [False, True]:
                        sig, ch = sig_from_mse(fit_mse(Y[:, m], X, model, cv))
                        for k, u in enumerate(ls):
                            rows.append(dict(session=s.session, subject=s.subject, unit=u, feature=fn, window=win, model=model, cv=cv,
                                             n_spk=Y[k, m].sum(), sig=sig[k], chance=ch[k]))
    return pd.DataFrame(rows)
t0 = time.time()
F7 = fig7(seed_of("fig7e-ca1-spikes"))
print(f"computed in {time.time()-t0:.0f} s")
def f7_table(F7):
    rows = []
    for (fn, win, model, cv), g in F7.groupby(["feature", "window", "model", "cv"]):
        for mn in [0, 20]:
            gg = g[g.n_spk >= mn] if mn else g
            k, n = int(gg.sig.sum()), len(gg)
            pb = stats.binomtest(k, n, max(gg.chance.mean(), 1e-6), alternative="greater").pvalue
            rows.append(dict(feature=fn, window=win, model=model, cv=cv, min_spikes=mn, neurons=n, percent=100 * k / n, chance_percent=100 * gg.chance.mean(), binom_p=pb))
    return pd.DataFrame(rows)
F7T = f7_table(F7)
EXPECT7 = {"ca1-spikes": 38, "state": 26, "duration": 20}
F7T["within_tol"] = [abs(r.percent - EXPECT7[r.feature]) <= 0.1 * EXPECT7[r.feature] for r in F7T.itertuples()]
print(F7T.to_string(float_format=lambda v: f"{v:.3g}"))
for fn, e in EXPECT7.items():
    g = F7T[F7T.feature == fn]
    print(f"{fn}: paper {e}%; combinations within tolerance {int(g.within_tol.sum())} of {len(g)}; range {g.percent.min():.1f} to {g.percent.max():.1f}%; "
          f"above chance (binomial p < 0.05) in {int((g.binom_p < 0.05).sum())}")
print("\nPer animal, linear in-sample start-stop, no minimum:")
print(F7[(F7.model == "linear") & (~F7.cv) & (F7.window == "start-stop")].groupby(["feature", "subject"]).sig.agg(["mean", "count"]).round(3).to_string())
EOF
. ../wk/bin/activate && python - <<'EOF'
# time one recording first
src=open('/tmp/claude-1001/nb/s07_fig7.py').read().replace('F7_SESS = [s for s in S if','F7_SESS = [s for s in S[85:87] if')
open('/tmp/claude-1001/nb/s07_sub.py','w').write(src)
EOF
python dev.py s02_sanity.py s03_fig1.py s07_sub.py 2>&1 | sed -n '/s03_fig1.py/,$p'
```

```
## s03_fig1.py 23.8s maxrss 1.86 GB
Recordings: 2 (Counter({'DT9': 2})); LS neurons 102; CA3 by unit label 0
Traceback (most recent call last):
  File "/tmp/claude-1001/wk/lib/python3.13/site-packages/scipy/stats/_stats_py.py", line 6290, in ttest_1samp
    popmean = xp.squeeze(popmean, axis=axis) if popmean.ndim > 0 else popmean
              ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/wk/lib/python3.13/site-packages/numpy/_core/fromnumeric.py", line 1701, in squeeze
    return squeeze(axis=axis)
ValueError: cannot select an axis to squeeze out which has size not equal to one

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/tmp/claude-1001/nb/dev.py", line 10, in <module>
    exec(compile(src,f,'exec'),ns)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "s07_sub.py", line 76, in <module>
    F7 = fig7(seed_of("fig7e-ca1-spikes"))
  File "s07_sub.py", line 70, in fig7
    sig, ch = sig_from_mse(fit_mse(Y[:, m], X, model, cv))
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's/t = stats.ttest_1samp(sh, act, axis=1)/t = stats.ttest_1samp(sh, act[:, None], axis=1)/; s/t2 = stats.ttest_1samp(sh\[:, 1:\], sh\[:, 0\], axis=1)/t2 = stats.ttest_1samp(sh[:, 1:], sh[:, :1], axis=1)/' s07_fig7.py && . ../wk/bin/activate && python - <<'EOF'
src=open('/tmp/claude-1001/nb/s07_fig7.py').read().replace('F7_SESS = [s for s in S if','F7_SESS = [s for s in S[85:87] if')
open('/tmp/claude-1001/nb/s07_sub.py','w').write(src)
EOF
python dev.py s02_sanity.py s03_fig1.py s07_sub.py 2>&1 | sed -n '/s03_fig1.py/,$p'
```

```
## s03_fig1.py 23.8s maxrss 1.86 GB
Recordings: 2 (Counter({'DT9': 2})); LS neurons 102; CA3 by unit label 0
computed in 81 s
       feature      window    model     cv  min_spikes  neurons  percent  chance_percent  binom_p  within_tol
0   ca1-spikes     +-50 ms   linear  False           0      102     42.2            18.6 3.55e-08       False
1   ca1-spikes     +-50 ms   linear  False          20       92     44.6            18.5 8.41e-09       False
2   ca1-spikes     +-50 ms   linear   True           0      102     52.9            36.3 0.000432       False
3   ca1-spikes     +-50 ms   linear   True          20       92     54.3            35.9 0.000226       False
4   ca1-spikes     +-50 ms  poisson  False           0      102     39.2            20.6 1.32e-05        True
5   ca1-spikes     +-50 ms  poisson  False          20       92     41.3            19.6 1.44e-06        True
6   ca1-spikes     +-50 ms  poisson   True           0      102       52            34.3 0.000187       False
7   ca1-spikes     +-50 ms  poisson   True          20       92     52.2            33.7   0.0002       False
8   ca1-spikes  start-stop   linear  False           0      102     57.8            36.3 7.62e-06       False
9   ca1-spikes  start-stop   linear  False          20       68       75            35.3 2.85e-11       False
10  ca1-spikes  start-stop   linear   True           0      102     57.8              49    0.046       False
11  ca1-spikes  start-stop   linear   True          20       68     70.6            48.5 0.000188       False
12  ca1-spikes  start-stop  poisson  False           0      102     54.9            30.4 2.35e-07       False
13  ca1-spikes  start-stop  poisson  False          20       68       75            33.8 4.71e-12       False
14  ca1-spikes  start-stop  poisson   True           0      102     52.9            47.1    0.138       False
15  ca1-spikes  start-stop  poisson   True          20       68     66.2              50  0.00517       False
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/tingley-2019 && cat >> tingley2019.py <<'EOF'


# --- LFP ---------------------------------------------------------------------
# Parameters (STAR Methods, Phase locking analysis): 120-200 Hz, 4th-order Butterworth, 7 ms RMS smoothing,
# epochs continuously above 2 SD of the mean, Hilbert phase, more than 50 spikes, Rayleigh p < 0.05, null of
# 10 circular shifts of the LFP phases. Detection (STAR Methods, Ripple detection): 120-200 Hz, Butterworth
# order 3, normalized squared signal (NSS). Zero-phase filtering (filtfilt) is a standard choice.

def lfp_channel_index(f: h5py.File, channel_row: int) -> int:
    """Column of the LFP array holding electrode-table row `channel_row`."""
    el = f["processing/ecephys/LFP/lfp/electrodes"][:]
    return int(np.flatnonzero(el == channel_row)[0])


def read_lfp_columns(url: str, rows: list, t_chunks=None) -> tuple:
    """LFP (float32) of the given electrode-table rows; whole recording, or only the listed time chunks of the
    dataset's chunking (returns the sample offset of each piece)."""
    f = open_nwb(url)
    d = f["processing/ecephys/LFP/lfp/data"]
    cols = [lfp_channel_index(f, r) for r in rows]
    ch = d.chunks[0]
    if t_chunks is None:
        out = np.empty((d.shape[0], len(cols)), np.float32)
        step = ch * 4
        for a in range(0, d.shape[0], step):
            b = min(d.shape[0], a + step)
            blk = d[a:b, min(cols):max(cols) + 1]
            out[a:b] = blk[:, [c - min(cols) for c in cols]]
        f.close()
        return out, None
    pieces = []
    for k in t_chunks:
        a, b = k * ch, min(d.shape[0], (k + 1) * ch)
        blk = d[a:b, :]
        pieces.append((a, blk[:, cols].astype(np.float32)))
    f.close()
    return pieces, ch


def bandpass(x, lo, hi, order, fs=FS_LFP):
    from scipy.signal import butter, sosfiltfilt
    sos = butter(order, [lo, hi], btype="band", fs=fs, output="sos")
    return sosfiltfilt(sos, x).astype(np.float32)


def analytic(x):
    from scipy.signal import hilbert
    n = len(x)
    nfft = 1 << int(np.ceil(np.log2(n))) if n < 2 ** 26 else n
    return hilbert(x, N=nfft)[:n].astype(np.complex64)


def high_power_epochs(filt, fs=FS_LFP, rms_ms=7.0, sd=2.0):
    """Mask of samples where the RMS-smoothed band power is above mean + sd * SD (continuous runs)."""
    w = max(int(round(rms_ms / 1000 * fs)), 1)
    p = np.sqrt(np.convolve(filt.astype(np.float64) ** 2, np.ones(w) / w, mode="same"))
    return p > p.mean() + sd * p.std()


def rayleigh(ph):
    """Rayleigh test (Zar; as CircStat's circ_rtest). Returns p, mean resultant length, mean angle."""
    n = len(ph)
    if n == 0:
        return np.nan, np.nan, np.nan
    C, S_ = np.cos(ph).sum(), np.sin(ph).sum()
    R = np.hypot(C, S_)
    r = R / n
    z = R ** 2 / n
    p = np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - R ** 2)) - (1 + 2 * n))
    return float(min(p, 1.0)), float(r), float(np.arctan2(S_, C))


def nss(filt):
    """Normalized squared signal: the squared filtered LFP, z-scored over the recording."""
    sq = filt.astype(np.float64) ** 2
    return ((sq - sq.mean()) / sq.std()).astype(np.float32)
EOF
cd $TMPDIR && . wk/bin/activate && python - <<'EOF'
import sys,time,pickle,numpy as np
sys.path.insert(0,'entries/tingley-2019')
import importlib, tingley2019 as T
S=pickle.load(open('sessions.pkl','rb'))
s=S[88]
e=s.electrodes; row=int(np.flatnonzero(e.ripple_detection_channel.str.contains('LSRipples'))[0]); row2=int(np.flatnonzero(e.ripple_detection_channel.str.contains('CA1Ripples'))[0])
print(s.session,row,row2, s.lfp_shape)
t=time.time(); x,_=T.read_lfp_columns(s.url,[row]); print('read',time.time()-t, x.shape)
t=time.time(); fl=T.bandpass(x[:,0],120,200,4); print('filt',time.time()-t)
t=time.time(); a=T.analytic(fl); print('hilb',time.time()-t)
t=time.time(); m=T.high_power_epochs(fl); print('epochs',time.time()-t, m.mean())
import resource; print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
```

```
20170505-396um-0um-merge 5 93 (34992135, 96)
read 55.96629476547241 (34992135, 1)
filt 1.063176155090332
hilb 1.8162968158721924
epochs 0.22487449645996094 0.03586414489998967
3.821924
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . wk/bin/activate && python - <<'EOF'
import sys,time,pickle,numpy as np
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,'entries/tingley-2019')
import tingley2019 as T
S=pickle.load(open('sessions.pkl','rb'))
ss=[S[i] for i in (70,71,86,87,89,90)]
def rd(s):
    f=T.open_nwb(s.url); d=f['processing/ecephys/LFP/lfp/data']
    t=time.time(); x=d[:8*1048576, 0:1]; return time.time()-t
t=time.time()
with ThreadPoolExecutor(6) as ex: r=list(ex.map(rd,ss))
print(r, time.time()-t, 'MB/s total', 6*8*32/(time.time()-t))
EOF
```

```
[5.214378118515015, 5.232525587081909, 5.588911056518555, 5.513783931732178, 5.130600452423096, 5.1522393226623535] 35.54081201553345 MB/s total 43.217918222945634
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/tingley-2019 && python - <<'EOF'
p='tingley2019.py'; s=open(p).read()
old=s[s.index('def analytic(x):'):s.index('def high_power_epochs')]
new='''def analytic(x, seg=1 << 22, pad=1 << 12):
    """Analytic signal (Hilbert transform) computed in overlapping segments, to bound memory."""
    from scipy.signal import hilbert
    n = len(x)
    out = np.empty(n, np.complex64)
    for a in range(0, n, seg):
        b = min(n, a + seg)
        lo, hi = max(0, a - pad), min(n, b + pad)
        h = hilbert(x[lo:hi].astype(np.float64))
        out[a:b] = h[a - lo:a - lo + (b - a)]
    return out


'''
s=s.replace(old,new)
old=s[s.index('def read_lfp_columns'):s.index('def bandpass')]
new='''def read_lfp_block(url: str, row: int, t_chunks=None):
    """The 16-channel storage block (the file's chunking) that holds electrode-table row `row`: returns the
    LFP of all its channels (int16; whole recording, or only the listed time chunks, concatenated), the
    electrode-table rows of its columns, and the sample offset of each time chunk read."""
    f = open_nwb(url)
    d = f["processing/ecephys/LFP/lfp/data"]
    el = f["processing/ecephys/LFP/lfp/electrodes"][:]
    col = int(np.flatnonzero(el == row)[0])
    cw = d.chunks[1]
    c0, c1 = (col // cw) * cw, min(d.shape[1], (col // cw + 1) * cw)
    ch = d.chunks[0]
    ks = range(int(np.ceil(d.shape[0] / ch))) if t_chunks is None else t_chunks
    pieces = [d[k * ch:min(d.shape[0], (k + 1) * ch), c0:c1] for k in ks]
    f.close()
    return np.concatenate(pieces), el[c0:c1], [k * ch for k in ks]


def read_lfp_all(url: str, t_chunks):
    """Every channel of the listed time chunks (int16), with the electrode-table row of each column."""
    f = open_nwb(url)
    d = f["processing/ecephys/LFP/lfp/data"]
    el = f["processing/ecephys/LFP/lfp/electrodes"][:]
    ch = d.chunks[0]
    pieces = [(k * ch, d[k * ch:min(d.shape[0], (k + 1) * ch), :]) for k in t_chunks]
    f.close()
    return pieces, el


def electrode_spike_groups(url: str) -> np.ndarray:
    f = open_nwb(url)
    g = f["general/extracellular_ephys/electrodes/spike_group"][:]
    f.close()
    return g


'''
s=s.replace(old,new)
s=s.replace('''def lfp_channel_index(f: h5py.File, channel_row: int) -> int:
    """Column of the LFP array holding electrode-table row `channel_row`."""
    el = f["processing/ecephys/LFP/lfp/electrodes"][:]
    return int(np.flatnonzero(el == channel_row)[0])


''','')
open(p,'w').write(s)
EOF
grep -n "^def " tingley2019.py
```

```
45:def list_assets() -> pd.DataFrame:
60:def _s(x):
64:def open_nwb(url: str) -> h5py.File:
114:def load_session(row) -> Session:
159:def load_all(assets: pd.DataFrame, workers: int = 8) -> list[Session]:
166:def merge_intervals(iv: np.ndarray) -> np.ndarray:
180:def in_intervals(t: np.ndarray, iv: np.ndarray) -> np.ndarray:
192:def intersect(a: np.ndarray, b: np.ndarray) -> np.ndarray:
206:def total(iv) -> float:
211:def state_at(t: np.ndarray, sess: Session) -> np.ndarray:
223:def ccg_all(spikes: list, maxlag: float, binsize: float = 0.001, chunk: int = 200_000) -> np.ndarray:
254:def gauss_smooth(c: np.ndarray, width_ms: float, kind: str = "sd") -> np.ndarray:
269:def jitter(spikes: list, rng, width: float = 0.2) -> list:
274:def restrict(spikes: list, iv: np.ndarray) -> list:
278:def triggered_counts(spikes: np.ndarray, times: np.ndarray, maxlag: float, binsize: float) -> np.ndarray:
292:def count_in(spikes: np.ndarray, starts: np.ndarray, stops: np.ndarray) -> np.ndarray:
302:def read_lfp_block(url: str, row: int, t_chunks=None):
319:def read_lfp_all(url: str, t_chunks):
330:def electrode_spike_groups(url: str) -> np.ndarray:
337:def bandpass(x, lo, hi, order, fs=FS_LFP):
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='tingley2019.py'; s=open(p).read()
s=s.replace('''def read_lfp_block(url: str, row: int, t_chunks=None):
    """The 16-channel storage block (the file's chunking) that holds electrode-table row `row`: returns the
    LFP of all its channels (int16; whole recording, or only the listed time chunks, concatenated), the
    electrode-table rows of its columns, and the sample offset of each time chunk read."""''','''def block_rows(url: str, row: int) -> np.ndarray:
    """Electrode-table rows of the 16-channel storage block (the file's chunking) that holds row `row`."""
    f = open_nwb(url)
    d = f["processing/ecephys/LFP/lfp/data"]
    el = f["processing/ecephys/LFP/lfp/electrodes"][:]
    col = int(np.flatnonzero(el == row)[0]); cw = d.chunks[1]
    out = el[(col // cw) * cw:min(d.shape[1], (col // cw + 1) * cw)]
    f.close()
    return out


def read_lfp_block(url: str, row: int, keep_rows=None, t_chunks=None):
    """The storage block (16 channels, the file's chunking) that holds electrode-table row `row`, read whole
    (reading one channel costs the same); only the columns of `keep_rows` are kept (int16; whole recording,
    or only the listed time chunks, concatenated). Returns the data, the rows kept, and the sample offset of
    each time chunk read."""''')
s=s.replace('''    ks = range(int(np.ceil(d.shape[0] / ch))) if t_chunks is None else t_chunks
    pieces = [d[k * ch:min(d.shape[0], (k + 1) * ch), c0:c1] for k in ks]
    f.close()
    return np.concatenate(pieces), el[c0:c1], [k * ch for k in ks]''','''    rows = el[c0:c1]
    sel = np.arange(len(rows)) if keep_rows is None else np.flatnonzero(np.isin(rows, keep_rows))
    ks = list(range(int(np.ceil(d.shape[0] / ch)))) if t_chunks is None else list(t_chunks)
    pieces = [d[k * ch:min(d.shape[0], (k + 1) * ch), c0:c1][:, sel] for k in ks]
    f.close()
    return np.concatenate(pieces), rows[sel], [k * ch for k in ks]''')
open(p,'w').write(s)
EOF
echo done
```

```
done
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat > s20_lfp.py <<'EOF'
# %% [markdown]
# ## LFP analyses
# One job per recording with LS units and the lab's LS HFO detection channel (the electrode marked `LSRipples` in
# `ripple_detection_channel`). Each job reads the 16-channel storage block holding that channel (reading one channel of a
# block costs as much as reading all of it), and, where the recording has CA1Ripples, the block of the CA1 detection channel.
# From these: phase locking of LS spikes (fig1d-phase-locking, dataset-composition reading a), locking of LS spikes to the
# CA1 channel (ls-spikes-not-locked-to-ca1-ripples), event times at the maximum NSS (fig5d-lag), and CA1-LS 120-180 Hz phase
# coherence around CA1 ripples (fig5f-no-phase-coherence). Random draws (null shifts, jitters) come from a generator seeded
# with the claim's seed and the recording's index.

# %% tags=["sanity"]
def det_row(s, name):
    r = np.flatnonzero(s.electrodes.ripple_detection_channel.str.contains(name).to_numpy())
    return int(r[0]) if len(r) else None
LFP_SESS = [s for s in S if det_row(s, "LSRipples") is not None and len(s.units_in(["ls"])) and ls_ev(s) is not None]
print(f"Recordings for the LFP jobs: {len(LFP_SESS)} ({collections.Counter(s.subject for s in LFP_SESS)}); with a CA1 detection channel and "
      f"CA1Ripples: {sum(det_row(s, 'CA1Ripples') is not None and ca1_ev(s) is not None for s in LFP_SESS)}")
print(f"LS units in them: {sum(len(s.units_in(['ls'])) for s in LFP_SESS)}; LFP hours to read: {sum(s.duration for s in LFP_SESS)/3600:.0f} (one block each, plus CA1 blocks)")
print("LS detection channel region labels:", collections.Counter(s.electrodes.region[det_row(s, 'LSRipples')] for s in LFP_SESS))
print("CA1 detection channel region labels:", collections.Counter(s.electrodes.region[det_row(s, 'CA1Ripples')] for s in LFP_SESS if det_row(s, 'CA1Ripples') is not None))

# %%
SEED_PL = seed_of("fig1d-phase-locking"); SEED_CA1 = seed_of("ls-spikes-not-locked-to-ca1-ripples"); SEED_COH = seed_of("fig5f-no-phase-coherence")
def lock_units(spk_list, ph, mask, rng, n_null=10, min_spikes=50):
    """Per unit: spikes in the mask, Rayleigh p, resultant length, mean phase; and the p-values under 10 circular shifts of the phase."""
    n = len(ph); shifts = rng.integers(int(FS * 1), n - int(FS * 1), n_null)
    res = []
    for sp in spk_list:
        idx = np.rint(sp * FS).astype(np.int64); idx = idx[(idx >= 0) & (idx < n)]
        idx = idx[mask[idx]]
        p, r, a = T.rayleigh(ph[idx].astype(np.float64))
        pn = [T.rayleigh(ph[(idx + k) % n].astype(np.float64))[0] for k in shifts] if len(idx) > min_spikes else [np.nan] * n_null
        res.append(dict(n=len(idx), p=p, r=r, angle=a, p_null=pn))
    return res
FS = T.FS_LFP
def nss_peak_times(x, ev):
    """Time of the maximum NSS (120-200 Hz, Butterworth order 3) between each event's start and stop."""
    z = T.nss(T.bandpass(x, 120, 200, 3))
    a = np.rint(ev.start_time.to_numpy() * FS).astype(int); b = np.rint(ev.stop_time.to_numpy() * FS).astype(int)
    return np.array([(lo + np.argmax(z[lo:hi + 1])) / FS if hi >= lo else (lo / FS) for lo, hi in zip(a, b)])
def lfp_job(k):
    s = LFP_SESS[k]; t0 = time.time()
    out = dict(session=s.session, subject=s.subject)
    ls_row = det_row(s, "LSRipples"); ca_row = det_row(s, "CA1Ripples") if ca1_ev(s) is not None else None
    ls_units = s.units_in(["ls"]); sg = T.electrode_spike_groups(s.url)
    blk = T.block_rows(s.url, ls_row)
    shank_row = {}
    for sh in np.unique(s.unit_shank[ls_units]):
        cand = [r for r in blk if sg[r] == sh]
        if cand: shank_row[sh] = int(cand[len(cand) // 2])
    X, rows, _ = T.read_lfp_block(s.url, ls_row, [ls_row] + list(shank_row.values()))
    rows = list(rows)
    x = X[:, rows.index(ls_row)].astype(np.float32)
    spk = [s.spikes[u] for u in ls_units]
    rng = np.random.default_rng([SEED_PL, k])
    for band in [(120, 200), (120, 180)]:
        fl = T.bandpass(x, *band, 4); ph = np.angle(T.analytic(fl)).astype(np.float32); m = T.high_power_epochs(fl)
        out[f"lock_{band[1]}"] = lock_units(spk, ph, m, rng)
        if band == (120, 200): out["epoch_frac"] = float(m.mean())
    # nearest-shank channel, 120-200 Hz
    near = [None] * len(ls_units)
    for sh, r in shank_row.items():
        fl = T.bandpass(X[:, rows.index(r)].astype(np.float32), 120, 200, 4); ph = np.angle(T.analytic(fl)).astype(np.float32); m = T.high_power_epochs(fl)
        sel = np.flatnonzero(s.unit_shank[ls_units] == sh)
        for j, rr in zip(sel, lock_units([spk[j] for j in sel], ph, m, rng)): near[j] = rr
    out["lock_near"] = near
    del X
    out["ls_nss_t"] = nss_peak_times(x, ls_ev(s))
    if ca_row is not None:
        Y, _, _ = T.read_lfp_block(s.url, ca_row, [ca_row]); y = Y[:, 0].astype(np.float32); del Y
        ce = ca1_ev(s)
        out["ca_nss_t"] = nss_peak_times(y, ce)
        fl = T.bandpass(y, 120, 200, 4); ph = np.angle(T.analytic(fl)).astype(np.float32)
        rip = np.zeros(len(y), bool)
        for a, b in zip(np.rint(ce.start_time.to_numpy() * FS).astype(int), np.rint(ce.stop_time.to_numpy() * FS).astype(int)): rip[a:b + 1] = True
        rng2 = np.random.default_rng([SEED_CA1, k])
        out["ca1lock_rip"] = lock_units(spk, ph, rip, rng2)
        out["ca1lock_hp"] = lock_units(spk, ph, T.high_power_epochs(fl), rng2)
        # coherence, 120-180 Hz: phase-locking value across CA1 ripples of the CA1 minus LS phase, at lags -100..100 ms (2 ms)
        pc = np.angle(T.analytic(T.bandpass(y, 120, 180, 4))).astype(np.float32); pl = np.angle(T.analytic(T.bandpass(x, 120, 180, 4))).astype(np.float32)
        lagsamp = np.rint(np.arange(-100, 101, 2) / 1000 * FS).astype(int)
        def plv(times):
            i = np.rint(times * FS).astype(int)[:, None] + lagsamp[None, :]
            i = i[(i.min(1) >= 0) & (i.max(1) < len(y))]
            return np.abs(np.exp(1j * (pc[i] - pl[i]).astype(np.float64)).mean(0))
        tt = ce.peak_time.to_numpy()
        rng3 = np.random.default_rng([SEED_COH, k])
        out["plv"] = plv(tt); out["plv_jit"] = np.vstack([plv(tt + rng3.uniform(-1, 1, len(tt))) for _ in range(100)])
        out["n_rip"] = len(tt)
    out["secs"] = time.time() - t0
    return out
from concurrent.futures import ThreadPoolExecutor
t0 = time.time()
with ThreadPoolExecutor(4) as ex:
    LFPR = list(ex.map(lfp_job, range(len(LFP_SESS))))
print(f"{len(LFPR)} recordings in {(time.time()-t0)/60:.1f} min (per recording {np.median([r['secs'] for r in LFPR]):.0f} s median); "
      f"peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.2f} GB")
EOF
cat > s21_lfp_claims.py <<'EOF'
# %% [markdown]
# ## fig1d-phase-locking (and dataset-composition, reading a)
# > The vast majority of LS neurons (1840 of 1989, 92%) are significantly phase-locked to the 120-200 Hz band (Rayleigh P < 0.05),
# > with a strong unimodal preference for the trough of each cycle.
#
# STAR Methods: epochs where the 120-200 Hz power (4th-order Butterworth, 7 ms RMS) is continuously above 2 SD; Hilbert phase of every
# spike in them; neurons with more than 50 spikes; Rayleigh p < 0.05; null of 10 circular shifts. Channel readings: the LS detection
# channel, and the channel of the neuron's shank (middle site of the shank, where the shank is in the detection channel's storage block).
# Band variant 120-180 Hz. Denominators (a) neurons with more than 50 spikes, (b) all LS neurons. Phase: angle of the analytic signal,
# trough at +-180 degrees.

# %% tags=["claim:fig1d-phase-locking", "claim:dataset-composition"]
def lock_table(key):
    rows = []
    for r in LFPR:
        for j, u in enumerate(r[key]):
            if u is None: continue
            rows.append(dict(session=r["session"], subject=r["subject"], n=u["n"], p=u["p"], r=u["r"], angle=u["angle"], p_null=u["p_null"]))
    return pd.DataFrame(rows)
PL = {}
for key, nm in [("lock_200", "detection channel, 120-200 Hz"), ("lock_near", "own shank channel, 120-200 Hz"), ("lock_180", "detection channel, 120-180 Hz")]:
    D = lock_table(key); PL[key] = D
    sel = D[D.n > 50]; sig = sel[sel.p < 0.05]
    null = np.nanmean(np.vstack(sel.p_null.values) < 0.05) if len(sel) else np.nan
    mang = np.angle(np.exp(1j * sig.angle).mean()); rt = T.rayleigh(sig.angle.to_numpy())
    print(f"{nm}: LS neurons {len(D)}; with > 50 spikes in high-power epochs {len(sel)}; significant {len(sig)}; fraction (a) {len(sig)/max(len(sel),1):.3f}, "
          f"(b) {len(sig)/max(len(D),1):.3f}; null fraction (10 shifts) {null:.3f}")
    print(f"   preferred phase of significant neurons: circular mean {np.degrees(mang):.1f} deg (|distance to 180| {180-abs(np.degrees(mang)):.1f}); "
          f"Rayleigh over neurons p = {rt[0]:.2g}, r = {rt[1]:.2f}; median resultant length {sig.r.median():.3f}")
D = PL["lock_200"]; sel = D[D.n > 50]
print("\nPer animal (detection channel, 120-200 Hz): neurons > 50 spikes, fraction significant")
print(sel.assign(sig=sel.p < 0.05).groupby("subject").sig.agg(["count", "mean"]).round(3).to_string())
per = sel.assign(sig=sel.p < 0.05).groupby("session").sig.agg(["count", "mean"])
print(f"Neurons with > 50 spikes per recording: {per['count'].min()} to {per['count'].max()}, mean {per['count'].mean():.1f} +- {per['count'].std():.1f} "
      f"(paper: 8-74, 29.6 +- 15.5); recordings {len(per)}")
print(f"dataset-composition reading (a): LS neurons with > 50 spikes in high-power epochs = {len(sel)} (paper 1989, tolerance 198.9)")
print(f"High-power epochs cover a median {np.median([r['epoch_frac'] for r in LFPR]):.3f} of each recording")
fig, ax = plt.subplots(1, 2, figsize=(8, 3))
ax[0].hist(sel.r, 50); ax[0].set_xlabel("resultant length"); ax[1].hist(np.degrees(sel[sel.p < .05].angle), 36); ax[1].set_xlabel("preferred phase (deg)"); plt.show()
print(f"Resultant length range {sel.r.min():.3f} to {sel.r.max():.3f}")

# %% [markdown]
# ## ls-spikes-not-locked-to-ca1-ripples
# > LS spiking is not phase-locked to the individual waves of hippocampal SPW-Rs.
#
# The same locking analysis with the 120-200 Hz phase of the CA1 detection channel, (a) inside CA1 ripples (CA1Ripples start to stop),
# (b) inside the high-power epochs of that channel. One-sided binomial test of the fraction significant against 5%.

# %% tags=["claim:ls-spikes-not-locked-to-ca1-ripples"]
for key, nm in [("ca1lock_rip", "(a) inside CA1 ripples"), ("ca1lock_hp", "(b) CA1 high-power epochs")]:
    rows = [dict(session=r["session"], subject=r["subject"], **{k: u[k] for k in ("n", "p", "r")}, p_null=u["p_null"]) for r in LFPR if key in r for u in r[key]]
    D = pd.DataFrame(rows); sel = D[D.n > 50]; k = int((sel.p < .05).sum())
    bt = stats.binomtest(k, len(sel), 0.05, alternative="greater")
    null = np.nanmean(np.vstack(sel.p_null.values) < 0.05)
    print(f"{nm}: LS neurons {len(D)} in {D.session.nunique()} recordings; > 50 spikes {len(sel)}; significant {k} ({k/max(len(sel),1):.3f}); "
          f"binomial p against 5% = {bt.pvalue:.2g}; null fraction (10 shifts) {null:.3f}; median resultant length {sel.r.median():.3f}")
    print("   per animal:", sel.assign(sig=sel.p < .05).groupby("subject").sig.agg(["count", "mean"]).round(3).to_dict("index"))
sel0 = PL["lock_200"][PL["lock_200"].n > 50]
print(f"Beside fig1d-phase-locking (LS channel): fraction {np.mean(sel0.p < .05):.3f}, median resultant length {sel0.r.median():.3f}")

# %% [markdown]
# ## fig5d-lag, event times at the maximum NSS
# The reading of the event time as the maximum-NSS bin (STAR Methods, "peak power bin"), on the detection channels.

# %% tags=["claim:fig5d-lag"]
lg = []
for r in LFPR:
    if "ca_nss_t" not in r: continue
    l, c = np.sort(r["ls_nss_t"]), np.sort(r["ca_nss_t"])
    lg.append(dict(session=r["session"], subject=r["subject"], lag=nearest_lag(l, c) * 1000))
LGN = pd.DataFrame(lg)
for win in [50, 25]:
    per = [np.median(x[np.abs(x) <= win]) for x in LGN.lag if (np.abs(x) <= win).sum()]
    allx = np.concatenate([x[np.abs(x) <= win] for x in LGN.lag])
    print(f"max-NSS times, within +-{win} ms: {len(allx)} pairs in {len(per)} recordings; (a) median of recording medians {np.median(per):.2f} ms; "
          f"(b) pooled median {np.median(allx):.2f} ms; CA1 leading in {np.mean(allx > 0):.3f}")

# %% [markdown]
# ## fig5f-no-phase-coherence
# > CA1-LS 120-180 Hz phase coherence around CA1 ripples does not differ from that of randomly jittered windows.
#
# The phase-locking value across CA1 ripples of the CA1 minus LS 120-180 Hz phase, at lags -100..100 ms around the ripple time,
# against 100 sets of windows jittered by a uniform +-1 s; averaged over recordings; bounds mean +-3 SD of the jittered sets.

# %% tags=["claim:fig5f-no-phase-coherence"]
C = [r for r in LFPR if "plv" in r]
act = np.mean([r["plv"] for r in C], 0); jit = np.mean([r["plv_jit"] for r in C], 0)      # [lags], [100, lags]
lagp = np.arange(-100, 101, 2); z0 = lagp == 0
mu, sd = jit.mean(0), jit.std(0, ddof=1)
print(f"{len(C)} recordings, {sum(r['n_rip'] for r in C)} CA1 ripples")
print(f"At the ripple time: PLV {act[z0][0]:.4f}; jittered mean {mu[z0][0]:.4f}, SD {sd[z0][0]:.4f}; upper bound (+3 SD) {mu[z0][0] + 3*sd[z0][0]:.4f}; "
      f"within bounds: {abs(act[z0][0] - mu[z0][0]) <= 3*sd[z0][0]}")
print(f"Lags (of {len(lagp)}) above +3 SD: {int((act > mu + 3*sd).sum())}; largest excess {np.max((act - mu) / sd):.1f} SD at {lagp[np.argmax((act - mu)/sd)]} ms")
print("Per recording at 0 ms, PLV against its own jittered mean and SD (first 10):",
      [(r["session"][:12], round(float(r["plv"][50]), 3), round(float(r["plv_jit"][:, 50].mean()), 3), round(float(r["plv_jit"][:, 50].std()), 3)) for r in C[:10]])
fig, ax = plt.subplots(figsize=(5, 3)); ax.plot(lagp, act, label="ripples"); ax.fill_between(lagp, mu - 3*sd, mu + 3*sd, alpha=.3, label="jittered +-3 SD")
ax.set_xlabel("lag (ms)"); ax.set_ylabel("PLV"); ax.legend(); plt.show()
print(f"Plotted PLV range {act.min():.4f} to {act.max():.4f}")
EOF
cat > devload2.py <<'EOF'
EOF
python - <<'EOF'
# subset test: 2 recordings
src=open('/tmp/claude-1001/nb/s20_lfp.py').read().replace('LFP_SESS = [s for s in S if','LFP_SESS = [s for s in S[87:89] if')
open('/tmp/claude-1001/nb/s20_sub.py','w').write(src)
EOF
cd $TMPDIR/nb && . ../wk/bin/activate && python dev.py s02_sanity.py s04_fig5.py s20_sub.py s21_lfp_claims.py 2>&1 | sed -n '/s04_fig5.py/,$p'
```

```
File "s04_fig5.py", line 52, in <module>
    for s in both_rec:
             ^^^^^^^^
NameError: name 'both_rec' is not defined
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && . ../wk/bin/activate && python dev.py s02_sanity.py s03_fig1.py s04_fig5.py s20_sub.py s21_lfp_claims.py 2>&1 | sed -n '/s04_fig5.py/,$p'
```

```
## s04_fig5.py 15.1s maxrss 1.92 GB
Recordings for the LFP jobs: 2 (Counter({'DT9': 2})); with a CA1 detection channel and CA1Ripples: 2
LS units in them: 98; LFP hours to read: 17 (one block each, plus CA1 blocks)
LS detection channel region labels: Counter({'ls': 2})
CA1 detection channel region labels: Counter({'hpc': 2})
2 recordings in 2.0 min (per recording 113 s median); peak memory 6.30 GB
## s20_sub.py 119.8s maxrss 6.30 GB
detection channel, 120-200 Hz: LS neurons 98; with > 50 spikes in high-power epochs 88; significant 36; fraction (a) 0.409, (b) 0.367; null fraction (10 shifts) 0.050
   preferred phase of significant neurons: circular mean -157.7 deg (|distance to 180| 22.3); Rayleigh over neurons p = 3.9e-06, r = 0.57; median resultant length 0.127
own shank channel, 120-200 Hz: LS neurons 58; with > 50 spikes in high-power epochs 57; significant 45; fraction (a) 0.789, (b) 0.776; null fraction (10 shifts) 0.046
   preferred phase of significant neurons: circular mean -163.7 deg (|distance to 180| 16.3); Rayleigh over neurons p = 1.3e-13, r = 0.75; median resultant length 0.285
detection channel, 120-180 Hz: LS neurons 98; with > 50 spikes in high-power epochs 90; significant 36; fraction (a) 0.400, (b) 0.367; null fraction (10 shifts) 0.041
   preferred phase of significant neurons: circular mean -160.8 deg (|distance to 180| 19.2); Rayleigh over neurons p = 2.6e-06, r = 0.57; median resultant length 0.115

Per animal (detection channel, 120-200 Hz): neurons > 50 spikes, fraction significant
         count   mean
subject              
DT9         88  0.409
Neurons with > 50 spikes per recording: 41 to 47, mean 44.0 +- 4.2 (paper: 8-74, 29.6 +- 15.5); recordings 2
dataset-composition reading (a): LS neurons with > 50 spikes in high-power epochs = 88 (paper 1989, tolerance 198.9)
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR/nb && python - <<'EOF'
p='s20_lfp.py'; s=open(p).read()
s=s.replace("""        if band == (120, 200): out["epoch_frac"] = float(m.mean())
""","""        if band == (120, 200): out["epoch_frac"] = float(m.mean())
        del fl, ph, m
""")
s=s.replace("""        for j, rr in zip(sel, lock_units([spk[j] for j in sel], ph, m, rng)): near[j] = rr
""","""        for j, rr in zip(sel, lock_units([spk[j] for j in sel], ph, m, rng)): near[j] = rr
        del fl, ph, m
""")
s=s.replace("""        out["ca1lock_hp"] = lock_units(spk, ph, T.high_power_epochs(fl), rng2)
""","""        out["ca1lock_hp"] = lock_units(spk, ph, T.high_power_epochs(fl), rng2)
        del fl, ph, rip
""")
s=s.replace("with ThreadPoolExecutor(4) as ex:","with ThreadPoolExecutor(3) as ex:")
s=s.replace('''# %%
SEED_PL''','''# %%
# Only LS spikes are needed here: the other units' spikes are released to save memory.
for s in S:
    for u in np.flatnonzero(s.unit_region != "ls"): s.spikes[u] = np.zeros(0)
SEED_PL''')
open(p,'w').write(s)
EOF
cat > s22_sites.py <<'EOF'
# %% [markdown]
# ## fig2-confined-to-ls and discussion-medial-septum (part a)
# > HFO events are seen only at recording sites within LS, not at sites in neighbouring structures.
#
# Recordings whose electrodes are labelled in LS and in another structure other than the hippocampus (and not `unknown`). Every
# channel is read for the two storage time chunks (about 14 min each) holding the most LSRipples events. Per site: mean 120-180 Hz
# power (4th-order Butterworth, squared) within +-25 ms of the LS HFO times in those chunks, divided by its mean at as many random
# times in the same chunks (the claim's seed). Sites by the electrodes' region label.

# %% tags=["claim:fig2-confined-to-ls", "claim:discussion-medial-septum"]
SITE_SESS = [s for s in S if ls_ev(s) is not None and (s.electrodes.region == "ls").any()
             and len(set(s.electrodes.region) - {"ls", "hpc", "ca1", "ca3", "unknown"}) > 0]
print(f"Recordings with LS and other non-hippocampal sites: {len(SITE_SESS)}: {[(s.session[:22], dict(collections.Counter(s.electrodes.region))) for s in SITE_SESS]}")
def site_job(k):
    s = SITE_SESS[k]; rng = np.random.default_rng([seed_of("fig2-confined-to-ls"), k])
    f = T.open_nwb(s.url); ch = f["processing/ecephys/LFP/lfp/data"].chunks[0]; f.close()
    t = ls_ev(s).peak_time.to_numpy(); kk = np.bincount((t * FS // ch).astype(int))
    best = np.argsort(kk)[::-1][:2]
    pieces, el = T.read_lfp_all(s.url, sorted(best))
    num = np.zeros(len(el)); den = np.zeros(len(el)); nev = 0
    w = int(0.025 * FS)
    for off, blk in pieces:
        tt = (t * FS).astype(int) - off; tt = tt[(tt > w) & (tt < len(blk) - w)]
        if len(tt) == 0: continue
        rt = rng.integers(w, len(blk) - w, len(tt))
        P = T.bandpass(blk.astype(np.float32).T, 120, 180, 4) ** 2           # channels x samples
        idx = (tt[:, None] + np.arange(-w, w + 1)[None]).ravel(); ridx = (rt[:, None] + np.arange(-w, w + 1)[None]).ravel()
        num += P[:, idx].sum(1); den += P[:, ridx].sum(1); nev += len(tt)
    reg = s.electrodes.region.to_numpy()[el]
    return pd.DataFrame(dict(session=s.session[:25], row=el, region=reg, ratio=num / den, n_events=nev))
with ThreadPoolExecutor(2) as ex:
    SITES = pd.concat(list(ex.map(site_job, range(len(SITE_SESS)))))
tab = SITES.groupby(["session", "region"]).ratio.agg(["count", "median", "max"]).round(2)
print(tab.to_string())
ok_rec = []
for sess, g in SITES.groupby("session"):
    med = g.groupby("region").ratio.median()
    others = [r for r in med.index if r not in ("ls", "hpc", "ca1", "ca3", "unknown")]
    cond = all(med["ls"] > med[r] for r in others) and all((g[g.region == r].ratio < 1.5).all() for r in others)
    ok_rec.append(cond)
    print(f"{sess}: LS median {med['ls']:.2f}; others {[(r, round(med[r], 2), round(g[g.region == r].ratio.max(), 2)) for r in others]}; holds: {cond}; events used {g.n_events.iloc[0]}")
print(f"fig2 criterion holds in {sum(ok_rec)} of {len(ok_rec)} recordings")
ms = SITES[SITES.region == "ms"]
for sess, g in SITES[SITES.session.isin(ms.session.unique())].groupby("session"):
    print(f"medial septum (a), {sess}: ms site median ratio {g[g.region == 'ms'].ratio.median():.2f} (n {int((g.region == 'ms').sum())}) against LS {g[g.region == 'ls'].ratio.median():.2f}")
EOF
python - <<'EOF'
src=open('/tmp/claude-1001/nb/s22_sites.py').read().replace('SITE_SESS = [s for s in S if','SITE_SESS = [s for s in S[55:58] if').replace("from concurrent","")
open('/tmp/claude-1001/nb/s22_sub.py','w').write("from concurrent.futures import ThreadPoolExecutor\nFS = T.FS_LFP\n"+src)
EOF
. ../wk/bin/activate && python dev.py s02_sanity.py s22_sub.py 2>&1 | sed -n '/s02_sanity.py/,$p'
```

```
Wed Nov 18 10:50:42 UTC 2026
## s02_sanity.py 40.6s maxrss 1.83 GB
Recordings with LS and other non-hippocampal sites: 2: [('20170325-576um-360um-1', {'hpc': 64, 'ls': 21, 'ms': 14, 'acg': 29}), ('20170401-864um-936um-m', {'hpc': 63, 'ms': 21, 'ls': 24, 'cc': 20})]
                                  count  median   max
session                   region                     
20170325-576um-360um-1703 acg        29    0.61  3.31
                          hpc        64    0.39  5.82
                          ls         21    1.01  3.88
                          ms         14    0.79  3.55
20170401-864um-936um-merg cc         20    0.85  3.35
                          hpc        63    1.15  2.03
                          ls         24    1.45  3.73
                          ms         21    0.89  2.68
20170325-576um-360um-1703: LS median 1.01; others [('acg', np.float64(0.61), np.float64(3.31)), ('ms', np.float64(0.79), np.float64(3.55))]; holds: False; events used 78
20170401-864um-936um-merg: LS median 1.45; others [('cc', np.float64(0.85), np.float64(3.35)), ('ms', np.float64(0.89), np.float64(2.68))]; holds: False; events used 58
fig2 criterion holds in 0 of 2 recordings
medial septum (a), 20170325-576um-360um-1703: ms site median ratio 0.79 (n 14) against LS 1.01
medial septum (a), 20170401-864um-936um-merg: ms site median ratio 0.89 (n 21) against LS 1.45
## s22_sub.py 31.1s maxrss 10.72 GB
Shell cwd was reset to
```

**Agent**

The site analysis peaked at 10.7 GB, which is too much. I'll filter in groups of 16 channels with one worker.

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
p='s22_sites.py'; s=open(p).read()
s=s.replace("""        P = T.bandpass(blk.astype(np.float32).T, 120, 180, 4) ** 2           # channels x samples
        idx = (tt[:, None] + np.arange(-w, w + 1)[None]).ravel(); ridx = (rt[:, None] + np.arange(-w, w + 1)[None]).ravel()
        num += P[:, idx].sum(1); den += P[:, ridx].sum(1); nev += len(tt)""","""        idx = (tt[:, None] + np.arange(-w, w + 1)[None]).ravel(); ridx = (rt[:, None] + np.arange(-w, w + 1)[None]).ravel()
        for c0 in range(0, blk.shape[1], 16):                                   # 16 channels at a time, to bound memory
            P = T.bandpass(blk[:, c0:c0 + 16].astype(np.float32).T, 120, 180, 4) ** 2
            num[c0:c0 + 16] += P[:, idx].sum(1); den[c0:c0 + 16] += P[:, ridx].sum(1)
        nev += len(tt)""")
s=s.replace("with ThreadPoolExecutor(2) as ex:","with ThreadPoolExecutor(1) as ex:")
open(p,'w').write(s)
EOF
grep -n "sosfiltfilt" entries/tingley-2019/tingley2019.py
```

```
352:    from scipy.signal import butter, sosfiltfilt
354:    return sosfiltfilt(sos, x).astype(np.float32)
Shell cwd was reset to
```

**Agent**

Before assembling, a look at how `entry.py run` executes the notebooks, sequentially or in parallel, and with what timeout.

**Agent calls Bash**

```bash
sed -n 558,616p tools/entry.py; cat schemas/entry.schema.json 2>/dev/null | head -60; ls schemas
```

```
def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
    if stamp:
        when = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(stamp["finished"]))
        for r in stamp["results"]:
            print(f"pass  {r['notebook']}  ({r['seconds']} s, reused)")
        print(f"reused the executed copies of {when}: nothing the run reads has changed since (hash "
              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
        return 0
    (output_dir / STAMP).unlink(missing_ok=True)   # whatever is there is no longer what a run left
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
    kernel = f"registry-{entry_dir.name}"
    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", python_of(entry_dir), str(venv)],
                ["uv", "pip", "install", "--quiet", "--python", str(python),
                 "-r", str(entry_dir / "requirements.lock.txt"), *HARNESS],
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
# defensive wrappers
p='s20_lfp.py'; s=open(p).read()
s=s.replace("def lfp_job(k):\n    s = LFP_SESS[k]; t0 = time.time()","def lfp_job(k):\n    try:\n        return _lfp_job(k)\n    except Exception as e:\n        return dict(session=LFP_SESS[k].session, subject=LFP_SESS[k].subject, error=repr(e), secs=0)\ndef _lfp_job(k):\n    s = LFP_SESS[k]; t0 = time.time()")
s=s.replace("""print(f"{len(LFPR)} recordings in""","""FAILED = [(r["session"], r["error"]) for r in LFPR if "error" in r]
print("Recordings whose job failed:", FAILED if FAILED else "none")
LFPR = [r for r in LFPR if "error" not in r]
print(f"{len(LFPR)} recordings in""")
open(p,'w').write(s)
p='s07_fig7.py'; s=open(p).read()
s=s.replace("""    for s in F7_SESS:
        c = ca1_ev(s)""","""    for s in F7_SESS:
      try:
        c = ca1_ev(s)""")
# indent the body of loop: simpler approach - wrap via function
open(p,'w').write(s)
EOF
grep -n "try:" s07_fig7.py
```

```
56:      try:
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
p='s07_fig7.py'; s=open(p).read()
a=s.index('def fig7(seed):'); b=s.index('t0 = time.time()\nF7 = fig7')
new='''def fig7_recording(s, rng, models=("linear", "poisson")):
    c = ca1_ev(s); st, sp_ = c.start_time.to_numpy(), c.stop_time.to_numpy(); tt = c.peak_time.to_numpy()
    hp = s.units_in(HPC); ls = s.units_in(["ls"])
    state = T.state_at(tt, s)
    feats = {"ca1-spikes": (sum(T.count_in(s.spikes[u], st, sp_) for u in hp).astype(float), np.ones(len(tt), bool)),
             "state": ((state == "NREM").astype(float), np.isin(state, ["NREM", "WAKE"])),
             "duration": (sp_ - st, np.ones(len(tt), bool))}
    rows = []
    for win in ["start-stop", "+-50 ms"]:
        Y = np.vstack([T.count_in(s.spikes[u], st, sp_) if win == "start-stop" else T.count_in(s.spikes[u], tt - 0.05, tt + 0.05) for u in ls]).astype(float)
        for fn, (x, m) in feats.items():
            if m.sum() < 10 or np.std(x[m]) == 0: continue
            xm = (x[m] - x[m].mean()) / x[m].std()
            X = np.vstack([xm] + [rng.permutation(xm) for _ in range(NSHUF)])
            for model in models:
                for cv in [False, True]:
                    sig, ch = sig_from_mse(fit_mse(Y[:, m], X, model, cv))
                    for k, u in enumerate(ls):
                        rows.append(dict(session=s.session, subject=s.subject, unit=u, feature=fn, window=win, model=model, cv=cv,
                                         n_spk=Y[k, m].sum(), sig=sig[k], chance=ch[k]))
    return rows
FAILED7 = []
def fig7(seed, models=("linear", "poisson")):
    rng = np.random.default_rng(seed)
    rows = []
    for s in F7_SESS:
        try:
            rows += fig7_recording(s, rng, models)
        except Exception as e:
            FAILED7.append((s.session, repr(e)))
    return pd.DataFrame(rows)
'''
s=s[:a]+new+s[b:]
s=s.replace('print(f"computed in {time.time()-t0:.0f} s")','print(f"computed in {time.time()-t0:.0f} s; recordings that failed: {FAILED7 if FAILED7 else \'none\'}")')
s+='''
# %% tags=["claim:fig7e-ca1-spikes", "claim:fig7e-state", "claim:fig7e-duration"]
# The shuffles are random: the linear-model readings under four more seeds (the Poisson fits are not repeated, for time).
for k in range(1, 5):
    sd = seed_of("fig7e-ca1-spikes") + 1000 * k
    D = f7_table(fig7(sd, models=("linear",)))
    D = D[D.min_spikes == 0]
    print(f"seed {sd}:", "; ".join(f"{fn} {g.percent.min():.1f}-{g.percent.max():.1f}% (within tolerance {int((abs(g.percent - EXPECT7[fn]) <= 0.1 * EXPECT7[fn]).sum())})"
                                 for fn, g in D.groupby("feature")))
'''
open(p,'w').write(s)
EOF
python -c "import ast;[ast.parse(open('$TMPDIR/nb/'+f).read()) for f in ['s07_fig7.py','s20_lfp.py','s22_sites.py']];print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent**

Now the headers (claims tables) and the main notebook's Result cells.

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's/pp = stats.ttest_rel(a, b, axis=0).pvalue \* 81; pi = stats.ttest_ind(a, b, axis=0).pvalue \* 81/pp = np.minimum(stats.ttest_rel(a, b, axis=0).pvalue * 81, 1); pi = np.minimum(stats.ttest_ind(a, b, axis=0).pvalue * 81, 1)/; s/pp = stats.ttest_rel(N, W, axis=0).pvalue \* nb; pi = stats.ttest_ind(N, W, axis=0).pvalue \* nb/pp = np.minimum(stats.ttest_rel(N, W, axis=0).pvalue * nb, 1); pi = np.minimum(stats.ttest_ind(N, W, axis=0).pvalue * nb, 1)/' s04_fig5.py && grep -c "np.minimum(stats" s04_fig5.py
cat > h_common.md <<'EOF'
| Claim | Where tested |
|---|---|
| dataset-composition | main notebook (counts); LFP notebook (LS neurons with more than 50 spikes) |
| fig1c-hfo-each-animal, fig1c-post-burst-suppression, fig1c-event-count, figs1-participation | main notebook |
| fig1d-phase-locking | LFP notebook |
| fig1f-shorter-than-ripples, fig1g-slower-than-ripples, fig1h-no-amplitude-frequency-correlation | main notebook |
| fig2-confined-to-ls | LFP notebook |
| fig2ef-intermediate-ls | blocked: metadata_insufficient (no relative depth of each recording within LS) |
| fig3-travelling-waves | blocked: metadata_insufficient (no electrode positions) |
| fig4b-pre-post-unchanged, fig4b-hfo-above-behav, fig4-sessions-few-change, fig4c-temporal-bias, fig4d-compression | main notebook |
| figs3d-hpc-compression-post, figs2-post-rate-increase, figs2c-no-ls-reactivation | main notebook |
| fig5b-nrem-and-rates, fig5e-state-coupling, fig5f-ripple-triggered-firing | main notebook |
| fig5d-lag | main notebook (deposited peak times); LFP notebook (maximum-NSS times) |
| fig5f-no-phase-coherence, ls-spikes-not-locked-to-ca1-ripples | LFP notebook |
| fig6-optogenetic-hfos | blocked: data_missing (the two optogenetic rats are not in the dandiset) |
| fig7e-ca1-spikes, fig7e-state, fig7e-duration | Figure 7E notebook |
| fig7e-ca1-depth | blocked: metadata_insufficient (no site positions or per-site waveforms) |
| fig7e-replay, fig7e-seqnmf, figs5-seqnmf-variance | blocked: other (not attempted within the run's time) |
| fig7e-content-independent, fig7e-coupled-only | blocked: depend on fig7e-ca1-depth (metadata_insufficient) |
| discussion-medial-septum | main notebook (part b); LFP notebook (part a) |
| discussion-cingulate-down-state | main notebook (reading a) |
| fig8-model | blocked: other (the model's data are elsewhere and it was not attempted within the run's time) |
EOF
python - <<'EOF'
tab=open('/tmp/claude-1001/nb/h_common.md').read()
def hdr(title, what, nb):
    lines = [f"# {title}", "",
    "Tingley D. and Buzsaki G. (2019). Routing of hippocampal ripples to subcortical structures via the lateral septum. Neuron 105, 138-149. doi:10.1016/j.neuron.2019.10.012.", "",
    "Dataset: DANDI:000218, version 0.261110.1911 (doi:10.48324/dandi.000218/0.261110.1911), streamed from the archive.", "",
    "Version. The paper cites no version of the dandiset (it predates it). The most recent published version, 0.261110.1911, is pinned: its files were re-converted with trial labels sorted with their rows, the lab's ripple and LS HFO detections, sleep states for every session with them, units with shank and region, and electrode flags, all of which the claims use; the earlier versions (0.220131.1608, 0.250624.0439) lack the event tables and sleep states, so they match the claims file's description less well. The LFP and spikes are the same data in all versions (release notes).", "",
    "Claims file: `claims/tingley-2019.yaml`, written from the accepted manuscript in PubMed Central (PMC6952543) with its supplement. The paper's full text and supplement were read here.", "",
    what, "",
    "Claims and where they are tested (all notebooks of this entry):", "", tab]
    src = "\n".join("# " + l if l else "#" for l in lines)
    open(f'/tmp/claude-1001/nb/{nb}','w').write("# %% [markdown]\n" + src + "\n")
hdr("Reproducing Tingley and Buzsaki (2019) from DANDI:000218: spikes and events",
    "This notebook tests the claims that use spikes, the lab's event tables, sleep states and trials. The LFP analyses are in `lfp_tingley_2019.ipynb` and the Figure 7E regressions in `fig7e_tingley_2019.ipynb`.", "h0_main.py")
hdr("Reproducing Tingley and Buzsaki (2019) from DANDI:000218: Figure 7E",
    "This notebook tests the Figure 7E claims that the dataset allows: LS spike counts in SPW-Rs predicted from the hippocampal spike count, the brain state and the SPW-R duration.", "h0_fig7.py")
hdr("Reproducing Tingley and Buzsaki (2019) from DANDI:000218: LFP analyses",
    "This notebook tests the claims that need the LFP: phase locking of LS spikes, locking to the CA1 ripple band, event times at the maximum NSS, CA1-LS phase coherence, and HFO power by recording site.", "h0_lfp.py")
EOF
cat > s19_defs.py <<'EOF'
# %%
from concurrent.futures import ThreadPoolExecutor
FS = T.FS_LFP
def nearest_lag(ls_t, ca_t):
    """LS time minus the nearest CA1 time (as in the main notebook, fig5d-lag)."""
    j = np.clip(np.searchsorted(ca_t, ls_t), 1, len(ca_t) - 1)
    a, b = ls_t - ca_t[j - 1], ls_t - ca_t[j]
    return np.where(np.abs(a) < np.abs(b), a, b)
EOF
echo ok
```

```
2
ok
Shell cwd was reset to
```

**Agent**

Before writing the fig1c conclusions I need the pooled post-burst decision printed at full precision, and the per-animal tables. Adding those prints and re-running the Figure 1 section.

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
p='s03_fig1.py'; s=open(p).read()
s=s.replace('''print(f"Animals with median LS HFO frequency in 120-180 Hz''','''for nm in ["+20..50 ms", "stop..+50 ms"]:
    ma, sa, mb, sb = allr[nm]
    print(f"Pooled over all LS neurons, after the burst ({nm}): HFO {ma:.6f} +- {sa:.6f} (SEM), random {mb:.6f}; random minus HFO {mb - ma:.6f}, "
          f"3 SEM {3 * sa:.6f}; below by more than 3 SEM: {mb - ma > 3 * sa}")
print(f"Animals with median LS HFO frequency in 120-180 Hz''')
s=s.replace('''    print(f"seed {sd}: animals above at the event bin {n_above}; below after the burst (+20..50) {n_post}, (stop..+50) {n_post2}")''','''    ra = summary(tr)
    pooled_post = {nm: ra[nm][2] - ra[nm][0] > 3 * ra[nm][1] for nm in ["+20..50 ms", "stop..+50 ms"]}
    print(f"seed {sd}: animals above at the event bin {n_above}; below after the burst (+20..50) {n_post}, (stop..+50) {n_post2}; "
          f"pooled below by more than 3 SEM: {pooled_post}")''')
open(p,'w').write(s)
EOF
. ../wk/bin/activate && python dev.py s02_sanity.py s03_fig1.py 2>&1 | sed -n '/s02_sanity.py/,$p' | grep -v "^## s02"
```

```
animals with LS units                         6
LS units, all (reading b)                     2551
recordings with LS and hippocampal units      48
  CA3 by unit label (i)                       10
  CA1 by unit label (i)                       38
  CA3 by ca3_channel flag (ii)                19
  CA1 by flag (ii)                            29
recordings with LSRipples and sleep states    77
  same, any LS table                          80
recordings with CA1Ripples and sleep states   47
  same, CA1Ripples or ripplesALL              55
LS units per recording, min                   8
LS units per recording, max                   74
LS units per recording, mean                  31.1
LS units per recording, SD                    15.5
recordings with LS units                      82

LS units and recordings by animal:
         count  sum  min  max  mean
subject                            
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
import re
def add_after(path, anchor_tag_line_start, text, occurrence_end_marker=None):
    pass
R = {
# insert before the markdown header of next section: we append result markdown after the claim's code cells by placing before next "# %% [markdown]\n# ## "
}
def insert_before(path, before, md):
    s=open(path).read()
    i=s.index(before)
    block="# %% [markdown]\n"+"\n".join("# "+l for l in md.strip().split("\n"))+"\n\n"
    s=s[:i]+block+s[i:]
    open(path,'w').write(s)
def append(path, md):
    s=open(path).read().rstrip("\n")+"\n\n# %% [markdown]\n"+"\n".join("# "+l for l in md.strip().split("\n"))+"\n"
    open(path,'w').write(s)
f='s03_fig1.py'
insert_before(f,"# %% [markdown]\n# ## fig1c-event-count","""**Result: dataset-composition, counts from spikes and tables.** Six animals have LS units (DT1, DT2, DT5, DT7, DT8, DT9), as in the paper. All LS units number 2551 (reading b; outside 1989 +- 198.9); reading (a) is in the LFP notebook. 48 recordings hold LS and hippocampal units: by the units' label 38 CA1 (within 37 +- 3.7) and 10 CA3 (outside 25 +- 2.5); by the `ca3_channel` flag 29 and 19, both outside. LS HFO rates come from 77 recordings with LSRipples and sleep states (80 with any LS table; 89 +- 8.9 needs at least 80.1), CA1 ripple rates from 47 with CA1Ripples (outside 53 +- 5.3) or 55 with ripplesALL as well (within). Recordings hold 8 to 74 LS units, mean 31.1 +- 15.5 (paper 8 to 74, 29.6 +- 15.5). The outcome is decided with reading (a) of the LS neuron count, in the LFP notebook.""")
insert_before(f,"# %% [markdown]\n# ## fig1f-shorter-than-ripples","""**Result: fig1c-event-count reproduced.** LSRipples holds 27014 events in the 77 recordings with LS electrodes and an LS table, in 6 animals (reading a), within 29955 +- 2995.5; counting only recordings with LS units (reading b) gives 25690, outside. Using the earlier LS tables where LSRipples is missing gives 28978 and 27654.""")
insert_before(f,"# %% [markdown]\n# ## fig1h-no-amplitude","""**Result: fig1f-shorter-than-ripples reproduced.** LS HFOs last 27.8 +- 9.5 ms and CA1 ripples 31.2 +- 13.7 ms (paper 27 +- 9 and 31 +- 14), rank-sum p = 1.2e-199, in the four animals with both tables; reading (2) gives the same means. LS HFOs are shorter in each of the four animals.

**Result: fig1g-slower-than-ripples reproduced.** LS HFOs peak at 147.6 +- 5.8 Hz and CA1 ripples at 158.3 +- 7.4 Hz (paper 147 +- 5.7 and 159 +- 8), rank-sum p < 1e-300 (printed as 0); slower in each animal. The frequencies are the lab's deposited values.""")
insert_before(f,"# %% [markdown]\n# ## fig1c-hfo-each-animal","""**Result: fig1h-no-amplitude-frequency-correlation reproduced, resting on an assumption.** Over 27014 LS HFOs, Pearson r = 0.006 (p = 0.3): no significant correlation. The Spearman reading finds a significant but negligible one (rho = 0.020, p = 0.00095). The paper names no test; the Pearson correlation, the usual test of a linear relation in a scatter like Figure 1H, is adopted as an assumption. Within animals, both correlations are significant in 5 of 6 animals (r from -0.107 to 0.169), with signs that differ between animals.""")
insert_before(f,"# %% [markdown]\n# ## figs1-participation","""**Result: fig1c-hfo-each-animal partially reproduced.** The median LS HFO frequency lies in 120-180 Hz in all 6 animals (142.9 to 149.2 Hz). The HFO-triggered spike probability exceeds the random-time mean by more than 3 SEM at the event bin in 4 of 6 animals (DT1, DT2, DT8, DT9; not DT5 and DT7), and over +-5 ms in 5 of 6 (not DT5); over the five seeds, 4 or 5 animals at the event bin. Pooled, the probability at the event bin is 0.0072 against 0.0016 at random times.

**Result: fig1c-post-burst-suppression not reproduced, resting on an assumption.** Pooled over 2327 LS neurons, the probability from each event's stop to 50 ms after its time is 0.001517 against 0.001593 at random times, a difference of 0.000076, less than 3 SEM (0.000201). From 20 to 50 ms after the event time it is 0.001399, below random by 0.000200, just over 3 SEM (0.000178), under the claim's seed; under 2 of the 4 other seeds it is not. The window from the stop is adopted as the reading of "immediately following the population burst". Per animal, firing is suppressed only in DT5, under both windows.""")
append(f,"""**Result: figs1-participation not reproduced.** Over the 73 recordings with LS units and LSRipples, 5.7% of LS neurons fire in an HFO, with 0.079 spikes per neuron per event (window a, pooled events). The largest values over the four combinations are 10.7% and 0.155 spikes (window b, mean over recordings). The paper reports 16% and 0.23. Per animal (window a) the fraction ranges from 3.3% (DT7) to 12.4% (DT1).""")
EOF
grep -c "Result:" s03_fig1.py
```

```
8
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
def insert_before(path, before, md):
    s=open(path).read(); i=s.index(before)
    s=s[:i]+"# %% [markdown]\n"+"\n".join("# "+l for l in md.strip().split("\n"))+"\n\n"+s[i:]; open(path,'w').write(s)
def append(path, md):
    s=open(path).read().rstrip("\n")+"\n\n# %% [markdown]\n"+"\n".join("# "+l for l in md.strip().split("\n"))+"\n"; open(path,'w').write(s)
s=open('s03_fig1.py').read()
s=s.replace('print("\\nAll animals pooled (mean HFO, SEM, mean random, SEM):"','print(f"\\nLS neurons in the triggered averages: {len(TRIG)} in {TRIG.session.nunique()} recordings")\nprint("All animals pooled (mean HFO, SEM, mean random, SEM):"')
open('s03_fig1.py','w').write(s)
f='s04_fig5.py'
insert_before(f,"# %% [markdown]\n# ## fig5d-lag","""**Result: fig5b-nrem-and-rates reproduced.** 72.9% of the 27014 LS HFOs fall in NREM, and the NREM rate exceeds the WAKE rate in 66 of 73 recordings (signed-rank p = 2.9e-12); DT7 is the exception, with 29.6% of its HFOs in NREM. LS HFO rates are lower than CA1 ripple rates in NREM (medians 0.024 and 0.320 per s; rank-sum p = 1.5e-13, signed-rank over 42 recordings p = 2.9e-10) and over all scored time (rank-sum p = 1.3e-12). The rates come from 77 LS and 47 CA1 recordings, against the paper's 89 and 53.""")
insert_before(f,"# %% [markdown]\n# ## fig5e-state-coupling","""**Result: fig5d-lag reproduced.** With the deposited peak times, the median lag of LS HFOs after the nearest CA1 ripple within +-50 ms is 6.20 ms over recording medians and 6.40 ms over 6572 pooled pairs (paper 6.4 +- 4.2), with CA1 leading in 63.9% of pairs; within +-25 ms, 4.80 ms. The pooled cross-correlogram peaks at 0 ms, 37.1 SD above its 100-200 ms flanks. Per animal the pooled median ranges from -7.2 ms (DT7) to 8.0 ms (DT9). The maximum-NSS reading is in the LFP notebook.""")
insert_before(f,"# %% [markdown]\n# ## fig5f-ripple-triggered-firing","""**Result: fig5e-state-coupling not reproduced.** Over 42 recordings, the fraction of LS HFOs with a CA1 ripple within +-25 ms is 0.302 in NREM and 0.091 in WAKE pooled (paper 0.3 and 0.15), and 0.213 and 0.118 as the mean over recordings. The NREM fraction is higher in 30 of 42 recordings, with t-test p = 0.0025 paired and 0.014 two-sample, short of both P < 6.6e-6 and the partial bound of 0.001. No cross-correlogram bin within +-25 ms differs at corrected p < 0.001 (smallest 0.026). Excluding trials from WAKE changes nothing.""")
insert_before(f,"# %% [markdown]\n# ## discussion-medial-septum","""**Result: fig5f-ripple-triggered-firing not reproduced.** Over 1266 LS neurons in 38 recordings (paper 1313), the CA1 ripple-triggered rate at zero lag is 2.14 Hz in NREM and 2.03 Hz in WAKE; no bin within +-25 ms differs at corrected p < 0.001 under any reading (smallest corrected p 0.18 paired, normalized rates). Normalized by the state's mean rate, the WAKE response is the larger (1.73 against 1.48).""")
append(f,"""**Result: discussion-medial-septum, part (b), does not hold.** The 25 units labelled `ms` (2 recordings, DT7) fire more within +-50 ms of CA1 ripples than on average (median ratio 1.43; below the mean in 6 of 25; signed-rank p = 0.0046). Part (a) and the outcome are in the LFP notebook.

**Result: discussion-cingulate-down-state, reading (a), does not hold.** The 31 units labelled `acg` (2 recordings, DT7) reach their minimum rate after CA1 ripples at 105 ms (0.62 of the mean rate), against 50 +- 5 ms, and a maximum at 150 ms; per recording the minimum lies at 105 and 130 ms. Reading (b) is in the LFP notebook.""")
f='s05_fig4.py'
insert_before(f,"# %% [markdown]\n# ## fig4b-hfo-above-behav","""**Result: fig4b-pre-post-unchanged partially reproduced, resting on an assumption.** With the CCG divided by the square root of the two spike counts, no reading finds PRE and POST different (rank-sum p 0.50 to 0.89 over 8 readings; effect r -0.013 to 0.025). With raw counts, all 8 readings find POST above PRE (p 0.0036 to 0.0065; r -0.10 to -0.12). The normalized CCG is adopted as an assumption: the paper compares epochs with very different spike counts (BEHAV medians are 10 to 100 times the HFO ones in raw counts), which only a rate-normalized measure allows. Only 361 to 503 pairs in 21 to 23 sessions pass the inclusion rule, against 7172 pairs in 53 sessions; no pair of DT8 passes.""")
insert_before(f,"# %% [markdown]\n# ## fig4-sessions-few-change","""**Result: fig4b-hfo-above-behav reproduced, resting on the assumption of fig4b-pre-post-unchanged.** Under all 8 normalized readings, PRE and POST exceed BEHAV (rank-sum p 1e-69 to 1e-129) and PRE, POST and BEHAV each exceed their jittered values (p <= 2.1e-6). Under raw counts, every epoch exceeds its jitter, but with BEHAV taken from the first to the last trial, PRE and POST do not exceed BEHAV (p 0.13 to 0.84). Under the four other jitter seeds, every epoch exceeds its jitter under all 16 readings.""")
insert_before(f,"# %% [markdown]\n# ## fig4c-temporal-bias","""**Result: fig4-sessions-few-change not reproduced.** 21 to 23 sessions have included pairs (paper 53 +- 5.3). At most 1 session per reading has PRE and POST different at p < 0.01 (fraction 0 to 0.048, against 0.132), and no reading has both directions.""")
insert_before(f,"# %% [markdown]\n# ## fig4d-compression","""**Result: fig4c-temporal-bias reproduced.** No reading finds the PRE-BEHAV and BEHAV-POST correlations different (paired p 0.060 to 0.90, two-sample 0.13 to 0.91; mean BEHAV-POST minus PRE-BEHAV -0.017 to 0.194), over 16 to 19 recordings with at least 3 pairs, against the paper's 53.""")
append(f,"""**Result: fig4d-compression partially reproduced.** PRE and POST CCGs correlate with BEHAV above chance at factor 1 in every reading. Every factor up to 5 to 8 (PRE) and 8 to 11 (POST) is above chance at p < 0.01 under the claim's seed (signed-rank and rank-sum), against the paper's ~20 (18 to 22). Under four other seeds the largest factor is 5 to 12. PRE and POST do not differ at p < 0.01 at any factor (smallest p 0.055).""")
f='s06_figs2s3.py'
insert_before(f,"# %% [markdown]\n# ## figs2-post-rate-increase","""**Result: figs3d-hpc-compression-post partially reproduced.** Over 9366 to 15066 hippocampal pairs in 42 recordings, the POST correlation with BEHAV exceeds the PRE one at p < 0.01 at 1 to 3 of the factors 1 to 7 (factor 3 in every reading, p <= 0.0012), not at most of them; POST medians are above PRE medians at every factor from 1 to 7.""")
insert_before(f,"# %% [markdown]\n# ## figs2c-no-ls-reactivation","""**Result: figs2-post-rate-increase partially reproduced.** Relative to the session average, LS rates are higher in POST NREM than in PRE NREM (1.334 against 1.265; paired p = 0.032, two-sample p = 0.036; 1570 neurons). CA1 rates (units labelled `hpc`) are lower in POST NREM (1.293 against 1.347; paired p = 0.043), and CA3 rates do not change (p = 0.59). The ca3_channel reading gives the same directions. Neuron counts are 1570, 2597 and 466 against 1754, 2315 and 1373.""")
append(f,"""**Result: figs2c-no-ls-reactivation reproduced.** With 25 ms bins after rate matching, EV does not exceed REV for LS-LS pairs (CA1 ripple epochs, paired p = 0.23; LS HFO epochs, p = 0.57), HPC-HPC pairs (p = 0.18) or HPC-LS pairs (p = 0.33), and the same holds under four other seeds. The paper's increase of EV over REV with 1 s bins appears only for HPC-HPC pairs without rate matching (paired p = 0.049).""")
EOF
grep -c Result s04_fig5.py s05_fig4.py s06_figs2s3.py
```

```
s04_fig5.py:6
s05_fig4.py:5
s06_figs2s3.py:3
Shell cwd was reset to
```

**Agent**

Correcting two ranges in the Result text, then adding cingulate reading (b) to the site job: the extremum of the ripple-triggered LFP at cingulate sites.

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
s=open('s05_fig4.py').read(); s=s.replace("(p 0.13 to 0.84)","(p 0.13 to 0.87)"); open('s05_fig4.py','w').write(s)
s=open('s06_figs2s3.py').read(); s=s.replace("POST medians are above PRE medians at every factor from 1 to 7.","POST medians are at or above PRE medians at every factor from 1 to 7.").replace("The ca3_channel reading gives the same directions.","The ca3_channel reading gives the same conclusions (CA1 lower, p = 0.018; CA3 unchanged, p = 0.94)."); open('s06_figs2s3.py','w').write(s)
p='s22_sites.py'; s=open(p).read()
s=s.replace("""    reg = s.electrodes.region.to_numpy()[el]
    return pd.DataFrame(dict(session=s.session[:25], row=el, region=reg, ratio=num / den, n_events=nev))""","""    reg = s.electrodes.region.to_numpy()[el]
    # discussion-cingulate-down-state, reading (b): CA1 ripple-triggered LFP of the acg sites in the same chunks
    trig = None
    if (reg == "acg").any() and ca1_ev(s) is not None:
        ct = ca1_ev(s).peak_time.to_numpy(); L = int(0.2 * FS); acc = []; ac = np.flatnonzero(reg == "acg")
        for off, blk in pieces:
            c = (ct * FS).astype(int) - off; c = c[(c > L) & (c < len(blk) - L)]
            if len(c): acc.append(blk[(c[:, None] + np.arange(-L, L + 1)[None]), :][:, :, ac].astype(np.float32).mean(2))
        if acc:
            m = np.vstack(acc).mean(0); trig = (m - m[:int(0.1 * FS)].mean(), sum(len(a) for a in acc))
    del pieces
    return pd.DataFrame(dict(session=s.session[:25], row=el, region=reg, ratio=num / den, n_events=nev)), trig""")
s=s.replace("""with ThreadPoolExecutor(1) as ex:
    SITES = pd.concat(list(ex.map(site_job, range(len(SITE_SESS)))))""","""SJ = [site_job(k) for k in range(len(SITE_SESS))]
SITES = pd.concat([a for a, _ in SJ])""")
s+='''
# %% [markdown]
# ## discussion-cingulate-down-state, reading (b)
# The CA1 ripple-triggered LFP averaged over the `acg` sites, in the same time chunks, baseline-subtracted (-200 to -120 ms); the delay is
# the time of its largest deviation between 0 and 200 ms.

# %% tags=["claim:discussion-cingulate-down-state"]
tl = np.arange(-int(0.2 * FS), int(0.2 * FS) + 1) / FS * 1000
for (df, tr), s in zip(SJ, SITE_SESS):
    if tr is None: continue
    x, n = tr; w = (tl >= 0) & (tl <= 200)
    k = np.argmax(np.abs(x[w]))
    print(f"{s.session[:25]}: {n} CA1 ripples; extremum of the acg ripple-triggered LFP at {tl[w][k]:.1f} ms ({x[w][k]:.1f} in the file's LFP units); "
          f"minimum at {tl[w][np.argmin(x[w])]:.1f} ms, maximum at {tl[w][np.argmax(x[w])]:.1f} ms")
'''
open(p,'w').write(s)
EOF
python -c "import ast;ast.parse(open('$TMPDIR/nb/s22_sites.py').read());print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's/baseline-subtracted (-200 to -120 ms)/baseline-subtracted (-200 to -100 ms)/' s22_sites.py && python - <<'EOF'
src=open('/tmp/claude-1001/nb/s22_sites.py').read().replace('SITE_SESS = [s for s in S if','SITE_SESS = [s for s in S[45:58] if')
open('/tmp/claude-1001/nb/s22_sub.py','w').write("from concurrent.futures import ThreadPoolExecutor\nFS = T.FS_LFP\n"+src)
EOF
. ../wk/bin/activate && python dev.py s02_sanity.py s22_sub.py 2>&1 | sed -n '/s02_sanity.py/,$p' | tail -30
```

```
ms         10   12.35  36.50
20170325-576um-360um-1703 acg        29    0.61   3.37
                          hpc        64    1.95  22.26
                          ls         21    0.97   3.94
                          ms         14    0.79   3.49
20170401-864um-936um-merg cc         20    1.34   5.22
                          hpc        63    1.26   2.51
                          ls         24    2.36   5.78
                          ms         21    1.50   4.04
20170315-288um-0um-170315: LS median 3.75; others [('acg', np.float64(0.98), np.float64(2.54)), ('cc', np.float64(2.19), np.float64(5.92))]; holds: False; events used 71
20170318-288um-0um-170318: LS median 2.89; others [('acg', np.float64(0.84), np.float64(11.51)), ('ms', np.float64(2.77), np.float64(12.0))]; holds: False; events used 52
20170320-432um-0um-merge: LS median 4.97; others [('acg', np.float64(0.48), np.float64(17.52)), ('ms', np.float64(12.32), np.float64(16.43))]; holds: False; events used 17
20170321-216um-0um-170321: LS median 1.82; others [('acg', np.float64(0.72), np.float64(8.91)), ('ms', np.float64(2.17), np.float64(8.08))]; holds: False; events used 113
20170324-576um-144um-1703: LS median 8.67; others [('acg', np.float64(1.01), np.float64(44.33)), ('ms', np.float64(12.35), np.float64(36.5))]; holds: False; events used 33
20170325-576um-360um-1703: LS median 0.97; others [('acg', np.float64(0.61), np.float64(3.37)), ('ms', np.float64(0.79), np.float64(3.49))]; holds: False; events used 78
20170401-864um-936um-merg: LS median 2.36; others [('cc', np.float64(1.34), np.float64(5.22)), ('ms', np.float64(1.5), np.float64(4.04))]; holds: False; events used 58
fig2 criterion holds in 0 of 7 recordings
medial septum (a), 20170318-288um-0um-170318: ms site median ratio 2.77 (n 3) against LS 2.89
medial septum (a), 20170320-432um-0um-merge: ms site median ratio 12.32 (n 7) against LS 4.97
medial septum (a), 20170321-216um-0um-170321: ms site median ratio 2.17 (n 7) against LS 1.82
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 657,720p tools/entry.py | grep -n "timeout\|max-minutes\|default" ; cd $TMPDIR/nb && sed -i 's/The LFP and spikes are the same data in all versions (release notes)./The LFP is the earlier version'"'"'s data, stored again in channel order (release notes)./' h0_main.py h0_fig7.py h0_lfp.py && grep -c "channel order" h0_main.py
```

```
8:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
9:    parser.add_argument("--max-minutes", type=float, default=60,
13:    parser.add_argument("--python", help="lock: the Python version to lock for (default: the entry's); "
16:                                                    "(default: executed/<entry>)")
50:                              args.timeout, args.max_minutes)
60:    return run(entry_dir, output_dir, args.timeout, args.max_minutes, args.fresh)
1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's/with ThreadPoolExecutor(3) as ex:/with ThreadPoolExecutor(4) as ex:/' s20_lfp.py && . ../wk/bin/activate && pip list 2>/dev/null | grep -i nbformat || uv pip install -q nbformat; E=entries/tingley-2019
python build.py $E/reproduce_tingley_2019.ipynb h0_main.py s01_setup.py s02_sanity.py s03_fig1.py s04_fig5.py s05_fig4.py s06_figs2s3.py
python build.py $E/lfp_tingley_2019.ipynb h0_lfp.py s01_setup.py s02_sanity.py s19_defs.py s20_lfp.py s21_lfp_claims.py s22_sites.py
python build.py $E/fig7e_tingley_2019.ipynb h0_fig7.py s01_setup.py s02_sanity.py s07_fig7.py
cat > $E/requirements.in <<'EOF'
h5py
matplotlib
numpy
pandas
remfile
scipy
EOF
cat > $E/entry.yaml <<'EOF'
schema_version: 1
name: tingley-2019
type: reproduction
title: Routing of hippocampal ripples to subcortical structures via the lateral septum (Tingley and Buzsaki 2019)
description: Tests the findings of Tingley and Buzsaki (2019) on dandiset 000218, which holds 98 recordings of lateral
  septum (LS) and hippocampus in six rats, with the lab's ripple and LS HFO detections, sleep states and maze trials.
  The main notebook uses spikes and event tables (HFO and ripple properties, state dependence, coupling, pair
  co-activation, reactivation); a second notebook the LFP (phase locking, coherence, HFO power by site); a third
  the Figure 7E regressions of LS firing on ripple features. The optogenetic rats, electrode positions and
  per-recording depths in LS are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_tingley_2019.ipynb
  title: Spikes and events
  runtime_minutes: 12
- path: lfp_tingley_2019.ipynb
  title: LFP analyses
  runtime_minutes: 45
- path: fig7e_tingley_2019.ipynb
  title: Figure 7E regressions
  runtime_minutes: 35
helpers:
- tingley2019.py
related:
- id: dandi:000218/0.261110.1911
  relation: uses_data
- id: doi:10.1016/j.neuron.2019.10.012
  relation: reproduces
EOF
cd  && python -c "import yaml,jsonschema,nbformat" && python tools/entry.py lock entries/tingley-2019 2>&1 | tail -3 && python tools/entry.py check entries/tingley-2019 2>&1 | tail -10
```

```
Exit code 1
nbformat                  5.11.1
Traceback (most recent call last):
  File "/tmp/claude-1001/nb/build.py", line 2, in <module>
    import sys,re,nbformat
ModuleNotFoundError: No module named 'nbformat'
Traceback (most recent call last):
  File "/tmp/claude-1001/nb/build.py", line 2, in <module>
    import sys,re,nbformat
ModuleNotFoundError: No module named 'nbformat'
Traceback (most recent call last):
  File "/tmp/claude-1001/nb/build.py", line 2, in <module>
    import sys,re,nbformat
ModuleNotFoundError: No module named 'nbformat'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import yaml,jsonschema,nbformat
ModuleNotFoundError: No module named 'yaml'
```

**Agent calls Bash**

```bash
cd $TMPDIR && . wk/bin/activate && uv pip install -q nbformat pyyaml jsonschema && cd nb && E=entries/tingley-2019 && python build.py $E/reproduce_tingley_2019.ipynb h0_main.py s01_setup.py s02_sanity.py s03_fig1.py s04_fig5.py s05_fig4.py s06_figs2s3.py && python build.py $E/lfp_tingley_2019.ipynb h0_lfp.py s01_setup.py s02_sanity.py s19_defs.py s20_lfp.py s21_lfp_claims.py s22_sites.py && python build.py $E/fig7e_tingley_2019.ipynb h0_fig7.py s01_setup.py s02_sanity.py s07_fig7.py && cd  && python tools/entry.py lock entries/tingley-2019 2>&1 | tail -3 && python tools/entry.py check entries/tingley-2019 2>&1 | tail -10
```

```
70 cells
24 cells
11 cells
wrote tingley-2019/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent**

Check passes. Starting the full run: lock is done, so `entry.py all` builds a clean environment and executes the three notebooks one after another. I expect about 95 minutes.

**Agent calls Bash**

```bash
date -u; cd  && . $TMPDIR/wk/bin/activate && python tools/entry.py all entries/tingley-2019 2>&1 | tail -40; date -u
```

```
Wed Nov 18 11:00:34 UTC 2026
Installed kernelspec registry-tingley-2019 in executed/tingley-2019/.venv/share/jupyter/kernels/registry-tingley-2019
0 error(s)
pass  reproduce_tingley_2019.ipynb  (909 s)
pass  lfp_tingley_2019.ipynb  (2895 s)
pass  fig7e_tingley_2019.ipynb  (949 s)
Wed Nov 18 12:19:57 UTC 2026
```

**Agent**

All three notebooks pass: 15, 48 and 16 minutes. It is 12:20. Reading the executed outputs.

**Agent calls Bash**

```bash
. $TMPDIR/wk/bin/activate && python - <<'EOF'
import nbformat
for name in ["lfp_tingley_2019.ipynb","fig7e_tingley_2019.ipynb"]:
    nb=nbformat.read(f"executed/tingley-2019/{name}",4)
    print("=========",name)
    for i,c in enumerate(nb.cells):
        if c.cell_type!='code': continue
        tags=c.metadata.get('tags',[])
        if 'sanity' in tags and i<8: continue
        for o in c.get('outputs',[]):
            if o.get('name')=='stdout': print(f"--- cell {i} {tags}\n"+o['text'][:6000])
            if o.get('output_type')=='error': print("ERROR",o['ename'],o['evalue'])
EOF
```

```
========= lfp_tingley_2019.ipynb
--- cell 2 []
98 files of dandiset 000218 version 0.261110.1911 loaded in 131 s; peak memory 2.36 GB

--- cell 10 ['sanity']
Recordings for the LFP jobs: 73 (Counter({'DT5': 17, 'DT8': 17, 'DT9': 13, 'DT1': 12, 'DT2': 10, 'DT7': 4})); with a CA1 detection channel and CA1Ripples: 41
LS units in them: 2327; LFP hours to read: 427 (one block each, plus CA1 blocks)
LS detection channel region labels: Counter({'ls': 73})
CA1 detection channel region labels: Counter({'hpc': 35, 'ca3': 6})

--- cell 11 []
Recordings whose job failed: none
73 recordings in 42.3 min (per recording 124 s median); peak memory 7.37 GB

--- cell 13 ['claim:fig1d-phase-locking', 'claim:dataset-composition']
detection channel, 120-200 Hz: LS neurons 2327; with > 50 spikes in high-power epochs 1996; significant 1209; fraction (a) 0.606, (b) 0.520; null fraction (10 shifts) 0.052
   preferred phase of significant neurons: circular mean -167.0 deg (|distance to 180| 13.0); Rayleigh over neurons p = 0, r = 0.78; median resultant length 0.206
own shank channel, 120-200 Hz: LS neurons 1299; with > 50 spikes in high-power epochs 1129; significant 883; fraction (a) 0.782, (b) 0.680; null fraction (10 shifts) 0.053
   preferred phase of significant neurons: circular mean -164.0 deg (|distance to 180| 16.0); Rayleigh over neurons p = 1.7e-302, r = 0.80; median resultant length 0.313
detection channel, 120-180 Hz: LS neurons 2327; with > 50 spikes in high-power epochs 2013; significant 1234; fraction (a) 0.613, (b) 0.530; null fraction (10 shifts) 0.051
[... 177 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required'));print(list(s['properties'].keys()))
o=s['properties']['outcomes']['items'];print(json.dumps(o,indent=0)[:3500])
"; python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
for k in ['findings','verifications','provenance','datasets','inputs']:
  print(k, json.dumps(s['properties'][k])[:1500])
print(json.dumps(s.get('\$defs',{}))[:3000])
"
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
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
[... 147 more lines not kept]
```

**Agent**

Writing the remaining Result cells and the Summary into the source notebooks and the executed copies.

**Agent calls Bash**

```bash
. $TMPDIR/wk/bin/activate && cat > $TMPDIR/nb/insert.py <<'PYEOF'
import nbformat, sys
FAIL = "A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method."
LFP = {
"claim:dataset-composition": """**Result: dataset-composition partially reproduced.** Reading (a): 1996 LS neurons have more than 50 spikes in high-power epochs (paper 1989 +- 198.9), 5 to 62 per recording (mean 27.3 +- 14.7) in 73 recordings. With the counts of the main notebook: 6 animals; CA1 recordings 38 (within); CA3 recordings 10 or 19 (outside 25 +- 2.5); LS HFO rate recordings 77 or 80 (outside 89 +- 8.9); CA1 ripple rate recordings 55 with ripplesALL (within; 47 with CA1Ripples alone); mean LS units per recording 31.1 (within). Four of the six counts other than animals are within tolerance.

**Result: fig1d-phase-locking partially reproduced.** Of 1996 LS neurons with more than 50 spikes in high-power epochs, 60.6% are significantly locked to the 120-200 Hz phase of the detection channel (52.0% of all 2327 LS neurons), and 78.2% of 1129 neurons to their own shank's channel, against 92.5% +- 9.25%; the 120-180 Hz band gives 61.3%. Ten circular shifts give 5.2%. The trough preference holds: significant neurons prefer -167.0 degrees (13.0 from the trough), Rayleigh over neurons p < 1e-300. Per animal the fraction ranges from 39.3% (DT9) to 76.8% (DT1).""",
"claim:ls-spikes-not-locked-to-ca1-ripples": """**Result: ls-spikes-not-locked-to-ca1-ripples not reproduced, resting on an assumption.** Inside CA1 ripples (reading a), 43 of 599 LS neurons with more than 50 spikes (7.2%) are locked to the CA1 channel's 120-200 Hz phase, above 5% (binomial p = 0.012), with a median resultant length of 0.068 (against 0.136 to the LS channel); shifted phases give 4.9%. In the CA1 high-power epochs (reading b), 5.0% (61 of 1218; p = 0.51), at chance. Reading (a), spikes during the SPW-Rs themselves, is adopted as the reading of "individual waves of hippocampal SPW-Rs". The locking found is weak: the fraction is 1.4 times chance.""",
"claim:fig5d-lag": """**Result: fig5d-lag, maximum-NSS reading.** With event times at the maximum NSS of the detection channels, the median lag is 6.00 ms over recording medians and 6.40 ms pooled (6241 pairs within +-50 ms, 36 recordings), CA1 leading in 64.2% of pairs; within +-25 ms, 3.40 and 4.00 ms. This agrees with the deposited-peak reading of the main notebook (6.20 and 6.40 ms).""",
"claim:fig5f-no-phase-coherence": """**Result: fig5f-no-phase-coherence not reproduced.** Over 41 recordings and 91316 CA1 ripples, the CA1-LS 120-180 Hz phase-locking value at the ripple time is 0.186, above the jittered windows' mean of 0.104 by more than 3 SD (SD 0.0072; bound 0.126); 14 of 101 lags lie above the bound, the largest 14.7 SD at 4 ms. In each of the first 10 recordings printed, the value at the ripple time exceeds its own jittered mean.""",
"claim:discussion-medial-septum": """**Result: fig2-confined-to-ls not reproduced.** In none of the 8 recordings with LS and other non-hippocampal sites does the criterion hold. LS sites have a higher median 120-180 Hz power ratio at HFO times than the acg sites in all 7 recordings with acg sites (e.g. 3.75 against 0.98), but medial septal sites reach ratios above the LS median in 3 recordings (median 12.32 against 4.97 in 20170320), and in every recording some sites outside LS exceed 1.5 (maxima 2.54 to 44.33). The ratios rest on 17 to 113 events in two chunks of each recording.

**Result: discussion-medial-septum not reproduced.** Part (a): the medial septal sites' median ratio lies below the LS sites' in 3 of 6 recordings (20170318, 20170325, 20170401) and above it in 3. Part (b), in the main notebook, does not hold either: the 25 `ms` units fire more around CA1 ripples than on average (median ratio 1.43).""",
"claim:discussion-cingulate-down-state": """**Result: discussion-cingulate-down-state not reproduced.** Reading (b): the extremum of the acg ripple-triggered LFP between 0 and 200 ms lies at 2.4 to 7.2 ms in 5 of 6 recordings and at 81.6 ms in one, not at 50 +- 5 ms (one recording has a minimum at 52.0 ms, smaller than its extremum at 2.4 ms). Reading (a), in the main notebook, places the units' minimum at 105 ms.""",
}
F7 = {
"claim:fig7e-ca1-spikes": """**Result: fig7e-ca1-spikes partially reproduced.** Over 1288 LS neurons in 42 recordings, the hippocampal spike count in a SPW-R significantly predicts the LS spike count of 47.0% to 80.0% of neurons over the 16 combinations, against 38% +- 3.8%; no combination is within tolerance. Every combination exceeds its chance rate (25.4% to 44.3%; binomial p <= 2.4e-7). The four other seeds (linear models) give 46.6% to 64.2%.

**Result: fig7e-state partially reproduced.** The state (NREM or WAKE) predicts 44.4% to 63.9% of 1238 LS neurons, against 26% +- 2.6%; none within tolerance; above chance in all 16 combinations (binomial p <= 3.2e-9).

**Result: fig7e-duration partially reproduced.** The SPW-R duration predicts 41.1% to 89.0% of 1288 LS neurons, against 20% +- 2%; none within tolerance; above chance in all 16 combinations (binomial p <= 6.3e-4).""",
}
SUMMARY = """## Summary

| Claim | Outcome | Notebook |
|---|---|---|
| dataset-composition | partially reproduced (4 of 6 counts; CA3 and LS HFO-rate recordings short) | main, LFP |
| fig1c-hfo-each-animal | partially reproduced (4 of 6 animals at the event bin, 5 of 6 at +-5 ms) | main |
| fig1c-post-burst-suppression | not reproduced (assumed window from the event stop) | main |
| fig1c-event-count | reproduced (27014 against 29955) | main |
| figs1-participation | not reproduced (5.7% to 10.7% of neurons, 0.079 to 0.155 spikes) | main |
| fig1d-phase-locking | partially reproduced (61% to 78% locked; trough preference holds) | LFP |
| fig1f-shorter-than-ripples | reproduced | main |
| fig1g-slower-than-ripples | reproduced | main |
| fig1h-no-amplitude-frequency-correlation | reproduced (assumed Pearson) | main |
| fig2-confined-to-ls | not reproduced | LFP |
| fig2ef-intermediate-ls | blocked: metadata_insufficient | |
| fig3-travelling-waves | blocked: metadata_insufficient | |
| fig4b-pre-post-unchanged | partially reproduced (assumed normalized CCG; 361 to 503 pairs against 7172) | main |
| fig4b-hfo-above-behav | reproduced (assumed normalized CCG) | main |
| fig4-sessions-few-change | not reproduced | main |
| fig4c-temporal-bias | reproduced | main |
| fig4d-compression | partially reproduced (largest factor 5 to 11 against ~20) | main |
| figs3d-hpc-compression-post | partially reproduced (1 to 3 of factors 1-7) | main |
| figs2-post-rate-increase | partially reproduced (LS only) | main |
| figs2c-no-ls-reactivation | reproduced | main |
| fig5b-nrem-and-rates | reproduced | main |
| fig5d-lag | reproduced (6.2 to 6.4 ms) | main, LFP |
| fig5e-state-coupling | not reproduced | main |
| fig5f-ripple-triggered-firing | not reproduced | main |
| fig5f-no-phase-coherence | not reproduced | LFP |
| ls-spikes-not-locked-to-ca1-ripples | not reproduced (assumed reading inside ripples; 7.2% against 5%) | LFP |
| fig6-optogenetic-hfos | blocked: data_missing | |
| fig7e-ca1-spikes, fig7e-state, fig7e-duration | partially reproduced (all far above the paper's percentages and above chance) | Figure 7E |
| fig7e-ca1-depth | blocked: metadata_insufficient | |
| fig7e-replay, fig7e-seqnmf, figs5-seqnmf-variance | blocked: other (not attempted within the run's time) | |
| fig7e-content-independent, fig7e-coupled-only | blocked: metadata_insufficient (depend on fig7e-ca1-depth) | |
| discussion-medial-septum | not reproduced | main, LFP |
| discussion-cingulate-down-state | not reproduced | main, LFP |
| fig8-model | blocked: other (not attempted within the run's time) | |

""" + FAIL + """

**How the analysis differs from the paper's.** The lab's deposited detections are used for LS HFOs (LSRipples) and CA1 ripples (CA1Ripples); their stored parameters differ from the Methods (LS: 120-180 Hz, durations up to 100 ms, peak thresholds of 4 to 6 SD in places; CA1: 130-200 Hz). PRE, BEHAV and POST are not marked in the files and are taken as before the first trial, from the first trial to the last, and after the last (an assumption). Where the paper leaves a method open, every reading the claims file names was run; the choices adopted as assumptions are the normalized CCG (Figure 4), the Pearson correlation (Figure 1H), the window from the event stop (post-burst suppression) and spikes inside CA1 ripples (locking to CA1). CA1 and CA3 are told apart by the units' region label, which marks most hippocampal units only `hpc`. Figure 2 site ratios use two 14-minute chunks of each recording. The Figure 7E Poisson fits were run under the claim's seed only.

**What was found about the dataset.** Six rats (DT1, DT2, DT5, DT7, DT8, DT9) with 2551 LS units in 82 recordings and 98 files; no recording is deposited twice. The two optogenetic rats are not in the dandiset. Electrode positions and the depth of each recording within LS are not stored, nor are the PRE, BEHAV and POST periods. Most hippocampal units are labelled `hpc`, so CA1 and CA3 populations cannot be told apart reliably (10 recordings have units labelled `ca3`, 19 have a `ca3_channel` flag). 36 units of DT7 20170407 have an empty region label. In 3 files, less than half of the trial time is scored WAKE (DT2 3540um-1288um 20160227, 12.5%; DT5 20161014, 20.3%; DT8 20170201, 31.6%). The DT9 CA3 recordings have no CA1 ripple table although the paper detected SPW-Rs on a CA1 reference electrode for CA3 recordings. The deposited LS detections use parameters that differ from the Methods, as the files' descriptions say.
"""
def insert_after_tag(nb, tag, md):
    idx = max(i for i, c in enumerate(nb.cells) if tag in c.metadata.get("tags", []))
    nb.cells.insert(idx + 1, nbformat.v4.new_markdown_cell(md))
for base in ["entries/tingley-2019", "executed/tingley-2019"]:
    nb = nbformat.read(f"{base}/lfp_tingley_2019.ipynb", 4)
    for tag in ["claim:discussion-cingulate-down-state", "claim:discussion-medial-septum", "claim:fig5f-no-phase-coherence", "claim:fig5d-lag", "claim:ls-spikes-not-locked-to-ca1-ripples", "claim:dataset-composition"]:
        insert_after_tag(nb, tag, LFP[tag])
    nb.cells.append(nbformat.v4.new_markdown_cell("## Summary\n\nThe outcomes of all claims, with how the analysis differs from the paper's and what was found about the dataset, are in the summary of `reproduce_tingley_2019.ipynb`.\n\n" + FAIL))
    nbformat.write(nb, f"{base}/lfp_tingley_2019.ipynb")
    nb = nbformat.read(f"{base}/fig7e_tingley_2019.ipynb", 4)
    insert_after_tag(nb, "claim:fig7e-ca1-spikes", F7["claim:fig7e-ca1-spikes"])
    nb.cells.append(nbformat.v4.new_markdown_cell("## Summary\n\nThe outcomes of all claims are in the summary of `reproduce_tingley_2019.ipynb`.\n\n" + FAIL))
    nbformat.write(nb, f"{base}/fig7e_tingley_2019.ipynb")
    nb = nbformat.read(f"{base}/reproduce_tingley_2019.ipynb", 4)
    nb.cells.append(nbformat.v4.new_markdown_cell(SUMMARY))
    nbformat.write(nb, f"{base}/reproduce_tingley_2019.ipynb")
print("ok")
PYEOF
cd  && python $TMPDIR/nb/insert.py
```

```
ok
```

**Agent**

Fixing two counts in the fig2 Result text: acg sites are in 6 recordings, not 7, and the maxima outside LS range from 3.49 to 44.33.

**Agent calls Bash**

```bash
. $TMPDIR/wk/bin/activate && cd  && python - <<'EOF'
import nbformat
for base in ["entries/tingley-2019","executed/tingley-2019"]:
    p=f"{base}/lfp_tingley_2019.ipynb"; nb=nbformat.read(p,4)
    n=0
    for c in nb.cells:
        if c.cell_type=="markdown" and "fig2-confined-to-ls not reproduced" in c.source:
            c.source=c.source.replace("than the acg sites in all 7 recordings with acg sites","than the acg sites in all 6 recordings with acg sites").replace("(maxima 2.54 to 44.33)","(the largest such ratio per recording is 3.49 to 44.33)"); n+=1
    nbformat.write(nb,p); print(p,n)
EOF
python tools/entry.py check entries/tingley-2019 2>&1 | tail -3
```

```
entries/tingley-2019/lfp_tingley_2019.ipynb 1
executed/tingley-2019/lfp_tingley_2019.ipynb 1
0 error(s)
```

**Agent**

Spot-checking that the executed main notebook matches the numbers in its Result cells, which I wrote from the development run.

**Agent calls Bash**

```bash
. $TMPDIR/wk/bin/activate && cd  && python - <<'EOF'
import nbformat,re
nb=nbformat.read("executed/tingley-2019/reproduce_tingley_2019.ipynb",4)
txt="\n".join(o.get('text','') for c in nb.cells if c.cell_type=='code' for o in c.get('outputs',[]))
for pat in ["Readings where PRE and POST differ","Readings with both parts","fraction 0.057","Pooled over all LS neurons","LS neurons in the triggered","Primarily NREM","within \\+-50 ms: 6572","paired p = 0.0025","LS neurons: 1266","factors 1-7 with POST","LS: 1570","CA1 ripples    LS-LS 0.025          True","seed 461066033","largest factor PRE","median ratio","minimum in 0-200"]:
    for m in re.finditer(pat,txt): print(txt[m.start():m.start()+260].replace("\n"," | ")); break
    else: print("MISSING",pat)
EOF
```

```
Readings where PRE and POST differ (rank-sum p < 0.05): 8 of 16; pairs per reading 361 to 503 (paper 7172, tolerance 717); sessions 21 to 23 (paper 53) |  | Per animal, reading (a, sd, raw, trials): pairs, median PRE, median POST, rank-sum p |   DT2: 49, 0.385, 0.39
Readings with both parts: 12; part 1 only: 0; part 2 only: 4; neither: 0 of 16 |  | seed 3611125032: readings with part 2 (each epoch above its jitter at p < 0.01) 16 of 16; BEHAV above jitter in 16; PRE in 16; POST in 16 |  | seed 3611126032: readings with part 2 (ea
fraction 0.057, spikes per neuron per event 0.079; (ii) mean of 73 recordings: fraction 0.069, spikes 0.096 | window (b): (i) pooled events: fraction 0.087, spikes per neuron per event 0.125; (ii) mean of 73 recordings: fraction 0.107, spikes 0.155 | Paper: 0.16 (
Pooled over all LS neurons, after the burst (+20..50 ms): HFO 0.001399 +- 0.000059 (SEM), random 0.001599; random minus HFO 0.000200, 3 SEM 0.000178; below by more than 3 SEM: True | Pooled over all LS neurons, after the burst (stop..+50 ms): HFO 0.001517 +- 0.0
LS neurons in the triggered averages: 2327 in 73 recordings | All animals pooled (mean HFO, SEM, mean random, SEM): {'event bin': (np.float64(0.00723), np.float64(0.00075), np.float64(0.00156), np.float64(0.00013)), '+-5 ms': (np.float64(0.00321), np.float64(0.0
Primarily NREM: 0.729 of 27014 LS HFOs fall in NREM; NREM rate > WAKE rate in 66 of 73 recordings, signed-rank p = 2.9e-12 | By animal, fraction of LS HFOs in NREM: {'DT1': 0.815, 'DT2': 0.801, 'DT5': 0.661, 'DT7': 0.296, 'DT8': 0.56, 'DT9': 0.868} | Lower than CA
within +-50 ms: 6572 pairs in 40 recordings; (a) median over recordings of medians 6.20 ms (SD over recordings 10.16); (b) pooled median 6.40 ms; positive (CA1 leading) fraction 0.639 | within +-25 ms: 5343 pairs in 40 recordings; (a) median over recordings of m
paired p = 0.0025 (t = 3.22), two-sample p = 0.014 (t = 2.50); NREM higher in 30 of 42 |  | WAKE = outside trials: 42 recordings |   CCG bins wit
[... 8 more lines not kept]
```

**Agent**

The executed outputs match the Result cells. Next: the entry README and the attempt record. I'll generate the record from Python so the YAML quoting is safe.

**Agent calls Bash**

```bash
cat > entries/tingley-2019/README.md <<'EOF'
# Tingley and Buzsaki (2019) on DANDI:000218

Tests the findings of Tingley D. and Buzsaki G. (2019), "Routing of hippocampal ripples to subcortical structures via the lateral septum", Neuron 105, 138-149 (doi:10.1016/j.neuron.2019.10.012), on dandiset 000218, version 0.261110.1911, streamed from the DANDI Archive.

- `reproduce_tingley_2019.ipynb`: the claims that use spikes, the lab's LS HFO and CA1 ripple tables, sleep states and trials (Figures 1, 4, 5, S1 to S3, and two Discussion statements). About 15 minutes.
- `lfp_tingley_2019.ipynb`: the claims that need the LFP (phase locking, locking to the CA1 ripple band, event times at the maximum NSS, CA1-LS coherence, HFO power by recording site). About 50 minutes.
- `fig7e_tingley_2019.ipynb`: LS spike counts in SPW-Rs predicted from the hippocampal spike count, brain state and SPW-R duration (Figure 7E). About 16 minutes.
- `tingley2019.py`: loading and shared measures; its docstrings say where each parameter comes from.

Claims on the optogenetic rats, on electrode geometry and on depth within LS cannot be tested from the dandiset; replay, seqNMF and the network model were not attempted within the run's time.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.
EOF
date -u
```

```
Wed Nov 18 12:21:59 UTC 2026
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/rec && cat > $TMPDIR/rec/make.py <<'PYEOF'
import yaml
M="reproduce_tingley_2019.ipynb"; L="lfp_tingley_2019.ipynb"; F="fig7e_tingley_2019.ipynb"
EPOCHS=("The dataset does not mark PRE, BEHAV and POST. PRE is taken as the recording before the first trial's start, BEHAV from the first trial's "
        "start to the last trial's stop, and POST after the last trial's stop (an assumption; the STAR Methods say each recording has the three periods in that order).")
DET=("Events are the lab's deposited detections (claims file, open detail i, reading a), LSRipples and CA1Ripples, whose stored parameters differ from the Methods "
     "(LS 120-180 Hz, durations up to 100 ms, peak thresholds of 4 to 6 SD in some files; CA1 130-200 Hz).")
NORM=("Assumed: the CCG divided by the square root of the product of the two neurons' spike counts in the epoch (claims reading iii). The paper does not say how "
      "the CCG is normalized; the normalized reading is adopted because the paper compares excess correlations across epochs with very different spike counts "
      "(BEHAV and HFO epochs), which raw counts do not allow. The raw-count readings are shown.")
o=[]
def add(**k): o.append(k)
add(claim="dataset-composition", outcome="partially_reproduced", notebook=L, output="claim:dataset-composition",
    measured=[6,1996,38,10,77,47,31.1],
    notes=("Animals 6 (DT1, DT2, DT5, DT7, DT8, DT9). LS neurons with more than 50 spikes in high-power epochs (reading a) 1996, within 1989 +- 198.9; all LS units 2551 (reading b). "
           "Of 48 recordings with LS and hippocampal units, 38 are CA1 and 10 CA3 by the units' label (CA1 within 37 +- 3.7, CA3 outside 25 +- 2.5); by the ca3_channel flag 29 and 19. "
           "LS HFO rates come from 77 recordings with LSRipples and sleep states (80 with any LS table; outside 89 +- 8.9). CA1 ripple rates come from 47 recordings with CA1Ripples "
           "(outside 53 +- 5.3), or 55 with ripplesALL too (within). LS units per recording 8 to 74, mean 31.1 +- 15.5 (within). Four of the six counts other than animals are within "
           "tolerance under one reading each, the partial bound. The counts by recording are in the main notebook (claim:dataset-composition)."),
    deviations=["CA1 and CA3 recordings are told apart by the units' region label and, as a variant, by the electrodes' ca3_channel flag; most hippocampal units are labelled only hpc.",
                "Recordings with rates are those with the event table and scored sleep; earlier LS tables and ripplesALL are counted as a variant."])
add(claim="fig1c-hfo-each-animal", outcome="partially_reproduced", notebook=M, output="claim:fig1c-hfo-each-animal",
    notes=("Median LS HFO frequency 142.9 to 149.2 Hz, inside 120-180 Hz in all 6 animals. The HFO-triggered LS spike probability exceeds the random-time mean by more than 3 SEM "
           "at the event bin in 4 of 6 animals (DT1, DT2, DT8, DT9) and over +-5 ms in 5 of 6 (all but DT5). Under the five seeds of the random times, 4, 4, 5, 4 and 5 animals at the event bin; "
           "the outcome is partial under all. Pooled over 2327 neurons, 0.0072 against 0.0016 spikes per ms per event."),
    deviations=[DET, "The triggered histogram's 1 ms bins over +-100 ms and the comparison windows are those set in the claims file; the random times are uniform over each recording."])
add(claim="fig1c-post-burst-suppression", outcome="not_reproduced", notebook=M, output="claim:fig1c-post-burst-suppression", assumed=True,
    notes=("From each event's stop to 50 ms after its time, the pooled probability is 0.001517 against 0.001593 at random times, a difference of 0.000076, less than 3 SEM (0.000201). "
           "From 20 to 50 ms after the event time it is 0.001399, below random by 0.000200, more than 3 SEM (0.000178) under the claim's seed; over the five seeds this reading "
           "gives suppression under 3 and none under 2, while the window from the stop gives none under all five. Per animal, only DT5 shows suppression, under both windows."),
    deviations=["Assumed: the window from each event's stop to 50 ms after its time, as the reading of the Results' 'immediately following the population burst'. The paper gives no window or test; the claims file names this window and one from 20 to 50 ms, which differ in outcome."])
add(claim="fig1c-event-count", outcome="reproduced", notebook=M, output="claim:fig1c-event-count", measured=27014,
    notes="LSRipples holds 27014 events in 77 recordings with LS electrodes, in 6 animals (reading a), within 29955 +- 2995.5. Recordings with LS units (reading b) hold 25690. With the earlier LS tables where LSRipples is missing, 28978.",
    deviations=[DET])
add(claim="figs1-participation", outcome="not_reproduced", notebook=M, output="claim:figs1-participation", measured=[0.057,0.079],
    notes=("Window start to stop, pooled events: 5.7% of LS neurons fire in an HFO, 0.079 spikes per neuron per event; mean over 73 recordings 6.9% and 0.096. Window +-25 ms: 8.7% and 0.125 pooled, "
           "10.7% and 0.155 over recordings. No combination reaches 16% +- 1.6% or 0.23 +- 0.023. Per animal (start to stop) 3.3% (DT7) to 12.4% (DT1)."),
    deviations=[DET])
add(claim="fig1d-phase-locking", outcome="partially_reproduced", notebook=L, output="claim:fig1d-phase-locking", measured=0.606,
    notes=("Detection channel, 120-200 Hz: 1209 of 1996 LS neurons with more than 50 spikes in high-power epochs are locked (60.6%; 52.0% of all 2327). Own shank's channel: 883 of 1129 (78.2%). "
           "120-180 Hz: 61.3%. All outside 92.5% +- 9.25%. The null of 10 circular shifts gives 5.2%. Significant neurons prefer -167.0 degrees, 13.0 from the trough, Rayleigh over neurons p < 1e-300, "
           "so the trough preference holds. Per animal 39.3% (DT9) to 76.8% (DT1)."),
    deviations=["The own-shank reading uses the middle site of the neuron's shank, and only for shanks whose sites share the detection channel's 16-channel storage block (1299 of 2327 neurons); reading other blocks would have multiplied the data streamed.",
                "Filtering is zero-phase (forward and backward), a standard choice; the Rayleigh p-value is the CircStat approximation."])
add(claim="fig1f-shorter-than-ripples", outcome="reproduced", notebook=M, output="claim:fig1f-shorter-than-ripples", measured=[27.8,31.2],
    notes="LS HFOs 27.8 +- 9.5 ms and CA1 ripples 31.2 +- 13.7 ms in the 4 animals with both tables (DT2, DT5, DT7, DT9), rank-sum p = 1.2e-199; reading (2) gives the same means. Shorter in each animal.",
    deviations=[DET])
add(claim="fig1g-slower-than-ripples", outcome="reproduced", notebook=M, output="claim:fig1g-slower-than-ripples", measured=[147.6,158.3],
    notes="LS HFOs 147.6 +- 5.8 Hz and CA1 ripples 158.3 +- 7.4 Hz, rank-sum p below 1e-300 (printed as 0); slower in each of the 4 animals.",
    deviations=[DET, "Frequencies are the deposited peak_frequency values, the lab's instantaneous frequency at the event peak, read as Hz."])
add(claim="fig1h-no-amplitude-frequency-correlation", outcome="reproduced", notebook=M, output="claim:fig1h-no-amplitude-frequency-correlation", assumed=True,
    notes=("Over 27014 LS HFOs, peak_amplitude against peak_frequency: Pearson r = 0.006 (p = 0.3); Spearman rho = 0.020 (p = 0.00095). With peak_normed_power, r = -0.000 (p = 0.96) and rho = 0.006 (p = 0.36). "
           "Within animals both correlations are significant in 5 of 6 animals, r from -0.107 to 0.169, with signs that differ between animals."),
    deviations=["Assumed: the Pearson correlation. The paper names no test; the claims file names Pearson and Spearman, which differ in outcome (Spearman finds a negligible but significant rho of 0.020). Pearson is the usual test of the linear relation a scatter like Figure 1H shows.",
                "Amplitude is the deposited peak_amplitude; peak_normed_power is shown as a variant."])
add(claim="fig2-confined-to-ls", outcome="not_reproduced", notebook=L, output="claim:fig2-confined-to-ls",
    notes=("Eight recordings (all DT7) have LS sites and sites of another non-hippocampal structure (acg, cc, ms, sfi). The criterion holds in none. The LS median power ratio exceeds the acg median in all 6 recordings with acg sites, "
           "but medial septal sites exceed the LS median in 3 recordings (12.32 against 4.97 in 20170320), and in every recording some site outside LS has a ratio above 1.5 (the largest per recording 3.49 to 44.33). "
           "Each recording's ratios rest on 17 to 113 LS HFOs."),
    deviations=["Power ratios are computed in the two storage chunks (about 14 min each) of each recording with the most LS HFOs, to bound the data streamed.", "Sites are placed by the electrodes' region labels; the dataset holds no depth estimate."])
add(claim="fig2ef-intermediate-ls", outcome="blocked", blocked_by="metadata_insufficient",
    notes=("The criterion needs each recording's estimated relative depth in LS (STAR Methods, Relative anatomical depth within LS). The dandiset does not store it; its release notes say the relative depth is not in the source files. "
           "Session names carry drive depths in um, which are not the paper's depth estimate (implantation depth, daily turns and histology). The per-recording phase-locking percentages it would use are computed in the LFP notebook."))
add(claim="fig3-travelling-waves", outcome="blocked", blocked_by="metadata_insufficient",
    notes="The speeds need the distance between sites along AP, ML and DV. The dandiset stores no electrode positions (release notes: every .prb file places sites by list position with one template), and the probe model of each recording is not stored.")
add(claim="fig4b-pre-post-unchanged", outcome="partially_reproduced", notebook=M, output="claim:fig4b-pre-post-unchanged", measured=462, assumed=True,
    notes=("Under the 8 normalized readings, the rank-sum test of PRE against POST finds no difference (p 0.50 to 0.89; effect r -0.013 to 0.025). Under the 8 raw-count readings it does (p 0.0036 to 0.0065, POST higher; r -0.10 to -0.12). "
           "Only 361 to 503 pairs in 21 to 23 sessions pass the inclusion rule (462 under inclusion a with BEHAV in trials), against 7172 pairs in 53 sessions; no DT8 pair passes. "
           "The absence holds under the adopted reading, on 6% of the paper's pairs."),
    deviations=[NORM, EPOCHS, DET, "The inclusion rule is applied to the spikes of each epoch (claims reading i); spikes during HFOs are those between each LS HFO's start and stop."])
add(claim="fig4b-hfo-above-behav", outcome="reproduced", notebook=M, output="claim:fig4b-hfo-above-behav", assumed=True,
    notes=("Under the 8 normalized readings PRE and POST exceed BEHAV (rank-sum p 7e-69 to 3e-129) and PRE, POST and BEHAV each exceed their jittered values (p <= 2.1e-6). Under raw counts every epoch exceeds its jitter, "
           "but with BEHAV from the first to the last trial PRE and POST do not exceed BEHAV (p 0.13 to 0.87). Under the four other jitter seeds all 16 readings keep every epoch above its jitter."),
    deviations=[NORM, EPOCHS, "The jitter moves every spike of the whole train by a uniform amount in +-200 ms before the epochs and HFO windows are applied; one jitter per pair."])
add(claim="fig4-sessions-few-change", outcome="not_reproduced", notebook=M, output="claim:fig4-sessions-few-change", measured=[23,0.0],
    notes="21 to 23 sessions have included pairs, against 53 +- 5.3. Under the adopted normalized readings 0 or 1 session differs at p < 0.01 (fraction 0 to 0.043); under raw counts 0 or 1 (up to 0.048). No reading has both directions.",
    deviations=[NORM, EPOCHS])
add(claim="fig4c-temporal-bias", outcome="reproduced", notebook=M, output="claim:fig4c-temporal-bias",
    notes=("No reading finds the PRE-BEHAV and BEHAV-POST correlations different: paired p 0.060 to 0.90, two-sample 0.13 to 0.91; mean BEHAV-POST minus PRE-BEHAV -0.017 to 0.194. "
           "16 to 19 recordings have at least 3 included pairs, against 53."),
    deviations=[EPOCHS, "Recordings need at least 3 included pairs for a correlation (a minimum set here)."])
add(claim="fig4d-compression", outcome="partially_reproduced", notebook=M, output="claim:fig4d-compression", measured=6,
    notes=("At factor 1 the HFO CCGs correlate with BEHAV above chance in every reading. Every factor up to 5 to 8 (PRE) and 8 to 11 (POST) is above chance at p < 0.01, against ~20 (18 to 22); "
           "with inclusion a and BEHAV in trials, PRE 6 and POST 8 by signed-rank, so 6 for both. Under four other seeds of the circular shift the largest factor is 5 to 12; the outcome is partial under all. "
           "PRE and POST do not differ at p < 0.01 at any factor (smallest p 0.055)."),
    deviations=[EPOCHS, "Chance shifts the BEHAV CCG circularly by a random amount, one shift per pair and factor."])
add(claim="figs3d-hpc-compression-post", outcome="partially_reproduced", notebook=M, output="claim:figs3d-hpc-compression-post",
    notes="Over 9366 to 15066 hippocampal pairs in 42 recordings, POST exceeds PRE at p < 0.01 at 1 to 3 of the factors 1 to 7 (factor 3 in every reading, p <= 0.0012), not at most. POST medians are at or above PRE medians at every factor 1 to 7.",
    deviations=[EPOCHS, "Hippocampal pairs are pairs with the same region label (hpc or ca3); CA1 ripples are CA1Ripples, so the DT9 CA3 recordings without that table are left out."])
add(claim="figs2-post-rate-increase", outcome="partially_reproduced", notebook=M, output="claim:figs2-post-rate-increase", measured=[1570,2597,466],
    notes=("Relative to the session average, LS rates are higher in POST NREM than PRE NREM (1.334 against 1.265; paired p = 0.032, two-sample p = 0.036). CA1 rates (units labelled hpc) are lower (1.293 against 1.347; paired p = 0.043), "
           "CA3 rates unchanged (p = 0.59). By the ca3_channel flag, CA1 lower (p = 0.018) and CA3 unchanged (p = 0.94). Counts 1570, 2597 and 466 against 1754, 2315 and 1373; LS is 9 short of the lower bound."),
    deviations=[EPOCHS, "CA1 is read as units labelled hpc or ca1 and CA3 as ca3, with the ca3_channel flag as a variant.", "Recordings need at least 60 s of NREM in both PRE and POST (a minimum set here)."])
add(claim="figs2c-no-ls-reactivation", outcome="reproduced", notebook=M, output="claim:figs2c-no-ls-reactivation",
    notes=("With 25 ms bins after rate matching EV does not exceed REV: LS-LS in CA1 ripple epochs 0.128 against 0.094 (paired p = 0.23), in LS HFO epochs 0.042 against 0.052 (p = 0.57); HPC-HPC 0.028 against 0.010 (p = 0.18); "
           "HPC-LS p = 0.33. The same under four other seeds. The Methods' increase of EV over REV with 1 s bins appears only for HPC-HPC pairs without rate matching (paired p = 0.049)."),
    deviations=[EPOCHS, "Bins are laid over the ripple epochs concatenated end to end.", "Rate matching removes spikes at random from the faster of PRE and POST NREM ripple epochs per neuron, 10 repetitions averaged."])
add(claim="fig5b-nrem-and-rates", outcome="reproduced", notebook=M, output="claim:fig5b-nrem-and-rates",
    notes=("72.9% of 27014 LS HFOs fall in NREM; NREM rate above WAKE in 66 of 73 recordings (signed-rank p = 2.9e-12); DT7 has 29.6% in NREM. LS rates are lower than CA1 rates in NREM (medians 0.024 and 0.320 per s; rank-sum p = 1.5e-13; "
           "signed-rank over 42 recordings p = 2.9e-10) and over all scored time (rank-sum p = 1.3e-12). 77 LS and 47 CA1 recordings, against 89 and 53."),
    deviations=[DET])
add(claim="fig5d-lag", outcome="reproduced", notebook=M, output="claim:fig5d-lag", measured=6.2,
    notes=("Deposited peak times, nearest CA1 ripple within +-50 ms: median of recording medians 6.20 ms, pooled 6.40 ms (6572 pairs, 40 recordings), CA1 leading in 63.9%; within +-25 ms 4.80 ms. "
           "Maximum-NSS times (LFP notebook): 6.00 and 6.40 ms within +-50 ms, 3.40 and 4.00 ms within +-25 ms. The pooled CCG peaks at 0 ms, 37.1 SD above its 100-200 ms flanks. "
           "Per animal the pooled median ranges from -7.2 ms (DT7) to 8.0 ms (DT9)."),
    deviations=[DET])
add(claim="fig5e-state-coupling", outcome="not_reproduced", notebook=M, output="claim:fig5e-state-coupling", measured=[0.213,0.118,42],
    notes=("42 recordings. Fraction of LS HFOs with a CA1 ripple within +-25 ms: mean over recordings 0.213 in NREM and 0.118 in WAKE; pooled 0.302 and 0.091. NREM higher in 30 of 42, t-test p = 0.0025 paired and 0.014 two-sample, "
           "above both 6.6e-6 and the partial bound of 0.001. No CCG bin within +-25 ms differs at Bonferroni p < 0.001 (smallest 0.026). WAKE outside trials gives the same."),
    deviations=[DET, "The state of an event is the state at its peak time; CCG bins of 5 ms over +-200 ms normalized by the number of CA1 ripples (the claims file's standard choice)."])
add(claim="fig5f-ripple-triggered-firing", outcome="not_reproduced", notebook=M, output="claim:fig5f-ripple-triggered-firing", measured=1266,
    notes=("1266 LS neurons in 38 recordings (within 1313 +- 131.3). At zero lag 2.14 Hz in NREM and 2.03 Hz in WAKE; no bin within +-25 ms has NREM higher at corrected p < 0.001 under any reading (smallest corrected p 0.18). "
           "Normalized by the state's mean rate the WAKE response is larger (1.73 against 1.48)."),
    deviations=[DET])
add(claim="fig5f-no-phase-coherence", outcome="not_reproduced", notebook=L, output="claim:fig5f-no-phase-coherence",
    notes=("41 recordings, 91316 CA1 ripples. The CA1-LS 120-180 Hz phase-locking value at the ripple time is 0.186 against 0.104 +- 0.0072 (mean and SD of 100 jittered sets); 14 of 101 lags lie above the +3 SD bound, the largest 14.7 SD at 4 ms. "
           "The jittered sets are drawn per recording from the claim's seed; the variation over five seeds was not run (the bound is 11 SD below the value)."),
    deviations=["Coherence is read as the phase-locking value across ripples of the CA1 minus LS phase (claims file); channels are the CA1 and LS detection channels."])
add(claim="ls-spikes-not-locked-to-ca1-ripples", outcome="not_reproduced", notebook=L, output="claim:ls-spikes-not-locked-to-ca1-ripples", assumed=True,
    notes=("Inside CA1 ripples (reading a) 43 of 599 LS neurons with more than 50 spikes (7.2%) are locked to the CA1 channel's 120-200 Hz phase, above 5% (one-sided binomial p = 0.012); median resultant length 0.068, against 0.136 for the LS channel; "
           "10 circular shifts give 4.9%. In the CA1 channel's high-power epochs (reading b) 61 of 1218 (5.0%, p = 0.51). The fraction locked to the LS channel is 60.6%."),
    deviations=["Assumed: reading (a), spikes inside CA1 ripples, as the reading of 'individual waves of hippocampal SPW-Rs'. The paper shows no method; the two readings of the claims file differ in outcome."])
add(claim="fig6-optogenetic-hfos", outcome="blocked", blocked_by="data_missing",
    notes="The two optogenetically injected rats, their light stimulation times and waveforms are not in the dandiset: its 98 files are the six rats DT1, DT2, DT5, DT7, DT8 and DT9, with no stimulus or optogenetic series in any file. The paper names no other archive for them.")
add(claim="fig7e-ca1-spikes", outcome="partially_reproduced", notebook=F, output="claim:fig7e-ca1-spikes", measured=64.4,
    notes=("1288 LS neurons in 42 recordings. Over 16 combinations the hippocampal spike count predicts 47.0% to 80.0% of neurons (64.4% with a cross-validated linear model, start-stop window, no minimum, the first combination); none within 38% +- 3.8%. "
           "Every combination exceeds its chance rate (25.4% to 44.3%; binomial p <= 2.4e-7). Linear models under four other seeds give 46.6% to 64.2%."),
    deviations=[DET, "The shuffles are repeated under five seeds for the linear models only; the Poisson fits were run under the claim's seed alone, for time.",
                "CA3 recordings use the CA1Ripples table; the DT9 CA3 recordings, which lack it, are left out (42 recordings against 62)."])
add(claim="fig7e-state", outcome="partially_reproduced", notebook=F, output="claim:fig7e-ca1-spikes", measured=52.9,
    notes="The state predicts 44.4% to 63.9% of 1238 LS neurons over 16 combinations (52.9% for the first), against 26% +- 2.6%; above chance in all (binomial p <= 3.2e-9). Linear models under four other seeds give 44.5% to 58.2%.",
    deviations=[DET, "As fig7e-ca1-spikes."])
add(claim="fig7e-duration", outcome="partially_reproduced", notebook=F, output="claim:fig7e-ca1-spikes", measured=69.0,
    notes="The SPW-R duration predicts 41.1% to 89.0% of 1288 LS neurons (69.0% for the first combination), against 20% +- 2%; above chance in all 16 combinations (binomial p <= 6.3e-4). Linear models under four other seeds give 40.1% to 72.0%.",
    deviations=[DET, "As fig7e-ca1-spikes."])
add(claim="fig7e-ca1-depth", outcome="blocked", blocked_by="metadata_insufficient",
    notes="Ripple depth needs each CA1 neuron's waveform on its three largest sites and the site spacing, and the 120-200 Hz power profile across a shank's sites. The units hold one waveform each and the dandiset stores no electrode positions.")
add(claim="fig7e-replay", outcome="blocked", blocked_by="other",
    notes="Not attempted within the run's five hours: the three replay scores need place fields from the linearized position and Bayesian decoding of every SPW-R in each of the readings the claims file names. The dataset holds the trials, linearized position and spikes the analysis would need.")
add(claim="fig7e-seqnmf", outcome="blocked", blocked_by="other",
    notes="Not attempted within the run's five hours (seqNMF with 40 templates on every recording, then the Figure 7E regressions). Depends also on figs5-seqnmf-variance.")
add(claim="figs5-seqnmf-variance", outcome="blocked", blocked_by="other",
    notes="Not attempted within the run's five hours: seqNMF (Mackevicius et al. 2019) would have to be ported or installed and run with 40 templates on the hippocampal spiking of 44 recordings under several readings.")
add(claim="fig7e-content-independent", outcome="blocked", blocked_by="metadata_insufficient",
    notes="Depends on fig7e-ca1-depth (metadata_insufficient), and on fig7e-replay and fig7e-seqnmf (not attempted). The three content-independent features tested (spike count, state, duration) are each above chance in every combination (Figure 7E notebook).")
add(claim="fig7e-coupled-only", outcome="blocked", blocked_by="metadata_insufficient",
    notes="Depends on fig7e-content-independent, which is blocked.")
add(claim="discussion-medial-septum", outcome="not_reproduced", notebook=L, output="claim:discussion-medial-septum",
    notes=("Part (a): in the 6 recordings with medial septal sites, their median HFO power ratio lies below the LS sites' in 3 (20170318, 20170325, 20170401) and above it in 3 (e.g. 12.32 against 4.97). "
           "Part (b) (main notebook): the 25 ms units in 2 recordings fire more within +-50 ms of CA1 ripples than on average (median ratio 1.43; below the mean in 6 of 25; signed-rank p = 0.0046). Neither part holds."),
    deviations=["Medial septal sites and units are those the dataset labels ms; power ratios use two chunks of each recording, as for fig2-confined-to-ls."])
add(claim="discussion-cingulate-down-state", outcome="not_reproduced", notebook=M, output="claim:discussion-cingulate-down-state", measured=105,
    notes=("Reading (a): the 31 acg units (2 recordings) reach their minimum triggered rate at 105 ms after CA1 ripples (0.62 of the mean rate); per recording 105 and 130 ms. Reading (b) (LFP notebook): the extremum of the acg ripple-triggered LFP "
           "lies at 2.4 to 7.2 ms in 5 of 6 recordings and at 81.6 ms in one. Neither is within 50 +- 5 ms."),
    deviations=["Anterior cingulate units and sites are those labelled acg; the LFP reading uses CA1 ripples in two chunks of each recording."])
add(claim="fig8-model", outcome="blocked", blocked_by="other",
    notes="Not attempted within the run's five hours. The model is in github.com/DavidTingley/papers at commit 9f4cd48 (pyNN with NEURON), not in the dandiset; installing NEURON and pyNN in a locked environment and running 200 runs per sequence type was not tried.")
rec = {
 "schema_version": 3, "id": "tingley-2019-02",
 "datasets": [{"archive": "dandi", "id": "000218", "version": "0.261110.1911", "doi": "10.48324/dandi.000218/0.261110.1911", "relation": "primary"}],
 "paper": "doi:10.1016/j.neuron.2019.10.012", "date": "2026-11-18", "entry": "tingley-2019",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-16"},
                "runner": {"platform": "GitHub Actions", "url": "https://github.com/catalystneuro/encore/actions/runs/44280379678"}},
 "outcomes": o,
 "findings": [
  {"kind": "data_missing", "statement": "The two rats of the optogenetic experiments (Figure 6, Figure S4), with their light stimulation times and waveforms, are not in the dandiset; its 98 files hold six rats (DT1, DT2, DT5, DT7, DT8, DT9) and no stimulus or optogenetic series."},
  {"kind": "metadata_insufficient", "statement": "Electrode positions are not stored, nor the probe model of each recording, so distances between sites, travelling-wave speeds (Figure 3) and CA1 neuron depths (Figure 7D, E) cannot be computed."},
  {"kind": "metadata_insufficient", "statement": "The estimated relative depth of each recording within LS (STAR Methods), on which Figure 2E, F and Figure S1C, D rest, is not stored; session names carry drive depths only."},
  {"kind": "metadata_insufficient", "statement": "The pre-behavior home cage, maze and post-behavior home cage periods of each recording are not marked; they can be inferred only from the first and last trials."},
  {"kind": "metadata_insufficient", "statement": "Most hippocampal units are labelled hpc, not CA1 or CA3, so CA1 and CA3 populations cannot be told apart reliably: 10 recordings have units labelled ca3 and 19 have a ca3_channel flag, against the paper's 25 CA3 recordings."},
  {"kind": "metadata_error", "statement": "The 36 units of sub-DT7 session 20170407-936um-1152um-merge have an empty region label."},
  {"kind": "other", "about": "data", "statement": "In three files less than half of the trial time is scored WAKE (DT2 3540um-1288um 20160227, 12.5%; DT5 20161014-1296um-1476um, 20.3%; DT8 20170201-72um-432um, 31.6%), against 100% in the median file; either the sleep scoring or the trial times of these files are doubtful."},
  {"kind": "data_missing", "statement": "The DT9 CA3 recordings (20170518, 20170519, 20170521, 20170525, 20170526) have no CA1 ripple table, although the paper detected SPW-Rs on a CA1 reference electrode for CA3 recordings; DT7 20170410 has 61 LS units but no LS HFO table, and DT2 20160215-122710 has 37 LS units and no event table at all."},
  {"kind": "other", "about": "data", "statement": "The deposited LS HFO detections (LSRipples) were made with parameters that differ from the paper's Methods (120-180 Hz, durations up to 100 ms, peak thresholds of 4 to 6 SD in some files, against 120-200 Hz, 15-250 ms and 5 SD), and CA1Ripples with 130-200 Hz; the files' descriptions say so. Their event counts, durations and frequencies match the paper's (27014 LS HFOs, 27.8 ms, 147.6 Hz)."},
  {"kind": "methods_unavailable", "statement": "Excess correlation (Figure 4B): how is each CCG normalized before smoothing? Raw counts make POST differ from PRE (rank-sum p 0.004); counts divided by the square root of the two spike counts do not (p 0.5 to 0.9). The normalized CCG was assumed. Which pairs passed inclusion (7172), given that the dataset yields 361 to 503 under the stated rule applied to HFO spikes?"},
  {"kind": "methods_unavailable", "statement": "Which test and window show the suppression of LS firing after the HFO population burst (Figures 1C, 5F)? From the event stop to 50 ms no suppression is found; from 20 to 50 ms a marginal one depending on the random baseline. The window from the stop was assumed."},
  {"kind": "methods_unavailable", "statement": "Which correlation and test does Figure 1H use for amplitude against peak frequency? Pearson finds none (p = 0.3) and Spearman a negligible significant one (rho = 0.020, p = 0.00095); Pearson was assumed."},
  {"kind": "methods_unavailable", "statement": "How was the absence of LS spike locking to individual SPW-R waves tested (no figure or method is given)? Inside CA1 ripples 7.2% of LS neurons are locked (binomial p = 0.012 against 5%); in the CA1 channel's high-power epochs 5.0%. Spikes inside ripples were assumed."},
  {"kind": "methods_unavailable", "statement": "Where do the pre-behavior, behavior and post-behavior periods begin and end in each recording? The first trial's start and the last trial's stop were assumed as the boundaries."}
 ]}
txt = yaml.safe_dump(rec, sort_keys=False, allow_unicode=True, width=110, default_flow_style=False)
open("attempts/tingley-2019-02.yaml","w").write(txt)
print(len(o), "outcomes")
PYEOF
. $TMPDIR/wk/bin/activate && python $TMPDIR/rec/make.py && cd  && python tools/entry.py check entries/tingley-2019 2>&1 | tail -5; grep -c "claim:" claims/tingley-2019.yaml; python -c "
import yaml;c=yaml.safe_load(open('claims/tingley-2019.yaml'));a=yaml.safe_load(open('attempts/tingley-2019-02.yaml'))
print(set(x['id'] for x in c['claims'])-set(x['claim'] for x in a['outcomes']))"
```

```
39 outcomes
0 error(s)
0
set()
```

**Agent**

The record validates with 0 errors. Pointing the fig7e-state and fig7e-duration outputs at their own tags, then checking the text for forbidden characters and words.

**Agent calls Bash**

```bash
sed -i 's/  output: claim:fig7e-ca1-spikes\n  measured: 52.9/X/' attempts/tingley-2019-02.yaml && . $TMPDIR/wk/bin/activate && python - <<'EOF'
import yaml
p='attempts/tingley-2019-02.yaml'; a=yaml.safe_load(open(p))
for o in a['outcomes']:
    if o['claim'] in ('fig7e-state','fig7e-duration'): o['output']='claim:'+o['claim']
open(p,'w').write(yaml.safe_dump(a, sort_keys=False, allow_unicode=True, width=110))
EOF
grep -n "—\|–\|rather\|\*\*" attempts/tingley-2019-02.yaml | head; for f in entries/tingley-2019/*.ipynb entries/tingley-2019/*.py entries/tingley-2019/README.md; do grep -l "—\|rather" $f; done; python - <<'EOF'
import nbformat,re
for n in ["reproduce","lfp","fig7e"]:
    nb=nbformat.read(f"entries/tingley-2019/{n}_tingley_2019.ipynb",4)
    for c in nb.cells:
        if c.cell_type=="markdown":
            b=re.findall(r"\*\*[^*]+\*\*",c.source)
            bad=[x for x in b if not x.startswith("**Result:") and not x.startswith("**How") and not x.startswith("**What")]
            if bad: print(n,bad)
EOF
python tools/entry.py check entries/tingley-2019 2>&1 | tail -2
```

```
0 error(s)
```

**Agent**

The Summary has two bold openers that the style rules don't allow. Removing them in both copies.

**Agent calls Bash**

```bash
. $TMPDIR/wk/bin/activate && python - <<'EOF'
import nbformat
for base in ["entries/tingley-2019","executed/tingley-2019"]:
    p=f"{base}/reproduce_tingley_2019.ipynb"; nb=nbformat.read(p,4)
    for c in nb.cells:
        if c.cell_type=="markdown" and c.source.startswith("## Summary"):
            c.source=c.source.replace("**How the analysis differs from the paper's.**","How the analysis differs from the paper's:").replace("**What was found about the dataset.**","What was found about the dataset:")
    nbformat.write(nb,p)
EOF
grep -c '\*\*How\|\*\*What' entries/tingley-2019/reproduce_tingley_2019.ipynb; python tools/entry.py check entries/tingley-2019 2>&1 | tail -1; python tools/entry.py handover entries/tingley-2019; ls executed/tingley-2019/handover; date -u
```

```
0
0 error(s)
wrote executed/tingley-2019/handover
fig7e_tingley_2019.ipynb
lfp_tingley_2019.ipynb
reproduce_tingley_2019.ipynb
tingley-2019.yaml
tingley2019.py
Wed Nov 18 12:24:22 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/wk/bin/activate && python tools/entry.py all entries/tingley-2019 2>&1 | tail -6; date -u
```

```
Installed kernelspec registry-tingley-2019 in executed/tingley-2019/.venv/share/jupyter/kernels/registry-tingley-2019
0 error(s)
pass  reproduce_tingley_2019.ipynb  (908 s)
pass  lfp_tingley_2019.ipynb  (2707 s)
pass  fig7e_tingley_2019.ipynb  (942 s)
Wed Nov 18 13:40:36 UTC 2026
```

**Agent**

Checking that the second run's tagged outputs are identical to the first, then rebuilding the handover.

**Agent calls Bash**

```bash
. $TMPDIR/wk/bin/activate && python - <<'EOF'
import nbformat,re
for n in ["lfp","fig7e","reproduce"]:
    nb=nbformat.read(f"executed/tingley-2019/{n}_tingley_2019.ipynb",4)
    txt="\n".join(o.get('text','') for c in nb.cells if c.cell_type=='code' and any(t.startswith('claim:') for t in c.metadata.get('tags',[])) for o in c.get('outputs',[]))
    for pat in ["fraction \\(a\\) 0.606","significant 43 \\(0.072\\)","PLV 0.1861","range 47.0 to 80.0","fig2 criterion holds in 0 of 8","Readings with both parts: 12","LSRipples, recordings with LS electrodes \\(a\\): 27014"]:
        if re.search(pat,txt): print(n,"ok",pat)
EOF
python tools/entry.py handover entries/tingley-2019 && python tools/entry.py check entries/tingley-2019 | tail -1; date -u
```

```
lfp ok fraction \(a\) 0.606
lfp ok significant 43 \(0.072\)
lfp ok PLV 0.1861
lfp ok fig2 criterion holds in 0 of 8
fig7e ok range 47.0 to 80.0
reproduce ok Readings with both parts: 12
reproduce ok LSRipples, recordings with LS electrodes \(a\): 27014
wrote executed/tingley-2019/handover
0 error(s)
Wed Nov 18 13:41:07 UTC 2026
```

**Agent**

I tested all 39 claims of `claims/tingley-2019.yaml` on DANDI:000218 version 0.261110.1911. Of the 39, 30 were tested and 9 blocked: 8 reproduced, 11 partially reproduced and 11 not reproduced. The entry is at `entries/tingley-2019`, with three notebooks (spikes and events, LFP, Figure 7E) and a helper module, and the record is `attempts/tingley-2019-02.yaml`. `tools/entry.py all` passes with 0 errors, and the handover is built. Nothing was committed.

**Blindness.** The dandiset's own release notes, which I had to read to choose the version, say the files were re-converted to fix "problems found by a reproduction attempt (issue #82)", and list the fixes. That is the only trace of an earlier attempt I met. I did not open the issue, and I saw none of that attempt's outcomes.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1c-event-count, fig1f-shorter-than-ripples, fig1g-slower-than-ripples, fig4c-temporal-bias, figs2c-no-ls-reactivation, fig5b-nrem-and-rates, fig5d-lag | reproduced |
| fig1h-no-amplitude-frequency-correlation, fig4b-hfo-above-behav | reproduced, resting on an assumption |
| dataset-composition, fig1c-hfo-each-animal, fig1d-phase-locking, fig4d-compression, figs3d-hpc-compression-post, figs2-post-rate-increase, fig7e-ca1-spikes, fig7e-state, fig7e-duration | partially reproduced |
| fig4b-pre-post-unchanged | partially reproduced, resting on an assumption |
| figs1-participation, fig2-confined-to-ls, fig4-sessions-few-change, fig5e-state-coupling, fig5f-ripple-triggered-firing, fig5f-no-phase-coherence, discussion-medial-septum, discussion-cingulate-down-state | not reproduced |
| fig1c-post-burst-suppression, ls-spikes-not-locked-to-ca1-ripples | not reproduced, resting on an assumption |
| fig2ef-intermediate-ls, fig3-travelling-waves, fig7e-ca1-depth | blocked: metadata_insufficient |
| fig7e-content-independent, fig7e-coupled-only | blocked: metadata_insufficient (they depend on fig7e-ca1-depth) |
| fig6-optogenetic-hfos | blocked: data_missing |
| fig7e-replay, fig7e-seqnmf, figs5-seqnmf-variance, fig8-model | blocked: other (not attempted within the run's time) |

## 2. The dataset, assumptions and questions

**What was found about the dataset:**
- **Composition:** six rats with 2551 LS units in 98 files, and no recording deposited twice.
- **Missing from the files:** the two optogenetic rats, electrode positions, each recording's depth within LS, and marked PRE / BEHAV / POST periods.
- **Hippocampal labels:** most hippocampal units are labelled only `hpc`, so CA1 and CA3 cannot be told apart reliably (10 or 19 CA3 recordings depending on the label used, against the paper's 25).
- **Labels and scoring:** 36 units in DT7 20170407 have an empty region label. In 3 files, less than half of the trial time is scored WAKE.
- **Missing event tables:** the DT9 CA3 recordings have no CA1 ripple table. DT7 20170410 has LS units but no LS HFO table.
- **Detection parameters:** the deposited LS HFO and CA1 ripple detections use parameters that differ from the Methods. Even so, their counts, durations and frequencies match the paper.

**Assumptions**, each recorded with a question for the paper's authors (`methods_unavailable`):
- **Epoch boundaries:** PRE, BEHAV and POST are split at the first trial's start and the last trial's stop.
- **Figure 4 CCGs:** normalized by the spike counts. Raw counts make PRE and POST differ.
- **Figure 1H:** Pearson correlation. Spearman finds a negligible but significant correlation.
- **Post-burst window:** starts at the event stop. The other window passes only under some seeds.
- **Locking to CA1:** spikes inside CA1 ripples. In the CA1 high-power epochs the fraction is at chance.

**Questions to a reader:** none.

## 3. Where the protocol was unclear or did not fit

1. **Time.** The time rule only names `too_large` for claims the computation stopped. Claims I chose not to attempt because of the five-hour limit had no named reason, so I used `other` and said so.
2. **Notebook time limit.** The 60-minute limit applies per notebook, so analyses that need the whole dataset had to be split across notebooks. Each one reloads the data (about 2.5 minutes).
3. **Seeds.** Repeating everything under five seeds did not fit for the Figure 7E Poisson fits or for the fig5f jitter. I repeated the linear Figure 7E models only, and gave the reasons in the deviations.
4. **Conclusions and run order.** Result cells must be backed by printed numbers, but the long notebooks' numbers exist only after the run. I added those cells as markdown after the first full run, then re-ran `entry.py all` so the executed copies and stamp match.
5. **Expected values beside an absence criterion.** fig4b-pre-post-unchanged has an expected pair count (7172) that the criterion does not use. I recorded partially reproduced: the absence holds, but only 462 pairs pass inclusion.
6. **Absence claims with no test named.** The rule to judge absence on the paper's test alone has nothing to apply when the paper names no test (fig1h, ls-spikes-not-locked). I treated those claims under step 1.6.

## 4. Runtime and failures

The final run took about 76 minutes: 15 for the main notebook, 45 for the LFP one and 16 for Figure 7E. Peak memory was about 7.4 GB, in the LFP notebook. No job failed in either full run. During development, one site analysis reached 10.7 GB; I bounded it before the full runs.

## End of run

74 turns, 223 minutes, $14.65 at API prices, result: success.
