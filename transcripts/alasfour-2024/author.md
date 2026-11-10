# alasfour-2024 · author · run 42750463933

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls
```

```
<persisted-output>
Output too large (38.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/f47e9e54-6b4a-4d7e-b3ca-9b3076caa694/tool-results/b1howooux.txt

Preview (first 2KB):
Tue Nov 10 03:43:33 UTC 2026
# Protocol for an attempt

Version: `pilot-14`. Record this version in the attempt's provenance.

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/f47e9e54-6b4a-4d7e-b3ca-9b3076caa694/tool-results/b1howooux.txt"
}
```

```
1	Tue Nov 10 03:43:33 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-14`. Record this version in the attempt's provenance.
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
[... 663 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/alasfour-2024.yaml; ls paper; cat papers/datasets/alasfour-2024.yaml
```

```
<persisted-output>
Output too large (42.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/f47e9e54-6b4a-4d7e-b3ca-9b3076caa694/tool-results/bn6qhrbke.txt

Preview (first 2KB):
# Claims for Alasfour & Gilja (2024), Front. Hum. Neurosci. 18:1388267, "Consistent
# spectro-spatial features of human ECoG successfully decode naturalistic behavioral states",
# on dandiset 000055 (AJILE12).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
#
# Text read. The version of record from PubMed Central (PMC11169785), in
# paper/10.3389-fnhum.2024.1388267.txt: abstract, Introduction, Methods, Results, figure legends
# (Figures 1 to 7), Table 1, Discussion and Data availability statement. The paper has no
# supplement (PMC lists none, and the text cites none). No PDF was supplied, so the figures
# could not be read; every claim rests on the text and the legends. Values shown only in the
# figures (per-feature accuracies, confidence intervals, the finite chance level, the
# per-participant matrices and curves) are not known here.
#
# Code read. None. The paper links no analysis code and names no software or toolbox.
#
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/f47e9e54-6b4a-4d7e-b3ca-9b3076caa694/tool-results/bn6qhrbke.txt"
}
```

```
1	# Claims for Alasfour & Gilja (2024), Front. Hum. Neurosci. 18:1388267, "Consistent
2	# spectro-spatial features of human ECoG successfully decode naturalistic behavioral states",
3	# on dandiset 000055 (AJILE12).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5	# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
6	#
7	# Text read. The version of record from PubMed Central (PMC11169785), in
8	# paper/10.3389-fnhum.2024.1388267.txt: abstract, Introduction, Methods, Results, figure legends
9	# (Figures 1 to 7), Table 1, Discussion and Data availability statement. The paper has no
10	# supplement (PMC lists none, and the text cites none). No PDF was supplied, so the figures
11	# could not be read; every claim rests on the text and the legends. Values shown only in the
12	# figures (per-feature accuracies, confidence intervals, the finite chance level, the
13	# per-participant matrices and curves) are not known here.
14	#
15	# Code read. None. The paper links no analysis code and names no software or toolbox.
16	#
17	# Data the paper used. Five of the twelve AJILE12 participants (Peterson et al., 2022), 2 male
18	# and 3 female, numbered 1, 2, 4, 5 and 8 in Table 1, chosen as those with at least 1 h of the
19	# behaviours of interest, in epilepsy monitoring with ECoG placed for clinical needs.
20	# Post-surgical days 3 to 7 only. ECoG at 1 kHz, preprocessed as in AJILE12 (median removed,
[... 652 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/10.3389-fnhum.2024.1388267.txt | head -c 60000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; python3 -c "
t=open('10.3389-fnhum.2024.1388267.txt').read()
i=t.find('Data preprocessing'); j=t.find('Discussion', i+20000)
print(len(t), i, j)
print(t[i-200:i+16000])
"
```

```
60627 11519 33699
Watching TV.” The following steps demonstrate that we can find spectro-spatial features that are discriminative between the two behavioral states and are consistent across participants. 2 Methods 2.1 Data preprocessing Neurophysiological recordings were obtained from the publicly available AJILE12 dataset ( Peterson et al., 2022 ). Five participants (2 males, 3 females) with electrocorticography (ECoG) electrodes planted on the cortical surface based on clinical needs were used in this study. We selected only participants with at least 1 h of recorded neural activity of the behaviors of interest to obtain adequate samples when training and testing our classification models. Of the 12 participants in the dataset, only 5 satisfied this criterion. Recordings lasted for an average of four days across participants and only post-surgical days 3–7 were included. The video was recorded synchronously with neural activity. The ECoG activity was recorded at a sampling rate of 1 kHz, and the video was recorded at 30 fps. The video for each participant was split into 2-min blocks, and each block was manually annotated using a coarse behavioral label. The active behavioral labels included talking, watching TV, and using a computer or phone, whereas the inactive behavioral labels included sleeping and awake rest. For most analyses in this study, we used two active labels: talking and watching TV. Naturally, when constrained to a hospital bed, the subjects’ natural tendency is to mostly engage in these two behaviors. These two labels, therefore, have a sufficient number of samples, and the analysis of the spatial-spectral features that separate them becomes tractable. Information regarding the five participants, including the number of electrodes used and the amount of data, is summarized in Table 1 . Figure 1 shows the locations of the ECoG electrodes on the cortical surfaces of the five participants used in this study. More information regarding subjects not use
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('paper/10.3389-fnhum.2024.1388267.txt').read()
i=t.find('We observe that participant specific d')
print(t[i:i+9000])
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/## DANDI/,/^## [^D]/p' docs/archives.md | head -120; ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in
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
README.md
entry.yaml
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/fouke-2025-01.yaml | head -150; cat entries/fouke-2025/README.md
```

```
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
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-5
  runner:
[... 164 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^[a-z_]*:" attempts/fouke-2025-01.yaml; sed -n '/^findings:/,/^verifications:/p' attempts/fouke-2025-01.yaml | head -40; grep -n "blocked_by\|assumed\|measured" attempts/fouke-2025-01.yaml | head; ls schemas
```

```
1:schema_version: 3
2:id: fouke-2025-01
3:datasets:
9:paper: doi:10.1016/j.cub.2025.04.027
10:date: 2026-10-14
11:entry: fouke-2025
12:provenance:
23:inputs:
35:outcomes:
244:findings:
310:verifications:
findings:
- kind: data_missing
  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
    the GitLab repository the paper names for all behavioural and imaging data holds analysis
    notebooks only. Nine of the paper's main findings cannot be tested.
- kind: metadata_insufficient
  statement: The stimulus codes 0 to 20 have no names or description in the files or the
    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
[... 45 more lines not kept]
```

**Agent**

Now the dataset. Let me survey DANDI:000055.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000055/ | python3 -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000055/versions/" | python3 -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000055/versions/0.220127.0436/assets/?page_size=100" | python3 -c "
import json,sys
d=json.load(sys.stdin)
for a in d['results']: print(a['path'], round(a['size']/1e9,2), a['asset_id'])
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q env && . env/bin/activate && uv pip install -q h5py remfile pynwb numpy scipy pandas scikit-learn statsmodels 2>&1 | tail -2; python -c "import pynwb,remfile;print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cat > $TMPDIR/probe.py <<'EOF'
import h5py, remfile, time, json, urllib.request
aid='7de9b149-2994-455e-a8c6-5e5893245baf'  # sub-08 ses-3
url=f'https://api.dandiarchive.org/api/assets/{aid}/download/'
import requests
s3=requests.head(url,allow_redirects=True).url
print(s3)
t=time.time()
f=h5py.File(remfile.File(s3),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name, obj.shape, obj.dtype, obj.chunks, obj.compression)
    else:
        a=dict(obj.attrs)
        print(name+'/', {k:(str(v)[:80]) for k,v in a.items() if k in('neurodata_type','description','unit','rate','starting_time','conversion')})
