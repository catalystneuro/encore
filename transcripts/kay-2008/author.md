# kay-2008 · author · run 43548126132

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls paper entries claims attempts | head -50
```

```
<persisted-output>
Output too large (40.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4daa12bf-a666-49b4-bb85-418f15804fbb/tool-results/bz2jcdmjr.txt

Preview (first 2KB):
Sat Nov 14 02:53:16 UTC 2026
# Protocol for an attempt

Version: `pilot-15`. Record this version in the attempt's provenance.

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4daa12bf-a666-49b4-bb85-418f15804fbb/tool-results/bz2jcdmjr.txt"
}
```

```
1	Sat Nov 14 02:53:16 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-15`. Record this version in the attempt's provenance.
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
[... 739 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper; cat claims/kay-2008.yaml; cat papers/datasets/kay-2008.yaml; ls entries/fouke-2025; ls questions | head -3; ls attempts | grep kay
```

```
<persisted-output>
Output too large (42.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4daa12bf-a666-49b4-bb85-418f15804fbb/tool-results/b0qmrmic1.txt

Preview (first 2KB):
10.1038-nature06713.pdf
10.1038-nature06713.supp.pdf
10.1038-nature06713.txt
vim-1.data-description.txt
# Claims for Kay, Naselaris, Prenger & Gallant (2008), Nature 452:352-355, "Identifying natural
# images from human brain activity", doi:10.1038/nature06713, on CRCNS data set vim-1.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
# protocol as stated in docs/protocol.md (Reader), version pilot-14.
#
# Text read: the version of record with its supplement, as PyMuPDF text under paper/
# (10.1038-nature06713.txt): the Letter, its Methods, and the Supplementary Information
# (Supplementary Figures 1 to 11, Supplementary Table 1, Supplementary Discussion 1 to 3,
# Supplementary Methods 1 to 11). PDF pages were rendered only for Figure 4 and Supplementary
# Figures 4, 5 and 8, whose numbers the text garbles. The data set's description
# (paper/vim-1.data-description.txt) was read only to know what it holds; no claim comes from it.
#
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4daa12bf-a666-49b4-bb85-418f15804fbb/tool-results/b0qmrmic1.txt"
}
```

```
1	10.1038-nature06713.pdf
2	10.1038-nature06713.supp.pdf
3	10.1038-nature06713.txt
4	vim-1.data-description.txt
5	# Claims for Kay, Naselaris, Prenger & Gallant (2008), Nature 452:352-355, "Identifying natural
6	# images from human brain activity", doi:10.1038/nature06713, on CRCNS data set vim-1.
7	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
8	# protocol as stated in docs/protocol.md (Reader), version pilot-14.
9	#
10	# Text read: the version of record with its supplement, as PyMuPDF text under paper/
11	# (10.1038-nature06713.txt): the Letter, its Methods, and the Supplementary Information
12	# (Supplementary Figures 1 to 11, Supplementary Table 1, Supplementary Discussion 1 to 3,
13	# Supplementary Methods 1 to 11). PDF pages were rendered only for Figure 4 and Supplementary
14	# Figures 4, 5 and 8, whose numbers the text garbles. The data set's description
15	# (paper/vim-1.data-description.txt) was read only to know what it holds; no claim comes from it.
16	#
17	# Code: the paper links no analysis code, so none was read. It names outside code for two steps:
18	# m-sequence generation by T. Liu (stimulus design only) and Gaussian kernel density estimation by
19	# A. Ihler (http://ttic.uchicago.edu/~ihler/code/), used for the set-size extrapolation.
20	#
[... 683 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/vim-1.data-description.txt; grep -n -A60 "## CRCNS" docs/archives.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=vim-1/" | python3 -c "
import sys,re
t=sys.stdin.read()
for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',t): print(s,k)
print(re.findall(r'<IsTruncated>(.*?)</IsTruncated>',t))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
wc -l paper/10.1038-nature06713.txt; grep -n "Supplementary Methods\|^[0-9]*\. \|Response estimation\|Gabor wavelet pyramid model\|Model fitting\|Voxel selection\|noise ceiling" paper/10.1038-nature06713.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature06713.txt",
 "offset": 1195,
 "limit": 560
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature06713.txt",
 "offset": 1755,
 "limit": 180
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/fouke-2025; cat entry.yaml requirements.in README.md; head -c 3000 reproduce_fouke_2025.ipynb; python3 -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells']: print(c['cell_type'], c['metadata'].get('tags'), c['source'][:1])
"; head -60 omr.py
```

```
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
  runtime_minutes: 6
helpers:
- omr.py
related:
- id: dandi:001453/0.250518.1950
  relation: uses_data
- id: doi:10.1016/j.cub.2025.04.027
[... 210 more lines not kept]
```

**Agent**

Now I'll open the data files to survey them.

**Agent calls Bash**

```bash
cd  date -u; python3 -c "import fsspec,h5py,numpy,scipy,nibabel;print('ok')" 2>&1; which uv; uv --version; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-1/checksums.md5 | grep -v "Sub._Ses"; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-1/filelist.txt | head -20
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q kenv && . kenv/bin/activate && uv pip install -q fsspec aiohttp requests h5py numpy scipy nibabel matplotlib jupyter nbconvert ipykernel 2>&1 | tail -2; python -c "
import fsspec,h5py,time
t=time.time()
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-1/EstimatedResponses.mat',block_size=2**22).open()
h=h5py.File(f,'r')
def p(n,o):
  if isinstance(o,h5py.Dataset): print(n,o.shape,o.dtype,o.chunks,o.compression)
h.visititems(p)
print(time.time()-t)
"
```

```
dataTrnS1 (1750, 25915) float64 (1750, 4) gzip
dataTrnS2 (1750, 26329) float64 (1750, 4) gzip
dataValS1 (120, 25915) float64 (120, 68) gzip
dataValS2 (120, 26329) float64 (120, 68) gzip
roiS1 (1, 25915) float64 (1, 6478) gzip
roiS2 (1, 26329) float64 (1, 6582) gzip
voxIdxS1 (1, 25915) float64 (1, 6478) gzip
voxIdxS2 (1, 26329) float64 (1, 6582) gzip
17.607340574264526
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && python -c "
import fsspec,h5py,time,numpy as np,resource
t=time.time()
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-1/EstimatedResponses.mat',block_size=2**23,cache_type='readahead').open()
h=h5py.File(f,'r')
for s in ['S1','S2']:
  roi=h['roi'+s][0]; vi=h['voxIdx'+s][0]
  print(s,np.unique(roi,return_counts=True), vi[:5], vi.min(), vi.max(), (vi==42205).sum(), roi[vi==42205], roi[vi==42205-1],roi[vi==42205+1])
print(time.time()-t)
t=time.time()
roi=h['roiS1'][0]; sel=np.where((roi>=1)&(roi<=6))[0]
v=h['dataValS1'][:]
print(v.shape, np.nanmean(v,0)[:5], np.nanstd(v,0)[:5], np.isnan(v).sum(), time.time()-t)
t=time.time()
d=h['dataTrnS1'][:, :2000]
print(d.shape, time.time()-t, d.mean(0)[:4], d.std(0)[:4], np.isnan(d).sum())
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
"
```

```
<string>:13: RuntimeWarning: Mean of empty slice
/tmp/claude-1001/kenv/lib/python3.13/site-packages/numpy/lib/_nanfunctions_impl.py:1997: RuntimeWarning: Degrees of freedom <= 0 for slice.
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
S1 (array([0., 1., 2., 3., 4., 5., 6., 7.]), array([17127,  1331,  2208,  1973,   484,   314,  1550,   928])) [657. 715. 716. 717. 718.] 657.0 71593.0 1 [1.] [1.] [1.]
S2 (array([0., 1., 2., 3., 4., 5., 6., 7.]), array([18626,  1513,  1982,  1780,   556,   492,  1022,   358])) [280. 281. 282. 294. 295.] 280.0 72856.0 0 [] [] [0.]
0.4896087646484375
(120, 25915) [-0.05870621  0.17284777 -0.10035238 -0.16925128 -0.06993393] [0.5194983  0.41046324 0.3904334  0.35240539 0.38981922] 137484 0.3971900939941406
(1750, 2000) 0.7612249851226807 [nan nan nan nan] [nan nan nan nan] 1153040
0.224852
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && python -c "
import fsspec,h5py,time,numpy as np
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-1/'
t=time.time()
h=h5py.File(fsspec.open(B+'Stimuli.mat',block_size=2**23,cache_type='readahead').open(),'r')
for k in h: print(k,h[k].shape,h[k].dtype)
st=h['stimTrn'][:]; print(st.shape, st.min(), st.max(), st.mean(), time.time()-t)
sq=h['seqTrn'][:]; sv=h['seqVal'][:]; print(sq.shape, sv.shape, sq.max(), sv.max())
print('trn: nonzero per run', (sq>0).sum(1)[:5], 'unique per run', [len(np.unique(r[r>0])) for r in sq[:3]])
print('val unique per run', [len(np.unique(r[r>0])) for r in sv], 'nonzero', (sv>0).sum(1))
r=sv[0]; print(r[:60])
h2=h5py.File(fsspec.open(B+'Stimuli_Val_FullRes.mat',block_size=2**23).open(),'r')
for k in h2: print(k,h2[k].shape,h2[k].dtype)
v=h2[list(h2.keys())[0]][:]; print(v.min(),v.max(), time.time()-t)
m=h5py.File(fsspec.open(B+'mask.mat').open(),'r') if False else None
" 2>&1 | tail -20
```

```
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    h=h5py.File(fsspec.open(B+'Stimuli.mat',block_size=2**23,cache_type='readahead').open(),'r')
  File "/tmp/claude-1001/kenv/lib/python3.13/site-packages/h5py/_hl/files.py", line 555, in __init__
    fid = make_fid(name, mode, userblock_size, fapl, fcpl, swmr=swmr)
  File "/tmp/claude-1001/kenv/lib/python3.13/site-packages/h5py/_hl/files.py", line 232, in make_fid
    fid = h5f.open(name, flags, fapl=fapl)
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "h5py/h5f.pyx", line 106, in h5py.h5f.open
OSError: Unable to synchronously open file (file signature not found)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && python -c "
import fsspec,time,numpy as np,scipy.io as sio,io
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-1/'
t=time.time()
with fsspec.open(B+'Stimuli.mat',block_size=2**23).open() as f: b=f.read(200); print(b[:120])
with fsspec.open(B+'Stimuli.mat',block_size=2**23).open() as f: d=sio.loadmat(io.BytesIO(f.read()))
for k,v in d.items():
  if not k.startswith('__'): print(k,v.shape,v.dtype, v.min(), v.max())
print(time.time()-t)
sq=d['seqTrn']; sv=d['seqVal']
print('trn nonzero per run', (sq>0).sum(0)[:5], 'unique per run', [len(np.unique(r[r>0])) for r in sq.T[:3]])
print('val unique per run', [len(np.unique(r[r>0])) for r in sv.T], 'nonzero', (sv>0).sum(0))
print(sv[:80,0])
with fsspec.open(B+'mask.mat').open() as f: m=sio.loadmat(io.BytesIO(f.read()))
for k,v in m.items():
  if not k.startswith('__'): print(k,v.shape,v.dtype,v.min(),v.max(),v.mean())
" 2>&1 | tail -20
```

```
b'MATLAB 5.0 MAT-file, Platform: GLNXA64, Created on: Mon Oct 24 09:35:48 2011                                            '
stimTrn (1750, 128, 128) float32 -0.5355023 0.4644977
stimVal (120, 128, 128) float32 -0.5355023 0.4644977
seqTrn (672, 25) uint16 0 1750
seqVal (696, 10) uint8 0 120
1.286463975906372
trn nonzero per run [140 140 140 140 140] unique per run [70, 70, 70]
val unique per run [12, 12, 12, 12, 12, 12, 12, 12, 12, 12] nonzero [162 162 162 162 162 162 162 162 162 162]
[10  0  0  0  1  0  0  0  5  0  0  0  6  0  0  0 10  0  0  0  4  0  0  0
  2  0  0  0  3  0  0  0  6  0  0  0  1  0  0  0  0  0  0  0 11  0  0  0
  2  0  0  0  2  0  0  0  7  0  0  0  2  0  0  0 10  0  0  0 12  0  0  0
  7  0  0  0  8  0  0  0]
mask (500, 500) float64 0.0 1.0 0.7091937618853019
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && python -c "
import fsspec,time,numpy as np,scipy.io as sio,io,h5py,gzip,nibabel as nib
B='https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-1/'
for n in ['Stimuli_Trn_FullRes_15.mat','Stimuli_Val_FullRes.mat']:
  t=time.time()
  with fsspec.open(B+n,block_size=2**23).open() as f: b=f.read()
  print(n,b[:60])
  try:
    h=h5py.File(io.BytesIO(b),'r'); 
    for k in h: print(k,h[k].shape,h[k].dtype)
  except Exception as e:
    d=sio.loadmat(io.BytesIO(b)); [print(k,v.shape,v.dtype) for k,v in d.items() if not k.startswith('__')]
  print(time.time()-t)
t=time.time()
with fsspec.open(B+'Sub1_Ses1_Run1_Val.nii.gz',block_size=2**23).open() as f: b=f.read()
print('read',time.time()-t)
raw=gzip.decompress(b); print('gunzip',time.time()-t, len(raw))
img=nib.Nifti1Image.from_bytes(raw); print(img.shape,img.get_data_dtype(),img.header.get_zooms(), time.time()-t)
" 2>&1 | tail -20
```

```
Stimuli_Trn_FullRes_15.mat b'MATLAB 7.3 MAT-file, Platform: GLNXA64, Created on: Sat Apr '
stimTrn (500, 500, 70) float32
0.5064141750335693
Stimuli_Val_FullRes.mat b'MATLAB 7.3 MAT-file, Platform: GLNXA64, Created on: Sat Apr '
stimVal (500, 500, 120) float32
0.48125362396240234
read 1.6169440746307373
gunzip 2.3681163787841797 205259104
(64, 64, 18, 696) float32 (np.float32(2.0), np.float32(2.0), np.float32(2.5), np.float32(0.0)) 2.368736743927002
Shell cwd was reset to
```

**Agent calls Bash**

```bash
mkdir -p entries/kay-2008; cd $TMPDIR && . kenv/bin/activate && python -c "
import numpy as np, os; print(os.cpu_count()); import numpy; numpy.show_config()" 2>&1 | grep -i -A3 "blas\|lapack" | head -20; free -g
```

