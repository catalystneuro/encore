# crcns-stc-1 · author · run 42256343726

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls claims/crcns-stc-1 paper entries | head -50
```

```
<persisted-output>
Output too large (36.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/eb26ca24-e32c-4e3b-add1-d9937a4baad3/tool-results/bgmvru06y.txt

Preview (first 2KB):
Fri Nov  6 16:55:04 UTC 2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/eb26ca24-e32c-4e3b-add1-d9937a4baad3/tool-results/bgmvru06y.txt"
}
```

```
1	Fri Nov  6 16:55:04 UTC 2026
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
[... 672 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/crcns-stc-1/*.yaml; ls paper; cat paper/stc-1.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/eb26ca24-e32c-4e3b-add1-d9937a4baad3/tool-results/bqzkzhj1o.txt"
}
```

```
1	# Claims for Gu, Liu, Fetsch, Yang, Fok, Sunkara, DeAngelis & Angelaki (2011), Neuron 71:750-761,
2	# "Perceptual Learning Reduces Interneuronal Correlations in Macaque Visual Cortex", on CRCNS data
3	# set stc-1 (doi:10.6080/K07P8WKF).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
5	# protocol as stated in docs/protocol.md (Reader).
6	#
7	# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF),
8	# with its Results, Discussion, Experimental Procedures and the legends of Figures 1 to 8, and
9	# the Supplemental Information PDF (legends of Figures S1 to S8). The article says the
10	# Supplemental Information "includes Experimental Procedures and eight figures"; the supplement
11	# as supplied, whose own contents page lists only the eight figures, holds no further
12	# procedures, so the Experimental Procedures of the article are taken as the whole Methods.
13	# The PDF could not be rendered here; the extracted text prints degree signs, minus signs and
14	# "approximately" as a replacement character, and quotes avoid those places. The paper links no
15	# analysis code, so none was read.
16	#
17	# Data the paper used. Eight male rhesus monkeys (Macaca mulatta): three "naive" animals trained
18	# only to fixate, and five "trained" animals extensively trained in a vestibular and visual
19	# heading discrimination task (left or right of straight ahead) before recording. Pairs of
20	# single units recorded simultaneously in area MSTd while the animals fixated passively and
[... 1002 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/eb26ca24-e32c-4e3b-add1-d9937a4baad3/tool-results/bqzkzhj1o.txt",
 "offset": 1023
}
```

```
1023	 
1024	Inferring decoding strategies for multiple correlated neural populations 
1025	Kaushik Lakshminarasimhan, Alexandre Pouget, Gregory DeAngelis, Dora Angelaki, 
1026	Xaq Pitkow.  bioRxiv doi: 10.1101/108019 
1027	 
1028	 
1029	Conditions for using the data 
1030	There are no restrictions. You’re free to use these data and publish your findings. 
1031	Depending on the subset of the data you use for publication, please cite one of the 
1032	above papers as you see fit. Please also cite the data set using the following: 
1033	 
1034	Yong Gu, Aihua Chen, Sheng Liu, Christopher Fetsch, Yang Y, Adhira Sunkara, 
1035	Kaushik J Lakshminarasimhan, Xaq Pitkow, Gregory DeAngelis, Dora Angelaki (2018); 
1036	Extracellular recordings from areas MSTd and VIP of macaque monkeys during a 
1037	heading discrimination task.  CRCNS.org. 
1038	http://dx.doi.org/10.6080/K07P8WKF 
1039	 
1040	
1041	Page 3 of 5 
1042	Methods 
[... 178 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/CRCNS/,/^## [A-Z]/p' docs/archives.md | head -150; ls entries/001453-fouke-2025 claims/001453;
```

```
## CRCNS

- **Datasets.** A CRCNS data set, identified by its short name (`ret-1`,
  `hc-3`), with a DOI of its own (`10.6080/...`). The registry's list is
  `targets/crcns.json`, written by hand; for now it holds one data set, to test
  the pipeline beyond DANDI.
- **Versions.** CRCNS data sets are not versioned. Record the version as
  `unversioned`, with the data set's DOI under `dataset: doi`, and give in the
  notebook header the MD5 sums from the data set's `checksums.md5` for the
  files read, so a later change is detectable.
- **Reading.** The files are in the public S3 bucket `crcnsarchive` (region
  us-west-2), under `<id>/`, readable without an account at
  `https://crcnsarchive.s3-us-west-2.amazonaws.com/<id>/<file>`; list a data
  set with `?list-type=2&prefix=<id>/` on the bucket's address. The site
  crcns.org asks for a login to download; the bucket does not. Most data sets
  are zip files of MATLAB or other files: open the zip in place with
  `fsspec.open(url, block_size=2**20).open()` and Python's `zipfile`, which
  read only the parts needed over range requests (`remfile` lacks what
  `zipfile` needs to read a member), and load members in memory
  (`scipy.io.loadmat`, or `h5py` for MATLAB 7.3 files). Do not download whole
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml README.md requirements.in; head -80 omr.py; python -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:12]: print(c['cell_type'],c.get('metadata'),'\n',''.join(c['source'])[:1500],'\n-----')
"
```

```
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
- id: doi:10.1016/j.cub.2025.04.027
[... 331 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/001453-fouke-2025-01.yaml | head -200; ls questions | head; ls transcripts | head -3
```

```
cat: attempts/001453-fouke-2025-01.yaml: No such file or directory
ls: cannot access 'questions': No such file or directory
ls: cannot access 'transcripts': No such file or directory
```

**Agent calls Bash**

```bash
cd  cat attempts/001453-fouke-2025-01.yaml | head -150; ls questions | head -3
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
[... 133 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '150,400p' attempts/001453-fouke-2025-01.yaml | grep -v "^    " | head -80; grep -n "blocked_by\|findings:\|kind:\|assumed" attempts/001453-fouke-2025-01.yaml | head -30; cat questions/000005.yaml | head -30
```

```
notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1h-zf-higher-angular-acceleration
  notes: With angular acceleration as the Methods define it, DC are higher than ZF for all nine
  deviations:
  - Follows the Methods' definition (degrees per second squared) on heading resampled to 30 Hz;
  - Heading is taken from the cumulative sum of `f0_vtheta`, as the code does; in DC files it does
- claim: figs1e-dc-respond-less-monocular
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:figs1e-dc-respond-less-monocular
  notes: Species effect F = 23.3, p = 2.5e-06. DC turn less toward the stimulus than ZF for
  deviations:
  - Codes 9 and 11 are assigned as the figure code has them; the stimulus software's conversion
- claim: fig1c-continuous-vs-bouts
  outcome: reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1c-continuous-vs-bouts
  notes: The median-to-mean ratio of instantaneous speed is 0.306 in ZF (25 fish, 0.244 to 0.580)
  deviations:
  - The paper shows this with representative traces and a bout analysis whose bout files are not
[... 119 more lines not kept]
```

**Agent**

Now list the dataset in the bucket.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=stc-1/" | python -c "
import sys,re; t=sys.stdin.read(); 
for k,s,m in re.findall(r'<Key>(.*?)</Key>.*?<LastModified>(.*?)</LastModified>.*?<Size>(.*?)</Size>',t): print(k,s,m)
print(re.findall('IsTruncated>(.*?)<',t))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://crcnsarchive.s3-us-west-2.amazonaws.com/stc-1/live; curl -s $B/checksums.md5; curl -s $B/filelist.txt; curl -s $B/demo.m; python -c "import scipy,fsspec,numpy;print(scipy.__version__)"
```

```
Exit code 1
39b69d14e7663f8c2280b1c26f1da74f  demo.m
df7412a2c15374bae17e46030e4d393c  docs/crcns_stc-1_data_description.docx
4c7b31c0ba81b3633dcb7efe8525519e  docs/crcns_stc-1_data_description.pdf
fa0527d8ebc46a5b43ddf32c876a7cd4  filelist.txt
cd4c13b360aa05689015f1bd2b88a05a  MSTd.mat
8d7924e0a1ae86c56b78cd1e2f530e2d  VIP.mat
# CRCNS.org 'stc-1' dataset files
# To use this for fetching files, comment out files that are
# not needed by putting a '#' as the first character on the line (default mode)
# or put a '+' as the first character to specifiy files to be fetched (+ mode).
# mode='default' (change to '+' for + mode).
 demo.m	2746 (2.6 KB)
 docs/crcns_stc-1_data_description.docx	38584 (37.6 KB)
 docs/crcns_stc-1_data_description.pdf	108958 (106.4 KB)
 MSTd.mat	65358 (63.8 KB)
 VIP.mat	45545 (44.4 KB)
 checksums.md5	318
load VIP.mat;

[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q scratch && . scratch/bin/activate && uv pip install -q scipy numpy fsspec aiohttp requests pandas statsmodels matplotlib && python - <<'EOF'
import fsspec, io, scipy.io as sio, numpy as np
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/stc-1/live/MSTd.mat"
with fsspec.open(url,"rb") as f: b=f.read()
import hashlib; print(hashlib.md5(b).hexdigest())
m=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)
print([k for k in m if not k.startswith('__')], m['__header__'])
for e in ['experiment1','experiment2','experiment3']:
    x=m[e]; print(e, x._fieldnames, getattr(x,'name',None))
p=m['experiment3'].pairs; print(len(p)); print(p[0]._fieldnames)
for i in range(3):
    q=p[i]; print(q.file_id, q.heading_pref, q.ves._fieldnames, q.ves.corr_signal, q.ves.corr_noise, q.vis.corr_signal, q.vis.corr_noise)
u=m['experiment1'].units; print(len(u), u[0]._fieldnames, u[0].ves._fieldnames, u[0].file_id)
u2=m['experiment2']; print(u2._fieldnames, len(u2.units), u2.units[0]._fieldnames, u2.units[0].ves._fieldnames)
print(u2.behv._fieldnames if hasattr(u2,'behv') else None)
EOF
```

```
Exit code 1
cd4c13b360aa05689015f1bd2b88a05a
['experiment1', 'experiment2', 'experiment3'] b'MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Thu Aug 30 10:12:39 2018'
experiment1 ['name', 'units'] passive heading
experiment2 ['name', 'units', 'behv'] heading discrimination
experiment3 ['name', 'pairs'] passive heading: pairwise recordings
127
['file_id', 'ves', 'vis']
Traceback (most recent call last):
  File "<stdin>", line 11, in <module>
AttributeError: 'mat_struct' object has no attribute 'heading_pref'
```

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && python - <<'EOF'
import fsspec, io, scipy.io as sio, numpy as np, collections
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/stc-1/live/MSTd.mat"
with fsspec.open(url,"rb") as f: b=f.read()
m=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)
p=m['experiment3'].pairs
for i in range(4):
    q=p[i]; print(repr(q.file_id), q.ves._fieldnames, [(k,getattr(q.ves,k)) for k in q.ves._fieldnames],[(k,getattr(q.vis,k)) for k in q.vis._fieldnames])
ids=[q.file_id for q in p]; print(ids)
u=m['experiment1'].units; print(len(u), u[0]._fieldnames, u[0].ves._fieldnames, repr(u[0].file_id), u[0].ves.stim_global, u[0].ves.resp_global)
e2=m['experiment2']; print(len(e2.units), e2.units[0]._fieldnames, e2.units[0].ves._fieldnames, e2.units[0].ves.stim_local, e2.units[0].ves.resp_local, e2.units[0].ves.cp, e2.units[0].ves.thresh, e2.units[0].file_id)
bh=e2.behv; print(type(bh), getattr(bh,'_fieldnames',None))
s=bh.subj if hasattr(bh,'subj') else bh
print(s if not hasattr(s,'__len__') else [(x.monk_id, x._fieldnames, x.ves._fieldnames) for x in np.atleast_1d(s)])
x=np.atleast_1d(s)[0]; print(x.ves.thresh, x.vis.thresh)
EOF
```

```
'm17c26r1' ['heading_pref', 'corr_signal', 'corr_noise'] [('heading_pref', array([  31.3781, -104.8791])), ('corr_signal', -0.431), ('corr_noise', 0.018)] [('heading_pref', array([  61.1839, -126.411 ])), ('corr_signal', -0.146), ('corr_noise', -0.203)]
'm17c28r1' ['heading_pref', 'corr_signal', 'corr_noise'] [('heading_pref', array([16.5134, 43.9667])), ('corr_signal', 0.412), ('corr_noise', -0.083)] [('heading_pref', array([-149.2214, -174.5574])), ('corr_signal', 0.816), ('corr_noise', -0.036)]
'm17c29r1' ['heading_pref', 'corr_signal', 'corr_noise'] [('heading_pref', array([68.9056, 78.5066])), ('corr_signal', 0.589), ('corr_noise', 0.106)] [('heading_pref', array([-117.4303,   46.5595])), ('corr_signal', 0.22), ('corr_noise', -0.111)]
'm17c30r1' ['heading_pref', 'corr_signal', 'corr_noise'] [('heading_pref', array([88.4037, 98.0819])), ('corr_signal', 0.721), ('corr_noise', 0.058)] [('heading_pref', array([ 163.9445, -119.3287])), ('corr_signal', 0.11), ('corr_noise', 0.16)]
['m17c26r1', 'm17c28r1', 'm17c29r1', 'm17c30r1', 'm17c31r3', 'm17c35r1', 'm17c36r1s', 'm17c39r2', 'm17c39r2', 'm17c39r2', 'm17c40r1s', 'm17c40r1s', 'm17c40r1s', 'm17c41r1s', 'm17c41r1s', 'm17c41r1s', 'm17c41r4', 'm17c41r4', 'm17c41r4', 'm17c42r1s', 'm17c44r1s', 'm17c48r1s', 'm18c101r1', 'm18c101r3', 'm18c103r1', 'm18c104r1', 'm18c107r1', 'm18c108r2', 'm18c109r1', 'm18c109r3', 'm18c110r1', 'm18c111r1', 'm18c112r1', 'm18c113r1', 'm18c114r1', 'm18c115r1', 'm18c118r2', 'm18c118r2', 'm18c118r2', 'm18c119r2', 'm18c119r2', 'm18c119r2', 'm18c121r1', 'm18c123r1', 'm18c125r1', 'm18c126r1', 'm18c127r1', 'm3c236r1', 'm3c295r1', 'm3c297r1', 'm3c304r1', 'm3c321r3', 'm1c108r1', 'm1c198r1', 'm1c203r1', 'm1c225r1', 'm1c238r1', 'm1c255r1', 'm1c278r1', 'm1c291r1', 'm1c445r1', 'm1c456r1', 'm1c531r1', 'm2c66r1', 'm2c76r1', 'm2c77r1', 'm2c95r1', 'm2c148r1', 'm2c170r1', 'm2c183r1', 'm2c193r1', 'm2c218r1', 'm2c232r1', 'm2c338r1', 'm2c342r3', 'm2c348r1', 'm2c370r1', 'm2c417r1', 'm2c430r1', 'm2c452r1', 'm2c457r1', '
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c paper/*.txt; grep -n "Experimental Procedures\|EXPERIMENTAL PROCEDURES\|Population Coding\|Noise and Signal\|Permutation" paper/10.1016-j.neuron.2011.06.015.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2011.06.015.txt",
 "limit": 640,
 "offset": 60
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2011.06.015.txt",
 "offset": 798,
 "limit": 195
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && python - <<'EOF'
import fsspec, io, scipy.io as sio, numpy as np, pandas as pd, re
from scipy import stats
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/stc-1/live/MSTd.mat"
with fsspec.open(url,"rb") as f: b=f.read()
m=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)
rows=[]
for i,q in enumerate(m['experiment3'].pairs):
    rows.append(dict(i=i,fid=q.file_id,monk=int(re.match(r'm(\d+)c',q.file_id).group(1)),
      sv=q.ves.corr_signal,nv=q.ves.corr_noise,sV=q.vis.corr_signal,nV=q.vis.corr_noise,
      pv1=q.ves.heading_pref[0],pv2=q.ves.heading_pref[1],pV1=q.vis.heading_pref[0],pV2=q.vis.heading_pref[1]))
d=pd.DataFrame(rows)
print(d.monk.value_counts())
print(d.describe().T)
print(d.isna().sum().sum())
d['s']=d.fid.str.endswith('s'); print(d.groupby('monk').s.sum())
# duplicates
print(d[d.duplicated(['sv','nv','sV','nV'],keep=False)])
naive={17,1,3}; d['naive']=d.monk.isin(naive)
d['pool']=(d.nv+d.nV)/2
for c in ['nv','nV','pool']:
    a,b_=d[~d.naive][c],d[d.naive][c]
    print(c,'trained',a.mean().round(4),a.sem().round(4),len(a),'naive',b_.mean().round(4),b_.sem().round(4),len(b_),stats.ttest_ind(a,b_).pvalue,stats.ttest_ind(a,b_,equal_var=False).pvalue)
print(d.groupby('monk')[['nv','nV','pool']].mean())
print(stats.spearmanr(d.nv,d.nV), stats.ttest_rel(d.nv,d.nV), d.nv.mean(),d.nV.mean())
# example pair
print(d[(abs(d.sV-0.83)<0.1)&(abs(d.sv-0.79)<0.1)])
# overlap exp1
e1=[u.file_id for u in m['experiment1'].units]; e2=[u.file_id for u in m['experiment2'].units]
print(set(e1)&set(d.fid), e1[:5], e2[:5])
print(sorted(d.fid.str.extract(r'(m\d+c\d+)')[0]) [:5], set(x[:x.index('r')] for x in e1)&set(x[:x.index('r')] for x in d.fid))
# rsignal check: heading pref vs rsignal
EOF
```

```
monk
19    35
18    26
17    22
2     18
1     11
5      8
3      5
24     2
Name: count, dtype: int64
      count       mean         std  ...      50%        75%       max
i     127.0  63.000000   36.805797  ...  63.0000   94.50000  126.0000
monk  127.0  13.047244    7.599977  ...  17.0000   19.00000   24.0000
sv    127.0   0.109439    0.443536  ...   0.1570    0.47700    0.9050
nv    127.0   0.055878    0.194839  ...   0.0580    0.16700    0.5440
sV    127.0   0.167391    0.495205  ...   0.1930    0.54225    0.9660
nV    127.0   0.049072    0.224104  ...   0.0350    0.19250    0.6805
pv1   127.0  -3.488750   99.249417  ...  -4.1132   82.47230  176.2635
pv2   127.0  20.680002  105.519534  ...  42.8315  103.44055  175.6508
pV1   127.0  13.045508  102.242297  ...  18.4890  104.29905  178.7051
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . scratch/bin/activate && python - <<'EOF'
import fsspec, io, scipy.io as sio, numpy as np, pandas as pd, re
def load(n):
    with fsspec.open(f"https://crcnsarchive.s3-us-west-2.amazonaws.com/stc-1/live/{n}.mat","rb") as f: b=f.read()
    return sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)
m=load('MSTd'); v=load('VIP')
p=m['experiment3'].pairs
from collections import defaultdict
g=defaultdict(list)
for q in p: g[q.file_id].append(q)
for k,qs in g.items():
    if len(qs)>1:
        prefs=[tuple(np.round(q.vis.heading_pref,2)) for q in qs]
        print(k,len(qs),prefs)
vp=v['experiment3'].pairs; print(len(vp), set(q.file_id for q in vp)&set(q.file_id for q in p))
e1=m['experiment1'].units;e2=m['experiment2'].units
print(all(a.file_id.split('r')[0]==b.file_id.split('r')[0] for a,b in zip(e1,e2)))
print(collections:=None)
print(sorted(set(re.match(r'm(\d+)',u.file_id).group(1) for u in e1)))
print([ (s.monk_id, s.ves.thresh, s.vis.thresh) for s in m['experiment2'].behv.subj])
print(e1[0].vis.stim_global, len(set(len(u.ves.resp_global) for u in e1)))
print(set(tuple(u.ves.stim_global) for u in e1))
EOF
```

```
Fri Nov  6 16:57:49 UTC 2026
m17c39r2 3 [(np.float64(-67.22), np.float64(65.04)), (np.float64(-67.22), np.float64(-17.76)), (np.float64(65.04), np.float64(-17.76))]
m17c40r1s 3 [(np.float64(4.11), np.float64(135.6)), (np.float64(4.11), np.float64(-140.38)), (np.float64(135.6), np.float64(-140.38))]
m17c41r1s 3 [(np.float64(112.22), np.float64(76.99)), (np.float64(112.22), np.float64(-19.84)), (np.float64(76.99), np.float64(-19.84))]
m17c41r4 3 [(np.float64(-161.36), np.float64(53.96)), (np.float64(-161.36), np.float64(-137.6)), (np.float64(53.96), np.float64(-137.6))]
m18c118r2 3 [(np.float64(140.62), np.float64(-156.99)), (np.float64(140.62), np.float64(158.05)), (np.float64(-156.99), np.float64(158.05))]
m18c119r2 3 [(np.float64(-76.64), np.float64(43.23)), (np.float64(-76.64), np.float64(-99.96)), (np.float64(43.23), np.float64(-99.96))]
m5c62r6 3 [(np.float64(-38.12), np.float64(-111.0)), (np.float64(-38.12), np.float64(-79.3)), (np.float64(-111.0), np.float64(-79.3))]
m19c16r1 3 [(np.float64(94.72), np.float64(-66.96)), (np.float64(94.72), np.float64(-64.23)), (np.float64(-66.96), np.float64(-64.23))]
m19c20r1 3 [(np.float64(96.17), np.float64(0.78)), (np.float64(96.17), np.float64(-111.24)), (np.float64(0.78), np.float64(-111.24))]
m19c21r1 6 [(np.float64(136.94), np.float64(144.61)), (np.float64(136.94), np.float64(-24.91)), (np.float64(136.94), np.float64(137.9)), (np.float64(144.61), np.float64(-24.91)), (np.float64(144.61), np.float64(137.9)), (np.float64(-24.91), np.float64(137.9))]
m19c23r1 3 [(np.float64(29.39), np.float64(-61.64)), (np.float64(29.39), np.float64(-19.87)), (np.float64(-61.64), np.float64(-19.87))]
m19c233r1 3 [(np.float64(174.78), np.float64(172.56)), (np.float64(174.78), np.float64(-177.65)), (np.float64(172.56), np.float64(-177.65))]
m19c236r1 3 [(np.float64(-173.17), np.float64(146.82)), (np.float64(-173.17), np.float64(-108.95)), (np.float64(146.82), np.float64(-108.95))]
139 set()
True
None
['2', '5']
[('2', <scipy.io.matlab._mio5_
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas tools; python tools/entry.py --help 2>&1 | head -30; grep -n "def cmd_\|def check" tools/entry.py | head -40
```

```
schemas:
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json

tools:
__pycache__
agent_run.py
archive_transcripts.sh
archives
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_site.py
build_targets.py
claims_check.py
conversion_issue.py
datasets.py
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=0)[:9000])"; sed -n 143,330p tools/entry.py | grep -n "crcns\|version\|names the dataset\|related"
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
[... 465 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));c=s['properties']['claims']['items'];print(list(c['properties']));print(json.dumps(c['properties'].get('kind'),indent=0));print(json.dumps(c['properties'].get('data'),indent=0)[:1500]); print(c.get('required'))"; grep -rn "kind: link" claims | head -3
```

```
['id', 'statement', 'source', 'kind', 'quote', 'inferred', 'expected', 'statistics', 'criterion', 'depends_on', 'data', 'where']
{
"description": "A finding the paper reports (`finding`, the default), or a check the registry adds that the dataset is the data the paper's outside material describes (`link`: the paper's tables, source data, code or deposits). Links are not findings of the paper and are counted apart from them.",
"enum": [
"finding",
"link"
]
}
{
"description": "What the claim's test uses: the dataset alone (`dataset`, the default); the dataset with names for its own codes taken from elsewhere (`with_labels`), which counts as the dataset; the dataset with other data from elsewhere (`with_inputs`), which is counted apart; or data the paper deposited in another public archive, which the dataset does not hold (`elsewhere`), counted apart from both. Outside sources that a test uses are listed under `inputs` in the attempt.",
"enum": [
"dataset",
"with_labels",
"with_inputs",
"elsewhere"
]
}
['id', 'statement', 'source']
claims/001933/10.1038-s41467-026-75194-3.yaml:70:  kind: link
claims/000045/10.7554-elife.63711.yaml:707:  kind: link
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 60,100p claims/001933/10.1038-s41467-026-75194-3.yaml
```

```
# difference of the WT and G2019S means over the pooled standard deviation.
# Quotes and statistics added 2026-10-19 from the full text (Europe PMC PMC13522591; Supplementary
# Figure 7 and 8 legends from its Supplementary Information PDF, 41467_2026_75194_MOESM1_ESM.pdf).
schema_version: 2
dataset:
  archive: dandi
  id: "001933"
paper: doi:10.1038/s41467-026-75194-3
claims:
- id: source-data-link
  kind: link
  statement: The dandiset's recordings are those behind the paper's Figure 6 and Supplementary
    Figures 7 and 8, and the paper's published per-stimulation traces, evoked integrals and
    spontaneous transient integrals can be recomputed from them.
  source: Figure 6C to 6F, Supplementary Figures 7B, 7C, 8C to 8E; Source Data (Zenodo
    10.5281/zenodo.19930567); Data availability
  quote: Raw tubular Data generated in this study from all experiments, and uncropped western blot
    images with metadata files in this study are available in source data file via the open-access
    option on the Zenodo repository (https://doi.org/10.5281/zenodo.19930567).
  data: with_inputs
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "35\b.*26\|22, 11\|n = 35\|individual animals" paper/*.txt | head; ls paper; python -c "
import fitz" 2>&1; pdftotext -v 2>&1 | head -1
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2011.06.015.txt",
 "offset": 1190,
 "limit": 160
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && cat > sim.py <<'EOF'
import numpy as np, time
from scipy.optimize import brentq
def wg(theta, pref, sigma):
    d = np.deg2rad(theta - pref)
    k = np.arange(-3, 4)
    return np.exp(-((d[..., None] + 2*np.pi*k) ** 2) / (2*np.deg2rad(sigma)**2)).sum(-1)
def sigma_for_fwhm(fwhm):
    def half(s):
        g = wg(np.array([0.0, fwhm/2, 180.0]), 0.0, s)
        return (g[1]-g[2])/(g[0]-g[2]) - 0.5
    return brentq(half, 5, 200)
SIG = sigma_for_fwhm(135)
def tuning(prefs, theta, A=30., b=10.):
    return b + A*wg(np.asarray(theta)[None, :] if np.ndim(theta) else np.array([theta])[None,:], np.asarray(prefs)[:, None], SIG)
def rsig(prefs, headings):
    F = tuning(prefs, headings)
    return np.corrcoef(F)
def threshold(prefs, slope, intercept, headings, A=30., b=10., trace=True):
    prefs = np.asarray(prefs, float)
    f = tuning(prefs, 0.0, A, b)[:, 0]
    h = 1e-3
    fp = (tuning(prefs, h, A, b)[:, 0] - tuning(prefs, -h, A, b)[:, 0]) / (2*h)
    if slope == 0 and intercept == 0:
        R = np.eye(len(prefs))
    else:
        R = slope*rsig(prefs, headings) + intercept
        np.fill_diagonal(R, 1.0)
    s = np.sqrt(f)
    Q = R * np.outer(s, s)
    Qp = R * (np.outer(fp, f) + np.outer(f, fp)) / (2*np.outer(s, s))
    Qi = np.linalg.inv(Q)
    I = fp @ Qi @ fp
    if trace:
        M = Qp @ Qi
        I += 0.5*np.sum(M * M.T)
    return np.sqrt(2)/np.sqrt(I)
EOF
python - <<'EOF'
import numpy as np, time
from sim import *
print(SIG)
H8 = np.arange(0,360,45.); Hc=np.arange(0,360,1.)
for H,name in [(H8,'8'),(Hc,'cont')]:
  for N in [256, 2000]:
    prefs = np.linspace(-180,180,N,endpoint=False)
    t=time.time()
    ind=threshold(prefs,0,0,H); nv=threshold(prefs,0.211,0.072,H); tr=threshold(prefs,0.211,0.005,H)
    ind2=threshold(prefs,0,0,H,trace=False); nv2=threshold(prefs,0.211,0.072,H,trace=False); tr2=threshold(prefs,0.211,0.005,H,trace=False)
    print(name,N, ind,nv,tr, nv/ind, tr/nv, '| no trace', nv2/ind2, tr2/nv2, time.time()-t)
EOF
```

```
58.00615461132711
8 256 2.2004997192544185 7.216687923534262 7.251277745608927 3.2795677547186632 1.0047930328207577 | no trace 3.7373134901752834 1.0095497665413937 0.09976506233215332
8 2000 0.7872747130760265 4.258100052308653 4.257995752495407 5.408658479162218 0.9999755055513104 | no trace 9.177337960080271 1.0033721795282085 2.626394033432007
cont 256 2.2004997192544185 7.216687919445979 7.251277742127707 3.2795677528607747 1.0047930329075923 | no trace 3.7373134874006166 1.0095497666507849 0.06084036827087402
cont 2000 0.7872747130760265 4.258100004658492 4.257995712304418 5.4086584186367626 0.9999755073027972 | no trace 9.177337661732574 1.003372184507195 3.0471324920654297
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && python - <<'EOF'
import numpy as np
from sim import *
H8 = np.arange(0,360,45.)
for lo,hi in [(-180,180),(0,180),(30,150),(45,135),(60,120),(75,105),(85,95)]:
    prefs=np.linspace(lo,hi,256,endpoint=(hi-lo)<360)
    R=rsig(prefs,H8); iu=np.triu_indices(256,1); pos=(R[iu]>0).mean()
    nv=threshold(prefs,0.211,0.072,H8); tr=threshold(prefs,0.211,0.005,H8); ind=threshold(prefs,0,0,H8)
    print(lo,hi, round(pos*100,1), nv, tr, ind, round((1-tr/nv)*100,2))
print('7a')
for p in [-90,-60,-30,0,30,60,90]:
    prefs=np.array([-90.,p]) if p!=-90 else np.array([-90.,-89.999])
    r=rsig(prefs,H8)[0,1]
    print(p, round(r,3), threshold(prefs,0.211,0.072,H8), threshold(prefs,0.211,0.005,H8))
EOF
```

```
-180 180 48.6 7.216687923534262 7.251277745608927 2.2004997192544185 -0.48
0 180 73.1 8.303846871458623 8.132186908651503 2.2048102027584346 2.07
30 150 92.4 8.52509496530305 8.162281733913325 1.8576465941886062 4.26
45 135 99.9 8.281438875810828 7.883826191047028 1.7321961847151588 4.8
60 120 100.0 7.975629285235553 7.590540455757944 1.645983493877725 4.83
75 105 100.0 7.809036562224942 7.451229958223053 1.596065136406933 4.58
85 95 100.0 7.932764026990618 7.559999432632401 1.58155052006169 4.7
7a
-90 1.0 20.171286107649927 19.654303587679827
-60 0.85 19.185655266865954 18.68127368213232
-30 0.455 22.21596885103568 21.640353501918504
0 -0.044 25.22684704613417 25.275688845272835
30 -0.5 21.026705123886952 21.632194054629583
60 -0.805 18.005259596008962 18.526492630065174
90 -0.912 18.884800187046185 19.418037714927962
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && python - <<'EOF'
import fsspec, io, scipy.io as sio, numpy as np, pandas as pd, re
from scipy import stats
import statsmodels.formula.api as smf, statsmodels.api as sm
with fsspec.open("https://crcnsarchive.s3-us-west-2.amazonaws.com/stc-1/live/MSTd.mat","rb") as f: b=f.read()
m=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)
rows=[]
for q in m['experiment3'].pairs:
    rows.append(dict(fid=q.file_id,monk=int(re.match(r'm(\d+)c',q.file_id).group(1)),sv=q.ves.corr_signal,nv=q.ves.corr_noise,sV=q.vis.corr_signal,nV=q.vis.corr_noise))
d=pd.DataFrame(rows); d['group']=np.where(d.monk.isin([17,1,3]),'naive','trained'); d['pool']=(d.nv+d.nV)/2
for cond,s,own in [('ves','sv','nv'),('vis','sV','nV')]:
  for y in ['pool',own]:
    full=smf.ols(f'{y}~{s}*C(group)',d).fit(); add=smf.ols(f'{y}~{s}+C(group)',d).fit()
    a2=sm.stats.anova_lm(full,typ=2); a1=sm.stats.anova_lm(add,typ=2)
    print(cond,y,'add',a1['PR(>F)'].round(5).to_dict(),'full',a2['PR(>F)'].round(5).to_dict())
    for g,dd in d.groupby('group'):
        r=smf.ols(f'{y}~{s}',dd).fit(); print('   ',g, r.params.round(3).to_dict(), r.conf_int().round(3).values.tolist())
# TLS plane
def tls(X,y):
    Z=np.column_stack([X,y]); mu=Z.mean(0); U,S,Vt=np.linalg.svd(Z-mu); n=Vt[-1]; coef=-n[:-1]/n[-1]; return coef, mu[-1]-mu[:-1]@coef
X=d[['sv','sV']].values;y=d.pool.values
c,i=tls(X,y);print('all',c,i)
for g,dd in d.groupby('group'):
    c,i=tls(dd[['sv','sV']].values,dd.pool.values);print(g,c,i)
    print(' ols', smf.ols('pool~sv+sV',dd).fit().params.round(4).to_dict())
# centered per group
dc=d.copy()
for col in ['sv','sV','pool']: dc[col]=d[col]-d.groupby('group')[col].transform('mean')
c,_=tls(dc[['sv','sV']].values,dc.pool.values); print('centered',c, {g:(dd.pool.mean()-dd[['sv','sV']].mean().values@c) for g,dd in d.groupby('group')})
print(smf.ols('pool~sv+sV+C(group)',d).fit().params)
EOF
```

```
ves pool add {'C(group)': 0.01793, 'sv': 0.00016, 'Residual': nan} full {'C(group)': 0.01838, 'sv': 0.00017, 'sv:C(group)': 0.82968, 'Residual': nan}
    naive {'Intercept': 0.095, 'sv': 0.119} [[0.026, 0.163], [-0.021, 0.259]]
    trained {'Intercept': 0.015, 'sv': 0.135} [[-0.018, 0.048], [0.06, 0.21]]
ves nv add {'C(group)': 0.18182, 'sv': 9e-05, 'Residual': nan} full {'C(group)': 0.18319, 'sv': 9e-05, 'sv:C(group)': 0.62964, 'Residual': nan}
    naive {'Intercept': 0.078, 'sv': 0.123} [[0.007, 0.15], [-0.023, 0.269]]
    trained {'Intercept': 0.024, 'sv': 0.162} [[-0.013, 0.062], [0.076, 0.248]]
vis pool add {'C(group)': 0.00712, 'sV': 0.00066, 'Residual': nan} full {'C(group)': 0.00736, 'sV': 0.0007, 'sV:C(group)': 0.96219, 'Residual': nan}
    naive {'Intercept': 0.096, 'sV': 0.107} [[0.028, 0.165], [-0.026, 0.24]]
    trained {'Intercept': 0.009, 'sV': 0.104} [[-0.026, 0.043], [0.038, 0.17]]
vis nV add {'C(group)': 0.00612, 'sV': 0.01677, 'Residual': nan} full {'C(group)': 0.00633, 'sV': 0.01721, 'sV:C(group)': 0.89361, 'Residual': nan}
    naive {'Intercept': 0.116, 'sV': 0.085} [[0.028, 0.205], [-0.086, 0.256]]
    trained {'Intercept': -0.002, 'sV': 0.097} [[-0.046, 0.042], [0.012, 0.181]]
all [0.13172118 0.08507505] 0.02381905849341799
naive [0.12318197 0.10579109] 0.0714459449034329
 ols {'Intercept': 0.0777, 'sv': 0.1055, 'sV': 0.0932}
trained [0.11920425 0.07570668] 0.004617508576232682
 ols {'Intercept': 0.0059, 'sv': 0.1067, 'sV': 0.0728}
centered [0.11909677 0.08381135] {'naive': np.float64(0.07692124360560043), 'trained': np.float64(0.0034195568321832848)}
Intercept              0.080802
C(group)[T.trained]   -0.075678
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . scratch/bin/activate && python - <<'EOF'
import fsspec, io, scipy.io as sio, numpy as np
with fsspec.open("https://crcnsarchive.s3-us-west-2.amazonaws.com/stc-1/live/MSTd.mat","rb") as f: b=f.read()
m=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)
s=m['experiment2'].behv.subj[0]; print(s.ves.thresh, s.vis.thresh)
e2=m['experiment2'].units; e1=m['experiment1'].units
cp=np.array([[u.ves.cp,u.vis.cp] for u in e2],float); print(np.isnan(cp).sum(0), cp.mean(0))
th=np.array([[u.ves.thresh,u.vis.thresh] for u in e2],float); print(np.nanmedian(th,0))
print(e2[0].com.cp, e2[0].ves.stim_local)
EOF
```

```
Fri Nov  6 16:59:31 UTC 2026
<scipy.io.matlab._mio5_params.mat_struct object at 0x728794b1de50> <scipy.io.matlab._mio5_params.mat_struct object at 0x728794b1e050>
[0 0] [0.54835659 0.52018062]
[21.69  14.729]
0.535 [ 9.    3.46  1.33  0.51  0.   -0.51 -1.33 -3.46 -9.  ]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && python - <<'EOF'
import fsspec, io, scipy.io as sio, numpy as np
with fsspec.open("https://crcnsarchive.s3-us-west-2.amazonaws.com/stc-1/live/MSTd.mat","rb") as f: b=f.read()
m=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)
for s in m['experiment2'].behv.subj:
    t=s.ves.thresh; print(s.monk_id, t._fieldnames, [np.shape(getattr(t,k)) for k in t._fieldnames]); print([getattr(t,k) for k in t._fieldnames][:3])
EOF
```

```
2 ['mu'] [()]
[1.2]
5 ['mu'] [()]
[3.1]
Shell cwd was reset to
```

**Agent**

Experiment 2 holds one final vestibular threshold per trained monkey (1.2 and 3.1 degrees) and no training history, so Figure 2A is blocked. Writing the helper module.

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-stc-1-gu-2011/stc1.py",
 "content": "\"\"\"Loading and measures for CRCNS stc-1, MSTd pairs, for Gu et al. (2011), Neuron 71:750-761.\n\nGu, Liu, Fetsch, Yang, Fok, Sunkara, DeAngelis & Angelaki (2011), \"Perceptual Learning Reduces\nInterneuronal Correlations in Macaque Visual Cortex\", doi:10.1016/j.neuron.2011.06.015.\n\nThe data set (doi:10.6080/K07P8WKF) is not versioned on CRCNS; it is read as `unversioned` from\nthe public bucket `crcnsarchive` under stc-1/live/, and each file is checked against the MD5 sum\nin the data set's checksums.md5, so that a later change is detected. Files are streamed into\nmemory; nothing is written to disk.\n\nMSTd.mat holds three structures (data descriptor, version 0.6). `experiment3.pairs` holds, per\npair and per condition (`ves`, `vis`), the signal correlation, the noise correlation and the\npreferred headings of the two units, with the `file_id` of the recording (for example\n`m17c26r1`, monkey 17). `experiment1.units` holds trial-averaged heading tuning curves and\n`experiment2.units` the choice probability and neuronal threshold of 129 single units from\nmonkeys 2 and 5 (Gu et al. 2008).\n\nWhere the parameters come from:\n\n- Training groups. The data set does not say which monkey is naive or trained. The paper gives\n  the pairs per animal under 1 mm (Figure S2B legend: trained 35, 26, 18 and 8, and one trained\n  animal with two pairs; naive 22, 11 and 5). `PAPER_PAIRS_PER_ANIMAL` holds these counts and\n  `assign_groups` matches the monkeys to them by count (the link claim).\n- Pooled noise correlation. The paper's main measure pools z-scored responses across the two\n  conditions (Experimental Procedures, Noise and Signal Correlations, paragraph 2); the data set\n  holds only the per-condition values. Since z-scoring per heading gives each condition's\n  responses unit variance, the Pearson correlation of the pooled z-scores is the trial-weighted\n  mean of the two per-condition correlations; with conditions interleaved and the same\n  repetitions (Experimental Procedures, Experimental Protocol and Task), the weights are equal.\n  `pooled_rnoise` is therefore the mean of the two values. This is an assumption: outliers\n  removed differently in the two conditions would make the weights differ slightly.\n- Type II regression (orthogonal distance) for the plane of equation 5: Experimental Procedures,\n  Population Coding, last sentence.\n- The simulations follow equations 2 to 5 of the Experimental Procedures and the Figure 6A\n  legend (wrapped-Gaussian tuning, bandwidth 135 degrees, preferences uniform, reference heading\n  0). Amplitude 30 spikes/s on a baseline of 10 spikes/s, counted over 1 s, and bandwidth as full\n  width at half height, are the readings the claims file names (fig6a-population-thresholds);\n  they are not from the paper. Preferences evenly spaced over the range is a standard choice.\n  `RSIGNAL_HEADINGS_8` (8 headings 45 degrees apart) and a 1-degree grid are the two rsignal\n  readings of the claims file.\n- Preferred heading from a tuning curve (fig8ab): the vector sum, or the peak of a periodic\n  cubic spline through the curve at 1 degree; the two readings of the claims file\n  (fig4dh-lateral-more-sensitive).\n- Fore-aft and lateral groups: within 45 degrees of 0 or 180, or of -90 or 90 (Results, Effects\n  of Training on Tuning Curves, paragraph 3). A preference at exactly 45 degrees from both is\n  counted as lateral, a standard choice that affects no value in these data.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport hashlib\nimport io\nimport re\n\nimport fsspec\nimport numpy as np\nimport pandas as pd\nimport scipy.io as sio\nfrom scipy.interpolate import CubicSpline\nfrom scipy.optimize import brentq\n\nDATASET_ID = \"stc-1\"\nDATASET_VERSION = \"unversioned\"\nDATASET_DOI = \"10.6080/K07P8WKF\"\nBASE_URL = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/stc-1/live\"\n# MD5 sums from stc-1/live/checksums.md5, read on 2026-11-06.\nMD5 = {\"MSTd.mat\": \"cd4c13b360aa05689015f1bd2b88a05a\", \"VIP.mat\": \"8d7924e0a1ae86c56b78cd1e2f530e2d\"}\n\n# Figure S2B legend: pairs under 1 mm per animal.\nPAPER_PAIRS_PER_ANIMAL = {\"trained\": [35, 26, 18, 8, 2], \"naive\": [22, 11, 5]}\n\n\ndef read_bytes(name: str) -> bytes:\n    \"\"\"Stream a file of the data set into memory and check its MD5 sum.\"\"\"\n    with fsspec.open(f\"{BASE_URL}/{name}\", \"rb\", block_size=2**20) as f:\n        data = f.read()\n    digest = hashlib.md5(data).hexdigest()\n    if name in MD5 and digest != MD5[name]:\n        raise ValueError(f\"{name}: MD5 {digest} differs from checksums.md5 ({MD5[name]})\")\n    return data\n\n\ndef checksums() -> dict[str, str]:\n    \"\"\"The data set's checksums.md5, as published now.\"\"\"\n    text = read_bytes(\"checksums.md5\").decode()\n    return {line.split()[1]: line.split()[0] for line in text.splitlines() if line.strip()}\n\n\ndef load_mat(name: str = \"MSTd.mat\"):\n    return sio.loadmat(io.BytesIO(read_bytes(name)), squeeze_me=True, struct_as_record=False)\n\n\ndef monkey_of(file_id: str) -> int:\n    return int(re.match(r\"m(\\d+)c\", file_id).group(1))\n\n\ndef pairs_table(mat) -> pd.DataFrame:\n    \"\"\"One row per pair of experiment3: monkey, recording, rsignal, rnoise, preferences.\"\"\"\n    rows = []\n    for i, q in enumerate(np.atleast_1d(mat[\"experiment3\"].pairs)):\n        row = {\"pair\": i, \"file_id\": q.file_id, \"monkey\": monkey_of(q.file_id)}\n        for cond in (\"ves\", \"vis\"):\n            c = getattr(q, cond)\n            row[f\"rsig_{cond}\"] = float(c.corr_signal)\n            row[f\"rnoise_{cond}\"] = float(c.corr_noise)\n            row[f\"pref1_{cond}\"], row[f\"pref2_{cond}\"] = (float(x) for x in c.heading_pref)\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\ndef assign_groups(counts: pd.Series) -> dict[int, str]:\n    \"\"\"Match monkeys to the paper's per-animal pair counts. Returns {} when the match is not unique.\"\"\"\n    wanted = {n: g for g, ns in PAPER_PAIRS_PER_ANIMAL.items() for n in ns}\n    if len(wanted) != sum(len(v) for v in PAPER_PAIRS_PER_ANIMAL.values()):\n        return {}\n    if sorted(counts.values) != sorted(wanted):\n        return {}\n    return {int(m): wanted[int(n)] for m, n in counts.items()}\n\n\ndef pooled_rnoise(df: pd.DataFrame) -> pd.Series:\n    \"\"\"Noise correlation pooled across conditions: the mean of the two (see module docstring).\"\"\"\n    return (df[\"rnoise_ves\"] + df[\"rnoise_vis\"]) / 2\n\n\ndef neurons_per_recording(df: pd.DataFrame) -> pd.Series:\n    \"\"\"Distinct units per recording, matching units across its pairs by both preferred headings.\"\"\"\n    out = {}\n    for fid, g in df.groupby(\"file_id\"):\n        units = set()\n        for _, r in g.iterrows():\n            for k in (\"1\", \"2\"):\n                units.add((round(r[f\"pref{k}_ves\"], 3), round(r[f\"pref{k}_vis\"], 3)))\n        out[fid] = len(units)\n    return pd.Series(out)\n\n\ndef unit_table(df: pd.DataFrame) -> pd.DataFrame:\n    \"\"\"Each pair entered twice, once at each unit's preferred heading (Figure 8C legend).\"\"\"\n    rows = []\n    for _, r in df.iterrows():\n        for k in (\"1\", \"2\"):\n            rows.append({\"pair\": r[\"pair\"], \"monkey\": r[\"monkey\"], \"group\": r.get(\"group\"),\n                         \"pref_ves\": r[f\"pref{k}_ves\"], \"pref_vis\": r[f\"pref{k}_vis\"],\n                         \"rnoise\": r[\"rnoise_pooled\"]})\n    return pd.DataFrame(rows)\n\n\ndef wrap180(a):\n    return (np.asarray(a, float) + 180.0) % 360.0 - 180.0\n\n\ndef preference_group(pref):\n    \"\"\"'fore-aft' within 45 degrees of 0 or 180, else 'lateral'.\"\"\"\n    d = np.abs(wrap180(pref))\n    fore_aft = (d < 45) | (d > 135)\n    return np.where(fore_aft, \"fore-aft\", \"lateral\")\n\n\ndef pref_vector_sum(headings, resp) -> float:\n    h = np.deg2rad(np.asarray(headings, float))\n    r = np.asarray(resp, float)\n    return float(np.rad2deg(np.arctan2((r * np.sin(h)).sum(), (r * np.cos(h)).sum())))\n\n\ndef pref_spline_peak(headings, resp) -> float:\n    h = np.asarray(headings, float) % 360.0\n    order = np.argsort(h)\n    h, r = h[order], np.asarray(resp, float)[order]\n    h, idx = np.unique(h, return_index=True)\n    r = r[idx]\n    cs = CubicSpline(np.append(h, h[0] + 360.0), np.append(r, r[0]), bc_type=\"periodic\")\n    grid = np.arange(0.0, 360.0, 1.0)\n    return float(wrap180(grid[np.argmax(cs(grid))]))\n\n\ndef tls_plane(X: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, float]:\n    \"\"\"Type II (orthogonal distance) fit of y = X @ coef + intercept.\"\"\"\n    Z = np.column_stack([X, y])\n    mu = Z.mean(0)\n    normal = np.linalg.svd(Z - mu)[2][-1]\n    coef = -normal[:-1] / normal[-1]\n    return coef, float(mu[-1] - mu[:-1] @ coef)\n\n\n# --- Simulations (equations 2 to 5) ---------------------------------------------------------\n\nAMPLITUDE = 30.0     # spikes/s, claims file reading, not from the paper\nBASELINE = 10.0      # spikes/s, claims file reading, not from the paper\nWINDOW_S = 1.0       # counting window, the middle 1 s (Experimental Procedures)\nBANDWIDTH = 135.0    # degrees, Figure 6A legend, read as full width at half height\nRSIGNAL_HEADINGS_8 = np.arange(0.0, 360.0, 45.0)\nRSIGNAL_HEADINGS_CONT = np.arange(0.0, 360.0, 1.0)\nNAIVE = (0.12, 0.091, 0.072)     # equation 5 coefficients for naive animals (Results)\nTRAINED = (0.12, 0.091, 0.005)   # and for trained animals\n\n\ndef _wrapped_gaussian(theta, pref, sigma):\n    d = np.deg2rad(np.asarray(theta, float)[None, :] - np.asarray(pref, float)[:, None])\n    k = 2 * np.pi * np.arange(-3, 4)\n    return np.exp(-((d[..., None] + k) ** 2) / (2 * np.deg2rad(sigma) ** 2)).sum(-1)\n\n\ndef sigma_for_fwhm(fwhm: float) -> float:\n    \"\"\"Sigma (degrees) of the wrapped Gaussian whose modulation has the given full width at half height.\"\"\"\n    def half(s):\n        g = _wrapped_gaussian([0.0, fwhm / 2, 180.0], [0.0], s)[0]\n        return (g[1] - g[2]) / (g[0] - g[2]) - 0.5\n    return brentq(half, 5.0, 200.0)\n\n\nSIGMA = sigma_for_fwhm(BANDWIDTH)\n\n\ndef tuning(prefs, theta, amplitude=AMPLITUDE, baseline=BASELINE):\n    \"\"\"Mean spike count in the window, shape (neurons, headings).\"\"\"\n    return WINDOW_S * (baseline + amplitude * _wrapped_gaussian(np.atleast_1d(theta), prefs, SIGMA))\n\n\ndef signal_corr(prefs, headings):\n    return np.corrcoef(tuning(prefs, headings))\n\n\ndef threshold(prefs, coefs=None, headings=RSIGNAL_HEADINGS_8, x_ref=0.0,\n              amplitude=AMPLITUDE, baseline=BASELINE, trace=True) -> float:\n    \"\"\"Discrimination threshold (degrees), equations 2 to 5; coefs None is independent noise.\n\n    coefs = (a_vestibular, a_visual, b). With congruent tuning both signal correlations equal the\n    one of the shared tuning curve, so r = (a_vestibular + a_visual) * rsignal + b.\n    \"\"\"\n    prefs = np.asarray(prefs, float)\n    f = tuning(prefs, x_ref, amplitude, baseline)[:, 0]\n    h = 1e-3\n    fp = (tuning(prefs, x_ref + h, amplitude, baseline)[:, 0]\n          - tuning(prefs, x_ref - h, amplitude, baseline)[:, 0]) / (2 * h)\n    if coefs is None:\n        R = np.eye(len(prefs))\n    else:\n        a_ves, a_vis, b = coefs\n        R = (a_ves + a_vis) * signal_corr(prefs, headings) + b\n        np.fill_diagonal(R, 1.0)\n    s = np.sqrt(f)\n    Q = R * np.outer(s, s)\n    Qp = R * (np.outer(fp, f) + np.outer(f, fp)) / (2 * np.outer(s, s))\n    Qi = np.linalg.inv(Q)\n    info = fp @ Qi @ fp\n    if trace:\n        M = Qp @ Qi\n        info += 0.5 * np.sum(M * M.T)\n    return float(np.sqrt(2.0) / np.sqrt(info))\n\n\ndef uniform_prefs(n, lo=-180.0, hi=180.0):\n    \"\"\"n preferences evenly spaced over [lo, hi] (the full circle excludes the repeated end).\"\"\"\n    return np.linspace(lo, hi, n, endpoint=(hi - lo) < 360.0)\n"
}
```

```
File created successfully at: entries/crcns-stc-1-gu-2011/stc1.py (file state is current in your context — no need to Read it back)
```

**Agent**

Now the link claim in the claims file (the one kind of claim the author adds).

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml",
 "old_string": "claims:\n- id: fig2b-trained-lower-noise-correlation",
 "new_string": "claims:\n- id: training-group-link\n  kind: link\n  statement: The monkeys of the data set's 127 MSTd pairs can be assigned to the paper's naive and\n    trained groups, and the assignment agrees with what the data set and the paper both describe.\n  source: Figure S2B legend; Experimental Procedures, Experimental Protocol and Task, paragraph 2\n  quote: 4 subjects (with n= 35, 26, 18, and 8 pairs) were trained in the heading discrimination\n    task (red curves) and 3 animals (with n= 22, 11 and 5 pairs) were naïve (blue curves). Data\n    from one trained animal with only two pairs of neurons is not shown.\n  data: with_labels\n  criterion: Added by the author (protocol, Author, step 1.4); the data set names each pair's\n    monkey in its file_id but not its training group. Monkeys are matched to groups by their\n    number of pairs, against the per-animal counts of the Figure S2B legend (trained 35, 26, 18,\n    8 and 2; naive 22, 11 and 5). Reproduced when every monkey's count matches exactly one count\n    of the legend, the group sizes come to 89 trained and 38 naive pairs, the group neuron counts\n    agree with the 146 trained and 64 naive neurons of the Figure 3 legend, and the monkeys whose\n    behavioural thresholds the data set holds (experiment 2, heading discrimination) fall in the\n    trained group. Not reproduced when the counts cannot be matched one to one.\n- id: fig2b-trained-lower-noise-correlation"
}
```

```
The file claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml'))
print(len(d['claims']), [c['id'] for c in d['claims']])
EOF
python tools/claims_check.py --help 2>&1 | head -5
```

```
35 ['training-group-link', 'fig2b-trained-lower-noise-correlation', 'fig2c-timecourse-naive-higher', 'figs2a-difference-decreases', 'figs2b-individual-animals', 'fig1-example-pair', 'fig1f-modality-correlated', 'fig1f-modality-means-equal', 'figs1-distance', 'methods-single-vs-multiple-electrodes', 'fig2a-behavioral-learning', 'fig3-mean-response-unchanged', 'fig3-fano-unchanged', 'fig4-tuning-width-visual', 'fig4-tuning-width-vestibular', 'fig4-amplitude-unchanged', 'fig4dh-lateral-more-sensitive', 'fig4dh-training-no-sensitivity-change', 'figs4-population-sensitivity-any-reference', 'fig5-noise-signal-positive', 'fig5-slope-unchanged', 'fig5-intercept-lower-trained', 'fig5-regression-coefficients', 'fig6a-population-thresholds', 'fig6b-slope-not-intercept', 'fig7a-pair-sign-of-effect', 'fig7b-msdt-pairs', 'fig7c-narrow-preferences', 'fig8ab-choice-probability-lateral', 'fig8cd-noise-not-preference', 'figs5-congruency', 'figs6-task-independent', 'figs8c-renormalization', 'figs8ab-eye-movements', 'discussion-stimulus-reduces-correlation']
Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re
p='claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml'
t=open(p).read()
targets=['fig2b-trained-lower-noise-correlation','figs2b-individual-animals','fig5-noise-signal-positive','fig5-slope-unchanged','fig5-intercept-lower-trained','fig5-regression-coefficients','fig8cd-noise-not-preference']
blocks=re.split(r'(?m)^(?=- id: )',t)
out=[]
for b in blocks:
    m=re.match(r'- id: (\S+)',b)
    if m and m.group(1) in targets:
        if '  depends_on:\n' in b:
            b=b.replace('  depends_on:\n','  depends_on:\n  - training-group-link\n',1)
        else:
            # insert before criterion
            b=b.replace('  criterion:','  depends_on:\n  - training-group-link\n  criterion:',1)
    out.append(b)
open(p,'w').write(''.join(out))
EOF
git diff --stat; python tools/claims_check.py claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml paper/10.1016-j.neuron.2011.06.015.txt 2>&1 | tail -15
```

Result: not kept, because it reads the paper's text.

**Agent**

Quote check passes with the link claim. Now the notebook: I'll generate it with a script, run it in a scratch environment to read the numbers, then write the conclusions.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/gen && cat > $TMPDIR/gen/cells1.py <<'EOF'
CELLS = []
def md(s, tags=None): CELLS.append(("markdown", s.strip("\n"), tags))
def code(s, tags=None): CELLS.append(("code", s.strip("\n"), tags))

md(r'''
# Reproducing Gu et al. (2011) from CRCNS stc-1

**Paper.** Gu Y, Liu S, Fetsch CR, Yang Y, Fok S, Sunkara A, DeAngelis GC, Angelaki DE (2011).
Perceptual learning reduces interneuronal correlations in macaque visual cortex. *Neuron* 71:750-761.
[doi:10.1016/j.neuron.2011.06.015](https://doi.org/10.1016/j.neuron.2011.06.015). The claims file
was written from the version of record (journal PDF text, with the Experimental Procedures and the
legends of Figures 1 to 8) and the Supplemental Information (legends of Figures S1 to S8).

**Data set.** CRCNS [stc-1](https://doi.org/10.6080/K07P8WKF) (doi:10.6080/K07P8WKF), data
descriptor version 0.6 (5 September 2018), read from the public bucket `crcnsarchive` under
`stc-1/live/`. CRCNS data sets are not versioned, and the paper cites no version, so the version is
recorded as `unversioned` (docs/archives.md, CRCNS). The bucket holds one copy of the data,
`stc-1/live/` (`orig/` holds only an older description document), so `live/` is the version
pinned. The file read, `MSTd.mat`, is checked on loading against its MD5 sum in the data set's
`checksums.md5`, `cd4c13b360aa05689015f1bd2b88a05a`, so a later change makes the notebook fail
(`VIP.mat`, read only to check for overlap, `8d7924e0a1ae86c56b78cd1e2f530e2d`).

**What the data set holds.** Derived values only. For the paper, experiment 3 of `MSTd.mat` holds
the 127 MSTd pairs separated by less than 1 mm, with per condition (vestibular, visual) the signal
correlation, the noise correlation and the two units' preferred headings, and the recording's
`file_id`, which names the monkey. It holds no spike times or trial responses, no training-group
label, no distances, no tuning curves of the pair units, none of the 52 pairs over 1 mm, none of the
single-electrode database of Figure 4, Figure S4 and Figure 8A, no training histories and no eye
records. Experiments 1 and 2 hold the tuning curves, choice probabilities and neuronal thresholds
of 129 single units of two trained monkeys from Gu et al. (2008); they are used for
fig8ab-choice-probability-lateral as a subset of the paper's database.

**Outside inputs.** None beyond the paper itself: the training group of each monkey comes from the
paper's per-animal pair counts (Figure S2B legend), checked by the link claim
`training-group-link`.

**Random numbers.** None of the analyses below draws random numbers.

| Claim | Tested here |
|---|---|
| training-group-link | tested (link) |
| fig2b-trained-lower-noise-correlation | tested |
| figs2b-individual-animals | tested (means per animal; no time courses) |
| fig1-example-pair | tested |
| fig1f-modality-correlated | tested on the 127 pairs under 1 mm |
| fig1f-modality-means-equal | tested on the 127 pairs under 1 mm |
| fig5-noise-signal-positive | tested |
| fig5-slope-unchanged | tested |
| fig5-intercept-lower-trained | tested |
| fig5-regression-coefficients | tested |
| fig6a-population-thresholds | tested (simulation) |
| fig6b-slope-not-intercept | tested (simulation) |
| fig7a-pair-sign-of-effect | tested (simulation) |
| fig7c-narrow-preferences | tested (simulation) |
| fig8ab-choice-probability-lateral | tested on 129 units of two monkeys |
| fig8cd-noise-not-preference | tested |
| fig2c-timecourse-naive-higher, figs2a-difference-decreases, fig3-mean-response-unchanged, fig3-fano-unchanged, figs8c-renormalization, discussion-stimulus-reduces-correlation | blocked: no spike times or trial responses |
| figs1-distance | blocked: no distances, no pairs over 1 mm |
| methods-single-vs-multiple-electrodes | blocked: no electrode label |
| fig2a-behavioral-learning | blocked: no training histories |
| fig4-tuning-width-visual, fig4-tuning-width-vestibular, fig4-amplitude-unchanged, fig4dh-lateral-more-sensitive, fig4dh-training-no-sensitivity-change, figs4-population-sensitivity-any-reference | blocked: no naive animals in the single-unit data |
| fig7b-msdt-pairs, figs5-congruency | blocked: no tuning curves of the pair units |
| figs6-task-independent | blocked: no discrimination-task correlations |
| figs8ab-eye-movements | blocked: no eye records |
''')

code(r'''
import time
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy import stats

import stc1

warnings.filterwarnings("ignore", category=FutureWarning)
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 30)
started = time.time()
mat = stc1.load_mat("MSTd.mat")
vip = stc1.load_mat("VIP.mat")
print(f"CRCNS {stc1.DATASET_ID} ({stc1.DATASET_VERSION}, doi:{stc1.DATASET_DOI}): MSTd.mat and VIP.mat "
      f"read and checked against their MD5 sums in {time.time() - started:.1f} s")
''')

md('''
## Data check

Each check of the metadata against the values is stated under its output.
''')

code(r'''
published = stc1.checksums()
print("checksums.md5 now lists:", published)
print("MSTd.mat and VIP.mat match the sums pinned in stc1.py:",
      all(published[k] == v for k, v in stc1.MD5.items()))
print("Variables in MSTd.mat:", [k for k in mat if not k.startswith("__")], mat["__header__"].decode())
for e in ("experiment1", "experiment2", "experiment3"):
    x = mat[e]
    print(f"{e}: name {x.name!r}, fields {x._fieldnames}")
q = mat["experiment3"].pairs[0]
print("experiment3.pairs fields:", q._fieldnames, "; per condition:", q.ves._fieldnames)
u1, u2 = mat["experiment1"].units[0], mat["experiment2"].units[0]
print("experiment1.units fields:", u1._fieldnames, u1.ves._fieldnames)
print("experiment2.units fields:", u2._fieldnames, u2.ves._fieldnames, "; com:", u2.com._fieldnames)
print("experiment2.behv.subj:", [(s.monk_id, s.ves.thresh._fieldnames) for s in mat["experiment2"].behv.subj])
''', ["sanity"])

code(r'''
pairs = stc1.pairs_table(mat)
print("Pairs in experiment3:", len(pairs), "(data descriptor: 127 MSTd pairs; paper: 127 pairs under 1 mm)")
print("Missing values:", int(pairs.isna().sum().sum()))
cols = ["rsig_ves", "rsig_vis", "rnoise_ves", "rnoise_vis", "pref1_ves", "pref2_ves", "pref1_vis", "pref2_vis"]
print("\nRanges (correlations are unitless; preferred headings in degrees):")
print(pairs[cols].describe().loc[["count", "mean", "min", "max"]].round(3).to_string())
print("\nPairs per monkey (monkey from file_id):")
counts = pairs.monkey.value_counts()
print(counts.to_string())
print("Monkeys in the data:", sorted(counts.index.tolist()),
      "; data descriptor lists MSTd pair monkeys 1, 2, 3, 5, 17, 18, 19")
print("Paper: 8 monkeys in all (Experimental Procedures, Subjects)")
''', ["sanity"])

md('''
The pairs hold every field the descriptor names, with no missing values. Correlations lie within
-1 and 1 and preferred headings within -180 and 180 degrees. The `file_id`s name eight monkeys,
as many as the paper's eight; the data descriptor lists seven for the MSTd pairs and leaves out
monkey 24, which has two pairs.
''')

code(r'''
# Units per recording: a unit in several pairs of one recording has the same preferred headings.
per_rec = pairs.groupby("file_id").size()
units = stc1.neurons_per_recording(pairs)
shape = pd.DataFrame({"pairs": per_rec, "units": units})
print("Recordings by (pairs, units):", shape.value_counts().sort_index().to_dict())
print("Every recording with k units has k(k-1)/2 pairs:",
      bool((shape.pairs == shape.units * (shape.units - 1) // 2).all()))
print("Distinct units over the 127 pairs:", int(units.sum()))
print("Largest number of pairs in one recording:", int(per_rec.max()), list(per_rec[per_rec == per_rec.max()].index),
      "; paper: 'maximum of 5 pairs in an experiment' (Experimental Procedures)")
dup = pairs.duplicated(subset=["rsig_ves", "rsig_vis", "rnoise_ves", "rnoise_vis"], keep=False)
print("\nPairs with identical correlations (deposited twice):", int(dup.sum()))
vip_ids = {p.file_id for p in np.atleast_1d(vip["experiment3"].pairs)}
vip_vals = {(round(float(p.ves.corr_noise), 4), round(float(p.vis.corr_noise), 4)) for p in np.atleast_1d(vip["experiment3"].pairs)}
mst_vals = set(zip(pairs.rnoise_ves.round(4), pairs.rnoise_vis.round(4)))
print("VIP pairs:", len(vip_ids and np.atleast_1d(vip["experiment3"].pairs)), "; recordings shared with MSTd:", len(vip_ids & set(pairs.file_id)),
      "; noise-correlation pairs shared:", len(vip_vals & mst_vals))
''', ["sanity"])

md('''
Within each recording the units can be told apart by their preferred headings, and every recording
with k units has exactly k(k-1)/2 pairs, so the pairs are all pairs of the units recorded together
and the 127 pairs come from the distinct units counted above. No pair is deposited twice, and no
MSTd pair is repeated in `VIP.mat`. One recording holds six pairs (four units), more than the
paper's stated maximum of five pairs per experiment.
''')

code(r'''
# Signal correlation should follow the similarity of the two preferences: a check that the
# preferred headings and the signal correlation of a pair refer to the same two units and condition.
for cond in ("ves", "vis"):
    sim = np.cos(np.deg2rad(pairs[f"pref1_{cond}"] - pairs[f"pref2_{cond}"]))
    other = "vis" if cond == "ves" else "ves"
    sim_other = np.cos(np.deg2rad(pairs[f"pref1_{other}"] - pairs[f"pref2_{other}"]))
    print(f"{cond}: Spearman rho of rsignal with cos(preference difference) of the same condition "
          f"{stats.spearmanr(pairs[f'rsig_{cond}'], sim)[0]:.3f}, of the other condition {stats.spearmanr(pairs[f'rsig_{cond}'], sim_other)[0]:.3f}")
''', ["sanity"])

md('''
Signal correlation follows the difference between the two preferred headings of the same
condition much more closely than that of the other condition, so the fields are consistent with
their description. The data hold no time series, so there is no clock to check against a trial
table (protocol, Author, step 2): every value used here is a per-pair or per-unit summary.
''')

code(r'''
groups = stc1.assign_groups(counts)
pairs["group"] = pairs.monkey.map(groups)
pairs["rnoise_pooled"] = stc1.pooled_rnoise(pairs)
units_by_group = {g: int(units[pairs[pairs.group == g].file_id.unique()].sum()) for g in ("trained", "naive")}
print("Group assigned per monkey:", groups)
print("Pairs per group:", pairs.group.value_counts().to_dict(), "; units per group:", units_by_group)
print("\nSingle-unit experiments: monkeys", sorted({stc1.monkey_of(u.file_id) for u in mat["experiment1"].units}),
      "; units in experiment1 and experiment2:", len(mat["experiment1"].units), len(mat["experiment2"].units))
same_cells = all(a.file_id.split("r")[0] == b.file_id.split("r")[0]
                 for a, b in zip(mat["experiment1"].units, mat["experiment2"].units))
print("experiment1 and experiment2 list the same cells in the same order (cell id before 'r'):", same_cells)
print("Headings of experiment1 tuning curves (deg):", mat["experiment1"].units[0].ves.stim_global)
print("Headings of experiment2 (deg):", mat["experiment2"].units[0].ves.stim_local)
print("Behavioural thresholds held (experiment2.behv, vestibular, visual):",
      {s.monk_id: (float(s.ves.thresh.mu), float(s.vis.thresh.mu)) for s in mat["experiment2"].behv.subj})
''', ["sanity"])

md('''
The data set gives no training group. The link claim below assigns the groups from the paper's
per-animal pair counts. Experiments 1 and 2 list the same 129 cells, from monkeys 2 and 5, which
the data set's own behavioural thresholds show performed the heading discrimination task.
''')
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && sed -i 's/len(vip_ids and np.atleast_1d(vip\["experiment3"\].pairs))/len(np.atleast_1d(vip["experiment3"].pairs))/' cells1.py && grep -n 'VIP pairs' cells1.py && cat > cells2.py <<'EOF'
from cells1 import CELLS, md, code

md('''
## training-group-link

> The monkeys of the data set's 127 MSTd pairs can be assigned to the paper's naive and trained
> groups, and the assignment agrees with what the data set and the paper both describe.

Criterion (added by the author): match monkeys to the Figure S2B counts (trained 35, 26, 18, 8 and
2; naive 22, 11 and 5); check 89 and 38 pairs, 146 and 64 neurons (Figure 3 legend), and that the
monkeys with behavioural thresholds in the data set are trained.
''')
code(r'''
legend = sorted(n for ns in stc1.PAPER_PAIRS_PER_ANIMAL.values() for n in ns)
print("Pairs per monkey in the data:", sorted(counts.values.tolist()))
print("Pairs per animal in the Figure S2B legend:", legend)
print("Counts in the legend all distinct:", len(set(legend)) == len(legend))
print("Monkeys matched one to one:", len(groups) == len(counts), groups)
print("Pairs per group:", pairs.group.value_counts().to_dict(), "(paper: trained 89, naive 38)")
print("Units per group:", units_by_group, "(Figure 3 legend: trained 146, naive 64)")
behv = sorted(int(s.monk_id) for s in mat["experiment2"].behv.subj)
print("Monkeys with discrimination thresholds in experiment2:", behv, "-> groups", [groups[m] for m in behv])
''', ["claim:training-group-link"])

md('''
## fig2b-trained-lower-noise-correlation

> Mean noise correlation among MSTd pairs (separated by less than 1 mm) is significantly smaller in
> trained animals (0.023 +- 0.017 SEM, n = 89) than in naive animals (0.116 +- 0.031, n = 38).

The pooled rnoise is the mean of the vestibular and visual values (assumption, see `stc1.py`). The
criterion's readings are a two-sided Student and a Welch t test; whether the stored values include
the renormalization in blocks of 20 trials cannot be told from the data set, which holds one value
per condition and no trial responses, so that reading cannot be run. The per-condition values are
shown as variants.
''')
code(r'''
def group_ttest(col, df=pairs):
    t, n = df[df.group == "trained"][col], df[df.group == "naive"][col]
    return {"measure": col, "trained_mean": t.mean(), "trained_sem": t.sem(), "n_trained": len(t),
            "naive_mean": n.mean(), "naive_sem": n.sem(), "n_naive": len(n),
            "difference": n.mean() - t.mean(),
            "p_student": stats.ttest_ind(t, n).pvalue, "p_welch": stats.ttest_ind(t, n, equal_var=False).pvalue}

fig2b = pd.DataFrame([group_ttest(c) for c in ("rnoise_pooled", "rnoise_ves", "rnoise_vis")])
print(fig2b.round(4).to_string(index=False))
print("\nExpected: trained 0.023 +- 0.017 (0.006 to 0.040), naive 0.116 +- 0.031 (0.085 to 0.147), p = 0.006")
row = fig2b.iloc[0]
print("Pooled means within tolerance:", abs(row.trained_mean - 0.023) <= 0.017, abs(row.naive_mean - 0.116) <= 0.031)
print("\nWithout the trained animal with two pairs (monkey 24):")
print(pd.DataFrame([group_ttest("rnoise_pooled", pairs[pairs.monkey != 24])]).round(4).to_string(index=False))
fig, ax = plt.subplots(1, 2, figsize=(8, 3), sharex=True)
for a, g in zip(ax, ("naive", "trained")):
    v = pairs[pairs.group == g].rnoise_pooled
    a.hist(v, bins=np.arange(-0.6, 0.71, 0.05), color="tab:blue" if g == "naive" else "tab:red")
    a.axvline(v.mean(), color="k")
    a.set_title(f"{g}, n = {len(v)}")
    a.set_xlabel("pooled rnoise")
plt.tight_layout(); plt.show()
print("Range of pooled rnoise plotted:", pairs.rnoise_pooled.min().round(3), "to", pairs.rnoise_pooled.max().round(3), "(all inside the axes)")
''', ["claim:fig2b-trained-lower-noise-correlation"])

md('''
## figs2b-individual-animals

> The greater noise correlation in naive animals holds for individual animals; four trained animals
> (35, 26, 18 and 8 pairs) and three naive animals (22, 11 and 5 pairs) are shown, and the
> difference is consistent across animals within each group.

Per animal, the mean pooled rnoise of its pairs. The time courses of Figure S2B need spike times,
which the data set does not hold.
''')
code(r'''
per_animal = (pairs.groupby(["group", "monkey"]).rnoise_pooled.agg(["count", "mean", "sem"])
              .sort_values(["group", "count"], ascending=[True, False]).round(4))
print(per_animal.to_string())
shown = per_animal[per_animal["count"] > 2]
naive_means = shown.loc["naive", "mean"]
trained_means = shown.loc["trained", "mean"]
print("\nPair counts, trained shown:", shown.loc["trained", "count"].tolist(), "(paper 35, 26, 18, 8)",
      "; naive:", shown.loc["naive", "count"].tolist(), "(paper 22, 11, 5)")
print("Lowest naive animal mean:", naive_means.min(), "; highest trained animal mean (shown):", trained_means.max())
print("Every naive mean above every trained mean (seven animals shown):", naive_means.min() > trained_means.max())
print("Every naive mean above the trained group mean", round(pairs[pairs.group == "trained"].rnoise_pooled.mean(), 4), ":",
      bool((naive_means > pairs[pairs.group == "trained"].rnoise_pooled.mean()).all()))
print("\nPer condition (variants):")
print(pairs.groupby(["group", "monkey"])[["rnoise_ves", "rnoise_vis"]].mean().round(4).to_string())
''', ["claim:figs2b-individual-animals"])

md('''
## fig1-example-pair

> For the example pair of Figure 1, signal correlation is 0.83 (visual) and 0.79 (vestibular), and
> noise correlation is 0.29 (visual, p = 0.04) and 0.14 (vestibular, p = 0.3).

The paper does not identify the pair; the criterion asks whether any pair has all four values
within 10%. The p values need the number of trials, which the data set does not hold.
''')
code(r'''
target = {"rsig_vis": 0.83, "rsig_ves": 0.79, "rnoise_vis": 0.29, "rnoise_ves": 0.14}
inside = pd.DataFrame({k: (pairs[k] - v).abs() <= 0.1 * v + 1e-9 for k, v in target.items()})
pairs["n_within"] = inside.sum(axis=1)
print("Pairs by number of the four values within tolerance:", pairs.n_within.value_counts().sort_index().to_dict())
cand = pairs[pairs.n_within >= 2].copy()
dist = sum(((cand[k] - v) / v) ** 2 for k, v in target.items()) ** 0.5
print("\nPairs with at least two values within tolerance, closest first:")
print(cand.assign(rel_distance=dist).sort_values("rel_distance")[["file_id", "group", *target, "n_within", "rel_distance"]].round(3).head(10).to_string(index=False))
print("\nPairs with all four within tolerance:", int((pairs.n_within == 4).sum()))
''', ["claim:fig1-example-pair"])

md('''
## fig1f-modality-correlated

> Noise correlations computed from visual and vestibular responses are correlated across pairs
> (R = 0.38, p << 0.001, Spearman rank correlation, 179 pairs).

Only the 127 pairs under 1 mm are in the data set, the criterion's other reading.
''')
code(r'''
rho, p = stats.spearmanr(pairs.rnoise_vis, pairs.rnoise_ves)
print(f"Spearman R = {rho:.3f}, p = {p:.2e}, n = {len(pairs)} (expected 0.38 +- 0.038, i.e. 0.342 to 0.418, n = 179)")
print("Pearson r =", round(stats.pearsonr(pairs.rnoise_vis, pairs.rnoise_ves)[0], 3))
print("\nPer group and per monkey:")
for key, g in list(pairs.groupby("group")) + list(pairs.groupby("monkey")):
    if len(g) >= 5:
        r_, p_ = stats.spearmanr(g.rnoise_vis, g.rnoise_ves)
        print(f"  {key}: n = {len(g)}, R = {r_:.3f}, p = {p_:.3g}")
fig, ax = plt.subplots(figsize=(3.5, 3.5))
ax.scatter(pairs.rnoise_vis, pairs.rnoise_ves, s=10, c=np.where(pairs.group == "naive", "tab:blue", "tab:red"))
ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_xlabel("rnoise visual"); ax.set_ylabel("rnoise vestibular")
plt.show()
''', ["claim:fig1f-modality-correlated"])

md('''
## fig1f-modality-means-equal

> Mean noise correlation does not differ between the vestibular (0.035 +- 0.014 SEM) and visual
> (0.039 +- 0.015) conditions (p > 0.8, paired t test).

A claim of absence, judged on a paired t test at p < 0.05, on the 127 pairs under 1 mm.
''')
code(r'''
v, w = pairs.rnoise_ves, pairs.rnoise_vis
res = stats.ttest_rel(v, w)
print(f"vestibular {v.mean():.4f} +- {v.sem():.4f}, visual {w.mean():.4f} +- {w.sem():.4f} (n = {len(v)})")
print(f"difference (vestibular - visual) {(v - w).mean():.4f}, 95% CI {np.round(stats.t.interval(0.95, len(v) - 1, (v - w).mean(), (v - w).sem()), 4)}")
print(f"paired t = {res.statistic:.3f}, p = {res.pvalue:.3f}")
print("Expected: vestibular 0.035 +- 0.014 (0.021 to 0.049), visual 0.039 +- 0.015 (0.024 to 0.054)")
print("Within tolerance:", abs(v.mean() - 0.035) <= 0.014, abs(w.mean() - 0.039) <= 0.015)
for g, d in pairs.groupby("group"):
    print(f"  {g}: vestibular {d.rnoise_ves.mean():.4f}, visual {d.rnoise_vis.mean():.4f}, paired p = {stats.ttest_rel(d.rnoise_ves, d.rnoise_vis).pvalue:.3f}")
''', ["claim:fig1f-modality-means-equal"])
EOF
echo ok
```

```
151:print("VIP pairs:", len(np.atleast_1d(vip["experiment3"].pairs)), "; recordings shared with MSTd:", len(vip_ids & set(pairs.file_id)),
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && cat > cells3.py <<'EOF'
from cells2 import CELLS, md, code

md('''
## fig5-noise-signal-positive

> Noise correlation increases with signal correlation in both conditions (vestibular p = 0.0001,
> visual p = 0.0004, ANCOVA).

Per condition, an ANCOVA of rnoise on rsignal and training group with their interaction, over the
127 pairs; the rnoise readings are the pooled value and the value of the same condition. How the
sums of squares are formed is not stated; Type II tests of the model with the interaction, and of
the model without it (the classical ANCOVA), are both shown (a choice made here, since the paper
does not say). The tests of all three ANCOVA claims are computed in this cell.
''')
code(r'''
def ancova(cond, measure):
    s = f"rsig_{cond}"
    full = smf.ols(f"{measure} ~ {s} * C(group)", pairs).fit()
    add = smf.ols(f"{measure} ~ {s} + C(group)", pairs).fit()
    a_full, a_add = sm.stats.anova_lm(full, typ=2), sm.stats.anova_lm(add, typ=2)
    return {"condition": cond, "rnoise": measure,
            "slope_all": add.params[s],
            "p_rsignal_full": a_full.loc[s, "PR(>F)"], "p_rsignal_additive": a_add.loc[s, "PR(>F)"],
            "p_group_full": a_full.loc["C(group)", "PR(>F)"], "p_group_additive": a_add.loc["C(group)", "PR(>F)"],
            "p_interaction": a_full.loc[f"{s}:C(group)", "PR(>F)"],
            "group_effect_additive": add.params["C(group)[T.trained]"]}

anc = pd.DataFrame([ancova(c, m) for c in ("ves", "vis") for m in ("rnoise_pooled", f"rnoise_{c}")])
print(anc.round(5).to_string(index=False))
print("\nPaper: rsignal vestibular p = 0.0001, visual p = 0.0004; interaction 0.9 and 0.9; training 0.02 and 0.008")
print("\nSlope of pooled rnoise on rsignal per monkey (OLS; monkeys with at least 5 pairs):")
rows = []
for m, d in pairs.groupby("monkey"):
    if len(d) >= 5:
        for c in ("ves", "vis"):
            r = stats.linregress(d[f"rsig_{c}"], d.rnoise_pooled)
            rows.append({"monkey": m, "group": groups[m], "condition": c, "n": len(d), "slope": r.slope, "p": r.pvalue})
print(pd.DataFrame(rows).pivot_table(index=["group", "monkey", "n"], columns="condition", values=["slope", "p"]).round(3).to_string())
fig, ax = plt.subplots(1, 2, figsize=(8, 3.5), sharey=True)
for a, c in zip(ax, ("vis", "ves")):
    for g, col in (("naive", "tab:blue"), ("trained", "tab:red")):
        d = pairs[pairs.group == g]
        a.scatter(d[f"rsig_{c}"], d.rnoise_pooled, s=10, color=col, label=g)
        fit = stats.linregress(d[f"rsig_{c}"], d.rnoise_pooled)
        a.plot([-1, 1], fit.intercept + fit.slope * np.array([-1, 1]), color=col)
    a.set_xlim(-1, 1); a.set_ylim(-1, 1); a.set_xlabel(f"rsignal {c}")
ax[0].set_ylabel("pooled rnoise"); ax[0].legend(); plt.tight_layout(); plt.show()
''', ["claim:fig5-noise-signal-positive"])

md('''
## fig5-slope-unchanged

> Training does not change the slope of the relation between noise and signal correlation
> (vestibular p = 0.9, visual p = 0.9, ANCOVA interaction).

A claim of absence, judged on the interaction term at p < 0.05 with the pooled rnoise; slopes and
their 95% intervals per group, from separate fits and from the ANCOVA model with the interaction
(Figure 5 legend: "Lines represent regression fits (ANCOVA)"), are reported.
''')
code(r'''
def group_lines(cond, measure):
    s = f"rsig_{cond}"
    rows = []
    cell = smf.ols(f"{measure} ~ 0 + C(group) + C(group):{s}", pairs).fit()
    ci_cell = cell.conf_int()
    for g in ("naive", "trained"):
        sep = smf.ols(f"{measure} ~ {s}", pairs[pairs.group == g]).fit()
        ci = sep.conf_int()
        rows.append({"condition": cond, "rnoise": measure, "group": g,
                     "slope": sep.params[s], "slope_lo": ci.loc[s, 0], "slope_hi": ci.loc[s, 1],
                     "intercept": sep.params["Intercept"], "int_lo": ci.loc["Intercept", 0], "int_hi": ci.loc["Intercept", 1],
                     "int_lo_ancova": ci_cell.loc[f"C(group)[{g}]", 0], "int_hi_ancova": ci_cell.loc[f"C(group)[{g}]", 1],
                     "slope_lo_ancova": ci_cell.loc[f"C(group)[{g}]:{s}", 0], "slope_hi_ancova": ci_cell.loc[f"C(group)[{g}]:{s}", 1]})
    return rows

lines = pd.DataFrame([r for c in ("ves", "vis") for m in ("rnoise_pooled", f"rnoise_{c}") for r in group_lines(c, m)])
print(lines.round(4).to_string(index=False))
print("\nInteraction p (pooled rnoise):", anc[anc.rnoise == "rnoise_pooled"].set_index("condition").p_interaction.round(3).to_dict())
print("Interaction p (same-condition rnoise):", anc[anc.rnoise != "rnoise_pooled"].set_index("condition").p_interaction.round(3).to_dict())
''', ["claim:fig5-slope-unchanged"])

md('''
## fig5-intercept-lower-trained

> Training lowers noise correlation uniformly across signal correlations, a main effect of training
> (vestibular p = 0.02, visual p = 0.008, ANCOVA) with non-overlapping 95% confidence intervals of
> the intercepts.

The training main effect is in the table of fig5-noise-signal-positive; the intercept intervals
are from the fig5-slope-unchanged table, under both the separate fits and the ANCOVA model.
''')
code(r'''
for (c, m), d in lines.groupby(["condition", "rnoise"], sort=False):
    n, t = d.set_index("group").loc["naive"], d.set_index("group").loc["trained"]
    a = anc[(anc.condition == c) & (anc.rnoise == m)].iloc[0]
    print(f"{c}, {m}: training p (full / additive) {a.p_group_full:.4f} / {a.p_group_additive:.4f}; "
          f"intercept naive {n.intercept:.4f}, trained {t.intercept:.4f}")
    print(f"    separate fits: naive [{n.int_lo:.4f}, {n.int_hi:.4f}], trained [{t.int_lo:.4f}, {t.int_hi:.4f}], overlap {t.int_hi >= n.int_lo}")
    print(f"    ANCOVA model:  naive [{n.int_lo_ancova:.4f}, {n.int_hi_ancova:.4f}], trained [{t.int_lo_ancova:.4f}, {t.int_hi_ancova:.4f}], overlap {t.int_hi_ancova >= n.int_lo_ancova}")
print("\nVariant, intercepts of the additive model (common slope), 95% CI of each group's intercept:")
for c in ("ves", "vis"):
    add = smf.ols(f"rnoise_pooled ~ 0 + C(group) + rsig_{c}", pairs).fit()
    ci = add.conf_int()
    print(f"  {c}: naive [{ci.loc['C(group)[naive]', 0]:.4f}, {ci.loc['C(group)[naive]', 1]:.4f}], "
          f"trained [{ci.loc['C(group)[trained]', 0]:.4f}, {ci.loc['C(group)[trained]', 1]:.4f}]")
''', ["claim:fig5-intercept-lower-trained"])

md('''
## fig5-regression-coefficients

> The plane fitted to noise and the two signal correlations is rnoise = 0.12 rsignal,vestibular +
> 0.091 rsignal,visual + 0.072 in naive animals, with the same slopes and an intercept of 0.005 in
> trained animals.

Type II (orthogonal) plane fits of pooled rnoise on the two signal correlations, under the
criterion's readings (a), (b) and (c); ordinary least squares as a variant. 95% intervals of the
intercepts by a bootstrap over pairs within each group (2000 resamples, seed fixed; the number of
resamples is a standard choice).
''')
code(r'''
X_cols = ["rsig_ves", "rsig_vis"]
expected = np.array([0.12, 0.091, 0.072, 0.005])
tol = np.array([0.012, 0.0091, 0.0072, 0.0005])

def readings(df):
    out = {}
    nv, tr = df[df.group == "naive"], df[df.group == "trained"]
    cen = df.copy()
    for c in X_cols + ["rnoise_pooled"]:
        cen[c] = df[c] - df.groupby("group")[c].transform("mean")
    coef_a, _ = stc1.tls_plane(cen[X_cols].values, cen.rnoise_pooled.values)
    out["a: common slopes, centred per group"] = coef_a
    coef_b, _ = stc1.tls_plane(df[X_cols].values, df.rnoise_pooled.values)
    out["b: slopes of one fit to all pairs"] = coef_b
    coef_c, _ = stc1.tls_plane(nv[X_cols].values, nv.rnoise_pooled.values)
    out["c: slopes of the naive fit"] = coef_c
    res = {}
    for k, coef in out.items():
        b_n = nv.rnoise_pooled.mean() - nv[X_cols].mean().values @ coef
        b_t = tr.rnoise_pooled.mean() - tr[X_cols].mean().values @ coef
        res[k] = np.array([coef[0], coef[1], b_n, b_t])
    for g, d in (("naive", nv), ("trained", tr)):
        co, b = stc1.tls_plane(d[X_cols].values, d.rnoise_pooled.values)
        res[f"separate orthogonal fit, {g}"] = np.array([co[0], co[1], b if g == "naive" else np.nan, b if g == "trained" else np.nan])
    ols_all = smf.ols("rnoise_pooled ~ 0 + C(group) + rsig_ves + rsig_vis", df).fit().params
    res["variant: OLS, common slopes"] = np.array([ols_all["rsig_ves"], ols_all["rsig_vis"], ols_all["C(group)[naive]"], ols_all["C(group)[trained]"]])
    for g, d in (("naive", nv), ("trained", tr)):
        o = smf.ols("rnoise_pooled ~ rsig_ves + rsig_vis", d).fit().params
        res[f"variant: OLS, {g}"] = np.array([o["rsig_ves"], o["rsig_vis"], o["Intercept"] if g == "naive" else np.nan, o["Intercept"] if g == "trained" else np.nan])
    return res

fits = readings(pairs)
table = pd.DataFrame(fits, index=["a_vestibular", "a_visual", "b_naive", "b_trained"]).T
within = table.apply(lambda r: pd.Series(np.abs(r.values - expected) <= tol + 1e-12, index=[f"in_{i}" for i in table.columns]), axis=1)
print(table.round(4).join(within).to_string())
print("\nExpected:", expected, "+-", tol)

rng = np.random.default_rng(20110825)
boot = {k: [] for k in fits if k[0] in "abc"}
for _ in range(2000):
    sample = pd.concat([d.iloc[rng.integers(0, len(d), len(d))] for _, d in pairs.groupby("group")])
    r = readings(sample)
    for k in boot:
        boot[k].append(r[k])
print("\nBootstrap 95% intervals (2000 resamples within groups):")
for k, v in boot.items():
    lo, hi = np.percentile(np.array(v), [2.5, 97.5], axis=0)
    print(f"  {k}: " + ", ".join(f"{n} [{a:.4f}, {b:.4f}]" for n, a, b in zip(table.columns, lo, hi)))
''', ["claim:fig5-regression-coefficients"])
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && cat > cells4.py <<'EOF'
from cells3 import CELLS, md, code

md('''
## fig6a-population-thresholds

> In simulated populations, correlated noise as measured in naive animals raises the population
> threshold about 5-fold over independent noise at 2000 neurons, while the uniform reduction in
> trained animals has little effect on the threshold compared with naive.

Equations 2 to 5 with the paper's coefficients, wrapped-Gaussian tuning of 135 degrees full width at
half height, preferences evenly spaced on the circle, congruent tuning, reference heading 0,
amplitude 30 spikes/s on a baseline of 10 spikes/s over 1 s (the claims file's readings). The two
rsignal readings (8 headings, 1-degree grid) are run. As variants: other amplitudes and baselines,
Fisher information without the trace term of equation 3, and the coefficients fitted here
(fig5-regression-coefficients, reading c).
''')
code(r'''
print(f"Wrapped-Gaussian sigma for a 135 degree full width at half height: {stc1.SIGMA:.2f} degrees")
sizes = [16, 64, 256, 1000, 2000]
rsig_readings = {"8 headings": stc1.RSIGNAL_HEADINGS_8, "1-degree grid": stc1.RSIGNAL_HEADINGS_CONT}
rows = []
for name, H in rsig_readings.items():
    for n in sizes:
        prefs = stc1.uniform_prefs(n)
        ind = stc1.threshold(prefs, None, H)
        nv = stc1.threshold(prefs, stc1.NAIVE, H)
        tr = stc1.threshold(prefs, stc1.TRAINED, H)
        rows.append({"rsignal": name, "N": n, "independent": ind, "naive": nv, "trained": tr,
                     "naive/independent": nv / ind, "trained/naive": tr / nv})
fig6a = pd.DataFrame(rows)
print(fig6a.round(4).to_string(index=False))
print("\nExpected at N = 2000: naive/independent 5 +- 0.5 (4.5 to 5.5), trained within 10% of naive")
''', ["claim:fig6a-population-thresholds"])
code(r'''
coef_c = fits["c: slopes of the naive fit"]
variants = []
prefs = stc1.uniform_prefs(2000)
for label, kw, cn, ct in [
        ("claims reading (A 30, baseline 10)", {}, stc1.NAIVE, stc1.TRAINED),
        ("A 17, baseline 10", {"amplitude": 17.0}, stc1.NAIVE, stc1.TRAINED),
        ("A 35, baseline 10", {"amplitude": 35.0}, stc1.NAIVE, stc1.TRAINED),
        ("A 30, baseline 2", {"baseline": 2.0}, stc1.NAIVE, stc1.TRAINED),
        ("A 30, baseline 20", {"baseline": 20.0}, stc1.NAIVE, stc1.TRAINED),
        ("no trace term", {"trace": False}, stc1.NAIVE, stc1.TRAINED),
        ("coefficients fitted here (reading c)", {}, tuple(coef_c[[0, 1, 2]]), (coef_c[0], coef_c[1], coef_c[3]))]:
    ind = stc1.threshold(prefs, None, **kw)
    nv = stc1.threshold(prefs, cn, **kw)
    tr = stc1.threshold(prefs, ct, **kw)
    variants.append({"variant (N = 2000, 8 headings)": label, "naive/independent": nv / ind, "trained/naive": tr / nv})
print(pd.DataFrame(variants).round(3).to_string(index=False))
fig, ax = plt.subplots(figsize=(4, 3))
d = fig6a[fig6a.rsignal == "8 headings"]
for col, style in (("independent", "k--"), ("naive", "b-"), ("trained", "r--")):
    ax.loglog(d.N, d[col], style, label=col)
ax.set_xlabel("population size"); ax.set_ylabel("threshold (deg)"); ax.legend(); plt.show()
''', ["claim:fig6a-population-thresholds"])

md('''
## fig6b-slope-not-intercept

> Population thresholds (256 neurons) are very sensitive to the slope of the relation between noise
> and signal correlation and only weakly sensitive to its intercept; a uniform increase in rnoise
> lowers the threshold slightly.

Grid of total slope (a_vestibular + a_visual, the slope on rsignal with congruent tuning) 0 to 0.4
and intercept 0 to 0.2, steps of 0.02 (the grid is the claims file's choice). Every point keeps
rnoise inside [-1, 1].
''')
code(r'''
slopes = np.round(np.arange(0.0, 0.4001, 0.02), 3)
intercepts = np.round(np.arange(0.0, 0.2001, 0.02), 3)
prefs256 = stc1.uniform_prefs(256)
fig6b = {}
for name, H in rsig_readings.items():
    grid = np.array([[stc1.threshold(prefs256, (s, 0.0, b), H) for s in slopes] for b in intercepts])
    fig6b[name] = grid
    slope_m = 0.12 + 0.091
    i_m = np.argmin(np.abs(slopes - 0.22))
    print(f"rsignal over {name}: threshold range over the grid {grid.min():.3f} to {grid.max():.3f} deg")
    for b_label, b in (("0.072 (naive)", 0.072), ("0.005 (trained)", 0.005)):
        row = np.array([stc1.threshold(prefs256, (s, 0.0, b), H) for s in slopes])
        print(f"  over slope 0 to 0.4 at intercept {b_label}: {row.min():.3f} to {row.max():.3f} (change {row.max() - row.min():.3f})")
        lo, hi = stc1.threshold(prefs256, (slope_m - 0.1, 0.0, b), H), stc1.threshold(prefs256, (slope_m + 0.1, 0.0, b), H)
        print(f"  over slope {slope_m - 0.1:.3f} to {slope_m + 0.1:.3f} (width 0.2) at intercept {b_label}: {lo:.3f} to {hi:.3f} (change {abs(hi - lo):.3f})")
    col = np.array([stc1.threshold(prefs256, (slope_m, 0.0, b), H) for b in intercepts])
    print(f"  over intercept 0 to 0.2 (width 0.2) at the measured slope {slope_m}: {col[0]:.3f} to {col[-1]:.3f} (change {col[-1] - col[0]:+.3f});"
          f" decreasing throughout: {bool(np.all(np.diff(col) < 0))}")
    print(f"  at slope 0.4: intercept 0 -> 0.2 changes threshold {grid[0, -1]:.3f} -> {grid[-1, -1]:.3f}")
fig, ax = plt.subplots(figsize=(4.5, 3.2))
cs = ax.contourf(slopes, intercepts, fig6b["8 headings"], 20)
plt.colorbar(cs, label="threshold (deg)")
ax.plot([0.211], [0.072], "bo"); ax.plot([0.211], [0.005], "wo")
ax.set_xlabel("slope"); ax.set_ylabel("intercept"); plt.show()
''', ["claim:fig6b-slope-not-intercept"])

md('''
## fig7a-pair-sign-of-effect

> For a single pair of neurons, reducing noise correlation lowers the discrimination threshold when
> signal correlation is positive and raises it when signal correlation is negative.

One neuron prefers -90 degrees, the other's preference is swept from -90 to 90 in 1 degree steps
(-89.9 for the first, so the two curves differ), tuning as in fig6a.
''')
code(r'''
rows = []
for name, H in rsig_readings.items():
    for p2 in np.arange(-90.0, 90.01, 1.0):
        prefs = np.array([-90.0, p2 if p2 != -90 else -89.9])
        r = stc1.signal_corr(prefs, H)[0, 1]
        rows.append({"rsignal_grid": name, "pref2": p2, "rsignal": r,
                     "naive": stc1.threshold(prefs, stc1.NAIVE, H), "trained": stc1.threshold(prefs, stc1.TRAINED, H)})
fig7a = pd.DataFrame(rows)
fig7a["trained_lower"] = fig7a.trained < fig7a.naive
for name, d in fig7a.groupby("rsignal_grid"):
    pos, neg = d[d.rsignal > 0], d[d.rsignal < 0]
    print(f"{name}: {len(pos)} pairs with rsignal > 0, trained lower in {int(pos.trained_lower.sum())}; "
          f"{len(neg)} with rsignal < 0, trained higher in {int((~neg.trained_lower).sum())}")
    print(f"   trained/naive range, rsignal > 0: {(pos.trained / pos.naive).min():.4f} to {(pos.trained / pos.naive).max():.4f}; "
          f"rsignal < 0: {(neg.trained / neg.naive).min():.4f} to {(neg.trained / neg.naive).max():.4f}")
print(fig7a[fig7a.rsignal_grid == "8 headings"].iloc[::15].round(4).to_string(index=False))
''', ["claim:fig7a-pair-sign-of-effect"])

md('''
## fig7c-narrow-preferences

> In a 256-neuron population, narrowing heading preferences to give more pairs with positive signal
> correlation (49%, 75%, 94%) makes the weaker noise correlations of trained animals improve coding,
> but at best the trained threshold is about 8% lower than the naive.

256 neurons with preferences evenly spaced over ranges centred on 90 degrees, from the full circle
to 10 degrees wide, including [0, 180] and [30, 150] of the Figure 7C legend.
''')
code(r'''
widths = [360, 300, 240, 180, 150, 120, 90, 60, 30, 10]
rows = []
for name, H in rsig_readings.items():
    for w in widths:
        lo, hi = (-180.0, 180.0) if w == 360 else (90 - w / 2, 90 + w / 2)
        prefs = stc1.uniform_prefs(256, lo, hi)
        R = stc1.signal_corr(prefs, H)
        iu = np.triu_indices(256, 1)
        nv, tr = stc1.threshold(prefs, stc1.NAIVE, H), stc1.threshold(prefs, stc1.TRAINED, H)
        rows.append({"rsignal": name, "range": f"[{lo:g}, {hi:g}]", "positive_rsignal_%": 100 * (R[iu] > 0).mean(),
                     "independent": stc1.threshold(prefs, None, H), "naive": nv, "trained": tr,
                     "improvement_%": 100 * (1 - tr / nv)})
fig7c = pd.DataFrame(rows)
print(fig7c.round(3).to_string(index=False))
for name, d in fig7c.groupby("rsignal"):
    print(f"\n{name}: best improvement {d['improvement_%'].max():.2f}% (expected 8 +- 0.8) at {d.loc[d['improvement_%'].idxmax(), 'range']}; "
          f"improvement non-decreasing as the range narrows: {bool(np.all(np.diff(d['improvement_%'].values) >= -1e-9))}")
    print("  positive rsignal at [-180, 180], [0, 180], [30, 150]:",
          d.set_index("range").loc[["[-180, 180]", "[0, 180]", "[30, 150]"], "positive_rsignal_%"].round(1).tolist(), "(expected 49 +- 4.9, 75 +- 7.5, 94 +- 9.4)")
print("\nVariants of the best improvement (8 headings):")
for label, kw in [("A 17, baseline 10", {"amplitude": 17.0}), ("A 30, baseline 2", {"baseline": 2.0}),
                  ("A 30, baseline 20", {"baseline": 20.0}), ("no trace term", {"trace": False})]:
    imp = []
    for w in widths:
        lo, hi = (-180.0, 180.0) if w == 360 else (90 - w / 2, 90 + w / 2)
        prefs = stc1.uniform_prefs(256, lo, hi)
        imp.append(100 * (1 - stc1.threshold(prefs, stc1.TRAINED, **kw) / stc1.threshold(prefs, stc1.NAIVE, **kw)))
    print(f"  {label}: " + ", ".join(f"{w}: {v:.2f}%" for w, v in zip(widths, imp)))
''', ["claim:fig7c-narrow-preferences"])
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && cat > cells5.py <<'EOF'
from cells4 import CELLS, md, code

md('''
## fig8ab-choice-probability-lateral

> Neurons preferring fore-aft headings have smaller choice probabilities than neurons preferring
> lateral headings (p = 0.019, t test), and choice probability does not differ between neurons
> preferring leftward and rightward headings (p = 0.11).

The paper's database has 311 values from single-electrode recordings, vestibular and visual pooled.
The data set holds the choice probabilities of 129 units from two trained monkeys (experiment 2,
Gu et al. 2008, one of the studies the paper draws on), in both conditions: 258 values, a subset
whose overlap with the paper's 311 cannot be checked. Each unit's preferred heading in a condition
comes from its experiment 1 tuning curve of the same condition (the same cells, recorded back to
back), by the two readings of the claims file. Leftward is a preference below 0 degrees (the
paper puts leftward at -90). Whether the leftward-rightward test covers all units or only the
lateral ones is not stated; both are run. Two-sample Student t tests, with Welch as a variant.
''')
code(r'''
rows = []
for u1, u2 in zip(mat["experiment1"].units, mat["experiment2"].units):
    for cond in ("ves", "vis"):
        c1, c2 = getattr(u1, cond), getattr(u2, cond)
        rows.append({"cell": u1.file_id, "monkey": stc1.monkey_of(u1.file_id), "condition": cond, "cp": float(c2.cp),
                     "pref_vector_sum": stc1.pref_vector_sum(c1.stim_global, c1.resp_global),
                     "pref_spline_peak": stc1.pref_spline_peak(c1.stim_global, c1.resp_global)})
cps = pd.DataFrame(rows)
print("Values:", len(cps), "from", cps.cell.nunique(), "units; per monkey and condition:", cps.groupby(["monkey", "condition"]).size().to_dict())
print("CP range", cps.cp.min(), "to", cps.cp.max(), "; missing", int(cps.cp.isna().sum()))
res = []
for reading in ("pref_vector_sum", "pref_spline_peak"):
    grp = stc1.preference_group(cps[reading])
    fa, la = cps.cp[grp == "fore-aft"], cps.cp[grp == "lateral"]
    left_all, right_all = cps.cp[cps[reading] < 0], cps.cp[cps[reading] >= 0]
    lat = cps[grp == "lateral"]
    left_lat, right_lat = lat.cp[lat[reading] < 0], lat.cp[lat[reading] >= 0]
    res.append({"preference": reading, "n_fore_aft": len(fa), "cp_fore_aft": fa.mean(), "n_lateral": len(la), "cp_lateral": la.mean(),
                "p_fa_vs_lat": stats.ttest_ind(fa, la).pvalue, "p_fa_vs_lat_welch": stats.ttest_ind(fa, la, equal_var=False).pvalue,
                "cp_left_all": left_all.mean(), "cp_right_all": right_all.mean(), "n_left_all": len(left_all), "n_right_all": len(right_all),
                "p_left_right_all": stats.ttest_ind(left_all, right_all).pvalue,
                "cp_left_lateral": left_lat.mean(), "cp_right_lateral": right_lat.mean(),
                "p_left_right_lateral": stats.ttest_ind(left_lat, right_lat).pvalue})
fig8ab = pd.DataFrame(res)
print(fig8ab.round(4).T.to_string())
print("\nPer monkey and condition (vector-sum preference): mean CP fore-aft, lateral, t-test p")
for (m, c), d in cps.groupby(["monkey", "condition"]):
    g = stc1.preference_group(d.pref_vector_sum)
    print(f"  monkey {m}, {c}: {d.cp[g == 'fore-aft'].mean():.3f} (n {int((g == 'fore-aft').sum())}), "
          f"{d.cp[g == 'lateral'].mean():.3f} (n {int((g == 'lateral').sum())}), p = {stats.ttest_ind(d.cp[g == 'fore-aft'], d.cp[g == 'lateral']).pvalue:.3f}")
''', ["claim:fig8ab-choice-probability-lateral"])

md('''
## fig8cd-noise-not-preference

> Noise correlation does not depend significantly on heading preference (p = 0.2, t test); lateral
> neurons have slightly smaller noise correlations than fore-aft neurons.

Each pair entered twice, at each unit's preferred heading (the data set's `heading_pref`), with
the pooled rnoise; t test of lateral against fore-aft. Of the claims file's readings, only the
trained pairs under 1 mm (178 points) can be formed from the data set: the other trained pairs, the
pairs over 1 mm and the 55 discrimination-task points are not in it. It is therefore the reading
closest to the legend's 328 and 55 that can be run, and the outcome is judged on it; all 127
pairs (254 points) are shown as a variant.
''')
code(r'''
ut = stc1.unit_table(pairs)
rows = []
for sample, d in (("trained pairs under 1 mm", ut[ut.group == "trained"]), ("all 127 pairs (variant)", ut)):
    for cond in ("vis", "ves"):
        g = stc1.preference_group(d[f"pref_{cond}"])
        fa, la = d.rnoise[g == "fore-aft"], d.rnoise[g == "lateral"]
        rows.append({"sample": sample, "preference": cond, "points": len(d), "n_fore_aft": len(fa), "rnoise_fore_aft": fa.mean(),
                     "sem_fa": fa.sem(), "n_lateral": len(la), "rnoise_lateral": la.mean(), "sem_lat": la.sem(),
                     "p_student": stats.ttest_ind(fa, la).pvalue, "p_welch": stats.ttest_ind(fa, la, equal_var=False).pvalue})
fig8cd = pd.DataFrame(rows)
print(fig8cd.round(4).to_string(index=False))
print("\nPaper: p = 0.2, lateral slightly below fore-aft; Figure 8C legend: 328 fixation and 55 task points")
''', ["claim:fig8cd-noise-not-preference"])
EOF
cat > build.py <<'EOF'
import sys, nbformat
sys.path.insert(0, '.')
from cells5 import CELLS
import cells_end  # noqa: adds conclusions/summary if present
nb = nbformat.v4.new_notebook()
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
for kind, src, tags in CELLS:
    cell = nbformat.v4.new_markdown_cell(src) if kind == "markdown" else nbformat.v4.new_code_cell(src)
    if tags:
        cell.metadata["tags"] = tags
    nb.cells.append(cell)
nbformat.write(nb, sys.argv[1])
print(len(nb.cells), "cells")
EOF
echo "" > cells_end.py
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && uv pip install -q nbformat nbclient ipykernel && cd gen && E=entries/crcns-stc-1-gu-2011 && python build.py $E/reproduce_gu_2011.ipynb && cd $E && time python -c "
import nbformat
from nbclient import NotebookClient
nb=nbformat.read('reproduce_gu_2011.ipynb',4)
NotebookClient(nb,timeout=1200,kernel_name='python3',resources={'metadata':{'path':'.'}}).execute()
nbformat.write(nb, '$TMPDIR/dev.ipynb')
" 2>&1 | tail -20
```

```
45 cells
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.

real	1m35.180s
user	4m48.065s
sys	0m2.081s
```

**Agent**

The full notebook runs without errors in 1.5 minutes. Reading the outputs now.

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && python -c "
import nbformat
nb=nbformat.read('dev.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    print('=====',c.metadata.get('tags'))
    for o in c.outputs:
        if o.output_type=='stream': print(o.text)
        elif o.output_type=='error': print('ERR',o.ename,o.evalue)
"
```

```
===== None
CRCNS stc-1 (unversioned, doi:10.6080/K07P8WKF): MSTd.mat and VIP.mat read and checked against their MD5 sums in 0.9 s

===== ['sanity']
checksums.md5 now lists: {'demo.m': '39b69d14e7663f8c2280b1c26f1da74f', 'docs/crcns_stc-1_data_description.docx': 'df7412a2c15374bae17e46030e4d393c', 'docs/crcns_stc-1_data_description.pdf': '4c7b31c0ba81b3633dcb7efe8525519e', 'filelist.txt': 'fa0527d8ebc46a5b43ddf32c876a7cd4', 'MSTd.mat': 'cd4c13b360aa05689015f1bd2b88a05a', 'VIP.mat': '8d7924e0a1ae86c56b78cd1e2f530e2d'}
MSTd.mat and VIP.mat match the sums pinned in stc1.py: True
Variables in MSTd.mat: ['experiment1', 'experiment2', 'experiment3'] MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Thu Aug 30 10:12:39 2018
experiment1: name 'passive heading', fields ['name', 'units']
experiment2: name 'heading discrimination', fields ['name', 'units', 'behv']
experiment3: name 'passive heading: pairwise recordings', fields ['name', 'pairs']
experiment3.pairs fields: ['file_id', 'ves', 'vis'] ; per condition: ['heading_pref', 'corr_signal', 'corr_noise']
experiment1.units fields: ['file_id', 'ves', 'vis'] ['stim_global', 'resp_global']
experiment2.units fields: ['file_id', 'ves', 'vis', 'com'] ['stim_local', 'resp_local', 'cp', 'thresh'] ; com: ['stim_local', 'resp_local', 'cp', 'thresh']
experiment2.behv.subj: [('2', ['mu']), ('5', ['mu'])]

===== ['sanity']
Pairs in experiment3: 127 (data descriptor: 127 MSTd pairs; paper: 127 pairs under 1 mm)
Missing values: 0

Ranges (correlations are unitless; preferred headings in degrees):
[... 342 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/crcns-stc-1-gu-2011 && . $TMPDIR/scratch/bin/activate && python - <<'EOF'
import numpy as np, stc1
p=stc1.uniform_prefs(256)
for b in np.arange(0,0.2001,0.02): print(round(b,2), round(stc1.threshold(p,(0.211,0,b)),4))
for p2 in np.arange(-5,6,1.0):
    pr=np.array([-90.,p2]); r=stc1.signal_corr(pr,stc1.RSIGNAL_HEADINGS_8)[0,1]
    print(p2, round(r,4), stc1.threshold(pr,stc1.NAIVE), stc1.threshold(pr,stc1.TRAINED))
EOF
```

```
Fri Nov  6 17:06:33 UTC 2026
0.0 7.2201
0.02 7.2536
0.04 7.2411
0.06 7.2261
0.08 7.2103
0.1 7.1939
0.12 7.1772
0.14 7.1602
0.16 7.1428
0.18 7.1252
0.2 7.1072
-5.0 0.0397 25.245282584388583 25.115035258444856
-4.0 0.0229 25.265676296713494 25.170459171014265
-3.0 0.0061 25.274105173999434 25.214496177466465
-2.0 -0.0107 25.2704544110379 25.24685025606105
-1.0 -0.0275 25.254687529346157 25.267297334325722
0.0 -0.0441 25.22684704613417 25.275688845272835
1.0 -0.0608 25.187053887380266 25.271954138106658
2.0 -0.0774 25.13550556146834 25.25610166875776
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && python - <<'EOF'
s=open('cells4.py').read()
old='''    print(f"  at slope 0.4: intercept 0 -> 0.2 changes threshold {grid[0, -1]:.3f} -> {grid[-1, -1]:.3f}")'''
new=old+'''
    print("  threshold at the measured slope by intercept:", dict(zip(intercepts.tolist(), np.round(col, 4).tolist())))
    print(f"  at the trained and naive intercepts (0.005, 0.072): {stc1.threshold(prefs256, (slope_m, 0.0, 0.005), H):.4f}, {stc1.threshold(prefs256, (slope_m, 0.0, 0.072), H):.4f}")'''
assert old in s; s=s.replace(old,new)
old2='''print(fig7a[fig7a.rsignal_grid == "8 headings"].iloc[::15].round(4).to_string(index=False))'''
new2='''exceptions = fig7a[((fig7a.rsignal > 0) & ~fig7a.trained_lower) | ((fig7a.rsignal < 0) & fig7a.trained_lower)]
print("Pairs against the rule:")
print(exceptions.round(4).to_string(index=False))
print(fig7a[fig7a.rsignal_grid == "8 headings"].iloc[::15].round(4).to_string(index=False))'''
assert old2 in s; s=s.replace(old2,new2)
open('cells4.py','w').write(s)
s=open('cells5.py').read()
old='''                     "pref_spline_peak": stc1.pref_spline_peak(c1.stim_global, c1.resp_global)})'''
new='''                     "pref_spline_peak": stc1.pref_spline_peak(c1.stim_global, c1.resp_global),
                     "pref_vector_sum_8": stc1.pref_vector_sum(c1.stim_global[even], c1.resp_global[even])})'''
assert old in s; s=s.replace(old,new)
s=s.replace('''rows = []
for u1, u2 in zip(mat["experiment1"].units''','''rows = []
even = np.isin(mat["experiment1"].units[0].ves.stim_global, np.arange(-180, 180, 45))  # variant: drop +-22.5
for u1, u2 in zip(mat["experiment1"].units''')
s=s.replace('''for reading in ("pref_vector_sum", "pref_spline_peak"):''','''cps["cp_deviation"] = (cps.cp - 0.5).abs()
print("Agreement of the readings' groups: vector sum and spline peak",
      round(float((stc1.preference_group(cps.pref_vector_sum) == stc1.preference_group(cps.pref_spline_peak)).mean()), 3),
      "; vector sum over all 10 and over the 8 evenly spaced headings",
      round(float((stc1.preference_group(cps.pref_vector_sum) == stc1.preference_group(cps.pref_vector_sum_8)).mean()), 3))
for reading in ("pref_vector_sum", "pref_spline_peak", "pref_vector_sum_8"):''')
old='''                "p_left_right_lateral": stats.ttest_ind(left_lat, right_lat).pvalue})'''
new='''                "p_left_right_lateral": stats.ttest_ind(left_lat, right_lat).pvalue,
                "variant_dev_fore_aft": cps.cp_deviation[grp == "fore-aft"].mean(), "variant_dev_lateral": cps.cp_deviation[grp == "lateral"].mean(),
                "variant_p_dev": stats.ttest_ind(cps.cp_deviation[grp == "fore-aft"], cps.cp_deviation[grp == "lateral"]).pvalue})'''
assert old in s; s=s.replace(old,new)
s=s.replace('''lateral ones is not stated; both are run. Two-sample Student t tests, with Welch as a variant.''','''lateral ones is not stated; both are run. Two-sample Student t tests, with Welch as a variant. As
further variants, not readings of the claims file: the vector sum over the 8 evenly spaced
headings only (experiment 1 adds +-22.5 degrees, which pulls a vector sum toward straight ahead),
and the distance of CP from 0.5 (the Figure 8A legend speaks of CPs "more deviated away from the
chance level of 0.5"; the data set does not say in which direction its CPs are signed).''')
open('cells5.py','w').write(s)
EOF
grep -n "stim_global\[even\]" cells5.py | head -2
```

```
32:                     "pref_vector_sum_8": stc1.pref_vector_sum(c1.stim_global[even], c1.resp_global[even])})
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . scratch/bin/activate && cd gen && E=entries/crcns-stc-1-gu-2011 && python build.py $E/reproduce_gu_2011.ipynb && cd $E && python -c "
import nbformat
from nbclient import NotebookClient
nb=nbformat.read('reproduce_gu_2011.ipynb',4)
NotebookClient(nb,timeout=1200,kernel_name='python3',resources={'metadata':{'path':'.'}}).execute()
nbformat.write(nb, '$TMPDIR/dev.ipynb')
for c in nb.cells:
    t=c.metadata.get('tags') or []
    if any(x in str(t) for x in ['fig6b','fig7a','fig8ab']):
        for o in c.outputs:
            if o.output_type=='stream': print(o.text[:4000])
            elif o.output_type=='error': print('ERR',o.ename,o.evalue)
" 2>&1 | grep -v WARNING
```

```
45 cells
rsignal over 8 headings: threshold range over the grid 1.970 to 8.556 deg
  over slope 0 to 0.4 at intercept 0.072 (naive): 2.121 to 8.537 (change 6.416)
  over slope 0.111 to 0.311 (width 0.2) at intercept 0.072 (naive): 6.034 to 8.006 (change 1.971)
  over slope 0 to 0.4 at intercept 0.005 (trained): 2.195 to 8.517 (change 6.322)
  over slope 0.111 to 0.311 (width 0.2) at intercept 0.005 (trained): 6.085 to 8.014 (change 1.929)
  over intercept 0 to 0.2 (width 0.2) at the measured slope 0.211: 7.220 to 7.107 (change -0.113); decreasing throughout: False
  at slope 0.4: intercept 0 -> 0.2 changes threshold 8.370 -> 8.444
  threshold at the measured slope by intercept: {0.0: 7.2201, 0.02: 7.2536, 0.04: 7.2411, 0.06: 7.2261, 0.08: 7.2103, 0.1: 7.1939, 0.12: 7.1772, 0.14: 7.1602, 0.16: 7.1428, 0.18: 7.1252, 0.2: 7.1072}
  at the trained and naive intercepts (0.005, 0.072): 7.2513, 7.2167

rsignal over 1-degree grid: threshold range over the grid 1.970 to 8.556 deg

  over slope 0 to 0.4 at intercept 0.072 (naive): 2.121 to 8.537 (change 6.416)
  over slope 0.111 to 0.311 (width 0.2) at intercept 0.072 (naive): 6.034 to 8.006 (change 1.971)

  over slope 0 to 0.4 at intercept 0.005 (trained): 2.195 to 8.517 (change 6.322)
  over slope 0.111 to 0.311 (width 0.2) at intercept 0.005 (trained): 6.085 to 8.014 (change 1.929)

  over intercept 0 to 0.2 (width 0.2) at the measured slope 0.211: 7.220 to 7.107 (change -0.113); decreasing throughout: False
[... 55 more lines not kept]
```

**Agent**

All the numbers are in. Writing the conclusions and the summary into the notebook.

**Agent calls Bash**

```bash
cd $TMPDIR/gen && cat > cells_end.py <<'EOF'
from cells5 import CELLS

CONCLUSIONS = {
"claim:training-group-link": '''
**Result: reproduced.** The eight monkeys' pair counts (35, 26, 22, 18, 11, 8, 5, 2) equal the eight
counts of the Figure S2B legend, all distinct, so each monkey matches one count. The match gives
89 trained and 38 naive pairs, and 146 trained and 64 naive units, as the paper and the Figure 3
legend state. Monkeys 2 and 5, whose discrimination thresholds the data set holds, fall in the
trained group. The groups rest on the paper's counts. The data set itself does not label them.
''',
"claim:fig2b-trained-lower-noise-correlation": '''
**Result: reproduced, resting on the assumption that the pooled rnoise is the mean of the two
per-condition values.** Trained 0.0241 +- 0.0174 (n = 89) and naive 0.1190 +- 0.0316 (n = 38), both
within tolerance of 0.023 +- 0.017 and 0.116 +- 0.031, Student t test p = 0.0056 (paper 0.006),
Welch p = 0.0108. The visual values alone give the same result (p = 0.0047). The vestibular values
alone do not reach significance (p = 0.071). Leaving out the two-pair animal gives p = 0.0032.
''',
"claim:figs2b-individual-animals": '''
**Result: reproduced for the per-animal means; the time courses cannot be tested.** The pair counts
of the animals shown are 35, 26, 18 and 8 (trained) and 22, 11 and 5 (naive), as in the legend. Every
naive animal's mean (0.0876 to 0.2545) is above every trained animal's mean among the four shown
(-0.0449 to 0.0484). The trained animal with two pairs, not shown in the paper, has a mean of 0.2708.
''',
"claim:fig1-example-pair": '''
**Result: reproduced.** One pair, m2c338r1 (a trained animal), has all four values within
tolerance: rsignal 0.828 visual and 0.786 vestibular, rnoise 0.291 visual and 0.142 vestibular. No
other pair has more than two. The per-pair p values (0.04 and 0.3) need trial counts, which the
data set does not hold.
''',
"claim:fig1f-modality-correlated": '''
**Result: partially reproduced.** Over the 127 pairs under 1 mm (the 179 are not in the data set),
Spearman R = 0.449, p = 1.2e-07. The correlation is positive and significant, but R is outside
0.342 to 0.418.
''',
"claim:fig1f-modality-means-equal": '''
**Result: reproduced.** The paired t test finds no difference (t = 0.346, p = 0.730, n = 127).
Vestibular 0.0559 +- 0.0173 is outside the tolerance of 0.035 +- 0.014, and visual 0.0491 +- 0.0199
is inside 0.039 +- 0.015. The sample is the 127 pairs under 1 mm, not the paper's 179.
''',
"claim:fig5-noise-signal-positive": '''
**Result: reproduced, resting on the pooled-rnoise assumption.** With the pooled rnoise the rsignal
term is significant in both conditions: vestibular p = 0.00017, visual p = 0.00070 (paper 0.0001 and
0.0004), with positive slopes (0.130 and 0.105). With the same-condition rnoise it is also
significant (p = 0.00009 and 0.017). Per monkey, the slopes are positive in 12 of 14 monkey and
condition cells. The two negative cells are both monkey 3, which has 5 pairs.
''',
"claim:fig5-slope-unchanged": '''
**Result: reproduced, resting on the pooled-rnoise assumption.** The interaction of rsignal and
training is not significant: vestibular p = 0.830, visual p = 0.962 (paper 0.9 and 0.9). Per group the
slopes are naive 0.119 [-0.021, 0.259] and trained 0.135 [0.060, 0.210] (vestibular), naive 0.107
[-0.026, 0.240] and trained 0.104 [0.038, 0.170] (visual). With the same-condition rnoise the
interaction p values are 0.630 and 0.894.
''',
"claim:fig5-intercept-lower-trained": '''
**Result: partially reproduced, resting on the pooled-rnoise assumption.** The main effect of
training holds in both conditions with the pooled rnoise (vestibular p = 0.0184, visual p = 0.0074;
paper 0.02 and 0.008). The naive intercepts are higher (0.095 against 0.015, and 0.096 against
0.009). But the 95% intervals of the intercepts overlap under every reading. With separate fits,
vestibular naive is [0.026, 0.163] and trained [-0.018, 0.048]. In the ANCOVA model they are
[0.036, 0.153] and [-0.020, 0.050]. The visual intervals overlap the same way, as do those of the
additive model. With the same-condition rnoise the vestibular main effect is not significant
(p = 0.183).
''',
"claim:fig5-regression-coefficients": '''
**Result: partially reproduced, resting on the pooled-rnoise assumption.** Under reading (a) the
slopes are 0.119 and 0.084, and the naive intercept is 0.077, all within tolerance. The trained
intercept is 0.0034, outside 0.005 +- 0.0005. Its bootstrap interval is [-0.026, 0.035], which
includes 0.005. Reading (b) gives 0.132, 0.085, 0.074 and 0.0024, with the same pattern. Under
reading (c) the visual slope (0.106) is outside tolerance. No reading puts all four values within
tolerance. The slopes match and the naive intercept exceeds the trained one, which the criterion
calls partial. The separate orthogonal fits come close to the paper's two equations
(naive 0.123, 0.106, 0.071; trained intercept 0.0046). The criterion does not list them as a
reading, and they do not share slopes.
''',
"claim:fig6a-population-thresholds": '''
**Result: reproduced, resting on the claims file's tuning amplitude and baseline, which the paper
does not give.** At 2000 neurons the naive threshold is 5.41 times the independent one (4.5 to 5.5),
and the trained threshold is within 0.01% of the naive one, under both rsignal readings. The ratio
depends on the unstated parameters: 4.32 to 5.90 over the amplitude and baseline variants. It is
9.18 without the trace term of equation 3.
''',
"claim:fig6b-slope-not-intercept": '''
**Result: reproduced, resting on the same tuning parameters.** At 256 neurons, changing the slope
over a width of 0.2 around the measured 0.211 changes the threshold by 1.97 degrees (naive
intercept) and 1.93 (trained). Changing the intercept over 0 to 0.2 at the measured slope changes
it by 0.11 degrees. The threshold falls as the intercept rises from 0.02 to 0.2 (7.254 to 7.107), and
from the trained to the naive intercept (7.251 to 7.217). It rises slightly between 0 and 0.02
(7.220 to 7.254).
''',
"claim:fig7a-pair-sign-of-effect": '''
**Result: partially reproduced, resting on the same tuning parameters.** For all 88 pairs with
positive rsignal the trained threshold is lower, and for 92 of 93 with negative rsignal it is
higher. The exception has rsignal = -0.011 (second preference -2 degrees), where trained is 0.09%
lower than naive: the sign changes just below rsignal = 0, not at it. The criterion asks for every
pair.
''',
"claim:fig7c-narrow-preferences": '''
**Result: not reproduced, resting on the same tuning parameters.** The proportions of positive
rsignal are 48.6%, 73.1% and 92.4% for [-180, 180], [0, 180] and [30, 150], all within tolerance.
The trained improvement over naive grows from -0.48% to 4.83% as the range narrows, and then
levels off (4.58% to 4.83%). The largest improvement, 4.83%, is below 8 +- 0.8%. Under the
variants the largest improvement is 3.6% to 6.0% with other amplitudes or baselines, and 11.75%
without the trace term.
''',
"claim:fig8ab-choice-probability-lateral": '''
**Result: not reproduced, on a subset of the paper's data (258 values from 129 units of two trained
monkeys, against 311).** Fore-aft units do not have smaller choice probabilities than lateral ones.
With preferences from the spline peak, fore-aft 0.527 against lateral 0.542, p = 0.136. With the
vector sum, fore-aft 0.546 against lateral 0.511, p = 0.0006, the opposite direction. Leftward and
rightward units do not differ under any reading (p = 0.27 to 0.56), as the paper reports. In the
variants, the vector sum over the 8 evenly spaced headings gives p = 0.691, and the distance of CP
from 0.5 gives p = 0.10 to 0.85. The readings assign units to groups differently: the vector sum
and the spline peak agree for 64% of values.
''',
"claim:fig8cd-noise-not-preference": '''
**Result: reproduced, resting on the pooled-rnoise assumption.** Over the 178 points of the
trained pairs under 1 mm, the reading nearest the legend's counts that the data set allows,
noise correlation does not differ between lateral and fore-aft units. With visual preferences
lateral 0.033 against fore-aft 0.014, p = 0.434. With vestibular preferences lateral 0.011 against
0.045, p = 0.170. Lateral is lower only with vestibular preferences. With all 127 pairs (254 points)
and vestibular preferences, the difference is significant (0.022 against 0.096, p = 0.0009).
''',
}

SUMMARY = '''
## Summary

| Claim | Outcome |
|---|---|
| training-group-link | reproduced |
| fig2b-trained-lower-noise-correlation | reproduced (assumed) |
| figs2b-individual-animals | reproduced (assumed; means only) |
| fig1-example-pair | reproduced |
| fig1f-modality-correlated | partially reproduced (127 of 179 pairs) |
| fig1f-modality-means-equal | reproduced (127 of 179 pairs) |
| fig5-noise-signal-positive | reproduced (assumed) |
| fig5-slope-unchanged | reproduced (assumed) |
| fig5-intercept-lower-trained | partially reproduced (assumed) |
| fig5-regression-coefficients | partially reproduced (assumed) |
| fig6a-population-thresholds | reproduced (assumed) |
| fig6b-slope-not-intercept | reproduced (assumed) |
| fig7a-pair-sign-of-effect | partially reproduced (assumed) |
| fig7c-narrow-preferences | not reproduced (assumed) |
| fig8ab-choice-probability-lateral | not reproduced (subset) |
| fig8cd-noise-not-preference | reproduced (assumed) |
| fig2c, figs2a, fig3 (two claims), figs8c, discussion-stimulus-reduces-correlation | blocked, data missing (no spike times or trial responses) |
| figs1-distance | blocked, data missing (no distances, no pairs over 1 mm) |
| methods-single-vs-multiple-electrodes | blocked, metadata insufficient (no electrode label) |
| fig2a-behavioral-learning | blocked, data missing (no training histories) |
| fig4 (three claims), fig4dh (two claims), figs4 | blocked, data missing (no naive single units) |
| fig7b-msdt-pairs, figs5-congruency | blocked, data missing (no tuning curves of the pair units) |
| figs6-task-independent | blocked, data missing |
| figs8ab-eye-movements | blocked, data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

How the analysis differs from the paper's. The data set holds per-condition noise correlations,
not the pooled one, so the pooled value is taken as the mean of the two. Under that reading the
main result matches the paper to the third decimal. Training groups come from the paper's
per-animal pair counts. Only the 127 pairs under 1 mm are available, where Figure 1F uses 179.
The simulations use a tuning amplitude and baseline that the paper does not give, and the
threshold ratios depend on them. Choice probabilities come from 129 units of two monkeys, not
the paper's 311.

What was found about the data set. It holds derived values only: no spike times, trial
responses, distances, electrode labels or training-group labels, and none of the 52 pairs over
1 mm. The data descriptor lists seven monkeys for the MSTd pairs. The files name eight,
including monkey 24 with two pairs. One recording (m19c21r1) has six pairs from four units,
where the paper states a maximum of five pairs per experiment. How the preferred headings
were computed is not described. The pairs are internally consistent (units per recording,
rsignal against the preference difference) and match the paper's group counts of pairs and
units.
'''

def _insert():
    for tag, text in CONCLUSIONS.items():
        idx = max(i for i, c in enumerate(CELLS) if c[2] and tag in c[2])
        CELLS.insert(idx + 1, ("markdown", text.strip("\n"), None))
    CELLS.append(("markdown", SUMMARY.strip("\n"), None))

_insert()
EOF
python - <<'EOF'
import re
t=open('/tmp/x','w') if False else None
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/gen && E=entries/crcns-stc-1-gu-2011 && $TMPDIR/scratch/bin/python build.py $E/reproduce_gu_2011.ipynb && cat > $E/requirements.in <<'EOF'
aiohttp
fsspec
matplotlib
numpy
pandas
requests
scipy
statsmodels
EOF
cat > $E/entry.yaml <<'EOF'
schema_version: 1
name: crcns-stc-1-gu-2011
type: reproduction
title: Perceptual learning and noise correlations in MSTd (Gu et al. 2011)
description: Tests the findings of Gu, Liu, Fetsch, Yang, Fok, Sunkara, DeAngelis and Angelaki
  (2011) on CRCNS stc-1, which holds the noise and signal correlations and preferred headings of the
  paper's 127 MSTd pairs under 1 mm, and single-unit tuning and choice probabilities of two trained
  monkeys. It compares noise correlations between naive and trained animals, their relation to
  signal correlation, and the paper's population simulations. Analyses that need spike times,
  distances or the single-electrode database cannot be run on it.
license: Apache-2.0
notebooks:
- path: reproduce_gu_2011.ipynb
  title: Reproducing Gu et al. (2011) from CRCNS stc-1
  runtime_minutes: 2
helpers:
- stc1.py
related:
- id: crcns:stc-1/unversioned
  relation: uses_data
- id: doi:10.1016/j.neuron.2011.06.015
  relation: reproduces
EOF
cat $TMPDIR/../ 2>/dev/null; python -c "import json;s=json.load(open('schemas/entry.schema.json'));print(list(s['properties']), s.get('required'))"
```

```
62 cells
['schema_version', 'name', 'type', 'title', 'description', 'license', 'notebooks', 'helpers', 'related'] ['schema_version', 'name', 'type', 'title', 'description', 'license', 'notebooks', 'related']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u && python tools/entry.py lock entries/crcns-stc-1-gu-2011 2>&1 | tail -5 && python tools/entry.py check entries/crcns-stc-1-gu-2011 2>&1 | tail -20
```

```
Fri Nov  6 17:09:27 UTC 2026
wrote entries/crcns-stc-1-gu-2011/requirements.lock.txt
0 error(s)
```

**Agent**

Lock and check pass. Now the attempt record and README.

**Agent calls Write**

```json
{
 "file_path": "attempts/crcns-stc-1-gu-2011-01.yaml",
 "content": "schema_version: 2\nid: crcns-stc-1-gu-2011-01\ndataset:\n  archive: crcns\n  id: stc-1\n  version: unversioned\n  doi: 10.6080/K07P8WKF\npaper: doi:10.1016/j.neuron.2011.06.015\ndate: 2026-11-06\nentry: crcns-stc-1-gu-2011\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-13\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/42256343726\ninputs:\n- what: Training group of each monkey, from the per-animal pair counts of the paper's Figure S2B\n    legend (trained 35, 26, 18, 8 and 2 pairs, naive 22, 11 and 5). The paper itself, used to label\n    the monkeys the data set names; no measurement comes from it.\n  source: doi:10.1016/j.neuron.2011.06.015 (Supplemental Information, Figure S2 legend)\noutcomes:\n- claim: training-group-link\n  outcome: reproduced\n  notebook: reproduce_gu_2011.ipynb\n  output: claim:training-group-link\n  notes: Monkeys are matched by their number of pairs. The eight counts in the data (35, 26, 22, 18,\n    11, 8, 5, 2) equal the eight of the Figure S2B legend, all distinct, so the match is one to one,\n    with monkeys 19, 18, 2, 5 and 24 trained and 17, 1 and 3 naive. It gives 89 trained and 38 naive\n    pairs, and 146 trained and 64 naive units (units told apart within a recording by their\n    preferred headings), as the paper and the Figure 3 legend state. Monkeys 2 and 5, whose\n    heading discrimination thresholds the data set holds in experiment 2, are trained.\n  deviations:\n  - The data set has no training-group label; the groups come from the paper's per-animal counts.\n- claim: fig2b-trained-lower-noise-correlation\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_gu_2011.ipynb\n  output: claim:fig2b-trained-lower-noise-correlation\n  measured:\n  - 0.0241\n  - 0.119\n  - 89\n  - 38\n  notes: Trained 0.0241 +- 0.0174 SEM (n = 89), naive 0.1190 +- 0.0316 (n = 38), both within the\n    reported SEMs; Student t test p = 0.0056 (paper 0.006), Welch p = 0.0108. Visual rnoise alone\n    gives p = 0.0047, vestibular alone p = 0.071. Without the trained animal with two pairs, p =\n    0.0032.\n  deviations:\n  - Assumed that the pooled rnoise is the mean of the vestibular and visual rnoise. The data set\n    holds only the per-condition values; the Experimental Procedures (Noise and Signal Correlations,\n    paragraph 2) pool the z-scored responses across conditions, and the correlation of pooled\n    z-scores is the trial-weighted mean of the per-condition correlations, with equal weights when\n    the conditions are interleaved with equal repetitions (Experimental Protocol and Task). Outlier\n    removal could make the weights differ slightly.\n  - Whether the stored values include the renormalization in blocks of 20 trials cannot be told,\n    and the reading with the other choice cannot be run, as the data set holds no trial responses.\n  - Training groups from the link claim.\n- claim: figs2b-individual-animals\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_gu_2011.ipynb\n  output: claim:figs2b-individual-animals\n  measured:\n  - 35\n  - 22\n  notes: Pair counts 35, 26, 18, 8 (trained shown) and 22, 11, 5 (naive) match the legend. Every\n    naive animal mean (0.0876 to 0.2545) exceeds every trained animal mean among those shown (-0.0449\n    to 0.0484). The trained animal with two pairs, not shown in the paper, has a mean of 0.2708. The\n    per-animal time courses of Figure S2B need spike times and are not tested.\n  deviations:\n  - Pooled rnoise as the mean of the two conditions (assumption, as in fig2b).\n  - Means over the middle 1 s only; the figure shows time courses.\n- claim: fig1-example-pair\n  outcome: reproduced\n  notebook: reproduce_gu_2011.ipynb\n  output: claim:fig1-example-pair\n  measured:\n  - 0.828\n  - 0.786\n  - 0.291\n  - 0.142\n  notes: Pair m2c338r1 (monkey 2, trained) has all four values within tolerance; no other pair has\n    more than two. The per-pair p values (0.04 and 0.3) need trial counts, which the data set does\n    not hold, so that part of the statement is not tested.\n- claim: fig1f-modality-correlated\n  outcome: partially_reproduced\n  notebook: reproduce_gu_2011.ipynb\n  output: claim:fig1f-modality-correlated\n  measured: 0.449\n  notes: Spearman R = 0.449, p = 1.2e-07, over 127 pairs; positive and significant, but outside 0.342\n    to 0.418. Trained 0.395 (n = 89), naive 0.480 (n = 38).\n  deviations:\n  - The 127 pairs under 1 mm, the criterion's second reading; the paper's 179 are not in the data\n    set.\n- claim: fig1f-modality-means-equal\n  outcome: reproduced\n  notebook: reproduce_gu_2011.ipynb\n  output: claim:fig1f-modality-means-equal\n  measured:\n  - 0.0559\n  - 0.0491\n  notes: Paired t = 0.346, p = 0.730, n = 127; mean difference 0.0068, 95% CI -0.032 to 0.046. The\n    vestibular mean (0.0559 +- 0.0173) is outside 0.035 +- 0.014; the visual mean (0.0491 +- 0.0199)\n    is inside 0.039 +- 0.015.\n  deviations:\n  - The 127 pairs under 1 mm, not the paper's 179.\n- claim: fig5-noise-signal-positive\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_gu_2011.ipynb\n  output: claim:fig5-noise-signal-positive\n  notes: With pooled rnoise the rsignal term has vestibular p = 0.00017 and visual p = 0.00070 (Type\n    II, model with interaction; the additive model gives 0.00016 and 0.00066), slopes 0.130 and\n    0.105. With the same-condition rnoise p = 0.00009 and 0.017. Per monkey, the slopes are\n    positive in 12 of 14 monkey and condition cells; the two negative ones are monkey 3 (5 pairs).\n  deviations:\n  - Pooled rnoise as the mean of the two conditions (assumption, as in fig2b).\n  - The paper does not say how the ANCOVA sums of squares are formed; Type II tests with and\n    without the interaction are shown and agree.\n- claim: fig5-slope-unchanged\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_gu_2011.ipynb\n  output: claim:fig5-slope-unchanged\n  notes: Interaction p = 0.830 (vestibular) and 0.962 (visual) with pooled rnoise; 0.630 and 0.894\n    with the same-condition rnoise. Slopes, vestibular, naive 0.119 (95% CI -0.021 to 0.259) and\n    trained 0.135 (0.060 to 0.210); visual, naive 0.107 (-0.026 to 0.240) and trained 0.104 (0.038\n    to 0.170).\n  deviations:\n  - Pooled rnoise as the mean of the two conditions (assumption, as in fig2b).\n- claim: fig5-intercept-lower-trained\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_gu_2011.ipynb\n  output: claim:fig5-intercept-lower-trained\n  notes: The training main effect holds with pooled rnoise (vestibular p = 0.0184, visual p =\n    0.0074; paper 0.02 and 0.008), with higher naive intercepts (0.095 against 0.015, 0.096 against\n    0.009). The 95% intervals of the intercepts overlap under every reading. Vestibular, separate\n    fits give naive 0.026 to 0.163 and trained -0.018 to 0.048; the ANCOVA model gives 0.036 to 0.153\n    and -0.020 to 0.050. Visual is alike, as is the additive model. With the same-condition rnoise\n    the vestibular main effect is not significant (p = 0.183).\n  deviations:\n  - Pooled rnoise as the mean of the two conditions (assumption, as in fig2b).\n  - The paper does not say how the intercept intervals of Figure 5D were computed; separate\n    per-group fits, the ANCOVA model with interaction (Figure 5 legend, \"regression fits (ANCOVA)\")\n    and the additive model are all shown, and all overlap.\n- claim: fig5-regression-coefficients\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_gu_2011.ipynb\n  output: claim:fig5-regression-coefficients\n  measured:\n  - 0.1191\n  - 0.0838\n  - 0.0769\n  - 0.0034\n  notes: Reading (a) gives slopes 0.119 and 0.084 and naive intercept 0.077, within tolerance, and\n    trained intercept 0.0034, outside 0.005 +- 0.0005 (bootstrap 95% interval -0.026 to 0.035).\n    Reading (b) gives 0.132, 0.085, 0.074 and 0.0024; reading (c) puts the visual slope (0.106)\n    outside tolerance. No reading has all four within tolerance; the slopes match and the naive\n    intercept exceeds the trained one under (a) and (b). Separate orthogonal fits per group give\n    naive 0.123, 0.106 and 0.071 and a trained intercept of 0.0046, close to the paper's\n    equations but with different slopes per group, which is not a reading of the criterion.\n  deviations:\n  - Pooled rnoise as the mean of the two conditions (assumption, as in fig2b).\n- claim: fig6a-population-thresholds\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_gu_2011.ipynb\n  output: claim:fig6a-population-thresholds\n  measured: 5.41\n  notes: At 2000 neurons the naive threshold is 5.41 times the independent one, and trained is\n    within 0.01% of naive, under both rsignal readings, which give the same values. The ratio is\n    4.32 to 5.90 over the amplitude and baseline variants, and 9.18 without the trace term of\n    equation 3. With the coefficients fitted here (reading c) it is 5.47.\n  deviations:\n  - Tuning amplitude 30 spikes/s, baseline 10 spikes/s and a 1 s count are the claims file's\n    readings; the paper does not give them, and the ratio depends on them.\n  - Preferences evenly spaced on the circle, a standard choice for the legend's \"uniformly\n    distributed\".\n- claim: fig6b-slope-not-intercept\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_gu_2011.ipynb\n  output: claim:fig6b-slope-not-intercept\n  notes: At 256 neurons a slope change of 0.2 around the measured 0.211 changes the threshold by\n    1.97 degrees (naive intercept) and 1.93 (trained), an intercept change over 0 to 0.2 at the\n    measured slope by 0.11. The threshold falls as the intercept rises from 0.02 to 0.2 (7.254 to\n    7.107) and from the trained to the naive intercept (7.251 to 7.217), with a small rise from 0\n    to 0.02 (7.220 to 7.254).\n  deviations:\n  - Tuning parameters as in fig6a (claims file readings, not from the paper).\n  - The slope axis is taken as the sum of the two slopes, the slope on rsignal when tuning is\n    congruent, as the Results assume for the simulations.\n- claim: fig7a-pair-sign-of-effect\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_gu_2011.ipynb\n  output: claim:fig7a-pair-sign-of-effect\n  notes: Trained is lower than naive for all 88 pairs with positive rsignal and higher for 92 of 93\n    with negative rsignal. The exception, at rsignal = -0.011, has trained 0.09% below naive; the\n    sign changes just below rsignal = 0. The criterion asks for every pair.\n  deviations:\n  - Tuning parameters as in fig6a (claims file readings, not from the paper).\n- claim: fig7c-narrow-preferences\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_gu_2011.ipynb\n  output: claim:fig7c-narrow-preferences\n  measured:\n  - 4.83\n  - 48.6\n  - 73.1\n  - 92.4\n  notes: The proportions of positive rsignal are within tolerance. The trained improvement grows\n    from -0.48% to 4.83% as the range narrows and then levels off (4.58% to 4.83%); its maximum,\n    4.83%, is below 8 +- 0.8%. The maximum is 3.6% to 6.0% under the amplitude and baseline\n    variants and 11.75% without the trace term of equation 3.\n  deviations:\n  - Tuning parameters as in fig6a (claims file readings, not from the paper); the result depends on\n    them and on the trace term.\n  - Ranges centred on 90 degrees with widths 360 to 10 degrees, containing the legend's [0, 180] and\n    [30, 150]; the figure's other ranges are not given in the text.\n- claim: fig8ab-choice-probability-lateral\n  outcome: not_reproduced\n  notebook: reproduce_gu_2011.ipynb\n  output: claim:fig8ab-choice-probability-lateral\n  notes: On 258 values from 129 units of monkeys 2 and 5, fore-aft units do not have smaller\n    choice probabilities. With spline-peak preferences, fore-aft 0.527 against lateral 0.542, p =\n    0.136. With the vector sum, 0.546 against 0.511, p = 0.0006, the opposite direction. Leftward\n    and rightward units do not differ under any reading (p = 0.27 to 0.56), as the paper says.\n    Variants, the vector sum over the 8 evenly spaced headings gives p = 0.691, and the distance of\n    CP from 0.5 gives p = 0.10 to 0.85. The vector sum and spline readings put 64% of values in the\n    same group.\n  deviations:\n  - A subset of the paper's data. The data set holds the choice probabilities of 129 units of two\n    trained monkeys from Gu et al. (2008), 258 values over the two conditions, against the paper's\n    311; whether they are among the 311 cannot be checked.\n  - Preferred headings from the experiment 1 tuning curves of the same cells, by the two readings of\n    the claims file; the data set does not say how its CPs are signed.\n- claim: fig8cd-noise-not-preference\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_gu_2011.ipynb\n  output: claim:fig8cd-noise-not-preference\n  notes: Over the 178 points of the trained pairs under 1 mm, lateral against fore-aft p = 0.434\n    with visual preferences (0.033 against 0.014) and p = 0.170 with vestibular preferences (0.011\n    against 0.045). Lateral is lower only with vestibular preferences. Variant with all 127 pairs\n    (254 points), vestibular preferences give a significant difference (0.022 against 0.096, p =\n    0.0009), visual do not (p = 0.623).\n  deviations:\n  - Of the claims file's readings only the trained pairs under 1 mm can be formed (178 points, the\n    legend has 328 and 55); the other trained pairs, the pairs over 1 mm and the task points are not\n    in the data set.\n  - Pooled rnoise as the mean of the two conditions (assumption, as in fig2b); preferred headings\n    as stored in the data set, whose method is not described.\n- claim: fig2c-timecourse-naive-higher\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs spike times in 500 ms windows. The data set (stc-1/live, MSTd.mat, VIP.mat, demo.m and\n    the docs) holds one noise correlation per pair and condition, no spike times or trial responses.\n- claim: figs2a-difference-decreases\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig2c-timecourse-naive-higher; no spike times in the data set.\n- claim: fig3-mean-response-unchanged\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs spike times of the pair units; the data set holds none.\n- claim: fig3-fano-unchanged\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs spike counts per trial and window; the data set holds none.\n- claim: figs8c-renormalization\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs trial-ordered responses to renormalize; the data set holds one value per pair and\n    condition, without saying whether it includes the renormalization.\n- claim: discussion-stimulus-reduces-correlation\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs prestimulus spike counts; the data set holds none.\n- claim: figs1-distance\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The data set holds only the 127 pairs under 1 mm, none of the 52 pairs over 1 mm, and no\n    distance or electrode label, so neither the third group nor the split of the first two can be\n    formed.\n- claim: methods-single-vs-multiple-electrodes\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: No pair carries an electrode label. Ten file_ids of monkey 17 end in \"s\", which the data\n    descriptor does not explain; the paper's 67 single-electrode pairs cannot be identified. The 52\n    pairs over 1 mm, needed for the reading over all 179 pairs, are not in the data set either.\n- claim: fig2a-behavioral-learning\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The training histories are not in the data set. Experiment 2 holds one threshold per\n    animal for two of the five trained monkeys (vestibular 1.2 and 3.1 degrees, both inside 0.9 to\n    3.3), not the thresholds over sessions the criterion fits.\n- claim: fig4-tuning-width-visual\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The single-electrode database of 992 and 556 neurons is not in the data set. Experiment 1\n    holds the tuning curves of 129 units of two trained monkeys only, so naive and trained cannot be\n    compared.\n- claim: fig4-tuning-width-vestibular\n  outcome: blocked\n  blocked_by: data_missing\n  notes: As fig4-tuning-width-visual.\n- claim: fig4-amplitude-unchanged\n  outcome: blocked\n  blocked_by: data_missing\n  notes: As fig4-tuning-width-visual.\n- claim: fig4dh-lateral-more-sensitive\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The criterion's factorial ANOVA needs naive and trained neurons from the single-electrode\n    database; the data set holds 129 units of two trained monkeys only.\n- claim: fig4dh-training-no-sensitivity-change\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Depends on fig4dh-lateral-more-sensitive; no naive single units in the data set.\n- claim: figs4-population-sensitivity-any-reference\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the naive and trained single-electrode database; only 129 trained units are in the\n    data set.\n- claim: fig7b-msdt-pairs\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the tuning curves of each pair's units; the pairs carry only rsignal and preferred\n    headings. Seven pair recordings share a cell id with experiment 1 units, but the data set does\n    not say which pair unit, if any, those curves belong to.\n- claim: figs5-congruency\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The congruency index is the correlation of each unit's visual and vestibular tuning\n    curves, which the data set does not hold for the pair units.\n- claim: figs6-task-independent\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Noise correlations during the discrimination task are not in the data set.\n- claim: figs8ab-eye-movements\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Eye position records are not in the data set.\nfindings:\n- kind: data_missing\n  statement: The data set holds derived values only. For the paper's pairs there are no spike times\n    or trial responses, no interneuronal distances, none of the 52 pairs over 1 mm, no\n    discrimination-task correlations and no eye records; the single-electrode database of Figures\n    4, S4 and 8A is represented only by 129 units of two trained monkeys, and the training histories\n    of Figure 2A by one threshold for each of two monkeys. Twenty of the 34 claims of the paper\n    cannot be tested.\n- kind: metadata_insufficient\n  statement: No pair or monkey carries a naive or trained label, which every comparison in the\n    paper needs. The groups can be recovered here only because the paper's per-animal pair counts\n    are all distinct and match the counts per monkey in the file_ids.\n- kind: metadata_insufficient\n  statement: No pair carries an electrode or distance label, and ten file_ids of monkey 17 end in\n    \"s\" without explanation, so the single-electrode and multi-electrode pairs cannot be told\n    apart.\n- kind: metadata_insufficient\n  statement: The data descriptor does not say how heading_pref was computed, how cp is signed\n    (relative to the unit's preferred direction or to a fixed choice), or the units of resp_global\n    (demo.m labels them spikes/s).\n- kind: metadata_error\n  statement: The data descriptor lists monkeys 1, 2, 3, 5, 17, 18 and 19 for the 127 MSTd pairs; the\n    file_ids name an eighth, monkey 24, with two pairs, the trained animal with two pairs of the\n    paper's Figure S2B.\n- kind: other\n  statement: Recording m19c21r1 holds six pairs from four units, where the paper states a maximum of\n    five pairs in an experiment (Experimental Procedures, Electrophysiological Recordings).\n- kind: methods_unavailable\n  statement: Question for the paper's authors. Is the pooled rnoise of Figure 2B and Figure 5 the\n    correlation of z-scores pooled over both conditions (which the mean of the two per-condition\n    values in the data set approximates, matching 0.023 and 0.116 to the third decimal), and do the\n    stored per-condition values include the renormalization in blocks of 20 trials?\n- kind: methods_unavailable\n  statement: Question for the paper's authors. What tuning amplitude, baseline and counting window\n    were used in the simulations of Figures 6 and 7, and was the trace term of equation 3 included?\n    With amplitude 30 and baseline 10 spikes/s over 1 s and the trace term, the naive threshold is\n    5.4 times the independent one at 2000 neurons, but the best trained improvement in Figure 7C is\n    4.8%, not 8%; without the trace term it is 9.2 times and up to 11.8%.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. How were the 95% intervals of the intercepts in\n    Figure 5D computed? Separate per-group fits, the ANCOVA model with interaction and the\n    common-slope model all give overlapping intervals on the 127 pairs of the data set.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. For Figure 8A and 8B, how was each unit's preferred\n    heading computed, which units entered the 311 values, and how was CP signed? On the 129 units of\n    the data set the fore-aft and lateral CPs differ in opposite directions under the vector sum and\n    the spline peak.\n"
}
```

```
File created successfully at: attempts/crcns-stc-1-gu-2011-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sed -i 's/Twenty of the 34 claims of the paper/Nineteen of the paper'"'"'s 34 claims/' attempts/crcns-stc-1-gu-2011-01.yaml && python - <<'EOF'
import yaml,re
p='attempts/crcns-stc-1-gu-2011-01.yaml'
d=yaml.safe_load(open(p))
def walk(x):
    if isinstance(x,dict):
        for v in x.values(): yield from walk(v)
    elif isinstance(x,list):
        for v in x: yield from walk(v)
    elif isinstance(x,str): yield x
bad=[s for s in walk(d) if ': ' in s]
print(bad)
print(len(d['outcomes']), {o['outcome'] for o in d['outcomes']})
import collections; print(collections.Counter(o['outcome'] for o in d['outcomes']))
c=yaml.safe_load(open('claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml'))
print(set(x['id'] for x in c['claims'])^set(o['claim'] for o in d['outcomes']))
EOF
grep -n "Nineteen" attempts/crcns-stc-1-gu-2011-01.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "entries/crcns-stc-1-gu-2011/README.md",
 "content": "# Gu, Liu, Fetsch, Yang, Fok, Sunkara, DeAngelis & Angelaki (2011) from CRCNS stc-1\n\nTests the findings of [Gu et al. (2011)](https://doi.org/10.1016/j.neuron.2011.06.015) that can be\ntested on [CRCNS stc-1](https://doi.org/10.6080/K07P8WKF). The data set holds derived values: the\nnoise and signal correlations and preferred headings of the paper's 127 MSTd pairs under 1 mm, and\nthe tuning curves and choice probabilities of 129 single units of two trained monkeys. It holds no\nspike times, distances, training-group labels or naive single units.\n\n| Claim | Outcome |\n|---|---|\n| The monkeys can be assigned to the naive and trained groups by their pair counts | Reproduced |\n| Noise correlation is lower in trained than in naive animals (Figure 2B) | Reproduced |\n| The difference holds in each animal (means; Figure S2B) | Reproduced |\n| The example pair of Figure 1 | Reproduced |\n| Visual and vestibular noise correlations are correlated (Figure 1F) | Partially reproduced |\n| Visual and vestibular means do not differ (Figure 1F) | Reproduced |\n| Noise correlation rises with signal correlation (Figure 5) | Reproduced |\n| Training does not change the slope (Figure 5C) | Reproduced |\n| Training lowers the intercept, with non-overlapping intervals (Figure 5D) | Partially reproduced |\n| The plane of equation 5 | Partially reproduced |\n| Correlations raise the population threshold 5-fold; training has little effect (Figure 6A) | Reproduced |\n| Thresholds depend on the slope more than the intercept (Figure 6B) | Reproduced |\n| For a pair, reducing correlations helps when rsignal > 0 and hurts when < 0 (Figure 7A) | Partially reproduced |\n| At best the trained threshold is about 8% lower (Figure 7C) | Not reproduced |\n| Fore-aft units have smaller choice probabilities (Figure 8A, 8B) | Not reproduced |\n| Noise correlation does not depend on heading preference (Figure 8C, 8D) | Reproduced |\n| Time courses, Fano factors, renormalization, prestimulus correlations | Blocked: data missing |\n| Distance groups, single against multiple electrodes | Blocked: data missing, metadata insufficient |\n| Training histories, single-electrode database (Figures 2A, 4, S4) | Blocked: data missing |\n| Pair tuning curves, task correlations, eye movements (Figures 7B, S5, S6, S8A, S8B) | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nMost outcomes rest on one assumption: the data set holds per-condition noise correlations, and the\npaper's pooled value is taken as their mean. Under it the main result matches the paper to the third\ndecimal. The simulations use a tuning amplitude and baseline that the paper does not give. The\nattempt record, with the reasons and the differences from the paper's method, is\n[`attempts/crcns-stc-1-gu-2011-01.yaml`](../../attempts/crcns-stc-1-gu-2011-01.yaml).\n\n- `reproduce_gu_2011.ipynb`: the analysis. It takes about two minutes.\n- `stc1.py`: loading the data set with its MD5 check, the pairs table, the group assignment, and\n  the Fisher information of equations 2 to 5. Other notebooks on this data set can import it.\n"
}
```

```
File created successfully at: entries/crcns-stc-1-gu-2011/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; python tools/entry.py all entries/crcns-stc-1-gu-2011 2>&1 | tail -15
```

```
Fri Nov  6 17:11:08 UTC 2026
Installed kernelspec registry-crcns-stc-1-gu-2011 in executed/crcns-stc-1-gu-2011/.venv/share/jupyter/kernels/registry-crcns-stc-1-gu-2011
0 error(s)
pass  reproduce_gu_2011.ipynb  (99 s)
```

**Agent**

Lock, check and run pass (99 s). Confirming the executed copy's numbers still match the conclusions.

**Agent calls Bash**

```bash
ls executed/crcns-stc-1-gu-2011/; cd executed/crcns-stc-1-gu-2011 && python3 - <<'EOF'
import json
nb=json.load(open('reproduce_gu_2011.ipynb'))
import re
txt=''
for c in nb['cells']:
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if o.get('output_type')=='error': print('ERROR', o['ename'])
            txt+=''.join(o.get('text',''))
for key in ['p_student','0.0056','m2c338r1','R = 0.449','p = 0.730','5.4087','4.83%','0.1363','0.4342','0.0034','0.8297','0.9622']:
    print(key, key in txt)
EOF
```

```
reproduce_gu_2011.ipynb
result.json
p_student True
0.0056 True
m2c338r1 True
R = 0.449 True
p = 0.730 True
5.4087 True
4.83% True
0.1363 True
0.4342 True
0.0034 True
0.8297 False
0.9622 False
```

**Agent**

Interaction p values print as 0.82968 and 0.962 (dict rounding), matching the 0.830 and 0.962 I cite. Running the handover.

**Agent calls Bash**

```bash
cd  && python tools/entry.py handover entries/crcns-stc-1-gu-2011 2>&1 | tail -5; ls executed/crcns-stc-1-gu-2011/handover; python tools/entry.py check entries/crcns-stc-1-gu-2011 | tail -2; git status --short; date -u
```

```
wrote executed/crcns-stc-1-gu-2011/handover
10.1016-j.neuron.2011.06.015.yaml
reproduce_gu_2011.ipynb
stc1.py
0 error(s)
 M claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml
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
?? attempts/crcns-stc-1-gu-2011-01.yaml
?? entries/crcns-stc-1-gu-2011/
?? scripts
Fri Nov  6 17:13:20 UTC 2026
```

**Agent**

The handover is built. Some untracked dotfiles (`.bashrc`, `.idea`, `scripts` and others) appeared at the repo root. Checking what they are before I report.

**Agent calls Bash**

```bash
ls -la .bashrc .profile .gitconfig .mcp.json scripts .idea .vscode 2>&1 | head -20
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 16:51 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 16:51 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 16:51 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 16:51 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 16:51 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 16:51 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Nov  6 16:51 scripts
```

**Agent**

I tested 16 of the 35 claims (15 of the paper's findings plus one link claim I added); the other 19 are blocked, because the dataset holds only per-pair summary values. The entry passes `lock`, `check` and `all`: the notebook ran from a clean environment in 99 s, and I confirmed the executed numbers match the conclusions. The handover package is built in `executed/crcns-stc-1-gu-2011/handover/`.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| training-group-link (added by me) | reproduced |
| fig2b-trained-lower-noise-correlation | reproduced (assumed): 0.0241 vs 0.119, p = 0.0056 (paper 0.023, 0.116, p = 0.006) |
| figs2b-individual-animals | reproduced (assumed; per-animal means only) |
| fig1-example-pair | reproduced (pair m2c338r1) |
| fig1f-modality-correlated | partially reproduced (R = 0.449 on 127 pairs; tolerance 0.342 to 0.418) |
| fig1f-modality-means-equal | reproduced (paired p = 0.73) |
| fig5-noise-signal-positive | reproduced (assumed) |
| fig5-slope-unchanged | reproduced (assumed) |
| fig5-intercept-lower-trained | partially reproduced (assumed): the training effect holds, but the intercept 95% intervals overlap |
| fig5-regression-coefficients | partially reproduced (assumed): trained intercept 0.0034, outside 0.005 ± 0.0005 |
| fig6a-population-thresholds | reproduced (assumed): ratio 5.41 |
| fig6b-slope-not-intercept | reproduced (assumed) |
| fig7a-pair-sign-of-effect | partially reproduced (assumed): 180 of 181 pairs follow the rule |
| fig7c-narrow-preferences | not reproduced (assumed): best improvement 4.83%, expected 8 ± 0.8 |
| fig8ab-choice-probability-lateral | not reproduced, on a subset (129 units from 2 monkeys, against the paper's 311) |
| fig8cd-noise-not-preference | reproduced (assumed) |
| 19 other claims | blocked: 18 `data_missing`, 1 `metadata_insufficient` (single vs multiple electrodes) |

**2. Dataset, assumptions, questions**

- **Version:** CRCNS is unversioned. I pinned `stc-1/live/` because the bucket holds only that copy of the data (`orig/` has just an older description document). The notebook checks the files against the dataset's own MD5 sums.
- **What it holds:** per-pair noise and signal correlations per condition and preferred headings for the 127 pairs under 1 mm, plus tuning curves and choice probabilities for 129 units from 2 trained monkeys. There are no spike times, distances, electrode labels, training-group labels, pairs over 1 mm or naive single units.
- **Training groups:** these come from the paper's per-animal pair counts (Figure S2B legend). The counts are all distinct and match the dataset one to one. The match also gives the paper's 146 and 64 neurons, and monkeys 2 and 5, which have discrimination thresholds in the file, come out as trained.
- **Findings:**
  - The data descriptor leaves out monkey 24 (2 pairs).
  - Recording m19c21r1 holds 6 pairs, where the paper says at most 5 per experiment.
  - Ten file IDs end in "s" with no explanation.
  - How `heading_pref` was computed and how `cp` is signed are not documented.
- **Main assumption:** I took the pooled noise correlation to be the mean of the two per-condition values. It follows from z-scoring when both conditions have equal trial counts, and it reproduces 0.023 and 0.116 to the third decimal.
- **Simulation parameters:** the tuning amplitude and baseline come from the claims file, not the paper, and the results depend on them.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - Is the pooled correlation the mean of the two conditions, and is the renormalization included?
  - Which amplitude, baseline and counting window did the simulations use, and did they include the trace term of equation 3?
  - How were the Figure 5D intercept intervals computed?
  - For Figure 8A, how were preferred headings and the sign of choice probability defined?
- **Questions to a reader:** none.

**3. Protocol gaps**

1. Link claims are framed around outside data. Here the labels came from the paper itself, so I recorded the paper's DOI under `inputs` and marked the link `with_labels`.
2. Adding the link claim meant adding `depends_on` to 7 existing claims. The protocol requires it, but it touches a claims file the author is otherwise told not to change. I changed nothing else.
3. The rule that every data stream must share the trial clock does not apply to a dataset of summary values only. I said so in the data check.
4. The protocol gives no category for "testable on a subset that may not be the paper's sample" (fig8ab). I tested it and named the subset in the deviations.
5. The criteria give no outcome for "all but one" (fig7a, 180 of 181) or for a mixed result without a partial rule. I chose `partially_reproduced` and gave the exact counts.
6. For fig8cd the claims file's preferred reading needs pairs that are not in the dataset. I judged it on the closest reading the data allow (178 points).
7. archives.md describes CRCNS zips; these files are plain `.mat`. I streamed them into memory with fsspec.

**4. Runtime and failures**

The work took about 25 minutes (16:53 to 17:13 UTC). The notebook runs in 99 s. Nothing failed. Some untracked files at the repo root (`.bashrc`, `.idea`, `scripts` and others) are sandbox device mounts created before I started; I left them alone. I did not commit or push.

## End of run

55 turns, 19 minutes, $4.78 at API prices, result: success.