f.visititems(show)
print(time.time()-t)
EOF
python $TMPDIR/probe.py 2>&1 | head -150
```

```
https://dandiarchive.s3.amazonaws.com/blobs/f30/ba3/f30ba333-ef76-4a3d-a185-c8d934e5f52e?response-content-disposition=attachment%3B%20filename%3D%22sub-08_ses-3_behavior%2Becephys.nwb%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=[removed: an AWS key]%2F20261110%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20261110T034435Z&X-Amz-Expires=21600&X-Amz-SignedHeaders=host&X-Amz-Signature=b63df9103442af5547ec1dbf16812eef40bc5c668e8e3f49e42d41d736659c6a
acquisition/ {}
acquisition/ElectricalSeries/ {'description': 'no description', 'neurodata_type': 'ElectricalSeries'}
acquisition/ElectricalSeries/data (43200000, 92) float32 (84375, 1) gzip
acquisition/ElectricalSeries/electrodes (92,) int64 None None
acquisition/ElectricalSeries/starting_time () float64 None None
analysis/ {}
file_create_date (1,) object None None
general/ {}
general/devices/ {}
general/devices/GRID/ {'neurodata_type': 'Device'}
general/devices/RAT/ {'neurodata_type': 'Device'}
general/devices/RMT/ {'neurodata_type': 'Device'}
general/devices/ROF/ {'neurodata_type': 'Device'}
general/devices/RPT/ {'neurodata_type': 'Device'}
general/extracellular_ephys/ {}
general/extracellular_ephys/GRID/ {'description': 'ECoG grid', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/RAT/ {'description': 'right anterior temporal', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/RMT/ {'description': 'right medial temporal', 'neurodata_type': 'ElectrodeGroup'}
general/extracellular_ephys/ROF/ {'description': 'right orbitofrontal', 'neurodata_type': 'ElectrodeGroup'}
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cat > $TMPDIR/probe2.py <<'EOF'
import h5py, remfile, time, requests, numpy as np, collections
aid='7de9b149-2994-455e-a8c6-5e5893245baf'
s3=requests.head(f'https://api.dandiarchive.org/api/assets/{aid}/download/',allow_redirects=True).url
t=time.time()
f=h5py.File(remfile.File(s3),'r')
e=f['general/extracellular_ephys/electrodes']
print('open',time.time()-t)
for k in e.keys():
    v=e[k][:]
    print(k, v[:6])
print('good', e['good'][:].sum())
ep=f['intervals/epochs']
lab=ep['labels'][:].astype(str); st=ep['start_time'][:]; sp=ep['stop_time'][:]
print(collections.Counter(lab).most_common(40))
print(st[:5], sp[:5], (sp-st)[:10])
es=f['acquisition/ElectricalSeries']
print(dict(es.attrs).keys(), {k:es[k].attrs.get('rate') for k in es}, es['starting_time'][()], dict(es['starting_time'].attrs), dict(es['data'].attrs))
print(f['session_start_time'][()], f['general/subject/subject_id'][()], f['session_description'][()], f['timestamps_reference_time'][()])
t=time.time()
x=es['data'][0:84375*4,:]
print('read 4 chunks x 92ch',time.time()-t, x.nbytes/1e6, np.isnan(x).mean(), x[:3,:5])
EOF
python $TMPDIR/probe2.py 2>&1
```

```
open 1.146406650543213
filtering [b'250 Hz lowpass' b'250 Hz lowpass' b'250 Hz lowpass' b'250 Hz lowpass'
 b'250 Hz lowpass' b'250 Hz lowpass']
good [False  True False  True  True False]
group [<HDF5 object reference> <HDF5 object reference> <HDF5 object reference>
 <HDF5 object reference> <HDF5 object reference> <HDF5 object reference>]
group_name [b'GRID' b'GRID' b'GRID' b'GRID' b'GRID' b'GRID']
high_freq_R2 [-0.00557543 -0.00236102  0.00155655 -0.00562477 -0.00397774 -0.00448955]
id [0 1 2 3 4 5]
imp [nan nan nan nan nan nan]
kurtosis [2.37583374e+03 1.95757358e+01 1.06647808e+04 6.02403450e+00
 6.75735474e+00 7.82557775e+03]
location [b'unknown' b'unknown' b'unknown' b'unknown' b'unknown' b'unknown']
low_freq_R2 [-0.00592764 -0.00325312  0.00287166 -0.00313005 -0.00502746 -0.00383126]
median_deviation [15.3319308  39.15281326 32.82362913 22.67336678 42.43319245 12.3058461 ]
standard_deviation [288.28932722  52.51216865  56.93539802  27.25805799  51.83329851
 163.26515396]
x [41.1347377  50.17415795 59.03113179 62.80054993 65.65865799 69.98993154]
y [ 26.05091321  18.29616229   6.54567415  -5.66545414 -14.58431485
 -27.39843689]
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s -m 30 "https://api.figshare.com/v2/projects/78666/articles" | head -c 3000; echo; curl -s -m 20 -o /dev/null -w "%{http_code}\n" https://api.github.com/repos/BruntonUWBio/naturalistic_arm_movements_ecog
```

Result: the fetched text is not kept.

**Agent**

Figshare is reachable and holds a pinned "ROI projection matrices and labels" item (DOI 10.6084/m9.figshare.12114408.v1). Checking its files.

**Agent calls Bash**

```bash
curl -s -m 30 "https://api.figshare.com/v2/articles/12114408" | python3 -c "
import json,sys; d=json.load(sys.stdin)
print(d['description'][:1500]); 
for f in d['files']: print(f['name'], f['size'], f['download_url'], f.get('computed_md5'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL -m 30 https://ndownloader.figshare.com/files/22276665 -o c.csv; curl -sL -m 30 https://ndownloader.figshare.com/files/22276704 -o e8.csv; cat c.csv | head -c 1500; echo; head -c 800 e8.csv; echo; python3 -c "
import pandas as pd; d=pd.read_csv('e8.csv',header=None); print(d.shape); print(d.iloc[:3,:8])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; . env/bin/activate; python -c "
import pandas as pd, numpy as np; d=pd.read_csv('e8.csv'); print(d.shape)
cols=['Precentral','Frontal_Mid','Postcentral','Parietal_Inf','SupraMarginal','Temporal_Sup','Temporal_Mid','Temporal_Inf']
print([c for c in d.columns if any(c.startswith(x+'_') for x in cols)])
sub=d[[c for c in d.columns if any(c.startswith(x+'_') for x in cols)]]
print(sub.iloc[:4]); print((sub.iloc[1:]>0).sum()); print(sub.iloc[1:].max())
"
```

```
(93, 116)
['Precentral_L', 'Precentral_R', 'Frontal_Mid_L', 'Frontal_Mid_R', 'Frontal_Mid_Orb_L', 'Frontal_Mid_Orb_R', 'Postcentral_L', 'Postcentral_R', 'Parietal_Inf_L', 'Parietal_Inf_R', 'SupraMarginal_L', 'SupraMarginal_R', 'Temporal_Sup_L', 'Temporal_Sup_R', 'Temporal_Mid_L', 'Temporal_Mid_R', 'Temporal_Inf_L', 'Temporal_Inf_R']
   Precentral_L  Precentral_R  ...  Temporal_Inf_L  Temporal_Inf_R
0  4.249200e+00  3.521100e-15  ...        6.449700    8.633700e-09
1  7.320200e-13  3.102600e-23  ...        0.002804    3.817800e-11
2  6.418700e-12  3.487600e-27  ...        0.013876    1.177800e-14
3  4.813800e-11  6.196400e-31  ...        0.035650    6.227600e-19

[4 rows x 18 columns]
Precentral_L         92
Precentral_R         92
Frontal_Mid_L        92
Frontal_Mid_R        92
Frontal_Mid_Orb_L    92
Frontal_Mid_Orb_R    92
Postcentral_L        92
Postcentral_R        92
Parietal_Inf_L       92
Parietal_Inf_R       92
SupraMarginal_L      92
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; . env/bin/activate; for p in 01 02 04 05; do id=$(python3 -c "print({'01':22276662,'02':22276671,'04':22276680,'05':22276686}['$p'])"); curl -sL -m 30 https://ndownloader.figshare.com/files/$id -o e$p.csv; done; mv e8.csv e08.csv; python -c "
import pandas as pd, numpy as np
R=['Precentral','Frontal_Mid','Postcentral','Parietal_Inf','SupraMarginal','Temporal_Sup','Temporal_Mid','Temporal_Inf']
for p in ['01','02','04','05','08']:
    d=pd.read_csv(f'e{p}.csv'); print(p, d.shape)
    for r in R:
        L=d[r+'_L'].values; Rr=d[r+'_R'].values
        print('  %-14s densL %.2f densR %.2g sumL %.2f sumR %.2f maxL %.2f maxR %.2f'%(r,L[0],Rr[0],L[1:].sum(),Rr[1:].sum(),L[1:].max(),Rr[1:].max()))
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
date -u; . $TMPDIR/env/bin/activate; cat > $TMPDIR/probe3.py <<'EOF'
import h5py, remfile, time, requests, numpy as np, zlib
from concurrent.futures import ThreadPoolExecutor
aid='7de9b149-2994-455e-a8c6-5e5893245baf'
s3=requests.head(f'https://api.dandiarchive.org/api/assets/{aid}/download/',allow_redirects=True).url
f=h5py.File(remfile.File(s3),'r')
d=f['acquisition/ElectricalSeries/data']
print(d.id.get_create_plist().get_nfilters(), [d.id.get_create_plist().get_filter(i)[0] for i in range(d.id.get_create_plist().get_nfilters())])
t=time.time()
n=d.id.get_num_chunks(); print('nchunks',n, time.time()-t)
t=time.time()
info={}
for i in range(n):
    c=d.id.get_chunk_info(i); info[c.chunk_offset]=(c.byte_offset,c.size)
print('chunk index',time.time()-t, len(info))
sess=requests.Session()
from requests.adapters import HTTPAdapter
sess.mount('https://',HTTPAdapter(pool_maxsize=32))
def get(key):
    off,sz=info[key]
    r=sess.get(s3,headers={'Range':f'bytes={off}-{off+sz-1}'})
    return np.frombuffer(zlib.decompress(r.content),dtype='<f4')
rows=list(range(100,120))
keys=[(r*84375,c) for r in rows for c in range(92)]
t=time.time()
with ThreadPoolExecutor(32) as ex: out=list(ex.map(get,keys))
dt=time.time()-t
tot=sum(info[k][1] for k in keys)
print('parallel', dt, tot/1e6, 'MB compressed', tot/1e6/dt,'MB/s', len(out)*84375*4/1e6/dt,'MB/s raw')
x=d[100*84375:100*84375+10, :3]; print(x, out[0][:3], out[1][:3])
EOF
python $TMPDIR/probe3.py 2>&1
```

```
Tue Nov 10 03:49:17 UTC 2026
1 [1]
nchunks 47104 142.37779116630554
chunk index 55.688326358795166 47104
parallel 7.84205961227417 575.674499 MB compressed 73.40858492059542 MB/s 79.18838043873428 MB/s raw
[[ 5.0572789e-01  2.1329920e+01  2.6842552e+01]
 [ 1.5407734e+00  8.7058315e+00  1.9020176e+01]
 [-5.2035570e-02  6.3960190e+00  2.3461514e+01]
 [ 4.1101766e+00  1.4761412e+01  3.0870178e+01]
 [ 8.3601723e+00  1.8800220e+01  3.7963173e+01]
 [ 6.9225459e+00  1.5677408e+01  3.9311188e+01]
 [ 1.1140753e+01  1.2607562e+01  3.9066681e+01]
 [ 1.1643878e+01  1.4740216e+01  4.6592751e+01]
 [ 1.1299492e+01  1.9594193e+01  5.4402031e+01]
 [ 1.2280397e+01  1.1978214e+01  6.0745216e+01]] [ 0.5057279   1.5407734  -0.05203557] [21.32992   8.705832  6.396019]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; uv pip install -q fsspec aiohttp 2>&1|tail -1; python -c "import remfile,inspect; print(inspect.signature(remfile.File.__init__)); import h5py; print(h5py.version.hdf5_version)"; cat > $TMPDIR/probe4.py <<'EOF'
import h5py, remfile, time, requests, fsspec
aid='7de9b149-2994-455e-a8c6-5e5893245baf'
s3=requests.head(f'https://api.dandiarchive.org/api/assets/{aid}/download/',allow_redirects=True).url
t=time.time()
fs=fsspec.filesystem('http')
fo=fs.open(s3,'rb',block_size=8*2**20,cache_type='blockcache')
f=h5py.File(fo,'r')
d=f['acquisition/ElectricalSeries/data']
info={}
def cb(c): info[c.chunk_offset]=(c.byte_offset,c.size)
d.id.chunk_iter(cb)
print('chunk_iter fsspec 8MB', time.time()-t, len(info))
EOF
python $TMPDIR/probe4.py 2>&1 | tail -3
```

```
(self, url: Union[str, Any], *, verbose: bool = False, disk_cache: Optional[remfile.DiskCache.DiskCache] = None, _min_chunk_size: int = 102400, _max_cache_size: int = 1000000000.0, _chunk_increment_factor: int = 1.7, _bytes_per_thread: int = 4194304, _max_threads: int = 1, _max_chunk_size: int = 104857600, _impose_request_failures_for_testing: bool = False, _size: Optional[int] = None, _use_session: bool = True)
2.0.0
chunk_iter fsspec 8MB 264.7927815914154 47104
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cat > $TMPDIR/probe5.py <<'EOF'
import h5py, time, requests, numpy as np, struct
from concurrent.futures import ThreadPoolExecutor
aid='7de9b149-2994-455e-a8c6-5e5893245baf'
s3=requests.head(f'https://api.dandiarchive.org/api/assets/{aid}/download/',allow_redirects=True).url
sess=requests.Session()
from requests.adapters import HTTPAdapter
sess.mount('https://',HTTPAdapter(pool_maxsize=64))
def rng(off,n):
    return sess.get(s3,headers={'Range':f'bytes={off}-{off+n-1}'}).content
class Log:
    def __init__(s): s.pos=0; s.log=[]; s.size=int(requests.head(s3).headers['Content-Length'])
    def seek(s,o,wh=0):
        s.pos = o if wh==0 else (s.pos+o if wh==1 else s.size+o); return s.pos
    def tell(s): return s.pos
    def read(s,n=-1):
        if n<0: n=s.size-s.pos
        b=rng(s.pos,n); s.log.append((s.pos,b[:4])); s.pos+=len(b); return b
    def readinto(s,buf):
        b=s.read(len(buf)); buf[:len(b)]=b; return len(b)
    def readable(s): return True
    def seekable(s): return True
t=time.time()
fo=Log(); f=h5py.File(fo,'r'); d=f['acquisition/ElectricalSeries/data']
n0=len(fo.log)
d.id.get_chunk_info_by_coord((0,0))
trees=[o for o,b in fo.log[n0:] if b==b'TREE']
print('opened',time.time()-t, trees[:3])
root=trees[0]
rank=len(d.shape)
def node(addr):
    b=rng(addr,24)
    assert b[:4]==b'TREE', b[:4]
    typ,lvl,used=b[4],b[5],struct.unpack('<H',b[6:8])[0]
    ks=8+8*(rank+1)
    b=rng(addr+24, used*(ks+8)+ks)
    ents=[]
    for i in range(used):
        p=i*(ks+8)
        sz,mask=struct.unpack('<II',b[p:p+8]); offs=struct.unpack('<%dQ'%(rank+1),b[p+8:p+ks]); child=struct.unpack('<Q',b[p+ks:p+ks+8])[0]
        ents.append((lvl,sz,mask,offs[:rank],child))
    return ents
t=time.time()
level=[root]; info={}
with ThreadPoolExecutor(64) as ex:
    while level:
        res=list(ex.map(node,level)); nxt=[]
        for ents in res:
            for lvl,sz,mask,offs,child in ents:
                if lvl==0: info[offs]=(child,sz)
                else: nxt.append(child)
        level=nxt
print('btree',time.time()-t,len(info))
c=d.id.get_chunk_info_by_coord((84375*100,5)); print(c, info[(84375*100,5)])
EOF
python $TMPDIR/probe5.py 2>&1 | tail -5
```

```
~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/requests/structures.py", line 65, in __getitem__
    return self._store[key.lower()][1]
           ~~~~~~~~~~~^^^^^^^^^^^^^
KeyError: 'content-length'
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cd $TMPDIR; sed -i "s|s.size=int(requests.head(s3).headers\['Content-Length'\])|s.size=int(sess.get(s3,headers={'Range':'bytes=0-0'}).headers['Content-Range'].split('/')[1])|" probe5.py; python probe5.py 2>&1 | tail -5
```

```
opened 3.0887908935546875 [7832, 1145542608, 20371287]
btree 4.677999496459961 47104
StoreInfo(chunk_offset=(8437500, 5), filter_mask=0, byte_offset=2882690328, size=314093) (2882690328, 314093)
Shell cwd was reset to
```

**Agent**

Index time is now ~8 s per file. Next: survey labels and electrodes in all 55 files (metadata only).

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cat > $TMPDIR/survey.py <<'EOF'
import h5py, remfile, requests, numpy as np, collections, json, time
from multiprocessing import Pool
V='0.220127.0436'
assets=[]
url=f'https://api.dandiarchive.org/api/dandisets/000055/versions/{V}/assets/?page_size=100'
for a in requests.get(url).json()['results']: assets.append((a['path'],a['asset_id']))
def one(pa):
    path,aid=pa
    s3=requests.head(f'https://api.dandiarchive.org/api/assets/{aid}/download/',allow_redirects=True).url
    f=h5py.File(remfile.File(s3),'r')
    e=f['general/extracellular_ephys/electrodes']
    ep=f['intervals/epochs']
    lab=ep['labels'][:].astype(str); st=ep['start_time'][:]; sp=ep['stop_time'][:]
    c=collections.Counter(); dur=collections.Counter()
    for l,a,b in zip(lab,st,sp): c[l]+=1; dur[l]+=b-a
    d=f['acquisition/ElectricalSeries/data']
    return dict(path=path, n_el=int(len(e['id'])), good=int(e['good'][:].sum()), good_idx=np.where(e['good'][:])[0].tolist(), shape=d.shape,
                counts=dict(c), dur=dict(dur), start=f['session_start_time'][()].decode(), sd=e['standard_deviation'][:].tolist(),
                x=e['x'][:].tolist())
t=time.time()
with Pool(12) as p: res=p.map(one,assets)
json.dump(res,open('/tmp/claude-1001/survey.json','w'))
for r in sorted(res,key=lambda r:r['path']):
    c=r['counts']; print(r['path'][7:20], r['n_el'], r['good'], r['shape'][0]/500/3600, r['start'], {k:v for k,v in c.items() if 'Talk' in k or 'TV' in k or 'Computer' in k})
print(time.time()-t)
EOF
python $TMPDIR/survey.py 2>&1 | tail -60
```

```
sub-01_ses-3_ 94 85 24.0 2000-01-02T19:00:00-05:00 {np.str_('Talk'): 105, np.str_('Talk, TV'): 24, np.str_('Computer/phone'): 16, np.str_('TV'): 92, np.str_('Eat, Talk'): 11, np.str_('Eat, TV'): 12}
sub-01_ses-4_ 94 91 24.0 2000-01-03T19:00:00-05:00 {np.str_('Talk'): 121, np.str_('Eat, Talk'): 17, np.str_('TV'): 128, np.str_('Eat, TV'): 7, np.str_('Talk, TV'): 15, np.str_('Computer/phone'): 99, np.str_('Talk, Computer/phone'): 4, np.str_('Eat, Computer/phone'): 1}
sub-01_ses-5_ 94 91 24.0 2000-01-04T19:00:00-05:00 {np.str_('Talk'): 79, np.str_('Computer/phone'): 57, np.str_('Computer/phone, TV'): 1, np.str_('TV'): 137, np.str_('Talk, Computer/phone'): 3, np.str_('Eat, TV'): 9, np.str_('Talk, TV'): 1}
sub-01_ses-7_ 94 91 15.477107222222223 2000-01-07T03:31:22.414000-05:00 {np.str_('Eat, Talk'): 7, np.str_('Talk'): 73, np.str_('Computer/phone'): 48, np.str_('TV'): 225, np.str_('Eat, Computer/phone'): 1, np.str_('Talk, Computer/phone'): 1, np.str_('Eat, TV'): 8, np.str_('Talk, TV'): 1}
sub-02_ses-3_ 86 85 24.0 2000-01-02T19:00:00-05:00 {np.str_('Talk'): 32, np.str_('Eat, TV'): 3, np.str_('TV'): 29}
sub-02_ses-4_ 86 85 24.0 2000-01-03T19:00:00-05:00 {np.str_('Talk'): 62, np.str_('TV'): 18, np.str_('Eat, TV'): 2, np.str_('Eat, Talk'): 2}
sub-02_ses-5_ 86 81 24.0 2000-01-04T19:00:00-05:00 {np.str_('Talk'): 74, np.str_('TV'): 33}
sub-02_ses-6_ 86 80 24.0 2000-01-05T19:00:00-05:00 {np.str_('TV'): 140, np.str_('Talk'): 56, np.str_('Eat, TV'): 8, np.str_('Eat, Talk'): 5, np.str_('Talk, Computer/phone'): 46, np.str_('Computer/phone'): 39, np.str_('Eat, Computer/phone'): 3}
sub-03_ses-3_ 96 79 24.0 2000-01-02T19:00:00-05:00 {np.str_('Computer/phone'): 136, np.str_('Talk'): 203, np.str_('Eat, Talk'): 14, np.str_('Talk, Computer/phone'): 37, np.str_('Eat, Talk, Computer/phone'): 7, np.str_('Eat, Talk, TV'): 6, np.str_('Talk, TV'): 7, np.str_('Talk, Other activity'): 2}
sub-03_ses-4_ 96 71 24.0 2000-01-03T19:00:00-05:00 {np.str_('Computer/phone'): 152, np.str_('Talk, Computer/phon
[... 46 more lines not kept]
```

**Agent**

Cohort check looks promising (only participants 1, 2, 4, 5, 8 have ≥1 h each of Talk and TV). Checking good-electrode counts against Table 1 under different readings.

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; python -c "
import json; r=json.load(open('$TMPDIR/survey.json'))
from collections import defaultdict
g=defaultdict(list)
for x in sorted(r,key=lambda x:x['path']): g[x['path'][:6]].append(set(x['good_idx']))
for s,l in g.items():
    inter=set.intersection(*l); uni=set.union(*l)
    print(s, 'per day',[len(a) for a in l],'inter',len(inter),'union',len(uni))
"
```

```
sub-01 per day [85, 91, 91, 91] inter 85 union 91
sub-02 per day [85, 85, 81, 80] inter 79 union 85
sub-03 per day [79, 71, 76, 79] inter 69 union 79
sub-04 per day [67, 80, 81, 82, 77] inter 58 union 83
sub-05 per day [104, 104, 100] inter 99 union 105
sub-06 per day [70, 70, 76, 74, 79] inter 62 union 79
sub-07 per day [63, 63, 63, 63, 61] inter 61 union 63
sub-08 per day [83, 82, 87, 82, 85] inter 68 union 91
sub-09 per day [124, 123, 116, 121, 106] inter 94 union 125
sub-10 per day [121, 121, 117, 121, 106] inter 96 union 124
sub-11 per day [103, 103, 105, 105, 105] inter 102 union 105
sub-12 per day [112, 115, 113, 113, 111] inter 103 union 118
```

**Agent**

Good electrodes per day vary, and Table 1's counts match no single reading (finding to report). Now writing the helper module with the fast reader and feature extraction.

**Agent calls Bash**

```bash
mkdir -p entries/alasfour-2024; date -u
```

```
Tue Nov 10 04:00:40 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "entries/alasfour-2024/ajile.py",
 "content": "\"\"\"Loading and measures for AJILE12 (DANDI:000055) as used by Alasfour and Gilja (2024).\n\nWhere each parameter comes from:\n\n- ``VERSION``: the only published version of the dandiset (the paper cites none).\n- ``PARTICIPANTS``: Table 1 of the paper (participants 1, 2, 4, 5, 8); the dandiset's\n  ``sub-01`` and so on are AJILE12's participant numbers (Peterson et al., 2022).\n- ``BANDS``: the claims file, M2 (Methods 2.1; beta is 8 to 32 Hz as printed).\n- Butterworth order 4, zero phase: the claims file, O3, a standard choice. Zero-phase\n  filtering (filtfilt) has the frequency response ``|H(f)|**2``; it is applied here in the\n  frequency domain together with the Hilbert transform, which gives the same envelope as\n  ``sosfiltfilt`` followed by ``scipy.signal.hilbert`` up to edge effects. 5 s of signal on\n  each side of a block is filtered with it and then dropped (``PAD_S``), a standard choice.\n- ``BIN_S``: 10-s bins, the claims file, M2.\n- Artifact rule constants (``ART_SD``, ``ART_FRAC``, ``ART_DUR_S``): the claims file, M3 and\n  O4 (Methods 2.1). The SD of a channel is the ``standard_deviation`` column of the day's\n  electrodes table (reading O4 (ii)) or the pooled SD over the participant's days (O4 (i)).\n- Labels: the epochs table's ``labels``; only blocks labelled with exactly one of ``Talk``,\n  ``TV`` or ``Computer/phone`` are classes (an assumption: a block with two labels cannot be\n  given to one class; the paper does not say).\n- ROI projection matrices: Figshare item 10.6084/m9.figshare.12114408.v1 (Peterson et al.,\n  2021a), as the claims file's header names it.\n\"\"\"\n\nimport io\nimport struct\nimport threading\nimport time\nimport zlib\nfrom concurrent.futures import ThreadPoolExecutor\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nimport requests\nimport scipy.fft as sfft\nfrom requests.adapters import HTTPAdapter\nfrom scipy import signal, stats\n\nDANDISET = \"000055\"\nVERSION = \"0.220127.0436\"\nAPI = \"https://api.dandiarchive.org/api\"\nPARTICIPANTS = [\"01\", \"02\", \"04\", \"05\", \"08\"]\nFS = 500.0\nBANDS = {\n    \"theta\": (4.0, 8.0),\n    \"alpha\": (8.0, 12.0),\n    \"beta\": (8.0, 32.0),\n    \"low_gamma\": (32.0, 55.0),\n    \"high_gamma\": (70.0, 110.0),\n}\nBAND_NAMES = list(BANDS)\nFILTER_ORDER = 4\nPAD_S = 5.0\nBIN_S = 10.0\nART_SD = 3.0\nART_FRAC = 0.10\nART_DUR_S = 2.0\nCLASS_LABELS = {\"Talk\": \"Talk\", \"TV\": \"TV\", \"Computer/phone\": \"Electronics\"}\n\nFIGSHARE_ARTICLE = 12114408\nFIGSHARE_DOI = \"10.6084/m9.figshare.12114408.v1\"\nROIS = [\n    \"Precentral\",\n    \"Frontal_Mid\",\n    \"Postcentral\",\n    \"Parietal_Inf\",\n    \"SupraMarginal\",\n    \"Temporal_Sup\",\n    \"Temporal_Mid\",\n    \"Temporal_Inf\",\n]\nROI_NAMES = {\n    \"Precentral\": \"precentral\",\n    \"Frontal_Mid\": \"middle frontal\",\n    \"Postcentral\": \"postcentral\",\n    \"Parietal_Inf\": \"inferior parietal\",\n    \"SupraMarginal\": \"supramarginal\",\n    \"Temporal_Sup\": \"superior temporal\",\n    \"Temporal_Mid\": \"middle temporal\",\n    \"Temporal_Inf\": \"inferior temporal\",\n}\n\n_session = requests.Session()\n_session.mount(\"https://\", HTTPAdapter(pool_maxsize=64, max_retries=3))\n\n\n# ----------------------------------------------------------------------------- archive\n\n\ndef list_assets():\n    \"\"\"Assets of the pinned version: DataFrame with path, asset_id, size, subject, session.\"\"\"\n    url = f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/?page_size=200\"\n    rows = []\n    while url:\n        d = _session.get(url, timeout=60).json()\n        rows += d[\"results\"]\n        url = d[\"next\"]\n    df = pd.DataFrame([dict(path=a[\"path\"], asset_id=a[\"asset_id\"], size=a[\"size\"]) for a in rows])\n    df[\"subject\"] = df.path.str.extract(r\"sub-(\\d+)\")[0]\n    df[\"session\"] = df.path.str.extract(r\"ses-(\\d+)\")[0].astype(int)\n    return df.sort_values([\"subject\", \"session\"]).reset_index(drop=True)\n\n\ndef s3_url(asset_id):\n    r = _session.head(f\"{API}/assets/{asset_id}/download/\", allow_redirects=True, timeout=60)\n    return r.url\n\n\ndef open_nwb(asset_id):\n    \"\"\"Open an asset by streaming (remfile and h5py). Returns (h5py.File, url).\"\"\"\n    url = s3_url(asset_id)\n    return h5py.File(remfile.File(url), \"r\"), url\n\n\ndef _get_range(url, off, n):\n    for attempt in range(6):\n        try:\n            r = _session.get(url, headers={\"Range\": f\"bytes={off}-{off + n - 1}\"}, timeout=120)\n            if r.status_code in (200, 206) and len(r.content) == n:\n                return r.content\n        except requests.RequestException:\n            pass\n        time.sleep(1 + 2 * attempt)\n    raise IOError(f\"range read failed at {off}\")\n\n\nclass _LoggingFile(io.RawIOBase):\n    \"\"\"A file-like view of a URL that records the offsets h5py reads (to find the B-tree root).\"\"\"\n\n    def __init__(self, url):\n        self.url, self.pos, self.log = url, 0, []\n        r = _session.get(url, headers={\"Range\": \"bytes=0-0\"}, timeout=60)\n        self.size = int(r.headers[\"Content-Range\"].split(\"/\")[1])\n\n    def seek(self, o, wh=0):\n        self.pos = o if wh == 0 else (self.pos + o if wh == 1 else self.size + o)\n        return self.pos\n\n    def tell(self):\n        return self.pos\n\n    def readable(self):\n        return True\n\n    def seekable(self):\n        return True\n\n    def readinto(self, buf):\n        n = min(len(buf), self.size - self.pos)\n        if n <= 0:\n            return 0\n        b = _get_range(self.url, self.pos, n)\n        self.log.append((self.pos, b[:4]))\n        buf[:n] = b\n        self.pos += n\n        return n\n\n\ndef chunk_index(url, path=\"acquisition/ElectricalSeries/data\", threads=48):\n    \"\"\"Byte offset and size of every chunk of a 2-D chunked dataset.\n\n    h5py's own chunk queries walk the version-1 B-tree node by node over the network\n    (about 200 s per file here); this reads the same B-tree level by level in parallel.\n    Returns (shape, chunks, {chunk_offset_tuple: (byte_offset, nbytes)}).\n    \"\"\"\n    lf = _LoggingFile(url)\n    f = h5py.File(lf, \"r\")\n    d = f[path]\n    shape, chunks = d.shape, d.chunks\n    plist = d.id.get_create_plist()\n    filters = [plist.get_filter(i)[0] for i in range(plist.get_nfilters())]\n    assert filters == [h5py.h5z.FILTER_DEFLATE], filters\n    n0 = len(lf.log)\n    probe = d.id.get_chunk_info_by_coord((0, 0))\n    roots = [o for o, b in lf.log[n0:] if b == b\"TREE\"]\n    if not roots:  # root already cached by h5py on open: take the first TREE read overall\n        roots = [o for o, b in lf.log if b == b\"TREE\"]\n    f.close()\n    rank = len(shape)\n    ks = 8 + 8 * (rank + 1)\n\n    def node(addr):\n        h = _get_range(url, addr, 24)\n        assert h[:4] == b\"TREE\"\n        lvl, used = h[5], struct.unpack(\"<H\", h[6:8])[0]\n        b = _get_range(url, addr + 24, used * (ks + 8) + ks)\n        out = []\n        for i in range(used):\n            p = i * (ks + 8)\n            sz, mask = struct.unpack(\"<II\", b[p : p + 8])\n            offs = struct.unpack(\"<%dQ\" % (rank + 1), b[p + 8 : p + ks])[:rank]\n            child = struct.unpack(\"<Q\", b[p + ks : p + ks + 8])[0]\n            out.append((lvl, sz, mask, offs, child))\n        return out\n\n    info, level = {}, [roots[0]]\n    with ThreadPoolExecutor(threads) as ex:\n        while level:\n            nxt = []\n            for ents in ex.map(node, level):\n                for lvl, sz, mask, offs, child in ents:\n                    if lvl == 0:\n                        assert mask == 0\n                        info[offs] = (child, sz)\n                    else:\n                        nxt.append(child)\n            level = nxt\n    assert info[(0, 0)] == (probe.byte_offset, probe.size)\n    n_expected = int(np.ceil(shape[0] / chunks[0]) * np.ceil(shape[1] / chunks[1]))\n    assert len(info) == n_expected, (len(info), n_expected)\n    return shape, chunks, info\n\n\ndef read_meta(asset_id):\n    \"\"\"Epochs, electrodes table and series attributes of one file (no signal data).\"\"\"\n    f, url = open_nwb(asset_id)\n    e = f[\"general/extracellular_ephys/electrodes\"]\n    el = pd.DataFrame(\n        {\n            k: (e[k][:].astype(str) if e[k].dtype.kind in \"OS\" else e[k][:])\n            for k in e.keys()\n            if k != \"group\"\n        }\n    )\n    ep = f[\"intervals/epochs\"]\n    epochs = pd.DataFrame(\n        dict(\n            label=ep[\"labels\"][:].astype(str),\n            start=ep[\"start_time\"][:],\n            stop=ep[\"stop_time\"][:],\n        )\n    )\n    es = f[\"acquisition/ElectricalSeries\"]\n    meta = dict(\n        session_start=f[\"session_start_time\"][()].decode(),\n        subject_id=f[\"general/subject/subject_id\"][()].decode(),\n        rate=float(es[\"starting_time\"].attrs[\"rate\"]),\n        starting_time=float(es[\"starting_time\"][()]),\n        conversion=float(es[\"data\"].attrs[\"conversion\"]),\n        unit=str(es[\"data\"].attrs[\"unit\"]),\n        shape=es[\"data\"].shape,\n        chunks=es[\"data\"].chunks,\n        electrodes_index=es[\"electrodes\"][:],\n    )\n    f.close()\n    return meta, el, epochs, url\n\n\n# ----------------------------------------------------------------------------- features\n\n\n_resp_cache = {}\n\n\ndef _band_responses(nfft):\n    \"\"\"For each band, the rfft bins where the zero-phase response |H|^2 exceeds 1e-6.\"\"\"\n    if nfft in _resp_cache:\n        return _resp_cache[nfft]\n    freqs = np.fft.rfftfreq(nfft, 1 / FS)\n    out = []\n    for lo, hi in BANDS.values():\n        sos = signal.butter(FILTER_ORDER, [lo, hi], btype=\"bandpass\", fs=FS, output=\"sos\")\n        _, h = signal.sosfreqz(sos, worN=freqs, fs=FS)\n        h2 = np.abs(h) ** 2\n        k = np.where(h2 > 1e-6)[0]\n        k0, k1 = k[0], k[-1] + 1\n        m = sfft.next_fast_len(k1 - k0)\n        w = h2[k0:k1] * 2.0  # analytic signal: positive frequencies doubled\n        out.append((k0, k1, m, w))\n    _resp_cache[nfft] = out\n    return out\n\n\ndef band_envelopes(x):\n    \"\"\"Hilbert envelopes of each band of x (samples by channels), at reduced rate.\n\n    Returns a list (one per band) of (times_in_samples, envelope array (m, channels)).\n    The analytic signal of a band is band-limited, so its magnitude is computed from the\n    band's own bins shifted to zero frequency, sampled at m points over the segment.\n    \"\"\"\n    n = x.shape[0]\n    X = sfft.rfft(x, axis=0, workers=4)\n    out = []\n    for k0, k1, m, w in _band_responses(n):\n        Z = np.zeros((m, x.shape[1]), dtype=np.complex128)\n        Z[: k1 - k0] = X[k0:k1] * w[:, None]\n        z = sfft.ifft(Z, axis=0, workers=4)\n        env = np.abs(z) / n  # |analytic(t)| = |sum_k Z_k e^{...}| / n\n        t = np.arange(m) * (n / m)\n        out.append((t, env))\n    return out\n\n\ndef envelope_check(x):\n    \"\"\"Envelope of one channel by sosfiltfilt and scipy.signal.hilbert, for comparison.\"\"\"\n    res = []\n    for lo, hi in BANDS.values():\n        sos = signal.butter(FILTER_ORDER, [lo, hi], btype=\"bandpass\", fs=FS, output=\"sos\")\n        res.append(np.abs(signal.hilbert(signal.sosfiltfilt(sos, x))))\n    return res\n\n\ndef _runs(mask):\n    \"\"\"Total True count and longest True run, per column of a boolean array.\"\"\"\n    total = mask.sum(0)\n    pad = np.zeros((1, mask.shape[1]), bool)\n    m = np.vstack([pad, mask, pad]).astype(np.int8)\n    d = np.diff(m, axis=0)\n    longest = np.zeros(mask.shape[1], int)\n    for c in np.where(total > 0)[0]:\n        s = np.where(d[:, c] == 1)[0]\n        e = np.where(d[:, c] == -1)[0]\n        longest[c] = (e - s).max()\n    return total, longest\n\n\ndef block_features(seg, i0, i1, sds):\n    \"\"\"Features and artifact statistics of one block.\n\n    seg: samples by channels (microvolts), with padding; the block is seg[i0:i1].\n    sds: list of per-channel SD arrays (one per artifact reading).\n    Returns dict with feats (bins, channels, bands), exceed totals and longest runs.\n    \"\"\"\n    seg = seg.astype(np.float64)\n    seg = seg - np.median(seg, axis=0)\n    envs = band_envelopes(seg)\n    nb = int(np.floor((i1 - i0) / (BIN_S * FS)))\n    feats = np.full((nb, seg.shape[1], len(BANDS)), np.nan, np.float32)\n    for bi, (t, env) in enumerate(envs):\n        rel = (t - i0) / (BIN_S * FS)\n        idx = np.floor(rel).astype(int)\n        for b in range(nb):\n            sel = idx == b\n            feats[b, :, bi] = env[sel].mean(0)\n    blk = seg[i0:i1]\n    blk_raw = blk + 0.0\n    tot, lon = [], []\n    for sd in sds:\n        a, b = _runs(np.abs(blk_raw) > ART_SD * sd[None, :])\n        tot.append(a)\n        lon.append(b)\n    return dict(\n        feats=feats,\n        exceed_total=np.array(tot),\n        exceed_longest=np.array(lon),\n        sumsq=(blk_raw.astype(np.float64) ** 2).sum(0),\n        n=blk.shape[0],\n    )\n\n\ndef extract_day(asset_id, channels, blocks, sds, threads=48, window=6, log=None):\n    \"\"\"Stream the blocks of one file and compute their features.\n\n    channels: electrode indices (columns of the ElectricalSeries) to read.\n    blocks: DataFrame with start, stop (s) and label; one row per 2-min block.\n    sds: list of per-channel SD arrays (microvolts, for ``channels``), one per artifact reading.\n    Only the chunks covering the blocks (plus ``PAD_S``) and the requested channels are read.\n    \"\"\"\n    url = s3_url(asset_id)\n    shape, chunks, info = chunk_index(url)\n    ch_len = chunks[0]\n    assert chunks[1] == 1\n    pad = int(PAD_S * FS)\n    spans = []\n    for b in blocks.itertuples():\n        i0 = int(round(b.start * FS))\n        i1 = int(round(b.stop * FS))\n        a0, a1 = max(0, i0 - pad), min(shape[0], i1 + pad)\n        spans.append((a0, a1, i0, i1))\n    rows_needed = sorted({r for a0, a1, _, _ in spans for r in range(a0 // ch_len, (a1 - 1) // ch_len + 1)})\n    last_use = {}\n    for k, (a0, a1, _, _) in enumerate(spans):\n        for r in range(a0 // ch_len, (a1 - 1) // ch_len + 1):\n            last_use[r] = k\n\n    def fetch_chunk(key):\n        off, sz = info[key]\n        raw = zlib.decompress(_get_range(url, off, sz))\n        a = np.frombuffer(raw, dtype=\"<f4\")\n        return a\n\n    ex = ThreadPoolExecutor(threads)\n\n    def fetch_row(r):\n        futs = [ex.submit(fetch_chunk, (r * ch_len, c)) for c in channels]\n        arr = np.stack([f.result() for f in futs], axis=1)\n        n_valid = min(ch_len, shape[0] - r * ch_len)\n        return arr[:n_valid]\n\n    row_ex = ThreadPoolExecutor(window)\n    pending = {}\n    nxt = 0\n\n    def ensure(upto):\n        nonlocal nxt\n        while nxt < len(rows_needed) and len(pending) < window + 2:\n            r = rows_needed[nxt]\n            pending[r] = row_ex.submit(fetch_row, r)\n            nxt += 1\n\n    have = {}\n    out = []\n    nbytes = 0\n    for k, (a0, a1, i0, i1) in enumerate(spans):\n        r0, r1 = a0 // ch_len, (a1 - 1) // ch_len\n        for r in range(r0, r1 + 1):\n            if r not in have:\n                ensure(r)\n                while r not in pending:\n                    ensure(r)\n                have[r] = pending.pop(r).result()\n                nbytes += sum(info[(r * ch_len, c)][1] for c in channels)\n                ensure(r)\n        seg = np.concatenate([have[r] for r in range(r0, r1 + 1)], axis=0)\n        seg = seg[a0 - r0 * ch_len : a1 - r0 * ch_len]\n        res = block_features(seg, i0 - a0, i1 - a0, sds)\n        out.append(res)\n        for r in list(have):\n            if last_use[r] <= k:\n                del have[r]\n    row_ex.shutdown()\n    ex.shutdown()\n    return out, nbytes\n\n\n# ----------------------------------------------------------------------------- ROIs\n\n\ndef figshare_files():\n    d = _session.get(f\"https://api.figshare.com/v2/articles/{FIGSHARE_ARTICLE}\", timeout=60).json()\n    return {f[\"name\"]: f for f in d[\"files\"]}, d\n\n\ndef load_projection(participant, files=None):\n    \"\"\"Projection matrix of one participant: (density per ROI, weights electrodes by ROI).\n\n    Columns are AAL regions of both hemispheres; the first numerical row is the electrode\n    density of each region (the Figshare item's description).\n    \"\"\"\n    files = files or figshare_files()[0]\n    f = files[f\"aal_{participant}_elecs2ROI.csv\"]\n    r = _session.get(f[\"download_url\"], timeout=120)\n    import hashlib\n\n    assert hashlib.md5(r.content).hexdigest() == f[\"computed_md5\"]\n    d = pd.read_csv(io.BytesIO(r.content))\n    return d.iloc[0], d.iloc[1:].reset_index(drop=True)\n\n\ndef load_centroids(files=None):\n    files = files or figshare_files()[0]\n    f = files[\"aal_01_ROIcentroids_Lside.csv\"]\n    r = _session.get(f[\"download_url\"], timeout=120)\n    return pd.read_csv(io.BytesIO(r.content))\n\n\n# ----------------------------------------------------------------------------- statistics\n\n\ndef bh_fdr(p, alpha):\n    \"\"\"Benjamini-Hochberg as written in Methods 2.2: reject all p <= P_k.\"\"\"\n    p = np.asarray(p, float)\n    ok = np.isfinite(p)\n    rej = np.zeros(p.shape, bool)\n    ps = np.sort(p[ok])\n    n = len(ps)\n    below = np.where(ps <= (np.arange(1, n + 1) / n) * alpha)[0]\n    if len(below):\n        pk = ps[below.max()]\n        rej[ok] = p[ok] <= pk\n    return rej\n\n\ndef finite_chance(n, c, alpha):\n    \"\"\"Combrisson and Jerbi (2015): binomial inverse at 1 - alpha for n samples, c classes.\"\"\"\n    return stats.binom.ppf(1 - alpha, n, 1.0 / c) / n\n"
}
```

```
File created successfully at: entries/alasfour-2024/ajile.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/alasfour-2024 && sed -i 's|        env = np.abs(z) / n  # |analytic(t)| = |sum_k Z_k e^{...}| / n|        env = np.abs(z) * (m / n)  # ifft_m carries 1/m; the analytic signal 1/n|' ajile.py && grep -n "env = np.abs" ajile.py; . $TMPDIR/env/bin/activate; cat > $TMPDIR/t1.py <<'EOF'
import sys, time, resource, numpy as np
sys.path.insert(0,'.')
import ajile as A
assets=A.list_assets()
a=assets[(assets.subject=='08')&(assets.session==3)].iloc[0]
meta,el,ep,url=A.read_meta(a.asset_id)
print(meta)
blocks=ep[ep.label.isin(['Talk','TV','Computer/phone'])].reset_index(drop=True)
print(len(blocks))
ch=np.where(el.good.values)[0]
sd=el.standard_deviation.values[ch]
t=time.time()
out,nb=A.extract_day(a.asset_id, ch, blocks.iloc[:12], [sd, sd])
dt=time.time()-t
print('12 blocks',dt, nb/1e6,'MB', nb/1e6/dt,'MB/s', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
print(out[0]['feats'].shape, out[0]['exceed_total'][0][:10], out[0]['exceed_longest'][0][:10])
print('sd check', np.sqrt(out[0]['sumsq']/out[0]['n'])[:8], sd[:8])
# envelope check on block 0, channel 0
f,u=A.open_nwb(a.asset_id)
b=blocks.iloc[0]; i0=int(round(b.start*500)); i1=int(round(b.stop*500))
x=f['acquisition/ElectricalSeries/data'][max(0,i0-2500):i1+2500, ch[0]].astype(float)
x=x-np.median(x)
ref=A.envelope_check(x)
o=i0-max(0,i0-2500)
for bi,r in enumerate(ref):
    rb=[r[o+k*5000:o+(k+1)*5000].mean() for k in range(out[0]['feats'].shape[0])]
    print(A.BAND_NAMES[bi], np.round(rb[:4],3), np.round(out[0]['feats'][:4,0,bi],3))
EOF
python $TMPDIR/t1.py
```

```
sed: -e expression #1, char 48: unknown option to `s'
{'session_start': '2000-01-02T19:00:00-05:00', 'subject_id': '08', 'rate': 500.0, 'starting_time': 0.0, 'conversion': 1e-06, 'unit': 'volts', 'shape': (43200000, 92), 'chunks': (84375, 1), 'electrodes_index': array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
       34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
       68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
       85, 86, 87, 88, 89, 90, 91])}
59
12 blocks 29.114802360534668 363.891622 MB 12.498509091487353 MB/s 0.873816 GB
(12, 83, 5) [ 39  68 208 106 168  61  34  38  76 110] [11 12 40 24 21 14 13  8  9 33]
sd check [38.54255957 21.17283143 41.36113994 41.46760329 52.09820333 26.76960256
 42.49650349 31.08992378] [52.51216865 27.25805799 51.83329851 57.25078829 60.7625326  31.86563377
 54.86186598 39.16833076]
theta [14.845 15.492 16.228 15.45 ] [0.005 0.005 0.006 0.005]
alpha [14.746 13.995 11.172 13.149] [0.005 0.005 0.004 0.005]
beta [23.636 21.382 20.887 22.178] [0.002 0.001 0.001 0.002]
low_gamma [7.318 7.245 8.244 7.458] [0.001 0.001 0.001 0.001]
high_gamma [3.469 3.647 4.331 3.935] [0. 0. 0. 0.]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/alasfour-2024/ajile.py",
 "old_string": "        env = np.abs(z) / n  # |analytic(t)| = |sum_k Z_k e^{...}| / n",
 "new_string": "        env = np.abs(z) * (m / n)  # ifft of length m divides by m; the analytic signal by n"
}
```

```
The file entries/alasfour-2024/ajile.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cat > $TMPDIR/t2.py <<'EOF'
import sys, time, numpy as np
sys.path.insert(0,'.')
import ajile as A
x=np.random.randn(65000,90).astype(np.float32)*50
sd=np.ones(90)*50
t=time.time(); r=A.block_features(x,2500,62500,[sd,sd]); print('block compute',time.time()-t)
t=time.time(); A.band_envelopes(x.astype(float)); print('env',time.time()-t)
EOF
python $TMPDIR/t2.py
```

```
block compute 0.27236509323120117
env 0.09799385070800781
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cat > $TMPDIR/t3.py <<'EOF'
import sys, time, resource, numpy as np
sys.path.insert(0,'.')
import ajile as A
assets=A.list_assets()
a=assets[(assets.subject=='08')&(assets.session==3)].iloc[0]
meta,el,ep,url=A.read_meta(a.asset_id)
blocks=ep[ep.label.isin(['Talk','TV','Computer/phone'])].reset_index(drop=True)
ch=np.where(el.good.values)[0]; sd=el.standard_deviation.values[ch]
t=time.time()
url=A.s3_url(a.asset_id); A.chunk_index(url); print('index',time.time()-t)
t=time.time()
out,nb=A.extract_day(a.asset_id, ch, blocks, [sd, sd], threads=64, window=10)
dt=time.time()-t
print(len(blocks),'blocks',dt, nb/1e6,'MB', nb/1e6/dt,'MB/s', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
print(np.round(out[0]['feats'][:3,0,:],2))
EOF
python $TMPDIR/t3.py
```

```
index 8.831986904144287
59 blocks 35.79935812950134 2104.762118 MB 58.79329205809193 MB/s 1.29254 GB
[[14.87 14.75 23.63  7.31  3.47]
 [15.48 13.99 21.38  7.24  3.65]
 [16.24 11.17 20.89  8.24  4.33]]
```

**Agent calls Bash**

```bash
cat >> ajile.py <<'EOF'


# ----------------------------------------------------------------------------- whole dataset


def class_blocks(epochs):
    """Blocks labelled with exactly one class label (Talk, TV, Computer/phone)."""
    b = epochs[epochs.label.isin(list(CLASS_LABELS))].copy()
    b["cls"] = b.label.map(CLASS_LABELS)
    return b.reset_index(drop=True)


def survey(assets, procs=8):
    """Metadata of every file: (dict of (subject, session) -> (meta, electrodes, epochs))."""
    from multiprocessing import Pool

    with Pool(procs) as p:
        res = p.map(read_meta, list(assets.asset_id))
    return {
        (s, ses): (m, el, ep)
        for (s, ses), (m, el, ep, _) in zip(zip(assets.subject, assets.session), res)
    }


def _extract_job(job):
    asset_id, channels, blocks, sds = job
    t = time.time()
    out, nbytes = extract_day(asset_id, channels, blocks, sds)
    return out, nbytes, time.time() - t


def extract_participant_days(jobs, procs=3):
    """Run extract_day over (asset_id, channels, blocks, sds) jobs in parallel processes."""
    from multiprocessing import get_context

    with get_context("spawn").Pool(procs) as p:
        return p.map(_extract_job, jobs, chunksize=1)
EOF
. $TMPDIR/env/bin/activate; cat > $TMPDIR/full.py <<'EOF'
import sys, time, resource, pickle, numpy as np, pandas as pd
sys.path.insert(0,'entries/alasfour-2024')
import ajile as A
if __name__=='__main__':
    t0=time.time()
    assets=A.list_assets()
    sel=assets[assets.subject.isin(A.PARTICIPANTS)]
    meta=A.survey(sel)
    print('survey',time.time()-t0)
    jobs=[]; keys=[]
    chans={}
    for p in A.PARTICIPANTS:
        days=sorted(s for (q,s) in meta if q==p)
        good=np.zeros(len(meta[(p,days[0])][1]),bool)
        for d in days: good|=meta[(p,d)][1].good.values
        ch=np.where(good)[0]; chans[p]=ch
        nsamp=np.array([meta[(p,d)][0]['shape'][0] for d in days])
        sdd=np.array([meta[(p,d)][1].standard_deviation.values[ch] for d in days])
        pooled=np.sqrt((nsamp[:,None]*sdd**2).sum(0)/nsamp.sum())
        for i,d in enumerate(days):
            b=A.class_blocks(meta[(p,d)][2])
            aid=sel[(sel.subject==p)&(sel.session==d)].asset_id.iloc[0]
            jobs.append((aid,ch,b,[sdd[i],pooled])); keys.append((p,d))
    # biggest first
    order=np.argsort([-len(j[2])*len(j[1]) for j in jobs])
    jobs=[jobs[i] for i in order]; keys=[keys[i] for i in order]
    res=A.extract_participant_days(jobs, procs=int(sys.argv[1]) if len(sys.argv)>1 else 3)
    tot=sum(r[1] for r in res)
    print('done',time.time()-t0, tot/1e9,'GB', [round(r[2]) for r in res])
    pickle.dump(dict(meta=meta,keys=keys,jobs=[(j[0],j[1],j[2]) for j in jobs],res=[r[0] for r in res],chans=chans),open('/tmp/claude-1001/feats.pkl','wb'))
    print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6, resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss/1e6)
EOF
date -u
```

```
Tue Nov 10 04:04:17 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cd $TMPDIR; sed 's|res=A.extract_participant_days(jobs|jobs=jobs[-3:]; keys=keys[-3:]; res=A.extract_participant_days(jobs|; s|feats.pkl|feats_sub.pkl|' full.py > sub.py; time python sub.py 3 2>&1 | tail -5
```

```
survey 6.605971097946167
done 61.70855164527893 4.580515491 GB [54, 47, 34]
0.173832 1.148892

real	1m2.768s
user	2m20.404s
sys	0m24.373s
Shell cwd was reset to
```

**Agent**

Subset works (~83 MB/s with 3 processes). Running the full extraction now (estimated ~25 min) to cache features for development.

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cd $TMPDIR; time python full.py 4 2>&1 | tail -5; date -u
```

```
return self._map_async(func, iterable, mapstar, chunksize).get()
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/multiprocessing/pool.py", line 774, in get
    raise self._value
ValueError: need at least one array to concatenate

real	15m0.877s
user	51m14.834s
sys	6m47.355s
Tue Nov 10 04:20:35 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/alasfour-2024; python3 - <<'EOF'
s=open('ajile.py').read()
old="""    out = []
    nbytes = 0
    for k, (a0, a1, i0, i1) in enumerate(spans):
        r0, r1 = a0 // ch_len, (a1 - 1) // ch_len"""
new="""    out = []
    nbytes = 0
    for k, (a0, a1, i0, i1) in enumerate(spans):
        if i0 < 0 or i1 > shape[0] or i1 <= i0:
            out.append(None)  # block outside the recorded samples: counted as dropped
            continue
        r0, r1 = a0 // ch_len, (a1 - 1) // ch_len"""
assert old in s; s=s.replace(old,new)
old2="""        spans.append((a0, a1, i0, i1))
    rows_needed = sorted({r for a0, a1, _, _ in spans for r in range(a0 // ch_len, (a1 - 1) // ch_len + 1)})
    last_use = {}
    for k, (a0, a1, _, _) in enumerate(spans):
        for r in range(a0 // ch_len, (a1 - 1) // ch_len + 1):"""
new2="""        spans.append((a0, a1, i0, i1))
    ok = [i0 >= 0 and i1 <= shape[0] and i1 > i0 for _, _, i0, i1 in spans]
    rows_needed = sorted(
        {r for (a0, a1, _, _), g in zip(spans, ok) if g for r in range(a0 // ch_len, (a1 - 1) // ch_len + 1)}
    )
    last_use = {}
    for k, ((a0, a1, _, _), g) in enumerate(zip(spans, ok)):
        if not g:
            continue
        for r in range(a0 // ch_len, (a1 - 1) // ch_len + 1):"""
assert old2 in s; s=s.replace(old2,new2)
old3="""    with get_context("spawn").Pool(procs) as p:
        return p.map(_extract_job, jobs, chunksize=1)"""
new3="""    with get_context("spawn").Pool(procs) as p:
        res = dict(p.imap_unordered(_extract_indexed, list(enumerate(jobs))))
    return [res[i] for i in range(len(jobs))]


def _extract_indexed(ij):
    i, job = ij
    return i, _extract_job(job)"""
assert old3 in s; s=s.replace(old3,new3)
open('ajile.py','w').write(s)
EOF
cd $TMPDIR; python3 - <<'EOF'
s=open('full.py').read()
s=s.replace("""    res=A.extract_participant_days(jobs, procs=int(sys.argv[1]) if len(sys.argv)>1 else 3)""",
"""    import os
    from multiprocessing import get_context
    todo=[i for i in range(len(jobs)) if not os.path.exists(f'/tmp/claude-1001/job_{keys[i][0]}_{keys[i][1]}.pkl')]
    with get_context('spawn').Pool(int(sys.argv[1])) as pool:
        for i,r in pool.imap_unordered(A._extract_indexed, [(i,jobs[i]) for i in todo]):
            pickle.dump(r, open(f'/tmp/claude-1001/job_{keys[i][0]}_{keys[i][1]}.pkl','wb')); print(keys[i], round(r[2]), flush=True)
    res=[pickle.load(open(f'/tmp/claude-1001/job_{k[0]}_{k[1]}.pkl','rb')) for k in keys]""")
open('full.py','w').write(s)
EOF
. $TMPDIR/env/bin/activate; time python full.py 4 2>&1 | tail -30; date -u
```

```
survey 5.440507173538208
('01', 7) 150
('05', 7) 301
('01', 5) 303
('01', 4) 370
('05', 4) 286
('02', 6) 235
('04', 7) 274
('01', 3) 235
('04', 6) 217
('05', 3) 120
('04', 5) 197
('04', 3) 29
('02', 5) 112
('04', 4) 204
('02', 4) 93
('08', 5) 87
('08', 4) 83
('08', 3) 77
('08', 7) 36
[... 10 more lines not kept]
```

**Agent**

Full extraction took 15 min (82.6 GB streamed). Now checking the link between the Figshare projection matrices and the dataset's electrodes.

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cd $TMPDIR; python - <<'EOF'
import pickle, numpy as np, pandas as pd, sys
sys.path.insert(0,'entries/alasfour-2024')
import ajile as A
D=pickle.load(open('feats.pkl','rb'))
meta=D['meta']
files,_=A.figshare_files()
cen=A.load_centroids(files)
names=pd.read_csv(A._session.get(files['aal_01_elecs2ROI.csv']['download_url']).content.decode() and __import__('io').BytesIO(A._session.get(files['aal_01_elecs2ROI.csv']['download_url']).content)).columns
print(len(names), cen.shape)
L=[i for i,n in enumerate(names) if n.endswith('_L')]
for p in A.PARTICIPANTS:
    dens,W=A.load_projection(p,files)
    el=meta[(p,3)][1] if (p,3) in meta else None
    xyz=el[['x','y','z']].values.copy(); xyz[:,0]=-np.abs(xyz[:,0])
    print(p, 'rows',len(W),'electrodes',len(el))
    n=min(len(W),len(el))
    # unnormalized g = w*dens for L columns
    C=cen.values[L]  # centroids rows correspond to columns order?
    g=(W.values[:n][:,L]*dens.values[L][None,:])
    d2=((xyz[:n,None,:]-C[None,:,:])**2).sum(-1)
    ok=(g>1e-300)&(dens.values[L][None,:]>0)
    lg=np.log(g[ok]); x=-d2[ok]
    r=np.corrcoef(lg,x)[0,1]; slope=np.polyfit(x,lg,1)[0]
    print('  corr log g vs -d2 %.5f, sigma %.2f'%(r, np.sqrt(1/(2*slope))))
EOF
```

```
116 (116, 3)
01 rows 98 electrodes 94
  corr log g vs -d2 0.95476, sigma 9.74
02 rows 86 electrodes 86
  corr log g vs -d2 0.95862, sigma 9.76
04 rows 84 electrodes 84
  corr log g vs -d2 0.95626, sigma 9.44
05 rows 106 electrodes 106
  corr log g vs -d2 0.95750, sigma 9.65
08 rows 92 electrodes 92
  corr log g vs -d2 0.95747, sigma 9.63
Shell cwd was reset to
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cd $TMPDIR; python - <<'EOF'
import pickle, numpy as np, pandas as pd, sys, io
sys.path.insert(0,'entries/alasfour-2024')
import ajile as A
D=pickle.load(open('feats.pkl','rb')); meta=D['meta']
files,_=A.figshare_files(); cen=A.load_centroids(files)
for p in A.PARTICIPANTS:
    dens,W=A.load_projection(p,files)
    names=W.columns; L=np.array([n.endswith('_L') for n in names])
    el=meta[(p,3)][1]
    xyz=el[['x','y','z']].values.copy()
    C=cen.values[L]; dl=dens.values[L]; keep=dl>1e-3
    g=W.values[:,L][:,keep]*dl[keep]; lg=np.log(np.maximum(g,1e-300))
    for flip in ['abs','none']:
        q=xyz.copy()
        if flip=='abs': q[:,0]=-np.abs(q[:,0])
        d2=((q[:,None,:]-C[keep][None,:,:])**2).sum(-1)
        # for each electrode, best row by correlation
        best=[]; rs=[]
        for i in range(len(el)):
            c=[np.corrcoef(-d2[i],lg[r])[0,1] for r in range(len(W))]
            best.append(int(np.argmax(c))); rs.append(max(c))
        best=np.array(best)
        n=min(len(W),len(el))
        print(p, flip, 'same index %d/%d'%((best[:n]==np.arange(n)).sum(), len(el)), 'median r %.4f'%np.median(rs), 'offsets', np.unique(best-np.arange(len(el)),return_counts=True))
EOF
```

```
/tmp/claude-1001/env/lib/python3.13/site-packages/numpy/lib/_function_base_impl.py:3037: RuntimeWarning: invalid value encountered in divide
  c /= stddev[:, None]
/tmp/claude-1001/env/lib/python3.13/site-packages/numpy/lib/_function_base_impl.py:3038: RuntimeWarning: invalid value encountered in divide
  c /= stddev[None, :]
01 abs same index 0/94 median r 0.9531 offsets (array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
       35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
       52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68,
       69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
       86, 87, 88, 89, 90, 91, 92, 93, 94]), array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1]))