```
blas:
    detection method: pkgconfig
    found: true
    include directory: /opt/_internal/cpython-3.13.14/lib/python3.13/site-packages/scipy_openblas64/include
    lib directory: /opt/_internal/cpython-3.13.14/lib/python3.13/site-packages/scipy_openblas64/lib
    name: scipy-openblas
    openblas configuration: OpenBLAS 0.3.34.106.0  USE64BITINT DYNAMIC_ARCH NO_AFFINITY
      SkylakeX MAX_THREADS=64
    pc file directory: /project/.openblas
    version: 0.3.34.106.0
  lapack:
    detection method: pkgconfig
    found: true
    include directory: /opt/_internal/cpython-3.13.14/lib/python3.13/site-packages/scipy_openblas64/include
    lib directory: /opt/_internal/cpython-3.13.14/lib/python3.13/site-packages/scipy_openblas64/lib
    name: scipy-openblas
    openblas configuration: OpenBLAS 0.3.34.106.0  USE64BITINT DYNAMIC_ARCH NO_AFFINITY
      SkylakeX MAX_THREADS=64
    pc file directory: /project/.openblas
    version: 0.3.34.106.0
[... 4 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/kay-2008/vim1.py",
 "content": "\"\"\"Loading and the identification pipeline of Kay, Naselaris, Prenger & Gallant (2008) for CRCNS vim-1.\n\nKay et al. (2008), Nature 452:352-355, doi:10.1038/nature06713. Files are streamed from the public\nCRCNS bucket (crcnsarchive, vim-1/); nothing is written to disk.\n\nThe data set holds, per subject, the estimated (repeated-trial) responses of about 26,000 voxels to\nthe 1,750 model estimation images (`dataTrn`) and the 120 identification images (`dataVal`), z-scored\nper voxel, with ROI labels (0 other, 1 V1, 2 V2, 3 V3, 4 V3A, 5 V3B, 6 V4, 7 LatOcc), and the\nstimuli at full resolution (500 px over 20 degrees).\n\nWhere the parameters come from (claims file `claims/kay-2008.yaml`, opening comment, P1 to P6 and\nO1 to O7, which cite the Supplementary Methods; SM below):\n\n- Stimulus resolutions min(500, round(2 ** (9 - x / 8))), x = 0..24 (SM 6, \"Stimulus\n  pre-processing\"); mean luminance over all stimuli subtracted (SM 6). Stimulus values are taken as\n  linear in luminance (O4, an assumption: the goggles' response is not given).\n- Down-sampling uses area averaging (a standard choice for a detail that should not change a\n  result; SM 6 does not say how the stimuli were resampled).\n- Gabor wavelet pyramid (SM 6, \"Design of the wavelet pyramid\"): f = 1, 2, 4, 8, 16 (and 32 at\n  128 px) cycles per field of view, centres on an f x f grid at the cell centres (O3, standard\n  choice), 8 orientations, 2 quadrature phases, isotropic Gaussian masks with a spatial frequency\n  bandwidth of 1 octave (full width at half maximum), so the Gaussian SD is\n  3 * sqrt(2 ln 2) / (2 pi) = 0.562 wavelengths (O3: the SD in pixels is fixed by the bandwidth only\n  up to convention; this convention gives an orientation bandwidth of 37 degrees against the 41 the\n  paper states), masks zeroed below 0.01 of peak, truncated at the image bounds, each wavelet\n  zero-mean and unit-length within its mask; one luminance-only wavelet over the whole image whose\n  channel is sqrt(2 * p ** 2) (SM 6, \"Transformation from image to predicted response\").\n- A wavelet's projection is set to zero if more than half of its mask (by weight) lies beyond 90%\n  of the stimulus radius (SM 6). The radius is that of the circular mask in `mask.mat`.\n- Fitting (SM 6, \"Estimation of model parameters\"): 20% of the training responses drawn at random\n  as a stopping set, responses mean-subtracted, channels z-scored, kernel from zero, step 0.001,\n  normalized gradient with momentum 0.9 (both the error gradient and the sum normalized to unit\n  length, our reading of the garbled formula), stop at the first iteration where the stopping-set\n  error no longer decreases. One stopping set is drawn per fit and shared by all voxels fitted\n  together (a standard choice for a random draw). The paper's 100 bootstrap fits, whose mean gives\n  the final parameters, are not run here for time (a deviation; `n_boot` runs a smaller number).\n- Rough localization (SM 5): orientation-invariant 128 px models over the full 20 degrees, the\n  central 10.0 degrees (128 px of the 256 px image) and the central 5.12 degrees (128 px of the\n  500 px image); the paper states 10.1 and 5.2 degrees, which the resolution list does not give\n  exactly. The spatial envelope is the sum of the channel masks (each normalized to sum to 1)\n  scaled by the absolute weights (SM 6, \"Calculation of tuning curves\"); an isotropic 2-D Gaussian\n  with a constant offset (the offset is our choice; SM 5 says only \"an isotropic two-dimensional\n  Gaussian\") is fitted to it at 32 x 32. The RF is the square of +/-2 SD; for the 10 and 5 degree\n  models it is valid only if wholly within the field of view. The best initial model is the valid\n  one with the least stopping-set error.\n- Predictive power is Pearson r on the 120 identification images (SM 6); its one-tailed p-value is\n  the fraction of 1,000 bootstrap resamples of the 120 image pairs with r <= 0 (O2, standard choice).\n- Final model (SM 5): 64 px, not orientation invariant (2,729 channels and a DC offset). Its field\n  of view is O5 reading (a), the square of +/-2 SD of the fitted Gaussian, taken from the\n  resolution of the list at which that square is closest to 64 px, or (b), the best initial\n  model's field of view at 64 px.\n- Identification (main text; SM 7): for each measured pattern, the 500 voxels with highest\n  predictive power over the other 119 images, then the image whose predicted pattern has the\n  highest Pearson r with the measured pattern.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\n\nimport fsspec\nimport h5py\nimport numpy as np\nimport scipy.io as sio\nfrom scipy import sparse\nfrom scipy.optimize import least_squares\n\nBASE = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-1/\"\nROI_NAMES = {0: \"other\", 1: \"V1\", 2: \"V2\", 3: \"V3\", 4: \"V3A\", 5: \"V3B\", 6: \"V4\", 7: \"LatOcc\"}\nSTIM_DEG = 20.0\nFULL_PX = 500\nRESOLUTIONS = [min(500, round(2 ** (9 - x / 8))) for x in range(25)]\nSTEP, MOMENTUM, STOP_FRACTION = 0.001, 0.9, 0.2\nN_VOXELS_ID = 500\n\n\ndef _open(name, block=2**23):\n    return fsspec.open(BASE + name, block_size=block, cache_type=\"readahead\").open()\n\n\n# ---------------------------------------------------------------------------------------------\n# Loading\n\n\ndef load_responses(subject, rois=(1, 2, 3, 6)):\n    \"\"\"Estimated responses of one subject ('S1' or 'S2') for the voxels in `rois`.\n\n    Returns a dict with trn (1750 x V), val (120 x V), roi, vox_idx (the data set's index into the\n    64 x 64 x 18 volume), and the counts per ROI over all voxels and of voxels dropped for NaNs.\n    \"\"\"\n    with _open(\"EstimatedResponses.mat\") as f, h5py.File(f, \"r\") as h:\n        roi = h[\"roi\" + subject][0].astype(int)\n        vox = h[\"voxIdx\" + subject][0].astype(int)\n        counts_all = {ROI_NAMES[k]: int((roi == k).sum()) for k in range(8)}\n        cols = np.where(np.isin(roi, rois))[0]\n        trn = h[\"dataTrn\" + subject][:, :][:, cols].astype(np.float32)\n        val = h[\"dataVal\" + subject][:, :][:, cols].astype(np.float32)\n        n_total = roi.size\n    bad = np.isnan(trn).any(0) | np.isnan(val).any(0)\n    out = dict(trn=trn[:, ~bad], val=val[:, ~bad], roi=roi[cols][~bad], vox_idx=vox[cols][~bad],\n               counts_all=counts_all, n_total=n_total,\n               dropped_nan={ROI_NAMES[k]: int((bad & (roi[cols] == k)).sum()) for k in rois})\n    return out\n\n\ndef load_stimuli():\n    \"\"\"Full-resolution stimuli (1870 x 500 x 500 float32: 1,750 training then 120 validation),\n    the 128 px stimuli of Stimuli.mat, the presentation sequences, and the circular mask.\"\"\"\n    full = np.empty((1870, FULL_PX, FULL_PX), np.float32)\n    i = 0\n    for k in range(1, 16):\n        with _open(f\"Stimuli_Trn_FullRes_{k:02d}.mat\") as f, h5py.File(f, \"r\") as h:\n            a = h[\"stimTrn\"][:]          # stored (500, 500, n): MATLAB n x 500 x 500\n            a = np.transpose(a, (2, 1, 0))\n            full[i:i + a.shape[0]] = a\n            i += a.shape[0]\n    with _open(\"Stimuli_Val_FullRes.mat\") as f, h5py.File(f, \"r\") as h:\n        full[i:] = np.transpose(h[\"stimVal\"][:], (2, 1, 0))\n    with _open(\"Stimuli.mat\") as f:\n        s = sio.loadmat(io.BytesIO(f.read()))\n    with _open(\"mask.mat\") as f:\n        m = sio.loadmat(io.BytesIO(f.read()))[\"mask\"]\n    small = np.concatenate([s[\"stimTrn\"], s[\"stimVal\"]]).astype(np.float32)\n    return dict(full=full, small=small, seq_trn=s[\"seqTrn\"], seq_val=s[\"seqVal\"], mask=m)\n\n\n# ---------------------------------------------------------------------------------------------\n# Resampling\n\n\ndef area_matrix(n_in, n_out):\n    \"\"\"n_out x n_in matrix that resamples by area averaging (overlap of output and input pixels).\"\"\"\n    edges_out = np.linspace(0, n_in, n_out + 1)\n    A = np.zeros((n_out, n_in))\n    for o in range(n_out):\n        a, b = edges_out[o], edges_out[o + 1]\n        for j in range(int(np.floor(a)), int(np.ceil(b))):\n            A[o, j] = min(b, j + 1) - max(a, j)\n    return (A / A.sum(1, keepdims=True)).astype(np.float32)\n\n\ndef resize_stack(imgs, n_out):\n    if imgs.shape[1] == n_out:\n        return imgs\n    A = area_matrix(imgs.shape[1], n_out)\n    return np.einsum(\"oi,nij,pj->nop\", A, imgs, A, optimize=True)\n\n\ndef crop(imgs, cy, cx, size, fill):\n    \"\"\"Square crop of side `size` px centred at (cy, cx) px (floats), padded with `fill`.\"\"\"\n    n = imgs.shape[1]\n    y0 = int(round(cy - size / 2)); x0 = int(round(cx - size / 2))\n    out = np.full((imgs.shape[0], size, size), fill, np.float32)\n    ys, xs = max(0, y0), max(0, x0)\n    ye, xe = min(n, y0 + size), min(n, x0 + size)\n    if ye > ys and xe > xs:\n        out[:, ys - y0:ye - y0, xs - x0:xe - x0] = imgs[:, ys:ye, xs:xe]\n    return out\n\n\n# ---------------------------------------------------------------------------------------------\n# Gabor wavelet pyramid\n\nSD_PER_WAVELENGTH = 3 * np.sqrt(2 * np.log(2)) / (2 * np.pi)\n\n\ndef gwp(npx, n_levels):\n    \"\"\"Wavelet pyramid at `npx` px with `n_levels` spatial frequencies (1, 2, 4, ... cycles/FOV).\n\n    Returns a sparse (npx*npx x n_wavelets) matrix with the wavelets in the order\n    level, grid row, grid column, orientation, phase; and a table of the channels (one per\n    quadrature pair, then the luminance channel last) with level, cycles per FOV, row and column\n    centre in px, orientation index, and the normalized mask of each channel (sparse, sums to 1).\n    \"\"\"\n    yy, xx = np.mgrid[0:npx, 0:npx].astype(np.float64) + 0.5\n    rows, cols, vals = [], [], []\n    mrows, mcols, mvals = [], [], []\n    chan = []\n    w = 0\n    for lev in range(n_levels):\n        f = 2 ** lev\n        lam = npx / f\n        sd = SD_PER_WAVELENGTH * lam\n        for gy in range(f):\n            for gx in range(f):\n                cy = (gy + 0.5) * npx / f\n                cx = (gx + 0.5) * npx / f\n                g = np.exp(-((yy - cy) ** 2 + (xx - cx) ** 2) / (2 * sd ** 2))\n                support = g >= 0.01\n                idx = np.flatnonzero(support)\n                gm = g.ravel()[idx]\n                for o in range(8):\n                    th = np.pi * o / 8\n                    u = (xx.ravel()[idx] - cx) * np.cos(th) + (yy.ravel()[idx] - cy) * np.sin(th)\n                    c = len(chan)\n                    for ph in (0, np.pi / 2):\n                        wv = gm * np.cos(2 * np.pi * u / lam + ph)\n                        wv = wv - wv.mean()\n                        wv = wv / np.linalg.norm(wv)\n                        rows.append(idx); cols.append(np.full(idx.size, w)); vals.append(wv)\n                        w += 1\n                    mrows.append(np.full(idx.size, c)); mcols.append(idx); mvals.append(gm / gm.sum())\n                    chan.append((lev, f, cy, cx, o))\n    # luminance-only wavelet\n    idx = np.arange(npx * npx)\n    rows.append(idx); cols.append(np.full(idx.size, w)); vals.append(np.full(idx.size, 1 / npx))\n    mrows.append(np.full(idx.size, len(chan))); mcols.append(idx); mvals.append(np.full(idx.size, 1 / npx ** 2))\n    chan.append((-1, 0, npx / 2, npx / 2, -1))\n    W = sparse.csc_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),\n                          shape=(npx * npx, w + 1), dtype=np.float32)\n    M = sparse.csr_matrix((np.concatenate(mvals), (np.concatenate(mrows), np.concatenate(mcols))),\n                          shape=(len(chan), npx * npx), dtype=np.float32)\n    table = np.array(chan, dtype=float)\n    return W, table, M\n\n\ndef edge_keep(table, M, npx, fov_deg, center_deg, radius_deg):\n    \"\"\"True for channels whose mask lies at most half beyond 90% of the stimulus radius (SM 6).\n\n    The FOV of `fov_deg` spans `npx` px and is centred at `center_deg` (x, y) from the stimulus centre.\n    \"\"\"\n    yy, xx = np.mgrid[0:npx, 0:npx].astype(np.float64) + 0.5\n    deg_per_px = fov_deg / npx\n    ry = (yy - npx / 2) * deg_per_px + center_deg[1]\n    rx = (xx - npx / 2) * deg_per_px + center_deg[0]\n    outside = (np.hypot(rx, ry) > 0.9 * radius_deg).ravel().astype(np.float32)\n    frac_out = M @ outside\n    keep = frac_out <= 0.5\n    keep[-1] = True                                   # luminance wavelet: always kept\n    return keep\n\n\ndef gwp_channels(imgs, W, table, keep, orientation_invariant):\n    \"\"\"Contrast-energy channels of `imgs` (n x npx x npx). Returns n x channels (float32).\"\"\"\n    n = imgs.shape[0]\n    P = (sparse.csr_matrix(W.T) @ imgs.reshape(n, -1).T).T  # n x wavelets\n    P = np.asarray(P, dtype=np.float32)\n    nq = (P.shape[1] - 1) // 2\n    E = np.sqrt(P[:, 0:2 * nq:2] ** 2 + P[:, 1:2 * nq:2] ** 2)\n    lum = np.sqrt(2 * P[:, -1:] ** 2)\n    E = E * keep[:-1][None, :]\n    if orientation_invariant:\n        E = E.reshape(n, -1, 8).sum(2)\n    return np.concatenate([E, lum], 1)\n\n\ndef orientation_invariant_table(table, M):\n    \"\"\"Channel table and masks after summing over orientation (one channel per position).\"\"\"\n    t = table[:-1].reshape(-1, 8, 5)[:, 0]\n    Mi = M[:-1][::8]\n    return np.concatenate([t, table[-1:]]), sparse.vstack([Mi, M[-1:]]).tocsr()\n\n\n# ---------------------------------------------------------------------------------------------\n# Gradient descent with early stopping\n\n\ndef fit_gd(X, Y, stop_idx, max_iter=5000, n_iter=None):\n    \"\"\"Gradient descent with early stopping (SM 6), vectorized over voxels (columns of Y).\n\n    X: n x q channels, Y: n x V responses, stop_idx: indices of the stopping set. Returns the\n    kernel in channel units (q x V), the DC offset (V), the stopping-set squared error at the\n    chosen iteration (V) and the iteration count (V). With `n_iter` (array, one per voxel) the\n    fit runs that many iterations instead of early stopping (used for bootstraps).\n    \"\"\"\n    n = X.shape[0]\n    fit = np.setdiff1d(np.arange(n), stop_idx)\n    Xf, Xs = X[fit], X[stop_idx]\n    xm, xs = Xf.mean(0), Xf.std(0)\n    xs[xs == 0] = 1\n    Xf = (Xf - xm) / xs\n    Xs = (Xs - xm) / xs\n    ym = Y[fit].mean(0)\n    Yf = Y[fit] - ym\n    Ys = Y[stop_idx] - ym\n    G = (Xf.T @ Xf).astype(np.float32)\n    C = (Xf.T @ Yf).astype(np.float32)\n    q, V = C.shape\n    h = np.zeros((q, V), np.float32)\n    g = np.zeros((q, V), np.float32)\n    best_h = h.copy()\n    err = (Ys ** 2).sum(0)\n    iters = np.zeros(V, int)\n    active = np.ones(V, bool) if n_iter is None else n_iter > 0\n    it = 0\n    while active.any() and it < max_iter:\n        a = np.flatnonzero(active)\n        grad = G @ h[:, a] - C[:, a]\n        grad /= np.maximum(np.linalg.norm(grad, axis=0), 1e-12)\n        gn = grad + MOMENTUM * g[:, a]\n        gn /= np.maximum(np.linalg.norm(gn, axis=0), 1e-12)\n        g[:, a] = gn\n        h[:, a] -= STEP * gn\n        it += 1\n        if n_iter is None:\n            e = ((Xs @ h[:, a] - Ys[:, a]) ** 2).sum(0)\n            better = e < err[a]\n            err[a[better]] = e[better]\n            iters[a[better]] = it\n            best_h[:, a[better]] = h[:, a[better]]\n            active[a[~better]] = False\n        else:\n            best_h[:, a] = h[:, a]\n            iters[a] = it\n            active[a[n_iter[a] <= it]] = False\n    k = best_h / xs[:, None]\n    dc = ym - xm @ k\n    return k, dc, err, iters\n\n\ndef fit_boot(X, Y, rng, n_boot=0):\n    \"\"\"Fit on the original responses with early stopping; then, with `n_boot` > 0, the paper's\n    bootstrap: resample the responses, draw a new stopping set, run the same iteration count,\n    and average the parameters (SM 6, \"Estimation of variance\").\"\"\"\n    n = X.shape[0]\n    stop = rng.choice(n, int(round(STOP_FRACTION * n)), replace=False)\n    k, dc, err, iters = fit_gd(X, Y, stop)\n    if n_boot == 0:\n        return k, dc, err, iters\n    ks, dcs = np.zeros_like(k), np.zeros_like(dc)\n    for _ in range(n_boot):\n        b = rng.integers(0, n, n)\n        sb = rng.choice(n, int(round(STOP_FRACTION * n)), replace=False)\n        kb, dcb, _, _ = fit_gd(X[b], Y[b], sb, n_iter=iters)\n        ks += kb; dcs += dcb\n    return ks / n_boot, dcs / n_boot, err, iters\n\n\n# ---------------------------------------------------------------------------------------------\n# Predictive power, significance, identification\n\n\ndef pearson_cols(a, b):\n    a = a - a.mean(0); b = b - b.mean(0)\n    return (a * b).sum(0) / np.sqrt((a ** 2).sum(0) * (b ** 2).sum(0))\n\n\ndef boot_p(meas, pred, rng, n_boot=1000):\n    \"\"\"One-tailed bootstrap p-value of r > 0 over images (O2): fraction of resamples with r <= 0.\"\"\"\n    n = meas.shape[0]\n    cnt = np.zeros(meas.shape[1])\n    for _ in range(n_boot):\n        b = rng.integers(0, n, n)\n        cnt += np.nan_to_num(pearson_cols(meas[b], pred[b]), nan=0) <= 0\n    return cnt / n_boot\n\n\ndef loo_power(meas, pred):\n    \"\"\"Predictive power of each voxel with each image left out: 120 x V matrix of Pearson r.\"\"\"\n    n = meas.shape[0]\n    out = np.empty(meas.shape, np.float64)\n    for j in range(n):\n        keep = np.arange(n) != j\n        out[j] = pearson_cols(meas[keep], pred[keep])\n    return out\n\n\ndef identify(meas, pred, power_loo, n_vox=N_VOXELS_ID, cand=None):\n    \"\"\"P5. meas: patterns to identify (n_meas x V), with the index of the image each shows given\n    by the row order of `power_loo`'s images via `which` below; pred: predicted patterns of the\n    candidate images (n_img x V). Returns the chosen image per measured pattern.\"\"\"\n    raise NotImplementedError\n\n\ndef identify_repeated(meas, pred, power_loo, n_vox=N_VOXELS_ID, cand=None):\n    \"\"\"Repeated-trial identification: meas and pred are 120 x V; voxel selection for pattern j\n    uses power_loo[j]. `cand` restricts the candidate voxels (boolean mask over V).\"\"\"\n    n = meas.shape[0]\n    choice = np.empty(n, int)\n    selected = []\n    for j in range(n):\n        pw = np.where(cand, power_loo[j], -np.inf) if cand is not None else power_loo[j]\n        pw = np.nan_to_num(pw, nan=-np.inf)\n        sel = np.argsort(-pw)[:n_vox]\n        selected.append(sel)\n        m = meas[j, sel]; m = m - m.mean()\n        p = pred[:, sel]; p = p - p.mean(1, keepdims=True)\n        r = p @ m / np.sqrt((p ** 2).sum(1) * (m ** 2).sum())\n        choice[j] = np.argmax(r)\n    return choice, selected\n\n\n# ---------------------------------------------------------------------------------------------\n# Gaussian fit to the spatial envelope\n\n\ndef fit_gaussian(env):\n    \"\"\"Isotropic 2-D Gaussian with offset fitted to an envelope (k x k). Returns (y0, x0, sd) in px\n    of the k x k grid (pixel centres at i + 0.5).\"\"\"\n    k = env.shape[0]\n    yy, xx = np.mgrid[0:k, 0:k] + 0.5\n    e = env / env.max() if env.max() > 0 else env\n    iy, ix = np.unravel_index(np.argmax(e), e.shape)\n\n    def res(p):\n        a, y0, x0, s, b = p\n        return (a * np.exp(-((yy - y0) ** 2 + (xx - x0) ** 2) / (2 * s ** 2)) + b - e).ravel()\n\n    p0 = [1 - np.median(e), iy + 0.5, ix + 0.5, k / 8, np.median(e)]\n    r = least_squares(res, p0, bounds=([0, -k, -k, 0.25, -1], [10, 2 * k, 2 * k, 4 * k, 1]),\n                      max_nfev=200)\n    return r.x[1], r.x[2], abs(r.x[3])\n\n\ndef envelopes(k, M, size, block):\n    \"\"\"Spatial envelopes (V x size/block x size/block) from kernels k (q x V) and masks M (q x px).\"\"\"\n    E = (M.T @ np.abs(k)).T  # V x px\n    V = E.shape[0]\n    E = E.reshape(V, size // block, block, size // block, block).mean((2, 4))\n    return E\n"
}
```

```
File created successfully at: entries/kay-2008/vim1.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && cat > t1.py <<'EOF'
import sys, time, resource, numpy as np
sys.path.insert(0, 'entries/kay-2008')
import vim1
t=time.time()
S=vim1.load_stimuli(); print('load', time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
full=S['full']; small=S['small']
r128=vim1.resize_stack(full[:50],128)
print('corr full->128 vs small', np.corrcoef(r128.ravel(), small[:50].ravel())[0,1], 'transposed', np.corrcoef(r128.transpose(0,2,1).ravel(), small[:50].ravel())[0,1])
print('corner values', full[:5,0,0], full[:5,250,250], 'mask corner', S['mask'][0,0], S['mask'][250,250])
m=S['mask']; print('mask radius px', np.sqrt(m.sum()/np.pi), 'unique', np.unique(m)[:5], len(np.unique(m)))
print('mean all', full.mean())
np.save('full_mean.npy', np.array(full.mean()))
t=time.time()
W,table,M=vim1.gwp(128,6); print('gwp', W.shape, W.nnz, time.time()-t)
EOF
python t1.py
```

```
load 17.846381187438965 2.429264
corr full->128 vs small 0.998100575495717 transposed 0.23216937100585133
corner values [0. 0. 0. 0. 0.] [ 0.4644977  -0.5278886  -0.20479202 -0.04354173 -0.21301386] mask corner 0.0 1.0
mask radius px 237.5623000540936 unique [0.00000000e+00 1.93449650e-07 1.42527852e-06 3.79434165e-06
 4.83677553e-06] 5414
mean all -0.07361545
gwp (16384, 21841) 9436160 0.6659367084503174
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && cat > t2.py <<'EOF'
import sys, time, resource, numpy as np
sys.path.insert(0, 'entries/kay-2008')
import vim1
t=time.time()
S=vim1.load_stimuli(); full=S['full']; mu=full.mean(); full-=mu
print('load', time.time()-t)
W,table,M=vim1.gwp(128,6)
ti,Mi=vim1.orientation_invariant_table(table,M)
R=np.sqrt(S['mask'].sum()/np.pi)/500*20
feats={}
for name,res,fov in [('20',128,20.0),('10',256,20*128/256),('5',500,20*128/500)]:
    t=time.time()
    imgs=vim1.resize_stack(full,res)
    imgs=vim1.crop(imgs,res/2,res/2,128,-mu)
    keep=vim1.edge_keep(table,M,128,fov,(0,0),R)
    X=vim1.gwp_channels(imgs,W,table,keep,True)
    feats[name]=X
    print(name, X.shape, keep.mean(), time.time()-t, X[:, :3].std(0), resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
np.savez('feats_init.npz', **feats)
EOF
python t2.py
```

```
load 16.22440457344055
20 (1870, 1366) 0.5722003479534841 4.887120485305786 [26.587343 13.340879 13.414587] 4.857276
10 (1870, 1366) 1.0 5.913886547088623 [32.092384 15.504697 15.61313 ] 5.446048
5 (1870, 1366) 1.0 3.9500067234039307 [33.833572 15.97824  15.989484] 5.446048
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && cat > t3.py <<'EOF'
import sys, time, resource, numpy as np
sys.path.insert(0, 'entries/kay-2008')
import vim1
t=time.time()
D=vim1.load_responses('S1'); print('resp', time.time()-t, D['trn'].shape, D['dropped_nan'], D['counts_all'])
print('trn mean/std', D['trn'].mean(0)[:3], D['trn'].std(0)[:3], 'val', D['val'].mean(0)[:3], D['val'].std(0)[:3])
F=np.load('feats_init.npz')
Y=D['trn']; V=Y.shape[1]
rng=np.random.default_rng(0)
for name in ['20']:
    X=F[name][:1750]
    t=time.time()
    k,dc,err,it=vim1.fit_boot(X,Y[:, :2000],rng)
    print(name,'fit',time.time()-t, 'iters pct', np.percentile(it,[5,25,50,75,95,100]))
    pred=F[name][1750:]@k+dc
    r=vim1.pearson_cols(D['val'][:, :2000],pred)
    for roi in [1,2,3,6]:
        s=D['roi'][:2000]==roi; print(roi, s.sum(), np.nanmedian(r[s]) if s.any() else None, (r[s]>0.25).mean() if s.any() else None)
EOF
python t3.py
```

```
entries/kay-2008/vim1.py:335: RuntimeWarning: invalid value encountered in divide
  return (a * b).sum(0) / np.sqrt((a ** 2).sum(0) * (b ** 2).sum(0))
resp 8.330372333526611 (1750, 6702) {'V1': 37, 'V2': 125, 'V3': 183, 'V4': 15} {'other': 17127, 'V1': 1331, 'V2': 2208, 'V3': 1973, 'V3A': 484, 'V3B': 314, 'V4': 1550, 'LatOcc': 928}
trn mean/std [ 0.000000e+00 -2.179827e-09  0.000000e+00] [0.9985704 0.9985704 0.9985704] val [-0.38574755 -0.11447372  0.11738954] [0.4713981  0.25530773 0.3607955 ]
20 fit 1.6979973316192627 iters pct [  0.   0.   9.  51. 131. 264.]
1 239 0.08880023 0.35564853556485354
2 544 0.10613158 0.3602941176470588
3 578 0.014608014 0.19377162629757785
6 639 0.011696566 0.14241001564945227
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && cat > t4.py <<'EOF'
import sys, time, resource, numpy as np
sys.path.insert(0, 'entries/kay-2008')
import vim1
D=vim1.load_responses('S1')
F=np.load('feats_init.npz')
W,table,M=vim1.gwp(128,6)
ti,Mi=vim1.orientation_invariant_table(table,M)
Y=D['trn']
rng=np.random.default_rng(0)
X=F['20'][:1750]
k,dc,err,it=vim1.fit_boot(X,Y[:, :300],rng)
t=time.time()
E=vim1.envelopes(k,Mi,128,4)
print('env', time.time()-t, E.shape)
t=time.time()
g=[vim1.fit_gaussian(e) for e in E]
print('gauss', time.time()-t)
g=np.array(g); print(g[:10])
EOF
python t4.py
```

