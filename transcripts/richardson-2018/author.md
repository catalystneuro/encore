# openneuro-ds000228 · author · run 40723326297

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; wc -l docs/protocol.md README.md docs/design.md docs/archives.md; ls claims/openneuro-ds000228 paper entries/001453-fouke-2025 claims/001453
```

```
Wed Oct 28 16:14:15 UTC 2026
  612 docs/protocol.md
  137 README.md
  271 docs/design.md
  287 docs/archives.md
 1307 total
claims/001453:
10.1016-j.cub.2025.04.027.yaml

claims/openneuro-ds000228:
10.1038-s41467-018-03399-2.yaml

entries/001453-fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt

[... 5 more lines not kept]
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
3	Version: `pilot-12`. Record this version in the attempt's provenance.
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

**Agent calls Read**

```json
{
 "file_path": "claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml"
}
```

```
1	# Claims for Richardson, Lisandrelli, Riobueno-Naylor & Saxe (2018), "Development of the social
2	# brain from age three to twelve years", Nature Communications 9, 1027,
3	# doi:10.1038/s41467-018-03399-2, on OpenNeuro dataset ds000228 ("MRI data of 3-12 year old children
4	# and adults during viewing of a short animated film"), snapshot 1.1.1
5	# (doi:10.18112/openneuro.ds000228.v1.1.1).
6	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
7	# protocol pilot-12 as stated in docs/protocol.md (Reader).
8	#
9	# Text read: the version of record (Nature Communications, open access, CC BY 4.0) as supplied
10	# under paper/ (text extracted from the PDF), with the main text, figure legends, Methods and the
11	# Supplementary Information (Supplementary Figures 1 to 8, Tables 1 to 4, Note 1). The four
12	# supplementary tables are images in the supplement PDF and are missing from the text; they were
13	# read from the PDF (pages 10 to 13), and their numbers are used below. The Peer Review File was
14	# not supplied and is not needed.
15	# Code: none linked. Code availability says the analysis code "is available from the
16	# corresponding author upon request", so no repository was read and no open detail is settled by
17	# code. The ToM behavioral battery is on OSF (https://osf.io/G5ZPV/, doi:10.17605/OSF.IO/G5ZPV).
18	#
19	# Data the paper used (Methods, Participants and fMRI sections; Supplementary Table 1).
20	# - 122 children aged 3.5 to 12 years (M 6.7, s.d. 2.3; 64 female) and 33 adults aged 18 to 39
[... 1135 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml",
 "offset": 1155
}
```

```
1155	    p: 0.08
1156	    p_relation: '>'
1157	    n: Pass 30, Fail 15
1158	  depends_on:
1159	  - rc-events
1160	  - beh-fb-groups
1161	  criterion: A claim of absence, judged on the paper's tests at p < .05, one linear regression per ToM
1162	    event, and for T03 a permutation test of the group effect (Methods, paragraph 11, R lmPerm).
1163	    Reproduced when no event shows a significant FB-group effect; not reproduced when any does.
1164	- id: rc-3yo-events
1165	  statement: Reverse correlation on the 3-year-olds alone finds 4 of the 12 adult pain events and 1 of
1166	    the 7 adult ToM events; of its 32 s of pain events 14 s fall in adult pain events and 8 s in
1167	    adult ToM event T04, and of its 8 s of ToM events 4 s fall in an adult ToM event and 4 s in
1168	    adult pain event P01.
1169	  source: Results, Reverse correlation analysis, paragraphs 4 and 5; Figure 4a (dark borders)
1170	  quote: 'identified 4 of the 12 pain events and 1 of the 7 ToM events discovered in the ... adult
1171	    sample. These events correspond to a subset of the timepoints that were identified as ToM or pain
1172	    events in 3 year olds (Pain: 14/32 s, ToM: 4/8 s)'
1173	  expected:
1174	  - quantity: 3yo pain event time
[... 254 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -80; grep -n "OpenNeuro" -A60 docs/archives.md | head -120
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
[... 148 more lines not kept]
```

**Agent**

Now list the dataset files.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
import requests, json, collections
q='{ snapshot(datasetId: "ds000228", tag: "1.1.1") { description { Name ReferencesAndLinks HowToAcknowledge } files(recursive: true) { filename size annexed directory id urls } } }'
r=requests.post("https://openneuro.org/crn/graphql",json={"query":q},timeout=120)
d=r.json()
json.dump(d,open("files.json","w"))
s=d["data"]["snapshot"]
print(s["description"])
fs=[f for f in s["files"] if not f["directory"]]
print(len(fs), sum(f["size"] for f in fs)/1e9)
c=collections.Counter()
for f in fs:
    parts=f["filename"].split("/")
    if parts[0].startswith("sub-"): c["sub/"+"/".join(parts[1:-1])+"/"+parts[-1].split("_",1)[-1]]+=1
    else: print(f["filename"], f["size"], f["urls"][0][:150])
for k,v in sorted(c.items()): print(v,k)
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'requests'
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && source dev/bin/activate && uv pip install -q requests pandas fsspec aiohttp nibabel numpy scipy statsmodels 2>&1 | tail -2; python -c "import pandas, nibabel; print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python - <<'EOF'
import requests, json, collections
q='{ snapshot(datasetId: "ds000228", tag: "1.1.1") { description { Name ReferencesAndLinks HowToAcknowledge } files(recursive: true) { filename size annexed directory id urls } } }'
r=requests.post("https://openneuro.org/crn/graphql",json={"query":q},timeout=120)
d=r.json()
json.dump(d,open("files.json","w"))
s=d["data"]["snapshot"]
print(s["description"])
fs=[f for f in s["files"] if not f["directory"]]
print(len(fs), sum(f["size"] for f in fs)/1e9)
c=collections.Counter(); sz=collections.Counter()
for f in fs:
    parts=f["filename"].split("/")
    if parts[0].startswith("sub-"):
        k="sub/"+"/".join(parts[1:-1])+"/"+parts[-1].split("_",1)[-1]; c[k]+=1; sz[k]+=f["size"]
    else: print(f["filename"], f["size"], f["id"], f["urls"][0][:160])
for k,v in sorted(c.items()): print(v,k, round(sz[k]/1e9,2))
EOF
```

```
<persisted-output>
Output too large (392.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8b06a7c9-71b7-4dbb-9b9e-9d14a5bf4835/tool-results/bepv0wi2p.txt

Preview (first 2KB):
{'Name': 'MRI data of 3-12 year old children and adults during viewing of a short animated film', 'ReferencesAndLinks': ['Richardson, H., Lisandrelli, G., Riobueno-Naylor, A., & Saxe, R. (2018). Development of the social brain from age three to twelve years. Nature communications, 9(1), 1027.', 'https://www.nature.com/articles/s41467-018-03399-2'], 'HowToAcknowledge': 'Richardson, H., Lisandrelli, G., Riobueno-Naylor, A., & Saxe, R. (2018). Development of the social brain from age three to twelve years. Nature communications, 9(1), 1027.'}
2060 22.215128736
CHANGES 453 b83ad35939cb9083805d1451e2e6fe5affe0835b https://openneuro.org/crn/datasets/ds000228/objects/b83ad35939cb9083805d1451e2e6fe5affe0835b?filename=CHANGES
README 1593 6d37c17444778fd32d906a840b2eb2ec0c36bf70 https://openneuro.org/crn/datasets/ds000228/objects/6d37c17444778fd32d906a840b2eb2ec0c36bf70?filename=README
dataset_description.json 1412 940a08748c32d0bc604d9b6174a56b675b27a8b8 https://openneuro.org/crn/datasets/ds000228/objects/940a08748c32d0bc604d9b6174a56b675b27a8b8?filename=dataset_description.json
.gitattributes 284 9033cfb3fffc6cd7fc6678ff17eddba7acb2fcd0 https://openneuro.org/crn/datasets/ds000228/objects/9033cfb3fffc6cd7fc6678ff17eddba7acb2fcd0?filename=.gitattributes
participants.json 4971 0a010b8ad59370db587afec9d0df4ad9a7bb999f https://openneuro.org/crn/datasets/ds000228/objects/0a010b8ad59370db587afec9d0df4ad9a7bb999f?filename=participants.json
participants.tsv 16041 4c6a181900081abf6f5bf6cb49b34e3a18e5798e https://openneuro.org/crn/datasets/ds000228/objects/4c6a181900081abf6f5bf6cb49b34e3a18e5798e?filename=participants.tsv
task-pixar_bold.json 887 a7997d30dece9e24eed6e0f4e1172e29cb1b1c3e https://openneuro.org/crn/datasets/ds000228/objects/a7997d30dece9e24eed6e0f4e1172e29cb
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python - <<'EOF'
import json, collections
fs=[f for f in json.load(open("files.json"))["data"]["snapshot"]["files"] if not f["directory"]]
c=collections.Counter(); sz=collections.Counter()
import re
for f in fs:
    k=re.sub(r"sub-[a-z]+\d+","sub-X",f["filename"])
    c[k]+=1; sz[k]+=f["size"]
for k,v in sorted(c.items()): print(v,k, round(sz[k]/1e6,1),"MB")
EOF
```

```
1 .datalad/.gitattributes 0.0 MB
1 .datalad/config 0.0 MB
1 .gitattributes 0.0 MB
1 CHANGES 0.0 MB
1 README 0.0 MB
1 dataset_description.json 0.0 MB
1 derivatives/README.txt 0.0 MB
1 derivatives/ROIs/AMCC_9mm_sphere_xyz.mat 0.0 MB
1 derivatives/ROIs/DMPFC_9mm_sphere_xyz.mat 0.0 MB
1 derivatives/ROIs/LInsula_9mm_sphere_xyz.mat 0.0 MB
1 derivatives/ROIs/LMFG_9mm_sphere_xyz.mat 0.0 MB
1 derivatives/ROIs/LS2_9mm_sphere_xyz.mat 0.0 MB
1 derivatives/ROIs/LTPJ_9mm_sphere_xyz.mat 0.0 MB
1 derivatives/ROIs/MMPFC_9mm_sphere_xyz.mat 0.0 MB
1 derivatives/ROIs/PC_9mm_sphere_xyz.mat 0.0 MB
1 derivatives/ROIs/RInsula_9mm_sphere_xyz.mat 0.0 MB
1 derivatives/ROIs/RMFG_9mm_sphere_xyz.mat 0.0 MB
1 derivatives/ROIs/RS2_9mm_sphere_xyz.mat 0.0 MB
1 derivatives/ROIs/RTPJ_9mm_sphere_xyz.mat 0.0 MB
1 derivatives/ROIs/VMPFC_9mm_sphere_xyz.mat 0.0 MB
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python - <<'EOF'
import json, requests
fs={f["filename"]:f for f in json.load(open("files.json"))["data"]["snapshot"]["files"] if not f["directory"]}
for n in ["README","CHANGES","dataset_description.json","derivatives/README.txt","participants.json","task-pixar_bold.json","sub-pixar001/func/sub-pixar001_task-pixar_bold.json"]:
    print("=====",n, fs[n]["id"]); print(requests.get(fs[n]["urls"][0]).text)
EOF
```

```
<persisted-output>
Output too large (326.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8b06a7c9-71b7-4dbb-9b9e-9d14a5bf4835/tool-results/b1vzg2682.txt

Preview (first 2KB):
===== README 6d37c17444778fd32d906a840b2eb2ec0c36bf70
Experiment Details
Participants watched Disney Pixar’s “Partly Cloudy” while lying in the scanner. There was no task; participants were simply instructed to lie still and watch the movie. The movie began after 10s of rest (black screen; TRs 1-5). The first 10s of the movie are the opening credits (disney castle, pixar logo; TRs 6-10). 

IPS = 168 TRs
TR = 2s
Experiment length: 5.6 minutes

Pixar Movie Reverse Correlation Events
Events defined by conducting reverse correlation analysis in two separate adult samples, using the average response in ToM brain regions (ToM events) and in the pain matrix (Pain events). Events listed are those that replicated across the two samples.  Onsets and Durations are noted in TRs (1 TR = 2s); scanner trigger = TR 1.

Event types: Theory of Mind (ToM), Physical Sensation/Pain (Pain)
TRs identified by RC analysis, as reported in Richardson et al. 2018
ToM Event Onsets; Durations 
46; 2
52; 3
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
f=/home/runner/.claude/projects/-home-runner-work-encore-encore/8b06a7c9-71b7-4dbb-9b9e-9d14a5bf4835/tool-results/b1vzg2682.txt; sed -n '/===== CHANGES/,/===== participants.json/p' $f; grep -n "=====" $f; wc -c $f
```

```
Permission for this tool use was denied. It requires approval, and this session has no approval surface — nobody can answer a permission prompt here — so it was denied automatically. The action was NOT performed; do not claim it succeeded, and do not retry it: this action, and anything else that requires approval, will be denied the same way for the rest of this session. Tell the user what was blocked and why you needed it, then continue with the parts of the task that do not require approval. What required approval: Claude requested permissions to edit /home/runner/.claude/projects/-home-runner-work-encore-encore/8b06a7c9-71b7-4dbb-9b9e-9d14a5bf4835/tool-results/b1vzg2682.txt which is a sensitive file.
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8b06a7c9-71b7-4dbb-9b9e-9d14a5bf4835/tool-results/b1vzg2682.txt",
 "offset": 95,
 "limit": 200
}
```

```
95	        "Richardson, Hilary",
96	        "Lisandrelli, Grace",
97	        "Riobueno-Naylor, Alexa",
98	        "Saxe, Rebecca"
99	    ],
100	    "Acknowledgements": "We thank the Athinoula A. Martinos Imaging Center at the McGovern Institute for Brain Research at MIT, Jorie Koster-Hale, Natalia Velez-Alicea, Mika Asaba, and Nir Jacoby for help with data collection. We thank Todd Thompson for his work making this dataset publicly available.",
101	    "HowToAcknowledge": "Richardson, H., Lisandrelli, G., Riobueno-Naylor, A., & Saxe, R. (2018). Development of the social brain from age three to twelve years. Nature communications, 9(1), 1027.",
102	    "Funding": [
103	        "This project was supported by a NSF Graduate Research Fellowship (#1122374 to HR), and an NSF CAREER award (#095518 to RS), NIH R01-MH096914-05, a Middleton Chair grant (RS), and support from the David and Lucile Packard Foundation (to RS)"
104	    ],
105	    "ReferencesAndLinks": [
106	        "Richardson, H., Lisandrelli, G., Riobueno-Naylor, A., & Saxe, R. (2018). Development of the social brain from age three to twelve years. Nature communications, 9(1), 1027.",
107	        "https://www.nature.com/articles/s41467-018-03399-2"
108	    ],
109	    "DatasetDOI": "doi:10.18112/openneuro.ds000228.v1.1.1"
110	}
111	===== derivatives/README.txt MD5E-s5293--955f1d5b9a262d6402bde466879e6fc4.txt
112	Derivatives
113	
114	fMRI Prep
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && uv pip install -q h5py 2>&1|tail -1; python - <<'EOF'
import json, requests, io, pandas as pd, scipy.io as sio, time, numpy as np
fs={f["filename"]:f for f in json.load(open("files.json"))["data"]["snapshot"]["files"] if not f["directory"]}
p=pd.read_csv(fs["participants.tsv"]["urls"][0],sep="\t")
pd.set_option("display.width",250); pd.set_option("display.max_columns",30)
print(p.shape); print(p.dtypes); print(p.head(3).T); 
for c in p.columns[1:]:
    if p[c].nunique()<12: print(c, p[c].value_counts(dropna=False).to_dict())
    else: print(c, p[c].describe().to_dict() if p[c].dtype!=object else p[c].unique()[:10])
n="derivatives/preprocessed_data/sub-pixar001/sub-pixar001_task-pixar_run-001_ART_and_CompCor_nuisance_regressors.mat"
print(fs[n]["urls"][0])
m=sio.loadmat(io.BytesIO(requests.get(fs[n]["urls"][0]).content))
for k,v in m.items(): print(k, getattr(v,'shape',v) if not k.startswith('__') else v)
r=sio.loadmat(io.BytesIO(requests.get(fs["derivatives/ROIs/RTPJ_9mm_sphere_xyz.mat"]["urls"][0]).content))
for k,v in r.items(): print(k, getattr(v,'shape',v) if not k.startswith('__') else v)
EOF
```

```
Exit code 1
(155, 19)
participant_id                  str
Age                         float64
AgeGroup                        str
Child_Adult                     str
Gender                          str
Handedness                      str
ToM Booklet-Matched         float64
ToM Booklet-Matched-NOFB    float64
FB_Composite                float64
FB_Group                        str
WPPSI BD raw                float64
WPPSI BD scaled             float64
KBIT_raw                    float64
KBIT_standard               float64
DCCS Summary                float64
Scanlog: Scanner                str
Scanlog: Coil                   str
Scanlog: Voxel slize            str
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python - <<'EOF'
import json, requests, io, h5py, numpy as np, scipy.io as sio
fs={f["filename"]:f for f in json.load(open("files.json"))["data"]["snapshot"]["files"] if not f["directory"]}
n="derivatives/preprocessed_data/sub-pixar001/sub-pixar001_task-pixar_run-001_ART_and_CompCor_nuisance_regressors.mat"
h=h5py.File(io.BytesIO(requests.get(fs[n]["urls"][0]).content))
def walk(g,pre=""):
    for k in g:
        o=g[k]
        if isinstance(o,h5py.Group): walk(o,pre+k+"/")
        else: print(pre+k,o.shape,o.dtype, o.attrs.get("MATLAB_class"))
walk(h)
for k in h:
    if isinstance(h[k],h5py.Dataset) and h[k].dtype!=object:
        a=h[k][()]; print(k, a.shape, np.round(a[:, :20] if a.ndim==2 else a,3))
for r in ["RTPJ_9mm_sphere_xyz.mat","rFFA.mat","right_primotor.mat","right_CS.mat"]:
    b=requests.get(fs["derivatives/ROIs/"+r]["urls"][0]).content
    try:
        m=sio.loadmat(io.BytesIO(b)); 
        for k,v in m.items():
            if not k.startswith("__"): print(r,k,type(v), getattr(v,"shape",None), v.dtype, v.dtype.names)
    except NotImplementedError:
        print(r,"v7.3"); walk(h5py.File(io.BytesIO(b)))