01 none same index 0/94 median r 0.9531 offsets (array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
       35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
       52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68,
       69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
       86, 87, 88, 89, 90, 91, 92, 93, 94]), array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cd $TMPDIR; python - <<'EOF' 2>/dev/null
import pickle, numpy as np, pandas as pd, sys, io
sys.path.insert(0,'entries/alasfour-2024')
import ajile as A
D=pickle.load(open('feats.pkl','rb')); meta=D['meta']
files,_=A.figshare_files(); cen=A.load_centroids(files)
for p in A.PARTICIPANTS:
    dens,W=A.load_projection(p,files)
    names=np.array(W.columns); L=np.array([n.endswith('_L') for n in names])
    el=meta[(p,3)][1]; xyz=el[['x','y','z']].values.copy(); xyz[:,0]=-np.abs(xyz[:,0])
    C=cen.values[L]; dl=dens.values[L]; keep=dl>0
    g=W.values[:,L]*dl; g[:,~keep]=0
    am=g.argmax(1)            # matrix ROI per row
    d2=((xyz[:,None,:]-C[None])**2).sum(-1); d2[:,~keep]=np.inf
    nn=d2.argmin(1)
    n=min(len(W),len(el))
    for off in ([0] if len(W)==len(el) else range(0,len(W)-len(el)+1)):
        agree=(am[off:off+len(el)]==nn).mean()
        print(p,'offset',off,'ROI agreement %.3f'%agree, 'n rows',len(W),'n el',len(el))
    # matrix eight-ROI members
    lab=[names[L][k][:-2] for k in am]
    print('  ', pd.Series(lab).value_counts().reindex(A.ROIS).fillna(0).astype(int).tolist(), 'dens',np.round(dens[[r+'_L' for r in A.ROIS]].values.astype(float),2).tolist())
EOF
```

```
01 offset 0 ROI agreement 0.628 n rows 98 n el 94
01 offset 1 ROI agreement 0.394 n rows 98 n el 94
01 offset 2 ROI agreement 0.160 n rows 98 n el 94
01 offset 3 ROI agreement 0.074 n rows 98 n el 94
01 offset 4 ROI agreement 0.064 n rows 98 n el 94
   [9, 4, 8, 1, 4, 6, 10, 14] dens [4.72, 3.9, 7.32, 1.34, 3.25, 5.43, 9.71, 8.27]
02 offset 0 ROI agreement 0.512 n rows 86 n el 86
   [0, 0, 4, 6, 6, 3, 22, 12] dens [0.15, 0.0, 3.66, 4.83, 5.06, 3.35, 15.37, 8.62]
04 offset 0 ROI agreement 0.560 n rows 84 n el 84
   [9, 10, 12, 4, 4, 4, 7, 8] dens [8.17, 8.62, 10.18, 2.97, 3.74, 4.45, 4.89, 3.22]
05 offset 0 ROI agreement 0.557 n rows 106 n el 106
   [4, 2, 13, 7, 5, 4, 17, 12] dens [3.54, 3.12, 9.07, 5.77, 4.94, 4.94, 12.99, 8.62]
08 offset 0 ROI agreement 0.641 n rows 92 n el 92
   [4, 7, 10, 2, 4, 6, 13, 8] dens [4.25, 6.4, 8.1, 2.11, 3.94, 5.03, 10.89, 6.45]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> entries/alasfour-2024/ajile.py <<'EOF'


# ----------------------------------------------------------------------------- samples


def artifact_drop(block, good, reading):
    """True when a block is dropped by the artifact rule (Methods 2.1; claims O4).

    reading: (rule, sd) with rule "a" (more than 2 s in total) or "b" (more than 2 s
    contiguous), sd 0 for the day's SD (O4 (ii)) and 1 for the participant's pooled SD (O4 (i)).
    good: boolean mask over the block's channels (the day's good electrodes).
    """
    rule, sd = reading
    stat = block["exceed_total"][sd] if rule == "a" else block["exceed_longest"][sd]
    bad = (stat > ART_DUR_S * FS) & good
    return bad.sum() >= ART_FRAC * good.sum()


def build_samples(days, artifact=("a", 0)):
    """10-s samples of one participant, in time order.

    days: list of (session, session_start_seconds, good_mask_over_channels, blocks_df, results).
    Returns dict: X (samples, channels, bands), cls, day, block id, time, and per-block table.
    """
    Xs, cls, day, blk, tt = [], [], [], [], []
    rows = []
    bid = 0
    for ses, t0, good, blocks, res in days:
        for b, r in zip(blocks.itertuples(), res):
            row = dict(session=ses, start=b.start, stop=b.stop, cls=b.cls, bid=bid)
            if r is None:
                row.update(status="outside recording")
            elif artifact is not None and artifact_drop(r, good, artifact):
                row.update(status="artifact", nbins=r["feats"].shape[0])
            else:
                nb = r["feats"].shape[0]
                row.update(status="kept", nbins=nb)
                Xs.append(r["feats"])
                cls += [b.cls] * nb
                day += [ses] * nb
                blk += [bid] * nb
                tt += list(t0 + b.start + BIN_S * np.arange(nb))
            rows.append(row)
            bid += 1
    X = np.concatenate(Xs, 0)
    order = np.argsort(np.array(tt), kind="stable")
    return dict(
        X=X[order],
        cls=np.array(cls)[order],
        day=np.array(day)[order],
        block=np.array(blk)[order],
        time=np.array(tt)[order],
        blocks=pd.DataFrame(rows),
    )


# ----------------------------------------------------------------------------- ROIs per reading


def roi_assignment(dens, W, xyz, centroids, reading):
    """ROI index (0 to 7, or -1 for none) of each electrode under a reading of O5.

    "a": largest stored projection weight among the eight ROIs (left-hemisphere columns).
    "b": nearest of the eight left-hemisphere ROI centroids, from the dataset's positions
         mirrored to the left hemisphere (x = -|x|).
    "c": the largest unnormalised weight (stored weight times the ROI's density, the
         Gaussian value of Methods 2.1) over all left AAL regions, kept only when that region
         is one of the eight: "thresholded only to include electrodes close to any of the
         eight defined ROIs, and the ROI label was assigned by choosing the ROI closest to
         each electrode" (Methods 2.1).
    """
    names = np.array(W.columns)
    eight = [r + "_L" for r in ROIS]
    n = len(xyz)
    if reading == "a":
        w = W[eight].values[:n]
        return w.argmax(1)
    if reading == "b":
        q = np.array(xyz, float).copy()
        q[:, 0] = -np.abs(q[:, 0])
        cl = np.array([np.where(names == e)[0][0] for e in eight])
        C = centroids.values[cl]
        d2 = ((q[:, None, :] - C[None]) ** 2).sum(-1)
        return d2.argmin(1)
    if reading == "c":
        L = np.array([c.endswith("_L") for c in names])
        g = W.values[:n][:, L] * dens.values[L].astype(float)[None, :]
        best = names[L][g.argmax(1)]
        return np.array([eight.index(b) if b in eight else -1 for b in best])
    raise ValueError(reading)


def roi_channels(assign, dens, channels, density_reading):
    """Channels (positions in ``channels``) of each ROI, dropping ROIs of density below 3.

    density_reading "i": fewer than 3 assigned electrodes; "ii": the matrix's density row
    below 3 (Methods 2.1, "electrode density of less than 3"; claims O5).
    """
    out = {}
    for k, r in enumerate(ROIS):
        idx = [j for j, c in enumerate(channels) if c < len(assign) and assign[c] == k]
        d = len(idx) if density_reading == "i" else float(dens[r + "_L"])
        if len(idx) == 0 or d < 3:
            continue
        out[r] = idx
    return out


# ----------------------------------------------------------------------------- classifier


def folds_and_buffers(n, buffer, k=7):
    """Contiguous folds of the time-ordered samples, with the training folds of each test fold.

    buffer "a": both neighbouring folds left out of training; "b": only the following one
    (the preceding one for the last fold) (claims O7).
    """
    edges = np.linspace(0, n, k + 1).round().astype(int)
    folds = [np.arange(edges[i], edges[i + 1]) for i in range(k)]
    out = []
    for i in range(k):
        if buffer == "a":
            excl = {i - 1, i, i + 1}
        else:
            excl = {i, i + 1} if i < k - 1 else {i, i - 1}
        train = [j for j in range(k) if j not in excl]
        out.append((train, i))
    return folds, out


def balance(idx, y, rng):
    """Random downsampling of every class to the smallest one (claims O8)."""
    classes = np.unique(y[idx])
    m = min((y[idx] == c).sum() for c in classes)
    keep = np.concatenate([rng.choice(idx[y[idx] == c], m, replace=False) for c in classes])
    return np.sort(keep)


def zscore(a):
    sd = a.std(0)
    sd[sd == 0] = 1
    return (a - a.mean(0)) / sd


def lda2(Xtr, ytr, Xte):
    """Two-class LDA with one covariance shared by the classes and equal priors.

    Returns predictions (bool, class 1) and the class means (mean0, mean1).
    Equivalent to scikit-learn's LinearDiscriminantAnalysis without shrinkage on balanced
    data (claims O8).
    """
    m0 = Xtr[~ytr].mean(0)
    m1 = Xtr[ytr].mean(0)
    R = np.concatenate([Xtr[~ytr] - m0, Xtr[ytr] - m1])
    S = R.T @ R / (len(Xtr) - 2)
    w = np.linalg.lstsq(S, m1 - m0, rcond=None)[0]
    b = -w @ (m0 + m1) / 2
    return Xte @ w + b > 0, m0, m1


def make_splits(y, classes, buffer, rng):
    """Indices of the balanced training and test sets of each of the 7 folds.

    The samples of the classes are pooled in time order (claims O7); y holds labels.
    """
    use = np.where(np.isin(y, classes))[0]
    folds, plan = folds_and_buffers(len(use), buffer)
    out = []
    for train, i in plan:
        tr = use[np.concatenate([folds[j] for j in train])]
        te = use[folds[i]]
        out.append((balance(tr, y, rng), balance(te, y, rng)))
    return out


def cv_two_class(F, y_is1, splits):
    """Fold accuracies and fitted mean differences (class 1 minus class 0, per feature)."""
    accs, diffs, ntest = [], [], []
    for tr, te in splits:
        Xtr, Xte = zscore(F[tr]), zscore(F[te])
        pred, m0, m1 = lda2(Xtr, y_is1[tr], Xte)
        accs.append((pred == y_is1[te]).mean())
        diffs.append(m1 - m0)
        ntest.append(len(te))
    return np.array(accs), diffs, np.array(ntest)
EOF
date -u
```

```
Tue Nov 10 04:37:59 UTC 2026
```

**Agent calls Bash**

```bash
cat >> entries/alasfour-2024/ajile.py <<'EOF'


def run_two_class(S, rois, feature="a", buffer="a", seed=0, classes=("Talk", "TV")):
    """Talking against watching TV for every ROI and band of one participant.

    S: samples (build_samples) restricted to the analysed channels; rois: ROI -> positions.
    feature "a": the electrodes of an ROI are its features, and the mean difference of the ROI
    is the mean over its electrodes; "b": one feature, the mean envelope of the ROI's
    electrodes (claims O6). Returns one row per ROI, band and fold.
    """
    rng = np.random.default_rng(seed)
    y = S["cls"]
    splits = make_splits(y, list(classes), buffer, rng)
    is1 = y == classes[0]
    rows = []
    for roi, pos in rois.items():
        for bi, band in enumerate(BAND_NAMES):
            F = S["X"][:, pos, bi].astype(np.float64)
            if feature == "b":
                F = F.mean(1, keepdims=True)
            accs, diffs, ntest = cv_two_class(F, is1, splits)
            for k in range(len(accs)):
                rows.append(
                    dict(roi=roi, band=band, fold=k, acc=accs[k], meandiff=float(np.mean(diffs[k])), ntest=ntest[k])
                )
    return pd.DataFrame(rows)


def add_chance(df, c=2):
    """Finite chance level per fold for alpha 0.05 and 0.01 (claims O9 (i))."""
    for a in (0.05, 0.01):
        df[f"chance_fold_{a}"] = [finite_chance(int(n), c, a) for n in df.ntest]
    return df


def group_tests(df, alpha_chance=0.05, chance_n="fold", fdr=0.01):
    """Participant-wide accuracy and mean-difference tests per feature (claims M6, M8, O9).

    chance_n "fold": a chance level per fold and a t-test of accuracy minus chance; "total":
    one chance level per participant from all its test samples.
    """
    d = df.copy()
    if chance_n == "fold":
        d["chance"] = d[f"chance_fold_{alpha_chance}"]
    else:
        tot = d.groupby(["participant", "roi", "band"]).ntest.transform("sum")
        d["chance"] = [finite_chance(int(n), 2, alpha_chance) for n in tot]
    rows = []
    for (roi, band), g in d.groupby(["roi", "band"]):
        ex = g.acc - g.chance
        t, p = stats.ttest_1samp(ex, 0.0)
        t2, p2 = stats.ttest_1samp(g.meandiff, 0.0)
        ci = stats.t.interval(0.95, len(g) - 1, loc=g.meandiff.mean(), scale=stats.sem(g.meandiff))
        rows.append(
            dict(
                roi=roi, band=band, n=len(g), acc=g.acc.mean(), chance=g.chance.mean(), t_acc=t, p_acc=p,
                meandiff=g.meandiff.mean(), md_lo=ci[0], md_hi=ci[1], t_md=t2, p_md=p2,
            )
        )
    r = pd.DataFrame(rows)
    r["sig_acc"] = bh_fdr(r.p_acc, fdr) & (r.acc > r.chance)
    r["sig_md"] = bh_fdr(r.p_md, fdr)
    r["consistent"] = r.sig_acc & r.sig_md
    return r
EOF
. $TMPDIR/env/bin/activate; cat > $TMPDIR/dev.py <<'EOF'
import pickle, numpy as np, pandas as pd, sys, time
sys.path.insert(0,'entries/alasfour-2024')
import ajile as A
pd.set_option('display.width',200)
D=pickle.load(open('/tmp/claude-1001/feats.pkl','rb')); meta=D['meta']
files,_=A.figshare_files(); cen=A.load_centroids(files)
proj={p:A.load_projection(p,files) for p in A.PARTICIPANTS}
def days_of(p):
    out=[]
    t00=None
    for k,(aid,ch,b),r in zip(D['keys'],D['jobs'],D['res']):
        pass
    items=sorted([(k[1],j,r) for k,j,r in zip(D['keys'],D['jobs'],D['res']) if k[0]==p])
    ch=D['chans'][p]
    for ses,(aid,c,b),r in items:
        m,el,ep=meta[(p,ses)]
        t0=pd.Timestamp(m['session_start']).timestamp()
        good=el.good.values[ch]
        out.append((ses,t0,good,b,r))
    return out
t=time.time()
allrows=[]
for p in A.PARTICIPANTS:
    days=days_of(p); ch=D['chans'][p]
    inter=np.all([meta[(p,d[0])][1].good.values[ch] for d in days],axis=0)
    S=A.build_samples(days,('a',0))
    print(p, S['blocks'].status.value_counts().to_dict(), S['X'].shape, pd.Series(S['cls']).value_counts().to_dict())
    S['X']=S['X'][:,inter,:]; chs=ch[inter]
    dens,W=proj[p]; el=meta[(p,days[0][0])][1]
    asg=A.roi_assignment(dens,W,el[['x','y','z']].values,cen,'c')
    rois=A.roi_channels(asg,dens,chs,'ii')
    print('  rois',{r:len(v) for r,v in rois.items()})
    df=A.run_two_class(S,rois,'a','a',seed=int(p))
    df['participant']=p; allrows.append(df)
df=A.add_chance(pd.concat(allrows))
print('time',time.time()-t)
G=A.group_tests(df)
print(G.pivot(index='band',columns='roi',values='acc').round(3))
print(G.pivot(index='band',columns='roi',values='sig_acc'))
print(G.pivot(index='band',columns='roi',values='meandiff').round(3))
print(G.pivot(index='band',columns='roi',values='consistent'))
print(df.groupby('participant').acc.mean(), df.groupby('participant').ntest.mean(), df.chance_fold_0.05.mean())
df.to_pickle('/tmp/claude-1001/main.pkl')
EOF
python $TMPDIR/dev.py
```

```
Exit code 1
  File "/tmp/claude-1001/dev.py", line 42
    print(df.groupby('participant').acc.mean(), df.groupby('participant').ntest.mean(), df.chance_fold_0.05.mean())
                                                                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; sed -i "s/df.chance_fold_0.05.mean()/df['chance_fold_0.05'].mean()/" $TMPDIR/dev.py; python $TMPDIR/dev.py
```

```
Exit code 1
01 {'artifact': 680, 'kept': 277, 'outside recording': 223} (3147, 91, 5) {'TV': 1666, 'Talk': 868, 'Electronics': 613}
  rois {'Precentral': 5, 'Frontal_Mid': 3, 'Postcentral': 6, 'SupraMarginal': 4, 'Temporal_Sup': 5, 'Temporal_Mid': 10, 'Temporal_Inf': 12}
Traceback (most recent call last):
  File "/tmp/claude-1001/dev.py", line 33, in <module>
    df=A.run_two_class(S,rois,'a','a',seed=int(p))
  File "entries/alasfour-2024/ajile.py", line 735, in run_two_class
    accs, diffs, ntest = cv_two_class(F, is1, splits)
                         ~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "entries/alasfour-2024/ajile.py", line 710, in cv_two_class
    pred, m0, m1 = lda2(Xtr, y_is1[tr], Xte)
                   ~~~~^^^^^^^^^^^^^^^^^^^^^
  File "entries/alasfour-2024/ajile.py", line 685, in lda2
    w = np.linalg.lstsq(S, m1 - m0, rcond=None)[0]
        ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/env/lib/python3.13/site-packages/numpy/linalg/_linalg.py", line 2556, in lstsq
    x, resids, rank, s = _umath_linalg.lstsq(a, b, rcond,
                         ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
                                             signature=signature)
                                             ^^^^^^^^^^^^^^^^^^^^
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cd $TMPDIR; python - <<'EOF'
import pickle, numpy as np, pandas as pd
D=pickle.load(open('feats.pkl','rb')); meta=D['meta']
for k,(aid,ch,b),r in zip(D['keys'],D['jobs'],D['res']):
    m=meta[k][0]
    nnone=sum(x is None for x in r)
    nan=[np.isnan(x['feats']).any() for x in r if x is not None]
    ma=b.stop.max(); 
    print(k, len(b), 'none',nnone, 'nan blocks',sum(nan), 'rec end h %.2f'%(m['shape'][0]/500/3600), 'last stop h %.2f'%(ma/3600))
EOF
```

```
('01', 4) 348 none 0 nan blocks 4 rec end h 24.00 last stop h 23.35
('01', 7) 346 none 223 nan blocks 2 rec end h 15.48 last stop h 23.99
('05', 7) 241 none 0 nan blocks 0 rec end h 24.00 last stop h 23.53
('01', 5) 273 none 0 nan blocks 17 rec end h 24.00 last stop h 22.31
('05', 4) 232 none 0 nan blocks 0 rec end h 24.00 last stop h 22.13
('04', 7) 268 none 0 nan blocks 22 rec end h 24.00 last stop h 23.82
('02', 6) 235 none 0 nan blocks 6 rec end h 24.00 last stop h 22.26
('01', 3) 213 none 0 nan blocks 7 rec end h 24.00 last stop h 21.06
('04', 6) 215 none 0 nan blocks 25 rec end h 24.00 last stop h 23.97
('04', 5) 205 none 0 nan blocks 18 rec end h 24.00 last stop h 22.85
('04', 4) 203 none 0 nan blocks 10 rec end h 24.00 last stop h 23.49
('05', 3) 89 none 0 nan blocks 1 rec end h 24.00 last stop h 20.42
('02', 5) 107 none 0 nan blocks 4 rec end h 24.00 last stop h 21.95
('04', 3) 97 none 77 nan blocks 0 rec end h 15.65 last stop h 23.98
('02', 4) 80 none 0 nan blocks 6 rec end h 24.00 last stop h 23.68
('08', 5) 64 none 0 nan blocks 1 rec end h 24.00 last stop h 21.21
('08', 4) 61 none 0 nan blocks 1 rec end h 24.00 last stop h 21.99
('08', 3) 59 none 0 nan blocks 0 rec end h 24.00 last stop h 23.65
('02', 3) 61 none 0 nan blocks 1 rec end h 24.00 last stop h 22.03
('08', 6) 43 none 0 nan blocks 1 rec end h 24.00 last stop h 23.08
[... 2 more lines not kept]
```

**Agent**

Finding: in `sub-01_ses-7` and `sub-04_ses-3` the ECoG lasts 15.5 h but the epochs run to 24 h (223 and 77 labelled blocks past the end). Checking whether the epochs are offset in time.

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cd $TMPDIR; python - <<'EOF'
import pickle, numpy as np, pandas as pd
D=pickle.load(open('feats.pkl','rb')); meta=D['meta']
for k in [('01',7),('04',3),('01',5)]:
    m,el,ep=meta[k]
    print(k, m['session_start'], m['shape'][0]/500/3600)
    e=ep.copy(); e['h']=e.start/3600
    brk=e[e.label.str.startswith('Blocklist (Data')]
    print('  first epochs:'); print(e.head(4).to_string())
    print('  data-break total h %.2f, first-non-break start h %.2f'%(((brk.stop-brk.start).sum()/3600), e[~e.label.str.startswith('Blocklist (Data')].h.min()))
    big=brk[(brk.stop-brk.start)>600]; print('  long breaks (h):', [(round(a/3600,2),round(b/3600,2)) for a,b in zip(big.start,big.stop)])
EOF
```

```
('01', 7) 2000-01-07T03:31:22.414000-05:00 15.477107222222223
  first epochs:
                    label         start          stop         h
0  Blocklist (Data break)      0.000000  30694.366667  0.000000
1                     Eat  30694.366667  30815.533333  8.526213
2               Eat, Talk  30815.533333  30937.733333  8.559870
3  Blocklist (Data break)  30937.733333  30937.800000  8.593815
  data-break total h 8.55, first-non-break start h 8.53
  long breaks (h): [(0.0, 8.53)]
('04', 3) 2000-01-03T03:20:48.322000-05:00 15.65324388888889
  first epochs:
                          label         start          stop          h
0        Blocklist (Data break)      0.000000  49079.800000   0.000000
1  Blocklist (Camera move/zoom)  49079.800000  49201.233333  13.633278
2        Blocklist (Data break)  49201.233333  49222.266667  13.667009
3                Computer/phone  49222.266667  49359.733333  13.672852
  data-break total h 18.81, first-non-break start h 13.63
  long breaks (h): [(0.0, 13.63), (13.84, 14.02), (14.22, 14.41), (14.57, 14.76), (14.96, 15.14), (15.31, 15.49), (15.69, 15.87), (16.04, 16.22), (16.42, 16.61), (16.77, 16.96), (17.16, 17.34), (17.51, 17.69), (17.89, 18.08), (18.24, 18.43), (18.63, 18.81), (18.98, 19.16), (19.36, 19.54), (19.72, 19.9), (20.09, 20.28), (20.44, 20.63), (20.83, 21.01), (21.18, 21.36), (21.56, 21.75), (21.91, 22.1), (22.3, 22.48), (22.65, 22.83), (23.03, 23.21), (23.38, 23.56), (23.76, 23.95)]
('01', 5) 2000-01-04T19:00:00-05:00 24.0
  first epochs:
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/alasfour-2024; python3 - <<'EOF'
s=open('ajile.py').read()
old='def extract_day(asset_id, channels, blocks, sds, threads=48, window=6, log=None):'
new='def extract_day(asset_id, channels, blocks, sds, threads=48, window=6, offset=0.0):'
assert old in s; s=s.replace(old,new)
old="""    for b in blocks.itertuples():
        i0 = int(round(b.start * FS))
        i1 = int(round(b.stop * FS))"""
new="""    for b in blocks.itertuples():
        i0 = int(round((b.start - offset) * FS))
        i1 = int(round((b.stop - offset) * FS))"""
assert old in s; s=s.replace(old,new)
old="""def _extract_job(job):
    asset_id, channels, blocks, sds = job
    t = time.time()
    out, nbytes = extract_day(asset_id, channels, blocks, sds)"""
new="""def epoch_offset(meta):
    \"\"\"Seconds from the epochs' clock to the ElectricalSeries' clock.

    In most files both start at 19:00 and the offset is 0. In two files (sub-01 ses-7,
    sub-04 ses-3) the session, and the ECoG, start later in the night while the epochs
    still start at 19:00, with a data break up to the start of the ECoG; the offset is the
    session start minus 19:00. This is found from the data (see the notebook's data check).
    \"\"\"
    t = pd.Timestamp(meta["session_start"])
    ref = t.normalize() + pd.Timedelta(hours=19)
    if ref > t:
        ref -= pd.Timedelta(days=1)
    return (t - ref).total_seconds()


def _extract_job(job):
    asset_id, channels, blocks, sds, offset = job
    t = time.time()
    out, nbytes = extract_day(asset_id, channels, blocks, sds, offset=offset)"""
assert old in s; s=s.replace(old,new)
open('ajile.py','w').write(s)
EOF
cd $TMPDIR; python3 - <<'EOF'
s=open('full.py').read()
s=s.replace("jobs.append((aid,ch,b,[sdd[i],pooled])); keys.append((p,d))","jobs.append((aid,ch,b,[sdd[i],pooled],A.epoch_offset(meta[(p,d)][0]))); print(p,d,A.epoch_offset(meta[(p,d)][0])); keys.append((p,d))")
s=s.replace("jobs=[(j[0],j[1],j[2]) for j in jobs]","jobs=[(j[0],j[1],j[2],j[4]) for j in jobs]")
open('full.py','w').write(s)
EOF
rm -f $TMPDIR/job_01_7.pkl $TMPDIR/job_04_3.pkl; . $TMPDIR/env/bin/activate; python full.py 2 2>&1 | grep -v "^0[1-8] [0-9] 0.0$" | tail; date -u
```

```
survey 41.30945587158203
01 7 30682.414
04 3 30048.322
('04', 3) 65
('01', 7) 170
done 212.4551899433136 89.067114069 GB [370, 170, 301, 303, 286, 274, 235, 235, 217, 197, 204, 120, 112, 65, 93, 87, 83, 77, 58, 49, 36]
0.353212 1.306628
Tue Nov 10 04:42:51 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> entries/alasfour-2024/ajile.py <<'EOF'


def restrict(S, mask):
    """Keep the channels in mask and drop samples with a missing value in any of them."""
    X = S["X"][:, mask, :]
    ok = ~np.isnan(X).any(axis=(1, 2))
    out = {k: (v[ok] if isinstance(v, np.ndarray) and len(v) == len(ok) else v) for k, v in S.items()}
    out["X"] = X[ok]
    out["n_nan_dropped"] = int((~ok).sum())
    return out
EOF
. $TMPDIR/env/bin/activate; cd $TMPDIR; python3 - <<'EOF'
s=open('dev.py').read()
s=s.replace("for ses,(aid,c,b),r in items:","for ses,(aid,c,b,off),r in items:")
s=s.replace("    S['X']=S['X'][:,inter,:]; chs=ch[inter]","    S=A.restrict(S,inter); chs=ch[inter]; print('  nan dropped',S['n_nan_dropped'])")
open('dev.py','w').write(s)
EOF
python dev.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dev.py", line 24, in <module>
    days=days_of(p); ch=D['chans'][p]
  File "/tmp/claude-1001/dev.py", line 11, in days_of
    for k,(aid,ch,b),r in zip(D['keys'],D['jobs'],D['res']):
          ^^^^^^^^^^
ValueError: too many values to unpack (expected 3)
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cd $TMPDIR; python3 - <<'EOF'
s=open('dev.py').read()
s=s.replace("""    for k,(aid,ch,b),r in zip(D['keys'],D['jobs'],D['res']):
        pass
""","")
open('dev.py','w').write(s)
EOF
python dev.py
```

```
01 {'artifact': 877, 'kept': 303} (3445, 91, 5) {'TV': 1863, 'Talk': 980, 'Electronics': 602}
  nan dropped 312
  rois {'Precentral': 5, 'Frontal_Mid': 3, 'Postcentral': 6, 'SupraMarginal': 4, 'Temporal_Sup': 5, 'Temporal_Mid': 10, 'Temporal_Inf': 12}
02 {'kept': 307, 'artifact': 176} (3499, 85, 5) {'Talk': 1654, 'TV': 1443, 'Electronics': 402}
  nan dropped 182
  rois {'Postcentral': 1, 'Parietal_Inf': 6, 'SupraMarginal': 5, 'Temporal_Sup': 3, 'Temporal_Mid': 21, 'Temporal_Inf': 12}
04 {'kept': 677, 'artifact': 311} (7296, 83, 5) {'Talk': 4579, 'TV': 1660, 'Electronics': 1057}
  nan dropped 871
  rois {'Precentral': 6, 'Frontal_Mid': 10, 'Postcentral': 8, 'SupraMarginal': 1, 'Temporal_Sup': 3, 'Temporal_Mid': 4, 'Temporal_Inf': 7}
05 {'kept': 341, 'artifact': 221} (3892, 105, 5) {'TV': 1699, 'Talk': 1556, 'Electronics': 637}
  nan dropped 11
  rois {'Precentral': 4, 'Frontal_Mid': 2, 'Postcentral': 13, 'Parietal_Inf': 6, 'SupraMarginal': 5, 'Temporal_Sup': 3, 'Temporal_Mid': 14, 'Temporal_Inf': 11}
08 {'kept': 236, 'artifact': 16} (2779, 91, 5) {'Talk': 1502, 'TV': 1066, 'Electronics': 211}
  nan dropped 73
  rois {'Precentral': 3, 'Frontal_Mid': 4, 'Postcentral': 8, 'SupraMarginal': 4, 'Temporal_Sup': 2, 'Temporal_Mid': 10, 'Temporal_Inf': 6}
time 0.6621685028076172
roi         Frontal_Mid  Parietal_Inf  ...  Temporal_Mid  Temporal_Sup
band                                   ...                            
alpha             0.509         0.544  ...         0.552         0.549
beta              0.497         0.547  ...         0.574         0.541
[... 46 more lines not kept]
```

**Agent**

