# 000055 · author · run 39980867141

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls paper claims/000055 entries attempts | head -50
```

```
<persisted-output>
Output too large (31KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b6a26f25-f6f7-46a9-acce-8bb0fcb10642/tool-results/b4e1ds09s.txt

Preview (first 2KB):
Fri Oct 23 15:48:32 UTC 2026
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
[... 22 more lines not kept]
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
3	Version: `pilot-10`. Record this version in the attempt's provenance.
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
18	  claim, and it asks a reader for any method detail the file lacks.
19	- The **verifier** checks the author's work and must not be the author.
20	
[... 506 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper claims/000055 entries/001453-fouke-2025 claims/001453 attempts | head -60; ls entries | head
```

```
attempts:
000003-senzai-2017-01.yaml
000004-chandravadia-2020-01.yaml
000005-yu-2016-01.yaml
000005-yu-2016-02.yaml
000006-economo-2018-01.yaml
000006-economo-2018-02.yaml
000008-scala-2021-01.yaml
000009-guo-2017-01.yaml
000010-li-2015-01.yaml
000011-li-2016-01.yaml
000013-hires-2015-01.yaml
000015-chen-2017-01.yaml
000019-bouchard-2013-01.yaml
000023-berg-2020-01.yaml
000034-buccino-2020-01.yaml
000035-scala-2021-01.yaml
000036-mayner-2022-01.yaml
000037-gillon-2023-01.yaml
000041-watson-2016-01.yaml
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper claims/000055 entries/001453-fouke-2025 claims/001453 questions | head -80; cat README.md | head -150
```

```
claims/000055:
10.1523-eneuro.0007-21.2021.yaml

claims/001453:
10.1016-j.cub.2025.04.027.yaml

entries/001453-fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt

paper:
10.1016-j.jneumeth.2021.109199.pdf
10.1016-j.jneumeth.2021.109199.txt
10.1038-s41597-022-01280-y.txt
10.1523-eneuro.0007-21.2021.txt

[... 160 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000055/*.yaml
```

```
<persisted-output>
Output too large (44.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b6a26f25-f6f7-46a9-acce-8bb0fcb10642/tool-results/bl7wx2ujz.txt

Preview (first 2KB):
# Claims for Peterson, Singh, Wang, Rao & Brunton (2021), eNeuro 8(3), ENEURO.0007-21.2021,
# "Behavioral and Neural Variability of Naturalistic Arm Movements", on dandiset 000055.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read. The version of record as served by Europe PMC (PMC8225404), from
# paper/10.1523-eneuro.0007-21.2021.txt: main text, Materials and Methods, figure legends,
# Tables 1 and 2, the legends of the Extended Data figures, and the review history. No PDF was
# supplied. The Extended Data figures (1-1, 2-1 to 2-4, 3-1, 4-1 to 4-7, 5-1, 6-1, 6-2) are
# EPS downloads and are not in the text; only their legends are. Claims that rest on them are
# taken from their legends and from the Results sentences that cite them. The per-subject
# electrode table (Extended Data Figure 1-1) and the per-subject feature confidence intervals
# (Extended Data Figures 2-3 and 2-4) could not be read.
#
# Code read. github.com/BruntonUWBio/naturalistic_arm_movements_ecog at commit
# 04c6faf2f219586fa834d10c614ef48a694cec55 (17 March 2021), Python 3.6 (MNE 0.19) and MATLAB.
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/000055/10.1523-eneuro.0007-21.2021.yaml"
}
```

```
1	# Claims for Peterson, Singh, Wang, Rao & Brunton (2021), eNeuro 8(3), ENEURO.0007-21.2021,
2	# "Behavioral and Neural Variability of Naturalistic Arm Movements", on dandiset 000055.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
4	# protocol pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read. The version of record as served by Europe PMC (PMC8225404), from
7	# paper/10.1523-eneuro.0007-21.2021.txt: main text, Materials and Methods, figure legends,
8	# Tables 1 and 2, the legends of the Extended Data figures, and the review history. No PDF was
9	# supplied. The Extended Data figures (1-1, 2-1 to 2-4, 3-1, 4-1 to 4-7, 5-1, 6-1, 6-2) are
10	# EPS downloads and are not in the text; only their legends are. Claims that rest on them are
11	# taken from their legends and from the Results sentences that cite them. The per-subject
12	# electrode table (Extended Data Figure 1-1) and the per-subject feature confidence intervals
13	# (Extended Data Figures 2-3 and 2-4) could not be read.
14	#
15	# Code read. github.com/BruntonUWBio/naturalistic_arm_movements_ecog at commit
16	# 04c6faf2f219586fa834d10c614ef48a694cec55 (17 March 2021), Python 3.6 (MNE 0.19) and MATLAB.
17	# It holds compute_spectral_power.py and tfr_utils.py (Morlet power, baseline, bootstrap
18	# masking, projection to regions), the MATLAB projection of electrodes onto AAL regions
19	# (project_ecog_to_rois.m, EEGLAB 13.5.4b, Measure Projection Toolbox 1.661),
20	# fit_regression_models.py and regression_utils.py (regression), and notebooks for Figures 2,
[... 630 more lines not kept]
```

**Agent**

Reading the protocol and claims is done. Next I'm looking at the example entry formats and the DANDI access notes.

**Agent calls Bash**

```bash
cat docs/archives.md | sed -n '1,200p'; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in entries/001453-fouke-2025/README.md
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
[... 149 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/001453-fouke-2025-01.yaml | head -250
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
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 250,400p attempts/001453-fouke-2025-01.yaml; cat questions/README.md; cat questions/000115.yaml | head -40; ls schemas
```

```
statement: The stimulus codes 0 to 20 have no names or description in the files or the
    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
    file of its stimulus software.
- kind: code_mismatch
  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
    while its conversion of the stimulus software's names gives the reverse (it carries a remap
    that swaps them). The data do not settle which is right; zebrafish barely turn to either, and
    Danionella turn more to the right for code 11, which fits the stimulus software's assignment
    only if the fish turn with lateral motion.
- kind: metadata_error
  statement: Subject ids 0 to 11 are each used for one zebrafish and one Danionella cerebrum, so
    subject_id does not identify an animal. The archive's summary counts 25 subjects and lists
    only Danio rerio; the files hold 37 fish of two species.
- kind: metadata_error
  statement: f0_vtheta is stated in radians/s but holds the heading change per frame in radians,
    and f0_vx and f0_vy are stated in pixels/s but are per frame. In most Danionella files the sum
    of f0_vtheta over a trial does not match the change of f0_theta (median ratios 0.09 to 0.89).
- kind: other
  statement: 18 of 25 zebrafish files and 1 of 12 Danionella files are sampled at 32 to 35 Hz,
    where the Methods state tracking at more than 150 Hz. Their timestamp intervals are regular
[... 180 more lines not kept]
```

**Agent**

Now the dataset itself.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000055/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000055/versions/" | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000055/versions/0.220127.0436/assets/?page_size=100" | python -c "
import json,sys; d=json.load(sys.stdin); print(d['count'])
for a in d['results']: print(a['asset_id'], a['path'], round(a['size']/1e9,2))"; curl -s "https://api.dandiarchive.org/api/dandisets/000055/versions/0.220127.0436/" | python -m json.tool | head -150
```

Result: the fetched text is not kept.

**Agent**

Dataset: one published version (0.220127.0436), 55 files, 846 GB, day sets match Table 2 on filenames. Setting up a dev environment and opening a file.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q h5py remfile pynwb numpy scipy pandas scikit-learn matplotlib dandi nbformat pyyaml jsonschema 2>&1 | tail -3; python -c "import pynwb,h5py;print(pynwb.__version__)"; nproc; free -g
```

```
4.2.0
4
               total        used        free      shared  buff/cache   available
Mem:              15           1           9           0           4          13
Swap:              2           0           2
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > probe.py <<'EOF'
import h5py, remfile, requests, time
aid='7b9e2ca1-9097-488a-b4e9-ac407fb31457'
r=requests.get(f'https://api.dandiarchive.org/api/assets/{aid}/download/',allow_redirects=False)
url=r.headers['Location']; print(url)
t=time.time()
f=h5py.File(remfile.File(url),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name, obj.shape, obj.dtype, obj.chunks, obj.compression, dict((k,(v if not hasattr(v,'shape') or v.size<5 else v.shape)) for k,v in obj.attrs.items() if k not in ('namespace','object_id')))
    else:
        print(name+'/', dict((k,v) for k,v in obj.attrs.items() if k not in ('namespace','object_id','neurodata_type')))
f.visititems(show)
print(time.time()-t)
EOF
python probe.py 2>&1 | head -150
```

```
https://dandiarchive.s3.amazonaws.com/blobs/e54/21f/e5421ff3-05f6-4d5e-a884-6d3e57a11951?response-content-disposition=attachment%3B%20filename%3D%22sub-01_ses-3_behavior%2Becephys.nwb%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=[removed: an AWS key]%2F20261023%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20261023T154912Z&X-Amz-Expires=21600&X-Amz-SignedHeaders=host&X-Amz-Signature=c47b6138b2002594185395e1b709f4b4c41117f81cef40014cc4e20b59c631ff
acquisition/ {}
acquisition/ECGL/ {'comments': 'no comments', 'description': 'Electrooculography for tracking saccades - left'}
acquisition/ECGL/data (43200000,) float32 None None {'conversion': np.float64(nan), 'resolution': np.float64(-1.0), 'unit': 'V'}
acquisition/ECGL/starting_time () float64 None None {'rate': np.float32(500.0), 'unit': 'seconds'}
acquisition/ECGR/ {'comments': 'no comments', 'description': 'Electrooculography for tracking saccades - right'}
acquisition/ECGR/data (43200000,) float32 None None {'conversion': np.float64(nan), 'resolution': np.float64(-1.0), 'unit': 'V'}
acquisition/ECGR/starting_time () float64 None None {'rate': np.float32(500.0), 'unit': 'seconds'}
acquisition/EOGL/ {'comments': 'no comments', 'description': 'Electrooculography for tracking saccades - left'}
acquisition/EOGL/data (43200000,) float32 None None {'conversion': np.float64(nan), 'resolution': np.float64(-1.0), 'unit': 'V'}
acquisition/EOGL/starting_time () float64 None None {'rate': np.float32(500.0), 'unit': 'seconds'}
acquisition/EOGR/ {'comments': 'no comments', 'description': 'Electrooculography for tracking saccades - right'}
acquisition/EOGR/data (43200000,) float32 None None {'conversion': np.float64(nan), 'resolution': np.float64(-1.0), 'unit': 'V'}
acquisition/EOGR/starting_time () float64 None None {'rate': np.float32(500.0), 'unit': 'seconds'}
acquisition/ElectricalSeries/ {'comments': 'no comments', 'description': 'no description'}
acquisition/ElectricalSeries/data (43200000, 94) float32 (84375, 1) gzip {'c
[... 135 more lines not kept]
```

**Agent**

The ECoG is chunked per channel (84375 samples = 169 s per chunk, gzip), so each event window costs ~94 chunk reads. Timing that now, since it decides which spectral claims are feasible.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > probe2.py <<'EOF'
import h5py, remfile, requests, time, numpy as np
aid='7b9e2ca1-9097-488a-b4e9-ac407fb31457'
url=requests.get(f'https://api.dandiarchive.org/api/assets/{aid}/download/',allow_redirects=False).headers['Location']
f=h5py.File(remfile.File(url),'r')
r=f['intervals/reaches']
st=r['start_time'][:]; print(st[:10], st.max(), len(st))
print('dur', (r['stop_time'][:]-st)[:10])
print('ReachEvents', f['processing/behavior/ReachEvents/timestamps'][:10])
print(f['session_start_time'][()], f['session_description'][()], f['general/session_id'][()], f['general/subject/subject_id'][()], f['identifier'][()])
for k in r.keys(): print(k, r[k][:5])
e=f['general/extracellular_ephys/electrodes']
for k in ['x','y','z','location','group_name','good','low_freq_R2','high_freq_R2','standard_deviation','kurtosis','imp','filtering']:
    print(k, e[k][:8])
lab=f['intervals/epochs/labels'][:]; import collections; print(collections.Counter(lab).most_common(20))
d=f['acquisition/ElectricalSeries/data']
t=time.time(); i=int(st[5]*500); x=d[i-2500:i+2500,:]; print('read', time.time()-t, x.shape, np.nanstd(x,0)[:5])
t=time.time(); i=int(st[50]*500); x=d[i-2500:i+2500,:]; print('read', time.time()-t)
t=time.time(); x=d[0:84375,0]; print('1chunk', time.time()-t)
EOF
python probe2.py 2>&1 | tail -40
```

```
0.63333333 0.8        1.43333333 1.9       ]
ReachEvents [ 1791.954  3520.224  3584.342 26884.644 27984.896 28768.352 28853.918
 29639.048 31409.66  31434.982]
b'2000-01-02T19:00:00-05:00' b'no description' b'3' b'01' b'4c571b6c-1028-476f-b0e1-e34aa27b3206'
Bimanual_class [1. 0. 0. 0. 1.]
Bimanual_overlap [0.53333333 0.         0.         0.         0.56666667]
Bimanual_ratio [0.95302723 0.02966791 0.00584825 0.         0.48777761]
Onset_speed_px_per_sec [201.5843534   94.0112274  156.4640741    4.46696938  28.92150996]
Reach_angle_degrees [ 110.4579147  -152.3603329  -103.2923865   -96.86916376   20.46058212]
Reach_magnitude_px [132.2131933   56.06810774 120.0208496   10.90791204  19.31058468]
Speech_ratio [0.245755   0.17399518 0.18533196 0.2800509  0.41486637]
id [0 1 2 3 4]
start_time [ 1791.954  3520.224  3584.342 26884.645 27984.897]
stop_time [ 1792.78733333  3521.19066667  3585.30866667 26885.67833333
 27985.56366667]
x [-45.64849509 -47.34715172 -50.29140891 -51.35896118 -51.21981805
 -51.21500147 -52.29101999 -53.89646881]
y [ 38.56037242  31.1828614   22.15720826  11.78726768   1.71388884
  -6.68089222 -18.12722609 -29.05987344]
z [36.18796239 41.17679881 45.19188514 48.72650925 53.00098123 57.99450481
[... 21 more lines not kept]
```

**Agent**

Reading one event's 10 s window across 94 channels takes ~1.6 s. Next: count all events across the 55 files to estimate the total, and check whether Figshare and an AAL atlas source are reachable.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > probe3.py <<'EOF'
import h5py, remfile, requests, time, numpy as np, json
from concurrent.futures import ThreadPoolExecutor
assets=[]
u="https://api.dandiarchive.org/api/dandisets/000055/versions/0.220127.0436/assets/?page_size=100"
assets=requests.get(u).json()['results']
def info(a):
    url=requests.get(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/",allow_redirects=False).headers['Location']
    f=h5py.File(remfile.File(url),'r')
    e=f['general/extracellular_ephys/electrodes']
    g=[x.decode() for x in e['group_name'][:]]
    st=f['intervals/reaches/start_time'][:]
    return dict(path=a['path'], n=len(st), nre=len(f['processing/behavior/ReachEvents/timestamps']), nch=f['acquisition/ElectricalSeries/data'].shape, ngood=int(e['good'][:].sum()), groups=sorted(set(g)), start=f['session_start_time'][()].decode(), desc=f['processing/behavior/ReachEvents'].attrs['description'], species=f['general/subject/species'][()].decode() if 'species' in f['general/subject'] else None,
      subj={k:(f['general/subject'][k][()] if isinstance(f['general/subject'][k],h5py.Dataset) else None) for k in f['general/subject'].keys()}, x0=float(np.nanmean(e['x'][:])))
t=time.time()
with ThreadPoolExecutor(8) as ex: res=list(ex.map(info, assets))
res.sort(key=lambda r:r['path'])
for r in res: print(r)
print(time.time()-t, sum(r['n'] for r in res))
json.dump(res, open('info.json','w'), default=str)
EOF
python probe3.py 2>&1 | tail -60; curl -s -m 10 -o /dev/null -w "%{http_code}\n" https://api.figshare.com/v2/projects/78666/articles; curl -s -m 10 -o /dev/null -w "%{http_code}\n" https://www.gin.cnrs.fr/wp-content/uploads/AAL3v2_for_SPM12.tar.gz; curl -s -m 10 -o /dev/null -w "%{http_code}\n" https://github.com
```

Result: the fetched text is not kept.

**Agent**

8088 events in the files (per subject 211 to 996). Checking what the paper's Figshare project holds, since the region projection needs either the AAL atlas or the paper's projection matrices.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.figshare.com/v2/projects/78666/articles | python -m json.tool | grep -E '"(id|title|doi|url_public_html)"';
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.figshare.com/v2/articles/12114408 | python -c "
import json,sys; d=json.load(sys.stdin); print(d['description'][:1500]); print(d['version'] if 'version' in d else '')
for f in d['files']: print(f['id'], f['name'], f['size'], f['download_url'])"; curl -s https://api.figshare.com/v2/articles/12115728 | python -c "
import json,sys; d=json.load(sys.stdin); print(d['description'][:1500])
for f in d['files']: print(f['id'], f['name'], f['size'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "false positive|200 |up to|per day|false-positive" *.txt | cut -c1-400 | head -30
```

```
10.1016-j.jneumeth.2021.109199.txt:221:code. Then, we band-pass filtered (1–200 Hz, FIR filter), notch filtered 
10.1016-j.jneumeth.2021.109199.txt:222:(60 Hz and harmonics up to 240 Hz, FIR notch filter) the data to minimize line noise, and downsampled the data to 500 Hz, all using the 
10.1016-j.jneumeth.2021.109199.txt:271:each frame, we annotated up to 9 keypoints on the subject’s body 
10.1016-j.jneumeth.2021.109199.txt:332:the entire movement (up to next rest state), and rest duration before and 
10.1016-j.jneumeth.2021.109199.txt:351:Finally, we generated metadata that we used to remove false positives that arise from pose estimation failures and unusual pose states. To 
10.1016-j.jneumeth.2021.109199.txt:386:guide our search, we selected up to 200 events per day over 5 days for 
10.1016-j.jneumeth.2021.109199.txt:388:to remove any false positives (17.8% mean ± 9.9% s.d. events) (see 
10.1016-j.jneumeth.2021.109199.txt:405:were 200 ms × 5 Hz resolution, truncated at 150 Hz; approximately 
10.1016-j.jneumeth.2021.109199.txt:460:events per subject (487 mean ± 215 per day) across 12 subjects. (Figs. 3 
10.1016-j.jneumeth.2021.109199.txt:551:Fig. 3. [Left] Number of right-wrist movement initiation events discovered per day for each of 12 subjects, totaling 475 to 3526 events per subject across their entire 
10.1016-j.jneumeth.2021.109199.txt:552:duration of clinical observation (268 mean ± 123 s.d. per day). [Right] Raster plot of right-wrist movement initiation event occurrences showing bursts of activity 
10.1016-j.jneumeth.2021.109199.txt:632:We controlled false positives in the event discovery process using a 
10.1016-j.jneumeth.2021.109199.txt:646:false positives. 
10.1016-j.jneumeth.2021.109199.txt:691:We believe that our dataset could serve several other lines of scientific inquiry. As a follow-up to the movement-initiation task described in 
10.1016-j.jneumeth.2021.109199.txt:711:The presence of false positives in the data also motivates exploring 
10.103
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -o -i -E ".{300}removed those with occlusio.{600}" paper/10.1038-s41597-022-01280-y.txt; grep -o -E ".{200}(Reach_|reaches table|ReachEvents|wrist movement events).{300}" paper/10.1038-s41597-022-01280-y.txt | head -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q mne fsspec aiohttp requests 2>&1|tail -1; cat > fif.py <<'EOF'
import fsspec, mne, time
t=time.time()
url='https://ndownloader.figshare.com/files/22280262'
f=fsspec.open(url, block_size=2**16).open()
ep=mne.read_epochs(f, preload=False, verbose='error')
print(time.time()-t, ep)
print(ep.metadata.head()); print(ep.metadata.columns.tolist()); print(len(ep.metadata), ep.info['bads'][:5], ep.tmin, ep.tmax, ep.info['sfreq'])
print(f.cache if hasattr(f,'cache') else '', getattr(f,'loc',None))
EOF
timeout 600 python fif.py 2>&1 | tail -20
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/fif.py", line 5, in <module>
    ep=mne.read_epochs(f, preload=False, verbose='error')
  File "<decorator-gen-172>", line 10, in read_epochs
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/mne/epochs.py", line 4451, in read_epochs
    return EpochsFIF(fname, proj, preload, verbose)
  File "<decorator-gen-173>", line 10, in __init__
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/mne/epochs.py", line 4502, in __init__
    raise ValueError("preload must be used with file-like objects")
ValueError: preload must be used with file-like objects
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > fif2.py <<'EOF'
import fsspec, time, io
from mne._fiff.open import fiff_open
from mne._fiff.tree import dir_tree_find
from mne._fiff.constants import FIFF
from mne._fiff.tag import read_tag
t=time.time()
url='https://ndownloader.figshare.com/files/22280262'
f=fsspec.open(url, block_size=2**16, cache_type='readahead').open()
fid, tree, _ = fiff_open(f, preload=False)
print('open', time.time()-t)
md = dir_tree_find(tree, FIFF.FIFFB_MNE_METADATA)
for d in md[0]['directory']:
    if d.kind == FIFF.FIFF_DESCRIPTION:
        tag = read_tag(fid, d.pos); s=tag.data
print(time.time()-t, s[:500])
from mne.utils import _prepare_read_metadata
import pandas as pd
m=pd.read_json(io.StringIO(s.replace("'",'"')) if False else io.StringIO(s), orient='records') if False else None
from mne.epochs import _prepare_read_metadata as p
md=p(s); print(md.head(), md.columns.tolist(), len(md))
EOF
timeout 600 python fif2.py 2>&1 | tail -20
```

```
open 2.353726387023926
2.6809709072113037 [{"day":3,"time":24077100,"event_timestamp":24077100,"mvmt":"r_wrist","vid_name":"f0bbc9a9_6_0676.avi","event_frame_idx":129,"false_pos":0,"reach_duration":35,"reach_r":48.2852742025,"reach_a":67.5649154926,"onset_velocity":1.6925100587,"other_reach_overlap":5,"bimanual":1,"other_lead_lag":3.0,"patient_id":"f0bbc9a9","I_over_C_ratio":0.0915287186,"r_wrist_x":[258.9048095942,258.9048095942,258.9048095942,258.9854705334,258.9854705334,258.9854705334,258.8006622791,258.7746561766,258.7746561766,258
   day  ...  audio_ratio
0    3  ...     0.301591
1    3  ...     0.384327
2    3  ...     0.339950
3    3  ...     0.324143
4    3  ...     0.233235

[5 rows x 21 columns] ['day', 'time', 'event_timestamp', 'mvmt', 'vid_name', 'event_frame_idx', 'false_pos', 'reach_duration', 'reach_r', 'reach_a', 'onset_velocity', 'other_reach_overlap', 'bimanual', 'other_lead_lag', 'patient_id', 'I_over_C_ratio', 'r_wrist_x', 'r_wrist_y', 'l_wrist_x', 'l_wrist_y', 'audio_ratio'] 15
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s,indent=1)[:6000])
EOF
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "One attempt at reproducing the claims of a target",
 "description": "Draft. To be revised after the pilot. An attempt is recorded whether or not it produced a working notebook.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "id",
  "dataset",
  "paper",
  "date",
  "provenance",
  "outcomes"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "id": {
[... 215 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -o -E ".{100}(0 dB|115|3 SD|standard deviations above).{500}" paper/10.1523-eneuro.0007-21.2021.txt | head; grep -o -E ".{50}(−0.5|-0.5|time-frequency|Morlet).{300}" paper/10.1523-eneuro.0007-21.2021.txt | head -8
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; mkdir -p entries/000055-peterson-2021
```

```
Fri Oct 23 15:55:37 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/000055-peterson-2021/ajile.py",
 "content": "\"\"\"Loading and measures for dandiset 000055 (AJILE12) and Peterson et al. (2021), eNeuro.\n\nOther notebooks on this dandiset can import this module. It streams the NWB files from the\nDANDI archive (remfile and h5py) and reads two public Figshare items of the paper by DOI.\n\nWhere the parameters come from:\n\n- Segments of 10 s centred on each movement onset, Morlet power at 1 to 121 Hz in 5 Hz steps,\n  n_cycles = frequency / 4, decimated by 50, 10*log10, minus each event's own mean over\n  -1.5 to -1 s: the claims file's opening comment (Methods and the paper's code).\n- LFB 8-32 Hz (bins 11 to 31 Hz) and HFB 76-100 Hz (bins 76 to 96 Hz) over 0 to 0.5 s, band\n  mean (Methods) and band median (code): the claims file's opening comment.\n- Region projection: the paper's own projection matrices (Figshare 10.6084/m9.figshare.12114408.v1),\n  bad electrodes set to weight 0 and each region's weights renormalised to sum to 1; regions\n  kept when the density row averaged over subjects exceeds 3: the claims file's opening comment.\n- Rejection of segments by their power spectral density (power below 0 dB, or 115-125 Hz power\n  more than 3 SD above all segments): the Methods, as the claims file gives them. How the PSD is\n  computed is not given; Welch's method with 1 s windows is a standard choice, and the two\n  readings of which channels count are in `segment_rejection` (see the question in\n  questions/000055.yaml).\n- Time-of-day bins (0-8, 8-16, 16-24 h) and the folding of the reach angle: the claims file.\n\"\"\"\nimport io\nimport json\nimport time\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\n\nDANDISET = \"000055\"\nVERSION = \"0.220127.0436\"\nAPI = \"https://api.dandiarchive.org/api\"\nFS = 500.0                     # ECoG sampling rate in the files (checked in the notebook)\nPOSE_FS = 30.0\nSEG_HALF = 5.0                 # 10 s segments centred on onset (claims file)\nFREQS = np.arange(1, 122, 5)   # 1, 6, ..., 121 Hz (claims file, code)\nDECIM = 50                     # 10 Hz time bins (claims file, code)\nBASE = (-1.5, -1.0)            # baseline window (Methods)\nKEEP = (-1.5, 1.5)             # time bins kept after the transform (covers every window used)\nLFB = (8, 32)\nHFB = (76, 100)\nWIN = (0.0, 0.5)               # banded power window (Methods)\nROI_ARTICLE = 12114408         # Figshare \"ROI projection matrices and labels\", version 1\nEPOCH_ARTICLE = 12115728       # Figshare \"Naturalistic reach ECoG data\", version 1\nROI_DOI = \"10.6084/m9.figshare.12114408.v1\"\nEPOCH_DOI = \"10.6084/m9.figshare.12115728.v1\"\n\n\ndef assets():\n    \"\"\"The version's NWB assets as a DataFrame (path, asset_id, size, subject, day).\"\"\"\n    url = f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200\"\n    rows = []\n    while url:\n        r = requests.get(url, timeout=60).json()\n        rows += r[\"results\"]\n        url = r[\"next\"]\n    df = pd.DataFrame([{\"path\": a[\"path\"], \"asset_id\": a[\"asset_id\"], \"size\": a[\"size\"]}\n                       for a in rows])\n    df[\"subject\"] = df.path.str.extract(r\"sub-(\\d+)/\")[0].astype(int)\n    df[\"day\"] = df.path.str.extract(r\"ses-(\\d+)_\")[0].astype(int)\n    return df.sort_values([\"subject\", \"day\"]).reset_index(drop=True)\n\n\ndef s3_url(asset_id):\n    r = requests.get(f\"{API}/assets/{asset_id}/download/\", allow_redirects=False, timeout=60)\n    return r.headers[\"Location\"]\n\n\ndef open_nwb(asset_id, cache_mb=0):\n    \"\"\"Open a streamed file with h5py. cache_mb sets h5py's chunk cache.\"\"\"\n    kw = {}\n    if cache_mb:\n        kw = dict(rdcc_nbytes=cache_mb * 2**20, rdcc_nslots=100003)\n    return h5py.File(remfile.File(s3_url(asset_id)), \"r\", **kw)\n\n\ndef _s(x):\n    return x.decode() if isinstance(x, bytes) else x\n\n\ndef read_meta(asset_id):\n    \"\"\"Everything but the ECoG and pose arrays: reaches, electrodes, epochs labels, attributes.\"\"\"\n    f = open_nwb(asset_id)\n    out = {}\n    r = f[\"intervals/reaches\"]\n    out[\"reaches\"] = pd.DataFrame({k: r[k][:] for k in r.keys() if k != \"id\"})\n    out[\"reach_events\"] = f[\"processing/behavior/ReachEvents/timestamps\"][:]\n    out[\"reach_side\"] = _s(f[\"processing/behavior/ReachEvents\"].attrs[\"description\"])\n    e = f[\"general/extracellular_ephys/electrodes\"]\n    cols = [c for c in e.attrs[\"colnames\"] if c != \"group\"]\n    el = pd.DataFrame({c: e[c][:] for c in cols})\n    for c in el.columns:\n        if el[c].dtype == object:\n            el[c] = el[c].map(_s)\n    out[\"electrodes\"] = el\n    ep = f[\"intervals/epochs\"]\n    out[\"epochs\"] = pd.DataFrame({\"start\": ep[\"start_time\"][:], \"stop\": ep[\"stop_time\"][:],\n                                  \"label\": [_s(x) for x in ep[\"labels\"][:]]})\n    es = f[\"acquisition/ElectricalSeries\"]\n    out[\"ecog_shape\"] = es[\"data\"].shape\n    out[\"ecog_rate\"] = float(es[\"starting_time\"].attrs[\"rate\"])\n    out[\"ecog_t0\"] = float(es[\"starting_time\"][()])\n    out[\"ecog_unit\"] = _s(es[\"data\"].attrs[\"unit\"])\n    out[\"ecog_conversion\"] = float(es[\"data\"].attrs[\"conversion\"])\n    out[\"ecog_chunks\"] = es[\"data\"].chunks\n    p = f[\"processing/behavior/Position\"]\n    out[\"pose_keys\"] = sorted(p.keys())\n    w = p[\"R_Wrist\"]\n    out[\"pose_shape\"] = w[\"data\"].shape\n    out[\"pose_rate\"] = float(w[\"starting_time\"].attrs[\"rate\"])\n    out[\"pose_t0\"] = float(w[\"starting_time\"][()])\n    out[\"pose_unit\"] = _s(w[\"data\"].attrs[\"unit\"])\n    out[\"session_start\"] = _s(f[\"session_start_time\"][()])\n    out[\"subject_attrs\"] = {k: _s(f[\"general/subject\"][k][()]) for k in f[\"general/subject\"].keys()}\n    out[\"groups\"] = {k: _s(f[f\"general/extracellular_ephys/{k}\"].attrs.get(\"description\", \"\"))\n                     for k in f[\"general/extracellular_ephys\"].keys() if k != \"electrodes\"}\n    out[\"acq\"] = sorted(f[\"acquisition\"].keys())\n    f.close()\n    return out\n\n\ndef wrist_traces(asset_id, onsets, side, t=(-1.5, 1.5)):\n    \"\"\"Wrist (x, y) around each onset, for the contralateral and the ipsilateral wrist.\n\n    Returns arrays (events, frames, 2) and the time axis. Frames are the pose frames nearest\n    to each onset plus offsets at 30 Hz.\"\"\"\n    f = open_nwb(asset_id, cache_mb=64)\n    p = f[\"processing/behavior/Position\"]\n    contra = \"R_Wrist\" if side.startswith(\"r\") else \"L_Wrist\"\n    ipsi = \"L_Wrist\" if contra == \"R_Wrist\" else \"R_Wrist\"\n    t0 = float(p[contra][\"starting_time\"][()])\n    off = np.arange(int(round(t[0] * POSE_FS)), int(round(t[1] * POSE_FS)) + 1)\n    res = {}\n    for name, key in ((\"contra\", contra), (\"ipsi\", ipsi)):\n        d = p[key][\"data\"]\n        n = d.shape[0]\n        arr = np.full((len(onsets), len(off), 2), np.nan)\n        for i, on in enumerate(onsets):\n            c = int(round((on - t0) * POSE_FS))\n            a, b = c + off[0], c + off[-1] + 1\n            if a < 0 or b > n:\n                continue\n            arr[i] = d[a:b, :]\n        res[name] = arr\n    f.close()\n    return res, off / POSE_FS\n\n\n# ---------------------------------------------------------------- Figshare inputs\n\ndef figshare_files(article):\n    d = requests.get(f\"https://api.figshare.com/v2/articles/{article}/versions/1\", timeout=60).json()\n    return {x[\"name\"]: x for x in d[\"files\"]}\n\n\ndef roi_matrices():\n    \"\"\"The paper's projection matrices: per subject a DataFrame (electrodes x regions), and the\n    density row (first numerical row of the file, as the Figshare description says).\"\"\"\n    files = figshare_files(ROI_ARTICLE)\n    out = {}\n    for s in range(1, 13):\n        name = f\"aal_{s:02d}_elecs2ROI.csv\"\n        txt = requests.get(files[name][\"download_url\"], timeout=120).text\n        out[s] = txt\n    return out, files\n\n\ndef parse_roi(txt):\n    df = pd.read_csv(io.StringIO(txt), header=None)\n    return df\n\n\ndef epoch_metadata(name, files):\n    \"\"\"The pandas metadata stored in one Figshare MNE epochs file, read over HTTP range requests\n    from the file's tag directory (the ECoG data in the file are not read).\"\"\"\n    import fsspec\n    from mne._fiff.constants import FIFF\n    from mne._fiff.open import fiff_open\n    from mne._fiff.tag import read_tag\n    from mne._fiff.tree import dir_tree_find\n    from mne.epochs import _prepare_read_metadata\n    for attempt in range(3):\n        try:\n            f = fsspec.open(files[name][\"download_url\"], block_size=2**16,\n                            cache_type=\"readahead\").open()\n            fid, tree, _ = fiff_open(f, preload=False)\n            md = dir_tree_find(tree, FIFF.FIFFB_MNE_METADATA)\n            s = None\n            for d in md[0][\"directory\"]:\n                if d.kind == FIFF.FIFF_DESCRIPTION:\n                    s = read_tag(fid, d.pos).data\n            bads = None\n            meas = dir_tree_find(tree, FIFF.FIFFB_MEAS_INFO)\n            for d in meas[0][\"directory\"]:\n                if d.kind == FIFF.FIFF_MNE_CH_NAME_LIST:\n                    pass\n            f.close()\n            return _prepare_read_metadata(s)\n        except Exception:\n            if attempt == 2:\n                raise\n            time.sleep(5)\n\n\n# ---------------------------------------------------------------- spectral power\n\n_WAVELETS = None\n\n\ndef _wavelets():\n    \"\"\"Morlet wavelets as mne.time_frequency.morlet builds them (sigma = n_cycles / (2 pi f),\n    support +-5 sigma, unit energy), n_cycles = f / 4.\"\"\"\n    global _WAVELETS\n    if _WAVELETS is None:\n        from mne.time_frequency import morlet\n        _WAVELETS = morlet(FS, FREQS, n_cycles=FREQS / 4.0)\n    return _WAVELETS\n\n\ndef morlet_power(x):\n    \"\"\"x: (channels, samples) in microvolts. Returns 10*log10 power, (channels, freqs, bins),\n    decimated by DECIM, and the time axis of the bins relative to the segment centre.\"\"\"\n    from scipy.signal import fftconvolve\n    ws = _wavelets()\n    n = x.shape[1]\n    out = np.empty((x.shape[0], len(FREQS), int(np.ceil(n / DECIM))), np.float32)\n    for k, w in enumerate(ws):\n        c = fftconvolve(x, w[None, :], mode=\"same\", axes=1)\n        p = (c.real ** 2 + c.imag ** 2)[:, ::DECIM]\n        out[:, k, :] = 10 * np.log10(np.maximum(p, 1e-30))\n    t = np.arange(out.shape[2]) * DECIM / FS - SEG_HALF\n    return out, t\n\n\ndef welch_db(x):\n    \"\"\"Welch PSD per channel with 1 s windows (standard choice), in dB of microvolt^2/Hz.\n    Returns (mean dB over 1-200 Hz per channel, mean dB over 115-125 Hz per channel).\"\"\"\n    from scipy.signal import welch\n    fr, p = welch(x, fs=FS, nperseg=int(FS), axis=1)\n    db = 10 * np.log10(np.maximum(p, 1e-30))\n    a = db[:, (fr >= 1) & (fr <= 200)].mean(1)\n    b = db[:, (fr >= 115) & (fr <= 125)].mean(1)\n    return a, b\n\n\ndef _band_idx(band):\n    return np.where((FREQS >= band[0]) & (FREQS <= band[1]))[0]\n\n\ndef extract_file(asset_id, onsets, proj=None, log=None):\n    \"\"\"Spectral measures for the events of one file.\n\n    onsets: event times in s. proj: (channels, regions) weights or None.\n    Returns a dict of arrays, one row per event:\n      'ok': whether the full 10 s segment is inside the recording;\n      'welch_all', 'welch_hf': (events, channels) Welch dB over 1-200 Hz and 115-125 Hz;\n      'band': (events, channels, 8): LFB/HFB x mean/median x with/without baseline;\n      'roi': (events, regions, freqs, bins) baseline-subtracted region power (if proj);\n      'tbins': time axis of the kept bins.\"\"\"\n    f = open_nwb(asset_id)\n    d = f[\"acquisition/ElectricalSeries/data\"]\n    conv = float(d.attrs[\"conversion\"])\n    n, nch = d.shape\n    cs = d.chunks[0]\n    half = int(SEG_HALF * FS)\n    order = np.argsort(onsets)\n    ne = len(onsets)\n    res = {\"ok\": np.zeros(ne, bool), \"welch_all\": np.full((ne, nch), np.nan, np.float32),\n           \"welch_hf\": np.full((ne, nch), np.nan, np.float32),\n           \"band\": np.full((ne, nch, 8), np.nan, np.float32)}\n    roi = None\n    lf, hf = _band_idx(LFB), _band_idx(HFB)\n    cache = {}\n    t_read = 0.0\n    tb = None\n    for i in order:\n        c = int(round(onsets[i] * FS))\n        a, b = c - half, c + half\n        if a < 0 or b > n:\n            continue\n        c0, c1 = a // cs, (b - 1) // cs\n        t1 = time.time()\n        for k in list(cache):\n            if k < c0:\n                del cache[k]\n        for k in range(c0, c1 + 1):\n            if k not in cache:\n                cache[k] = d[k * cs:min((k + 1) * cs, n), :]\n        t_read += time.time() - t1\n        blk = np.concatenate([cache[k] for k in range(c0, c1 + 1)], axis=0)\n        x = blk[a - c0 * cs:b - c0 * cs, :].T.astype(np.float64)\n        x = np.nan_to_num(x)\n        # values are stored in microvolts (conversion 1e-6 to volts); keep microvolts\n        wa, wh = welch_db(x)\n        res[\"welch_all\"][i], res[\"welch_hf\"][i] = wa, wh\n        p, t = morlet_power(x)\n        bmask = (t >= BASE[0]) & (t <= BASE[1])\n        base = p[:, :, bmask].mean(2, keepdims=True)\n        pb = p - base\n        wmask = (t >= WIN[0]) & (t <= WIN[1])\n        for j, (src) in enumerate((pb, p)):\n            for bi, idx in enumerate((lf, hf)):\n                sub = src[:, idx][:, :, wmask]\n                res[\"band\"][i, :, j * 4 + bi * 2 + 0] = sub.mean((1, 2))\n                res[\"band\"][i, :, j * 4 + bi * 2 + 1] = np.median(np.median(sub, 2), 1)\n        kmask = (t >= KEEP[0] - 1e-9) & (t <= KEEP[1] + 1e-9)\n        tb = t[kmask]\n        if proj is not None:\n            if roi is None:\n                roi = np.full((ne, proj.shape[1], len(FREQS), kmask.sum()), np.nan, np.float32)\n            roi[i] = np.einsum(\"cr,cft->rft\", proj, pb[:, :, kmask])\n        res[\"ok\"][i] = True\n    f.close()\n    res[\"roi\"] = roi\n    res[\"tbins\"] = tb\n    res[\"t_read\"] = t_read\n    return res\n\n\n# band layout in res['band'][..., k]\nBAND_COLS = [\"lfb_mean_bl\", \"lfb_median_bl\", \"hfb_mean_bl\", \"hfb_median_bl\",\n             \"lfb_mean_raw\", \"lfb_median_raw\", \"hfb_mean_raw\", \"hfb_median_raw\"]\n\n\ndef fold_angle(a):\n    \"\"\"Fold the image angle to -90 (down) .. +90 (up) degrees, as the claims file gives it from\n    the code: negate the image angle (image y points down) and fold 90-270 degrees.\"\"\"\n    a = -np.asarray(a, float)\n    a = (a + 180) % 360 - 180          # -180..180\n    a = np.where(a > 90, 180 - a, a)\n    a = np.where(a < -90, -180 - a, a)\n    return a\n"
}
```

```
File created successfully at: entries/000055-peterson-2021/ajile.py (file state is current in your context — no need to Read it back)
```

**Agent**

Timing the extraction on one file (sub-01 day 3, 156 events):

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t1.py <<'EOF'
import sys, time; sys.path.insert(0,'entries/000055-peterson-2021')
import ajile, numpy as np
aid='7b9e2ca1-9097-488a-b4e9-ac407fb31457'
m=ajile.read_meta(aid)
on=m['reaches'].start_time.values[:40]
t=time.time(); r=ajile.extract_file(aid, on); print('40 events', time.time()-t, 'read', r['t_read'])
print(r['ok'].sum(), np.nanmedian(r['welch_all']), np.nanmin(r['welch_all']), r['band'][:3,1,:])
print(len(set((on*500)//84375)))
EOF
python t1.py
```

```
40 events 35.867188453674316 read 27.860945224761963
40 -7.235352 -17.362467 [[ 1.1744856   3.034916    0.43547186  0.26750803 36.12702    37.461845
  13.636437   13.283242  ]
 [-0.77295417 -0.31513596  2.3286614   4.6091995  34.08397    35.241993
  16.010492   17.1715    ]
 [ 3.7352245   1.9158077   0.8894545   1.3220468  39.718075   37.453552
  16.63457    19.222008  ]]
25
Shell cwd was reset to
```

**Agent**

One chunk row (169 s × all channels) takes ~1 s to stream and events cluster, so 40 events cost 36 s on one stream. Testing parallel throughput across 8 processes to estimate the full run:

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t2.py <<'EOF'
import sys, time; sys.path.insert(0,'entries/000055-peterson-2021')
import ajile, numpy as np
from concurrent.futures import ProcessPoolExecutor
A=ajile.assets()
sel=A.iloc[::7].head(8)
def job(aid):
    import os; os.environ['OMP_NUM_THREADS']='1'
    m=ajile.read_meta(aid); on=m['reaches'].start_time.values[:25]
    t=time.time(); r=ajile.extract_file(aid,on); 
    return time.time()-t, r['t_read'], len(set((on*500).astype(int)//84375)), m['ecog_shape'][1]
t=time.time()
with ProcessPoolExecutor(8) as ex: out=list(ex.map(job, sel.asset_id))
print(out); print('wall', time.time()-t)
EOF
OMP_NUM_THREADS=1 python t2.py
```

```
[(27.54120421409607, 17.59908413887024, 15, 94), (23.638983011245728, 15.005029201507568, 16, 86), (35.834768295288086, 27.55780053138733, 23, 84), (22.42200541496277, 13.840502262115479, 15, 80), (18.22524118423462, 11.61410665512085, 14, 64), (32.94536542892456, 25.378108739852905, 14, 126), (28.205014944076538, 16.64043426513672, 14, 126), (32.05163598060608, 22.9482204914093, 19, 106)]
wall 37.683162689208984
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python -c "
import numpy as np, time
from sklearn.linear_model import HuberRegressor
rng=np.random.default_rng(0); X=rng.normal(size=(600,18)); y=X[:,0]*.3+rng.standard_t(3,600)
t=time.time()
for i in range(50): HuberRegressor().fit(X[:540],y[:540])
print((time.time()-t)/50)
X=X[:,:4]
t=time.time()
for i in range(50): HuberRegressor().fit(X[:540],y[:540])
print((time.time()-t)/50)
"
```

```
0.0011204957962036132
0.000857248306274414
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t3.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'entries/000055-peterson-2021')
import ajile, numpy as np, pandas as pd
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
A=ajile.assets()
files=ajile.figshare_files(ajile.EPOCH_ARTICLE)
names=sorted(files)
def g(n): return n, ajile.epoch_metadata(n, files)
t=time.time()
with ProcessPoolExecutor(8) as ex: md=dict(ex.map(g, names))
print('fig', time.time()-t)
with ProcessPoolExecutor(8) as ex: meta=dict(zip(A.path, ex.map(ajile.read_meta, A.asset_id)))
print('meta', time.time()-t)
pickle.dump((A,md,meta), open('cache.pkl','wb'))
EOF
python t3.py
```

```
fig 18.86319899559021
meta 31.05221724510193
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pickle, numpy as np, pandas as pd
A,md,meta=pickle.load(open('cache.pkl','rb'))
n0=sorted(md)[0]; m=md[n0]; print(m.drop(columns=['r_wrist_x','r_wrist_y','l_wrist_x','l_wrist_y']).head(8).to_string())
r=meta['sub-01/sub-01_ses-3_behavior+ecephys.nwb']['reaches']; print(r.head(8).to_string())
print(len(m), len(r), m.false_pos.sum())
print(meta['sub-01/sub-01_ses-3_behavior+ecephys.nwb']['session_start'])
print(np.array(m.r_wrist_x.iloc[0]).shape)
tot=0
for p in A.path:
    s=int(p[4:6]); d=int(p.split('ses-')[1][0])
    nm=[k for k in md if k.startswith(f'subj_{s:02d}_day_{d}_')][0]
    print(p, nm, len(meta[p]['reaches']), len(md[nm]), int(md[nm].false_pos.sum()))
"
```

```
day      time  event_timestamp     mvmt             vid_name  event_frame_idx  false_pos patient_id  I_over_C_ratio  audio_ratio  reach_duration     reach_r     reach_a  onset_velocity  other_reach_overlap  bimanual  other_lead_lag
0    3   1791954          1791954  r_wrist  a0f66459_5_0486.avi              785          1   a0f66459        0.953027     0.245755              25  132.213193  110.457915        6.719478                   16         1           -30.0
1    3   3520224          3520224  r_wrist  a0f66459_5_0500.avi             2206          0   a0f66459        0.029668     0.173995              29   56.068108 -152.360333        3.133708                    0         0             NaN
2    3   3584342          3584342  r_wrist  a0f66459_5_0501.avi              536          0   a0f66459        0.005848     0.185332              29  120.020850 -103.292387        5.215469                    0         0             NaN
3    3  26884645         26884645  r_wrist  a0f66459_5_0695.avi             1165          1   a0f66459        0.000000     0.280051              31   10.907912  -96.869164        0.148899                    0         0             NaN
4    3  27984897         27984897  r_wrist  a0f66459_5_0704.avi             1799          1   a0f66459        0.487778     0.414866              20   19.310585   20.460582        0.964050                   17         1             3.0
5    3  28768352         28768352  r_wrist  a0f66459_5_0711.avi               73          0   a0f66459        0.039133     0.365911              41   37.482779  147.428994        3.061077                    0         0             NaN
6    3  28853918         28853918  r_wrist  a0f66459_5_0711.avi             2640          0   a0f66459        0.030491     0.501548              19   35.601992 -122.635080        2.163772                    0         0             NaN
7    3  29639049         29639049  r_wrist  a0f66459_6_0000.avi              674          0   a0f66459        0.454378     
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pickle, numpy as np, pandas as pd
A,md,meta=pickle.load(open('cache.pkl','rb'))
for p in ['sub-01/sub-01_ses-7_behavior+ecephys.nwb','sub-04/sub-04_ses-3_behavior+ecephys.nwb','sub-06/sub-06_ses-3_behavior+ecephys.nwb']:
    s=int(p[4:6]); d=int(p.split('ses-')[1][0]); nm=[k for k in md if k.startswith(f'subj_{s:02d}_day_{d}_')][0]
    print(p, meta[p]['session_start'], md[nm][['time','event_timestamp']].head(3).values.tolist(), meta[p]['reaches'].start_time.head(3).values, meta[p]['ecog_t0'], meta[p]['pose_t0'], meta[p]['ecog_shape'][0]/500/3600)
# sleep label by clock
rows=[]
for p,m in meta.items():
    st=pd.Timestamp(m['session_start']); 
    h0=st.tz_convert('UTC').hour+st.tz_convert('UTC').minute/60
    h1=st.hour+st.minute/60
    e=m['epochs']; s=e[e.label=='Sleep/rest']
    mid=(s.start+s.stop)/2/3600
    rows+= [((h0+x)%24,(h1+x)%24) for x in mid]
r=np.array(rows); print('sleep hours, UTC reading', np.histogram(r[:,0],bins=range(0,25,3))[0]); print('local -05 reading', np.histogram(r[:,1],bins=range(0,25,3))[0])
allr=pd.concat([m['reaches'] for m in meta.values()]); print(allr.isna().sum().to_dict()); print(allr.describe().T.to_string())
f=pd.concat(md.values()); print((f.reach_duration/30).describe(), f.other_lead_lag.isna().mean(), f.I_over_C_ratio.isna().sum())
"
```

```
sub-01/sub-01_ses-7_behavior+ecephys.nwb 2000-01-07T03:31:22.414000-05:00 [[32313385, 32313385], [32323618, 32323618], [32800671, 32800671]] [32313.385 32323.618 32800.671] 0.0 0.0 15.477107222222223
sub-04/sub-04_ses-3_behavior+ecephys.nwb 2000-01-03T03:20:48.322000-05:00 [[49319452, 49319452], [50646161, 50646161], [50689061, 50689061]] [49319.452 50646.161 50689.061] 0.0 0.0 15.65324388888889
sub-06/sub-06_ses-3_behavior+ecephys.nwb 2000-01-03T03:07:20.566000-05:00 [[29754283, 29754283], [29785583, 29785583], [31504309, 31504309]] [29754.283 29785.583 31504.309] 0.0 0.0 15.877620555555556
sleep hours, UTC reading [3280 3594 2060 1143 1107  991  928 2505]
local -05 reading [2597 1271 1094 1108  928 1738 3159 3713]
{'Bimanual_class': 0, 'Bimanual_overlap': 0, 'Bimanual_ratio': 0, 'Onset_speed_px_per_sec': 0, 'Reach_angle_degrees': 0, 'Reach_magnitude_px': 0, 'Speech_ratio': 0, 'start_time': 0, 'stop_time': 0}
                         count          mean           std         min           25%           50%           75%           max
Bimanual_class          8088.0      0.726261      0.445904    0.000000      0.000000      1.000000      1.000000      1.000000
Bimanual_overlap        8088.0      0.574720      0.587977    0.000000      0.000000      0.466667      0.933333      3.833333
Bimanual_ratio          8088.0      0.256181      0.272983    0.000000      0.022210      0.136723      0.452750      1.000000
Onset_speed_px_per_sec  8088.0    133.749204    114.373369    0.000000     59.882017    103.494220    171.086759   1492.069915
Reach_angle_degrees     8088.0    -33.693680     96.088785 -179.980165   -105.443952    -67.153638     42.749073    179.848348
Reach_magnitude_px      8088.0    102.092205     69.294338    3.926522     54.157260     87.686988    130.967914    680.562436
Speech_ratio            8088.0      0.309974      0.135430    0.000000      0.202715      0.302111      0.410594      0.826687
start_time              8088.0  50271.031122  19822.093268  
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import sys; sys.path.insert(0,'entries/000055-peterson-2021')
import ajile, pickle, io, pandas as pd, numpy as np
txt,files=ajile.roi_matrices()
pickle.dump(txt,open('roi.pkl','wb'))
t=txt[1]; print(t[:1500])
print([ (s, len(txt[s].splitlines())) for s in txt])
c=files['aal_01_ROIcentroids_Lside.csv']; import requests; print(requests.get(c['download_url']).text[:800])
"
```

```
Precentral_L,Precentral_R,Frontal_Sup_L,Frontal_Sup_R,Frontal_Sup_Orb_L,Frontal_Sup_Orb_R,Frontal_Mid_L,Frontal_Mid_R,Frontal_Mid_Orb_L,Frontal_Mid_Orb_R,Frontal_Inf_Oper_L,Frontal_Inf_Oper_R,Frontal_Inf_Tri_L,Frontal_Inf_Tri_R,Frontal_Inf_Orb_L,Frontal_Inf_Orb_R,Rolandic_Oper_L,Rolandic_Oper_R,Supp_Motor_Area_L,Supp_Motor_Area_R,Olfactory_L,Olfactory_R,Frontal_Sup_Medial_L,Frontal_Sup_Medial_R,Frontal_Med_Orb_L,Frontal_Med_Orb_R,Rectus_L,Rectus_R,Insula_L,Insula_R,Cingulum_Ant_L,Cingulum_Ant_R,Cingulum_Mid_L,Cingulum_Mid_R,Cingulum_Post_L,Cingulum_Post_R,Hippocampus_L,Hippocampus_R,ParaHippocampal_L,ParaHippocampal_R,Amygdala_L,Amygdala_R,Calcarine_L,Calcarine_R,Cuneus_L,Cuneus_R,Lingual_L,Lingual_R,Occipital_Sup_L,Occipital_Sup_R,Occipital_Mid_L,Occipital_Mid_R,Occipital_Inf_L,Occipital_Inf_R,Fusiform_L,Fusiform_R,Postcentral_L,Postcentral_R,Parietal_Sup_L,Parietal_Sup_R,Parietal_Inf_L,Parietal_Inf_R,SupraMarginal_L,SupraMarginal_R,Angular_L,Angular_R,Precuneus_L,Precuneus_R,Paracentral_Lobule_L,Paracentral_Lobule_R,Caudate_L,Caudate_R,Putamen_L,Putamen_R,Pallidum_L,Pallidum_R,Thalamus_L,Thalamus_R,Heschl_L,Heschl_R,Temporal_Sup_L,Temporal_Sup_R,Temporal_Pole_Sup_L,Temporal_Pole_Sup_R,Temporal_Mid_L,Temporal_Mid_R,Temporal_Pole_Mid_L,Temporal_Pole_Mid_R,Temporal_Inf_L,Temporal_Inf_R,Cerebelum_Crus1_L,Cerebelum_Crus1_R,Cerebelum_Crus2_L,Cerebelum_Crus2_R,Cerebelum_3_L,Cerebelum_3_R,Cerebelum_4_5_L,Cerebelum_4_5_R,Cerebelum_6_L,Cerebelum_6_R,Cerebelum_7b_L,Cerebelum_7b_R,Cere
[(1, 100), (2, 88), (3, 98), (4, 86), (5, 108), (6, 82), (7, 66), (8, 94), (9, 128), (10, 128), (11, 108), (12, 126)]
x,y,z
-39.2,-6.92,50.36
0,0,0
-19.448,32.793,42.172
0,0,0
-19.733,44.333,-13.533
0,0,0
-34.078,32.247,34.273
0,0,0
-32,50.077,-11.154
0,0,0
-49.6,11.8,17.4
0,0,0
-46,30.556,13.444
0,0,0
-37.913,32.391,-11.261
0,0,0
-49.5,-9,12.5
[... 45 more lines not kept]
```

**Agent**

Row counts of the projection matrices match the DANDI channel counts for 11 subjects (header plus density row plus one row per electrode). S01 has 98 rows against 94 channels. Looking closer:

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pickle, io, pandas as pd, numpy as np
txt=pickle.load(open('roi.pkl','rb'))
for s in [1,2]:
    df=pd.read_csv(io.StringIO(txt[s]))
    print(s, df.shape, df.iloc[0][['Precentral_L','Precentral_R','Postcentral_L','Frontal_Mid_L']].values, df.iloc[1:].sum(0).sort_values().tail(5).to_dict())
    print(df.iloc[-6:, :8])
    print(df.iloc[1:].sum(1).describe())
"
```

```
<string>:6: Pandas4Warning: Starting with pandas version 4.0 all arguments of sum will be keyword-only.
<string>:8: Pandas4Warning: Starting with pandas version 4.0 all arguments of sum will be keyword-only.
<string>:6: Pandas4Warning: Starting with pandas version 4.0 all arguments of sum will be keyword-only.
<string>:8: Pandas4Warning: Starting with pandas version 4.0 all arguments of sum will be keyword-only.
1 (99, 116) [4.7166e+00 1.9466e-15 7.3174e+00 3.8951e+00] {'SupraMarginal_L': 1.0000095017152486, 'Heschl_L': 1.0000095712360395, 'Angular_L': 1.0000097431901558, 'Cerebelum_6_L': 1.0000108266230074, 'Cerebelum_9_L': 1.000011794949882}
    Precentral_L  Precentral_R  ...  Frontal_Mid_L  Frontal_Mid_R
93  8.552500e-23  3.346800e-28  ...   1.278200e-31   5.891100e-38
94  4.722600e-16  4.468000e-30  ...   2.430500e-25   2.631100e-36
95  0.000000e+00  0.000000e+00  ...   0.000000e+00   0.000000e+00
96  0.000000e+00  0.000000e+00  ...   0.000000e+00   0.000000e+00
97  0.000000e+00  0.000000e+00  ...   0.000000e+00   0.000000e+00
98  0.000000e+00  0.000000e+00  ...   0.000000e+00   0.000000e+00

[6 rows x 8 columns]
count    98.000000
mean      1.173470
std       3.247142
min       0.000000
25%       0.174403
50%       0.273209
[... 23 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "questions/000055.yaml",
 "content": "dandiset: \"000055\"\npaper: doi:10.1523/eneuro.0007-21.2021\nquestions:\n- claim: fig2-event-counts\n  asked: 2026-10-23\n  question: >-\n    Reading (b) of the event set drops \"ECoG segments with power below 0 dB or with 115-125 Hz\n    power more than 3 SD above all segments\". How is that power computed and over what? The\n    claims file does not say which spectral estimate is used (Welch, multitaper, the Morlet\n    power), over which frequencies the \"power below 0 dB\" is taken, whether it is judged per\n    electrode or on the mean over electrodes, whether bad electrodes count, whether the 3 SD\n    are over the segments of a subject or of a day, and in which unit (microvolts or volts) the\n    0 dB is set. The same choice sets the event set of every claim that uses reading (b).\n    This attempt runs two readings with a Welch estimate (1 s windows) in microvolts squared\n    per Hz: (b1) the PSD averaged over good electrodes, a segment dropped when the mean over\n    1-200 Hz is below 0 dB or the mean over 115-125 Hz is more than 3 SD above the subject's\n    segments; (b2) the same per good electrode, a segment dropped when any good electrode\n    fails.\n  passage: >-\n    \"... computing the power spectral density for each segment and discarding segments with\n    power <0 dB or with abnormally high power at 115-125 Hz (>3 SDs) compared with all\n    segments.\" (Materials and Methods, ECoG-event synchronization). The paper's code at\n    04c6faf starts from the curated Figshare epochs and does not hold this step.\n  why: >-\n    In volts every segment is below 0 dB and all events would be dropped; per electrode, more\n    segments fail than on the mean. The event counts of fig2-event-counts are within tolerance\n    with the false positives alone removed, so a rule that drops many segments moves them out\n    of tolerance, and the drop changes the events of every reading-(b) claim.\n"
}
```

```
File created successfully at: questions/000055.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u
```

```
Fri Oct 23 16:00:47 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && python - <<'EOF'
s=open('ajile.py').read()
start=s.index('def welch_db(x):')
end=s.index('# band layout in res')
new='''def welch_means(x):
    """Welch PSD per channel with 1 s windows (a standard choice; the Methods name no
    estimator), in microvolt^2/Hz. Returns the linear mean over 1-200 Hz and over 115-125 Hz
    per channel."""
    from scipy.signal import welch
    fr, p = welch(x, fs=FS, nperseg=int(FS), axis=1)
    return p[:, (fr >= 1) & (fr <= 200)].mean(1), p[:, (fr >= 115) & (fr <= 125)].mean(1)


def _band_idx(band):
    return np.where((FREQS >= band[0]) & (FREQS <= band[1]))[0]


# Morlet power is computed on -1.8 to +1.8 s of each 10 s segment. Every wavelet here has the
# same support, +-5 sigma = +-0.2 s (sigma = n_cycles / (2 pi f) = 1 / (8 pi) s), so the bins
# kept (-1.5 to 1.5 s) are the same as on the full segment; -1.8 s keeps the decimation grid of
# the full segment (bins at -5 + k * 0.1 s).
SUB = 1.8


def segment_measures(x, proj=None):
    """Measures of one 10 s segment x (channels, samples), microvolts."""
    wa, wh = welch_means(x)
    half = x.shape[1] // 2
    k = int(SUB * FS)
    p, t = morlet_power(x[:, half - k:half + k + 1])
    t = t + SEG_HALF - SUB                       # time relative to onset
    bmask = (t >= BASE[0] - 1e-9) & (t <= BASE[1] + 1e-9)
    pb = p - p[:, :, bmask].mean(2, keepdims=True)
    wmask = (t >= WIN[0] - 1e-9) & (t <= WIN[1] + 1e-9)
    lf, hf = _band_idx(LFB), _band_idx(HFB)
    band = np.empty((x.shape[0], 8), np.float32)
    for j, src in enumerate((pb, p)):
        for bi, idx in enumerate((lf, hf)):
            sub = src[:, idx][:, :, wmask]
            band[:, j * 4 + bi * 2 + 0] = sub.mean((1, 2))
            band[:, j * 4 + bi * 2 + 1] = np.median(np.median(sub, 2), 1)
    kmask = (t >= KEEP[0] - 1e-9) & (t <= KEEP[1] + 1e-9)
    roi = None if proj is None else np.einsum("cr,cft->rft", proj, pb[:, :, kmask])
    return wa, wh, band, roi, t[kmask]


def extract_file(asset_id, onsets, proj=None):
    """Spectral measures for the events of one file, reading each chunk row of the ECoG once.

    onsets: event times in s. proj: (channels, regions) weights or None.
    Returns a dict, one row per event:
      'ok': whether the full 10 s segment is inside the recording;
      'psd_all', 'psd_hf': (events, channels) Welch mean PSD over 1-200 and 115-125 Hz;
      'band': (events, channels, 8), columns BAND_COLS;
      'roi': (events, regions, freqs, bins) baseline-subtracted region power (if proj);
      'tbins': time of the kept bins; 'seconds': wall time."""
    t_start = time.time()
    f = open_nwb(asset_id)
    d = f["acquisition/ElectricalSeries/data"]
    n, nch = d.shape
    cs = d.chunks[0]
    half = int(SEG_HALF * FS)
    onsets = np.asarray(onsets, float)
    ne = len(onsets)
    res = {"ok": np.zeros(ne, bool), "psd_all": np.full((ne, nch), np.nan, np.float32),
           "psd_hf": np.full((ne, nch), np.nan, np.float32),
           "band": np.full((ne, nch, 8), np.nan, np.float32), "roi": None, "tbins": None}
    cache = {}
    for i in np.argsort(onsets):
        c = int(round(onsets[i] * FS))
        a, b = c - half, c + half
        if a < 0 or b > n:
            continue
        c0, c1 = a // cs, (b - 1) // cs
        for k in list(cache):
            if k < c0:
                del cache[k]
        for k in range(c0, c1 + 1):
            if k not in cache:
                for attempt in range(4):
                    try:
                        cache[k] = d[k * cs:min((k + 1) * cs, n), :]
                        break
                    except Exception:
                        if attempt == 3:
                            raise
                        time.sleep(5)
        blk = np.concatenate([cache[k] for k in range(c0, c1 + 1)], axis=0)
        x = np.nan_to_num(blk[a - c0 * cs:b - c0 * cs, :].T.astype(np.float64))
        wa, wh, band, roi, tb = segment_measures(x, proj)
        res["psd_all"][i], res["psd_hf"][i], res["band"][i] = wa, wh, band
        if roi is not None:
            if res["roi"] is None:
                res["roi"] = np.full((ne,) + roi.shape, np.nan, np.float32)
            res["roi"][i] = roi
        res["tbins"] = tb
        res["ok"][i] = True
    f.close()
    res["seconds"] = time.time() - t_start
    return res


def _extract_job(args):
    import os
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    key, asset_id, onsets, proj = args
    return key, extract_file(asset_id, onsets, proj)


def extract_many(jobs, workers=12):
    """jobs: list of (key, asset_id, onsets, proj). Runs files in parallel processes, the
    largest first. Returns {key: result}."""
    from concurrent.futures import ProcessPoolExecutor
    jobs = sorted(jobs, key=lambda j: -len(j[2]))
    out = {}
    with ProcessPoolExecutor(workers) as ex:
        for key, r in ex.map(_extract_job, jobs):
            out[key] = r
    return out


'''
s=s[:start]+new+s[end:]
# remove old extract_file (the first one) and old _band_idx
i=s.index('def _band_idx(band):\n    return np.where((FREQS >= band[0]) & (FREQS <= band[1]))[0]\n\n\ndef extract_file(asset_id, onsets, proj=None, log=None):')
j=s.index('# band layout in res')
s=s[:i]+s[j:]
open('ajile.py','w').write(s)
EOF
grep -n "^def \|^SUB\|^# band" ajile.py
```

```
Traceback (most recent call last):
  File "<stdin>", line 124, in <module>
ValueError: substring not found
52:def assets():
67:def s3_url(asset_id):
72:def open_nwb(asset_id, cache_mb=0):
80:def _s(x):
84:def read_meta(asset_id):
125:def wrist_traces(asset_id, onsets, side, t=(-1.5, 1.5)):
154:def figshare_files(article):
159:def roi_matrices():
171:def parse_roi(txt):
176:def epoch_metadata(name, files):
213:def _wavelets():
223:def morlet_power(x):
238:def welch_db(x):
249:def _band_idx(band):
253:def extract_file(asset_id, onsets, proj=None, log=None):
323:# band layout in res['band'][..., k]
328:def fold_angle(a):
```

**Agent calls Bash**

```bash
python - <<'EOF'
import re
src=open('/dev/stdin').read() if False else None
EOF
python - <<'EOF'
s=open('ajile.py').read()
exec_src=open('/proc/self/fd/0').read() if False else None
EOF
echo ok
```

```
ok
```

**Agent calls Read**

```json
{
 "file_path": "entries/000055-peterson-2021/ajile.py",
 "offset": 236,
 "limit": 20
}
```

```
236	
237	
238	def welch_db(x):
239	    """Welch PSD per channel with 1 s windows (standard choice), in dB of microvolt^2/Hz.
240	    Returns (mean dB over 1-200 Hz per channel, mean dB over 115-125 Hz per channel)."""
241	    from scipy.signal import welch
242	    fr, p = welch(x, fs=FS, nperseg=int(FS), axis=1)
243	    db = 10 * np.log10(np.maximum(p, 1e-30))
244	    a = db[:, (fr >= 1) & (fr <= 200)].mean(1)
245	    b = db[:, (fr >= 115) & (fr <= 125)].mean(1)
246	    return a, b
247	
248	
249	def _band_idx(band):
250	    return np.where((FREQS >= band[0]) & (FREQS <= band[1]))[0]
251	
252	
253	def extract_file(asset_id, onsets, proj=None, log=None):
254	    """Spectral measures for the events of one file.
255
```

**Agent**

I'll rewrite the file section in full with the Write tool for clarity.

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('ajile.py').read()
i=s.index('def welch_db(x):'); j=s.index('# band layout in res')
open('ajile.py','w').write(s[:i]+'#SPECTRAL#\n\n\n'+s[j:])
EOF
grep -n "#SPECTRAL#" ajile.py
```

```
238:#SPECTRAL#
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000055-peterson-2021/ajile.py",
 "old_string": "#SPECTRAL#\n",
 "new_string": "def welch_means(x):\n    \"\"\"Welch PSD per channel with 1 s windows (a standard choice; the Methods name no\n    estimator), in microvolt^2/Hz. Returns the linear mean over 1-200 Hz and over 115-125 Hz\n    per channel.\"\"\"\n    from scipy.signal import welch\n    fr, p = welch(x, fs=FS, nperseg=int(FS), axis=1)\n    return p[:, (fr >= 1) & (fr <= 200)].mean(1), p[:, (fr >= 115) & (fr <= 125)].mean(1)\n\n\ndef _band_idx(band):\n    return np.where((FREQS >= band[0]) & (FREQS <= band[1]))[0]\n\n\n# Morlet power is computed on -1.8 to +1.8 s of each 10 s segment. Every wavelet here has the\n# same support, +-5 sigma = +-0.2 s (sigma = n_cycles / (2 pi f) = 1 / (8 pi) s), so the bins\n# kept (-1.5 to 1.5 s) are the same as on the full segment; -1.8 s keeps the decimation grid of\n# the full segment (bins at -5 + k * 0.1 s).\nSUB = 1.8\n\n\ndef segment_measures(x, proj=None):\n    \"\"\"Measures of one 10 s segment x (channels, samples), microvolts.\"\"\"\n    wa, wh = welch_means(x)\n    half = x.shape[1] // 2\n    k = int(SUB * FS)\n    p, t = morlet_power(x[:, half - k:half + k + 1])\n    t = t + SEG_HALF - SUB                       # time relative to onset\n    bmask = (t >= BASE[0] - 1e-9) & (t <= BASE[1] + 1e-9)\n    pb = p - p[:, :, bmask].mean(2, keepdims=True)\n    wmask = (t >= WIN[0] - 1e-9) & (t <= WIN[1] + 1e-9)\n    lf, hf = _band_idx(LFB), _band_idx(HFB)\n    band = np.empty((x.shape[0], 8), np.float32)\n    for j, src in enumerate((pb, p)):\n        for bi, idx in enumerate((lf, hf)):\n            sub = src[:, idx][:, :, wmask]\n            band[:, j * 4 + bi * 2 + 0] = sub.mean((1, 2))\n            band[:, j * 4 + bi * 2 + 1] = np.median(np.median(sub, 2), 1)\n    kmask = (t >= KEEP[0] - 1e-9) & (t <= KEEP[1] + 1e-9)\n    roi = None if proj is None else np.einsum(\"cr,cft->rft\", proj, pb[:, :, kmask])\n    return wa, wh, band, roi, t[kmask]\n\n\ndef extract_file(asset_id, onsets, proj=None):\n    \"\"\"Spectral measures for the events of one file, reading each chunk row of the ECoG once.\n\n    onsets: event times in s. proj: (channels, regions) weights or None.\n    Returns a dict, one row per event:\n      'ok': whether the full 10 s segment is inside the recording;\n      'psd_all', 'psd_hf': (events, channels) Welch mean PSD over 1-200 and 115-125 Hz;\n      'band': (events, channels, 8), columns BAND_COLS;\n      'roi': (events, regions, freqs, bins) baseline-subtracted region power (if proj);\n      'tbins': time of the kept bins; 'seconds': wall time.\"\"\"\n    t_start = time.time()\n    f = open_nwb(asset_id)\n    d = f[\"acquisition/ElectricalSeries/data\"]\n    n, nch = d.shape\n    cs = d.chunks[0]\n    half = int(SEG_HALF * FS)\n    onsets = np.asarray(onsets, float)\n    ne = len(onsets)\n    res = {\"ok\": np.zeros(ne, bool), \"psd_all\": np.full((ne, nch), np.nan, np.float32),\n           \"psd_hf\": np.full((ne, nch), np.nan, np.float32),\n           \"band\": np.full((ne, nch, 8), np.nan, np.float32), \"roi\": None, \"tbins\": None}\n    cache = {}\n    for i in np.argsort(onsets):\n        c = int(round(onsets[i] * FS))\n        a, b = c - half, c + half\n        if a < 0 or b > n:\n            continue\n        c0, c1 = a // cs, (b - 1) // cs\n        for k in list(cache):\n            if k < c0:\n                del cache[k]\n        for k in range(c0, c1 + 1):\n            if k not in cache:\n                for attempt in range(4):\n                    try:\n                        cache[k] = d[k * cs:min((k + 1) * cs, n), :]\n                        break\n                    except Exception:\n                        if attempt == 3:\n                            raise\n                        time.sleep(5)\n        blk = np.concatenate([cache[k] for k in range(c0, c1 + 1)], axis=0)\n        x = np.nan_to_num(blk[a - c0 * cs:b - c0 * cs, :].T.astype(np.float64))\n        wa, wh, band, roi, tb = segment_measures(x, proj)\n        res[\"psd_all\"][i], res[\"psd_hf\"][i], res[\"band\"][i] = wa, wh, band\n        if roi is not None:\n            if res[\"roi\"] is None:\n                res[\"roi\"] = np.full((ne,) + roi.shape, np.nan, np.float32)\n            res[\"roi\"][i] = roi\n        res[\"tbins\"] = tb\n        res[\"ok\"][i] = True\n    f.close()\n    res[\"seconds\"] = time.time() - t_start\n    return res\n\n\ndef _extract_job(args):\n    key, asset_id, onsets, proj = args\n    return key, extract_file(asset_id, onsets, proj)\n\n\ndef extract_many(jobs, workers=12):\n    \"\"\"jobs: list of (key, asset_id, onsets, proj). Runs files in parallel processes, the\n    largest first. Returns {key: result}.\"\"\"\n    from concurrent.futures import ProcessPoolExecutor\n    jobs = sorted(jobs, key=lambda j: -len(j[2]))\n    out = {}\n    with ProcessPoolExecutor(workers) as ex:\n        for key, r in ex.map(_extract_job, jobs):\n            out[key] = r\n    return out\n"
}
```

```
The file entries/000055-peterson-2021/ajile.py has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t4.py <<'EOF'
import sys, time; sys.path.insert(0,'entries/000055-peterson-2021')
import ajile, numpy as np
x=np.random.default_rng(0).normal(size=(4,5000))*30
p,t=ajile.morlet_power(x); 
wa,wh,band,roi,tb=ajile.segment_measures(x)
# compare kept bins with full-segment
full_t=t; m=(full_t>=-1.5-1e-9)&(full_t<=1.5+1e-9)
k=int(1.8*500); half=2500
p2,t2=ajile.morlet_power(x[:,half-k:half+k+1]); t2=t2+5-1.8
m2=(t2>=-1.5-1e-9)&(t2<=1.5+1e-9)
print(np.abs(p[:,:,m]-p2[:,:,m2]).max(), full_t[m][:3], t2[m2][:3], m.sum(), m2.sum())
import mne
from mne.time_frequency import tfr_array_morlet
q=tfr_array_morlet(x[None], 500., ajile.FREQS, n_cycles=ajile.FREQS/4., output='power', decim=50, verbose=False)[0]
print(np.abs(10*np.log10(q)-p).max())
EOF
python t4.py
```

```
0.0 [-1.5 -1.4 -1.3] [-1.5 -1.4 -1.3] 31 31
41.772997588761186
Shell cwd was reset to
```

**Agent**

The sub-segment matches the full segment exactly. My power differs from MNE's `tfr_array_morlet` by up to 42 dB, so checking whether that is an edge effect or a constant offset:

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat >> t4.py <<'EOF'
d=10*np.log10(q)-p
print(np.round(d[0,:,45:55].mean(1),3)); print(np.round(d[0,5,:8],2), np.round(d[0,5,-8:],2))
EOF
python t4.py 2>&1 | tail -3
```

```
0.000e+00 -0.000e+00  0.000e+00  0.000e+00 -0.000e+00 -0.000e+00
  0.000e+00]
[ 0. -0.  0. -0. -0. -0.  0. -0.] [-0.  0.  0. -0. -0. -0.  0.  0.]
Shell cwd was reset to
```

**Agent**

The difference is only at the segment edges; the kept bins match MNE exactly. Adding the projection helpers, then running a development extraction on S04 and S09 (628 events):

**Agent calls Bash**

```bash
cat >> entries/000055-peterson-2021/ajile.py <<'EOF'


# ---------------------------------------------------------------- regions

REGIONS = ["Frontal_Mid", "Precentral", "Postcentral", "Parietal_Inf", "SupraMarginal",
           "Temporal_Sup", "Temporal_Mid", "Temporal_Inf"]
REGION_NAMES = {"Frontal_Mid": "middle frontal", "Precentral": "precentral",
                "Postcentral": "postcentral", "Parietal_Inf": "inferior parietal",
                "SupraMarginal": "supramarginal", "Temporal_Sup": "superior temporal",
                "Temporal_Mid": "middle temporal", "Temporal_Inf": "inferior temporal"}


def roi_tables(txt):
    """Parse a projection file: the density row (Series over regions) and the electrode
    weights (DataFrame, electrodes x regions), left-side columns with the '_L' dropped."""
    df = pd.read_csv(io.StringIO(txt))
    df = df[[c for c in df.columns if c.endswith("_L")]]
    df.columns = [c[:-2] for c in df.columns]
    return df.iloc[0], df.iloc[1:].reset_index(drop=True)


def projection(weights, good, regions=REGIONS):
    """Weights (electrodes x regions) with bad electrodes set to 0 and each region's column
    renormalised to sum to 1 (claims file, from the code). Rows beyond the file's channels
    are dropped by the caller."""
    w = weights[regions].to_numpy(float).copy()
    w[~np.asarray(good, bool)] = 0
    s = w.sum(0, keepdims=True)
    s[s == 0] = np.nan
    return w / s
EOF
cd $TMPDIR && . dev/bin/activate && cat > dev1.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'entries/000055-peterson-2021')
import ajile, numpy as np
A,md,meta=pickle.load(open('cache.pkl','rb')); txt=pickle.load(open('roi.pkl','rb'))
jobs=[]
for _,a in A[A.subject.isin([4,9])].iterrows():
    m=meta[a.path]; nch=m['ecog_shape'][1]
    dens,W=ajile.roi_tables(txt[a.subject]); W=W.iloc[:nch]
    P=ajile.projection(W, m['electrodes'].good.values)
    jobs.append(((a.subject,a.day), a.asset_id, m['reaches'].start_time.values, np.nan_to_num(P)))
t=time.time(); out=ajile.extract_many(jobs, workers=10); print('wall', time.time()-t, sum(len(j[2]) for j in jobs))
print({k:round(v['seconds']) for k,v in out.items()})
pickle.dump(out, open('dev_ext.pkl','wb'))
EOF
OMP_NUM_THREADS=1 python dev1.py
```

```
wall 196.57198238372803 628
{(4, 7): 113, (9, 5): 196, (4, 4): 81, (4, 6): 67, (4, 5): 51, (9, 6): 43, (4, 3): 14, (9, 7): 33, (9, 4): 22, (9, 3): 26}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pickle, numpy as np
A,md,meta=pickle.load(open('cache.pkl','rb')); out=pickle.load(open('dev_ext.pkl','rb'))
for s in [4,9]:
    ks=[k for k in out if k[0]==s]
    allm=[];hf=[];perch=[];perchhf=[]
    for k in sorted(ks):
        p=[p for p in meta if p.startswith(f'sub-{s:02d}/sub-{s:02d}_ses-{k[1]}')][0]
        g=meta[p]['electrodes'].good.values
        r=out[k]; allm+=list(10*np.log10(r['psd_all'][:,g].mean(1))); hf+=list(10*np.log10(r['psd_hf'][:,g].mean(1)))
        perch+=list((10*np.log10(r['psd_all'][:,g])).min(1))
    allm=np.array(allm); hf=np.array(hf); perch=np.array(perch)
    print(s, len(allm), 'mean-dB min', allm.min().round(2), (allm<0).sum(), 'hf>3sd', (hf>hf.mean()+3*hf.std()).sum(), 'perch<0', (perch<0).sum(), np.percentile(allm,[1,50,99]).round(1))
r=out[(4,7)]; print(r['roi'].shape, r['tbins'], np.nanmean(r['roi'][:,1],0)[:, 15:20].mean(1).round(2))
print(np.nanmean(r['band'][:,:,:],axis=(0,1)).round(2))
"
```

```
4 417 mean-dB min nan 0 hf>3sd 0 perch<0 274 [nan nan nan]
9 211 mean-dB min 5.57 0 hf>3sd 1 perch<0 211 [ 5.7 10.7 15.7]
(159, 8, 25, 31) [-1.50000000e+00 -1.40000000e+00 -1.30000000e+00 -1.20000000e+00
 -1.10000000e+00 -1.00000000e+00 -9.00000000e-01 -8.00000000e-01
 -7.00000000e-01 -6.00000000e-01 -5.00000000e-01 -4.00000000e-01
 -3.00000000e-01 -2.00000000e-01 -1.00000000e-01 -2.22044605e-16
  1.00000000e-01  2.00000000e-01  3.00000000e-01  4.00000000e-01
  5.00000000e-01  6.00000000e-01  7.00000000e-01  8.00000000e-01
  9.00000000e-01  1.00000000e+00  1.10000000e+00  1.20000000e+00
  1.30000000e+00  1.40000000e+00  1.50000000e+00] [-0.24 -0.73 -1.1  -0.77 -0.49 -0.47 -0.43 -0.49 -0.45 -0.4  -0.32 -0.22
 -0.11  0.04  0.08  0.02 -0.03  0.02 -0.02  0.05 -0.03 -0.05 -0.08 -0.07
 -0.07]
[-0.67 -0.   -0.32  0.33 29.19 29.71 14.43 15.18]
Shell cwd was reset to
```

**Agent**

Per-electrode reading (b2) drops every S09 segment, since some good electrodes always have a mean PSD below 0 dB. Reading (b1) drops 0 or 1. Checking why S04 has NaN rows:

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pickle, numpy as np
A,md,meta=pickle.load(open('cache.pkl','rb')); out=pickle.load(open('dev_ext.pkl','rb'))
for k,r in sorted(out.items()):
    p=[p for p in meta if p.startswith(f'sub-{k[0]:02d}/sub-{k[0]:02d}_ses-{k[1]}')][0]
    g=meta[p]['electrodes'].good.values
    bad=~np.isfinite(10*np.log10(r['psd_all'][:,g].mean(1)))
    print(k, (~r['ok']).sum(), bad.sum(), (r['psd_all'][:,g]==0).any(1).sum() if True else '', np.isnan(r['psd_all'][:, g]).all(0).sum())
"
```

```
(4, 3) 22 22 0 0
(4, 4) 0 0 0 0
(4, 5) 0 0 0 0
(4, 6) 0 0 0 0
(4, 7) 0 0 0 0
(9, 3) 0 0 0 0
(9, 4) 0 0 0 0
(9, 5) 0 0 0 0
(9, 6) 0 0 0 0
(9, 7) 0 0 0 0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pickle, numpy as np
A,md,meta=pickle.load(open('cache.pkl','rb'))
m=meta['sub-04/sub-04_ses-3_behavior+ecephys.nwb']; st=m['reaches'].start_time.values
print(m['ecog_shape'][0]/500, m['pose_shape'][0]/30, st.min(), st.max(), (st>m['ecog_shape'][0]/500).sum(), m['session_start'])
f=md['subj_04_day_3_l_epo.fif']; print(f.false_pos.values[st*500+2500>m['ecog_shape'][0]].sum())
for p,m in meta.items():
    st=m['reaches'].start_time.values; n=m['ecog_shape'][0]/500
    k=((st-5<0)|(st+5>n)).sum()
    if k: print(p, k, n, m['pose_shape'][0]/30, st.max())
"
```

```
56351.678 86400.0 49319.452000000005 86318.42 22 2000-01-03T03:20:48.322000-05:00
7
sub-01/sub-01_ses-7_behavior+ecephys.nwb 132 55717.586 86400.0 85786.776
sub-04/sub-04_ses-3_behavior+ecephys.nwb 22 56351.678 86400.0 86318.42
sub-06/sub-06_ses-3_behavior+ecephys.nwb 83 57159.434 86400.0 79624.103
sub-08/sub-08_ses-4_behavior+ecephys.nwb 1 86400.0 86400.0 86440.332
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t5.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'entries/000055-peterson-2021')
import ajile, numpy as np, pandas as pd
A,md,meta=pickle.load(open('cache.pkl','rb'))
for p in ['sub-06/sub-06_ses-3_behavior+ecephys.nwb','sub-01/sub-01_ses-7_behavior+ecephys.nwb']:
    m=meta[p]; a=A[A.path==p].asset_id.iloc[0]
    st=m['reaches'].start_time.values; n=m['ecog_shape'][0]/500
    ss=pd.Timestamp(m['session_start']).tz_convert('UTC'); off=ss.hour*3600+ss.minute*60+ss.second+ss.microsecond/1e6
    print(p, 'offset', off, 'n+off', n+off, 'min st', st.min(), 'events before offset', (st<off).sum())
    f=ajile.open_nwb(a); w=f['processing/behavior/Position/R_Wrist/data']
    x=w[::3000,0]; tt=np.arange(len(x))*100
    print(' pose nan before off', np.isnan(x[tt<off]).mean(), 'after', np.isnan(x[tt>=off]).mean())
    g=m['electrodes'].good.values
    sel=st[(st>off+10)&(st-off+10<n)][:30]
    for name, on in (('stored', sel), ('shifted', sel-off)):
        on=on[(on>5)&(on<n-5)]
        r=ajile.extract_file(a, on)
        b=r['band'][:, g]
        print(' ', name, len(on), 'LFB', np.nanmean(b[:,:,0]).round(3), 'HFB', np.nanmean(b[:,:,2]).round(3), 'per-event LFB<0 frac', (np.nanmean(b[:,:,0],1)<0).mean().round(2))
EOF
OMP_NUM_THREADS=1 python t5.py
```

```
sub-06/sub-06_ses-3_behavior+ecephys.nwb offset 29240.566 n+off 86400.0 min st 29754.283 events before offset 0
 pose nan before off 0.017064846416382253 after 0.010507880910683012
  stored 30 LFB 0.261 HFB 0.185 per-event LFB<0 frac 0.43
  shifted 30 LFB -0.41 HFB 0.504 per-event LFB<0 frac 0.67
sub-01/sub-01_ses-7_behavior+ecephys.nwb offset 30682.414 n+off 86400.0 min st 32313.385 events before offset 0
 pose nan before off 1.0 after 0.02872531418312388
  stored 30 LFB -0.067 HFB -0.101 per-event LFB<0 frac 0.53
  shifted 30 LFB -0.568 HFB -0.068 per-event LFB<0 frac 0.57
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd entries/000055-peterson-2021 && python - <<'EOF'
s=open('ajile.py').read()
old_start=s.index('def segment_measures(x, proj=None):')
old_end=s.index('def extract_file(asset_id, onsets, proj=None):')
new='''CTRL = -3.0                    # pseudo-onset of the clock check (a standard choice)


def segment_measures(x, proj=None):
    """Measures of one 10 s segment x (channels, samples), microvolts."""
    wa, wh = welch_means(x)
    half = x.shape[1] // 2
    k0, k1 = int((SUB - CTRL) * FS), int(SUB * FS)
    p, t = morlet_power(x[:, half - k0:half + k1 + 1])
    t = t - (SUB - CTRL)                         # time relative to onset
    lf, hf = _band_idx(LFB), _band_idx(HFB)

    def win(lo, hi):
        return (t >= lo - 1e-9) & (t <= hi + 1e-9)
    pb = p - p[:, :, win(*BASE)].mean(2, keepdims=True)
    wmask = win(*WIN)
    band = np.empty((x.shape[0], 8), np.float32)
    for j, src in enumerate((pb, p)):
        for bi, idx in enumerate((lf, hf)):
            sub = src[:, idx][:, :, wmask]
            band[:, j * 4 + bi * 2 + 0] = sub.mean((1, 2))
            band[:, j * 4 + bi * 2 + 1] = np.median(np.median(sub, 2), 1)
    # clock check: the same band means around a pseudo-onset at CTRL s, with its own baseline
    pc = p - p[:, :, win(CTRL + BASE[0], CTRL + BASE[1])].mean(2, keepdims=True)
    cm = win(CTRL + WIN[0], CTRL + WIN[1])
    ctrl = np.stack([pc[:, lf][:, :, cm].mean((1, 2)), pc[:, hf][:, :, cm].mean((1, 2))], 1)
    kmask = win(*KEEP)
    roi = None if proj is None else np.einsum("cr,cft->rft", proj, pb[:, :, kmask])
    return wa, wh, band, ctrl.astype(np.float32), roi, t[kmask]


'''
s=s[:old_start]+new+s[old_end:]
s=s.replace('''           "band": np.full((ne, nch, 8), np.nan, np.float32), "roi": None, "tbins": None}''','''           "band": np.full((ne, nch, 8), np.nan, np.float32),
           "ctrl": np.full((ne, nch, 2), np.nan, np.float32), "roi": None, "tbins": None}''')
s=s.replace('''        wa, wh, band, roi, tb = segment_measures(x, proj)
        res["psd_all"][i], res["psd_hf"][i], res["band"][i] = wa, wh, band''','''        wa, wh, band, ctrl, roi, tb = segment_measures(x, proj)
        res["psd_all"][i], res["psd_hf"][i], res["band"][i] = wa, wh, band
        res["ctrl"][i] = ctrl''')
s=s.replace("""      'band': (events, channels, 8), columns BAND_COLS;""","""      'band': (events, channels, 8), columns BAND_COLS;
      'ctrl': (events, channels, 2), LFB and HFB means around the pseudo-onset CTRL;""")
open('ajile.py','w').write(s)
EOF
grep -n "SUB = \|SUB\b" ajile.py | head
```

```
Fri Oct 23 16:08:12 UTC 2026
255:SUB = 1.8
265:    k0, k1 = int((SUB - CTRL) * FS), int(SUB * FS)
267:    t = t - (SUB - CTRL)                         # time relative to onset
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('ajile.py').read()
s=s.replace("    t = t - (SUB - CTRL)                         # time relative to onset","    t = t + SEG_HALF - (SUB - CTRL)              # time relative to onset")
s=s.replace("""# Morlet power is computed on -1.8 to +1.8 s of each 10 s segment. Every wavelet here has the
# same support, +-5 sigma = +-0.2 s (sigma = n_cycles / (2 pi f) = 1 / (8 pi) s), so the bins
# kept (-1.5 to 1.5 s) are the same as on the full segment; -1.8 s keeps the decimation grid of
# the full segment (bins at -5 + k * 0.1 s).""","""# Morlet power is computed on -4.8 to +1.8 s of each 10 s segment. Every wavelet here has the
# same support, +-5 sigma = +-0.2 s (sigma = n_cycles / (2 pi f) = 1 / (8 pi) s), so every bin
# used (-4.5 to 1.5 s) is the same as on the full segment; -4.8 s keeps the decimation grid of
# the full segment (bins at -5 + k * 0.1 s).""")
open('ajile.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys; sys.path.insert(0,'entries/000055-peterson-2021')
import ajile, numpy as np
x=np.random.default_rng(0).normal(size=(4,5000))*30
p,t=ajile.morlet_power(x)
wa,wh,band,ctrl,roi,tb=ajile.segment_measures(x, np.ones((4,2))/4)
m=(t>=-1.5-1e-9)&(t<=1.5+1e-9); pb=p-p[:,:,(t>=-1.5-1e-9)&(t<=-1+1e-9)].mean(2,keepdims=True)
print(tb[:3], tb[-1], np.abs(roi[0]-pb[:,:,m].mean(0)).max())
EOF
```

```
[-1.5 -1.4 -1.3] 1.5 4.76837158203125e-07
Shell cwd was reset to
```

**Agent**

The ROI projection checks out against a direct computation. Now writing the regression functions:

**Agent calls Bash**

```bash
cat >> entries/000055-peterson-2021/ajile.py <<'EOF'


# ---------------------------------------------------------------- regression (Figure 6)
# Every choice below is the claims file's (opening comment, "Regression method"): ten features,
# day and time of day one-hot (0-8, 8-16, 16-24 h), the others z-scored, reach duration and
# magnitude log transformed, missing bimanual ratios 0.5; forward selection by OLS adjusted R2
# on all of the subject's events, unselected features set to 0; sklearn HuberRegressor with
# its defaults; 200 random splits with equal numbers of test events from each day; Delta R2 by
# shuffling a feature (all its one-hot columns together) in the training events and scoring on
# the unshuffled test events (Methods), and on shuffled test events (code, variant).

FEATURES = ["day", "time_of_day", "reach_duration", "reach_magnitude", "reach_angle",
            "onset_speed", "speech_ratio", "bimanual_ratio", "bimanual_overlap", "bimanual_class"]


def design(ev):
    """ev: the subject's events with columns day, hour, duration, magnitude, angle_folded,
    onset_speed, speech_ratio, bimanual_ratio, bimanual_overlap, bimanual_class.
    Returns X (events, columns) and groups (feature name per column)."""
    cols, groups = [], []
    for d in sorted(ev.day.unique()):
        cols.append((ev.day == d).astype(float).to_numpy())
        groups.append("day")
    tod = np.digitize(ev.hour.to_numpy(), [8, 16])
    for b in range(3):
        cols.append((tod == b).astype(float))
        groups.append("time_of_day")
    cont = {"reach_duration": np.log(ev.duration.to_numpy()),
            "reach_magnitude": np.log(ev.magnitude.to_numpy()),
            "reach_angle": ev.angle_folded.to_numpy(),
            "onset_speed": ev.onset_speed.to_numpy(),
            "speech_ratio": ev.speech_ratio.to_numpy(),
            "bimanual_ratio": np.nan_to_num(ev.bimanual_ratio.to_numpy(), nan=0.5),
            "bimanual_overlap": ev.bimanual_overlap.to_numpy(),
            "bimanual_class": ev.bimanual_class.to_numpy()}
    for k, v in cont.items():
        sd = v.std()
        cols.append((v - v.mean()) / sd if sd > 0 else v * 0)
        groups.append(k)
    return np.column_stack(cols), np.array(groups)


def _adj_r2(X, y):
    A = np.column_stack([np.ones(len(y)), X]) if X.shape[1] else np.ones((len(y), 1))
    beta, *_ = np.linalg.lstsq(A, y, rcond=None)
    res = y - A @ beta
    r2 = 1 - (res @ res) / ((y - y.mean()) @ (y - y.mean()))
    n, p = len(y), A.shape[1] - 1
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)


def forward_select(X, groups, y):
    """Greedy forward selection of features (column groups) by OLS adjusted R2."""
    chosen, best = [], -np.inf
    remaining = list(dict.fromkeys(groups))
    while remaining:
        scores = {}
        for g in remaining:
            m = np.isin(groups, chosen + [g])
            scores[g] = _adj_r2(X[:, m], y)
        g = max(scores, key=scores.get)
        if scores[g] <= best:
            break
        best = scores[g]
        chosen.append(g)
        remaining.remove(g)
    return chosen


def day_balanced_splits(days, n_splits, test_frac, rng):
    """Index arrays (train, test) with equal numbers of test events from each day."""
    days = np.asarray(days)
    ud = np.unique(days)
    per = max(1, int(round(test_frac * len(days))) // len(ud))
    per = min(per, min((days == d).sum() for d in ud) - 1)
    out = []
    for _ in range(n_splits):
        test = np.concatenate([rng.choice(np.where(days == d)[0], per, replace=False) for d in ud])
        mask = np.ones(len(days), bool)
        mask[test] = False
        out.append((np.where(mask)[0], test))
    return out


def fit_model(X, groups, y, days, seed, n_splits=200, test_frac=0.1):
    """One electrode and band. Returns dict with the selected features, the split-averaged
    test R2, Delta R2 per feature (Methods and code versions) and coefficients per column."""
    from sklearn.linear_model import HuberRegressor
    from sklearn.metrics import r2_score
    rng = np.random.default_rng(seed)
    ok = np.isfinite(y)
    X, y, days = X[ok], y[ok], np.asarray(days)[ok]
    sel = forward_select(X, groups, y)
    Xs = X * np.isin(groups, sel)[None, :]
    feats = list(dict.fromkeys(groups))
    r2s, coefs = [], []
    d_m = {g: [] for g in feats}
    d_c = {g: [] for g in feats}
    for tr, te in day_balanced_splits(days, n_splits, test_frac, rng):
        h = HuberRegressor().fit(Xs[tr], y[tr])
        r2 = r2_score(y[te], h.predict(Xs[te]))
        r2s.append(r2)
        coefs.append(h.coef_)
        for g in feats:
            if g not in sel:
                d_m[g].append(0.0)
                d_c[g].append(0.0)
                continue
            m = groups == g
            Xtr = Xs[tr].copy()
            Xtr[:, m] = Xtr[rng.permutation(len(tr))][:, m]
            hs = HuberRegressor().fit(Xtr, y[tr])
            d_m[g].append(r2 - r2_score(y[te], hs.predict(Xs[te])))
            Xte = Xs[te].copy()
            Xte[:, m] = Xte[rng.permutation(len(te))][:, m]
            d_c[g].append(r2 - r2_score(y[te], hs.predict(Xte)))
    return {"selected": sel, "r2": float(np.mean(r2s)),
            "delta_methods": {g: float(np.mean(v)) for g, v in d_m.items()},
            "delta_code": {g: float(np.mean(v)) for g, v in d_c.items()},
            "coef": np.mean(coefs, 0), "n": int(ok.sum())}


def _fit_job(args):
    key, X, groups, y, days, seed, kw = args
    return key, fit_model(X, groups, y, days, seed, **kw)


def fit_many(jobs, workers=4):
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        return dict(ex.map(_fit_job, jobs, chunksize=4))
EOF
date -u
```

```
Fri Oct 23 16:08:52 UTC 2026
```

**Agent**

Now a helper that assembles the event table (DANDI features, linked Figshare flags, time of day, ECoG clock offset), then timing the regression on the dev subjects:

**Agent calls Bash**

```bash
cat >> entries/000055-peterson-2021/ajile.py <<'EOF'


# ---------------------------------------------------------------- events

def clock_offset(session_start):
    """Seconds from midnight to the session start, read on the UTC clock of the stored time
    (the notebook shows the sleep labels fall at night on this reading)."""
    ss = pd.Timestamp(session_start).tz_convert("UTC")
    return ss.hour * 3600 + ss.minute * 60 + ss.second + ss.microsecond / 1e6


def events_table(A, meta, figmeta):
    """One row per DANDI event, with its features, the linked Figshare record and its
    false-positive flag. A: assets(); meta: {path: read_meta()}; figmeta: {fif name: DataFrame}."""
    rows = []
    for _, a in A.iterrows():
        m = meta[a.path]
        r = m["reaches"].copy()
        r["subject"], r["day"], r["path"], r["asset_id"] = a.subject, a.day, a.path, a.asset_id
        r["side"] = m["reach_side"]
        off = clock_offset(m["session_start"])
        r["offset"] = off
        r["hour"] = ((r.start_time) / 3600.0) % 24       # events count from midnight (see notebook)
        r["duration"] = r.stop_time - r.start_time
        r["magnitude"] = r.Reach_magnitude_px
        r["angle_folded"] = fold_angle(r.Reach_angle_degrees)
        r["onset_speed"] = r.Onset_speed_px_per_sec
        r["speech_ratio"] = r.Speech_ratio
        r["bimanual_ratio"] = r.Bimanual_ratio
        r["bimanual_overlap"] = r.Bimanual_overlap
        r["bimanual_class"] = r.Bimanual_class
        r["ev_index"] = np.arange(len(r))
        name = [k for k in figmeta if k.startswith(f"subj_{a.subject:02d}_day_{a.day}_")]
        if len(name) == 1:
            fm = figmeta[name[0]].copy()
            fm["key_ms"] = fm.event_timestamp.astype(np.int64)
            r["key_ms"] = np.round(r.start_time * 1000).astype(np.int64)
            fm = fm.drop_duplicates("key_ms")
            r = r.merge(fm.drop(columns=[c for c in fm.columns if c.endswith(("_x", "_y"))]),
                        on="key_ms", how="left", suffixes=("", "_fig"))
            r["fig_file"] = name[0]
        rows.append(r)
    return pd.concat(rows, ignore_index=True)
EOF
cd $TMPDIR && . dev/bin/activate && cat > t6.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'entries/000055-peterson-2021')
import ajile, numpy as np, pandas as pd
A,md,meta=pickle.load(open('cache.pkl','rb')); out=pickle.load(open('dev_ext.pkl','rb'))
ev=ajile.events_table(A,meta,md)
print(ev.false_pos.isna().sum(), ev.groupby('subject').false_pos.apply(lambda x:(x==0).sum()).to_dict())
print(ev[['hour','offset']].describe())
# magnitude etc vs fig
print(np.abs(ev.magnitude-ev.reach_r).max(), np.abs(ev.Reach_angle_degrees-ev.reach_a).max(), np.abs(ev.duration*30-ev.reach_duration).max(), np.abs(ev.onset_speed/30-ev.onset_velocity).max(), np.abs(ev.bimanual_overlap*30-ev.other_reach_overlap).max(), (ev.bimanual_class!=ev.bimanual).sum(), (ev.bimanual_class!=ev.other_lead_lag.notna()).sum(), np.nanmax(np.abs(ev.bimanual_ratio-ev.I_over_C_ratio)), ev.bimanual_ratio[ev.I_over_C_ratio.isna()].describe(), np.abs(ev.speech_ratio-ev.audio_ratio).max())
s=9; e=ev[(ev.subject==s)&(ev.false_pos==0)]
X,g=ajile.design(e)
band=np.concatenate([out[(s,d)]['band'][ev[(ev.subject==s)&(ev.day==d)].false_pos.values==0] for d in sorted(e.day.unique())])
y=band[:,10,0]
t=time.time(); r=ajile.fit_model(X,g,y,e.day.values,0); print(time.time()-t, r['selected'], r['r2'])
EOF
OMP_NUM_THREADS=1 python t6.py
```

```
0 {1: 659, 2: 209, 3: 584, 4: 268, 5: 203, 6: 869, 7: 675, 8: 850, 9: 151, 10: 620, 11: 896, 12: 947}
              hour        offset
count  8088.000000   8088.000000
mean     13.961208   1450.950035
std       5.507189   6439.779383
min       0.011203      0.000000
25%       9.889675      0.000000
50%      14.464523      0.000000
75%      18.480132      0.000000
max      23.996123  30682.414000
5.000001124244591e-08 4.9900023668669746e-08 1.0186340659856796e-08 1.6233336452842195e-08 1.0000007932831068e-08 0 0 5.00000152392488e-10 count    26.0
mean      0.5
std       0.0
min       0.5
25%       0.5
50%       0.5
75%       0.5
max       0.5
Name: bimanual_ratio, dtype: float64 5.000000413701855e-10
1.1324975490570068 [np.str_('speech_ratio')] -0.09273046988835883
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && python - <<'EOF'
s=open('ajile.py').read()
old=s[s.index('    sel = forward_select(X, groups, y)\n'):s.index('    return {"selected": sel, "r2": float(np.mean(r2s)),')]
new='''    sel = forward_select(X, groups, y)
    # Unselected features are set to 0 (code); a zero column gets a zero coefficient under
    # Huber's L2 penalty and does not change the fit, so the fit uses the selected columns.
    keep = np.isin(groups, sel)
    if not keep.any():
        keep = np.zeros(len(groups), bool)
    Xs = X[:, keep] if keep.any() else np.zeros((len(y), 1))
    gs = groups[keep] if keep.any() else np.array(["none"])
    feats = list(dict.fromkeys(groups))
    r2s, coefs = [], []
    d_m = {g: [] for g in feats}
    d_c = {g: [] for g in feats}
    for tr, te in day_balanced_splits(days, n_splits, test_frac, rng):
        h = HuberRegressor().fit(Xs[tr], y[tr])
        r2 = r2_score(y[te], h.predict(Xs[te]))
        r2s.append(r2)
        c = np.zeros(len(groups))
        if keep.any():
            c[keep] = h.coef_
        coefs.append(c)
        for g in feats:
            if g not in sel:
                d_m[g].append(0.0)
                d_c[g].append(0.0)
                continue
            m = gs == g
            Xtr = Xs[tr].copy()
            Xtr[:, m] = Xtr[rng.permutation(len(tr))][:, m]
            hs = HuberRegressor().fit(Xtr, y[tr])
            d_m[g].append(r2 - r2_score(y[te], hs.predict(Xs[te])))
            Xte = Xs[te].copy()
            Xte[:, m] = Xte[rng.permutation(len(te))][:, m]
            d_c[g].append(r2 - r2_score(y[te], hs.predict(Xte)))
'''
s=s.replace(old,new)
open('ajile.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cat > t7.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'entries/000055-peterson-2021')
import ajile, numpy as np, pandas as pd
A,md,meta=pickle.load(open('cache.pkl','rb')); out=pickle.load(open('dev_ext.pkl','rb'))
ev=ajile.events_table(A,meta,md)
for s in [9,4]:
    e=ev[(ev.subject==s)&(ev.false_pos==0)]
    X,g=ajile.design(e)
    band=np.concatenate([out[(s,d)]['band'][ev[(ev.subject==s)&(ev.day==d)].false_pos.values==0] for d in sorted(e.day.unique())])
    t=time.time(); ns=[]
    for ch in range(0,band.shape[1],12):
        for b in (0,2):
            y=band[:,ch,b]; 
            if not np.isfinite(y).sum()>50: continue
            r=ajile.fit_model(X,g,y,e.day.values,0); ns.append(len(r['selected']))
    print(s, (time.time()-t)/len(ns), np.mean(ns), r['r2'])
EOF
OMP_NUM_THREADS=1 python t7.py
```

```
9 1.501250982284546 3.5 -0.1501589908761379
4 1.2299841472080775 3.0 -0.04342827958758886
Shell cwd was reset to
```

**Agent**

About 1.3 s per regression model, so roughly 13 min for all good electrodes in both bands on 4 cores. Checking how `tools/entry.py` enforces the notebook time limit:

**Agent calls Bash**

```bash
grep -n -i "timeout\|30\b\|minutes\|runtime" tools/entry.py | head -30
```

```
28:that takes longer than --max-minutes fails, even if it ran without error.
301:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
323:             f"--ExecutePreprocessor.timeout={timeout}", f"--ExecutePreprocessor.kernel_name={kernel}",
330:        if ok and seconds > max_minutes * 60:
332:            error = f"took {seconds / 60:.0f} minutes; the limit is {max_minutes:.0f}"
390:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
391:    parser.add_argument("--max-minutes", type=float, default=30,
411:    return run(entry_dir, output_dir, args.timeout, args.max_minutes)
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && python -c "
import pickle
A,md,meta=pickle.load(open('cache.pkl','rb'))
g={}
for p,m in meta.items(): g.update({(p[:6],k):v for k,v in m['groups'].items()})
for k,v in sorted(g.items()): print(k,v)
" | sort -u -k2 | head -80
```

```
Fri Oct 23 16:11:21 UTC 2026
('sub-10', 'AHD') anterior hippocampal depth
('sub-10', 'AID') anterior insular depth
('sub-01', 'ECG') electrocardiogram
('sub-01', 'EOG') electrooculogram
('sub-01', 'GRID') ECoG grid
('sub-09', 'Grid') ECoG grid
('sub-06', 'L Grid') Left ECoG grid
('sub-03', 'LAD') left anterior depth
('sub-01', 'LAT') left anterior temporal
('sub-11', 'LATD') left anterior temporal depth
('sub-09', 'LF') left frontal
('sub-01', 'LID') left insular depth
('sub-01', 'LMT') left medial temporal
('sub-11', 'LMTD') left medial temporal depth
('sub-06', 'LO') left occipital
('sub-10', 'LOF') left orbitofrontal
('sub-03', 'LPD') left posterior depth
('sub-01', 'LPT') left posterior temporal
('sub-01', 'LTO') left temporal occipital
[... 20 more lines not kept]
```

**Agent**

Depth groups are named "depth" in their descriptions. By that rule 7 subjects have depth electrodes, where the paper says 5; I'll report it. Writing notebook 1:

**Agent calls Write**

```json
{
 "file_path": "entries/000055-peterson-2021/build_nb.py",
 "content": "\"\"\"Builds the notebooks of this entry from cell sources (run once; the notebooks are committed).\"\"\"\nimport nbformat as nbf\n\nCELLS = []\n\n\ndef md(s):\n    CELLS.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tag=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tag:\n        c.metadata[\"tags\"] = [tag] if isinstance(tag, str) else list(tag)\n    CELLS.append(c)\n\n\ndef save(path):\n    nb = nbf.v4.new_notebook()\n    nb.cells = list(CELLS)\n    nb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\n    nbf.write(nb, path)\n    CELLS.clear()\n\n\nimport nb1_cells  # noqa: E402,F401  (fills CELLS for notebook 1)\nsave(\"reproduce_peterson_2021.ipynb\")\nimport nb2_cells  # noqa: E402,F401\nsave(\"reproduce_peterson_2021_regression.ipynb\")\n"
}
```

```
File created successfully at: entries/000055-peterson-2021/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent**

I'll keep the build tooling out of the entry: notebooks written as percent-format scripts in $TMPDIR, which I can also run directly as scripts on the subset, then converted.

**Agent calls Bash**

```bash
rm entries/000055-peterson-2021/build_nb.py; mkdir -p $TMPDIR/build; cat > $TMPDIR/build/conv.py <<'EOF'
"""Convert a percent-format script into a notebook. '# %% [markdown]' starts a markdown cell
(lines prefixed '# '), '# %%' a code cell, '# %% tags=a,b' a tagged code cell."""
import sys, nbformat as nbf
src, dst = sys.argv[1], sys.argv[2]
cells, cur, kind, tags = [], [], None, []
def flush():
    if kind is None: return
    text = "\n".join(cur).strip("\n")
    if kind == "md":
        text = "\n".join(l[2:] if l.startswith("# ") else l.lstrip("#") for l in text.splitlines())
        cells.append(nbf.v4.new_markdown_cell(text))
    else:
        c = nbf.v4.new_code_cell(text)
        if tags: c.metadata["tags"] = tags
        cells.append(c)
for line in open(src).read().splitlines():
    if line.startswith("# %%"):
        flush(); cur = []
        rest = line[4:].strip()
        if rest.startswith("[markdown]"): kind, tags = "md", []
        else:
            kind = "code"
            tags = rest[5:].split(",") if rest.startswith("tags=") else []
        continue
    cur.append(line)
flush()
nb = nbf.v4.new_notebook(); nb.cells = cells
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbf.write(nb, dst)
EOF
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build/nb1.py",
 "content": "# %% [markdown]\n# # Peterson et al. (2021), eNeuro: behaviour and spectral power, from dandiset 000055\n#\n# Paper: Peterson, Singh, Wang, Rao and Brunton (2021), \"Behavioral and Neural Variability of\n# Naturalistic Arm Movements\", eNeuro 8(3), doi:10.1523/ENEURO.0007-21.2021.\n#\n# Dataset: DANDI:000055 (AJILE12), version 0.220127.0436 (doi:10.48324/dandi.000055/0.220127.0436).\n# The paper cites no version of the dandiset. 0.220127.0436 is its only published version, and the\n# draft has the same 55 assets and the same size, so the published version is pinned.\n#\n# Claims: `claims/000055/10.1523-eneuro.0007-21.2021.yaml`, written from the version of record\n# (Europe PMC, PMC8225404), with the legends of the Extended Data figures; the figures themselves\n# were not available to the readers.\n#\n# Outside inputs, both from the paper's Figshare project and pinned by DOI:\n# the projection matrices from electrodes to AAL regions (10.6084/m9.figshare.12114408.v1), the\n# paper's own output of its projection step, used for every claim on regions; and the metadata of\n# the curated epoch files (10.6084/m9.figshare.12115728.v1), read for their false-positive flags\n# only (the ECoG in those files is not read). Two link claims, added by this attempt, test that both\n# match the dataset.\n#\n# This notebook tests the claims below. The regression claims of Figure 6 are in\n# `reproduce_peterson_2021_regression.ipynb`.\n#\n# | Claim | Here |\n# |---|---|\n# | figshare-event-link, figshare-roi-link (link claims of this attempt) | tested |\n# | subject-days, cohort, fig2-event-counts | tested |\n# | fig2-features-differ-across-subjects, fig2-reach-shape, fig2-bimanual-skew | tested |\n# | extfig2-1c-contralateral-larger, extfig2-2-feature-correlations, fig2-days-and-waking | tested |\n# | fig3-group-lfb-decrease-hfb-increase, fig3-sensorimotor-largest, fig3-lfb-more-widespread | tested |\n# | fig4-precentral-subject-variability | tested |\n# | fig5-band-power-differs-across-subjects, table1-subject-band-power-ci, fig5-recording-day-effects | tested |\n# | extfig5-1-baseline-reduces-day-variability, discussion-day-changes-small | tested |\n# | fig6b, fig6-r2, fig6c, extfig6-2, fig6d (two claims) | regression notebook |\n\n# %%\nimport os, time, io\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"OPENBLAS_NUM_THREADS\", \"1\")\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom concurrent.futures import ProcessPoolExecutor\nimport matplotlib\nimport matplotlib.pyplot as plt\nimport ajile\n\nT0 = time.time()\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\n# All 12 subjects; AJILE_SUBJECTS restricts them while developing.\nSUBJECTS = [int(s) for s in os.environ.get(\"AJILE_SUBJECTS\", \",\".join(map(str, range(1, 13)))).split(\",\")]\nA_all = ajile.assets()\nA = A_all[A_all.subject.isin(SUBJECTS)].reset_index(drop=True)\nwith ProcessPoolExecutor(8) as ex:\n    meta = dict(zip(A.path, ex.map(ajile.read_meta, A.asset_id)))\nfig_files = ajile.figshare_files(ajile.EPOCH_ARTICLE)\nfig_names = sorted(n for n in fig_files if int(n[5:7]) in SUBJECTS)\nwith ProcessPoolExecutor(8) as ex:\n    figmeta = dict(zip(fig_names, ex.map(ajile.epoch_metadata, fig_names, [fig_files] * len(fig_names))))\nroi_txt, roi_files = ajile.roi_matrices()\nprint(f\"{len(A_all)} assets in the version, {len(A)} read; {len(figmeta)} Figshare epoch files; \"\n      f\"loaded in {time.time() - T0:.0f} s\")\n\n# %% [markdown]\n# ## Data check\n\n# %% tags=sanity\nprint(\"Assets per subject and the days they hold (from the file names):\")\nprint(A_all.groupby(\"subject\").day.apply(lambda d: sorted(d)).to_string())\nprint(\"total assets\", len(A_all), \"; total size\", round(A_all[\"size\"].sum() / 1e9), \"GB\")\nrows = []\nfor _, a in A.iterrows():\n    m = meta[a.path]\n    el = m[\"electrodes\"]\n    rows.append(dict(subject=a.subject, day=a.day, subject_id=m[\"subject_attrs\"].get(\"subject_id\"),\n                     species=m[\"subject_attrs\"].get(\"species\"), side=m[\"reach_side\"],\n                     events=len(m[\"reaches\"]), reach_events_equal=bool(np.allclose(m[\"reach_events\"], m[\"reaches\"].start_time, atol=0.002)),\n                     channels=m[\"ecog_shape\"][1], good=int(el.good.sum()),\n                     ecog_hours=round(m[\"ecog_shape\"][0] / m[\"ecog_rate\"] / 3600, 3), ecog_rate=m[\"ecog_rate\"],\n                     ecog_unit=m[\"ecog_unit\"], conversion=m[\"ecog_conversion\"], chunks=m[\"ecog_chunks\"],\n                     pose_hours=round(m[\"pose_shape\"][0] / m[\"pose_rate\"] / 3600, 3), pose_rate=m[\"pose_rate\"],\n                     pose_unit=m[\"pose_unit\"], session_start=m[\"session_start\"],\n                     x_mean=round(el.x.mean(), 1)))\nfiles = pd.DataFrame(rows)\nprint(files.drop(columns=[\"chunks\"]).to_string())\nprint(\"subject attributes held:\", sorted({k for m in meta.values() for k in m[\"subject_attrs\"]}))\nprint(\"electrode table columns:\", list(meta[A.path[0]][\"electrodes\"].columns))\nprint(\"ECoG chunk shapes:\", sorted({str(c) for c in files.chunks}))\nprint(\"files whose ECoG is shorter than the pose:\")\nprint(files[files.ecog_hours < files.pose_hours - 0.01][[\"subject\", \"day\", \"ecog_hours\", \"pose_hours\", \"session_start\"]].to_string())\n\n# %% [markdown]\n# The ECoG is stored with `conversion` 1e-6 to volts, so the stored values are microvolts, and the\n# spectral power below is in dB of microvolts squared. The pose is labelled \"meters\" but holds image\n# pixels (values up to several hundred, and the reaches table gives magnitudes in pixels).\n#\n# Session start times are stored as 19:00 or 03:xx at offset -05:00. Read on the UTC clock they are\n# midnight, or the time a recording began on a day that started late. The next cell checks this\n# reading against the coarse behavioural labels: on the UTC reading sleep falls at night.\n\n# %% tags=sanity\npose_rng = []\nfor p in A.path[:3]:\n    f = ajile.open_nwb(A.set_index(\"path\").loc[p, \"asset_id\"])\n    d = f[\"processing/behavior/Position/R_Wrist/data\"][::3000, :]\n    pose_rng.append((p, np.nanmin(d), np.nanmax(d)))\n    f.close()\nprint(\"R_Wrist pose range, every 3000th frame, first three files:\", [(p.split(\"/\")[1][:12], round(a), round(b)) for p, a, b in pose_rng])\nsleep = []\nfor p, m in meta.items():\n    st = pd.Timestamp(m[\"session_start\"])\n    e = m[\"epochs\"]\n    s = e[e.label == \"Sleep/rest\"]\n    mid = (s.start + s.stop) / 2\n    for clock, t0 in ((\"UTC\", st.tz_convert(\"UTC\")), (\"stated offset\", st)):\n        h0 = t0.hour + t0.minute / 60 + t0.second / 3600\n        sleep += [(clock, (h0 + x / 3600) % 24, d) for x, d in zip(mid, s.stop - s.start)]\nsl = pd.DataFrame(sleep, columns=[\"clock\", \"hour\", \"dur\"])\ntab = sl.groupby([\"clock\", pd.cut(sl.hour, range(0, 25, 3))], observed=False).dur.sum().unstack(0) / 3600\nprint(\"Hours labelled Sleep/rest by clock hour, under the two readings of the session start:\")\nprint(tab.round(0).to_string())\nprint(\"epochs labels:\", pd.concat([m[\"epochs\"] for m in meta.values()]).label.value_counts().to_dict())\n\n# %% [markdown]\n# ### Link claims: the Figshare inputs against the dataset\n#\n# figshare-event-link. The Figshare epoch files hold one metadata row per event, with a timestamp\n# in milliseconds from the start of the file, the reach features in frames, and the paper's\n# false-positive flag. Records are matched on the timestamp. The link holds when every DANDI event\n# has exactly one Figshare record with the same timestamp, and the features both hold agree\n# (magnitude and angle as stored, duration, onset speed and overlap converted from frames at 30\n# frames/s, bimanual class, bimanual ratio, speech ratio).\n\n# %% tags=claim:figshare-event-link\nev = ajile.events_table(A, meta, figmeta)\nnd = len(ev)\nnf = sum(len(v) for v in figmeta.values())\nmatched = ev.false_pos.notna()\nprint(f\"DANDI events {nd}, Figshare records {nf}, DANDI events matched on timestamp {matched.sum()} ({matched.mean():.1%})\")\ndup = sum(v.event_timestamp.duplicated().sum() for v in figmeta.values())\nprint(\"duplicated timestamps within a Figshare file:\", dup)\nagree = {\n    \"magnitude (px)\": np.abs(ev.magnitude - ev.reach_r).max(),\n    \"angle (deg)\": np.abs(ev.Reach_angle_degrees - ev.reach_a).max(),\n    \"duration (s vs frames/30)\": np.abs(ev.duration - ev.reach_duration / 30).max(),\n    \"onset speed (px/s vs px/frame*30)\": np.abs(ev.onset_speed - ev.onset_velocity * 30).max(),\n    \"overlap (s vs frames/30)\": np.abs(ev.bimanual_overlap - ev.other_reach_overlap / 30).max(),\n    \"speech ratio\": np.abs(ev.speech_ratio - ev.audio_ratio).max(),\n    \"bimanual ratio (where Figshare has one)\": np.nanmax(np.abs(ev.bimanual_ratio - ev.I_over_C_ratio)),\n}\nfor k, v in agree.items():\n    print(f\"  largest difference, {k}: {v:.2e}\")\nprint(\"  bimanual class differs from Figshare 'bimanual':\", int((ev.bimanual_class != ev.bimanual).sum()),\n      \"; differs from 'other_lead_lag exists':\", int((ev.bimanual_class != ev.other_lead_lag.notna()).sum()))\nprint(\"  Figshare ratios missing:\", int(ev.I_over_C_ratio.isna().sum()), \"; DANDI values there:\",\n      ev.bimanual_ratio[ev.I_over_C_ratio.isna()].unique())\nprint(\"  Figshare day equals the DANDI file's day:\", bool((ev.day_fig == ev.day).all()) if \"day_fig\" in ev else None)\nprint(\"false positives per subject (Figshare flag):\")\nfp = ev.groupby(\"subject\").false_pos.agg(events=\"size\", false_pos=\"sum\")\nfp[\"kept\"] = fp.events - fp.false_pos\nprint(fp.astype(int).T.to_string())\nprint(f\"false positives overall: {int(ev.false_pos.sum())} of {nd} ({ev.false_pos.mean():.1%}); the dataset holds no flag for them\")\n\n# %% [markdown]\n# figshare-roi-link. Each projection file has a header of 116 AAL regions, a density row, and one\n# row of weights per electrode. The link holds when each subject's file has one row per channel of\n# the dataset in the same order. Rows carry no identifier, so the order is checked through\n# positions: for each electrode, the weighted mean of the region centroids that the Figshare\n# centroid file gives is compared with the electrode's MNI position from the dataset (mirrored to\n# the left), against the same distance with the rows of the file shuffled.\n\n# %% tags=claim:figshare-roi-link\nrng = np.random.default_rng(55)\ncent_txt = {s: ajile.requests.get(roi_files[f\"aal_{s:02d}_ROIcentroids_Lside.csv\"][\"download_url\"], timeout=60).text for s in SUBJECTS}\nroi_rows = []\nW_all, DENS = {}, {}\nfor s in SUBJECTS:\n    dens, W = ajile.roi_tables(roi_txt[s])\n    full = pd.read_csv(io.StringIO(roi_txt[s]))\n    cen = pd.read_csv(io.StringIO(cent_txt[s]))\n    cen.index = full.columns\n    cenL = cen.loc[[c for c in full.columns if c.endswith(\"_L\")]]\n    cenL.index = [c[:-2] for c in cenL.index]\n    p0 = A.path[A.subject == s].iloc[0]\n    el = meta[p0][\"electrodes\"]\n    nch = len(el)\n    extra = W.iloc[nch:]\n    Wn = W.iloc[:nch].to_numpy(float)\n    xyz = el[[\"x\", \"y\", \"z\"]].to_numpy(float).copy()\n    xyz[:, 0] = -np.abs(xyz[:, 0])\n    valid = cenL.abs().sum(1).to_numpy() > 0\n    C = cenL.to_numpy(float)\n\n    def dist(Wm):\n        w = Wm[:, valid] / Wm[:, valid].sum(1, keepdims=True)\n        return np.nanmedian(np.linalg.norm(w @ C[valid] - xyz, axis=1))\n    d_true = dist(Wn)\n    d_shuf = [dist(Wn[rng.permutation(nch)]) for _ in range(200)]\n    same_pos = all(np.allclose(meta[p][\"electrodes\"][[\"x\", \"y\", \"z\"]].to_numpy(), el[[\"x\", \"y\", \"z\"]].to_numpy())\n                   for p in A.path[A.subject == s])\n    roi_rows.append(dict(subject=s, channels=nch, rows=len(W), extra_rows=len(extra),\n                         extra_rows_all_zero=bool((extra.to_numpy() == 0).all()) if len(extra) else True,\n                         median_dist_mm=round(d_true, 1), shuffled_min=round(min(d_shuf), 1),\n                         shuffled_median=round(np.median(d_shuf), 1), positions_same_all_days=same_pos))\n    W_all[s] = W.iloc[:nch]\n    DENS[s] = dens\nroi_link = pd.DataFrame(roi_rows)\nprint(roi_link.to_string(index=False))\ndens_mean = pd.DataFrame(DENS).T.mean()\nsel_regions = dens_mean[dens_mean > 3].sort_values(ascending=False)\nprint(\"regions with electrode density averaged over subjects above 3:\", sel_regions.round(2).to_dict())\nprint(\"the claims file's eight regions:\", ajile.REGIONS, \"; same set:\", set(sel_regions.index) == set(ajile.REGIONS))\n\n# %% [markdown]\n# ### Clock of the ECoG\n#\n# In three files the ECoG is 15.5 to 15.9 h long while the pose and the event times span 24 h, and\n# some events lie after the end of the ECoG. In each of them the ECoG length plus the session start\n# (on the UTC clock) is 24 h. This fits an ECoG that starts at the session start while the events and\n# the pose count from midnight. Below, events of those files are read both ways: the stored clock\n# (ECoG time = event time) and the shifted one (ECoG time = event time minus the session start). The\n# movement response (LFB decrease and HFB increase over 0 to 0.5 s against -1.5 to -1 s, averaged\n# over good electrodes with the precentral projection weights) decides which clock holds.\n\n# %%\nproj = {}\nfor _, a in A.iterrows():\n    el = meta[a.path][\"electrodes\"]\n    proj[a.path] = np.nan_to_num(ajile.projection(W_all[a.subject], el.good.to_numpy()))\nshort = files[files.ecog_hours < files.pose_hours - 0.01]\nshort_paths = [A.path[(A.subject == r.subject) & (A.day == r.day)].iloc[0] for r in short.itertuples()]\ncjobs = []\nfor p in short_paths:\n    e = ev[ev.path == p]\n    n = meta[p][\"ecog_shape\"][0] / ajile.FS\n    off = e.offset.iloc[0]\n    on = e.start_time.to_numpy()\n    ok = (on - off > 6) & (on < n - 6) & (on > 6)        # inside the ECoG on both clocks\n    cjobs.append(((p, \"stored\"), e.asset_id.iloc[0], on[ok][:40], proj[p]))\n    cjobs.append(((p, \"shifted\"), e.asset_id.iloc[0], on[ok][:40] - off, proj[p]))\nt = time.time()\ncres = ajile.extract_many(cjobs, workers=6)\npre = ajile.REGIONS.index(\"Precentral\")\nfor p in short_paths:\n    for clock in (\"stored\", \"shifted\"):\n        r = cres[(p, clock)]\n        w = proj[p][:, pre]\n        lfb = r[\"band\"][:, :, 0] @ w\n        hfb = r[\"band\"][:, :, 2] @ w\n        print(f\"{p.split('/')[1][:12]} {clock:8s} n={len(lfb)} precentral LFB {np.mean(lfb):+.2f} dB \"\n              f\"(Wilcoxon p={stats.wilcoxon(lfb).pvalue:.2g}), HFB {np.mean(hfb):+.2f} dB (p={stats.wilcoxon(hfb).pvalue:.2g})\")\n    e = ev[ev.path == p]\n    n = meta[p][\"ecog_shape\"][0] / ajile.FS\n    print(f\"   events outside the ECoG on the stored clock: {int(((e.start_time + 5) > n).sum())} of {len(e)}; \"\n          f\"on the shifted clock: {int(((e.start_time - e.offset - 5) < 0).sum() + ((e.start_time - e.offset + 5) > n).sum())}\")\nprint(f\"({time.time() - t:.0f} s)\")\n\n# %% [markdown]\n# The shifted clock is used for these three files from here on (ECoG time = event time minus the\n# session start on the UTC clock; for the other 52 files the session start is midnight and nothing\n# changes).\n#\n# ### Spectral measures for every event\n#\n# One pass over the ECoG of every event: Welch PSD means for the segment rejection, Morlet power\n# per electrode in the two bands, region spectrograms with the paper's projection weights (bad\n# electrodes of the file set to 0, each region renormalised), and the clock check of the next cell.\n\n# %%\njobs = []\nfor p in A.path:\n    e = ev[ev.path == p]\n    jobs.append((p, e.asset_id.iloc[0], (e.start_time - e.offset).to_numpy(), proj[p]))\nt = time.time()\nspec = ajile.extract_many(jobs, workers=12)\nprint(f\"spectral pass over {sum(len(j[2]) for j in jobs)} events in {len(jobs)} files: {time.time() - t:.0f} s \"\n      f\"(slowest file {max(r['seconds'] for r in spec.values()):.0f} s)\")\nTB = next(iter(spec.values()))[\"tbins\"]\nF = ajile.FREQS\nev[\"ok\"] = np.concatenate([spec[p][\"ok\"] for p in A.path])\nprint(\"events whose 10 s segment is outside the ECoG:\", int((~ev.ok).sum()))\n\n# %% [markdown]\n# Clock check for every file: per event, the precentral-weighted LFB and HFB change over 0 to 0.5 s\n# after onset against -1.5 to -1 s, and the same measure around a pseudo-onset 3 s before the\n# event (window -3 to -2.5 s against -4.5 to -4 s). A shared clock shows a stronger LFB decrease\n# and HFB increase at the true onset; the per-file test is a Wilcoxon signed-rank test of the\n# per-event differences (true minus pseudo-onset).\n\n# %% tags=sanity\nrows = []\nfor p in A.path:\n    r = spec[p]\n    w = proj[p][:, pre]\n    ok = r[\"ok\"]\n    l, h = r[\"band\"][ok, :, 0] @ w, r[\"band\"][ok, :, 2] @ w\n    lc, hc = r[\"ctrl\"][ok, :, 0] @ w, r[\"ctrl\"][ok, :, 1] @ w\n    sub = ev[ev.path == p]\n    rows.append(dict(subject=sub.subject.iloc[0], day=sub.day.iloc[0], n=int(ok.sum()),\n                     lfb_onset=l.mean(), lfb_pseudo=lc.mean(), p_lfb=stats.wilcoxon(l - lc).pvalue,\n                     hfb_onset=h.mean(), hfb_pseudo=hc.mean(), p_hfb=stats.wilcoxon(h - hc).pvalue))\nclock = pd.DataFrame(rows)\nclock[\"contrast\"] = (clock.lfb_onset < clock.lfb_pseudo) & (clock.p_lfb < 0.05) | (clock.hfb_onset > clock.hfb_pseudo) & (clock.p_hfb < 0.05)\nprint(clock.round(3).to_string(index=False))\nprint(f\"files where the onset differs from the pseudo-onset in the expected direction (p<0.05 in LFB or HFB): \"\n      f\"{int(clock.contrast.sum())} of {len(clock)}\")\nprint(\"files where it could not be established:\", clock[~clock.contrast][[\"subject\", \"day\"]].values.tolist())\n\n# %% [markdown]\n# ### Event sets\n#\n# (a) every event in the dataset; (b) after dropping the Figshare false positives and the segments\n# rejected on their power spectral density. How that PSD is computed is not in the claims file\n# (question in `questions/000055.yaml`); two readings are run with a Welch estimate in microvolts\n# squared per Hz. (b1): on the PSD averaged over good electrodes, drop a segment whose mean over\n# 1-200 Hz is below 0 dB or whose mean over 115-125 Hz is more than 3 SD above the subject's\n# segments. (b2): the same on each good electrode, dropping a segment when any good electrode\n# fails. The false positives alone are also shown.\n\n# %% tags=sanity\npa, ph, pa_ch, ph_ch = [], [], [], []\nfor p in A.path:\n    g = meta[p][\"electrodes\"].good.to_numpy()\n    r = spec[p]\n    pa.append(10 * np.log10(r[\"psd_all\"][:, g].mean(1)))\n    ph.append(10 * np.log10(r[\"psd_hf\"][:, g].mean(1)))\n    pa_ch.append(np.nanmin(10 * np.log10(r[\"psd_all\"][:, g]), 1))\n    hf = 10 * np.log10(r[\"psd_hf\"][:, g])\n    pa_ch[-1] = (pa_ch[-1], hf)\nev[\"psd_db\"] = np.concatenate(pa)\nev[\"hf_db\"] = np.concatenate(ph)\nev[\"min_ch_db\"] = np.concatenate([x[0] for x in pa_ch])\nrej1 = np.zeros(len(ev), bool)\nrej2 = np.zeros(len(ev), bool)\nfor s in SUBJECTS:\n    m = (ev.subject == s).to_numpy() & ev.ok.to_numpy()\n    hf = ev.hf_db[m]\n    rej1[m] = (ev.psd_db[m] < 0).to_numpy() | (hf > hf.mean() + 3 * hf.std()).to_numpy()\n    # per electrode: an electrode's 115-125 Hz power more than 3 SD above its segments\n    idx = np.where(ev.subject == s)[0]\n    hfc = np.concatenate([x[1] if x[1].shape[1] == pa_ch[A.path.tolist().index(A.path[(A.subject == s)].iloc[0])][1].shape[1] else np.full((len(x[1]), pa_ch[A.path.tolist().index(A.path[(A.subject == s)].iloc[0])][1].shape[1]), np.nan) for x, pth in zip(pa_ch, A.path) if pth in set(A.path[A.subject == s])])\n    mu, sd = np.nanmean(hfc[ev.ok.to_numpy()[idx]], 0), np.nanstd(hfc[ev.ok.to_numpy()[idx]], 0)\n    rej2[idx] = (ev.min_ch_db.to_numpy()[idx] < 0) | np.any(hfc > mu + 3 * sd, axis=1)\nev[\"rej_b1\"] = rej1 & ev.ok\nev[\"rej_b2\"] = rej2 & ev.ok\nev[\"set_a\"] = True\nev[\"set_fp\"] = ev.false_pos == 0\nev[\"set_b1\"] = ev.set_fp & ev.ok & ~ev.rej_b1\nev[\"set_b2\"] = ev.set_fp & ev.ok & ~ev.rej_b2\nprint(\"PSD averaged over good electrodes, dB (uV^2/Hz), 1-200 Hz: range\", ev.psd_db.min().round(1), \"to\", ev.psd_db.max().round(1))\nprint(ev.groupby(\"subject\")[[\"set_a\", \"set_fp\", \"set_b1\", \"set_b2\", \"rej_b1\", \"rej_b2\"]].sum().T.to_string())\n\n# %% [markdown]\n# ## Claims on subjects, days and electrodes\n#\n# > subject-days (link): The dataset's subjects and recording days are the paper's subjects S01 to\n# > S12 and the recording days the paper lists for each.\n\n# %% tags=claim:subject-days\ntable2 = {1: [3, 4, 5, 7], 2: [3, 4, 5, 6], 3: [3, 4, 5, 6], 5: [3, 4, 7]}\ntable2.update({s: [3, 4, 5, 6, 7] for s in [4, 6, 7, 8, 9, 10, 11, 12]})\nhave = A_all.groupby(\"subject\").day.apply(lambda d: sorted(d)).to_dict()\nfor s in range(1, 13):\n    print(f\"S{s:02d} paper {table2[s]} dataset {have.get(s)} {'same' if have.get(s) == table2[s] else 'DIFFERENT'}\")\nprint(\"subject-days in the dataset:\", len(A_all), \"; in Table 2:\", sum(len(v) for v in table2.values()))\nprint(\"subject ids inside the files equal the file names:\", all(int(meta[p][\"subject_attrs\"][\"subject_id\"]) == s for p, s in zip(A.path, A.subject)))\nprint(\"Figshare file names (subject, day) equal the DANDI ones:\",\n      sorted((int(n[5:7]), int(n.split(\"_day_\")[1][0])) for n in figmeta) == sorted(zip(A.subject, A.day)))\n\n# %% [markdown]\n# > cohort: Twelve subjects (8 male, 4 female, 29.4 +- 7.9 years) had on average 87.0 +- 12.9\n# > surface electrodes; five also had 23.2 +- 12.1 depth electrodes; five were implanted in the\n# > right hemisphere and seven in the left.\n#\n# Surface electrodes are those of groups whose description does not say \"depth\"; depth electrodes\n# those whose description does. The hemisphere is the side of the mean electrode x coordinate and,\n# separately, the side of the reaching wrist (the contralateral one).\n\n# %% tags=claim:cohort\ncrow = []\nfor s in SUBJECTS:\n    p0 = A.path[A.subject == s].iloc[0]\n    m = meta[p0]\n    el = m[\"electrodes\"]\n    desc = el.group_name.map(m[\"groups\"])\n    depth = desc.str.contains(\"depth\", case=False)\n    crow.append(dict(subject=s, channels=len(el), surface=int((~depth).sum()), depth=int(depth.sum()),\n                     depth_groups=\",\".join(sorted(el.group_name[depth].unique())),\n                     hemisphere_x=\"right\" if el.x.mean() > 0 else \"left\",\n                     wrist=m[\"reach_side\"], sex=m[\"subject_attrs\"].get(\"sex\"), age=m[\"subject_attrs\"].get(\"age\")))\ncoh = pd.DataFrame(crow)\nprint(coh.to_string(index=False))\nprint(\"subjects:\", len(coh))\nprint(f\"mean surface electrodes per subject: {coh.surface.mean():.1f} (SD {coh.surface.std():.1f})\")\ndd = coh[coh.depth > 0]\nprint(f\"subjects with depth electrodes: {len(dd)}; mean depth electrodes among them {dd.depth.mean():.1f} (SD {dd.depth.std():.1f})\")\nprint(\"right hemisphere by x:\", int((coh.hemisphere_x == 'right').sum()), \"; by left-wrist events:\", int((coh.wrist == 'l_wrist').sum()))\nprint(\"sex and age in the files:\", coh.sex.unique(), coh.age.unique(), \"(not held: not testable)\")\n\n# %% [markdown]\n# > fig2-event-counts: Each subject contributed between 151 and 947 movement events (median 640\n# > across subjects).\n\n# %% tags=claim:fig2-event-counts\ncnt = ev.groupby(\"subject\")[[\"set_a\", \"set_fp\", \"set_b1\", \"set_b2\"]].sum()\nprint(cnt.T.to_string())\nexp = [(151, 15.1), (947, 94.7), (640, 64)]\nfor c in cnt.columns:\n    v = [cnt[c].min(), cnt[c].max(), cnt[c].median()]\n    ok = [abs(x - e) <= tol for x, (e, tol) in zip(v, exp)]\n    print(f\"reading {c}: fewest {v[0]}, most {v[1]}, median {v[2]}; within tolerance {ok} -> {'all three' if all(ok) else 'no'}\")\n\n# %% [markdown]\n# ## Behaviour (Figure 2 and Extended Data Figures 2-1 and 2-2)\n#\n# > fig2-features-differ-across-subjects: All ten behavioural and environmental features differ\n# > significantly across subjects.\n#\n# Features as the paper gives them: day of recording (as a number), time of day (hour of the\n# day), reach duration (s), reach magnitude (px), reach angle (folded to -90 to 90 degrees), onset\n# speed (px/s), speech ratio, bimanual ratio (missing values are 0.5 in the dataset), bimanual\n# overlap (s) and bimanual class.\n\n# %% tags=claim:fig2-features-differ-across-subjects\nFEAT = {\"day\": \"day\", \"time of day (h)\": \"hour\", \"reach duration (s)\": \"duration\", \"reach magnitude (px)\": \"magnitude\",\n        \"reach angle (deg)\": \"angle_folded\", \"onset speed (px/s)\": \"onset_speed\", \"speech ratio\": \"speech_ratio\",\n        \"bimanual ratio\": \"bimanual_ratio\", \"bimanual overlap (s)\": \"bimanual_overlap\", \"bimanual class\": \"bimanual_class\"}\nkw = []\nfor setname in (\"set_b1\", \"set_a\", \"set_b2\"):\n    e = ev[ev[setname]]\n    for k, c in FEAT.items():\n        h, p = stats.kruskal(*[g[c].to_numpy() for _, g in e.groupby(\"subject\")])\n        kw.append(dict(events=setname, feature=k, H=h, p=p))\nkw = pd.DataFrame(kw)\nprint(kw.pivot(index=\"feature\", columns=\"events\", values=\"p\").to_string(float_format=lambda x: f\"{x:.2e}\"))\nfor s in (\"set_b1\", \"set_a\", \"set_b2\"):\n    print(s, \": features with p < 0.001:\", int((kw[kw.events == s].p < 0.001).sum()), \"of 10\")\nprint(\"feature ranges (reading b1):\")\nprint(ev[ev.set_b1][list(FEAT.values())].describe().T[[\"min\", \"50%\", \"max\"]].round(3).to_string())\n\n# %% [markdown]\n# > fig2-reach-shape: Reach duration and reach magnitude vary little across subjects, with most\n# > reaches lasting under 2 s and covering under 200 pixels, and reach angle distributions tend to\n# > be bimodal with peaks near +90 and -90 degrees, with few side-to-side reaches.\n#\n# The kernel density uses scipy's Gaussian kernel with Scott's bandwidth (the seaborn default the\n# claims file names), evaluated at 1 degree steps on -90 to 90. A local maximum is a grid point\n# higher than its neighbours; an end point of the grid counts when it is higher than its one\n# neighbour (a standard choice: a peak at the edge of the folded range is a peak at +-90).\n\n# %% tags=claim:fig2-reach-shape\ngrid = np.arange(-90, 91, 1.0)\n\n\ndef angle_modes(a):\n    k = stats.gaussian_kde(a, bw_method=\"scott\")(grid)\n    pk = [i for i in range(len(grid)) if (i == 0 or k[i] > k[i - 1]) and (i == len(grid) - 1 or k[i] > k[i + 1])]\n    top = sorted(pk, key=lambda i: -k[i])[:2]\n    locs = sorted(grid[top])\n    bim = len(locs) == 2 and abs(locs[0] + 90) <= 15 and abs(locs[1] - 90) <= 15 and k[90] < min(k[top])\n    return locs, k[90], [k[i] for i in top], bim\n\n\ndef shape_table(e):\n    rows = []\n    for s, g in list(e.groupby(\"subject\")) + [(\"pooled\", e)]:\n        locs, k0, kt, bim = angle_modes(g.angle_folded.to_numpy())\n        rows.append(dict(subject=s, n=len(g), frac_dur_lt2=(g.duration < 2).mean(), med_dur=g.duration.median(),\n                         frac_mag_lt200=(g.magnitude < 200).mean(), med_mag=g.magnitude.median(),\n                         peaks=locs, dens0=k0, peak_dens=np.round(kt, 5), bimodal_pm90=bim,\n                         frac_side=(g.angle_folded.abs() < 30).mean()))\n    return pd.DataFrame(rows)\n\n\nfor setname in (\"set_b1\", \"set_a\"):\n    t = shape_table(ev[ev[setname]])\n    print(f\"events {setname}\")\n    print(t.round(3).to_string(index=False))\n    subj = t[t.subject != \"pooled\"]\n    pooled = t[t.subject == \"pooled\"].iloc[0]\n    dur_ok = (subj.frac_dur_lt2 > 0.5).sum()\n    mag_ok = (subj.frac_mag_lt200 > 0.5).sum()\n    print(f\"  duration part: pooled {pooled.frac_dur_lt2:.3f}, subjects with >half under 2 s {dur_ok} of {len(subj)}\")\n    print(f\"  magnitude part: pooled {pooled.frac_mag_lt200:.3f}, subjects with >half under 200 px {mag_ok} of {len(subj)}\")\n    print(f\"  angle part: pooled bimodal at +-90 {pooled.bimodal_pm90}; subjects {int(subj.bimodal_pm90.sum())} of {len(subj)}\")\n\n# %% [markdown]\n# > fig2-bimanual-skew: Bimanual ratio and bimanual overlap are skewed toward unimanual movement of\n# > the contralateral arm, less so for subjects 02, 04 and 05, while the bimanual class is mostly\n# > bimanual.\n\n# %% tags=claim:fig2-bimanual-skew\nfor setname in (\"set_b1\", \"set_a\"):\n    e = ev[ev[setname]]\n    rows = []\n    for s, g in list(e.groupby(\"subject\")) + [(\"pooled\", e)]:\n        rows.append(dict(subject=s, med_ratio=g.bimanual_ratio.median(), skew_overlap=stats.skew(g.bimanual_overlap),\n                         frac_bimanual=g.bimanual_class.mean()))\n    t = pd.DataFrame(rows)\n    subj = t[t.subject != \"pooled\"].copy()\n    pooled = t[t.subject == \"pooled\"].iloc[0]\n    top_ratio = set(subj.nlargest(5, \"med_ratio\").subject)\n    low_skew = set(subj.nsmallest(5, \"skew_overlap\").subject)\n    print(f\"events {setname}\")\n    print(t.round(3).to_string(index=False))\n    print(f\"  ratio part: pooled median {pooled.med_ratio:.3f}; subjects with median < 0.5: {int((subj.med_ratio < 0.5).sum())} of {len(subj)}\")\n    print(f\"  overlap part: pooled skewness {pooled.skew_overlap:.3f}; subjects with skewness > 0: {int((subj.skew_overlap > 0).sum())} of {len(subj)}\")\n    print(f\"  class part: pooled fraction bimanual {pooled.frac_bimanual:.3f}; subjects above half: {int((subj.frac_bimanual > 0.5).sum())} of {len(subj)}\")\n    print(f\"  five highest median ratios: {sorted(top_ratio)}; five lowest overlap skewness: {sorted(low_skew)}\")\n    print(f\"  S02, S04, S05 among the highest ratios: {[s in top_ratio for s in (2, 4, 5)]}; among the lowest skewness: {[s in low_skew for s in (2, 4, 5)]}\")\n\n# %% [markdown]\n# > extfig2-1c-contralateral-larger: Across all 12 subjects, the median displacement of the\n# > contralateral wrist after movement onset is substantially greater than that of the ipsilateral\n# > wrist.\n#\n# Wrist positions are read from the pose at 30 frames/s around each event (pose and events share\n# the midnight clock in every file, see the data check). Displacement is the Euclidean distance in\n# pixels from (a) the mean position over -1.5 to -1 s and (b) the position at onset; per subject,\n# the median over events at each frame, and its peak over 0 to 1.5 s.\n\n# %% tags=claim:extfig2-1c-contralateral-larger\ndef _wrist_job(args):\n    p, aid, on, side = args\n    return p, ajile.wrist_traces(aid, on, side)\n\n\nt = time.time()\nwjobs = [(p, ev.asset_id[ev.path == p].iloc[0], ev.start_time[ev.path == p].to_numpy(), meta[p][\"reach_side\"]) for p in A.path]\nwith ProcessPoolExecutor(12) as ex:\n    wr = dict(ex.map(_wrist_job, wjobs))\ntw = wr[A.path[0]][1]\nprint(f\"wrist traces read in {time.time() - t:.0f} s; {len(tw)} frames from {tw[0]} to {tw[-1]} s\")\nbase_m = (tw >= -1.5 - 1e-9) & (tw <= -1 + 1e-9)\npost_m = (tw >= 0) & (tw <= 1.5 + 1e-9)\ni0 = int(np.argmin(np.abs(tw)))\nrows = []\nfor setname in (\"set_b1\", \"set_a\"):\n    for s in SUBJECTS:\n        disp = {}\n        for side in (\"contra\", \"ipsi\"):\n            arrs = [wr[p][0][side][ev[ev.path == p][setname].to_numpy()] for p in A.path[A.subject == s]]\n            X = np.concatenate(arrs)\n            for reading, ref in ((\"a\", np.nanmean(X[:, base_m], 1, keepdims=True)), (\"b\", X[:, i0:i0 + 1])):\n                d = np.linalg.norm(X - ref, axis=2)\n                disp[(side, reading)] = np.nanmedian(d, 0)\n        for reading in (\"a\", \"b\"):\n            c, i = disp[(\"contra\", reading)][post_m].max(), disp[(\"ipsi\", reading)][post_m].max()\n            rows.append(dict(events=setname, reading=reading, subject=s, contra_peak=c, ipsi_peak=i, ratio=c / i, holds=c > i))\nwt = pd.DataFrame(rows)\nprint(wt.pivot_table(index=\"subject\", columns=[\"events\", \"reading\"], values=\"ratio\").round(2).to_string())\nprint(wt.groupby([\"events\", \"reading\"]).holds.sum().to_string())\nprint(\"contralateral and ipsilateral peaks (px), reading b1:\")\nprint(wt[wt.events == \"set_b1\"].pivot_table(index=\"subject\", columns=\"reading\", values=[\"contra_peak\", \"ipsi_peak\"]).round(1).to_string())\nnan_frac = np.mean([np.isnan(wr[p][0][\"contra\"]).any(axis=(1, 2)).mean() for p in A.path])\nprint(f\"mean fraction of events with a missing contralateral pose frame in -1.5 to 1.5 s: {nan_frac:.3f} (nan frames are skipped by the medians)\")\n\n# %% [markdown]\n# > extfig2-2-feature-correlations: Over all events, reach magnitude correlates with reach duration\n# > (r = 0.26) and onset speed (r = 0.56), reach duration with bimanual overlap (r = 0.48), and the\n# > bimanual features with one another (overlap and ratio 0.51, class and ratio 0.50, overlap and\n# > class 0.61).\n\n# %% tags=claim:extfig2-2-feature-correlations\npairs = [(\"magnitude\", \"duration\", 0.26), (\"magnitude\", \"onset_speed\", 0.56), (\"duration\", \"bimanual_overlap\", 0.48),\n         (\"bimanual_overlap\", \"bimanual_ratio\", 0.51), (\"bimanual_class\", \"bimanual_ratio\", 0.50),\n         (\"bimanual_overlap\", \"bimanual_class\", 0.61)]\nfor setname in (\"set_b1\", \"set_a\", \"set_b2\"):\n    C = ev[ev[setname]][[c for c in FEAT.values()]].corr()\n    vals = [C.loc[a, b] for a, b, _ in pairs]\n    within = [abs(v - e) <= 0.1 * e for v, (_, _, e) in zip(vals, pairs)]\n    print(f\"events {setname} (n={int(ev[setname].sum())}): \" + \"; \".join(f\"{a}-{b} r={v:.3f} (paper {e})\" for (a, b, e), v in zip(pairs, vals)))\n    print(f\"   within 10%: {within} -> {sum(within)} of 6\")\n\n# %% [markdown]\n# > fig2-days-and-waking: Reach counts were fairly even across recording days except for subjects\n# > 04, 05 and 09, each with one day holding most events, and events occurred mostly during waking\n# > hours.\n\n# %% tags=claim:fig2-days-and-waking\ne = ev[ev.set_b1]\ndc = e.groupby([\"subject\", \"day\"]).size().unstack()\nbusiest = (dc.max(1) / dc.sum(1))\nwake = e.groupby(\"subject\").hour.apply(lambda h: ((h >= 8) & (h < 24)).mean())\nout = pd.DataFrame({\"busiest_day_frac\": busiest, \"busiest_day\": dc.idxmax(1), \"waking_frac\": wake})\nprint(dc.fillna(0).astype(int).to_string())\nprint(out.round(3).to_string())\nprint(\"subjects whose busiest day holds more than half:\", list(out.index[out.busiest_day_frac > 0.5]))\nprint(\"subjects with more than half of events in 08:00-24:00:\", int((out.waking_frac > 0.5).sum()), \"of\", len(out))\nea = ev\nprint(\"reading a, busiest-day fractions:\", (ea.groupby([\"subject\", \"day\"]).size().unstack().pipe(lambda d: d.max(1) / d.sum(1))).round(3).to_dict())\n\n# %% [markdown]\n# ## Spectral power (Figures 3 to 5, Table 1, Extended Data Figure 5-1)\n#\n# Region power per event is the projection of each electrode's baseline-subtracted Morlet power\n# (dB) with the paper's weights. The group spectrogram and its mask follow the claims file:\n# per subject the median over events, the mean over subjects, the group median over -1.5 to -1 s\n# subtracted again; the null takes, for each frequency, each subject's baseline bins shuffled\n# and the median over subjects, about 2000 values per frequency; two-sided percentile p;\n# Benjamini-Hochberg over all frequency and time bins of the region at 0.05.\n\n# %%\nSET = \"set_b1\"\nroi_ev = np.concatenate([spec[p][\"roi\"] for p in A.path])          # events, regions, freqs, bins\nsel_ev = ev[SET].to_numpy()\nsubj_med = {s: np.nanmedian(roi_ev[sel_ev & (ev.subject == s).to_numpy()], 0) for s in SUBJECTS}\nbmask = (TB >= -1.5 - 1e-9) & (TB <= -1 + 1e-9)\ngrp = np.mean([subj_med[s] for s in SUBJECTS], 0)\ngrp = grp - np.median(grp[:, :, bmask], axis=2, keepdims=True)\n\n\ndef bh(p, q=0.05):\n    p = np.asarray(p).ravel()\n    o = np.argsort(p)\n    th = q * np.arange(1, len(p) + 1) / len(p)\n    ok = p[o] <= th\n    k = np.max(np.where(ok)[0]) + 1 if ok.any() else 0\n    sig = np.zeros(len(p), bool)\n    sig[o[:k]] = True\n    return sig\n\n\nrng_mask = np.random.default_rng(3)\nS = np.stack([subj_med[s] for s in SUBJECTS])                        # subjects, regions, freqs, bins\nnb = int(bmask.sum())\nreps = int(np.ceil(2000 / nb))\nmasked = np.zeros_like(grp)\nnsig = {}\nfor r in range(len(ajile.REGIONS)):\n    pvals = np.zeros(grp.shape[1:])\n    for fi in range(len(F)):\n        base = S[:, r, fi][:, bmask]                                   # subjects x baseline bins\n        null = np.concatenate([np.median(np.stack([rng_mask.permutation(b) for b in base]), 0) for _ in range(reps)])\n        obs = grp[r, fi]\n        hi = (null[None, :] >= obs[:, None]).mean(1)\n        lo = (null[None, :] <= obs[:, None]).mean(1)\n        pvals[fi] = np.minimum(1, 2 * np.minimum(hi, lo))\n    sig = bh(pvals).reshape(pvals.shape)\n    masked[r] = np.where(sig, grp[r], 0)\n    nsig[ajile.REGIONS[r]] = int(sig.sum())\nprint(f\"null values per frequency: {reps * nb}; significant bins per region (of {grp.shape[1] * grp.shape[2]}):\", nsig)\nprint(\"group spectrogram range (dB):\", grp.min().round(2), grp.max().round(2), \"; time bins\", TB[0], \"to\", TB[-1])\n\n# %% [markdown]\n# > fig3-group-lfb-decrease-hfb-increase: At the group level, low-frequency power decreases and\n# > high-frequency power increases at movement initiation in several cortical regions.\n\n# %% tags=claim:fig3-group-lfb-decrease-hfb-increase\nlo_f = (F >= 4) & (F <= 30)\nhi_f = (F >= 50) & (F <= 120)\nwin = (TB >= 0 - 1e-9) & (TB <= 0.5 + 1e-9)\nt0 = int(np.argmin(np.abs(TB)))\nrows = []\nfor r, name in enumerate(ajile.REGIONS):\n    rows.append(dict(region=ajile.REGION_NAMES[name],\n                     a_low=masked[r][lo_f][:, win].mean(), a_high=masked[r][hi_f][:, win].mean(),\n                     b_low=masked[r][lo_f, t0].mean(), b_high=masked[r][hi_f, t0].mean(),\n                     unmasked_a_low=grp[r][lo_f][:, win].mean(), unmasked_a_high=grp[r][hi_f][:, win].mean()))\nf3 = pd.DataFrame(rows)\nf3[\"a_holds\"] = (f3.a_low < 0) & (f3.a_high > 0)\nf3[\"b_holds\"] = (f3.b_low < 0) & (f3.b_high > 0)\nprint(f3.round(3).to_string(index=False))\nthree = [\"precentral\", \"postcentral\", \"inferior parietal\"]\nfor rd in (\"a\", \"b\"):\n    print(f\"reading {rd}: holds in {int(f3[f3.region.isin(three)][rd + '_holds'].sum())} of the 3 named regions; in {int(f3[rd + '_holds'].sum())} of 8\")\nfig, axs = plt.subplots(2, 4, figsize=(14, 6), sharex=True, sharey=True)\nfor r, ax in enumerate(axs.ravel()):\n    im = ax.pcolormesh(TB, F, masked[r], cmap=\"RdBu_r\", vmin=-1.5, vmax=1.5, shading=\"nearest\")\n    ax.set_title(ajile.REGION_NAMES[ajile.REGIONS[r]])\nfig.colorbar(im, ax=axs, label=\"dB (masked)\")\nfig.supxlabel(\"time from onset (s)\")\nfig.supylabel(\"frequency (Hz)\")\nplt.show()\nprint(f\"masked values range {masked.min():.2f} to {masked.max():.2f} dB; values outside the colour scale +-1.5 dB: {int((np.abs(masked) > 1.5).sum())}\")\n\n# %% [markdown]\n# > fig3-sensorimotor-largest: Spectral power changes are largest in precentral, postcentral and\n# > inferior parietal regions, and the three temporal regions show minimal movement-related\n# > changes.\n\n# %% tags=claim:fig3-sensorimotor-largest\nw2 = (TB >= -0.5 - 1e-9) & (TB <= 0.5 + 1e-9)\nrows = []\nfor r, name in enumerate(ajile.REGIONS):\n    m = np.abs(masked[r])\n    rows.append(dict(region=ajile.REGION_NAMES[name], a=m[:, win].mean(), b_low=m[lo_f][:, win].mean(),\n                     b_high=m[hi_f][:, win].mean(), c=m[:, w2].mean()))\nf3b = pd.DataFrame(rows).set_index(\"region\")\nprint(f3b.round(4).to_string())\ntemporal = [\"superior temporal\", \"middle temporal\", \"inferior temporal\"]\nfor col in (\"a\", \"b_low\", \"b_high\", \"c\"):\n    top3 = list(f3b[col].sort_values(ascending=False).index[:3])\n    t_below = all(f3b.loc[t, col] < f3b.loc[three, col].min() for t in temporal)\n    print(f\"{col}: top three {top3}; named three are the top three: {set(top3) == set(three)}; \"\n          f\"named in top three: {len(set(top3) & set(three))}; every temporal region below all three: {t_below}\")\nrank_b = (f3b.b_low.rank(ascending=False) <= 3) & (f3b.b_high.rank(ascending=False) <= 3)\nprint(\"reading b, regions in the top three in both bands:\", list(f3b.index[rank_b]))\n\n# %% [markdown]\n# > fig3-lfb-more-widespread: Low-frequency power decreases are more spatially widespread than\n# > high-frequency increases and are also present in supramarginal and superior temporal regions.\n\n# %% tags=claim:fig3-lfb-more-widespread\nneg = {ajile.REGION_NAMES[n]: int((masked[r][lo_f][:, win] < 0).sum()) for r, n in enumerate(ajile.REGIONS)}\npos = {ajile.REGION_NAMES[n]: int((masked[r][hi_f][:, win] > 0).sum()) for r, n in enumerate(ajile.REGIONS)}\nprint(\"significant negative 4-30 Hz bins over 0-0.5 s per region:\", neg)\nprint(\"significant positive 50-120 Hz bins over 0-0.5 s per region:\", pos)\nra_low, ra_high = sum(v > 0 for v in neg.values()), sum(v > 0 for v in pos.values())\nrb_low, rb_high = sum(neg.values()) / lo_f.sum(), sum(pos.values()) / hi_f.sum()\nprint(f\"reading a: regions with a negative LFB bin {ra_low}, with a positive HFB bin {ra_high}\")\nprint(f\"reading b: negative LFB bins per frequency bin {rb_low:.2f} ({lo_f.sum()} bins), positive HFB bins per frequency bin {rb_high:.2f} ({hi_f.sum()} bins)\")\nprint(\"supramarginal and superior temporal negative LFB bins:\", neg[\"supramarginal\"], neg[\"superior temporal\"])\n\n# %% [markdown]\n# > fig4-precentral-subject-variability: In the precentral region every subject shows the\n# > low/high-frequency pattern, but amplitudes and frequency bands vary; subjects 03, 06, 07, 08 and\n# > 11 have increases up to 120 Hz, subjects 09 and 12 mainly at 60-80 Hz, and subjects 04 and 08\n# > have narrower low-frequency decreases.\n\n# %% tags=claim:fig4-precentral-subject-variability\nspec_s = {}\nfor s in SUBJECTS:\n    m = subj_med[s][pre]\n    m = m - m[:, bmask].mean(1, keepdims=True)\n    spec_s[s] = m[:, win].mean(1)\nSP = pd.DataFrame(spec_s, index=F).T\nprint(\"precentral spectrum per subject, 0-0.5 s (dB):\")\nprint(SP.round(2).to_string())\nlfb_f, hfb_f = (F >= 8) & (F <= 32), (F >= 76) & (F <= 100)\np1 = {s: (SP.loc[s, lfb_f].mean() < 0) and (SP.loc[s, hfb_f].mean() > 0) for s in SUBJECTS}\nprint(\"part 1, LFB mean < 0 and HFB mean > 0:\", p1, \"->\", all(p1.values()))\nnamed2 = [s for s in (3, 6, 7, 8, 11) if s in SUBJECTS]\np2 = {s: bool((SP.loc[s, [116, 121]] > 0).all()) for s in named2}\nprint(\"part 2, 116 and 121 Hz positive:\", p2, \"->\", all(p2.values()))\np3 = {}\nfor s in [s for s in (9, 12) if s in SUBJECTS]:\n    hi = SP.loc[s, F >= 56]\n    fmax = hi.idxmax()\n    p3[s] = (61 <= fmax <= 76) and (SP.loc[s, (F >= 101) & (F <= 121)].mean() < hi.max() / 2)\n    print(f\"   S{s:02d}: largest 56-121 Hz bin at {fmax} Hz ({hi.max():.2f} dB); mean 101-121 Hz {SP.loc[s, (F >= 101) & (F <= 121)].mean():.2f} dB\")\nprint(\"part 3:\", p3, \"->\", all(p3.values()))\nwidth = {s: int((SP.loc[s, F <= 46] < SP.loc[s, F <= 46].min() / 2).sum()) for s in SUBJECTS}\nfewest = sorted(width, key=lambda s: width[s])[:3]\nprint(\"part 4, width of the decrease (1-46 Hz bins below half of the most negative):\", width)\nties = sorted(set(width.values()))\nprint(\"   three fewest (ties broken by subject order):\", fewest, \"; S04 and S08 among them:\", [s in fewest for s in (4, 8)],\n      \"; subjects with width <= the third smallest:\", [s for s in SUBJECTS if width[s] <= sorted(width.values())[2]])\n\n# %% [markdown]\n# ### Banded precentral power per event\n#\n# Band power from the region spectrogram of each event over 0 to 0.5 s: LFB bins 11 to 31 Hz,\n# HFB bins 76 to 96 Hz, the mean over bins (Methods; main) and the median over time bins then\n# over frequency bins (code; variant). Without baseline: the projection of each electrode's\n# 10*log10 band mean with no subtraction.\n\n# %%\nlf_i, hf_i = (F >= 8) & (F <= 32), (F >= 76) & (F <= 100)\npr = roi_ev[:, pre][:, :, win]                                        # events, freqs, bins\nbp = pd.DataFrame({\"lfb_mean\": pr[:, lf_i].mean((1, 2)), \"hfb_mean\": pr[:, hf_i].mean((1, 2)),\n                   \"lfb_median\": np.median(np.median(pr[:, lf_i], 2), 1), \"hfb_median\": np.median(np.median(pr[:, hf_i], 2), 1)})\nraw_l, raw_h, bl_l, bl_h = [], [], [], []\nfor p in A.path:\n    w = proj[p][:, pre]\n    b = spec[p][\"band\"]\n    raw_l.append(b[:, :, 4] @ w)\n    raw_h.append(b[:, :, 6] @ w)\n    bl_l.append(b[:, :, 0] @ w)\n    bl_h.append(b[:, :, 2] @ w)\nbp[\"lfb_raw\"], bp[\"hfb_raw\"] = np.concatenate(raw_l), np.concatenate(raw_h)\nbp[\"lfb_check\"] = np.concatenate(bl_l)\nbp[[\"subject\", \"day\"]] = ev[[\"subject\", \"day\"]].to_numpy()\nbp = bp[ev[SET].to_numpy()].reset_index(drop=True)\nprint(\"check, band mean from the region spectrogram equals the projection of electrode band means:\",\n      float(np.nanmax(np.abs(bp.lfb_mean - bp.lfb_check))))\nprint(bp.drop(columns=[\"lfb_check\"]).describe().T[[\"count\", \"mean\", \"min\", \"max\"]].round(2).to_string())\n\n# %% [markdown]\n# > fig5-band-power-differs-across-subjects: Precentral LFB and HFB power in the 0.5 s after\n# > movement onset differs significantly across subjects.\n\n# %% tags=claim:fig5-band-power-differs-across-subjects\nfor c in (\"lfb_mean\", \"hfb_mean\", \"lfb_median\", \"hfb_median\"):\n    h, p = stats.kruskal(*[g[c].to_numpy() for _, g in bp.groupby(\"subject\")])\n    print(f\"{c}: Kruskal-Wallis H = {h:.1f}, p = {p:.2e} ({bp.subject.nunique()} subjects, {len(bp)} events)\")\n\n# %% [markdown]\n# > table1-subject-band-power-ci: Each subject's precentral band power lies in the 95% bootstrap\n# > interval Table 1 gives; LFB power is below baseline and HFB power above it for most subjects.\n\n# %% tags=claim:table1-subject-band-power-ci\nT1 = {1: (-1.87, -1.29, 0.03, 0.23), 2: (-1.12, -0.31, 0.07, 0.64), 3: (-2.11, -1.73, 1.39, 1.67), 4: (-0.17, 0.01, 0.32, 0.52),\n      5: (-0.7, -0.38, 0.2, 0.48), 6: (-1.63, -1.11, 2.02, 2.37), 7: (-0.84, -0.51, 1.14, 1.34), 8: (-0.3, 0.04, 0.36, 0.63),\n      9: (-0.57, -0.08, -0.11, 0.23), 10: (-0.87, -0.35, 0.01, 0.3), 11: (-2.3, -1.86, 0.09, 0.34), 12: (-0.66, -0.44, 0.06, 0.2)}\nrng_t1 = np.random.default_rng(1)\nrows = []\nfor s in SUBJECTS:\n    g = bp[bp.subject == s]\n    for band, (lo_i, hi_i) in ((\"LFB\", (0, 1)), (\"HFB\", (2, 3))):\n        lo, hi = T1[s][lo_i], T1[s][hi_i]\n        for bandstat in (\"mean\", \"median\"):\n            v = g[f\"{band.lower()}_{bandstat}\"].to_numpy()\n            for evstat, fn in ((\"mean\", np.mean), (\"median\", np.median)):\n                est = fn(v)\n                boot = fn(v[rng_t1.integers(0, len(v), (5000, len(v)))], axis=1)\n                rows.append(dict(subject=s, band=band, band_stat=bandstat, event_stat=evstat, estimate=est,\n                                 paper_lo=lo, paper_hi=hi, inside=lo <= est <= hi,\n                                 boot_lo=np.percentile(boot, 2.5), boot_hi=np.percentile(boot, 97.5)))\nt1 = pd.DataFrame(rows)\nsummary = t1.groupby([\"band_stat\", \"event_stat\"]).inside.sum()\nprint(\"subject and band pairs inside the paper's interval, of\", 2 * len(SUBJECTS), \":\")\nprint(summary.to_string())\nprint(t1[(t1.band_stat == \"mean\") & (t1.event_stat == \"mean\")].round(2).to_string(index=False))\nbest = summary.idxmax()\nprint(\"best reading:\", best, int(summary.max()))\nprint(t1[(t1.band_stat == best[0]) & (t1.event_stat == best[1])].round(2).to_string(index=False))\nlfb_neg = (t1[(t1.band == \"LFB\") & (t1.band_stat == \"mean\") & (t1.event_stat == \"mean\")].estimate < 0).sum()\nhfb_pos = (t1[(t1.band == \"HFB\") & (t1.band_stat == \"mean\") & (t1.event_stat == \"mean\")].estimate > 0).sum()\nprint(f\"subjects with mean LFB below 0: {lfb_neg}; with mean HFB above 0: {hfb_pos} (of {len(SUBJECTS)})\")\n\n# %% [markdown]\n# > fig5-recording-day-effects: Precentral band power differs significantly across recording days\n# > in LFB for subjects 03, 05, 06, 07, 08 and 11, and in HFB for subjects 03, 04, 07, 08 and 10.\n\n# %% tags=claim:fig5-recording-day-effects\npaper_sig = {(\"LFB\", s) for s in (3, 5, 6, 7, 8, 11)} | {(\"HFB\", s) for s in (3, 4, 7, 8, 10)}\nrows = []\nfor s in SUBJECTS:\n    g = bp[bp.subject == s]\n    for band in (\"LFB\", \"HFB\"):\n        for st in (\"mean\", \"median\"):\n            c = f\"{band.lower()}_{st}\"\n            h, p = stats.kruskal(*[x[c].to_numpy() for _, x in g.groupby(\"day\")])\n            rows.append(dict(subject=s, band=band, band_stat=st, p=p, sig=p < 0.05, paper_sig=(band, s) in paper_sig))\ndy = pd.DataFrame(rows)\ndy[\"agree\"] = dy.sig == dy.paper_sig\nprint(dy.pivot_table(index=\"subject\", columns=[\"band\", \"band_stat\"], values=\"p\").to_string(float_format=lambda x: f\"{x:.3g}\"))\nprint(\"pairs agreeing with the paper's pattern, of\", 2 * len(SUBJECTS), \":\", dy.groupby(\"band_stat\").agree.sum().to_dict())\nprint(\"disagreeing pairs (band mean):\", dy[(dy.band_stat == \"mean\") & ~dy.agree][[\"subject\", \"band\", \"p\", \"paper_sig\"]].round(4).values.tolist())\nprint(\"significant pairs (band mean):\", int(dy[dy.band_stat == \"mean\"].sig.sum()))\nprint(\"per-day means (dB), band mean:\")\nprint(bp.groupby([\"subject\", \"day\"])[[\"lfb_mean\", \"hfb_mean\"]].mean().unstack().round(2).to_string())\n\n# %% [markdown]\n# > extfig5-1-baseline-reduces-day-variability: Subtracting the -1.5 to -1 s baseline reduces the\n# > variability of band power across recording days, though clear variability remains.\n#\n# Reading (a): precentral region, per subject, the SD across days of the day means of event band\n# power, with baseline (band mean) and without (projected 10*log10 band mean). Reading (b): the\n# same per electrode, on the days the electrode is marked good, for electrodes good on at least two\n# days.\n\n# %% tags=claim:extfig5-1-baseline-reduces-day-variability\nrows = []\nfor s in SUBJECTS:\n    g = bp[bp.subject == s]\n    dm = g.groupby(\"day\")[[\"lfb_mean\", \"hfb_mean\", \"lfb_raw\", \"hfb_raw\"]].mean()\n    rows.append(dict(subject=s, lfb_sd_bl=dm.lfb_mean.std(), lfb_sd_raw=dm.lfb_raw.std(),\n                     hfb_sd_bl=dm.hfb_mean.std(), hfb_sd_raw=dm.hfb_raw.std()))\nra = pd.DataFrame(rows)\nprint(ra.round(3).to_string(index=False))\nfor b in (\"lfb\", \"hfb\"):\n    print(f\"reading a, {b}: SD with baseline below SD without in {int((ra[b + '_sd_bl'] < ra[b + '_sd_raw']).sum())} of {len(ra)} subjects\")\nel_rows = []\nfor s in SUBJECTS:\n    paths = list(A.path[A.subject == s])\n    nch = spec[paths[0]][\"band\"].shape[1]\n    for c in range(nch):\n        dm = {k: [] for k in (\"lb\", \"lr\", \"hb\", \"hr\")}\n        for p in paths:\n            if not meta[p][\"electrodes\"].good.iloc[c]:\n                continue\n            msk = ev[ev.path == p][SET].to_numpy()\n            b = spec[p][\"band\"][msk, c]\n            for k, j in ((\"lb\", 0), (\"lr\", 4), (\"hb\", 2), (\"hr\", 6)):\n                dm[k].append(np.nanmean(b[:, j]))\n        if len(dm[\"lb\"]) >= 2:\n            el_rows.append(dict(subject=s, ch=c, **{k: np.std(v, ddof=1) for k, v in dm.items()}))\nrb = pd.DataFrame(el_rows)\nfor b, (kb, kr) in ((\"lfb\", (\"lb\", \"lr\")), (\"hfb\", (\"hb\", \"hr\"))):\n    print(f\"reading b, {b}: SD with baseline below SD without in {int((rb[kb] < rb[kr]).sum())} of {len(rb)} electrodes \"\n          f\"(median SD with {rb[kb].median():.3f}, without {rb[kr].median():.3f} dB)\")\nprint(\"by subject, fraction of electrodes with lower SD after baseline (LFB, HFB):\")\nprint(rb.assign(l=rb.lb < rb.lr, h=rb.hb < rb.hr).groupby(\"subject\")[[\"l\", \"h\"]].mean().round(2).T.to_string())\nprint(\"significant day effects found in fig5-recording-day-effects (band mean):\", int(dy[dy.band_stat == \"mean\"].sig.sum()))\n\n# %% [markdown]\n# > discussion-day-changes-small: Day-to-day changes in baseline-subtracted spectral power are\n# > small (about 1-2 dB) compared with spectral power without baseline subtraction (about 10-50\n# > dB).\n\n# %% tags=claim:discussion-day-changes-small\nrows = []\nfor s in SUBJECTS:\n    g = bp[bp.subject == s]\n    for band in (\"lfb\", \"hfb\"):\n        dm = g.groupby(\"day\")[f\"{band}_mean\"].mean()\n        rows.append(dict(subject=s, band=band, max_dev=np.abs(dm - g[f\"{band}_mean\"].mean()).max(),\n                         day_range=dm.max() - dm.min(), level_uV=g[f\"{band}_raw\"].mean(), level_V=g[f\"{band}_raw\"].mean() - 120))\ndc2 = pd.DataFrame(rows)\nprint(dc2.round(2).to_string(index=False))\nprint(f\"largest day-to-day change (deviation of a day mean from the subject mean): {dc2.max_dev.max():.2f} dB; all at most 2.2 dB: {bool((dc2.max_dev <= 2.2).all())}\")\nprint(f\"largest range of day means: {dc2.day_range.max():.2f} dB\")\nfor u in (\"level_uV\", \"level_V\"):\n    print(f\"level without baseline, {u}: {dc2[u].min():.1f} to {dc2[u].max():.1f} dB; all in 9-55 dB: {bool(dc2[u].between(9, 55).all())}\")\n\n# %% [markdown]\n# ## Summary\n#\n# (Written after the run; see the attempt record.)\n\n# %%\nprint(f\"notebook ran in {(time.time() - T0) / 60:.1f} min\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build/nb1.py (file state is current in your context — no need to Read it back)
```

**Agent**

The rejection cell came out convoluted; rewriting it cleanly before running:

**Agent calls Bash**

```bash
cd $TMPDIR/build && python - <<'EOF'
s=open('nb1.py').read()
i=s.index('pa, ph, pa_ch, ph_ch = [], [], [], []'); j=s.index('ev["rej_b1"] = rej1 & ev.ok')
new='''rej1 = np.zeros(len(ev), bool)
rej2 = np.zeros(len(ev), bool)
psd_db = np.full(len(ev), np.nan)
for s in SUBJECTS:
    paths = list(A.path[A.subject == s])
    idx = np.where(ev.subject == s)[0]                       # events of the subject, in file order
    good = np.concatenate([np.tile(meta[p]["electrodes"].good.to_numpy(), (len(spec[p]["ok"]), 1)) for p in paths])
    allc = np.concatenate([spec[p]["psd_all"] for p in paths])
    hfc = np.concatenate([spec[p]["psd_hf"] for p in paths])
    ok = ev.ok.to_numpy()[idx]
    # (b1) PSD averaged over good electrodes
    mean_all = 10 * np.log10(np.nansum(np.where(good, allc, 0), 1) / good.sum(1))
    mean_hf = 10 * np.log10(np.nansum(np.where(good, hfc, 0), 1) / good.sum(1))
    psd_db[idx] = mean_all
    mu, sd = np.nanmean(mean_hf[ok]), np.nanstd(mean_hf[ok])
    rej1[idx] = (mean_all < 0) | (mean_hf > mu + 3 * sd)
    # (b2) each good electrode
    db_all = np.where(good, 10 * np.log10(allc), np.inf)
    db_hf = np.where(good, 10 * np.log10(hfc), np.nan)
    mu_c, sd_c = np.nanmean(db_hf[ok], 0), np.nanstd(db_hf[ok], 0)
    rej2[idx] = (np.min(db_all, 1) < 0) | np.any(db_hf > mu_c + 3 * sd_c, axis=1)
ev["psd_db"] = psd_db
'''
s=s[:i]+new+s[j:]
open('nb1.py','w').write(s)
EOF
grep -n "rej_b1\|psd_db" nb1.py | head
```

```
325:psd_db = np.full(len(ev), np.nan)
336:    psd_db[idx] = mean_all
344:ev["psd_db"] = psd_db
345:ev["rej_b1"] = rej1 & ev.ok
349:ev["set_b1"] = ev.set_fp & ev.ok & ~ev.rej_b1
351:print("PSD averaged over good electrodes, dB (uV^2/Hz), 1-200 Hz: range", ev.psd_db.min().round(1), "to", ev.psd_db.max().round(1))
352:print(ev.groupby("subject")[["set_a", "set_fp", "set_b1", "set_b2", "rej_b1", "rej_b2"]].sum().T.to_string())
Shell cwd was reset to
```

**Agent**

Moving the wrist job into the helper (safer with process pools), then running notebook 1 as a script on S04 and S09:

**Agent calls Bash**

```bash
cat >> entries/000055-peterson-2021/ajile.py <<'EOF'


def _wrist_job(args):
    key, asset_id, onsets, side = args
    return key, wrist_traces(asset_id, onsets, side)


def wrist_many(jobs, workers=12):
    """jobs: list of (key, asset_id, onsets, side). Returns {key: (traces, time axis)}."""
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(workers) as ex:
        return dict(ex.map(_wrist_job, jobs))
EOF
cd $TMPDIR/build && python - <<'EOF'
s=open('nb1.py').read()
s=s.replace('''def _wrist_job(args):
    p, aid, on, side = args
    return p, ajile.wrist_traces(aid, on, side)


t = time.time()''','''t = time.time()''')
s=s.replace('''with ProcessPoolExecutor(12) as ex:
    wr = dict(ex.map(_wrist_job, wjobs))''','''wr = ajile.wrist_many(wjobs, workers=12)''')
open('nb1.py','w').write(s)
EOF
cd entries/000055-peterson-2021 && . $TMPDIR/dev/bin/activate && date -u && AJILE_SUBJECTS=4,9 MPLBACKEND=Agg timeout 1500 python $TMPDIR/build/nb1.py > $TMPDIR/dev_nb1.log 2>&1; echo exit $?; date -u; tail -5 $TMPDIR/dev_nb1.log
```

```
Fri Oct 23 16:15:13 UTC 2026
exit 1
Fri Oct 23 16:15:15 UTC 2026
Traceback (most recent call last):
  File "/tmp/claude-1001/build/nb1.py", line 47, in <module>
    import ajile
ModuleNotFoundError: No module named 'ajile'
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && PYTHONPATH=. AJILE_SUBJECTS=4,9 MPLBACKEND=Agg timeout 1500 python $TMPDIR/build/nb1.py > $TMPDIR/dev_nb1.log 2>&1; echo exit $?; date -u; tail -30 $TMPDIR/dev_nb1.log
```

```
exit 1
Fri Oct 23 16:18:06 UTC 2026
subject-days in the dataset: 55 ; in Table 2: 55
subject ids inside the files equal the file names: True
Figshare file names (subject, day) equal the DANDI ones: True
 subject  channels  surface  depth      depth_groups hemisphere_x   wrist  sex  age
       4        84       84      0                          right l_wrist None None
       9       126       98     28 LID,RATD,RFD,RPTD         left r_wrist None None
subjects: 2
mean surface electrodes per subject: 91.0 (SD 9.9)
subjects with depth electrodes: 1; mean depth electrodes among them 28.0 (SD nan)
right hemisphere by x: 1 ; by left-wrist events: 1
sex and age in the files: [None] [None] (not held: not testable)
subject    4    9
set_a    417  211
set_fp   268  151
set_b1   268  150
set_b2    69    0
reading set_a: fewest 211, most 417, median 314.0; within tolerance [np.False_, np.False_, np.False_] -> no
reading set_fp: fewest 151, most 268, median 209.5; within tolerance [np.True_, np.False_, np.False_] -> no
[... 12 more lines not kept]
```

**Agent**

Reading (b2) leaves S09 with no events, so the Kruskal-Wallis call fails on empty groups. Adding a guard:

**Agent calls Bash**

```bash
cd $TMPDIR/build && python - <<'EOF'
s=open('nb1.py').read()
s=s.replace('''T0 = time.time()''','''T0 = time.time()


def kruskal(groups):
    """Kruskal-Wallis over the groups with at least one value; nan when fewer than two."""
    groups = [np.asarray(g) for g in groups if len(g) > 0]
    if len(groups) < 2:
        return np.nan, np.nan
    return stats.kruskal(*groups)
''')
s=s.replace('stats.kruskal(*[','kruskal([')
open('nb1.py','w').write(s)
EOF
grep -c "kruskal(\[" $TMPDIR/build/nb1.py; . $TMPDIR/dev/bin/activate && PYTHONPATH=. AJILE_SUBJECTS=4,9 MPLBACKEND=Agg timeout 1500 python $TMPDIR/build/nb1.py > $TMPDIR/dev_nb1.log 2>&1; echo exit $?; date -u; grep -n "Traceback" -A 12 $TMPDIR/dev_nb1.log | tail -15
```

```
3
exit 1
Fri Oct 23 16:18:14 UTC 2026
1:Traceback (most recent call last):
2-  File "/tmp/claude-1001/build/nb1.py", line 47, in <module>
3-    import ajile
4-ModuleNotFoundError: No module named 'ajile'
Shell cwd was reset to
```

**Agent**

I'll add a dev-only wrapper outside the entry that caches the extraction on disk, so iterating on the analysis doesn't re-stream the ECoG each time:

**Agent calls Bash**

```bash
cat > $TMPDIR/build/devrun.py <<'EOF'
import sys, os, pickle, hashlib, runpy
sys.path.insert(0, "entries/000055-peterson-2021")
import ajile
def cached(fn, name):
    def w(jobs, workers=12):
        key = hashlib.md5(repr([(j[0], len(j[2]), float(sum(j[2]))) for j in jobs]).encode()).hexdigest()
        path = f"{os.environ['TMPDIR']}/cache_{name}_{key}.pkl"
        if os.path.exists(path):
            return pickle.load(open(path, "rb"))
        r = fn(jobs, workers); pickle.dump(r, open(path, "wb")); return r
    return w
ajile.extract_many = cached(ajile.extract_many, "ext")
ajile.wrist_many = cached(ajile.wrist_many, "wr")
runpy.run_path(sys.argv[1], run_name="__main__")
EOF
cd entries/000055-peterson-2021 && . $TMPDIR/dev/bin/activate && AJILE_SUBJECTS=4,9 MPLBACKEND=Agg timeout 1500 python $TMPDIR/build/devrun.py $TMPDIR/build/nb1.py > $TMPDIR/dev_nb1.log 2>&1; echo exit $?; date -u; grep -n "Traceback" -A 12 $TMPDIR/dev_nb1.log | tail -15
```

```
exit 1
Fri Oct 23 16:21:44 UTC 2026
284:Traceback (most recent call last):
285-  File "/tmp/claude-1001/build/devrun.py", line 14, in <module>
286-    runpy.run_path(sys.argv[1], run_name="__main__")
287-    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
288-  File "<frozen runpy>", line 294, in run_path
289-  File "<frozen runpy>", line 98, in _run_module_code
290-  File "<frozen runpy>", line 88, in _run_code
291-  File "/tmp/claude-1001/build/nb1.py", line 752, in <module>
292-    "; subjects with width <= the third smallest:", [s for s in SUBJECTS if width[s] <= sorted(width.values())[2]])
293-                                                                                        ~~~~~~~~~~~~~~~~~~~~~~^^^
294-IndexError: list index out of range
```

**Agent**

Only a subset artefact (two subjects). Guarding it and reading the output so far:

**Agent calls Bash**

```bash
cd $TMPDIR/build && sed -i 's/sorted(width.values())\[2\]\])/sorted(width.values())[min(2, len(width) - 1)]])/' nb1.py && cd entries/000055-peterson-2021 && . $TMPDIR/dev/bin/activate && AJILE_SUBJECTS=4,9 MPLBACKEND=Agg timeout 1500 python $TMPDIR/build/devrun.py $TMPDIR/build/nb1.py > $TMPDIR/dev_nb1.log 2>&1; echo exit $?; grep -n "Traceback" -A 12 $TMPDIR/dev_nb1.log | tail -15; cat $TMPDIR/dev_nb1.log | cut -c1-250
```

```
exit 0
/tmp/claude-1001/build/nb1.py:202: Pandas4Warning: Starting with pandas version 4.0 all arguments of sum will be keyword-only.
  valid = cenL.abs().sum(1).to_numpy() > 0
/tmp/claude-1001/build/nb1.py:351: RuntimeWarning: Mean of empty slice
  mu_c, sd_c = np.nanmean(db_hf[ok], 0), np.nanstd(db_hf[ok], 0)
/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/lib/_nanfunctions_impl.py:1997: RuntimeWarning: Degrees of freedom <= 0 for slice.
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
55 assets in the version, 10 read; 10 Figshare epoch files; loaded in 21 s
Assets per subject and the days they hold (from the file names):
subject
1        [3, 4, 5, 7]
2        [3, 4, 5, 6]
3        [3, 4, 5, 6]
4     [3, 4, 5, 6, 7]
5           [3, 4, 7]
6     [3, 4, 5, 6, 7]
7     [3, 4, 5, 6, 7]
8     [3, 4, 5, 6, 7]
9     [3, 4, 5, 6, 7]
10    [3, 4, 5, 6, 7]
[... 333 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pickle, numpy as np
A,md,meta=pickle.load(open('cache.pkl','rb'))
import sys; sys.path.insert(0,'entries/000055-peterson-2021'); import ajile
tot=0; byt=0
for p,m in meta.items():
    st=m['reaches'].start_time.values-ajile.clock_offset(m['session_start'])
    cs=m['ecog_chunks'][0]; rows=set()
    for t in st:
        a=int((t-5)*500); b=int((t+5)*500)-1
        rows.update(range(max(a,0)//cs, max(b,0)//cs+1))
    tot+=len(rows); byt+=len(rows)*cs*4*m['ecog_shape'][1]
print('chunk rows', tot, 'GB', byt/1e9)
"
ls -la $TMPDIR/cache_ext_* | head
```

```
chunk rows 5157 GB 167.66541516
-rw-r--r-- 1 runner runner 18540016 Oct 23 16:21 /tmp/claude-1001/cache_ext_22caf115a91f15a894d68d1569efbf2c.pkl
-rw-r--r-- 1 runner runner   751213 Oct 23 16:19 /tmp/claude-1001/cache_ext_34000a9aef583faf069b8aaa58102cc7.pkl
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && OMP_NUM_THREADS=1 python -c "
import numpy as np, time
from sklearn.linear_model import HuberRegressor
rng=np.random.default_rng(0)
for n in [200,600,900]:
    X=rng.normal(size=(n,4)); y=X[:,0]*.3+rng.standard_t(3,n)
    t=time.time()
    for i in range(40): HuberRegressor().fit(X[:int(.9*n)],y[:int(.9*n)])
    print(n,(time.time()-t)/40)
"
```

```
200 0.000945812463760376
600 0.0008429467678070068
900 0.0008990645408630371
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && python - <<'EOF'
s=open('ajile.py').read()
# light mode for segment_measures / extract_file
s=s.replace('''def segment_measures(x, proj=None):
    """Measures of one 10 s segment x (channels, samples), microvolts."""
    wa, wh = welch_means(x)
    half = x.shape[1] // 2
    k0, k1 = int((SUB - CTRL) * FS), int(SUB * FS)''','''def segment_measures(x, proj=None, light=False):
    """Measures of one 10 s segment x (channels, samples), microvolts. light=True computes only
    the Welch means and the band powers (Morlet over -1.8 to 0.8 s; no clock check)."""
    wa, wh = welch_means(x)
    half = x.shape[1] // 2
    if light:
        k0, k1 = int(SUB * FS), int(0.8 * FS)
        p, t = morlet_power(x[:, half - k0:half + k1 + 1])
        t = t + SEG_HALF - SUB
    else:
        k0, k1 = int((SUB - CTRL) * FS), int(SUB * FS)''')
s=s.replace('''    p, t = morlet_power(x[:, half - k0:half + k1 + 1])
    t = t + SEG_HALF - (SUB - CTRL)              # time relative to onset
''','''        p, t = morlet_power(x[:, half - k0:half + k1 + 1])
        t = t + SEG_HALF - (SUB - CTRL)          # time relative to onset
''')
s=s.replace('''    # clock check: the same band means around a pseudo-onset at CTRL s, with its own baseline
    pc = p''','''    if light:
        return wa, wh, band, None, None, None
    # clock check: the same band means around a pseudo-onset at CTRL s, with its own baseline
    pc = p''')
s=s.replace('''def extract_file(asset_id, onsets, proj=None):''','''def extract_file(asset_id, onsets, proj=None, light=False):''')
s=s.replace('''        wa, wh, band, ctrl, roi, tb = segment_measures(x, proj)
        res["psd_all"][i], res["psd_hf"][i], res["band"][i] = wa, wh, band
        res["ctrl"][i] = ctrl''','''        wa, wh, band, ctrl, roi, tb = segment_measures(x, proj, light)
        res["psd_all"][i], res["psd_hf"][i], res["band"][i] = wa, wh, band
        if ctrl is not None:
            res["ctrl"][i] = ctrl''')
s=s.replace('''def _extract_job(args):
    key, asset_id, onsets, proj = args
    return key, extract_file(asset_id, onsets, proj)''','''def _extract_job(args):
    key, asset_id, onsets, proj = args[:4]
    light = args[4] if len(args) > 4 else False
    return key, extract_file(asset_id, onsets, proj, light)''')
s+='''

def rejection(ev, A, meta, spec, subjects):
    """Segment rejection on the Welch PSD (Methods; the estimator is a standard choice, see the
    question in questions/000055.yaml). Returns (rej_b1, rej_b2, psd_db) over the rows of ev,
    which must hold the events of A's files in A's order.
    (b1) PSD averaged over good electrodes: mean over 1-200 Hz below 0 dB, or mean over
    115-125 Hz more than 3 SD above the subject's segments.
    (b2) the same on each good electrode; a segment fails when any good electrode fails."""
    rej1 = np.zeros(len(ev), bool)
    rej2 = np.zeros(len(ev), bool)
    psd_db = np.full(len(ev), np.nan)
    ok_all = np.concatenate([spec[p]["ok"] for p in A.path])
    for s in subjects:
        paths = list(A.path[A.subject == s])
        idx = np.where(ev.subject.to_numpy() == s)[0]
        good = np.concatenate([np.tile(meta[p]["electrodes"].good.to_numpy(), (len(spec[p]["ok"]), 1))
                               for p in paths])
        allc = np.concatenate([spec[p]["psd_all"] for p in paths])
        hfc = np.concatenate([spec[p]["psd_hf"] for p in paths])
        ok = ok_all[idx]
        with np.errstate(divide="ignore", invalid="ignore"):
            mean_all = 10 * np.log10(np.nansum(np.where(good, allc, 0), 1) / good.sum(1))
            mean_hf = 10 * np.log10(np.nansum(np.where(good, hfc, 0), 1) / good.sum(1))
            psd_db[idx] = np.where(ok, mean_all, np.nan)
            mu, sd = np.nanmean(mean_hf[ok]), np.nanstd(mean_hf[ok])
            rej1[idx] = ok & ((mean_all < 0) | (mean_hf > mu + 3 * sd))
            db_all = np.where(good, 10 * np.log10(allc), np.inf)
            db_hf = np.where(good, 10 * np.log10(hfc), np.nan)
            mu_c, sd_c = np.nanmean(db_hf[ok], 0), np.nanstd(db_hf[ok], 0)
            rej2[idx] = ok & ((np.min(db_all, 1) < 0) | np.any(db_hf > mu_c + 3 * sd_c, axis=1))
    return rej1, rej2, psd_db
'''
open('ajile.py','w').write(s)
EOF
cd $TMPDIR/build && python - <<'EOF'
s=open('nb1.py').read()
i=s.index('rej1 = np.zeros(len(ev), bool)\nrej2'); j=s.index('ev["rej_b1"] = rej1 & ev.ok')
s=s[:i]+'rej1, rej2, ev["psd_db"] = ajile.rejection(ev, A, meta, spec, SUBJECTS)\n'+s[j:]
open('nb1.py','w').write(s)
EOF
grep -n "ajile.rejection" $TMPDIR/build/nb1.py; date -u
```

```
332:rej1, rej2, ev["psd_db"] = ajile.rejection(ev, A, meta, spec, SUBJECTS)
Fri Oct 23 16:23:46 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && sed -n '/^def segment_measures/,/^def extract_file/p' ajile.py
```

```
def segment_measures(x, proj=None, light=False):
    """Measures of one 10 s segment x (channels, samples), microvolts. light=True computes only
    the Welch means and the band powers (Morlet over -1.8 to 0.8 s; no clock check)."""
    wa, wh = welch_means(x)
    half = x.shape[1] // 2
    if light:
        k0, k1 = int(SUB * FS), int(0.8 * FS)
        p, t = morlet_power(x[:, half - k0:half + k1 + 1])
        t = t + SEG_HALF - SUB
    else:
        k0, k1 = int((SUB - CTRL) * FS), int(SUB * FS)
        p, t = morlet_power(x[:, half - k0:half + k1 + 1])
        t = t + SEG_HALF - (SUB - CTRL)          # time relative to onset
    lf, hf = _band_idx(LFB), _band_idx(HFB)

    def win(lo, hi):
        return (t >= lo - 1e-9) & (t <= hi + 1e-9)
    pb = p - p[:, :, win(*BASE)].mean(2, keepdims=True)
    wmask = win(*WIN)
    band = np.empty((x.shape[0], 8), np.float32)
[... 17 more lines not kept]
```

**Agent**

Light mode is correct (the wavelet support needs data to 0.7 s; 0.8 s is read). Now the overlapping pipeline in the helper and notebook 2:

**Agent calls Bash**

```bash
cat >> entries/000055-peterson-2021/ajile.py <<'EOF'


def _fit_batch(batch):
    return [_fit_job(a) for a in batch]


def regression_pipeline(file_jobs, subject_files, make_models, workers=12, batch=6):
    """Extraction and model fits in one process pool, so the fits of a subject start as soon as
    its files are read. file_jobs: (path, asset_id, onsets, None, True) per file; subject_files:
    {subject: [paths]}; make_models(subject, {path: result}) returns fit-job tuples
    (key, X, groups, y, days, seed, kwargs). Returns ({path: result}, {key: fit}, timings)."""
    from concurrent.futures import ProcessPoolExecutor, as_completed
    t0 = time.time()
    spec, fits, done_at = {}, {}, {}
    left = {s: set(p) for s, p in subject_files.items()}
    with ProcessPoolExecutor(workers) as ex:
        futs = {ex.submit(_extract_job, j): "x" for j in sorted(file_jobs, key=lambda j: -len(j[2]))}
        pending = set(futs)
        while pending:
            for f in as_completed(list(pending)):
                pending.discard(f)
                kind = futs[f]
                if kind == "x":
                    path, res = f.result()
                    spec[path] = res
                    for s in left:
                        left[s].discard(path)
                    for s in [s for s, v in left.items() if not v]:
                        del left[s]
                        done_at[s] = time.time() - t0
                        models = make_models(s, {p: spec[p] for p in subject_files[s]})
                        for i in range(0, len(models), batch):
                            g = ex.submit(_fit_batch, models[i:i + batch])
                            futs[g] = "f"
                            pending.add(g)
                else:
                    for key, r in f.result():
                        fits[key] = r
                break
    return spec, fits, {"subjects_read_at": done_at, "total": time.time() - t0}
EOF
echo done
```

```
/bin/bash: line 1: entries/000055-peterson-2021/ajile.py: No such file or directory
done
```

**Agent calls Bash**

```bash
cat >> entries/000055-peterson-2021/ajile.py <<'EOF'


def _fit_batch(batch):
    return [_fit_job(a) for a in batch]


def regression_pipeline(file_jobs, subject_files, make_models, workers=12, batch=6):
    """Extraction and model fits in one process pool, so the fits of a subject start as soon as
    its files are read. file_jobs: (path, asset_id, onsets, None, True) per file; subject_files:
    {subject: [paths]}; make_models(subject, {path: result}) returns fit-job tuples
    (key, X, groups, y, days, seed, kwargs). Returns ({path: result}, {key: fit}, timings)."""
    from concurrent.futures import FIRST_COMPLETED, ProcessPoolExecutor, wait
    t0 = time.time()
    spec, fits, done_at = {}, {}, {}
    left = {s: set(p) for s, p in subject_files.items()}
    with ProcessPoolExecutor(workers) as ex:
        kinds = {ex.submit(_extract_job, j): "x" for j in sorted(file_jobs, key=lambda j: -len(j[2]))}
        pending = set(kinds)
        while pending:
            done, pending = wait(pending, return_when=FIRST_COMPLETED)
            for f in done:
                if kinds[f] == "x":
                    path, res = f.result()
                    spec[path] = res
                    for s in list(left):
                        left[s].discard(path)
                        if not left[s]:
                            del left[s]
                            done_at[s] = time.time() - t0
                            models = make_models(s, {p: spec[p] for p in subject_files[s]})
                            for i in range(0, len(models), batch):
                                g = ex.submit(_fit_batch, models[i:i + batch])
                                kinds[g] = "f"
                                pending.add(g)
                else:
                    for key, r in f.result():
                        fits[key] = r
    return spec, fits, {"subjects_read_at": done_at, "total": time.time() - t0}
EOF
echo ok
```

```
ok
```

**Agent**

Writing notebook 2:

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build/nb2.py",
 "content": "# %% [markdown]\n# # Peterson et al. (2021), eNeuro: regression of single-event power on behaviour (Figure 6)\n#\n# Paper: Peterson, Singh, Wang, Rao and Brunton (2021), eNeuro 8(3), doi:10.1523/ENEURO.0007-21.2021.\n# Dataset: DANDI:000055, version 0.220127.0436, the dandiset's only published version (see the\n# header of `reproduce_peterson_2021.ipynb`, which also holds the data check, the link claims and\n# the clock of the ECoG). Claims: `claims/000055/10.1523-eneuro.0007-21.2021.yaml`.\n#\n# This notebook tests the six claims on the regression models of Figure 6. It reads the ECoG of\n# every event again (band power only) and fits, for every electrode and band, the models the\n# claims file's opening comment describes: forward selection by OLS adjusted R2, sklearn's\n# HuberRegressor, 200 random splits with 90% training events and equal numbers of test events from\n# each day, Delta R2 by shuffling one feature. The events are those of reading (b1) in the first\n# notebook (Figshare false positives dropped, segments rejected on the PSD averaged over good\n# electrodes). The ECoG clock of the three late-starting files is shifted as in the first notebook.\n#\n# | Claim | Here |\n# |---|---|\n# | fig6b-best-models-sensorimotor | tested |\n# | fig6-r2-at-most-025 | tested |\n# | fig6c-angle-and-day-most-informative | tested |\n# | extfig6-2-angle-most-retained | tested |\n# | fig6d-upward-reaches-enhance-pattern | tested |\n# | fig6d-angle-and-day-largest-coefficients | tested |\n#\n# Not run, for time: the code's 80/20 split and the median band power as variants (each would\n# double the fits), and the code's log(x + 1) transforms.\n\n# %%\nimport os, time, io, zlib\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"OPENBLAS_NUM_THREADS\", \"1\")\nimport numpy as np\nimport pandas as pd\nfrom concurrent.futures import ProcessPoolExecutor\nimport matplotlib.pyplot as plt\nimport ajile\n\nT0 = time.time()\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\nSUBJECTS = [int(s) for s in os.environ.get(\"AJILE_SUBJECTS\", \",\".join(map(str, range(1, 13)))).split(\",\")]\nA_all = ajile.assets()\nA = A_all[A_all.subject.isin(SUBJECTS)].reset_index(drop=True)\nwith ProcessPoolExecutor(8) as ex:\n    meta = dict(zip(A.path, ex.map(ajile.read_meta, A.asset_id)))\nfig_files = ajile.figshare_files(ajile.EPOCH_ARTICLE)\nfig_names = sorted(n for n in fig_files if int(n[5:7]) in SUBJECTS)\nwith ProcessPoolExecutor(8) as ex:\n    figmeta = dict(zip(fig_names, ex.map(ajile.epoch_metadata, fig_names, [fig_files] * len(fig_names))))\nroi_txt, roi_files = ajile.roi_matrices()\nev = ajile.events_table(A, meta, figmeta)\nprint(f\"{len(A)} files, {len(ev)} events, {int(ev.false_pos.sum())} Figshare false positives; loaded in {time.time() - T0:.0f} s\")\n\n# %% tags=sanity\nW_all = {}\nfor s in SUBJECTS:\n    dens, W = ajile.roi_tables(roi_txt[s])\n    W_all[s] = W.iloc[:len(meta[A.path[A.subject == s].iloc[0]][\"electrodes\"])]\ngood_all = {}\nfor s in SUBJECTS:\n    g = np.stack([meta[p][\"electrodes\"].good.to_numpy() for p in A.path[A.subject == s]])\n    good_all[s] = g.all(0)\n    print(f\"S{s:02d}: {g.shape[1]} channels, good on every day {int(g.all(0).sum())}, good on some days only \"\n          f\"{int((g.any(0) & ~g.all(0)).sum())}, never good {int((~g.any(0)).sum())}; events {int((ev.subject == s).sum())}, \"\n          f\"days {sorted(ev.day[ev.subject == s].unique())}\")\nprint(\"ECoG clock shifted (session start, s) for:\", ev.groupby(\"path\").offset.first()[lambda x: x > 0].round(1).to_dict())\nprint(\"feature ranges over all events:\")\nprint(ev[[\"day\", \"hour\", \"duration\", \"magnitude\", \"angle_folded\", \"onset_speed\", \"speech_ratio\", \"bimanual_ratio\",\n          \"bimanual_overlap\", \"bimanual_class\"]].describe().T[[\"min\", \"50%\", \"max\"]].round(3).to_string())\n\n# %% [markdown]\n# ### Band power and model fits\n#\n# Models are fitted at every electrode, good or not; the main results use the electrodes marked\n# good on every day of the subject, and the code's inclusion of bad electrodes is a variant. One\n# model per subject, electrode and band; the seed of each model's splits is fixed from its\n# subject, electrode and band.\n\n# %%\nBANDS = {\"LFB\": 0, \"HFB\": 2}        # columns of ajile.BAND_COLS: band mean with baseline (Methods)\nsubject_files = {s: list(A.path[A.subject == s]) for s in SUBJECTS}\nfile_jobs = [(p, ev.asset_id[ev.path == p].iloc[0], (ev.start_time - ev.offset)[ev.path == p].to_numpy(), None, True) for p in A.path]\nDESIGN = {}\n\n\ndef make_models(s, spec_s):\n    A_s = A[A.subject == s].reset_index(drop=True)\n    ev_s = ev[ev.subject == s].reset_index(drop=True)\n    ok = np.concatenate([spec_s[p][\"ok\"] for p in A_s.path])\n    rej1, _, _ = ajile.rejection(ev_s.assign(ok=ok), A_s, meta, spec_s, [s])\n    keep = (ev_s.false_pos == 0).to_numpy() & ok & ~rej1\n    e = ev_s[keep]\n    X, groups = ajile.design(e)\n    band = np.concatenate([spec_s[p][\"band\"] for p in A_s.path])[keep]\n    DESIGN[s] = dict(X=X, groups=groups, n=int(keep.sum()), rejected=int((ok & ~rej1 == False).sum()))\n    jobs = []\n    for c in range(band.shape[1]):\n        for b, j in BANDS.items():\n            seed = zlib.crc32(f\"{s}-{c}-{b}\".encode())\n            jobs.append(((s, c, b), X, groups, band[:, c, j], e.day.to_numpy(), seed, {\"n_splits\": 200, \"test_frac\": 0.1}))\n    return jobs\n\n\nt = time.time()\nspec, fits, timing = ajile.regression_pipeline(file_jobs, subject_files, make_models, workers=12)\nprint(f\"band power for {sum(len(j[2]) for j in file_jobs)} events and {len(fits)} models in {time.time() - t:.0f} s; \"\n      f\"subjects read at (s): { {k: round(v) for k, v in timing['subjects_read_at'].items()} }\")\nprint(\"events per subject used:\", {s: d[\"n\"] for s, d in DESIGN.items()})\nprint(\"columns of the design:\", {s: len(d[\"groups\"]) for s, d in DESIGN.items()})\n\n# %%\nFEATS = ajile.FEATURES\nrows = []\nfor (s, c, b), r in fits.items():\n    g = DESIGN[s][\"groups\"]\n    coef = r[\"coef\"]\n    cf = {}\n    for f in FEATS:\n        m = g == f\n        cf[f] = np.std(coef[m]) if f in (\"day\", \"time_of_day\") else coef[m][0]\n    rows.append(dict(subject=s, ch=c, band=b, good=bool(good_all[s][c]), r2=r[\"r2\"], n=r[\"n\"],\n                     n_selected=len(r[\"selected\"]), **{\"sel_\" + f: f in r[\"selected\"] for f in FEATS},\n                     **{\"dm_\" + f: r[\"delta_methods\"][f] for f in FEATS}, **{\"dc_\" + f: r[\"delta_code\"][f] for f in FEATS},\n                     **{\"coef_\" + f: cf[f] for f in FEATS}))\nR = pd.DataFrame(rows)\nprint(f\"models: {len(R)}; at good electrodes {int(R.good.sum())}; with nothing selected {int((R.n_selected == 0).sum())}; \"\n      f\"failed fits {len(DESIGN) and sum(1 for s in SUBJECTS for c in range(len(good_all[s])) for b in BANDS if (s, c, b) not in fits)}\")\nprint(\"full-model test R2 at good electrodes, by band:\")\nprint(R[R.good].groupby(\"band\").r2.describe().round(3).to_string())\nprint(\"R2 range over all models:\", R.r2.min().round(3), \"to\", R.r2.max().round(3))\nLFB_R2 = R[R.band == \"LFB\"].set_index([\"subject\", \"ch\"]).r2\nR[\"r2_lfb\"] = [LFB_R2[(s, c)] for s, c in zip(R.subject, R.ch)]\nprint(\"models with R2 > 0.05, good electrodes:\", R[R.good & (R.r2 > 0.05)].groupby(\"band\").size().to_dict())\nprint(\"by subject (good, R2 > 0.05):\")\nprint(R[R.good & (R.r2 > 0.05)].groupby([\"subject\", \"band\"]).size().unstack(fill_value=0).T.to_string())\n\n# %% [markdown]\n# > fig6-r2-at-most-025: All regression models explain at most 25% of the variance of withheld\n# > single-event power.\n\n# %% tags=claim:fig6-r2-at-most-025\nbest = R[R.good].sort_values(\"r2\", ascending=False).head(5)\nprint(\"largest split-averaged R2, good electrodes:\")\nprint(best[[\"subject\", \"ch\", \"band\", \"r2\", \"n_selected\"]].round(4).to_string(index=False))\nprint(f\"largest R2 at good electrodes: {R[R.good].r2.max():.4f}; at most 0.275: {R[R.good].r2.max() <= 0.275}\")\nprint(f\"variant, all electrodes (bad included): {R.r2.max():.4f}\")\nprint(\"largest per subject and band (good):\")\nprint(R[R.good].groupby([\"subject\", \"band\"]).r2.max().unstack().round(3).T.to_string())\nel0 = pd.concat([meta[p][\"electrodes\"].assign(subject=s) for s in SUBJECTS for p in A.path[A.subject == s][:1]])\nprint(\"for reference only, the R2 columns stored in the dataset's electrode table (not used for the outcome):\",\n      \"low_freq_R2 max\", round(el0.low_freq_R2.max(), 3), \"; high_freq_R2 max\", round(el0.high_freq_R2.max(), 3))\ncmp = R[R.good].pivot_table(index=[\"subject\", \"ch\"], columns=\"band\", values=\"r2\")\nel0 = el0.reset_index().rename(columns={\"index\": \"ch\"}).set_index([\"subject\", \"ch\"])\nj = cmp.join(el0[[\"low_freq_R2\", \"high_freq_R2\"]])\nprint(\"correlation of these R2 with the stored columns (good electrodes): LFB\",\n      round(j.LFB.corr(j.low_freq_R2), 3), \"; HFB\", round(j.HFB.corr(j.high_freq_R2), 3))\n\n# %% [markdown]\n# > fig6b-best-models-sensorimotor: Regression models with the highest withheld R2 are mainly at\n# > electrodes over frontoparietal sensorimotor areas, for both bands.\n#\n# (a) Each electrode in the region of the eight with its largest weight in the paper's projection\n# matrix. (b) R2 projected onto the eight regions with the projection weights (electrodes good on\n# every day, each region renormalised), then averaged over subjects.\n\n# %% tags=claim:fig6b-best-models-sensorimotor\nFP5 = [\"Frontal_Mid\", \"Precentral\", \"Postcentral\", \"Parietal_Inf\", \"SupraMarginal\"]\nSM3 = [\"Precentral\", \"Postcentral\", \"Parietal_Inf\"]\nTEMP = [\"Temporal_Sup\", \"Temporal_Mid\", \"Temporal_Inf\"]\nassign, wmax = {}, {}\nfor s in SUBJECTS:\n    W8 = W_all[s][ajile.REGIONS].to_numpy(float)\n    for c in range(len(W8)):\n        assign[(s, c)] = ajile.REGIONS[int(np.argmax(W8[c]))]\n        wmax[(s, c)] = W8[c].max()\nR[\"region\"] = [assign[(s, c)] for s, c in zip(R.subject, R.ch)]\nR[\"wmax\"] = [wmax[(s, c)] for s, c in zip(R.subject, R.ch)]\nfor band in BANDS:\n    g = R[R.good & (R.band == band)]\n    hi = g[g.r2 > 0.05]\n    frac = hi.region.isin(FP5).mean() if len(hi) else np.nan\n    med_sm, med_t = g[g.region.isin(SM3)].r2.median(), g[g.region.isin(TEMP)].r2.median()\n    print(f\"{band} (a): electrodes with R2 > 0.05: {len(hi)}, in the five frontoparietal regions {frac:.3f}; \"\n          f\"median R2 sensorimotor {med_sm:.4f} against temporal {med_t:.4f}\")\n    print(\"    counts of R2 > 0.05 by region:\", hi.region.value_counts().to_dict())\n    print(\"    median R2 by region:\", g.groupby(\"region\").r2.median().round(4).to_dict())\n    lowk = g[g.wmax < 1e-6]\n    print(f\"    electrodes whose largest weight is below 1e-6 (assigned anyway): {len(lowk)}; without them, fraction in \"\n          f\"frontoparietal {hi[hi.wmax >= 1e-6].region.isin(FP5).mean():.3f}\")\n    proj_r2 = []\n    for s in SUBJECTS:\n        P = ajile.projection(W_all[s], good_all[s])\n        r2 = g[g.subject == s].set_index(\"ch\").r2.reindex(range(len(P))).fillna(0).to_numpy()\n        proj_r2.append(np.nan_to_num(P, nan=0).T @ r2 / np.where(np.isnan(P).all(0), np.nan, 1))\n    pr = pd.Series(np.nanmean(proj_r2, 0), index=ajile.REGIONS).sort_values(ascending=False)\n    print(f\"{band} (b): projected R2 averaged over subjects:\", pr.round(4).to_dict())\n    print(f\"    top three {list(pr.index[:3])}, all among the five frontoparietal: {set(pr.index[:3]) <= set(FP5)}\")\n\n# %% [markdown]\n# > fig6c-angle-and-day-most-informative: Reach angle and day of recording are the most\n# > informative features for single-event power, especially for low-frequency power.\n\n# %% tags=claim:fig6c-angle-and-day-most-informative\ndef ranking(df, prefix):\n    return df[[prefix + f for f in FEATS]].median().rename(lambda c: c[len(prefix):]).sort_values(ascending=False)\n\n\nvariants = {\n    \"main (Methods Delta R2, good, R2 > 0.05 per band)\": (lambda d, b: d[d.good & (d.band == b) & (d.r2 > 0.05)], \"dm_\"),\n    \"code Delta R2 (test events shuffled too)\": (lambda d, b: d[d.good & (d.band == b) & (d.r2 > 0.05)], \"dc_\"),\n    \"selection by LFB R2 for both bands\": (lambda d, b: d[d.good & (d.band == b) & (d.r2_lfb > 0.05)], \"dm_\"),\n    \"bad electrodes included\": (lambda d, b: d[(d.band == b) & (d.r2 > 0.05)], \"dm_\"),\n}\nfor name, (fsel, pre) in variants.items():\n    for band in BANDS:\n        d = fsel(R, band)\n        rk = ranking(d, pre)\n        print(f\"{name}, {band} (n={len(d)}): \" + \", \".join(f\"{k} {v:.4f}\" for k, v in rk.items()))\n        print(f\"    top two: {list(rk.index[:2])}\")\nfig, axs = plt.subplots(1, 2, figsize=(12, 4), sharey=True)\nfor ax, band in zip(axs, BANDS):\n    d = R[R.good & (R.band == band) & (R.r2 > 0.05)]\n    ax.boxplot([d[\"dm_\" + f] for f in FEATS], showfliers=False)\n    ax.set_xticks(range(1, 11), FEATS, rotation=60, ha=\"right\")\n    ax.set_title(f\"{band}, n={len(d)}\")\naxs[0].set_ylabel(\"Delta R2\")\nplt.tight_layout()\nplt.show()\nvals = R[R.good & (R.r2 > 0.05)][[\"dm_\" + f for f in FEATS]]\nprint(f\"Delta R2 range over the plotted models: {vals.min().min():.4f} to {vals.max().max():.4f} (outliers not drawn)\")\n\n# %% [markdown]\n# > extfig6-2-angle-most-retained: Reach angle is the feature most often retained by forward\n# > selection in sensorimotor regions, followed by reach duration, reach magnitude, bimanual ratio\n# > and bimanual overlap.\n\n# %% tags=claim:extfig6-2-angle-most-retained\nret = {}\nfor band in BANDS:\n    per_s = []\n    for s in SUBJECTS:\n        d = R[(R.subject == s) & (R.band == band)].set_index(\"ch\").reindex(range(len(good_all[s])))\n        S = d[[\"sel_\" + f for f in FEATS]].astype(float).to_numpy()\n        P = np.nan_to_num(ajile.projection(W_all[s], good_all[s]), nan=0)\n        valid = P.sum(0) > 0\n        v = (P.T @ np.nan_to_num(S)) / np.where(valid, 1, np.nan)[:, None]\n        per_s.append(v)\n    ret[band] = pd.DataFrame(np.nanmean(per_s, 0), index=ajile.REGIONS, columns=FEATS)\n    print(f\"{band}: retention probability, projected and averaged over subjects\")\n    print(ret[band].round(3).to_string())\nangle_top = {(b, r): ret[b].loc[r].idxmax() == \"reach_angle\" for b in BANDS for r in SM3}\nprint(\"reach angle highest in each sensorimotor region and band:\", angle_top, \"->\", all(angle_top.values()))\norder = [\"reach_duration\", \"reach_magnitude\", \"bimanual_ratio\", \"bimanual_overlap\"]\nfor name, regs in ((\"(a) three sensorimotor regions, both bands\", SM3), (\"(b) all eight regions, both bands\", ajile.REGIONS)):\n    avg = pd.concat([ret[b].loc[regs] for b in BANDS]).mean().sort_values(ascending=False)\n    print(f\"{name}: \" + \", \".join(f\"{k} {v:.3f}\" for k, v in avg.items()))\n    print(f\"    ranked second to fifth: {list(avg.index[1:5])}; the legend's order: {list(avg.index[1:5]) == order}\")\n\n# %% [markdown]\n# > fig6d-upward-reaches-enhance-pattern: Upward reaches are associated with lower low-frequency\n# > power and higher high-frequency power.\n\n# %% tags=claim:fig6d-upward-reaches-enhance-pattern\nfor name, fsel in ((\"main\", lambda d, b: d[d.good & (d.band == b) & (d.r2 > 0.05)]),\n                   (\"selection by LFB R2\", lambda d, b: d[d.good & (d.band == b) & (d.r2_lfb > 0.05)]),\n                   (\"bad electrodes included\", lambda d, b: d[(d.band == b) & (d.r2 > 0.05)])):\n    out = []\n    for band in BANDS:\n        d = fsel(R, band)\n        out.append(f\"{band} median angle coefficient {d.coef_reach_angle.median():+.4f} (n={len(d)}, \"\n                   f\"{(d.coef_reach_angle < 0).mean():.2f} negative, {(d.coef_reach_angle == 0).mean():.2f} zero)\")\n    print(f\"{name}: \" + \"; \".join(out))\nd = R[R.good & (R.r2 > 0.05)]\nprint(\"by subject, median angle coefficient (main):\")\nprint(d.groupby([\"subject\", \"band\"]).coef_reach_angle.median().unstack().round(4).T.to_string())\n\n# %% [markdown]\n# > fig6d-angle-and-day-largest-coefficients: Reach angle and day of recording have the largest\n# > coefficient magnitudes among the features, and the SD of the recording-day coefficients is\n# > large.\n\n# %% tags=claim:fig6d-angle-and-day-largest-coefficients\nfor name, fsel in ((\"main\", lambda d, b: d[d.good & (d.band == b) & (d.r2 > 0.05)]),\n                   (\"selection by LFB R2\", lambda d, b: d[d.good & (d.band == b) & (d.r2_lfb > 0.05)]),\n                   (\"bad electrodes included\", lambda d, b: d[(d.band == b) & (d.r2 > 0.05)])):\n    for band in BANDS:\n        d = fsel(R, band)\n        C = d[[\"coef_\" + f for f in FEATS]].rename(columns=lambda c: c[5:])\n        ra = C.abs().median().sort_values(ascending=False)\n        rb = C.median().abs().sort_values(ascending=False)\n        print(f\"{name}, {band} (n={len(d)}):\")\n        print(\"   (a) median |coef|: \" + \", \".join(f\"{k} {v:.4f}\" for k, v in ra.items()))\n        print(\"   (b) |median coef|: \" + \", \".join(f\"{k} {v:.4f}\" for k, v in rb.items()))\n        print(f\"   top two (a) {list(ra.index[:2])}; (b) {list(rb.index[:2])}\")\n\n# %% [markdown]\n# ## Summary\n#\n# (Written after the run; see the attempt record.)\n\n# %%\nprint(f\"notebook ran in {(time.time() - T0) / 60:.1f} min\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build/nb2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && date -u && AJILE_SUBJECTS=9 MPLBACKEND=Agg timeout 1500 python $TMPDIR/build/devrun.py $TMPDIR/build/nb2.py > $TMPDIR/dev_nb2.log 2>&1; echo exit $?; date -u; grep -n "Traceback" -A 14 $TMPDIR/dev_nb2.log | tail -16
```

```
Fri Oct 23 16:25:27 UTC 2026
exit 0
Fri Oct 23 16:29:22 UTC 2026
```

**Agent calls Bash**

```bash
grep -v Warning $TMPDIR/dev_nb2.log | grep -v "^  " | cut -c1-300 | head -120
```

```
5 files, 211 events, 60 Figshare false positives; loaded in 17 s
S09: 126 channels, good on every day 94, good on some days only 31, never good 1; events 211, days [np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)]
ECoG clock shifted (session start, s) for: {}
feature ranges over all events:
day                3.000   5.000    7.000
hour               4.959  11.715   22.704
duration           0.300   1.267    3.267
magnitude          4.071  43.547  195.319
angle_folded     -89.782  17.403   89.728
onset_speed        3.489  32.256  374.187
speech_ratio       0.094   0.341    0.709
bimanual_ratio     0.000   0.108    0.933
bimanual_overlap   0.000   0.267    2.567
bimanual_class     0.000   1.000    1.000
band power for 211 events and 252 models in 216 s; subjects read at (s): {9: 75}
events per subject used: {9: 150}
columns of the design: {9: 16}
models: 252; at good electrodes 188; with nothing selected 0; failed fits 0
full-model test R2 at good electrodes, by band:
band                                                        
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && sed -n 1,60p tools/entry.py; grep -n "def check" -A 80 tools/entry.py | grep -n -i "embed\|number\|array\|forbid\|reject\|pattern\|re\.compile" | head -30
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
[... 39 more lines not kept]
```

**Agent**

Adding the two link claims to the claims file (the only claims an author writes), placed before `checks:`:

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000055/10.1523-eneuro.0007-21.2021.yaml",
 "old_string": "checks:\n- date: 2026-10-23\n  kind: agent",
 "new_string": "- id: figshare-event-link\n  kind: link\n  statement: The paper's curated epoch files on Figshare (10.6084/m9.figshare.12115728.v1) hold the\n    same events as the dataset, so their false-positive flags can be applied to the dataset's\n    events.\n  source: Added by the author of attempt 000055-peterson-2021-01 (protocol, Author, step 4)\n  inferred: A registry check, not a finding of the paper. The dataset holds no false-positive flag;\n    reading (b) of fig2-event-counts needs it, and the paper's code reads it from these files.\n  data: with_labels\n  criterion: Records are matched on the event time, the Figshare event_timestamp (ms from the start\n    of the file) against the dataset's reach start_time. The link holds (reproduced) when every\n    dataset event has exactly one Figshare record of the same subject and day with that time, and\n    the features both hold agree (reach magnitude and angle as stored; duration, onset speed and\n    bimanual overlap after converting frames at 30 frames per second; bimanual class, bimanual\n    ratio and speech ratio) to within 1e-6. Partially reproduced when at least 95% of events match.\n- id: figshare-roi-link\n  kind: link\n  statement: The paper's projection matrices from electrodes to AAL regions on Figshare\n    (10.6084/m9.figshare.12114408.v1) have one row per electrode of the dataset, in the dataset's\n    order.\n  source: Added by the author of attempt 000055-peterson-2021-01 (protocol, Author, step 4)\n  inferred: A registry check, not a finding of the paper. The projection matrices are the paper's\n    output of the AAL projection step the opening comment describes; the AAL atlas through the\n    Measure Projection Toolbox could not be fetched here, so the regions claims use them.\n  data: with_inputs\n  criterion: Per subject, the number of weight rows is compared with the dataset's channels. Rows\n    carry no identifier, so the order is checked through positions. For each electrode, the\n    weighted mean of the region centroids of the Figshare centroid file is compared with the\n    electrode's MNI position in the dataset, mirrored to the left. The link holds (reproduced)\n    when every subject has one row per channel, any extra rows are all zero, and the median distance\n    is below the smallest of 200 row-shuffled distances for every subject. The eight regions with\n    density averaged over subjects above 3 are also compared with the eight of the opening comment.\n    Partially reproduced when this holds for 10 or 11 subjects.\nchecks:\n- date: 2026-10-23\n  kind: agent"
}
```

```
The file claims/000055/10.1523-eneuro.0007-21.2021.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py --help 2>&1 | head -5; python -c "
import json,yaml,jsonschema
s=json.load(open('schemas/claims.schema.json')); d=yaml.safe_load(open('claims/000055/10.1523-eneuro.0007-21.2021.yaml'))
v=jsonschema.Draft202012Validator(s); print([e.message for e in v.iter_errors(d)][:5])"
```

```
Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
['{\'id\': \'figshare-event-link\', \'kind\': \'link\', \'statement\': "The paper\'s curated epoch files on Figshare (10.6084/m9.figshare.12115728.v1) hold the same events as the dataset, so their false-positive flags can be applied to the dataset\'s events.", \'source\': \'Added by the author of attempt 000055-peterson-2021-01 (protocol, Author, step 4)\', \'inferred\': "A registry check, not a finding of the paper. The dataset holds no false-positive flag; reading (b) of fig2-event-counts needs it, and the paper\'s code reads it from these files.", \'data\': \'with_labels\', \'criterion\': "Records are matched on the event time, the Figshare event_timestamp (ms from the start of the file) against the dataset\'s reach start_time. The link holds (reproduced) when every dataset event has exactly one Figshare record of the same subject and day with that time, and the features both hold agree (reach magnitude and angle as stored; duration, onset speed and bimanual overlap after converting frames at 30 frames per second; bimanual class, bimanual ratio and speech ratio) to within 1e-6. Partially reproduced when at least 95% of events match."} should not be valid under {\'required\': [\'inferred\']}', '{\'id\': \'figshare-roi-link\', \'kind\': \'link\', \'statement\': "The paper\'s projection matrices from electrodes to AAL regions on Figshare (10.6084/m9.figshare.12114408.v1) have one row per electrode of the dataset, in the dataset\'s order.", \'source\': \'Added by the author of attempt 000055-peterson-2021-01 (protocol, Author, step 4)\', \'inferred\': "A registry check, not a finding of the paper. The projection matrices are the paper\'s output of the AAL projection step the opening comment describes; the AAL atlas through the Me
[... 1 more lines not kept]
```

**Agent**

Link claims must not carry `inferred`. Removing those lines (the date message is from parsing the existing `checks` date and was already there):

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/000055/10.1523-eneuro.0007-21.2021.yaml'
s=open(p).read()
import re
s=s.replace('''  inferred: A registry check, not a finding of the paper. The dataset holds no false-positive flag;
    reading (b) of fig2-event-counts needs it, and the paper's code reads it from these files.
''','')
s=s.replace('''  inferred: A registry check, not a finding of the paper. The projection matrices are the paper's
    output of the AAL projection step the opening comment describes; the AAL atlas through the
    Measure Projection Toolbox could not be fetched here, so the regions claims use them.
''','')
open(p,'w').write(s)
EOF
python -c "
import json,yaml,jsonschema
s=json.load(open('schemas/claims.schema.json')); d=yaml.safe_load(open('claims/000055/10.1523-eneuro.0007-21.2021.yaml'))
v=jsonschema.Draft202012Validator(s); print([e.message[:200] for e in v.iter_errors(d)][:5])"; git diff --stat
```

```
["datetime.date(2026, 10, 23) is not of type 'string'"]
 claims/000055/10.1523-eneuro.0007-21.2021.yaml | 28 ++++++++++++++++++++++++++
 1 file changed, 28 insertions(+)
```

**Agent**

Now a tweak to the discussion cell (report the events whose raw band power is below 0 dB, which points to zeroed ECoG), then the entry files:

**Agent calls Bash**

```bash
cd $TMPDIR/build && python - <<'EOF'
s=open('nb1.py').read()
s=s.replace('''print(dc2.round(2).to_string(index=False))
print(f"largest day-to-day change''','''print(dc2.round(2).to_string(index=False))
low = bp[(bp.lfb_raw < 0) | (bp.hfb_raw < 0)]
print(f"events whose precentral band power without baseline is below 0 dB (ECoG zeroed in the 0-0.5 s window): {len(low)} of {len(bp)}, "
      f"by subject {low.subject.value_counts().sort_index().to_dict()}; their lowest value {min(low.lfb_raw.min(), low.hfb_raw.min()) if len(low) else float('nan'):.0f} dB")
med = bp.groupby("subject")[["lfb_raw", "hfb_raw"]].median()
print(f"level without baseline as the median over events instead (uV): {med.min().min():.1f} to {med.max().max():.1f} dB")
print(f"largest day-to-day change''')
open('nb1.py','w').write(s)
EOF
cd entries/000055-peterson-2021 && cat > requirements.in <<'EOF'
aiohttp
fsspec
h5py
matplotlib
mne
numpy
pandas
remfile
requests
scikit-learn
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 000055-peterson-2021
type: reproduction
title: Behavioral and neural variability of naturalistic arm movements (Peterson et al. 2021)
description: Tests the findings of Peterson, Singh, Wang, Rao and Brunton (2021) on dandiset 000055
  (AJILE12), which holds the ECoG, pose and wrist movement events of the paper's 12 subjects over 55
  days. It covers the behavioural features of the events, the spectral power around movement onset
  by region and subject, its variation across days, and the regression of single-event power on
  behaviour. Two inputs come from the paper's Figshare project, the false-positive flags of the
  events and the projection matrices onto brain regions.
license: Apache-2.0
notebooks:
- path: reproduce_peterson_2021.ipynb
  title: Behaviour, links and spectral power (Figures 2 to 5, Table 1)
  runtime_minutes: 15
- path: reproduce_peterson_2021_regression.ipynb
  title: Regression of single-event power on behaviour (Figure 6)
  runtime_minutes: 20
helpers:
- ajile.py
related:
- id: dandi:000055/0.220127.0436
  relation: uses_data
- id: doi:10.1523/eneuro.0007-21.2021
  relation: reproduces
- id: doi:10.6084/m9.figshare.12114408.v1
  relation: uses_data
- id: doi:10.6084/m9.figshare.12115728.v1
  relation: uses_data
EOF
. $TMPDIR/dev/bin/activate; python $TMPDIR/build/conv.py $TMPDIR/build/nb1.py reproduce_peterson_2021.ipynb && python $TMPDIR/build/conv.py $TMPDIR/build/nb2.py reproduce_peterson_2021_regression.ipynb && echo "# placeholder" > README.md && cd  && python tools/entry.py lock entries/000055-peterson-2021 2>&1 | tail -3 && python tools/entry.py check entries/000055-peterson-2021 2>&1 | tail -15
```

```
wrote entries/000055-peterson-2021/requirements.lock.txt
0 error(s)
```

**Agent**

Check passes with 0 errors. Starting the full run of both notebooks from the locked environment (expected about 35 to 40 min):

**Agent calls Bash**

```bash
date -u; python tools/entry.py all entries/000055-peterson-2021 2>&1 | tail -20; date -u
```

```
Fri Oct 23 16:30:35 UTC 2026
Installed kernelspec registry-000055-peterson-2021 in executed/000055-peterson-2021/.venv/share/jupyter/kernels/registry-000055-peterson-2021
0 error(s)
pass  reproduce_peterson_2021.ipynb  (1001 s)
pass  reproduce_peterson_2021_regression.ipynb  (1722 s)
Fri Oct 23 17:16:17 UTC 2026
```

**Agent**

Both notebooks pass: 16.7 min and 28.7 min. The regression notebook is close to the 30-min limit, so I'll keep that in mind. Reading the outputs of notebook 1:

**Agent calls Bash**

```bash
cd executed/000055-peterson-2021 && ls; python - <<'EOF' > $TMPDIR/out1.txt
import nbformat
nb=nbformat.read('reproduce_peterson_2021.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print(f"=== cell {i} {c.metadata.get('tags','')}")
    for o in c.outputs:
        if o.output_type=='stream' and o.name=='stdout': print(o.text)
        elif o.output_type=='error': print('ERROR', o.ename, o.evalue)
EOF
wc -l $TMPDIR/out1.txt; sed -n 1,140p $TMPDIR/out1.txt | cut -c1-260
```

```
reproduce_peterson_2021.ipynb
reproduce_peterson_2021_regression.ipynb
result.json
702 /tmp/claude-1001/out1.txt
=== cell 1 
55 assets in the version, 55 read; 55 Figshare epoch files; loaded in 44 s

=== cell 3 ['sanity']
Assets per subject and the days they hold (from the file names):
subject
1        [3, 4, 5, 7]
2        [3, 4, 5, 6]
3        [3, 4, 5, 6]
4     [3, 4, 5, 6, 7]
5           [3, 4, 7]
6     [3, 4, 5, 6, 7]
7     [3, 4, 5, 6, 7]
8     [3, 4, 5, 6, 7]
9     [3, 4, 5, 6, 7]
10    [3, 4, 5, 6, 7]
[... 124 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 140,420p $TMPDIR/out1.txt | cut -c1-260
```

```
events outside the ECoG on the stored clock: 132 of 190; on the shifted clock: 0
sub-04_ses-3 stored   n=13 precentral LFB +0.35 dB (Wilcoxon p=0.19), HFB +0.19 dB (p=0.54)
sub-04_ses-3 shifted  n=13 precentral LFB -0.65 dB (Wilcoxon p=0.013), HFB -0.04 dB (p=0.79)
   events outside the ECoG on the stored clock: 22 of 35; on the shifted clock: 0
sub-06_ses-3 stored   n=40 precentral LFB +0.39 dB (Wilcoxon p=0.2), HFB +0.29 dB (p=0.25)
sub-06_ses-3 shifted  n=40 precentral LFB -1.69 dB (Wilcoxon p=7.2e-05), HFB +2.65 dB (p=1.6e-10)
   events outside the ECoG on the stored clock: 83 of 166; on the shifted clock: 0
(35 s)

=== cell 13 
spectral pass over 8088 events in 55 files: 863 s (slowest file 415 s)
events whose 10 s segment is outside the ECoG: 1

=== cell 15 ['sanity']
 subject  day   n  lfb_onset  lfb_pseudo  p_lfb  hfb_onset  hfb_pseudo  p_hfb  contrast
       1    3 156     -1.551      -0.034  0.000     -0.273       0.104  0.198      True
       1    4 196     -3.153      -0.061  0.000     -1.471       0.006  0.730      True
       1    5 199     -1.613       1.482  0.000      0.012       1.459  0.028      True
       1    7 190     -1.349      -0.124  0.001      0.056       0.012  0.473      True
       2    3  51     -0.292      -0.357  0.829     -0.044      -0.132  0.800     False
[... 260 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 420,702p $TMPDIR/out1.txt | cut -c1-300
```

```
=== cell 33 ['claim:extfig2-2-feature-correlations']
events set_b1 (n=6887): magnitude-duration r=0.259 (paper 0.26); magnitude-onset_speed r=0.562 (paper 0.56); duration-bimanual_overlap r=0.475 (paper 0.48); bimanual_overlap-bimanual_ratio r=0.508 (paper 0.51); bimanual_class-bimanual_ratio r=0.496 (paper 0.5); bimanual_overlap-bimanual_class r=0.60
   within 10%: [np.True_, np.True_, np.True_, np.True_, np.True_, np.True_] -> 6 of 6
events set_a (n=8088): magnitude-duration r=0.231 (paper 0.26); magnitude-onset_speed r=0.609 (paper 0.56); duration-bimanual_overlap r=0.505 (paper 0.48); bimanual_overlap-bimanual_ratio r=0.501 (paper 0.51); bimanual_class-bimanual_ratio r=0.494 (paper 0.5); bimanual_overlap-bimanual_class r=0.598
   within 10%: [np.False_, np.True_, np.True_, np.True_, np.True_, np.True_] -> 5 of 6
events set_b2 (n=2873): magnitude-duration r=0.317 (paper 0.26); magnitude-onset_speed r=0.502 (paper 0.56); duration-bimanual_overlap r=0.513 (paper 0.48); bimanual_overlap-bimanual_ratio r=0.464 (paper 0.51); bimanual_class-bimanual_ratio r=0.443 (paper 0.5); bimanual_overlap-bimanual_class r=0.56
   within 10%: [np.False_, np.False_, np.True_, np.True_, np.False_, np.True_] -> 3 of 6

=== cell 35 ['claim:fig2-days-and-waking']
day        3    4    5    6    7
subject                         
1        121  166  186    0  186
2         38   66   56   44    0
3        186  168  127   99    0
4         19   42   32   60  115
5         35   39    0    0  125
6        157  184  183  163  164
7         70   77  173  181  170
8        179  174  133  185  178
9         11   13   83   22   21
[... 261 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF' > $TMPDIR/out2.txt
import nbformat
nb=nbformat.read('reproduce_peterson_2021_regression.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print(f"=== cell {i} {c.metadata.get('tags','')}")
    for o in c.outputs:
        if o.output_type=='stream' and o.name=='stdout': print(o.text)
        elif o.output_type=='error': print('ERROR', o.ename, o.evalue)
EOF
cut -c1-300 $TMPDIR/out2.txt | grep -v "^S[0-9][0-9]: " | head -150
```

```
=== cell 1 
55 files, 8088 events, 1157 Figshare false positives; loaded in 42 s

=== cell 2 ['sanity']
ECoG clock shifted (session start, s) for: {'sub-01/sub-01_ses-7_behavior+ecephys.nwb': 30682.4, 'sub-04/sub-04_ses-3_behavior+ecephys.nwb': 30048.3, 'sub-06/sub-06_ses-3_behavior+ecephys.nwb': 29240.6}
feature ranges over all events:
                     min      50%       max
day                3.000    5.000     7.000
hour               0.011   14.465    23.996
duration           0.233    1.100     3.933
magnitude          3.927   87.687   680.562
angle_folded     -89.936   39.038    89.998
onset_speed        0.000  103.494  1492.070
speech_ratio       0.000    0.302     0.827
bimanual_ratio     0.000    0.137     1.000
bimanual_overlap   0.000    0.467     3.833
bimanual_class     0.000    1.000     1.000

=== cell 4 
band power for 8088 events and 2368 models in 1673 s; subjects read at (s): {8: 479, 6: 484, 12: 493, 11: 535, 3: 554, 1: 567, 10: 604, 7: 613, 4: 651, 2: 668, 5: 671, 9: 697}
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && python - <<'EOF'
s=open('ajile.py').read()
# per-bin power for rejection b3
s=s.replace('''    if light:
        return wa, wh, band, None, None, None
    # clock check''','''    # per 0.1 s bin from -1.5 s, the linear power averaged over frequencies (rejection b3)
    zb = win(KEEP[0], KEEP[1])
    binpow = (10 ** (p[:, :, zb] / 10)).mean(1).astype(np.float32)
    if light:
        return wa, wh, band, None, None, binpow
    # clock check''')
s=s.replace('''    roi = None if proj is None else np.einsum("cr,cft->rft", proj, pb[:, :, kmask])
    return wa, wh, band, ctrl.astype(np.float32), roi, t[kmask]''','''    roi = None if proj is None else np.einsum("cr,cft->rft", proj, pb[:, :, kmask])
    return wa, wh, band, ctrl.astype(np.float32), roi, (t[kmask], binpow)''')
s=s.replace('''        wa, wh, band, ctrl, roi, tb = segment_measures(x, proj, light)
        res["psd_all"][i], res["psd_hf"][i], res["band"][i] = wa, wh, band''','''        wa, wh, band, ctrl, roi, extra = segment_measures(x, proj, light)
        tb, binpow = extra if isinstance(extra, tuple) else (None, extra)
        if "binpow" not in res:
            res["binpow"] = np.full((ne,) + binpow.shape, np.nan, np.float32)
        res["binpow"][i] = binpow
        res["psd_all"][i], res["psd_hf"][i], res["band"][i] = wa, wh, band''')
s=s.replace('''        res["tbins"] = tb
        res["ok"][i] = True''','''        if tb is not None:
            res["tbins"] = tb
        res["ok"][i] = True''')
s=s.replace('''      'ctrl': (events, channels, 2), LFB and HFB means around the pseudo-onset CTRL;''','''      'ctrl': (events, channels, 2), LFB and HFB means around the pseudo-onset CTRL;
      'binpow': (events, channels, bins), power averaged over frequencies per 0.1 s bin from
      -1.5 s (to 1.5 s, or 0.8 s when light);''')
# rejection b3
s=s.replace('''    (b2) the same on each good electrode; a segment fails when any good electrode fails."""
    rej1 = np.zeros(len(ev), bool)''','''    (b2) the same on each good electrode; a segment fails when any good electrode fails.
    (b3) as (b1), and also a segment whose Morlet power averaged over good electrodes and
    frequencies is below 0 dB in any 0.1 s bin from -1.5 s on (ECoG zeroed by the preprocessing
    in the analysed window). Returns (rej_b1, rej_b2, psd_db, rej_b3)."""
    rej3 = np.zeros(len(ev), bool)
    rej1 = np.zeros(len(ev), bool)''')
s=s.replace('''            rej2[idx] = ok & ((np.min(db_all, 1) < 0) | np.any(db_hf > mu_c + 3 * sd_c, axis=1))
    return rej1, rej2, psd_db''','''            rej2[idx] = ok & ((np.min(db_all, 1) < 0) | np.any(db_hf > mu_c + 3 * sd_c, axis=1))
            bp = np.concatenate([spec[p]["binpow"] for p in paths])
            gm = np.nansum(np.where(good[:, :, None], bp, 0), 1) / good.sum(1)[:, None]
            low = np.nanmin(10 * np.log10(gm), 1) < 0
            rej3[idx] = rej1[idx] | (ok & low)
    return rej1, rej2, psd_db, rej3''')
# warm start for shuffled refits
s=s.replace('''            hs = HuberRegressor().fit(Xtr, y[tr])''','''            # warm start from the unshuffled fit: the Huber objective is convex, so the optimum is
            # the same; it only shortens the optimisation
            hs = HuberRegressor(warm_start=True)
            hs.coef_, hs.intercept_, hs.scale_ = h.coef_.copy(), h.intercept_, h.scale_
            hs.fit(Xtr, y[tr])''')
open('ajile.py','w').write(s)
EOF
grep -n "binpow\|rej3\|warm" ajile.py | head -20
```

```
288:    binpow = (10 ** (p[:, :, zb] / 10)).mean(1).astype(np.float32)
290:        return wa, wh, band, None, None, binpow
297:    return wa, wh, band, ctrl.astype(np.float32), roi, (t[kmask], binpow)
309:      'binpow': (events, channels, bins), power averaged over frequencies per 0.1 s bin from
348:        tb, binpow = extra if isinstance(extra, tuple) else (None, extra)
349:        if "binpow" not in res:
350:            res["binpow"] = np.full((ne,) + binpow.shape, np.nan, np.float32)
351:        res["binpow"][i] = binpow
548:            # warm start from the unshuffled fit: the Huber objective is convex, so the optimum is
550:            hs = HuberRegressor(warm_start=True)
639:    rej3 = np.zeros(len(ev), bool)
662:            bp = np.concatenate([spec[p]["binpow"] for p in paths])
665:            rej3[idx] = rej1[idx] | (ok & low)
666:    return rej1, rej2, psd_db, rej3
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; grep -n "warm_start" -A3 $(python -c "import sklearn.linear_model._huber as h;print(h.__file__)") | head -20; cd entries/000055-peterson-2021 && python - <<'EOF'
s=open('ajile.py').read()
s=s.replace('''    f.close()
    res["seconds"] = time.time() - t_start
    return res''','''    f.close()
    if "binpow" not in res:
        res["binpow"] = np.full((ne, nch, 31), np.nan, np.float32)
    res["seconds"] = time.time() - t_start
    return res''')
open('ajile.py','w').write(s)
EOF
cd $TMPDIR && OMP_NUM_THREADS=1 python - <<'EOF'
import sys,time; sys.path.insert(0,'entries/000055-peterson-2021')
import ajile, numpy as np, pandas as pd
rng=np.random.default_rng(0); n=600
ev=pd.DataFrame(dict(day=rng.integers(3,8,n),hour=rng.uniform(0,24,n),duration=rng.uniform(.3,3,n),magnitude=rng.uniform(5,300,n),angle_folded=rng.uniform(-90,90,n),onset_speed=rng.uniform(1,500,n),speech_ratio=rng.uniform(0,1,n),bimanual_ratio=rng.uniform(0,1,n),bimanual_overlap=rng.uniform(0,2,n),bimanual_class=rng.integers(0,2,n).astype(float)))
X,g=ajile.design(ev); y=0.5*X[:,g=='reach_angle'][:,0]+rng.standard_t(3,n)
t=time.time(); r=ajile.fit_model(X,g,y,ev.day.values,1); print(time.time()-t, r['selected'], round(r['r2'],4), {k:round(v,4) for k,v in r['delta_methods'].items() if v})
x=rng.normal(size=(3,5000))*30; x[:,2000:2600]=0
w=ajile.segment_measures(x, None, True); print(w[5].shape, np.log10(w[5].min(1)))
w=ajile.segment_measures(x, None, False); print(w[5][1].shape, w[5][0][:3])
EOF
```

```
164:    warm_start : bool, default=False
165-        This is useful if the stored attributes of a previously used model
166-        has to be reused. If set to False, then the coefficients will
167-        be rewritten for every call to fit.
168:        See :term:`the Glossary <warm_start>`.
169-
170-    fit_intercept : bool, default=True
171-        Whether or not to fit the intercept. This can be set to False
--
255:        "warm_start": ["boolean"],
256-        "fit_intercept": ["boolean"],
257-        "tol": [Interval(Real, 0.0, None, closed="left")],
258-    }
--
266:        warm_start=False,
267-        fit_intercept=True,
268-        tol=1e-05,
269-    ):
--
273:        self.warm_start = warm_start
[... 4 more lines not kept]
```

**Agent**

Zeroed ECoG is detected (bin power about 1e-28). Confirming that sklearn's warm start actually reads the attributes I set:

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate; grep -n "if self.warm_start" -A8 $(python -c "import sklearn.linear_model._huber as h;print(h.__file__)")
```

```
310:        if self.warm_start and hasattr(self, "coef_"):
311-            parameters = np.concatenate((self.coef_, [self.intercept_, self.scale_]))
312-        else:
313-            if self.fit_intercept:
314-                parameters = np.zeros(X.shape[1] + 2)
315-            else:
316-                parameters = np.zeros(X.shape[1] + 1)
317-            # Make sure to initialize the scale parameter to a strictly
318-            # positive value:
```

**Agent**

Warm start reads `coef_`, `intercept_` and `scale_` as set. Now refactoring notebook 1's spectral section so every claim runs under both b1 and b3:

**Agent calls Bash**

```bash
cd $TMPDIR/build && grep -n "^# ## Spectral power\|^# %% \[markdown\]\|^# > \|^# ## Summary" nb1.py | sed -n '1,200p' | awk -F: '$1>560' | head -40
```

```
561:# > hours.
576:# %% [markdown]
577:# ## Spectral power (Figures 3 to 5, Table 1, Extended Data Figure 5-1)
628:# %% [markdown]
629:# > fig3-group-lfb-decrease-hfb-increase: At the group level, low-frequency power decreases and
630:# > high-frequency power increases at movement initiation in several cortical regions.
660:# %% [markdown]
661:# > fig3-sensorimotor-largest: Spectral power changes are largest in precentral, postcentral and
662:# > inferior parietal regions, and the three temporal regions show minimal movement-related
663:# > changes.
683:# %% [markdown]
684:# > fig3-lfb-more-widespread: Low-frequency power decreases are more spatially widespread than
685:# > high-frequency increases and are also present in supramarginal and superior temporal regions.
698:# %% [markdown]
699:# > fig4-precentral-subject-variability: In the precentral region every subject shows the
700:# > low/high-frequency pattern, but amplitudes and frequency bands vary; subjects 03, 06, 07, 08 and
701:# > 11 have increases up to 120 Hz, subjects 09 and 12 mainly at 60-80 Hz, and subjects 04 and 08
702:# > have narrower low-frequency decreases.
733:# %% [markdown]
762:# %% [markdown]
[... 18 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build/spectral.py",
 "content": "# %% [markdown]\n# ## Spectral power (Figures 3 to 5, Table 1, Extended Data Figure 5-1)\n#\n# Region power per event is the projection of each electrode's baseline-subtracted Morlet power\n# (dB) with the paper's weights. The group spectrogram and its mask follow the claims file:\n# per subject the median over events, the mean over subjects, the group median over -1.5 to -1 s\n# subtracted again; the null takes, for each frequency, each subject's baseline bins shuffled\n# and the median over subjects, about 2000 values per frequency; two-sided percentile p;\n# Benjamini-Hochberg over all frequency and time bins of the region at 0.05.\n#\n# Every spectral claim is run on the events of reading (b1) and of reading (b3) of the segment\n# rejection (see \"Event sets\"); (b2) leaves no events in four subjects and is not used here.\n\n# %%\nSETS = [\"set_b1\", \"set_b3\"]\nroi_ev = np.concatenate([spec[p][\"roi\"] for p in A.path])          # events, regions, freqs, bins\nbmask = (TB >= -1.5 - 1e-9) & (TB <= -1 + 1e-9)\nwin = (TB >= 0 - 1e-9) & (TB <= 0.5 + 1e-9)\nlo_f = (F >= 4) & (F <= 30)\nhi_f = (F >= 50) & (F <= 120)\nlf_i, hf_i = (F >= 8) & (F <= 32), (F >= 76) & (F <= 100)\n\n\ndef bh(p, q=0.05):\n    p = np.asarray(p).ravel()\n    o = np.argsort(p)\n    th = q * np.arange(1, len(p) + 1) / len(p)\n    ok = p[o] <= th\n    k = np.max(np.where(ok)[0]) + 1 if ok.any() else 0\n    sig = np.zeros(len(p), bool)\n    sig[o[:k]] = True\n    return sig\n\n\ndef group_spectrogram(setname, seed):\n    sel_ev = ev[setname].to_numpy()\n    subj_med = {s: np.nanmedian(roi_ev[sel_ev & (ev.subject == s).to_numpy()], 0) for s in SUBJECTS}\n    grp = np.mean([subj_med[s] for s in SUBJECTS], 0)\n    grp = grp - np.median(grp[:, :, bmask], axis=2, keepdims=True)\n    rng_mask = np.random.default_rng(seed)\n    S = np.stack([subj_med[s] for s in SUBJECTS])                    # subjects, regions, freqs, bins\n    nb = int(bmask.sum())\n    reps = int(np.ceil(2000 / nb))\n    masked = np.zeros_like(grp)\n    nsig = {}\n    for r in range(len(ajile.REGIONS)):\n        pvals = np.zeros(grp.shape[1:])\n        for fi in range(len(F)):\n            base = S[:, r, fi][:, bmask]                               # subjects x baseline bins\n            null = np.concatenate([np.median(np.stack([rng_mask.permutation(b) for b in base]), 0) for _ in range(reps)])\n            obs = grp[r, fi]\n            hi = (null[None, :] >= obs[:, None]).mean(1)\n            lo = (null[None, :] <= obs[:, None]).mean(1)\n            pvals[fi] = np.minimum(1, 2 * np.minimum(hi, lo))\n        sig = bh(pvals).reshape(pvals.shape)\n        masked[r] = np.where(sig, grp[r], 0)\n        nsig[ajile.REGIONS[r]] = int(sig.sum())\n    return dict(subj_med=subj_med, grp=grp, masked=masked, nsig=nsig, nnull=reps * nb)\n\n\nG = {SET: group_spectrogram(SET, seed=3) for SET in SETS}\nfor SET in SETS:\n    g = G[SET]\n    print(f\"{SET}: null values per frequency {g['nnull']}; significant bins per region (of {g['grp'].shape[1] * g['grp'].shape[2]}):\", g[\"nsig\"])\n    print(f\"   group spectrogram range (dB): {g['grp'].min():.2f} to {g['grp'].max():.2f}; time bins {TB[0]} to {TB[-1]} s\")\n\n# %% [markdown]\n# > fig3-group-lfb-decrease-hfb-increase: At the group level, low-frequency power decreases and\n# > high-frequency power increases at movement initiation in several cortical regions.\n\n# %% tags=claim:fig3-group-lfb-decrease-hfb-increase\nt0 = int(np.argmin(np.abs(TB)))\nthree = [\"precentral\", \"postcentral\", \"inferior parietal\"]\nF3 = {}\nfor SET in SETS:\n    masked, grp = G[SET][\"masked\"], G[SET][\"grp\"]\n    rows = []\n    for r, name in enumerate(ajile.REGIONS):\n        rows.append(dict(region=ajile.REGION_NAMES[name],\n                         a_low=masked[r][lo_f][:, win].mean(), a_high=masked[r][hi_f][:, win].mean(),\n                         b_low=masked[r][lo_f, t0].mean(), b_high=masked[r][hi_f, t0].mean(),\n                         unmasked_a_low=grp[r][lo_f][:, win].mean(), unmasked_a_high=grp[r][hi_f][:, win].mean()))\n    f3 = pd.DataFrame(rows)\n    f3[\"a_holds\"] = (f3.a_low < 0) & (f3.a_high > 0)\n    f3[\"b_holds\"] = (f3.b_low < 0) & (f3.b_high > 0)\n    F3[SET] = f3\n    print(f\"events {SET}\")\n    print(f3.round(3).to_string(index=False))\n    for rd in (\"a\", \"b\"):\n        print(f\"  reading {rd}: holds in {int(f3[f3.region.isin(three)][rd + '_holds'].sum())} of the 3 named regions; in {int(f3[rd + '_holds'].sum())} of 8\")\nmasked = G[\"set_b1\"][\"masked\"]\nfig, axs = plt.subplots(2, 4, figsize=(14, 6), sharex=True, sharey=True)\nfor r, ax in enumerate(axs.ravel()):\n    im = ax.pcolormesh(TB, F, masked[r], cmap=\"RdBu_r\", vmin=-1.5, vmax=1.5, shading=\"nearest\")\n    ax.set_title(ajile.REGION_NAMES[ajile.REGIONS[r]])\nfig.colorbar(im, ax=axs, label=\"dB (masked), events b1\")\nfig.supxlabel(\"time from onset (s)\")\nfig.supylabel(\"frequency (Hz)\")\nplt.show()\nprint(f\"plotted (b1) masked values range {masked.min():.2f} to {masked.max():.2f} dB; values outside the colour scale +-1.5 dB: {int((np.abs(masked) > 1.5).sum())}\")\n\n# %% [markdown]\n# > fig3-sensorimotor-largest: Spectral power changes are largest in precentral, postcentral and\n# > inferior parietal regions, and the three temporal regions show minimal movement-related\n# > changes.\n\n# %% tags=claim:fig3-sensorimotor-largest\nw2 = (TB >= -0.5 - 1e-9) & (TB <= 0.5 + 1e-9)\ntemporal = [\"superior temporal\", \"middle temporal\", \"inferior temporal\"]\nfor SET in SETS:\n    masked = G[SET][\"masked\"]\n    rows = []\n    for r, name in enumerate(ajile.REGIONS):\n        m = np.abs(masked[r])\n        rows.append(dict(region=ajile.REGION_NAMES[name], a=m[:, win].mean(), b_low=m[lo_f][:, win].mean(),\n                         b_high=m[hi_f][:, win].mean(), c=m[:, w2].mean()))\n    f3b = pd.DataFrame(rows).set_index(\"region\")\n    print(f\"events {SET}\")\n    print(f3b.round(4).to_string())\n    for col in (\"a\", \"b_low\", \"b_high\", \"c\"):\n        top3 = list(f3b[col].sort_values(ascending=False).index[:3])\n        t_below = all(f3b.loc[t, col] < f3b.loc[three, col].min() for t in temporal)\n        print(f\"  {col}: top three {top3}; named three are the top three: {set(top3) == set(three)}; \"\n              f\"named in top three: {len(set(top3) & set(three))}; every temporal region below all three: {t_below}\")\n    rank_b = (f3b.b_low.rank(ascending=False) <= 3) & (f3b.b_high.rank(ascending=False) <= 3)\n    print(\"  reading b, regions in the top three in both bands:\", list(f3b.index[rank_b]))\n\n# %% [markdown]\n# > fig3-lfb-more-widespread: Low-frequency power decreases are more spatially widespread than\n# > high-frequency increases and are also present in supramarginal and superior temporal regions.\n\n# %% tags=claim:fig3-lfb-more-widespread\nfor SET in SETS:\n    masked = G[SET][\"masked\"]\n    neg = {ajile.REGION_NAMES[n]: int((masked[r][lo_f][:, win] < 0).sum()) for r, n in enumerate(ajile.REGIONS)}\n    pos = {ajile.REGION_NAMES[n]: int((masked[r][hi_f][:, win] > 0).sum()) for r, n in enumerate(ajile.REGIONS)}\n    print(f\"events {SET}\")\n    print(\"  significant negative 4-30 Hz bins over 0-0.5 s per region:\", neg)\n    print(\"  significant positive 50-120 Hz bins over 0-0.5 s per region:\", pos)\n    ra_low, ra_high = sum(v > 0 for v in neg.values()), sum(v > 0 for v in pos.values())\n    rb_low, rb_high = sum(neg.values()) / lo_f.sum(), sum(pos.values()) / hi_f.sum()\n    print(f\"  reading a: regions with a negative LFB bin {ra_low}, with a positive HFB bin {ra_high}\")\n    print(f\"  reading b: negative LFB bins per frequency bin {rb_low:.2f} ({lo_f.sum()} bins), positive HFB bins per frequency bin {rb_high:.2f} ({hi_f.sum()} bins)\")\n    print(\"  supramarginal and superior temporal negative LFB bins:\", neg[\"supramarginal\"], neg[\"superior temporal\"])\n\n# %% [markdown]\n# > fig4-precentral-subject-variability: In the precentral region every subject shows the\n# > low/high-frequency pattern, but amplitudes and frequency bands vary; subjects 03, 06, 07, 08 and\n# > 11 have increases up to 120 Hz, subjects 09 and 12 mainly at 60-80 Hz, and subjects 04 and 08\n# > have narrower low-frequency decreases.\n\n# %% tags=claim:fig4-precentral-subject-variability\nfor SET in SETS:\n    spec_s = {}\n    for s in SUBJECTS:\n        m = G[SET][\"subj_med\"][s][pre]\n        m = m - m[:, bmask].mean(1, keepdims=True)\n        spec_s[s] = m[:, win].mean(1)\n    SP = pd.DataFrame(spec_s, index=F).T\n    print(f\"events {SET}: precentral spectrum per subject, 0-0.5 s (dB):\")\n    print(SP.round(2).to_string())\n    p1 = {s: bool((SP.loc[s, lf_i].mean() < 0) and (SP.loc[s, hf_i].mean() > 0)) for s in SUBJECTS}\n    print(\"  part 1, LFB mean < 0 and HFB mean > 0:\", p1, \"->\", all(p1.values()))\n    p2 = {s: bool((SP.loc[s, [116, 121]] > 0).all()) for s in (3, 6, 7, 8, 11) if s in SUBJECTS}\n    print(\"  part 2, 116 and 121 Hz positive:\", p2, \"->\", all(p2.values()))\n    p3 = {}\n    for s in [s for s in (9, 12) if s in SUBJECTS]:\n        hi = SP.loc[s, F >= 56]\n        fmax = hi.idxmax()\n        p3[s] = bool((61 <= fmax <= 76) and (SP.loc[s, (F >= 101) & (F <= 121)].mean() < hi.max() / 2))\n        print(f\"     S{s:02d}: largest 56-121 Hz bin at {fmax} Hz ({hi.max():.2f} dB); mean 101-121 Hz {SP.loc[s, (F >= 101) & (F <= 121)].mean():.2f} dB\")\n    print(\"  part 3:\", p3, \"->\", all(p3.values()))\n    width = {s: int((SP.loc[s, F <= 46] < SP.loc[s, F <= 46].min() / 2).sum()) for s in SUBJECTS}\n    third = sorted(width.values())[min(2, len(width) - 1)]\n    print(\"  part 4, width of the decrease (1-46 Hz bins below half of the most negative):\", width)\n    print(\"     three fewest (ties broken by subject order):\", sorted(width, key=lambda s: width[s])[:3],\n          \"; subjects with width <= the third smallest:\", [s for s in SUBJECTS if width[s] <= third],\n          \"; S04 and S08 at or below it:\", [width.get(s, 99) <= third for s in (4, 8)])\n\n# %% [markdown]\n# ### Banded precentral power per event\n#\n# Band power from the region spectrogram of each event over 0 to 0.5 s: LFB bins 11 to 31 Hz,\n# HFB bins 76 to 96 Hz, the mean over bins (Methods; main) and the median over time bins then\n# over frequency bins (code; variant). Without baseline: the projection of each electrode's\n# 10*log10 band mean with no subtraction.\n\n# %%\npr = roi_ev[:, pre][:, :, win]                                        # events, freqs, bins\nbp_all = pd.DataFrame({\"lfb_mean\": pr[:, lf_i].mean((1, 2)), \"hfb_mean\": pr[:, hf_i].mean((1, 2)),\n                       \"lfb_median\": np.median(np.median(pr[:, lf_i], 2), 1), \"hfb_median\": np.median(np.median(pr[:, hf_i], 2), 1)})\nraw_l, raw_h, bl_l = [], [], []\nfor p in A.path:\n    w = proj[p][:, pre]\n    b = spec[p][\"band\"]\n    raw_l.append(b[:, :, 4] @ w)\n    raw_h.append(b[:, :, 6] @ w)\n    bl_l.append(b[:, :, 0] @ w)\nbp_all[\"lfb_raw\"], bp_all[\"hfb_raw\"] = np.concatenate(raw_l), np.concatenate(raw_h)\nbp_all[\"lfb_check\"] = np.concatenate(bl_l)\nbp_all[[\"subject\", \"day\"]] = ev[[\"subject\", \"day\"]].to_numpy()\nBP = {SET: bp_all[ev[SET].to_numpy()].reset_index(drop=True) for SET in SETS}\nprint(\"check, band mean from the region spectrogram equals the projection of electrode band means:\",\n      float(np.nanmax(np.abs(BP[\"set_b1\"].lfb_mean - BP[\"set_b1\"].lfb_check))))\nfor SET in SETS:\n    print(f\"events {SET}:\")\n    print(BP[SET].drop(columns=[\"lfb_check\"]).describe().T[[\"count\", \"mean\", \"min\", \"max\"]].round(2).to_string())\n\n# %% [markdown]\n# > fig5-band-power-differs-across-subjects: Precentral LFB and HFB power in the 0.5 s after\n# > movement onset differs significantly across subjects.\n\n# %% tags=claim:fig5-band-power-differs-across-subjects\nfor SET in SETS:\n    bp = BP[SET]\n    for c in (\"lfb_mean\", \"hfb_mean\", \"lfb_median\", \"hfb_median\"):\n        h, p = kruskal([g[c].to_numpy() for _, g in bp.groupby(\"subject\")])\n        print(f\"{SET} {c}: Kruskal-Wallis H = {h:.1f}, p = {p:.2e} ({bp.subject.nunique()} subjects, {len(bp)} events)\")\n\n# %% [markdown]\n# > table1-subject-band-power-ci: Each subject's precentral band power lies in the 95% bootstrap\n# > interval Table 1 gives; LFB power is below baseline and HFB power above it for most subjects.\n\n# %% tags=claim:table1-subject-band-power-ci\nT1 = {1: (-1.87, -1.29, 0.03, 0.23), 2: (-1.12, -0.31, 0.07, 0.64), 3: (-2.11, -1.73, 1.39, 1.67), 4: (-0.17, 0.01, 0.32, 0.52),\n      5: (-0.7, -0.38, 0.2, 0.48), 6: (-1.63, -1.11, 2.02, 2.37), 7: (-0.84, -0.51, 1.14, 1.34), 8: (-0.3, 0.04, 0.36, 0.63),\n      9: (-0.57, -0.08, -0.11, 0.23), 10: (-0.87, -0.35, 0.01, 0.3), 11: (-2.3, -1.86, 0.09, 0.34), 12: (-0.66, -0.44, 0.06, 0.2)}\nfor SET in SETS:\n    bp = BP[SET]\n    rng_t1 = np.random.default_rng(1)\n    rows = []\n    for s in SUBJECTS:\n        g = bp[bp.subject == s]\n        for band, (lo_i, hi_i) in ((\"LFB\", (0, 1)), (\"HFB\", (2, 3))):\n            lo, hi = T1[s][lo_i], T1[s][hi_i]\n            for bandstat in (\"mean\", \"median\"):\n                v = g[f\"{band.lower()}_{bandstat}\"].to_numpy()\n                for evstat, fn in ((\"mean\", np.mean), (\"median\", np.median)):\n                    est = fn(v)\n                    boot = fn(v[rng_t1.integers(0, len(v), (5000, len(v)))], axis=1)\n                    rows.append(dict(subject=s, band=band, band_stat=bandstat, event_stat=evstat, estimate=est,\n                                     paper_lo=lo, paper_hi=hi, inside=lo <= est <= hi,\n                                     boot_lo=np.percentile(boot, 2.5), boot_hi=np.percentile(boot, 97.5)))\n    t1 = pd.DataFrame(rows)\n    summary = t1.groupby([\"band_stat\", \"event_stat\"]).inside.sum()\n    print(f\"events {SET}: subject and band pairs inside the paper's interval, of {2 * len(SUBJECTS)}:\")\n    print(summary.to_string())\n    best = summary.idxmax()\n    print(\"  best reading (band statistic, event statistic):\", best, int(summary.max()))\n    print(t1[(t1.band_stat == best[0]) & (t1.event_stat == best[1])].round(2).to_string(index=False))\n    if SET == \"set_b1\":\n        print(\"  the band mean and event mean reading, for comparison:\")\n        print(t1[(t1.band_stat == \"mean\") & (t1.event_stat == \"mean\")].round(2).to_string(index=False))\n    mm = t1[(t1.band_stat == best[0]) & (t1.event_stat == best[1])]\n    print(f\"  under the best reading, subjects with LFB below 0: {int((mm[mm.band == 'LFB'].estimate < 0).sum())}; \"\n          f\"with HFB above 0: {int((mm[mm.band == 'HFB'].estimate > 0).sum())} (of {len(SUBJECTS)})\")\n\n# %% [markdown]\n# > fig5-recording-day-effects: Precentral band power differs significantly across recording days\n# > in LFB for subjects 03, 05, 06, 07, 08 and 11, and in HFB for subjects 03, 04, 07, 08 and 10.\n\n# %% tags=claim:fig5-recording-day-effects\npaper_sig = {(\"LFB\", s) for s in (3, 5, 6, 7, 8, 11)} | {(\"HFB\", s) for s in (3, 4, 7, 8, 10)}\nDY = {}\nfor SET in SETS:\n    bp = BP[SET]\n    rows = []\n    for s in SUBJECTS:\n        g = bp[bp.subject == s]\n        for band in (\"LFB\", \"HFB\"):\n            for st in (\"mean\", \"median\"):\n                c = f\"{band.lower()}_{st}\"\n                h, p = kruskal([x[c].to_numpy() for _, x in g.groupby(\"day\")])\n                rows.append(dict(subject=s, band=band, band_stat=st, p=p, sig=p < 0.05, paper_sig=(band, s) in paper_sig))\n    dy = pd.DataFrame(rows)\n    dy[\"agree\"] = dy.sig == dy.paper_sig\n    DY[SET] = dy\n    print(f\"events {SET}: Kruskal-Wallis p across days\")\n    print(dy.pivot_table(index=\"subject\", columns=[\"band\", \"band_stat\"], values=\"p\").to_string(float_format=lambda x: f\"{x:.3g}\"))\n    print(f\"  pairs agreeing with the paper's pattern, of {2 * len(SUBJECTS)}:\", dy.groupby(\"band_stat\").agree.sum().to_dict())\n    print(\"  disagreeing pairs (band mean):\", dy[(dy.band_stat == \"mean\") & ~dy.agree][[\"subject\", \"band\", \"p\", \"paper_sig\"]].round(4).values.tolist())\n    print(\"  significant pairs (band mean):\", int(dy[dy.band_stat == \"mean\"].sig.sum()))\n    print(\"  per-day means (dB), band mean:\")\n    print(bp.groupby([\"subject\", \"day\"])[[\"lfb_mean\", \"hfb_mean\"]].mean().unstack().round(2).to_string())\n\n# %% [markdown]\n# > extfig5-1-baseline-reduces-day-variability: Subtracting the -1.5 to -1 s baseline reduces the\n# > variability of band power across recording days, though clear variability remains.\n#\n# Reading (a): precentral region, per subject, the SD across days of the day means of event band\n# power, with baseline (band mean) and without (projected 10*log10 band mean). Reading (b): the\n# same per electrode, on the days the electrode is marked good, for electrodes good on at least two\n# days.\n\n# %% tags=claim:extfig5-1-baseline-reduces-day-variability\nfor SET in SETS:\n    bp = BP[SET]\n    rows = []\n    for s in SUBJECTS:\n        g = bp[bp.subject == s]\n        dm = g.groupby(\"day\")[[\"lfb_mean\", \"hfb_mean\", \"lfb_raw\", \"hfb_raw\"]].mean()\n        rows.append(dict(subject=s, lfb_sd_bl=dm.lfb_mean.std(), lfb_sd_raw=dm.lfb_raw.std(),\n                         hfb_sd_bl=dm.hfb_mean.std(), hfb_sd_raw=dm.hfb_raw.std()))\n    ra = pd.DataFrame(rows)\n    print(f\"events {SET}\")\n    print(ra.round(3).to_string(index=False))\n    for b in (\"lfb\", \"hfb\"):\n        print(f\"  reading a, {b}: SD with baseline below SD without in {int((ra[b + '_sd_bl'] < ra[b + '_sd_raw']).sum())} of {len(ra)} subjects\")\n    el_rows = []\n    for s in SUBJECTS:\n        paths = list(A.path[A.subject == s])\n        nch = spec[paths[0]][\"band\"].shape[1]\n        for c in range(nch):\n            dm = {k: [] for k in (\"lb\", \"lr\", \"hb\", \"hr\")}\n            for p in paths:\n                if not meta[p][\"electrodes\"].good.iloc[c]:\n                    continue\n                msk = ev[ev.path == p][SET].to_numpy()\n                b = spec[p][\"band\"][msk, c]\n                for k, j in ((\"lb\", 0), (\"lr\", 4), (\"hb\", 2), (\"hr\", 6)):\n                    dm[k].append(np.nanmean(b[:, j]))\n            if len(dm[\"lb\"]) >= 2:\n                el_rows.append(dict(subject=s, ch=c, **{k: np.std(v, ddof=1) for k, v in dm.items()}))\n    rb = pd.DataFrame(el_rows)\n    for b, (kb, kr) in ((\"lfb\", (\"lb\", \"lr\")), (\"hfb\", (\"hb\", \"hr\"))):\n        print(f\"  reading b, {b}: SD with baseline below SD without in {int((rb[kb] < rb[kr]).sum())} of {len(rb)} electrodes \"\n              f\"(median SD with {rb[kb].median():.3f}, without {rb[kr].median():.3f} dB)\")\n    print(\"  by subject, fraction of electrodes with lower SD after baseline (LFB, HFB):\")\n    print(rb.assign(l=rb.lb < rb.lr, h=rb.hb < rb.hr).groupby(\"subject\")[[\"l\", \"h\"]].mean().round(2).T.to_string())\n    print(\"  significant day effects found in fig5-recording-day-effects (band mean):\", int(DY[SET][DY[SET].band_stat == \"mean\"].sig.sum()))\n\n# %% [markdown]\n# > discussion-day-changes-small: Day-to-day changes in baseline-subtracted spectral power are\n# > small (about 1-2 dB) compared with spectral power without baseline subtraction (about 10-50\n# > dB).\n\n# %% tags=claim:discussion-day-changes-small\nfor SET in SETS:\n    bp = BP[SET]\n    rows = []\n    for s in SUBJECTS:\n        g = bp[bp.subject == s]\n        for band in (\"lfb\", \"hfb\"):\n            dm = g.groupby(\"day\")[f\"{band}_mean\"].mean()\n            rows.append(dict(subject=s, band=band, max_dev=np.abs(dm - g[f\"{band}_mean\"].mean()).max(),\n                             day_range=dm.max() - dm.min(), level_uV=g[f\"{band}_raw\"].mean(), level_V=g[f\"{band}_raw\"].mean() - 120))\n    dc2 = pd.DataFrame(rows)\n    print(f\"events {SET}\")\n    print(dc2.round(2).to_string(index=False))\n    low = bp[(bp.lfb_raw < 0) | (bp.hfb_raw < 0)]\n    print(f\"  events whose precentral band power without baseline is below 0 dB: {len(low)} of {len(bp)}, \"\n          f\"by subject {low.subject.value_counts().sort_index().to_dict()}\")\n    med = bp.groupby(\"subject\")[[\"lfb_raw\", \"hfb_raw\"]].median()\n    print(f\"  level without baseline as the median over events instead (uV): {med.min().min():.1f} to {med.max().max():.1f} dB\")\n    print(f\"  largest day-to-day change (deviation of a day mean from the subject mean): {dc2.max_dev.max():.2f} dB; all at most 2.2 dB: {bool((dc2.max_dev <= 2.2).all())}; \"\n          f\"pairs above 2.2 dB: {dc2[dc2.max_dev > 2.2][['subject', 'band']].values.tolist()}\")\n    print(f\"  largest range of day means: {dc2.day_range.max():.2f} dB\")\n    for u in (\"level_uV\", \"level_V\"):\n        print(f\"  level without baseline, {u}: {dc2[u].min():.1f} to {dc2[u].max():.1f} dB; all in 9-55 dB: {bool(dc2[u].between(9, 55).all())}\")\n\n"
}
```

```
File created successfully at: /tmp/claude-1001/build/spectral.py (file state is current in your context — no need to Read it back)
```

**Agent**

Splicing that in, then adding b3 to the event-set cell and the behaviour loops:

**Agent calls Bash**

```bash
cd $TMPDIR/build && python - <<'EOF'
s=open('nb1.py').read()
i=s.index('# %% [markdown]\n# ## Spectral power'); j=s.index('# %% [markdown]\n# ## Summary')
s=s[:i]+open('spectral.py').read()+s[j:]
s=s.replace('rej1, rej2, ev["psd_db"] = ajile.rejection(ev, A, meta, spec, SUBJECTS)\n','rej1, rej2, ev["psd_db"], rej3 = ajile.rejection(ev, A, meta, spec, SUBJECTS)\n')
s=s.replace('''ev["rej_b2"] = rej2 & ev.ok''','''ev["rej_b2"] = rej2 & ev.ok
ev["rej_b3"] = rej3 & ev.ok''')
s=s.replace('''ev["set_b2"] = ev.set_fp & ev.ok & ~ev.rej_b2''','''ev["set_b2"] = ev.set_fp & ev.ok & ~ev.rej_b2
ev["set_b3"] = ev.set_fp & ev.ok & ~ev.rej_b3''')
s=s.replace('''print(ev.groupby("subject")[["set_a", "set_fp", "set_b1", "set_b2", "rej_b1", "rej_b2"]].sum().T.to_string())''','''print(ev.groupby("subject")[["set_a", "set_fp", "set_b1", "set_b2", "set_b3", "rej_b1", "rej_b2", "rej_b3"]].sum().T.to_string())
zb = ev.rej_b3 & ~ev.rej_b1 & ev.set_fp
print(f"segments that (b3) drops beyond (b1), among events not flagged false positive: {int(zb.sum())}")''')
# event-set markdown
s=s.replace('''# fails. The false positives alone are also shown.''','''# fails. The false positives alone are also shown. A third reading, (b3), was added after the
# first run of this notebook showed segments whose ECoG is zeroed (the preprocessing zeroes
# high-amplitude artifacts) inside the analysed window, which (b1) keeps because the Welch PSD
# of the whole 10 s is above 0 dB: (b3) drops what (b1) drops and also any segment whose Morlet
# power, averaged over good electrodes and frequencies, is below 0 dB in a 0.1 s bin from -1.5 s
# to 1.5 s.''')
s=s.replace('''cnt = ev.groupby("subject")[["set_a", "set_fp", "set_b1", "set_b2"]].sum()''','''cnt = ev.groupby("subject")[["set_a", "set_fp", "set_b1", "set_b2", "set_b3"]].sum()''')
s=s.replace('''for setname in ("set_b1", "set_a", "set_b2"):
    e = ev[ev[setname]]
    for k, c in FEAT.items():''','''for setname in ("set_b1", "set_b3", "set_a", "set_b2"):
    e = ev[ev[setname]]
    for k, c in FEAT.items():''')
s=s.replace('''for s in ("set_b1", "set_a", "set_b2"):
    print(s, ": features''','''for s in ("set_b1", "set_b3", "set_a", "set_b2"):
    print(s, ": features''')
s=s.replace('''for setname in ("set_b1", "set_a"):
    t = shape_table''','''for setname in ("set_b1", "set_b3", "set_a"):
    t = shape_table''')
s=s.replace('''for setname in ("set_b1", "set_a"):
    e = ev[ev[setname]]
    rows = []''','''for setname in ("set_b1", "set_b3", "set_a"):
    e = ev[ev[setname]]
    rows = []''')
s=s.replace('''for setname in ("set_b1", "set_a"):
    for s in SUBJECTS:
        disp = {}''','''for setname in ("set_b1", "set_b3", "set_a"):
    for s in SUBJECTS:
        disp = {}''')
s=s.replace('''for setname in ("set_b1", "set_a", "set_b2"):
    C = ev[ev[setname]]''','''for setname in ("set_b1", "set_b3", "set_a", "set_b2"):
    C = ev[ev[setname]]''')
# days-waking: loop b1 and b3
i=s.index('# %% tags=claim:fig2-days-and-waking'); j=s.index('# %% [markdown]', i)
new='''# %% tags=claim:fig2-days-and-waking
for SET in ("set_b1", "set_b3", "set_a"):
    e = ev[ev[SET]]
    dc = e.groupby(["subject", "day"]).size().unstack()
    busiest = dc.max(axis=1) / dc.sum(axis=1)
    wake = e.groupby("subject").hour.apply(lambda h: ((h >= 8) & (h < 24)).mean())
    out = pd.DataFrame({"busiest_day_frac": busiest, "busiest_day": dc.idxmax(axis=1), "waking_frac": wake})
    print(f"events {SET}")
    print(dc.fillna(0).astype(int).to_string())
    print(out.round(3).to_string())
    print("  subjects whose busiest day holds more than half:", list(out.index[out.busiest_day_frac > 0.5]))
    print("  subjects with more than half of events in 08:00-24:00:", int((out.waking_frac > 0.5).sum()), "of", len(out))

'''
s=s[:i]+new+s[j:]
s=s.replace('valid = cenL.abs().sum(1).to_numpy() > 0','valid = cenL.abs().sum(axis=1).to_numpy() > 0')
open('nb1.py','w').write(s)
EOF
grep -n "set_b3" nb1.py | wc -l; cd entries/000055-peterson-2021 && rm -f $TMPDIR/cache_ext_* $TMPDIR/cache_wr_*; . $TMPDIR/dev/bin/activate && date -u && AJILE_SUBJECTS=4,9 MPLBACKEND=Agg timeout 1500 python $TMPDIR/build/devrun.py $TMPDIR/build/nb1.py > $TMPDIR/dev_nb1.log 2>&1; echo exit $?; date -u; grep -n "Traceback" -A 14 $TMPDIR/dev_nb1.log | tail -16
```

```
11
Fri Oct 23 17:19:57 UTC 2026
exit 0
Fri Oct 23 17:22:49 UTC 2026
```

**Agent**

The dev run passes (it is 17:23). Checking the b3 counts and that the per-set outputs look right:

**Agent calls Bash**

```bash
grep -n -A12 "PSD averaged over good" $TMPDIR/dev_nb1.log | cut -c1-200; grep -n "events set_b3" -A3 $TMPDIR/dev_nb1.log | head -20 | cut -c1-200; grep -n "pairs inside\|best reading\|all at most" $TMPDIR/dev_nb1.log | cut -c1-200
```

```
93:PSD averaged over good electrodes, dB (uV^2/Hz), 1-200 Hz: range 4.3 to 16.2
94-subject    4    9
95-set_a    417  211
96-set_fp   268  151
97-set_b1   268  150
98-set_b2    69    0
99-set_b3   267  150
100-rej_b1     0    1
101-rej_b2   298  211
102-rej_b3     3    1
103-segments that (b3) drops beyond (b1), among events not flagged false positive: 1
104-S01 paper [3, 4, 5, 7] dataset [3, 4, 5, 7] same
105-S02 paper [3, 4, 5, 6] dataset [3, 4, 5, 6] same
174:events set_b3
175-subject   n  frac_dur_lt2  med_dur  frac_mag_lt200  med_mag         peaks  dens0          peak_dens  bimodal_pm90  frac_side
176-      4 267         0.914    1.067           0.974   80.257        [68.0]  0.003          [0.01148]         False      0.191
177-      9 150         0.880    1.300           1.000   64.713 [-62.0, 66.0]  0.003   [0.0062, 0.0054]         False      0.147
--
200:events set_b3
201-subject  med_ratio  skew_overlap  frac_bimanual
[... 21 more lines not kept]
```

**Agent**

Both readings run. Updating notebook 2 for the new return value of `rejection` and a note that it uses b1 only, adding b3 to the question, then the full run:

**Agent calls Bash**

```bash
cd $TMPDIR/build && python - <<'EOF'
s=open('nb2.py').read()
s=s.replace("    rej1, _, _ = ajile.rejection(ev_s.assign(ok=ok), A_s, meta, spec_s, [s])","    rej1, _, _, _ = ajile.rejection(ev_s.assign(ok=ok), A_s, meta, spec_s, [s])")
s=s.replace('''    DESIGN[s] = dict(X=X, groups=groups, n=int(keep.sum()), rejected=int((ok & ~rej1 == False).sum()))''','''    DESIGN[s] = dict(X=X, groups=groups, n=int(keep.sum()), rejected=int((ok & rej1).sum()))''')
s=s.replace('''# Not run, for time: the code's 80/20 split and the median band power as variants (each would
# double the fits), and the code's log(x + 1) transforms.''','''# Not run, for time: the code's 80/20 split and the median band power as variants (each would
# double the fits), the code's log(x + 1) transforms, and the events of reading (b3) of the first
# notebook (which also drops the segments with zeroed ECoG; a second set of fits does not fit in
# the notebook's 30 minutes). The fits here use the events of reading (b1).''')
open('nb2.py','w').write(s)
EOF
cd  && python - <<'EOF'
p='questions/000055.yaml'
s=open(p).read()
s=s.replace('''    fails.
  passage: >-''','''    fails. A first run showed segments whose ECoG is zeroed (the preprocessing zeroes
    high-amplitude artifacts) inside the analysed window, which (b1) keeps because the Welch PSD of
    the whole 10 s is above 0 dB; a third reading is run in the first notebook, (b3): as (b1), and
    also dropping a segment whose Morlet power averaged over good electrodes and frequencies is
    below 0 dB in any 0.1 s bin from -1.5 to 1.5 s. Is the paper's "power <0 dB" a PSD of the whole
    segment (b1), per electrode (b2), or power over time within the segment (b3)?
  passage: >-''')
s=s.replace('''    of tolerance, and the drop changes the events of every reading-(b) claim.''','''    of tolerance, and the drop changes the events of every reading-(b) claim. (b2) leaves no
    events in four subjects, so it cannot be the paper's rule. Between (b1) and (b3) about 40
    events differ, but their band power is near +-300 dB (zeroed ECoG), so means over events
    differ widely: under (b1) the band-mean and event-mean reading of Table 1 matches 8 of 24
    intervals.''')
open(p,'w').write(s)
EOF
cd entries/000055-peterson-2021 && . $TMPDIR/dev/bin/activate && python $TMPDIR/build/conv.py $TMPDIR/build/nb1.py reproduce_peterson_2021.ipynb && python $TMPDIR/build/conv.py $TMPDIR/build/nb2.py reproduce_peterson_2021_regression.ipynb && cd ../.. && python tools/entry.py check entries/000055-peterson-2021 2>&1 | tail -3; date -u
```

```
0 error(s)
Fri Oct 23 17:23:20 UTC 2026
```

**Agent**

Check passes. Full run of both notebooks (about 45 min):

**Agent calls Bash**

```bash
date -u; python tools/entry.py all entries/000055-peterson-2021 2>&1 | tail -4; date -u
```

```
Fri Oct 23 17:23:23 UTC 2026
Installed kernelspec registry-000055-peterson-2021 in executed/000055-peterson-2021/.venv/share/jupyter/kernels/registry-000055-peterson-2021
0 error(s)
pass  reproduce_peterson_2021.ipynb  (1023 s)
pass  reproduce_peterson_2021_regression.ipynb  (1657 s)
Fri Oct 23 18:08:26 UTC 2026
```

**Agent**

Both pass again: 17.0 and 27.6 min. Extracting the outputs:

**Agent calls Bash**

```bash
cd executed/000055-peterson-2021 && for nb in reproduce_peterson_2021 reproduce_peterson_2021_regression; do python - $nb <<'EOF' > $TMPDIR/$1.txt
import nbformat,sys
nb=nbformat.read(sys.argv[1]+'.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print(f"=== cell {i} {c.metadata.get('tags','')}")
    for o in c.outputs:
        if o.output_type=='stream' and o.name=='stdout': print(o.text)
        elif o.output_type=='error': print('ERROR', o.ename, o.evalue)
EOF
done; ls $TMPDIR/*.txt; python - <<'EOF'
import nbformat
nb=nbformat.read('reproduce_peterson_2021.ipynb',4)
out=[]
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    t=''.join(o.get('text','') for o in c.outputs if o.output_type=='stream' and o.name=='stdout')
    out.append(f"=== cell {i} {c.metadata.get('tags','')}\n{t}")
open('/tmp/claude-1001/o1.txt','w').write('\n'.join(out))
nb=nbformat.read('reproduce_peterson_2021_regression.ipynb',4)
out=[]
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    t=''.join(o.get('text','') for o in c.outputs if o.output_type=='stream' and o.name=='stdout')
    out.append(f"=== cell {i} {c.metadata.get('tags','')}\n{t}")
open('/tmp/claude-1001/o2.txt','w').write('\n'.join(out))
EOF
grep -n -A12 "PSD averaged over good" $TMPDIR/o1.txt | cut -c1-200; grep -n -A10 "claim:fig2-event-counts" $TMPDIR/o1.txt | cut -c1-200
```

```
/tmp/claude-1001/out1.txt
/tmp/claude-1001/out2.txt
214:PSD averaged over good electrodes, dB (uV^2/Hz), 1-200 Hz: range -inf to 33.7
215-subject   1    2    3    4    5    6    7    8    9    10   11   12
216-set_a    741  305  642  417  267  956  800  965  211  806  982  996
217-set_fp   659  209  584  268  203  869  675  850  151  620  896  947
218-set_b1   659  204  580  268  199  851  671  849  150  618  892  946
219-set_b2     2  178  490   69   73  670  598   28    0    0  765    0
220-set_b3   656  202  580  267  199  841  668  841  150  598  888  942
221-rej_b1     0    6    5    0    4   18    4    1    1    4    4    1
222-rej_b2   737   49  105  298  166  227   91  930  211  806  150  996
223-rej_b3     3    8    5    3    4   30    7   10    1   29    9    7
224-segments that (b3) drops beyond (b1), among events not flagged false positive: 55
225-
226-=== cell 19 ['claim:subject-days']
263:=== cell 23 ['claim:fig2-event-counts']
264-subject   1    2    3    4    5    6    7    8    9    10   11   12
265-set_a    741  305  642  417  267  956  800  965  211  806  982  996
266-set_fp   659  209  584  268  203  869  675  850  151  620  896  947
267-set_b1   659  204  580  268  199  851  671  849  150  618  892  946
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 274,1200p $TMPDIR/o1.txt | grep -v "^ *[0-9]* *[0-9.-]* *[0-9.-]* *[0-9.-]* *[0-9.-]* *[0-9.-]*  *[0-9.-]*  *\[" | grep -n "reading set_b3\|set_b3 :\|part:\|events set_b3\|holds in\|top three\|reading a:\|reading b:\|supramarginal and\|part [1-4]\|three fewest\|S0[0-9]: largest\|Kruskal\|inside the paper\|best reading\|under the best\|pairs agreeing\|disagreeing\|significant pairs\|SD with baseline\|significant day\|largest day\|level without\|below 0 dB\|ratio part\|overlap part\|class part\|five highest\|S02, S04\|within 10%\|busiest day\|more than half of events\|holds\b" | cut -c1-260
```

```
1:reading set_b3: fewest 150, most 942, median 627.0; within tolerance [np.True_, np.True_, np.True_] -> all three
17:set_b3 : features with p < 0.001: 10 of 10
37:  duration part: pooled 0.918, subjects with >half under 2 s 12 of 12
38:  magnitude part: pooled 0.914, subjects with >half under 200 px 12 of 12
39:  angle part: pooled bimodal at +-90 False; subjects 0 of 12
40:events set_b3
43:  duration part: pooled 0.918, subjects with >half under 2 s 12 of 12
44:  magnitude part: pooled 0.915, subjects with >half under 200 px 12 of 12
45:  angle part: pooled bimodal at +-90 False; subjects 0 of 12
49:  duration part: pooled 0.917, subjects with >half under 2 s 12 of 12
50:  magnitude part: pooled 0.915, subjects with >half under 200 px 12 of 12
51:  angle part: pooled bimodal at +-90 False; subjects 0 of 12
69:  ratio part: pooled median 0.115; subjects with median < 0.5: 12 of 12
70:  overlap part: pooled skewness 1.094; subjects with skewness > 0: 12 of 12
71:  class part: pooled fraction bimanual 0.717; subjects above half: 12 of 12
72:  five highest median ratios: [2, 3, 4, 5, 7]; five lowest overlap skewness: [2, 3, 5, 7, 10]
73:  S02, S04, S05 among the highest ratios: [True, True, True]; among the lowest skewness: [True, False, True]
74:events set_b3
89:  ratio part: pooled median 0.113; subjects with median < 0.5: 12 of 12
90:  overlap part: pooled skewness 1.101; subjects with skewness > 0: 12 of 12
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "events set_b1 (n=\|events set_b3 (n=\|events set_a (n=" $TMPDIR/o1.txt | cut -c1-400; sed -n 421,430p $TMPDIR/o1.txt; sed -n 480,490p $TMPDIR/o1.txt; grep -n "wrist traces\|set_a   a\|set_b1  a\|set_b3  a\|  b  " $TMPDIR/o1.txt | head; grep -n -B2 -A30 "claim:extfig2-1c" $TMPDIR/o1.txt | sed -n 1,30p | cut -c1-120
```

```
467:events set_b1 (n=6887): magnitude-duration r=0.259 (paper 0.26); magnitude-onset_speed r=0.562 (paper 0.56); duration-bimanual_overlap r=0.475 (paper 0.48); bimanual_overlap-bimanual_ratio r=0.508 (paper 0.51); bimanual_class-bimanual_ratio r=0.496 (paper 0.5); bimanual_overlap-bimanual_class r=0.609 (paper 0.61)
469:events set_b3 (n=6832): magnitude-duration r=0.261 (paper 0.26); magnitude-onset_speed r=0.561 (paper 0.56); duration-bimanual_overlap r=0.473 (paper 0.48); bimanual_overlap-bimanual_ratio r=0.507 (paper 0.51); bimanual_class-bimanual_ratio r=0.496 (paper 0.5); bimanual_overlap-bimanual_class r=0.610 (paper 0.61)
471:events set_a (n=8088): magnitude-duration r=0.231 (paper 0.26); magnitude-onset_speed r=0.609 (paper 0.56); duration-bimanual_overlap r=0.505 (paper 0.48); bimanual_overlap-bimanual_ratio r=0.501 (paper 0.51); bimanual_class-bimanual_ratio r=0.494 (paper 0.5); bimanual_overlap-bimanual_class r=0.598 (paper 0.61)
  five highest median ratios: [2, 3, 4, 5, 7]; five lowest overlap skewness: [2, 3, 4, 5, 7]
  S02, S04, S05 among the highest ratios: [True, True, True]; among the lowest skewness: [True, True, True]

=== cell 31 ['claim:extfig2-1c-contralateral-larger']
wrist traces read in 23 s; 91 frames from -1.5 to 1.5 s
events   set_a        set_b1        set_b3       
reading      a      b      a      b      a      b
subject                                          
1         7.53  10.29   7.53  10.35   7.54  10.13
2         1.71   1.73   1.66   1.69   1.63   1.66
1        121  166  186    0  186
2         38   66   56   44    0
3        186  168  127   99    0
4         19   42   32   60  115
5         35   39    0    0  125
6        157  184  183  163  164
7         70   77  173  181  170
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A6 "inside the paper's interval" $TMPDIR/o1.txt | cut -c1-120; grep -n "cell 11\|stored \|shifted \|outside the ECoG\|spectral pass\|files where" $TMPDIR/o1.txt | cut -c1-200; grep -v "^S[0-9][0-9]: " $TMPDIR/o2.txt | grep -n "models\|largest\|variant\|correlation\|(a):\|(b):\|top two\|top three\|highest in each\|ranked second\|median angle\|R2 > 0.05\|band power for\|notebook ran" | cut -c1-260
```

```
730:events set_b1: subject and band pairs inside the paper's interval, of 24:
731-band_stat  event_stat
732-mean       mean           8
733-           median        21
734-median     mean           9
735-           median        21
736-  best reading (band statistic, event statistic): ('mean', 'median') 21
--
789:events set_b3: subject and band pairs inside the paper's interval, of 24:
790-band_stat  event_stat
791-mean       mean          22
792-           median        20
793-median     mean          21
794-           median        21
795-  best reading (band statistic, event statistic): ('mean', 'mean') 22
137:=== cell 11 
138:sub-01_ses-7 stored   n=40 precentral LFB +0.11 dB (Wilcoxon p=0.52), HFB -0.14 dB (p=0.63)
139:sub-01_ses-7 shifted  n=40 precentral LFB -1.21 dB (Wilcoxon p=0.039), HFB +0.01 dB (p=0.98)
140:   events outside the ECoG on the stored clock: 132 of 190; on the shifted clock: 0
141:sub-04_ses-3 stored   n=13 precentral LFB +0.35 dB (Wilcoxon p=0.19), HFB +0.19 dB (p=0.54)
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
cat result.json | head -30; grep -n "result.json\|sha\|hash" tools/entry.py | head
```

```
{
 "entry": "000055-peterson-2021",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_peterson_2021.ipynb",
   "ok": true,
   "seconds": 1023,
   "error": null
  },
  {
   "notebook": "reproduce_peterson_2021_regression.ipynb",
   "ok": true,
   "seconds": 1657,
   "error": null
  }
 ]
}
245:            # claims file is shared, and an earlier attempt may predate the claim's `elsewhere`.
326:            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
[... 1 more lines not kept]
```

**Agent**

No hashes are stored, so the conclusion cells can be added as markdown without changing what ran. Getting the remaining numbers for the conclusions:

**Agent calls Bash**

```bash
grep -n -A12 "claim:fig2-features-differ" $TMPDIR/o1.txt | cut -c1-120; grep -n -A16 "contralateral and ipsilateral peaks" $TMPDIR/o1.txt | cut -c1-100; grep -n -B3 -A22 "events set_b1$" $TMPDIR/o1.txt | grep -A12 "region  a_low" | head -12
```

```
276:=== cell 25 ['claim:fig2-features-differ-across-subjects']
277-events                   set_a    set_b1    set_b2    set_b3
278-feature                                                     
279-bimanual class        1.43e-94  7.19e-82  2.10e-12  3.45e-81
280-bimanual overlap (s)  8.41e-77  9.70e-69  2.06e-10  1.98e-67
281-bimanual ratio       1.45e-118 6.95e-105  2.14e-27 4.53e-105
282-day                   2.04e-75  7.15e-77  3.93e-65  4.94e-76
283-onset speed (px/s)    0.00e+00  0.00e+00  5.85e-67  0.00e+00
284-reach angle (deg)     4.87e-37  1.47e-30  7.91e-07  6.03e-30
285-reach duration (s)    1.15e-34  1.54e-31  3.33e-07  1.80e-31
286-reach magnitude (px) 1.36e-307 1.36e-274  3.86e-45 1.19e-271
287-speech ratio         3.77e-266 4.56e-237 6.28e-124 2.55e-236
288-time of day (h)       4.69e-59  7.43e-52  1.06e-29  1.77e-52
448:contralateral and ipsilateral peaks (px), reading b1:
449-        contra_peak        ipsi_peak      
450-reading           a      b         a     b
451-subject                                   
452-1              76.2   74.4      10.1   7.2
453-2              69.9   72.8      42.1  43.1
454-3              63.7   62.8      23.4  19.8
[... 22 more lines not kept]
```

**Agent**

Writing the conclusion cells and the summaries into both notebook sources:

**Agent calls Bash**

```bash
cat > $TMPDIR/build/results1.py <<'EOF'
R1 = {
"figshare-event-link": "**Result: reproduced.** All 8088 dataset events have exactly one Figshare record with the same timestamp (100.0%), no timestamp repeats within a file, and the features both hold agree to within 4.9e-07 (onset speed; 5e-08 or less for the others), with no event whose bimanual class differs. The Figshare flags mark 1157 events (14.3%) as false positives; the dataset does not mark them.",
"figshare-roi-link": "**Result: reproduced.** Every subject's matrix has one row per channel of the dataset; S01's has 4 more rows, all zero. The median distance between an electrode's position and the weighted mean of its region centroids is 15.6 to 27.6 mm, below the smallest of 200 row-shuffled distances in every subject (44.9 to 54.9 mm). The eight regions with density averaged over subjects above 3 are the claims file's eight.",
"subject-days": "**Result: reproduced.** The 12 subjects hold exactly the days of Table 2, 55 subject-days, the subject ids inside the files equal the file names, and the Figshare files carry the same subject and day pairs.",
"cohort": "**Result: partially reproduced.** The files hold 12 subjects, a mean of 84.8 surface electrodes (paper 87.0 +- 12.9), and 5 subjects implanted on the right by the mean x coordinate and by the reaching wrist (paper 5). Counting as depth electrodes the groups whose description says \"depth\", 7 subjects have them (paper 5), with a mean of 23.7 among them (paper 23.2 +- 12.1). Sex and age are not in the files, so the 8 males and the mean age are not testable.",
"fig2-event-counts": "**Result: reproduced** under reading (b). With the Figshare false positives and the rejected segments dropped, the fewest, most and median events per subject are 150, 946 and 638.5 under (b1) and 150, 942 and 627.0 under (b3), all within tolerance; the false positives alone give 151, 947 and 639.5, the paper's numbers. Reading (a), all events in the dataset, gives 211, 996 and 770.5, with the fewest and the median outside tolerance. Rejection reading (b2) leaves no events in S09, S10 and S12.",
"fig2-features-differ-across-subjects": "**Result: reproduced.** All ten features differ across subjects with p < 0.001 under (b1), (b3) and (a): the largest p is 1.47e-30 (reach angle) under (b1) and 6.03e-30 under (b3).",
"fig2-reach-shape": "**Result: partially reproduced.** More than half of the reaches last under 2 s and cover under 200 pixels in all 12 subjects and pooled (pooled 0.918 and 0.914 under (b1)). The reach angle part does not hold: the two highest density peaks are near -55 to -73 and +62 to +75 degrees, not within 15 degrees of +-90, in 0 of 12 subjects and pooled (-72 and 75), under (b1), (b3) and (a).",
"fig2-bimanual-skew": "**Result: blocked (methods underspecified).** The ratio, overlap and class parts hold pooled and in 12 of 12 subjects under every event set (pooled median ratio 0.115, overlap skewness 1.094, fraction bimanual 0.717 under (b1)). S02, S04 and S05 are among the five highest median ratios under every set; among the five lowest overlap skewness S04 is under (b3) and (a) but not under (b1), where S10 takes its place. The criterion names no event set and the rejection rule is open (question asked), so the claim is reproduced under (b3) and (a) and partially reproduced under (b1).",
"extfig2-1c-contralateral-larger": "**Result: reproduced.** The peak of the median contralateral displacement over 0 to 1.5 s exceeds the ipsilateral one in 12 of 12 subjects under both rest positions and every event set; the ratio is 1.30 (S04) to 39.8 (S12) under reading (a) with events (b1), and the contralateral peaks are 55.8 to 157.2 pixels.",
"extfig2-2-feature-correlations": "**Result: reproduced.** Under (b1) the six correlations are 0.259, 0.562, 0.475, 0.508, 0.496 and 0.609 (paper 0.26, 0.56, 0.48, 0.51, 0.50, 0.61), all within 10%; under (b3) also 6 of 6. With all events (a), 5 of 6 are within 10% (magnitude and duration 0.231).",
"fig2-days-and-waking": "**Result: partially reproduced.** The busiest day holds more than half of the events in S05 (0.628) and S09 (0.553) but not in S04 (0.429, day 7), and in none of the other nine, under (b1); (b3) and (a) give the same two subjects. More than half of the events fall between 08:00 and 24:00 in 12 of 12 subjects (0.662 to 0.970). Only the waking part holds.",
"fig3-group-lfb-decrease-hfb-increase": "**Result: reproduced.** In precentral, postcentral and inferior parietal regions the masked 4-30 Hz mean is negative and the masked 50-120 Hz mean positive, both over 0 to 0.5 s (reading a; precentral -0.871 and 0.480 dB under (b1)) and at the bin nearest onset (reading b), under (b1) and (b3). Under (b1) the pattern holds in 7 of 8 regions by reading (a) and 4 of 8 by reading (b).",
"fig3-sensorimotor-largest": "**Result: reproduced.** Under all three readings, and under (b1) and (b3), precentral, postcentral and inferior parietal are the three regions with the largest mean absolute masked power, and every temporal region is below all three (reading a under (b1): 0.502, 0.495 and 0.325 dB against 0.045, 0.003 and 0.018 for the temporal regions).",
"fig3-lfb-more-widespread": "**Result: reproduced.** Under (b1), 8 regions have a significant LFB decrease and 7 a significant HFB increase over 0 to 0.5 s (reading a), and there are 36.2 significant negative bins per LFB frequency bin against 23.4 positive bins per HFB frequency bin (reading b); supramarginal and superior temporal have 30 and 25 significant negative LFB bins. (b3) gives 8 against 7 and 35.2 against 23.9.",
"fig4-precentral-subject-variability": "**Result: partially reproduced.** Parts 2 and 3 hold: the 116 and 121 Hz bins are positive in S03, S06, S07, S08 and S11, and the largest 56-121 Hz bin is at 71 Hz in S09 and 66 Hz in S12, with the 101-121 Hz mean below half of it. Part 4 holds: the widths of the decrease are 1 (S08) and 2 (S04) bins under (b1), the two smallest; under (b3) S08 has 2 and S04 shares the third smallest width (3) with S02, S03, S05 and S07. Part 1 fails in S09, whose 76-100 Hz mean is not positive, under both event sets.",
"fig5-band-power-differs-across-subjects": "**Result: reproduced.** Kruskal-Wallis across the 12 subjects gives p below 1e-300 (printed as 0) for LFB (H = 762.0) and HFB (H = 1244.4) under (b1), and under (b3) (H = 773.9 and 1253.1), with the band median as well.",
"table1-subject-band-power-ci": "**Result: partially reproduced.** No reading puts all 24 subject and band values inside the paper's intervals. The best reading is 21 of 24 under (b1) (band mean, median over events) and 22 of 24 under (b3) (band mean, mean over events); both are at least 18. Under (b1) the band mean averaged over events, the Methods' reading, gives 8 of 24, pulled by events with zeroed ECoG (values to +-311 dB). LFB is below 0 in 12 of 12 subjects and HFB above 0 in 12 (b1, best reading) and 11 (b3) of 12.",
"fig5-recording-day-effects": "**Result: partially reproduced.** 23 of the 24 subject and band pairs agree with the paper's pattern of significant day effects, under (b1) and (b3) and with the band mean or median. The pair that differs is S10 HFB, significant in the paper (p = 0.006) and not here (p = 0.452 under (b1), 0.200 under (b3)).",
"extfig5-1-baseline-reduces-day-variability": "**Result: reproduced.** The SD across days of the day means is lower with baseline subtraction than without in 10 and 9 of 12 subjects (LFB, HFB) for the precentral region and in 1018 and 971 of 1144 electrodes under (b1); in 10 and 11 of 12 subjects and 1028 and 1006 electrodes under (b3). Variability remains: fig5-recording-day-effects finds 10 significant day effects.",
"discussion-day-changes-small": "**Result: blocked (methods underspecified).** Under (b3) every day mean is within 1.00 dB of its subject's mean and the level without baseline is 12.3 to 36.4 dB in microvolts, so both parts hold. Under (b1) the largest deviation is 8.15 dB (S10), above 2.2 dB in S02, S06 and S10, and the level is 8.5 to 35.4 dB; both fail, because of 42 events whose precentral ECoG is zeroed in the window. The two open readings of the segment rejection give different outcomes (question asked). In volts every level is below 0 dB.",
}
EOF
cat > $TMPDIR/build/results2.py <<'EOF'
R2 = {
"fig6-r2-at-most-025": "**Result: reproduced.** The largest split-averaged withheld R2 over good electrodes and both bands is 0.2626 (S04, HFB), at most 0.275. With electrodes marked bad included it is 1.0000, from a bad electrode. These R2 correlate with the R2 columns stored in the dataset's electrode table (0.74 for LFB, 0.706 for HFB).",
"fig6b-best-models-sensorimotor": "**Result: reproduced.** Under reading (a), all 12 LFB and 6 HFB models with R2 > 0.05 are at electrodes assigned to the five frontoparietal regions (fraction 1.000), and the median R2 of sensorimotor electrodes is above that of temporal ones (-0.0172 against -0.0210 for LFB, -0.0185 against -0.0212 for HFB). Under reading (b) the three regions with the highest projected R2 are precentral, postcentral and middle frontal in both bands. Few models pass 0.05 (18 of 1952 at good electrodes), from four subjects.",
"fig6c-angle-and-day-most-informative": "**Result: reproduced.** Over the 12 LFB models with R2 > 0.05, reach angle (median Delta R2 0.0823) and day of recording (0.0104) have the two largest medians; over the 6 HFB models day (0.1708) and reach angle (0.0127) are first and second. The code's Delta R2 gives the same top two. With selection by LFB R2, or with bad electrodes included, the HFB medians are all 0.",
"extfig6-2-angle-most-retained": "**Result: not reproduced.** Reach angle has the highest retention probability in none of the six sensorimotor region and band pairs; bimanual ratio is the most retained feature in every one of them (0.454 to 0.598). Averaged over the three sensorimotor regions and both bands, the order after bimanual ratio (0.526) is bimanual overlap, reach duration, day and reach angle; over all eight regions it is reach duration, bimanual overlap, bimanual class and day.",
"fig6d-upward-reaches-enhance-pattern": "**Result: reproduced.** The median reach angle coefficient is -1.3385 over the 12 LFB models with R2 > 0.05 (all negative) and +0.4067 over the 6 HFB models (none negative). With selection by LFB R2 the HFB median is 0.0000, and with bad electrodes included both medians are 0.0000.",
"fig6d-angle-and-day-largest-coefficients": "**Result: reproduced.** In both bands and under both readings reach angle and day of recording have the two largest coefficient magnitudes: LFB 1.3385 and 0.6102, HFB 1.1390 (day) and 0.4067 (angle). With selection by LFB R2 the HFB top two are reach duration and day; with bad electrodes included, reading (b) gives day and time of day.",
}
EOF
cd $TMPDIR/build && python - <<'EOF'
import re
exec(open('results1.py').read()); exec(open('results2.py').read())
def insert(src, R):
    s=open(src).read()
    for cid, text in R.items():
        tag=f'# %% tags=claim:{cid}\n'
        i=s.index(tag)
        j=s.index('\n# %%', i+len(tag))
        md='\n# %% [markdown]\n' + '\n'.join('# '+l for l in wrap(text)) + '\n'
        s=s[:j]+'\n'+md.rstrip('\n')+'\n'+s[j:]
    open(src,'w').write(s)
import textwrap
def wrap(t): return textwrap.wrap(t, 96, break_long_words=False, break_on_hyphens=False)
insert('nb1.py', R1); insert('nb2.py', R2)
EOF
grep -c "Result:" nb1.py nb2.py
```

```
nb1.py:20
nb2.py:6
Shell cwd was reset to
```

**Agent**

Fixing two conclusion sentences that the printed numbers don't quite support (the angle peak ranges, and the ±311 dB range, which is −311 to +317):

**Agent calls Bash**

```bash
cd $TMPDIR/build && python - <<'EOF'
import textwrap
s=open('nb1.py').read()
def w(t): return '\n'.join('# '+l for l in textwrap.wrap(t,96,break_long_words=False,break_on_hyphens=False))
old=[l for l in s.split('\n# %% [markdown]\n') if l.startswith('# **Result: partially reproduced.** More than half of the reaches')][0]
new=w("**Result: partially reproduced.** More than half of the reaches last under 2 s and cover under 200 pixels in all 12 subjects and pooled (pooled 0.918 and 0.914 under (b1)). The reach angle part does not hold under (b1), (b3) or (a): the highest density peak is at 62 to 75 degrees in every subject, the other peak below 0 is at -54 to -73 degrees in nine subjects (S02 and S06 have it near 0 and S04 has one peak), and in 0 of 12 subjects and pooled (-72 and 75 degrees) are both peaks within 15 degrees of +-90.")
s=s.replace(old.split('\n\n')[0], new)
s=s.replace("pulled by events with zeroed ECoG (values to +-311 dB)","pulled by events with zeroed ECoG (event values from -311 to +317 dB)")
open('nb1.py','w').write(s)
EOF
grep -n "highest density peak\|from -311" $TMPDIR/build/nb1.py | cut -c1-80; grep -n "1.1390\|0.6102" $TMPDIR/o2.txt | head -3 | cut -c1-150
```

```
533:# part does not hold under (b1), (b3) or (a): the highest density peak is at
141:   (a) median |coef|: reach_angle 1.3385, day 0.6102, reach_duration 0.2420, bimanual_ratio 0.2391, bimanual_class 0.0169, time_of_day 0.0000, ons
142:   (b) |median coef|: reach_angle 1.3385, day 0.6102, bimanual_ratio 0.2391, time_of_day 0.0000, reach_magnitude 0.0000, reach_duration 0.0000, on
145:   (a) median |coef|: day 1.1390, reach_angle 0.4067, bimanual_class 0.2808, reach_magnitude 0.1309, speech_ratio 0.0788, time_of_day 0.0000, onse
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n -A2 "zeroed ECoG (values" $TMPDIR/build/nb1.py; grep -n -B1 -A1 "+-311" $TMPDIR/build/nb1.py
```

```
967-# mean averaged over events, the Methods' reading, gives 8 of 24, pulled by events with zeroed
968:# ECoG (values to +-311 dB). LFB is below 0 in 12 of 12 subjects and HFB above 0 in 12 (b1, best
969-# reading) and 11 (b3) of 12.
```

**Agent calls Bash**

```bash
cd $TMPDIR/build && sed -i '968s/# ECoG (values to +-311 dB)\./# ECoG (event values from -311 to +317 dB)./' nb1.py && sed -n 966,969p nb1.py; date -u
```

```
# 22 of 24 under (b3) (band mean, mean over events); both are at least 18. Under (b1) the band
# mean averaged over events, the Methods' reading, gives 8 of 24, pulled by events with zeroed
# ECoG (event values from -311 to +317 dB). LFB is below 0 in 12 of 12 subjects and HFB above 0 in 12 (b1, best
# reading) and 11 (b3) of 12.
Fri Oct 23 18:11:06 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/build && sed -i 's/# rejection (see "Event sets"); (b2) leaves no events in four subjects and is not used here./# rejection (see "Event sets"); (b2) leaves no events in three subjects and is not used here./' nb1.py && grep -n "three subjects and is not used" nb1.py | head -2; cd  && sed -i 's/(b2) leaves no$/(b2) leaves no/; s/    events in four subjects, so it cannot be the paper.s rule./    events in three subjects (S09, S10, S12), so it cannot be the paper'"'"'s rule./' questions/000055.yaml && grep -n "three subjects" questions/000055.yaml
```

```
678:# rejection (see "Event sets"); (b2) leaves no events in three subjects and is not used here.
34:    events in three subjects (S09, S10, S12), so it cannot be the paper's rule. Between (b1) and (b3) about 40
```

**Agent calls Bash**

```bash
sed -i 's/Between (b1) and (b3) about 40$/Between (b1) and (b3) 55/; s/Between (b1) and (b3) about 40 /Between (b1) and (b3) 55 /' questions/000055.yaml && sed -n 30,40p questions/000055.yaml && python -c "import yaml;yaml.safe_load(open('questions/000055.yaml'))"
```

```
In volts every segment is below 0 dB and all events would be dropped; per electrode, more
    segments fail than on the mean. The event counts of fig2-event-counts are within tolerance
    with the false positives alone removed, so a rule that drops many segments moves them out
    of tolerance, and the drop changes the events of every reading-(b) claim. (b2) leaves no
    events in three subjects (S09, S10, S12), so it cannot be the paper's rule. Between (b1) and (b3) 55
    events differ, but their band power is near +-300 dB (zeroed ECoG), so means over events
    differ widely: under (b1) the band-mean and event-mean reading of Table 1 matches 8 of 24
    intervals.
```

**Agent calls Bash**

```bash
sed -i 's/    events differ, but their band power is near +-300 dB (zeroed ECoG), so means over events/    events differ; 42 of them have precentral band power near +-300 dB (zeroed ECoG), so means over events/' questions/000055.yaml && python -c "import yaml;yaml.safe_load(open('questions/000055.yaml'))" && cd $TMPDIR/build && python - <<'EOF'
s=open('nb1.py').read()
summ='''# %% [markdown]
# ## Summary
#
# | Claim | Outcome | Notebook |
# |---|---|---|
# | figshare-event-link (link) | reproduced | this one |
# | figshare-roi-link (link) | reproduced | this one |
# | subject-days (link) | reproduced | this one |
# | cohort | partially reproduced | this one |
# | fig2-event-counts | reproduced | this one |
# | fig2-features-differ-across-subjects | reproduced | this one |
# | fig2-reach-shape | partially reproduced | this one |
# | fig2-bimanual-skew | blocked, methods underspecified | this one |
# | extfig2-1c-contralateral-larger | reproduced | this one |
# | extfig2-2-feature-correlations | reproduced | this one |
# | fig2-days-and-waking | partially reproduced | this one |
# | fig3-group-lfb-decrease-hfb-increase | reproduced | this one |
# | fig3-sensorimotor-largest | reproduced | this one |
# | fig3-lfb-more-widespread | reproduced | this one |
# | fig4-precentral-subject-variability | partially reproduced | this one |
# | fig5-band-power-differs-across-subjects | reproduced | this one |
# | table1-subject-band-power-ci | partially reproduced | this one |
# | fig5-recording-day-effects | partially reproduced | this one |
# | extfig5-1-baseline-reduces-day-variability | reproduced | this one |
# | discussion-day-changes-small | blocked, methods underspecified | this one |
# | fig6-r2-at-most-025 | reproduced | regression |
# | fig6b-best-models-sensorimotor | reproduced | regression |
# | fig6c-angle-and-day-most-informative | reproduced | regression |
# | extfig6-2-angle-most-retained | not reproduced | regression |
# | fig6d-upward-reaches-enhance-pattern | reproduced | regression |
# | fig6d-angle-and-day-largest-coefficients | reproduced | regression |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# How the analysis differs from the paper's:
#
# - The false-positive flags are read from the paper's Figshare epoch files, linked to the
#   dataset's events by their timestamps; the dataset does not mark the false positives.
# - The regions use the paper's own projection matrices from Figshare, not a new projection from
#   the AAL atlas, and the bad electrodes of each file are set to 0 before renormalising.
# - The PSD rejection of segments is not specified beyond "power <0 dB" and "abnormally high
#   power at 115-125 Hz (>3 SDs)"; three readings are run and a question is asked. Two claims
#   are blocked because readings (b1) and (b3) give different outcomes.
# - The ECoG of three files is read on a clock shifted by the session start (see the clock check).
# - Kernel density, peak and tie rules of fig2-reach-shape and fig4 are standard choices stated
#   in their cells.
#
# What was found about the dataset:
#
# - It holds the 12 subjects and 55 days of the paper and 8088 events, 1157 of which the paper's
#   Figshare files mark as false positives; the dataset has no flag for them, and with them the
#   per-subject counts do not match the paper's (211 to 996, median 770.5).
# - In sub-01 day 7, sub-04 day 3 and sub-06 day 3 the ECoG starts at the session start while the
#   pose and the events count from midnight, but the ECoG's starting time is stored as 0; on the
#   stored clock 237 events lie beyond the end of the ECoG, and the movement response appears only
#   on the shifted clock.
# - Session start times are stored at offset -05:00, but the sleep labels fall at night only when
#   they are read on the UTC clock.
# - The pose is labelled in meters but holds pixels; the ECoG is labelled volts with conversion
#   1e-6, consistent with values in microvolts.
# - Bimanual overlap is described as a fraction of the movement duration but holds seconds
#   (frames of the Figshare files divided by 30).
# - The electrode groups whose description says "depth" are in 7 subjects, where the paper
#   counts 5 subjects with depth electrodes.
# - Some events have ECoG zeroed in the analysed window (42 of the events kept by reading b1);
#   the files do not mark the zeroed stretches.
# - Sex and age of the subjects are not in the files.
'''
i=s.index('# %% [markdown]\n# ## Summary')
j=s.index('# %%\nprint(f"notebook ran in')
s=s[:i]+summ+'\n'+s[j:]
open('nb1.py','w').write(s)
s=open('nb2.py').read()
summ2='''# %% [markdown]
# ## Summary
#
# | Claim | Outcome |
# |---|---|
# | fig6-r2-at-most-025 | reproduced |
# | fig6b-best-models-sensorimotor | reproduced |
# | fig6c-angle-and-day-most-informative | reproduced |
# | extfig6-2-angle-most-retained | not reproduced |
# | fig6d-upward-reaches-enhance-pattern | reproduced |
# | fig6d-angle-and-day-largest-coefficients | reproduced |
#
# The other claims are in `reproduce_peterson_2021.ipynb`, with the full table.
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# How the analysis differs from the paper's: the events are those of rejection reading (b1)
# only, and the readings (b3) and the code's 80/20 split, median band power and log(x + 1)
# transforms were not run, for time; electrodes are those marked good on every day of the
# subject (electrodes good on some days only are in the bad-electrode variant); the region
# assignment uses the paper's projection matrices. Only 18 of 1952 models at good electrodes
# reach a withheld R2 above 0.05, so the claims on those models rest on 12 LFB and 6 HFB models
# from four subjects.
#
# What was found about the dataset: the electrode table holds R2 columns (`low_freq_R2`,
# `high_freq_R2`) without a description of how they were computed; the R2 here correlate with
# them (0.74 and 0.706).
'''
i=s.index('# %% [markdown]\n# ## Summary')
j=s.index('# %%\nprint(f"notebook ran in')
s=s[:i]+summ2+'\n'+s[j:]
open('nb2.py','w').write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent**

Summaries are written. Rebuilding the notebooks and starting the final full run (about 45 min):

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && . $TMPDIR/dev/bin/activate && python $TMPDIR/build/conv.py $TMPDIR/build/nb1.py reproduce_peterson_2021.ipynb && python $TMPDIR/build/conv.py $TMPDIR/build/nb2.py reproduce_peterson_2021_regression.ipynb && deactivate && cd ../.. && date -u && python tools/entry.py all entries/000055-peterson-2021 2>&1 | tail -3; date -u
```

```
Fri Oct 23 18:11:46 UTC 2026
0 error(s)
pass  reproduce_peterson_2021.ipynb  (997 s)
pass  reproduce_peterson_2021_regression.ipynb  (1640 s)
Fri Oct 23 18:56:05 UTC 2026
```

**Agent**

Final run passes: 16.6 and 27.3 min. Checking that the printed numbers match the run the conclusions were written from:

**Agent calls Bash**

```bash
cd executed/000055-peterson-2021 && python - <<'EOF'
import nbformat
for nbn, old in (('reproduce_peterson_2021','/tmp/claude-1001/o1.txt'),('reproduce_peterson_2021_regression','/tmp/claude-1001/o2.txt')):
    nb=nbformat.read(nbn+'.ipynb',4)
    out=[]
    for i,c in enumerate(nb.cells):
        if c.cell_type!='code': continue
        t=''.join(o.get('text','') for o in c.outputs if o.output_type=='stream' and o.name=='stdout')
        out.append(t)
    new='\n'.join(out).splitlines()
    o=[l for l in open(old).read().splitlines() if not l.startswith('=== cell')]
    import difflib
    d=[l for l in difflib.unified_diff([x for x in o if x.strip()],[x for x in new if x.strip()],lineterm='',n=0) if l[:1] in '+-' and not l.startswith(('+++','---'))]
    print(nbn, len(d)); print('\n'.join(x[:160] for x in d[:20]))
EOF
```

```
reproduce_peterson_2021 10
-55 assets in the version, 55 read; 55 Figshare epoch files; loaded in 42 s
+55 assets in the version, 55 read; 55 Figshare epoch files; loaded in 43 s
-(34 s)
-spectral pass over 8088 events in 55 files: 877 s (slowest file 408 s)
+(33 s)
+spectral pass over 8088 events in 55 files: 853 s (slowest file 405 s)
-wrist traces read in 23 s; 91 frames from -1.5 to 1.5 s
+wrist traces read in 24 s; 91 frames from -1.5 to 1.5 s
-notebook ran in 16.9 min
+notebook ran in 16.5 min
reproduce_peterson_2021_regression 8
-band power for 8088 events and 2368 models in 1607 s; subjects read at (s): {12: 459, 8: 481, 6: 483, 11: 492, 3: 569, 1: 585, 7: 609, 2: 636, 5: 644, 4: 645, 
-events per subject used: {12: 946, 8: 849, 6: 851, 11: 892, 3: 580, 1: 659, 7: 671, 2: 204, 5: 199, 4: 268, 10: 618, 9: 150}
-columns of the design: {12: 16, 8: 16, 6: 16, 11: 16, 3: 15, 1: 15, 7: 16, 2: 15, 5: 14, 4: 16, 10: 16, 9: 16}
+band power for 8088 events and 2368 models in 1590 s; subjects read at (s): {8: 471, 11: 477, 6: 495, 12: 522, 1: 572, 3: 574, 10: 606, 7: 628, 2: 639, 4: 652,
+events per subject used: {8: 849, 11: 892, 6: 851, 12: 946, 1: 659, 3: 580, 10: 618, 7: 671, 2: 204, 4: 268, 5: 199, 9: 150}
+columns of the design: {8: 16, 11: 16, 6: 16, 12: 16, 1: 15, 3: 15, 10: 16, 7: 16, 2: 15, 4: 16, 5: 14, 9: 16}
-notebook ran in 27.5 min
+notebook ran in 27.2 min
```

**Agent**

Only timings and dict ordering differ; every result is identical. Writing the README and the attempt record now (18:57).

**Agent calls Write**

```json
{
 "file_path": "entries/000055-peterson-2021/README.md",
 "content": "# Peterson, Singh, Wang, Rao & Brunton (2021) from dandiset 000055\n\nTests the findings of [Peterson et al. (2021)](https://doi.org/10.1523/ENEURO.0007-21.2021) on\n[DANDI:000055](https://dandiarchive.org/dandiset/000055/0.220127.0436) (AJILE12), which holds the\nECoG, upper-body pose and wrist movement events of the paper's 12 subjects over 55 days.\n\n| Claim | Outcome |\n|---|---|\n| The dataset's subjects and days are the paper's (link) | Reproduced |\n| The Figshare false-positive flags and projection matrices match the dataset (two links) | Reproduced |\n| Cohort: subjects, electrodes, hemispheres | Partially reproduced |\n| 151 to 947 events per subject, median 640 | Reproduced |\n| All ten features differ across subjects | Reproduced |\n| Reach duration and magnitude; bimodal reach angle | Partially reproduced |\n| Bimanual features skewed to unimanual | Blocked: methods underspecified |\n| Contralateral wrist moves more than ipsilateral | Reproduced |\n| Correlations between features | Reproduced |\n| Days with most events; waking hours | Partially reproduced |\n| Group LFB decrease and HFB increase at movement onset | Reproduced |\n| Changes largest in sensorimotor regions | Reproduced |\n| LFB decreases more widespread than HFB increases | Reproduced |\n| Precentral spectra vary across subjects | Partially reproduced |\n| Precentral band power differs across subjects | Reproduced |\n| Per-subject band power in the Table 1 intervals | Partially reproduced |\n| Recording-day effects on band power | Partially reproduced |\n| Baseline subtraction reduces day-to-day variability | Reproduced |\n| Day-to-day changes are 1-2 dB | Blocked: methods underspecified |\n| Withheld R2 at most 0.25 | Reproduced |\n| Best models at sensorimotor electrodes | Reproduced |\n| Reach angle and day most informative | Reproduced |\n| Reach angle most often retained by forward selection | Not reproduced |\n| Upward reaches enhance the movement response | Reproduced |\n| Reach angle and day have the largest coefficients | Reproduced |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe dataset does not mark the 1157 events the paper treated as false positives; their flags are\nread from the paper's Figshare epoch files, linked by timestamp. The regions use the paper's own\nprojection matrices from Figshare. In three files the ECoG starts at the session start while the\nevents count from midnight, which the files do not say; the notebook shows it and reads those\nfiles on the shifted clock. How the paper rejected segments on their power spectral density is\nnot specified; three readings are run and a question is open. The attempt record, with the\nreasons and the differences from the paper's method, is\n[`attempts/000055-peterson-2021-01.yaml`](../../attempts/000055-peterson-2021-01.yaml).\n\n- `reproduce_peterson_2021.ipynb`: the data check, the link claims, the behaviour claims and the\n  spectral claims. About 17 minutes, most of it streaming about 170 GB of ECoG around the events.\n- `reproduce_peterson_2021_regression.ipynb`: the regression claims of Figure 6. About 27\n  minutes: it streams the ECoG again and fits 2368 models of 200 splits each.\n- `ajile.py`: loading the files and the Figshare inputs, the spectral measures, the segment\n  rejection, the region projection and the regression. Other notebooks on this dandiset can\n  import it.\n"
}
```

```
The file entries/000055-peterson-2021/README.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  sed -n 250,420p attempts/001453-fouke-2025-01.yaml | grep -n "verifications\|^[a-z]" | head; grep -n "findings\|inputs" -A3 schemas/attempt.schema.json | grep -E '"(what|source|kind|statement|claims)"' | head
```

```
60:verifications:
```

**Agent calls Bash**

```bash
python -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']['properties']
for k in ['measured','deviations','proposed']: print(k, json.dumps(o.get(k))[:600])
print(json.dumps(s['properties']['inputs'])[:600]); print(json.dumps(s['properties']['findings'])[:700])"
```

```
measured {"description": "The values obtained, for claims with expected values: one number, or one per expected value, in the same order.", "oneOf": [{"type": "number"}, {"type": "array", "minItems": 1, "items": {"type": "number"}}]}
deviations {"description": "How the test differed from the paper's method or data, e.g. one session of four, or a substituted model.", "type": "array", "items": {"type": "string", "minLength": 1}}
proposed {"description": "A change of outcome found after the last verification round, held until a further round agrees with it.", "type": "object", "additionalProperties": false, "required": ["outcome", "reason"], "properties": {"outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}, "blocked_by": {"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "too_large", "not_runnable", "other"]}, "reason": {"type": "string", "minLength": 1}}}
{"description": "Everything the attempt used that is not in the dataset.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["what", "source"], "properties": {"what": {"type": "string", "minLength": 1}, "source": {"description": "A DOI, or a repository URL with the commit read.", "type": "string", "minLength": 1}}}}
{"description": "What the attempt found about the dataset itself, whatever the outcomes. These roll up into the per-dataset report.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["kind", "statement"], "properties": {"kind": {"enum": ["metadata_error", "data_missing", "identifier_missing", "metadata_insufficient", "selection_undocumented", "methods_unavailable", "format_error", "code_mismatch", "paper_inconsistency", "other"]}, "statement": {"type": "string", "minLength": 1}}}}
```

**Agent**

Writing the attempt record (built in Python and dumped, so any scalar containing ": " gets quoted):

**Agent calls Bash**

```bash
cat > $TMPDIR/build/record.py <<'PYEOF'
import yaml
NB1 = "reproduce_peterson_2021.ipynb"
NB2 = "reproduce_peterson_2021_regression.ipynb"
B1B3 = ("Readings (b1) and (b3) of the segment rejection are the attempt's readings of the Methods' "
        "PSD rule (question in questions/000055.yaml); the claims file does not say how the PSD is computed.")
REG = ("Events of rejection reading (b1) only; reading (b3), the code's 80/20 split, the median band power "
       "and the code's log(x + 1) transforms were not run, as a second set of 2368 models does not fit "
       "in the notebook's 30 minutes (the main fits take about 27 minutes with the streaming).")
REG2 = ("Electrodes are those marked good on every day of the subject (1952 of 2368 models); the "
        "claims file says good electrodes without saying how a per-day flag is combined. Electrodes good "
        "on some days only are in the bad-electrode variant.")
o = []
def add(claim, outcome, notes, nb=NB1, deviations=None, measured=None, blocked_by=None):
    d = {"claim": claim, "outcome": outcome}
    if blocked_by: d["blocked_by"] = blocked_by
    d["notebook"] = nb
    d["output"] = f"claim:{claim}"
    if measured is not None: d["measured"] = measured
    d["notes"] = notes
    if deviations: d["deviations"] = deviations
    o.append(d)

add("subject-days", "reproduced",
    "The 12 subjects hold exactly the days of Table 2, 55 subject-days. The subject ids inside the files equal "
    "the file names, and the Figshare epoch files carry the same subject and day pairs, so S01 to S12 are the "
    "dataset's subjects 01 to 12.")
add("cohort", "partially_reproduced",
    "12 subjects. Mean surface electrodes 84.8 (SD 11.6; paper 87.0 +- 12.9). Groups whose description says "
    "depth are in 7 subjects (paper 5), with a mean of 23.7 depth electrodes among them (SD 13.4; paper 23.2 +- 12.1). "
    "5 subjects are implanted on the right by the mean x coordinate and by the reaching wrist (paper 5). Sex and "
    "age are not in the files, so the 8 males and the mean age of 29.4 years are not testable; no measured "
    "values are given as two of the seven expected values cannot be measured.",
    deviations=["Surface and depth electrodes are told apart by the group descriptions in the files; the "
                "per-subject electrode table of the paper (Extended Data Figure 1-1) was not available."])
add("fig2-event-counts", "reproduced",
    "Reading (b) matches. (b1) gives fewest 150, most 946, median 638.5; (b3) gives 150, 942 and 627.0; the "
    "Figshare false positives alone give 151, 947 and 639.5, the paper's numbers. Reading (a), all 8088 events "
    "of the dataset, gives 211, 996 and 770.5, outside tolerance for the fewest and the median. Rejection "
    "reading (b2) leaves no events in S09, S10 and S12.",
    measured=[150, 946, 638.5],
    deviations=["The false-positive flags come from the paper's Figshare epoch files (link claim "
                "figshare-event-link); the dataset holds none.", B1B3])
add("fig2-features-differ-across-subjects", "reproduced",
    "Kruskal-Wallis across subjects gives p < 0.001 for all ten features under (b1), (b3), (a) and (b2); the "
    "largest p is 1.47e-30 (reach angle) under (b1) and 6.03e-30 under (b3).",
    deviations=[B1B3, "Time of day is tested as the hour of the day on the midnight clock of the events."])
add("fig2-reach-shape", "partially_reproduced",
    "More than half of the reaches last under 2 s and cover under 200 pixels in 12 of 12 subjects and pooled "
    "(pooled 0.918 and 0.914 under (b1)); the per-subject medians are 1.03 to 1.30 s and 64.7 to 173.7 px. The "
    "angle part fails: the highest density peak is at 62 to 75 degrees in every subject, the other peak below 0 "
    "at -54 to -73 degrees in nine subjects, and in 0 of 12 subjects and pooled (-72 and 75 degrees) are both "
    "peaks within 15 degrees of +-90. The same under (b3) and (a).",
    deviations=["The criterion names no event set; (b1), (b3) and (a) are shown and agree.",
                "A grid end point counts as a density peak when higher than its neighbour (a standard choice)."])
add("fig2-bimanual-skew", "blocked", blocked_by="methods_underspecified",
    notes="The ratio, overlap and class parts hold pooled and in 12 of 12 subjects under every event set (pooled "
    "median ratio 0.115, overlap skewness 1.094, fraction bimanual 0.717 under (b1)). S02, S04 and S05 are among "
    "the five highest median ratios under every set. Among the five lowest overlap skewness S04 is under (b3) and "
    "(a) but not under (b1), where S10 takes its place, so the claim is reproduced under (b3) and (a) and "
    "partially reproduced under (b1). The criterion names no event set, and the rejection rule that separates "
    "(b1) from (b3) is the open question.",
    deviations=[B1B3])
add("extfig2-1c-contralateral-larger", "reproduced",
    "The peak of the median contralateral displacement over 0 to 1.5 s exceeds the ipsilateral one in 12 of 12 "
    "subjects under both rest positions and under (b1), (b3) and (a). Under rest reading (a) and events (b1) the "
    "ratio is 1.30 (S04) to 39.8 (S12), and S02, S04 and S05 have ratios of 1.66, 1.30 and 1.43. Contralateral "
    "peaks are 55.8 to 157.2 pixels.",
    deviations=["Pose and events are read on their shared midnight clock; 0.7% of events have a missing pose frame, "
                "skipped by the medians."])
add("extfig2-2-feature-correlations", "reproduced",
    "Under (b1), 6887 events, the correlations are 0.259, 0.562, 0.475, 0.508, 0.496 and 0.609, all within 10% "
    "of the paper's. Under (b3) also 6 of 6. With all events (a), 5 of 6 (magnitude and duration 0.231).",
    measured=[0.259, 0.562, 0.475, 0.508, 0.496, 0.609], deviations=[B1B3])
add("fig2-days-and-waking", "partially_reproduced",
    "The busiest day holds more than half of the events in S05 (0.628) and S09 (0.553) but not in S04 (0.429, "
    "day 7 with 115 of 268), and in none of the other nine subjects (0.203 to 0.324), under (b1); (b3) and (a) "
    "name the same two subjects. More than half of the events fall between 08:00 and 24:00 in 12 of 12 subjects "
    "(0.662 to 0.970). Only the waking part holds.",
    deviations=["Hours are on the midnight clock of the events, which the sleep labels support; the stored session "
                "start times carry an offset of -05:00 that does not fit the sleep labels."])
add("fig3-group-lfb-decrease-hfb-increase", "reproduced",
    "In precentral, postcentral and inferior parietal regions the masked 4-30 Hz mean is negative and the "
    "50-120 Hz mean positive under both readings and both event sets; under (b1) and reading (a) precentral "
    "-0.871 and 0.480 dB, postcentral -0.866 and 0.499, inferior parietal -0.684 and 0.276. Under (b1) the "
    "pattern holds in 7 of 8 regions by reading (a) and 4 of 8 by reading (b).",
    deviations=["Regions use the paper's Figshare projection matrices (link claim figshare-roi-link).", B1B3,
                "The ECoG of three files is read on the clock shifted by the session start."])
add("fig3-sensorimotor-largest", "reproduced",
    "Under readings (a), (b) and (c) and both event sets, precentral, postcentral and inferior parietal are the "
    "three largest of the eight regions and every temporal region is below all three. Reading (a) under (b1): "
    "postcentral 0.502, precentral 0.495, inferior parietal 0.325 dB against 0.045, 0.003 and 0.018 for the "
    "temporal regions.",
    deviations=["Regions use the paper's Figshare projection matrices.", B1B3])
add("fig3-lfb-more-widespread", "reproduced",
    "Under (b1), 8 regions have a significant negative LFB bin and 7 a significant positive HFB bin over 0 to "
    "0.5 s (reading a), and there are 36.2 negative bins per LFB frequency bin against 23.4 positive bins per HFB "
    "frequency bin (reading b); supramarginal and superior temporal have 30 and 25 negative LFB bins. (b3) gives "
    "8 against 7 and 35.2 against 23.9.",
    deviations=["Regions use the paper's Figshare projection matrices.", B1B3])
add("fig4-precentral-subject-variability", "partially_reproduced",
    "Three of four parts hold under both event sets. Part 1 fails in S09, whose 76-100 Hz mean is not positive "
    "(its spectrum is near 0 above 50 Hz); the other 11 subjects show the pattern. Part 2 holds (116 and 121 Hz "
    "positive in S03, S06, S07, S08, S11). Part 3 holds (largest 56-121 Hz bin at 71 Hz in S09 and 66 Hz in "
    "S12). Part 4: widths are 1 bin for S08 and 2 for S04 under (b1), the two smallest; under (b3) S08 has 2 and "
    "S04 shares the third smallest width (3) with S02, S03, S05 and S07, which is counted as among the three "
    "fewest; breaking the tie by subject order would leave S04 out, and the outcome would still be partial.",
    deviations=["Ties in the width of part 4 count as at or below the third smallest (the paper implies no tie rule).",
                "Regions use the paper's Figshare projection matrices.", B1B3])
add("fig5-band-power-differs-across-subjects", "reproduced",
    "Kruskal-Wallis across the 12 subjects gives p below 1e-300 (printed as 0) for LFB (H = 762.0) and HFB "
    "(H = 1244.4) under (b1), 6887 events, and under (b3), 6832 events (H = 773.9 and 1253.1); the band median "
    "gives the same.",
    deviations=["Regions use the paper's Figshare projection matrices.", B1B3])
add("table1-subject-band-power-ci", "partially_reproduced",
    "No reading puts all 24 values inside the paper's intervals. The best is 21 of 24 under (b1) (band mean, "
    "median over events; S02 LFB, S06 LFB and S10 LFB outside) and 22 of 24 under (b3) (band mean, mean over "
    "events). Under (b1) the band mean averaged over events gives 8 of 24, because 42 events with zeroed ECoG in "
    "the window have values from -311 to +317 dB. LFB is below 0 in 12 of 12 subjects and HFB above 0 in 12 "
    "(b1) and 11 (b3) of 12 under the best readings.",
    deviations=["Regions use the paper's Figshare projection matrices.", B1B3])
add("fig5-recording-day-effects", "partially_reproduced",
    "23 of 24 subject and band pairs agree with the paper's pattern under (b1) and (b3), with the band mean or "
    "median; 10 pairs are significant. S10 HFB differs, significant in the paper (p = 0.006) and not here "
    "(p = 0.452 under (b1), 0.200 under (b3)); S10 has 19 of the 42 zeroed events of (b1).",
    deviations=["Regions use the paper's Figshare projection matrices.", B1B3])
add("extfig5-1-baseline-reduces-day-variability", "reproduced",
    "SD across days of the day means is lower with baseline than without in 10 and 9 of 12 subjects (LFB, HFB, "
    "reading a) and in 1018 and 971 of 1144 electrodes (reading b) under (b1); 10 and 11 of 12 and 1028 and 1006 "
    "under (b3). fig5-recording-day-effects finds 10 significant day effects, so variability remains. Median SD "
    "per electrode under (b3) is 0.265 and 0.232 dB with baseline against 0.794 and 0.612 without.",
    deviations=["Regions use the paper's Figshare projection matrices.", B1B3])
add("discussion-day-changes-small", "blocked", blocked_by="methods_underspecified",
    notes="The readings of the segment rejection give different outcomes. Under (b3) the largest deviation of a "
    "day mean from its subject's mean is 1.00 dB and the level without baseline is 12.3 to 36.4 dB in "
    "microvolts, so both parts hold (reproduced). Under (b1) it is 8.15 dB (S10), above 2.2 dB in S02, S06 and "
    "S10, and the level is 8.5 to 35.4 dB, so both parts fail (not reproduced); 42 events with zeroed ECoG "
    "cause both. In volts every level is below 0 dB (-111.5 to -83.6).",
    deviations=["Regions use the paper's Figshare projection matrices.", B1B3])
add("fig6b-best-models-sensorimotor", "reproduced", nb=NB2,
    notes="Reading (a): all 12 LFB and 6 HFB models with R2 > 0.05 are at electrodes assigned to the five "
    "frontoparietal regions (fraction 1.000), and the median R2 of sensorimotor electrodes is above that of "
    "temporal ones (-0.0172 against -0.0210 LFB, -0.0185 against -0.0212 HFB). Reading (b): the three regions "
    "with the highest projected R2 are precentral, postcentral and middle frontal in both bands. Only 18 of 1952 "
    "models at good electrodes pass 0.05, from S01, S03, S04 and S07, so the result rests on few models.",
    deviations=[REG, REG2, "Regions use the paper's Figshare projection matrices."])
add("fig6-r2-at-most-025", "reproduced", nb=NB2, measured=0.2626,
    notes="The largest split-averaged withheld R2 over good electrodes and both bands is 0.2626 (S04, HFB), at "
    "most 0.275. With electrodes marked bad included it is 1.0000, at a bad electrode. The R2 here correlate "
    "with the dataset's stored low_freq_R2 and high_freq_R2 columns (0.74 and 0.706); the largest stored values "
    "are 0.149 and 0.255.",
    deviations=[REG, REG2])
add("fig6c-angle-and-day-most-informative", "reproduced", nb=NB2,
    notes="LFB, 12 models with R2 > 0.05: reach angle (median Delta R2 0.0823) and day (0.0104) are the top two. "
    "HFB, 6 models: day (0.1708) then reach angle (0.0127). The code's Delta R2 gives the same top two. With "
    "selection by LFB R2 or with bad electrodes included the HFB medians are all 0, and with bad electrodes "
    "the LFB median of reach angle is 0.0040 and of day 0.",
    deviations=[REG, REG2])
add("extfig6-2-angle-most-retained", "not_reproduced", nb=NB2,
    notes="Reach angle has the highest retention probability in none of the six sensorimotor region and band "
    "pairs (0.182 to 0.341); bimanual ratio is the most retained in all six (0.454 to 0.598). Averaged over the "
    "three sensorimotor regions and both bands the order is bimanual ratio, bimanual overlap, reach duration, "
    "day, reach angle; over all eight regions bimanual ratio, reach duration, bimanual overlap, bimanual class, "
    "day. Forward selection runs by OLS on all of a subject's events, so it does not depend on the splits.",
    deviations=[REG, REG2, "A one-hot feature counts as retained when its columns are selected together, as the "
                "selection here adds whole features; the criterion's 1/columns weighting then gives 1."])
add("fig6d-upward-reaches-enhance-pattern", "reproduced", nb=NB2,
    notes="Median reach angle coefficient -1.3385 over the 12 LFB models with R2 > 0.05 (all negative) and "
    "+0.4067 over the 6 HFB models (none negative). With selection by LFB R2 the HFB median is 0.0000 (8 of 12 "
    "zero); with bad electrodes included both medians are 0.0000.",
    deviations=[REG, REG2])
add("fig6d-angle-and-day-largest-coefficients", "reproduced", nb=NB2,
    notes="Under both readings reach angle and day have the two largest coefficient magnitudes in both bands: "
    "LFB 1.3385 and 0.6102, HFB 1.1390 (day) and 0.4067 (angle). The day value is the SD of its one-hot "
    "coefficients. With selection by LFB R2 the HFB top two are reach duration and day; with bad electrodes "
    "included reading (b) gives day and time of day.",
    deviations=[REG, REG2])
add("figshare-event-link", "reproduced",
    "All 8088 dataset events match exactly one Figshare record on the timestamp (100.0%), with no repeated "
    "timestamps, and the shared features agree to within 4.9e-07. The Figshare flags mark 1157 events (14.3%) "
    "as false positives, 49 to 186 per subject.")
add("figshare-roi-link", "reproduced",
    "Every subject's matrix has one row per channel; S01's has 4 more rows, all zero. The median distance "
    "between electrode positions and their weighted region centroids is 15.6 to 27.6 mm, below the smallest of "
    "200 shuffled orders in every subject (44.9 to 54.9 mm). The eight regions with mean density above 3 are "
    "the claims file's eight. Electrode positions differ between days in S03 and S12, and the first day's are "
    "used for the check.")

rec = {
 "schema_version": 2,
 "id": "000055-peterson-2021-01",
 "dataset": {"archive": "dandi", "id": "000055", "version": "0.220127.0436", "doi": "10.48324/dandi.000055/0.220127.0436"},
 "paper": "doi:10.1523/eneuro.0007-21.2021",
 "date": "2026-10-23",
 "entry": "000055-peterson-2021",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                "agent": {"harness": "Claude Code (GitHub Actions)", "model": "claude-opus-5-5", "protocol": "pilot-10"},
                "runner": {"platform": "GitHub Actions", "url": "https://github.com/catalystneuro/encore/actions/runs/39980867141"}},
 "inputs": [
  {"what": "The metadata tables of the paper's curated MNE epoch files (one per subject and day), read over HTTP from "
           "the files' tag directories for their false-positive flags; the ECoG in the files is not read.",
   "source": "doi:10.6084/m9.figshare.12115728.v1"},
  {"what": "The paper's projection matrices from electrodes to AAL regions (aal_XX_elecs2ROI.csv) and the region "
           "centroids (aal_XX_ROIcentroids_Lside.csv), used for every claim on regions.",
   "source": "doi:10.6084/m9.figshare.12114408.v1"},
 ],
 "outcomes": o,
 "findings": [
  {"kind": "data_missing", "statement": "The dataset holds 8088 wrist movement events without marking the 1157 the "
   "paper's Figshare epoch files flag as false positives (14.3%, 49 to 186 per subject). The data descriptor says the "
   "events were visually inspected and false positives removed (6931 events), but the files hold all 8088, so the "
   "per-subject counts are 211 to 996 against the paper's 151 to 947."},
  {"kind": "metadata_error", "statement": "In sub-01 ses-7, sub-04 ses-3 and sub-06 ses-3 the ECoG series is 15.5 to "
   "15.9 h long and starts at the session start, while the pose and the event times count from midnight; the ECoG's "
   "starting_time is stored as 0. On the stored clock 237 events lie beyond the end of the ECoG and no movement "
   "response is seen; shifted by the session start (30682, 30048 and 29241 s) every event falls inside the ECoG and "
   "the precentral LFB decrease appears (for example -1.69 against +0.39 dB in sub-06 ses-3)."},
  {"kind": "metadata_error", "statement": "Session start times are stored at offset -05:00 (19:00 the day before, or "
   "03:xx), but the Sleep/rest labels fall at night (00:00 to 06:00) only when the stored times are read on the UTC "
   "clock, which makes them midnight. Read with the stated offset, the sleep peak falls at 18:00 to 24:00."},
  {"kind": "metadata_error", "statement": "The pose series are labelled in meters but hold image pixels (values up to "
   "several hundred, and the reaches table states pixels)."},
  {"kind": "metadata_error", "statement": "Bimanual_overlap is described as a fraction of the contralateral movement "
   "duration, but it holds seconds: it equals the Figshare overlap in frames divided by 30, and reaches 3.83."},
  {"kind": "metadata_insufficient", "statement": "The electrode table's low_freq_R2 and high_freq_R2 columns are "
   "described only as R^2 for each band, without the model, events or splits behind them; they correlate 0.74 and "
   "0.71 with the regression R2 of this attempt."},
  {"kind": "metadata_insufficient", "statement": "The subjects' sex and age, given in the paper, are not in the files, "
   "and the electrode locations are all 'unknown'; whether an electrode is a depth electrode can only be read from "
   "the group descriptions, which give 7 subjects with depth electrodes where the paper reports 5."},
  {"kind": "other", "statement": "Some ECoG segments around events are zeroed (the preprocessing zeroes high-amplitude "
   "artifacts), without a mark in the files; 42 of the events kept by a whole-segment PSD rejection have zeroed "
   "precentral ECoG in the 0 to 0.5 s window, with band power near -300 dB, enough to change means over events."},
  {"kind": "other", "statement": "Electrode MNI positions differ between recording days within S03 and S12, though "
   "the channels are the same."},
  {"kind": "other", "statement": "The clock of the ECoG against the events could not be established by the movement "
   "response in 10 of 55 files (sub-02 days 3, 5, 6; sub-04 day 4; sub-08 day 7; sub-09 days 3, 4, 5, 7; sub-12 day "
   "6), mostly files with few events; it was shown in the other 45."},
 ],
}
class D(yaml.SafeDumper): pass
def str_rep(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)
D.add_representer(str, str_rep)
out = yaml.dump(rec, Dumper=D, sort_keys=False, width=100, allow_unicode=True)
open("attempts/000055-peterson-2021-01.yaml", "w").write(out)
print(len(o))
PYEOF
. $TMPDIR/dev/bin/activate && python $TMPDIR/build/record.py && deactivate && grep -n ": .*: " attempts/000055-peterson-2021-01.yaml | grep -v "^ *[0-9]*: *- \?[a-z_]*: '" | head; python tools/entry.py check entries/000055-peterson-2021 2>&1 | tail -5; date -u
```

```
26
261:  notes: 'Reading (a): all 12 LFB and 6 HFB models with R2 > 0.05 are at electrodes assigned to the five
295:  notes: 'LFB, 12 models with R2 > 0.05: reach angle (median Delta R2 0.0823) and day (0.0104) are the
0 error(s)
Fri Oct 23 18:58:03 UTC 2026
```

**Agent**

Record written and check passes. Rewording the two strings that contain ": " so every scalar can stay plain, and tightening the volts range wording:

**Agent calls Bash**

```bash
cd $TMPDIR/build && python - <<'EOF'
s=open('record.py').read()
s=s.replace('notes="Reading (a): all 12 LFB','notes="Under reading (a), all 12 LFB')
s=s.replace('temporal ones (-0.0172 against -0.0210 LFB, -0.0185 against -0.0212 HFB). Reading (b): the three regions','temporal ones (-0.0172 against -0.0210 LFB, -0.0185 against -0.0212 HFB). Under reading (b) the three regions')
s=s.replace('notes="LFB, 12 models with R2 > 0.05: reach angle','notes="Over the 12 LFB models with R2 > 0.05, reach angle')
s=s.replace('are the top two. "\n    "HFB, 6 models: day (0.1708)','are the top two. "\n    "Over the 6 HFB models day (0.1708)')
s=s.replace('cause both. In volts every level is below 0 dB (-111.5 to -83.6).','cause both. In volts every level is below 0 dB under both readings (between -111.5 and -83.6 dB).')
open('record.py','w').write(s)
EOF
cd  && . $TMPDIR/dev/bin/activate && python $TMPDIR/build/record.py && deactivate && grep -c "^  notes: '\|: '" attempts/000055-peterson-2021-01.yaml; grep -n ": '" attempts/000055-peterson-2021-01.yaml | head
```

```
26
7
5:  id: '000055'
9:date: '2026-10-23'
81:  notes: 'More than half of the reaches last under 2 s and cover under 200 pixels in 12 of 12 subjects
159:  notes: 'Under readings (a), (b) and (c) and both event sets, precentral, postcentral and inferior parietal
183:  notes: 'Three of four parts hold under both event sets. Part 1 fails in S09, whose 76-100 Hz mean is
344:  notes: 'Under both readings reach angle and day have the two largest coefficient magnitudes in both
391:  statement: 'Bimanual_overlap is described as a fraction of the contralateral movement duration, but
```

**Agent calls Bash**

```bash
cd $TMPDIR/build && python - <<'EOF'
s=open('record.py').read()
reps=[("The \"\n    \"angle part fails: the highest","The \"\n    \"angle part fails; the highest"),
("Reading (a) under (b1): \"\n    \"postcentral","Under reading (a) and (b1), \"\n    \"postcentral"),
("Part 4: widths","In part 4 the widths"),
("in both bands: \"\n    \"LFB 1.3385","in both bands, \"\n    \"LFB 1.3385"),
("but it holds seconds: it equals","but it holds seconds; it equals")]
for a,b in reps:
    assert a in s, a
    s=s.replace(a,b)
open('record.py','w').write(s)
EOF
cd  && . $TMPDIR/dev/bin/activate && python $TMPDIR/build/record.py && deactivate && grep -n ": '" attempts/000055-peterson-2021-01.yaml | head; grep -n ": " questions/000055.yaml | grep -v "^[0-9]*: *[a-z_]*: \|^[0-9]*:- [a-z]*: " | head
```

```
26
5:  id: '000055'
9:date: '2026-10-23'
15:    per Hz: (b1) the PSD averaged over good electrodes, a segment dropped when the mean over
20:    the whole 10 s is above 0 dB; a third reading is run in the first notebook, (b3): as (b1), and
36:    differ widely: under (b1) the band-mean and event-mean reading of Table 1 matches 8 of 24
```

**Agent**

Every remaining quoted scalar is quoted only for its id or date. Running the check and the handover:

**Agent calls Bash**

```bash
python tools/entry.py check entries/000055-peterson-2021 2>&1 | tail -3 && python tools/entry.py handover entries/000055-peterson-2021 2>&1 | tail -5; ls executed/000055-peterson-2021/handover; python - <<'EOF'
import nbformat
nb=nbformat.read('executed/000055-peterson-2021/handover/reproduce_peterson_2021.ipynb',4)
print(sum('**Result' in c.source for c in nb.cells if c.cell_type=='markdown'), any('## Summary' in c.source for c in nb.cells))
EOF
date -u
```

```
0 error(s)
wrote executed/000055-peterson-2021/handover
10.1523-eneuro.0007-21.2021.yaml
ajile.py
reproduce_peterson_2021.ipynb
reproduce_peterson_2021_regression.ipynb
0 False
Fri Oct 23 18:58:52 UTC 2026
```

**Agent**

Handover built with the conclusions and summaries removed. Running the quote checker on the claims file (I added the two link claims) and reviewing what changed in the repository:

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000055/10.1523-eneuro.0007-21.2021.yaml paper/10.1523-eneuro.0007-21.2021.txt 2>&1 | tail -5; git status --short; git diff --stat
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls -la entries/000055-peterson-2021/; rm -rf entries/000055-peterson-2021/__pycache__; ls -la scripts .idea 2>/dev/null | head; date -u
```

```
total 176
drwxr-xr-x  4 runner runner  4096 Oct 23 18:56 .
drwxr-xr-x 75 runner runner  4096 Oct 23 15:55 ..
drwxr-xr-x  3 runner runner  4096 Oct 23 16:01 .claude
-rw-r--r--  1 runner runner  3445 Oct 23 18:56 README.md
drwxr-xr-x  2 runner runner  4096 Oct 23 17:18 __pycache__
-rw-r--r--  1 runner runner 31580 Oct 23 17:18 ajile.py
-rw-r--r--  1 runner runner  1279 Oct 23 16:30 entry.yaml
-rw-r--r--  1 runner runner 83229 Oct 23 18:11 reproduce_peterson_2021.ipynb
-rw-r--r--  1 runner runner 26592 Oct 23 18:11 reproduce_peterson_2021_regression.ipynb
-rw-r--r--  1 runner runner    84 Oct 23 16:30 requirements.in
-rw-r--r--  1 runner runner  2214 Oct 23 16:30 requirements.lock.txt
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 23 15:44 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 23 15:44 scripts
Fri Oct 23 18:59:01 UTC 2026
```

**Agent calls Bash**

```bash
find entries/000055-peterson-2021/.claude | head; ls entries/000055-peterson-2021/
```

```
entries/000055-peterson-2021/.claude
entries/000055-peterson-2021/.claude/.cc-writes
README.md
ajile.py
entry.yaml
reproduce_peterson_2021.ipynb
reproduce_peterson_2021_regression.ipynb
requirements.in
requirements.lock.txt
```

**Agent**

I've done steps 1 to 6 of the Author section for DANDI:000055 (pinned at 0.220127.0436) and built the handover. The final `entry.py all` passed: notebook 1 took 16.6 min and the regression notebook 27.3 min, which is close to the 30-minute CI limit. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| subject-days, figshare-event-link, figshare-roi-link (the last two are link claims I added) | reproduced |
| cohort | partially reproduced: 7 subjects have depth electrodes against the paper's 5; sex and age are not in the files |
| fig2-event-counts | reproduced: once the Figshare false positives are dropped, the counts are exactly 151 / 947 / 639.5 |
| fig2-features-differ-across-subjects | reproduced |
| fig2-reach-shape | partially reproduced: the angle peaks sit at about ±55 to 75°, not within 15° of ±90° |
| fig2-bimanual-skew | blocked, methods_underspecified: the two rejection readings (b1, b3) give different outcomes |
| extfig2-1c-contralateral-larger | reproduced |
| extfig2-2-feature-correlations | reproduced (6 of 6) |
| fig2-days-and-waking | partially reproduced: S04's busiest day holds 0.43 of its events, not more than half |
| fig3 (three claims) | reproduced |
| fig4-precentral-subject-variability | partially reproduced: S09 has no HFB increase |
| fig5-band-power-differs-across-subjects | reproduced |
| table1-subject-band-power-ci | partially reproduced (21 to 22 of 24) |
| fig5-recording-day-effects | partially reproduced (23 of 24 agree; S10 HFB differs) |
| extfig5-1-baseline-reduces-day-variability | reproduced |
| discussion-day-changes-small | blocked, methods_underspecified: b1 gives not reproduced, b3 gives reproduced |
| fig6-r2, fig6b, fig6c, fig6d (two claims) | reproduced, from only 18 models with R² > 0.05 |
| extfig6-2-angle-most-retained | not reproduced: bimanual ratio is retained most often, not reach angle |

## 2. The dataset and my question

- **False positives are not marked.** The files hold all 8088 events, including the 1157 that the paper's Figshare files flag as false positives. I linked the flags to the events by timestamp (100% match, all features agree).
- **Wrong ECoG clock in three files.** In sub-01 day 7, sub-04 day 3 and sub-06 day 3 the ECoG actually starts at the session start, but its stored starting time is 0. On the stored clock 237 events fall after the ECoG ends. Shifting the ECoG by the session start makes the movement response appear, so I used the shifted clock.
- **Metadata errors:**
  - the session start offset of −05:00 is wrong (sleep labels only fall at night on the UTC clock);
  - the pose is labelled meters but holds pixels;
  - Bimanual_overlap is described as a fraction but holds seconds;
  - electrode positions differ between days for S03 and S12;
  - the stored `low_freq_R2` / `high_freq_R2` columns have no method description. My regression R² correlates with them at 0.74 and 0.71.
- **Zeroed ECoG.** Some segments around events are zeroed and not marked. 42 events kept by the whole-segment rejection have zeroed precentral ECoG in the analysis window.
- **Region projection.** I used the paper's Figshare projection matrices instead of re-projecting from the AAL atlas, which I could not fetch; a link claim checks them against the electrode positions.
- **One question** is in `questions/000055.yaml`: how the paper's PSD rejection ("power <0 dB", Methods) is computed. I ran three readings:
  - b1: Welch PSD averaged over good electrodes;
  - b2: per electrode, which leaves no events in three subjects;
  - b3: b1 plus Morlet power below 0 dB in any time bin of the analysis window.

## 3. Where the protocol was unclear, and what I did

1. **Adding a reading after seeing the data.** I added b3 only after the first run exposed the zeroed segments. Readings are meant to be fixed before analysis, so I recorded this openly in the question and the notebook, and blocked the two claims where b1 and b3 disagree.
2. **No event set in some criteria.** Some criteria (bimanual-skew, reach-shape) don't say which events to use. I applied the reader's several-readings rule, which led to the bimanual-skew block.
3. **Outside data standing in for a method step.** The protocol doesn't cover using the paper's own intermediate output in place of a step (the projection matrices). I added a link claim marked `data: with_inputs`. Also, claims that drop the Figshare false positives still say `data: dataset`, and authors can't change that field; I noted this.
4. **No way to share heavy results between notebooks.** Each notebook has to re-stream about 170 GB of ECoG. The regression's variants (80/20 split, median band power, the b3 events) didn't fit in 30 minutes, so I didn't run them and recorded that as a deviation.
5. **`measured` must be numbers only.** For cohort, two expected values can't be measured, so I left `measured` out and put the values in the notes.
6. **Re-running for conclusions.** It isn't clear whether adding markdown conclusions requires a full re-run (45 min here). I re-ran so the executed copy contains them.
7. **Ties.** In fig4 part 4 under b3, S04 ties for third smallest. The paper gives no tie rule, so I counted ties as included, recorded it as a deviation, and showed the strict-order result. The outcome is partial either way.

## 4. Runtime and failures

The work ran from 15:45 to 19:00 UTC, with three full runs of the entry. No run failed. The two notebooks and the entry files are in `entries/000055-peterson-2021/`, the record is `attempts/000055-peterson-2021-01.yaml`, and the verifier package is in `executed/000055-peterson-2021/handover/`.

The repo root has untracked files I didn't create (`.bashrc`, `.gitconfig`, `.mcp.json`, `scripts`, `.idea`, and others), plus an empty `.claude/.cc-writes` folder inside the entry. I left them alone; make sure they don't get committed with the entry.

## End of run

117 turns, 191 minutes, result: success.
