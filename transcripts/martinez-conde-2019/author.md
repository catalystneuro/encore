# martinez-conde-2019 · author · run 43699045378

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  ls; cat docs/protocol.md; ls entries/fouke-2025 paper claims attempts | head -50
```

```
<persisted-output>
Output too large (40.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/5dab85ce-1834-411c-91af-bfb914e14918/tool-results/bkf7tj1tt.txt

Preview (first 2KB):
Sun Nov 15 09:30:40 UTC 2026
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
[... 46 more lines not kept]
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
3	Version: `pilot-15`. Record this version in the attempt's provenance.
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
[... 657 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/martinez-conde-2019.yaml; ls paper; ls entries/martinez-conde-2019 attempts | grep -i martinez; ls questions | grep -i mart; cat papers/datasets/martinez-conde-2019.yaml
```

```
<persisted-output>
Output too large (30.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/5dab85ce-1834-411c-91af-bfb914e14918/tool-results/bzg3mtkxq.txt

Preview (first 2KB):
# Claims for Martinez-Conde, McCamy, Troncoso, Otero-Millan & Macknik (2019), PLoS ONE 14(3)
# e0210941, tested on CRCNS pvc-12.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
#
# Text read: the version of record, PMC6438452 (open access), from the Europe PMC full text XML
# (paper/10.1371-journal.pone.0210941.txt): main text, Materials and methods, figure legends,
# Table 1, and the legends of the supporting information (S1 to S4 Fig, S1 and S2 Table). The
# supplementary files themselves are not in the text. S1 Table (exact p-values of Fig 4B) and
# S2 Table (the t-tests of Fig 7C, with confidence intervals and t-statistics) are missing, so
# the claims record only the bounds and statements the main text gives. The reference list is
# not in the text either, so reference [3] (the DOG model output of Fig 7D) cannot be named
# beyond its number. The paper links no analysis code; none was read.
#
# Data the paper used (Materials and methods; Results, paragraphs 1 to 4). Two adult rhesus
# monkeys (Macaca mulatta, one male, one female; monkey J and monkey A). 118 V1 single units
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/martinez-conde-2019.yaml"
}
```

```
1	# Claims for Martinez-Conde, McCamy, Troncoso, Otero-Millan & Macknik (2019), PLoS ONE 14(3)
2	# e0210941, tested on CRCNS pvc-12.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
4	# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
5	#
6	# Text read: the version of record, PMC6438452 (open access), from the Europe PMC full text XML
7	# (paper/10.1371-journal.pone.0210941.txt): main text, Materials and methods, figure legends,
8	# Table 1, and the legends of the supporting information (S1 to S4 Fig, S1 and S2 Table). The
9	# supplementary files themselves are not in the text. S1 Table (exact p-values of Fig 4B) and
10	# S2 Table (the t-tests of Fig 7C, with confidence intervals and t-statistics) are missing, so
11	# the claims record only the bounds and statements the main text gives. The reference list is
12	# not in the text either, so reference [3] (the DOG model output of Fig 7D) cannot be named
13	# beyond its number. The paper links no analysis code; none was read.
14	#
15	# Data the paper used (Materials and methods; Results, paragraphs 1 to 4). Two adult rhesus
16	# monkeys (Macaca mulatta, one male, one female; monkey J and monkey A). 118 V1 single units
17	# recorded (102 from J, 16 from A), 60 discarded before analysis, 58 analysed. Each neuron was
18	# tested in one to three conditions during a guided-viewing task (fixation cross jumping over a
19	# grid, 2x2 DVA window). Conditions, with the corner-fold aligned to the neuron's preferred
20	# orientation: Square and Edge (25 neurons; folds P180 (flat gradient) and S90, plus the Edge),
[... 507 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -la paper entries/martinez-conde-2019 attempts | head -80; cat papers/datasets/martinez-conde-2019.yaml; ls questions; cat README.md | head -100
```

```
ls: cannot access 'entries/martinez-conde-2019': No such file or directory
attempts:
total 19916
drwxr-xr-x  2 runner runner  16384 Nov 15 09:30 .
drwxr-xr-x 21 runner runner   4096 Nov 15 09:30 ..
-rw-r--r--  1 runner runner  35216 Nov 15 09:24 amjad-2025-01.yaml
-rw-r--r--  1 runner runner  46897 Nov 15 09:24 andrews-2024-01.yaml
-rw-r--r--  1 runner runner  80255 Nov 15 09:24 armstrong-2026-01.yaml
-rw-r--r--  1 runner runner  71222 Nov 15 09:24 asari-2009-01.yaml
-rw-r--r--  1 runner runner  87848 Nov 15 09:24 ashworth-2025-01.yaml
-rw-r--r--  1 runner runner  56714 Nov 15 09:24 athalye-2023-01.yaml
-rw-r--r--  1 runner runner  45219 Nov 15 09:24 azcorra-2023-01.yaml
-rw-r--r--  1 runner runner  93014 Nov 15 09:24 bech-2026-01.yaml
-rw-r--r--  1 runner runner  89121 Nov 15 09:24 bellvila-2026-01.yaml
-rw-r--r--  1 runner runner  83955 Nov 15 09:24 bennett-2024-01.yaml
-rw-r--r--  1 runner runner  64022 Nov 15 09:24 berg-2020-01.yaml
-rw-r--r--  1 runner runner  47276 Nov 15 09:24 boran-2022-01.yaml
-rw-r--r--  1 runner runner  50541 Nov 15 09:24 bouabid-2026-01.yaml
-rw-r--r--  1 runner runner  51001 Nov 15 09:24 bouchard-2013-01.yaml
-rw-r--r--  1 runner runner  42792 Nov 15 09:24 brezovec-2022-01.yaml
[... 328 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -la paper; sed -n '/CRCNS/,/^## /p' docs/archives.md | head -120
```

```
total 88
drwxr-xr-x  2 runner runner  4096 Nov 15 09:30 .
drwxr-xr-x 21 runner runner  4096 Nov 15 09:30 ..
-rw-r--r--  1 runner runner 69698 Nov 15 09:30 10.1371-journal.pone.0210941.txt
-rw-r--r--  1 runner runner  5938 Nov 15 09:30 pvc-12.data-description.txt
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
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat paper/pvc-12.data-description.txt; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=pvc-12/" | python -c "import sys,re; t=sys.stdin.read(); [print(k,s) for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',t)]"
```

Result: the fetched text is not kept.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1371-journal.pone.0210941.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  for f in checksums.md5 filelist.txt; do curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-12/live/$f; echo; done; ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  which python; python -c "import fsspec, scipy, numpy, aiohttp, openpyxl; print('ok')"; cat entries/fouke-2025/README.md; cat attempts/fouke-2025-01.yaml | head -150
```

```
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fsspec, scipy, numpy, aiohttp, openpyxl; print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'fsspec'
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
[... 170 more lines not kept]
```

**Agent**

Set up a scratch environment to survey the zip.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q scratch && source scratch/bin/activate && uv pip install -q fsspec aiohttp requests scipy numpy openpyxl pandas matplotlib h5py statsmodels 2>&1 | tail -3; python - <<'EOF'
import fsspec, zipfile
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-12/live/V1_Vasarely_data.zip"
f=fsspec.open(url,block_size=2**20).open()
z=zipfile.ZipFile(f)
names=z.infolist()
print(len(names))
for i in names: print(i.filename, i.file_size, i.compress_size)
EOF
```

```
159
V1_Vasarely_data/ 0 0
V1_Vasarely_data/Edge-compare/ 0 0
V1_Vasarely_data/Edge-compare/AEC071800J1_Stimulus.mat 66795 49061
V1_Vasarely_data/Edge-compare/AEC071800J1_SpikeRateMap.mat 3306113 3301691
V1_Vasarely_data/Edge-compare/AEC070300J2_SpikeRateMap.mat 1538141 1533928
V1_Vasarely_data/Edge-compare/AEC072000J1_SpikeRateMap.mat 1851894 1850356
V1_Vasarely_data/Edge-compare/AEC07240J1C_SpikeRateMap.mat 2729444 2720371
V1_Vasarely_data/Edge-compare/AEC09010J1C_SpikeRateMap.mat 2409386 2398283
V1_Vasarely_data/Edge-compare/AEC09040J3B_SpikeRateMap.mat 371991 364008
V1_Vasarely_data/Edge-compare/AEC070600J2_SpikeRateMap.mat 1815467 1812835
V1_Vasarely_data/Edge-compare/AEC071200J1_SpikeRateMap.mat 1770882 1768208
V1_Vasarely_data/Edge-compare/AEC071000J4_Stimulus.mat 70242 49374
V1_Vasarely_data/Edge-compare/AEC042500J2_Stimulus.mat 92614 77736
V1_Vasarely_data/Edge-compare/AEC070300J1_Stimulus.mat 119904 104322
V1_Vasarely_data/Edge-compare/AEC070600J1_Stimulus.mat 117330 99072
V1_Vasarely_data/Edge-compare/AEC08080J3C_Stimulus.mat 92960 76606
V1_Vasarely_data/Edge-compare/AEC070400A1_Stimulus.mat 99228 80799
V1_Vasarely_data/Edge-compare/AEC08100J2C_Stimulus.mat 96699 82668
V1_Vasarely_data/Edge-compare/AEC071200J1_Stimulus.mat 78147 60437
[... 141 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
import fsspec, zipfile, io, collections, pandas as pd, scipy.io as sio, numpy as np
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-12/live/V1_Vasarely_data.zip"
f=fsspec.open(url,block_size=2**20).open()
z=zipfile.ZipFile(f)
c=collections.Counter()
for i in z.namelist():
    p=i.split('/')
    if len(p)==3 and p[2]: c[(p[1],p[2].split('_')[1])]+=1
print(c)
x=pd.read_excel(io.BytesIO(z.read('V1_Vasarely_data/V1_Vasarely_data_SMC.xlsx')),sheet_name=None,header=None)
for k,v in x.items():
    print(k,v.shape); pd.set_option('display.width',250); pd.set_option('display.max_rows',200); pd.set_option('display.max_columns',50); print(v.to_string())
for nm in ['V1_Vasarely_data/Edge-compare/AEC071800J1_SpikeRateMap.mat','V1_Vasarely_data/Edge-compare/AEC071800J1_Stimulus.mat']:
    m=sio.loadmat(io.BytesIO(z.read(nm)),squeeze_me=True,struct_as_record=False)
    d=m['dat']; print(nm, d._fieldnames)
    for fn in d._fieldnames:
        a=getattr(d,fn); print(fn, type(a), getattr(a,'dtype',None), getattr(a,'shape',None), np.nanmin(a), np.nanmax(a), np.isnan(a).sum() if a.dtype.kind=='f' else '')
EOF
```

```
Exit code 1
Counter({('Star', 'Stimulus.mat'): 29, ('Star', 'SpikeRateMap.mat'): 29, ('Corners', 'SpikeRateMap.mat'): 26, ('Corners', 'Stimulus.mat'): 26, ('Edge-compare', 'Stimulus.mat'): 22, ('Edge-compare', 'SpikeRateMap.mat'): 22})
Sheet1 (63, 6)
     0   1         2        3     4             5
0  NaN NaN       NaN      NaN   NaN           NaN
1  NaN NaN       NaN      NaN   NaN           NaN
2  NaN NaN       NaN      NaN   NaN           NaN
3  NaN NaN       NaN      NaN   NaN           NaN
4  NaN NaN      Cell  Corners  Star  Edge-Compare
5  NaN NaN  041900J2        X   NaN           NaN
6  NaN NaN  042000J1        X   NaN           NaN
7  NaN NaN  042400J2        X   NaN           NaN
8  NaN NaN  042500J2      NaN   NaN             X
9  NaN NaN  042600J2        X   NaN           NaN
10 NaN NaN  042700J2        X     X           NaN
11 NaN NaN  042800J2        X   NaN           NaN
12 NaN NaN  050800J1      NaN   NaN           NaN
13 NaN NaN  050900J1        X   NaN           NaN
14 NaN NaN  051000J3        X     X           NaN
15 NaN NaN  051500J1        X   NaN           NaN
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
import fsspec, zipfile, io, scipy.io as sio, numpy as np
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-12/live/V1_Vasarely_data.zip"
z=zipfile.ZipFile(fsspec.open(url,block_size=2**20).open())
def show(nm):
    m=sio.loadmat(io.BytesIO(z.read(nm)),squeeze_me=True,struct_as_record=False)
    print(nm, [k for k in m if not k.startswith('__')])
    d=m['dat']; 
    for fn in d._fieldnames:
        a=getattr(d,fn)
        if isinstance(a,np.ndarray) and a.dtype.kind in 'fiub':
            fa=a.astype(float); print(' ',fn, a.dtype, a.shape, np.nanmin(fa), np.nanmax(fa), 'nan',np.isnan(fa).sum(), 'sum',np.nansum(fa), 'nonzero',(fa!=0).sum())
        else: print(' ',fn, type(a), repr(a)[:300])
for nm in ['V1_Vasarely_data/Edge-compare/AEC071800J1_SpikeRateMap.mat','V1_Vasarely_data/Edge-compare/AEC071800J1_Stimulus.mat','V1_Vasarely_data/Star/ABD071800J1_SpikeRateMap.mat','V1_Vasarely_data/Star/ABD071800J1_Stimulus.mat','V1_Vasarely_data/Corners/ABC071800J1_SpikeRateMap.mat','V1_Vasarely_data/Corners/ABC071800J1_Stimulus.mat','V1_Vasarely_data/Star/ABS042700J2_Stimulus.mat','V1_Vasarely_data/Star/ABS042700J2_SpikeRateMap.mat']:
    show(nm)
EOF
```

```
Exit code 1
V1_Vasarely_data/Edge-compare/AEC071800J1_SpikeRateMap.mat ['dat']
  norm <class 'int'> 0
  image <class 'scipy.sparse._csc.csc_array'> <Compressed Sparse Column sparse array of dtype 'float64'
	with 13609 stored elements and shape (480, 640)>
  smoothed_image float64 (480, 640) 0.0 0.048585291116370485 nan 0 sum 806.9030358097484 nonzero 152876
  Standard <class 'scipy.io.matlab._mio5_params.mat_struct'> <scipy.io.matlab._mio5_params.mat_struct object at 0x75a5dec6f950>
  smoothed_image_norm float64 (480, 640) -0.08008065261765629 1.4848628497970164 nan 0 sum 1389.757563385082 nonzero 307200
V1_Vasarely_data/Edge-compare/AEC071800J1_Stimulus.mat ['dat']
  EdgecompImage float64 (480, 640) 0.0 100.0 nan 0 sum 1668721.2121212124 nonzero 35650
  SquareVert <class 'numpy.ndarray'> array([<scipy.io.matlab._mio5_params.mat_struct object at 0x75a5de8ffbd0>,
       <scipy.io.matlab._mio5_params.mat_struct object at 0x75a5de8ffb50>,
       <scipy.io.matlab._mio5_params.mat_struct object at 0x75a5de8ffad0>,
       <scipy.io.matlab._mio5_params.mat_struct object at 0x75a5de8ffa50>,

  RectVert <class 'numpy.ndarray'> array([<scipy.io.matlab._mio5_params.mat_struct object at 0x75a5de965850>,
       <scipy.io.matlab._mio5_params.mat_struct object at 0x75a5de9658d0>,
       <scipy.io.matlab._mio5_params.mat_struct object at 0x75a5de965950>,
       <scipy.io.matlab._mio5_params.mat_struct object at 0x75a5de9659d0>,

[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
import fsspec, zipfile, io, scipy.io as sio, numpy as np, h5py
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-12/live/V1_Vasarely_data.zip"
z=zipfile.ZipFile(fsspec.open(url,block_size=2**20).open())
def ld(nm): return sio.loadmat(io.BytesIO(z.read(nm)),squeeze_me=True,struct_as_record=False)['dat']
def desc(o,ind='  ',depth=0):
    if hasattr(o,'_fieldnames'):
        for fn in o._fieldnames:
            a=getattr(o,fn)
            print(ind+fn, end=': ')
            if hasattr(a,'_fieldnames'): print(); desc(a,ind+'  ',depth+1)
            elif isinstance(a,np.ndarray) and a.dtype==object:
                print('objarray',a.shape); 
                for k,e in enumerate(a[:2]): print(ind+'  [%d]'%k); desc(e,ind+'    ',depth+1)
            elif isinstance(a,np.ndarray) and a.size>20: print(a.dtype,a.shape,np.nanmin(a),np.nanmax(a))
            else: print(repr(a)[:200])
d=ld('V1_Vasarely_data/Edge-compare/AEC071800J1_SpikeRateMap.mat')
im=d.image.toarray(); print('image sum',im.sum(),'max',im.max(),'unique',np.unique(im)[:10])
desc(d.Standard)
for nm in ['V1_Vasarely_data/Edge-compare/AEC071800J1_Stimulus.mat','V1_Vasarely_data/Star/ABD071800J1_Stimulus.mat','V1_Vasarely_data/Corners/ABC071800J1_Stimulus.mat']:
    print(nm); s=ld(nm); 
    for fn in s._fieldnames:
        a=getattr(s,fn)
        if isinstance(a,np.ndarray) and a.dtype==object:
            print(fn,len(a)); desc(a[0]); desc(a[-1])
h=h5py.File(io.BytesIO(z.read('V1_Vasarely_data/Star/ABS042700J2_Stimulus.mat')),'r')
h.visit(print)
h=h5py.File(io.BytesIO(z.read('V1_Vasarely_data/Star/ABS042700J2_SpikeRateMap.mat')),'r')
h.visit(print)
EOF
```

```
Exit code 1
image sum 808.449745373719 max 1.0 unique [0.         0.00097087 0.00097847 0.00106838 0.00111732 0.00112867
 0.00114025 0.00116822 0.00118483 0.00119048]
  image: float64 (337, 151) 0.0 0.8346649298015734
  smoothed_image: float64 (337, 151) 0.0006874043755376391 0.03353222199754746
  EdgecompVert: 
    SquareVert: objarray (100,)
      [0]
        x: array([145.71067812,  75.        ,   4.28932188,  75.        ])
        y: array([257.64466094, 186.93398282, 257.64466094, 328.35533906])
      [1]
        x: array([144.99642884,  75.        ,   5.00357116,  75.        ])
        y: array([257.64466094, 187.6482321 , 257.64466094, 327.64108979])
    RectVert: objarray (100,)
      [0]
        x: array([ 75.,  75., 345., 345.])
        y: array([157.64466094,   7.64466094,   7.64466094, 157.64466094])
      [1]
        x: array([ 75.,  75., 345., 345.])
        y: array([156.12950943,   7.64466094,   7.64466094, 156.12950943])
[... 298 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && time python - <<'EOF'
import fsspec, zipfile, io, scipy.io as sio, numpy as np, h5py, pickle, time
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-12/live/V1_Vasarely_data.zip"
z=zipfile.ZipFile(fsspec.open(url,block_size=2**20).open())
out={}
for nm in z.namelist():
    if not nm.endswith('.mat'): continue
    b=z.read(nm)
    try:
        d=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)['dat']
        out[nm]=('v5',d)
    except NotImplementedError:
        out[nm]=('h5',b)
    except Exception as e:
        out[nm]=('err',repr(e),b[:200])
pickle.dump({k:v for k,v in out.items()},open('all.pkl','wb'))
for k,v in out.items():
    if v[0]!='v5': print(k,v[0],v[1][:120] if v[0]=='err' else '')
EOF
```

```
V1_Vasarely_data/Star/ABS042700J2_Stimulus.mat h5 
V1_Vasarely_data/Star/ABS051000J3_Stimulus.mat h5 
V1_Vasarely_data/Star/ABS051000J3_SpikeRateMap.mat h5 

real	0m15.638s
user	0m3.284s
sys	0m0.889s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && rm -f all.pkl && source scratch/bin/activate && cat > survey.py <<'EOF'
import fsspec, zipfile, io, scipy.io as sio, numpy as np, h5py
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-12/live/V1_Vasarely_data.zip"
z=zipfile.ZipFile(fsspec.open(url,block_size=2**20).open())
def ld(nm):
    b=z.read(nm)
    try: return sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)['dat']
    except NotImplementedError: return h5py.File(io.BytesIO(b),'r')
EOF
python - <<'EOF'
exec(open('survey.py').read())
for nm in sorted(z.namelist()):
    if not nm.endswith('SpikeRateMap.mat'): continue
    d=ld(nm)
    if isinstance(d,h5py.File):
        print(nm.split('/')[-2:],'H5', list(d['dat'].keys())); continue
    S=d.Standard
    im=d.image.toarray() if hasattr(d.image,'toarray') else d.image
    print(nm.split('/')[-1][:12], d._fieldnames==['norm','image','smoothed_image','Standard','smoothed_image_norm'], 'norm',d.norm, 'imgsum %.1f max %.3f'%(im.sum(),im.max()), 'sm max %.4f'%d.smoothed_image.max(), 'nrm [%.3f %.3f]'%(d.smoothed_image_norm.min(),d.smoothed_image_norm.max()), S._fieldnames, S.image.shape, 'Snrm [%.3f %.3f]'%(S.smoothed_image_norm.min(),S.smoothed_image_norm.max()), 'base %.5f'%S.BaseActivity)
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 9, in <module>
AttributeError: 'mat_struct' object has no attribute 'smoothed_image_norm'. Did you mean: 'smoothed_image'?
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
exec(open('survey.py').read())
import numpy as np
def g(o,f): 
    a=getattr(o,f,None); 
    if a is None: return None
    return a.toarray() if hasattr(a,'toarray') else a
for nm in sorted(z.namelist()):
    if not nm.endswith('SpikeRateMap.mat'): continue
    d=ld(nm)
    if isinstance(d,h5py.File):
        print(nm.split('/')[-1],'H5', list(d['dat'].keys())); continue
    S=getattr(d,'Standard',None)
    im=g(d,'image'); sm=g(d,'smoothed_image'); nr=g(d,'smoothed_image_norm')
    s=f"{nm.split('/')[-1][:12]} {d._fieldnames} img {im.shape} sum {im.sum():.1f} max {im.max():.3f} sm {sm.max()*1000:.1f}"
    if nr is not None: s+=f" nrm[{nr.min():.3f},{nr.max():.3f}]"
    if S is not None:
        s+=f" S{S._fieldnames} {S.image.shape}"
        if hasattr(S,'BaseActivity'): s+=f" base {S.BaseActivity*1000:.2f}"
    print(s)
EOF
```

```
ABC041900J2_ ['norm', 'image', 'smoothed_image', 'Standard'] img (480, 640) sum 1682.0 max 1.000 sm 78.8 S['image', 'smoothed_image', 'CornersVert'] (273, 209)
ABC042000J1_ ['norm', 'image', 'smoothed_image', 'Standard', 'smoothed_image_norm'] img (480, 640) sum 2693.9 max 1.000 sm 125.9 nrm[-1.000,0.998] S['image', 'smoothed_image', 'CornersVert', 'smoothed_image_norm', 'BaseActivity'] (273, 209) base 0.11
ABC042400J2_ ['norm', 'image', 'smoothed_image', 'Standard', 'smoothed_image_norm'] img (480, 640) sum 214.4 max 1.000 sm 29.7 nrm[-1.000,0.977] S['image', 'smoothed_image', 'CornersVert', 'smoothed_image_norm', 'BaseActivity'] (273, 209) base 0.35
ABC042600J2_ ['norm', 'image', 'smoothed_image', 'Standard', 'smoothed_image_norm'] img (480, 640) sum 1112.5 max 1.000 sm 79.7 nrm[-1.000,0.793] S['image', 'smoothed_image', 'CornersVert', 'smoothed_image_norm', 'BaseActivity'] (273, 209) base 9.20
ABC042700J2_ ['norm', 'image', 'smoothed_image', 'Standard', 'smoothed_image_norm'] img (480, 640) sum 901.0 max 1.000 sm 41.0 nrm[-1.000,0.537] S['image', 'smoothed_image', 'CornersVert', 'smoothed_image_norm', 'BaseActivity'] (273, 209) base 12.34
ABC042800J2_ ['norm', 'image', 'smoothed_image', 'Standard', 'smoothed_image_norm'] img (480, 640) sum 511.2 max 1.000 sm 44.5 nrm[-1.000,0.825] S['image', 'smoothed_image', 'CornersVert', 'smoothed_image_norm', 'BaseActivity'] (273, 209) base 4.27
ABC050900J1A ['norm', 'image', 'eyetime', 'smoothed_image', 'Standard', 'smoothed_image_norm'] img (480, 640) sum 610.5 max 1.000 sm 42.9 nrm[-0.000,0.043] S['image', 'smoothed_image', 'CornersVert', 'smoothed_image_norm', 'BaseActivity'] (273, 209) base 0.10
ABC051000J3_ ['norm', 'image', 'smoothed_image', 'Standard', 'smoothed_image_norm'] img (480, 640) sum 367.8 max 1.000 sm 59.3 nrm[nan,nan] S['image', 'smoothed_image', 'CornersVert', 'smoothed_image_norm', 'BaseActivity'] (273, 209) base 0.00
ABC051500J1_ ['norm', 'image', 'smoothed_image', 'Standard', 'smoothed_image_norm'] img
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
exec(open('survey.py').read())
import numpy as np
from scipy.ndimage import correlate
from scipy.signal import convolve2d
def fspecial(n,s):
    x=np.arange(n)-(n-1)/2; g=np.exp(-(x[:,None]**2+x[None,:]**2)/(2*s*s)); return g/g.sum()
K=fspecial(16,7)
for nm in ['V1_Vasarely_data/Edge-compare/AEC071800J1_SpikeRateMap.mat','V1_Vasarely_data/Star/ABD071200J1_SpikeRateMap.mat','V1_Vasarely_data/Corners/ABC050900J1A_SpikeRateMap.mat']:
    d=ld(nm); im=d.image.toarray()
    sm=d.smoothed_image
    c=convolve2d(im,K,mode='same')
    print(nm, 'conv same maxabs diff', np.abs(c-sm).max(), 'rel', np.abs(c-sm).max()/sm.max())
    for sh in [(0,0),(1,0),(0,1),(1,1),(-1,-1)]:
        cc=np.roll(c,sh,(0,1)); print(sh, np.abs(cc-sm)[20:-20,20:-20].max()/sm.max())
    if hasattr(d,'eyetime'):
        et=d.eyetime; et=et.toarray() if hasattr(et,'toarray') else et
        print('eyetime',et.shape,et.min(),et.max(),et.sum(), np.unique(et)[:10])
        nz=et>0; cnt=im*et; print('count from image*eyetime', cnt.sum(), np.abs(cnt[nz]-np.round(cnt[nz])).max())
EOF
```

```
Sun Nov 15 09:33:31 UTC 2026
V1_Vasarely_data/Edge-compare/AEC071800J1_SpikeRateMap.mat conv same maxabs diff 0.01415489860858872 rel 0.29134123277526935
(0, 0) 0.29134123277526935
(1, 0) 0.3356374014521868
(0, 1) 0.33070148915536735
(1, 1) 0.37477698270963616
(-1, -1) 0.18986681315360232
V1_Vasarely_data/Star/ABD071200J1_SpikeRateMap.mat conv same maxabs diff 0.00903691241171426 rel 0.3626037178545028
(0, 0) 0.3626037178545028
(1, 0) 0.41042167713199784
(0, 1) 0.48491747591060064
(1, 1) 0.495474292932406
(-1, -1) 0.2616717154926122
V1_Vasarely_data/Corners/ABC050900J1A_SpikeRateMap.mat conv same maxabs diff 0.01347446140628921 rel 0.3140001001746122
(0, 0) 0.3140001001746122
(1, 0) 0.3422874971278406
(0, 1) 0.3669525419273012
(1, 1) 0.3645017245303021
(-1, -1) 0.26652470332475203
eyetime (480, 640) 0.0 1504.0 1165423.0 [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
exec(open('survey.py').read())
import numpy as np
from scipy.signal import convolve2d
def fspecial(n,s):
    x=np.arange(n)-(n-1)/2; g=np.exp(-(x[:,None]**2+x[None,:]**2)/(2*s*s)); return g/g.sum()
d=ld('V1_Vasarely_data/Corners/ABC050900J1A_SpikeRateMap.mat')
im=d.image.toarray(); et=d.eyetime; sm=d.smoothed_image
cnt=im*et; vis=(et>0).astype(float)
for n,s in [(16,7),(17,7),(15,7),(16,7.0)]:
    K=fspecial(n,s)
    C=lambda a: convolve2d(a,K,mode='same')
    cands={'conv(img)':C(im),'conv(cnt)/conv(et)':C(cnt)/np.maximum(C(et),1e-12),'conv(img)/conv(vis)':C(im)/np.maximum(C(vis),1e-12)}
    for k,v in cands.items():
        m=(sm>0)
        print(n,s,k, np.abs(v-sm)[m].max()/sm.max(), np.corrcoef(v[m],sm[m])[0,1])
print('sm zeros',(sm==0).sum(),'vis zeros',(vis==0).sum())
print(d.smoothed_image_norm.min(), d.smoothed_image_norm.max(), d.Standard.BaseActivity)
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 12, in <module>
  File "<stdin>", line 11, in <lambda>
  File "/tmp/claude-1001/scratch/lib/python3.13/site-packages/scipy/signal/_signaltools.py", line 1842, in convolve2d
    raise ValueError('convolve2d inputs must both be 2-D arrays')
ValueError: convolve2d inputs must both be 2-D arrays
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
exec(open('survey.py').read())
import numpy as np
from scipy.signal import convolve2d
def fspecial(n,s):
    x=np.arange(n)-(n-1)/2; g=np.exp(-(x[:,None]**2+x[None,:]**2)/(2*s*s)); return g/g.sum()
d=ld('V1_Vasarely_data/Corners/ABC050900J1A_SpikeRateMap.mat')
im=np.asarray(d.image.toarray(),float); et=d.eyetime; et=np.asarray(et.toarray() if hasattr(et,'toarray') else et,float); sm=d.smoothed_image
cnt=im*et; vis=(et>0).astype(float)
for n,s in [(16,7),(17,7),(15,7)]:
    K=fspecial(n,s)
    C=lambda a: convolve2d(a,K,mode='same')
    cands={'conv(img)':C(im),'conv(cnt)/conv(et)':C(cnt)/np.maximum(C(et),1e-12),'conv(img)/conv(vis)':C(im)/np.maximum(C(vis),1e-12)}
    for k,v in cands.items():
        m=(sm>0)
        print(n,s,k, np.abs(v-sm)[m].max()/sm.max(), np.corrcoef(v[m],sm[m])[0,1])
print('sm zeros',(sm==0).sum(),'vis zeros',(vis==0).sum())
print(d.smoothed_image_norm.min(), d.smoothed_image_norm.max(), d.Standard.BaseActivity)
EOF
```

```
16 7 conv(img) 0.3140001001746122 0.9734031032609848
16 7 conv(cnt)/conv(et) 23.303122488366505 -0.08224945727329949
16 7 conv(img)/conv(vis) 23.303122488366505 -0.017734798175983682
17 7 conv(img) 0.31605451622028574 0.9788442478098651
17 7 conv(cnt)/conv(et) 23.288286174345345 -0.1102692530641308
17 7 conv(img)/conv(vis) 23.288286174345345 -0.05251148582639506
15 7 conv(img) 0.21354618208334025 0.9853710958513152
15 7 conv(cnt)/conv(et) 23.288286174345345 -0.07924755626267305
15 7 conv(img)/conv(vis) 23.288286174345345 -0.005672831456496666
sm zeros 190421 vis zeros 298211
-9.580344399502106e-05 0.04281648033806811 9.580344399502106e-05
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
exec(open('survey.py').read())
import numpy as np
from scipy.signal import fftconvolve
def fspecial(n,s):
    x=np.arange(n)-(n-1)/2; g=np.exp(-(x[:,None]**2+x[None,:]**2)/(2*s*s)); return g/g.sum()
d=ld('V1_Vasarely_data/Corners/ABC050900J1A_SpikeRateMap.mat')
im=np.asarray(d.image.toarray(),float); sm=d.smoothed_image
best=[]
for n in range(8,50,2):
  for s in [3,4,5,6,7,8,10,12,14]:
    full=fftconvolve(im,fspecial(n,s),mode='full')
    for o in range(n//2-2,n//2+2):
        v=full[o:o+480,o:o+640]
        r=np.abs(v-sm).max()/sm.max(); best.append((r,n,s,o))
best.sort(); print(best[:8])
# also nonzero support
print('support sm', (sm>0).sum())
EOF
```

```
[(np.float64(0.06792767785813318), 16, 5, 8), (np.float64(0.09314655838229756), 48, 4, 24), (np.float64(0.09314656421572468), 46, 4, 23), (np.float64(0.09314658909483481), 44, 4, 22), (np.float64(0.09314669517201551), 42, 4, 21), (np.float64(0.09314673745350624), 40, 4, 20), (np.float64(0.09314698598123847), 38, 4, 19), (np.float64(0.0931499944984473), 36, 4, 18)]
support sm 116779
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
exec(open('survey.py').read())
import numpy as np
np.set_printoptions(precision=1,suppress=True,linewidth=200)
for nm in ['V1_Vasarely_data/Edge-compare/AEC071800J1_SpikeRateMap.mat','V1_Vasarely_data/Star/ABD071800J1_SpikeRateMap.mat','V1_Vasarely_data/Corners/ABC071800J1_SpikeRateMap.mat','V1_Vasarely_data/Corners/ABC060600J1_SpikeRateMap.mat']:
    S=ld(nm).Standard
    V=[getattr(S,f) for f in S._fieldnames if f.endswith('Vert')][0]
    print(nm.split('/')[-1], S.image.shape)
    if hasattr(V,'_fieldnames'):
        for f in V._fieldnames:
            arr=getattr(V,f); print(f,len(arr)); 
            for k in [0,49,50,99]: print(k,arr[k].x,arr[k].y)
    else:
        print(len(V))
        for k in [0,49,50,99]: print(k,np.c_[V[k].x,V[k].y].T)
    if hasattr(S,'smoothed_image_norm'):
        sm=S.smoothed_image; nr=S.smoothed_image_norm; b=S.BaseActivity
        a=(sm-b); print('norm ratio', np.nanmedian(nr[a!=0]/a[a!=0]), 'max-b',1/(sm.max()-b), 'max',1/sm.max(), 'b',b)
EOF
```

```
AEC071800J1_SpikeRateMap.mat (337, 151)
SquareVert 100
0 [145.7  75.    4.3  75. ] [257.6 186.9 257.6 328.4]
49 [110.7  75.   39.3  75. ] [257.6 221.9 257.6 293.4]
50 [110.  75.  40.  75.] [257.6 222.6 257.6 292.6]
99 [75. 75. 75. 75.] [257.6 257.6 257.6 257.6]
RectVert 100
0 [ 75.  75. 345. 345.] [157.6   7.6   7.6 157.6]
49 [ 75.  75. 345. 345.] [83.4  7.6  7.6 83.4]
50 [ 75.  75. 345. 345.] [81.9  7.6  7.6 81.9]
99 [ 75.  75. 345. 345.] [7.6 7.6 7.6 7.6]
norm ratio 32.21023207757163 max-b 32.21023207757163 max 29.822061898347798 b 0.0024861867627901197
ABD071800J1_SpikeRateMap.mat (321, 321)
100
0 [[160.  134.1  85.   89.3  30.1  63.4  10.   63.4  30.1  89.3  85.  134.1 160.  185.9 235.  230.7 289.9 256.6 310.  256.6 289.9 230.7 235.  185.9]
 [310.  256.6 289.9 230.7 235.  185.9 160.  134.1  85.   89.3  30.1  63.4  10.   63.4  30.1  89.3  85.  134.1 160.  185.9 235.  230.7 289.9 256.6]]
49 [[160.  146.9 122.1 124.3  94.4 111.2  84.2 111.2  94.4 124.3 122.1 146.9 160.  173.1 197.9 195.7 225.6 208.8 235.8 208.8 225.6 195.7 197.9 173.1]
 [235.8 208.8 225.6 195.7 197.9 173.1 160.  146.9 122.1 124.3  94.4 111.2  84.2 111.2  94.4 124.3 122.1 146.9 160.  173.1 197.9 195.7 225.6 208.8]]
50 [[160.  147.2 122.9 125.   95.7 112.2  85.8 112.2  95.7 125.  122.9 147.2 160.  172.8 197.1 195.  224.3 207.8 234.2 207.8 224.3 195.  197.1 172.8]
 [234.2 207.8 224.3 195.  197.1 172.8 160.  147.2 122.9 125.   95.7 112.2  85.8 112.2  95.7 125.  122.9 147.2 160.  172.8 197.1 195.  224.3 207.8]]
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
exec(open('survey.py').read())
import numpy as np
from scipy.ndimage import map_coordinates
np.set_printoptions(precision=3,suppress=True,linewidth=200)
def fit(P,Q):  # Q ~ R P + t ; P,Q Nx2
    Pm,Qm=P.mean(0),Q.mean(0); H=(P-Pm).T@(Q-Qm); U,s,Vt=np.linalg.svd(H); R=(U@Vt).T
    if np.linalg.det(R)<0: Vt[-1]*=-1; R=(U@Vt).T
    t=Qm-R@Pm; return R,t
for pre,cond,vf in [('AEC071800J1','Edge-compare','SquareVert'),('ABD071800J1','Star','DiagVert'),('ABC071800J1','Corners','CornersVert')]:
    d=ld(f'V1_Vasarely_data/{cond}/{pre}_SpikeRateMap.mat'); s=ld(f'V1_Vasarely_data/{cond}/{pre}_Stimulus.mat')
    S=d.Standard; SV=getattr(S,[f for f in S._fieldnames if f.endswith('Vert')][0])
    if hasattr(SV,'_fieldnames'): SV=getattr(SV,vf)
    FV=getattr(s,vf)
    P=np.vstack([np.c_[FV[k].x,FV[k].y] for k in range(0,90,10)]).astype(float)
    Q=np.vstack([np.c_[SV[k].x,SV[k].y] for k in range(0,90,10)]).astype(float)
    R,t=fit(P,Q); print(pre,'angle',np.degrees(np.arctan2(R[1,0],R[0,0])),'t',t,'resid',np.abs(P@R.T+t-Q).max())
    # map standard pixel (r,c) -> full; standard x=c+off?
    Ri=R.T
    H,W=S.smoothed_image.shape
    best=[]
    for off in [0,1]:
      for foff in [0,1]:
        cc,rr=np.meshgrid(np.arange(W)+off,np.arange(H)+off)
        X=np.c_[cc.ravel(),rr.ravel()]-t; F=X@Ri.T  # full x,y
        v=map_coordinates(d.smoothed_image,[F[:,1]-foff,F[:,0]-foff],order=1,cval=np.nan).reshape(H,W)
        m=~np.isnan(v); best.append((np.abs(v-S.smoothed_image)[m].max()/S.smoothed_image.max(),off,foff))
    print(sorted(best))
EOF
```

```
AEC071800J1 angle -74.99999999999999 t [-338.922  407.624] resid 6.394884621840902e-14
[(np.float64(1.1295399535442505), 1, 1), (np.float64(1.1300460640626073), 0, 1), (np.float64(1.1588571804456786), 1, 0), (np.float64(1.1624289603161684), 0, 0)]
ABD071800J1 angle -1.1817068949368097e-15 t [-180. -176.] resid 50.00000000000006
[(np.float64(0.8754951225547553), 1, 0), (np.float64(0.8848116214495583), 0, 1), (np.float64(0.891075911927213), 0, 0), (np.float64(0.891075911927213), 1, 1)]
ABC071800J1 angle -75.0 t [-306.327  354.434] resid 4.547473508864641e-13
[(np.float64(2.492477858249814), 1, 1), (np.float64(2.5049228208205148), 1, 0), (np.float64(2.5223520503373766), 0, 1), (np.float64(2.5347903201825144), 0, 0)]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
exec(open('survey.py').read())
import numpy as np
np.set_printoptions(precision=1,suppress=True,linewidth=200)
s=ld('V1_Vasarely_data/Edge-compare/AEC071800J1_Stimulus.mat'); I=s.EdgecompImage
for k in [0,50,99]:
    x,y=s.SquareVert[k].x.astype(float),s.SquareVert[k].y.astype(float); print('sq',k,x,y)
cx,cy=252,361
print('I around center (row=y,col=x)'); print(I[cy-3:cy+4,cx-3:cx+4])
print('I around (row=x,col=y)'); print(I[cx-3:cx+4,cy-3:cy+4])
print('I flipped row 480-y'); print(I[480-cy-3:480-cy+4,cx-3:cx+4])
# where is the max region
r,c=np.where(I==I.max()); print('max at rows',r.min(),r.max(),'cols',c.min(),c.max())
EOF
```

```
sq 0 [270.3 320.3 233.7 183.7] [429.3 342.7 292.7 379.3]
sq 50 [261.1 285.8 242.9 218.2] [394.8 351.9 327.2 370.1]
sq 99 [252. 252. 252. 252.] [361. 361. 361. 361.]
I around center (row=y,col=x)
[[ 96.   97.   97.   96.   93.9  93.9  92.9]
 [ 96.   97.   99.   97.   97.   96.   93.9]
 [ 97.   99.  100.   99.   97.   96.   92.9]
 [ 97.   97.   99.   97.   96.   93.9  92.9]
 [ 96.   96.   97.   97.   96.   92.9  91.9]
 [ 92.9  93.9  96.   96.   93.9  91.9  90.9]
 [ 91.9  92.9  92.9  93.9  92.9  90.9  89.9]]
I around (row=x,col=y)
[[0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]]
I flipped row 480-y
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
exec(open('survey.py').read())
import numpy as np
from scipy.ndimage import map_coordinates
def fit(P,Q):
    Pm,Qm=P.mean(0),Q.mean(0); H=(P-Pm).T@(Q-Qm); U,s,Vt=np.linalg.svd(H); R=(U@Vt).T
    t=Qm-R@Pm; return R,t
pre,cond,vf='AEC071800J1','Edge-compare','SquareVert'
d=ld(f'V1_Vasarely_data/{cond}/{pre}_SpikeRateMap.mat'); s=ld(f'V1_Vasarely_data/{cond}/{pre}_Stimulus.mat')
S=d.Standard; SV=S.EdgecompVert.SquareVert; FV=s.SquareVert
P=np.vstack([np.c_[FV[k].x,FV[k].y] for k in range(0,90,10)]).astype(float)
Q=np.vstack([np.c_[SV[k].x,SV[k].y] for k in range(0,90,10)]).astype(float)
R,t=fit(P,Q)
H,W=S.smoothed_image.shape
cc,rr=np.meshgrid(np.arange(W)+1,np.arange(H)+1)
X=np.c_[cc.ravel(),rr.ravel()]
F=(X-t)@R   # inverse: P = R^T (Q - t) -> row-vector form (Q-t) @ R
for name,M in [('sm',d.smoothed_image),('img',d.image.toarray())]:
  for flip in ['none','ud']:
    MM=M if flip=='none' else M[::-1]
    v=map_coordinates(MM,[F[:,1]-1,F[:,0]-1],order=1,cval=np.nan).reshape(H,W)
    tgt=S.smoothed_image if name=='sm' else S.image
    m=~np.isnan(v); print(name,flip,np.corrcoef(v[m],tgt[m])[0,1], np.abs(v-tgt)[m].max()/tgt.max(), m.mean())
# where is stimulus in Standard: sample stimulus image
v=map_coordinates(s.EdgecompImage,[F[:,1]-1,F[:,0]-1],order=1,cval=np.nan).reshape(H,W)
print(np.round(v[::24,::10]))
EOF
```

```
sm none -0.04302749480274404 1.1295399535442505 1.0
sm ud -0.11635507543563951 0.9605434435535971 1.0
img none -0.005655133237546678 1.1362808970686362 1.0
img ud -0.009233450294599793 1.0 1.0
[[ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0. 88. 89. 88. 89. 89. 89. 89. 88.]
 [ 0.  0.  0.  0.  0.  0.  0.  0. 72. 72. 72. 73. 72. 73. 72. 72.]
 [ 0.  0.  0.  0.  0.  0.  0.  0. 56. 56. 56. 56. 56. 56. 56. 57.]
 [ 0.  0.  0.  0.  0.  0.  0.  0. 40. 40. 40. 40. 40. 40. 40. 40.]
 [ 0.  0.  0.  0.  0.  0.  0.  0. 24. 24. 24. 24. 24. 24. 24. 24.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  8.  8.  8.  8.  8.  8.  8.  8.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  4.  1.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  9. 23. 37. 34. 21.  5.  0.  0.  0.  0.  0.]
 [ 0.  0.  1. 15. 29. 43. 57. 70. 68. 54. 41. 26. 12.  0.  0.  0.]
 [ 0.  0. 15. 28. 42. 56. 70. 84. 81. 67. 53. 39. 25. 11.  0.  0.]
 [ 0.  0.  0.  0.  8. 22. 37. 50. 48. 34. 20.  5.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  2. 17. 14.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && cat > xf.py <<'EOF'
import numpy as np
from scipy.ndimage import map_coordinates
from scipy.signal import fftconvolve
def fit(P,Q):
    Pm,Qm=P.mean(0),Q.mean(0); H=(P-Pm).T@(Q-Qm); U,s,Vt=np.linalg.svd(H); R=(U@Vt).T
    t=Qm-R@Pm; return R,t
def find_offset(full, std, R, t, search=200):
    # sample full map at Standard coords shifted by (dx,dy) in full frame; brute force over integer shifts via FFT
    H,W=std.shape
    cc,rr=np.meshgrid(np.arange(W)+1,np.arange(H)+1)
    F=(np.c_[cc.ravel(),rr.ravel()]-t)@R
    best=None
    # coarse search
    for dy in range(-search,search+1,4):
        for dx in range(-search,search+1,4):
            v=map_coordinates(full,[F[:,1]-1+dy,F[:,0]-1+dx],order=1,cval=0).reshape(H,W)
            e=np.abs(v-std).max()
            if best is None or e<best[0]: best=(e,dx,dy)
    e,bx,by=best
    for dy in np.arange(by-4,by+4.01,0.5):
        for dx in np.arange(bx-4,bx+4.01,0.5):
            v=map_coordinates(full,[F[:,1]-1+dy,F[:,0]-1+dx],order=1,cval=0).reshape(H,W)
            e=np.abs(v-std).max()
            if e<best[0]: best=(e,dx,dy)
    return best
EOF
python - <<'EOF'
exec(open('survey.py').read()); exec(open('xf.py').read())
import time
for pre,cond,vf in [('AEC071800J1','Edge-compare','SquareVert'),('ABC071800J1','Corners','CornersVert')]:
    d=ld(f'V1_Vasarely_data/{cond}/{pre}_SpikeRateMap.mat'); s=ld(f'V1_Vasarely_data/{cond}/{pre}_Stimulus.mat')
    S=d.Standard; SV=getattr(S,[f for f in S._fieldnames if f.endswith('Vert')][0])
    if hasattr(SV,'_fieldnames'): SV=getattr(SV,vf)
    FV=getattr(s,vf)
    P=np.vstack([np.c_[FV[k].x,FV[k].y] for k in range(0,90,10)]).astype(float)
    Q=np.vstack([np.c_[SV[k].x,SV[k].y] for k in range(0,90,10)]).astype(float)
    R,t=fit(P,Q); t0=time.time()
    b=find_offset(d.smoothed_image,S.smoothed_image,R,t,search=160)
    print(pre,b,b[0]/S.smoothed_image.max(),time.time()-t0)
EOF
```

```
AEC071800J1 (np.float64(0.0005333168653471037), np.float64(-155.0), np.float64(-100.0)) 0.015904608569814144 9.078445196151733
ABC071800J1 (np.float64(0.00034963711572989905), np.float64(-140.5), np.float64(-117.0)) 0.02426226092686393 10.211596012115479
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
exec(open('survey.py').read()); exec(open('xf.py').read())
for pre,cond,vf,off in [('AEC071800J1','Edge-compare','SquareVert',(-155,-100)),('ABC071800J1','Corners','CornersVert',(-140.5,-117))]:
    d=ld(f'V1_Vasarely_data/{cond}/{pre}_SpikeRateMap.mat'); s=ld(f'V1_Vasarely_data/{cond}/{pre}_Stimulus.mat')
    S=d.Standard; SV=getattr(S,[f for f in S._fieldnames if f.endswith('Vert')][0])
    if hasattr(SV,'_fieldnames'): SV=getattr(SV,vf)
    FV=getattr(s,vf)
    P=np.vstack([np.c_[FV[k].x,FV[k].y] for k in range(0,90,10)]).astype(float)
    Q=np.vstack([np.c_[SV[k].x,SV[k].y] for k in range(0,90,10)]).astype(float)
    R,t=fit(P,Q); H,W=S.image.shape
    c=(np.array([(W+1)/2,(H+1)/2])-t)@R
    im=d.image.toarray(); r,cc=np.nonzero(im)
    sm=d.smoothed_image; r2,c2=np.nonzero(sm)
    print(pre,'ROI centre full',c,'+off',c+np.array(off),'spike px bbox centre x',(cc.min()+cc.max())/2+1,'y',(r.min()+r.max())/2+1,'mean',cc.mean()+1,r.mean()+1,'sm bbox',(c2.min()+c2.max())/2+1,(r2.min()+r2.max())/2+1, 'bbox size',cc.max()-cc.min(),r.max()-r.min())
EOF
```

```
AEC071800J1 ROI centre full [337.88298641 339.02299933] +off [182.88298641 239.02299933] spike px bbox centre x 273.0 y 247.0 mean 198.88830920714233 243.23910647365713 sm bbox 276.5 246.5 bbox size 544 388
ABC071800J1 ROI centre full [316.48444323 341.03498044] +off [175.98444323 224.03498044] spike px bbox centre x 245.5 y 254.0 mean 184.26537712218203 243.57486779849708 sm bbox 248.5 253.5 bbox size 487 352
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && cat > xf2.py <<'EOF'
import numpy as np
from scipy.ndimage import map_coordinates
from scipy.signal import fftconvolve
def fit(P,Q):
    Pm,Qm=P.mean(0),Q.mean(0); H=(P-Pm).T@(Q-Qm); U,s,Vt=np.linalg.svd(H); R=(U@Vt).T
    if np.linalg.det(R)<0: raise ValueError('reflection')
    t=Qm-R@Pm; return R,t
def star_fit(FV,SV):
    best=None
    for sh in range(24):
        P=np.vstack([np.c_[np.roll(FV[k].x,sh),np.roll(FV[k].y,sh)] for k in range(0,90,10)]).astype(float)
        Q=np.vstack([np.c_[SV[k].x,SV[k].y] for k in range(0,90,10)]).astype(float)
        R,t=fit(P,Q); e=np.abs(P@R.T+t-Q).max()
        if best is None or e<best[0]: best=(e,R,t,sh)
    return best
def offset_fft(full,std,R,t,s=250):
    H,W=std.shape
    cc,rr=np.meshgrid(np.arange(-s,W+s)+1,np.arange(-s,H+s)+1)
    F=(np.c_[cc.ravel(),rr.ravel()]-t)@R
    G=map_coordinates(full,[F[:,1]-1,F[:,0]-1],order=1,cval=0).reshape(H+2*s,W+2*s)
    # SSD = sum G^2 window - 2 xcorr + const
    xc=fftconvolve(G,std[::-1,::-1],mode='valid')
    g2=fftconvolve(G**2,np.ones_like(std),mode='valid')
    ssd=g2-2*xc+(std**2).sum()
    i,j=np.unravel_index(np.argmin(ssd),ssd.shape)
    v=G[i:i+H,j:j+W]
    return (j-s,i-s), np.abs(v-std).max()/std.max(), np.corrcoef(v.ravel(),std.ravel())[0,1]
EOF
python - <<'EOF'
exec(open('survey.py').read()); exec(open('xf2.py').read())
for nm in sorted(z.namelist()):
    if not nm.endswith('SpikeRateMap.mat'): continue
    d=ld(nm)
    if isinstance(d,h5py.File) or not hasattr(d,'Standard'): continue
    cond=nm.split('/')[1]; pre=nm.split('/')[-1].split('_')[0]
    s=ld(nm.replace('SpikeRateMap','Stimulus')); S=d.Standard
    if cond=='Star':
        e,R,t,sh=star_fit(s.DiagVert,S.DiagVert)
    else:
        vf='SquareVert' if cond=='Edge-compare' else 'CornersVert'
        SV=S.EdgecompVert.SquareVert if cond=='Edge-compare' else S.CornersVert
        FV=getattr(s,vf)
        P=np.vstack([np.c_[FV[k].x,FV[k].y] for k in range(0,90,10)]).astype(float)
        Q=np.vstack([np.c_[SV[k].x,SV[k].y] for k in range(0,90,10)]).astype(float)
        R,t=fit(P,Q); e=np.abs(P@R.T+t-Q).max(); sh=None
    ang=np.degrees(np.arctan2(R[1,0],R[0,0]))
    off,err,cor=offset_fft(d.smoothed_image,S.smoothed_image,R,t)
    print(cond[:4],pre,'vfit %.1e'%e,'rot %.1f'%ang,'sh',sh,'shift(std frame)',off,'maxerr %.3f r %.4f'%(err,cor))
EOF
```

```
Corn ABC041900J2 vfit 4.5e-13 rot -30.0 sh None shift(std frame) (np.int64(-247), np.int64(166)) maxerr 0.086 r 0.9985
Corn ABC042000J1 vfit 3.4e-13 rot -50.0 sh None shift(std frame) (np.int64(-144), np.int64(244)) maxerr 0.006 r 1.0000
Corn ABC042400J2 vfit 4.0e-13 rot 90.0 sh None shift(std frame) (np.int64(-56), np.int64(-250)) maxerr 0.772 r 0.5991
Corn ABC042600J2 vfit 3.4e-13 rot 50.0 sh None shift(std frame) (np.int64(-214), np.int64(-230)) maxerr 0.025 r 0.9996
Corn ABC042700J2 vfit 4.5e-13 rot 75.0 sh None shift(std frame) (np.int64(-89), np.int64(-250)) maxerr 0.522 r 0.8858
Corn ABC042800J2 vfit 2.3e-13 rot 80.0 sh None shift(std frame) (np.int64(-74), np.int64(-250)) maxerr 0.873 r 0.5784
Corn ABC050900J1A vfit 6.8e-13 rot -60.0 sh None shift(std frame) (np.int64(-119), np.int64(250)) maxerr 0.844 r 0.5939
Corn ABC051000J3 vfit 5.7e-13 rot 40.0 sh None shift(std frame) (np.int64(-237), np.int64(-172)) maxerr 0.040 r 0.9993
Corn ABC051500J1 vfit 2.4e-13 rot 75.0 sh None shift(std frame) (np.int64(-250), np.int64(-250)) maxerr 1.000 r 0.0275
Corn ABC051600J1 vfit 9.1e-13 rot -85.0 sh None shift(std frame) (np.int64(57), np.int64(250)) maxerr 0.785 r 0.2991
Corn ABC051800J1 vfit 4.5e-13 rot -70.0 sh None shift(std frame) (np.int64(-64), np.int64(244)) maxerr 0.933 r 0.2636
Corn ABC052600J1 vfit 2.8e-13 rot 80.0 sh None shift(std frame) (np.int64(-66), np.int64(-250)) maxerr 0.796 r 0.6244
Corn ABC060600J1 vfit 4.5e-13 rot 15.0 sh None shift(std frame) (np.int64(-250), np.int64(-173)) maxerr 0.829 r 0.4208
Corn ABC060700J1 vfit 5.7e-13 rot 15.0 sh None shift(std frame) (np.int64(-97), np.int64(-204)) maxerr 0.047 r 0.9989
Corn ABC062100J1 vfit 3.4e-13 rot 75.0 sh None shift(std frame) (np.int64(-115), np.int64(-250)) maxerr 1.000 r 0.4099
Corn ABC062600J1 vfit 4.5e-13 rot -70.0 sh None shift(std frame) (np.int64(-83), np.int64(250)) maxerr 0.586 r 0.3794
Corn ABC062700J1 vfit 4.5e-13 rot 10.0 sh None shift(std frame) (np.int64(-247), np.int64(47)) maxerr 0.
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
exec(open('survey.py').read()); exec(open('xf2.py').read())
np.set_printoptions(linewidth=250)
def std_stim(d,s,cond):
    S=d.Standard
    if cond=='Star': e,R,t,sh=star_fit(s.DiagVert,S.DiagVert); I=s.DiagImage
    else:
        vf='SquareVert' if cond=='Edge-compare' else 'CornersVert'
        SV=S.EdgecompVert.SquareVert if cond=='Edge-compare' else S.CornersVert
        FV=getattr(s,vf); I=s.EdgecompImage if cond=='Edge-compare' else s.CornersImage
        P=np.vstack([np.c_[FV[k].x,FV[k].y] for k in range(0,90,10)]).astype(float)
        Q=np.vstack([np.c_[SV[k].x,SV[k].y] for k in range(0,90,10)]).astype(float)
        R,t=fit(P,Q)
    H,W=S.image.shape
    cc,rr=np.meshgrid(np.arange(W)+1,np.arange(H)+1)
    F=(np.c_[cc.ravel(),rr.ravel()]-t)@R
    return map_coordinates(I,[F[:,1]-1,F[:,0]-1],order=0,cval=-1).reshape(H,W)
for pre,cond in [('AEC071800J1','Edge-compare'),('ABD071800J1','Star'),('ABC071800J1','Corners'),('ABC060600J1','Corners')]:
    d=ld(f'V1_Vasarely_data/{cond}/{pre}_SpikeRateMap.mat'); s=ld(f'V1_Vasarely_data/{cond}/{pre}_Stimulus.mat')
    St=std_stim(d,s,cond); H,W=St.shape
    print(pre,cond,St.shape)
    step=8
    for r in range(0,H,step):
        print('%3d '%r+''.join(' ' if v<0 else ('.' if v<1 else ('#' if v>99 else str(int(v//10)))) for v in St[r,::4]))
EOF
```

```
Sun Nov 15 09:37:23 UTC 2026
AEC071800J1 Edge-compare (337, 151)
  0 ......................................
  8 ...................9999999999999999999
 16 ...................9999999999999999999
 24 ...................8888888888888888888
 32 ...................8888888888888888888
 40 ...................7777777777777777777
 48 ...................7777777777777777777
 56 ...................6666666666666666666
 64 ...................6666666666666666666
 72 ...................5555555555555555555
 80 ...................5555555555555555555
 88 ...................4444444444444444444
 96 ...................4444444444444444444
104 ...................3333333333333333333
112 ...................2222222233333333333
120 ...................2222222222222222222
128 ...................1111111111111111111
136 ...................1111111111111111111
[... 138 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
exec(open('survey.py').read())
import numpy as np
def box(M,x0,y0,w=16):  # x0,y0 = 1-based coords of top-left; inclusive w pixels
    r0=int(round(y0))-1; c0=int(round(x0))-1
    return M[r0:r0+w,c0:c0+w]
rows=[]
for nm in sorted(z.namelist()):
    if 'Edge' not in nm or not nm.endswith('SpikeRateMap.mat'): continue
    d=ld(nm); S=d.Standard
    if not hasattr(S,'BaseActivity'): continue
    sq0=S.EdgecompVert.SquareVert[0]; cx,cy=sq0.x[1],sq0.y[0]  # x of top vertex, y of centre
    cx=float(sq0.x[1]); cy=float(sq0.y[0])
    res={}
    for name,M in [('sm',S.smoothed_image),('img',S.image)]:
      for half in [69]:
        for mode in ['centred','inside','outside']:
          vals=[]
          for sx in [-1,1]:
            for sy in [-1,1]:
              X=cx+sx*half; Y=cy+sy*half
              if mode=='centred': x0,y0=X-8,Y-8
              elif mode=='inside': x0=X if sx<0 else X-16; y0=Y if sy<0 else Y-16
              else: x0=X-16 if sx<0 else X; y0=Y-16 if sy<0 else Y
              b=box(M,x0,y0); vals.append(b.mean() if b.size==256 else np.nan)
          res[(name,mode)]=np.nanmean(vals)
    print(nm.split('/')[-1][:11],'base %.3f'%(S.BaseActivity*1000),' '.join('%s/%s %.3f'%(k[0],k[1],v*1000) for k,v in res.items()))
EOF
```

```
<stdin>:25: RuntimeWarning: Mean of empty slice
AEC052900J1 base 5.604 sm/centred 8.380 sm/inside 6.997 sm/outside nan img/centred 8.639 img/inside 7.800 img/outside nan
AEC063000J1 base 2.082 sm/centred 1.962 sm/inside 2.479 sm/outside nan img/centred 1.932 img/inside 2.690 img/outside nan
AEC070500J2 base 13.767 sm/centred 10.414 sm/inside 16.864 sm/outside nan img/centred 10.879 img/inside 17.470 img/outside nan
AEC071000J4 base 24.145 sm/centred 20.763 sm/inside 22.011 sm/outside nan img/centred 19.842 img/inside 21.435 img/outside nan
AEC071800J1 base 2.486 sm/centred 2.503 sm/inside 4.047 sm/outside nan img/centred 1.832 img/inside 3.993 img/outside nan
AEC07240J1C base 6.930 sm/centred 7.873 sm/inside 8.259 sm/outside nan img/centred 7.772 img/inside 7.614 img/outside nan
AEC07250J1D base 9.008 sm/centred 12.164 sm/inside 10.990 sm/outside nan img/centred 12.045 img/inside 11.505 img/outside nan
AEC09010J1C base 5.640 sm/centred 4.758 sm/inside 6.146 sm/outside nan img/centred 5.212 img/inside 6.185 img/outside nan
AEC09270A1C base 1.132 sm/centred 0.695 sm/inside 0.621 sm/outside nan img/centred 0.558 img/inside 0.522 img/outside nan
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
exec(open('survey.py').read())
import numpy as np
for nm in sorted(z.namelist()):
    if not nm.endswith('SpikeRateMap.mat'): continue
    d=ld(nm)
    if isinstance(d,h5py.File) or not hasattr(d,'Standard') or not hasattr(d.Standard,'BaseActivity'): continue
    S=d.Standard; b=S.BaseActivity; sm=S.smoothed_image; im=S.image
    q=(sm<b).mean(); qi=(im<b).mean(); qf=(d.smoothed_image<b).mean()
    # exact matches of b in any 16x16 box mean?
    from scipy.signal import fftconvolve
    bm=fftconvolve(sm,np.ones((16,16))/256,mode='valid')
    k=np.argmin(np.abs(bm-b)); r,c=np.unravel_index(k,bm.shape)
    print(nm.split('/')[-1][:12],'b %.3f'%(b*1000),'q_sm %.3f q_img %.3f'%(q,qi),'closest single box %.4f at r%d c%d'%(bm[r,c]*1000,r,c),'n boxes within 0.1%%: %d'%(np.abs(bm-b)<1e-3*b).sum())
EOF
```

```
ABC042000J1_ b 0.106 q_sm 0.012 q_img 0.265 closest single box 0.1076 at r257 c187 n boxes within 0.1%: 0
ABC042400J2_ b 0.352 q_sm 0.279 q_img 0.905 closest single box 0.3522 at r41 c171 n boxes within 0.1%: 11
ABC042600J2_ b 9.202 q_sm 0.400 q_img 0.776 closest single box 9.2018 at r121 c60 n boxes within 0.1%: 47
ABC042700J2_ b 12.342 q_sm 0.568 q_img 0.822 closest single box 12.3422 at r119 c172 n boxes within 0.1%: 69
ABC042800J2_ b 4.270 q_sm 0.463 q_img 0.821 closest single box 4.2697 at r233 c16 n boxes within 0.1%: 30
ABC050900J1A b 0.096 q_sm 0.020 q_img 0.627 closest single box 0.1991 at r257 c0 n boxes within 0.1%: 0
ABC051000J3_ b 0.000 q_sm 0.000 q_img 0.000 closest single box 0.0000 at r1 c20 n boxes within 0.1%: 0
ABC051500J1_ b 0.618 q_sm 0.230 q_img 0.666 closest single box 0.6182 at r25 c186 n boxes within 0.1%: 9
ABC051600J1_ b 0.036 q_sm 0.078 q_img 0.447 closest single box 0.0357 at r248 c146 n boxes within 0.1%: 0
ABC051800J1_ b 1.010 q_sm 0.166 q_img 0.625 closest single box 1.0101 at r10 c8 n boxes within 0.1%: 13
ABC052600J1_ b 1.323 q_sm 0.218 q_img 0.592 closest single box 1.3227 at r57 c30 n boxes within 0.1%: 37
ABC062800A4_ b 0.399 q_sm 0.268 q_img 0.748 closest single box 0.3985 at r109 c26 n boxes within 0.1%: 5
ABC063000J1_ b 0.000 q_sm 0.000 q_img 0.000 closest single box 0.0000 at r1 c3 n boxes within 0.1%: 0
ABC070500J2_ b 8.865 q_sm 0.212 q_img 0.529 closest single box 8.8650 at r176 c24 n boxes within 0.1%: 18
ABC071000J4_ b 19.891 q_sm 0.251 q_img 0.560 closest single box 19.8903 at r196 c25 n boxes within 0.1%: 18
ABC071800J1_ b 1.380 q_sm 0.325 q_img 0.773 closest single box 1.3802 at r231 c126 n boxes within 0.1%: 38
ABC07240J1D_ b 7.556 q_sm 0.234 q_img 0.498 closest single box 7.5536 at r154 c11 n boxes within 0.1%: 4
ABC07250J1E_ b 9.896 q_sm 0.187 q_img 0.722 closest single box 9.8957 at r170 c158 n boxes within 0.1%: 39
ABC09010J1E_ b 4.247 q_sm 0.400 q_img 0.781 closest single box 4.2468 at r80 c79 n boxes within 0.1%
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
exec(open('survey.py').read())
import numpy as np
def box(M,x0,y0,w=16):
    r0=int(round(y0))-1; c0=int(round(x0))-1
    if r0<0 or c0<0 or r0+w>M.shape[0] or c0+w>M.shape[1]: return np.full((1,),np.nan)
    return M[r0:r0+w,c0:c0+w]
for nm in sorted(z.namelist()):
    if 'Star' not in nm or not nm.endswith('SpikeRateMap.mat'): continue
    d=ld(nm)
    if isinstance(d,h5py.File) or not hasattr(d,'Standard'): continue
    S=d.Standard; b=S.BaseActivity
    out=[]
    for half in [150,141.4,106.1,100]:
      for mode in ['centred','inside']:
        vals=[]
        for sx in [-1,1]:
          for sy in [-1,1]:
            X=160+sx*half; Y=160+sy*half
            if mode=='centred': x0,y0=X-7.5,Y-7.5
            else: x0=X if sx<0 else X-15; y0=Y if sy<0 else Y-15
            vals.append(box(S.smoothed_image,x0,y0).mean())
        out.append('%g/%s %.3f'%(half,mode[0],np.nanmean(vals)*1000))
    print(nm.split('/')[-1][:11],'b %.3f |'%(b*1000),' '.join(out))
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 11, in <module>
AttributeError: 'mat_struct' object has no attribute 'BaseActivity'
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
exec(open('survey.py').read())
import numpy as np
def box(M,x0,y0,w=16):
    r0=int(round(y0))-1; c0=int(round(x0))-1
    if r0<0 or c0<0 or r0+w>M.shape[0] or c0+w>M.shape[1]: return np.full((1,),np.nan)
    return M[r0:r0+w,c0:c0+w]
for nm in sorted(z.namelist()):
    if 'Star' not in nm or not nm.endswith('SpikeRateMap.mat'): continue
    d=ld(nm)
    if isinstance(d,h5py.File) or not hasattr(d,'Standard'): continue
    S=d.Standard; b=getattr(S,'BaseActivity',np.nan)
    out=[]
    for half in [150,141.4,106.1,100]:
      for mode in ['centred','inside']:
        vals=[]
        for sx in [-1,1]:
          for sy in [-1,1]:
            X=160+sx*half; Y=160+sy*half
            if mode=='centred': x0,y0=X-7.5,Y-7.5
            else: x0=X if sx<0 else X-15; y0=Y if sy<0 else Y-15
            vals.append(box(S.smoothed_image,x0,y0).mean())
        out.append('%g/%s %.3f'%(half,mode[0],np.nanmean(vals)*1000))
    print(nm.split('/')[-1][:11],'b %.3f |'%(b*1000),' '.join(out))
EOF
```

```
ABD051700J1 b nan | 150/c 6.714 150/i 7.688 141.4/c 8.127 141.4/i 9.974 106.1/c 11.462 106.1/i 13.215 100/c 13.000 100/i 13.623
ABD062700J1 b nan | 150/c 0.339 150/i 1.410 141.4/c 1.789 141.4/i 4.923 106.1/c 13.749 106.1/i 14.779 100/c 14.976 100/i 12.801
ABD062800A4 b 3.635 | 150/c 2.846 150/i 3.557 141.4/c 3.588 141.4/i 3.971 106.1/c 5.587 106.1/i 5.010 100/c 4.845 100/i 5.558
ABD062800J1 b 0.807 | 150/c 1.044 150/i 1.397 141.4/c 1.425 141.4/i 2.034 106.1/c 2.775 106.1/i 2.908 100/c 2.979 100/i 2.911
ABD063000J1 b 2.076 | 150/c 0.311 150/i 1.857 141.4/c 2.173 141.4/i 3.243 106.1/c 12.247 106.1/i 14.536 100/c 14.272 100/i 15.649
ABD070500J2 b 8.453 | 150/c 4.334 150/i 6.877 141.4/c 7.227 141.4/i 8.454 106.1/c 14.538 106.1/i 15.375 100/c 15.002 100/i 15.278
ABD071000J4 b 1.016 | 150/c 1.758 150/i 1.362 141.4/c 1.329 141.4/i 2.186 106.1/c 13.585 106.1/i 12.338 100/c 12.891 100/i 8.551
ABD071800A1 b 1.587 | 150/c 1.903 150/i 1.727 141.4/c 1.745 141.4/i 4.437 106.1/c 12.291 106.1/i 16.526 100/c 15.791 100/i 19.042
ABD071800J1 b 5.985 | 150/c 4.053 150/i 5.253 141.4/c 5.852 141.4/i 11.630 106.1/c 14.708 106.1/i 16.161 100/c 15.673 100/i 18.438
ABD07240J1B b 3.274 | 150/c 0.279 150/i 1.649 141.4/c 1.937 141.4/i 3.973 106.1/c 6.669 106.1/i 8.596 100/c 8.270 100/i 8.759
ABD07250J1C b 5.369 | 150/c 1.161 150/i 3.422 141.4/c 3.779 141.4/i 6.176 106.1/c 7.296 106.1/i 6.828 100/c 6.812 100/i 7.404
ABD09010J1D b 0.709 | 150/c 0.572 150/i 0.609 141.4/c 0.622 141.4/i 0.674 106.1/c 2.545 106.1/i 4.294 100/c 3.952 100/i 5.382
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
exec(open('survey.py').read()); exec(open('xf2.py').read())
import collections
res=collections.defaultdict(dict)
for nm in sorted(z.namelist()):
    if not nm.endswith('SpikeRateMap.mat'): continue
    pre=nm.split('/')[-1].split('_')[0]; cell=pre[3:]; cell=cell[:-1] if cell[-1] in 'ABCDE' and len(cell)>8 else cell
    if cell not in ['071800J1','071000J4','070500J2','07240J1','07250J1','09010J1','063000J1','070300J1','071200J1','072000J1','08080J4','08100J1']: continue
    d=ld(nm)
    if isinstance(d,h5py.File) or not hasattr(d,'Standard'): continue
    cond=nm.split('/')[1]; s=ld(nm.replace('SpikeRateMap','Stimulus')); S=d.Standard
    if cond=='Star': e,R,t,sh=star_fit(s.DiagVert,S.DiagVert)
    else:
        vf='SquareVert' if cond=='Edge-compare' else 'CornersVert'
        SV=S.EdgecompVert.SquareVert if cond=='Edge-compare' else S.CornersVert
        FV=getattr(s,vf)
        P=np.vstack([np.c_[FV[k].x,FV[k].y] for k in range(0,90,10)]).astype(float)
        Q=np.vstack([np.c_[SV[k].x,SV[k].y] for k in range(0,90,10)]).astype(float)
        R,t=fit(P,Q)
    off,err,cor=offset_fft(d.smoothed_image,S.smoothed_image,R,t,s=420)
    full=np.array(off,float)@R
    res[cell][cond]=(full.round(1),round(cor,4))
for k,v in res.items(): print(k,v)
EOF
```

```
Sun Nov 15 09:39:12 UTC 2026
063000J1 {'Corners': (array([-242. ,   72.5]), np.float64(0.9996)), 'Edge-compare': (array([-263.3,  121.8]), np.float64(0.9989)), 'Star': (array([-234.4,   99. ]), np.float64(0.5628))}
070500J2 {'Corners': (array([-300.2,   79.1]), np.float64(0.9996)), 'Edge-compare': (array([-267.9,   80.4]), np.float64(0.9986)), 'Star': (array([-277.4,   81. ]), np.float64(0.9987))}
071000J4 {'Corners': (array([-255.7,   89.3]), np.float64(0.9997)), 'Edge-compare': (array([-244. ,   73.8]), np.float64(0.9955)), 'Star': (array([-239. ,   73.5]), np.float64(0.9984))}
071800J1 {'Corners': (array([-141.2, -117.5]), np.float64(0.9972)), 'Edge-compare': (array([-155.2, -100.2]), np.float64(0.9997)), 'Star': (array([-144.5, -110.4]), np.float64(0.3818))}
070300J1 {'Edge-compare': (array([ -87.6, -142.4]), np.float64(0.9989))}
071200J1 {'Edge-compare': (array([-107.4, -110.9]), np.float64(0.9988))}
072000J1 {'Edge-compare': (array([-123.2, -110.5]), np.float64(0.9992))}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
mkdir -p entries/martinez-conde-2019; ls entries/fouke-2025/; head -80 entries/fouke-2025/omr.py; python - <<'EOF'
import json
nb=json.load(open('entries/fouke-2025/reproduce_fouke_2025.ipynb'))
print(nb['metadata']); 
for c in nb['cells'][:6]: print(c['cell_type'], c.get('metadata'), ''.join(c['source'])[:600]); print('---')
EOF
```

```
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt
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
[... 130 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/martinez-conde-2019/vasarely.py",
 "content": "\"\"\"Loading and measures for CRCNS pvc-12, V1 responses to Vasarely-based illusions.\n\nMartinez-Conde, McCamy, Troncoso, Otero-Millan & Macknik (2019), PLoS ONE 14(3): e0210941,\ndoi:10.1371/journal.pone.0210941. Data set doi:10.6080/K05D8Q1T.\n\nThe data set is one zip, V1_Vasarely_data.zip, streamed from the public S3 bucket and opened in\nplace; nothing is written to disk. It holds, per neuron and experiment (Corners, Star,\nEdge-compare), a `<code>_SpikeRateMap.mat` and a `<code>_Stimulus.mat`, and a spreadsheet that\nlists the cells. The data descriptor names the fields image, smoothed_image and\nsmoothed_image_norm. The files hold more than it says:\n\n- `image` (480 x 640) is the unsmoothed spike rate map, spikes per 1 ms sample of eye time at\n  each display unit (DU); one file also stores `eyetime`, and image * eyetime is an integer\n  count there. `smoothed_image` is its smoothed version. Both are in gaze coordinates.\n- `Standard`, in 60 of the 77 spike rate map files, holds the map registered to the stimulus,\n  rotated so that the aligned fold is vertical and cropped to the region of interest (ROI), with\n  the stimulus's equal-luminance polygons in the same frame (`EdgecompVert`, `DiagVert`,\n  `CornersVert`) and, in 40 of them, `BaseActivity`. The registration from the gaze frame to\n  `Standard` uses the neuron's receptive field position, which the files do not store, so a\n  file without `Standard` cannot be registered here.\n\nWhere the parameters come from:\n\n- Spike rate map: the smoothed map of `Standard` (`smoothed_image`), times 1000 to give spikes/s.\n  The Fig 3B legend says the rate map is smoothed after division by eye time. The unsmoothed\n  `Standard.image` is a variant (claim fig4b-spike-rate-difference).\n- Geometry, all in the Standard frame and read from each file's own polygons: polygon k of\n  the Square, the Star and the Edge rectangle is the k% equal-luminance boundary (k = 0..99,\n  the last one collapsing to the 100% point); in Corners it is the (99 - k)% boundary, as the\n  stimulus image shows (`check_luminance`). Fold ends (0% and 100%) come from polygons 0 and 99.\n- Midpoint: the 8 x 8 DU square centred on the 50% point of the fold (Results, \"Strength of\n  neuronal responses\", paragraph 1; Fig 2 legend). The Square and the Star have two symmetric\n  midpoints on the aligned diagonal, averaged (Methods, Corners, paragraph 2).\n- P180: the line in the rectangle 48 DU from the Edge, parallel to it (Methods, Square and edge:\n  \"3 DVA (48 DU) away from Edge in the rectangle at the 50% luminance line\").\n- Corners: of the two 40 degree folds, the bright one (Methods, Corners, paragraph 2, \"We did\n  not analyze dark corner-folds\"). Which one is bright is decided from the stimulus: on a\n  bright fold the luminance on the fold is higher than beside it on the same row, as on the\n  Square's diagonal (Fig 1A legend, nested squares of decreasing luminance have bright\n  diagonals). `fold_is_ridge` computes it.\n- Blocks along a fold: ten non-overlapping blocks from 0% to 100% luminance, each 10% of the\n  fold long and 8 DU wide (Results, \"Responses averaged along the entire fold\", paragraph 1).\n- Absolute baseline, reading \"squares\": the mean rate in 16 x 16 DU squares in 0% luminance\n  areas (Methods, Visual stimuli). Square and Edge: four squares inside the corners of the\n  138 x 138 DU square centred on the Square (Methods, Square and edge; centred on the corners\n  they would leave the ROI). Star: four squares inside the corners of the 300 x 300 DU square\n  that circumscribes the 0% star's circumscribed circle (radius 150 DU; Methods, Star). Corners:\n  the paper says only \"two 1 x 1 DVA square regions in 0% luminance areas within the ROI\"\n  (Fig 2C shows them); the squares taken here are the two bottom corners of the ROI, the only\n  0% band inside it. This placement is an assumption. Reading \"dataset\": the file's own\n  `Standard.BaseActivity`, undocumented, present for 40 of the 60 registered files.\n- RMS contrast: 16 x 16 DU square centred on the Edge, moved from 0% to 100% in 1.5% steps\n  (Results, \"Neuron responses to corner-folds vs. different contrasts along edge\"). The\n  definition of RMS contrast is open; `rms_contrast` gives the readings of the claims file.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport re\nimport zipfile\n\nimport fsspec\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport scipy.io as sio\nfrom scipy.ndimage import map_coordinates\n\nBUCKET = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-12/live/\"\nZIP_URL = BUCKET + \"V1_Vasarely_data.zip\"\nZIP_MD5 = \"e1301fe463e72332e2303b2053ee0559\"   # checksums.md5 of the data set\nDOI = \"10.6080/K05D8Q1T\"\n\nCONDITIONS = {\"Edge-compare\": \"Square and Edge\", \"Star\": \"Star\", \"Corners\": \"Corners\"}\nDU_PER_DVA = 16\nMID_SIZE = 8            # DU, midpoint square (Results; Fig 2 legend)\nBLOCK_WIDTH = 8         # DU (Results, Responses averaged along the entire fold)\nBASE_SIZE = 16          # DU, baseline squares (Methods, Visual stimuli)\nCIRC_HALF = 69          # DU, half of the 138 DU square around the Square (Methods)\nP180_OFFSET = 48        # DU from the Edge into the rectangle (Methods)\nRMS_BOX = 16            # DU (Results, contrast section)\nRMS_STEP = 1.5          # % luminance (Results, contrast section)\nRATE_SCALE = 1000.0     # maps are spikes per 1 ms sample; times 1000 gives spikes/s\n\nCODE_RE = re.compile(r\"^(A[A-Z]{2})(\\d+[JA]\\d)([A-Z]?)$\")\n\n\ndef open_zip() -> zipfile.ZipFile:\n    \"\"\"The data set's zip, opened in place over range requests.\"\"\"\n    return zipfile.ZipFile(fsspec.open(ZIP_URL, block_size=2**20).open())\n\n\ndef checksums() -> str:\n    with fsspec.open(BUCKET + \"checksums.md5\", \"rt\") as f:\n        return f.read()\n\n\ndef read_mat(z: zipfile.ZipFile, name: str):\n    \"\"\"The `dat` variable of a MATLAB file; files saved as v7.3 come back as an h5py File.\"\"\"\n    raw = z.read(name)\n    try:\n        return sio.loadmat(io.BytesIO(raw), squeeze_me=True, struct_as_record=False)[\"dat\"]\n    except NotImplementedError:\n        return h5py.File(io.BytesIO(raw), \"r\")\n\n\ndef parse_code(stem: str) -> dict:\n    \"\"\"File code such as ABC07240J1D: experiment prefix, cell (as in the spreadsheet), suffix.\"\"\"\n    m = CODE_RE.match(stem)\n    prefix, cell, suffix = m.groups()\n    return {\"prefix\": prefix, \"cell\": cell, \"suffix\": suffix, \"monkey\": cell[-2]}\n\n\ndef spreadsheet(z: zipfile.ZipFile) -> pd.DataFrame:\n    \"\"\"V1_Vasarely_data_SMC.xlsx: one row per cell, an X under each experiment.\"\"\"\n    raw = pd.read_excel(io.BytesIO(z.read(\"V1_Vasarely_data/V1_Vasarely_data_SMC.xlsx\")), header=None)\n    head = raw.index[raw.eq(\"Cell\").any(axis=1)][0]\n    cols = raw.iloc[head].tolist()\n    df = raw.iloc[head + 1:].copy()\n    df.columns = cols\n    df = df[[c for c in cols if isinstance(c, str)]].dropna(subset=[\"Cell\"])\n    df[\"Cell\"] = df[\"Cell\"].astype(str)\n    for c in [\"Corners\", \"Star\", \"Edge-Compare\"]:\n        df[c] = df[c].astype(str).str.strip().eq(\"X\")\n    return df.reset_index(drop=True)\n\n\ndef _dense(a):\n    a = a.toarray() if hasattr(a, \"toarray\") else a\n    return np.asarray(a, dtype=float)\n\n\ndef _poly(p) -> np.ndarray:\n    return np.c_[np.asarray(p.x, float).ravel(), np.asarray(p.y, float).ravel()]\n\n\ndef _rigid(P: np.ndarray, Q: np.ndarray):\n    \"\"\"Rotation R and translation t with Q = P R^T + t (least squares).\"\"\"\n    Pm, Qm = P.mean(0), Q.mean(0)\n    U, _, Vt = np.linalg.svd((P - Pm).T @ (Q - Qm))\n    R = (U @ Vt).T\n    return R, Qm - R @ Pm\n\n\ndef standard_stimulus(stim, std, condition: str) -> np.ndarray:\n    \"\"\"The file's stimulus image resampled into the Standard frame (nearest pixel).\n\n    The transform is fitted on the equal-luminance polygons, which both files store; image\n    pixel (row, col) has coordinates (x, y) = (col + 1, row + 1), as the stimulus image and\n    its polygons show.\n    \"\"\"\n    if condition == \"Edge-compare\":\n        full, frame, image = stim.SquareVert, std.EdgecompVert.SquareVert, stim.EdgecompImage\n        pairs = [(_poly(full[k]), _poly(frame[k])) for k in range(0, 90, 10)]\n    elif condition == \"Corners\":\n        full, frame, image = stim.CornersVert, std.CornersVert, stim.CornersImage\n        pairs = [(_poly(full[k]), _poly(frame[k])) for k in range(0, 90, 10)]\n    else:\n        full, frame, image = stim.DiagVert, std.DiagVert, stim.DiagImage\n        best = None\n        for shift in range(24):   # the star's vertices may be listed from another point\n            P = np.vstack([np.roll(_poly(full[k]), shift, axis=0) for k in range(0, 90, 10)])\n            Q = np.vstack([_poly(frame[k]) for k in range(0, 90, 10)])\n            R, t = _rigid(P, Q)\n            err = np.abs(P @ R.T + t - Q).max()\n            if best is None or err < best[0]:\n                best = (err, R, t)\n        _, R, t = best\n        pairs = None\n    if pairs is not None:\n        P = np.vstack([p for p, _ in pairs])\n        Q = np.vstack([q for _, q in pairs])\n        R, t = _rigid(P, Q)\n    H, W = std.smoothed_image.shape\n    cc, rr = np.meshgrid(np.arange(W) + 1.0, np.arange(H) + 1.0)\n    F = (np.c_[cc.ravel(), rr.ravel()] - t) @ R\n    return map_coordinates(np.asarray(image, float), [F[:, 1] - 1, F[:, 0] - 1], order=0,\n                           cval=np.nan).reshape(H, W)\n\n\ndef fold_geometry(std, condition: str) -> dict:\n    \"\"\"Folds as vertical segments in the Standard frame: x, y at 0% and y at 100% luminance.\n\n    Read from the file's polygons (see the module docstring). Square and Star give two\n    half-diagonals each; Corners gives both 40 degree folds, labelled by apex direction.\n    \"\"\"\n    folds = {}\n    if condition == \"Edge-compare\":\n        sq0, sq99 = _poly(std.EdgecompVert.SquareVert[0]), _poly(std.EdgecompVert.SquareVert[99])\n        cx, cy = sq99.mean(0)\n        on_axis = sq0[np.abs(sq0[:, 0] - cx) < 1]\n        for y0 in sorted(on_axis[:, 1]):\n            folds[\"S90_\" + (\"near\" if y0 < cy else \"far\")] = (cx, y0, cy)\n        r0, r99 = _poly(std.EdgecompVert.RectVert[0]), _poly(std.EdgecompVert.RectVert[99])\n        ex = r0[:, 0].min()\n        inward = 1.0 if r0[:, 0].max() > ex else -1.0\n        y_zero = r0[:, 1].max() if r99[:, 1].mean() < r0[:, 1].mean() else r0[:, 1].min()\n        y_full = r99[:, 1].mean()\n        folds[\"Edge\"] = (ex, y_zero, y_full)\n        folds[\"P180\"] = (ex + inward * P180_OFFSET, y_zero, y_full)\n        folds[\"_square_centre\"] = (cx, cy)\n    elif condition == \"Star\":\n        p0, p99 = _poly(std.DiagVert[0]), _poly(std.DiagVert[99])\n        cx, cy = p99.mean(0)\n        r = np.hypot(p0[:, 0] - cx, p0[:, 1] - cy)\n        outer = p0[(r > r.max() - 1) & (np.abs(p0[:, 0] - cx) < 1)]\n        for x0, y0 in sorted(map(tuple, outer), key=lambda v: v[1]):\n            folds[\"S52_\" + (\"upper\" if y0 < cy else \"lower\")] = (cx, y0, cy)\n        folds[\"_centre\"] = (cx, cy)\n        folds[\"_outer_radius\"] = r.max()\n    else:\n        p0, p99 = _poly(std.CornersVert[0]), _poly(std.CornersVert[99])\n        # apexes: vertices that move along y only; in polygon 0 the up-pointing apex is the\n        # vertex with the smallest y, the down-pointing one is the local maximum inside the zigzag\n        up = p0[np.argmin(p0[:, 1])]\n        inner = p0[(p0[:, 0] > p0[:, 0].min() + 1) & (p0[:, 0] < p0[:, 0].max() - 1)]\n        base_y = np.median(inner[:, 1])\n        down = inner[np.argmax(np.where(inner[:, 1] < base_y + 200, inner[:, 1], -np.inf))]\n        for name, apex in [(\"S40_up\", up), (\"S40_down\", down)]:\n            k99 = p99[np.argmin(np.abs(p99[:, 0] - apex[0]) + 1e3 * (np.abs(p99[:, 0] - apex[0]) > 0.5))]\n            # Corners polygons run from 100% (k = 0) to 0% (k = 99); see check_luminance\n            folds[name] = (apex[0], k99[1], apex[1])\n    return folds\n\n\ndef box_mask(shape, x: float, y: float, w: float, h: float) -> np.ndarray:\n    \"\"\"Pixels whose centres (1-based coordinates) lie in [x - w/2, x + w/2) x [y - h/2, y + h/2).\"\"\"\n    H, W = shape\n    cols = np.arange(W) + 1.0\n    rows = np.arange(H) + 1.0\n    mc = (cols >= x - w / 2) & (cols < x + w / 2)\n    mr = (rows >= y - h / 2) & (rows < y + h / 2)\n    return mr[:, None] & mc[None, :]\n\n\ndef box_mean(M: np.ndarray, x: float, y: float, w: float, h: float | None = None) -> float:\n    m = box_mask(M.shape, x, y, w, w if h is None else h)\n    return float(M[m].mean()) if m.any() else np.nan\n\n\ndef point_at(fold, frac: float):\n    \"\"\"(x, y) at luminance fraction frac (0 = 0%, 1 = 100%) along a fold.\"\"\"\n    x, y0, y1 = fold\n    return x, y0 + frac * (y1 - y0)\n\n\ndef midpoint(M, fold) -> float:\n    x, y = point_at(fold, 0.5)\n    return box_mean(M, x, y, MID_SIZE)\n\n\ndef blocks(M, fold, n: int = 10) -> np.ndarray:\n    \"\"\"Mean of M in n blocks from 0% to 100%, each 1/n of the fold long and 8 DU wide.\"\"\"\n    x, y0, y1 = fold\n    L = abs(y1 - y0)\n    return np.array([box_mean(M, x, y0 + (i + 0.5) / n * (y1 - y0), BLOCK_WIDTH, L / n)\n                     for i in range(n)])\n\n\ndef fold_is_ridge(lum: np.ndarray, fold, side: float = 10.0) -> float:\n    \"\"\"Luminance on the fold minus beside it (same row, +-side DU), mean over 20% to 80%.\n\n    Positive on a bright fold (luminance peaks on the fold), negative on a dark one.\n    \"\"\"\n    x, y0, y1 = fold\n    out = []\n    for f in np.linspace(0.2, 0.8, 13):\n        _, y = point_at(fold, f)\n        on = box_mean(lum, x, y, 2)\n        off = np.nanmean([box_mean(lum, x - side, y, 2), box_mean(lum, x + side, y, 2)])\n        out.append(on - off)\n    return float(np.nanmean(out))\n\n\ndef baseline_squares(shape, condition: str, folds: dict) -> list[tuple[float, float]]:\n    \"\"\"Centres of the 16 x 16 DU baseline squares (reading \"squares\"; module docstring).\"\"\"\n    H, W = shape\n    s = BASE_SIZE / 2\n    if condition == \"Edge-compare\":\n        cx, cy = folds[\"_square_centre\"]\n        return [(cx + sx * (CIRC_HALF - s), cy + sy * (CIRC_HALF - s)) for sx in (-1, 1) for sy in (-1, 1)]\n    if condition == \"Star\":\n        cx, cy = folds[\"_centre\"]\n        R = folds[\"_outer_radius\"]\n        return [(cx + sx * (R - s), cy + sy * (R - s)) for sx in (-1, 1) for sy in (-1, 1)]\n    # Corners: the two bottom corners of the ROI, in the 0% band (an assumption)\n    return [(1 + s - 0.5 + 0.5, H - s + 0.5), (W - s + 0.5, H - s + 0.5)]\n\n\ndef baseline(M, centres) -> float:\n    return float(np.mean([box_mean(M, x, y, BASE_SIZE) for x, y in centres]))\n\n\ndef load_all(z: zipfile.ZipFile | None = None) -> list[dict]:\n    \"\"\"Every spike rate map file with its stimulus, reduced to what the analysis uses.\"\"\"\n    z = z or open_zip()\n    recs = []\n    for name in sorted(z.namelist()):\n        if not name.endswith(\"_SpikeRateMap.mat\"):\n            continue\n        condition = name.split(\"/\")[1]\n        stem = name.split(\"/\")[-1].split(\"_\")[0]\n        rec = {\"file\": stem, \"condition\": condition, **parse_code(stem)}\n        d = read_mat(z, name)\n        if isinstance(d, h5py.File):\n            rec.update(format=\"v7.3\", fields=sorted(d[\"dat\"].keys()), registered=False)\n            recs.append(rec)\n            continue\n        rec[\"format\"] = \"v5\"\n        rec[\"fields\"] = list(d._fieldnames)\n        img = _dense(d.image)\n        rec[\"full_image_max\"] = float(img.max())\n        rec[\"full_smoothed_max_hz\"] = float(np.asarray(d.smoothed_image).max() * RATE_SCALE)\n        if hasattr(d, \"eyetime\"):\n            et = _dense(d.eyetime)\n            rec[\"eyetime_s\"] = float(et.sum() / 1000)\n            rec[\"spikes_from_eyetime\"] = float(np.round(img * et).sum())\n            rec[\"count_is_integer\"] = bool(np.allclose(img * et, np.round(img * et)))\n        std = getattr(d, \"Standard\", None)\n        rec[\"registered\"] = std is not None\n        if std is not None:\n            rec[\"std_fields\"] = list(std._fieldnames)\n            rec[\"rate\"] = np.asarray(std.smoothed_image, float) * RATE_SCALE\n            rec[\"rate_unsmoothed\"] = _dense(std.image) * RATE_SCALE\n            rec[\"base_dataset\"] = (float(std.BaseActivity) * RATE_SCALE\n                                   if hasattr(std, \"BaseActivity\") else np.nan)\n            rec[\"folds\"] = fold_geometry(std, condition)\n            stim = read_mat(z, name.replace(\"_SpikeRateMap\", \"_Stimulus\"))\n            rec[\"lum\"] = standard_stimulus(stim, std, condition)\n            if condition == \"Edge-compare\":\n                rec[\"std_rect\"] = _poly(std.EdgecompVert.RectVert[0])\n        recs.append(rec)\n    return recs\n\n\ndef check_luminance(rec: dict) -> dict:\n    \"\"\"Stimulus luminance (0-100) at the 0%, 50% and 100% points of each fold, and on the\n    baseline squares, read from the file's own stimulus image in the Standard frame.\"\"\"\n    lum = rec[\"lum\"]\n    out = {}\n    for k, f in rec[\"folds\"].items():\n        if k.startswith(\"_\"):\n            continue\n        for frac in (0.05, 0.5, 0.95):\n            x, y = point_at(f, frac)\n            out[f\"{k}@{int(frac * 100)}%\"] = box_mean(lum, x, y, 2)\n        out[f\"{k} ridge\"] = fold_is_ridge(lum, f)\n    centres = baseline_squares(lum.shape, rec[\"condition\"], rec[\"folds\"])\n    out[\"baseline squares max lum\"] = max(np.nanmax(lum[box_mask(lum.shape, x, y, BASE_SIZE, BASE_SIZE)])\n                                          for x, y in centres)\n    return out\n\n\ndef bright_corner_fold(rec: dict) -> str:\n    \"\"\"Name of the bright S40 fold of a Corners file (the one with the luminance ridge).\"\"\"\n    r = {k: fold_is_ridge(rec[\"lum\"], rec[\"folds\"][k]) for k in (\"S40_up\", \"S40_down\")}\n    return max(r, key=r.get)\n\n\ndef fold_measures(rec: dict, base: float, smoothed: bool = True) -> dict:\n    \"\"\"Per fold: midpoint response, midpoint spike rate difference and the ten block\n    differences (halves of the Square and Star kept apart, as `<fold>_<half>`).\"\"\"\n    M = rec[\"rate\"] if smoothed else rec[\"rate_unsmoothed\"]\n    out = {}\n    folds = rec[\"folds\"]\n    if rec[\"condition\"] == \"Edge-compare\":\n        names = {\"Edge\": [\"Edge\"], \"P180\": [\"P180\"], \"S90\": [\"S90_near\", \"S90_far\"]}\n    elif rec[\"condition\"] == \"Star\":\n        names = {\"S52\": [\"S52_upper\", \"S52_lower\"]}\n    else:\n        bright = bright_corner_fold(rec)\n        dark = \"S40_down\" if bright == \"S40_up\" else \"S40_up\"\n        names = {\"S40\": [bright], \"S40dark\": [dark]}\n    for fold, parts in names.items():\n        mids = [midpoint(M, folds[p]) for p in parts]\n        out[fold] = {\n            \"response\": float(np.mean(mids)),\n            \"diff\": float(np.mean(mids)) - base,\n            \"blocks\": [blocks(M, folds[p]) - base for p in parts],\n        }\n    return out\n\n\ndef rms_contrast(lum: np.ndarray, edge_fold, levels: np.ndarray) -> pd.DataFrame:\n    \"\"\"Local RMS contrast of the stimulus in a 16 x 16 DU square centred on the Edge at each\n    luminance level (%). Readings: (a) SD / mean of the luminance values; (b) SD of the\n    luminance normalised to 0-1.\"\"\"\n    rows = []\n    for L in levels:\n        x, y = point_at(edge_fold, L / 100)\n        v = lum[box_mask(lum.shape, x, y, RMS_BOX, RMS_BOX)]\n        v = v[~np.isnan(v)]\n        rows.append({\"level\": L, \"a_sd_over_mean\": v.std() / v.mean() if v.mean() > 0 else np.nan,\n                     \"b_sd_norm\": (v / 100).std(), \"mean_lum\": v.mean()})\n    return pd.DataFrame(rows)\n\n\ndef edge_response(M, edge_fold, level: float) -> float:\n    \"\"\"Mean of M in a 16 x 16 DU square centred on the Edge at a luminance level (%).\"\"\"\n    x, y = point_at(edge_fold, level / 100)\n    return box_mean(M, x, y, RMS_BOX)\n"
}
```

```
File created successfully at: entries/martinez-conde-2019/vasarely.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/martinez-conde-2019 && python - <<'EOF'
import re
s=open('vasarely.py').read()
s=s.replace("""            k99 = p99[np.argmin(np.abs(p99[:, 0] - apex[0]) + 1e3 * (np.abs(p99[:, 0] - apex[0]) > 0.5))]
""","""            same_x = p99[np.abs(p99[:, 0] - apex[0]) < 0.5]
            k99 = same_x[np.argmin(np.abs(same_x[:, 1] - apex[1] - 100))]
""")
s=s.replace("return [(1 + s - 0.5 + 0.5, H - s + 0.5), (W - s + 0.5, H - s + 0.5)]","return [(s + 0.5, H - s + 0.5), (W - s + 0.5, H - s + 0.5)]")
open('vasarely.py','w').write(s)
EOF
cd $TMPDIR && source scratch/bin/activate && time python - <<'EOF'
import sys,resource; sys.path.insert(0,'entries/martinez-conde-2019')
import vasarely as v, numpy as np, pandas as pd, pickle
pd.set_option('display.width',250); pd.set_option('display.max_columns',40); pd.set_option('display.max_rows',200)
recs=v.load_all()
print(len(recs), resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
rows=[]
for r in recs:
    if not r['registered']: continue
    c=v.check_luminance(r); c['file']=r['file']; c['cond']=r['condition']; rows.append(c)
df=pd.DataFrame(rows)
for cond,g in df.groupby('cond'):
    print(cond); print(g.dropna(axis=1,how='all').round(1).describe().T[['count','min','max']])
for r in recs:
    if r['registered']: print(r['file'], {k:tuple(np.round(f,1)) for k,f in r['folds'].items() if not k.startswith('_')}) if r['file'] in ('AEC071800J1','ABD071800J1','ABC071800J1','ABC060600J1') else None
EOF
```

```
entries/martinez-conde-2019/vasarely.py:351: RuntimeWarning: All-NaN slice encountered
  out["baseline squares max lum"] = max(np.nanmax(lum[box_mask(lum.shape, x, y, BASE_SIZE, BASE_SIZE)])
77 0.275044 GB
Corners
                          count   min   max
S40_up@5%                  26.0   5.1   6.6
S40_up@50%                 26.0  50.3  51.5
S40_up@95%                 26.0  95.5  96.5
S40_up ridge               26.0 -25.2 -24.0
S40_down@5%                26.0   1.8   3.5
S40_down@50%               26.0  46.7  49.0
S40_down@95%               26.0  91.9  93.4
S40_down ridge             26.0  23.3  25.0
baseline squares max lum   25.0   1.0   1.0
Edge-compare
                          count   min   max
baseline squares max lum   22.0   0.0   0.0
S90_near@5%                22.0   3.8   5.1
S90_near@50%               22.0  49.2  50.5
S90_near@95%               22.0  94.4  95.7
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
import sys; sys.path.insert(0,'entries/martinez-conde-2019')
import vasarely as v, numpy as np, pandas as pd
from scipy import stats
recs=[r for r in v.load_all() if r['registered']]
rows=[]
for r in recs:
    cen=v.baseline_squares(r['rate'].shape,r['condition'],r['folds'])
    bsq=v.baseline(r['rate'],cen)
    for bname,b in [('squares',bsq),('dataset',r['base_dataset'])]:
        m=v.fold_measures(r,b)
        for f,d in m.items():
            rows.append(dict(file=r['file'],cell=r['cell'],cond=r['condition'],base_reading=bname,base=b,fold=f,resp=d['response'],diff=d['diff']))
df=pd.DataFrame(rows)
print(df.groupby(['base_reading','fold'])['diff'].agg(['count','mean','sem','median']).round(2))
print(df.groupby(['base_reading','cond'])['base'].agg(['count','mean','median']).round(2))
EOF
```

```
count   mean   sem  median
base_reading fold                               
dataset      Edge         9  14.01  1.88   13.17
             P180         9   3.58  1.08    2.19
             S40         19  29.10  5.54   22.63
             S40dark     19  11.28  2.67    7.61
             S52         10  20.57  3.17   19.84
             S90          9   9.08  2.48    7.43
squares      Edge        22  18.72  4.28   13.86
             P180        22   3.88  0.91    3.61
             S40         26  26.41  4.29   23.35
             S40dark     26  12.03  2.03    7.60
             S52         12  19.10  3.01   16.92
             S90         22   8.21  1.98    5.83
                           count  mean  median
base_reading cond                             
dataset      Corners          38  4.29    1.32
             Edge-compare     27  7.87    5.64
             Star             10  3.29    2.68
squares      Corners          52  3.49    2.45
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
import sys; sys.path.insert(0,'entries/martinez-conde-2019')
import vasarely as v, numpy as np, pandas as pd
z=v.open_zip()
d=v.read_mat(z,'V1_Vasarely_data/Edge-compare/AEC071800J1_SpikeRateMap.mat'); s=v.read_mat(z,'V1_Vasarely_data/Edge-compare/AEC071800J1_Stimulus.mat')
lum=v.standard_stimulus(s,d.Standard,'Edge-compare'); f=v.fold_geometry(d.Standard,'Edge-compare')
lv=np.arange(0,100.01,1.5)
t=v.rms_contrast(lum,f['Edge'],lv)
print(t.iloc[::6].round(3).to_string())
# other readings: michelson? std/mean on lum where background = 0? Weber...
for L in [0,24,51,75,99]:
    x,y=v.point_at(f['Edge'],L/100); m=v.box_mask(lum.shape,x,y,16,16); vals=lum[m]; print(L, np.round(np.unique(vals),1)[:20], vals.size)
EOF
```

```
Sun Nov 15 09:43:46 UTC 2026
    level  a_sd_over_mean  b_sd_norm  mean_lum
0     0.0           2.154      0.014     0.631
6     9.0           1.075      0.048     4.451
12   18.0           0.972      0.092     9.422
18   27.0           0.948      0.133    14.074
24   36.0           0.956      0.179    18.766
30   45.0           0.937      0.223    23.781
36   54.0           0.943      0.268    28.468
42   63.0           0.935      0.312    33.357
48   72.0           0.935      0.358    38.273
54   81.0           0.941      0.401    42.673
60   90.0           0.948      0.449    47.333
66   99.0           1.431      0.453    31.633
0 [0.  1.  2.  3.  4.  5.1] 256
24 [ 0.  17.2 18.2 19.2 20.2 21.2 22.2 23.2 24.2 25.3 26.3 27.3 28.3 29.3] 256
51 [ 0.  45.5 46.5 47.5 48.5 49.5 50.5 51.5 52.5 53.5 54.5 55.6] 256
75 [ 0.  68.7 69.7 70.7 71.7 72.7 73.7 74.7 75.8 76.8 77.8 78.8 79.8] 256
99 [  0.   91.9  92.9  93.9  94.9  96.   97.   98.   99.  100. ] 256
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && uv pip install -q nbformat nbclient ipykernel 2>&1 | tail -1; grep -n "notebook\|kernel\|tags\|sanity\|claim:" tools/entry.py | head -60
```

```
6:    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
17:- every notebook in the directory is listed in entry.yaml, and exists;
18:- notebooks are committed without outputs;
20:- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
21:- each notebook has a cell tagged `sanity` that prints what was loaded;
22:- no notebook or helper embeds a large literal array or an encoded image, or
26:notebook through a Jupyter kernel installed in that environment, in the entry
28:go to --output-dir (default: executed/<name>/, which git ignores). A notebook
36:(docs/protocol.md): the executed notebooks with the conclusions removed (every
64:HARNESS = ["ipykernel", "nbconvert"]      # needed to execute, not part of the entry
172:def code_of(notebook_path: Path) -> str:
173:    nb = nbformat.read(notebook_path, as_version=4)
188:    listed = [n["path"] for n in entry.get("notebooks", [])]
191:        report.error(rel / name, "notebook is not listed in entry.yaml")
193:        report.error(rel / "entry.yaml", f"listed notebook {name!r} does not exist")
235:            report.error(rel / name, "commit notebooks without outputs (clear them before committing)")
236:        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
237:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
241:                report.error(rel / name, f"neither the notebook nor a helper names dataset {dandiset}")
244:                report.error(rel / name, f"neither the notebook nor a helper names version {version} "
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 225,260p tools/entry.py; sed -n 600,640p tools/entry.py
```

```
report.error(rel / "entry.yaml", "an orientation or reproduction entry must relate to a dataset")
        for d, v in versions.items():
            if not v:
                report.error(rel / "entry.yaml", f"pin the version of dataset {d}, as {archives[d]}:{d}/<version>")
    helper_code = "\n".join((entry_dir / h).read_text() for h in helpers if (entry_dir / h).is_file())

    for name in [n for n in listed if n in present]:
        path = entry_dir / name
        nb = nbformat.read(path, as_version=4)
        if any(c.cell_type == "code" and (c.get("outputs") or c.get("execution_count")) for c in nb.cells):
            report.error(rel / name, "commit notebooks without outputs (clear them before committing)")
        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
        code = code_of(path)
        for dandiset in dandisets:
            if dandiset not in code and dandiset not in helper_code:
                report.error(rel / name, f"neither the notebook nor a helper names dataset {dandiset}")
            version = versions[dandiset]
            if version and version not in code and version not in helper_code:
                report.error(rel / name, f"neither the notebook nor a helper names version {version} "
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "_derivation_checks" -A30 tools/entry.py | head -50
```

```
246:        _derivation_checks(report, rel / name, code)
247-    for name in helpers:
248-        if (entry_dir / name).is_file():
249:            _derivation_checks(report, rel / name, (entry_dir / name).read_text())
250-
251-    # Claims and attempts that go with this entry.
252-    claims_by_target, labels_used, kinds_by_target, claims_checked = {}, {}, {}, {}
253-    for path in claims_paths():
254-        data = validate(report, path, "claims") or {}
255-        ids = {c["id"] for c in data.get("claims", [])}
256-        claims_by_target[claims_target(data)] = ids
257-        claims_checked[claims_target(data)] = max((str(c.get("date") or "") for c in data.get("checks") or []),
258-                                                  default="")
259-        kinds_by_target[claims_target(data)] = {
260-            c["id"]: c.get("data", "dataset") for c in data.get("claims", [])}
261-        labels_used[claims_target(data)] = any(
262-            c.get("data") == "with_labels" for c in data.get("claims", []))
263-        for c in data.get("claims", []):
264-            for other in c.get("depends_on", []):
265-                if other not in ids:
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/martinez-conde-2019 && python - <<'EOF'
s=open('vasarely.py').read()
s=s.replace('''BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-12/live/"''','''DATASET_ID = "pvc-12"
DATASET_VERSION = "unversioned"   # CRCNS data sets have no versions; the zip's MD5 is pinned below
BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pvc-12/live/"''')
open('vasarely.py','w').write(s)
EOF
grep -n "DATASET_ID\|ZIP_MD5" vasarely.py
```

```
70:DATASET_ID = "pvc-12"
74:ZIP_MD5 = "e1301fe463e72332e2303b2053ee0559"   # checksums.md5 of the data set
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(r\"\"\"\n# Reproducing Martinez-Conde et al. (2019) from CRCNS pvc-12\n\n**Paper.** Martinez-Conde S, McCamy MB, Troncoso XG, Otero-Millan J, Macknik SL (2019). Area V1\nresponses to illusory corner-folds in Vasarely's nested squares and the Alternating Brightness\nStar illusions. *PLoS ONE* 14(3): e0210941.\n[doi:10.1371/journal.pone.0210941](https://doi.org/10.1371/journal.pone.0210941). The claims file\nwas written from the version of record (PMC6438452, Europe PMC full text), without the\nsupplementary files S1 and S2 Table.\n\n**Dataset.** CRCNS [pvc-12](https://crcns.org/data-sets/pvc/pvc-12),\n[doi:10.6080/K05D8Q1T](https://doi.org/10.6080/K05D8Q1T): one zip, `V1_Vasarely_data.zip`,\nstreamed from the public bucket `crcnsarchive` (`pvc-12/live/`) and opened in place. CRCNS data\nsets have no versions, so the version is recorded as `unversioned`, and the MD5 of the zip from\nthe data set's `checksums.md5` (e1301fe463e72332e2303b2053ee0559) is printed below so that a later\nchange can be detected. The paper cites the data set by its DOI only; there is one published copy\n(`live/`), and it is the one used.\n\n**Data descriptor.** The data set's documentation (version 0.7, Feb 15, 2018) describes per\nneuron and experiment a spike rate map file and a stimulus file, and says the data set holds 53\nneurons. The files hold an ROI-registered copy of each map (`Standard`) that the descriptor does\nnot mention; the analysis rests on it (see the data check).\n\n| Claim | Tested here |\n|---|---|\n| neuron-counts | tested |\n| spikes-per-condition | blocked: the spike counts and eye times are not in the data set |\n| s4-baseline-no-difference | tested |\n| fig4a-above-baseline | tested |\n| fig4b-spike-rate-difference | tested |\n| fig4b-pairwise-significance | tested |\n| fig5-average-maps | tested |\n| table1-edge, table1-p180, table1-s90, table1-s52, table1-s40 | tested |\n| fig6-midpoint-representative | tested |\n| fig7a-rms-contrast-fit | tested (from the stimulus images) |\n| fig7c-fold-edge-equivalence | tested |\n| fig7c-fold-edge-significance | tested |\n| fig7d-nonlinear | tested |\n| fig7d-dog-similar | blocked: the DOG model output of reference [3] is not public as data |\n| s3-latency-peak | blocked: the maps are made at one latency (60 ms); no spike times or eye positions |\n\"\"\")\n\ncode(r\"\"\"\nimport time\nimport resource\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.optimize import least_squares\nfrom scipy.signal import fftconvolve\nfrom statsmodels.stats.multitest import multipletests\n\nimport vasarely as v\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\nprint(\"checksums.md5 of the data set:\")\nprint(v.checksums())\nz = v.open_zip()\nrecs = v.load_all(z)\nsheet = v.spreadsheet(z)\nprint(f\"data set {v.DATASET_ID} ({v.DATASET_VERSION}, doi:{v.DOI}); {len(recs)} spike rate map files \"\n      f\"loaded in {time.time() - started:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nEach check of the description against the values is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\ninfo = pd.DataFrame([{k: r.get(k) for k in [\"file\", \"condition\", \"prefix\", \"cell\", \"suffix\", \"monkey\", \"format\",\n                                             \"registered\"]} | {\n    \"has_BaseActivity\": bool(np.isfinite(r.get(\"base_dataset\", np.nan))),\n    \"fields\": \",\".join(r[\"fields\"]) if isinstance(r[\"fields\"], list) else r[\"fields\"]} for r in recs])\nprint(\"Spike rate map files by experiment, format, and whether they hold the registered map `Standard`:\")\nprint(pd.crosstab([info.condition, info.format], info.registered, margins=True).to_string())\nprint(\"\\n... and the undocumented BaseActivity:\")\nprint(pd.crosstab(info.condition, info.has_BaseActivity).to_string())\nprint(\"\\nFiles by monkey (J or A, from the cell code) and experiment:\")\nprint(pd.crosstab(info.monkey, info.condition, margins=True).to_string())\nprint(\"\\nTop-level fields of the spike rate map files (count of files):\")\nprint(info.fields.value_counts().to_string())\nprint(\"\\nEvery stimulus file has a spike rate map file and the reverse:\",\n      sorted(n.replace(\"_Stimulus\", \"\") for n in z.namelist() if n.endswith(\"_Stimulus.mat\")) ==\n      sorted(n.replace(\"_SpikeRateMap\", \"\") for n in z.namelist() if n.endswith(\"_SpikeRateMap.mat\")))\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nThe descriptor names three fields (image, smoothed_image, smoothed_image_norm); every file has\nthe first two, 37 of 77 have `smoothed_image_norm`, and 60 of 77 have `Standard`, the map\nregistered to the stimulus. All 17 files without `Standard` are Star files, two of them (prefix\nABS) in an older layout (one saved as MATLAB v7.3). Prefixes are ABC (Corners), ABD and ABS (Star)\nand AEC (Edge-compare); the letter after the cell number (A to E) is not explained anywhere.\n\"\"\")\n\ncode(r\"\"\"\ncells_files = info.groupby(\"cell\").condition.apply(lambda s: sorted(s)).rename(\"files\")\nsheet_marks = sheet.set_index(\"Cell\")[[\"Corners\", \"Star\", \"Edge-Compare\"]]\nsheet_marks.columns = [\"Corners\", \"Star\", \"Edge-compare\"]\nlisted = sheet_marks.apply(lambda r: sorted(c for c in r.index if r[c]), axis=1).rename(\"spreadsheet\")\ncmp = pd.concat([listed, cells_files], axis=1)\ncmp[\"files\"] = cmp[\"files\"].apply(lambda x: x if isinstance(x, list) else [])\ncmp[\"spreadsheet\"] = cmp[\"spreadsheet\"].apply(lambda x: x if isinstance(x, list) else [])\nprint(f\"Spreadsheet rows (cells): {len(sheet)}; with at least one experiment marked: {int(sheet_marks.any(axis=1).sum())}\")\nprint(\"Spreadsheet marks per experiment:\", sheet_marks.sum().to_dict())\nprint(\"Cells with files:\", cells_files.size)\nmismatch = cmp[cmp.spreadsheet.apply(tuple) != cmp.files.apply(tuple)]\nprint(\"\\nCells where the spreadsheet and the files disagree:\")\nprint(mismatch.to_string() if len(mismatch) else \"none\")\nprint(\"\\nSpreadsheet rows with no experiment marked:\", sheet.loc[~sheet_marks.any(axis=1).values, \"Cell\"].tolist())\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nThe spreadsheet lists 58 cells, the paper's number of analysed neurons, but marks an experiment for\nonly 53, which is the number the data descriptor gives; the files match the spreadsheet's marks\ncell by cell.\n\"\"\")\n\ncode(r\"\"\"\n# Duplicates: identical maps deposited under two names\nimport hashlib\nhashes = {}\nfor r in recs:\n    if r[\"registered\"]:\n        h = hashlib.md5(np.round(r[\"rate\"], 9).tobytes()).hexdigest()\n        hashes.setdefault(h, []).append(r[\"file\"])\ndups = [f for f in hashes.values() if len(f) > 1]\nprint(\"Registered maps that are identical in two files:\", dups if dups else \"none\")\n# Also the gaze-frame maps of all v5 files\nfull = {}\nfor name in sorted(n for n in z.namelist() if n.endswith(\"_SpikeRateMap.mat\")):\n    d = v.read_mat(z, name)\n    if hasattr(d, \"_fieldnames\"):\n        full.setdefault(hashlib.md5(np.asarray(d.smoothed_image).tobytes()).hexdigest(), []).append(name.split(\"/\")[-1])\nprint(\"Gaze-frame maps that are identical in two files:\", [f for f in full.values() if len(f) > 1] or \"none\")\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\n### Units and smoothing of the maps\n\"\"\")\n\ncode(r\"\"\"\neye = [r for r in recs if \"eyetime_s\" in r]\nfor r in eye:\n    print(f\"{r['file']}: eye time {r['eyetime_s']:.1f} s; image * eyetime is an integer count at every pixel: \"\n          f\"{r['count_is_integer']}; total {r['spikes_from_eyetime']:.0f} spikes\")\nmx = pd.Series({r[\"file\"]: r[\"full_image_max\"] for r in recs if \"full_image_max\" in r})\nprint(f\"Maximum of `image` over files: min {mx.min():.3f}, max {mx.max():.3f} (a pixel seen for one 1 ms sample with one spike)\")\nsm = pd.Series({r[\"file\"]: r[\"full_smoothed_max_hz\"] for r in recs if \"full_smoothed_max_hz\" in r})\nprint(f\"Peak of smoothed_image times 1000 (spikes/s): {sm.min():.1f} to {sm.max():.1f}\")\nreg = [r for r in recs if r[\"registered\"]]\nrate_all = np.concatenate([r[\"rate\"].ravel() for r in reg])\nprint(f\"Registered smoothed maps (spikes/s): min {rate_all.min():.2f}, median {np.median(rate_all):.2f}, max {rate_all.max():.1f}\")\nprint(\"Registered map sizes (rows x cols) by experiment:\",\n      {c: sorted({r['rate'].shape for r in reg if r['condition'] == c}) for c in v.CONDITIONS})\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\n`image` is the unsmoothed spike count divided by the eye time in 1 ms samples: in the one file\nthat also stores `eyetime`, the product is an integer count everywhere. So the maps are spikes per\nsample, and times 1000 they are spikes/s, consistent with the paper's units (Table 1, spikes per s)\nand with peak rates of 18 to 140 spikes/s. The descriptor calls `image` \"the raw spikes counts\";\nthe values are rates, not counts.\n\"\"\")\n\ncode(r\"\"\"\ndef fspecial(n, s):\n    x = np.arange(n) - (n - 1) / 2\n    g = np.exp(-(x[:, None] ** 2 + x[None, :] ** 2) / (2 * s * s))\n    return g / g.sum()\n\nrows = []\nfor name in [\"Edge-compare/AEC071800J1\", \"Star/ABD071200J1\", \"Corners/ABC050900J1A\"]:\n    d = v.read_mat(z, f\"V1_Vasarely_data/{name}_SpikeRateMap.mat\")\n    img = d.image.toarray()\n    for n, s in [(16, 7), (16, 5)]:\n        c = fftconvolve(img, fspecial(n, s), mode=\"full\")[n // 2:n // 2 + 480, n // 2:n // 2 + 640]\n        rows.append({\"file\": name, \"kernel\": f\"{n} px, SD {s}\", \"r\": np.corrcoef(c.ravel(), d.smoothed_image.ravel())[0, 1],\n                     \"max abs diff / peak\": np.abs(c - d.smoothed_image).max() / d.smoothed_image.max()})\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nSmoothing `image` with the Gaussian of the Fig 3B legend (16 DU, SD 7 DU) does not give\n`smoothed_image` exactly: the two correlate closely but differ by up to about a third of the peak.\nThe smoothing the files used is therefore not the one described, or not applied to `image` alone;\nthe analysis uses the files' own smoothed maps.\n\"\"\")\n\nmd(r\"\"\"\n### Registration of the maps to the stimulus\n\n`Standard` holds the map rotated so that the aligned fold is vertical and cropped to the ROI, with\nthe stimulus's equal-luminance polygons in the same frame. The map in `Standard` matches the\ngaze-frame `smoothed_image` after the same rotation as the stimulus and a shift that differs from\nneuron to neuron (the receptive field position), which the files do not store. Below, for each\nfold, the stimulus luminance read from each file's own stimulus image, resampled into the\nStandard frame by the transform fitted on the polygons, at 5%, 50% and 95% of the fold, and the\n\"ridge\" (luminance on the fold minus beside it; positive on a bright fold).\n\"\"\")\n\ncode(r\"\"\"\nchk = pd.DataFrame([{\"file\": r[\"file\"], \"condition\": r[\"condition\"], **v.check_luminance(r)} for r in reg])\nfor c, g in chk.groupby(\"condition\"):\n    g = g.dropna(axis=1, how=\"all\").drop(columns=[\"file\", \"condition\"])\n    print(f\"--- {c} ({len(g)} files): luminance, % (min to max over files)\")\n    print(g.agg([\"min\", \"max\"]).T.round(1).to_string())\nprint(\"\\nBright S40 fold per Corners file:\", pd.Series([v.bright_corner_fold(r) for r in reg if r[\"condition\"] == \"Corners\"]).value_counts().to_dict())\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nIn every registered file the folds run from 0% to 100% luminance as the paper describes, the\nSquare and Star folds are bright ridges, P180 is flat (ridge 0), and the baseline squares lie on\n0% luminance (the Corners images code 0% as 1.01). Of the two 40 degree folds of Corners, the one\nwhose apex points down in the Standard frame is the bright one in all 26 files; it is the S40 fold\nused. The Edge \"ridge\" is not meaningful, as the Edge is a boundary.\n\nA spatial check that the maps are registered to the stimulus: on Square and Edge, the paper's\nneurons respond along the Edge (Table 1). The cell below compares, per neuron, the mean rate in a\nband 8 DU wide along the Edge with the same band moved sideways by 24 to 64 DU, in both directions.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor r in reg:\n    if r[\"condition\"] != \"Edge-compare\":\n        continue\n    M = r[\"rate\"]\n    x, y0, y1 = r[\"folds\"][\"Edge\"]\n    yc, L = (y0 + y1) / 2, abs(y1 - y0)\n    on = v.box_mean(M, x, yc, 8, L)\n    off = [v.box_mean(M, x + s, yc, 8, L) for s in (-64, -48, -32, -24, 24, 32, 48, 64)]\n    rows.append({\"file\": r[\"file\"], \"on_edge\": on, \"max_shifted\": np.nanmax(off), \"on_is_max\": on > np.nanmax(off)})\nreg_chk = pd.DataFrame(rows)\nprint(reg_chk.round(2).to_string(index=False))\nprint(f\"\\nEdge band above every shifted band in {reg_chk.on_is_max.sum()} of {len(reg_chk)} neurons; \"\n      f\"median on {reg_chk.on_edge.median():.1f} against median of the shifted maxima {reg_chk.max_shifted.median():.1f} spikes/s\")\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\n### Baseline\n\nTwo readings of the absolute baseline are carried through (see the helper's docstring):\n\"squares\", the 16 x 16 DU squares the Methods describe, placed as the helper says (the Corners\nplacement is an assumption), and \"dataset\", the undocumented `BaseActivity` of the file where\nthere is one. The cell compares them.\n\"\"\")\n\ncode(r\"\"\"\nbase_rows = []\nfor r in reg:\n    centres = v.baseline_squares(r[\"rate\"].shape, r[\"condition\"], r[\"folds\"])\n    base_rows.append({\"file\": r[\"file\"], \"cell\": r[\"cell\"], \"monkey\": r[\"monkey\"], \"condition\": r[\"condition\"],\n                      \"base_squares\": v.baseline(r[\"rate\"], centres), \"base_dataset\": r[\"base_dataset\"],\n                      \"base_squares_unsmoothed\": v.baseline(r[\"rate_unsmoothed\"], centres)})\nB = pd.DataFrame(base_rows)\nboth = B.dropna(subset=[\"base_dataset\"])\nprint(f\"Files with both: {len(both)}; Pearson r = {np.corrcoef(both.base_squares, both.base_dataset)[0, 1]:.3f}; \"\n      f\"median |difference| {np.median(np.abs(both.base_squares - both.base_dataset)):.2f} spikes/s\")\nprint(both.groupby(\"condition\").apply(lambda g: pd.Series({\n    \"n\": len(g), \"r\": np.corrcoef(g.base_squares, g.base_dataset)[0, 1],\n    \"median squares\": g.base_squares.median(), \"median dataset\": g.base_dataset.median()})).round(2).to_string())\nprint(\"\\nBaseline range (spikes/s), squares:\", B.base_squares.min().round(2), \"to\", B.base_squares.max().round(2),\n      \"; dataset:\", B.base_dataset.min().round(2), \"to\", B.base_dataset.max().round(2))\nprint(\"Files whose BaseActivity is exactly 0:\", B.loc[B.base_dataset == 0, \"file\"].tolist())\n\"\"\", [\"sanity\"])\n\nmd(r\"\"\"\nThe two baselines agree only roughly, and no placement of 16 x 16 DU squares tried while preparing\nreproduced `BaseActivity` (not run here); how `BaseActivity` was computed is not documented. Two\nfiles have a `BaseActivity` of exactly 0 spikes/s.\n\"\"\")\n\nmd(r\"\"\"\n### Per-neuron measures\n\nAll claims below use these tables. Each registered file gives, per fold, the midpoint response\n(8 x 8 DU), the spike rate difference (response minus baseline) and the ten block differences.\nNeurons are those with a registered map: 22 Square and Edge, 12 Star and 26 Corners (paper: 25, 30\nand 28). Star files without `Standard` cannot be placed on the stimulus and are left out.\n\"\"\")\n\ncode(r\"\"\"\nFOLDS = [\"P180\", \"S90\", \"S52\", \"S40\"]\nANGLE = {\"P180\": 180, \"S90\": 90, \"S52\": 52, \"S40\": 40}\nrows = []\nfor r, b in zip(reg, base_rows):\n    for reading, base in [(\"squares\", b[\"base_squares\"]), (\"dataset\", b[\"base_dataset\"])]:\n        for smoothed in (True, False):\n            if not smoothed and reading == \"dataset\":\n                continue\n            bb = base if smoothed else b[\"base_squares_unsmoothed\"]\n            for fold, m in v.fold_measures(r, bb, smoothed=smoothed).items():\n                rows.append({\"file\": r[\"file\"], \"cell\": r[\"cell\"], \"monkey\": r[\"monkey\"], \"condition\": r[\"condition\"],\n                             \"base_reading\": reading, \"smoothed\": smoothed, \"fold\": fold, \"base\": bb,\n                             \"response\": m[\"response\"], \"diff\": m[\"diff\"], \"blocks\": m[\"blocks\"]})\nT = pd.DataFrame(rows)\nmain = T[(T.base_reading == \"squares\") & T.smoothed]\nprint(\"Neurons per fold (main reading):\", main.groupby(\"fold\").size().to_dict())\nprint(\"Neurons per fold with a dataset BaseActivity:\", T[(T.base_reading == \"dataset\") & T[\"diff\"].notna()].groupby(\"fold\").size().to_dict())\nprint(main.groupby(\"fold\")[[\"response\", \"base\", \"diff\"]].agg([\"min\", \"median\", \"max\"]).round(2).to_string())\n\ndef by(reading=\"squares\", smoothed=True):\n    t = T[(T.base_reading == reading) & (T.smoothed == smoothed)].dropna(subset=[\"diff\"])\n    return {f: g.set_index(\"file\") for f, g in t.groupby(\"fold\")}\n\"\"\", [\"sanity\"])\n\n# ---------------- claims ----------------\n\nmd(r\"\"\"\n## neuron-counts\n\n> Of 118 V1 neurons recorded from two monkeys (102 from monkey J, 16 from monkey A), 60 were\n> discarded for technical problems and 58 analysed; 7 were tested in all three conditions, 11 in\n> two and 40 in one, giving 25 neurons for Square and Edge, 30 for Star and 28 for Corners.\n\"\"\")\n\ncode(r\"\"\"\npaper = {\"neurons analysed\": 58, \"Square and Edge\": 25, \"Star\": 30, \"Corners\": 28,\n         \"in all three\": 7, \"in two\": 11, \"in one\": 40}\nnconds = info.groupby(\"cell\").condition.nunique()\nours = {\"neurons analysed\": nconds.size, \"Square and Edge\": (info.condition == \"Edge-compare\").sum(),\n        \"Star\": (info.condition == \"Star\").sum(), \"Corners\": (info.condition == \"Corners\").sum(),\n        \"in all three\": int((nconds == 3).sum()), \"in two\": int((nconds == 2).sum()), \"in one\": int((nconds == 1).sum())}\nregi = info[info.registered]\nnreg = regi.groupby(\"cell\").condition.nunique()\nours_reg = {\"neurons analysed\": nreg.size, \"Square and Edge\": (regi.condition == \"Edge-compare\").sum(),\n            \"Star\": (regi.condition == \"Star\").sum(), \"Corners\": (regi.condition == \"Corners\").sum(),\n            \"in all three\": int((nreg == 3).sum()), \"in two\": int((nreg == 2).sum()), \"in one\": int((nreg == 1).sum())}\ntab = pd.DataFrame({\"paper\": paper, \"files\": ours, \"registered files\": ours_reg})\ntab[\"files match\"] = tab.paper == tab.files\nprint(tab.to_string())\nprint(\"\\nCells by monkey (files):\", info.drop_duplicates(\"cell\").monkey.value_counts().to_dict(),\n      \"; spreadsheet rows by monkey:\", sheet.Cell.str[-2].value_counts().to_dict())\nprint(\"Sum over experiments, paper 7*3 + 11*2 + 40 =\", 7 * 3 + 11 * 2 + 40, \"; files:\", len(info))\n\"\"\", [\"claim:neuron-counts\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** The files hold 53 cells (A 6, J 47 by the cell code), with 22 Square\nand Edge, 29 Star and 26 Corners files, and 6 cells in all three experiments, 12 in two and 35 in\none; none of the paper's counts match. The spreadsheet lists 58 cells, the paper's number, but\nfive have no experiment and no files. Of these, 60 files can be placed on the stimulus (22, 12 and\n26).\n\"\"\")\n\nmd(r\"\"\"\n## spikes-per-condition (blocked)\n\n> Each experimental condition required at least 10,000 spikes, and the mean number of spikes per\n> condition was 35,998 (STD 25,981).\n\nThe number of spikes needs the spike count map or the eye time map, which the files do not hold:\n`image` is a rate (count divided by eye time). One file of 77 also stores its eye time, and its\ncount is printed in the data check (one neuron and condition). The claim is blocked.\n\"\"\")\n\nmd(r\"\"\"\n## s4-baseline-no-difference\n\n> Absolute baseline activity did not differ significantly across the three visual stimuli\n> (Square and Edge, Star, Corners).\n\"\"\")\n\ncode(r\"\"\"\ndef baseline_tests(col, label):\n    g = {c: B.loc[B.condition == c, col].dropna().values for c in v.CONDITIONS}\n    print(f\"--- baseline reading: {label}\")\n    print(pd.DataFrame({c: {\"n\": len(x), \"q25\": np.percentile(x, 25), \"median\": np.median(x), \"q75\": np.percentile(x, 75),\n                            \"min\": x.min(), \"max\": x.max(), \"mean\": x.mean()} for c, x in g.items()}).round(2).to_string())\n    pairs = [(\"Edge-compare\", \"Star\"), (\"Edge-compare\", \"Corners\"), (\"Star\", \"Corners\")]\n    p = [stats.ranksums(g[a], g[b]).pvalue for a, b in pairs]\n    q = multipletests(p, method=\"fdr_bh\")[1]\n    for (a, b), pp, qq in zip(pairs, p, q):\n        print(f\"(a) rank sum {a} vs {b}: p = {pp:.4f}, BH = {qq:.4f}\")\n    kw = stats.kruskal(*g.values())\n    an = stats.f_oneway(*g.values())\n    print(f\"(b) Kruskal-Wallis H = {kw.statistic:.2f}, p = {kw.pvalue:.4f}\")\n    print(f\"(c) one-way ANOVA F = {an.statistic:.2f}, p = {an.pvalue:.4f}\")\n    return min(q), kw.pvalue, an.pvalue\n\nres_s4 = {lab: baseline_tests(col, lab) for col, lab in [(\"base_squares\", \"squares (main)\"), (\"base_dataset\", \"dataset BaseActivity\")]}\nfor lab, (qa, pb, pc) in res_s4.items():\n    print(f\"{lab}: any reading significant at 0.05: {min(qa, pb, pc) < 0.05}\")\n# by monkey, main reading\nprint(\"\\nMedian baseline by monkey and experiment (squares):\")\nprint(B.pivot_table(index=\"monkey\", columns=\"condition\", values=\"base_squares\", aggfunc=[\"count\", \"median\"]).round(2).to_string())\n\"\"\", [\"claim:s4-baseline-no-difference\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** With the paper's squares, the baselines differ across the stimuli\n(Square and Edge median 7.68, Star 1.84, Corners 2.45 spikes/s): Square and Edge against Corners\nis significant after BH correction, and the Kruskal-Wallis test is significant (p < 0.05), though\nthe ANOVA is not. With the files' own `BaseActivity` (fewer neurons) none of the three readings is\nsignificant. The outcome rests on the placement of the baseline squares, which for Corners is an\nassumption, and on 12 of the paper's 30 Star neurons.\n\"\"\")\n\nmd(r\"\"\"\n## fig4a-above-baseline\n\n> For every fold (P180, S90, S52, S40), most neurons' midpoint fold responses lie above their\n> absolute baseline activity, and the mass center of each fold's points lies above the line of\n> unit slope, with the mass center's distance from that line increasing as the fold angle\n> decreases.\n\"\"\")\n\ncode(r\"\"\"\ndef fig4a(reading):\n    d = by(reading)\n    rows = []\n    for f in FOLDS:\n        t = d[f]\n        pos = t[(t.response > 0) & (t.base > 0)]\n        rows.append({\"fold\": f, \"n\": len(t), \"above\": int((t.response > t.base).sum()),\n                     \"frac_above\": (t.response > t.base).mean(),\n                     \"(a) centre resp\": t.response.mean(), \"(a) centre base\": t.base.mean(),\n                     \"(a) distance\": t.response.mean() - t.base.mean(),\n                     \"(b) n log\": len(pos), \"(b) distance log10\": np.log10(pos.response).mean() - np.log10(pos.base).mean()})\n    out = pd.DataFrame(rows).set_index(\"fold\")\n    return out\n\nfor reading in [\"squares\", \"dataset\"]:\n    out = fig4a(reading)\n    print(f\"--- baseline reading: {reading}\")\n    print(out.round(3).to_string())\n    for col in [\"(a) distance\", \"(b) distance log10\"]:\n        dd = out[col].values\n        print(f\"{col}: ordered P180 < S90 < S52 < S40: {bool(np.all(np.diff(dd) > 0))}; all above the line: {bool((dd > 0).all())}\")\n    print(\"more than half above, every fold:\", bool((out.frac_above > 0.5).all()))\n\nfig, ax = plt.subplots(1, 4, figsize=(13, 3.2))\nd = by(\"squares\")\nfor a, f in zip(ax, FOLDS):\n    t = d[f]\n    a.loglog(t.base.clip(lower=0.05), t.response.clip(lower=0.05), \".\")\n    a.plot([0.05, 200], [0.05, 200], \"k:\")\n    a.plot(t.base.mean(), t.response.mean(), \"r+\", ms=12)\n    a.set_title(f); a.set_xlabel(\"baseline (spikes/s)\")\nax[0].set_ylabel(\"midpoint response (spikes/s)\")\nplt.tight_layout(); plt.show()\nprint(\"Values clipped at 0.05 spikes/s for the log axes:\", int(sum(((d[f].base < 0.05) | (d[f].response < 0.05)).sum() for f in FOLDS)))\n\"\"\", [\"claim:fig4a-above-baseline\"])\n\nmd(r\"\"\"\n**Result: reproduced.** With the paper's squares, more than half of the neurons lie above their\nbaseline for every fold, every mass centre lies above the unit line, and its distance increases\nfrom P180 to S40 under both readings of the mass centre (raw means and log means). The order and\nthe majority also hold with the files' `BaseActivity`, though there under the log reading S52 is\nnot below S40 is shown above. The result rests on 12 Star neurons.\n\"\"\")\n\nmd(r\"\"\"\n## fig4b-spike-rate-difference\n\n> The mean spike rate difference at the fold midpoint decreases with increasing fold angle, from\n> S40 (25.60 spikes/s) through S52 (18.10) and S90 (10.69) to P180 (4.87).\n\"\"\")\n\ncode(r\"\"\"\nPAPER_MID = {\"S40\": (25.60, 4.18), \"S52\": (18.10, 2.39), \"S90\": (10.69, 1.94), \"P180\": (4.87, 1.15)}\n\ndef mid_table(reading=\"squares\", smoothed=True):\n    d = by(reading, smoothed)\n    rows = []\n    for f in [\"S40\", \"S52\", \"S90\", \"P180\"]:\n        t = d[f][\"diff\"]\n        exp, tol = PAPER_MID[f]\n        rows.append({\"fold\": f, \"n\": len(t), \"mean\": t.mean(), \"sem\": t.sem(), \"median\": t.median(),\n                     \"paper\": exp, \"tolerance\": tol, \"within\": abs(t.mean() - exp) <= tol})\n    out = pd.DataFrame(rows).set_index(\"fold\")\n    out.attrs[\"ordered\"] = bool(np.all(np.diff(out[\"mean\"].values) < 0))\n    return out\n\nfor reading, smoothed in [(\"squares\", True), (\"dataset\", True), (\"squares\", False)]:\n    out = mid_table(reading, smoothed)\n    print(f\"--- baseline {reading}, {'smoothed' if smoothed else 'unsmoothed'} map: ordered S40 > S52 > S90 > P180: {out.attrs['ordered']}\")\n    print(out.round(2).to_string())\n# by monkey, main reading\nd = by(\"squares\")\nprint(\"\\nMean difference by monkey (main reading):\")\nprint(pd.DataFrame({f: d[f].groupby(\"monkey\")[\"diff\"].agg([\"count\", \"mean\"]).stack() for f in FOLDS}).round(2).to_string())\n# Corners: dark fold for reference\nprint(f\"\\nCorners dark S40 fold (not used by the paper): mean {d['S40dark']['diff'].mean():.2f} ± {d['S40dark']['diff'].sem():.2f}\")\n\"\"\", [\"claim:fig4b-spike-rate-difference\"])\n\nmd(r\"\"\"\n**Result: partially reproduced.** With the paper's squares and the smoothed map, the means are\nordered S40 > S52 > S90 > P180 (26.41, 19.10, 8.21 and 3.88 spikes/s), and S40, S52 and P180 are\nwithin the paper's SEM, while S90 is 0.54 spikes/s below its range. With the files'\n`BaseActivity` the order holds and only S90 is within tolerance; with the unsmoothed map the order\nalso holds (values above). The S40 value rests on the assumed placement of the Corners baseline\nsquares; the Star value on 12 of 30 neurons.\n\"\"\")\n\nmd(r\"\"\"\n## fig4b-pairwise-significance\n\n> The midpoint spike rate difference for S40 is significantly larger than for S90 and for P180,\n> and that for S52 is significantly larger than for P180.\n\"\"\")\n\ncode(r\"\"\"\ndef pairwise(reading=\"squares\"):\n    d = by(reading)\n    pairs = [(\"S40\", \"S52\"), (\"S40\", \"S90\"), (\"S40\", \"P180\"), (\"S52\", \"S90\"), (\"S52\", \"P180\"), (\"S90\", \"P180\")]\n    rows = []\n    for a, b in pairs:\n        x, y = d[a][\"diff\"], d[b][\"diff\"]\n        rows.append({\"pair\": f\"{a} > {b}\", \"mean diff\": x.mean() - y.mean(), \"p\": stats.ranksums(x, y).pvalue,\n                     \"direction ok\": x.mean() > y.mean(), \"named\": (a, b) in [(\"S40\", \"S90\"), (\"S40\", \"P180\"), (\"S52\", \"P180\")]})\n    out = pd.DataFrame(rows)\n    out[\"BH (a) six pairs\"] = multipletests(out.p, method=\"fdr_bh\")[1]\n    out[\"BH (b) three named\"] = np.nan\n    out.loc[out.named, \"BH (b) three named\"] = multipletests(out.loc[out.named, \"p\"], method=\"fdr_bh\")[1]\n    return out\n\nfor reading in [\"squares\", \"dataset\"]:\n    out = pairwise(reading)\n    print(f\"--- baseline {reading}\")\n    print(out.round(5).to_string(index=False))\n    named = out[out.named]\n    for col in [\"BH (a) six pairs\", \"BH (b) three named\"]:\n        print(f\"{col}: all three named pairs significant in direction: {bool(((named[col] < 0.05) & named['direction ok']).all())}\")\n\"\"\", [\"claim:fig4b-pairwise-significance\"])\n\nmd(r\"\"\"\n**Result: reproduced.** With the paper's squares, S40 > S90, S40 > P180 and S52 > P180 are\nsignificant by rank sum tests with BH correction under both families (all six pairs, or the three\nnamed), with the p-values shown above. With the files' `BaseActivity`, the same three pairs are\nsignificant under both families as well.\n\"\"\")\n\nmd(r\"\"\"\n## fig5-average-maps\n\n> The population-average spike rate difference maps show neural activity increasing as the\n> corner angle decreases.\n\"\"\")\n\ncode(r\"\"\"\ndef avg_map(condition, reading=\"squares\"):\n    maps = []\n    for r, b in zip(reg, base_rows):\n        if r[\"condition\"] != condition:\n            continue\n        base = b[\"base_squares\"] if reading == \"squares\" else b[\"base_dataset\"]\n        if np.isfinite(base):\n            maps.append((r, r[\"rate\"] - base))\n    shapes = {m.shape for _, m in maps}\n    # Corners maps come in two sizes; the smaller is the larger cropped by 8 DU on each side\n    H, W = max(shapes)\n    stack = []\n    for r, m in maps:\n        pad = (H - m.shape[0]) // 2\n        stack.append(np.pad(m, pad, constant_values=np.nan) if pad else m)\n    ref = next(r for r, m in maps if m.shape == (H, W))\n    return np.nanmean(stack, axis=0), ref, len(stack)\n\nrows = []\nfig, ax = plt.subplots(1, 3, figsize=(12, 4))\nfor a, cond in zip(ax, v.CONDITIONS):\n    A, ref, n = avg_map(cond)\n    im = a.imshow(A, cmap=\"viridis\"); a.set_title(f\"{v.CONDITIONS[cond]} (N = {n})\"); plt.colorbar(im, ax=a)\n    print(f\"{cond}: average map range {np.nanmin(A):.2f} to {np.nanmax(A):.2f} spikes/s\")\n    fake = dict(ref, rate=A + 0.0, rate_unsmoothed=A + 0.0)\n    for fold, m in v.fold_measures(fake, 0.0).items():\n        if fold in FOLDS:\n            rows.append({\"fold\": fold, \"N\": n, \"midpoint of average map\": m[\"diff\"],\n                         \"mean of the ten blocks\": np.mean(np.mean(m[\"blocks\"], axis=0))})\nplt.tight_layout(); plt.show()\nf5 = pd.DataFrame(rows).set_index(\"fold\").loc[[\"S40\", \"S52\", \"S90\", \"P180\"]]\nprint(f5.round(2).to_string())\nfor col in f5.columns[1:]:\n    print(f\"{col}: ordered S40 > S52 > S90 > P180: {bool(np.all(np.diff(f5[col].values) < 0))}\")\n\"\"\", [\"claim:fig5-average-maps\"])\n\nmd(r\"\"\"\n**Result: reproduced.** The average maps, read at the midpoint squares, are ordered S40 > S52 >\nS90 > P180, as the criterion requires; as the claims file notes, this repeats the means of\nfig4b-spike-rate-difference. The variant, the mean over the ten fold blocks of the average map, is\nordered the same way.\n\"\"\")\n\nmd(r\"\"\"\n## Table 1 (table1-edge, table1-p180, table1-s90, table1-s52, table1-s40)\n\nTen blocks along each fold from 0% to 100% luminance, 8 DU wide, 10% of the fold long; per neuron\nthe minimum, maximum, mean and median of the ten block differences, and the midpoint. Reading (a):\nper neuron, then mean ± SEM over neurons. Reading (b): the same summaries of the population-average\nprofile. For S90 and S52, reading (i) averages the two half-diagonals block by block; reading (ii)\nsummarises each half on its own and averages the two summaries per neuron.\n\"\"\")\n\ncode(r\"\"\"\nPAPER_T1 = {\n    \"Edge\": [(7.98, 1.60), (33.13, 5.11), (20.44, 3.33), (20.77, 3.48), (22.01, 3.41)],\n    \"P180\": [(0.18, 1.01), (10.28, 1.53), (4.55, 1.12), (4.03, 1.06), (4.87, 1.15)],\n    \"S90\": [(4.36, 1.07), (14.61, 2.48), (9.22, 1.61), (9.31, 1.62), (10.69, 1.94)],\n    \"S52\": [(6.26, 1.33), (25.39, 3.52), (15.66, 2.23), (15.93, 2.36), (18.10, 2.39)],\n    \"S40\": [(9.33, 1.69), (35.11, 4.17), (22.81, 3.11), (22.83, 3.48), (25.60, 4.18)],\n}\nSTATS = [\"min\", \"max\", \"mean\", \"median\", \"midpoint\"]\n\ndef summaries(blocks_list, half_mode):\n    if half_mode == \"i\" or len(blocks_list) == 1:\n        b = np.mean(blocks_list, axis=0)\n        return np.array([np.nanmin(b), np.nanmax(b), np.nanmean(b), np.nanmedian(b)])\n    return np.mean([[np.nanmin(b), np.nanmax(b), np.nanmean(b), np.nanmedian(b)] for b in blocks_list], axis=0)\n\ndef table1(fold, reading=\"squares\"):\n    t = by(reading)[fold]\n    out = {}\n    for half in ([\"i\", \"ii\"] if fold in (\"S90\", \"S52\") else [\"i\"]):\n        per = np.array([summaries(b, half) for b in t.blocks])\n        per = np.c_[per, t[\"diff\"].values]\n        a = pd.DataFrame({\"(a) mean\": per.mean(0), \"(a) sem\": per.std(0, ddof=1) / np.sqrt(len(per))}, index=STATS)\n        if half == \"i\":\n            prof = np.mean([np.mean(b, axis=0) for b in t.blocks], axis=0)\n            bvals = [np.nanmin(prof), np.nanmax(prof), np.nanmean(prof), np.nanmedian(prof), t[\"diff\"].mean()]\n        else:\n            halves = np.array([np.array(b) for b in t.blocks])  # neurons x halves x blocks\n            bvals = list(np.mean([[np.nanmin(p), np.nanmax(p), np.nanmean(p), np.nanmedian(p)] for p in halves.mean(0)], axis=0)) + [t[\"diff\"].mean()]\n        a[\"(b) population profile\"] = bvals\n        a[\"paper\"] = [p for p, _ in PAPER_T1[fold]]\n        a[\"tolerance\"] = [s for _, s in PAPER_T1[fold]]\n        a[\"(a) within\"] = (a[\"(a) mean\"] - a.paper).abs() <= a.tolerance\n        a[\"(b) within\"] = (a[\"(b) population profile\"] - a.paper).abs() <= a.tolerance\n        out[half] = a\n    return out, len(t)\n\ndef report_table1(fold):\n    res = {}\n    for reading in [\"squares\", \"dataset\"]:\n        tabs, n = table1(fold, reading)\n        for half, a in tabs.items():\n            key = f\"{reading}, halves ({half})\" if fold in (\"S90\", \"S52\") else reading\n            print(f\"--- {fold}, baseline {key}, N = {n}\")\n            print(a.round(2).to_string())\n            for r in [\"(a)\", \"(b)\"]:\n                k = int(a[f\"{r} within\"].sum())\n                res[(key, r)] = k\n                print(f\"reading {r}: {k} of 5 within tolerance\")\n    return res\n\"\"\")\n\nfor fold, cid in [(\"Edge\", \"table1-edge\"), (\"P180\", \"table1-p180\"), (\"S90\", \"table1-s90\"), (\"S52\", \"table1-s52\"), (\"S40\", \"table1-s40\")]:\n    md(f\"### {cid}\\n\\n> Table 1, {fold}: minimum, maximum, mean and median over the ten blocks, and the midpoint.\")\n    code(f\"\"\"\nt1_{fold} = report_table1(\"{fold}\")\nd = by(\"squares\")[\"{fold}\"]\nprof = np.mean([np.mean(b, axis=0) for b in d.blocks], axis=0)\nprint(\"\\\\nPopulation-average block profile, 0% to 100% (main reading):\", np.round(prof, 2))\nprint(\"Block differences that are missing (ROI not covered):\", int(sum(np.isnan(np.array(b)).sum() for b in d.blocks)))\n\"\"\", [f\"claim:{cid}\"])\n    md({\n        \"Edge\": \"**Result: partially reproduced.** With the paper's squares, reading (a) puts four of the five values within tolerance (the maximum is above its range), and reading (b) two of five; with the files' `BaseActivity` (9 neurons) reading (a) gives four of five as well (above).\",\n        \"P180\": \"**Result: reproduced.** With the paper's squares, reading (a) puts all five values within the paper's SEM (above); the dataset baseline gives four of five under (a).\",\n        \"S90\": \"**Result: partially reproduced.** With the paper's squares, the best reading puts three of the five values within tolerance (above): the minimum, maximum and median under halves (ii) and reading (a), while the mean and the midpoint are below. With the files' `BaseActivity`, more values are within tolerance (above).\",\n        \"S52\": \"**Result: reproduced.** With the paper's squares, reading (a) puts all five values within tolerance under both half readings (above). The values rest on 12 of the paper's 30 Star neurons.\",\n        \"S40\": \"**Result: reproduced.** With the paper's squares and the bright S40 fold, reading (a) puts all five values within tolerance (above). The values rest on the assumed placement of the two Corners baseline squares.\",\n    }[fold])\n\nmd(r\"\"\"\n## fig6-midpoint-representative\n\n> For each fold and the Edge, the spike rate difference at the midpoint does not differ\n> significantly from the mean or the median spike rate difference along the fold or Edge, so the\n> midpoint response represents the whole fold.\n\"\"\")\n\ncode(r\"\"\"\ndef fig6(reading=\"squares\", half=\"i\"):\n    d = by(reading)\n    rows = []\n    for f in [\"Edge\", \"P180\", \"S90\", \"S52\", \"S40\"]:\n        t = d[f]\n        per = np.array([summaries(b, half) for b in t.blocks])\n        mid = t[\"diff\"].values\n        for k, col in [(\"mean\", 2), (\"median\", 3)]:\n            rows.append({\"fold\": f, \"against\": k, \"n\": len(mid), \"median(mid - along)\": np.median(mid - per[:, col]),\n                         \"rank sum p\": stats.ranksums(mid, per[:, col]).pvalue,\n                         \"signed rank p (variant)\": stats.wilcoxon(mid, per[:, col]).pvalue})\n    return pd.DataFrame(rows)\n\nfor reading in [\"squares\", \"dataset\"]:\n    for half in [\"i\", \"ii\"]:\n        out = fig6(reading, half)\n        print(f\"--- baseline {reading}, halves ({half})\")\n        print(out.round(4).to_string(index=False))\n        print(f\"rank sum tests significant at 0.05: {int((out['rank sum p'] < 0.05).sum())} of {len(out)}; \"\n              f\"signed rank (variant): {int((out['signed rank p (variant)'] < 0.05).sum())} of {len(out)}\")\n\"\"\", [\"claim:fig6-midpoint-representative\"])\n\nmd(r\"\"\"\n**Result: reproduced.** By the paper's test (rank sum, alpha 0.05, no correction), none of the ten\ncomparisons of midpoint against the mean or median along the fold is significant under either\nbaseline or half reading. The paired signed rank test, shown as a variant, does find the midpoint\nhigher than the mean along several folds (above), so the absence rests on the unpaired test the\npaper names.\n\"\"\")\n\nmd(r\"\"\"\n## fig7a-rms-contrast-fit\n\n> Local RMS contrast along the Edge rises from 0.61 to 0.943 with luminance and is fit by an\n> exponential model, f(l) = -0.34 exp(-0.05 l) + 0.95, with R2 = 0.9983.\n\"\"\")\n\ncode(r\"\"\"\nlevels = np.arange(0, 100 + 1e-9, v.RMS_STEP)\nedge_recs = [r for r in reg if r[\"condition\"] == \"Edge-compare\"]\ncurves = {r[\"file\"]: v.rms_contrast(r[\"lum\"], r[\"folds\"][\"Edge\"], levels) for r in edge_recs}\nref = curves[edge_recs[0][\"file\"]]\nspread = max(np.nanmax(np.abs(c[[\"a_sd_over_mean\", \"b_sd_norm\"]].values - ref[[\"a_sd_over_mean\", \"b_sd_norm\"]].values)) for c in curves.values())\nprint(f\"{len(curves)} Edge stimuli; largest difference between their RMS curves: {spread:.3f}\")\nmean_curve = pd.concat(curves.values()).groupby(\"level\").mean()\nprint(mean_curve.iloc[::6].round(3).to_string())\n\ndef model(p, l):\n    return p[0] * np.exp(-p[1] * l) + p[2]\n\nPAPER_FIT = {\"min\": (0.61, 0.061), \"max\": (0.943, 0.094), \"a\": (-0.34, 0.034), \"b\": (0.05, 0.005), \"c\": (0.95, 0.095), \"R2\": (0.9983, 0.0017)}\nfits = {}\nfor col in [\"a_sd_over_mean\", \"b_sd_norm\"]:\n    y = mean_curve[col].values; l = mean_curve.index.values; ok = np.isfinite(y)\n    for loss in [\"linear\", \"soft_l1\"]:   # least squares (Levenberg-Marquardt) and a robust fit standing in for LAR\n        p = least_squares(lambda p: model(p, l[ok]) - y[ok], x0=[-0.34, 0.05, 0.95], loss=loss,\n                          f_scale=0.01, method=\"lm\" if loss == \"linear\" else \"trf\").x\n        r2 = 1 - np.sum((y[ok] - model(p, l[ok])) ** 2) / np.sum((y[ok] - y[ok].mean()) ** 2)\n        vals = {\"min\": np.nanmin(y), \"max\": np.nanmax(y), \"a\": p[0], \"b\": p[1], \"c\": p[2], \"R2\": r2}\n        within = {k: abs(vals[k] - PAPER_FIT[k][0]) <= PAPER_FIT[k][1] for k in vals}\n        fits[(col, loss)] = (vals, within)\n        print(f\"reading {col}, fit {loss}: \" + \", \".join(f\"{k} {vals[k]:.4f}{'' if within[k] else ' (out)'}\" for k in vals))\npaper_curve = model([-0.34, 0.05, 0.95], levels)\nprint(f\"\\nPaper's curve at 0, 50 and 100%: {paper_curve[0]:.3f}, {model([-0.34, 0.05, 0.95], 50):.3f}, {paper_curve[-1]:.3f}\")\nplt.figure(figsize=(5, 3.2))\nplt.plot(mean_curve.index, mean_curve.a_sd_over_mean, \".\", label=\"(a) SD / mean\")\nplt.plot(mean_curve.index, mean_curve.b_sd_norm, \".\", label=\"(b) SD of 0-1 luminance\")\nplt.plot(levels, paper_curve, \"k-\", label=\"paper's fit\")\nplt.ylim(0, 1.5); plt.xlabel(\"Edge luminance (%)\"); plt.ylabel(\"RMS contrast\"); plt.legend(); plt.show()\nprint(\"Points of reading (a) above the axis (1.5):\", int((mean_curve.a_sd_over_mean > 1.5).sum()))\n\"\"\", [\"claim:fig7a-rms-contrast-fit\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** Neither reading of RMS contrast computed on the 22 Edge stimulus images\ngives the paper's curve: the SD over the mean is about 0.94 over most of the Edge but rises above\n1 near 0% (so its range is not 0.61 to 0.943), and the SD of the 0-1 luminance rises from 0.01 to\n0.45. Neither fit gives the paper's parameters (values above). The definition of RMS contrast the\npaper used (its reference [21]) is not in the text read.\n\"\"\")\n\nmd(r\"\"\"\n## fig7c-fold-edge-equivalence\n\n> Neural responses to P180 are roughly equivalent to those to a 50% contrast Edge, while\n> responses to S40 are close to those to a 90% contrast Edge.\n\"\"\")\n\ncode(r\"\"\"\nA_, B_, C_ = -0.34, 0.05, 0.95\nrms_levels = np.round(np.arange(0.610, 0.943 + 1e-9, 0.037), 3)\nlum_at_rms = -np.log((rms_levels - C_) / A_) / B_\nprint(\"RMS levels:\", rms_levels)\nprint(\"Luminance (%) of each level by the inverse of the paper's fit:\", np.round(lum_at_rms, 1))\n\ndef edge_table(reading=\"squares\"):\n    rows = []\n    for r, b in zip(reg, base_rows):\n        if r[\"condition\"] != \"Edge-compare\":\n            continue\n        base = b[\"base_squares\"] if reading == \"squares\" else b[\"base_dataset\"]\n        if not np.isfinite(base):\n            continue\n        rows.append({\"file\": r[\"file\"],\n                     **{(\"lum\", L): v.edge_response(r[\"rate\"], r[\"folds\"][\"Edge\"], L) - base for L in range(0, 101, 10)},\n                     **{(\"rms\", c): v.edge_response(r[\"rate\"], r[\"folds\"][\"Edge\"], L) - base for c, L in zip(rms_levels, lum_at_rms)}})\n    return pd.DataFrame(rows).set_index(\"file\")\n\ndef equivalence(reading=\"squares\"):\n    E = edge_table(reading)\n    m = mid_table(reading)\n    out = {}\n    for kind in [\"lum\", \"rms\"]:\n        cols = [c for c in E.columns if c[0] == kind]\n        means = E[cols].mean()\n        lv = np.array([c[1] for c in cols], float)\n        near = {f: lv[np.argmin(np.abs(means.values - m.loc[f, \"mean\"]))] for f in [\"P180\", \"S40\"]}\n        out[kind] = (means, near)\n        print(f\"--- baseline {reading}, Edge levels by {'luminance %' if kind == 'lum' else 'RMS contrast'}:\")\n        print(\"Edge mean response:\", \" \".join(f\"{l:g}:{x:.2f}\" for l, x in zip(lv, means.values)))\n        print(f\"P180 mean {m.loc['P180', 'mean']:.2f} -> nearest level {near['P180']:g}; S40 mean {m.loc['S40', 'mean']:.2f} -> nearest level {near['S40']:g}\")\n    ok_a = abs(out[\"lum\"][1][\"P180\"] - 50) <= 10 and abs(out[\"lum\"][1][\"S40\"] - 90) <= 10\n    step = 0.037\n    ok_b = out[\"rms\"][1][\"P180\"] == rms_levels[0] and abs(out[\"rms\"][1][\"S40\"] - 0.90) <= step + 1e-9\n    print(f\"(a) within one step of 50% and 90%: {ok_a}; (b) P180 at the lowest level and S40 within one step of 0.90: {ok_b}\")\n    return E\n\nE_main = equivalence(\"squares\")\n_ = equivalence(\"dataset\")\n\"\"\", [\"claim:fig7c-fold-edge-equivalence\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** With the paper's squares, under reading (a) the Edge level nearest the\nP180 mean and the one nearest the S40 mean are printed above, and they are not within one 10% step\nof 50% and 90% together; under reading (b) the S40 mean is not matched within one step of 0.90. The\nEdge responses here are lower than the paper's near the bright end (the Edge maximum block is above\nthe paper's range, but the 16 x 16 DU squares straddle the Edge).\n\"\"\")\n\nmd(r\"\"\"\n## fig7c-fold-edge-significance\n\n> Responses to P180 are significantly lower than responses to a 94% contrast Edge, and responses\n> to S40 are significantly higher than responses to an Edge of less than 68% contrast.\n\"\"\")\n\ncode(r\"\"\"\ndef fold_edge_tests(reading=\"squares\"):\n    E = edge_table(reading)\n    d = by(reading)\n    rows = []\n    for f in FOLDS:\n        x = d[f][\"diff\"].values\n        for c in rms_levels:\n            y = E[(\"rms\", c)].dropna().values\n            t = stats.ttest_ind(x, y)\n            rows.append({\"fold\": f, \"rms\": c, \"fold - edge\": x.mean() - y.mean(), \"t\": t.statistic, \"p\": t.pvalue})\n    T7 = pd.DataFrame(rows)\n    T7[\"BH all 40\"] = multipletests(T7.p, method=\"fdr_bh\")[1]\n    T7[\"BH per fold\"] = T7.groupby(\"fold\").p.transform(lambda p: multipletests(p, method=\"fdr_bh\")[1])\n    T7[\"Bonf all 40\"] = np.minimum(T7.p * len(T7), 1)\n    T7[\"Bonf per fold\"] = np.minimum(T7.p * 10, 1)\n    return T7\n\nfor reading in [\"squares\", \"dataset\"]:\n    T7 = fold_edge_tests(reading)\n    print(f\"--- baseline {reading}\")\n    print(T7[T7.fold.isin([\"P180\", \"S40\"])].round(4).to_string(index=False))\n    for col in [\"p\", \"BH all 40\", \"BH per fold\", \"Bonf all 40\", \"Bonf per fold\"]:\n        p180 = T7[(T7.fold == \"P180\") & (T7.rms == rms_levels[-1])].iloc[0]\n        s40 = T7[(T7.fold == \"S40\") & (T7.rms.isin(rms_levels[:2]))]\n        ok = (p180[col] < 0.05 and p180[\"fold - edge\"] < 0) and bool(((s40[col] < 0.05) & (s40[\"fold - edge\"] > 0)).all())\n        sig = T7[(T7.fold == \"S40\") & (T7[col] < 0.05) & (T7[\"fold - edge\"] > 0)].rms.tolist()\n        print(f\"{col}: claim holds {ok}; S40 significantly higher at RMS {sig}\")\n\"\"\", [\"claim:fig7c-fold-edge-significance\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** With the paper's squares, P180 is significantly lower than the Edge at\nRMS 0.943, but S40 is not significantly higher than the Edge at 0.610 and 0.647 under any of the\ncorrections, nor uncorrected (values above).\n\"\"\")\n\nmd(r\"\"\"\n## fig7d-nonlinear\n\n> The relationship between corner angle and V1 spike rate difference is parametric but\n> apparently not linear.\n\"\"\")\n\ncode(r\"\"\"\nfor reading in [\"squares\", \"dataset\"]:\n    m = mid_table(reading).loc[[\"S40\", \"S52\", \"S90\", \"P180\"]]\n    ang = np.array([40, 52, 90, 180], float)\n    slope, icpt = np.polyfit(ang, m[\"mean\"].values, 1)\n    resid = m[\"mean\"].values - (slope * ang + icpt)\n    off = np.abs(resid) > m[\"sem\"].values\n    print(f\"--- baseline {reading}: line {slope:.4f} * angle + {icpt:.2f}\")\n    print(pd.DataFrame({\"angle\": ang, \"mean\": m[\"mean\"].values, \"sem\": m[\"sem\"].values, \"residual\": resid, \"off by > SEM\": off}, index=m.index).round(3).to_string())\n    print(f\"monotonic: {m.attrs['ordered']}; non-linear by the rule (a point off the line by more than its SEM): {bool(off.any())}\")\n    seg = np.diff(m[\"mean\"].values) / np.diff(ang)\n    seg_se = np.sqrt(m[\"sem\"].values[1:] ** 2 + m[\"sem\"].values[:-1] ** 2) / np.diff(ang)\n    print(\"variant, slopes 40-52, 52-90, 90-180:\", np.round(seg, 4), \"SE:\", np.round(seg_se, 4))\n    for i in range(2):\n        diff = abs(seg[i] - seg[i + 1]); se = np.hypot(seg_se[i], seg_se[i + 1])\n        print(f\"  slope {i + 1} vs {i + 2}: difference {diff:.4f}, propagated SE {se:.4f}, differ by more: {diff > se}\")\n\"\"\", [\"claim:fig7d-nonlinear\"])\n\nmd(r\"\"\"\n**Result: reproduced.** The four means are monotonic in angle, and under the criterion's rule at\nleast one of them lies off the least-squares line by more than its SEM (residuals above), so the\nrelation is judged non-linear; the slope variant is shown above.\n\"\"\")\n\nmd(r\"\"\"\n## fig7d-dog-similar and s3-latency-peak (blocked)\n\nfig7d-dog-similar needs the output of the difference-of-Gaussians model of the paper's reference\n[3], which is not in the data set and is not published as data. s3-latency-peak needs maps made at\nlatencies other than 60 ms, which need spike times and eye positions; the data set holds only maps.\n\"\"\")\n\nmd(r\"\"\"\n## Summary\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"Total run time {time.time() - started:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\")\n\nmd(r\"\"\"\n| Claim | Outcome |\n|---|---|\n| neuron-counts | not reproduced |\n| spikes-per-condition | blocked (data missing) |\n| s4-baseline-no-difference | not reproduced (assumed Corners baseline placement) |\n| fig4a-above-baseline | reproduced |\n| fig4b-spike-rate-difference | partially reproduced |\n| fig4b-pairwise-significance | reproduced |\n| fig5-average-maps | reproduced |\n| table1-edge | partially reproduced |\n| table1-p180 | reproduced |\n| table1-s90 | partially reproduced |\n| table1-s52 | reproduced |\n| table1-s40 | reproduced |\n| fig6-midpoint-representative | reproduced |\n| fig7a-rms-contrast-fit | not reproduced |\n| fig7c-fold-edge-equivalence | not reproduced |\n| fig7c-fold-edge-significance | not reproduced |\n| fig7d-nonlinear | reproduced |\n| fig7d-dog-similar | blocked (data missing) |\n| s3-latency-peak | blocked (data missing) |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning\nand the differences from the paper's method.\n\nHow the analysis differs from the paper's: it uses the maps the files hold, registered by the\nauthors (`Standard`), and so only 60 of the 77 neuron and condition maps (Star 12 of 29); the\npaper used 83. The baseline squares follow the Methods for Square and Edge and Star; their place in\nCorners is an assumption. The Edge contrast levels use the paper's fitted parameters.\n\nWhat was found about the data set: the data set holds 53 cells and 77 maps, not the paper's 58\nneurons and 83 maps; 17 Star maps lack the registration to the stimulus, which the files do not\notherwise allow; the files hold undocumented fields (`Standard`, `BaseActivity`, `norm`,\n`eyetime`, `original_image`); `image` is a rate, not the count the descriptor names; the stored\nsmoothing differs from the described filter; the spike counts and eye times needed for the spike\ntotals are missing; two files have a baseline of exactly 0.\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"display_name\": \"Python 3\", \"language\": \"python\", \"name\": \"python3\"}\nnbf.write(nb, \"entries/martinez-conde-2019/reproduce_martinez_conde_2019.ipynb\")\nprint(\"written\", len(cells))\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && source scratch/bin/activate && python build_nb.py && cd entries/martinez-conde-2019 && time python - <<'EOF'
import nbformat
from nbclient import NotebookClient
nb=nbformat.read('reproduce_martinez_conde_2019.ipynb',as_version=4)
c=NotebookClient(nb,timeout=1800,kernel_name='python3',resources={'metadata':{'path':'.'}},allow_errors=True)
c.execute()
nbformat.write(nb,'/tmp/claude-1001/exec.ipynb')
for i,cell in enumerate(nb.cells):
    if cell.cell_type!='code': continue
    for o in cell.get('outputs',[]):
        if o.output_type=='error': print('ERROR cell',i,o.ename,o.evalue)
EOF
```

```
Sun Nov 15 09:47:10 UTC 2026
written 77
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.

real	0m39.848s
user	0m11.769s
sys	0m1.112s
```

**Agent calls Bash**

```bash
cd $TMPDIR && source scratch/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('/tmp/claude-1001/exec.ipynb',as_version=4)
for i,cell in enumerate(nb.cells):
    if cell.cell_type!='code': continue
    tags=cell.metadata.get('tags',[])
    print(f'===== cell {i} {tags}')
    for o in cell.get('outputs',[]):
        if o.output_type=='stream': print(o.text[:6000])
        elif o.output_type=='error': print('ERR',o.evalue)
EOF
```

```
<persisted-output>
Output too large (38.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/5dab85ce-1834-411c-91af-bfb914e14918/tool-results/bdpgg72fn.txt

Preview (first 2KB):
===== cell 1 []
checksums.md5 of the data set:

9ca5ae49dfc19e516b09c99e62eefc23  docs/crcns_pvc-12_data_description.docx
e67a2f96c6651ba3c9ac3a28297a00f4  docs/crcns_pvc-12_data_description.pdf
06c85736f287b47c60ab2da8539ff226  filelist.txt
e1301fe463e72332e2303b2053ee0559  V1_Vasarely_data.zip


data set pvc-12 (unversioned, doi:10.6080/K05D8Q1T); 77 spike rate map files loaded in 20 s; peak memory 0.37 GB

===== cell 3 ['sanity']
Spike rate map files by experiment, format, and whether they hold the registered map `Standard`:
registered           False  True  All
condition    format                  
Corners      v5          0    26   26
[... 36 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/5dab85ce-1834-411c-91af-bfb914e14918/tool-results/bdpgg72fn.txt"
}
```

```
1	===== cell 1 []
2	checksums.md5 of the data set:
3	
4	9ca5ae49dfc19e516b09c99e62eefc23  docs/crcns_pvc-12_data_description.docx
5	e67a2f96c6651ba3c9ac3a28297a00f4  docs/crcns_pvc-12_data_description.pdf
6	06c85736f287b47c60ab2da8539ff226  filelist.txt
7	e1301fe463e72332e2303b2053ee0559  V1_Vasarely_data.zip
8	
9	
10	data set pvc-12 (unversioned, doi:10.6080/K05D8Q1T); 77 spike rate map files loaded in 20 s; peak memory 0.37 GB
11	
12	===== cell 3 ['sanity']
13	Spike rate map files by experiment, format, and whether they hold the registered map `Standard`:
14	registered           False  True  All
15	condition    format                  
16	Corners      v5          0    26   26
17	Edge-compare v5          0    22   22
18	Star         v5         16    12   28
19	             v7.3        1     0    1
20	All                     17    60   77
[... 637 more lines not kept]
```

**Agent**

Notebook runs in 35 s, 0.44 GB. Now correcting the conclusion texts to match the printed numbers.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a[:60]
    s=s.replace(a,b)
rep("""The descriptor names three fields (image, smoothed_image, smoothed_image_norm); every file has
the first two, 37 of 77 have""","""The descriptor names three fields (image, smoothed_image, smoothed_image_norm); every file has
the first two, 38 of 77 have""")
rep("""**Result: not reproduced.** The files hold 53 cells (A 6, J 47 by the cell code), with 22 Square
and Edge, 29 Star and 26 Corners files, and 6 cells in all three experiments, 12 in two and 35 in
one; none of the paper's counts match. The spreadsheet lists 58 cells, the paper's number, but
five have no experiment and no files. Of these, 60 files can be placed on the stimulus (22, 12 and
26).""","""**Result: not reproduced.** The files hold 53 cells (49 from monkey J and 4 from monkey A by the
cell code), with 22 Square and Edge, 29 Star and 26 Corners files (paper 25, 30 and 28); 7 cells
are in all three experiments, as in the paper, but 10 are in two and 36 in one (paper 11 and 40).
The spreadsheet lists 58 cells, the paper's number, but five have no experiment marked and no
files. Of the 77 files, 60 can be placed on the stimulus (22, 12 and 26).""")
rep("""**Result: not reproduced.** With the paper's squares, the baselines differ across the stimuli
(Square and Edge median 7.68, Star 1.84, Corners 2.45 spikes/s): Square and Edge against Corners
is significant after BH correction, and the Kruskal-Wallis test is significant (p < 0.05), though
the ANOVA is not. With the files' own `BaseActivity` (fewer neurons) none of the three readings is
significant. The outcome rests on the placement of the baseline squares, which for Corners is an
assumption, and on 12 of the paper's 30 Star neurons.""","""**Result: not reproduced.** With the paper's squares, the baselines differ across the stimuli
(medians: Square and Edge 7.68, Star 1.84, Corners 2.45 spikes/s), and all three readings find
it: rank sum with BH, Square and Edge against Star 0.0128 and against Corners 0.0076; Kruskal-Wallis
p = 0.0035; ANOVA p = 0.0010. With the files' own `BaseActivity` (9, 10 and 19 neurons) none of
the three readings is significant (smallest BH 0.109, Kruskal-Wallis p = 0.114, ANOVA p = 0.166).
The outcome rests on the placement of the baseline squares (an assumption for Corners), and on
12 of the paper's 30 Star neurons.""")
rep("""**Result: reproduced.** With the paper's squares, more than half of the neurons lie above their
baseline for every fold, every mass centre lies above the unit line, and its distance increases
from P180 to S40 under both readings of the mass centre (raw means and log means). The order and
the majority also hold with the files' `BaseActivity`, though there under the log reading S52 is
not below S40 is shown above. The result rests on 12 Star neurons.""","""**Result: reproduced.** With the paper's squares, 20 of 22 (P180), 20 of 22 (S90), 12 of 12
(S52) and 26 of 26 (S40) neurons lie above their baseline, every mass centre lies above the unit
line, and its distance increases from P180 to S40 under both readings of the mass centre (raw
means 3.88, 8.21, 19.10, 26.41 spikes/s; log means 0.179, 0.299, 0.926, 1.036 log10 units). The
same holds with the files' `BaseActivity`. The Star result rests on 12 neurons.""")
rep("""**Result: partially reproduced.** With the paper's squares and the smoothed map, the means are
ordered S40 > S52 > S90 > P180 (26.41, 19.10, 8.21 and 3.88 spikes/s), and S40, S52 and P180 are
within the paper's SEM, while S90 is 0.54 spikes/s below its range. With the files'
`BaseActivity` the order holds and only S90 is within tolerance; with the unsmoothed map the order
also holds (values above). The S40 value rests on the assumed placement of the Corners baseline
squares; the Star value on 12 of 30 neurons.""","""**Result: partially reproduced.** With the paper's squares and the smoothed map, the means are
ordered S40 > S52 > S90 > P180 (26.41, 19.10, 8.21 and 3.88 spikes/s), and S40, S52 and P180 are
within the paper's SEM, while S90 is 0.54 spikes/s below its range (8.75 to 12.63). With the files'
`BaseActivity` the order holds, and S40 and S90 are within tolerance while S52 (20.57) and P180
(3.58) are not; with the unsmoothed map the order holds and P180 (3.25) is the one outside. The S40
value rests on the assumed placement of the Corners baseline squares; the Star value on 12 of 30
neurons.""")
rep("""**Result: reproduced.** With the paper's squares, S40 > S90, S40 > P180 and S52 > P180 are
significant by rank sum tests with BH correction under both families (all six pairs, or the three
named), with the p-values shown above. With the files' `BaseActivity`, the same three pairs are
significant under both families as well.""","""**Result: reproduced.** With the paper's squares, S40 > S90 (BH p = 0.00012 over six pairs),
S40 > P180 (p < 0.00001) and S52 > P180 (p = 0.00005) are significant by rank sum tests with BH
correction under both families (all six pairs, or the three named). Of the pairs the text does not
claim, S52 > S90 is also significant (0.0053) and S40 > S52 and S90 > P180 are not. With the files'
`BaseActivity`, the three named pairs are significant under both families as well.""")
rep("""**Result: reproduced.** The average maps, read at the midpoint squares, are ordered S40 > S52 >
S90 > P180, as the criterion requires; as the claims file notes, this repeats the means of
fig4b-spike-rate-difference. The variant, the mean over the ten fold blocks of the average map, is
ordered the same way.""","""**Result: reproduced.** The average maps, read at the midpoint squares, are ordered S40 (26.41) >
S52 (19.07) > S90 (8.15) > P180 (3.79 spikes/s), as the criterion requires; as the claims file
notes, this repeats the means of fig4b-spike-rate-difference. The variant, the mean over the ten
fold blocks of the average map, is ordered the same way (23.14, 17.20, 7.43, 3.47).""")
rep('''        "Edge": "**Result: partially reproduced.** With the paper's squares, reading (a) puts four of the five values within tolerance (the maximum is above its range), and reading (b) two of five; with the files' `BaseActivity` (9 neurons) reading (a) gives four of five as well (above).",
        "P180": "**Result: reproduced.** With the paper's squares, reading (a) puts all five values within the paper's SEM (above); the dataset baseline gives four of five under (a).",
        "S90": "**Result: partially reproduced.** With the paper's squares, the best reading puts three of the five values within tolerance (above): the minimum, maximum and median under halves (ii) and reading (a), while the mean and the midpoint are below. With the files' `BaseActivity`, more values are within tolerance (above).",
        "S52": "**Result: reproduced.** With the paper's squares, reading (a) puts all five values within tolerance under both half readings (above). The values rest on 12 of the paper's 30 Star neurons.",
        "S40": "**Result: reproduced.** With the paper's squares and the bright S40 fold, reading (a) puts all five values within tolerance (above). The values rest on the assumed placement of the two Corners baseline squares.",''','''        "Edge": "**Result: not reproduced.** No reading puts three of the five values within tolerance: with the paper's squares, reading (a) gives two (maximum 29.86 and midpoint 18.72) and reading (b) two (median and midpoint); the minimum (5.50), mean (16.92) and median (16.78) of reading (a) are below the paper's ranges. With the files' `BaseActivity` (9 neurons) no value is within tolerance.",
        "P180": "**Result: partially reproduced.** With the paper's squares, reading (a) puts three of the five values within tolerance (maximum 10.28, mean 3.47, midpoint 3.88) and reading (b) three (mean, median, midpoint); the minimum of reading (a) is -1.71 against 0.18 ± 1.01. The files' `BaseActivity` also gives three of five under (a).",
        "S90": "**Result: not reproduced.** No reading puts three of the five values within tolerance: with the paper's squares, reading (a) gives one (the maximum) under either half reading, and reading (b) none; the mean of the blocks is 7.46 against 9.22 ± 1.61. With the files' `BaseActivity` (9 neurons) the best reading gives two.",
        "S52": "**Result: partially reproduced.** With the paper's squares, reading (a) puts four of the five values within tolerance under both half readings; the minimum (9.19 under halves (i), 7.61 under (ii)) is above 6.26 ± 1.33. The values rest on 12 of the paper's 30 Star neurons.",
        "S40": "**Result: reproduced.** With the paper's squares and the bright S40 fold, reading (a) puts all five values within tolerance (10.65, 34.40, 23.14, 23.15 and 26.41 spikes/s); so does the files' `BaseActivity` (19 neurons). The values rest on the assumed placement of the two Corners baseline squares.",''')
rep("""**Result: reproduced.** By the paper's test (rank sum, alpha 0.05, no correction), none of the ten
comparisons of midpoint against the mean or median along the fold is significant under either
baseline or half reading. The paired signed rank test, shown as a variant, does find the midpoint
higher than the mean along several folds (above), so the absence rests on the unpaired test the
paper names.""","""**Result: reproduced.** By the paper's test (rank sum, alpha 0.05, no correction), none of the ten
comparisons of midpoint against the mean or median along the fold is significant under either
baseline or half reading (smallest p 0.36). The paired signed rank test, shown as a variant, finds
the midpoint higher than the mean and the median along S40 (p = 0.015 and 0.009) and than the
median along S90 (p = 0.025), so the absence rests on the unpaired test the paper names; the
median differences are 2.39 and 1.36 spikes/s for S40.""")
rep("""**Result: not reproduced.** Neither reading of RMS contrast computed on the 22 Edge stimulus images
gives the paper's curve: the SD over the mean is about 0.94 over most of the Edge but rises above
1 near 0% (so its range is not 0.61 to 0.943), and the SD of the 0-1 luminance rises from 0.01 to
0.45. Neither fit gives the paper's parameters (values above). The definition of RMS contrast the
paper used (its reference [21]) is not in the text read.""","""**Result: not reproduced.** Neither reading of RMS contrast computed on the 22 Edge stimulus images
gives the paper's curve: the SD over the mean (a) is about 0.95 from 18% to 90% luminance but
rises to 2.09 at 0% and 1.40 at 99%, so its range is 0.94 to 2.09, not 0.61 to 0.943; the SD of
the 0-1 luminance (b) rises from 0.014 to 0.475. Neither fit gives the paper's parameters (a:
a = 1.16, b = 0.25, R2 = 0.89; b: a = -52.2, b = 0.0001). The definition of RMS contrast the
paper used (its reference [21]) is not in the text read.""")
rep("""**Result: not reproduced.** With the paper's squares, under reading (a) the Edge level nearest the
P180 mean and the one nearest the S40 mean are printed above, and they are not within one 10% step
of 50% and 90% together; under reading (b) the S40 mean is not matched within one step of 0.90. The
Edge responses here are lower than the paper's near the bright end (the Edge maximum block is above
the paper's range, but the 16 x 16 DU squares straddle the Edge).""","""**Result: not reproduced.** With the paper's squares, the P180 mean (3.88 spikes/s) is below the
Edge response at every level (8.61 at 0% luminance and 17.19 at 50%), so under reading (a) it is
nearest the 0% level, not 50%, while S40 (26.41) is nearest 90%, as the paper says. Under reading
(b), P180 is at the lowest level, as the rule allows, but S40 is nearest 0.943, 0.043 from 0.90,
more than one step (0.037). With the files' `BaseActivity`, P180 is nearest 0% and S40 nearest 80%
under (a).""")
rep("""**Result: not reproduced.** With the paper's squares, P180 is significantly lower than the Edge at
RMS 0.943, but S40 is not significantly higher than the Edge at 0.610 and 0.647 under any of the
corrections, nor uncorrected (values above).""","""**Result: reproduced.** With the paper's squares, P180 is significantly lower than the Edge at
RMS 0.943 (p = 0.0005) and S40 significantly higher than the Edge at 0.610 and 0.647 (p = 0.0007
and 0.0009), under every correction and family. With Bonferroni over the 40 tests, S40 is
significant at 0.610 and 0.647 only, the levels below 0.68; with BH over 40 it is significant up to
0.795. With the files' `BaseActivity`, the claim holds uncorrected and with BH, not with
Bonferroni.""")
rep("""**Result: reproduced.** The four means are monotonic in angle, and under the criterion's rule at
least one of them lies off the least-squares line by more than its SEM (residuals above), so the
relation is judged non-linear; the slope variant is shown above.""","""**Result: reproduced.** The four means are monotonic in angle, and S40, S90 and P180 lie off the
least-squares line by more than their SEM (residuals 4.77, -6.26 and 2.31 spikes/s), so the relation
is judged non-linear under the criterion's rule. In the variant, the slope from 52 to 90 degrees
(-0.287) differs from the slope from 90 to 180 (-0.048) by more than their propagated SE (0.098);
the first two slopes do not differ by more than theirs.""")
rep("""Smoothing `image` with the Gaussian of the Fig 3B legend (16 DU, SD 7 DU) does not give
`smoothed_image` exactly: the two correlate closely but differ by up to about a third of the peak.
The smoothing the files used is therefore not the one described, or not applied to `image` alone;
the analysis uses the files' own smoothed maps.""","""Smoothing `image` with the Gaussian of the Fig 3B legend (16 DU, SD 7 DU) does not give
`smoothed_image`: the two differ by 19% to 27% of the peak. A 16 DU Gaussian with SD 5 DU comes
much closer (r = 0.999, 5% to 7% of the peak) but is not exact either. The analysis uses the
files' own smoothed maps.""")
rep("""| s4-baseline-no-difference | not reproduced (assumed Corners baseline placement) |
| fig4a-above-baseline | reproduced |
| fig4b-spike-rate-difference | partially reproduced |
| fig4b-pairwise-significance | reproduced |
| fig5-average-maps | reproduced |
| table1-edge | partially reproduced |
| table1-p180 | reproduced |
| table1-s90 | partially reproduced |
| table1-s52 | reproduced |
| table1-s40 | reproduced |
| fig6-midpoint-representative | reproduced |
| fig7a-rms-contrast-fit | not reproduced |
| fig7c-fold-edge-equivalence | not reproduced |
| fig7c-fold-edge-significance | not reproduced |""","""| s4-baseline-no-difference | not reproduced (assumption: baseline placement) |
| fig4a-above-baseline | reproduced |
| fig4b-spike-rate-difference | partially reproduced (assumption: Corners baseline placement) |
| fig4b-pairwise-significance | reproduced |
| fig5-average-maps | reproduced |
| table1-edge | not reproduced |
| table1-p180 | partially reproduced |
| table1-s90 | not reproduced |
| table1-s52 | partially reproduced |
| table1-s40 | reproduced (assumption: Corners baseline placement) |
| fig6-midpoint-representative | reproduced |
| fig7a-rms-contrast-fit | not reproduced |
| fig7c-fold-edge-equivalence | not reproduced |
| fig7c-fold-edge-significance | reproduced |""")
rep("""otherwise allow; the files hold undocumented fields (`Standard`, `BaseActivity`, `norm`,
`eyetime`, `original_image`); `image` is a rate, not the count the descriptor names; the stored
smoothing differs from the described filter; the spike counts and eye times needed for the spike
totals are missing; two files have a baseline of exactly 0.""","""otherwise allow; the files hold undocumented fields (`Standard`, `BaseActivity`, `norm`,
`eyetime`, `original_image`); `image` is a rate, not the count the descriptor names; the stored
smoothing differs from the filter the paper describes (SD 7 DU); the spike counts and eye times
needed for the spike totals are missing; two files have a `BaseActivity` of exactly 0; the
spreadsheet lists 58 cells, five of them with no data.""")
open(p,'w').write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='build_nb.py'; s=open(p).read()
a='''md(r"""
### Baseline
'''
assert s.count(a)==1
s=s.replace(a,'''md(r"""
The band along the Edge is above every sideways shift in 16 of 22 neurons (median 21.7 against
17.2 spikes/s). This is consistent with the registered maps lying on the stimulus as the polygons
say; it does not prove the registration of each neuron, which rests on the authors' `Standard`.
""")

'''+a)
open(p,'w').write(s)
EOF
cd entries/martinez-conde-2019
cat > requirements.in <<'EOF'
fsspec
aiohttp
requests
h5py
matplotlib
numpy
openpyxl
pandas
scipy
statsmodels
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: martinez-conde-2019
type: reproduction
title: V1 responses to illusory corner-folds (Martinez-Conde et al. 2019)
description: Tests the findings of Martinez-Conde, McCamy, Troncoso, Otero-Millan and Macknik (2019) on
  CRCNS pvc-12, which holds per neuron the spike rate maps of V1 neurons of two monkeys viewing the
  Square and Edge, Star and Corners stimuli, and the stimulus images. It compares midpoint and
  along-fold responses across fold angles, the baselines, and the responses to folds against those
  to the Edge. The spike times and eye positions behind the maps are not in the data set.
license: Apache-2.0
notebooks:
- path: reproduce_martinez_conde_2019.ipynb
  title: Reproducing Martinez-Conde et al. (2019) from CRCNS pvc-12
  runtime_minutes: 1
helpers:
- vasarely.py
related:
- id: crcns:pvc-12/unversioned
  relation: uses_data
- id: doi:10.1371/journal.pone.0210941
  relation: reproduces
EOF
python $TMPDIR/build_nb.py 2>/dev/null || (source $TMPDIR/scratch/bin/activate && python $TMPDIR/build_nb.py); ls
```

```
written 78
__pycache__
entry.yaml
reproduce_martinez_conde_2019.ipynb
requirements.in
vasarely.py
```

**Agent calls Bash**

```bash
cd  && rm -rf entries/martinez-conde-2019/__pycache__ && date -u && python tools/entry.py lock entries/martinez-conde-2019 2>&1 | tail -5 && cat entries/martinez-conde-2019/entry.yaml | tail -5
```

```
Sun Nov 15 09:49:32 UTC 2026
wrote martinez-conde-2019/requirements.lock.txt (Python 3.13, with hashes)
related:
- id: crcns:pvc-12/unversioned
  relation: uses_data
- id: doi:10.1371/journal.pone.0210941
  relation: reproduces
```

**Agent calls Bash**

```bash
head -3 entries/martinez-conde-2019/entry.yaml; grep python entries/martinez-conde-2019/entry.yaml; python tools/entry.py check entries/martinez-conde-2019 2>&1 | tail -20
```

```
schema_version: 1
name: martinez-conde-2019
type: reproduction
python: "3.13"
0 error(s)
```

**Agent calls Bash**

```bash
cd  sed -n 150,400p attempts/fouke-2025-01.yaml | grep -v "^    " | head -80; ls schemas; python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json')) if __import__('os').path.exists('schemas/attempt.schema.json') else None
print(json.dumps(s,indent=0)[:6000] if s else 'none')
EOF
```

```
outcome: not_reproduced
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
[... 355 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']['properties']
for k in o: 
    if k not in ('claim','outcome','blocked_by','notes','notebook','output','measured'): print(k, json.dumps(o[k])[:400])
for k in ['inputs','findings','verifications']:
    print(k, json.dumps(s['properties'].get(k))[:1500])
print([k for k in s['properties']])
EOF
```

```
deviations {"description": "How the test differed from the paper's method or data, e.g. one session of four, or a substituted model.", "type": "array", "items": {"type": "string", "minLength": 1}}
assumed {"description": "True when the outcome rests on an assumption about a method the paper leaves open: a choice the paper best supports, stated in a deviation that says what was assumed and why (docs/protocol.md, Author, step 1.6).", "type": "boolean"}
proposed {"description": "A change of outcome found after the last verification round, held until a further round agrees with it.", "type": "object", "additionalProperties": false, "required": ["outcome", "reason"], "properties": {"outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}, "blocked_by": {"description": "Required when outcome is blocked.", "enum": ["data_missin
inputs {"description": "Everything the attempt used that is not in the dataset.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["what", "source"], "properties": {"what": {"type": "string", "minLength": 1}, "source": {"description": "A DOI, or a repository URL with the commit read.", "type": "string", "minLength": 1}}}}
findings {"description": "What the attempt found, whatever the outcomes: about the dataset itself (`about: data`, for its owner and the archive, shown on the dataset's page) or about the paper (`about: paper`, shown on the paper's page).", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["kind", "statement"], "properties": {"kind": {"enum": ["metadata_error", "data_missing", "identifier_missing", "metadata_insufficient", "selection_undocumented", "methods_unavailable", "format_error", "code_mismatch", "paper_inconsistency", "other"]}, "statement": {"type": "string", "minLength": 1}, "found": {"description": "How the finding was found. Unset: by the attempt itself. `on_prompt`: by the reconcile step of a repeat attempt, wh
[... 2 more lines not kept]
```

**Agent**

Entry checks pass. Running the entry from a clean environment now.

**Agent calls Bash**

```bash
cd  date -u; time python tools/entry.py all entries/martinez-conde-2019 2>&1 | tail -15
```

```
Sun Nov 15 09:49:49 UTC 2026
Installed kernelspec registry-martinez-conde-2019 in executed/martinez-conde-2019/.venv/share/jupyter/kernels/registry-martinez-conde-2019
0 error(s)
pass  reproduce_martinez_conde_2019.ipynb  (45 s)

real	0m57.256s
user	0m19.921s
sys	0m3.553s
```

**Agent calls Bash**

```bash
cd  source $TMPDIR/scratch/bin/activate; python - <<'EOF'
import nbformat
def outs(p):
    nb=nbformat.read(p,as_version=4); r=[]
    for c in nb.cells:
        if c.cell_type=='code':
            r.append(''.join(o.get('text','') for o in c.get('outputs',[]) if o.output_type=='stream'))
    return r
a=outs('/tmp/claude-1001/exec.ipynb'); b=outs('executed/martinez-conde-2019/reproduce_martinez_conde_2019.ipynb')
print(len(a),len(b))
import difflib
for i,(x,y) in enumerate(zip(a,b)):
    if x!=y:
        d=[l for l in difflib.unified_diff(x.splitlines(),y.splitlines(),lineterm='',n=0) if not l.startswith(('---','+++','@@'))]
        print('cell',i,d[:8])
nb=nbformat.read('executed/martinez-conde-2019/reproduce_martinez_conde_2019.ipynb',as_version=4)
print([o.get('ename') for c in nb.cells if c.cell_type=='code' for o in c.outputs if o.output_type=='error'])
EOF
```

```
28 28
cell 0 ['-data set pvc-12 (unversioned, doi:10.6080/K05D8Q1T); 77 spike rate map files loaded in 20 s; peak memory 0.37 GB', '+data set pvc-12 (unversioned, doi:10.6080/K05D8Q1T); 77 spike rate map files loaded in 21 s; peak memory 0.38 GB']
cell 27 ['-Total run time 35 s; peak memory 0.44 GB', '+Total run time 38 s; peak memory 0.45 GB']
[]
```

**Agent**

Clean run matches (45 s). Writing the README and the attempt record.

**Agent calls Write**

```json
{
 "file_path": "entries/martinez-conde-2019/README.md",
 "content": "# Martinez-Conde, McCamy, Troncoso, Otero-Millan & Macknik (2019) from CRCNS pvc-12\n\nTests the findings of [Martinez-Conde et al. (2019)](https://doi.org/10.1371/journal.pone.0210941)\non [CRCNS pvc-12](https://doi.org/10.6080/K05D8Q1T), which holds per neuron and stimulus the spike\nrate maps of V1 neurons of two monkeys viewing the Square and Edge, Star and Corners stimuli, and\nthe stimulus images. The spike times and eye positions behind the maps are not in it.\n\n| Claim | Outcome |\n|---|---|\n| Neuron counts (58 neurons; 25, 30 and 28 per stimulus) | Not reproduced |\n| Spikes per condition (mean 35,998) | Blocked: data missing |\n| No difference in baseline across stimuli | Not reproduced |\n| Midpoint responses above baseline, more so for sharper folds | Reproduced |\n| Midpoint spike rate difference per fold (Table 1) | Partially reproduced |\n| S40 > S90, S40 > P180, S52 > P180 | Reproduced |\n| Average maps increase with sharper corners | Reproduced |\n| Table 1, Edge, P180, S90, S52, S40 | Not, partially, not, partially, reproduced |\n| Midpoint represents the whole fold | Reproduced |\n| RMS contrast along the Edge and its exponential fit | Not reproduced |\n| P180 like a 50% and S40 like a 90% contrast Edge | Not reproduced |\n| P180 below the 94% Edge, S40 above the Edge below 68% | Reproduced |\n| Non-linear relation of response to angle | Reproduced |\n| Similar to the DOG model of reference [3] | Blocked: data missing |\n| Responses peak near 60 ms latency | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe data set holds 53 cells and 77 maps, where the paper analysed 58 neurons and 83 maps, and only\n60 of the maps carry the authors' registration to the stimulus; the Star results rest on 12 of the\npaper's 30 neurons. The attempt record, with the reasons and the differences from the paper's\nmethod, is [`attempts/martinez-conde-2019-02.yaml`](../../attempts/martinez-conde-2019-02.yaml).\n\n- `reproduce_martinez_conde_2019.ipynb`: the analysis. It takes about a minute, most of it\n  streaming the zip.\n- `vasarely.py`: loading the zip in place, the fold geometry read from each file's own polygons,\n  the midpoint, block, baseline and Edge measures. Other notebooks on this data set can import it.\n"
}
```

```
File created successfully at: entries/martinez-conde-2019/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  ls questions | grep -i mart; grep -n "author-again\|reconcil" docs/agents/*.md 2>/dev/null | head -5; ls docs/agents/
```

```
martel-2025.yaml
docs/agents/reconcile.md:1:You reconcile a repeat attempt in the reproduction registry, checked out in the current directory. Read docs/protocol.md, "Repeat attempts", first. Attempt `{attempt}` on paper `{key}` (data: {dataset}; entry `entries/{entry}`, dataset version {version}) was made blind: its author did not see `{earlier}` (made on version {earlier_version}). Its record is `attempts/{earlier}.yaml`. Its entry is `entries/{earlier_entry}` as it was when that record was last changed: `c=$(git log -1 --format=%H -- attempts/{earlier}.yaml)`, then `git show $c:entries/{earlier_entry}/<file>`. Both have been through their verification rounds. Your job is to say how the two compare, in a `reconciliation` block of `attempts/{attempt}.yaml` (its schema is in `schemas/attempt.schema.json`). Do not change the outcomes, statements or notes that the blind attempt recorded, its claims file or its notebooks.
answer.md
author-again.md
author-answers.md
author-revise-3.md
author-revise.md
author.md
claims-check.md
claims.md
paper-match.md
reconcile.md
recorder.md
verifier-1.md
verifier-2.md
verifier-3.md
```

**Agent calls Write**

```json
{
 "file_path": "attempts/martinez-conde-2019-02.yaml",
 "content": "schema_version: 3\nid: martinez-conde-2019-02\ndatasets:\n- archive: crcns\n  id: pvc-12\n  version: unversioned\n  doi: 10.6080/K05D8Q1T\n  relation: primary\npaper: doi:10.1371/journal.pone.0210941\ndate: 2026-11-15\nentry: martinez-conde-2019\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-15\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/43699045378\noutcomes:\n- claim: neuron-counts\n  outcome: not_reproduced\n  notebook: reproduce_martinez_conde_2019.ipynb\n  output: claim:neuron-counts\n  measured:\n  - 53\n  - 22\n  - 29\n  - 26\n  - 7\n  - 10\n  - 36\n  notes: Cells are identified by the code in the file names (the experiment prefix and a trailing\n    letter removed), which matches the spreadsheet V1_Vasarely_data_SMC.xlsx cell by cell. The\n    files hold 53 cells (49 from monkey J, 4 from monkey A) and 77 maps, 22 Square and Edge, 29\n    Star and 26 Corners (paper 25, 30, 28); 7 cells are in all three experiments, as in the paper,\n    10 in two and 36 in one (paper 11 and 40). The spreadsheet lists 58 cells, the paper's number,\n    but marks no experiment for 5 of them, and the zip has no files for those 5. The 118 recorded\n    and the 102 and 16 per monkey cannot be checked; the data set holds only analysed cells. Only\n    60 maps (22, 12, 26) can be placed on the stimulus (see the findings).\n- claim: spikes-per-condition\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The number of spikes per neuron and condition needs the spike count map or the eye time\n    map, under either reading of the criterion. The files hold rate maps (`image` is the count\n    divided by eye time in 1 ms samples). One file of 77, ABC050900J1A, also stores `eyetime`; its\n    count is 15,644 spikes, above the 10,000 minimum. Spike times are not in the data set either.\n- claim: s4-baseline-no-difference\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_martinez_conde_2019.ipynb\n  output: claim:s4-baseline-no-difference\n  notes: With the 16 x 16 DU squares of the Methods, median baselines are 7.68 (Square and Edge,\n    22 neurons), 1.84 (Star, 12) and 2.45 spikes/s (Corners, 26). All three readings find a\n    difference; (a) rank sum with BH, Square and Edge against Star p = 0.0128 and against Corners\n    p = 0.0076, Star against Corners p = 0.73; (b) Kruskal-Wallis H = 11.31, p = 0.0035; (c) ANOVA\n    F = 7.81, p = 0.0010. With the files' own undocumented BaseActivity (9, 10 and 19 neurons;\n    medians 5.64, 2.68, 1.32) no reading is significant (smallest BH p = 0.109, Kruskal-Wallis\n    p = 0.114, ANOVA p = 0.166). The outcome rests on the squares as placed here (see deviations),\n    and the Star group has 12 of the paper's 30 neurons.\n  deviations:\n  - Absolute baseline from squares placed as the Methods describe for Square and Edge (inside the\n    corners of the 138 x 138 DU square around the Square; centred on the corners they leave the\n    ROI) and Star (inside the corners of the 300 x 300 DU square around the 0% star's\n    circumscribed circle). For Corners the paper gives no positions in the text (\"two 1 x 1 DVA\n    square regions in 0% luminance areas within the ROI\", Methods, Corners; shown only in Fig 2C);\n    the two bottom corners of the ROI, the only 0% band inside it, are assumed. The files'\n    BaseActivity is shown as a variant.\n  - Star has 12 neurons, Square and Edge 22 and Corners 26 (paper 30, 25 and 28).\n- claim: fig4a-above-baseline\n  outcome: reproduced\n  notebook: reproduce_martinez_conde_2019.ipynb\n  output: claim:fig4a-above-baseline\n  notes: Above baseline, 20 of 22 neurons for P180, 20 of 22 for S90, 12 of 12 for S52 and 26 of\n    26 for S40. Mass centres lie above the unit line for every fold, and their vertical distance is\n    ordered P180 < S90 < S52 < S40 under reading (a), raw means (3.88, 8.21, 19.10, 26.41 spikes/s),\n    and (b), log means (0.179, 0.299, 0.926, 1.036 log10 units; 2 S40 neurons with a zero baseline\n    left out of the log). The same holds with the files' BaseActivity.\n  deviations:\n  - Baselines as in s4-baseline-no-difference; the outcome is the same under both baselines.\n  - Star has 12 neurons (paper 30).\n- claim: fig4b-spike-rate-difference\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_martinez_conde_2019.ipynb\n  output: claim:fig4b-spike-rate-difference\n  measured:\n  - 26.41\n  - 19.1\n  - 8.21\n  - 3.88\n  notes: Means ± SEM, S40 26.41 ± 4.29 (26 neurons), S52 19.10 ± 3.01 (12), S90 8.21 ± 1.98 (22),\n    P180 3.88 ± 0.91 (22). Ordered S40 > S52 > S90 > P180; S40, S52 and P180 within tolerance, S90\n    0.54 spikes/s below 10.69 ± 1.94. With the files' BaseActivity, 29.10, 20.57, 9.08, 3.58, ordered,\n    with S40 and S90 within tolerance; with the unsmoothed map, 27.75, 20.35, 9.35, 3.25, ordered,\n    with P180 outside. The dark S40 fold of Corners, not used, gives 12.03.\n  deviations:\n  - Baselines as in s4-baseline-no-difference; which values fall within tolerance depends on the\n    baseline, so the outcome rests on the placement of the squares.\n  - The spike rate map is the files' own registered, smoothed map (Standard.smoothed_image), whose\n    smoothing is close to a Gaussian of SD 5 DU, not the 7 DU of the Fig 3B legend.\n  - The bright S40 fold of Corners is identified from the stimulus image as the one on which\n    luminance peaks (Methods, Corners, paragraph 2, \"We did not analyze dark corner-folds\"); it is\n    the same fold in all 26 files.\n  - Star has 12 neurons, Square and Edge 22, Corners 26 (paper 30, 25, 28).\n- claim: fig4b-pairwise-significance\n  outcome: reproduced\n  notebook: reproduce_martinez_conde_2019.ipynb\n  output: claim:fig4b-pairwise-significance\n  notes: Rank sum tests with BH over all six pairs; S40 > S90 p = 0.00012, S40 > P180 p < 0.00001,\n    S52 > P180 p = 0.00005; also significant over the three named pairs. Of the other pairs, S52 >\n    S90 is significant (p = 0.0053), S40 > S52 (p = 0.35) and S90 > P180 (p = 0.072) are not. With\n    the files' BaseActivity the three named pairs are significant as well.\n  deviations:\n  - Baselines and neuron numbers as in fig4b-spike-rate-difference.\n- claim: fig5-average-maps\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_martinez_conde_2019.ipynb\n  output: claim:fig5-average-maps\n  notes: Average spike rate difference maps per stimulus (22, 12 and 26 neurons) read at the\n    midpoint squares give S40 26.41 > S52 19.07 > S90 8.15 > P180 3.79 spikes/s; the variant, mean\n    over the ten fold blocks, 23.14 > 17.20 > 7.43 > 3.47. As the criterion says, the midpoint\n    reading repeats the means of fig4b-spike-rate-difference.\n  deviations:\n  - The measure of the maps is the assumption the criterion names. The Corners maps of the\n    smaller size (257 x 193) are padded by 8 DU to the larger frame before averaging.\n- claim: table1-edge\n  outcome: not_reproduced\n  notebook: reproduce_martinez_conde_2019.ipynb\n  output: claim:table1-edge\n  measured:\n  - 5.5\n  - 29.86\n  - 16.92\n  - 16.78\n  - 18.72\n  notes: Reading (a), per neuron then mean over 22 neurons, min 5.50, max 29.86, mean 16.92, median\n    16.78, midpoint 18.72 spikes/s; two of five within tolerance (max, midpoint). Reading (b),\n    population profile, 9.96, 21.01, 16.92, 17.63, 18.72; two of five (median, midpoint). With the\n    files' BaseActivity (9 neurons) none of five under either reading.\n  deviations:\n  - Blocks and midpoint are centred on the Edge line, so half of each block lies outside the\n    rectangle; the paper does not say otherwise.\n  - Baselines as in s4-baseline-no-difference; 22 neurons (paper 25).\n- claim: table1-p180\n  outcome: partially_reproduced\n  notebook: reproduce_martinez_conde_2019.ipynb\n  output: claim:table1-p180\n  measured:\n  - -1.71\n  - 10.28\n  - 3.47\n  - 2.84\n  - 3.88\n  notes: Reading (a), min -1.71, max 10.28, mean 3.47, median 2.84, midpoint 3.88; three of five\n    within tolerance (max, mean, midpoint). Reading (b), 1.59, 4.93, 3.47, 3.58, 3.88; three of\n    five (mean, median, midpoint). With the files' BaseActivity, three of five under (a).\n  deviations:\n  - P180 is the line 48 DU from the Edge inside the rectangle, parallel to it (Methods, Square and\n    edge).\n  - Baselines as in s4-baseline-no-difference; 22 neurons (paper 25).\n- claim: table1-s90\n  outcome: not_reproduced\n  notebook: reproduce_martinez_conde_2019.ipynb\n  output: claim:table1-s90\n  measured:\n  - 2.27\n  - 13.42\n  - 7.46\n  - 7.52\n  - 8.21\n  notes: Reading (a) with halves (i), min 2.27, max 13.42, mean 7.46, median 7.52, midpoint 8.21;\n    one of five within tolerance (max). Halves (ii) under (a) also one; reading (b) none under\n    either half reading. With the files' BaseActivity (9 neurons) the best reading gives two of\n    five. Measured values are reading (a) with halves (i).\n  deviations:\n  - Baselines as in s4-baseline-no-difference; 22 neurons (paper 25).\n- claim: table1-s52\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_martinez_conde_2019.ipynb\n  output: claim:table1-s52\n  measured:\n  - 9.19\n  - 25.22\n  - 17.2\n  - 16.97\n  - 19.1\n  notes: Reading (a) with halves (i), min 9.19, max 25.22, mean 17.20, median 16.97, midpoint 19.10;\n    four of five within tolerance, the minimum above 6.26 ± 1.33; halves (ii) also four of five\n    (min 7.61). Reading (b) three of five. With the files' BaseActivity (10 neurons) the best\n    reading gives two of five, so the outcome rests on the baseline squares.\n  deviations:\n  - Star has 12 neurons (paper 30); the other 17 Star maps cannot be registered to the stimulus.\n  - Baselines as in s4-baseline-no-difference.\n- claim: table1-s40\n  outcome: reproduced\n  notebook: reproduce_martinez_conde_2019.ipynb\n  output: claim:table1-s40\n  measured:\n  - 10.65\n  - 34.4\n  - 23.14\n  - 23.15\n  - 26.41\n  notes: Reading (a), min 10.65, max 34.40, mean 23.14, median 23.15, midpoint 26.41; all five\n    within tolerance. Reading (b) three of five. With the files' BaseActivity (19 neurons), reading\n    (a) also gives five of five.\n  deviations:\n  - The bright S40 fold as in fig4b-spike-rate-difference; 26 neurons (paper 28).\n  - Baselines as in s4-baseline-no-difference; the outcome is the same under both baselines.\n- claim: fig6-midpoint-representative\n  outcome: reproduced\n  notebook: reproduce_martinez_conde_2019.ipynb\n  output: claim:fig6-midpoint-representative\n  notes: None of the ten rank sum tests (midpoint against the mean and the median of the blocks,\n    for Edge, P180, S90, S52, S40) is significant at 0.05, under either baseline or half reading;\n    smallest p 0.36. Median differences midpoint minus along-fold range from -0.21 (Edge, median)\n    to 2.39 spikes/s (S40, mean). The paired signed rank variant finds 3 of 10 significant (S40\n    mean p = 0.015, S40 median p = 0.009, S90 median p = 0.025), so the absence rests on the\n    unpaired test the paper names.\n  deviations:\n  - Baselines and neuron numbers as in the Table 1 claims.\n- claim: fig7a-rms-contrast-fit\n  outcome: not_reproduced\n  notebook: reproduce_martinez_conde_2019.ipynb\n  output: claim:fig7a-rms-contrast-fit\n  measured:\n  - 0.9437\n  - 2.0898\n  - 1.155\n  - 0.2497\n  - 0.9668\n  - 0.8904\n  notes: Computed on the 22 Edge stimulus images in the registered frame (a 16 x 16 DU square\n    centred on the Edge, 0% to 100% in 1.5% steps, curves averaged over images; the images differ\n    by up to 0.217). Reading (a), SD over mean, is about 0.95 from 18% to 90% but 2.09 at 0% and\n    1.40 at 99%, range 0.94 to 2.09; its fit gives a = 1.155, b = 0.250, c = 0.967, R2 = 0.890\n    (measured, least squares). Reading (b), SD of 0-1 luminance, rises from 0.014 to 0.475 and fits\n    with a = -52.2, b = 0.0001, c = 52.2, R2 = 0.9988. No value but c of reading (a) and R2 of\n    reading (b) is within tolerance. A robust fit (soft L1, standing in for least absolute\n    residuals) gives the same picture.\n  deviations:\n  - The definition of RMS contrast is the paper's reference [21], not in the text read; the two\n    readings of the claims file were run, and neither gives the paper's curve.\n  - Least absolute residuals (MATLAB LAR) is approximated by a soft L1 robust fit.\n- claim: fig7c-fold-edge-equivalence\n  outcome: not_reproduced\n  notebook: reproduce_martinez_conde_2019.ipynb\n  output: claim:fig7c-fold-edge-equivalence\n  notes: Edge responses (16 x 16 DU squares centred on the Edge, 22 neurons) rise from 8.61\n    spikes/s at 0% to 20.06 at 90% luminance. P180 (3.88) is below every Edge level, nearest 0%,\n    not 50%; S40 (26.41) is nearest 90%, as the paper says. Under reading (b), RMS levels from the\n    inverse of the paper's fit (luminance 0% to 77.7%), P180 is at the lowest level as the rule\n    allows, but S40 is nearest 0.943, 0.043 from 0.90, more than one step of 0.037. With the\n    files' BaseActivity, P180 nearest 0% and S40 nearest 80% under (a).\n  deviations:\n  - The RMS levels use the paper's fitted parameters, since the refit of fig7a-rms-contrast-fit\n    does not reproduce them.\n  - Baselines and neuron numbers as in fig4b-spike-rate-difference.\n- claim: fig7c-fold-edge-significance\n  outcome: reproduced\n  notebook: reproduce_martinez_conde_2019.ipynb\n  output: claim:fig7c-fold-edge-significance\n  notes: Two-sample t-tests of fold midpoint against Edge response at the ten RMS levels. P180 is\n    lower than the Edge at 0.943 (t = -3.77, p = 0.0005) and S40 higher than the Edge at 0.610\n    (t = 3.63, p = 0.0007) and 0.647 (t = 3.55, p = 0.0009), significant under BH over 40 tests,\n    BH per fold, Bonferroni over 40 and Bonferroni per fold. With Bonferroni over 40, S40 is\n    significant at 0.610 and 0.647 only, the levels below 0.68; with BH over 40, up to 0.795, and\n    0.684 is significant under BH. With the files' BaseActivity the claim holds uncorrected and\n    with BH, not with Bonferroni.\n  deviations:\n  - Edge levels and baselines as in fig7c-fold-edge-equivalence.\n- claim: fig7d-nonlinear\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_martinez_conde_2019.ipynb\n  output: claim:fig7d-nonlinear\n  notes: The four means are monotonic in angle. The least-squares line (-0.143 per degree) leaves\n    S40, S90 and P180 off by more than their SEM (residuals 4.77, -6.26, 2.31 spikes/s). Variant,\n    the slope from 52 to 90 degrees (-0.287) differs from that from 90 to 180 (-0.048) by more\n    than the propagated SE (0.098); the slopes 40 to 52 and 52 to 90 do not differ by more than\n    theirs (0.322 against 0.447). With the files' BaseActivity, S90 and P180 are off the line by\n    more than their SEM.\n  deviations:\n  - The rule for non-linearity is the assumption the criterion names; the paper reports no test.\n- claim: fig7d-dog-similar\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the output of the difference-of-Gaussians model of the paper's reference [3] at the\n    four angles. It is not in the data set, and the paper and its supporting information give it\n    only as a curve in Fig 7D; no public, pinned copy of the model output was found.\n- claim: s3-latency-peak\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs maps made at latencies from 1 to 2400 ms, which need the spike times and eye\n    positions. The data set holds only the maps made at 60 ms.\nfindings:\n- kind: data_missing\n  statement: The data set holds 53 cells and 77 spike rate maps (22 Square and Edge, 29 Star, 26\n    Corners), where the paper analysed 58 neurons and 83 maps (25, 30, 28). The spreadsheet\n    V1_Vasarely_data_SMC.xlsx lists 58 cells, but five of them (050800J1, 062000J1, 072100_C,\n    062600A2, 09250A1) have no experiment marked and no files.\n- kind: metadata_insufficient\n  statement: 17 of the 29 Star spike rate map files have no `Standard` struct, the map registered\n    to the stimulus. The maps of the other files are in gaze coordinates, and registering them\n    needs the receptive field position of the neuron, which no file stores (the shift between the\n    gaze-frame map and `Standard` differs from file to file, and by 10 to 40 DU between the\n    experiments of one cell). These 17 maps, two of them in an older layout (prefix ABS, one\n    saved as MATLAB v7.3), cannot be placed on the stimulus.\n- kind: metadata_insufficient\n  statement: The data descriptor does not mention most of what the files hold. `Standard` (the\n    registered, rotated and cropped map with the equal-luminance polygons of the stimulus in the\n    same frame), `BaseActivity` (a baseline in spikes per ms, in 40 files, whose computation is not\n    stated and does not match the baseline squares the paper describes), `norm`, `eyetime` (one\n    file) and `original_image` (two files) are undocumented, as are the prefixes ABC, ABD, ABS and\n    AEC, the letter after the cell number (A to E), and the units of the maps (spikes per 1 ms\n    sample).\n- kind: metadata_error\n  statement: The data descriptor says `image` \"contains the raw spikes counts for each pixel\". It\n    holds the count divided by the eye time in 1 ms samples, a rate; in the one file that also\n    stores `eyetime`, image times eyetime is an integer count at every pixel, and the maximum of\n    `image` is 1.0 in every file.\n- kind: data_missing\n  statement: The spike count maps, the eye time maps (except in one file), the spike times and the\n    eye positions are not in the data set, so the number of spikes per condition and the maps at\n    other latencies (S3 Fig) cannot be computed.\n- kind: other\n  about: data\n  statement: The stored `smoothed_image` is not the Gaussian smoothing (16 DU, SD 7 DU) that the\n    paper's Fig 3B legend describes. Smoothing `image` with that filter differs from it by 19% to\n    27% of the peak in the three files tested; a 16 DU Gaussian with SD 5 DU comes within 5% to 7%.\n- kind: other\n  about: data\n  statement: Two files, ABC051000J3 and ABC063000J1, have a `BaseActivity` of exactly 0 spikes/s,\n    and in ABC051000J3 `smoothed_image_norm` is NaN everywhere.\n- kind: methods_unavailable\n  statement: Where were the two baseline squares of the Corners stimulus? The text says only \"two\n    1 x 1 DVA (16 x 16 DU) square regions in 0% luminance areas within the ROI\" (Methods, Corners)\n    and shows them in Fig 2C. This attempt took the two bottom corners of the ROI. For Square and\n    Edge and for Star, were the four squares inside the corners of the circumscribing square, as\n    assumed here (centred on the corners they leave the ROI)? The baseline decides whether the\n    baselines differ across stimuli (S4 Fig) and which Table 1 values fall within the paper's SEM;\n    the files' own `BaseActivity` gives different results.\n- kind: methods_unavailable\n  statement: How was the local RMS contrast along the Edge computed (reference [21])? Neither the\n    SD of luminance over its mean nor the SD of luminance scaled to 0 to 1, in a 16 x 16 DU square\n    centred on the Edge of the deposited stimulus images, gives the range 0.61 to 0.943 or the fit\n    f(l) = -0.34 exp(-0.05 l) + 0.95.\n- kind: methods_unavailable\n  statement: Which test found no difference in absolute baseline across the stimuli (S4 Fig), and\n    in Table 1 were the minimum, maximum, mean and median taken per neuron and then averaged, or\n    from the population-average profile, and were the two half-diagonals of the Square and the Star\n    averaged before or after the summaries? The attempt ran each reading the claims file lists.\n"
}
```

```
File created successfully at: attempts/martinez-conde-2019-02.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/martinez-conde-2019 && python - <<'EOF'
s=open('vasarely.py').read()
old_start=s.index("def standard_stimulus(")
old_end=s.index("def fold_geometry(")
new='''def frame_transform(stim, std, condition: str):
    """Rotation R and translation t from the stimulus file's frame to the Standard frame,
    fitted on the equal-luminance polygons, which both files store (Q = P R^T + t)."""
    if condition == "Edge-compare":
        full, frame = stim.SquareVert, std.EdgecompVert.SquareVert
    elif condition == "Corners":
        full, frame = stim.CornersVert, std.CornersVert
    else:
        full, frame = stim.DiagVert, std.DiagVert
    best = None
    # the star's vertices may be listed from another point, so try every cyclic shift
    for shift in (range(24) if condition == "Star" else [0]):
        P = np.vstack([np.roll(_poly(full[k]), shift, axis=0) for k in range(0, 90, 10)])
        Q = np.vstack([_poly(frame[k]) for k in range(0, 90, 10)])
        R, t = _rigid(P, Q)
        err = np.abs(P @ R.T + t - Q).max()
        if best is None or err < best[0]:
            best = (err, R, t)
    return best[1], best[2]


def _to_full(shape, R, t, margin: int = 0):
    H, W = shape
    cc, rr = np.meshgrid(np.arange(-margin, W + margin) + 1.0, np.arange(-margin, H + margin) + 1.0)
    return (np.c_[cc.ravel(), rr.ravel()] - t) @ R, (H + 2 * margin, W + 2 * margin)


def standard_stimulus(stim, std, condition: str) -> np.ndarray:
    """The file's stimulus image resampled into the Standard frame (nearest pixel); image pixel
    (row, col) has coordinates (x, y) = (col + 1, row + 1), as the image and its polygons show."""
    image = {"Edge-compare": "EdgecompImage", "Corners": "CornersImage", "Star": "DiagImage"}[condition]
    R, t = frame_transform(stim, std, condition)
    F, shape = _to_full(std.smoothed_image.shape, R, t)
    return map_coordinates(np.asarray(getattr(stim, image), float), [F[:, 1] - 1, F[:, 0] - 1], order=0,
                           cval=np.nan).reshape(shape)


def gaze_shift(full_map: np.ndarray, std_map: np.ndarray, R, t, margin: int = 420):
    """The shift (DU, display frame) that carries the stimulus-frame position of each Standard
    pixel to where the gaze-frame map holds its value, found by least squares over integer shifts
    in the Standard frame; with the correlation of the shifted map with `std_map`. It stands for
    the receptive field position, which the files do not store."""
    F, shape = _to_full(std_map.shape, R, t, margin)
    G = map_coordinates(full_map, [F[:, 1] - 1, F[:, 0] - 1], order=1, cval=0).reshape(shape)
    xc = fftconvolve(G, std_map[::-1, ::-1], mode="valid")
    g2 = fftconvolve(G ** 2, np.ones_like(std_map), mode="valid")
    i, j = np.unravel_index(np.argmin(g2 - 2 * xc), xc.shape)
    H, W = std_map.shape
    r = np.corrcoef(G[i:i + H, j:j + W].ravel(), std_map.ravel())[0, 1]
    return np.array([j - margin, i - margin], float) @ R, float(r)


'''
s=s[:old_start]+new+s[old_end:]
s=s.replace("from scipy.ndimage import map_coordinates","from scipy.ndimage import map_coordinates\nfrom scipy.signal import fftconvolve")
s=s.replace('''            rec["lum"] = standard_stimulus(stim, std, condition)''','''            rec["lum"] = standard_stimulus(stim, std, condition)
            if shifts:
                R, t = frame_transform(stim, std, condition)
                rec["gaze_shift"], rec["gaze_shift_r"] = gaze_shift(np.asarray(d.smoothed_image, float),
                                                                    np.asarray(std.smoothed_image, float), R, t)''')
s=s.replace('''def load_all(z: zipfile.ZipFile | None = None) -> list[dict]:
    """Every spike rate map file with its stimulus, reduced to what the analysis uses."""''','''def load_all(z: zipfile.ZipFile | None = None, shifts: bool = True) -> list[dict]:
    """Every spike rate map file with its stimulus, reduced to what the analysis uses."""''')
s=s.replace('''        rec["full_smoothed_max_hz"] = float(np.asarray(d.smoothed_image).max() * RATE_SCALE)''','''        rec["full_smoothed_max_hz"] = float(np.asarray(d.smoothed_image).max() * RATE_SCALE)
        if hasattr(d, "smoothed_image_norm"):
            rec["norm_all_nan"] = bool(np.isnan(np.asarray(d.smoothed_image_norm, float)).all())''')
open('vasarely.py','w').write(s)
EOF
grep -n "_rigid\|def \|shifts" vasarely.py | head -40
```

```
92:def open_zip() -> zipfile.ZipFile:
97:def checksums() -> str:
102:def read_mat(z: zipfile.ZipFile, name: str):
111:def parse_code(stem: str) -> dict:
118:def spreadsheet(z: zipfile.ZipFile) -> pd.DataFrame:
132:def _dense(a):
137:def _poly(p) -> np.ndarray:
141:def _rigid(P: np.ndarray, Q: np.ndarray):
149:def frame_transform(stim, std, condition: str):
163:        R, t = _rigid(P, Q)
170:def _to_full(shape, R, t, margin: int = 0):
176:def standard_stimulus(stim, std, condition: str) -> np.ndarray:
186:def gaze_shift(full_map: np.ndarray, std_map: np.ndarray, R, t, margin: int = 420):
188:    pixel to where the gaze-frame map holds its value, found by least squares over integer shifts
201:def fold_geometry(std, condition: str) -> dict:
247:def box_mask(shape, x: float, y: float, w: float, h: float) -> np.ndarray:
257:def box_mean(M: np.ndarray, x: float, y: float, w: float, h: float | None = None) -> float:
262:def point_at(fold, frac: float):
268:def midpoint(M, fold) -> float:
273:def blocks(M, fold, n: int = 10) -> np.ndarray:
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
s=open('vasarely.py').read()
s=s.replace('''def frame_transform(stim, std, condition: str):
    """Rotation R and translation t from the stimulus file's frame to the Standard frame,
    fitted on the equal-luminance polygons, which both files store (Q = P R^T + t)."""''','''def frame_transform(stim, std, condition: str, every: bool = False):
    """Rotation R and translation t from the stimulus file's frame to the Standard frame,
    fitted on the equal-luminance polygons, which both files store (Q = P R^T + t). The star is
    symmetric under turns of 30 degrees, so its polygons fit several; `every` returns them all."""''')
s=s.replace('''    best = None
    # the star's vertices may be listed from another point, so try every cyclic shift
    for shift in (range(24) if condition == "Star" else [0]):
        P = np.vstack([np.roll(_poly(full[k]), shift, axis=0) for k in range(0, 90, 10)])
        Q = np.vstack([_poly(frame[k]) for k in range(0, 90, 10)])
        R, t = _rigid(P, Q)
        err = np.abs(P @ R.T + t - Q).max()
        if best is None or err < best[0]:
            best = (err, R, t)
    return best[1], best[2]''','''    fits = []
    # the star's vertices may be listed from another point, so try every cyclic shift
    for shift in (range(24) if condition == "Star" else [0]):
        P = np.vstack([np.roll(_poly(full[k]), shift, axis=0) for k in range(0, 90, 10)])
        Q = np.vstack([_poly(frame[k]) for k in range(0, 90, 10)])
        R, t = _rigid(P, Q)
        fits.append((np.abs(P @ R.T + t - Q).max(), R, t))
    fits.sort(key=lambda f: f[0])
    if every:
        return [(R, t) for err, R, t in fits if err < 1e-6]
    return fits[0][1], fits[0][2]''')
s=s.replace('''            if shifts:
                R, t = frame_transform(stim, std, condition)
                rec["gaze_shift"], rec["gaze_shift_r"] = gaze_shift(np.asarray(d.smoothed_image, float),
                                                                    np.asarray(std.smoothed_image, float), R, t)''','''            if shifts:
                found = [gaze_shift(np.asarray(d.smoothed_image, float), np.asarray(std.smoothed_image, float), R, t)
                         for R, t in frame_transform(stim, std, condition, every=True)]
                rec["gaze_shift"], rec["gaze_shift_r"] = max(found, key=lambda f: f[1])''')
open('vasarely.py','w').write(s)
EOF
cd $TMPDIR && source scratch/bin/activate && time python - <<'EOF'
import sys,resource; sys.path.insert(0,'entries/martinez-conde-2019')
import vasarely as v, numpy as np, pandas as pd
recs=v.load_all()
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
df=pd.DataFrame([{'file':r['file'],'cell':r['cell'],'cond':r['condition'],'dx':r['gaze_shift'][0],'dy':r['gaze_shift'][1],'r':r['gaze_shift_r']} for r in recs if r['registered']])
print(df.round(3).to_string())
print({r['file']:r['norm_all_nan'] for r in recs if r.get('norm_all_nan')})
EOF
```

```
0.447204
            file      cell          cond       dx       dy      r
0    ABC041900J2  041900J2       Corners -296.908   20.260  0.998
1    ABC042000J1  042000J1       Corners -279.476   46.530  1.000
2    ABC042400J2  042400J2       Corners -277.000   59.000  0.999
3    ABC042600J2  042600J2       Corners -313.747   16.092  1.000
4    ABC042700J2  042700J2       Corners -269.346   19.969  0.999
5    ABC042800J2  042800J2       Corners -283.151   22.168  1.000
6   ABC050900J1A  050900J1       Corners -290.229   31.309  0.998
7    ABC051000J3  051000J3       Corners -292.112   20.581  0.999
8    ABC051500J1  051500J1       Corners -385.086    7.591  1.000
9    ABC051600J1  051600J1       Corners -342.927   -7.139  1.000
10   ABC051800J1  051800J1       Corners -361.650   -2.456  0.999
11   ABC052600J1  052600J1       Corners -294.274   16.145  1.000
12   ABC060600J1  060600J1       Corners -341.134    9.620  1.000
13   ABC060700J1  060700J1       Corners -146.494 -171.943  0.999
14   ABC062100J1  062100J1       Corners -308.866   47.684  1.000
15   ABC062600J1  062600J1       Corners -331.128   72.633  1.000
16   ABC062700J1  062700J1       Corners -235.086   89.177  1.000
17   ABC062800A4  062800A4       Corners -108.083  107.662  1.000
[... 48 more lines not kept]
```

**Agent**

All 60 registered maps are the gaze-frame map rotated and shifted (r ≥ 0.996), and the shift for one cell differs across experiments. Adding this to the notebook.

**Agent calls Bash**

```bash
cd entries/martinez-conde-2019 && python - <<'EOF'
s=open('vasarely.py').read()
s=s.replace('''        if hasattr(d, "smoothed_image_norm"):
            rec["norm_all_nan"] = bool(np.isnan(np.asarray(d.smoothed_image_norm, float)).all())
''','')
open('vasarely.py','w').write(s)
p='/tmp/claude-1001/build_nb.py'; s=open(p).read()
a='''md(r"""
In every registered file the folds run'''
assert s.count(a)==1
s=s.replace(a,'''code(r"""
sh = pd.DataFrame([{"file": r["file"], "cell": r["cell"], "condition": r["condition"], "shift_x": r["gaze_shift"][0],
                    "shift_y": r["gaze_shift"][1], "r": r["gaze_shift_r"]} for r in reg])
print(f"Standard map against the rotated, shifted gaze-frame map: r from {sh.r.min():.3f} to {sh.r.max():.3f} over {len(sh)} files")
multi = sh[sh.cell.isin(sh.cell[sh.cell.duplicated()])].sort_values(["cell", "condition"])
print("Shift (DU, display frame) for cells registered in more than one experiment:")
print(multi.round(1).to_string(index=False))
spread = multi.groupby("cell").apply(lambda g: np.hypot(g.shift_x.max() - g.shift_x.min(), g.shift_y.max() - g.shift_y.min()))
print(f"Largest distance between the shifts of one cell, per cell: {spread.round(1).to_dict()}")
""", ["sanity"])

md(r"""
Every `Standard` map is the gaze-frame `smoothed_image` rotated like the stimulus and shifted
(r of at least 0.996). The shift stands for the receptive field position, which the files do not
store, and it is not the same for one cell across experiments (distances printed above), so it
cannot be taken from another experiment of the same cell. The 17 Star maps without `Standard`
therefore cannot be placed on the stimulus here.
""")

'''+a)
open(p,'w').write(s)
EOF
source $TMPDIR/scratch/bin/activate && python $TMPDIR/build_nb.py && rm -rf __pycache__
```

```
written 80
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/martinez-conde-2019 2>&1 | tail -4; source $TMPDIR/scratch/bin/activate; python - <<'EOF'
import nbformat
nb=nbformat.read('executed/martinez-conde-2019/reproduce_martinez_conde_2019.ipynb',as_version=4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='code':
        t=''.join(o.get('text','') for o in c.outputs if o.output_type=='stream')
        if 'Shift (DU' in t or 'Total run' in t or 'loaded in' in t: print(t)
    for o in c.get('outputs',[]):
        if o.output_type=='error': print('ERR',i,o.evalue)
EOF
```

```
Sun Nov 15 09:54:17 UTC 2026
Installed kernelspec registry-martinez-conde-2019 in executed/martinez-conde-2019/.venv/share/jupyter/kernels/registry-martinez-conde-2019
0 error(s)
pass  reproduce_martinez_conde_2019.ipynb  (72 s)
checksums.md5 of the data set:
9ca5ae49dfc19e516b09c99e62eefc23  docs/crcns_pvc-12_data_description.docx
e67a2f96c6651ba3c9ac3a28297a00f4  docs/crcns_pvc-12_data_description.pdf
06c85736f287b47c60ab2da8539ff226  filelist.txt
e1301fe463e72332e2303b2053ee0559  V1_Vasarely_data.zip

data set pvc-12 (unversioned, doi:10.6080/K05D8Q1T); 77 spike rate map files loaded in 50 s; peak memory 0.51 GB

Standard map against the rotated, shifted gaze-frame map: r from 0.996 to 1.000 over 60 files
Shift (DU, display frame) for cells registered in more than one experiment:
       file     cell    condition  shift_x  shift_y   r
ABC062700J1 062700J1      Corners   -235.1     89.2 1.0
ABD062700J1 062700J1         Star   -233.5    106.1 1.0
ABC062800A4 062800A4      Corners   -108.1    107.7 1.0
ABD062800A4 062800A4         Star    -79.8     88.7 1.0
ABC063000J1 063000J1      Corners   -242.0     72.5 1.0
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/martinez-conde-2019-02.yaml'; s=open(p).read()
a='''    needs the receptive field position of the neuron, which no file stores (the shift between the
    gaze-frame map and `Standard` differs from file to file, and by 10 to 40 DU between the
    experiments of one cell). These 17 maps,'''
assert a in s
s=s.replace(a,'''    needs the receptive field position of the neuron, which no file stores. Each `Standard` map is
    the gaze-frame map rotated and shifted (r of at least 0.996 over 60 files), and the shift
    differs from file to file and, for one cell, by 11 to 58 DU between experiments. These 17 maps,''')
a='''- kind: other
  about: data
  statement: Two files, ABC051000J3 and ABC063000J1, have a `BaseActivity` of exactly 0 spikes/s,
    and in ABC051000J3 `smoothed_image_norm` is NaN everywhere.'''
assert a in s
s=s.replace(a,'''- kind: other
  about: data
  statement: Two files, ABC051000J3 and ABC063000J1, have a `BaseActivity` of exactly 0 spikes/s.''')
open(p,'w').write(s)
p='entries/martinez-conde-2019/entry.yaml'; s=open(p).read(); s=s.replace('runtime_minutes: 1','runtime_minutes: 2'); open(p,'w').write(s)
p='entries/martinez-conde-2019/README.md'; s=open(p).read(); s=s.replace('It takes about a minute, most of it\n  streaming the zip.','It takes about two minutes, most of it\n  streaming the zip and matching each registered map to its gaze-frame map.'); open(p,'w').write(s)
EOF
python tools/entry.py all entries/martinez-conde-2019 2>&1 | tail -3
```

```
Installed kernelspec registry-martinez-conde-2019 in executed/martinez-conde-2019/.venv/share/jupyter/kernels/registry-martinez-conde-2019
0 error(s)
pass  reproduce_martinez_conde_2019.ipynb  (73 s)
```

**Agent calls Bash**

```bash
cd  source $TMPDIR/scratch/bin/activate; python - <<'EOF'
import nbformat
def tagged(p):
    nb=nbformat.read(p,as_version=4); d={}
    for c in nb.cells:
        for t in c.metadata.get('tags',[]):
            if t.startswith('claim:'): d[t]=''.join(o.get('text','') for o in c.outputs if o.output_type=='stream')
    return d
a=tagged('/tmp/claude-1001/exec.ipynb'); b=tagged('executed/martinez-conde-2019/reproduce_martinez_conde_2019.ipynb')
print(len(a),len(b),[k for k in a if a[k]!=b.get(k)])
EOF
python tools/entry.py handover entries/martinez-conde-2019; ls executed/martinez-conde-2019/handover; date -u
```

```
16 16 []
Traceback (most recent call last):
  File "tools/entry.py", line 59, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
ls: cannot access 'executed/martinez-conde-2019/handover': No such file or directory
Sun Nov 15 09:57:15 UTC 2026
```

**Agent calls Bash**

```bash
cd  /opt/hostedtoolcache/Python/3.13.18/x64/bin/python tools/entry.py handover entries/martinez-conde-2019; ls executed/martinez-conde-2019/handover; /opt/hostedtoolcache/Python/3.13.18/x64/bin/python tools/entry.py check entries/martinez-conde-2019 | tail -2; ls entries/martinez-conde-2019; git status --short 2>/dev/null | head
```

```
wrote executed/martinez-conde-2019/handover
martinez-conde-2019.yaml
reproduce_martinez_conde_2019.ipynb
vasarely.py
0 error(s)
README.md
__pycache__
entry.yaml
reproduce_martinez_conde_2019.ipynb
requirements.in
requirements.lock.txt
vasarely.py
```

**Agent calls Bash**

```bash
cd  rm -rf entries/martinez-conde-2019/__pycache__; ls entries/martinez-conde-2019; date -u
```

```
README.md
entry.yaml
reproduce_martinez_conde_2019.ipynb
requirements.in
requirements.lock.txt
vasarely.py
Sun Nov 15 09:57:48 UTC 2026
```

**Agent**

I've done steps 1 to 6: the entry is at `entries/martinez-conde-2019/`, the record at `attempts/martinez-conde-2019-02.yaml`, and `tools/entry.py check` and `all` report 0 errors. The handover is in `executed/martinez-conde-2019/handover/`. Nothing is committed. I did not see any earlier attempt, by accident or otherwise.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| neuron-counts | not reproduced (53 cells; 22/29/26 maps per stimulus against the paper's 25/30/28; 7 cells in all three stimuli matches) |
| spikes-per-condition | blocked, data_missing |
| s4-baseline-no-difference | not reproduced, rests on an assumption |
| fig4a-above-baseline | reproduced |
| fig4b-spike-rate-difference | partially reproduced, rests on an assumption (order holds; S90 is 8.21, just below its tolerance) |
| fig4b-pairwise-significance | reproduced |
| fig5-average-maps | reproduced, rests on an assumption |
| table1-edge | not reproduced |
| table1-p180 | partially reproduced |
| table1-s90 | not reproduced |
| table1-s52 | partially reproduced, rests on an assumption |
| table1-s40 | reproduced |
| fig6-midpoint-representative | reproduced |
| fig7a-rms-contrast-fit | not reproduced |
| fig7c-fold-edge-equivalence | not reproduced |
| fig7c-fold-edge-significance | reproduced |
| fig7d-nonlinear | reproduced, rests on an assumption |
| fig7d-dog-similar | blocked, data_missing |
| s3-latency-peak | blocked, data_missing |

## 2. Dataset, assumptions, questions

What the dataset holds:
- **Counts.** One zip holding 77 rate maps for 53 cells. The spreadsheet lists 58 cells, but 5 of them have no files.
- **Registration.** Only 60 maps carry `Standard`, the authors' map registered to the stimulus, which the data descriptor does not mention. Placing a map on the stimulus needs the receptive-field position, which no file stores, and it differs between experiments of the same cell by 11 to 58 DU.
- **Star neurons left out.** Because of that, the 17 Star maps without `Standard` cannot be registered, and the Star results rest on 12 of the paper's 30 neurons.
- **Units.** The descriptor calls `image` raw spike counts; it is actually a rate (spikes per 1 ms sample of eye time).
- **Smoothing.** The stored smoothing is close to a Gaussian with SD 5 DU, not the 7 DU in the Fig 3B legend.
- **Undocumented baseline.** The files' `BaseActivity` is not documented, does not match the paper's baseline squares, and is exactly 0 in two files.
- **Missing data.** The files have no spike counts, eye times (except in one file), spike times or eye positions, which is what blocks the spike-count and latency claims.

Assumptions:
- **Baseline square positions.** For Square and Edge and for Star, I put the squares inside the corners of the circumscribing square, because centred on the corners they fall outside the region analysed. The paper gives no positions for the two Corners squares; I used the two bottom corners of that region, the only 0% luminance band in it. The files' `BaseActivity` is run as a variant.
- **Which S40 fold is bright.** I picked it from the stimulus image as the fold where luminance peaks; it is the same fold in all 26 Corners files.

There are three `methods_unavailable` questions for the authors: where the baseline squares are, how RMS contrast is defined (their reference [21]), and which test and order of summary lie behind S4 Fig and Table 1. I asked no reader questions.

## 3. Protocol gaps

1. The protocol has no spatial version of the "same clock" check for map-only data. I compared each neuron's response along the Edge with the same band shifted sideways (16 of 22 neurons peak on the Edge) and reported it as consistent with registration, not proof.
2. It is unclear whether the data set's own undocumented baseline counts as the paper's method. I kept the paper's squares as the main reading and showed `BaseActivity` as a variant; the outcomes are marked as resting on the assumption wherever the two disagree.
3. The `assumed` flag does not say whether an assumption the claims file itself names (for example the non-linearity rule in fig7d-nonlinear) counts. I set `assumed: true` in those cases.
4. For "record the first reading" when no reading matches, the protocol gives no rule. I recorded reading (a), halves (i) for S90.

## 4. Runtime and failures

The notebook runs in about 73 s with 0.51 GB peak memory, and the whole session took about 35 minutes. Nothing failed.

## End of run

67 turns, 27 minutes, $7.03 at API prices, result: success.