Pipeline works (accuracies 53–60%, finite chance ≈ 0.56 at α 0.05). Checking whether the archive's asset metadata has sex and age for Table 1.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000055/versions/0.220127.0436/assets/7de9b149-2994-455e-a8c6-5e5893245baf/" | python3 -c "
import json,sys; d=json.load(sys.stdin); print(json.dumps(d.get('wasAttributedTo'),indent=0)[:800]); print(d.keys())"; curl -s "https://api.dandiarchive.org/api/dandisets/000055/versions/0.220127.0436/" | python3 -c "
import json,sys; d=json.load(sys.stdin); print(d['description'][:1500]); print(d.get('relatedResource')); print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent**

No sex or age in the dataset. Now writing the notebook (generated from a script so I can develop its cells on the cached features).

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/cells.py",
 "content": "# Cells of the notebook. Each cell starts with a line \"# %% [markdown]\" or \"# %% tags=...\" .\n# %% [markdown]\n# # Alasfour and Gilja (2024) on AJILE12 (DANDI:000055)\n#\n# Paper: A. Alasfour and V. Gilja, \"Consistent spectro-spatial features of human ECoG successfully\n# decode naturalistic behavioral states\", Front. Hum. Neurosci. 18:1388267 (2024),\n# doi:10.3389/fnhum.2024.1388267. The claims file (`claims/alasfour-2024.yaml`) was written from the\n# version of record (PMC11169785); the paper has no supplement and links no code.\n#\n# Dataset: DANDI:000055 (AJILE12), version **0.220127.0436**, streamed from the archive. The paper\n# cites no version; this is the only published version (the draft has the same 55 assets and size),\n# so it is pinned.\n#\n# Outside input: the electrode-to-ROI projection matrices of Peterson et al. (2021a), Figshare item\n# doi:10.6084/m9.figshare.12114408.v1, which the claims file names for every claim on regions\n# (`data: with_inputs`).\n#\n# | Claim | Tested here |\n# |---|---|\n# | roi-projection-link (link claim added by the author) | tested |\n# | cohort-selection | tested |\n# | table1-participants | tested |\n# | fig2-highest-accuracy, fig2-rois-three-bands, fig2-inferior-temporal-all-bands, fig2-beta-temporal-only, fig2-single-band-rois | tested |\n# | anova-roi-band-effects, anova-no-interaction | tested |\n# | posthoc-band-averages, posthoc-roi-averages | tested |\n# | fig3-three-class | tested |\n# | fig4-not-single-participant, fig4-missing-rois, fig4-participant2-high | tested |\n# | fig5-gamma-higher-talking, fig5-theta-alpha-lower-talking, fig5-pre-postcentral, fig5-parietal-temporal-no-gamma, fig5-middle-temporal-tv | tested |\n# | inferior-temporal-high-gamma-inconsistent, all-rois-but-inferior-parietal | tested |\n# | fig6-sign-consistency, fig6-examples | tested |\n# | fig7-non-additive, fig7-participant4-low-gamma, fig7-above-70, discussion-above-80, fig7-exceeds-group, fig7-best-band-varies | tested |\n#\n# Readings. The claims file names readings for details the paper leaves open (O1 to O16). Every\n# analysis is run under a grid of them: artifact rule O4 (a, b) by SD (i, ii); ROI assignment O5\n# (a, b, and c, a reading taken from Methods 2.1, see the helper) by density rule (i, ii); ROI feature\n# O6 (a, b); buffer O7 (a, b); chance level O9, alpha (0.05, 0.01) by n (per fold, per participant).\n# The main reading, the one the paper best supports in this attempt's judgement, is O4 (a)(ii),\n# O5 (c)(ii), O6 (a), O7 (a), O9 alpha 0.05 per fold. Each claim's section prints the main reading's\n# result and how many readings of the grid meet the criterion.\n\n# %% tags=[\"setup\"]\nimport os\nimport time\n\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"OPENBLAS_NUM_THREADS\", \"1\")\nimport itertools\nimport resource\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport statsmodels.formula.api as smf\nfrom statsmodels.stats.anova import anova_lm\nfrom statsmodels.stats.multicomp import pairwise_tukeyhsd\nfrom sklearn.discriminant_analysis import LinearDiscriminantAnalysis\n\nimport ajile as A\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\nT0 = time.time()\nP = A.PARTICIPANTS\nSHORT = {r: A.ROI_NAMES[r] for r in A.ROIS}\n\n# %% [markdown]\n# ## Survey of the dataset\n#\n# Every asset of the pinned version, and the metadata (epochs, electrodes, series attributes) of every\n# file; no signal data are read here.\n\n# %% tags=[\"survey\"]\nassets = A.list_assets()\nprint(len(assets), \"assets,\", assets.subject.nunique(), \"subjects,\", round(assets[\"size\"].sum() / 1e9, 1), \"GB\")\nprint(assets.groupby(\"subject\").session.apply(list).to_string())\nMETA = A.survey(assets)\nm0, el0, ep0 = META[(\"08\", 3)]\nprint(\"ElectricalSeries:\", m0[\"shape\"], \"chunks\", m0[\"chunks\"], \"rate\", m0[\"rate\"], \"unit\", m0[\"unit\"], \"conversion\", m0[\"conversion\"])\nprint(\"electrodes columns:\", list(el0.columns))\nprint(\"epochs columns: labels, start_time, stop_time; labels seen:\")\nlabs = pd.concat([META[k][2].label for k in META]).value_counts()\nprint(labs.to_string())\n\n# %% [markdown]\n# ## Feature extraction\n#\n# For the five participants of Table 1, every block labelled with exactly one of Talk, TV or\n# Computer/phone is streamed (only the chunks covering the block, plus 5 s each side, and only the\n# electrodes good on at least one day), filtered into the five bands, enveloped, and averaged into\n# 10-s bins. The artifact statistics of each block are kept for every reading of the artifact rule.\n# The epochs of two files are on a clock 8.5 h and 8.3 h ahead of the ECoG (data check below); the\n# offset is applied here.\n\n# %% tags=[\"extract\"]\nCH, JOBS, KEYS = {}, [], []\nfor p in P:\n    days = sorted(s for (q, s) in META if q == p)\n    good = np.zeros(len(META[(p, days[0])][1]), bool)\n    for d in days:\n        good |= META[(p, d)][1].good.values\n    ch = np.where(good)[0]\n    CH[p] = ch\n    nsamp = np.array([META[(p, d)][0][\"shape\"][0] for d in days])\n    sdd = np.array([META[(p, d)][1].standard_deviation.values[ch] for d in days])\n    pooled = np.sqrt((nsamp[:, None] * sdd**2).sum(0) / nsamp.sum())\n    for i, d in enumerate(days):\n        b = A.class_blocks(META[(p, d)][2])\n        aid = assets[(assets.subject == p) & (assets.session == d)].asset_id.iloc[0]\n        JOBS.append((aid, ch, b, [sdd[i], pooled], A.epoch_offset(META[(p, d)][0])))\n        KEYS.append((p, d))\norder = np.argsort([-len(j[2]) * len(j[1]) for j in JOBS])\nJOBS = [JOBS[i] for i in order]\nKEYS = [KEYS[i] for i in order]\nt = time.time()\nRES = A.extract_participant_days(JOBS, procs=4)\nprint(\"extracted\", sum(len(j[2]) for j in JOBS), \"blocks from\", len(JOBS), \"files,\",\n      round(sum(r[1] for r in RES) / 1e9, 1), \"GB read, in\", round((time.time() - t) / 60, 1), \"min\")\n\n# %% tags=[\"days\"]\nDAYS = {p: [] for p in P}\nfor (p, d), job, r in sorted(zip(KEYS, JOBS, RES), key=lambda z: z[0]):\n    m, el, ep = META[(p, d)]\n    t0 = pd.Timestamp(m[\"session_start\"]).timestamp() - A.epoch_offset(m)\n    DAYS[p].append((d, t0, el.good.values[CH[p]], job[2], r[0]))\nprint({p: [d[0] for d in DAYS[p]] for p in P})\n\n# %% [markdown]\n# ## Data check\n\n# %% tags=[\"sanity\"]\nprint(\"Per file: duration of the ECoG, epochs' last stop, offset applied, class blocks, blocks outside the ECoG\")\nrows = []\nfor p in P:\n    for d, t0, good, blocks, res in DAYS[p]:\n        m = META[(p, d)][0]\n        rows.append(dict(participant=p, session=d, ecog_h=m[\"shape\"][0] / m[\"rate\"] / 3600,\n                         epochs_end_h=META[(p, d)][2].stop.max() / 3600, offset_h=A.epoch_offset(m) / 3600,\n                         start=m[\"session_start\"], blocks=len(blocks), outside=sum(r is None for r in res),\n                         good=int(good.sum()), channels_read=len(good)))\nFILES = pd.DataFrame(rows)\nprint(FILES.round(3).to_string())\nprint(\"ECoG duration + offset, h: min %.3f, max %.3f\" % ((FILES.ecog_h + FILES.offset_h).min(), (FILES.ecog_h + FILES.offset_h).max()))\nfor k in [(\"01\", 7), (\"04\", 3)]:\n    ep = META[k][2]\n    first = ep[~ep.label.str.startswith(\"Blocklist (Data\")].start.min()\n    print(k, \"first epoch that is not a data break starts at %.1f s; offset %.1f s; ECoG starts at 0 s of its own clock\"\n          % (first, A.epoch_offset(META[k][0])))\nprint()\nprint(\"Units: ElectricalSeries stored in\", m0[\"unit\"], \"with conversion\", m0[\"conversion\"], \"-> values are microvolts\")\nprint(\"Sampling rate (all files):\", sorted({META[k][0][\"rate\"] for k in META}))\nprint(\"Block durations, s:\", end=\" \")\ndur = pd.concat([b.stop - b.start for p in P for _, _, _, b, _ in DAYS[p]])\nprint(\"min %.1f, median %.1f, max %.1f, n %d\" % (dur.min(), dur.median(), dur.max(), len(dur)))\nprint()\nprint(\"SD column of the electrodes table against the RMS of the class blocks (median ratio RMS / SD per file):\")\nfor p in P:\n    rr = []\n    for d, t0, good, blocks, res in DAYS[p]:\n        ss = sum(r[\"sumsq\"] for r in res if r is not None)\n        nn = sum(r[\"n\"] for r in res if r is not None)\n        sd = META[(p, d)][1].standard_deviation.values[CH[p]]\n        rr.append(np.nanmedian(np.sqrt(ss / nn)[good] / sd[good]))\n    print(\" \", p, np.round(rr, 2))\nprint()\nprint(\"Envelope check against sosfiltfilt + scipy.signal.hilbert on one block and channel:\")\nr0 = DAYS[\"08\"][0]\naid = assets[(assets.subject == \"08\") & (assets.session == 3)].asset_id.iloc[0]\nf, _ = A.open_nwb(aid)\nb = r0[3].iloc[0]\ni0, i1 = int(round(b.start * 500)), int(round(b.stop * 500))\nx = f[\"acquisition/ElectricalSeries/data\"][max(0, i0 - 2500): i1 + 2500, CH[\"08\"][0]].astype(float)\nx = x - np.median(x)\no = i0 - max(0, i0 - 2500)\nfor bi, ref in enumerate(A.envelope_check(x)):\n    rb = np.array([ref[o + k * 5000: o + (k + 1) * 5000].mean() for k in range(r0[4][0][\"feats\"].shape[0])])\n    ours = r0[4][0][\"feats\"][:, 0, bi]\n    print(\"  %-10s max relative difference over %d bins: %.4f (values %.2f to %.2f uV)\"\n          % (A.BAND_NAMES[bi], len(rb), np.max(np.abs(ours - rb) / rb), rb.min(), rb.max()))\nf.close()\n\n# %% [markdown]\n# ### Readings and samples\n#\n# The analysed channels are the electrodes good on every day of the participant (an assumption: the\n# paper gives one count per participant, and a fixed channel set is needed across days). Samples are\n# the 10-s bins of kept blocks, in time order; a bin with a missing value in an analysed channel is\n# dropped.\n\n# %% tags=[\"samples\"]\nFILES_FIG = A.figshare_files()[0]\nCEN = A.load_centroids(FILES_FIG)\nPROJ = {p: A.load_projection(p, FILES_FIG) for p in P}\nART = {\"a-ii\": (\"a\", 0), \"b-ii\": (\"b\", 0), \"a-i\": (\"a\", 1), \"b-i\": (\"b\", 1)}\nSAMPLES = {}\nfor an, ar in ART.items():\n    for p in P:\n        inter = np.all([g for _, _, g, _, _ in DAYS[p]], axis=0)\n        S = A.build_samples(DAYS[p], ar)\n        SAMPLES[(an, p)] = A.restrict(S, inter)\n        SAMPLES[(an, p)][\"channels\"] = CH[p][inter]\nrows = []\nfor (an, p), S in SAMPLES.items():\n    st = S[\"blocks\"].status.value_counts()\n    c = pd.Series(S[\"cls\"]).value_counts()\n    rows.append(dict(artifact=an, participant=p, channels=len(S[\"channels\"]), blocks_kept=st.get(\"kept\", 0),\n                     blocks_artifact=st.get(\"artifact\", 0), blocks_outside=st.get(\"outside recording\", 0),\n                     bins_nan_dropped=S[\"n_nan_dropped\"], Talk=c.get(\"Talk\", 0), TV=c.get(\"TV\", 0),\n                     Electronics=c.get(\"Electronics\", 0)))\nprint(pd.DataFrame(rows).to_string())\n\n\ndef roi_sets(p, o5, dens_r, channels):\n    dens, W = PROJ[p]\n    el = META[(p, DAYS[p][0][0])][1]\n    asg = A.roi_assignment(dens, W, el[[\"x\", \"y\", \"z\"]].values, CEN, o5)\n    return A.roi_channels(asg, dens, channels, dens_r)\n\n\nGRID = list(itertools.product(ART, [\"c\", \"a\", \"b\"], [\"ii\", \"i\"], [\"a\", \"b\"], [\"a\", \"b\"]))\nMAIN = (\"a-ii\", \"c\", \"ii\", \"a\", \"a\")\nCHANCES = [(0.05, \"fold\"), (0.01, \"fold\"), (0.05, \"total\"), (0.01, \"total\")]\nt = time.time()\nFOLDS = {}\nfor g in GRID:\n    an, o5, dr, o6, o7 = g\n    parts = []\n    for p in P:\n        S = SAMPLES[(an, p)]\n        rois = roi_sets(p, o5, dr, S[\"channels\"])\n        df = A.run_two_class(S, rois, o6, o7, seed=1000 + int(p))\n        df[\"participant\"] = p\n        parts.append(df)\n    FOLDS[g] = A.add_chance(pd.concat(parts, ignore_index=True))\nGROUP = {(g, ch): A.group_tests(FOLDS[g], ch[0], ch[1]) for g in GRID for ch in CHANCES}\nprint(len(GRID), \"pipelines,\", len(GROUP), \"readings with the chance levels;\", round(time.time() - t), \"s\")\nprint(\"Main reading:\", MAIN)\nprint(\"ROIs per participant under the main reading (electrodes):\")\nfor p in P:\n    S = SAMPLES[(\"a-ii\", p)]\n    print(\" \", p, {SHORT[r]: len(v) for r, v in roi_sets(p, \"c\", \"ii\", S[\"channels\"]).items()})\n\n\ndef readings_meeting(pred, chance=True):\n    \"\"\"Readings of the grid (and chance levels) under which pred(group table, folds) holds.\"\"\"\n    ok = []\n    for g in GRID:\n        for ch in (CHANCES if chance else CHANCES[:1]):\n            if pred(GROUP[(g, ch)], FOLDS[g]):\n                ok.append((g, ch))\n    return ok\n\n\ndef show_readings(ok, chance=True):\n    n = len(GRID) * (len(CHANCES) if chance else 1)\n    main = (MAIN, CHANCES[0]) in ok\n    print(\"criterion met under the main reading:\", main, \"| readings meeting it: %d of %d\" % (len(ok), n))\n    if ok:\n        df = pd.DataFrame([dict(artifact=g[0], O5=g[1] + \"-\" + g[2], O6=g[3], O7=g[4], alpha=c[0], n=c[1]) for g, c in ok])\n        for col in df.columns:\n            print(\"   \", col, df[col].value_counts().to_dict())\n    return main\n\n\ndef mat(G, col, fmt=None):\n    m = G.pivot(index=\"band\", columns=\"roi\", values=col).reindex(index=A.BAND_NAMES, columns=A.ROIS)\n    m.columns = [SHORT[c] for c in m.columns]\n    return m\n\n\nGM = GROUP[(MAIN, CHANCES[0])]\nFM = FOLDS[MAIN]\n\n# %% [markdown]\n# ### Clock check\n#\n# Decoding Talk against TV with the true labels and with the labels shifted in time (the pooled\n# samples rolled by half their number), under the main reading, high gamma of all ROI electrodes. For\n# the two files with an epoch offset, a classifier trained on the participant's other days is tested\n# on that day, with and without the offset.\n\n# %% tags=[\"clock\"]\nrng = np.random.default_rng(7)\nfor p in P:\n    S = SAMPLES[(\"a-ii\", p)]\n    pos = sorted({i for v in roi_sets(p, \"c\", \"ii\", S[\"channels\"]).values() for i in v})\n    F = S[\"X\"][:, pos, 4].astype(float)\n    y = S[\"cls\"]\n    out = []\n    for shift in [0, len(y) // 2]:\n        ys = np.roll(y, shift)\n        sp = A.make_splits(ys, [\"Talk\", \"TV\"], \"a\", rng)\n        acc, _, nt = A.cv_two_class(F, ys == \"Talk\", sp)\n        out.append(acc.mean())\n    print(\"participant\", p, \"accuracy true labels %.3f, shifted labels %.3f\" % tuple(out))\nfor p, d in [(\"01\", 7), (\"04\", 3)]:\n    S = SAMPLES[(\"a-ii\", p)]\n    pos = sorted({i for v in roi_sets(p, \"c\", \"ii\", S[\"channels\"]).values() for i in v})\n    tr = np.where((S[\"day\"] != d) & np.isin(S[\"cls\"], [\"Talk\", \"TV\"]))[0]\n    te = np.where((S[\"day\"] == d) & np.isin(S[\"cls\"], [\"Talk\", \"TV\"]))[0]\n    tr, te = A.balance(tr, S[\"cls\"], rng), A.balance(te, S[\"cls\"], rng)\n    F = S[\"X\"][:, pos, 4].astype(float)\n    pred, _, _ = A.lda2(A.zscore(F[tr]), S[\"cls\"][tr] == \"Talk\", A.zscore(F[te]))\n    acc = (pred == (S[\"cls\"][te] == \"Talk\")).mean()\n    print(\"participant %s day %d with the offset: tested on %d balanced bins of that day, accuracy %.3f (chance 0.05 level %.3f)\"\n          % (p, d, len(te), acc, A.finite_chance(len(te), 2, 0.05)))\nprint(\"Without the offset, %d and %d of the class blocks of these two files lie past the end of the ECoG.\"\n      % tuple(int(((META[k][2].stop[META[k][2].label.isin(list(A.CLASS_LABELS))]) * 500 > META[k][0][\"shape\"][0]).sum())\n              for k in [(\"01\", 7), (\"04\", 3)]))\n\n# %% [markdown]\n# ## roi-projection-link (link claim)\n#\n# \"The projection matrices of Peterson et al. (2021a), Figshare 10.6084/m9.figshare.12114408.v1, match\n# the dataset's electrodes: one row per electrode, in the order of the electrodes table, and the\n# Gaussian weights agree with the dataset's electrode positions.\" Rows are matched by index. The\n# matrix's own ROI (largest Gaussian value over the left AAL regions, reading O5 c) is compared with\n# the ROI nearest to the dataset's position mirrored to the left hemisphere.\n\n# %% tags=[\"claim:roi-projection-link\"]\nlink = []\nfor p in P:\n    dens, W = PROJ[p]\n    el = META[(p, DAYS[p][0][0])][1]\n    names = np.array(W.columns)\n    L = np.array([c.endswith(\"_L\") for c in names])\n    xyz = el[[\"x\", \"y\", \"z\"]].values.copy()\n    xyz[:, 0] = -np.abs(xyz[:, 0])\n    C = CEN.values[L]\n    dl = dens.values[L].astype(float)\n    n = min(len(W), len(el))\n    g = W.values[:n][:, L] * dl[None]\n    d2 = ((xyz[:n, None, :] - C[None]) ** 2).sum(-1)\n    d2[:, dl <= 0] = np.inf\n    agree = (g.argmax(1) == d2.argmin(1)).mean()\n    ok = (g > 0) & np.isfinite(d2)\n    r = np.corrcoef(np.log(g[ok]), -d2[ok])[0, 1]\n    shifts = {s: (W.values[s:s + len(el)][:, L] * dl).argmax(1) for s in range(len(W) - len(el) + 1)} if len(W) > len(el) else {}\n    sh = {s: round(float((v == d2.argmin(1)[: len(v)]).mean()), 3) for s, v in shifts.items()}\n    a8 = A.roi_assignment(dens, W, el[[\"x\", \"y\", \"z\"]].values, CEN, \"c\")\n    b8 = A.roi_assignment(dens, W, el[[\"x\", \"y\", \"z\"]].values, CEN, \"b\")\n    link.append(dict(participant=p, matrix_rows=len(W), electrodes=len(el), roi_agreement=round(agree, 3),\n                     corr_logweight_negd2=round(r, 3), eight_roi_label_agreement=round(float((a8[a8 >= 0] == b8[a8 >= 0]).mean()), 3),\n                     agreement_by_row_shift=sh))\nprint(pd.DataFrame(link).to_string())\nprint(\"Density row (left hemisphere) of the eight ROIs:\")\nprint(pd.DataFrame({p: PROJ[p][0][[r + \"_L\" for r in A.ROIS]].astype(float).round(2).values for p in P}, index=[SHORT[r] for r in A.ROIS]).to_string())\n\n# %% [markdown]\n# **Result: the link holds in part.** Four of the five matrices have one row per electrode; participant\n# 1's has 98 rows for 94 electrodes, and an index match fits best with no shift. The matrix's own ROI and\n# the ROI nearest to the dataset's mirrored position agree for 51 to 64% of electrodes, so the matrices\n# were not computed from these positions exactly; the region claims are tested with both the\n# matrices (O5 a, c) and the positions (O5 b).\n\n# %% [markdown]\n# ## cohort-selection\n#\n# \"Of the twelve AJILE12 participants, only five (2 male, 3 female) had at least 1 h of recorded neural\n# activity of the behaviours of interest, and these five were analysed.\" Minutes are the summed\n# durations of the epochs labelled Talk or TV over the files (days 3 to 7), with single-label epochs\n# (main) and with any epoch whose label includes the class (variant); before artifact rejection only\n# (the signals of the other seven participants are not read).\n\n# %% tags=[\"claim:cohort-selection\"]\nrows = []\nfor s in sorted(assets.subject.unique()):\n    ks = [k for k in META if k[0] == s]\n    ep = pd.concat([META[k][2] for k in ks])\n    ep[\"dur\"] = (ep.stop - ep.start) / 60\n    r = dict(subject=s, days=len(ks))\n    for c, lab in [(\"Talk\", \"Talk\"), (\"TV\", \"TV\")]:\n        r[c + \"_single\"] = ep[ep.label == lab].dur.sum()\n        r[c + \"_any\"] = ep[ep.label.str.split(\", \").apply(lambda l: lab in l)].dur.sum()\n    rows.append(r)\ncoh = pd.DataFrame(rows).round(1)\nfor lab in [\"single\", \"any\"]:\n    coh[\"each_1h_\" + lab] = (coh[\"Talk_\" + lab] >= 60) & (coh[\"TV_\" + lab] >= 60)\n    coh[\"both_1h_\" + lab] = (coh[\"Talk_\" + lab] + coh[\"TV_\" + lab]) >= 60\nprint(coh.to_string())\nfor c in [c for c in coh.columns if c.startswith((\"each\", \"both\"))]:\n    print(c, \"->\", list(coh.subject[coh[c]]))\nprint(\"Sex and age: the files' subject entries hold only species and subject_id:\", list(META[(\"08\", 3)][0].keys())[:2],\n      \"; the archive's asset metadata lists species only.\")\n\n# %% [markdown]\n# **Result: reproduced.** Under reading O2 (a), at least 1 h of each of talking and watching TV, exactly\n# subjects 01, 02, 04, 05 and 08 qualify, with single-label or any-label epochs; under (b) more\n# subjects qualify. The sex of the participants is not in the dataset, so \"2 male, 3 female\" cannot be\n# checked.\n\n# %% [markdown]\n# ## table1-participants\n#\n# \"Table 1 gives, per participant, sex, age, good electrodes and minutes of talking, watching TV and\n# using electronics; all five have at least 2 h of data for the two states.\"\n\n# %% tags=[\"claim:table1-participants\"]\nT1 = {\"01\": (85, 493, 605, 291), \"02\": (80, 331, 338, 68), \"04\": (67, 696, 312, 181), \"05\": (104, 340, 480, 212), \"08\": (82, 216, 156, 29)}\nrows = []\nfor p in P:\n    goods = [int(g.sum()) for _, _, g, _, _ in DAYS[p]]\n    inter = int(np.all([g for _, _, g, _, _ in DAYS[p]], axis=0).sum())\n    union = len(CH[p])\n    rows.append(dict(participant=p, table1=T1[p][0], day3=goods[0], per_day=goods, min_day=min(goods), all_days=inter, any_day=union))\nel_t = pd.DataFrame(rows)\nprint(\"Good electrodes:\")\nprint(el_t.to_string())\nfor c in [\"day3\", \"min_day\", \"all_days\", \"any_day\"]:\n    print(\"  reading %-8s matches %d of 5\" % (c, (el_t[c] == el_t.table1).sum()))\nrows = []\nfor an in [None] + list(ART):\n    for p in P:\n        if an is None:\n            bl = A.build_samples(DAYS[p], None)[\"blocks\"]\n        else:\n            bl = SAMPLES[(an, p)][\"blocks\"]\n        kept = bl[bl.status == \"kept\"]\n        mins = {c: ((kept.stop - kept.start)[kept.cls == c]).sum() / 60 for c in [\"Talk\", \"TV\", \"Electronics\"]}\n        rows.append(dict(artifact=an or \"none\", participant=p, **{k: round(v, 1) for k, v in mins.items()}))\nmn = pd.DataFrame(rows)\nfor c, i in [(\"Talk\", 1), (\"TV\", 2), (\"Electronics\", 3)]:\n    mn[c + \"_t1\"] = mn.participant.map(lambda p: T1[p][i])\n    mn[c + \"_ok\"] = (mn[c] - mn[c + \"_t1\"]).abs() <= 0.1 * mn[c + \"_t1\"]\nmn[\"n_within_10pct\"] = mn[[\"Talk_ok\", \"TV_ok\", \"Electronics_ok\"]].sum(1)\nmn[\"talk_tv_ge_120\"] = (mn.Talk + mn.TV) >= 120\nprint(\"Minutes per class (single-label blocks inside the ECoG), before and after artifact rejection:\")\nprint(mn.to_string())\nprint(mn.groupby(\"artifact\").agg(within=(\"n_within_10pct\", \"sum\"), all_ge_120=(\"talk_tv_ge_120\", \"all\")).to_string())\n\n# %% [markdown]\n# **Result: partially reproduced.** No reading of the good-electrode count matches all five values of\n# Table 1 (the counts change from day to day), and no artifact reading puts all 15 minute values within\n# 10%; every participant has at least 120 min of talking and watching TV. Sex and age are not in the\n# dataset.\n\n# %% [markdown]\n# ## fig2-highest-accuracy\n#\n# \"Across the 40 ROI and band features, the highest participant-wide classification accuracy of\n# Talking against Watching TV is 69%, for high gamma in the inferior temporal lobe.\" Accuracy of a\n# feature is the mean of its fold accuracies over participants (35 when all five have the ROI).\n\n# %% tags=[\"claim:fig2-highest-accuracy\"]\nprint(\"Main reading, mean fold accuracy (ROI columns, band rows):\")\nprint(mat(GM, \"acc\").round(3).to_string())\nprint(\"folds per feature:\", GM.n.min(), \"to\", GM.n.max())\nprint(\"range of accuracies %.3f to %.3f\" % (GM.acc.min(), GM.acc.max()))\ntop = GM.sort_values(\"acc\", ascending=False).head(3)\nprint(\"top features:\", [(SHORT[r], b, round(a, 3)) for r, b, a in zip(top.roi, top.band, top.acc)])\nrows = []\nfor g in GRID:\n    G = GROUP[(g, CHANCES[0])]\n    best = G.loc[G.acc.idxmax()]\n    it = G[(G.roi == \"Temporal_Inf\") & (G.band == \"high_gamma\")]\n    rows.append(dict(reading=g, best=(SHORT[best.roi], best.band), best_acc=round(best.acc, 3),\n                     it_hg=round(float(it.acc.iloc[0]), 3) if len(it) else np.nan))\nR2 = pd.DataFrame(rows)\nR2[\"it_hg_highest\"] = R2.best.apply(lambda b: b == (\"inferior temporal\", \"high_gamma\"))\nR2[\"within_tol\"] = (R2.it_hg - 0.69).abs() <= 0.069\nprint(R2.to_string())\nprint(\"readings where IT high gamma is highest: %d; within 62.1 to 75.9%%: %d; both: %d of %d\"\n      % (R2.it_hg_highest.sum(), R2.within_tol.sum(), (R2.it_hg_highest & R2.within_tol).sum(), len(R2)))\n\n# %% [markdown]\n# ## Significance of features (Figure 2)\n#\n# Shared by the four claims that follow. Significance: t-test of fold accuracy minus finite chance,\n# BH FDR at 0.01 over the 40 features, mean above chance (M6, O9).\n\n# %% tags=[\"fig2-significance\"]\nprint(\"Main reading, significant features (1) and finite chance level\", round(GM.chance.mean(), 3))\nprint(mat(GM, \"sig_acc\").astype(int).to_string())\nfor ch in CHANCES:\n    G = GROUP[(MAIN, ch)]\n    print(\"main pipeline, chance\", ch, \"significant features:\", int(G.sig_acc.sum()), \"chance level %.3f\" % G.chance.mean())\n\n# %% [markdown]\n# ## fig2-rois-three-bands\n#\n# \"The postcentral gyrus, supramarginal gyrus and superior, middle and inferior temporal lobes each have\n# three or more bands with accuracy significantly above chance.\"\n\n# %% tags=[\"claim:fig2-rois-three-bands\"]\nFIVE = [\"Postcentral\", \"SupraMarginal\", \"Temporal_Sup\", \"Temporal_Mid\", \"Temporal_Inf\"]\n\n\ndef nsig(G):\n    return G[G.sig_acc].groupby(\"roi\").size().reindex(A.ROIS).fillna(0).astype(int)\n\n\nprint(\"main reading, significant bands per ROI:\", {SHORT[k]: v for k, v in nsig(GM).items()})\nok = readings_meeting(lambda G, F: all(nsig(G)[r] >= 3 for r in FIVE))\nmain_ok = show_readings(ok)\nok4 = readings_meeting(lambda G, F: sum(nsig(G)[r] >= 3 for r in FIVE) >= 4)\nprint(\"readings where at least four of the five ROIs have 3 bands:\", len(ok4))\nbest = max(((sum(nsig(GROUP[k])[r] >= 3 for r in FIVE), k) for k in GROUP), key=lambda z: z[0])\nprint(\"largest number of the five ROIs with 3 or more bands over all readings:\", best[0], \"at\", best[1])\n\n# %% [markdown]\n# ## fig2-inferior-temporal-all-bands\n#\n# \"All five bands in the inferior temporal lobe decode significantly above chance.\"\n\n# %% tags=[\"claim:fig2-inferior-temporal-all-bands\"]\nprint(\"main reading, IT significant bands:\", int(nsig(GM)[\"Temporal_Inf\"]))\nprint(\"IT p-values (main):\", GM[GM.roi == \"Temporal_Inf\"].set_index(\"band\").p_acc.round(5).to_dict())\nok = readings_meeting(lambda G, F: nsig(G)[\"Temporal_Inf\"] == 5)\nshow_readings(ok)\nok4 = readings_meeting(lambda G, F: nsig(G)[\"Temporal_Inf\"] >= 4)\nprint(\"readings with at least 4 IT bands significant:\", len(ok4))\nprint(\"distribution of IT significant bands over readings:\", pd.Series([int(nsig(GROUP[k])[\"Temporal_Inf\"]) for k in GROUP]).value_counts().sort_index().to_dict())\n\n# %% [markdown]\n# ## fig2-beta-temporal-only\n#\n# \"Beta decodes above chance only in the middle and inferior temporal lobes.\"\n\n# %% tags=[\"claim:fig2-beta-temporal-only\"]\n\n\ndef beta_sig(G):\n    return sorted(G[(G.band == \"beta\") & G.sig_acc].roi)\n\n\nprint(\"main reading, ROIs with significant beta:\", [SHORT[r] for r in beta_sig(GM)])\nok = readings_meeting(lambda G, F: beta_sig(G) == sorted([\"Temporal_Mid\", \"Temporal_Inf\"]))\nshow_readings(ok)\nokp = readings_meeting(lambda G, F: {\"Temporal_Mid\", \"Temporal_Inf\"} <= set(beta_sig(G)) and len(beta_sig(G)) == 3)\nprint(\"readings with both temporal ROIs and one other:\", len(okp))\nprint(\"distribution of beta-significant ROI sets:\", pd.Series([\", \".join(SHORT[r] for r in beta_sig(GROUP[k])) or \"none\" for k in GROUP]).value_counts().head(8).to_dict())\n\n# %% [markdown]\n# ## fig2-single-band-rois\n#\n# \"The inferior parietal lobe decodes above chance only with high gamma, and the middle frontal lobe\n# only with theta.\"\n\n# %% tags=[\"claim:fig2-single-band-rois\"]\n\n\ndef sig_bands(G, roi):\n    return sorted(G[(G.roi == roi) & G.sig_acc].band)\n\n\nprint(\"main: inferior parietal\", sig_bands(GM, \"Parietal_Inf\"), \"| middle frontal\", sig_bands(GM, \"Frontal_Mid\"))\nprint(\"inferior parietal present in the main reading for\", FM[FM.roi == \"Parietal_Inf\"].participant.unique().tolist())\nok = readings_meeting(lambda G, F: sig_bands(G, \"Parietal_Inf\") == [\"high_gamma\"] and sig_bands(G, \"Frontal_Mid\") == [\"theta\"])\nshow_readings(ok)\nok1 = readings_meeting(lambda G, F: sig_bands(G, \"Parietal_Inf\") == [\"high_gamma\"] or sig_bands(G, \"Frontal_Mid\") == [\"theta\"])\nprint(\"readings where one of the two holds:\", len(ok1))\n\n# %% [markdown]\n# ## anova-roi-band-effects\n#\n# \"In a two-way ANOVA on accuracy, both ROI and band contribute significantly to decodability (p\n# reported as 0 for both).\"\n\n# %% tags=[\"claim:anova-roi-band-effects\"]\n\n\ndef anova(F, typ=2, level=\"fold\"):\n    d = F if level == \"fold\" else F.groupby([\"participant\", \"roi\", \"band\"], as_index=False).acc.mean()\n    m = smf.ols(\"acc ~ C(roi) * C(band)\", data=d).fit()\n    return anova_lm(m, typ=typ)\n\n\nfor lvl in [\"fold\", \"participant\"]:\n    for typ in [2, 1, 3]:\n        a = anova(FM, typ, lvl)\n        print(\"main, %s level, type %d:\" % (lvl, typ), {k: \"F=%.2f p=%.2g\" % (a.loc[k, \"F\"], a.loc[k, \"PR(>F)\"]) for k in a.index if k != \"Residual\" and k != \"Intercept\"})\nrows = []\nfor g in GRID:\n    for lvl in [\"fold\", \"participant\"]:\n        a = anova(FOLDS[g], 2, lvl)\n        rows.append(dict(reading=g, level=lvl, p_roi=a.loc[\"C(roi)\", \"PR(>F)\"], p_band=a.loc[\"C(band)\", \"PR(>F)\"],\n                         p_int=a.loc[\"C(roi):C(band)\", \"PR(>F)\"], F_int=a.loc[\"C(roi):C(band)\", \"F\"]))\nAN = pd.DataFrame(rows)\nAN[\"both_lt_001\"] = (AN.p_roi < 0.001) & (AN.p_band < 0.001)\nprint(\"type II over the grid: both main effects p < 0.001 in %d of %d (fold level %d of %d)\"\n      % (AN.both_lt_001.sum(), len(AN), AN[AN.level == \"fold\"].both_lt_001.sum(), (AN.level == \"fold\").sum()))\nprint(\"p_roi range %.2g to %.2g; p_band range %.2g to %.2g\" % (AN.p_roi.min(), AN.p_roi.max(), AN.p_band.min(), AN.p_band.max()))\n\n# %% [markdown]\n# ## anova-no-interaction\n#\n# \"The interaction between ROI and band has no significant effect on accuracy (p = 0.46).\" Judged on\n# type II sums of squares over the pooled fold accuracies of the main reading.\n\n# %% tags=[\"claim:anova-no-interaction\"]\na = anova(FM, 2, \"fold\")\nprint(\"main, type II, fold accuracies: interaction F = %.3f, df = %d, p = %.3g\" % (a.loc[\"C(roi):C(band)\", \"F\"], a.loc[\"C(roi):C(band)\", \"df\"], a.loc[\"C(roi):C(band)\", \"PR(>F)\"]))\nprint(\"over the grid (type II): interaction p >= 0.05 in %d of %d fold-level readings; p range %.3g to %.3g\"\n      % ((AN[AN.level == \"fold\"].p_int >= 0.05).sum(), (AN.level == \"fold\").sum(), AN[AN.level == \"fold\"].p_int.min(), AN[AN.level == \"fold\"].p_int.max()))\nprint(\"participant level: p >= 0.05 in %d of %d\" % ((AN[AN.level == \"participant\"].p_int >= 0.05).sum(), (AN.level == \"participant\").sum()))\n\n# %% [markdown]\n# ## posthoc-band-averages\n#\n# \"Averaged over ROIs, high gamma has the highest accuracy (63%) and beta the lowest (56%, barely above\n# the finite chance level).\" O11 (a) mean of all fold accuracies of the band; (b) mean of the\n# per-feature means.\n\n# %% tags=[\"claim:posthoc-band-averages\"]\n\n\ndef band_avgs(G, F, how):\n    if how == \"a\":\n        return F.groupby(\"band\").acc.mean()\n    return G.groupby(\"band\").acc.mean()\n\n\nrows = []\nfor g in GRID:\n    for ch in CHANCES:\n        G, F = GROUP[(g, ch)], FOLDS[g]\n        chance = G.chance.mean()\n        for how in \"ab\":\n            b = band_avgs(G, F, how)\n            ok = (abs(b[\"high_gamma\"] - 0.63) <= 0.063 and abs(b[\"beta\"] - 0.56) <= 0.056 and b.idxmax() == \"high_gamma\"\n                  and b.idxmin() == \"beta\" and b[\"beta\"] > chance and (b[\"beta\"] - chance) < (b[\"high_gamma\"] - chance))\n            order_ok = b.idxmax() == \"high_gamma\" and b.idxmin() == \"beta\"\n            rows.append(dict(reading=g, chance=ch, O11=how, hg=b[\"high_gamma\"], beta=b[\"beta\"], top=b.idxmax(), bottom=b.idxmin(), chance_level=chance, ok=ok, order_ok=order_ok))\nBA = pd.DataFrame(rows)\nprint(\"main (O11 a):\", band_avgs(GM, FM, \"a\").round(3).to_dict(), \"chance %.3f\" % GM.chance.mean())\nprint(\"main (O11 b):\", band_avgs(GM, FM, \"b\").round(3).to_dict())\nprint(\"criterion met in %d of %d readings; order (HG top, beta bottom) in %d\" % (BA.ok.sum(), len(BA), BA.order_ok.sum()))\nprint(\"highest band over readings:\", BA.top.value_counts().to_dict(), \"| lowest:\", BA.bottom.value_counts().to_dict())\nprint(\"HG average range %.3f to %.3f; beta %.3f to %.3f\" % (BA.hg.min(), BA.hg.max(), BA.beta.min(), BA.beta.max()))\n\n# %% [markdown]\n# ## posthoc-roi-averages\n#\n# \"Averaged over bands, the inferior temporal lobe has the highest accuracy (66%) and is statistically\n# higher than every other ROI; the middle frontal lobe is lowest (54%).\" Post-hoc tests O12 (a) Tukey\n# HSD at 0.05 on the pooled fold accuracies; (b) pairwise two-sample t-tests, BH FDR at 0.01.\n\n# %% tags=[\"claim:posthoc-roi-averages\"]\n\n\ndef roi_posthoc(F, how):\n    others = [r for r in A.ROIS if r != \"Temporal_Inf\" and r in set(F.roi)]\n    if how == \"a\":\n        tk = pairwise_tukeyhsd(F.acc.values, F.roi.values, alpha=0.05)\n        t = pd.DataFrame(tk.summary().data[1:], columns=tk.summary().data[0])\n        sig = []\n        for r in others:\n            row = t[((t.group1 == r) & (t.group2 == \"Temporal_Inf\")) | ((t.group2 == r) & (t.group1 == \"Temporal_Inf\"))]\n            sig.append(bool(row.reject.iloc[0]))\n        return sig, len(others)\n    ps = [stats.ttest_ind(F[F.roi == \"Temporal_Inf\"].acc, F[F.roi == r].acc).pvalue for r in others]\n    return list(A.bh_fdr(ps, 0.01)), len(others)\n\n\nrows = []\nfor g in GRID:\n    F = FOLDS[g]\n    G = GROUP[(g, CHANCES[0])]\n    for o11 in \"ab\":\n        r = F.groupby(\"roi\").acc.mean() if o11 == \"a\" else G.groupby(\"roi\").acc.mean()\n        for o12 in \"ab\":\n            sig, n = roi_posthoc(F, o12)\n            rows.append(dict(reading=g, O11=o11, O12=o12, it=r.get(\"Temporal_Inf\", np.nan), mf=r.get(\"Frontal_Mid\", np.nan), top=r.idxmax(), bottom=r.idxmin(),\n                             n_sig=sum(sig), n_others=n))\nRA = pd.DataFrame(rows)\nRA[\"order_ok\"] = (RA.top == \"Temporal_Inf\") & (RA.bottom == \"Frontal_Mid\")\nRA[\"ok\"] = RA.order_ok & ((RA.it - 0.66).abs() <= 0.066) & ((RA.mf - 0.54).abs() <= 0.054) & (RA.n_sig == 7)\nprint(\"main:\", FM.groupby(\"roi\").acc.mean().rename(SHORT).round(3).to_dict())\nprint(\"main Tukey: IT higher than %d of %d other ROIs\" % tuple(roi_posthoc(FM, \"a\")[0:1][0].count(True) for _ in [0]) if False else \"\", end=\"\")\ns, n = roi_posthoc(FM, \"a\")\nprint(\"main Tukey: IT significantly different from %d of %d other ROIs; t-tests: %d\" % (sum(s), n, sum(roi_posthoc(FM, \"b\")[0])))\nprint(\"criterion met in %d of %d readings; order holds in %d; IT different from all seven in %d\"\n      % (RA.ok.sum(), len(RA), RA.order_ok.sum(), (RA.n_sig == 7).sum()))\nprint(\"top ROI over readings:\", RA.top.map(SHORT).value_counts().to_dict(), \"| bottom:\", RA.bottom.map(SHORT).value_counts().to_dict())\nprint(\"IT average range %.3f to %.3f; middle frontal %.3f to %.3f\" % (RA.it.min(), RA.it.max(), RA.mf.min(), RA.mf.max()))\n\n# %% [markdown]\n# ## fig3-three-class\n#\n# \"With Using Electronics added as a third class, decoding with all electrodes is above the finite\n# chance level for all four participants with enough data, with high variability; Participant 2 is\n# highest (above 70% in every band) and much higher than Participant 4.\" Participants 01, 02, 04, 05;\n# the features are all electrodes of the eight ROIs; scikit-learn LDA (shared covariance); three\n# balanced classes; the 7-fold scheme of M5; chance for c = 3 (O16).\n\n# %% tags=[\"claim:fig3-three-class\"]\nrng3 = np.random.default_rng(303)\nrows = []\nfor an in [\"a-ii\", \"b-ii\"]:\n    for o5, dr in [(\"c\", \"ii\"), (\"a\", \"ii\"), (\"b\", \"i\")]:\n        for o7 in \"ab\":\n            for p in [\"01\", \"02\", \"04\", \"05\"]:\n                S = SAMPLES[(an, p)]\n                pos = sorted({i for v in roi_sets(p, o5, dr, S[\"channels\"]).values() for i in v})\n                sp = A.make_splits(S[\"cls\"], [\"Talk\", \"TV\", \"Electronics\"], o7, rng3)\n                for bi, band in enumerate(A.BAND_NAMES):\n                    F = S[\"X\"][:, pos, bi].astype(float)\n                    accs, nts = [], []\n                    for tr, te in sp:\n                        clf = LinearDiscriminantAnalysis().fit(A.zscore(F[tr]), S[\"cls\"][tr])\n                        accs.append((clf.predict(A.zscore(F[te])) == S[\"cls\"][te]).mean())\n                        nts.append(len(te))\n                    rows.append(dict(artifact=an, O5=o5 + \"-\" + dr, O7=o7, participant=p, band=band, acc=np.mean(accs),\n                                     chance_fold05=np.mean([A.finite_chance(n, 3, 0.05) for n in nts]),\n                                     chance_total05=A.finite_chance(sum(nts), 3, 0.05), chance_total01=A.finite_chance(sum(nts), 3, 0.01),\n                                     n_test=sum(nts), electrodes=len(pos)))\nTC = pd.DataFrame(rows)\nmain3 = TC[(TC.artifact == \"a-ii\") & (TC.O5 == \"c-ii\") & (TC.O7 == \"a\")]\nprint(main3.pivot(index=\"participant\", columns=\"band\", values=\"acc\").round(3).to_string())\nprint(\"chance (per fold, 0.05):\", main3.groupby(\"participant\").chance_fold05.mean().round(3).to_dict())\nres3 = []\nfor k, g in TC.groupby([\"artifact\", \"O5\", \"O7\"]):\n    m = g.pivot(index=\"participant\", columns=\"band\", values=\"acc\")\n    above = all((g.acc > g[c]).all() for c in [\"chance_fold05\"])\n    above01 = (g.acc > g.chance_total01).all()\n    p2_70 = (m.loc[\"02\"] > 0.70).all()\n    p2_top = (m.mean(1).idxmax() == \"02\")\n    p2_gt4 = (m.loc[\"02\"] > m.loc[\"04\"]).all()\n    p2_gt4_b = (m.loc[\"02\"] > m.loc[\"05\"]).all()\n    res3.append(dict(reading=k, above_all=above, above_all_001=above01, p2_above70=p2_70, p2_highest=p2_top, p2_gt_p4=p2_gt4, p2_gt_t1_5=p2_gt4_b,\n                     p2_min=m.loc[\"02\"].min(), best=m.mean(1).idxmax()))\nR3 = pd.DataFrame(res3)\nR3[\"ok\"] = R3.above_all & R3.p2_above70 & R3.p2_highest & R3.p2_gt_p4\nprint(R3.round(3).to_string())\nprint(\"criterion met in %d of %d readings; above chance everywhere in %d\" % (R3.ok.sum(), len(R3), R3.above_all.sum()))\n\n# %% [markdown]\n# ## fig4-not-single-participant\n#\n# \"Every participant has accuracy significantly above chance for multiple ROI and band features.\" O13\n# (a) per participant, t-test of the 7 fold accuracies against the per-fold chance, BH FDR at 0.01 over\n# the participant's features; (b) mean fold accuracy above the participant's finite chance threshold\n# (n = all test samples).\n\n# %% tags=[\"claim:fig4-not-single-participant\"]\n\n\ndef per_participant(F, alpha=0.05, how=\"a\"):\n    out = {}\n    for p, g in F.groupby(\"participant\"):\n        rows = []\n        for (roi, band), h in g.groupby([\"roi\", \"band\"]):\n            if how == \"a\":\n                pv = stats.ttest_1samp(h.acc - h[f\"chance_fold_{alpha}\"], 0).pvalue\n                rows.append(dict(roi=roi, band=band, acc=h.acc.mean(), p=pv, above=h.acc.mean() > h[f\"chance_fold_{alpha}\"].mean()))\n            else:\n                rows.append(dict(roi=roi, band=band, acc=h.acc.mean(), p=np.nan, above=h.acc.mean() > A.finite_chance(int(h.ntest.sum()), 2, alpha)))\n        d = pd.DataFrame(rows)\n        d[\"sig\"] = (A.bh_fdr(d.p, 0.01) & d.above) if how == \"a\" else d.above\n        out[p] = d\n    return out\n\n\nrows = []\nfor g in GRID:\n    for alpha in (0.05, 0.01):\n        for how in \"ab\":\n            pp = per_participant(FOLDS[g], alpha, how)\n            rows.append(dict(reading=g, alpha=alpha, O13=how, **{p: int(pp[p].sig.sum()) if p in pp else 0 for p in P}))\nR4 = pd.DataFrame(rows)\nR4[\"n_ge2\"] = (R4[P] >= 2).sum(1)\nprint(\"main (O13 a, alpha 0.05): significant features per participant\", R4.iloc[0][P].to_dict())\nprint(R4.groupby([\"O13\", \"alpha\"])[P].median().to_string())\nprint(\"readings with all five participants >= 2 features: %d of %d; >= 4 participants: %d\" % ((R4.n_ge2 == 5).sum(), len(R4), (R4.n_ge2 >= 4).sum()))\n\n# %% [markdown]\n# ## fig4-missing-rois\n#\n# \"Participants 2 and 3 have no electrodes in at least one of the eight ROIs.\" Under O1 (a), figure\n# participants 2 and 3 are Table 1's 02 and 04.\n\n# %% tags=[\"claim:fig4-missing-rois\"]\nrows = []\nfor o5 in \"cab\":\n    for dr in [\"ii\", \"i\"]:\n        miss = {p: [SHORT[r] for r in A.ROIS if r not in roi_sets(p, o5, dr, SAMPLES[(\"a-ii\", p)][\"channels\"])] for p in P}\n        lack = sorted(p for p in P if miss[p])\n        rows.append(dict(O5=o5 + \"-\" + dr, lacking=lack, ok=lack == [\"02\", \"04\"], partial={\"02\", \"04\"} <= set(lack) and lack != [\"02\", \"04\"], missing=miss))\nR4m = pd.DataFrame(rows)\nprint(R4m.to_string())\nprint(\"criterion met under %d of %d ROI readings\" % (R4m.ok.sum(), len(R4m)))\n\n# %% [markdown]\n# ## fig4-participant2-high\n#\n# \"Participant 2 performs best, with several features above 75% accuracy and low and high gamma in the\n# inferior temporal lobe above 80%.\"\n\n# %% tags=[\"claim:fig4-participant2-high\"]\nrows = []\nfor g in GRID:\n    pm = FOLDS[g].groupby([\"participant\", \"roi\", \"band\"]).acc.mean().reset_index()\n    mean_p = pm.groupby(\"participant\").acc.mean()\n    p2 = pm[pm.participant == \"02\"]\n    it = p2[p2.roi == \"Temporal_Inf\"].set_index(\"band\").acc\n    rows.append(dict(reading=g, best=mean_p.idxmax(), p2_mean=mean_p[\"02\"], n75=int((p2.acc > 0.75).sum()),\n                     it_lg=it.get(\"low_gamma\", np.nan), it_hg=it.get(\"high_gamma\", np.nan), p2_max=p2.acc.max()))\nR4h = pd.DataFrame(rows)\nR4h[\"ok\"] = (R4h.best == \"02\") & (R4h.n75 >= 2) & (R4h.it_lg > 0.8) & (R4h.it_hg > 0.8)\nR4h[\"partial\"] = (R4h.best == \"02\") & (R4h.n75 >= 2) & (R4h.it_lg > 0.75) & (R4h.it_hg > 0.75)\nprint(\"main:\", R4h.iloc[0].to_dict())\nprint(\"participant mean accuracy, main:\", FM.groupby(\"participant\").acc.mean().round(3).to_dict())\nprint(\"best participant over readings:\", R4h.best.value_counts().to_dict())\nprint(\"criterion met in %d of %d; partial in %d; features above 75%% for participant 02: max %d; IT LG range %.3f to %.3f, IT HG %.3f to %.3f; max feature %.3f\"\n      % (R4h.ok.sum(), len(R4h), R4h.partial.sum(), R4h.n75.max(), R4h.it_lg.min(), R4h.it_lg.max(), R4h.it_hg.min(), R4h.it_hg.max(), R4h.p2_max.max()))\n\n# %% [markdown]\n# ## Mean differences (Figure 5)\n#\n# Talking minus watching TV of the fitted LDA class means (z-scored training data), per fold; t-test\n# against zero with BH FDR at 0.01; a feature is consistent when this and the accuracy test are both\n# significant (M8).\n\n# %% tags=[\"fig5-table\"]\nprint(\"main reading, mean difference (35 folds when all participants have the ROI):\")\nprint(mat(GM, \"meandiff\").round(3).to_string())\nprint(\"main reading, consistent features (sign shown):\")\nprint((mat(GM, \"consistent\").astype(float) * np.sign(mat(GM, \"meandiff\"))).to_string())\nprint(\"range of mean differences %.3f to %.3f; consistent: %d\" % (GM.meandiff.min(), GM.meandiff.max(), GM.consistent.sum()))\nprint(\"consistent features per reading:\", pd.Series([int(GROUP[k].consistent.sum()) for k in GROUP]).describe().round(1).to_dict())\n\n# %% [markdown]\n# ## fig5-gamma-higher-talking\n#\n# \"Low and high gamma activity is higher when a participant is talking than when watching TV.\"\n\n# %% tags=[\"claim:fig5-gamma-higher-talking\"]\n\n\ndef cons(G, bands):\n    return G[G.consistent & G.band.isin(bands)]\n\n\ndef gamma_ok(G, F):\n    c = cons(G, [\"low_gamma\", \"high_gamma\"])\n    return len(c) and (c.meandiff > 0).all() and set(c.band) == {\"low_gamma\", \"high_gamma\"}\n\n\nc = cons(GM, [\"low_gamma\", \"high_gamma\"])\nprint(\"main: consistent gamma features\", [(SHORT[r], b, round(m, 3)) for r, b, m in zip(c.roi, c.band, c.meandiff)])\nok = readings_meeting(gamma_ok)\nshow_readings(ok)\nfr = [((cons(GROUP[k], [\"low_gamma\", \"high_gamma\"]).meandiff > 0).mean() if len(cons(GROUP[k], [\"low_gamma\", \"high_gamma\"])) else np.nan) for k in GROUP]\nprint(\"fraction of consistent gamma features positive, over readings: median %.2f, readings with a majority positive %d of %d\"\n      % (np.nanmedian(fr), np.sum(np.array(fr) > 0.5), len(fr)))\n\n# %% [markdown]\n# ## fig5-theta-alpha-lower-talking\n#\n# \"Theta and alpha activity is lower when a participant is talking than when watching TV.\"\n\n# %% tags=[\"claim:fig5-theta-alpha-lower-talking\"]\n\n\ndef ta_ok(G, F):\n    c = cons(G, [\"theta\", \"alpha\"])\n    return len(c) and (c.meandiff < 0).all() and set(c.band) == {\"theta\", \"alpha\"}\n\n\nc = cons(GM, [\"theta\", \"alpha\"])\nprint(\"main: consistent theta and alpha features\", [(SHORT[r], b, round(m, 3)) for r, b, m in zip(c.roi, c.band, c.meandiff)])\nok = readings_meeting(ta_ok)\nshow_readings(ok)\nfr = [((cons(GROUP[k], [\"theta\", \"alpha\"]).meandiff < 0).mean() if len(cons(GROUP[k], [\"theta\", \"alpha\"])) else np.nan) for k in GROUP]\nprint(\"fraction of consistent theta/alpha features negative: median %.2f, readings with a majority negative %d of %d\"\n      % (np.nanmedian(fr), np.sum(np.array(fr) > 0.5), len(fr)))\n\n# %% [markdown]\n# ## fig5-pre-postcentral\n#\n# \"The largest differences are in the precentral and postcentral gyri, with consistent differences in\n# theta, alpha, low gamma and high gamma.\"\n\n# %% tags=[\"claim:fig5-pre-postcentral\"]\nSIGNS = {\"theta\": -1, \"alpha\": -1, \"low_gamma\": 1, \"high_gamma\": 1}\n\n\ndef prepost(G):\n    top = G.loc[G.meandiff.abs().idxmax()]\n    n = 0\n    for r in [\"Precentral\", \"Postcentral\"]:\n        for b, s in SIGNS.items():\n            row = G[(G.roi == r) & (G.band == b)]\n            n += int(len(row) and row.consistent.iloc[0] and np.sign(row.meandiff.iloc[0]) == s)\n    return top.roi in (\"Precentral\", \"Postcentral\"), n, (SHORT[top.roi], top.band, round(top.meandiff, 3))\n\n\nprint(\"main:\", prepost(GM))\nok = readings_meeting(lambda G, F: prepost(G)[0] and prepost(G)[1] == 8)\nshow_readings(ok)\nns = pd.Series([prepost(GROUP[k])[1] for k in GROUP])\nprint(\"of the 8 features consistent with the expected sign, over readings:\", ns.value_counts().sort_index().to_dict())\nprint(\"largest |difference| in pre- or postcentral in %d of %d readings\" % (sum(prepost(GROUP[k])[0] for k in GROUP), len(GROUP)))\n\n# %% [markdown]\n# ## fig5-parietal-temporal-no-gamma\n#\n# \"In the supramarginal gyrus, inferior parietal lobe and superior temporal lobe there is no consistent\n# gamma increase during talking, while the theta and alpha differences are still present there.\"\n\n# %% tags=[\"claim:fig5-parietal-temporal-no-gamma\"]\nTHREE = [\"SupraMarginal\", \"Parietal_Inf\", \"Temporal_Sup\"]\n\n\ndef ptg(G):\n    g = G[G.roi.isin(THREE) & G.band.isin([\"low_gamma\", \"high_gamma\"])]\n    gamma_none = not (g.consistent & (g.meandiff > 0)).any()\n    ta = {r: bool((G[(G.roi == r) & G.band.isin([\"theta\", \"alpha\"])].pipe(lambda d: d.consistent & (d.meandiff < 0))).any()) for r in THREE}\n    return gamma_none, ta\n\n\nprint(\"main:\", ptg(GM))\nprint(GM[GM.roi.isin(THREE)][[\"roi\", \"band\", \"meandiff\", \"md_lo\", \"md_hi\", \"p_md\", \"consistent\"]].round(4).to_string())\nok = readings_meeting(lambda G, F: ptg(G)[0] and all(ptg(G)[1].values()))\nshow_readings(ok)\nokp = readings_meeting(lambda G, F: ptg(G)[0] and sum(ptg(G)[1].values()) >= 2)\nprint(\"gamma part holds and theta/alpha in at least 2 of 3 ROIs:\", len(okp), \"| gamma part alone:\", len(readings_meeting(lambda G, F: ptg(G)[0])))\n\n# %% [markdown]\n# ## fig5-middle-temporal-tv\n#\n# \"The middle temporal lobe shows consistently higher activity in 4 of the 5 bands when participants\n# watch TV than when they talk.\"\n\n# %% tags=[\"claim:fig5-middle-temporal-tv\"]\n\n\ndef mt_neg(G):\n    g = G[G.roi == \"Temporal_Mid\"]\n    return int((g.consistent & (g.meandiff < 0)).sum())\n\n\nprint(\"main: middle temporal bands consistent with a negative difference:\", mt_neg(GM))\nprint(GM[GM.roi == \"Temporal_Mid\"][[\"band\", \"acc\", \"sig_acc\", \"meandiff\", \"p_md\", \"consistent\"]].round(4).to_string())\nok = readings_meeting(lambda G, F: mt_neg(G) == 4)\nshow_readings(ok)\nprint(\"distribution over readings:\", pd.Series([mt_neg(GROUP[k]) for k in GROUP]).value_counts().sort_index().to_dict())\n\n# %% [markdown]\n# ## inferior-temporal-high-gamma-inconsistent\n#\n# \"High gamma in the inferior temporal lobe decodes well but its mean difference is virtually zero.\"\n# A claim of absence judged on the paper's test (M8) under the main reading; the grid is a variant.\n\n# %% tags=[\"claim:inferior-temporal-high-gamma-inconsistent\"]\nrow = GM[(GM.roi == \"Temporal_Inf\") & (GM.band == \"high_gamma\")].iloc[0]\nprint(\"main: IT high gamma accuracy %.3f (significant %s, p = %.3g); mean difference %.4f, 95%% CI %.4f to %.4f, p = %.3g, significant after BH: %s\"\n      % (row.acc, row.sig_acc, row.p_acc, row.meandiff, row.md_lo, row.md_hi, row.p_md, row.sig_md))\nrank = (GM.meandiff.abs() >= abs(row.meandiff)).sum()\nprint(\"its |mean difference| ranks %d of %d features (median |difference| %.4f)\" % (rank, len(GM), GM.meandiff.abs().median()))\nv = pd.DataFrame([dict(sig_acc=GROUP[k].query(\"roi=='Temporal_Inf' and band=='high_gamma'\").sig_acc.iloc[0],\n                       sig_md=GROUP[k].query(\"roi=='Temporal_Inf' and band=='high_gamma'\").sig_md.iloc[0]) for k in GROUP])\nprint(\"over readings: accuracy significant in %d, mean difference significant in %d, of %d\" % (v.sig_acc.sum(), v.sig_md.sum(), len(v)))\n\n# %% [markdown]\n# ## all-rois-but-inferior-parietal\n#\n# \"Every ROI except the inferior parietal lobe has at least one band that both separates the two\n# behaviours and is consistent across participants.\"\n\n# %% tags=[\"claim:all-rois-but-inferior-parietal\"]\n\n\ndef roi_cons(G):\n    return G[G.consistent].groupby(\"roi\").size().reindex(A.ROIS).fillna(0).astype(int)\n\n\nprint(\"main, consistent bands per ROI:\", {SHORT[k]: v for k, v in roi_cons(GM).items()})\nSEVEN = [r for r in A.ROIS if r != \"Parietal_Inf\"]\nok = readings_meeting(lambda G, F: all(roi_cons(G)[r] >= 1 for r in SEVEN) and roi_cons(G)[\"Parietal_Inf\"] == 0)\nshow_readings(ok)\nokp = readings_meeting(lambda G, F: sum(roi_cons(G)[r] >= 1 for r in SEVEN) >= 6 and roi_cons(G)[\"Parietal_Inf\"] == 0)\nprint(\"six of seven with IP none:\", len(okp))\nprint(\"number of the seven ROIs with a consistent band, over readings:\", pd.Series([sum(roi_cons(GROUP[k])[r] >= 1 for r in SEVEN) for k in GROUP]).value_counts().sort_index().to_dict())\n\n# %% [markdown]\n# ## fig6-sign-consistency\n#\n# \"The sign of the Talking minus Watching TV difference is the same in all participants for 9 of the 40\n# ROI and band combinations (22.5%).\" Per participant, the mean over the 7 folds of the ROI's mean\n# difference. O14 (a) the participants that have the ROI share a sign; (b) only combinations present in\n# all five can count.\n\n# %% tags=[\"claim:fig6-sign-consistency\"]\n\n\ndef same_sign(F, how):\n    m = F.groupby([\"roi\", \"band\", \"participant\"]).meandiff.mean().unstack()\n    out = []\n    for (roi, band), r in m.iterrows():\n        v = r.dropna()\n        if how == \"b\" and len(v) < 5:\n            continue\n        if len(v) >= 2 and (np.all(v > 0) or np.all(v < 0)):\n            out.append((roi, band, int(np.sign(v.iloc[0]))))\n    return out\n\n\nfor how in \"ab\":\n    s = same_sign(FM, how)\n    print(\"main, O14 %s: %d combinations\" % (how, len(s)), [(SHORT[r], b, sg) for r, b, sg in s])\nrows = []\nfor g in GRID:\n    for how in \"ab\":\n        rows.append(dict(reading=g, O14=how, n=len(same_sign(FOLDS[g], how))))\nR6 = pd.DataFrame(rows)\nprint(\"count over readings:\", R6.n.value_counts().sort_index().to_dict())\nprint(\"readings with 8 to 10: %d of %d; 7 or 11: %d\" % (R6.n.between(8, 10).sum(), len(R6), R6.n.isin([7, 11]).sum()))\nprint(\"main per-participant matrix of mean differences (participant 02):\")\nprint(FM[FM.participant == \"02\"].groupby([\"band\", \"roi\"]).meandiff.mean().unstack().rename(columns=SHORT).round(3).to_string())\n\n# %% [markdown]\n# ## fig6-examples\n#\n# \"High gamma in the precentral, middle frontal and postcentral regions, and alpha in the precentral,\n# inferior parietal and supramarginal regions, have the same sign in all participants.\"\n\n# %% tags=[\"claim:fig6-examples\"]\nSIX = [(\"Precentral\", \"high_gamma\"), (\"Frontal_Mid\", \"high_gamma\"), (\"Postcentral\", \"high_gamma\"),\n       (\"Precentral\", \"alpha\"), (\"Parietal_Inf\", \"alpha\"), (\"SupraMarginal\", \"alpha\")]\n\n\ndef six_count(F, how):\n    s = {(r, b) for r, b, _ in same_sign(F, how)}\n    return sum(x in s for x in SIX)\n\n\nprint(\"main:\", {how: six_count(FM, how) for how in \"ab\"})\nm = FM.groupby([\"roi\", \"band\", \"participant\"]).meandiff.mean().unstack()\nprint(m.loc[SIX].round(3).rename(index=SHORT).to_string())\nR6[\"six\"] = [six_count(FOLDS[g], how) for g in GRID for how in \"ab\"]\nprint(\"over readings:\", R6.six.value_counts().sort_index().to_dict(), \"| all six in\", (R6.six == 6).sum(), \"| 4 or 5 in\", R6.six.isin([4, 5]).sum())\n\n# %% [markdown]\n# ## Figure 7: adding ROIs\n#\n# Per participant and band, ROIs ranked and added one at a time. O15 (a): within each outer fold one\n# training fold (the one next to the buffer) is held out as a validation set to rank ROIs by their\n# single-ROI accuracy, the classifier is trained on the other training folds and tested on the test\n# fold; (b): ROIs ranked by the participant's single-ROI cross-validated accuracies, and the 7-fold\n# scheme of M5. Run on the main artifact reading for every ROI reading, O6 and O7.\n\n# %% tags=[\"fig7-compute\"]\nrng7 = np.random.default_rng(707)\n\n\ndef curves(S, rois, o6, o7, o15, single=None):\n    y = S[\"cls\"]\n    use = np.where(np.isin(y, [\"Talk\", \"TV\"]))[0]\n    folds, plan = A.folds_and_buffers(len(use), o7)\n    names = list(rois)\n    out = {}\n    for bi, band in enumerate(A.BAND_NAMES):\n        feats = {r: (S[\"X\"][:, rois[r], bi].astype(float) if o6 == \"a\" else S[\"X\"][:, rois[r], bi].astype(float).mean(1, keepdims=True)) for r in names}\n        accs = np.zeros((len(plan), len(names)))\n        for fi, (train, i) in enumerate(plan):\n            te = A.balance(use[folds[i]], y, rng7)\n            if o15 == \"a\":\n                v = min(train, key=lambda j: (abs(j - i), -j))  # nearest training fold to the test fold\n                v = [j for j in train if abs(j - i) == min(abs(t - i) for t in train)][-1]\n                tr = A.balance(use[np.concatenate([folds[j] for j in train if j != v])], y, rng7)\n                va = A.balance(use[folds[v]], y, rng7)\n                sc = []\n                for r in names:\n                    pr, _, _ = A.lda2(A.zscore(feats[r][tr]), y[tr] == \"Talk\", A.zscore(feats[r][va]))\n                    sc.append((pr == (y[va] == \"Talk\")).mean())\n                rank = [names[k] for k in np.argsort(sc)[::-1]]\n            else:\n                tr = A.balance(use[np.concatenate([folds[j] for j in train])], y, rng7)\n                rank = sorted(names, key=lambda r: -single[(r, band)])\n            for k in range(1, len(names) + 1):\n                Fk = np.concatenate([feats[r] for r in rank[:k]], axis=1)\n                pr, _, _ = A.lda2(A.zscore(Fk[tr]), y[tr] == \"Talk\", A.zscore(Fk[te]))\n                accs[fi, k - 1] = (pr == (y[te] == \"Talk\")).mean()\n        out[band] = accs\n    return out\n\n\nt = time.time()\nCURVES = {}\nfor g in GRID:\n    an, o5, dr, o6, o7 = g\n    if an != \"a-ii\":\n        continue\n    single_all = FOLDS[g].groupby([\"participant\", \"roi\", \"band\"]).acc.mean()\n    for o15 in \"ab\":\n        for p in P:\n            S = SAMPLES[(an, p)]\n            rois = roi_sets(p, o5, dr, S[\"channels\"])\n            CURVES[(g, o15, p)] = curves(S, rois, o6, o7, o15, single_all.loc[p])\nprint(len(CURVES), \"curve sets in\", round(time.time() - t), \"s\")\n\n\ndef curve_table(g, o15):\n    rows = []\n    for p in P:\n        for band, accs in CURVES[(g, o15, p)].items():\n            m = accs.mean(0)\n            ci = stats.t.ppf(0.975, accs.shape[0] - 1) * stats.sem(accs[:, 0])\n            rows.append(dict(participant=p, band=band, k=len(m), top1=m[0], all=m[-1], best=m.max(), best_k=int(m.argmax()) + 1,\n                             ci_top1=ci, curve=np.round(m, 3)))\n    return pd.DataFrame(rows)\n\n\nCT = {(g, o15): curve_table(g, o15) for g in GRID if g[0] == \"a-ii\" for o15 in \"ab\"}\nct = CT[(MAIN, \"a\")]\nprint(\"main reading, O15 (a):\")\nprint(ct.drop(columns=\"curve\").round(3).to_string())\nprint(\"curves (mean test accuracy for k = 1, 2, ... ROIs), participant 01:\")\nfor r in ct[ct.participant == \"01\"].itertuples():\n    print(\"  \", r.band, r.curve)\nprint(\"range of curve values %.3f to %.3f\" % (min(c.min() for c in ct.curve), max(c.max() for c in ct.curve)))\n\n# %% [markdown]\n# ## fig7-non-additive\n#\n# \"Adding electrodes from further top-ranked ROIs generally does not improve a participant's decoding\n# performance.\" Readings: (a) additive when all ROIs beat the top ROI alone; (b) additive when the best\n# over k beats the top ROI by more than the 95% interval of the top ROI's fold accuracies.\n\n# %% tags=[\"claim:fig7-non-additive\"]\nrows = []\nfor (g, o15), c in CT.items():\n    na = int((c[\"all\"] > c.top1).sum())\n    nb = int((c.best - c.top1 > c.ci_top1).sum())\n    rows.append(dict(reading=g, O15=o15, additive_a=na, additive_b=nb))\nR7 = pd.DataFrame(rows)\nprint(R7.to_string())\nprint(\"main (O15 a): additive curves, reading (a) %d of 25, reading (b) %d of 25\" % (R7.iloc[0].additive_a, R7.iloc[0].additive_b))\nprint(\"readings with at most 5 additive: (a) %d, (b) %d, of %d; 6 to 12: (a) %d, (b) %d\"\n      % ((R7.additive_a <= 5).sum(), (R7.additive_b <= 5).sum(), len(R7), R7.additive_a.between(6, 12).sum(), R7.additive_b.between(6, 12).sum()))\n\n# %% [markdown]\n# ## fig7-participant4-low-gamma\n#\n# \"The only notable additive case is Participant 4 in the low gamma band.\" Figure participant 4 is\n# Table 1's 05 under O1 (a) and 04 under O1 (b).\n\n# %% tags=[\"claim:fig7-participant4-low-gamma\"]\nrows = []\nfor (g, o15), c in CT.items():\n    c = c.assign(gain=c.best - c.top1).sort_values(\"gain\", ascending=False).reset_index(drop=True)\n    for o1, p4 in [(\"a\", \"05\"), (\"b\", \"04\")]:\n        pos = c.index[(c.participant == p4) & (c.band == \"low_gamma\")][0] + 1\n        rows.append(dict(reading=g, O15=o15, O1=o1, rank=pos, gain=c.gain[pos - 1], top=(c.participant[0], c.band[0], round(c.gain[0], 3))))\nR7b = pd.DataFrame(rows)\nprint(R7b.head(4).to_string())\nprint(\"rank 1 in %d of %d; among top three in %d\" % ((R7b[\"rank\"] == 1).sum(), len(R7b), (R7b[\"rank\"] <= 3).sum()))\n\n# %% [markdown]\n# ## fig7-above-70\n#\n# \"With a simple LDA, every participant reaches more than 70% accuracy, with a maximum of about 80% for\n# Participant 4 in the low and high gamma bands.\"\n\n# %% tags=[\"claim:fig7-above-70\"]\nrows = []\nfor (g, o15), c in CT.items():\n    best = c.groupby(\"participant\").best.max()\n    for o1, p4 in [(\"a\", \"05\"), (\"b\", \"04\")]:\n        lg = c[(c.participant == p4) & (c.band == \"low_gamma\")].best.iloc[0]\n        hg = c[(c.participant == p4) & (c.band == \"high_gamma\")].best.iloc[0]\n        rows.append(dict(reading=g, O15=o15, O1=o1, n_above70=int((best > 0.7).sum()), p4_lg=lg, p4_hg=hg,\n                         p4_highest=best.idxmax() == p4, **{\"best_\" + p: best[p] for p in P}))\nR7c = pd.DataFrame(rows)\nR7c[\"ok\"] = (R7c.n_above70 == 5) & ((R7c.p4_lg - 0.8).abs() <= 0.08) & ((R7c.p4_hg - 0.8).abs() <= 0.08) & R7c.p4_highest\nprint(R7c.head(2).round(3).to_string())\nprint(\"criterion met in %d of %d; participants above 70%%, over readings:\" % (R7c.ok.sum(), len(R7c)), R7c.n_above70.value_counts().sort_index().to_dict())\nprint(\"best accuracy per participant, range over readings:\", {p: (round(R7c[\"best_\" + p].min(), 3), round(R7c[\"best_\" + p].max(), 3)) for p in P})\n\n# %% [markdown]\n# ## discussion-above-80\n#\n# \"Subject-specific classification performance regularly exceeds 80% with a simple LDA.\" Read as at\n# least three of the five participants with some feature (Figure 4) or curve point (Figure 7) above 80%.\n\n# %% tags=[\"claim:discussion-above-80\"]\nrows = []\nfor (g, o15), c in CT.items():\n    f4 = FOLDS[g].groupby([\"participant\", \"roi\", \"band\"]).acc.mean().groupby(\"participant\").max()\n    f7 = c.groupby(\"participant\").best.max()\n    top = pd.concat([f4, f7], axis=1).max(1)\n    rows.append(dict(reading=g, O15=o15, n_above80=int((top > 0.8).sum()), max_any=top.max(), **{p: round(top[p], 3) for p in P}))\nR8 = pd.DataFrame(rows)\nprint(R8.head(2).to_string())\nprint(\"participants above 80%% over readings:\", R8.n_above80.value_counts().sort_index().to_dict(), \"| max %.3f\" % R8.max_any.max())\n\n# %% [markdown]\n# ## fig7-exceeds-group\n#\n# \"For individual participants, performance usually exceeds the group-level performance of Figure 2.\"\n# (a) each participant's best Figure 7 accuracy against the highest participant-wide accuracy of Figure\n# 2, at least four of five; (b) each curve's best against the participant-wide accuracy of the same\n# band in the curve's top ROI, more than half of the 25.\n\n# %% tags=[\"claim:fig7-exceeds-group\"]\nrows = []\nfor (g, o15), c in CT.items():\n    G = GROUP[(g, CHANCES[0])]\n    best_p = c.groupby(\"participant\").best.max()\n    na = int((best_p > G.acc.max()).sum())\n    single = FOLDS[g].groupby([\"participant\", \"roi\", \"band\"]).acc.mean()\n    nb = 0\n    for r in c.itertuples():\n        sub = single.loc[r.participant].xs(r.band, level=\"band\")\n        top_roi = sub.idxmax()\n        ga = G[(G.roi == top_roi) & (G.band == r.band)].acc.iloc[0]\n        nb += int(r.best > ga)\n    rows.append(dict(reading=g, O15=o15, group_max=G.acc.max(), n_part_a=na, n_curves_b=nb))\nR9 = pd.DataFrame(rows)\nprint(R9.head(2).round(3).to_string())\nprint(\"reading (a) at least 4 of 5 in %d of %d; reading (b) more than 12 of 25 in %d\" % ((R9.n_part_a >= 4).sum(), len(R9), (R9.n_curves_b > 12).sum()))\n\n# %% [markdown]\n# ## fig7-best-band-varies\n#\n# \"The band that gives a participant's highest performance varies by participant; Participant 5 is best\n# with theta and Participant 3 best with alpha.\" Under O1 (a), figure 5 is Table 1's 08, figure 3 is 04.\n\n# %% tags=[\"claim:fig7-best-band-varies\"]\nrows = []\nfor (g, o15), c in CT.items():\n    bb = c.loc[c.groupby(\"participant\").best.idxmax()].set_index(\"participant\").band\n    rows.append(dict(reading=g, O15=o15, **bb.to_dict()))\nR10 = pd.DataFrame(rows)\nR10[\"ok\"] = (R10[\"08\"] == \"theta\") & (R10[\"04\"] == \"alpha\")\nR10[\"one\"] = (R10[\"08\"] == \"theta\") | (R10[\"04\"] == \"alpha\")\nprint(R10.head(2).to_string())\nprint(\"best band of 08:\", R10[\"08\"].value_counts().to_dict(), \"| of 04:\", R10[\"04\"].value_counts().to_dict())\nprint(\"both in %d of %d; one in %d; number of distinct best bands across participants (main): %d\"\n      % (R10.ok.sum(), len(R10), R10.one.sum(), R10.iloc[0][P].nunique()))\n\n# %% tags=[\"runtime\"]\nprint(\"runtime %.1f min, peak memory %.2f GB (this process), children %.2f GB\"\n      % ((time.time() - T0) / 60, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6, resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1e6))\n"
}
```

```
File created successfully at: /tmp/claude-1001/cells.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/runcells.py <<'EOF'
import re, sys, time, pickle, os
os.chdir('entries/alasfour-2024'); sys.path.insert(0,'.')
src=open('/tmp/claude-1001/cells.py').read()
parts=re.split(r'^# %% ?', src, flags=re.M)[1:]
cells=[]
for p in parts:
    head,_,body=p.partition('\n')
    cells.append((head.strip(), body))
