# 000055 · author · run 42333071861

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries | tail -30; ls claims/000055 paper; wc -l docs/protocol.md README.md docs/design.md
```

```
Sat Nov  7 03:17:55 UTC 2026
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
schemas
[... 48 more lines not kept]
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
[... 596 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md docs/design.md | head -420; cat docs/archives.md | sed -n '1,200p'
```

```
<persisted-output>
Output too large (32.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/3c342b6a-94ef-423e-8f61-7a61074e612d/tool-results/bic6jxu24.txt

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

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/3c342b6a-94ef-423e-8f61-7a61074e612d/tool-results/bic6jxu24.txt"
}
```

```
1	# Encore Science: the registry
2	
3	Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).
4	
5	Agents, and people, try to reproduce the key findings of papers from the open
6	data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
7	here: the notebooks when it works, and the reason when it does not.
8	
9	- **For the archive:** evidence of whether each dandiset is complete and
10	  accurate enough to support the findings of its paper.
11	- **For analysts:** working notebooks to build new analyses on.
12	
13	Status: pilot. All eight pilot targets have been attempted and checked by an
14	independent agent.
15	
16	**Dashboard:** <https://encorescience.org/>
17	
18	## Reading the outcomes
19	
20	An outcome says what one attempt could recover from the data in a dandiset,
[... 591 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000055/*.yaml; ls entries/001453-fouke-2025 claims/001453; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in
```

```
<persisted-output>
Output too large (46KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/3c342b6a-94ef-423e-8f61-7a61074e612d/tool-results/bx69xtlg2.txt

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

**Agent calls Bash**

```bash
cat attempts/001453-fouke-2025-01.yaml
```

```
<persisted-output>
Output too large (34.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/3c342b6a-94ef-423e-8f61-7a61074e612d/tool-results/b4gtx1tlm.txt

Preview (first 2KB):
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
[... 28 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/3c342b6a-94ef-423e-8f61-7a61074e612d/tool-results/bx69xtlg2.txt"
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
[... 669 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,400p /home/runner/.claude/projects/-home-runner-work-encore-encore/3c342b6a-94ef-423e-8f61-7a61074e612d/tool-results/b4gtx1tlm.txt | cut -c1-200 | head -150; grep -n "^[a-z]" attempts/001453-fouke-2025-01.yaml
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
[... 141 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 230,330p attempts/001453-fouke-2025-01.yaml | cut -c1-220; ls schemas; ls tools
```

```
- claim: fig3cd-zf-turn-more
  outcome: blocked
  blocked_by: data_missing
  notes: The head-fixed tail tracking is not in the dandiset, nor in the paper's GitLab repository.
- claim: fig4f-longer-on-duration
  outcome: blocked
  blocked_by: data_missing
  notes: Needs the imaging and the head-fixed tail tracking, neither of which is in the dandiset.
- claim: fig4hi-vspn-lateralized
  outcome: blocked
  blocked_by: data_missing
  notes: Needs the imaging, the tail tracking and the registration to the mapzebrain atlas, none
    of which is in the dandiset.
findings:
- kind: data_missing
  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
    the GitLab repository the paper names for all behavioural and imaging data holds analysis
    notebooks only. Nine of the paper's main findings cannot be tested.
- kind: metadata_insufficient
[... 113 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000055/versions/" | python -c "import json,sys;d=json.load(sys.stdin);[print(v['version'],v['created'],v['asset_count'],v['size']) for v in d['results']]"; curl -s "https://api.dandiarchive.org/api/dandisets/000055/versions/0.220127.0436/assets/?page_size=100" | python -c "import json,sys;d=json.load(sys.stdin);print(d['count']);[print(a['path'],a['size'],a['asset_id']) for a in d['results']]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
python -c "import pynwb, h5py, remfile, numpy, scipy; print(pynwb.__version__)" 2>&1; which uv python; python --version
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb, h5py, remfile, numpy, scipy; print(pynwb.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
Python 3.13.18
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q pynwb h5py remfile numpy scipy pandas matplotlib dandi mne scikit-learn statsmodels 2>&1 | tail -3; python -c "import pynwb, mne, sklearn; print(pynwb.__version__, mne.__version__)"
```

```
4.2.0 1.13.2
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import h5py, remfile, requests, time
aid="7b9e2ca1-9097-488a-b4e9-ac407fb31457"  # sub-01 ses-3
r=requests.get(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False)
url=r.headers["Location"]
t=time.time()
f=h5py.File(remfile.File(url),"r")
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name,obj.shape,obj.dtype,obj.chunks,obj.compression, dict((k,(v if not hasattr(v,'shape') or v.size<5 else '...')) for k,v in obj.attrs.items() if k not in('namespace','object_id')))
    else:
        a={k:v for k,v in obj.attrs.items() if k not in ('namespace','object_id')}
        print(name+"/",a)
f.visititems(show)
print(time.time()-t)
EOF
python survey.py 2>&1 | grep -v "^specifications" | head -200
```

```
acquisition/ {}
acquisition/ECGL/ {'comments': 'no comments', 'description': 'Electrooculography for tracking saccades - left', 'neurodata_type': 'TimeSeries'}
acquisition/ECGL/data (43200000,) float32 None None {'conversion': np.float64(nan), 'resolution': np.float64(-1.0), 'unit': 'V'}
acquisition/ECGL/starting_time () float64 None None {'rate': np.float32(500.0), 'unit': 'seconds'}
acquisition/ECGR/ {'comments': 'no comments', 'description': 'Electrooculography for tracking saccades - right', 'neurodata_type': 'TimeSeries'}
acquisition/ECGR/data (43200000,) float32 None None {'conversion': np.float64(nan), 'resolution': np.float64(-1.0), 'unit': 'V'}
acquisition/ECGR/starting_time () float64 None None {'rate': np.float32(500.0), 'unit': 'seconds'}
acquisition/EOGL/ {'comments': 'no comments', 'description': 'Electrooculography for tracking saccades - left', 'neurodata_type': 'TimeSeries'}
acquisition/EOGL/data (43200000,) float32 None None {'conversion': np.float64(nan), 'resolution': np.float64(-1.0), 'unit': 'V'}
acquisition/EOGL/starting_time () float64 None None {'rate': np.float32(500.0), 'unit': 'seconds'}
acquisition/EOGR/ {'comments': 'no comments', 'description': 'Electrooculography for tracking saccades - right', 'neurodata_type': 'TimeSeries'}
acquisition/EOGR/data (43200000,) float32 None None {'conversion': np.float64(nan), 'resolution': np.float64(-1.0), 'unit': 'V'}
acquisition/EOGR/starting_time () float64 None None {'rate': np.float32(500.0), 'unit': 'seconds'}
acquisition/ElectricalSeries/ {'comments': 'no comments', 'description': 'no description', 'neurodata_type': 'ElectricalSeries'}
acquisition/ElectricalSeries/data (43200000, 94) float32 (84375, 1) gzip {'conversion': np.float64(1e-06), 'resolution': np.float64(-1.0), 'unit': 'volts'}
acquisition/ElectricalSeries/electrodes (94,) int64 None None {'description': 'all electrodes', 'neurodata_type': 'DynamicTableRegion', 'table': <HDF5 object reference>}
acquisition/ElectricalSeries/starting_t
[... 113 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cat > t2.py <<'EOF'
import h5py, remfile, requests, time, numpy as np
aid="7b9e2ca1-9097-488a-b4e9-ac407fb31457"
url=requests.get(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False).headers["Location"]
t=time.time()
f=h5py.File(remfile.File(url),"r")
print("open",time.time()-t)
for k in ['session_start_time','session_description','identifier','general/session_id','general/subject/subject_id','general/subject/species','timestamps_reference_time']:
    print(k, f[k][()])
print(list(f['general/subject'].attrs.items()))
print(list(f['general'].keys()))
e=f['general/extracellular_ephys/electrodes']
for c in ['location','group_name','good','x','y','z','filtering','imp']:
    v=e[c][:]; print(c, v[:5], np.unique(v)[:10] if v.dtype==object or v.dtype==bool else (np.nanmin(v),np.nanmax(v)))
print("open+meta",time.time()-t)
r=f['intervals/reaches']
st=r['start_time'][:]; sp=r['stop_time'][:]
print(st[:5], sp[:5], (sp-st).min(), np.median(sp-st))
ev=f['processing/behavior/ReachEvents/timestamps'][:]; print(ev[:5])
lab=f['intervals/epochs/labels'][:]; print(np.unique(lab, return_counts=True))
ep=f['intervals/epochs/start_time'][:]; print(ep[:3], f['intervals/epochs/stop_time'][-3:])
d=f['acquisition/ElectricalSeries/data']
t=time.time(); i=int(st[10]*500); x=d[i-2500:i+2500,:]; print("10s all ch", time.time()-t, x.shape, x[:2,:4])
t=time.time(); w=f['processing/behavior/Position/R_Wrist/data']; j=int(st[10]*30); y=w[j-45:j+45,:]; print("wrist",time.time()-t, y[:3])
EOF
python t2.py
```

```
Sat Nov  7 03:21:03 UTC 2026
/tmp/claude-1001/t2.py:13: RuntimeWarning: All-NaN slice encountered
  v=e[c][:]; print(c, v[:5], np.unique(v)[:10] if v.dtype==object or v.dtype==bool else (np.nanmin(v),np.nanmax(v)))
open 0.5232634544372559
session_start_time b'2000-01-02T19:00:00-05:00'
session_description b'no description'
identifier b'4c571b6c-1028-476f-b0e1-e34aa27b3206'
general/session_id b'3'
general/subject/subject_id b'01'
general/subject/species b'Homo sapiens'
timestamps_reference_time b'2000-01-02T19:00:00-05:00'
[('namespace', 'core'), ('neurodata_type', 'Subject'), ('object_id', '84fbf8d4-7653-404f-92e3-0d48f5626a77')]
['devices', 'extracellular_ephys', 'session_id', 'subject']
location [b'unknown' b'unknown' b'unknown' b'unknown' b'unknown'] [b'unknown']
group_name [b'GRID' b'GRID' b'GRID' b'GRID' b'GRID'] [b'GRID' b'LAT' b'LID' b'LMT' b'LPT' b'LTO']
good [False  True  True  True  True] [False  True]
x [-45.64849509 -47.34715172 -50.29140891 -51.35896118 -51.21981805] (np.float64(-69.92889087665836), np.float64(-13.62310121190364))
y [38.56037242 31.1828614  22.15720826 11.78726768  1.71388884] (np.float64(-96.01996972594984), np.float64(38.74864095990316))
z [36.18796239 41.17679881 45.19188514 48.72650925 53.00098123] (np.float64(-45.102521725855055), np.float64(62.70910171006423))
filtering [b'250 Hz lowpass' b'250 Hz lowpass' b'250 Hz lowpass' b'250 Hz lowpass'
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
nproc; free -g | head -2; df -h $TMPDIR | tail -1; curl -s "https://api.figshare.com/v2/projects/78666/articles" | python -c "import json,sys;d=json.load(sys.stdin);[print(a['id'],a['title'],a.get('doi')) for a in d]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.figshare.com/v2/articles/12114408" | python -c "import json,sys;d=json.load(sys.stdin);print(d['version'],d['description'][:1500]);[print(f['id'],f['name'],f['size'],f['computed_md5']) for f in d['files']]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL https://ndownloader.figshare.com/files/22276662 -o p01.csv; curl -sL https://ndownloader.figshare.com/files/22276665 -o c01.csv; head -c 1500 p01.csv; echo; python -c "
import pandas as pd; d=pd.read_csv('p01.csv'); print(d.shape); print(d.columns[:10].tolist()); print(d.iloc[:3,:8])"; cat c01.csv | head -20
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; . dev/bin/activate; python -c "
import pandas as pd, numpy as np; d=pd.read_csv('p01.csv'); print(d.shape)
print(d.iloc[:4,[0,6,56,60,62,80,84,88]])
cols=['Frontal_Mid_L','Precentral_L','Postcentral_L','Parietal_Inf_L','SupraMarginal_L','Temporal_Sup_L','Temporal_Mid_L','Temporal_Inf_L']
print(d[cols].iloc[0]); w=d[cols].iloc[1:]; print(w.sum(0)); print((w>0).sum(0))
"
```

```
<string>:5: Pandas4Warning: Starting with pandas version 4.0 all arguments of sum will be keyword-only.
(99, 116)
   Precentral_L  Frontal_Mid_L  ...  Temporal_Mid_L  Temporal_Inf_L
0      4.716600        3.89510  ...    9.706500e+00    8.266700e+00
1      0.000319        0.17785  ...    2.077500e-15    3.095700e-21
2      0.003332        0.17148  ...    8.370900e-15    2.615500e-21
3      0.026213        0.15346  ...    9.777600e-14    1.062200e-20

[4 rows x 8 columns]
Frontal_Mid_L      3.8951
Precentral_L       4.7166
Postcentral_L      7.3174
Parietal_Inf_L     1.3433
SupraMarginal_L    3.2530
Temporal_Sup_L     5.4340
Temporal_Mid_L     9.7065
Temporal_Inf_L     8.2667
Name: 0, dtype: float64
Frontal_Mid_L      1.000000
Precentral_L       1.000003
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc -c *.txt; grep -n -i "Materials and Methods\|^Results\|^Discussion\|^References" 10.1523-eneuro.0007-21.2021.txt | head
```

```
<persisted-output>
Output too large (85.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/3c342b6a-94ef-423e-8f61-7a61074e612d/tool-results/bija250vc.txt

Preview (first 2KB):
 74189 10.1016-j.jneumeth.2021.109199.txt
 58884 10.1038-s41597-022-01280-y.txt
153224 10.1523-eneuro.0007-21.2021.txt
286297 total
7:2821 eneuro eNeuro eNeuro Society for Neuroscience PMC8225404 8225404 8225404 34031100 10.1523/ENEURO.0007-21.2021 Behavioral and Neural Variability of Naturalistic Arm Movements Peterson Steven M 1 2 ✉ Singh Satpreet H 3 Wang Nancy X R 4 5 Rao Rajesh P N 3 5 6 Brunton Bingni W 1 2 1 Department of Biology, University of Washington, Seattle, Washington 98195 2 eScience Institute, University of Washington, Seattle, Washington 98195 3 Department of Electrical & Computer Engineering, University of Washington, Seattle, Washington 98195 4 IBM Research, San Jose, California 95120 5 Paul G. Allen School of Computer Science and Engineering, University of Washington, Seattle, Washington 98195 6 Center for Neurotechnology, University of Washington, Seattle, Washington 98195 The authors declare no competing financial interests. Author contributions: N.X.R.W., R.P.N.R., and B.W.B. designed research; S.M.P. and S.H.S. performed research; S.M.P. and S.H.S. contributed unpublished reagents/analytic tools; S.M.P., S.H.S., R.P.N.R., and B.W.B. analyzed data; S.M.P. and B.W.B. wrote the paper. This research was supported by Defense Advanced Research Projects Agency Grant FA8750-18-2-0259, National Science Foundation Grants 1630178 and EEC-1028725, the Sloan Foundation, the Washington Research Foundation, and the Weill Neurohub. * S.M.P. and S.H.S. contributed equally to this work. ✉ Correspondence should be addressed to Steven M. Peterson at [removed: an e-mail address] . ✉ Corresponding author. 19 6 2021 8 3 ENEURO.0007-21.2021 ENEURO.0007-21.2021 25 6 2021 Copyright © 2021 Peterson et al. This is an open-access article distributed under the terms of th
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import textwrap,re
t=open('paper/10.1523-eneuro.0007-21.2021.txt').read()
i=t.find('Materials and Methods'); j=t.find('Results',i+20000) 
print(i,j,len(t))
s=t[i:i+60000]
k=s.find(' Results ')
open('/tmp/claude-1001/methods.txt','w').write(textwrap.fill(s[:max(k,30000)],200))
EOF
wc -c /tmp/claude-1001/methods.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/methods.txt"
}
```

```
1	Materials and Methods Subject information We analyzed opportunistic clinical recordings from 12 subjects (8 males, 4 females) during their clinical epilepsy monitoring. Subjects were (mean ± SD)
2	29.4 ± 7.9 years old at the time of recording. Our study was approved by the University of Washington Institutional Review Board for the protection of human subjects. All subjects provided written
3	informed consent. We selected subjects who had ECoG electrode coverage near primary motor cortex, with either one 8 × 8 or two 4 × 8 electrode grids placed subdurally on the cortical surface.
4	Additional electrodes were implanted on the cortical surface for some subjects, resulting in 87.0 ± 12.9 total surface electrodes per subject (mean ± SD). In addition, five subjects had 23.2 ± 12.1
5	intracortical depth electrodes (mean ± SD). Electrodes were implanted primarily within one hemisphere for each subject (five right hemisphere, seven left hemisphere). Single-subject electrode
6	placement and recording duration information are given in Extended Data Figure 1-1 . Figure 1-1 Single-subject recording days used and electrode information. Surface electrodes refer to grid and strip
7	electrodes placed on the cortical surface, while depth electrodes reach deep cortical and subcortical areas. Download Figure 1-1, EPS file . Data collection Subjects underwent 24 h clinical
8	monitoring, involving semicontinuous ECoG and audio/video recordings over 7.4 ± 2.2 d per subject (mean ± SD). Some breaks occurred throughout monitoring [on average, 8.3 ± 3.2 total breaks per
9	subject, each lasting 1.9 ± 2.4 h (mean ± SD)]. For all subjects, we restricted our analysis to days 3–7 following the electrode implantation surgery, to exclude potentially anomalous neural and
10	behavioral activity immediately following electrode implantation surgery. For several subjects, some days were excluded because of corrupted or missing data files, as noted in Extended Data Fig. 1-1 .
11	During clinical monit
[... 142 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re,textwrap
t=open('paper/10.1038-s41597-022-01280-y.txt').read()
for kw in ['reach','Reach','events','stop_time','false','Bimanual','pixel','time of day','start time','session_start','R2','R 2','good']:
    for m in re.finditer(kw,t):
        pass
for m in re.finditer(r'[^.]*(?:reach|events|false|pixel|R 2|R2|midnight|start time|good electrode|hours)[^.]*\.',t):
    s=m.group(0).strip()
    if len(s)<600: print('-',s)
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cat > bench.py <<'EOF'
import h5py, remfile, requests, time, numpy as np
from concurrent.futures import ProcessPoolExecutor
ids=["7b9e2ca1-9097-488a-b4e9-ac407fb31457","42f73251-88be-4407-a7bf-4ea671bbb448","5122cc42-981c-4fa3-92f4-5f9ccfb8c092","554a74cc-824b-4a02-8b23-63aa51ac2369","c4674f3f-fd0d-471c-a9a4-a0d0eeaed105","87c2f790-8f6c-4e73-a54f-f275af6a2680","5791a9f3-5c0c-484b-b690-b5ce9fea589e","7de9b149-2994-455e-a8c6-5e5893245baf"]
def work(aid):
    url=requests.get(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=False).headers["Location"]
    f=h5py.File(remfile.File(url),"r")
    st=f['intervals/reaches/start_time'][:]
    d=f['acquisition/ElectricalSeries/data']
    t=time.time(); n=0
    for s in st[20:32]:
        i=int(round(s*500)); x=d[i-2500:i+2500,:]; n+=1
    return aid[:4], d.shape[1], len(st), (time.time()-t)/n
t=time.time()
with ProcessPoolExecutor(8) as ex:
    for r in ex.map(work, ids): print(r)
print("total", time.time()-t)
EOF
python bench.py
```

```
Sat Nov  7 03:22:20 UTC 2026
('7b9e', 94, 156, 0.8175474603970846)
('42f7', 86, 51, 0.6363114515940348)
('5122', 96, 198, 0.6223824421564738)
('554a', 84, 35, 5.7816505432128906e-05)
('c467', 106, 56, 0.7076835036277771)
('87c2', 80, 166, 0.579583744208018)
('5791', 64, 93, 0.575713038444519)
('7de9', 92, 197, 0.9215701222419739)
total 11.89192795753479
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL https://github.com/BruntonUWBio/naturalistic_arm_movements_ecog/archive/04c6faf2f219586fa834d10c614ef48a694cec55.tar.gz | tar xz && ls naturalistic_arm_movements_ecog-*/ && wc -l naturalistic_arm_movements_ecog-*/*.py
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/naturalistic_arm_movements_ecog-*/compute_power_gen_figs_python && ls -la && cat config.py 2>/dev/null | head -80; grep -n "def \|tlim\|crop\|decim\|n_cycles\|freqs\|baseline" compute_spectral_power.py | head -60
```

```
total 1188
drwxr-xr-x 5 runner runner   4096 Mar 17  2021 .
drwxr-xr-x 4 runner runner   4096 Mar 17  2021 ..
drwxr-xr-x 2 runner runner   4096 Mar 17  2021 .ipynb_checkpoints
-rw-r--r-- 1 runner runner 293178 Mar 17  2021 Behavioral_features_Fig2.ipynb
-rw-r--r-- 1 runner runner 131272 Mar 17  2021 Plot_banded_power_Fig5.ipynb
-rw-r--r-- 1 runner runner 346936 Mar 17  2021 Projected_spectral_power_Figs3_4.ipynb
-rw-r--r-- 1 runner runner 311124 Mar 17  2021 Regression_results_Fig6.ipynb
drwxr-xr-x 2 runner runner   4096 Mar 17  2021 __pycache__
drwxr-xr-x 3 runner runner   4096 Mar 17  2021 archived_code
-rw-r--r-- 1 runner runner   4133 Mar 17  2021 compute_spectral_power.py
-rw-r--r-- 1 runner runner   3612 Mar 17  2021 config.py
-rw-r--r-- 1 runner runner  14482 Mar 17  2021 feat_plot_utils.py
-rw-r--r-- 1 runner runner   4830 Mar 17  2021 fit_regression_models.py
-rw-r--r-- 1 runner runner  27457 Mar 17  2021 regression_utils.py
-rw-r--r-- 1 runner runner  38091 Mar 17  2021 tfr_utils.py
import numpy as np

root_dir = '.../data_release_scripts/'

[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/naturalistic_arm_movements_ecog-*/compute_power_gen_figs_python && sed -n 1,90p compute_spectral_power.py; grep -n "^def " tfr_utils.py
```

```
import os, mne, sys, pdb, argparse, h5py, glob, natsort
os.environ["OMP_NUM_THREADS"] = "1" #avoid multithreading if have Anaconda numpy
import numpy as np
import pandas as pd
from datetime import datetime as dt
import scipy.io as sio

#Import custom scripts
import config
from tfr_utils import compute_tfr,tfr_subtract_baseline,tfr_boot_sig_mask,str2bool

#Set parameters
def main(ecog_lp,savefolder,averagePower,stat_method): 
    '''
    Use MNE to compute spectrograms from ECoG trials (with false positive trials removed, if desired).
    '''
    
    #Load parameters
    alpha = config.constants_compute_tfr['alpha']
    n_perms = config.constants_compute_tfr['n_perms']
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/naturalistic_arm_movements_ecog-*/compute_power_gen_figs_python && sed -n 25,205p tfr_utils.py; sed -n 286,350p tfr_utils.py
```

```
def compute_tfr(epochsAllMove,epoch_times,freqs = np.arange(6, 123, 3),crop_val=0.5,decim=30):
    #Time-frequency analysis (from https://plot.ly/ipython-notebooks/mne-tutorial/ -> Time-frequency analysis)
    n_cycles = freqs / 4.  # different number of cycle per frequency

    #Compute power for move trials
    print('Computing power...')
    power = tfr_morlet(epochsAllMove, freqs=freqs, n_cycles=n_cycles, use_fft=False,
                       return_itc=False, decim=decim, n_jobs=1,average=False)
    print('Power computation complete!')
    power.crop(epoch_times[0]+crop_val, epoch_times[1]-crop_val) #trim epoch to avoid edge effects
    power.data = 10*np.log10(power.data) #convert to log scale
    power.data[np.isinf(power.data)]=0 #set infinite values to 0
    return power

def tfr_subtract_baseline(power,chan_ind,baseidx,compute_mean=False):
    """
    From MNE format to time x freq x trials with baseline subtraction
    """
    if power.data.ndim==4:
        input_power = np.squeeze(power.data[:,chan_ind,:,:]) #trials x freq x time
[... 227 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/naturalistic_arm_movements_ecog-*/compute_power_gen_figs_python && python - <<'EOF'
import json
for nb in ['Projected_spectral_power_Figs3_4.ipynb','Plot_banded_power_Fig5.ipynb']:
    d=json.load(open(nb))
    print('=====',nb)
    for c in d['cells']:
        if c['cell_type']=='code':
            s=''.join(c['source'])
            print('---'); print(s[:1800])
EOF
```

```
===== Projected_spectral_power_Figs3_4.ipynb
---
%matplotlib notebook
import os,mne,glob,natsort
os.environ["OMP_NUM_THREADS"] = "1" #avoid multithreading if have Anaconda numpy
import numpy as np
import pandas as pd
from tqdm import tqdm_notebook as tqdm #useful for seeing progress
from matplotlib import gridspec
import matplotlib.pyplot as plt
import matplotlib.patches as patches

import config
from tfr_utils import load_project_spectral_power,plot_specs_group,plot_specs_single_region
---
tfr_lp = '.../naturalistic_reaches/tfr/'
roi_proj_loadpath = '.../roi_proj_matlab/'
n_subjs = 12

rem_bad_chans = True #don't use bad channels for ROI projection
[... 155 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000055/versions/0.220127.0436/assets/ccdc3ae1-e98d-4a17-93d8-5b7386689fe0/" | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d.get('wasAttributedTo'),indent=0)[:800]); print(d.get('wasGeneratedBy',[{}])[0].get('description') if d.get('wasGeneratedBy') else None)"; curl -s "https://api.dandiarchive.org/api/dandisets/000055/versions/0.220127.0436/" | python -c "import json,sys;d=json.load(sys.stdin);print(d['name']);print(d['description'][:2000]);print(d.get('relatedResource'));print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
mkdir -p entries/000055-peterson-2021; cat entries/001453-fouke-2025/README.md | head -30; sed -n 1,60p entries/001453-fouke-2025/omr.py; python - <<'EOF'
import json
d=json.load(open('entries/001453-fouke-2025/reproduce_fouke_2025.ipynb'))
for c in d['cells'][:6]:
    print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:1200]); print('----')
EOF
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
[... 162 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/naturalistic_arm_movements_ecog-*/compute_power_gen_figs_python && sed -n 623,652p tfr_utils.py; grep -n "baseline_vals_movement\|metadata_pos_min_time\|def plot_behavior_traces" -r --include=*.py . | head
```

```
def compute_wrist_radial_distance(contra_metadata_sbj,wrist_contra):
    '''
    Create variable for plotting contralateral wrist displacements. 
    '''
    #Compute baseline-subtracted displacement
    wrist_x = contra_metadata_sbj.loc[:,wrist_contra+'_wrist_x']
    wrist_x = [np.asarray(val) for val in wrist_x]
    wrist_y = contra_metadata_sbj.loc[:,wrist_contra+'_wrist_y']
    wrist_y = [np.asarray(val) for val in wrist_y]
    contra_vals = np.sqrt(np.asarray(wrist_x)**2 +np.asarray(wrist_y)**2)

    #Determine baseline in samples
    min_t_val = config.metadata_pos_min_time
    base_times = np.asarray(config.baseline_vals_movement)
    base_times = (base_times-min_t_val)*config.fs_video #baseline frame limits
    base_times_range = np.arange(base_times[0],base_times[1]+1)
    base_times_range = base_times_range.astype('int')

    #Subtract baseline from position data
    contra_vals_basesub = contra_vals.copy()
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/naturalistic_arm_movements_ecog-*/compute_power_gen_figs_python && grep -n "^def " regression_utils.py; sed -n "$(grep -n 'def _forward_selected_new' regression_utils.py | cut -d: -f1),+40p" regression_utils.py; sed -n "$(grep -n 'def train_test_split_day_balance' regression_utils.py | cut -d: -f1),+30p" regression_utils.py
```

```
19:def user_def_f_aves(sbj_id):
51:def load_power_metadata(s,tfr_loadpath):
88:def update_events_dataframe(df_in,log_cols=['run_1'],log_cols1=['reach_r','onset_velocity'],bimanual_thresh=None):
117:def standardize_feats(df_in):
132:def train_test_split_power_inds(n_evs,per_train):
143:def train_test_split_day_balance(day_lst, per_train):
161:def _forward_selected_new(data, response,d_val=False):
200:def num2written(num_in):
218:def written2num(num_in):
236:def single_subj_regression(tfr_lp,max_chan_num,feats2use,n_perms,model_type,add_interactions=False,s=0):
463:def compute_r2_score_colors(r2_dat_plot,del_r2_dat_plot,n_subjs,n_freqs,n_coefs,
534:def compute_reg_coef_colors(coefs_pats_all,n_subjs,n_freqs,n_coefs,plot_sd_coef=False):
569:def compute_ind_subj_r2_colors(reg_r2_test_ave,n_subjs,n_freqs,r2_thresh):
def _forward_selected_new(data, response,d_val=False):
    """Linear model designed by forward selection. 
    Obtained at https://planspace.org/20150423-forward_selection_with_statsmodels/

    Parameters:
    -----------
    data : pandas DataFrame with all possible predictors and response
[... 66 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/000055-peterson-2021/ajile.py",
 "content": "\"\"\"Loading and measures for AJILE12, dandiset 000055, for Peterson et al. (2021), eNeuro.\n\nPeterson, Singh, Wang, Rao & Brunton (2021), \"Behavioral and Neural Variability of Naturalistic\nArm Movements\", eNeuro 8(3), doi:10.1523/ENEURO.0007-21.2021.\n\nEach NWB file holds one subject and one 24 h recording day: preprocessed ECoG at 500 Hz\n(`acquisition/ElectricalSeries`, stored in microvolts with a conversion of 1e-6 to volts), the\nelectrode table (MNI x, y, z, group, `good`, and the paper's regression R2 per electrode), pose\nof nine key points at 30 frames per second (`processing/behavior/Position`, in pixels though the\nfiles say meters), the contralateral wrist movement events (`processing/behavior/ReachEvents`)\nand their ten features (`intervals/reaches`), and coarse behaviour labels (`intervals/epochs`).\nFiles are streamed from the archive at the pinned version with remfile and h5py; nothing is\nwritten to disk.\n\nWhere the parameters come from:\n\n- The spectral method follows the claims file's opening comment (Methods, \"ECoG-event\n  synchronization and segmentation\", and the paper's code at commit 04c6faf of\n  github.com/BruntonUWBio/naturalistic_arm_movements_ecog, config.py and tfr_utils.py):\n  10 s segments centred on each event; Morlet power at 1 to 121 Hz in 5 Hz steps with\n  n_cycles = f/4, decimated by 50 (10 Hz bins); the 0.5 s at each end cropped off (config\n  `pad_val`, `compute_tfr`), giving -4.5 to 4.5 s; 10*log10, with infinite values set to 0\n  (`compute_tfr`); the mean over -1.5 to -1 s subtracted per electrode and frequency\n  (`tfr_subtract_baseline(compute_mean=True)`). The code uses `tfr_morlet(use_fft=False)`;\n  here the same wavelets are convolved by FFT (`use_fft=True`), which gives the same values\n  away from the segment edges, and the edges are cropped. A standard choice that cannot change\n  a result.\n- Band power (Methods, \"Single-event spectral power linear regression\"; Figure 5 legend): 0 to\n  0.5 s, LFB 8-32 Hz (bins 11 to 31 Hz) and HFB 76-100 Hz (bins 76 to 96 Hz); the band mean\n  (Methods, \"averaged\") as the main measure and the code's median over time bins then over\n  frequency bins (Plot_banded_power_Fig5.ipynb) as a variant.\n- Bad segment rejection (Methods, \"ECoG-event synchronization and segmentation\": \"discarding\n  segments with power <0 dB or with abnormally high power at 115-125 Hz (>3 SDs) compared with\n  all segments\"). The paper's preprocessing code is not published, so how the segment's power\n  is summarised is an assumption: Welch power spectral density of each good electrode (1 s\n  Hann windows, half overlap, a standard choice), 10*log10, averaged over 1-200 Hz and over\n  good electrodes for the 0 dB test, and over 115-125 Hz for the 3 SD test, the SD taken over\n  all of a subject's segments.\n- Projection onto the eight regions uses the paper's projection matrices deposited on Figshare\n  (doi:10.6084/m9.figshare.12114408.v1, aal_XX_elecs2ROI.csv), read as the code\n  `load_project_spectral_power` reads them: the first row is the electrode density, the rows\n  whose mean is not zero are the electrodes in order, bad electrodes get weight 0 and each\n  region's weights are renormalised to sum to 1 (`rem_bad_chans=True` in the Figure 3 to 5\n  notebooks). The bad electrodes are those of the subject's first file, as the code takes the\n  bad list of the first file.\n- The wrist traces of Extended Data Figure 2-1 use the code's window (config\n  `metadata_pos_min_time = -1.5`, `baseline_vals_movement = [-1.5, -1]`) and a 1.5 s end,\n  as the claims file says.\n- Time of day: the files start at midnight local time (data descriptor, Methods: \"each file\n  contained data from one entire 24-hour recording day that started and ended at midnight\"),\n  so the hour of an event is its start time in the file divided by 3600.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport os\nfrom concurrent.futures import ProcessPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\n\nDANDISET_ID = \"000055\"\nDANDISET_VERSION = \"0.220127.0436\"\nAPI = \"https://api.dandiarchive.org/api\"\n\nFIGSHARE_ROI = \"https://api.figshare.com/v2/articles/12114408/versions/1\"\nROI_COLUMNS = [\"Frontal_Mid_L\", \"Precentral_L\", \"Postcentral_L\", \"Parietal_Inf_L\",\n               \"SupraMarginal_L\", \"Temporal_Sup_L\", \"Temporal_Mid_L\", \"Temporal_Inf_L\"]\nROI_NAMES = [\"middle frontal\", \"precentral\", \"postcentral\", \"inferior parietal\",\n             \"supramarginal\", \"superior temporal\", \"middle temporal\", \"inferior temporal\"]\n\nFS = 500.0\nSEG_HALF_S = 5.0                 # 10 s segments centred on the event\nPAD_S = 0.5                      # code: pad_val, cropped off each end\nFREQS = np.arange(1, 124, 5)     # code: np.arange(1, 124, 5) = 1, 6, ..., 121 Hz\nDECIM = 50                       # code: decim\nTIMES = np.round(np.arange(-SEG_HALF_S + PAD_S, SEG_HALF_S - PAD_S + 1e-9, DECIM / FS), 2)\nBASELINE = (-1.5, -1.0)          # Methods and code\nT_AVE = (0.0, 0.5)               # Methods: first 0.5 s after onset\nLFB = (8, 32)\nHFB = (76, 100)\nPOSE_HZ = 30.0\nPOSE_WIN = (-1.5, 1.5)           # code: metadata_pos_min_time; end of plotting axis\n\n\ndef asset_url(asset_id: str) -> str:\n    r = requests.get(f\"{API}/assets/{asset_id}/download/\", allow_redirects=False, timeout=60)\n    return r.headers[\"Location\"]\n\n\ndef list_assets() -> pd.DataFrame:\n    url = f\"{API}/dandisets/{DANDISET_ID}/versions/{DANDISET_VERSION}/assets/?page_size=200\"\n    rows = []\n    while url:\n        d = requests.get(url, timeout=60).json()\n        for a in d[\"results\"]:\n            p = a[\"path\"]\n            sub = p.split(\"/\")[0].split(\"-\")[1]\n            day = int(p.split(\"_ses-\")[1].split(\"_\")[0])\n            rows.append({\"path\": p, \"subject\": sub, \"day\": day, \"asset_id\": a[\"asset_id\"],\n                         \"size_gb\": a[\"size\"] / 1e9})\n        url = d[\"next\"]\n    return pd.DataFrame(rows).sort_values([\"subject\", \"day\"]).reset_index(drop=True)\n\n\ndef _open(asset_id):\n    return h5py.File(remfile.File(asset_url(asset_id)), \"r\")\n\n\ndef _s(v):\n    return v.decode() if isinstance(v, bytes) else v\n\n\ndef read_session(asset_id: str) -> dict:\n    \"\"\"Metadata, electrodes, events with their features, and wrist traces of one file.\"\"\"\n    f = _open(asset_id)\n    out = {\"asset_id\": asset_id,\n           \"subject_id\": _s(f[\"general/subject/subject_id\"][()]),\n           \"species\": _s(f[\"general/subject/species\"][()]),\n           \"session_id\": _s(f[\"general/session_id\"][()]),\n           \"session_start_time\": _s(f[\"session_start_time\"][()])}\n    subj_keys = list(f[\"general/subject\"].keys())\n    out[\"subject_fields\"] = subj_keys\n    e = f[\"general/extracellular_ephys/electrodes\"]\n    el = pd.DataFrame({c: e[c][:] for c in [\"x\", \"y\", \"z\", \"group_name\", \"good\", \"low_freq_R2\",\n                                             \"high_freq_R2\", \"standard_deviation\", \"kurtosis\"]})\n    el[\"group_name\"] = el[\"group_name\"].map(_s)\n    el[\"location\"] = [_s(v) for v in e[\"location\"][:]]\n    out[\"group_desc\"] = {g: _s(f[f\"general/extracellular_ephys/{g}\"].attrs[\"description\"])\n                         for g in f[\"general/extracellular_ephys\"].keys()\n                         if g != \"electrodes\"}\n    out[\"electrodes\"] = el\n    es = f[\"acquisition/ElectricalSeries\"]\n    out[\"ecog_shape\"] = es[\"data\"].shape\n    out[\"ecog_rate\"] = float(es[\"starting_time\"].attrs[\"rate\"])\n    out[\"ecog_start\"] = float(es[\"starting_time\"][()])\n    out[\"ecog_unit\"] = _s(es[\"data\"].attrs[\"unit\"])\n    out[\"ecog_conversion\"] = float(es[\"data\"].attrs[\"conversion\"])\n    out[\"ecog_electrodes\"] = es[\"electrodes\"][:]\n    r = f[\"intervals/reaches\"]\n    ev = pd.DataFrame({c: r[c][:] for c in r.attrs[\"colnames\"]})\n    ev.columns = [_s(c) for c in ev.columns]\n    out[\"reach_columns\"] = list(ev.columns)\n    ev[\"duration\"] = ev[\"stop_time\"] - ev[\"start_time\"]\n    out[\"events\"] = ev\n    re_ = f[\"processing/behavior/ReachEvents\"]\n    out[\"reach_event_desc\"] = _s(re_.attrs[\"description\"])\n    out[\"reach_event_times\"] = re_[\"timestamps\"][:]\n    lab = [_s(v) for v in f[\"intervals/epochs/labels\"][:]]\n    out[\"epochs\"] = pd.DataFrame({\"start\": f[\"intervals/epochs/start_time\"][:],\n                                  \"stop\": f[\"intervals/epochs/stop_time\"][:], \"label\": lab})\n    pos = f[\"processing/behavior/Position\"]\n    out[\"pose_names\"] = list(pos.keys())\n    out[\"pose_shape\"] = pos[\"R_Wrist/data\"].shape\n    out[\"pose_rate\"] = float(pos[\"R_Wrist/starting_time\"].attrs[\"rate\"])\n    out[\"pose_start\"] = float(pos[\"R_Wrist/starting_time\"][()])\n    out[\"pose_unit\"] = _s(pos[\"R_Wrist/data\"].attrs[\"unit\"])\n    # Wrist traces around each event, both wrists, -1.5 to 1.5 s at 30 frames per second.\n    n = int(round((POSE_WIN[1] - POSE_WIN[0]) * POSE_HZ)) + 1\n    tr = {}\n    for w in [\"L_Wrist\", \"R_Wrist\"]:\n        d = pos[f\"{w}/data\"]\n        arr = np.full((len(ev), n, 2), np.nan)\n        for k, t0 in enumerate(ev[\"start_time\"].values):\n            i0 = int(round((t0 - out[\"pose_start\"] + POSE_WIN[0]) * out[\"pose_rate\"]))\n            if i0 >= 0 and i0 + n <= d.shape[0]:\n                arr[k] = d[i0:i0 + n, :]\n        tr[w] = arr\n    out[\"wrist\"] = tr\n    f.close()\n    return out\n\n\ndef load_sessions(assets: pd.DataFrame, workers: int = 8) -> list[dict]:\n    with ProcessPoolExecutor(workers) as ex:\n        res = list(ex.map(read_session, assets[\"asset_id\"]))\n    for r, (_, a) in zip(res, assets.iterrows()):\n        r[\"subject\"], r[\"day\"], r[\"path\"] = a[\"subject\"], a[\"day\"], a[\"path\"]\n    return res\n\n\ndef fold_angle(a):\n    \"\"\"Reach angle folded to -90 (down) to 90 (up) degrees, if not already.\"\"\"\n    a = np.asarray(a, float) % 360\n    out = np.where(a > 270, a - 360, a)\n    out = np.where((a >= 90) & (a <= 270), 180 - a, out)\n    return out\n\n\n# ---------------------------------------------------------------- regions of interest\n\ndef roi_files() -> dict:\n    d = requests.get(FIGSHARE_ROI, timeout=60).json()\n    return {f[\"name\"]: (f[\"download_url\"], f[\"computed_md5\"]) for f in d[\"files\"]}\n\n\ndef read_roi_matrix(subject: str, files: dict) -> pd.DataFrame:\n    url, _ = files[f\"aal_{subject}_elecs2ROI.csv\"]\n    return pd.read_csv(url)\n\n\ndef roi_weights(df: pd.DataFrame, good: np.ndarray) -> np.ndarray:\n    \"\"\"Electrodes x 8 weights as load_project_spectral_power(rem_bad_chans=True) builds them.\"\"\"\n    rows = np.nonzero(df.transpose().mean().values != 0)[0][1:]\n    w = df.iloc[rows][ROI_COLUMNS].to_numpy(float)\n    if len(w) != len(good):\n        raise ValueError(f\"{len(w)} projection rows for {len(good)} electrodes\")\n    w[~good] = 0\n    return w / w.sum(0, keepdims=True)\n\n\n# ---------------------------------------------------------------- spectral power\n\ndef _band_idx(band):\n    return np.nonzero((FREQS >= band[0]) & (FREQS <= band[1]))[0]\n\n\ndef _tidx(lo, hi):\n    return np.nonzero((TIMES >= lo - 1e-9) & (TIMES <= hi + 1e-9))[0]\n\n\ndef segment_power(x: np.ndarray) -> np.ndarray:\n    \"\"\"x: electrodes x samples (10 s, microvolts) -> electrodes x freqs x times, dB, cropped.\"\"\"\n    from mne.time_frequency import tfr_array_morlet\n    p = tfr_array_morlet(x[None], sfreq=FS, freqs=FREQS, n_cycles=FREQS / 4.0, zero_mean=True,\n                         use_fft=True, decim=DECIM, output=\"power\", n_jobs=1, verbose=False)[0]\n    t_all = np.arange(p.shape[-1]) * DECIM / FS - SEG_HALF_S\n    keep = np.nonzero((t_all >= TIMES[0] - 1e-6) & (t_all <= TIMES[-1] + 1e-6))[0]\n    p = p[..., keep]\n    with np.errstate(divide=\"ignore\"):\n        p = 10 * np.log10(p)\n    p[np.isinf(p)] = 0\n    return p\n\n\ndef segment_quality(x: np.ndarray, good: np.ndarray) -> tuple[float, float]:\n    \"\"\"Mean Welch log power (dB) of a segment over 1-200 Hz and over 115-125 Hz, good electrodes.\"\"\"\n    from scipy.signal import welch\n    f, pxx = welch(x[good], fs=FS, nperseg=int(FS), axis=-1)\n    with np.errstate(divide=\"ignore\"):\n        db = 10 * np.log10(pxx)\n    db[np.isinf(db)] = -300.0\n    a = db[:, (f >= 1) & (f <= 200)].mean()\n    b = db[:, (f >= 115) & (f <= 125)].mean()\n    return float(a), float(b)\n\n\ndef band_values(p: np.ndarray) -> dict:\n    \"\"\"p: ... x freqs x times (dB). Band power over 0-0.5 s: mean (Methods) and median (code).\"\"\"\n    ti = _tidx(*T_AVE)\n    out = {}\n    for name, band in [(\"lfb\", LFB), (\"hfb\", HFB)]:\n        fi = _band_idx(band)\n        sub = p[..., fi, :][..., ti]\n        out[f\"{name}_mean\"] = sub.mean(axis=(-1, -2))\n        out[f\"{name}_median\"] = np.median(np.median(sub, axis=-1), axis=-1)\n    return out\n\n\ndef ecog_session(args) -> dict:\n    \"\"\"Read each event's 10 s segment of one file and reduce it.\n\n    Returns per event: segment quality, region spectrograms (8 x freqs x times, baseline\n    subtracted), region and electrode band power with and without baseline subtraction.\n    `shift_s` moves every segment by that many seconds (for the clock check).\n    \"\"\"\n    asset_id, starts, weights, good = args[:4]\n    max_events = args[4] if len(args) > 4 else None\n    f = _open(asset_id)\n    d = f[\"acquisition/ElectricalSeries/data\"]\n    t0 = float(f[\"acquisition/ElectricalSeries/starting_time\"][()])\n    n_total = d.shape[0]\n    half = int(SEG_HALF_S * FS)\n    bi = _tidx(*BASELINE)\n    res = {k: [] for k in [\"ok\", \"q_all\", \"q_hf\", \"roi_spec\", \"roi_band\", \"roi_band_raw\",\n                           \"el_band\", \"el_band_raw\"]}\n    for k, s in enumerate(starts):\n        if max_events is not None and k >= max_events:\n            break\n        c = int(round((s - t0) * FS))\n        if c - half < 0 or c + half > n_total:\n            res[\"ok\"].append(False)\n            for key in [\"q_all\", \"q_hf\"]:\n                res[key].append(np.nan)\n            for key in [\"roi_spec\", \"roi_band\", \"roi_band_raw\", \"el_band\", \"el_band_raw\"]:\n                res[key].append(None)\n            continue\n        x = d[c - half:c + half, :].T.astype(np.float64)\n        qa, qh = segment_quality(x, good)\n        p = segment_power(x)                                  # elec x f x t, dB\n        raw_roi = np.einsum(\"er,eft->rft\", weights, p)\n        pb = p - p[..., bi].mean(-1, keepdims=True)           # baseline subtracted per electrode\n        roi = np.einsum(\"er,eft->rft\", weights, pb)\n        res[\"ok\"].append(True)\n        res[\"q_all\"].append(qa)\n        res[\"q_hf\"].append(qh)\n        res[\"roi_spec\"].append(roi.astype(np.float32))\n        res[\"roi_band\"].append(band_values(roi))\n        res[\"roi_band_raw\"].append(band_values(raw_roi))\n        res[\"el_band\"].append(band_values(pb))\n        res[\"el_band_raw\"].append(band_values(p))\n    f.close()\n    return res\n\n\ndef load_ecog(jobs: list, workers: int = 8) -> list[dict]:\n    os.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\n    with ProcessPoolExecutor(workers) as ex:\n        return list(ex.map(ecog_session, jobs))\n\n\n# ---------------------------------------------------------------- group statistics\n\ndef boot_sig_mask(curr_power: np.ndarray, baseidx: np.ndarray, rng: np.random.Generator,\n                  n_perms: int = 2000, alpha: float = 0.05, use_median: bool = False) -> np.ndarray:\n    \"\"\"tfr_boot_sig_mask of the paper's code: curr_power is freq x time x subjects.\n\n    The baseline time bins are shuffled within frequency and subject, the median over subjects\n    is taken, ceil(n_perms / n_baseline) times; two-sided percentile p; Benjamini-Hochberg over\n    all frequency and time bins at alpha; non-significant values set to 0. The average over\n    subjects is the mean (plot_specs_group is called with useMedian=False), while the bootstrap\n    takes the median, as in the code.\n    \"\"\"\n    from scipy.stats import percentileofscore\n    from statsmodels.stats.multitest import multipletests\n    ave = np.median(curr_power, axis=2) if use_median else np.mean(curr_power, axis=2)\n    n_iter = int(np.ceil(n_perms / len(baseidx)))\n    nf = curr_power.shape[0]\n    boot = np.zeros((nf, len(baseidx), n_iter))\n    base = curr_power[:, baseidx, :]\n    for it in range(n_iter):\n        tmp = base.copy()\n        for j in range(nf):\n            for k in range(tmp.shape[2]):\n                tmp[j, :, k] = tmp[j, rng.permutation(len(baseidx)), k]\n        boot[:, :, it] = np.median(tmp, 2)\n    boot = boot.reshape(nf, -1).T\n    p = np.zeros(ave.shape)\n    for j in range(nf):\n        for k in range(ave.shape[1]):\n            q = percentileofscore(boot[:, j], ave[j, k]) / 100\n            p[j, k] = 2 * (1 - q) if q > 0.5 else 2 * q\n    pc = multipletests(p.ravel(), alpha=alpha, method=\"fdr_bh\")[1].reshape(ave.shape)\n    out = ave.copy()\n    out[pc >= alpha] = 0\n    return out\n"
}
```

```
File created successfully at: entries/000055-peterson-2021/ajile.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cat > run_beh.py <<'EOF'
import sys, time, pickle
sys.path.insert(0,'entries/000055-peterson-2021')
import ajile
t=time.time()
A=ajile.list_assets()
S=ajile.load_sessions(A, workers=8)
print(time.time()-t)
pickle.dump((A,S),open('beh.pkl','wb'))
EOF
python run_beh.py
```

```
Sat Nov  7 03:25:14 UTC 2026
28.06690549850464
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle, numpy as np, pandas as pd
A,S=pickle.load(open('beh.pkl','rb'))
rows=[]
for s in S:
    el=s['electrodes']; ev=s['events']
    rows.append(dict(sub=s['subject'],day=s['day'],sid=s['subject_id'],sess=s['session_id'],start=s['session_start_time'],nel=len(el),ngood=int(el.good.sum()),nev=len(ev),wrist=s['reach_event_desc'],
      ecog=s['ecog_shape'],pose=s['pose_shape'][0], groups=','.join(sorted(el.group_name.unique())), r2max=np.nanmax(el.low_freq_R2.values), r2hmax=np.nanmax(el.high_freq_R2.values), xmean=el.x.mean()))
D=pd.DataFrame(rows); pd.set_option('display.width',250); print(D.to_string())
print(D.groupby('sub').nev.sum().to_string(), D.nev.sum())
print(S[0]['group_desc']); print(S[0]['subject_fields'], S[0]['reach_columns'])
for s in S:
    if s['day']==min(x['day'] for x in S if x['subject']==s['subject']):
        print(s['subject'], s['group_desc'])
EOF
```

```
sub  day sid sess                             start  nel  ngood  nev    wrist             ecog     pose                                        groups     r2max    r2hmax      xmean
0   01    3  01    3         2000-01-02T19:00:00-05:00   94     85  156  r_wrist   (43200000, 94)  2592000                      GRID,LAT,LID,LMT,LPT,LTO  0.149291  0.055118 -53.675056
1   01    4  01    4         2000-01-03T19:00:00-05:00   94     91  196  r_wrist   (43200000, 94)  2592000                      GRID,LAT,LID,LMT,LPT,LTO  0.149291  0.055118 -53.675056
2   01    5  01    5         2000-01-04T19:00:00-05:00   94     91  199  r_wrist   (43200000, 94)  2592000                      GRID,LAT,LID,LMT,LPT,LTO  0.149291  0.055118 -53.675056
3   01    7  01    7  2000-01-07T03:31:22.414000-05:00   94     91  190  r_wrist   (27858793, 94)  2592000                      GRID,LAT,LID,LMT,LPT,LTO  0.149291  0.055118 -53.675056
4   02    3  02    3         2000-01-02T19:00:00-05:00   86     85   51  l_wrist   (43200000, 86)  2592000                              GRID,RDA,RDP,RST  0.016180  0.031845  54.465985
5   02    4  02    4         2000-01-03T19:00:00-05:00   86     85   94  l_wrist   (43200000, 86)  2592000                              GRID,RDA,RDP,RST  0.016180  0.031845  54.465985
6   02    5  02    5         2000-01-04T19:00:00-05:00   86     81   82  l_wrist   (43200000, 86)  2592000                              GRID,RDA,RDP,RST  0.016180  0.031845  54.465985
7   02    6  02    6         2000-01-05T19:00:00-05:00   86     80   78  l_wrist   (43200000, 86)  2592000                              GRID,RDA,RDP,RST  0.016180  0.031845  54.465985
8   03    3  03    3         2000-01-02T19:00:00-05:00   96     79  198  r_wrist   (43200000, 96)  2592000                          GRID,LAD,LAT,LMT,LPD  0.146372  0.139716 -49.264743
9   03    4  03    4         2000-01-03T19:00:00-05:00   96     71  193  r_wrist   (43200000, 96)  2592000                          GRID,LAD,LAT,LMT,LPD  0.146372 
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle, numpy as np, pandas as pd
A,S=pickle.load(open('beh.pkl','rb'))
for s in S:
    ev=s['events']
    print(s['subject'],s['day'],s['session_start_time'][11:19],'ecog t0',s['ecog_start'],'dur h',round(s['ecog_shape'][0]/500/3600,2),'pose t0',s['pose_start'],'ev range h',round(ev.start_time.min()/3600,2),round(ev.start_time.max()/3600,2), 'epochs end h', round(s['epochs'].stop.max()/3600,2), 'evt==start',np.allclose(s['reach_event_times'],ev.start_time,atol=0.01))
EOF
```

```
01 3 19:00:00 ecog t0 0.0 dur h 24.0 pose t0 0.0 ev range h 0.5 21.04 epochs end h 24.0 evt==start True
01 4 19:00:00 ecog t0 0.0 dur h 24.0 pose t0 0.0 ev range h 0.43 23.55 epochs end h 24.0 evt==start True
01 5 19:00:00 ecog t0 0.0 dur h 24.0 pose t0 0.0 ev range h 0.55 22.28 epochs end h 24.0 evt==start True
01 7 03:31:22 ecog t0 0.0 dur h 15.48 pose t0 0.0 ev range h 8.98 23.83 epochs end h 24.0 evt==start False
02 3 19:00:00 ecog t0 0.0 dur h 24.0 pose t0 0.0 ev range h 6.01 22.0 epochs end h 24.0 evt==start True
02 4 19:00:00 ecog t0 0.0 dur h 24.0 pose t0 0.0 ev range h 0.1 23.75 epochs end h 24.0 evt==start True
02 5 19:00:00 ecog t0 0.0 dur h 24.0 pose t0 0.0 ev range h 0.5 22.35 epochs end h 24.0 evt==start True
02 6 19:00:00 ecog t0 0.0 dur h 24.0 pose t0 0.0 ev range h 1.39 20.04 epochs end h 24.0 evt==start True
03 3 19:00:00 ecog t0 0.0 dur h 24.0 pose t0 0.0 ev range h 0.1 23.78 epochs end h 24.0 evt==start True
03 4 19:00:00 ecog t0 0.0 dur h 24.0 pose t0 0.0 ev range h 0.67 24.0 epochs end h 24.0 evt==start True
03 5 19:00:00 ecog t0 0.0 dur h 24.0 pose t0 0.0 ev range h 0.04 8.1 epochs end h 24.0 evt==start True
03 6 19:00:00 ecog t0 0.0 dur h 24.0 pose t0 0.0 ev range h 8.54 22.62 epochs end h 24.0 evt==start True
04 3 03:20:48 ecog t0 0.0 dur h 15.65 pose t0 0.0 ev range h 13.7 23.98 epochs end h 24.0 evt==start False
04 4 19:00:00 ecog t0 0.0 dur h 24.0 pose t0 0.0 ev range h 0.07 23.92 epochs end h 24.0 evt==start True
04 5 19:00:00 ecog t0 0.0 dur h 24.0 pose t0 0.0 ev range h 0.24 22.13 epochs end h 24.0 evt==start True
04 6 19:00:00 ecog t0 0.0 dur h 24.0 pose t0 0.0 ev range h 5.34 23.51 epochs end h 24.0 evt==start True
04 7 19:00:00 ecog t0 0.0 dur h 24.0 pose t0 0.0 ev range h 0.45 23.8 epochs end h 24.0 evt==start True
05 3 19:00:00 ecog t0 0.0 dur h 24.0 pose t0 0.0 ev range h 0.07 20.34 epochs end h 24.0 evt==start True
05 4 19:00:00 ecog t0 0.0 dur h 24.0 pose t0 0.0 ev range h 0.25 20.36 epochs end h 24.0 evt==start True
05 7 19:00
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle, numpy as np, pandas as pd
A,S=pickle.load(open('beh.pkl','rb'))
for s in S:
    ev=s['events']; t=s['reach_event_times']
    if not np.allclose(t,ev.start_time,atol=0.01):
        d=t-ev.start_time.values
        print(s['subject'],s['day'],len(t),len(ev),np.round(np.percentile(d,[0,50,100]),3), (np.abs(d)>0.01).sum())
        dur=24*3600-s['ecog_shape'][0]/500
        print('  offset s',dur, 'events beyond ecog if offset 0:',(ev.start_time>s['ecog_shape'][0]/500-5).sum(), 'events before offset', (ev.start_time<dur+5).sum())
EOF
```

```
01 7 190 190 [-30682.415 -30682.415 -30682.413] 190
  offset s 30682.413999999997 events beyond ecog if offset 0: 132 events before offset 0
04 3 35 35 [-30048.323 -30048.323 -30048.321] 35
  offset s 30048.322 events beyond ecog if offset 0: 22 events before offset 0
06 3 166 166 [-29240.567 -29240.567 -29240.565] 166
  offset s 29240.566 events beyond ecog if offset 0: 83 events before offset 0
08 4 197 197 [-8.64e+04  0.00e+00  1.00e-03] 1
  offset s 0.0 events beyond ecog if offset 0: 1 events before offset 0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t_ecog.py <<'EOF'
import sys, time, pickle, numpy as np
sys.path.insert(0,'entries/000055-peterson-2021')
import ajile
A,S=pickle.load(open('beh.pkl','rb'))
files=ajile.roi_files()
for sub in sorted(set(s['subject'] for s in S)):
    df=ajile.read_roi_matrix(sub,files)
    first=[s for s in S if s['subject']==sub][0]
    rows=np.nonzero(df.transpose().mean().values!=0)[0][1:]
    print(sub, df.shape[0]-1, len(rows), len(first['electrodes']), 'good',first['electrodes'].good.sum(), 'density',df.iloc[0][ajile.ROI_COLUMNS].round(1).tolist())
s=[s for s in S if s['subject']=='04' and s['day']==3][0]
df=ajile.read_roi_matrix('04',files); good=s['electrodes'].good.values
W=ajile.roi_weights(df,good)
t=time.time()
rA=ajile.ecog_session((s['asset_id'], s['reach_event_times'], W, good))
print('time',time.time()-t, sum(rA['ok']))
rB=ajile.ecog_session((s['asset_id'], s['events'].start_time.values, W, good))
for name,r in [('ReachEvents',rA),('start_time',rB)]:
    h=[b['hfb_mean'][1] for b,o in zip(r['roi_band'],r['ok']) if o]; l=[b['lfb_mean'][1] for b,o in zip(r['roi_band'],r['ok']) if o]
    print(name, len(h), 'precentral HFB', np.round(np.median(h),3), 'LFB', np.round(np.median(l),3), 'q', np.round(np.nanmedian(r['q_all']),1))
pickle.dump((rA,rB),open('t04.pkl','wb'))
EOF
python t_ecog.py
```

```
01 98 94 94 good 85 density [3.9, 4.7, 7.3, 1.3, 3.3, 5.4, 9.7, 8.3]
02 86 86 86 good 85 density [0.0, 0.2, 3.7, 4.8, 5.1, 3.3, 15.4, 8.6]
03 96 80 96 good 79 density [0.1, 4.2, 8.9, 7.0, 4.5, 3.4, 9.7, 3.6]
04 84 84 84 good 67 density [8.6, 8.2, 10.2, 3.0, 3.7, 4.5, 4.9, 3.2]
05 106 106 106 good 104 density [3.1, 3.5, 9.1, 5.8, 4.9, 4.9, 13.0, 8.6]
06 80 80 80 good 70 density [0.0, 2.1, 6.4, 7.5, 4.9, 2.7, 6.5, 0.7]
07 64 64 64 good 63 density [6.0, 9.2, 12.7, 4.8, 4.3, 2.8, 1.2, 0.0]
08 92 92 92 good 83 density [6.4, 4.2, 8.1, 2.1, 3.9, 5.0, 10.9, 6.4]
09 126 126 126 good 124 density [8.3, 5.4, 8.5, 3.6, 4.1, 4.9, 12.7, 8.0]
10 126 126 126 good 121 density [11.4, 8.1, 7.9, 3.2, 5.2, 5.2, 4.2, 2.8]
11 106 106 106 good 103 density [3.6, 7.2, 9.9, 6.2, 3.4, 4.5, 9.6, 6.5]
12 124 116 124 good 112 density [1.7, 4.7, 6.7, 0.5, 4.0, 6.5, 13.0, 7.1]
time 30.54310369491577 35
ReachEvents 35 precentral HFB -0.05 LFB -0.23 q -7.1
start_time 13 precentral HFB 0.02 LFB 0.484 q -7.4
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys,pickle,numpy as np
sys.path.insert(0,'entries/000055-peterson-2021')
import ajile
A,S=pickle.load(open('beh.pkl','rb'))
files=ajile.roi_files()
for sub in ['01','03','12']:
    df=ajile.read_roi_matrix(sub,files)
    z=np.nonzero(df.iloc[1:].transpose().mean().values==0)[0]
    first=[s for s in S if s['subject']==sub][0]; el=first['electrodes']
    print(sub,'zero rows',z.tolist())
    if len(df)-1==len(el): print(el.group_name.values[z].tolist())
    print(el.group_name.value_counts().to_dict())
EOF
```

```
01 zero rows [94, 95, 96, 97]
{'GRID': 64, 'LID': 8, 'LAT': 6, 'LPT': 6, 'LTO': 6, 'LMT': 4}
03 zero rows [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]
['LAD', 'LAD', 'LAD', 'LAD', 'LAD', 'LAD', 'LAD', 'LAD', 'LPD', 'LPD', 'LPD', 'LPD', 'LPD', 'LPD', 'LPD', 'LPD']
{'GRID': 64, 'LAT': 8, 'LMT': 8, 'LAD': 8, 'LPD': 8}
12 zero rows [72, 73, 74, 75, 76, 77, 78, 79]
['AID', 'AID', 'AID', 'AID', 'AID', 'AID', 'AID', 'AID']
{'GRID': 64, 'LOF': 8, 'AID': 8, 'PID': 8, 'AHD': 8, 'PHD': 8, 'LTP': 6, 'LPT': 6, 'LAT': 4, 'LMT': 4}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && python - <<'EOF'
p='ajile.py'; s=open(p).read()
old_w='''    rows = np.nonzero(df.transpose().mean().values != 0)[0][1:]
    w = df.iloc[rows][ROI_COLUMNS].to_numpy(float)'''
new_w='''    if len(df) - 1 == len(good):
        rows = np.arange(1, len(df))       # one row per electrode, in the file's order
    else:
        rows = np.nonzero(df.transpose().mean().values != 0)[0][1:]   # the code's rule
    w = df.iloc[rows][ROI_COLUMNS].to_numpy(float)'''
assert old_w in s; s=s.replace(old_w,new_w)
s=s.replace('''    """Electrodes x 8 weights as load_project_spectral_power(rem_bad_chans=True) builds them."""''','''    """Electrodes x 8 weights as load_project_spectral_power(rem_bad_chans=True) builds them.

    The code keeps the rows whose mean is not zero. Where the file has one row per electrode
    of the NWB file (10 of 12 subjects, with all-zero rows for some depth electrodes), every
    row is kept in order, so that the zero rows stay with their electrodes; where it has more
    rows (S01: 98 rows, the last four all zero, for 94 electrodes), the code's rule is used.
    """''')
old_q='''def segment_quality(x: np.ndarray, good: np.ndarray) -> tuple[float, float]:
    """Mean Welch log power (dB) of a segment over 1-200 Hz and over 115-125 Hz, good electrodes."""
    from scipy.signal import welch
    f, pxx = welch(x[good], fs=FS, nperseg=int(FS), axis=-1)
    with np.errstate(divide="ignore"):
        db = 10 * np.log10(pxx)
    db[np.isinf(db)] = -300.0
    a = db[:, (f >= 1) & (f <= 200)].mean()
    b = db[:, (f >= 115) & (f <= 125)].mean()
    return float(a), float(b)'''
new_q='''def segment_quality(x: np.ndarray, good: np.ndarray) -> tuple[float, float, float]:
    """Welch power of a segment's good electrodes (microvolts squared per Hz), in dB.

    Returns (a) 10*log10 of the power density averaged over 1-200 Hz, then averaged over
    electrodes (the reading used for the 0 dB test); (b) the same over 115-125 Hz (the 3 SD
    test); (c) the log density averaged over 1-200 Hz (the other reading of the 0 dB test).
    """
    from scipy.signal import welch
    f, pxx = welch(x[good], fs=FS, nperseg=int(FS), axis=-1)
    with np.errstate(divide="ignore"):
        a = 10 * np.log10(pxx[:, (f >= 1) & (f <= 200)].mean(-1))
        b = 10 * np.log10(pxx[:, (f >= 115) & (f <= 125)].mean(-1))
        c = 10 * np.log10(pxx[:, (f >= 1) & (f <= 200)])
    a[np.isinf(a)], b[np.isinf(b)], c[np.isinf(c)] = -300.0, -300.0, -300.0
    return float(a.mean()), float(b.mean()), float(c.mean())'''
assert old_q in s; s=s.replace(old_q,new_q)
s=s.replace('''    res = {k: [] for k in ["ok", "q_all", "q_hf", "roi_spec",''','''    res = {k: [] for k in ["ok", "q_all", "q_hf", "q_log", "roi_spec",''')
s=s.replace('''            for key in ["q_all", "q_hf"]:''','''            for key in ["q_all", "q_hf", "q_log"]:''')
s=s.replace('''        qa, qh = segment_quality(x, good)''','''        qa, qh, ql = segment_quality(x, good)''')
s=s.replace('''        res["q_hf"].append(qh)''','''        res["q_hf"].append(qh)
        res["q_log"].append(ql)''')
s=s.replace('''    `shift_s` moves every segment by that many seconds (for the clock check).
''','''    `starts` are event times on the ECoG clock (seconds from the series' first sample).
''')
s=s.replace('''- The bad electrodes are those of the subject's first file, as the code takes the
  bad list of the first file.''','''- The bad electrodes are those of the subject's first file, as the code takes the
  bad list of the first file.''')
s=s.replace('''  is summarised is an assumption: Welch power spectral density of each good electrode (1 s
  Hann windows, half overlap, a standard choice), 10*log10, averaged over 1-200 Hz and over
  good electrodes for the 0 dB test, and over 115-125 Hz for the 3 SD test, the SD taken over
  all of a subject's segments.''','''  is summarised is an assumption: Welch power spectral density of each good electrode (1 s
  Hann windows, half overlap, a standard choice) in microvolts squared per Hz, averaged over
  1-200 Hz, converted to dB and averaged over good electrodes for the 0 dB test, and the same
  over 115-125 Hz for the 3 SD test, the SD taken over all of a subject's segments. The other
  reading, the mean of the log density, is returned as well (`segment_quality`).''')
open(p,'w').write(s)
EOF
grep -n "q_log\|rows = " ajile.py | head
```

```
97:    rows = []
215:        rows = np.arange(1, len(df))       # one row per electrode, in the file's order
217:        rows = np.nonzero(df.transpose().mean().values != 0)[0][1:]   # the code's rule
293:    res = {k: [] for k in ["ok", "q_all", "q_hf", "q_log", "roi_spec", "roi_band", "roi_band_raw",
301:            for key in ["q_all", "q_hf", "q_log"]:
315:        res["q_log"].append(ql)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle,numpy as np
A,S=pickle.load(open('beh.pkl','rb'))
for s in S:
    w='R_Wrist' if s['reach_event_desc']=='r_wrist' else 'L_Wrist'
    tr=s['wrist'][w]; base=np.nanmean(tr[:,0:16],1)
    disp=np.linalg.norm(tr-base[:,None],axis=2)
    m=np.nanmedian(disp,0)
    if s['day'] in (3,7) or s['subject'] in('01','04','06'):
        print(s['subject'],s['day'], 'nan frac',np.isnan(tr).mean().round(2),'median disp at -1, 0, 0.5, 1 s', m[[15,45,60,75]].round(1))
EOF
```

```
<stdin>:5: RuntimeWarning: Mean of empty slice
01 3 nan frac 0.0 median disp at -1, 0, 0.5, 1 s [ 1.1  2.1 34.3 59.2]
01 4 nan frac 0.0 median disp at -1, 0, 0.5, 1 s [ 1.2  2.5 42.7 78.1]
01 5 nan frac 0.0 median disp at -1, 0, 0.5, 1 s [ 0.7  1.9 38.5 54.6]
01 7 nan frac 0.0 median disp at -1, 0, 0.5, 1 s [ 0.5  2.2 59.4 86.4]
02 3 nan frac 0.0 median disp at -1, 0, 0.5, 1 s [ 1.   3.8 33.7 61.8]
03 3 nan frac 0.0 median disp at -1, 0, 0.5, 1 s [ 1.   2.1 65.4 78.9]
04 3 nan frac 0.0 median disp at -1, 0, 0.5, 1 s [ 1.   2.7 30.1 44.7]
04 4 nan frac 0.0 median disp at -1, 0, 0.5, 1 s [ 1.4  3.5 20.3 38.5]
04 5 nan frac 0.0 median disp at -1, 0, 0.5, 1 s [ 1.1  3.4 36.6 52.5]
04 6 nan frac 0.0 median disp at -1, 0, 0.5, 1 s [ 1.   4.2 41.9 73.7]
04 7 nan frac 0.0 median disp at -1, 0, 0.5, 1 s [ 1.2  3.5 38.6 54.2]
05 3 nan frac 0.0 median disp at -1, 0, 0.5, 1 s [ 1.7  4.1 27.9 32.9]
05 7 nan frac 0.0 median disp at -1, 0, 0.5, 1 s [ 1.1  2.5 45.8 54.2]
06 3 nan frac 0.0 median disp at -1, 0, 0.5, 1 s [ 0.6  1.3 47.6 75.8]
06 4 nan frac 0.0 median disp at -1, 0, 0.5, 1 s [ 0.6  1.2 57.4 77. ]
06 5 nan frac 0.01 median disp at -1, 0, 0.5, 1 s [ 0.5  1.1 51.4 85.7]
06 6 nan frac 0.0 median disp at -1, 0, 0.5, 1 s [ 0.5  1.4 31.7 74.7]
06 7 nan frac 0.01 median disp at -1, 0, 0.5, 1 s [ 0.7  1.3 41.6 73.1]
07 3 nan frac 0.0 median disp at -1, 0, 0.5, 1 s [ 0.8  1.4 21.2 37.1]
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && cat >> ajile.py <<'EOF'


def ecog_offset(session: dict) -> float:
    """Seconds from midnight to the ECoG series' first sample.

    The files' events (`intervals/reaches`) and pose are on a clock that starts at midnight.
    Three files hold less than 24 h of ECoG (S01 day 7, S04 day 3, S06 day 3); their ECoG
    `starting_time` is 0, but `ReachEvents` and the session start time put its first sample at
    midnight plus the missing time, i.e. the series ends at midnight. The notebook checks this
    against the neural response.
    """
    return 24 * 3600.0 - session["ecog_shape"][0] / session["ecog_rate"]


def ecog_jobs(sessions: list, weights: dict, offset: bool = True) -> list:
    jobs = []
    for s in sessions:
        good = s["subject_good"]
        off = ecog_offset(s) if offset else 0.0
        jobs.append((s["asset_id"], s["events"]["start_time"].values - off, weights[s["subject"]],
                     good))
    return jobs
EOF
cd $TMPDIR && . dev/bin/activate && cat > run_ecog.py <<'EOF'
import sys, time, pickle, numpy as np, os
os.environ["OMP_NUM_THREADS"]="1"
sys.path.insert(0,'entries/000055-peterson-2021')
import ajile
A,S=pickle.load(open('beh.pkl','rb'))
files=ajile.roi_files()
W={}
for sub in sorted(set(s['subject'] for s in S)):
    first=[s for s in S if s['subject']==sub][0]
    good=first['electrodes'].good.values
    W[sub]=ajile.roi_weights(ajile.read_roi_matrix(sub,files),good)
    for s in S:
        if s['subject']==sub: s['subject_good']=good
jobs=ajile.ecog_jobs(S,W)
if len(sys.argv)>1:
    n=int(sys.argv[1]); jobs=[j+(n,) for j in jobs[:8]]
t=time.time()
R=ajile.load_ecog(jobs, workers=int(os.environ.get('W','8')))
print('time',time.time()-t, sum(sum(r['ok']) for r in R))
pickle.dump((W,R),open('ecog.pkl' if len(sys.argv)==1 else 'ecog_sub.pkl','wb'))
EOF
W=8 python run_ecog.py 10
```

```
time 23.107198476791382 80
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && W=4 python run_ecog.py 10; python - <<'EOF'
import cProfile,pstats,sys,pickle,numpy as np
sys.path.insert(0,'entries/000055-peterson-2021')
import ajile
x=np.random.randn(94,5000)*20
good=np.ones(94,bool)
import time
t=time.time(); 
for _ in range(5): ajile.segment_power(x)
print('power',(time.time()-t)/5)
t=time.time()
for _ in range(5): ajile.segment_quality(x,good)
print('q',(time.time()-t)/5)
p=ajile.segment_power(x); W=np.random.rand(94,8)
t=time.time()
for _ in range(5):
    pb=p-p[...,:6].mean(-1,keepdims=True); np.einsum("er,eft->rft", W, pb); ajile.band_values(pb); ajile.band_values(p)
print('rest',(time.time()-t)/5)
EOF
```

```
time 27.105767726898193 80
power 0.3717511177062988
q 0.11972179412841796
rest 0.0027875423431396483
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && python - <<'EOF'
p='ajile.py'; s=open(p).read()
old=s[s.index('def segment_power'):s.index('def segment_quality')]
new='''_WAVELET_FFT = {}


def _wavelet_fft(n_fft: int) -> np.ndarray:
    """FFTs of MNE's Morlet wavelets (mne.time_frequency.morlet, zero_mean=True) for FREQS."""
    if n_fft not in _WAVELET_FFT:
        ws = []
        for f, nc in zip(FREQS, FREQS / 4.0):
            sigma_t = nc / (2.0 * np.pi * f)
            t = np.arange(0.0, 5.0 * sigma_t, 1.0 / FS)
            t = np.r_[-t[::-1], t[1:]]
            osc = np.exp(2.0 * 1j * np.pi * f * t) - np.exp(-2.0 * (np.pi * f * sigma_t) ** 2)
            w = osc * np.exp(-(t ** 2) / (2.0 * sigma_t ** 2))
            w /= np.sqrt(0.5) * np.linalg.norm(w.ravel())
            ws.append(w)
        _WAVELET_FFT[n_fft] = (np.array([np.fft.fft(w, n_fft) for w in ws]),
                               np.array([len(w) for w in ws]))
    return _WAVELET_FFT[n_fft]


def segment_power(x: np.ndarray) -> np.ndarray:
    """x: electrodes x samples (10 s, microvolts) -> electrodes x freqs x times, dB, cropped.

    Convolution with each wavelet by FFT, 'same' mode as in mne.time_frequency.tfr_array_morlet
    (use_fft=True), then every 50th sample, cropped to TIMES, 10*log10 with infinite values
    set to 0 (code, compute_tfr).
    """
    n = x.shape[-1]
    n_fft = 1 << int(np.ceil(np.log2(n + 400)))
    wf, wl = _wavelet_fft(n_fft)
    xf = np.fft.fft(x, n_fft, axis=-1)
    out = np.empty((x.shape[0], len(FREQS), len(range(0, n, DECIM))))
    for i, (w, L) in enumerate(zip(wf, wl)):
        c = np.fft.ifft(xf * w[None], axis=-1)
        start = (L - 1) // 2
        c = c[:, start:start + n][:, ::DECIM]
        out[:, i] = c.real ** 2 + c.imag ** 2
    t_all = np.arange(out.shape[-1]) * DECIM / FS - SEG_HALF_S
    keep = np.nonzero((t_all >= TIMES[0] - 1e-6) & (t_all <= TIMES[-1] + 1e-6))[0]
    p = out[..., keep]
    with np.errstate(divide="ignore"):
        p = 10 * np.log10(p)
    p[np.isinf(p)] = 0
    return p


'''
s=s.replace(old,new)
s=s.replace('''  here the same wavelets are convolved by FFT (`use_fft=True`), which gives the same values
  away from the segment edges, and the edges are cropped. A standard choice that cannot change
  a result.''','''  here the same wavelets (MNE's `morlet`, zero mean) are convolved by FFT, as MNE does with
  `use_fft=True`, which gives the same values away from the segment edges, and the edges are
  cropped. A standard choice that cannot change a result; `segment_power` is checked against
  MNE in the notebook.''')
open(p,'w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys,time,numpy as np
sys.path.insert(0,'entries/000055-peterson-2021')
import ajile
from mne.time_frequency import tfr_array_morlet
rng=np.random.default_rng(0); x=rng.standard_normal((94,5000))*20
t=time.time(); p=ajile.segment_power(x); print('mine',time.time()-t)
q=tfr_array_morlet(x[None],sfreq=500,freqs=ajile.FREQS,n_cycles=ajile.FREQS/4,zero_mean=True,use_fft=True,decim=50,output='power',verbose=False)[0]
q=10*np.log10(q[...,5:96]); print(p.shape,q.shape, np.abs(p-q).max())
q2=tfr_array_morlet(x[None,:3],sfreq=500,freqs=ajile.FREQS,n_cycles=ajile.FREQS/4,zero_mean=True,use_fft=False,decim=50,output='power',verbose=False)[0]
print('vs direct', np.abs(p[:3]-10*np.log10(q2[...,5:96])).max())
EOF
```

```
mine 0.15594220161437988
(94, 25, 91) (94, 25, 91) 1.20614629395277e-12
vs direct 1.4788170688007085e-13
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && W=8 python run_ecog.py; date -u
```

```
Sat Nov  7 03:30:01 UTC 2026
time 1604.3210077285767 8087
Sat Nov  7 03:56:53 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle,numpy as np,pandas as pd
A,S=pickle.load(open('beh.pkl','rb')); W,R=pickle.load(open('ecog.pkl','rb'))
rows=[]
for s,r in zip(S,R):
    for k in range(len(s['events'])):
        rows.append(dict(sub=s['subject'],day=s['day'],ok=r['ok'][k],qa=r['q_all'][k],qh=r['q_hf'][k],ql=r['q_log'][k]))
D=pd.DataFrame(rows)
print(D.groupby('sub')[['qa','qh','ql']].describe().round(1).iloc[:, [1,3,5,7, 9,11,13,15]].to_string())
print((~D.ok).sum(), D[~D.ok])
for scope in ['sub','all']:
    if scope=='sub':
        thr=D.groupby('sub').qh.transform(lambda v: v.mean()+3*v.std())
    else:
        thr=D.qh.mean()+3*D.qh.std()
    bad=(D.qa<0)|(D.qh>thr)|(~D.ok)
    cnt=D[~bad].groupby('sub').size()
    print(scope, cnt.tolist(), cnt.min(), cnt.max(), cnt.median(), 'qa<0',(D.qa<0).sum(),'hf',(D.qh>thr).sum())
print('ql<0', (D.ql<0).sum(), len(D))
EOF
```

```
qa                      qh                  
     mean   min   50%   max  mean   min   50%   max
sub                                                
01    7.7   5.2   7.6  11.6 -12.2 -14.1 -12.3  -9.7
02   12.1   8.0  11.8  20.8 -12.3 -14.6 -12.3  -8.8
03   10.1   6.7  10.1  18.1 -11.3 -14.3 -11.5   6.8
04    7.0   5.2   6.6  12.1 -12.1 -13.5 -12.0 -10.3
05   11.2   6.0   9.6  17.5 -11.6 -13.8 -11.7  -8.0
06    9.1   6.9   9.0  14.3  -7.6 -10.0  -7.8  -1.9
07   10.3   7.4  10.3  14.9 -10.7 -11.5 -10.7  -8.7
08    5.6   3.7   5.5  10.7 -10.2 -12.3 -10.3  -6.6
09    7.2   3.2   7.1  13.3 -16.3 -17.8 -16.3 -14.1
10    8.0   3.8   8.4  12.5 -13.3 -15.1 -13.5  -7.3
11   11.7 -11.9  11.6  18.0  -9.5 -25.4  -9.9  -3.4
12    7.7   4.6   7.5  13.0 -13.5 -14.7 -13.5 -11.6
1      sub  day     ok  qa  qh  ql
4521  08    4  False NaN NaN NaN
sub [738, 301, 637, 417, 263, 938, 790, 957, 211, 793, 978, 989] 211 989 764.0 qa<0 1 hf 74
all [741, 305, 640, 417, 267, 927, 800, 964, 211, 806, 977, 996] 211 996 770.5 qa<0 1 hf 35
ql<0 7931 8088
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle,numpy as np,pandas as pd
A,S=pickle.load(open('beh.pkl','rb'))
E=pd.concat([s['events'].assign(sub=s['subject'],day=s['day']) for s in S])
print(E.isna().groupby(E['sub']).sum().to_string())
print(E.describe().round(2).to_string())
print(E.Bimanual_class.value_counts(dropna=False).head())
print(E.Reach_angle_degrees.describe())
print(E.groupby('sub').size().to_dict())
EOF
```

```
start_time  stop_time  Reach_magnitude_px  Reach_angle_degrees  Onset_speed_px_per_sec  Speech_ratio  Bimanual_ratio  Bimanual_overlap  Bimanual_class  duration  sub  day
sub                                                                                                                                                                            
01            0          0                   0                    0                       0             0               0                 0               0         0    0    0
02            0          0                   0                    0                       0             0               0                 0               0         0    0    0
03            0          0                   0                    0                       0             0               0                 0               0         0    0    0
04            0          0                   0                    0                       0             0               0                 0               0         0    0    0
05            0          0                   0                    0                       0             0               0                 0               0         0    0    0
06            0          0                   0                    0                       0             0               0                 0               0         0    0    0
07            0          0                   0                    0                       0             0               0                 0               0         0    0    0
08            0          0                   0                    0                       0             0               0                 0               0         0    0    0
09            0          0                   0                    0                       0             0               0                 0               0         0    0    0
10            0          0                   0                    0  
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle,numpy as np,pandas as pd
A,S=pickle.load(open('beh.pkl','rb'))
res=[]
for s in S[:12]:
    w='R_Wrist' if s['reach_event_desc']=='r_wrist' else 'L_Wrist'
    tr=s['wrist'][w]; ev=s['events']
    for k in range(len(ev)):
        n=int(round(ev.duration.iloc[k]*30))
        seg=tr[k,45:46+min(n,45)]
        if np.isnan(seg).any(): continue
        d=seg-seg[0]; r=np.linalg.norm(d,axis=1); j=r.argmax()
        ang=np.degrees(np.arctan2(d[j,1],d[j,0]))
        res.append((ev.Reach_angle_degrees.iloc[k], ang, ev.Reach_magnitude_px.iloc[k], r[j]))
R=np.array(res)
def cd(a,b): return np.abs((a-b+180)%360-180)
print('n',len(R),'median |diff| same sign', np.median(cd(R[:,0],R[:,1])), 'negated', np.median(cd(R[:,0],-R[:,1])))
print('magnitude ratio median', np.median(R[:,2]/R[:,3]), np.corrcoef(R[:,2],R[:,3])[0,1])
E=pd.concat([s['events'] for s in S]); print('ratio==0.5', (E.Bimanual_ratio==0.5).mean())
EOF
```

```
n 1687 median |diff| same sign 2.299367862773181 negated 114.75973208448045
magnitude ratio median 0.9916641485796727 0.7531729461805858
ratio==0.5 0.003214638971315529
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && python - <<'EOF'
p='ajile.py'; s=open(p).read()
old='''    n_iter = int(np.ceil(n_perms / len(baseidx)))
    nf = curr_power.shape[0]
    boot = np.zeros((nf, len(baseidx), n_iter))
    base = curr_power[:, baseidx, :]
    for it in range(n_iter):
        tmp = base.copy()
        for j in range(nf):
            for k in range(tmp.shape[2]):
                tmp[j, :, k] = tmp[j, rng.permutation(len(baseidx)), k]
        boot[:, :, it] = np.median(tmp, 2)
    boot = boot.reshape(nf, -1).T
    p = np.zeros(ave.shape)
    for j in range(nf):
        for k in range(ave.shape[1]):
            q = percentileofscore(boot[:, j], ave[j, k]) / 100
            p[j, k] = 2 * (1 - q) if q > 0.5 else 2 * q'''
new='''    n_iter = int(np.ceil(n_perms / len(baseidx)))
    nf = curr_power.shape[0]
    boot = np.zeros((nf, len(baseidx), n_iter))
    base = curr_power[:, baseidx, :]
    for it in range(n_iter):
        order = np.argsort(rng.random(base.shape), axis=1)   # shuffle time within freq, subject
        boot[:, :, it] = np.median(np.take_along_axis(base, order, axis=1), 2)
    boot = boot.reshape(nf, -1)
    p = np.zeros(ave.shape)
    for j in range(nf):
        q = percentileofscore(boot[j], ave[j], kind="rank") / 100
        p[j] = np.where(q > 0.5, 2 * (1 - q), 2 * q)'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/000055-peterson-2021 && cat >> ajile.py <<'EOF'


# ---------------------------------------------------------------- regression (timing only)

def regression_design(ev: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """The ten features of one subject's events as the claims file's opening comment sets them:
    day one-hot, time of day one-hot in 0-8, 8-16, 16-24 h, log duration, log magnitude, folded
    angle, onset speed, speech ratio, bimanual ratio, overlap and class, all z-scored."""
    cols, groups = {}, {}
    for d in sorted(ev["day"].unique()):
        cols[f"day_{d}"] = (ev["day"] == d).astype(float)
    groups["day"] = [c for c in cols]
    for b in range(3):
        cols[f"tod_{b}"] = (ev["tod_bin"] == b).astype(float)
    groups["time_of_day"] = [f"tod_{b}" for b in range(3)]
    cols["duration"] = np.log(ev["duration"])
    cols["magnitude"] = np.log(ev["magnitude"])
    for c in ["angle", "speed", "speech", "bimanual_ratio", "bimanual_overlap", "bimanual_class"]:
        cols[c] = ev[c].astype(float)
        groups[c] = [c]
    groups["duration"], groups["magnitude"] = ["duration"], ["magnitude"]
    X = pd.DataFrame(cols, index=ev.index)
    sd = X.std(ddof=0).replace(0, 1)
    return (X - X.mean()) / sd, groups


def _adj_r2(X, y):
    A = np.column_stack([np.ones(len(y)), X])
    beta, *_ = np.linalg.lstsq(A, y, rcond=None)
    res = y - A @ beta
    r2 = 1 - (res @ res) / ((y - y.mean()) @ (y - y.mean()))
    n, k = len(y), A.shape[1] - 1
    return 1 - (1 - r2) * (n - 1) / (n - k - 1)


def forward_select(X: pd.DataFrame, groups: dict, y: np.ndarray) -> list:
    """Forward selection by OLS adjusted R2 (code, _forward_selected_new), over feature groups."""
    remaining, selected, current = list(groups), [], 0.0
    while remaining:
        scores = [(_adj_r2(X[sum((groups[g] for g in selected + [c]), [])].to_numpy(), y), c)
                  for c in remaining]
        best, cand = max(scores)
        if best > current:
            selected.append(cand)
            remaining.remove(cand)
            current = best
        else:
            break
    return selected


def regression_model(X, groups, y, days, rng, n_splits=200, per_train=0.9):
    """One electrode and band: Huber regression over day-balanced splits, full R2 and Delta R2."""
    from sklearn.linear_model import HuberRegressor
    from sklearn.metrics import r2_score
    sel = forward_select(X, groups, y)
    cols = sum((groups[g] for g in sel), [])
    Xs = X[cols].to_numpy()
    days = np.asarray(days)
    uni = np.unique(days)
    n_test_day = int(((1 - per_train) * len(days)) // len(uni))
    r2s, dr2 = [], {g: [] for g in groups}
    for _ in range(n_splits):
        tr, te = [], []
        for d in uni:
            idx = rng.permutation(np.nonzero(days == d)[0])
            tr.extend(idx[:-n_test_day])
            te.extend(idx[-n_test_day:])
        tr, te = np.array(tr), np.array(te)
        if not cols:
            r2s.append(0.0)
            continue
        m = HuberRegressor().fit(Xs[tr], y[tr])
        full = r2_score(y[te], m.predict(Xs[te]))
        r2s.append(full)
        for g in groups:
            if g not in sel:
                dr2[g].append(0.0)
                continue
            Xsh = Xs[tr].copy()
            gi = [cols.index(c) for c in groups[g]]
            Xsh[:, gi] = Xsh[rng.permutation(len(tr))][:, gi]
            ms = HuberRegressor().fit(Xsh, y[tr])
            dr2[g].append(full - r2_score(y[te], ms.predict(Xs[te])))
    return {"selected": sel, "r2": float(np.mean(r2s)),
            "delta_r2": {g: float(np.mean(v)) if v else 0.0 for g, v in dr2.items()}}
EOF
echo ok
```

```
/bin/bash: line 1: cd: entries/000055-peterson-2021: No such file or directory
ok
```

**Agent calls Bash**

```bash
pwd; grep -n "^def " entries/000055-peterson-2021/ajile.py
```

```
entries/000055-peterson-2021
91:def asset_url(asset_id: str) -> str:
96:def list_assets() -> pd.DataFrame:
111:def _open(asset_id):
115:def _s(v):
119:def read_session(asset_id: str) -> dict:
179:def load_sessions(assets: pd.DataFrame, workers: int = 8) -> list[dict]:
187:def fold_angle(a):
197:def roi_files() -> dict:
202:def read_roi_matrix(subject: str, files: dict) -> pd.DataFrame:
207:def roi_weights(df: pd.DataFrame, good: np.ndarray) -> np.ndarray:
228:def _band_idx(band):
232:def _tidx(lo, hi):
239:def _wavelet_fft(n_fft: int) -> np.ndarray:
256:def segment_power(x: np.ndarray) -> np.ndarray:
282:def segment_quality(x: np.ndarray, good: np.ndarray) -> tuple[float, float, float]:
299:def band_values(p: np.ndarray) -> dict:
311:def ecog_session(args) -> dict:
358:def load_ecog(jobs: list, workers: int = 8) -> list[dict]:
366:def boot_sig_mask(curr_power: np.ndarray, baseidx: np.ndarray, rng: np.random.Generator,
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> entries/000055-peterson-2021/ajile.py <<'EOF'


# ---------------------------------------------------------------- regression (timing only)

def regression_design(ev: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """The ten features of one subject's events as the claims file's opening comment sets them:
    day one-hot, time of day one-hot in 0-8, 8-16, 16-24 h, log duration, log magnitude, folded
    angle, onset speed, speech ratio, bimanual ratio, overlap and class, all z-scored."""
    cols, groups = {}, {}
    for d in sorted(ev["day"].unique()):
        cols[f"day_{d}"] = (ev["day"] == d).astype(float)
    groups["day"] = [c for c in cols]
    for b in range(3):
        cols[f"tod_{b}"] = (ev["tod_bin"] == b).astype(float)
    groups["time_of_day"] = [f"tod_{b}" for b in range(3)]
    cols["duration"] = np.log(ev["duration"])
    cols["magnitude"] = np.log(ev["magnitude"])
    groups["duration"], groups["magnitude"] = ["duration"], ["magnitude"]
    for c in ["angle", "speed", "speech", "bimanual_ratio", "bimanual_overlap", "bimanual_class"]:
        cols[c] = ev[c].astype(float)
        groups[c] = [c]
    X = pd.DataFrame(cols, index=ev.index)
    sd = X.std(ddof=0).replace(0, 1)
    return (X - X.mean()) / sd, groups


def _adj_r2(X, y):
    A = np.column_stack([np.ones(len(y)), X])
    beta, *_ = np.linalg.lstsq(A, y, rcond=None)
    res = y - A @ beta
    r2 = 1 - (res @ res) / ((y - y.mean()) @ (y - y.mean()))
    n, k = len(y), A.shape[1] - 1
    return 1 - (1 - r2) * (n - 1) / (n - k - 1)


def forward_select(X: pd.DataFrame, groups: dict, y: np.ndarray) -> list:
    """Forward selection by OLS adjusted R2 (code, _forward_selected_new), over feature groups."""
    remaining, selected, current = list(groups), [], 0.0
    while remaining:
        scores = [(_adj_r2(X[sum((groups[g] for g in selected + [c]), [])].to_numpy(), y), c)
                  for c in remaining]
        best, cand = max(scores)
        if best > current:
            selected.append(cand)
            remaining.remove(cand)
            current = best
        else:
            break
    return selected


def regression_model(X, groups, y, days, rng, n_splits=200, per_train=0.9):
    """One electrode and band: Huber regression over day-balanced splits, full R2 and Delta R2.

    Used here only to time one model (sklearn HuberRegressor defaults, as the code)."""
    from sklearn.linear_model import HuberRegressor
    from sklearn.metrics import r2_score
    sel = forward_select(X, groups, y)
    cols = sum((groups[g] for g in sel), [])
    Xs = X[cols].to_numpy()
    days = np.asarray(days)
    uni = np.unique(days)
    n_test_day = int(((1 - per_train) * len(days)) // len(uni))
    r2s, dr2 = [], {g: [] for g in groups}
    for _ in range(n_splits):
        tr, te = [], []
        for d in uni:
            idx = rng.permutation(np.nonzero(days == d)[0])
            tr.extend(idx[:-n_test_day])
            te.extend(idx[-n_test_day:])
        tr, te = np.array(tr), np.array(te)
        if not cols:
            r2s.append(0.0)
            continue
        m = HuberRegressor().fit(Xs[tr], y[tr])
        full = r2_score(y[te], m.predict(Xs[te]))
        r2s.append(full)
        for g in groups:
            if g not in sel:
                dr2[g].append(0.0)
                continue
            Xsh = Xs[tr].copy()
            gi = [cols.index(c) for c in groups[g]]
            Xsh[:, gi] = Xsh[rng.permutation(len(tr))][:, gi]
            ms = HuberRegressor().fit(Xsh, y[tr])
            dr2[g].append(full - r2_score(y[te], ms.predict(Xs[te])))
    return {"selected": sel, "r2": float(np.mean(r2s)),
            "delta_r2": {g: float(np.mean(v)) if v else 0.0 for g, v in dr2.items()}}
EOF
date -u
```

```
Sat Nov  7 03:58:36 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nbtools.py",
 "content": "\"\"\"Convert a '# %%' source file to an ipynb, or run its code cells (dev mode, cached loads).\"\"\"\nimport re\nimport sys\n\nimport nbformat\n\n\ndef parse(path):\n    cells, cur, kind, tags = [], [], None, []\n    for line in open(path).read().split(\"\\n\"):\n        m = re.match(r\"^# %%( \\[markdown\\])?( tags=(\\S+))?\\s*$\", line)\n        if m:\n            if kind is not None:\n                cells.append((kind, tags, \"\\n\".join(cur).strip(\"\\n\")))\n            kind = \"markdown\" if m.group(1) else \"code\"\n            tags = m.group(3).split(\",\") if m.group(3) else []\n            cur = []\n        else:\n            cur.append(line)\n    if kind is not None:\n        cells.append((kind, tags, \"\\n\".join(cur).strip(\"\\n\")))\n    return cells\n\n\ndef build(src, out):\n    nb = nbformat.v4.new_notebook()\n    for kind, tags, text in parse(src):\n        if kind == \"markdown\":\n            text = \"\\n\".join(l[2:] if l.startswith(\"# \") else l[1:] if l.startswith(\"#\") else l\n                             for l in text.split(\"\\n\"))\n            c = nbformat.v4.new_markdown_cell(text)\n        else:\n            c = nbformat.v4.new_code_cell(text)\n        if tags:\n            c.metadata[\"tags\"] = tags\n        nb.cells.append(c)\n    nb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\n    nbformat.write(nb, out)\n\n\ndef run(src, upto=None, start=None):\n    import pickle\n    g = {}\n    cells = [c for c in parse(src) if c[0] == \"code\"]\n    for i, (kind, tags, text) in enumerate(cells):\n        if \"# LOAD-BEH\" in text:\n            text = text + \"\\nassets, sessions = __import__('pickle').load(open('/tmp/claude-1001/beh.pkl','rb'))\"\n        if \"# LOAD-ECOG\" in text:\n            text = (\"weights, ecog = __import__('pickle').load(open('/tmp/claude-1001/ecog.pkl','rb'))\\n\"\n                    + text.split(\"# LOAD-ECOG-END\")[1])\n        print(f\"\\n######## cell {i} {tags}\")\n        exec(compile(text, f\"cell{i}\", \"exec\"), g)\n        if upto is not None and i >= upto:\n            break\n    return g\n\n\nif __name__ == \"__main__\":\n    if sys.argv[1] == \"build\":\n        build(sys.argv[2], sys.argv[3])\n    else:\n        run(sys.argv[2])\n"
}
```

```
File created successfully at: /tmp/claude-1001/nbtools.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && python - <<'EOF'
s=open('nbtools.py').read()
s=s.replace('''        if "# LOAD-BEH" in text:
            text = text + "\\nassets, sessions = __import__('pickle').load(open('/tmp/claude-1001/beh.pkl','rb'))"''','''        if "# LOAD-BEH-END" in text:
            text = ("assets, sessions = __import__('pickle').load(open('/tmp/claude-1001/beh.pkl','rb'))\\n"
                    + text.split("# LOAD-BEH-END")[1])''')
s=s.replace('if "# LOAD-ECOG" in text:','if "# LOAD-ECOG-END" in text:')
open('nbtools.py','w').write(s)
EOF
grep -n "LOAD" nbtools.py
```

```
46:        if "# LOAD-BEH-END" in text:
48:                    + text.split("# LOAD-BEH-END")[1])
49:        if "# LOAD-ECOG-END" in text:
51:                    + text.split("# LOAD-ECOG-END")[1])
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_src.py",
 "content": "# %% [markdown]\n# # Reproducing Peterson et al. (2021) from dandiset 000055\n#\n# HEADER\n\n# %%\nimport os\nimport time\nimport warnings\n\nos.environ[\"OMP_NUM_THREADS\"] = \"1\"\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport ajile\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 300)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\nSUBJECTS = [f\"{i:02d}\" for i in range(1, 13)]\n\n# %%\nstarted = time.time()\nassets = ajile.list_assets()\nsessions = ajile.load_sessions(assets)\n# LOAD-BEH-END\nprint(f\"{len(sessions)} files of dandiset {ajile.DANDISET_ID} version {ajile.DANDISET_VERSION}, \"\n      f\"{assets.size_gb.sum():.0f} GB in all; metadata, events and wrist traces read in \"\n      f\"{time.time() - started:.0f} s\")\n\n# %%\n# One table of events. Time of day from the midnight clock of the files (see the helper).\nrows = []\nfor s in sessions:\n    e = s[\"events\"].copy()\n    e[\"subject\"], e[\"day\"], e[\"k\"] = s[\"subject\"], s[\"day\"], np.arange(len(e))\n    rows.append(e)\nev = pd.concat(rows, ignore_index=True)\nev = ev.rename(columns={\"Reach_magnitude_px\": \"magnitude\", \"Reach_angle_degrees\": \"angle_file\",\n                        \"Onset_speed_px_per_sec\": \"speed\", \"Speech_ratio\": \"speech\",\n                        \"Bimanual_ratio\": \"bimanual_ratio\", \"Bimanual_overlap\": \"bimanual_overlap\",\n                        \"Bimanual_class\": \"bimanual_class\"})\n# The files' angle is atan2(dy, dx) in image coordinates (checked below); the paper's angle\n# negates it (y up) and folds 90-270 degrees onto 90 to -90 (Methods; code).\nev[\"angle\"] = ajile.fold_angle(-ev[\"angle_file\"])\nev[\"hour\"] = ev[\"start_time\"] / 3600.0\nev[\"tod_bin\"] = np.clip((ev[\"hour\"] // 8).astype(int), 0, 2)\nFEATURES = [\"day\", \"hour\", \"duration\", \"magnitude\", \"angle\", \"speed\", \"speech\",\n            \"bimanual_ratio\", \"bimanual_overlap\", \"bimanual_class\"]\nprint(len(ev), \"events\")\n\n# %% [markdown]\n# ## Data check\n#\n# Counts by subject and day, units and ranges of every variable used, and the clocks of the\n# data streams. Each check of the metadata against the data is stated under its output.\n\n# %% tags=sanity\ninfo = pd.DataFrame([{\n    \"subject\": s[\"subject\"], \"day\": s[\"day\"], \"subject_id\": s[\"subject_id\"], \"session_id\": s[\"session_id\"],\n    \"session_start_time\": s[\"session_start_time\"], \"electrodes\": len(s[\"electrodes\"]),\n    \"good\": int(s[\"electrodes\"][\"good\"].sum()), \"events\": len(s[\"events\"]), \"wrist\": s[\"reach_event_desc\"],\n    \"ecog_hours\": round(s[\"ecog_shape\"][0] / s[\"ecog_rate\"] / 3600, 2), \"ecog_Hz\": s[\"ecog_rate\"],\n    \"pose_hours\": round(s[\"pose_shape\"][0] / s[\"pose_rate\"] / 3600, 2), \"pose_Hz\": s[\"pose_rate\"],\n    \"first_event_h\": round(s[\"events\"].start_time.min() / 3600, 2),\n    \"last_event_h\": round(s[\"events\"].start_time.max() / 3600, 2)} for s in sessions])\nprint(info.to_string(index=False))\nprint(\"\\nSubjects:\", info.subject.nunique(), \"; files:\", len(info), \"; events:\", int(info.events.sum()))\nprint(\"subject_id and session_id agree with the file names:\",\n      bool((info.subject_id == info.subject).all() and (info.session_id.astype(int) == info.day).all()))\nprint(\"Subject fields in the files:\", sorted({tuple(s[\"subject_fields\"]) for s in sessions}))\nprint(\"ECoG unit and conversion:\", {(s[\"ecog_unit\"], s[\"ecog_conversion\"]) for s in sessions},\n      \"; pose unit:\", {s[\"pose_unit\"] for s in sessions})\nprint(\"Electrode tables identical across a subject's files:\",\n      all(sessions[i][\"electrodes\"].drop(columns=[\"good\"]).equals(sessions[j][\"electrodes\"].drop(columns=[\"good\"]))\n          for i in range(len(sessions)) for j in range(len(sessions))\n          if sessions[i][\"subject\"] == sessions[j][\"subject\"]))\nprint(\"Good flags differ between a subject's files:\",\n      sorted({s[\"subject\"] for s in sessions for t in sessions\n              if s[\"subject\"] == t[\"subject\"] and not np.array_equal(s[\"electrodes\"].good.values, t[\"electrodes\"].good.values)}))\n\n# %% [markdown]\n# The files hold 12 subjects and 55 subject-days, ECoG at 500 Hz and pose at 30 frames per\n# second. The ECoG is stored with a conversion of 1e-6 to volts, so the stored values are\n# microvolts; the pose is labelled meters but holds pixels (the data descriptor gives pixels, and\n# the values span hundreds). The subject has no sex or age in the files or the archive's metadata.\n# Three files hold less than 24 h of ECoG and start later (S01 day 7, S04 day 3, S06 day 3); the\n# clocks of these files are checked below.\n\n# %% tags=sanity\ndesc = {c: None for c in [\"start_time\", \"stop_time\", \"duration\", \"magnitude\", \"angle_file\", \"angle\", \"speed\",\n                          \"speech\", \"bimanual_ratio\", \"bimanual_overlap\", \"bimanual_class\", \"hour\"]}\nprint(ev[list(desc)].describe().T[[\"count\", \"mean\", \"min\", \"50%\", \"max\"]].round(3).to_string())\nprint(\"\\nMissing values in any feature:\", int(ev[list(desc)].isna().sum().sum()))\nprint(\"Bimanual ratio exactly 0.5 (the code's fill for missing values):\", int((ev.bimanual_ratio == 0.5).sum()))\nprint(\"Bimanual overlap above 1 (the file calls it a fraction of the movement):\",\n      int((ev.bimanual_overlap > 1).sum()), \"events\")\nprint(\"Bimanual class values:\", sorted(ev.bimanual_class.unique()))\nprint(\"Events per day, largest:\", int(ev.groupby([\"subject\", \"day\"]).size().max()),\n      \"(Methods: up to 200 per day)\")\nprint(\"Reach durations (stop - start) within 0.5-4 s (Methods' movement duration rule):\",\n      int(ev.duration.between(0.5, 4).sum()), \"of\", len(ev), \"; shortest\", round(ev.duration.min(), 3), \"s\")\n\n# %% tags=sanity\n# Reach angle convention: angle and magnitude from the wrist trace (onset to the largest\n# displacement within the reach), compared with the files' values.\nrows = []\nfor s in sessions:\n    w = \"R_Wrist\" if s[\"reach_event_desc\"] == \"r_wrist\" else \"L_Wrist\"\n    tr = s[\"wrist\"][w]\n    for k, d in enumerate(s[\"events\"].duration.values):\n        n = int(round(d * ajile.POSE_HZ))\n        seg = tr[k, 45:46 + min(n, 45)]\n        if np.isnan(seg).any():\n            continue\n        dd = seg - seg[0]\n        r = np.linalg.norm(dd, axis=1)\n        j = r.argmax()\n        rows.append((s[\"events\"][\"Reach_angle_degrees\"].values[k], np.degrees(np.arctan2(dd[j, 1], dd[j, 0])),\n                     s[\"events\"][\"Reach_magnitude_px\"].values[k], r[j], d <= 1.5))\nang = pd.DataFrame(rows, columns=[\"file_angle\", \"trace_angle\", \"file_mag\", \"trace_mag\", \"within_window\"])\ncirc = lambda a, b: np.abs((a - b + 180) % 360 - 180)\na = ang[ang.within_window]\nprint(f\"{len(a)} reaches of at most 1.5 s with a full trace\")\nprint(\"median |file angle - trace angle|, image coordinates:\", round(np.median(circ(a.file_angle, a.trace_angle)), 2),\n      \"deg; with the trace angle negated (y up):\", round(np.median(circ(a.file_angle, -a.trace_angle)), 2), \"deg\")\nprint(\"median file magnitude / trace magnitude:\", round(np.median(a.file_mag / a.trace_mag), 3))\nprint(\"Folded angle (paper convention, +90 up): share of events above 0:\", round((ev.angle > 0).mean(), 3))\n\n# %% [markdown]\n# The files' reach angle is the angle of the reach in image coordinates (y pointing down), not yet\n# negated, so upward reaches have negative values; the paper's angle (+90 for upward) is its\n# negation folded onto -90 to 90, as the code does. The files do not say which convention they use.\n# The magnitudes match the traces.\n\n# %% tags=sanity\n# Clock of the pose and of the event times: contralateral wrist displacement from its mean\n# position over -1.5 to -1 s, at the events and at the events shifted by -30 s.\ndef median_disp(tr, base_slice=slice(0, 16)):\n    base = np.nanmean(tr[:, base_slice], 1)\n    return np.nanmedian(np.linalg.norm(tr - base[:, None], axis=2), 0)\n\nrows = []\nfor s in sessions:\n    w = \"R_Wrist\" if s[\"reach_event_desc\"] == \"r_wrist\" else \"L_Wrist\"\n    m = median_disp(s[\"wrist\"][w])\n    rows.append({\"subject\": s[\"subject\"], \"day\": s[\"day\"], \"disp_at_-1s\": m[15].round(1),\n                 \"disp_at_0s\": m[45].round(1), \"disp_at_+1s\": m[75].round(1)})\nclk = pd.DataFrame(rows)\nprint(clk.to_string(index=False))\nprint(\"Sessions where the contralateral wrist moves less than 10 pixels by +1 s:\",\n      clk[clk[\"disp_at_+1s\"] < 10][[\"subject\", \"day\"]].values.tolist())\n\n# %% [markdown]\n# In every file the contralateral wrist is still before the event time and moves after it, so the\n# pose and the event table share a clock, including in the three files with less than 24 h of\n# ECoG (whose events lie between 8 and 24 h). The shifted control needs the ECoG and is below.\n\n# %% tags=sanity\n# Time of day: the coarse behaviour labels by hour. Sleep should fall at night if the files\n# start at midnight, as the data descriptor says.\nlab = pd.concat([s[\"epochs\"].assign(subject=s[\"subject\"]) for s in sessions])\nlab[\"hour\"] = ((lab.start + lab.stop) / 2 / 3600).astype(int)\nsleep = lab[lab.label == \"Sleep/rest\"].groupby(\"hour\").size().reindex(range(24), fill_value=0)\nprint(\"Sleep/rest labels by hour of the file clock:\\n\", sleep.to_string())\nprint(\"Share of Sleep/rest labels at 0-8 h:\", round(sleep[:8].sum() / sleep.sum(), 3),\n      \"; events at 0-8 h:\", round((ev.hour < 8).mean(), 3))\nprint(\"session_start_time values:\", sorted(info.session_start_time.unique()))\n\n# %% [markdown]\n# Sleep labels fall mostly in the first hours of the file clock, which fits files that start at\n# midnight local time. The files' `session_start_time` of 19:00 at UTC-5 is midnight UTC, so the\n# stated time zone is not the local one; the three late files have start times of 03:07 to 03:31\n# at UTC-5, the start of their ECoG (checked below). The hour of an event is taken from the file\n# clock.\n\n# %% tags=sanity\n# Duplicates: identical event tables or wrist traces in two files.\nkeys = {}\nfor s in sessions:\n    k1 = np.round(s[\"events\"].start_time.values, 3).tobytes()\n    k2 = np.nan_to_num(s[\"wrist\"][\"R_Wrist\"]).round(2).tobytes()\n    keys.setdefault((\"events\", hash(k1)), []).append((s[\"subject\"], s[\"day\"]))\n    keys.setdefault((\"wrist\", hash(k2)), []).append((s[\"subject\"], s[\"day\"]))\ndups = {k: v for k, v in keys.items() if len(v) > 1}\nprint(\"Files with identical event times or identical wrist traces:\", dups if dups else \"none\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_src.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && . dev/bin/activate && cd entries/000055-peterson-2021 && python -c "
import sys; sys.path.insert(0,'/tmp/claude-1001'); import nbtools; nbtools.run('/tmp/claude-1001/nb_src.py')" 2>&1 | tail -150
```

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import sys; sys.path.insert(0,'/tmp/claude-1001'); import nbtools; nbtools.run('/tmp/claude-1001/nb_src.py')
                                                       ^^^^^^^^^^^^^^
  File "/tmp/claude-1001/nbtools.py", line 5, in <module>
    import nbformat
ModuleNotFoundError: No module named 'nbformat'
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && . dev/bin/activate && uv pip install -q nbformat nbconvert ipykernel pingouin 2>&1|tail -1; cd entries/000055-peterson-2021 && python -c "
import sys; sys.path.insert(0,'/tmp/claude-1001'); import nbtools; nbtools.run('/tmp/claude-1001/nb_src.py')" 2>&1 | tail -150
```

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import sys; sys.path.insert(0,'/tmp/claude-1001'); import nbtools; nbtools.run('/tmp/claude-1001/nb_src.py')
                                                                       ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/nbtools.py", line 53, in run
    exec(compile(text, f"cell{i}", "exec"), g)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "cell1", line 5, in <module>
NameError: name 'started' is not defined. Did you mean: 'sorted'?

######## cell 0 []

######## cell 1 []
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && sed -i "s|text = (\"assets, sessions = |text = (\"started=__import__('time').time(); assets, sessions = |" nbtools.py && . dev/bin/activate && cd entries/000055-peterson-2021 && python -c "
import sys; sys.path.insert(0,'/tmp/claude-1001'); import nbtools; nbtools.run('/tmp/claude-1001/nb_src.py')" 2>&1 | tail -150
```

```
08    5         08          5        2000-01-04T19:00:00-05:00          92    87     173 l_wrist       24.00    500.0        24.0     30.0           7.15         21.21
     08    6         08          6        2000-01-05T19:00:00-05:00          92    82     198 l_wrist       24.00    500.0        24.0     30.0           0.70         23.00
     08    7         08          7        2000-01-06T19:00:00-05:00          92    85     200 l_wrist       24.00    500.0        24.0     30.0           4.69         23.76
     09    3         09          3        2000-01-02T19:00:00-05:00         126   124      15 r_wrist       24.00    500.0        24.0     30.0           6.69         21.10
     09    4         09          4        2000-01-03T19:00:00-05:00         126   123      18 r_wrist       24.00    500.0        24.0     30.0           5.85         19.31
     09    5         09          5        2000-01-04T19:00:00-05:00         126   116     109 r_wrist       24.00    500.0        24.0     30.0           7.38         22.40
     09    6         09          6        2000-01-05T19:00:00-05:00         126   121      38 r_wrist       24.00    500.0        24.0     30.0           6.20         22.70
     09    7         09          7        2000-01-06T19:00:00-05:00         126   106      31 r_wrist       24.00    500.0        24.0     30.0           4.96         21.39
     10    3         10          3        2000-01-02T19:00:00-05:00         126   121     184 r_wrist       24.00    500.0        24.0     30.0           2.76         23.89
     10    4         10          4        2000-01-03T19:00:00-05:00         126   121     154 r_wrist       24.00    500.0        24.0     30.0           0.83         22.28
     10    5         10          5        2000-01-04T19:00:00-05:00         126   117     112 r_wrist       24.00    500.0        24.0     30.0           2.81         23.80
     10    6         10          6        2000-01-05T19:00:00-05:00         126   121     157 r_wrist 
[... 138 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && python - <<'EOF'
s=open('nb_src.py').read()
s=s.replace('''print("Electrode tables identical across a subject's files:",
      all(sessions[i]["electrodes"].drop(columns=["good"]).equals(sessions[j]["electrodes"].drop(columns=["good"]))''','''LOC = ["x", "y", "z", "group_name", "low_freq_R2", "high_freq_R2"]
print("Electrode positions, groups and stored R2 identical across a subject's files:",
      all(sessions[i]["electrodes"][LOC].equals(sessions[j]["electrodes"][LOC])''')
open('nb_src.py','w').write(s)
EOF
date -u
```

```
Sat Nov  7 03:59:48 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> /tmp/claude-1001/nb_src.py <<'EOF'

# %% [markdown]
# ## ECoG: projection matrices and event segments
#
# The paper's projection of electrodes onto the eight regions (AAL atlas through the Measure
# Projection Toolbox) is taken from its own output on Figshare (doi:10.6084/m9.figshare.12114408.v1),
# which the claims file names as the paper's output of that step. Claim `roi-projection-link`
# checks that its rows can be matched to the dataset's electrodes. The bad electrodes are those of
# each subject's first file, as the paper's code takes them.

# %%
roi_meta = ajile.roi_files()
roi_mats, weights_check = {}, {}
for sub in SUBJECTS:
    roi_mats[sub] = ajile.read_roi_matrix(sub, roi_meta)
first_good = {}
for s in sessions:
    first_good.setdefault(s["subject"], s["electrodes"]["good"].values.copy())
for s in sessions:
    s["subject_good"] = first_good[s["subject"]]
print("Figshare files read (name, md5):")
for sub in SUBJECTS:
    print(f"  aal_{sub}_elecs2ROI.csv", roi_meta[f"aal_{sub}_elecs2ROI.csv"][1])

# %%
started = time.time()
weights = {sub: ajile.roi_weights(roi_mats[sub], first_good[sub]) for sub in SUBJECTS}
ecog = ajile.load_ecog(ajile.ecog_jobs(sessions, weights))
# LOAD-ECOG-END
print(f"ECoG segments of {sum(sum(r['ok']) for r in ecog)} events read and reduced in "
      f"{(time.time() - started) / 60:.1f} min")
EOF
echo
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat >> /tmp/claude-1001/nb_src.py <<'EOF'

# %%
# Per-event ECoG measures, aligned with the event table.
REG = {n: i for i, n in enumerate(ajile.ROI_NAMES)}
ev["ok"] = np.concatenate([r["ok"] for r in ecog])
for key in ["q_all", "q_hf", "q_log"]:
    ev[key] = np.concatenate([r[key] for r in ecog])
spec = np.full((len(ev), 8, len(ajile.FREQS), len(ajile.TIMES)), np.nan, dtype=np.float32)
i = 0
for r in ecog:
    for ok, sp in zip(r["ok"], r["roi_spec"]):
        if ok:
            spec[i] = sp
        i += 1
for kind in ["roi_band", "roi_band_raw"]:
    for meas in ["lfb_mean", "lfb_median", "hfb_mean", "hfb_median"]:
        vals = np.full((len(ev), 8), np.nan)
        i = 0
        for r in ecog:
            for ok, b in zip(r["ok"], r[kind]):
                if ok:
                    vals[i] = b[meas]
                i += 1
        for reg, j in REG.items():
            ev[f"{kind}:{reg}:{meas}"] = vals[:, j]
# Bad segments (Methods): power below 0 dB, or 115-125 Hz power more than 3 SD above the mean
# of the subject's segments. False positives are not marked in the files (see the data check).
thr = ev[ev.ok].groupby("subject").q_hf.agg(lambda v: v.mean() + 3 * v.std())
ev["bad_low"] = ev.q_all < 0
ev["bad_hf"] = ev.q_hf > ev.subject.map(thr)
ev["keep_b"] = ev.ok & ~ev.bad_low & ~ev.bad_hf
TIMES, FREQS = ajile.TIMES, ajile.FREQS
print("Events with a full ECoG segment:", int(ev.ok.sum()), "of", len(ev))
print("Segments below 0 dB:", int(ev.bad_low.sum()), "; 115-125 Hz above 3 SD:", int((ev.bad_hf & ~ev.bad_low).sum()),
      "; kept (reading b):", int(ev.keep_b.sum()))
print("Other reading of the 0 dB test (mean of the log density below 0 dB):", int((ev.q_log < 0).sum()), "of",
      int(ev.ok.sum()), "segments would go, so that reading is not usable")
print(ev[ev.ok].groupby("subject")[["q_all", "q_hf"]].agg(["min", "median", "max"]).round(1).to_string())

# %% tags=sanity
# segment_power against MNE's own Morlet transform, on one segment of the data.
from mne.time_frequency import tfr_array_morlet
import h5py, remfile
s0 = sessions[0]
f0 = h5py.File(remfile.File(ajile.asset_url(s0["asset_id"])), "r")
c0 = int(round(s0["events"].start_time.values[0] * ajile.FS))
x0 = f0["acquisition/ElectricalSeries/data"][c0 - 2500:c0 + 2500, :8].T.astype(float)
f0.close()
mine = ajile.segment_power(x0)
ref = tfr_array_morlet(x0[None], sfreq=ajile.FS, freqs=FREQS, n_cycles=FREQS / 4, zero_mean=True, use_fft=False,
                       decim=ajile.DECIM, output="power", verbose=False)[0][..., 5:96]
print("largest difference from MNE tfr_array_morlet(use_fft=False), dB:", float(np.abs(mine - 10 * np.log10(ref)).max()))
print("segment amplitude range (microvolts):", round(float(x0.min()), 1), round(float(x0.max()), 1))

# %% tags=sanity
# Clock of the ECoG against the events: precentral and postcentral band power change from the
# -1.5 to -1 s baseline to 0-0.5 s, at the event time and at a pseudo-event 3 s earlier
# (-3 to -2.5 s against -4.5 to -4 s) in the same segments; median over events per file.
ti = lambda lo, hi: np.nonzero((TIMES >= lo - 1e-6) & (TIMES <= hi + 1e-6))[0]
lf = np.nonzero((FREQS >= 8) & (FREQS <= 32))[0]
hf = np.nonzero((FREQS >= 76) & (FREQS <= 100))[0]
def band_change(sp, band, t_on, t_base):
    return sp[..., band, :][..., t_on].mean((-1, -2)) - sp[..., band, :][..., t_base].mean((-1, -2))
rows = []
for (sub, day), g in ev[ev.ok].groupby(["subject", "day"]):
    sp = spec[g.index][:, [REG["precentral"], REG["postcentral"]]]
    row = {"subject": sub, "day": day, "n": len(g)}
    for name, band in [("HFB", hf), ("LFB", lf)]:
        true = band_change(sp, band, ti(0, 0.5), ti(-1.5, -1))
        pseudo = band_change(sp, band, ti(-3, -2.5), ti(-4.5, -4))
        best = np.argmax(np.abs(np.median(true, 0)))
        row[f"{name}_event"] = round(float(np.median(true[:, best])), 2)
        row[f"{name}_pseudo"] = round(float(np.median(pseudo[:, best])), 2)
    rows.append(row)
clock = pd.DataFrame(rows)
print(clock.to_string(index=False))
clock_ok = (clock.HFB_event > 0) & (clock.LFB_event < 0) & (clock.HFB_event > clock.HFB_pseudo) & (clock.LFB_event < clock.LFB_pseudo)
print("Files with HFB up, LFB down at the event and both larger than at the pseudo-event:", int(clock_ok.sum()), "of", len(clock))
print("Files where this does not hold:", clock[~clock_ok][["subject", "day"]].values.tolist())

# %% tags=sanity
# The three files with less than 24 h of ECoG: event times on the ECoG clock with the offset
# of the helper (ECoG ends at midnight) against no offset (ECoG starts at midnight).
late = [s for s in sessions if ajile.ecog_offset(s) > 1]
alt = ajile.load_ecog(ajile.ecog_jobs(late, weights, offset=False), workers=3)
for s, r in zip(late, alt):
    g = ev[(ev.subject == s["subject"]) & (ev.day == s["day"]) & ev.ok]
    pre = REG["precentral"]
    a_h = band_change(spec[g.index][:, pre], hf, ti(0, 0.5), ti(-1.5, -1))
    a_l = band_change(spec[g.index][:, pre], lf, ti(0, 0.5), ti(-1.5, -1))
    sp_b = np.array([x[pre] for x, ok in zip(r["roi_spec"], r["ok"]) if ok])
    b_h = band_change(sp_b, hf, ti(0, 0.5), ti(-1.5, -1)) if len(sp_b) else np.array([np.nan])
    b_l = band_change(sp_b, lf, ti(0, 0.5), ti(-1.5, -1)) if len(sp_b) else np.array([np.nan])
    print(f"S{s['subject']} day {s['day']}: offset {ajile.ecog_offset(s):.1f} s; with offset {len(a_h)} events, "
          f"precentral HFB {np.median(a_h):+.2f} dB, LFB {np.median(a_l):+.2f} dB; without offset {len(sp_b)} events in "
          f"range, HFB {np.median(b_h):+.2f} dB, LFB {np.median(b_l):+.2f} dB; ReachEvents minus offset-corrected "
          f"times, max |diff| {np.max(np.abs(s['reach_event_times'] - (s['events'].start_time.values - ajile.ecog_offset(s)))):.3f} s")
EOF
echo
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat >> /tmp/claude-1001/nb_src.py <<'EOF'

# %% [markdown]
# ## Claim `subject-days`
#
# > The dataset's subjects and recording days are the paper's subjects S01 to S12 and the
# > recording days the paper lists for each.

# %% tags=claim:subject-days
TABLE2 = {"01": [3, 4, 5, 7], "02": [3, 4, 5, 6], "03": [3, 4, 5, 6], "05": [3, 4, 7]}
TABLE2 = {s: TABLE2.get(s, [3, 4, 5, 6, 7]) for s in SUBJECTS}
days = info.groupby("subject").day.apply(list).to_dict()
for sub in SUBJECTS:
    print(f"S{sub}: dataset days {days[sub]}, Table 2 {TABLE2[sub]}, match {days[sub] == TABLE2[sub]}")
print("All 12 match:", all(days[s] == TABLE2[s] for s in SUBJECTS), "; subject-days:", sum(len(v) for v in days.values()))

# %% [markdown]
# ## Claim `roi-projection-link`
#
# > The rows of the paper's projection matrices (Figshare) can be matched one to one to the
# > dataset's electrodes, and the weights fit the electrodes' positions.

# %% tags=claim:roi-projection-link
cent_rows = {}
rows = []
rng_link = np.random.default_rng(55)
for sub in SUBJECTS:
    df = roi_mats[sub]
    el = [s for s in sessions if s["subject"] == sub][0]["electrodes"]
    n_rows = len(df) - 1
    zero = np.nonzero(df.iloc[1:].transpose().mean().values == 0)[0]
    cen = pd.read_csv(roi_meta[f"aal_{sub}_ROIcentroids_Lside.csv"][0])
    cen = cen.iloc[[df.columns.get_loc(c) for c in ajile.ROI_COLUMNS]].to_numpy(float)
    w = weights[sub]
    xyz = el[["x", "y", "z"]].to_numpy(float).copy()
    xyz[:, 0] = -np.abs(xyz[:, 0])                       # right hemisphere mirrored to the left
    dist = np.linalg.norm(xyz[:, None, :] - cen[None], axis=2)
    use = w.sum(1) > 0
    agree = np.mean(np.argmax(w[use], 1) == np.argmin(dist[use], 1))
    null = np.mean([np.mean(np.argmax(w[use], 1) == np.argmin(dist[use][rng_link.permutation(use.sum())], 1))
                    for _ in range(200)])
    rho = stats.spearmanr(w[use].ravel(), -dist[use].ravel())[0]
    rows.append({"subject": sub, "electrodes": len(el), "matrix_rows": n_rows, "all_zero_rows": len(zero),
                 "zero_row_groups": ",".join(sorted(set(el.group_name.values[zero]))) if n_rows == len(el) else
                 f"rows {zero.min()}-{zero.max()} (beyond the {len(el)} electrodes)",
                 "rows_used": len(w), "top_weight_is_nearest_centroid": round(agree, 3),
                 "same_with_order_shuffled": round(null, 3), "spearman_weight_vs_proximity": round(rho, 3)})
link = pd.DataFrame(rows)
print(link.to_string(index=False))
print("Subjects whose rows match the electrodes one to one:", int((link.rows_used == link.electrodes).sum()), "of 12")
print("Subjects where the weights fit positions better than with the order shuffled:",
      int((link.top_weight_is_nearest_centroid > link.same_with_order_shuffled).sum()), "of 12")
dens = pd.concat([roi_mats[s].iloc[0] for s in SUBJECTS], axis=1).mean(1)
print("Regions with mean electrode density > 3 (Methods):",
      [c for c in dens.index if dens[c] > 3], "\nthe eight of the claims file:", ajile.ROI_COLUMNS)

# %% [markdown]
# ## Claim `cohort`
#
# > Twelve subjects (8 male, 4 female, 29.4 +- 7.9 years) had on average 87.0 +- 12.9 surface
# > electrodes; five also had 23.2 +- 12.1 depth electrodes; five were implanted in the right
# > hemisphere and seven in the left.

# %% tags=claim:cohort
rows = []
for sub in SUBJECTS:
    s = [x for x in sessions if x["subject"] == sub][0]
    el = s["electrodes"]
    depth_groups = [g for g, d in s["group_desc"].items() if "depth" in d.lower()]
    is_depth = el.group_name.isin(depth_groups)
    rows.append({"subject": sub, "surface": int((~is_depth).sum()), "depth": int(is_depth.sum()),
                 "depth_groups": ",".join(depth_groups), "wrist": s["reach_event_desc"],
                 "mean_x": round(el.x.mean(), 1)})
coh = pd.DataFrame(rows)
print(coh.to_string(index=False))
hemi_right = (coh.wrist == "l_wrist").sum()
print(f"\nsubjects {len(coh)}; surface electrodes mean {coh.surface.mean():.1f} +- {coh.surface.std():.1f} (SD); "
      f"subjects with depth electrodes {(coh.depth > 0).sum()}, their mean {coh[coh.depth > 0].depth.mean():.1f} +- "
      f"{coh[coh.depth > 0].depth.std():.1f}; right hemisphere (left wrist events, x > 0) {hemi_right}")
print("Right hemisphere by wrist agrees with the sign of mean x:", bool(((coh.wrist == "l_wrist") == (coh.mean_x > 0)).all()))
print("Sex and age: not in the files or the archive's metadata (subject fields:", sessions[0]["subject_fields"], ")")
both = coh.copy()
both["all"] = both.surface + both.depth
print("Variant, every electrode counted: mean", round(both["all"].mean(), 1))

# %% [markdown]
# ## Claim `fig2-event-counts`
#
# > Each subject contributed between 151 and 947 movement events (median 640 across subjects).

# %% tags=claim:fig2-event-counts
cnt = pd.DataFrame({"a_all_events": ev.groupby("subject").size(),
                    "b_bad_segments_dropped": ev[ev.keep_b].groupby("subject").size()})
print(cnt.T.to_string())
for c in cnt:
    v = cnt[c]
    print(f"{c}: fewest {v.min()} (151 +- 15.1), most {v.max()} (947 +- 94.7), median {v.median():.1f} (640 +- 64); "
          f"within: {abs(v.min() - 151) <= 15.1}, {abs(v.max() - 947) <= 94.7}, {abs(v.median() - 640) <= 64}")
print("Total events:", len(ev), "; the data descriptor (Peterson et al. 2022, Sci Data) states 6931 verified events")
EOF
echo
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat >> /tmp/claude-1001/nb_src.py <<'EOF'

# %% [markdown]
# ## Claim `fig2-features-differ-across-subjects`
#
# > All ten behavioural and environmental features differ significantly across subjects.

# %% tags=claim:fig2-features-differ-across-subjects
rows = []
for label, sel in [("b", ev.keep_b), ("a", np.ones(len(ev), bool))]:
    for f in FEATURES:
        groups = [g[f].values for _, g in ev[sel].groupby("subject")]
        h, p = stats.kruskal(*groups)
        rows.append({"reading": label, "feature": f, "H": round(h, 1), "p": p, "below_0.001": p < 0.001})
kw = pd.DataFrame(rows)
print(kw.to_string(index=False))
print("All ten p < 0.001, reading b:", bool(kw[kw.reading == "b"].below_0.001.all()),
      "; reading a:", bool(kw[kw.reading == "a"].below_0.001.all()))
print("Largest p:", kw.groupby("reading").p.max().to_dict())

# %% [markdown]
# ## Claim `fig2-reach-shape`
#
# > Reach duration and reach magnitude vary little across subjects, with most reaches lasting
# > under 2 s and covering under 200 pixels, and reach angle distributions tend to be bimodal with
# > peaks near +90 and -90 degrees, with few side-to-side reaches.

# %% tags=claim:fig2-reach-shape
from scipy.stats import gaussian_kde
grid = np.linspace(-90, 90, 361)
def bimodal(a):
    dens = gaussian_kde(a, bw_method="scott")(grid)
    peaks = [i for i in range(1, len(grid) - 1) if dens[i] > dens[i - 1] and dens[i] >= dens[i + 1]]
    # ends of the range count as maxima when the density rises towards them
    if dens[0] > dens[1]:
        peaks.append(0)
    if dens[-1] > dens[-2]:
        peaks.append(len(grid) - 1)
    top = sorted(peaks, key=lambda i: -dens[i])[:2]
    locs = sorted(grid[top])
    zero = dens[np.argmin(np.abs(grid))]
    ok = len(locs) == 2 and abs(locs[0] + 90) <= 15 and abs(locs[1] - 90) <= 15 and zero < dens[top].min()
    return ok, locs, zero / dens[top].min() if len(top) else np.nan
E = ev[ev.keep_b]
rows = []
for sub, g in list(E.groupby("subject")) + [("pooled", E)]:
    ok, locs, rel = bimodal(g.angle.values)
    rows.append({"subject": sub, "n": len(g), "median_duration_s": round(g.duration.median(), 2),
                 "share_under_2s": round((g.duration < 2).mean(), 3), "median_magnitude_px": round(g.magnitude.median(), 1),
                 "share_under_200px": round((g.magnitude < 200).mean(), 3), "angle_peaks": np.round(locs, 1).tolist(),
                 "density_at_0_over_lower_peak": round(rel, 2), "bimodal_at_pm90": ok,
                 "share_within_30deg_of_0": round((g.angle.abs() < 30).mean(), 3)})
rs = pd.DataFrame(rows)
print(rs.to_string(index=False))
subj = rs[rs.subject != "pooled"]
pool = rs[rs.subject == "pooled"].iloc[0]
dm = (subj.share_under_2s > 0.5) & (subj.share_under_200px > 0.5)
print(f"\nduration and magnitude part: pooled {pool.share_under_2s > 0.5 and pool.share_under_200px > 0.5}, "
      f"subjects {int(dm.sum())} of 12")
print(f"angle part: pooled {pool.bimodal_at_pm90}, subjects {int(subj.bimodal_at_pm90.sum())} of 12")
print("Variant, reading a (all events):")
E2 = ev
print(" share under 2 s", round((E2.duration < 2).mean(), 3), "; under 200 px", round((E2.magnitude < 200).mean(), 3),
      "; pooled angle bimodal at +-90:", bimodal(E2.angle.values)[0], np.round(bimodal(E2.angle.values)[1], 1).tolist())

# %%
fig, axes = plt.subplots(1, 3, figsize=(12, 3))
for sub, g in E.groupby("subject"):
    axes[0].hist(g.duration, bins=np.linspace(0, 4, 41), histtype="step", density=True)
    axes[1].hist(g.magnitude, bins=np.linspace(0, 700, 71), histtype="step", density=True)
    axes[2].plot(grid, gaussian_kde(g.angle, bw_method="scott")(grid), lw=1)
axes[0].set_xlabel("reach duration (s)"); axes[1].set_xlabel("reach magnitude (pixels)"); axes[2].set_xlabel("reach angle (deg, +90 up)")
plt.tight_layout(); plt.show()
print("Plotted ranges: duration", round(E.duration.min(), 2), "-", round(E.duration.max(), 2), "s; magnitude",
      round(E.magnitude.min(), 1), "-", round(E.magnitude.max(), 1), "px (none outside the axes)")

# %% [markdown]
# ## Claim `fig2-bimanual-skew`
#
# > Bimanual ratio and bimanual overlap are skewed toward unimanual movement of the contralateral
# > arm, less so for subjects 02, 04 and 05, while the bimanual class is mostly bimanual.

# %% tags=claim:fig2-bimanual-skew
def bim_table(E):
    rows = []
    for sub, g in list(E.groupby("subject")) + [("pooled", E)]:
        rows.append({"subject": sub, "median_ratio": round(g.bimanual_ratio.median(), 3),
                     "ratio_skewed": g.bimanual_ratio.median() < 0.5,
                     "overlap_skewness": round(stats.skew(g.bimanual_overlap), 3),
                     "overlap_skewed": stats.skew(g.bimanual_overlap) > 0,
                     "share_class_bimanual": round(g.bimanual_class.mean(), 3),
                     "class_mostly_bimanual": g.bimanual_class.mean() > 0.5})
    return pd.DataFrame(rows)
for label, E_ in [("b", ev[ev.keep_b]), ("a", ev)]:
    bt = bim_table(E_)
    subj = bt[bt.subject != "pooled"]
    pool = bt[bt.subject == "pooled"].iloc[0]
    top_ratio = subj.sort_values("median_ratio", ascending=False).subject.head(5).tolist()
    low_skew = subj.sort_values("overlap_skewness").subject.head(5).tolist()
    named = all(s in top_ratio for s in ["02", "04", "05"]) and all(s in low_skew for s in ["02", "04", "05"])
    print(f"Reading {label}")
    print(bt.to_string(index=False))
    print(f"ratio part: pooled {pool.ratio_skewed}, subjects {int(subj.ratio_skewed.sum())}/12; overlap part: pooled "
          f"{pool.overlap_skewed}, subjects {int(subj.overlap_skewed.sum())}/12; class part: pooled {pool.class_mostly_bimanual}, "
          f"subjects {int(subj.class_mostly_bimanual.sum())}/12")
    print(f"five highest median ratios {top_ratio}; five lowest overlap skewness {low_skew}; S02, S04, S05 in both: {named}\n")
EOF
echo
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat >> /tmp/claude-1001/nb_src.py <<'EOF'

# %% [markdown]
# ## Claim `extfig2-1c-contralateral-larger`
#
# > Across all 12 subjects, the median displacement of the contralateral wrist after movement
# > onset is substantially greater than that of the ipsilateral wrist, confirming that event
# > detection mainly picked contralateral movements.

# %% tags=claim:extfig2-1c-contralateral-larger
t_pose = np.round(np.arange(91) / ajile.POSE_HZ + ajile.POSE_WIN[0], 3)
post = (t_pose >= 0) & (t_pose <= 1.5)
def disp(tr, reading):
    base = np.nanmean(tr[:, :16], 1) if reading == "a" else tr[:, 45]   # -1.5 to -1 s, or onset
    return np.linalg.norm(tr - base[:, None], axis=2)
rows = []
for sub in SUBJECTS:
    ss = [s for s in sessions if s["subject"] == sub]
    contra = "R_Wrist" if ss[0]["reach_event_desc"] == "r_wrist" else "L_Wrist"
    ipsi = "L_Wrist" if contra == "R_Wrist" else "R_Wrist"
    keep = np.concatenate([ev[(ev.subject == sub) & (ev.day == s["day"])].keep_b.values for s in ss])
    row = {"subject": sub, "contra": contra}
    for reading in ["a", "b"]:
        c = np.concatenate([disp(s["wrist"][contra], reading) for s in ss])[keep]
        i_ = np.concatenate([disp(s["wrist"][ipsi], reading) for s in ss])[keep]
        cm, im = np.nanmedian(c, 0)[post].max(), np.nanmedian(i_, 0)[post].max()
        row[f"{reading}_contra_peak_px"] = round(cm, 1)
        row[f"{reading}_ipsi_peak_px"] = round(im, 1)
        row[f"{reading}_ratio"] = round(cm / im, 2)
    rows.append(row)
cw = pd.DataFrame(rows)
print(cw.to_string(index=False))
for r in ["a", "b"]:
    print(f"reading {r}: contralateral peak larger in {(cw[f'{r}_contra_peak_px'] > cw[f'{r}_ipsi_peak_px']).sum()} of 12; "
          f"ratio min {cw[f'{r}_ratio'].min()}, median {cw[f'{r}_ratio'].median()}")

# %% [markdown]
# ## Claim `extfig2-2-feature-correlations`
#
# > Over all events, reach magnitude correlates with reach duration (r = 0.26) and onset speed
# > (r = 0.56), reach duration with bimanual overlap (r = 0.48), and the bimanual features with
# > one another (overlap and ratio 0.51, class and ratio 0.50, overlap and class 0.61).

# %% tags=claim:extfig2-2-feature-correlations
PAIRS = [("magnitude", "duration", 0.26), ("magnitude", "speed", 0.56), ("duration", "bimanual_overlap", 0.48),
         ("bimanual_overlap", "bimanual_ratio", 0.51), ("bimanual_class", "bimanual_ratio", 0.50),
         ("bimanual_overlap", "bimanual_class", 0.61)]
rows = []
for label, E_ in [("b", ev[ev.keep_b]), ("a", ev)]:
    corr = E_[FEATURES].corr()
    for x, y, paper in PAIRS:
        r = corr.loc[x, y]
        rows.append({"reading": label, "pair": f"{x} - {y}", "r": round(r, 3), "paper": paper,
                     "within_10pct": abs(r - paper) <= 0.1 * paper + 1e-9})
cr = pd.DataFrame(rows)
print(cr.to_string(index=False))
print("Within tolerance:", cr.groupby("reading").within_10pct.sum().to_dict(), "of 6")
print("\nPer subject, reading b (r):")
print(pd.DataFrame({f"{x}-{y}": ev[ev.keep_b].groupby("subject").apply(lambda g: g[x].corr(g[y])).round(2)
                    for x, y, _ in PAIRS}).to_string())

# %% [markdown]
# ## Claim `fig2-days-and-waking`
#
# > Reach counts were fairly even across recording days except for subjects 04, 05 and 09, each
# > with one day holding most events, and events occurred mostly during waking hours.

# %% tags=claim:fig2-days-and-waking
for label, E_ in [("b", ev[ev.keep_b]), ("a", ev)]:
    per_day = E_.groupby(["subject", "day"]).size().unstack(fill_value=0)
    busiest = (per_day.max(1) / per_day.sum(1)).round(3)
    awake = E_.groupby("subject").hour.apply(lambda h: (h >= 8).mean()).round(3)
    out = pd.DataFrame({"busiest_day_share": busiest, "share_08_24h": awake})
    print(f"Reading {label}\n", per_day.to_string(), "\n", out.T.to_string())
    over = out.index[out.busiest_day_share > 0.5].tolist()
    print(f"subjects whose busiest day holds more than half: {over}; named 04, 05, 09; "
          f"waking part (more than half at 08-24 h) holds in {(out.share_08_24h > 0.5).sum()} of 12\n")
EOF
cd /tmp/claude-1001 && . dev/bin/activate && cd entries/000055-peterson-2021 && python -c "
import sys; sys.path.insert(0,'/tmp/claude-1001'); import nbtools; nbtools.run('/tmp/claude-1001/nb_src.py')" 2>&1 | sed -n '/cell 9 /,$p'
```

```
######## cell 9 []
Figshare files read (name, md5):
  aal_01_elecs2ROI.csv 2f21bb61045296257e648323f9d58644
  aal_02_elecs2ROI.csv ddc5de6527a31405f0ec67f4a81ef8ea
  aal_03_elecs2ROI.csv 4f8b58ab393be10af1d59389a0c387de
  aal_04_elecs2ROI.csv 2e84691cbf15b005142eb079e559fceb
  aal_05_elecs2ROI.csv 6b5969a62e21a8407d936b1d3b86c1be
  aal_06_elecs2ROI.csv 5e75a457f63eb70226b013a1b0a71383
  aal_07_elecs2ROI.csv c1d620aea4f38cf280d5bf06787ef47c
  aal_08_elecs2ROI.csv 7be91f3f41c5883b144e9116a3c36e0b
  aal_09_elecs2ROI.csv 4579d56608e6b245fc715e1ad69fc396
  aal_10_elecs2ROI.csv fd66592385d1eca9bd3afdac2cac4dbb
  aal_11_elecs2ROI.csv fd7aaadaa43193a7f2f13b686090b4b9
  aal_12_elecs2ROI.csv 1b212f9a9c38fba07d00bc01e057ad13

######## cell 10 []
ECoG segments of 8087 events read and reduced in 0.1 min

######## cell 11 []
Events with a full ECoG segment: 8087 of 8088
[... 161 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && . dev/bin/activate && python - <<'EOF'
import sys,pickle,numpy as np
sys.path.insert(0,'entries/000055-peterson-2021')
import ajile, h5py, remfile
A,S=pickle.load(open('beh.pkl','rb')); W,R=pickle.load(open('ecog.pkl','rb'))
for idx in [0,1,8,30]:
    s=S[idx]; r=R[idx]
    sp=np.array([x for x in r['roi_spec'] if x is not None])
    print(s['subject'],s['day'],'nan events',np.isnan(sp).any(axis=(1,2,3)).mean(), 'band nan', np.mean([np.isnan(b['lfb_mean']).any() for b in r['el_band'] if b is not None]))
    elb=np.array([b['lfb_mean'] for b in r['el_band'] if b is not None]); 
    print('  electrodes with nan', np.nonzero(np.isnan(elb).any(0))[0], 'good flags of those (file)', s['electrodes'].good.values[np.isnan(elb).any(0)], 'first-file good', S[[i for i,x in enumerate(S) if x['subject']==s['subject']][0]]['electrodes'].good.values[np.isnan(elb).any(0)])
f=h5py.File(remfile.File(ajile.asset_url(S[0]['asset_id'])),'r')
x=f['acquisition/ElectricalSeries/data'][1000000:1005000,:]
print('nan cols', np.nonzero(np.isnan(x).any(0))[0], np.isnan(x).mean())
EOF
```

```
01 3 nan events 0.00641025641025641 band nan 0.00641025641025641
  electrodes with nan [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47
 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71
 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93] good flags of those (file) [False  True  True  True  True  True  True  True  True  True  True  True
  True  True  True  True  True  True  True  True  True False  True  True
  True  True  True  True  True False  True  True  True  True  True  True
 False  True  True  True  True  True  True  True  True  True  True  True
  True  True  True  True  True  True  True  True  True  True  True  True
  True  True  True  True  True False  True  True False  True  True  True
  True  True  True  True False  True  True  True False  True  True  True
  True  True  True  True False  True  True  True  True  True] first-file good [False  True  True  True  True  True  True  True  True  True  True  True
  True  True  True  True  True  True  True  True  True False  True  True
  True  True  True  True  True False  True  True  True  True  True  True
 False  True  True  True  True  True  True  True  True  True  True  True
  True  True  True  True  True  True  True  True  True  True  True  True
  True  True  True  True  True False  True  True False  True  True  True
  True  True  True  True False  True  True  True False  True  True  True
  True  True  True  True False  True  True  True  True  True]
01 4 nan events 0.00510204081632653 band nan 0.00510204081632653
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && python - <<'EOF'
s=open('nb_src.py').read()
old='''ev["bad_low"] = ev.q_all < 0
ev["bad_hf"] = ev.q_hf > ev.subject.map(thr)
ev["keep_b"] = ev.ok & ~ev.bad_low & ~ev.bad_hf'''
new='''ev["bad_missing"] = ev.ok & ~np.isfinite(ev.q_all)          # segments with missing (NaN) samples
ev["bad_low"] = ev.q_all < 0
ev["bad_hf"] = ev.q_hf > ev.subject.map(thr)
ev["keep_b"] = ev.ok & ~ev.bad_missing & ~ev.bad_low & ~ev.bad_hf'''
assert old in s; s=s.replace(old,new)
s=s.replace('''print("Segments below 0 dB:", int(ev.bad_low.sum()),''','''print("Segments with missing (NaN) samples:", int(ev.bad_missing.sum()), "in",
      ev[ev.bad_missing].groupby(["subject", "day"]).size().to_dict())
print("Segments below 0 dB:", int(ev.bad_low.sum()),''')
s=s.replace('''for (sub, day), g in ev[ev.ok].groupby(["subject", "day"]):
    sp = spec[g.index][:, [REG["precentral"], REG["postcentral"]]]''','''for (sub, day), g in ev[ev.keep_b].groupby(["subject", "day"]):
    sp = spec[g.index][:, [REG["precentral"], REG["postcentral"]]]''')
s=s.replace('''    g = ev[(ev.subject == s["subject"]) & (ev.day == s["day"]) & ev.ok]''','''    g = ev[(ev.subject == s["subject"]) & (ev.day == s["day"]) & ev.keep_b]''')
s=s.replace('''    sp_b = np.array([x[pre] for x, ok in zip(r["roi_spec"], r["ok"]) if ok])''','''    sp_b = np.array([x[pre] for x, ok in zip(r["roi_spec"], r["ok"]) if ok and np.isfinite(x[pre]).all()])''')
s=s.replace('below_0.001','p_below_0001')
open('nb_src.py','w').write(s)
EOF
cd /tmp/claude-1001 && . dev/bin/activate && cd entries/000055-peterson-2021 && python -c "
import sys; sys.path.insert(0,'/tmp/claude-1001'); import nbtools; nbtools.run('/tmp/claude-1001/nb_src.py')" 2>&1 | sed -n '/cell 11 /,/cell 12 /p;/cell 13 /,/cell 15 /p;/cell 19 /,$p' | grep -v "^     .*  NaN"
```

```
######## cell 11 []
Events with a full ECoG segment: 8087 of 8088
Segments with missing (NaN) samples: 124 in {('01', 3): 1, ('01', 4): 1, ('01', 5): 4, ('02', 4): 1, ('02', 5): 2, ('04', 4): 1, ('04', 6): 1, ('04', 7): 3, ('06', 3): 1, ('06', 4): 7, ('06', 6): 8, ('06', 7): 11, ('07', 7): 6, ('08', 3): 4, ('08', 4): 2, ('08', 6): 3, ('08', 7): 1, ('10', 3): 7, ('10', 5): 1, ('10', 6): 23, ('10', 7): 16, ('11', 3): 2, ('11', 4): 1, ('11', 5): 3, ('11', 6): 1, ('11', 7): 3, ('12', 3): 2, ('12', 4): 3, ('12', 5): 3, ('12', 7): 2}
Segments below 0 dB: 1 ; 115-125 Hz above 3 SD: 74 ; kept (reading b): 7888
Other reading of the 0 dB test (mean of the log density below 0 dB): 7931 of 8087 segments would go, so that reading is not usable
        q_all               q_hf             
          min median   max   min median   max
subject                                      
01        5.2    7.6  11.6 -14.1  -12.3  -9.7
02        8.0   11.8  20.8 -14.6  -12.3  -8.8
03        6.7   10.1  18.1 -14.3  -11.5   6.8
04        5.2    6.6  12.1 -13.5  -12.0 -10.3
05        6.0    9.6  17.5 -13.8  -11.7  -8.0
06        6.9    9.0  14.3 -10.0   -7.8  -1.9
07        7.4   10.3  14.9 -11.5  -10.7  -8.7
08        3.7    5.5  10.7 -12.3  -10.3  -6.6
09        3.2    7.1  13.3 -17.8  -16.3 -14.1
10        3.8    8.4  12.5 -15.1  -13.5  -7.3
11      -11.9   11.6  18.0 -25.4   -9.9  -3.4
12        4.6    7.5  13.0 -14.7  -13.5 -11.6
[... 244 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat >> /tmp/claude-1001/nb_src.py <<'EOF'

# %% [markdown]
# ## Claim `fig3-group-lfb-decrease-hfb-increase`
#
# > At the group level, low-frequency power decreases and high-frequency power increases at
# > movement initiation in several cortical regions, as in controlled movement experiments.

# %% tags=claim:fig3-group-lfb-decrease-hfb-increase
rng_fig3 = np.random.default_rng(3)
keep = ev.keep_b.values
subj_med = np.stack([np.median(spec[np.nonzero(keep & (ev.subject.values == sub))[0]], axis=0) for sub in SUBJECTS])
base_i = ti(-1.5, -1)
group = subj_med.mean(0)
subj_c = subj_med - np.median(group[..., base_i], axis=-1, keepdims=True)[None]     # plot_specs_group
masked = np.stack([ajile.boot_sig_mask(np.moveaxis(subj_c[:, r], 0, -1), base_i, rng_fig3) for r in range(8)])
unmasked = subj_c.mean(0)
LF34 = np.nonzero((FREQS >= 4) & (FREQS <= 30))[0]
HF50 = np.nonzero((FREQS >= 50) & (FREQS <= 120))[0]
t_a, t_b = ti(0, 0.5), np.array([np.argmin(np.abs(TIMES))])
rows = []
for r, name in enumerate(ajile.ROI_NAMES):
    row = {"region": name}
    for lab, tt in [("a_0-0.5s", t_a), ("b_t0", t_b)]:
        row[f"{lab}_LF4-30"] = round(float(masked[r][LF34][:, tt].mean()), 3)
        row[f"{lab}_HF50-120"] = round(float(masked[r][HF50][:, tt].mean()), 3)
    row["unmasked_a_LF"] = round(float(unmasked[r][LF34][:, t_a].mean()), 3)
    row["unmasked_a_HF"] = round(float(unmasked[r][HF50][:, t_a].mean()), 3)
    row["significant_bins"] = int((masked[r] != 0).sum())
    rows.append(row)
f3 = pd.DataFrame(rows)
print(f3.to_string(index=False))
named = ["precentral", "postcentral", "inferior parietal"]
for lab in ["a_0-0.5s", "b_t0"]:
    holds = f3[f3.region.isin(named)].apply(lambda r: r[f"{lab}_LF4-30"] < 0 and r[f"{lab}_HF50-120"] > 0, axis=1)
    print(f"reading {lab}: pattern holds in {int(holds.sum())} of 3 named regions",
          dict(zip(named, holds.values)))
print("Regions with the pattern under reading a:",
      f3[(f3["a_0-0.5s_LF4-30"] < 0) & (f3["a_0-0.5s_HF50-120"] > 0)].region.tolist())

# %%
fig, axes = plt.subplots(2, 4, figsize=(13, 5), sharex=True, sharey=True)
tsel = ti(-1.5, 1.5)
for r, ax in enumerate(axes.ravel()):
    im = ax.pcolormesh(TIMES[tsel], FREQS, masked[r][:, tsel], cmap="RdBu_r", vmin=-1, vmax=1, shading="nearest")
    ax.axvline(0, color="k", lw=1)
    ax.set_title(ajile.ROI_NAMES[r], fontsize=9)
axes[1, 0].set_xlabel("time (s)"); axes[1, 0].set_ylabel("frequency (Hz)")
fig.colorbar(im, ax=axes, label="dB (masked)")
plt.show()
print("masked values shown, -1.5 to 1.5 s: range", round(float(masked[..., tsel].min()), 2), "to",
      round(float(masked[..., tsel].max()), 2), "dB; values beyond +-1 dB:", int((np.abs(masked[..., tsel]) > 1).sum()))

# %% [markdown]
# ## Claim `fig3-sensorimotor-largest`
#
# > Spectral power changes are largest in precentral, postcentral and inferior parietal regions,
# > and the three temporal regions show minimal movement-related changes.

# %% tags=claim:fig3-sensorimotor-largest
temporal = ["superior temporal", "middle temporal", "inferior temporal"]
def check_rank(vals):
    order = list(pd.Series(vals).sort_values(ascending=False).index)
    top3 = set(order[:3]) == set(named)
    temp_below = all(vals[t] < min(vals[n] for n in named) for t in temporal)
    return order, top3, temp_below, sum(n in order[:3] for n in named)
res = {}
va = {n: float(np.abs(masked[r][:, t_a]).mean()) for r, n in enumerate(ajile.ROI_NAMES)}
vc = {n: float(np.abs(masked[r][:, ti(-0.5, 0.5)]).mean()) for r, n in enumerate(ajile.ROI_NAMES)}
vl = {n: float(np.abs(masked[r][LF34][:, t_a]).mean()) for r, n in enumerate(ajile.ROI_NAMES)}
vh = {n: float(np.abs(masked[r][HF50][:, t_a]).mean()) for r, n in enumerate(ajile.ROI_NAMES)}
print(pd.DataFrame({"a_all_freqs_0-0.5": va, "b_LF": vl, "b_HF": vh, "c_all_freqs_-0.5-0.5": vc}).round(3).to_string())
for lab, v in [("a", va), ("c", vc)]:
    order, top3, tb, k = check_rank(v)
    print(f"reading {lab}: order {order}; named three are the top three {top3} ({k} of 3); temporal below all three {tb}")
ol, tl, tbl, kl = check_rank(vl)
oh, th, tbh, kh = check_rank(vh)
print(f"reading b: LF order {ol}\n           HF order {oh}\n  top three in both {tl and th} (LF {kl}/3, HF {kh}/3); "
      f"temporal below all three in both {tbl and tbh}")

# %% [markdown]
# ## Claim `fig3-lfb-more-widespread`
#
# > Low-frequency power decreases are more spatially widespread than high-frequency increases and
# > are also present in supramarginal and superior temporal regions.

# %% tags=claim:fig3-lfb-more-widespread
neg_lf = {n: int((masked[r][LF34][:, t_a] < 0).sum()) for r, n in enumerate(ajile.ROI_NAMES)}
pos_hf = {n: int((masked[r][HF50][:, t_a] > 0).sum()) for r, n in enumerate(ajile.ROI_NAMES)}
print(pd.DataFrame({"significant negative 4-30 Hz bins": neg_lf, "significant positive 50-120 Hz bins": pos_hf}).to_string())
a_lf, a_hf = sum(v > 0 for v in neg_lf.values()), sum(v > 0 for v in pos_hf.values())
b_lf, b_hf = sum(neg_lf.values()) / len(LF34), sum(pos_hf.values()) / len(HF50)
print(f"reading a: regions with LF decreases {a_lf}, with HF increases {a_hf}; LF larger {a_lf > a_hf}")
print(f"reading b: LF bins per frequency {b_lf:.2f}, HF bins per frequency {b_hf:.2f}; LF larger {b_lf > b_hf}")
print("supramarginal and superior temporal have LF decreases:", neg_lf["supramarginal"] > 0, neg_lf["superior temporal"] > 0)
EOF
echo
```

```
Sat Nov  7 04:04:52 UTC 2026
```

**Agent calls Bash**

```bash
cat >> /tmp/claude-1001/nb_src.py <<'EOF'

# %% [markdown]
# ## Claim `fig4-precentral-subject-variability`
#
# > In the precentral region every subject shows the low/high-frequency pattern, but amplitudes
# > and frequency bands vary; subjects 03, 06, 07, 08 and 11 have increases up to 120 Hz, subjects
# > 09 and 12 mainly at 60-80 Hz, and subjects 04 and 08 have narrower low-frequency decreases.

# %% tags=claim:fig4-precentral-subject-variability
pre = REG["precentral"]
sp4 = subj_med[:, pre] - subj_med[:, pre][..., base_i].mean(-1, keepdims=True)     # plot_specs_single_region
spectrum = pd.DataFrame(sp4[..., t_a].mean(-1), index=SUBJECTS, columns=FREQS)
print("Precentral spectrum, mean over 0-0.5 s (dB):")
print(spectrum.round(2).to_string())
lfb_i, hfb_i = (FREQS >= 8) & (FREQS <= 32), (FREQS >= 76) & (FREQS <= 100)
p1 = (spectrum.loc[:, lfb_i].mean(1) < 0) & (spectrum.loc[:, hfb_i].mean(1) > 0)
print("\n(1) LFB mean < 0 and HFB mean > 0:", p1.to_dict(), "->", bool(p1.all()))
p2 = {s: bool(spectrum.loc[s, 116] > 0 and spectrum.loc[s, 121] > 0) for s in ["03", "06", "07", "08", "11"]}
print("(2) 116 and 121 Hz positive:", p2, "->", all(p2.values()))
p3 = {}
for s in ["09", "12"]:
    hi = spectrum.loc[s, FREQS >= 56]
    peak_f = hi.idxmax()
    p3[s] = (int(peak_f), round(hi.max(), 3), round(spectrum.loc[s, (FREQS >= 101)].mean(), 3),
             bool(61 <= peak_f <= 76 and spectrum.loc[s, FREQS >= 101].mean() < hi.max() / 2))
print("(3) peak frequency, peak, mean 101-121 Hz, holds:", p3, "->", all(v[-1] for v in p3.values()))
low = spectrum.loc[:, FREQS <= 46]
width = {s: int((low.loc[s] < low.loc[s].min() / 2).sum()) for s in SUBJECTS}
fewest = sorted(width, key=lambda s: (width[s], s))[:3]
ties = sorted(width.values())[2]
print("(4) width of the decrease (1-46 Hz bins below half the most negative value):", width)
print("    three fewest:", fewest, "; third-smallest width", ties, "shared by",
      [s for s in SUBJECTS if width[s] == ties], "; S04 and S08 among them:", "04" in fewest and "08" in fewest)
print("Parts holding:", int(p1.all()) + int(all(p2.values())) + int(all(v[-1] for v in p3.values())) +
      int("04" in fewest and "08" in fewest), "of 4")

# %% [markdown]
# ## Claim `fig5-band-power-differs-across-subjects`
#
# > Precentral LFB and HFB power in the 0.5 s after movement onset differs significantly across
# > subjects.

# %% tags=claim:fig5-band-power-differs-across-subjects
E = ev[ev.keep_b]
for meas in ["mean", "median"]:
    for band in ["lfb", "hfb"]:
        col = f"roi_band:precentral:{band}_{meas}"
        h, p = stats.kruskal(*[g[col].values for _, g in E.groupby("subject")])
        print(f"band {meas}, {band.upper()}: Kruskal-Wallis H = {h:.1f}, p = {p:.3g}, n = {len(E)} events in 12 subjects")

# %% [markdown]
# ## Claim `table1-subject-band-power-ci`
#
# > Each subject's precentral band power lies in the 95% bootstrap interval Table 1 gives; LFB
# > power is below baseline and HFB power above it for most subjects.

# %% tags=claim:table1-subject-band-power-ci
TABLE1 = {"01": [(-1.87, -1.29), (0.03, 0.23)], "02": [(-1.12, -0.31), (0.07, 0.64)], "03": [(-2.11, -1.73), (1.39, 1.67)],
          "04": [(-0.17, 0.01), (0.32, 0.52)], "05": [(-0.7, -0.38), (0.2, 0.48)], "06": [(-1.63, -1.11), (2.02, 2.37)],
          "07": [(-0.84, -0.51), (1.14, 1.34)], "08": [(-0.3, 0.04), (0.36, 0.63)], "09": [(-0.57, -0.08), (-0.11, 0.23)],
          "10": [(-0.87, -0.35), (0.01, 0.3)], "11": [(-2.3, -1.86), (0.09, 0.34)], "12": [(-0.66, -0.44), (0.06, 0.2)]}
rng_t1 = np.random.default_rng(1)
rows, inside = [], {}
for sub in SUBJECTS:
    g = E[E.subject == sub]
    for bi_, band in enumerate(["lfb", "hfb"]):
        lo, hi = TABLE1[sub][bi_]
        row = {"subject": sub, "band": band.upper(), "paper_ci": f"{lo} to {hi}"}
        for bm in ["mean", "median"]:
            v = g[f"roi_band:precentral:{band}_{bm}"].values
            for stat_name, fn in [("mean", np.mean), ("median", np.median)]:
                est = fn(v)
                key = f"{stat_name}_of_band{bm}"
                row[key] = round(est, 3)
                inside.setdefault(key, []).append(lo <= est <= hi)
        v = g[f"roi_band:precentral:{band}_mean"].values
        boot = np.array([np.mean(v[rng_t1.integers(0, len(v), len(v))]) for _ in range(5000)])
        row["bootstrap_ci_mean_of_bandmean"] = f"{np.percentile(boot, 2.5):.2f} to {np.percentile(boot, 97.5):.2f}"
        rows.append(row)
t1 = pd.DataFrame(rows)
print(t1.to_string(index=False))
print("\nPoint estimates inside the paper's interval, of 24 subject and band pairs:",
      {k: int(sum(v)) for k, v in inside.items()})
lfb_neg = (t1[t1.band == "LFB"]["mean_of_bandmean"] < 0).sum()
hfb_pos = (t1[t1.band == "HFB"]["mean_of_bandmean"] > 0).sum()
print(f"LFB below baseline in {lfb_neg} of 12 subjects; HFB above in {hfb_pos} of 12 (mean of band mean)")

# %% [markdown]
# ## Claim `fig5-recording-day-effects`
#
# > Precentral band power differs significantly across recording days in LFB for subjects 03,
# > 05, 06, 07, 08 and 11, and in HFB for subjects 03, 04, 07, 08 and 10, despite baseline
# > subtraction.

# %% tags=claim:fig5-recording-day-effects
PAPER_SIG = {("03", "lfb"), ("05", "lfb"), ("06", "lfb"), ("07", "lfb"), ("08", "lfb"), ("11", "lfb"),
             ("03", "hfb"), ("04", "hfb"), ("07", "hfb"), ("08", "hfb"), ("10", "hfb")}
rows = []
for meas in ["mean", "median"]:
    for band in ["lfb", "hfb"]:
        for sub in SUBJECTS:
            g = E[E.subject == sub]
            h, p = stats.kruskal(*[d[f"roi_band:precentral:{band}_{meas}"].values for _, d in g.groupby("day")])
            rows.append({"measure": meas, "band": band.upper(), "subject": sub, "p": p, "significant": p < 0.05,
                         "paper_significant": (sub, band) in PAPER_SIG})
dayk = pd.DataFrame(rows)
dayk["agrees"] = dayk.significant == dayk.paper_significant
print(dayk.pivot_table(index=["band", "subject"], columns="measure", values="p").round(4).to_string())
print("\nAgreement with the paper's 24 subject and band pairs:", dayk.groupby("measure").agrees.sum().to_dict())
for meas in ["mean", "median"]:
    d = dayk[dayk.measure == meas]
    print(f"band {meas}: significant here but not in the paper {d[d.significant & ~d.paper_significant][['band','subject']].values.tolist()}; "
          f"in the paper but not here {d[~d.significant & d.paper_significant][['band','subject']].values.tolist()}")
EOF
echo
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat >> /tmp/claude-1001/nb_src.py <<'EOF'

# %% [markdown]
# ## Claim `extfig5-1-baseline-reduces-day-variability`
#
# > Subtracting the -1.5 to -1 s baseline reduces the variability of band power across recording
# > days, though clear variability remains.

# %% tags=claim:extfig5-1-baseline-reduces-day-variability
# Electrode band power (band mean), with and without baseline subtraction, for kept events.
el = {}
i = 0
for s, r in zip(sessions, ecog):
    for k, ok in enumerate(r["ok"]):
        if keep[i]:
            for kind in ["el_band", "el_band_raw"]:
                for band in ["lfb", "hfb"]:
                    el.setdefault((s["subject"], kind, band), []).append((s["day"], r[kind][k][f"{band}_mean"]))
        i += 1
rows_a, rows_b = [], []
for sub in SUBJECTS:
    good = first_good[sub]
    for band in ["lfb", "hfb"]:
        g = E[E.subject == sub]
        sd = {}
        for kind, col in [("with", f"roi_band:precentral:{band}_mean"), ("without", f"roi_band_raw:precentral:{band}_mean")]:
            sd[kind] = g.groupby("day")[col].mean().std()
        rows_a.append({"subject": sub, "band": band.upper(), "sd_with": round(sd["with"], 3), "sd_without": round(sd["without"], 3)})
        for kind in ["with", "without"]:
            items = el[(sub, "el_band" if kind == "with" else "el_band_raw", band)]
            days_ = np.array([d for d, _ in items])
            vals = np.array([v for _, v in items])[:, good]
            dm = np.array([vals[days_ == d].mean(0) for d in np.unique(days_)])
            sd[kind + "_el"] = dm.std(0, ddof=1)
        for k_ in range(good.sum()):
            rows_b.append({"subject": sub, "band": band.upper(), "sd_with": sd["with_el"][k_], "sd_without": sd["without_el"][k_]})
ra, rb = pd.DataFrame(rows_a), pd.DataFrame(rows_b)
print("Reading a, precentral region per subject (SD across days of day means, dB):")
print(ra.pivot(index="subject", columns="band", values=["sd_with", "sd_without"]).to_string())
for band in ["LFB", "HFB"]:
    a_ = ra[ra.band == band]
    b_ = rb[rb.band == band]
    print(f"{band}: reading a, SD lower with baseline in {(a_.sd_with < a_.sd_without).sum()} of {len(a_)} subjects "
          f"(median {a_.sd_with.median():.3f} against {a_.sd_without.median():.3f} dB); reading b, in "
          f"{(b_.sd_with < b_.sd_without).sum()} of {len(b_)} good electrodes ({(b_.sd_with < b_.sd_without).mean():.3f}; "
          f"median {b_.sd_with.median():.3f} against {b_.sd_without.median():.3f} dB)")
print("Day effects that remain (claim fig5-recording-day-effects, band mean): significant subject and band pairs",
      int(dayk[(dayk.measure == "mean") & dayk.significant].shape[0]))

# %% [markdown]
# ## Claim `discussion-day-changes-small`
#
# > Day-to-day changes in baseline-subtracted spectral power are small (about 1-2 dB) compared
# > with spectral power without baseline subtraction (about 10-50 dB).

# %% tags=claim:discussion-day-changes-small
rows = []
for sub in SUBJECTS:
    g = E[E.subject == sub]
    for band in ["lfb", "hfb"]:
        col = f"roi_band:precentral:{band}_mean"
        dm = g.groupby("day")[col].mean()
        raw = g[f"roi_band_raw:precentral:{band}_mean"].mean()
        rows.append({"subject": sub, "band": band.upper(), "largest_day_change_dB": round((dm - g[col].mean()).abs().max(), 3),
                     "day_mean_range_dB": round(dm.max() - dm.min(), 3), "level_uV_dB": round(raw, 2),
                     "level_V_dB": round(raw - 120, 2)})
dc = pd.DataFrame(rows)
print(dc.to_string(index=False))
print(f"\nlargest day change {dc.largest_day_change_dB.max():.3f} dB (holds at <= 2.2: {(dc.largest_day_change_dB <= 2.2).all()}); "
      f"range of day means up to {dc.day_mean_range_dB.max():.3f} dB")
print(f"levels without baseline: microvolts {dc.level_uV_dB.min():.1f} to {dc.level_uV_dB.max():.1f} dB "
      f"(within 9-55: {dc.level_uV_dB.between(9, 55).all()}); volts {dc.level_V_dB.min():.1f} to {dc.level_V_dB.max():.1f} dB "
      f"(within 9-55: {dc.level_V_dB.between(9, 55).all()})")

# %% [markdown]
# ## Regression claims (Figure 6 and Extended Data Figure 6-2): timing
#
# The six regression claims need, for every good electrode of every subject and both bands, forward
# selection and 200 day-balanced splits, each with a Huber fit of the full model and one refit per
# selected feature (opening comment of the claims file). One model is timed here and the whole is
# estimated from it.

# %% tags=claim:fig6-r2-at-most-025
rng_fig6 = np.random.default_rng(6)
sub = "07"
g = E[E.subject == sub]
X, groups = ajile.regression_design(g)
items = el[(sub, "el_band", "lfb")]
vals = np.array([v for _, v in items])
best = int(np.argmax([abs(np.corrcoef(X["angle"], vals[:, k])[0, 1]) for k in range(vals.shape[1])]))
t0 = time.time()
model = ajile.regression_model(X, groups, vals[:, best], g.day.values, rng_fig6, n_splits=200)
t_model = time.time() - t0
n_models = 2 * sum(int(first_good[s].sum()) for s in SUBJECTS)
print(f"one model (S{sub}, electrode {best}, LFB, {len(g)} events, 200 splits): {t_model:.1f} s; "
      f"selected {model['selected']}; withheld R2 {model['r2']:.3f}")
print(f"models needed: {n_models} (good electrodes x 2 bands); estimate for the main analysis "
      f"{t_model * n_models / 3600:.1f} h on one core, {t_model * n_models / 3600 / os.cpu_count():.1f} h on "
      f"{os.cpu_count()} cores; the claims add three variants (80/20 split, the code's shuffle, bad electrodes)")
r2_file = pd.concat([s["electrodes"].assign(subject=s["subject"]) for s in sessions if s["day"] == min(
    x["day"] for x in sessions if x["subject"] == s["subject"])])
print("For reference, the regression R2 stored in the files' electrode tables (low_freq_R2, high_freq_R2): "
      f"max {r2_file.low_freq_R2.max():.3f} and {r2_file.high_freq_R2.max():.3f}; electrodes with values "
      f"{int(r2_file.low_freq_R2.notna().sum())} of {len(r2_file)}")
EOF
cd /tmp/claude-1001 && . dev/bin/activate && cd entries/000055-peterson-2021 && python -c "
import sys; sys.path.insert(0,'/tmp/claude-1001'); import nbtools; nbtools.run('/tmp/claude-1001/nb_src.py')" 2>&1 | sed -n '/cell 26 /,$p'
```

```
######## cell 26 ['claim:fig3-group-lfb-decrease-hfb-increase']
           region  a_0-0.5s_LF4-30  a_0-0.5s_HF50-120  b_t0_LF4-30  b_t0_HF50-120  unmasked_a_LF  unmasked_a_HF  significant_bins
   middle frontal           -0.405              0.223       -0.363          0.215         -0.405          0.223              1436
       precentral           -0.885              0.496       -0.748          0.460         -0.885          0.496              1353
      postcentral           -0.890              0.507       -0.742          0.477         -0.890          0.507              1434
inferior parietal           -0.663              0.277       -0.592          0.278         -0.663          0.277              1337
    supramarginal           -0.304              0.014       -0.201          0.000         -0.304          0.049               700
superior temporal           -0.143             -0.003       -0.114         -0.007         -0.156         -0.008               380
  middle temporal           -0.005              0.003        0.000          0.004         -0.027          0.011               233
inferior temporal            0.000              0.012        0.000          0.006         -0.011          0.034               205
reading a_0-0.5s: pattern holds in 3 of 3 named regions {'precentral': np.True_, 'postcentral': np.True_, 'inferior parietal': np.True_}
reading b_t0: pattern holds in 3 of 3 named regions {'precentral': np.True_, 'postcentral': np.True_, 'inferior parietal': np.True_}
Regions with the pattern under reading a: ['middle frontal', 'precentral', 'postcentral', 'inferior parietal', 'supramarginal', 'middle temporal']

######## cell 27 []
masked values shown, -1.5 to 1.5 s: range -1.31 to 0.7 dB; values beyond +-1 dB: 53

######## cell 28 ['claim:fig3-sensorimotor-largest']
                   a_all_freqs_0-0.5   b_LF   b_HF  c_all_freqs_-0.5-0.5
middle frontal                 0.236  0.405  0.223                 0.167
[... 173 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd /tmp/claude-1001 && python - <<'EOF'
s=open('nb_src.py').read()
old='''print("Parts holding:", int(p1.all())'''
new='''# The bin count ties four subjects at 3 bins. Tie-break by the width in Hz of the run of the
# spectrum below half its minimum, around the minimum, with linear interpolation between bins.
def width_hz(v, f):
    m = int(np.argmin(v)); h = v[m] / 2
    lo = m
    while lo > 0 and v[lo - 1] < h:
        lo -= 1
    hi = m
    while hi < len(v) - 1 and v[hi + 1] < h:
        hi += 1
    left = f[lo] if lo == 0 else f[lo - 1] + (h - v[lo - 1]) / (v[lo] - v[lo - 1]) * (f[lo] - f[lo - 1])
    right = f[hi] if hi == len(v) - 1 else f[hi] + (h - v[hi]) / (v[hi + 1] - v[hi]) * (f[hi + 1] - f[hi])
    return right - left
whz = {s: round(width_hz(low.loc[s].values.astype(float), FREQS[FREQS <= 46].astype(float)), 1) for s in SUBJECTS}
fewest_hz = sorted(whz, key=lambda s: whz[s])[:3]
print("    width in Hz (interpolated):", whz, "\\n    three narrowest:", fewest_hz,
      "; S04 and S08 among them:", "04" in fewest_hz and "08" in fewest_hz)
print("Parts holding:", int(p1.all())'''
assert old in s; s=s.replace(old,new)
s += '''

# %% tags=sanity
# How much the assumed reading of the bad-segment rule matters: the main ECoG numbers with only
# the segments with missing samples dropped (no 0 dB or 115-125 Hz rule).
E_alt = ev[ev.ok & ~ev.bad_missing]
print("events:", len(E_alt), "against", len(E))
for band in ["lfb", "hfb"]:
    col = f"roi_band:precentral:{band}_mean"
    h, p = stats.kruskal(*[g[col].values for _, g in E_alt.groupby("subject")])
    ins = sum(TABLE1[s][0 if band == "lfb" else 1][0] <= E_alt[E_alt.subject == s][col].mean() <= TABLE1[s][0 if band == "lfb" else 1][1]
              for s in SUBJECTS)
    sig = [s for s in SUBJECTS if stats.kruskal(*[d[col].values for _, d in E_alt[E_alt.subject == s].groupby("day")])[1] < 0.05]
    print(f"{band.upper()}: across subjects p = {p:.3g}; Table 1 means inside {ins} of 12; day effects in {sig}")
'''
open('nb_src.py','w').write(s)
EOF
echo ok
```

```
Sat Nov  7 04:07:36 UTC 2026
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n "claim:\|blocked\|sanity\|def check" tools/entry.py | head -60; python tools/entry.py --help 2>&1 | head -20
```

```
21:- each notebook has a cell tagged `sanity` that prints what was loaded;
143:def check(entry_dir: Path) -> Report:
196:        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
197:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
273:            report.error(where, f"claim {claim!r} has no outcome; give every claim one, blocked included")
284:            # A claim on data in another archive names where they are, so it is never blocked for missing data,
288:                if outcome.get("blocked_by") == "data_missing":
292:                if outcome.get("outcome") != "blocked" and not attempt.get("inputs"):
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES]
                {lock,check,run,all,handover} entry [entry ...]

Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,60p tools/entry.py; sed -n 143,420p tools/entry.py
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
[... 318 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && . dev/bin/activate && cd entries/000055-peterson-2021 && python -c "
import sys; sys.path.insert(0,'/tmp/claude-1001'); import nbtools; nbtools.run('/tmp/claude-1001/nb_src.py')" 2>&1 | grep -A3 "width in Hz\|Parts holding\|cell 37" ; date -u
```

```
width in Hz (interpolated): {'01': np.float64(25.8), '02': np.float64(24.7), '03': np.float64(17.2), '04': np.float64(14.4), '05': np.float64(16.9), '06': np.float64(19.2), '07': np.float64(17.3), '08': np.float64(9.4), '09': np.float64(19.7), '10': np.float64(18.0), '11': np.float64(16.8), '12': np.float64(19.5)} 
    three narrowest: ['08', '04', '11'] ; S04 and S08 among them: True
Parts holding: 4 of 4

######## cell 31 ['claim:fig5-band-power-differs-across-subjects']
band mean, LFB: Kruskal-Wallis H = 796.1, p = 1.31e-163, n = 7888 events in 12 subjects
--
######## cell 37 ['sanity']
events: 7963 against 7888
LFB: across subjects p = 1.46e-165; Table 1 means inside 12 of 12; day effects in ['03', '05', '06', '07', '08', '11']
HFB: across subjects p = 7.68e-263; Table 1 means inside 10 of 12; day effects in ['03', '04', '07', '08', '10']
Sat Nov  7 04:09:10 UTC 2026
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && cat > results.py <<'EOF'
R = {
"subject-days": "**Result: reproduced.** The dataset's subjects 01 to 12 have exactly the days of Table 2 (55 subject-days), so the subjects are matched by number.",
"roi-projection-link": "**Result: reproduced.** For all 12 subjects the projection matrix has one row per electrode of the NWB file (S01 has four extra all-zero rows at the end, dropped by the code's rule), the all-zero rows of S03 and S12 fall on depth electrode groups (LAD and LPD; AID), and the region with the largest weight is the region with the nearest centroid for 0.59 to 0.79 of electrodes, against 0.16 to 0.26 with the electrode order shuffled; the Spearman correlation of weight with proximity is 0.92 to 0.94. The regions with mean density above 3 are the eight of the claims file.",
"cohort": "**Result: partially reproduced.** 12 subjects, a mean of 84.8 surface electrodes (87.0 +- 12.9), a mean of 23.7 depth electrodes in the subjects that have them (23.2 +- 12.1) and 5 right-hemisphere subjects match. Seven subjects have electrode groups described as depth in the files, where the paper says five. Sex and age are not in the dataset, so those two values are not testable.",
"fig2-event-counts": "**Result: not reproduced.** The dataset holds 211 to 996 events per subject (median 770.5); after dropping segments with missing samples, below 0 dB or with high 115-125 Hz power, 211 to 989 (median 764). The fewest (211 against 151 +- 15.1) and the median (against 640 +- 64) are outside tolerance under both readings; the most is within. The files hold 8088 events, where the data descriptor states 6931, and no event is marked as a false positive.",
"fig2-features-differ-across-subjects": "**Result: reproduced.** All ten Kruskal-Wallis tests across subjects give p < 0.001 under both event sets (largest p 9.9e-35).",
"fig2-reach-shape": "**Result: partially reproduced.** More than half of the reaches last under 2 s and cover under 200 pixels pooled (0.918 and 0.915) and in all 12 subjects. The angle part does not hold: the two highest maxima of the angle density lie at -71.5 and 75.0 degrees pooled and within 15 degrees of +-90 in no subject, and the density at 0 is not below both peaks in 7 of 12 subjects; 23% of reaches lie within 30 degrees of horizontal.",
"fig2-bimanual-skew": "**Result: reproduced.** The median bimanual ratio is below 0.5 and the overlap skewness positive pooled and in all 12 subjects, the class is bimanual for more than half of the events pooled (0.725) and in all 12, and S02, S04 and S05 are among the five subjects with the highest median ratio and among the five with the lowest overlap skewness, under both event sets.",
"extfig2-1c-contralateral-larger": "**Result: reproduced.** The peak of the median contralateral displacement exceeds the ipsilateral one in all 12 subjects under both readings of the rest position (ratios 1.12 to 37.8 under reading a, 1.08 to 42.0 under reading b). In S04 and S05 the two are close (ratios 1.08 to 1.32).",
"extfig2-2-feature-correlations": "**Result: partially reproduced.** Five of the six correlations are within tolerance (0.604, 0.503, 0.502, 0.494, 0.599); reach magnitude and duration give r = 0.233, just below the tolerance of 0.26 +- 0.026, under both event sets (0.231 with all events).",
"fig2-days-and-waking": "**Result: partially reproduced.** One day holds more than half of the events for S05 (0.605) and S09 (0.517) and for no other subject, but not for S04, whose busiest day holds 0.379. More than half of the events fall at 08 to 24 h in all 12 subjects (0.641 to 0.964), so the waking part holds.",
"fig3-group-lfb-decrease-hfb-increase": "**Result: reproduced.** After masking, the mean over 4-30 Hz is negative and over 50-120 Hz positive in precentral (-0.885 and 0.496 dB), postcentral (-0.890, 0.507) and inferior parietal (-0.663, 0.277) over 0 to 0.5 s, and also at the time bin of onset (reading b). Middle frontal and supramarginal show the same pattern.",
"fig3-sensorimotor-largest": "**Result: reproduced.** Under all three readings, postcentral, precentral and inferior parietal are the three regions with the largest mean absolute masked power, and the three temporal regions are below all of them (for example reading a: 0.523, 0.512, 0.336 dB against at most 0.039 for the temporal regions).",
"fig3-lfb-more-widespread": "**Result: blocked (methods underspecified).** The two readings disagree. Reading a counts 7 regions with low-frequency decreases and 7 with high-frequency increases (no difference); reading b gives 35.2 significant low-frequency bins per frequency against 25.9 high-frequency (low-frequency larger). Supramarginal and superior temporal both have significant 4-30 Hz decreases (30 and 24 bins).",
"fig4-precentral-subject-variability": "**Result: reproduced.** All four parts hold: every subject has a negative LFB and positive HFB mean in precentral; S03, S06, S07, S08 and S11 are positive at 116 and 121 Hz; S09 and S12 peak at 66 Hz with the 101-121 Hz mean below half the peak; S08 has the narrowest decrease (2 bins, 9.4 Hz). S04 ties with S03, S05 and S07 at 3 bins; by the interpolated width S04 is second narrowest (14.4 Hz), so it is among the three.",
"fig5-band-power-differs-across-subjects": "**Result: reproduced.** Kruskal-Wallis across the 12 subjects gives p = 1.3e-163 (LFB) and 7.1e-264 (HFB) with the band mean, and p < 1e-150 with the code's median.",
"table1-subject-band-power-ci": "**Result: partially reproduced.** With the mean over events of the band mean, 23 of 24 subject and band values lie inside the paper's intervals; S06 HFB is 1.78 dB against 2.02 to 2.37. The other readings give 20 to 21 of 24. LFB is below baseline and HFB above it in all 12 subjects.",
"fig5-recording-day-effects": "**Result: reproduced.** With the band mean, the Kruskal-Wallis tests across days agree with the paper on all 24 subject and band pairs (the 11 significant pairs and the 13 others); with the code's band median, 23 of 24 (LFB S05 gives p = 0.088).",
"extfig5-1-baseline-reduces-day-variability": "**Result: reproduced.** The SD across days is lower with baseline subtraction for 9 of 12 subjects in LFB and 12 of 12 in HFB (reading a) and for 0.918 and 0.901 of good electrodes (reading b). Variability remains: 11 subject and band pairs have significant day effects after baseline subtraction (median SD with baseline 0.20 and 0.14 dB in the precentral region).",
"discussion-day-changes-small": "**Result: reproduced.** The largest deviation of a day mean from the subject mean is 1.01 dB (the range of day means reaches 1.80 dB), and the power without baseline subtraction is 12.4 to 36.3 dB with the data in microvolts, inside 9 to 55 dB; in volts it would be -107.5 to -83.7 dB.",
"fig6-r2-at-most-025": "**Result: blocked (too large).** One model takes the time printed above; the 2192 models of the main analysis alone exceed the notebook limit of 60 minutes on this machine, before the variants the claims ask for. The six regression claims are blocked for this reason.",
}
EOF
python - <<'EOF'
import re
exec(open('/tmp/claude-1001/results.py').read())
s=open('/tmp/claude-1001/nb_src.py').read()
for cid,text in R.items():
    tag=f"# %% tags=claim:{cid}\n"
    i=s.index(tag)
    # next section header after this tag
    j=s.find("\n# %% [markdown]\n# ## ", i)
    k=s.find("\n# %% tags=sanity\n# How much", i)
    if k!=-1 and (j==-1 or k<j): j=k
    block="\n# %% [markdown]\n# "+text+"\n"
    if j==-1: s=s+block
    else: s=s[:j]+"\n"+block+s[j:]
open('/tmp/claude-1001/nb_src.py','w').write(s)
EOF
grep -c "Result:" /tmp/claude-1001/nb_src.py
```

```
20
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && python - <<'EOF'
s=open('nb_src.py').read()
old="The angle part does not hold: the two highest maxima of the angle density lie at -71.5 and 75.0 degrees pooled and within 15 degrees of +-90 in no subject, and the density at 0 is not below both peaks in 7 of 12 subjects; 23% of reaches lie within 30 degrees of horizontal."
new="The angle part does not hold: the two highest maxima of the angle density lie at -71.5 and 75.0 degrees pooled, and within 15 degrees of +-90 in no subject (S02 and S04 have a single maximum, and in S03, S06 and S07 the density at 0 exceeds the lower peak); 22.9% of reaches lie within 30 degrees of horizontal. The density is a kernel estimate cut at +-90, which pulls maxima near the ends inward."
assert old in s; s=s.replace(old,new)
open('nb_src.py','w').write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && python - <<'EOF'
s=open('nb_src.py').read()
s=s.replace(" The density is a kernel estimate cut at +-90, which pulls maxima near the ends inward.","")
header='''# **Paper.** Peterson SM, Singh SH, Wang NXR, Rao RPN, Brunton BW (2021). Behavioral and neural
# variability of naturalistic arm movements. *eNeuro* 8(3), ENEURO.0007-21.2021.
# [doi:10.1523/ENEURO.0007-21.2021](https://doi.org/10.1523/ENEURO.0007-21.2021). The claims file was
# written from the version of record in Europe PMC (PMC8225404): main text, Methods, legends, Tables 1
# and 2 and the legends of the Extended Data figures.
#
# **Dataset.** [DANDI:000055](https://dandiarchive.org/dandiset/000055/0.220127.0436) (AJILE12),
# version 0.220127.0436. The paper cites no DANDI version: its data statement points to the curated
# epochs on Figshare, and the dandiset was published later. This is the only published version, and
# the draft lists the same 55 files with the same total size, so the published version is pinned.
# The files are streamed; nothing is downloaded.
#
# **What the dataset holds.** 12 subjects and 55 subject-days of preprocessed ECoG (500 Hz), pose of
# nine key points (30 frames per second), 8088 contralateral wrist movement events with the paper's
# ten features, coarse behaviour labels, and an electrode table with MNI positions, a `good` flag and
# the paper's regression R2 per electrode. Sex and age are not in it.
#
# **Outside input.** The projection of electrodes onto the eight AAL regions is the paper's own
# output on Figshare ([doi:10.6084/m9.figshare.12114408.v1](https://doi.org/10.6084/m9.figshare.12114408.v1)),
# used for the region claims (`data: with_inputs`) and checked by the link claim `roi-projection-link`.
#
# **Event sets.** Reading a is every event in the files. Reading b drops ECoG segments with missing
# samples, with power below 0 dB or with 115-125 Hz power more than 3 SD above the subject's segments
# (Methods); the summary of segment power these tests use is an assumption (helper docstring). The
# false positives the paper removed are not marked in the files, so they cannot be dropped.
#
# | Claim | Tested here |
# |---|---|
# | subject-days, roi-projection-link (link claims) | tested |
# | cohort, fig2-event-counts, fig2-features-differ-across-subjects, fig2-reach-shape, fig2-bimanual-skew | tested |
# | extfig2-1c-contralateral-larger, extfig2-2-feature-correlations, fig2-days-and-waking | tested |
# | fig3-group-lfb-decrease-hfb-increase, fig3-sensorimotor-largest, fig3-lfb-more-widespread | tested (the last blocked: its readings disagree) |
# | fig4-precentral-subject-variability, fig5-band-power-differs-across-subjects, table1-subject-band-power-ci | tested |
# | fig5-recording-day-effects, extfig5-1-baseline-reduces-day-variability, discussion-day-changes-small | tested |
# | fig6b-best-models-sensorimotor, fig6-r2-at-most-025, fig6c-angle-and-day-most-informative, extfig6-2-angle-most-retained, fig6d-upward-reaches-enhance-pattern, fig6d-angle-and-day-largest-coefficients | blocked, too large (timed below) |
#
# The notebook reads about 8000 ECoG segments of 10 s from 55 files of 8 to 20 GB each; that step takes
# about half an hour.'''
s=s.replace("# HEADER", header)
s+='''

# %% [markdown]
# ## Summary
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
# and the differences from the paper's method.
#
# | Claim | Outcome |
# |---|---|
# | subject-days (link) | reproduced |
# | roi-projection-link (link, Figshare projection matrices) | reproduced |
# | cohort | partially reproduced (seven subjects with depth electrodes, not five; sex and age not in the dataset) |
# | fig2-event-counts | not reproduced (211 to 996 events per subject, median 770.5) |
# | fig2-features-differ-across-subjects | reproduced |
# | fig2-reach-shape | partially reproduced (angle peaks near +-70, not +-90) |
# | fig2-bimanual-skew | reproduced |
# | extfig2-1c-contralateral-larger | reproduced |
# | extfig2-2-feature-correlations | partially reproduced (5 of 6) |
# | fig2-days-and-waking | partially reproduced (S04's busiest day holds 38%) |
# | fig3-group-lfb-decrease-hfb-increase | reproduced |
# | fig3-sensorimotor-largest | reproduced |
# | fig3-lfb-more-widespread | blocked, methods underspecified (readings disagree) |
# | fig4-precentral-subject-variability | reproduced (one tie broken by interpolated width) |
# | fig5-band-power-differs-across-subjects | reproduced |
# | table1-subject-band-power-ci | partially reproduced (23 of 24) |
# | fig5-recording-day-effects | reproduced (24 of 24) |
# | extfig5-1-baseline-reduces-day-variability | reproduced |
# | discussion-day-changes-small | reproduced |
# | six regression claims (Figure 6, Extended Data Figure 6-2) | blocked, too large |
#
# **How the analysis differs from the paper's.** The paper's preprocessing, event pruning and visual
# removal of false positives were done before the data were deposited; the dataset holds 8088 events and
# marks none as false positives, so all are kept. The bad-segment rules use an assumed summary of
# segment power; with only segments with missing samples dropped, the ECoG outcomes are unchanged
# (last data check above). Region power uses the paper's Figshare projection matrices, not a new
# projection from the AAL atlas. Bad electrodes are those of each subject's first file. The Morlet
# transform is computed by FFT and matches MNE's direct convolution. The regression claims were not run.
#
# **What was found about the dataset.** (1) In three files (S01 day 7, S04 day 3, S06 day 3) the ECoG
# covers only the end of the day but its `starting_time` is 0, while the event table and pose use a
# clock from midnight; the ECoG must be shifted by 8.1 to 8.5 h, as `ReachEvents` and the neural
# response show. (2) The files hold 8088 events; the data descriptor states 6931 verified events, and
# the paper's counts per subject are lower than the files'. (3) The reach angle is stored in image
# coordinates (upward negative) and unfolded, without saying so. (4) The pose is labelled meters but
# is in pixels. (5) `session_start_time` gives midnight UTC labelled as 19:00 at UTC-5. (6) Bimanual
# overlap is described as a fraction but reaches 3.83 (it is in seconds). (7) 124 event segments contain
# missing ECoG samples. (8) Sex and age are not recorded. (9) Seven subjects have electrode groups
# described as depth, where the paper says five.
'''
open('nb_src.py','w').write(s)
EOF
grep -n "fig6-r2" /tmp/claude-1001/nb_src.py | head
```

```
38:# | fig6b-best-models-sensorimotor, fig6-r2-at-most-025, fig6c-angle-and-day-most-informative, extfig6-2-angle-most-retained, fig6d-upward-reaches-enhance-pattern, fig6d-angle-and-day-largest-coefficients | blocked, too large (timed below) |
1019:# %% tags=claim:fig6-r2-at-most-025
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001 && sed -i 's/marks none as false positives, so all are kept. The bad-segment rules use an assumed summary of\n//' nb_src.py && python - <<'EOF'
s=open('/tmp/claude-1001/nb_src.py').read()
old="""# segment power; with only segments with missing samples dropped, the ECoG outcomes are unchanged
# (last data check above)."""
new="""# segment power; with only segments with missing samples dropped, the across-subject tests, the day
# effects and the Table 1 outcome (22 of 24 inside) do not change (last data check above)."""
assert old in s; s=s.replace(old,new); open('/tmp/claude-1001/nb_src.py','w').write(s)
EOF
E=entries/000055-peterson-2021
cat > $E/requirements.in <<'EOF'
h5py
matplotlib
mne
numpy
pandas
remfile
requests
scikit-learn
scipy
statsmodels
EOF
cat > $E/entry.yaml <<'EOF'
schema_version: 1
name: 000055-peterson-2021
type: reproduction
title: Behavioral and neural variability of naturalistic arm movements (Peterson et al. 2021)
description: Tests the findings of Peterson, Singh, Wang, Rao and Brunton (2021) on dandiset 000055
  (AJILE12), which holds 55 days of ECoG and pose from 12 people in clinical epilepsy monitoring, with
  their wrist movement events and event features. It compares the behavioural features across
  subjects and days, the group and per-subject movement-related spectral power in eight cortical
  regions, and the variation of precentral band power across subjects and recording days. The
  regression models of Figure 6 were too large to run here.
license: Apache-2.0
notebooks:
- path: reproduce_peterson_2021.ipynb
  title: Reproducing Peterson et al. (2021) from dandiset 000055
  runtime_minutes: 35
helpers:
- ajile.py
related:
- id: dandi:000055/0.220127.0436
  relation: uses_data
- id: doi:10.1523/eneuro.0007-21.2021
  relation: reproduces
EOF
cd /tmp/claude-1001 && . dev/bin/activate && python nbtools.py build nb_src.py $E/reproduce_peterson_2021.ipynb && cd  && python tools/entry.py lock entries/000055-peterson-2021 && ls entries/000055-peterson-2021; date -u
```

```
wrote entries/000055-peterson-2021/requirements.lock.txt
__pycache__
ajile.py
entry.yaml
reproduce_peterson_2021.ipynb
requirements.in
requirements.lock.txt
Sat Nov  7 04:10:26 UTC 2026
```

**Agent calls Bash**

```bash
rm -rf entries/000055-peterson-2021/__pycache__; python -c "
import json;s=json.load(open('schemas/claims.schema.json'));c=s['properties']['claims']['items'];print(json.dumps(c,indent=0)[:3000])"; grep -n "kind: link" -A12 claims/001453/*.yaml | head -30
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
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import re,yaml
p='claims/000055/10.1523-eneuro.0007-21.2021.yaml'
s=open(p).read()
link='''- id: roi-projection-link
  kind: link
  statement: The rows of the paper's projection matrices from electrodes to the eight regions,
    deposited on Figshare, can be matched one to one to the dataset's electrodes, and their weights
    fit the electrodes' positions.
  source: Methods, Projecting power into regions of interest; Figshare item 12114408 version 1
    (aal_XX_elecs2ROI.csv and aal_XX_ROIcentroids_Lside.csv)
  data: with_inputs
  criterion: Added by the author (protocol, author step 4). Rows are matched to the electrodes of
    each subject's NWB file by order, as the paper's code (load_project_spectral_power) applies them
    to its power files; where a file has more rows than electrodes, the code's rule (drop all-zero
    rows) is used. The link holds (reproduced) when for all 12 subjects the rows used equal the
    electrodes in number, and the region with the largest weight is the region whose centroid
    (aal_XX_ROIcentroids_Lside.csv) is nearest the electrode's mirrored MNI position for more
    electrodes than with the electrode order shuffled (200 shuffles). Partially reproduced when this
    holds for 9 to 11 subjects. The eight regions with mean density above 3 are also checked against
    those the claims file names.
'''
anchor='- id: cohort\n'
assert anchor in s and 'roi-projection-link' not in s
s=s.replace(anchor, link+anchor,1)
targets=['fig3-group-lfb-decrease-hfb-increase','fig3-sensorimotor-largest','fig3-lfb-more-widespread','fig4-precentral-subject-variability','fig5-band-power-differs-across-subjects','table1-subject-band-power-ci','fig5-recording-day-effects','extfig5-1-baseline-reduces-day-variability','discussion-day-changes-small','fig6b-best-models-sensorimotor','extfig6-2-angle-most-retained']
for t in targets:
    i=s.index(f'- id: {t}\n'); j=s.find('\n- id: ',i+5); j=len(s) if j==-1 else j
    if s.find('\nchecks:',i)!=-1 and s.find('\nchecks:',i)<j: j=s.find('\nchecks:',i)
    block=s[i:j]
    if '  depends_on:\n' in block:
        k=block.index('  depends_on:\n')+len('  depends_on:\n')
        while block[k:].startswith('  - '):
            k=block.index('\n',k)+1
        block=block[:k]+'  - roi-projection-link\n'+block[k:]
    else:
        assert '  data: with_inputs\n' in block, t
        block=block.replace('  data: with_inputs\n','  data: with_inputs\n  depends_on:\n  - roi-projection-link\n',1)
    s=s[:i]+block+s[j:]
open(p,'w').write(s)
d=yaml.safe_load(s)
for c in d['claims']: print(c['id'], c.get('data','dataset'), c.get('depends_on'))
EOF
```

```
subject-days dataset None
roi-projection-link with_inputs None
cohort dataset None
fig2-event-counts dataset None
fig2-features-differ-across-subjects dataset None
fig2-reach-shape dataset None
fig2-bimanual-skew dataset None
extfig2-1c-contralateral-larger dataset None
extfig2-2-feature-correlations dataset None
fig2-days-and-waking dataset None
fig3-group-lfb-decrease-hfb-increase with_inputs ['roi-projection-link']
fig3-sensorimotor-largest with_inputs ['fig3-group-lfb-decrease-hfb-increase', 'roi-projection-link']
fig3-lfb-more-widespread with_inputs ['fig3-group-lfb-decrease-hfb-increase', 'roi-projection-link']
fig4-precentral-subject-variability with_inputs ['roi-projection-link']
fig5-band-power-differs-across-subjects with_inputs ['roi-projection-link']
table1-subject-band-power-ci with_inputs ['roi-projection-link']
fig5-recording-day-effects with_inputs ['roi-projection-link']
extfig5-1-baseline-reduces-day-variability with_inputs ['fig5-recording-day-effects', 'roi-projection-link']
discussion-day-changes-small with_inputs ['roi-projection-link']
fig6b-best-models-sensorimotor with_inputs ['roi-projection-link']
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required')); print(list(s['properties'].keys()))
o=s['properties']['outcomes']['items']; print(o.get('required'), list(o['properties'].keys()))
print(json.dumps(s['properties']['provenance'],indent=0)[:1500]); print(json.dumps(s['properties']['inputs'],indent=0)[:600]); print(json.dumps(s['properties']['findings']['items'],indent=0)[:1200])"
```

```
['schema_version', 'id', 'dataset', 'paper', 'date', 'provenance', 'outcomes']
['schema_version', 'id', 'dataset', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
['claim', 'outcome'] ['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'proposed']
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
[... 118 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/000055-peterson-2021-01.yaml",
 "content": "schema_version: 2\nid: 000055-peterson-2021-01\ndataset:\n  archive: dandi\n  id: \"000055\"\n  version: 0.220127.0436\n  doi: 10.48324/dandi.000055/0.220127.0436\npaper: doi:10.1523/eneuro.0007-21.2021\ndate: 2026-11-07\nentry: 000055-peterson-2021\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-13\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/42333071861\ninputs:\n- what: The paper's projection matrices from electrodes to AAL regions (aal_XX_elecs2ROI.csv, first\n    row the electrode density, then one row per electrode) and the region centroids\n    (aal_XX_ROIcentroids_Lside.csv), for the 12 subjects, from Figshare item 12114408 version 1,\n    \"ROI projection matrices and labels\". Used for every claim on regions and checked by claim\n    roi-projection-link.\n  source: doi:10.6084/m9.figshare.12114408.v1\n- what: The paper's analysis code, read for method details (config.py, tfr_utils.py,\n    compute_spectral_power.py, regression_utils.py and the notebooks of Figures 3 to 5); no code or\n    data from it is run.\n  source: https://github.com/BruntonUWBio/naturalistic_arm_movements_ecog at commit\n    04c6faf2f219586fa834d10c614ef48a694cec55\noutcomes:\n- claim: subject-days\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:subject-days\n  notes: The dataset's subjects 01 to 12 have exactly the days of Table 2, 55 subject-days in all, so\n    subjects are matched by number. No two files share event times or wrist traces.\n- claim: roi-projection-link\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:roi-projection-link\n  notes: For all 12 subjects the rows used equal the electrodes of the NWB file. S01's matrix has 98\n    rows for 94 electrodes; the last four are all zero and are dropped by the code's rule. The\n    all-zero rows of S03 (16) and S12 (8) fall on whole depth groups (LAD and LPD; AID). The region\n    with the largest weight is the one with the nearest centroid for 0.587 to 0.786 of electrodes,\n    against 0.163 to 0.258 with the electrode order shuffled, in all 12 subjects; the Spearman\n    correlation of weight with proximity is 0.916 to 0.937. The regions with mean density above 3\n    are the eight the claims file names.\n  deviations:\n  - This link claim was written by the author during the attempt (protocol, author step 4), after\n    the electrode and row counts had been listed.\n- claim: cohort\n  outcome: partially_reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:cohort\n  measured:\n  - 12\n  - null\n  - null\n  - 84.8\n  - 7\n  - 23.7\n  - 5\n  notes: 12 subjects, a mean of 84.8 surface electrodes (SD 11.6; 87.0 +- 12.9), a mean of 23.7 depth\n    electrodes in the subjects with depth electrodes (23.2 +- 12.1) and 5 subjects implanted in the\n    right hemisphere (judged by the wrist of the events, which agrees with the sign of the mean MNI\n    x) match. Seven subjects (S01, S02, S03, S09, S10, S11, S12) have electrode groups whose\n    description says depth, where the paper says five. Sex and age are not in the files or the\n    archive's metadata and are not testable.\n  deviations:\n  - Depth electrodes are those in groups whose description in the file contains \"depth\"; the paper's\n    per-subject table (Extended Data Figure 1-1) could not be read.\n- claim: fig2-event-counts\n  outcome: not_reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig2-event-counts\n  measured:\n  - 211\n  - 996\n  - 770.5\n  notes: Reading a (all events) gives 211 to 996 events per subject, median 770.5; reading b (bad\n    segments dropped) 211 to 989, median 764. The most is within tolerance under both; the fewest\n    (against 151 +- 15.1) and the median (against 640 +- 64) are not. The files hold 8088 events and\n    the data descriptor of the dataset states 6931 verified events. No event is marked as a false\n    positive, and the paper removed 17.8% of events as false positives or occlusions, so the dataset\n    likely holds events the paper dropped.\n  deviations:\n  - The false-positive removal of reading b cannot be applied, as the files do not mark false\n    positives.\n  - The bad-segment rule of reading b uses an assumed summary of segment power (see\n    fig3-group-lfb-decrease-hfb-increase); here it drops 1 segment below 0 dB, 74 with high 115-125\n    Hz power and 124 with missing samples.\n- claim: fig2-features-differ-across-subjects\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig2-features-differ-across-subjects\n  notes: All ten Kruskal-Wallis tests across the 12 subjects give p < 0.001 under reading b (7888\n    events) and reading a (8088); the largest p is 9.9e-35 (reach duration).\n  deviations:\n  - Reach angle is the files' angle negated and folded onto -90 to 90 degrees. The files store the\n    angle in image coordinates (it matches the wrist trace to a median of 1.46 degrees, and to 116.58\n    degrees when negated), and the code negates it and folds 90-270 degrees. Time of day is in hours\n    from the files' midnight clock.\n- claim: fig2-reach-shape\n  outcome: partially_reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig2-reach-shape\n  notes: Duration and magnitude part holds. Pooled, 0.918 of reaches last under 2 s and 0.915 cover\n    under 200 pixels, and both shares exceed one half in all 12 subjects (lowest 0.881 and 0.591,\n    S08 for magnitude). Angle part does not hold. The two highest maxima of the angle density lie at\n    -71.5 and 75.0 degrees pooled and within 15 degrees of +-90 in no subject; S02 and S04 have a\n    single maximum, and in S03, S06 and S07 the density at 0 exceeds the lower peak. 22.9% of reaches\n    lie within 30 degrees of horizontal. Reading a gives the same.\n  deviations:\n  - Angle convention as in fig2-features-differ-across-subjects.\n- claim: fig2-bimanual-skew\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig2-bimanual-skew\n  notes: The median bimanual ratio is below 0.5 (pooled 0.136) and the overlap skewness positive\n    (pooled 1.114) in all 12 subjects; the class is bimanual for 0.725 of events pooled and more than\n    half in all 12 (lowest 0.507, S12). The five highest median ratios are S04, S07, S05, S02, S03 and\n    the five lowest overlap skewness S07, S05, S02, S03, S04, so S02, S04 and S05 are in both. Reading\n    a gives the same.\n  deviations:\n  - Bimanual ratio has no missing values in the files (26 events are exactly 0.5), so the code's\n    fill of 0.5 changes nothing.\n- claim: extfig2-1c-contralateral-larger\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:extfig2-1c-contralateral-larger\n  notes: The peak over 0 to 1.5 s of the median contralateral displacement exceeds the ipsilateral\n    one in all 12 subjects under reading a (rest position the mean over -1.5 to -1 s; ratios 1.12 to\n    37.81, median 4.3) and reading b (position at onset; ratios 1.08 to 42.01, median 5.83). The\n    margin is small for S04 (1.12 and 1.32) and S05 (1.15 and 1.08), so \"substantially\" holds for\n    10 of 12 subjects if read as a ratio above 1.5.\n- claim: extfig2-2-feature-correlations\n  outcome: partially_reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:extfig2-2-feature-correlations\n  measured:\n  - 0.233\n  - 0.604\n  - 0.503\n  - 0.502\n  - 0.494\n  - 0.599\n  notes: Five of six pooled Pearson correlations are within tolerance under reading b; reach\n    magnitude and duration give 0.233 against 0.26 +- 0.026 (lower bound 0.234). Reading a gives\n    0.231, 0.609, 0.505, 0.501, 0.494 and 0.598, also five of six.\n- claim: fig2-days-and-waking\n  outcome: partially_reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig2-days-and-waking\n  notes: The busiest day holds more than half of the events for S05 (0.605) and S09 (0.517) and for\n    none of the other subjects, but S04's busiest day holds 0.379, so the day part does not hold as\n    written. More than half of each subject's events fall at 08 to 24 h (0.641 to 0.964), so the\n    waking part holds. Reading a gives the same.\n  deviations:\n  - The hour of an event is taken from the files' clock, which starts at midnight; the Sleep/rest\n    labels fall mostly in its first hours (0.545 of them at 0 to 8 h).\n- claim: fig3-group-lfb-decrease-hfb-increase\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig3-group-lfb-decrease-hfb-increase\n  assumed: true\n  notes: After the bootstrap mask, the mean over 4-30 Hz and 0 to 0.5 s is negative and over 50-120\n    Hz positive in precentral (-0.885 and 0.496 dB), postcentral (-0.890 and 0.507) and inferior\n    parietal (-0.663 and 0.277), and also at the onset time bin (-0.748 and 0.460, -0.742 and 0.477,\n    -0.592 and 0.278). Middle frontal and supramarginal show the same pattern over 0 to 0.5 s.\n  deviations:\n  - Region power uses the paper's projection matrices from Figshare (claim roi-projection-link), not a\n    new projection from the AAL atlas.\n  - The bad electrodes are those of each subject's first file, as the code takes them; the files'\n    good flags differ between days for every subject.\n  - Assumed reading of the bad-segment rule (Methods, \"discarding segments with power <0 dB or with\n    abnormally high power at 115-125 Hz (>3 SDs) compared with all segments\"). The paper's\n    preprocessing code is not published. The segment's Welch power density in microvolts squared per\n    Hz is averaged over 1-200 Hz (or 115-125 Hz), converted to dB and averaged over good electrodes;\n    the 3 SD limit is taken over the subject's segments. Averaging the log density instead would drop\n    7931 of 8087 segments, so that reading is not usable. Segments with missing samples are dropped\n    (Methods, \"segments with missing data\").\n  - The bootstrap mask covers -4.5 to 4.5 s (the 10 s segment less the code's 0.5 s pad), so the FDR\n    correction runs over 25 x 91 bins per region; the paper's power files may span a different time\n    range.\n  - ECoG times in three files (S01 day 7, S04 day 3, S06 day 3) are shifted by 29241 to 30682 s, the\n    ECoG missing at the start of the day (see findings).\n- claim: fig3-sensorimotor-largest\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig3-sensorimotor-largest\n  assumed: true\n  notes: Under readings a, b and c postcentral, precentral and inferior parietal are the three\n    largest regions and the temporal regions are below all three. Reading a gives 0.523, 0.512 and\n    0.336 dB, then middle frontal 0.236, supramarginal 0.093 and the temporal regions at most 0.039.\n  deviations:\n  - As for fig3-group-lfb-decrease-hfb-increase.\n- claim: fig3-lfb-more-widespread\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig3-lfb-more-widespread\n  notes: The criterion's two readings disagree, and the criterion blocks the claim when they do.\n    Reading a counts 7 regions with a significant 4-30 Hz decrease and 7 with a significant 50-120 Hz\n    increase over 0 to 0.5 s, so low frequencies are not more widespread. Reading b gives 35.2\n    significant decreasing bins per low frequency against 25.9 increasing bins per high frequency,\n    so they are. Supramarginal (30 bins) and superior temporal (24 bins) both have significant\n    low-frequency decreases; superior temporal has no significant high-frequency increase. Question\n    for the paper's authors. How was \"more spatially widespread\" judged, as the number of regions\n    with any significant change or as the extent of significant time-frequency bins? The Results\n    sentence (Intracortical spectral power, paragraph 2) and Figure 3 give no measure; with region\n    counts the two bands tie here at 7 of 8.\n- claim: fig4-precentral-subject-variability\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig4-precentral-subject-variability\n  assumed: true\n  notes: All four parts hold. (1) Every subject has a negative 8-32 Hz mean and a positive 76-100 Hz\n    mean in precentral over 0 to 0.5 s. (2) S03, S06, S07, S08 and S11 are positive at 116 and 121\n    Hz. (3) S09 and S12 both peak at 66 Hz among 56-121 Hz, with the 101-121 Hz mean (0.05 and 0.045\n    dB) below half the peak (0.373 and 0.289). (4) S08 has the narrowest decrease (2 bins); S03, S04,\n    S05 and S07 tie at 3 bins for the next places, and by the interpolated width S08 (9.4 Hz), S04\n    (14.4 Hz) and S11 (16.8 Hz) are the three narrowest.\n  deviations:\n  - The bin count of part 4 ties four subjects for the second and third places. The tie is broken by\n    the width in Hz of the run below half the minimum, interpolated between bins, a finer form of the\n    same measure; the paper and its code give no rule. Under the bin count with the tie read against\n    S04, part 4 fails and the claim would be partially reproduced.\n  - As for fig3-group-lfb-decrease-hfb-increase.\n- claim: fig5-band-power-differs-across-subjects\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig5-band-power-differs-across-subjects\n  notes: Kruskal-Wallis across the 12 subjects (7888 events) gives p = 1.31e-163 for LFB and 7.06e-264\n    for HFB with the band mean, and 9.09e-165 and 7.79e-258 with the code's band median. With only\n    segments with missing samples dropped (7963 events), p = 1.46e-165 and 7.68e-263.\n  deviations:\n  - As for fig3-group-lfb-decrease-hfb-increase, except that the outcome does not depend on the\n    assumed bad-segment rule.\n- claim: table1-subject-band-power-ci\n  outcome: partially_reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:table1-subject-band-power-ci\n  notes: Under the reading mean over events of the band mean, 23 of 24 subject and band values lie\n    inside the paper's intervals; S06 HFB is 1.782 dB against 2.02 to 2.37 (the bootstrap interval\n    here is 1.64 to 1.92). The other readings give 21 (median of band mean), 21 (mean of band median)\n    and 20 (median of band median) of 24. LFB is below baseline and HFB above it in all 12 subjects.\n    With only segments with missing samples dropped, 22 of 24 (LFB 12, HFB 10).\n  deviations:\n  - As for fig3-group-lfb-decrease-hfb-increase; the outcome does not depend on the assumed\n    bad-segment rule.\n- claim: fig5-recording-day-effects\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig5-recording-day-effects\n  notes: With the band mean, the per-subject Kruskal-Wallis tests across days agree with the paper on\n    all 24 subject and band pairs, the 11 the paper names significant (largest p 0.0331, HFB S07) and\n    the 13 others not (smallest p 0.068, HFB S01). With the code's band median, 23 of 24 agree; LFB\n    S05 gives p = 0.088. With only segments with missing samples dropped, the same 11 pairs are\n    significant.\n  deviations:\n  - As for fig5-band-power-differs-across-subjects.\n- claim: extfig5-1-baseline-reduces-day-variability\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:extfig5-1-baseline-reduces-day-variability\n  assumed: true\n  notes: Reading a (precentral region per subject), the SD across days of the day means is lower\n    with baseline subtraction for 9 of 12 subjects in LFB (median 0.202 against 0.865 dB) and 12 of\n    12 in HFB (0.140 against 0.480 dB). Reading b (per good electrode), for 1006 of 1096 electrodes\n    in LFB and 988 of 1096 in HFB. Variability remains, as 11 subject and band pairs have significant\n    day effects after baseline subtraction (fig5-recording-day-effects).\n  deviations:\n  - As for fig3-group-lfb-decrease-hfb-increase. Power without baseline is the 10*log10 band power\n    with no subtraction, with the data in microvolts.\n- claim: discussion-day-changes-small\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:discussion-day-changes-small\n  assumed: true\n  notes: The largest deviation of a day mean from the subject's mean precentral band power is 1.011 dB\n    (S03 LFB), within 2.2 dB; the range of day means, the other reading the claims file mentions,\n    reaches 1.801 dB. Without baseline subtraction the mean band power is 12.4 to 36.3 dB with the\n    data in microvolts, inside 9 to 55 dB; in volts it would be -107.5 to -83.7 dB.\n  deviations:\n  - As for fig3-group-lfb-decrease-hfb-increase. The files store microvolts (conversion 1e-6 to\n    volts), and the level part holds with that unit.\n- claim: fig6b-best-models-sensorimotor\n  outcome: blocked\n  blocked_by: too_large\n  notes: The regression of the claims file (forward selection, then 200 day-balanced splits with a\n    Huber fit of the full model and a refit per selected feature) is needed for each of 1096 good\n    electrodes and 2 bands. One model (S07, one electrode, LFB, 784 events, 8 features selected) took\n    about 8 s here (printed in the notebook), so the main analysis alone is about 4.7 h on one core\n    and 1.2 h on the 4 cores of the runner, over the 60 minute notebook limit before the three\n    variants the claims ask for and after the 27 minutes of ECoG reading. Not run.\n- claim: fig6-r2-at-most-025\n  outcome: blocked\n  blocked_by: too_large\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig6-r2-at-most-025\n  notes: Blocked as fig6b-best-models-sensorimotor; the notebook times one model and prints the\n    estimate. For reference only, the files' electrode tables hold a regression R2 per electrode\n    (low_freq_R2, high_freq_R2) with largest values 0.149 and 0.255; these are stored results, not\n    computed here, and decide nothing.\n- claim: fig6c-angle-and-day-most-informative\n  outcome: blocked\n  blocked_by: too_large\n  notes: Blocked as fig6b-best-models-sensorimotor.\n- claim: extfig6-2-angle-most-retained\n  outcome: blocked\n  blocked_by: too_large\n  notes: Blocked as fig6b-best-models-sensorimotor.\n- claim: fig6d-upward-reaches-enhance-pattern\n  outcome: blocked\n  blocked_by: too_large\n  notes: Blocked as fig6b-best-models-sensorimotor.\n- claim: fig6d-angle-and-day-largest-coefficients\n  outcome: blocked\n  blocked_by: too_large\n  notes: Blocked as fig6b-best-models-sensorimotor.\nfindings:\n- kind: metadata_error\n  statement: In three files (sub-01 ses-7, sub-04 ses-3, sub-06 ses-3) the ECoG holds 15.5 to 15.9 h\n    and its starting_time is 0, while the reaches table and the pose run on a clock from midnight.\n    The ECoG starts 29241 to 30682 s after midnight, the time missing from 24 h; ReachEvents and the\n    session start time agree, and the movement response appears only with this shift (S06 day 3,\n    precentral HFB +1.98 dB with it, -0.07 dB without). Read with starting_time as given, the event\n    times point at the wrong ECoG or past its end.\n- kind: other\n  statement: The files hold 8088 wrist movement events (211 to 996 per subject), where the data\n    descriptor states 6931 verified events and the paper reports 151 to 947 per subject (median 640).\n    No event is marked as a false positive or as removed, so the events the paper analysed cannot be\n    selected.\n- kind: metadata_insufficient\n  statement: Reach_angle_degrees is described only as \"Reach angle in degrees\". It holds the angle of\n    the reach in image coordinates (y down, -180 to 180), so upward reaches are negative, while the\n    paper's feature is the negated angle folded to -90 to 90.\n- kind: metadata_error\n  statement: Pose positions are labelled meters but hold pixels (the data descriptor gives pixels; the\n    values span hundreds).\n- kind: metadata_error\n  statement: Bimanual_overlap is described as a fraction of the contralateral movement duration, but\n    1708 of 8088 values exceed 1 (up to 3.83); it behaves as seconds.\n- kind: metadata_error\n  statement: session_start_time is 19:00 at UTC-5 for files that start at local midnight (midnight UTC\n    written in another zone), and 03:07 to 03:31 at UTC-5 for the three files whose ECoG starts later.\n- kind: other\n  statement: 124 of the event segments contain missing (NaN) ECoG samples on every electrode, in 30 of\n    55 files.\n- kind: data_missing\n  statement: The subjects' sex and age, which the paper reports, are not in the files or the archive's\n    metadata.\n- kind: paper_inconsistency\n  statement: Seven subjects have electrode groups described as depth in the files (S01, S02, S03, S09,\n    S10, S11, S12), where the paper says five subjects had depth electrodes.\n- kind: metadata_insufficient\n  statement: The electrode `good` flags differ between a subject's files, and nothing says which list\n    the paper used; the paper's code takes the list of each subject's first file.\n- kind: methods_unavailable\n  statement: The paper's rule for bad ECoG segments (\"power <0 dB or with abnormally high power at\n    115-125 Hz (>3 SDs) compared with all segments\") does not say how a segment's power is\n    summarised, in which unit, or whether the SD is over a subject's or all segments, and the\n    preprocessing code is not published. Question for the authors. Was the 0 dB test applied to the\n    log of the mean power density over frequencies and electrodes in microvolts squared, as assumed\n    here? The mean of the log density is below 0 dB for nearly every segment.\n- kind: methods_unavailable\n  statement: The paper does not say how it judged low-frequency decreases \"more spatially widespread\"\n    than high-frequency increases (Results, Intracortical spectral power, paragraph 2). Question for\n    the authors. Was it the number of regions with significant changes or the extent of significant\n    bins? The two give different answers here.\n"
}
```

```
File created successfully at: attempts/000055-peterson-2021-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s['properties']['outcomes']['items']['properties']['measured'],indent=0))"; grep -n ": .*: " attempts/000055-peterson-2021-01.yaml | grep -v "^\s*[0-9]*:\s*- " | head
```

```
{
"description": "The values obtained, for claims with expected values: one number, or one per expected value, in the same order.",
"oneOf": [
{
"type": "number"
},
{
"type": "array",
"minItems": 1,
"items": {
"type": "number"
}
}
]
}
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/000055-peterson-2021-01.yaml'; s=open(p).read()
old='''  measured:
  - 12
  - null
  - null
  - 84.8
  - 7
  - 23.7
  - 5
  notes: 12 subjects'''
assert old in s; s=s.replace(old,'''  notes: No value is recorded under measured, as two of the seven expected values (male subjects,
    mean age) cannot be measured. 12 subjects''')
open(p,'w').write(s)
EOF
cat > entries/000055-peterson-2021/README.md <<'EOF'
# Peterson, Singh, Wang, Rao & Brunton (2021) from dandiset 000055

Tests the findings of [Peterson et al. (2021)](https://doi.org/10.1523/ENEURO.0007-21.2021) on
[DANDI:000055](https://dandiarchive.org/dandiset/000055/0.220127.0436) (AJILE12), which holds 55 days
of ECoG and pose from 12 people in clinical epilepsy monitoring, with their wrist movement events and
event features. Region power uses the paper's projection matrices from
[Figshare](https://doi.org/10.6084/m9.figshare.12114408.v1).

| Claim | Outcome |
|---|---|
| Subjects and days match Table 2 (link) | Reproduced |
| The Figshare projection matrices match the dataset's electrodes (link) | Reproduced |
| Cohort and electrode counts | Partially reproduced |
| 151 to 947 events per subject, median 640 | Not reproduced |
| All ten features differ across subjects | Reproduced |
| Reach duration, magnitude and bimodal angle | Partially reproduced |
| Bimanual features skewed to unimanual | Reproduced |
| Contralateral wrist moves more than ipsilateral | Reproduced |
| Feature correlations (Extended Data Figure 2-2) | Partially reproduced |
| Events by day and in waking hours | Partially reproduced |
| Group LFB decrease and HFB increase (Figure 3) | Reproduced |
| Largest changes in sensorimotor regions | Reproduced |
| LFB decreases more widespread than HFB increases | Blocked: methods underspecified |
| Per-subject precentral spectra (Figure 4) | Reproduced |
| Band power differs across subjects (Figure 5) | Reproduced |
| Per-subject band power in Table 1 intervals | Partially reproduced |
| Band power differs across days (Figure 5, Table 2) | Reproduced |
| Baseline subtraction reduces day variability | Reproduced |
| Day changes small next to absolute power | Reproduced |
| Regression models (Figure 6, Extended Data Figure 6-2), six claims | Blocked: too large |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

In three files the ECoG starts after midnight but is stored with a start time of 0; `ajile.py`
shifts it (`ecog_offset`). The files hold 8088 events with no false positives marked, more than the
paper analysed. The notebook reads about 8000 ECoG segments and takes about half an hour. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/000055-peterson-2021-01.yaml`](../../attempts/000055-peterson-2021-01.yaml).
EOF
python tools/entry.py check entries/000055-peterson-2021; date -u
```

```
0 error(s)
Sat Nov  7 04:12:27 UTC 2026
```

**Agent calls Bash**

```bash
grep -n "add_argument" tools/entry.py
```

```
428:    parser.add_argument("command", choices=["lock", "check", "run", "all", "handover"])
429:    parser.add_argument("entry", type=Path, nargs="+",
431:    parser.add_argument("--output-dir", type=Path, help="where executed notebooks go")
432:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
433:    parser.add_argument("--max-minutes", type=float, default=60,
```

**Agent calls Bash**

```bash
python tools/entry.py all entries/000055-peterson-2021 2>&1 | tail -30; date -u
```

```
Installed kernelspec registry-000055-peterson-2021 in executed/000055-peterson-2021/.venv/share/jupyter/kernels/registry-000055-peterson-2021
0 error(s)
pass  reproduce_peterson_2021.ipynb  (1723 s)
Sat Nov  7 04:41:23 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/000055-peterson-2021 && python - <<'EOF'
import nbformat
nb=nbformat.read('reproduce_peterson_2021.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    tags=c.metadata.get('tags',[])
    out=''.join(o.get('text','') for o in c.outputs if o.output_type=='stream')
    err=[o for o in c.outputs if o.output_type=='error']
    if err: print('ERROR',tags)
    if any(t.startswith('claim:') for t in tags) or 'Segments' in out or 'ECoG segments' in out or 'one model' in out or 'events:' in out[:10] or 'S01 day 7' in out:
        lines=[l for l in out.split('\n') if any(k in l for k in ['->','reading','Result','within','All ','Agreement','inside','events','p =','largest','levels','one model','models needed','LFB:','HFB:','Within','subjects whose','top three','order','Parts','three','S0','pattern','LF larger','supramarginal','fewest','duration and','angle part','ratio part','contralateral','subjects 12','stored'])]
        print('==',tags); print('\n'.join(lines[:40]))
EOF
```

```
== []
ECoG segments of 8087 events read and reduced in 26.5 min
== []
Segments below 0 dB: 1 ; 115-125 Hz above 3 SD: 74 ; kept (reading b): 7888
Other reading of the 0 dB test (mean of the log density below 0 dB): 7931 of 8087 segments would go, so that reading is not usable
== ['sanity']
S01 day 7: offset 30682.4 s; with offset 190 events, precentral HFB +0.10 dB, LFB -1.61 dB; without offset 58 events in range, HFB -0.15 dB, LFB +0.03 dB; ReachEvents minus offset-corrected times, max |diff| 0.001 s
S04 day 3: offset 30048.3 s; with offset 35 events, precentral HFB -0.07 dB, LFB -0.31 dB; without offset 13 events in range, HFB +0.02 dB, LFB +0.48 dB; ReachEvents minus offset-corrected times, max |diff| 0.001 s
S06 day 3: offset 29240.6 s; with offset 164 events, precentral HFB +1.98 dB, LFB -1.60 dB; without offset 81 events in range, HFB -0.07 dB, LFB +0.27 dB; ReachEvents minus offset-corrected times, max |diff| 0.001 s
== ['claim:subject-days']
S01: dataset days [3, 4, 5, 7], Table 2 [3, 4, 5, 7], match True
S02: dataset days [3, 4, 5, 6], Table 2 [3, 4, 5, 6], match True
S03: dataset days [3, 4, 5, 6], Table 2 [3, 4, 5, 6], match True
S04: dataset days [3, 4, 5, 6, 7], Table 2 [3, 4, 5, 6, 7], match True
S05: dataset days [3, 4, 7], Table 2 [3, 4, 7], match True
S06: dataset days [3, 4, 5, 6, 7], Table 2 [3, 4, 5, 6, 7], match True
S07: dataset days [3, 4, 5, 6, 7], Table 2 [3, 4, 5, 6, 7], match True
S08: dataset days [3, 4, 5, 6, 7], Table 2 [3, 4, 5, 6, 7], match True
S09: dataset days [3, 4, 5, 6, 7], Table 2 [3, 4, 5, 6, 7], match True
All 12 match: True ; subject-days: 55
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && python - <<'EOF'
import nbformat
old="after dropping segments with missing samples, below 0 dB or with high 115-125 Hz power, 211 to 989 (median 764)"
new="after dropping segments with missing samples, below 0 dB or with high 115-125 Hz power, 211 to 979 (median 739)"
for p in ['entries/000055-peterson-2021/reproduce_peterson_2021.ipynb','executed/000055-peterson-2021/reproduce_peterson_2021.ipynb']:
    nb=nbformat.read(p,4); n=0
    for c in nb.cells:
        if c.cell_type=='markdown' and old in c.source:
            c.source=c.source.replace(old,new); n+=1
    nbformat.write(nb,p); print(p,n)
s=open('/tmp/claude-1001/nb_src.py').read(); s=s.replace(old,new); open('/tmp/claude-1001/nb_src.py','w').write(s)
p='attempts/000055-peterson-2021-01.yaml'; s=open(p).read()
for a,b in [("""  - 996
  - 770.5
  notes: Reading a (all events) gives 211 to 996 events per subject, median 770.5; reading b (bad
    segments dropped) 211 to 989, median 764.""","""  - 996
  - 770.5
  notes: Reading a (all events) gives 211 to 996 events per subject, median 770.5; reading b (bad
    segments dropped) 211 to 979, median 739."""),
 ("about 8 s here (printed in the notebook), so the main analysis alone is about 4.7 h on one core","8.0 s here (printed in the notebook), so the main analysis alone is about 4.9 h on one core")]:
    assert a in s, a[:40]; s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n "989\|764\|4.7 h" attempts/000055-peterson-2021-01.yaml entries/000055-peterson-2021/README.md; python tools/entry.py check entries/000055-peterson-2021; date -u
```

```
entries/000055-peterson-2021/reproduce_peterson_2021.ipynb 1
executed/000055-peterson-2021/reproduce_peterson_2021.ipynb 1
0 error(s)
Sat Nov  7 04:41:47 UTC 2026
```

**Agent calls Bash**

```bash
python tools/entry.py handover entries/000055-peterson-2021 && ls executed/000055-peterson-2021/handover; git status --short | head -20
```

```
wrote executed/000055-peterson-2021/handover
10.1523-eneuro.0007-21.2021.yaml
ajile.py
reproduce_peterson_2021.ipynb
 M claims/000055/10.1523-eneuro.0007-21.2021.yaml
 M tools/build_site.py
 M tools/runner/run_requests.py
 M tools/site_assets/app.css
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
?? attempts/000055-peterson-2021-01.yaml
?? entries/000055-peterson-2021/
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la .bashrc .bash_profile .gitconfig .mcp.json .profile .ripgreprc .zprofile .zshrc .idea .vscode scripts 2>&1 | head -20; git status --short entries/000055-peterson-2021
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 03:10 .bash_profile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 03:10 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 03:10 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 03:10 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 03:10 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 03:10 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 03:10 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 03:10 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 03:10 .zprofile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 03:10 .zshrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  7 03:10 scripts
?? entries/000055-peterson-2021/
```

**Agent calls Bash**

```bash
ls -a entries/000055-peterson-2021; rm -rf entries/000055-peterson-2021/__pycache__; python tools/entry.py check entries/000055-peterson-2021; date -u
```

```
.
..
.claude
README.md
__pycache__
ajile.py
entry.yaml
reproduce_peterson_2021.ipynb
requirements.in
requirements.lock.txt
0 error(s)
Sat Nov  7 04:42:18 UTC 2026
```

**Agent calls Bash**

```bash
ls -la entries/000055-peterson-2021/.claude; find entries/000055-peterson-2021/.claude | head
```

```
total 12
drwxr-xr-x 3 runner runner 4096 Nov  7 03:28 .
drwxr-xr-x 3 runner runner 4096 Nov  7 04:42 ..
drwx------ 2 runner runner 4096 Nov  7 03:28 .cc-writes
entries/000055-peterson-2021/.claude
entries/000055-peterson-2021/.claude/.cc-writes
```

**Agent calls Bash**

```bash
rmdir entries/000055-peterson-2021/.claude/.cc-writes entries/000055-peterson-2021/.claude 2>&1; ls -a entries/000055-peterson-2021
```

```
Permission for this tool use was denied. It requires approval, and this session has no approval surface — nobody can answer a permission prompt here — so it was denied automatically. The action was NOT performed; do not claim it succeeded, and do not retry it: this action, and anything else that requires approval, will be denied the same way for the rest of this session. Tell the user what was blocked and why you needed it, then continue with the parts of the task that do not require approval. What required approval: Claude requested permissions to edit entries/000055-peterson-2021/.claude/.cc-writes which is a sensitive file.
```

**Agent**

All five Author steps are done and the handover is built. The entry passed `tools/entry.py all` with 0 check errors, and the notebook ran from a clean environment in 1723 s (29 min). I did not verify my own work, commit or push.

**1. Outcome per claim** (pinned version 0.220127.0436: it is the only published version, the paper cites no DANDI version, and the draft lists the same 55 files with the same total size)

| Claim | Outcome |
|---|---|
| subject-days (link) | reproduced |
| roi-projection-link (link claim I added) | reproduced |
| cohort | partially reproduced |
| fig2-event-counts | not reproduced: 211 to 996 events per subject, median 770.5 |
| fig2-features-differ-across-subjects | reproduced |
| fig2-reach-shape | partially reproduced: angle peaks near ±70, not ±90 |
| fig2-bimanual-skew | reproduced |
| extfig2-1c-contralateral-larger | reproduced |
| extfig2-2-feature-correlations | partially reproduced: 5 of 6, magnitude–duration r = 0.233 against 0.26 ± 0.026 |
| fig2-days-and-waking | partially reproduced: S04's busiest day holds 38% |
| fig3-group-lfb-decrease-hfb-increase | reproduced (assumed) |
| fig3-sensorimotor-largest | reproduced (assumed) |
| fig3-lfb-more-widespread | blocked, methods_underspecified: the criterion's two readings disagree |
| fig4-precentral-subject-variability | reproduced (assumed; one tie broken) |
| fig5-band-power-differs-across-subjects | reproduced |
| table1-subject-band-power-ci | partially reproduced: 23 of 24 inside |
| fig5-recording-day-effects | reproduced: 24 of 24 agree |
| extfig5-1-baseline-reduces-day-variability | reproduced (assumed) |
| discussion-day-changes-small | reproduced (assumed) |
| The six Figure 6 and Extended Data 6-2 regression claims | blocked, too_large |

The regression claims are blocked because one model timed in the notebook took 8.0 s. The 2192 models give an estimate of 4.9 h on one core, or 1.2 h on 4 cores, before the variants the claims ask for.

**2. Dataset, assumptions, questions**

What I found about the dataset:
- **ECoG clock:** in three files (sub-01 ses-7, sub-04 ses-3, sub-06 ses-3) the ECoG covers only the end of the day but has `starting_time` 0. The events and pose use a clock that starts at midnight. Shifting the ECoG by 29241 to 30682 s fixes it, and the neural response confirms the shift.
- **Event count:** the files hold 8088 events with no false positives marked. The data descriptor says 6931, and the paper's counts per subject are lower.
- **Undocumented conventions:**
  - The reach angle is stored in image coordinates and not folded.
  - The pose is labelled meters but holds pixels.
  - Bimanual overlap is described as a fraction but reaches 3.83.
  - `session_start_time` gives midnight UTC labelled as 19:00 at UTC-5.
- **Missing values:** 124 event segments have missing (NaN) ECoG samples.
- **Subjects:** sex and age are not recorded. Seven subjects have electrode groups described as depth, where the paper says five.
- **Good flags:** the electrode `good` flags differ between days. I used each subject's first file, as the paper's code does.

Inputs: the paper's projection matrices on Figshare (doi:10.6084/m9.figshare.12114408.v1), checked by the link claim, and the paper's code at commit 04c6faf, which I only read.

Assumption: how a segment's power is summarised for the 0 dB and 3 SD rejection rules. I checked that it does not change the outcomes of the Figure 5, Table 1 and day-effect claims. I did not check that for the claims marked "assumed" in the table, so those carry `assumed: true`.

Two questions for the paper's authors are recorded as `methods_unavailable` findings:
- How was each segment's power summarised for the bad-segment rules?
- What measure decided that low-frequency decreases are "more spatially widespread"?

I asked a reader no questions.

**3. Where the protocol was unclear**
1. Step 4 says the author writes link claims but not whether that can happen after looking at the data. I wrote `roi-projection-link` after listing electrode and row counts, said so in its deviations, and added it to `depends_on` of the claims that use the Figshare matrices. I changed no statement, expected value or criterion.
2. Ties in a criterion's ranking: the protocol says to break them "as the paper implies", and here the paper implies nothing. In fig4 I broke the tie with a finer form of the same measure (interpolated width in Hz), recorded it as a deviation and gave the other result.
3. `measured` cannot hold null when some expected values cannot be measured. I left it out for cohort and explained in the notes.
4. After the run I corrected one conclusion's numbers (reading b gives 211 to 979, median 739, not 211 to 989, median 764). I edited that markdown cell in both the committed and executed notebooks, which is not re-run evidence. The protocol does not say how to handle this.

**4. Runtime and failures**

About 1 h 30 min of the 5 h (03:15 to about 04:43). Reading the ECoG segments takes 26.5 min of each notebook run, so it is close to the 60-minute limit. Nothing failed.

Two leftovers in the checkout:
- `entries/000055-peterson-2021/.claude/` is an empty folder the harness created. Removing it needed approval, which was denied automatically. Git ignores empty folders, so it should not show up in the commit.
- The untracked dotfiles at the repository root are sandbox device mounts dated 03:10, before this run. I left them alone.

## End of run

93 turns, 85 minutes, $8.25 at API prices, result: success.
