# 000034 · author · run 39708723196

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls; ls claims/000034 paper entries tools
```

```
# Protocol for an attempt

Version: `pilot-10`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim, and it asks a reader for any method detail the file lacks.
- The **verifier** checks the author's work and must not be the author.

[... 579 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000034/10.7554-elife.61834.yaml
```

```
<persisted-output>
Output too large (41.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/9ce68c0c-584d-4d35-b0e9-b0bc67ec6552/tool-results/bfckx8uov.txt

Preview (first 2KB):
# Claims for Buccino, Hurwitz, Garcia, Magland, Siegle, Hurwitz & Hennig (2020), eLife 9:e61834,
# on dandiset 000034.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record, full text from Europe PMC (PMC7704107): main text, figure and
# figure-supplement legends, Materials and methods, the decision letter and author response. The
# one supplementary file is eLife's transparent reporting form, which says "The manuscript does
# not contain any statistical analysis"; so no claim has `statistics`. No PDF of the main text was
# supplied: numbers drawn only in figures (Figure 1, figure supplements 3 and 4; the dots of
# Figure 3, figure supplement 1) could not be read and are not used.
#
# Code read: the notebooks the paper links, in github.com/SpikeInterface/spikeinterface.github.io
# (clone at 657c6d8; the four notebooks were last changed at ee08fb6, 2020-09-29, before
# publication): posts/ensemble-sorting-of-a-neuropixels-recording.ipynb (Figures 1 and 4),
# ground-truth-comparison-and-ensemble-sorting-of-a-synthetic-neuropixels-recording.ipynb
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md docs/design.md docs/archives.md | head -400
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
cat docs/archives.md | sed -n 1,200p
```

```
# Archives

The registry tests papers against data in public archives. So far it reads one,
the DANDI Archive. The protocol is written for any archive. What is particular
to an archive (how its datasets are named, versioned and read) is here, and an
agent is pointed to its archive's section.

A dataset is keyed as `<archive>:<id>` and shown as `<LABEL>:<id>`, for example
`DANDI:000003`. Its files in this repository (`claims/`, `questions/`,
`transcripts/`, the `attempt/` branch, the paper store) are under its folder
name: the identifier alone for DANDI, which the registry began with, and
`<archive>-<id>` for any other archive. `tools/datasets.py` holds the table of
archives and turns one form of a dataset's name into another. The workflows
take a dataset in any of these forms.

## DANDI

- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
[... 77 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/9ce68c0c-584d-4d35-b0e9-b0bc67ec6552/tool-results/bfckx8uov.txt"
}
```

```
1	# Claims for Buccino, Hurwitz, Garcia, Magland, Siegle, Hurwitz & Hennig (2020), eLife 9:e61834,
2	# on dandiset 000034.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
4	# protocol pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read: the version of record, full text from Europe PMC (PMC7704107): main text, figure and
7	# figure-supplement legends, Materials and methods, the decision letter and author response. The
8	# one supplementary file is eLife's transparent reporting form, which says "The manuscript does
9	# not contain any statistical analysis"; so no claim has `statistics`. No PDF of the main text was
10	# supplied: numbers drawn only in figures (Figure 1, figure supplements 3 and 4; the dots of
11	# Figure 3, figure supplement 1) could not be read and are not used.
12	#
13	# Code read: the notebooks the paper links, in github.com/SpikeInterface/spikeinterface.github.io
14	# (clone at 657c6d8; the four notebooks were last changed at ee08fb6, 2020-09-29, before
15	# publication): posts/ensemble-sorting-of-a-neuropixels-recording.ipynb (Figures 1 and 4),
16	# ground-truth-comparison-and-ensemble-sorting-of-a-synthetic-neuropixels-recording.ipynb
17	# (Figures 2 and 3), ensemble-sorting-of-a-neuropixels-recording-2.ipynb (Figure 1, figure
18	# supplement 3) and ensemble-sorting-of-a-3brain-biocam-recording-from-a-retina.ipynb (Figure 1,
19	# figure supplement 4). They hold the sorter runs, the comparisons, the plots and printed counts.
20	# No code was found for Figure 3, figure supplements 1 and 2. The library code read is
[... 651 more lines not kept]
```

**Agent calls Bash**

```bash
ls entries/001453-fouke-2025 claims/001453 questions | head -50; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; cat attempts/001453-fouke-2025-01.yaml | head -150
```

```
claims/001453:
10.1016-j.cub.2025.04.027.yaml

entries/001453-fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt

questions:
000005.yaml
000008.yaml
000009.yaml
000010.yaml
000061.yaml
000582.yaml
001754.yaml
README.md
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,400p attempts/001453-fouke-2025-01.yaml | grep -n -A12 "blocked\|^findings\|^verifications" | head -120; ls schemas; cat questions/README.md; cat questions/000005.yaml | head -40
```

```
49:  outcome: blocked
50:  blocked_by: metadata_insufficient
51-  notes: The numbers come from single representative fish and trials. Fig1-S1.ipynb selects them
52-    by the index of a data folder and a trial number (for example DC folder 29, trial 79), and the
53-    dandiset gives no mapping from those folders to its subjects, nor the original file names.
54-- claim: fig2d-shared-architecture
55:  outcome: blocked
56:  blocked_by: data_missing
57-  notes: The two-photon imaging data are not in the dandiset, which holds only freely swimming
58-    tracking. The GitLab repository the paper names for "all behavioral and imaging data" holds
59-    notebooks only, and no other dandiset of this lab or paper was found on the archive.
60-- claim: fig2g-dsi-similar
61:  outcome: blocked
62:  blocked_by: data_missing
63-  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
64-- claim: fig2h-fewer-motion-responsive
65:  outcome: blocked
66:  blocked_by: data_missing
67-  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
68-- claim: fig2k-more-monocular
[... 101 more lines not kept]
```

**Agent**

Read the protocol, claims file and example formats. Now listing dandiset 000034 versions and assets.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000034/versions/ | python -m json.tool | head -60; curl -s "https://api.dandiarchive.org/api/dandisets/000034/versions/draft/assets/?page_size=100" | python -c "import json,sys; d=json.load(sys.stdin); print(d['count']); [print(a['path'],a['size'],a['asset_id'],a['modified']) for a in d['results']]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000034/versions/0.211030.0713/assets/?page_size=100" | python -c "import json,sys; d=json.load(sys.stdin); [print(a['path'],a['size'],a['asset_id']) for a in d['results']]"; curl -s https://api.dandiarchive.org/api/dandisets/000034/versions/0.211030.0713/ | python -m json.tool | head -150; python -c "import pynwb, remfile, h5py; print(pynwb.__version__)"; nproc; free -g; nvidia-smi 2>&1 | head -2; which matlab
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q explore && . explore/bin/activate && uv pip install -q pynwb remfile h5py dandi numpy pandas scipy 2>&1 | tail -2; python -c "import pynwb; print(pynwb.__version__)"
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/entry.py; grep -n "def \|sanity\|claim:" tools/entry.py | head -80
```

```
4.2.0
Shell cwd was reset to
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
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
- each notebook has a cell tagged `sanity` that prints what was loaded;
[... 78 more lines not kept]
```

**Agent**

Now listing the contents of all six files (metadata only, streamed).

**Agent calls Bash**

```bash
cd $TMPDIR && . explore/bin/activate && cat > insp.py <<'EOF'
import h5py, remfile, requests, sys
V="0.211030.0713"
r=requests.get(f"https://api.dandiarchive.org/api/dandisets/000034/versions/{V}/assets/?page_size=100").json()
for a in r['results']:
    url=f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
    s3=requests.head(url,allow_redirects=True).url
    f=h5py.File(remfile.File(s3),'r')
    print("=====",a['path'])
    def vis(name,obj):
        if isinstance(obj,h5py.Dataset):
            print(" ",name,obj.shape,obj.dtype,obj.chunks,obj.compression, dict((k,(v if not hasattr(v,'shape') or v.size<5 else v.shape)) for k,v in obj.attrs.items() if k not in('namespace','object_id','neurodata_type')))
        else:
            att={k:v for k,v in obj.attrs.items() if k not in('namespace','object_id')}
            print(" G",name,att)
    f.visititems(vis)
    for k in ['session_description','identifier','session_start_time']:
        print(k, f[k][()] if k in f else None)
EOF
python insp.py 2>&1 | grep -v "^  general/" | head -300
```

```
Exit code 143
Command timed out after 20m 0s
```

**Agent**

The full listing timed out at 20 minutes. Retrying one file at a time, smallest first, with unbuffered output.

**Agent calls Bash**

```bash
cd $TMPDIR && . explore/bin/activate && cat > insp1.py <<'EOF'
import h5py, remfile, requests, sys, time
V="0.211030.0713"
aid=sys.argv[1]
url=f"https://api.dandiarchive.org/api/assets/{aid}/download/"
s3=requests.head(url,allow_redirects=True).url
t=time.time()
f=h5py.File(remfile.File(s3),'r')
def vis(name,obj):
    if name.startswith('specifications'): return
    if isinstance(obj,h5py.Dataset):
        print(" ",name,obj.shape,obj.dtype,obj.chunks,obj.compression, {k:v for k,v in obj.attrs.items() if k in ('unit','conversion','rate','starting_time','resolution','description')},flush=True)
    else:
        print(" G",name,{k:v for k,v in obj.attrs.items() if k not in('namespace','object_id')},flush=True)
f.visititems(vis)
print(time.time()-t)
EOF
timeout 600 python -u insp1.py af1745f6-e14a-473a-987d-cef7e29a3956 2>&1 | head -150
```

```
G acquisition {}
 G analysis {}
  file_create_date (1,) object None None {}
 G general {}
 G general/subject {'neurodata_type': 'Subject'}
  general/subject/age () object None None {}
  general/subject/description () object None None {}
  general/subject/sex () object None None {}
  general/subject/species () object None None {}
  general/subject/subject_id () object None None {}
  identifier () object None None {}
 G processing {}
  session_description () object None None {}
  session_start_time () object None None {}
 G stimulus {}
 G stimulus/presentation {}
 G stimulus/templates {}
  timestamps_reference_time () object None None {}
 G units {'colnames': array(['spike_times'], dtype=object), 'description': 'Autogenerated by NWBFile', 'neurodata_type': 'Units'}
  units/id (258,) int32 None None {}
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . explore/bin/activate && for a in c696fc2b-d2e6-4e27-8775-01657193c4a2 3e0d4539-902e-46b4-9cfb-119e0f69fbd0; do echo "#### $a"; timeout 900 python -u insp1.py $a 2>&1 | grep -v "^  general/\(extracellular_ephys/[^/]*/\)\?electrodes/\|^ G general/extracellular_ephys/\(probe\|shank\|ch\)" | head -120; done
```

```
#### c696fc2b-d2e6-4e27-8775-01657193c4a2
 G acquisition {}
 G analysis {}
  file_create_date (1,) object None None {}
 G general {}
 G general/subject {'neurodata_type': 'Subject'}
  general/subject/age () object None None {}
  general/subject/description () object None None {}
  general/subject/sex () object None None {}
  general/subject/species () object None None {}
  general/subject/subject_id () object None None {}
  identifier () object None None {}
 G processing {}
  session_description () object None None {}
  session_start_time () object None None {}
 G stimulus {}
 G stimulus/presentation {}
 G stimulus/templates {}
  timestamps_reference_time () object None None {}
 G units {'colnames': array(['spike_times'], dtype=object), 'description': 'Autogenerated by NWBFile', 'neurodata_type': 'Units'}
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . explore/bin/activate && cat > insp2.py <<'EOF'
import h5py, remfile, requests, sys, time
aid=sys.argv[1]
s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
t=time.time()
f=h5py.File(remfile.File(s3),'r')
print(list(f.keys()), time.time()-t, flush=True)
for g in ['acquisition','processing','analysis','units']:
    if g in f:
        print(g, list(f[g].keys()), flush=True)
for k in f['acquisition']:
    o=f['acquisition'][k]
    print(k, dict(o.attrs), flush=True)
    for kk in o: 
        d=o[kk]; print('  ',kk, getattr(d,'shape',None), getattr(d,'dtype',None), getattr(d,'chunks',None), dict(d.attrs), flush=True)
    if 'starting_time' in o: print('  start', o['starting_time'][()], dict(o['starting_time'].attrs))
if 'units' in f:
    u=f['units']; print('units', dict(u.attrs), {k:u[k].shape for k in u}, flush=True)
for k in ['session_description','identifier','session_start_time']: print(k, f[k][()])
for k in f['general/subject']: print('subject',k,f['general/subject'][k][()])
print('elec cols', list(f['general/extracellular_ephys/electrodes'].keys()) if 'electrodes' in f['general/extracellular_ephys'] else None)
print(time.time()-t)
EOF
for a in 9822a813-0dec-4d07-810b-1c13341c168d 76c211c2-d588-48a7-a4c8-ea103ff0570a 6d94dcf4-0b38-4323-8250-04fdc7039a66; do echo "#### $a"; timeout 1500 python -u insp2.py $a 2>&1 | head -60; done
```

```
#### 9822a813-0dec-4d07-810b-1c13341c168d
['acquisition', 'analysis', 'file_create_date', 'general', 'identifier', 'processing', 'session_description', 'session_start_time', 'specifications', 'stimulus', 'timestamps_reference_time'] 1.1234581470489502
acquisition ['ElectricalSeries']
processing []
analysis []
ElectricalSeries {'comments': 'Generated from SpikeInterface::NwbRecordingExtractor', 'description': 'acquisition_description', 'namespace': 'core', 'neurodata_type': 'ElectricalSeries', 'object_id': '5257175e-a807-4061-8012-250bc61d78ef'}
   data (3148820, 1024) uint16 (12301, 1) {'conversion': np.float64(1e-06), 'resolution': np.float64(-1.0), 'unit': 'volts'}
   electrodes (1024,) int64 None {'description': 'electrode_table_region', 'namespace': 'hdmf-common', 'neurodata_type': 'DynamicTableRegion', 'object_id': '5346cfc4-26b4-464e-992d-e94b03187a39', 'table': <HDF5 object reference>}
   starting_time () float64 None {'rate': np.float64(23199.090358491783), 'unit': 'seconds'}
  start 0.0 {'rate': np.float64(23199.090358491783), 'unit': 'seconds'}
session_description b'no description'
identifier b'57e10c71-c0d2-488a-a34d-13d6dcaf7af1'
session_start_time b'2020-08-07T09:42:57.434275+01:00'
subject age b'P29'
subject description b'stim2_smallarray_fullfield'
subject sex b''
subject species b'mus musculus'
subject subject_id b'P29_16_05_14_retina02_left'
elec cols ['filtering', 'group', 'group_name', 'id', 'imp', 'location', 'rel_x', 'rel_y', 'x', 'y', 'z']
1.2897684574127197
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . explore/bin/activate && cat > insp3.py <<'EOF'
import h5py, remfile, requests, time, numpy as np
def op(aid):
    s3=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
    return h5py.File(remfile.File(s3),'r')
for aid in ['af1745f6-e14a-473a-987d-cef7e29a3956','c696fc2b-d2e6-4e27-8775-01657193c4a2','3e0d4539-902e-46b4-9cfb-119e0f69fbd0']:
    f=op(aid)
    print(aid, {k:f['general/subject'][k][()] for k in f['general/subject']}, f['session_start_time'][()], f['identifier'][()], f['session_description'][()])
    if 'units' in f:
        st=f['units/spike_times'][:]; idx=f['units/spike_times_index'][:]; ids=f['units/id'][:]
        print(' ids', ids.min(), ids.max(), len(np.unique(ids)), 'times', st.min(), st.max(), 'sorted per unit', all(np.all(np.diff(s)>=0) for s in np.split(st, idx[:-1])))
        print(' frames*30000 integer?', np.abs(st*30000-np.round(st*30000)).max())
        print(' first ids', ids[:30])
    else:
        e=f['general/extracellular_ephys/electrodes']
        print(' loc', np.unique(e['location'][:]), 'filtering', np.unique(e['filtering'][:]))
        print(' x', np.unique(e['rel_x'][:]), 'y range', e['rel_y'][:].min(), e['rel_y'][:].max(), 'ids', e['id'][:][:10], e['id'][:].max())
        d=f['acquisition/ElectricalSeries/data']
        t=time.time(); x=d[0:52736,:]; print(' read 1.76 s all ch', time.time()-t, x.min(), x.max(), x.std())
EOF
python -u insp3.py
```

```
af1745f6-e14a-473a-987d-cef7e29a3956 {'age': b'', 'description': b'', 'sex': b'', 'species': b'mus musculus', 'subject_id': b'mouse412804'} b'2020-08-24T15:55:42.004284+02:00' b'2bddd311-a20a-4f69-aa12-14bcf21bca46' b'No description'
 ids 0 563 258 times 0.0031666666666666666 899.9996333333333 sorted per unit True
 frames*30000 integer? 1.862645149230957e-09
 first ids [ 0  2  3  4  5  8  9 10 11 12 13 15 16 18 19 20 25 26 27 28 30 32 33 34
 36 37 38 41 43 44]
c696fc2b-d2e6-4e27-8775-01657193c4a2 {'age': b'', 'description': b'', 'sex': b'', 'species': b'mus musculus', 'subject_id': b'mouse412804'} b'2020-08-24T15:55:43.012201+02:00' b'8c8ed690-70a9-4f31-9f74-765b69cf6ce3' b'No description'
 ids 0 573 319 times 0.0031666666666666666 899.9996333333333 sorted per unit True
 frames*30000 integer? 1.862645149230957e-09
 first ids [ 0  2  3  4  5  7  8  9 11 13 15 16 17 18 19 20 22 23 24 25 26 27 28 30
 31 32 33 34 35 37]
3e0d4539-902e-46b4-9cfb-119e0f69fbd0 {'age': b'', 'description': b'', 'sex': b'', 'species': b'mus musculus', 'subject_id': b'mouse412804'} b'2020-08-03T11:57:32.640004+01:00' b'dbb9c71a-8357-4597-9091-67c89330fab0' b'no description'
 loc [b'unknown'] filtering [b'none']
 x [11. 27. 43. 59.] y range 20.0 2840.0 ids [0 1 2 3 4 5 6 7 8 9] 247
 read 1.76 s all ch 49.77127385139465 -3441 1528 79.31065057494337
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.13 sc && . sc/bin/activate && uv pip install spikecomparison==0.2.6 spikeextractors==0.8.4 2>&1 | tail -15; python -c "import spikecomparison, spikeextractors; print(spikecomparison.__version__, spikeextractors.__version__)"
```

```
Exit code 1
 + pandas==3.0.6
 + python-dateutil==3.0.0
 + requests==2.34.2
 + scikit-learn==1.9.1
 + scipy==1.18.1
 + six==1.17.0
 + spikecomparison==0.2.6
 + spikeextractors==0.8.4
 + spikefeatures==0.1.2
 + spikemetrics==0.2.4
 + spikesorters==0.4.2
 + spiketoolkit==0.7.1
 + threadpoolctl==3.7.0
 + tzdata==2026.5
 + urllib3==2.8.0
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import spikecomparison, spikeextractors; print(spikecomparison.__version__, spikeextractors.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sc/bin/activate && uv pip install -q spikecomparison==0.2.6 spikeextractors==0.8.4 spiketoolkit==0.6.3 spikesorters==0.3.3 setuptools 2>&1 | tail -5; python -c "
import spikecomparison, spikeextractors, spiketoolkit, spikesorters; print(spikecomparison.__version__, spikeextractors.__version__, spiketoolkit.__version__, spikesorters.__version__)
import numpy as np, spikeextractors as se, spikecomparison as sc
s1=se.NumpySortingExtractor(); s1.set_times_labels(np.array([10,100,1000,5000]), np.array([0,0,1,1])); s1.set_sampling_frequency(30000)
s2=se.NumpySortingExtractor(); s2.set_times_labels(np.array([12,100,1003,5000]), np.array([5,5,7,7])); s2.set_sampling_frequency(30000)
c=sc.compare_two_sorters(s1,s2); print(c.hungarian_match_12, c.agreement_scores)
"; uv pip list 2>/dev/null | grep -i "numpy\|pandas\|networkx\|scipy"
```

```
/tmp/claude-1001/sc/lib/python3.13/site-packages/spikemetrics/metrics.py:796: SyntaxWarning: invalid escape sequence '\s'
  NN_hit(X) = 1/k \sum_i=1^k |{x in A such that ith closest neighbor is in X}| / |A|
Traceback (most recent call last):
  File "<string>", line 6, in <module>
    c=sc.compare_two_sorters(s1,s2); print(c.hungarian_match_12, c.agreement_scores)
  File "/tmp/claude-1001/sc/lib/python3.13/site-packages/spikecomparison/symmetricsortingcomparison.py", line 154, in compare_two_sorters
    return SymmetricSortingComparison(sorting1=sorting1, sorting2=sorting2, sorting1_name=sorting1_name,
                                      sorting2_name=sorting2_name, delta_time=delta_time,
                                      sampling_frequency=sampling_frequency,
                                      match_score=match_score, chance_score=chance_score,
                                      n_jobs=n_jobs, verbose=verbose)
  File "/tmp/claude-1001/sc/lib/python3.13/site-packages/spikecomparison/symmetricsortingcomparison.py", line 16, in __init__
    BaseTwoSorterComparison.__init__(self, sorting1, sorting2, sorting1_name=sorting1_name,
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                     sorting2_name=sorting2_name,
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                     delta_time=delta_time, sampling_frequency=sampling_frequency,
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                     match_score=match_score, chance_score=chance_score,
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sc/bin/activate && python -W ignore -c "
import numpy as np; np.float=float; np.int=int; np.bool=bool
import spikeextractors as se, spikecomparison as sc
s1=se.NumpySortingExtractor(); s1.set_times_labels(np.array([10,100,1000,5000,7000]), np.array([0,0,1,1,2])); s1.set_sampling_frequency(30000)
s2=se.NumpySortingExtractor(); s2.set_times_labels(np.array([12,100,1003,5000,7020]), np.array([5,5,7,7,8])); s2.set_sampling_frequency(30000)
c=sc.compare_two_sorters(s1,s2); print(c.hungarian_match_12); print(c.agreement_scores); print(c.get_matching())
m=sc.compare_multiple_sorters([s1,s2,s2],['a','b','c']); print(m.get_agreement_sorting(minimum_agreement_count=1).get_unit_ids())
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 3, in <module>
    import spikeextractors as se, spikecomparison as sc
  File "/tmp/claude-1001/sc/lib/python3.13/site-packages/spikecomparison/__init__.py", line 3, in <module>
    from .comparisontools import (count_matching_events, compute_agreement_score, count_match_spikes,
            make_agreement_scores, make_possible_match, make_best_match, make_hungarian_match,
            do_score_labels, compare_spike_trains, do_confusion_matrix, do_count_score, compute_performence)
  File "/tmp/claude-1001/sc/lib/python3.13/site-packages/spikecomparison/comparisontools.py", line 6, in <module>
    import pandas as pd
  File "/tmp/claude-1001/sc/lib/python3.13/site-packages/pandas/__init__.py", line 46, in <module>
    from pandas.core.api import (
    ...<61 lines>...
    )
  File "/tmp/claude-1001/sc/lib/python3.13/site-packages/pandas/core/api.py", line 23, in <module>
    from pandas.core.algorithms import (
    ...<2 lines>...
    )
  File "/tmp/claude-1001/sc/lib/python3.13/site-packages/pandas/core/algorithms.py", line 83, in <module>
    from pandas.core.array_algos.take import take_nd
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sc/bin/activate && python -W ignore -c "
import numpy as np
if not hasattr(np,'float'): np.float=float
import spikeextractors as se, spikecomparison as sc
s1=se.NumpySortingExtractor(); s1.set_times_labels(np.array([10,100,1000,5000,7000]), np.array([0,0,1,1,2])); s1.set_sampling_frequency(30000)
s2=se.NumpySortingExtractor(); s2.set_times_labels(np.array([12,100,1003,5000,7020]), np.array([5,5,7,7,8])); s2.set_sampling_frequency(30000)
c=sc.compare_two_sorters(s1,s2); print(c.hungarian_match_12); print(c.agreement_scores); print(c.get_matching())
m=sc.compare_multiple_sorters([s1,s2,s2],['a','b','c']); print(m.get_agreement_sorting(minimum_agreement_count=1).get_unit_ids())
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 7, in <module>
    c=sc.compare_two_sorters(s1,s2); print(c.hungarian_match_12); print(c.agreement_scores); print(c.get_matching())
  File "/tmp/claude-1001/sc/lib/python3.13/site-packages/spikecomparison/symmetricsortingcomparison.py", line 154, in compare_two_sorters
    return SymmetricSortingComparison(sorting1=sorting1, sorting2=sorting2, sorting1_name=sorting1_name,
                                      sorting2_name=sorting2_name, delta_time=delta_time,
                                      sampling_frequency=sampling_frequency,
                                      match_score=match_score, chance_score=chance_score,
                                      n_jobs=n_jobs, verbose=verbose)
  File "/tmp/claude-1001/sc/lib/python3.13/site-packages/spikecomparison/symmetricsortingcomparison.py", line 16, in __init__
    BaseTwoSorterComparison.__init__(self, sorting1, sorting2, sorting1_name=sorting1_name,
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                     sorting2_name=sorting2_name,
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                     delta_time=delta_time, sampling_frequency=sampling_frequency,
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                     match_score=match_score, chance_score=chance_score,
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                     n_jobs=n_jobs, verbose=verbose)
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sc/bin/activate && grep -rhoE "np\.(float|int|bool|Inf|NaN|NAN|PINF|object|str|long|unicode|product|cumproduct|alltrue|sometrue|in1d|trapz|row_stack|asfarray)\b[^_]" sc/lib/python3.13/site-packages/{spikecomparison,spikeextractors}/ | sort | uniq -c
```

```
1 np.Inf:
      1 np.bool)
      3 np.float)
      4 np.float,
      3 np.in1d(
      5 np.int)
      4 np.int,
      1 np.product(
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sc/bin/activate && python -W ignore -c "
import numpy as np
for name,val in [('float',float),('int',int),('Inf',np.inf),('product',np.prod),('in1d',np.isin)]:
    if name not in np.__dict__ : setattr(np,name,val)
import spikeextractors as se, spikecomparison as sc
s1=se.NumpySortingExtractor(); s1.set_times_labels(np.array([10,100,1000,5000,7000]), np.array([0,0,1,1,2])); s1.set_sampling_frequency(30000)
s2=se.NumpySortingExtractor(); s2.set_times_labels(np.array([12,100,1003,5000,7020]), np.array([5,5,7,7,8])); s2.set_sampling_frequency(30000)
c=sc.compare_two_sorters(s1,s2); print(c.hungarian_match_12); print(c.agreement_scores); 
m=sc.compare_multiple_sorters([s1,s2,s2],['a','b','c']); a=m.get_agreement_sorting(minimum_agreement_count=1); print(a.get_unit_ids(), [a.get_unit_property(u,'agreement_number') for u in a.get_unit_ids()])
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 9, in <module>
    m=sc.compare_multiple_sorters([s1,s2,s2],['a','b','c']); a=m.get_agreement_sorting(minimum_agreement_count=1); print(a.get_unit_ids(), [a.get_unit_property(u,'agreement_number') for u in a.get_unit_ids()])
  File "/tmp/claude-1001/sc/lib/python3.13/site-packages/spikecomparison/multisortingcomparison.py", line 342, in compare_multiple_sorters
    return MultiSortingComparison(sorting_list=sorting_list, name_list=name_list, delta_time=delta_time,
                                  match_score=match_score, chance_score=chance_score, n_jobs=n_jobs,
                                  spiketrain_mode=spiketrain_mode, sampling_frequency=sampling_frequency,
                                  verbose=verbose)
  File "/tmp/claude-1001/sc/lib/python3.13/site-packages/spikecomparison/multisortingcomparison.py", line 27, in __init__
    self._do_agreement()
    ~~~~~~~~~~~~~~~~~~^^
  File "/tmp/claude-1001/sc/lib/python3.13/site-packages/spikecomparison/multisortingcomparison.py", line 180, in _do_agreement
    sorter_unit = int(node.split('_')[1])
ValueError: invalid literal for int() with base 10: '5.0'
0    5.0
1    7.0
2   -1.0
dtype: float64
     5    7    8
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "def make_hungarian_match" -A45 sc/lib/python3.13/site-packages/spikecomparison/comparisontools.py; sed -n 150,200p sc/lib/python3.13/site-packages/spikecomparison/multisortingcomparison.py
```

```
309:def make_hungarian_match(agreement_scores, min_score):
310-    """
311-    Given an agreement matrix and a min_score threshold.
312-    return the "optimal" match with the "hungarian" algo.
313-    This use internally the scipy.optimze.linear_sum_assignment implementation.
314-    
315-    Parameters
316-    ----------
317-    agreement_scores: pd.DataFrame
318-    
319-    min_score: float
320-    
321-    
322-    Returns
323-    -----------
324-    hungarian_match_12: pd.Series
325-    
326-    hungarian_match_21: pd.Series
327-    
328-    """
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sc/bin/activate && uv pip install -q "pandas==2.2.3" 2>&1|tail -2; python -W ignore -c "
import numpy as np
for name,val in [('float',float),('int',int),('Inf',np.inf),('product',np.prod),('in1d',np.isin)]:
    if name not in np.__dict__ : setattr(np,name,val)
import spikeextractors as se, spikecomparison as sc
s1=se.NumpySortingExtractor(); s1.set_times_labels(np.array([10,100,1000,5000,7000]), np.array([0,0,1,1,2])); s1.set_sampling_frequency(30000)
s2=se.NumpySortingExtractor(); s2.set_times_labels(np.array([12,100,1003,5000,7020]), np.array([5,5,7,7,8])); s2.set_sampling_frequency(30000)
c=sc.compare_two_sorters(s1,s2); print(c.hungarian_match_12); print(c.agreement_scores); 
m=sc.compare_multiple_sorters([s1,s2,s2],['a','b','c']); a=m.get_agreement_sorting(minimum_agreement_count=1); print(a.get_unit_ids(), [a.get_unit_property(u,'agreement_number') for u in a.get_unit_ids()])
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 9, in <module>
    m=sc.compare_multiple_sorters([s1,s2,s2],['a','b','c']); a=m.get_agreement_sorting(minimum_agreement_count=1); print(a.get_unit_ids(), [a.get_unit_property(u,'agreement_number') for u in a.get_unit_ids()])
  File "/tmp/claude-1001/sc/lib/python3.13/site-packages/spikecomparison/multisortingcomparison.py", line 342, in compare_multiple_sorters
    return MultiSortingComparison(sorting_list=sorting_list, name_list=name_list, delta_time=delta_time,
                                  match_score=match_score, chance_score=chance_score, n_jobs=n_jobs,
                                  spiketrain_mode=spiketrain_mode, sampling_frequency=sampling_frequency,
                                  verbose=verbose)
  File "/tmp/claude-1001/sc/lib/python3.13/site-packages/spikecomparison/multisortingcomparison.py", line 27, in __init__
    self._do_agreement()
    ~~~~~~~~~~~~~~~~~~^^
  File "/tmp/claude-1001/sc/lib/python3.13/site-packages/spikecomparison/multisortingcomparison.py", line 180, in _do_agreement
    sorter_unit = int(node.split('_')[1])
ValueError: invalid literal for int() with base 10: '5.0'
0    5.0
1    7.0
2   -1.0
dtype: float64
     5    7    8
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "class NwbSortingExtractor" -A80 sc/lib/python3.13/site-packages/spikeextractors/extractors/nwbextractors/nwbextractors.py | grep -n "sampling\|rate\|spike_times\|int(\|round\|time_to_frame\|def " | head -40; grep -n "def time_to_frame" -A8 sc/lib/python3.13/site-packages/spikeextractors/baseextractor.py sc/lib/python3.13/site-packages/spikeextractors/sortingextractor.py | head -20
```

```
8:584-    def __init__(self, file_path, electrical_series=None, sampling_frequency=None):
21:597-            if sampling_frequency is None:
23:599-                # important to know the sampling_frequency
32:608-                # get rate
33:609-                if es.rate is not None:
34:610-                    self._sampling_frequency = es.rate
36:612-                    self._sampling_frequency = 1 / (es.timestamps[1] - es.timestamps[0])
38:614-                self._sampling_frequency = sampling_frequency
47:623-                if item == 'spike_times':
64:640-                    'start_frame': self.time_to_frame(row['start_time']),
65:641-                    'end_frame': self.time_to_frame(row['stop_time'])}
68:644-                        'sampling_frequency': sampling_frequency}
70:646-    def get_unit_ids(self):
81:657-            unit_ids = [int(i) for i in nwbfile.units.id[:]]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 655,700p sc/lib/python3.13/site-packages/spikeextractors/extractors/nwbextractors/nwbextractors.py; grep -rn "def time_to_frame" -A10 sc/lib/python3.13/site-packages/spikeextractors/*.py | head -30
```

```
with NWBHDF5IO(self._path, 'r') as io:
            nwbfile = io.read()
            unit_ids = [int(i) for i in nwbfile.units.id[:]]
        return unit_ids

    @check_valid_unit_id
    def get_unit_spike_train(self, unit_id, start_frame=None, end_frame=None):
        start_frame, end_frame = self._cast_start_end_frame(start_frame, end_frame)
        if start_frame is None:
            start_frame = 0
        if end_frame is None:
            end_frame = np.Inf
        check_nwb_install()
        with NWBHDF5IO(self._path, 'r') as io:
            nwbfile = io.read()
            # chosen unit and interval
            times = nwbfile.units['spike_times'][list(nwbfile.units.id[:]).index(unit_id)][:]
            # spike times are measured in samples
            frames = self.time_to_frame(times)
        return frames[(frames > start_frame) & (frames < end_frame)]
[... 57 more lines not kept]
```

**Agent**

The loader uses `round(t × fs)`, with fs taken from the recording (30 kHz) because the curated files carry no rate. Computing the pairwise curator comparison now.

**Agent calls Bash**

```bash
cd $TMPDIR && . sc/bin/activate && uv pip install -q remfile h5py requests && python -W ignore -c "
import numpy as np, h5py, remfile, requests
for name,val in [('float',float),('int',int),('Inf',np.inf),('product',np.prod),('in1d',np.isin)]:
    if name not in np.__dict__ : setattr(np,name,val)
import spikeextractors as se, spikecomparison as sc
def load(aid):
    s3=requests.head(f'https://api.dandiarchive.org/api/assets/{aid}/download/',allow_redirects=True).url
    f=h5py.File(remfile.File(s3),'r'); st=f['units/spike_times'][:]; idx=f['units/spike_times_index'][:]; ids=f['units/id'][:]
    s=se.NumpySortingExtractor(); fr=[]; lab=[]
    for u,tr in zip(ids,np.split(st,idx[:-1])):
        x=np.round(tr*30000).astype(int); x=x[x>0]; fr.append(x); lab.append(np.full(len(x),u))
    s.set_times_labels(np.concatenate(fr),np.concatenate(lab)); s.set_sampling_frequency(30000.); return s
c1=load('af1745f6-e14a-473a-987d-cef7e29a3956'); c2=load('c696fc2b-d2e6-4e27-8775-01657193c4a2')
c=sc.compare_two_sorters(c1,c2,'C1','C2')
m=(c.hungarian_match_12!=-1).sum(); n1=len(c1.get_unit_ids()); n2=len(c2.get_unit_ids())
print(n1,n2,m,n1+n2-m, m/(n1+n2-m))
sc_=c.agreement_scores.values; print('scores of matched', np.percentile([c.agreement_scores.loc[a,b] for a,b in c.hungarian_match_12.items() if b!=-1],[0,5,50]))
print('identical spike trains', sum(np.array_equal(c1.get_unit_spike_train(a), c2.get_unit_spike_train(int(b))) for a,b in c.hungarian_match_12.items() if b!=-1))
print('same id pairs', sum(int(a)==int(b) for a,b in c.hungarian_match_12.items() if b!=-1))
for th in [0.3,0.4,0.5,0.6,0.7,0.8]:
    cc=sc.compare_two_sorters(c1,c2,match_score=th); mm=(cc.hungarian_match_12!=-1).sum(); print(th,mm,n1+n2-mm)
"
```

```
258 319 226 351 0.6438746438746439
scores of matched [0.50998411 0.71341789 1.        ]
identical spike trains 186
same id pairs 181
0.3 231 346
0.4 229 348
0.5 226 351
0.6 222 355
0.7 216 361
0.8 208 369
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sc/bin/activate && uv pip install -q scipy && python -W ignore -u -c "
import numpy as np, h5py, remfile, requests, time
from scipy.signal import butter, sosfiltfilt
def op(aid):
    s3=requests.head(f'https://api.dandiarchive.org/api/assets/{aid}/download/',allow_redirects=True).url
    return h5py.File(remfile.File(s3),'r')
f=op('3e0d4539-902e-46b4-9cfb-119e0f69fbd0'); t=time.time()
N=26368*2; x=f['acquisition/ElectricalSeries/data'][0:N,:].astype(float); print('read',time.time()-t)
sos=butter(3,[300,6000],btype='band',fs=30000,output='sos'); y=sosfiltfilt(sos,x,axis=0); y-=np.median(y,axis=1,keepdims=True)
c=op('af1745f6-e14a-473a-987d-cef7e29a3956'); st=c['units/spike_times'][:]; idx=c['units/spike_times_index'][:]
lags=np.arange(-45,46)
best=[];amp0=[];ampsh=[]
rng=np.random.default_rng(0)
for tr in np.split(st,idx[:-1]):
    fr=np.round(tr*30000).astype(int); fr=fr[(fr>100)&(fr<N-100)]
    if len(fr)<5: continue
    a=np.array([(-y[fr+L]).mean(0).max() for L in lags]); best.append(lags[a.argmax()]); amp0.append(a[lags==0][0])
    sh=np.sort(rng.integers(100,N-100,len(fr))); ampsh.append((-y[sh]).mean(0).max())
best=np.array(best); print('units',len(best),'best lag median',np.median(best), 'frac |lag|<=3', np.mean(np.abs(best)<=3), np.percentile(best,[10,25,75,90]))
print('amp at 0 median',np.median(amp0),'random times median',np.median(ampsh))
"
```

```
read 48.47561955451965
units 84 best lag median 0.0 frac |lag|<=3 0.8809523809523809 [-1.7 -1.   0.   2.7]
amp at 0 median 454.57978435218956 random times median 55.993913673502576
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . sc/bin/activate && python -W ignore -u -c "
import numpy as np, h5py, remfile, requests, time
def op(aid):
    s3=requests.head(f'https://api.dandiarchive.org/api/assets/{aid}/download/',allow_redirects=True).url
    return h5py.File(remfile.File(s3),'r')
for aid,n in [('9822a813-0dec-4d07-810b-1c13341c168d',12301),('76c211c2-d588-48a7-a4c8-ea103ff0570a',7911),('6d94dcf4-0b38-4323-8250-04fdc7039a66',18750)]:
    f=op(aid); d=f['acquisition/ElectricalSeries/data']; t=time.time(); x=d[0:n,:]; print(aid,'read',round(time.time()-t,1), x.dtype, x.min(), x.max(), np.median(x), np.median(x.std(0)), 'nconst ch', (x.std(0)==0).sum())
    e=f['general/extracellular_ephys/electrodes']; print('  rel_x', np.unique(e['rel_x'][:])[:8], len(np.unique(e['rel_x'][:])), 'rel_y', e['rel_y'][:].min(), e['rel_y'][:].max(), 'loc', np.unique(e['location'][:])[:3])
"
```

```
9822a813-0dec-4d07-810b-1c13341c168d read 136.9 uint16 1660 4096 2049.0 9.59652965485699 nconst ch 5
  rel_x [1344. 1386. 1428. 1470. 1512. 1554. 1596. 1638.] 32 rel_y 1344.0 2646.0 loc [b'unknown']
76c211c2-d588-48a7-a4c8-ea103ff0570a read 72.4 float64 -531.18 821.3399999999999 332.28 15.867419073345932 nconst ch 0
  rel_x [11. 27. 43. 59.] 4 rel_y 20.0 3840.0 loc [b'unknown']
6d94dcf4-0b38-4323-8250-04fdc7039a66 read 84.9 float32 -620.808 216.87852 1.1107891 18.26095 nconst ch 0
  rel_x [-24.  -8.   8.  24.] 4 rel_y -1910.0 1910.0 loc [b'unknown']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.13 sorters && . sorters/bin/activate && for p in tridesclous==1.6.0 herdingspikes==0.3.7 spyking-circus==0.9.7; do echo "## $p"; timeout 600 uv pip install -q $p 2>&1 | tail -4; done; which matlab mpiexec nvcc 2>&1
```

```
Exit code 1
## tridesclous==1.6.0
## herdingspikes==0.3.7
[tool.uv.extra-build-dependencies]
herdingspikes = ["numpy"]

or `uv pip install numpy` into the environment and re-run with `--no-build-isolation`.
## spyking-circus==0.9.7
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
for s in ['entry','attempt']:
    d=json.load(open(f'schemas/{s}.schema.json'))
    print(s, json.dumps(d)[:6000]); print()
EOF
```

```
entry {"$schema": "https://json-schema.org/draft/2020-12/schema", "title": "An entry: a directory of notebooks with its metadata (entry.yaml)", "description": "Draft. To be revised after the pilot.", "type": "object", "additionalProperties": false, "required": ["schema_version", "name", "type", "title", "description", "license", "notebooks", "related"], "properties": {"schema_version": {"const": 1}, "name": {"description": "Unique across the registry, and the name of the entry's directory.", "type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$", "maxLength": 100}, "type": {"enum": ["orientation", "reproduction", "analysis"]}, "title": {"type": "string", "minLength": 1, "maxLength": 300}, "description": {"type": "string", "minLength": 1}, "license": {"description": "SPDX identifier.", "type": "string"}, "notebooks": {"type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["path"], "properties": {"path": {"type": "string", "pattern": "\\.ipynb$"}, "title": {"type": "string"}, "runtime_minutes": {"description": "Roughly how long it takes to run.", "type": "integer", "minimum": 1}}}}, "helpers": {"description": "Python modules in the entry that the notebooks import.", "type": "array", "items": {"type": "string", "pattern": "\\.py$"}}, "related": {"type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["id", "relation"], "properties": {"id": {"description": "A dataset as <archive>:<id>[/<version>] (dandi:000003/0.220126.1855), doi:<doi>, or entry:<name>.", "type": "string", "pattern": "^(dandi:[0-9]{6}(/.+)?|doi:10\\.[0-9]{4,9}/.+|entry:[a-z0-9]+(-[a-z0-9]+)*|[a-z][a-z0-9-]*:[^\\s/]+(/\\S+)?)$"}, "relation": {"enum": ["uses_data", "reproduces", "derived_from", "references"]}}}}}}

attempt {"$schema": "https://json-schema.org/draft/2020-12/schema", "title": "One attempt at reproducing the claims of a target", "description": "Draft. To be revised after the pilot. An attempt is
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
d=json.load(open('schemas/attempt.schema.json'))
s=json.dumps(d); i=s.find('"verifications"'); print(s[i:i+5000])
EOF
sed -n 1,60p entries/001453-fouke-2025/omr.py; python - <<'EOF'
import json
nb=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:6]: print(c['cell_type'], c['metadata'], ''.join(c['source'])[:1500]); print('---')
print(nb['metadata'])
EOF
```

```
"verifications": {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["date", "kind", "by", "results"], "properties": {"date": {"type": "string", "format": "date"}, "kind": {"enum": ["agent", "person", "paper_author"]}, "by": {"type": "string"}, "results": {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["claim", "agrees"], "properties": {"claim": {"type": "string"}, "agrees": {"type": "boolean"}, "reason": {"description": "The verifier's reason, in its own words.", "type": "string"}, "response": {"description": "What the author changed or replied, kept apart from the verifier's reason.", "type": "string"}, "outcome": {"description": "The outcome the verifier would give.", "enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}}}}, "reviewed": {"description": "What was reviewed, e.g. a commit, when the attempt changed afterwards.", "type": "string"}}}}, "findings": {"description": "What the attempt found about the dataset itself, whatever the outcomes. These roll up into the per-dataset report.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["kind", "statement"], "properties": {"kind": {"enum": ["metadata_error", "data_missing", "identifier_missing", "metadata_insufficient", "selection_undocumented", "methods_unavailable", "format_error", "code_mismatch", "paper_inconsistency", "other"]}, "statement": {"type": "string", "minLength": 1}}}}, "inputs": {"description": "Everything the attempt used that is not in the dataset.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["what", "source"], "properties": {"what": {"type": "string", "minLength": 1}, "source": {"description": "A DOI, or a repository URL with the commit read.", "type": "string", "minLength": 1}}}}}, "allOf": [{"if": {"properties": {"provenance": {"properties": {"kind": {"const": "agent"}}}}}, "then": {"properties": {"provena
[... 162 more lines not kept]
```

**Agent**

Writing the entry now: helper module, notebook, entry.yaml and requirements. First, a quick look at what the paper's data availability statement says about the dataset version.

**Agent calls Bash**

```bash
grep -n -i "dandi\|000034\|246\|active channels" paper/10.7554-elife.61834.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -o -i ".\{200\}dandi.\{200\}" paper/10.7554-elife.61834.txt | head -5; grep -o -i ".\{150\}246.\{100\}" paper/10.7554-elife.61834.txt | head -3; grep -o -i ".\{100\}10 *µV.\{100\}\|.\{150\}Gaussian noise.\{100\}" paper/10.7554-elife.61834.txt | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "entries/000034-buccino-2020/si000034.py",
 "content": "\"\"\"Loading and checks for dandiset 000034, the recordings of Buccino et al. (2020), eLife 9:e61834,\n\"SpikeInterface, a unified framework for spike sorting\", doi:10.7554/eLife.61834.\n\nThe dandiset holds six NWB files: a 15 min Neuropixels recording of mouse 412804 and two manual\ncurations of its Kilosort2 output (spike times only), a simulated (MEArec) Neuropixels recording\nwith its 250 ground-truth units, a rat cortex Neuropixels recording (dataset spe-c1) and a mouse\nretina Biocam recording. Files are streamed from the archive at the pinned version with remfile\nand h5py; nothing is written to disk.\n\nWhere the parameters come from:\n\n- Spike times are turned into frames as spikeextractors 0.8.4 NwbSortingExtractor does\n  (`round(t * fs)`, frames > 0), at the sampling rate of the recording the curations were made\n  from (30 kHz); the curated files carry no rate of their own.\n- The comparison of the two curations is spikecomparison 0.2.6 `compare_two_sorters` with its\n  defaults (delta_time 0.4 ms, match_score 0.5, chance_score 0.1), as the claims file's opening\n  comment and fig4a-curators-agree give it. spikeextractors 0.8.4 uses NumPy aliases removed in\n  NumPy 2 (`np.float`, `np.int`, `np.Inf`, `np.product`, `np.in1d`); `legacy_numpy_aliases`\n  restores them as the builtins and functions they stood for, which changes no computation.\n- The band-pass filter (300 to 6000 Hz, third-order Butterworth, zero phase), the common median\n  reference and the lag range of the clock check are standard choices for a data check; they\n  decide no outcome.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport shutil\nimport subprocess\nimport time\n\nimport h5py\nimport numpy as np\nimport remfile\nimport requests\nfrom scipy.signal import butter, sosfiltfilt\n\nDANDISET_ID = \"000034\"\nDANDISET_VERSION = \"0.211030.0713\"\nAPI = \"https://api.dandiarchive.org/api\"\n\nCURATED_1 = \"sub-mouse412804/sub-mouse412804_ses-20200824T155542.nwb\"\nCURATED_2 = \"sub-mouse412804/sub-mouse412804_ses-20200824T155543.nwb\"\nMOUSE = \"sub-mouse412804/sub-mouse412804_ecephys.nwb\"\nMEAREC = \"sub-MEAREC-250neuron-Neuropixels/sub-MEAREC-250neuron-Neuropixels_ecephys.nwb\"\nRAT = \"sub-c1/sub-c1_ecephys.nwb\"\nRETINA = \"sub-P29-16-05-14-retina02-left/sub-P29-16-05-14-retina02-left_ecephys.nwb\"\nRECORDINGS = {\"mouse412804\": MOUSE, \"MEArec\": MEAREC, \"rat c1\": RAT, \"retina\": RETINA}\n\nCURATION_FS = 30000.0      # the mouse recording's rate, used for the curated spike times\nBAND = (300.0, 6000.0)     # standard choice, clock check only\n\n\ndef list_assets(version: str = DANDISET_VERSION) -> list[dict]:\n    \"\"\"Path, size and asset id of every asset of a version of the dandiset.\"\"\"\n    url = f\"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=200\"\n    out = []\n    while url:\n        page = requests.get(url, timeout=60).json()\n        out += [{\"path\": a[\"path\"], \"size\": a[\"size\"], \"asset_id\": a[\"asset_id\"]} for a in page[\"results\"]]\n        url = page.get(\"next\")\n    return out\n\n\ndef version_info(version: str = DANDISET_VERSION) -> dict:\n    return requests.get(f\"{API}/dandisets/{DANDISET_ID}/versions/{version}/info/\", timeout=60).json()\n\n\ndef open_nwb(path: str, version: str = DANDISET_VERSION) -> h5py.File:\n    \"\"\"Open an asset of the pinned version for streaming.\"\"\"\n    asset = next(a for a in list_assets(version) if a[\"path\"] == path)\n    s3 = requests.head(f\"{API}/assets/{asset['asset_id']}/download/\", allow_redirects=True, timeout=60).url\n    return h5py.File(remfile.File(s3), \"r\")\n\n\ndef _text(x):\n    return x.decode() if isinstance(x, bytes) else str(x)\n\n\ndef describe(f: h5py.File) -> dict:\n    \"\"\"Subject, session and the raw series of one file (no data read beyond metadata).\"\"\"\n    out = {k: _text(f[\"general/subject\"][k][()]) for k in f[\"general/subject\"]}\n    out[\"session_start_time\"] = _text(f[\"session_start_time\"][()])\n    if \"ElectricalSeries\" in f.get(\"acquisition\", {}):\n        es = f[\"acquisition/ElectricalSeries\"]\n        d = es[\"data\"]\n        rate = float(es[\"starting_time\"].attrs[\"rate\"])\n        out.update(frames=d.shape[0], channels=d.shape[1], dtype=str(d.dtype), chunks=d.chunks,\n                   rate_hz=rate, duration_s=d.shape[0] / rate, starting_time=float(es[\"starting_time\"][()]),\n                   conversion=float(d.attrs[\"conversion\"]), unit=_text(d.attrs[\"unit\"]),\n                   offset=float(d.attrs[\"offset\"]) if \"offset\" in d.attrs else None)\n    if \"units\" in f:\n        out[\"units\"] = int(f[\"units/id\"].shape[0])\n        out[\"unit_columns\"] = [_text(c) for c in f[\"units\"].attrs[\"colnames\"]]\n    return out\n\n\ndef load_units(f: h5py.File) -> dict[int, np.ndarray]:\n    \"\"\"Spike times (s) per unit id, from the Units table.\"\"\"\n    st = f[\"units/spike_times\"][:]\n    idx = f[\"units/spike_times_index\"][:]\n    ids = f[\"units/id\"][:]\n    return {int(u): t for u, t in zip(ids, np.split(st, idx[:-1]))}\n\n\ndef to_frames(times: np.ndarray, fs: float = CURATION_FS) -> np.ndarray:\n    \"\"\"As spikeextractors 0.8.4 NwbSortingExtractor.get_unit_spike_train: round, keep frames > 0.\"\"\"\n    frames = np.round(np.asarray(times) * fs).astype(\"int64\")\n    return frames[frames > 0]\n\n\ndef read_block(f: h5py.File, n_frames: int, channels: slice = slice(None)):\n    \"\"\"Read the first n_frames of the raw series; return the values and the seconds it took.\"\"\"\n    t0 = time.time()\n    x = f[\"acquisition/ElectricalSeries/data\"][0:n_frames, channels]\n    return x, time.time() - t0\n\n\ndef bandpass_cmr(x: np.ndarray, fs: float) -> np.ndarray:\n    \"\"\"Band-pass and common median reference (standard choices, for the clock check).\"\"\"\n    sos = butter(3, BAND, btype=\"band\", fs=fs, output=\"sos\")\n    y = sosfiltfilt(sos, x.astype(\"float64\"), axis=0)\n    return y - np.median(y, axis=1, keepdims=True)\n\n\ndef lag_scan(y: np.ndarray, trains: dict[int, np.ndarray], lags: np.ndarray, min_spikes: int,\n             rng: np.random.Generator, margin: int = 100) -> dict:\n    \"\"\"For each unit with enough spikes in the block, the mean trace at its spike frames shifted by\n    each lag, and its largest negative deflection over channels. If the spike times share the\n    recording's clock, the deflection peaks at lag 0. Random frames give the reference.\"\"\"\n    n = y.shape[0]\n    best, amp0, amp_rand, units = [], [], [], []\n    for u, fr in trains.items():\n        fr = fr[(fr > margin) & (fr < n - margin)]\n        if len(fr) < min_spikes:\n            continue\n        a = np.array([(-y[fr + L]).mean(0).max() for L in lags])\n        rnd = np.sort(rng.integers(margin, n - margin, len(fr)))\n        units.append(u)\n        best.append(int(lags[a.argmax()]))\n        amp0.append(float(a[lags == 0][0]))\n        amp_rand.append(float((-y[rnd]).mean(0).max()))\n    return {\"unit\": np.array(units), \"best_lag\": np.array(best), \"amp_at_0\": np.array(amp0),\n            \"amp_random\": np.array(amp_rand)}\n\n\ndef legacy_numpy_aliases() -> list[str]:\n    \"\"\"Restore the NumPy names spikeextractors 0.8.4 and spikecomparison 0.2.6 use.\"\"\"\n    added = []\n    for name, value in [(\"float\", float), (\"int\", int), (\"Inf\", np.inf), (\"product\", np.prod),\n                        (\"in1d\", np.isin)]:\n        if name not in np.__dict__:\n            setattr(np, name, value)\n            added.append(name)\n    return added\n\n\ndef numpy_sorting(trains: dict[int, np.ndarray], fs: float = CURATION_FS):\n    \"\"\"A spikeextractors 0.8.4 sorting from frames per unit.\"\"\"\n    import spikeextractors as se\n    times = np.concatenate([trains[u] for u in trains])\n    labels = np.concatenate([np.full(len(trains[u]), u) for u in trains])\n    s = se.NumpySortingExtractor()\n    s.set_times_labels(times, labels)\n    s.set_sampling_frequency(fs)\n    return s\n\n\ndef compare_two(trains1, trains2, name1=\"C1\", name2=\"C2\", **kwargs):\n    \"\"\"spikecomparison 0.2.6 compare_two_sorters, defaults unless given.\"\"\"\n    import spikecomparison as sc\n    return sc.compare_two_sorters(numpy_sorting(trains1), numpy_sorting(trains2), name1, name2, **kwargs)\n\n\ndef environment() -> dict:\n    \"\"\"What the sorters the paper ran would need: MATLAB (Kilosort2, IronClust, HDSort), a CUDA\n    GPU (Kilosort2), MPI (SpyKING Circus).\"\"\"\n    gpu = None\n    if shutil.which(\"nvidia-smi\"):\n        gpu = subprocess.run([\"nvidia-smi\", \"-L\"], capture_output=True, text=True).stdout.strip()\n    return {\"matlab\": shutil.which(\"matlab\"), \"nvcc\": shutil.which(\"nvcc\"), \"nvidia-smi\": shutil.which(\"nvidia-smi\"),\n            \"gpu\": gpu, \"mpiexec\": shutil.which(\"mpiexec\")}\n"
}
```

```
File created successfully at: entries/000034-buccino-2020/si000034.py (file state is current in your context — no need to Read it back)
```

**Agent**

Now the notebook.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/gen && cat > $TMPDIR/gen/make_nb.py <<'PYEOF'
import nbformat as nbf
nb = nbf.v4.new_notebook()
C = []
def md(s, tags=None):
    c = nbf.v4.new_markdown_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    C.append(c)
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s.strip("\n"))
    if tags: c.metadata["tags"] = tags
    C.append(c)

md(r"""
# Reproducing Buccino et al. (2020) from dandiset 000034

**Paper.** Buccino AP, Hurwitz CL, Garcia S, Magland J, Siegle JH, Hurwitz R, Hennig MH (2020).
SpikeInterface, a unified framework for spike sorting. *eLife* 9:e61834.
[doi:10.7554/eLife.61834](https://doi.org/10.7554/eLife.61834). The claims file
(`claims/000034/10.7554-elife.61834.yaml`) was written from the version of record (full text from
Europe PMC, PMC7704107, with the figure-supplement legends, the Methods and the author response)
and the paper's notebooks in `SpikeInterface/spikeinterface.github.io` (last changed at ee08fb6).

**Dandiset.** [DANDI:000034](https://dandiarchive.org/dandiset/000034/0.211030.0713), version
0.211030.0713 (doi:10.48324/dandi.000034/0.211030.0713). The paper cites the draft
(`dandiset/000034/draft`), as it was published before any version existed. This is the only
published version; the data check below shows that it holds the same six assets (same asset ids
and sizes) as today's draft, so the choice does not change the data.

**What the dandiset holds.** The four recordings the paper analyses (mouse Neuropixels, simulated
MEArec Neuropixels with ground truth, rat cortex Neuropixels, mouse retina Biocam) and the two
experts' manual curations of the paper's Kilosort2 output on the mouse recording. It holds no
output of any of the six spike sorters the paper compares.

**Why most claims are blocked.** Every finding except the presence of the recordings rests on
running six spike sorters on these recordings. Kilosort2, IronClust and HDSort are MATLAB
programs (Kilosort2 also needs a CUDA GPU); they cannot be put in a locked Python environment, and
this runner has neither MATLAB nor a GPU. The section "Why the sorter claims are blocked" also
measures how fast the recordings stream: reading any of them whole would take hours, over the
30 minute limit of a notebook here.

| Claim | Tested here | Blocked by |
|---|---|---|
| recordings-as-described (link) | yes | |
| fig1b-unit-counts | no | not_runnable |
| fig1c-low-agreement | no | not_runnable |
| fig1d-most-units-unmatched | no | not_runnable |
| fig1s2-agreement-scores-high | no | not_runnable |
| fig1s3-s4-other-recordings-disagree | no | not_runnable |
| fig2c-sim-unit-counts | no | not_runnable |
| fig2s1a-precision-recall-bias | no | not_runnable |
| fig2s1b-accuracy-snr | no | not_runnable |
| fig2d-ks2-highest-scores | no | not_runnable |
| fig2e-ks2-unit-types | no | not_runnable |
| fig2e-ks2-curated-unit-types | no | not_runnable |
| fig2e-tdc-few-fp-hds-many-fp | no | not_runnable |
| fig3a-sim-low-agreement | no | not_runnable |
| fig3b-sorters-prone-to-low-agreement | no | not_runnable |
| fig3c-fp-found-by-one-sorter | no | not_runnable |
| fig3s1-ks2-ic-best-pair | no | not_runnable |
| fig3s1-pairs-remove-fp-four-keep-tp | no | not_runnable |
| fig3d-snr-rises-with-agreement | no | not_runnable |
| fig3s2-snr-does-not-separate-ks2-fp | no | not_runnable |
| fig4a-curators-agree | in part (the curator counts; blocked as it depends on fig1b-unit-counts) | not_runnable |
| fig4b-single-sorter-match-curated | no | not_runnable |
| fig4c-consensus-match-curated | no | not_runnable |
| fig4d-nonconsensus-rarely-curated | no | not_runnable |
""")

code(r"""
import time
import warnings

import numpy as np
import pandas as pd

import si000034 as si

warnings.filterwarnings("ignore")
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 30)
started = time.time()
print(f"dandiset {si.DANDISET_ID} version {si.DANDISET_VERSION}")
""")

md("## Data check\n\nEach check of the metadata against the values is stated under its output.")

code(r"""
pinned = pd.DataFrame(si.list_assets(si.DANDISET_VERSION))
draft = pd.DataFrame(si.list_assets("draft"))
print("Assets of version", si.DANDISET_VERSION)
print(pinned.to_string(index=False))
same = pinned.merge(draft, on=["path", "size", "asset_id"], how="outer", indicator=True)
print("\nAssets in both the pinned version and the draft, same id and size:", int((same._merge == "both").sum()),
      "; only in one:", int((same._merge != "both").sum()))
info = si.version_info()
print("Version name:", info["metadata"]["name"])
print("Description:", info["metadata"]["description"][-250:])
""", tags=["sanity"])

md("""
The pinned version and the draft hold the same six files. The description says the dandiset holds
all recordings analysed in the paper.
""")

code(r"""
files = {"curated 1": si.CURATED_1, "curated 2": si.CURATED_2, **si.RECORDINGS}
handles, rows = {}, []
for name, path in files.items():
    f = si.open_nwb(path)
    handles[name] = f
    d = si.describe(f)
    rows.append({"name": name, "path": path.split("/")[-1], **d})
desc = pd.DataFrame(rows).set_index("name")
cols = ["subject_id", "species", "age", "session_start_time", "frames", "channels", "rate_hz", "duration_s",
        "dtype", "chunks", "conversion", "offset", "unit", "starting_time", "units", "unit_columns"]
print(desc[cols].to_string())
""", tags=["sanity"])

md("""
Every recording starts at time 0 and has a regular rate. Each stores its raw data in chunks of one
channel by several thousand frames, so a read of a short stretch of all channels fetches one chunk
per channel. The curated files hold a Units table with spike times only (no rate, no labels, no
link to the Kilosort2 units). The simulated file holds its 250 ground-truth units with their soma
locations. No file says which cells are excitatory or inhibitory, or how the recordings were cut or
filtered (`filtering` is "none" and `location` "unknown" for every channel).
""")

code(r"""
cur = {k: si.load_units(handles[k]) for k in ["curated 1", "curated 2"]}
gt = si.load_units(handles["MEArec"])
for name, units in [*cur.items(), ("MEArec ground truth", gt)]:
    t = np.concatenate(list(units.values()))
    n = np.array([len(v) for v in units.values()])
    print(f"{name}: {len(units)} units, ids {min(units)} to {max(units)}, {len(t)} spikes, times {t.min():.4f} to {t.max():.4f} s, "
          f"spikes per unit {n.min()} to {n.max()} (median {np.median(n):.0f}), sorted within every unit: "
          f"{all(np.all(np.diff(v) >= 0) for v in units.values())}")
for name in cur:
    t = np.concatenate(list(cur[name].values()))
    print(f"{name}: largest distance of t*30000 from a whole frame: {np.abs(t * 30000 - np.round(t * 30000)).max():.1e} frames")
ids1, ids2 = set(cur["curated 1"]), set(cur["curated 2"])
print("Unit ids in both curations:", len(ids1 & ids2), "; spike trains identical under the same id:",
      sum(np.array_equal(cur["curated 1"][u], cur["curated 2"][u]) for u in ids1 & ids2))
soma = handles["MEArec"]["units/soma_location"][:]
print("MEArec soma locations (um): x", soma[:, 0].min().round(1), "to", soma[:, 0].max().round(1),
      "; y", soma[:, 1].min().round(1), "to", soma[:, 1].max().round(1), "; z", soma[:, 2].min().round(1), "to", soma[:, 2].max().round(1))
""", tags=["sanity"])

md("""
The curated spike times lie within the 900 s of the mouse recording and fall on whole frames at
30 kHz, which is consistent with spike times taken from that recording. The two curations share
many unit ids with identical spike trains; these are the Kilosort2 clusters both experts kept
unchanged, as expected of two curations of one sorting. They are two different files, not one
recording deposited twice. The ground-truth spikes lie within the simulated recording's 600 s.
""")

code(r"""
env = si.environment()
print("Software the paper's sorters need, on this runner:", env)
""", tags=["sanity"])

md("""
### Clock and units of the raw data

The curated spike times and the ground-truth spike times are checked against the raw traces they
belong to: the mean trace at each unit's spike frames, shifted by -1.5 to +1.5 ms, should have its
deepest trough at lag 0 if the spike times share the recording's clock, and random frames give the
reference. Only the first chunk of each channel is read (1.76 s of the mouse recording, 0.59 s of
the simulation), because streaming is slow; the time of each read is printed and used below.
""")

code(r"""
rng_clock = np.random.default_rng(34001)
reads = []
lags = np.arange(-45, 46)

mouse = handles["mouse412804"]
n_mouse = mouse["acquisition/ElectricalSeries/data"].chunks[0] * 2
x, secs = si.read_block(mouse, n_mouse)
reads.append({"recording": "mouse412804", "frames": n_mouse, "channels": x.shape[1], "seconds_of_data": n_mouse / 30000, "read_s": secs})
print(f"mouse412804: {x.shape} {x.dtype}, values {x.min()} to {x.max()} (x conversion 1e-6 = volts, i.e. microvolts), read in {secs:.1f} s")
y = si.bandpass_cmr(x, 30000.0)
print(f"  band-passed: median channel SD {np.median(y.std(0)):.1f} uV")
for name in cur:
    trains = {u: si.to_frames(t) for u, t in cur[name].items()}
    r = si.lag_scan(y, trains, lags, min_spikes=5, rng=rng_clock)
    print(f"  {name}: {len(r['unit'])} units with >= 5 spikes in the block; lag of the deepest trough (frames): median "
          f"{np.median(r['best_lag']):.0f}, 10th to 90th percentile {np.percentile(r['best_lag'], 10):.0f} to "
          f"{np.percentile(r['best_lag'], 90):.0f}, within 3 frames: {np.mean(np.abs(r['best_lag']) <= 3):.2f}; "
          f"trough at lag 0 median {np.median(r['amp_at_0']):.0f} uV, at random frames {np.median(r['amp_random']):.0f} uV")
del x, y
""", tags=["sanity"])

code(r"""
mea = handles["MEArec"]
n_mea = mea["acquisition/ElectricalSeries/data"].chunks[0]
x, secs = si.read_block(mea, n_mea)
reads.append({"recording": "MEArec", "frames": n_mea, "channels": x.shape[1], "seconds_of_data": n_mea / 32000, "read_s": secs})
print(f"MEArec: {x.shape} {x.dtype}, values {x.min():.1f} to {x.max():.1f} uV, read in {secs:.1f} s")
mad_sd = np.median(np.abs(x - np.median(x, 0)), 0) / 0.6745
print(f"  noise SD per channel from the median absolute deviation: median {np.median(mad_sd):.2f} uV, range "
      f"{mad_sd.min():.2f} to {mad_sd.max():.2f} (paper: additive Gaussian noise of 10 uV SD)")
y = si.bandpass_cmr(x, 32000.0)
trains = {u: si.to_frames(t, 32000.0) for u, t in gt.items()}
r = si.lag_scan(y, trains, lags, min_spikes=2, rng=rng_clock)
print(f"  ground truth: {len(r['unit'])} units with >= 2 spikes in the block; lag of the deepest trough: median "
      f"{np.median(r['best_lag']):.0f}, within 3 frames: {np.mean(np.abs(r['best_lag']) <= 3):.2f}; trough at lag 0 median "
      f"{np.median(r['amp_at_0']):.0f} uV, at random frames {np.median(r['amp_random']):.0f} uV")
del x, y
""", tags=["sanity"])

code(r"""
rat = handles["rat c1"]
n_rat = rat["acquisition/ElectricalSeries/data"].chunks[0]
x, secs = si.read_block(rat, n_rat, slice(0, 128))
reads.append({"recording": "rat c1", "frames": n_rat, "channels": x.shape[1], "seconds_of_data": n_rat / 30000, "read_s": secs})
print(f"rat c1, channels 0 to 127: {x.dtype}, values {x.min():.1f} to {x.max():.1f}, per-channel mean "
      f"{x.mean(0).min():.1f} to {x.mean(0).max():.1f}, median channel SD {np.median(x.std(0)):.1f}, read in {secs:.1f} s")
ret = handles["retina"]
n_ret = ret["acquisition/ElectricalSeries/data"].chunks[0]
x, secs = si.read_block(ret, n_ret, slice(0, 256))
reads.append({"recording": "retina", "frames": n_ret, "channels": x.shape[1], "seconds_of_data": n_ret / desc.loc["retina", "rate_hz"], "read_s": secs})
vals, counts = np.unique(x, return_counts=True)
print(f"retina, channels 0 to 255: {x.dtype}, values {x.min()} to {x.max()}, median {np.median(x):.0f}, median channel SD "
      f"{np.median(x.std(0)):.1f}, channels constant over the block: {(x.std(0) == 0).sum()}, samples at {x.max()}: "
      f"{counts[-1]}, read in {secs:.1f} s")
print("retina stated conversion", desc.loc["retina", "conversion"], desc.loc["retina", "unit"], "; offset attribute:", desc.loc["retina", "offset"])
del x
""", tags=["sanity"])

md("""
The mouse curations and the simulated ground truth share the clocks of their recordings: for most
units the trough of the mean trace is at lag 0 or within a few frames, and much deeper than at
random frames (numbers above). This is shown on the first seconds of each recording only. The
mouse and simulated data in microvolts have plausible ranges, and the simulated noise level
estimated from the traces is printed against the paper's 10 uV. The retina recording is stored as
unsigned integers centred near 2048 and reaching 4096, which is consistent with raw ADC counts of a
12-bit converter, not with microvolts; read with the stated conversion (1e-6 V per unit, no
offset) every channel would sit near +2 mV. The gain and offset that turn these counts into volts
are not in the file. No claim tested here uses the retina's values.
""")

md("""
## recordings-as-described (link claim)

> The dandiset holds the recordings the paper analyses and the files its notebooks name, with the
> properties the paper and the notebooks give.

Criterion: each of the five named files is present, and a recording of mouse 412804 with 30 kHz,
15 min (27,000,000 frames) and 246 (paper) or 248 (notebook) channels; the simulated recording
lasts 10 min and its ground truth has 250 units; the rat recording has 384 channels at 30 kHz; the
Biocam recording has 1024 channels at about 23199 Hz.
""")

code(r"""
named = ["sub-mouse412804_ses-20200824T155542.nwb", "sub-mouse412804_ses-20200824T155543.nwb",
         "sub-MEAREC-250neuron-Neuropixels_ecephys.nwb", "sub-c1_ecephys.nwb", "sub-P29-16-05-14-retina02-left_ecephys.nwb"]
present = set(pinned.path.str.split("/").str[-1])
checks = [(f"file {n} present", n in present, "") for n in named]
m, s, r, b = (desc.loc[k] for k in ["mouse412804", "MEArec", "rat c1", "retina"])
checks += [
    ("mouse 412804 recording present", m.subject_id == "mouse412804", f"{m.path}, subject {m.subject_id}"),
    ("mouse: 30 kHz", m.rate_hz == 30000, m.rate_hz),
    ("mouse: 27,000,000 frames (15 min)", m.frames == 27_000_000, f"{m.frames} frames, {m.duration_s:.1f} s"),
    ("mouse: 246 or 248 channels", m.channels in (246, 248), m.channels),
    ("simulated: 10 min", abs(s.duration_s - 600) < 1, f"{s.duration_s:.2f} s at {s.rate_hz:.0f} Hz"),
    ("simulated: 250 ground-truth units", s.units == 250, s.units),
    ("rat: 384 channels", r.channels == 384, r.channels),
    ("rat: 30 kHz", r.rate_hz == 30000, f"{r.rate_hz} Hz, {r.duration_s:.2f} s (notebook printed 270.0 s)"),
    ("retina: 1024 channels", b.channels == 1024, b.channels),
    ("retina: about 23199 Hz", abs(b.rate_hz - 23199) < 1, f"{b.rate_hz:.3f} Hz, {b.duration_s:.2f} s (notebook printed 135.7 s)"),
]
link = pd.DataFrame(checks, columns=["check", "holds", "value"])
print(link.to_string(index=False))
print("\nAll hold:", bool(link.holds.all()), f"({int(link.holds.sum())} of {len(link)})")
""", tags=["claim:recordings-as-described"])

md("""
**Result: reproduced.** All 15 checks above hold: the five named files are present, the mouse 412804
recording has 248 channels (the notebook's count, not the paper's 246) at 30 kHz for 27,000,000
frames, the simulation lasts 600 s with 250 ground-truth units, the rat recording has 384 channels at
30 kHz, and the retina recording 1024 channels at 23199.09 Hz.
""")

md("""
## Why the sorter claims are blocked

Every other claim needs the units that the six sorters (HerdingSpikes2, Kilosort2, IronClust,
Tridesclous, SpyKING Circus, HDSort) return on these recordings; the dandiset holds none of them,
and the claims file fixes the method as running those sorters. Below: what the runner offers, and
how long reading each recording whole would take at the streaming rate measured above.
""")

code(r"""
print("MATLAB:", env["matlab"], "| CUDA compiler:", env["nvcc"], "| GPU:", env["gpu"], "| MPI:", env["mpiexec"])
rt = pd.DataFrame(reads)
rt["chunks_read"] = rt.channels
rt["s_per_chunk"] = rt.read_s / rt.chunks_read
dur = desc.duration_s.reindex(rt.recording).values
chans = desc.channels.reindex(rt.recording).values
frames_per_chunk = np.array([desc.loc[k, "chunks"][0] for k in rt.recording])
rt["chunks_whole_file"] = np.ceil(desc.frames.reindex(rt.recording).values / frames_per_chunk) * chans
rt["hours_whole_file"] = rt.chunks_whole_file * rt.s_per_chunk / 3600
print(rt.round(3).to_string(index=False))
print(f"\nShortest estimated time to stream a whole recording: {rt.hours_whole_file.min():.1f} h; notebook limit 0.5 h.")
""")

md("""
Kilosort2, IronClust and HDSort need MATLAB, and Kilosort2 a CUDA GPU; none is on this runner and
none can be installed from a lock file. While preparing (not run here), Tridesclous 1.6.0 and
SpyKING Circus 0.9.7 installed with pip on Python 3.13, HerdingSpikes 0.3.7 failed to build, and
SpyKING Circus has no MPI to run with. Even the three Python sorters would first need each
recording read whole, which the table above puts at hours per recording.
""")

md("""
## fig4a-curators-agree (blocked; the curator counts computed)

> The two experts' manual curations of the Kilosort2 output agree on most curated units (226 of
> 351, 64.2%), and 174 Kilosort2 units are discarded by both.

The claim depends on fig1b-unit-counts (the Kilosort2 run), which is blocked, so it is blocked for
the same reason. Its count of 174 needs the Kilosort2 run. Its other numbers come from the two
curated files alone under the criterion's second reading: `compare_two_sorters(curated 1,
curated 2)` with defaults, 226 = matched pairs, 351 = the two counts summed less the matched pairs.
They are computed here. The first reading (`compare_multiple_sorters` with the Kilosort2 run) cannot
be run.
""")

code(r"""
added = si.legacy_numpy_aliases()
import spikecomparison, spikeextractors
print("spikecomparison", spikecomparison.__version__, "| spikeextractors", spikeextractors.__version__, "| NumPy aliases restored:", added)
tr1 = {u: si.to_frames(t) for u, t in cur["curated 1"].items()}
tr2 = {u: si.to_frames(t) for u, t in cur["curated 2"].items()}
comp = si.compare_two(tr1, tr2)
match = comp.hungarian_match_12
n1, n2, k = len(tr1), len(tr2), int((match != -1).sum())
print(f"curated 1: {n1} units; curated 2: {n2} units")
print(f"matched pairs (both curators): {k}; units of either curator: {n1 + n2 - k}; ratio {100 * k / (n1 + n2 - k):.2f}%")
print("expected: 226 +- 22.6; 351 +- 35.1; 64.2 +- 6.42%")
scores = np.array([comp.agreement_scores.loc[a, b] for a, b in match.items() if b != -1])
print(f"agreement scores of matched pairs: min {scores.min():.3f}, median {np.median(scores):.3f}, equal to 1: {(scores == 1).sum()}")
print("\nDependence on the minimum score (criterion: the default, 0.5):")
for ms in [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]:
    c = si.compare_two(tr1, tr2, match_score=ms)
    kk = int((c.hungarian_match_12 != -1).sum())
    print(f"  match_score {ms}: both {kk}, either {n1 + n2 - kk}, {100 * kk / (n1 + n2 - kk):.2f}%")
print(f"\nrun time so far {(time.time() - started) / 60:.1f} min")
""", tags=["claim:fig4a-curators-agree"])

md("""
**Result: blocked (not_runnable), as the claim depends on the blocked Kilosort2 run.** The part that
does not need that run matches: the curators share 226 matched units of 351 (64.39%). These are the
paper's 226 and 351 exactly; the paper prints 64.2% for their ratio. With a minimum score of 0.3 to
0.8 the shared count ranges from 231 to 208, inside the tolerance throughout. The 174 Kilosort2 units
both curators discarded could not be counted.
""")

md("""
## Summary

| Claim | Outcome |
|---|---|
| recordings-as-described (link) | reproduced |
| fig4a-curators-agree | blocked, not_runnable (226 of 351 curated units shared, as in the paper; the 174 needs the Kilosort2 run) |
| the 22 other claims (fig1b to fig4d) | blocked, not_runnable |

**How the analysis differs from the paper's.** No sorter was run. The paper ran six sorters, three
of them in MATLAB, on the four recordings; this attempt could only check the recordings and compare
the two curations with each other. The curations were compared with spikecomparison 0.2.6, the
version the paper's notebooks ran, on NumPy 2 with the removed NumPy aliases restored.

**What was found about the dataset.**
- The dandiset holds the four recordings and the two curations the paper names, with the stated
  rates, channel counts, durations and number of ground-truth units. It holds no sorter output, so
  the paper's comparisons can be repeated only by running the sorters again.
- The mouse recording has 248 channels; the paper says 246 active channels. Which two are inactive
  is not marked.
- The curated sortings carry no rate, no unit labels and no link to the Kilosort2 units they were
  curated from; their spike times are consistent with the mouse recording's clock (trough at lag 0).
- The retina recording is stored as unsigned counts centred near 2048 with a stated conversion of
  1e-6 V and no offset, which would give a DC level of about 2 mV; the gain and offset of the
  Biocam's converter are not in the file.
- Every raw series is chunked one channel per chunk, so streaming a stretch of all channels is
  very slow (table above).
- The paper's 64.2% for 226 of 351 is 64.39%.
""")

nb.cells = C
nb.metadata = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}}
nbf.write(nb, "entries/000034-buccino-2020/reproduce_buccino_2020.ipynb")
PYEOF
python $TMPDIR/gen/make_nb.py && cat > entries/000034-buccino-2020/requirements.in <<'EOF'
h5py
numpy
pandas
remfile
requests
scipy
setuptools
spikecomparison==0.2.6
spikeextractors==0.8.4
spikesorters==0.3.3
spiketoolkit==0.6.3
EOF
cat > entries/000034-buccino-2020/entry.yaml <<'EOF'
schema_version: 1
name: 000034-buccino-2020
type: reproduction
title: SpikeInterface spike sorter comparison (Buccino et al. 2020)
description: Tests the findings of Buccino, Hurwitz, Garcia, Magland, Siegle, Hurwitz and Hennig
  (2020) on dandiset 000034, which holds the mouse, simulated, rat and retina recordings the paper
  sorts and two manual curations of its Kilosort2 output. It checks that the recordings are as
  described, that the curated and ground-truth spike times share the recordings' clocks, and
  compares the two curations. The findings about sorter outputs are blocked, as three of the six
  sorters need MATLAB and a GPU and the recordings stream too slowly to sort here.