start=sys.argv[1] if len(sys.argv)>1 else None
ns={}
EXTRACT='''
import pickle
D=pickle.load(open('/tmp/claude-1001/feats.pkl','rb'))
CH=D['chans']; KEYS=D['keys']; JOBS=[(a,c,b,None,o) for a,c,b,o in D['jobs']]; RES=[(r,0,0) for r in D['res']]
'''
for head,body in cells:
    if head.startswith('[markdown]'): continue
    tag=re.findall(r'"([^"]+)"',head)
    tag=tag[0] if tag else ''
    code=EXTRACT if tag=='extract' else body
    if tag=='survey' and os.path.exists('/tmp/claude-1001/survey_ns.pkl'):
        exec(body.split('META = A.survey(assets)')[0], ns)
        ns['META']=pickle.load(open('/tmp/claude-1001/survey_ns.pkl','rb'))
        exec(body.split('META = A.survey(assets)')[1], ns)
        continue
    t=time.time()
    print('=====',tag, flush=True)
    try:
        exec(code, ns)
    except Exception as e:
        import traceback; traceback.print_exc(); print('FAILED IN', tag); break
    if tag=='survey': pickle.dump(ns['META'],open('/tmp/claude-1001/survey_ns.pkl','wb'))
    print('----- %.1fs'%(time.time()-t), flush=True)