```
env 0.021456241607666016 (300, 32, 32)
gauss 1.4404809474945068
[[ 10.61127057  11.2503347    3.98826605]
 [-12.89894025 -12.89894017   3.14407464]
 [ 21.15943579  25.08660979   2.37870937]
 [ 15.22722484  15.25077456  20.08757062]
 [ 16.05149244  15.47713294  17.43810798]
 [-12.89894025 -12.89894017   3.14407464]
 [ 14.47280223  15.0684045   22.95958421]
 [-12.89894025 -12.89894017   3.14407464]
 [  6.59463055  12.62970593   1.42880639]
 [ 16.13942816  15.43596215  20.31714772]]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/kay-2008 && python3 - <<'EOF'
p='vim1.py'
s=open(p).read()
start=s.index('def identify(meas, pred, power_loo')
end=s.index('def identify_repeated')
s=s[:start]+s[end:]
s=s.replace('''    G = (Xf.T @ Xf).astype(np.float32)
    C = (Xf.T @ Yf).astype(np.float32)
    q, V = C.shape''','''    use_gram = Y.shape[1] > 50          # few voxels: the gradient from the samples is cheaper
    C = (Xf.T @ Yf).astype(np.float32)
    G = (Xf.T @ Xf).astype(np.float32) if use_gram else None
    q, V = C.shape''')
s=s.replace('''        grad = G @ h[:, a] - C[:, a]''','''        grad = (G @ h[:, a] if use_gram else Xf.T @ (Xf @ h[:, a])) - C[:, a]''')
s=s.replace('''    Xf = (Xf - xm) / xs
    Xs = (Xs - xm) / xs''','''    Xf = ((Xf - xm) / xs).astype(np.float32)
    Xs = ((Xs - xm) / xs).astype(np.float32)''')
open(p,'w').write(s)
EOF
cat >> vim1.py <<'EOF'


# ---------------------------------------------------------------------------------------------
# The pipeline for one subject

FOVS = {"20": (128, STIM_DEG), "10": (256, STIM_DEG * 128 / 256), "5": (500, STIM_DEG * 128 / 500)}
FINAL_B = {"20": (64, STIM_DEG), "10": (128, STIM_DEG * 64 / 128), "5": (250, STIM_DEG * 64 / 250)}


def stimulus_radius_deg(mask):
    """Radius of the circular stimulus mask, from its area (degrees)."""
    return float(np.sqrt(mask.sum() / np.pi) / mask.shape[0] * STIM_DEG)


def fov_images(full, fill, res, npx):
    """Stimuli resampled to `res` px over 20 degrees, central `npx` px."""
    return crop(resize_stack(full, res), res / 2, res / 2, npx, fill)


def initial_channels(full, fill, radius):
    """Orientation-invariant 128 px channels for the three initial fields of view (SM 5)."""
    W, table, M = gwp(128, 6)
    ti, Mi = orientation_invariant_table(table, M)
    out = {}
    for name, (res, fov) in FOVS.items():
        keep = edge_keep(table, M, 128, fov, (0, 0), radius)
        out[name] = gwp_channels(fov_images(full, fill, res, 128), W, table, keep, True)
    return out, Mi


def final_b_channels(full, fill, radius):
    """64 px channels, not orientation invariant, over the three initial fields of view (O5 b)."""
    W, table, M = gwp(64, 5)
    out = {}
    for name, (res, fov) in FINAL_B.items():
        keep = edge_keep(table, M, 64, fov, (0, 0), radius)
        out[name] = gwp_channels(fov_images(full, fill, res, 64), W, table, keep, False)
    return out, (W, table, M)


def initial_models(D, chans, Mi, rng, n_boot_p=1000):
    """Fit the three initial models to every voxel of D, fit Gaussians to their envelopes, choose
    the best initial model (SM 5), and give its predictive power and bootstrap p-value (SM 6)."""
    Y, Yv = D["trn"], D["val"]
    V = Y.shape[1]
    stop = rng.choice(Y.shape[0], int(round(STOP_FRACTION * Y.shape[0])), replace=False)
    res = {}
    for name in FOVS:
        X = chans[name]
        k, dc, err, iters = fit_gd(X[:1750], Y, stop)
        pred = X[1750:] @ k + dc
        r = np.nan_to_num(pearson_cols(Yv, pred), nan=0.0)
        fov = FOVS[name][1]
        E = envelopes(k, Mi, 128, 4)
        gs = np.full((V, 3), np.nan)
        for v in np.flatnonzero(iters > 0):
            gs[v] = fit_gaussian(E[v])
        cx = (gs[:, 1] / 32 - 0.5) * fov
        cy = -(gs[:, 0] / 32 - 0.5) * fov
        sd = gs[:, 2] / 32 * fov
        inside = (np.abs(cx) + 2 * sd <= fov / 2) & (np.abs(cy) + 2 * sd <= fov / 2)
        valid = (iters > 0) & (inside if name != "20" else True)
        res[name] = dict(k=k, dc=dc, err=err, iters=iters, r=r, pred=pred, cx=cx, cy=cy, sd=sd,
                         valid=valid)
    names = list(FOVS)
    errs = np.stack([np.where(res[n]["valid"], res[n]["err"], np.inf) for n in names])
    best = np.argmin(errs, 0)
    has = np.isfinite(errs.min(0))
    pick = lambda key: np.stack([res[n][key] for n in names])[best, np.arange(V)]
    best_r = np.where(has, pick("r"), 0.0)
    best_pred = np.stack([res[n]["pred"] for n in names])[best, :, np.arange(V)].T
    p = boot_p(Yv, best_pred, rng, n_boot_p)
    p[~has] = 1.0
    return dict(models=res, best=np.array(names)[best], has=has, r=best_r, p=p, pred=best_pred,
                cx=pick("cx"), cy=pick("cy"), sd=pick("sd"))


def final_b(D, init, chans_b, rng, voxels, n_boot=0):
    """Final 64 px models over the best initial model's field of view (O5 b) for `voxels`."""
    V = D["trn"].shape[1]
    pred = np.zeros((120, V), np.float32)
    kern = {}
    for name in FINAL_B:
        vs = np.flatnonzero(voxels & (init["best"] == name))
        if vs.size == 0:
            continue
        X = chans_b[name]
        k, dc, err, iters = fit_boot(X[:1750], D["trn"][:, vs], rng, n_boot)
        pred[:, vs] = X[1750:] @ k + dc
        for j, v in enumerate(vs):
            kern[v] = (name, k[:, j], dc[j])
    return pred, kern


def final_a_plan(init, voxels):
    """Field of view of the final model under O5 (a): the +/-2 SD square, at the resolution of the
    list where that square is closest to 64 px (in log size). Returns resolution and the centre
    (row, column) in px of that resolution, per voxel."""
    side = 4 * init["sd"]
    want = 64 * STIM_DEG / np.maximum(side, 1e-6)
    resl = np.array(RESOLUTIONS)
    pick = np.abs(np.log(resl[None, :]) - np.log(want[:, None])).argmin(1)
    res = resl[pick]
    col = res / 2 + init["cx"] * res / STIM_DEG
    row = res / 2 - init["cy"] * res / STIM_DEG
    return np.where(voxels, res, 0), row, col


def final_a(D, init, full, fill, radius, rng, voxels, W64, log=None):
    """Final 64 px models over the +/-2 SD square of each voxel (O5 a), one voxel at a time."""
    W, table, M = W64
    V = D["trn"].shape[1]
    res, row, col = final_a_plan(init, voxels)
    pred = np.zeros((120, V), np.float32)
    kern = {}
    stop = rng.choice(1750, int(round(STOP_FRACTION * 1750)), replace=False)
    for r in sorted(set(res[voxels])):
        stack = resize_stack(full, int(r))
        fov = 64 * STIM_DEG / r
        for v in np.flatnonzero(voxels & (res == r)):
            imgs = crop(stack, row[v], col[v], 64, fill)
            centre = ((col[v] - r / 2) * STIM_DEG / r, (r / 2 - row[v]) * STIM_DEG / r)
            keep = edge_keep(table, M, 64, fov, centre, radius)
            X = gwp_channels(imgs, W, table, keep, False)
            k, dc, err, iters = fit_gd(X[:1750], D["trn"][:, [v]], stop)
            pred[:, v] = X[1750:] @ k[:, 0] + dc[0]
            kern[v] = (int(r), k[:, 0], dc[0], centre, fov)
        del stack
        if log is not None:
            log(r)
    return pred, kern
EOF
python3 -c "import ast;ast.parse(open('vim1.py').read())"
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && cat > t5.py <<'EOF'
import sys, time, resource, numpy as np
sys.path.insert(0, 'entries/kay-2008')
import vim1
T=time.time()
S=vim1.load_stimuli(); full=S['full']; mu=float(full.mean()); full-=mu; fill=-mu
R=vim1.stimulus_radius_deg(S['mask'])
D=vim1.load_responses('S1')
t=time.time(); ch,Mi=vim1.initial_channels(full,fill,R); print('init chans',time.time()-t)
t=time.time(); chb,W64=vim1.final_b_channels(full,fill,R); print('final b chans',time.time()-t)
rng=np.random.default_rng(1)
t=time.time(); init=vim1.initial_models(D,ch,Mi,rng); print('initial models',time.time()-t)
roi=D['roi']; v13=np.isin(roi,[1,2,3])
for a in [1,2,3,6]:
    s=roi==a; print(a, s.sum(), (init['p'][s]<0.01).sum(), 'frac of all', (init['p'][s]<0.01).sum()/D['counts_all'][vim1.ROI_NAMES[a]], np.median(init['r'][s]))
print('best', {n:(init['best'][init['has']]==n).sum() for n in vim1.FOVS})
candA=v13 & (init['p']<0.01); candB=v13 & init['has']
print('cand', candA.sum(), candB.sum())
t=time.time(); predb,kb=vim1.final_b(D,init,chb,rng,candB); print('final b',time.time()-t)
Yv=D['val']
for nm,cand in [('O1a',candA),('O1b',candB)]:
    pl=vim1.loo_power(Yv,predb)
    ch_,sel=vim1.identify_repeated(Yv,predb,pl,cand=cand)
    print('O5b',nm,'correct',(ch_==np.arange(120)).sum())
    pl2=vim1.loo_power(Yv,init['pred'])
    ch2,_=vim1.identify_repeated(Yv,init['pred'],pl2,cand=cand)
    print('initial-best',nm,'correct',(ch2==np.arange(120)).sum())
sub=candA & (np.cumsum(candA)<=40)
t=time.time(); preda,ka=vim1.final_a(D,init,full,fill,R,rng,sub,W64); print('final a 40 vox',time.time()-t)
ra=vim1.pearson_cols(Yv[:,sub],preda[:,sub]); rb=vim1.pearson_cols(Yv[:,sub],predb[:,sub]); print('r a vs b', np.nanmedian(ra), np.nanmedian(rb))
print('total',time.time()-T, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
python t5.py 2>&1 | grep -v Warn
```

```
return (a * b).sum(0) / np.sqrt((a ** 2).sum(0) * (b ** 2).sum(0))
init chans 11.337483167648315
final b chans 4.357396841049194
initial models 75.4543137550354
1 1294 548 frac of all 0.41172051089406464 0.13480268
2 2083 667 frac of all 0.3020833333333333 0.069176465
3 1790 359 frac of all 0.1819564115560061 0.025243904
6 1535 271 frac of all 0.17483870967741935 0.01857288
best {'20': np.int64(3306), '10': np.int64(950), '5': np.int64(1032)}
cand 1574 4135
final b 11.632712841033936
O5b O1a correct 91
initial-best O1a correct 96
O5b O1b correct 91
initial-best O1b correct 96
final a 40 vox 29.346049785614014
r a vs b 0.34399775 0.33156443
total 160.87910509109497 6.016932
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . kenv/bin/activate && cat > t6.py <<'EOF'
import sys, time, resource, numpy as np
sys.path.insert(0, 'entries/kay-2008')
import vim1
S=vim1.load_stimuli(); full=S['full']; mu=float(full.mean()); full-=mu; fill=-mu
R=vim1.stimulus_radius_deg(S['mask'])
D=vim1.load_responses('S1')
ch,Mi=vim1.initial_channels(full,fill,R)
chb,W64=vim1.final_b_channels(full,fill,R)
del full
rng=np.random.default_rng(1)
init=vim1.initial_models(D,ch,Mi,rng,n_boot_p=200)
roi=D['roi']; v13=np.isin(roi,[1,2,3])
candA=v13 & (init['p']<0.01)
Yv=D['val']
for nb in [0,10,30]:
    t=time.time(); predb,kb=vim1.final_b(D,init,chb,np.random.default_rng(2),candA,n_boot=nb)
    pl=vim1.loo_power(Yv,predb)
    c,_=vim1.identify_repeated(Yv,predb,pl,cand=candA)
    print(nb,'time',time.time()-t,'correct',(c==np.arange(120)).sum(), 'median r', np.median(vim1.pearson_cols(Yv[:,candA],predb[:,candA])))
EOF
python t6.py 2>&1 | grep -v Warn
```

```
Sat Nov 14 03:03:59 UTC 2026
  return (a * b).sum(0) / np.sqrt((a ** 2).sum(0) * (b ** 2).sum(0))
0 time 7.904927968978882 correct 93 median r nan
10 time 75.18179702758789 correct 95 median r nan
30 time 207.80288577079773 correct 94 median r nan
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  sed -n 940,1000p paper/10.1038-nature06713.txt; grep -n "Discussion 1" paper/10.1038-nature06713.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1037,1110p paper/10.1038-nature06713.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,30p tools/entry.py; grep -n "def cmd_\|tags\|sanity\|claim:" tools/entry.py | head -40; cat entries/fouke-2025/entry.yaml | head -3; ls executed 2>/dev/null | head -3
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
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 200,260p tools/entry.py; sed -n 370,400p tools/entry.py
```

```
if not requirements.is_file():
        report.error(rel, "no requirements.in")
    elif not lock.is_file():
        report.error(rel, "no requirements.lock.txt; run `tools/entry.py lock`")
    else:
        locked_for = LOCK_VERSION.search(lock.read_text()[:2000])
        if entry.get("python") and locked_for and locked_for.group(1) != str(entry["python"]):
            report.error(rel / "requirements.lock.txt", f"locked for Python {locked_for.group(1)}, but entry.yaml "
                         f"says {entry['python']}; run `tools/entry.py lock`")
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
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/build.py <<'EOF'
import sys, nbformat
src = open(sys.argv[1]).read()
cells = []
for block in src.split("\n##CELL ")[1:]:
    head, _, body = block.partition("\n")
    parts = head.split()
    kind = parts[0]
    tags = [t for p in parts[1:] if p.startswith("tags=") for t in p[5:].split(",")]
    body = body.rstrip("\n")
    c = nbformat.v4.new_markdown_cell(body) if kind == "md" else nbformat.v4.new_code_cell(body)
    if tags:
        c.metadata["tags"] = tags
    cells.append(c)
nb = nbformat.v4.new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbformat.write(nb, sys.argv[2])
print(len(cells), "cells")
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/kay-2008 && python3 - <<'EOF'
p='vim1.py'
s=open(p).read()
s=s.replace('''BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-1/"''','''DATASET = "vim-1"            # CRCNS data set, doi:10.6080/K0QN64NG
VERSION = "unversioned"      # CRCNS data sets are not versioned (docs/archives.md); MD5s in the notebook
BASE = f"https://crcnsarchive.s3-us-west-2.amazonaws.com/{DATASET}/"''')
open(p,'w').write(s)
EOF
grep -n "^DATASET\|^VERSION\|^BASE" vim1.py
```

```
68:DATASET = "vim-1"            # CRCNS data set, doi:10.6080/K0QN64NG
69:VERSION = "unversioned"      # CRCNS data sets are not versioned (docs/archives.md); MD5s in the notebook
70:BASE = f"https://crcnsarchive.s3-us-west-2.amazonaws.com/{DATASET}/"
```

**Agent calls Bash**

```bash
cd  grep -B3 -A15 '"vim-1"' targets/crcns.json | head -40
```

```
"catalystneuro": []
  },
  {
   "id": "vim-1",
   "name": "fMRI of human visual areas in response to natural images",
   "url": "http://crcns.org/data-sets/vc/vim-1",
   "doi": "10.6080/K0QN64NG",
   "published_version": null,
   "asset_count": 93,
   "size_gb": 12.18,
   "data_standards": [
    "MATLAB",
    "compressed archives"
   ],
   "species": [
    "Human"
   ],
   "approaches": [
    "functional magnetic resonance imaging"
```

**Agent calls Bash**

```bash
cd entries/kay-2008 && cat >> vim1.py <<'EOF'


# ---------------------------------------------------------------------------------------------
# Retinotopy-only model (SM 8)


def ro_channels(full, init, voxels, weighted=True, chunk=256):
    """The two RO channels for `voxels` at the original 500 px resolution (SM 8): the absolute
    spatially-weighted luminance and the spatially-weighted contrast (square root of the weighted
    variance), with the weights of the Gaussian G of the best initial model; with
    `weighted=False`, the standard metrics (mean and SD) over the +/-2 SD square of G.
    Returns two 1870 x V arrays (zero for voxels not in `voxels`)."""
    n = full.shape[0]
    flat = full.reshape(n, -1)
    sq = flat ** 2
    yy, xx = np.mgrid[0:FULL_PX, 0:FULL_PX] + 0.5
    px = FULL_PX / STIM_DEG
    vs = np.flatnonzero(voxels)
    L = np.zeros((n, voxels.size), np.float32)
    Cn = np.zeros((n, voxels.size), np.float32)
    for i in range(0, vs.size, chunk):
        v = vs[i:i + chunk]
        cx = FULL_PX / 2 + init["cx"][v] * px
        cy = FULL_PX / 2 - init["cy"][v] * px
        sd = init["sd"][v] * px
        if weighted:
            w = np.exp(-((yy.ravel()[:, None] - cy) ** 2 + (xx.ravel()[:, None] - cx) ** 2) / (2 * sd ** 2))
        else:
            w = ((np.abs(yy.ravel()[:, None] - cy) <= 2 * sd) & (np.abs(xx.ravel()[:, None] - cx) <= 2 * sd))
        w = w.astype(np.float32)
        tot = np.maximum(w.sum(0), 1e-12)
        m1 = (flat @ w) / tot
        m2 = (sq @ w) / tot
        L[:, v] = np.abs(m1)
        Cn[:, v] = np.sqrt(np.maximum(m2 - m1 ** 2, 0))
    return L, Cn


def fit_ro(D, L, C, rng, voxels):
    """Fit the RO model (gradient descent of SM 6) to `voxels`; predictions for the 120 images."""
    V = D["trn"].shape[1]
    pred = np.zeros((120, V), np.float32)
    stop = rng.choice(1750, int(round(STOP_FRACTION * 1750)), replace=False)
    for v in np.flatnonzero(voxels):
        X = np.stack([L[:, v], C[:, v]], 1)
        k, dc, err, iters = fit_gd(X[:1750], D["trn"][:, [v]], stop)
        pred[:, v] = X[1750:] @ k[:, 0] + dc[0]
    return pred


# ---------------------------------------------------------------------------------------------
# Tuning curves and envelopes of final models (SM 6, "Calculation of tuning curves")


def gratings(npx=64, n_phase=16, amplitude=0.5):
    """Sinusoidal gratings at the 8 orientations and 5 spatial frequencies (1 to 16 cycles per
    FOV) of the 64 px pyramid, at `n_phase` phases: array (8, 5, n_phase, npx, npx). The
    amplitude is a standard choice (the stimulus values span about +/-0.5); with the energy model
    it scales the curves but does not change their shape."""
    yy, xx = np.mgrid[0:npx, 0:npx] + 0.5
    out = np.empty((8, 5, n_phase, npx, npx), np.float32)
    for o in range(8):
        th = np.pi * o / 8
        u = xx * np.cos(th) + yy * np.sin(th)
        for s in range(5):
            f = 2 ** s
            for p in range(n_phase):
                out[o, s, p] = amplitude * np.cos(2 * np.pi * f * u / npx + 2 * np.pi * p / n_phase)
    return out


def tuning(kern_list, keep_list, W64, grat):
    """Orientation (8) and spatial frequency (5) tuning curves of final models: the model's
    response to each grating, averaged over phase, then over SF (orientation curve) or orientation
    (SF curve). `kern_list` holds (kernel, dc); `keep_list` the edge masks used for each."""
    W, table, M = W64
    n = grat.shape[0] * grat.shape[1] * grat.shape[2]
    imgs = grat.reshape(n, 64, 64)
    ori, sf = [], []
    for (k, dc), keep in zip(kern_list, keep_list):
        X = gwp_channels(imgs, W, table, keep, False)
        r = (X @ k + dc).reshape(grat.shape[:3]).mean(2)
        ori.append(r.mean(1)); sf.append(r.mean(0))
    return np.array(ori), np.array(sf)


def final_envelope(k, M):
    """Spatial envelope of a final model (64 x 64), masks normalized to sum to 1 (SM 6)."""
    return (M.T @ np.abs(k)).reshape(64, 64)


# ---------------------------------------------------------------------------------------------
# Image similarity (Supplementary Discussion 1)


def local_contrast(full_raw, block_px, relative=False):
    """RMS contrast in square blocks of `block_px` px (0.6 degrees is 15 px at 500 px): the SD of
    the values in each block, or with `relative` that SD over the block mean (values shifted to
    start at 0, as the absolute luminance is not given)."""
    n = full_raw.shape[0]
    nb = FULL_PX // block_px
    a = full_raw[:, :nb * block_px, :nb * block_px].reshape(n, nb, block_px, nb, block_px)
    sd = a.std((2, 4))
    if relative:
        sd = sd / np.maximum(a.mean((2, 4)), 1e-6)
    return sd.reshape(n, -1)


def corr_rows(a, b):
    a = a - a.mean(1, keepdims=True); b = b - b.mean(1, keepdims=True)
    a /= np.linalg.norm(a, axis=1, keepdims=True); b /= np.linalg.norm(b, axis=1, keepdims=True)
    return a @ b.T
EOF
python3 -c "import ast;ast.parse(open('vim1.py').read())"; date -u
```

```
Sat Nov 14 03:12:35 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='vim1.py'
s=open(p).read()
s=s.replace('''    W, table, M = gwp(64, 5)
    out = {}
    for name, (res, fov) in FINAL_B.items():
        keep = edge_keep(table, M, 64, fov, (0, 0), radius)
        out[name] = gwp_channels(fov_images(full, fill, res, 64), W, table, keep, False)
    return out, (W, table, M)''','''    W, table, M = gwp(64, 5)
    out, keeps = {}, {}
    for name, (res, fov) in FINAL_B.items():
        keeps[name] = edge_keep(table, M, 64, fov, (0, 0), radius)
        out[name] = gwp_channels(fov_images(full, fill, res, 64), W, table, keeps[name], False)
    return out, keeps, (W, table, M)''')
s=s.replace('''            kern[v] = (int(r), k[:, 0], dc[0], centre, fov)''','''            kern[v] = (int(r), k[:, 0], dc[0], centre, fov, keep)''')
open(p,'w').write(s)
EOF
echo
```

