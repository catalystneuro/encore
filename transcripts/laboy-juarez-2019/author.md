# laboy-juarez-2019 · author · run 43263909874

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries claims attempts paper | head -100; wc -l docs/*.md README.md
```

```
Thu Nov 12 17:01:43 UTC 2026
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
[... 124 more lines not kept]
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
3	Version: `pilot-14`. Record this version in the attempt's provenance.
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
ls paper entries/fouke-2025 entries/fouke-2025/*; cat claims/laboy-juarez-2019.yaml
```

```
<persisted-output>
Output too large (66KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/ed3735a8-7bcc-46af-aa17-f9992ba32306/tool-results/bq1vd0gwe.txt

Preview (first 2KB):
entries/fouke-2025/README.md
entries/fouke-2025/entry.yaml
entries/fouke-2025/omr.py
entries/fouke-2025/reproduce_fouke_2025.ipynb
entries/fouke-2025/requirements.in
entries/fouke-2025/requirements.lock.txt

entries/fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt

paper:
[... 25 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/laboy-juarez-2019.yaml"
}
```

```
1	# Claims for Laboy-Juarez, Langberg, Ahn & Feldman (2019), "Elementary motion sequence detectors in
2	# whisker somatosensory cortex", Nature Neuroscience 22, 1438-1449, doi:10.1038/s41593-019-0448-6,
3	# tested on CRCNS ssc-9 (primary; doi:10.6080/K0FJ2F13, "Extracellular recordings in mouse barrel
4	# cortex during single- and 2-whisker stimulation", whose description names this paper as the
5	# basis of its three experiments).
6	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
7	# protocol pilot-14 as stated in docs/protocol.md (Reader).
8	#
9	# Text read. paper/10.1038-s41593-019-0448-6.txt, the version of record (PDF supplied by a person,
10	# extracted with PyMuPDF), with the main text, figure legends, Methods, Data and Code availability,
11	# the Nature Research reporting summary, and the supplement (41593_2019_448_MOESM1_ESM.pdf), which
12	# holds the legends of Supplementary Figures 1 to 8. The PDF was not opened: every number used
13	# below is printed in the text or a legend. The Methods' sparseness and supralinearity formulas
14	# are garbled by the extraction; they are read here as the standard lifetime sparseness of Vinje
15	# and Gallant (ref. 28), S = (1 - E(r)^2 / E(r^2)) / (1 - 1/n), and as
16	# z = (mu_CWSW - (mu_CW + mu_SW)) / sqrt(se_CW^2 + se_SW^2), which is what the legible parts say.
17	# The data set's description (paper/ssc-9.data-description.txt) was read only to know what it
18	# holds; no claim comes from it.
19	#
20	# Code. The paper links none; "The Matlab code for performing the statistical and data analyses
[... 901 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/laboy-juarez-2019.yaml",
 "offset": 922
}
```

```
922	  criterion: The alignment index is the Pearson correlation, over the eight combinations at the
923	    best dt, between linear predictions and residuals (measured minus 0.64 times linear) (Fig. 7f
924	    legend). The legend labels the outbound group "Best dt >= 0" in one panel and "> 0" in the
925	    other; 121 + 56 = 177 of 187; readings are (a) best dt = 0 excluded, (b) included with
926	    outbound, (c) units whose best-combination curve was set constant across dt (no best dt;
927	    Methods, dt smoothing) excluded, with best dt = 0 read as in (a) or (b). Reproduced when, under one reading, both t-tests give p < 0.05 with the inbound
928	    means higher; partially reproduced for one.
929	- id: fig7g-inbound-decoding
930	  statement: Spatial combination decoding was better for inbound-order stimuli than for
931	    outbound-order stimuli.
932	  source: Results, Order selectivity dominates dt tuning, paragraph 2; Figure 7g
933	  quote: spatial combination decoding was better for inbound order stimuli than outbound order
934	    stimuli (Fig. 7g)
935	  depends_on:
936	  - fig3e-identity-decoder
937	  criterion: The identity decoder retrained and tested within each 10 ms dt range of Fig. 7g
938	    ([-50,-41] to [41,50]), 1000 ensembles each. The ensemble size and units are not stated, and
939	    the decoder is "as in Fig. 4", whose decoders are built on CW-tuned or SW-tuned units apart;
940	    readings are (a) N = 187 from the selective units, (b) N = 100 from the selective units, (c)
941	    the CW-tuned and SW-tuned decoders of Fig. 4 apart, each at N = 100. Reproduced when, under
[... 216 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/ssc-9.data-description.txt; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in entries/fouke-2025/README.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,400p docs/archives.md | grep -n -i -A40 "## CRCNS" | head -80; cat papers/datasets/laboy-juarez-2019.yaml 2>/dev/null; ls questions | head;
```

```
33:## CRCNS
34-
35-- **Datasets.** A CRCNS data set, identified by its short name (`ret-1`,
36-  `hc-3`), with a DOI of its own (`10.6080/...`). The registry's list is
37-  `targets/crcns.json`, written by hand; for now it holds one data set, to test
38-  the pipeline beyond DANDI.
39-- **Versions.** CRCNS data sets are not versioned. Record the version as
40-  `unversioned`, with the data set's DOI under `dataset: doi`, and give in the
41-  notebook header the MD5 sums from the data set's `checksums.md5` for the
42-  files read, so a later change is detectable.
43-- **Reading.** The files are in the public S3 bucket `crcnsarchive` (region
44-  us-west-2), under `<id>/`, readable without an account at
45-  `https://crcnsarchive.s3-us-west-2.amazonaws.com/<id>/<file>`; list a data
46-  set with `?list-type=2&prefix=<id>/` on the bucket's address. The site
47-  crcns.org asks for a login to download; the bucket does not. Most data sets
48-  are zip files of MATLAB or other files: open the zip in place with
49-  `fsspec.open(url, block_size=2**20).open()` and Python's `zipfile`, which
50-  read only the parts needed over range requests (`remfile` lacks what
51-  `zipfile` needs to read a member), and load members in memory
52-  (`scipy.io.loadmat`, or `h5py` for MATLAB 7.3 files). Do not download whole
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=ssc-9/" | python3 -c "
import sys,re
t=sys.stdin.read()
for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',t): print(s,k)
print('trunc', re.findall(r'<IsTruncated>(.*?)<',t))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
B=https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live; curl -s $B/checksums.md5; curl -s $B/filelist.txt; python3 -c "import fsspec,scipy,h5py,sklearn;print('ok')"; ls ~/.venv 2>/dev/null; which python; python --version
```

```
2e7a774017619e76c46db85722587be3  data.zip
d716508f420a0a6cd87b9298c966648e  docs/crcns_ssc-9_data_description.docx
d5d1590c38b8eea45e070e8cdfc4827f  docs/crcns_ssc-9_data_description.pdf
3e88ce7e756bd74c360ba5dcfffc0316  filelist.txt
# CRCNS.org 'ssc-9' dataset files
# To use this for fetching files, comment out files that are
# not needed by putting a '#' as the first character on the line (default mode)
# or put a '+' as the first character to specifiy files to be fetched (+ mode).
# mode='default' (change to '+' for + mode).
 data.zip	169025319 (161.1 MB)
 docs/crcns_ssc-9_data_description.docx	56609 (55.2 KB)
 docs/crcns_ssc-9_data_description.pdf	177890 (173.7 KB)
 checksums.md5	235
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fsspec,scipy,h5py,sklearn;print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'fsspec'
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
Python 3.13.18
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q fsspec aiohttp requests scipy h5py numpy pandas scikit-learn statsmodels matplotlib nbformat nbclient ipykernel 2>&1 | tail -2; python -c "import fsspec,scipy;print('ok')"; echo $TMPDIR
```

```
ok
/tmp/claude-1001
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec,zipfile,time
t=time.time()
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
for i in z.infolist(): print(i.file_size,i.compress_size,i.filename)
print(time.time()-t)
"
```

```
0 0 Experiment1/
197920064 6934545 Experiment1/20170515.mat
187229784 8523949 Experiment1/20170605.mat
121144216 4725976 Experiment1/20170513.mat
268508984 9161808 Experiment1/20170621.mat
234340312 10072901 Experiment1/20170510.mat
0 0 Experiment2/
37575384 1949212 Experiment2/20160506.mat
295982744 16213543 Experiment2/20160504.mat
177090632 7561663 Experiment2/20160909.mat
110691368 6272996 Experiment2/20160808.mat
227210616 9552758 Experiment2/20160406.mat
314003976 14047623 Experiment2/20160817.mat
99185816 3954426 Experiment2/20160829.mat
288344288 12215810 Experiment2/20160803.mat
132898224 6512587 Experiment2/20160325.mat
13991576 698308 Experiment2/20160316.mat
46108640 2518922 Experiment2/20160225.mat
547630272 32646827 Experiment2/20160914.mat
0 0 Experiment3/
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec,zipfile,time,io,scipy.io as sio,resource
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
for name in ['Experiment2/20160316.mat','Experiment3/20190123.mat']:
  t=time.time(); b=z.read(name); print(name, len(b), b[:120])
  m=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)
  print(time.time()-t, [k for k in m if not k.startswith('__')])
  for k,v in m.items():
    if k.startswith('__'): continue
    print(k,type(v),getattr(v,'shape',None))
    u=v[0] if hasattr(v,'shape') and v.shape else v
    for fn in u._fieldnames:
      x=getattr(u,fn); print('  ',fn,type(x),getattr(x,'shape',None), repr(x)[:300] if not hasattr(x,'shape') or x.dtype!=object else [repr(x[i])[:80] for i in range(3)])
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
"
```

```
Experiment2/20160316.mat 13991576 b'MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Fri May 10 16:38:31 2019                                        \x00\x00\x00\x00'
0.7767066955566406 ['UnitInfoExp2']
UnitInfoExp2 <class 'numpy.ndarray'> (2,)
   recName <class 'str'> None 'KJL_20160316_1721-2119_chn1_Param1.mat'
   recDepth <class 'int'> None 635
   waveform <class 'numpy.ndarray'> (47, 4) array([[ 1.02980310e-01, -4.02042154e+00,  1.71807126e+00,
         7.75646281e-01],
       [ 1.51943648e-01, -3.83908380e+00,  1.80507936e+00,
         8.40751582e-01],
       [ 1.32556971e-01, -3.71496773e+00,  1.86936345e+00,
         9.22093365e-01],
       [ 1.50912278e-02, -3.66151260e+00,  1.
   DeflectedWs <class 'numpy.ndarray'> (29924,) ['array([5, 3], dtype=uint8)', 'array([8, 6], dtype=uint8)', 'array([8, 1], dtype=uint8)']
   timeWs <class 'numpy.ndarray'> (29924,) ['array([150, 108], dtype=uint8)', 'array([150, 159], dtype=uint8)', 'array([150, 131], dtype=uint8)']
   directionWs <class 'numpy.ndarray'> (29924,) ['array([1, 1], dtype=uint8)', 'array([ 1, -1], dtype=int16)', 'array([ 1, -1], dtype=int16)']
   spkTime <class 'numpy.ndarray'> (29924,) ['array([ 8.864     , 39.264     , 64.16      , 73.952     , 99.29962992])', 'array([], dtype=uint8)', 'array([], dtype=uint8)']
Experiment3/20190123.mat 13135760 b'MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Fri May 10 16:05:57 2019                                        \x00\x00\x00\x00'
0.4973905086517334 ['UnitInfoExp3']
UnitInfoExp3 <class 'numpy.ndarray'> (11,)
   spkTime <class 'numpy.ndarray'> (8118,) ['array([292.14961373,   1.        ])', 'array([290.76592679,   2.        ])', 'array([[ 37.78800583,   3.        ],\n       [ 41.59728575,   3.        ],\n      ']
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec,zipfile,time,io,scipy.io as sio,numpy as np
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
m=sio.loadmat(io.BytesIO(z.read('Experiment3/20190123.mat')),squeeze_me=True,struct_as_record=False)['UnitInfoExp3']
u=m[0]
e=u.experiment
def show(s,ind=''):
  for fn in s._fieldnames:
    x=getattr(s,fn)
    if hasattr(x,'_fieldnames'): print(ind,fn,'struct'); show(x,ind+'  ')
    else: print(ind,fn,type(x).__name__,getattr(x,'shape',None),repr(x)[:200])
show(e)
for i in range(8): print(u.DeflectedWs[i],u.DeltaT[i],np.atleast_2d(u.spkTime[i])[:6].tolist())
import collections
print(collections.Counter(str(d) for d in u.DeflectedWs).most_common(50))
print(collections.Counter(u.DeltaT[~np.isnan(u.DeltaT)]))
for v in m: print(v.recName, getattr(v.experiment,'_fieldnames',None) and None, len(v.spkTime))
"
```

```
Index ndarray (0,) array([], dtype='<U1')
 Animal_ID str None '181207t'
 Recording_Date int None 190123
 Genotype str None 'B6'
 Age int None -1
 Rec_Num int None 2
 Whiskers str None 'E2 E1 delta D2 D1 gamma C2 C1 beta'
 Piezo_Distance int None 2500
 Weight_Percent int None 80
 Tip_Depth int None 560
 Electrode str None 'Poly2_16Ch'
 Electrode_Serial_Num str None 'G767'
 Bad_Channels ndarray (0,) array([], dtype=uint8)
 Channel_Map ndarray (4,) array([array([26, 27, 17, 10], dtype=uint8),
       array([ 4,  1, 15, 16], dtype=uint8),
       array([18, 13, 22,  9], dtype=uint8),
       array([11, 14,  3,  2], dtype=uint8)], dtype=object)
 Fs float None 24414.063
[1 8] -40.0 [[292.14961372784654, 1.0]]
[8 9] 0.0 [[290.7659267929841, 2.0]]
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q pymupdf && curl -s -o desc.pdf https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/docs/crcns_ssc-9_data_description.pdf && python -c "
import fitz
d=fitz.open('desc.pdf')
for p in [1,2]:
  d[p].get_pixmap(dpi=80).save(f'p{p}.png')
"; ls $TMPDIR/*.png
```

Result: the fetched text is not kept.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p1.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p2.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
wc -c paper/*.txt; grep -n -i "Δt\b" paper/10.1038-s41593-019-0448-6.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -E "^(Methods|Online content|Analysis of neuronal|Δt smoothing|Combination selectivity|Neural decoders|Testing for|Recordings in awake|Data availability|Statistics)" paper/10.1038-s41593-019-0448-6.txt; wc -l paper/10.1038-s41593-019-0448-6.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-019-0448-6.txt",
 "offset": 1896,
 "limit": 300
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; grep -n -i -E "SW precedes|CW precedes|leads|negative Δt|sham|spontaneous" paper/10.1038-s41593-019-0448-6.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && /usr/bin/time -v python -c "
import fsspec,zipfile,time,io,scipy.io as sio,numpy as np,resource
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
t=time.time()
b=z.read('Experiment2/20160914.mat'); print('read',time.time()-t)
m=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False); del b
print('load',time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
u=list(m.values())[-1]
print(len(u), len(u[0].DeflectedWs))
" 2>&1 | grep -E "read|load|^[0-9]|Maximum resident|Elapsed"
```

```
read 1.9324018955230713
load 14.88805603981018 3.095736
58 33481
b=z.read('Experiment2/20160914.mat'); print('read',time.time()-t)
m=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False); del b
print('load',time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:16.77
	Maximum resident set size (kbytes): 3095736
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import fsspec,zipfile,io,scipy.io as sio,numpy as np,collections,sys
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
names=[i.filename for i in z.infolist() if i.filename.endswith('.mat')]
for name in names:
    m=sio.loadmat(io.BytesIO(z.read(name)),squeeze_me=True,struct_as_record=False)
    key=[k for k in m if not k.startswith('__')][0]
    U=np.atleast_1d(m[key])
    u=U[0]
    T=len(u.DeflectedWs)
    same=all(len(v.DeflectedWs)==T and all(np.array_equal(np.atleast_1d(a),np.atleast_1d(b),equal_nan=True) for a,b in zip(v.DeflectedWs[:500],u.DeflectedWs[:500])) for v in U)
    nw=collections.Counter(np.size(d) if not (np.size(d)==1 and np.isnan(np.atleast_1d(d)[0]).any()) else 0 for d in u.DeflectedWs)
    info=f'{name} key={key} units={len(U)} trials={T} sameTrials={same} nWhiskers={dict(nw)}'
    if hasattr(u,'timeWs'):
        tw=collections.Counter(int(np.min(np.atleast_1d(t))) for t,d in zip(u.timeWs,u.DeflectedWs) if np.size(d)>0 and np.size(t)>0)
        info+=f' firstTime={dict(tw.most_common(5))}'
        shamt=[t for t,d in zip(u.timeWs,u.DeflectedWs) if np.size(d)==1 and np.isnan(np.atleast_1d(d).astype(float)).any()][:3]
        info+=f' shamTimeWs={[repr(s) for s in shamt]}'
    allsp=np.concatenate([np.atleast_2d(s)[:,0] if np.ndim(s)==2 else np.atleast_1d(s).astype(float) for s in u.spkTime if np.size(s)])
    info+=f' spk range {allsp.min():.1f}-{allsp.max():.1f}'
    print(info)
    print('   recNames',collections.Counter(v.recName for v in U), 'depths', [getattr(v,'recDepth',None) for v in U])
    if hasattr(u,'experiment'):
        e=u.experiment; print('   exp', e.Animal_ID, e.Recording_Date, e.Whiskers, 'tip',e.Tip_Depth, 'age',e.Age, [ (v.experiment.Animal_ID,v.experiment.Tip_Depth) for v in U][:3])
    sys.stdout.flush()
EOF
python survey.py 2>&1 | tee survey.txt
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/survey.py", line 15, in <module>
    tw=collections.Counter(int(np.min(np.atleast_1d(t))) for t,d in zip(u.timeWs,u.DeflectedWs) if np.size(d)>0 and np.size(t)>0)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/collections/__init__.py", line 614, in __init__
    self.update(iterable, **kwds)
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/collections/__init__.py", line 706, in update
    _count_elements(self, iterable)
    ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/survey.py", line 15, in <genexpr>
    tw=collections.Counter(int(np.min(np.atleast_1d(t))) for t,d in zip(u.timeWs,u.DeflectedWs) if np.size(d)>0 and np.size(t)>0)
                           ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: cannot convert float NaN to integer
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && sed -i 's/tw=collections.Counter(int(np.min(np.atleast_1d(t)))/tw=collections.Counter(float(np.min(np.atleast_1d(t).astype(float)))/' survey.py && python survey.py 2>&1 | tee survey.txt
```

```
Experiment1/20170515.mat key=UnitInfoExp1 units=34 trials=25999 sameTrials=False nWhiskers={2: 23529, 1: 2340, 0: 130} firstTime={150.0: 15613, 100.0: 3536, 125.0: 3397, 140.0: 3323, nan: 1} shamTimeWs=['nan', 'nan', 'nan'] spk range 0.2-498.8
   recNames Counter({'KJL_20170515_1439-1801_chn3_Param1.mat': 6, 'KJL_20170515_1902-2236_chn3_Param1.mat': 5, 'KJL_20170515_1902-2236_chn4_Param1.mat': 5, 'KJL_20170515_1439-1801_chn1_Param1.mat': 4, 'KJL_20170515_1902-2236_chn2_Param1.mat': 4, 'KJL_20170515_1439-1801_chn2_Param1.mat': 3, 'KJL_20170515_1902-2236_chn1_Param1.mat': 3, 'KJL_20170515_1902-2236_chn5_Param1.mat': 3, 'KJL_20170515_1439-1801_chn4_Param1.mat': 1}) depths [550, 550, 550, 550, 450, 450, 450, 350, 350, 350, 350, 350, 350, 250, 1048, 1048, 1048, 948, 948, 948, 948, 848, 848, 848, 848, 848, 748, 748, 748, 748, 748, 648, 648, 648]
Experiment1/20170605.mat key=UnitInfoExp1 units=28 trials=34995 sameTrials=False nWhiskers={2: 31672, 1: 3148, 0: 175} firstTime={150.0: 21218, 140.0: 4547, 125.0: 4541, 100.0: 4514, nan: 1} shamTimeWs=['nan', 'nan', 'nan'] spk range 0.0-498.9
   recNames Counter({'KJL_20170605_1908-2240_chn2_Param1.mat': 9, 'KJL_20170605_1313-1817_chn1_Param1.mat': 4, 'KJL_20170605_1313-1817_chn3_Param1.mat': 4, 'KJL_20170605_1908-2240_chn3_Param1.mat': 4, 'KJL_20170605_1908-2240_chn1_Param1.mat': 3, 'KJL_20170605_1313-1817_chn4_Param1.mat': 2, 'KJL_20170605_1908-2240_chn4_Param1.mat': 2}) depths [490, 490, 490, 490, 290, 290, 290, 290, 190, 190, 948, 948, 948, 848, 848, 848, 848, 848, 848, 848, 848, 848, 748, 748, 748, 748, 648, 648]
Experiment1/20170513.mat key=UnitInfoExp1 units=21 trials=24985 sameTrials=True nWhiskers={1: 2250, 2: 22610, 0: 125} firstTime={150.0: 15045, 125.0: 3302, 100.0: 3297, 140.0: 3216, nan: 1} shamTimeWs=['nan', 'nan', 'nan'] spk range 0.0-498.9
   recNames Counter({'KJL_20170513_1728-2053_chn1_Param1.mat': 6, 'KJL_20170513_1728-2053_chn2_Param1.mat': 6, 'KJL_20170513_1728-2053_chn3_Param1.mat': 6, 'KJL_20170513_1728-2
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec,zipfile,io,scipy.io as sio,numpy as np,collections
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
U=sio.loadmat(io.BytesIO(z.read('Experiment2/20160808.mat')),squeeze_me=True,struct_as_record=False)['UnitInfoExp2']
u=U[0]
k=0
for i in range(len(u.DeflectedWs)):
  if np.size(u.DeflectedWs[i])==3 and k<8: print(u.DeflectedWs[i],u.timeWs[i],u.directionWs[i]); k+=1
print('2-whisker examples'); k=0
for i in range(len(u.DeflectedWs)):
  if np.size(u.DeflectedWs[i])==2 and k<8: print(u.DeflectedWs[i],u.timeWs[i],u.directionWs[i]); k+=1
print('singles');k=0
for i in range(len(u.DeflectedWs)):
  if np.size(u.DeflectedWs[i])==1 and k<6: print(u.DeflectedWs[i],u.timeWs[i],u.directionWs[i]); k+=1
c=collections.Counter(tuple(sorted(np.atleast_1d(d).tolist())) for d in u.DeflectedWs if np.size(d)>=2)
print(sorted(c.items()))
"
```

```
[5 4 6] [150 122 171] [1 1 1]
[5 8 2] [150 131 143] [1 1 1]
[5 8 2] [150 170 130] [1 1 1]
[5 6 4] [150 142 186] [1 1 1]
[5 8 2] [150 200 193] [1 1 1]
[5 6 4] [150 187 153] [1 1 1]
[5 2 8] [150 170 146] [1 1 1]
[5 6 4] [150 148 154] [1 1 1]
2-whisker examples
[8 6] [150 198] [1 1]
[5 3] [150 152] [1 1]
[5 1] [150 141] [1 1]
[5 4] [150 181] [1 1]
[5 7] [150 154] [ 1 -1]
[8 4] [150 150] [ 1 -1]
[5 4] [150 161] [ 1 -1]
[5 6] [150 164] [ 1 -1]
singles
6 150 -1
1 150 1
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec,zipfile,io,scipy.io as sio,numpy as np,collections
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
for fn in ['Experiment3/20190123.mat','Experiment3/20190215.mat']:
  U=sio.loadmat(io.BytesIO(z.read(fn)),squeeze_me=True,struct_as_record=False)['UnitInfoExp3']
  print(fn)
  for u in U[:4]:
    sp=[np.atleast_2d(s) for s in u.spkTime]
    allt=np.concatenate([s[:,0] for s in sp if s.size]); idx=np.concatenate([s[:,1] for s in sp if s.size])
    tri=np.concatenate([np.full(len(s),i+1) for i,s in enumerate(sp) if s.size])
    print(' n',len(allt),'quantiles',np.percentile(allt,[0,1,50,99,99.9,100]).round(1),'col2==index',np.mean(idx==tri), 'shapes',collections.Counter(s.shape[1] if s.size else 0 for s in sp))
    h,_=np.histogram(allt,bins=np.arange(0,320,10)); print(' hist',h.tolist())
    # CW single (label 4)
    cw=[i for i,d in enumerate(u.DeflectedWs) if np.size(d)==1 and np.atleast_1d(d)[0]==4]
    h,_=np.histogram(np.concatenate([sp[i][:,0] for i in cw if sp[i].size]),bins=np.arange(0,320,10)); print(' CWhist',h.tolist())
    sham=[i for i,d in enumerate(u.DeflectedWs) if np.size(d)==1 and np.isnan(float(np.atleast_1d(d)[0]))]
    h,_=np.histogram(np.concatenate([sp[i][:,0] for i in sham if sp[i].size]),bins=np.arange(0,320,10)); print(' shamhist',h.tolist())
"
```

```
Experiment3/20190123.mat
 n 55490 quantiles [0.000000e+00 4.600000e+00 2.150000e+02 2.124695e+05 2.414759e+05
 2.452165e+05] col2==index 1.0 shapes Counter({2: 7902, 0: 216})
 hist [1206, 1192, 1499, 1680, 1581, 1517, 1170, 1067, 1144, 1074, 970, 956, 1098, 1131, 1342, 1361, 1468, 1596, 1463, 1322, 1273, 1212, 1105, 1097, 1098, 1108, 877, 930, 942, 938, 296]
 CWhist [13, 8, 6, 4, 8, 9, 7, 8, 5, 5, 10, 10, 5, 14, 11, 15, 12, 12, 10, 11, 3, 9, 14, 9, 12, 9, 6, 12, 9, 10, 0]
 shamhist [25, 27, 27, 21, 20, 25, 19, 17, 17, 23, 16, 19, 29, 25, 19, 22, 18, 30, 23, 17, 22, 16, 32, 13, 17, 25, 18, 14, 12, 15, 3]
 n 8157 quantiles [1.000000e-01 1.970000e+01 7.230000e+01 1.731907e+05 2.386494e+05
 2.439038e+05] col2==index 1.0 shapes Counter({0: 4969, 2: 3149})
 hist [41, 43, 96, 578, 1670, 1041, 536, 335, 778, 501, 249, 120, 84, 78, 72, 75, 68, 61, 67, 73, 61, 50, 54, 44, 50, 33, 32, 26, 38, 36, 10]
 CWhist [2, 0, 3, 26, 59, 33, 19, 6, 2, 0, 0, 1, 1, 2, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0]
 shamhist [1, 4, 4, 0, 2, 2, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 2, 1, 0, 0, 2, 1]
 n 5684 quantiles [1.000000e-01 6.400000e+00 1.801000e+02 2.029196e+05 2.245698e+05
 2.391696e+05] col2==index 1.0 shapes Counter({0: 5437, 2: 2681})
 hist [92, 91, 170, 376, 354, 246, 168, 197, 155, 127, 110, 104, 77, 68, 107, 122, 133, 144, 162, 137, 128, 107, 127, 97, 110, 96, 71, 68, 75, 78, 17]
 CWhist [0, 1, 2, 9, 7, 7, 0, 4, 0, 0, 1, 1, 1, 1, 0, 2, 3, 0, 0, 0, 0, 0, 3, 0, 1, 1, 0, 0, 1, 0, 0]
 shamhist [3, 1, 1, 1, 1, 2, 1, 3, 5, 2, 3, 3, 4, 0, 1, 1, 2, 0, 3, 2, 2, 0, 2, 0, 4, 1, 0, 1, 2, 2, 1]
 n 10654 quantiles [0.000000e+00 6.200000e+00 1.924000e+02 2.251906e+05 2.431919e+05
 2.449688e+05] col2==index 1.0 shapes Counter({2: 4059, 0: 4059})
 hist [175, 194, 374, 899, 759, 301, 204, 386, 299, 189, 119, 120, 119, 157, 182, 181, 214, 170, 228, 209, 213, 189, 191, 184, 194, 200, 141, 128, 178, 154, 58]
 CWhist [2, 3, 8, 7, 14, 4, 0, 0, 3, 3, 3, 0, 0, 2, 1, 0, 5, 3, 2, 2
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec,zipfile,io,scipy.io as sio,numpy as np,collections
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
U=sio.loadmat(io.BytesIO(z.read('Experiment3/20190129.mat')),squeeze_me=True,struct_as_record=False)['UnitInfoExp3']
bins=np.arange(0,200,5)
def ph(u,sel):
  s=[np.atleast_2d(u.spkTime[i])[:,0] for i in sel if np.size(u.spkTime[i])]
  return np.histogram(np.concatenate(s) if s else [],bins=bins)[0]
D=U[0].DeflectedWs; DT=U[0].DeltaT
def idx(f): return [i for i in range(len(D)) if f(np.atleast_1d(D[i]).astype(float),DT[i])]
groups={'CWsingle':idx(lambda d,t:len(d)==1 and d[0]==4),
'CWfirst_listed,+40':idx(lambda d,t:len(d)==2 and d[0]==4 and t==40),
'CWfirst_listed,-40':idx(lambda d,t:len(d)==2 and d[0]==4 and t==-40),
'CWsecond_listed,+40':idx(lambda d,t:len(d)==2 and d[1]==4 and t==40),
'CWsecond_listed,-40':idx(lambda d,t:len(d)==2 and d[1]==4 and t==-40),
'CW,0':idx(lambda d,t:len(d)==2 and 4 in d and t==0)}
for g,s in groups.items():
  tot=sum(ph(u,s) for u in U); print(g,len(s),(tot/len(s)).round(1).tolist())
print(collections.Counter((int(np.atleast_1d(d)[0]==4), DT[i]) for i,d in enumerate(D) if np.size(d)==2 and 4 in np.atleast_1d(d)))
"
```

```
CWsingle 112 [0.2, 0.4, 0.2, 0.4, 0.9, 1.5, 1.5, 1.9, 1.3, 1.1, 0.9, 1.0, 0.8, 0.7, 0.6, 0.4, 0.4, 0.3, 0.4, 0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.2, 0.2, 0.3, 0.3]
CWfirst_listed,+40 610 [0.2, 0.2, 0.2, 0.3, 0.8, 1.6, 1.6, 1.7, 1.5, 1.1, 1.0, 0.9, 0.7, 0.6, 0.6, 0.5, 0.4, 0.4, 0.3, 0.3, 0.2, 0.2, 0.2, 0.1, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.1, 0.2, 0.2, 0.2, 0.3, 0.2]
CWfirst_listed,-40 615 [0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.4, 0.5, 0.4, 0.4, 0.4, 0.3, 0.8, 1.4, 1.5, 1.7, 1.5, 1.1, 1.0, 0.9, 0.7, 0.7, 0.5, 0.5, 0.4, 0.3, 0.3, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2]
CWsecond_listed,+40 349 [0.2, 0.2, 0.2, 0.2, 0.3, 0.2, 0.3, 0.5, 0.6, 0.6, 0.6, 0.5, 1.0, 1.6, 1.6, 1.7, 1.5, 1.2, 0.9, 0.8, 0.7, 0.6, 0.5, 0.5, 0.3, 0.3, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.2, 0.2, 0.1, 0.1, 0.2, 0.2]
CWsecond_listed,-40 351 [0.2, 0.2, 0.2, 0.2, 0.9, 1.6, 1.5, 1.6, 1.4, 1.0, 0.9, 0.9, 0.6, 0.5, 0.5, 0.4, 0.5, 0.4, 0.4, 0.4, 0.3, 0.3, 0.3, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3]
CW,0 926 [0.2, 0.2, 0.2, 0.3, 0.8, 1.6, 1.5, 1.7, 1.4, 1.1, 1.0, 0.8, 0.7, 0.6, 0.5, 0.4, 0.4, 0.3, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.3, 0.2, 0.3]
Counter({(1, np.float64(-40.0)): 615, (1, np.float64(40.0)): 610, (1, np.float64(0.0)): 577, (0, np.float64(-40.0)): 351, (0, np.float64(0.0)): 349, (0, np.float64(40.0)): 349})
Shell cwd was reset to
```

**Agent calls Bash**

```bash
sed -n 30,130p paper/10.1038-s41593-019-0448-6.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "entries/laboy-juarez-2019/lj2019.py",
 "content": "\"\"\"Loading and measures for CRCNS ssc-9 (Laboy-Juarez, Langberg, Ahn & Feldman 2019).\n\nThe data set is one zip, ``ssc-9/live/data.zip``, in the public S3 bucket ``crcnsarchive``.\nIt is opened in place over range requests (fsspec and zipfile, docs/archives.md, \"CRCNS\"); each\nMATLAB file is read into memory, reduced to spike counts per trial, and dropped.\n\nWhere each parameter comes from:\n\n- Response window, 0 to 125 ms after the onset of the first deflected whisker: claims file,\n  \"Common method\" (Methods, \"Analysis of neuronal data\" and \"dt smoothing\").\n- Whisker labels: the data descriptor (paper/ssc-9.data-description.txt and its PDF figure).\n  Experiments 1 and 2 use the grid 1 4 7 / 2 5 8 / 3 6 9 (columns caudal to rostral, rows\n  dorsal to ventral), CW = 5; experiment 3 uses 6 7 8 / 3 4 5 / 1 2 9, CW = 4.\n- dt sign: negative dt means the SW leads the CW (Fig. 1c legend, \"negative dt (SW precedes\n  CW)\"), so dt = t_SW - t_CW.\n- Experiment 3 epochs have no deflection times. DeltaT is the time of the second whisker in\n  DeflectedWs minus that of the first, and epoch time 0 is the first deflection in time; this is\n  shown from the latency of the CW response in the notebook's data check (a finding, the data\n  descriptor does not say it).\n- Poisson likelihood ratio test of responsiveness across the nine whiskers and sham: Methods,\n  \"Analysis of neuronal data\".\n- Lifetime sparseness: claims file header, Vinje and Gallant (ref. 28).\n- dt smoothing: Methods, \"dt smoothing\" (claims file, common method). Kernels with SD 0.5 to 30 ms\n  in 0.2 ms steps, tenfold cross-validation repeated 50 times.\n- Combination selectivity shuffle: Methods, \"Combination selectivity\" (5000 shuffles,\n  Mahalanobis distance, FDR control at 0.05).\n- Decoders: Methods, \"Neural decoders\".\n\"\"\"\n\nimport io\nimport zipfile\n\nimport fsspec\nimport numpy as np\nimport pandas as pd\nimport scipy.io as sio\nfrom scipy import stats\n\nURL = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip\"\nWINDOW = 125.0  # ms, Methods, \"Analysis of neuronal data\"\n\n# Positions (row, column) of each label: row 0 dorsal to 2 ventral, column 0 caudal to 2 rostral.\nPOS12 = {1: (0, 0), 2: (1, 0), 3: (2, 0), 4: (0, 1), 5: (1, 1), 6: (2, 1), 7: (0, 2), 8: (1, 2), 9: (2, 2)}\nPOS3 = {6: (0, 0), 3: (1, 0), 1: (2, 0), 7: (0, 1), 4: (1, 1), 2: (2, 1), 8: (0, 2), 5: (1, 2), 9: (2, 2)}\nCW12, CW3 = 5, 4\n# Face position names, by (row offset, column offset) from the CW.\nPOSNAME = {(0, 1): \"rostral within-row\", (0, -1): \"caudal within-row\",\n           (-1, 0): \"dorsal same-arc\", (1, 0): \"ventral same-arc\",\n           (-1, 1): \"dorsal rostral\", (-1, -1): \"dorsal caudal\",\n           (1, 1): \"ventral rostral\", (1, -1): \"ventral caudal\", (0, 0): \"CW\"}\n# Layer bounds in um below pia, Methods, \"Surgical preparation\".\nLAYERS = [(\"L2/3\", 100, 417), (\"L4\", 418, 587), (\"L5\", 588, 889), (\"L6\", 890, 1154)]\n\n\ndef open_zip():\n    return zipfile.ZipFile(fsspec.open(URL, block_size=2 ** 20).open())\n\n\ndef mat_names(z, experiment):\n    return sorted(i.filename for i in z.infolist()\n                  if i.filename.startswith(f\"Experiment{experiment}/\") and i.filename.endswith(\".mat\"))\n\n\ndef relpos(label, exp):\n    pos, cw = (POS3, CW3) if exp == 3 else (POS12, CW12)\n    r, c = pos[label]\n    r0, c0 = pos[cw]\n    return (r - r0, c - c0)\n\n\ndef layer_of(depth):\n    for name, lo, hi in LAYERS:\n        if lo <= depth <= hi:\n            return name\n    return \"outside\"\n\n\ndef _vec(x):\n    return np.atleast_1d(np.asarray(x, dtype=float)).ravel()\n\n\ndef _trial_table_12(u):\n    \"\"\"Trial table of experiments 1 and 2 from one unit's struct.\"\"\"\n    rows = []\n    for d, t, r in zip(u.DeflectedWs, u.timeWs, u.directionWs):\n        d, t, r = _vec(d), _vec(t), _vec(r)\n        if d.size == 1 and np.isnan(d[0]):\n            rows.append((\"sham\", 0, 0, np.nan, 0, 0, np.nan))\n            continue\n        onset = np.nanmin(t)\n        if d.size == 1:\n            rows.append((\"single\", int(d[0]), 0, 0.0, int(r[0]), 0, onset))\n        elif d.size == 2:\n            if CW12 in d:\n                i = int(np.where(d == CW12)[0][0])\n                j = 1 - i\n                # a = CW, b = SW, dt = t_SW - t_CW\n                rows.append((\"cwsw\", CW12, int(d[j]), t[j] - t[i], int(r[i]), int(r[j]), onset))\n            else:\n                i, j = (0, 1) if d[0] < d[1] else (1, 0)\n                rows.append((\"swsw\", int(d[i]), int(d[j]), t[j] - t[i], int(r[i]), int(r[j]), onset))\n        else:\n            rows.append((\"triple\", 0, 0, np.nan, 0, 0, onset))\n    return pd.DataFrame(rows, columns=[\"kind\", \"a\", \"b\", \"dt\", \"da\", \"db\", \"onset\"])\n\n\ndef _trial_table_3(u):\n    rows = []\n    for d, dt in zip(u.DeflectedWs, u.DeltaT):\n        d = _vec(d)\n        if d.size == 1 and np.isnan(d[0]):\n            rows.append((\"sham\", 0, 0, np.nan, 1, 1, 0.0))\n        elif d.size == 1:\n            rows.append((\"single\", int(d[0]), 0, 0.0, 1, 0, 0.0))\n        else:\n            # DeltaT = t(second listed) - t(first listed) (shown in the data check).\n            t = np.array([0.0, dt])\n            if CW3 in d:\n                i = int(np.where(d == CW3)[0][0])\n                j = 1 - i\n                rows.append((\"cwsw\", CW3, int(d[j]), t[j] - t[i], 1, 1, 0.0))\n            else:\n                i, j = (0, 1) if d[0] < d[1] else (1, 0)\n                rows.append((\"swsw\", int(d[i]), int(d[j]), t[j] - t[i], 1, 1, 0.0))\n    return pd.DataFrame(rows, columns=[\"kind\", \"a\", \"b\", \"dt\", \"da\", \"db\", \"onset\"])\n\n\ndef _spikes(u, exp):\n    \"\"\"All spike times of a unit with their trial index.\"\"\"\n    cells = [np.atleast_2d(np.asarray(s, dtype=float))[:, 0] if exp == 3 and np.size(s)\n             else _vec(s) if np.size(s) else np.zeros(0) for s in u.spkTime]\n    n = np.fromiter((len(c) for c in cells), int, len(cells))\n    t = np.concatenate(cells) if n.sum() else np.zeros(0)\n    tri = np.repeat(np.arange(len(cells)), n)\n    return t, tri\n\n\ndef load_experiment(z, exp, files=None, log=print):\n    \"\"\"Return (units, tables, info).\n\n    units: DataFrame, one row per unit (file, recording, depth, waveform hash, spike hash).\n    tables: dict recording -> trial table, with a column per unit of spike counts in the response\n    window (``c<k>``), counts over the whole trial (``w<k>``), counts in the 100 ms before onset\n    (``p<k>``), and 10 ms bins from -50 to +200 ms around onset for single and sham trials.\n    \"\"\"\n    key = f\"UnitInfoExp{exp}\"\n    units, tables, extras = [], {}, {}\n    for name in files or mat_names(z, exp):\n        U = np.atleast_1d(sio.loadmat(io.BytesIO(z.read(name)), squeeze_me=True,\n                                      struct_as_record=False)[key])\n        for u in U:\n            rec = u.recName.rsplit(\"_chn\", 1)[0].rsplit(\"_ch\", 1)[0] if exp != 3 else u.recName.rsplit(\"_chn\", 1)[0]\n            dhash = hash(tuple(_vec(d).tobytes() for d in u.DeflectedWs[:2000]))\n            if rec not in tables:\n                tab = _trial_table_3(u) if exp == 3 else _trial_table_12(u)\n                tab.attrs[\"dhash\"] = dhash\n                tables[rec] = tab\n                extras[rec] = {}\n            tab = tables[rec]\n            assert tab.attrs[\"dhash\"] == dhash and len(tab) == len(u.DeflectedWs), (name, rec)\n            k = len(units)\n            t, tri = _spikes(u, exp)\n            onset = tab[\"onset\"].to_numpy()\n            on = onset[tri]\n            # Sham trials have no onset: reading (a) of O1 places the window where single\n            # deflections occur in that recording's trials.\n            sham_on = np.nanmedian(tab.loc[tab.kind == \"single\", \"onset\"]) if exp != 3 else 0.0\n            on = np.where(np.isnan(on), sham_on, on)\n            rel = t - on\n            ntr = len(tab)\n            c = np.bincount(tri[(rel >= 0) & (rel < WINDOW)], minlength=ntr)\n            p = np.bincount(tri[(rel >= -100) & (rel < 0)], minlength=ntr)\n            maxt = 600.0 if exp != 3 else 300.0\n            w = np.bincount(tri[(t >= 0) & (t < maxt)], minlength=ntr)\n            sel = tab.kind.isin([\"single\", \"sham\"]).to_numpy()\n            keep = sel[tri] & (rel >= -50) & (rel < 200)\n            psth = np.zeros((ntr, 25), np.int16)\n            np.add.at(psth, (tri[keep], ((rel[keep] + 50) // 10).astype(int)), 1)\n            extras[rec][f\"c{k}\"] = c.astype(np.int16)\n            extras[rec][f\"p{k}\"] = p.astype(np.int16)\n            extras[rec][f\"w{k}\"] = w.astype(np.int16)\n            extras[rec][f\"h{k}\"] = psth[sel]\n            if exp == 3:\n                e = u.experiment\n                depth, animal, whiskers = float(e.Tip_Depth), str(e.Animal_ID), str(e.Whiskers)\n            else:\n                depth, animal, whiskers = float(u.recDepth), name.split(\"/\")[1][:8], \"\"\n            units.append(dict(unit=k, file=name, recording=rec, depth=depth, animal=animal,\n                              whiskers=whiskers, n_spikes=len(t),\n                              n_out=int(np.sum((t < 0) | (t > maxt))),\n                              max_t=float(t.max()) if len(t) else np.nan,\n                              spike_hash=hash(np.round(t, 3).tobytes())))\n        del U\n        log(f\"{name}: {sum(1 for x in units if x['file'] == name)} units\")\n    for rec, tab in tables.items():\n        ex = extras[rec]\n        cols = {key_: v for key_, v in ex.items() if not key_.startswith(\"h\")}\n        tables[rec] = pd.concat([tab, pd.DataFrame(cols)], axis=1)\n        tables[rec].attrs[\"psth\"] = {key_: v for key_, v in ex.items() if key_.startswith(\"h\")}\n        tables[rec].attrs[\"psth_rows\"] = tab.kind.isin([\"single\", \"sham\"]).to_numpy()\n    return pd.DataFrame(units), tables\n\n\n# ---------------------------------------------------------------- measures\n\ndef sparseness(r, axis=-1):\n    \"\"\"Lifetime sparseness (Vinje and Gallant 2000), the claims file's reading of the Methods.\"\"\"\n    r = np.asarray(r, float)\n    n = r.shape[axis]\n    m1 = r.mean(axis=axis)\n    m2 = (r ** 2).mean(axis=axis)\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        s = (1 - m1 ** 2 / m2) / (1 - 1 / n)\n    return np.where(m2 > 0, s, 0.0)\n\n\ndef poisson_lrt(counts, groups):\n    \"\"\"Likelihood ratio test that a Poisson rate is equal across groups (Methods).\"\"\"\n    counts = np.asarray(counts, float)\n    labels, g = np.unique(groups, return_inverse=True)\n    S = np.bincount(g, weights=counts)\n    n = np.bincount(g)\n    lam0 = counts.sum() / n.sum()\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        term = np.where(S > 0, S * np.log(S / (n * lam0)), 0.0)\n    G = 2 * term.sum()\n    return G, stats.chi2.sf(G, len(labels) - 1)\n\n\ndef gaussian_kernels(n, sds):\n    \"\"\"Row-normalised Gaussian smoothing matrices (n x n) for each SD (renormalised at edges).\"\"\"\n    x = np.arange(n)\n    d = x[:, None] - x[None, :]\n    K = np.exp(-0.5 * (d[None] / np.asarray(sds)[:, None, None]) ** 2)\n    return K / K.sum(axis=2, keepdims=True)\n\n\ndef gaussian_kernels_zeropad(n, sds):\n    \"\"\"As gaussian_kernels but with zero padding at the edges (kernel normalised on the full line).\"\"\"\n    x = np.arange(n)\n    d = x[:, None] - x[None, :]\n    sds = np.asarray(sds)[:, None, None]\n    K = np.exp(-0.5 * (d[None] / sds) ** 2)\n    full = np.sqrt(2 * np.pi) * sds  # integral; sums over the infinite integer line are close\n    return K / full\n\n\nSDS = np.round(np.arange(0.5, 30.0 + 1e-9, 0.2), 1)  # Methods, \"dt smoothing\"\n\n\ndef dt_smooth(y, dti, ndt, rng, kernels, reps=50, folds=10):\n    \"\"\"Cross-validated Gaussian smoothing of a dt tuning curve (Methods, \"dt smoothing\").\n\n    y: single-trial counts; dti: index of each trial's dt on the 1 ms grid (0..ndt-1).\n    Returns (curve, sd, status), status 'modulated', 'monotonic' (likelihood rises with SD up to\n    the largest) or 'unsmoothed' (unsmoothed likelihood beats every smoothed one); the curve is the\n    mean over dt for the last two.\n\n    A held-out dt with no training trials takes the unit's training mean in the unsmoothed curve\n    (claims file, methods-dt-modulation reading (a)); zero rates are floored at 1e-3 spikes so\n    the log likelihood stays finite (a standard choice; it affects only zero-count bins).\n    \"\"\"\n    y = np.asarray(y, float)\n    n = len(y)\n    ll_raw = 0.0\n    ll_sm = np.zeros(kernels.shape[0])\n    for _ in range(reps):\n        perm = rng.permutation(n)\n        fold = np.empty(n, int)\n        fold[perm] = np.arange(n) % folds\n        for f in range(folds):\n            tr = fold != f\n            te = ~tr\n            s = np.bincount(dti[tr], weights=y[tr], minlength=ndt)\n            c = np.bincount(dti[tr], minlength=ndt)\n            mtr = y[tr].mean()\n            raw = np.where(c > 0, s / np.maximum(c, 1), mtr)\n            sm = kernels @ raw  # (K, ndt)\n            yt, dt_t = y[te], dti[te]\n            lam = np.maximum(raw[dt_t], 1e-3)\n            ll_raw += np.sum(yt * np.log(lam) - lam)\n            lam = np.maximum(sm[:, dt_t], 1e-3)\n            ll_sm += np.sum(yt * np.log(lam) - lam, axis=1)\n    s = np.bincount(dti, weights=y, minlength=ndt)\n    c = np.bincount(dti, minlength=ndt)\n    raw_all = np.where(c > 0, s / np.maximum(c, 1), y.mean())\n    best = int(np.argmax(ll_sm))\n    if best == len(ll_sm) - 1 and np.all(np.diff(ll_sm) >= 0):\n        return np.full(ndt, y.mean()), np.inf, \"monotonic\"\n    if ll_raw > ll_sm.max():\n        return np.full(ndt, y.mean()), np.nan, \"unsmoothed\"\n    return kernels[best] @ raw_all, SDS[best], \"modulated\"\n\n\ndef mahalanobis_p(measured, shuffled):\n    \"\"\"P-value of the measured trace's Mahalanobis distance from the shuffled mean (Methods).\"\"\"\n    mu = shuffled.mean(axis=0)\n    C = np.cov(shuffled, rowvar=False)\n    P = np.linalg.pinv(C, rcond=1e-10, hermitian=True)\n    d = shuffled - mu\n    ds = np.einsum(\"ij,jk,ik->i\", d, P, d)\n    dm = (measured - mu) @ P @ (measured - mu)\n    return (1 + np.sum(ds >= dm)) / (1 + len(ds)), dm\n\n\ndef bh(p, q=0.05):\n    \"\"\"Benjamini-Hochberg false discovery rate control; returns the rejected mask.\"\"\"\n    p = np.asarray(p)\n    n = len(p)\n    o = np.argsort(p)\n    thr = q * np.arange(1, n + 1) / n\n    ok = p[o] <= thr\n    k = np.max(np.where(ok)[0]) + 1 if ok.any() else 0\n    rej = np.zeros(n, bool)\n    rej[o[:k]] = True\n    return rej\n\n\ndef logistic_prob_table(x_train, y_train, ncls, maxcount, max_iter=1000):\n    \"\"\"One-versus-all logistic classifiers on one feature (spike count), Methods, \"Neural decoders\".\n\n    Returns P[count, class], the probability of each class for each count 0..maxcount; with one\n    integer feature the classifier is a function of the count alone.\n    \"\"\"\n    from sklearn.linear_model import LogisticRegression\n\n    grid = np.arange(maxcount + 1, dtype=float)[:, None]\n    P = np.zeros((maxcount + 1, ncls))\n    for k in range(ncls):\n        yk = (y_train == k).astype(int)\n        if yk.min() == yk.max():\n            P[:, k] = yk.mean()\n            continue\n        m = LogisticRegression(max_iter=max_iter, C=1e6)\n        m.fit(x_train[:, None].astype(float), yk)\n        P[:, k] = m.predict_proba(grid)[:, 1]\n    return P\n\n\ndef heldout_probs(x, y, ncls, rng, folds=10):\n    \"\"\"Probabilities for each trial from the classifier fitted on the other folds (tenfold CV).\"\"\"\n    x = np.asarray(x, int)\n    maxc = int(x.max()) if len(x) else 0\n    out = np.zeros((len(x), ncls))\n    perm = rng.permutation(len(x))\n    fold = np.empty(len(x), int)\n    fold[perm] = np.arange(len(x)) % folds\n    for f in range(folds):\n        tr = fold != f\n        P = logistic_prob_table(x[tr], y[tr], ncls, maxc)\n        out[~tr] = P[x[~tr]]\n    return out\n\n\ndef ensemble_accuracy(unit_probs, unit_labels, N, n_ens, rng, ncls, per_class=False):\n    \"\"\"Population decoding (Methods): units sampled with replacement, summed probabilities.\n\n    unit_probs[i]: held-out probability rows of unit i; unit_labels[i]: their true classes.\n    Each ensemble tests one held-out trial per unit per class, drawn independently for each unit\n    (claims file, O6).\n    \"\"\"\n    idx_by = [[np.where(l == k)[0] for k in range(ncls)] for l in unit_labels]\n    nu = len(unit_probs)\n    correct = np.zeros((n_ens, ncls))\n    for e in range(n_ens):\n        units = rng.integers(0, nu, N)\n        tot = np.zeros((ncls, ncls))\n        for u in units:\n            for k in range(ncls):\n                ii = idx_by[u][k]\n                if len(ii):\n                    tot[k] += unit_probs[u][ii[rng.integers(len(ii))]]\n        correct[e] = np.argmax(tot, axis=1) == np.arange(ncls)\n    return correct if per_class else correct.mean(axis=1)\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > load_all.py <<'EOF'
import sys, time, pickle, resource
sys.path.insert(0,'entries/laboy-juarez-2019')
import lj2019 as L
z=L.open_zip()
out={}
for exp in [1,3,2]:
    t=time.time()
    out[exp]=L.load_experiment(z,exp)
    print(exp,'time',time.time()-t,'maxrss GB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,flush=True)
pickle.dump(out,open('data.pkl','wb'))
EOF
python load_all.py 2>&1 | tail -30
```

```
Experiment1/20170510.mat: 38 units
Experiment1/20170513.mat: 21 units
Experiment1/20170515.mat: 34 units
Experiment1/20170605.mat: 28 units
Experiment1/20170621.mat: 39 units
1 time 35.04612755775452 maxrss GB 1.766508
Experiment3/20181114.mat: 14 units
Experiment3/20190123.mat: 11 units
Experiment3/20190124.mat: 13 units
Experiment3/20190128.mat: 9 units
Experiment3/20190129.mat: 20 units
Experiment3/20190215.mat: 14 units
3 time 5.597563743591309 maxrss GB 1.766508
Experiment2/20160225.mat: 8 units
Experiment2/20160316.mat: 2 units
Experiment2/20160325.mat: 14 units
Experiment2/20160406.mat: 21 units
Experiment2/20160504.mat: 34 units
Experiment2/20160506.mat: 4 units
Traceback (most recent call last):
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec,zipfile,io,scipy.io as sio,numpy as np
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
U=sio.loadmat(io.BytesIO(z.read('Experiment2/20160803.mat')),squeeze_me=True,struct_as_record=False)['UnitInfoExp2']
ref={}
for u in U:
  d=[np.atleast_1d(np.asarray(x,float)) for x in u.DeflectedWs]
  t=[np.atleast_1d(np.asarray(x,float)) for x in u.timeWs]
  h=hash(tuple(x.tobytes() for x in d)); ht=hash(tuple(x.tobytes() for x in t))
  print(u.recName,len(d),h%10000,ht%10000)
"
```

```
KJL_20160803_1803-2527_chn1_Param1.mat 43486 8199 3159
KJL_20160803_1803-2527_chn1_Param1.mat 43486 8199 3159
KJL_20160803_1803-2527_chn1_Param1.mat 43486 8199 3159
KJL_20160803_1803-2527_chn1_Param1.mat 43486 8199 3159
KJL_20160803_1803-2527_chn1_Param1.mat 43486 8199 3159
KJL_20160803_1803-2527_chn2_Param1.mat 43486 8199 3159
KJL_20160803_1803-2527_chn2_Param1.mat 43486 8199 3159
KJL_20160803_1803-2527_chn2_Param1.mat 43486 8199 3159
KJL_20160803_1803-2527_chn2_Param1.mat 43486 8199 3159
KJL_20160803_1803-2527_chn2_Param1.mat 43486 8199 3159
KJL_20160803_1803-2527_chn2_Param1.mat 43486 8199 3159
KJL_20160803_1803-2527_chn3_Param1.mat 25177 8983 3687
KJL_20160803_1803-2527_chn3_Param1.mat 25177 8983 3687
KJL_20160803_1803-2527_chn3_Param1.mat 25177 8983 3687
KJL_20160803_1803-2527_chn3_Param1.mat 25177 8983 3687
KJL_20160803_1803-2527_chn4_Param1.mat 43486 8199 3159
KJL_20160803_1803-2527_chn4_Param1.mat 43486 8199 3159
KJL_20160803_2641-2952_chn1_Param1.mat 25177 8983 3687
KJL_20160803_2641-2952_chn1_Param1.mat 25177 8983 3687
KJL_20160803_2641-2952_chn1_Param1.mat 25177 8983 3687
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019 && python - <<'EOF'
s=open('lj2019.py').read()
old='''            rec = u.recName.rsplit("_chn", 1)[0].rsplit("_ch", 1)[0] if exp != 3 else u.recName.rsplit("_chn", 1)[0]
            dhash = hash(tuple(_vec(d).tobytes() for d in u.DeflectedWs[:2000]))
            if rec not in tables:'''
new='''            # Units are grouped by their trial sequence (stimuli and their times), not by
            # recName: in 20160803 the recName of some units names another recording than the
            # one whose trials they carry (reported in the data check).
            dhash = hash(tuple(_vec(d).tobytes() for d in u.DeflectedWs)
                         + tuple(_vec(d).tobytes() for d in (u.DeltaT if exp == 3 else u.timeWs)))
            rec = f"{name.split('/')[1][:-4]}:{abs(dhash) % 10 ** 6:06d}"
            if rec not in tables:'''
assert old in s
s=s.replace(old,new)
s=s.replace('''            units.append(dict(unit=k, file=name, recording=rec, depth=depth,''','''            units.append(dict(unit=k, file=name, recording=rec, recName=str(u.recName), depth=depth,''')
open('lj2019.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python load_all.py 2>&1 | grep -E "time|Error|error"
```

```
1 time 42.00607657432556 maxrss GB 1.760468
3 time 6.98038649559021 maxrss GB 1.760468
2 time 94.74778580665588 maxrss GB 3.50282
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && python -c "
import pickle,numpy as np,pandas as pd,collections
D=pickle.load(open('data.pkl','rb'))
for e in [1,2,3]:
  U,T=D[e]
  print('EXP',e,len(U),'units',len(T),'recordings')
  print(U.groupby('file').recording.nunique().to_dict())
  # recName vs recording mismatch
  g=U.groupby('recording').recName.apply(lambda s: sorted(set(x.rsplit('_ch',1)[0] for x in s)))
  print({k:v for k,v in g.items() if len(v)>1})
  print('dup spike hashes', U.spike_hash.duplicated().sum(), 'out-of-range spikes', U.n_out.sum(), 'of', U.n_spikes.sum())
  for r,t in list(T.items())[:1]:
    print(t.kind.value_counts().to_dict())
    c=t[t.kind=='cwsw']; print('cwsw dt range',c.dt.min(),c.dt.max(),c.dt.nunique(), 'dirs', collections.Counter(zip(c.da,c.db)))
    s=t[t.kind=='swsw']; print('swsw pairs',sorted(set(zip(s.a,s.b))), 'dirs', collections.Counter(zip(s.da,s.db)))
    print('single dirs',collections.Counter(zip(t[t.kind=='single'].a,t[t.kind=='single'].da)))
"
```

```
Thu Nov 12 17:12:54 UTC 2026
EXP 1 160 units 8 recordings
{'Experiment1/20170510.mat': 2, 'Experiment1/20170513.mat': 1, 'Experiment1/20170515.mat': 2, 'Experiment1/20170605.mat': 2, 'Experiment1/20170621.mat': 1}
{}
dup spike hashes 0 out-of-range spikes 0 of 3784220
{'swsw': 19311, 'cwsw': 5672, 'single': 2485, 'sham': 138}
cwsw dt range -50.0 50.0 7 dirs Counter({(1, 1): 4964, (1, -1): 708})
swsw pairs [(1, 2), (1, 3), (1, 4), (1, 6), (1, 7), (1, 8), (1, 9), (2, 3), (2, 4), (2, 6), (2, 7), (2, 8), (2, 9), (3, 4), (3, 6), (3, 7), (3, 8), (3, 9), (4, 6), (4, 7), (4, 8), (4, 9), (6, 7), (6, 8), (6, 9), (7, 8), (7, 9), (8, 9)] dirs Counter({(1, 1): 14548, (1, -1): 2733, (-1, 1): 2030})
single dirs Counter({(5, -1): 139, (1, 1): 138, (4, -1): 138, (7, 1): 138, (9, -1): 138, (2, -1): 138, (3, -1): 138, (1, -1): 138, (3, 1): 138, (4, 1): 138, (8, -1): 138, (5, 1): 138, (6, 1): 138, (9, 1): 138, (6, -1): 138, (7, -1): 138, (2, 1): 138, (8, 1): 138})
EXP 2 247 units 16 recordings
{'Experiment2/20160225.mat': 1, 'Experiment2/20160316.mat': 1, 'Experiment2/20160325.mat': 1, 'Experiment2/20160406.mat': 1, 'Experiment2/20160504.mat': 2, 'Experiment2/20160506.mat': 1, 'Experiment2/20160803.mat': 2, 'Experiment2/20160808.mat': 1, 'Experiment2/20160817.mat': 1, 'Experiment2/20160829.mat': 1, 'Experiment2/20160909.mat': 2, 'Experiment2/20160914.mat': 2}
{'20160803:002860': ['KJL_20160803_1803-2527', 'KJL_20160803_2641-2952'], '20160909:042098': ['KJL_20160909_1747-2222', 'KJL_20160909_2358-3005']}
dup spike hashes 1 out-of-range spikes 0 of 11181625
{'cwsw': 12837, 'swsw': 8595, 'single': 2926}
cwsw dt range -50.0 50.0 101 dirs Counter({(1, 1): 6366, (1, -1): 5369, (-1, 1): 1102})
swsw pairs [(4, 8), (6, 8), (7, 8), (8, 9)] dirs Counter({(1, 1): 4374, (-1, 1): 3122, (1, -1): 1099})
single dirs Counter({(2, 1): 164, (2, -1): 164, (1, -1): 163, (9, 1): 163, (3, 1): 163, (7, -1): 163, (8, 1): 163, (6, 1): 163, (5, 1): 163, (7, 1): 162, (4, -1): 162, (9, -1): 162, (3, -1): 162, (5, -
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pickle,numpy as np,pandas as pd,collections
D=pickle.load(open('data.pkl','rb'))
U,T=D[3]
print(U[['file','n_spikes','n_out','max_t']].groupby('file').sum())
U,T=D[2]
d=U[U.spike_hash.duplicated(keep=False)]; print(d[['file','recName','depth','n_spikes']])
for r,t in T.items():
  c=t[t.kind=='cwsw']; print(r, len(t), dict(t.kind.value_counts()), dict(collections.Counter(zip(c.da,c.db))), 'n dt',c.dt.nunique())
U,T=D[1]
for r,t in T.items():
  c=t[t.kind=='cwsw']; print(r, len(t), dict(t.kind.value_counts()), dict(collections.Counter(zip(c.da,c.db))))
"
```

```
n_spikes   n_out         max_t
file                                                    
Experiment3/20181114.mat    133981   35486  2.435481e+05
Experiment3/20190123.mat    149165   47397  2.686573e+06
Experiment3/20190124.mat    256731   83513  1.744411e+06
Experiment3/20190128.mat     70879   22392  6.238113e+05
Experiment3/20190129.mat    374088  130064  3.601248e+05
Experiment3/20190215.mat    341751  114210  5.930644e+06
                         file  ...  n_spikes
178  Experiment2/20160909.mat  ...     20654
179  Experiment2/20160909.mat  ...     20654

[2 rows x 4 columns]
20160225:760476 24358 {'cwsw': np.int64(12837), 'swsw': np.int64(8595), 'single': np.int64(2926)} {(1, -1): 5369, (1, 1): 6366, (-1, 1): 1102} n dt 101
20160316:665184 29924 {'cwsw': np.int64(14860), 'swsw': np.int64(11474), 'single': np.int64(3590)} {(1, 1): 7482, (-1, 1): 849, (1, -1): 6529} n dt 101
20160325:517202 40500 {'triple': np.int64(18000), 'cwsw': np.int64(12085), 'swsw': np.int64(5915), 'single': np.int64(4050), 'sham': np.int64(450)} {(1, -1): 5889, (1, 1): 6130, (-1, 1): 66} n dt 101
20160406:140977 46747 {'triple': np.int64(20623), 'cwsw': np.int64(13739), 'swsw': np.int64(6885), 'single': np.int64(4950), 'sham': np.int64(550)} {(1, -1): 6926, (1, 1): 6813} n dt 101
20160504:193032 42494 {'cwsw': np.int64(25078), 'swsw': np.int64(12668), 'single': np.int64(4498), 'sham': np.int64(250)} {(1, 1): 12591, (1, -1): 12487} n dt 101
20160504:781711 33996 {'cwsw': np.int64(20144), 'swsw': np.int64(10053), 'single': np.int64(3599), 'sham': np.int64(200)} {(1, -1): 9968, (1, 1): 10176} n dt 101
20160506:869356 39961 {'cwsw': np.int64(23620), 'swsw': np.int64(11872), 'single': np.int64(4234), 'sham': np.int64(235)} {(1, -1): 11875, (1, 1): 11745} n dt 101
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import fsspec,zipfile,io,scipy.io as sio,numpy as np
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
U=sio.loadmat(io.BytesIO(z.read('Experiment3/20190128.mat')),squeeze_me=True,struct_as_record=False)['UnitInfoExp3']
u=U[0]
big=[(i,np.atleast_2d(s)[:,0]) for i,s in enumerate(u.spkTime) if np.size(s)]
nb=[(i,x[x>300]) for i,x in big if (x>300).any()]
print(len(big),len(nb))
for i,x in nb[:15]: print(i, x[:6].round(1), len(x), 'within', np.sum(np.atleast_2d(u.spkTime[i])[:,0]<=300))
"
```

```
2372 339
289 [425.2] 1 within 0
553 [2778.6 2779.9 2783.2 2785.7 2789.1 2790. ] 7 within 0
1180 [3653.9] 1 within 0
1181 [5874.6] 1 within 0
1241 [1741.8] 1 within 0
1502 [9899.3] 1 within 0
1516 [345. 666.] 2 within 0
1606 [1546.7 7545.3] 2 within 0
1977 [342.6] 1 within 0
1980 [2572.1] 1 within 0
2076 [2431.  2487.4] 2 within 0
2105 [925.] 1 within 0
2289 [8896.6] 1 within 0
2437 [707.1] 1 within 0
2470 [2332.5 6520.5] 2 within 0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019 && python - <<'EOF'
s=open('lj2019.py').read()
old='''            extras[rec][f"w{k}"] = w.astype(np.int16)'''
new='''            extras[rec][f"w{k}"] = w.astype(np.int16)
            # Spikes after the end of the epoch (experiment 3 epochs are about 300 ms long).
            extras[rec][f"o{k}"] = np.bincount(tri[t >= maxt], minlength=ntr).astype(np.int32)'''
assert old in s; s=s.replace(old,new)
open('lj2019.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python load_all.py 2>&1 | grep -E "time|Error|error"
```

```
1 time 40.89404821395874 maxrss GB 1.773192
3 time 6.6823365688323975 maxrss GB 1.773192
2 time 94.93823170661926 maxrss GB 3.553944
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n -i -E "Supplementary Fig(ure)? 1|ranked|Fig. 1g|lifetime sparseness of|z-scored" paper/10.1038-s41593-019-0448-6.txt | head -20; sed -n 280,312p paper/10.1038-s41593-019-0448-6.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/nb && cat > $TMPDIR/nb/build.py <<'EOF'
"""Build the notebook from cell files: '# %% tags' code cells, '# %% [markdown]' markdown cells."""
import sys, re, nbformat
src = "".join(open(f).read() for f in sys.argv[2:])
cells = []
for block in re.split(r"^# %%", src, flags=re.M)[1:]:
    head, _, body = block.partition("\n")
    body = body.strip("\n")
    head = head.strip()
    if head.startswith("[markdown]"):
        cells.append(nbformat.v4.new_markdown_cell(body))
    else:
        c = nbformat.v4.new_code_cell(body)
        tags = [t for t in head.replace("tags=", "").split(",") if t.strip()] if head else []
        if tags:
            c.metadata["tags"] = [t.strip() for t in tags]
        cells.append(c)
nb = nbformat.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbformat.write(nb, sys.argv[1])
print(len(cells), "cells")
EOF
cat > $TMPDIR/nb/run.py <<'EOF'
"""Dev runner: exec code cells of the given files in one namespace; LJ_DEV=1 loads the cached data."""
import sys, re, time, os
os.chdir('entries/laboy-juarez-2019')
sys.path.insert(0, '.')
ns = {}
for f in sys.argv[1:]:
    src = open(f).read()
    for block in re.split(r"^# %%", src, flags=re.M)[1:]:
        head, _, body = block.partition("\n")
        if head.strip().startswith("[markdown]"):
            continue
        t = time.time()
        exec(compile(body, f, "exec"), ns)
        print(f"--- cell {head.strip()} {time.time()-t:.1f}s", flush=True)
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cat >> entries/laboy-juarez-2019/lj2019.py <<'EOF'


def trial_length(units, rec):
    """Trial length in ms of a recording: the largest spike time rounded up to 100 ms."""
    return float(np.ceil(units.loc[units.recording == rec, "max_t"].max() / 100.0) * 100.0)


def lrt_responsive(tab, k, single_mask, sham_reading, length):
    """Poisson LRT across the nine whiskers and sham (Methods, "Analysis of neuronal data").

    single_mask selects the single-whisker trials used (for example one direction, O2).
    Sham reading (O1): 'a' counts sham spikes in the 125 ms window at the singles' onset;
    'b' uses the whole sham trial, with its exposure (length / 125 windows), so the rate is the
    whole-trial rate scaled to 125 ms. Recordings without sham trials are tested on the nine
    whiskers alone. Returns (G, p).
    """
    s = tab[single_mask]
    counts = list(s[f"c{k}"].to_numpy(float))
    groups = list(s["a"].to_numpy())
    expo = [1.0] * len(s)
    sh = tab[tab.kind == "sham"]
    if len(sh):
        if sham_reading == "a":
            counts += list(sh[f"c{k}"].to_numpy(float))
            expo += [1.0] * len(sh)
        else:
            counts += list(sh[f"w{k}"].to_numpy(float))
            expo += [length / WINDOW] * len(sh)
        groups += [0] * len(sh)
    counts, groups, expo = np.array(counts), np.array(groups), np.array(expo)
    labels, g = np.unique(groups, return_inverse=True)
    S = np.bincount(g, weights=counts)
    E = np.bincount(g, weights=expo)
    lam0 = counts.sum() / expo.sum()
    with np.errstate(divide="ignore", invalid="ignore"):
        term = np.where(S > 0, S * np.log(S / (E * lam0)), 0.0)
    G = 2 * term.sum()
    return G, stats.chi2.sf(G, len(labels) - 1)


def spont_rate(tab, k, sham_reading, length):
    """Spontaneous rate in Hz from sham trials (O1 readings as in lrt_responsive)."""
    sh = tab[tab.kind == "sham"]
    if not len(sh):
        return np.nan
    if sham_reading == "a":
        return sh[f"c{k}"].mean() / (WINDOW / 1000.0)
    return sh[f"w{k}"].mean() / (length / 1000.0)
EOF
cat > $TMPDIR/nb/00_load_dev.py <<'EOF'
# %%
import pickle, sys
sys.path.insert(0, '.')
import numpy as np, pandas as pd
import lj2019 as L
_D = pickle.load(open('/tmp/claude-1001/data.pkl', 'rb'))
U1, T1 = _D[1]; U2, T2 = _D[2]; U3, T3 = _D[3]
EOF
echo
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nb/00_load.py <<'EOF'
# %%
import resource
import time

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

import lj2019 as L

t0 = time.time()
z = L.open_zip()
U1, T1 = L.load_experiment(z, 1)
U3, T3 = L.load_experiment(z, 3)
U2, T2 = L.load_experiment(z, 2)
print(f"loaded in {time.time() - t0:.0f} s, peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB")
EOF
cat > $TMPDIR/nb/01_check.py <<'EOF'
# %% [markdown]
## Data check

What was loaded, by experiment, recording and condition, with the checks of the data descriptor against the values.

# %% tags=sanity
from scipy import stats
import matplotlib.pyplot as plt
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 30)
for e, (U, T) in {1: (U1, T1), 2: (U2, T2), 3: (U3, T3)}.items():
    print(f"=== Experiment {e}: {U.file.nunique()} files, {len(T)} recordings (distinct trial sequences), {len(U)} units")
    rows = []
    for rec, tab in T.items():
        kc = tab.kind.value_counts()
        rows.append(dict(recording=rec, units=int((U.recording == rec).sum()), trials=len(tab),
                         single=kc.get("single", 0), cwsw=kc.get("cwsw", 0), swsw=kc.get("swsw", 0),
                         triple=kc.get("triple", 0), sham=kc.get("sham", 0),
                         dt_values=tab.loc[tab.kind == "cwsw", "dt"].nunique(),
                         dt_min=tab.loc[tab.kind == "cwsw", "dt"].min(), dt_max=tab.loc[tab.kind == "cwsw", "dt"].max(),
                         trial_ms=L.trial_length(U, rec) if e != 3 else np.nan))
    print(pd.DataFrame(rows).to_string(index=False))
    print("units per file:", U.groupby("file").size().to_dict())
    dup = U[U.spike_hash.duplicated(keep=False)]
    print("units with identical spike times (duplicates):", len(dup))
    if len(dup):
        print(dup[["unit", "file", "recName", "depth", "n_spikes"]].to_string(index=False))
    mism = U.groupby("recording").recName.apply(lambda s: sorted(set(x.rsplit("_ch", 1)[0] for x in s)))
    mism = mism[mism.apply(len) > 1]
    print("recordings whose units carry more than one recName stem:", mism.to_dict())
    print("depth range (um):", U.depth.min(), "to", U.depth.max())
EOF
cd $TMPDIR/nb && . ../dev/bin/activate && python run.py 00_load_dev.py 01_check.py 2>&1 | tail -80
```

```
Traceback (most recent call last):
  File "/tmp/claude-1001/nb/run.py", line 7, in <module>
    src = open(f).read()
          ~~~~^^^
FileNotFoundError: [Errno 2] No such file or directory: '00_load_dev.py'
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i "s|src = open(f).read()|src = open(os.path.join('/tmp/claude-1001/nb', f)).read()|" run.py && . ../dev/bin/activate && python run.py 00_load_dev.py 01_check.py 2>&1 | tail -80
```

```
--- cell  0.8s
=== Experiment 1: 5 files, 8 recordings (distinct trial sequences), 160 units
      recording  units  trials  single  cwsw  swsw  triple  sham  dt_values  dt_min  dt_max  trial_ms
20170510:875303     12   27606    2485  5672 19311       0   138          7   -50.0    50.0     500.0
20170510:918907     26   26057    2347  5350 18229       0   131          7   -50.0    50.0     500.0
20170513:155998     21   24985    2250  4862 17748       0   125          7   -50.0    50.0     500.0
20170515:273575     14   25999    2340  5162 18367       0   130          7   -50.0    50.0     500.0
20170515:036833     20   24997    2250  5022 17600       0   125          7   -50.0    50.0     500.0
20170605:707953     10   34995    3148  7015 24657       0   175          7   -50.0    50.0     500.0
20170605:716301     18   24997    2250  5053 17569       0   125          7   -50.0    50.0     500.0
20170621:618308     39   29997    2700  5945 21202       0   150          7   -50.0    50.0     500.0
units per file: {'Experiment1/20170510.mat': 38, 'Experiment1/20170513.mat': 21, 'Experiment1/20170515.mat': 34, 'Experiment1/20170605.mat': 28, 'Experiment1/20170621.mat': 39}
units with identical spike times (duplicates): 0
recordings whose units carry more than one recName stem: {}
depth range (um): 190.0 to 1048.0
=== Experiment 2: 12 files, 16 recordings (distinct trial sequences), 247 units
      recording  units  trials  single  cwsw  swsw  triple  sham  dt_values  dt_min  dt_max  trial_ms
20160225:487285      8   24358    2926 12837  8595       0     0        101   -50.0    50.0     600.0
20160316:075886      2   29924    3590 14860 11474       0     0        101   -50.0    50.0     500.0
20160325:019965     14   40500    4050 12085  5915   18000   450        101   -50.0    50.0     500.0
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019 && python - <<'EOF'
s=open('lj2019.py').read()
s=s.replace('import io\nimport zipfile\n','import hashlib\nimport io\nimport zipfile\n')
old='''            dhash = hash(tuple(_vec(d).tobytes() for d in u.DeflectedWs)
                         + tuple(_vec(d).tobytes() for d in (u.DeltaT if exp == 3 else u.timeWs)))
            rec = f"{name.split('/')[1][:-4]}:{abs(dhash) % 10 ** 6:06d}"'''
new='''            h = hashlib.md5()
            for d in list(u.DeflectedWs) + list(u.DeltaT if exp == 3 else u.timeWs):
                h.update(_vec(d).tobytes())
            dhash = h.hexdigest()
            rec = f"{name.split('/')[1][:-4]}:{dhash[:6]}"'''
assert old in s; s=s.replace(old,new)
old='''spike_hash=hash(np.round(t, 3).tobytes())))'''
new='''spike_hash=hashlib.md5(np.round(t, 3).tobytes()).hexdigest()))'''
assert old in s; s=s.replace(old,new)
open('lj2019.py','w').write(s)
EOF
grep -n "hash" lj2019.py | head
```

```
30:import hashlib
142:    units: DataFrame, one row per unit (file, recording, depth, waveform hash, spike hash).
156:            h = hashlib.md5()
159:            dhash = h.hexdigest()
160:            rec = f"{name.split('/')[1][:-4]}:{dhash[:6]}"
163:                tab.attrs["dhash"] = dhash
167:            assert tab.attrs["dhash"] == dhash and len(tab) == len(u.DeflectedWs), (name, rec)
201:                              spike_hash=hashlib.md5(np.round(t, 3).tobytes()).hexdigest()))
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nb/10_exp1.py <<'EOF'
# %% [markdown]
## Experiment 1

Per unit: the mean count in the 125 ms window for each single whisker (both deflection directions pooled, the main reading; caudal only as a variant, see the data check), for each of the 252 sequences (36 combinations x 7 dt), and the spontaneous rate from sham trials under both sham readings (O1).

# %%
def exp1_table(U, T, single_dirs=(1, -1)):
    rows, seqs = [], {}
    for rec, tab in T.items():
        ks = U.loc[U.recording == rec, "unit"].tolist()
        length = L.trial_length(U, rec)
        cols = [f"c{k}" for k in ks]
        sing = tab[(tab.kind == "single") & tab.da.isin(single_dirs)].groupby("a")[cols].mean()
        pair = tab[tab.kind.isin(["cwsw", "swsw"])].groupby(["kind", "a", "b", "dt"])[cols].mean()
        for k in ks:
            r = dict(unit=k, recording=rec)
            for sr in "ab":
                G, p = L.lrt_responsive(tab, k, (tab.kind == "single") & tab.da.isin(single_dirs), sr, length)
                r[f"p_resp_{sr}"] = p
                r[f"spont_{sr}"] = L.spont_rate(tab, k, sr, length)
            for w in range(1, 10):
                r[f"s{w}"] = sing.loc[w, f"c{k}"]
            rows.append(r)
            seqs[k] = pair[f"c{k}"]
    df = U[["unit", "file", "recording", "depth", "animal"]].merge(pd.DataFrame(rows), on=["unit", "recording"])
    df["layer"] = df.depth.apply(L.layer_of)
    return df, seqs

E1, SEQ1 = exp1_table(U1, T1)
E1c, _ = exp1_table(U1, T1, single_dirs=(1,))
print(E1.groupby("layer").size().to_dict())

# %% [markdown]
### exp1-units

> In experiment 1, 142 of 160 single units from 8 recording sites in 5 mice were whisker-responsive, 36 in L2/3, 48 in L4, 44 in L5 and 14 in L6.

# %% tags=claim:exp1-units
exp = {"units": 160, "responsive": 142, "L2/3": 36, "L4": 48, "L5": 44, "L6": 14}
out = []
for name, df in [("both directions", E1), ("caudal singles only", E1c)]:
    for sr in "ab":
        resp = df[df[f"p_resp_{sr}"] < 0.05]
        row = dict(singles=name, sham_reading=sr, units=len(df), recordings=df.recording.nunique(),
                   mice=df.animal.nunique(), responsive=len(resp))
        for lay in ["L2/3", "L4", "L5", "L6", "outside"]:
            row[lay] = int((resp.layer == lay).sum())
        row["all within 10%"] = all(abs(row[q] - v) <= 0.1 * v for q, v in exp.items() if q != "units") and abs(len(df) - 160) <= 16
        out.append(row)
print(pd.DataFrame(out).to_string(index=False))
print("all units by layer:", E1.layer.value_counts().to_dict())
print("responsive units per mouse (both directions, sham reading a):",
      E1[E1.p_resp_a < 0.05].groupby("animal").size().to_dict(), "of", E1.groupby("animal").size().to_dict())
EOF
cd $TMPDIR/nb && . ../dev/bin/activate && python run.py 00_load_dev.py 10_exp1.py 2>&1 | tail -30
```

```
--- cell  0.9s
{'L2/3': 38, 'L4': 52, 'L5': 53, 'L6': 17}
--- cell  6.1s
            singles sham_reading  units  recordings  mice  responsive  L2/3  L4  L5  L6  outside  all within 10%
    both directions            a    160           8     5         155    36  51  52  16        0           False
    both directions            b    160           8     5         158    38  52  52  16        0           False
caudal singles only            a    160           8     5         144    36  48  46  14        0            True
caudal singles only            b    160           8     5         147    36  50  47  14        0            True
all units by layer: {'L5': 53, 'L4': 52, 'L2/3': 38, 'L6': 17}
responsive units per mouse (both directions, sham reading a): {'20170510': 37, '20170513': 21, '20170515': 33, '20170605': 26, '20170621': 38} of {'20170510': 38, '20170513': 21, '20170515': 34, '20170605': 28, '20170621': 39}
--- cell tags=claim:exp1-units 0.0s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
s=open('10_exp1.py').read()
s=s.replace('''def exp1_table(U, T, single_dirs=(1, -1)):''','''def exp1_table(U, T, single_dirs=(1,), pair_dirs=((1, 1),)):''')
s=s.replace('''        pair = tab[tab.kind.isin(["cwsw", "swsw"])].groupby''','''        pd_ok = pd.Series(list(zip(tab.da, tab.db)), index=tab.index).isin(pair_dirs)
        pair = tab[tab.kind.isin(["cwsw", "swsw"]) & pd_ok].groupby''')
s=s.replace('''E1, SEQ1 = exp1_table(U1, T1)
E1c, _ = exp1_table(U1, T1, single_dirs=(1,))''','''E1, SEQ1 = exp1_table(U1, T1)
E1all, SEQ1all = exp1_table(U1, T1, single_dirs=(1, -1), pair_dirs=((1, 1), (1, -1), (-1, 1), (-1, -1)))''')
s=s.replace('''for name, df in [("both directions", E1), ("caudal singles only", E1c)]:''','''for name, df in [("caudal (main)", E1), ("both directions pooled", E1all)]:''')
s=s.replace('''Per unit: the mean count in the 125 ms window for each single whisker (both deflection directions pooled, the main reading; caudal only as a variant, see the data check)''','''Per unit: the mean count in the 125 ms window for each single whisker deflected caudally (the paper's nine single-whisker stimuli; the files also hold rostral deflections, see the data check; all directions pooled is shown as a variant for exp1-units)''')
s=s.replace('''print("responsive units per mouse (both directions, sham reading a):"''','''print("responsive units per mouse (caudal, sham reading a):"''')
open('10_exp1.py','w').write(s)
EOF
cat >> $TMPDIR/nb/10_exp1.py <<'EOF'

# %%
R1 = E1[E1.p_resp_a < 0.05].copy()  # responsive units, sham reading (a); see exp1-units
W = [f"s{w}" for w in range(1, 10)]
R1["best_w"] = R1[W].to_numpy().argmax(axis=1) + 1
R1["cw_tuned"] = R1.best_w == L.CW12
print(len(R1), "responsive units used below (sham reading a); CW-tuned", int(R1.cw_tuned.sum()))

# %% [markdown]
### fig1b-somatotopy

> On average across experiment 1 units, the CW evoked the most spikes, followed by the within-row SWs.

# %% tags=claim:fig1b-somatotopy
pos = {w: L.POSNAME[L.relpos(w, 1)] for w in range(1, 10)}
m = R1[W].mean()
sem = R1[W].sem()
tab_ = pd.DataFrame({"position": [pos[w] for w in range(1, 10)], "mean": m.values, "sem": sem.values}, index=range(1, 10)).sort_values("mean", ascending=False)
print(tab_.round(3).to_string())
order = tab_.position.tolist()
print("CW largest:", order[0] == "CW", "| next two:", order[1:3])
print("by layer:")
print(R1.groupby("layer")[W].mean().rename(columns={f"s{w}": pos[w] for w in range(1, 10)}).round(2).T.to_string())

# %% [markdown]
### exp1-cw-tuned-fraction

> In experiment 1, 61% of responsive units were driven most strongly by the CW (89 units) and 39% by a SW (53 units).

# %% tags=claim:exp1-cw-tuned-fraction
for sr in "ab":
    r = E1[E1[f"p_resp_{sr}"] < 0.05]
    cw = int((r[W].to_numpy().argmax(axis=1) + 1 == L.CW12).sum())
    print(f"sham reading {sr}: responsive {len(r)}, CW-tuned {cw}, SW-tuned {len(r) - cw}, fraction CW {cw / len(r):.3f}")
print("by mouse (reading a):", R1.groupby("animal").cw_tuned.agg(["sum", "size"]).to_dict("index"))

# %% [markdown]
### exp1-cw-sw-comparable-firing

> CW-tuned and SW-tuned units had comparable spontaneous activity (1.28 +- 0.24 and 2.08 +- 0.4 Hz) and maximal evoked firing (4.8 +- 0.48 and 4.56 +- 0.64 spikes per stimulus).

# %% tags=claim:exp1-cw-sw-comparable-firing
R1["max_single"] = R1[W].max(axis=1)
R1["max_all"] = [max(R1.loc[i, "max_single"], SEQ1[k].max()) for i, k in zip(R1.index, R1.unit)]
rows = []
for col, lab in [("spont_a", "spont, sham reading a (Hz)"), ("spont_b", "spont, sham reading b (Hz)"),
                 ("max_single", "max evoked, reading a: best single"), ("max_all", "max evoked, reading b: best of 261")]:
    a, b = R1.loc[R1.cw_tuned, col], R1.loc[~R1.cw_tuned, col]
    t = stats.ttest_ind(a, b)
    rows.append(dict(measure=lab, cw_mean=a.mean(), cw_sem=a.sem(), sw_mean=b.mean(), sw_sem=b.sem(), t=t.statistic, p=t.pvalue))
print(pd.DataFrame(rows).round(3).to_string(index=False))
print("expected: spont 1.28 +- 0.24 (CW), 2.08 +- 0.4 (SW); max evoked 4.8 +- 0.48 (CW), 4.56 +- 0.64 (SW)")

# %% [markdown]
### supp1d-sw-tuning-broader

> Single-whisker tuning was broader for SW-tuned than for CW-tuned units in experiment 1 (one-factor ANOVA on ranked tuning curves, p = .0003).

# %% tags=claim:supp1d-sw-tuning-broader
X = R1[W].to_numpy()
ranked = -np.sort(-X, axis=1) / X.max(axis=1, keepdims=True)
cwm = R1.cw_tuned.to_numpy()
a_cw, a_sw = ranked[cwm, 1:].mean(axis=1), ranked[~cwm, 1:].mean(axis=1)
fa = stats.f_oneway(a_cw, a_sw)
print(f"(a) mean of ranks 2-9: CW-tuned {a_cw.mean():.3f}, SW-tuned {a_sw.mean():.3f}, F = {fa.statistic:.2f}, p = {fa.pvalue:.2g}")
fb = stats.f_oneway(ranked[cwm, 1:].ravel(), ranked[~cwm, 1:].ravel())
print(f"(b) pooled rank values (ranks 2-9): CW {ranked[cwm, 1:].mean():.3f}, SW {ranked[~cwm, 1:].mean():.3f}, F = {fb.statistic:.2f}, p = {fb.pvalue:.2g}")
fb9 = stats.f_oneway(ranked[cwm].ravel(), ranked[~cwm].ravel())
print(f"(b') pooled rank values with rank 1: p = {fb9.pvalue:.2g}")
print("mean ranked curve CW-tuned:", ranked[cwm].mean(0).round(2), "\nmean ranked curve SW-tuned:", ranked[~cwm].mean(0).round(2))

# %% [markdown]
### fig1d-best-sequence-exceeds-single

> Nearly all experiment 1 units spiked more to their best two-whisker combination than to their best single whisker, with a slope of 1.26.

# %% tags=claim:fig1d-best-sequence-exceeds-single
R1["best_seq"] = [SEQ1[k].max() for k in R1.unit]
x, y = R1.max_single.to_numpy(), R1.best_seq.to_numpy()
slope0 = (x @ y) / (x @ x)
lr = stats.linregress(x, y)
print(f"(a) slope through origin {slope0:.3f}; (b) slope with intercept {lr.slope:.3f} (intercept {lr.intercept:.3f})")
print(f"units with best sequence > best single: {np.sum(y > x)} of {len(x)} ({np.mean(y > x):.3f})")
print("ranges: best single", x.min().round(2), "-", x.max().round(2), "; best sequence", y.min().round(2), "-", y.max().round(2))
print("by mouse, fraction above:", R1.assign(above=y > x).groupby("animal").above.mean().round(2).to_dict())

# %% [markdown]
### fig1e-best-combination-includes-cw

> The best combination included the CW for 70% of all units, 85% of CW-tuned units and 47% of SW-tuned units, against a chance level of 22%.

# %% tags=claim:fig1e-best-combination-includes-cw
def best_combo(s):
    comb = s.groupby(level=["kind", "a", "b"]).max()
    return comb.idxmax()
bc = [best_combo(SEQ1[k]) for k in R1.unit]
R1["best_has_cw"] = [b[0] == "cwsw" for b in bc]
print(f"all {R1.best_has_cw.mean():.3f} (n={len(R1)}), CW-tuned {R1.loc[R1.cw_tuned, 'best_has_cw'].mean():.3f} (n={R1.cw_tuned.sum()}), "
      f"SW-tuned {R1.loc[~R1.cw_tuned, 'best_has_cw'].mean():.3f} (n={(~R1.cw_tuned).sum()}); chance 8/36 = {8 / 36:.3f}")
print("by mouse:", R1.groupby("animal").best_has_cw.mean().round(2).to_dict())

# %% [markdown]
### fig1f-cwsw-exceeds-swsw

> The best CW-SW sequence evoked more spikes than the best SW-SW sequence.

# %% tags=claim:fig1f-cwsw-exceeds-swsw
rows = []
for reading in ["a", "b"]:
    d = []
    for i, k in zip(R1.index, R1.unit):
        s = SEQ1[k]
        comb = s.groupby(level=["kind", "a", "b"]).max()
        allr = np.r_[R1.loc[i, W].to_numpy(float), s.to_numpy()] if reading == "a" else comb.to_numpy()
        mu, sd = allr.mean(), allr.std(ddof=1)
        d.append(((comb["cwsw"].max() - mu) / sd, (comb["swsw"].max() - mu) / sd))
    d = np.array(d)
    t = stats.ttest_rel(d[:, 0], d[:, 1])
    rows.append(dict(reading=reading, above_diagonal=int(np.sum(d[:, 0] > d[:, 1])), n=len(d),
                     mean_diff=(d[:, 0] - d[:, 1]).mean(), t=t.statistic, p=t.pvalue))
print(pd.DataFrame(rows).to_string(index=False))

# %% [markdown]
### fig1g-cwsw-sharper and supp2-sw-tuned-sharpest-cwsw

> Neurons were more sharply tuned, by lifetime sparseness, among CW-SW sequences than among SW-SW sequences.

> SW-tuned units had particularly sharp tuning for CW-SW sequences.

# %% tags=claim:fig1g-cwsw-sharper
Ns = np.arange(2, 57)
def topN_sparse(v, Ns):
    v = -np.sort(-np.asarray(v, float))
    return np.array([L.sparseness(v[:n]) for n in Ns])
SPc = np.array([topN_sparse(SEQ1[k]["cwsw"].to_numpy(), Ns) for k in R1.unit])
SPs = np.array([topN_sparse(SEQ1[k]["swsw"].to_numpy(), Ns) for k in R1.unit])
print("sequences per unit: CW-SW", len(SEQ1[R1.unit.iloc[0]]["cwsw"]), "SW-SW", len(SEQ1[R1.unit.iloc[0]]["swsw"]))
mc, ms = SPc.mean(0), SPs.mean(0)
print("mean sparseness at N = 2, 5, 10, 20, 40, 56: CW-SW", mc[[0, 3, 8, 18, 38, 54]].round(3), "SW-SW", ms[[0, 3, 8, 18, 38, 54]].round(3))
print(f"CW-SW above SW-SW at {np.sum(mc > ms)} of {len(Ns)} values of N")
print("paired t-test at each N (descriptive), largest p:", max(stats.ttest_rel(SPc[:, i], SPs[:, i]).pvalue for i in range(len(Ns))))

# %% tags=claim:supp2-sw-tuned-sharpest-cwsw
cwm = R1.cw_tuned.to_numpy()
msw, mcw = SPc[~cwm].mean(0), SPc[cwm].mean(0)
print("CW-SW sparseness, SW-tuned at N = 2, 5, 10, 20, 40, 56:", msw[[0, 3, 8, 18, 38, 54]].round(3))
print("CW-SW sparseness, CW-tuned at N = 2, 5, 10, 20, 40, 56:", mcw[[0, 3, 8, 18, 38, 54]].round(3))
print(f"SW-tuned above CW-tuned at {np.sum(msw > mcw)} of {len(Ns)} values of N")
EOF
cd $TMPDIR/nb && . ../dev/bin/activate && python run.py 00_load_dev.py 10_exp1.py 2>&1 | tail -70
```

```
--- cell  0.9s
{'L2/3': 38, 'L4': 52, 'L5': 53, 'L6': 17}
--- cell  6.5s
               singles sham_reading  units  recordings  mice  responsive  L2/3  L4  L5  L6  outside  all within 10%
         caudal (main)            a    160           8     5         144    36  48  46  14        0            True
         caudal (main)            b    160           8     5         147    36  50  47  14        0            True
both directions pooled            a    160           8     5         155    36  51  52  16        0           False
both directions pooled            b    160           8     5         158    38  52  52  16        0           False
all units by layer: {'L5': 53, 'L4': 52, 'L2/3': 38, 'L6': 17}
responsive units per mouse (caudal, sham reading a): {'20170510': 36, '20170513': 21, '20170515': 30, '20170605': 21, '20170621': 36} of {'20170510': 38, '20170513': 21, '20170515': 34, '20170605': 28, '20170621': 39}
--- cell tags=claim:exp1-units 0.0s
144 responsive units used below (sham reading a); CW-tuned 87
--- cell  0.0s
             position   mean    sem
5                  CW  0.517  0.043
8  rostral within-row  0.368  0.038
2   caudal within-row  0.327  0.032
3      ventral caudal  0.292  0.034
9     ventral rostral  0.282  0.032
4     dorsal same-arc  0.263  0.028
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && echo "from scipy import stats" >> 00_load_dev.py && . ../dev/bin/activate && python run.py 00_load_dev.py 10_exp1.py 2>&1 | sed -n '/exp1-cw-tuned-fraction/,$p'
```

```
--- cell tags=claim:exp1-cw-tuned-fraction 0.0s
                           measure  cw_mean  cw_sem  sw_mean  sw_sem      t     p
        spont, sham reading a (Hz)    1.332   0.144    2.052   0.429 -1.848 0.067
        spont, sham reading b (Hz)    1.271   0.130    2.005   0.395 -2.054 0.042
max evoked, reading a: best single    0.581   0.053    0.601   0.090 -0.205 0.838
max evoked, reading b: best of 261    0.856   0.072    0.914   0.112 -0.460 0.646
expected: spont 1.28 +- 0.24 (CW), 2.08 +- 0.4 (SW); max evoked 4.8 +- 0.48 (CW), 4.56 +- 0.64 (SW)
--- cell tags=claim:exp1-cw-sw-comparable-firing 0.0s
(a) mean of ranks 2-9: CW-tuned 0.393, SW-tuned 0.482, F = 11.94, p = 0.00072
(b) pooled rank values (ranks 2-9): CW 0.393, SW 0.482, F = 41.71, p = 1.6e-10
(b') pooled rank values with rank 1: p = 7.9e-07
mean ranked curve CW-tuned: [1.   0.71 0.55 0.44 0.38 0.33 0.29 0.25 0.19] 
mean ranked curve SW-tuned: [1.   0.77 0.65 0.55 0.48 0.43 0.38 0.34 0.26]
--- cell tags=claim:supp1d-sw-tuning-broader 0.0s
(a) slope through origin 1.379; (b) slope with intercept 1.258 (intercept 0.138)
units with best sequence > best single: 143 of 144 (0.993)
ranges: best single 0.07 - 3.68 ; best sequence 0.14 - 4.82
by mouse, fraction above: {'20170510': 0.97, '20170513': 1.0, '20170515': 1.0, '20170605': 1.0, '20170621': 1.0}
--- cell tags=claim:fig1d-best-sequence-exceeds-single 0.0s
all 0.694 (n=144), CW-tuned 0.851 (n=87), SW-tuned 0.456 (n=57); chance 8/36 = 0.222
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pickle,collections
D=pickle.load(open('data.pkl','rb'))
U,T=D[1]
for r,t in T.items():
  s=t[(t.kind=='swsw')]
  c=collections.Counter(zip(s.a,s.b,s.dt,s.da,s.db))
  combos=collections.Counter((a,b) for (a,b,dt,da,db) in c if da==1 and db==1)
  print(r, len(combos), sorted([(k,v) for k,v in combos.items() if v!=7])[:10])
  print('  dirs per combo sample', sorted(collections.Counter((a,b,da,db) for (a,b,dt,da,db) in c).items())[:12])
  break
"
```

```
20170510:875303 27 []
  dirs per combo sample [((1, 2, 1, 1), 7), ((1, 3, 1, -1), 7), ((1, 3, 1, 1), 7), ((1, 4, 1, 1), 7), ((1, 6, 1, 1), 7), ((1, 7, 1, 1), 7), ((1, 8, 1, -1), 7), ((1, 8, 1, 1), 7), ((1, 9, 1, 1), 7), ((2, 3, 1, -1), 7), ((2, 3, 1, 1), 7), ((2, 4, 1, 1), 7)]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import pickle,collections
D=pickle.load(open('data.pkl','rb'))
U,T=D[1]
for r,t in T.items():
  s=t[(t.kind.isin(['swsw','cwsw']))]
  c=collections.Counter(zip(s.a,s.b,s.da,s.db))
  allc=set((a,b) for a,b,_,_ in c)
  same=set((a,b) for a,b,da,db in c if da==db)
  print(r, len(allc), 'same-dir combos',len(same), 'missing same-dir:',sorted(allc-same), {k:v for k,v in c.items() if k[2]!=k[3]})
"
```

```
20170510:875303 36 same-dir combos 35 missing same-dir: [(3, 8)] {(5, 8, 1, -1): 361, (3, 8, 1, -1): 300, (6, 8, 1, -1): 352, (2, 3, 1, -1): 325, (5, 3, 1, -1): 347, (3, 6, -1, 1): 347, (8, 9, -1, 1): 320, (3, 4, -1, 1): 323, (4, 8, 1, -1): 376, (3, 9, -1, 1): 369, (3, 8, -1, 1): 319, (7, 8, 1, -1): 334, (1, 8, 1, -1): 350, (3, 7, -1, 1): 352, (1, 3, 1, -1): 364, (2, 8, 1, -1): 332}
20170510:918907 36 same-dir combos 35 missing same-dir: [(3, 8)] {(1, 3, 1, -1): 310, (2, 8, 1, -1): 355, (3, 9, -1, 1): 354, (3, 7, -1, 1): 312, (5, 8, 1, -1): 331, (6, 8, 1, -1): 308, (8, 9, -1, 1): 327, (3, 4, -1, 1): 337, (3, 8, 1, -1): 330, (3, 6, -1, 1): 329, (4, 8, 1, -1): 338, (1, 8, 1, -1): 324, (3, 8, -1, 1): 302, (5, 3, 1, -1): 343, (7, 8, 1, -1): 321, (2, 3, 1, -1): 320}
20170513:155998 36 same-dir combos 36 missing same-dir: [] {}
20170515:273575 36 same-dir combos 36 missing same-dir: [] {}
20170515:036833 36 same-dir combos 36 missing same-dir: [] {}
20170605:707953 36 same-dir combos 36 missing same-dir: [] {}
20170605:716301 36 same-dir combos 36 missing same-dir: [] {}
20170621:618308 36 same-dir combos 36 missing same-dir: [] {}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
s=open('10_exp1.py').read()
s=s.replace('''def exp1_table(U, T, single_dirs=(1,), pair_dirs=((1, 1),)):''','''ALLDIRS = ((1, 1), (1, -1), (-1, 1), (-1, -1))
def exp1_table(U, T, single_dirs=(1,), pair_dirs=ALLDIRS):''')
s=s.replace('''E1all, SEQ1all = exp1_table(U1, T1, single_dirs=(1, -1), pair_dirs=((1, 1), (1, -1), (-1, 1), (-1, -1)))''','''E1all, SEQ1all = exp1_table(U1, T1, single_dirs=(1, -1))''')
s=s.replace('''(the paper's nine single-whisker stimuli; the files also hold rostral deflections, see the data check; all directions pooled is shown as a variant for exp1-units)''','''(the paper's nine single-whisker stimuli; the files also hold rostral deflections, see the data check; both directions pooled is shown as a variant for exp1-units), and for each of the 252 sequences, all trials of the sequence (in 20170510 the pairs that involve whisker 3 or 8 are coded with that whisker deflected rostrally, and the pair 3-8 both ways; see the data check)''')
open('10_exp1.py','w').write(s)
EOF
. ../dev/bin/activate && python run.py 00_load_dev.py 10_exp1.py 2>&1 | grep -A3 -E "sequences per unit|reading  above|slope through|^all 0|SW-tuned above|measure"
```

```
measure  cw_mean  cw_sem  sw_mean  sw_sem      t     p
        spont, sham reading a (Hz)    1.332   0.144    2.052   0.429 -1.848 0.067
        spont, sham reading b (Hz)    1.271   0.130    2.005   0.395 -2.054 0.042
max evoked, reading a: best single    0.581   0.053    0.601   0.090 -0.205 0.838
--
(a) slope through origin 1.345; (b) slope with intercept 1.211 (intercept 0.153)
units with best sequence > best single: 143 of 144 (0.993)
ranges: best single 0.07 - 3.68 ; best sequence 0.14 - 4.82
by mouse, fraction above: {'20170510': 0.97, '20170513': 1.0, '20170515': 1.0, '20170605': 1.0, '20170621': 1.0}
--
all 0.688 (n=144), CW-tuned 0.862 (n=87), SW-tuned 0.421 (n=57); chance 8/36 = 0.222
by mouse: {'20170510': 0.53, '20170513': 0.81, '20170515': 0.77, '20170605': 0.71, '20170621': 0.69}
--- cell tags=claim:fig1e-best-combination-includes-cw 0.1s
reading  above_diagonal   n  mean_diff        t        p
      a              99 144   0.539119 5.086294 0.000001
      b              99 144   0.474793 5.078332 0.000001
--- cell tags=claim:fig1f-cwsw-exceeds-swsw 0.3s
sequences per unit: CW-SW 56 SW-SW 196
mean sparseness at N = 2, 5, 10, 20, 40, 56: CW-SW [0.013 0.016 0.023 0.034 0.055 0.094] SW-SW [0.01  0.012 0.015 0.02  0.032 0.044]
CW-SW above SW-SW at 55 of 55 values of N
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> entries/laboy-juarez-2019/lj2019.py <<'EOF'


# ---------------------------------------------------------------- experiment 2

DT_GRID = np.arange(-50, 51)  # the files hold 101 dt values, -50 to +50 ms (data check)
SWS12 = [1, 2, 3, 4, 6, 7, 8, 9]


def set_mask(tab, which):
    """CW-SW trials of the correlated (same direction) or anti-correlated set."""
    m = tab.kind == "cwsw"
    same = tab.da == tab.db
    return m & (same if which == "corr" else ~same)


def set_dirs(tab, which):
    """Directions each whisker takes in a set's CW-SW trials: {whisker: set of directions} (O2 a)."""
    s = tab[set_mask(tab, which)]
    out = {CW12: set(s.da.unique())}
    for w in SWS12:
        out[w] = set(s.loc[s.b == w, "db"].unique())
    return out


def single_mask_for(tab, dirs):
    m = np.zeros(len(tab), bool)
    for w, ds in dirs.items():
        m |= ((tab.kind == "single") & (tab.a == w) & tab.da.isin(list(ds))).to_numpy()
    return m


def fast_dt_smooth(y, dti, rng, kernels, reps=50, folds=10, ndt=101, floor=1e-3):
    """Vectorised form of dt_smooth (same method; Methods, "dt smoothing")."""
    y = np.asarray(y, float)
    n = len(y)
    ranks = np.argsort(np.argsort(rng.random((reps, n)), axis=1), axis=1)
    fold = ranks % folds  # (reps, n)
    fid = (np.arange(reps)[:, None] * folds + fold).ravel()  # fold id 0..reps*folds-1
    F = reps * folds
    dd = np.tile(dti, reps)
    yy = np.tile(y, reps)
    S_te = np.bincount(fid * ndt + dd, weights=yy, minlength=F * ndt).reshape(F, ndt)
    N_te = np.bincount(fid * ndt + dd, minlength=F * ndt).reshape(F, ndt).astype(float)
    S_all = np.bincount(dti, weights=y, minlength=ndt)
    N_all = np.bincount(dti, minlength=ndt).astype(float)
    S_tr, N_tr = S_all - S_te, N_all - N_te
    mtr = S_tr.sum(1, keepdims=True) / N_tr.sum(1, keepdims=True)
    raw = np.where(N_tr > 0, S_tr / np.maximum(N_tr, 1), mtr)  # (F, ndt)
    lam = np.maximum(raw, floor)
    ll_raw = np.sum(S_te * np.log(lam) - N_te * lam)
    K = kernels.shape[0]
    sm = np.einsum("kij,fj->kfi", kernels, raw)  # (K, F, ndt)
    lam = np.maximum(sm, floor)
    ll_sm = np.einsum("fi,kfi->k", S_te, np.log(lam)) - np.einsum("fi,kfi->k", N_te, lam)
    raw_all = np.where(N_all > 0, S_all / np.maximum(N_all, 1), y.mean())
    best = int(np.argmax(ll_sm))
    if best == K - 1:
        return np.full(ndt, y.mean()), None, "monotonic", raw_all
    if ll_raw > ll_sm.max():
        return np.full(ndt, y.mean()), None, "unsmoothed", raw_all
    return kernels[best] @ raw_all, best, "modulated", raw_all


def shuffle_csi(y, comb, dti, kern_idx, kernels, rng, n_shuf=5000, ncomb=8, ndt=101, chunk=500):
    """CSI traces of shuffles of single-trial counts across combinations within each dt (Methods).

    kern_idx[c] is the kernel index of combination c, or None for a curve set constant across dt;
    a shuffled curve of such a combination is set to its mean over dt (the measured curve's
    treatment carried over to the shuffles; the Methods do not say).
    """
    y = np.asarray(y, float)
    n = len(y)
    order = np.argsort(dti, kind="stable")
    y, comb, dti = y[order], comb[order], dti[order]
    N = np.bincount(comb * ndt + dti, minlength=ncomb * ndt).reshape(ncomb, ndt).astype(float)
    out = []
    for start in range(0, n_shuf, chunk):
        m = min(chunk, n_shuf - start)
        keys = dti[None, :] + rng.random((m, n))
        perm = np.argsort(keys, axis=1)  # a permutation within each dt group
        c_sh = comb[perm]
        idx = (np.arange(m)[:, None] * ncomb * ndt + c_sh * ndt + dti[None, :]).ravel()
        S = np.bincount(idx, weights=np.tile(y, m), minlength=m * ncomb * ndt).reshape(m, ncomb, ndt)
        cm = S.sum(2) / N.sum(1)[None, :]
        raw = np.where(N[None] > 0, S / np.maximum(N[None], 1), cm[:, :, None])
        sm = np.empty_like(raw)
        for c in range(ncomb):
            if kern_idx[c] is None:
                sm[:, c, :] = (S[:, c, :].sum(1) / N[c].sum())[:, None]
            else:
                sm[:, c, :] = raw[:, c, :] @ kernels[kern_idx[c]].T
        out.append(sparseness(np.transpose(sm, (0, 2, 1))))  # (m, ndt)
    return np.vstack(out)
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nb/20_exp2_core.py <<'EOF'
# %% [markdown]
## Experiment 2: responses, dt smoothing and the shuffle test

For each unit and each stimulus set (correlated, anti-correlated): responsiveness by the Poisson test under the direction readings (O2) and sham readings (O1); the eight CW-SW dt tuning curves on the 1 ms grid, smoothed by the cross-validated Gaussian method of the Methods; the cwSTRF, best combination and best dt; the CSI trace; and the shuffle test (5000 shuffles). The duplicate unit found in the data check (unit 179, the same spike train as unit 178) is dropped.

# %%
t0 = time.time()
KER = L.gaussian_kernels(101, L.SDS)
rng_sm = np.random.default_rng(20190801)
dup2 = set(U2.loc[U2.spike_hash.duplicated(keep="first"), "unit"])
rows2, CUR = [], {}
for rec, tab in T2.items():
    length = L.trial_length(U2, rec)
    ks = [k for k in U2.loc[U2.recording == rec, "unit"] if k not in dup2]
    sing = tab[tab.kind == "single"]
    for which in ["corr", "anti"]:
        dirs = L.set_dirs(tab, which)
        smask_a = L.single_mask_for(tab, dirs)
        smask_b = (tab.kind == "single").to_numpy()
        st = tab[L.set_mask(tab, which)]
        comb = st.b.map({w: i for i, w in enumerate(L.SWS12)}).to_numpy()
        dti = (st.dt.to_numpy() + 50).astype(int)
        # direction pairs of each trial of the set, for the direction-specific linear prediction
        for k in ks:
            r = dict(unit=k, recording=rec, set=which)
            for o2, sm_ in [("a", smask_a), ("b", smask_b)]:
                for sr in "ab":
                    r[f"p_{o2}{sr}"] = L.lrt_responsive(tab, k, sm_, sr, length)[1]
            r["spont_a"] = L.spont_rate(tab, k, "a", length)
            r["spont_b"] = L.spont_rate(tab, k, "b", length)
            c = sing[f"c{k}"]
            means = sing.groupby(["a", "da"])[f"c{k}"].mean()
            vars_ = sing.groupby(["a", "da"])[f"c{k}"].var()
            ns_ = sing.groupby(["a", "da"])[f"c{k}"].size()
            y = st[f"c{k}"].to_numpy(float)
            # O2 (a): linear prediction per trial from its own directions, averaged per combination
            lin_a = np.array([np.mean(means.loc[(L.CW12, st.da.iloc[0])] * 0 + [means.loc[(L.CW12, da)] + means.loc[(w, db)]
                                      for da, db in zip(st.da[st.b == w], st.db[st.b == w])]) for w in L.SWS12])
            mb = sing.groupby("a")[f"c{k}"].mean()
            lin_b = np.array([mb.loc[L.CW12] + mb.loc[w] for w in L.SWS12])
            curves, status, kidx = np.zeros((8, 101)), [], []
            for ci in range(8):
                sel = comb == ci
                cv, ki, stt, raw = L.fast_dt_smooth(y[sel], dti[sel], rng_sm, KER)
                curves[ci] = cv
                status.append(stt)
                kidx.append(ki)
            CUR[(k, which)] = dict(curves=curves, status=status, kidx=kidx, y=y, comb=comb, dti=dti,
                                  lin_a=lin_a, lin_b=lin_b, single_means=means, single_vars=vars_, single_n=ns_,
                                  dirs=dirs)
            rows2.append(r)
    print(rec, f"{time.time() - t0:.0f} s", flush=True)
S2 = U2[["unit", "file", "recording", "depth", "animal"]].merge(pd.DataFrame(rows2), on=["unit", "recording"])
S2["layer"] = S2.depth.apply(L.layer_of)
print(len(S2), "unit-sets;", S2.unit.nunique(), "units")
EOF
cd $TMPDIR/nb && cat > sub_load.py <<'EOF'
# %%
T2 = {k: v for k, v in list(T2.items())[2:3]}
U2 = U2[U2.recording.isin(T2)]
import time
EOF
. ../dev/bin/activate && python run.py 00_load_dev.py sub_load.py 20_exp2_core.py 2>&1 | tail -5
```

```
--- cell  0.9s
--- cell  0.0s
20160325:019965 45 s
28 unit-sets; 14 units
--- cell  45.0s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019 && python - <<'EOF'
s=open('lj2019.py').read()
old='''    sm = np.einsum("kij,fj->kfi", kernels, raw)  # (K, F, ndt)
    lam = np.maximum(sm, floor)
    ll_sm = np.einsum("fi,kfi->k", S_te, np.log(lam)) - np.einsum("fi,kfi->k", N_te, lam)'''
new='''    sm = (kernels.reshape(K * ndt, ndt) @ raw.T).reshape(K, ndt, F)  # (K, ndt, F)
    lam = np.maximum(sm, floor)
    ll_sm = (np.log(lam).reshape(K, -1) @ S_te.T.ravel()) - (lam.reshape(K, -1) @ N_te.T.ravel())'''
assert old in s; s=s.replace(old,new)
open('lj2019.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python -c "
import sys,time; sys.path.insert(0,'entries/laboy-juarez-2019')
import lj2019 as L, numpy as np
K=L.gaussian_kernels(101,L.SDS); rng=np.random.default_rng(0)
dti=rng.integers(0,101,850); y=rng.poisson(0.5+0.5*np.exp(-((dti-30)/8.)**2))
t=time.time()
for i in range(10): r=L.fast_dt_smooth(y,dti,rng,K)
print((time.time()-t)/10, r[1:3])
import cProfile
cProfile.run('L.fast_dt_smooth(y,dti,rng,K)',sort='cumtime')
" 2>&1 | head -25
```

```
0.03155951499938965 (28, 'modulated')
         88 function calls in 0.031 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.031    0.031 {built-in method builtins.exec}
        1    0.001    0.001    0.031    0.031 <string>:1(<module>)
        1    0.029    0.029    0.030    0.030 lj2019.py:463(fast_dt_smooth)
        3    0.000    0.000    0.001    0.000 fromnumeric.py:48(_wrapfunc)
        2    0.000    0.000    0.001    0.000 fromnumeric.py:1115(argsort)
        2    0.001    0.000    0.001    0.000 {method 'argsort' of 'numpy.ndarray' objects}
        3    0.000    0.000    0.000    0.000 {method 'ravel' of 'numpy.ndarray' objects}
        5    0.000    0.000    0.000    0.000 {method 'reduce' of 'numpy.ufunc' objects}
        1    0.000    0.000    0.000    0.000 {method 'mean' of 'numpy.ndarray' objects}
        2    0.000    0.000    0.000    0.000 _shape_base_impl.py:1157(tile)
        1    0.000    0.000    0.000    0.000 _methods.py:115(_mean)
        2    0.000    0.000    0.000    0.000 {method 'sum' of 'numpy.ndarray' objects}
        2    0.000    0.000    0.000    0.000 _methods.py:47(_sum)
        2    0.000    0.000    0.000    0.000 {method 'repeat' of 'numpy.ndarray' objects}
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
s=open('20_exp2_core.py').read()
old='''            lin_a = np.array([np.mean(means.loc[(L.CW12, st.da.iloc[0])] * 0 + [means.loc[(L.CW12, da)] + means.loc[(w, db)]
                                      for da, db in zip(st.da[st.b == w], st.db[st.b == w])]) for w in L.SWS12])'''
new='''            md = means.to_dict()
            lin_a = np.array([np.mean([md[(L.CW12, da)] + md[(w, db)] for da, db in zip(st.da[st.b == w], st.db[st.b == w])])
                              for w in L.SWS12])'''
assert old in s; s=s.replace(old,new)
s=s.replace('''            c = sing[f"c{k}"]
''','')
open('20_exp2_core.py','w').write(s)
EOF
cat > $TMPDIR/nb/21_exp2_shuffle.py <<'EOF'
# %%
t0 = time.time()
rng_sh = np.random.default_rng(20190802)
for i, r in S2.iterrows():
    d = CUR[(r.unit, r.set)]
    csi = L.sparseness(d["curves"].T)
    sh = L.shuffle_csi(d["y"], d["comb"], d["dti"], d["kidx"], KER, rng_sh)
    p, dm = L.mahalanobis_p(csi, sh)
    d["csi_trace"] = csi
    S2.loc[i, "p_shuffle"] = p
    S2.loc[i, "maha"] = dm
print(f"shuffle tests: {time.time() - t0:.0f} s")
EOF
. ../dev/bin/activate && python run.py 00_load_dev.py sub_load.py 20_exp2_core.py 21_exp2_shuffle.py 2>&1 | tail -4
```

```
28 unit-sets; 14 units
--- cell  8.3s
shuffle tests: 17 s
--- cell  17.3s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat > dump2.py <<'EOF'
# %%
pickle.dump((S2, CUR, KER), open('/tmp/claude-1001/exp2.pkl', 'wb'))
EOF
. ../dev/bin/activate && /usr/bin/time -v python run.py 00_load_dev.py 20_exp2_core.py 21_exp2_shuffle.py dump2.py 2>&1 | grep -E "cell|unit-sets|shuffle|Maximum res|Elapsed"
```

```
--- cell  1.0s
	Command being timed: "python run.py 00_load_dev.py 20_exp2_core.py 21_exp2_shuffle.py dump2.py"
	Elapsed (wall clock) time (h:mm:ss or m:ss): 0:01.14
	Maximum resident set size (kbytes): 419160
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && . ../dev/bin/activate && python run.py 00_load_dev.py 20_exp2_core.py 2>&1 | tail -5
```

```
exec(compile(body, f, "exec"), ns)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "20_exp2_core.py", line 1, in <module>
    # %% [markdown]
NameError: name 'time' is not defined. Did you forget to import 'time'?
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && echo "import time, pickle" >> 00_load_dev.py && . ../dev/bin/activate && /usr/bin/time -v python run.py 00_load_dev.py 20_exp2_core.py 21_exp2_shuffle.py dump2.py 2>&1 | grep -E "cell|unit-sets|shuffle|Maximum res|Elapsed|Error"; date -u
```

```
--- cell  0.9s
492 unit-sets; 246 units
--- cell  167.3s
shuffle tests: 424 s
--- cell  423.7s
--- cell  16.4s
	Command being timed: "python run.py 00_load_dev.py 20_exp2_core.py 21_exp2_shuffle.py dump2.py"
	Elapsed (wall clock) time (h:mm:ss or m:ss): 10:09.24
	Maximum resident set size (kbytes): 9102444
Thu Nov 12 17:32:11 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's|print(f"--- cell {head.strip()} {time.time()-t:.1f}s", flush=True)|import resource; print(f"--- cell {head.strip()} {time.time()-t:.1f}s maxrss {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.2f} GB", flush=True)|' run.py && . ../dev/bin/activate && python run.py 00_load_dev.py sub_load.py 20_exp2_core.py 21_exp2_shuffle.py 2>&1 | grep cell
```

```
--- cell  0.9s maxrss 0.42 GB
--- cell  0.0s maxrss 0.42 GB
--- cell  8.8s maxrss 0.82 GB
--- cell  17.7s maxrss 0.84 GB
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat > sub_load2.py <<'EOF'
# %%
T2 = {k: v for k, v in T2.items() if k.startswith('20160504') or k.startswith('20160914')}
U2 = U2[U2.recording.isin(T2)]
U2 = U2.groupby('recording').head(2)
EOF
sed -i 's|    print(rec, f"{time.time() - t0:.0f} s", flush=True)|    print(rec, f"{time.time() - t0:.0f} s", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6, flush=True)|' 20_exp2_core.py && echo "import resource" >> 00_load_dev.py && . ../dev/bin/activate && python run.py 00_load_dev.py sub_load2.py 20_exp2_core.py 21_exp2_shuffle.py 2>&1 | grep -v Warn | tail
```

```
--- cell  0.9s maxrss 0.42 GB
--- cell  0.0s maxrss 0.42 GB
20160504:720192 2 s 0.661184
20160504:214735 3 s 0.709288
20160914:307658 4 s 0.74786
20160914:894688 6 s 0.829744
16 unit-sets; 8 units
--- cell  6.0s maxrss 0.83 GB
shuffle tests: 17 s
--- cell  17.4s maxrss 0.95 GB
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && . ../dev/bin/activate && python run.py 00_load_dev.py 20_exp2_core.py 2>&1 | grep -v Warn | tail -20
```

```
--- cell  0.8s maxrss 0.42 GB
20160225:487285 4 s 0.669912
20160316:075886 6 s 0.671352
20160325:019965 14 s 0.86124
20160406:230725 28 s 1.362652
20160504:720192 35 s 1.458424
20160504:214735 50 s 1.871872
20160506:009977 52 s 1.87266
20160803:526806 60 s 2.036748
20160803:158660 76 s 2.421648
20160808:969942 83 s 2.546328
20160817:773295 102 s 3.331736
20160829:885448 107 s 3.374196
20160909:689152 114 s 3.513868
20160909:219915 118 s 3.529328
20160914:307658 135 s 4.024744
20160914:894688 158 s 4.978588
492 unit-sets; 246 units
--- cell  158.2s maxrss 4.98 GB
Shell cwd was reset to
```

**Agent calls Bash**

```bash
ls -la $TMPDIR/*.pkl
```

```
-rw-r--r-- 1 runner runner  276133053 Nov 12 17:16 /tmp/claude-1001/data.pkl
-rw-r--r-- 1 runner runner 4405219146 Nov 12 17:32 /tmp/claude-1001/exp2.pkl
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat > /tmp/claude-1001/nb/sz.py <<'EOF'
# %%
d = CUR[next(iter(CUR))]
for k_, v_ in d.items():
    print(k_, len(pickle.dumps(v_)), type(v_))
EOF
. ../dev/bin/activate && python run.py 00_load_dev.py sub_load.py 20_exp2_core.py sz.py 2>&1 | tail -16
```

```
20160325:019965 8 s 0.81804
28 unit-sets; 14 units
--- cell  8.4s maxrss 0.82 GB
curves 6617 <class 'numpy.ndarray'>
status 52 <class 'list'>
kidx 27 <class 'list'>
y 49192 <class 'numpy.ndarray'>
comb 49192 <class 'numpy.ndarray'>
dti 49192 <class 'numpy.ndarray'>
lin_a 212 <class 'numpy.ndarray'>
lin_b 212 <class 'numpy.ndarray'>
single_means 3192599 <class 'pandas.Series'>
single_vars 3192599 <class 'pandas.Series'>
single_n 1224 <class 'pandas.Series'>
dirs 327 <class 'dict'>
--- cell  0.0s maxrss 0.82 GB
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019 && python - <<'EOF'
s=open('lj2019.py').read()
old='''    for rec, tab in tables.items():
        ex = extras[rec]
        cols = {key_: v for key_, v in ex.items() if not key_.startswith("h")}
        tables[rec] = pd.concat([tab, pd.DataFrame(cols)], axis=1)
        tables[rec].attrs["psth"] = {key_: v for key_, v in ex.items() if key_.startswith("h")}
        tables[rec].attrs["psth_rows"] = tab.kind.isin(["single", "sham"]).to_numpy()
    return pd.DataFrame(units), tables'''
new='''    psth = {}
    for rec, tab in tables.items():
        ex = extras[rec]
        cols = {key_: v for key_, v in ex.items() if not key_.startswith("h")}
        tab.attrs = {}  # pandas copies attrs into every derived object
        tables[rec] = pd.concat([tab, pd.DataFrame(cols)], axis=1)
        psth[rec] = dict(rows=tab.kind.isin(["single", "sham"]).to_numpy(),
                         **{key_: v for key_, v in ex.items() if key_.startswith("h")})
    return pd.DataFrame(units), tables, psth'''
assert old in s; s=s.replace(old,new)
s=s.replace('''    """Return (units, tables, info).''','''    """Return (units, tables, psth).''')
s=s.replace('''    (``p<k>``), and 10 ms bins from -50 to +200 ms around onset for single and sham trials.''','''    (``p<k>``), and spikes after the epoch (``o<k>``); psth: dict recording -> counts in 10 ms
    bins from -50 to +200 ms around onset for the single and sham trials (``rows``).''')
open('lj2019.py','w').write(s)
EOF
grep -n "attrs" lj2019.py; cd $TMPDIR && sed -i 's/out\[exp\]=L.load_experiment(z,exp)/out[exp]=L.load_experiment(z,exp)/' load_all.py && . dev/bin/activate && python load_all.py 2>&1 | grep -E "time|Error"; ls -la data.pkl
```

```
164:                tab.attrs["dhash"] = dhash
168:            assert tab.attrs["dhash"] == dhash and len(tab) == len(u.DeflectedWs), (name, rec)
209:        tab.attrs = {}  # pandas copies attrs into every derived object
1 time 42.896578550338745 maxrss GB 1.773252
3 time 6.846580266952515 maxrss GB 1.773252
2 time 96.8318521976471 maxrss GB 3.55344
-rw-r--r-- 1 runner runner 276146237 Nov 12 17:39 data.pkl
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's/U1, T1 = _D\[1\]; U2, T2 = _D\[2\]; U3, T3 = _D\[3\]/U1, T1, P1 = _D[1]; U2, T2, P2 = _D[2]; U3, T3, P3 = _D[3]/' 00_load_dev.py && sed -i 's/^U1, T1 = /U1, T1, P1 = /; s/^U3, T3 = /U3, T3, P3 = /; s/^U2, T2 = /U2, T2, P2 = /' 00_load.py && cat 00_load_dev.py && grep "= L.load" 00_load.py && . ../dev/bin/activate && python run.py 00_load_dev.py 20_exp2_core.py 21_exp2_shuffle.py dump2.py 2>&1 | grep -E "cell|unit-sets|shuffle|Error"; ls -la /tmp/claude-1001/exp2.pkl; date -u
```

```
# %%
import pickle, sys
sys.path.insert(0, '.')
import numpy as np, pandas as pd
import lj2019 as L
_D = pickle.load(open('/tmp/claude-1001/data.pkl', 'rb'))
U1, T1, P1 = _D[1]; U2, T2, P2 = _D[2]; U3, T3, P3 = _D[3]
from scipy import stats
import time, pickle
import resource
U1, T1, P1 = L.load_experiment(z, 1)
U3, T3, P3 = L.load_experiment(z, 3)
U2, T2, P2 = L.load_experiment(z, 2)
--- cell  0.9s maxrss 0.42 GB
492 unit-sets; 246 units
--- cell  143.7s maxrss 0.67 GB
shuffle tests: 412 s
--- cell  412.4s maxrss 0.82 GB
--- cell  0.6s maxrss 0.82 GB
-rw-r--r-- 1 runner runner 52017216 Nov 12 17:48 /tmp/claude-1001/exp2.pkl
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat > load2_dev.py <<'EOF'
# %%
S2, CUR, KER = pickle.load(open('/tmp/claude-1001/exp2.pkl', 'rb'))
EOF
cat > 22_exp2_a.py <<'EOF'
# %% [markdown]
### exp2-units

> In experiment 2, 247 single units were isolated in 12 mice; 224 were responsive to correlated and 227 to anti-correlated stimuli.

# %% tags=claim:exp2-units
print(f"units in the files: {len(U2)} in {U2.file.nunique()} files; after dropping the duplicate: {S2.unit.nunique()}")
rows = []
for o2 in "ab":
    for sr in "ab":
        resp = S2[S2[f"p_{o2}{sr}"] < 0.05]
        rows.append(dict(directions=o2, sham=sr, corr=int((resp.set == "corr").sum()), anti=int((resp.set == "anti").sum()),
                         sets=len(resp)))
print(pd.DataFrame(rows).to_string(index=False))
RESP = (S2.p_aa < 0.05)  # main reading: O2 (a), sham (a)
print("layers of responsive sets (O2 a, sham a):", S2[RESP].groupby(["set", "layer"]).size().unstack().to_dict("index"))
print("expected layer counts corr/anti: L2/3 54/54, L4 78/79, L5 71/70, L6 21/24")
print("responsive sets per mouse:", S2[RESP].groupby("animal").size().to_dict())
print("recordings without sham trials (tested on the nine whiskers alone):",
      [r for r, t in T2.items() if (t.kind == "sham").sum() == 0])

# %% [markdown]
### methods-dt-modulation

> Of 3,608 dt tuning curves, 33% had monotonically increasing likelihoods and 23% were best fit unsmoothed, so 56% (2,004) were set constant across dt.

Reading (a) of the criterion (held-out dt values without training trials scored on the training mean, kernel renormalised at the edges) is the main run; reading (b), zero padding at the edges, is run below on the responsive sets.

# %% tags=claim:methods-dt-modulation
def status_table(S, key="status"):
    st = np.concatenate([CUR[(u, s)][key] for u, s in zip(S.unit, S.set)])
    n = len(st)
    return dict(curves=n, monotonic=np.mean(st == "monotonic"), unsmoothed=np.mean(st == "unsmoothed"),
                constant=int(np.sum(st != "modulated")), constant_frac=np.mean(st != "modulated"))
print("responsive sets (O2 a, sham a):", {k: round(v, 3) for k, v in status_table(S2[RESP]).items()})
print("all sets:", {k: round(v, 3) for k, v in status_table(S2).items()})
EOF
. ../dev/bin/activate && python run.py 00_load_dev.py load2_dev.py 22_exp2_a.py 2>&1 | grep -v "^---"
```

```
units in the files: 247 in 12 files; after dropping the duplicate: 246
directions sham  corr  anti  sets
         a    a   231   232   463
         a    b   238   236   474
         b    a   237   237   474
         b    b   240   240   480
layers of responsive sets (O2 a, sham a): {'anti': {'L2/3': 51.0, 'L4': 80.0, 'L5': 74.0, 'L6': 27.0, 'outside': nan}, 'corr': {'L2/3': 52.0, 'L4': 79.0, 'L5': 73.0, 'L6': 26.0, 'outside': 1.0}}
expected layer counts corr/anti: L2/3 54/54, L4 78/79, L5 71/70, L6 21/24
responsive sets per mouse: {'20160225': 15, '20160316': 4, '20160325': 28, '20160406': 42, '20160504': 64, '20160506': 7, '20160803': 74, '20160808': 24, '20160817': 52, '20160829': 16, '20160909': 27, '20160914': 110}
recordings without sham trials (tested on the nine whiskers alone): ['20160225:10da10', '20160316:2dc362']
responsive sets (O2 a, sham a): {'curves': 3704, 'monotonic': np.float64(0.574), 'unsmoothed': np.float64(0.0), 'constant': 2127, 'constant_frac': np.float64(0.574)}
all sets: {'curves': 3936, 'monotonic': np.float64(0.583), 'unsmoothed': np.float64(0.0), 'constant': 2295, 'constant_frac': np.float64(0.583)}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat > 23_exp2_b.py <<'EOF'
# %% [markdown]
### exp2-combination-selective-prevalence

> 52% of experiment 2 units (129) were significantly combination-selective, based on correlated (35%) or anti-correlated stimuli (46%); 187 response sets were combination-selective and 264 nonselective.

# %% tags=claim:exp2-combination-selective-prevalence
R2 = S2[RESP].copy().reset_index(drop=True)
R2["sel_fdr_all"] = L.bh(R2.p_shuffle.to_numpy())
R2["sel_fdr_sets"] = False
for s_ in ["corr", "anti"]:
    m = (R2.set == s_).to_numpy()
    R2.loc[m, "sel_fdr_sets"] = L.bh(R2.loc[m, "p_shuffle"].to_numpy())
ncell = S2.unit.nunique()
rows = []
for fam in ["sel_fdr_all", "sel_fdr_sets"]:
    sel = R2[R2[fam]]
    cells = sel.unit.nunique()
    nc, na = int((sel.set == "corr").sum()), int((sel.set == "anti").sum())
    rc, ra = int((R2.set == "corr").sum()), int((R2.set == "anti").sum())
    rows.append(dict(fdr_family=fam, selective_sets=len(sel), nonselective_sets=len(R2) - len(sel), cells=cells,
                     frac_cells=cells / ncell, corr_over_resp=nc / rc, anti_over_resp=na / ra,
                     corr_over_cells=nc / ncell, anti_over_cells=na / ncell))
print(pd.DataFrame(rows).round(3).to_string(index=False))
print("uncorrected p < 0.05:", int((R2.p_shuffle < 0.05).sum()), "of", len(R2))
print("selective sets per mouse (FDR all):", R2[R2.sel_fdr_all].groupby("animal").size().to_dict())
SEL = R2.sel_fdr_all.to_numpy()  # main reading (O4 a)
EOF
. ../dev/bin/activate && python run.py 00_load_dev.py load2_dev.py 22_exp2_a.py 23_exp2_b.py 2>&1 | grep -v "^---" | tail -8
```

```
recordings without sham trials (tested on the nine whiskers alone): ['20160225:10da10', '20160316:2dc362']
responsive sets (O2 a, sham a): {'curves': 3704, 'monotonic': np.float64(0.574), 'unsmoothed': np.float64(0.0), 'constant': 2127, 'constant_frac': np.float64(0.574)}
all sets: {'curves': 3936, 'monotonic': np.float64(0.583), 'unsmoothed': np.float64(0.0), 'constant': 2295, 'constant_frac': np.float64(0.583)}
  fdr_family  selective_sets  nonselective_sets  cells  frac_cells  corr_over_resp  anti_over_resp  corr_over_cells  anti_over_cells
 sel_fdr_all             318                145    189       0.768           0.641           0.733            0.602            0.691
sel_fdr_sets             312                151    188       0.764           0.610           0.737            0.573            0.695
uncorrected p < 0.05: 340 of 463
selective sets per mouse (FDR all): {'20160225': 10, '20160316': 4, '20160325': 20, '20160406': 28, '20160504': 50, '20160506': 6, '20160803': 57, '20160808': 20, '20160817': 27, '20160829': 7, '20160909': 7, '20160914': 82}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat > test_maha.py <<'EOF'
# %%
rng_t = np.random.default_rng(1)
res = []
for i, r in R2.sample(40, random_state=0).iterrows():
    d = CUR[(r.unit, r.set)]
    sh = L.shuffle_csi(d["y"], d["comb"], d["dti"], d["kidx"], KER, rng_t, n_shuf=2000)
    mu = sh.mean(0); C = np.cov(sh, rowvar=False)
    out = dict(p0=r.p_shuffle)
    for rc in [1e-10, 1e-6, 1e-3, 1e-2]:
        P = np.linalg.pinv(C, rcond=rc, hermitian=True)
        ds = np.einsum("ij,jk,ik->i", sh - mu, P, sh - mu); dm = (d["csi_trace"] - mu) @ P @ (d["csi_trace"] - mu)
        out[f"p_{rc}"] = (1 + np.sum(ds >= dm)) / (1 + len(ds))
    ds = np.sum((sh - mu) ** 2, 1); dm = np.sum((d["csi_trace"] - mu) ** 2)
    out["p_eucl"] = (1 + np.sum(ds >= dm)) / (1 + len(ds))
    out["mean_csi_meas"] = d["csi_trace"].mean(); out["mean_csi_sh"] = mu.mean()
    res.append(out)
res = pd.DataFrame(res)
print(res.round(4).to_string())
print((res.drop(columns=["mean_csi_meas", "mean_csi_sh"]) < 0.05).mean())
EOF
. ../dev/bin/activate && python run.py 00_load_dev.py load2_dev.py 22_exp2_a.py 23_exp2_b.py test_maha.py 2>&1 | tail -52
```

```
uncorrected p < 0.05: 340 of 463
selective sets per mouse (FDR all): {'20160225': 10, '20160316': 4, '20160325': 20, '20160406': 28, '20160504': 50, '20160506': 6, '20160803': 57, '20160808': 20, '20160817': 27, '20160829': 7, '20160909': 7, '20160914': 82}
--- cell tags=claim:exp2-combination-selective-prevalence 0.0s maxrss 0.49 GB
        p0  p_1e-10  p_1e-06  p_0.001  p_0.01  p_eucl  mean_csi_meas  mean_csi_sh
0   0.0002   0.0005   0.0005   0.0005  0.0005  0.0005         0.0344       0.0051
1   0.0020   0.0025   0.0005   0.0005  0.0005  0.0005         0.0324       0.0064
2   0.0002   0.0005   0.0005   0.0005  0.0005  0.0005         0.1219       0.0111
3   0.0328   0.0285   0.0135   0.0045  0.0040  0.0055         0.0055       0.0022
4   0.0002   0.0005   0.0005   0.0005  0.0005  0.0005         0.0424       0.0056
5   0.0198   0.0155   0.0010   0.0005  0.0005  0.0005         0.0219       0.0092
6   0.2340   0.1734   0.1474   0.1249  0.2164  0.4888         0.0079       0.0062
7   0.0566   0.0550   0.0215   0.0100  0.0090  0.0010         0.0933       0.0326
8   0.0002   0.0005   0.0005   0.0005  0.0005  0.0005         0.0167       0.0032
9   0.0530   0.0505   0.0265   0.0125  0.0090  0.0030         0.0227       0.0083
10  0.0124   0.0165   0.0085   0.0065  0.0040  0.0010         0.0142       0.0042
11  0.0010   0.0020   0.0015   0.0010  0.0005  0.0005         0.0162       0.0065
12  0.0426   0.0275   0.0225   0.0145  0.0145  0.0240         0.0876       0.0408
13  0.1720   0.1604   0.0640   0.0505  0.0340  0.0110         0.0517       0.0202
14  0.0002   0.0005   0.0005   0.0005  0.0005  0.0005         0.0799       0.0086
15  0.0468   0.0330   0.0045   0.0020  0.0015  0.0020         0.0483       0.0181
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i -E "Fig. 2f|Supplementary Fig. 4|0.81|Fig. 6b|Fig. 6c|alignment|half-width|Fig. 7a|Fig. 7b|1,309|z-scored" paper/10.1038-s41593-019-0448-6.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 820,870p paper/10.1038-s41593-019-0448-6.txt; sed -n 1296,1312p paper/10.1038-s41593-019-0448-6.txt; sed -n 2368,2384p paper/10.1038-s41593-019-0448-6.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat > 24_exp2_c.py <<'EOF'
# %% [markdown]
### Per-unit measures used by the claims below

For each responsive set (a "unit" in the paper's sense): the best combination and best dt (the maximum of the cwSTRF), the eight responses at the best dt under O3 (a) the smoothed value and (b) the mean raw count within +-5 ms of the best dt, the linear predictions under O2 (a) direction-specific and (b) both directions, CW or SW tuning under the same two readings, and the spontaneous rate. A set whose best-combination curve was set constant across dt has no defined best dt (the argmax then falls on the first tied dt); it is flagged.

# %%
def derive(R):
    out = []
    for _, r in R.iterrows():
        d = CUR[(r.unit, r.set)]
        cv = d["curves"]
        c_best, j_best = np.unravel_index(np.argmax(cv), cv.shape)
        resp_a = cv[:, j_best]
        near = np.abs(d["dti"] - j_best) <= 5
        resp_b = np.array([d["y"][near & (d["comb"] == c)].mean() if np.any(near & (d["comb"] == c)) else np.nan for c in range(8)])
        sm = d["single_means"]
        dirs = d["dirs"]
        sing_a = np.array([sm.loc[[(w, x) for x in sorted(dirs[w])]].mean() for w in range(1, 10)])
        sing_b = np.array([sm.loc[w].mean() for w in range(1, 10)])
        out.append(dict(c_best=c_best, j_best=j_best, dt_best=j_best - 50, best_const=d["status"][c_best] != "modulated",
                        resp_a=resp_a, resp_b=resp_b, lin_a=d["lin_a"], lin_b=d["lin_b"],
                        cw_tuned_a=np.argmax(sing_a) + 1 == L.CW12, cw_tuned_b=np.argmax(sing_b) + 1 == L.CW12,
                        sing_a=sing_a, sing_b=sing_b,
                        csi_a=L.sparseness(resp_a), csi_b=L.sparseness(resp_b),
                        csi_lin_a=L.sparseness(d["lin_a"]), csi_lin_b=L.sparseness(d["lin_b"])))
    return pd.concat([R.reset_index(drop=True), pd.DataFrame(out)], axis=1)

M2 = derive(R2)
M2["sel"] = SEL
print(len(M2), "sets;", int(M2.sel.sum()), "selective;", int(M2.best_const.sum()), "with a constant best-combination curve")
EOF
. ../dev/bin/activate && python run.py 00_load_dev.py load2_dev.py 22_exp2_a.py 23_exp2_b.py 24_exp2_c.py 2>&1 | tail -3
```

```
--- cell tags=claim:exp2-combination-selective-prevalence 0.0s maxrss 0.49 GB
463 sets; 318 selective; 90 with a constant best-combination curve
--- cell  1.5s maxrss 0.49 GB
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat > 25_exp2_d.py <<'EOF'
# %% [markdown]
### fig2f-shuffle-abolishes-tuning

> Average peak-aligned combination tuning of combination-selective units was sharp, and shuffling spike counts across stimuli and trials abolished it.

# %% tags=claim:fig2f-shuffle-abolishes-tuning
rng_2f = np.random.default_rng(2)
selM = M2[M2.sel]
meas, sh_a, sh_b = [], [], []
for _, r in selM.iterrows():
    d = CUR[(r.unit, r.set)]
    order = np.r_[r.c_best, [c for c in range(8) if c != r.c_best]]
    meas.append(r.resp_a[order])
    y_sh = d["y"].copy()
    for j in np.unique(d["dti"]):  # one shuffle across combinations within each dt
        ii = np.where(d["dti"] == j)[0]
        y_sh[ii] = y_sh[rng_2f.permutation(ii)]
    curves = np.zeros((8, 101))
    for c in range(8):
        sel_ = d["comb"] == c
        raw = np.bincount(d["dti"][sel_], weights=y_sh[sel_], minlength=101) / np.maximum(np.bincount(d["dti"][sel_], minlength=101), 1)
        curves[c] = KER[d["kidx"][c]] @ raw if d["kidx"][c] is not None else np.full(101, y_sh[sel_].mean())
    v = curves[:, r.j_best]
    sh_a.append(v[order])
    sh_b.append(np.r_[v.max(), np.delete(v, v.argmax())])
meas, sh_a, sh_b = map(np.array, (meas, sh_a, sh_b))
for name, arr in [("measured", meas), ("shuffled, aligned to measured best (a)", sh_a), ("shuffled, own peak (b)", sh_b)]:
    m = arr.mean(0)
    print(f"{name}: mean curve {m.round(3)}, CSI of mean curve {L.sparseness(m):.3f}")
first, rest = sh_a[:, 0], sh_a[:, 1:].mean(1)
diff = first - rest
print(f"(a) shuffled first point minus mean of the other seven: {diff.mean():.4f} (s.e.m. {diff.std(ddof=1) / np.sqrt(len(diff)):.4f}); "
      f"s.e.m. of the first point {first.std(ddof=1) / np.sqrt(len(first)):.4f}; n = {len(diff)}")

# %% [markdown]
### fig2f-most-selective-lower-firing

> Among combination-selective units, the 25% most selective had lower spontaneous and whisker-evoked firing than the 25% least selective.

# %% tags=claim:fig2f-most-selective-lower-firing
q = selM.sort_values("csi_a")
nq = len(q) // 4
lo, hi = q.iloc[:nq], q.iloc[-nq:]
rows = []
for lab, f in [("spont, sham a (Hz)", lambda d: d.spont_a), ("spont, sham b (Hz)", lambda d: d.spont_b),
               ("evoked (a): best response", lambda d: d.resp_a.apply(np.max)), ("evoked (b): mean of 8", lambda d: d.resp_a.apply(np.mean))]:
    a, b = f(hi).dropna(), f(lo).dropna()
    t = stats.ttest_ind(a, b)
    rows.append(dict(measure=lab, most_selective=a.mean(), least_selective=b.mean(), t=t.statistic, p=t.pvalue, n=f"{len(a)}/{len(b)}"))
print(pd.DataFrame(rows).round(4).to_string(index=False))

# %% [markdown]
### supp4-selectivity-at-high-rates

> Substantial combination selectivity was present among the most responsive combination-selective units and after subtracting spontaneous activity.

# %% tags=claim:supp4-selectivity-at-high-rates
bestr = M2.resp_a.apply(np.max)
print("selective < 0.81:", int(((bestr < 0.81) & M2.sel).sum()), "| selective >= 0.81:", int(((bestr >= 0.81) & M2.sel).sum()),
      "| nonselective >= 0.81:", int(((bestr >= 0.81) & ~M2.sel).sum()), "| nonselective < 0.81:", int(((bestr < 0.81) & ~M2.sel).sum()))
g = M2[(bestr >= 0.81) & M2.sel]
al = []
for _, r in g.iterrows():
    order = np.r_[r.c_best, [c for c in range(8) if c != r.c_best]]
    sp = r.spont_a * L.WINDOW / 1000 if np.isfinite(r.spont_a) else np.nan
    al.append(r.resp_a[order] - sp)
al = np.array(al)
al = al[np.isfinite(al).all(1)]
pk = al[:, 0] - al[:, 1:].mean(1)
print(f"high-rate selective, spontaneous subtracted (n = {len(al)}, sets with sham trials): mean curve {al.mean(0).round(3)}")
print(f"peak minus mean of other seven: {pk.mean():.3f}, s.e.m. {pk.std(ddof=1) / np.sqrt(len(pk)):.3f}, ratio {pk.mean() / (pk.std(ddof=1) / np.sqrt(len(pk))):.1f}")

# %% [markdown]
### fig2g-best-combination-bias

> Best CW-SW combinations covered all combinations but were nonuniformly distributed, biased toward the rostral within-row SW and the SWs ventral to the CW (Rayleigh test, P = 4 x 10-19, n = 451).

# %% tags=claim:fig2g-best-combination-bias
def rayleigh(theta):
    n = len(theta)
    Rbar = np.abs(np.mean(np.exp(1j * theta)))
    Z = n * Rbar ** 2
    p = np.exp(np.sqrt(1 + 4 * n + 4 * (n ** 2 - (n * Rbar) ** 2)) - (1 + 2 * n))  # Zar's approximation
    return Z, min(p, 1.0)
bw = np.array(L.SWS12)[M2.c_best]
rel = [L.relpos(w, 2) for w in bw]
theta = np.array([np.arctan2(-dr, dc) for dr, dc in rel])  # angle on the face: rostral = 0, dorsal = 90 degrees
Z, p = rayleigh(theta)
cnt = pd.Series([L.POSNAME[x] for x in rel]).value_counts()
print(cnt.to_string())
print(f"Rayleigh Z = {Z:.2f}, p = {p:.2g}, n = {len(theta)}")
dors = sum(cnt.get(x, 0) for x in ["dorsal same-arc", "dorsal rostral", "dorsal caudal"])
vent = sum(cnt.get(x, 0) for x in ["ventral same-arc", "ventral rostral", "ventral caudal"])
print(f"every SW best at least once: {len(cnt) == 8}; most frequent: {cnt.index[0]}; ventral row {vent} vs dorsal row {dors}")
print("by set:", M2.groupby("set").apply(lambda d: pd.Series([L.POSNAME[L.relpos(w, 2)] for w in np.array(L.SWS12)[d.c_best]]).value_counts().idxmax()).to_dict())
EOF
. ../dev/bin/activate && python run.py 00_load_dev.py load2_dev.py 22_exp2_a.py 23_exp2_b.py 24_exp2_c.py 25_exp2_d.py 2>&1 | sed -n '/selective; /,$p' | grep -v "^---"
```

```
463 sets; 318 selective; 90 with a constant best-combination curve
measured: mean curve [0.861 0.515 0.53  0.551 0.563 0.567 0.577 0.607], CSI of mean curve 0.033
shuffled, aligned to measured best (a): mean curve [0.594 0.586 0.581 0.586 0.584 0.58  0.58  0.584], CSI of mean curve 0.000
shuffled, own peak (b): mean curve [0.665 0.575 0.572 0.572 0.575 0.569 0.573 0.574], CSI of mean curve 0.003
(a) shuffled first point minus mean of the other seven: 0.0114 (s.e.m. 0.0049); s.e.m. of the first point 0.0273; n = 318
                  measure  most_selective  least_selective        t   p     n
       spont, sham a (Hz)          0.8270           3.9376  -7.9501 0.0 74/78
       spont, sham b (Hz)          0.8862           3.8410  -7.8026 0.0 74/78
evoked (a): best response          0.6080           1.2423  -6.6676 0.0 79/79
    evoked (b): mean of 8          0.3064           1.0092 -10.2529 0.0 79/79
selective < 0.81: 178 | selective >= 0.81: 140 | nonselective >= 0.81: 28 | nonselective < 0.81: 117
high-rate selective, spontaneous subtracted (n = 128, sets with sham trials): mean curve [0.953 0.444 0.455 0.478 0.512 0.517 0.538 0.564]
peak minus mean of other seven: 0.451, s.e.m. 0.020, ratio 22.9
rostral within-row    150
ventral caudal         87
ventral rostral        62
ventral same-arc       61
caudal within-row      40
dorsal same-arc        26
dorsal rostral         23
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's/print(pd.DataFrame(rows).round(4).to_string(index=False))/print(pd.DataFrame(rows).to_string(index=False, float_format=lambda v: f"{v:.4g}"))/' 25_exp2_d.py && cat > 26_exp2_e.py <<'EOF'
# %% [markdown]
### fig3a-sharper-than-linear

> CW-SW combination tuning was sharper than predicted from the linear sum of single-whisker responses for nearly all units (P = 1 x 10-50, paired t-test).

# %% tags=claim:fig3a-sharper-than-linear
rows = []
for o3 in "ab":
    for o2 in "ab":
        m, l = M2[f"csi_{o3}"], M2[f"csi_lin_{o2}"]
        t = stats.ttest_rel(m, l)
        rows.append(dict(O3=o3, O2=o2, n=len(m), measured=m.mean(), linear=l.mean(), frac_above=np.mean(m > l), t=t.statistic, p=t.pvalue))
fmt = lambda v: f"{v:.4g}"
print(pd.DataFrame(rows).to_string(index=False, float_format=fmt))

# %% [markdown]
### fig3b-sharper-in-both-groups

> Measured CSI exceeded linearly predicted CSI in both combination-selective (187) and nonselective (264) units.

# %% tags=claim:fig3b-sharper-in-both-groups
rows = []
for grp, g in [("selective", M2[M2.sel]), ("nonselective", M2[~M2.sel])]:
    for o3, o2 in [("a", "a"), ("a", "b"), ("b", "a"), ("b", "b")]:
        m, l = g[f"csi_{o3}"], g[f"csi_lin_{o2}"]
        rows.append(dict(group=grp, O3=o3, O2=o2, n=len(g), measured=m.mean(), linear=l.mean(),
                         p_two_sample=stats.ttest_ind(m, l).pvalue, p_paired=stats.ttest_rel(m, l).pvalue))
print(pd.DataFrame(rows).to_string(index=False, float_format=fmt))

# %% [markdown]
### fig3b-linear-sharper-in-selective

> The linearly predicted receptive field was sharper in combination-selective than in nonselective units.

# %% tags=claim:fig3b-linear-sharper-in-selective
for o2 in "ab":
    a, b = M2.loc[M2.sel, f"csi_lin_{o2}"], M2.loc[~M2.sel, f"csi_lin_{o2}"]
    t = stats.ttest_ind(a, b)
    print(f"O2 ({o2}): linear CSI selective {a.mean():.4f} (n={len(a)}), nonselective {b.mean():.4f} (n={len(b)}), t = {t.statistic:.2f}, p = {t.pvalue:.3g}")

# %% [markdown]
### supp6-layers

> Combination selectivity existed in all layers but was stronger in L2-4 than in L5-6 (one-factor ANOVA, P = 0.0025).

# %% tags=claim:supp6-layers
print("units (sets) by layer, all responsive:", M2.layer.value_counts().to_dict(), "; expected 108 / 157 / 141 / 45")
for lab, g in [("(a) all responsive sets", M2), ("(b) selective sets", M2[M2.sel])]:
    g = g[g.layer != "outside"]
    vals = {lay: np.log10(g.loc[g.layer == lay, "csi_a"].clip(lower=1e-6)) for lay in ["L2/3", "L4", "L5", "L6"]}
    f = stats.f_oneway(*vals.values())
    print(lab, {k: (round(v.mean(), 3), len(v)) for k, v in vals.items()}, f"F = {f.statistic:.2f}, p = {f.pvalue:.3g}")
print("sets outside the layer bounds:", int((M2.layer == "outside").sum()), "; CSI = 0 sets (floored at 1e-6 for the log):", int((M2.csi_a <= 0).sum()))

# %% [markdown]
### fig4a-sw-tuned-sharper

> SW-tuned units were more sharply combination-tuned than CW-tuned units (P = 3.4 x 10-4, two-sample t-test; 169 CW-tuned, 282 SW-tuned).

# %% tags=claim:fig4a-sw-tuned-sharper
for o2 in "ab":
    cw = M2[f"cw_tuned_{o2}"].to_numpy(bool)
    a, b = M2.loc[~cw, "csi_a"], M2.loc[cw, "csi_a"]
    t = stats.ttest_ind(a, b)
    print(f"O2 ({o2}): CW-tuned {cw.sum()}, SW-tuned {(~cw).sum()}; CSI SW-tuned {a.mean():.4f}, CW-tuned {b.mean():.4f}, t = {t.statistic:.2f}, p = {t.pvalue:.3g}")

# %% [markdown]
### fig5a-global-scaling

> Across all stimuli and units, CW-SW responses at the best dt were well predicted by a 64% scaling of the linear sum of single-whisker responses (R2 = 0.90, n = 3,608 combinations).

# %% tags=claim:fig5a-global-scaling
rows = []
for o3 in "ab":
    for o2 in "ab":
        y = np.concatenate(M2[f"resp_{o3}"].to_numpy())
        x = np.concatenate(M2[f"lin_{o2}"].to_numpy())
        ok = np.isfinite(x) & np.isfinite(y)
        x, y = x[ok], y[ok]
        b = (x @ y) / (x @ x)
        sse = np.sum((y - b * x) ** 2)
        rows.append(dict(O3=o3, O2=o2, n=len(x), slope=b, R2_centred=1 - sse / np.sum((y - y.mean()) ** 2), R2_uncentred=1 - sse / np.sum(y ** 2)))
F5 = pd.DataFrame(rows)
print(F5.to_string(index=False, float_format=fmt))
print("ranges: measured", np.concatenate(M2.resp_a.to_numpy()).min().round(3), "-", np.concatenate(M2.resp_a.to_numpy()).max().round(3),
      "; linear", np.concatenate(M2.lin_a.to_numpy()).min().round(3), "-", np.concatenate(M2.lin_a.to_numpy()).max().round(3))
SLOPE = 0.64  # the paper's scaling, used by the Fig. 6 claims as the criteria say

# %% [markdown]
### fig5bc-linearity-index

> Nonoptimal combinations had a linearity index of 0.63 +- 0.003 and best combinations 0.95 +- 0.02 (P = 1.3 x 10-147, two-sample t-test).

# %% tags=claim:fig5bc-linearity-index
rows = []
for o3 in "ab":
    for o2 in "ab":
        li = [r[f"resp_{o3}"] / r[f"lin_{o2}"] for _, r in M2.iterrows()]
        best = np.array([v[c] for v, c in zip(li, M2.c_best)])
        sub = np.concatenate([np.delete(v, c) for v, c in zip(li, M2.c_best)])
        best, sub = best[np.isfinite(best)], sub[np.isfinite(sub)]
        t = stats.ttest_ind(best, sub)
        rows.append(dict(O3=o3, O2=o2, best=best.mean(), best_sem=stats.sem(best), nonopt=sub.mean(), nonopt_sem=stats.sem(sub),
                         n_best=len(best), n_nonopt=len(sub), t=t.statistic, p=t.pvalue))
print(pd.DataFrame(rows).to_string(index=False, float_format=fmt))

# %% [markdown]
### fig5c-pseudo-unit-shuffle

> Pseudo-units made by sampling eight random points from Fig. 5a had very similar linearity for their strongest and weaker responses (0.71 against 0.67), so the best-combination linearity is not a trivial consequence of response strength.

# %% tags=claim:fig5c-pseudo-unit-shuffle
rng_5c = np.random.default_rng(5)
y_all = np.concatenate(M2.resp_a.to_numpy()); x_all = np.concatenate(M2.lin_a.to_numpy())
for npu in [len(M2), 10000]:
    bl, sl = [], []
    for _ in range(npu):
        ii = rng_5c.choice(len(y_all), 8, replace=False)
        li = y_all[ii] / x_all[ii]
        c = np.argmax(y_all[ii])
        bl.append(li[c]); sl.extend(np.delete(li, c))
    print(f"{npu} pseudo-units: strongest {np.mean(bl):.3f}, remaining {np.mean(sl):.3f}")

# %% [markdown]
### fig5c-sublinear-at-all-dt

> Sublinearity for nonoptimal combinations held at all dt values, not only at the best dt.

# %% tags=claim:fig5c-sublinear-at-all-dt
peak_sub, best_li = [], []
for _, r in M2.iterrows():
    cv = CUR[(r.unit, r.set)]["curves"]
    li = cv / r.lin_a[:, None]
    peak_sub.extend(np.delete(li.max(axis=1), r.c_best))
    best_li.append(r.resp_a[r.c_best] / r.lin_a[r.c_best])
peak_sub, best_li = np.array(peak_sub), np.array(best_li)
t = stats.ttest_ind(peak_sub, best_li)
print(f"peak linearity index over dt, nonoptimal: mean {peak_sub.mean():.3f} (n={len(peak_sub)}); best combination at best dt {best_li.mean():.3f} (n={len(best_li)}); t = {t.statistic:.2f}, p = {t.pvalue:.3g}")

# %% [markdown]
### supralinear-best-8-percent

> Only 8% of units had significant supralinearity for the best combination.

# %% tags=claim:supralinear-best-8-percent
rows = []
for o3 in "ab":
    zs, dfs = [], []
    for _, r in M2.iterrows():
        d = CUR[(r.unit, r.set)]
        sm_, sv, sn = d["single_means"], d["single_vars"], d["single_n"]
        dirs = d["dirs"]
        w = L.SWS12[r.c_best]
        def m_se(wh):
            keys = [(wh, x) for x in sorted(dirs[wh])]
            mu = sm_.loc[keys].mean()
            se2 = np.mean([sv.loc[k_] / sn.loc[k_] for k_ in keys]) / len(keys)
            return mu, se2
        (mc, sc), (ms, ss) = m_se(L.CW12), m_se(w)
        mu = r[f"resp_{o3}"][r.c_best]
        zs.append((mu - (mc + ms)) / np.sqrt(sc + ss))
        near = (np.abs(d["dti"] - r.j_best) <= 5) & (d["comb"] == r.c_best)
        dfs.append(max(near.sum() - 1, 1))
    zs, dfs = np.array(zs), np.array(dfs)
    for ref, pv in [("normal", stats.norm.sf(zs)), ("t", stats.t.sf(zs, dfs))]:
        for grp, m in [("all", np.ones(len(M2), bool)), ("selective", M2.sel.to_numpy())]:
            rows.append(dict(O3=o3, reference=ref, units=grp, n=int(m.sum()), frac_supralinear=np.mean(pv[m] < 0.05)))
print(pd.DataFrame(rows).to_string(index=False, float_format=fmt))
EOF
. ../dev/bin/activate && python run.py 00_load_dev.py load2_dev.py 22_exp2_a.py 23_exp2_b.py 24_exp2_c.py 26_exp2_e.py 2>&1 | sed -n '/selective; /,$p' | grep -v "^---"
```

```
463 sets; 318 selective; 90 with a constant best-combination curve
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/scipy/_external/array_api_compat/common/_aliases.py", line 649, in finfo
    return xp.finfo(type_)
           ~~~~~~~~^^^^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/_core/getlimits.py", line 216, in __new__
    obj = object.__new__(cls)._init(dtype)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/_core/getlimits.py", line 226, in _init
    _populate_finfo_constants(self, self.dtype)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^
ValueError: data type dtype('O') not compatible with finfo

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tmp/claude-1001/nb/run.py", line 13, in <module>
    exec(compile(body, f, "exec"), ns)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "26_exp2_e.py", line 5, in <module>
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/scipy/stats/_axis_nan_policy.py", line 601, in axis_nan_policy_wrapper
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
s=open('24_exp2_c.py').read()
old='''    return pd.concat([R.reset_index(drop=True), pd.DataFrame(out)], axis=1)'''
new='''    df = pd.DataFrame(out)
    for c in ["csi_a", "csi_b", "csi_lin_a", "csi_lin_b"]:
        df[c] = df[c].astype(float)
    for c in ["c_best", "j_best", "dt_best"]:
        df[c] = df[c].astype(int)
    for c in ["best_const", "cw_tuned_a", "cw_tuned_b"]:
        df[c] = df[c].astype(bool)
    return pd.concat([R.reset_index(drop=True), df], axis=1)'''
s=s.replace(old,new); open('24_exp2_c.py','w').write(s)
EOF
. ../dev/bin/activate && python run.py 00_load_dev.py load2_dev.py 22_exp2_a.py 23_exp2_b.py 24_exp2_c.py 26_exp2_e.py 2>&1 | sed -n '/selective; /,$p' | grep -v "^---"
```

```
463 sets; 318 selective; 90 with a constant best-combination curve
O3 O2   n  measured  linear  frac_above     t         p
 a  a 463   0.08625 0.03471      0.9114 15.34 3.123e-43
 a  b 463   0.08625 0.02665       0.946 16.28 1.896e-47
 b  a 463    0.1414 0.03471      0.9784 21.55 8.523e-72
 b  b 463    0.1414 0.02665      0.9914 21.71 1.529e-72
       group O3 O2   n  measured  linear  p_two_sample  p_paired
   selective  a  a 318   0.09343 0.03985     1.381e-19 1.904e-37
   selective  a  b 318   0.09343 0.03116     1.563e-27 3.259e-40
   selective  b  a 318     0.143 0.03985     6.054e-43 9.698e-57
   selective  b  b 318     0.143 0.03116     1.188e-51  2.27e-57
nonselective  a  a 145   0.07051 0.02344     5.467e-08 7.164e-10
nonselective  a  b 145   0.07051 0.01676     4.421e-10 5.802e-11
nonselective  b  a 145    0.1378 0.02344      2.07e-18 1.155e-19
nonselective  b  b 145    0.1378 0.01676     2.276e-20 1.273e-19
O2 (a): linear CSI selective 0.0399 (n=318), nonselective 0.0234 (n=145), t = 4.00, p = 7.31e-05
O2 (b): linear CSI selective 0.0312 (n=318), nonselective 0.0168 (n=145), t = 4.68, p = 3.72e-06
units (sets) by layer, all responsive: {'L4': 159, 'L5': 147, 'L2/3': 103, 'L6': 53, 'outside': 1} ; expected 108 / 157 / 141 / 45
(a) all responsive sets {'L2/3': (np.float64(-1.13), 103), 'L4': (np.float64(-1.235), 159), 'L5': (np.float64(-1.393), 147), 'L6': (np.float64(-1.341), 53)} F = 8.22, p = 2.44e-05
(b) selective sets {'L2/3': (np.float64(-1.068), 66), 'L4': (np.float64(-1.183), 107), 'L5': (np.float64(-1.313), 112), 'L6': (np.float64(-1.255), 33)} F = 5.26, p = 0.00149
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 975,1010p paper/10.1038-s41593-019-0448-6.txt; sed -n 1440,1460p paper/10.1038-s41593-019-0448-6.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat > 27_exp2_f.py <<'EOF'
# %% [markdown]
### fig6b-best-above-worst-below-scaled

> In both combination-selective and nonselective units, the best combination exceeded the 0.64-scaled linear prediction and the worst combination fell below it.

# %% tags=claim:fig6b-best-above-worst-below-scaled
def ranked_resid(g, o3="a", o2="a"):
    res, lin_, meas_ = [], [], []
    for _, r in g.iterrows():
        o = np.argsort(-r[f"resp_{o3}"])
        res.append(r[f"resp_{o3}"][o] - SLOPE * r[f"lin_{o2}"][o])
        meas_.append(r[f"resp_{o3}"][o]); lin_.append(SLOPE * r[f"lin_{o2}"][o])
    return np.array(res), np.array(meas_), np.array(lin_)
RES = {}
for grp, g in [("selective", M2[M2.sel]), ("nonselective", M2[~M2.sel])]:
    res, me, li = ranked_resid(g)
    RES[grp] = res
    tb, tw = stats.ttest_rel(me[:, 0], li[:, 0]), stats.ttest_rel(me[:, -1], li[:, -1])
    print(f"{grp} (n={len(g)}): best {me[:, 0].mean():.3f} vs 0.64 x linear {li[:, 0].mean():.3f}, t = {tb.statistic:.2f}, p = {tb.pvalue:.3g}; "
          f"worst {me[:, -1].mean():.3f} vs {li[:, -1].mean():.3f}, t = {tw.statistic:.2f}, p = {tw.pvalue:.3g}")
    print("   mean residual by rank:", res.mean(0).round(3))

# %% [markdown]
### fig6b-enhancement-not-different

> The magnitude of combination-specific enhancement for the best combination did not differ between selective and nonselective units (P = 0.24, t-test).

# %% tags=claim:fig6b-enhancement-not-different
a, b = RES["selective"][:, 0], RES["nonselective"][:, 0]
t = stats.ttest_ind(a, b)
print(f"rank-1 residual: selective {a.mean():.4f} (n={len(a)}), nonselective {b.mean():.4f} (n={len(b)}), difference {a.mean() - b.mean():.4f}, t = {t.statistic:.2f}, p = {t.pvalue:.3g}")
for o3, o2 in [("b", "a"), ("a", "b")]:
    ra = ranked_resid(M2[M2.sel], o3, o2)[0][:, 0]; rb = ranked_resid(M2[~M2.sel], o3, o2)[0][:, 0]
    print(f"variant O3 {o3}, O2 {o2}: difference {ra.mean() - rb.mean():.4f}, p = {stats.ttest_ind(ra, rb).pvalue:.3g}")

# %% [markdown]
### fig6b-suppression-greater-selective

> Suppression of the two weakest CW-SW combinations was modestly greater in selective units (P = 0.001 and P = 0.002, two-sample t-tests, Bonferroni).

# %% tags=claim:fig6b-suppression-greater-selective
for rank in [7, 8]:
    a, b = RES["selective"][:, rank - 1], RES["nonselective"][:, rank - 1]
    t = stats.ttest_ind(a, b)
    print(f"rank {rank}: selective {a.mean():.4f}, nonselective {b.mean():.4f}, t = {t.statistic:.2f}, p = {t.pvalue:.3g}, "
          f"Bonferroni x8 {min(1, 8 * t.pvalue):.3g}, x2 {min(1, 2 * t.pvalue):.3g}")

# %% [markdown]
### fig6c-enhancement-strongest-sw

> Combination-selective units nonlinearly enhanced combinations involving the strongest single SW (P = 1.2 x 10-8, one-factor ANOVA), while nonselective units showed an opposite, much weaker trend (P = 0.03).

# %% tags=claim:fig6c-enhancement-strongest-sw
for grp, g in [("selective", M2[M2.sel]), ("nonselective", M2[~M2.sel])]:
    byrank = []
    for _, r in g.iterrows():
        sw_resp = r.sing_a[np.array(L.SWS12) - 1]
        o = np.argsort(-sw_resp)
        byrank.append((r.resp_a - SLOPE * r.lin_a)[o])
    byrank = np.array(byrank)
    f = stats.f_oneway(*byrank.T)
    m = byrank.mean(0)
    print(f"{grp} (n={len(g)}): mean residual by SW rank {m.round(4)}; ANOVA F = {f.statistic:.2f}, p = {f.pvalue:.3g}; "
          f"rank 1 largest {m.argmax() == 0}; rank 1 below mean of 2-8: {m[0] < m[1:].mean()}")

# %% [markdown]
### fig7a-dt-half-width

> For their best combinations, combination-selective units had sharp dt tuning with an average half-width of about 10 ms around the best dt; suboptimal combinations had weaker, broader dt tuning.

# %% tags=claim:fig7a-dt-half-width
lags = np.arange(-100, 101)
def aligned(g):
    best, sub = [], []
    for _, r in g.iterrows():
        cv = CUR[(r.unit, r.set)]["curves"] / CUR[(r.unit, r.set)]["curves"].max()
        A = np.full((8, len(lags)), np.nan)
        A[:, 100 - r.j_best: 100 - r.j_best + 101] = cv
        best.append(A[r.c_best]); sub.extend(np.delete(A, r.c_best, axis=0))
    return np.array(best), np.array(sub)
def halfwidth(curve, mode):
    c = curve[np.isfinite(curve)] if False else curve
    pk = c[100]
    lvl = (pk + np.nanmin(c)) / 2 if mode == "halfway" else pk / 2
    left = np.where(np.isfinite(c[:100]) & (c[:100] <= lvl))[0]
    right = np.where(np.isfinite(c[101:]) & (c[101:] <= lvl))[0]
    if not len(left) or not len(right):
        return np.nan
    return ((100 - left.max()) + (right.min() + 1)) / 2
for lab, g in [("selective, all", M2[M2.sel]), ("selective, best curve dt-modulated", M2[M2.sel & ~M2.best_const])]:
    B, S = aligned(g)
    mb, ms = np.nanmean(B, 0), np.nanmean(S, 0)
    hw_a, hw_c = halfwidth(mb, "halfway"), halfwidth(mb, "half")
    hw_b = np.nanmean([halfwidth(b, "halfway") for b in B])
    print(f"{lab} (n={len(g)}): half-width (a) {hw_a}, (b) {hw_b:.1f} (units with a defined value: {np.sum(np.isfinite([halfwidth(b, 'halfway') for b in B]))}), (c) {hw_c} ms")
    print(f"   suboptimal mean at best dt {ms[100]:.3f} vs best {mb[100]:.3f}; suboptimal half-width (a) {halfwidth(ms / ms[100] * ms[100], 'halfway')}, (c) {halfwidth(ms, 'half')}")
    print("   mean best curve at lags -30..30 step 5:", mb[70:131:5].round(3))

# %% [markdown]
### fig7b-inbound-best-outbound-suboptimal

> Mean dt tuning had a minimum at -10 ms; best combinations evoked maximal responses at -30 to -50 ms (SW leads CW, inbound), suboptimal combinations at +30 to +50 ms (outbound).

# %% tags=claim:fig7b-inbound-best-outbound-suboptimal
for zmode in ["unit", "curve"]:
    zb, zs = [], []
    for _, r in M2[M2.sel].iterrows():
        cv = CUR[(r.unit, r.set)]["curves"]
        if zmode == "unit":
            z_ = (cv - cv.mean()) / cv.std() if cv.std() > 0 else cv * 0
        else:
            sd = cv.std(axis=1, keepdims=True)
            z_ = np.where(sd > 0, (cv - cv.mean(axis=1, keepdims=True)) / np.where(sd > 0, sd, 1), 0)
        zb.append(z_[r.c_best]); zs.extend(np.delete(z_, r.c_best, axis=0))
    mb, ms = np.mean(zb, 0), np.mean(zs, 0)
    dts = L.DT_GRID
    print(f"z-scored per {zmode}: best n={len(zb)}, suboptimal n={len(zs)}")
    print(f"   best peaks at {dts[mb.argmax()]} ms, minimum at {dts[mb.argmin()]} ms; suboptimal peaks at {dts[ms.argmax()]} ms, minimum at {dts[ms.argmin()]} ms; "
          f"pooled minimum at {dts[np.mean(zb + zs, 0).argmin()]} ms; suboptimal below best at the best peak: {ms[mb.argmax()] < mb.max()}")
    print("   best mean every 10 ms:", mb[::10].round(2), "\n   suboptimal mean every 10 ms:", ms[::10].round(2))
EOF
. ../dev/bin/activate && python run.py 00_load_dev.py load2_dev.py 22_exp2_a.py 23_exp2_b.py 24_exp2_c.py 27_exp2_f.py 2>&1 | sed -n '/selective; /,$p' | grep -v "^---"
```

```
463 sets; 318 selective; 90 with a constant best-combination curve
Traceback (most recent call last):
  File "/tmp/claude-1001/nb/run.py", line 13, in <module>
    exec(compile(body, f, "exec"), ns)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "27_exp2_f.py", line 10, in <module>
    o = np.argsort(-r[f"resp_{o3}"])
              ^^^^^^^^^^^^^^^
  File "27_exp2_f.py", line 5, in ranked_resid
NameError: name 'SLOPE' is not defined
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's/^def ranked_resid(g, o3="a", o2="a"):/SLOPE = 0.64  # the paper'"'"'s global scaling (Results, Fig. 6), as the criteria say\ndef ranked_resid(g, o3="a", o2="a"):/' 27_exp2_f.py && . ../dev/bin/activate && python run.py 00_load_dev.py load2_dev.py 22_exp2_a.py 23_exp2_b.py 24_exp2_c.py 27_exp2_f.py 2>&1 | sed -n '/selective; /,$p' | grep -v "^---"
```

```
463 sets; 318 selective; 90 with a constant best-combination curve
selective (n=318): best 0.861 vs 0.64 x linear 0.704, t = 14.71, p = 1.06e-37; worst 0.449 vs 0.529, t = -12.44, p = 3.39e-29
   mean residual by rank: [ 0.157  0.043  0.02   0.004 -0.013 -0.023 -0.047 -0.08 ]
nonselective (n=145): best 0.514 vs 0.64 x linear 0.402, t = 10.40, p = 3.08e-19; worst 0.315 vs 0.353, t = -5.53, p = 1.49e-07
   mean residual by rank: [ 0.112  0.043  0.026  0.014  0.002 -0.005 -0.017 -0.038]
rank-1 residual: selective 0.1572 (n=318), nonselective 0.1119 (n=145), difference 0.0453, t = 2.60, p = 0.00957
variant O3 b, O2 a: difference 0.0475, p = 0.0117
variant O3 a, O2 b: difference 0.0571, p = 0.00404
rank 7: selective -0.0467, nonselective -0.0165, t = -3.29, p = 0.00106, Bonferroni x8 0.00852, x2 0.00213
rank 8: selective -0.0796, nonselective -0.0382, t = -3.92, p = 0.000103, Bonferroni x8 0.000825, x2 0.000206
selective (n=318): mean residual by SW rank [ 0.0533  0.0268  0.0013 -0.005  -0.0153 -0.0046 -0.0022  0.0067]; ANOVA F = 7.91, p = 1.61e-09; rank 1 largest True; rank 1 below mean of 2-8: False
nonselective (n=145): mean residual by SW rank [0.0043 0.0119 0.0074 0.0175 0.0126 0.021  0.0296 0.0331]; ANOVA F = 1.47, p = 0.172; rank 1 largest False; rank 1 below mean of 2-8: True
selective, all (n=318): half-width (a) 16.5, (b) 14.9 (units with a defined value: 74), (c) nan ms
   suboptimal mean at best dt 0.613 vs best 1.000; suboptimal half-width (a) 24.5, (c) nan
   mean best curve at lags -30..30 step 5: [0.737 0.744 0.768 0.792 0.839 0.925 1.    0.948 0.888 0.854 0.831 0.821
 0.81 ]
selective, best curve dt-modulated (n=248): half-width (a) 11.5, (b) 14.9 (units with a defined value: 74), (c) nan ms
   suboptimal mean at best dt 0.605 vs best 1.000; suboptimal half-width (a) nan, (c) nan
   mean best curve at lags -30..30 step 5: [0.737 0.744 0.768 0.792 0.839 0.925 1.    0.93  0.848 0.799 0.765 0.748
 0.728]
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat > 28_exp2_g.py <<'EOF'
# %% [markdown]
### fig7c-pca

> Of the dt tuning curves, 357 of best (79%) and 1,247 of suboptimal combinations (40%) were significantly modulated; three PCs captured 75% of their variance, PC1 sigmoidal about 0 ms (order) and PC2 U-shaped (speed).

# %% tags=claim:fig7c-pca
rows_pc = []
for _, r in M2.iterrows():
    d = CUR[(r.unit, r.set)]
    for c in range(8):
        if d["status"][c] == "modulated":
            cv = d["curves"][c]
            rows_pc.append(dict(unit=r.unit, set=r.set, sel=r.sel, best=c == r.c_best, z=(cv - cv.mean()) / cv.std()))
PC = pd.DataFrame(rows_pc)
Z = np.vstack(PC.z.to_numpy())
nb_, ns_ = int(PC.best.sum()), int((~PC.best).sum())
print(f"modulated best curves {nb_} of {len(M2)} ({nb_ / len(M2):.2f}); suboptimal {ns_} of {7 * len(M2)} ({ns_ / (7 * len(M2)):.2f})")
Zc = Z - Z.mean(0)
u_, s_, vt = np.linalg.svd(Zc, full_matrices=False)
ev = s_ ** 2 / np.sum(s_ ** 2)
print("variance explained by PCs 1-5:", ev[:5].round(3), "; first three:", ev[:3].sum().round(3))
dts = L.DT_GRID
pc1 = vt[0] * (1 if vt[0][dts > 0].mean() > vt[0][dts < 0].mean() else -1)
pc2 = vt[1]
sc1 = Zc @ pc1
PC["pc1"] = sc1; PC["pc2"] = Zc @ pc2; PC["pc3"] = Zc @ vt[2]
zero_cross = dts[np.where(np.diff(np.sign(pc1)) != 0)[0]]
print("PC1 sign changes at dt:", zero_cross, "; PC1 every 10 ms:", pc1[::10].round(3))
far, near = pc2[np.abs(dts) > 30].mean(), pc2[np.abs(dts) < 10].mean()
print(f"PC2 mean |dt| > 30: {far:.3f}, |dt| < 10: {near:.3f} (opposite signs: {np.sign(far) != np.sign(near)}); PC2 every 10 ms:", pc2[::10].round(3))

# %% [markdown]
### fig7e-pc1-best-suboptimal

> In combination-selective cells, best combinations had negative PC1 weights and suboptimal combinations positive (P = 5.7 x 10-16, t-test), an inbound order preference nearly absent in nonselective cells; PC2 and PC3 weights did not differ across cell or stimulus types.

# %% tags=claim:fig7e-pc1-best-suboptimal
g = PC.groupby(["sel", "best"]).pc1.agg(["mean", "size"])
print(g)
sb, ss = PC.loc[PC.sel & PC.best, "pc1"], PC.loc[PC.sel & ~PC.best, "pc1"]
nb, ns = PC.loc[~PC.sel & PC.best, "pc1"], PC.loc[~PC.sel & ~PC.best, "pc1"]
t = stats.ttest_ind(sb, ss)
print(f"selective best vs suboptimal: t = {t.statistic:.2f}, p = {t.pvalue:.3g}; difference {sb.mean() - ss.mean():.3f}; "
      f"nonselective difference {nb.mean() - ns.mean():.3f} (ratio {(nb.mean() - ns.mean()) / (sb.mean() - ss.mean()):.2f}), p = {stats.ttest_ind(nb, ns).pvalue:.3g}")
for pc in ["pc2", "pc3"]:
    grps = {"sel best": PC.loc[PC.sel & PC.best, pc], "nonsel best": PC.loc[~PC.sel & PC.best, pc], "all suboptimal": PC.loc[~PC.best, pc]}
    ks = list(grps)
    out = [f"{ks[i]} vs {ks[j]}: p = {stats.ttest_ind(grps[ks[i]], grps[ks[j]]).pvalue:.3g}" for i in range(3) for j in range(i + 1, 3)]
    print(pc, {k: round(v.mean(), 3) for k, v in grps.items()}, "|", "; ".join(out))

# %% [markdown]
### fig7f-inbound-sharper

> Combination-selective units preferring inbound order (best dt < 0, n = 121) were more sharply tuned than those preferring outbound order (n = 56; P = 0.03) and had better alignment of nonlinear and linear components (P = 0.01).

# %% tags=claim:fig7f-inbound-sharper
sel = M2[M2.sel].copy()
sel["align"] = [np.corrcoef(r.lin_a, r.resp_a - SLOPE * r.lin_a)[0, 1] for _, r in sel.iterrows()]
rows = []
for lab, g in [("(a) dt = 0 excluded", sel[sel.dt_best != 0]), ("(b) dt = 0 with outbound", sel),
               ("(c)+(a) constant best curve and dt = 0 excluded", sel[~sel.best_const & (sel.dt_best != 0)]),
               ("(c)+(b) constant best curve excluded", sel[~sel.best_const])]:
    inb, outb = g[g.dt_best < 0], g[g.dt_best >= 0]
    t1, t2 = stats.ttest_ind(inb.csi_a, outb.csi_a), stats.ttest_ind(inb.align, outb.align)
    rows.append(dict(reading=lab, inbound=len(inb), outbound=len(outb), csi_in=inb.csi_a.mean(), csi_out=outb.csi_a.mean(), p_csi=t1.pvalue,
                     align_in=inb.align.mean(), align_out=outb.align.mean(), p_align=t2.pvalue))
print(pd.DataFrame(rows).to_string(index=False, float_format=fmt))
print("selective sets with a constant best-combination curve (best dt falls on -50 ms by the tie):", int(sel.best_const.sum()))
EOF
. ../dev/bin/activate && python run.py 00_load_dev.py load2_dev.py 22_exp2_a.py 23_exp2_b.py 24_exp2_c.py 26_exp2_e.py 27_exp2_f.py 28_exp2_g.py 2>&1 | sed -n '/fig7c/,$p;/modulated best/,$p' | grep -v "^---"
```

```
modulated best curves 373 of 463 (0.81); suboptimal 1204 of 3241 (0.37)
variance explained by PCs 1-5: [0.447 0.28  0.109 0.06  0.032] ; first three: 0.836
PC1 sign changes at dt: [0] ; PC1 every 10 ms: [-0.129 -0.127 -0.114 -0.089 -0.05  -0.004  0.042  0.085  0.115  0.134
  0.144]
PC2 mean |dt| > 30: 0.107, |dt| < 10: -0.133 (opposite signs: True); PC2 every 10 ms: [ 0.152  0.111  0.044 -0.037 -0.108 -0.141 -0.119 -0.05   0.034  0.105
  0.151]
                 mean  size
                 mean  size
sel   best                 
sel   best                 
False False  1.232686   366
False False  1.232686   366
      True  -0.284283   125
      True  -0.284283   125
True  False  0.206604   838
True  False  0.206604   838
      True  -2.374038   248
      True  -2.374038   248
selective best vs suboptimal: t = -5.38, p = 8.89e-08; difference -2.581; nonselective difference -1.517 (ratio 0.59), p = 0.0162
selective best vs suboptimal: t = -5.38, p = 8.89e-08; difference -2.581; nonselective difference -1.517 (ratio 0.59), p = 0.0162
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's/sel\["align"\]/sel["align_idx"]/; s/inb.align, outb.align/inb["align_idx"], outb["align_idx"]/; s/align_in=inb.align.mean(), align_out=outb.align.mean()/align_in=inb["align_idx"].mean(), align_out=outb["align_idx"].mean()/' 28_exp2_g.py && . ../dev/bin/activate && python run.py 00_load_dev.py load2_dev.py 22_exp2_a.py 23_exp2_b.py 24_exp2_c.py 26_exp2_e.py 27_exp2_f.py 28_exp2_g.py 2>&1 | sed -n '/^ *reading/,$p' | grep -v "^---"; date -u
```

```
reading  inbound  outbound  csi_in  csi_out   p_csi  align_in  align_out   p_align
                            (a) dt = 0 excluded      204       112 0.09963  0.08258  0.1118    0.2412    0.03755 4.751e-05
                       (b) dt = 0 with outbound      204       114 0.09963  0.08235  0.1041    0.2412    0.03309 2.841e-05
(c)+(a) constant best curve and dt = 0 excluded      134       112  0.1086  0.08258 0.03009    0.3194    0.03755 1.305e-07
           (c)+(b) constant best curve excluded      134       114  0.1086  0.08235 0.02735    0.3194    0.03309 6.845e-08
selective sets with a constant best-combination curve (best dt falls on -50 ms by the tie): 70
Thu Nov 12 17:52:35 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> entries/laboy-juarez-2019/lj2019.py <<'EOF'


# ---------------------------------------------------------------- decoders (Methods, "Neural decoders")

def fit_logistic_1d(x, Y, iters=1000, ridge=1e-4, tol=1e-8):
    """Logistic regressions of each column of the binary matrix Y on one feature x, by Newton's method.

    "Logistic functions were fit over 1,000 iterations" (Methods) is read as the iteration limit
    (claims file, O6). The small ridge keeps the fit finite when a class is perfectly separated
    (a standard choice; it cannot change which class wins except at exact ties).
    Returns params (K, 2): intercept and slope.
    """
    x = np.asarray(x, float)
    X = np.c_[np.ones_like(x), x]
    K = Y.shape[1]
    w = np.zeros((K, 2))
    for _ in range(iters):
        eta = X @ w.T  # (n, K)
        p = 1 / (1 + np.exp(-eta))
        g = X.T @ (Y - p) - ridge * w.T  # (2, K)
        Wt = p * (1 - p)
        H00 = Wt.sum(0) + ridge
        H01 = (Wt * x[:, None]).sum(0)
        H11 = (Wt * x[:, None] ** 2).sum(0) + ridge
        det = H00 * H11 - H01 ** 2
        d0 = (H11 * g[0] - H01 * g[1]) / det
        d1 = (-H01 * g[0] + H00 * g[1]) / det
        w[:, 0] += d0
        w[:, 1] += d1
        if np.max(np.abs(np.r_[d0, d1])) < tol:
            break
    return w


def heldout_prob_rows(x, y, ncls, rng, folds=10):
    """Tenfold cross-validated one-versus-all probabilities for each trial (Methods).

    x: counts, y: class labels 0..ncls-1. Each trial's row comes from the classifiers fitted on the
    other nine folds.
    """
    x = np.asarray(x, float)
    out = np.zeros((len(x), ncls))
    perm = rng.permutation(len(x))
    fold = np.empty(len(x), int)
    fold[perm] = np.arange(len(x)) % folds
    for f in range(folds):
        tr = fold != f
        Y = (y[tr][:, None] == np.arange(ncls)[None, :]).astype(float)
        w = fit_logistic_1d(x[tr], Y)
        out[~tr] = 1 / (1 + np.exp(-(w[:, 0][None, :] + np.outer(x[~tr], w[:, 1]))))
    return out


class Pool:
    """Held-out probability rows of many units, for population decoding by summed probabilities."""

    def __init__(self, probs, labels, ncls):
        self.ncls = ncls
        rows, off, cnt = [], [], []
        start = 0
        for P, lab in zip(probs, labels):
            o, c = [], []
            for k in range(ncls):
                ii = np.where(lab == k)[0]
                rows.append(P[ii])
                o.append(start)
                c.append(len(ii))
                start += len(ii)
            off.append(o)
            cnt.append(c)
        self.P = np.vstack(rows)
        self.off = np.array(off)
        self.cnt = np.array(cnt)

    def accuracy(self, N, n_ens, rng, units=None, chunk=250):
        """Per-ensemble, per-class accuracy (n_ens, ncls); units sampled with replacement."""
        pool = np.arange(len(self.off)) if units is None else np.asarray(units)
        res = []
        for s in range(0, n_ens, chunk):
            m = min(chunk, n_ens - s)
            u = pool[rng.integers(0, len(pool), (m, N))]  # (m, N)
            r = rng.random((m, N, self.ncls))
            idx = self.off[u] + np.minimum((r * self.cnt[u]).astype(int), self.cnt[u] - 1)  # (m, N, ncls)
            tot = self.P[idx].sum(axis=1)  # (m, ncls_true, ncls_prob)
            res.append(np.argmax(tot, axis=2) == np.arange(self.ncls)[None, :])
        return np.vstack(res)
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat > 29_exp2_dec.py <<'EOF'
# %% [markdown]
### Decoders

Per unit (a responsive set), one-versus-all logistic classifiers of combination identity on the single-trial count, trials within +-5 ms of the unit's best dt, with tenfold cross-validated held-out probabilities; ensembles of N units drawn with replacement, one held-out trial per unit per combination (O6), and the combination with the largest summed probability is the answer. Linear-prediction decoders use counts made by adding a single-trial CW count and a single-trial SW count drawn from the single-whisker trials in the set's directions (Methods, "Neural decoders"). Combinations are identified by SW face position (O5). Sets lacking trials of some combination in the window are dropped (counted below).

# %%
t0 = time.time()
rng_dec = np.random.default_rng(3)
def unit_trials(r, window=None):
    d = CUR[(r.unit, r.set)]
    if window is None:
        m = np.abs(d["dti"] - r.j_best) <= 5
    else:
        m = (d["dti"] - 50 >= window[0]) & (d["dti"] - 50 <= window[1])
    return d["y"][m], d["comb"][m]
def lin_trials(r, labels, rng):
    """Linearly predicted single-trial counts: a CW single-trial count plus a SW single-trial count."""
    d = CUR[(r.unit, r.set)]
    tab = T2[r.recording]
    sing = tab[tab.kind == "single"]
    x = np.zeros(len(labels))
    cwv = sing.loc[(sing.a == L.CW12) & sing.da.isin(list(d["dirs"][L.CW12])), f"c{r.unit}"].to_numpy()
    for k in range(8):
        w = L.SWS12[k]
        swv = sing.loc[(sing.a == w) & sing.da.isin(list(d["dirs"][w])), f"c{r.unit}"].to_numpy()
        ii = np.where(labels == k)[0]
        x[ii] = rng.choice(cwv, len(ii)) + rng.choice(swv, len(ii))
    return x
DEC, DECL, dropped = {}, {}, 0
for i, r in M2.iterrows():
    x, y = unit_trials(r)
    if len(np.unique(y)) < 8:
        dropped += 1
        continue
    DEC[i] = (L.heldout_prob_rows(x, y, 8, rng_dec), y)
    xl = lin_trials(r, y, rng_dec)
    DECL[i] = (L.heldout_prob_rows(xl, y, 8, rng_dec), y)
print(f"classifiers for {len(DEC)} sets ({dropped} dropped) in {time.time() - t0:.0f} s")
ids = np.array(list(DEC))
POOL = L.Pool([DEC[i][0] for i in ids], [DEC[i][1] for i in ids], 8)
POOLL = L.Pool([DECL[i][0] for i in ids], [DECL[i][1] for i in ids], 8)
pos_of = {i: j for j, i in enumerate(ids)}
def members(mask):
    return np.array([pos_of[i] for i in M2.index[mask] if i in pos_of])
SEL_IDX = members(M2.sel.to_numpy())

# %% [markdown]
### fig3e-identity-decoder

> A population decoder of CW-SW combination identity from single-trial counts reached 42% accuracy for 187 selective units (chance 12.5%), 82% for the rostral within-row SW and 23 to 28% for the three dorsal-row SWs, and was weaker on linearly predicted counts.

# %% tags=claim:fig3e-identity-decoder
rng_3e = np.random.default_rng(31)
names = [L.POSNAME[L.relpos(w, 2)] for w in L.SWS12]
for N in [10, 50, 100, 187, len(SEL_IDX)]:
    acc = POOL.accuracy(N, 2500, rng_3e, SEL_IDX)
    accl = POOLL.accuracy(N, 2500, rng_3e, SEL_IDX)
    m, ml = acc.mean(1), accl.mean(1)
    print(f"N = {N}: measured {m.mean():.3f} (s.d. {m.std():.3f}); linear prediction {ml.mean():.3f} (s.d. {ml.std():.3f}); "
          f"difference {m.mean() - ml.mean():.3f} vs sum of s.d. {m.std() + ml.std():.3f}")
    if N == 187:
        print("   per combination at N = 187:", dict(zip(names, acc.mean(0).round(3))))
print("selective sets in the pool:", len(SEL_IDX), "; chance 0.125")

# %% [markdown]
### fig3g-binary-decoder

> A binary decoder discriminating each unit's best CW-SW combination from suboptimal combinations reached 70% accuracy for 10 neurons and over 90% for 100.

# %% tags=claim:fig3g-binary-decoder
rng_3g = np.random.default_rng(32)
def binary_pool(rows_, mode, rng):
    probs, labs = [], []
    for i, r in rows_.iterrows():
        x, y = unit_trials(r)
        best = y == r.c_best
        if mode == "a":  # suboptimal trials pooled over the seven, as many as best trials
            sub = rng.choice(np.where(~best)[0], best.sum(), replace=best.sum() > (~best).sum())
        else:  # one suboptimal combination drawn at random
            c2 = rng.choice([c for c in range(8) if c != r.c_best])
            sub = np.where(y == c2)[0]
        ii = np.r_[np.where(best)[0], sub]
        lab = np.r_[np.ones(best.sum(), int), np.zeros(len(sub), int)]
        P = L.heldout_prob_rows(x[ii], lab, 2, rng)
        probs.append(P); labs.append(lab)
    return L.Pool(probs, labs, 2)
rows = []
for units_lab, rows_ in [("(c) selective", M2[M2.sel]), ("(d) all", M2)]:
    for mode in "ab":
        pool = binary_pool(rows_, mode, rng_3g)
        r_ = dict(units=units_lab, suboptimal=mode, n_units=len(rows_))
        for N in [10, 100]:
            acc = pool.accuracy(N, 2500, rng_3g).mean(1)
            r_[f"N{N}"] = acc.mean()
        rows.append(r_)
print(pd.DataFrame(rows).to_string(index=False, float_format=fmt))

# %% [markdown]
### fig4c-sw-tuned-decoding

> Combination identity was decoded from SW-tuned units more accurately and efficiently than from CW-tuned units, and decoding from CW-tuned units was still above chance.

# %% tags=claim:fig4c-sw-tuned-decoding
rng_4c = np.random.default_rng(4)
rows = []
for lab, base in [("(a) selective", M2.sel.to_numpy()), ("(b) all", np.ones(len(M2), bool))]:
    for grp, gm in [("SW-tuned", ~M2.cw_tuned_a.to_numpy()), ("CW-tuned", M2.cw_tuned_a.to_numpy())]:
        idx = members(base & gm)
        r_ = dict(units=lab, group=grp, n=len(idx))
        for N in [10, 25, 50, 100, 150]:
            acc = POOL.accuracy(N, 2500, rng_4c, idx).mean(1)
            r_[f"N{N}"] = acc.mean()
            if N == 150:
                r_["sd150"] = acc.std()
        rows.append(r_)
print(pd.DataFrame(rows).to_string(index=False, float_format=fmt))

# %% [markdown]
### fig7g-inbound-decoding

> Spatial combination decoding was better for inbound-order stimuli than for outbound-order stimuli.

# %% tags=claim:fig7g-inbound-decoding
rng_7g = np.random.default_rng(7)
ranges = [(-50, -41), (-40, -31), (-30, -21), (-20, -11), (-10, -1), (0, 9), (10, 19), (20, 29), (30, 39), (41, 50)]
out7 = {}
for rg in ranges:
    probs, labs, keep = [], [], []
    for i, r in M2[M2.sel].iterrows():
        x, y = unit_trials(r, window=rg)
        if len(np.unique(y)) < 8:
            continue
        probs.append(L.heldout_prob_rows(x, y, 8, rng_7g)); labs.append(y); keep.append(i)
    pool = L.Pool(probs, labs, 8)
    keep = np.array(keep)
    cw = M2.loc[keep, "cw_tuned_a"].to_numpy()
    res = {}
    for lab, N, units in [("(a) N=187", 187, None), ("(b) N=100", 100, None),
                          ("(c) CW-tuned N=100", 100, np.where(cw)[0]), ("(c) SW-tuned N=100", 100, np.where(~cw)[0])]:
        acc = pool.accuracy(N, 1000, rng_7g, units).mean(1)
        res[lab] = (acc.mean(), acc.std())
    out7[rg] = res
tab7 = pd.DataFrame({str(rg): {k: v[0] for k, v in res.items()} for rg, res in out7.items()}).T
print(tab7.round(3).to_string())
for col in tab7.columns:
    neg, pos = tab7[col].iloc[:5].mean(), tab7[col].iloc[5:].mean()
    sd = np.mean([out7[rg][col][1] for rg in ranges])
    print(f"{col}: mean over negative ranges {neg:.3f}, over [0, 9] and up {pos:.3f}, difference {neg - pos:.3f}, mean bootstrap s.d. {sd:.3f}")
print("note: the range [40, 40] is dropped by the Fig. 7g bins ([31, 40] would be next); the paper's ten ranges are used as the claims file gives them")

# %% [markdown]
### supp8-order-decoding

> A population decoder of sequence order (dt in -50 to -10 against +10 to +50 ms) from best-combination responses was about 65% correct for 100 units, against chance of 50%.

# %% tags=claim:supp8-order-decoding
rng_s8 = np.random.default_rng(8)
for lab, rows_ in [("(a) selective", M2[M2.sel]), ("(b) all", M2)]:
    probs, labs = [], []
    for i, r in rows_.iterrows():
        d = CUR[(r.unit, r.set)]
        dt_ = d["dti"] - 50
        m = (d["comb"] == r.c_best) & (np.abs(dt_) >= 10)
        lab_ = (dt_[m] > 0).astype(int)
        probs.append(L.heldout_prob_rows(d["y"][m], lab_, 2, rng_s8)); labs.append(lab_)
    pool = L.Pool(probs, labs, 2)
    for N in [10, 100]:
        acc = pool.accuracy(N, 2500, rng_s8).mean(1)
        print(f"{lab}, N = {N}: accuracy {acc.mean():.3f} (s.d. {acc.std():.3f}); chance 0.5")
print(f"decoders: {time.time() - t0:.0f} s")
EOF
sed -i 's/^    print(f"   suboptimal mean at best dt {ms\[100\]:.3f} vs best {mb\[100\]:.3f}; suboptimal half-width (a) {halfwidth(ms \/ ms\[100\] \* ms\[100\], .halfway.)}, (c) {halfwidth(ms, .half.)}")/    print(f"   suboptimal mean at best dt {ms[100]:.3f} vs best {mb[100]:.3f}; suboptimal half-width (a) {halfwidth(ms, \"halfway\")}, (c) {halfwidth(ms, \"half\")} (nan: the curve does not fall to the level within +-100 ms)")/' 27_exp2_f.py; grep -n "suboptimal half-width" 27_exp2_f.py | head -2
. ../dev/bin/activate && python run.py 00_load_dev.py load2_dev.py 22_exp2_a.py 23_exp2_b.py 24_exp2_c.py 26_exp2_e.py 29_exp2_dec.py 2>&1 | sed -n '/classifiers for/,$p' | grep -v "^---"; date -u
```

```
97:    print(f"   suboptimal mean at best dt {ms[100]:.3f} vs best {mb[100]:.3f}; suboptimal half-width (a) {halfwidth(ms, "halfway")}, (c) {halfwidth(ms, "half")} (nan: the curve does not fall to the level within +-100 ms)")
classifiers for 463 sets (0 dropped) in 5 s
N = 10: measured 0.135 (s.d. 0.100); linear prediction 0.123 (s.d. 0.093); difference 0.011 vs sum of s.d. 0.193
N = 50: measured 0.148 (s.d. 0.079); linear prediction 0.130 (s.d. 0.074); difference 0.018 vs sum of s.d. 0.153
N = 100: measured 0.145 (s.d. 0.064); linear prediction 0.128 (s.d. 0.053); difference 0.017 vs sum of s.d. 0.116
N = 187: measured 0.135 (s.d. 0.041); linear prediction 0.127 (s.d. 0.030); difference 0.008 vs sum of s.d. 0.072
   per combination at N = 187: {'dorsal caudal': np.float64(0.0), 'caudal within-row': np.float64(0.0), 'ventral caudal': np.float64(0.02), 'dorsal same-arc': np.float64(0.034), 'ventral same-arc': np.float64(0.039), 'dorsal rostral': np.float64(0.0), 'rostral within-row': np.float64(0.986), 'ventral rostral': np.float64(0.002)}
N = 318: measured 0.129 (s.d. 0.024); linear prediction 0.125 (s.d. 0.012); difference 0.004 vs sum of s.d. 0.036
selective sets in the pool: 318 ; chance 0.125
        units suboptimal  n_units    N10   N100
(c) selective          a      318 0.6088  0.817
(c) selective          b      318 0.6158  0.818
      (d) all          a      463 0.5906 0.7626
      (d) all          b      463 0.5854 0.7474
        units    group   n    N10    N25    N50   N100   N150   sd150
(a) selective SW-tuned 224 0.1399  0.149 0.1487 0.1414 0.1365 0.04038
(a) selective CW-tuned  94 0.1221 0.1313 0.1407   0.15 0.1553 0.07457
      (b) all SW-tuned 289 0.1303 0.1438  0.142 0.1391 0.1354  0.0399
      (b) all CW-tuned 174  0.114 0.1188 0.1225  0.128 0.1317 0.06138
            (a) N=187  (b) N=100  (c) CW-tuned N=100  (c) SW-tuned N=100
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
s=open('29_exp2_dec.py').read()
old='''print("selective sets in the pool:", len(SEL_IDX), "; chance 0.125")'''
new='''print("selective sets in the pool:", len(SEL_IDX), "; chance 0.125")
single = np.array([np.mean(np.argmax(DEC[i][0], 1) == DEC[i][1]) for i in ids[SEL_IDX]])
print(f"single-unit held-out accuracy (own argmax), selective sets: mean {single.mean():.3f}, range {single.min():.3f} to {single.max():.3f}")
print("best combination of the selective sets by face position:", pd.Series(np.array(names)[M2.loc[M2.sel, "c_best"]]).value_counts().to_dict())'''
s=s.replace(old,new); open('29_exp2_dec.py','w').write(s)
EOF
cat > 30_exp3.py <<'EOF'
# %% [markdown]
## Experiment 3 (awake mice)

Epochs are aligned to the first deflection (data check). The files hold no lick times and no Go or No-go labels, so the exclusion of epochs within 200 ms of a lick (Methods) cannot be applied: every epoch is used. A variant drops, per unit, the epochs whose spike list holds a time after 300 ms (see the data check; what these are is not documented). Sham reading (a) is the 0 to 125 ms window of sham epochs; (b) the whole 300 ms sham epoch, scaled.

# %%
def exp3_table(U, T, drop_late=False):
    rows, seqs = [], {}
    for rec, tab in T.items():
        for k in U.loc[U.recording == rec, "unit"]:
            t_ = tab[tab[f"o{k}"] == 0] if drop_late else tab
            r = dict(unit=k, recording=rec)
            for sr in "ab":
                r[f"p_resp_{sr}"] = L.lrt_responsive(t_, k, (t_.kind == "single").to_numpy(), sr, 300.0)[1]
                r[f"spont_{sr}"] = L.spont_rate(t_, k, sr, 300.0)
            sing = t_[t_.kind == "single"].groupby("a")[f"c{k}"].mean()
            for w in range(1, 10):
                r[f"s{w}"] = sing.loc[w]
            rows.append(r)
            seqs[k] = t_[t_.kind.isin(["cwsw", "swsw"])].groupby(["kind", "a", "b", "dt"])[f"c{k}"].mean()
    df = U[["unit", "file", "recording", "animal"]].merge(pd.DataFrame(rows), on=["unit", "recording"])
    return df, seqs
E3, SEQ3 = exp3_table(U3, T3)
E3d, SEQ3d = exp3_table(U3, T3, drop_late=True)
W = [f"s{w}" for w in range(1, 10)]

# %% [markdown]
### exp3-units-cw-tuned

> In awake mice (experiment 3), 81 single units were recorded, 74 were whisker-responsive and 62% (46) of these were CW-tuned; average single-whisker tuning peaked at the CW.

# %% tags=claim:exp3-units-cw-tuned
for lab, df in [("all epochs", E3), ("epochs with late spikes dropped", E3d)]:
    for sr in "ab":
        r = df[df[f"p_resp_{sr}"] < 0.05]
        cw = (r[W].to_numpy().argmax(1) + 1 == L.CW3)
        mean_s = r[W].mean()
        print(f"{lab}, sham {sr}: units {len(df)}, responsive {len(r)}, CW-tuned {cw.sum()} ({cw.mean():.2f}); "
              f"largest mean single-whisker response: whisker {int(mean_s.values.argmax()) + 1} (CW = {L.CW3})")
R3 = E3[E3.p_resp_a < 0.05].copy()
R3["cw_tuned"] = R3[W].to_numpy().argmax(1) + 1 == L.CW3
print("mean single-whisker response by face position (responsive, all epochs, sham a):",
      {L.POSNAME[L.relpos(w, 3)]: round(R3[f"s{w}"].mean(), 3) for w in range(1, 10)})
print("responsive per mouse:", R3.groupby("animal").size().to_dict(), "of", E3.groupby("animal").size().to_dict())

# %% [markdown]
### fig8c-awake-cw-stronger

> Among CW-tuned units, CW-evoked spiking was about twofold stronger, and sharper, in awake mice than in anesthetized mice of experiment 1 (P < 0.001, two-sample t-test).

# %% tags=claim:fig8c-awake-cw-stronger
for sr in "ab":
    aw = R3[R3.cw_tuned]
    an = R1[R1.cw_tuned]
    cw_aw = aw[f"s{L.CW3}"] - aw[f"spont_{sr}"] * L.WINDOW / 1000
    cw_an = an[f"s{L.CW12}"] - an[f"spont_{sr}"] * L.WINDOW / 1000
    t = stats.ttest_ind(cw_aw, cw_an)
    sw_aw = np.sort(aw[[f"s{w}" for w in range(1, 10) if w != L.CW3]].to_numpy(), 1)[:, ::-1] / aw[[f"s{L.CW3}"]].to_numpy()
    sw_an = np.sort(an[[f"s{w}" for w in range(1, 10) if w != L.CW12]].to_numpy(), 1)[:, ::-1] / an[[f"s{L.CW12}"]].to_numpy()
    print(f"sham {sr}: CW above spontaneous, awake {cw_aw.mean():.3f} (n={len(aw)}), anesthetized {cw_an.mean():.3f} (n={len(an)}), "
          f"ratio {cw_aw.mean() / cw_an.mean():.2f}, t = {t.statistic:.2f}, p = {t.pvalue:.3g}")
print("ranked SW responses / CW, awake:", sw_aw.mean(0).round(3), "mean", sw_aw.mean().round(3))
print("ranked SW responses / CW, anesthetized:", sw_an.mean(0).round(3), "mean", sw_an.mean().round(3))

# %% [markdown]
### fig8d-awake-best-sequence

> In awake mice the best two-whisker sequence evoked more spikes than the best single whisker in nearly all units (slope 1.24).

# %% tags=claim:fig8d-awake-best-sequence
x = R3[W].max(1).to_numpy(); y = np.array([SEQ3[k].max() for k in R3.unit])
lr = stats.linregress(x, y)
print(f"(a) slope through origin {(x @ y) / (x @ x):.3f}; (b) with intercept {lr.slope:.3f} (intercept {lr.intercept:.3f}); "
      f"best sequence > best single in {np.sum(y > x)} of {len(x)} ({np.mean(y > x):.3f}); sequences per unit {len(SEQ3[R3.unit.iloc[0]])}")
print("by mouse, fraction above:", R3.assign(above=y > x).groupby("animal").above.mean().round(2).to_dict())

# %% [markdown]
### exp3-combination-selective

> In awake mice, 39% of responsive units were significantly combination-selective (29 units); 76% of these and 80% of all responsive units preferred a sequence containing the CW.

# %% tags=claim:exp3-combination-selective
rng_e3 = np.random.default_rng(83)
SW3 = [w for w in range(1, 10) if w != L.CW3]
p3, X3 = [], {}
for _, r in R3.iterrows():
    tab = T3[r.recording]
    st = tab[tab.kind == "cwsw"]
    y = st[f"c{r.unit}"].to_numpy(float)
    comb = st.b.map({w: i for i, w in enumerate(SW3)}).to_numpy()
    dti = st.dt.map({-40.0: 0, 0.0: 1, 40.0: 2}).to_numpy()
    N = np.bincount(comb * 3 + dti, minlength=24).reshape(8, 3)
    meas = np.bincount(comb * 3 + dti, weights=y, minlength=24).reshape(8, 3) / N
    csi = L.sparseness(meas.T)
    keys = dti[None, :] + rng_e3.random((5000, len(y)))
    perm = np.argsort(keys, axis=1)
    order = np.argsort(dti, kind="stable")
    ys, cs, ds = y[order], comb[order], dti[order]
    keys = ds[None, :] + rng_e3.random((5000, len(y)))
    cperm = cs[np.argsort(keys, axis=1)]
    S = np.zeros((5000, 8, 3))
    idx = (np.arange(5000)[:, None] * 24 + cperm * 3 + ds[None, :]).ravel()
    S = np.bincount(idx, weights=np.tile(ys, 5000), minlength=5000 * 24).reshape(5000, 8, 3) / N[None]
    sh = L.sparseness(np.transpose(S, (0, 2, 1)))
    p, _ = L.mahalanobis_p(csi, sh)
    p3.append(p)
    X3[r.unit] = dict(meas=meas, y=y, comb=comb, dti=dti)
R3["p_shuffle"] = p3
R3["sel"] = L.bh(R3.p_shuffle.to_numpy())
def best_has_cw(k):
    s = SEQ3[k]
    comb = s.groupby(level=["kind", "a", "b"]).max()
    return comb.idxmax()[0] == "cwsw"
R3["best_cw"] = [best_has_cw(k) for k in R3.unit]
print(f"selective (FDR 0.05): {R3.sel.sum()} of {len(R3)} ({R3.sel.mean():.3f}); uncorrected p < 0.05: {(R3.p_shuffle < 0.05).sum()}")
print(f"best sequence contains the CW: selective {R3.loc[R3.sel, 'best_cw'].mean():.3f}, all responsive {R3.best_cw.mean():.3f}")
print("selective per mouse:", R3[R3.sel].groupby("animal").size().to_dict())

# %% [markdown]
### fig8h-awake-linearity, fig8i-awake-sharper-than-linear, fig8j-awake-inbound-stronger

> In awake mice, responses to each unit's best CW-SW combination were roughly linear (linearity index 0.93 +- 0.03) and to suboptimal combinations sublinear (0.71 +- 0.009, P = 6.2 x 10-17, two-sample t-test).

> In awake mice, combination tuning was sharper than linearly predicted for virtually all responsive units (P = 9.6 x 10-11, paired t-test).

> In awake mice, responses to inbound CW-SW sequences (dt = -40 ms) were stronger than to outbound (+40 ms) or simultaneous (0 ms) deflections (P = 2.2 x 10-14, one-factor ANOVA).

# %% tags=claim:fig8h-awake-linearity
LI_b, LI_s, CSI_m, CSI_l = [], [], [], []
for _, r in R3.iterrows():
    meas = X3[r.unit]["meas"]
    c, j = np.unravel_index(np.argmax(meas), meas.shape)
    lin = np.array([r[f"s{L.CW3}"] + r[f"s{w}"] for w in SW3])
    li = meas[:, j] / lin
    LI_b.append(li[c]); LI_s.extend(np.delete(li, c))
    CSI_m.append(L.sparseness(meas[:, j])); CSI_l.append(L.sparseness(lin))
LI_b, LI_s, CSI_m, CSI_l = map(np.array, (LI_b, LI_s, CSI_m, CSI_l))
t = stats.ttest_ind(LI_b, LI_s)
print(f"linearity index: best {LI_b.mean():.3f} +- {stats.sem(LI_b):.3f} (n={len(LI_b)}), suboptimal {LI_s.mean():.3f} +- {stats.sem(LI_s):.3f} (n={len(LI_s)}); t = {t.statistic:.2f}, p = {t.pvalue:.3g}")

# %% tags=claim:fig8i-awake-sharper-than-linear
t = stats.ttest_rel(CSI_m, CSI_l)
print(f"CSI measured {CSI_m.mean():.4f}, linear {CSI_l.mean():.4f}; measured above linear in {np.sum(CSI_m > CSI_l)} of {len(CSI_m)} ({np.mean(CSI_m > CSI_l):.3f}); paired t = {t.statistic:.2f}, p = {t.pvalue:.3g}")

# %% tags=claim:fig8j-awake-inbound-stronger
za, zb_ = [], []
for _, r in R3.iterrows():
    meas = X3[r.unit]["meas"]
    z_ = (meas - meas.mean()) / meas.std()
    za.append(z_.max(0))
    c = np.unravel_index(np.argmax(meas), meas.shape)[0]
    zb_.append(z_[c])
for lab, arr in [("(a) largest of the eight at each dt", np.array(za)), ("(b) the unit's best combination at each dt", np.array(zb_))]:
    f = stats.f_oneway(*arr.T)
    print(f"{lab}: means at -40, 0, +40 ms {arr.mean(0).round(3)}; ANOVA F = {f.statistic:.2f}, p = {f.pvalue:.3g}")

# %% [markdown]
### fig8k-awake-binary-decoder

> In awake mice, decoding of best against suboptimal CW-SW combinations from single-trial firing was accurate and efficient.

# %% tags=claim:fig8k-awake-binary-decoder
rng_8k = np.random.default_rng(88)
rows = []
for mode in "ab":
    probs, labs = [], []
    for _, r in R3[R3.sel].iterrows():
        d = X3[r.unit]
        c, j = np.unravel_index(np.argmax(d["meas"]), d["meas"].shape)
        m = d["dti"] == j
        x, yv = d["y"][m], d["comb"][m]
        best = yv == c
        if mode == "a":
            sub = rng_8k.choice(np.where(~best)[0], best.sum(), replace=best.sum() > (~best).sum())
        else:
            sub = np.where(yv == rng_8k.choice([q for q in range(8) if q != c]))[0]
        ii = np.r_[np.where(best)[0], sub]
        lab = np.r_[np.ones(best.sum(), int), np.zeros(len(sub), int)]
        probs.append(L.heldout_prob_rows(x[ii], lab, 2, rng_8k)); labs.append(lab)
    pool = L.Pool(probs, labs, 2)
    r_ = dict(suboptimal=mode, units=int(R3.sel.sum()))
    for N in [5, 10, 15, 20, 25]:
        r_[f"N{N}"] = pool.accuracy(N, 2500, rng_8k).mean()
    rows.append(r_)
print(pd.DataFrame(rows).to_string(index=False, float_format=fmt))
EOF
. ../dev/bin/activate && python run.py 00_load_dev.py 10_exp1.py 30_exp3.py 2>&1 | sed -n '/^all epochs/,$p' | grep -v "^---"; date -u
```

```
all epochs, sham a: units 81, responsive 74, CW-tuned 46 (0.62); largest mean single-whisker response: whisker 4 (CW = 4)
all epochs, sham b: units 81, responsive 78, CW-tuned 47 (0.60); largest mean single-whisker response: whisker 4 (CW = 4)
epochs with late spikes dropped, sham a: units 81, responsive 75, CW-tuned 46 (0.61); largest mean single-whisker response: whisker 4 (CW = 4)
epochs with late spikes dropped, sham b: units 81, responsive 76, CW-tuned 46 (0.61); largest mean single-whisker response: whisker 4 (CW = 4)
mean single-whisker response by face position (responsive, all epochs, sham a): {'ventral caudal': np.float64(0.448), 'ventral same-arc': np.float64(0.514), 'caudal within-row': np.float64(0.439), 'CW': np.float64(0.845), 'rostral within-row': np.float64(0.443), 'dorsal caudal': np.float64(0.444), 'dorsal same-arc': np.float64(0.411), 'dorsal rostral': np.float64(0.373), 'ventral rostral': np.float64(0.503)}
responsive per mouse: {'181207': 26, '181207t': 22, '190122p': 14, 'B6180927': 12} of {'181207': 29, '181207t': 24, '190122p': 14, 'B6180927': 14}
sham a: CW above spontaneous, awake 0.709 (n=46), anesthetized 0.414 (n=87), ratio 1.71, t = 3.14, p = 0.00212
sham b: CW above spontaneous, awake 0.715 (n=46), anesthetized 0.422 (n=87), ratio 1.70, t = 3.08, p = 0.00254
ranked SW responses / CW, awake: [0.593 0.498 0.43  0.377 0.343 0.301 0.254 0.205] mean 0.375
ranked SW responses / CW, anesthetized: [0.705 0.547 0.441 0.38  0.335 0.294 0.247 0.192] mean 0.393
(a) slope through origin 1.300; (b) with intercept 1.234 (intercept 0.114); best sequence > best single in 73 of 74 (0.986); sequences per unit 108
by mouse, fraction above: {'181207': 0.96, '181207t': 1.0, '190122p': 1.0, 'B6180927': 1.0}
selective (FDR 0.05): 27 of 74 (0.365); uncorrected p < 0.05: 35
best sequence contains the CW: selective 0.704, all responsive 0.784
selective per mouse: {'181207': 10, '181207t': 6, '190122p': 8, 'B6180927': 3}
linearity index: best 0.941 +- 0.028 (n=7
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019 && python - <<'EOF'
s=open('lj2019.py').read()
old='''            sel = tab.kind.isin(["single", "sham"]).to_numpy()'''
new='''            sel = tab.kind.isin(["single", "sham"]).to_numpy() | (exp == 3)'''
assert old in s; s=s.replace(old,new)
old='''        psth[rec] = dict(rows=tab.kind.isin(["single", "sham"]).to_numpy(),'''
new='''        psth[rec] = dict(rows=tab.kind.isin(["single", "sham"]).to_numpy() | (exp == 3),'''
assert old in s; s=s.replace(old,new)
s=s.replace('''    (``p<k>``), and spikes after the epoch (``o<k>``); psth: dict recording -> counts in 10 ms
    bins from -50 to +200 ms around onset for the single and sham trials (``rows``).''','''    (``p<k>``), and spikes after the epoch (``o<k>``); psth: dict recording -> counts in 10 ms
    bins from -50 to +200 ms around onset for the single and sham trials (all trials in
    experiment 3), with the trial mask ``rows``.''')
open('lj2019.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && python load_all.py 2>&1 | grep -E "time|Error"
```

```
1 time 43.97684979438782 maxrss GB 1.772932
3 time 7.125699758529663 maxrss GB 1.772932
2 time 97.67087364196777 maxrss GB 3.591996
Shell cwd was reset to
```

**Agent**

Now the rest of the data check cells.

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
s=open('30_exp3.py').read()
old='''    keys = dti[None, :] + rng_e3.random((5000, len(y)))
    perm = np.argsort(keys, axis=1)
    order'''
new='''    order'''
assert old in s; s=s.replace(old,new)
s=s.replace('''    S = np.zeros((5000, 8, 3))
''','')
open('30_exp3.py','w').write(s)
EOF
cat >> 01_check.py <<'EOF'

# %% tags=sanity
print("Stimulus directions (1 caudal, -1 rostral, data descriptor) by experiment:")
for e, T in [(1, T1), (2, T2), (3, T3)]:
    allt = pd.concat(T.values())
    s = allt[allt.kind == "single"]
    p = allt[allt.kind.isin(["cwsw", "swsw"])]
    print(f"  exp {e}: single-whisker trials by direction {s.da.value_counts().to_dict()}; two-whisker trials by (first, second) direction "
          f"{pd.Series(list(zip(p.da, p.db))).value_counts().to_dict()}")
t510 = [t for r, t in T1.items() if r.startswith("20170510")]
for t in t510:
    p = t[t.kind.isin(["cwsw", "swsw"])]
    mixed = p[p.da != p.db]
    print("  20170510 recording: pairs with opposite directions involve whiskers",
          sorted(set(mixed.a) | set(mixed.b)), "; whisker pairs among them:", sorted(set(zip(mixed.a, mixed.b))))
print("Three-whisker stimuli (not in the paper or the descriptor):")
for r, t in T2.items():
    if (t.kind == "triple").any():
        print(f"  {r}: {(t.kind == 'triple').sum()} trials")
print("Experiment 2 CW-SW dt values: ", sorted(pd.concat(T2.values()).query("kind == 'cwsw'").dt.unique().astype(int))[:3], "...",
      pd.concat(T2.values()).query("kind == 'cwsw'").dt.nunique(), "values (the paper says 100)")
print("Experiment 2 CW-SW trials per combination and dt, mean:",
      round(pd.concat(T2.values()).query("kind == 'cwsw'").groupby(["da", "db", "b", "dt"]).size().mean() / len(T2), 2))
print("Experiment 3 epochs: spikes after 300 ms, by file:")
for f, g in U3.groupby("file"):
    print(f"  {f}: {g.n_out.sum()} of {g.n_spikes.sum()} spikes ({g.n_out.sum() / g.n_spikes.sum():.2f}), largest time {g.max_t.max():.0f} ms")
late = np.concatenate([(t[[c for c in t.columns if c.startswith("o")]].to_numpy() > 0).ravel() for t in T3.values()])
print(f"  epochs (unit x epoch) holding any spike after 300 ms: {late.mean():.3f}")
inwin = np.concatenate([((t[[c for c in t.columns if c.startswith("o")]].to_numpy() > 0) & (t[[c for c in t.columns if c.startswith("c")]].to_numpy() > 0)).ravel() for t in T3.values()])
print(f"  of these, with a spike in 0-125 ms as well: {inwin.sum() / max(late.sum(), 1):.3f}")
print("Experiment 3 experiment field: whiskers by recording", U3.groupby("recording").whiskers.first().to_dict())
print("Experiment 3 tip depth (um):", U3.groupby("recording").depth.first().to_dict(), "; no per-unit depth in the files")

# %% [markdown]
The experiment 3 files give no deflection times. The latency of the CW response in CW-SW epochs shows how DeltaT and the epoch clock are defined: if epoch time 0 is the first deflection and dt = t_SW - t_CW, the CW-driven response comes 40 ms later when the SW leads (dt = -40) than when the CW leads (dt = +40). Mean counts over the 81 units in 10 ms bins.

# %% tags=sanity
bins = np.arange(-50, 200, 10)
def mean_psth(cond):
    tot, n = 0, 0
    for rec, tab in T3.items():
        P = P3[rec]
        m = cond(tab).to_numpy()[P["rows"]]
        for k in U3.loc[U3.recording == rec, "unit"]:
            tot = tot + P[f"h{k}"][m].sum(0)
            n += m.sum()
    return tot / n
for lab, cond in [("CW alone", lambda t: (t.kind == "single") & (t.a == L.CW3)),
                  ("CW-SW, dt = +40 (CW at 0)", lambda t: (t.kind == "cwsw") & (t.dt == 40)),
                  ("CW-SW, dt = -40 (SW at 0, CW at 40)", lambda t: (t.kind == "cwsw") & (t.dt == -40)),
                  ("SW alone", lambda t: (t.kind == "single") & (t.a != L.CW3)),
                  ("sham", lambda t: t.kind == "sham")]:
    h = mean_psth(cond)
    print(f"{lab:38s} peak bin starts at {bins[h.argmax()]:4d} ms; per-bin means x100:", (100 * h).round(1)[3:16])
print("bins shown start at", bins[3:16])

# %% [markdown]
Clock check for every recording: the nine single whiskers are decoded from the population's counts in windows before and after the deflection onset (multinomial logistic regression, fivefold cross-validation; chance 1/9). A shared clock gives chance before onset and above chance after it.

# %% tags=sanity
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
wins = {"-50 to 0 ms": slice(0, 5), "0 to 50 ms": slice(5, 10), "50 to 100 ms": slice(10, 15)}
rows = []
for e, (U, T, P) in {1: (U1, T1, P1), 2: (U2, T2, P2), 3: (U3, T3, P3)}.items():
    for rec, tab in T.items():
        Pm = P[rec]
        sub = tab[Pm["rows"]]
        m = (sub.kind == "single").to_numpy() & ((sub.da == 1).to_numpy())
        ks = U.loc[U.recording == rec, "unit"].tolist()
        r = dict(exp=e, recording=rec, units=len(ks), trials=int(m.sum()))
        for w, sl in wins.items():
            X = np.stack([Pm[f"h{k}"][m][:, sl].sum(1) for k in ks], 1).astype(float)
            r[w] = cross_val_score(LogisticRegression(max_iter=300), X, sub.a.to_numpy()[m], cv=5).mean()
        rows.append(r)
CLK = pd.DataFrame(rows)
print(CLK.round(3).to_string(index=False))
print("mean accuracy by window:", CLK[list(wins)].mean().round(3).to_dict(), "; chance", round(1 / 9, 3))
EOF
. ../dev/bin/activate && python run.py 00_load_dev.py 01_check.py 2>&1 | sed -n '/Stimulus directions/,$p' | grep -v "^---"; date -u
```

```
Stimulus directions (1 caudal, -1 rostral, data descriptor) by experiment:
  exp 1: single-whisker trials by direction {1: 9886, -1: 9884}; two-whisker trials by (first, second) direction {(1, 1): 188052, (1, -1): 6721, (-1, 1): 3991}
  exp 2: single-whisker trials by direction {1: 32205, -1: 32202}; two-whisker trials by (first, second) direction {(1, 1): 181902, (1, -1): 124763, (-1, 1): 65549, (-1, -1): 8367}
  exp 3: single-whisker trials by direction {1: 4679}; two-whisker trials by (first, second) direction {(1, 1): 56238}
  20170510 recording: pairs with opposite directions involve whiskers [1, 2, 3, 4, 5, 6, 7, 8, 9] ; whisker pairs among them: [(1, 3), (1, 8), (2, 3), (2, 8), (3, 4), (3, 6), (3, 7), (3, 8), (3, 9), (4, 8), (5, 3), (5, 8), (6, 8), (7, 8), (8, 9)]
  20170510 recording: pairs with opposite directions involve whiskers [1, 2, 3, 4, 5, 6, 7, 8, 9] ; whisker pairs among them: [(1, 3), (1, 8), (2, 3), (2, 8), (3, 4), (3, 6), (3, 7), (3, 8), (3, 9), (4, 8), (5, 3), (5, 8), (6, 8), (7, 8), (8, 9)]
Three-whisker stimuli (not in the paper or the descriptor):
  20160325:946652: 18000 trials
  20160406:237ffc: 20623 trials
  20160803:233bcd: 19461 trials
  20160808:429fdb: 16191 trials
  20160817:0ef174: 22267 trials
  20160829:6066e9: 24273 trials
  20160909:f387b2: 20244 trials
  20160909:a32d3a: 16195 trials
  20160914:0f1a60: 19630 trials
Experiment 2 CW-SW dt values:  [np.int64(-50), np.int64(-49), np.int64(-48)] ... 101 values (the paper says 100)
Experiment 2 CW-SW trials per combination and dt, mean: 4.83
Experiment 3 epochs: spikes after 300 ms, by file:
  Experiment3/20181114.mat: 35486 of 133981 spikes (0.26), largest time 18096 ms
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
s=open('01_check.py').read()
s=s.replace('''late = np.concatenate([(t[[c for c in t.columns if c.startswith("o")]].to_numpy() > 0).ravel() for t in T3.values()])''','''import re
ocols = lambda t, p: [c for c in t.columns if re.fullmatch(p + r"\\d+", c)]
late = np.concatenate([(t[ocols(t, "o")].to_numpy() > 0).ravel() for t in T3.values()])''')
s=s.replace('''inwin = np.concatenate([((t[[c for c in t.columns if c.startswith("o")]].to_numpy() > 0) & (t[[c for c in t.columns if c.startswith("c")]].to_numpy() > 0)).ravel() for t in T3.values()])''','''inwin = np.concatenate([((t[ocols(t, "o")].to_numpy() > 0) & (t[ocols(t, "c")].to_numpy() > 0)).ravel() for t in T3.values()])''')
old='''    mixed = p[p.da != p.db]
    print("  20170510 recording: pairs with opposite directions involve whiskers",
          sorted(set(mixed.a) | set(mixed.b)), "; whisker pairs among them:", sorted(set(zip(mixed.a, mixed.b))))'''
new='''    mixed = p[p.da != p.db]
    rostral = sorted(set(mixed.loc[mixed.da == -1, "a"]) | set(mixed.loc[mixed.db == -1, "b"]))
    print(f"  20170510 recording: {len(mixed)} of {len(p)} two-whisker trials have opposite directions; the whisker deflected rostrally in them is one of",
          rostral, "; same-direction trials of the pairs that involve 3 or 8:",
          int(((p.da == p.db) & (p.a.isin([3, 8]) | p.b.isin([3, 8]))).sum()))'''
assert old in s; s=s.replace(old,new)
open('01_check.py','w').write(s)
EOF
. ../dev/bin/activate && python run.py 00_load_dev.py 01_check.py 2>&1 | sed -n '/20170510 rec/,$p' | grep -v "^---" | grep -v "^ *Experiment3\|Three\|^  2016"; date -u
```

```
20170510 recording: 5471 of 24983 two-whisker trials have opposite directions; the whisker deflected rostrally in them is one of [3, 8] ; same-direction trials of the pairs that involve 3 or 8: 4865
  20170510 recording: 5241 of 23579 two-whisker trials have opposite directions; the whisker deflected rostrally in them is one of [3, 8] ; same-direction trials of the pairs that involve 3 or 8: 4564
Experiment 2 CW-SW dt values:  [np.int64(-50), np.int64(-49), np.int64(-48)] ... 101 values (the paper says 100)
Experiment 2 CW-SW trials per combination and dt, mean: 4.83
Experiment 3 epochs: spikes after 300 ms, by file:
  epochs (unit x epoch) holding any spike after 300 ms: 0.056
  of these, with a spike in 0-125 ms as well: 0.412
Experiment 3 experiment field: whiskers by recording {'20181114:be5c61': 'E2 E1 delta D2 D1 gamma C2 C1 beta', '20190123:4f1cce': 'E2 E1 delta D2 D1 gamma C2 C1 beta', '20190124:a141c6': 'D2 D1 gamma C2 C1 beta B2 B1 alpha', '20190128:af342f': 'E3 E2 E1 D3 D2 D1 C3 C2 C1', '20190129:65f07b': 'E2 E1 delta D2 D1 gamma C2 C1 beta', '20190215:ff0748': 'E2 E1 delta D2 D1 gamma C2 C1 beta'}
Experiment 3 tip depth (um): {'20181114:be5c61': 520.0, '20190123:4f1cce': 560.0, '20190124:a141c6': 550.0, '20190128:af342f': 550.0, '20190129:65f07b': 560.0, '20190215:ff0748': 550.0} ; no per-unit depth in the files
CW alone                               peak bin starts at   30 ms; per-bin means x100: [ 0.   0.   3.2  3.9 11.9 16.9 14.3  8.7  5.8  4.   3.1  2.3  2.4]
CW-SW, dt = +40 (CW at 0)              peak bin starts at   30 ms; per-bin means x100: [ 0.   0.   2.7  3.6 12.1 16.7 13.8  8.6  5.6  4.7  4.5  3.4  2.6]
CW-SW, dt = -40 (SW at 0, CW at 40)    peak bin starts at   70 ms; per-bin means x100: [ 0.   0.   2.8  2.8  3.6  6.7  6.7  5.4 10.  14.6 13.3  8.6  5.9]
SW alone                               peak bin starts at   40 ms; per-bin means x100: [0.  0.  2.7 2.8 3.6 6.9 6.9 5.1 3.1 2.4 2.1 2.2 2.1]
sham                                   peak bin sta
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat >> 22_exp2_a.py <<'EOF'

# %% tags=claim:methods-dt-modulation
t0 = time.time()
KERZ = L.gaussian_kernels_zeropad(101, L.SDS)
rng_z = np.random.default_rng(20190803)
stz = []
for _, r in S2[RESP].iterrows():
    d = CUR[(r.unit, r.set)]
    for ci in range(8):
        sel_ = d["comb"] == ci
        stz.append(L.fast_dt_smooth(d["y"][sel_], d["dti"][sel_], rng_z, KERZ)[2])
stz = np.array(stz)
print(f"reading (b), zero padding: curves {len(stz)}, monotonic {np.mean(stz == 'monotonic'):.3f}, unsmoothed {np.mean(stz == 'unsmoothed'):.3f}, "
      f"constant {np.sum(stz != 'modulated')} ({np.mean(stz != 'modulated'):.3f}); {time.time() - t0:.0f} s")
print("expected: monotonic 0.33 +- 0.033, unsmoothed 0.23 +- 0.023, constant 2004 +- 200.4")
EOF
cat > 05_header.py <<'EOF'
# %% [markdown]
# Reproducing Laboy-Juarez et al. (2019) from CRCNS ssc-9

Paper: Laboy-Juarez KJ, Langberg T, Ahn S, Feldman DE (2019). Elementary motion sequence detectors in whisker somatosensory cortex. Nature Neuroscience 22, 1438-1449. doi:10.1038/s41593-019-0448-6.

Dataset: CRCNS ssc-9, "Extracellular recordings in mouse barrel cortex during single- and 2-whisker stimulation", doi:10.6080/K0FJ2F13, read from the public bucket at `https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip`. CRCNS data sets are not versioned (docs/archives.md), so the version is recorded as `unversioned`, pinned by the MD5 sums of the files read, from the data set's `checksums.md5`: `data.zip` 2e7a774017619e76c46db85722587be3 (the only data file; the docs are `crcns_ssc-9_data_description.pdf` d5d1590c38b8eea45e070e8cdfc4827f, version 0.6 of May 13, 2019). There is one published version, the one the paper's Data availability statement points to (crcns.org), so it is the one used; the next cell checks the sum.

Claims file: `claims/laboy-juarez-2019.yaml`, written from the version of record with its supplement. The paper links no code (available on request), so every method below comes from the claims file, the Methods, the legends and the supplement; details taken from the paper cite the passage.

Claims tested and blocked (outcomes are in the summary at the end):

| Claim | Status |
|---|---|
| exp1-units to supp2-sw-tuned-sharpest-cwsw (experiment 1, 10 claims) | tested |
| exp2-units to supp8-order-decoding (experiment 2, 30 claims) | tested |
| exp3-units-cw-tuned to fig8k-awake-binary-decoder (experiment 3, 8 claims) | tested |
| fig8b-awake-behavior | blocked: the files hold no lick times or trial types |

# %%
import hashlib
import fsspec
h = hashlib.md5()
with fsspec.open("https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip", block_size=2 ** 22) as f:
    for chunk in iter(lambda: f.read(2 ** 22), b""):
        h.update(chunk)
print("data.zip MD5", h.hexdigest(), "| matches checksums.md5:", h.hexdigest() == "2e7a774017619e76c46db85722587be3")
EOF
grep -c "tags=claim" 10_exp1.py 22_exp2_a.py 23_exp2_b.py 25_exp2_d.py 26_exp2_e.py 27_exp2_f.py 28_exp2_g.py 29_exp2_dec.py 30_exp3.py
```

```
10_exp1.py:10
22_exp2_a.py:3
23_exp2_b.py:1
25_exp2_d.py:4
26_exp2_e.py:10
27_exp2_f.py:6
28_exp2_g.py:3
29_exp2_dec.py:5
30_exp3.py:8
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && . ../dev/bin/activate && time python run.py 00_load_dev.py 01_check.py 10_exp1.py 20_exp2_core.py 21_exp2_shuffle.py 22_exp2_a.py 23_exp2_b.py 24_exp2_c.py 25_exp2_d.py 26_exp2_e.py 27_exp2_f.py 28_exp2_g.py 29_exp2_dec.py 30_exp3.py > full.log 2>&1; tail -5 full.log; grep -c . full.log; date -u
```

```
real	10m37.269s
user	38m15.273s
sys	0m7.257s
--- cell tags=claim:fig8j-awake-inbound-stronger 0.0s maxrss 9.84 GB
suboptimal  units     N5    N10    N15    N20    N25
         a     27 0.6524 0.7076  0.759 0.7846  0.815
         b     27 0.6738 0.7332 0.7656 0.8054 0.8292
--- cell tags=claim:fig8k-awake-binary-decoder 0.1s maxrss 9.84 GB
458
Thu Nov 12 18:10:49 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && grep -E "^--- cell" full.log | awk '{print $0}' | head -80
```

```
--- cell  0.8s maxrss 0.46 GB
--- cell tags=sanity 0.3s maxrss 0.48 GB
--- cell tags=sanity 8.6s maxrss 9.84 GB
--- cell tags=sanity 0.0s maxrss 9.84 GB
--- cell tags=sanity 4.5s maxrss 9.84 GB
--- cell  2.1s maxrss 9.84 GB
--- cell tags=claim:exp1-units 0.0s maxrss 9.84 GB
--- cell  0.0s maxrss 9.84 GB
--- cell tags=claim:fig1b-somatotopy 0.0s maxrss 9.84 GB
--- cell tags=claim:exp1-cw-tuned-fraction 0.0s maxrss 9.84 GB
--- cell tags=claim:exp1-cw-sw-comparable-firing 0.0s maxrss 9.84 GB
--- cell tags=claim:supp1d-sw-tuning-broader 0.0s maxrss 9.84 GB
--- cell tags=claim:fig1d-best-sequence-exceeds-single 0.0s maxrss 9.84 GB
--- cell tags=claim:fig1e-best-combination-includes-cw 0.1s maxrss 9.84 GB
--- cell tags=claim:fig1f-cwsw-exceeds-swsw 0.2s maxrss 9.84 GB
--- cell tags=claim:fig1g-cwsw-sharper 0.1s maxrss 9.84 GB
--- cell tags=claim:supp2-sw-tuned-sharpest-cwsw 0.0s maxrss 9.84 GB
--- cell  113.8s maxrss 9.84 GB
--- cell  370.8s maxrss 9.84 GB
--- cell tags=claim:exp2-units 0.0s maxrss 9.84 GB
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
s=open('01_check.py').read()
s=s.replace('''    allt = pd.concat(T.values())''','''    allt = pd.concat([t[["kind", "a", "b", "dt", "da", "db"]] for t in T.values()])''')
s=s.replace('''print("Experiment 2 CW-SW dt values: ", sorted(pd.concat(T2.values()).query("kind == 'cwsw'").dt.unique().astype(int))[:3], "...",
      pd.concat(T2.values()).query("kind == 'cwsw'").dt.nunique(), "values (the paper says 100)")
print("Experiment 2 CW-SW trials per combination and dt, mean:",
      round(pd.concat(T2.values()).query("kind == 'cwsw'").groupby(["da", "db", "b", "dt"]).size().mean() / len(T2), 2))''','''cw2 = pd.concat([t.loc[t.kind == "cwsw", ["b", "dt", "da", "db"]].assign(rec=r) for r, t in T2.items()])
print("Experiment 2 CW-SW dt values:", int(cw2.dt.min()), "to", int(cw2.dt.max()), "in", cw2.dt.nunique(), "values (the paper says 100 values within +-50 ms)")
same = cw2.da == cw2.db
print("Experiment 2 trials per CW-SW combination and dt, mean over recordings: correlated",
      round(cw2[same].groupby(["rec", "b", "dt"]).size().mean(), 2), "| anti-correlated", round(cw2[~same].groupby(["rec", "b", "dt"]).size().mean(), 2),
      "(the paper gives 8.42 +- 4.2 per unique sequence)")''')
open('01_check.py','w').write(s)
EOF
. ../dev/bin/activate && python run.py 00_load_dev.py 01_check.py 2>&1 | grep -E "cell|Experiment 2"
```

```
--- cell  0.8s maxrss 0.46 GB
=== Experiment 2: 12 files, 16 recordings (distinct trial sequences), 247 units
--- cell tags=sanity 0.3s maxrss 0.48 GB
Experiment 2 CW-SW dt values: -50 to 50 in 101 values (the paper says 100 values within +-50 ms)
Experiment 2 trials per CW-SW combination and dt, mean over recordings: correlated 9.68 | anti-correlated 9.66 (the paper gives 8.42 +- 4.2 per unique sequence)
--- cell tags=sanity 0.4s maxrss 0.58 GB
--- cell tags=sanity 0.0s maxrss 0.58 GB
--- cell tags=sanity 4.6s maxrss 0.58 GB
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -n '/claim:supp2/,/claim:fig7f/p' full.log | grep -v "^--- cell" | head -150
```

```
20160225:10da10 4 s 9.836184
20160316:2dc362 5 s 9.836184
20160325:946652 11 s 9.836184
20160406:237ffc 20 s 9.836184
20160504:6b0f02 26 s 9.836184
20160504:a2e8d2 36 s 9.836184
20160506:7a1a88 38 s 9.836184
20160803:233bcd 44 s 9.836184
20160803:1a588f 56 s 9.836184
20160808:429fdb 61 s 9.836184
20160817:0ef174 74 s 9.836184
20160829:6066e9 78 s 9.836184
20160909:f387b2 84 s 9.836184
20160909:a32d3a 86 s 9.836184
20160914:5bd957 99 s 9.836184
20160914:0f1a60 114 s 9.836184
492 unit-sets; 246 units
shuffle tests: 371 s
units in the files: 247 in 12 files; after dropping the duplicate: 246
directions sham  corr  anti  sets
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && cat >> 10_exp1.py <<'EOF'

# %% [markdown]
### Experiment 1 under the other readings of the stimulus directions

The main analysis above uses the caudal single-whisker deflections and every trial of each sequence. The same measures with (i) both directions of the single-whisker deflections pooled, and (ii) caudal singles with same-direction sequence trials only (which drops, in the two 20170510 recordings, the sequences that involve whisker 3 or 8 in their same-direction form; see the data check):

# %% tags=claim:exp1-units
def exp1_summary(E, SEQ):
    R = E[E.p_resp_a < 0.05].copy()
    R["cw_tuned"] = R[W].to_numpy().argmax(1) + 1 == L.CW12
    x = R[W].max(1).to_numpy(); y = np.array([SEQ[k].max() for k in R.unit])
    lr_ = stats.linregress(x, y)
    bc_ = np.array([best_combo(SEQ[k])[0] == "cwsw" for k in R.unit])
    m_ = R[W].mean()
    order_ = [L.POSNAME[L.relpos(int(c[1:]), 1)] for c in m_.sort_values(ascending=False).index]
    Xr = R[W].to_numpy(); rk = -np.sort(-Xr, 1) / Xr.max(1, keepdims=True)
    cwm_ = R.cw_tuned.to_numpy()
    return dict(responsive=len(R), cw_tuned=int(cwm_.sum()), sw_tuned=int((~cwm_).sum()),
                spont_cw=R.loc[cwm_, "spont_a"].mean(), spont_sw=R.loc[~cwm_, "spont_a"].mean(),
                max_single_cw=R.loc[cwm_, W].max(1).mean(), max_single_sw=R.loc[~cwm_, W].max(1).mean(),
                p_broader=stats.f_oneway(rk[cwm_, 1:].mean(1), rk[~cwm_, 1:].mean(1)).pvalue,
                slope_intercept=lr_.slope, frac_above=np.mean(y > x),
                best_cw_all=bc_.mean(), best_cw_cwtuned=bc_[cwm_].mean(), best_cw_swtuned=bc_[~cwm_].mean(),
                order=" > ".join(order_[:3]),
                **{f"{lay}": int((R.layer == lay).sum()) for lay in ["L2/3", "L4", "L5", "L6"]})
_, SEQ1same = exp1_table(U1, T1, pair_dirs=((1, 1), (-1, -1)))
var1 = pd.DataFrame({"main (caudal singles, all sequence trials)": exp1_summary(E1, SEQ1),
                     "(i) both directions of singles": exp1_summary(E1all, SEQ1all),
                     "(ii) same-direction sequence trials only": exp1_summary(E1, SEQ1same)})
print(var1.to_string())
EOF
python - <<'EOF'
import re
p='/tmp/claude-1001/nb/10_exp1.py'
s=open(p).read()
# the variant cell uses best_combo, defined in the fig1e cell: fine since it comes after
open(p,'w').write(s)
EOF
. ../dev/bin/activate && python run.py 00_load_dev.py 10_exp1.py 2>&1 | tail -25
```

```
--- cell tags=claim:fig1g-cwsw-sharper 0.1s maxrss 0.48 GB
CW-SW sparseness, SW-tuned at N = 2, 5, 10, 20, 40, 56: [0.022 0.026 0.037 0.055 0.085 0.129]
CW-SW sparseness, CW-tuned at N = 2, 5, 10, 20, 40, 56: [0.008 0.01  0.013 0.019 0.036 0.07 ]
SW-tuned above CW-tuned at 55 of 55 values of N
--- cell tags=claim:supp2-sw-tuned-sharpest-cwsw 0.0s maxrss 0.48 GB
                  main (caudal singles, all sequence trials)               (i) both directions of singles     (ii) same-direction sequence trials only
responsive                                               144                                          155                                          144
cw_tuned                                                  87                                           86                                           87
sw_tuned                                                  57                                           69                                           57
spont_cw                                            1.332384                                      1.26341                                     1.332384
spont_sw                                            2.051721                                     2.181864                                     2.051721
max_single_cw                                       0.580514                                     0.584445                                     0.580514
max_single_sw                                       0.600531                                     0.646943                                     0.600531
p_broader                                           0.000723                                      0.00016                                     0.000723
slope_intercept                                     1.211319                                     1.185142                                     1.257677
frac_above                                          0.993056                                     0.967742                     
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i -E "def .*handover|Result:|summary|conclusion" tools/entry.py | head -30
```

```
36:(docs/protocol.md): the executed notebooks with the conclusions removed (every
37:markdown cell that begins "**Result:" and everything from the "## Summary"
590:def strip_conclusions(nb):
591:    """The notebook without the author's conclusions, for a verifier's first round."""
595:        if cell.cell_type == "markdown" and text.startswith("## Summary"):
597:        if cell.cell_type == "markdown" and text.startswith("**Result:"):
604:def handover(entry_dir: Path, output_dir: Path) -> int:
614:        nb = strip_conclusions(nbformat.read(executed, as_version=4))
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/entry.py; grep -n "def check" -A60 tools/entry.py | grep -n -i -E "tag|sanity|claim|yaml|require" | head -40
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
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -n '/claim:fig7f/,$p' full.log | grep -v "^--- cell" | head -80
```

```
classifiers for 463 sets (0 dropped) in 6 s
N = 10: measured 0.135 (s.d. 0.100); linear prediction 0.123 (s.d. 0.093); difference 0.011 vs sum of s.d. 0.193
N = 50: measured 0.148 (s.d. 0.079); linear prediction 0.130 (s.d. 0.074); difference 0.018 vs sum of s.d. 0.153
N = 100: measured 0.145 (s.d. 0.064); linear prediction 0.128 (s.d. 0.053); difference 0.017 vs sum of s.d. 0.116
N = 187: measured 0.135 (s.d. 0.041); linear prediction 0.127 (s.d. 0.030); difference 0.008 vs sum of s.d. 0.072
   per combination at N = 187: {'dorsal caudal': np.float64(0.0), 'caudal within-row': np.float64(0.0), 'ventral caudal': np.float64(0.02), 'dorsal same-arc': np.float64(0.034), 'ventral same-arc': np.float64(0.039), 'dorsal rostral': np.float64(0.0), 'rostral within-row': np.float64(0.986), 'ventral rostral': np.float64(0.002)}
N = 318: measured 0.129 (s.d. 0.024); linear prediction 0.125 (s.d. 0.012); difference 0.004 vs sum of s.d. 0.036
selective sets in the pool: 318 ; chance 0.125
single-unit held-out accuracy (own argmax), selective sets: mean 0.142, range 0.081 to 0.297
best combination of the selective sets by face position: {'rostral within-row': 111, 'ventral caudal': 61, 'ventral rostral': 44, 'ventral same-arc': 42, 'caudal within-row': 22, 'dorsal same-arc': 17, 'dorsal rostral': 13, 'dorsal caudal': 8}
        units suboptimal  n_units    N10   N100
(c) selective          a      318 0.6088  0.817
(c) selective          b      318 0.6158  0.818
      (d) all          a      463 0.5906 0.7626
      (d) all          b      463 0.5854 0.7474
        units    group   n    N10    N25    N50   N100   N150   sd150
(a) selective SW-tuned 224 0.1399  0.149 0.1487 0.1414 0.1365 0.04038
(a) selective CW-tuned  94 0.1221 0.1313 0.1407   0.15 0.1553 0.07457
      (b) all SW-tuned 289 0.1303 0.1438  0.142 0.1391 0.1354  0.0399
      (b) all CW-tuned 174  0.114 0.1188 0.1225  0.128 0.1317 0.06138
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && sed -i 's|print("note: the range \[40, 40\] is dropped by the Fig. 7g bins (\[31, 40\] would be next); the paper.s ten ranges are used as the claims file gives them")|print("note: the ten ranges are those of the claims file; dt = +40 ms falls in none of them")|' 29_exp2_dec.py && grep -n "falls in none" 29_exp2_dec.py && cat > results.md <<'EOF'
## exp1-units
**Result: reproduced (resting on an assumption).** With caudal single-whisker deflections and sham reading (a), 144 of the 160 units in 8 recordings from 5 mice are responsive, 36 in L2/3, 48 in L4, 46 in L5 and 14 in L6, every count within its tolerance; sham reading (b) gives 147 with 36, 50, 47 and 14. Pooling both deflection directions of the singles gives 155 responsive units with 52 in L5, outside its tolerance (44 +- 4.4), so the outcome rests on reading the paper's nine single-whisker stimuli as the caudal ones.

## fig1b-somatotopy
**Result: reproduced.** The CW has the largest mean response over the 144 responsive units (0.517 spikes per stimulus), followed by the rostral (0.368) and caudal (0.327) within-row SWs. The same order holds under both other direction readings.

## exp1-cw-tuned-fraction
**Result: reproduced.** 87 of 144 responsive units are CW-tuned and 57 SW-tuned (fraction 0.604), all within tolerance of 89, 53 and 0.61; sham reading (b) gives 89 and 58 (0.605).

## exp1-cw-sw-comparable-firing
**Result: partially reproduced.** Spontaneous rates match: 1.33 +- 0.14 Hz for CW-tuned and 2.05 +- 0.43 Hz for SW-tuned units under sham reading (a) (1.27 and 2.01 under (b)), within the paper's 1.28 +- 0.24 and 2.08 +- 0.4. Maximal evoked firing does not: the best single-whisker response is 0.58 and 0.60 spikes per stimulus and the best response over all 261 stimuli 0.86 and 0.91, against 4.8 and 4.56. CW-tuned and SW-tuned units do not differ in maximal firing (p = 0.84 and 0.65); the spontaneous difference gives p = 0.067 and 0.042.

## supp1d-sw-tuning-broader
**Result: reproduced.** The mean normalized response over ranks 2 to 9 is 0.482 for SW-tuned and 0.393 for CW-tuned units, a one-factor ANOVA gives p = 0.00072 under reading (a) and p = 1.6e-10 under reading (b).

## fig1d-best-sequence-exceeds-single
**Result: reproduced.** The slope of best sequence on best single whisker is 1.211 with an intercept (reading b, within 1.26 +- 0.126) and 1.345 through the origin (reading a, outside); 143 of 144 units (0.993) respond more to their best sequence.

## fig1e-best-combination-includes-cw
**Result: partially reproduced (resting on an assumption).** The best combination contains the CW for 0.688 of all units and 0.862 of CW-tuned units, within tolerance, and for 0.421 of SW-tuned units, just below the tolerance band (0.423 to 0.517); chance is 0.222. With both directions of singles pooled (0.464) or with same-direction sequence trials only (0.456) all three fractions are within tolerance, so the outcome depends on the direction reading.

## fig1f-cwsw-exceeds-swsw
**Result: reproduced.** 99 of 144 units lie above the diagonal under both z-scoring readings, with a mean z-scored difference of 0.54 (reading a, paired t-test p = 1e-6) and 0.47 (reading b, p = 1e-6).

## fig1g-cwsw-sharper
**Result: reproduced.** The mean lifetime sparseness of the N best CW-SW sequences is above that of the N best SW-SW sequences at all 55 values of N from 2 to 56 (for example 0.094 against 0.044 at N = 56).

## supp2-sw-tuned-sharpest-cwsw
**Result: reproduced.** The CW-SW sparseness of SW-tuned units is above that of CW-tuned units at all 55 values of N (0.129 against 0.070 at N = 56).

## exp2-units
**Result: reproduced.** The files hold 247 units in 12 mice (246 after dropping a duplicated unit); under direction reading (a) and sham reading (a), 231 are responsive to correlated and 232 to anti-correlated stimuli, within tolerance of 224 and 227; the other three readings give 237 to 240, also within tolerance.

## methods-dt-modulation
**Result: not reproduced.** Of the 3,704 CW-SW curves of the responsive sets, under reading (a) 0.574 have likelihoods that rise up to the largest kernel, none is best fit unsmoothed, and 2,127 (0.574) are set constant: the total count is within tolerance of 2,004 but the two fractions are far from 0.33 and 0.23. Under reading (b) (zero padding) only 39 curves (0.011) are set constant.

## exp2-combination-selective-prevalence
**Result: not reproduced.** The shuffle test finds 318 of 463 responsive sets combination-selective (FDR over all sets; 312 with the two sets apart), in 189 of 246 cells (0.768), against 187 sets and 129 cells (0.52). The fractions are 0.641 and 0.733 of the responsive correlated and anti-correlated sets, or 0.602 and 0.691 of all cells, against 0.35 and 0.46. The p-values do not depend much on how the covariance is inverted (a check on 40 sets, not in this notebook, gave more selective sets with larger regularization).

## fig2f-shuffle-abolishes-tuning
**Result: reproduced.** Over the 318 selective sets the mean peak-aligned tuning has a CSI of 0.033 (peak 0.861 against 0.515 to 0.607 for the other combinations); one shuffle per set gives a flat curve (CSI 0.000 aligned to the measured best combination, 0.003 aligned to its own peak), and the shuffled first point exceeds the mean of the other seven by 0.011, within the s.e.m. of that point (0.027).

## fig2f-most-selective-lower-firing
**Result: reproduced.** The most selective quarter (79 sets) has lower spontaneous firing (0.83 against 3.94 Hz, p = 4e-13) and lower evoked firing (best response 0.61 against 1.24 spikes per stimulus, p = 4e-10; mean of eight 0.31 against 1.01) than the least selective quarter.

## supp4-selectivity-at-high-rates
**Result: partially reproduced.** Among the 128 high-rate selective sets with sham trials, the spontaneous-subtracted peak-aligned tuning has a peak 0.451 above the mean of the other seven combinations, 22.9 times its s.e.m. The group counts are not reproduced: 178 selective sets below 0.81 spikes per stimulus, 140 at or above, and 28 nonselective at or above, against 95, 92 and 91.

## fig2g-best-combination-bias
**Result: reproduced.** Best combinations of the 463 responsive sets are nonuniform (Rayleigh p = 1.1e-22); every SW is best for at least 14 sets, the rostral within-row SW is the most frequent (150), and the ventral row (210) is more frequent than the dorsal row (63).

## fig3a-sharper-than-linear
**Result: reproduced.** Measured CSI at the best dt (0.086) is above the linear CSI (0.035) by paired t-test (p = 3e-43), with 0.911 of 463 sets above under readings O3 (a) and O2 (a); the other readings give 0.946 to 0.991 and p below 1e-46.

## fig3b-sharper-in-both-groups
**Result: reproduced.** Measured CSI exceeds linear CSI in the 318 selective sets (0.093 against 0.040, two-sample p = 1.4e-19) and in the 145 nonselective sets (0.071 against 0.023, p = 5.5e-8), under every reading.

## fig3b-linear-sharper-in-selective
**Result: reproduced.** The linear CSI is higher in selective sets (0.0399 against 0.0234, p = 7.3e-5; 0.0312 against 0.0168, p = 3.7e-6 under O2 b).

## supp6-layers
**Result: partially reproduced.** Log10 CSI differs across layers (ANOVA p = 2.4e-5 over all responsive sets, p = 0.0015 over selective sets), with L2/3 (-1.13) and L4 (-1.24) above L5 (-1.39) and L6 (-1.34). The layer counts are 103, 159 and 147 for L2/3 to L5, within tolerance, and 53 for L6, outside 45 +- 4.5.

## fig3e-identity-decoder
**Result: not reproduced.** The summed-probability decoder reaches 0.135 at N = 187 selective sets (chance 0.125), against 0.42; it reports the rostral within-row combination for nearly every stimulus (accuracy 0.986 for that combination, 0 to 0.039 for the others, against 0.82 and 0.23 to 0.28 for the dorsal row). The linear-prediction decoder is lower by 0.008, less than the sum of the two s.d. (0.072).

## fig3g-binary-decoder
**Result: not reproduced.** The best-against-suboptimal decoder reaches 0.609 to 0.616 at N = 10 and 0.817 to 0.818 at N = 100 over the selective sets (readings a and b), and 0.585 to 0.591 and 0.747 to 0.763 over all sets; accuracy at N = 10 is below the tolerance band (0.63 to 0.77) under every reading.

## fig4a-sw-tuned-sharper
**Result: reproduced.** Under O2 (a), 174 sets are CW-tuned and 289 SW-tuned (within tolerance of 169 and 282), and SW-tuned sets are more sharply combination-tuned (CSI 0.103 against 0.058, p = 3.6e-7); O2 (b) gives 216 and 247 with p = 7.5e-5.

## fig4c-sw-tuned-decoding
**Result: partially reproduced.** Over all sets (reading b), SW-tuned decoders are more accurate than CW-tuned ones at every size (0.130 against 0.114 at N = 10, 0.135 against 0.132 at N = 150); over selective sets (reading a) the order reverses from N = 100. CW-tuned decoders at N = 150 (0.132 and 0.155) are not above chance (0.125) by two s.d. (s.d. 0.061 and 0.075).

## fig5a-global-scaling
**Result: reproduced.** The least-squares slope through the origin of the 3,704 measured responses on their linear predictions is 0.636, with R2 = 0.926 (centred) or 0.967 (uncentred); the other readings give slopes 0.620 to 0.643 and R2 0.868 to 0.967.

## fig5bc-linearity-index
**Result: partially reproduced.** The linearity index is 0.909 +- 0.021 for best combinations and 0.645 +- 0.003 for nonoptimal ones (p = 1.6e-120), against 0.95 +- 0.02 and 0.63 +- 0.003; both means miss their tolerance and lie within 10% of the reported values, and the ordering and test hold. Reading O3 (b) with O2 (a) puts the best mean (0.964) within tolerance but not the nonoptimal one (0.652).

## fig5c-pseudo-unit-shuffle
**Result: reproduced.** Over 463 pseudo-units the strongest responses have a linearity of 0.680 and the remaining ones 0.671, within tolerance of 0.71 and 0.67 (0.684 and 0.678 over 10,000 pseudo-units).

## fig5c-sublinear-at-all-dt
**Result: reproduced.** The peak linearity index over dt of the 3,241 nonoptimal combinations has a mean of 0.703, below 1 and below the best-combination mean of 0.909 (p = 2e-61).

## supralinear-best-8-percent
**Result: reproduced.** Under O3 (a), 0.072 of the 318 selective sets (reading d) are significantly supralinear for their best combination, inside the tolerance band (0.072 to 0.088) at its lower edge, by either reference distribution; over all 463 sets the fraction is 0.093, and O3 (b) gives 0.129 and 0.151.

## fig6b-best-above-worst-below-scaled
**Result: reproduced.** The best combination exceeds the 0.64-scaled linear prediction in selective (p = 1e-37) and nonselective sets (p = 3e-19), and the worst combination falls below it (p = 3e-29 and 1.5e-7).

## fig6b-enhancement-not-different
**Result: not reproduced.** The rank-1 enhancement is 0.157 in selective and 0.112 spikes per stimulus in nonselective sets, a difference of 0.045 that the two-sample t-test finds (p = 0.0096); the variants give p = 0.012 and 0.004.

## fig6b-suppression-greater-selective
**Result: reproduced.** Residuals at ranks 7 and 8 are more negative in selective sets (-0.047 against -0.017 and -0.080 against -0.038), with Bonferroni-corrected p = 0.0085 and 0.0008 over eight ranks (0.0021 and 0.0002 over two).

## fig6c-enhancement-strongest-sw
**Result: partially reproduced.** In selective sets the residual differs with the rank of the SW's single-whisker response (ANOVA p = 1.6e-9) and is largest for the strongest SW (0.053). In nonselective sets the rank-1 residual (0.004) is below the mean of ranks 2 to 8, but the ANOVA does not find the trend (p = 0.17).

## fig7a-dt-half-width
**Result: reproduced (resting on an assumption).** Over the 248 selective sets whose best-combination curve is dt-modulated, the mean aligned curve falls halfway from its peak to its minimum at a half-width of 11.5 ms (reading a), within 10 +- 2 ms; the suboptimal mean is lower at the best dt (0.605 against 1.000) and does not fall to that level within +-100 ms. Including the 70 sets whose best curve is constant, and so has no best dt, gives 16.5 ms; the per-unit reading (b) gives 14.9 ms (74 sets with a defined value), and reading (c) is undefined because the mean curve stays above half its peak.

## fig7b-inbound-best-outbound-suboptimal
**Result: partially reproduced.** Z-scored within each unit, the mean best-combination curve of the 318 selective sets peaks at -50 ms and the suboptimal mean (2,226 curves) at +42 ms, below the best mean there. The minimum is at 0 ms for the best mean, -6 ms for the suboptimal mean and -3 ms pooled, none within -10 +- 1 ms; z-scoring each curve gives the same peaks and minima at 0, -5 and -3 ms.

## fig7c-pca
**Result: partially reproduced.** 373 best (0.81) and 1,204 suboptimal (0.37) curves are dt-modulated, within tolerance of 357 and 1,247. PC1 is sigmoidal with its sign change at 0 ms, and PC2 is U-shaped (0.107 for |dt| > 30 ms, -0.133 for |dt| < 10 ms); but three PCs explain 0.836 of the variance, above the tolerance band (0.675 to 0.825).

## fig7e-pc1-best-suboptimal
**Result: partially reproduced.** In selective sets, best combinations have negative PC1 weights (-2.37) and suboptimal ones positive (0.21), p = 8.9e-8. The pattern is not nearly absent in nonselective sets: their best-minus-suboptimal difference is 0.59 of the selective one (p = 0.016). For PC2, nonselective best and all suboptimal weights differ (p = 0.005); no PC3 pair differs.

## fig7f-inbound-sharper
**Result: partially reproduced.** Excluding the sets whose best curve is constant (reading c), inbound-preferring sets are more sharply tuned (CSI 0.109 against 0.083, p = 0.030 or 0.027) and better aligned (0.319 against 0.038 or 0.033, p = 1e-7); under readings (a) and (b) alignment holds (p = 5e-5) and the CSI difference does not (p = 0.11 and 0.10). The group sizes, 134 inbound and 112 or 114 outbound under reading (c), are outside 121 +- 12.1 and 56 +- 5.6.

## fig7g-inbound-decoding
**Result: not reproduced.** Decoding over the five negative dt ranges exceeds that over the five others by 0.014 (N = 187), 0.016 (N = 100), 0.014 (CW-tuned) and 0.019 (SW-tuned), each smaller than the mean bootstrap s.d. (0.057 to 0.075); accuracies stay between 0.094 and 0.165 (chance 0.125).

## supp8-order-decoding
**Result: not reproduced.** The order decoder reaches 0.581 at N = 100 over selective sets and 0.570 over all sets, below the tolerance band (0.585 to 0.715); chance is 0.5.

## exp3-units-cw-tuned
**Result: reproduced.** Of 81 units, 74 are responsive and 46 (0.62) CW-tuned under sham reading (a), and the mean single-whisker response is largest for the CW (0.845 spikes per stimulus); sham reading (b) and the variant without late-spike epochs give 75 to 78 and 46 to 47. The lick exclusion could not be applied.

## fig8c-awake-cw-stronger
**Result: partially reproduced.** The CW response above spontaneous is 0.709 spikes per stimulus in 46 awake CW-tuned units and 0.414 in 87 anesthetized ones, a ratio of 1.71, within tolerance of 2 +- 0.3, and awake tuning is sharper (mean SW/CW ratio 0.375 against 0.393). The two-sample t-test gives p = 0.0021, not below 0.001.

## fig8d-awake-best-sequence
**Result: reproduced.** The slope with an intercept is 1.234 (reading b, within 1.24 +- 0.124; 1.300 through the origin), and 73 of 74 units (0.986) respond more to their best sequence.

## exp3-combination-selective
**Result: reproduced.** 27 of 74 responsive units (0.365) are combination-selective after FDR control, within tolerance of 29 and 0.39; the best sequence contains the CW for 0.704 of selective and 0.784 of all responsive units, within tolerance of 0.76 and 0.80.

## fig8h-awake-linearity
**Result: partially reproduced.** The linearity index is 0.941 +- 0.028 for best and 0.723 +- 0.009 for suboptimal combinations (p = 1.5e-16), against 0.93 +- 0.03 and 0.71 +- 0.009: the best mean is within tolerance, the suboptimal mean misses it and lies within 10% of 0.71.

## fig8i-awake-sharper-than-linear
**Result: reproduced.** Measured CSI (0.057) is above linear CSI (0.023) in 70 of 74 units (0.946), paired t-test p = 9e-9.

## fig8j-awake-inbound-stronger
**Result: reproduced.** Z-scored peak responses are largest at -40 ms under both readings (1.95, 0.93 and 1.36 at -40, 0 and +40 ms, ANOVA p = 8e-14; 1.75, 0.10 and 0.64, p = 2.6e-15).

## fig8k-awake-binary-decoder
**Result: reproduced.** Over the 27 selective units, accuracy rises with ensemble size, from 0.652 and 0.674 at N = 5 to 0.815 and 0.829 at N = 25 (readings a and b).
EOF
echo done
```

```
152:print("note: the ten ranges are those of the claims file; dt = +40 ms falls in none of them")
done
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nb && python - <<'EOF'
s=open('results.md').read()
s=s.replace(''' The p-values do not depend much on how the covariance is inverted (a check on 40 sets, not in this notebook, gave more selective sets with larger regularization).''','')
s=s.replace('''**Result: reproduced.** 87 of 144 responsive units are CW-tuned and 57 SW-tuned (fraction 0.604), all within tolerance of 89, 53 and 0.61; sham reading (b) gives 89 and 58 (0.605).''','''**Result: reproduced (resting on an assumption).** 87 of 144 responsive units are CW-tuned and 57 SW-tuned (fraction 0.604), all within tolerance of 89, 53 and 0.61; sham reading (b) gives 89 and 58 (0.605). With both directions of singles pooled, 86 are CW-tuned and 69 SW-tuned, outside the tolerance of 53, so the outcome rests on the caudal reading.''')
open('results.md','w').write(s)
EOF
cat > 90_summary.py <<'EOF'
# %% [markdown]
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| exp1-units | reproduced (assumption: caudal singles) |
| fig1b-somatotopy | reproduced |
| exp1-cw-tuned-fraction | reproduced (assumption: caudal singles) |
| exp1-cw-sw-comparable-firing | partially reproduced |
| supp1d-sw-tuning-broader | reproduced |
| fig1d-best-sequence-exceeds-single | reproduced |
| fig1e-best-combination-includes-cw | partially reproduced (assumption: caudal singles) |
| fig1f-cwsw-exceeds-swsw | reproduced |
| fig1g-cwsw-sharper | reproduced |
| supp2-sw-tuned-sharpest-cwsw | reproduced |
| exp2-units | reproduced |
| methods-dt-modulation | not reproduced |
| exp2-combination-selective-prevalence | not reproduced |
| fig2f-shuffle-abolishes-tuning | reproduced |
| fig2f-most-selective-lower-firing | reproduced |
| supp4-selectivity-at-high-rates | partially reproduced |
| fig2g-best-combination-bias | reproduced |
| fig3a-sharper-than-linear | reproduced |
| fig3b-sharper-in-both-groups | reproduced |
| fig3b-linear-sharper-in-selective | reproduced |
| supp6-layers | partially reproduced |
| fig3e-identity-decoder | not reproduced |
| fig3g-binary-decoder | not reproduced |
| fig4a-sw-tuned-sharper | reproduced |
| fig4c-sw-tuned-decoding | partially reproduced |
| fig5a-global-scaling | reproduced |
| fig5bc-linearity-index | partially reproduced |
| fig5c-pseudo-unit-shuffle | reproduced |
| fig5c-sublinear-at-all-dt | reproduced |
| supralinear-best-8-percent | reproduced |
| fig6b-best-above-worst-below-scaled | reproduced |
| fig6b-enhancement-not-different | not reproduced |
| fig6b-suppression-greater-selective | reproduced |
| fig6c-enhancement-strongest-sw | partially reproduced |
| fig7a-dt-half-width | reproduced (assumption: sets without a best dt left out of the alignment) |
| fig7b-inbound-best-outbound-suboptimal | partially reproduced |
| fig7c-pca | partially reproduced |
| fig7e-pc1-best-suboptimal | partially reproduced |
| fig7f-inbound-sharper | partially reproduced |
| fig7g-inbound-decoding | not reproduced |
| supp8-order-decoding | not reproduced |
| exp3-units-cw-tuned | reproduced |
| fig8c-awake-cw-stronger | partially reproduced |
| fig8d-awake-best-sequence | reproduced |
| exp3-combination-selective | reproduced |
| fig8h-awake-linearity | partially reproduced |
| fig8i-awake-sharper-than-linear | reproduced |
| fig8j-awake-inbound-stronger | reproduced |
| fig8k-awake-binary-decoder | reproduced |
| fig8b-awake-behavior | blocked: data missing (no lick times or trial types) |

How the analysis differs from the paper's:

- The paper's code is not public; every method comes from the claims file and the Methods. Details the paper leaves open are run under each reading the claims file names.
- Experiment 1: the files hold both deflection directions of each single whisker; the caudal ones are taken as the paper's nine single-whisker stimuli (they give the paper's unit counts; the pooled reading is shown). Sequence trials are pooled over directions.
- Experiment 2: one of two units with identical spike trains is dropped (246 cells, 463 responsive sets). Units are grouped by their trial sequence, not by recName. The selective set found by the shuffle test (318 sets) is larger than the paper's (187), and every later claim on selective units uses it. Sets whose best-combination curve is set constant across dt have no defined best dt; they are flagged and, for Fig. 7a and reading (c) of Fig. 7f, left out.
- Experiment 3: lick times are not in the files, so epochs near licks are not excluded; epochs are aligned to the first deflection, as the CW latencies show.

What was found about the dataset:

- The three experiments are present with the paper's counts of units (160, 247 and 81), recording sites (8 in experiment 1), mice (5, 12 and 4) and sessions (6 in experiment 3).
- Experiment 1 files hold rostral as well as caudal single-whisker deflections (18 single-whisker stimuli, not the paper's 9). In both 20170510 recordings the sequences involving whisker 3 or 8 are coded with that whisker deflected rostrally.
- Nine experiment 2 recordings hold 16,000 to 24,000 three-whisker trials, which neither the paper nor the data descriptor mentions. CW-SW dt takes 101 values (-50 to +50 ms), not 100.
- Two experiment 2 units (20160909, recNames chn3 and chn4, depths 250 and 150 um) have identical spike trains. In 20160803 and 20160909 some units carry the recName of another recording than the one whose trials they hold. Two experiment 2 recordings (20160225, 20160316) have no sham trials.
- Experiment 3 files have no deflection times, no lick times, no trial types and no per-unit depth; the DeltaT sign convention is not documented. About a third of experiment 3 spike times lie after the 300 ms epoch, up to 425 s, in 5.6% of unit-epochs.
EOF
python - <<'EOF'
# build: insert result cells after the last cell of each claim
import re, nbformat
p='/tmp/claude-1001/nb/'
files=['05_header.py','00_load.py','01_check.py','10_exp1.py','20_exp2_core.py','21_exp2_shuffle.py','22_exp2_a.py','23_exp2_b.py','24_exp2_c.py','25_exp2_d.py','26_exp2_e.py','27_exp2_f.py','28_exp2_g.py','29_exp2_dec.py','30_exp3.py','90_summary.py']
open(p+'build2.py','w').write('''
import re, sys, nbformat
p = "/tmp/claude-1001/nb/"
files = %r
res = {}
for block in re.split(r"^## ", open(p + "results.md").read(), flags=re.M)[1:]:
    cid, _, body = block.partition("\\n")
    res[cid.strip()] = body.strip()
cells = []
for f in files:
    for block in re.split(r"^# %%%%", open(p + f).read(), flags=re.M)[1:]:
        head, _, body = block.partition("\\n")
        body = body.strip("\\n")
        head = head.strip()
        if head.startswith("[markdown]"):
            cells.append(nbformat.v4.new_markdown_cell(body))
        else:
            c = nbformat.v4.new_code_cell(body)
            if head:
                c.metadata["tags"] = [t.strip() for t in head.replace("tags=", "").split(",") if t.strip()]
            cells.append(c)
last = {}
for i, c in enumerate(cells):
    for t in c.metadata.get("tags", []):
        if t.startswith("claim:"):
            last[t[6:]] = i
missing = set(res) - set(last)
assert not missing, missing
for cid, i in sorted(last.items(), key=lambda kv: -kv[1]):
    cells.insert(i + 1, nbformat.v4.new_markdown_cell(res[cid]))
nb = nbformat.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nb.metadata["language_info"] = {"name": "python"}
nbformat.write(nb, sys.argv[1])
print(len(cells), "cells;", len(last), "claims")
''' % files)
EOF
. ../dev/bin/activate && python build2.py entries/laboy-juarez-2019/reproduce_laboy_juarez_2019.ipynb
```

```
170 cells; 49 claims
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019 && cat > entry.yaml <<'EOF'
schema_version: 1
name: laboy-juarez-2019
type: reproduction
title: Two-whisker sequence tuning in mouse S1 (Laboy-Juarez et al. 2019)
description: Tests the findings of Laboy-Juarez, Langberg, Ahn and Feldman (2019) on CRCNS ssc-9, which
  holds the spike times of single units in mouse barrel cortex during single- and two-whisker
  stimulation in the paper's three experiments (anesthetized survey, dense dt mapping, awake mice).
  It covers responsiveness and single-whisker tuning, combination selectivity, linear and
  nonlinear integration, dt tuning, population decoders, and the awake replication. The lick
  times needed for the behavioral claim are not in the files.
license: Apache-2.0
notebooks:
- path: reproduce_laboy_juarez_2019.ipynb
  title: Reproducing Laboy-Juarez et al. (2019) from CRCNS ssc-9
  runtime_minutes: 15
helpers:
- lj2019.py
related:
- id: crcns:ssc-9/unversioned
  relation: uses_data
- id: doi:10.1038/s41593-019-0448-6
  relation: reproduces
EOF
cat > requirements.in <<'EOF'
aiohttp
fsspec
matplotlib
numpy
pandas
requests
scikit-learn
scipy
EOF
cd  && grep -n "matplotlib\|plt" $TMPDIR/nb/*.py | head -3; python tools/entry.py lock entries/laboy-juarez-2019 2>&1 | tail -3 && python tools/entry.py check entries/laboy-juarez-2019 2>&1 | tail -10
```

```
/tmp/claude-1001/nb/00_load.py:8:import matplotlib.pyplot as plt
/tmp/claude-1001/nb/01_check.py:8:import matplotlib.pyplot as plt
wrote laboy-juarez-2019/requirements.lock.txt (Python 3.13, with hashes)
error: entries/laboy-juarez-2019/reproduce_laboy_juarez_2019.ipynb: neither the notebook nor a helper names version unversioned of dataset ssc-9, which entry.yaml pins
1 error(s)
```

**Agent calls Bash**

```bash
grep -n "names version" -B25 tools/entry.py | grep -v "^\s*$" | head -40
```

```
219-    archives = {r["id"].split(":", 1)[1].partition("/")[0]: r["id"].split(":", 1)[0]
220-                for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))}
221-    dandisets = [d for d, _, _ in used]
222-    versions = {d: v for d, _, v in used}
223-    if entry.get("type") in ("orientation", "reproduction"):
224-        if not dandisets:
225-            report.error(rel / "entry.yaml", "an orientation or reproduction entry must relate to a dataset")
226-        for d, v in versions.items():
227-            if not v:
228-                report.error(rel / "entry.yaml", f"pin the version of dataset {d}, as {archives[d]}:{d}/<version>")
229-    helper_code = "\n".join((entry_dir / h).read_text() for h in helpers if (entry_dir / h).is_file())
230-
231-    for name in [n for n in listed if n in present]:
232-        path = entry_dir / name
233-        nb = nbformat.read(path, as_version=4)
234-        if any(c.cell_type == "code" and (c.get("outputs") or c.get("execution_count")) for c in nb.cells):
235-            report.error(rel / name, "commit notebooks without outputs (clear them before committing)")
236-        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
237-            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
238-        code = code_of(path)
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019 && python - <<'EOF'
s=open('lj2019.py').read()
old='''URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip"'''
new='''DATASET = "ssc-9"
# CRCNS data sets are not versioned (docs/archives.md); the file read is pinned by its MD5 sum
# from the data set's checksums.md5.
VERSION = "unversioned"
DATA_MD5 = "2e7a774017619e76c46db85722587be3"
URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip"'''
s=s.replace(old,new); open('lj2019.py','w').write(s)
EOF
cd $TMPDIR/nb && python - <<'EOF'
p='05_header.py'; s=open(p).read()
old='''import hashlib
import fsspec
h = hashlib.md5()
with fsspec.open("https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-9/live/data.zip", block_size=2 ** 22) as f:
    for chunk in iter(lambda: f.read(2 ** 22), b""):
        h.update(chunk)
print("data.zip MD5", h.hexdigest(), "| matches checksums.md5:", h.hexdigest() == "2e7a774017619e76c46db85722587be3")'''
new='''import hashlib
import fsspec
import lj2019 as L
h = hashlib.md5()
with fsspec.open(L.URL, block_size=2 ** 22) as f:  # streamed in chunks, not stored
    for chunk in iter(lambda: f.read(2 ** 22), b""):
        h.update(chunk)
print(f"CRCNS {L.DATASET}, version {L.VERSION}: data.zip MD5 {h.hexdigest()}, matches checksums.md5: {h.hexdigest() == L.DATA_MD5}")'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
. ../dev/bin/activate && python build2.py entries/laboy-juarez-2019/reproduce_laboy_juarez_2019.ipynb && cd  && python tools/entry.py check entries/laboy-juarez-2019 2>&1 | tail -5; date -u
```

```
170 cells; 49 claims
0 error(s)
Thu Nov 12 18:14:40 UTC 2026
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/laboy-juarez-2019 2>&1 | tail -15; date -u
```

```
Installed kernelspec registry-laboy-juarez-2019 in executed/laboy-juarez-2019/.venv/share/jupyter/kernels/registry-laboy-juarez-2019
0 error(s)
pass  reproduce_laboy_juarez_2019.ipynb  (775 s)

real	13m3.218s
user	40m7.570s
sys	0m10.238s
Thu Nov 12 18:27:48 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import nbformat
nb=nbformat.read('executed/laboy-juarez-2019/reproduce_laboy_juarez_2019.ipynb',4)
out=[]
for c in nb.cells:
  if c.cell_type=='code':
    for o in c.get('outputs',[]):
      if o.get('name')=='stdout': out.append(o['text'])
      elif o.get('output_type')=='error': out.append('ERROR '+o['ename'])
open('exec_out.txt','w').write(''.join(out))
" && grep -v -E "^[0-9]{8}:" exec_out.txt > a.txt; grep -v -E "^--- cell|^[0-9]{8}:" nb/full.log > b.txt; diff <(sort a.txt) <(sort b.txt) | head -60
```

```
5d4
<                   main (caudal singles, all sequence trials)               (i) both directions of singles     (ii) same-direction sequence trials only
188d186
< CRCNS ssc-9, version unversioned: data.zip MD5 2e7a774017619e76c46db85722587be3, matches checksums.md5: True
198,199c196,197
< Experiment 2 CW-SW dt values: -50 to 50 in 101 values (the paper says 100 values within +-50 ms)
< Experiment 2 trials per CW-SW combination and dt, mean over recordings: correlated 9.68 | anti-correlated 9.66 (the paper gives 8.42 +- 4.2 per unique sequence)
---
> Experiment 2 CW-SW dt values:  [np.int64(-50), np.int64(-49), np.int64(-48)] ... 101 values (the paper says 100)
> Experiment 2 CW-SW trials per combination and dt, mean: 4.83
203,225d200
< Experiment1/20170510.mat: 38 units
< Experiment1/20170513.mat: 21 units
< Experiment1/20170515.mat: 34 units
< Experiment1/20170605.mat: 28 units
< Experiment1/20170621.mat: 39 units
< Experiment2/20160225.mat: 8 units
< Experiment2/20160316.mat: 2 units
< Experiment2/20160325.mat: 14 units
< Experiment2/20160406.mat: 21 units
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && diff <(sort a.txt) <(sort b.txt) | sed -n '60,200p' | grep -v -E "^< (p_broader|responsive|slope_intercept|spont_|sw_tuned)"
```

```
< order            CW > rostral within-row > caudal within-row  CW > rostral within-row > caudal within-row  CW > rostral within-row > caudal within-row
---
> note: the range [40, 40] is dropped by the Fig. 7g bins ([31, 40] would be next); the paper's ten ranges are used as the claims file gives them
332c293
< reading (b), zero padding: curves 3704, monotonic 0.011, unsmoothed 0.000, constant 39 (0.011); 96 s
---
> reading (b), zero padding: curves 3704, monotonic 0.011, unsmoothed 0.000, constant 39 (0.011); 89 s
337d297
364c324
< shuffle tests: 363 s
---
> shuffle tests: 371 s
368,370d327
372d328
Shell cwd was reset to
```

**Agent calls Bash**

```bash
sed -n 1,80p attempts/fouke-2025-01.yaml; grep -n -E "^[a-z_]+:" attempts/fouke-2025-01.yaml
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
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,320p attempts/fouke-2025-01.yaml; ls schemas; grep -n -E "blocked_by|assumed|missing_datasets|found|about|kind" schemas/attempt*.json | head -40
```

```
blocked_by: metadata_insufficient
  notes: The numbers come from single representative fish and trials. Fig1-S1.ipynb selects them
    by the index of a data folder and a trial number (for example DC folder 29, trial 79), and the
    dandiset gives no mapping from those folders to its subjects, nor the original file names.
- claim: fig2d-shared-architecture
  outcome: blocked
  blocked_by: data_missing
  notes: The two-photon imaging data are not in the dandiset, which holds only freely swimming
    tracking. The GitLab repository the paper names for "all behavioral and imaging data" holds
    notebooks only, and no other dandiset of this lab or paper was found on the archive.
- claim: fig2g-dsi-similar
  outcome: blocked
  blocked_by: data_missing
  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
- claim: fig2h-fewer-motion-responsive
  outcome: blocked
  blocked_by: data_missing
  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
- claim: fig2k-more-monocular
  outcome: blocked
[... 129 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,140p schemas/attempt.schema.json | grep -v '^\s*$' | head -140
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
    "datasets",
    "paper",
    "date",
    "provenance",
    "outcomes"
  ],
  "properties": {
    "schema_version": {
      "const": 3
    },
    "id": {
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 140,300p schemas/attempt.schema.json | grep -E '"[a-z_]+": \{|enum|required|description' | head -60
```

```
"superseded_by": {
          "description": "The id of the attempt that replaces it, once there is one.",
    "provenance": {
      "required": [
      "properties": {
        "kind": {
          "enum": [
        "accountable": {
          "description": "The person or organisation responsible for this attempt.",
          "required": [
          "properties": {
            "name": {
            "orcid": {
            "ror": {
        "agent": {
          "description": "Required when kind is agent.",
          "required": [
          "properties": {
            "harness": {
            "model": {
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']['properties']
print(json.dumps(o['measured'])[:400]); print(o['outcome']['enum'], o['blocked_by']['enum'])
f=s['properties']['findings']['items']; print(f['required'], f['properties']['kind']['enum'])
print(list(s['properties'].keys()))
print(json.dumps(s['properties']['inputs'])[:300])
"
```

```
{"description": "The values obtained, for claims with expected values: one number, or one per expected value, in the same order.", "oneOf": [{"type": "number"}, {"type": "array", "minItems": 1, "items": {"type": "number"}}]}
['reproduced', 'partially_reproduced', 'not_reproduced', 'blocked'] ['data_missing', 'metadata_insufficient', 'methods_underspecified', 'data_unreadable', 'dataset_missing', 'too_large', 'not_runnable', 'other']
['kind', 'statement'] ['metadata_error', 'data_missing', 'identifier_missing', 'metadata_insufficient', 'selection_undocumented', 'methods_unavailable', 'format_error', 'code_mismatch', 'paper_inconsistency', 'other']
['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
{"description": "Everything the attempt used that is not in the dataset.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["what", "source"], "properties": {"what": {"type": "string", "minLength": 1}, "source": {"description": "A DOI, or a repository URL with
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/rec && cat > $TMPDIR/rec/make.py <<'PYEOF'
import yaml
NB = "reproduce_laboy_juarez_2019.ipynb"
CAUDAL = ("Assumption. The experiment 1 files hold each single whisker deflected in both directions (18 "
          "single-whisker stimuli), where the paper describes 9 single-whisker deflections. The caudal "
          "deflections are taken as the paper's nine, as experiment 3, whose stimuli the Methods call "
          "identical to experiment 1 apart from amplitude and dt (Methods, Recordings in awake behaving "
          "mice), used caudal deflections only, and as this reading gives the paper's unit counts. The "
          "notebook shows both directions pooled as a variant.")
PAIRS = ("Sequence responses pool all trials of a sequence over deflection directions. In the two 20170510 "
         "recordings the sequences involving whisker 3 or 8 were delivered with that whisker deflected "
         "rostrally, so a same-direction reading would drop them; the notebook shows it as a variant.")
SHAM = ("Sham reading (a) of the claims file (O1), the 125 ms window at the time single deflections occur, "
        "is used for the responsive set of the later claims; reading (b) is shown for the counts.")
SEL2 = ("The selective sets are those this attempt's shuffle test finds (318 of 463 responsive sets, "
        "against the paper's 187 of 451); see exp2-combination-selective-prevalence.")
DUP = ("One of two experiment 2 units with identical spike trains (20160909) is dropped, so experiment 2 "
       "has 246 cells and 463 responsive sets under the main readings (O2 a, sham a).")
O2O3 = "Main readings O2 (a) and O3 (a); the other combinations are shown in the notebook."
NOLICK = ("The exclusion of epochs within 200 ms of a lick (Methods, Recordings in awake behaving mice) is "
          "not applied, as the files hold no lick times.")
CONST = ("Assumption. Sets whose best-combination curve is set constant across dt (Methods, dt smoothing) "
         "have no best dt, and the maximum of the cwSTRF falls on the first tied dt (-50 ms); they are "
         "left out of the alignment on the best dt, as an alignment needs a best dt. The notebook shows "
         "the result with them included.")

def oc(claim, outcome, notes, measured=None, deviations=None, assumed=None, blocked_by=None):
    d = {"claim": claim, "outcome": outcome}
    if blocked_by:
        d["blocked_by"] = blocked_by
    else:
        d["notebook"] = NB
        d["output"] = f"claim:{claim}"
    if measured is not None:
        d["measured"] = measured
    d["notes"] = notes
    if deviations:
        d["deviations"] = deviations
    if assumed:
        d["assumed"] = True
    return d

outcomes = [
 oc("exp1-units", "reproduced",
    "160 units in 8 recordings from 5 mice; 144 responsive under sham reading (a), 36 in L2/3, 48 in L4, 46 in L5 "
    "and 14 in L6, all within tolerance. Sham reading (b) gives 147 (36, 50, 47, 14). With both directions of "
    "the singles pooled, 155 are responsive and 52 lie in L5, outside 44 +- 4.4, so the outcome rests on the "
    "caudal reading.", [160, 144, 36, 48, 46, 14], [CAUDAL], True),
 oc("fig1b-somatotopy", "reproduced",
    "Mean responses over the 144 responsive units are largest for the CW (0.517 spikes per stimulus), then the "
    "rostral (0.368) and caudal (0.327) within-row SWs. The order is the same under both direction variants.",
    deviations=[CAUDAL]),
 oc("exp1-cw-tuned-fraction", "reproduced",
    "87 CW-tuned and 57 SW-tuned of 144 (0.604), within tolerance; sham reading (b) gives 89 and 58. With both "
    "directions of the singles pooled, 86 and 69, the SW-tuned count outside 53 +- 5.3.",
    [87, 57, 0.604], [CAUDAL], True),
 oc("exp1-cw-sw-comparable-firing", "partially_reproduced",
    "Spontaneous rates match (1.33 +- 0.14 Hz CW-tuned, 2.05 +- 0.43 Hz SW-tuned under sham reading a; 1.27 and "
    "2.01 under b). Maximal evoked firing does not; the best single-whisker response is 0.58 and 0.60 spikes "
    "per stimulus and the best response over all 261 stimuli 0.86 and 0.91, against 4.8 and 4.56, so no "
    "reading of maximal evoked firing in spikes per stimulus in the 125 ms window comes near the paper's values. "
    "The groups do not differ in maximal firing (t-test p = 0.84 and 0.65); spontaneous p = 0.067 (a) and 0.042 (b).",
    [1.332, 2.052, 0.581, 0.601], [CAUDAL]),
 oc("supp1d-sw-tuning-broader", "reproduced",
    "Mean normalized response over ranks 2 to 9 is 0.482 for SW-tuned and 0.393 for CW-tuned units; one-factor "
    "ANOVA p = 0.00072 (reading a) and 1.6e-10 (reading b), 0.00016 with both directions pooled.",
    deviations=[CAUDAL]),
 oc("fig1d-best-sequence-exceeds-single", "reproduced",
    "Slope 1.211 with an intercept (reading b, within tolerance) and 1.345 through the origin (reading a); 143 of "
    "144 units (0.993) respond more to the best sequence. Both direction variants give slopes 1.185 and 1.258.",
    1.211, [CAUDAL, PAIRS]),
 oc("fig1e-best-combination-includes-cw", "partially_reproduced",
    "The best combination contains the CW for 0.688 of all units and 0.862 of CW-tuned units, within tolerance, "
    "and 0.421 of SW-tuned units, just below the band 0.423 to 0.517 (chance 0.222). With both directions of the "
    "singles pooled (0.671, 0.837, 0.464) or with same-direction sequence trials only (0.694, 0.851, 0.456) all "
    "three fractions are within tolerance; the outcome rests on the main reading.",
    [0.688, 0.862, 0.421], [CAUDAL, PAIRS], True),
 oc("fig1f-cwsw-exceeds-swsw", "reproduced",
    "99 of 144 units above the diagonal under both z-scoring readings; mean difference 0.54 (a) and 0.47 (b), "
    "paired t-test p = 1e-6 in both.", deviations=[CAUDAL, PAIRS]),
 oc("fig1g-cwsw-sharper", "reproduced",
    "Mean CW-SW sparseness is above SW-SW sparseness at all 55 values of N (0.094 against 0.044 at N = 56). The "
    "per-N paired t-tests are descriptive (largest p 0.20).", deviations=[PAIRS]),
 oc("supp2-sw-tuned-sharpest-cwsw", "reproduced",
    "SW-tuned units have higher CW-SW sparseness than CW-tuned units at all 55 values of N (0.129 against 0.070 "
    "at N = 56).", deviations=[CAUDAL]),
 oc("exp2-units", "reproduced",
    "247 units in 12 files (12 mice), 246 after dropping a duplicate; 231 responsive to correlated and 232 to "
    "anti-correlated stimuli under O2 (a) and sham (a), and 237 to 240 under the other readings, all within "
    "tolerance. Layer counts (correlated/anti) are 52/51 L2/3, 79/80 L4, 73/74 L5 and 26/27 L6, against "
    "54/54, 78/79, 71/70 and 21/24. Two recordings without sham trials are tested on the nine whiskers alone.",
    [247, 231, 232], [DUP, "Responsiveness in the two recordings without sham trials (20160225, 20160316) is tested "
     "across the nine whiskers alone."]),
 oc("methods-dt-modulation", "not_reproduced",
    "Of 3,704 CW-SW curves of the responsive sets, under reading (a) 0.574 have likelihoods rising to the largest "
    "kernel, none is best unsmoothed, and 2,127 (0.574) are set constant; the total is within tolerance of 2,004 "
    "but the fractions are far from 0.33 and 0.23. The unsmoothed 1 ms curve never beats a smoothed one in "
    "held-out likelihood here. Under reading (b), zero padding, 39 curves (0.011) are set constant. All 3,936 "
    "curves give 0.583 under reading (a).", [0.574, 0.0, 2127],
    ["Zero rates in the held-out likelihood are floored at 1e-3 spikes (a standard choice; the paper does not say).",
     "The 3,704 curves are those of this attempt's 463 responsive sets, against the paper's 3,608."]),
 oc("exp2-combination-selective-prevalence", "not_reproduced",
    "318 of 463 responsive sets are selective with FDR over all sets (312 with the two sets apart), in 189 of 246 "
    "cells (0.768), against 187 sets and 129 cells (0.52). Fractions are 0.641 and 0.733 of responsive correlated "
    "and anti-correlated sets, or 0.602 and 0.691 of all cells, against 0.35 and 0.46. 340 sets have uncorrected p "
    "< 0.05. The paper states no false-positive rate for the test.",
    [189, 0.768, 0.641, 0.733, 318, 145],
    ["A shuffled curve of a combination whose measured curve was set constant across dt is set to its own mean "
     "over dt (the Methods say each shuffled curve is smoothed with its measured kernel; a constant curve has none).",
     "The Mahalanobis distance uses the pseudo-inverse of the shuffle covariance (smoothed CSI traces are nearly "
     "collinear across dt).", DUP]),
 oc("fig2f-shuffle-abolishes-tuning", "reproduced",
    "Mean peak-aligned tuning of the 318 selective sets has a CSI of 0.033; one shuffle per set gives CSI 0.000 "
    "aligned to the measured best and 0.003 aligned to its own peak; the shuffled first point exceeds the other "
    "seven by 0.011, within its s.e.m. (0.027).", deviations=[SEL2, O2O3]),
 oc("fig2f-most-selective-lower-firing", "reproduced",
    "Most against least selective quarter (79 sets each) spontaneous 0.83 against 3.94 Hz (p = 4e-13), best "
    "response 0.61 against 1.24 spikes per stimulus (p = 4e-10), mean of eight 0.31 against 1.01 (p = 4e-19).",
    deviations=[SEL2]),
 oc("supp4-selectivity-at-high-rates", "partially_reproduced",
    "After subtracting spontaneous firing, the peak-aligned tuning of the 128 high-rate selective sets with sham "
    "trials has a peak 0.451 above the mean of the other seven, 22.9 times its s.e.m. The counts are 178, 140 and "
    "28 against 95, 92 and 91, following from the larger selective set.", [178, 140, 28], [SEL2]),
 oc("fig2g-best-combination-bias", "reproduced",
    "Rayleigh p = 1.1e-22 over 463 sets; every SW is best for at least 14; rostral within-row most frequent (150); "
    "ventral row 210 against dorsal row 63.",
    deviations=["The Rayleigh p-value uses Zar's approximation; angles place the eight SWs at 45 degree steps by "
     "face position (O5)."]),
 oc("fig3a-sharper-than-linear", "reproduced",
    "Measured CSI 0.086 against linear 0.035, paired p = 3e-43, 0.911 of 463 sets above (O3 a, O2 a); the other "
    "readings give 0.946 to 0.991 above and p below 1e-46.", deviations=[O2O3]),
 oc("fig3b-sharper-in-both-groups", "reproduced",
    "Selective 0.093 against 0.040 (two-sample p = 1.4e-19), nonselective 0.071 against 0.023 (p = 5.5e-8); all "
    "readings and the paired variant give p < 0.005.", deviations=[SEL2]),
 oc("fig3b-linear-sharper-in-selective", "reproduced",
    "Linear CSI 0.0399 in selective against 0.0234 in nonselective sets, p = 7.3e-5 (O2 b, p = 3.7e-6).",
    deviations=[SEL2]),
 oc("supp6-layers", "partially_reproduced",
    "Log10 CSI differs by layer (ANOVA p = 2.4e-5 over all responsive sets, 0.0015 over selective sets), with "
    "L2/3 (-1.13) and L4 (-1.24) above L5 (-1.39) and L6 (-1.34). Layer counts 103, 159, 147 are within tolerance "
    "and L6 (53) is not (45 +- 4.5). One set lies outside the layer bounds.", [103, 159, 147, 53]),
 oc("fig3e-identity-decoder", "not_reproduced",
    "Accuracy at N = 187 selective sets is 0.135 (chance 0.125) against 0.42; the summed probabilities favour the "
    "rostral within-row combination, which is the best of 111 of the 318 selective sets (accuracy 0.986 for it, 0 "
    "to 0.039 for the others; dorsal row 0.0 to 0.034). Single-unit held-out accuracy averages 0.142. The "
    "linear-prediction decoder is lower by 0.008, less than the sum of the s.d. (0.072).",
    [0.135, 0.986, 0.0, 0.034],
    [SEL2, "Logistic regressions are fitted by Newton's method with a small ridge (1e-4) to keep separated "
     "classes finite; held-out probabilities by tenfold cross-validation, one test trial per unit and "
     "combination per ensemble (O6)."]),
 oc("fig3g-binary-decoder", "not_reproduced",
    "N = 10 accuracy 0.609 (reading a) and 0.616 (b) over selective sets, 0.591 and 0.585 over all sets, below "
    "0.63; N = 100 accuracy 0.817 and 0.818 (selective), 0.763 and 0.747 (all).", 0.609, [SEL2]),
 oc("fig4a-sw-tuned-sharper", "reproduced",
    "O2 (a) 174 CW-tuned and 289 SW-tuned sets, within tolerance; CSI 0.103 against 0.058, p = 3.6e-7. O2 (b) 216 "
    "and 247 (outside), p = 7.5e-5.", [174, 289]),
 oc("fig4c-sw-tuned-decoding", "partially_reproduced",
    "Over all sets (reading b) SW-tuned decoders beat CW-tuned at every size (0.130 against 0.114 at N = 10, 0.135 "
    "against 0.132 at N = 150); over selective sets (a) CW-tuned are higher from N = 100. CW-tuned accuracy at N = "
    "150 (0.132 all, 0.155 selective) is not above 0.125 by two s.d. (0.061, 0.075).", deviations=[SEL2]),
 oc("fig5a-global-scaling", "reproduced",
    "Slope through the origin 0.636, R2 0.926 centred and 0.967 uncentred, over 3,704 combinations (O3 a, O2 a); "
    "other readings give slopes 0.620 to 0.643.", [0.636, 0.926, 3704], [O2O3]),
 oc("fig5bc-linearity-index", "partially_reproduced",
    "Nonoptimal 0.645 +- 0.003 and best 0.909 +- 0.021 (two-sample p = 1.6e-120), against 0.63 +- 0.003 and 0.95 "
    "+- 0.02; both outside tolerance and within 10%; O3 (b) puts the best mean (0.964) within tolerance but not "
    "the nonoptimal (0.652).", [0.645, 0.909], [O2O3]),
 oc("fig5c-pseudo-unit-shuffle", "reproduced",
    "463 pseudo-units give 0.680 for the strongest and 0.671 for the remaining responses; 10,000 give 0.684 and "
    "0.678.", [0.680, 0.671]),
 oc("fig5c-sublinear-at-all-dt", "reproduced",
    "Mean peak linearity index over dt for 3,241 nonoptimal combinations is 0.703, below 1 and below the best "
    "combination mean 0.909, p = 2e-61."),
 oc("supralinear-best-8-percent", "reproduced",
    "Under O3 (a), 0.072 of the 318 selective sets (reading d) are supralinear by either reference, at the lower "
    "edge of 0.08 +- 0.008; over all 463 sets 0.093, and under O3 (b) 0.129 and 0.151.", 0.072,
    [SEL2, "The standard errors of the single-whisker means are those of the directions in the set's stimuli (O2 a)."]),
 oc("fig6b-best-above-worst-below-scaled", "reproduced",
    "Best above 0.64-scaled linear in selective (p = 1e-37) and nonselective sets (p = 3e-19); worst below (p = "
    "3e-29 and 1.5e-7).", deviations=[SEL2]),
 oc("fig6b-enhancement-not-different", "not_reproduced",
    "Rank-1 enhancement 0.157 (selective, 318) against 0.112 (nonselective, 145) spikes per stimulus, difference "
    "0.045, two-sample t-test p = 0.0096 (variants p = 0.012 and 0.004).", deviations=[SEL2]),
 oc("fig6b-suppression-greater-selective", "reproduced",
    "Rank 7 residual -0.047 against -0.017 (p = 0.0011), rank 8 -0.080 against -0.038 (p = 0.0001); Bonferroni "
    "over eight ranks 0.0085 and 0.0008, over two 0.0021 and 0.0002.", deviations=[SEL2]),
 oc("fig6c-enhancement-strongest-sw", "partially_reproduced",
    "Selective sets ANOVA p = 1.6e-9 with the strongest-SW residual largest (0.053); nonselective sets have the "
    "rank-1 residual (0.004) below the mean of ranks 2 to 8 but ANOVA p = 0.17.",
    deviations=[SEL2, "SW ranks are by single-whisker response in the set's directions (O2 a)."]),
 oc("fig7a-dt-half-width", "reproduced",
    "Over 248 selective sets with a dt-modulated best curve the mean aligned curve has a half-width of 11.5 ms "
    "(reading a); the suboptimal mean is 0.605 at the best dt and does not fall halfway within +-100 ms. With the "
    "70 constant-curve sets included, 16.5 ms; reading (b) 14.9 ms (74 sets with a defined value); reading (c) "
    "undefined (the mean stays above half its peak).", 11.5, [CONST, SEL2], True),
 oc("fig7b-inbound-best-outbound-suboptimal", "partially_reproduced",
    "Z-scored per unit, the best-combination mean (318) peaks at -50 ms and the suboptimal mean (2,226) at +42 ms, "
    "below the best there; minima at 0 (best), -6 (suboptimal) and -3 ms (pooled), none within -10 +- 1. Z-scoring "
    "each curve gives minima at 0, -5 and -3 ms.", 0, [SEL2]),
 oc("fig7c-pca", "partially_reproduced",
    "373 best (0.81) and 1,204 suboptimal (0.37) curves are modulated, within tolerance; PC1 changes sign at 0 ms, "
    "PC2 is 0.107 for |dt| > 30 and -0.133 for |dt| < 10; three PCs explain 0.836, above 0.825.",
    [373, 1204, 0.836]),
 oc("fig7e-pc1-best-suboptimal", "partially_reproduced",
    "Selective best PC1 -2.37, suboptimal 0.21, p = 8.9e-8. The nonselective difference is 0.59 of the selective "
    "one (p = 0.016), not under a third. PC2 differs between nonselective best and all suboptimal (p = 0.005); "
    "PC3 pairs do not differ (p >= 0.097).", deviations=[SEL2]),
 oc("fig7f-inbound-sharper", "partially_reproduced",
    "Reading (c) (constant best curves excluded) gives 134 inbound and 112 (a) or 114 (b) outbound sets, CSI 0.109 "
    "against 0.083 (p = 0.030 and 0.027) and alignment 0.319 against 0.038 or 0.033 (p = 1e-7); readings (a) and "
    "(b) give 204 inbound, CSI p = 0.11 and 0.10, alignment p = 5e-5. Both tests hold under reading (c); the group "
    "sizes are outside 121 +- 12.1 and 56 +- 5.6.", [134, 112], [SEL2]),
 oc("fig7g-inbound-decoding", "not_reproduced",
    "Mean accuracy over negative ranges minus that over the others is 0.014 (N = 187), 0.016 (N = 100), 0.014 "
    "(CW-tuned) and 0.019 (SW-tuned), each below the mean bootstrap s.d. (0.057 to 0.075); accuracies range 0.094 "
    "to 0.165.", deviations=[SEL2, "dt = +40 ms lies in none of the ten ranges the claims file gives."]),
 oc("supp8-order-decoding", "not_reproduced",
    "Order decoding at N = 100 reaches 0.581 over selective sets and 0.570 over all sets, below 0.585 (chance 0.5).",
    0.581, [SEL2]),
 oc("exp3-units-cw-tuned", "reproduced",
    "81 units, 74 responsive (sham a), 46 CW-tuned (0.62); the CW has the largest mean single-whisker response "
    "(0.845). Sham (b) gives 78 and 47; dropping epochs with spikes after 300 ms gives 75 to 76 and 46.",
    [81, 74, 46], [NOLICK]),
 oc("fig8c-awake-cw-stronger", "partially_reproduced",
    "CW response above spontaneous 0.709 (46 awake CW-tuned) against 0.414 (87 anesthetized), ratio 1.71, within "
    "2 +- 0.3; awake tuning is sharper (mean ranked SW/CW 0.375 against 0.393). The t-test gives p = 0.0021 (sham "
    "b 0.0025), not below 0.001, a case the criterion's partial rule does not name; the effect is present, at a "
    "weaker significance.", 1.71, [NOLICK, CAUDAL], True),
 oc("fig8d-awake-best-sequence", "reproduced",
    "Slope 1.234 with an intercept (1.300 through the origin); 73 of 74 units (0.986) above.", 1.234, [NOLICK]),
 oc("exp3-combination-selective", "reproduced",
    "27 of 74 responsive units selective after FDR (0.365); best sequence contains the CW for 0.704 of selective "
    "and 0.784 of all responsive units.", [0.365, 27, 0.704, 0.784], [NOLICK]),
 oc("fig8h-awake-linearity", "partially_reproduced",
    "Best 0.941 +- 0.028 (within 0.93 +- 0.03), suboptimal 0.723 +- 0.009 (outside 0.71 +- 0.009, within 10%), "
    "p = 1.5e-16.", [0.941, 0.723], [NOLICK]),
 oc("fig8i-awake-sharper-than-linear", "reproduced",
    "Measured CSI 0.057 against linear 0.023, 70 of 74 units above (0.946), paired p = 9e-9.", deviations=[NOLICK]),
 oc("fig8j-awake-inbound-stronger", "reproduced",
    "Z-scored peak responses 1.95, 0.93, 1.36 at -40, 0, +40 ms (ANOVA p = 8e-14, reading a) and 1.75, 0.10, "
    "0.64 (p = 2.6e-15, reading b).", deviations=[NOLICK]),
 oc("fig8k-awake-binary-decoder", "reproduced",
    "Over 27 selective units accuracy rises from 0.652 (a) and 0.674 (b) at N = 5 to 0.815 and 0.829 at N = 25.",
    deviations=[NOLICK, "The selective units are this attempt's 27, against the paper's 29."]),
 oc("fig8b-awake-behavior", "blocked",
    "The experiment 3 files hold spike times, deflected whiskers and DeltaT per epoch, with no lick times, trial "
    "boundaries or Go and No-go labels (data descriptor, and every field of every file listed in the data "
    "check). The paper names no other source for the behavioral data.", blocked_by="data_missing"),
]

findings = [
 {"kind": "data_missing", "statement": "The experiment 3 files hold no lick times, trial boundaries or Go and No-go "
  "labels, so the behavior of Figure 8b cannot be tested and epochs within 200 ms of a lick, which the Methods "
  "exclude, cannot be identified. They also hold no deflection times and no per-unit recording depth (only the "
  "electrode tip depth)."},
 {"kind": "metadata_insufficient", "statement": "The experiment 3 epochs have no deflection times, and the data "
  "descriptor does not say how DeltaT is signed or where epoch time 0 lies. The CW response latencies show that "
  "DeltaT is the time of the second listed whisker minus that of the first and that time 0 is the earlier "
  "deflection (the CW-driven peak is at 30 ms when the CW leads and at 70 ms when the SW leads by 40 ms)."},
 {"kind": "other", "about": "data", "statement": "About a third of the experiment 3 spike times (26 to 35% per "
  "file) lie after the roughly 300 ms stimulus epoch, up to 425 s after its start, in 5.6% of unit-epochs; the "
  "data descriptor does not mention them. The response window (0 to 125 ms) is unaffected."},
 {"kind": "metadata_insufficient", "statement": "The experiment 1 files hold each single whisker deflected in both "
  "directions (18 single-whisker stimuli), where the paper describes 9 single-whisker deflections; which "
  "direction the paper used is not stated. The caudal deflections reproduce the paper's unit counts. In both "
  "20170510 recordings the sequences that involve whisker 3 or 8 are coded with that whisker deflected "
  "rostrally (about 5,300 trials per recording), which neither the paper nor the descriptor mentions."},
 {"kind": "other", "about": "data", "statement": "Nine of the 16 experiment 2 recordings hold 16,000 to 24,000 "
  "three-whisker trials (whiskers 2, 5 and 8, or 4, 5 and 6), which neither the paper nor the data descriptor "
  "mentions."},
 {"kind": "metadata_error", "statement": "Two experiment 2 units in 20160909 (recNames chn3 and chn4, depths 250 "
  "and 150 um) have identical spike trains, a duplicated unit. In 20160803 and 20160909 some units carry the "
  "recName of another recording than the one whose trial sequence they hold."},
 {"kind": "other", "about": "data", "statement": "Two experiment 2 recordings (20160225 and 20160316, 10 units) have "
  "no sham trials, which the Methods use for responsiveness and spontaneous rates. CW-SW dt takes 101 values, "
  "-50 to +50 ms, where the paper gives 100."},
 {"kind": "methods_unavailable", "statement": "Question for the authors. The dt smoothing classifies 23% of curves "
  "as best fit unsmoothed; here the unsmoothed 1 ms curve never beats a smoothed one in held-out Poisson "
  "likelihood, and the share of curves whose likelihood rises to the largest kernel (57%) depends on how the "
  "kernel meets the +-50 ms edges (1% with zero padding). How were held-out dt values without training trials, "
  "zero rates and the edges handled?"},
 {"kind": "methods_unavailable", "statement": "Question for the authors. A unit whose best-combination dt curve is "
  "set constant across dt has no best dt, yet Figures 7a, 7b and 7f align or split units by it. Were such units "
  "left out (121 + 56 = 177 of 187 suggests so), or how was their best dt chosen? This attempt leaves them out of "
  "the alignment of Figure 7a."},
 {"kind": "methods_unavailable", "statement": "Question for the authors. Which deflection direction were the nine "
  "single-whisker stimuli of experiment 1, and how were the rostral deflections in the files used? This attempt "
  "takes the caudal ones."},
 {"kind": "methods_unavailable", "statement": "The shuffle test of combination selectivity finds 69% of response "
  "sets selective here against the paper's 41%. The Methods do not say how a curve set constant across dt is "
  "treated in the shuffles or how the Mahalanobis covariance of nearly collinear smoothed traces is inverted, and "
  "the analysis code is available only on request."},
]

rec = {
 "schema_version": 3,
 "id": "laboy-juarez-2019-01",
 "datasets": [{"archive": "crcns", "id": "ssc-9", "version": "unversioned", "doi": "10.6080/K0FJ2F13",
               "relation": "primary"}],
 "paper": "doi:10.1038/s41593-019-0448-6",
 "date": "2026-11-12",
 "entry": "laboy-juarez-2019",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
                "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-14"},
                "runner": {"platform": "GitHub Actions",
                           "url": "https://github.com/catalystneuro/encore/actions/runs/43263909874"}},
 "outcomes": outcomes,
 "findings": findings,
}
class D(yaml.SafeDumper):
    pass
out = yaml.dump(rec, Dumper=D, sort_keys=False, allow_unicode=True, width=100)
open("attempts/laboy-juarez-2019-01.yaml", "w").write(out)
print(len(outcomes), "outcomes")
PYEOF
cd $TMPDIR && . dev/bin/activate && pip list 2>/dev/null | grep -i pyyaml || uv pip install -q pyyaml; python rec/make.py && cd  && python tools/entry.py check entries/laboy-juarez-2019 2>&1 | tail -5; grep -c ": " attempts/laboy-juarez-2019-01.yaml | head -1
```

```
PyYAML                    6.0.3
50 outcomes
0 error(s)
304
```

**Agent calls Bash**

```bash
grep -n -i -E "rather|—|–" attempts/laboy-juarez-2019-01.yaml entries/laboy-juarez-2019/*.py entries/laboy-juarez-2019/*.yaml $TMPDIR/nb/results.md $TMPDIR/nb/*.py | grep -v "/run.py\|build" | head; python3 - <<'EOF'
import yaml,re
txt=open('attempts/laboy-juarez-2019-01.yaml').read()
# find plain (unquoted) scalars containing ': '
for i,l in enumerate(txt.splitlines()):
    s=l.strip()
    m=re.match(r"^(- )?[a-z_]+: (.*)$", s)
    body = m.group(2) if m else s
    if ': ' in body and not body.startswith(("'",'"')):
        print(i+1, l[:120])
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019 && cat > README.md <<'EOF'
# Laboy-Juarez, Langberg, Ahn & Feldman (2019) from CRCNS ssc-9

Tests the findings of [Laboy-Juarez et al. (2019)](https://doi.org/10.1038/s41593-019-0448-6) on
[CRCNS ssc-9](https://doi.org/10.6080/K0FJ2F13), which holds the spike times of single units in
mouse barrel cortex during single- and two-whisker stimulation in the paper's three experiments:
a survey of all two-whisker combinations in anesthetized mice (Figure 1), dense dt mapping of
CW-SW sequences in anesthetized mice (Figures 2 to 7) and a replication in awake mice (Figure 8).

| Experiment | Claims | Reproduced | Partially | Not reproduced | Blocked |
|---|---|---|---|---|---|
| 1, anesthetized survey | 10 | 8 | 2 | 0 | 0 |
| 2, dense dt mapping | 30 | 15 | 9 | 6 | 0 |
| 3, awake mice | 9 | 5 | 3 | 0 | 1 |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The unit counts of all three experiments match the paper. Single-whisker tuning, the preference
for CW-SW sequences, sublinear integration with near-linear best combinations, the inbound order
preference and the awake results mostly reproduce. The shuffle test of combination selectivity
finds more selective response sets than the paper (318 of 463, against 187 of 451), the dt
smoothing classifies curves differently, and the population decoders of combination identity
and order fall short of the paper's accuracies. The paper's analysis code is available only on
request, so these methods rest on the Methods text. The behavioral claim is blocked: the files
hold no lick times.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/laboy-juarez-2019-01.yaml`](../../attempts/laboy-juarez-2019-01.yaml).

- `reproduce_laboy_juarez_2019.ipynb`: the analysis. It takes about 13 minutes, most of it the
  dt smoothing and the 5,000 shuffles per response set of experiment 2.
- `lj2019.py`: streaming the zip from the CRCNS bucket and reducing each unit to spike counts per
  trial, with the Poisson responsiveness test, lifetime sparseness, the cross-validated dt
  smoothing, the shuffle test and the population decoders of the Methods.
EOF
cd  && python3 -c "
import yaml
r=yaml.safe_load(open('attempts/laboy-juarez-2019-01.yaml'))
import collections
ids=[o['claim'] for o in r['outcomes']]
groups={'1':ids[:10],'2':ids[10:40],'3':ids[40:]}
for g,l in groups.items():
  print(g,len(l),collections.Counter(o['outcome'] for o in r['outcomes'] if o['claim'] in l))
"
```

```
1 10 Counter({'reproduced': 8, 'partially_reproduced': 2})
2 30 Counter({'reproduced': 15, 'partially_reproduced': 9, 'not_reproduced': 6})
3 10 Counter({'reproduced': 6, 'partially_reproduced': 2, 'not_reproduced': 1, 'blocked': 1})
```

**Agent calls Bash**

```bash
python3 -c "
import yaml,collections
r=yaml.safe_load(open('attempts/laboy-juarez-2019-01.yaml'))
ids=[o['claim'] for o in r['outcomes']]
groups={'1':ids[:10],'2':ids[10:41],'3':ids[41:]}
for g,l in groups.items():
  print(g,len(l),l[0],l[-1],collections.Counter(o['outcome'] for o in r['outcomes'] if o['claim'] in l))
c=yaml.safe_load(open('claims/laboy-juarez-2019.yaml'))
print(len(c['claims']), set(x['id'] for x in c['claims'])^set(ids))
"
```

```
1 10 exp1-units supp2-sw-tuned-sharpest-cwsw Counter({'reproduced': 8, 'partially_reproduced': 2})
2 31 exp2-units supp8-order-decoding Counter({'reproduced': 15, 'partially_reproduced': 9, 'not_reproduced': 7})
3 9 exp3-units-cw-tuned fig8b-awake-behavior Counter({'reproduced': 6, 'partially_reproduced': 2, 'blocked': 1})
50 set()
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019 && python3 - <<'EOF'
s=open('README.md').read()
s=s.replace("| 2, dense dt mapping | 30 | 15 | 9 | 6 | 0 |","| 2, dense dt mapping | 31 | 15 | 9 | 7 | 0 |")
s=s.replace("| 3, awake mice | 9 | 5 | 3 | 0 | 1 |","| 3, awake mice | 9 | 6 | 2 | 0 | 1 |")
open('README.md','w').write(s)
p='/tmp/claude-1001/nb/05_header.py'; s=open(p).read()
s=s.replace("| exp2-units to supp8-order-decoding (experiment 2, 30 claims) | tested |","| exp2-units to supp8-order-decoding (experiment 2, 31 claims) | tested |")
open(p,'w').write(s)
EOF
grep -n "claims) |" /tmp/claude-1001/nb/05_header.py; cd $TMPDIR/nb && . ../dev/bin/activate && python build2.py entries/laboy-juarez-2019/reproduce_laboy_juarez_2019.ipynb
```

```
14:| exp1-units to supp2-sw-tuned-sharpest-cwsw (experiment 1, 10 claims) | tested |
15:| exp2-units to supp8-order-decoding (experiment 2, 31 claims) | tested |
16:| exp3-units-cw-tuned to fig8k-awake-binary-decoder (experiment 3, 8 claims) | tested |
170 cells; 49 claims
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python tools/entry.py all entries/laboy-juarez-2019 2>&1 | tail -4; date -u
```

```
Installed kernelspec registry-laboy-juarez-2019 in executed/laboy-juarez-2019/.venv/share/jupyter/kernels/registry-laboy-juarez-2019
0 error(s)
pass  reproduce_laboy_juarez_2019.ipynb  (786 s)
Thu Nov 12 18:43:32 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import nbformat
nb=nbformat.read('executed/laboy-juarez-2019/reproduce_laboy_juarez_2019.ipynb',4)
out=[];err=0
for c in nb.cells:
  if c.cell_type=='code':
    for o in c.get('outputs',[]):
      if o.get('name')=='stdout': out.append(o['text'])
      if o.get('output_type')=='error': err+=1
open('exec_out2.txt','w').write(''.join(out)); print('errors',err)
" && diff <(grep -v -E " s$| s,|in [0-9]+ s|[0-9]+ s\)|loaded in" exec_out.txt) <(grep -v -E " s$| s,|in [0-9]+ s|[0-9]+ s\)|loaded in" exec_out2.txt) | head; cd  && python tools/entry.py handover entries/laboy-juarez-2019 2>&1 | tail -3; ls executed/laboy-juarez-2019/handover/; git status --short | head
```

```
errors 0
223,238c223,238
< 20160225:10da10 4 s 3.654084
< 20160316:2dc362 4 s 3.654084
< 20160325:946652 11 s 3.654084
< 20160406:237ffc 21 s 3.654084
< 20160504:6b0f02 26 s 3.654084
< 20160504:a2e8d2 36 s 3.654084
< 20160506:7a1a88 38 s 3.654084
< 20160803:233bcd 44 s 3.654084
< 20160803:1a588f 56 s 3.654084
wrote executed/laboy-juarez-2019/handover
laboy-juarez-2019.yaml
lj2019.py
reproduce_laboy_juarez_2019.ipynb
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
git status --short | grep -v "^?? \.[a-z]" ; ls -la .bashrc .mcp.json 2>&1 | head -3
```

```
?? attempts/laboy-juarez-2019-01.yaml
?? entries/laboy-juarez-2019/
?? scripts
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 12 16:54 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 12 16:54 .mcp.json
```

**Agent calls Bash**

```bash
ls -la scripts | head; ls entries/laboy-juarez-2019/
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 12 16:54 scripts
README.md
__pycache__
entry.yaml
lj2019.py
reproduce_laboy_juarez_2019.ipynb
requirements.in
requirements.lock.txt
```

**Agent calls Bash**

```bash
rm -rf entries/laboy-juarez-2019/__pycache__; git check-ignore -q executed && echo "executed ignored"; python tools/entry.py check entries/laboy-juarez-2019 2>&1 | tail -1; date -u
```

```
executed ignored
0 error(s)
Thu Nov 12 18:44:01 UTC 2026
```

**Agent**

I finished the attempt and ran the handover. The notebook executes cleanly through `tools/entry.py all` in about 13 minutes (peak memory 3.7 GB), and `check` reports no errors. The handover package is in `executed/laboy-juarez-2019/handover/`. Nothing is committed.

## 1. Outcomes (50 claims)

| Claim | Outcome |
|---|---|
| exp1-units, exp1-cw-tuned-fraction | reproduced (assumed) |
| fig1b, supp1d, fig1d, fig1f, fig1g, supp2 | reproduced |
| exp1-cw-sw-comparable-firing | partially: spontaneous rates match; maximal evoked firing is 0.6–0.9 spikes per stimulus against the paper's 4.8 |
| fig1e-best-combination-includes-cw | partially (assumed): SW-tuned fraction 0.421 against a lower bound of 0.423 |
| exp2-units, fig2f-shuffle, fig2f-most-selective, fig2g, fig3a, fig3b both, fig4a, fig5a, fig5c-pseudo, fig5c-all-dt, supralinear, fig6b-best/worst, fig6b-suppression | reproduced |
| fig7a-dt-half-width | reproduced (assumed): 11.5 ms |
| supp4, supp6, fig4c, fig5bc, fig6c, fig7b, fig7c, fig7e, fig7f | partially |
| methods-dt-modulation, exp2-combination-selective-prevalence, fig3e, fig3g, fig6b-enhancement-not-different, fig7g, supp8 | not reproduced |
| exp3-units, fig8d, exp3-combination-selective, fig8i, fig8j, fig8k | reproduced |
| fig8c, fig8h | partially |
| fig8b-awake-behavior | blocked: data_missing |

The total is 29 reproduced, 13 partially, 7 not reproduced and 1 blocked. The main divergence is the shuffle test: it finds 318 of 463 response sets combination-selective, against the paper's 187 of 451. Every later claim about selective units uses this larger set.

## 2. Dataset, assumptions and questions

**What the dataset holds.** Unit counts match the paper: 160, 247 and 81 units, in 8, 16 and 6 recordings. Problems found:
- **Experiment 1:** the files hold rostral as well as caudal single-whisker deflections (18 stimuli, not 9). In both 20170510 recordings, whiskers 3 and 8 are deflected rostrally in their pairs.
- **Undocumented three-whisker trials** in 9 of the 16 experiment 2 recordings, 16,000 to 24,000 each.
- **Duplicated unit:** two units in 20160909 have identical spike trains. In 20160803 and 20160909, some units carry the recName of a different recording than the one whose trials they hold.
- **Missing sham trials** in two experiment 2 recordings (20160225, 20160316).
- **Experiment 2 dt values:** 101 of them (−50 to +50 ms), where the paper says 100.
- **Experiment 3 gaps:** no deflection times, lick times, trial types or per-unit depth. The sign convention of DeltaT is undocumented; I worked it out from CW response latencies.
- **Experiment 3 late spikes:** about a third of spike times fall after the ~300 ms epoch, up to 425 s.

**Assumptions.** These are recorded as deviations, with `assumed: true` on exp1-units, exp1-cw-tuned-fraction, fig1e, fig7a and fig8c.
- Experiment 1 single-whisker stimuli are the caudal deflections. Experiment 3, which the Methods call identical to experiment 1, used only caudal ones, and this reading gives the paper's counts.
- Response sets whose best-combination curve was set constant across dt have no best dt, so they are left out of the Fig. 7a alignment.

**Questions for the paper's authors** (`methods_unavailable` findings):
- How the dt smoothing handled edges, zero rates and held-out dt values with no training trials. The "unsmoothed" category never wins here.
- Which best dt was used for units whose curves were set constant.
- Which deflection direction experiment 1 used.
- How the selectivity shuffle handled constant curves and inverted the Mahalanobis covariance.

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. **Every reading versus combinations of readings.** The claims file has several open details that multiply (O1 to O4). I ran the main combination for every claim, the variants on each claim's own readings, and did not carry alternative selections (for example the other FDR family) into the downstream claims.
2. **Expected values the criterion leaves out.** For supp6 and fig7f, the layer and group counts are in `expected` but not in the criterion's "reproduced when" clause. I treated a missed count as partially reproduced.
3. **Partial rules that miss the case.** For fig8c and fig1e the result fits neither the criterion's full rule nor its partial rule. I used the protocol's definition of partially reproduced and explained this in the notes.
4. **Testing on a parent claim's different selection.** Dependent claims are blocked only when their parent is blocked. Here the parent ran but selected a different set of units. I tested the dependent claims anyway and noted the different set in each.
5. **Which outcomes to mark `assumed`.** A single assumption (the experiment 1 direction) touches every experiment 1 claim. I marked only the claims whose outcome changed under the alternative reading, and showed all readings in one variant table.
6. **The clock check does not fit experiment 3.** Its epochs start at the stimulus, so decoding before onset is trivially at chance. I added the CW latency shift (30 ms against 70 ms) as the check instead.

## 4. Runtime and failures

The final notebook takes 13 minutes. The session took about 1 h 50 min from the start of work.

Two problems during development were fixed before the final run:
- Peak memory reached 9.8 GB. pandas copies `DataFrame.attrs` into every derived object, and a wide concatenation of tables made it worse; the final peak is 3.7 GB.
- Python's randomized `hash()` gave recording IDs that changed between runs; I replaced it with MD5.

Nothing failed in the final run. The untracked `.bashrc`, `scripts` and similar entries in the repository root are sandbox device files that existed before this session.

## End of run

114 turns, 103 minutes, $9.86 at API prices, result: success.