license: Apache-2.0
notebooks:
- path: reproduce_buccino_2020.ipynb
  title: Reproducing Buccino et al. (2020) from dandiset 000034
  runtime_minutes: 6
helpers:
- si000034.py
related:
- id: dandi:000034/0.211030.0713
  relation: uses_data
- id: doi:10.7554/elife.61834
  relation: reproduces
EOF
pip list 2>/dev/null | grep -i "nbformat\|jsonschema\|pyyaml" ; python tools/entry.py lock entries/000034-buccino-2020
```

```
fastjsonschema            2.22.2
jsonschema                4.26.0
jsonschema-specifications 2025.9.1
nbformat                  5.11.1
PyYAML                    6.0.3
wrote entries/000034-buccino-2020/requirements.lock.txt
```

**Agent**

Entry files written and the environment is locked. Running check and the full notebook from a clean environment.

**Agent calls Bash**

```bash
time python tools/entry.py all entries/000034-buccino-2020 2>&1 | tail -30
```

```
Installed kernelspec registry-000034-buccino-2020 in executed/000034-buccino-2020/.venv/share/jupyter/kernels/registry-000034-buccino-2020
0 error(s)
pass  reproduce_buccino_2020.ipynb  (291 s)

real	5m12.778s
user	5m48.084s
sys	0m19.654s
```

**Agent**

The notebook ran clean in 291 s. Reading the executed outputs to confirm the conclusions match the numbers.

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/000034-buccino-2020/reproduce_buccino_2020.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            t=o.get('text') or o.get('data',{}).get('text/plain','')
            print(''.join(t) if isinstance(t,list) else t)
        print('-----')
EOF
```