```
(Bash completed with no output)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_src.txt",
 "content": "\n##CELL md\n# Reproducing Kay et al. (2008) from CRCNS vim-1\n\n**Paper.** Kay KN, Naselaris T, Prenger RJ, Gallant JL (2008). Identifying natural images from human\nbrain activity. *Nature* 452:352-355. [doi:10.1038/nature06713](https://doi.org/10.1038/nature06713).\nThe claims file `claims/kay-2008.yaml` was written from the version of record with its\nSupplementary Information (Supplementary Figures 1 to 11, Supplementary Table 1, Supplementary\nDiscussion 1 to 3, Supplementary Methods 1 to 11; SM below).\n\n**Data set.** CRCNS [vim-1](http://crcns.org/data-sets/vc/vim-1), doi:10.6080/K0QN64NG, read\nanonymously from the public bucket `crcnsarchive` (`vim-1/`, no `live/` folder). CRCNS data sets are\nnot versioned, so the version is recorded as `unversioned` (docs/archives.md); the paper cites no\nversion, and the bucket holds a single copy, the one documented by the data set's readme version\n1.2 of 2013-04-09. The MD5 sums of the files read, from the data set's `checksums.md5`, are:\n\n| File | MD5 |\n|---|---|\n| EstimatedResponses.mat | 7b702b34d42ba612118d6ad99e86e217 |\n| Stimuli.mat | 464676501cb768b005f93a32c70e73c2 |\n| Stimuli_Trn_FullRes_01.mat to _15.mat | listed in the data check below |\n| Stimuli_Val_FullRes.mat | 2e7d70ecff050d8c74b066b35e5bc00c |\n| mask.mat | 19e624419b35eaed38534047665c526c |\n| Sub1_Ses1_Run1_Val.nii.gz (timing estimate only) | listed in the data check below |\n\n**What the data set holds.** For each of the two subjects, the repeated-trial responses\n(estimated per image, z-scored per voxel) of about 26,000 voxels to the 1,750 model estimation\nimages and the 120 identification images, ROI labels, the stimuli at 128 px and at full\nresolution, the presentation sequences, the circular stimulus mask, anatomy, and the raw time series\nof the five sessions (70 runs). It does not hold the later sessions of S1, the 999-image library\nof the set-size analyses, the retinotopic mapping scans, single-trial responses, or the standard\nerrors of the response estimates.\n\n**Method.** The identification pipeline of the claims file (P1 to P5) is in `vim1.py`, whose\ndocstring says where each parameter comes from. Two departures apply to every tested claim: the\npaper's 100 bootstrap fits per model are replaced by one fit (10 bootstrap fits are shown as a\nvariant), and one stopping set is drawn per fit and shared by the voxels fitted together.\n\n| Claim | Data | Status |\n|---|---|---|\n| fig3-s1-repeated-120 | dataset | tested |\n| fig4a-s2-repeated-120 | dataset | tested |\n| fig4a-single-trial | dataset | blocked: too large for the time left (estimate below) |\n| fig4a-noise-ceiling | dataset | blocked: depends on fig4a-single-trial |\n| fig4b-set-size-1000 | with inputs | blocked: the 999-image library is not public |\n| fig4b-extrapolation | with inputs | blocked: needs the library |\n| fig4c-retinotopy-only-extrapolation | with inputs | blocked: needs the library |\n| suppm8-retinotopy-only-120 | dataset | tested |\n| suppfig8-constrained-models | with inputs | blocked: needs the library |\n| time-two-months | dataset | blocked: sessions not in the data set |\n| time-fourteen-months | dataset | blocked: session not in the data set |\n| errors-similar-images | dataset | tested |\n| suppfig4-500-voxels | dataset | blocked: depends on fig4a-single-trial (repeated trials shown) |\n| supptable1-voxel-counts | dataset | tested |\n| supptable1-predictive-power-by-area | dataset | tested |\n| supptable1-snr | dataset | blocked: too large for the time left |\n| methods-v4-poor | dataset | tested |\n| fig2-representative-voxel | dataset | tested |\n| suppfig7-roi-tuning | dataset | tested |\n| suppfig10-retinotopy-validation | dataset | blocked: mapping data not in the data set |\n| suppfig11-rf-size-eccentricity | dataset | tested |\n| suppdisc1-classification-extension | dataset | tested |\n| suppm7-selected-voxels-v1 | dataset | tested |\n\n##CELL code\nimport os\nfor var in (\"OMP_NUM_THREADS\", \"OPENBLAS_NUM_THREADS\", \"MKL_NUM_THREADS\"):\n    os.environ.setdefault(var, \"4\")\nimport io, gzip, time, resource\nimport numpy as np\nimport fsspec\nimport matplotlib.pyplot as plt\nfrom scipy import stats\nimport vim1\n\nSTARTED = time.time()\ndef peak_gb():\n    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6\nprint(\"data set\", vim1.DATASET, \"version\", vim1.VERSION)\n\n##CELL md\n## Data check\n\nThe MD5 sums are read from the data set's `checksums.md5` for every file this notebook reads.\n\n##CELL code tags=sanity\nwith fsspec.open(vim1.BASE + \"checksums.md5\", \"rt\") as f:\n    md5 = dict(reversed(line.split()) for line in f if line.strip())\nread = ([\"EstimatedResponses.mat\", \"Stimuli.mat\", \"mask.mat\", \"Stimuli_Val_FullRes.mat\",\n         \"Sub1_Ses1_Run1_Val.nii.gz\"] + [f\"Stimuli_Trn_FullRes_{k:02d}.mat\" for k in range(1, 16)])\nfor name in read:\n    print(f\"{name:30s} {md5[name]}\")\n\n##CELL code tags=sanity\nt = time.time()\nS = vim1.load_stimuli()\nfull = S[\"full\"]\nraw_min, raw_max = float(full.min()), float(full.max())\nMU = float(full.mean())\nfull -= MU                       # mean luminance over all stimuli subtracted (SM 6)\nFILL = -MU                       # the grey background (0 in the files) after that subtraction\nRADIUS = vim1.stimulus_radius_deg(S[\"mask\"])\nprint(f\"stimuli loaded in {time.time() - t:.0f} s; full resolution {full.shape}, values {raw_min:.3f} to {raw_max:.3f}, \"\n      f\"mean {MU:.4f}; 128 px {S['small'].shape}\")\nprint(\"corner pixel of every full-resolution image is 0 (grey background):\", bool((full[:, 0, 0] == FILL).all()))\nr128 = vim1.resize_stack(full[:200] + MU, 128)\nprint(\"full resolution resampled to 128 px against Stimuli.mat, r =\",\n      round(float(np.corrcoef(r128.ravel(), S[\"small\"][:200].ravel())[0, 1]), 4),\n      \"(transposed:\", round(float(np.corrcoef(r128.transpose(0, 2, 1).ravel(), S[\"small\"][:200].ravel())[0, 1]), 3), \")\")\nr128v = vim1.resize_stack(full[1750:] + MU, 128)\nprint(\"validation images, same comparison, r =\", round(float(np.corrcoef(r128v.ravel(), S[\"small\"][1750:].ravel())[0, 1]), 4))\ndel r128, r128v\nm = S[\"mask\"]\nprint(f\"mask {m.shape}, values {m.min()} to {m.max()}; radius from its area {RADIUS:.2f} deg of 20 \"\n      f\"(stimulus diameter {2 * RADIUS:.1f} deg)\")\nseq_trn, seq_val = S[\"seq_trn\"], S[\"seq_val\"]\nprint(\"training runs:\", seq_trn.shape[1], \"of\", seq_trn.shape[0], \"s; image onsets per run\",\n      sorted(set((seq_trn > 0).sum(0))), \"; distinct images per run\", sorted({len(np.unique(c[c > 0])) for c in seq_trn.T}),\n      \"; presentations per image\", sorted(set(np.bincount(seq_trn[seq_trn > 0])[1:])),\n      \"; onsets 4 s apart:\", bool(all((np.flatnonzero(c)[:, None] % 4 == np.flatnonzero(c)[0] % 4).all() for c in seq_trn.T)))\nprint(\"identification runs:\", seq_val.shape[1], \"of\", seq_val.shape[0], \"s; image onsets per run\",\n      sorted(set((seq_val > 0).sum(0))), \"; distinct images per run\", sorted({len(np.unique(c[c > 0])) for c in seq_val.T}),\n      \"; presentations per image over all runs\", sorted(set(np.bincount(seq_val[seq_val > 0])[1:])))\nfirst6 = [(seq_val[:24:4, j] == seq_val[-24::4, j]).all() for j in range(10)]\nprint(\"first 6 trials repeated at the end of each identification run:\", first6)\nprint(\"images per session (identification): \", [len(np.unique(seq_val[:, 2 * s:2 * s + 2][seq_val[:, 2 * s:2 * s + 2] > 0])) for s in range(5)])\nprint(\"training images over all runs:\", len(np.unique(seq_trn[seq_trn > 0])))\n\n##CELL code tags=sanity\nDATA = {}\nfor subj in (\"S1\", \"S2\"):\n    D = vim1.load_responses(subj)\n    DATA[subj] = D\n    print(subj, \"voxels in the file:\", D[\"n_total\"], \"; per ROI:\", D[\"counts_all\"])\n    print(\"   kept V1, V2, V3, V4 (no NaN):\", {vim1.ROI_NAMES[k]: int((D['roi'] == k).sum()) for k in (1, 2, 3, 6)},\n          \"; dropped for NaN:\", D[\"dropped_nan\"])\n    tr, va = D[\"trn\"], D[\"val\"]\n    print(f\"   training responses {tr.shape}: per-voxel mean {np.abs(tr.mean(0)).max():.2e} (max abs), \"\n          f\"SD {tr.std(0).min():.3f} to {tr.std(0).max():.3f}, range {tr.min():.1f} to {tr.max():.1f}\")\n    print(f\"   identification responses {va.shape}: per-voxel mean {va.mean(0).min():.2f} to {va.mean(0).max():.2f}, \"\n          f\"SD {va.std(0).min():.2f} to {va.std(0).max():.2f}\")\n    print(f\"   voxel index range {D['vox_idx'].min()} to {D['vox_idx'].max()} (64 x 64 x 18 = {64 * 64 * 18})\")\nd1 = DATA[\"S1\"]\nw = np.flatnonzero(d1[\"vox_idx\"] == 42205)\nprint(\"S1 voxel index 42205:\", \"present, ROI\", [vim1.ROI_NAMES[d1['roi'][i]] for i in w] if w.size else \"absent\")\nprint(f\"peak memory {peak_gb():.1f} GB\")\n\n##CELL md\nThe training responses are z-scored per voxel, as the readme says (mean 0, SD 1 to rounding). The\nidentification responses are not z-scored on their own; their means and SDs vary by voxel, which\nfits the paper's statement that the training responses' mean and SD were applied to them (SM 3).\nThe readme says the `.mat` files are MATLAB 7.3; `Stimuli.mat` and `mask.mat` are MATLAB 5 files\n(the full-resolution files are 7.3), and it gives `Stimuli_Trn_FullRes_15.mat` as 70 x 120 x 120,\nwhich is 70 x 500 x 500. The stimulus sequences and voxel counts are checked against the paper in\nthe output above. Whether the responses and stimuli share their image order is checked below by\npredicting the identification responses with the images in their order and in shuffled orders.\n\n## The identification pipeline\n\nPer subject: the three orientation-invariant initial models for every V1, V2, V3 and V4 voxel; the\nbest initial model and its predictive power and bootstrap p-value; final models under O5 (b) for\nevery V1 to V3 voxel with a best initial model, and under O5 (a) for the V1 to V3 voxels whose best\ninitial model has p < 0.01 (O1 a). The combination O1 (b) with O5 (a) is not run: it needs a\nseparate model for each of about 4,000 voxels per subject, and at the rate printed below it would\nadd about 50 minutes.\n\n##CELL code\nt = time.time()\nchans_init, M_init = vim1.initial_channels(full, FILL, RADIUS)\nchans_b, keeps_b, W64 = vim1.final_b_channels(full, FILL, RADIUS)\nprint(f\"channels in {time.time() - t:.0f} s:\", {k: v.shape for k, v in chans_init.items()}, \"initial;\",\n      {k: v.shape for k, v in chans_b.items()}, \"final (O5 b)\")\nfor name, (res, fov) in vim1.FOVS.items():\n    keep = vim1.edge_keep(*vim1.gwp(128, 6)[1:], 128, fov, (0, 0), RADIUS) if False else None\nprint(\"fields of view of the initial models (deg):\", {k: round(v[1], 2) for k, v in vim1.FOVS.items()})\n\n\ndef run_subject(subj, seed):\n    rng = np.random.default_rng(seed)\n    D = DATA[subj]\n    out = dict(D=D)\n    t = time.time()\n    init = vim1.initial_models(D, chans_init, M_init, rng)\n    out[\"init\"] = init\n    out[\"t_init\"] = time.time() - t\n    v13 = np.isin(D[\"roi\"], [1, 2, 3])\n    out[\"candA\"] = v13 & (init[\"p\"] < 0.01)\n    out[\"candB\"] = v13 & init[\"has\"]\n    t = time.time()\n    out[\"pred_b\"], out[\"kern_b\"] = vim1.final_b(D, init, chans_b, rng, out[\"candB\"])\n    out[\"t_b\"] = time.time() - t\n    t = time.time()\n    out[\"pred_a\"], out[\"kern_a\"] = vim1.final_a(D, init, full, FILL, RADIUS, rng, out[\"candA\"], W64)\n    out[\"t_a\"] = time.time() - t\n    return out\n\n\nRES = {}\nfor subj, seed in ((\"S1\", 1), (\"S2\", 2)):\n    RES[subj] = R = run_subject(subj, seed)\n    init = R[\"init\"]\n    print(f\"{subj}: initial models {R['t_init']:.0f} s, final (b) {R['t_b']:.0f} s for {R['candB'].sum()} voxels, \"\n          f\"final (a) {R['t_a']:.0f} s for {R['candA'].sum()} voxels ({R['t_a'] / max(R['candA'].sum(), 1):.2f} s each); \"\n          f\"peak memory {peak_gb():.1f} GB\")\n    for name in vim1.FOVS:\n        mm = init[\"models\"][name]\n        print(f\"   initial {name:>2s} deg: fits that stopped at iteration 0 (no kernel) {int((mm['iters'] == 0).sum())} of \"\n              f\"{mm['iters'].size}; iterations median {np.median(mm['iters']):.0f}, max {mm['iters'].max()}; valid RF {int(mm['valid'].sum())}\")\n    print(\"   best initial model:\", {n: int((init['best'][init['has']] == n).sum()) for n in vim1.FOVS},\n          \"; voxels with none:\", int((~init['has']).sum()))\n\n##CELL md\n### Do the responses and the stimuli share their order?\n\nThe best initial model's predictions are correlated with the identification responses in the\nimages' order, and in 20 random permutations of the image order.\n\n##CELL code tags=sanity\nrng_check = np.random.default_rng(7)\nfor subj in (\"S1\", \"S2\"):\n    R = RES[subj]; D = R[\"D\"]; v1 = (D[\"roi\"] == 1) & R[\"init\"][\"has\"]\n    true_r = np.median(vim1.pearson_cols(D[\"val\"][:, v1], R[\"init\"][\"pred\"][:, v1]))\n    perm = [np.median(vim1.pearson_cols(D[\"val\"][rng_check.permutation(120)][:, v1], R[\"init\"][\"pred\"][:, v1]))\n            for _ in range(20)]\n    print(f\"{subj}: median r over {v1.sum()} V1 voxels, image order {true_r:.3f}; permuted orders {min(perm):.3f} to {max(perm):.3f}\")\n\n##CELL md\nResponses and stimuli line up in the order the readme gives: the shuffled orders give median\ncorrelations near zero.\n\n## fig3-s1-repeated-120 and fig4a-s2-repeated-120\n\n> For subject S1, the image seen was identified correctly for 92% (110 of 120) of the\n> repeated-trial voxel activity patterns from 120 novel natural images, against chance of 0.8%.\n> For subject S2, 72% (86 of 120) of the images were identified correctly from repeated-trial\n> patterns.\n\nCriterion: P1 to P5; the values must hold under one of the readings of O1 (candidate voxels:\n(a) V1 to V3 voxels whose best initial model has p < 0.01, (b) all V1 to V3 voxels) and O5 (final\nmodel field of view: (a) the +/-2 SD square, (b) the best initial model's field of view). Expected\n92 +/- 9.2 (S1) and 72 +/- 7.2 (S2) percent correct.\n\n##CELL code tags=claim:fig3-s1-repeated-120,claim:fig4a-s2-repeated-120\nREADINGS = {\"O1a-O5a\": (\"pred_a\", \"candA\"), \"O1a-O5b\": (\"pred_b\", \"candA\"), \"O1b-O5b\": (\"pred_b\", \"candB\")}\nID = {}\nfor subj in (\"S1\", \"S2\"):\n    R = RES[subj]; D = R[\"D\"]\n    for name, (pk, ck) in READINGS.items():\n        pred = R[pk]\n        power = vim1.loo_power(D[\"val\"], pred)\n        choice, sel = vim1.identify_repeated(D[\"val\"], pred, power, cand=R[ck])\n        ID[subj, name] = dict(choice=choice, sel=sel, power=power, pred=pred, cand=R[ck])\n        n_ok = int((choice == np.arange(120)).sum())\n        print(f\"{subj} {name}: {n_ok}/120 = {100 * n_ok / 120:.1f}% correct (candidate voxels {R[ck].sum()}; \"\n              f\"binomial p against chance 1/120 = {stats.binomtest(n_ok, 120, 1 / 120, alternative='greater').pvalue:.1e})\")\n    # the best initial model alone, for reference\n    power = vim1.loo_power(D[\"val\"], R[\"init\"][\"pred\"])\n    choice, _ = vim1.identify_repeated(D[\"val\"], R[\"init\"][\"pred\"], power, cand=R[\"candA\"])\n    print(f\"{subj} best initial models only (O1 a): {(choice == np.arange(120)).sum()}/120\")\nprint(\"O1 b with O5 a: not run (time, see above).\")\n\n##CELL md\nVariant: the paper's bootstrap averaging (SM 6, \"Estimation of variance\"), with 10 bootstrap fits\nin place of 100, for the final models under O5 (b) on the O1 (a) voxels.\n\n##CELL code tags=claim:fig3-s1-repeated-120,claim:fig4a-s2-repeated-120\nfor subj, seed in ((\"S1\", 11), (\"S2\", 12)):\n    R = RES[subj]; D = R[\"D\"]\n    t = time.time()\n    pred_boot, _ = vim1.final_b(D, R[\"init\"], chans_b, np.random.default_rng(seed), R[\"candA\"], n_boot=10)\n    power = vim1.loo_power(D[\"val\"], pred_boot)\n    choice, _ = vim1.identify_repeated(D[\"val\"], pred_boot, power, cand=R[\"candA\"])\n    n_ok = int((choice == np.arange(120)).sum())\n    print(f\"{subj} O1a-O5b with 10 bootstrap fits: {n_ok}/120 = {100 * n_ok / 120:.1f}% ({time.time() - t:.0f} s)\")\n\n##CELL code tags=claim:fig3-s1-repeated-120,claim:fig4a-s2-repeated-120\nfig, axes = plt.subplots(1, 2, figsize=(9, 4))\nfor ax, subj in zip(axes, (\"S1\", \"S2\")):\n    I = ID[subj, \"O1a-O5a\"]; D = RES[subj][\"D\"]; sel = I[\"sel\"]\n    rmat = np.array([[np.corrcoef(D[\"val\"][j, sel[j]], I[\"pred\"][i, sel[j]])[0, 1] for i in range(120)] for j in range(120)])\n    ax.imshow(rmat, cmap=\"viridis\"); ax.set_xlabel(\"predicted pattern (image)\"); ax.set_ylabel(\"measured pattern (image)\")\n    ax.set_title(f\"{subj}, O1a-O5a: r from {rmat.min():.2f} to {rmat.max():.2f}\")\nplt.tight_layout(); plt.show()\n\n##CELL md\n**Result: not reproduced.** The values are printed above for each reading; the criterion asks\nfor 82.8% or more for S1 and 64.8% to 79.2% for S2 under one reading.\n\n##CELL md\n## Single-trial claims: what it would take\n\nfig4a-single-trial, fig4a-noise-ceiling (which depends on it) and supptable1-snr need responses the\ndata set does not hold: single-trial amplitudes, or the standard errors of the repeated-trial\namplitudes. Both come from fitting the BRS model (SM 3 and 4) to the time series of every voxel:\nper session, a repeated-trial fit with a Fourier basis to get each voxel's HRF, then a fit with one\namplitude per trial (1,024 trials and 28 polynomial terms on 4,752 time points per session) with\nfirst-order autoregressive noise, iterated to convergence. Each voxel has its own HRF and noise\nmodel, so each needs its own least-squares fits. The cell below streams one run and times one\nsingle-trial least-squares solve of that size.\n\n##CELL code\nt = time.time()\nwith fsspec.open(vim1.BASE + \"Sub1_Ses1_Run1_Val.nii.gz\", block_size=2**23).open() as f:\n    raw_bytes = f.read()\nimport nibabel as nib\nimg = nib.Nifti1Image.from_bytes(gzip.decompress(raw_bytes))\nt_stream = time.time() - t\nprint(f\"one run streamed and decompressed in {t_stream:.1f} s: shape {img.shape}, {img.get_data_dtype()}, \"\n      f\"voxel size {img.header.get_zooms()[:3]} mm, TR field {img.header.get_zooms()[3]}\")\nn_tp = 5 * seq_trn.shape[0] + 2 * seq_val.shape[0]\nn_trials = 5 * int((seq_trn[:, 0] > 0).sum()) + 2 * int((seq_val[:, 0] > 0).sum())\nn_reg = n_trials + 4 * 7\nA = np.random.default_rng(0).standard_normal((n_tp, n_reg)).astype(np.float32)\ny = np.random.default_rng(1).standard_normal((n_tp, 1)).astype(np.float32)\nt = time.time()\nfor _ in range(3):\n    np.linalg.lstsq(A, y, rcond=None)\nt_solve = (time.time() - t) / 3\nn_vox = sum(int(np.isin(RES[s][\"D\"][\"roi\"], [1, 2, 3]).sum()) for s in (\"S1\", \"S2\"))\nn_iter = 3\nest = n_vox * 5 * n_iter * t_solve / 60 + 70 * t_stream / 60\nprint(f\"one solve of {n_tp} x {n_reg}: {t_solve:.2f} s; {n_vox} V1 to V3 voxels x 5 sessions x {n_iter} iterations \"\n      f\"(the least the autoregressive procedure needs) + streaming 70 runs: about {est:.0f} minutes, \"\n      f\"before the repeated-trial HRF fits\")\ndel raw_bytes, img, A\n\n##CELL md\nThe estimate printed above is over the notebook limit of 60 minutes and the time left in this run,\nso these claims are blocked as `too_large` and not run.\n\n## supptable1-voxel-counts\n\n> The visual areas hold 1331 (V1), 2208 (V2) and 1973 (V3) voxels in S1, and 1513, 1982 and 1780 in S2.\n\nCriterion: counts of voxels assigned to each area; reproduced when all six are within 10%.\n\n##CELL code tags=claim:supptable1-voxel-counts\npaper_counts = {\"S1\": (1331, 2208, 1973), \"S2\": (1513, 1982, 1780)}\nfor subj in (\"S1\", \"S2\"):\n    c = RES[subj][\"D\"][\"counts_all\"]\n    for area, exp in zip((\"V1\", \"V2\", \"V3\"), paper_counts[subj]):\n        print(f\"{subj} {area}: {c[area]} voxels labelled in the data set (paper {exp}; difference {c[area] - exp})\")\n\n##CELL md\n**Result: reproduced.** All six counts printed above equal the paper's.\n\n## supptable1-predictive-power-by-area\n\n> The fraction of voxels whose best initial model has significant predictive power falls from V1\n> to V2 to V3 (S1 40%, 31%, 17%; S2 25%, 21%, 13%).\n\nCriterion: best initial model, p < 0.01 by the bootstrap (O2), as a percentage of each area's\nvoxels; reproduced when V1 > V2 > V3 in both subjects and at least four of six values are within\n10%.\n\n##CELL code tags=claim:supptable1-predictive-power-by-area\npaper_frac = {\"S1\": (40, 31, 17), \"S2\": (25, 21, 13)}\nFRAC = {}\nfor subj in (\"S1\", \"S2\"):\n    R = RES[subj]; D = R[\"D\"]\n    for area, k, exp in zip((\"V1\", \"V2\", \"V3\"), (1, 2, 3), paper_frac[subj]):\n        n_sig = int(((D[\"roi\"] == k) & (R[\"init\"][\"p\"] < 0.01)).sum())\n        tot = D[\"counts_all\"][area]\n        FRAC[subj, area] = 100 * n_sig / tot\n        within = abs(FRAC[subj, area] - exp) <= 0.1 * exp\n        print(f\"{subj} {area}: {n_sig} of {tot} = {FRAC[subj, area]:.1f}% (paper {exp}%, within 10%: {within}); \"\n              f\"of the {(D['roi'] == k).sum()} voxels without NaN {100 * n_sig / (D['roi'] == k).sum():.1f}%; \"\n              f\"median r {np.median(R['init']['r'][D['roi'] == k]):.3f}\")\n    print(f\"{subj} order V1 > V2 > V3: {FRAC[subj, 'V1'] > FRAC[subj, 'V2'] > FRAC[subj, 'V3']}\")\n    for thr in (0.001, 0.05):\n        print(f\"   variant p < {thr}:\", [round(100 * float(((D['roi'] == k) & (R['init']['p'] < thr)).sum()) / D['counts_all'][a], 1)\n                                    for a, k in ((\"V1\", 1), (\"V2\", 2), (\"V3\", 3))])\nprint(\"values within 10%:\", sum(abs(FRAC[s, a] - e) <= 0.1 * e for s in (\"S1\", \"S2\") for a, e in zip((\"V1\", \"V2\", \"V3\"), paper_frac[s])), \"of 6\")\n\n##CELL md\n**Result: see the printed values.** The outcome follows from the order in each subject and the\ncount of values within tolerance printed above.\n\n## methods-v4-poor\n\n> The GWP model characterizes the responses of voxels in V1, V2 and V3 but does poorly for higher\n> areas such as V4.\n\nCriterion: the percentage of voxels whose best initial model has p < 0.01, for V4 (the data set's\nlabels) and V1 to V3; reproduced when the V4 percentage is below the V3 percentage in both subjects.\n\n##CELL code tags=claim:methods-v4-poor\nfor subj in (\"S1\", \"S2\"):\n    R = RES[subj]; D = R[\"D\"]\n    row = []\n    for area, k in ((\"V1\", 1), (\"V2\", 2), (\"V3\", 3), (\"V4\", 6)):\n        s = D[\"roi\"] == k\n        row.append(f\"{area} {100 * ((R['init']['p'] < 0.01) & s).sum() / D['counts_all'][area]:.1f}% \"\n                   f\"(median r {np.median(R['init']['r'][s]):.3f})\")\n    v3 = ((R['init']['p'] < 0.01) & (D['roi'] == 3)).sum() / D['counts_all']['V3']\n    v4 = ((R['init']['p'] < 0.01) & (D['roi'] == 6)).sum() / D['counts_all']['V4']\n    print(subj, \"; \".join(row), f\"; V4 below V3: {v4 < v3}\")\n\n##CELL md\n**Result: see the printed values** (V4 against V3 in each subject).\n\n## suppm7-selected-voxels-v1\n\n> Most of the 500 voxels used for identification were located in V1, where predictive power was highest.\n\nReadings: (a) voxels selected in more than half of the 120 selections, (b) the top 500 by\npredictive power over all 120 images; reproduced when more than half are in V1 in both subjects.\nShown for every identification reading; O1a-O5a is the first.\n\n##CELL code tags=claim:suppm7-selected-voxels-v1\nfor name in READINGS:\n    for subj in (\"S1\", \"S2\"):\n        I = ID[subj, name]; D = RES[subj][\"D\"]\n        counts = np.bincount(np.concatenate(I[\"sel\"]), minlength=D[\"roi\"].size)\n        a = np.flatnonzero(counts > 60)\n        r_all = np.where(I[\"cand\"], np.nan_to_num(vim1.pearson_cols(D[\"val\"], I[\"pred\"]), nan=-1), -np.inf)\n        b = np.argsort(-r_all)[:500]\n        fa = [(D[\"roi\"][a] == k).mean() for k in (1, 2, 3)]\n        fb = [(D[\"roi\"][b] == k).mean() for k in (1, 2, 3)]\n        print(f\"{name} {subj}: (a) {a.size} voxels, V1/V2/V3 = {fa[0]:.2f}/{fa[1]:.2f}/{fa[2]:.2f}; \"\n              f\"(b) V1/V2/V3 = {fb[0]:.2f}/{fb[1]:.2f}/{fb[2]:.2f}\")\n\n##CELL md\n**Result: see the printed fractions.**\n\n## errors-similar-images\n\n> Identification errors tended to occur when the selected image was visually similar to the correct image.\n\nCriterion: for each error of the S1 and S2 repeated-trial identification, the percentile of the\nselected image's similarity to the correct image among the correct image's similarities to the\nother 119; readings (a) pixel luminance correlation, (b) correlation of local RMS contrast in\n0.6 degree blocks; reproduced when, under one reading, the pooled errors have a median percentile\nabove 50 by a one-sided Wilcoxon signed-rank test at p < 0.05. Main identification reading O1a-O5a,\nothers shown.\n\n##CELL code tags=claim:errors-similar-images\nval_raw = full[1750:] + MU\nsim_lum = vim1.corr_rows(val_raw.reshape(120, -1), val_raw.reshape(120, -1))\nBLOCK = round(0.6 * vim1.FULL_PX / vim1.STIM_DEG)\ncon_val = vim1.local_contrast(val_raw, BLOCK)\nsim_con = vim1.corr_rows(con_val, con_val)\nprint(f\"blocks of {BLOCK} px ({BLOCK * vim1.STIM_DEG / vim1.FULL_PX:.2f} deg), {con_val.shape[1]} per image\")\n\n\ndef error_percentiles(choice, sim):\n    out = []\n    for j in np.flatnonzero(choice != np.arange(120)):\n        others = np.delete(sim[j], j)\n        out.append(100 * (others < sim[j, choice[j]]).mean())\n    return np.array(out)\n\n\nfor name in READINGS:\n    for sname, sim in ((\"(a) luminance\", sim_lum), (\"(b) local contrast\", sim_con)):\n        pct = np.concatenate([error_percentiles(ID[s, name][\"choice\"], sim) for s in (\"S1\", \"S2\")])\n        w = stats.wilcoxon(pct - 50, alternative=\"greater\")\n        per = {s: np.median(error_percentiles(ID[s, name][\"choice\"], sim)) for s in (\"S1\", \"S2\")}\n        print(f\"{name} {sname}: {pct.size} errors, median percentile {np.median(pct):.1f} \"\n              f\"(S1 {per['S1']:.1f}, S2 {per['S2']:.1f}); Wilcoxon one-sided p = {w.pvalue:.2g}\")\nrng_null = np.random.default_rng(21)\nnull = [np.median(np.concatenate([error_percentiles(rng_null.integers(0, 120, 120), sim_lum)])) for _ in range(200)]\nprint(f\"null (random choices), median percentile over 200 draws: {np.median(null):.1f} (5th to 95th {np.percentile(null, 5):.1f} to {np.percentile(null, 95):.1f})\")\n\n##CELL md\n**Result: see the printed percentiles and tests.**\n\n## suppdisc1-classification-extension\n\n> Extending classification to novel images works poorly, 1.7% and 0.8% correct with pixel\n> luminance similarity (not above chance) and 5% and 5.8% with local contrast (above chance), for\n> S1 and S2.\n\nCriterion: match each identification pattern to the most correlated of the 1,750 training\npatterns, then pick the identification image most similar to that training image. Voxels (a) the\n500 voxels of P5 for that pattern (O1a-O5a), (b) all candidate V1 to V3 voxels (O1 a and b). RMS\ncontrast (a) SD in the block, (b) SD over the block mean. Reproduced when, under one reading, each\ncount is within one image of 2, 1, 6, 7, the luminance results have binomial p >= 0.05 and the\ncontrast results p < 0.0001.\n\n##CELL code tags=claim:suppdisc1-classification-extension\ntrn_raw = full[:1750] + MU\nsim_trn_lum = vim1.corr_rows(trn_raw.reshape(1750, -1), val_raw.reshape(120, -1))     # 1750 x 120\ncon_trn = vim1.local_contrast(trn_raw, BLOCK)\nsim_trn_con = vim1.corr_rows(con_trn, con_val)\nshift = -raw_min   # values shifted to start at 0 for the relative contrast (absolute luminance not given)\ncon_trn_rel = vim1.local_contrast(trn_raw + shift, BLOCK, relative=True)\ncon_val_rel = vim1.local_contrast(val_raw + shift, BLOCK, relative=True)\nsim_trn_rel = vim1.corr_rows(con_trn_rel, con_val_rel)\ndel trn_raw\npaper = {(\"S1\", \"lum\"): 2, (\"S2\", \"lum\"): 1, (\"S1\", \"con\"): 6, (\"S2\", \"con\"): 7}\nfor vname in (\"(a) 500 voxels of P5\", \"(b) O1a voxels\", \"(b) O1b voxels\"):\n    for subj in (\"S1\", \"S2\"):\n        D = RES[subj][\"D\"]; R = RES[subj]\n        tr = D[\"trn\"] - D[\"trn\"].mean(1, keepdims=True)\n        matched = np.empty(120, int)\n        for j in range(120):\n            if vname.startswith(\"(a)\"):\n                vs = ID[subj, \"O1a-O5a\"][\"sel\"][j]\n            else:\n                vs = np.flatnonzero(R[\"candA\"] if \"O1a\" in vname else R[\"candB\"])\n            m = D[\"val\"][j, vs] - D[\"val\"][j, vs].mean()\n            t_ = D[\"trn\"][:, vs] - D[\"trn\"][:, vs].mean(1, keepdims=True)\n            matched[j] = np.argmax(t_ @ m / np.linalg.norm(t_, axis=1))\n        line = []\n        for mname, sim, key in ((\"luminance\", sim_trn_lum, \"lum\"), (\"contrast SD\", sim_trn_con, \"con\"),\n                                (\"contrast SD/mean\", sim_trn_rel, \"con\")):\n            pick = np.argmax(sim[matched], 1)\n            k_ = int((pick == np.arange(120)).sum())\n            p_ = stats.binomtest(k_, 120, 1 / 120, alternative=\"greater\").pvalue\n            line.append(f\"{mname} {k_}/120 (paper {paper[subj, key]}, p = {p_:.2g})\")\n        print(f\"{vname} {subj}: \" + \"; \".join(line))\n\n##CELL md\n**Result: see the printed counts.**\n\n## suppm8-retinotopy-only-120\n\n> At set size 120 with repeated trials, averaged across subjects, the retinotopy-only model\n> identified 55% of images with spatially-weighted luminance and contrast and 42% with the standard\n> (unweighted) metrics, both below the Gabor wavelet pyramid model.\n\nCriterion: the RO model (SM 8) at the best initial model's Gaussian, fitted by the gradient\ndescent of SM 6, voxels by its own predictive power (SM 7), identification by P5, the two\nsubjects averaged; reproduced when both values are within 10% (55 +/- 5.5, 42 +/- 4.2) and below the\nGWP mean computed here. The candidate voxels follow O1 (a) and (b).\n\n##CELL code tags=claim:suppm8-retinotopy-only-120\nRO = {}\nfor subj, seed in ((\"S1\", 31), (\"S2\", 32)):\n    R = RES[subj]; D = R[\"D\"]; rng = np.random.default_rng(seed)\n    for metric, weighted in ((\"weighted\", True), (\"standard\", False)):\n        t = time.time()\n        L, C = vim1.ro_channels(full + MU, R[\"init\"], R[\"candB\"], weighted=weighted)\n        pred = vim1.fit_ro(D, L, C, rng, R[\"candB\"])\n        power = vim1.loo_power(D[\"val\"], pred)\n        for cname in (\"candA\", \"candB\"):\n            choice, _ = vim1.identify_repeated(D[\"val\"], pred, power, cand=R[cname])\n            RO[subj, metric, cname] = 100 * (choice == np.arange(120)).mean()\n        print(f\"{subj} RO {metric}: O1a {RO[subj, metric, 'candA']:.1f}%, O1b {RO[subj, metric, 'candB']:.1f}% \"\n              f\"({time.time() - t:.0f} s)\")\n        del L, C\ngwp_mean = {name: np.mean([100 * (ID[s, name][\"choice\"] == np.arange(120)).mean() for s in (\"S1\", \"S2\")]) for name in READINGS}\nfor cname in (\"candA\", \"candB\"):\n    w_ = np.mean([RO[s, \"weighted\", cname] for s in (\"S1\", \"S2\")])\n    s_ = np.mean([RO[s, \"standard\", cname] for s in (\"S1\", \"S2\")])\n    print(f\"{cname}: mean over subjects, weighted {w_:.1f}% (paper 55), standard {s_:.1f}% (paper 42)\")\nprint(\"GWP mean over subjects:\", {k: round(v, 1) for k, v in gwp_mean.items()})\n\n##CELL md\n**Result: see the printed values.**\n\n## suppfig11-rf-size-eccentricity\n\n> Receptive-field size increases with eccentricity, and from V1 to V2 to V3.\n\nCriterion: RF size is the extent of +/-2 SD (4 SD) of the Gaussian fitted to the best initial\nmodel's envelope; voxels with p < 0.01 whose RF lies wholly inside the stimulus; pooled across\nsubjects; 1 degree eccentricity bins (0.5 degree as a variant), median per bin with at least 10\nvoxels; reproduced when, per area, the Spearman correlation of size with eccentricity is positive\nat p < 0.05, and in most bins shared by the three areas the medians order V1 < V2 < V3. \"Inside the\nstimulus\" is read as inside the 20 degree square; inside the circular aperture is shown too.\n\n##CELL code tags=claim:suppfig11-rf-size-eccentricity\nrows = []\nfor subj in (\"S1\", \"S2\"):\n    R = RES[subj]; D = R[\"D\"]; init = R[\"init\"]\n    ecc = np.hypot(init[\"cx\"], init[\"cy\"]); size = 4 * init[\"sd\"]\n    in_sq = (np.abs(init[\"cx\"]) + 2 * init[\"sd\"] <= 10) & (np.abs(init[\"cy\"]) + 2 * init[\"sd\"] <= 10)\n    in_circ = ecc + 2 * init[\"sd\"] <= RADIUS\n    for k in (1, 2, 3):\n        s = (D[\"roi\"] == k) & (init[\"p\"] < 0.01)\n        rows.append((subj, k, ecc[s], size[s], in_sq[s], in_circ[s]))\nfig, axes = plt.subplots(1, 2, figsize=(10, 4))\nfor ax, (bounds, idx) in zip(axes, ((\"square\", 4), (\"circle\", 5))):\n    for width in (1.0, 0.5):\n        bins = np.arange(0, 10 + width, width)\n        med = {}\n        for k in (1, 2, 3):\n            e = np.concatenate([r[2][r[idx]] for r in rows if r[1] == k]); z = np.concatenate([r[3][r[idx]] for r in rows if r[1] == k])\n            rho, p = stats.spearmanr(e, z)\n            b = np.digitize(e, bins) - 1\n            med[k] = {i: np.median(z[b == i]) for i in range(len(bins) - 1) if (b == i).sum() >= 10}\n            if width == 1.0:\n                print(f\"{bounds} V{k}: {e.size} voxels, Spearman rho {rho:.3f}, p = {p:.2g}; size {z.min():.1f} to {z.max():.1f} deg; \"\n                      f\"by subject \" + \", \".join(f\"{s} {int((r[idx]).sum())}\" for s in (\"S1\", \"S2\") for r in rows if r[0] == s and r[1] == k))\n                ax.plot(bins[list(med[k])] + width / 2, list(med[k].values()), \"o-\", label=f\"V{k}\")\n        shared = sorted(set(med[1]) & set(med[2]) & set(med[3]))\n        ordered = [med[1][i] < med[2][i] < med[3][i] for i in shared]\n        print(f\"   {bounds}, {width} deg bins: {sum(ordered)} of {len(shared)} shared bins ordered V1 < V2 < V3\")\n    ax.set_xlabel(\"eccentricity (deg)\"); ax.set_ylabel(\"median RF size, 4 SD (deg)\"); ax.set_title(f\"RF inside the {bounds}\"); ax.legend()\nplt.tight_layout(); plt.show()\n\n##CELL md\n**Result: see the printed correlations and bin counts.**\n\n## fig2-representative-voxel\n\n> A representative V1 voxel of S1 (voxel 42205) has its receptive field in the left hemifield just\n> below the horizontal meridian, broadband orientation tuning and high-pass spatial frequency tuning.\n\nThe data set's `voxIdx` holds 42205 for one S1 V1 voxel; it is taken to be the paper's voxel (the\npaper does not say how it numbers voxels). Criterion: envelope peak left of the vertical meridian\nand below the horizontal meridian within the central half of the stimulus height; SF tuning highest\nat the highest frequency; orientation tuning maximum less than twice its minimum.\n\n##CELL code tags=claim:fig2-representative-voxel\nGRAT = vim1.gratings()\nW, table, M = W64\nXg = vim1.gwp_channels(GRAT.reshape(-1, 64, 64), W, table, np.ones(table.shape[0], bool), False)   # 640 x channels\n\n\ndef tuning_of(k, dc, keep):\n    r = ((Xg * keep[None, :]) @ k + dc).reshape(GRAT.shape[:3]).mean(2)\n    return r.mean(1), r.mean(0)\n\n\nR = RES[\"S1\"]; D = R[\"D\"]\nv = int(np.flatnonzero(D[\"vox_idx\"] == 42205)[0])\ninit = R[\"init\"]\nprint(f\"voxel 42205: ROI {vim1.ROI_NAMES[D['roi'][v]]}, best initial model {init['best'][v]} deg, r = {init['r'][v]:.3f}, \"\n      f\"p = {init['p'][v]:.3f}; Gaussian centre ({init['cx'][v]:.2f}, {init['cy'][v]:.2f}) deg, SD {init['sd'][v]:.2f} deg\")\nfor reading in (\"O5a\", \"O5b\"):\n    if reading == \"O5a\":\n        if v not in R[\"kern_a\"]:\n            print(\"O5a: no final model (voxel not among the O1 a voxels)\"); continue\n        res_, k, dc, centre, fov, keep = R[\"kern_a\"][v]\n    else:\n        name, k, dc = R[\"kern_b\"][v]; keep = keeps_b[name]; fov = vim1.FINAL_B[name][1]; centre = (0.0, 0.0)\n    env = vim1.final_envelope(k, M)\n    iy, ix = np.unravel_index(np.argmax(env), env.shape)\n    px_deg = fov / 64\n    x_deg = centre[0] + (ix + 0.5 - 32) * px_deg; y_deg = centre[1] - (iy + 0.5 - 32) * px_deg\n    ori, sf = tuning_of(k, dc, keep)\n    sf_cpd = np.array([1, 2, 4, 8, 16]) / fov\n    pr = np.corrcoef(D[\"val\"][:, v], (R[\"pred_a\"] if reading == \"O5a\" else R[\"pred_b\"])[:, v])[0, 1]\n    print(f\"{reading}: FOV {fov:.2f} deg centred ({centre[0]:.2f}, {centre[1]:.2f}); predictive power r = {pr:.3f}\")\n    print(f\"   envelope peak at ({x_deg:.2f}, {y_deg:.2f}) deg: left {x_deg < 0}, below {y_deg < 0}, within 5 deg of the horizontal meridian {abs(y_deg) <= 5}\")\n    print(\"   orientation tuning (0 to 157.5 deg):\", np.round(ori, 3), f\"; max/min {ori.max() / ori.min():.2f}\" if ori.min() > 0 else \"; min <= 0\",\n          f\"; without the DC offset max/min {(ori - dc).max() / (ori - dc).min():.2f}\" if (ori - dc).min() > 0 else \"\")\n    print(\"   SF tuning at\", np.round(sf_cpd, 2), \"cycles/deg:\", np.round(sf, 3), f\"; highest at {sf_cpd[np.argmax(sf)]:.2f} cycles/deg, the highest frequency: {np.argmax(sf) == 4}\")\n\n##CELL md\n**Result: see the printed location and tuning.**\n\n## suppfig7-roi-tuning\n\n> The V1-averaged orientation tuning curve is nearly flat and the V1-averaged spatial frequency\n> tuning curve is band-pass; voxels have only a slight orientation bias.\n\nCriterion: mean over V1 voxels of the final models' grating tuning curves, bootstrap SE across\nvoxels; reproduced when, under one reading, the orientation curve's range is under 10% of its mean\nand the SF curve peaks at an intermediate frequency above both its lowest and highest values by\nmore than 2 SE. Reading (a) of the models (final GWP); reading (b), model I of the constrained\nmodels, is not run. Voxels: all V1 voxels with a final model, under O5 (a) and (b). The curves are\naveraged over the five spatial frequency levels of each model (1 to 16 cycles per field of view),\nsince the fields of view differ between voxels.\n\n##CELL code tags=claim:suppfig7-roi-tuning\nrng_t = np.random.default_rng(41)\nfig, axes = plt.subplots(2, 4, figsize=(14, 6))\ncol = 0\nfor subj in (\"S1\", \"S2\"):\n    R = RES[subj]; D = R[\"D\"]\n    for reading in (\"O5a\", \"O5b\"):\n        oris, sfs = [], []\n        for v, val in (R[\"kern_a\"] if reading == \"O5a\" else R[\"kern_b\"]).items():\n            if D[\"roi\"][v] != 1:\n                continue\n            if reading == \"O5a\":\n                _, k, dc, _, _, keep = val\n            else:\n                name, k, dc = val; keep = keeps_b[name]\n            o, s = tuning_of(k, dc, keep)\n            oris.append(o); sfs.append(s)\n        oris, sfs = np.array(oris), np.array(sfs)\n        mo, ms = oris.mean(0), sfs.mean(0)\n        boot = rng_t.integers(0, len(oris), (1000, len(oris)))\n        se_o = oris[boot].mean(1).std(0); se_s = sfs[boot].mean(1).std(0)\n        rng_ratio = (mo.max() - mo.min()) / abs(mo.mean())\n        peak = int(np.argmax(ms))\n        bandpass = 0 < peak < 4 and ms[peak] - ms[0] > 2 * se_s[peak] and ms[peak] - ms[4] > 2 * se_s[peak]\n        print(f\"{subj} {reading}: {len(oris)} V1 voxels; orientation curve {np.round(mo, 3)} (SE {se_o.max():.3f}), \"\n              f\"range/mean {100 * rng_ratio:.1f}%\")\n        print(f\"   SF curve (1 to 16 cycles/FOV) {np.round(ms, 3)} (SE {np.round(se_s, 3)}); peak at level {peak}; band-pass by the rule: {bandpass}\")\n        axes[0, col].errorbar(np.arange(8) * 22.5, mo, se_o); axes[0, col].set_title(f\"{subj} {reading} orientation\")\n        axes[1, col].errorbar([1, 2, 4, 8, 16], ms, se_s); axes[1, col].set_xscale(\"log\"); axes[1, col].set_title(f\"{subj} {reading} SF\")\n        col += 1\nplt.tight_layout(); plt.show()\n\n##CELL md\n**Result: see the printed curves.**\n\n## suppfig4-500-voxels (repeated trials only; blocked)\n\nThe claim needs the single-trial conditions, which are blocked; the repeated-trial conditions are\nshown as a variant that does not decide the outcome.\n\n##CELL code tags=claim:suppfig4-500-voxels\nNV = [1, 5, 10, 20, 50, 100, 200, 500, 1000]\nfor subj in (\"S1\", \"S2\"):\n    I = ID[subj, \"O1a-O5a\"]; D = RES[subj][\"D\"]\n    for name in (\"O1a-O5a\", \"O1b-O5b\"):\n        I = ID[subj, name]\n        perf = [100 * (vim1.identify_repeated(D[\"val\"], I[\"pred\"], I[\"power\"], n_vox=n, cand=I[\"cand\"])[0] == np.arange(120)).mean() for n in NV]\n        print(f\"{subj} {name} ({I['cand'].sum()} candidates):\", dict(zip(NV, np.round(perf, 1))))\n\n##CELL md\n## Summary\n\n| Claim | Outcome |\n|---|---|\n| filled in after the run | |\n\n##CELL code\nprint(f\"total run time {(time.time() - STARTED) / 60:.1f} minutes; peak memory {peak_gb():.1f} GB\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_src.txt (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && cat > t7.py <<'EOF'
import sys, time, numpy as np
sys.path.insert(0, 'entries/kay-2008')
import vim1
W,table,M=vim1.gwp(64,5)
print('nnz',W.nnz, W.shape)
imgs=np.random.default_rng(0).standard_normal((1870,64,64)).astype(np.float32)
keep=np.ones(table.shape[0],bool)
t=time.time(); X=vim1.gwp_channels(imgs,W,table,keep,False); print('sparse',time.time()-t)
Wd=W.toarray()
t=time.time(); P=imgs.reshape(1870,-1)@Wd; print('dense',time.time()-t)
Y=np.random.default_rng(1).standard_normal((1750,1)).astype(np.float32)
stop=np.arange(350)
t=time.time(); vim1.fit_gd(X[:1750],Y,stop); print('fit',time.time()-t)
t=time.time(); vim1.edge_keep(table,M,64,5.0,(1,1),9.5); print('keep',time.time()-t)
EOF
python t7.py
```

