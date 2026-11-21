# hiraoka-2025 · author · run 44950987917

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries claims attempts paper tools
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
3	Version: `pilot-18`. Record this version in the attempt's provenance.
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
[... 760 more lines not kept]
```

```
Sat Nov 21 21:25:47 UTC 2026
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
[... 1109 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -100; wc -l docs/design.md docs/archives.md paper/*; cat claims/hiraoka-2025.yaml; cat papers/datasets/hiraoka-2025.yaml; ls papers/author-notes | grep hira; ls questions | grep hira
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/hiraoka-2025.yaml; echo ----; cat papers/datasets/hiraoka-2025.yaml; ls papers/author-notes | grep hira; ls questions | grep hira; wc -l docs/design.md docs/archives.md paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1063-5.0296506.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the archives doc (DANDI section) and the newest entry for formats.

**Agent calls Bash**

```bash
sed -n 1,140p docs/archives.md; ls -la entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; ls entries/grosmark-2016-000044 2>/dev/null
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
[... 164 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/fouke-2025-01.yaml; cat entries/fouke-2025/README.md; head -c 3000 entries/fouke-2025/omr.py
```

```
<persisted-output>
Output too large (40.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d5f43af1-6c78-4069-b9cb-7cb9365aab6e/tool-results/b28jhqz6v.txt

Preview (first 2KB):
schema_version: 3
id: fouke-2025-01
datasets:
- archive: dandi
  id: "001453"
  version: 0.250518.1950
  doi: 10.48324/dandi.001453/0.250518.1950
  relation: primary
paper: doi:10.1016/j.cub.2025.04.027
date: 2026-10-14
entry: fouke-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
f=/home/runner/.claude/projects/-home-runner-work-encore-encore/d5f43af1-6c78-4069-b9cb-7cb9365aab6e/tool-results/b28jhqz6v.txt; grep -n "^[a-z_]*:" $f; sed -n '/^deviations:/,/^verifications:/p' $f | head -60; sed -n '/^findings:/,$p' $f | head -50
```

```
Permission for this tool use was denied. It requires approval, and this session has no approval surface — nobody can answer a permission prompt here — so it was denied automatically. The action was NOT performed; do not claim it succeeded, and do not retry it: this action, and anything else that requires approval, will be denied the same way for the rest of this session. Tell the user what was blocked and why you needed it, then continue with the parts of the task that do not require approval. What required approval: This Bash command contains multiple operations. The following parts require approval: f=/home/runner/.claude/projects/-home-runner-work-encore-encore/d5f43af1-6c78-4069-b9cb-7cb9365aab6e/tool-results/b28jhqz6v.txt; grep -n "^[a-z_]*:" $f; sed -n '/^deviations:/,/^verifications:/p' $f, head -60; sed -n '/^findings:/,$p' $f
```

**Agent calls Grep**

```json
{
 "pattern": "^[a-z_]+:|^  [a-z_]+:|^- [a-z_]+:",
 "path": "attempts/fouke-2025-01.yaml",
 "output_mode": "content",
 "head_limit": 120
}
```

```
1:schema_version: 3
2:id: fouke-2025-01
3:datasets:
4:- archive: dandi
5:  id: "001453"
6:  version: 0.250518.1950
7:  doi: 10.48324/dandi.001453/0.250518.1950
8:  relation: primary
9:paper: doi:10.1016/j.cub.2025.04.027
10:date: 2026-10-14
11:entry: fouke-2025
12:provenance:
13:  kind: agent
14:  accountable:
16:  agent:
20:  runner:
23:inputs:
24:- what: Names of the stimulus codes (the conversion of stimulus names to codes, its printed list of
30:  source: https://gitlab.oit.duke.edu/ean26/danionella_omr_neuralcircuits2025 at commit
32:- what: Stimulus names in protocol order, from the protocol file
[... 102 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/fouke-2025-01.yaml",
 "offset": 238
}
```

```
238	  notes: Needs the imaging and the head-fixed tail tracking, neither of which is in the dandiset.
239	- claim: fig4hi-vspn-lateralized
240	  outcome: blocked
241	  blocked_by: data_missing
242	  notes: Needs the imaging, the tail tracking and the registration to the mapzebrain atlas, none
243	    of which is in the dandiset.
244	findings:
245	- kind: data_missing
246	  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
247	    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
248	    the GitLab repository the paper names for all behavioural and imaging data holds analysis
249	    notebooks only. Nine of the paper's main findings cannot be tested.
250	- kind: metadata_insufficient
251	  statement: The stimulus codes 0 to 20 have no names or description in the files or the
252	    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
253	    file of its stimulus software.
254	- kind: code_mismatch
255	  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
256	    while its conversion of the stimulus software's names gives the reverse (it carries a remap
257	    that swaps them). The data do not settle which is right; zebrafish barely turn to either, and
[... 393 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas; python tools/entry.py --help 2>&1 | head -30; ls questions | head -3; sed -n 1,80p docs/design.md | head -5
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES] [--fresh] [--python PYTHON]
                [--before BEFORE]
                {lock,check,run,all,handover,upgrade-python,hash}
                entry [entry ...]

Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
[... 22 more lines not kept]
```

**Agent**

Now the dandiset itself.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000044/versions/ | python -m json.tool | grep -E '"version"|"status"|"modified"|"size"|"asset_count"'; curl -s "https://api.dandiarchive.org/api/dandisets/000044/versions/0.210812.1516/assets/?page_size=100" | python -c "
import json,sys; d=json.load(sys.stdin); print(d['count'])
for a in d['results']: print(a['path'], a['size'], a['asset_id'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
python -c "import h5py, remfile, pynwb, numpy, scipy; print(pynwb.__version__)" 2>&1; python -c "import powerlaw; print(powerlaw.__version__)" 2>&1; python --version; uv --version; nproc; free -g
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import h5py, remfile, pynwb, numpy, scipy; print(pynwb.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'h5py'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import powerlaw; print(powerlaw.__version__)
    ^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'powerlaw'
Python 3.13.18
uv 0.13.9 (x86_64-unknown-linux-gnu)
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          12           0           2          14
Swap:              2           0           2
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q h5py remfile pynwb numpy scipy pandas powerlaw matplotlib jupyter nbclient ipykernel 2>&1 | tail -3; python -c "import powerlaw,pynwb; print(powerlaw.__version__, pynwb.__version__)"
```

```
2.0.0 4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import h5py, remfile, requests, json, time
t=time.time()
V='0.210812.1516'
r=requests.get(f'https://api.dandiarchive.org/api/dandisets/000044/versions/{V}/assets/?page_size=100').json()
a=[x for x in r['results'] if 'Achilles-10252013' in x['path']][0]
info=requests.get(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/").json()
url=[u for u in info['contentUrl'] if 's3' in u][0]; print(url)
f=h5py.File(remfile.File(url),'r')
def walk(g,p=''):
    for k,v in g.items():
        if k in ('acquisition',) : 
            print('acq keys', list(v.keys())); continue
        if isinstance(v,h5py.Dataset): print(p+'/'+k, v.shape, v.dtype, dict((kk,str(vv)[:80]) for kk,vv in v.attrs.items() if kk in('unit','description','resolution','conversion')))
        else:
            print(p+'/'+k+'/', dict((kk,str(vv)[:100]) for kk,vv in v.attrs.items() if kk in ('neurodata_type','description')))
            walk(v,p+'/'+k)
for k in f.keys():
    if k=='acquisition': print('acquisition', list(f[k].keys())); continue
    walk(f[k],'/'+k)
print(time.time()-t)
EOF
python survey.py 2>&1 | grep -v "processing/.*/data\b" | head -150
```

```
https://dandiarchive.s3.amazonaws.com/blobs/4f5/a84/4f5a84aa-a6e4-496a-9b23-535fa6fbd3ae
acquisition []
Traceback (most recent call last):
  File "/tmp/claude-1001/survey.py", line 19, in <module>
    walk(f[k],'/'+k)
    ~~~~^^^^^^^^^^^^
  File "/tmp/claude-1001/survey.py", line 10, in walk
    for k,v in g.items():
               ^^^^^^^
AttributeError: 'Dataset' object has no attribute 'items'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import re
s=open('survey.py').read()
s=s.replace("""for k in f.keys():
    if k=='acquisition': print('acquisition', list(f[k].keys())); continue
    walk(f[k],'/'+k)""","walk(f)")
open('survey.py','w').write(s)
EOF
python survey.py 2>&1 | head -200
```

```
https://dandiarchive.s3.amazonaws.com/blobs/4f5/a84/4f5a84aa-a6e4-496a-9b23-535fa6fbd3ae
acq keys []
/analysis/ {}
/file_create_date (1,) object {}
/general/ {}
/general/devices/ {}
/general/devices/Device/ {'description': 'Silicon electrodes on Ampliplex probe; all probes were implanted parallel to the ', 'neurodata_type': 'Device'}
/general/experimenter (1,) object {}
/general/extracellular_ephys/ {}
/general/extracellular_ephys/electrodes/ {'description': 'metadata about extracellular electrodes', 'neurodata_type': 'DynamicTable'}
/general/extracellular_ephys/electrodes/bad_electrode (128,) bool {'description': 'Indicator for if the electrode was removed from analysis due to low-amplitude or'}
/general/extracellular_ephys/electrodes/filtering (128,) object {'description': 'description of hardware filtering'}
/general/extracellular_ephys/electrodes/group (128,) object {'description': 'a reference to the ElectrodeGroup this electrode is a part of'}
/general/extracellular_ephys/electrodes/group_name (128,) object {'description': 'the name of the ElectrodeGroup this electrode is a part of'}
/general/extracellular_ephys/electrodes/id (128,) int64 {}
/general/extracellular_ephys/electrodes/imp (128,) float64 {'description': 'the impedance of the channel'}
/general/extracellular_ephys/electrodes/location (128,) object {'description': 'the location of channel within the subject e.g. brain region'}
/general/extracellular_ephys/electrodes/shank_electrode_number (128,) int64 {'description': '0-indexed channel within a shank.'}
/general/extracellular_ephys/electrodes/x (128,) float64 {'description': 'the x coordinate of the channel location'}
/general/extracellular_ephys/electrodes/y (128,) float64 {'description': 'the y coordinate of the channel location'}
[... 107 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > u.py <<'EOF'
import h5py, remfile, numpy as np
url='https://dandiarchive.s3.amazonaws.com/blobs/4f5/a84/4f5a84aa-a6e4-496a-9b23-535fa6fbd3ae'
f=h5py.File(remfile.File(url),'r')
u=f['units']; ids=u['id'][:]; idx=u['spike_times_index'][:]; st=u['spike_times'][:]
ct=u['cell_type'][:].astype(str); loc=u['location'][:].astype(str); sh=u['shank_id'][:]
print('ids',ids[:15], ids.max(), len(ids)); print(np.unique(ct,return_counts=True)); print(np.unique(loc,return_counts=True))
print('shank_id', sh[:30])
ep=f['intervals/epochs']; print(ep['label'][:], ep['start_time'][:], ep['stop_time'][:])
print('session', f['session_description'][()], f['general/session_id'][()], f['session_start_time'][()])
print('related', f['general/related_publications'][:])
start=np.r_[0,idx[:-1]]
for i in range(len(ids)):
    s=st[start[i]:idx[i]]; d=np.diff(s)*1000
    print(i, ids[i], ct[i], sh[i], len(s), round(d.min(),3) if len(d) else None, round(d.max(),1) if len(d) else None, 'sorted' if np.all(d>=0) else 'UNSORTED', (d==0).sum())
print('spike range', st.min(), st.max())
EOF
python u.py
```

```
ids [ 1  2  6  7  9 11 12 13 16 18 20 21 22 23 27] 272 137
(array(['excitatory', 'inhibitory'], dtype='<U10'), array([120,  17]))
(array(['lCA1', 'rCA1'], dtype='<U4'), array([65, 72]))
shank_id [ 0  1  5  6  8 10 11 12 15 17 19 20 21 22 26 27 28  3  3  1  3  8  9 10
 11 12 13 14 15 16]
[b'PREEpoch' b'MazeEpoch' b'POSTEpoch'] [    0.  18079.5 20147. ] [18079.5    20147.     34861.1032]
session b'This data set is composed of eight bilateral silicon-probe multi-cellular electrophysiological ' b'Achilles_10252013' b'2013-10-25T00:00:00-04:00'
related [b'Grosmark, A.D., and Buzs\xc3\xa1ki, G. (2016). Diversity in neural firing dynamics supports both rigid and learned hippocampal sequences. Science 351, 1440\xe2\x80\x931443.'
 b'Chen, Z., Grosmark, A.D., Penagos, H., and Wilson, M.A. (2016). Uncovering representations of sleep-associated hippocampal ensemble spike activity. Sci. Rep. 6, 32193.']
0 1 excitatory 0 34006 0.85 91522.4 sorted 0
1 2 inhibitory 1 295084 0.85 23649.9 sorted 0
2 6 excitatory 5 6485 8.05 117496.1 sorted 0
3 7 excitatory 6 50906 0.85 43495.7 sorted 0
4 9 excitatory 8 9077 0.95 148695.9 sorted 0
5 11 excitatory 10 15083 0.85 120000.5 sorted 0
6 12 excitatory 11 45325 0.85 36890.9 sorted 0
7 13 excitatory 12 28260 0.85 77927.6 sorted 0
8 16 excitatory 15 36797 0.85 62212.8 sorted 0
9 18 inhibitory 17 228356 1.05 18229.7 sorted 0
10 20 inhibitory 19 344348 0.85 11780.2 sorted 0
[... 128 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cat > t.py <<'EOF'
import h5py, remfile, numpy as np, time, powerlaw, warnings, resource
warnings.filterwarnings('ignore')
url='https://dandiarchive.s3.amazonaws.com/blobs/4f5/a84/4f5a84aa-a6e4-496a-9b23-535fa6fbd3ae'
f=h5py.File(remfile.File(url),'r')
idx=f['units/spike_times_index'][:]
s=f['units/spike_times'][idx[8]:idx[9]]*1000
np.save('u18.npy', s)
tau=np.diff(s)
def bursts(tau, d):
    cut=np.flatnonzero(tau>d)
    edges=np.r_[0,cut+1,len(tau)+1]
    return np.diff(edges)
grid=10**np.arange(0,5,0.01)
mx=np.array([bursts(tau,d).max() for d in grid]); m=np.array([len(bursts(tau,d)) for d in grid])
lo=grid[np.argmax(mx>=100)]; hi=grid[np.flatnonzero(m>=100)[-1]]
print('relevant', lo, hi)
for d in [55,140,370,940,2400,6300]:
    b=bursts(tau,d)
    for disc in [True,False]:
        for xm in [None,1]:
            t=time.time()
            F=powerlaw.Fit(b,discrete=disc,xmin=xm,verbose=False)
            R,p=F.distribution_compare('power_law','exponential',normalized_ratio=True)
            print(d,len(b),b.max(),disc,xm,round(F.xmin,1),round(F.alpha,3),round(F.sigma,3),round(R,2),p, round(time.time()-t,2))
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
EOF
python t.py
```

```
Exit code 1
Sat Nov 21 21:28:17 UTC 2026
relevant 56.23413251903491 6165.9500186148225
55 88805 94 True None 4.0 2.912 0.015 14.61 2.2578520054830035e-48 0.21
Traceback (most recent call last):
  File "/tmp/claude-1001/t.py", line 24, in <module>
    print(d,len(b),b.max(),disc,xm,round(F.xmin,1),round(F.alpha,3),round(F.sigma,3),round(R,2),p, round(time.time()-t,2))
                                                         ^^^^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/powerlaw/fitting.py", line 347, in __getattr__
    raise AttributeError(name)
AttributeError: alpha
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && sed -i 's/round(F.alpha,3),round(F.sigma,3)/round(F.power_law.alpha,3),round(F.power_law.sigma,3)/' t.py && sed -i "s#^s=f\['units.*#s=np.load('u18.npy')#; s#^idx=.*##; s#^f=h5py.*##" t.py && python t.py
```

```
relevant 56.23413251903491 6165.9500186148225
55 88805 94 True None 4.0 2.912 0.015 14.61 2.2578520054830035e-48 0.21
55 88805 94 True 1 1.0 1.948 0.003 -4.74 2.100028524161384e-06 0.12
55 88805 94 False None 1.0 2.617 0.005 75.79 0.0 0.22
55 88805 94 False 1 1.0 2.617 0.005 75.79 0.0 0.03
140 47401 401 True None 8.0 2.489 0.019 18.43 7.019506579853405e-76 0.27
140 47401 401 True 1 1.0 1.73 0.003 18.0 2.0880503263865975e-72 0.04
140 47401 401 False None 8.0 2.64 0.021 21.45 4.65883190620823e-102 0.23
140 47401 401 False 1 1.0 2.103 0.005 42.52 0.0 0.02
370 22548 844 True None 12.0 2.334 0.02 18.36 2.614025702113159e-75 0.26
370 22548 844 True 1 1.0 1.53 0.004 12.06 1.6455051690824182e-33 0.02
370 22548 844 False None 14.0 2.416 0.024 19.42 5.483445312437755e-84 0.22
370 22548 844 False 1 1.0 1.716 0.005 26.15 9.247122842695953e-151 0.01
940 7760 3568 True None 29.0 2.297 0.032 10.65 1.780730010949587e-26 0.09
940 7760 3568 True 1 1.0 1.374 0.004 4.99 6.181185012880832e-07 0.01
940 7760 3568 False None 29.0 2.327 0.033 10.93 8.625499866773476e-28 0.07
940 7760 3568 False 1 1.0 1.464 0.005 9.65 4.842077782454346e-22 0.0
2400 1340 48441 True None 134.0 2.368 0.079 2.95 0.0032150133661620743 0.04
2400 1340 48441 True 1 1.0 1.248 0.007 0.98 0.3290328487460614 0.0
2400 1340 48441 False None 134.0 2.375 0.08 2.96 0.0031074603491150115 0.03
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > s.py <<'EOF'
import h5py, remfile, numpy as np, requests, time
for V in ['0.210812.1516','0.261106.0236']:
    r=requests.get(f'https://api.dandiarchive.org/api/dandisets/000044/versions/{V}/assets/?page_size=100').json()
    for a in sorted(r['results'],key=lambda x:x['path']):
        m=requests.get(f"https://api.dandiarchive.org/api/dandisets/000044/versions/{V}/assets/{a['asset_id']}/").json()
        print(V, a['path'].split('/')[-1], a['size'], m.get('digest',{}).get('dandi:dandi-etag'), [u for u in m['contentUrl'] if 's3' in u][0][-36:])
EOF
python s.py
```

```
0.210812.1516 sub-Achilles_ses-Achilles-10252013_behavior+ecephys.nwb 8737990464 c938bde98b18c45c10d1b77196b4ce73-131 4f5a84aa-a6e4-496a-9b23-535fa6fbd3ae
0.210812.1516 sub-Achilles_ses-Achilles-11012013_behavior+ecephys.nwb 9189442768 bbd5278c9a4dc50a3ab2aaf220c2ec6d-137 75a14b2b-05f2-4bb1-abcb-e2af85579af2
0.210812.1516 sub-Buddy_ses-Buddy-06272013_behavior+ecephys.nwb 5237757153 dc9cfac539499d864c8b10bbc002a2a7-79 98b25cb1-310c-45f7-97cc-669fce2057b7
0.210812.1516 sub-Cicero_ses-Cicero-09012014_behavior+ecephys.nwb 8681533792 9efe0f7a7613fe5799d8c6e9d7e8cf92-130 ced32609-16ab-4c4c-991f-8fa9f40e9401
0.210812.1516 sub-Cicero_ses-Cicero-09102014_behavior+ecephys.nwb 9122396663 ea1f2dfff75c7f595f040ba67c7fb4b4-136 6b8206bd-2829-48d9-95fc-e713cb3d363a
0.210812.1516 sub-Cicero_ses-Cicero-09172014_behavior+ecephys.nwb 8357219071 91574ad86a1088e6edc08f2c6bfea6bc-125 12fdc641-306b-4c83-8112-8244e4a846e1
0.210812.1516 sub-Gatsby_ses-Gatsby-08022013_behavior+ecephys.nwb 7943570110 d0d883f8a6ba45eedb5389732db54d03-119 810e9d83-a8f3-475a-9a71-634659b1c690
0.210812.1516 sub-Gatsby_ses-Gatsby-08282013_behavior+ecephys.nwb 8439009562 5482165e91bf7b199209054bd8174ae1-126 560a7710-50a3-4a16-9a5b-d079310eaa1f
0.261106.0236 sub-Achilles_ses-Achilles-10252013_behavior+ecephys.nwb 9745823699 ae10fdf48406481221f8a133c688248a-146 170bca2e-c8ef-4a96-bb54-38a6e5dc6d8f
0.261106.0236 sub-Achilles_ses-Achilles-11012013_behavior+ecephys.nwb 10437759803 87889a8539dff2d90d9a3b830520943d-156 4062c448-8063-4339-814e-694898316f1e
0.261106.0236 sub-Buddy_ses-Buddy-06272013_behavior+ecephys.nwb 5440961437 89d9aff6aba557fe7ba6db9e4964930e-82 276a351e-f701-4de8-9e53-9c633f70d02d
0.261106.0236 sub-Cicero_ses-Cicero-09012014_behavior+ecephys.nwb 9824661232 1f1c1c57fffbe34d8543f02367627f0d-147 852e3c46-bea6-4d13-a85e-9a40dd8b1232
0.261106.0236 sub-Cicero_ses-Cicero-09102014_behavior+ecephys.nwb 10282435393 69a123330c20b4c927b71be595c1ddcf-154 6dd64378-b98b-4195-a8aa-7db2a9b8a817
0.261106.0236 sub-Cicero_
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > s2.py <<'EOF'
import h5py, remfile, numpy as np
for b in ['4f5/a84/4f5a84aa-a6e4-496a-9b23-535fa6fbd3ae','170/bca/170bca2e-c8ef-4a96-bb54-38a6e5dc6d8f']:
    f=h5py.File(remfile.File('https://dandiarchive.s3.amazonaws.com/blobs/'+b),'r')
    u=f['units']; print(b, list(u.keys()), len(u['id']), u['id'][:10], np.diff(np.r_[0,u['spike_times_index'][:]])[:10])
    print(list(f['processing'].keys()), list(f['intervals'].keys()), list(f['acquisition'].keys()))
    if 'cell_type' in u: print(u['cell_type'][:10])
EOF
python s2.py
```

```
4f5/a84/4f5a84aa-a6e4-496a-9b23-535fa6fbd3ae ['cell_type', 'id', 'location', 'shank_id', 'spike_times', 'spike_times_index'] 137 [ 1  2  6  7  9 11 12 13 16 18] [ 34006 295084   6485  50906   9077  15083  45325  28260  36797 228356]
['behavior', 'ecephys'] ['epochs'] []
[b'excitatory' b'inhibitory' b'excitatory' b'excitatory' b'excitatory'
 b'excitatory' b'excitatory' b'excitatory' b'excitatory' b'inhibitory']
170/bca/170bca2e-c8ef-4a96-bb54-38a6e5dc6d8f ['cell_type', 'cluster_id', 'electrode_group', 'electrodes', 'electrodes_index', 'hemisphere', 'id', 'spike_group', 'spike_times', 'spike_times_index'] 137 [102 103 107 108 110 112 113 114 117 119] [ 34006 295084   6485  50906   9077  15083  45325  28260  36797 228356]
['behavior', 'ecephys'] ['epochs', 'trials'] ['accelerometer', 'neck_emg']
[b'pyramidal cell' b'interneuron' b'pyramidal cell' b'pyramidal cell'
 b'pyramidal cell' b'pyramidal cell' b'pyramidal cell' b'pyramidal cell'
 b'pyramidal cell' b'interneuron']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
mkdir -p entries/hiraoka-2025; cd $TMPDIR && . dev/bin/activate && python -c "
import powerlaw, inspect; src=inspect.getsource(powerlaw.Fit.distribution_compare); print(src[:1500])"; python -c "import powerlaw,inspect; print(inspect.signature(powerlaw.Fit.__init__))"
```

```
def distribution_compare(self, dist1, dist2, nested=None, **kwargs):
        """
        Returns the loglikelihood ratio, and its p-value, between the two
        distribution fits, assuming the candidate distributions are nested.

        Parameters
        ----------
        dist1 : str
            Name of the first candidate distribution (eg. 'power_law')

        dist2 : str
            Name of the second candidate distribution (eg. 'exponential')

        nested : bool or None, optional
            Whether to assume the candidate distributions are nested versions
            of each other. If None (default), the function will automatically
            set nested=True if one distribution name is a substring of the other
            (i.e., if either dist1 in dist2 or dist2 in dist1). Otherwise, it
            will assume nested=False.

[... 24 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/hiraoka-2025/bursttree.py",
 "content": "\"\"\"Bursty trains, merging numbers and power-law fits for Hiraoka & Jo (2025) on DANDI:000044.\n\nPaper: T. Hiraoka and H.-H. Jo, \"Hierarchical organization of bursty trains in event\nsequences\", doi:10.1063/5.0296506 (text read: the arXiv preprint body under paper/).\nClaims: claims/hiraoka-2025.yaml. Where a parameter comes from is said beside it:\n\n- \"Methods\" means Section II of the paper, as the claims file's opening comment gives it.\n- O1 to O4 are the open details named in the claims file's opening comment.\n- \"Assumption\" marks a choice this attempt made where neither source fixes it.\n- \"Standard choice\" marks a detail that cannot change an outcome.\n\nData are streamed from the DANDI archive at the pinned version (DANDI_VERSION); nothing is\nwritten to disk.\n\"\"\"\nfrom __future__ import annotations\n\nimport warnings\n\nimport h5py\nimport numpy as np\nimport remfile\nimport requests\n\nDANDISET = \"000044\"\n# The version the paper cites (ref. 39: https://dandiarchive.org/dandiset/000044/0.210812.1516).\nDANDI_VERSION = \"0.210812.1516\"\n# The latest published version, read only to show how it differs from the cited one.\nLATEST_VERSION = \"0.261106.0236\"\nAPI = \"https://api.dandiarchive.org/api\"\n\n# Methods: relevant timescales are those with max burst size >= 100 and >= 100 bursts.\nMIN_MAX_BURST = 100\nMIN_BURSTS = 100\n# Claims file, O3: a power law is supported when R > 0 and p < 0.05 (Figure 2 legend).\nP_SUPPORT = 0.05\n# Claims file, O4: grid (a) geometric with ratio 1.82, grid (b) log10 step 0.052,\n# both from the lower end of the relevant range.\nGRIDS = {\"a\": np.log10(1.82), \"b\": 0.052}\n# Figure 2 legend: merging-number pairs delta = r * delta' for the neuron.\nNEURON_RATIOS = (3.3, 5.9, 11.0)\n# Claims file, O3: the four fit readings (xmin by KS or xmin = 1; discrete or continuous).\nREADINGS = {\n    \"ks_discrete\": dict(xmin=None, discrete=True),\n    \"ks_continuous\": dict(xmin=None, discrete=False),\n    \"x1_discrete\": dict(xmin=1, discrete=True),\n    \"x1_continuous\": dict(xmin=1, discrete=False),\n}\n\n\n# ---------------------------------------------------------------- archive access\ndef list_assets(version: str = DANDI_VERSION) -> list[dict]:\n    \"\"\"Assets of the dandiset at a version: path, size, asset id and S3 URL.\"\"\"\n    url = f\"{API}/dandisets/{DANDISET}/versions/{version}/assets/?page_size=200\"\n    out = []\n    while url:\n        page = requests.get(url, timeout=60).json()\n        for a in page[\"results\"]:\n            meta = requests.get(\n                f\"{API}/dandisets/{DANDISET}/versions/{version}/assets/{a['asset_id']}/\", timeout=60\n            ).json()\n            s3 = [u for u in meta[\"contentUrl\"] if \"s3\" in u][0]\n            out.append(dict(path=a[\"path\"], size=a[\"size\"], asset_id=a[\"asset_id\"], url=s3))\n        url = page.get(\"next\")\n    return sorted(out, key=lambda a: a[\"path\"])\n\n\ndef open_nwb(url: str) -> h5py.File:\n    \"\"\"Open a streamed NWB file with h5py (read only).\"\"\"\n    return h5py.File(remfile.File(url), \"r\")\n\n\ndef _str(a):\n    return np.array([x.decode() if isinstance(x, bytes) else str(x) for x in a])\n\n\ndef load_units(f: h5py.File) -> dict:\n    \"\"\"The units table: ids, every column, and spike times per unit (seconds, as stored).\"\"\"\n    u = f[\"units\"]\n    idx = u[\"spike_times_index\"][:]\n    st = u[\"spike_times\"][:]\n    start = np.r_[0, idx[:-1]]\n    out = {\"id\": u[\"id\"][:], \"spikes\": [st[a:b] for a, b in zip(start, idx)]}\n    for k in u.keys():\n        if k in (\"id\", \"spike_times\", \"spike_times_index\") or k.endswith(\"_index\"):\n            continue\n        d = u[k]\n        if d.ndim == 1 and d.shape[0] == len(idx):\n            v = d[:]\n            out[k] = _str(v) if v.dtype.kind in \"OSU\" else v\n    return out\n\n\ndef load_epochs(f: h5py.File) -> dict:\n    e = f[\"intervals/epochs\"]\n    return dict(label=_str(e[\"label\"][:]), start=e[\"start_time\"][:], stop=e[\"stop_time\"][:])\n\n\n# ---------------------------------------------------------------- bursts (Methods)\ndef iets(times_ms: np.ndarray) -> np.ndarray:\n    \"\"\"Interevent times tau_i = t_(i+1) - t_i (Methods).\"\"\"\n    return np.diff(np.sort(times_ms))\n\n\ndef burst_sizes(tau: np.ndarray, delta: float) -> np.ndarray:\n    \"\"\"Sizes of the bursts at timescale delta: maximal runs whose IETs are all <= delta (Methods).\"\"\"\n    cut = np.flatnonzero(tau > delta)\n    edges = np.r_[0, cut + 1, len(tau) + 1]\n    return np.diff(edges)\n\n\ndef merging_numbers(tau: np.ndarray, dprime: float, delta: float) -> np.ndarray:\n    \"\"\"Merging numbers k_j: bursts at delta' that make up the j-th burst at delta (Eqs. 2-3).\n\n    Within a burst at delta, every IET in (delta', delta] separates two bursts at delta', so\n    k_j = 1 + the number of such IETs inside burst j.\n    \"\"\"\n    assert dprime < delta\n    burst_of_iet = np.r_[0, np.cumsum(tau > delta)][:-1]\n    inside = tau <= delta\n    m = int((tau > delta).sum()) + 1\n    k = 1 + np.bincount(burst_of_iet[inside], weights=(tau[inside] > dprime), minlength=m)\n    return k.astype(np.int64)\n\n\ndef relevant_range(tau: np.ndarray) -> tuple[float, float]:\n    \"\"\"Relevant timescales (Methods), computed exactly from the IETs.\n\n    Lower end: the smallest delta with max burst size >= 100, the smallest over all runs of\n    100 consecutive events of their largest IET. Upper end: delta must stay below the 99th\n    largest IET for m_delta >= 100; the returned bound is that IET (exclusive).\n    \"\"\"\n    w = MIN_MAX_BURST - 1\n    if len(tau) < max(w, MIN_BURSTS):\n        return np.nan, np.nan\n    lo = np.lib.stride_tricks.sliding_window_view(tau, w).max(axis=1).min()\n    hi = np.sort(tau)[-(MIN_BURSTS - 1)]\n    return float(lo), float(hi)\n\n\ndef grid(lo: float, hi: float, step_log10: float) -> np.ndarray:\n    \"\"\"Geometric grid of delta from the lower end of the relevant range (claims file, O4).\"\"\"\n    if not np.isfinite(lo) or hi <= lo:\n        return np.array([])\n    n = int(np.floor(np.log10(hi / lo) / step_log10 + 1e-9)) + 1\n    g = lo * 10 ** (step_log10 * np.arange(n))\n    return g[g < hi]\n\n\ndef pairs_on_grid(g: np.ndarray, hi: float, ratios=NEURON_RATIOS) -> list[tuple[float, float, float]]:\n    \"\"\"(delta', delta, ratio) with delta' on the grid and delta = ratio * delta' inside the range.\"\"\"\n    return [(dp, r * dp, r) for r in ratios for dp in g if r * dp < hi]\n\n\n# ---------------------------------------------------------------- fits (Methods, O3)\ndef fit(x: np.ndarray, reading: str) -> dict:\n    \"\"\"Maximum-likelihood power-law fit and likelihood-ratio test against an exponential.\n\n    Uses the powerlaw package (Alstott et al., ref. 37 of the paper, implementing Clauset et al.,\n    ref. 36): Fit(...) and distribution_compare('power_law', 'exponential'). The readings of the\n    lower cutoff and of discreteness are those of the claims file, O3.\n    \"\"\"\n    import powerlaw\n\n    x = np.asarray(x, dtype=float)\n    kw = READINGS[reading]\n    out = dict(reading=reading, n=len(x), xmax=float(x.max()) if len(x) else np.nan)\n    if len(x) < 2 or np.unique(x).size < 2:\n        out.update(alpha=np.nan, sigma=np.nan, xmin=np.nan, n_tail=0, R=np.nan, p=np.nan, supported=False)\n        return out\n    with warnings.catch_warnings():\n        warnings.simplefilter(\"ignore\")\n        F = powerlaw.Fit(x, verbose=False, **kw)\n        try:\n            R, p = F.distribution_compare(\"power_law\", \"exponential\")\n        except Exception:  # a failed test is counted as not supported and reported\n            R, p = np.nan, np.nan\n    out.update(\n        alpha=float(F.power_law.alpha),\n        sigma=float(F.power_law.sigma),\n        xmin=float(F.xmin),\n        n_tail=int((x >= F.xmin).sum()),\n        R=float(R),\n        p=float(p),\n        supported=bool(np.isfinite(R) and R > 0 and p < P_SUPPORT),\n    )\n    return out\n\n\ndef analyse_sequence(times_ms, grid_name=\"b\", ratios=NEURON_RATIOS, readings=tuple(READINGS),\n                     extra_pairs=()) -> dict:\n    \"\"\"Burst-size fits on the grid and merging-number fits on the pairs, under each reading.\n\n    Returns relevant range, grid, a list of burst rows (delta, reading, fit) and of pair rows\n    (delta', delta, ratio, reading, fit). Beta is also fitted at each pair's delta, which need\n    not be on the grid. `extra_pairs` adds fixed (delta', delta, ratio) pairs, such as the\n    labels of Figure 2.\n    \"\"\"\n    tau = iets(np.asarray(times_ms, dtype=float))\n    lo, hi = relevant_range(tau)\n    g = grid(lo, hi, GRIDS[grid_name])\n    prs = pairs_on_grid(g, hi, ratios) + list(extra_pairs)\n    deltas = sorted(set(np.round(np.r_[g, [p[0] for p in prs], [p[1] for p in prs]], 9)))\n    on_grid = set(np.round(g, 9))\n    bursts, pairs = [], []\n    for d in deltas:\n        b = burst_sizes(tau, d)\n        for r in readings:\n            row = fit(b, r)\n            row.update(delta=d, on_grid=d in on_grid, m=len(b), bmax=int(b.max()), bmean=float(b.mean()))\n            bursts.append(row)\n    for dp, d, ratio in prs:\n        k = merging_numbers(tau, dp, d)\n        for r in readings:\n            row = fit(k, r)\n            row.update(dprime=dp, delta=d, ratio=ratio, m=len(k), kmean=float(k.mean()),\n                       extra=(dp, d, ratio) in list(extra_pairs))\n            pairs.append(row)\n    return dict(n=len(tau) + 1, tau_min=float(tau.min()), tau_max=float(tau.max()), lo=lo, hi=hi,\n                grid=g, bursts=bursts, pairs=pairs)\n\n\ndef unit_pattern(times_ms, grid_name, reading, ratios=NEURON_RATIOS) -> dict:\n    \"\"\"Claim fig2-other-neurons-similar: does one unit show the pattern under one reading?\n\n    Pattern (criterion): power law supported for burst sizes at more than half of the unit's\n    relevant timescales on the grid, and for merging numbers at more than half of its pairs.\n    Units whose relevant range holds fewer than three grid points are not used.\n    \"\"\"\n    tau = iets(np.asarray(times_ms, dtype=float))\n    lo, hi = relevant_range(tau)\n    g = grid(lo, hi, GRIDS[grid_name])\n    out = dict(n=len(tau) + 1, lo=lo, hi=hi, n_grid=len(g))\n    if len(g) < 3:\n        out.update(used=False)\n        return out\n    bf = [fit(burst_sizes(tau, d), reading) for d in g]\n    prs = pairs_on_grid(g, hi, ratios)\n    kf = [fit(merging_numbers(tau, dp, d), reading) for dp, d, _ in prs]\n    nb = sum(x[\"supported\"] for x in bf)\n    nk = sum(x[\"supported\"] for x in kf)\n    betas = [x[\"alpha\"] for x in bf if np.isfinite(x[\"alpha\"])]\n    out.update(used=True, n_pairs=len(prs), b_supported=nb, k_supported=nk,\n               b_frac=nb / len(g), k_frac=nk / len(prs) if prs else np.nan,\n               median_beta=float(np.median(betas)) if betas else np.nan,\n               pattern=bool(nb > len(g) / 2 and len(prs) > 0 and nk > len(prs) / 2))\n    return out\n\n\n# ---------------------------------------------------------------- the model (Section IV)\ndef timescales(series: str, L: int, delta0=1.0, w=None) -> np.ndarray:\n    \"\"\"delta_l for l = 0..L: linear (Eq. 12), quadratic (Eq. 13) or exponential (Eq. 14).\n\n    Section IV: delta_0 = 1, w = 100 for linear and quadratic, w = 2 for exponential.\n    \"\"\"\n    l = np.arange(L + 1, dtype=float)\n    if series == \"linear\":\n        return delta0 + (100 if w is None else w) * l\n    if series == \"quadratic\":\n        return delta0 + (100 if w is None else w) * l ** 2\n    if series == \"exponential\":\n        return delta0 * (2 if w is None else w) ** l\n    raise ValueError(series)\n\n\ndef simulate_incremental(n: int, series: str, gamma: float, rng: np.random.Generator) -> np.ndarray:\n    \"\"\"Algorithm 2 (incremental), with memory function q(kappa) = (kappa/(kappa+1))^(gamma-1) (Eq. 16)\n    and uniform IETs on [delta_l, delta_(l+1)] (Eq. 10). Returns n event times, t_1 = 0.\"\"\"\n    L = 200\n    d = timescales(series, L)\n    kappa = np.zeros(L, dtype=np.int64)  # 0 = not set\n    t = np.empty(n)\n    t[0] = 0.0\n    i, l = 1, 0\n    e = gamma - 1.0\n    buf = rng.random(1 << 20)\n    bi = 0\n    while i < n:\n        if bi >= len(buf) - 2:\n            buf = rng.random(1 << 20)\n            bi = 0\n        if kappa[l] == 0:\n            kappa[l] = 1\n        r = buf[bi]; bi += 1\n        kp = kappa[l]\n        if r < (kp / (kp + 1.0)) ** e:\n            u = buf[bi]; bi += 1\n            t[i] = t[i - 1] + d[l] + (d[l + 1] - d[l]) * u\n            i += 1\n            kappa[l] = kp + 1\n            l = 0\n        else:\n            kappa[l] = 1\n            l += 1\n    return t\n\n\ndef simulate_decremental(n: int, series: str, gamma: float, rng: np.random.Generator) -> np.ndarray:\n    \"\"\"Algorithm 1 (decremental), merging numbers from the zeta distribution of Eq. 15, uniform IETs.\"\"\"\n    from scipy.stats import zipf\n\n    L = 200\n    d = timescales(series, L)\n    kappa = np.full(L, -1, dtype=np.int64)  # -1 = not set\n    t = np.empty(n)\n    t[0] = 0.0\n    i, l = 1, 0\n    ks = zipf.rvs(gamma, size=1 << 20, random_state=rng)\n    ki = 0\n    us = rng.random(1 << 20)\n    ui = 0\n    while i < n:\n        if kappa[l] <= 0:\n            if ki >= len(ks):\n                ks = zipf.rvs(gamma, size=1 << 20, random_state=rng); ki = 0\n            kappa[l] = ks[ki]; ki += 1\n        elif kappa[l] == 1:\n            kappa[l] = 0\n            l += 1\n        else:\n            if ui >= len(us):\n                us = rng.random(1 << 20); ui = 0\n            t[i] = t[i - 1] + d[l] + (d[l + 1] - d[l]) * us[ui]; ui += 1\n            i += 1\n            kappa[l] -= 1\n            l = 0\n    return t\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t2.py <<'EOF'
import sys, time, numpy as np, resource
sys.path.insert(0,'entries/hiraoka-2025')
import bursttree as bt
# synthetic check
t=np.array([0,1,2,10,11,30,31,32,33,100.])
tau=bt.iets(t)
print(bt.burst_sizes(tau,1.5), bt.burst_sizes(tau,25), bt.merging_numbers(tau,1.5,25))
s=np.load('u18.npy')
for g in 'ab':
    t0=time.time(); r=bt.analyse_sequence(s,g); print(g, len(r['grid']), len(r['bursts']), len(r['pairs']), round(time.time()-t0,1),'s', r['lo'], r['hi'])
t0=time.time(); x=bt.simulate_incremental(10**6,'linear',2.5,np.random.default_rng(1)); print('sim',time.time()-t0, np.diff(x).min(), np.diff(x).max())
t0=time.time(); y=bt.simulate_decremental(10**6,'linear',2.5,np.random.default_rng(1)); print('simdec',time.time()-t0, np.diff(y).min(), np.diff(y).max())
for ser in ['quadratic','exponential']:
    x=bt.simulate_incremental(10**6,ser,2.5,np.random.default_rng(1)); print(ser, np.diff(x).max(), bt.relevant_range(np.diff(x)))
t0=time.time(); r=bt.analyse_sequence(x,'a',ratios=(5.3,12,28),readings=('ks_discrete',)); print('model a ks_discrete', len(r['bursts']),len(r['pairs']),time.time()-t0)
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
EOF
python t2.py
```

```
[3 2 4 1] [9 1] [3 1]
a 8 92 60 8.9 s 55.24999999627471 6282.750000001863
b 40 460 300 36.3 s 55.24999999627471 6282.750000001863
sim 3.4424777030944824 1.0001262798905373 2637.1824001451023
simdec 2.220519542694092 1.0000758916139603 2662.6381247490644
quadratic 69518.6672076974 (92.34918728470802, 10520.275318920612)
exponential 91390461.70540738 (1.9134918749332428, 1277.2085364609957)
model a ks_discrete 33 22 8.898376703262329
0.314528 GB
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t3.py <<'EOF'
import sys, time, numpy as np
sys.path.insert(0,'entries/hiraoka-2025')
import bursttree as bt
t0=time.time()
A=bt.list_assets(); print('list',time.time()-t0)
tot=0
for a in A:
    f=bt.open_nwb(a['url']); u=f['units']; ct=bt._str(u['cell_type'][:]); n=np.diff(np.r_[0,u['spike_times_index'][:]])
    print(a['path'].split('/')[-1], len(ct), (ct=='excitatory').sum(), u['spike_times'].shape, u['spike_times'].chunks, f['intervals/epochs/label'][:])
    tot+=(ct=='excitatory').sum()
print(tot, time.time()-t0)
f=bt.open_nwb(A[0]['url']); t0=time.time(); x=f['units/spike_times'][:]; print('read st', time.time()-t0, x.shape)
EOF
python t3.py
```

```
list 1.216360092163086
sub-Achilles_ses-Achilles-10252013_behavior+ecephys.nwb 137 120 (8414607,) None [b'PREEpoch' b'MazeEpoch' b'POSTEpoch']
sub-Achilles_ses-Achilles-11012013_behavior+ecephys.nwb 104 92 (7665373,) None [b'PREEpoch' b'MazeEpoch' b'POSTEpoch']
sub-Buddy_ses-Buddy-06272013_behavior+ecephys.nwb 68 48 (6412255,) None [b'PREEpoch' b'MazeEpoch' b'POSTEpoch']
sub-Cicero_ses-Cicero-09012014_behavior+ecephys.nwb 73 55 (9158616,) None [b'PREEpoch' b'MazeEpoch' b'POSTEpoch']
sub-Cicero_ses-Cicero-09102014_behavior+ecephys.nwb 105 81 (13280381,) None [b'PREEpoch' b'MazeEpoch' b'POSTEpoch']
sub-Cicero_ses-Cicero-09172014_behavior+ecephys.nwb 72 59 (7708448,) None [b'PREEpoch' b'MazeEpoch' b'POSTEpoch']
sub-Gatsby_ses-Gatsby-08022013_behavior+ecephys.nwb 80 66 (5653138,) None [b'PREEpoch' b'MazeEpoch' b'POSTEpoch']
sub-Gatsby_ses-Gatsby-08282013_behavior+ecephys.nwb 51 41 (5775679,) None [b'PREEpoch' b'MazeEpoch' b'POSTEpoch']
562 10.593947649002075
read st 0.9156036376953125 (8414607,)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t4.py <<'EOF'
import sys, time, numpy as np
sys.path.insert(0,'entries/hiraoka-2025')
import bursttree as bt
A=bt.list_assets(); f=bt.open_nwb(A[0]['url']); U=bt.load_units(f)
exc=[i for i in range(len(U['id'])) if U['cell_type'][i]=='excitatory']
for i in exc[:40:5]:
    s=U['spikes'][i]*1000
    for g in 'ab':
        for r in bt.READINGS:
            t0=time.time(); o=bt.unit_pattern(s,g,r); 
            print(i,len(s),g,r,o.get('n_grid'),o.get('n_pairs'),o.get('b_supported'),o.get('k_supported'),o.get('pattern'),round(o.get('median_beta',np.nan),2),round(time.time()-t0,2))
EOF
python t4.py
```

```
0 34006 a ks_discrete 8 15 7 4 False 2.36 1.3
0 34006 a ks_continuous 8 15 7 8 True 2.44 0.63
0 34006 a x1_discrete 8 15 8 5 False 1.58 0.12
0 34006 a x1_continuous 8 15 8 13 True 1.81 0.06
0 34006 b ks_discrete 37 66 29 12 False 2.37 3.48
0 34006 b ks_continuous 37 66 29 41 True 2.5 2.74
0 34006 b x1_discrete 37 66 35 26 False 1.56 0.47
0 34006 b x1_continuous 37 66 37 58 True 1.78 0.25
6 45325 a ks_discrete 6 9 4 0 False 2.83 0.8
6 45325 a ks_continuous 6 9 5 3 False 2.86 0.7
6 45325 a x1_discrete 6 9 0 0 False 1.55 0.09
6 45325 a x1_continuous 6 9 4 4 False 1.75 0.05
6 45325 b ks_discrete 29 42 18 2 False 2.84 3.61
6 45325 b ks_continuous 29 42 22 15 False 2.8 3.13
6 45325 b x1_discrete 29 42 0 0 False 1.5 0.37
6 45325 b x1_continuous 29 42 21 16 False 1.66 0.19
13 8554 a ks_discrete 6 9 3 1 False 2.57 0.36
13 8554 a ks_continuous 6 9 4 3 False 2.68 0.28
13 8554 a x1_discrete 6 9 1 1 False 1.56 0.04
13 8554 a x1_continuous 6 9 6 9 True 1.78 0.02
[... 45 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/hiraoka-2025/bursttree.py",
 "old_string": "def grid(lo: float, hi: float, step_log10: float) -> np.ndarray:\n    \"\"\"Geometric grid of delta from the lower end of the relevant range (claims file, O4).\"\"\"\n    if not np.isfinite(lo) or hi <= lo:\n        return np.array([])\n    n = int(np.floor(np.log10(hi / lo) / step_log10 + 1e-9)) + 1\n    g = lo * 10 ** (step_log10 * np.arange(n))\n    return g[g < hi]",
 "new_string": "def grid(lo: float, hi: float, grid_name: str) -> np.ndarray:\n    \"\"\"Geometric grid of delta from the lower end of the relevant range (claims file, O4).\n\n    Grid (a): ratio 1.82 from the lower end. Grid (b): log10 step \"about 0.052\" (O4), made\n    exact by fitting a whole number of steps between the two ends of the range, as the\n    Figure 2 legend says the values shown \"span the entire range of relevant timescales\";\n    for the representative unit this gives 40 steps of 0.0514, of which every 5th point gives\n    the delta' labels (55, 100, 180, 330, 590 ms) and every 8th the delta labels (55, 140,\n    370, 940, 2400, 6300 ms). Points at or above the upper end are dropped (fewer than 100\n    bursts, Methods).\n    \"\"\"\n    if not np.isfinite(lo) or hi <= lo:\n        return np.array([])\n    span = np.log10(hi / lo)\n    step = GRIDS[grid_name]\n    if grid_name == \"b\":\n        step = span / max(1, round(span / step))\n    n = int(np.floor(span / step + 1e-9)) + 1\n    g = lo * 10 ** (step * np.arange(n))\n    return g[g < hi * (1 - 1e-12)]"
}
```

```
The file entries/hiraoka-2025/bursttree.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/hiraoka-2025 && sed -i 's/g = grid(lo, hi, GRIDS\[grid_name\])/g = grid(lo, hi, grid_name)/' bursttree.py && grep -n "grid(lo" bursttree.py
```

```
140:def grid(lo: float, hi: float, grid_name: str) -> np.ndarray:
213:    g = grid(lo, hi, grid_name)
244:    g = grid(lo, hi, grid_name)
```

**Agent calls Bash**

```bash
cat >> entries/hiraoka-2025/bursttree.py <<'EOF'


def unit_all_patterns(times_ms) -> list[dict]:
    """unit_pattern under both grids (O4) and the four fit readings (O3), for a worker pool."""
    out = []
    for g in GRIDS:
        for r in READINGS:
            row = unit_pattern(times_ms, g, r)
            row.update(grid=g, reading=r)
            out.append(row)
    return out


def ccdf_at(x: np.ndarray, at: np.ndarray) -> np.ndarray:
    """P(X >= a) for each a in `at` (complementary cumulative distribution)."""
    xs = np.sort(x)
    return 1.0 - np.searchsorted(xs, at, side="left") / len(xs)


def spike_counts(times_s: np.ndarray, edges: np.ndarray) -> np.ndarray:
    return np.histogram(times_s, edges)[0]
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import h5py,remfile
f=h5py.File(remfile.File('https://dandiarchive.s3.amazonaws.com/blobs/4f5/a84/4f5a84aa-a6e4-496a-9b23-535fa6fbd3ae'),'r')
g=f['processing/behavior/1.6mLinearMazePosition/1.6mLinearMazeSpatialSeries']
print(list(g.keys()), dict(g['starting_time'].attrs), g['starting_time'][()])
import numpy as np; d=g['data'][:]; print(np.nanmin(d,0),np.nanmax(d,0), np.isnan(d).mean())
s=f['processing/behavior/states']; print(np.unique(s['label'][:].astype(str),return_counts=True))
"
```

```
['data', 'reference_frame', 'starting_time'] {'rate': np.float64(0.025599910848541185), 'unit': 'seconds'} 18079.5
[-0.60002758 -0.57243482] [1.38465145 1.62845347] 0.21383819122854808
(array(['Awake', 'Non-REM', 'REM'], dtype='<U7'), array([62, 60, 22]))
Shell cwd was reset to
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/nbsrc && cat > $TMPDIR/nbsrc/build.py <<'EOF'
"""Build .ipynb from a percent-format source: '# %%' code, '# %% [md]' markdown, 'tags=a,b'."""
import sys, nbformat, re
src, dst = sys.argv[1], sys.argv[2]
cells = []; cur = None
for line in open(src).read().split('\n'):
    m = re.match(r'^# %%( \[md\])?(?: tags=(\S+))?\s*$', line)
    if m:
        if cur: cells.append(cur)
        cur = dict(md=bool(m.group(1)), tags=(m.group(2) or '').split(',') if m.group(2) else [], lines=[])
        continue
    cur['lines'].append(line)
cells.append(cur)
nb = nbformat.v4.new_notebook()
for c in cells:
    text = '\n'.join(c['lines']).strip('\n')
    if c['md']:
        text = '\n'.join(l[2:] if l.startswith('# ') else (l[1:] if l.startswith('#') else l) for l in text.split('\n'))
        cell = nbformat.v4.new_markdown_cell(text)
    else:
        cell = nbformat.v4.new_code_cell(text)
    if c['tags']: cell.metadata['tags'] = c['tags']
    nb.cells.append(cell)
nb.metadata['kernelspec'] = dict(name='python3', display_name='Python 3', language='python')
nbformat.write(nb, dst)
print(dst, len(nb.cells))
EOF
date -u
```

```
Sat Nov 21 21:34:45 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nbsrc/main.py",
 "content": "# %% [md]\n# # Reproducing Hiraoka & Jo (2025) on DANDI:000044: the representative neuron\n#\n# HEADER_PLACEHOLDER\n\n# %%\nimport time, resource, zlib\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom scipy.stats import spearmanr\nimport bursttree as bt\n\nT0 = time.time()\npd.set_option(\"display.width\", 200, \"display.max_columns\", 30, \"display.max_rows\", 200)\nPAPER = \"hiraoka-2025\"\nprint(\"dandiset\", bt.DANDISET, \"version\", bt.DANDI_VERSION)\n\n# %% [md]\n# ## Data check\n#\n# Every session of the pinned version is opened and its units table read (ids, every column,\n# spike times). Spike times are stored in seconds; the analysis uses milliseconds, as the paper\n# does. The checks: counts of units by session and cell type, that spike times are sorted, that\n# they fall inside the session's epochs, the epoch durations against the paper's description\n# (two four-hour rest periods around a 45-minute maze session), and whether any spike train is\n# deposited twice (identical spike count and times, within or across sessions).\n\n# %% tags=sanity\nassets = bt.list_assets()\nrows, units, epochs = [], {}, {}\nfor a in assets:\n    ses = a[\"path\"].split(\"ses-\")[1].split(\"_\")[0]\n    f = bt.open_nwb(a[\"url\"])\n    U = bt.load_units(f); E = bt.load_epochs(f)\n    units[ses], epochs[ses] = U, E\n    allsp = np.concatenate(U[\"spikes\"])\n    rows.append(dict(session=ses, subject=a[\"path\"].split(\"/\")[0], size_GB=round(a[\"size\"] / 1e9, 2),\n                     units=len(U[\"id\"]), excitatory=int((U[\"cell_type\"] == \"excitatory\").sum()),\n                     inhibitory=int((U[\"cell_type\"] == \"inhibitory\").sum()),\n                     columns=\",\".join(k for k in U if k != \"spikes\"),\n                     spikes=len(allsp), t_first_s=round(allsp.min(), 2), t_last_s=round(allsp.max(), 2),\n                     all_sorted=all(np.all(np.diff(s) >= 0) for s in U[\"spikes\"]),\n                     min_iet_ms=round(min(np.diff(s).min() for s in U[\"spikes\"] if len(s) > 1) * 1e3, 3),\n                     epochs=\" \".join(f\"{l}:{(b - a_) / 3600:.2f}h\" for l, a_, b in zip(E[\"label\"], E[\"start\"], E[\"stop\"])),\n                     session_end_s=round(E[\"stop\"].max(), 1)))\nsurvey = pd.DataFrame(rows)\nprint(survey.to_string())\nprint(\"units\", survey.units.sum(), \"excitatory\", survey.excitatory.sum(), \"inhibitory\", survey.inhibitory.sum())\nprint(\"locations:\", {s: dict(zip(*np.unique(u[\"location\"], return_counts=True))) for s, u in units.items()})\n# spikes inside the epochs\nfor s, U in units.items():\n    allsp = np.concatenate(U[\"spikes\"]); E = epochs[s]\n    inside = np.zeros(len(allsp), bool)\n    for a_, b in zip(E[\"start\"], E[\"stop\"]):\n        inside |= (allsp >= a_) & (allsp <= b)\n    print(f\"{s}: fraction of spikes inside an epoch {inside.mean():.6f}\")\n# duplicates: identical spike trains\nkeys = {}\nfor s, U in units.items():\n    for i, sp in enumerate(U[\"spikes\"]):\n        keys.setdefault((len(sp), round(float(sp[0]), 6), round(float(sp[-1]), 6)), []).append((s, int(U[\"id\"][i])))\ndups = {k: v for k, v in keys.items() if len(v) > 1}\nprint(\"spike trains sharing count, first and last spike:\", len(dups), dups if dups else \"\")\nsame_counts = pd.Series({s: tuple(np.sort([len(x) for x in U[\"spikes\"]])) for s, U in units.items()})\nprint(\"sessions with identical sorted spike-count lists:\", same_counts.duplicated(keep=False).sum())\n\n# %% [md]\n# ### Clock of the spikes and the behaviour\n#\n# The analysis uses spike times only; the epochs are used for one variant. To check that spikes\n# and the maze-epoch position share a clock, the summed rate of the excitatory units of the\n# representative session in 1 s bins is correlated with running speed, with the position shifted\n# in time. A shared clock gives a peak near zero shift. The position series stores\n# `starting_time` with an attribute `rate` (read below), which is checked against the epoch.\n\n# %%\nf = bt.open_nwb([a[\"url\"] for a in assets if \"Achilles-10252013\" in a[\"path\"]][0])\nps = f[\"processing/behavior/1.6mLinearMazePosition/1.6mLinearMazeSpatialSeries\"]\npos = ps[\"data\"][:]; t_start = float(ps[\"starting_time\"][()]); rate_attr = float(ps[\"starting_time\"].attrs[\"rate\"])\nE = epochs[\"Achilles-10252013\"]\nmaze = dict(zip(E[\"label\"], zip(E[\"start\"], E[\"stop\"])))[\"MazeEpoch\"]\nprint(f\"position samples {len(pos)}, starting_time {t_start} s, 'rate' attribute {rate_attr:.6f}\")\nprint(f\"span if 'rate' is in Hz: {len(pos) / rate_attr:.0f} s; span if it is the sampling interval: {len(pos) * rate_attr:.1f} s; maze epoch {maze[1] - maze[0]:.1f} s\")\nprint(f\"position range x {np.nanmin(pos[:,0]):.2f} to {np.nanmax(pos[:,0]):.2f} m, y {np.nanmin(pos[:,1]):.2f} to {np.nanmax(pos[:,1]):.2f} m; NaN fraction {np.isnan(pos[:,0]).mean():.3f}\")\ntp = t_start + rate_attr * np.arange(len(pos))  # the interval reading, which fits the epoch\nedges = np.arange(maze[0], maze[1], 1.0)\nidx = np.clip(np.searchsorted(tp, edges), 0, len(pos) - 1)\np1 = pos[idx]\nspeed = np.r_[np.hypot(*np.diff(p1, axis=0).T), np.nan]\nU = units[\"Achilles-10252013\"]\npop = sum(bt.spike_counts(s, np.r_[edges, edges[-1] + 1]) for s, c in zip(U[\"spikes\"], U[\"cell_type\"]) if c == \"excitatory\").astype(float)\nshifts = np.arange(-120, 121, 5)\ncc = []\nfor sh in shifts:\n    a_ = speed[max(0, sh): len(speed) + min(0, sh)]; b = pop[max(0, -sh): len(pop) + min(0, -sh)]\n    ok = np.isfinite(a_) & np.isfinite(b)\n    cc.append(np.corrcoef(a_[ok], b[ok])[0, 1])\ncc = np.array(cc)\nprint(\"correlation of excitatory population rate with speed, by shift of the position (s):\")\nprint(pd.Series(cc.round(3), index=shifts).to_string())\nprint(f\"peak at shift {shifts[np.nanargmax(cc)]} s, r = {np.nanmax(cc):.3f}; median |r| at shifts beyond 60 s {np.nanmedian(np.abs(cc[np.abs(shifts) > 60])):.3f}\")\n\n# %% [md]\n# ### Version check\n#\n# The paper cites version 0.210812.1516 (ref. 39), pinned here. The latest published version,\n# 0.261106.0236, renumbers the units and relabels the cell types; its units table for the\n# representative session is read to show the difference for the unit the claims use.\n\n# %%\nlatest = [a for a in bt.list_assets(bt.LATEST_VERSION) if \"Achilles-10252013\" in a[\"path\"]][0]\nfl = bt.open_nwb(latest[\"url\"]); UL = bt.load_units(fl)\nU = units[\"Achilles-10252013\"]\nprint(\"cited version columns:\", [k for k in U if k != \"spikes\"])\nprint(\"latest version columns:\", [k for k in UL if k != \"spikes\"])\ncmp = pd.DataFrame({\"cited_id\": U[\"id\"][:12], \"cited_type\": U[\"cell_type\"][:12], \"cited_n\": [len(s) for s in U[\"spikes\"][:12]],\n                    \"latest_id\": UL[\"id\"][:12], \"latest_type\": UL[\"cell_type\"][:12],\n                    \"latest_cluster_id\": UL.get(\"cluster_id\", np.full(len(UL[\"id\"]), -1))[:12], \"latest_n\": [len(s) for s in UL[\"spikes\"][:12]]})\nprint(cmp.to_string())\nsame = len(U[\"spikes\"]) == len(UL[\"spikes\"]) and all(len(a_) == len(b) and np.allclose(a_, b) for a_, b in zip(U[\"spikes\"], UL[\"spikes\"]))\nprint(\"same spike trains in the same order in both versions:\", same)\n\n# %% [md]\n# ## fig2-neuron-representative-sequence\n#\n# > The representative neuronal sequence (unit 9 of session Achilles-10252013) has 228 356\n# > spikes, with IETs from 1.05 ms to 1.82 x 10^4 ms.\n#\n# Criterion: the unit is found as in O1 (readings (a) units id 9, (b) row 9 counted from 0,\n# (c) the ninth unit counted from 1, (d) a cluster number 9 in the unit metadata, here the\n# `shank_id` column, described as \"0-indexed id of cluster identified from the shank\"), with all\n# spikes of the session (O2). Reproduced when under one reading all three values are within\n# tolerance (n 228 356 +/- 22 836, tau_min 1.05 +/- 0.105 ms, tau_max 18 200 +/- 1 820 ms).\n\n# %% tags=claim:fig2-neuron-representative-sequence\nU = units[\"Achilles-10252013\"]\ndef stats(i):\n    s = U[\"spikes\"][i] * 1e3; d = np.diff(s)\n    return dict(row=i, id=int(U[\"id\"][i]), cell_type=U[\"cell_type\"][i], shank_id=int(U[\"shank_id\"][i]), n=len(s),\n                tau_min_ms=round(d.min(), 3), tau_max_ms=round(d.max(), 1),\n                match=bool(abs(len(s) - 228356) <= 22835.6 and abs(d.min() - 1.05) <= 0.105 and abs(d.max() - 18200) <= 1820))\no1 = []\no1 += [dict(reading=\"(a) id 9\", **stats(i)) for i in np.flatnonzero(U[\"id\"] == 9)]\no1 += [dict(reading=\"(b) row 9 from 0\", **stats(9))]\no1 += [dict(reading=\"(c) ninth from 1\", **stats(8))]\no1 += [dict(reading=\"(d) shank_id 9\", **stats(i)) for i in np.flatnonzero(U[\"shank_id\"] == 9)]\no1 = pd.DataFrame(o1); print(o1.to_string())\nREP = 9\nprint(\"units in the session matching all three values:\", [int(U[\"id\"][i]) for i in range(len(U[\"id\"])) if stats(i)[\"match\"]])\n# the same row in the latest version\nprint(\"latest version, row 9:\", dict(id=int(UL[\"id\"][9]), cell_type=UL[\"cell_type\"][9], n=len(UL[\"spikes\"][9])),\n      \"; ids equal to 9 in latest:\", int((UL[\"id\"] == 9).sum()))\nspk = U[\"spikes\"][REP] * 1e3\ntau = bt.iets(spk)\nprint(f\"representative: n = {len(spk)}, tau_min = {tau.min():.3f} ms, tau_max = {tau.max():.1f} ms, cell_type {U['cell_type'][REP]}, location {U['location'][REP]}\")\n\n# %% [md]\n# ## fig2-iet-broad\n#\n# > The IETs of each process, the representative neuron included, extend across several orders\n# > of magnitude.\n#\n# Criterion: for the representative unit, reproduced when tau_max / tau_min >= 10^3.\n\n# %% tags=claim:fig2-iet-broad\nratio = tau.max() / tau.min()\nprint(f\"tau_max / tau_min = {ratio:.0f} ({np.log10(ratio):.2f} decades); paper 1.82e4 / 1.05 = {18200 / 1.05:.0f} ({np.log10(18200 / 1.05):.2f} decades)\")\nprint(\"IET percentiles (ms):\", dict(zip([0, 1, 50, 99, 100], np.percentile(tau, [0, 1, 50, 99, 100]).round(2))))\nh, e = np.histogram(tau, np.logspace(0, 4.5, 46), density=True)\nfig, ax = plt.subplots(figsize=(4, 3)); ax.loglog(np.sqrt(e[1:] * e[:-1]), h, \"o-\", ms=3)\nax.set_xlabel(\"tau (ms)\"); ax.set_ylabel(\"P(tau)\"); ax.set_title(\"IETs, representative unit\")\nprint(f\"IETs outside the plotted 1 to {10**4.5:.0f} ms: {(tau < 1).sum() + (tau > 10**4.5).sum()}\")\n\n# %% [md]\n# ## Bursts and merging numbers of the representative unit\n#\n# Relevant timescales, grids, bursts and fits as in the Methods and in O3 and O4 of the claims\n# file (the helper says where each detail comes from). Both grids are run under the four fit\n# readings. The pairs of Figure 2 (delta' = 55, 100, 180, 330, 590 ms; delta = 3.3, 5.9 and 11\n# delta') are added as fixed pairs for fig2-neuron-merging-collapse.\n\n# %%\nFIG2_PAIRS = [(dp, r * dp, r) for dp in (55, 100, 180, 330, 590) for r in bt.NEURON_RATIOS]\nt1 = time.time()\nRES = {g: bt.analyse_sequence(spk, g, extra_pairs=FIG2_PAIRS if g == \"b\" else ()) for g in bt.GRIDS}\nprint(f\"fits done in {time.time() - t1:.0f} s\")\nlo, hi = RES[\"a\"][\"lo\"], RES[\"a\"][\"hi\"]\nprint(f\"relevant timescales: {lo:.2f} ms (smallest delta with a burst of >= 100 events) to {hi:.2f} ms (the 99th largest IET; delta must stay below it for >= 100 bursts)\")\nprint(f\"paper (Figure 2 labels): about 55 to 6300 ms\")\nfor g in bt.GRIDS:\n    print(f\"grid ({g}): {len(RES[g]['grid'])} points, step log10 {np.log10(RES[g]['grid'][1] / RES[g]['grid'][0]):.4f}:\", RES[g][\"grid\"].round(1))\nB = pd.concat([pd.DataFrame(RES[g][\"bursts\"]).assign(grid=g) for g in bt.GRIDS], ignore_index=True)\nP = pd.concat([pd.DataFrame(RES[g][\"pairs\"]).assign(grid=g) for g in bt.GRIDS], ignore_index=True)\nprint(\"fits with a failed test (R or p not finite):\", int((~np.isfinite(B.R)).sum() + (~np.isfinite(P.R)).sum()), \"of\", len(B) + len(P))\n\n# %% [md]\n# ## fig2-neuron-burst-size-heavy-tail\n#\n# > For the representative neuron, the burst size distributions are heavy-tailed across different\n# > timescales.\n#\n# Criterion: at each delta of the grid (O4) over the relevant range, fit and test as in O3.\n# Reproduced when the power law is supported (R > 0, p < 0.05) at more than half of the relevant\n# timescales and at every one below 3000 ms; partially reproduced when at more than half but not\n# at every one below 3000 ms. As a reference, the same test is run on the IETs shuffled in time\n# (a renewal process, whose burst sizes decay exponentially; Introduction), under the claim's\n# seed and four more.\n\n# %% tags=claim:fig2-neuron-burst-size-heavy-tail\nBg = B[B.on_grid]\nsumm = []\nfor (g, r), d in Bg.groupby([\"grid\", \"reading\"]):\n    below = d[d.delta < 3000]\n    summ.append(dict(grid=g, reading=r, n_delta=len(d), supported=int(d.supported.sum()), frac=round(d.supported.mean(), 3),\n                     n_below3000=len(below), supported_below3000=int(below.supported.sum()),\n                     more_than_half=bool(d.supported.sum() > len(d) / 2), all_below3000=bool(below.supported.all())))\nsumm = pd.DataFrame(summ); print(summ.to_string())\nprint(\"\\nper delta, grid (a):\")\nprint(Bg[Bg.grid == \"a\"].pivot_table(index=\"delta\", columns=\"reading\", values=[\"alpha\", \"R\", \"p\"]).round(4).to_string())\nprint(\"\\nper delta, grid (b), supported (1) or not (0):\")\nprint(Bg[Bg.grid == \"b\"].pivot_table(index=\"delta\", columns=\"reading\", values=\"supported\").astype(int).to_string())\nprint(\"\\nunsupported, grid (b): \", Bg[(Bg.grid == \"b\") & ~Bg.supported][[\"reading\", \"delta\", \"alpha\", \"R\", \"p\", \"m\"]].round(4).to_string())\n# reference: shuffled IETs\nseed = zlib.crc32(f\"{PAPER}/fig2-neuron-burst-size-heavy-tail\".encode())\nref = []\nfor off in (0, 1000, 2000, 3000, 4000):\n    rng = np.random.default_rng(seed + off)\n    ts = np.r_[0, np.cumsum(rng.permutation(tau))]\n    tt = bt.iets(ts); g_ = bt.grid(*bt.relevant_range(tt), \"a\")\n    sup = [bt.fit(bt.burst_sizes(tt, d), \"ks_discrete\")[\"supported\"] for d in g_]\n    ref.append(dict(seed=seed + off, n_delta=len(g_), supported=int(sum(sup))))\nprint(\"\\nshuffled IETs (renewal reference), grid (a), ks_discrete:\"); print(pd.DataFrame(ref).to_string())\n\n# %% [md]\n# ## fig2-neuron-beta-stable\n#\n# > For neuronal spikes the fitted burst-size exponent stays near 2.35 for several decades of\n# > timescales, up to about 3000 ms.\n#\n# Criterion: beta at each delta of the grid from the lower end of the relevant range to 3000 ms,\n# fit of O3. Readings: (a) every estimate within 2.35 +/- 0.235; (b) the median within that band\n# and the range under 0.47. Reproduced when (a) or (b) holds under one reading of O3.\n\n# %% tags=claim:fig2-neuron-beta-stable\nst = []\nfor (g, r), d in Bg[Bg.delta < 3000].groupby([\"grid\", \"reading\"]):\n    a_ = d.alpha.values\n    st.append(dict(grid=g, reading=r, n=len(a_), median=round(np.median(a_), 3), min=round(a_.min(), 3), max=round(a_.max(), 3),\n                   range=round(np.ptp(a_), 3), max_sigma=round(d.sigma.max(), 3),\n                   all_in_band=bool(np.all(np.abs(a_ - 2.35) <= 0.235)),\n                   median_in_band_range_ok=bool(abs(np.median(a_) - 2.35) <= 0.235 and np.ptp(a_) < 0.47)))\nst = pd.DataFrame(st); print(st.to_string())\nprint(\"\\nbeta per delta below 3000 ms (grid a), with standard errors:\")\nprint(Bg[(Bg.grid == \"a\") & (Bg.delta < 3000)].pivot_table(index=\"delta\", columns=\"reading\", values=[\"alpha\", \"sigma\", \"xmin\"]).round(3).to_string())\nfig, ax = plt.subplots(figsize=(5, 3))\nfor r, d in Bg[Bg.grid == \"b\"].groupby(\"reading\"):\n    ax.semilogx(d.delta, d.alpha, \"o-\", ms=3, label=r)\nax.axhspan(2.35 - 0.235, 2.35 + 0.235, color=\"0.9\"); ax.axvline(3000, ls=\":\", c=\"k\")\nax.set_xlabel(\"delta (ms)\"); ax.set_ylabel(\"beta\"); ax.legend(fontsize=7)\nprint(\"plotted beta range (grid b):\", Bg[Bg.grid == \"b\"].alpha.min().round(3), \"to\", Bg[Bg.grid == \"b\"].alpha.max().round(3))\n\n# %% [md]\n# ## fig2-neuron-merging-heavy-tail\n#\n# > For the representative neuron, the merging-number distributions are heavy-tailed for various\n# > pairs of timescales, and their fitted exponents gamma stay fairly constant across a wide range\n# > of timescales.\n#\n# Criterion: pairs delta = 3.3, 5.9 and 11 delta', delta' on the grid (O4), both in the relevant\n# range; fit and test as in O3. Reproduced when the power law is supported for more than half of\n# the pairs and the gamma of those pairs has an interquartile range below 0.5; partially\n# reproduced when only the first holds.\n\n# %% tags=claim:fig2-neuron-merging-heavy-tail\nPg = P[~P.extra]\nmh = []\nfor (g, r), d in Pg.groupby([\"grid\", \"reading\"]):\n    s = d[d.supported].alpha\n    iqr = float(np.subtract(*np.percentile(s, [75, 25]))) if len(s) else np.nan\n    mh.append(dict(grid=g, reading=r, n_pairs=len(d), supported=int(d.supported.sum()), frac=round(d.supported.mean(), 3),\n                   gamma_median=round(s.median(), 3) if len(s) else np.nan, gamma_iqr=round(iqr, 3),\n                   gamma_min=round(s.min(), 3) if len(s) else np.nan, gamma_max=round(s.max(), 3) if len(s) else np.nan,\n                   more_than_half=bool(d.supported.sum() > len(d) / 2), iqr_below_05=bool(iqr < 0.5)))\nmh = pd.DataFrame(mh); print(mh.to_string())\nprint(\"\\ngamma per pair, grid (a):\")\nprint(Pg[Pg.grid == \"a\"].pivot_table(index=[\"ratio\", \"dprime\"], columns=\"reading\", values=\"alpha\").round(3).to_string())\nprint(\"\\nsupported per pair, grid (a):\")\nprint(Pg[Pg.grid == \"a\"].pivot_table(index=[\"ratio\", \"dprime\"], columns=\"reading\", values=\"supported\").astype(int).to_string())\n\n# %% [md]\n# ## fig2-neuron-merging-collapse\n#\n# > Rescaled merging-number distributions for different pairs of delta and delta' collapse onto\n# > each other, so the burst tree is self-similar across levels.\n#\n# Criterion, the pairs of Figure 2 (delta' = 55, 100, 180, 330, 590 ms, each with delta = 3.3,\n# 5.9 and 11 delta'): (a) the complementary cumulative distributions of k / <k> differ by no more\n# than a factor of 2 at every point where all are above 10^-3; (b) the gamma estimates lie within\n# +/- 0.5 of their median (under a reading of O3). Reproduced when either holds. The points are\n# 200 values of k / <k> spaced logarithmically from 0.01 to 1000 (a standard choice).\n\n# %% tags=claim:fig2-neuron-merging-collapse\nxs = np.logspace(-2, 3, 200)\ncurves = {}\nfor dp, d, r in FIG2_PAIRS:\n    k = bt.merging_numbers(tau, dp, d)\n    curves[(dp, r)] = bt.ccdf_at(k / k.mean(), xs)\nC = np.array(list(curves.values()))\nok = np.all(C > 1e-3, axis=0)\nfac = C[:, ok].max(axis=0) / C[:, ok].min(axis=0)\nprint(f\"pairs: {len(curves)}; points where all CCDFs exceed 1e-3: {ok.sum()} (k/<k> from {xs[ok].min():.3f} to {xs[ok].max():.2f})\")\nprint(f\"largest ratio between the highest and lowest CCDF at those points: {fac.max():.2f} at k/<k> = {xs[ok][fac.argmax()]:.2f}; median ratio {np.median(fac):.2f}\")\nprint(f\"(a) holds: {bool(fac.max() <= 2)}\")\n# excluding the smallest k/<k> where CCDF = 1 for all, how do the curves differ in the tail only (k/<k> >= 1)?\ntail = ok & (xs >= 1)\nprint(f\"in the tail alone (k/<k> >= 1): max ratio {(C[:, tail].max(0) / C[:, tail].min(0)).max():.2f}\")\nPf = P[P.extra]\ncg = []\nfor r_, d in Pf.groupby(\"reading\"):\n    med = d.alpha.median()\n    cg.append(dict(reading=r_, median=round(med, 3), max_dev=round((d.alpha - med).abs().max(), 3),\n                   within_05=bool(((d.alpha - med).abs() <= 0.5).all()), supported=int(d.supported.sum()), m_min=int(d.m.min())))\nprint(pd.DataFrame(cg).to_string())\nprint(Pf.pivot_table(index=[\"dprime\", \"ratio\"], columns=\"reading\", values=\"alpha\").round(3).to_string())\nprint(\"pairs of Figure 2 with delta beyond the relevant range:\", [(dp, round(d, 0)) for dp, d, r in FIG2_PAIRS if d >= hi])\nfig, ax = plt.subplots(figsize=(4, 3))\nfor (dp, r), c in curves.items():\n    ax.loglog(xs, np.where(c > 0, c, np.nan), lw=0.8)\nax.set_xlabel(\"k / <k>\"); ax.set_ylabel(\"P(K >= k)\"); ax.set_ylim(1e-5, 1.5)\n\n# %% [md]\n# ## fig2-exponents-above-two\n#\n# > In most cases both gamma and the burst-size exponent at the smaller timescale exceed 2, so the\n# > scaling relation reduces to beta at delta equal to the smaller of gamma and beta at delta',\n# > which agrees with the observations.\n#\n# Criterion, for the pairs of fig2-neuron-merging-heavy-tail with the fit of O3: (1) in more than\n# half of the pairs both gamma and beta(delta') exceed 2; (2) in more than half, beta(delta) is\n# within 10% of min(gamma, beta(delta')). Reproduced when both hold, partially when only (1).\n\n# %% tags=claim:fig2-exponents-above-two\nkey = lambda x: np.round(x, 9)\nbmap = {(g, r, key(d)): a_ for g, r, d, a_ in B[[\"grid\", \"reading\", \"delta\", \"alpha\"]].itertuples(index=False)}\nX = Pg.copy()\nX[\"beta_dprime\"] = [bmap[(g, r, key(dp))] for g, r, dp in X[[\"grid\", \"reading\", \"dprime\"]].itertuples(index=False)]\nX[\"beta_delta\"] = [bmap[(g, r, key(d))] for g, r, d in X[[\"grid\", \"reading\", \"delta\"]].itertuples(index=False)]\nX[\"pred\"] = np.minimum(X.alpha, X.beta_dprime)\nX[\"both_gt2\"] = (X.alpha > 2) & (X.beta_dprime > 2)\nX[\"eq8_10pct\"] = (X.beta_delta - X.pred).abs() <= 0.1 * X.pred\nea = X.groupby([\"grid\", \"reading\"]).agg(n_pairs=(\"alpha\", \"size\"), both_gt2=(\"both_gt2\", \"sum\"), eq8_within10=(\"eq8_10pct\", \"sum\"),\n                                         median_rel_err=(\"pred\", lambda s: np.nan)).reset_index()\nea[\"median_rel_err\"] = [np.median(np.abs(d.beta_delta - d.pred) / d.pred) for _, d in X.groupby([\"grid\", \"reading\"])]\nea[\"cond1\"] = ea.both_gt2 > ea.n_pairs / 2; ea[\"cond2\"] = ea.eq8_within10 > ea.n_pairs / 2\nprint(ea.round(3).to_string())\nprint(\"\\ngrid (a), per pair:\")\nprint(X[X.grid == \"a\"][[\"reading\", \"dprime\", \"delta\", \"ratio\", \"alpha\", \"beta_dprime\", \"beta_delta\", \"pred\", \"both_gt2\", \"eq8_10pct\"]].round(3).to_string())\n\n# %% [md]\n# ## fig2-neuron-beta-decrease-follows-gamma\n#\n# > For neuronal spikes, beta is stable below 3000 ms, where beta at the smaller timescale is below\n# > gamma. Above 3000 ms beta decreases, apparently driven by a decreasing gamma.\n#\n# Criterion: (1) for pairs with delta < 3000 ms, beta(delta') < gamma in more than half; (2) for\n# delta > 3000 ms within the relevant range, beta has a negative Spearman correlation with log\n# delta; (3) over the same range, gamma has a negative Spearman correlation with log delta for at\n# least one of the three ratios. Reproduced when all three hold under one reading of O3, partially\n# when (1) and (2) hold. If the range above 3000 ms has fewer than three grid points, (2) and (3)\n# are reported and not judged. \"Negative\" is read as rho < 0; the p-value is shown.\n\n# %% tags=claim:fig2-neuron-beta-decrease-follows-gamma\ndec = []\nfor (g, r), d in X.groupby([\"grid\", \"reading\"]):\n    lowp = d[d.delta < 3000]\n    c1 = int((lowp.beta_dprime < lowp.alpha).sum())\n    bb = Bg[(Bg.grid == g) & (Bg.reading == r) & (Bg.delta > 3000)]\n    rho2, p2 = spearmanr(np.log(bb.delta), bb.alpha) if len(bb) >= 2 else (np.nan, np.nan)\n    gam = {}\n    for ratio_, dd in d[d.delta > 3000].groupby(\"ratio\"):\n        gam[ratio_] = (len(dd),) + (tuple(np.round(spearmanr(np.log(dd.delta), dd.alpha), 3)) if len(dd) >= 2 else (np.nan, np.nan))\n    judged = len(bb) >= 3\n    dec.append(dict(grid=g, reading=r, pairs_below3000=len(lowp), beta_dprime_lt_gamma=c1, cond1=bool(c1 > len(lowp) / 2),\n                    n_grid_above3000=len(bb), rho_beta=round(rho2, 3), p_beta=round(p2, 4), cond2=bool(rho2 < 0) if judged else None,\n                    gamma_by_ratio=gam, cond3=bool(any(v[1] < 0 for v in gam.values() if v[0] >= 2)) if judged else None))\ndec = pd.DataFrame(dec); print(dec.to_string())\nprint(\"\\nbeta above 3000 ms:\")\nprint(Bg[Bg.delta > 3000].pivot_table(index=[\"grid\", \"delta\"], columns=\"reading\", values=\"alpha\").round(3).to_string())\n\n# %% [md]\n# ### Variant (O2): the epochs taken separately\n#\n# The claims use all spikes of the session. As a variant, the representative unit is analysed in\n# each epoch alone (IETs across epoch boundaries removed), under grid (b) and the KS readings.\n\n# %%\nE = epochs[\"Achilles-10252013\"]\nvar = []\nfor lab, a_, b in zip(E[\"label\"], E[\"start\"] * 1e3, E[\"stop\"] * 1e3):\n    s = spk[(spk >= a_) & (spk <= b)]\n    rr = bt.analyse_sequence(s, \"b\", readings=(\"ks_discrete\", \"ks_continuous\"))\n    bb = pd.DataFrame(rr[\"bursts\"]); bb = bb[bb.on_grid]\n    pp = pd.DataFrame(rr[\"pairs\"])\n    for r_, d in bb.groupby(\"reading\"):\n        below = d[d.delta < 3000]\n        var.append(dict(epoch=lab, reading=r_, n=rr[\"n\"], lo=round(rr[\"lo\"], 1), hi=round(rr[\"hi\"], 1), n_delta=len(d),\n                        b_supported=int(d.supported.sum()), median_beta_below3000=round(below.alpha.median(), 3) if len(below) else np.nan,\n                        k_supported=int(pp[pp.reading == r_].supported.sum()), n_pairs=int((pp.reading == r_).sum())))\nprint(pd.DataFrame(var).to_string())\n\n# %% [md]\n# ## Summary\n#\n# SUMMARY_PLACEHOLDER\n\n# %%\nprint(f\"notebook time {(time.time() - T0) / 60:.1f} min, peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nbsrc/main.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python nbsrc/build.py nbsrc/main.py entries/hiraoka-2025/reproduce_hiraoka_2025.ipynb && cd entries/hiraoka-2025 && time jupyter nbconvert --to notebook --execute reproduce_hiraoka_2025.ipynb --output $TMPDIR/main_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | tail -5
```

```
entries/hiraoka-2025/reproduce_hiraoka_2025.ipynb 30
[NbConvertApp] Converting notebook reproduce_hiraoka_2025.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 182344 bytes to /tmp/claude-1001/main_out.ipynb

real	2m14.864s
user	1m43.755s
sys	0m2.270s
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > show.py <<'EOF'
import nbformat, sys
nb=nbformat.read(sys.argv[1],4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print(f'===== cell {i} {c.metadata.get("tags","")}')
    for o in c.outputs:
        if o.output_type=='stream': print(o.text[:int(sys.argv[2]) if len(sys.argv)>2 else 8000])
        elif o.output_type=='error': print('ERROR', o.ename, o.evalue)
        elif 'text/plain' in o.get('data',{}): print(o['data']['text/plain'][:300])
EOF
python show.py main_out.ipynb
```

```
<persisted-output>
Output too large (33.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d5f43af1-6c78-4069-b9cb-7cb9365aab6e/tool-results/bo9zenqjc.txt

Preview (first 2KB):
===== cell 1 
dandiset 000044 version 0.210812.1516

===== cell 3 ['sanity']
             session       subject  size_GB  units  excitatory  inhibitory                         columns    spikes  t_first_s  t_last_s  all_sorted   min_iet_ms                                          epochs  session_end_s
0  Achilles-10252013  sub-Achilles     8.74    137         120          17  id,cell_type,location,shank_id   8414607       0.04  34861.10        True         0.85  PREEpoch:5.02h MazeEpoch:0.57h POSTEpoch:4.09h        34861.1
1  Achilles-11012013  sub-Achilles     9.19    104          92          12  id,cell_type,location,shank_id   7665373       0.00  36629.21        True         0.85  PREEpoch:5.37h MazeEpoch:0.74h POSTEpoch:4.06h        36629.2
2     Buddy-06272013     sub-Buddy     5.24     68          48          20  id,cell_type,location,shank_id   6412255       0.08  21054.70       False -21054371.65  PREEpoch:2.98h MazeEpoch:0.65h POSTEpoch:2.22h        21054.7
3    Cicero-09012014    sub-Cicero     8.68     73          55          18  id,cell_type,location,shank_id   9158616       0.07  34756.80       False -34666502.85  PREEpoch:4.31h MazeEpoch:1.54h POSTEpoch:3.80h        34756.8
4    Cicero-09102014    sub-Cicero     9.12    105          81          24  id,cell_type,location,shank_id  13280381       0.00  36498.60        True         0.85  PREEpoch:4.79h MazeEpoch:0.84h POSTEpoch:4.51h        36498.6
5    Cicero-09172014    sub-Cicero     8.36     72          59          13  id,cell_type,location,shank_id   7708448       0.00  33560.19        True         0.85  PREEpoch:4.44h MazeEpoch:0.85h POSTEpoch:4.02h        33560.2
6    Gatsby-08022013    sub-Gatsby     7.94     80          66          14  id,cell_type,location,shank_id   5653138       0.
[... 3 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d5f43af1-6c78-4069-b9cb-7cb9365aab6e/tool-results/bo9zenqjc.txt"
}
```

```
1	===== cell 1 
2	dandiset 000044 version 0.210812.1516
3	
4	===== cell 3 ['sanity']
5	             session       subject  size_GB  units  excitatory  inhibitory                         columns    spikes  t_first_s  t_last_s  all_sorted   min_iet_ms                                          epochs  session_end_s
6	0  Achilles-10252013  sub-Achilles     8.74    137         120          17  id,cell_type,location,shank_id   8414607       0.04  34861.10        True         0.85  PREEpoch:5.02h MazeEpoch:0.57h POSTEpoch:4.09h        34861.1
7	1  Achilles-11012013  sub-Achilles     9.19    104          92          12  id,cell_type,location,shank_id   7665373       0.00  36629.21        True         0.85  PREEpoch:5.37h MazeEpoch:0.74h POSTEpoch:4.06h        36629.2
8	2     Buddy-06272013     sub-Buddy     5.24     68          48          20  id,cell_type,location,shank_id   6412255       0.08  21054.70       False -21054371.65  PREEpoch:2.98h MazeEpoch:0.65h POSTEpoch:2.22h        21054.7
9	3    Cicero-09012014    sub-Cicero     8.68     73          55          18  id,cell_type,location,shank_id   9158616       0.07  34756.80       False -34666502.85  PREEpoch:4.31h MazeEpoch:1.54h POSTEpoch:3.80h        34756.8
10	4    Cicero-09102014    sub-Cicero     9.12    105          81          24  id,cell_type,location,shank_id  13280381       0.00  36498.60        True         0.85  PREEpoch:4.79h MazeEpoch:0.84h POSTEpoch:4.51h        36498.6
11	5    Cicero-09172014    sub-Cicero     8.36     72          59          13  id,cell_type,location,shank_id   7708448       0.00  33560.19        True         0.85  PREEpoch:4.44h MazeEpoch:0.85h POSTEpoch:4.02h        33560.2
12	6    Gatsby-08022013    sub-Gatsby     7.94     80          66          14  id,cell_type,location,shank_id   5653138       0.01  32002.37       False -32000478.40  PREEpoch:4.74h MazeEpoch:0.65h POSTEpoch:3.06h        30413.6
13	7    Gatsby-08282013    sub-Gatsby     8.44     51          41          10  id,cell_t
[... 430 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > uns.py <<'EOF'
import sys, numpy as np
sys.path.insert(0,'entries/hiraoka-2025')
import bursttree as bt
A=bt.list_assets()
for a in A:
    if not any(s in a['path'] for s in ['Buddy','Cicero-09012014','Gatsby-08022013']): continue
    f=bt.open_nwb(a['url']); U=bt.load_units(f); E=bt.load_epochs(f)
    for i,s in enumerate(U['spikes']):
        d=np.diff(s); nb=(d<0).sum()
        if nb:
            j=np.flatnonzero(d<0)
            ss=np.sort(s); dup=(np.diff(ss)==0).sum()
            print(a['path'].split('ses-')[1][:18], 'row',i,'id',U['id'][i],U['cell_type'][i],'n',len(s),'breaks',nb,'at',j[:3],'values',s[j[0]-1:j[0]+3].round(3),'dup after sort',dup, 'first run end',s[j[0]].round(1), 'min', s.min().round(2), 'max', s.max().round(1))
    if 'Gatsby' in a['path']:
        allsp=np.concatenate(U['spikes']); print('epochs',E); 
        out=allsp[allsp>E['stop'].max()]; print('after end', len(out), out.min(), out.max())
        per=[(i,(s>E['stop'].max()).sum()) for i,s in enumerate(U['spikes']) if (s>E['stop'].max()).sum()]
        print('units with spikes after end', len(per), per[:10])
        gaps=[(E['stop'][k],E['start'][k+1]) for k in range(2)]; print('gaps',gaps)
EOF
python uns.py
```

```
Buddy-06272013_beh row 1 id 2 excitatory n 70899 breaks 1 at [65535] values [2.1054315e+04 2.1054679e+04 3.0800000e-01 4.5240000e+00] dup after sort 3 first run end 21054.7 min 0.31 max 21054.7
Cicero-09012014_be row 1 id 2 excitatory n 99358 breaks 1 at [65535] values [34756.752 34756.797    90.294   184.485] dup after sort 0 first run end 34756.8 min 90.29 max 34756.8
Gatsby-08022013_be row 1 id 2 inhibitory n 250254 breaks 1 at [131071] values [3.1999731e+04 3.2000504e+04 2.6000000e-02 8.1000000e-02] dup after sort 146 first run end 32000.5 min 0.03 max 32001.8
epochs {'label': array(['PREEpoch', 'MazeEpoch', 'POSTEpoch'], dtype='<U9'), 'start': array([    0. , 17079.2, 19414.3]), 'stop': array([17079.2  , 19414.3  , 30413.628])}
after end 263976 30413.62975 32002.3718
units with spikes after end 79 [(1, np.int64(9062)), (2, np.int64(11055)), (3, np.int64(243)), (4, np.int64(278)), (5, np.int64(491)), (6, np.int64(264)), (7, np.int64(1980)), (8, np.int64(252)), (9, np.int64(2203)), (10, np.int64(1063))]
gaps [(np.float64(17079.2), np.float64(17079.2)), (np.float64(19414.3), np.float64(19414.3))]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > uns2.py <<'EOF'
import sys, numpy as np
sys.path.insert(0,'entries/hiraoka-2025')
import bursttree as bt
A=bt.list_assets()
for a in A:
    if not any(s in a['path'] for s in ['Buddy','Cicero-09012014','Gatsby-08022013']): continue
    f=bt.open_nwb(a['url']); U=bt.load_units(f)
    s=U['spikes'][1]; j=np.flatnonzero(np.diff(s)<0)[0]+1
    r1,r2=s[:j],s[j:]
    print(a['path'].split('ses-')[1][:18], 'run1',len(r1),r1[0].round(2),r1[-1].round(1),'rate',round(len(r1)/(r1[-1]-r1[0]),3),'run2',len(r2),r2[0].round(2),r2[-1].round(1),'rate',round(len(r2)/(r2[-1]-r2[0]),3))
    print('  median IET run1 %.1f ms run2 %.1f ms'%(np.median(np.diff(r1))*1e3, np.median(np.diff(r2))*1e3))
    for i,o in enumerate(U['spikes']):
        if i==1: continue
        c2=np.isin(np.round(r2,5),np.round(o,5)).mean(); c1=np.isin(np.round(r1,5),np.round(o,5)).mean()
        if c2>0.05 or c1>0.05: print('  overlap with row',i,'id',U['id'][i],'run1 %.3f run2 %.3f'%(c1,c2), len(o))
    print('  dataset chunks', f['units/spike_times'].chunks, 'index dtype', f['units/spike_times_index'].dtype, f['units/spike_times_index'][:3])
EOF
python uns2.py
```

```
Buddy-06272013_beh run1 65536 5393.23 21054.7 rate 4.185 run2 5363 0.31 21032.8 rate 0.255
  median IET run1 43.1 ms run2 201.1 ms
  dataset chunks None index dtype uint32 [14678 85577 91267]
Cicero-09012014_be run1 65536 18931.91 34756.8 rate 4.141 run2 33822 90.29 34756.8 rate 0.976
  median IET run1 42.9 ms run2 143.2 ms
  dataset chunks None index dtype uint32 [  8316 107674 225143]
Gatsby-08022013_be run1 131072 7378.65 32000.5 rate 5.323 run2 119182 0.03 32001.8 rate 3.724
  median IET run1 44.1 ms run2 53.7 ms
  dataset chunks None index dtype uint32 [ 61964 312218 716537]
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nbsrc/pop.py",
 "content": "# %% [md]\n# # Hiraoka & Jo (2025) on DANDI:000044: the other neurons\n#\n# Paper: T. Hiraoka and H.-H. Jo, \"Hierarchical organization of bursty trains in event\n# sequences\", doi:10.1063/5.0296506, read from the arXiv preprint body under `paper/`.\n# Dataset: DANDI:000044 version 0.210812.1516, the version the paper cites (ref. 39); see the\n# header of `reproduce_hiraoka_2025.ipynb` for the choice of version and the claims table.\n# This notebook tests one claim, `fig2-other-neurons-similar`, which needs a fit of every\n# pyramidal unit and is kept apart for its run time (about 25 minutes on 4 processes).\n\n# %%\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\"); os.environ.setdefault(\"OPENBLAS_NUM_THREADS\", \"1\")\nimport time, resource\nfrom concurrent.futures import ProcessPoolExecutor\nimport numpy as np\nimport pandas as pd\nimport bursttree as bt\n\nT0 = time.time()\npd.set_option(\"display.width\", 200, \"display.max_columns\", 30, \"display.max_rows\", 300)\nprint(\"dandiset\", bt.DANDISET, \"version\", bt.DANDI_VERSION)\n\n# %% [md]\n# ## Data check\n#\n# The units tables of all eight sessions: counts by cell type, and spike trains that are not\n# sorted in time (the burst analysis sorts each train before taking IETs).\n\n# %% tags=sanity\nassets = bt.list_assets()\ntrains, rows = [], []\nfor a in assets:\n    ses = a[\"path\"].split(\"ses-\")[1].split(\"_\")[0]\n    U = bt.load_units(bt.open_nwb(a[\"url\"]))\n    uns = [int(U[\"id\"][i]) for i, s in enumerate(U[\"spikes\"]) if np.any(np.diff(s) < 0)]\n    rows.append(dict(session=ses, units=len(U[\"id\"]), excitatory=int((U[\"cell_type\"] == \"excitatory\").sum()),\n                     inhibitory=int((U[\"cell_type\"] == \"inhibitory\").sum()), unsorted_unit_ids=uns))\n    for i, s in enumerate(U[\"spikes\"]):\n        if U[\"cell_type\"][i] == \"excitatory\":\n            trains.append(dict(session=ses, row=i, id=int(U[\"id\"][i]), n=len(s), unsorted=int(U[\"id\"][i]) in uns, spikes_ms=s * 1e3))\nprint(pd.DataFrame(rows).to_string())\nprint(\"excitatory (pyramidal) units:\", len(trains), \"; of them with unsorted spike times:\", sum(t[\"unsorted\"] for t in trains))\nprint(\"spikes per excitatory unit: min\", min(t[\"n\"] for t in trains), \"median\", int(np.median([t[\"n\"] for t in trains])), \"max\", max(t[\"n\"] for t in trains))\n\n# %% [md]\n# ## fig2-other-neurons-similar\n#\n# > Other neurons of the recordings show patterns similar to the representative unit, with\n# > heavy-tailed burst-size and merging-number distributions across timescales.\n#\n# Criterion: the set is (a) the pyramidal units of session Achilles-10252013, or (b) the pyramidal\n# units of every session. \"Pyramidal\" is read as the `cell_type` value `excitatory`, the only\n# label for principal cells in this version. Only units whose relevant range holds at least three\n# grid points are used, with all spikes of the session (O2) and each fit of O3, under both grids\n# of O4. A unit shows the pattern when the power law is supported (R > 0, p < 0.05) for burst sizes\n# at more than half of its relevant timescales and for merging numbers at more than half of its\n# pairs (ratios 3.3, 5.9 and 11). Reproduced when more than half of the units show the pattern\n# under one reading. The distribution of each unit's median beta is reported.\n\n# %% tags=claim:fig2-other-neurons-similar\nt1 = time.time()\nwith ProcessPoolExecutor(max_workers=4) as ex:\n    res = list(ex.map(bt.unit_all_patterns, [t[\"spikes_ms\"] for t in trains], chunksize=2))\nprint(f\"{len(trains)} units fitted in {(time.time() - t1) / 60:.1f} min\")\nR = pd.DataFrame([dict(session=t[\"session\"], id=t[\"id\"], n_spikes=t[\"n\"], unsorted=t[\"unsorted\"], **r)\n                  for t, rr in zip(trains, res) for r in rr])\nR[\"set_a\"] = R.session == \"Achilles-10252013\"\n\ndef summarise(d):\n    used = d[d.used]\n    return pd.Series(dict(units=d.id.nunique(), used=len(used), pattern=int(used.pattern.sum()),\n                          frac_pattern=round(used.pattern.mean(), 3) if len(used) else np.nan,\n                          median_b_frac=round(used.b_frac.median(), 3), median_k_frac=round(used.k_frac.median(), 3),\n                          beta_q25=round(used.median_beta.quantile(0.25), 3), beta_median=round(used.median_beta.median(), 3),\n                          beta_q75=round(used.median_beta.quantile(0.75), 3)))\n\nprint(\"set (a), Achilles-10252013:\")\nprint(R[R.set_a].groupby([\"grid\", \"reading\"]).apply(summarise).to_string())\nprint(\"\\nset (b), all sessions:\")\nprint(R.groupby([\"grid\", \"reading\"]).apply(summarise).to_string())\nprint(\"\\nset (b) by session, fraction of used units showing the pattern:\")\nprint(R[R.used].pivot_table(index=\"session\", columns=[\"grid\", \"reading\"], values=\"pattern\", aggfunc=\"mean\").round(3).to_string())\nprint(\"\\nset (b) by session, median over units of the median beta:\")\nprint(R[R.used].pivot_table(index=\"session\", columns=[\"grid\", \"reading\"], values=\"median_beta\", aggfunc=\"median\").round(3).to_string())\nprint(\"\\nunits dropped (fewer than three grid points):\")\nprint(R[~R.used].groupby([\"grid\"]).id.count().to_string())\nprint(\"\\nwithout the units with unsorted spike times, set (b):\")\nprint(R[~R.unsorted].groupby([\"grid\", \"reading\"]).apply(summarise)[[\"used\", \"pattern\", \"frac_pattern\"]].to_string())\n\n# %% [md]\n# ### Burst sizes and merging numbers taken apart\n#\n# The pattern needs both parts. Their separate rates show which part fails where a reading\n# falls short.\n\n# %%\nused = R[R.used]\npart = used.assign(burst_ok=used.b_frac > 0.5, merge_ok=used.k_frac > 0.5).groupby([\"grid\", \"reading\"]).agg(\n    used=(\"id\", \"size\"), burst_ok=(\"burst_ok\", \"mean\"), merge_ok=(\"merge_ok\", \"mean\"), both=(\"pattern\", \"mean\"))\nprint(\"set (b):\"); print(part.round(3).to_string())\nparta = used[used.set_a].assign(burst_ok=lambda d: d.b_frac > 0.5, merge_ok=lambda d: d.k_frac > 0.5).groupby([\"grid\", \"reading\"]).agg(\n    used=(\"id\", \"size\"), burst_ok=(\"burst_ok\", \"mean\"), merge_ok=(\"merge_ok\", \"mean\"), both=(\"pattern\", \"mean\"))\nprint(\"\\nset (a):\"); print(parta.round(3).to_string())\nprint(f\"\\nnotebook time {(time.time() - T0) / 60:.1f} min, peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB (main process)\")\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && sed 's/^t1 = time.time()$/trains = trains[:6] + trains[200:206]\nt1 = time.time()/' nbsrc/pop.py > nbsrc/pop_sub.py && python nbsrc/build.py nbsrc/pop_sub.py entries/hiraoka-2025/sub_test.ipynb && cd entries/hiraoka-2025 && time jupyter nbconvert --to notebook --execute sub_test.ipynb --output $TMPDIR/pop_sub_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | tail -1; rm sub_test.ipynb; cd $TMPDIR && python show.py pop_sub_out.ipynb 3000
```

```
entries/hiraoka-2025/sub_test.ipynb 8
[NbConvertApp] Writing 17120 bytes to /tmp/claude-1001/pop_sub_out.ipynb

real	1m11.866s
user	2m21.371s
sys	0m2.907s
===== cell 1 
dandiset 000044 version 0.210812.1516

===== cell 3 ['sanity']
             session  units  excitatory  inhibitory unsorted_unit_ids
0  Achilles-10252013    137         120          17                []
1  Achilles-11012013    104          92          12                []
2     Buddy-06272013     68          48          20               [2]
3    Cicero-09012014     73          55          18               [2]
4    Cicero-09102014    105          81          24                []
5    Cicero-09172014     72          59          13                []
6    Gatsby-08022013     80          66          14               [2]
7    Gatsby-08282013     51          41          10                []
excitatory (pyramidal) units: 562 ; of them with unsorted spike times: 2
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import sys,numpy as np; sys.path.insert(0,'entries/hiraoka-2025')
import bursttree as bt
for f in (bt.simulate_incremental, bt.simulate_decremental):
    t=f(10**5,'linear',2.5,np.random.default_rng(3)); tau=np.diff(t); lev=((tau-1)//100).astype(int)
    print(f.__name__, np.bincount(lev))
"
```

```
simulate_incremental [60938 24099  8627  3856  1372   614   263   132    57    29     1     8
     2     0     1]
simulate_decremental [48949 23383 13323  7202  3404  1775   873   483   418    74    53    21
    11    14     4     3     5     0     3     0     0     0     0     0
     0     1]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd entries/hiraoka-2025 && python - <<'EOF'
s=open('bursttree.py').read()
old_inc=s[s.index('def simulate_incremental'):s.index('def simulate_decremental')]
new_inc='''def _q_exact_zeta(gamma: float, kmax: int = 1 << 16) -> np.ndarray:
    """Eq. 9 applied to the zeta distribution of Eq. 15: q(kappa) = zeta(gamma, kappa+1) / zeta(gamma, kappa)
    (Hurwitz zeta), for kappa = 0..kmax (index 0 unused). A variant; Section IV uses Eq. 16."""
    from scipy.special import zeta

    k = np.arange(1, kmax + 2, dtype=float)
    z = zeta(gamma, k)
    return np.r_[np.nan, z[1:] / z[:-1]]


def simulate_incremental(n: int, series: str, gamma: float, rng: np.random.Generator,
                         memory: str = "eq16") -> np.ndarray:
    """Algorithm 2 (incremental), with uniform IETs on [delta_l, delta_(l+1)] (Eq. 10).

    memory="eq16": q(kappa) = (kappa/(kappa+1))^(gamma-1), Eq. 16, as Section IV uses.
    memory="eq9_zeta": q(kappa) from Eq. 9 applied exactly to the zeta distribution (Eq. 15),
    a variant. Returns n event times, t_1 = 0.
    """
    L = 400
    d = timescales(series, L)
    qx = _q_exact_zeta(gamma) if memory == "eq9_zeta" else None
    kappa = np.zeros(L, dtype=np.int64)  # 0 = not set
    t = np.empty(n)
    t[0] = 0.0
    i, l = 1, 0
    e = gamma - 1.0
    buf = rng.random(1 << 20)
    bi = 0
    while i < n:
        if bi >= len(buf) - 2:
            buf = rng.random(1 << 20)
            bi = 0
        if kappa[l] == 0:
            kappa[l] = 1
        r = buf[bi]; bi += 1
        kp = kappa[l]
        if qx is None:
            q = (kp / (kp + 1.0)) ** e
        elif kp < len(qx) - 1:
            q = qx[kp]
        else:
            q = (kp / (kp + 1.0)) ** e  # beyond the table the two agree to within 1e-9
        if r < q:
            u = buf[bi]; bi += 1
            t[i] = t[i - 1] + d[l] + (d[l + 1] - d[l]) * u
            i += 1
            kappa[l] = kp + 1
            l = 0
        else:
            kappa[l] = 1
            l += 1
    return t


'''
s=s.replace(old_inc,new_inc)
old_dec=s[s.index('def simulate_decremental'):s.index('def unit_all_patterns')]
new_dec='''def sample_merging(size: int, gamma: float, rng: np.random.Generator, dist: str = "zeta") -> np.ndarray:
    """Merging numbers k >= 1. dist="zeta": Eq. 15, as Section IV states for P(k).
    dist="eq16": the distribution whose memory function is Eq. 16, P(K >= k) = k^-(gamma-1),
    sampled as floor(U^(-1/(gamma-1))); a variant."""
    from scipy.stats import zipf

    if dist == "zeta":
        return zipf.rvs(gamma, size=size, random_state=rng)
    u = 1.0 - rng.random(size)  # in (0, 1]
    return np.floor(u ** (-1.0 / (gamma - 1.0))).astype(np.int64)


def simulate_decremental(n: int, series: str, gamma: float, rng: np.random.Generator,
                         dist: str = "zeta") -> np.ndarray:
    """Algorithm 1 (decremental), merging numbers from sample_merging, uniform IETs (Eq. 10)."""
    L = 400
    d = timescales(series, L)
    kappa = np.full(L, -1, dtype=np.int64)  # -1 = not set
    t = np.empty(n)
    t[0] = 0.0
    i, l = 1, 0
    ks = sample_merging(1 << 20, gamma, rng, dist)
    ki = 0
    us = rng.random(1 << 20)
    ui = 0
    while i < n:
        if kappa[l] <= 0:
            if ki >= len(ks):
                ks = sample_merging(1 << 20, gamma, rng, dist); ki = 0
            kappa[l] = ks[ki]; ki += 1
        elif kappa[l] == 1:
            kappa[l] = 0
            l += 1
        else:
            if ui >= len(us):
                us = rng.random(1 << 20); ui = 0
            t[i] = t[i - 1] + d[l] + (d[l + 1] - d[l]) * us[ui]; ui += 1
            i += 1
            kappa[l] -= 1
            l = 0
    return t


'''
s=s.replace(old_dec,new_dec)
open('bursttree.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python -c "
import sys,numpy as np; sys.path.insert(0,'entries/hiraoka-2025')
import bursttree as bt
print(bt._q_exact_zeta(2.5)[1:4], [(k/(k+1))**1.5 for k in (1,2,3)])
for name,f,kw in [('inc eq16',bt.simulate_incremental,{}),('inc eq9',bt.simulate_incremental,{'memory':'eq9_zeta'}),('dec zeta',bt.simulate_decremental,{}),('dec eq16',bt.simulate_decremental,{'dist':'eq16'})]:
    t=f(10**5,'linear',2.5,np.random.default_rng(3),**kw); tau=np.diff(t); lev=((tau-1)//100).astype(int)
    print(name, np.bincount(lev)[:8], len(bt.burst_sizes(tau,101)))
"
```

```
Sat Nov 21 21:43:03 UTC 2026
[0.2545587  0.48233297 0.61052874] [0.3535533905932738, 0.5443310539518174, 0.649519052838329]
inc eq16 [60938 24099  8627  3856  1372   614   263   132] 39062
inc eq9 [48587 24114 12915  7684  2833  1603  1067   512] 51413
dec zeta [48949 23383 13323  7202  3404  1775   873   483] 51051
dec eq16 [64167 21334  9114  3202  1293   487   263   111] 35833
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nbsrc/model.py",
 "content": "# %% [md]\n# # Hiraoka & Jo (2025): the dynamic generative algorithms (Section IV, Figure 4)\n#\n# Paper: T. Hiraoka and H.-H. Jo, \"Hierarchical organization of bursty trains in event\n# sequences\", doi:10.1063/5.0296506, read from the arXiv preprint body under `paper/`.\n# These claims are `data: elsewhere` in the claims file: their data are not deposited and are\n# generated here by the paper's Algorithms 1 and 2, for which no code is linked. They do not use\n# DANDI:000044 (version 0.210812.1516, the subject of `reproduce_hiraoka_2025.ipynb`); the helper\n# names it, and the sanity cell below only checks that the pinned version is reachable.\n#\n# Set-up from Section IV, paragraph 9: n = 10^6 events, gamma = 2.5, delta_0 = 1, uniform IETs\n# (Eq. 10), linear (Eq. 12) and quadratic (Eq. 13) timescales with w = 100, exponential (Eq. 14)\n# with w = 2, merging numbers zeta-distributed (Eq. 15) with the memory function of Eq. 16 for the\n# incremental algorithm (Algorithm 2), which Figure 4 uses.\n#\n# Claims tested here: fig4-model-heavy-tails, fig4-model-iet-shapes, model-decremental-equivalent.\n\n# %%\nimport time, resource, zlib\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom scipy.stats import ks_2samp\nimport bursttree as bt\n\nT0 = time.time()\npd.set_option(\"display.width\", 200, \"display.max_columns\", 30, \"display.max_rows\", 300)\nPAPER = \"hiraoka-2025\"\nN, GAMMA = 10**6, 2.5\nSERIES = (\"linear\", \"quadratic\", \"exponential\")\n# Figure 4 legends: merging-number pairs delta = r * delta' per series.\nRATIOS = {\"linear\": (1.8, 2.4, 3.3), \"quadratic\": (3.3, 5.9, 11.0), \"exponential\": (5.3, 12.0, 28.0)}\nOFFSETS = (0, 1000, 2000, 3000, 4000)\ndef seed_of(claim):\n    return zlib.crc32(f\"{PAPER}/{claim}\".encode())\n\n# %% tags=sanity\nprint(\"dandiset\", bt.DANDISET, \"version\", bt.DANDI_VERSION, \"(not used by these claims)\")\nprint(\"assets at the pinned version:\", len(bt.list_assets()))\nfor s in SERIES:\n    print(s, \"delta_l for l = 0..5:\", bt.timescales(s, 5))\nprint(\"memory function Eq. 16, q(1..4):\", np.round([(k / (k + 1)) ** (GAMMA - 1) for k in range(1, 5)], 4))\nprint(\"Eq. 9 applied to the zeta distribution, q(1..4):\", np.round(bt._q_exact_zeta(GAMMA)[1:5], 4))\n# what each choice implies for P(k): mean merging number, from 10^6 samples\nrng = np.random.default_rng(seed_of(\"model-decremental-equivalent\") + 99)\nfor dist in (\"zeta\", \"eq16\"):\n    k = bt.sample_merging(10**6, GAMMA, rng, dist)\n    print(f\"P(k) {dist}: P(k=1) = {(k == 1).mean():.4f}, mean k = {k.mean():.3f}\")\nt1 = time.time(); _ = bt.simulate_incremental(10**5, \"linear\", GAMMA, np.random.default_rng(0)); print(f\"time for 1e5 events: {time.time() - t1:.2f} s\")\n\n# %% [md]\n# ## fig4-model-heavy-tails\n#\n# > Event sequences generated by the incremental dynamic algorithm, with linear, quadratic or\n# > exponential timescale series, show heavy-tailed burst-size and merging-number distributions\n# > over a wide range of timescales, with stable exponents.\n#\n# Criterion: Algorithm 2 with the set-up above; bursts, fit and test as for Figure 2 (O3, O4); the\n# pairs of the Figure 4 legends. Reproduced when, for each series, the power law is supported at\n# more than half of the relevant timescales and pairs, and the beta and gamma estimates each have\n# an interquartile range below 0.5. Under the claim's seed both grids and all four fit readings are\n# run; under the four further seeds, grid (a) with all four readings (a choice for run time).\n\n# %% tags=claim:fig4-model-heavy-tails\ndef judge_series(res):\n    B = pd.DataFrame(res[\"bursts\"]); B = B[B.on_grid]; P = pd.DataFrame(res[\"pairs\"])\n    out = []\n    for r, b in B.groupby(\"reading\"):\n        p = P[P.reading == r]\n        iqr = lambda x: float(np.subtract(*np.percentile(x, [75, 25]))) if len(x) else np.nan\n        out.append(dict(reading=r, n_delta=len(b), b_supported=int(b.supported.sum()), n_pairs=len(p), k_supported=int(p.supported.sum()),\n                        beta_median=round(b.alpha.median(), 3), beta_iqr=round(iqr(b.alpha), 3),\n                        gamma_median=round(p.alpha.median(), 3) if len(p) else np.nan, gamma_iqr=round(iqr(p.alpha), 3),\n                        holds=bool(b.supported.sum() > len(b) / 2 and len(p) > 0 and p.supported.sum() > len(p) / 2\n                                   and iqr(b.alpha) < 0.5 and iqr(p.alpha) < 0.5)))\n    return out\n\nS = seed_of(\"fig4-model-heavy-tails\")\nrows, seqs = [], {}\nt1 = time.time()\nfor off in OFFSETS:\n    for j, s in enumerate(SERIES):\n        rng = np.random.default_rng(S + off + j)  # one generator per series: seed, seed + 1, seed + 2\n        t = bt.simulate_incremental(N, s, GAMMA, rng)\n        if off == 0:\n            seqs[s] = t\n        for g in ((\"a\", \"b\") if off == 0 else (\"a\",)):\n            res = bt.analyse_sequence(t, g, ratios=RATIOS[s])\n            for row in judge_series(res):\n                rows.append(dict(seed=S + off, series=s, grid=g, lo=round(res[\"lo\"], 2), hi=round(res[\"hi\"], 1), **row))\n    print(f\"seed offset {off} done, {(time.time() - t1) / 60:.1f} min\")\nH = pd.DataFrame(rows)\nprint(H[H.seed == S].to_string())\nby = H.groupby([\"seed\", \"grid\", \"series\"]).holds.any().unstack(\"series\")\nby[\"all_series\"] = by.all(axis=1)\nprint(\"\\nholds under at least one reading, per series:\"); print(by.to_string())\none = H.groupby([\"seed\", \"grid\", \"reading\"]).holds.all().unstack(\"reading\")\nprint(\"\\nholds for all three series under the same reading:\"); print(one.to_string())\n\n# %%\nfig, axs = plt.subplots(1, 3, figsize=(11, 3))\nfor ax, s in zip(axs, SERIES):\n    tau = np.diff(seqs[s]); lo, hi = bt.relevant_range(tau)\n    for d in bt.grid(lo, hi, \"a\")[::2]:\n        b = bt.burst_sizes(tau, d); x = np.unique(b)\n        ax.loglog(x / b.mean(), bt.ccdf_at(b, x), lw=0.8, label=f\"{d:.0f}\")\n    ax.set_title(s); ax.set_xlabel(\"b / <b>\"); ax.legend(fontsize=6)\naxs[0].set_ylabel(\"P(B >= b)\")\nprint(\"burst-size CCDFs at every second point of grid (a), claim's seed; all values are plotted\")\n\n# %% [md]\n# ## fig4-model-iet-shapes\n#\n# > The IET distribution of the model depends on the timescale series. With linear timescales it\n# > resembles that of the earthquakes, and with exponential timescales it is a power law\n# > reminiscent of the Wikipedia edits.\n#\n# Criterion: the tau_max labels of Figure 4 (1960, 20 800 and 81 600, each +/- 10%), from\n# simulations set up as in fig4-model-heavy-tails. The comparison of shapes is made by eye in the\n# paper and is reported, not judged; the earthquake and Wikipedia sequences are not available here\n# (see fig2-earthquake-beta and fig2-wikipedia-beta), so only the model's shapes are shown. The\n# largest IET is drawn from the highest level the sequence reaches, so it is shown with that level.\n\n# %% tags=claim:fig4-model-iet-shapes\nS2 = seed_of(\"fig4-model-iet-shapes\")\nEXP = {\"linear\": 1960, \"quadratic\": 20800, \"exponential\": 81600}\nrows = []\niet = {}\nfor off in OFFSETS:\n    for j, s in enumerate(SERIES):\n        t = bt.simulate_incremental(N, s, GAMMA, np.random.default_rng(S2 + off + j))\n        tau = np.diff(t); d = bt.timescales(s, 400)\n        top = int(np.searchsorted(d, tau.max()) - 1)\n        rows.append(dict(seed=S2 + off, series=s, tau_min=round(tau.min(), 3), tau_max=round(tau.max(), 1), top_level=top,\n                         level_range=f\"{d[top]:.0f}-{d[top + 1]:.0f}\", expected=EXP[s], within_10pct=bool(abs(tau.max() - EXP[s]) <= 0.1 * EXP[s])))\n        if off == 0:\n            iet[s] = tau\nT = pd.DataFrame(rows); print(T.to_string())\nprint(\"\\nexpected level of the paper's tau_max:\", {s: int(np.searchsorted(bt.timescales(s, 400), v) - 1) for s, v in EXP.items()})\nprint(\"within 10% under the claim's seed:\", T[T.seed == S2].set_index(\"series\").within_10pct.to_dict())\nprint(\"within 10% over the five seeds:\", T.groupby(\"series\").within_10pct.sum().to_dict())\nfig, ax = plt.subplots(figsize=(4.5, 3))\nfor s in SERIES:\n    h, e = np.histogram(iet[s], np.logspace(0, 6, 61), density=True)\n    ax.loglog(np.sqrt(e[1:] * e[:-1]), np.where(h > 0, h, np.nan), \"o-\", ms=2, label=s)\n    print(s, \"IETs outside 1 to 1e6:\", int(((iet[s] < 1) | (iet[s] > 1e6)).sum()))\nax.set_xlabel(\"tau\"); ax.set_ylabel(\"P(tau)\"); ax.legend(fontsize=7)\n# shape: a straight line in log-log over decades marks a power law; slope by least squares on the binned density\nfor s in SERIES:\n    h, e = np.histogram(iet[s], np.logspace(0, 6, 61), density=True); x = np.sqrt(e[1:] * e[:-1]); ok = h > 0\n    sl = np.polyfit(np.log10(x[ok & (x > 10)]), np.log10(h[ok & (x > 10)]), 1)[0] if (ok & (x > 10)).sum() > 2 else np.nan\n    print(f\"{s}: log-log slope of P(tau) above tau = 10: {sl:.2f}; decades with IETs: {np.log10(iet[s].max() / iet[s].min()):.2f}\")\n\n# %% [md]\n# ## model-decremental-equivalent\n#\n# > The decremental algorithm (Algorithm 1) produces sequences statistically equivalent to those\n# > of the incremental algorithm (Algorithm 2), since the memory function of Eq. 9 encodes the\n# > whole merging-number distribution.\n#\n# Criterion: both algorithms with the parameters of fig4-model-heavy-tails. Reproduced when, at\n# each relevant timescale, two-sample Kolmogorov-Smirnov tests of the burst sizes do not differ at\n# p < 0.05 after Bonferroni correction. The relevant timescales are taken from the incremental\n# sequence, on both grids of O4.\n#\n# Section IV gives the decremental algorithm P(k), the zeta distribution of Eq. 15, and the\n# incremental one the memory function of Eq. 16, which it calls the one that Eq. 9 gives. The\n# sanity cell shows that they differ (q(1) = 0.354 against 0.255), so the two algorithms run\n# \"with the parameters\" can be read three ways: (L) literally, zeta for Algorithm 1 and Eq. 16\n# for Algorithm 2; (Z) both from the zeta distribution, Algorithm 2 with Eq. 9 applied exactly;\n# (Q) both from Eq. 16, Algorithm 1 with the P(k) whose memory function is Eq. 16. All three are\n# run. The first generator of the claim drives Algorithm 2, the second (seed + 1) Algorithm 1.\n\n# %% tags=claim:model-decremental-equivalent\nS3 = seed_of(\"model-decremental-equivalent\")\nVARIANTS = {\"L\": (\"eq16\", \"zeta\"), \"Z\": (\"eq9_zeta\", \"zeta\"), \"Q\": (\"eq16\", \"eq16\")}\nrows = []\nt1 = time.time()\nfor off in OFFSETS:\n    for v, (mem, dist) in VARIANTS.items():\n        for j, s in enumerate(SERIES):\n            ti = bt.simulate_incremental(N, s, GAMMA, np.random.default_rng(S3 + off + 2 * j), memory=mem)\n            td = bt.simulate_decremental(N, s, GAMMA, np.random.default_rng(S3 + off + 2 * j + 1), dist=dist)\n            ta, tb = np.diff(ti), np.diff(td)\n            lo, hi = bt.relevant_range(ta)\n            for g in (\"a\", \"b\"):\n                gr = bt.grid(lo, hi, g)\n                ps = []; ds = []\n                for d in gr:\n                    r = ks_2samp(bt.burst_sizes(ta, d), bt.burst_sizes(tb, d))\n                    ps.append(r.pvalue); ds.append(r.statistic)\n                ps = np.array(ps)\n                rows.append(dict(seed=S3 + off, variant=v, series=s, grid=g, n_tests=len(gr), n_reject=int((ps * len(gr) < 0.05).sum()),\n                                 min_p_bonf=float(min(1, ps.min() * len(gr))), max_D=round(max(ds), 4),\n                                 m_inc=len(bt.burst_sizes(ta, gr[0])), m_dec=len(bt.burst_sizes(tb, gr[0])),\n                                 iet_max_inc=round(ta.max(), 0), iet_max_dec=round(tb.max(), 0)))\n    print(f\"seed offset {off} done, {(time.time() - t1) / 60:.1f} min\")\nK = pd.DataFrame(rows)\nprint(K[K.seed == S3].to_string())\neq = K.groupby([\"seed\", \"variant\", \"grid\"]).n_reject.sum().unstack([\"variant\", \"grid\"])\nprint(\"\\nnumber of timescales where the burst sizes differ (Bonferroni p < 0.05), summed over the three series:\")\nprint(eq.to_string())\nprint(f\"\\nnotebook time {(time.time() - T0) / 60:.1f} min, peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && sed 's/^N, GAMMA = 10\*\*6, 2.5/N, GAMMA = 10**5, 2.5/; s/^OFFSETS = (0, 1000, 2000, 3000, 4000)/OFFSETS = (0, 1000)/' nbsrc/model.py > nbsrc/model_sub.py && python nbsrc/build.py nbsrc/model_sub.py entries/hiraoka-2025/sub_test.ipynb && cd entries/hiraoka-2025 && time jupyter nbconvert --to notebook --execute sub_test.ipynb --output $TMPDIR/model_sub_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | tail -1; rm sub_test.ipynb; cd $TMPDIR && python show.py model_sub_out.ipynb 6000
```

```
entries/hiraoka-2025/sub_test.ipynb 10
[NbConvertApp] Writing 132740 bytes to /tmp/claude-1001/model_sub_out.ipynb

real	1m3.190s
user	1m1.850s
sys	0m0.445s
===== cell 1 
===== cell 2 ['sanity']
dandiset 000044 version 0.210812.1516 (not used by these claims)

assets at the pinned version: 8
linear delta_l for l = 0..5: [  1. 101. 201. 301. 401. 501.]
quadratic delta_l for l = 0..5: [1.000e+00 1.010e+02 4.010e+02 9.010e+02 1.601e+03 2.501e+03]
exponential delta_l for l = 0..5: [ 1.  2.  4.  8. 16. 32.]
memory function Eq. 16, q(1..4): [0.3536 0.5443 0.6495 0.7155]
Eq. 9 applied to the zeta distribution, q(1..4): [0.2546 0.4823 0.6105 0.6892]
P(k) zeta: P(k=1) = 0.7450, mean k = 1.927
P(k) eq16: P(k=1) = 0.6459, mean k = 2.590

time for 1e5 events: 0.34 s
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='nbsrc/model.py'; s=open(p).read()
s=s.replace('''VARIANTS = {"L": ("eq16", "zeta"), "Z": ("eq9_zeta", "zeta"), "Q": ("eq16", "eq16")}''','''VARIANTS = {"L": ("eq16", "zeta"), "Z": ("eq9_zeta", "zeta"), "Q": ("eq16", "eq16"), "N": ("eq16", None)}''')
s=s.replace('''            td = bt.simulate_decremental(N, s, GAMMA, np.random.default_rng(S3 + off + 2 * j + 1), dist=dist)''','''            rng2 = np.random.default_rng(S3 + off + 2 * j + 1)
            td = bt.simulate_incremental(N, s, GAMMA, rng2) if dist is None else bt.simulate_decremental(N, s, GAMMA, rng2, dist=dist)''')
s=s.replace('''# run. The first generator of the claim drives Algorithm 2, the second (seed + 1) Algorithm 1.''','''# run. The first generator of the claim drives Algorithm 2, the second (seed + 1) Algorithm 1.
# As the test's reference, (N) compares two runs of Algorithm 2 (Eq. 16) with the two generators:
# the same algorithm, so any rejection there is the test's own rate on these correlated sequences.''')
open(p,'w').write(s)
EOF
grep -n '"N"' nbsrc/model.py; date -u
```

```
178:VARIANTS = {"L": ("eq16", "zeta"), "Z": ("eq9_zeta", "zeta"), "Q": ("eq16", "eq16"), "N": ("eq16", None)}
Sat Nov 21 21:45:17 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
curl -s -m 20 -o /dev/null -w "%{http_code}\n" "https://service.scedc.caltech.edu/fdsnws/event/1/query?starttime=1993-01-01&endtime=1993-01-02&format=text"; curl -s -m 20 -o /dev/null -w "%{http_code}\n" https://dumps.wikimedia.org/enwiki/20151002/; curl -s -m 20 -o /dev/null -w "%{http_code}\n" "https://archive.org/advancedsearch.php?q=enwiki-20151002&fl%5B%5D=identifier&rows=5&output=json"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s -m 20 "https://archive.org/advancedsearch.php?q=enwiki-20151002&fl%5B%5D=identifier&rows=5&output=json" | head -c 600; echo; curl -s -m 30 "https://service.scedc.caltech.edu/fdsnws/event/1/query?starttime=1993-01-01&endtime=1993-01-02&format=text" | head -3
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s -m 30 "https://archive.org/metadata/enwiki-20151002" | python -c "
import json,sys; d=json.load(sys.stdin); fs=d.get('files',[])
print(len(fs), sum(int(f.get('size',0)) for f in fs)/1e9,'GB total')
for f in fs:
    n=f['name']
    if 'stub-meta-history' in n or 'pages-meta-history' in n and n.endswith('.7z')==False: print(n, int(f.get('size',0))/1e9)
" | head -30
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s -m 30 "https://archive.org/metadata/enwiki-20151002" | python -c "
import json,sys; d=json.load(sys.stdin); fs=d.get('files',[])
st=[f for f in fs if 'stub-meta-history' in f['name']]; print('stub', [(f['name'], int(f.get('size',0))/1e9) for f in st])
h=[f for f in fs if 'pages-meta-history' in f['name'] and f['name'].endswith('.bz2')]; print('history bz2', len(h), sum(int(f.get('size',0)) for f in h)/1e9)
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='nbsrc/main.py'; s=open(p).read()
s=s.replace('''                   range=round(np.ptp(a_), 3), max_sigma=round(d.sigma.max(), 3),''','''                   range=round(np.ptp(a_), 3), max_sigma=round(d.sigma.max(), 3), n_in_band=int((np.abs(a_ - 2.35) <= 0.235).sum()),
                   first_delta_all_in_band_after=round(min([dd for dd in d.delta if np.all(np.abs(d.alpha[d.delta >= dd] - 2.35) <= 0.235)], default=np.nan), 1),''')
open(p,'w').write(s)
EOF
grep -n "n_in_band" nbsrc/main.py | head -2
```

```
250:                   range=round(np.ptp(a_), 3), max_sigma=round(d.sigma.max(), 3), n_in_band=int((np.abs(a_ - 2.35) <= 0.235).sum()),
253:                   median_in_band_range_ok=bool(abs(np.median(a_) - 2.35) <= 0.235 and np.ptp(a_) < 0.47)))
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='nbsrc/main.py'; s=open(p).read()
header='''Paper: Takayuki Hiraoka and Hang-Hyun Jo, "Hierarchical organization of bursty trains in event
# sequences", doi:10.1063/5.0296506. The claims file (`claims/hiraoka-2025.yaml`) was written from
# `paper/10.1063-5.0296506.txt`, whose body is the arXiv preprint (arXiv:2508.18281v1, dated
# September 22, 2025); the paper has no supplement and links no code.
#
# Dataset: DANDI:000044 (Grosmark and Buzsaki 2016), version **0.210812.1516**, DOI
# 10.48324/dandi.000044/0.210812.1516. Why this version: the paper cites it (ref. 39,
# https://dandiarchive.org/dandiset/000044/0.210812.1516), and the claims file gives it. Later
# versions exist (latest 0.261106.0236); they re-export the files, renumber the units and rename
# the cell types, which matters for finding "unit 9" (shown in the version check below). The spike
# trains themselves are the same in the representative session.
#
# Files are streamed from the archive with `remfile` and `h5py`; nothing is downloaded to disk.
# The helper `bursttree.py` holds the loading, the burst and merging-number measures, the fits and
# the paper's two algorithms, and says where each parameter comes from.
#
# Notebooks of this entry: this one (data check and the representative neuron),
# `other_neurons.ipynb` (fig2-other-neurons-similar) and `model.ipynb` (Section IV, Figure 4).
#
# | Claim | Tested where | Status |
# |---|---|---|
# | fig2-neuron-representative-sequence | this notebook | tested |
# | fig2-iet-broad | this notebook | tested |
# | fig2-neuron-burst-size-heavy-tail | this notebook | tested |
# | fig2-neuron-beta-stable | this notebook | tested |
# | fig2-neuron-beta-decrease-follows-gamma | this notebook | tested |
# | fig2-neuron-merging-heavy-tail | this notebook | tested |
# | fig2-neuron-merging-collapse | this notebook | tested |
# | fig2-exponents-above-two | this notebook | tested |
# | fig2-other-neurons-similar | other_neurons.ipynb | tested |
# | fig2-wikipedia-beta | none | blocked (`too_large`): the paper's preprocessed edits are not public; the October 2015 dump survives on the Internet Archive (item enwiki-20151002, stub-meta-history 47.4 GB compressed) |
# | fig2-earthquake-beta | none | blocked (`other`): the SCSN catalog is public but continuously revised and has no pinned version |
# | fig4-model-heavy-tails | model.ipynb | tested (data generated by Algorithm 2) |
# | fig4-model-iet-shapes | model.ipynb | tested (data generated by Algorithm 2) |
# | model-decremental-equivalent | model.ipynb | tested (data generated by Algorithms 1 and 2) |
#
# Open details O1 to O4 are those of the claims file's opening comment. Every result is shown
# under each reading they name; the outcomes say which readings they rest on.'''
s=s.replace('HEADER_PLACEHOLDER', header)
open(p,'w').write(s)
EOF
echo ok
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/version \*\*0.210812.1516\*\*, DOI/version 0.210812.1516, DOI/' nbsrc/main.py && grep -c '\*\*' nbsrc/main.py; cd entries/hiraoka-2025 && cat > requirements.in <<'EOF'
h5py
matplotlib
numpy
pandas
powerlaw
remfile
requests
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: hiraoka-2025
type: reproduction
title: Hierarchical organization of bursty trains in hippocampal spike trains (Hiraoka and Jo 2025)
description: Tests the neuronal findings of Hiraoka and Jo (2025) on dandiset 000044, the hippocampal
  recordings of Grosmark and Buzsaki (2016) that the paper analyses. It finds the paper's
  representative unit, measures bursty trains and merging numbers across timescales, fits their
  power-law tails, and checks whether other pyramidal units show the same pattern. It also runs the
  paper's two generative algorithms. The Wikipedia and earthquake sequences of the paper are not
  tested.
license: Apache-2.0
notebooks:
- path: reproduce_hiraoka_2025.ipynb
  title: Hiraoka and Jo (2025) on dandiset 000044, the representative neuron
  runtime_minutes: 3
- path: other_neurons.ipynb
  title: Hiraoka and Jo (2025) on dandiset 000044, the other pyramidal units
  runtime_minutes: 40
- path: model.ipynb
  title: Hiraoka and Jo (2025), the dynamic generative algorithms of Section IV
  runtime_minutes: 20
helpers:
- bursttree.py
related:
- id: dandi:000044/0.210812.1516
  relation: uses_data
- id: doi:10.1063/5.0296506
  relation: reproduces
EOF
cd $TMPDIR && . dev/bin/activate && for n in main:reproduce_hiraoka_2025 pop:other_neurons model:model; do python nbsrc/build.py nbsrc/${n%%:*}.py entries/hiraoka-2025/${n##*:}.ipynb; done; cd  && python tools/entry.py lock entries/hiraoka-2025 2>&1 | tail -5 && python tools/entry.py check entries/hiraoka-2025 2>&1 | tail -20
```

```
5
entries/hiraoka-2025/reproduce_hiraoka_2025.ipynb 30
entries/hiraoka-2025/other_neurons.ipynb 8
entries/hiraoka-2025/model.ipynb 10
wrote hiraoka-2025/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent**

Entry checks pass. Starting the first full clean-environment run of all three notebooks (estimated about 60 minutes).

**Agent calls Bash**

```bash
date -u; cd  && time python tools/entry.py run entries/hiraoka-2025 2>&1 | tail -15; date -u
```

```
Sat Nov 21 21:47:00 UTC 2026
Installed kernelspec registry-hiraoka-2025 in executed/hiraoka-2025/.venv/share/jupyter/kernels/registry-hiraoka-2025
pass  reproduce_hiraoka_2025.ipynb  (135 s)
pass  other_neurons.ipynb  (1655 s)
pass  model.ipynb  (984 s)

real	46m18.374s
user	124m51.949s
sys	0m10.983s
Sat Nov 21 22:33:18 UTC 2026
```

**Agent calls Bash**

```bash
ls executed/hiraoka-2025/; cd $TMPDIR && . dev/bin/activate && python show.py executed/hiraoka-2025/other_neurons.ipynb 20000
```

```
model.ipynb
other_neurons.ipynb
reproduce_hiraoka_2025.ipynb
result.json
===== cell 1 
dandiset 000044 version 0.210812.1516

===== cell 3 ['sanity']
             session  units  excitatory  inhibitory unsorted_unit_ids
0  Achilles-10252013    137         120          17                []
1  Achilles-11012013    104          92          12                []
2     Buddy-06272013     68          48          20               [2]
3    Cicero-09012014     73          55          18               [2]
4    Cicero-09102014    105          81          24                []
5    Cicero-09172014     72          59          13                []
6    Gatsby-08022013     80          66          14               [2]
7    Gatsby-08282013     51          41          10                []
excitatory (pyramidal) units: 562 ; of them with unsorted spike times: 2
spikes per excitatory unit: min 2130 median 18690 max 134385

[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python show.py executed/hiraoka-2025/model.ipynb 30000
```

```
===== cell 1 
===== cell 2 ['sanity']
dandiset 000044 version 0.210812.1516 (not used by these claims)

assets at the pinned version: 8
linear delta_l for l = 0..5: [  1. 101. 201. 301. 401. 501.]
quadratic delta_l for l = 0..5: [1.000e+00 1.010e+02 4.010e+02 9.010e+02 1.601e+03 2.501e+03]
exponential delta_l for l = 0..5: [ 1.  2.  4.  8. 16. 32.]
memory function Eq. 16, q(1..4): [0.3536 0.5443 0.6495 0.7155]
Eq. 9 applied to the zeta distribution, q(1..4): [0.2546 0.4823 0.6105 0.6892]
P(k) zeta: P(k=1) = 0.7450, mean k = 1.927
P(k) eq16: P(k=1) = 0.6459, mean k = 2.590

time for 1e5 events: 0.34 s

===== cell 4 ['claim:fig4-model-heavy-tails']
seed offset 0 done, 5.2 min

seed offset 1000 done, 6.4 min

[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python show.py executed/hiraoka-2025/reproduce_hiraoka_2025.ipynb 20000 | sed -n '/claim:fig2-neuron-beta-stable/,/plotted beta/p' | head -14
```

```
===== cell 17 ['claim:fig2-neuron-beta-stable']
  grid        reading   n  median    min    max  range  max_sigma  n_in_band  first_delta_all_in_band_after  all_in_band  median_in_band_range_ok
0    a  ks_continuous   7   2.433  2.326  2.878  0.552      0.061          5                          183.0        False                    False
1    a    ks_discrete   7   2.316  2.272  2.907  0.635      0.061          5                          183.0        False                    False
2    a  x1_continuous   7   1.750  1.314  2.615  1.301      0.007          1                            NaN        False                    False
3    a    x1_discrete   7   1.549  1.269  1.948  0.679      0.006          0                            NaN        False                    False
4    b  ks_continuous  34   2.411  2.314  2.999  0.685      0.088         24                          180.4        False                    False
5    b    ks_discrete  34   2.354  2.270  2.975  0.705      0.088         27                          126.5        False                    False
6    b  x1_continuous  34   1.701  1.266  2.615  1.350      0.009          7                            NaN        False                    False
7    b    x1_discrete  34   1.521  1.232  1.948  0.715      0.008          0                            NaN        False                    False

beta per delta below 3000 ms (grid a), with standard errors:
                    alpha                                               sigma                                                xmin                                      
reading     ks_continuous ks_discrete x1_continuous x1_discrete ks_continuous ks_discrete x1_continuous x1_discrete ks_continuous ks_discrete x1_continuous x1_discrete
Shell cwd was reset to
```

**Agent**

The first full run passed: 135 s, 27.6 min and 16.4 min for the three notebooks. Results are in hand. I'm now writing the conclusions and the summary, then the record, before the final run.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='nbsrc/pop.py'; s=open(p).read()
s=s.replace('return pd.Series(dict(units=d.id.nunique(), used=len(used)','return pd.Series(dict(units=len(d), used=len(used)')
open(p,'w').write(s)
p='nbsrc/model.py'; s=open(p).read()
s=s.replace('''level_range=f"{d[top]:.0f}-{d[top + 1]:.0f}", expected=EXP[s], within_10pct''','''level_range=f"{d[top]:.0f}-{d[top + 1]:.0f}", expected=EXP[s], rel_diff=round(tau.max() / EXP[s] - 1, 3), within_10pct''')
open(p,'w').write(s)
EOF
grep -c "rel_diff" nbsrc/model.py; date -u
```

```
1
Sat Nov 21 22:35:22 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > concl.py <<'PYEOF'
import re
def insert_after(path, tag, md):
    s = open(path).read()
    i = s.index(f"# %% tags={tag}\n")
    j = s.find("\n# %%", i + 5)
    block = "\n# %% [md]\n" + "\n".join("# " + l if l else "#" for l in md.strip().split("\n")) + "\n"
    s = s[:j] + "\n" + block + s[j:] if j != -1 else s + "\n" + block
    open(path, "w").write(s)

M = "nbsrc/main.py"
insert_after(M, "claim:fig2-neuron-representative-sequence", """
**Result: reproduced.** Under reading (b) of O1, row 9 of the units table counted from 0 (unit id
18), the unit has 228 356 spikes, tau_min 1.050 ms and tau_max 18 229.7 ms, all within tolerance,
and it is the only unit of the session that matches. Readings (a), (c) and (d) do not match. The
files label this unit `inhibitory` (`interneuron` in the latest version), while the paper
describes its neuronal data as pyramidal cells. In the latest version the same row has id 119 and
no unit has id 9.""")
insert_after(M, "claim:fig2-iet-broad", """
**Result: reproduced.** tau_max / tau_min = 17 362, 4.24 decades, above the three decades of the
criterion and the same as the paper's 1.82 x 10^4 / 1.05 (4.24 decades).""")
insert_after(M, "claim:fig2-neuron-burst-size-heavy-tail", """
**Result: reproduced, under the KS readings of the fit.** With xmin chosen by the KS distance,
the power law is supported at every relevant timescale on both grids (8 of 8 on grid (a), 40 of
40 on grid (b), discrete or continuous), so at every one below 3000 ms. With xmin = 1 it is
supported at more than half of the timescales but not at every one below 3000 ms (grid (b): 29
of 40 discrete, 32 of 40 continuous), which would make it partially reproduced. The shuffled-IET
reference has no supported timescale under any of the five seeds (0 of 5 or 6).""")
insert_after(M, "claim:fig2-neuron-beta-stable", """
**Result: partially reproduced.** Under the discrete KS fit on grid (b), the median beta below
3000 ms is 2.354, the paper's 2.35, and 27 of 34 estimates lie within 2.35 +/- 0.235, all of
them from 126.5 ms to 3000 ms. At the smallest timescales beta is higher (2.975 on grid (b) and
2.907 on grid (a) at 55 ms), so the range is 0.705 and neither reading of the criterion holds,
under any fit (ranges 0.552 to 1.350). The continuous KS fit gives a median of 2.411 (grid (b));
the xmin = 1 fits give medians of 1.521 to 1.750, outside the band.""")
insert_after(M, "claim:fig2-neuron-merging-heavy-tail", """
**Result: reproduced, under the KS readings of the fit.** The power law is supported for 14 or
15 of 15 pairs on grid (a) and 71 or 72 of 76 on grid (b), and the gamma of the supported pairs
has an interquartile range of 0.383 to 0.426 (median gamma 2.633 to 2.752). With xmin = 1 the
discrete fit is supported for 6 of 15 and 19 of 76 pairs, and the continuous fit has an
interquartile range of 0.597 and 0.673.""")
insert_after(M, "claim:fig2-neuron-merging-collapse", """
**Result: reproduced, by reading (b) under the discrete KS fit only, with no margin.** The gamma
of the 15 pairs of Figure 2 lie within 0.490 of their median (2.610), against the 0.5 of reading
(b); under the other fits they spread by 0.521 to 1.172 from their median. Reading (a) fails: the
complementary cumulative distributions of k/<k> differ by up to a factor of 12.54 (at k/<k> =
10.35) where all exceed 10^-3, with a median factor of 1.63. One of the pairs of Figure 2 (delta'
= 590 ms, delta = 6490 ms) lies above the relevant range, with 89 bursts.""")
insert_after(M, "claim:fig2-exponents-above-two", """
**Result: reproduced, under the KS readings of the fit.** Both gamma and beta(delta') exceed 2
in 15 of 15 pairs on grid (a) and 76 of 76 on grid (b), and beta(delta) is within 10% of
min(gamma, beta(delta')) in 11 and 12 of 15 and in 48 and 58 of 76 pairs (median relative error
0.058 to 0.084). Under xmin = 1 both conditions fail (both exponents above 2 in 0 to 17 pairs).""")
insert_after(M, "claim:fig2-neuron-beta-decrease-follows-gamma", """
**Result: reproduced, on grid (b) under the KS readings of the fit; not judged on grid (a).** For
pairs with delta < 3000 ms, beta(delta') < gamma in 38 (continuous) and 40 (discrete) of 57.
Above 3000 ms grid (b) has 6 points; beta falls from 2.064 to 1.867 (discrete fit), Spearman rho
= -0.829 (p = 0.0416), and gamma falls with delta for each ratio (rho -0.714, -0.964 and -0.943).
Grid (a) has one point above 3000 ms, so parts (2) and (3) are not judged there; its part (1)
holds (7 and 8 of 12). Under xmin = 1, part (1) fails (24 of 57) while parts (2) and (3) hold.""")
s = open(M).read()
s = s.replace("""# ## Summary
#
# SUMMARY_PLACEHOLDER""", """# ### Note on the variant
#
# Taken epoch by epoch, the representative unit has 96 875 spikes in the first rest period, 44 099
# in the maze and 87 382 in the second rest period, which sum to the 228 356 of Figure 2: the
# paper used the whole session (O2). The maze epoch alone has a relevant range of only 55.2 to
# 812.3 ms and a median beta below 3000 ms of 1.707 to 1.802; the rest periods give 2.499 to 2.829.

# %% [md]
# ## Summary
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# | Claim | Outcome | Rests on |
# |---|---|---|
# | fig2-neuron-representative-sequence | reproduced | O1 reading (b), row 9 counted from 0 (unit id 18) |
# | fig2-iet-broad | reproduced | |
# | fig2-neuron-burst-size-heavy-tail | reproduced | KS fits (assumption: the discrete KS fit); xmin = 1 gives partial |
# | fig2-neuron-beta-stable | partially reproduced | median 2.354, but beta near 2.9 at 55 ms |
# | fig2-neuron-beta-decrease-follows-gamma | reproduced | grid (b), KS fits |
# | fig2-neuron-merging-heavy-tail | reproduced | KS fits |
# | fig2-neuron-merging-collapse | reproduced | reading (b), discrete KS fit, max deviation 0.490 against 0.5 |
# | fig2-exponents-above-two | reproduced | KS fits |
# | fig2-other-neurons-similar | not reproduced | assumption: the discrete KS fit; reproduced under the continuous fits (`other_neurons.ipynb`) |
# | fig2-wikipedia-beta | blocked (too_large) | |
# | fig2-earthquake-beta | blocked (other) | |
# | fig4-model-heavy-tails | partially reproduced | discrete KS fit; seed sensitive (`model.ipynb`) |
# | fig4-model-iet-shapes | partially reproduced | seed sensitive (`model.ipynb`) |
# | model-decremental-equivalent | not reproduced | literal set-up of Section IV (`model.ipynb`) |
#
# How the analysis differs from the paper's:
#
# - The fit is the `powerlaw` package (version in the lock file), as the paper cites, under the
#   four readings of O3. Where the readings disagree and the claims file gives no rule, the
#   discrete fit with xmin chosen by the KS distance is adopted as an assumption: burst sizes and
#   merging numbers are integers, Clauset et al. (ref. 36) give the discrete estimator for them,
#   and it gives the paper's beta of 2.35 for the representative unit (median 2.354). The paper does
#   not say which it used.
# - The grid of delta is not given in the paper. Grid (b) fits a whole number of log steps (40 of
#   0.0514 for the representative unit) between the ends of the relevant range; every 5th point
#   then gives the delta' labels of Figure 2 and every 8th the delta labels. Grid (a) has ratio 1.82
#   (O4).
# - The relevant range is computed exactly from the IETs (55.25 to 6282.75 ms here); Figure 2 shows
#   6300 ms, which has 99 bursts by this count.
#
# What was found about the dataset:
#
# - The paper's "unit 9" is row 9 of the units table counted from 0 (id 18). It is labelled
#   inhibitory, though the paper describes the data as pyramidal cells. Later versions renumber
#   the units, so "unit 9" cannot be found by id in any version.
# - In three sessions (Buddy-06272013, Cicero-09012014, Gatsby-08022013) the spike train of unit id
#   2 is not sorted: it is two sorted runs, the first of exactly 65 536 or 131 072 spikes starting
#   in mid-session, the second starting at the beginning (`other_neurons.ipynb` and the data check).
# - In Gatsby-08022013, 4.7% of the spikes fall after the end of the last epoch (30 413.6 s).
# - The position series stores its sampling interval (0.0256 s) in the attribute `rate`, which
#   NWB defines as a rate in Hz.
# - The epochs are longer than the paper's description of the maze session (45 minutes): the maze
#   epochs last 0.57 to 1.54 h, and the first rest periods 2.98 to 5.37 h.
# - No spike train is deposited twice. The spikes and the maze position share a clock: the
#   excitatory population rate correlates with running speed at r = 0.618 at zero shift, and at a
#   median |r| of 0.043 beyond 60 s.""")
open(M, "w").write(s)

P = "nbsrc/pop.py"
insert_after(P, "claim:fig2-other-neurons-similar", """
**Result: not reproduced under the discrete KS fit adopted here (an assumption); reproduced under
the continuous fits.** With the discrete KS fit, 129 and 130 of 554 and 562 units show the pattern
in set (b) (0.233 and 0.231), and 14 and 9 of 120 in set (a) (0.117 and 0.075), on grids (a) and
(b). With the continuous KS fit, the powerlaw package's default, set (b) passes narrowly (303 of
554, 0.547; 315 of 562, 0.560) and set (a) does not (0.400 and 0.392); with the continuous fit
from xmin = 1 both sets pass (0.883 to 0.906). The discrete fit from xmin = 1 gives 0.017 to
0.215. Under the discrete KS fit the median over units of the median beta is 2.404 and 2.400 in
set (b) (interquartile range 2.156 to 2.648 on grid (a)) and 2.550 and 2.538 in set (a). Leaving
out the two units with unsorted spike times changes no fraction by more than 0.003.""")
s = open(P).read()
s += """
# %% [md]
# **Result (parts).** Under the discrete KS fit, the burst-size part of the pattern holds in 0.736
# and 0.769 of the units of set (b), and the merging-number part in 0.247 and 0.238: it is the
# merging numbers that fail. In set (a), the merging part holds in 0.117 and 0.075.
"""
open(P, "w").write(s)

D = "nbsrc/model.py"
insert_after(D, "claim:fig4-model-heavy-tails", """
**Result: partially reproduced under the discrete KS fit, and seed sensitive.** Under the claim's
seed the linear and quadratic series hold on both grids. The exponential series has heavy tails
(the power law is supported at 42 of 52 timescales and 79 of 94 pairs on grid (b)), but its gamma
has an interquartile range of 0.522 (grid (a)) and 0.502 (grid (b)), just above 0.5. Under the
four other seeds the discrete KS fit holds for all three series (grid (a)). Each series holds
under some reading of the fit under all five seeds, but under the claim's seed no single reading
holds for all three.""")
insert_after(D, "claim:fig4-model-iet-shapes", """
**Result: partially reproduced, and seed sensitive.** Under the claim's seed tau_max is 1711.4
(linear, rel_diff -0.127 from 1960), 21 390.9 (quadratic, within 10% of 20 800) and 61 320.3
(exponential, rel_diff -0.249 from 81 600). tau_max is an IET of the highest level the sequence
reaches, which varies from seed to seed (levels 14 to 18 linear, 14 to 16 quadratic, 13 to 18
exponential, against 19, 14 and 16 for the paper's values); over the five seeds the values are
within 10% in 2, 2 and 0 of 5. tau_min is 1.000 or 1.001 in all, as in Figure 4. On shape, P(tau)
falls with a log-log slope of -2.27, -1.98 and -2.15 above tau = 10 over 3.23, 4.33 and 4.79
decades; the comparison with the earthquake and Wikipedia sequences cannot be made here.""")
insert_after(D, "claim:model-decremental-equivalent", """
**Result: not reproduced.** Under the literal set-up (L), the burst sizes differ at every relevant
timescale of all three series under every seed (22 to 25 timescales on grid (a), 105 to 114 on
grid (b)), with KS D up to 0.4487; the decremental sequences also have more bursts at the lowest
timescale (566 721 against 414 726 in the linear series). With both algorithms on the same P(k)
the differences are small (D at most 0.1874) but some tests still reject under the claim's seed
(Z: 3 and 11 timescales, Q: 4 and 11), as they do for two runs of the same algorithm (N: 4 and
11). The KS criterion thus rejects even identical algorithms on these correlated sequences, and
only Z under seed + 4000 passes it (0 and 0).""")
PYEOF
python concl.py && . dev/bin/activate && for n in main:reproduce_hiraoka_2025 pop:other_neurons model:model; do python nbsrc/build.py nbsrc/${n%%:*}.py entries/hiraoka-2025/${n##*:}.ipynb; done
```

```
entries/hiraoka-2025/reproduce_hiraoka_2025.ipynb 39
entries/hiraoka-2025/other_neurons.ipynb 10
entries/hiraoka-2025/model.ipynb 13
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='nbsrc/main.py'; s=open(p).read()
s=s.replace('''# duplicates: identical spike trains''','''# spike trains not sorted in time: where they break
for s, U in units.items():
    for i, sp in enumerate(U["spikes"]):
        br = np.flatnonzero(np.diff(sp) < 0)
        if len(br):
            print(f"{s}: unit id {U['id'][i]} ({U['cell_type'][i]}), {len(sp)} spikes, {len(br)} break(s) after index {br.tolist()}; "
                  f"first run {sp[0]:.2f} to {sp[br[0]]:.2f} s ({br[0] + 1} spikes), second run {sp[br[0] + 1]:.2f} to {sp[-1]:.2f} s")
# duplicates: identical spike trains''')
s=s.replace('''At the smallest timescales beta is higher (2.975 on grid (b) and
# 2.907 on grid (a) at 55 ms), so the range''','''At the smallest timescales beta is higher (2.907 at 55 ms, up to
# 2.975 on grid (b)), so the range''')
s=s.replace('''lies above the relevant range, with 89 bursts.''','''lies above the relevant range; the fewest bursts among the 15 pairs is 89.''')
open(p,'w').write(s)
p='nbsrc/model.py'; s=open(p).read()
s=s.replace('''**Result: not reproduced.** Under the literal set-up (L), the burst sizes differ at every relevant
# timescale of all three series under every seed (22 to 25 timescales on grid (a), 105 to 114 on
# grid (b)), with KS D up to 0.4487;''','''**Result: not reproduced.** Under the literal set-up (L) and the claim's seed, the burst sizes
# differ at every relevant timescale of all three series (23 of 23 on grid (a), 113 of 113 on grid
# (b)), and at 22 to 25 and 105 to 114 timescales under the five seeds, with KS D up to 0.4487;''')
open(p,'w').write(s)
EOF
grep -n "2.975 on grid\|fewest bursts\|113 of 113" nbsrc/*.py | head; . dev/bin/activate && for n in main:reproduce_hiraoka_2025 pop:other_neurons model:model; do python nbsrc/build.py nbsrc/${n%%:*}.py entries/hiraoka-2025/${n##*:}.ipynb; done
```

```
nbsrc/main.py:336:# 2.975 on grid (b)), so the range is 0.705 and neither reading of the criterion holds,
nbsrc/main.py:424:# = 590 ms, delta = 6490 ms) lies above the relevant range; the fewest bursts among the 15 pairs is 89.
nbsrc/model.py:232:# differ at every relevant timescale of all three series (23 of 23 on grid (a), 113 of 113 on grid
entries/hiraoka-2025/reproduce_hiraoka_2025.ipynb 39
entries/hiraoka-2025/other_neurons.ipynb 10
entries/hiraoka-2025/model.ipynb 13
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required')); p=s['properties']; print(list(p))
o=p['outcomes']['items']; print('outcome', o.get('required'), list(o['properties']))
f=p['findings']['items']; print('finding', f.get('required'), list(f['properties'])); print(json.dumps(f['properties'].get('kind'))[:400]); print(json.dumps(o['properties'].get('blocked_by'))[:300])
print(json.dumps(p['provenance'])[:1500])
"
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs', 'findings_review']
outcome ['claim', 'outcome'] ['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'seed_sensitive', 'proposed']
finding ['kind', 'statement'] ['kind', 'statement', 'found', 'about', 'severity', 'datasets']
{"enum": ["metadata_error", "data_missing", "identifier_missing", "metadata_insufficient", "selection_undocumented", "methods_unavailable", "format_error", "code_mismatch", "paper_inconsistency", "other"]}
{"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "dataset_missing", "too_large", "not_runnable", "other"]}
{"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties": {"kind": {"enum": ["agent", "person"]}, "accountable": {"description": "The person or organisation responsible for this attempt.", "type": "object", "additionalProperties": false, "required": ["name"], "properties": {"name": {"type": "string"}, "orcid": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$"}, "ror": {"type": "string"}}}, "agent": {"description": "Required when kind is agent.", "type": "object", "additionalProperties": false, "required": ["harness", "model", "protocol"], "properties": {"harness": {"type": "string"}, "model": {"type": "string"}, "protocol": {"description": "Version of the reproduction protocol the agent followed.", "type": "string"}}}, "runner": {"description": "Where the attempt was run: the platform, and the run that wrote this record. Its other runs (verification rounds, revisions) are linked from their transcripts.", "type": "object", "additionalProperties": false, "required": ["pla
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json; s=json.load(open('schemas/attempt.schema.json')); p=s['properties']; o=p['outcomes']['items']['properties']
print(json.dumps(o['measured'])[:600]); print(json.dumps(p['inputs'])[:600]); print(json.dumps(p['findings']['items']['properties']['severity'])); print(json.dumps(p['findings']['items']['properties']['found']))"
```

```
{"description": "The values obtained, for claims with expected values: one number, or one per expected value, in the same order.", "oneOf": [{"type": "number"}, {"type": "array", "minItems": 1, "items": {"type": "number"}}]}
{"description": "Everything the attempt used that is not in the dataset.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["what", "source"], "properties": {"what": {"type": "string", "minLength": 1}, "source": {"description": "A DOI, or a repository URL with the commit read.", "type": "string", "minLength": 1}}}}
{"description": "For a finding about the data: how much it harms someone who uses the dataset (docs/protocol.md, the attempt record). `critical`: the data are wrong and nothing shows it, so an analysis gives a wrong result. `major`: a main analysis is blocked or changed, and the user would notice. `minor`: evident from the values or easy to work around, a wrong unit label included. `none`: no problem, a check that passed. Required from protocol pilot-18.", "enum": ["critical", "major", "minor", "none"]}
{"description": "How the finding was found. Unset: by the attempt itself. `on_prompt`: by the reconcile step of a repeat attempt, which checked a finding of the earlier attempt that this one, made blind, did not report (docs/protocol.md, \"Repeat attempts\").", "enum": ["on_prompt"]}
```

**Agent calls Write**

```json
{
 "file_path": "attempts/hiraoka-2025-01.yaml",
 "content": "schema_version: 3\nid: hiraoka-2025-01\ndatasets:\n- archive: dandi\n  id: \"000044\"\n  version: 0.210812.1516\n  doi: 10.48324/dandi.000044/0.210812.1516\n  relation: reuses\npaper: doi:10.1063/5.0296506\ndate: 2026-11-21\nentry: hiraoka-2025\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-18\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/44950987917\noutcomes:\n- claim: fig2-neuron-representative-sequence\n  outcome: reproduced\n  notebook: reproduce_hiraoka_2025.ipynb\n  output: claim:fig2-neuron-representative-sequence\n  measured: [228356, 1.05, 18229.7]\n  notes: Under reading (b) of O1, row 9 of the units table of Achilles-10252013 counted from 0\n    (unit id 18), the unit has 228 356 spikes, tau_min 1.050 ms and tau_max 18 229.7 ms. It is\n    the only unit of the session within all three tolerances. Readings (a) id 9 (9077 spikes),\n    (c) the ninth unit (36 797 spikes) and (d) shank_id 9 (four units) do not match. The unit is\n    labelled inhibitory in this version and interneuron in the latest; the paper describes its\n    neuronal data as pyramidal cells. Its 228 356 spikes are those of the whole session (96 875,\n    44 099 and 87 382 in the three epochs), which settles O2.\n- claim: fig2-iet-broad\n  outcome: reproduced\n  notebook: reproduce_hiraoka_2025.ipynb\n  output: claim:fig2-iet-broad\n  measured: 17362\n  notes: tau_max over tau_min is 17 362, 4.24 decades, against the three decades of the criterion;\n    the paper's labels give the same 4.24 decades.\n- claim: fig2-neuron-burst-size-heavy-tail\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_hiraoka_2025.ipynb\n  output: claim:fig2-neuron-burst-size-heavy-tail\n  notes: With xmin chosen by the KS distance, discrete or continuous, the power law is supported\n    (R > 0, p < 0.05) at 8 of 8 timescales of grid (a) and 40 of 40 of grid (b), all of those\n    below 3000 ms included. With xmin = 1 it is supported at 5 of 8 and 29 of 40 (discrete) and\n    7 of 8 and 32 of 40 (continuous), more than half but not every one below 3000 ms, which is\n    partially reproduced on grid (b) for both and on grid (a) for the discrete fit. The outcome\n    rests on the adopted discrete KS fit (see deviations); every KS reading gives it. On the IETs\n    shuffled in time, a renewal reference, no timescale is supported under any of the five seeds\n    (0 of 5 or 6, grid (a)).\n  deviations:\n  - The fit reading is open (claims file, O3) and the readings differ in outcome here, with no\n    rule in the claims file for a claim that counts tests. Assumed the discrete maximum-likelihood\n    fit with xmin chosen by the KS distance, because burst sizes and merging numbers are integers,\n    the method the paper cites for its fits (Clauset et al., ref. 36, through the powerlaw package,\n    ref. 37) gives the discrete estimator for integer data, and this reading gives the paper's beta\n    for the representative unit (median 2.354 against 2.35). The paper does not say which it used.\n  - The grid of delta is open (O4). Grid (b) fits a whole number of log10 steps near 0.052 between\n    the ends of the relevant range (40 steps of 0.0514 for this unit), as the Figure 2 legend says\n    the values shown span the entire range of relevant timescales; every 5th point then gives the\n    delta' labels of Figure 2 and every 8th the delta labels.\n- claim: fig2-neuron-beta-stable\n  outcome: partially_reproduced\n  notebook: reproduce_hiraoka_2025.ipynb\n  output: claim:fig2-neuron-beta-stable\n  measured: 2.354\n  notes: Under the discrete KS fit on grid (b) the median beta below 3000 ms is 2.354 and 27 of 34\n    estimates are within 2.35 +/- 0.235, every one from 126.5 ms to 3000 ms (1.4 decades). At the\n    smallest timescales beta is higher (2.907 at 55 ms, up to 2.975 on grid (b)), so the range is\n    0.705 and neither reading of the criterion holds under any fit (ranges 0.552 to 1.350; medians\n    2.316 to 2.433 under the KS fits, 1.521 to 1.750 with xmin = 1). Partially reproduced, because\n    the paper's value holds over most of the range but not at its lower end. The standard errors\n    are at most 0.088.\n  deviations:\n  - Measured is the median under the discrete KS fit on grid (b), the first reading the criterion\n    allows on the fit adopted elsewhere; the other readings are in the notebook.\n- claim: fig2-neuron-beta-decrease-follows-gamma\n  outcome: reproduced\n  notebook: reproduce_hiraoka_2025.ipynb\n  output: claim:fig2-neuron-beta-decrease-follows-gamma\n  notes: On grid (b), under both KS fits, beta at delta' is below gamma for 38 (continuous) and 40\n    (discrete) of 57 pairs with delta < 3000 ms; above 3000 ms the 6 grid points give a Spearman\n    rho of -0.829 (p = 0.042) for beta, which falls from 2.064 to 1.867 (discrete), and gamma falls\n    with delta for each ratio (rho -0.714, -0.964 and -0.943). Grid (a) has one point above 3000 ms,\n    so parts (2) and (3) are not judged on it; its part (1) holds (7 and 8 of 12). Under xmin = 1\n    part (1) fails (24 of 57), so the outcome rests on the KS fits, as O3 allows for a claim on\n    exponents. The paper names no test; the claim's \"seems to be driven\" is not tested beyond\n    these correlations.\n- claim: fig2-neuron-merging-heavy-tail\n  outcome: reproduced\n  notebook: reproduce_hiraoka_2025.ipynb\n  output: claim:fig2-neuron-merging-heavy-tail\n  notes: Under the KS fits the power law is supported for 14 (discrete) and 15 (continuous) of 15\n    pairs on grid (a) and 71 and 72 of 76 on grid (b); the gamma of the supported pairs has an\n    interquartile range of 0.383 to 0.426 and a median of 2.633 to 2.752. With xmin = 1 the\n    discrete fit is supported for 6 of 15 and 19 of 76 pairs, and the continuous fit has an\n    interquartile range of 0.673 and 0.597.\n- claim: fig2-neuron-merging-collapse\n  outcome: reproduced\n  notebook: reproduce_hiraoka_2025.ipynb\n  output: claim:fig2-neuron-merging-collapse\n  notes: Reproduced by reading (b) under the discrete KS fit alone, with no margin. The gamma of the\n    15 pairs of Figure 2 lie within 0.490 of their median of 2.610 (the band is 0.5); under the\n    other fits the largest deviation is 0.521 to 1.172. Reading (a) fails, as the complementary\n    cumulative distributions of k over its mean differ by up to a factor of 12.54 (median 1.63)\n    where all exceed 10^-3. One pair of Figure 2 (delta' 590 ms, delta 6490 ms) lies above the\n    relevant range.\n  deviations:\n  - The pairs are the labels of Figure 2 as printed (55, 100, 180, 330 and 590 ms), as the\n    criterion gives them. The comparison points for reading (a) are 200 values of k over its mean,\n    log-spaced from 0.01 to 1000, a standard choice.\n- claim: fig2-exponents-above-two\n  outcome: reproduced\n  notebook: reproduce_hiraoka_2025.ipynb\n  output: claim:fig2-exponents-above-two\n  notes: Under the KS fits both gamma and beta at delta' exceed 2 in 15 of 15 pairs (grid a) and 76\n    of 76 (grid b), and beta at delta is within 10% of the smaller of the two in 11 and 12 of 15 and\n    48 and 58 of 76 pairs (median relative error 0.058 to 0.084). Under xmin = 1 both conditions\n    fail (both above 2 in 0 to 17 pairs).\n- claim: fig2-other-neurons-similar\n  outcome: not_reproduced\n  assumed: true\n  notebook: other_neurons.ipynb\n  output: claim:fig2-other-neurons-similar\n  notes: Under the adopted discrete KS fit, 129 of 554 (grid a) and 130 of 562 (grid b) pyramidal\n    units of all sessions show the pattern (0.233 and 0.231), and 14 and 9 of 120 in\n    Achilles-10252013 (0.117 and 0.075). The burst-size part holds in 0.736 and 0.769 of the units\n    of all sessions, the merging-number part in 0.247 and 0.238. The readings of the fit disagree;\n    with the continuous KS fit, the powerlaw package's default, all sessions pass narrowly (303 of\n    554, 0.547; 315 of 562, 0.560) and Achilles-10252013 does not (0.400 and 0.392); with the\n    continuous fit from xmin = 1 both sets pass (0.883 to 0.906); the discrete fit from xmin = 1\n    gives 0.017 to 0.215. Under the discrete KS fit the median over units of each unit's median\n    beta is 2.404 and 2.400 for all sessions (interquartile range 2.156 to 2.648, grid a) and\n    ranges by session from 2.155 to 2.550. 32 units have fewer than three points on grid (a) and\n    are not used there. The fraction showing the pattern varies by session from 0.075 to 0.424\n    under the discrete KS fit. The question of the fit is put to the paper's authors (findings).\n  deviations:\n  - The fit is the adopted discrete KS fit (see fig2-neuron-burst-size-heavy-tail); the outcome\n    would be reproduced under the continuous fits, so it rests on that assumption.\n  - Pyramidal units are read as those with cell_type excitatory, the only label for principal\n    cells in this version (562 of 690 units). The paper's own representative unit is labelled\n    inhibitory, so the paper may have used every unit; that set was not run.\n  - Two of the 562 units have unsorted spike times (data finding); the trains are sorted before the\n    IETs are taken, and leaving them out changes no fraction by more than 0.003.\n- claim: fig2-wikipedia-beta\n  outcome: blocked\n  blocked_by: too_large\n  notes: The paper's preprocessed edit histories were provided privately and are not deposited. The\n    English Wikipedia dump of October 2, 2015 is no longer on dumps.wikimedia.org (the directory\n    answers 404) but is kept on the Internet Archive (item enwiki-20151002), where the smallest\n    file holding every revision's editor and time, the stub-meta-history, is 47.4 GB compressed. Streaming\n    and parsing it to rebuild the editors' sequences, with a preprocessing and a definition of\n    frequent editors the paper does not give, does not fit the run's time.\n- claim: fig2-earthquake-beta\n  outcome: blocked\n  blocked_by: other\n  notes: The Southern California Seismic Network catalog is public (the SCEDC event service\n    answered a query for 1993) but it is revised continuously and has no versioned release, and\n    the paper gives no retrieval date or event identifiers, so it cannot be pinned as the protocol\n    requires for outside data (author, step 1.4). Not tested.\n- claim: fig4-model-heavy-tails\n  outcome: partially_reproduced\n  assumed: true\n  seed_sensitive: true\n  notebook: model.ipynb\n  output: claim:fig4-model-heavy-tails\n  notes: Sequences generated here by Algorithm 2 with the set-up of Section IV. Under the claim's\n    seed and the discrete KS fit the linear and quadratic series hold on both grids; the exponential\n    series has heavy tails (supported at 42 of 52 timescales and 79 of 94 pairs on grid b) but its\n    gamma has an interquartile range of 0.522 (grid a) and 0.502 (grid b), above the 0.5 of the\n    criterion. Under the four other seeds the discrete KS fit holds for all three series (grid a).\n    Each series holds under some reading of the fit under every seed, but under the claim's seed no\n    single reading holds for all three.\n  deviations:\n  - One reading of the fit is applied to all three series alike, the adopted discrete KS fit; taking\n    for each series whichever reading holds would give reproduced.\n  - Under the four further seeds only grid (a) was run, for run time.\n  - No code is linked for Algorithm 2; it is implemented from the pseudocode and Section IV\n    (Eqs. 10, 12 to 14 and 16).\n- claim: fig4-model-iet-shapes\n  outcome: partially_reproduced\n  seed_sensitive: true\n  notebook: model.ipynb\n  output: claim:fig4-model-iet-shapes\n  measured: [1711.4, 21390.9, 61320.3]\n  notes: Under the claim's seed tau_max is 1711.4 (linear, 0.127 below 1960), 21 390.9 (quadratic,\n    within 10% of 20 800) and 61 320.3 (exponential, 0.249 below 81 600), so one of three is within\n    tolerance. tau_max is an IET of the highest level the sequence reaches, which varies with the\n    seed (levels 14 to 18 linear, 14 to 16 quadratic and 13 to 18 exponential, against 19, 14 and\n    16 for the paper's values); over the five seeds the values are within 10% in 2, 2 and 0 of 5.\n    tau_min is 1.000 or 1.001 throughout, as in Figure 4. The comparison of shapes with the\n    earthquake and Wikipedia sequences is not judged and cannot be made here; the model's P(tau)\n    falls with log-log slopes of -2.27, -1.98 and -2.15 above tau = 10.\n- claim: model-decremental-equivalent\n  outcome: not_reproduced\n  seed_sensitive: true\n  notebook: model.ipynb\n  output: claim:model-decremental-equivalent\n  notes: Under the literal set-up of Section IV (Algorithm 1 with the zeta distribution of Eq. 15,\n    Algorithm 2 with the memory function of Eq. 16) the burst sizes differ at every relevant\n    timescale of the three series under the claim's seed (23 of 23 on grid a, 113 of 113 on grid\n    b; 22 to 25 and 105 to 114 over the five seeds), with KS D up to 0.4487, and the decremental\n    sequence has more bursts at the lowest timescale (566 721 against 414 726, linear). Eq. 16 is\n    not the memory function Eq. 9 gives for the zeta distribution (q(1) is 0.354 against 0.255;\n    mean merging number 2.59 against 1.93). With both algorithms on one distribution (readings Z\n    and Q) the differences are small (D at most 0.1874), but the criterion still rejects at 3 and\n    11 (Z) and 4 and 11 (Q) timescales under the claim's seed, as it does for two runs of the same\n    algorithm (reference N, 4 and 11), so the KS criterion rejects even identical algorithms on\n    these correlated sequences. Every reading is not reproduced under the claim's seed; reading Z\n    passes under seed + 4000 (0 and 0 rejections), hence seed_sensitive. The literal reading is not\n    reproduced under all five seeds.\n  deviations:\n  - The paper's \"statistically equivalent\" holds by construction when the decremental algorithm\n    draws from the distribution whose memory function the incremental one uses. The three\n    readings of the set-up (L literal, Z both zeta, Q both from Eq. 16) are all run, with two runs\n    of Algorithm 2 as the reference of the test.\n  - The relevant timescales of each comparison are those of the incremental sequence.\nfindings:\n- kind: format_error\n  severity: major\n  datasets: [\"000044\"]\n  statement: In Buddy-06272013, Cicero-09012014 and Gatsby-08022013 the spike train of unit id 2 is\n    not sorted in time. Each is two sorted runs, the first of exactly 65 536 spikes (131 072 in\n    Gatsby-08022013) starting in mid-session and running to its end, the second starting near the\n    session's start. The power-of-two length suggests a fault in the conversion; whether the train\n    holds one unit's spikes could not be told.\n- kind: other\n  about: data\n  severity: minor\n  datasets: [\"000044\"]\n  statement: In Gatsby-08022013, 263 976 spikes (4.7%) fall after the end of the last epoch\n    (30 413.6 s), up to 32 002.4 s, in no epoch.\n- kind: metadata_error\n  severity: minor\n  datasets: [\"000044\"]\n  statement: The position series of the maze stores its sampling interval (0.0256 s) in the\n    attribute rate of starting_time, which NWB defines in Hz. Read as a rate the series would last\n    3 154 777 s; read as an interval it lasts the 2067.5 s of the maze epoch.\n- kind: identifier_missing\n  severity: minor\n  datasets: [\"000044\"]\n  statement: The units table ids of the cited version (id 18 for the paper's \"unit 9\") differ from\n    those of the latest version (id 119 for the same row, with a cluster_id of 19), and neither holds\n    the number the paper uses. The paper's unit can be found only as a row position, and only\n    because its spike count and IETs match the paper's figure.\n- kind: other\n  about: data\n  severity: none\n  datasets: [\"000044\"]\n  statement: No spike train is deposited twice (no two units share their spike count and first and\n    last spike, within or across the eight sessions), and the spikes and the maze position share a\n    clock (the excitatory population rate correlates with running speed at r = 0.618 at zero shift\n    and at a median absolute r of 0.043 beyond 60 s). The epochs differ from the paper's\n    description of 45 minutes of maze and four hours of rest each, with maze epochs of 0.57 to\n    1.54 h and first rest periods of 2.98 to 5.37 h.\n- kind: other\n  about: paper\n  statement: The paper describes its neuronal data as recordings of pyramidal cells, but its\n    representative unit (row 9 of Achilles-10252013) is labelled inhibitory in the cited version\n    and interneuron in the latest, and fires 6.6 spikes per second over the session. Which units\n    the paper analysed, and whether it used the cell types, is not said.\n- kind: paper_inconsistency\n  statement: Section IV gives the zeta distribution (Eq. 15) as P(k) and calls Eq. 16 the memory\n    function that Eq. 9 gives for it, but Eq. 9 applied to the zeta distribution gives q(1) = 0.255,\n    not the 0.354 of Eq. 16. The incremental algorithm with Eq. 16 therefore draws merging numbers\n    with P(K >= k) = k^-(gamma-1) (mean 2.59), and the decremental one with Eq. 15 draws zeta\n    numbers (mean 1.93), so the two are not statistically equivalent as set up.\n- kind: methods_unavailable\n  statement: Question for the authors. Which power-law fit was used for burst sizes and merging\n    numbers, discrete or continuous, and with xmin chosen by the KS distance or fixed? The paper\n    cites Clauset et al. and the powerlaw package without its options or version. On this\n    dataset the discrete fit with xmin by the KS distance gives the paper's beta of 2.35 for unit 9,\n    and the choice decides whether other neurons show the pattern (23% of pyramidal units under\n    it, 56% under the package's continuous default). This attempt assumed the former.\n- kind: methods_unavailable\n  statement: Question for the authors. Which grid of timescales was used, and which units were\n    meant by \"other sequences in the datasets\"? The Figure 2 labels fit 41 log-spaced points over\n    the relevant range, which this attempt used; whether all units or the pyramidal ones were\n    analysed is not said. Which merging-number distribution did the decremental algorithm draw\n    from, given that Eq. 16 is not the memory function of the zeta distribution?\n"
}
```

```
File created successfully at: attempts/hiraoka-2025-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && python - <<'EOF'
p='nbsrc/main.py'; s=open(p).read()
s=s.replace('''    print(f"{s}: fraction of spikes inside an epoch {inside.mean():.6f}")''','''    print(f"{s}: fraction of spikes inside an epoch {inside.mean():.6f}; spikes after the last epoch ends ({E['stop'].max():.1f} s): {(allsp > E['stop'].max()).sum()}, up to {allsp.max():.1f} s")''')
open(p,'w').write(s)
EOF
. dev/bin/activate && python nbsrc/build.py nbsrc/main.py entries/hiraoka-2025/reproduce_hiraoka_2025.ipynb
cd  && python - <<'EOF'
p='attempts/hiraoka-2025-01.yaml'; s=open(p).read()
s=s.replace(''' and interneuron in the latest, and fires 6.6 spikes per second over the session. Which units''',''' and interneuron in the latest. Which units''')
s=s.replace('''starting in mid-session and running to its end, the second''','''starting in mid-session and running to the end of the recording, the second''')
open(p,'w').write(s)
EOF
grep -n ": " attempts/hiraoka-2025-01.yaml | grep -v "^[0-9]*: *[-a-z_]*: \|^[0-9]*:  *- [a-z_]*: " | head
```

```
Sat Nov 21 22:38:01 UTC 2026
entries/hiraoka-2025/reproduce_hiraoka_2025.ipynb 39
4:- archive: dandi
24:- claim: fig2-neuron-representative-sequence
36:- claim: fig2-iet-broad
43:- claim: fig2-neuron-burst-size-heavy-tail
67:- claim: fig2-neuron-beta-stable
82:- claim: fig2-neuron-beta-decrease-follows-gamma
94:- claim: fig2-neuron-merging-heavy-tail
103:- claim: fig2-neuron-merging-collapse
117:- claim: fig2-exponents-above-two
125:- claim: fig2-other-neurons-similar
```

**Agent calls Bash**

```bash
python -c "
import yaml
d=yaml.safe_load(open('attempts/hiraoka-2025-01.yaml'))
def walk(x,p=''):
    if isinstance(x,dict): [walk(v,p+'/'+str(k)) for k,v in x.items()]
    elif isinstance(x,list): [walk(v,p+'[]') for v in x]
    elif isinstance(x,str) and (': ' in x or '—' in x or 'rather' in x or '**' in x): print(p, x[:80])
walk(d); print(len(d['outcomes']))
"; grep -n "rather\|—\|\*\*" entries/hiraoka-2025/bursttree.py $TMPDIR/nbsrc/*.py | grep -v "Result:" | grep -v "\*\* \|\*\*r\|\*\*s\|\*\*kw\|\*\*row\|\*\*stats\|\*\* (\|\*\*(" | head
```

```
14
/tmp/claude-1001/nbsrc/main.py:226:print(f"IETs outside the plotted 1 to {10**4.5:.0f} ms: {(tau < 1).sum() + (tau > 10**4.5).sum()}")
/tmp/claude-1001/nbsrc/model.py:29:N, GAMMA = 10**6, 2.5
/tmp/claude-1001/nbsrc/model.py:47:    k = bt.sample_merging(10**6, GAMMA, rng, dist)
/tmp/claude-1001/nbsrc/model.py:49:t1 = time.time(); _ = bt.simulate_incremental(10**5, "linear", GAMMA, np.random.default_rng(0)); print(f"time for 1e5 events: {time.time() - t1:.2f} s")
/tmp/claude-1001/nbsrc/model_sub.py:29:N, GAMMA = 10**5, 2.5
/tmp/claude-1001/nbsrc/model_sub.py:47:    k = bt.sample_merging(10**6, GAMMA, rng, dist)
/tmp/claude-1001/nbsrc/model_sub.py:49:t1 = time.time(); _ = bt.simulate_incremental(10**5, "linear", GAMMA, np.random.default_rng(0)); print(f"time for 1e5 events: {time.time() - t1:.2f} s")
```

**Agent calls Write**

```json
{
 "file_path": "entries/hiraoka-2025/README.md",
 "content": "# Hiraoka and Jo (2025) on DANDI:000044\n\nTests the findings of T. Hiraoka and H.-H. Jo, \"Hierarchical organization of bursty trains in\nevent sequences\" (doi:10.1063/5.0296506), on dandiset 000044 version 0.210812.1516, the version the\npaper cites: the hippocampal recordings of Grosmark and Buzsaki (2016). The claims are in\n`claims/hiraoka-2025.yaml` and the record in `attempts/hiraoka-2025-01.yaml`.\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\n- `reproduce_hiraoka_2025.ipynb`: the data check, the paper's representative unit (row 9 of\n  session Achilles-10252013), and its bursty trains, merging numbers and power-law fits (Figure 2).\n- `other_neurons.ipynb`: the same pattern in every pyramidal unit of the eight sessions (about\n  30 minutes on 4 processes).\n- `model.ipynb`: the paper's two generative algorithms (Section IV, Figure 4), simulated here.\n- `bursttree.py`: loading, bursts, merging numbers, fits and the algorithms, with the source of\n  each parameter.\n\nThe Wikipedia and earthquake sequences of the paper are not tested.\n\nRun with `python tools/entry.py all entries/hiraoka-2025`.\n"
}
```

```
File created successfully at: entries/hiraoka-2025/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; cd  && time python tools/entry.py all entries/hiraoka-2025 2>&1 | tail -15; date -u
```

```
Sat Nov 21 22:38:19 UTC 2026
error: attempts/hiraoka-2025-01.yaml: claim 'fig4-model-heavy-tails' was tested on data in another archive; list them under `inputs`
error: attempts/hiraoka-2025-01.yaml: claim 'fig4-model-iet-shapes' was tested on data in another archive; list them under `inputs`
error: attempts/hiraoka-2025-01.yaml: claim 'model-decremental-equivalent' was tested on data in another archive; list them under `inputs`
3 error(s)

real	0m5.114s
user	0m4.953s
sys	0m0.163s
Sat Nov 21 22:38:25 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/hiraoka-2025-01.yaml'; s=open(p).read()
s=s.replace('''outcomes:
- claim: fig2-neuron-representative-sequence''','''inputs:
- what: Synthetic event sequences for the claims on the model (fig4-model-heavy-tails,
    fig4-model-iet-shapes, model-decremental-equivalent), not deposited by the paper. They are
    generated in model.ipynb by Algorithms 1 and 2 of the paper's Section IV, implemented in
    bursttree.py from the pseudocode and Eqs. 9 to 16, with seeds from the claims.
  source: doi:10.1063/5.0296506
outcomes:
- claim: fig2-neuron-representative-sequence''')
open(p,'w').write(s)
EOF
python tools/entry.py check entries/hiraoka-2025 2>&1 | tail -5
```

```
0 error(s)
```

**Agent calls Bash**

```bash
date -u; cd  && time python tools/entry.py all entries/hiraoka-2025 2>&1 | tail -8; date -u
```

```
Sat Nov 21 22:38:41 UTC 2026
Installed kernelspec registry-hiraoka-2025 in executed/hiraoka-2025/.venv/share/jupyter/kernels/registry-hiraoka-2025
0 error(s)
pass  reproduce_hiraoka_2025.ipynb  (135 s)
pass  other_neurons.ipynb  (1664 s)
pass  model.ipynb  (980 s)

real	46m28.789s
user	125m24.612s
sys	0m11.502s
Sat Nov 21 23:25:10 UTC 2026
```

**Agent**

The final run passed (all three notebooks). Now confirming that the executed outputs match the conclusions.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && E=executed/hiraoka-2025; python show.py $E/reproduce_hiraoka_2025.ipynb 20000 > m.txt; python show.py $E/other_neurons.ipynb 20000 > p.txt; python show.py $E/model.ipynb 30000 > d.txt; sed -n '1,40p' m.txt | grep -v "^ *-\?[0-9]* *-\?0\.[0-9]*$"; grep -n "ERROR" m.txt p.txt d.txt; diff <(python show.py main_out.ipynb 20000 | sed -n '/claim:fig2-neuron-representative/,$p' | grep -v "fits done\|notebook time") <(sed -n '/claim:fig2-neuron-representative/,$p' m.txt | grep -v "fits done\|notebook time") | head -20
```

```
===== cell 1 
dandiset 000044 version 0.210812.1516

===== cell 3 ['sanity']
             session       subject  size_GB  units  excitatory  inhibitory                         columns    spikes  t_first_s  t_last_s  all_sorted   min_iet_ms                                          epochs  session_end_s
0  Achilles-10252013  sub-Achilles     8.74    137         120          17  id,cell_type,location,shank_id   8414607       0.04  34861.10        True         0.85  PREEpoch:5.02h MazeEpoch:0.57h POSTEpoch:4.09h        34861.1
1  Achilles-11012013  sub-Achilles     9.19    104          92          12  id,cell_type,location,shank_id   7665373       0.00  36629.21        True         0.85  PREEpoch:5.37h MazeEpoch:0.74h POSTEpoch:4.06h        36629.2
2     Buddy-06272013     sub-Buddy     5.24     68          48          20  id,cell_type,location,shank_id   6412255       0.08  21054.70       False -21054371.65  PREEpoch:2.98h MazeEpoch:0.65h POSTEpoch:2.22h        21054.7
3    Cicero-09012014    sub-Cicero     8.68     73          55          18  id,cell_type,location,shank_id   9158616       0.07  34756.80       False -34666502.85  PREEpoch:4.31h MazeEpoch:1.54h POSTEpoch:3.80h        34756.8
4    Cicero-09102014    sub-Cicero     9.12    105          81          24  id,cell_type,location,shank_id  13280381       0.00  36498.60        True         0.85  PREEpoch:4.79h MazeEpoch:0.84h POSTEpoch:4.51h        36498.6
5    Cicero-09172014    sub-Cicero     8.36     72          59          13  id,cell_type,location,shank_id   7708448       0.00  33560.19        True         0.85  PREEpoch:4.44h MazeEpoch:0.85h POSTEpoch:4.02h        33560.2
6    Gatsby-08022013    sub-Gatsby     7.94     80          66          14  id,cell_type,location,shank_id   5653138       0.01  32002.37       False -32000478.40  PREEpoch:4.74h MazeEpoch:0.65h POSTEpoch:3.06h        30413.6
7    Gatsby-08282013    sub-Gatsby     8.44     51          41          10  id,cell_type,location,shank_id   577567
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && diff <(python3 -c "
import re,sys
for l in open('main_out_dump.txt' if False else '/dev/null'): pass") /dev/null; . dev/bin/activate; python show.py main_out.ipynb 20000 | grep -v "===== cell\|fits done\|notebook time" > a.txt; grep -v "===== cell\|fits done\|notebook time" m.txt > b.txt; diff a.txt b.txt | grep "^[<>]" | grep -v "n_in_band\|first_delta\|^> *[0-9] *[ab] *[kx]\|break\|after the last\|first run" | head; echo ---; diff <(grep -v "===== cell\|min,\|notebook time\|done" pop_sub_out.ipynb >/dev/null; python show.py $TMPDIR/pop_sub_out.ipynb 1 >/dev/null; echo) /dev/null >/dev/null; sed -n '/claim:fig2-other/,/units dropped/p' p.txt | sed -n '1,25p'; tail -25 d.txt
```

```
< Achilles-10252013: fraction of spikes inside an epoch 1.000000
< Achilles-11012013: fraction of spikes inside an epoch 1.000000
< Buddy-06272013: fraction of spikes inside an epoch 1.000000
< Cicero-09012014: fraction of spikes inside an epoch 1.000000
< Cicero-09102014: fraction of spikes inside an epoch 1.000000
< Cicero-09172014: fraction of spikes inside an epoch 1.000000
< 
< Gatsby-08022013: fraction of spikes inside an epoch 0.953305
< Gatsby-08282013: fraction of spikes inside an epoch 1.000000
> 
---
===== cell 5 ['claim:fig2-other-neurons-similar']
562 units fitted in 27.3 min
set (a), Achilles-10252013:
                    units   used  pattern  frac_pattern  median_b_frac  median_k_frac  beta_q25  beta_median  beta_q75
grid reading                                                                                                          
a    ks_continuous  120.0  120.0     48.0         0.400          0.800          0.500     2.428        2.652     2.816
     ks_discrete    120.0  120.0     14.0         0.117          0.750          0.000     2.330        2.550     2.757
     x1_continuous  120.0  120.0    107.0         0.892          1.000          0.867     1.667        1.774     1.914
     x1_discrete    120.0  120.0      2.0         0.017          0.500          0.000     1.501        1.562     1.636
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n '/claim:fig4-model-iet-shapes/,/decades with/p' d.txt | head -12; sed -n '/claim:fig4-model-heavy/,/holds under at least/p' d.txt | grep -E "exponential|linear .*ks_discrete|quadratic .*ks_discrete" | head -8
```

```
===== cell 8 ['claim:fig4-model-iet-shapes']
         seed       series  tau_min   tau_max  top_level    level_range  expected  rel_diff  within_10pct
0   739628792       linear    1.000    1711.4         17      1701-1801      1960    -0.127         False
1   739628792    quadratic    1.000   21390.9         14    19601-22501     20800     0.028          True
2   739628792  exponential    1.000   61320.3         15    32768-65536     81600    -0.249         False
3   739629792       linear    1.000    1822.1         18      1801-1901      1960    -0.070          True
4   739629792    quadratic    1.000   22337.3         14    19601-22501     20800     0.074          True
5   739629792  exponential    1.000  102433.4         16   65536-131072     81600     0.255         False
6   739630792       linear    1.000    1471.1         14      1401-1501      1960    -0.249         False
7   739630792    quadratic    1.001   27244.0         16    25601-28901     20800     0.310         False
8   739630792  exponential    1.000   15505.5         13     8192-16384     81600    -0.810         False
9   739631792       linear    1.000    1589.4         15      1501-1601      1960    -0.189         False
1   4174482686       linear    a  92.19    853.1    ks_discrete        4            4        8            8        2.203     0.183         2.320      0.249   True
5   4174482686       linear    b  92.19    853.1    ks_discrete       19           19       35           34        2.464     0.318         2.391      0.490   True
9   4174482686    quadratic    a  92.35  10745.3    ks_discrete        8            7       15           12        2.443     0.115         2.504      0.172   True
13  4174482686    quadratic    b  92.35  10745.3    ks_discrete       40           34       76           58        2.469     0.118         2.446      0.216   True
16  4174482686  exponential    a   1.90    920.2  ks_continuous       11            8       20           19        2.472     0.370       
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
python tools/entry.py handover entries/hiraoka-2025 2>&1 | tail -5; ls executed/hiraoka-2025/handover/; git status --short | head -20; date -u
```

```
wrote executed/hiraoka-2025/handover
bursttree.py
hiraoka-2025.yaml
model.ipynb
other_neurons.ipynb
reproduce_hiraoka_2025.ipynb
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
?? attempts/hiraoka-2025-01.yaml
?? entries/hiraoka-2025/
?? scripts
Sat Nov 21 23:25:59 UTC 2026
```

**Agent calls Bash**

```bash
grep -c "Result:" executed/hiraoka-2025/handover/*.ipynb; grep -c "Summary" executed/hiraoka-2025/handover/reproduce_hiraoka_2025.ipynb; ls -la .bashrc scripts | head -3; python tools/entry.py check entries/hiraoka-2025 | tail -1
```

```
executed/hiraoka-2025/handover/model.ipynb:0
executed/hiraoka-2025/handover/other_neurons.ipynb:0
executed/hiraoka-2025/handover/reproduce_hiraoka_2025.ipynb:0
0
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 21 21:19 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 21 21:19 scripts
0 error(s)
```

**Agent**

## Report: hiraoka-2025 author run (Hiraoka and Jo 2025 on DANDI:000044)

Steps 1 to 5 are done and the handover package is built. `python tools/entry.py all entries/hiraoka-2025` reports 0 errors and all three notebooks pass from a clean environment. I did not commit anything.

### 1. Outcome per claim

| Claim | Outcome | Notes |
|---|---|---|
| fig2-neuron-representative-sequence | reproduced | "Unit 9" is row 9 counted from 0 (id 18): 228 356 spikes, τmin 1.050 ms, τmax 18 229.7 ms. It is the only matching unit. |
| fig2-iet-broad | reproduced | The IETs span 4.24 decades. |
| fig2-neuron-burst-size-heavy-tail | reproduced (assumed) | Power law supported at 40 of 40 timescales with the KS-xmin fits. With xmin = 1 it would only be partially reproduced. |
| fig2-neuron-beta-stable | partially reproduced | Median β is 2.354 and 27 of 34 estimates are in the band. β reaches about 2.9 at 55 ms, so the range rule fails. |
| fig2-neuron-beta-decrease-follows-gamma | reproduced | Holds on grid (b): ρ = −0.829. Grid (a) has one point above 3000 ms, so it could not be judged there. |
| fig2-neuron-merging-heavy-tail | reproduced | 71 to 72 of 76 pairs supported; γ interquartile range 0.38 to 0.43. |
| fig2-neuron-merging-collapse | reproduced | Holds by reading (b) under the discrete KS fit only, with no margin (0.490 against 0.5). Reading (a) fails. |
| fig2-exponents-above-two | reproduced | Holds under the KS fits. |
| fig2-other-neurons-similar | not reproduced (assumed) | Under the discrete KS fit, 23% of the 562 pyramidal units show the pattern. Under the package's continuous default it is 56%, which would pass. |
| fig2-wikipedia-beta | blocked, `too_large` | The paper's preprocessed data are private. The 2015 dump survives only as a 47.4 GB stub history on the Internet Archive. |
| fig2-earthquake-beta | blocked, `other` | The SCSN catalog is public but continuously revised, so it cannot be pinned. |
| fig4-model-heavy-tails | partially reproduced (assumed, seed-sensitive) | Under the claim's seed the exponential series misses on γ interquartile range (0.50 to 0.52). The other four seeds pass. |
| fig4-model-iet-shapes | partially reproduced (seed-sensitive) | One of three τmax values is within tolerance. τmax is set by the highest level reached, which varies with the seed. |
| model-decremental-equivalent | not reproduced (seed-sensitive) | See the paper inconsistency below. |

### 2. Dataset, assumptions, questions

- **Version:** pinned 0.210812.1516, the version the paper cites. Later versions renumber the units and rename cell types; the spike trains are the same.
- **Unsorted spike trains:** in Buddy-06272013, Cicero-09012014 and Gatsby-08022013, unit id 2 is not sorted in time. It is two sorted runs, and the first is exactly 65 536 (or 131 072) spikes long. Rated major.
- **Spikes outside the epochs:** in Gatsby-08022013, 4.7% of spikes fall after the last epoch ends. Rated minor.
- **Position metadata:** the position series stores its sampling interval (0.0256 s) in its `rate` attribute. Rated minor.
- **Unit ids:** the paper's "unit 9" cannot be found by id in any version. Rated minor.
- **Representative unit:** it is labelled inhibitory, although the paper describes its data as pyramidal cells.
- **Checks that passed:** no recording or spike train is deposited twice, and the spikes share a clock with the maze position (r = 0.618 at zero shift).
- **Paper inconsistency:** Eq. 16 is not the memory function that Eq. 9 gives for the zeta distribution (q(1) is 0.354 against 0.255). As set up in Section IV, the two algorithms therefore draw different merging-number distributions and differ at every timescale. A self-consistent pairing differs only slightly. Even so, the claim's KS criterion rejects equivalence for two runs of the same algorithm, so it cannot confirm equivalence on these correlated sequences.
- **Assumption:** where the four fit readings disagree and the claims file gives no rule, I used the discrete fit with xmin chosen by the KS distance. This follows Clauset et al. for integer data and gives the paper's β of 2.35. Grid (b) uses 40 equal log steps between the ends of the relevant range, which reproduces both sets of Figure 2 labels.
- **Questions for the paper's authors**, recorded as `methods_unavailable` findings: which fit was used; which grid and which units were analysed; and which distribution the decremental algorithm drew from.
- **Questions to a reader:** none.

### 3. Where the protocol was unclear or missing something

1. The claims file's "holds under any reading" rule covers only claims on exponents. For claims that count tests, I followed step 1.6 and adopted a reading as an assumption.
2. The check requires `inputs` for `data: elsewhere` claims even when the data are simulated from the paper's own algorithms. I listed the paper's DOI as the source.
3. Nothing says what `blocked_by` to use for outside data that is public but has no versioned release. I used `other`.
4. Protocol and claims file seem to conflict for the Wikipedia data. The claims file marks the claim `data: elsewhere`, for which the protocol forbids `data_missing`, yet the paper's own data are public nowhere. I used `too_large`, based on the size of the raw dump, without timing a fetch.
5. It is unclear how `seed_sensitive` applies when different readings change outcome under different seeds. I set it to true and gave the details in the notes.
6. The protocol has no provision for a criterion whose reference shows it rejects even identical algorithms. I applied the criterion as written and reported the reference in the notes.
7. Any edit, even to a markdown conclusion, forces a full re-run of the entry (46 min). Writing conclusions after seeing the outputs therefore costs two full runs. I left the `runtime_minutes` values in `entry.yaml` (3, 40, 20) as upper estimates so as not to trigger a third run.

### 4. Runtime and failures

- **Run:** about 2 h 06 min (21:20 to 23:26 UTC), including two full clean runs of the entry.
- **Notebook times:** 2.3 min for `reproduce_hiraoka_2025.ipynb`, 27.7 min for `other_neurons.ipynb` (4 processes) and 16.3 min for `model.ipynb`. Peak memory was under 1 GB.
- **Failures:**
  - One permission-denied shell command early on; I used a different tool for the same read.
  - The first `entry.py all` failed its check because the simulated claims had no `inputs`; I added them.
  - Nothing else failed.
- **Untracked files:** `git status` shows `.bashrc`, `scripts` and similar untracked entries in the checkout root. The two I inspected (`.bashrc`, `scripts`) are null-device placeholders dated 21:19, from before this run; they were not created by this work.

## End of run

73 turns, 121 minutes, $6.80 at API prices, result: success.