```
dandiset 000034 version 0.211030.0713

-----
Assets of version 0.211030.0713
                                                                         path        size                             asset_id
                      sub-mouse412804/sub-mouse412804_ses-20200824T155542.nwb     9693752 af1745f6-e14a-473a-987d-cef7e29a3956
                      sub-mouse412804/sub-mouse412804_ses-20200824T155543.nwb    11732540 c696fc2b-d2e6-4e27-8775-01657193c4a2
    sub-P29-16-05-14-retina02-left/sub-P29-16-05-14-retina02-left_ecephys.nwb  6470908640 9822a813-0dec-4d07-810b-1c13341c168d
                                  sub-mouse412804/sub-mouse412804_ecephys.nwb 13411878072 3e0d4539-902e-46b4-9cfb-119e0f69fbd0
                                                    sub-c1/sub-c1_ecephys.nwb 24916614016 76c211c2-d588-48a7-a4c8-ea103ff0570a
sub-MEAREC-250neuron-Neuropixels/sub-MEAREC-250neuron-Neuropixels_ecephys.nwb 29530187056 6d94dcf4-0b38-4323-8250-04fdc7039a66

Assets in both the pinned version and the draft, same id and size: 6 ; only in one: 0

Version name: SpikeInterface, a unified framework for spike sorting
Description: nalysed in the paper: "SpikeInterface, a unified framework for spike sorting." Alessio P. Buccino, Cole L. Hurwitz, Samuel Garcia, Jeremy Magland, Joshua H. Siegle, Roger Hurwitz, Matthias H. Hennig, eLife - doi: https://doi.org/10.7554/eLife.61834; 

-----
                               subject_id        species  age                session_start_time      frames  channels       rate_hz  duration_s    dtype      chunks  conversion  offset   unit  starting_time  units                  unit_columns
name                                                                                                                                                                                                                                               
[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && python - <<'EOF'
p='make_nb.py'; s=open(p).read()
old='''rt["chunks_read"] = rt.channels
rt["s_per_chunk"] = rt.read_s / rt.chunks_read
dur = desc.duration_s.reindex(rt.recording).values
chans = desc.channels.reindex(rt.recording).values
frames_per_chunk = np.array([desc.loc[k, "chunks"][0] for k in rt.recording])'''
new='''chans = desc.channels.reindex(rt.recording).values
frames_per_chunk = np.array([desc.loc[k, "chunks"][0] for k in rt.recording])
rt["chunks_read"] = rt.channels * np.ceil(rt.frames / frames_per_chunk)
rt["s_per_chunk"] = rt.read_s / rt.chunks_read'''
assert old in s; s=s.replace(old,new)
old='''random frames (numbers above). This is shown on the first seconds of each recording only. The
mouse and simulated data in microvolts have plausible ranges, and the simulated noise level
estimated from the traces is printed against the paper's 10 uV. The retina'''
new='''random frames (numbers above). This is shown on the first seconds of each recording only. The
mouse and simulated data in microvolts have plausible ranges. The noise level of the simulation
estimated from its traces is above the paper's 10 uV (printed above), but the estimate includes the
overlapping spikes of 250 cells, so it does not show what noise was added; this is left open. The
rat recording carries a DC offset that differs between channels. The retina'''
assert old in s; s=s.replace(old,new)
old='''offset) every channel would sit near +2 mV. The gain'''
new='''offset) every channel would sit near +2 mV, and samples at 4096 (printed above) look like
saturation, which the paper's notebook removes with `blank_saturation`. The gain'''
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
cd  && python $TMPDIR/gen/make_nb.py && time python tools/entry.py all entries/000034-buccino-2020 2>&1 | tail -3
```

