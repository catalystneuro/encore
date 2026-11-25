# peterson-2021 · author · run 45551254647

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries attempts claims paper; wc -l docs/*.md README.md
```

```
Wed Nov 25 05:12:04 UTC 2026
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
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
protocol.lock
[... 1104 more lines not kept]
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
9	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
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

**Agent calls Bash**

```bash
cat claims/peterson-2021.yaml; ls papers/datasets/ | grep peterson; cat papers/datasets/peterson-2021.yaml; ls questions | grep peterson; ls papers/author-notes 2>/dev/null | grep peterson
```

```
<persisted-output>
Output too large (46.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/f827794a-c716-4e85-a39e-d824755c2636/tool-results/bsd089gz1.txt

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/f827794a-c716-4e85-a39e-d824755c2636/tool-results/bsd089gz1.txt"
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
[... 674 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -80; sed -n '/## DANDI/,/^## [A-Z]/p' docs/archives.md
```

```
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>. The protocol the checks follow, and the `encore` command that runs the same check on your own data, are in [encore-protocol](https://github.com/encorescience/encore-protocol). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Site:** <https://encorescience.org/>, with the registry's dashboard at <https://encorescience.org/registry/> and what Encore offers a journal at <https://encorescience.org/journals/>.

## Reading the outcomes

An outcome says what one attempt could recover from the data in a dandiset,
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
ls -R entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; cat attempts/fouke-2025-01.yaml | head -150
```

```
entries/fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt
schema_version: 1
name: fouke-2025
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
[... 166 more lines not kept]
```

**Agent**

Read the protocol, claims (24 claims) and the example entry. Now surveying the dandiset.

**Agent calls Bash**

```bash
sed -n '150,400p' attempts/fouke-2025-01.yaml | grep -n -A12 '^findings' | head -40; ls schemas; python -c "import pynwb,remfile,h5py,dandi;print('ok')"
```

```
Exit code 1
95:findings:
96-- kind: data_missing
97-  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
98-    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
99-    the GitLab repository the paper names for all behavioural and imaging data holds analysis
100-    notebooks only. Nine of the paper's main findings cannot be tested.
101-- kind: metadata_insufficient
102-  statement: The stimulus codes 0 to 20 have no names or description in the files or the
103-    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
104-    file of its stimulus software.
105-- kind: code_mismatch
106-  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
107-    while its conversion of the stimulus software's names gives the reverse (it carries a remap
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
Traceback (most recent call last):
  File "<string>", line 1, in <module>
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q pynwb remfile h5py dandi numpy scipy pandas matplotlib requests 2>&1 | tail -2; python -c "import pynwb;print(pynwb.__version__)"
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000055/versions/0.261123.1703/ | python -c "import json,sys;d=json.load(sys.stdin);print(d['name']);print(d.get('description')[:3000]);print(d.get('assetsSummary'));print(d.get('doi'))"; curl -s "https://api.dandiarchive.org/api/dandisets/000055/versions/0.261123.1703/assets/?page_size=200" | python -c "import json,sys;d=json.load(sys.stdin);print(d['count']);[print(a['path'],a['size']//1e6,a['asset_id']) for a in d['results']]"
```

```
4.2.0
Shell cwd was reset to
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import h5py, remfile, requests, time, pynwb, sys
aid=sys.argv[1]
t=time.time()
url=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
f=h5py.File(remfile.File(url),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name,obj.shape,obj.dtype,obj.chunks, obj.compression, dict((k,v) for k,v in obj.attrs.items() if k in('unit','conversion','rate','resolution','description','starting_time')))
    else:
        a={k:v for k,v in obj.attrs.items() if k in ('description','neurodata_type','colnames')}
        print(name+'/',a)
f.visititems(show)
for k in ['session_start_time','session_description','identifier']: print(k,f[k][()])
for k in f['general'].keys():
    o=f['general'][k]
    if isinstance(o,h5py.Dataset): print('general',k,o[()])
if 'subject' in f['general']:
    for k,v in f['general/subject'].items(): print('subject',k,v[()])
print('time',time.time()-t)
EOF
python survey.py 35cebbe1-cbdb-4b45-a132-fed5f67b6d76 2>&1 | head -200
```

```
acquisition/ {}
acquisition/ECGL/ {'description': 'Electrooculography for tracking saccades - left', 'neurodata_type': 'TimeSeries'}
acquisition/ECGL/data (43200000,) float32 None None {'conversion': np.float64(nan), 'resolution': np.float64(-1.0), 'unit': 'V'}
acquisition/ECGL/starting_time () float64 None None {'rate': np.float32(500.0), 'unit': 'seconds'}
acquisition/ECGR/ {'description': 'Electrooculography for tracking saccades - right', 'neurodata_type': 'TimeSeries'}
acquisition/ECGR/data (43200000,) float32 None None {'conversion': np.float64(nan), 'resolution': np.float64(-1.0), 'unit': 'V'}
acquisition/ECGR/starting_time () float64 None None {'rate': np.float32(500.0), 'unit': 'seconds'}
acquisition/EOGL/ {'description': 'Electrooculography for tracking saccades - left', 'neurodata_type': 'TimeSeries'}
acquisition/EOGL/data (43200000,) float32 None None {'conversion': np.float64(nan), 'resolution': np.float64(-1.0), 'unit': 'V'}
acquisition/EOGL/starting_time () float64 None None {'rate': np.float32(500.0), 'unit': 'seconds'}
acquisition/EOGR/ {'description': 'Electrooculography for tracking saccades - right', 'neurodata_type': 'TimeSeries'}
acquisition/EOGR/data (43200000,) float32 None None {'conversion': np.float64(nan), 'resolution': np.float64(-1.0), 'unit': 'V'}
acquisition/EOGR/starting_time () float64 None None {'rate': np.float32(500.0), 'unit': 'seconds'}
acquisition/ElectricalSeries/ {'description': 'no description', 'neurodata_type': 'ElectricalSeries'}
acquisition/ElectricalSeries/data (43200000, 94) float32 (84375, 1) gzip {'conversion': np.float64(1e-06), 'resolution': np.float64(-1.0), 'unit': 'volts'}
acquisition/ElectricalSeries/electrodes (94,) int64 None None {'description': 'all electrodes'}
acquisition/ElectricalSeries/starting_time () float64 None None {'rate': np.float32(500.0), 'unit': 'seconds'}
analysis/ {}
file_create_date (1,) object None None {}
general/ {}
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; curl -s https://api.figshare.com/v2/articles/12114408 | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('title'),d.get('version'),d.get('doi'));[print(f['name'],f['size'],f['download_url']) for f in d.get('files',[])][:80]" | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > tecog.py <<'EOF'
import h5py, remfile, requests, time, numpy as np
from concurrent.futures import ThreadPoolExecutor
aid="35cebbe1-cbdb-4b45-a132-fed5f67b6d76"
url=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
t=time.time()
f=h5py.File(remfile.File(url),'r')
ds=f['acquisition/ElectricalSeries/data']
ev=f['processing/behavior/ReachEvents/timestamps'][:]
st=f['intervals/reaches/start_time'][:]
print('open',time.time()-t, ev[:5], st[:5], len(ev))
dsid=ds.id
# chunk info
n=dsid.get_num_chunks(); print('nchunks',n)
sizes=[dsid.get_chunk_info(i).size for i in range(0,n,max(1,n//200))]
print('mean chunk bytes',np.mean(sizes))
t=time.time()
x=ds[int(ev[0]*500)-1000:int(ev[0]*500)+500,:]
print('one event all ch',time.time()-t, x.shape)
# raw chunk read via byte ranges
import fsspec
EOF
python tecog.py
```

```
open 1.010176658630371 [ 1791.954  3520.224  3584.342 26884.644 27984.896] [ 1791.954  3520.224  3584.342 26884.645 27984.897] 156
nchunks 48128
mean chunk bytes 312798.1592039801
one event all ch 1.2299296855926514 (1500, 94)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd paper; wc -c *.txt; grep -n -i -E "^#|Materials and Methods|synchroniz|0 dB|115|baseline|Morlet|wavelet|regression|Huber|withheld|forward|day-balanced|90%|split|false positive|pixel|onset speed|reach duration|time of day|waking|kurtosis" 10.1523-eneuro.0007-21.2021.txt | head -120
```

```
<persisted-output>
Output too large (101.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/f827794a-c716-4e85-a39e-d824755c2636/tool-results/bdol89oy1.txt

Preview (first 2KB):
153224 10.1523-eneuro.0007-21.2021.txt
7:2821 eneuro eNeuro eNeuro Society for Neuroscience PMC8225404 8225404 8225404 34031100 10.1523/ENEURO.0007-21.2021 Behavioral and Neural Variability of Naturalistic Arm Movements Peterson Steven M 1 2 ✉ Singh Satpreet H 3 Wang Nancy X R 4 5 Rao Rajesh P N 3 5 6 Brunton Bingni W 1 2 1 Department of Biology, University of Washington, Seattle, Washington 98195 2 eScience Institute, University of Washington, Seattle, Washington 98195 3 Department of Electrical & Computer Engineering, University of Washington, Seattle, Washington 98195 4 IBM Research, San Jose, California 95120 5 Paul G. Allen School of Computer Science and Engineering, University of Washington, Seattle, Washington 98195 6 Center for Neurotechnology, University of Washington, Seattle, Washington 98195 The authors declare no competing financial interests. Author contributions: N.X.R.W., R.P.N.R., and B.W.B. designed research; S.M.P. and S.H.S. performed research; S.M.P. and S.H.S. contributed unpublished reagents/analytic tools; S.M.P., S.H.S., R.P.N.R., and B.W.B. analyzed data; S.M.P. and B.W.B. wrote the paper. This research was supported by Defense Advanced Research Projects Agency Grant FA8750-18-2-0259, National Science Foundation Grants 1630178 and EEC-1028725, the Sloan Foundation, the Washington Research Foundation, and the Weill Neurohub. * S.M.P. and S.H.S. contributed equally to this work. ✉ Correspondence should be addressed to Steven M. Peterson at [removed: an e-mail address] . ✉ Corresponding author. 19 6 2021 8 3 ENEURO.0007-21.2021 ENEURO.0007-21.2021 25 6 2021 Copyright © 2021 Peterson et al. This is an open-access article distributed under the terms of the Creative Commons Attribution 4.0 International license , which permits u
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && python3 - <<'EOF'
t=open('paper/10.1523-eneuro.0007-21.2021.txt').read()
i=t.find('Materials and Methods')
j=t.find('Results',i+2000)
print(len(t),i,j)
print(t[i:i+26000])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
mkdir -p entries/peterson-2021 && cd $TMPDIR && . dev/bin/activate && cat > meta.py <<'EOF'
import h5py, remfile, requests, time, numpy as np, pandas as pd, pickle
from concurrent.futures import ThreadPoolExecutor
V="0.261123.1703"
r=requests.get(f"https://api.dandiarchive.org/api/dandisets/000055/versions/{V}/assets/?page_size=200").json()['results']
def one(a):
    url=requests.head(f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/",allow_redirects=True).url
    f=h5py.File(remfile.File(url),'r')
    e=f['general/extracellular_ephys/electrodes']
    el=pd.DataFrame({k:e[k][:] for k in e.keys() if k not in('group',)})
    rt=f['intervals/reaches']; re_=pd.DataFrame({k:rt[k][:] for k in rt.keys()})
    ep=f['intervals/epochs']; epd=pd.DataFrame({k:ep[k][:] for k in ep.keys()})
    out=dict(path=a['path'],sub=f['general/subject/subject_id'][()],age=f['general/subject/age'][()],sex=f['general/subject/sex'][()],ses=f['general/session_id'][()],
      start=f['session_start_time'][()],el=el,reaches=re_,epochs=epd,evts=f['processing/behavior/ReachEvents/timestamps'][:],evdesc=f['processing/behavior/ReachEvents'].attrs['description'],
      ecog_shape=f['acquisition/ElectricalSeries/data'].shape, es_el=f['acquisition/ElectricalSeries/electrodes'][:],
      pose_shape=f['processing/behavior/Position/R_Wrist/data'].shape)
    return out
t=time.time()
with ThreadPoolExecutor(12) as ex: res=list(ex.map(one,r))
print(time.time()-t)
pickle.dump(res,open('meta.pkl','wb'))
EOF
python meta.py
```

```
69.97146916389465
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle, pandas as pd, numpy as np
pd.set_option('display.width',250); pd.set_option('display.max_columns',30)
res=sorted(pickle.load(open('meta.pkl','rb')),key=lambda d:d['path'])
for d in res:
    el=d['el']; r=d['reaches']
    print(d['path'].split('/')[1], d['sub'],d['ses'],d['age'],d['sex'],d['start'],d['ecog_shape'],d['pose_shape'],len(el),len(r),len(d['evts']),d['evdesc'], 'good',el.good.sum(), sorted(set(el.group_name.astype(str))) if d['ses']==b'3' else '', 'epochs',len(d['epochs']))
d=res[0]
print(d['el'].head(10)); print(d['el'].describe())
print(d['reaches'].head(10)); print(d['reaches'].describe())
print(d['epochs'].head(10)); print(d['epochs'].labels.value_counts())
print(d['es_el'][:10])
EOF
```

```
sub-01_ses-3_behavior+ecephys.nwb b'01' b'3' b'P44Y' b'M' b'2000-01-03T00:00:00+00:00' (43200000, 94) (2592000, 2) 94 156 156 r_wrist good 85 ['GRID', 'LAT', 'LID', 'LMT', 'LPT', 'LTO'] epochs 1427
sub-01_ses-4_behavior+ecephys.nwb b'01' b'4' b'P44Y' b'M' b'2000-01-04T00:00:00+00:00' (43200000, 94) (2592000, 2) 94 196 196 r_wrist good 91  epochs 1431
sub-01_ses-5_behavior+ecephys.nwb b'01' b'5' b'P44Y' b'M' b'2000-01-05T00:00:00+00:00' (43200000, 94) (2592000, 2) 94 199 199 r_wrist good 91  epochs 1431
sub-01_ses-7_behavior+ecephys.nwb b'01' b'7' b'P44Y' b'M' b'2000-01-07T00:00:00+00:00' (27858793, 94) (2592000, 2) 94 190 190 r_wrist good 91  epochs 920
sub-02_ses-3_behavior+ecephys.nwb b'02' b'3' b'P20Y' b'M' b'2000-01-03T00:00:00+00:00' (43200000, 86) (2592000, 2) 86 51 51 l_wrist good 85 ['GRID', 'RDA', 'RDP', 'RST'] epochs 1435
sub-02_ses-4_behavior+ecephys.nwb b'02' b'4' b'P20Y' b'M' b'2000-01-04T00:00:00+00:00' (43200000, 86) (2592000, 2) 86 94 94 l_wrist good 85  epochs 1431
sub-02_ses-5_behavior+ecephys.nwb b'02' b'5' b'P20Y' b'M' b'2000-01-05T00:00:00+00:00' (43200000, 86) (2592000, 2) 86 82 82 l_wrist good 81  epochs 1431
sub-02_ses-6_behavior+ecephys.nwb b'02' b'6' b'P20Y' b'M' b'2000-01-06T00:00:00+00:00' (43200000, 86) (2592000, 2) 86 78 78 l_wrist good 80  epochs 1435
sub-03_ses-3_behavior+ecephys.nwb b'03' b'3' b'P33Y' b'M' b'2000-01-03T00:00:00+00:00' (43200000, 96) (2592000, 2) 96 198 198 r_wrist good 79 ['GRID', 'LAD', 'LAT', 'LMT', 'LPD'] epochs 1427
sub-03_ses-4_behavior+ecephys.nwb b'03' b'4' b'P33Y' b'M' b'2000-01-04T00:00:00+00:00' (43200000, 96) (2592000, 2) 96 193 193 r_wrist good 71  epochs 1413
sub-03_ses-5_behavior+ecephys.nwb b'03' b'5' b'P33Y' b'M' b'2000-01-05T00:00:00+00:00' (43200000, 96) (2592000, 2) 96 137 137 r_wrist good 76  epochs 479
sub-03_ses-6_behavior+ecephys.nwb b'03' b'6' b'P33Y' b'M' b'2000-01-06T00:00:00+00:00' (43200000, 96) (2592000, 2) 96 114 114 r_wrist good 79  epochs 928
sub-04_ses-3_behavior+ecephys.nwb b'04' b'3
[... 112 more lines not kept]
```

**Agent**

Subjects and days match the paper's Table 2 exactly. Now building the ECoG chunk fetcher and timing it, since the spectral claims depend on whether ~200 GB of streaming is feasible.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q mne scikit-learn 2>&1|tail -1; cat > tchunk.py <<'EOF'
import h5py, remfile, requests, time, numpy as np, zlib
from concurrent.futures import ThreadPoolExecutor
aid="35cebbe1-cbdb-4b45-a132-fed5f67b6d76"
url=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
f=h5py.File(remfile.File(url),'r')
ds=f['acquisition/ElectricalSeries/data']
print(ds.id.get_create_plist().get_nfilters(), [ds.id.get_create_plist().get_filter(i)[:2] for i in range(ds.id.get_create_plist().get_nfilters())])
t=time.time()
info=[]
def cb(ci): info.append((ci.chunk_offset, ci.byte_offset, ci.size))
ds.id.chunk_iter(cb)
print('chunk_iter',time.time()-t,len(info))
EOF
python tchunk.py
```

```
1 [(1, 1)]
chunk_iter 113.04141926765442 48128
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > tchunk2.py <<'EOF'
import h5py, remfile, requests, time, numpy as np, zlib
from concurrent.futures import ThreadPoolExecutor
aid="35cebbe1-cbdb-4b45-a132-fed5f67b6d76"
url=requests.head(f"https://api.dandiarchive.org/api/assets/{aid}/download/",allow_redirects=True).url
f=h5py.File(remfile.File(url),'r')
ds=f['acquisition/ElectricalSeries/data']; nch=ds.shape[1]; CH=ds.chunks[0]
ev=f['processing/behavior/ReachEvents/timestamps'][:]
t=time.time()
need=set()
for e in ev:
    s=int(round((e-5)*500)); en=s+5000
    for c in range(s//CH,(en-1)//CH+1): need.add(c)
need=sorted(need); print('time chunks',len(need),'of',ds.shape[0]//CH)
offs={}
for c in need:
    for ch in range(nch):
        ci=ds.id.get_chunk_info_by_coord((c*CH,ch)); offs[(c,ch)]=(ci.byte_offset,ci.size)
print('chunk info',time.time()-t, len(offs))
sess=requests.Session()
ad=requests.adapters.HTTPAdapter(pool_connections=64,pool_maxsize=64); sess.mount('https://',ad)
def get(k):
    o,s=offs[k]
    r=sess.get(url,headers={'Range':f'bytes={o}-{o+s-1}'})
    return k,np.frombuffer(zlib.decompress(r.content),dtype='<f4')
t=time.time()
keys=list(offs)[:94*40]
with ThreadPoolExecutor(48) as ex: out=list(ex.map(get,keys))
dt=time.time()-t
print('fetched',len(keys),dt, sum(offs[k][1] for k in keys)/dt/1e6,'MB/s')
# verify against h5py
k,a=out[5]; c,ch=k
print(np.allclose(a, ds[c*CH:(c+1)*CH, ch]))
EOF
python tchunk2.py
```

```
time chunks 94 of 512
chunk info 100.39037370681763 8836
fetched 3760 10.37520694732666 112.00926534766026 MB/s
True
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pandas as pd, requests, io, pickle, numpy as np
res=sorted(pickle.load(open('meta.pkl','rb')),key=lambda d:d['path'])
nel={}
for d in res: nel[int(d['sub'])]=len(d['el'])
for s,(a,b) in {1:(22276662,22276665),5:(22276686,22276689),9:(22276710,22276713)}.items():
    m=pd.read_csv(io.StringIO(requests.get(f'https://ndownloader.figshare.com/files/{a}').text),header=None)
    c=pd.read_csv(io.StringIO(requests.get(f'https://ndownloader.figshare.com/files/{b}').text),header=None)
    print(s,m.shape,nel[s],(m.sum(1)==0).sum()); print(m.iloc[:3,:8]); print(c.head(3), c.shape)
EOF
```

```
<stdin>:8: Pandas4Warning: Starting with pandas version 4.0 all arguments of sum will be keyword-only.
<stdin>:8: Pandas4Warning: Starting with pandas version 4.0 all arguments of sum will be keyword-only.
<stdin>:8: Pandas4Warning: Starting with pandas version 4.0 all arguments of sum will be keyword-only.
1 (100, 116) 94 0
              0             1  ...              6              7
0  Precentral_L  Precentral_R  ...  Frontal_Mid_L  Frontal_Mid_R
1        4.7166    1.9466e-15  ...         3.8951     5.0465e-15
2    0.00031939    1.6774e-10  ...        0.17785        0.13995

[3 rows x 8 columns]
       0      1      2
0      x      y      z
1  -39.2  -6.92  50.36
2      0      0      0 (117, 3)
5 (108, 116) 106 0
              0             1  ...              6              7
0  Precentral_L  Precentral_R  ...  Frontal_Mid_L  Frontal_Mid_R
1         3.544    7.0807e-15  ...         3.1207     1.7627e-07
2    9.4946e-07      0.018858  ...     2.8934e-15     1.6442e-23

[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python - <<'EOF'
import numpy as np, time
from sklearn.linear_model import HuberRegressor
rng=np.random.default_rng(0)
X=rng.standard_normal((700,14)); y=X[:,0]*0.3+rng.standard_normal(700)
t=time.time()
for i in range(100): HuberRegressor().fit(X[:630],y[:630])
print((time.time()-t)/100)
X=X[:,:5]
t=time.time()
for i in range(100): HuberRegressor().fit(X[:630],y[:630])
print((time.time()-t)/100)
EOF
date -u
```

```
0.0016575002670288087
0.0014220356941223144
Wed Nov 25 05:25:06 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle, pandas as pd, numpy as np
res=sorted(pickle.load(open('meta.pkl','rb')),key=lambda d:d['path'])
from collections import defaultdict
g=defaultdict(list)
for d in res: g[d['sub']].append(d)
for s,L in g.items():
    G=np.array([d['el'].good.values for d in L])
    gn=L[0]['el'].group_name.astype(str).values
    same=all((d['el'][['x','y','z']].values==L[0]['el'][['x','y','z']].values).all() for d in L)
    r2same=all(np.allclose(d['el'].low_freq_R2.values,L[0]['el'].low_freq_R2.values,equal_nan=True) for d in L)
    print(s, G.shape, 'bad any',(~G).any(0).sum(),'bad all',(~G).all(0).sum(), 'per-ses bad',(~G).sum(1), 'xyz same',same,'R2 same',r2same, 'x mean',L[0]['el'].x.mean().round(1), dict(zip(*np.unique(gn,return_counts=True))))
    rr=pd.concat([d['reaches'] for d in L]); print('   nan', rr.isna().sum().to_dict())
EOF
```

```
b'01' (4, 94) bad any 9 bad all 3 per-ses bad [9 3 3 3] xyz same True R2 same True x mean -53.7 {'GRID': np.int64(64), 'LAT': np.int64(6), 'LID': np.int64(8), 'LMT': np.int64(4), 'LPT': np.int64(6), 'LTO': np.int64(6)}
   nan {'Bimanual_class': 0, 'Bimanual_overlap': 0, 'Bimanual_ratio': 0, 'Onset_speed_px_per_sec': 0, 'Reach_angle_degrees': 0, 'Reach_magnitude_px': 0, 'Speech_ratio': 0, 'id': 0, 'start_time': 0, 'stop_time': 0}
b'02' (4, 86) bad any 7 bad all 1 per-ses bad [1 1 5 6] xyz same True R2 same True x mean 54.5 {'GRID': np.int64(64), 'RDA': np.int64(8), 'RDP': np.int64(8), 'RST': np.int64(6)}
   nan {'Bimanual_class': 0, 'Bimanual_overlap': 0, 'Bimanual_ratio': 0, 'Onset_speed_px_per_sec': 0, 'Reach_angle_degrees': 0, 'Reach_magnitude_px': 0, 'Speech_ratio': 0, 'id': 0, 'start_time': 0, 'stop_time': 0}
b'03' (4, 96) bad any 27 bad all 17 per-ses bad [17 25 20 17] xyz same False R2 same True x mean -49.3 {'GRID': np.int64(64), 'LAD': np.int64(8), 'LAT': np.int64(8), 'LMT': np.int64(8), 'LPD': np.int64(8)}
   nan {'Bimanual_class': 0, 'Bimanual_overlap': 0, 'Bimanual_ratio': 0, 'Onset_speed_px_per_sec': 0, 'Reach_angle_degrees': 0, 'Reach_magnitude_px': 0, 'Speech_ratio': 0, 'id': 0, 'start_time': 0, 'stop_time': 0}
b'04' (5, 84) bad any 26 bad all 1 per-ses bad [17  4  3  2  7] xyz same True R2 same True x mean 49.0 {'GRID': np.int64(64), 'RAT': np.int64(6), 'RMT': np.int64(6), 'RPT': np.int64(8)}
   nan {'Bimanual_class': 0, 'Bimanual_overlap': 0, 'Bimanual_ratio': 0, 'Onset_speed_px_per_sec': 0, 'Reach_angle_degrees': 0, 'Reach_magnitude_px': 0, 'Speech_ratio': 0, 'id': 0, 'start_time': 0, 'stop_time': 0}
b'05' (3, 106) bad any 7 bad all 1 per-ses bad [2 2 6] xyz same True R2 same True x mean 53.9 {'GRID': np.int64(64), 'RAT': np.int64(6), 'RF': np.int64(16), 'RMT': np.int64(6), 'RPT': np.int64(8), 'RTP': np.int64(6)}
   nan {'Bimanual_class': 0, 'Bimanual_overlap': 0, 'Bimanual_ratio': 0, 'Onset_speed_px_per_sec': 0, 'Reach_angle_degrees': 0, 'Reach_mag
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle, numpy as np
res=sorted(pickle.load(open('meta.pkl','rb')),key=lambda d:d['path'])
for s in [b'03',b'12']:
    L=[d for d in res if d['sub']==s]
    A=[d['el'][['x','y','z']].values for d in L]
    for i,a in enumerate(A[1:]):
        dif=np.abs(a-A[0]); print(s,i+1,np.nanmax(dif), np.isnan(a).sum(), np.isnan(A[0]).sum(), (dif>1e-6).any(1).sum())
EOF
```

```
b'03' 1 0.0 48 48 0
b'03' 2 0.0 48 48 0
b'03' 3 0.0 48 48 0
b'12' 1 0.0 24 24 0
b'12' 2 0.0 24 24 0
b'12' 3 0.0 24 24 0
b'12' 4 0.0 24 24 0
Shell cwd was reset to
```

**Agent**

Positions are NaN for 16 electrodes of S03 and 8 of S12; good flags vary by day. Writing the helper.

**Agent calls Write**

```json
{
 "file_path": "entries/peterson-2021/ajile.py",
 "content": "\"\"\"Loading and measures for Peterson et al. (2021) on DANDI:000055 (AJILE12).\n\nEverything is streamed from the archive at a pinned version; nothing is written to disk.\n\nWhere each parameter comes from:\n\n- Spectral method (claims file, opening comment, from the paper's Methods and code): Morlet\n  wavelet power at 1 to 121 Hz in 5 Hz steps with n_cycles = frequency / 4, MNE's wavelet\n  definition (sigma_t = n_cycles / (2 pi f), support of 5 sigma_t on each side, normalised;\n  zero_mean False, the MNE 0.19 default of the code), decimated by 50 samples (10 Hz bins at\n  500 Hz) aligned on the event, 10*log10 power. Because n_cycles / f is the same at every\n  frequency, every wavelet spans +-0.2 s, so power is computed only at the time bins used here\n  (-1.5 s to +1.0 s around onset); this gives the same values as convolving the whole 10 s\n  segment.\n- Baseline: each event's mean over the bins -1.5 to -1 s (inclusive) is subtracted, per\n  electrode and frequency (claims file).\n- Band power: bins 0 to 0.5 s (inclusive), LFB 11-31 Hz bins, HFB 76-96 Hz bins (claims file).\n  The band mean (Methods) and the band median (code: median over time, then over frequency)\n  are both returned.\n- Segment rejection (Methods, \"ECoG-event synchronization and segmentation\": \"discarding\n  segments with power <0 dB or with abnormally high power at 115-125 Hz (>3 SDs) compared with\n  all segments\"). The paper does not say how power is pooled over electrodes and\n  frequencies. Assumption: Welch PSD (1 s Hann windows) of the 10 s segment centred on the\n  event, averaged over the session's good electrodes; the segment's power is 10*log10 of the\n  mean PSD over 1-200 Hz, and its high-frequency power 10*log10 of the mean over 115-125 Hz,\n  compared with the mean + 3 SD over all of the subject's segments. Segments that run past the\n  ends of the recording, or that hold exact zeros on every electrode (the preprocessing zeroes\n  artifacts and breaks), count as missing data.\n- Good electrodes: the `good` column of each session's electrodes table (Methods: bad\n  electrodes removed). It differs between sessions of a subject; each event uses the flags of\n  its own session (assumption, stated in the notebook).\n- Region projection (claims file; Methods \"Projecting power into regions of interest\"): the\n  paper's own projection matrices from Figshare item 12114408 v1, rows matched to the\n  electrodes by order, bad electrodes weight 0, each region's weights renormalised to sum 1.\n- Pose windows for Extended Data Figure 2-1c: -1.5 to +1.5 s around onset at 30 Hz (claims\n  file criterion: baseline -1.5 to -1 s, window 0 to 1.5 s).\n\"\"\"\n\nimport io\nimport zlib\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\n\nDANDISET = \"000055\"\nVERSION = \"0.261123.1703\"\nAPI = \"https://api.dandiarchive.org/api\"\nFIGSHARE_ITEM = 12114408  # ROI projection matrices and labels, version 1\n\nFS = 500.0\nFREQS = np.arange(1, 122, 5).astype(float)\nN_CYCLES = FREQS / 4.0\nDECIM = 50\nBIN_T = np.round(np.arange(-1.5, 1.0001, 0.1), 1)  # time bins kept, s\nBASE = (BIN_T >= -1.5) & (BIN_T <= -1.0)\nWIN = (BIN_T >= 0.0) & (BIN_T <= 0.5)\nLFB = (FREQS >= 8) & (FREQS <= 32)\nHFB = (FREQS >= 76) & (FREQS <= 100)\nSEG_HALF = 5.0  # 10 s segments centred on the event\nROIS = [\"Frontal_Mid_L\", \"Precentral_L\", \"Postcentral_L\", \"Parietal_Inf_L\",\n        \"SupraMarginal_L\", \"Temporal_Sup_L\", \"Temporal_Mid_L\", \"Temporal_Inf_L\"]\nROI_NAMES = [\"middle frontal\", \"precentral\", \"postcentral\", \"inferior parietal\",\n             \"supramarginal\", \"superior temporal\", \"middle temporal\", \"inferior temporal\"]\nFEATURES = [\"day\", \"time_of_day\", \"duration\", \"magnitude\", \"angle\", \"onset_speed\",\n            \"speech_ratio\", \"bimanual_ratio\", \"bimanual_overlap\", \"bimanual_class\"]\n\n\ndef list_assets():\n    \"\"\"Assets of the pinned version, with subject and session parsed from the path.\"\"\"\n    url = f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200\"\n    rows = []\n    while url:\n        r = requests.get(url, timeout=60).json()\n        rows += r[\"results\"]\n        url = r[\"next\"]\n    df = pd.DataFrame([{\"path\": a[\"path\"], \"asset_id\": a[\"asset_id\"], \"size\": a[\"size\"]} for a in rows])\n    df[\"subject\"] = df.path.str.extract(r\"sub-(\\d+)/\")[0].astype(int)\n    df[\"session\"] = df.path.str.extract(r\"_ses-(\\d+)_\")[0].astype(int)\n    return df.sort_values([\"subject\", \"session\"]).reset_index(drop=True)\n\n\ndef s3_url(asset_id):\n    return requests.head(f\"{API}/assets/{asset_id}/download/\", allow_redirects=True, timeout=60).url\n\n\ndef open_nwb(asset_id):\n    url = s3_url(asset_id)\n    return h5py.File(remfile.File(url), \"r\"), url\n\n\ndef _txt(v):\n    return v.decode() if isinstance(v, bytes) else v\n\n\ndef load_session_meta(asset_id):\n    \"\"\"Small datasets of one file: subject, electrodes, reaches, epochs, series shapes.\"\"\"\n    f, _ = open_nwb(asset_id)\n    e = f[\"general/extracellular_ephys/electrodes\"]\n    el = pd.DataFrame({k: e[k][:] for k in e.keys() if k != \"group\"})\n    for c in (\"group_name\", \"location\"):\n        el[c] = el[c].map(_txt)\n    rt = f[\"intervals/reaches\"]\n    reaches = pd.DataFrame({k: rt[k][:] for k in rt.keys()})\n    ep = f[\"intervals/epochs\"]\n    epochs = pd.DataFrame({k: ep[k][:] for k in ep.keys()})\n    epochs[\"labels\"] = epochs[\"labels\"].map(_txt)\n    es = f[\"acquisition/ElectricalSeries\"]\n    pos = f[\"processing/behavior/Position\"]\n    out = dict(\n        asset_id=asset_id,\n        subject_id=_txt(f[\"general/subject/subject_id\"][()]),\n        age=_txt(f[\"general/subject/age\"][()]),\n        sex=_txt(f[\"general/subject/sex\"][()]),\n        session_id=_txt(f[\"general/session_id\"][()]),\n        session_start=_txt(f[\"session_start_time\"][()]),\n        session_description=_txt(f[\"session_description\"][()]),\n        electrodes=el, reaches=reaches, epochs=epochs,\n        event_times=f[\"processing/behavior/ReachEvents/timestamps\"][:],\n        event_wrist=_txt(f[\"processing/behavior/ReachEvents\"].attrs[\"description\"]),\n        ecog_shape=es[\"data\"].shape,\n        ecog_rate=float(es[\"starting_time\"].attrs[\"rate\"]),\n        ecog_start=float(es[\"starting_time\"][()]),\n        ecog_conversion=float(es[\"data\"].attrs[\"conversion\"]),\n        ecog_unit=_txt(es[\"data\"].attrs[\"unit\"]),\n        ecog_chunks=es[\"data\"].chunks,\n        es_electrodes=es[\"electrodes\"][:],\n        pose_series=sorted(pos.keys()),\n        pose_shape=pos[\"R_Wrist/data\"].shape,\n        pose_rate=float(pos[\"R_Wrist/starting_time\"].attrs[\"rate\"]),\n        pose_start=float(pos[\"R_Wrist/starting_time\"][()]),\n        pose_unit=_txt(pos[\"R_Wrist/data\"].attrs[\"unit\"]),\n    )\n    f.close()\n    return out\n\n\ndef load_all_meta(assets, workers=12):\n    with ThreadPoolExecutor(workers) as ex:\n        return list(ex.map(load_session_meta, assets.asset_id))\n\n\ndef fold_angle(a):\n    \"\"\"Fold reach angles (degrees, -180 to 180) to -90..90 (Methods: 90-270 mapped to 90..-90).\n\n    An angle a in (90, 270) (that is, a > 90 or a < -90) becomes 180 - a, wrapped to -90..90.\n    \"\"\"\n    a = np.mod(np.asarray(a, float), 360.0)\n    out = np.where(a <= 90, a, np.where(a >= 270, a - 360, 180 - a))\n    return out\n\n\ndef event_table(metas):\n    \"\"\"One row per reach event, with the ten features of the paper.\"\"\"\n    rows = []\n    for m in metas:\n        r = m[\"reaches\"].copy()\n        r[\"subject\"] = int(m[\"subject_id\"])\n        r[\"day\"] = int(m[\"session_id\"])\n        r[\"asset_id\"] = m[\"asset_id\"]\n        r[\"ev_index\"] = np.arange(len(r))\n        rows.append(r)\n    ev = pd.concat(rows, ignore_index=True)\n    ev[\"time_of_day\"] = ev.start_time / 3600.0  # hours after midnight (session_description)\n    ev[\"duration\"] = ev.stop_time - ev.start_time\n    ev[\"magnitude\"] = ev.Reach_magnitude_px\n    ev[\"angle_raw\"] = ev.Reach_angle_degrees\n    ev[\"onset_speed\"] = ev.Onset_speed_px_per_sec\n    ev[\"speech_ratio\"] = ev.Speech_ratio\n    ev[\"bimanual_ratio\"] = ev.Bimanual_ratio.fillna(0.5)\n    ev[\"bimanual_overlap\"] = ev.Bimanual_overlap\n    ev[\"bimanual_class\"] = ev.Bimanual_class\n    return ev\n\n\n# ----------------------------------------------------------------------------- figshare inputs\n\ndef figshare_files():\n    r = requests.get(f\"https://api.figshare.com/v2/articles/{FIGSHARE_ITEM}/versions/1\", timeout=60).json()\n    return {f[\"name\"]: f[\"download_url\"] for f in r[\"files\"]}, r\n\n\ndef load_projection(subject, files):\n    \"\"\"Projection matrix (rows = electrodes in file order, columns = AAL regions) and centroids.\"\"\"\n    m = pd.read_csv(io.StringIO(requests.get(files[f\"aal_{subject:02d}_elecs2ROI.csv\"], timeout=60).text))\n    c = pd.read_csv(io.StringIO(requests.get(files[f\"aal_{subject:02d}_ROIcentroids_Lside.csv\"], timeout=60).text))\n    return m, c\n\n\n# ----------------------------------------------------------------------------- spectral\n\ndef morlet_bank():\n    \"\"\"MNE's Morlet wavelets (mne.time_frequency.morlet, zero_mean=False), one column per frequency.\"\"\"\n    sigma_t = N_CYCLES / (2.0 * np.pi * FREQS)\n    ws = []\n    for f, s in zip(FREQS, sigma_t):\n        t = np.arange(0.0, 5.0 * s, 1.0 / FS)\n        t = np.r_[-t[::-1], t[1:]]\n        w = np.exp(2j * np.pi * f * t) * np.exp(-t ** 2 / (2.0 * s ** 2))\n        w /= np.sqrt(0.5) * np.linalg.norm(w.ravel())\n        ws.append(w)\n    n = max(len(w) for w in ws)\n    bank = np.zeros((n, len(FREQS)), complex)\n    for i, w in enumerate(ws):\n        o = (n - len(w)) // 2\n        bank[o:o + len(w), i] = w\n    return bank\n\n\ndef band_stats(spec):\n    \"\"\"spec: (..., n_freq, n_bins) dB. Returns band mean and code-style median for LFB and HFB.\"\"\"\n    w = spec[..., :, WIN]\n    out = {}\n    for name, sel in ((\"lfb\", LFB), (\"hfb\", HFB)):\n        b = w[..., sel, :]\n        out[name + \"_mean\"] = b.mean(axis=(-2, -1))\n        out[name + \"_median\"] = np.median(np.median(b, axis=-1), axis=-1)\n    return out\n\n\ndef _segment_psd(seg):\n    from scipy.signal import welch\n    f, p = welch(seg, fs=FS, nperseg=int(FS), axis=-1)\n    return f, p\n\n\ndef session_spectral(asset_id, event_times, good, weights, n_threads=24, batch_chunks=6,\n                     wrist_names=(\"L_Wrist\", \"R_Wrist\")):\n    \"\"\"Spectral measures, segment checks and wrist windows for the events of one file.\n\n    good: bool (n_ch,) good electrodes of this session. weights: (n_ch, n_roi) projection\n    weights with bad electrodes already 0 and columns summing to 1.\n    Returns a dict of arrays, one row per event.\n    \"\"\"\n    f, url = open_nwb(asset_id)\n    ds = f[\"acquisition/ElectricalSeries/data\"]\n    n_t, n_ch = ds.shape\n    CH = ds.chunks[0]\n    assert ds.chunks[1] == 1\n    bank = morlet_bank()\n    half = (bank.shape[0] - 1) // 2\n    n_ev = len(event_times)\n    s0 = np.round(np.asarray(event_times) * FS).astype(int)  # event sample (series starts at 0 s)\n    seg_lo, seg_hi = s0 - int(SEG_HALF * FS), s0 + int(SEG_HALF * FS)\n    inside = (seg_lo >= 0) & (seg_hi <= n_t)\n    nb, nf, nr = len(BIN_T), len(FREQS), weights.shape[1]\n    region = np.full((n_ev, nr, nf, nb), np.nan, np.float32)\n    elec = {k: np.full((n_ev, n_ch), np.nan, np.float32) for k in\n            [\"lfb_mean\", \"hfb_mean\", \"lfb_median\", \"hfb_median\", \"lfb_mean_raw\", \"hfb_mean_raw\"]}\n    seg_db = np.full(n_ev, np.nan)\n    hf_db = np.full(n_ev, np.nan)\n    allzero = np.zeros(n_ev, bool)\n    # chunks needed\n    need = {}\n    for i in np.flatnonzero(inside):\n        for c in range(seg_lo[i] // CH, (seg_hi[i] - 1) // CH + 1):\n            need.setdefault(c, []).append(i)\n    tchunks = sorted(need)\n    sess = requests.Session()\n    sess.mount(\"https://\", requests.adapters.HTTPAdapter(pool_connections=n_threads, pool_maxsize=n_threads))\n\n    def fetch(arg):\n        c, ch, off, size = arg\n        for attempt in range(5):\n            try:\n                r = sess.get(url, headers={\"Range\": f\"bytes={off}-{off + size - 1}\"}, timeout=120)\n                r.raise_for_status()\n                return c, ch, np.frombuffer(zlib.decompress(r.content), dtype=\"<f4\")\n            except Exception:\n                if attempt == 4:\n                    raise\n    cache = {}\n    done = np.zeros(n_ev, bool)\n    bins_off = np.round(BIN_T * FS).astype(int)\n    with ThreadPoolExecutor(n_threads) as ex:\n        for b0 in range(0, len(tchunks), batch_chunks):\n            batch = tchunks[b0:b0 + batch_chunks]\n            args = []\n            for c in batch:\n                if c in cache:\n                    continue\n                for ch in range(n_ch):\n                    ci = ds.id.get_chunk_info_by_coord((c * CH, ch))\n                    args.append((c, ch, ci.byte_offset, ci.size))\n            arrs = {}\n            for c, ch, a in ex.map(fetch, args):\n                arrs.setdefault(c, [None] * n_ch)[ch] = a\n            for c, lst in arrs.items():\n                n = min(len(a) for a in lst)\n                cache[c] = np.stack([a[:n] for a in lst], axis=1)\n            # events whose chunks are all present\n            ready = [i for c in batch for i in need[c] if not done[i]\n                     and all(cc in cache for cc in range(seg_lo[i] // CH, (seg_hi[i] - 1) // CH + 1))]\n            for i in sorted(set(ready)):\n                cs = range(seg_lo[i] // CH, (seg_hi[i] - 1) // CH + 1)\n                block = np.concatenate([cache[c] for c in cs], axis=0)\n                start = cs[0] * CH\n                seg = block[seg_lo[i] - start: seg_hi[i] - start].T.astype(np.float64)  # (n_ch, 5000), uV\n                done[i] = True\n                allzero[i] = bool(np.all(seg[good] == 0, axis=0).any())\n                fr, p = _segment_psd(seg[good])\n                pm = p.mean(axis=0)\n                seg_db[i] = 10 * np.log10(pm[(fr >= 1) & (fr <= 200)].mean())\n                hf_db[i] = 10 * np.log10(pm[(fr >= 115) & (fr <= 125)].mean())\n                centre = int(SEG_HALF * FS)\n                idx = centre + bins_off[:, None] + np.arange(-half, half + 1)[None, :]  # (nb, taps)\n                win = seg[:, idx]  # (n_ch, nb, taps)\n                # convolution: flip the kernel\n                pw = np.abs(win @ bank[::-1, :]) ** 2  # (n_ch, nb, nf)\n                with np.errstate(divide=\"ignore\"):\n                    db = 10 * np.log10(pw).transpose(0, 2, 1)  # (n_ch, nf, nb)\n                bs = db - db[:, :, BASE].mean(axis=-1, keepdims=True)\n                st = band_stats(bs)\n                for k, v in st.items():\n                    elec[k][i] = v\n                raw = band_stats(db)\n                elec[\"lfb_mean_raw\"][i] = raw[\"lfb_mean\"]\n                elec[\"hfb_mean_raw\"][i] = raw[\"hfb_mean\"]\n                dbg = np.where(np.isfinite(db), db, 0.0)\n                region[i] = np.einsum(\"cr,cfb->rfb\", weights, dbg)\n            # keep only chunks needed later\n            keep = set(tchunks[b0 + batch_chunks: b0 + batch_chunks + 2])\n            for c in list(cache):\n                if c not in keep:\n                    del cache[c]\n    # wrist windows, -1.5 to +1.5 s at 30 Hz\n    pos = f[\"processing/behavior/Position\"]\n    prate = float(pos[\"R_Wrist/starting_time\"].attrs[\"rate\"])\n    p0 = float(pos[\"R_Wrist/starting_time\"][()])\n    n_p = pos[\"R_Wrist/data\"].shape[0]\n    k = np.arange(-45, 46)\n    wrist = {w: np.full((n_ev, len(k), 2), np.nan) for w in wrist_names}\n    for w in wrist_names:\n        d = pos[f\"{w}/data\"]\n        for i, t in enumerate(event_times):\n            c = int(round((t - p0) * prate))\n            if c - 45 >= 0 and c + 46 <= n_p:\n                wrist[w][i] = d[c - 45:c + 46, :]\n    f.close()\n    return dict(region=region, elec=elec, seg_db=seg_db, hf_db=hf_db, inside=inside, allzero=allzero,\n                wrist=wrist, wrist_t=k / prate)\n\n\n# ----------------------------------------------------------------------------- regression\n\ndef design_matrix(ev, log_speed=False):\n    \"\"\"Features as the Methods (and code) encode them. Returns (X, column feature names).\"\"\"\n    cols, names = [], []\n    for d in sorted(ev.day.unique()):\n        cols.append((ev.day == d).astype(float).values)\n        names.append(\"day\")\n    tod = np.digitize(ev.time_of_day.values, [8, 16])\n    for b in range(3):\n        cols.append((tod == b).astype(float))\n        names.append(\"time_of_day\")\n    cont = {\n        \"duration\": np.log(ev.duration.values),\n        \"magnitude\": np.log(ev.magnitude.values + 1),\n        \"angle\": fold_angle(ev.angle_raw.values),\n        \"onset_speed\": np.log(ev.onset_speed.values + 1) if log_speed else ev.onset_speed.values,\n        \"speech_ratio\": ev.speech_ratio.values,\n        \"bimanual_ratio\": ev.bimanual_ratio.values,\n        \"bimanual_overlap\": ev.bimanual_overlap.values,\n        \"bimanual_class\": ev.bimanual_class.values,\n    }\n    for k, v in cont.items():\n        sd = v.std()\n        cols.append((v - v.mean()) / sd if sd > 0 else v * 0)\n        names.append(k)\n    return np.column_stack(cols), np.array(names)\n\n\ndef forward_select(X, y, names):\n    \"\"\"Forward selection of features (groups of columns) by OLS adjusted R2 (code _forward_selected_new).\"\"\"\n    feats = list(dict.fromkeys(names))\n    chosen, best = [], -np.inf\n    n = len(y)\n    while True:\n        cand = []\n        for f in feats:\n            if f in chosen:\n                continue\n            sel = np.isin(names, chosen + [f])\n            A = np.column_stack([np.ones(n), X[:, sel]])\n            beta, *_ = np.linalg.lstsq(A, y, rcond=None)\n            res = y - A @ beta\n            r2 = 1 - res @ res / ((y - y.mean()) @ (y - y.mean()))\n            p = A.shape[1] - 1\n            adj = 1 - (1 - r2) * (n - 1) / (n - p - 1)\n            cand.append((adj, f))\n        if not cand:\n            break\n        adj, f = max(cand)\n        if adj > best:\n            best = adj\n            chosen.append(f)\n        else:\n            break\n    return chosen\n\n\ndef day_balanced_splits(days, n_splits, test_frac, rng):\n    \"\"\"Random splits with equal numbers of test events from each day (code train_test_split_day_balance).\"\"\"\n    uniq = np.unique(days)\n    per_day = min((days == d).sum() for d in uniq)\n    n_test_total = int(round(test_frac * len(days)))\n    k = max(1, min(per_day, n_test_total // len(uniq)))\n    out = []\n    for _ in range(n_splits):\n        test = np.concatenate([rng.choice(np.flatnonzero(days == d), k, replace=False) for d in uniq])\n        mask = np.zeros(len(days), bool)\n        mask[test] = True\n        out.append(mask)\n    return out\n\n\ndef r2(y, p):\n    return 1 - ((y - p) ** 2).sum() / ((y - y.mean()) ** 2).sum()\n\n\ndef fit_models(X, names, y, splits, chosen, delta=False, shuffle_rng=None, code_shuffle=False):\n    \"\"\"Huber models (sklearn defaults) over the splits. Returns mean test R2, mean coefficients,\n    and mean Delta R2 per feature when delta is True (feature shuffled in training data, scored\n    on unshuffled test data, Methods; code_shuffle also shuffles the test events, code).\"\"\"\n    from sklearn.linear_model import HuberRegressor\n    feats = list(dict.fromkeys(names))\n    sel = np.isin(names, chosen)\n    Xs = X[:, sel]\n    nsel = names[sel]\n    r2s, coefs = [], []\n    dr2 = {f: [] for f in feats}\n    for test in splits:\n        tr = ~test\n        m = HuberRegressor().fit(Xs[tr], y[tr])\n        full = r2(y[test], m.predict(Xs[test]))\n        r2s.append(full)\n        c = np.zeros(X.shape[1])\n        c[sel] = m.coef_\n        coefs.append(c)\n        if delta:\n            for f in feats:\n                if f not in chosen:\n                    dr2[f].append(0.0)\n                    continue\n                cols = nsel == f\n                Xtr = Xs[tr].copy()\n                perm = shuffle_rng.permutation(tr.sum())\n                Xtr[:, cols] = Xtr[perm][:, cols]\n                Xte = Xs[test].copy()\n                if code_shuffle:\n                    pt = shuffle_rng.permutation(test.sum())\n                    Xte[:, cols] = Xte[pt][:, cols]\n                ms = HuberRegressor().fit(Xtr, y[tr])\n                dr2[f].append(full - r2(y[test], ms.predict(Xte)))\n    out = dict(r2=float(np.mean(r2s)), coef=np.mean(coefs, axis=0))\n    if delta:\n        out[\"delta\"] = {f: float(np.mean(v)) for f, v in dr2.items()}\n    return out\n"
}
```

```
File created successfully at: entries/peterson-2021/ajile.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python3 - <<'EOF'
import re
s=open('ajile.py').read()
s=s.replace("""            keep = set(tchunks[b0 + batch_chunks: b0 + batch_chunks + 2])""","""            keep = {batch[-1]}""")
open('ajile.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cat > t1.py <<'EOF'
import sys, time, resource, numpy as np
sys.path.insert(0,'entries/peterson-2021')
import ajile, pickle
res=sorted(pickle.load(open('meta.pkl','rb')),key=lambda d:d['path'])
d=res[0]
aid="35cebbe1-cbdb-4b45-a132-fed5f67b6d76"
good=d['el'].good.values
w=np.zeros((len(good),8)); w[good]=1; w/=w.sum(0)
t=time.time()
ev=d['evts'][:40]
out=ajile.session_spectral(aid, ev, good, w)
print('time',time.time()-t, 'maxrss MB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
print(out['seg_db'][:10], out['hf_db'][:10], out['inside'].sum(), out['allzero'].sum())
r=out['region'][:, 1]  # (ev, f, b)
bs=r-r[:,:,ajile.BASE].mean(-1,keepdims=True)
print(np.round(np.median(bs,0)[:, 12:22],2))
print(out['elec']['lfb_mean'][:3,:5], out['elec']['hfb_mean_raw'][:3,:5])
print(out['wrist']['R_Wrist'][0,40:50])
EOF
python t1.py
```

```
time 73.31350946426392 maxrss MB 926.788
[ 9.42247815  8.88341121  9.39732668  7.9448735   9.03380254 11.80506798
 11.15399193  9.57589286  8.70263786  8.73785863] [-11.20514981 -11.83431644 -10.69018192 -11.38780469 -11.99014719
 -11.65660899 -11.33556435 -11.12546735  -9.95137626 -11.13144582] 40 0
[[-0.17 -0.55 -0.73 -0.35  0.12  0.57  0.11  0.48 -0.16 -0.22]
 [-0.46 -0.59 -0.38 -0.39 -0.35 -0.39 -0.04  0.01 -0.8  -0.52]
 [-0.26 -0.1   0.17  0.07 -0.13 -0.17  0.12  0.13 -0.19 -0.04]
 [-0.42 -0.67 -0.13 -0.08 -0.18 -0.69  0.23  0.02 -0.57 -0.41]
 [ 0.07 -0.12 -0.27 -0.22 -0.01  0.08  0.54  0.25  0.23 -0.29]
 [-0.26 -0.08 -0.34 -0.52 -0.23 -0.33  0.01 -0.03 -0.09 -0.06]
 [-0.46 -0.1  -0.41 -0.22 -0.21 -0.45 -0.1   0.05 -0.17 -0.14]
 [ 0.01 -0.38 -0.28 -0.42 -0.36 -0.68 -0.22 -0.32 -0.24 -0.68]
 [ 0.23 -0.31 -0.16 -0.47 -0.06 -0.21 -0.32  0.25 -0.33 -0.1 ]
 [-0.11 -0.56  0.09 -0.26  0.02 -0.11 -0.05 -0.06  0.16 -0.58]
 [-0.28  0.03  0.   -0.14 -0.21  0.17 -0.08 -0.11  0.12 -0.11]
 [ 0.21  0.17 -0.15  0.19  0.06  0.23 -0.02 -0.24  0.19 -0.04]
 [ 0.2  -0.37  0.04 -0.3  -0.08  0.35 -0.15 -0.   -0.25  0.23]
 [-0.05 -0.03 -0.54 -0.12 -0.04 -0.17  0.01 -0.12 -0.12 -0.23]
 [-0.07 -0.01  0.17 -0.03  0.16 -0.19  0.43  0.01 -0.17 -0.03]
 [ 0.06 -0.38 -0.29 -0.15 -0.05 -0.12  0.16 -0.17 -0.25 -0.02]
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t2.py <<'EOF'
import sys, time, resource, numpy as np, pickle
sys.path.insert(0,'entries/peterson-2021')
import ajile
from concurrent.futures import ProcessPoolExecutor
res=sorted(pickle.load(open('meta.pkl','rb')),key=lambda d:d['path'])
assets=ajile.list_assets()
def job(i):
    d=res[i]; aid=assets.asset_id[assets.path==d['path']].iloc[0]
    good=d['el'].good.values; w=np.zeros((len(good),8)); w[good]=1; w/=w.sum(0)
    t=time.time(); o=ajile.session_spectral(aid, d['evts'][:15], good, w, n_threads=16)
    return time.time()-t
if __name__=='__main__':
    t=time.time()
    with ProcessPoolExecutor(10) as ex: r=list(ex.map(job, [0,5,10,15,20,25,30,35,40,45]))
    print(r, time.time()-t)
EOF
python t2.py; date -u
```

```
entries/peterson-2021/ajile.py:315: RuntimeWarning: invalid value encountered in subtract
  bs = db - db[:, :, BASE].mean(axis=-1, keepdims=True)
[51.009878396987915, 31.175313234329224, 8.800239562988281, 57.50787806510925, 62.44637584686279, 48.559722661972046, 20.713539838790894, 144.58608293533325, 48.04277062416077, 45.23278307914734] 144.78112888336182
Wed Nov 25 05:31:08 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t3.py <<'EOF'
import h5py, remfile, requests, time, numpy as np, zlib, sys
sys.path.insert(0,'entries/peterson-2021')
import ajile
from concurrent.futures import ThreadPoolExecutor
aid="0d4aaf7f-7e40-4e06-b758-7008bcffac55"  # sub-09 ses-3, 126 ch
f,url=ajile.open_nwb(aid)
ds=f['acquisition/ElectricalSeries/data']; CH=ds.chunks[0]; nch=ds.shape[1]
ev=f['processing/behavior/ReachEvents/timestamps'][:]
cs=sorted({int(e*500)//CH for e in ev})
print(len(cs))
t=time.time(); args=[]
for c in cs[:5]:
    for ch in range(nch):
        ci=ds.id.get_chunk_info_by_coord((c*CH,ch)); args.append((ci.byte_offset,ci.size))
print('lookup',len(args),time.time()-t)
s=requests.Session(); s.mount('https://',requests.adapters.HTTPAdapter(pool_maxsize=32))
def g(a):
    o,n=a; r=s.get(url,headers={'Range':f'bytes={o}-{o+n-1}'}); return len(zlib.decompress(r.content))
t=time.time()
with ThreadPoolExecutor(32) as ex: L=list(ex.map(g,args))
dt=time.time()-t; print('fetch',dt,sum(a[1] for a in args)/dt/1e6,'MB/s')
offs=np.array([a[0] for a in args]); print(np.diff(offs[:10]), [a[1] for a in args[:5]])
EOF
python t3.py
```

```
14
lookup 630 68.48310971260071
fetch 1.7613592147827148 109.05844724223206 MB/s
[313001 313655 313538 313787 313082 313400 313382 313268 313177] [313001, 313655, 313538, 313787, 313082]
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "entries/peterson-2021/ajile.py",
 "offset": 236,
 "limit": 80
}
```

```
236	    Returns a dict of arrays, one row per event.
237	    """
238	    f, url = open_nwb(asset_id)
239	    ds = f["acquisition/ElectricalSeries/data"]
240	    n_t, n_ch = ds.shape
241	    CH = ds.chunks[0]
242	    assert ds.chunks[1] == 1
243	    bank = morlet_bank()
244	    half = (bank.shape[0] - 1) // 2
245	    n_ev = len(event_times)
246	    s0 = np.round(np.asarray(event_times) * FS).astype(int)  # event sample (series starts at 0 s)
247	    seg_lo, seg_hi = s0 - int(SEG_HALF * FS), s0 + int(SEG_HALF * FS)
248	    inside = (seg_lo >= 0) & (seg_hi <= n_t)
249	    nb, nf, nr = len(BIN_T), len(FREQS), weights.shape[1]
250	    region = np.full((n_ev, nr, nf, nb), np.nan, np.float32)
251	    elec = {k: np.full((n_ev, n_ch), np.nan, np.float32) for k in
252	            ["lfb_mean", "hfb_mean", "lfb_median", "hfb_median", "lfb_mean_raw", "hfb_mean_raw"]}
253	    seg_db = np.full(n_ev, np.nan)
254	    hf_db = np.full(n_ev, np.nan)
255	    allzero = np.zeros(n_ev, bool)
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python3 - <<'EOF'
s=open('ajile.py').read()
a=s.index("    sess = requests.Session()\n    sess.mount")
b=s.index("            # events whose chunks are all present")
new='''    sess = requests.Session()
    sess.mount("https://", requests.adapters.HTTPAdapter(pool_connections=n_threads, pool_maxsize=n_threads))
    raw_bytes = CH * 4

    def fetch(arg):
        """All channels of time chunk c. The file stores the chunks of one time block one after
        another in channel order, so one range read from the first channel's chunk holds them
        all; each zlib stream is decoded in turn, and every decoded chunk must have the full
        chunk length. The last channel's offset is checked against the index."""
        c, off, off_last = arg
        span = (off_last - off) + raw_bytes + 4096
        for attempt in range(5):
            try:
                r = sess.get(url, headers={"Range": f"bytes={off}-{off + span - 1}"}, timeout=300)
                r.raise_for_status()
                buf = r.content
                break
            except Exception:
                if attempt == 4:
                    raise
        cols, pos = [], 0
        for ch in range(n_ch):
            d = zlib.decompressobj()
            out = d.decompress(buf[pos:])
            if len(out) != raw_bytes or not d.eof:
                raise ValueError(f"chunk {c},{ch}: decoded {len(out)} bytes")
            cols.append(np.frombuffer(out, dtype="<f4"))
            if ch == n_ch - 2:
                pass
            pos = len(buf) - len(d.unused_data)
            if ch == n_ch - 2 and off + pos != off_last:
                raise ValueError(f"chunk {c}: channels not contiguous")
        return c, np.stack(cols, axis=1)
    cache = {}
    done = np.zeros(n_ev, bool)
    bins_off = np.round(BIN_T * FS).astype(int)
    with ThreadPoolExecutor(n_threads) as ex:
        for b0 in range(0, len(tchunks), batch_chunks):
            batch = tchunks[b0:b0 + batch_chunks]
            args = []
            for c in batch:
                if c in cache:
                    continue
                first = ds.id.get_chunk_info_by_coord((c * CH, 0)).byte_offset
                last = ds.id.get_chunk_info_by_coord((c * CH, n_ch - 1)).byte_offset
                args.append((c, first, last))
            for c, arr in ex.map(fetch, args):
                cache[c] = arr
'''
s=s[:a]+new+s[b:]
s=s.replace("n_threads=24, batch_chunks=6","n_threads=6, batch_chunks=6")
open('ajile.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cat > t4.py <<'EOF'
import sys, time, numpy as np
sys.path.insert(0,'entries/peterson-2021')
import ajile
aid="0d4aaf7f-7e40-4e06-b758-7008bcffac55"
f,url=ajile.open_nwb(aid); ds=f['acquisition/ElectricalSeries/data']
ev=f['processing/behavior/ReachEvents/timestamps'][:]
good=np.ones(ds.shape[1],bool); w=np.ones((ds.shape[1],8))/ds.shape[1]
t=time.time(); o=ajile.session_spectral(aid, ev, good, w); print('15 ev',time.time()-t)
# compare one event's raw against h5py
i=3; s=int(round(ev[i]*500)); x=ds[s-50:s+50, :].astype(float)
print(np.isfinite(o['elec']['lfb_mean'][:,0]).sum())
EOF
python t4.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t4.py", line 8, in <module>
    t=time.time(); o=ajile.session_spectral(aid, ev, good, w); print('15 ev',time.time()-t)
                     ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "entries/peterson-2021/ajile.py", line 308, in session_spectral
    for c, arr in ex.map(fetch, args):
                  ~~~~~~^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/_base.py", line 625, in result_iterator
    yield _result_or_cancel(fs.pop())
          ~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/_base.py", line 318, in _result_or_cancel
    return fut.result(timeout)
           ~~~~~~~~~~^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/_base.py", line 460, in result
    return self.__get_result()
           ~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/_base.py", line 402, in __get_result
    raise self._exception
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/concurrent/futures/thread.py", line 59, in run
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t5.py <<'EOF'
import sys, numpy as np
sys.path.insert(0,'entries/peterson-2021')
import ajile
aid="0d4aaf7f-7e40-4e06-b758-7008bcffac55"
f,url=ajile.open_nwb(aid); ds=f['acquisition/ElectricalSeries/data']; CH=ds.chunks[0]
for c in [100,101]:
  info=[ds.id.get_chunk_info_by_coord((c*CH,ch)) for ch in range(ds.shape[1])]
  off=np.array([i.byte_offset for i in info]); sz=np.array([i.size for i in info])
  gap=off[1:]-(off[:-1]+sz[:-1]); print(c, off[0], np.unique(gap,return_counts=True), np.flatnonzero(gap))
  print(off[:3], off[-3:])
EOF
python t5.py
```

```
100 3841015329 (array([   0, 2616]), array([122,   3])) [  4  61 118]
[3841015329 3841328963 3841642609] [3878669731 3878887660 3879151302]
101 3879432088 (array([   0, 2616]), array([123,   2])) [ 49 106]
[3879432088 3879745729 3880059630] [3917101377 3917318338 3917581951]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python3 - <<'EOF'
s=open('ajile.py').read()
old=s[s.index("        cols, pos = [], 0\n"):s.index("        return c, np.stack(cols, axis=1)\n")]
new='''        cols, pos = [], 0
        for ch in range(n_ch):
            if buf[pos:pos + 4] == b"TREE":
                # an HDF5 B-tree node written between two chunks: skip to the next zlib stream
                nxt = pos + 4
                while True:
                    nxt = buf.index(b"\\x78", nxt)
                    try:
                        zlib.decompressobj().decompress(buf[nxt:nxt + 64])
                        break
                    except zlib.error:
                        nxt += 1
                pos = nxt
            d = zlib.decompressobj()
            out = d.decompress(buf[pos:])
            if len(out) != raw_bytes or not d.eof:
                raise ValueError(f"chunk {c},{ch}: decoded {len(out)} bytes")
            cols.append(np.frombuffer(out, dtype="<f4"))
            if ch == n_ch - 1 and off + pos != off_last:
                raise ValueError(f"chunk {c}: last channel not at its indexed offset")
            pos = len(buf) - len(d.unused_data)
'''
s=s.replace(old,new)
s=s.replace("span = (off_last - off) + raw_bytes + 4096","span = (off_last - off) + raw_bytes + 4096")
open('ajile.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cat >> t4.py <<'EOF'
k=o['elec']['lfb_mean'][:,0]; print(k[:5])
EOF
python t4.py
```

```
15 ev 143.62660574913025
15
[-7.6656747  -0.6770661   1.8544611   4.3334546   0.05166302]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python3 - <<'EOF'
s=open('ajile.py').read()
s=s.replace('''            d = zlib.decompressobj()
            out = d.decompress(buf[pos:])
            if len(out) != raw_bytes or not d.eof:
                raise ValueError(f"chunk {c},{ch}: decoded {len(out)} bytes")
            cols.append(np.frombuffer(out, dtype="<f4"))
            if ch == n_ch - 1 and off + pos != off_last:
                raise ValueError(f"chunk {c}: last channel not at its indexed offset")
            pos = len(buf) - len(d.unused_data)
''','''            d = zlib.decompressobj()
            piece = mv[pos:pos + raw_bytes + 1024]
            out = d.decompress(piece)
            if len(out) != raw_bytes or not d.eof:
                raise ValueError(f"chunk {c},{ch}: decoded {len(out)} bytes")
            cols.append(np.frombuffer(out, dtype="<f4"))
            if ch == n_ch - 1 and off + pos != off_last:
                raise ValueError(f"chunk {c}: last channel not at its indexed offset")
            pos += len(piece) - len(d.unused_data)
''')
s=s.replace('''        cols, pos = [], 0
''','''        cols, pos = [], 0
        mv = memoryview(buf)
''')
open('ajile.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python -X importtime -c 1 2>/dev/null; python t4.py
```

```
15 ev 135.03815293312073
15
[-7.6656747  -0.6770661   1.8544611   4.3334546   0.05166302]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -m cProfile -s cumtime t4.py 2>&1 | head -40
```

```
15 ev 136.8266270160675
15
[-7.6656747  -0.6770661   1.8544611   4.3334546   0.05166302]
         12486624 function calls (11747544 primitive calls) in 139.845 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   1277/1    0.032    0.000  139.855  139.855 {built-in method builtins.exec}
        1    0.002    0.002  139.855  139.855 t4.py:1(<module>)
        1    0.035    0.035  136.818  136.818 ajile.py:230(session_spectral)
1070/1058    0.013    0.000  136.571    0.129 sessions.py:557(request)
1066/1054    0.007    0.000  135.638    0.129 sessions.py:655(get)
1072/1058    0.022    0.000  135.473    0.128 sessions.py:752(send)
    16461    0.026    0.000  132.507    0.008 RemFile.py:190(readinto)
    16461    0.040    0.000  132.472    0.008 RemFile.py:123(read)
    17089    0.102    0.000  132.428    0.008 RemFile.py:196(_load_chunk)
     1051    0.019    0.000  132.323    0.126 RemFile.py:410(_get_bytes)
     1051    0.009    0.000  132.302    0.126 RemFile.py:439(fetch_bytes)
124431/51500    0.129    0.000  131.562    0.003 socket.py:710(readinto)
[... 21 more lines not kept]
```

**Agent**

Remote B-tree lookups through h5py cost ~37 HTTP round-trips each. I'll read the chunk B-tree directly with parallel range requests instead.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t6.py <<'EOF'
import sys, numpy as np, struct, requests, time, h5py
sys.path.insert(0,'entries/peterson-2021')
import ajile
aid="0d4aaf7f-7e40-4e06-b758-7008bcffac55"
f,url=ajile.open_nwb(aid); ds=f['acquisition/ElectricalSeries/data']
info=h5py.h5o.get_info(ds.id)
print([a for a in dir(info) if not a.startswith('_')])
addr=getattr(info,'addr',None); print(addr)
b=requests.get(url,headers={'Range':f'bytes={addr}-{addr+4095}'}).content
print(b[:16])
EOF
python t6.py
```

```
['addr', 'atime', 'btime', 'ctime', 'fileno', 'hdr', 'meta_size', 'mtime', 'num_attrs', 'rc', 'type']
2864
b'\x01\x00\x0e\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python3 - <<'EOF'
s=open('ajile.py').read()
idx=s.index("def session_spectral(")
new='''def _range(sess, url, off, n):
    for attempt in range(5):
        try:
            r = sess.get(url, headers={"Range": f"bytes={off}-{off + n - 1}"}, timeout=300)
            r.raise_for_status()
            return r.content
        except Exception:
            if attempt == 4:
                raise


def chunk_index(ds, url, sess, n_threads=16):
    """Address and size of every chunk of a chunked 2-D dataset, read from the file's version 1
    B-tree with parallel range requests (h5py's own lookups go node by node over the network and
    take about 0.1 s each). Returns {(row offset, column offset): (address, size)}."""
    import struct
    addr = h5py.h5o.get_info(ds.id).addr
    hdr = _range(sess, url, addr, 4096)
    assert hdr[0] == 1, "object header version 1 expected"
    nmsg = struct.unpack("<H", hdr[2:4])[0]
    blocks = [(hdr, 16, 16 + struct.unpack("<I", hdr[8:12])[0])]
    root = None
    seen = 0
    while blocks and root is None:
        buf, p, end = blocks.pop(0)
        while p + 8 <= end and seen < nmsg:
            mtype, msize = struct.unpack("<HH", buf[p:p + 4])
            data = buf[p + 8:p + 8 + msize]
            seen += 1
            if mtype == 8:  # data layout, version 3, chunked
                assert data[0] == 3 and data[1] == 2, "chunked layout version 3 expected"
                root = struct.unpack("<Q", data[3:11])[0]
                rank = data[2]
                break
            if mtype == 0x10:  # continuation
                caddr, clen = struct.unpack("<QQ", data[:16])
                blocks.append((_range(sess, url, caddr, clen), 0, clen))
            p += 8 + msize
    assert root is not None
    key_size = 8 + 8 * rank
    out = {}

    def read_node(a):
        head = _range(sess, url, a, 24)
        assert head[:4] == b"TREE" and head[4] == 1
        level, used = head[5], struct.unpack("<H", head[6:8])[0]
        body = _range(sess, url, a + 24, used * (key_size + 8) + key_size)
        items = []
        for i in range(used):
            k = body[i * (key_size + 8): i * (key_size + 8) + key_size]
            size = struct.unpack("<I", k[:4])[0]
            offs = struct.unpack("<" + "Q" * rank, k[8:8 + 8 * rank])
            child = struct.unpack("<Q", body[i * (key_size + 8) + key_size: (i + 1) * (key_size + 8)])[0]
            items.append((offs, size, child))
        return level, items
    level_nodes = [root]
    with ThreadPoolExecutor(n_threads) as ex:
        while level_nodes:
            nxt = []
            for level, items in ex.map(read_node, level_nodes):
                for offs, size, child in items:
                    if level == 0:
                        out[(offs[0], offs[1])] = (child, size)
                    else:
                        nxt.append(child)
            level_nodes = nxt
    return out


'''
s=s[:idx]+new+s[idx:]
# replace fetch & lookups to use index
a=s.index("    raw_bytes = CH * 4\n")
b=s.index("    cache = {}\n    done = np.zeros(n_ev, bool)")
s=s[:a]+'''    raw_bytes = CH * 4
    index = chunk_index(ds, url, sess)
    assert len(index) == -(-n_t // CH) * n_ch, "chunk index incomplete"

    def fetch(c):
        """All channels of time chunk c, read in one range request: the file stores the chunks
        of one time block one after another (with B-tree nodes between some of them)."""
        locs = [index[(c * CH, ch)] for ch in range(n_ch)]
        lo = min(a for a, _ in locs)
        hi = max(a + n for a, n in locs)
        buf = _range(sess, url, lo, hi - lo)
        cols = []
        for a, n in locs:
            out = zlib.decompress(buf[a - lo:a - lo + n])
            if len(out) != raw_bytes:
                raise ValueError(f"chunk {c}: decoded {len(out)} bytes")
            cols.append(np.frombuffer(out, dtype="<f4"))
        return c, np.stack(cols, axis=1)
'''+s[b:]
s=s.replace('''            args = []
            for c in batch:
                if c in cache:
                    continue
                first = ds.id.get_chunk_info_by_coord((c * CH, 0)).byte_offset
                last = ds.id.get_chunk_info_by_coord((c * CH, n_ch - 1)).byte_offset
                args.append((c, first, last))
''','''            args = [c for c in batch if c not in cache]
''')
open('ajile.py','w').write(s)
EOF
grep -n "def fetch" -A3 ajile.py | head; cd $TMPDIR && . dev/bin/activate && python t4.py
```

```
337:    def fetch(c):
338-        """All channels of time chunk c, read in one range request: the file stores the chunks
339-        of one time block one after another (with B-tree nodes between some of them)."""
340-        locs = [index[(c * CH, ch)] for ch in range(n_ch)]
15 ev 160.48746609687805
15
[-7.6656747  -0.6770661   1.8544611   4.3334546   0.05166302]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t7.py <<'EOF'
import sys, time, numpy as np, requests
sys.path.insert(0,'entries/peterson-2021')
import ajile
aid="0d4aaf7f-7e40-4e06-b758-7008bcffac55"
t=time.time(); f,url=ajile.open_nwb(aid); ds=f['acquisition/ElectricalSeries/data']; print('open',time.time()-t)
s=requests.Session(); s.mount('https://',requests.adapters.HTTPAdapter(pool_maxsize=32))
t=time.time(); b=ajile._range(s,url,0,100); print('one req',time.time()-t)
t=time.time(); b=ajile._range(s,url,0,100); print('one req',time.time()-t)
t=time.time(); idx=ajile.chunk_index(ds,url,s,n_threads=32); print('index',time.time()-t,len(idx))
EOF
python t7.py
```

```
open 1.0367381572723389
one req 0.1333451271057129
one req 0.04803633689880371
index 148.03808665275574 64512
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t8.py <<'EOF'
import sys, time, numpy as np, requests
sys.path.insert(0,'entries/peterson-2021')
import ajile
from concurrent.futures import ThreadPoolExecutor
aid="0d4aaf7f-7e40-4e06-b758-7008bcffac55"
url=ajile.s3_url(aid)
s=requests.Session(); s.mount('https://',requests.adapters.HTTPAdapter(pool_maxsize=32))
offs=np.random.default_rng(0).integers(0,10**10,200)
t=time.time()
with ThreadPoolExecutor(32) as ex: L=list(ex.map(lambda o: ajile._range(s,url,int(o),2600), offs))
print('200 reqs',time.time()-t)
import ajile as A
f,url2=A.open_nwb(aid); ds=f['acquisition/ElectricalSeries/data']
cnt={'n':0}
orig=A._range
def wrapped(*a):
    cnt['n']+=1; return orig(*a)
A._range=wrapped
t=time.time(); idx=A.chunk_index(ds,url,s,n_threads=32); print('index',time.time()-t,cnt)
EOF
python t8.py
```

```
200 reqs 0.8331079483032227
index 144.89521074295044 {'n': 2307}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && sed -i 's/            level_nodes = nxt\n/X/' ajile.py && python3 - <<'EOF'
s=open('ajile.py').read()
s=s.replace("            level_nodes = nxt\n","            level_nodes = nxt\n            print('level', len(nxt), flush=True)\n",1)
open('ajile.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && timeout 60 python t7.py
```

```
Exit code 124
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && timeout 100 python -u t7.py
```

```
Exit code 124
open 0.9846620559692383
one req 0.17003536224365234
one req 0.05589008331298828
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t9.py <<'EOF'
import sys, time, numpy as np, requests, struct, h5py
sys.path.insert(0,'entries/peterson-2021')
import ajile
aid="0d4aaf7f-7e40-4e06-b758-7008bcffac55"
f,url=ajile.open_nwb(aid); ds=f['acquisition/ElectricalSeries/data']
s=requests.Session()
addr=h5py.h5o.get_info(ds.id).addr
t=time.time(); hdr=ajile._range(s,url,addr,4096); print(time.time()-t)
nmsg=struct.unpack("<H",hdr[2:4])[0]; p=16
for i in range(nmsg):
    mt,ms=struct.unpack("<HH",hdr[p:p+4]); print(mt,ms, hdr[p+8:p+8+min(ms,24)].hex()); p+=8+ms
EOF
timeout 60 python -u t9.py
```

```
Exit code 124
```

**Agent calls Bash**

```bash
ps aux --sort=-%cpu | head -8; date -u
```

```
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
runner         2 50.0  0.0  10224  5912 ?        S    05:57   0:00 /bin/bash -c source /home/runner/.claude/shell-snapshots/snapshot-bash-1795583524162-ktle20.sh 2>/dev/null || true && export TMPDIR=/tmp/claude-1001 && shopt -u extglob 2>/dev/null || true && { \builtin unalias -- 'unsetenv'; \builtin unset -f -- 'unsetenv'; } >/dev/null 2>&1 || true && eval 'ps aux --sort=-%cpu | head -8; date -u' < /dev/null && pwd -P >| /tmp/claude-1001/cwd-5444
runner         1 42.8  0.0   3804  1504 ?        Ss   05:57   0:00 bwrap --new-session --die-with-parent --ro-bind / / --ro-bind /home/runner /home/runner --ro-bind /opt/hostedtoolcache /opt/hostedtoolcache --ro-bind /run/containerd /run/containerd --ro-bind /tmp/claude-1001/-home-runner-work-encore-registry-encore-registry /tmp/claude-1001/-home-runner-work-encore-registry-encore-registry --ro-bind /home/runner/.config /home/runner/.config --ro-bind /home/runner/work /home/runner/work --ro-bind /home/runner/.local /home/runner/.local --ro-bind /opt/hostedtoolcache/node /opt/hostedtoolcache/node --ro-bind /opt/hostedtoolcache/Python /opt/hostedtoolcache/Python --ro-bind /home/runner/.cargo /home/runner/.cargo --ro-bind /home/runner/.dotnet /home/runner/.dotnet --ro-bind /home/runner/.claude /home/runner/.claude --ro-bind /tmp/claude-1001/-home-runner-work-encore-registry-encore-registry/f827794a-c716-4e85-a39e-d824755c2636 /tmp/claude-1001/-home-runner-work-encore-registry-encore-registry/f827794a-c716-4e85-a39e-d824755c2636 --ro-bind /home/runner/work/encore-registry /home/runner/work/encore-registry --ro-bind /opt/hostedtoolcache/node/22.23.5 /opt/hostedtoolcache/node/22.23.5 --ro-bind /opt/hostedtoolcache/Python/3.13.18 /opt/hostedtoolcache/Python/3.13.18 --ro-bind /home/runner/.config/composer /home/runner/.config/composer --ro-bind /home/runner/work/_temp /home/runner/work/_temp --ro-bind /opt/hostedtoolcache/node/22.23.5/x64 /opt/hostedtoolcac
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > t10.py <<'EOF'
import sys, time, h5py
sys.path.insert(0,'entries/peterson-2021')
import ajile
f,url=ajile.open_nwb("0d4aaf7f-7e40-4e06-b758-7008bcffac55"); g=f['acquisition/ElectricalSeries']
t=time.time(); oi=h5py.h5g.get_objinfo(g.id, b'data'); print(oi.objno, oi.fileno, time.time()-t)
print(h5py.h5o.get_info.__doc__)
EOF
timeout 60 python -u t10.py
```

```
(2864, 0) (1, 0) 0.000102996826171875
(ObjectID loc, STRING name=, INT index=, **kwds) => ObjInfo

    Get information describing an object in an HDF5 file.  Provide the object
    itself, or the containing group and exactly one of "name" or "index".

    STRING obj_name (".")
        When "index" is specified, look in this subgroup instead.
        Otherwise ignored.

    PropID lapl (None)
        Link access property list

    INT index_type (h5.INDEX_NAME)

    INT order (h5.ITER_INC)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python3 - <<'EOF'
s=open('ajile.py').read()
s=s.replace("""    addr = h5py.h5o.get_info(ds.id).addr
""","""    parent, name = ds.name.rsplit("/", 1)
    addr = h5py.h5g.get_objinfo(ds.file[parent].id, name.encode()).objno[0]
""")
s=s.replace("            print('level', len(nxt), flush=True)\n","")
open('ajile.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && timeout 300 python -u t7.py && timeout 600 python -u t4.py
```

```
open 0.984318733215332
one req 0.19939804077148438
one req 0.0546717643737793
index 7.478564739227295 64512
15 ev 18.578578233718872
15
[-7.6656747  -0.6770661   1.8544611   4.3334546   0.05166302]
Shell cwd was reset to
```

**Agent**

Index read now takes 7 s per file instead of minutes, and values are unchanged. Measuring aggregate throughput across parallel files.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && sed -i 's/d\[.evts.\]\[:15\], good, w, n_threads=16)/d["evts"][:40], good, w)/' t2.py && sed -i 's/ProcessPoolExecutor(10)/ProcessPoolExecutor(8)/' t2.py && grep -n session_spectral t2.py && timeout 900 python -u t2.py 2>&1 | grep -v Warn; date -u
```

```
10:    t=time.time(); o=ajile.session_spectral(aid, d["evts"][:40], good, w)
  bs = db - db[:, :, BASE].mean(axis=-1, keepdims=True)
[36.712942361831665, 36.16328239440918, 33.43435788154602, 37.07988500595093, 29.321311235427856, 22.78675079345703, 36.536377906799316, 35.37922191619873, 24.334352254867554, 20.867326021194458] 50.31697940826416
Wed Nov 25 05:58:46 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python3 - <<'EOF'
s=open('ajile.py').read()
s=s.replace('''    es = f["acquisition/ElectricalSeries"]
    pos = f["processing/behavior/Position"]''','''    groups = {k: _txt(v.attrs.get("description", "")) for k, v in f["general/extracellular_ephys"].items()
              if isinstance(v, h5py.Group) and v.attrs.get("neurodata_type") in (b"ElectrodeGroup", "ElectrodeGroup")}
    es = f["acquisition/ElectricalSeries"]
    pos = f["processing/behavior/Position"]''')
s=s.replace('''        electrodes=el, reaches=reaches, epochs=epochs,''','''        electrodes=el, groups=groups, reaches=reaches, epochs=epochs,''')
# pseudo-event control
s=s.replace('''    elec = {k: np.full((n_ev, n_ch), np.nan, np.float32) for k in
            ["lfb_mean", "hfb_mean", "lfb_median", "hfb_median", "lfb_mean_raw", "hfb_mean_raw"]}''','''    elec = {k: np.full((n_ev, n_ch), np.nan, np.float32) for k in
            ["lfb_mean", "hfb_mean", "lfb_median", "hfb_median", "lfb_mean_raw", "hfb_mean_raw",
             "lfb_mean_shift", "hfb_mean_shift"]}''')
s=s.replace('''                idx = centre + bins_off[:, None] + np.arange(-half, half + 1)[None, :]  # (nb, taps)
                win = seg[:, idx]  # (n_ch, nb, taps)
                # convolution: flip the kernel
                pw = np.abs(win @ bank[::-1, :]) ** 2  # (n_ch, nb, nf)
                with np.errstate(divide="ignore"):
                    db = 10 * np.log10(pw).transpose(0, 2, 1)  # (n_ch, nf, nb)''','''                taps = np.arange(-half, half + 1)[None, :]
                idx = centre + bins_off[:, None] + taps  # (nb, taps)
                # convolution: flip the kernel
                pw = np.abs(seg[:, idx] @ bank[::-1, :]) ** 2  # (n_ch, nb, nf)
                # control: the same measure around a pseudo-onset SHIFT_S before the event
                pws = np.abs(seg[:, idx + int(SHIFT_S * FS)] @ bank[::-1, :]) ** 2
                with np.errstate(divide="ignore"):
                    db = 10 * np.log10(pw).transpose(0, 2, 1)  # (n_ch, nf, nb)
                    dbs = 10 * np.log10(pws).transpose(0, 2, 1)
                sh = band_stats(dbs - dbs[:, :, BASE].mean(axis=-1, keepdims=True))
                elec["lfb_mean_shift"][i] = sh["lfb_mean"]
                elec["hfb_mean_shift"][i] = sh["hfb_mean"]''')
s=s.replace('''SEG_HALF = 5.0  # 10 s segments centred on the event''','''SEG_HALF = 5.0  # 10 s segments centred on the event
SHIFT_S = -3.0  # pseudo-onset for the clock check: 3 s before the event, inside the same segment''')
s+='''

def _spectral_job(args):
    import os
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    asset_id, times, good, weights = args
    return session_spectral(asset_id, times, good, weights)


def run_spectral(jobs, workers=8):
    """jobs: list of (asset_id, event_times, good, weights). Runs files in parallel processes."""
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn")) as ex:
        return list(ex.map(_spectral_job, jobs))
'''
open('ajile.py','w').write(s)
EOF
grep -n "SHIFT_S" ajile.py | head
```

```
64:SHIFT_S = -3.0  # pseudo-onset for the clock check: 3 s before the event, inside the same segment
384:                # control: the same measure around a pseudo-onset SHIFT_S before the event
385:                pws = np.abs(seg[:, idx + int(SHIFT_S * FS)] @ bank[::-1, :]) ** 2
```

**Agent calls Bash**

```bash
cat >> ajile.py <<'EOF'


def match_projection(m, n_el):
    """Rows of a projection matrix matched to the file's electrodes by order (code
    load_project_spectral_power); when there are more rows than electrodes, all-zero rows are
    dropped first (claims file, roi-projection-link). Returns (array n_el x regions, how)."""
    a = m.values.astype(float)
    how = "as is"
    if len(a) > n_el:
        nz = ~np.all(a == 0, axis=1)
        a = a[nz]
        how = f"dropped {int((~nz).sum())} all-zero rows"
    if len(a) != n_el:
        return None, how + f"; {len(a)} rows for {n_el} electrodes"
    return a, how


def session_weights(proj, good):
    """Weights of the eight regions: bad electrodes 0, each region renormalised to sum 1."""
    w = proj.copy()
    w[~good] = 0
    s = w.sum(axis=0)
    return w / np.where(s > 0, s, np.nan)
EOF
cd $TMPDIR && . dev/bin/activate && cat > dev_spec.py <<'EOF'
import sys, time, pickle, numpy as np, resource
sys.path.insert(0,'entries/peterson-2021')
import ajile
if __name__=='__main__':
    t=time.time()
    assets=ajile.list_assets(); metas=ajile.load_all_meta(assets); print('meta',time.time()-t, flush=True)
    files,_=ajile.figshare_files()
    proj={}
    for s in range(1,13):
        m,c=ajile.load_projection(s,files)
        n_el=len([x for x in metas if int(x['subject_id'])==s][0]['electrodes'])
        a,how=ajile.match_projection(m,n_el); print(s,m.shape,n_el,how)
        proj[s]=(m,c,a)
    jobs=[]
    for x in metas:
        s=int(x['subject_id']); a=proj[s][2]
        cols=[list(proj[s][0].columns).index(r) for r in ajile.ROIS]
        good=x['electrodes'].good.values.astype(bool)
        w=ajile.session_weights(a[:,cols],good)
        jobs.append((x['asset_id'],x['event_times'],good,w))
    t=time.time()
    res=ajile.run_spectral(jobs)
    print('spectral',time.time()-t, 'rss',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3, resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss/1e3)
    pickle.dump(dict(metas=metas,proj=proj,res=res,assets=assets),open('dev_spec.pkl','wb'))
EOF
date -u; timeout 3000 python -u dev_spec.py 2>&1 | grep -v -i warn; date -u
```

```
Wed Nov 25 06:00:01 UTC 2026
meta 74.07548546791077
1 (99, 116) 94 dropped 4 all-zero rows; 95 rows for 94 electrodes
2 (87, 116) 86 dropped 0 all-zero rows; 87 rows for 86 electrodes
3 (97, 116) 96 dropped 16 all-zero rows; 81 rows for 96 electrodes
4 (85, 116) 84 dropped 0 all-zero rows; 85 rows for 84 electrodes
5 (107, 116) 106 dropped 0 all-zero rows; 107 rows for 106 electrodes
6 (81, 116) 80 dropped 0 all-zero rows; 81 rows for 80 electrodes
7 (65, 116) 64 dropped 0 all-zero rows; 65 rows for 64 electrodes
8 (93, 116) 92 dropped 0 all-zero rows; 93 rows for 92 electrodes
9 (127, 116) 126 dropped 0 all-zero rows; 127 rows for 126 electrodes
10 (127, 116) 126 dropped 0 all-zero rows; 127 rows for 126 electrodes
11 (107, 116) 106 dropped 0 all-zero rows; 107 rows for 106 electrodes
12 (125, 116) 124 dropped 8 all-zero rows; 117 rows for 124 electrodes
Traceback (most recent call last):
  File "/tmp/claude-1001/dev_spec.py", line 19, in <module>
    w=ajile.session_weights(a[:,cols],good)
                            ~^^^^^^^^
TypeError: 'NoneType' object is not subscriptable
Wed Nov 25 06:01:32 UTC 2026
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys; sys.path.insert(0,'entries/peterson-2021')
import ajile, numpy as np, requests
files,_=ajile.figshare_files()
txt=requests.get(files['aal_07_elecs2ROI.csv']).text.splitlines()
print(len(txt)); print(txt[0][:200]); print(txt[1][:200]); print(txt[-1][:200]); print(txt[-2][:200])
txt=requests.get(files['aal_01_elecs2ROI.csv']).text.splitlines()
a=np.array([[float(v) for v in l.split(',')] for l in txt[1:]])
print(np.flatnonzero(a.sum(1)==0), a.sum(1)[:3], a.sum(1)[-3:])
EOF
```

```
66
Precentral_L,Precentral_R,Frontal_Sup_L,Frontal_Sup_R,Frontal_Sup_Orb_L,Frontal_Sup_Orb_R,Frontal_Mid_L,Frontal_Mid_R,Frontal_Mid_Orb_L,Frontal_Mid_Orb_R,Frontal_Inf_Oper_L,Frontal_Inf_Oper_R,Frontal_
9.2131,0.00087454,4.2852,0.00027989,9.9119e-07,2.0083e-21,5.9877,1.8577e-08,3.1721e-07,4.0379e-26,2.082,2.5101e-13,0.57728,2.5916e-14,0.0093642,3.9861e-24,1.3025,2.0191e-21,0.86975,0.065848,1.257e-06,
0.00021229,5.4489e-33,8.8381e-12,1.5165e-21,0.94356,0.94124,6.5224e-07,5.9694e-21,0.79073,0.17849,0.10068,3.3244e-19,0.076233,3.1939e-16,0.77285,0.062133,0.14249,4.3793e-13,7.7346e-18,3.0691e-20,0.930
0.00052086,1.2408e-32,2.1702e-13,4.3082e-24,0.011886,0.00064198,1.2848e-07,1.4137e-23,0.00072571,1.2406e-05,0.055109,4.3284e-21,0.0055506,2.5582e-19,0.018235,2.3786e-05,0.19704,4.4217e-15,4.5461e-18,2
[95 96 97 98] [77.9068004   3.08330307  1.15116204] [0. 0. 0.]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys; sys.path.insert(0,'entries/peterson-2021')
import ajile, numpy as np, requests, pickle
files,_=ajile.figshare_files()
for s in range(1,13):
    txt=requests.get(files[f'aal_{s:02d}_elecs2ROI.csv']).text.splitlines()
    a=np.array([[float(v) for v in l.split(',')] for l in txt[1:]])
    z=np.flatnonzero(a.sum(1)==0)
    print(s, a.shape, np.allclose(a[0],a[1:].sum(0),rtol=1e-3), np.abs(a[0]-a[1:].sum(0)).max().round(4), 'zero rows',z)
EOF
```

```
1 (99, 116) False 8.7065 zero rows [95 96 97 98]
2 (87, 116) False 14.368 zero rows []
3 (97, 116) False 8.7352 zero rows [81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96]
4 (85, 116) False 9.177 zero rows []
5 (107, 116) False 11.994 zero rows []
6 (81, 116) False 7.3363 zero rows []
7 (65, 116) False 11.656 zero rows []
8 (93, 116) False 9.893 zero rows []
9 (127, 116) False 11.659 zero rows []
10 (127, 116) False 10.429 zero rows []
11 (107, 116) False 8.8755 zero rows []
12 (125, 116) False 11.999 zero rows [73 74 75 76 77 78 79 80]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle, numpy as np
res=sorted(pickle.load(open('meta.pkl','rb')),key=lambda d:d['path'])
for s in [b'01',b'03',b'12']:
    d=[x for x in res if x['sub']==s][0]; el=d['el']
    print(s, np.flatnonzero(el.x.isna()), el.group_name.values[[0,-1]], len(el))
    print(el.groupby('group_name').id.agg(['min','max']))
EOF
```

```
b'01' [] [b'GRID' b'LTO'] 94
            min  max
group_name          
b'GRID'       0   63
b'LAT'       72   77
b'LID'       64   71
b'LMT'       78   81
b'LPT'       82   87
b'LTO'       88   93
b'03' [80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95] [b'GRID' b'LPD'] 96
            min  max
group_name          
b'GRID'       0   63
b'LAD'       80   87
b'LAT'       64   71
b'LMT'       72   79
b'LPD'       88   95
b'12' [72 73 74 75 76 77 78 79] [b'GRID' b'PHD'] 124
            min  max
group_name          
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && for f in tfr_utils.py compute_spectral_power.py; do curl -s -o $f https://raw.githubusercontent.com/BruntonUWBio/naturalistic_arm_movements_ecog/04c6faf2f219586fa834d10c614ef48a694cec55/$f; done; ls -la tfr_utils.py; grep -n "elecs2ROI\|read_csv\|def load_project_spectral_power\|def tfr_boot_sig_mask" -A12 tfr_utils.py | head -120
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -s https://api.github.com/repos/BruntonUWBio/naturalistic_arm_movements_ecog/git/trees/04c6faf2f219586fa834d10c614ef48a694cec55?recursive=1 | python3 -c "import json,sys;d=json.load(sys.stdin);[print(t['path']) for t in d.get('tree',[])]; print(d.get('message'))" | head -50
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL https://api.github.com/repos/BruntonUWBio/naturalistic_arm_movements_ecog/git/trees/04c6faf2f219586fa834d10c614ef48a694cec55?recursive=1 | python3 -c "import json,sys;d=json.load(sys.stdin);[print(t['path']) for t in d.get('tree',[])]; print(d.get('message'))" | head -50
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && mkdir -p code && cd code && B=https://raw.githubusercontent.com/BruntonUWBio/naturalistic_arm_movements_ecog/04c6faf2f219586fa834d10c614ef48a694cec55/compute_power_gen_figs_python; for f in tfr_utils.py compute_spectral_power.py regression_utils.py fit_regression_models.py config.py; do curl -sL -o $f $B/$f; done; ls -la; grep -n "elecs2ROI" -B3 -A25 tfr_utils.py | head -80
```

```
total 96
drwxr-xr-x 2 runner runner  4096 Nov 25 06:02 .
drwx------ 7 runner runner  4096 Nov 25 06:02 ..
-rw-r--r-- 1 runner runner  4133 Nov 25 06:02 compute_spectral_power.py
-rw-r--r-- 1 runner runner  3612 Nov 25 06:02 config.py
-rw-r--r-- 1 runner runner  4830 Nov 25 06:02 fit_regression_models.py
-rw-r--r-- 1 runner runner 27457 Nov 25 06:02 regression_utils.py
-rw-r--r-- 1 runner runner 38091 Nov 25 06:02 tfr_utils.py
151-        metadata_list += [str(j)]*int(power_load.data.shape[0])
152-
153-        #Project to ROI's
154:        df = pd.read_csv(roi_proj_loadpath+atlas+'_'+str(j+1).zfill(2)+'_elecs2ROI.csv')
155-        chan_ind_vals = np.nonzero(df.transpose().mean().values!=0)[0][1:] #+ 1
156-        
157-        if rem_bad_chans:
158-            inds2drop = []
159-            for i,bad_ch in enumerate(bad_chans):
160-                inds2drop.append(np.nonzero(ch_list==bad_ch)[0])
161-            inds2drop = np.asarray(inds2drop)
162-            if len(inds2drop)==1:
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 120,150p tfr_utils.py; sed -n 178,200p tfr_utils.py
```

```
curr_masked_power_ave = np.copy(curr_power) #no significance mask
    return curr_masked_power_ave

def str2bool(v):
    #Allows True/False booleans in argparse
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
        
        
def load_project_spectral_power(tfr_lp,roi_proj_loadpath,good_rois,n_subjs,atlas='aal',rem_bad_chans=False):
    '''
    Loads in electrode-level spectral power and projects it to ROI's. 
    '''
    first_pass = 0
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python3 - <<'EOF'
s=open('ajile.py').read()
a=s.index("def match_projection(")
b=s.index("def session_weights(")
s=s[:a]+'''def match_projection(m, positions_known):
    """Rows of a projection matrix matched to the file's electrodes, by the paper's code
    (tfr_utils.load_project_spectral_power, commit 04c6faf): it keeps the rows that are not all
    zero and drops the first of them (`np.nonzero(df.transpose().mean().values != 0)[0][1:]`),
    and applies the rest, in order, to the channels of its power files. Here they are applied,
    in order, to the electrodes whose positions are known (electrodes without a position get
    no weight). Returns (array n_electrodes x regions or None, note)."""
    a = m.values.astype(float)
    keep = np.flatnonzero(a.mean(axis=1) != 0)[1:]
    rows = a[keep]
    n_known = int(positions_known.sum())
    if len(rows) != n_known:
        return None, f"{len(rows)} rows for {n_known} electrodes with positions"
    out = np.zeros((len(positions_known), a.shape[1]))
    out[positions_known] = rows
    return out, f"{len(rows)} rows for {n_known} electrodes with positions"


'''+s[b:]
open('ajile.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python3 - <<'EOF'
s=open('dev_spec.py').read()
s=s.replace("""        n_el=len([x for x in metas if int(x['subject_id'])==s][0]['electrodes'])
        a,how=ajile.match_projection(m,n_el); print(s,m.shape,n_el,how)""","""        el=[x for x in metas if int(x['subject_id'])==s][0]['electrodes']
        a,how=ajile.match_projection(m,el.x.notna().values); print(s,m.shape,len(el),how)""")
open('dev_spec.py','w').write(s)
EOF
date -u; timeout 3000 python -u dev_spec.py 2>&1 | grep -v -i warn; date -u
```

```
Wed Nov 25 06:02:41 UTC 2026
meta 71.9441032409668
1 (99, 116) 94 94 rows for 94 electrodes with positions
2 (87, 116) 86 86 rows for 86 electrodes with positions
3 (97, 116) 96 80 rows for 80 electrodes with positions
4 (85, 116) 84 84 rows for 84 electrodes with positions
5 (107, 116) 106 106 rows for 106 electrodes with positions
6 (81, 116) 80 80 rows for 80 electrodes with positions
7 (65, 116) 64 64 rows for 64 electrodes with positions
8 (93, 116) 92 92 rows for 92 electrodes with positions
9 (127, 116) 126 126 rows for 126 electrodes with positions
10 (127, 116) 126 126 rows for 126 electrodes with positions
11 (107, 116) 106 106 rows for 106 electrodes with positions
12 (125, 116) 124 116 rows for 116 electrodes with positions
  sh = band_stats(dbs - dbs[:, :, BASE].mean(axis=-1, keepdims=True))
  bs = db - db[:, :, BASE].mean(axis=-1, keepdims=True)
  sh = band_stats(dbs - dbs[:, :, BASE].mean(axis=-1, keepdims=True))
  bs = db - db[:, :, BASE].mean(axis=-1, keepdims=True)
  sh = band_stats(dbs - dbs[:, :, BASE].mean(axis=-1, keepdims=True))
  bs = db - db[:, :, BASE].mean(axis=-1, keepdims=True)
[... 5 more lines not kept]
```

**Agent**

Full spectral pass ran in 11.3 min (peak 1.9 GB per worker). Exploring the results before writing the notebook.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0,'entries/peterson-2021')
import ajile
D=pickle.load(open('dev_spec.pkl','rb')); metas=D['metas']; res=D['res']
ev=ajile.event_table(metas)
ev['inside']=np.concatenate([r['inside'] for r in res]); ev['allzero']=np.concatenate([r['allzero'] for r in res])
ev['seg_db']=np.concatenate([r['seg_db'] for r in res]); ev['hf_db']=np.concatenate([r['hf_db'] for r in res])
print(ev.groupby('subject').agg(n=('day','size'),inside=('inside','sum'),allzero=('allzero','sum'),segmin=('seg_db','min'),segmed=('seg_db','median'),hfmed=('hf_db','median'),hfsd=('hf_db','std')))
thr=ev.groupby('subject').hf_db.transform(lambda x: x.mean()+3*x.std())
ev['hf_bad']=ev.hf_db>thr
ev['lowpow']=ev.seg_db<0
ev['keep']=ev.inside & ~ev.allzero & ~ev.lowpow & ~ev.hf_bad
print(ev.groupby('subject')[['hf_bad','lowpow','keep']].sum())
k=ev.groupby('subject').keep.sum(); print(k.min(),k.max(),k.median())
# alternative: pooled 3SD over all segments
thr2=ev.hf_db.mean()+3*ev.hf_db.std(); k2=(ev.inside&~ev.allzero&~ev.lowpow&(ev.hf_db<=thr2)).groupby(ev.subject).sum(); print(k2.values,k2.min(),k2.max(),k2.median())
# precentral response
R=np.concatenate([r['region'] for r in res]); print(R.shape)
bs=R-R[...,ajile.BASE].mean(-1,keepdims=True)
for s in range(1,13):
    m=(ev.subject==s)&ev.keep
    med=np.nanmedian(bs[m.values,1],0)
    print(s, np.round(med[ajile.LFB][:, ajile.WIN].mean(),2), np.round(med[ajile.HFB][:, ajile.WIN].mean(),2))
EOF
```

```
n  inside  allzero    segmin     segmed      hfmed      hfsd
subject                                                                
1        741     609        0  6.686532   9.140452 -10.283821  0.649185
2        305     305        0  9.641773  13.835800 -10.966133  0.968590
3        642     642        0  8.225174  11.151647 -10.861366  2.023666
4        417     395        0  6.144314   7.703697 -10.713440  0.907139
5        267     267        0  8.087405  11.721268 -10.817744  1.880007
6        956     873        0  8.010738  10.119283  -6.305089  2.630164
7        800     800        0  8.605080  11.549769  -9.945867  0.383008
8        965     965        0  4.969142   6.535867  -9.425217  0.780416
9        211     211        0  5.565672  10.692827 -14.934697  1.014697
10       806     806        0  6.594260  11.143776 -11.960049  0.930103
11       982     982        0 -9.466383  13.504057  -8.674952  2.102651
12       996     996        0  6.825577  10.351387 -12.265086  0.463590
         hf_bad  lowpow  keep
subject                      
1             0       0   609
2             6       0   299
3             5       0   637
4             0       0   395
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -n "def _forward_selected_new" -A45 regression_utils.py | head -70; grep -n "def train_test_split_day_balance" -A30 regression_utils.py | head -40
```

```
161:def _forward_selected_new(data, response,d_val=False):
162-    """Linear model designed by forward selection. 
163-    Obtained at https://planspace.org/20150423-forward_selection_with_statsmodels/
164-
165-    Parameters:
166-    -----------
167-    data : pandas DataFrame with all possible predictors and response
168-
169-    response: string, name of response column in data
170-
171-    Returns:
172-    --------
173-    selected: "optimal" features
174-               selected by forward selection
175-               evaluated by adjusted R-squared
176-    """
177-    remaining = set(data.columns)
178-    remaining.remove(response)
179-    selected = []
180-    current_score, best_new_score = 0.0, 0.0
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -n "get_dummies\|one_hot\|OneHot\|HuberRegressor\|_forward_selected_new(\|shuffle\|r2_score\|feat_select_prob\|n_splits\|per_train\|np.log\|time_of_day\|bins" regression_utils.py fit_regression_models.py | head -60
```

```
regression_utils.py:13:from sklearn.linear_model import HuberRegressor
regression_utils.py:97:        df_out[col] = np.log(df_in[col]+1)
regression_utils.py:99:        df_out[col] = np.log(df_in[col])
regression_utils.py:132:def train_test_split_power_inds(n_evs,per_train):
regression_utils.py:137:    np.random.shuffle(len_arr)
regression_utils.py:138:    train_per = int(per_train*n_evs)
regression_utils.py:143:def train_test_split_day_balance(day_lst, per_train):
regression_utils.py:150:    n_test_day = int(((1-per_train)*len(day_lst))//len(day_uni))
regression_utils.py:155:        np.random.shuffle(len_arr)
regression_utils.py:161:def _forward_selected_new(data, response,d_val=False):
regression_utils.py:245:    t_ave = config.constants_regress['t_ave'] #time bins to average over (in sec)
regression_utils.py:252:    feat_select_prob = np.zeros([max_chan_num,n_feats,n_freqs,n_perms])
regression_utils.py:281:        #Crop power data and average across time bins
regression_utils.py:285:            power_prev_t_ave = np.median(power_prev.data,axis=-1) #average across time bins
regression_utils.py:288:        power_subj_t_ave = np.median(power_subj.data,axis=-1) #average across time bins
regression_utils.py:293:        f_inds_lo = np.nonzero(np.logical_and(power_subj.freqs>=f_ave_lo[0],power_subj.freqs<=f_ave_lo[1]))[0]
regression_utils.py:294:        f_inds_hi = np.nonzero(np.logical_and(power_subj.freqs>=f_ave_hi[0],power_subj.freqs<=f_ave_hi[1]))[0]
regression_utils.py:304:        one_hot = pd.get_dummies(df_metadata_all['day'])
regression_utils.py:312:        tod_one_hot = pd.DataFrame(np.asarray(tod).T,columns=['morning','afternoon','evening'])
regression_utils.py:320:            for day_col in one_hot.columns:
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && sed -n 336,412p regression_utils.py
```

```
power_prev_t_ave[...,0] = np.median(power_prev_t_ave_cp[...,f_inds_lo_prev],axis=-1)
            power_prev_t_ave[...,1] = np.median(power_prev_t_ave_cp[...,f_inds_hi_prev],axis=-1)
        
        #Find train and validation (last day) indices
#         train_inds,val_inds = train_test_split_power_inds(df_metadata_std.shape[0],per_train=.9)
        train_inds,val_inds = train_test_split_day_balance(day_lst,per_train=.8)
        
        #Perform regressions
        coef_inds_keep = len(set(df_metadata_std.columns.tolist()).intersection(feats2use))-1
        for elec_ind in tqdm(range(power_subj_t_ave.shape[1])):
            for freq_i in range(power_subj_t_ave.shape[-1]):
                df_copy = df_metadata_std.copy()
                df_copy = df_copy.drop('patient_id',axis=1)
                df_copy.columns = df_copy.columns.astype(str)
                
                #Forward selection to select only the most important features
                df_forward = df_copy.copy()
                df_forward['power'] = power_subj_t_ave[:,elec_ind,freq_i]
                new_colnames = []
                for col_val in df_forward.columns:
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python3 - <<'EOF'
s=open('ajile.py').read()
a=s.index("def forward_select(")
b=s.index("def day_balanced_splits(")
s=s[:a]+'''def forward_select(X, y):
    """Forward selection over single columns by OLS adjusted R2, starting from 0 and adding the
    best column while the score improves (code regression_utils._forward_selected_new, which
    selects among the columns of the design, one-hot day and time-of-day columns one by one).
    Runs on all of the subject's events, as the code does. Returns a boolean mask of columns."""
    n, p = X.shape
    chosen = np.zeros(p, bool)
    current = 0.0
    yc = y - y.mean()
    sst = yc @ yc
    while not chosen.all():
        best, best_j = -np.inf, None
        for j in np.flatnonzero(~chosen):
            sel = chosen.copy()
            sel[j] = True
            A = np.column_stack([np.ones(n), X[:, sel]])
            beta, *_ = np.linalg.lstsq(A, y, rcond=None)
            res = y - A @ beta
            k = sel.sum()
            adj = 1 - (res @ res / sst) * (n - 1) / (n - k - 1)
            if adj > best:
                best, best_j = adj, j
        if best > current:
            chosen[best_j] = True
            current = best
        else:
            break
    return chosen


'''+s[b:]
a=s.index("def fit_models(")
s=s[:a]+'''def fit_models(X, names, y, splits, chosen, delta=False, shuffle_rng=None, code_shuffle=False):
    """Huber models (sklearn HuberRegressor defaults, code) on the chosen columns over the
    splits. Returns the mean test R2, the mean coefficients (0 for columns not chosen) and,
    when delta is True, the mean Delta R2 per feature: the model refit with the feature's
    columns shuffled in the training events and scored on the unshuffled test events
    (Methods); with code_shuffle the test events are shuffled too and scored shuffled (code).
    A feature with no chosen column gets Delta R2 0 (code: its columns are zero)."""
    from sklearn.linear_model import HuberRegressor
    feats = list(dict.fromkeys(names))
    Xs = X[:, chosen]
    nsel = names[chosen]
    r2s, coefs = [], []
    dr2 = {f: [] for f in feats}
    for test in splits:
        tr = ~test
        if chosen.sum() == 0:
            pred = np.full(test.sum(), np.mean(y[tr]))
            r2s.append(r2(y[test], pred))
            coefs.append(np.zeros(X.shape[1]))
            if delta:
                for f in feats:
                    dr2[f].append(0.0)
            continue
        m = HuberRegressor().fit(Xs[tr], y[tr])
        full = r2(y[test], m.predict(Xs[test]))
        r2s.append(full)
        c = np.zeros(X.shape[1])
        c[chosen] = m.coef_
        coefs.append(c)
        if delta:
            for f in feats:
                cols = nsel == f
                if not cols.any():
                    dr2[f].append(0.0)
                    continue
                Xtr = Xs[tr].copy()
                perm = shuffle_rng.permutation(tr.sum())
                Xtr[:, cols] = Xtr[perm][:, cols]
                Xte = Xs[test].copy()
                if code_shuffle:
                    pt = shuffle_rng.permutation(test.sum())
                    Xte[:, cols] = Xte[pt][:, cols]
                ms = HuberRegressor().fit(Xtr, y[tr])
                dr2[f].append(full - r2(y[test], ms.predict(Xte)))
    out = dict(r2=float(np.mean(r2s)), coef=np.mean(coefs, axis=0))
    if delta:
        out["delta"] = {f: float(np.mean(v)) for f, v in dr2.items()}
    return out


def retention(chosen, names):
    """Per feature, 1 when kept by forward selection; a day or time-of-day column counts as
    1 / number of its columns (code feat_select_prob)."""
    out = {}
    for f in dict.fromkeys(names):
        cols = names == f
        out[f] = float(chosen[cols].sum() / cols.sum())
    return out


def coef_summary(coef, names):
    """Coefficient per feature; for day and time of day the SD of their one-hot coefficients
    (Figure 6 legend; code np.std over those coefficients)."""
    out = {}
    for f in dict.fromkeys(names):
        c = coef[names == f]
        out[f] = float(np.std(c)) if f in ("day", "time_of_day") else float(c[0])
    return out


def regress_subject(args):
    """All models of one subject. args: dict with X, names, Y (n_ev, n_el, n_targets), days,
    seed, target names, which targets get Delta R2. Returns a list of per-model dicts."""
    import os
    os.environ["OMP_NUM_THREADS"] = "1"
    X, names, Y, days, seed = args["X"], args["names"], args["Y"], args["days"], args["seed"]
    rng = np.random.default_rng(seed)
    splits90 = day_balanced_splits(days, 200, 0.1, rng)
    splits80 = day_balanced_splits(days, 200, 0.2, np.random.default_rng(seed + 1))
    shuf = np.random.default_rng(seed + 2)
    out = []
    for k in range(Y.shape[1]):
        for t, tname in enumerate(args["targets"]):
            y = Y[:, k, t]
            chosen = forward_select(X, y)
            row = dict(subject=args["subject"], electrode=args["electrodes"][k], target=tname,
                       retention=retention(chosen, names))
            if tname in args["main_targets"]:
                main = fit_models(X, names, y, splits90, chosen)
                row["r2"] = main["r2"]
                row["coef"] = coef_summary(main["coef"], names)
                row["r2_80"] = fit_models(X, names, y, splits80, chosen)["r2"]
                if main["r2"] > args["delta_min_r2"]:
                    row["delta"] = fit_models(X, names, y, splits90, chosen, delta=True, shuffle_rng=shuf)["delta"]
                    row["delta_code"] = fit_models(X, names, y, splits80, chosen, delta=True, shuffle_rng=shuf,
                                                   code_shuffle=True)["delta"]
            else:
                row["r2"] = fit_models(X, names, y, splits90, chosen)["r2"]
            out.append(row)
    return out
'''
open('ajile.py','w').write(s)
EOF
python3 -c "import ast;ast.parse(open('entries/peterson-2021/ajile.py').read())"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
s=open('ajile.py').read()
s=s.replace('''    out = []
    for k in range(Y.shape[1]):
        for t, tname in enumerate(args["targets"]):''','''    out = []
    for k in range(Y.shape[1]):
        r2_lfb = -np.inf
        for t, tname in enumerate(args["targets"]):''')
s=s.replace('''                row["r2_80"] = fit_models(X, names, y, splits80, chosen)["r2"]
                if main["r2"] > args["delta_min_r2"]:''','''                row["r2_80"] = fit_models(X, names, y, splits80, chosen)["r2"]
                if tname.startswith("lfb"):
                    r2_lfb = main["r2"]
                # Delta R2 where the band's own R2 passes, or the LFB R2 (the code's selection)
                if max(main["r2"], r2_lfb) > args["delta_min_r2"]:''')
s+='''

def run_regression(jobs, workers=4):
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn")) as ex:
        return [r for rows in ex.map(regress_subject, jobs) for r in rows]
'''
open('ajile.py','w').write(s)
EOF
date -u
```

```
Wed Nov 25 06:16:37 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0,'entries/peterson-2021')
import ajile
D=pickle.load(open('dev_spec.pkl','rb')); metas=D['metas']; res=D['res']
ev=ajile.event_table(metas)
W=[];
for m,r in zip(metas,res):
    w='R_Wrist' if m['event_wrist']=='r_wrist' else 'L_Wrist'
    W.append(r['wrist'][w])
W=np.concatenate(W); t=res[0]['wrist_t']
on=W[:,45,:]
ang_img=[];mag=[]
for i in range(len(ev)):
    n=int(min(ev.duration[i],1.5)*30)
    seg=W[i,45:46+n]-on[i]
    d=np.hypot(seg[:,0],seg[:,1]); j=np.nanargmax(d) if np.isfinite(d).any() else 0
    ang_img.append(np.degrees(np.arctan2(seg[j,1],seg[j,0]))); mag.append(d[j])
ang_img=np.array(ang_img); mag=np.array(mag)
ok=(ev.duration<=1.5)&np.isfinite(ang_img)
def angdiff(a,b): return np.abs((a-b+180)%360-180)
print('n',ok.sum(),'img med diff',np.median(angdiff(ang_img[ok],ev.angle_raw[ok])),'neg med diff',np.median(angdiff(-ang_img[ok],ev.angle_raw[ok])))
print('mag ratio median',np.nanmedian(mag[ok]/ev.magnitude[ok]))
print(ev.groupby('subject').angle_raw.describe())
for m in metas[:12:3]: print(m['groups'])
EOF
```

```
n 6376 img med diff 1.5759565982105812 neg med diff 116.4926953160458
mag ratio median 1.007053868259317
         count       mean         std  ...        50%        75%         max
subject                                ...                                  
1        741.0 -31.133238   99.011174  ... -72.884028  64.161742  179.798287
2        305.0 -26.746851  112.533733  ... -53.267709  55.624486  179.848348
3        642.0 -37.495090   94.501172  ... -68.018495  17.278862  179.584053
4        417.0 -50.232406   92.196025  ... -77.129377   0.949352  177.568122
5        267.0 -32.398977   99.208807  ... -61.058089  51.210429  177.404785
6        956.0 -39.035932  100.847919  ... -72.930691  20.069786  179.795000
7        800.0 -32.221372   82.967902  ... -57.796102   9.135445  178.111611
8        965.0 -24.131707   92.716264  ... -59.004282  57.224266  179.552642
9        211.0 -20.165847  102.949459  ... -35.780812  68.894630  178.871669
10       806.0 -15.688842  102.852709  ... -31.011545  75.123299  179.352470
11       982.0 -42.191910   91.900012  ... -77.723721   1.341958  179.695472
12       996.0 -43.074778   92.098231  ... -77.710139  32.344331  179.289704

[12 rows x 8 columns]
{'ECG': 'electrocardiogram', 'EOG': 'electrooculogram', 'GRID': 'ECoG grid', 'LAT': 'left anterior temporal', 'LID': 'left insular depth', 'LMT': 'left medial temporal', 'LPT': 'left posterior temporal', 'LTO': 'left temporal occipital'}
{'ECG': 'electrocardiogram', 'EOG': 'electrooculogram', 'GRID': 'ECoG grid', 'LAT': 'left anterior temporal', 'LID': 'left insular depth', 'LMT': 'left medial temporal', 'LPT': 'left posterior temporal', 'LTO': 'left temporal occipital'}
[... 3 more lines not kept]
```

**Agent**

The stored reach angle matches the image-coordinate angle from the pose (median difference 1.6°), so it must be negated before folding, as the paper's code does. Writing the notebook now.

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python3 - <<'EOF'
s=open('ajile.py').read()
s=s.replace('''    ev["angle_raw"] = ev.Reach_angle_degrees''','''    ev["angle_raw"] = ev.Reach_angle_degrees
    # The stored angle is in image coordinates (y grows downward; checked against the pose in
    # the notebook). The code negates it before folding, so that +90 is upward (Methods).
    ev["angle"] = fold_angle(-ev.Reach_angle_degrees.values)''')
s=s.replace('''        "angle": fold_angle(ev.angle_raw.values),''','''        "angle": ev.angle.values,''')
open('ajile.py','w').write(s)
EOF
grep -n '"angle"' ajile.py
```

```
69:FEATURES = ["day", "time_of_day", "duration", "magnitude", "angle", "onset_speed",
176:    ev["angle"] = fold_angle(-ev.Reach_angle_degrees.values)
442:        "angle": ev.angle.values,
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat as nbf\nimport sys\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip()))\n\n\ndef code(s, tags=()):\n    c = nbf.v4.new_code_cell(s.strip())\n    if tags:\n        c.metadata[\"tags\"] = list(tags)\n    cells.append(c)\n\n\nmd(open(\"/tmp/claude-1001/header.md\").read())\n\ncode(r'''\nimport os, re, time, zlib, resource\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport matplotlib.pyplot as plt\nimport ajile\n\nKEY = \"peterson-2021\"\ndef seed(claim):\n    \"\"\"Seed of a claim's generator (protocol, author step 3).\"\"\"\n    return zlib.crc32(f\"{KEY}/{claim}\".encode())\nSEED_OFFSETS = [0, 1000, 2000, 3000, 4000]\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\nT0 = time.time()\nprint(\"dandiset\", ajile.DANDISET, \"version\", ajile.VERSION)\n''')\n\ncode(r'''\n# LOAD-META: list the assets of the pinned version and read every file's small datasets (streamed)\nassets = ajile.list_assets()\nmetas = ajile.load_all_meta(assets)\nprint(len(assets), \"files,\", assets[\"size\"].sum() / 1e9, \"GB in all\")\n''')\n\ncode(r'''\nev_all = ajile.event_table(metas)\nsubjects = sorted(ev_all.subject.unique())\nprint(\"subjects:\", subjects)\ndays = ev_all.groupby(\"subject\").day.unique().map(sorted)\nprint(\"days per subject:\", days.to_dict())\nfor m in metas[:1]:\n    print(\"session_description:\", m[\"session_description\"])\n# Per-file facts\nrows = []\nfor m in metas:\n    el = m[\"electrodes\"]\n    rows.append(dict(subject=int(m[\"subject_id\"]), day=int(m[\"session_id\"]), sex=m[\"sex\"], age=m[\"age\"],\n                     start=m[\"session_start\"][:10], ecog_hours=m[\"ecog_shape\"][0] / m[\"ecog_rate\"] / 3600,\n                     n_el=m[\"ecog_shape\"][1], n_el_table=len(el), good=int(el.good.sum()),\n                     no_position=int(el.x.isna().sum()), events=len(m[\"reaches\"]), event_wrist=m[\"event_wrist\"],\n                     pose_hours=m[\"pose_shape\"][0] / m[\"pose_rate\"] / 3600,\n                     events_after_ecog_end=int((m[\"event_times\"] + 5 > m[\"ecog_shape\"][0] / m[\"ecog_rate\"]).sum())))\nfiles = pd.DataFrame(rows)\nprint(files.to_string())\n''', tags=(\"sanity\",))\n\ncode(r'''\n# Checks of the description against the values\nm0 = metas[0]\nprint(\"ECoG unit:\", m0[\"ecog_unit\"], \"conversion:\", m0[\"ecog_conversion\"], \"rate:\", m0[\"ecog_rate\"], \"start:\", m0[\"ecog_start\"],\n      \"chunks:\", m0[\"ecog_chunks\"])\nprint(\"pose unit:\", m0[\"pose_unit\"], \"rate:\", m0[\"pose_rate\"], \"series:\", m0[\"pose_series\"])\nprint(\"all ECoG at 500 Hz:\", all(m[\"ecog_rate\"] == 500 for m in metas), \"; all pose at 30 Hz:\", all(m[\"pose_rate\"] == 30 for m in metas))\nprint(\"ElectricalSeries rows = electrodes table:\", all(m[\"ecog_shape\"][1] == len(m[\"electrodes\"]) and\n      np.array_equal(m[\"es_electrodes\"], np.arange(len(m[\"electrodes\"]))) for m in metas))\nprint(\"ReachEvents timestamps = reaches start_time (max diff, s):\",\n      max(np.abs(m[\"event_times\"] - m[\"reaches\"].start_time.values).max() for m in metas))\n# electrode positions and flags across a subject's files\nfor s in subjects:\n    ms = [m for m in metas if int(m[\"subject_id\"]) == s]\n    xyz = [m[\"electrodes\"][[\"x\", \"y\", \"z\"]].values for m in ms]\n    same = all(np.array_equal(a, xyz[0], equal_nan=True) for a in xyz)\n    G = np.array([m[\"electrodes\"].good.values for m in ms])\n    print(f\"S{s:02d}: positions identical across files {same}; electrodes without position {int(np.isnan(xyz[0][:, 0]).sum())}; \"\n          f\"bad per file {list((~G).sum(1))}; bad in every file {(~G).all(0).sum()}; bad in any file {(~G).any(0).sum()}\")\nprint(\"columns of the reaches table:\", list(metas[0][\"reaches\"].columns))\nprint(\"columns of the electrodes table:\", list(metas[0][\"electrodes\"].columns))\nprint(\"columns of the epochs table:\", list(metas[0][\"epochs\"].columns))\ndesc = ev_all[[\"duration\", \"magnitude\", \"angle_raw\", \"onset_speed\", \"speech_ratio\", \"Bimanual_ratio\", \"bimanual_overlap\",\n               \"bimanual_class\", \"time_of_day\"]].describe().T\nprint(desc)\nprint(\"missing values per reaches column:\", ev_all[[\"Reach_magnitude_px\", \"Reach_angle_degrees\", \"Onset_speed_px_per_sec\",\n      \"Speech_ratio\", \"Bimanual_ratio\", \"Bimanual_overlap\", \"Bimanual_class\"]].isna().sum().to_dict())\nprint(\"bimanual_class values:\", sorted(ev_all.bimanual_class.unique()))\n''', tags=(\"sanity\",))\n\ncode(r'''\n# Coarse behavioural labels (epochs) at the event times. The Methods exclude movements during\n# sleep, unrelated experiments and private times.\nlab = []\nfor m in metas:\n    ep = m[\"epochs\"]\n    for t in m[\"event_times\"]:\n        k = np.flatnonzero((ep.start_time.values <= t) & (ep.stop_time.values > t))\n        lab.append(ep.labels.values[k[0]] if len(k) else \"(none)\")\nev_all[\"epoch_label\"] = lab\nprint(ev_all.epoch_label.value_counts().to_string())\n''', tags=(\"sanity\",))\n\nmd(r'''\n## Projection matrices (outside input) and claim `roi-projection-link`\n\n> The rows of the paper's projection matrices from electrodes to the eight regions, deposited on\n> Figshare, can be matched one to one to the dataset's electrodes, and their weights fit the\n> electrodes' positions.\n\nFigshare item 12114408, version 1 (doi:10.6084/m9.figshare.12114408.v1), read at run time. Rows are\nmatched as the paper's code does (`tfr_utils.load_project_spectral_power`, commit 04c6faf): it keeps\nthe non-zero rows and drops the first of them (`np.nonzero(df.transpose().mean().values != 0)[0][1:]`).\n''')\n\ncode(r'''\nfiles, fig_meta = ajile.figshare_files()\nprint(\"Figshare item\", fig_meta[\"id\"], \"version\", fig_meta[\"version\"], fig_meta[\"doi\"])\nproj, cents, link_rows = {}, {}, []\nel_first = {s: [m for m in metas if int(m[\"subject_id\"]) == s][0][\"electrodes\"] for s in subjects}\nfor s in subjects:\n    m, c = ajile.load_projection(s, files)\n    el = el_first[s]\n    known = el.x.notna().values\n    a, note = ajile.match_projection(m, known)\n    # rule as the claims file words it: drop all-zero rows only\n    allz = m.values.astype(float)\n    n_nonzero = int((allz.mean(axis=1) != 0).sum())\n    proj[s] = (list(m.columns), a)\n    cents[s] = c\n    link_rows.append(dict(subject=s, csv_rows=len(m), electrodes=len(el), with_position=int(known.sum()),\n                          nonzero_rows=n_nonzero, code_rule=note, matched=a is not None))\nlink = pd.DataFrame(link_rows)\nprint(link.to_string())\ncols_all = proj[1][0]\n# regions kept: mean electrode density over subjects > 3 (Methods)\ndens = np.array([proj[s][1].sum(axis=0) for s in subjects]).mean(axis=0)\nkept = [cols_all[i] for i in np.flatnonzero(dens > 3)]\nprint(\"regions with mean density > 3:\", kept)\nprint(\"same as the eight of the claims file:\", sorted(kept) == sorted(ajile.ROIS))\n''', tags=(\"claim:roi-projection-link\",))\n\ncode(r'''\n# Largest-weight region against the nearest region centroid, with mirrored MNI positions\nrng = np.random.default_rng(seed(\"roi-projection-link\"))\ndef nearest_match(s, rng=None, n_shuffle=200):\n    names, a = proj[s]\n    c = cents[s]\n    cn = [str(x) for x in c.columns]\n    cent = c.values.astype(float)            # one row per AAL region, left-side centroids\n    el = el_first[s]\n    known = el.x.notna().values\n    pos = el[[\"x\", \"y\", \"z\"]].values[known].copy()\n    pos[:, 0] = -np.abs(pos[:, 0])             # mirror to the left hemisphere\n    W = a[known]\n    has = W.sum(axis=1) > 0\n    valid = np.isfinite(cent).all(axis=1) & (np.abs(cent).sum(axis=1) > 0)\n    d = np.linalg.norm(pos[:, None, :] - cent[None, :, :], axis=2)\n    d[:, ~valid] = np.inf\n    near = d.argmin(axis=1)\n    top = np.where(valid[None, :], W, -np.inf).argmax(axis=1)\n    obs = int((near[has] == top[has]).sum())\n    null = []\n    for _ in range(n_shuffle):\n        p = rng.permutation(len(W))\n        topp = np.where(valid[None, :], W[p], -np.inf).argmax(axis=1)\n        null.append(int((near[has] == topp[has]).sum()))\n    return obs, int(has.sum()), np.array(null)\nprint(\"centroid table shape:\", cents[1].shape, \"columns:\", list(cents[1].columns))\nres_link = []\nfor s in subjects:\n    obs, n, null = nearest_match(s, rng)\n    res_link.append(dict(subject=s, matched_electrodes=n, top_is_nearest=obs, frac=obs / n,\n                         shuffled_mean=null.mean(), shuffled_max=null.max(), beats_all_shuffles=obs > null.max()))\nres_link = pd.DataFrame(res_link)\nprint(res_link.to_string())\n# seed sensitivity\nfor off in SEED_OFFSETS[1:]:\n    r2_ = np.random.default_rng(seed(\"roi-projection-link\") + off)\n    print(\"seed +\", off, \"subjects beating every shuffle:\", sum(nearest_match(s, r2_)[0] > nearest_match(s, r2_)[2].max() for s in subjects))\nn_ok = int((link.matched & res_link.beats_all_shuffles).sum())\nprint(\"subjects with rows = electrodes and positions fitting the weights:\", n_ok, \"of 12\")\n''', tags=(\"claim:roi-projection-link\",))\n\nmd(r'''\n**Result: ...** (link)\n''')\n\nmd(r'''\n## Spectral power of every event (streamed)\n\nFor each file, the chunk index of the ECoG series is read from the file's B-tree, and the chunks\nholding the 10 s around each event are fetched and decoded. The helper's docstring gives the source\nof every parameter. Every event's segment is checked by the Methods' rule, and its power is\nprojected to the eight regions with the weights of that file's good electrodes.\n''')\n\ncode(r'''\n# SPECTRAL\nt = time.time()\nroi_idx = [cols_all.index(r) for r in ajile.ROIS]\njobs = []\nfor m in metas:\n    s = int(m[\"subject_id\"])\n    good = m[\"electrodes\"].good.values.astype(bool)\n    w = ajile.session_weights(proj[s][1][:, roi_idx], good)\n    jobs.append((m[\"asset_id\"], m[\"event_times\"], good, w))\nspec = ajile.run_spectral(jobs, workers=8)\nprint(f\"spectral pass {time.time() - t:.0f} s; peak memory of a worker \"\n      f\"{resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1e6:.2f} GB\")\n''')\n\ncode(r'''\nev = ev_all.copy()\nev[\"inside\"] = np.concatenate([r[\"inside\"] for r in spec])\nev[\"allzero\"] = np.concatenate([r[\"allzero\"] for r in spec])\nev[\"seg_db\"] = np.concatenate([r[\"seg_db\"] for r in spec])\nev[\"hf_db\"] = np.concatenate([r[\"hf_db\"] for r in spec])\nREG = np.concatenate([r[\"region\"] for r in spec])          # (event, region, freq, bin), dB, no baseline\nREG_BS = REG - REG[..., ajile.BASE].mean(axis=-1, keepdims=True)\nELEC = {k: [r[\"elec\"][k] for r in spec] for k in spec[0][\"elec\"]}  # per file: (event, electrode)\nhf_thr = ev[ev.inside].groupby(\"subject\").hf_db.agg(lambda x: x.mean() + 3 * x.std())\nev[\"hf_bad\"] = ev.hf_db > ev.subject.map(hf_thr)\nev[\"low_power\"] = ev.seg_db < 0\nev[\"keep\"] = ev.inside & ~ev.allzero & ~ev.low_power & ~ev.hf_bad\ndrop = ev.groupby(\"subject\").agg(events=(\"keep\", \"size\"), no_ecog=(\"inside\", lambda x: int((~x).sum())),\n                                 zeroed=(\"allzero\", \"sum\"), below_0dB=(\"low_power\", \"sum\"),\n                                 hf_3sd=(\"hf_bad\", \"sum\"), kept=(\"keep\", \"sum\"))\nprint(drop.to_string())\nprint(\"segment power (dB, uV^2/Hz, mean 1-200 Hz): range\", np.nanmin(ev.seg_db).round(2), \"to\", np.nanmax(ev.seg_db).round(2))\nprint(\"region power without baseline (dB): range\", np.nanmin(REG).round(1), \"to\", np.nanmax(REG).round(1))\nprint(\"NaN region values among kept events:\", int(np.isnan(REG[ev.keep.values]).sum()))\n''', tags=(\"sanity\",))\n\ncode(r'''\n# Clock check: event-locked band power at the true onsets against a pseudo-onset 3 s earlier in the\n# same segments (same electrodes, same events). Precentral-weighted mean over good electrodes.\nrows = []\nfor s in subjects:\n    lf, hf, lfs, hfs = [], [], [], []\n    for m, r in zip(metas, spec):\n        if int(m[\"subject_id\"]) != s:\n            continue\n        k = ev[(ev.asset_id == m[\"asset_id\"])].keep.values\n        good = m[\"electrodes\"].good.values.astype(bool)\n        w = ajile.session_weights(proj[s][1][:, roi_idx], good)[:, 1]\n        w = np.nan_to_num(w)\n        for key, lst in ((\"lfb_mean\", lf), (\"hfb_mean\", hf), (\"lfb_mean_shift\", lfs), (\"hfb_mean_shift\", hfs)):\n            lst.append(np.nansum(r[\"elec\"][key][k] * w[None, :], axis=1))\n    lf, hf, lfs, hfs = map(np.concatenate, (lf, hf, lfs, hfs))\n    rows.append(dict(subject=s, lfb_onset=np.median(lf), lfb_pseudo=np.median(lfs),\n                     hfb_onset=np.median(hf), hfb_pseudo=np.median(hfs),\n                     p_hfb=stats.wilcoxon(hf, hfs).pvalue, p_lfb=stats.wilcoxon(lf, lfs).pvalue))\nclock = pd.DataFrame(rows)\nprint(clock.round(4).to_string())\n# Pose: contralateral wrist speed around onset\nspd = []\nfor m, r in zip(metas, spec):\n    w = \"R_Wrist\" if m[\"event_wrist\"] == \"r_wrist\" else \"L_Wrist\"\n    p = r[\"wrist\"][w]\n    spd.append(np.linalg.norm(np.diff(p, axis=1), axis=2) * 30)\nspd = np.concatenate(spd)\ntt = spec[0][\"wrist_t\"][1:]\nprint(\"median contralateral wrist speed (px/s) at -1.0, -0.5, 0, +0.25, +0.5 s:\",\n      [round(float(np.nanmedian(spd[:, np.argmin(np.abs(tt - x))])), 1) for x in (-1.0, -0.5, 0.0, 0.25, 0.5)])\n''', tags=(\"sanity\",))\n\ncode(r'''\n# Reach angle convention: the stored angle against the angle of the wrist's largest displacement\n# from its onset position, computed from the pose (events up to 1.5 s long, the pose window)\nW = np.concatenate([r[\"wrist\"][\"R_Wrist\" if m[\"event_wrist\"] == \"r_wrist\" else \"L_Wrist\"] for m, r in zip(metas, spec)])\nimg_ang, pmag = np.full(len(ev), np.nan), np.full(len(ev), np.nan)\nfor i in range(len(ev)):\n    if ev.duration.values[i] > 1.5:\n        continue\n    n = int(ev.duration.values[i] * 30)\n    seg = W[i, 45:46 + n] - W[i, 45]\n    d = np.hypot(seg[:, 0], seg[:, 1])\n    if np.isfinite(d).any():\n        j = np.nanargmax(d)\n        img_ang[i] = np.degrees(np.arctan2(seg[j, 1], seg[j, 0]))\n        pmag[i] = d[j]\nok = np.isfinite(img_ang)\nadiff = lambda a, b: np.abs((a - b + 180) % 360 - 180)\nprint(\"events compared:\", ok.sum())\nprint(\"median |stored - image angle (y down)|:\", np.median(adiff(ev.angle_raw.values[ok], img_ang[ok])).round(2), \"deg\")\nprint(\"median |stored - angle with y up|:\", np.median(adiff(ev.angle_raw.values[ok], -img_ang[ok])).round(2), \"deg\")\nprint(\"median pose magnitude / stored magnitude:\", np.median(pmag[ok] / ev.magnitude.values[ok]).round(3))\n''', tags=(\"sanity\",))\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nexec(open(\"/tmp/claude-1001/build_claims.py\").read())\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/peterson-2021/reproduce_peterson_2021.ipynb\")\nprint(len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_claims.py",
 "content": "# Claim sections, appended to `cells` by build_nb.py\n\nmd(r'''\n## Event sets\n\nReading (a): every event in the reaches tables. Reading (b): the events left after the Methods'\nsegment rejection (no ECoG for the whole 10 s segment, zeroed data, power below 0 dB, or 115-125 Hz\npower more than 3 SD above the subject's segments). The dataset has no false-positive flag; the\nMethods say those events were removed by visual inspection, so none are dropped for it here.\n''')\n\ncode(r'''\nEVA = ev\nEVB = ev[ev.keep]\nprint(\"reading a:\", len(EVA), \"events; reading b:\", len(EVB))\n''')\n\n# ---------------------------------------------------------------- subject-days\nmd(r'''\n## subject-days\n\n> The dataset's subjects and recording days are the paper's subjects S01 to S12 and the recording\n> days the paper lists for each.\n''')\ncode(r'''\npaper_days = {1: [3, 4, 5, 7], 2: [3, 4, 5, 6], 3: [3, 4, 5, 6], 5: [3, 4, 7]}\npaper_days = {s: paper_days.get(s, [3, 4, 5, 6, 7]) for s in range(1, 13)}\ncmp = pd.DataFrame({\"paper\": pd.Series(paper_days).map(str), \"dataset\": days.map(lambda d: str([int(x) for x in d]))})\ncmp[\"same\"] = [paper_days[s] == [int(x) for x in days[s]] for s in cmp.index]\nprint(cmp.to_string())\nprint(\"subject-days in the dataset:\", sum(len(d) for d in days), \"; all match:\", cmp.same.all())\n''', tags=(\"claim:subject-days\",))\nmd(\"**Result: ...** (subject-days)\")\n\n# ---------------------------------------------------------------- cohort\nmd(r'''\n## cohort\n\n> Twelve subjects (8 male, 4 female, 29.4 +- 7.9 years) had on average 87.0 +- 12.9 surface\n> electrodes; five also had 23.2 +- 12.1 depth electrodes; five were implanted in the right\n> hemisphere and seven in the left.\n\nSurface electrodes are those of groups whose description is not a depth electrode; depth electrodes\nare those of groups described as depth. The hemisphere is the side of the mean x (MNI) of the\nsubject's electrodes with positions.\n''')\ncode(r'''\nrows = []\nfor s in subjects:\n    m = [x for x in metas if int(x[\"subject_id\"]) == s][0]\n    el = m[\"electrodes\"]\n    gdesc = el.group_name.map(m[\"groups\"]).fillna(\"\")\n    depth = gdesc.str.contains(\"depth\", case=False)\n    rows.append(dict(subject=s, sex=m[\"sex\"], age=int(re.findall(r\"\\d+\", m[\"age\"])[0]), electrodes=len(el),\n                     surface=int((~depth).sum()), depth=int(depth.sum()), mean_x=el.x.mean(),\n                     hemisphere=\"right\" if el.x.mean() > 0 else \"left\",\n                     groups=\", \".join(f\"{g} ({m['groups'].get(g, '?')})\" for g in el.group_name.unique())))\ncoh = pd.DataFrame(rows)\nprint(coh.drop(columns=\"groups\").to_string())\nfor _, r in coh.iterrows():\n    print(f\"S{r.subject:02d}:\", r.groups)\ndsub = coh[coh.depth > 0]\nvals = dict(subjects=len(coh), male=int((coh.sex == \"M\").sum()), mean_age=coh.age.mean(), sd_age=coh.age.std(),\n            mean_surface=coh.surface.mean(), sd_surface=coh.surface.std(), with_depth=len(dsub),\n            mean_depth=dsub.depth.mean(), sd_depth=dsub.depth.std(), right=int((coh.hemisphere == \"right\").sum()))\nprint({k: round(float(v), 2) for k, v in vals.items()})\nexp = [(\"subjects\", 12, 0), (\"male\", 8, 0), (\"mean_age\", 29.4, 7.9), (\"mean_surface\", 87.0, 12.9),\n       (\"with_depth\", 5, 0), (\"mean_depth\", 23.2, 12.1), (\"right\", 5, 0)]\nfor k, v, tol in exp:\n    print(f\"{k}: measured {vals[k]:.2f}, expected {v} +- {tol}: {'within' if abs(vals[k] - v) <= tol else 'OUTSIDE'}\")\n# variant: the grid only as surface (a reading of 'surface' the data do not settle)\n''', tags=(\"claim:cohort\",))\nmd(\"**Result: ...** (cohort)\")\n\n# ---------------------------------------------------------------- event counts\nmd(r'''\n## fig2-event-counts\n\n> Each subject contributed between 151 and 947 movement events (median 640 across subjects).\n''')\ncode(r'''\ncnt = pd.DataFrame({\"a_all\": EVA.groupby(\"subject\").size(), \"b_kept\": EVB.groupby(\"subject\").size(),\n                    \"with_ecog\": ev[ev.inside].groupby(\"subject\").size()})\nprint(cnt.to_string())\nfor col in cnt:\n    c = cnt[col]\n    ok = abs(c.min() - 151) <= 15.1 and abs(c.max() - 947) <= 94.7 and abs(c.median() - 640) <= 64\n    print(f\"{col}: min {c.min()}, max {c.max()}, median {c.median()} -> all three within tolerance: {ok}\")\n''', tags=(\"claim:fig2-event-counts\",))\nmd(\"**Result: ...** (fig2-event-counts)\")\n\n# ---------------------------------------------------------------- features differ\nmd(r'''\n## fig2-features-differ-across-subjects\n\n> All ten behavioural and environmental features differ significantly across subjects.\n''')\ncode(r'''\ndef kw_by_subject(E):\n    out = {}\n    for f in ajile.FEATURES:\n        groups = [g[f].values for _, g in E.groupby(\"subject\")]\n        out[f] = stats.kruskal(*groups)\n    return pd.DataFrame({f: dict(H=r.statistic, p=r.pvalue) for f, r in out.items()}).T\nkwb = kw_by_subject(EVB); kwa = kw_by_subject(EVA)\ntab = kwb.join(kwa, lsuffix=\"_b\", rsuffix=\"_a\")\nprint(tab.to_string(float_format=lambda x: f\"{x:.3g}\"))\nprint(\"reading b: p < 0.001 for all ten:\", (kwb.p < 0.001).all(), \"; reading a:\", (kwa.p < 0.001).all())\nprint(\"largest p (b):\", kwb.p.max(), kwb.p.idxmax())\n''', tags=(\"claim:fig2-features-differ-across-subjects\",))\nmd(\"**Result: ...** (fig2-features-differ-across-subjects)\")\n\n# ---------------------------------------------------------------- reach shape\nmd(r'''\n## fig2-reach-shape\n\n> Reach duration and reach magnitude vary little across subjects, with most reaches lasting under\n> 2 s and covering under 200 pixels, and reach angle distributions tend to be bimodal with peaks near\n> +90 and -90 degrees, with few side-to-side reaches.\n\nAngle density: Gaussian KDE with Scott's bandwidth on the folded angle, evaluated on -90 to 90 in\nsteps of 0.5 degrees (a standard grid). The grid's end points count as local maxima when they exceed\ntheir neighbour, since the folded angle cannot pass +-90 (standard choice, stated).\n''')\ncode(r'''\ngrid = np.arange(-90, 90.01, 0.5)\ndef bimodal(a):\n    d = stats.gaussian_kde(a)(grid)\n    peaks = [i for i in range(len(d)) if (i == 0 or d[i] > d[i - 1]) and (i == len(d) - 1 or d[i] > d[i + 1])]\n    top = sorted(peaks, key=lambda i: -d[i])[:2]\n    pk = sorted(grid[top])\n    d0 = d[np.argmin(np.abs(grid))]\n    ok = len(pk) == 2 and abs(pk[0] + 90) <= 15 and abs(pk[1] - 90) <= 15 and d0 < min(d[top])\n    return ok, pk, d0, [d[i] for i in top]\nrows = []\nfor s, g in list(EVB.groupby(\"subject\")) + [(\"pooled\", EVB)]:\n    ok, pk, d0, dp = bimodal(g.angle.values)\n    rows.append(dict(subject=s, n=len(g), frac_dur_lt2=(g.duration < 2).mean(), median_dur=g.duration.median(),\n                     frac_mag_lt200=(g.magnitude < 200).mean(), median_mag=g.magnitude.median(),\n                     peaks=np.round(pk, 1), dens0=round(d0, 5), dens_peaks=np.round(dp, 5), bimodal_pm90=ok,\n                     frac_side=(np.abs(g.angle) < 30).mean()))\nrs = pd.DataFrame(rows)\nprint(rs.to_string())\nper = rs[rs.subject != \"pooled\"]; pool = rs[rs.subject == \"pooled\"].iloc[0]\ndur_part = pool.frac_dur_lt2 > 0.5 and (per.frac_dur_lt2 > 0.5).sum() >= 10\nmag_part = pool.frac_mag_lt200 > 0.5 and (per.frac_mag_lt200 > 0.5).sum() >= 10\nang_part = pool.bimodal_pm90 and per.bimodal_pm90.sum() > 6\nprint(\"duration part:\", dur_part, (per.frac_dur_lt2 > 0.5).sum(), \"of 12; magnitude part:\", mag_part,\n      (per.frac_mag_lt200 > 0.5).sum(), \"of 12; angle part:\", ang_part, per.bimodal_pm90.sum(), \"of 12\")\nprint(\"ranges: duration\", EVB.duration.min().round(3), \"to\", EVB.duration.max().round(3), \"s; magnitude\",\n      EVB.magnitude.min().round(1), \"to\", EVB.magnitude.max().round(1), \"px\")\n# reading a as a variant\nra = [bimodal(g.angle.values)[0] for _, g in EVA.groupby(\"subject\")]\nprint(\"reading a: bimodal subjects\", sum(ra), \"; pooled\", bimodal(EVA.angle.values)[0],\n      \"; duration<2 s in\", int((EVA.groupby('subject').duration.apply(lambda x: (x < 2).mean()) > 0.5).sum()),\n      \"subjects; magnitude<200 in\", int((EVA.groupby('subject').magnitude.apply(lambda x: (x < 200).mean()) > 0.5).sum()))\n''', tags=(\"claim:fig2-reach-shape\",))\ncode(r'''\nfig, axs = plt.subplots(3, 4, figsize=(12, 7), sharex=True)\nfor ax, (s, g) in zip(axs.ravel(), EVB.groupby(\"subject\")):\n    ax.plot(grid, stats.gaussian_kde(g.angle.values)(grid))\n    ax.set_title(f\"S{s:02d}\", fontsize=9)\nfig.supxlabel(\"folded reach angle (deg, +90 up)\"); fig.supylabel(\"density\"); plt.tight_layout(); plt.show()\nprint(\"all angles lie in -90..90:\", EVB.angle.between(-90, 90).all())\n''', tags=(\"claim:fig2-reach-shape\",))\nmd(\"**Result: ...** (fig2-reach-shape)\")\n\n# ---------------------------------------------------------------- bimanual skew\nmd(r'''\n## fig2-bimanual-skew\n\n> Bimanual ratio and bimanual overlap are skewed toward unimanual movement of the contralateral arm,\n> less so for subjects 02, 04 and 05, while the bimanual class is mostly bimanual.\n''')\ncode(r'''\nrows = []\nfor s, g in list(EVB.groupby(\"subject\")) + [(\"pooled\", EVB)]:\n    rows.append(dict(subject=s, ratio_median=g.bimanual_ratio.median(), overlap_skew=stats.skew(g.bimanual_overlap),\n                     overlap_median=g.bimanual_overlap.median(), class_frac_bimanual=g.bimanual_class.mean()))\nbs_ = pd.DataFrame(rows)\nprint(bs_.to_string())\nper = bs_[bs_.subject != \"pooled\"].set_index(\"subject\"); pool = bs_[bs_.subject == \"pooled\"].iloc[0]\nratio_ok = pool.ratio_median < 0.5 and (per.ratio_median < 0.5).sum() >= 9\nover_ok = pool.overlap_skew > 0 and (per.overlap_skew > 0).sum() >= 9\nclass_ok = pool.class_frac_bimanual > 0.5 and (per.class_frac_bimanual > 0.5).sum() > 6\ntop_ratio = per.ratio_median.sort_values(ascending=False).index[:5].tolist()\nlow_skew = per.overlap_skew.sort_values().index[:5].tolist()\nnamed = [2, 4, 5]\nless_ratio = all(s in top_ratio for s in named); less_over = all(s in low_skew for s in named)\nprint(\"ratio part:\", ratio_ok, int((per.ratio_median < 0.5).sum()), \"of 12; overlap part:\", over_ok,\n      int((per.overlap_skew > 0).sum()), \"of 12; class part:\", class_ok, int((per.class_frac_bimanual > 0.5).sum()), \"of 12\")\nprint(\"five highest median ratios:\", top_ratio, \"-> S02, S04, S05 among them:\", less_ratio)\nprint(\"five lowest overlap skewness:\", low_skew, \"-> S02, S04, S05 among them:\", less_over)\nprint(\"bimanual ratio range\", EVB.bimanual_ratio.min(), EVB.bimanual_ratio.max(), \"; overlap range\",\n      EVB.bimanual_overlap.min(), EVB.bimanual_overlap.max(), \"(the description says a fraction of the contralateral movement)\")\nprint(\"overlap values above 1:\", int((EVB.bimanual_overlap > 1).sum()))\n''', tags=(\"claim:fig2-bimanual-skew\",))\nmd(\"**Result: ...** (fig2-bimanual-skew)\")\n\n# ---------------------------------------------------------------- extfig2-1c\nmd(r'''\n## extfig2-1c-contralateral-larger\n\n> Across all 12 subjects, the median displacement of the contralateral wrist after movement onset is\n> substantially greater than that of the ipsilateral wrist.\n\nContralateral wrist: the wrist named in the ReachEvents description of each file. Pose windows\n-1.5 to +1.5 s at 30 Hz; peak over 0 to 1.5 s of the median over events.\n''')\ncode(r'''\ntw = spec[0][\"wrist_t\"]\ncontra, ipsi = [], []\nfor m, r in zip(metas, spec):\n    c = \"R_Wrist\" if m[\"event_wrist\"] == \"r_wrist\" else \"L_Wrist\"\n    i = \"L_Wrist\" if c == \"R_Wrist\" else \"R_Wrist\"\n    contra.append(r[\"wrist\"][c]); ipsi.append(r[\"wrist\"][i])\ncontra, ipsi = np.concatenate(contra), np.concatenate(ipsi)\nbase = (tw >= -1.5) & (tw <= -1.0); post = (tw >= 0) & (tw <= 1.5); onset = np.argmin(np.abs(tw))\ndef disp(P, reading):\n    ref = np.nanmean(P[:, base], axis=1) if reading == \"a\" else P[:, onset]\n    return np.linalg.norm(P - ref[:, None, :], axis=2)\nrows = []\nkb = ev.keep.values\nfor reading in (\"a\", \"b\"):\n    Dc, Di = disp(contra, reading), disp(ipsi, reading)\n    for s in subjects:\n        sel = kb & (ev.subject.values == s)\n        mc, mi = np.nanmedian(Dc[sel], axis=0), np.nanmedian(Di[sel], axis=0)\n        rows.append(dict(reading=reading, subject=s, n=int(sel.sum()), contra_peak=np.nanmax(mc[post]),\n                         ipsi_peak=np.nanmax(mi[post]), ratio=np.nanmax(mc[post]) / np.nanmax(mi[post])))\ndd = pd.DataFrame(rows)\ndd[\"holds\"] = dd.contra_peak > dd.ipsi_peak\nprint(dd.round(3).to_string())\nprint(dd.groupby(\"reading\").holds.sum())\nprint(\"events with missing pose in the window:\", int(np.isnan(contra[kb]).any(axis=(1, 2)).sum()), \"of\", int(kb.sum()))\n''', tags=(\"claim:extfig2-1c-contralateral-larger\",))\nmd(\"**Result: ...** (extfig2-1c-contralateral-larger)\")\n\n# ---------------------------------------------------------------- correlations\nmd(r'''\n## extfig2-2-feature-correlations\n\n> Over all events, reach magnitude correlates with reach duration (r = 0.26) and onset speed\n> (r = 0.56), reach duration with bimanual overlap (r = 0.48), and the bimanual features with one\n> another (overlap and ratio 0.51, class and ratio 0.50, overlap and class 0.61).\n''')\ncode(r'''\npairs = [(\"magnitude\", \"duration\", 0.26), (\"magnitude\", \"onset_speed\", 0.56), (\"duration\", \"bimanual_overlap\", 0.48),\n         (\"bimanual_overlap\", \"bimanual_ratio\", 0.51), (\"bimanual_class\", \"bimanual_ratio\", 0.50),\n         (\"bimanual_overlap\", \"bimanual_class\", 0.61)]\nrows = []\nfor a_, b_, v in pairs:\n    rb = EVB[[a_, b_]].corr().iloc[0, 1]; ra_ = EVA[[a_, b_]].corr().iloc[0, 1]\n    rows.append(dict(pair=f\"{a_} vs {b_}\", paper=v, r_b=rb, r_a=ra_, within_b=abs(rb - v) <= 0.1 * v + 1e-9,\n                     within_a=abs(ra_ - v) <= 0.1 * v + 1e-9))\ncr = pd.DataFrame(rows)\nprint(cr.round(3).to_string())\nprint(\"within tolerance, reading b:\", int(cr.within_b.sum()), \"of 6; reading a:\", int(cr.within_a.sum()), \"of 6\")\n''', tags=(\"claim:extfig2-2-feature-correlations\",))\nmd(\"**Result: ...** (extfig2-2-feature-correlations)\")\n\n# ---------------------------------------------------------------- days and waking\nmd(r'''\n## fig2-days-and-waking\n\n> Reach counts were fairly even across recording days except for subjects 04, 05 and 09, each with\n> one day holding most events, and events occurred mostly during waking hours.\n''')\ncode(r'''\npc = EVB.groupby([\"subject\", \"day\"]).size().unstack(fill_value=0)\nprint(pc.to_string())\nbusiest = (pc.max(axis=1) / pc.sum(axis=1))\nwake = EVB.groupby(\"subject\").time_of_day.apply(lambda x: ((x >= 8) & (x < 24)).mean())\nout = pd.DataFrame({\"busiest_day_frac\": busiest, \"busiest_day\": pc.idxmax(axis=1), \"waking_frac\": wake})\nprint(out.round(3).to_string())\nover = set(out.index[out.busiest_day_frac > 0.5]); named = {4, 5, 9}\nprint(\"subjects whose busiest day holds > half:\", sorted(over), \"; named S04, S05, S09\")\nprint(\"day part exact:\", over == named, \"; waking part (all subjects > half):\", bool((wake > 0.5).all()))\nprint(\"time of day range (h):\", EVB.time_of_day.min().round(2), \"to\", EVB.time_of_day.max().round(2))\nprint(\"events in 0-8 h by subject:\", EVB[EVB.time_of_day < 8].groupby(\"subject\").size().to_dict())\npa = EVA.groupby([\"subject\", \"day\"]).size().unstack(fill_value=0)\nprint(\"reading a, subjects whose busiest day holds > half:\", sorted(pa.index[(pa.max(axis=1) / pa.sum(axis=1)) > 0.5]))\n''', tags=(\"claim:fig2-days-and-waking\",))\nmd(\"**Result: ...** (fig2-days-and-waking)\")\n\n# ---------------------------------------------------------------- fig3 group\nmd(r'''\n## fig3-group-lfb-decrease-hfb-increase\n\n> At the group level, low-frequency power decreases and high-frequency power increases at movement\n> initiation in several cortical regions.\n\nPer subject, the median over events (reading b) of baseline-subtracted region power; the mean over\nthe 12 subjects; the group mean over -1.5 to -1 s subtracted again. Masking as in the code's\n`tfr_boot_sig_mask` as the claims file gives it: each subject's baseline bins are drawn at random\nwithin frequency, the median over subjects taken, about 2000 values per frequency; two-sided\npercentile p; Benjamini-Hochberg over the region's frequency and time bins (-1.5 to +1.0 s, the\nbins computed here); non-significant values set to 0.\n''')\ncode(r'''\nkbv = ev.keep.values\nsubj_v = ev.subject.values\nSUBJ_MED = np.stack([np.nanmedian(REG_BS[kbv & (subj_v == s)], axis=0) for s in subjects])  # (subj, roi, f, b)\nGROUP = SUBJ_MED.mean(axis=0)\nGROUP = GROUP - GROUP[..., ajile.BASE].mean(axis=-1, keepdims=True)\nbase_idx = np.flatnonzero(ajile.BASE)\n\ndef bh(p, q=0.05):\n    p = p.ravel(); n = len(p); o = np.argsort(p)\n    thr = q * np.arange(1, n + 1) / n\n    ok = p[o] <= thr\n    k = np.max(np.flatnonzero(ok)) + 1 if ok.any() else 0\n    sig = np.zeros(n, bool); sig[o[:k]] = True\n    return sig\n\ndef mask_group(rng, n_boot=2000):\n    masked = np.zeros_like(GROUP)\n    for r in range(GROUP.shape[0]):\n        S = SUBJ_MED[:, r]                                   # (subj, f, b)\n        null = np.empty((n_boot, S.shape[1]))\n        for f in range(S.shape[1]):\n            pick = rng.integers(0, len(base_idx), size=(n_boot, S.shape[0]))\n            vals = S[np.arange(S.shape[0])[None, :], f, base_idx[pick]]\n            null[:, f] = np.median(vals, axis=1)\n        obs = GROUP[r]\n        p = np.empty_like(obs)\n        for f in range(obs.shape[0]):\n            for b in range(obs.shape[1]):\n                p[f, b] = min(1.0, 2 * min((null[:, f] >= obs[f, b]).mean(), (null[:, f] <= obs[f, b]).mean()))\n        sig = bh(p).reshape(obs.shape)\n        masked[r] = np.where(sig, obs, 0.0)\n    return masked\n\nLOW = (ajile.FREQS >= 4) & (ajile.FREQS <= 30); HIGH = (ajile.FREQS >= 50) & (ajile.FREQS <= 120)\nb0 = np.argmin(np.abs(ajile.BIN_T))\ndef fig3_outcome(M):\n    rows = []\n    for r, name in enumerate(ajile.ROI_NAMES):\n        rows.append(dict(region=name, low_a=M[r][LOW][:, ajile.WIN].mean(), high_a=M[r][HIGH][:, ajile.WIN].mean(),\n                         low_b=M[r][LOW][:, b0].mean(), high_b=M[r][HIGH][:, b0].mean()))\n    t = pd.DataFrame(rows).set_index(\"region\")\n    t[\"holds_a\"] = (t.low_a < 0) & (t.high_a > 0); t[\"holds_b\"] = (t.low_b < 0) & (t.high_b > 0)\n    return t\nMASKS = {off: mask_group(np.random.default_rng(seed(\"fig3-group-lfb-decrease-hfb-increase\") + off)) for off in SEED_OFFSETS}\nMASKED = MASKS[0]\nt3 = fig3_outcome(MASKED)\nprint(t3.round(3).to_string())\nnamed3 = [\"precentral\", \"postcentral\", \"inferior parietal\"]\nprint(\"named regions holding under a:\", int(t3.loc[named3, \"holds_a\"].sum()), \"; under b:\", int(t3.loc[named3, \"holds_b\"].sum()))\nprint(\"unmasked group values, same summaries:\")\nprint(fig3_outcome(GROUP).round(3).to_string())\nfor off in SEED_OFFSETS[1:]:\n    tt3 = fig3_outcome(MASKS[off])\n    print(\"seed +\", off, \": named holding a/b:\", int(tt3.loc[named3, \"holds_a\"].sum()), int(tt3.loc[named3, \"holds_b\"].sum()))\nprint(\"fraction of bins significant per region:\", {n: round(float((MASKED[r] != 0).mean()), 3) for r, n in enumerate(ajile.ROI_NAMES)})\n''', tags=(\"claim:fig3-group-lfb-decrease-hfb-increase\",))\ncode(r'''\nfig, axs = plt.subplots(2, 4, figsize=(13, 6), sharex=True, sharey=True)\nlim = np.abs(MASKED).max()\nfor r, ax in enumerate(axs.ravel()):\n    im = ax.pcolormesh(ajile.BIN_T, ajile.FREQS, MASKED[r], cmap=\"RdBu_r\", vmin=-lim, vmax=lim, shading=\"nearest\")\n    ax.set_title(ajile.ROI_NAMES[r], fontsize=9); ax.axvline(0, color=\"k\", lw=0.5)\nfig.colorbar(im, ax=axs, label=\"dB\"); fig.supxlabel(\"time from onset (s)\"); fig.supylabel(\"Hz\"); plt.show()\nprint(\"colour range +-\", round(float(lim), 3), \"dB; masked values range\", MASKED.min().round(3), \"to\", MASKED.max().round(3))\n''', tags=(\"claim:fig3-group-lfb-decrease-hfb-increase\",))\nmd(\"**Result: ...** (fig3-group-lfb-decrease-hfb-increase)\")\n\n# ---------------------------------------------------------------- fig3 largest\nmd(r'''\n## fig3-sensorimotor-largest\n\n> Spectral power changes are largest in precentral, postcentral and inferior parietal regions, and\n> the three temporal regions show minimal movement-related changes.\n''')\ncode(r'''\ntemporal = [\"superior temporal\", \"middle temporal\", \"inferior temporal\"]\ndef largest(M):\n    win_c = (ajile.BIN_T >= -0.5) & (ajile.BIN_T <= 0.5)\n    t = pd.DataFrame({\"a_all_0_0.5\": [np.abs(M[r][:, ajile.WIN]).mean() for r in range(8)],\n                      \"b_low\": [np.abs(M[r][LOW][:, ajile.WIN]).mean() for r in range(8)],\n                      \"b_high\": [np.abs(M[r][HIGH][:, ajile.WIN]).mean() for r in range(8)],\n                      \"c_all_-0.5_0.5\": [np.abs(M[r][:, win_c]).mean() for r in range(8)]}, index=ajile.ROI_NAMES)\n    res = {}\n    for col in [\"a_all_0_0.5\", \"c_all_-0.5_0.5\"]:\n        top3 = t[col].sort_values(ascending=False).index[:3].tolist()\n        res[col] = (sorted(top3) == sorted(named3), sum(n in top3 for n in named3),\n                    all(t.loc[x, col] < t.loc[named3, col].min() for x in temporal), top3)\n    # (b): a region ranks high when it is in the top three in both ranges\n    tl = t.b_low.sort_values(ascending=False).index[:3].tolist(); th = t.b_high.sort_values(ascending=False).index[:3].tolist()\n    both = [n for n in named3 if n in tl and n in th]\n    tmp_ok = all(t.loc[x, \"b_low\"] < t.loc[named3, \"b_low\"].min() and t.loc[x, \"b_high\"] < t.loc[named3, \"b_high\"].min() for x in temporal)\n    res[\"b\"] = (len(both) == 3, len(both), tmp_ok, (tl, th))\n    return t, res\nt3l, r3l = largest(MASKED)\nprint(t3l.round(4).to_string())\nfor k, v in r3l.items():\n    print(f\"reading {k}: three named are the top three {v[0]}; named in top three {v[1]}; temporal below all three {v[2]}; top {v[3]}\")\nfor off in SEED_OFFSETS[1:]:\n    _, rr = largest(MASKS[off])\n    print(\"seed +\", off, {k: (v[0], v[1], v[2]) for k, v in rr.items()})\n''', tags=(\"claim:fig3-sensorimotor-largest\",))\nmd(\"**Result: ...** (fig3-sensorimotor-largest)\")\n\n# ---------------------------------------------------------------- fig3 widespread\nmd(r'''\n## fig3-lfb-more-widespread\n\n> Low-frequency power decreases are more spatially widespread than high-frequency increases and are\n> also present in supramarginal and superior temporal regions.\n''')\ncode(r'''\ndef widespread(M):\n    neg = np.array([(M[r][LOW][:, ajile.WIN] < 0).sum() for r in range(8)])\n    pos = np.array([(M[r][HIGH][:, ajile.WIN] > 0).sum() for r in range(8)])\n    a_ = ((neg > 0).sum(), (pos > 0).sum())\n    b_ = (neg.sum() / LOW.sum(), pos.sum() / HIGH.sum())\n    present = {n: int(neg[ajile.ROI_NAMES.index(n)]) for n in [\"supramarginal\", \"superior temporal\"]}\n    return neg, pos, a_, b_, present\nneg, pos, a_, b_, present = widespread(MASKED)\nprint(pd.DataFrame({\"sig_negative_4_30Hz_bins\": neg, \"sig_positive_50_120Hz_bins\": pos}, index=ajile.ROI_NAMES).to_string())\nprint(\"(a) regions with any: low\", a_[0], \"high\", a_[1], \"-> low larger:\", a_[0] > a_[1])\nprint(\"(b) bins per frequency bin: low\", round(b_[0], 3), \"high\", round(b_[1], 3), \"-> low larger:\", b_[0] > b_[1])\nprint(\"significant negative low-frequency bins in supramarginal / superior temporal:\", present)\nfor off in SEED_OFFSETS[1:]:\n    _, _, aa, bb, pp = widespread(MASKS[off])\n    print(\"seed +\", off, \"a:\", aa, \"b:\", np.round(bb, 3), pp)\n''', tags=(\"claim:fig3-lfb-more-widespread\",))\nmd(\"**Result: ...** (fig3-lfb-more-widespread)\")\n\n# ---------------------------------------------------------------- fig4\nmd(r'''\n## fig4-precentral-subject-variability\n\n> In the precentral region every subject shows the low/high-frequency pattern, but amplitudes and\n> frequency bands vary; subjects 03, 06, 07, 08 and 11 have increases up to 120 Hz, subjects 09 and\n> 12 mainly at 60-80 Hz, and subjects 04 and 08 have narrower low-frequency decreases.\n''')\ncode(r'''\nP = SUBJ_MED[:, 1].copy()                                     # precentral (subj, f, b), unmasked\nP = P - P[..., ajile.BASE].mean(axis=-1, keepdims=True)\nspec4 = P[..., ajile.WIN].mean(axis=-1)                        # (subj, f)\nF = ajile.FREQS\ntab4 = pd.DataFrame(spec4, index=[f\"S{s:02d}\" for s in subjects], columns=[int(f) for f in F])\nprint(tab4.round(2).to_string())\np1 = pd.DataFrame({\"lfb_8_32\": spec4[:, ajile.LFB].mean(1), \"hfb_76_100\": spec4[:, ajile.HFB].mean(1)}, index=tab4.index)\np1[\"holds\"] = (p1.lfb_8_32 < 0) & (p1.hfb_76_100 > 0)\nprint(p1.round(3).to_string())\npart1 = bool(p1.holds.all())\ni116, i121 = list(F).index(116), list(F).index(121)\npart2_rows = {s: (spec4[subjects.index(s), i116] > 0 and spec4[subjects.index(s), i121] > 0) for s in [3, 6, 7, 8, 11]}\npart2 = all(part2_rows.values())\nhi = F >= 56\np3 = {}\nfor s in [9, 12]:\n    v = spec4[subjects.index(s)]\n    fmax = F[hi][np.argmax(v[hi])]; top = v[hi].max()\n    p3[s] = (fmax, round(float(top), 3), round(float(v[(F >= 101)].mean()), 3), 61 <= fmax <= 76 and v[F >= 101].mean() < top / 2)\npart3 = all(x[3] for x in p3.values())\nlow = F <= 46\nwidth = {s: int((spec4[i][low] < spec4[i][low].min() / 2).sum()) for i, s in enumerate(subjects)}\nfewest = sorted(width, key=lambda s: width[s])[:3]\nties = sorted(width.values())[:4]\npart4 = 4 in fewest and 8 in fewest\nprint(\"part 1 (every subject):\", part1, \"; part 2:\", part2_rows, part2, \"; part 3:\", p3, part3)\nprint(\"part 4 widths (bins below half the minimum, 1-46 Hz):\", width, \"; three fewest:\", fewest, \"(four smallest widths:\", ties, \")\", part4)\nprint(\"parts holding:\", sum([part1, part2, part3, part4]), \"of 4\")\n''', tags=(\"claim:fig4-precentral-subject-variability\",))\nmd(\"**Result: ...** (fig4-precentral-subject-variability)\")\n\n# ---------------------------------------------------------------- banded precentral power\nmd(r'''\n## Banded precentral power per event\n\nBand mean (Methods) and band median (code) of baseline-subtracted precentral power over 0 to 0.5 s,\nand the band mean without baseline subtraction (for extfig5-1 and the Discussion claim).\n''')\ncode(r'''\npre = REG[:, 1]\npre_bs = REG_BS[:, 1]\nst_bs = ajile.band_stats(pre_bs); st_raw = ajile.band_stats(pre)\nfor k, v in st_bs.items():\n    ev[\"pre_\" + k] = v\nfor k, v in st_raw.items():\n    ev[\"pre_raw_\" + k] = v\nEVB = ev[ev.keep]\nprint(EVB[[\"pre_lfb_mean\", \"pre_hfb_mean\", \"pre_lfb_median\", \"pre_hfb_median\", \"pre_raw_lfb_mean\", \"pre_raw_hfb_mean\"]].describe().round(3).to_string())\n''')\n\nmd(r'''\n## fig5-band-power-differs-across-subjects\n\n> Precentral LFB and HFB power in the 0.5 s after movement onset differs significantly across subjects.\n''')\ncode(r'''\nfor band in (\"lfb\", \"hfb\"):\n    for st in (\"mean\", \"median\"):\n        g = [x[f\"pre_{band}_{st}\"].values for _, x in EVB.groupby(\"subject\")]\n        r = stats.kruskal(*g)\n        print(f\"{band.upper()} band {st}: H = {r.statistic:.1f}, p = {r.pvalue:.3g}, n = {len(EVB)} events in 12 subjects\")\n''', tags=(\"claim:fig5-band-power-differs-across-subjects\",))\nmd(\"**Result: ...** (fig5-band-power-differs-across-subjects)\")\n\nmd(r'''\n## table1-subject-band-power-ci\n\n> Each subject's precentral band power lies in the 95% bootstrap interval Table 1 gives; LFB power\n> is below baseline and HFB power above it for most subjects.\n''')\ncode(r'''\nT1 = {1: ((-1.87, -1.29), (0.03, 0.23)), 2: ((-1.12, -0.31), (0.07, 0.64)), 3: ((-2.11, -1.73), (1.39, 1.67)),\n      4: ((-0.17, 0.01), (0.32, 0.52)), 5: ((-0.7, -0.38), (0.2, 0.48)), 6: ((-1.63, -1.11), (2.02, 2.37)),\n      7: ((-0.84, -0.51), (1.14, 1.34)), 8: ((-0.3, 0.04), (0.36, 0.63)), 9: ((-0.57, -0.08), (-0.11, 0.23)),\n      10: ((-0.87, -0.35), (0.01, 0.3)), 11: ((-2.3, -1.86), (0.09, 0.34)), 12: ((-0.66, -0.44), (0.06, 0.2))}\nrng = np.random.default_rng(seed(\"table1-subject-band-power-ci\"))\nrows = []\nfor s, g in EVB.groupby(\"subject\"):\n    for bi, band in enumerate((\"lfb\", \"hfb\")):\n        lo, hi_ = T1[s][bi]\n        row = dict(subject=s, band=band, paper_lo=lo, paper_hi=hi_)\n        for bst in (\"mean\", \"median\"):\n            x = g[f\"pre_{band}_{bst}\"].values\n            for stat, fn in ((\"mean\", np.mean), (\"median\", np.median)):\n                v = fn(x)\n                row[f\"{stat}_of_band{bst}\"] = v\n                row[f\"in_{stat}_of_band{bst}\"] = lo <= v <= hi_\n            boot = np.array([np.median(x[rng.integers(0, len(x), len(x))]) for _ in range(5000)])\n            row[f\"ci_median_band{bst}\"] = np.round(np.percentile(boot, [2.5, 97.5]), 2)\n        rows.append(row)\nt1 = pd.DataFrame(rows)\nprint(t1.round(3).to_string())\nfor col in [c for c in t1.columns if c.startswith(\"in_\")]:\n    print(col, int(t1[col].sum()), \"of 24\")\nprint(\"LFB below 0 (median of band mean):\", int((t1[t1.band == \"lfb\"].median_of_bandmean < 0).sum()), \"of 12; HFB above 0:\",\n      int((t1[t1.band == \"hfb\"].median_of_bandmean > 0).sum()), \"of 12\")\n''', tags=(\"claim:table1-subject-band-power-ci\",))\nmd(\"**Result: ...** (table1-subject-band-power-ci)\")\n\nmd(r'''\n## fig5-recording-day-effects\n\n> Precentral band power differs significantly across recording days in LFB for subjects 03, 05, 06,\n> 07, 08 and 11, and in HFB for subjects 03, 04, 07, 08 and 10, despite baseline subtraction.\n''')\ncode(r'''\npaper_sig = {\"lfb\": {3, 5, 6, 7, 8, 11}, \"hfb\": {3, 4, 7, 8, 10}}\nrows = []\nfor s, g in EVB.groupby(\"subject\"):\n    for band in (\"lfb\", \"hfb\"):\n        row = dict(subject=s, band=band, paper_sig=s in paper_sig[band])\n        for bst in (\"mean\", \"median\"):\n            p = stats.kruskal(*[x[f\"pre_{band}_{bst}\"].values for _, x in g.groupby(\"day\")]).pvalue\n            row[f\"p_band{bst}\"] = p; row[f\"agree_band{bst}\"] = (p < 0.05) == (s in paper_sig[band])\n        row[\"day_means\"] = np.round(g.groupby(\"day\")[f\"pre_{band}_mean\"].mean().values, 2)\n        rows.append(row)\nt5 = pd.DataFrame(rows)\nprint(t5.to_string(float_format=lambda x: f\"{x:.3g}\"))\nprint(\"pairs agreeing, band mean:\", int(t5.agree_bandmean.sum()), \"of 24; band median:\", int(t5.agree_bandmedian.sum()), \"of 24\")\n''', tags=(\"claim:fig5-recording-day-effects\",))\nmd(\"**Result: ...** (fig5-recording-day-effects)\")\n\nmd(r'''\n## extfig5-1-baseline-reduces-day-variability\n\n> Subtracting the -1.5 to -1 s baseline reduces the variability of band power across recording\n> days, though clear variability remains.\n''')\ncode(r'''\nrows = []\nfor s, g in EVB.groupby(\"subject\"):\n    for band in (\"lfb\", \"hfb\"):\n        rows.append(dict(subject=s, band=band, sd_with=g.groupby(\"day\")[f\"pre_{band}_mean\"].mean().std(),\n                         sd_without=g.groupby(\"day\")[f\"pre_raw_{band}_mean\"].mean().std()))\nta = pd.DataFrame(rows); ta[\"reduced\"] = ta.sd_with < ta.sd_without\nprint(\"(a) precentral, per subject\"); print(ta.round(3).to_string())\n# (b) per good electrode (good in every file of the subject)\nrows = []\nfor s in subjects:\n    idx = [i for i, m in enumerate(metas) if int(m[\"subject_id\"]) == s]\n    good_all = np.all([metas[i][\"electrodes\"].good.values for i in idx], axis=0)\n    for band in (\"lfb\", \"hfb\"):\n        with_, without = [], []\n        for i in idx:\n            k = ev[ev.asset_id == metas[i][\"asset_id\"]].keep.values\n            with_.append(np.nanmean(ELEC[f\"{band}_mean\"][i][k][:, good_all], axis=0))\n            without.append(np.nanmean(ELEC[f\"{band}_mean_raw\"][i][k][:, good_all], axis=0))\n        sw, so = np.std(with_, axis=0, ddof=1), np.std(without, axis=0, ddof=1)\n        rows.append(dict(subject=s, band=band, electrodes=int(good_all.sum()), frac_reduced=np.mean(sw < so),\n                         n_reduced=int((sw < so).sum()), median_sd_with=np.median(sw), median_sd_without=np.median(so)))\ntb = pd.DataFrame(rows)\nprint(\"(b) per good electrode\"); print(tb.round(3).to_string())\nfor band in (\"lfb\", \"hfb\"):\n    a_frac = ta[ta.band == band].reduced.mean()\n    b_frac = tb[tb.band == band].n_reduced.sum() / tb[tb.band == band].electrodes.sum()\n    print(f\"{band.upper()}: (a) reduced in {a_frac:.2f} of subjects; (b) reduced in {b_frac:.3f} of electrodes\")\nprint(\"SD with baseline, range over subjects (dB):\", ta.sd_with.min().round(3), \"to\", ta.sd_with.max().round(3))\n''', tags=(\"claim:extfig5-1-baseline-reduces-day-variability\",))\nmd(\"**Result: ...** (extfig5-1-baseline-reduces-day-variability)\")\n\nmd(r'''\n## discussion-day-changes-small\n\n> Day-to-day changes in baseline-subtracted spectral power are small (about 1-2 dB) compared with\n> spectral power without baseline subtraction (about 10-50 dB).\n''')\ncode(r'''\nrows = []\nfor s, g in EVB.groupby(\"subject\"):\n    for band in (\"lfb\", \"hfb\"):\n        dm = g.groupby(\"day\")[f\"pre_{band}_mean\"].mean()\n        rows.append(dict(subject=s, band=band, max_dev=(dm - g[f\"pre_{band}_mean\"].mean()).abs().max(),\n                         day_range=dm.max() - dm.min(), level_uV=g[f\"pre_raw_{band}_mean\"].mean(),\n                         level_V=g[f\"pre_raw_{band}_mean\"].mean() - 120))\ntd = pd.DataFrame(rows)\nprint(td.round(3).to_string())\np1_ = bool((td.max_dev <= 2.2).all())\nlev_uv = bool(td.level_uV.between(9, 55).all()); lev_v = bool(td.level_V.between(9, 55).all())\nprint(\"largest day deviation:\", td.max_dev.max().round(3), \"dB -> part 1:\", p1_)\nprint(\"levels (uV^2 reading):\", td.level_uV.min().round(2), \"to\", td.level_uV.max().round(2), \"dB, in 9-55:\", lev_uv,\n      \"; (V^2 reading):\", td.level_V.min().round(2), \"to\", td.level_V.max().round(2), \"in 9-55:\", lev_v)\nprint(\"fraction of subject-band levels in 9-55 dB (uV^2):\", td.level_uV.between(9, 55).mean().round(3))\n''', tags=(\"claim:discussion-day-changes-small\",))\nmd(\"**Result: ...** (discussion-day-changes-small)\")\n\n# ---------------------------------------------------------------- regression\nmd(r'''\n## Regression models (Figure 6)\n\nOne model per subject, electrode and band, on the events of reading (b). Electrodes are those good\nin every file of the subject (the Methods remove bad electrodes; the flags differ between files, see\nthe data check). Ten features as the Methods and code encode them; forward selection over single\ncolumns on all events (code); Huber regression (sklearn defaults); 200 day-balanced splits with 10%\ntest events (Methods), and 20% (code) as a variant. Delta R2 is computed where the model's own R2,\nor its electrode's LFB R2, exceeds 0.05. The splits use the generator of claim\nfig6b-best-models-sensorimotor, the 80/20 splits its seed + 1 and the shuffles its seed + 2; the\nother Figure 6 claims use these same fits.\n''')\ncode(r'''\nt = time.time()\nREG_SEED = seed(\"fig6b-best-models-sensorimotor\")\ndef regression_jobs(seed0, include_bad=False):\n    jobs = []\n    for s in subjects:\n        idx = [i for i, m in enumerate(metas) if int(m[\"subject_id\"]) == s]\n        E = pd.concat([ev[ev.asset_id == metas[i][\"asset_id\"]] for i in idx])\n        keep = E.keep.values\n        G = np.array([metas[i][\"electrodes\"].good.values for i in idx])\n        use = np.ones(G.shape[1], bool) if include_bad else G.all(axis=0)\n        Y = np.stack([np.concatenate([ELEC[k][i] for i in idx])[keep][:, use]\n                      for k in (\"lfb_mean\", \"hfb_mean\", \"lfb_median\", \"hfb_median\")], axis=-1)\n        finite = np.isfinite(Y).all(axis=(0, 2))\n        Ek = E[keep]\n        X, names = ajile.design_matrix(Ek)\n        jobs.append(dict(subject=s, X=X, names=names, Y=Y[:, finite], days=Ek.day.values, seed=seed0,\n                         electrodes=np.flatnonzero(use)[finite], targets=[\"lfb_mean\", \"hfb_mean\", \"lfb_median\", \"hfb_median\"],\n                         main_targets=[\"lfb_mean\", \"hfb_mean\"], delta_min_r2=0.05, dropped_nonfinite=int((~finite).sum()),\n                         good_all=G.all(axis=0)))\n    return jobs\nJOBS = regression_jobs(REG_SEED)\nprint(\"models per subject (electrodes):\", {j[\"subject\"]: j[\"Y\"].shape[1] for j in JOBS},\n      \"; electrodes dropped for non-finite power:\", {j[\"subject\"]: j[\"dropped_nonfinite\"] for j in JOBS})\nREGR = pd.DataFrame(ajile.run_regression(JOBS, workers=4))\nprint(f\"regression {time.time() - t:.0f} s, {len(REGR)} models\")\nREGR[\"band\"] = REGR.target.str[:3]\nMAIN = REGR[REGR.target.isin([\"lfb_mean\", \"hfb_mean\"])].copy()\nprint(MAIN.groupby(\"band\").r2.describe().round(4).to_string())\n''')\n\nmd(r'''\n## fig6-r2-at-most-025\n\n> All regression models explain at most 25% of the variance of withheld single-event power.\n''')\ncode(r'''\nmx = MAIN.r2.max(); row = MAIN.loc[MAIN.r2.idxmax()]\nprint(f\"largest split-averaged withheld R2 (90/10, band mean): {mx:.4f} (S{row.subject:02d}, electrode {row.electrode}, {row.band})\")\nprint(\"largest with 80/20 splits:\", MAIN.r2_80.max().round(4), \"; with band median:\", REGR[REGR.target.str.endswith(\"median\")].r2.max().round(4))\nprint(\"models with R2 > 0.05:\", MAIN.groupby(\"band\").r2.apply(lambda x: int((x > 0.05).sum())).to_dict(), \"of\", MAIN.groupby(\"band\").size().to_dict())\nprint(\"ten largest:\"); print(MAIN.nlargest(10, \"r2\")[[\"subject\", \"electrode\", \"band\", \"r2\", \"r2_80\"]].round(4).to_string())\n''', tags=(\"claim:fig6-r2-at-most-025\",))\nmd(\"**Result: ...** (fig6-r2-at-most-025)\")\n\nmd(r'''\n## fig6b-best-models-sensorimotor\n\n> Regression models with the highest withheld R2 are mainly at electrodes over frontoparietal\n> sensorimotor areas, for both bands.\n''')\ncode(r'''\nfrontopar = [\"middle frontal\", \"precentral\", \"postcentral\", \"inferior parietal\", \"supramarginal\"]\nsensor3 = [\"precentral\", \"postcentral\", \"inferior parietal\"]\ndef region_of(s, e):\n    w = proj[s][1][e, roi_idx]\n    return ajile.ROI_NAMES[int(np.argmax(w))] if w.sum() > 0 else \"none\"\nMAIN[\"region\"] = [region_of(s, e) for s, e in zip(MAIN.subject, MAIN.electrode)]\nfor band in (\"lfb\", \"hfb\"):\n    M = MAIN[MAIN.band == band]\n    sel = M[M.r2 > 0.05]\n    frac = sel.region.isin(frontopar).mean() if len(sel) else np.nan\n    med_s = M[M.region.isin(sensor3)].r2.median(); med_t = M[M.region.isin(temporal)].r2.median()\n    # (b) projected R2: per subject weighted mean with the good-electrode weights, then mean over subjects\n    proj_r2 = []\n    for s in subjects:\n        Ms = M[M.subject == s]\n        w = np.nan_to_num(proj[s][1][Ms.electrode.values][:, roi_idx])\n        w = w / np.where(w.sum(0) > 0, w.sum(0), np.nan)\n        proj_r2.append(np.nansum(w * Ms.r2.values[:, None], axis=0))\n    pr = pd.Series(np.nanmean(proj_r2, axis=0), index=ajile.ROI_NAMES).sort_values(ascending=False)\n    print(f\"{band.upper()}: (a) {len(sel)} models with R2 > 0.05, fraction in the five frontoparietal regions {frac:.3f};\",\n          f\"median R2 sensorimotor {med_s:.4f} vs temporal {med_t:.4f}\")\n    print(\"   regions of the models with R2 > 0.05:\", sel.region.value_counts().to_dict())\n    print(\"   (b) projected R2 by region:\", pr.round(4).to_dict(), \"-> top three frontoparietal:\", all(x in frontopar for x in pr.index[:3]))\n    print(\"   models with R2 > 0.05 per subject:\", sel.subject.value_counts().sort_index().to_dict())\n''', tags=(\"claim:fig6b-best-models-sensorimotor\",))\nmd(\"**Result: ...** (fig6b-best-models-sensorimotor)\")\n\nmd(r'''\n## fig6c-angle-and-day-most-informative\n\n> Reach angle and day of recording are the most informative features for single-event power,\n> especially for low-frequency power.\n''')\ncode(r'''\ndef delta_table(df, col=\"delta\", select=\"own\"):\n    out = {}\n    for band in (\"lfb\", \"hfb\"):\n        M = df[df.band == band]\n        if select == \"own\":\n            M = M[M.r2 > 0.05]\n        else:\n            lfb_r2 = df[df.band == \"lfb\"].set_index([\"subject\", \"electrode\"]).r2\n            M = M[[lfb_r2.get((s, e), -1) > 0.05 for s, e in zip(M.subject, M.electrode)]]\n        D = pd.DataFrame([d for d in M[col] if isinstance(d, dict)])\n        out[band] = D.median().sort_values(ascending=False) if len(D) else pd.Series(dtype=float)\n        out[band + \"_n\"] = len(D)\n    return out\nfor label, col, selm in ((\"Methods Delta R2, own-band selection\", \"delta\", \"own\"),\n                         (\"code Delta R2 (80/20, test shuffled), own-band selection\", \"delta_code\", \"own\"),\n                         (\"Methods Delta R2, selection by LFB R2 (code)\", \"delta\", \"lfb\")):\n    d = delta_table(MAIN, col, selm)\n    print(label)\n    for band in (\"lfb\", \"hfb\"):\n        print(f\"  {band.upper()} ({d[band + '_n']} models):\", d[band].round(5).to_dict())\n        print(\"     top two:\", list(d[band].index[:2]))\n''', tags=(\"claim:fig6c-angle-and-day-most-informative\",))\nmd(\"**Result: ...** (fig6c-angle-and-day-most-informative)\")\n\nmd(r'''\n## extfig6-2-angle-most-retained\n\n> Reach angle is the feature most often retained by forward selection in sensorimotor regions,\n> followed by reach duration, reach magnitude, bimanual ratio and bimanual overlap.\n''')\ncode(r'''\nRET = {}\nfor band in (\"lfb\", \"hfb\"):\n    M = MAIN[MAIN.band == band]\n    per_s = []\n    for s in subjects:\n        Ms = M[M.subject == s]\n        R = pd.DataFrame(list(Ms.retention)).reindex(columns=ajile.FEATURES).values\n        w = np.nan_to_num(proj[s][1][Ms.electrode.values][:, roi_idx])\n        w = w / np.where(w.sum(0) > 0, w.sum(0), np.nan)\n        per_s.append(np.einsum(\"er,ef->rf\", np.nan_to_num(w), R))\n    RET[band] = pd.DataFrame(np.nanmean(per_s, axis=0), index=ajile.ROI_NAMES, columns=ajile.FEATURES)\n    print(band.upper()); print(RET[band].round(3).to_string())\nangle_top = {(b, r): RET[b].loc[r].idxmax() for b in (\"lfb\", \"hfb\") for r in sensor3}\nprint(\"most retained feature in each sensorimotor region and band:\", angle_top)\nangle_part = all(v == \"angle\" for v in angle_top.values())\norder_paper = [\"duration\", \"magnitude\", \"bimanual_ratio\", \"bimanual_overlap\"]\nra_ = pd.concat([RET[b].loc[sensor3] for b in RET]).mean().sort_values(ascending=False)\nrb_ = pd.concat([RET[b] for b in RET]).mean().sort_values(ascending=False)\nprint(\"(a) three sensorimotor regions, both bands:\", ra_.round(3).to_dict())\nprint(\"(b) all eight regions, both bands:\", rb_.round(3).to_dict())\nprint(\"angle part:\", angle_part, \"; order part (a):\", list(ra_.index[1:5]) == order_paper, list(ra_.index[1:5]),\n      \"; (b):\", list(rb_.index[1:5]) == order_paper, list(rb_.index[1:5]))\n''', tags=(\"claim:extfig6-2-angle-most-retained\",))\nmd(\"**Result: ...** (extfig6-2-angle-most-retained)\")\n\nmd(r'''\n## fig6d-upward-reaches-enhance-pattern\n\n> Upward reaches are associated with lower low-frequency power and higher high-frequency power.\n''')\ncode(r'''\nfor label, selm in ((\"own-band R2 > 0.05\", \"own\"), (\"LFB R2 > 0.05 (code)\", \"lfb\")):\n    out = {}\n    lfb_r2 = MAIN[MAIN.band == \"lfb\"].set_index([\"subject\", \"electrode\"]).r2\n    for band in (\"lfb\", \"hfb\"):\n        M = MAIN[MAIN.band == band]\n        M = M[M.r2 > 0.05] if selm == \"own\" else M[[lfb_r2.get((s, e), -1) > 0.05 for s, e in zip(M.subject, M.electrode)]]\n        c = np.array([d[\"angle\"] for d in M.coef])\n        out[band] = (len(c), np.median(c) if len(c) else np.nan, (c < 0).mean() if len(c) else np.nan)\n    print(label, {b: dict(n=v[0], median_angle_coef=round(float(v[1]), 4), frac_negative=round(float(v[2]), 3)) for b, v in out.items()})\n''', tags=(\"claim:fig6d-upward-reaches-enhance-pattern\",))\nmd(\"**Result: ...** (fig6d-upward-reaches-enhance-pattern)\")\n\nmd(r'''\n## fig6d-angle-and-day-largest-coefficients\n\n> Reach angle and day of recording have the largest coefficient magnitudes among the features, and\n> the SD of the recording-day coefficients is large.\n''')\ncode(r'''\nfor label, selm in ((\"own-band R2 > 0.05\", \"own\"), (\"LFB R2 > 0.05 (code)\", \"lfb\")):\n    lfb_r2 = MAIN[MAIN.band == \"lfb\"].set_index([\"subject\", \"electrode\"]).r2\n    for band in (\"lfb\", \"hfb\"):\n        M = MAIN[MAIN.band == band]\n        M = M[M.r2 > 0.05] if selm == \"own\" else M[[lfb_r2.get((s, e), -1) > 0.05 for s, e in zip(M.subject, M.electrode)]]\n        C = pd.DataFrame(list(M.coef))\n        ra = C.abs().median().sort_values(ascending=False); rb = C.median().abs().sort_values(ascending=False)\n        print(f\"{label}, {band.upper()} ({len(C)} models)\")\n        print(\"   (a) median |coef|:\", ra.round(4).to_dict(), \"top two\", list(ra.index[:2]))\n        print(\"   (b) |median coef|:\", rb.round(4).to_dict(), \"top two\", list(rb.index[:2]))\n''', tags=(\"claim:fig6d-angle-and-day-largest-coefficients\",))\nmd(\"**Result: ...** (fig6d-angle-and-day-largest-coefficients)\")\n\ncode(r'''\n# Seed sensitivity of the regression: full-model R2 of the models with R2 > 0.03 under the main seed,\n# refit with the splits of the claim's seed + 1000 ... + 4000 (Delta R2 not refit: see the summary)\nt = time.time()\ntop = MAIN[MAIN.r2 > 0.03][[\"subject\", \"electrode\"]].drop_duplicates()\nsens = {}\nfor off in SEED_OFFSETS[1:]:\n    jobs = []\n    for j in JOBS:\n        es = set(top[top.subject == j[\"subject\"]].electrode)\n        k = np.array([e in es for e in j[\"electrodes\"]])\n        if not k.any():\n            continue\n        jj = dict(j); jj[\"Y\"] = j[\"Y\"][:, k][:, :, :2]; jj[\"electrodes\"] = j[\"electrodes\"][k]\n        jj[\"targets\"] = [\"lfb_mean\", \"hfb_mean\"]; jj[\"seed\"] = REG_SEED + off; jj[\"delta_min_r2\"] = np.inf\n        jobs.append(jj)\n    R = pd.DataFrame(ajile.run_regression(jobs, workers=4))\n    R[\"band\"] = R.target.str[:3]\n    sens[off] = R\n    print(f\"seed + {off}: largest R2 {R.r2.max():.4f}; models > 0.05:\", R.groupby('band').r2.apply(lambda x: int((x > 0.05).sum())).to_dict())\nprint(f\"{time.time() - t:.0f} s\")\n''', tags=(\"claim:fig6-r2-at-most-025\",))\n\nmd(open(\"/tmp/claude-1001/summary.md\").read())\n\ncode(r'''\nprint(f\"notebook run time {(time.time() - T0) / 60:.1f} min; peak memory of this process \"\n      f\"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n''')\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_claims.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && echo "# Header placeholder" > header.md && echo "## Summary placeholder" > summary.md && . dev/bin/activate && uv pip install -q nbformat nbclient ipykernel 2>&1 | tail -1; python build_nb.py && cat > harness.py <<'EOF'
import nbformat, pickle, sys, time, os
os.chdir('entries/peterson-2021'); sys.path.insert(0,'.')
import matplotlib; matplotlib.use('Agg')
nb=nbformat.read('reproduce_peterson_2021.ipynb',4)
stop=int(sys.argv[1]) if len(sys.argv)>1 else 999
start=int(sys.argv[2]) if len(sys.argv)>2 else 0
ns={}
if start>0:
    ns=pickle.load(open('/tmp/claude-1001/ns.pkl','rb'))
D=pickle.load(open('/tmp/claude-1001/dev_spec.pkl','rb'))
for i,c in enumerate(nb.cells):
    if c.cell_type!='code' or i<start: continue
    if i>stop: break
    src=c.source
    if src.startswith('# LOAD-META'):
        src="assets=__D['assets']; metas=__D['metas']"
    if src.startswith('# SPECTRAL'):
        src="roi_idx=[cols_all.index(r) for r in ajile.ROIS]; spec=__D['res']"
    ns['__D']=D
    t=time.time()
    print(f'===== cell {i}', flush=True)
    exec(compile(src,f'cell{i}','exec'),ns)
    print(f'----- {time.time()-t:.1f}s', flush=True)
    if 'REGR' in ns and i==stop:
        pass
keep={k:v for k,v in ns.items() if not k.startswith('__') and k not in ('ajile','plt','stats','np','pd','os','re','time','zlib','resource')}
try:
    pickle.dump({k:v for k,v in keep.items() if not callable(v) or k in()},open('/tmp/claude-1001/ns_try.pkl','wb'))
except Exception as e: print('pickle fail',e)
EOF
python -c "
import nbformat;nb=nbformat.read('entries/peterson-2021/reproduce_peterson_2021.ipynb',4)
for i,c in enumerate(nb.cells): print(i,c.cell_type,c.source[:60].replace(chr(10),' '))"
```

```
98 cells
0 markdown # Header placeholder
1 code import os, re, time, zlib, resource os.environ.setdefault("O
2 code # LOAD-META: list the assets of the pinned version and read 
3 code ev_all = ajile.event_table(metas) subjects = sorted(ev_all.s
4 code # Checks of the description against the values m0 = metas[0]
5 code # Coarse behavioural labels (epochs) at the event times. The
6 markdown ## Projection matrices (outside input) and claim `roi-projec
7 code files, fig_meta = ajile.figshare_files() print("Figshare ite
8 code # Largest-weight region against the nearest region centroid,
9 markdown **Result: ...** (link)
10 markdown ## Spectral power of every event (streamed)  For each file, 
11 code # SPECTRAL t = time.time() roi_idx = [cols_all.index(r) for 
12 code ev = ev_all.copy() ev["inside"] = np.concatenate([r["inside"
13 code # Clock check: event-locked band power at the true onsets ag
14 code # Reach angle convention: the stored angle against the angle
15 markdown ## Event sets  Reading (a): every event in the reaches table
16 code EVA = ev EVB = ev[ev.keep] print("reading a:", len(EVA), "ev
17 markdown ## subject-days  > The dataset's subjects and recording days
18 code paper_days = {1: [3, 4, 5, 7], 2: [3, 4, 5, 6], 3: [3, 4, 5,
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && timeout 1800 python -u harness.py 74 2>&1 | grep -v -i "warn" | head -400
```

```
===== cell 1
dandiset 000055 version 0.261123.1703
----- 1.5s
===== cell 2
----- 0.0s
===== cell 3
subjects: [np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7), np.int64(8), np.int64(9), np.int64(10), np.int64(11), np.int64(12)]
days per subject: {1: [np.int64(3), np.int64(4), np.int64(5), np.int64(7)], 2: [np.int64(3), np.int64(4), np.int64(5), np.int64(6)], 3: [np.int64(3), np.int64(4), np.int64(5), np.int64(6)], 4: [np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)], 5: [np.int64(3), np.int64(4), np.int64(7)], 6: [np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)], 7: [np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)], 8: [np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)], 9: [np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)], 10: [np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)], 11: [np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)], 12: [np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)]}
session_description: All times are the hospital's local wall-clock times. The recording dates were removed to de-identify the participants, and the dates are shifted to January 2000. The offset of the times from UTC is unknown, so session_start_time is given with a +00:00 offset. The session starts at midnight of the recording day, and every time in the file counts from that midnight.
    subject  day sex   age       start  ecog_hours  n_el  n_el_table  good  no_position  events event_wrist  pose_hours  events_after_ecog_end
0         1    3   M  P44Y  2000-01-03   24.000000    94          94    85            0     156     r_wrist        24.0                      0
1         1    4   M  P44Y  2000-01-04   24.000000    94          94    91            0     196     r_wrist        24.0                      0
2         1    5   M  P44Y  2000-01-05   24.000000    94          94    91            0     199     r_wrist        24
[... 123 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && grep -n "^def " ajile.py; ls
```

```
73:def list_assets():
87:def s3_url(asset_id):
91:def open_nwb(asset_id):
96:def _txt(v):
100:def load_session_meta(asset_id):
144:def load_all_meta(assets, workers=12):
149:def fold_angle(a):
159:def event_table(metas):
187:def figshare_files():
192:def load_projection(subject, files):
201:def morlet_bank():
219:def band_stats(spec):
230:def _segment_psd(seg):
236:def _range(sess, url, off, n):
247:def chunk_index(ds, url, sess, n_threads=16):
306:def session_spectral(asset_id, event_times, good, weights, n_threads=6, batch_chunks=6,
429:def design_matrix(ev, log_speed=False):
456:def forward_select(X, y):
486:def day_balanced_splits(days, n_splits, test_frac, rng):
501:def r2(y, p):
[... 8 more lines not kept]
```

**Agent**

I accidentally truncated a few helper functions in an earlier edit; restoring them.

**Agent calls Bash**

```bash
cat >> ajile.py <<'EOF'


def _spectral_job(args):
    import os
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    asset_id, times, good, weights = args
    return session_spectral(asset_id, times, good, weights)


def run_spectral(jobs, workers=8):
    """jobs: list of (asset_id, event_times, good, weights). Runs files in parallel processes."""
    from concurrent.futures import ProcessPoolExecutor
    import multiprocessing as mp
    with ProcessPoolExecutor(workers, mp_context=mp.get_context("spawn")) as ex:
        return list(ex.map(_spectral_job, jobs))


def match_projection(m, positions_known):
    """Rows of a projection matrix matched to the file's electrodes, by the paper's code
    (tfr_utils.load_project_spectral_power, commit 04c6faf): it keeps the rows that are not all
    zero and drops the first of them (`np.nonzero(df.transpose().mean().values != 0)[0][1:]`),
    and applies the rest, in order, to the channels of its power files. Here they are applied,
    in order, to the electrodes whose positions are known (electrodes without a position get
    no weight). Returns (array n_electrodes x regions or None, note)."""
    a = m.values.astype(float)
    keep = np.flatnonzero(a.mean(axis=1) != 0)[1:]
    rows = a[keep]
    n_known = int(positions_known.sum())
    if len(rows) != n_known:
        return None, f"{len(rows)} rows for {n_known} electrodes with positions"
    out = np.zeros((len(positions_known), a.shape[1]))
    out[positions_known] = rows
    return out, f"{len(rows)} rows for {n_known} electrodes with positions"


def session_weights(proj, good):
    """Weights of the eight regions: bad electrodes 0, each region renormalised to sum 1."""
    w = proj.copy()
    w[~good] = 0
    s = w.sum(axis=0)
    return w / np.where(s > 0, s, np.nan)
EOF
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import pickle, numpy as np
D=pickle.load(open('dev_spec.pkl','rb'))
for m in D['metas']:
    d=np.abs(m['event_times']-m['reaches'].start_time.values)
    if d.max()>0.01: print(m['subject_id'],m['session_id'], (d>0.01).sum(), m['event_times'][d>0.01][:5], m['reaches'].start_time.values[d>0.01][:5], m['reaches'].stop_time.values[d>0.01][:5])
EOF
```

```
08 4 1 [40.332] [86440.332] [86440.89866667]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && timeout 1800 python -u harness.py 74 2>&1 | grep -v -i "warn" | sed -n '/===== cell 7/,$p' | head -400
```

```
===== cell 7
Figshare item 12114408 version 1 10.6084/m9.figshare.12114408.v1
    subject  csv_rows  electrodes  with_position  nonzero_rows                                   code_rule  matched
0         1        99          94             94            95    94 rows for 94 electrodes with positions     True
1         2        87          86             86            87    86 rows for 86 electrodes with positions     True
2         3        97          96             80            81    80 rows for 80 electrodes with positions     True
3         4        85          84             84            85    84 rows for 84 electrodes with positions     True
4         5       107         106            106           107  106 rows for 106 electrodes with positions     True
5         6        81          80             80            81    80 rows for 80 electrodes with positions     True
6         7        65          64             64            65    64 rows for 64 electrodes with positions     True
7         8        93          92             92            93    92 rows for 92 electrodes with positions     True
8         9       127         126            126           127  126 rows for 126 electrodes with positions     True
9        10       127         126            126           127  126 rows for 126 electrodes with positions     True
10       11       107         106            106           107  106 rows for 106 electrodes with positions     True
11       12       125         124            116           117  116 rows for 116 electrodes with positions     True
regions with mean density > 3: []
same as the eight of the claims file: False
----- 12.7s
===== cell 8
centroid table shape: (116, 3) columns: ['x', 'y', 'z']
[... 381 more lines not kept]
```

**Agent**

Most behavioural and spectral claims run. Two things to check: the region-density rule returns no regions, and some events have exactly 0 dB raw power (probably partially zeroed segments).

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import sys, pickle, numpy as np, pandas as pd
sys.path.insert(0,'entries/peterson-2021')
import ajile
D=pickle.load(open('dev_spec.pkl','rb')); metas=D['metas']; res=D['res']
files,_=ajile.figshare_files()
dens=[]
for s in [1,2,7]:
    m,c=ajile.load_projection(s,files)
    print(s, m.values.sum(0)[:8].round(2), m.columns[:8].tolist())
R=np.concatenate([r['region'] for r in res])
pre=R[:,1]
raw=pre[..., ajile.WIN][:, ajile.LFB].mean((1,2))
ev=ajile.event_table(metas)
z=np.flatnonzero(raw==0); print('zero events',len(z), ev.iloc[z][['subject','day','start_time']].head())
bs=pre-pre[...,ajile.BASE].mean(-1,keepdims=True); v=bs[..., ajile.WIN][:, ajile.LFB].mean((1,2))
ext=np.flatnonzero(np.abs(v)>15); print('extreme',len(ext)); print(ev.iloc[ext][['subject','day','start_time']].value_counts(['subject','day']).head(20))
i=ext[0]; print(np.round(pre[i][5],1))
EOF
```

```
1 [5.72 1.   1.04 1.   1.01 1.   4.9  1.  ] ['Precentral_L', 'Precentral_R', 'Frontal_Sup_L', 'Frontal_Sup_R', 'Frontal_Sup_Orb_L', 'Frontal_Sup_Orb_R', 'Frontal_Mid_L', 'Frontal_Mid_R']
2 [1.15 1.   1.   1.   1.   1.   1.   1.  ] ['Precentral_L', 'Precentral_R', 'Frontal_Sup_L', 'Frontal_Sup_R', 'Frontal_Sup_Orb_L', 'Frontal_Sup_Orb_R', 'Frontal_Mid_L', 'Frontal_Mid_R']
7 [10.21  1.    5.29  1.    1.    1.    6.99  1.  ] ['Precentral_L', 'Precentral_R', 'Frontal_Sup_L', 'Frontal_Sup_R', 'Frontal_Sup_Orb_L', 'Frontal_Sup_Orb_R', 'Frontal_Mid_L', 'Frontal_Mid_R']
zero events 58       subject  day  start_time
115         1    3   67883.439
302         1    4   62246.633
361         1    5   26700.490
898         2    5   24351.591
1972        4    7   32001.271
extreme 32
subject  day
10       6      7
6        6      3
         7      3
8        3      3
11       7      3
7        7      2
11       5      2
12       4      2
1        4      1
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import sys, numpy as np
sys.path.insert(0,'entries/peterson-2021')
import ajile, pickle
D=pickle.load(open('dev_spec.pkl','rb')); m=D['metas'][0]; r=D['res'][0]
i=115; print(r['allzero'][i], r['inside'][i], r['seg_db'][i])
f,url=ajile.open_nwb(m['asset_id']); ds=f['acquisition/ElectricalSeries/data']
t=m['event_times'][i]; s=int(round(t*500))
x=ds[s-2500:s+2500,:]
good=m['electrodes'].good.values
print((x[:, good]==0).all(0).sum(), 'good electrodes all-zero in segment of', good.sum())
z=(x[:,good]==0); print('samples all good zero', z.all(1).sum(), 'per-electrode zero frac', np.round(z.mean(0)[:10],2))
print(np.round(np.abs(x[2500-600:2500+200:50,:4]),1))
EOF
```

```
False True nan
0 good electrodes all-zero in segment of 85
samples all good zero 0 per-electrode zero frac [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[[nan nan nan nan]
 [nan nan nan nan]
 [nan nan nan nan]
 [nan nan nan nan]
 [nan nan nan nan]
 [nan nan nan nan]
 [nan nan nan nan]
 [nan nan nan nan]
 [nan nan nan nan]
 [nan nan nan nan]
 [nan nan nan nan]
 [nan nan nan nan]
 [nan nan nan nan]
 [nan nan nan nan]
 [nan nan nan nan]
 [nan nan nan nan]]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('build_nb.py').read()
s=s.replace('''# regions kept: mean electrode density over subjects > 3 (Methods)
dens = np.array([proj[s][1].sum(axis=0) for s in subjects]).mean(axis=0)''','''# The first non-zero row of each file, the row the code drops, holds the electrode density of each
# region (the remaining rows sum to 1 per region). Regions kept: mean density over subjects > 3 (Methods).
dens_rows = []
for s in subjects:
    m, _ = ajile.load_projection(s, files)
    a = m.values.astype(float)
    first = a[np.flatnonzero(a.mean(axis=1) != 0)[0]]
    rest = a[np.flatnonzero(a.mean(axis=1) != 0)[1:]]
    dens_rows.append(first)
    if s == 1:
        print("S01: rows after the first sum per region to (first 6 regions):", rest.sum(axis=0)[:6].round(3))
dens = np.array(dens_rows).mean(axis=0)
print("mean density of the eight regions:", {r: round(float(dens[cols_all.index(r)]), 2) for r in ajile.ROIS})''')
s=s.replace('''ev["keep"] = ev.inside & ~ev.allzero & ~ev.low_power & ~ev.hf_bad
drop = ev.groupby("subject").agg(events=("keep", "size"), no_ecog=("inside", lambda x: int((~x).sum())),
                                 zeroed=("allzero", "sum"), below_0dB=("low_power", "sum"),''','''# Segments holding NaN samples (the files store missing ECoG as NaN) have NaN power: missing data
ev["nan_data"] = ev.inside & ev.seg_db.isna()
ev["keep"] = ev.inside & ~ev.nan_data & ~ev.allzero & ~ev.low_power & ~ev.hf_bad
drop = ev.groupby("subject").agg(events=("keep", "size"), no_ecog=("inside", lambda x: int((~x).sum())),
                                 nan_data=("nan_data", "sum"), zeroed=("allzero", "sum"), below_0dB=("low_power", "sum"),''')
s=s.replace('''hf_thr = ev[ev.inside].groupby("subject")''','''hf_thr = ev[ev.inside & ev.hf_db.notna()].groupby("subject")''')
open('build_nb.py','w').write(s)
s=open('build_claims.py').read()
s=s.replace('''cnt = pd.DataFrame({"a_all": EVA.groupby("subject").size(), "b_kept": EVB.groupby("subject").size(),
                    "with_ecog": ev[ev.inside].groupby("subject").size()})''','''cnt = pd.DataFrame({"a_all": EVA.groupby("subject").size(), "b_kept": EVB.groupby("subject").size(),
                    "with_ecog": ev[ev.inside & ~ev.nan_data].groupby("subject").size()})''')
open('build_claims.py','w').write(s)
EOF
grep -n "nan_data" build_nb.py | head -3; . dev/bin/activate && python build_nb.py && timeout 900 python -u harness.py 12 2>&1 | grep -v -i warn | sed -n '/===== cell 7/,$p' | grep -v "^ \+[0-9]\+ \+[0-9]\+ \+[0-9]\+ \+[0-9]\+ .*rows for"
```

```
245:ev["nan_data"] = ev.inside & ev.seg_db.isna()
246:ev["keep"] = ev.inside & ~ev.nan_data & ~ev.allzero & ~ev.low_power & ~ev.hf_bad
248:                                 nan_data=("nan_data", "sum"), zeroed=("allzero", "sum"), below_0dB=("low_power", "sum"),
98 cells
===== cell 7
Figshare item 12114408 version 1 10.6084/m9.figshare.12114408.v1
    subject  csv_rows  electrodes  with_position  nonzero_rows                                   code_rule  matched
0         1        99          94             94            95    94 rows for 94 electrodes with positions     True
1         2        87          86             86            87    86 rows for 86 electrodes with positions     True
2         3        97          96             80            81    80 rows for 80 electrodes with positions     True
3         4        85          84             84            85    84 rows for 84 electrodes with positions     True
4         5       107         106            106           107  106 rows for 106 electrodes with positions     True
5         6        81          80             80            81    80 rows for 80 electrodes with positions     True
6         7        65          64             64            65    64 rows for 64 electrodes with positions     True
7         8        93          92             92            93    92 rows for 92 electrodes with positions     True
8         9       127         126            126           127  126 rows for 126 electrodes with positions     True
9        10       127         126            126           127  126 rows for 126 electrodes with positions     True
10       11       107         106            106           107  106 rows for 106 electrodes with positions     True
11       12       125         124            116           117  116 rows for 116 electrodes with positions     True
S01: rows after the first sum per region to (first 6 regions): [1. 1. 1. 1. 1. 1.]
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && python3 - <<'EOF'
s=open('harness.py').read()
s=s.replace('''    ns['__D']=D''','''    ns['__D']=D
    if 'REGR = pd.DataFrame(ajile.run_regression' in src and os.path.exists('/tmp/claude-1001/regr.pkl'):
        src=src.split('REGR = pd.DataFrame')[0]+"REGR=pickle.load(open('/tmp/claude-1001/regr.pkl','rb'))\\n"+'REGR["band"]'+src.split('REGR["band"]',1)[1]
        ns['pickle']=pickle''')
s=s.replace('''    print(f'----- {time.time()-t:.1f}s', flush=True)''','''    print(f'----- {time.time()-t:.1f}s', flush=True)
    if 'REGR' in ns and not os.path.exists('/tmp/claude-1001/regr.pkl'):
        pickle.dump(ns['REGR'],open('/tmp/claude-1001/regr.pkl','wb'))''')
open('harness.py','w').write(s)
EOF
. dev/bin/activate && timeout 3000 python -u harness.py 94 2>&1 | grep -v -i warn | sed -n '/===== cell 46/,$p' | sed -n '/===== cell 5[6-9]/,$p'
```

```
<persisted-output>
Output too large (230.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/f827794a-c716-4e85-a39e-d824755c2636/tool-results/bl5vra1gm.txt

Preview (first 2KB):
Wed Nov 25 06:23:16 UTC 2026
===== cell 56
      1     6     11    16    21    26    31    36    41    46    51    56    61    66    71    76    81    86    91    96    101   106   111   116   121
S01  0.10 -0.52 -1.35 -1.91 -1.57 -1.12 -1.02 -0.93 -0.75 -0.54 -0.36 -0.23 -0.16 -0.01  0.02  0.07  0.03  0.02  0.05  0.02  0.11  0.15  0.16  0.07 -0.01
S02  0.29 -0.10 -0.48 -0.55 -0.27 -0.20 -0.34 -0.17  0.06  0.18  0.20  0.06  0.00  0.30  0.12  0.44 -0.04  0.13  0.16  0.22  0.18  0.17 -0.04  0.07  0.12
S03  0.71 -0.74 -2.17 -2.86 -2.18 -1.01 -0.61 -0.30 -0.02  0.17  0.38  0.60  0.93  1.11  1.17  1.27  1.25  1.24  1.34  1.34  1.43  1.30  1.18  1.23  1.10
S04  0.04 -0.33 -0.39 -0.19 -0.03 -0.01  0.14  0.12  0.07  0.07  0.25  0.30  0.40  0.43  0.47  0.51  0.46  0.52  0.46  0.53  0.49  0.45  0.47  0.41  0.39
S05 -0.20 -0.32 -0.80 -0.88 -0.54 -0.38 -0.20 -0.09 -0.02 -0.04  0.11  0.18  0.24  0.26  0.33  0.25  0.23  0.18  0.33  0.41  0.33  0.12  0.20  0.30  0.23
S06  2.15  0.88 -0.40 -1.02 -1.34 -1.18 -0.84 -0.21  0.24  0.33  0.49  0.75  1.11  1.38  1.49  1.47  1.56  1.64  1.65  1.53  1.58  1.43  1.48  1.46  1.29
S07 -0.01 -0.69 -1.40 -1.30 -0.56 -0.17  0.17  0.44  0.66  0.89  1.03  1.13  1.08  1.25  1.21  1.18  1.20  1.15  1.27  1.23  1.18  1.18  1.12  1.13  1.07
S08  0.33  0.20 -0.01 -0.05 -0.05 -0.21 -0.14  0.03  0.09  0.19  0.18  0.21  0.36  0.38  0.40  0.41  0.39  0.37  0.44  0.35  0.34  0.29  0.32  0.29  0.28
S09 -0.57 -0.46 -0.39 -0.31 -0.22 -0.32 -0.01  0.02  0.24  0.24  0.02  0.14 -0.07  0.24  0.23  0.10  0.04  0.00 -0.04 -0.26 -0.03 -0.07 -0.21 -0.07 -0.16
S10 -0.12 -0.65 -0.65 -0.46 -0.33 -0.19 -0.16 -0.07 -0.04 -0.03 -0.02  0.09  0.24  0.16  0.15  0.17  0.20  0.09  0.13  0.21  0.18  0.15  0.13  0.17  0.12
S11 -0.17 -0.80 -1.73 -2.95 
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
F=/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/f827794a-c716-4e85-a39e-d824755c2636/tool-results/bl5vra1gm.txt; grep -v -i "lbfgs\|iteration\|scikit-learn\|https\|n_iter_i\|STOP:\|Increase the\|regression:\|^ *$\|_check_optimize\|self.n_iter\|of ITERATIONS\|Please also refer\|^--*$" $F | sed -n '/===== cell 5[6-9]/,$p' | head -300
```

```
<persisted-output>
Output too large (32.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/f827794a-c716-4e85-a39e-d824755c2636/tool-results/bfc15tve8.txt

Preview (first 2KB):
===== cell 56
      1     6     11    16    21    26    31    36    41    46    51    56    61    66    71    76    81    86    91    96    101   106   111   116   121
S01  0.10 -0.52 -1.35 -1.91 -1.57 -1.12 -1.02 -0.93 -0.75 -0.54 -0.36 -0.23 -0.16 -0.01  0.02  0.07  0.03  0.02  0.05  0.02  0.11  0.15  0.16  0.07 -0.01
S02  0.29 -0.10 -0.48 -0.55 -0.27 -0.20 -0.34 -0.17  0.06  0.18  0.20  0.06  0.00  0.30  0.12  0.44 -0.04  0.13  0.16  0.22  0.18  0.17 -0.04  0.07  0.12
S03  0.71 -0.74 -2.17 -2.86 -2.18 -1.01 -0.61 -0.30 -0.02  0.17  0.38  0.60  0.93  1.11  1.17  1.27  1.25  1.24  1.34  1.34  1.43  1.30  1.18  1.23  1.10
S04  0.04 -0.33 -0.39 -0.19 -0.03 -0.01  0.14  0.12  0.07  0.07  0.25  0.30  0.40  0.43  0.47  0.51  0.46  0.52  0.46  0.53  0.49  0.45  0.47  0.41  0.39
S05 -0.20 -0.32 -0.80 -0.88 -0.54 -0.38 -0.20 -0.09 -0.02 -0.04  0.11  0.18  0.24  0.26  0.33  0.25  0.23  0.18  0.33  0.41  0.33  0.12  0.20  0.30  0.23
S06  2.15  0.88 -0.40 -1.02 -1.34 -1.18 -0.84 -0.21  0.24  0.33  0.49  0.75  1.11  1.38  1.49  1.47  1.56  1.64  1.65  1.53  1.58  1.43  1.48  1.46  1.29
S07 -0.01 -0.69 -1.40 -1.30 -0.56 -0.17  0.17  0.44  0.66  0.89  1.03  1.13  1.08  1.25  1.21  1.18  1.20  1.15  1.27  1.23  1.18  1.18  1.12  1.13  1.07
S08  0.33  0.20 -0.01 -0.05 -0.05 -0.21 -0.14  0.03  0.09  0.19  0.18  0.21  0.36  0.38  0.40  0.41  0.39  0.37  0.44  0.35  0.34  0.29  0.32  0.29  0.28
S09 -0.57 -0.46 -0.39 -0.31 -0.22 -0.32 -0.01  0.02  0.24  0.24  0.02  0.14 -0.07  0.24  0.23  0.10  0.04  0.00 -0.04 -0.26 -0.03 -0.07 -0.21 -0.07 -0.16
S10 -0.12 -0.65 -0.65 -0.46 -0.33 -0.19 -0.16 -0.07 -0.04 -0.03 -0.02  0.09  0.24  0.16  0.15  0.17  0.20  0.09  0.13  0.21  0.18  0.15  0.13  0.17  0.12
S11 -0.17 -0.80 -1.73 -2.95 -3.23 -1.85 -0.66 -0.68 -0.62 
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
F=/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/f827794a-c716-4e85-a39e-d824755c2636/tool-results/bfc15tve8.txt; grep -v "warnings.warn\|ConvergenceWarning\|^ *warn" $F | sed -n '/===== cell 59/,$p' | cut -c1-260 | head -220
```

```
===== cell 59
       pre_lfb_mean  pre_hfb_mean  pre_lfb_median  pre_hfb_median  pre_raw_lfb_mean  pre_raw_hfb_mean
count      7650.000      7650.000        7650.000        7650.000          7650.000          7650.000
mean         -0.833         0.547          -0.797           0.595            34.371            18.657
std           2.044         1.422           2.110           1.490             2.063             2.640
min         -16.091        -7.695         -17.426          -7.453            27.336             9.731
25%          -1.856        -0.304          -1.814          -0.306            32.915            16.881
50%          -0.544         0.447          -0.518           0.485            34.172            18.316
75%           0.376         1.299           0.444           1.384            35.642            20.140
max           9.897         7.683          11.023           8.449            45.380            28.081
----- 0.0s
===== cell 61
LFB band mean: H = 749.8, p = 0, n = 7650 events in 12 subjects
LFB band median: H = 775.8, p = 0, n = 7650 events in 12 subjects
HFB band mean: H = 1048.2, p = 0, n = 7650 events in 12 subjects
HFB band median: H = 1011.9, p = 0, n = 7650 events in 12 subjects
----- 0.0s
===== cell 64
    subject band  paper_lo  paper_hi  mean_of_bandmean  in_mean_of_bandmean  median_of_bandmean  in_median_of_bandmean ci_median_bandmean  mean_of_bandmedian  in_mean_of_bandmedian  median_of_bandmedian  in_median_of_bandmedian ci_median_bandmedian
0         1  lfb     -1.87     -1.29            -1.353                 True              -1.319                   True     [-1.66, -0.96]              -1.337                   True                -1.330                     True       [-1.69, -0.95]
[... 200 more lines not kept]
```

**Agent calls Bash**

```bash
F=/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/f827794a-c716-4e85-a39e-d824755c2636/tool-results/bfc15tve8.txt; tail -5 $F | cut -c1-300; ls -la /tmp/claude-1001/regr.pkl 2>&1
```

```
Exit code 2
9         3    4   M  P33Y  2000-01-04   24.000000    96          96    71           16     193     r_wrist        24.0                      0
10        3    5   M  P33Y  2000-01-05   24.000000    96          96    76           16     137     r_wrist        24.0                      0
11        3    6   M  P33Y  2000-01-06   24.000000    96          96    79           16     114     r_wrist        24.0                      0
12        4    3   F  P19Y  2000-01-03   15.653244    84          84    67            0      35     l_wrist        24.0                     22
13        4    4   F  P19Y  2000-01-04   24.000000    84          84    80            0      98     l_wrist        24.0                      0
ls: cannot access '/tmp/claude-1001/regr.pkl': No such file or directory
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python3 - <<'EOF'
s=open('ajile.py').read()
s=s.replace('''    from sklearn.linear_model import HuberRegressor
    feats = list(dict.fromkeys(names))
    Xs = X[:, chosen]''','''    from sklearn.linear_model import HuberRegressor
    import warnings
    from sklearn.exceptions import ConvergenceWarning
    feats = list(dict.fromkeys(names))
    Xs = X[:, chosen]
    nonconv = [0]

    def fit(A, b):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always", ConvergenceWarning)
            m = HuberRegressor().fit(A, b)
        nonconv[0] += sum(issubclass(x.category, ConvergenceWarning) for x in w)
        return m''')
s=s.replace('''        m = HuberRegressor().fit(Xs[tr], y[tr])
        full = r2(y[test], m.predict(Xs[test]))''','''        m = fit(Xs[tr], y[tr])
        full = r2(y[test], m.predict(Xs[test]))''')
s=s.replace('''                ms = HuberRegressor().fit(Xtr, y[tr])''','''                ms = fit(Xtr, y[tr])''')
s=s.replace('''    out = dict(r2=float(np.mean(r2s)), coef=np.mean(coefs, axis=0))
    if delta:''','''    out = dict(r2=float(np.mean(r2s)), coef=np.mean(coefs, axis=0), fits=len(splits) * (1 + (len(feats) if delta else 0)),
               nonconverged=nonconv[0])
    if delta:''')
s=s.replace('''                main = fit_models(X, names, y, splits90, chosen)
                row["r2"] = main["r2"]''','''                main = fit_models(X, names, y, splits90, chosen)
                row["r2"] = main["r2"]
                row["nonconverged"] = main["nonconverged"]''')
open('ajile.py','w').write(s)
EOF
cd $TMPDIR && python3 - <<'EOF'
s=open('harness.py').read()
lines=s.split('\n')
i=[k for k,l in enumerate(lines) if l.startswith('nb=nbformat.read')][0]
body='\n'.join('    '+l for l in lines[i:])
s='\n'.join(lines[:i])+"\nif __name__=='__main__':\n"+body
open('harness.py','w').write(s)
EOF
. dev/bin/activate && python build_nb.py >/dev/null && date -u && timeout 3000 python -u harness.py 95 2>&1 | grep -v "warnings.warn\|ConvergenceWarning\|^ *warn" | sed -n '/===== cell 76/,$p' | cut -c1-250
```

```
Wed Nov 25 06:25:04 UTC 2026
===== cell 76
models per subject (electrodes): {np.int64(1): 85, np.int64(2): 79, np.int64(3): 69, np.int64(4): 58, np.int64(5): 99, np.int64(6): 62, np.int64(7): 61, np.int64(8): 68, np.int64(9): 94, np.int64(10): 96, np.int64(11): 102, np.int64(12): 103} ; elect
regression 1326 s, 3904 models
      count    mean     std     min     25%     50%     75%     max
band                                                               
hfb   976.0 -0.0222  0.0306 -0.1829 -0.0344 -0.0148 -0.0076  0.1773
lfb   976.0 -0.0215  0.0300 -0.1473 -0.0343 -0.0145 -0.0070  0.1039
----- 1325.6s
===== cell 78
largest split-averaged withheld R2 (90/10, band mean): 0.1773 (S07, electrode 10, hfb)
largest with 80/20 splits: 0.1837 ; with band median: 0.1578
models with R2 > 0.05: {'hfb': 14, 'lfb': 14} of {'hfb': 976, 'lfb': 976}
ten largest:
      subject  electrode band      r2   r2_80
1845        7         10  hfb  0.1773  0.1837
1565        6          2  hfb  0.1340  0.1289
1101        4         57  hfb  0.1123  0.0857
872         3         62  lfb  0.1039  0.1054
844         3         52  lfb  0.0939  0.0853
[... 85 more lines not kept]
```

**Agent**

Dev run complete: regression takes 22 min, so the full notebook should run in about 40 min. Pulling the post-fix numbers for the spectral claims before writing conclusions.

**Agent calls Bash**

```bash
F=/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/f827794a-c716-4e85-a39e-d824755c2636/tool-results/bl5vra1gm.txt; grep -v "warnings.warn\|ConvergenceWarning\|^ *warn" $F | sed -n '/===== cell 12$/,/===== cell 56/p' | cut -c1-220 | grep -v "^ *[0-9]* *[ab] *[0-9]* *[0-9]* *[0-9.]* *[0-9.]* *[0-9.]* *True"
```

```
<persisted-output>
Output too large (64.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/f827794a-c716-4e85-a39e-d824755c2636/tool-results/bc2ptca4j.txt

Preview (first 2KB):
===== cell 12
         events  no_ecog  nan_data  zeroed  below_0dB  hf_3sd  kept
subject                                                            
1           741      132         6       0          0       0   603
2           305        0         3       0          0       6   296
3           642        0         0       0          0       5   637
4           417       22         5       0          0       0   390
5           267        0         0       0          0       3   264
6           956       83        28       0          0      14   831
7           800        0         6       0          0       6   788
8           965        0        10       0          0      10   945
9           211        0         0       0          0       1   210
10          806        0        47       0          0      14   745
11          982        0        10       0          1       6   965
12          996        0        10       0          0      10   976
segment power (dB, uV^2/Hz, mean 1-200 Hz): range -9.47 to 33.67
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
F=/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/f827794a-c716-4e85-a39e-d824755c2636/tool-results/bc2ptca4j.txt; grep -E "^=====|reading|within|holding|seed \+|part|subjects whose|named|three|largest|\(a\)|\(b\)|significant|all three|p < 0.001|measured|ratio part|five|bimodal|fraction of bins|^(middle|precentral|postcentral|inferior|supramarginal|superior)" $F | cut -c1-200 | head -150
```

```
===== cell 12
===== cell 13
===== cell 14
seed + 1000 subjects beating every shuffle: 12
seed + 2000 subjects beating every shuffle: 12
seed + 3000 subjects beating every shuffle: 12
seed + 4000 subjects beating every shuffle: 12
===== cell 11
===== cell 12
seed + 1000 subjects beating every shuffle: 12
seed + 2000 subjects beating every shuffle: 12
seed + 3000 subjects beating every shuffle: 12
seed + 4000 subjects beating every shuffle: 12
===== cell 11
===== cell 12
===== cell 13
seed + 1000 subjects beating every shuffle: 12
seed + 2000 subjects beating every shuffle: 12
seed + 3000 subjects beating every shuffle: 12
seed + 4000 subjects beating every shuffle: 12
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('build_claims.py').read()
s=s.replace('''print(MAIN.groupby("band").r2.describe().round(4).to_string())
''','''print(MAIN.groupby("band").r2.describe().round(4).to_string())
print("Huber fits that did not converge (main models, 200 fits each):", int(MAIN.nonconverged.sum()), "of", 200 * len(MAIN),
      "; models with any:", int((MAIN.nonconverged > 0).sum()))
''')
open('build_claims.py','w').write(s)
EOF
. dev/bin/activate && python build_nb.py >/dev/null && date -u && timeout 3000 python -u harness.py 97 > dev_out.txt 2>&1; date -u; grep -c . dev_out.txt
```

```
Wed Nov 25 06:52:02 UTC 2026
Wed Nov 25 06:56:05 UTC 2026
791
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "warnings.warn\|ConvergenceWarning\|^ *warn" dev_out.txt | sed -n '/===== cell 12$/,/===== cell 59/p' | grep -v "^ *[0-9]\+ \+[ab] \+[0-9]\+" | cut -c1-200 | sed -n '1,400p' | grep -v "^S[01][0-9] " | head -150
```

```
===== cell 12
         events  no_ecog  nan_data  zeroed  below_0dB  hf_3sd  kept
subject                                                            
1           741      132         6       0          0       0   603
2           305        0         3       0          0       6   296
3           642        0         0       0          0       5   637
4           417       22         5       0          0       0   390
5           267        0         0       0          0       3   264
6           956       83        28       0          0      14   831
7           800        0         6       0          0       6   788
8           965        0        10       0          0      10   945
9           211        0         0       0          0       1   210
10          806        0        47       0          0      14   745
11          982        0        10       0          1       6   965
12          996        0        10       0          0      10   976
segment power (dB, uV^2/Hz, mean 1-200 Hz): range -9.47 to 33.67
region power without baseline (dB): range -26.4 to 71.3
NaN region values among kept events: 0
----- 0.1s
===== cell 13
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import sys, numpy as np
sys.path.insert(0,'entries/peterson-2021')
import ajile
a=np.array([-67,-105,42,10,170,-170,95,-95])
print(ajile.fold_angle(-a))
import pickle; D=pickle.load(open('dev_spec.pkl','rb')); ev=ajile.event_table(D['metas'])
print((ev.angle>0).mean(), (ev.angle_raw<0).mean(), np.percentile(ev.angle,[10,25,50,75,90]))
EOF
```

```
[ 67.  75. -42. -10. -10.  10. -85.  85.]
0.6833580613254204 0.6833580613254204 [-66.02816238 -18.74409055  39.03802542  70.53642682  82.91771172]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "warnings.warn\|ConvergenceWarning\|^ *warn" dev_out.txt | sed -n '/===== cell 37$/,/===== cell 59/p' | grep -E "=====|reading|within|holding|seed \+|part|subjects whose|named|three|largest|\(a\)|\(b\)|significant|fraction|^[a-z ]{8,20} +-?[0-9]" | cut -c1-220
```

```
===== cell 37
   reading  subject    n  contra_peak  ipsi_peak   ratio  holds
reading
===== cell 40
                                 pair  paper    r_b    r_a  within_b  within_a
within tolerance, reading b: 5 of 6; reading a: 5 of 6
===== cell 43
day        3    4    5    6    7
subjects whose busiest day holds > half: [5, 9] ; named S04, S05, S09
day part exact: False ; waking part (all subjects > half): True
events in 0-8 h by subject: {1: 28, 2: 108, 3: 185, 4: 61, 5: 44, 6: 89, 7: 88, 8: 88, 9: 33, 10: 99, 11: 200, 12: 142}
reading a, subjects whose busiest day holds > half: [5, 9]
===== cell 46
middle frontal    -0.336   0.172 -0.293   0.149     True     True
precentral        -0.758   0.445 -0.622   0.408     True     True
postcentral       -0.773   0.467 -0.647   0.439     True     True
inferior parietal -0.589   0.262 -0.528   0.249     True     True
supramarginal     -0.266   0.010 -0.190   0.007     True     True
superior temporal -0.127  -0.002 -0.103   0.000    False    False
middle temporal   -0.003   0.002  0.000   0.006     True    False
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "warnings.warn\|ConvergenceWarning\|^ *warn" dev_out.txt | sed -n '/===== cell 61$/,$p' | grep -E "=====|band|of 24|of 12|reduced in|largest|part|levels|fraction|Huber|top two|LFB|HFB|\(a\)|\(b\)|seed|own|regions|projected|angle|notebook" | grep -v "^ *[0-9]\+ \+[0-9]\+ \+[lh]fb" | cut -c1-250
```

```
===== cell 61
LFB band mean: H = 749.8, p = 0, n = 7650 events in 12 subjects
LFB band median: H = 775.8, p = 0, n = 7650 events in 12 subjects
HFB band mean: H = 1048.2, p = 0, n = 7650 events in 12 subjects
HFB band median: H = 1011.9, p = 0, n = 7650 events in 12 subjects
===== cell 64
    subject band  paper_lo  paper_hi  mean_of_bandmean  in_mean_of_bandmean  median_of_bandmean  in_median_of_bandmean ci_median_bandmean  mean_of_bandmedian  in_mean_of_bandmedian  median_of_bandmedian  in_median_of_bandmedian ci_median_bandmedian
in_mean_of_bandmean 21 of 24
in_median_of_bandmean 18 of 24
in_mean_of_bandmedian 17 of 24
in_median_of_bandmedian 18 of 24
LFB below 0 (median of band mean): 12 of 12; HFB above 0: 12 of 12
===== cell 67
    subject band  paper_sig  p_bandmean  agree_bandmean  p_bandmedian  agree_bandmedian                            day_means
pairs agreeing, band mean: 20 of 24; band median: 19 of 24
===== cell 70
(a) precentral, per subject
    subject band  sd_with  sd_without  reduced
(b) per good electrode
    subject band  electrodes  frac_reduced  n_reduced  median_sd_with  median_sd_without
[... 71 more lines not kept]
```

**Agent**

Dev results are in. Writing the notebook header, conclusions and summary now, then the entry files, so the single full run (~40 min) produces the final executed copy.

**Agent calls Bash**

```bash
date -u; ls tools; python tools/entry.py --help 2>&1 | head -20; cat entries/fouke-2025/README.md | head -30
```

```
Wed Nov 25 06:57:06 UTC 2026
__pycache__
agent_run.py
archive_transcripts.sh
archives
author_notes.py
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_osf_targets.py
build_reuse_targets.py
build_site.py
build_sparc_targets.py
build_targets.py
build_zenodo_targets.py
changed_entries.py
claims_check.py
[... 75 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/header.md",
 "content": "# Reproducing Peterson et al. (2021) from DANDI:000055\n\nPaper: Peterson, Singh, Wang, Rao and Brunton (2021), \"Behavioral and Neural Variability of\nNaturalistic Arm Movements\", eNeuro 8(3), ENEURO.0007-21.2021, doi:10.1523/eneuro.0007-21.2021.\n\nDataset: DANDI:000055 (AJILE12), version 0.261123.1703 (doi:10.48324/dandi.000055/0.261123.1703).\nThis version was asked for in the prompt of this attempt, a repeat attempt that tests what the\ndataset holds now. It holds 55 NWB files, one per subject and recording day, with ECoG at 500 Hz,\npose at 30 Hz, the contralateral wrist movement events and their features. Every file is streamed;\nnothing is downloaded.\n\nClaims: `claims/peterson-2021.yaml`, written from the version of record (Europe PMC, PMC8225404)\nand checked by a second reader. Method details the claims file does not give are taken from the\npaper's Methods and its code (github.com/BruntonUWBio/naturalistic_arm_movements_ecog, commit\n04c6faf2f219586fa834d10c614ef48a694cec55), cited where they are used. Outside input: the paper's\nprojection matrices from electrodes to regions, Figshare item 12114408 version 1\n(doi:10.6084/m9.figshare.12114408.v1).\n\nThe notebook runs for about 40 minutes: about 12 minutes to stream the ECoG around 8088 events\n(about 150 GB of compressed chunks) and about 25 minutes for the 3904 regression models.\n\n| Claim | Tested | Outcome |\n|---|---|---|\n| subject-days | yes | reproduced |\n| roi-projection-link | yes (with the Figshare matrices) | reproduced |\n| cohort | yes | partially reproduced |\n| fig2-event-counts | yes | not reproduced |\n| fig2-features-differ-across-subjects | yes | reproduced |\n| fig2-reach-shape | yes | partially reproduced |\n| fig2-bimanual-skew | yes | reproduced |\n| extfig2-1c-contralateral-larger | yes | reproduced |\n| extfig2-2-feature-correlations | yes | partially reproduced |\n| fig2-days-and-waking | yes | partially reproduced |\n| fig3-group-lfb-decrease-hfb-increase | yes | reproduced |\n| fig3-sensorimotor-largest | yes | reproduced |\n| fig3-lfb-more-widespread | yes | blocked (methods underspecified: the readings disagree) |\n| fig4-precentral-subject-variability | yes | partially reproduced |\n| fig5-band-power-differs-across-subjects | yes | reproduced |\n| table1-subject-band-power-ci | yes | partially reproduced |\n| fig5-recording-day-effects | yes | partially reproduced |\n| extfig5-1-baseline-reduces-day-variability | yes | reproduced |\n| discussion-day-changes-small | yes | reproduced |\n| fig6b-best-models-sensorimotor | yes | reproduced |\n| fig6-r2-at-most-025 | yes | reproduced |\n| fig6c-angle-and-day-most-informative | yes | reproduced |\n| extfig6-2-angle-most-retained | yes | partially reproduced |\n| fig6d-upward-reaches-enhance-pattern | yes | reproduced |\n| fig6d-angle-and-day-largest-coefficients | yes | reproduced |\n\nAssumptions (the paper leaves these open; each is stated where it is used): how the segment\nrejection pools power over electrodes and frequencies; that each event uses the good-electrode flags\nof its own file for the region projection, and that the regression and electrode-level analyses use\nthe electrodes good in every file of the subject.\n"
}
```

```
<tool_use_error>File has not been read yet. Read it first before writing to it.</tool_use_error>
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/results.py",
 "content": "RESULTS = {\n\"link\": \"\"\"**Result: reproduced.** The paper's code rule (keep the non-zero rows, drop the first) leaves as\nmany rows as electrodes with a position in all 12 subjects; the dropped first row is the electrode\ndensity of each region, and the regions whose mean density exceeds 3 are exactly the eight of the\nclaims file. For every subject the largest-weight region is the nearest region centroid for 36 to\n55% of electrodes, against at most 14 electrodes in 200 shuffles of the electrode order, under all\nfive seeds. The 16 electrodes of S03 and the 8 of S12 without positions have no row; they get no\nweight.\"\"\",\n\"subject-days\": \"\"\"**Result: reproduced.** The dataset's subjects 01 to 12 have exactly the days of Table 2, 55\nsubject-days in all.\"\"\",\n\"cohort\": \"\"\"**Result: partially reproduced.** Twelve subjects, 8 male, mean age 29.42 years (SD 7.94), 84.83 surface\nelectrodes on average and 5 right-hemisphere implants match. Electrode groups described as depth\nare in 7 subjects, not 5 (S01, S02, S03, S09, S10, S11, S12), with 23.71 depth electrodes on\naverage, within the stated SD of 23.2.\"\"\",\n\"fig2-event-counts\": \"\"\"**Result: not reproduced.** Under no reading are all three values within tolerance. All events: 211\nto 996, median 770.5. After the segment rejection: 210 to 976, median 691.0. Events with ECoG and\nno missing samples: 211 to 986, median 700.5. The paper gives 151 to 947, median 640; the fewest\nevents are 210 or more in every reading, outside 151 +- 15.1.\"\"\",\n\"fig2-features-differ-across-subjects\": \"\"\"**Result: reproduced.** All ten features differ across subjects (Kruskal-Wallis), with the largest p\n1.1e-32 (reach duration) on the events of reading (b), and p < 0.001 for all ten on all events.\"\"\",\n\"fig2-reach-shape\": \"\"\"**Result: partially reproduced.** Most reaches last under 2 s (88 to 95% per subject, 91.8% pooled)\nand cover under 200 pixels (59 to 100% per subject, 91.3% pooled), in all 12 subjects. The angle\npart fails: the density of the folded angle has its two highest maxima within 15 degrees of -90 and\n+90 with a lower density at 0 in none of the 12 subjects and not pooled. Pooled, the maxima are at\n-71.5 and +75 degrees, and the density at 0 (0.00407) is above the lower maximum (0.004). Reading\n(a) gives the same.\"\"\",\n\"fig2-bimanual-skew\": \"\"\"**Result: reproduced.** The median bimanual ratio is below 0.5 and the overlap skewness positive in\n12 of 12 subjects and pooled (0.14 and 1.11); more than half of the events are bimanual in 12 of 12\n(73% pooled). S02, S04 and S05 are among the five subjects with the highest median ratio and among\nthe five with the lowest overlap skewness.\"\"\",\n\"extfig2-1c-contralateral-larger\": \"\"\"**Result: reproduced.** In all 12 subjects, under both readings of the rest position, the peak of the\nmedian contralateral displacement over 0 to 1.5 s exceeds that of the ipsilateral wrist; the ratio\nis 1.06 to 41.5 (reading b, smallest for S05 and S04, which move both arms most).\"\"\",\n\"extfig2-2-feature-correlations\": \"\"\"**Result: partially reproduced.** Five of the six correlations are within 10% of the paper's under\nboth event sets. Reach magnitude and duration correlate at r = 0.229 (reading b), below 0.26 - 0.026.\"\"\",\n\"fig2-days-and-waking\": \"\"\"**Result: partially reproduced.** Events are mostly in waking hours: 63 to 95% of each subject's events\nfall between 08:00 and 24:00. The busiest day holds more than half of the events for S05 (0.606) and\nS09 (0.519) and for no other subject; for S04 it holds 0.403, so the day part does not hold.\"\"\",\n\"fig3-group-lfb-decrease-hfb-increase\": \"\"\"**Result: reproduced.** In precentral, postcentral and inferior parietal regions the masked group\npower over 4-30 Hz is below 0 and over 50-120 Hz above 0, both over 0 to 0.5 s (for example\nprecentral -0.758 and 0.445 dB) and at the bin of 0 s, under all five seeds. Middle frontal and\nsupramarginal show the same pattern; the temporal regions do not.\"\"\",\n\"fig3-sensorimotor-largest\": \"\"\"**Result: reproduced.** Under all three readings and all five seeds the three largest regions are\npostcentral, precentral and inferior parietal, and each temporal region is below all three (for\nreading a, 0.462, 0.447 and 0.296 dB against at most 0.032).\"\"\",\n\"fig3-lfb-more-widespread\": \"\"\"**Result: blocked (methods underspecified).** The readings disagree. Reading (b), bins per frequency\nbin, gives 34.2 significant negative low-frequency bins against 23.9 positive high-frequency bins,\nand holds under all five seeds. Reading (a), regions with any significant bin, gives 7 against 7\n(not larger), and 6 or 8 against 8 under the other seeds. Supramarginal (30 bins) and superior\ntemporal (23 bins) do have significant low-frequency decreases.\"\"\",\n\"fig4-precentral-subject-variability\": \"\"\"**Result: partially reproduced.** Three of four parts hold. S03, S06, S07, S08 and S11 have positive\npower at 116 and 121 Hz; S09 and S12 peak at 66 and 71 Hz with little power above 100 Hz; S04 and S08\nare among the three subjects with the narrowest low-frequency decrease (2 bins, with S07). Part 1\nfails in one subject: S09 has a mean of -0.03 dB over 76-100 Hz.\"\"\",\n\"fig5-band-power-differs-across-subjects\": \"\"\"**Result: reproduced.** Precentral band power differs across the 12 subjects in both bands, for band\nmeans and band medians (Kruskal-Wallis H = 750 to 1048, p below the smallest double).\"\"\",\n\"table1-subject-band-power-ci\": \"\"\"**Result: partially reproduced.** Under the best reading (mean over events of the band mean), 21 of\n24 subject and band values lie in Table 1's intervals; the other readings give 17 or 18. The three\noutside are S03 HFB (1.235 against 1.39 to 1.67), S06 LFB (-1.036 against -1.63 to -1.11) and S06 HFB\n(1.596 against 2.02 to 2.37). LFB power is below 0 and HFB power above 0 in all 12 subjects (median\nof band means).\"\"\",\n\"fig5-recording-day-effects\": \"\"\"**Result: partially reproduced.** With band means, 20 of 24 subject and band pairs agree with the\npaper (19 with band medians). The day effect is significant where the paper finds none for S01 LFB\n(p = 0.044), S01 HFB (p = 0.029) and S06 HFB (p = 8.5e-11), and not significant for S10 HFB\n(p = 0.10), where the paper finds one.\"\"\",\n\"extfig5-1-baseline-reduces-day-variability\": \"\"\"**Result: reproduced.** Baseline subtraction lowers the SD of day means in 10 of 12 subjects for LFB\nand 11 of 12 for HFB (reading a), and at 91% and 90% of electrodes (reading b). Variability remains:\nday effects are significant in 11 subject and band pairs (fig5-recording-day-effects), with SDs of\nup to 0.85 dB after subtraction.\"\"\",\n\"discussion-day-changes-small\": \"\"\"**Result: reproduced.** The largest deviation of a day mean from the subject mean is 1.48 dB (S06 HFB),\nat most 2.2 dB in every subject and band. Without baseline subtraction the precentral band power is\n12.2 to 36.5 dB in microvolts squared, within 9 to 55 dB; in volts squared it would be about -108 to\n-84 dB.\"\"\",\n\"fig6-r2-at-most-025\": \"\"\"**Result: reproduced.** The largest split-averaged withheld R2 is 0.177 (S07, HFB), at most 0.275. It is\n0.184 with 80/20 splits and 0.158 with band medians, and 0.165 to 0.184 under the other four seeds.\"\"\",\n\"fig6b-best-models-sensorimotor\": \"\"\"**Result: reproduced.** Of the models with R2 > 0.05 (14 per band), all LFB and 13 of 14 HFB electrodes\nare in the five frontoparietal regions, and the median R2 of sensorimotor electrodes is above that\nof temporal ones in both bands. Projected onto the regions, the three highest are precentral,\npostcentral and middle frontal in both bands.\"\"\",\n\"fig6c-angle-and-day-most-informative\": \"\"\"**Result: reproduced.** Over the 14 LFB models with R2 > 0.05, recording day (median Delta R2 0.038) and\nreach angle (0.032) are the two most informative features; the other eight have medians of 0. The\nsame two lead in HFB, and under the code's Delta R2 and the code's selection by LFB R2.\"\"\",\n\"extfig6-2-angle-most-retained\": \"\"\"**Result: partially reproduced.** Reach angle is the most often retained feature in precentral,\npostcentral and inferior parietal regions for both bands (0.52 averaged over these). The order of the\nnext four does not hold: over the sensorimotor regions it is speech ratio, duration, magnitude and\nonset speed, and over all regions speech ratio, magnitude, bimanual class and onset speed.\"\"\",\n\"fig6d-upward-reaches-enhance-pattern\": \"\"\"**Result: reproduced.** Over models with R2 > 0.05 the median reach angle coefficient is -0.70 for LFB\n(13 of 14 negative) and +0.54 for HFB (13 of 14 positive); with the code's selection by LFB R2 the\nHFB median is +0.24.\"\"\",\n\"fig6d-angle-and-day-largest-coefficients\": \"\"\"**Result: reproduced.** Under both readings, recording day (SD of its one-hot coefficients) and reach\nangle have the two largest coefficient magnitudes in both bands: LFB 0.98 and 0.70, HFB 0.71 and 0.54.\nThe code's selection by LFB R2 gives the same two.\"\"\",\n}\n"
}
```

```
File created successfully at: /tmp/claude-1001/results.py (file state is current in your context — no need to Read it back)
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/header.md"
}
```

```
1	# Header placeholder
2
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/day effects are significant in 11 subject and band pairs/day effects are significant in 13 subject and band pairs/' results.py && grep -v "warnings.warn\|ConvergenceWarning\|^ *warn" dev_out.txt | sed -n '/===== cell 37$/,/===== cell 40/p' | head -30; grep -v "warnings.warn" dev_out.txt | sed -n '/===== cell 43$/,/===== cell 46/p' | sed -n '/busiest_day_frac/,/^subjects/p'
```

```
===== cell 37
cell37:10: RuntimeWarning: Mean of empty slice
   reading  subject    n  contra_peak  ipsi_peak   ratio  holds
0        a        1  603       65.976     12.165   5.424   True
1        a        2  296       60.161     35.804   1.680   True
2        a        3  637       63.300     22.163   2.856   True
3        a        4  390       54.758     48.779   1.123   True
4        a        5  264       52.092     43.855   1.188   True
5        a        6  831       81.695     12.327   6.628   True
6        a        7  788       50.162     22.566   2.223   True
7        a        8  945      150.967     21.280   7.094   True
8        a        9  210       38.884      6.989   5.564   True
9        a       10  745       68.579     22.252   3.082   True
10       a       11  965       60.416     10.790   5.599   True
11       a       12  976       88.279      2.317  38.096   True
12       b        1  603       64.890      8.795   7.378   True
13       b        2  296       60.762     34.719   1.750   True
14       b        3  637       61.752     19.023   3.246   True
15       b        4  390       52.276     40.309   1.297   True
16       b        5  264       51.309     48.207   1.064   True
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/is 1.06 to 41.5 (reading b/is 1.06 to 42.0 (reading b/; s/for S04 it holds 0.403/for S04 it holds 0.400/; s/63 to 95% of each subject/64 to 95% of each subject/' results.py && grep -c "42.0\|0.400\|64 to 95" results.py
```

```
3
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/header.md",
 "content": "# Reproducing Peterson et al. (2021) from DANDI:000055\n\nPaper: Peterson, Singh, Wang, Rao and Brunton (2021), \"Behavioral and Neural Variability of\nNaturalistic Arm Movements\", eNeuro 8(3), ENEURO.0007-21.2021, doi:10.1523/eneuro.0007-21.2021.\n\nDataset: DANDI:000055 (AJILE12), version 0.261123.1703 (doi:10.48324/dandi.000055/0.261123.1703).\nThis version was asked for in the prompt of this attempt, a repeat attempt that tests what the\ndataset holds now. It holds 55 NWB files, one per subject and recording day, with ECoG at 500 Hz,\npose at 30 Hz, the contralateral wrist movement events and their features. Every file is streamed;\nnothing is downloaded.\n\nClaims: `claims/peterson-2021.yaml`, written from the version of record (Europe PMC, PMC8225404)\nand checked by a second reader. Method details the claims file does not give are taken from the\npaper's Methods and its code (github.com/BruntonUWBio/naturalistic_arm_movements_ecog, commit\n04c6faf2f219586fa834d10c614ef48a694cec55), cited where they are used. Outside input: the paper's\nprojection matrices from electrodes to regions, Figshare item 12114408 version 1\n(doi:10.6084/m9.figshare.12114408.v1).\n\nThe notebook runs for about 40 minutes: about 12 minutes to stream the ECoG around 8088 events\n(about 150 GB of compressed chunks) and about 25 minutes for the 3904 regression models.\n\n| Claim | Tested | Outcome |\n|---|---|---|\n| subject-days | yes | reproduced |\n| roi-projection-link | yes (with the Figshare matrices) | reproduced |\n| cohort | yes | partially reproduced |\n| fig2-event-counts | yes | not reproduced |\n| fig2-features-differ-across-subjects | yes | reproduced |\n| fig2-reach-shape | yes | partially reproduced |\n| fig2-bimanual-skew | yes | reproduced |\n| extfig2-1c-contralateral-larger | yes | reproduced |\n| extfig2-2-feature-correlations | yes | partially reproduced |\n| fig2-days-and-waking | yes | partially reproduced |\n| fig3-group-lfb-decrease-hfb-increase | yes | reproduced |\n| fig3-sensorimotor-largest | yes | reproduced |\n| fig3-lfb-more-widespread | yes | blocked (methods underspecified: the readings disagree) |\n| fig4-precentral-subject-variability | yes | partially reproduced |\n| fig5-band-power-differs-across-subjects | yes | reproduced |\n| table1-subject-band-power-ci | yes | partially reproduced |\n| fig5-recording-day-effects | yes | partially reproduced |\n| extfig5-1-baseline-reduces-day-variability | yes | reproduced |\n| discussion-day-changes-small | yes | reproduced |\n| fig6b-best-models-sensorimotor | yes | reproduced |\n| fig6-r2-at-most-025 | yes | reproduced |\n| fig6c-angle-and-day-most-informative | yes | reproduced |\n| extfig6-2-angle-most-retained | yes | partially reproduced |\n| fig6d-upward-reaches-enhance-pattern | yes | reproduced |\n| fig6d-angle-and-day-largest-coefficients | yes | reproduced |\n\nAssumptions (the paper leaves these open; each is stated where it is used): how the segment\nrejection pools power over electrodes and frequencies; that each event uses the good-electrode flags\nof its own file for the region projection, and that the regression and electrode-level analyses use\nthe electrodes good in every file of the subject.\n"
}
```

```
The file /tmp/claude-1001/header.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/summary.md <<'EOF'
## Summary

| Claim | Outcome |
|---|---|
| subject-days | reproduced |
| roi-projection-link | reproduced |
| cohort | partially reproduced (depth electrodes in 7 subjects, not 5) |
| fig2-event-counts | not reproduced (210 to 976 events per subject, median 691) |
| fig2-features-differ-across-subjects | reproduced |
| fig2-reach-shape | partially reproduced (no angle density peaks within 15 degrees of +-90) |
| fig2-bimanual-skew | reproduced |
| extfig2-1c-contralateral-larger | reproduced |
| extfig2-2-feature-correlations | partially reproduced (5 of 6) |
| fig2-days-and-waking | partially reproduced (S04's busiest day holds 40%) |
| fig3-group-lfb-decrease-hfb-increase | reproduced |
| fig3-sensorimotor-largest | reproduced |
| fig3-lfb-more-widespread | blocked, methods underspecified (the two readings disagree) |
| fig4-precentral-subject-variability | partially reproduced (3 of 4 parts; S09 has no HFB increase) |
| fig5-band-power-differs-across-subjects | reproduced |
| table1-subject-band-power-ci | partially reproduced (21 of 24) |
| fig5-recording-day-effects | partially reproduced (20 of 24) |
| extfig5-1-baseline-reduces-day-variability | reproduced |
| discussion-day-changes-small | reproduced |
| fig6b-best-models-sensorimotor | reproduced |
| fig6-r2-at-most-025 | reproduced |
| fig6c-angle-and-day-most-informative | reproduced |
| extfig6-2-angle-most-retained | partially reproduced (order of the next four features differs) |
| fig6d-upward-reaches-enhance-pattern | reproduced |
| fig6d-angle-and-day-largest-coefficients | reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

How the analysis differs from the paper's. The paper started from its own curated epochs and
spectral power (Figshare); here everything is computed from the dataset's continuous ECoG, with the
Methods' spectral method and the code's parameters. The segment rejection pools power over the good
electrodes and 1-200 Hz (an assumption). The good-electrode flags differ between a subject's files;
the projection uses each file's flags, and the regression uses electrodes good in every file. The
dataset has no false-positive flag, so none are removed beyond what it holds. The regression's
Delta R2 is computed only where R2 > 0.05 (the only models the claims use), the code's Delta R2
variant is run with the code's 80/20 splits, and the seed check of the regression refits the
full-model R2 only. Bad electrodes are not refit as a variant.

What was found about the dataset (numbers above):

- The subjects and days are those of the paper, and the paper's projection matrices match the
  electrodes in all 12 subjects. The event features, the pose and the ECoG agree with one another:
  the stored reach magnitude equals the one computed from the pose (ratio 1.007), and event-locked
  power changes are present at the true onsets and absent at pseudo-onsets 3 s earlier in 10 of 12
  subjects for HFB and 11 of 12 for LFB. For S09 the neural data could not establish the alignment.
- The ECoG of three files ends hours before the day ends (S01 day 7, S04 day 3, S06 day 3), while the
  pose and the events go on: 237 events have no ECoG. Another 125 events fall on NaN samples.
- The dataset holds more events than the paper analysed (8088; 211 to 996 per subject, median 770.5,
  against 151 to 947, median 640).
- Undocumented conventions: the reach angle is in image coordinates (y down); the bimanual overlap,
  described as a fraction of the movement, is in seconds (1661 events above 1); the pose is labelled
  meters but is in pixels; good-electrode flags differ between a subject's files; 24 electrodes
  (S03, S12) have no position; the electrodes table carries R2 columns without a description.
- One event (S08 day 4) is at 40.3 s in ReachEvents and at 86440.3 s in the reaches table.
- Electrode groups described as depth are in 7 subjects, where the paper reports 5.
EOF
cd $TMPDIR && python3 - <<'EOF'
s=open('build_nb.py').read()
s=s.replace('''nb = nbf.v4.new_notebook()
nb.cells = cells
exec(open("/tmp/claude-1001/build_claims.py").read())''','''nb = nbf.v4.new_notebook()
exec(open("/tmp/claude-1001/build_claims.py").read())
exec(open("/tmp/claude-1001/results.py").read())
import re as _re
for c in cells:
    if c.cell_type == "markdown":
        m = _re.match(r"\\*\\*Result: \\.\\.\\.\\*\\* \\((.+)\\)$", c.source.strip())
        if m:
            c.source = RESULTS[m.group(1)]''')
open('build_nb.py','w').write(s)
EOF
. dev/bin/activate && python build_nb.py && grep -c "Result: \.\.\." entries/peterson-2021/reproduce_peterson_2021.ipynb
```

```
98 cells
0
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/absent at pseudo-onsets 3 s earlier in 10 of 12\n//' summary.md && python3 - <<'EOF'
s=open('/tmp/claude-1001/summary.md').read()
s=s.replace("""power changes are present at the true onsets and absent at pseudo-onsets 3 s earlier in 10 of 12
  subjects for HFB and 11 of 12 for LFB. For S09 the neural data could not establish the alignment.""","""power changes at the true onsets differ from those at pseudo-onsets 3 s earlier (Wilcoxon p < 0.05)
  in 11 of 12 subjects for LFB and 9 of 12 for HFB. For S09 neither band differs, so the neural data
  could not establish the alignment there.""")
open('/tmp/claude-1001/summary.md','w').write(s)
EOF
. dev/bin/activate && python build_nb.py && cd entries/peterson-2021 && cat > requirements.in <<'EOF'
h5py
ipykernel
matplotlib
numpy
pandas
remfile
requests
scikit-learn
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: peterson-2021
type: reproduction
title: Behavioral and neural variability of naturalistic arm movements (Peterson et al. 2021)
description: Tests the findings of Peterson, Singh, Wang, Rao and Brunton (2021) on dandiset 000055
  (AJILE12), which holds the ECoG, pose and wrist movement events of the paper's 12 subjects over 55
  days. It checks the cohort and the events, the behavioural features of Figure 2, the movement-related
  spectral power of Figures 3 to 5 and Table 1, projected to regions with the paper's projection
  matrices from Figshare, and the single-event regression models of Figure 6.
license: Apache-2.0
notebooks:
- path: reproduce_peterson_2021.ipynb
  title: Reproducing Peterson et al. (2021) from dandiset 000055
  runtime_minutes: 40
helpers:
- ajile.py
related:
- id: dandi:000055/0.261123.1703
  relation: uses_data
- id: doi:10.6084/m9.figshare.12114408.v1
  relation: uses_data
- id: doi:10.1523/eneuro.0007-21.2021
  relation: reproduces
EOF
grep -n "relation" ../../schemas/entry.schema.json | head; grep -n '"enum"' -A8 ../../schemas/entry.schema.json | head -40
```

```
98 cells
46:        "required": ["id", "relation"],
53:          "relation": {"enum": ["uses_data", "reproduces", "derived_from", "references"]}
16:    "type": {"enum": ["orientation", "reproduction", "analysis"]},
17-    "title": {"type": "string", "minLength": 1, "maxLength": 300},
18-    "description": {"type": "string", "minLength": 1},
19-    "license": {"description": "SPDX identifier.", "type": "string"},
20-    "python": {"description": "The Python version the entry runs on, major.minor; its lock is compiled for it (tools/entry.py lock). Entries from before the field run on the version their lock names.", "type": "string", "pattern": "^3\\.[0-9]+$"},
21-    "notebooks": {
22-      "type": "array",
23-      "minItems": 1,
24-      "items": {
--
53:          "relation": {"enum": ["uses_data", "reproduces", "derived_from", "references"]}
54-        }
55-      }
56-    }
57-  }
58-}
```

**Agent calls Bash**

```bash
cat > README.md <<'EOF'
# Peterson, Singh, Wang, Rao & Brunton (2021) from dandiset 000055

Tests the findings of [Peterson et al. (2021)](https://doi.org/10.1523/eneuro.0007-21.2021) on
[DANDI:000055](https://dandiarchive.org/dandiset/000055/0.261123.1703) (AJILE12), which holds the
ECoG, pose and wrist movement events of the paper's 12 subjects over 55 days. The ECoG around each
of 8088 events is streamed from the archive, and region power uses the paper's projection matrices
from [Figshare](https://doi.org/10.6084/m9.figshare.12114408.v1).

| Claim | Outcome |
|---|---|
| Subjects and days are the paper's | Reproduced |
| The Figshare projection matrices match the electrodes | Reproduced |
| Cohort: sex, age, electrodes, hemispheres | Partially reproduced |
| 151 to 947 events per subject, median 640 | Not reproduced |
| All ten features differ across subjects | Reproduced |
| Reach duration and magnitude small, angles peak at +-90 | Partially reproduced |
| Bimanual features skewed toward unimanual | Reproduced |
| Contralateral wrist moves more than ipsilateral | Reproduced |
| Feature correlations | Partially reproduced |
| Events even across days except S04, S05, S09; mostly waking | Partially reproduced |
| Group LFB decrease and HFB increase at onset | Reproduced |
| Largest changes in sensorimotor regions | Reproduced |
| LFB decreases more widespread than HFB increases | Blocked: methods underspecified |
| Precentral pattern per subject | Partially reproduced |
| Band power differs across subjects | Reproduced |
| Table 1 intervals | Partially reproduced |
| Recording-day effects per subject | Partially reproduced |
| Baseline subtraction reduces day variability | Reproduced |
| Day-to-day changes are 1-2 dB | Reproduced |
| Best models over sensorimotor areas | Reproduced |
| R2 at most 0.25 | Reproduced |
| Reach angle and day most informative | Reproduced |
| Reach angle most often retained | Partially reproduced |
| Upward reaches enhance the pattern | Reproduced |
| Angle and day have the largest coefficients | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The notebook runs for about 40 minutes. The attempt record, with the reasons and the differences
from the paper's method, is [`attempts/peterson-2021-02.yaml`](../../attempts/peterson-2021-02.yaml).
EOF
cd  && date -u && timeout 900 python tools/entry.py lock entries/peterson-2021 2>&1 | tail -5
```

```
Wed Nov 25 06:58:47 UTC 2026
wrote peterson-2021/requirements.lock.txt (Python 3.13, with hashes)
```

**Agent calls Bash**

```bash
rm -rf entries/peterson-2021/__pycache__; timeout 600 python tools/entry.py check entries/peterson-2021 2>&1 | tail -20
```

```
0 error(s)
```

**Agent**

Entry checks pass. Starting the full run from a clean environment (~40 min, foreground).

**Agent calls Bash**

```bash
date -u; timeout 5400 python tools/entry.py all entries/peterson-2021 2>&1 | tail -30; date -u
```

```
Wed Nov 25 06:59:01 UTC 2026
Installed kernelspec registry-peterson-2021 in executed/peterson-2021/.venv/share/jupyter/kernels/registry-peterson-2021
0 error(s)
pass  reproduce_peterson_2021.ipynb  (2203 s)
Wed Nov 25 07:35:53 UTC 2026
```

**Agent**

Run passed in 36.7 min. Checking the executed outputs against the conclusions.

**Agent calls Bash**

```bash
ls executed/peterson-2021/; cd $TMPDIR && . dev/bin/activate && python - <<'EOF' > exec_out.txt
import nbformat
nb=nbformat.read('executed/peterson-2021/reproduce_peterson_2021.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    print('===== cell',i)
    for o in c.get('outputs',[]):
        if o.get('name')=='stderr': continue
        t=o.get('text') or (o.get('data',{}) or {}).get('text/plain','')
        print(t if isinstance(t,str) else ''.join(t))
EOF
diff <(grep -v "warnings.warn\|ConvergenceWarning\|^ *warn\|^-----\|RuntimeWarning" dev_out.txt | grep -E "within|of 24|of 12|part|largest|reading|top two|seed \+|named|levels|fraction|Huber|subjects whose|in 9-55") <(grep -E "within|of 24|of 12|part|largest|reading|top two|seed \+|named|levels|fraction|Huber|subjects whose|in 9-55" exec_out.txt) | head -40; grep -E "spectral pass|regression [0-9]|notebook run time|^[0-9]+ s$" exec_out.txt
```

```
reproduce_peterson_2021.ipynb
result.json
spectral pass 489 s; peak memory of a worker 1.84 GB
regression 1360 s, 3904 models
207 s
notebook run time 36.6 min; peak memory of this process 1.04 GB
Shell cwd was reset to
```

**Agent**

Executed outputs match the development numbers exactly. Now writing the attempt record; checking the schema first.

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required'))
for k,v in s['properties'].items(): print(k, json.dumps(v)[:300])
" | head -60
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
schema_version {"const": 3}
id {"type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"}
datasets {"description": "Every dataset the attempt used (docs/protocol.md, \"Record the attempt\").", "type": "array", "minItems": 1, "items": {"description": "A dataset the attempt used: the archive, the dataset's identifier there, the pinned version, and how the paper relates to it.", "type": "object", "a
missing_datasets {"description": "Datasets the paper's claims rest on that this attempt could not use; claims that need one are blocked with dataset_missing.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["why"], "properties": {"archive": {"type": "string"}, "id": {"type":
paper {"type": "string", "pattern": "^doi:10\\.[0-9]{4,9}/.+$"}
date {"type": "string", "format": "date"}
entry {"description": "The entry this attempt produced (its name), if any.", "type": "string"}
deprecated {"description": "Set when the attempt no longer stands, for example because its claims were written without the paper's full text. The record is kept as it was; its outcomes are shown but not counted.", "type": "object", "additionalProperties": false, "required": ["date", "reason"], "properties": {"
provenance {"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties": {"kind": {"enum": ["agent", "person"]}, "accountable": {"description": "The person or organisation responsible for this attempt.", "type": "object", "additionalProperties": false, "required": ["name"
outcomes {"description": "One per claim attempted.", "type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["claim", "outcome"], "properties": {"claim": {"description": "Claim id from the target's claims file.", "type": "string"}, "outcome": {"enum": ["reprodu
verifications {"type": "array", "items": {"type": "object", "additio
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
P=s['properties']
print(json.dumps(P['outcomes']['items']['properties'])[:2500]); print()
print(json.dumps(P['findings']['items'])[:2500]); print()
print(json.dumps(P['provenance'])[:1800]); print(json.dumps(P['datasets']['items'])[:800])
"
```

```
{"claim": {"description": "Claim id from the target's claims file.", "type": "string"}, "outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"], "description": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`."}, "blocked_by": {"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "dataset_missing", "too_large", "not_runnable", "other"]}, "notes": {"description": "What differs, or what was missing, stated factually.", "type": "string"}, "notebook": {"description": "Path of the notebook within the entry.", "type": "string"}, "output": {"description": "Which output shows the result, e.g. a cell tag.", "type": "string"}, "measured": {"description": "The values obtained, for claims with expected values: one number, or one per expected value, in the same order.", "oneOf": [{"type": "number"}, {"type": "array", "minItems": 1, "items": {"type": "number"}}]}, "deviations": {"description": "How the test differed from the paper's method or data, e.g. one session of four, or a substituted model.", "type": "array", "items": {"type": "string", "minLength": 1}}, "assumed": {"description": "True when the outcome rests on an assumption about a method the paper leaves open: a choice the paper best supports, stated in a deviation that says what was assumed and why (docs/protocol.md, Author, step 1.6).", "type": "boolean"}, "seed_sensitive": {"type": "boolean", "description": "True when the outcome is not the same under all five seeds the protocol asks for (docs/protocol.md, Author, step 3)."}, "proposed": {"description": "A change of outcome found after the last verification round, held until a further round agrees with it.", "type": "object", "additionalProperties": false, "required": ["outcome", "reason"], "properties": {"outcome": {"enum": ["reproduced", "partially_r
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n '/===== cell 40/,/===== cell 43/p' exec_out.txt; grep -n "mean_age\|largest split" exec_out.txt; date -u
```

```
===== cell 40
                                 pair  paper    r_b    r_a  within_b  within_a
0               magnitude vs duration   0.26  0.229  0.231     False     False
1            magnitude vs onset_speed   0.56  0.610  0.609      True      True
2        duration vs bimanual_overlap   0.48  0.508  0.505      True      True
3  bimanual_overlap vs bimanual_ratio   0.51  0.500  0.501      True      True
4    bimanual_class vs bimanual_ratio   0.50  0.494  0.494      True      True
5  bimanual_overlap vs bimanual_class   0.61  0.596  0.598      True      True
within tolerance, reading b: 5 of 6; reading a: 5 of 6

===== cell 43
265:{'subjects': 12.0, 'male': 8.0, 'mean_age': 29.42, 'sd_age': 7.94, 'mean_surface': 84.83, 'sd_surface': 11.61, 'with_depth': 7.0, 'mean_depth': 23.71, 'sd_depth': 13.39, 'right': 5.0}
268:mean_age: measured 29.42, expected 29.4 +- 7.9: within
705:largest split-averaged withheld R2 (90/10, band mean): 0.1773 (S07, electrode 10, hfb)
Wed Nov 25 07:36:11 UTC 2026
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "attempts/peterson-2021-02.yaml",
 "content": "schema_version: 3\nid: peterson-2021-02\ndatasets:\n- archive: dandi\n  id: \"000055\"\n  version: 0.261123.1703\n  doi: 10.48324/dandi.000055/0.261123.1703\n  relation: primary\npaper: doi:10.1523/eneuro.0007-21.2021\ndate: 2026-11-25\nentry: peterson-2021\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-18\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/encorescience/encore-registry/actions/runs/45551254647\ninputs:\n- what: The paper's projection matrices from electrodes to AAL regions and the region centroids\n    (aal_XX_elecs2ROI.csv and aal_XX_ROIcentroids_Lside.csv for the 12 subjects), read at run time.\n    Used for every claim on regions and for the link claim roi-projection-link.\n  source: doi:10.6084/m9.figshare.12114408.v1\noutcomes:\n- claim: subject-days\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:subject-days\n  notes: The dataset's subjects 01 to 12 have exactly the days of Table 2 (S01 days 3, 4, 5 and 7;\n    S02 and S03 days 3 to 6; S05 days 3, 4 and 7; the others days 3 to 7), 55 subject-days. The\n    subjects are taken as S01 to S12 in order.\n- claim: roi-projection-link\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:roi-projection-link\n  notes: The paper's code rule (keep the rows that are not all zero and drop the first of them,\n    tfr_utils.load_project_spectral_power) leaves exactly as many rows as electrodes with a\n    position in all 12 subjects. The dropped first row is the electrode density of each region (the\n    other rows sum to 1 per region), and the regions with mean density above 3 are exactly the eight\n    of the claims file. The largest-weight region is the region whose centroid is nearest the\n    mirrored electrode position for 36 to 55% of electrodes per subject, against at most 14\n    electrodes in 200 shuffles of the electrode order; all 12 subjects beat every shuffle under all\n    five seeds.\n  deviations:\n  - The criterion's rule as worded (drop all-zero rows) leaves one row too many in every subject and\n    drops the zero rows of the 24 electrodes without a position in S03 and S12. The code's rule\n    (tfr_utils.load_project_spectral_power, commit 04c6faf, `np.nonzero(df.transpose().mean().values\n    != 0)[0][1:]`) also drops the first non-zero row; it is used, and the rows are applied in order\n    to the electrodes with a position. Electrodes without a position get no weight.\n- claim: cohort\n  outcome: partially_reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:cohort\n  measured:\n  - 12\n  - 8\n  - 29.42\n  - 84.83\n  - 7\n  - 23.71\n  - 5\n  notes: Twelve subjects, 8 male, mean age 29.42 years (SD 7.94), 84.83 surface electrodes on average\n    (SD 11.61) and 5 right-hemisphere implants match. Electrode groups described in the files as\n    depth are in 7 subjects (S01 8, S02 16, S03 16, S09 28, S10 48, S11 18, S12 32), not 5; their mean\n    of 23.71 (SD 13.39) is within the stated 23.2 +- 12.1. The ages are the files' ages, which may\n    not be the ages at recording.\n  deviations:\n  - Surface and depth electrodes are told apart by the description of each electrode group (depth\n    when it says depth). The hemisphere is the side of the mean MNI x of the subject's electrodes.\n- claim: fig2-event-counts\n  outcome: not_reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig2-event-counts\n  measured:\n  - 211\n  - 996\n  - 770.5\n  notes: Under reading (a), all events in the files, the counts per subject are 211 to 996 with median\n    770.5. Under reading (b), after the segment rejection, they are 210 to 976 with median 691. With\n    only the events that have ECoG without missing samples, 211 to 986, median 700.5. The fewest\n    events are outside 151 +- 15.1 in every reading, and the median is outside 640 +- 64 in all but\n    none. The dataset has no false-positive flag, so reading (b) cannot drop those events.\n  deviations:\n  - The dataset has no flag for the events the paper removed as false positives; none are dropped\n    for it.\n  - Reading (b) uses the assumed pooling of the segment rejection (see the deviation of\n    fig3-group-lfb-decrease-hfb-increase); 125 events with NaN ECoG samples and 237 without ECoG\n    count as missing data.\n- claim: fig2-features-differ-across-subjects\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig2-features-differ-across-subjects\n  notes: One-way Kruskal-Wallis across the 12 subjects on the 7650 events of reading (b) gives\n    p < 0.001 for all ten features; the largest p is 1.1e-32 (reach duration). Reading (a), all 8088\n    events, gives the same.\n  deviations:\n  - Time of day is the event time in hours after the file's midnight (the files' session\n    description); reach duration is stop_time minus start_time; reach angle is the stored angle\n    negated and folded to -90..90, as the code does, because the stored angle is in image\n    coordinates (checked against the pose).\n- claim: fig2-reach-shape\n  outcome: partially_reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig2-reach-shape\n  notes: Most reaches last under 2 s (88 to 95% per subject, 91.8% pooled) and cover under 200 pixels\n    (59 to 100% per subject, 91.3% pooled), in 12 of 12 subjects. The angle part fails in 0 of 12\n    subjects and pooled. Pooled, the two highest maxima of the folded-angle density are at -71.5 and\n    +75 degrees, and the density at 0 degrees (0.00407) is above the lower maximum (0.004). The\n    kernel density smooths the mass at the +-90 boundary inward, so the maxima fall inside the 15\n    degree window only rarely. Reading (a) gives the same outcome.\n  deviations:\n  - The density is evaluated on a 0.5 degree grid, and the end points of the grid count as maxima\n    when they exceed their neighbour (standard choices, stated in the notebook).\n- claim: fig2-bimanual-skew\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig2-bimanual-skew\n  notes: The median bimanual ratio is below 0.5 in 12 of 12 subjects (0.14 pooled) and the overlap\n    skewness positive in 12 of 12 (1.11 pooled); more than half the events are bimanual in 12 of 12\n    (73% pooled). The five highest median ratios are S04, S07, S05, S02 and S03, and the five lowest\n    overlap skewnesses S07, S05, S02, S03 and S04, so S02, S04 and S05 are among both.\n  deviations:\n  - The files hold no missing bimanual ratios, so the code's fill value of 0.5 is never used.\n- claim: extfig2-1c-contralateral-larger\n  outcome: reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:extfig2-1c-contralateral-larger\n  notes: In all 12 subjects and under both readings of the rest position, the peak over 0 to 1.5 s of\n    the median contralateral displacement exceeds that of the ipsilateral wrist. The ratio is 1.06 to\n    42.0 under reading (b) and 1.12 to 38.1 under reading (a); it is smallest for S05 and S04. The\n    contralateral wrist is the one the ReachEvents description of each file names. 58 of 7650 events\n    have missing pose in the window and are left out of the medians.\n- claim: extfig2-2-feature-correlations\n  outcome: partially_reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:extfig2-2-feature-correlations\n  measured:\n  - 0.229\n  - 0.61\n  - 0.508\n  - 0.5\n  - 0.494\n  - 0.596\n  notes: Five of the six Pearson correlations over the pooled events of reading (b) are within 10% of\n    the paper's; reach magnitude and duration correlate at 0.229, below 0.234. Reading (a) gives 0.231\n    for that pair and the same five matches.\n- claim: fig2-days-and-waking\n  outcome: partially_reproduced\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig2-days-and-waking\n  notes: The waking part holds; 64 to 95% of each subject's events fall between 08:00 and 24:00. The\n    busiest day holds more than half of the events for S05 (0.606, day 7) and S09 (0.519, day 5) and\n    for none of the other subjects; for S04 it holds 0.400 (day 7), so the day part does not hold.\n    Reading (a) gives the same two subjects.\n- claim: fig3-group-lfb-decrease-hfb-increase\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig3-group-lfb-decrease-hfb-increase\n  notes: Over 0 to 0.5 s the masked group power over 4-30 Hz and 50-120 Hz is -0.758 and +0.445 dB in\n    precentral, -0.773 and +0.467 in postcentral, and -0.589 and +0.262 in inferior parietal; at the\n    bin of 0 s the signs are the same. All three hold under both readings and all five seeds. Middle\n    frontal and supramarginal show the pattern too; superior and inferior temporal do not.\n  deviations:\n  - Spectral power is computed from the dataset's continuous ECoG, not from the paper's curated\n    Figshare epochs, with the Methods' and the code's parameters (helper docstring).\n  - Assumed, as the Methods do not say how power is pooled for the segment rejection; Welch power of\n    the 10 s segment averaged over the file's good electrodes, 10*log10 of its mean over 1-200 Hz\n    (below 0 dB drops) and over 115-125 Hz (above the subject's mean + 3 SD drops). Segments with\n    NaN samples or without ECoG count as missing data. 75 events drop for high-frequency power and 1\n    for low power; the rest of the 438 dropped events have no ECoG or NaN samples.\n  - Assumed, as the good-electrode flags differ between a subject's files; each event is projected\n    with the weights of its own file's good electrodes, renormalised to sum 1 per region (code).\n  - The bootstrap mask's Benjamini-Hochberg correction runs over the bins computed here (-1.5 to +1.0\n    s in 0.1 s steps, 25 frequencies); the paper's time range is not stated.\n- claim: fig3-sensorimotor-largest\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig3-sensorimotor-largest\n  notes: Under readings (a), (b) and (c) and all five seeds, the three largest regions are postcentral,\n    precentral and inferior parietal, and each temporal region is below all three. Reading (a) gives\n    0.462, 0.447 and 0.296 dB for the three, 0.193 for middle frontal, and at most 0.032 for the\n    temporal regions.\n  deviations:\n  - The same spectral method and assumptions as fig3-group-lfb-decrease-hfb-increase.\n- claim: fig3-lfb-more-widespread\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig3-lfb-more-widespread\n  notes: The two readings the criterion names disagree, so the claim is blocked as the criterion\n    says. Reading (b), significant bins per frequency bin over 0 to 0.5 s summed over the eight\n    regions, gives 34.2 for low-frequency decreases against 23.9 for high-frequency increases, and\n    holds under all five seeds. Reading (a), regions with any significant bin, gives 7 against 7 under\n    the claim's seed, and 6 or 8 against 8 under the others, so the low count is never larger.\n    Supramarginal (30 bins) and superior temporal (23 bins) have significant low-frequency decreases.\n    The question of which measure the paper meant is recorded for its authors.\n  deviations:\n  - The same spectral method and assumptions as fig3-group-lfb-decrease-hfb-increase.\n- claim: fig4-precentral-subject-variability\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig4-precentral-subject-variability\n  notes: Three of four parts hold. Part 2, S03, S06, S07, S08 and S11 have positive power at 116 and\n    121 Hz. Part 3, S09 and S12 peak among 56-121 Hz at 66 and 71 Hz, with means over 101-121 Hz below\n    half the peak. Part 4, S04 and S08 are among the three subjects with the narrowest low-frequency\n    decrease (2 bins, with S07). Part 1 fails in one subject; S09 has a mean of -0.03 dB over 76-100 Hz\n    (its 8-32 Hz mean is -0.25). The other 11 subjects show the pattern.\n  deviations:\n  - The same spectral method and assumptions as fig3-group-lfb-decrease-hfb-increase.\n- claim: fig5-band-power-differs-across-subjects\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig5-band-power-differs-across-subjects\n  notes: Kruskal-Wallis across the 12 subjects on 7650 events gives H = 750 (LFB) and 1048 (HFB) for\n    band means, and 776 and 1012 for band medians, with p printed as 0 (below the smallest double).\n  deviations:\n  - The same spectral method and assumptions as fig3-group-lfb-decrease-hfb-increase.\n- claim: table1-subject-band-power-ci\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:table1-subject-band-power-ci\n  notes: Under the best of the four readings (the mean over events of the band mean), 21 of 24 subject\n    and band values lie inside Table 1's intervals; the other readings give 18, 17 and 18. Outside\n    are S03 HFB (1.235 against 1.39 to 1.67), S06 LFB (-1.036 against -1.63 to -1.11) and S06 HFB\n    (1.596 against 2.02 to 2.37). The median band mean is below 0 for LFB and above 0 for HFB in all\n    12 subjects. The attempt's own 5000-replicate bootstrap intervals are printed beside them.\n  deviations:\n  - The same spectral method and assumptions as fig3-group-lfb-decrease-hfb-increase.\n- claim: fig5-recording-day-effects\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig5-recording-day-effects\n  notes: With band means 20 of 24 subject and band pairs agree with the paper (19 with band medians).\n    A day effect is found where the paper has none for S01 LFB (p = 0.044), S01 HFB (p = 0.029) and S06\n    HFB (p = 8.5e-11), and is not found for S10 HFB (p = 0.10), where the paper reports p = 0.006. The\n    other ten significant pairs of the paper are significant here (largest p 0.019). S01 lost 132\n    events of day 7, where its ECoG ends early.\n  deviations:\n  - The same spectral method and assumptions as fig3-group-lfb-decrease-hfb-increase.\n- claim: extfig5-1-baseline-reduces-day-variability\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:extfig5-1-baseline-reduces-day-variability\n  notes: Reading (a), baseline subtraction lowers the SD of the precentral day means in 10 of 12\n    subjects for LFB and 11 of 12 for HFB. Reading (b), it lowers it at 91.3% of good electrodes for\n    LFB and 90.4% for HFB. Variability remains; 13 subject and band pairs have a significant day effect\n    (fig5-recording-day-effects), and the SDs after subtraction are 0.03 to 0.85 dB.\n  deviations:\n  - The same spectral method and assumptions as fig3-group-lfb-decrease-hfb-increase. Reading (b)\n    uses the electrodes good in every file of the subject (assumed, see fig6b-best-models-sensorimotor).\n- claim: discussion-day-changes-small\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:discussion-day-changes-small\n  notes: The largest deviation of a day mean from the subject's mean is 1.48 dB (S06 HFB), and every\n    subject and band is at most 2.2 dB; the largest range of day means is 2.04 dB (S06 LFB). Without\n    baseline subtraction the precentral band power is 12.2 to 36.5 dB in microvolts squared (the\n    files' stored unit), inside 9 to 55 dB; in volts squared it would be -108 to -84 dB.\n  deviations:\n  - The same spectral method and assumptions as fig3-group-lfb-decrease-hfb-increase.\n- claim: fig6b-best-models-sensorimotor\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig6b-best-models-sensorimotor\n  notes: 14 LFB and 14 HFB models have withheld R2 above 0.05, of 976 per band. Reading (a), all 14 LFB\n    and 13 of 14 HFB electrodes are in the five frontoparietal regions (the other in superior\n    temporal), and the median R2 of sensorimotor electrodes exceeds that of temporal ones (LFB -0.0102\n    against -0.0158, HFB -0.0117 against -0.0154). Reading (b), the three regions with the highest\n    projected R2 are precentral, postcentral and middle frontal in both bands.\n  deviations:\n  - Assumed, as the good-electrode flags differ between a subject's files; the models use the\n    electrodes good in every file of the subject (976 electrodes), on the 7650 events of reading (b).\n    The paper reports 4.9 +- 4.9 surface electrodes removed per subject; the files mark 1 to 17 bad in\n    every file and 3 to 32 in at least one.\n  - Forward selection over single design columns starting from an adjusted R2 of 0, on all of the\n    subject's events, as the code does (_forward_selected_new); 200 day-balanced splits with 10% test\n    events (Methods). The splits use the seed of this claim, and the other Figure 6 claims use the same\n    fits.\n  - The seed check refits the full-model R2 of the models with R2 above 0.03 under the four other\n    seeds (12 to 14 models per band pass 0.05); Delta R2, coefficients and retention were not refit\n    under them, for time.\n  - The code's fits at bad electrodes were not run as a variant.\n- claim: fig6-r2-at-most-025\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig6-r2-at-most-025\n  measured: 0.1773\n  notes: The largest split-averaged withheld R2 is 0.1773 (S07, HFB), at most 0.275. It is 0.1837 with\n    the code's 80/20 splits and 0.1578 with band medians, and 0.165 to 0.184 under the four other\n    seeds. No Huber fit failed to converge.\n  deviations:\n  - As for fig6b-best-models-sensorimotor.\n- claim: fig6c-angle-and-day-most-informative\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig6c-angle-and-day-most-informative\n  notes: Over the 14 LFB models with R2 above 0.05, recording day (median Delta R2 0.0383) and reach\n    angle (0.0325) rank first and second; the eight other features have medians of 0. In HFB the same\n    two lead (0.0603 and 0.0232). The code's Delta R2 (80/20, test events shuffled) and the code's\n    selection by LFB R2 give the same two in both bands (with selection by LFB R2 the HFB order is\n    angle, then day).\n  deviations:\n  - As for fig6b-best-models-sensorimotor. The code's Delta R2 variant is run with the code's 80/20\n    splits, combining two of the criterion's variants.\n- claim: extfig6-2-angle-most-retained\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:extfig6-2-angle-most-retained\n  notes: Reach angle has the highest retention probability in precentral, postcentral and inferior\n    parietal regions for both bands (0.517 averaged over these). The order of the next four does not\n    hold under either reading; over the three sensorimotor regions it is speech ratio (0.360),\n    duration (0.359), magnitude (0.359) and onset speed (0.348), and over all eight regions speech\n    ratio, magnitude, bimanual class and onset speed.\n  deviations:\n  - As for fig6b-best-models-sensorimotor. Forward selection runs once per model on all events (the\n    code runs it in every split on all events, which gives the same selection each time).\n- claim: fig6d-upward-reaches-enhance-pattern\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig6d-upward-reaches-enhance-pattern\n  notes: Over models with R2 above 0.05, the median reach angle coefficient is -0.702 for LFB (13 of 14\n    negative) and +0.536 for HFB (13 of 14 positive). With the code's selection by LFB R2 the HFB median\n    is +0.237. Positive angles are upward because the stored image-coordinate angle is negated before\n    folding, as the code does; the convention was checked against the pose.\n  deviations:\n  - As for fig6b-best-models-sensorimotor.\n- claim: fig6d-angle-and-day-largest-coefficients\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_peterson_2021.ipynb\n  output: claim:fig6d-angle-and-day-largest-coefficients\n  notes: Under both readings, recording day (SD of its one-hot coefficients) and reach angle have the\n    two largest magnitudes in both bands; LFB 0.976 and 0.702, HFB 0.709 and 0.536 (the next is\n    magnitude, 0.281). With the code's selection by LFB R2 the same two lead (HFB 0.241 and 0.237).\n  deviations:\n  - As for fig6b-best-models-sensorimotor.\nfindings:\n- kind: selection_undocumented\n  about: data\n  severity: major\n  statement: The files hold 8088 movement events, 211 to 996 per subject (median 770.5), where the\n    paper analysed 151 to 947 per subject (median 640). Nothing in the files marks the events the\n    paper used or the false positives it removed, so the paper's event set cannot be rebuilt;\n    dropping the events without usable ECoG still leaves 210 to 976 per subject (median 691).\n- kind: data_missing\n  severity: minor\n  statement: The ECoG of three files ends hours before the day ends while the pose and the events go\n    on to 24 h; sub-01 day 7 (15.5 h), sub-04 day 3 (15.7 h) and sub-06 day 3 (15.9 h). 237 events\n    (132, 22 and 83) have no neural data.\n- kind: metadata_insufficient\n  severity: minor\n  statement: The ECoG holds stretches of NaN samples, which the files do not describe; 125 events\n    have NaN samples within 5 s of onset (47 of them in sub-10).\n- kind: metadata_error\n  severity: minor\n  statement: The bimanual overlap is described as a fraction of the contralateral movement duration,\n    but 1661 of 8088 values are above 1 (up to 3.83); the values are consistent with seconds.\n- kind: metadata_error\n  severity: minor\n  statement: The pose series are labelled in meters, but the values are pixels; the reach magnitudes\n    computed from the pose equal the stored pixel magnitudes (median ratio 1.007).\n- kind: metadata_insufficient\n  severity: minor\n  statement: The reach angle has no stated convention. It is the angle in image coordinates (y\n    downward), -180 to 180 degrees, matching the pose to a median of 1.6 degrees, so upward reaches\n    are negative. The paper's code negates and folds it.\n- kind: metadata_insufficient\n  severity: minor\n  statement: The `good` flags of the electrodes differ between the files of a subject (bad in at least\n    one file 3 to 32 per subject, bad in every file 1 to 17), and nothing says how they were set or\n    which applies to the subject's analyses. The paper reports 4.9 +- 4.9 surface electrodes removed\n    per subject.\n- kind: metadata_insufficient\n  severity: minor\n  statement: The electrodes table carries low_freq_R2 and high_freq_R2 columns with no description of\n    the model or data they come from.\n- kind: identifier_missing\n  severity: minor\n  statement: 24 electrodes have no position (NaN x, y, z), the 16 depth electrodes of sub-03 and 8 of\n    sub-12; the paper's projection matrices give them no row.\n- kind: metadata_error\n  severity: minor\n  statement: One event of sub-08 day 4 is at 40.3 s in ReachEvents and at 86440.3 s in the reaches\n    table; the other 8087 agree to 1 ms.\n- kind: other\n  about: data\n  severity: minor\n  statement: Electrode groups described as depth electrodes are in 7 subjects (sub-01, 02, 03, 09, 10,\n    11 and 12), where the paper reports depth electrodes in 5.\n- kind: other\n  about: data\n  severity: minor\n  statement: The coarse behavioural labels (epochs) are empty at 4767 of the 8088 event times, and 17\n    events fall in epochs labelled sleep or blocklist, which the Methods say were excluded.\n- kind: other\n  about: data\n  severity: none\n  statement: Checks that passed. The subjects and days are the paper's; the paper's projection\n    matrices match the electrodes of all 12 subjects; ECoG is at 500 Hz in microvolts and pose at 30 Hz.\n    Band power at the event onsets differs from that at pseudo-onsets 3 s earlier in the same segments\n    in 11 of 12 subjects for LFB and 9 of 12 for HFB, consistent with ECoG and events sharing a clock;\n    for sub-09 neither band differs, so the alignment could not be established there.\n- kind: methods_unavailable\n  statement: Question for the authors. The Methods drop segments with power below 0 dB or with\n    115-125 Hz power more than 3 SD above all segments, but do not say how power is pooled over\n    electrodes and frequencies, or whether the SD is per subject. This attempt assumed the Welch power\n    of the 10 s segment averaged over good electrodes, 1-200 Hz for the 0 dB test and 115-125 Hz for\n    the 3 SD test per subject; it drops 76 events. Please confirm or correct.\n- kind: methods_unavailable\n  statement: Question for the authors. The Results say low-frequency decreases are more spatially\n    widespread than high-frequency increases (Figure 3) without a measure. Counting regions with any\n    significant bin gives a tie (7 against 7), and counting significant bins per frequency bin favours\n    the low frequencies (34.2 against 23.9). Which measure was meant?\n- kind: methods_unavailable\n  statement: Question for the authors. The dataset's good-electrode flags differ between a subject's\n    days. Were bad electrodes removed per day or per subject, and did the regression use the\n    electrodes good on every day? This attempt projected each event with its own day's flags and fit\n    the regression at electrodes good on every day.\n"
}
```

```
File created successfully at: attempts/peterson-2021-02.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/peterson-2021-02.yaml",
 "old_string": "only the events that have ECoG without missing samples, 211 to 986, median 700.5. The fewest\n    events are outside 151 +- 15.1 in every reading, and the median is outside 640 +- 64 in all but\n    none. The dataset has no false-positive flag, so reading (b) cannot drop those events.",
 "new_string": "only the events that have ECoG without missing samples, 211 to 986, median 700.5. Under reading\n    (b) the median and the largest count are within tolerance, but in every reading the fewest events\n    (210 or 211, in S09) are outside 151 +- 15.1. The dataset has no false-positive flag, so reading\n    (b) cannot drop those events."
}
```

```
The file attempts/peterson-2021-02.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -n "dev\b\|9-55\|fewest" /dev/null; timeout 600 python tools/entry.py check entries/peterson-2021 2>&1 | tail -15; date -u
```

```
0 error(s)
Wed Nov 25 07:38:01 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import yaml
d=yaml.safe_load(open('attempts/peterson-2021-02.yaml'))
def walk(x,p=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,p+'/'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,p+f'[{i}]')
    elif isinstance(x,str) and (': ' in x or '—' in x or 'rather' in x): print(p, x[:100])
walk(d)
print(len(d['outcomes']), len(d['findings']))
EOF
grep -c "—\|rather" entries/peterson-2021/README.md entries/peterson-2021/ajile.py; python3 -c "
import json;nb=json.load(open('entries/peterson-2021/reproduce_peterson_2021.ipynb'))
s=''.join(''.join(c['source']) for c in nb['cells']); print(s.count('—'), s.count('rather'), sum(1 for c in nb['cells'] if c.get('outputs')))"
```

```
25 16
entries/peterson-2021/README.md:0
entries/peterson-2021/ajile.py:0
0 0 0
```

**Agent calls Bash**

```bash
timeout 600 python tools/entry.py handover entries/peterson-2021 2>&1 | tail -10; ls executed/peterson-2021/handover/; date -u
```

```
wrote executed/peterson-2021/handover
ajile.py
peterson-2021.yaml
reproduce_peterson_2021.ipynb
Wed Nov 25 07:38:26 UTC 2026
```

**Agent**

The attempt is complete: the entry ran from a clean environment, its checks pass, and the handover package for the verifier is built. I did not verify my own work. I did not come across any earlier attempt on this paper. Besides the paper, the claims file and the dataset, I read only the paper's own code on GitHub (commit 04c6faf) and the Figshare projection matrices it names.

## 1. Outcomes (DANDI:000055, version 0.261123.1703)

| Claim | Outcome |
|---|---|
| subject-days | reproduced |
| roi-projection-link | reproduced |
| cohort | partially reproduced (7 subjects have depth electrodes, the paper says 5) |
| fig2-event-counts | not reproduced (fewest events per subject is 210, against 151 ± 15.1) |
| fig2-features-differ-across-subjects | reproduced |
| fig2-reach-shape | partially reproduced (no angle density peaks within 15° of ±90) |
| fig2-bimanual-skew | reproduced |
| extfig2-1c-contralateral-larger | reproduced |
| extfig2-2-feature-correlations | partially reproduced (5 of 6) |
| fig2-days-and-waking | partially reproduced (S04's busiest day holds 40% of its events) |
| fig3-group-lfb-decrease-hfb-increase | reproduced, assumed |
| fig3-sensorimotor-largest | reproduced, assumed |
| fig3-lfb-more-widespread | blocked, methods_underspecified (the two readings disagree: 7 vs 7 regions, 34.2 vs 23.9 bins) |
| fig4-precentral-subject-variability | partially reproduced, assumed (3 of 4 parts; S09 shows no high-frequency increase) |
| fig5-band-power-differs-across-subjects | reproduced, assumed |
| table1-subject-band-power-ci | partially reproduced, assumed (21 of 24 values inside the intervals) |
| fig5-recording-day-effects | partially reproduced, assumed (20 of 24 agree) |
| extfig5-1-baseline-reduces-day-variability | reproduced, assumed |
| discussion-day-changes-small | reproduced, assumed |
| fig6b, fig6-r2 (largest R² 0.177), fig6c, fig6d-upward, fig6d-largest | reproduced, assumed |
| extfig6-2-angle-most-retained | partially reproduced, assumed (the order of the next four features differs) |

## 2. Dataset, assumptions, questions

**What the dataset holds:**
- The subjects and days match Table 2 exactly.
- The Figshare projection matrices match the electrodes of all 12 subjects. This uses the code's row rule; the first row of each file is the region density.
- The ECoG of three files ends hours before the day ends (sub-01 day 7, sub-04 day 3, sub-06 day 3), so 237 events have no neural data. Another 125 events fall on NaN samples.
- There are 8088 events, more than the paper analysed, and nothing marks the paper's subset (rated major).
- Undocumented conventions:
  - the reach angle is in image coordinates (y downward);
  - the bimanual overlap is in seconds although it is described as a fraction;
  - the pose is labelled meters but holds pixels;
  - the good-electrode flags differ between a subject's days;
  - 24 electrodes have no position;
  - the R² columns in the electrodes table have no description.
- One event in sub-08 day 4 has timestamps a day apart in two tables.
- The clock is consistent with the events in 11 of 12 subjects. It could not be established for sub-09.

**Assumptions** (recorded as `assumed: true` on the outcomes):
- how the segment rejection pools power over electrodes and frequencies;
- each event is projected to regions with its own day's good-electrode flags;
- the regression and electrode-level analyses use electrodes that are good on every day.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings): the pooling in the segment rejection, the measure behind "widespread", and whether bad electrodes were removed per day or per subject.

**Questions to a reader:** none.

## 3. Protocol points

1. The roi-projection-link criterion says "drop all-zero rows", but the code also drops the first non-zero row. I used the code's rule and recorded it as a deviation.
2. The protocol asks for notebooks under about 10 minutes. This one cannot be, because the data are about 150 GB of ECoG chunks. It runs in 37 minutes and I recorded that.
3. Running every random step under five seeds is too costly for 3904 Huber models. Under the four extra seeds I refit only the full-model R² of the top models; Delta R², coefficients and retention were not refit. This is recorded as a deviation.
4. For the clock check with an event table on continuous recordings, the protocol's guidance did not fit directly. I contrasted band power at true onsets with pseudo-onsets 3 s earlier in the same segments.
5. The cohort claim has no rule for a partial result. I used `partially_reproduced` because one count differs.
6. It is unclear when a small event-set choice counts as "resting on an assumption". I marked every spectral and regression outcome `assumed: true`.

## 4. Runtime and failures

- The run took about 2 h 33 min (05:06 to 07:39 UTC).
- Notebook: 36.6 min. The ECoG streaming took 8 min, the regression 23 min and the seed refits 3.5 min. Peak memory was 1.8 GB per worker.
- Nothing failed in the final run.

During development I fixed these:
- h5py's remote chunk lookups took about 0.1 s each, so I read the chunk index from the file directly and fetch byte ranges in parallel;
- NaN samples in the ECoG were at first not caught by the segment rejection;
- I had accidentally deleted part of the helper module in an earlier edit and restored it.

Files are in `entries/peterson-2021`:
- reproduce_peterson_2021.ipynb
- ajile.py
- entry.yaml
- README.md

The record is `attempts/peterson-2021-02.yaml`.

## End of run

106 turns, 147 minutes, $10.27 at API prices, result: success.