```
nnz 1785024 (4096, 5457)
sparse 0.3876368999481201
dense 0.16117215156555176
fit 0.012933492660522461
keep 0.0006086826324462891
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/kay-2008 && python3 - <<'EOF'
p='vim1.py'
s=open(p).read()
s=s.replace('''    P = (sparse.csr_matrix(W.T) @ imgs.reshape(n, -1).T).T  # n x wavelets
    P = np.asarray(P, dtype=np.float32)''','''    if sparse.issparse(W):
        P = np.asarray((sparse.csr_matrix(W.T) @ imgs.reshape(n, -1).T).T, dtype=np.float32)
    else:                                                  # dense wavelets: faster for many images
        P = imgs.reshape(n, -1) @ W''')
s=s.replace('''    W, table, M = W64
    V = D["trn"].shape[1]
    res, row, col = final_a_plan(init, voxels)''','''    W, table, M = W64
    W = W.toarray()
    V = D["trn"].shape[1]
    res, row, col = final_a_plan(init, voxels)''')
open(p,'w').write(s)
EOF
python3 - <<'EOF'
p='/tmp/claude-1001/nb_src.txt'
s=open(p).read()
s=s.replace('''for name, (res, fov) in vim1.FOVS.items():
    keep = vim1.edge_keep(*vim1.gwp(128, 6)[1:], 128, fov, (0, 0), RADIUS) if False else None
''','')
s=s.replace('''        tr = D["trn"] - D["trn"].mean(1, keepdims=True)
        matched = np.empty(120, int)
        for j in range(120):
            if vname.startswith("(a)"):
                vs = ID[subj, "O1a-O5a"]["sel"][j]
            else:
                vs = np.flatnonzero(R["candA"] if "O1a" in vname else R["candB"])
            m = D["val"][j, vs] - D["val"][j, vs].mean()
            t_ = D["trn"][:, vs] - D["trn"][:, vs].mean(1, keepdims=True)
            matched[j] = np.argmax(t_ @ m / np.linalg.norm(t_, axis=1))''','''        matched = np.empty(120, int)
        if not vname.startswith("(a)"):
            vs = np.flatnonzero(R["candA"] if "O1a" in vname else R["candB"])
            matched = np.argmax(vim1.corr_rows(D["trn"][:, vs].copy(), D["val"][:, vs].copy()), 0)
        for j in range(120 if vname.startswith("(a)") else 0):
            vs = ID[subj, "O1a-O5a"]["sel"][j]
            m = D["val"][j, vs] - D["val"][j, vs].mean()
            t_ = D["trn"][:, vs] - D["trn"][:, vs].mean(1, keepdims=True)
            matched[j] = np.argmax(t_ @ m / np.linalg.norm(t_, axis=1))''')
open(p,'w').write(s)
EOF
cd entries/kay-2008 && . $TMPDIR/kenv/bin/activate && python $TMPDIR/build.py $TMPDIR/nb_src.txt reproduce_kay_2008.ipynb
```

```
42 cells
```

**Agent calls Bash**