```
Installed kernelspec registry-000034-buccino-2020 in executed/000034-buccino-2020/.venv/share/jupyter/kernels/registry-000034-buccino-2020
0 error(s)
pass  reproduce_buccino_2020.ipynb  (288 s)

real	5m9.926s
user	5m47.570s
sys	0m19.196s
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/000034-buccino-2020/reproduce_buccino_2020.ipynb'))
for c in nb['cells']:
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            t=o.get('text') or o.get('data',{}).get('text/plain','')
            t=''.join(t) if isinstance(t,list) else t
            if 'hours' in t or 'mouse412804:' in t or 'MEArec:' in t or 'matched pairs' in t: print(t)
EOF
```

```
mouse412804: (52736, 248) int16, values -3441 to 1528 (x conversion 1e-6 = volts, i.e. microvolts), read in 46.8 s

MEArec: (18750, 384) float32, values -620.8 to 216.9 uV, read in 71.6 s

MATLAB: None | CUDA compiler: None | GPU: None | MPI: None
  recording  frames  channels  seconds_of_data  read_s  chunks_read  s_per_chunk  chunks_whole_file  hours_whole_file
mouse412804   52736       248            1.758  46.790        496.0        0.094           253952.0             6.655
     MEArec   18750       384            0.586  71.624        384.0        0.187           393216.0            20.373
     rat c1    7911       128            0.264  23.018        128.0        0.180           393216.0            19.642
     retina   12301       256            0.530  34.141        256.0        0.133           262144.0             9.711

Shortest estimated time to stream a whole recording: 6.7 h; notebook limit 0.5 h.

curated 1: 258 units; curated 2: 319 units
matched pairs (both curators): 226; units of either curator: 351; ratio 64.39%
expected: 226 +- 22.6; 351 +- 35.1; 64.2 +- 6.42%
agreement scores of matched pairs: min 0.510, median 1.000, equal to 1: 144

Dependence on the minimum score (criterion: the default, 0.5):
```