EOF
. $TMPDIR/env/bin/activate; uv pip install -q statsmodels scikit-learn 2>&1|tail -1; date -u; python $TMPDIR/runcells.py 2>&1 | tail -150
```

```
Tue Nov 10 04:47:58 UTC 2026
81   (b-i, a, ii, a, b)  (inferior temporal, high_gamma)     0.705  0.705           True        True
82   (b-i, a, ii, b, a)        (postcentral, high_gamma)     0.561  0.550          False       False
83   (b-i, a, ii, b, b)             (postcentral, alpha)     0.560  0.539          False       False
84    (b-i, a, i, a, a)  (inferior temporal, high_gamma)     0.706  0.706           True        True
85    (b-i, a, i, a, b)  (inferior temporal, high_gamma)     0.705  0.705           True        True
86    (b-i, a, i, b, a)        (postcentral, high_gamma)     0.574  0.550          False       False
87    (b-i, a, i, b, b)             (postcentral, alpha)     0.572  0.539          False       False
88   (b-i, b, ii, a, a)  (inferior temporal, high_gamma)     0.712  0.712           True        True
89   (b-i, b, ii, a, b)  (inferior temporal, high_gamma)     0.712  0.712           True        True
90   (b-i, b, ii, b, a)  (inferior temporal, high_gamma)     0.579  0.579           True       False
91   (b-i, b, ii, b, b)  (inferior parietal, high_gamma)     0.579  0.545          False       False
92    (b-i, b, i, a, a)  (inferior temporal, high_gamma)     0.712  0.712           True        True
93    (b-i, b, i, a, b)  (inferior temporal, high_gamma)     0.712  0.712           True        True
94    (b-i, b, i, b, a)  (inferior temporal, high_gamma)     0.579  0.579           True       False
95    (b-i, b, i, b, b)  (inferior parietal, high_gamma)     0.579  0.545          False       False
readings where IT high gamma is highest: 36; within 62.1 to 75.9%: 38; both: 30 of 96
----- 0.1s
===== fig2-significance
Main reading, significant features (1) and finite chance level 0.565
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cd $TMPDIR; python3 - <<'EOF'
s=open('cells.py').read()
s=s.replace("""    C = CEN.values[L]
    dl = dens.values[L].astype(float)""","""    Cl = CEN.values[L]
    dl = dens.values[L].astype(float)""")