EOF
```

```
R (29, 168) float32 b'single'
R (29, 168) [[ 1.     0.     0.     0.     0.     0.     0.     0.     0.     0.
   0.     0.     0.     0.     0.     0.     0.     0.     0.     0.   ]
 [ 0.     1.     0.     0.     0.     0.     0.     0.     0.     0.
   0.     0.     0.     0.     0.     0.     0.     0.     0.     0.   ]
 [ 0.     0.     1.     0.     0.     0.     0.     0.     0.     0.
   0.     0.     0.     0.     0.     0.     0.     0.     0.     0.   ]
 [ 0.     0.     0.     1.     0.     0.     0.     0.     0.     0.
   0.     0.     0.     0.     0.     0.     0.     0.     0.     0.   ]
 [ 0.     0.     0.     0.     0.     1.     0.     0.     0.     0.
   0.     0.     0.     0.     0.     0.     0.     0.     0.     0.   ]
 [ 0.     0.     0.     0.     0.     0.     1.     0.     0.     0.
   0.     0.     0.     0.     0.     0.     0.     0.     0.     0.   ]
 [ 0.     0.     0.     0.     0.     0.     0.     1.     0.     0.
   0.     0.     0.     0.     0.     0.     0.     0.     0.     0.   ]
 [ 0.     0.     0.     0.     0.     0.     0.     0.     1.     0.
   0.     0.     0.     0.     0.     0.     0.     0.     0.     0.   ]
 [ 0.     0.     0.     0.     0.     0.     0.     0.     0.     1.
   0.     0.     0.     0.     0.     0.     0.     0.     0.     0.   ]
 [ 0.     0.     0.     0.     0.     0.     0.     0.     0.     0.
[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source dev/bin/activate && python - <<'EOF'
import json, requests, io, gzip, time, numpy as np, nibabel as nib, h5py
fs={f["filename"]:f for f in json.load(open("files.json"))["data"]["snapshot"]["files"] if not f["directory"]}
n="derivatives/preprocessed_data/sub-pixar001/sub-pixar001_task-pixar_run-001_swrf_bold.nii.gz"
t=time.time(); b=requests.get(fs[n]["urls"][0]).content; t1=time.time()
raw=gzip.decompress(b); t2=time.time()
img=nib.Nifti1Image.from_bytes(raw); d=np.asanyarray(img.dataobj); t3=time.time()
print(len(b)/1e6,"MB", t1-t,t2-t1,t3-t2, img.shape, d.dtype, img.header.get_zooms(), img.header['scl_slope'])
print(img.affine)
for x in ["CompCor_mask","analysis_mask"]:
    m=nib.Nifti1Image.from_bytes(gzip.decompress(requests.get(fs[f"derivatives/preprocessed_data/sub-pixar001/sub-pixar001_{x}.nii.gz"]["urls"][0]).content))
    print(x, m.shape, np.asanyarray(m.dataobj).sum(), np.allclose(m.affine,img.affine))
r=h5py.File(io.BytesIO(requests.get(fs["derivatives/ROIs/RTPJ_9mm_sphere_xyz.mat"]["urls"][0]).content))
XYZ=r["roi_XYZ"][()]; mm=r["roi_XYZmm"][()]; print(XYZ[:,:3], mm[:,:3], r["xY/M"][()].T, r["peak_xyz_mm"][()].ravel())
f=h5py.File(io.BytesIO(requests.get(fs["derivatives/ROIs/rFFA.mat"]["urls"][0]).content)); print(f["roi_xyz"][()][:,:5])
f=h5py.File(io.BytesIO(requests.get(fs["derivatives/ROIs/right_primotor.mat"]["urls"][0]).content)); print(f["roi_xyz"][()][:,:5])
EOF
```

```
91.565296 MB 1.5171842575073242 0.6834821701049805 0.05842900276184082 (79, 95, 68, 168) int16 (np.float32(2.0), np.float32(2.0), np.float32(2.0), np.float32(0.0)) nan
[[  -2.    0.    0.   78.]
 [   0.    2.    0. -112.]
 [   0.    0.    2.  -50.]
 [   0.    0.    0.    1.]]
CompCor_mask (79, 95, 68) 9764 True
analysis_mask (79, 95, 68) nan True
[[16. 15. 16.]
 [25. 26. 26.]
 [37. 37. 37.]] [[ 48.  50.  48.]
 [-64. -62. -62.]
 [ 22.  22.  22.]] [[  -2.    0.    0.   80.]
 [   0.    2.    0. -114.]
 [   0.    0.    2.  -52.]
 [   0.    0.    0.    1.]] [ 48. -60.  30.]
[[ 42.  44.  42.  40.  44.]
 [-52. -50. -50. -50. -48.]
 [-34. -34. -34. -34. -34.]]
[[ 38.  38.  42.  40.  38.]
 [-24. -30. -28. -28. -28.]
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper && wc -l *.txt && grep -n "fMRI data analysis\|Methods\|Statistic\|Code availability\|Data availability" 10.1038-s41467-018-03399-2.txt | head -30
```

```
2095 10.1038-s41467-018-03399-2.txt
139:explicit ToM task (see Methods)21. 3- to 5-year-old children (n =
186:as a network with synchronized responses. We conducted interregion correlation analyses (see Methods)42, in order to test three
209:Methods,
341:in the ToM behavioral battery (see Methods). There was a
384:event from all child participants (see Methods). This analysis was
1252:Methods
1317:fMRI data analysis. FMRI data were analyzed using SPM8 (http://www.fil.ion.ucl.
1546:Code availability. The analysis code used to generate the findings of this study is
1548:Data availability. The fMRI and behavioral data collected and analyzed during the
1735:(Eds). Statistical parametric mapping: the analysis of functional brain images.
1832:colleagues (see Methods and Supplementary Figure 6). Bilateral fusiform regions (blue) were 
1860:coordinates: [-10 -86 2], [10 -86 2], see Methods). Boxplots show within- and across-network zscored correlation values for all participants (n=122 children, n=33 adults), binned by age group, 
1902:participants (n=33; see Methods); dark orange outlines denote 4 events (18s total M(SD) length 
1909:the adult data, included here for illustration. Statistical tests of age-related change were 
1924:Peak timepoints were chosen based on the adult data, included here for illustration. Statistical 
1941:to create independent, stimulus-tailored group ROIs (see Methods). We also used this sample to 
2056:whether ToM and pain events were significantly non-overlapping, described in Methods. The
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-018-03399-2.txt",
 "offset": 1252,
 "limit": 310
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; cd  cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in entries/001453-fouke-2025/README.md; head -c 6000 attempts/001453-fouke-2025-01.yaml; ls questions | head; ls tools
```

```
Wed Oct 28 16:16:07 UTC 2026
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
  title: Reproducing Fouke et al. (2025) from dandiset 001453
  runtime_minutes: 6
helpers:
- omr.py
related:
- id: dandi:001453/0.250518.1950
  relation: uses_data
[... 189 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas; grep -n "blocked\|findings:\|- kind\|assumed\|data:" attempts/001453-fouke-2025-01.yaml | head -30; sed -n '/^findings:/,$p' attempts/001453-fouke-2025-01.yaml | head -40; ls attempts | grep -i openneuro; ls entries | grep -i openneuro
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
198:  outcome: blocked
199:  blocked_by: metadata_insufficient
204:  outcome: blocked
205:  blocked_by: data_missing
210:  outcome: blocked
211:  blocked_by: data_missing
214:  outcome: blocked
215:  blocked_by: data_missing
218:  outcome: blocked
219:  blocked_by: data_missing
222:  outcome: blocked
223:  blocked_by: data_missing
226:  outcome: blocked
227:  blocked_by: data_missing
231:  outcome: blocked
232:  blocked_by: data_missing
235:  outcome: blocked
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=1)[:9000])"; sed -n 1,80p tools/entry.py | head -80
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
[... 437 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "names the dataset\|def check_names\|related\|openneuro" tools/entry.py | head -30; cat entries/001453-fouke-2025/omr.py | head -60
```

```
19:- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
154:    # Datasets are related as <archive>:<id>/<version> (docs/archives.md); papers as doi:, entries as entry:.
156:            for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))]
158:                for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))}
392:    papers = {r["id"] for r in entry.get("related", []) if r["relation"] == "reproduces"}
394:                 for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))}
"""Loading and measures for the freely swimming optomotor data of dandiset 001453.

Fouke, He, Loring & Naumann (2025), Current Biology, doi:10.1016/j.cub.2025.04.027.

Each NWB file holds one fish: x and y position (pixels), heading (`f0_theta`, radians), its
change per frame (`f0_vtheta`; the file says radians/s, the data show radians per frame),
velocity estimates, and per frame the stimulus code and trial number (`stim_index`). Files are
streamed from the archive at the pinned version; nothing is written to disk.

Where the parameters come from:

- Trial processing follows the paper's analysis notebook, Fig1-S1.ipynb, in
  https://gitlab.oit.duke.edu/ean26/danionella_omr_neuralcircuits2025 at commit
  33a5c297ff4ab6ff49f6bdd96139e9fdd867025c (the Methods give none of these): Savitzky-Golay
[... 46 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/openneuro-ds000228-richardson-2018/social_brain.py",
 "content": "\"\"\"Loading and measures for OpenNeuro ds000228, snapshot 1.1.1 (Richardson et al. 2018).\n\nRichardson, Lisandrelli, Riobueno-Naylor & Saxe (2018), \"Development of the social brain from\nage three to twelve years\", Nature Communications 9, 1027, doi:10.1038/s41467-018-03399-2.\n\nThe snapshot holds, for 155 participants, the raw BOLD and T1 images and the paper's own\npreprocessed data under derivatives/preprocessed_data (SPM8, normalized to MNI, 2 mm voxels,\n5 mm smoothing; `*_swrf_bold.nii.gz`), with the ART artifact indicators and five CompCor\nregressors of each run (`*_ART_and_CompCor_nuisance_regressors.mat`, matrix R, one row per\nregressor), and the group ROIs under derivatives/ROIs. Behaviour and demographics are in\nparticipants.tsv. Every file is read from its URL pinned to the snapshot (urls[0] of the\nOpenNeuro GraphQL listing) into memory; nothing is written to disk.\n\nWhere the parameters come from (claims file: claims/openneuro-ds000228/; the labels P1 to P9\nand O1 to O9 are those of its header):\n\n- ROI voxels: the masks deposited in derivatives/ROIs (reading O1a), in MNI mm; their sizes\n  equal those of Supplementary Table 2. M1 (right_primotor, left_primotor), V1 (right_CS,\n  left_CS), face (rSTS_masked, lSTS, rOFA, lOFA, rFFA, lFFA) and scene (rRSC, lRSC, rTOS, lTOS,\n  rPPA, lPPA) are named as in derivatives/README.txt.\n- Timecourse preprocessing (P4, Methods, fMRI data analysis, paragraph 4: \"We applied nearest\n  neighbor interpolation over artifact timepoints ... regressed out two kinds of nuisance\n  covariates ... The residual timecourses were then high-pass filtered with a cutoff of 100 s.\n  Timecourses from all voxels within an ROI were averaged ... and artifact timepoints were\n  subsequently excluded (NaNed)\"). Every step is linear and the same for each voxel, so it is\n  applied to the ROI's mean timecourse, which gives the same result as per voxel then average.\n  Nearest-neighbour ties (an artifact run with good timepoints at equal distance on both\n  sides) take the earlier timepoint, a standard choice that cannot change a result beyond\n  rounding. The regression includes an intercept (standard). The 100 s high-pass is SPM's\n  discrete cosine basis (spm_filter: order fix(2 * n * TR / cutoff) + 1, constant included),\n  the standard SPM8 filter, which the paper used.\n- Artifact regressors (O2): the deposited R matrix has one indicator per artifact timepoint\n  (reading O2a); `single_artifact_regressor=True` gives reading O2b.\n- M1 regression for the inter-region correlation (P4, Methods paragraph 5: \"we additionally\n  regressed out the raw timecourse extracted from bilateral primary motor cortex\"): the mean\n  raw timecourse over the voxels of both M1 ROIs.\n- Inter-region correlation (P5, Methods paragraph 7): Pearson r of every ROI pair over\n  non-artifact timepoints, Fisher z, averaged within ToM, within Pain, across.\n- Network timecourse (P6, Methods paragraph 9): z-normalized ROI timecourses averaged over the\n  network's ROIs; the span of the z-normalization is reading O6 (TRs 11 to 168, or all).\n- Reverse correlation (P7, Methods paragraph 9): one-tailed one-sample t-test against 0 at each\n  TR from 11, events are runs of two or more significant TRs; the alpha is reading O5.\n- Partial correlations: Spearman partial correlation as R's ppcor (Pearson partial correlation\n  of the ranks, t test with n - 2 - k degrees of freedom); partial Kendall tau as ppcor\n  (reading O8), its p from ppcor's normal approximation.\n- Williams' test: Williams' T2 for two dependent correlations sharing one variable (Steiger\n  1980, eq. 7), with its t on n - 3 degrees of freedom; Steiger's Z (eq. 14) is also given.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport gzip\nimport io\nfrom concurrent.futures import ThreadPoolExecutor\nfrom functools import lru_cache\n\nimport h5py\nimport nibabel as nib\nimport numpy as np\nimport pandas as pd\nimport requests\nfrom scipy import stats\n\nDATASET_ID = \"ds000228\"\nSNAPSHOT = \"1.1.1\"\nSNAPSHOT_DOI = \"10.18112/openneuro.ds000228.v1.1.1\"\nGRAPHQL = \"https://openneuro.org/crn/graphql\"\n\nN_TR = 168\nTR_S = 2.0\nFIRST_MOVIE_TR = 11          # README and Methods: TRs 1-5 rest, 6-10 logos, movie from TR 11\nHIGHPASS_S = 100.0\nN_COMPCOR = 5\n\nTOM_ROIS = [\"RTPJ\", \"LTPJ\", \"PC\", \"DMPFC\", \"MMPFC\", \"VMPFC\"]\nPAIN_ROIS = [\"RS2\", \"LS2\", \"RInsula\", \"LInsula\", \"RMFG\", \"LMFG\", \"AMCC\"]\nFACE_ROIS = [\"rSTS_masked\", \"lSTS\", \"rOFA\", \"lOFA\", \"rFFA\", \"lFFA\"]\nSCENE_ROIS = [\"rRSC\", \"lRSC\", \"rTOS\", \"lTOS\", \"rPPA\", \"lPPA\"]\nM1_ROIS = [\"right_primotor\", \"left_primotor\"]\nV1_ROIS = [\"right_CS\", \"left_CS\"]\nFFA_ROIS = [\"rFFA\", \"lFFA\"]\nNETWORKS = {\"ToM\": TOM_ROIS, \"Pain\": PAIN_ROIS, \"Face\": FACE_ROIS, \"Scene\": SCENE_ROIS,\n            \"M1\": M1_ROIS, \"V1\": V1_ROIS}\nALL_ROIS = TOM_ROIS + PAIN_ROIS + FACE_ROIS + SCENE_ROIS + M1_ROIS + V1_ROIS\n\n\n@lru_cache(maxsize=1)\ndef file_table() -> pd.DataFrame:\n    \"\"\"Every file of the snapshot: filename, size, annexed, id (checksum) and pinned url.\"\"\"\n    query = ('{ snapshot(datasetId: \"%s\", tag: \"%s\") { files(recursive: true) '\n             '{ filename size annexed directory id urls } } }' % (DATASET_ID, SNAPSHOT))\n    r = requests.post(GRAPHQL, json={\"query\": query}, timeout=300)\n    r.raise_for_status()\n    files = [f for f in r.json()[\"data\"][\"snapshot\"][\"files\"] if not f[\"directory\"]]\n    df = pd.DataFrame(files).drop(columns=\"directory\")\n    df[\"url\"] = df[\"urls\"].str[0]\n    return df.drop(columns=\"urls\").set_index(\"filename\")\n\n\ndef url(filename: str) -> str:\n    return file_table().loc[filename, \"url\"]\n\n\ndef fetch(filename: str) -> bytes:\n    for attempt in range(4):\n        try:\n            r = requests.get(url(filename), timeout=300)\n            r.raise_for_status()\n            return r.content\n        except requests.RequestException:\n            if attempt == 3:\n                raise\n    raise RuntimeError(filename)\n\n\ndef participants() -> pd.DataFrame:\n    return pd.read_csv(io.BytesIO(fetch(\"participants.tsv\")), sep=\"\\t\")\n\n\ndef text(filename: str) -> str:\n    return fetch(filename).decode(\"utf-8\", errors=\"replace\")\n\n\ndef roi_mm(name: str) -> np.ndarray:\n    \"\"\"MNI mm coordinates (3 x n voxels) of a deposited ROI.\"\"\"\n    fn = f\"derivatives/ROIs/{name}_9mm_sphere_xyz.mat\" if name in TOM_ROIS + PAIN_ROIS \\\n        else f\"derivatives/ROIs/{name}.mat\"\n    with h5py.File(io.BytesIO(fetch(fn)), \"r\") as h:\n        return h[\"roi_XYZmm\"][()] if \"roi_XYZmm\" in h else h[\"roi_xyz\"][()]\n\n\n@lru_cache(maxsize=1)\ndef all_roi_mm() -> dict:\n    return {name: roi_mm(name) for name in ALL_ROIS}\n\n\ndef derivative(sub: str, suffix: str) -> str:\n    return f\"derivatives/preprocessed_data/{sub}/{sub}_{suffix}\"\n\n\ndef nuisance(sub: str) -> tuple[np.ndarray, np.ndarray]:\n    \"\"\"(artifact indicators, n_artifacts x 168; CompCor regressors, 5 x 168) from matrix R.\"\"\"\n    with h5py.File(io.BytesIO(fetch(derivative(\n            sub, \"task-pixar_run-001_ART_and_CompCor_nuisance_regressors.mat\"))), \"r\") as h:\n        R = h[\"R\"][()].astype(float)\n    return R[:-N_COMPCOR], R[-N_COMPCOR:]\n\n\ndef extract_subject(sub: str) -> dict:\n    \"\"\"Raw ROI timecourses of one participant from its preprocessed (swrf) BOLD image.\n\n    For each ROI: the mean over all its voxels, the mean over its voxels that hold data (no\n    zero or non-finite value at any timepoint; reading O1c), and the count of such voxels.\n    \"\"\"\n    raw = gzip.decompress(fetch(derivative(sub, \"task-pixar_run-001_swrf_bold.nii.gz\")))\n    img = nib.Nifti1Image.from_bytes(raw)\n    data = np.asanyarray(img.dataobj)\n    inv = np.linalg.inv(img.affine)\n    out = {\"shape\": img.shape, \"zooms\": img.header.get_zooms(), \"affine\": img.affine,\n           \"dtype\": str(data.dtype)}\n    rois = {}\n    for name, mm in all_roi_mm().items():\n        vox = np.rint(inv[:3, :3] @ mm + inv[:3, 3:4]).astype(int)\n        inside = np.all((vox >= 0) & (vox < np.array(img.shape[:3])[:, None]), axis=0)\n        ts = np.full((mm.shape[1], img.shape[3]), np.nan)\n        ts[inside] = data[vox[0, inside], vox[1, inside], vox[2, inside], :].astype(float)\n        good = np.all(np.isfinite(ts) & (ts != 0), axis=1)\n        rois[name] = {\"all\": np.nanmean(ts, axis=0), \"with_data\": ts[good].mean(axis=0)\n                      if good.any() else np.full(img.shape[3], np.nan),\n                      \"n_vox\": mm.shape[1], \"n_with_data\": int(good.sum())}\n    out[\"rois\"] = rois\n    out[\"artifacts\"], out[\"compcor\"] = nuisance(sub)\n    return out\n\n\ndef extract_all(subjects, n_threads: int = 8) -> dict:\n    all_roi_mm()\n    with ThreadPoolExecutor(n_threads) as ex:\n        return dict(zip(subjects, ex.map(extract_subject, subjects)))\n\n\n# ---------------------------------------------------------------- timecourse preprocessing\n\ndef artifact_index(indicators: np.ndarray) -> np.ndarray:\n    \"\"\"0-based timepoints flagged by the ART indicator rows.\"\"\"\n    return np.sort(np.flatnonzero(indicators.sum(axis=0) > 0))\n\n\ndef nearest_neighbour_fill(ts: np.ndarray, bad: np.ndarray) -> np.ndarray:\n    out = ts.copy()\n    good = np.setdiff1d(np.arange(len(ts)), bad)\n    for t in bad:\n        out[t] = ts[good[np.argmin(np.abs(good - t))]]\n    return out\n\n\ndef dct_highpass_basis(n: int = N_TR, tr: float = TR_S, cutoff: float = HIGHPASS_S) -> np.ndarray:\n    \"\"\"SPM's discrete cosine set for a high-pass cutoff (spm_filter), constant excluded.\"\"\"\n    order = int(np.fix(2 * (n * tr) / cutoff + 1))\n    t = np.arange(n)\n    return np.stack([np.sqrt(2 / n) * np.cos(np.pi * (2 * t + 1) * k / (2 * n))\n                     for k in range(1, order)], axis=1)\n\n\ndef residualize(y: np.ndarray, X: np.ndarray) -> np.ndarray:\n    X = np.column_stack([np.ones(len(y)), X])\n    beta, *_ = np.linalg.lstsq(X, y, rcond=None)\n    return y - X @ beta\n\n\ndef clean(ts: np.ndarray, indicators: np.ndarray, compcor: np.ndarray, extra=None,\n          single_artifact_regressor: bool = False) -> np.ndarray:\n    \"\"\"P4: interpolate over artifacts, regress nuisance, high-pass, NaN the artifacts.\"\"\"\n    bad = artifact_index(indicators)\n    y = nearest_neighbour_fill(ts, bad) if len(bad) else ts.copy()\n    art = indicators.T if not single_artifact_regressor else indicators.sum(axis=0)[:, None]\n    parts = [compcor.T] + ([art] if len(bad) else [])\n    if extra is not None:\n        parts.append(np.asarray(extra).reshape(len(ts), -1))\n    y = residualize(y, np.column_stack(parts))\n    hp = dct_highpass_basis(len(ts))\n    y = y - hp @ np.linalg.lstsq(hp, y, rcond=None)[0]\n    y[bad] = np.nan\n    return y\n\n\ndef subject_timecourses(sub_data: dict, rois, voxels: str = \"with_data\", m1: bool = False,\n                        single_artifact_regressor: bool = False) -> dict:\n    \"\"\"Cleaned timecourse of each ROI; with m1=True the bilateral M1 raw mean is regressed out.\"\"\"\n    extra = None\n    if m1:\n        r, l = sub_data[\"rois\"][\"right_primotor\"], sub_data[\"rois\"][\"left_primotor\"]\n        extra = (r[voxels] * r[\"n_with_data\" if voxels == \"with_data\" else \"n_vox\"]\n                 + l[voxels] * l[\"n_with_data\" if voxels == \"with_data\" else \"n_vox\"]) / (\n            r[\"n_with_data\" if voxels == \"with_data\" else \"n_vox\"]\n            + l[\"n_with_data\" if voxels == \"with_data\" else \"n_vox\"])\n    return {name: clean(sub_data[\"rois\"][name][voxels], sub_data[\"artifacts\"],\n                        sub_data[\"compcor\"], extra, single_artifact_regressor)\n            for name in rois}\n\n\n# ---------------------------------------------------------------- inter-region correlation\n\ndef fisher_corr(a: np.ndarray, b: np.ndarray, trs=None) -> float:\n    ok = np.isfinite(a) & np.isfinite(b)\n    if trs is not None:\n        ok &= np.isin(np.arange(len(a)), trs)\n    return float(np.arctanh(np.corrcoef(a[ok], b[ok])[0, 1]))\n\n\ndef irc_matrix(tcs: dict, rois, trs=None) -> pd.DataFrame:\n    m = pd.DataFrame(np.nan, index=rois, columns=rois)\n    for i, a in enumerate(rois):\n        for b in rois[i + 1:]:\n            m.loc[a, b] = m.loc[b, a] = fisher_corr(tcs[a], tcs[b], trs)\n    return m\n\n\ndef within(m: pd.DataFrame, rois, exclude_pairs=()) -> float:\n    vals = [m.loc[a, b] for i, a in enumerate(rois) for b in rois[i + 1:]\n            if {a, b} not in [set(p) for p in exclude_pairs]]\n    return float(np.mean(vals))\n\n\ndef across(m: pd.DataFrame, rois_a, rois_b) -> float:\n    return float(np.mean([m.loc[a, b] for a in rois_a for b in rois_b]))\n\n\n# ---------------------------------------------------------------- network timecourses\n\ndef network_timecourse(tcs: dict, rois, z_span: str = \"movie\", z: bool = True) -> np.ndarray:\n    \"\"\"P6: each ROI timecourse z-normalized (over TRs 11-168, 'movie', or all 168, 'all';\n    artifact NaNs left out), then averaged over the network's ROIs.\"\"\"\n    span = np.arange(FIRST_MOVIE_TR - 1, N_TR) if z_span == \"movie\" else np.arange(N_TR)\n    out = []\n    for r in rois:\n        x = tcs[r].copy()\n        if z:\n            x = (x - np.nanmean(x[span])) / np.nanstd(x[span], ddof=1)\n        out.append(x)\n    return np.mean(out, axis=0)\n\n\ndef reverse_correlation(group_tcs: np.ndarray, alpha: float, fdr: bool = False):\n    \"\"\"P7. group_tcs: participants x 168. Returns per-TR (1-based TR, mean, t, p, significant)\n    from TR 11, and the events as lists of 1-based TRs.\"\"\"\n    trs = np.arange(FIRST_MOVIE_TR, N_TR + 1)\n    x = group_tcs[:, trs - 1]\n    t, p = stats.ttest_1samp(x, 0, axis=0, nan_policy=\"omit\", alternative=\"greater\")\n    t, p = np.asarray(t), np.asarray(p)\n    if fdr:\n        sig = stats.false_discovery_control(p) < alpha\n    else:\n        sig = p < alpha\n    table = pd.DataFrame({\"TR\": trs, \"mean\": np.nanmean(x, axis=0), \"t\": t, \"p\": p, \"sig\": sig})\n    events, run = [], []\n    for tr, s in zip(trs, sig):\n        if s:\n            run.append(tr)\n        else:\n            if len(run) >= 2:\n                events.append(run)\n            run = []\n    if len(run) >= 2:\n        events.append(run)\n    return table, events\n\n\ndef rank_events(events, table: pd.DataFrame):\n    \"\"\"Events ranked by the mean at their peak TR, highest first, with the peak TR.\"\"\"\n    mean = table.set_index(\"TR\")[\"mean\"]\n    rows = [{\"trs\": e, \"onset\": e[0], \"length_tr\": len(e),\n             \"peak_tr\": int(mean.loc[e].idxmax()), \"peak_mean\": float(mean.loc[e].max())}\n            for e in events]\n    return pd.DataFrame(rows).sort_values(\"peak_mean\", ascending=False).reset_index(drop=True)\n\n\ndef overlap_permutation(lengths_a, lengths_b, zeros_a: int, zeros_b: int, n_perm: int,\n                        rng: np.random.Generator) -> np.ndarray:\n    \"\"\"Methods paragraph 10: random timecourses with the same events in random order and a\n    random split of the zeros between them (at least one between events). Returns the overlap\n    (timepoints in both) of each permutation.\"\"\"\n    def one(lengths, n_zeros):\n        lengths = rng.permutation(lengths)\n        k = len(lengths)\n        gaps = np.zeros(k + 1, int)\n        gaps[1:k] = 1\n        rest = n_zeros - (k - 1)\n        gaps += rng.multinomial(rest, np.ones(k + 1) / (k + 1))\n        seq = []\n        for g, L in zip(gaps[:-1], lengths):\n            seq += [0] * g + [1] * L\n        seq += [0] * gaps[-1]\n        return np.array(seq, bool)\n    out = np.empty(n_perm, int)\n    for i in range(n_perm):\n        a, b = one(lengths_a, zeros_a), one(lengths_b, zeros_b)\n        n = min(len(a), len(b))\n        out[i] = int((a[:n] & b[:n]).sum())\n    return out\n\n\n# ---------------------------------------------------------------- statistics\n\ndef _resid(y, Z):\n    return residualize(np.asarray(y, float), np.asarray(Z, float).reshape(len(y), -1))\n\n\ndef partial_spearman(x, y, covars) -> tuple[float, float, int]:\n    \"\"\"ppcor::pcor.test(method='spearman'): Pearson partial correlation of ranks.\"\"\"\n    x, y = stats.rankdata(x), stats.rankdata(y)\n    Z = np.column_stack([stats.rankdata(c) for c in np.atleast_2d(np.asarray(covars).T)\n                         ]) if np.ndim(covars) > 1 else stats.rankdata(covars)[:, None]\n    r = np.corrcoef(_resid(x, Z), _resid(y, Z))[0, 1]\n    n, k = len(x), Z.shape[1]\n    df = n - 2 - k\n    t = r * np.sqrt(df / (1 - r ** 2))\n    return float(r), float(2 * stats.t.sf(abs(t), df)), df\n\n\ndef kendall(x, y) -> tuple[float, float]:\n    res = stats.kendalltau(x, y, variant=\"b\", method=\"asymptotic\")\n    return float(res.statistic), float(res.pvalue)\n\n\ndef partial_kendall(x, y, z) -> tuple[float, float]:\n    \"\"\"ppcor::pcor.test(method='kendall') with one covariate (reading O8).\"\"\"\n    txy, tyz, txz = kendall(x, y)[0], kendall(y, z)[0], kendall(x, z)[0]\n    r = (txy - txz * tyz) / np.sqrt((1 - txz ** 2) * (1 - tyz ** 2))\n    n, gp = len(x), 1\n    stat = r / np.sqrt(2 * (2 * (n - gp) + 5) / (9 * (n - gp) * (n - 1 - gp)))\n    return float(r), float(2 * stats.norm.sf(abs(stat)))\n\n\ndef williams(r12: float, r13: float, r23: float, n: int) -> dict:\n    \"\"\"Difference of r12 and r13 (variable 1 shared). Williams' T2 and Steiger's Z.\"\"\"\n    detR = 1 - r12 ** 2 - r13 ** 2 - r23 ** 2 + 2 * r12 * r13 * r23\n    rbar = (r12 + r13) / 2\n    t2 = (r12 - r13) * np.sqrt((n - 1) * (1 + r23) / (\n        2 * (n - 1) / (n - 3) * detR + rbar ** 2 * (1 - r23) ** 3))\n    psi = r23 * (1 - 2 * rbar ** 2) - 0.5 * rbar ** 2 * (1 - 2 * rbar ** 2 - r23 ** 2)\n    c = psi / (1 - rbar ** 2) ** 2\n    z = (np.arctanh(r12) - np.arctanh(r13)) * np.sqrt(n - 3) / np.sqrt(2 - 2 * c)\n    return {\"t\": float(t2), \"p_t\": float(2 * stats.t.sf(abs(t2), n - 3)),\n            \"z\": float(z), \"p_z\": float(2 * stats.norm.sf(abs(z)))}\n\n\ndef ols(df: pd.DataFrame, y: str, xs, zscore: bool = False):\n    \"\"\"Ordinary least squares; with zscore=True the outcome and continuous predictors are\n    z-scored (reading O4a). Returns the statsmodels result.\"\"\"\n    import statsmodels.api as sm\n    d = df[[y] + list(xs)].dropna().astype(float)\n    if zscore:\n        for c in [y] + list(xs):\n            if d[c].nunique() > 2:\n                d[c] = (d[c] - d[c].mean()) / d[c].std(ddof=1)\n    return sm.OLS(d[y], sm.add_constant(d[list(xs)])).fit()\n"
}
```

```
File created successfully at: entries/openneuro-ds000228-richardson-2018/social_brain.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018 && source $TMPDIR/dev/bin/activate && python - <<'EOF'
import time, numpy as np, social_brain as sb
t=time.time(); p=sb.participants(); print(time.time()-t)
t=time.time(); d=sb.extract_all(list(p.participant_id[:8]), n_threads=8); print("8 subs", time.time()-t)
s=d["sub-pixar001"]
print(s["shape"], s["artifacts"].shape, s["artifacts"].sum(1)[:5], sb.artifact_index(s["artifacts"]))
for k,v in s["rois"].items(): print(k, v["n_vox"], v["n_with_data"], np.round(v["all"][:3],1))
EOF
```

```
0.9157345294952393
8 subs 10.814619541168213
(79, 95, 68, 168) (24, 168) [1. 1. 1. 1. 1.] [  0   1   2   3   5   6   7   8   9  10  13  14  15  16  22  23  24  25
  26  27  69  70  71 164]
RTPJ 376 376 [1649.  1645.3 1651. ]
LTPJ 368 368 [2218.  2206.3 2220.2]
PC 382 382 [999.6 989.  990.4]
DMPFC 217 217 [3159.4 3152.8 3159.2]
MMPFC 275 275 [3009.4 3002.  3011.9]
VMPFC 198 198 [1077.6 1063.3 1068.6]
RS2 368 368 [1439.3 1447.5 1444.9]
LS2 269 269 [1921.5 1924.8 1933.2]
RInsula 309 309 [775.3 776.6 780.9]
LInsula 240 240 [936.5 934.1 935.7]
RMFG 142 142 [3423.7 3419.7 3430.4]
LMFG 256 256 [2165.2 2161.4 2166.3]
AMCC 249 249 [897.1 895.3 896.9]
rSTS_masked 2503 2503 [1288.  1287.4 1290.7]
lSTS 844 844 [1609.9 1606.4 1615.1]
rOFA 790 764 [899.4 900.6 903.4]
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python - <<'EOF'
import time, pickle, os, social_brain as sb
p=sb.participants()
t=time.time(); d=sb.extract_all(list(p.participant_id), n_threads=8); print("all", time.time()-t)
pickle.dump(d, open(os.environ["TMPDIR"]+"/extract.pkl","wb"))
EOF
date -u
```

```
all 94.80242896080017
Wed Oct 28 16:20:12 UTC 2026
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python - <<'EOF'
import pickle, os, numpy as np, pandas as pd, social_brain as sb
from scipy import stats
d=pickle.load(open(os.environ["TMPDIR"]+"/extract.pkl","rb"))
p=sb.participants()
p["n_art"]=[len(sb.artifact_index(d[s]["artifacts"])) for s in p.participant_id]
p["n_art_rows"]=[d[s]["artifacts"].shape[0] for s in p.participant_id]
print((p.n_art==p.n_art_rows).all(), set(d[s]["shape"] for s in d), set(d[s]["dtype"] for s in d))
# indicator rows each single 1?
print(all((d[s]["artifacts"].sum(1)==1).all() for s in d))
ch=p[p.Child_Adult=="child"]; ad=p[p.Child_Adult=="adult"]
print(len(ch),len(ad),(ch.Gender=="F").sum(),(ad.Gender=="F").sum(), ch.Age.mean(), ch.Age.std(), ad.Age.min(),ad.Age.max(), ad.Age.mean())
print(ch.groupby("AgeGroup").Age.agg(["count","min","max","mean"]))
print("max art frac", p.n_art.max()/168)
print(p.groupby("Child_Adult").n_art.agg(["mean","std"]))
print(stats.ttest_ind(ch.n_art, ad.n_art, equal_var=False))
y=ch[ch.Age<6]; print(len(y), y.FB_Group.value_counts(), y.groupby("FB_Group").Gender.apply(lambda g:(g=="F").sum()))
print(y.groupby("FB_Group").Age.agg(["mean","std"]))
print(y.groupby(["AgeGroup","FB_Group"]).size().unstack())
print(ch.groupby("AgeGroup")["ToM Booklet-Matched"].mean())
print("DCCS n", ch["DCCS Summary"].notna().sum(), y["DCCS Summary"].notna().sum(), ch.loc[ch["DCCS Summary"].notna(),"Age"].max())
print(p.groupby("AgeGroup")["Scanlog: Voxel slize"].value_counts().unstack(), p.groupby("AgeGroup")["Scanlog: Slice Gap"].value_counts(dropna=False).unstack())
print(ch.FB_Group.value_counts(dropna=False)); print(ad.FB_Group.value_counts(dropna=False))
print(p.Handedness.groupby(p.Child_Adult).value_counts())
# ROI voxel coverage
cov=pd.DataFrame({s:{r:d[s]["rois"][r]["n_with_data"]/d[s]["rois"][r]["n_vox"] for r in sb.ALL_ROIS} for s in d}).T
print(cov.min().round(3).to_dict()); print((cov<1).sum().to_dict())
EOF
```

```
True {(79, 95, 68, 168)} {'int16'}
True
122 33 64 20 6.709461013672131 2.330938057965228 18.0 39.0 24.772727272727273
          count       min        max      mean
AgeGroup                                      
3yo          17  3.518138   3.989049  3.751983
4yo          14  4.057495   4.856947  4.430038
5yo          34  5.010000   5.990000  5.509118
7yo          23  7.000000   7.960000  7.536087
8-12yo       34  8.020000  12.300000  9.767941
max art frac 0.2857142857142857
                  mean        std
Child_Adult                      
adult         2.818182   3.995736
child        10.508197  10.597244
TtestResult(statistic=np.float64(6.489244032668625), pvalue=np.float64(1.4407253613475335e-09), df=np.float64(137.7402733685932))
65 FB_Group
pass    30
inc     20
fail    15
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warning
import pickle, os, numpy as np, pandas as pd, social_brain as sb
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd
d=pickle.load(open(os.environ["TMPDIR"]+"/extract.pkl","rb"))
p=sb.participants(); p["n_art"]=[len(sb.artifact_index(d[s]["artifacts"])) for s in p.participant_id]
ch=p[p.Child_Adult=="child"].copy(); y=ch[ch.Age<6].copy()
tom="ToM Booklet-Matched"; nofb="ToM Booklet-Matched-NOFB"; dc="DCCS Summary"
print("tom~age", sb.kendall(ch[tom],ch.Age)); yd=y.dropna(subset=[dc]); print("dccs~age",len(yd), sb.kendall(yd[dc],yd.Age))
print("tom~dccs|age", sb.partial_kendall(yd[tom],yd[dc],yd.Age))
for var in [nofb, tom, "Age", dc]:
    sub=y.dropna(subset=[var])
    print("==",var, sub.groupby("FB_Group")[var].agg(["mean","sem","count"]).round(3).to_dict())
    print(" KW", stats.kruskal(*[g[var] for _,g in sub.groupby("FB_Group")]))
    for sc in ["raw","z"]:
        v=sub[var] if sc=="raw" else (sub[var]-sub[var].mean())/sub[var].std()
        r=pairwise_tukeyhsd(v, sub.FB_Group); print(sc, r.summary().data[1:])
print("art~age", stats.spearmanr(ch.n_art, ch.Age)); print("art~tom", sb.kendall(ch.n_art, ch[tom]))
pf=y[y.FB_Group.isin(["pass","fail"])].copy(); pf["fail"]=(pf.FB_Group=="fail").astype(float)
r=sb.ols(pf,"n_art",["fail"]); print(r.params.round(3).to_dict(), r.tvalues.round(3).to_dict(), r.pvalues.round(3).to_dict())
r=sb.ols(yd,"n_art",[dc]); print(r.params.round(3).to_dict(), r.tvalues.round(3).to_dict(), r.pvalues.round(3).to_dict())
r=sb.ols(yd,"n_art",[dc],zscore=True); print(r.params.round(3).to_dict())
EOF
```

```
tom~age (0.6645109945299056, 5.413319963175981e-26)
dccs~age 64 (0.19818854635818364, 0.048087042159399615)
tom~dccs|age (0.18580539418324113, 0.031376760571341665)
== ToM Booklet-Matched-NOFB {'mean': {'fail': 0.546, 'inc': 0.572, 'pass': 0.753}, 'sem': {'fail': 0.043, 'inc': 0.034, 'pass': 0.021}, 'count': {'fail': 15, 'inc': 20, 'pass': 30}}
 KW KruskalResult(statistic=np.float64(22.95494150955819), pvalue=np.float64(1.0360907227146506e-05))
raw [['fail', 'inc', np.float64(0.0262), np.float64(0.8455), np.float64(-0.0875), np.float64(0.1398), np.False_], ['fail', 'pass', np.float64(0.2077), np.float64(0.0), np.float64(0.1025), np.float64(0.3129), np.True_], ['inc', 'pass', np.float64(0.1816), np.float64(0.0001), np.float64(0.0855), np.float64(0.2776), np.True_]]
z [['fail', 'inc', np.float64(0.1561), np.float64(0.8455), np.float64(-0.5222), np.float64(0.8344), np.False_], ['fail', 'pass', np.float64(1.2399), np.float64(0.0), np.float64(0.612), np.float64(1.8679), np.True_], ['inc', 'pass', np.float64(1.0838), np.float64(0.0001), np.float64(0.5106), np.float64(1.6571), np.True_]]
== ToM Booklet-Matched {'mean': {'fail': 0.451, 'inc': 0.571, 'pass': 0.792}, 'sem': {'fail': 0.037, 'inc': 0.026, 'pass': 0.017}, 'count': {'fail': 15, 'inc': 20, 'pass': 30}}
 KW KruskalResult(statistic=np.float64(41.507046183286946), pvalue=np.float64(9.701959139860405e-10))
raw [['fail', 'inc', np.float64(0.1197), np.float64(0.0073), np.float64(0.028), np.float64(0.2114), np.True_], ['fail', 'pass', np.float64(0.3412), np.float64(0.0), np.float64(0.2563), np.float64(0.4261), np.True_], ['inc', 'pass', np.float64(0.2215), np.float64(0.0), np.float64(0.144), np.float64(0.299), np.True_]]
z [['fail', 'inc', np.float64(0.6606), np.float64(0.0073), np.float64(0.1543), np.float64(1.167), np.True_], ['fail', 'pass', np.float64(1.8833), np.float64(0.0), np.float64(1.4145), np.float64(2.3521), np.True_], ['inc', 'pass', np.float64(1.2227), np.float64(0.0), np.float64(0.7947), np.float64(1.6506)
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && cat > $TMPDIR/irc_dev.py <<'EOF'
import pickle, os, numpy as np, pandas as pd, social_brain as sb, itertools
from scipy import stats
d=pickle.load(open(os.environ["TMPDIR"]+"/extract.pkl","rb"))
p=sb.participants(); p["n_art"]=[len(sb.artifact_index(d[s]["artifacts"])) for s in p.participant_id]
p=p.set_index("participant_id")
def irc_table(m1=True, voxels="with_data", single=False, movie_only=False):
    rows={}
    trs=np.arange(10,168) if movie_only else None
    rois=sb.TOM_ROIS+sb.PAIN_ROIS
    for s in p.index:
        tc=sb.subject_timecourses(d[s], rois, voxels, m1, single)
        m=sb.irc_matrix(tc, rois, trs)
        rows[s]={"wToM":sb.within(m,sb.TOM_ROIS),"wPain":sb.within(m,sb.PAIN_ROIS),"across":sb.across(m,sb.TOM_ROIS,sb.PAIN_ROIS)}
    return pd.DataFrame(rows).T
EOF
python - <<'EOF'
import sys,os; sys.path.insert(0,os.environ["TMPDIR"]); exec(open(os.environ["TMPDIR"]+"/irc_dev.py").read())
import time
for cfg in [dict(), dict(voxels="all"), dict(single=True), dict(movie_only=True), dict(m1=False)]:
    t=time.time(); T=irc_table(**cfg).join(p)
    ad=T[T.Child_Adult=="adult"]; ch=T[T.Child_Adult=="child"]; y3=ch[ch.AgeGroup=="3yo"]
    print(cfg, round(time.time()-t,1))
    print(" adult", ad[["wToM","wPain","across"]].mean().round(3).to_dict(), stats.ttest_rel(ad.wToM,ad.across).statistic.round(2), stats.ttest_rel(ad.wPain,ad.across).statistic.round(2))
    print(" 3yo", y3[["wToM","wPain","across"]].mean().round(3).to_dict(), stats.ttest_rel(y3.wToM,y3.across).statistic.round(2), stats.ttest_rel(y3.wPain,y3.across).statistic.round(2))
    for v in ["wToM","wPain","across"]: print("  age", v, np.round(sb.partial_spearman(ch[v],ch.Age,ch.n_art),4))
EOF
```

```
{} 1.6
 adult {'wToM': 0.604, 'wPain': 0.398, 'across': -0.051} 19.06 21.78
 3yo {'wToM': 0.326, 'wPain': 0.179, 'across': 0.074} 8.43 4.54
  age wToM [3.061e-01 6.000e-04 1.190e+02]
  age wPain [  0.4607   0.     119.    ]
  age across [-2.593e-01  4.100e-03  1.190e+02]
{'voxels': 'all'} 1.6
 adult {'wToM': 0.604, 'wPain': 0.398, 'across': -0.051} 19.06 21.78
 3yo {'wToM': 0.326, 'wPain': 0.179, 'across': 0.074} 8.43 4.54
  age wToM [3.061e-01 6.000e-04 1.190e+02]
  age wPain [  0.4607   0.     119.    ]
  age across [-2.593e-01  4.100e-03  1.190e+02]
{'single': True} 1.5
 adult {'wToM': 0.606, 'wPain': 0.402, 'across': -0.047} 18.94 21.59
 3yo {'wToM': 0.321, 'wPain': 0.185, 'across': 0.074} 8.37 5.0
  age wToM [3.236e-01 3.000e-04 1.190e+02]
  age wPain [  0.4584   0.     119.    ]
  age across [-2.613e-01  3.800e-03  1.190e+02]
{'movie_only': True} 1.9
 adult {'wToM': 0.594, 'wPain': 0.397, 'across': -0.053} 18.87 20.97
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import sys,os; exec(open(os.environ["TMPDIR"]+"/irc_dev.py").read())
T=irc_table().join(p); T["adult"]=(T.Child_Adult=="adult").astype(float); T["child"]=1-T.adult
ch=T[T.Child_Adult=="child"].copy(); tom="ToM Booklet-Matched"
for v in ["wToM","wPain","across"]:
    for z in [False,True]:
        r=sb.ols(T,v,["child","n_art"],zscore=z); print(v,z, r.params.round(3).to_dict(), r.tvalues.round(2).to_dict(), r.pvalues.apply(lambda x:f"{x:.2g}").to_dict())
for v in ["wToM","across"]:
    print(v,"tom|art", sb.partial_kendall(ch[v],ch[tom],ch.n_art))
    r=sb.ols(ch,v,[tom,"Age","n_art"]); print(" reg", r.tvalues.round(2).to_dict(), r.pvalues.round(3).to_dict())
y=ch[(ch.Age<6)&ch.FB_Group.isin(["pass","fail"])].copy(); y["fail"]=(y.FB_Group=="fail").astype(float)
print(y.groupby("FB_Group")[["wToM","across"]].agg(["mean","sem"]).round(3))
for v in ["wToM","across"]:
    for z in [False,True]:
        r=sb.ols(y,v,["fail","Age","n_art"],zscore=z); print(v,z, r.params.round(3).to_dict(), r.tvalues.round(2).to_dict(), r.pvalues.round(3).to_dict())
r=sb.ols(y,"wToM",["fail","Age","n_art","DCCS Summary"]); print("dccs", r.tvalues.round(2).to_dict(), r.pvalues.round(3).to_dict())
# 3yo matrix
rois=sb.TOM_ROIS+sb.PAIN_ROIS
ms=[]
for s in ch[ch.AgeGroup=="3yo"].index:
    tc=sb.subject_timecourses(d[s], rois, "with_data", True); ms.append(sb.irc_matrix(tc,rois).values)
M=pd.DataFrame(np.nanmean(ms,0),index=rois,columns=rois)
def ranked(R):
    return sorted([((a,b),round(M.loc[a,b],3)) for i,a in enumerate(R) for b in R[i+1:]], key=lambda x:-x[1])[:5]
print(ranked(sb.TOM_ROIS)); print(ranked(sb.PAIN_ROIS))
EOF
```

```
wToM False {'const': 0.609, 'child': -0.173, 'n_art': -0.002} {'const': 27.12, 'child': -6.54, 'n_art': -1.64} {'const': '4.1e-60', 'child': '8.7e-10', 'n_art': '0.1'}
wToM True {'const': 0.912, 'child': -1.158, 'n_art': -0.119} {'const': 5.87, 'child': -6.54, 'n_art': -1.64} {'const': '2.7e-08', 'child': '8.7e-10', 'n_art': '0.1'}
wPain False {'const': 0.399, 'child': -0.135, 'n_art': -0.0} {'const': 23.38, 'child': -6.72, 'n_art': -0.51} {'const': '3.3e-52', 'child': '3.5e-10', 'n_art': '0.61'}
wPain True {'const': 0.948, 'child': -1.204, 'n_art': -0.038} {'const': 6.02, 'child': -6.72, 'n_art': -0.51} {'const': '1.2e-08', 'child': '3.5e-10', 'n_art': '0.61'}
across False {'const': -0.057, 'child': 0.087, 'n_art': 0.002} {'const': -3.49, 'child': 4.49, 'n_art': 2.87} {'const': '0.00063', 'child': '1.4e-05', 'n_art': '0.0048'}
across True {'const': -0.654, 'child': 0.83, 'n_art': 0.218} {'const': -4.03, 'child': 4.49, 'n_art': 2.87} {'const': '8.8e-05', 'child': '1.4e-05', 'n_art': '0.0048'}
wToM tom|art (0.2460452700510633, 6.286063992811235e-05)
 reg {'const': 5.45, 'ToM Booklet-Matched': 2.04, 'Age': 0.62, 'n_art': -1.14} {'const': 0.0, 'ToM Booklet-Matched': 0.044, 'Age': 0.536, 'n_art': 0.257}
across tom|art (-0.12527079010966907, 0.041603114566900586)
 reg {'const': 2.39, 'ToM Booklet-Matched': 1.29, 'Age': -2.98, 'n_art': 2.64} {'const': 0.018, 'ToM Booklet-Matched': 0.2, 'Age': 0.004, 'n_art': 0.009}
           wToM        across       
           mean    sem   mean    sem
FB_Group                            
fail      0.345  0.033  0.056  0.020
pass      0.398  0.025  0.087  0.014
wToM False {'const': -0.005, 'fail': 0.034, 'Age': 0.077, 'n_art': 0.0} {'const': -0.03, 'fail': 0.66, 'Age': 2.61, 'n_art': 0.02} {'const': 0.976, 'fail': 0.512, 'Age': 0.013, 'n_art': 0.983}
wToM True {'const': -0.086, 'fail': 0.259, 'Age': 0.49, 'n_art': 0.003} {'const': -0.45, 'fail': 0.66, 'Age': 2.61, 'n_art': 0.02} {'const': 0.654, 'fail': 0.512, 'Age': 0.013, 'n_art': 0.9
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import sys,os; exec(open(os.environ["TMPDIR"]+"/irc_dev.py").read())
ad=p[p.Child_Adult=="adult"].index; y3=p[p.AgeGroup=="3yo"].index
rois=sb.TOM_ROIS+sb.PAIN_ROIS
orig=sb.dct_highpass_basis
def run(label, **kw):
    out={}
    for grp,idx in [("adult",ad),("3yo",y3)]:
        vals=[]
        for s in idx:
            tc=sb.subject_timecourses(d[s], rois, "with_data", True)
            m=sb.irc_matrix(tc,rois); vals.append([sb.within(m,sb.TOM_ROIS),sb.within(m,sb.PAIN_ROIS),sb.across(m,sb.TOM_ROIS,sb.PAIN_ROIS)])
        out[grp]=np.round(np.mean(vals,0),3)
    print(label,out)
run("base")
for cut in [1e9, 50, 30]:
    sb.dct_highpass_basis=lambda n=168,tr=2.0,cutoff=cut: orig(n,tr,cut) if cut<1e8 else np.zeros((n,0))
    run(f"hp{cut}")
sb.dct_highpass_basis=orig
# no compcor
c=sb.clean
sb.clean=lambda ts,ind,cc,extra=None,single=False: c(ts,ind,np.zeros((0,168)),extra,single)
run("nocompcor")
sb.clean=c
EOF
```

```
base {'adult': array([ 0.604,  0.398, -0.051]), '3yo': array([0.326, 0.179, 0.074])}
hp1000000000.0 {'adult': array([0.626, 0.397, 0.032]), '3yo': array([0.334, 0.19 , 0.097])}
hp50 {'adult': array([ 0.556,  0.38 , -0.017]), '3yo': array([0.333, 0.17 , 0.072])}
hp30 {'adult': array([ 0.537,  0.375, -0.006]), '3yo': array([0.332, 0.167, 0.074])}
nocompcor {'adult': array([0.645, 0.465, 0.059]), '3yo': array([0.401, 0.286, 0.187])}
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate && cat >> $TMPDIR/irc_dev.py <<'EOF'
def net_tcs(net, z=True, z_span="movie", voxels="with_data"):
    out={}
    for s in p.index:
        tc=sb.subject_timecourses(d[s], sb.NETWORKS[net] if net!="FFA" else sb.FFA_ROIS, voxels, False)
        out[s]=sb.network_timecourse(tc, sb.NETWORKS[net] if net!="FFA" else sb.FFA_ROIS, z_span, z)
    return pd.DataFrame(out).T
EOF
python - <<'EOF' 2>&1 | grep -v Warn
import sys,os; exec(open(os.environ["TMPDIR"]+"/irc_dev.py").read())
ad=p[p.Child_Adult=="adult"].index
for span in ["movie","all"]:
  N={n:net_tcs(n,z_span=span) for n in ["ToM","Pain"]}
  for a,fdr in [(0.05,False),(0.01,False),(0.05,True)]:
    res={}
    for n in ["ToM","Pain"]:
        tab,ev=sb.reverse_correlation(N[n].loc[ad].values,a,fdr); r=sb.rank_events(ev,tab)
        res[n]=r
        print(span,a,fdr,n,len(ev), 2*r.length_tr.sum(), list(zip(r.onset,r.length_tr,r.peak_tr)))
EOF
```

```
movie 0.05 False ToM 9 80 [(129, 4, 131), (90, 9, 95), (63, 4, 64), (149, 7, 150), (45, 3, 46), (122, 5, 125), (52, 4, 54), (163, 2, 163), (24, 2, 25)]
movie 0.05 False Pain 10 84 [(107, 7, 112), (116, 5, 118), (71, 8, 77), (38, 4, 39), (158, 4, 160), (134, 3, 135), (83, 2, 84), (56, 5, 56), (142, 2, 142), (100, 2, 100)]
movie 0.01 False ToM 7 56 [(130, 3, 131), (91, 7, 95), (63, 4, 64), (150, 6, 150), (46, 2, 46), (122, 4, 125), (53, 2, 54)]
movie 0.01 False Pain 8 62 [(107, 7, 112), (116, 5, 118), (71, 7, 77), (38, 3, 39), (158, 3, 160), (134, 2, 135), (83, 2, 84), (56, 2, 56)]
movie 0.05 True ToM 7 56 [(130, 3, 131), (91, 7, 95), (63, 4, 64), (150, 6, 150), (46, 2, 46), (122, 4, 125), (53, 2, 54)]
movie 0.05 True Pain 8 62 [(107, 7, 112), (116, 5, 118), (71, 7, 77), (38, 3, 39), (158, 3, 160), (134, 2, 135), (83, 2, 84), (56, 2, 56)]
all 0.05 False ToM 9 80 [(129, 4, 131), (90, 9, 95), (63, 4, 64), (149, 7, 150), (45, 3, 46), (122, 5, 125), (52, 4, 54), (163, 2, 163), (24, 2, 25)]
all 0.05 False Pain 10 84 [(107, 7, 112), (116, 5, 118), (71, 8, 77), (38, 4, 39), (158, 4, 160), (134, 3, 135), (83, 2, 84), (56, 5, 56), (142, 2, 142), (100, 2, 100)]
all 0.01 False ToM 7 56 [(130, 3, 131), (91, 7, 95), (63, 4, 64), (150, 6, 150), (46, 2, 46), (122, 4, 125), (53, 2, 54)]
all 0.01 False Pain 8 62 [(107, 7, 112), (116, 5, 118), (71, 7, 77), (38, 3, 39), (158, 3, 160), (134, 2, 135), (83, 2, 84), (56, 2, 56)]
all 0.05 True ToM 7 56 [(130, 3, 131), (91, 7, 95), (63, 4, 64), (150, 6, 150), (46, 2, 46), (122, 4, 125), (53, 2, 54)]
all 0.05 True Pain 8 62 [(107, 7, 112), (116, 5, 118), (71, 7, 77), (38, 3, 39), (158, 3, 160), (134, 2, 135), (83, 2, 84), (56, 2, 56)]
```

**Agent calls Bash**

```bash
cd paper && source $TMPDIR/dev/bin/activate && (python -c "import fitz" 2>/dev/null || uv pip install -q pymupdf) && python - <<'EOF'
import fitz
doc=fitz.open("10.1038-s41467-018-03399-2.supp.pdf"); print(len(doc))
for i in range(9,13):
    pg=doc[i]; pix=pg.get_pixmap(dpi=110); pix.save(f"/tmp/claude-1001/supp_p{i+1}.png"); print(i+1, pg.get_text()[:200].replace("\n"," "))
EOF
ls $TMPDIR/*.png
```

```
[0;93m2026-10-28 16:22:17.210966583 [W:onnxruntime:Default, device_discovery.cc:95 GetPciBusId] Skipping pci_bus_id for PCI path at "/sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/MSFT1000:00/5620e0c7-8062-4dce-aeb7-520c7ef76171" because filename "5620e0c7-8062-4dce-aeb7-520c7ef76171" did not match expected pattern of [0-9a-f]+:[0-9a-f]+:[0-9a-f]+[.][0-9a-f]+[m
/tmp/claude-1001/dev/lib/python3.13/site-packages/fitz/__init__.py:17: FutureWarning: The `fitz` API is deprecated and will be removed in future. Use `import pymupdf` instead.
  warnings.warn(
15
10 Supplementary Table 1    Supplementary Table 1. Demographic information and behavioral data by age group.  Number of participants (N), age range and average and standard deviation of age (years), gend
11 Supplementary Table 2    Supplementary Table 2. Group regions of interest.  Contrast used, regions identified,  peak/center coordinate [x y z], and size (number of voxels) for each region of interest 
12 Supplementary Table 3    Supplementary Table 3. ToM and Pain Event details. Time (in stimulus), duration (seconds),  and peak timepoint (TR) and description for each ToM and Pain event.2 Peak timepoin
13 Supplementary Table 4    Supplementary Table 4. Average timecourse correlations. This table provides the Pearson  correlation value (r) between the average timecourse of response in each network inclu
/tmp/claude-1001/supp_p10.png
/tmp/claude-1001/supp_p11.png
/tmp/claude-1001/supp_p12.png
/tmp/claude-1001/supp_p13.png
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp_p12.png"
}
```

Result: no output.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/openneuro-ds000228-richardson-2018/social_brain.py",
 "old_string": "@lru_cache(maxsize=1)\ndef file_table() -> pd.DataFrame:",
 "new_string": "AGE_GROUPS = [\"3yo\", \"4yo\", \"5yo\", \"7yo\", \"8-12yo\"]\n\n# Supplementary Table 3 (the paper's reference, not data): event, start time in the stimulus\n# (m:ss), duration (s) and peak TR. The claims file (rc-events) reads the event's TRs as onset\n# TR = stimulus seconds / 2 + 8, for duration / 2 TRs; with it every peak TR falls inside.\nSUPP_TABLE3 = pd.DataFrame(\n    [(\"T01\", \"4:00\", 10, 131), (\"T02\", \"2:46\", 16, 96), (\"T03\", \"1:14\", 6, 46),\n     (\"T04\", \"4:42\", 14, 150), (\"T05\", \"1:28\", 8, 54), (\"T06\", \"3:48\", 10, 124),\n     (\"T07\", \"1:50\", 4, 64),\n     (\"P01\", \"3:36\", 10, 118), (\"P02\", \"2:06\", 18, 73), (\"P03\", \"3:20\", 12, 111),\n     (\"P04\", \"1:00\", 6, 39), (\"P05\", \"1:34\", 6, 56), (\"P06\", \"4:10\", 10, 135),\n     (\"P07\", \"5:02\", 4, 160), (\"P08\", \"0:42\", 4, 29), (\"P09\", \"4:28\", 4, 143),\n     (\"P10\", \"1:20\", 4, 49), (\"P11\", \"2:30\", 4, 84), (\"P12\", \"3:04\", 4, 100)],\n    columns=[\"event\", \"time\", \"duration_s\", \"peak_tr\"])\nSUPP_TABLE3[\"network\"] = np.where(SUPP_TABLE3.event.str[0] == \"T\", \"ToM\", \"Pain\")\nSUPP_TABLE3[\"onset_tr\"] = SUPP_TABLE3.time.map(\n    lambda s: int(s.split(\":\")[0]) * 60 + int(s.split(\":\")[1])) // 2 + 8\nSUPP_TABLE3[\"trs\"] = [list(range(o, o + d // 2))\n                      for o, d in zip(SUPP_TABLE3.onset_tr, SUPP_TABLE3.duration_s)]\n\n\ndef match_table_events(found_events, network: str) -> pd.Series:\n    \"\"\"For each Supplementary Table 3 event of a network, whether a found event overlaps it.\"\"\"\n    found = set(tr for e in found_events for tr in e)\n    t = SUPP_TABLE3[SUPP_TABLE3.network == network]\n    return pd.Series([bool(found & set(trs)) for trs in t.trs], index=t.event)\n\n\n@lru_cache(maxsize=1)\ndef file_table() -> pd.DataFrame:"
}
```

```
The file entries/openneuro-ds000228-richardson-2018/social_brain.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; cd  python3 -c "import nbformat, yaml, jsonschema; print('ok')"; ls executed 2>/dev/null | head -3; grep -n "def cmd_handover\|def cmd_check\|tags\|claim:" tools/entry.py | head -30
```

```
Wed Oct 28 16:22:49 UTC 2026
ok
174:        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
286:                if not any(tag in c.metadata.get("tags", []) for c in nb.cells):
```

**Agent calls Bash**

```bash
cd  sed -n 140,200p tools/entry.py; sed -n 260,330p tools/entry.py
```

```
requirements, lock = entry_dir / "requirements.in", entry_dir / "requirements.lock.txt"
    if not requirements.is_file():
        report.error(rel, "no requirements.in")
    elif not lock.is_file():
        report.error(rel, "no requirements.lock.txt; run `tools/entry.py lock`")
    else:
        pinned = {re.split(r"[=<>!~\[ ]", line, maxsplit=1)[0].lower().replace("_", "-")
                  for line in lock.read_text().splitlines() if line and not line.startswith((" ", "#"))}
        for line in requirements.read_text().splitlines():
            name = re.split(r"[=<>!~\[ ;]", line.strip(), maxsplit=1)[0].lower().replace("_", "-")
            if name and not name.startswith("#") and name not in pinned:
                report.error(rel / "requirements.lock.txt", f"{name} is required but not locked; re-run lock")

    # Datasets are related as <archive>:<id>/<version> (docs/archives.md); papers as doi:, entries as entry:.
    used = [r["id"].split(":", 1)[1].partition("/")
            for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))]
    archives = {r["id"].split(":", 1)[1].partition("/")[0]: r["id"].split(":", 1)[0]
                for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))}
    dandisets = [d for d, _, _ in used]
    versions = {d: v for d, _, v in used}
[... 111 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper && grep -n "Supplementary Note 1\|face events\|Face events" -i 10.1038-s41467-018-03399-2.txt | head; grep -n "Williams" 10.1038-s41467-018-03399-2.txt | head
```

```
470:Supplementary Note 1 for a similar overlap analysis between
2019:network and Pain matrix, and for the bilateral fusiform regions used in Supplementary Note 1 
2052:Supplementary Note 1: Face events overlap analysis 
2054:identified as face events and timepoints identified as ToM or pain events was significantly different 
2057:permuted face timecourses included seven face events, with durations of 16, 4, 5, 7, 4, 4, 4 TRs (see 
1876:than within-Scene and within-M1 correlations (Williams’ test of differences in age correlations:
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-018-03399-2.txt",
 "offset": 1820,
 "limit": 250
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u
```

```
Wed Oct 28 16:23:33 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat, sys, json\nfrom nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell\n\ncells = []\ndef md(s, tags=None):\n    c = new_markdown_cell(s.strip(\"\\n\"))\n    if tags: c.metadata[\"tags\"] = tags\n    cells.append(c)\ndef code(s, tags=None):\n    c = new_code_cell(s.strip(\"\\n\"))\n    if tags: c.metadata[\"tags\"] = tags\n    cells.append(c)\n\nexec(open(sys.argv[1]).read())\nnb = new_notebook(cells=cells, metadata={\"kernelspec\": {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}})\nnbformat.write(nb, sys.argv[2])\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/cells.py",
 "content": "md(r'''\n# Richardson et al. (2018) on OpenNeuro ds000228, snapshot 1.1.1\n\nPaper: Richardson, Lisandrelli, Riobueno-Naylor & Saxe (2018), \"Development of the social brain\nfrom age three to twelve years\", Nature Communications 9, 1027,\n[doi:10.1038/s41467-018-03399-2](https://doi.org/10.1038/s41467-018-03399-2).\n\nDataset: [OpenNeuro ds000228](https://openneuro.org/datasets/ds000228/versions/1.1.1), snapshot\n`1.1.1`, DOI 10.18112/openneuro.ds000228.v1.1.1. The paper cites the dataset on OpenfMRI\nwithout a version; the claims file names snapshot 1.1.1, which is also the latest published\nsnapshot. Its CHANGES file says 1.1.1 only updated the citation to the paper (2023), so the\npinned snapshot holds the same data as 1.1.0. It is pinned because the claims file gives it and\nthe protocol pins the latest published version when the paper cites none.\n\nClaims: `claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml`, written from the version of\nrecord and its Supplementary Information (Supplementary Tables 1 to 4 read from the PDF). Its\nheader labels the shared pipeline P1 to P9 and the open details O1 to O9; this notebook uses the\nsame labels.\n\nWhat the snapshot holds (listed below from the archive): for all 155 participants the raw BOLD\nand T1 images and the paper's own preprocessed data (SPM8, normalized, smoothed; ART artifact\nindicators and five CompCor regressors per run; white-matter and brain masks), the group ROIs\nof every network the paper uses (ToM, Pain, face and scene parcels, M1, V1), and the behavioural\nscores in participants.tsv. Every file is read into memory from its URL pinned to the snapshot.\n\n| Claim | Tested here |\n|---|---|\n| participants, supp-table1-behavior-by-age, beh-tom-age, beh-tom-dccs, beh-fb-groups, beh-fb-tom, beh-fb-age, beh-fb-dccs | tested (participants.tsv) |\n| motion-child-adult, motion-not-age-tom, motion-not-fb | tested (deposited ART indicators) |\n| irc-adult, irc-age-within, irc-age-across, irc-adult-vs-child, irc-3yo-distinct, irc-3yo-not-anticorrelated, irc-3yo-homologous, irc-3yo-nonbilateral, irc-tom-behavior, irc-tom-behavior-age, irc-fb-within, irc-fb-within-dccs, irc-fb-across | tested (deposited preprocessed BOLD and ROIs) |\n| irc-control-networks, irc-williams, supp-table4-other-networks, face-rc, face-overlap | tested; the face and scene parcels the claims file lists as outside input are deposited in the snapshot |\n| rc-events, rc-overlap, rc-child-adult-timecourse, rc-age-events, rc-t04-tom, rc-fb-no-difference, rc-3yo-events | tested |\n| maturity-across, maturity-within, maturity-tom-behavior, maturity-fb | tested |\n| replication-sample | blocked: the independent sample of 20 adults is not deposited anywhere |\n| hand-coded-events | blocked: the hand coding of Jacoby et al. 2016 is not in the snapshot or the paper |\n''')\n\ncode(r'''\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom statsmodels.stats.multicomp import pairwise_tukeyhsd\nimport matplotlib.pyplot as plt\nimport social_brain as sb\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\nprint(\"dataset\", sb.DATASET_ID, \"snapshot\", sb.SNAPSHOT, \"doi\", sb.SNAPSHOT_DOI)\nfiles = sb.file_table()\nprint(len(files), \"files,\", round(files[\"size\"].sum() / 1e9, 2), \"GB\")\nkinds = files.index.str.replace(r\"sub-pixar\\d+\", \"sub-*\", regex=True)\nprint(files.groupby(kinds)[\"size\"].agg([\"count\", \"sum\"]).rename(columns={\"sum\": \"bytes\"}).to_string())\n''')\n\ncode(r'''\n# The files read whole, with their checksums (OpenNeuro `id`); the per-participant files read are\n# the swrf BOLD image and the nuisance-regressor file of each participant, listed after extraction.\nfor f in [\"dataset_description.json\", \"README\", \"CHANGES\", \"participants.tsv\", \"participants.json\",\n          \"task-pixar_bold.json\", \"derivatives/README.txt\"]:\n    print(f, files.loc[f, \"id\"])\nfor r in sb.ALL_ROIS:\n    f = [k for k in files.index if k.startswith(\"derivatives/ROIs/\" + r)]\n    print(f[0], files.loc[f[0], \"id\"])\nprint()\nprint(sb.text(\"CHANGES\"))\nprint(sb.text(\"README\"))\n''')\n\ncode(r'''\nprint(sb.text(\"derivatives/README.txt\"))\nprint(sb.text(\"participants.json\"))\nprint(sb.text(\"task-pixar_bold.json\"))\n''')\n\nmd(r'''\n## Loading\n\nEach participant's preprocessed image (`*_swrf_bold.nii.gz`, about 90 MB) is read into memory,\nand the voxels of the 29 deposited ROIs are kept; the nuisance file gives the artifact\nindicators and the CompCor regressors. This takes about two minutes.\n''')\n\ncode(r'''\np = sb.participants()\nsubs = list(p.participant_id)\nD = sb.extract_all(subs, n_threads=8)\np[\"n_art\"] = [len(sb.artifact_index(D[s][\"artifacts\"])) for s in subs]\np = p.set_index(\"participant_id\")\nTOM, NOFB, DCCS = \"ToM Booklet-Matched\", \"ToM Booklet-Matched-NOFB\", \"DCCS Summary\"\nchildren = p[p.Child_Adult == \"child\"].copy()\nadults = p[p.Child_Adult == \"adult\"].copy()\nyoung = children[children.Age < 6].copy()\nprint(len(subs), \"participants loaded\")\nprint(pd.Series({s: files.loc[sb.derivative(s, \"task-pixar_run-001_swrf_bold.nii.gz\"), \"id\"]\n                 for s in subs[:3]}).to_string(), \"... (checksums of all 155 in `files`)\")\n''')\n\nmd(r'''\n## Data check\n''')\n\ncode(r'''\nprint(\"participants.tsv columns:\", list(p.reset_index().columns))\nprint(p.reset_index().describe(include=\"all\").T.to_string())\nprint()\nprint(\"children\", len(children), \"adults\", len(adults))\nprint(\"children: female\", (children.Gender == \"F\").sum(), \"mean age %.2f (s.d. %.2f)\" % (children.Age.mean(), children.Age.std()),\n      \"range %.2f to %.2f\" % (children.Age.min(), children.Age.max()))\nprint(\"adults: female\", (adults.Gender == \"F\").sum(), \"mean age %.2f (s.d. %.2f)\" % (adults.Age.mean(), adults.Age.std()),\n      \"range %.0f to %.0f\" % (adults.Age.min(), adults.Age.max()))\nprint(p.groupby(\"AgeGroup\").Age.agg([\"count\", \"min\", \"max\", \"mean\", \"std\"]).round(2).to_string())\nprint(\"handedness:\", p.groupby(\"Child_Adult\").Handedness.value_counts().to_dict())\nprint(\"under 6:\", len(young), \"FB groups\", young.FB_Group.value_counts().to_dict(),\n      \"; FB_Group in children aged 6 and over:\", children[children.Age >= 6].FB_Group.value_counts().to_dict())\nprint(\"DCCS present:\", children[DCCS].notna().sum(), \"children, all aged under 6:\", bool((children.loc[children[DCCS].notna(), \"Age\"] < 6).all()))\nprint(\"FB_Composite against FB_Group (cut-offs of the Methods):\")\nprint(pd.crosstab(young.FB_Composite, young.FB_Group).to_string())\nprint(\"ToM score range %.2f to %.2f; no-FB score range %.2f to %.2f\" % (children[TOM].min(), children[TOM].max(), children[NOFB].min(), children[NOFB].max()))\nprint()\nprint(\"voxel size by age group (Methods: 3.13 mm for 5 + 28 adults, 3 7yo, 20 8-12yo):\")\nprint(pd.crosstab(p.AgeGroup, [p[\"Scanlog: Voxel slize\"], p[\"Scanlog: Slice Gap\"].fillna(0)]).to_string())\nprint(\"coil:\", pd.crosstab(p.AgeGroup, p[\"Scanlog: Coil\"]).to_dict())\n''', tags=[\"sanity\"])\n\ncode(r'''\nshapes = {tuple(D[s][\"shape\"]) for s in subs}\nzooms = {tuple(float(z) for z in D[s][\"zooms\"][:3]) for s in subs}\nprint(\"preprocessed image shapes:\", shapes, \"voxel sizes (mm):\", zooms, \"dtype:\", {D[s][\"dtype\"] for s in subs})\nprint(\"affines identical:\", all(np.allclose(D[s][\"affine\"], D[subs[0]][\"affine\"]) for s in subs))\nprint(\"168 volumes in every image (TR 2 s from task-pixar_bold.json):\", all(D[s][\"shape\"][3] == sb.N_TR for s in subs))\nprint(\"artifact indicator rows each flag one timepoint:\", all((D[s][\"artifacts\"].sum(axis=1) == 1).all() for s in subs))\nprint(\"CompCor rows per participant:\", {D[s][\"compcor\"].shape for s in subs})\nprint(\"artifact timepoints per participant: max %d of 168 (%.2f; Methods drop at one third)\" % (p.n_art.max(), p.n_art.max() / 168))\nprint(p.groupby(\"AgeGroup\").n_art.agg([\"mean\", \"std\", \"min\", \"max\"]).round(2).to_string())\nroi_size = pd.Series({r: D[subs[0]][\"rois\"][r][\"n_vox\"] for r in sb.ALL_ROIS})\nprint(\"ROI sizes (voxels):\", roi_size.to_dict())\nprint(\"Supplementary Table 2 sizes: RTPJ 376 LTPJ 368 PC 382 DMPFC 217 MMPFC 275 VMPFC 198; RS2 368 LS2 269 RInsula 309 LInsula 240 RMFG 142 LMFG 256 AMCC 249; RFFA 1019 LFFA 531\")\ncover = pd.DataFrame({s: {r: D[s][\"rois\"][r][\"n_with_data\"] for r in sb.ALL_ROIS} for s in subs}).T\nprint(\"participants with any ROI voxel without data (zero or non-finite at some timepoint), per ROI:\")\nprint((cover < roi_size).sum().to_string())\nprint(\"fewest voxels with data in a face ROI:\", int(cover[sb.FACE_ROIS].min().min()),\n      \"(Supplementary Fig. 4: every participant had at least 100 voxels in every face ROI)\")\nface_incomplete = (cover[sb.FACE_ROIS] < roi_size[sb.FACE_ROIS]).any(axis=1)\nprint(\"participants with incomplete face-ROI coverage:\", int(face_incomplete.sum()),\n      p.loc[face_incomplete[face_incomplete].index, \"AgeGroup\"].value_counts().to_dict(),\n      \"(Supplementary Fig. 4: 17, of them 2 adults, 12 8-12yo, one each 7yo, 4yo, 3yo)\")\n''', tags=[\"sanity\"])\n\nmd(r'''\nTiming check. There are no events files; the movie timing is fixed (README: TRs 1 to 5 rest,\n6 to 10 logos, movie from TR 11). Two checks that the image volumes and the regressors share the\nsame clock: (1) the artifact indicators should fall on the timepoints where the ROI signal jumps,\ncompared with the same indicators shifted in time; (2) the adult ToM-network signal should be\nhigher during the paper's ToM events than during its pain events (Supplementary Table 3), and the\ncontrast should drop when the event labels are shifted in time.\n''')\n\ncode(r'''\ndef jump_at(s, shift):\n    x = np.mean([D[s][\"rois\"][r][\"all\"] for r in sb.TOM_ROIS + sb.PAIN_ROIS], axis=0)\n    dx = np.abs(np.diff(x, prepend=x[0]))\n    dx = dx / np.median(dx[dx > 0])\n    a = (sb.artifact_index(D[s][\"artifacts\"]) + shift) % sb.N_TR\n    return np.mean(dx[a]) if len(a) else np.nan\nfor shift in [0, 1, 2, 5, 20]:\n    vals = [jump_at(s, shift) for s in subs if p.loc[s, \"n_art\"] > 0]\n    print(f\"artifact indicators shifted by {shift:2d} TRs: median over participants of the ROI-signal jump at flagged TRs (in units of the median jump) = {np.nanmedian(vals):.2f}\")\n''', tags=[\"sanity\"])\n\nmd(r'''\n## Behaviour (participants.tsv)\n\n### participants\n\n> The sample is 122 children aged 3.5 to 12 years (64 female) and 33 adults aged 18 to 39 (20\n> female); five further children were excluded for excessive motion. By age group there are 17,\n> 14, 34, 23 and 34 children aged 3, 4, 5, 7 and 8 to 12 years.\n''')\n\ncode(r'''\ncounts = {\"children\": len(children), \"adults\": len(adults), \"female children\": int((children.Gender == \"F\").sum()),\n          \"female adults\": int((adults.Gender == \"F\").sum())}\ncounts.update({f\"children {g}\": int((children.AgeGroup == g).sum()) for g in sb.AGE_GROUPS})\ncounts[\"mean child age\"] = round(children.Age.mean(), 2)\nexpected = [122, 33, 64, 20, 17, 14, 34, 23, 34, 6.7]\nprint(pd.DataFrame({\"measured\": counts, \"expected\": expected}).to_string())\nprint(\"Age-group ranges:\", children.groupby(\"AgeGroup\").Age.agg([\"min\", \"max\"]).round(2).to_dict(\"index\"))\nprint(\"The 5 children excluded for motion are not in the dataset (155 participants listed).\")\n''', tags=[\"claim:participants\"])\nmd('**Result: TBD**')\n\nmd(r'''\n### supp-table1-behavior-by-age\n\n> Mean ToM score rises across age groups (3yo .54, 4yo .63, 5yo .73, 7yo .88, 8-12yo .96), and\n> the false-belief groups (pass/inconsistent/fail) are 4/4/9 at 3 years, 3/7/4 at 4 years and\n> 23/9/2 at 5 years.\n''')\ncode(r'''\nm = children.groupby(\"AgeGroup\")[TOM].agg([\"mean\", \"std\", \"count\"]).loc[sb.AGE_GROUPS]\nm[\"expected\"] = [0.54, 0.63, 0.73, 0.88, 0.96]\nm[\"within 10%\"] = (m[\"mean\"] - m.expected).abs() <= 0.1 * m.expected\nprint(m.round(3).to_string())\nfb = pd.crosstab(young.AgeGroup, young.FB_Group)[[\"pass\", \"inc\", \"fail\"]]\nprint(fb.to_string())\nprint(\"expected 3yo 4/4/9, 4yo 3/7/4, 5yo 23/9/2; totals\", fb.sum().to_dict(), \"(expected 30, 20, 15)\")\n''', tags=[\"claim:supp-table1-behavior-by-age\"])\nmd('**Result: TBD**')\n\nmd(r'''\n### beh-tom-age\n\n> Among children, ToM score (proportion correct) increases with age (Kendall tau = .66), and\n> among the 3- to 5-year-olds DCCS summary score also increases with age (Kendall tau = .20).\n''')\ncode(r'''\nt1 = sb.kendall(children[TOM], children.Age)\nyd = young.dropna(subset=[DCCS])\nt2 = sb.kendall(yd[DCCS], yd.Age)\nprint(f\"ToM score ~ age, n = {len(children)}: tau-b = {t1[0]:.3f}, p = {t1[1]:.2g} (paper .66, p < .00001)\")\nprint(f\"DCCS ~ age, n = {len(yd)}: tau-b = {t2[0]:.3f}, p = {t2[1]:.3f} (paper .20, p = .049)\")\nfor v in [\"a\", \"c\"]:\n    print(f\"  variant tau-{v}:\", round(stats.kendalltau(children[TOM], children.Age, variant=v).statistic, 3),\n          round(stats.kendalltau(yd[DCCS], yd.Age, variant=v).statistic, 3))\n''', tags=[\"claim:beh-tom-age\"])\nmd('**Result: TBD**')\n\nmd(r'''\n### beh-tom-dccs\n\n> In 3- to 5-year-olds, ToM and DCCS scores are positively correlated controlling for age\n> (partial Kendall tau = .19).\n''')\ncode(r'''\nr, pv = sb.partial_kendall(yd[TOM], yd[DCCS], yd.Age)\nprint(f\"partial tau(ToM, DCCS | age), n = {len(yd)}: {r:.3f}, p = {pv:.3f} (paper .19, p = .03)\")\n''', tags=[\"claim:beh-tom-dccs\"])\nmd('**Result: TBD**')\n\nmd(r'''\n### beh-fb-groups\n\n> Among the 65 children aged 3 to 5, the false-belief composite gives 30 passers (15 female), 20\n> inconsistent performers (13 female) and 15 failers (6 female).\n''')\ncode(r'''\ng = young.groupby(\"FB_Group\").agg(n=(\"Age\", \"size\"), female=(\"Gender\", lambda x: int((x == \"F\").sum())),\n                                  age_mean=(\"Age\", \"mean\"), age_sd=(\"Age\", \"std\"))\nprint(g.round(2).to_string())\nrecut = pd.cut(young.FB_Composite, [-1, 2, 4, 6], labels=[\"fail\", \"inc\", \"pass\"]).astype(str)\nprint(\"groups recomputed from FB_Composite agree with FB_Group:\", bool((recut == young.FB_Group).all()))\nprint(\"handedness by group:\", young.groupby(\"FB_Group\").Handedness.value_counts().to_dict())\n''', tags=[\"claim:beh-fb-groups\"])\nmd('**Result: TBD**')\n\nmd(r'''\n### beh-fb-tom, beh-fb-age, beh-fb-dccs\n\n> False-belief failers and inconsistent performers score lower than passers on the remaining ToM\n> items (means .55, .57 and .75). False-belief failers are younger than inconsistent performers\n> and passers (mean ages 4.1, 4.8 and 5.2 years). False-belief failers have lower DCCS scores than\n> the other two groups (means 1.73, 2.26, 2.33).\n\nTukey HSD over the three groups (statsmodels `pairwise_tukeyhsd`), diffs under both scales of O9;\nKruskal-Wallis from scipy.\n''')\ncode(r'''\ndef fb_tests(var):\n    sub = young.dropna(subset=[var])\n    out = sub.groupby(\"FB_Group\")[var].agg([\"mean\", \"sem\", \"count\"]).loc[[\"fail\", \"inc\", \"pass\"]]\n    print(out.round(3).to_string())\n    kw = stats.kruskal(*[sub.loc[sub.FB_Group == g, var] for g in [\"pass\", \"inc\", \"fail\"]])\n    print(f\"Kruskal-Wallis H = {kw.statistic:.2f}, p = {kw.pvalue:.2g}\")\n    for scale in [\"z-scored (O9a)\", \"raw (O9b)\"]:\n        v = (sub[var] - sub[var].mean()) / sub[var].std() if scale.startswith(\"z\") else sub[var]\n        t = pairwise_tukeyhsd(v.values, sub.FB_Group.values)\n        df = pd.DataFrame(t.summary().data[1:], columns=t.summary().data[0])\n        print(\" Tukey,\", scale); print(df.to_string(index=False))\n    return out, kw\n\nprint(\"== beh-fb-tom, reading (a): 18 non-FB items (ToM Booklet-Matched-NOFB)\")\nfbtom_a = fb_tests(NOFB)\nprint(\"\\n== beh-fb-tom, reading (b): full ToM score\")\nfbtom_b = fb_tests(TOM)\n''', tags=[\"claim:beh-fb-tom\"])\nmd('**Result: TBD**')\ncode(r'''\nfbage = fb_tests(\"Age\")\n''', tags=[\"claim:beh-fb-age\"])\nmd('**Result: TBD**')\ncode(r'''\nfbdccs = fb_tests(DCCS)\n''', tags=[\"claim:beh-fb-dccs\"])\nmd('**Result: TBD**')\n\nmd(r'''\n## Motion\n\nThe number of artifact timepoints is the number of ART indicator rows in each participant's\ndeposited nuisance file (P2).\n\n### motion-child-adult\n\n> Children have more artifact timepoints than adults (mean 10.5 against 2.8).\n''')\ncode(r'''\nw = stats.ttest_ind(children.n_art, adults.n_art, equal_var=False)\nprint(p.groupby(\"Child_Adult\").n_art.agg([\"mean\", \"std\", \"count\"]).round(2).to_string())\nprint(f\"Welch t = {w.statistic:.2f}, df = {w.df:.1f}, p = {w.pvalue:.2g} (paper t(137.7) = 6.49, p < .000001)\")\n''', tags=[\"claim:motion-child-adult\"])\nmd('**Result: TBD**')\n\nmd(r'''\n### motion-not-age-tom\n\n> Among children, the number of artifact timepoints is not correlated with age or with ToM score.\n''')\ncode(r'''\nrs = stats.spearmanr(children.n_art, children.Age)\nrk = sb.kendall(children.n_art, children[TOM])\nprint(f\"Spearman(n_art, age) = {rs.statistic:.3f}, p = {rs.pvalue:.2f} (paper .02, p = .86)\")\nprint(f\"Kendall(n_art, ToM score) = {rk[0]:.3f}, p = {rk[1]:.2f} (paper -.005, p = .94)\")\n''', tags=[\"claim:motion-not-age-tom\"])\nmd('**Result: TBD**')\n\nmd(r'''\n### motion-not-fb\n\n> In 3- to 5-year-olds, the number of artifact timepoints does not differ between false-belief\n> passers and failers, nor vary with DCCS score.\n''')\ncode(r'''\npf = young[young.FB_Group.isin([\"pass\", \"fail\"])].copy()\npf[\"fail\"] = (pf.FB_Group == \"fail\").astype(float)\nfor z in [False, True]:\n    r1 = sb.ols(pf, \"n_art\", [\"fail\"], zscore=z)\n    r2 = sb.ols(yd, \"n_art\", [DCCS], zscore=z)\n    print(f\"{'z-scored (O4a)' if z else 'raw (O4b)'}: FB group (fail = 1, n = {int(r1.nobs)}) b = {r1.params['fail']:.3f}, t = {r1.tvalues['fail']:.2f}, p = {r1.pvalues['fail']:.2f};\"\n          f\" DCCS (n = {int(r2.nobs)}) b = {r2.params[DCCS]:.3f}, t = {r2.tvalues[DCCS]:.2f}, p = {r2.pvalues[DCCS]:.2f}\")\nprint(\"paper: FB b = -.04, t = -.12, p = .9; DCCS b = .16, t = 1.18, p = .25\")\n''', tags=[\"claim:motion-not-fb\"])\nmd('**Result: TBD**')\n\nmd(r'''\n## Inter-region correlation\n\nPipeline P4 and P5 on the deposited preprocessed images. For each participant, every ROI\ntimecourse is cleaned (`sb.clean`) and correlated with every other. Readings run: O1 (all voxels\nof the deposited masks, `all`, or only voxels with data, `with_data`; the deposited masks match\nSupplementary Table 2 so reading O1b, full spheres, is not needed), O2 (one indicator per\nartifact timepoint, a, or one regressor, b) and O3 (all 168 TRs, a, or TRs 11 to 168, b). The\nmain reading is O1 all, O2a (the deposited regressors), O3a.\n''')\ncode(r'''\nREADINGS = [(v, s, m) for v in [\"all\", \"with_data\"] for s in [False, True] for m in [False, True]]\ndef reading_name(r):\n    return f\"O1 {r[0]}, O2{'b' if r[1] else 'a'}, O3{'b' if r[2] else 'a'}\"\nMAIN = (\"all\", False, False)\nTP = sb.TOM_ROIS + sb.PAIN_ROIS\nBILATERAL = {\"a\": [(\"RTPJ\", \"LTPJ\"), (\"RS2\", \"LS2\"), (\"RInsula\", \"LInsula\"), (\"RMFG\", \"LMFG\")],\n             \"b\": [(\"RTPJ\", \"LTPJ\"), (\"RInsula\", \"LInsula\")]}\n\ndef irc_measures(reading, m1):\n    voxels, single, movie = reading\n    trs = np.arange(sb.FIRST_MOVIE_TR - 1, sb.N_TR) if movie else None\n    rois = TP if m1 else sb.ALL_ROIS\n    rows, mats = {}, {}\n    for s in subs:\n        tc = sb.subject_timecourses(D[s], rois, voxels, m1, single)\n        m = sb.irc_matrix(tc, rois, trs)\n        mats[s] = m\n        row = {\"wToM\": sb.within(m, sb.TOM_ROIS), \"wPain\": sb.within(m, sb.PAIN_ROIS),\n               \"across\": sb.across(m, sb.TOM_ROIS, sb.PAIN_ROIS)}\n        for k, pairs in BILATERAL.items():\n            row[f\"wToM_nonbi_{k}\"] = sb.within(m, sb.TOM_ROIS, pairs)\n            row[f\"wPain_nonbi_{k}\"] = sb.within(m, sb.PAIN_ROIS, pairs)\n        if not m1:\n            for net in [\"Face\", \"Scene\", \"M1\", \"V1\"]:\n                row[\"w\" + net] = sb.within(m, sb.NETWORKS[net])\n            row[\"aFaceScene\"] = sb.across(m, sb.FACE_ROIS, sb.SCENE_ROIS)\n            row[\"aM1V1\"] = sb.across(m, sb.M1_ROIS, sb.V1_ROIS)\n        rows[s] = row\n    return pd.DataFrame(rows).T.join(p), mats\n\nIRC = {r: irc_measures(r, True) for r in READINGS}          # M1 regressed: main-text analyses\nIRC_NOM1 = {r: irc_measures(r, False) for r in READINGS}    # no M1 regression: Supplementary Fig. 3\nirc = IRC[MAIN][0]\nprint(irc.groupby(\"AgeGroup\")[[\"wToM\", \"wPain\", \"across\"]].agg([\"mean\", \"sem\"]).round(3).to_string())\nprint(\"ranges:\", irc[[\"wToM\", \"wPain\", \"across\"]].agg([\"min\", \"max\"]).round(3).to_dict())\n''')\n\ncode(r'''\nfig, axes = plt.subplots(1, 3, figsize=(12, 3.2), sharey=True)\norder = sb.AGE_GROUPS + [\"Adult\"]\nfor ax, v in zip(axes, [\"wToM\", \"wPain\", \"across\"]):\n    ax.boxplot([irc.loc[irc.AgeGroup == g, v] for g in order], tick_labels=order)\n    ax.axhline(0, color=\"grey\", lw=0.5); ax.set_title(v)\naxes[0].set_ylabel(\"Fisher z (main reading)\")\nplt.tight_layout(); plt.show()\nprint(\"all values shown; y range\", round(irc[[\"wToM\", \"wPain\", \"across\"]].min().min(), 3), \"to\", round(irc[[\"wToM\", \"wPain\", \"across\"]].max().max(), 3))\n''')\n\nmd(r'''\n### irc-adult\n\n> In adults, within-ToM (mean z .48) and within-Pain (.35) correlations are strongly positive and\n> the across-network correlation is negative (-.17), each within-network value exceeding the\n> across-network value.\n''')\ncode(r'''\ndef tol(v, e, t):\n    return abs(v - e) <= t + 1e-12\nrows = []\nfor r in READINGS:\n    a = IRC[r][0].loc[adults.index]\n    t1 = stats.ttest_rel(a.wToM, a.across); t2 = stats.ttest_rel(a.wPain, a.across)\n    rows.append({\"reading\": reading_name(r), \"wToM\": a.wToM.mean(), \"wPain\": a.wPain.mean(), \"across\": a.across.mean(),\n                 \"t ToM-across\": t1.statistic, \"p1\": t1.pvalue, \"t Pain-across\": t2.statistic, \"p2\": t2.pvalue})\nres = pd.DataFrame(rows)\nres[\"values in tolerance\"] = [sum([tol(x.wToM, .48, .02), tol(x.wPain, .35, .02), tol(x.across, -.17, .02),\n                                    tol(x[\"t ToM-across\"], 19.1, 1.91), tol(x[\"t Pain-across\"], 23.2, 2.32)]) for _, x in res.iterrows()]\nprint(res.to_string(float_format=lambda x: f\"{x:.3g}\"))\nprint(\"expected: .48, .35, -.17, t 19.1, t 23.2 (5 values)\")\n''', tags=[\"claim:irc-adult\"])\nmd('**Result: TBD**')\n\nmd(r'''\n### irc-age-within and irc-age-across\n\n> Among children, within-ToM and within-Pain correlations increase with age, controlling for\n> motion. Among children, the across-network correlation decreases with age.\n\nPartial Spearman correlation with the number of artifact timepoints as covariate (ppcor form).\n''')\ncode(r'''\nrows = []\nfor r in READINGS:\n    c = IRC[r][0].loc[children.index]\n    row = {\"reading\": reading_name(r)}\n    for v in [\"wToM\", \"wPain\", \"across\"]:\n        rr, pv, df = sb.partial_spearman(c[v], c.Age, c.n_art)\n        row[v + \" rs\"], row[v + \" p\"] = rr, pv\n    rows.append(row)\nage_irc = pd.DataFrame(rows)\nprint(age_irc.to_string(float_format=lambda x: f\"{x:.3g}\"))\nprint(\"df =\", df, \"; expected wToM .37 (p < .00005), wPain .28 (p = .002), across -.35 (p < .0001), tolerance 10%\")\n''', tags=[\"claim:irc-age-within\", \"claim:irc-age-across\"])\nmd('**Result: TBD**')\n\nmd(r'''\n### irc-adult-vs-child\n\n> Adults have higher within-ToM and within-Pain correlations and a more negative across-network\n> correlation than children, controlling for motion.\n\nRegression of each measure on group (child = 1, adult = 0) and number of artifact timepoints.\n''')\ncode(r'''\nrows = []\nfor r in READINGS:\n    t = IRC[r][0].copy(); t[\"child\"] = (t.Child_Adult == \"child\").astype(float)\n    for v in [\"wToM\", \"wPain\", \"across\"]:\n        f = sb.ols(t, v, [\"child\", \"n_art\"]); fz = sb.ols(t, v, [\"child\", \"n_art\"], zscore=True)\n        rows.append({\"reading\": reading_name(r), \"measure\": v, \"b raw\": f.params[\"child\"], \"b z (O4a)\": fz.params[\"child\"],\n                     \"t\": f.tvalues[\"child\"], \"p\": f.pvalues[\"child\"], \"t motion\": f.tvalues[\"n_art\"], \"p motion\": f.pvalues[\"n_art\"]})\nprint(pd.DataFrame(rows).to_string(float_format=lambda x: f\"{x:.3g}\"))\nprint(\"expected t: wToM -5.7, wPain -3.8, across 7.2 (10%); paper motion effect: wToM t = -4.3, others n.s.\")\n''', tags=[\"claim:irc-adult-vs-child\"])\nmd('**Result: TBD**')\n\nmd(r'''\n### irc-control-networks and irc-williams\n\n> Without M1 regression, within-ToM (rs .39), within-Pain (.38), within-Scene (.23) and within-M1\n> (.30) correlations rise with age in children, within-Face and within-V1 do not, and the across\n> ToM-Pain correlation falls with age (-.26) while across Face-Scene and M1-V1 do not change.\n\nThe face and scene parcels are those deposited in derivatives/ROIs (the same Julian et al. 2012\nparcels the claims file names as an outside input).\n''')\ncode(r'''\nCTRL = [\"wToM\", \"wPain\", \"wScene\", \"wM1\", \"across\", \"wFace\", \"wV1\", \"aFaceScene\", \"aM1V1\"]\nEXP = {\"wToM\": .39, \"wPain\": .38, \"wScene\": .23, \"wM1\": .30, \"across\": -.26}\nrows = []\nfor r in READINGS:\n    c = IRC_NOM1[r][0].loc[children.index]\n    for v in CTRL:\n        rr, pv, _ = sb.partial_spearman(c[v], c.Age, c.n_art)\n        rows.append({\"reading\": reading_name(r), \"measure\": v, \"rs\": rr, \"p\": pv,\n                     \"expected\": EXP.get(v, np.nan), \"in tolerance\": tol(rr, EXP[v], abs(EXP[v]) * .1) if v in EXP else None})\nctrl = pd.DataFrame(rows)\nprint(ctrl.pivot(index=\"reading\", columns=\"measure\", values=\"rs\")[CTRL].round(3).to_string())\nprint(ctrl.pivot(index=\"reading\", columns=\"measure\", values=\"p\")[CTRL].round(4).to_string())\nprint(\"paper: wToM .39 (<.0001), wPain .38 (<.0001), wScene .23 (.01), wM1 .30 (.001), across -.26 (.005); wFace .06 (.53), wV1 -.16 (.09), aFaceScene .02 (.8), aM1V1 .18 (.05)\")\nprint(\"adult means (main reading):\", IRC_NOM1[MAIN][0].loc[adults.index, CTRL].mean().round(3).to_dict())\n''', tags=[\"claim:irc-control-networks\"])\nmd('**Result: TBD**')\n\ncode(r'''\nPAIRS = [(\"wToM\", \"wFace\"), (\"wPain\", \"wFace\"), (\"wToM\", \"wScene\"), (\"wPain\", \"wScene\"), (\"wToM\", \"wM1\"), (\"wPain\", \"wM1\"),\n         (\"wToM\", \"wV1\"), (\"wPain\", \"wV1\"), (\"across\", \"aFaceScene\"), (\"across\", \"aM1V1\")]\nSHOULD = [True, True, False, False, False, False, True, True, True, True]\nrows = []\nfor r in READINGS:\n    c = IRC_NOM1[r][0].loc[children.index]\n    for reading_w in [\"a (partial, motion)\", \"b (no covariate)\"]:\n        for (x, y), should in zip(PAIRS, SHOULD):\n            if reading_w.startswith(\"a\"):\n                rx = sb.partial_spearman(c[x], c.Age, c.n_art)[0]; ry = sb.partial_spearman(c[y], c.Age, c.n_art)[0]\n                rxy = sb.partial_spearman(c[x], c[y], c.n_art)[0]\n            else:\n                rx = stats.spearmanr(c[x], c.Age).statistic; ry = stats.spearmanr(c[y], c.Age).statistic\n                rxy = stats.spearmanr(c[x], c[y]).statistic\n            w = sb.williams(rx, ry, rxy, len(c))\n            sig = w[\"p_t\"] < .05\n            same_dir = (abs(rx) > abs(ry))\n            rows.append({\"reading\": reading_name(r), \"williams\": reading_w, \"pair\": f\"{x} vs {y}\", \"r age x\": rx, \"r age y\": ry,\n                         \"r xy\": rxy, \"t\": w[\"t\"], \"p_t\": w[\"p_t\"], \"z\": w[\"z\"], \"p_z\": w[\"p_z\"], \"paper significant\": should,\n                         \"as paper\": (sig and same_dir) if should else (not sig)})\nwil = pd.DataFrame(rows)\nprint(wil[(wil.reading == reading_name(MAIN))].drop(columns=\"reading\").to_string(float_format=lambda x: f\"{x:.3g}\"))\nprint(wil.groupby([\"reading\", \"williams\"])[\"as paper\"].sum().rename(\"comparisons as in the paper, of 10\").to_string())\n''', tags=[\"claim:irc-williams\"])\nmd('**Result: TBD**')\n\nmd(r'''\n### irc-3yo-distinct, irc-3yo-not-anticorrelated, irc-3yo-homologous, irc-3yo-nonbilateral\n\nThe 17 children of the 3yo group.\n''')\ncode(r'''\ny3 = children[children.AgeGroup == \"3yo\"].index\nrows = []\nfor r in READINGS:\n    t = IRC[r][0].loc[y3]\n    t1 = stats.ttest_rel(t.wToM, t.across); t2 = stats.ttest_rel(t.wPain, t.across)\n    rows.append({\"reading\": reading_name(r), \"wToM\": t.wToM.mean(), \"sem ToM\": t.wToM.sem(), \"wPain\": t.wPain.mean(),\n                 \"sem Pain\": t.wPain.sem(), \"t ToM-across\": t1.statistic, \"p1\": t1.pvalue, \"t Pain-across\": t2.statistic, \"p2\": t2.pvalue,\n                 \"in tolerance (of 4)\": sum([tol(t.wToM.mean(), .21, .02), tol(t.wPain.mean(), .23, .02),\n                                            tol(t1.statistic, 6.2, .62), tol(t2.statistic, 6.9, .69)])})\nprint(pd.DataFrame(rows).to_string(float_format=lambda x: f\"{x:.3g}\"))\nprint(\"expected wToM .21, wPain .23 (tolerance .02), t 6.2 and 6.9 (10%), n = 17\")\n''', tags=[\"claim:irc-3yo-distinct\"])\nmd('**Result: TBD**')\ncode(r'''\nrows = []\nfor r in READINGS:\n    a = IRC[r][0].loc[y3, \"across\"]\n    tt = stats.ttest_1samp(a, 0)\n    rows.append({\"reading\": reading_name(r), \"mean across\": a.mean(), \"sem\": a.sem(), \"t vs 0 (variant)\": tt.statistic, \"p\": tt.pvalue})\nprint(pd.DataFrame(rows).to_string(float_format=lambda x: f\"{x:.3g}\"))\nprint(\"expected .05 (tolerance .02); adults (main reading)\", round(IRC[MAIN][0].loc[adults.index, \"across\"].mean(), 3))\n''', tags=[\"claim:irc-3yo-not-anticorrelated\"])\nmd('**Result: TBD**')\ncode(r'''\nfor r in [MAIN, (\"with_data\", False, True)]:\n    M = pd.DataFrame(np.mean([IRC[r][1][s].values for s in y3], axis=0), index=TP, columns=TP)\n    print(reading_name(r))\n    for net, rois in [(\"ToM\", sb.TOM_ROIS), (\"Pain\", sb.PAIN_ROIS)]:\n        pairs = sorted([(M.loc[a, b], a, b) for i, a in enumerate(rois) for b in rois[i + 1:]], reverse=True)\n        print(f\"  {net} pairs by 3yo mean z:\", \", \".join(f\"{a}-{b} {v:.3f}\" for v, a, b in pairs[:6]))\nM = pd.DataFrame(np.mean([IRC[MAIN][1][s].values for s in y3], axis=0), index=TP, columns=TP)\nfig, ax = plt.subplots(figsize=(5, 4.5))\nim = ax.imshow(M.values, vmin=-0.6, vmax=0.6, cmap=\"RdBu_r\"); ax.set_xticks(range(13), TP, rotation=90); ax.set_yticks(range(13), TP)\nplt.colorbar(im, label=\"mean Fisher z, 3yo\"); plt.tight_layout(); plt.show()\nprint(\"matrix range (off-diagonal):\", round(np.nanmin(M.values), 3), \"to\", round(np.nanmax(M.values), 3), \"; colour scale -0.6 to 0.6\")\n''', tags=[\"claim:irc-3yo-homologous\"])\nmd('**Result: TBD**')\ncode(r'''\nrows = []\nfor r in READINGS:\n    t = IRC[r][0].loc[y3]\n    for k in [\"a\", \"b\"]:\n        t1 = stats.ttest_rel(t[f\"wToM_nonbi_{k}\"], t.across); t2 = stats.ttest_rel(t[f\"wPain_nonbi_{k}\"], t.across)\n        rows.append({\"reading\": reading_name(r), \"pairs dropped\": k, \"ToM\": t[f\"wToM_nonbi_{k}\"].mean(), \"Pain\": t[f\"wPain_nonbi_{k}\"].mean(),\n                     \"t ToM\": t1.statistic, \"p ToM\": t1.pvalue, \"t Pain\": t2.statistic, \"p Pain\": t2.pvalue,\n                     \"in tolerance (of 4)\": sum([tol(t[f\"wToM_nonbi_{k}\"].mean(), .20, .02), tol(t[f\"wPain_nonbi_{k}\"].mean(), .17, .02),\n                                                tol(t1.statistic, 5.1, .51), tol(t2.statistic, 4.4, .44)])})\nprint(pd.DataFrame(rows).to_string(float_format=lambda x: f\"{x:.3g}\"))\nprint(\"expected ToM .20, Pain .17 (tolerance .02); t 5.1 (p = .0001), 4.4 (p = .0005)\")\n''', tags=[\"claim:irc-3yo-nonbilateral\"])\nmd('**Result: TBD**')\n\nmd(r'''\n### irc-tom-behavior and irc-tom-behavior-age\n''')\ncode(r'''\nrows = []\nfor r in READINGS:\n    c = IRC[r][0].loc[children.index]\n    a = sb.partial_kendall(c.wToM, c[TOM], c.n_art); b = sb.partial_kendall(c.across, c[TOM], c.n_art)\n    rows.append({\"reading\": reading_name(r), \"tau wToM\": a[0], \"p wToM\": a[1], \"tau across\": b[0], \"p across\": b[1]})\nprint(pd.DataFrame(rows).to_string(float_format=lambda x: f\"{x:.3g}\"))\nprint(\"expected wToM .23 (p = .0002), across -.20 (p = .001), tolerance 10%\")\n''', tags=[\"claim:irc-tom-behavior\"])\nmd('**Result: TBD**')\ncode(r'''\nrows = []\nfor r in READINGS:\n    c = IRC[r][0].loc[children.index]\n    for v in [\"wToM\", \"across\"]:\n        f = sb.ols(c, v, [TOM, \"Age\", \"n_art\"]); fz = sb.ols(c, v, [TOM, \"Age\", \"n_art\"], zscore=True)\n        rows.append({\"reading\": reading_name(r), \"measure\": v, \"b ToM raw\": f.params[TOM], \"b ToM z\": fz.params[TOM],\n                     \"t ToM\": f.tvalues[TOM], \"p ToM\": f.pvalues[TOM], \"t age\": f.tvalues[\"Age\"], \"p age\": f.pvalues[\"Age\"]})\nprint(pd.DataFrame(rows).to_string(float_format=lambda x: f\"{x:.3g}\"))\nprint(\"paper: ToM score ts < 1, ps > .3\")\n''', tags=[\"claim:irc-tom-behavior-age\"])\nmd('**Result: TBD**')\n\nmd(r'''\n### irc-fb-within, irc-fb-within-dccs, irc-fb-across\n\nPassers (30) against failers (15), fail coded 1, with age and motion (and DCCS).\n''')\ncode(r'''\npf_idx = young[young.FB_Group.isin([\"pass\", \"fail\"])].index\nrows = []\nfor r in READINGS:\n    t = IRC[r][0].loc[pf_idx].copy(); t[\"fail\"] = (t.FB_Group == \"fail\").astype(float)\n    for v in [\"wToM\", \"across\"]:\n        f = sb.ols(t, v, [\"fail\", \"Age\", \"n_art\"]); fz = sb.ols(t, v, [\"fail\", \"Age\", \"n_art\"], zscore=True)\n        g = sb.ols(t, v, [\"fail\", \"Age\", \"n_art\", DCCS])\n        rows.append({\"reading\": reading_name(r), \"measure\": v, \"mean pass\": t.loc[t.fail == 0, v].mean(), \"mean fail\": t.loc[t.fail == 1, v].mean(),\n                     \"b raw\": f.params[\"fail\"], \"b z\": fz.params[\"fail\"], \"t\": f.tvalues[\"fail\"], \"p\": f.pvalues[\"fail\"],\n                     \"t with DCCS\": g.tvalues[\"fail\"], \"p with DCCS\": g.pvalues[\"fail\"], \"t DCCS\": g.tvalues[DCCS], \"p DCCS\": g.pvalues[DCCS]})\nfbirc = pd.DataFrame(rows)\nprint(fbirc.to_string(float_format=lambda x: f\"{x:.3g}\"))\nprint(\"paper: wToM pass .29, fail .25, b = -.70, t = -2.06, p = .046 (pass higher); with DCCS t = -1.80, p = .079; across .04 against .03, t = 1.2, p = .23\")\n''', tags=[\"claim:irc-fb-within\", \"claim:irc-fb-within-dccs\", \"claim:irc-fb-across\"])\nmd('**Result: TBD**')\n\nmd(r'''\n## Reverse correlation\n\nNetwork timecourses (P6) from ROI timecourses cleaned without the M1 regressor. O6: z over\nTRs 11 to 168 (a) or all 168 (b). O5: p < .05 (a), p < .01 (b), FDR p < .05 over the 158\ntimepoints (c). O1 is fixed at the main reading (z-normalization makes O1's voxel choice\nirrelevant up to the few partial voxels; shown in the IRC section).\n''')\ncode(r'''\ndef network_tcs(net, z=True, z_span=\"movie\", voxels=\"all\"):\n    rois = sb.FFA_ROIS if net == \"FFA\" else sb.NETWORKS[net]\n    out = {}\n    for s in subs:\n        tc = sb.subject_timecourses(D[s], rois, voxels, False)\n        out[s] = sb.network_timecourse(tc, rois, z_span, z)\n    return pd.DataFrame(out).T\n\nNETS = [\"ToM\", \"Pain\", \"Face\", \"Scene\", \"M1\", \"V1\", \"FFA\"]\nNZ = {(n, span): network_tcs(n, True, span) for n in [\"ToM\", \"Pain\", \"FFA\"] for span in [\"movie\", \"all\"]}\nRAW = {n: network_tcs(n, False) for n in NETS}\nO5 = {\"a p<.05\": (0.05, False), \"b p<.01\": (0.01, False), \"c FDR<.05\": (0.05, True)}\nRC = {}\nfor span in [\"movie\", \"all\"]:\n    for k, (alpha, fdr) in O5.items():\n        for n in [\"ToM\", \"Pain\", \"FFA\"]:\n            tab, ev = sb.reverse_correlation(NZ[(n, span)].loc[adults.index].values, alpha, fdr)\n            RC[(n, span, k)] = (tab, ev, sb.rank_events(ev, tab))\nrows = []\nfor (n, span, k), (tab, ev, rk) in RC.items():\n    if n == \"FFA\":\n        continue\n    m = sb.match_table_events(ev, n)\n    rows.append({\"network\": n, \"O6 z span\": span, \"O5\": k, \"events\": len(ev), \"seconds\": 2 * sum(len(e) for e in ev),\n                 \"table events found\": int(m.sum()), \"of\": len(m), \"missed\": \",\".join(m.index[~m])})\nrcsum = pd.DataFrame(rows)\nprint(rcsum.to_string())\n''')\n\nmd(r'''\n### rc-events\n\n> Reverse correlation on the adult network timecourses finds seven ToM events (68 s, mean length\n> 9.7 s) and twelve pain events (86 s, mean length 7.2 s), at the times of Supplementary Table 3.\n''')\ncode(r'''\nfor (n, span, k), (tab, ev, rk) in RC.items():\n    if n != \"FFA\" and span == \"movie\":\n        print(n, k, \"events (onset TR, TRs, peak TR):\", [(int(a), int(b), int(c)) for a, b, c in zip(rk.onset, rk.length_tr, rk.peak_tr)])\n        print(\"   mean length %.1f s (s.d. %.1f)\" % (2 * rk.length_tr.mean(), 2 * rk.length_tr.std()) if len(rk) else \"\")\nprint(sb.SUPP_TABLE3[[\"event\", \"time\", \"duration_s\", \"peak_tr\", \"onset_tr\"]].to_string(index=False))\nscore = rcsum.groupby([\"O6 z span\", \"O5\"]).apply(lambda g: pd.Series({\n    \"table events found\": g[\"table events found\"].sum(), \"count error\": (g.events - g[\"of\"]).abs().sum(),\n    \"ToM events\": int(g.loc[g.network == \"ToM\", \"events\"].iloc[0]), \"Pain events\": int(g.loc[g.network == \"Pain\", \"events\"].iloc[0]),\n    \"ToM s\": int(g.loc[g.network == \"ToM\", \"seconds\"].iloc[0]), \"Pain s\": int(g.loc[g.network == \"Pain\", \"seconds\"].iloc[0])}), include_groups=False)\nprint(score.to_string())\nbest = score.sort_values([\"table events found\", \"count error\"], ascending=[False, True]).index[0]\nBEST_SPAN, BEST_O5 = best\nprint(\"best-matching reading (most table events found, then smallest count error):\", best)\n''', tags=[\"claim:rc-events\"])\n\ncode(r'''\nfig, axes = plt.subplots(2, 1, figsize=(12, 5), sharex=True)\nfor ax, n, col in zip(axes, [\"ToM\", \"Pain\"], [\"tab:red\", \"tab:green\"]):\n    tab, ev, rk = RC[(n, BEST_SPAN, BEST_O5)]\n    ax.plot(tab.TR, tab[\"mean\"], color=col)\n    for e in ev:\n        ax.axvspan(e[0] - 0.5, e[-1] + 0.5, color=col, alpha=0.2)\n    for _, row in sb.SUPP_TABLE3[sb.SUPP_TABLE3.network == n].iterrows():\n        ax.axvspan(row.trs[0] - 0.5, row.trs[-1] + 0.5, fill=False, edgecolor=\"k\", lw=0.8)\n    ax.set_ylabel(f\"adult mean, {n} (z)\"); ax.axhline(0, color=\"grey\", lw=0.5)\naxes[1].set_xlabel(\"TR (shaded: found events; outlined: Supplementary Table 3)\")\nplt.tight_layout(); plt.show()\nprint(\"y ranges:\", {n: (round(RC[(n, BEST_SPAN, BEST_O5)][0][\"mean\"].min(), 2), round(RC[(n, BEST_SPAN, BEST_O5)][0][\"mean\"].max(), 2)) for n in [\"ToM\", \"Pain\"]})\n''', tags=[\"claim:rc-events\"])\nmd('**Result: TBD**')\n\nmd(r'''\n### rc-overlap\n\n> ToM and pain events overlap at a single timepoint (the last of T05 and first of P05), less\n> overlap than chance in a permutation test.\n\nPermutations as Methods paragraph 10, 1000 per reading, seed fixed for this section.\n''')\ncode(r'''\nrng = np.random.default_rng(20180301)\ndef overlap_test(ev_a, ev_b, zeros_a, zeros_b, n_perm=1000):\n    obs = len(set(t for e in ev_a for t in e) & set(t for e in ev_b for t in e))\n    perm = sb.overlap_permutation([len(e) for e in ev_a], [len(e) for e in ev_b], zeros_a, zeros_b, n_perm, rng)\n    return obs, (perm <= obs).sum(), perm.mean()\nrows = []\nevsets = {\"found (\" + BEST_SPAN + \", \" + BEST_O5 + \")\": (RC[(\"ToM\", BEST_SPAN, BEST_O5)][1], RC[(\"Pain\", BEST_SPAN, BEST_O5)][1])}\nfor k in O5:\n    evsets[f\"found (movie, {k})\"] = (RC[(\"ToM\", \"movie\", k)][1], RC[(\"Pain\", \"movie\", k)][1])\nevsets[\"Supplementary Table 3 events (variant)\"] = (list(sb.SUPP_TABLE3[sb.SUPP_TABLE3.network == \"ToM\"].trs), list(sb.SUPP_TABLE3[sb.SUPP_TABLE3.network == \"Pain\"].trs))\nfor name, (et, ep) in evsets.items():\n    nt, np_ = sum(map(len, et)), sum(map(len, ep))\n    for reading, (za, zb) in {\"(a) 158 TRs\": (158 - nt, 158 - np_), \"(b) paper's zeros 125, 116\": (125, 116)}.items():\n        obs, k, mean = overlap_test(et, ep, za, zb)\n        rows.append({\"events\": name, \"reading\": reading, \"observed overlap TRs\": obs, \"perms <= observed\": k, \"p\": k / 1000, \"mean perm overlap\": mean})\novl = pd.DataFrame(rows)\nprint(ovl.to_string())\nboth = set(t for e in RC[(\"ToM\", BEST_SPAN, BEST_O5)][1] for t in e) & set(t for e in RC[(\"Pain\", BEST_SPAN, BEST_O5)][1] for t in e)\nprint(\"overlapping TRs of found events:\", sorted(both))\n''', tags=[\"claim:rc-overlap\"])\nmd('**Result: TBD**')\n\nmd(r'''\n### rc-child-adult-timecourse and supp-table4-other-networks\n\nNetwork timecourses before z-normalization, averaged over the participants of each age group\n(artifact timepoints left out), correlated with the adult average over TRs 11 to 168.\n''')\ncode(r'''\nMOVIE = np.arange(sb.FIRST_MOVIE_TR - 1, sb.N_TR)\ndef group_r(net, idx):\n    a = np.nanmean(RAW[net].loc[adults.index].values, axis=0)[MOVIE]\n    c = np.nanmean(RAW[net].loc[idx].values, axis=0)[MOVIE]\n    res = stats.pearsonr(a, c)\n    return res.statistic, res.pvalue\nrows = []\nfor net in NETS:\n    for g in sb.AGE_GROUPS:\n        r, pv = group_r(net, children[children.AgeGroup == g].index)\n        rows.append({\"network\": net, \"group\": g, \"r\": r, \"p\": pv})\n    r, pv = group_r(net, children.index)\n    rows.append({\"network\": net, \"group\": \"all children\", \"r\": r, \"p\": pv})\ngr = pd.DataFrame(rows)\nprint(gr.pivot(index=\"network\", columns=\"group\", values=\"r\").round(3).to_string())\nprint(gr.pivot(index=\"network\", columns=\"group\", values=\"p\").map(lambda x: f\"{x:.1e}\").to_string())\n''')\ncode(r'''\nEXP_TP = {\"ToM\": [.28, .31, .60, .72, .82], \"Pain\": [.60, .56, .73, .83, .89]}\nfor net, e in EXP_TP.items():\n    g = gr[(gr.network == net) & gr.group.isin(sb.AGE_GROUPS)].copy(); g[\"expected\"] = e\n    g[\"in tolerance\"] = [tol(a, b, .1 * b) for a, b in zip(g.r, g.expected)]\n    g[\"p < .0005\"] = g.p < .0005\n    print(g.to_string(index=False, float_format=lambda x: f\"{x:.3g}\"))\n''', tags=[\"claim:rc-child-adult-timecourse\"])\nmd('**Result: TBD**')\ncode(r'''\nEXP_S4 = {\"Face\": [.75, .59, .71, .84, .86], \"Scene\": [.61, .67, .77, .80, .85], \"M1\": [.11, .06, .35, .44, .53],\n          \"V1\": [.53, .61, .78, .74, .76], \"FFA\": [.72, .60, .68, .82, .83]}\nrows = []\nfor net, e in EXP_S4.items():\n    g = gr[(gr.network == net) & gr.group.isin(sb.AGE_GROUPS)]\n    for (_, x), ex in zip(g.iterrows(), e):\n        rows.append({\"network\": net, \"group\": x.group, \"r\": x.r, \"expected\": ex, \"in tolerance\": tol(x.r, ex, .1 * ex),\n                     \"p\": x.p, \"significant (p < .0005)\": x.p < .0005})\ns4 = pd.DataFrame(rows)\nprint(s4.to_string(index=False, float_format=lambda x: f\"{x:.3g}\"))\nprint(\"in tolerance:\", int(s4[\"in tolerance\"].sum()), \"of 25; not significant:\", list(s4.loc[~s4[\"significant (p < .0005)\"], [\"network\", \"group\"]].itertuples(index=False, name=None)))\n''', tags=[\"claim:supp-table4-other-networks\"])\nmd('**Result: TBD**')\n\nmd(r'''\n### rc-age-events, rc-t04-tom, rc-fb-no-difference\n\nResponse magnitude at the peak TR of each Supplementary Table 3 event, ToM events from the ToM\nnetwork and pain events from the Pain network. O7a: z-normalized timecourse (O6 a or b); O7b:\nbefore z-normalization. Children whose peak TR is an artifact timepoint (NaN) are left out of\nthat event's test; their number is printed.\n''')\ncode(r'''\nMAG = {}\nfor name, src in {\"O7a z movie\": lambda n: NZ[(n, \"movie\")], \"O7a z all\": lambda n: NZ[(n, \"all\")], \"O7b raw\": lambda n: RAW[n]}.items():\n    MAG[name] = pd.DataFrame({row.event: src(row.network)[row.peak_tr - 1] for _, row in sb.SUPP_TABLE3.iterrows()})\nrows = []\nfor name, mag in MAG.items():\n    for ev in mag.columns:\n        c = children.join(mag[[ev]]).dropna(subset=[ev])\n        rr, pv, _ = sb.partial_spearman(c[ev], c.Age, c.n_art)\n        rows.append({\"reading\": name, \"event\": ev, \"n\": len(c), \"rs\": rr, \"p\": pv, \"passes p < .0026\": pv < .0026 and rr > 0})\nage_ev = pd.DataFrame(rows)\nprint(age_ev.pivot(index=\"event\", columns=\"reading\", values=\"rs\").round(3).join(\n      age_ev.pivot(index=\"event\", columns=\"reading\", values=\"p\").map(lambda x: f\"{x:.1e}\"), rsuffix=\" p\").to_string())\nprint(\"children left out (artifact at peak):\", age_ev.groupby(\"event\").n.first().rsub(len(children)).to_dict())\nfor name in MAG:\n    passed = list(age_ev[(age_ev.reading == name) & age_ev[\"passes p < .0026\"]].event)\n    print(name, \"events passing:\", passed, \"; with rs > .28:\", list(age_ev[(age_ev.reading == name) & age_ev[\"passes p < .0026\"] & (age_ev.rs > .28)].event))\nprint(\"paper: P01, P04, P08, T01, T02\")\n''', tags=[\"claim:rc-age-events\"])\nmd('**Result: TBD**')\ncode(r'''\nrows = []\nfor name, mag in MAG.items():\n    for ev in [e for e in mag.columns if e.startswith(\"T\")]:\n        c = children.join(mag[[ev]]).dropna(subset=[ev])\n        f = sb.ols(c, ev, [TOM, \"Age\", \"n_art\"]); fz = sb.ols(c, ev, [TOM, \"Age\", \"n_art\"], zscore=True)\n        rows.append({\"reading\": name, \"event\": ev, \"n\": int(f.nobs), \"b raw\": f.params[TOM], \"b z\": fz.params[TOM], \"t\": f.tvalues[TOM], \"p\": f.pvalues[TOM], \"p < .007\": f.pvalues[TOM] < .007})\nt04 = pd.DataFrame(rows)\nprint(t04.to_string(index=False, float_format=lambda x: f\"{x:.3g}\"))\nprint(\"paper T04: b = .4, t = 2.98, p = .0035; only T04 marked\")\n''', tags=[\"claim:rc-t04-tom\"])\nmd('**Result: TBD**')\ncode(r'''\nrng_fb = np.random.default_rng(1027)\nrows = []\nfor name, mag in MAG.items():\n    for ev in [e for e in mag.columns if e.startswith(\"T\")]:\n        c = young.loc[pf_idx].join(mag[[ev]]).dropna(subset=[ev]).copy(); c[\"fail\"] = (c.FB_Group == \"fail\").astype(float)\n        f = sb.ols(c, ev, [\"fail\", \"Age\", \"n_art\"])\n        row = {\"reading\": name, \"event\": ev, \"n\": int(f.nobs), \"mean pass\": c.loc[c.fail == 0, ev].mean(), \"mean fail\": c.loc[c.fail == 1, ev].mean(),\n               \"t\": f.tvalues[\"fail\"], \"p\": f.pvalues[\"fail\"]}\n        if ev == \"T03\":\n            t_obs = f.tvalues[\"fail\"]; perm = []\n            for _ in range(5000):\n                cc = c.copy(); cc[\"fail\"] = rng_fb.permutation(cc.fail.values)\n                perm.append(sb.ols(cc, ev, [\"fail\", \"Age\", \"n_art\"]).tvalues[\"fail\"])\n            row[\"p permutation (T03)\"] = float(np.mean(np.abs(perm) >= abs(t_obs)))\n        rows.append(row)\nfbev = pd.DataFrame(rows)\nprint(fbev.to_string(index=False, float_format=lambda x: f\"{x:.3g}\"))\nprint(\"smallest p per reading:\", fbev.groupby(\"reading\").p.min().round(4).to_dict(), \"(paper: all p > .08)\")\n''', tags=[\"claim:rc-fb-no-difference\"])\nmd('**Result: TBD**')\n\nmd(r'''\n### rc-3yo-events\n\n> Reverse correlation on the 3-year-olds alone finds 4 of the 12 adult pain events and 1 of the 7\n> adult ToM events; of its 32 s of pain events 14 s fall in adult pain events and 8 s in adult ToM\n> event T04, and of its 8 s of ToM events 4 s fall in an adult ToM event and 4 s in adult pain\n> event P01.\n\nAdult events are those of Supplementary Table 3 (Figure 4a); the events found here in adults\nare shown as a variant.\n''')\ncode(r'''\ndef tr_set(evs):\n    return set(t for e in evs for t in e)\nTAB = {n: dict(zip(sb.SUPP_TABLE3[sb.SUPP_TABLE3.network == n].event, sb.SUPP_TABLE3[sb.SUPP_TABLE3.network == n].trs)) for n in [\"ToM\", \"Pain\"]}\nrows = []\nfor span in [\"movie\", \"all\"]:\n    for k, (alpha, fdr) in O5.items():\n        e3 = {n: sb.reverse_correlation(NZ[(n, span)].loc[y3].values, alpha, fdr)[1] for n in [\"ToM\", \"Pain\"]}\n        row = {\"O6\": span, \"O5\": k}\n        for n, other in [(\"Pain\", \"ToM\"), (\"ToM\", \"Pain\")]:\n            s3 = tr_set(e3[n])\n            row[f\"3yo {n} events\"] = len(e3[n]); row[f\"3yo {n} s\"] = 2 * len(s3)\n            row[f\"adult {n} events found\"] = sum(bool(s3 & set(v)) for v in TAB[n].values())\n            row[f\"{n} s in adult {n} events\"] = 2 * len(s3 & tr_set(TAB[n].values()))\n            row[f\"{n} s in adult {other} events\"] = 2 * len(s3 & tr_set(TAB[other].values()))\n        row[\"Pain s in T04\"] = 2 * len(tr_set(e3[\"Pain\"]) & set(TAB[\"ToM\"][\"T04\"]))\n        row[\"ToM s in P01\"] = 2 * len(tr_set(e3[\"ToM\"]) & set(TAB[\"Pain\"][\"P01\"]))\n        row[\"3yo events (TR lists)\"] = {n: [(e[0], len(e)) for e in e3[n]] for n in e3}\n        row[\"vs found adult events: Pain s\"] = 2 * len(tr_set(e3[\"Pain\"]) & tr_set(RC[(\"Pain\", span, k)][1]))\n        row[\"vs found adult events: ToM s\"] = 2 * len(tr_set(e3[\"ToM\"]) & tr_set(RC[(\"ToM\", span, k)][1]))\n        rows.append(row)\nr3 = pd.DataFrame(rows)\nprint(r3.drop(columns=\"3yo events (TR lists)\").T.to_string())\nfor _, x in r3.iterrows():\n    print(x.O6, x.O5, x[\"3yo events (TR lists)\"])\nprint(\"paper: 3yo pain 32 s, 4 of 12 adult pain events, 14 s in adult pain events, 8 s in T04; 3yo ToM 8 s, 1 of 7 adult ToM events, 4 s in a ToM event, 4 s in P01\")\nprint(\"reading of rc-events used by the criterion:\", BEST_SPAN, BEST_O5)\n''', tags=[\"claim:rc-3yo-events\"])\nmd('**Result: TBD**')\n\nmd(r'''\n## Functional maturity\n\nEach child's ToM (Pain) network timecourse before z-normalization, TRs 11 to 168, artifact\ntimepoints left out, correlated (Pearson) with the adult mean timecourse (Methods paragraph 13).\nIRC measures are those of irc-age-within (M1 regressed), under each IRC reading.\n''')\ncode(r'''\ndef maturity(net):\n    adult_mean = np.nanmean(RAW[net].loc[adults.index].values, axis=0)[MOVIE]\n    out = {}\n    for s in children.index:\n        x = RAW[net].loc[s].values[MOVIE]; ok = np.isfinite(x)\n        out[s] = stats.pearsonr(x[ok], adult_mean[ok]).statistic\n    return pd.Series(out)\nMAT = pd.DataFrame({\"mat_ToM\": maturity(\"ToM\"), \"mat_Pain\": maturity(\"Pain\")})\nprint(MAT.describe().round(3).to_string())\n''')\ncode(r'''\nrows = []\nfor r in READINGS:\n    c = IRC[r][0].loc[children.index].join(MAT)\n    for net, wv in [(\"ToM\", \"wToM\"), (\"Pain\", \"wPain\")]:\n        f = sb.ols(c, f\"mat_{net}\", [\"across\", wv, \"Age\", \"n_art\"]); fz = sb.ols(c, f\"mat_{net}\", [\"across\", wv, \"Age\", \"n_art\"], zscore=True)\n        rows.append({\"reading\": reading_name(r), \"network\": net, \"b across raw\": f.params[\"across\"], \"b across z\": fz.params[\"across\"],\n                     \"t across\": f.tvalues[\"across\"], \"p across\": f.pvalues[\"across\"], \"b within z\": fz.params[wv], \"t within\": f.tvalues[wv], \"p within\": f.pvalues[wv]})\nprint(pd.DataFrame(rows).to_string(float_format=lambda x: f\"{x:.3g}\"))\nprint(\"paper: ToM across b = -.4, t = -5.5, within t = 1.5 (p = .14); Pain across b = -.51, t = -7.4, within t = 1.9 (p = .06)\")\n''', tags=[\"claim:maturity-across\"])\nmd('**Result: TBD**')\ncode(r'''\nrows = []\nfor r in READINGS:\n    c = IRC[r][0].loc[children.index].join(MAT)\n    for net, wv in [(\"ToM\", \"wToM\"), (\"Pain\", \"wPain\")]:\n        f = sb.ols(c, wv, [f\"mat_{net}\", \"Age\", \"n_art\"]); fz = sb.ols(c, wv, [f\"mat_{net}\", \"Age\", \"n_art\"], zscore=True)\n        rows.append({\"reading\": reading_name(r), \"measure\": wv, \"b maturity z\": fz.params[f\"mat_{net}\"], \"t maturity\": f.tvalues[f\"mat_{net}\"],\n                     \"p maturity\": f.pvalues[f\"mat_{net}\"], \"b age z\": fz.params[\"Age\"], \"t age\": f.tvalues[\"Age\"], \"p age\": f.pvalues[\"Age\"]})\nprint(pd.DataFrame(rows).to_string(float_format=lambda x: f\"{x:.3g}\"))\nprint(\"paper: maturity t = .48 (ToM), .61 (Pain), n.s.; age t = 2.5 (p = .01), 1.96 (p = .05)\")\n''', tags=[\"claim:maturity-within\"])\nmd('**Result: TBD**')\ncode(r'''\nc = children.join(MAT)\nrr, pv, df = sb.partial_spearman(c.mat_ToM, c[TOM], c.n_art)\nprint(f\"partial Spearman(ToM maturity, ToM score | motion) = {rr:.3f}, p = {pv:.2g}, df = {df} (paper .54, p = 1.3e-10)\")\nf = sb.ols(c, \"mat_ToM\", [\"Age\", TOM, \"n_art\"]); fz = sb.ols(c, \"mat_ToM\", [\"Age\", TOM, \"n_art\"], zscore=True)\nprint(f\"regression: ToM score b z = {fz.params[TOM]:.2f}, t = {f.tvalues[TOM]:.2f}, p = {f.pvalues[TOM]:.3f}; age b z = {fz.params['Age']:.2f}, t = {f.tvalues['Age']:.2f}, p = {f.pvalues['Age']:.2g}\")\nprint(\"paper: ToM score b = .1, t = 1.2, p = .3; age b = .5, t = 4.2, p < .00005\")\n''', tags=[\"claim:maturity-tom-behavior\"])\nmd('**Result: TBD**')\ncode(r'''\nc = young.loc[pf_idx].join(MAT).copy(); c[\"fail\"] = (c.FB_Group == \"fail\").astype(float)\nf = sb.ols(c, \"mat_ToM\", [\"fail\", \"Age\", \"n_art\"]); fz = sb.ols(c, \"mat_ToM\", [\"fail\", \"Age\", \"n_art\"], zscore=True)\nprint(c.groupby(\"FB_Group\").mat_ToM.agg([\"mean\", \"sem\", \"count\"]).round(3).to_string())\nprint(f\"FB group (fail = 1): b raw = {f.params['fail']:.3f}, b z = {fz.params['fail']:.2f}, t = {f.tvalues['fail']:.2f}, p = {f.pvalues['fail']:.2f} (paper b = -.12, t = -.35, p = .73)\")\n''', tags=[\"claim:maturity-fb\"])\nmd('**Result: TBD**')\n\nmd(r'''\n## Face regions\n\n### face-rc and face-overlap\n\nBilateral fusiform ROIs (deposited rFFA, 1019 voxels, and lFFA, 531 voxels).\n''')\ncode(r'''\nr_all = group_r(\"FFA\", children.index); r_3 = group_r(\"FFA\", y3)\nprint(f\"children (n = {len(children)}) against adults: r = {r_all[0]:.3f}, p = {r_all[1]:.1e} (paper .86, p < 1e-47)\")\nprint(f\"3yo (n = {len(y3)}) against adults: r = {r_3[0]:.3f}, p = {r_3[1]:.1e} (paper .72, p < 1e-26)\")\nrows = []\nfor span in [\"movie\", \"all\"]:\n    for k, (alpha, fdr) in O5.items():\n        tab, ev, rk = RC[(\"FFA\", span, k)]\n        e3 = sb.reverse_correlation(NZ[(\"FFA\", span)].loc[y3].values, alpha, fdr)[1]\n        rows.append({\"O6\": span, \"O5\": k, \"adult events\": len(ev), \"adult s\": 2 * sum(map(len, ev)), \"adult lengths (TRs)\": [len(e) for e in rk.trs],\n                     \"3yo events\": len(e3), \"3yo s\": 2 * sum(map(len, e3)), \"3yo TRs in adult events\": len(tr_set(e3) & tr_set(ev)), \"3yo TR count\": len(tr_set(e3))})\nface = pd.DataFrame(rows)\nprint(face.to_string())\nprint(\"paper: adults 7 events, 88 s, lengths 16, 4, 5, 7, 4, 4, 4 TRs; 3yo 4 events, 18 s, 8 of 9 TRs in adult events\")\ntab, ev, rk = RC[(\"FFA\", BEST_SPAN, BEST_O5)]\nrows = []\nfor name, src in {\"O7a z\": NZ[(\"FFA\", BEST_SPAN)], \"O7b raw\": RAW[\"FFA\"]}.items():\n    for i, row in rk.iterrows():\n        c = children.join(src[row.peak_tr - 1].rename(\"mag\")).dropna(subset=[\"mag\"])\n        rr, pv, _ = sb.partial_spearman(c.mag, c.Age, c.n_art)\n        rows.append({\"reading\": name, \"event\": f\"F{i + 1:02d}\", \"peak TR\": row.peak_tr, \"n\": len(c), \"rs\": rr, \"p\": pv,\n                     \"p < .0071\": pv < .0071, f\"p < .05/{len(rk)}\": pv < .05 / len(rk)})\nprint(f\"face-event magnitudes against age (events of the {BEST_SPAN}, {BEST_O5} reading):\")\nprint(pd.DataFrame(rows).to_string(index=False, float_format=lambda x: f\"{x:.3g}\"))\nprint(\"paper: |rs| < .24, ps > .01, none significant at .0071\")\n''', tags=[\"claim:face-rc\"])\nmd('**Result: TBD**')\ncode(r'''\nrng_face = np.random.default_rng(88)\nrows = []\nfor span, k in [(BEST_SPAN, BEST_O5)] + [(\"movie\", k) for k in O5 if k != BEST_O5 or BEST_SPAN != \"movie\"]:\n    ef = RC[(\"FFA\", span, k)][1]\n    for other in [\"ToM\", \"Pain\"]:\n        eo = RC[(other, span, k)][1]\n        nf, no = sum(map(len, ef)), sum(map(len, eo))\n        obs = len(tr_set(ef) & tr_set(eo))\n        perm = sb.overlap_permutation([len(e) for e in ef], [len(e) for e in eo], 158 - nf, 158 - no, 1000, rng_face)\n        rows.append({\"reading\": f\"{span}, {k}\", \"face vs\": other, \"observed overlap TRs\": obs, \"perms <= observed\": int((perm <= obs).sum()),\n                     \"p (fewer than chance)\": float((perm <= obs).mean()), \"mean perm overlap\": perm.mean()})\nprint(pd.DataFrame(rows).to_string(index=False, float_format=lambda x: f\"{x:.3g}\"))\nprint(\"paper: face-ToM 4 TRs, p = .11; face-pain 15 TRs, p = .93\")\n''', tags=[\"claim:face-overlap\"])\nmd('**Result: TBD**')\n\nmd(r'''\n## Blocked claims\n\n- replication-sample: the independent sample of 20 adults (Fedorenko and colleagues) is not in\n  the snapshot, and the paper names no archive for it.\n- hand-coded-events: the \"mental\", \"social\" and \"pain\" coding of Jacoby et al. (2016) is not in\n  the snapshot; the README lists only the reverse-correlation events, and the paper does not\n  give the coded times.\n\n## Summary\n\nTBD\n''')\n"
}
```

```
File created successfully at: /tmp/claude-1001/cells.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018 && python3 - <<'EOF'
import re
s=open("social_brain.py").read()
old=s[s.index("def irc_matrix"):s.index("def within")]
new='''def irc_matrix(tcs: dict, rois, trs=None) -> pd.DataFrame:
    """Fisher z of the Pearson correlation of every ROI pair, over timepoints where all are
    finite (the artifact timepoints are NaN in every ROI) and, if given, within `trs`."""
    X = np.stack([tcs[r] for r in rois])
    ok = np.all(np.isfinite(X), axis=0)
    if trs is not None:
        ok &= np.isin(np.arange(X.shape[1]), trs)
    with np.errstate(divide="ignore"):
        z = np.arctanh(np.corrcoef(X[:, ok]))
    np.fill_diagonal(z, np.nan)
    return pd.DataFrame(z, index=rois, columns=rois)


'''
s=s.replace(old,new)
open("social_brain.py","w").write(s)
EOF
cat > requirements.in <<'EOF'
h5py
matplotlib
nibabel
numpy
pandas
requests
scipy
statsmodels
EOF
source $TMPDIR/dev/bin/activate && uv pip install -q matplotlib nbconvert ipykernel nbformat 2>&1 | tail -1; python $TMPDIR/build_nb.py $TMPDIR/cells.py reproduce_richardson_2018.ipynb && date -u && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output $TMPDIR/dev_exec.ipynb reproduce_richardson_2018.ipynb 2>&1 | tail -5
```

```
Wed Oct 28 16:27:07 UTC 2026
[32m    655[39m raw_length = raw_lengths.pop()
[32m    656[39m [38;5;28;01mif[39;00m have_series:

[31mValueError[39m: Mixing dicts with non-Series may lead to ambiguous ordering.


real	1m51.147s
user	2m14.183s
sys	1m19.630s
```

**Agent calls Bash**

```bash
cat > $TMPDIR/devrun.py <<'EOF'
import nbformat, sys, os, pickle, io, contextlib, traceback, time
import matplotlib; matplotlib.use("Agg")
sys.path.insert(0, os.getcwd())
import social_brain as sb
_D = pickle.load(open(os.environ["TMPDIR"] + "/extract.pkl", "rb"))
nb = nbformat.read(sys.argv[1], as_version=4)
start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
ns = {}
if start:
    ns = pickle.load(open(os.environ["TMPDIR"] + "/ns.pkl", "rb")) if False else {}
for i, c in enumerate(nb.cells):
    if c.cell_type != "code": continue
    src = c.source
    t = time.time()
    print(f"----- cell {i} {c.metadata.get('tags', '')}")
    try:
        exec(compile(src, f"cell{i}", "exec"), ns)
        if "import social_brain as sb" in src:
            ns["sb"].extract_all = lambda subs, n_threads=8: {s: _D[s] for s in subs}
    except Exception:
        traceback.print_exc(); break
    print(f"  [{time.time()-t:.1f}s]")
EOF
cd entries/openneuro-ds000228-richardson-2018 && source $TMPDIR/dev/bin/activate && python $TMPDIR/devrun.py reproduce_richardson_2018.ipynb 2>&1 | grep -v Warning > $TMPDIR/out1.txt; grep -n "cell \|Error\|Traceback" $TMPDIR/out1.txt | tail -20
```

```
1:----- cell 1 
65:----- cell 2 
190:----- cell 3 
413:----- cell 5 
419:----- cell 7 ['sanity']
441:n_art                     155.0    NaN           NaN  NaN   8.870968  10.076145       0.0       1.0       5.0      12.0   48.0Traceback (most recent call last):
453:    raise ValueError(
456:ValueError: Mixing dicts with non-Series may lead to ambiguous ordering.
497:----- cell 8 ['sanity']
547:----- cell 10 ['sanity']
554:----- cell 12 ['claim:participants']
```

**Agent calls Bash**

```bash
sed -n 440,600p $TMPDIR/out1.txt
```

```
Scanlog: Slice Gap        127.0    NaN           NaN  NaN   0.105512   0.022911       0.1       0.1       0.1       0.1    0.2
n_art                     155.0    NaN           NaN  NaN   8.870968  10.076145       0.0       1.0       5.0      12.0   48.0Traceback (most recent call last):
  File "/tmp/claude-1001/devrun.py", line 17, in <module>
    exec(compile(src, f"cell{i}", "exec"), ns)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "cell12", line 6, in <module>
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/frame.py", line 533, in __init__
    mgr = dict_to_mgr(data, index, columns, dtype=dtype, copy=copy)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/internals/construction.py", line 463, in dict_to_mgr
    return arrays_to_mgr(arrays, columns, index, dtype=dtype, consolidate=copy)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/internals/construction.py", line 116, in arrays_to_mgr
    index = _extract_index(arrays)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/internals/construction.py", line 652, in _extract_index
    raise ValueError(
        "Mixing dicts with non-Series may lead to ambiguous ordering."
    )
ValueError: Mixing dicts with non-Series may lead to ambiguous ordering.


children 122 adults 33
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open("cells.py").read()
s=s.replace('''print(pd.DataFrame({"measured": counts, "expected": expected}).to_string())''','''print(pd.DataFrame({"measured": pd.Series(counts), "expected": expected}).to_string())''')
old=s[s.index("def jump_at(s, shift):"):s.index("''', tags=[\"sanity\"])", s.index("def jump_at(s, shift):"))]
new='''def spike_at(s, shift):
    # isolated artifact timepoints only; deviation of the mean ToM+Pain ROI signal from the median
    # of the 7 timepoints around it, in units of that participant's median deviation
    x = np.mean([D[s]["rois"][r]["all"] for r in sb.TOM_ROIS + sb.PAIN_ROIS], axis=0)
    med = pd.Series(x).rolling(7, center=True, min_periods=4).median().values
    dev = np.abs(x - med); dev = dev / np.median(dev)
    a = sb.artifact_index(D[s]["artifacts"])
    iso = [t for t in a if t - 1 not in a and t + 1 not in a and 3 <= t + shift < sb.N_TR - 3]
    return [dev[t + shift] for t in iso]
for shift in [-2, -1, 0, 1, 2, 10]:
    vals = np.concatenate([spike_at(s, shift) for s in subs])
    print(f"isolated artifact timepoints shifted by {shift:3d} TRs: n = {len(vals)}, median deviation = {np.median(vals):.2f}")
'''
s=s.replace(old,new)
s=s.replace("Two checks that the image volumes and the regressors share the\nsame clock: (1) the artifact indicators should fall on the timepoints where the ROI signal jumps,\ncompared with the same indicators shifted in time;","Two checks that the image volumes and the regressors share the\nsame clock: (1) the ROI signal should deviate most at isolated artifact timepoints, compared\nwith the same indicators shifted in time;")
s=s.replace("(2) the adult ToM-network signal should be\nhigher during the paper's ToM events than during its pain events (Supplementary Table 3), and the\ncontrast should drop when the event labels are shifted in time.","(2) the adult ToM-network signal should be\nhigher during the paper's ToM events than during its pain events (Supplementary Table 3), and the\ncontrast should drop when the event labels are shifted in time; this is shown in the reverse\ncorrelation section, after the network timecourses are built.")
open("cells.py","w").write(s)
EOF
grep -n "spike_at\|shown in the reverse" cells.py | head
```

```
155:contrast should drop when the event labels are shifted in time; this is shown in the reverse
160:def spike_at(s, shift):
170:    vals = np.concatenate([spike_at(s, shift) for s in subs])
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open("cells.py").read()
anchor="md(r'''\n### rc-events"
new='''code(r\'\'\'
# Timing check (2): adult network contrast during the paper's ToM against pain events, with the
# event labels shifted in time.
tom_trs = np.array(sorted(tr_set_ := set(t for v in sb.SUPP_TABLE3[sb.SUPP_TABLE3.network == "ToM"].trs for t in v)))
pain_trs = np.array(sorted(set(t for v in sb.SUPP_TABLE3[sb.SUPP_TABLE3.network == "Pain"].trs for t in v)))
for shift in [-10, -4, -2, 0, 2, 4, 10]:
    out = []
    for n in ["ToM", "Pain"]:
        m = np.nanmean(NZ[(n, "movie")].loc[adults.index].values, axis=0)
        tt, pp = np.clip(tom_trs + shift, 11, 168) - 1, np.clip(pain_trs + shift, 11, 168) - 1
        out.append(m[tt].mean() - m[pp].mean())
    print(f"shift {shift:3d} TRs: ToM network, ToM minus pain events = {out[0]:.2f}; Pain network, ToM minus pain events = {out[1]:.2f}")
\'\'\', tags=["sanity"])

'''
s=s.replace(anchor,new+anchor,1)
open("cells.py","w").write(s)
EOF
cd entries/openneuro-ds000228-richardson-2018 && source $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py $TMPDIR/cells.py reproduce_richardson_2018.ipynb && python $TMPDIR/devrun.py reproduce_richardson_2018.ipynb 2>&1 | grep -v Warning > $TMPDIR/out1.txt; grep -n "^----- cell\|Error\|Traceback\|\[.*s\]$" $TMPDIR/out1.txt | tail -30
```

```
1:----- cell 1 
64:  [0.7s]
65:----- cell 2 
189:  [0.5s]
190:----- cell 3 
412:  [1.4s]
413:----- cell 5 
418:  [0.2s]
419:----- cell 7 ['sanity']
441:n_art                     155.0    NaN           NaN  NaN   8.870968  10.076145       0.0       1.0       5.0      12.0   48.0Traceback (most recent call last):
452:    raise ValueError(f"Unknown `variant` '{variant}' specified. "
454:ValueError: Unknown `variant` 'a' specified. `variant` must be 'b' or 'c'.
494:  [0.0s]
495:----- cell 8 ['sanity']
544:  [0.0s]
545:----- cell 10 ['sanity']
552:  [0.1s]
553:----- cell 12 ['claim:participants']
567:  [0.0s]
568:----- cell 15 ['claim:supp-table1-behavior-by-age']
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/for v in \["a", "c"\]:/for v in ["c"]:/' cells.py && cd entries/openneuro-ds000228-richardson-2018 && source $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py $TMPDIR/cells.py reproduce_richardson_2018.ipynb && python $TMPDIR/devrun.py reproduce_richardson_2018.ipynb 2>&1 | grep -v Warning > $TMPDIR/out1.txt; grep -n "^----- cell\|Error\|Traceback\|\[.*s\]$" $TMPDIR/out1.txt | tail -30
```

```
981:----- cell 84 ['claim:rc-overlap']
994:  [0.3s]
995:----- cell 87 
1014:  [0.0s]
1015:----- cell 88 ['claim:rc-child-adult-timecourse']
1028:  [0.0s]
1029:----- cell 90 ['claim:supp-table4-other-networks']
1057:  [0.0s]
1058:----- cell 93 ['claim:rc-age-events']
1085:  [0.1s]
1086:----- cell 95 ['claim:rc-t04-tom']
1110:  [0.1s]
1111:----- cell 97 ['claim:rc-fb-no-difference']
1135:  [19.0s]
1136:----- cell 100 ['claim:rc-3yo-events']
1162:  [0.2s]
1163:----- cell 103 
1173:  [0.0s]
1174:----- cell 104 ['claim:maturity-across']
1193:  [0.1s]
[... 10 more lines not kept]
```

**Agent**

It all runs. Now read the outputs.

**Agent calls Bash**

```bash
date -u; sed -n 545,800p $TMPDIR/out1.txt
```

```
Wed Oct 28 16:30:37 UTC 2026
children 3yo        17.00      17.0
children 4yo        14.00      14.0
children 5yo        34.00      34.0
children 7yo        23.00      23.0
children 8-12yo     34.00      34.0
mean child age       6.71       6.7
Age-group ranges: {'3yo': {'min': 3.52, 'max': 3.99}, '4yo': {'min': 4.06, 'max': 4.86}, '5yo': {'min': 5.01, 'max': 5.99}, '7yo': {'min': 7.0, 'max': 7.96}, '8-12yo': {'min': 8.02, 'max': 12.3}}
The 5 children excluded for motion are not in the dataset (155 participants listed).
  [0.0s]
----- cell 15 ['claim:supp-table1-behavior-by-age']
           mean    std  count  expected  within 10%
AgeGroup                                           
3yo       0.517  0.178     17      0.54        True
4yo       0.610  0.152     14      0.63        True
5yo       0.724  0.154     34      0.73        True
7yo       0.875  0.080     23      0.88        True
8-12yo    0.956  0.063     34      0.96        True
FB_Group  pass  inc  fail
AgeGroup                 
[... 237 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 800,1010p $TMPDIR/out1.txt
```

```
b (no covariate)       8
O1 with_data, O2b, O3a  a (partial, motion)    8
                        b (no covariate)       8
O1 with_data, O2b, O3b  a (partial, motion)    8
                        b (no covariate)       8
  [0.2s]
----- cell 60 ['claim:irc-3yo-distinct']
                  reading  wToM  sem ToM  wPain  sem Pain  t ToM-across       p1  t Pain-across       p2  in tolerance (of 4)
0        O1 all, O2a, O3a 0.326   0.0273  0.179    0.0212          8.43 2.77e-07           4.54 0.000338                    0
1        O1 all, O2a, O3b 0.325   0.0264  0.182    0.0218          8.71 1.82e-07           4.43 0.000418                    0
2        O1 all, O2b, O3a 0.321   0.0247  0.185    0.0204          8.37 3.06e-07              5  0.00013                    0
3        O1 all, O2b, O3b 0.322   0.0244  0.187    0.0212          8.52 2.42e-07           4.79 0.000201                    0
4  O1 with_data, O2a, O3a 0.326   0.0273  0.179    0.0212          8.43 2.77e-07           4.54 0.000338                    0
5  O1 with_data, O2a, O3b 0.325   0.0264  0.182    0.0218          8.71 1.82e-07           4.43 0.000418                    0
6  O1 with_data, O2b, O3a 0.321   0.0247  0.185    0.0204          8.37 3.06e-07              5  0.00013                    0
7  O1 with_data, O2b, O3b 0.322   0.0244  0.187    0.0212          8.52 2.42e-07           4.79 0.000201                    0
expected wToM .21, wPain .23 (tolerance .02), t 6.2 and 6.9 (10%), n = 17
  [0.0s]
----- cell 62 ['claim:irc-3yo-not-anticorrelated']
                  reading  mean across    sem  t vs 0 (variant)       p
[... 191 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1010,1280p $TMPDIR/out1.txt
```

```
Pain     7.1e-13  4.0e-12  1.3e-24  6.4e-36  7.4e-48      6.0e-37
Scene    2.6e-19  4.3e-23  1.1e-33  1.6e-32  1.3e-44      1.0e-38
ToM      7.6e-03  2.5e-05  1.3e-14  7.2e-25  2.5e-34      3.1e-24
V1       6.0e-09  1.2e-20  6.5e-29  8.8e-26  1.3e-32      4.0e-30
  [0.0s]
----- cell 88 ['claim:rc-child-adult-timecourse']
network  group     r        p  expected  in tolerance  p < .0005
    ToM    3yo 0.212  0.00761      0.28         False      False
    ToM    4yo 0.329  2.5e-05      0.31          True       True
    ToM    5yo 0.564 1.27e-14       0.6          True       True
    ToM    7yo 0.703 7.23e-25      0.72          True       True
    ToM 8-12yo 0.785 2.51e-34      0.82          True       True
network  group     r        p  expected  in tolerance  p < .0005
   Pain    3yo 0.531 7.08e-13       0.6         False       True
   Pain    4yo 0.516 4.01e-12      0.56          True       True
   Pain    5yo 0.701 1.26e-24      0.73          True       True
   Pain    7yo 0.797 6.43e-36      0.83          True       True
   Pain 8-12yo 0.862 7.41e-48      0.89          True       True
  [0.0s]
----- cell 90 ['claim:supp-table4-other-networks']
[... 243 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open("cells.py").read()
s=s.replace('''        df = pd.DataFrame(t.summary().data[1:], columns=t.summary().data[0])
        print(" Tukey,", scale); print(df.to_string(index=False))''','''        df = pd.DataFrame(t.summary().data[1:], columns=t.summary().data[0])
        df["p-adj (exact)"] = [f"{x:.2g}" for x in t.pvalues]
        print(" Tukey,", scale); print(df.to_string(index=False))''')
s=s.replace('''print(ctrl.pivot(index="reading", columns="measure", values="p")[CTRL].round(4).to_string())''','''print(ctrl.pivot(index="reading", columns="measure", values="p")[CTRL].map(lambda x: f"{x:.2g}").to_string())''')
s=s.replace('''best = score.sort_values(["table events found", "count error"], ascending=[False, True]).index[0]
BEST_SPAN, BEST_O5 = best
print("best-matching reading (most table events found, then smallest count error):", best)''','''# Most table events found, then smallest count error; ties between the two O6 spans go to O6b
# (all 168 TRs): the Methods (paragraph 9) z-normalize each ROI timecourse and only then leave out
# the first 10 timepoints from the t-tests.
score["O6 preference"] = [0 if span == "all" else 1 for span, _ in score.index]
best = score.sort_values(["table events found", "count error", "O6 preference"], ascending=[False, True, True]).index[0]
BEST_SPAN, BEST_O5 = best
print("best-matching reading (most table events found, then smallest count error, then O6b):", best)''')
open("cells.py","w").write(s)
EOF
grep -c "O6 preference" cells.py
```

```
2
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018 && source $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py $TMPDIR/cells.py reproduce_richardson_2018.ipynb && python $TMPDIR/devrun.py reproduce_richardson_2018.ipynb 2>&1 | grep -v Warning > $TMPDIR/out2.txt; grep -n "Traceback" $TMPDIR/out2.txt; grep -A8 "Tukey" $TMPDIR/out2.txt | grep -v "^--$" | head -80; grep -A12 "claim:irc-control" $TMPDIR/out2.txt | tail -11; grep "best-matching\|isolated" $TMPDIR/out2.txt
```

```
Tukey, z-scored (O9a)
group1 group2  meandiff  p-adj   lower  upper  reject p-adj (exact)
  fail    inc    0.1561 0.8455 -0.5222 0.8344   False          0.85
  fail   pass    1.2399 0.0000  0.6120 1.8679    True       3.8e-05
   inc   pass    1.0838 0.0001  0.5106 1.6571    True       7.8e-05
 Tukey, raw (O9b)
group1 group2  meandiff  p-adj   lower  upper  reject p-adj (exact)
  fail    inc    0.0262 0.8455 -0.0875 0.1398   False          0.85
  fail   pass    0.2077 0.0000  0.1025 0.3129    True       3.8e-05
   inc   pass    0.1816 0.0001  0.0855 0.2776    True       7.8e-05

== beh-fb-tom, reading (b): full ToM score
           mean    sem  count
FB_Group                     
 Tukey, z-scored (O9a)
group1 group2  meandiff  p-adj  lower  upper  reject p-adj (exact)
  fail    inc    0.6606 0.0073 0.1543 1.1670    True        0.0073
  fail   pass    1.8833 0.0000 1.4145 2.3521    True       1.6e-13
   inc   pass    1.2227 0.0000 0.7947 1.6506    True       1.1e-08
 Tukey, raw (O9b)
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
grep -B2 -A10 "^measure                    wToM" $TMPDIR/out2.txt | head -14; date -u
```

```
O1 with_data, O2b, O3a  0.371  0.526   0.291  0.235  -0.251  0.118 -0.061       0.071  0.193
O1 with_data, O2b, O3b  0.379  0.538   0.300  0.246  -0.251  0.125 -0.083       0.076  0.216
measure                    wToM    wPain   wScene     wM1  across wFace   wV1 aFaceScene  aM1V1
reading                                                                                        
O1 all, O2a, O3a        3.5e-05  6.4e-10   0.0014   0.012  0.0064  0.25  0.45       0.48  0.028
O1 all, O2a, O3b        3.2e-05  8.9e-11    0.001  0.0074  0.0051   0.2   0.4       0.44  0.017
O1 all, O2b, O3a        2.8e-05  5.7e-10   0.0012  0.0096  0.0056   0.2  0.51       0.44  0.034
O1 all, O2b, O3b        1.8e-05    2e-10  0.00083  0.0066  0.0054  0.17  0.37       0.41  0.017
O1 with_data, O2a, O3a  3.5e-05  6.4e-10   0.0014   0.012  0.0064  0.25  0.45       0.48  0.028
O1 with_data, O2a, O3b  3.2e-05  8.9e-11    0.001  0.0074  0.0051   0.2   0.4       0.44  0.017
O1 with_data, O2b, O3a  2.8e-05  5.7e-10   0.0012  0.0096  0.0056   0.2  0.51       0.44  0.034
O1 with_data, O2b, O3b  1.8e-05    2e-10  0.00083  0.0066  0.0054  0.17  0.37       0.41  0.017
paper: wToM .39 (<.0001), wPain .38 (<.0001), wScene .23 (.01), wM1 .30 (.001), across -.26 (.005); wFace .06 (.53), wV1 -.16 (.09), aFaceScene .02 (.8), aM1V1 .18 (.05)
Wed Oct 28 16:33:06 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -c "Result: TBD" cells.py && python3 - <<'EOF'
s=open("cells.py").read()
# diagnostic variant cell after irc-adult code
anchor="''', tags=[\"claim:irc-adult\"])\n"
diag='''
code(r\'\'\'
# Variants that are not the paper's method, to show how far the adult and 3yo means move with the
# filter and the CompCor regressors (main reading otherwise).
def means_with(clean_fn, idx):
    vals = []
    for s in idx:
        tc = {r: clean_fn(s, r) for r in TP}
        m = sb.irc_matrix(tc, TP)
        vals.append([sb.within(m, sb.TOM_ROIS), sb.within(m, sb.PAIN_ROIS), sb.across(m, sb.TOM_ROIS, sb.PAIN_ROIS)])
    return np.round(np.mean(vals, axis=0), 3)
def m1_of(s):
    r, l = D[s]["rois"]["right_primotor"], D[s]["rois"]["left_primotor"]
    return (r["all"] * r["n_vox"] + l["all"] * l["n_vox"]) / (r["n_vox"] + l["n_vox"])
def variant(hp_cutoff=sb.HIGHPASS_S, compcor=True):
    def f(s, r):
        d = D[s]; bad = sb.artifact_index(d["artifacts"])
        y = sb.nearest_neighbour_fill(d["rois"][r]["all"], bad) if len(bad) else d["rois"][r]["all"].copy()
        parts = ([d["compcor"].T] if compcor else []) + ([d["artifacts"].T] if len(bad) else []) + [m1_of(s)[:, None]]
        y = sb.residualize(y, np.column_stack(parts))
        if hp_cutoff:
            hp = sb.dct_highpass_basis(sb.N_TR, sb.TR_S, hp_cutoff); y = y - hp @ np.linalg.lstsq(hp, y, rcond=None)[0]
        y[bad] = np.nan
        return y
    return f
y3_idx = children[children.AgeGroup == "3yo"].index
for name, fn in {"paper (100 s, CompCor)": variant(), "no high-pass": variant(None), "50 s high-pass": variant(50.0), "no CompCor": variant(compcor=False)}.items():
    print(f"{name:24s} adults (wToM, wPain, across) {means_with(fn, adults.index)}   3yo {means_with(fn, y3_idx)}")
print("paper: adults .48, .35, -.17; 3yo .21, .23, .05")
\'\'\', tags=["claim:irc-adult"])
'''
s=s.replace(anchor, anchor+diag,1)
R=[
"**Result: reproduced.** All nine counts match exactly (122 children, 33 adults, 64 and 20 female; 17, 14, 34, 23 and 34 children by age group) and the mean child age is 6.71 years against 6.7. The age-group ranges match Supplementary Table 1. The five children excluded for motion are not in the dataset.",
"**Result: reproduced.** The five mean ToM scores (.517, .610, .724, .875, .956) are within 10% of .54, .63, .73, .88 and .96, and the nine false-belief group counts by age (4/4/9, 3/7/4, 23/9/2) match exactly.",
"**Result: reproduced.** ToM score against age: tau-b = .665 (paper .66), p = 5.4e-26. DCCS against age in the 64 children with a DCCS score: tau-b = .198 (paper .20), p = .048 (paper .049, same side of .05).",
"**Result: reproduced.** Partial Kendall tau of ToM and DCCS given age = .186 (paper .19, tolerance .019), p = .031 (paper .03).",
"**Result: reproduced.** 30 passers (15 female), 20 inconsistent (13 female), 15 failers (6 female), as deposited in FB_Group; the groups recomputed from FB_Composite with the Methods' cut-offs are the same.",
"**Result: reproduced.** Under reading (a), the 18 non-false-belief items deposited as ToM Booklet-Matched-NOFB, the means are .546, .572 and .753 (paper .55, .57, .75) and Kruskal-Wallis H = 22.95 (paper 22.96), p = 1e-05. The Tukey tests match: Pass-Fail diff 1.24 on the z scale (paper 1.2), p = 3.8e-05; Pass-Inc 1.08 (paper 1.08), p = 7.8e-05; Inc-Fail .16 (paper .16), p = .85. The z-scaled diffs (O9a) are the ones that match the paper's. Reading (b), the full score, gives means .451, .571, .792, out of tolerance for failers and passers.",
"**Result: reproduced.** Mean ages 4.08, 4.75 and 5.23 (paper 4.1, 4.8, 5.2). Tukey on the z scale: Pass-Fail diff 1.42 (paper 1.4), p = 4.3e-06; Inc-Fail .83 (paper .83), p = .015 (paper .01); Pass-Inc .59 (paper .59), p = .047 (paper .047).",
"**Result: reproduced.** Mean DCCS 1.733, 2.263 and 2.333 (paper 1.73, 2.26, 2.33), Kruskal-Wallis H = 7.56, p = .023 (paper 7.56, .02); Tukey Pass-Fail diff .88 on the z scale (paper .88), p = .012; Inc-Fail .78 (paper .78), p = .052 (paper .052, reported, not deciding).",
"**Result: reproduced.** Mean artifact timepoints 10.51 (s.d. 10.6) in children and 2.82 (s.d. 4.0) in adults (paper 10.5 and 2.8); Welch t = 6.49 on 137.7 df, p = 1.4e-09, as in the paper.",
"**Result: reproduced.** Neither correlation is significant: Spearman with age .017, p = .86; Kendall with ToM score -.005, p = .94, the paper's values.",
"**Result: reproduced.** Neither effect is significant: FB group t = .12, p = .90 (z-scaled b = .039; the paper's sign is the opposite coding), DCCS t = 1.17, p = .24 (z-scaled b = .148, paper .16).",
"**Result: partially reproduced.** Within-ToM and within-Pain correlations are strongly positive in adults and above the across-network value (t = 19.1 and 21.8 under the main reading, both p < 1e-18), but the means are .604, .398 and -.051 against .48, .35 and -.17, all three out of tolerance under every reading; the two t values are within tolerance under three of the four O2 and O3 readings. The across-network mean is negative (-.051) but much weaker than the paper's. None of the variants outside the paper's method (no high-pass, 50 s high-pass, no CompCor) brings the means to the paper's.",
"**Result: not reproduced (irc-age-within), not reproduced (irc-age-across), by Rule S.** Within-ToM rises with age (partial rs = .306, p = .00064) and within-Pain too (.461, p = 1.1e-07), and the across-network correlation falls (-.259, p = .0041), so the directions hold and all three are significant at .05. But rs within-ToM and across are out of tolerance (.37 and -.35, 10%) and their p-values do not reach the paper's bounds (p < .00005 and p < .0001) under any reading; within-Pain is much stronger than the paper's .28. Rule S counts a test that does not meet the paper's bound as failing.",
"**Result: partially reproduced.** Adults have higher within-ToM (t = -6.54 for the child effect, p = 8.7e-10) and within-Pain (t = -6.72, p = 3.5e-10) correlations and a more negative across-network correlation (t = 4.49, p = 1.4e-05) than children, so the tests hold with the paper's signs, but all three t values are outside 10% of -5.7, -3.8 and 7.2 under every reading. z-scaled b values are -1.16, -1.20 and .83 (paper -.97, -.75, 1.26). The motion effects differ from the paper's: on within-ToM t = -1.64 (paper -4.3), on across t = 2.87, p = .005 (paper not significant).",
"**Result: partially reproduced.** The ToM and Pain age effects hold (within-ToM rs = .367, p = 3.5e-05; within-Pain .525, p = 6.4e-10; across -.247, p = .0064), with within-ToM and across in tolerance and within-Pain out (.38 expected). Within-Scene (.288, p = .0014) and within-M1 (.227, p = .012) rise with age as in the paper, both out of tolerance. Within-Face (.106, p = .25), within-V1 (-.069, p = .45) and across Face-Scene (.065, p = .48) show no age effect, as in the paper, but across M1-V1 does (.200, p = .028; paper .18, p = .05) under every reading.",
"**Result: partially reproduced.** The six differences the paper finds significant are significant in the same direction under both readings (Face and V1 against ToM and Pain, t = 2.51 to 5.03; across ToM-Pain against Face-Scene and M1-V1, t = -2.95 and -4.0, main reading, reading a). Of the four the paper finds not significant, ToM against Scene (t = .75) and ToM against M1 (t = 1.32) are not, but Pain against Scene (t = 2.62, p = .0098) and Pain against M1 (t = 2.92, p = .0043) are. 8 of 10 comparisons follow the paper under every reading.",
"**Result: not reproduced, by Rule S.** In the 17 three-year-olds within-ToM (.326) and within-Pain (.179) exceed the across-network value (t = 8.43, p = 2.8e-07; t = 4.54, p = .00034), so the networks are distinct, but none of the four values is within tolerance (.21, .23, 6.2, 6.9), and the Pain test does not reach the paper's bound of p < .00001 under any reading.",
"**Result: partially reproduced.** The 3yo across-network mean is positive, .074 (s.e. .020), not anti-correlated, against adults' -.051; it is just outside the tolerance (.05 ± .02) under every reading (.074 to .075). A one-sample t-test shows it above 0 (t = 3.75, p = .0017).",
"**Result: not reproduced.** In the 3yo mean matrix the strongest Pain pair is RInsula-LInsula (.856), and the three homologous Pain pairs are the top three, but the strongest ToM pair is RTPJ-PC (.637); RTPJ-LTPJ (.558) ranks fourth of 15. Neither reading of the criterion holds for ToM.",
"**Result: partially reproduced.** Under reading (b), dropping only the two pairs the paper names, non-bilateral within-ToM (.309, t = 7.64, p = 1e-06) and within-Pain (.146, t = 3.03, p = .008) exceed the across-network value, so the tests hold, but the means and t values are out of tolerance (except Pain t under O2b, 3.43 and 3.3). Under reading (a), dropping all three Pain pairs, non-bilateral Pain (.106) does not differ from across (t = 1.34, p = .20).",
"**Result: partially reproduced.** Within-ToM correlation rises with ToM score controlling for motion (partial tau = .246, p = 6.3e-05; paper .23, within tolerance). The across-network correlation falls with ToM score (tau = -.125, p = .042) but less than the paper's -.20, out of tolerance; both tests are significant with the paper's signs.",
"**Result: not reproduced, resting on an assumption.** Under the main reading (O2a, O3a) the ToM score effect on within-ToM is significant with age and motion in the model (t = 2.04, p = .044); on across-network it is not (t = 1.29, p = .20). The readings disagree: O3b gives p = .069, O2b .048, O2b with O3b .088. The main reading is adopted (see deviations).",
"**Result: not reproduced (irc-fb-within, irc-fb-within-dccs, irc-fb-across; irc-fb-across rests on an assumption).** Passers have a slightly higher within-ToM correlation than failers (.398 against .345), but with age and motion the group effect is not significant (t = .66, p = .51; paper p = .046) under any reading, and with DCCS added p = .69, outside the .05 to .10 band. Across-network, passers (.087) are above failers (.057) and the group effect is significant under the main reading (t = -2.18, p = .035), where the paper finds none; O3b gives p = .051, O2b .034, O2b with O3b .047.",
"**Result: partially reproduced.** At p < .05 uncorrected (reading O5a, the best match to Supplementary Table 3; O6 makes no difference for these networks), all seven ToM events and 10 of 12 pain events of Supplementary Table 3 are found (P08 and P10 missed), but the counts are 9 ToM events (80 s) and 10 pain events (84 s), against 7 (68 s) and 12 (86 s). The ToM count matches under O5b and O5c (7 events, 56 s), where only 8 of 12 pain events are found. The pain time (84 s) is within tolerance; the ToM time is not under any reading.",
"**Result: partially reproduced.** The ToM and pain events found (O5a) do not overlap at all (0 TRs, where the paper has 1), which is less than chance: 2 of 1000 permutations have as little overlap under reading (a) and 2 under (b) (p = .002, mean permuted overlap 11.9 TRs). The overlap count differs from the paper's by one timepoint. With the paper's own events from Supplementary Table 3 the overlap is 1 TR (the last of T05 and first of P05), p = .002 (a) and .008 (b).",
"**Result: partially reproduced.** Every age group's mean timecourse correlates with the adult mean, at p < .01 (the paper's Bonferroni alpha) in every case: ToM r = .212, .329, .564, .703, .785 and Pain .531, .516, .701, .797, .862. 8 of 10 values are within 10%; ToM 3yo (.212 against .28, p = .0076) and Pain 3yo (.531 against .60) are below.",
"**Result: not reproduced.** 17 of the 25 values are within 10% (the criterion's partial outcome needs 20). The significance pattern holds at p < .0005 (only 3yo M1, p = .00078, and 4yo M1, p = .019, are not), but the M1 values differ throughout (.265, .186, .434, .350, .315 against .11, .06, .35, .44, .53), and the 3yo Face (.637 against .75), V1 (.442 against .53) and FFA (.589 against .72) values are low.",
"**Result: not reproduced.** Under the z-normalized magnitudes (O7a, either O6 span), four events pass p < .0026 with positive rs: T02 (.325), T07 (.352), P04 (.324) and T03 (.274). Of the paper's five (P01, P04, P08, T01, T02), only P04 and T02 pass; P01 (rs = .193, p = .038), T01 (.270, p = .0036) and P08 (.019, p = .84) do not, and T03 and T07 pass where the paper has them not. Under O7b no event passes.",
"**Result: not reproduced.** The T04 magnitude does not rise with ToM score with age and motion in the model: t = 1.18, p = .24 (O7a, TRs 11 to 168; t = 1.14 and .71 under the other readings), against t = 2.98, p = .0035. No ToM event passes p < .007 under any reading.",
"**Result: reproduced, resting on an assumption.** Under the z-normalized magnitudes (O7a), no ToM event differs between passers and failers with age and motion in the model (smallest p = .091 for T05 with O6a, .072 with O6b; T03 permutation p = .72). Under O7b, magnitudes before z-normalization, T05 has p = .0497, just below .05. O7a is adopted (see deviations).",
"**Result: partially reproduced, resting on an assumption.** Under the rc-events reading (O5a) with O6b, the 3yo pain events (40 s) overlap 6 of the 12 adult pain events (22 s in adult pain events) and adult ToM event T04 (6 s), and the 3yo ToM events (24 s) overlap 1 of 7 adult ToM events (4 s) and adult pain event P01 (4 s). The two cross-network overlaps of the claim hold; the times and the pain-event count do not (paper 32 s, 4 of 12, 14 s, 8 s in T04; 8 s of ToM events). Under O6a the 3yo ToM events do not overlap P01 (0 s), so the claim would not be reproduced; O6b is adopted (see deviations).",
"**Result: partially reproduced.** With age and motion in the model, a stronger across-network anti-correlation predicts a more adult-like timecourse in both networks (ToM t = -4.52, p = 1.5e-05; Pain t = -3.55, p = .00055), with the paper's sign, but both t values are out of tolerance (-5.5 and -7.4). Within-ToM does not predict ToM maturity (t = 1.53, p = .13), as in the paper; within-Pain does predict Pain maturity (t = 2.40, p = .018), where the paper's effect was not significant (p = .06).",
"**Result: reproduced, resting on an assumption.** Under the main reading neither maturity effect is significant (within-ToM t = .83, p = .41; within-Pain t = 1.80, p = .075), while age is (t = 2.39, p = .019; t = 4.22, p = 4.9e-05). Under O2b with O3b the Pain maturity effect has p = .040; the main reading is adopted (see deviations).",
"**Result: reproduced.** ToM maturity correlates with ToM score controlling for motion (partial rs = .498, p = 6.1e-09; paper .54, tolerance .054). With age in the regression the ToM score effect vanishes (t = .04, p = .97) while age remains (t = 4.46, p = 1.8e-05).",
"**Result: reproduced.** ToM maturity does not differ between passers and failers with age and motion in the model (t = 1.53, p = .13; failers .095, passers .168).",
"**Result: not reproduced.** The children's mean fusiform timecourse correlates with the adults' (r = .818, within 10% of .86, p = 2.8e-39), but the 3yo correlation is .589 against .72, outside tolerance and above the paper's bound (p = 3.8e-16 against p < 1e-26). Reverse correlation finds 10 adult face events (108 s) and 6 three-year-old events (32 s) under the rc-events reading (O5a, O6b), against 7 (88 s) and 4 (18 s); no reading gives 7 adult events. No face-event magnitude changes with age at alpha .0071 (smallest p = .011), as in the paper.",
"**Result: reproduced.** The face events overlap the ToM events by 7 TRs and the pain events by 25 TRs (paper 4 and 15), and neither overlap is smaller than chance (p = .052 and .983 under the rc-events reading; .098 to .166 and .94 to .96 under the others).",
]
parts=s.split("**Result: TBD**")
assert len(parts)==len(R)+1, (len(parts), len(R))
out=parts[0]
for r,pp in zip(R,parts[1:]): out+=r+pp
open("cells.py","w").write(out)
EOF
```

```
37
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open("cells.py").read()
s=s.replace("out of tolerance (except Pain t under O2b, 3.43 and 3.3)","out of tolerance (except the Pain mean under O2b, .152 and .153)")
s=s.replace("No face-event magnitude changes with age at alpha .0071 (smallest p = .011), as in the paper.","No face-event magnitude changes with age at alpha .0071 (smallest p = .010), as in the paper.")
summary = r'''## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| participants | reproduced |
| supp-table1-behavior-by-age | reproduced |
| beh-tom-age | reproduced |
| beh-tom-dccs | reproduced |
| beh-fb-groups | reproduced |
| beh-fb-tom | reproduced |
| beh-fb-age | reproduced |
| beh-fb-dccs | reproduced |
| motion-child-adult | reproduced |
| motion-not-age-tom | reproduced |
| motion-not-fb | reproduced |
| irc-adult | partially reproduced |
| irc-age-within | not reproduced |
| irc-age-across | not reproduced |
| irc-adult-vs-child | partially reproduced |
| irc-control-networks | partially reproduced |
| irc-williams | partially reproduced |
| irc-3yo-distinct | not reproduced |
| irc-3yo-not-anticorrelated | partially reproduced |
| irc-3yo-homologous | not reproduced |
| irc-3yo-nonbilateral | partially reproduced |
| irc-tom-behavior | partially reproduced |
| irc-tom-behavior-age | not reproduced (assumed reading) |
| irc-fb-within | not reproduced |
| irc-fb-within-dccs | not reproduced |
| irc-fb-across | not reproduced (assumed reading) |
| rc-events | partially reproduced |
| rc-overlap | partially reproduced |
| rc-child-adult-timecourse | partially reproduced |
| supp-table4-other-networks | not reproduced |
| rc-age-events | not reproduced |
| rc-t04-tom | not reproduced |
| rc-fb-no-difference | reproduced (assumed reading) |
| rc-3yo-events | partially reproduced (assumed reading) |
| maturity-across | partially reproduced |
| maturity-within | reproduced (assumed reading) |
| maturity-tom-behavior | reproduced |
| maturity-fb | reproduced |
| face-rc | not reproduced |
| face-overlap | reproduced |
| replication-sample | blocked: the independent adult sample is not public |
| hand-coded-events | blocked: the hand coding of Jacoby et al. 2016 is not in the dataset or the paper |

How the analysis differs from the paper's. The analysis starts from the paper's own
preprocessed images, artifact indicators, CompCor regressors and ROI masks, all deposited in the
snapshot, so the differences are in the steps after them: the ROI-mean shortcut (exact for the
linear steps the Methods describe), SPM's discrete cosine high-pass filter for "a cutoff of 100
s", an intercept in the nuisance regression, the ppcor forms of the partial correlations, and the
readings O1 to O9 of the claims file, each run. The paper's analysis code is not public.

What was found about the dataset. Every behavioural and demographic number of the paper is
recovered exactly from participants.tsv, and the artifact counts match the Methods to the
decimal. The deposited ROI masks have the sizes of Supplementary Table 2, and the artifact
indicators line up with spikes in the image data (median deviation 6.45 at the flagged
timepoints against at most 2.6 one or two TRs away). With these data and the pipeline of the
Methods, the inter-region correlations are higher within networks and less negative across
networks than the paper reports (adults .604, .398, -.051 against .48, .35, -.17), and the
event-level tests of age and ToM score (rc-age-events, rc-t04-tom) and the false-belief group
effect on within-ToM correlation do not come out as in the paper. The voxel-size column
(named "Scanlog: Voxel slize") counts 2 seven-year-olds and 21 8-12-year-olds at 3.13 mm with
no slice gap, where the Methods say 3 and 20, and the no-gap level is stored as an empty value
where participants.json defines "None". The face-ROI coverage count differs from Supplementary
Fig. 4 (19 participants with any face-ROI voxel without data, against 17).
'''
i=s.index("## Summary")
j=s.index("''')", i)
s=s[:i]+summary+s[j:]
open("cells.py","w").write(s)
EOF
cd entries/openneuro-ds000228-richardson-2018 && source $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py $TMPDIR/cells.py reproduce_richardson_2018.ipynb && python $TMPDIR/devrun.py reproduce_richardson_2018.ipynb 2>&1 | grep -v Warning > $TMPDIR/out3.txt; grep -n "Traceback" $TMPDIR/out3.txt; grep -A6 "paper (100 s" $TMPDIR/out3.txt; date -u
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/build_nb.py", line 14, in <module>
    exec(open(sys.argv[1]).read())
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 258
    md('**Result: reproduced.** 30 passers (15 female), 20 inconsistent (13 female), 15 failers (6 female), as deposited in FB_Group; the groups recomputed from FB_Composite with the Methods' cut-offs are the same.')
                                                                                                                                                                                                                      ^
SyntaxError: unterminated string literal (detected at line 258)
grep: /tmp/claude-1001/out3.txt: No such file or directory
grep: /tmp/claude-1001/out3.txt: No such file or directory
Wed Oct 28 16:34:38 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
lines=open("cells.py").read().split("\n")
out=[]
for l in lines:
    if l.startswith("md('**Result:") and l.endswith("')"):
        l='md("""'+l[4:-2]+'""")'
    out.append(l)
open("cells.py","w").write("\n".join(out))
EOF
cd entries/openneuro-ds000228-richardson-2018 && source $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py $TMPDIR/cells.py reproduce_richardson_2018.ipynb && python $TMPDIR/devrun.py reproduce_richardson_2018.ipynb 2>&1 | grep -v Warning > $TMPDIR/out3.txt; grep -n "Traceback" $TMPDIR/out3.txt; grep -A6 "paper (100 s" $TMPDIR/out3.txt; date -u
```

```
paper (100 s, CompCor)   adults (wToM, wPain, across) [ 0.604  0.398 -0.051]   3yo [0.326 0.179 0.074]
no high-pass             adults (wToM, wPain, across) [0.626 0.397 0.032]   3yo [0.334 0.19  0.097]
50 s high-pass           adults (wToM, wPain, across) [ 0.556  0.38  -0.017]   3yo [0.333 0.17  0.072]
no CompCor               adults (wToM, wPain, across) [0.645 0.465 0.059]   3yo [0.401 0.286 0.187]
paper: adults .48, .35, -.17; 3yo .21, .23, .05
  [0.6s]
----- cell 50 ['claim:irc-age-within', 'claim:irc-age-across']
Wed Oct 28 16:35:26 UTC 2026
```

**Agent calls ToolSearch**

```json
{
 "query": "select:WebSearch,WebFetch",
 "max_results": 2
}
```

Result: no output.

**Agent calls WebSearch**

```json
{
 "query": "Jacoby Bruneau Koster-Hale Saxe 2016 NeuroImage \"Partly Cloudy\" localizer mental pain events timing"
}
```

Result: the fetched text is not kept.

**Agent calls WebFetch**

```json
{
 "url": "https://saxelab.mit.edu/theory-mind-and-pain-matrix-localizer-movie-viewing-experiment",
 "prompt": "What downloads are offered (URLs), and is there a DOI, OSF or GitHub link with a version or commit? Are the hand-coded event onsets listed on the page?"
}
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open("cells.py").read()
old='''- hand-coded-events: the "mental", "social" and "pain" coding of Jacoby et al. (2016) is not in
  the snapshot; the README lists only the reverse-correlation events, and the paper does not
  give the coded times.'''
new='''- hand-coded-events: the "mental", "social" and "pain" coding of Jacoby et al. (2016) is not in
  the snapshot (its README lists only the reverse-correlation events), and the paper does not
  give the coded times. The Saxe lab's web page offers the experiment script (movloc.zip,
  version of 29 March 2019) that holds them, with no DOI or repository commit to pin it, so it
  cannot be used as a pinned input.'''
assert old in s
s=s.replace(old,new)
s=s.replace("| hand-coded-events | blocked: the hand coding of Jacoby et al. 2016 is not in the snapshot or the paper |","| hand-coded-events | blocked: the hand coding of Jacoby et al. 2016 is not in the snapshot or the paper, and the lab's script that holds it is not pinned |")
s=s.replace("| hand-coded-events | blocked: the hand coding of Jacoby et al. 2016 is not in the dataset or the paper |","| hand-coded-events | blocked: the hand coding of Jacoby et al. 2016 is in no pinned public source |")
open("cells.py","w").write(s)
EOF
grep -n "hand-coded" cells.py | head
```

```
35:| hand-coded-events | blocked: the hand coding of Jacoby et al. 2016 is not in the snapshot or the paper, and the lab's script that holds it is not pinned |
1058:- hand-coded-events: the "mental", "social" and "pain" coding of Jacoby et al. (2016) is not in
1112:| hand-coded-events | blocked: the hand coding of Jacoby et al. 2016 is in no pinned public source |
Shell cwd was reset to
```

**Agent**

Now entry.yaml and README.

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018 && cat > entry.yaml <<'EOF'
schema_version: 1
name: openneuro-ds000228-richardson-2018
type: reproduction
title: Development of the social brain from age three to twelve (Richardson et al. 2018)
description: Tests the findings of Richardson, Lisandrelli, Riobueno-Naylor and Saxe (2018) on
  OpenNeuro ds000228, which holds movie-viewing fMRI of 122 children aged 3 to 12 and 33 adults,
  with the paper's preprocessed images, artifact and CompCor regressors, group ROIs and
  behavioural scores. It covers the behavioural results, motion, inter-region correlations within
  and across the ToM and pain networks, reverse correlation of network timecourses, functional
  maturity, and the face-region analyses.
license: Apache-2.0
notebooks:
- path: reproduce_richardson_2018.ipynb
  title: Reproducing Richardson et al. (2018) from OpenNeuro ds000228
  runtime_minutes: 5
helpers:
- social_brain.py
related:
- id: openneuro:ds000228/1.1.1
  relation: uses_data
- id: doi:10.1038/s41467-018-03399-2
  relation: reproduces
EOF
cp $TMPDIR/cells.py /dev/null; source $TMPDIR/dev/bin/activate && python $TMPDIR/build_nb.py $TMPDIR/cells.py reproduce_richardson_2018.ipynb && cd  && python tools/entry.py lock entries/openneuro-ds000228-richardson-2018 && date -u
```

```
wrote entries/openneuro-ds000228-richardson-2018/requirements.lock.txt
Wed Oct 28 16:36:14 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "attempts/openneuro-ds000228-richardson-2018-01.yaml",
 "content": "schema_version: 2\nid: openneuro-ds000228-richardson-2018-01\ndataset:\n  archive: openneuro\n  id: ds000228\n  version: 1.1.1\n  doi: 10.18112/openneuro.ds000228.v1.1.1\npaper: doi:10.1038/s41467-018-03399-2\ndate: 2026-10-28\nentry: openneuro-ds000228-richardson-2018\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-12\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/40723326297\noutcomes:\n- claim: participants\n  outcome: reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:participants\n  measured: [122, 33, 64, 20, 17, 14, 34, 23, 34, 6.71]\n  notes: All nine counts match exactly and the mean child age is 6.71 years (s.d. 2.33). The age\n    ranges of the five child groups match Supplementary Table 1. The five children excluded for\n    motion are not in the dataset, so that part of the statement cannot be checked beyond the\n    absence of any participant with one third or more artifact timepoints (maximum 48 of 168).\n- claim: supp-table1-behavior-by-age\n  outcome: reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:supp-table1-behavior-by-age\n  measured: [0.517, 0.61, 0.724, 0.875, 0.956, 30]\n  notes: Mean ToM scores .517, .610, .724, .875 and .956 are within 10% of the paper's. The false\n    belief groups by age are 4/4/9, 3/7/4 and 23/9/2, as in the paper.\n- claim: beh-tom-age\n  outcome: reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:beh-tom-age\n  measured: [0.665, 0.198]\n  notes: ToM score against age, tau-b = .665, p = 5.4e-26 (n = 122). DCCS against age, tau-b =\n    .198, p = .048 (n = 64; paper p = .049). Tau-c gives .654 and .191.\n- claim: beh-tom-dccs\n  outcome: reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:beh-tom-dccs\n  measured: 0.186\n  notes: Partial Kendall tau of ToM and DCCS given age = .186, p = .031 (n = 64).\n- claim: beh-fb-groups\n  outcome: reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:beh-fb-groups\n  measured: [30, 20, 15]\n  notes: 30 passers (15 female), 20 inconsistent (13 female), 15 failers (6 female) in the\n    deposited FB_Group of the 65 children under 6; recomputing the groups from FB_Composite with\n    the Methods' cut-offs gives the same. FB_Group is also filled for 57 children aged 6 and over\n    (54 pass, 3 inc), which the paper does not use.\n- claim: beh-fb-tom\n  outcome: reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:beh-fb-tom\n  measured: [0.546, 0.572, 0.753, 22.95]\n  notes: Reading (a), the 18 non-false-belief items deposited as ToM Booklet-Matched-NOFB, gives\n    means .546, .572, .753 and Kruskal-Wallis H = 22.95, p = 1e-05. Tukey on z-scored scores\n    (O9a), Pass-Fail diff 1.24, p = 3.8e-05; Pass-Inc 1.08, p = 7.8e-05; Inc-Fail .16, p = .85,\n    the paper's diffs. Reading (b), the full ToM score, gives means .451, .571, .792 (failers and\n    passers out of tolerance), H = 41.5, and a significant Inc-Fail difference (p = .0073), so\n    the claim holds under reading (a) only.\n  deviations:\n  - The paper does not define \"remaining ToM items\"; the criterion's two readings were run and\n    reading (a) matches. participants.json describes ToM Booklet-Matched-NOFB as the 18 items\n    without the six false-belief questions.\n- claim: beh-fb-age\n  outcome: reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:beh-fb-age\n  measured: [4.08, 4.75, 5.23]\n  notes: Mean ages 4.08, 4.75, 5.23. Tukey on z-scored age, Pass-Fail diff 1.42, p = 4.3e-06;\n    Inc-Fail .83, p = .015; Pass-Inc .59, p = .047.\n- claim: beh-fb-dccs\n  outcome: reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:beh-fb-dccs\n  measured: [1.733, 2.263, 2.333]\n  notes: Mean DCCS 1.733, 2.263 (n = 19), 2.333; Kruskal-Wallis H = 7.56, p = .023; Tukey on the z\n    scale, Pass-Fail diff .88, p = .012; Inc-Fail .78, p = .052, as in the paper.\n- claim: motion-child-adult\n  outcome: reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:motion-child-adult\n  measured: [10.51, 2.82]\n  notes: Artifact timepoints are the deposited ART indicator rows (one per flagged timepoint).\n    Children 10.51 (s.d. 10.6), adults 2.82 (s.d. 4.0); Welch t = 6.49, df = 137.7, p = 1.4e-09.\n- claim: motion-not-age-tom\n  outcome: reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:motion-not-age-tom\n  notes: Spearman with age .017, p = .86; Kendall with ToM score -.005, p = .94. Neither is\n    significant.\n- claim: motion-not-fb\n  outcome: reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:motion-not-fb\n  notes: FB group (fail coded 1, n = 45), t = .12, p = .90, z-scaled b = .039; DCCS (n = 64), t =\n    1.17, p = .24, z-scaled b = .148. Neither is significant.\n- claim: irc-adult\n  outcome: partially_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:irc-adult\n  measured: [0.604, 0.398, -0.051, 19.1, 21.8]\n  notes: Main reading (O1 all voxels of the deposited masks, O2a, O3a). Adult means within-ToM\n    .604, within-Pain .398, across -.051; paired t within-ToM against across 19.1 and within-Pain\n    against across 21.8, both p < 1e-18. The two t values are in tolerance under three of the\n    four O2 and O3 readings; the three means are out of tolerance under all. O1 with only voxels\n    with data gives identical values. Variants outside the paper's method (no high-pass, 50 s\n    high-pass, no CompCor) give adult means from .556 to .645 within-ToM and -.051 to .059\n    across, none near the paper's.\n  deviations:\n  - The 100 s high-pass filter is SPM's discrete cosine basis (spm_filter); the Methods say SPM8\n    and \"a cutoff of 100 s\" without naming the filter. A standard choice.\n  - The cleaning is applied to the ROI mean timecourse, which equals cleaning each voxel and\n    averaging, as every step of Methods paragraph 4 is linear and the same for each voxel.\n- claim: irc-age-within\n  outcome: not_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:irc-age-within\n  measured: [0.306, 0.461]\n  notes: Partial Spearman with age, motion as covariate, n = 122 children. Within-ToM rs = .306,\n    p = .00064; within-Pain .461, p = 1.1e-07 (main reading); .306 to .324 and .458 to .470\n    under the other readings. Both rise with age and are significant at .05, but both are out of\n    tolerance (.37 and .28), and within-ToM does not reach the paper's bound p < .00005 under any\n    reading, which Rule S counts as a failed test.\n- claim: irc-age-across\n  outcome: not_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:irc-age-across\n  measured: -0.259\n  notes: Across-network partial rs with age = -.259, p = .0041 (main reading; -.259 to -.271,\n    p = .0026 to .0041 under the others). It falls with age, significant at .05, but is out of\n    tolerance (-.35) and does not reach the paper's bound p < .0001, which Rule S counts as a\n    failed test.\n- claim: irc-adult-vs-child\n  outcome: partially_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:irc-adult-vs-child\n  measured: [-6.54, -6.72, 4.49]\n  notes: Regression on group (child = 1) and artifact count. Child effect on within-ToM t =\n    -6.54, p = 8.7e-10; within-Pain t = -6.72, p = 3.5e-10; across t = 4.49, p = 1.4e-05; all\n    with the paper's signs and below its p values, but all three t values are out of tolerance\n    under every reading (-6.23 to -7.05, -6.48 to -6.72, 3.92 to 4.49). z-scaled b (O4a) -1.16,\n    -1.20, .83; raw b -.173, -.135, .087. Motion effects differ from the paper's, within-ToM t =\n    -1.64, p = .10 (paper -4.3), across t = 2.87, p = .005 (paper not significant).\n- claim: irc-control-networks\n  outcome: partially_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:irc-control-networks\n  measured: [0.367, 0.525, 0.288, 0.227, -0.247]\n  notes: No M1 regression, main reading. Age partial rs, within-ToM .367 (p = 3.5e-05), within-Pain\n    .525 (p = 6.4e-10), within-Scene .288 (p = .0014), within-M1 .227 (p = .012), across ToM-Pain\n    -.247 (p = .0064); within-ToM and across are in tolerance, within-Pain, Scene and M1 are not.\n    Within-Face .106 (p = .25), within-V1 -.069 (p = .45) and across Face-Scene .065 (p = .48)\n    are not significant, as in the paper; across M1-V1 is, .200 (p = .028; .017 to .034 under the\n    other readings), where the paper has p = .05 and the criterion counts it as no change. The\n    ToM and Pain results hold and one control result differs, the criterion's partial outcome.\n  deviations:\n  - The face and scene parcels are the ones deposited in derivatives/ROIs of the snapshot\n    (rSTS_masked, lSTS, rOFA, lOFA, rFFA, lFFA; rRSC, lRSC, rTOS, lTOS, rPPA, lPPA), which the\n    dataset's README names as the Julian et al. 2012 parcels; the claims file treats them as an\n    outside input, but no outside data were used. The M1 and V1 ROIs are also deposited.\n- claim: irc-williams\n  outcome: partially_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:irc-williams\n  notes: Williams' T2 (and Steiger's Z, which agrees) on the age correlations of\n    irc-control-networks. Under both readings (partial with motion, or plain Spearman) and every\n    pipeline reading, the six differences the paper finds significant are significant in the same\n    direction (main reading, reading a, t = 2.51 to 5.03 for Face and V1 against ToM and Pain;\n    -2.95 and -4.0 for across ToM-Pain against Face-Scene and M1-V1). ToM against Scene (t = .75)\n    and ToM against M1 (t = 1.32) are not significant, as in the paper, but Pain against Scene (t\n    = 2.62, p = .0098) and Pain against M1 (t = 2.92, p = .0043) are, so the within-Pain age\n    effect is stronger than Scene and M1, unlike the paper. 8 of 10 comparisons follow the paper.\n    The criterion states only the reproduced outcome; the partial outcome is the protocol's\n    \"holds only in part\".\n  deviations:\n  - The paper reports z for Williams' test; Williams' T2 is a t on n - 3 df. Both T2 and\n    Steiger's Z are shown; they give the same conclusions.\n- claim: irc-3yo-distinct\n  outcome: not_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:irc-3yo-distinct\n  measured: [0.326, 0.179, 8.43, 4.54]\n  notes: 17 three-year-olds, main reading. Within-ToM .326, within-Pain .179, both above the\n    across-network value (t = 8.43, p = 2.8e-07; t = 4.54, p = .00034). The networks are distinct,\n    but no value is in tolerance under any reading and the Pain test does not reach the paper's\n    bound p < .00001 (p = .00013 to .00042 across readings), a failed test under Rule S.\n- claim: irc-3yo-not-anticorrelated\n  outcome: partially_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:irc-3yo-not-anticorrelated\n  measured: 0.074\n  notes: 3yo across-network mean .074 (s.e. .020; .074 to .075 under every reading), not\n    negative, just above the tolerance .05 ± .02. Variant one-sample t = 3.75, p = .0017, so the\n    3yo across correlation is above zero. Adults -.051.\n- claim: irc-3yo-homologous\n  outcome: not_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:irc-3yo-homologous\n  notes: In the 3yo mean matrix (main reading) the strongest Pain pair is RInsula-LInsula (.856)\n    and the three homologous Pain pairs rank first to third (.856, .656, .339). Among ToM pairs\n    RTPJ-PC (.637), LTPJ-PC (.635) and DMPFC-MMPFC (.609) are above RTPJ-LTPJ (.558), which ranks\n    fourth, so neither reading holds for ToM. O3b gives the same order.\n- claim: irc-3yo-nonbilateral\n  outcome: partially_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:irc-3yo-nonbilateral\n  measured: [0.309, 0.146, 7.64, 3.03]\n  notes: Reading (b), dropping RTPJ-LTPJ and RInsula-LInsula, main pipeline reading. Non-bilateral\n    ToM .309 (t = 7.64, p = 1e-06) and Pain .146 (t = 3.03, p = .008) both exceed across, with p\n    on the paper's side of .05, but the means and t values are out of tolerance, except the Pain\n    mean under O2b (.152, .153). Reading (a), dropping also RS2-LS2 and RMFG-LMFG, gives Pain .106,\n    t = 1.34, p = .20, not significant. The criterion allows either reading; under (b) the tests\n    hold and values differ.\n- claim: irc-tom-behavior\n  outcome: partially_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:irc-tom-behavior\n  measured: [0.246, -0.125]\n  notes: Partial Kendall tau with ToM score, motion as covariate (ppcor form, O8). Within-ToM\n    .246, p = 6.3e-05, in tolerance; across -.125, p = .042, out of tolerance (-.20 ± .02). Both\n    have the paper's signs and p on the same side of .05. Other readings, .237 to .259 and -.121\n    to -.132.\n- claim: irc-tom-behavior-age\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:irc-tom-behavior-age\n  notes: Regression on ToM score, age and motion, children. Main reading, ToM score effect on\n    within-ToM t = 2.04, p = .044 (z-scaled b = .275), significant, where the paper has none;\n    on across t = 1.29, p = .20. Readings, within-ToM p = .069 (O3b), .048 (O2b), .088 (O2b, O3b);\n    across p = .19 to .27 in all. The outcome rests on the O2a and O3a readings.\n  deviations:\n  - Assumed O2a (one regressor per artifact timepoint), as deposited in the paper's own nuisance\n    files, and O3a (all 168 TRs), since the Methods restrict the timepoints to TRs 11 to 168 only\n    for the reverse correlation and maturity analyses (paragraphs 9 and 13), not for the\n    inter-region correlation (paragraph 7). Under O3b the claim would be reproduced.\n- claim: irc-fb-within\n  outcome: not_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:irc-fb-within\n  measured: [0.398, 0.345, 0.66]\n  notes: Passers (n = 30) .398, failers (n = 15) .345, so passers are higher, but the group effect\n    with age and motion is t = .66, p = .51 (fail coded 1; z-scaled b = .26), not significant\n    under any reading (p = .48 to .55). The paper has t = -2.06, p = .046 and means .29 and .25,\n    both out of tolerance here.\n- claim: irc-fb-within-dccs\n  outcome: not_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:irc-fb-within-dccs\n  measured: 0.4\n  notes: With DCCS added, the group effect is t = .40, p = .69 (other readings p = .59 to .69),\n    outside the .05 to .10 band; DCCS t = -.86, p = .39. It depends on irc-fb-within, which was\n    tested and not reproduced.\n- claim: irc-fb-across\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:irc-fb-across\n  notes: Passers .087, failers .057 (paper .04, .03). Group effect with age and motion t = -2.18,\n    p = .035 under the main reading (fail coded 1, z-scaled b = -.87), significant, where the paper\n    finds no difference. Readings, p = .051 (O3b), .034 (O2b), .047 (O2b, O3b). The outcome rests on\n    the main reading.\n  deviations:\n  - Assumed O2a and O3a, as for irc-tom-behavior-age. Under O3b the claim would be reproduced (p =\n    .051).\n- claim: rc-events\n  outcome: partially_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:rc-events\n  measured: [9, 10, 80, 84]\n  notes: The best-matching reading is O5a (p < .05 uncorrected); O6 changes nothing for the ToM and\n    Pain networks. It finds 9 ToM events (80 s, mean 8.9 s) and 10 pain events (84 s, mean 8.4 s),\n    covering all 7 ToM events and 10 of 12 pain events of Supplementary Table 3 (P08 and P10\n    missed). Under O5b and O5c, 7 ToM events (56 s, all 7 table events) and 8 pain events (62 s,\n    8 of 12). The pain time is in tolerance under O5a, the ToM time under none; the counts never\n    both match. At least 5 of 7 and 9 of 12 table events are found under O5a, the partial\n    outcome. Peak TRs of the found ToM events (131, 95, 64, 150, 46, 125, 54) are within one TR\n    of the table's.\n- claim: rc-overlap\n  outcome: partially_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:rc-overlap\n  measured: [0, 0.002]\n  notes: The found events (O5a) overlap at no timepoint, against 1 in the paper; permutation p =\n    .002 under both readings of the zero counts (mean permuted overlap 11.9 and 11.1 TRs). Under\n    O5b and O5c the overlap is also 0, p = .019 to .036. With the paper's own events (Supplementary\n    Table 3, variant) the overlap is 1 TR, p = .002 and .008. Less overlap than chance holds; the\n    overlap count does not match.\n  deviations:\n  - Seed fixed (a standard choice); the random gaps split the remaining zeros by a multinomial\n    draw after one zero between events, a reading of Methods paragraph 10, which says only \"a\n    random proportion of zeros between events\".\n- claim: rc-child-adult-timecourse\n  outcome: partially_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:rc-child-adult-timecourse\n  measured: [0.212, 0.329, 0.564, 0.703, 0.785, 0.531, 0.516, 0.701, 0.797, 0.862]\n  notes: Every r is significant at the paper's Bonferroni alpha of .01 (ToM 3yo p = .0076, all\n    others p < 3e-05); 8 of 10 are within 10%, ToM 3yo (.212 against .28) and Pain 3yo (.531\n    against .60) are below. ToM 3yo has an exact p in the paper (.00046), judged on the side of\n    the corrected alpha.\n- claim: supp-table4-other-networks\n  outcome: not_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:supp-table4-other-networks\n  measured: [0.637, 0.634, 0.66, 0.825, 0.848, 0.636, 0.684, 0.781, 0.772, 0.847, 0.265, 0.186,\n    0.434, 0.35, 0.315, 0.442, 0.654, 0.742, 0.713, 0.773, 0.589, 0.621, 0.638, 0.812, 0.835]\n  notes: 17 of 25 values within 10%, below the 20 the partial outcome needs. The significance\n    pattern holds (only M1 3yo, p = .00078, and M1 4yo, p = .019, miss p < .0005), but all five\n    M1 values are out of tolerance (.265, .186, .434, .350, .315 against .11, .06, .35, .44, .53),\n    and the 3yo Face, V1 and FFA values are low. Scene matches in every group.\n  deviations:\n  - Face, scene, M1 and V1 ROIs are the ones deposited in the snapshot, not an outside input.\n- claim: rc-age-events\n  outcome: not_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:rc-age-events\n  notes: Magnitudes at the 19 Supplementary Table 3 peak TRs. Under O7a (either O6 span), T02 (rs\n    = .325), T07 (.352), P04 (.324) and T03 (.274) pass p < .0026; of the paper's five, P01 (rs =\n    .193, p = .038), T01 (.270, p = .0036) and P08 (.019, p = .84) do not. Under O7b no event\n    passes. 1 to 8 children per event are left out for an artifact at the peak TR.\n- claim: rc-t04-tom\n  outcome: not_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:rc-t04-tom\n  measured: 1.18\n  notes: T04 magnitude on ToM score, age and motion (n = 114), t = 1.18, p = .24 (O7a, z over TRs\n    11 to 168); 1.14 and .71 under the other readings. No ToM event reaches p < .007 under any\n    reading (smallest p = .061).\n- claim: rc-fb-no-difference\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:rc-fb-no-difference\n  notes: Passers against failers, with age and motion, per ToM event. Under O7a no event differs\n    (smallest p = .091, T05, with O6a; .072 with O6b); T03 permutation p = .72 (5000 permutations\n    of the group labels). Under O7b T05 has p = .0497.\n  deviations:\n  - Assumed O7a, magnitudes from the z-normalized network timecourse, because the events and their\n    peak timepoints are defined on that timecourse (Methods paragraphs 9 and 11, \"the timepoint\n    with the highest average signal value in adults\"). Under O7b the claim would not be\n    reproduced.\n  - The T03 permutation test permutes the group labels and refits the regression (5000\n    permutations, fixed seed); the paper cites R's lmPerm without its settings.\n- claim: rc-3yo-events\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:rc-3yo-events\n  measured: [40, 24, 6, 1]\n  notes: Reverse correlation on the 17 three-year-olds with the rc-events reading (O5a) and O6b.\n    3yo pain events 40 s overlapping 6 of 12 adult pain events (22 s) and T04 (6 s); 3yo ToM events\n    24 s overlapping 1 of 7 adult ToM events (4 s) and P01 (4 s). Both cross-network overlaps hold;\n    times and the pain count do not. Under O6a, pain 40 s, 6 of 12, T04 6 s; ToM 20 s, 1 of 7, P01\n    0 s, so the P01 overlap fails. Adult events are those of Supplementary Table 3.\n  deviations:\n  - The rc-events reading ties between O6a and O6b. Assumed O6b, z-normalization over all 168 TRs,\n    because Methods paragraph 9 z-normalizes each ROI timecourse first and leaves out the first 10\n    timepoints only from the t-tests. Under O6a the claim would not be reproduced.\n- claim: maturity-across\n  outcome: partially_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:maturity-across\n  measured: [-4.52, -3.55]\n  notes: Maturity on across, within, age and motion (n = 122). Across effect ToM t = -4.52, p =\n    1.5e-05; Pain t = -3.55, p = .00055; both negative and significant but out of tolerance under\n    every reading. Within-ToM t = 1.53, p = .13, not significant, as in the paper; within-Pain t =\n    2.40, p = .018, significant, where the paper has p = .06. z-scaled b across -.34 and -.28.\n- claim: maturity-within\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:maturity-within\n  notes: Within-network on maturity, age and motion. Main reading, maturity t = .83, p = .41\n    (ToM) and t = 1.80, p = .075 (Pain); age t = 2.39, p = .019 and t = 4.22, p = 4.9e-05.\n    Pain maturity p is .083 (O3b), .056 (O2b) and .040 (O2b, O3b).\n  deviations:\n  - Assumed O2a and O3a, as for irc-tom-behavior-age. Under O2b with O3b the Pain maturity effect\n    is significant and the claim would not be reproduced.\n- claim: maturity-tom-behavior\n  outcome: reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:maturity-tom-behavior\n  measured: 0.498\n  notes: Partial Spearman of ToM maturity with ToM score, motion as covariate, .498, p = 6.1e-09.\n    With age in the regression, ToM score t = .04, p = .97; age t = 4.46, p = 1.8e-05.\n- claim: maturity-fb\n  outcome: reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:maturity-fb\n  notes: Group effect with age and motion t = 1.53, p = .13 (failers .095, passers .168), not\n    significant.\n- claim: face-rc\n  outcome: not_reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:face-rc\n  measured: [0.818, 0.589, 10, 108, 32, 6]\n  notes: Children against adults r = .818 (p = 2.8e-39), in tolerance; 3yo r = .589 (p = 3.8e-16),\n    out of tolerance and above the paper's bound p < 1e-26. Under the rc-events reading (O5a,\n    O6b) 10 adult face events (108 s) and 6 3yo events (32 s); no reading gives 7 adult events\n    (8 to 10, 72 to 108 s). No face-event magnitude changes with age at .0071 (smallest p =\n    .010). The correlations do not both hold, so neither the reproduced nor the partial outcome of\n    the criterion applies.\n  deviations:\n  - The fusiform ROIs are the deposited rFFA (1019 voxels) and lFFA (531), the sizes of\n    Supplementary Table 2.\n  - Face-event peaks are the found adult events' peaks, as the paper gives no face peak TRs.\n- claim: face-overlap\n  outcome: reproduced\n  notebook: reproduce_richardson_2018.ipynb\n  output: claim:face-overlap\n  notes: Face events overlap ToM events by 7 TRs (p = .052 for fewer than chance) and pain events\n    by 25 TRs (p = .983) under the rc-events reading; .098 to .166 and .94 to .96 under the\n    others. Neither is below .05. The overlaps differ from the paper's 4 and 15 TRs.\n- claim: replication-sample\n  outcome: blocked\n  blocked_by: other\n  notes: The independent sample of 20 adults is not in the snapshot, and neither the paper nor the\n    dataset's README names an archive that holds it. The claims file marks the claim `elsewhere`\n    with no archive; as the data are public nowhere, data_missing would apply, which the checker\n    does not allow for an `elsewhere` claim.\n- claim: hand-coded-events\n  outcome: blocked\n  blocked_by: other\n  notes: The hand-coded events of Jacoby et al. 2016 are not in the snapshot (its README lists\n    only reverse-correlation events) or the paper. The Saxe lab web page\n    (https://saxelab.mit.edu/theory-mind-and-pain-matrix-localizer-movie-viewing-experiment)\n    offers the experiment script movloc.zip (version of 29 March 2019) whose mov_localizer.m holds\n    them, but with no DOI or repository commit, so it cannot be pinned as the protocol requires\n    for an outside input.\nfindings:\n- kind: other\n  statement: With the paper's own deposited preprocessed images, artifact and CompCor regressors\n    and ROI masks, and the pipeline of the Methods, the inter-region correlations differ from the\n    paper's, higher within networks and less negative across them (adults .604, .398 and -.051\n    against .48, .35 and -.17; 3yo within-ToM .326 against .21). Several downstream results\n    (within-ToM difference between false-belief passers and failers, age effects at event peaks,\n    the T04 effect of ToM score) do not come out as reported. Either the deposited data or the\n    described pipeline differs from what produced the paper's numbers.\n- kind: methods_unavailable\n  statement: For the authors, which timepoints entered the inter-region correlations (all 168 TRs,\n    or TRs 11 to 168 as in the reverse correlation), and whether the artifact timepoints were\n    regressed with one indicator each? irc-tom-behavior-age, irc-fb-across and maturity-within\n    change outcome with this choice; this attempt assumed all 168 TRs and one indicator each, as\n    in the deposited regressor files.\n- kind: methods_unavailable\n  statement: For the authors, over which timepoints was each ROI timecourse z-normalized before\n    the reverse correlation, and were child event magnitudes taken from the z-normalized\n    timecourse? rc-3yo-events depends on the first (all 168 TRs assumed) and rc-fb-no-difference\n    on the second (z-normalized assumed). The alpha of the reverse-correlation t-tests is also not\n    stated; p < .05 uncorrected matches Supplementary Table 3 best.\n- kind: methods_unavailable\n  statement: The analysis code is available only on request, and the high-pass filter\n    implementation (SPM discrete cosine assumed) is not stated.\n- kind: metadata_error\n  statement: participants.tsv lists 2 seven-year-olds and 21 8-12-year-olds with 3.13 mm voxels and\n    no slice gap, where the Methods say 3 and 20. The column is named \"Scanlog: Voxel slize\", and\n    the no-gap level is stored as an empty value where participants.json defines the level\n    \"None\".\n- kind: other\n  statement: 19 participants (14 aged 8-12, 2 adults, one each 4, 5 and 7 years) have face-ROI\n    voxels without data at some timepoint, where Supplementary Fig. 4 counts 17 with incomplete\n    ventral coverage (12 aged 8-12, 2 adults, one each 3, 4 and 7 years); the minimum of 101 voxels\n    with data agrees with its \"at least 100 voxels\". The coverage criterion may differ.\n- kind: other\n  statement: The independent sample of 20 adults that defined the ToM and pain ROIs and replicated\n    the events is not deposited anywhere; the ROIs it produced are in the dataset.\n"
}
```

```
File created successfully at: attempts/openneuro-ds000228-richardson-2018-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds000228-richardson-2018 && cat > README.md <<'EOF'
# Richardson, Lisandrelli, Riobueno-Naylor & Saxe (2018) from OpenNeuro ds000228

Tests the findings of [Richardson et al. (2018)](https://doi.org/10.1038/s41467-018-03399-2) on
[OpenNeuro ds000228](https://openneuro.org/datasets/ds000228/versions/1.1.1), snapshot 1.1.1,
which holds movie-viewing fMRI of 122 children aged 3 to 12 and 33 adults, with the paper's own
preprocessed images, artifact and CompCor regressors, group ROIs and behavioural scores.

| Claims | Outcome |
|---|---|
| Sample, behaviour and motion (11 claims) | Reproduced |
| Inter-region correlations (15 claims) | 8 partially reproduced, 7 not reproduced |
| Reverse correlation (8 claims) | 1 reproduced, 4 partially reproduced, 3 not reproduced |
| Functional maturity (4 claims) | 3 reproduced, 1 partially reproduced |
| Face regions (2 claims) | 1 reproduced, 1 not reproduced |
| Replication sample and hand-coded events (2 claims) | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Every behavioural number of the paper is recovered from participants.tsv. With the deposited
preprocessed data and the pipeline of the Methods, the inter-region correlations are higher within
networks and less negative across them than the paper reports, and several event-level and
false-belief results do not come out as reported. Four outcomes rest on readings of a method the
paper leaves open. The attempt record, with the reasons and the differences from the paper's
method, is
[`attempts/openneuro-ds000228-richardson-2018-01.yaml`](../../attempts/openneuro-ds000228-richardson-2018-01.yaml).

- `reproduce_richardson_2018.ipynb`: the analysis. It takes about five minutes, most of it
  streaming the 155 preprocessed images (14 GB).
- `social_brain.py`: loading from the pinned snapshot, ROI extraction, the timecourse cleaning
  of the Methods, inter-region correlation, reverse correlation and the statistics. Other
  notebooks on this dataset can import it.
EOF
cd  && python tools/entry.py check entries/openneuro-ds000228-richardson-2018 2>&1 | tail -20
```

```
error: attempts/openneuro-ds000228-richardson-2018-01.yaml: not valid YAML: mapping values are not allowed here
  in "<unicode string>", line 469, column 79:
     ... 20. The column is named "Scanlog: Voxel slize", and
                                         ^
1 error(s)
```

**Agent calls Bash**

```bash
sed -i 's/no slice gap, where the Methods say 3 and 20. The column is named "Scanlog: Voxel slize", and/no slice gap, where the Methods say 3 and 20. The voxel-size column name is misspelled ("Voxel slize"), and/' attempts/openneuro-ds000228-richardson-2018-01.yaml && sed -i 's/| Inter-region correlations (15 claims) | 8 partially reproduced, 7 not reproduced |/| Inter-region correlations (15 claims) | 7 partially reproduced, 8 not reproduced |/; s/Four outcomes rest on/Five outcomes rest on/' entries/openneuro-ds000228-richardson-2018/README.md && grep -n ': .*: ' attempts/openneuro-ds000228-richardson-2018-01.yaml | head; python tools/entry.py check entries/openneuro-ds000228-richardson-2018 2>&1 | tail -20
```

```
0 error(s)
```

**Agent calls Bash**

```bash
date -u; python tools/entry.py all entries/openneuro-ds000228-richardson-2018 2>&1 | tail -15; date -u
```

```
Wed Oct 28 16:38:49 UTC 2026
Installed kernelspec registry-openneuro-ds000228-richardson-2018 in executed/openneuro-ds000228-richardson-2018/.venv/share/jupyter/kernels/registry-openneuro-ds000228-richardson-2018
0 error(s)
pass  reproduce_richardson_2018.ipynb  (147 s)
Wed Oct 28 16:41:36 UTC 2026
```

**Agent calls Bash**

```bash
sed -i 's/runtime_minutes: 5/runtime_minutes: 3/' entries/openneuro-ds000228-richardson-2018/entry.yaml && sed -i 's/It takes about five minutes/It takes about three minutes/' entries/openneuro-ds000228-richardson-2018/README.md && python3 - <<'EOF'
import nbformat,re
nb=nbformat.read("executed/openneuro-ds000228-richardson-2018/reproduce_richardson_2018.ipynb",4)
txt="\n".join(o.get("text","") for c in nb.cells if c.cell_type=="code" for o in c.outputs if o.get("output_type")=="stream")
errs=[o for c in nb.cells if c.cell_type=="code" for o in c.outputs if o.get("output_type")=="error"]
print("errors",len(errs))
dev=open("/tmp/claude-1001/out3.txt").read()
# compare numeric tokens of lines starting with key phrases
keys=["Welch t","partial tau","best-matching","in tolerance:","events passing","children (n = 122)","3yo (n = 17)","partial Spearman(ToM","regression: ToM","FB group (fail = 1): b raw","overlapping TRs","smallest p per reading","isolated artifact timepoints shifted by   0"]
for k in keys:
    a=[l for l in txt.split("\n") if k in l]; b=[l for l in dev.split("\n") if k in l]
    print(k, "SAME" if a==b else ("DIFF", a[:2], b[:2]))
EOF
```

```
errors 0
Welch t SAME
partial tau SAME
best-matching SAME
in tolerance: SAME
events passing SAME
children (n = 122) SAME
3yo (n = 17) SAME
partial Spearman(ToM SAME
regression: ToM SAME
FB group (fail = 1): b raw SAME
overlapping TRs SAME
smallest p per reading SAME
isolated artifact timepoints shifted by   0 SAME
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import nbformat,re
nb=nbformat.read("executed/openneuro-ds000228-richardson-2018/reproduce_richardson_2018.ipynb",4)
ex=[l for c in nb.cells if c.cell_type=="code" for o in c.outputs if o.get("output_type")=="stream" for l in o.get("text","").split("\n")]
dev=[l for l in open("/tmp/claude-1001/out3.txt").read().split("\n") if not l.startswith("-----") and not re.match(r"^\s+\[\d+\.\ds\]$",l)]
s=set(dev); miss=[l for l in ex if l not in s and l.strip()]
print(len(ex), len(miss)); print("\n".join(miss[:15]))
EOF
```

```
1248 2
/tmp/claude-1001/ipykernel_40/1048283978.py:11: Pandas4Warning: The 'lsuffix' and 'rsuffix' keywords in DataFrame.join are deprecated and will be removed in a future version. Use the 'suffixes' keyword instead.
  print(age_ev.pivot(index="event", columns="reading", values="rs").round(3).join(
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/openneuro-ds000228-richardson-2018 2>&1 | tail -3 && python tools/entry.py handover entries/openneuro-ds000228-richardson-2018 2>&1 | tail -5; ls executed/openneuro-ds000228-richardson-2018/handover; git status --short; date -u
```

```
0 error(s)
wrote executed/openneuro-ds000228-richardson-2018/handover
10.1038-s41467-018-03399-2.yaml
reproduce_richardson_2018.ipynb
social_brain.py
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
?? attempts/openneuro-ds000228-richardson-2018-01.yaml
?? entries/openneuro-ds000228-richardson-2018/
?? scripts
Wed Oct 28 16:42:13 UTC 2026
```

**Agent**

The attempt is written and its checks pass. Of 42 claims, 15 are reproduced, 12 partially reproduced, 13 not reproduced and 2 blocked. `entry.py check` reports 0 errors, the notebook ran clean in 147 s (`entry.py all`: pass), its outputs match my development run line for line, and the handover is built in `executed/openneuro-ds000228-richardson-2018/handover/`. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| participants, supp-table1-behavior-by-age, beh-tom-age, beh-tom-dccs, beh-fb-groups, beh-fb-tom, beh-fb-age, beh-fb-dccs | reproduced |
| motion-child-adult, motion-not-age-tom, motion-not-fb | reproduced |
| irc-adult, irc-adult-vs-child, irc-control-networks, irc-williams, irc-3yo-not-anticorrelated, irc-3yo-nonbilateral, irc-tom-behavior | partially reproduced |
| irc-age-within, irc-age-across, irc-3yo-distinct | not reproduced (by Rule S: the effects are significant at .05 but miss the paper's p bounds, and the values are out of tolerance) |
| irc-3yo-homologous, irc-fb-within, irc-fb-within-dccs | not reproduced |
| irc-tom-behavior-age, irc-fb-across | not reproduced, resting on an assumption |
| rc-events, rc-overlap, rc-child-adult-timecourse, maturity-across | partially reproduced |
| rc-3yo-events | partially reproduced, resting on an assumption |
| supp-table4-other-networks, rc-age-events, rc-t04-tom, face-rc | not reproduced |
| rc-fb-no-difference, maturity-within | reproduced, resting on an assumption |
| maturity-tom-behavior, maturity-fb, face-overlap | reproduced |
| replication-sample, hand-coded-events | blocked (`other`) |

**2. The dataset**

- **What it holds.** Snapshot 1.1.1 holds the paper's own preprocessed images (`*_swrf_bold`), the artifact and CompCor regressors, and every ROI mask, including the face, scene, M1 and V1 regions. The masks have the sizes of Supplementary Table 2. I pinned 1.1.1 because the claims file names it, it is the latest snapshot, and its CHANGES file says it only updated the citation.
- **What matches.** Every behavioural number is recovered exactly from participants.tsv. The artifact counts match the Methods, and the artifact flags line up in time with spikes in the image data.
- **Main finding.** With the paper's preprocessed data and the pipeline the Methods describe, the inter-region correlations come out higher within networks and less negative across them. In adults they are .604, .398 and -.051 against the paper's .48, .35 and -.17. Several event-level and false-belief results do not come out as reported.
- **Minor metadata problems.**
  - The voxel-size counts by age group differ from the Methods (2 and 21 participants against 3 and 20).
  - The column is misspelled "Voxel slize".
  - The "None" slice-gap level is stored as an empty value.
  - 19 participants have incomplete face-ROI coverage, where Supplementary Fig. 4 counts 17.
- **Assumptions**, each recorded as a deviation and asked of the paper's authors as a `methods_unavailable` finding:
  - The inter-region correlations use all 168 TRs and one regressor per artifact timepoint, as in the deposited files.
  - The z-normalization spans all 168 TRs.
  - Child event magnitudes come from the z-normalized timecourse.
  - The high-pass filter is SPM's cosine filter.
- **Questions to a reader:** none.

**3. Where the protocol was unclear, wrong or missing something**

1. replication-sample is marked `data: elsewhere` with no archive, because the sample is public nowhere. The protocol would block it as `data_missing`, but the checker rejects that reason for `elsewhere` claims. I used `other` and explained in the notes.
2. The Jacoby et al. hand coding exists only in a zip on the Saxe lab website, with no DOI or commit. The protocol has no block reason for "public but cannot be pinned", so I used `other`.
3. The claims file treats the face and scene parcels as outside input, but the dataset holds them. I used the deposited copies, recorded that as a deviation, and left the claims' `data: with_inputs` unchanged since I may not edit claims.
4. Rule S counts a test that misses the paper's p bound as a failed test, even when the effect is significant in the same direction. This turned three claims into "not reproduced". I applied it as written and gave the effect sizes in the notes.
5. Several criteria (irc-williams, face-rc) define only the "reproduced" outcome. For irc-williams I used `partially_reproduced` for an effect that holds in part, under the protocol's general definition.
6. The data-check rule assumes trial tables, and this movie study has none. I checked timing in two ways: the ROI signal spikes at isolated artifact timepoints against shifted ones (6.45 against at most 2.6), and the ToM-against-pain event contrast falls when the event labels are shifted.
7. Readings that change an absence claim's outcome fall between two rules: "absence is judged on the paper's test alone" and author step 1.6. I followed step 1.6 and marked those outcomes as resting on an assumption.

**4. Runtime and failures**

The whole run took about 32 minutes (16:10 to 16:42 UTC). Extracting the ROIs takes about 95 s and the notebook 147 s in total. Nothing failed. The one notebook warning is a pandas deprecation notice. Untracked dotfiles (`.bashrc`, `.gitconfig`, `.idea`, `scripts` and others) appeared at the repository root. I did not create them on purpose and left them in place; they should not go into the commit.

Sources: [Saxe lab localizer page](https://saxelab.mit.edu/theory-mind-and-pain-matrix-localizer-movie-viewing-experiment), [Jacoby et al. 2016](https://www.sciencedirect.com/science/article/abs/pii/S1053811915010472)

## End of run

68 turns, 28 minutes, result: success.