**Agent**

Second run checked: the mouse estimate is now 6.7 h, and the curator counts are unchanged. Before writing the attempt record, checking how the paper and the archive name the rat recording's species.

**Agent calls Bash**

```bash
grep -o -i ".\{100\}\(norvegicus\|lister\|rattus\|wistar\|sprague\).\{100\}" paper/10.7554-elife.61834.txt | head; curl -s https://api.dandiarchive.org/api/dandisets/000034/versions/0.211030.0713/ | python -c "import json,sys; d=json.load(sys.stdin); print(d['assetsSummary']['species'], d.get('relatedResource'))"
```

Result: the fetched text is not kept.

**Agent calls Write**

```json
{
 "file_path": "entries/000034-buccino-2020/README.md",
 "content": "# Buccino et al. (2020) on dandiset 000034\n\nTests the findings of Buccino et al. (2020), \"SpikeInterface, a unified framework for spike\nsorting\" (eLife 9:e61834), on [DANDI:000034](https://dandiarchive.org/dandiset/000034/0.211030.0713)\nversion 0.211030.0713.\n\nThe dandiset holds the four recordings the paper sorts and the two manual curations of its\nKilosort2 output. The notebook checks that the recordings are as the paper describes them, that\nthe curated and ground-truth spike times share the clocks of their recordings, and compares the\ntwo curations with each other (226 shared units of 351, as in the paper). The findings about sorter\noutputs are blocked: the dandiset holds no sorter output, three of the six sorters need MATLAB (one\nalso a GPU), and streaming any recording whole takes hours.\n\n- `reproduce_buccino_2020.ipynb`: the notebook.\n- `si000034.py`: loading, the clock check and the curation comparison.\n"
}
```