s=s.replace("d2 = ((xyz[:n, None, :] - C[None]) ** 2).sum(-1)","d2 = ((xyz[:n, None, :] - Cl[None]) ** 2).sum(-1)")
open('cells.py','w').write(s)
EOF
python $TMPDIR/runcells.py > $TMPDIR/out1.txt 2>&1; grep -n "FAILED\|Error" $TMPDIR/out1.txt | head; wc -l $TMPDIR/out1.txt
```

```
738 /tmp/claude-1001/out1.txt
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -v "^ *[0-9]* *(\(a\|b\)-i" out1.txt | head -300
```

```
===== setup
----- 1.2s
55 assets, 12 subjects, 845.9 GB
subject
01       [3, 4, 5, 7]
02       [3, 4, 5, 6]
03       [3, 4, 5, 6]
04    [3, 4, 5, 6, 7]
05          [3, 4, 7]
06    [3, 4, 5, 6, 7]
07    [3, 4, 5, 6, 7]
08    [3, 4, 5, 6, 7]
09    [3, 4, 5, 6, 7]
10    [3, 4, 5, 6, 7]
11    [3, 4, 5, 6, 7]
12    [3, 4, 5, 6, 7]
ElectricalSeries: (43200000, 92) chunks (84375, 1) rate 500.0 unit volts conversion 1e-06
electrodes columns: ['filtering', 'good', 'group_name', 'high_freq_R2', 'id', 'imp', 'kurtosis', 'location', 'low_freq_R2', 'median_deviation', 'standard_deviation', 'x', 'y', 'z']
epochs columns: labels, start_time, stop_time; labels seen:
label
[... 281 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n '/claim:anova-roi-band-effects/,$p' out1.txt | grep -v "^ *[0-9]\+ \+(\(a\|b\)-i" | head -280
```

```
===== claim:anova-roi-band-effects
main, fold level, type 2: {'C(roi)': 'F=7.22 p=1.7e-08', 'C(band)': 'F=7.18 p=1e-05', 'C(roi):C(band)': 'F=0.78 p=0.79'}
main, fold level, type 1: {'C(roi)': 'F=7.22 p=1.7e-08', 'C(band)': 'F=7.18 p=1e-05', 'C(roi):C(band)': 'F=0.78 p=0.79'}
main, fold level, type 3: {'C(roi)': 'F=1.17 p=0.32', 'C(band)': 'F=1.54 p=0.19', 'C(roi):C(band)': 'F=0.78 p=0.79'}
main, participant level, type 2: {'C(roi)': 'F=2.83 p=0.0087', 'C(band)': 'F=2.82 p=0.028', 'C(roi):C(band)': 'F=0.31 p=1'}
main, participant level, type 1: {'C(roi)': 'F=2.83 p=0.0087', 'C(band)': 'F=2.82 p=0.028', 'C(roi):C(band)': 'F=0.31 p=1'}
main, participant level, type 3: {'C(roi)': 'F=0.46 p=0.86', 'C(band)': 'F=0.61 p=0.66', 'C(roi):C(band)': 'F=0.31 p=1'}
type II over the grid: both main effects p < 0.001 in 59 of 192 (fold level 44 of 96)
p_roi range 1.2e-44 to 0.95; p_band range 3.4e-22 to 0.82
----- 2.3s
===== claim:anova-no-interaction
main, type II, fold accuracies: interaction F = 0.779, df = 28, p = 0.789
over the grid (type II): interaction p >= 0.05 in 77 of 96 fold-level readings; p range 0.00629 to 0.988
participant level: p >= 0.05 in 96 of 96
----- 0.0s
===== claim:posthoc-band-averages
main (O11 a): {'alpha': 0.541, 'beta': 0.549, 'high_gamma': 0.58, 'low_gamma': 0.562, 'theta': 0.538} chance 0.565
main (O11 b): {'alpha': 0.541, 'beta': 0.547, 'high_gamma': 0.576, 'low_gamma': 0.56, 'theta': 0.537}
criterion met in 12 of 768 readings; order (HG top, beta bottom) in 132
highest band over readings: {'high_gamma': 728, 'low_gamma': 36, 'theta': 4} | lowest: {'theta': 332, 'alpha': 280, 'beta': 136, 'low_gamma': 20}
[... 243 more lines not kept]
```

**Agent**

All cells run on the cache (4.8 min of analysis). Now fixing small issues (main chance reading, SD check with missing values, clock check context) and writing the result cells.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
s=open('cells.py').read()
def rep(a,b):
    global s
    assert a in s, a[:60]
    s=s.replace(a,b)
rep('CHANCES = [(0.05, "fold"), (0.01, "fold"), (0.05, "total"), (0.01, "total")]','CHANCES = [(0.05, "total"), (0.01, "total"), (0.05, "fold"), (0.01, "fold")]')
rep("# The main reading, the one the paper best supports in this attempt's judgement, is O4 (a)(ii),\n# O5 (c)(ii), O6 (a), O7 (a), O9 alpha 0.05 per fold.","# The main reading, the one the paper best supports in this attempt's judgement, is O4 (a)(ii),\n# O5 (c)(ii), O6 (a), O7 (a), O9 alpha 0.05 with n all test samples of the participant (Figure 2\n# draws one dashed chance line).")
rep("""        ss = sum(r["sumsq"] for r in res if r is not None)
        nn = sum(r["n"] for r in res if r is not None)""","""        ss = np.nansum([r["sumsq"] for r in res if r is not None], axis=0)
        nn = np.sum([np.isfinite(r["sumsq"]) * r["n"] for r in res if r is not None], axis=0)""")
rep('''print("min %.1f, median %.1f, max %.1f, n %d" % (dur.min(), dur.median(), dur.max(), len(dur)))''','''print("min %.1f, median %.1f, max %.1f, n %d; outside 110 to 130 s: %d; shorter than 10 s (no bin): %d"
      % (dur.min(), dur.median(), dur.max(), len(dur), ((dur < 110) | (dur > 130)).sum(), (dur < 10).sum()))''')
rep('''for p, d in [("01", 7), ("04", 3)]:
    S = SAMPLES[("a-ii", p)]''','''print("Leave-one-day-out: trained on the participant's other days, tested on one day (high gamma, all ROI electrodes):")
for p in ["01", "04"]:
  for d in sorted(set(SAMPLES[("a-ii", p)]["day"])):
    S = SAMPLES[("a-ii", p)]''')
rep('''    print("participant %s day %d with the offset: tested on %d balanced bins of that day, accuracy %.3f (chance 0.05 level %.3f)"
          % (p, d, len(te), acc, A.finite_chance(len(te), 2, 0.05)))''','''    print("  participant %s day %d%s: %d balanced bins, accuracy %.3f (finite chance at 0.05: %.3f)"
          % (p, d, " (offset applied)" if (p, d) in [("01", 7), ("04", 3)] else "", len(te), acc, A.finite_chance(len(te), 2, 0.05)))''')
s=s.replace('''    tr = np.where((S["day"] != d) & np.isin(S["cls"], ["Talk", "TV"]))[0]
    te = np.where((S["day"] == d) & np.isin(S["cls"], ["Talk", "TV"]))[0]
    tr, te = A.balance(tr, S["cls"], rng), A.balance(te, S["cls"], rng)
    F = S["X"][:, pos, 4].astype(float)
    pred, _, _ = A.lda2(A.zscore(F[tr]), S["cls"][tr] == "Talk", A.zscore(F[te]))
    acc = (pred == (S["cls"][te] == "Talk")).mean()''','''    pos = sorted({i for v in roi_sets(p, "c", "ii", S["channels"]).values() for i in v})
    tr = np.where((S["day"] != d) & np.isin(S["cls"], ["Talk", "TV"]))[0]
    te = np.where((S["day"] == d) & np.isin(S["cls"], ["Talk", "TV"]))[0]
    if min((S["cls"][te] == c).sum() for c in ["Talk", "TV"]) < 5:
        print("  participant %s day %d: fewer than 5 bins of a class" % (p, d))
        continue
    tr, te = A.balance(tr, S["cls"], rng), A.balance(te, S["cls"], rng)
    F = S["X"][:, pos, 4].astype(float)
    pred, _, _ = A.lda2(A.zscore(F[tr]), S["cls"][tr] == "Talk", A.zscore(F[te]))
    acc = (pred == (S["cls"][te] == "Talk")).mean()''')
rep('''    pos = sorted({i for v in roi_sets(p, "c", "ii", S["channels"]).values() for i in v})
    pos = sorted({i for v in roi_sets(p, "c", "ii", S["channels"]).values() for i in v})''','''    pos = sorted({i for v in roi_sets(p, "c", "ii", S["channels"]).values() for i in v})''')
rep('print("participants above 80%% over readings:"','print("participants above 80% over readings:"')
rep('''print("main Tukey: IT higher than %d of %d other ROIs" % tuple(roi_posthoc(FM, "a")[0:1][0].count(True) for _ in [0]) if False else "", end="")
''','')
rep('''                v = min(train, key=lambda j: (abs(j - i), -j))  # nearest training fold to the test fold
                v = [j for j in train''','''                v = [j for j in train''')  # nearest training fold to the test fold (the later one on a tie)
open('cells.py','w').write(s)
EOF
grep -n "pos = sorted" $TMPDIR/cells.py | head; sed -n '/Leave-one-day-out/,/Without the offset/p' $TMPDIR/cells.py
```

```
287:    pos = sorted({i for v in roi_sets(p, "c", "ii", S["channels"]).values() for i in v})
301:    pos = sorted({i for v in roi_sets(p, "c", "ii", S["channels"]).values() for i in v})
699:                pos = sorted({i for v in roi_sets(p, o5, dr, S["channels"]).values() for i in v})
print("Leave-one-day-out: trained on the participant's other days, tested on one day (high gamma, all ROI electrodes):")
for p in ["01", "04"]:
  for d in sorted(set(SAMPLES[("a-ii", p)]["day"])):
    S = SAMPLES[("a-ii", p)]
    pos = sorted({i for v in roi_sets(p, "c", "ii", S["channels"]).values() for i in v})
    tr = np.where((S["day"] != d) & np.isin(S["cls"], ["Talk", "TV"]))[0]
    te = np.where((S["day"] == d) & np.isin(S["cls"], ["Talk", "TV"]))[0]
    if min((S["cls"][te] == c).sum() for c in ["Talk", "TV"]) < 5:
        print("  participant %s day %d: fewer than 5 bins of a class" % (p, d))
        continue
    tr, te = A.balance(tr, S["cls"], rng), A.balance(te, S["cls"], rng)
    F = S["X"][:, pos, 4].astype(float)
    pred, _, _ = A.lda2(A.zscore(F[tr]), S["cls"][tr] == "Talk", A.zscore(F[te]))
    acc = (pred == (S["cls"][te] == "Talk")).mean()
    print("  participant %s day %d%s: %d balanced bins, accuracy %.3f (finite chance at 0.05: %.3f)"
          % (p, d, " (offset applied)" if (p, d) in [("01", 7), ("04", 3)] else "", len(te), acc, A.finite_chance(len(te), 2, 0.05)))
print("Without the offset, %d and %d of the class blocks of these two files lie past the end of the ECoG."
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; python $TMPDIR/runcells.py > $TMPDIR/out2.txt 2>&1; grep -n "FAILED" $TMPDIR/out2.txt; sed -n '/===== sanity/,/===== samples/p' $TMPDIR/out2.txt | tail -22; sed -n '/===== clock/,/-----/p' $TMPDIR/out2.txt; grep -n "criterion met\|readings meeting\|main\b\|main:" $TMPDIR/out2.txt | head -80; date -u
```

```
('01', 7) first epoch that is not a data break starts at 30694.4 s; offset 30682.4 s; ECoG starts at 0 s of its own clock
('04', 3) first epoch that is not a data break starts at 49079.8 s; offset 30048.3 s; ECoG starts at 0 s of its own clock

Units: ElectricalSeries stored in volts with conversion 1e-06 -> values are microvolts
Sampling rate (all files): [500.0]
Block durations, s: min 0.1, median 119.9, max 482.4, n 3465; outside 110 to 130 s: 110; shorter than 10 s (no bin): 38

SD column of the electrodes table against the RMS of the class blocks (median ratio RMS / SD per file):
  01 [1.02 0.96 0.94 1.  ]
  02 [0.96 0.96 0.87 0.9 ]
  04 [0.98 0.99 0.93 0.93 0.93]
  05 [0.96 0.93 0.84]
  08 [1.05 0.86 0.79 0.85 0.79]

Envelope check against sosfiltfilt + scipy.signal.hilbert on one block and channel:
  theta      max relative difference over 12 bins: 0.0028 (values 14.85 to 19.42 uV)
  alpha      max relative difference over 12 bins: 0.0056 (values 11.17 to 16.01 uV)
  beta       max relative difference over 12 bins: 0.0005 (values 20.03 to 24.61 uV)
  low_gamma  max relative difference over 12 bins: 0.0008 (values 6.67 to 8.24 uV)
  high_gamma max relative difference over 12 bins: 0.0005 (values 3.47 to 5.29 uV)
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate; cd entries/alasfour-2024; python - <<'EOF'
import sys; sys.path.insert(0,'.')
import ajile as A, numpy as np, pickle
META=pickle.load(open('/tmp/claude-1001/survey_ns.pkl','rb'))
assets=A.list_assets()
for p,d in [('04',3),('01',7),('01',5)]:
    m,el,ep=META[(p,d)]
    aid=assets[(assets.subject==p)&(assets.session==d)].asset_id.iloc[0]
    f,_=A.open_nwb(aid); x=f['acquisition/ElectricalSeries/data']
    off=A.epoch_offset(m); n=x.shape[0]
    brk=ep[ep.label.str.startswith('Blocklist (Data')&((ep.stop-ep.start)>300)]
    dat=ep[~ep.label.str.startswith('Blocklist')&((ep.stop-ep.start)>60)]
    for name,o in [('offset',off),('zero',0.0)]:
        res=[]
        for lab,tab in [('break',brk),('labelled',dat)]:
            vals=[]
            for a,b in list(zip(tab.start,tab.stop))[:12]:
                mid=(a+b)/2-o
                i=int(mid*500)
                if 0<=i<n-500:
                    s=x[i:i+500,0]
                    vals.append((np.isnan(s).mean(), float(np.nanstd(s)) if not np.all(np.isnan(s)) else -1))
            res.append((lab,len(vals),np.round(np.mean([v[0] for v in vals]),2) if vals else None, np.round(np.median([v[1] for v in vals]),1) if vals else None))
        print(p,d,name,res)
EOF
```

```
04 3 offset [('break', 11, np.float64(0.09), np.float64(40.7)), ('labelled', 12, np.float64(0.08), np.float64(32.9))]
04 3 zero [('break', 6, np.float64(0.0), np.float64(38.3)), ('labelled', 12, np.float64(0.0), np.float64(45.5))]
01 7 offset [('break', 0, None, None), ('labelled', 12, np.float64(0.08), np.float64(29.7))]
01 7 zero [('break', 1, np.float64(0.0), np.float64(24.2)), ('labelled', 12, np.float64(0.0), np.float64(33.9))]
01 5 offset [('break', 0, None, None), ('labelled', 12, np.float64(0.0), np.float64(24.0))]
01 5 zero [('break', 0, None, None), ('labelled', 12, np.float64(0.0), np.float64(24.0))]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n '/claim:fig3-three-class/,/claim:fig4-missing/p' out2.txt | head -40; sed -n '/claim:fig7-participant4/,/runtime/p' out2.txt | head -40; grep -n "readings where IT high\|within_tol\b" out2.txt | head -3
```

```
===== claim:fig3-three-class
band         alpha   beta  high_gamma  low_gamma  theta
participant                                            
01           0.497  0.501       0.466      0.408  0.415
02           0.463  0.469       0.547      0.516  0.510
04           0.450  0.431       0.359      0.357  0.422
05           0.412  0.417       0.521      0.537  0.436
chance (per fold, 0.05): {'01': 0.404, '02': 0.388, '04': 0.403, '05': 0.404}
            reading  above_all  above_all_001  p2_above70  p2_highest  p2_gt_p4  p2_gt_t1_5  p2_min best     ok
0   (a-ii, a-ii, a)       True           True       False        True      True        True   0.519   02  False
1   (a-ii, a-ii, b)       True           True       False        True      True        True   0.545   02  False
2    (a-ii, b-i, a)       True           True       False        True      True        True   0.549   02  False
3    (a-ii, b-i, b)       True           True       False        True      True        True   0.549   02  False
4   (a-ii, c-ii, a)      False           True       False        True      True       False   0.463   02  False
5   (a-ii, c-ii, b)      False           True       False        True      True       False   0.468   02  False
6   (b-ii, a-ii, a)       True           True       False        True      True        True   0.529   02  False
7   (b-ii, a-ii, b)       True           True       False        True      True        True   0.569   02  False
8    (b-ii, b-i, a)       True           True       False        True      True        True   0.547   02  False
9    (b-ii, b-i, b)       True           True       False       False     False        True   0.527   01  False
10  (b-ii, c-ii, a)       True           True       False        True     False        True   0.496   02  False
[... 52 more lines not kept]
```

**Agent**

Now inserting the conclusion cells and summary into the notebook source.

**Agent calls Bash**

```bash
cd $TMPDIR; cat > results.py <<'EOF'
R = {
"claim:roi-projection-link": "**Result: partially reproduced.** Four of the five matrices have one row per electrode; participant 01's has 98 rows for 94 electrodes, and an index match agrees best with no shift (0.628, against 0.394 or less when shifted). The matrix's own ROI and the ROI nearest to the dataset's mirrored position agree for 51 to 64% of electrodes (69 to 77% among electrodes the matrix puts in one of the eight ROIs), so the matrices were not computed from these positions exactly. Region claims are run with ROIs from the matrices (O5 a, c) and from the positions (O5 b).",
"claim:cohort-selection": "**Result: reproduced.** Under O2 (a), at least 1 h of each of talking and watching TV over days 3 to 7, exactly subjects 01, 02, 04, 05 and 08 qualify with single-label epochs; counting any epoch whose label includes the class adds 03 and 06; under O2 (b) all twelve qualify. Sex is not in the dataset, so the 2 male and 3 female split cannot be checked.",
"claim:table1-participants": "**Result: not reproduced.** No reading of the good-electrode count matches all five Table 1 values: the minimum over days matches 4 of 5 (05 has 100, Table 1 104), the first day 3 of 5. No artifact reading puts all 15 minute values within 10% (at most 4 of 15 under O4 a-i); without rejection or under rule (b) the minutes exceed Table 1 (01 talking 763.5 against 493), and under rule (a) they fall below it (01 talking 171.6 to 208.0). Every participant has at least 120 min of talking and watching TV under every reading. Sex and age are not in the dataset.",
"claim:fig2-highest-accuracy": "**Result: reproduced, resting on the ROI reading.** In 30 of the 96 pipelines inferior temporal high gamma has the highest of the 40 accuracies and lies within 62.1 to 75.9% (up to 0.712 with O5 b); all 30 use the electrodes as features (O6 a) and ROIs from O5 (a) or (b). Under the main reading it is second (0.613, just below the tolerance) after middle temporal high gamma (0.628).",
"claim:fig2-rois-three-bands": "**Result: reproduced, resting on the readings.** The five ROIs each have three or more significant bands in 14 of 384 readings, all with the artifact SD over the participant's days (O4 a-i) and a chance level from all test samples; at least four of the five do in 40. Under the main reading only the middle temporal lobe has three (postcentral 1, supramarginal 2, inferior temporal 2).",
"claim:fig2-inferior-temporal-all-bands": "**Result: reproduced, resting on the readings.** All five inferior temporal bands are significant in 134 of 384 readings, nearly all with the electrodes as features (O6 a); under the main reading 2 of 5 are (beta and high gamma, p = 2e-05; the others p 0.003 to 0.010 do not pass the FDR cut). 206 readings have none.",
"claim:fig2-beta-temporal-only": "**Result: reproduced, resting on the readings.** Beta is significant in exactly the middle and inferior temporal lobes in 29 of 384 readings. Under the main reading it is significant in those two and in the supramarginal gyrus; in 206 readings beta is significant nowhere.",
"claim:fig2-single-band-rois": "**Result: reproduced, resting on the readings.** Both parts hold in only 4 of 384 readings (all O5 a-i, artifact rule b, chance from all test samples); one of the two holds in 49. Under the main reading neither ROI has a significant band, and the inferior parietal lobe exists for only two participants (02, 05).",
"claim:anova-roi-band-effects": "**Result: reproduced.** Under the main reading (type II, fold accuracies) ROI F = 7.22, p = 1.7e-08 and band F = 7.18, p = 1e-05, both below 0.001; type I gives the same. Type III (p 0.32 and 0.19) and participant means (p 0.0087 and 0.028) do not. Over the grid both main effects are below 0.001 in 44 of 96 fold-level readings.",
"claim:anova-no-interaction": "**Result: reproduced, resting on an assumption** (type II sums of squares on fold accuracies, the claims file's choice). The interaction has F = 0.779 on 28 df, p = 0.789. It is not significant in 77 of 96 fold-level readings (p 0.0063 to 0.988) and in all 96 on participant means.",
"claim:posthoc-band-averages": "**Result: reproduced, resting on the readings.** The criterion holds in 12 of 768 readings. Under the main reading high gamma is highest (0.580, within tolerance) and beta (0.549) is within tolerance and above the chance level 0.520, but theta (0.538) and alpha (0.541) are lower than beta, so the order fails. High gamma is the top band in 728 of 768 readings; beta is the bottom band in 136.",
"claim:posthoc-roi-averages": "**Result: reproduced, resting on the readings.** The criterion holds in 64 of 384 readings. Under the main reading middle frontal is lowest (0.516, within tolerance) and inferior temporal highest (0.582, below the 59.4% bound) but significantly different from only 3 of 7 ROIs. The inferior temporal lobe is the top ROI in 200 readings and differs from all seven in 112.",
"claim:fig3-three-class": "**Result: partially reproduced.** In 10 of 12 readings every participant is above its per-fold finite chance level in every band (main reading: participant 04 falls below it in low and high gamma, 0.357 and 0.359 against 0.403). Participant 02 is highest in 11 of 12 and above participant 04 in every band in 9, but its lowest band never exceeds 70% (0.463 to 0.549).",
"claim:fig4-not-single-participant": "**Result: reproduced, resting on the reading of participant-level significance.** Under O13 (b), mean fold accuracy above the participant's finite chance level, every participant has many features above chance (medians 17.5 to 26 per participant) in all 192 such readings. Under O13 (a), a t-test of the 7 fold accuracies with FDR, at most participant 02 has 1 or 2, so the claim fails there.",
"claim:fig4-missing-rois": "**Result: partially reproduced.** Participants 02 and 04 (figure 2 and 3 under O1 a) lack at least one ROI under every ROI reading, but so do 08 (inferior parietal) under all six and 01 under five, so no reading has exactly those two.",
"claim:fig4-participant2-high": "**Result: partially reproduced.** Participant 02 has the highest mean accuracy under the main reading (0.607) and in 62 of 96 pipelines, with 2 to 7 features above 75%; the first two parts and inferior temporal gamma above 75% hold together in 44 pipelines, but both inferior temporal gamma values exceed 80% in none (at most 0.800).",
"claim:fig5-gamma-higher-talking": "**Result: reproduced, resting on the readings.** In 68 of 384 readings every consistent gamma feature is positive and both gamma bands have one. Under the main reading only postcentral low gamma is consistent (+0.196). Where any consistent gamma feature exists, the median share positive is 1.00.",
"claim:fig5-theta-alpha-lower-talking": "**Result: reproduced, resting on the readings.** In 30 of 384 readings, all with O4 a-i, every consistent theta and alpha feature is negative and both bands have one; under the main reading none is consistent, though the mean differences of alpha are negative in all eight ROIs.",
"claim:fig5-pre-postcentral": "**Result: reproduced, resting on the readings.** Both parts hold in 2 of 384 readings. The largest absolute difference is in the pre- or postcentral gyrus in 348 readings, but the eight features are consistent with the expected signs in only 6 readings (6 or more in 11). Under the main reading the largest difference is middle frontal low gamma (+0.202) and 1 of the 8 is consistent.",
"claim:fig5-parietal-temporal-no-gamma": "**Result: partially reproduced.** No gamma feature of the three ROIs is a consistent increase in 352 of 384 readings (main reading included), but theta or alpha is consistent in all three ROIs in no reading; in two of the three in 22. Under the main reading the alpha differences are negative there (-0.098 to -0.155) without passing the FDR cut.",
"claim:fig5-middle-temporal-tv": "**Result: partially reproduced.** Four middle temporal bands consistent with a negative difference occur in no reading; three occur in 19 of 384. Under the main reading none is consistent (no middle temporal band passes the accuracy test, while alpha and beta have p = 0.007 and 0.008 for the mean difference).",
"claim:inferior-temporal-high-gamma-inconsistent": "**Result: reproduced.** Under the main reading inferior temporal high gamma is significant for accuracy (0.613, p = 2.4e-05) and its mean difference (0.032, 95% CI -0.059 to 0.122, p = 0.48) is not; its absolute difference ranks 33 of 40. The mean difference is not significant in any of the 384 readings.",
"claim:all-rois-but-inferior-parietal": "**Result: reproduced, resting on the readings.** It holds in 2 of 384 readings (and six of seven in 10); in 250 readings no ROI has a consistent band, and under the main reading only the postcentral gyrus does.",
"claim:fig6-sign-consistency": "**Result: reproduced, resting on the readings.** 8 to 10 combinations share a sign in 49 of 192 readings (counts range 0 to 14). Under the main reading O14 (a) gives 7 and O14 (b) gives 2.",
"claim:fig6-examples": "**Result: partially reproduced.** All six named combinations never share a sign in one reading; 4 or 5 do in 44 of 192 (main reading 4 under O14 a). Precentral high gamma fails through participant 08 (-0.054) and supramarginal alpha through participants 02 and 04.",
"claim:fig7-non-additive": "**Result: reproduced, resting on the reading of additive.** Under reading (b) at most 5 of 25 curves are additive in 36 of 48 readings (main reading: 8). Under reading (a) all ROIs beat the top ROI in 22 of 25 curves under the main reading, and at most 5 in only 2 readings.",
"claim:fig7-participant4-low-gamma": "**Result: partially reproduced.** Figure participant 4's low gamma curve never has the largest gain of the 25; it is among the three largest in 5 of 96 readings. Under the main reading it ranks 9 (O1 a) or 21 (O1 b), and the largest gain is participant 02's low gamma (0.159).",
"claim:fig7-above-70": "**Result: partially reproduced.** Four participants exceed 70% in 18 of 96 readings and all five in 2, where figure participant 4 is not the highest or not near 80%; under the main reading two do (02 0.798, 05 0.714). Best accuracies range 0.546 to 0.722 (01), 0.625 to 0.882 (02), 0.592 to 0.735 (04), 0.626 to 0.766 (05), 0.558 to 0.703 (08).",
"claim:discussion-above-80": "**Result: partially reproduced.** At most one participant (02) exceeds 80% in any reading (31 of 48; maximum 0.882); three never do.",
"claim:fig7-exceeds-group": "**Result: reproduced.** Under reading (a) at least four of five participants' best curve accuracies exceed the highest participant-wide accuracy in 39 of 48 readings (main: 4 of 5, against 0.628), and under reading (b) more than half of the curves exceed the participant-wide accuracy of their band in their top ROI in all 48 (main: 20 and 25 of 25).",
"claim:fig7-best-band-varies": "**Result: partially reproduced.** The best band does vary (two to four distinct best bands over participants), but participant 08's best band is never theta when 04's is alpha; one of the two holds in 16 of 48 readings (main O15 a: 04 alpha, 08 alpha).",
}
EOF
python3 - <<'EOF'
import re
exec(open('/tmp/claude-1001/results.py').read())
s=open('/tmp/claude-1001/cells.py').read()
# drop prewritten result cells
s=re.sub(r'# %% \[markdown\]\n# \*\*Result:.*?(?=\n# %% )', '', s, flags=re.S)
parts=re.split(r'(?=^# %% )', s, flags=re.M)
out=[]
for p in parts:
    out.append(p)
    m=re.match(r'# %% tags=\["([^"]+)"\]', p)
    if m and m.group(1) in R:
        txt=R[m.group(1)]
        import textwrap
        md='\n'.join('# '+l for l in textwrap.wrap(txt,100))
        out.append('# %% [markdown]\n'+md+'\n\n')
s=''.join(out)
summary='''# %% [markdown]
# ## Summary
#
# | Claim | Outcome |
# |---|---|
'''
oc={"roi-projection-link":"partially reproduced","cohort-selection":"reproduced","table1-participants":"not reproduced",
"fig2-highest-accuracy":"reproduced (assumed)","fig2-rois-three-bands":"reproduced (assumed)","fig2-inferior-temporal-all-bands":"reproduced (assumed)",
"fig2-beta-temporal-only":"reproduced (assumed)","fig2-single-band-rois":"reproduced (assumed)","anova-roi-band-effects":"reproduced",
"anova-no-interaction":"reproduced (assumed)","posthoc-band-averages":"reproduced (assumed)","posthoc-roi-averages":"reproduced (assumed)",
"fig3-three-class":"partially reproduced","fig4-not-single-participant":"reproduced (assumed)","fig4-missing-rois":"partially reproduced",
"fig4-participant2-high":"partially reproduced","fig5-gamma-higher-talking":"reproduced (assumed)","fig5-theta-alpha-lower-talking":"reproduced (assumed)",
"fig5-pre-postcentral":"reproduced (assumed)","fig5-parietal-temporal-no-gamma":"partially reproduced","fig5-middle-temporal-tv":"partially reproduced",
"inferior-temporal-high-gamma-inconsistent":"reproduced","all-rois-but-inferior-parietal":"reproduced (assumed)","fig6-sign-consistency":"reproduced (assumed)",
"fig6-examples":"partially reproduced","fig7-non-additive":"reproduced (assumed)","fig7-participant4-low-gamma":"partially reproduced",
"fig7-above-70":"partially reproduced","discussion-above-80":"partially reproduced","fig7-exceeds-group":"reproduced","fig7-best-band-varies":"partially reproduced"}
for k,v in oc.items(): summary+='# | %s | %s |\n'%(k,v)
summary+='''#
# "Assumed" marks an outcome that holds under some of the readings the claims file names (its
# criteria say "under one reading") but not under all, or that rests on a choice the paper does not
# make. Many of these hold in a small share of the readings; each section gives the count.
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
# and the differences from the paper's method.
#
# How the analysis differs from the paper's: the paper's code is not available, so the folds, the
# buffer, the chance level, the ROI assignment, the artifact rule's details and the feature of an ROI
# are run under the readings the claims file names; the analysed electrodes are those good on every
# day; blocks with two or more labels are left out; the Butterworth order (4) and zero phase are a
# standard choice, applied in the frequency domain.
#
# What was found about the dataset: in two files (sub-01 ses-7, sub-04 ses-3) the epochs are timed
# from 19:00 while the ECoG starts at 03:31 and 03:20, so 223 and 77 labelled blocks lie past the end
# of the ECoG unless an offset is applied; with it, sub-01 ses-7 decodes like the other days but
# sub-04 ses-3 does not (0.460), so its clock is not established. The good-electrode flags change from
# day to day. The files hold no sex or age. 110 of the 3465 class epochs are not about 2 min long
# (0.1 to 482 s). The projection matrices agree with the dataset's electrode positions for only about
# 60% of electrodes, and participant 01's has four rows more than the dataset has electrodes.

'''
i=s.find('# %% tags=["runtime"]')
s=s[:i]+summary+s[i:]
open('/tmp/claude-1001/cells.py','w').write(s)
EOF
grep -c "Result:" cells.py; date -u
```

```
31
Tue Nov 10 05:02:36 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; awk '/claim:fig2-highest-accuracy/,/fig2-significance/' out2.txt | grep "True        True" | awk '{print $2,$3,$4,$5,$6}' | sort | uniq -c | head -40; awk '/claim:fig2-highest-accuracy/,/fig2-significance/' out2.txt | grep "True        True" | awk '{print $(NF-2)}' | sort -n | tail -1; sed -n '/claim:fig5-middle-temporal-tv/,/-----/p' out2.txt | head -12; python3 - <<'EOF'
EOF
```

```
1 (a-i, a, i, a, a)
      1 (a-i, a, i, a, b)
      1 (a-i, a, ii, a, a)
      1 (a-i, a, ii, a, b)
      1 (a-i, b, i, a, a)
      1 (a-i, b, i, a, b)
      1 (a-i, b, ii, a, a)
      1 (a-i, b, ii, a, b)
      1 (a-ii, a, i, a, b)
      1 (a-ii, a, ii, a, b)
      1 (a-ii, b, i, a, a)
      1 (a-ii, b, i, a, b)
      1 (a-ii, b, ii, a, a)
      1 (a-ii, b, ii, a, b)
      1 (b-i, a, i, a, a)
      1 (b-i, a, i, a, b)
      1 (b-i, a, ii, a, a)
      1 (b-i, a, ii, a, b)
      1 (b-i, b, i, a, a)
      1 (b-i, b, i, a, b)
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
s=open('cells.py').read()
reps=[("1. Under the main reading it is second","1. Under the main reading it is second"),
("(up to 0.712 with O5 b); all 30 use the electrodes as features (O6 a) and ROIs from O5 (a) or (b).","(0.705 to 0.730); all 30 use the electrodes as features (O6 a) and ROIs from O5 (a) or (b)."),
("readings, nearly all with the electrodes as features (O6 a)","readings, all with the electrodes as features (O6 a)"),
("(0.463 to 0.549)","(0.463 to 0.569)"),
("Under O13 (a), a t-test of the 7 fold accuracies with FDR, at most participant 02 has 1 or 2, so the claim fails there.","Under O13 (a), a t-test of the 7 fold accuracies with FDR, the median count is 0 to 2 per participant, so the claim fails there."),
("with 2 to 7 features above 75%;","with up to 7 features above 75% (2 under the main reading);"),
("(no middle temporal band passes the accuracy test, while alpha and beta have p = 0.007 and 0.008 for the mean difference)","(beta, low and high gamma pass the accuracy test; the mean differences of alpha and beta, -0.107 and -0.106 with p = 0.007 and 0.008, do not pass the FDR cut)"),
("(two to four distinct best bands over participants)","(two distinct best bands under the main reading)"),
]
import re
for a,b in reps:
    # results are wrapped; normalise by searching in unwrapped text of results.py instead
    pass
r=open('results.py').read()
for a,b in reps:
    if a in r: r=r.replace(a,b)
    else: print('miss',a[:40])
open('results.py','w').write(r)
EOF
grep -c "0.705 to 0.730" results.py
```

```
miss 1. Under the main reading it is second
1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import re, textwrap
exec(open('/tmp/claude-1001/results.py').read())
s=open('/tmp/claude-1001/cells.py').read()
s=re.sub(r'# %% \[markdown\]\n# \*\*Result:.*?(?=^# %% )', '', s, flags=re.S|re.M)
parts=re.split(r'(?=^# %% )', s, flags=re.M)
out=[]
for p in parts:
    out.append(p)
    m=re.match(r'# %% tags=\["([^"]+)"\]', p)
    if m and m.group(1) in R:
        out.append('# %% [markdown]\n'+'\n'.join('# '+l for l in textwrap.wrap(R[m.group(1)],100))+'\n\n')
s=''.join(out)
open('/tmp/claude-1001/cells.py','w').write(s)
# build notebook
import json
cells=[]
for p in re.split(r'(?=^# %% )', s, flags=re.M):
    if not p.strip() or not p.startswith('# %%'): continue
    head,_,body=p.partition('\n')
    body=body.rstrip('\n')
    if '[markdown]' in head:
        src='\n'.join(l[2:] if l.startswith('# ') else l.lstrip('#') for l in body.split('\n'))
        cells.append(dict(cell_type='markdown',metadata={},source=src.strip('\n').splitlines(True)))
    else:
        tags=re.findall(r'"([^"]+)"',head)
        cells.append(dict(cell_type='code',metadata={'tags':tags},source=body.strip('\n').splitlines(True),outputs=[],execution_count=None))
nb=dict(cells=cells,metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},'language_info':{'name':'python'}},nbformat=4,nbformat_minor=5)
json.dump(nb,open('entries/alasfour-2024/reproduce_alasfour_2024.ipynb','w'),indent=1)
print(len(cells),'cells', sum(c['cell_type']=='markdown' and any('Result:' in l for l in c['source']) for c in cells),'result cells')
EOF
grep -n "Result" -c entries/alasfour-2024/reproduce_alasfour_2024.ipynb 2>/dev/null; cd  grep -n "Result" entries/alasfour-2024/reproduce_alasfour_2024.ipynb | head -3; sed -n '1,80p' tools/entry.py | head -80
```

```
114 cells 31 result cells
468:    "**Result: partially reproduced.** Four of the five matrices have one row per electrode; participant\n",
524:    "**Result: reproduced.** Under O2 (a), at least 1 h of each of talking and watching TV over days 3 to\n",
587:    "**Result: not reproduced.** No reading of the good-electrode count matches all five Table 1 values:\n",
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

[... 65 more lines not kept]
```

**Agent**

Notebook built (114 cells). Writing `entry.yaml`, `requirements.in` and README, then lock and run.

**Agent calls Bash**

```bash
cd entries/alasfour-2024; cat > requirements.in <<'EOF'
h5py
matplotlib
numpy
pandas
remfile
requests
scikit-learn
scipy
statsmodels
EOF
grep -n "matplotlib\|import" ajile.py | head -20; cat > entry.yaml <<'EOF'
schema_version: 1
name: alasfour-2024
type: reproduction
title: Spectro-spatial decoding of talking and watching TV in AJILE12 (Alasfour and Gilja 2024)
description: Tests the findings of Alasfour and Gilja (2024) on dandiset 000055 (AJILE12), which holds
  the ECoG, electrode positions and annotated 2-min behaviour blocks of the paper's five participants.
  It streams the talking, watching TV and using electronics blocks, computes band envelopes in 10-s
  bins, and repeats the per-ROI and per-band LDA decoding, the mean-difference consistency analysis,
  the three-class decoding and the ROI-adding analysis under the readings the claims file names. The
  electrode-to-ROI projection matrices come from Figshare.
license: Apache-2.0
notebooks:
- path: reproduce_alasfour_2024.ipynb
  title: Reproducing Alasfour and Gilja (2024) from dandiset 000055
  runtime_minutes: 25
helpers:
- ajile.py
related:
- id: dandi:000055/0.220127.0436
  relation: uses_data
- id: doi:10.3389/fnhum.2024.1388267
  relation: reproduces
- id: doi:10.6084/m9.figshare.12114408.v1
  relation: uses_data
EOF
sed -i '/^matplotlib$/d' requirements.in; cat requirements.in; python3 -c "import json;print(json.load(open('schemas/entry.schema.json'))['properties']['related'])" | head -20
```

```
25:import io
26:import struct
27:import threading
28:import time
29:import zlib
30:from concurrent.futures import ThreadPoolExecutor
32:import h5py
33:import numpy as np
34:import pandas as pd
35:import remfile
36:import requests
37:import scipy.fft as sfft
38:from requests.adapters import HTTPAdapter
39:from scipy import signal, stats
453:    import hashlib
501:    from multiprocessing import Pool
535:    from multiprocessing import get_context
h5py
numpy
pandas
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/entry.py lock entries/alasfour-2024 2>&1 | tail -5; python tools/entry.py check entries/alasfour-2024 2>&1 | tail -20
```

```
wrote alasfour-2024/requirements.lock.txt (Python 3.13, with hashes)
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
0 error(s)
```

**Agent calls Bash**

```bash
cd  python3 -c "
import nbformat
p='entries/alasfour-2024/reproduce_alasfour_2024.ipynb'
nb=nbformat.read(p,4); _,nb=nbformat.validator.normalize(nb); nb=nbformat.from_dict(nb); nbformat.write(nb,p)
"; date -u; time python tools/entry.py all entries/alasfour-2024 2>&1 | tail -15; date -u
```

```
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
Tue Nov 10 05:04:06 UTC 2026
Installed kernelspec registry-alasfour-2024 in executed/alasfour-2024/.venv/share/jupyter/kernels/registry-alasfour-2024
0 error(s)
pass  reproduce_alasfour_2024.ipynb  (1280 s)

real	21m29.324s
user	58m51.343s
sys	7m27.544s
Tue Nov 10 05:25:35 UTC 2026
```

**Agent**

The notebook ran clean in 21 min. Checking the executed outputs against the conclusions.

**Agent calls Bash**

```bash
cd  ls executed/alasfour-2024/; python3 - > $TMPDIR/exec.txt <<'EOF'
import nbformat
nb=nbformat.read('executed/alasfour-2024/reproduce_alasfour_2024.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code':
        print('=====',c.metadata.get('tags'))
        for o in c.get('outputs',[]):
            if o.output_type=='stream': print(o.text)
            elif o.output_type=='error': print('ERROR',o.ename,o.evalue)
            elif 'text/plain' in o.get('data',{}): print(o['data']['text/plain'])
EOF
diff <(grep -v "^-----\|^=====" $TMPDIR/out2.txt | grep -v "s$" ) <(grep -v "^=====" $TMPDIR/exec.txt) | head -60
```

```
reproduce_alasfour_2024.ipynb
result.json
14a15
> 
50a52,54
> 
> extracted 3465 blocks from 21 files, 89.1 GB read, in 16.1 min
> 
51a56
> 
78a84
> Units: ElectricalSeries stored in volts with conversion 1e-06 -> values are microvolts
89a96
> 
94a102,103
> 
>    artifact participant  channels  blocks_kept  blocks_artifact  blocks_outside  bins_nan_dropped  Talk    TV  Electronics
114a124,125
> 
> 96 pipelines, 384 readings with the chance levels; 85 s
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; awk '/claim:fig2-highest-accuracy/,/fig2-significance/' exec.txt | grep "True *True$" | sed 's/.*high_gamma) *//' | awk '{print $1}' | sort -n | sed -n '1p;$p'; grep -n "discussion-above-80" -A8 exec.txt | head -12; date -u
```

```
0.695
0.730
801:===== ['claim:discussion-above-80']
802-               reading O15  n_above80   max_any     01     02     04     05     08
803-0  (a-ii, c, ii, a, a)   a          0  0.798242  0.641  0.798  0.642  0.714  0.638
804-1  (a-ii, c, ii, a, a)   b          1  0.819866  0.659  0.820  0.644  0.735  0.657
805-participants above 80% over readings: {0: 17, 1: 31} | max 0.882
806-
807-/tmp/claude-1001/ipykernel_69/3114865837.py:5: Pandas4Warning: Starting with pandas version 4.0 all arguments of max will be keyword-only.
808-  top = pd.concat([f4, f7], axis=1).max(1)
809-
Tue Nov 10 05:25:57 UTC 2026
Shell cwd was reset to
```

**Agent**

Range is 0.695–0.730; fixing that text and one unverified "(02)". Then the link claim goes into the claims file (protocol step 1.4) and I write the record.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import nbformat
for p in ['entries/alasfour-2024/reproduce_alasfour_2024.ipynb','executed/alasfour-2024/reproduce_alasfour_2024.ipynb']:
    nb=nbformat.read(p,4); n=0
    for c in nb.cells:
        if c.cell_type=='markdown':
            s=c.source
            s2=s.replace('(0.705 to 0.730)','(0.695 to 0.730)').replace('At most one participant (02) exceeds','At most one participant exceeds')
            if s2!=s: c.source=s2; n+=1
    nbformat.write(nb,p); print(p,n)
EOF
python3 -c "
import json; s=json.load(open('schemas/claims.schema.json'))
c=s['properties']['claims']['items']; print(list(c['properties'].keys())); print(c['properties'].get('kind')); print(c.get('required'))"
```

```
entries/alasfour-2024/reproduce_alasfour_2024.ipynb 2
executed/alasfour-2024/reproduce_alasfour_2024.ipynb 2
['id', 'statement', 'source', 'kind', 'quote', 'inferred', 'expected', 'statistics', 'criterion', 'depends_on', 'data', 'where', 'datasets']
{'description': "A finding the paper reports (`finding`, the default), or a check the registry adds that the dataset is the data the paper's outside material describes (`link`: the paper's tables, source data, code or deposits). Links are not findings of the paper and are counted apart from them.", 'enum': ['finding', 'link']}
['id', 'statement', 'source']
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import re
p='claims/alasfour-2024.yaml'
s=open(p).read()
head,sep,rest=s.partition('\nclaims:\n')
body,sep2,checks=rest.partition('\nchecks:\n')
blocks=re.split(r'(?=^- id: )', body, flags=re.M)
out=[]
for b in blocks:
    if '  data: with_inputs\n' in b:
        if '  depends_on:\n' in b:
            b=b.replace('  depends_on:\n','  depends_on:\n  - roi-projection-link\n',1)
        else:
            b=b.replace('  data: with_inputs\n','  data: with_inputs\n  depends_on:\n  - roi-projection-link\n',1)
    out.append(b)
link='''- id: roi-projection-link
  kind: link
  statement: The electrode-to-ROI projection matrices of Peterson et al. (2021a), Figshare
    10.6084/m9.figshare.12114408.v1, belong to the dataset's electrodes, one row per electrode in
    the order of the electrodes table, and their Gaussian weights agree with the dataset's electrode
    positions.
  source: Methods, 2.1 Data preprocessing, paragraph 3
  quote: The spatial locations of the electrodes across the cortical surface were determined using
    the electrode-to-region of interest (ROI) projection matrices used in a previous study that
    analyzed the AJILE12 dataset from the same authors
  data: with_inputs
  criterion: Added by the author (protocol, author step 1.4). Rows are matched to electrodes by index.
    Reproduced when every participant's matrix has one row per electrode and the matrix's own ROI
    (largest Gaussian value over the left AAL regions) is the ROI nearest to the dataset's position
    mirrored to the left hemisphere for at least 90% of electrodes; partially reproduced when the
    row counts match for most participants or the ROIs agree for at least half of the electrodes;
    not reproduced otherwise.
'''
body=''.join(out).rstrip('\n')+'\n'+link.rstrip('\n')
s=head+sep+body+sep2+checks
open(p,'w').write(s)
EOF
grep -c "roi-projection-link" claims/alasfour-2024.yaml; python3 -c "import yaml;d=yaml.safe_load(open('claims/alasfour-2024.yaml'));print(len(d['claims']))"
```

```
29
31
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required')); 
for k,v in s['properties'].items(): print(k, str(v)[:300])
" | head -60
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
schema_version {'const': 3}
id {'type': 'string', 'pattern': '^[a-z0-9]+(-[a-z0-9]+)*$'}
datasets {'description': 'Every dataset the attempt used (docs/protocol.md, "Record the attempt").', 'type': 'array', 'minItems': 1, 'items': {'description': "A dataset the attempt used: the archive, the dataset's identifier there, the pinned version, and how the paper relates to it.", 'type': 'object', 'add
missing_datasets {'description': "Datasets the paper's claims rest on that this attempt could not use; claims that need one are blocked with dataset_missing.", 'type': 'array', 'items': {'type': 'object', 'additionalProperties': False, 'required': ['why'], 'properties': {'archive': {'type': 'string'}, 'id': {'type':
paper {'type': 'string', 'pattern': '^doi:10\\.[0-9]{4,9}/.+$'}
date {'type': 'string', 'format': 'date'}
entry {'description': 'The entry this attempt produced (its name), if any.', 'type': 'string'}
deprecated {'description': "Set when the attempt no longer stands, for example because its claims were written without the paper's full text. The record is kept as it was; its outcomes are shown but not counted.", 'type': 'object', 'additionalProperties': False, 'required': ['date', 'reason'], 'properties': {'
provenance {'type': 'object', 'additionalProperties': False, 'required': ['kind', 'accountable'], 'properties': {'kind': {'enum': ['agent', 'person']}, 'accountable': {'description': 'The person or organisation responsible for this attempt.', 'type': 'object', 'additionalProperties': False, 'required': ['name'
outcomes {'description': 'One per claim attempted.', 'type': 'array', 'minItems': 1, 'items': {'type': 'object', 'additionalProperties': False, 'required': ['claim', 'outcome'], 'properties': {'claim': {'description': "Claim id from the target's claims file.", 'type': 'string'}, 'outcome': {'enum': ['reprodu
verifications {'type': 'array', 'items': {'type': 'object', 'additio
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json; s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['properties']['outcomes']['items']['properties'],indent=0)[:2500]); print(json.dumps(s['properties']['provenance'],indent=0)[:1500]); print(json.dumps(s['properties']['findings']['items']['properties'],indent=0)[:800])"
```

```
{
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
},
"blocked_by": {
"description": "Required when outcome is blocked.",
"enum": [
"data_missing",
"metadata_insufficient",
"methods_underspecified",
[... 187 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n "bins_nan\|a-ii *0[1-8]" exec.txt | head -8; grep -n "it_hg_highest" -A3 exec.txt | head -5
```

```
109:   artifact participant  channels  blocks_kept  blocks_artifact  blocks_outside  bins_nan_dropped  Talk    TV  Electronics
110:0      a-ii          01        85          303              877               0               312   795  1771          567
111:1      a-ii          02        79          307              176               0               182  1550  1365          402
112:2      a-ii          04        58          677              311               0               871  3765  1614         1046
113:3      a-ii          05        99          341              221               0                11  1545  1699          637
114:4      a-ii          08        68          236               16               0                73  1445  1062          199
216:5      a-ii          01   171.6   323.9        105.9      493    False    605  False             291           False               0            True
217:6      a-ii          02   288.2   252.8         69.8      331    False    338  False              68            True               1            True
259:                reading                             best  best_acc  it_hg  it_hg_highest  within_tol
260-0   (a-ii, c, ii, a, a)    (middle temporal, high_gamma)     0.628  0.613          False       False
261-1   (a-ii, c, ii, a, b)    (middle temporal, high_gamma)     0.626  0.625          False        True
262-2   (a-ii, c, ii, b, a)   (inferior parietal, low_gamma)     0.556  0.480          False       False
Shell cwd was reset to
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/rec; cat > $TMPDIR/rec/gen.py <<'EOF'
import yaml
NB = "reproduce_alasfour_2024.ipynb"
COMMON = [
    "The paper links no code; every open detail is run under the readings the claims file names (O4 artifact rule and SD, O5 ROI assignment and density, O6 ROI feature, O7 buffer, O9 chance level), a grid of 96 pipelines by 4 chance levels. The outcome follows the criterion, which accepts a match under one reading; the notes give how many readings match and the result under the main reading.",
    "Main reading, an assumption of this attempt: O4 (a) with the day's SD (the electrodes table's standard_deviation column), O5 reading (c), O5 density (ii), O6 (a), O7 (a), and O9 alpha 0.05 with n all test samples of the participant (Figure 2 legend, one dashed finite chance line).",
    "O5 reading (c) is taken from Methods 2.1 (\"The projection matrices were thresholded only to include electrodes close to any of the eight defined ROIs, and the ROI label was assigned by choosing the ROI closest to each electrode\"); an electrode is kept when its largest Gaussian value over all left AAL regions is one of the eight. Electrodes are mirrored to the left hemisphere, as the matrices' left-side columns imply.",
    "Analysed electrodes are those flagged good on every day of the participant (85, 79, 58, 99, 68), an assumption; Table 1's counts match no reading of the per-day flags.",
    "Only epochs labelled with exactly one of Talk, TV or Computer/phone are used; epochs with two labels (for example Talk, TV) are left out, an assumption. 10-s bins with a missing value in an analysed electrode are dropped (312, 182, 871, 11 and 73 bins).",
    "The Butterworth filters (order 4, zero phase, the claims file's standard choice O3) and the Hilbert envelope are computed in the frequency domain on each block with 5 s of padding each side; the notebook shows they agree with sosfiltfilt and scipy.signal.hilbert within 0.6%.",
    "The epochs of sub-01 ses-7 and sub-04 ses-3 are shifted by the session start minus 19:00 (8.52 h and 8.35 h) to the ECoG clock; the clock of sub-04 ses-3 is not established (its day decodes at 0.460).",
    "Under the main artifact reading many blocks are dropped (participant 01 keeps 303 of 1180); the rule as read may differ from the paper's.",
]
def o(claim, outcome, notes, dev=None, assumed=None, measured=None, common=True, blocked_by=None):
    d = dict(claim=claim, outcome=outcome, notebook=NB, output="claim:" + claim)
    if measured is not None: d["measured"] = measured
    d["notes"] = notes
    dv = (COMMON if common else []) + (dev or [])
    if dv: d["deviations"] = dv
    if assumed is not None: d["assumed"] = assumed
    return d
OUT = [
o("roi-projection-link", "partially_reproduced",
  "Four of five matrices have one row per electrode (86, 84, 106, 92); participant 01's has 98 rows for 94 electrodes, and an index match agrees best with no row shift (ROI agreement 0.628, against 0.394 or less when shifted). The matrix's own ROI (largest Gaussian value over the left AAL regions) and the ROI nearest to the dataset's mirrored position agree for 0.628, 0.512, 0.560, 0.557 and 0.641 of electrodes (0.641 to 0.774 among electrodes the matrix assigns to the eight ROIs); log weights correlate with minus the squared distance at 0.955 to 0.959. The matrices fit these positions only roughly, so ROIs from the matrices (O5 a, c) and from the positions (O5 b) are both run. The link criterion was written by the author after the survey of the matrices.",
  common=False, dev=["Link claim added by the author (protocol, author step 1.4); its thresholds (90% for reproduced, half for partial) are the author's."]),
o("cohort-selection", "reproduced",
  "Under O2 (a), at least 60 min of each of Talk and TV over the files (days 3 to 7), exactly subjects 01, 02, 04, 05 and 08 qualify with single-label epochs (TV minutes of the others 0 to 177.6; subject 03 has 838.3 min of talking and 41.9 of TV). Counting any epoch whose label includes the class adds 03 and 06; under O2 (b) all twelve qualify. Counted before artifact rejection only, since the other participants' signals were not read. Sex is not in the dataset, so the 2 male and 3 female split cannot be checked.",
  measured=5, common=False, dev=["Minutes counted before artifact rejection only."]),
o("table1-participants", "not_reproduced",
  "Good electrodes per day are 01 [85, 91, 91, 91], 02 [85, 85, 81, 80], 04 [67, 80, 81, 82, 77], 05 [104, 104, 100], 08 [83, 82, 87, 82, 85]; Table 1 (85, 80, 67, 104, 82) matches the minimum over days for 4 of 5, the first day for 3, the electrodes good on all days for 1. Minutes before rejection exceed Table 1 (01 talking 763.5 against 493, TV 1162.6 against 605); after rejection by rule (a) they fall below it (01 talking 171.6); at most 4 of the 15 values are within 10% under any reading (O4 a-i). Talking plus TV is at least 120 min for all five under every reading. Sex and age are not in the dataset. Measured gives the minimum good count over days and the minutes before rejection.",
  measured=[85, 80, 67, 100, 82, 763.5, 1162.6, 445.6, 445.9, 439.1, 77.7, 1208.5, 415.7, 313.4, 380.6, 517.6, 230.0, 285.8, 184.5, 37.9],
  common=False, dev=["Minutes are summed epoch durations of single-label epochs inside the ECoG; epochs are not all 2 min long."]),
o("fig2-highest-accuracy", "reproduced",
  "In 30 of 96 pipelines inferior temporal high gamma has the highest of the 40 accuracies and lies within 62.1 to 75.9% (0.695 to 0.730); all 30 use O6 (a) and O5 (a) or (b). Under the main reading it is 0.613, second after middle temporal high gamma (0.628). Measured is the main reading.",
  measured=61.3, assumed=True),
o("fig2-rois-three-bands", "reproduced",
  "All five ROIs have three or more significant bands in 14 of 384 readings, all with the artifact SD pooled over the participant's days (O4 a-i) and a chance level from all test samples; at least four of the five in 40. Under the main reading postcentral 1, supramarginal 2, superior temporal 0, middle temporal 3 and inferior temporal 2. With a chance level per fold (0.565 at alpha 0.05) no feature is significant under the main pipeline.",
  assumed=True),
o("fig2-inferior-temporal-all-bands", "reproduced",
  "All five inferior temporal bands are significant in 134 of 384 readings, all with O6 (a); none are in 206. Under the main reading 2 of 5 (beta and high gamma, p = 2e-05; alpha, low gamma and theta p = 0.003, 0.006 and 0.010 do not pass the FDR cut).",
  assumed=True),
o("fig2-beta-temporal-only", "reproduced",
  "Beta is significant in exactly the middle and inferior temporal lobes in 29 of 384 readings; in those two and one other in 6; nowhere in 206. Under the main reading it is significant in the supramarginal gyrus and the middle and inferior temporal lobes.",
  assumed=True),
o("fig2-single-band-rois", "reproduced",
  "Both parts hold in 4 of 384 readings (all O5 a-i with artifact rule b and a chance level from all test samples); one of the two holds in 49. Under the main reading neither ROI has a significant band, and the inferior parietal lobe exists only for participants 02 and 05. The outcome rests on a small share of the readings.",
  assumed=True),
o("anova-roi-band-effects", "reproduced",
  "Main reading, type II on the pooled fold accuracies: ROI F = 7.22, p = 1.7e-08; band F = 7.18, p = 1e-05 (type I the same). Type III gives p = 0.32 and 0.19, and participant means give p = 0.0087 and 0.028. Over the grid both are below 0.001 in 44 of 96 fold-level readings and 59 of 192 overall.",
  assumed=True),
o("anova-no-interaction", "reproduced",
  "Main reading, type II on fold accuracies: interaction F = 0.779 on 28 df, p = 0.789; types I and III give the same p. Not significant in 77 of 96 fold-level readings (p 0.0063 to 0.988) and in all 96 on participant means (p = 1.0 under the main reading). The effect is small whichever reading.",
  assumed=True),
o("posthoc-band-averages", "reproduced",
  "The criterion holds in 12 of 768 readings (O11 by grid by chance level). Under the main reading high gamma 0.580 and beta 0.549 are both within tolerance and beta is above the chance level 0.520, but theta (0.538) and alpha (0.541) are lower than beta, so beta is not the lowest. High gamma is the top band in 728 of 768 readings; beta is the bottom band in 136. Measured is the main reading (O11 a).",
  measured=[58.0, 54.9], assumed=True),
o("posthoc-roi-averages", "reproduced",
  "The criterion holds in 64 of 384 readings. Under the main reading middle frontal is lowest (0.516) and inferior temporal highest (0.582, below the 59.4% bound, with middle temporal 0.581), and Tukey's HSD separates inferior temporal from 3 of the 7 other ROIs (pairwise t-tests also 3). Inferior temporal is the top ROI in 200 readings and differs from all seven in 112. Measured is the main reading (O11 a).",
  measured=[58.2, 51.6], assumed=True),
o("fig3-three-class", "partially_reproduced",
  "Over 12 readings (artifact a-ii, b-ii; ROI sets c-ii, a-ii, b-i; buffer a, b), every participant is above its per-fold finite chance level (0.388 to 0.404) in every band in 10; under the main reading participant 04 is below it in low and high gamma (0.357, 0.359). Participant 02 has the highest mean in 11 and exceeds participant 04 in every band in 9, but its lowest band is 0.463 to 0.569, never above 70%; its accuracies under the main reading are 0.463 to 0.547.",
  dev=["The three-class scheme is not described; it is the two-class scheme with three balanced classes, scikit-learn LDA, and chance for c = 3 (claims O16). Participants 01, 02, 04 and 05, as the criterion says. Run on 12 readings, not the whole grid."]),
o("fig4-not-single-participant", "reproduced",
  "Under O13 (b), mean fold accuracy above the participant's finite chance level, every participant has at least 2 features above chance in all 192 such readings (medians 17.5 to 26 features). Under O13 (a), a t-test of the 7 fold accuracies against chance with FDR at 0.01 per participant, medians are 0 to 2 and the claim fails. The outcome rests on O13 (b).",
  assumed=True),
o("fig4-missing-rois", "partially_reproduced",
  "Under every ROI reading participants 02 and 04 (figure 2 and 3 under O1 a) lack at least one ROI (02 precentral and middle frontal, 04 inferior parietal), but 08 lacks the inferior parietal lobe under all six readings and 01 under five, and under c-i 05 too; no reading leaves exactly 02 and 04."),
o("fig4-participant2-high", "partially_reproduced",
  "Participant 02 has the highest mean accuracy under the main reading (0.607; others 0.536 to 0.549) and in 62 of 96 pipelines, with up to 7 features above 75% (2 under the main reading, maximum 0.774). The first two parts with inferior temporal low and high gamma above 75% hold in 44 pipelines; both above 80% in none (at most 0.800). Under the main reading inferior temporal low and high gamma are 0.668 and 0.697."),
o("fig5-gamma-higher-talking", "reproduced",
  "In 68 of 384 readings every consistent gamma feature is positive and both gamma bands have one. Under the main reading one gamma feature is consistent, postcentral low gamma (+0.196), so the criterion fails there. In readings with consistent gamma features the median share positive is 1.00. Mean differences of gamma are positive in the precentral, middle frontal and postcentral regions under the main reading (+0.103 to +0.202).",
  assumed=True),
o("fig5-theta-alpha-lower-talking", "reproduced",
  "In 30 of 384 readings, all with O4 a-i, every consistent theta and alpha feature is negative and both bands have one. Under the main reading none is consistent, though the alpha mean differences are negative in all eight ROIs (-0.028 to -0.199).",
  assumed=True),
o("fig5-pre-postcentral", "reproduced",
  "Both parts hold in 2 of 384 readings. The largest absolute difference is in the pre- or postcentral gyrus in 348 readings; all 8 named features are consistent with the expected signs in 6 readings and at least 6 of 8 in 11. Under the main reading the largest difference is middle frontal low gamma (+0.202) and 1 of the 8 is consistent. The outcome rests on a small share of the readings.",
  assumed=True),
o("fig5-parietal-temporal-no-gamma", "partially_reproduced",
  "No gamma feature of the supramarginal gyrus, inferior parietal lobe or superior temporal lobe is a consistent increase in 352 of 384 readings, including the main one (gamma differences -0.050 to +0.050 there, all CIs spanning 0). Theta or alpha is consistent in all three ROIs in no reading, and in two of the three in 22. Under the main reading alpha differences there are -0.098 to -0.155 (p 0.006 to 0.30), not passing the FDR cut."),
o("fig5-middle-temporal-tv", "partially_reproduced",
  "Four middle temporal bands consistent with a negative difference occur in no reading; three in 19 of 384, one or two in 11, none in 354. Under the main reading beta, low and high gamma pass the accuracy test but no mean difference passes the FDR cut (alpha -0.107, p = 0.0072; beta -0.106, p = 0.0080). All five middle temporal differences are negative under the main reading. Measured is the main reading.",
  measured=0),
o("inferior-temporal-high-gamma-inconsistent", "reproduced",
  "Main reading: accuracy 0.613, significant (p = 2.4e-05); mean difference 0.032, 95% CI -0.059 to 0.122, p = 0.48, not significant; its absolute difference ranks 33 of 40 (median absolute difference 0.082). The mean difference is not significant in any of 384 readings; the accuracy is significant in 169."),
o("all-rois-but-inferior-parietal", "reproduced",
  "It holds in 2 of 384 readings, and six of seven ROIs with the inferior parietal lobe none in 10; in 250 readings no ROI has a consistent band, and under the main reading only the postcentral gyrus does. The outcome rests on a small share of the readings.",
  assumed=True),
o("fig6-sign-consistency", "reproduced",
  "8 to 10 combinations share a sign across participants in 49 of 192 readings (O14 by pipeline; counts 0 to 14). Under the main reading O14 (a) gives 7 (middle frontal high and low gamma, inferior parietal alpha, postcentral alpha and high gamma, precentral alpha and low gamma) and O14 (b) gives 2. Measured is the main reading, O14 (a).",
  measured=7, assumed=True),
o("fig6-examples", "partially_reproduced",
  "All six named combinations share a sign in no reading; 4 or 5 do in 44 of 192 (main reading 4 under O14 a, 1 under O14 b). Under the main reading precentral high gamma fails through participant 08 (-0.054) and supramarginal alpha through participants 02 (+0.124) and 04 (+0.036)."),
o("fig7-non-additive", "reproduced",
  "Under reading (b), additive when the best over k beats the top ROI by more than the 95% interval of its fold accuracies, at most 5 of 25 curves are additive in 36 of 48 readings (main reading 8). Under reading (a), all ROIs beating the top ROI, 22 of 25 are additive under the main reading and at most 5 in only 2 readings. The outcome rests on reading (b).",
  dev=["Run on the main artifact reading only, for every ROI reading, O6 and O7 (24 pipelines) under O15 (a) and (b). The validation fold of O15 (a) is the training fold nearest the test fold."], assumed=True),
o("fig7-participant4-low-gamma", "partially_reproduced",
  "Figure participant 4's low gamma curve never has the largest gain of the 25; it is among the three largest in 5 of 96 readings. Under the main reading it ranks 9 (O1 a, Table 1's 05) or 21 (O1 b, 04), and the largest gain is participant 02's low gamma (0.159).",
  dev=["As fig7-non-additive."], assumed=True),
o("fig7-above-70", "partially_reproduced",
  "Four participants exceed 70% in 18 of 96 readings and all five in 2, where figure participant 4 is not both highest and within 72 to 88%. Under the main reading two do (02 0.798, 05 0.714); figure participant 4 (05 under O1 a) reaches 0.708 in low and 0.714 in high gamma. Best accuracies range 0.546 to 0.722 (01), 0.625 to 0.882 (02), 0.592 to 0.735 (04), 0.626 to 0.766 (05), 0.558 to 0.703 (08). Measured is the main reading's best of low and high gamma for 05.",
  measured=71.4, dev=["As fig7-non-additive."], assumed=True),
o("discussion-above-80", "partially_reproduced",
  "At most one participant exceeds 80% in a feature or curve point in any reading (31 of 48 readings have one; maximum 0.882); under the main reading none with O15 (a) and one (02, 0.820) with O15 (b).",
  dev=["As fig7-non-additive."], assumed=True),
o("fig7-exceeds-group", "reproduced",
  "Reading (a), each participant's best curve accuracy against the highest participant-wide accuracy: at least four of five exceed it in 39 of 48 readings (main: 4 of 5 against 0.628). Reading (b), each curve's best against the same band in its top ROI: more than 12 of 25 in all 48 (main: 20 and 25).",
  dev=["As fig7-non-additive."], assumed=True),
o("fig7-best-band-varies", "partially_reproduced",
  "The best band differs between participants (main reading, O15 a: high gamma for 01, 02 and 05, alpha for 04 and 08), but 08's best band is theta while 04's is alpha in no reading; one of the two holds in 16 of 48. Over readings 08's best band is high gamma in 27 and theta in 7; 04's is low gamma in 15 and alpha in 9.",
  dev=["As fig7-non-additive."], assumed=True),
]
FIND = [
 dict(kind="metadata_error", statement="In sub-01_ses-7 and sub-04_ses-3 the epochs table is timed from 19:00 while the ElectricalSeries starts at the session start, 03:31:22 and 03:20:48 (starting_time 0), so the epochs end at 24.0 h against 15.48 h and 15.65 h of ECoG; 223 and 77 of their Talk, TV and Computer/phone epochs lie past the end of the ECoG unless the 8.52 h and 8.35 h offset is applied. In the other 19 files of these participants both clocks start at 19:00."),
 dict(kind="other", statement="With that offset applied, sub-01 ses-7 decodes talking against watching TV like the participant's other days (0.679 against 0.592 to 0.695, trained on the other days), but sub-04 ses-3 decodes below chance (0.460 against 0.714 to 0.816 on days 4 to 6), so the alignment of its annotations with its ECoG is not established."),
 dict(kind="metadata_insufficient", statement="The files and the archive's metadata give no sex or age for the participants (the subject entries hold species and subject_id only), so Table 1's sex and age and the paper's 2 male and 3 female cannot be checked."),
 dict(kind="other", statement="The electrodes table's good flag changes from day to day (participant 04 has 67 to 82 good electrodes on its five days; 58 are good on all days), and the paper's per-participant counts (Table 1) match no single rule for combining the days."),
 dict(kind="other", statement="Of the 3465 epochs with a single Talk, TV or Computer/phone label in these participants' files, 110 are not about 2 min long (0.1 to 482.4 s; 38 are shorter than 10 s), where the dataset's documentation and the paper describe 2-min blocks."),
 dict(kind="other", statement="The ECoG holds missing values (NaN) inside some labelled blocks; 1449 10-s bins of the analysed electrodes were dropped for it (871 for participant 04)."),
 dict(kind="other", statement="The ROI projection matrices on Figshare (10.6084/m9.figshare.12114408.v1) agree only roughly with the dataset's electrode positions; their ROI and the nearest ROI by the dataset's position agree for 51 to 64% of electrodes, and participant 01's matrix has 98 rows for the dataset's 94 electrodes."),
 dict(kind="methods_unavailable", statement="Questions for the paper's authors, each a detail that changes outcomes here. (1) Which finite chance level was used (alpha, and n per fold or per participant)? With n per fold and alpha 0.05 no feature is significant here. (2) How was the artifact rule applied (total or contiguous 2 s, and the SD over which span)? As read, rule (a) drops up to 74% of a participant's blocks. (3) Which electrodes count as close to the eight ROIs, and is an ROI's density the matrix's density row or a count of electrodes? (4) Is the feature of an ROI its electrodes or their mean? (5) Which folds form the one-fold buffer? (6) Which electrodes are a participant's good electrodes when the flag changes across days? (7) Were epochs with two labels (for example Talk, TV) used? (8) How was the validation set of Figure 7 formed, and what were the ANOVA's observations and sums of squares? (9) Which numbering do the figures use for participants (the Results name a Participant 3 not in Table 1)?"),
]
rec = dict(
 schema_version=3, id="alasfour-2024-01",
 datasets=[dict(archive="dandi", id="000055", version="0.220127.0436", doi="10.48324/dandi.000055/0.220127.0436", relation="reuses")],
 paper="doi:10.3389/fnhum.2024.1388267", date="2026-11-10", entry="alasfour-2024",
 provenance=dict(kind="agent", accountable=dict(name="CatalystNeuro"),
   agent=dict(harness="Claude Code", model="claude-opus-5-5", protocol="pilot-14"),
   runner=dict(platform="GitHub Actions", url="https://github.com/catalystneuro/encore/actions/runs/42750463933")),
 inputs=[dict(what="Electrode-to-ROI projection matrices (aal_<participant>_elecs2ROI.csv, with each region's density in the first row) and the AAL region centroids (aal_01_ROIcentroids_Lside.csv) of Peterson et al. (2021a), checked against their Figshare MD5 sums.", source="doi:10.6084/m9.figshare.12114408.v1")],
 outcomes=OUT, findings=FIND)
s = yaml.safe_dump(rec, sort_keys=False, width=100, allow_unicode=True)
open('attempts/alasfour-2024-01.yaml','w').write(s)
EOF
. $TMPDIR/env/bin/activate; uv pip install -q pyyaml; python $TMPDIR/rec/gen.py; cd  grep -n "^ *[a-z_]*: [^'\"].*: " attempts/alasfour-2024-01.yaml | head; python tools/entry.py check entries/alasfour-2024 2>&1 | tail -5; date -u
```

```
Traceback (most recent call last):
  File "tools/entry.py", line 54, in <module>
    import nbformat
ModuleNotFoundError: No module named 'nbformat'
Tue Nov 10 05:28:00 UTC 2026
```

**Agent calls Bash**

```bash
cd  /usr/bin/env -u VIRTUAL_ENV PATH=/opt/hostedtoolcache/Python/3.13.18/x64/bin:/usr/bin:/bin:$HOME/.local/bin:$HOME/.cargo/bin python tools/entry.py check entries/alasfour-2024 2>&1 | grep -v Warning | tail -8; head -40 attempts/alasfour-2024-01.yaml
```

```
0 error(s)
schema_version: 3
id: alasfour-2024-01
datasets:
- archive: dandi
  id: '000055'
  version: 0.220127.0436
  doi: 10.48324/dandi.000055/0.220127.0436
  relation: reuses
paper: doi:10.3389/fnhum.2024.1388267
date: '2026-11-10'
entry: alasfour-2024
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-14
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -i 's/(2021a), checked against their Figshare MD5 sums./(2021a); the matrices are checked against their Figshare MD5 sums./' $TMPDIR/rec/gen.py; . $TMPDIR/env/bin/activate; python $TMPDIR/rec/gen.py; deactivate 2>/dev/null; cat > entries/alasfour-2024/README.md <<'EOF'
# Alasfour & Gilja (2024) from dandiset 000055 (AJILE12)

Tests the findings of [Alasfour and Gilja (2024)](https://doi.org/10.3389/fnhum.2024.1388267) on
[DANDI:000055](https://dandiarchive.org/dandiset/000055/0.220127.0436), which holds the ECoG, electrode
positions and annotated behaviour blocks of the paper's five participants (AJILE12 participants 01,
02, 04, 05 and 08). The electrode-to-ROI projection matrices come from
[Figshare](https://doi.org/10.6084/m9.figshare.12114408.v1).

| Claim | Outcome |
|---|---|
| The projection matrices belong to the dataset's electrodes (link) | Partially reproduced |
| Five of twelve participants have at least 1 h of each behaviour | Reproduced |
| Table 1: good electrodes and minutes per behaviour | Not reproduced |
| Figure 2: highest accuracy, significant bands per ROI (five claims) | Reproduced, resting on the readings |
| Two-way ANOVA: ROI and band effects, no interaction | Reproduced |
| Band and ROI averages | Reproduced, resting on the readings |
| Three-class decoding | Partially reproduced |
| Figure 4: every participant above chance | Reproduced, resting on the reading |
| Figure 4: missing ROIs; participant 2 highest | Partially reproduced |
| Figure 5: gamma higher, theta and alpha lower when talking; pre- and postcentral largest | Reproduced, resting on the readings |
| Figure 5: no gamma in parietal and superior temporal ROIs; middle temporal 4 of 5 bands | Partially reproduced |
| Inferior temporal high gamma decodes without a consistent mean difference | Reproduced |
| Every ROI but the inferior parietal has a consistent band | Reproduced, resting on the readings |
| Figure 6: 9 of 40 combinations share a sign | Reproduced, resting on the readings |
| Figure 6: the six named combinations | Partially reproduced |
| Figure 7: not additive; above group level | Reproduced (not additive resting on the reading) |
| Figure 7: participant 4 low gamma, above 70%, best bands; above 80% regularly | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper links no code, and many details are open (chance level, artifact rule, ROI assignment, ROI
feature, buffer). Every analysis runs under the grid of readings the claims file names; its criteria
accept a match under one reading, and many matches hold in a small share of them. The notebook gives,
for each claim, the result under the main reading and how many readings meet the criterion. The epochs
of two files are on a clock 8.5 h ahead of their ECoG; the offset is applied, and for sub-04 ses-3 the
alignment could not be confirmed. The attempt record is
[`attempts/alasfour-2024-01.yaml`](../../attempts/alasfour-2024-01.yaml).

- `reproduce_alasfour_2024.ipynb`: the analysis. It takes about 21 minutes, 16 of them streaming
  89 GB of the ECoG (only the labelled blocks and the good electrodes) in four processes.
- `ajile.py`: listing and streaming the files (with a parallel reader of the HDF5 chunk index),
  band envelopes in 10-s bins, the artifact rule, ROI assignment from the projection matrices, the
  cross-validated LDA and the finite chance level. Other notebooks on this dandiset can import it.
EOF
python tools/entry.py check entries/alasfour-2024 2>&1 | grep -v Warn | tail -3; python tools/entry.py handover entries/alasfour-2024 2>&1 | tail -3; ls executed/alasfour-2024/handover
```

```
0 error(s)
wrote executed/alasfour-2024/handover
ajile.py
alasfour-2024.yaml
reproduce_alasfour_2024.ipynb
```

**Agent calls Bash**

```bash
cd  grep -n "—\|rather\|\*\*[^R]" entries/alasfour-2024/README.md entries/alasfour-2024/ajile.py attempts/alasfour-2024-01.yaml | head; python3 -c "
import nbformat;nb=nbformat.read('entries/alasfour-2024/reproduce_alasfour_2024.ipynb',4)
import re
for c in nb.cells:
  if c.cell_type=='markdown':
    for m in re.findall(r'—|rather|\*\*(?!Result)[^*]+\*\*',c.source): print(repr(m))
print(all(not c.get('outputs') for c in nb.cells if c.cell_type=='code'))
"; git status --short; date -u
```

```
entries/alasfour-2024/ajile.py:10:  filtering (filtfilt) has the frequency response ``|H(f)|**2``; it is applied here in the
entries/alasfour-2024/ajile.py:266:        h2 = np.abs(h) ** 2
entries/alasfour-2024/ajile.py:348:        sumsq=(blk_raw.astype(np.float64) ** 2).sum(0),
entries/alasfour-2024/ajile.py:627:        d2 = ((q[:, None, :] - C[None]) ** 2).sum(-1)
'**0.220127.0436**'
True
 M claims/alasfour-2024.yaml
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
?? attempts/alasfour-2024-01.yaml
?? entries/alasfour-2024/
?? scripts
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for p in entries/alasfour-2024/reproduce_alasfour_2024.ipynb executed/alasfour-2024/reproduce_alasfour_2024.ipynb executed/alasfour-2024/handover/reproduce_alasfour_2024.ipynb; do sed -i 's/\*\*0.220127.0436\*\*/0.220127.0436/' $p; done; grep -c "\*\*0.2201" entries/alasfour-2024/reproduce_alasfour_2024.ipynb; python tools/entry.py check entries/alasfour-2024 2>&1 | grep -v Warn | tail -2; ls scripts | head -3; git log --oneline -1 -- scripts 2>/dev/null | head -2
```

```
0
0 error(s)
scripts
```

**Agent**

I've done steps 1 to 6 of the Author section. The entry passes `check` and ran clean from a fresh environment (`pass reproduce_alasfour_2024.ipynb (1280 s)`), the record is written, and `handover` built `executed/alasfour-2024/handover/`. Nothing is committed.

**Main caveat.** The paper gives no code and leaves many details open, so every claim runs under a grid of the readings the claims file names: 96 pipelines × 4 chance levels = 384 readings. The criteria accept a match "under one reading". Many claims marked reproduced match in only a few of the 384: fig2-single-band-rois 4, fig5-pre-postcentral 2, all-rois-but-inferior-parietal 2. Under my main reading most of them fail. The notebook and record give the count for every claim, and those outcomes carry `assumed: true`.

## 1. Outcomes (31 claims, including one link claim I added)

| Claim | Outcome |
|---|---|
| roi-projection-link | partially reproduced |
| cohort-selection | reproduced |
| table1-participants | not reproduced |
| fig2-highest-accuracy, fig2-rois-three-bands, fig2-inferior-temporal-all-bands, fig2-beta-temporal-only, fig2-single-band-rois | reproduced (assumed) |
| anova-roi-band-effects | reproduced (assumed) |
| anova-no-interaction | reproduced (assumed) |
| posthoc-band-averages, posthoc-roi-averages | reproduced (assumed) |
| fig3-three-class | partially reproduced |
| fig4-not-single-participant | reproduced (assumed) |
| fig4-missing-rois, fig4-participant2-high | partially reproduced |
| fig5-gamma-higher-talking, fig5-theta-alpha-lower-talking, fig5-pre-postcentral | reproduced (assumed) |
| fig5-parietal-temporal-no-gamma, fig5-middle-temporal-tv | partially reproduced |
| inferior-temporal-high-gamma-inconsistent | reproduced |
| all-rois-but-inferior-parietal | reproduced (assumed) |
| fig6-sign-consistency | reproduced (assumed) |
| fig6-examples | partially reproduced |
| fig7-non-additive | reproduced (assumed) |
| fig7-exceeds-group | reproduced (assumed) |
| fig7-participant4-low-gamma, fig7-above-70, discussion-above-80, fig7-best-band-varies | partially reproduced |

No claim is blocked.

## 2. Dataset, assumptions, questions

**Version.** I pinned 0.220127.0436, the only published version; the paper cites none.

**Findings about the dataset:**
- **Clock offset.** In `sub-01 ses-7` and `sub-04 ses-3` the epochs are timed from 19:00, but the ECoG starts at 03:31 and 03:20. Without correcting for this, 223 and 77 labelled blocks fall past the end of the recording. With the offset applied, `sub-01 ses-7` decodes like that participant's other days. `sub-04 ses-3` decodes at 0.460, against 0.71 to 0.82 on days 4 to 6, so its alignment is not established. I kept it in and name it in the record.
- **Good electrodes** change from day to day. Table 1's counts match no rule for combining the days.
- **No sex or age** anywhere in the files or archive metadata, so the "2 male, 3 female" part can't be checked.
- **Block lengths.** 110 of the 3,465 class epochs are not about 2 min long (0.1 to 482 s).
- **Missing values.** NaN values inside labelled blocks; 1,449 ten-second bins were dropped for this.
- **Projection matrices (Figshare).** They agree with the dataset's electrode positions for only 51 to 64% of electrodes, and participant 01's matrix has 98 rows for 94 electrodes.

**Assumptions** (all stated as deviations in the record):
- Electrodes used: those good on every day.
- Blocks used: single-label epochs only; blocks labelled e.g. "Talk, TV" are left out.
- Main reading:
  - artifact rule O4 (a) with the day's SD from the electrodes table;
  - ROI reading O5 (c), which I took from Methods 2.1 and cite;
  - density rule (ii);
  - ROI feature O6 (a) and buffer O7 (a);
  - chance level at alpha 0.05 from all of a participant's test samples, because Figure 2 draws one chance line.

Under this reading the artifact rule drops up to 74% of a participant's blocks.

**Questions for the paper's authors:** nine, recorded as a `methods_unavailable` finding (chance level, artifact rule, ROI threshold and density, ROI feature, buffer, good electrodes, multi-label blocks, Figure 7 validation set and ANOVA, participant numbering).

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. **Readings versus criteria.** Step 1.6 says the outcome is the one all readings give, or the best-supported reading as an assumption. These criteria say "under one reading". I followed the criteria, marked `assumed: true` and reported counts. With a large grid this makes "reproduced" easy to reach.
2. **`measured` value.** The rule is to record "the first reading the criterion lists", but the criteria name grids, not an ordered list. I recorded the main reading's values, which for fig2-highest-accuracy sits beside a "reproduced" outcome.
3. **Link claim.** Adding it means editing the claims file: I added `roi-projection-link` and put it in `depends_on` of every `with_inputs` claim. Its criterion was written after I had surveyed the matrices, and its notes say so.
4. **Clock check.** The protocol says to name a session whose clock can't be established, not whether to drop it. I kept `sub-04 ses-3` in.
5. **Development cache.** I cached derived features (not raw files) in `$TMPDIR` while developing; the notebook recomputes everything from the stream. The protocol is silent on this.
6. **Size of the reading grid.** There is no guidance. I ran the full grid for the two-class analyses and reduced grids for the three-class analysis (12 readings) and Figure 7 (48).
7. **Harness string.** I used "Claude Code" as the prompt gave, where the example record uses "Claude Code (GitHub Actions)".

## 4. Runtime and failures

- **Notebook:** 21 min. Of that, 16 min is streaming 89 GB in four processes, using a parallel reader of the HDF5 chunk index (h5py's own index lookup took about 200 s per file).
- **Session:** about 1 h 50 min, from 03:37 to about 05:30 UTC.
- **Failures:** my first full extraction crashed after 15 min on a block past the end of a recording, which is how the clock offset turned up. One rerun followed.
- **Other files:** the untracked dotfiles and the empty `scripts/` directory at the repo root are not from this work and were left alone.

## End of run

77 turns, 106 minutes, $7.30 at API prices, result: success.