```bash
. $TMPDIR/kenv/bin/activate && python3 - <<'EOF'
s=open('/tmp/claude-1001/nb_src.txt').read()
s=s.replace('out["pred_a"], out["kern_a"] = vim1.final_a(D, init, full, FILL, RADIUS, rng, out["candA"], W64)',
 'out["pred_a"], out["kern_a"] = vim1.final_a(D, init, full, FILL, RADIUS, rng, out["candA"] & (np.cumsum(out["candA"]) <= 60), W64)')
s=s.replace('L, C = vim1.ro_channels(full + MU, R["init"], R["candB"], weighted=weighted)','L, C = vim1.ro_channels(full + MU, R["init"], R["candA"], weighted=weighted)')
s=s.replace('pred = vim1.fit_ro(D, L, C, rng, R["candB"])','pred = vim1.fit_ro(D, L, C, rng, R["candA"])')
open('/tmp/claude-1001/nb_dev.txt','w').write(s)
EOF
python $TMPDIR/build.py $TMPDIR/nb_dev.txt $TMPDIR/dev.ipynb && cp vim1.py $TMPDIR/ && cd $TMPDIR && date -u && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 dev.ipynb --output dev_out.ipynb 2>&1 | tail -5; date -u
```

```
42 cells
Sat Nov 14 03:16:12 UTC 2026
[NbConvertApp] Converting notebook dev.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 780138 bytes to dev_out.ipynb

real	7m28.473s
user	18m25.995s
sys	0m14.053s
Sat Nov 14 03:23:40 UTC 2026
Shell cwd was reset to
```

**Agent**

It ran end to end on the subset. Let me read the outputs.

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && python -c "
import nbformat
nb=nbformat.read('dev_out.ipynb',4)
for c in nb.cells:
  if c.cell_type!='code': continue
  for o in c.outputs:
    if o.output_type=='stream': print(o.text[-3000:])
    elif o.output_type=='error': print('ERR',o.ename,o.evalue)
  print('-----')
"
```

```
data set vim-1 version unversioned

-----
EstimatedResponses.mat         7b702b34d42ba612118d6ad99e86e217
Stimuli.mat                    464676501cb768b005f93a32c70e73c2
mask.mat                       19e624419b35eaed38534047665c526c
Stimuli_Val_FullRes.mat        2e7d70ecff050d8c74b066b35e5bc00c
Sub1_Ses1_Run1_Val.nii.gz      c40a6175ec86fc1f735db2fc4fa262f9
Stimuli_Trn_FullRes_01.mat     42a63e5b44a9e100e5e9d645226258a3
Stimuli_Trn_FullRes_02.mat     f4bf9ebb43f0236d330e10c4caaed918
Stimuli_Trn_FullRes_03.mat     b2af93d7f3e6b0d9a5584cf10dfdad11
Stimuli_Trn_FullRes_04.mat     a5a706ffea10d519b6eaf47a820df2bf
Stimuli_Trn_FullRes_05.mat     7a8b15e9c56f6d24f1368c30b3608026
Stimuli_Trn_FullRes_06.mat     7bd8f4820f34a5ee9187f17355b5cbe2
Stimuli_Trn_FullRes_07.mat     57b14d879c3f28fcf713633efadf71ae
Stimuli_Trn_FullRes_08.mat     4fd4462f29d08f922ecca8c36c7dc080
Stimuli_Trn_FullRes_09.mat     85e93ae9e7246c23e85b3b6fa86c2902
Stimuli_Trn_FullRes_10.mat     656fe7b8e3102533bc25e4f13487436c
Stimuli_Trn_FullRes_11.mat     04b32a61c2b09b58b2cf5336457bd731
Stimuli_Trn_FullRes_12.mat     95ad49db750ddd1b79e04457524ba66e
[... 199 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "Figure 2 |Fig. 2|Figure 2\b" paper/10.1038-nature06713.txt | head; grep -n "Supplementary Figure 7\." paper/10.1038-nature06713.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 872,885p paper/10.1038-nature06713.txt; grep -n "Figure 2\|spatial frequency tuning" paper/10.1038-nature06713.txt | head;
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
. $TMPDIR/kenv/bin/activate && python3 - <<'EOF'
p='/tmp/claude-1001/nb_src.txt'
s=open(p).read()
old_start=s.index('        oris, sfs = [], []\n        for v, val in')
old_end=s.index('plt.tight_layout(); plt.show()\n\n##CELL md\n**Result: see the printed curves.**')
new='''        oris, sfs, dcs = [], [], []
        for v, val in (R["kern_a"] if reading == "O5a" else R["kern_b"]).items():
            if D["roi"][v] != 1:
                continue
            if reading == "O5a":
                _, k, dc, _, _, keep = val
            else:
                name, k, dc = val; keep = keeps_b[name]
            o, s = tuning_of(k, dc, keep)
            oris.append(o); sfs.append(s); dcs.append(dc)
        dcs = np.array(dcs)[:, None]
        for label, oo, ss in (("with DC", np.array(oris), np.array(sfs)), ("without DC", np.array(oris) - dcs, np.array(sfs) - dcs)):
            mo, ms = oo.mean(0), ss.mean(0)
            boot = rng_t.integers(0, len(oo), (1000, len(oo)))
            se_o = oo[boot].mean(1).std(0); se_s = ss[boot].mean(1).std(0)
            rng_ratio = (mo.max() - mo.min()) / abs(mo.mean())
            peak = int(np.argmax(ms))
            bandpass = 0 < peak < 4 and ms[peak] - ms[0] > 2 * se_s[peak] and ms[peak] - ms[4] > 2 * se_s[peak]
            print(f"{subj} {reading} {label}: {len(oo)} V1 voxels; orientation curve {np.round(mo, 3)} (SE up to {se_o.max():.3f}), "
                  f"range/mean {100 * rng_ratio:.1f}% (flat by the rule: {rng_ratio < 0.1})")
            print(f"   SF curve (1 to 16 cycles/FOV) {np.round(ms, 3)} (SE {np.round(se_s, 3)}); peak at level {peak}; band-pass by the rule: {bandpass}")
            if label == "without DC":
                axes[0, col].errorbar(np.arange(8) * 22.5, mo, se_o); axes[0, col].set_title(f"{subj} {reading} orientation")
                axes[1, col].errorbar([1, 2, 4, 8, 16], ms, se_s); axes[1, col].set_xscale("log"); axes[1, col].set_title(f"{subj} {reading} SF")
                axes[1, col].set_xlabel("cycles per FOV")
        if reading == "O5a":
            fovs = np.array([val[4] for v, val in R["kern_a"].items() if D["roi"][v] == 1])
            print(f"   fields of view {fovs.min():.1f} to {fovs.max():.1f} deg (median {np.median(fovs):.1f}): level 16 cycles/FOV is "
                  f"{16 / np.median(fovs):.2f} cycles/deg at the median")
        col += 1
'''
s=s[:old_start]+new+s[old_end:]
s=s.replace('''    print("   orientation tuning (0 to 157.5 deg):", np.round(ori, 3), f"; max/min {ori.max() / ori.min():.2f}" if ori.min() > 0 else "; min <= 0",
          f"; without the DC offset max/min {(ori - dc).max() / (ori - dc).min():.2f}" if (ori - dc).min() > 0 else "")''','''    print("   orientation tuning (0 to 157.5 deg):", np.round(ori, 3), f"; max/min {ori.max() / ori.min():.2f}" if ori.min() > 0 else "; min <= 0",
          f"; without the DC offset {np.round(ori - dc, 3)}, max/min {(ori - dc).max() / (ori - dc).min():.2f}" if (ori - dc).min() > 0 else "; without DC min <= 0")''')
open(p,'w').write(s)
EOF
grep -n "rng_t\|without DC" $TMPDIR/nb_src.txt | head; date -u
```

```
637:          f"; without the DC offset {np.round(ori - dc, 3)}, max/min {(ori - dc).max() / (ori - dc).min():.2f}" if (ori - dc).min() > 0 else "; without DC min <= 0")
657:rng_t = np.random.default_rng(41)
674:        for label, oo, ss in (("with DC", np.array(oris), np.array(sfs)), ("without DC", np.array(oris) - dcs, np.array(sfs) - dcs)):
676:            boot = rng_t.integers(0, len(oo), (1000, len(oo)))
684:            if label == "without DC":
Sat Nov 14 03:24:25 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/kay-2008 && cat > requirements.in <<'EOF'
aiohttp
fsspec
h5py
matplotlib
nibabel
numpy
requests
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: kay-2008
type: reproduction
title: Identifying natural images from human brain activity (Kay et al. 2008)
description: Tests the findings of Kay, Naselaris, Prenger and Gallant (2008) on CRCNS data set vim-1, which
  holds the estimated fMRI responses of two subjects to 1,750 model estimation images and 120
  identification images, with ROI labels, the stimuli and the raw time series. It fits the Gabor
  wavelet pyramid receptive-field models of the paper, identifies the 120 images from the responses,
  and tests the retinotopy-only model, voxel counts and predictive power by area, receptive-field
  size, tuning, and the classification extension. The 999-image library, the later sessions of S1
  and the retinotopic mapping scans are not in the data set.
license: Apache-2.0
notebooks:
- path: reproduce_kay_2008.ipynb
  title: Reproducing Kay et al. (2008) from CRCNS vim-1
  runtime_minutes: 25
helpers:
- vim1.py
related:
- id: crcns:vim-1/unversioned
  relation: uses_data
- id: doi:10.1038/nature06713
  relation: reproduces
EOF
. $TMPDIR/kenv/bin/activate && python $TMPDIR/build.py $TMPDIR/nb_src.txt reproduce_kay_2008.ipynb && cd ../.. && python tools/entry.py lock entries/kay-2008 2>&1 | tail -3 && python tools/entry.py check entries/kay-2008 2>&1 | tail -15
```

```
42 cells
wrote kay-2008/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent calls Bash**

```bash
date -u && python tools/entry.py all entries/kay-2008 2>&1 | tail -15; date -u
```

```
Sat Nov 14 03:24:43 UTC 2026
Installed kernelspec registry-kay-2008 in executed/kay-2008/.venv/share/jupyter/kernels/registry-kay-2008
0 error(s)
pass  reproduce_kay_2008.ipynb  (1057 s)
Sat Nov 14 03:42:27 UTC 2026
```

**Agent**

The full run passed in about 18 minutes. Reading the results.

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && python -c "
import nbformat
nb=nbformat.read('executed/kay-2008/reproduce_kay_2008.ipynb',4)
for i,c in enumerate(nb.cells):
  if c.cell_type!='code' or i<8: continue
  for o in c.outputs:
    if o.output_type=='stream': print(o.text[-3500:])
    elif o.output_type=='error': print('ERR',o.ename,o.evalue)
  print('-----',i)