```
File created successfully at: entries/000034-buccino-2020/README.md (file state is current in your context — no need to Read it back)
```

**Agent**

Now the attempt record.

**Agent calls Bash**

```bash
cat > $TMPDIR/gen/make_attempt.py <<'PYEOF'
import yaml
SORTER = ("needs the six sorters' output on the {rec}. The dandiset holds no sorter output. Kilosort2, IronClust "
          "and HDSort are MATLAB programs (Kilosort2 also needs a CUDA GPU); the runner has no MATLAB, GPU or MPI "
          "(printed in the notebook) and they cannot be installed from a lock file. While preparing, Tridesclous "
          "1.6.0 and SpyKING Circus 0.9.7 installed with pip on Python 3.13 and HerdingSpikes 0.3.7 failed to build. "
          "Streaming the {rec} whole at the measured rate would take {hours} h (notebook table), over the 30 min limit.")
real = dict(rec="mouse Neuropixels recording", hours="6.7")
sim = dict(rec="simulated recording", hours="20.4")
blocked = [
 ("fig1b-unit-counts", SORTER.format(**real)),
 ("fig1c-low-agreement", SORTER.format(**real)),
 ("fig1d-most-units-unmatched", SORTER.format(**real)),
 ("fig1s2-agreement-scores-high", "Needs the six sorters' output on the mouse recording or the simulated recording. "
   + SORTER.format(**real).split(". ", 1)[1]),
 ("fig1s3-s4-other-recordings-disagree", "Needs the sorters' output on the rat and retina recordings. "
   + SORTER.format(rec="rat recording", hours="19.6").split(". ", 1)[1] + " The retina recording would take 9.7 h."),
 ("fig2c-sim-unit-counts", SORTER.format(**sim)),
 ("fig2s1a-precision-recall-bias", SORTER.format(**sim)),
 ("fig2s1b-accuracy-snr", SORTER.format(**sim) + " The ground-truth SNR would also need the simulated traces around 500 spikes per unit."),
 ("fig2d-ks2-highest-scores", SORTER.format(**sim)),
 ("fig2e-ks2-unit-types", SORTER.format(**sim)),
 ("fig2e-ks2-curated-unit-types", SORTER.format(**sim)),
 ("fig2e-tdc-few-fp-hds-many-fp", SORTER.format(**sim)),
 ("fig3a-sim-low-agreement", SORTER.format(**sim)),
 ("fig3b-sorters-prone-to-low-agreement", SORTER.format(**sim)),
 ("fig3c-fp-found-by-one-sorter", SORTER.format(**sim)),
 ("fig3s1-ks2-ic-best-pair", SORTER.format(**sim)),
 ("fig3s1-pairs-remove-fp-four-keep-tp", SORTER.format(**sim)),
 ("fig3d-snr-rises-with-agreement", SORTER.format(**sim)),
 ("fig3s2-snr-does-not-separate-ks2-fp", SORTER.format(**sim)),
 ("fig4b-single-sorter-match-curated", SORTER.format(**real) + " The curated sortings are in the dandiset (see fig4a-curators-agree)."),
 ("fig4c-consensus-match-curated", SORTER.format(**real) + " The curated sortings are in the dandiset."),
 ("fig4d-nonconsensus-rarely-curated", SORTER.format(**real) + " The curated sortings are in the dandiset."),
]
for i,(c,n) in enumerate(blocked):
    blocked[i]=(c, n[0].upper()+n[1:] if n.startswith("needs") else n)
outcomes = [{
  "claim": "recordings-as-described", "outcome": "reproduced", "notebook": "reproduce_buccino_2020.ipynb",
  "output": "claim:recordings-as-described",
  "notes": ("All 15 checks hold. The five files the claims file names are present. The mouse 412804 recording is "
            "sub-mouse412804_ecephys.nwb, 27,000,000 frames at 30 kHz (900 s), 248 channels (the notebook's count; "
            "the paper says 246 active channels). The simulation lasts 600.00 s at 32 kHz and holds 250 ground-truth "
            "units. The rat recording has 384 channels at 30 kHz (270.01 s) and the retina recording 1024 channels at "
            "23199.09 Hz (135.73 s). The curated and ground-truth spike times share the clocks of their recordings on "
            "the first seconds read (deepest mean trough at lag 0 in median; within 3 frames for 0.88 and 0.86 of the "
            "curated units and 0.63 of the ground-truth units)."),
  "deviations": ["The paper's notebook loads a local file, mouse412804_probeC_15min.nwb; the dandiset's mouse recording is matched to it by subject and properties, not by name."],
}]
for c, n in blocked[:19]:
    outcomes.append({"claim": c, "outcome": "blocked", "blocked_by": "not_runnable", "notes": n})
outcomes.append({
  "claim": "fig4a-curators-agree", "outcome": "blocked", "blocked_by": "not_runnable",
  "notebook": "reproduce_buccino_2020.ipynb", "output": "claim:fig4a-curators-agree",
  "notes": ("Blocked because the claim depends on fig1b-unit-counts (the Kilosort2 run), which is blocked; its count "
            "of 174 Kilosort2 units discarded by both curators needs that run, and the paper's own Kilosort2 output, "
            "which the curators worked on, is not in the dandiset. The rest was computed from the two curated files "
            "under the criterion's second reading (compare_two_sorters of spikecomparison 0.2.6, defaults): curated 1 "
            "has 258 units and curated 2 has 319; 226 are matched and 351 belong to either, 64.39%, so 226 and 351 "
            "equal the paper's and 64.39% is within 6.42 of its 64.2%. With a minimum score from 0.3 to 0.8 the "
            "matched count goes from 231 to 208, inside the tolerance. The first reading (compare_multiple_sorters "
            "with the Kilosort2 run) could not be run."),
  "deviations": ["spikecomparison 0.2.6 and spikeextractors 0.8.4 were run on NumPy 2 with the removed aliases np.float, np.int, np.Inf, np.product and np.in1d restored as the builtins and functions they stood for.",
                 "The curated files carry no sampling rate; their spike times were turned into frames at the mouse recording's 30 kHz, as the paper's loader (NwbSortingExtractor) does with the rate it is given."],
})
for c, n in blocked[19:]:
    outcomes.append({"claim": c, "outcome": "blocked", "blocked_by": "not_runnable", "notes": n})

rec = {
 "schema_version": 2,
 "id": "000034-buccino-2020-01",
 "dataset": {"archive": "dandi", "id": "000034", "version": "0.211030.0713", "doi": "10.48324/dandi.000034/0.211030.0713"},
 "paper": "doi:10.7554/elife.61834",
 "date": "2026-10-22",
 "entry": "000034-buccino-2020",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
   "agent": {"harness": "Claude Code (GitHub Actions)", "model": "claude-opus-5-5", "protocol": "pilot-10"},
   "runner": {"platform": "GitHub Actions", "url": "https://github.com/catalystneuro/reproduction-registry/actions/runs/39708723196"}},
 "outcomes": outcomes,
 "findings": [
  {"kind": "data_missing", "statement": ("The dandiset holds no output of the six spike sorters the paper compares, "
     "including the Kilosort2 run that the two experts curated. Every comparison of sorters in the paper, and the "
     "comparison of the curations with Kilosort2, can be repeated only by running the sorters again, three of them "
     "in MATLAB, and a new Kilosort2 run will not give the units the curators worked on.")},
  {"kind": "metadata_insufficient", "statement": ("The two curated files hold spike times only, with no sampling "
     "rate, no unit labels, no curator name and no link to the Kilosort2 clusters they were curated from; which file "
     "is curator 1 and which curator 2 is not stated (the files differ only by session time, 15:55:42 and 15:55:43). "
     "Their spike times fall on whole frames at 30 kHz and match the mouse recording's clock.")},
  {"kind": "metadata_error", "statement": ("The retina recording is stored as unsigned 16-bit values centred near "
     "2048 and reaching 4096, consistent with raw counts of a 12-bit converter, while the file states a conversion "
     "of 1e-6 V per unit and no offset, which would put every channel near +2 mV. The converter's gain and offset are "
     "not in the file.")},
  {"kind": "metadata_insufficient", "statement": ("The electrode tables give location 'unknown' and filtering 'none' "
     "for every channel and placeholder group descriptions; the mouse recording has 248 channels where the paper "
     "says 246 are active, without marking which; the simulated file does not say which ground-truth cells are "
     "excitatory or inhibitory or what noise was added; the archive's species summary lists only house mouse though "
     "one recording is from a rat (its file gives 'rattus rattus').")},
  {"kind": "other", "statement": ("Every raw series is stored in chunks of one channel by 7911 to 26368 frames, "
     "so reading a stretch of all channels fetches one chunk per channel. Streamed from the archive at about 0.1 "
     "to 0.2 s per chunk, reading a whole recording would take 6.7 to 20 h.")},
  {"kind": "paper_inconsistency", "statement": ("The paper gives 226 of 351 curated units as 64.2%; 226/351 is "
     "64.39%.")},
 ],
}
class D(yaml.SafeDumper): pass
def str_rep(d, s):
    return d.represent_scalar("tag:yaml.org,2002:str", s)
D.add_representer(str, str_rep)
open("attempts/000034-buccino-2020-01.yaml","w").write(yaml.dump(rec, Dumper=D, sort_keys=False, width=110, allow_unicode=True))
PYEOF
python $TMPDIR/gen/make_attempt.py && grep -n ": .*: " attempts/000034-buccino-2020-01.yaml | grep -v "^\S*\s*- \|'" | head; python tools/entry.py check entries/000034-buccino-2020; grep -c "claim:" attempts/000034-buccino-2020-01.yaml; grep -n "outcome:" attempts/000034-buccino-2020-01.yaml | sort -k3 | awk '{print $3}' | uniq -c
```

```
0 error(s)
26
     23 blocked
      1 reproduced
```

**Agent calls Bash**

```bash
sed -n 1,75p attempts/000034-buccino-2020-01.yaml; python -c "
import yaml; d=yaml.safe_load(open('attempts/000034-buccino-2020-01.yaml')); c=yaml.safe_load(open('claims/000034/10.7554-elife.61834.yaml'))
print(sorted(o['claim'] for o in d['outcomes'])==sorted(x['id'] for x in c['claims']))
for o in d['outcomes']: print(o['claim'], o.get('notes','')[:60])"
```

```
schema_version: 2
id: 000034-buccino-2020-01
dataset:
  archive: dandi
  id: '000034'
  version: 0.211030.0713
  doi: 10.48324/dandi.000034/0.211030.0713
paper: doi:10.7554/elife.61834
date: '2026-10-22'
entry: 000034-buccino-2020
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-10
  runner:
    platform: GitHub Actions
[... 80 more lines not kept]
```

**Agent**

Every claim has an outcome. Checking the prose rules (no em dashes, no "rather", no ": " inside plain YAML scalars), then building the handover.

**Agent calls Bash**

```bash
grep -n -i "rather\|—" entries/000034-buccino-2020/* attempts/000034-buccino-2020-01.yaml; grep -n "^\s*\(notes\|statement\|- \)'\|: '" attempts/000034-buccino-2020-01.yaml | head; python -c "
import yaml
for p in ['attempts/000034-buccino-2020-01.yaml','entries/000034-buccino-2020/entry.yaml']:
    s=open(p).read()
    for i,l in enumerate(s.splitlines()):
        v=l.split(': ',1)[1] if ': ' in l.strip(' -') else l.strip(' -')
        if ': ' in v and not v.strip().startswith((\"'\",'\"')): print(p,i+1,l[:100])
"; python tools/entry.py handover entries/000034-buccino-2020; ls executed/000034-buccino-2020/handover
```