" | grep -v RuntimeWarning | grep -v "return (a"
```

```
S1: median r over 1084 V1 voxels, image order 0.215; permuted orders -0.024 to 0.046
S2: median r over 1083 V1 voxels, image order 0.140; permuted orders -0.035 to 0.025

----- 9
S1 O1a-O5a: 109/120 = 90.8% correct (candidate voxels 1574; binomial p against chance 1/120 = 2.5e-212)

S1 O1a-O5b: 91/120 = 75.8% correct (candidate voxels 1574; binomial p against chance 1/120 = 2.7e-162)

S1 O1b-O5b: 91/120 = 75.8% correct (candidate voxels 4135; binomial p against chance 1/120 = 2.7e-162)

S1 best initial models only (O1 a): 96/120

S2 O1a-O5a: 87/120 = 72.5% correct (candidate voxels 1086; binomial p against chance 1/120 = 3.6e-152)

S2 O1a-O5b: 56/120 = 46.7% correct (candidate voxels 1086; binomial p against chance 1/120 = 1.6e-82)

S2 O1b-O5b: 56/120 = 46.7% correct (candidate voxels 3770; binomial p against chance 1/120 = 1.6e-82)

S2 best initial models only (O1 a): 77/120
O1 b with O5 a: not run (time, see above).
[... 139 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kay-2008 && cat >> vim1.py <<'EOF'


def aperture(fov, centre, radius, npx=64):
    """True for the pixels of a field of view that lie inside the circular stimulus (radius in deg)."""
    yy, xx = np.mgrid[0:npx, 0:npx] + 0.5
    x = centre[0] + (xx - npx / 2) * fov / npx
    y = centre[1] - (yy - npx / 2) * fov / npx
    return np.hypot(x, y) <= radius
EOF
. $TMPDIR/kenv/bin/activate && python3 - <<'EOF'
p='/tmp/claude-1001/nb_src.txt'
s=open(p).read()
# aperture variant in suppfig7
s=s.replace('''            o, s = tuning_of(k, dc, keep)
            oris.append(o); sfs.append(s); dcs.append(dc)
        dcs = np.array(dcs)[:, None]
        for label, oo, ss in (("with DC", np.array(oris), np.array(sfs)), ("without DC", np.array(oris) - dcs, np.array(sfs) - dcs)):''','''            o, s = tuning_of(k, dc, keep)
            oris.append(o); sfs.append(s); dcs.append(dc)
            ap = vim1.aperture(val[4], val[3], RADIUS) if reading == "O5a" else vim1.aperture(vim1.FINAL_B[name][1], (0.0, 0.0), RADIUS)
            Xap = vim1.gwp_channels((GRAT * ap).reshape(-1, 64, 64), Wd64, table, keep, False)
            r_ap = (Xap @ k).reshape(GRAT.shape[:3]).mean(2)
            oris_ap.append(r_ap.mean(1)); sfs_ap.append(r_ap.mean(0))
        dcs = np.array(dcs)[:, None]
        for label, oo, ss in (("with DC", np.array(oris), np.array(sfs)), ("without DC", np.array(oris) - dcs, np.array(sfs) - dcs),
                              ("without DC, gratings inside the stimulus aperture", np.array(oris_ap), np.array(sfs_ap)),
                              ("median over voxels, without DC", np.array(oris) - dcs, np.array(sfs) - dcs)):
            if label.startswith("median"):
                mo, ms = np.median(oo, 0), np.median(ss, 0)
                print(f"{subj} {reading} {label}: orientation {np.round(mo, 3)}, range/median {100 * (mo.max() - mo.min()) / abs(mo.mean()):.1f}%; "
                      f"SF {np.round(ms, 3)}, peak at level {int(np.argmax(ms))}")
                continue''')
s=s.replace('''        oris, sfs, dcs = [], [], []''','''        oris, sfs, dcs, oris_ap, sfs_ap = [], [], [], [], []''')
s=s.replace('''rng_t = np.random.default_rng(41)''','''rng_t = np.random.default_rng(41)
Wd64 = W.toarray()''')
# fig2 aperture variant
s=s.replace('''    print("   SF tuning at", np.round(sf_cpd, 2), "cycles/deg:", np.round(sf, 3), f"; highest at {sf_cpd[np.argmax(sf)]:.2f} cycles/deg, the highest frequency: {np.argmax(sf) == 4}")''','''    print("   SF tuning at", np.round(sf_cpd, 2), "cycles/deg:", np.round(sf, 3), f"; highest at {sf_cpd[np.argmax(sf)]:.2f} cycles/deg, the highest frequency: {np.argmax(sf) == 4}")
    ap = vim1.aperture(fov, centre, RADIUS)
    Xap = vim1.gwp_channels((GRAT * ap).reshape(-1, 64, 64), W, table, keep, False)
    r_ap = (Xap @ k).reshape(GRAT.shape[:3]).mean(2)
    o_ap, s_ap = r_ap.mean(1), r_ap.mean(0)
    print(f"   variant, gratings inside the stimulus aperture ({ap.mean():.2f} of the FOV), without DC: orientation {np.round(o_ap, 3)}, "
          f"max/min {o_ap.max() / o_ap.min():.2f}; SF {np.round(s_ap, 3)}, highest at level {np.argmax(s_ap)}")
    print(f"   envelope near the peak (rows top to bottom, deg above the horizontal meridian of each row): "
          f"{[round(centre[1] - (i + 0.5 - 32) * px_deg, 2) for i in range(iy - 2, iy + 3)]}")
    print("   ", np.round(env[iy - 2:iy + 3, ix - 2:ix + 3] / env.max(), 3).tolist())''')
# SNR timing
s=s.replace('''print(f"one solve of {n_tp} x {n_reg}: {t_solve:.2f} s;''','''n_tp_r = 5 * seq_trn.shape[0]; n_reg_r = 350 + 4 * 5
A_r = np.random.default_rng(2).standard_normal((n_tp_r, n_reg_r)).astype(np.float32)
t = time.time()
for _ in range(3):
    np.linalg.lstsq(A_r, y[:n_tp_r], rcond=None)
t_solve_r = (time.time() - t) / 3
est_r = n_vox * 5 * n_iter * 2 * t_solve_r / 60 + 50 * t_stream / 60
print(f"repeated-trial fit (for the SNR), one solve of {n_tp_r} x {n_reg_r}: {t_solve_r:.3f} s; with the alternating HRF step "
      f"(counted as a second solve) over {n_vox} voxels x 5 sessions x {n_iter} iterations + streaming 50 runs: about {est_r:.0f} minutes")
print(f"one solve of {n_tp} x {n_reg}: {t_solve:.2f} s;''')
open(p,'w').write(s)
EOF
grep -n "Wd64\|oris_ap" $TMPDIR/nb_src.txt | head
```

```
676:Wd64 = W.toarray()
682:        oris, sfs, dcs, oris_ap, sfs_ap = [], [], [], [], []
693:            Xap = vim1.gwp_channels((GRAT * ap).reshape(-1, 64, 64), Wd64, table, keep, False)
695:            oris_ap.append(r_ap.mean(1)); sfs_ap.append(r_ap.mean(0))
698:                              ("without DC, gratings inside the stimulus aperture", np.array(oris_ap), np.array(sfs_ap)),
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && cp entries/kay-2008/vim1.py . && python -c "
import numpy as np, vim1
GRAT=vim1.gratings(); W,table,M=vim1.gwp(64,5); Wd64=W.toarray()
k=np.random.default_rng(0).standard_normal(table.shape[0]).astype(np.float32); keep=np.ones(table.shape[0],bool)
ap=vim1.aperture(5.0,(-8.0,0.5),9.5); print(ap.mean())
Xap=vim1.gwp_channels((GRAT*ap).reshape(-1,64,64),Wd64,table,keep,False)
r=(Xap@k).reshape(GRAT.shape[:3]).mean(2); print(r.shape, r.mean(1)[:3])
"
```

```
0.77490234375
(8, 5) [  6.7757998 -16.31394   -14.322939 ]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
. $TMPDIR/kenv/bin/activate && python3 - <<'EOF'
p='/tmp/claude-1001/nb_src.txt'
s=open(p).read()
def rep(old,new):
    global s
    assert s.count(old)==1, old
    s=s.replace(old,new)
rep('''**Result: not reproduced.** The values are printed above for each reading; the criterion asks
for 82.8% or more for S1 and 64.8% to 79.2% for S2 under one reading.''','''**Result: reproduced (both claims).** Under O1 (a) with O5 (a), 109 of 120 images (90.8%) are
identified for S1 and 87 of 120 (72.5%) for S2, against 110 and 86 in the paper and chance of 1 in
120; both are within tolerance. Under O5 (b), with the final model over the best initial model's
field of view, performance is 75.8% (S1) and 46.7% (S2) for both readings of O1, outside tolerance,
and below the best initial models alone (96 and 77 of 120). Ten bootstrap fits change O5 (b) by at
most three images (90 and 59 of 120). The O1 (b) with O5 (a) combination was not run.''')
rep('''**Result: see the printed values.** The outcome follows from the order in each subject and the
count of values within tolerance printed above.''','''**Result: reproduced.** The fractions are 41.2%, 30.2% and 18.2% (S1) and 26.8%, 22.6% and 13.1%
(S2), all six within 10% of the paper's values, and V1 > V2 > V3 in both subjects. The denominators
are all voxels the data set labels in each area; 345 (S1) and 214 (S2) of them have NaN responses
and count as not significant.''')
rep('''**Result: see the printed values** (V4 against V3 in each subject).''','''**Result: reproduced.** V4 voxels with significant predictive power are 17.5% (S1) and 8.6% (S2),
below V3 (18.2% and 13.1%) in both subjects; the S1 margin is small (0.7 points). Median r is
0.019 (S1) and 0.000 (S2) in V4, against 0.135 and 0.069 in V1.''')
rep('''**Result: see the printed fractions.**''','''**Result: not reproduced.** Under the first identification reading (O1a-O5a), 48% of the selected
voxels lie in V1 in both subjects, under both readings of the selection (V2 41 to 42%, V3 10 to
11%); under O5 (b) it is 42 to 43%. V1 holds the largest share but not more than half.''')
rep('''**Result: see the printed percentiles and tests.**''','''**Result: reproduced, under reading (b).** With local contrast as the similarity, the 44 errors of
O1a-O5a have a median percentile of 68.9 (S1 93.3, S2 64.7), one-sided Wilcoxon p = 0.00031; with
pixel luminance the median is 42.4 (p = 0.7). The other identification readings give the same
pattern (contrast 61.3 and 63.9, p = 1.2e-05; luminance p >= 0.93). Random choices give a median
near 50 (49.6).''')
rep('''**Result: see the printed counts.**''','''**Result: not reproduced.** The luminance metric is not above chance under any reading (0 to 3 of
120, p >= 0.08), as in the paper. The contrast metric is above chance at p < 0.0001 only for S1 with
the 500 voxels of P5 and the SD measure (9 of 120, p = 8.8e-07); for S2 it is 1 or 2 of 120
(p >= 0.26) under every reading, against 7 in the paper. No reading gives the paper's pattern.''')
rep('''**Result: see the printed values.**''','''**Result: reproduced.** Averaged over subjects, the RO model identifies 53.3% of images with the
spatially-weighted metrics and 43.8% with the standard metrics (O1 a; 52.9% and 42.5% under O1 b),
within tolerance of 55% and 42%, and both below the GWP mean of 81.7% under O1a-O5a (and of 61.2%
under the O5 (b) readings).''')
rep('''**Result: see the printed correlations and bin counts.**''','''**Result: reproduced, resting on the reading of "inside the stimulus" as the 20 degree square.**
RF size increases with eccentricity in each area (Spearman rho 0.535, 0.628 and 0.649, p < 1e-40),
and in 1 degree bins the medians order V1 < V2 < V3 in 5 of the 8 bins shared by the three areas.
With RFs required to lie inside the circular aperture the correlations hold (rho 0.573 to 0.676)
but the order holds in 3 of 6 bins; with 0.5 degree bins it holds in 6 of 12 (square) and 3 of 9
(circle), half or fewer.''')
rep('''**Result: see the printed location and tuning.**''','''**Result: partially reproduced, resting on O5 (a) and tuning without the DC offset.** Under O5 (a),
whose 5.45 degree field of view gives a highest frequency of 2.94 cycles/deg as on the paper's axis
(2.9), the envelope peaks at (-3.42, +0.24) deg: in the left hemifield but 0.24 degrees above the
horizontal meridian (the fitted Gaussian's centre, -0.57, is below); SF tuning is highest at the
highest frequency (high-pass); the orientation tuning's max/min is 2.23 without the DC offset and
16.2 with it, so not broadband by the rule. Under O5 (b) the peak is at (-4.22, -0.47), SF tuning is
highest at the highest frequency and orientation max/min is 1.77 without the DC offset (6.54 with
it): all three parts hold without the DC offset.''')
rep('''**Result: see the printed curves.**''','''**Result: not reproduced.** In every reading run (O5 a and b, both subjects, with or without the DC
offset, gratings over the field of view or inside the aperture, mean or median over voxels), the V1
spatial frequency curve rises to the highest level (16 cycles per field of view), so it is
high-pass, not band-pass, and the orientation curve's range is far above 10% of its mean (47% at
the least). Under O5 (a) the mean curves are dominated by a few voxels with very large responses to
full-field gratings (SE up to about 1,000 in the units of the responses).''')
rep('''| Claim | Outcome |
|---|---|
| filled in after the run | |''','''| Claim | Outcome |
|---|---|
| fig3-s1-repeated-120 | reproduced (109/120 under O1a-O5a) |
| fig4a-s2-repeated-120 | reproduced (87/120 under O1a-O5a) |
| fig4a-single-trial | blocked, too large |
| fig4a-noise-ceiling | blocked, too large (depends on single trials) |
| fig4b-set-size-1000 | blocked, data missing (999-image library) |
| fig4b-extrapolation | blocked, data missing |
| fig4c-retinotopy-only-extrapolation | blocked, data missing |
| suppm8-retinotopy-only-120 | reproduced |
| suppfig8-constrained-models | blocked, data missing |
| time-two-months | blocked, data missing |
| time-fourteen-months | blocked, data missing |
| errors-similar-images | reproduced (local contrast reading) |
| suppfig4-500-voxels | blocked, too large (depends on single trials) |
| supptable1-voxel-counts | reproduced |
| supptable1-predictive-power-by-area | reproduced |
| supptable1-snr | blocked, too large |
| methods-v4-poor | reproduced |
| fig2-representative-voxel | partially reproduced (assumed) |
| suppfig7-roi-tuning | not reproduced |
| suppfig10-retinotopy-validation | blocked, data missing |
| suppfig11-rf-size-eccentricity | reproduced (assumed) |
| suppdisc1-classification-extension | not reproduced |
| suppm7-selected-voxels-v1 | not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

How the analysis differs from the paper's: one gradient-descent fit per model instead of the mean of
100 bootstrap fits; one stopping set shared by the voxels fitted together; the initial fields of
view are 10.0 and 5.12 degrees (the paper's 10.1 and 5.2 are not on its resolution list); the
wavelet SD follows from a 1-octave bandwidth (orientation bandwidth 37 degrees, not 41); stimulus
values taken as linear in luminance; area-averaging resampling; the final model's field of view
read two ways (O5), of which only the +/-2 SD square reproduces the identification results; the
O1 (b) with O5 (a) combination not run. The single-trial and SNR analyses need per-voxel fits of
the time series that do not fit in the time available.

What was found about the data set: the repeated-trial responses, ROI labels and stimuli match the
paper (voxel counts per area equal Supplementary Table 1; run designs as SM 1 describes). The readme
calls `Stimuli.mat` a MATLAB 7.3 file (it is MATLAB 5) and gives `Stimuli_Trn_FullRes_15.mat` as
70 x 120 x 120 (it is 70 x 500 x 500). 345 (S1) and 214 (S2) V1 to V3 voxels have NaN responses,
which the readme does not mention. The NIfTI headers give a TR of 0. The data set holds no
single-trial responses, no standard errors, none of S1's later sessions, no 999-image library and
no retinotopic mapping data.''')
open(p,'w').write(s)
EOF
cd entries/kay-2008 && python $TMPDIR/build.py $TMPDIR/nb_src.txt reproduce_kay_2008.ipynb && date -u
```

```
42 cells
Sat Nov 14 03:44:25 UTC 2026
```

**Agent calls Bash**

```bash
cd  && date -u && python tools/entry.py all entries/kay-2008 2>&1 | tail -4; date -u
```

```
Sat Nov 14 03:44:30 UTC 2026
Installed kernelspec registry-kay-2008 in executed/kay-2008/.venv/share/jupyter/kernels/registry-kay-2008
0 error(s)
pass  reproduce_kay_2008.ipynb  (1246 s)
Sat Nov 14 04:05:24 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && python -c "
import nbformat
nb=nbformat.read('executed/kay-2008/reproduce_kay_2008.ipynb',4)
for i,c in enumerate(nb.cells):
  if c.cell_type!='code' or i not in (7,9,11,13,17,33,35,39): continue
  for o in c.outputs:
    if o.output_type=='stream': print(o.text[-4000:])
    elif o.output_type=='error': print('ERR',o.ename,o.evalue)
  print('-----',i)
" | grep -v RuntimeWarning | grep -v "return (a"
```

```
channels in 20 s: {'20': (1870, 1366), '10': (1870, 1366), '5': (1870, 1366)} initial; {'20': (1870, 2729), '10': (1870, 2729), '5': (1870, 2729)} final (O5 b)
fields of view of the initial models (deg): {'20': 20.0, '10': 10.0, '5': 5.12}


S1: initial models 72 s, final (b) 11 s for 4135 voxels, final (a) 350 s for 1574 voxels (0.22 s each); peak memory 8.1 GB
   initial 20 deg: fits that stopped at iteration 0 (no kernel) 1944 of 6702; iterations median 8, max 395; valid RF 4758
   initial 10 deg: fits that stopped at iteration 0 (no kernel) 2100 of 6702; iterations median 5, max 295; valid RF 2251
   initial  5 deg: fits that stopped at iteration 0 (no kernel) 2401 of 6702; iterations median 3, max 211; valid RF 1771
   best initial model: {'20': 3306, '10': 950, '5': 1032} ; voxels with none: 1414

S2: initial models 61 s, final (b) 6 s for 3770 voxels, final (a) 248 s for 1086 voxels (0.23 s each); peak memory 8.3 GB
   initial 20 deg: fits that stopped at iteration 0 (no kernel) 2059 of 6083; iterations median 6, max 296; valid RF 4024
   initial 10 deg: fits that stopped at iteration 0 (no kernel) 2240 of 6083; iterations median 4, max 183; valid RF 1539
   initial  5 deg: fits that stopped at iteration 0 (no kernel) 2316 of 6083; iterations median 3, max 225; valid RF 1463
   best initial model: {'20': 2906, '10': 729, '5': 829} ; voxels with none: 1619

----- 7
S1: median r over 1084 V1 voxels, image order 0.215; permuted orders -0.024 to 0.046
S2: median r over 1083 V1 voxels, image order 0.140; permuted orders -0.035 to 0.025

[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && python -c "
import nbformat
nb=nbformat.read('executed/kay-2008/reproduce_kay_2008.ipynb',4)
c=nb.cells[37]
for o in c.outputs:
    if o.output_type=='stream': print(o.text[-6000:])
"
```

```
S1 O5a with DC: 548 V1 voxels; orientation curve [ 262.813  457.035   53.422 -143.375  -60.459   98.917  137.286  146.661] (SE up to 1028.782), range/mean 504.4% (flat by the rule: False)
   SF curve (1 to 16 cycles/FOV) [ -6.05   -9.886  -6.312 110.018 507.418] (SE [ 42.217  84.72  166.884 375.636 960.333]); peak at level 4; band-pass by the rule: False
S1 O5a without DC: 548 V1 voxels; orientation curve [ 263.327  457.549   53.936 -142.861  -59.944   99.431  137.8    147.175] (SE up to 1019.018), range/mean 502.2% (flat by the rule: False)
   SF curve (1 to 16 cycles/FOV) [ -5.536  -9.372  -5.798 110.532 507.933] (SE [ 42.621  85.478 167.607 369.972 946.666]); peak at level 4; band-pass by the rule: False
S1 O5a without DC, gratings inside the stimulus aperture: 548 V1 voxels; orientation curve [0.86  1.051 1.178 0.947 0.763 0.959 1.067 0.951] (SE up to 0.031), range/mean 42.7% (flat by the rule: False)
   SF curve (1 to 16 cycles/FOV) [0.275 0.488 0.917 1.493 1.687] (SE [0.011 0.019 0.033 0.042 0.053]); peak at level 4; band-pass by the rule: False
S1 O5a median over voxels, without DC: orientation [0.821 1.031 1.153 0.94  0.737 0.939 1.042 0.966], range/median 43.6%; SF [0.211 0.432 0.879 1.546 1.574], peak at level 4
   fields of view 2.6 to 20.0 deg (median 4.6): level 16 cycles/FOV is 3.49 cycles/deg at the median

S1 O5b with DC: 1084 V1 voxels; orientation curve [-0.     0.16   0.316  0.182  0.049  0.183  0.245  0.083] (SE up to 0.013), range/mean 208.1% (flat by the rule: False)
   SF curve (1 to 16 cycles/FOV) [-0.214 -0.212 -0.195  0.22   1.161] (SE [0.008 0.008 0.01  0.009 0.044]); peak at level 4; band-pass by the rule: False
S1 O5b without DC: 1084 V1 voxels; orientation curve [0.21  0.371 0.527 0.392 0.259 0.393 0.455 0.293] (SE up to 0.019), range/mean 87.4% (flat by the rule: False)
   SF curve (1 to 16 cycles/FOV) [-0.004 -0.002  0.016  0.43   1.372] (SE [0.002 0.004 0.007 0.016 0.05 ]); peak at level 4; band-pass by the rule: False
S1 O5b without
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/kenv/bin/activate && python3 - <<'EOF'
p='/tmp/claude-1001/nb_src.txt'
s=open(p).read()
def rep(old,new,count=1):
    global s
    assert s.count(old)==count, (old, s.count(old))
    s=s.replace(old,new)
rep('''every V1 to V3 voxel with a best initial model, and under O5 (a) for the V1 to V3 voxels whose best
initial model has p < 0.01 (O1 a). The combination O1 (b) with O5 (a) is not run: it needs a
separate model for each of about 4,000 voxels per subject, and at the rate printed below it would
add about 50 minutes.''','''every V1 to V3 voxel with a best initial model (O1 b), and under O5 (a) for the same voxels, one
model per voxel. Each voxel's final model is fitted on its own, so the O1 (a) readings use the
same models restricted to the voxels whose best initial model has p < 0.01.''')
rep('''    out["pred_a"], out["kern_a"] = vim1.final_a(D, init, full, FILL, RADIUS, rng, out["candA"], W64)''','''    out["pred_a"], out["kern_a"] = vim1.final_a(D, init, full, FILL, RADIUS, rng, out["candB"], W64)''')
rep('''f"final (a) {R['t_a']:.0f} s for {R['candA'].sum()} voxels ({R['t_a'] / max(R['candA'].sum(), 1):.2f} s each); "''','''f"final (a) {R['t_a']:.0f} s for {R['candB'].sum()} voxels ({R['t_a'] / max(R['candB'].sum(), 1):.2f} s each); "''')
rep('''READINGS = {"O1a-O5a": ("pred_a", "candA"), "O1a-O5b": ("pred_b", "candA"), "O1b-O5b": ("pred_b", "candB")}''','''READINGS = {"O1a-O5a": ("pred_a", "candA"), "O1a-O5b": ("pred_b", "candA"), "O1b-O5a": ("pred_a", "candB"),
            "O1b-O5b": ("pred_b", "candB")}''')
rep('''print("O1 b with O5 a: not run (time, see above).")
''','')
rep('''range is far above 10% of its mean (47% at
the least).''','''range is far above 10% of its mean (26% at
the least).''')
rep('''        for v, val in (R["kern_a"] if reading == "O5a" else R["kern_b"]).items():
            if D["roi"][v] != 1:''','''        for v, val in (R["kern_a"] if reading == "O5a" else R["kern_b"]).items():
            if D["roi"][v] != 1 or not R["candB"][v]:''')
open(p,'w').write(s)
EOF
grep -n "O1 (a) with O5 (a), 109\|O1a-O5a\b" $TMPDIR/nb_src.txt | head -5
```

```
241:READINGS = {"O1a-O5a": ("pred_a", "candA"), "O1a-O5b": ("pred_b", "candA"), "O1b-O5a": ("pred_a", "candB"),
276:    I = ID[subj, "O1a-O5a"]; D = RES[subj]["D"]; sel = I["sel"]
279:    ax.set_title(f"{subj}, O1a-O5a: r from {rmat.min():.2f} to {rmat.max():.2f}")
283:**Result: reproduced (both claims).** Under O1 (a) with O5 (a), 109 of 120 images (90.8%) are
422:Shown for every identification reading; O1a-O5a is the first.
```

**Agent calls Bash**

```bash
. $TMPDIR/kenv/bin/activate && python3 - <<'EOF'
p='/tmp/claude-1001/nb_src.txt'
s=open(p).read()
old='''read two ways (O5), of which only the +/-2 SD square reproduces the identification results; the
O1 (b) with O5 (a) combination not run. The single-trial'''
assert old in s
s=s.replace(old,'''read two ways (O5), of which only the +/-2 SD square reproduces the identification results. The single-trial''')
open(p,'w').write(s)
EOF
cd entries/kay-2008 && python $TMPDIR/build.py $TMPDIR/nb_src.txt reproduce_kay_2008.ipynb && cd ../.. && date -u && python tools/entry.py all entries/kay-2008 2>&1 | tail -3; date -u
```

```
42 cells
Sat Nov 14 04:06:00 UTC 2026
Installed kernelspec registry-kay-2008 in executed/kay-2008/.venv/share/jupyter/kernels/registry-kay-2008
0 error(s)
pass  reproduce_kay_2008.ipynb  (2348 s)
Sat Nov 14 04:45:16 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && python -c "
import nbformat
nb=nbformat.read('executed/kay-2008/reproduce_kay_2008.ipynb',4)
for i,c in enumerate(nb.cells):
  if c.cell_type!='code' or i not in (7,9,11,23,25,27,29,37,41): continue
  for o in c.outputs:
    if o.output_type=='stream': print(o.text[-5000:])
  print('-----',i)
" | grep -v RuntimeWarning | grep -v "return (a\|r = p @"
```

```
channels in 17 s: {'20': (1870, 1366), '10': (1870, 1366), '5': (1870, 1366)} initial; {'20': (1870, 2729), '10': (1870, 2729), '5': (1870, 2729)} final (O5 b)
fields of view of the initial models (deg): {'20': 20.0, '10': 10.0, '5': 5.12}


S1: initial models 74 s, final (b) 11 s for 4135 voxels, final (a) 847 s for 4135 voxels (0.20 s each); peak memory 8.1 GB
   initial 20 deg: fits that stopped at iteration 0 (no kernel) 1944 of 6702; iterations median 8, max 395; valid RF 4758
   initial 10 deg: fits that stopped at iteration 0 (no kernel) 2100 of 6702; iterations median 5, max 295; valid RF 2251
   initial  5 deg: fits that stopped at iteration 0 (no kernel) 2401 of 6702; iterations median 3, max 211; valid RF 1771
   best initial model: {'20': 3306, '10': 950, '5': 1032} ; voxels with none: 1414

S2: initial models 61 s, final (b) 6 s for 3770 voxels, final (a) 762 s for 3770 voxels (0.20 s each); peak memory 8.3 GB
   initial 20 deg: fits that stopped at iteration 0 (no kernel) 2059 of 6083; iterations median 6, max 296; valid RF 4024
   initial 10 deg: fits that stopped at iteration 0 (no kernel) 2240 of 6083; iterations median 4, max 183; valid RF 1539
   initial  5 deg: fits that stopped at iteration 0 (no kernel) 2316 of 6083; iterations median 3, max 225; valid RF 1463
   best initial model: {'20': 2906, '10': 729, '5': 829} ; voxels with none: 1619

----- 7
S1: median r over 1084 V1 voxels, image order 0.215; permuted orders -0.024 to 0.046
S2: median r over 1083 V1 voxels, image order 0.140; permuted orders -0.035 to 0.025

[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/kenv/bin/activate && python3 - <<'EOF'
p='/tmp/claude-1001/nb_src.txt'
s=open(p).read()
def rep(old,new):
    global s
    assert s.count(old)==1, old
    s=s.replace(old,new)
rep('''**Result: reproduced (both claims).** Under O1 (a) with O5 (a), 109 of 120 images (90.8%) are
identified for S1 and 87 of 120 (72.5%) for S2, against 110 and 86 in the paper and chance of 1 in
120; both are within tolerance. Under O5 (b)''','''**Result: reproduced (both claims).** Under O1 (a) with O5 (a), 109 of 120 images (90.8%) are
identified for S1 and 87 of 120 (72.5%) for S2, against 110 and 86 in the paper and chance of 1 in
120; both are within tolerance. O1 (b) with O5 (a) gives 109 (90.8%) and 86 (71.7%). Under O5 (b)''')
rep('''most three images (90 and 59 of 120). The O1 (b) with O5 (a) combination was not run.''','''most three images (90 and 59 of 120).''')
rep('''(26% at
the least).''','''(31% at
the least).''')
rep('''full-field gratings (SE up to about 1,000 in the units of the responses).''','''full-field gratings (SE up to about 740 in the units of the responses); gratings inside the
aperture remove that, and the curves still rise to the highest level.''')
rep('''The other identification readings give the same
pattern (contrast 61.3 and 63.9, p = 1.2e-05; luminance p >= 0.93).''','''The other identification readings give the same
pattern (contrast 68.9, 61.3 and 63.9, p <= 0.00015; luminance p >= 0.7).''')
open(p,'w').write(s)
EOF
cd entries/kay-2008 && python $TMPDIR/build.py $TMPDIR/nb_src.txt reproduce_kay_2008.ipynb && sed -i 's/runtime_minutes: 25/runtime_minutes: 40/' entry.yaml && cat ../../attempts/fouke-2025-01.yaml | head -150
```

```
42 cells
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
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '/^findings:/,$p' attempts/fouke-2025-01.yaml | head -80; ls schemas; grep -n "blocked_by\|enum" schemas/attempt*.json | head -40
```

```
findings:
- kind: data_missing
  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
    the GitLab repository the paper names for all behavioural and imaging data holds analysis
    notebooks only. Nine of the paper's main findings cannot be tested.
- kind: metadata_insufficient
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
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['required'])); print(list(s['properties'].keys()))
o=s['properties']['outcomes']['items']; print(o.get('required'), list(o['properties'].keys()))
print(json.dumps(s['properties']['datasets'],indent=0)[:800])
print(json.dumps(s['properties']['provenance'],indent=0)[:1500])
print(json.dumps(s['properties']['findings']['items'],indent=0)[:1200])
"
```

```
["schema_version", "id", "datasets", "paper", "date", "provenance", "outcomes"]
['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
['claim', 'outcome'] ['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'proposed']
{
"description": "Every dataset the attempt used (docs/protocol.md, \"Record the attempt\").",
"type": "array",
"minItems": 1,
"items": {
"description": "A dataset the attempt used: the archive, the dataset's identifier there, the pinned version, and how the paper relates to it.",
"type": "object",
"additionalProperties": false,
"required": [
"archive",
"id",
"version",
"relation"
],
"properties": {
"archive": {
"description": "The archive that holds the dataset, in lower case: dandi, ebrains, openneuro, dryad, zenodo, figshare and so on.",
[... 129 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/kay-2008-01.yaml",
 "content": "schema_version: 3\nid: kay-2008-01\ndatasets:\n- archive: crcns\n  id: vim-1\n  version: unversioned\n  doi: 10.6080/K0QN64NG\n  relation: primary\npaper: doi:10.1038/nature06713\ndate: 2026-11-14\nentry: kay-2008\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-15\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/43548126132\noutcomes:\n- claim: fig3-s1-repeated-120\n  outcome: reproduced\n  notebook: reproduce_kay_2008.ipynb\n  output: claim:fig3-s1-repeated-120\n  measured:\n  - 90.8\n  notes: Under O1 (a) with O5 (a), 109 of 120 S1 images are identified (90.8%, paper 110 of 120),\n    binomial p against chance 1/120 of 2.5e-212; O1 (b) with O5 (a) also gives 109. With the final\n    model over the best initial model's field of view (O5 b) it is 91 of 120 (75.8%) under both\n    readings of O1, outside tolerance, and the best initial models alone give 96. Ten bootstrap fits\n    give 90 under O5 (b). The value holds under the O5 (a) readings, as the criterion allows.\n  deviations:\n  - Each model is fitted once by gradient descent with early stopping; the paper's final parameters\n    are the mean of 100 bootstrap fits (SM 6, \"Estimation of variance\"), not run for time. Ten\n    bootstrap fits, run as a variant under O5 (b), change the result by one image (S1) and three\n    (S2).\n  - One stopping set (20% of the 1,750 responses) is drawn per fit and shared by the voxels fitted\n    together, a standard choice for a random draw (SM 6 draws one per fit).\n  - The initial fields of view are 10.0 and 5.12 degrees, from the paper's resolution list\n    min(500, round(2^(9 - x/8))) (SM 6); the paper states 10.1 and 5.2 degrees (SM 5), which the\n    list does not give.\n  - The Gaussian SD of each wavelet follows from a 1-octave spatial frequency bandwidth (full width\n    at half maximum), which gives an orientation bandwidth of 37 degrees where SM 6 states 41 (O3,\n    standard choice). Wavelet centres at the grid cell centres (O3).\n  - Stimulus values are taken as linear in luminance (O4); the goggles' response is not given.\n  - Stimuli are resampled by area averaging; SM 6 does not say how.\n  - An isotropic Gaussian with a constant offset is fitted to each initial model's envelope at 32 x\n    32; SM 5 says only \"an isotropic two-dimensional Gaussian\".\n  - The significance of predictive power is by 1,000 bootstrap resamples of the 120 image pairs\n    (O2, standard choice).\n  - The responses are the data set's estimated repeated-trial responses, z-scored per voxel by the\n    data set; the paper standardized per session (SM 3). Voxels with NaN responses are left out\n    (S1 345, S2 214 of V1 to V3).\n- claim: fig4a-s2-repeated-120\n  outcome: reproduced\n  notebook: reproduce_kay_2008.ipynb\n  output: claim:fig4a-s2-repeated-120\n  measured:\n  - 72.5\n  notes: Under O1 (a) with O5 (a), 87 of 120 S2 images are identified (72.5%, paper 86); O1 (b) with\n    O5 (a) gives 86 (71.7%). Under O5 (b) it is 56 of 120 (46.7%) for both readings of O1, and 59\n    with ten bootstrap fits; the best initial models alone give 77.\n  deviations:\n  - As fig3-s1-repeated-120 (one fit in place of 100 bootstrap fits, shared stopping set, field of\n    view sizes, wavelet SD, linear luminance, resampling, Gaussian with offset, NaN voxels left out).\n- claim: fig4a-single-trial\n  outcome: blocked\n  blocked_by: too_large\n  notes: The data set holds no single-trial responses, only the raw time series (70 runs) and the\n    repeated-trial estimates. Single-trial amplitudes need the BRS model (SM 3 and 4) fitted to every\n    voxel's time series, first with a Fourier basis per session to get its HRF, then with one\n    amplitude per trial (1,024 trials and 28 polynomial terms on 4,752 time points per session)\n    and first-order autoregressive noise, iterated to convergence; each voxel has its own design\n    after the HRF and the noise transform. The notebook streams one run (2.5 s) and times one\n    single-trial solve at 0.23 s, which gives about 586 minutes for the 10,228 V1 to V3 voxels of\n    both subjects, 5 sessions and 3 iterations, before the HRF fits. This is over the notebook limit\n    and the time left in the run. Nothing was computed on single trials.\n- claim: fig4a-noise-ceiling\n  outcome: blocked\n  blocked_by: too_large\n  notes: Needs the single-trial patterns of fig4a-single-trial, which are blocked as too large.\n- claim: fig4b-set-size-1000\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the paper's 999-image library (SM 7), which the paper does not deposit or name a\n    source for. The data set holds only the 1,750 and 120 images of the experiment (its file list\n    and readme); the paper's text and supplement give no other location.\n- claim: fig4b-extrapolation\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the 999-image library of fig4b-set-size-1000, which is not public.\n- claim: fig4c-retinotopy-only-extrapolation\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the 999-image library of fig4b-set-size-1000, which is not public. The\n    retinotopy-only model itself is tested at set size 120 under suppm8-retinotopy-only-120.\n- claim: suppm8-retinotopy-only-120\n  outcome: reproduced\n  notebook: reproduce_kay_2008.ipynb\n  output: claim:suppm8-retinotopy-only-120\n  measured:\n  - 53.3\n  - 43.8\n  notes: Averaged over subjects, 53.3% with the spatially-weighted metrics (S1 68.3, S2 38.3) and\n    43.8% with the standard metrics (S1 59.2, S2 28.3), candidate voxels under O1 (a); 52.9% and\n    42.5% under O1 (b). Both are within tolerance and below the GWP mean of 81.7% (O1a-O5a) and of\n    61.2% (O5 b readings).\n  deviations:\n  - The contrast channel is read as the square root of the weighted variance (the SM 8 formula is\n    garbled in the text); fitted by the gradient descent of SM 6 with the deviations of\n    fig3-s1-repeated-120.\n- claim: suppfig8-constrained-models\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Judged at set size 1,000 by P6, which needs the 999-image library of fig4b-set-size-1000,\n    not public. The variant at set size 120 that the criterion allows was not run.\n- claim: time-two-months\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The two later S1 sessions (120 new images) are not in the data set; its 93 files hold the\n    five main sessions of each subject only (seqVal lists 10 identification runs and 120 images),\n    and the readme does not mention them. The paper gives no other location.\n- claim: time-fourteen-months\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The single-run S1 session about 14 months later is not in the data set, as for\n    time-two-months.\n- claim: errors-similar-images\n  outcome: reproduced\n  notebook: reproduce_kay_2008.ipynb\n  output: claim:errors-similar-images\n  notes: Under reading (b), local RMS contrast in 0.6 degree blocks, the 44 errors of O1a-O5a pooled\n    over subjects have a median percentile of 68.9 (S1 93.3, S2 64.7), one-sided Wilcoxon p =\n    0.00031. Under reading (a), pixel luminance, the median is 42.4 (p = 0.7). The other\n    identification readings agree (contrast 61.3 to 68.9, p <= 0.00015; luminance p >= 0.7).\n    Random choices give a median percentile of 49.6. The claim holds under one reading, as the\n    criterion allows.\n- claim: suppfig4-500-voxels\n  outcome: blocked\n  blocked_by: too_large\n  notes: Two of its four conditions are single-trial, which are blocked (fig4a-single-trial). For\n    repeated trials (O1a-O5a), performance at 1, 5, 10, 20, 50, 100, 200, 500 and 1,000 voxels is\n    0.8, 7.5, 19.2, 36.7, 61.7, 71.7, 85.8, 90.8 and 90.8% for S1 and 0.8, 6.7, 16.7, 23.3, 45.8,\n    61.7, 73.3, 72.5 and 66.7% for S2, so the rule holds in both repeated-trial conditions (500 is\n    the highest or within 3 points of it, and above 50).\n- claim: supptable1-voxel-counts\n  outcome: reproduced\n  notebook: reproduce_kay_2008.ipynb\n  output: claim:supptable1-voxel-counts\n  measured:\n  - 1331\n  - 2208\n  - 1973\n  - 1513\n  - 1982\n  - 1780\n  notes: The data set's ROI labels give exactly the paper's six counts.\n- claim: supptable1-predictive-power-by-area\n  outcome: reproduced\n  notebook: reproduce_kay_2008.ipynb\n  output: claim:supptable1-predictive-power-by-area\n  measured:\n  - 41.2\n  - 30.2\n  - 18.2\n  - 26.8\n  - 22.6\n  - 13.1\n  notes: All six fractions are within 10% of the paper's and V1 > V2 > V3 in both subjects. The\n    denominators are all voxels labelled in each area; voxels with NaN responses count as not\n    significant. At p < 0.001 and p < 0.05 the order holds as well.\n  deviations:\n  - The initial models carry the fitting deviations of fig3-s1-repeated-120.\n- claim: supptable1-snr\n  outcome: blocked\n  blocked_by: too_large\n  notes: The data set gives no standard errors for its response estimates. Reading (a) needs the\n    repeated-trial BRS fit of every voxel's time series per session, reading (b) a bootstrap over\n    runs of the same fits. The notebook times one repeated-trial solve (0.033 s) and estimates about\n    171 minutes for the V1 to V3 voxels of both subjects with the alternating HRF step and 3\n    iterations, over the time left in the run once the identification pipeline (39 minutes) is in\n    the notebook.\n- claim: methods-v4-poor\n  outcome: reproduced\n  notebook: reproduce_kay_2008.ipynb\n  output: claim:methods-v4-poor\n  notes: V4 voxels with significant predictive power are 17.5% (S1) and 8.6% (S2), below V3 (18.2%\n    and 13.1%) in both subjects; the S1 margin is 0.7 points. Median r in V4 is 0.019 and 0.000,\n    against 0.135 and 0.069 in V1.\n- claim: fig2-representative-voxel\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_kay_2008.ipynb\n  output: claim:fig2-representative-voxel\n  notes: The data set's voxIdx holds 42205 for one S1 voxel, in V1, taken to be the paper's voxel.\n    Its best initial model has r = 0.75 and its Gaussian centre is (-3.89, -0.57) deg. Under O5 (a),\n    the reading adopted, the envelope peaks at (-3.42, +0.24) deg, left of the vertical meridian but\n    0.24 degrees above the horizontal one; the SF tuning is highest at the highest frequency, 2.94\n    cycles/deg; the orientation tuning's max/min is 2.23 without the DC offset and 16.2 with it, so\n    the broadband rule fails. Left hemifield and high-pass hold; just below and broadband do not.\n    Under O5 (b) the peak is at (-4.22, -0.47), SF tuning is highest at the highest frequency (0.80\n    cycles/deg) and the max/min is 1.77 without the DC offset (6.54 with it), so all three parts hold\n    without the DC offset.\n  deviations:\n  - The readings differ in outcome. O5 (a) is adopted as an assumption, as the paper best supports\n    it; its 5.45 degree field of view gives a highest frequency of 2.94 cycles/deg, the end of the\n    spatial frequency axis of Figure 2b (2.9), where the O5 (b) model's ends at 0.80, and only O5\n    (a) reproduces the identification results.\n  - Tuning curves are taken without the DC offset, as an assumption; SM 6 does not say whether the\n    tuning curves include it, and with it the minimum of the orientation curve is near zero, which\n    makes the max/min rule fail under both readings.\n  - The paper does not say how it numbers voxels; voxIdx is assumed to be its numbering.\n- claim: suppfig7-roi-tuning\n  outcome: not_reproduced\n  notebook: reproduce_kay_2008.ipynb\n  output: claim:suppfig7-roi-tuning\n  notes: Over all V1 voxels with a final model (1,084 in S1 and 1,083 in S2), the mean spatial\n    frequency curve rises to the highest level (16 cycles per field of view) under O5 (a) and (b), in\n    both subjects, with or without the DC offset, with gratings over the field of view or inside the\n    stimulus aperture, and for the median over voxels; it is high-pass, not band-pass. The\n    orientation curve's range is 31% to 504% of its mean, against the 10% rule. Under O5 (a) a few\n    voxels with very large responses to full-field gratings dominate the mean (SE up to about 740);\n    gratings inside the aperture remove them (orientation range 42.5% in S1 and 31.4% in S2) without\n    changing the spatial frequency curve's shape. Reading (b) of the models (model I of the\n    constrained models) and reading (b) of the voxels were not run.\n  deviations:\n  - The curves are averaged over each model's five spatial frequency levels in cycles per field of\n    view, as the fields of view differ between voxels; the paper does not say how the curves of\n    voxels with different fields of view are combined.\n  - Grating amplitude 0.5, a standard choice that scales but does not shape the curves.\n- claim: suppfig10-retinotopy-validation\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The multifocal retinotopic mapping scans are not in the data set; its readme says the\n    localizer scans behind the ROIs are not included, and its file list holds none. The paper gives\n    no other location.\n- claim: suppfig11-rf-size-eccentricity\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_kay_2008.ipynb\n  output: claim:suppfig11-rf-size-eccentricity\n  notes: With RFs inside the 20 degree square (V1 732, V2 829, V3 342 voxels over both subjects), RF\n    size increases with eccentricity in each area (Spearman rho 0.535, 0.628 and 0.649, p < 1e-40),\n    and in 1 degree bins the medians order V1 < V2 < V3 in 5 of the 8 bins shared by the three\n    areas. With RFs inside the circular aperture the correlations hold (rho 0.573 to 0.676) and the\n    order holds in 3 of 6 bins, not most; with 0.5 degree bins it holds in 6 of 12 (square) and 3 of\n    9 (circle).\n  deviations:\n  - The legend's \"estimated RF location was not completely within the stimulus bounds\" is read as\n    the +/-2 SD square inside the 20 x 20 degree stimulus square, as an assumption; the paper gives\n    the stimulus size as 20 x 20 degrees and uses square fields of view. Inside the circular aperture\n    the bin order fails.\n- claim: suppdisc1-classification-extension\n  outcome: not_reproduced\n  notebook: reproduce_kay_2008.ipynb\n  output: claim:suppdisc1-classification-extension\n  notes: The luminance metric is not above chance under any reading (0 to 3 of 120, p >= 0.08), as\n    in the paper. The contrast metric is above chance at p < 0.0001 only for S1 with the 500 voxels\n    of P5 and the SD measure (9 of 120, p = 8.8e-07, paper 6); for S2 it is 1 or 2 of 120 (p >= 0.26)\n    under every reading, against 7 in the paper. No reading gives the paper's significance pattern.\n  deviations:\n  - For the relative contrast reading, stimulus values are shifted to start at 0, as the absolute\n    luminance is not given. Image similarity uses the full 500 px images, blocks of 15 px (0.6\n    degrees).\n- claim: suppm7-selected-voxels-v1\n  outcome: not_reproduced\n  notebook: reproduce_kay_2008.ipynb\n  output: claim:suppm7-selected-voxels-v1\n  notes: Under O1a-O5a, 48% of the selected voxels lie in V1 in both subjects under both readings of\n    the selection (V2 41 to 42%, V3 10 to 11%); O1b-O5a gives the same, and the O5 (b) readings give\n    42 to 43%. V1 holds the largest share but not more than half.\nfindings:\n- kind: data_missing\n  statement: The data set holds the two subjects' five main sessions only. The two later S1 sessions\n    and the session about 14 months later, the 999-image library of the set-size analyses, and the\n    multifocal retinotopic mapping scans are not in it (the readme says the localizer scans are not\n    included). Eight of the paper's findings cannot be tested for this reason.\n- kind: metadata_insufficient\n  statement: The data set gives the repeated-trial response estimates without their standard errors\n    and holds no single-trial estimates, so the SNR of Supplementary Table 1 and the single-trial\n    results of Figure 4a can be had only by refitting the BRS model to every voxel's time series.\n- kind: metadata_error\n  statement: The readme says the .mat files are MATLAB 7.3 (HDF5) files readable with PyTables;\n    Stimuli.mat and mask.mat are MATLAB 5 files, which h5py and PyTables cannot open. It gives\n    Stimuli_Trn_FullRes_15.mat as 70 x 120 x 120; it holds 70 images of 500 x 500.\n- kind: metadata_insufficient\n  statement: 345 V1 to V3 voxels of S1 and 214 of S2 (and 15 S1 V4 voxels) have NaN responses in\n    EstimatedResponses.mat; the readme does not mention them or say why.\n- kind: metadata_insufficient\n  statement: The readme does not say whether voxIdx is 0-based or 1-based in the 64 x 64 x 18 volume,\n    or how it relates to the paper's voxel numbers (Figure 2 names voxel 42205, which voxIdx holds\n    for one S1 V1 voxel).\n- kind: metadata_error\n  statement: The NIfTI headers of the time series give a TR of 0 (pixdim[4]); the TR of 1 s is only in\n    the paper.\n- kind: methods_unavailable\n  statement: The final model's field of view is \"specifically tailored to the estimated RF\n    location\" (SM 5), with no rule given. Identification depends on it here; with the square of\n    +/-2 SD of the fitted Gaussian the paper's 92% and 72% are reproduced (90.8% and 72.5%), with\n    the best initial model's field of view the result is 75.8% and 46.7%. Which rule, and at which\n    of the 25 resolutions, did the paper use?\n- kind: methods_unavailable\n  statement: SM 6 does not say whether the grating tuning curves include the DC offset, whether the\n    gratings were restricted to the stimulus aperture, or how ROI-averaged curves combine voxels\n    whose fields of view, and so whose spatial frequencies in cycles per degree, differ. Here the V1\n    average is high-pass under every choice tried, where Supplementary Figure 7 shows it band-pass.\n- kind: methods_unavailable\n  statement: Supplementary Figure 11 omits voxels whose RF was \"not completely within the stimulus\n    bounds\"; whether the bounds are the 20 degree square or the circular aperture changes whether\n    V1 < V2 < V3 holds in most eccentricity bins here.\n- kind: paper_inconsistency\n  about: paper\n  statement: SM 5 gives the initial fields of view as 10.1 and 5.2 degrees, but at 128 px the\n    resolution list of SM 6 gives 10.0 (256 px) and 5.12 (500 px) degrees; and a 1-octave bandwidth\n    with an isotropic Gaussian gives an orientation bandwidth of about 37 degrees, not the 41 stated.\n"
}
```

```
File created successfully at: attempts/kay-2008-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sed -i 's/included). Eight of the paper/included). Seven of the paper/' attempts/kay-2008-01.yaml && cat > entries/kay-2008/README.md <<'EOF'
# Kay, Naselaris, Prenger & Gallant (2008) from CRCNS vim-1

Tests the findings of [Kay et al. (2008)](https://doi.org/10.1038/nature06713) that can be tested on
CRCNS [vim-1](http://crcns.org/data-sets/vc/vim-1) (doi:10.6080/K0QN64NG), which holds the estimated
fMRI responses of two subjects to 1,750 model estimation images and 120 identification images, ROI
labels, the stimuli and the raw time series. The 999-image library of the set-size analyses, the
later sessions of subject S1 and the retinotopic mapping scans are not in it.

| Claim | Outcome |
|---|---|
| S1 identifies 92% of 120 images (Figure 3) | Reproduced (90.8%) |
| S2 identifies 72% of 120 images (Figure 4a) | Reproduced (72.5%) |
| Retinotopy-only model, 55% and 42% at 120 images | Reproduced |
| Errors fall on visually similar images | Reproduced (local contrast reading) |
| Voxel counts per area (Supplementary Table 1) | Reproduced |
| Predictive power falls from V1 to V2 to V3 | Reproduced |
| The model does poorly in V4 | Reproduced |
| RF size grows with eccentricity and from V1 to V3 | Reproduced (assumed) |
| Representative voxel 42205 (Figure 2) | Partially reproduced (assumed) |
| V1-averaged tuning curves (Supplementary Figure 7) | Not reproduced |
| Classification extension (Supplementary Discussion 1) | Not reproduced |
| Most selected voxels lie in V1 | Not reproduced |
| Single-trial identification, noise ceiling, voxel-number curve, SNR | Blocked: too large |
| Set sizes up to 1,000 and beyond, retinotopy-only extrapolation, constrained models | Blocked: data missing |
| Later sessions (two and fourteen months), retinotopic validation | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The identification results hold only when the final receptive-field model covers the square of
+/-2 SD of the fitted Gaussian; over the best initial model's field of view they are much lower. The
paper does not say which it used. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/kay-2008-01.yaml`](../../attempts/kay-2008-01.yaml).

- `reproduce_kay_2008.ipynb`: the analysis. It takes about 40 minutes, most of it fitting one final
  model per voxel.
- `vim1.py`: loading the files, the Gabor wavelet pyramid, the gradient descent fits, identification
  and the retinotopy-only model. Other notebooks on this data set can import it.
EOF
python tools/entry.py check entries/kay-2008 2>&1 | tail -10; date -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u && python tools/entry.py all entries/kay-2008 2>&1 | tail -3; date -u
```

```
Sat Nov 14 04:47:01 UTC 2026
Installed kernelspec registry-kay-2008 in executed/kay-2008/.venv/share/jupyter/kernels/registry-kay-2008
0 error(s)
pass  reproduce_kay_2008.ipynb  (2333 s)
Sat Nov 14 05:26:02 UTC 2026
```

**Agent**

Final run passed (39 min). Checking that the executed numbers match every conclusion.

**Agent calls Bash**

```bash
cd $TMPDIR && . kenv/bin/activate && python -c "
import nbformat
nb=nbformat.read('executed/kay-2008/reproduce_kay_2008.ipynb',4)
for i,c in enumerate(nb.cells):
  if c.cell_type!='code': continue
  for o in c.outputs:
    if o.output_type=='stream': print(o.text[-1800:])
    if o.output_type=='error': print('ERR')
  print('-----',i)
" | grep -v RuntimeWarning | grep -v "return (a\|r = p @" | sed -n '/S1: initial/,$p' | grep -v "^   initial" | head -150
```

```
S1: initial models 75 s, final (b) 11 s for 4135 voxels, final (a) 844 s for 4135 voxels (0.20 s each); peak memory 8.1 GB
   best initial model: {'20': 3306, '10': 950, '5': 1032} ; voxels with none: 1414

S2: initial models 62 s, final (b) 6 s for 3770 voxels, final (a) 758 s for 3770 voxels (0.20 s each); peak memory 8.4 GB
   best initial model: {'20': 2906, '10': 729, '5': 829} ; voxels with none: 1619

----- 7
S1: median r over 1084 V1 voxels, image order 0.215; permuted orders -0.024 to 0.046
S2: median r over 1083 V1 voxels, image order 0.140; permuted orders -0.035 to 0.025

----- 9
S1 O1a-O5a: 109/120 = 90.8% correct (candidate voxels 1574; binomial p against chance 1/120 = 2.5e-212)

S1 O1a-O5b: 91/120 = 75.8% correct (candidate voxels 1574; binomial p against chance 1/120 = 2.7e-162)

S1 O1b-O5a: 109/120 = 90.8% correct (candidate voxels 4135; binomial p against chance 1/120 = 2.5e-212)

S1 O1b-O5b: 91/120 = 75.8% correct (candidate voxels 4135; binomial p against chance 1/120 = 2.7e-162)

S1 best initial models only (O1 a): 96/120
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/(2.5 s) and times one\b/(2.7 s) and times one/; s/single-trial solve at 0.23 s, which gives about 586 minutes/single-trial solve at 0.24 s, which gives about 615 minutes/; s/repeated-trial solve (0.033 s) and estimates about/repeated-trial solve (0.032 s) and estimates about/; s/    171 minutes for the V1/    164 minutes for the V1/; s/range is 31% to 504% of its mean/range is 31% to 449% of its mean/' attempts/kay-2008-01.yaml && grep -n "615\|164 min\|449\|2.7 s\|0.032" attempts/kay-2008-01.yaml; grep -n "single-trial solve\|171\|586\|504" attempts/kay-2008-01.yaml
```

```
77:    after the HRF and the noise transform. The notebook streams one run (2.7 s) and times one
78:    single-trial solve at 0.24 s, which gives about 615 minutes for the 10,228 V1 to V3 voxels of
182:    runs of the same fits. The notebook times one repeated-trial solve (0.032 s) and estimates about
183:    164 minutes for the V1 to V3 voxels of both subjects with the alternating HRF step and 3
224:    orientation curve's range is 31% to 449% of its mean, against the 10% rule. Under O5 (a) a few
78:    single-trial solve at 0.24 s, which gives about 615 minutes for the 10,228 V1 to V3 voxels of
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/kay-2008 2>&1 | tail -3 && python tools/entry.py handover entries/kay-2008 2>&1 | tail -5; ls executed/kay-2008/handover/; git status --short; date -u
```

```
0 error(s)
wrote executed/kay-2008/handover
kay-2008.yaml
reproduce_kay_2008.ipynb
vim1.py
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
?? attempts/kay-2008-01.yaml
?? entries/kay-2008/
?? scripts
Sat Nov 14 05:26:30 UTC 2026
```

**Agent**

The attempt on Kay et al. (2008) is finished: 12 claims tested, 11 blocked. The entry passes `check` and a clean `run` (39 minutes, peak memory 8.6 GB), and the handover package was built. No verification of my own was done.

**1. Outcome per claim**

| Claim | Outcome |
|---|---|
| fig3-s1-repeated-120 | reproduced: 109/120 (90.8%), paper 110 |
| fig4a-s2-repeated-120 | reproduced: 87/120 (72.5%), paper 86 |
| suppm8-retinotopy-only-120 | reproduced: 53.3% and 43.8% (paper 55 and 42), both below the main model |
| errors-similar-images | reproduced with the local-contrast similarity (p = 0.00031); not with pixel luminance |
| supptable1-voxel-counts | reproduced: all six counts are exact |
| supptable1-predictive-power-by-area | reproduced: 6 of 6 within tolerance, V1 > V2 > V3 |
| methods-v4-poor | reproduced (the S1 margin is 0.7 points) |
| suppfig11-rf-size-eccentricity | reproduced, resting on an assumption |
| fig2-representative-voxel | partially reproduced, resting on an assumption |
| suppfig7-roi-tuning | not reproduced: the V1 spatial-frequency curve rises to the highest frequency in every variant, so it is not band-pass |
| suppdisc1-classification-extension | not reproduced: S2's contrast result is never above chance |
| suppm7-selected-voxels-v1 | not reproduced: 48% of selected voxels are in V1, not more than half |
| fig4a-single-trial, fig4a-noise-ceiling, suppfig4-500-voxels | blocked, `too_large`: refitting every voxel's time series is estimated at about 615 min |
| supptable1-snr | blocked, `too_large`: estimated about 164 min |
| fig4b-set-size-1000, fig4b-extrapolation, fig4c, suppfig8, time-two-months, time-fourteen-months, suppfig10 | blocked, `data_missing` |

**2. Dataset, assumptions, questions**

- **Choice of reading:** The identification results depend on the final model's field of view. With the ±2 SD square of the fitted Gaussian (O5 a), both subjects reproduce. With the best initial model's field of view (O5 b), the result is 75.8% and 46.7%.
- **Version:** CRCNS data sets are not versioned, so I recorded it as `unversioned` with doi:10.6080/K0QN64NG, and put the MD5 sums from the bucket in the notebook.
- **What the data set lacks:** single-trial responses, standard errors of the estimates, S1's later sessions, the 999-image library, and the retinotopic mapping scans.
- **Readme errors:** it calls `Stimuli.mat` and `mask.mat` MATLAB 7.3 files, but they are MATLAB 5. It gives `Stimuli_Trn_FullRes_15.mat` as 70×120×120, but it holds 70 images of 500×500.
- **Undocumented:** 345 (S1) and 214 (S2) V1 to V3 voxels have NaN responses; the readme does not say whether `voxIdx` is 0- or 1-based; the NIfTI headers give a TR of 0.
- **Assumptions:**
  - fig2: I adopted O5 (a), because its field of view puts the highest frequency at 2.94 cycles/deg, matching the 2.9 on Figure 2b's axis. Tuning curves are taken without the DC offset. I also assumed `voxIdx` 42205 is the paper's voxel 42205.
  - suppfig11: "within the stimulus bounds" is read as the 20° square.
  - A standard wavelet SD, stimulus values linear in luminance, a Gaussian fit with an offset, and area-averaging resampling.
- **Deviations:** one fit per model instead of the mean of 100 bootstrap fits (a 10-bootstrap variant changed results by at most 3 images), and one stopping set shared by the voxels fitted together.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings): the rule for the final model's field of view; how tuning curves are computed (DC offset, aperture, how voxels with different fields of view are combined); and square or circle for "stimulus bounds". There is also one `paper_inconsistency` finding: the stated 10.1°/5.2° fields of view and 41° orientation bandwidth do not follow from the paper's own resolution list and 1-octave bandwidth.
- **Questions to a reader:** none.

**3. Where the protocol was unclear or did not fit**

1. Running every reading versus time: the claims file asks for every O1×O5 combination. One combination roughly doubled the runtime (21 to 39 min), which is over the 10-minute aim but under the 60-minute limit. I ran it anyway.
2. A claim that depends on a blocked claim is blocked, even when part of it can be tested. suppfig4 holds in both repeated-trial conditions but is recorded as blocked, with those numbers in its notes.
3. `too_large` estimates need numbers, but numbers from analyses outside the notebook may not enter the record. I put small timing cells in the notebook so the estimates come from it.
4. A "standard choice" that should not change the outcome did change it: whether tuning curves include the DC offset decides fig2. I treated it as an assumption.
5. archives.md says to open zips with fsspec, but vim-1 has no zips: plain `.mat` files (mixed MATLAB 5 and 7.3) and gzipped NIfTI. I streamed each whole file into memory. The NIfTI files cannot be range-read, so each was read whole into memory and decompressed, never written to disk.
6. The data-check step's requirement that every stream shares the trial table's clock does not fit per-image estimates. I used predictive power with the image order shuffled as the contrast.

**4. Runtime and failures**

The run used about 2 h 40 min of the 5 h. The notebook took 39 min per full run, and the entry was executed three times. Nothing failed. `git status` shows untracked dotfiles (`.bashrc`, `.idea`, `.mcp.json` and others) and a `scripts/` folder that I did not create; they should be kept out of the commit.

## End of run

64 turns, 154 minutes, $6.13 at API prices, result: success.