```
grep: entries/000034-buccino-2020/__pycache__: Is a directory
5:  id: '000034'
9:date: '2026-10-22'
199:  notes: 'Blocked because the claim depends on fig1b-unit-counts (the Kilosort2 run), which is blocked; its count
wrote executed/000034-buccino-2020/handover
10.7554-elife.61834.yaml
reproduce_buccino_2020.ipynb
si000034.py
```

**Agent calls Bash**

```bash
sed -i 's/compare_two_sorters of spikecomparison 0.2.6, defaults): curated 1 "/compare_two_sorters of spikecomparison 0.2.6, defaults). Curated 1 "/' $TMPDIR/gen/make_attempt.py && python $TMPDIR/gen/make_attempt.py && grep -n "notes: '" attempts/000034-buccino-2020-01.yaml; rm -rf entries/000034-buccino-2020/__pycache__; python tools/entry.py check entries/000034-buccino-2020; git status --short
```

```
0 error(s)
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
?? attempts/000034-buccino-2020-01.yaml
?? entries/000034-buccino-2020/
?? scripts
```

**Agent calls Bash**

```bash
ls -la .bashrc .profile .gitconfig .mcp.json scripts .idea .vscode 2>&1 | head -20
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 22 01:56 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 22 01:56 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 22 01:56 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 22 01:56 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 22 01:56 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 22 01:56 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 22 01:56 scripts
```

**Agent**

The entry ran clean and the verifier's handover is built in `executed/000034-buccino-2020/handover/`. Only 1 of the 24 claims could be tested, and it reproduced; the other 23 are blocked because the paper's six spike sorters cannot be run here. Nothing is committed.

**1. Outcomes** (`attempts/000034-buccino-2020-01.yaml`)

| Claim | Outcome |
|---|---|
| recordings-as-described (link) | reproduced (all 15 checks hold) |
| fig4a-curators-agree | blocked, not_runnable. It depends on the blocked fig1b-unit-counts. Computed anyway from the two curated files: 226 shared units of 351 (64.39%), exactly the paper's 226 and 351. The paper's 174 needs the Kilosort2 run. |
| fig1b, fig1c, fig1d, fig1s2, fig1s3-s4, fig2c, fig2s1a, fig2s1b, fig2d, fig2e (×3), fig3a, fig3b, fig3c, fig3s1 (×2), fig3d, fig3s2, fig4b, fig4c, fig4d (22 claims) | blocked, not_runnable |

**2. What was found about the dataset.** I pinned 0.211030.0713: the paper cites only the draft, and this is the only published version, with the same six files (same ids and sizes) as the draft.
- **Contents:** all four recordings and both curations are there, with the stated rates, channel counts, durations and 250 ground-truth units. No sorter output is deposited, including the Kilosort2 run the curators worked on.
- **Clocks:** on the first seconds read, the curated and ground-truth spike times line up with spikes in the raw traces (deepest trough at lag 0).
- **Curated files:** spike times only. They have no sampling rate, no unit labels, no link to the Kilosort2 clusters, and nothing says which file is curator 1.
- **Retina recording:** stored as raw 12-bit converter counts (centred near 2048, saturating at 4096), but the file says 1e-6 V per count with no offset. Recorded as a metadata error.
- **Missing descriptions:** electrode location and filtering are placeholders; nothing marks which 2 of the 248 mouse channels are inactive (the paper says 246); the simulated file does not record cell types; the archive's species summary omits the rat.
- **Streaming:** every raw series is stored one channel per chunk, so reading any recording whole would take 6.7 to 20 h.
- **Paper:** 226/351 is 64.39%; the paper prints 64.2%.
- **Questions asked:** none. The one tested claim was fully specified.

**3. Protocol gaps**
1. The rule "a claim that depends on a blocked claim is blocked" forced fig4a to blocked even though its curator counts were computed and match. I followed the rule and put the numbers in the notes. The protocol has no outcome for a claim tested only in part because one of its parts is blocked.
2. When sorting software cannot run, `not_runnable` and `too_large` overlap: streaming alone would also exceed the time limit. I used not_runnable, citing MATLAB/GPU as the main reason and the measured streaming times in the notes.
3. The paper-era libraries (spikecomparison 0.2.6, spikeextractors 0.8.4) do not run on the fixed Python 3.13 with NumPy 2. The protocol says nothing about restoring removed library names. I restored five NumPy aliases (`np.float` and others) to their original meanings, which changes no computation, and recorded it as a deviation. The multi-sorter comparison in the same library also fails under pandas 2 and later, but every claim that uses it needs sorter outputs anyway.
4. The protocol's 10-minute aim is hard to meet when the data check itself needs slow raw reads. I read only the first chunk of each recording.

**4. Runtime and failures.** The notebook ran in 288 s. One exploratory metadata listing timed out at 20 minutes, because walking every electrode column is very slow over the network; targeted reads replaced it. HerdingSpikes 0.3.7 failed to build; Tridesclous 1.6.0 and SpyKING Circus 0.9.7 installed, but SpyKING Circus has no MPI to run with. Some empty device files (`.bashrc`, `scripts` and others) appear as untracked in `git status`; they come from the sandbox, not from me, and I left them alone.

Files are in `entries/000034-buccino-2020/`:
- `reproduce_buccino_2020.ipynb`
- `si000034.py`
- `entry.yaml`
- `requirements.in` and its lock file
- `README.md`

## End of run

48 turns, 58 minutes, result: success.
