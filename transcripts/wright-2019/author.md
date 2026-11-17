# wright-2019 · author · run 43001997692

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls paper entries claims attempts | head -50
```

```
<persisted-output>
Output too large (39.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b18d9502-3789-4423-8284-71166547054b/tool-results/bc74c92jc.txt

Preview (first 2KB):
Wed Nov 11 10:19:22 UTC 2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/b18d9502-3789-4423-8284-71166547054b/tool-results/bc74c92jc.txt"
}
```

```
1	Wed Nov 11 10:19:22 UTC 2026
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
[... 713 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper; cat claims/wright-2019.yaml; ls entries/fouke-2025; cat papers/datasets/wright-2019.yaml; ls questions | grep wright; ls attempts | grep wright; ls entries | grep wright
```

```
<persisted-output>
Output too large (61.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b18d9502-3789-4423-8284-71166547054b/tool-results/b3qw7kyvv.txt

Preview (first 2KB):
10.7554-elife.45013.txt
pag-1.data-description.txt
# Claims for Wright & McDannald (2019), eLife 8:e45013, "Ventrolateral periaqueductal gray neurons
# prioritize threat probability over fear output", on CRCNS data set pag-1.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
# protocol as stated in docs/protocol.md (Reader, version pilot-14).
#
# Text read: the version of record, PMC6435320 (open access), from the Europe PMC full-text JATS
# XML as supplied under paper/ (10.7554-elife.45013.txt): main text, Materials and methods, the
# legends of Figures 1 to 6 and of all figure supplements (Figure 1, supplements 1 to 6; Figure 2,
# supplements 1 and 2; Figure 5, supplements 1 and 2), and the example regression input table of
# the Methods. The paper has no other supplement. No PDF was supplied, so the values printed only
# inside figures (the R2 and sign-test p-values of Figure 4, the F values of Figure 5, supplement
# 1, the tuning curves of Figure 5E and 5J) could not be read; the claims on them are judged on
# the tests the legends name.
#
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/CRCNS/,/^## [A-Z]/p' docs/archives.md | head -120
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
[... 8 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/b18d9502-3789-4423-8284-71166547054b/tool-results/b3qw7kyvv.txt"
}
```

```
1	10.7554-elife.45013.txt
2	pag-1.data-description.txt
3	# Claims for Wright & McDannald (2019), eLife 8:e45013, "Ventrolateral periaqueductal gray neurons
4	# prioritize threat probability over fear output", on CRCNS data set pag-1.
5	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
6	# protocol as stated in docs/protocol.md (Reader, version pilot-14).
7	#
8	# Text read: the version of record, PMC6435320 (open access), from the Europe PMC full-text JATS
9	# XML as supplied under paper/ (10.7554-elife.45013.txt): main text, Materials and methods, the
10	# legends of Figures 1 to 6 and of all figure supplements (Figure 1, supplements 1 to 6; Figure 2,
11	# supplements 1 and 2; Figure 5, supplements 1 and 2), and the example regression input table of
12	# the Methods. The paper has no other supplement. No PDF was supplied, so the values printed only
13	# inside figures (the R2 and sign-test p-values of Figure 4, the F values of Figure 5, supplement
14	# 1, the tuning curves of Figure 5E and 5J) could not be read; the claims on them are judged on
15	# the tests the legends name.
16	#
17	# Code. The paper links one source of code, the lab website ("Med Associates programs used for
18	# behavior and MATLAB programs used for behavioral analyses are made freely available at our lab
19	# website, http://mcdannaldlab.org/resources"). On 2026-11-10 that address returned 404, and the
20	# only Internet Archive capture (2020-10-25) of the page holds no files or links. No code was
[... 1049 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/pag-1.data-description.txt; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent**

Read the protocol, claims (about 40 claims) and data description. Now listing the bucket.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=pag-1/" | python3 -c "
import sys,re
t=sys.stdin.read()
for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',t): print(s,k)
print('trunc', re.findall(r'<IsTruncated>(.*?)<',t))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
B=https://crcnsarchive.s3-us-west-2.amazonaws.com/pag-1/live; curl -s $B/checksums.md5; curl -s $B/filelist.txt; python3 -c "import fsspec,zipfile" && echo ok; ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in
```

```
5437f01d5071fe55a1baedbb146f56e0  data.zip
0ac5a035f0c0521ccefcb410862e8792  docs/crcns_pag-1_data_description.docx
9ac2531d1605bc085e2fef87b446c6cb  docs/crcns_pag-1_data_description.pdf
a45c303f4e9c12949c149fe2d9e16601  filelist.txt
# CRCNS.org 'pag-1' dataset files
# To use this for fetching files, comment out files that are
# not needed by putting a '#' as the first character on the line (default mode)
# or put a '+' as the first character to specifiy files to be fetched (+ mode).
# mode='default' (change to '+' for + mode).
 data.zip	83639372 (79.7 MB)
 docs/crcns_pag-1_data_description.docx	32409 (31.6 KB)
 docs/crcns_pag-1_data_description.pdf	109269 (106.7 KB)
 checksums.md5	235
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fsspec,zipfile
ModuleNotFoundError: No module named 'fsspec'
README.md
entry.yaml
omr.py
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q wv && . wv/bin/activate && uv pip install -q fsspec aiohttp requests scipy numpy pandas statsmodels h5py matplotlib nbformat nbclient ipykernel 2>&1 | tail -2; python -c "
import fsspec,zipfile
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/pag-1/live/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
for i in z.infolist(): print(i.file_size,i.compress_size,i.filename)
" | head -300 | awk 'NR<40 || /cube|\.m$|Script|script/' | head -80
```

```
0 0 data/
223138 11388 data/cue3.wav
223242 10313 data/cue2.wav
223272 10970 data/cue1.wav
14595 3139 data/cubeScript.m
0 0 data/mFiles/
351126 350495 data/mFiles/dr01101616epr38aSPK14a.mat
570783 569576 data/mFiles/rf02102116epr38bSPK13a.mat
19336 19081 data/mFiles/rf03101216epr38bSPK11a.mat
932701 930453 data/mFiles/dr01101116epr38aSPK04a.mat
32894 32611 data/mFiles/rf03101216epr38bSPK07a.mat
138001 137673 data/mFiles/rf02101416epr38bSPK12c.mat
141038 140747 data/mFiles/dr01102016epr38aSPK08a.mat
675448 673965 data/mFiles/dr01092216epr38aSPK14a.mat
270529 270025 data/mFiles/rf02092116epr38bSPK09a.mat
205631 205226 data/mFiles/dr01101616epr38aSPK14b.mat
373953 373251 data/mFiles/rf02100916epr38bSPK05b.mat
584854 583548 data/mFiles/dr01110116epr38aSPK11a.mat
48781 48511 data/mFiles/rf03101716epr38bSPK11a.mat
19188 18931 data/mFiles/dr02092216epr38aSPK07a.mat
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . wv/bin/activate && python -c "
import fsspec,zipfile,io
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/pag-1/live/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
names=[i.filename for i in z.infolist()]
print(len([n for n in names if n.startswith('data/mFiles/') and n.endswith('.mat')]))
print([n for n in names if not n.startswith('data/mFiles/')])
open('cubeScript.m','wb').write(z.read('data/cubeScript.m'))
open('analysisScript.m','wb').write(z.read('data/analysisScript.m'))
"; cat cubeScript.m
```

```
245
['data/', 'data/cue3.wav', 'data/cue2.wav', 'data/cue1.wav', 'data/cubeScript.m', 'data/analysisScript.m', 'data/cubeFile/', 'data/cubeFile/cube.mat']
% Written by: Mike McDannald 12/11/2017                     
% Organize single units into 3-D data structures

clear all; %#ok<CLALL>
tic;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Open file to be analyzed %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%

fileList = dir('C:\Users\user1\data'); % location of folder with .mat files
fileList = fileList(~[fileList.isdir]); % ignore folders 
numfiles = numel(fileList); % count # of files

for ii = 1:numfiles % perform for each file
    
load(['C:\Users\user1\data\',fileList(ii).name]);

[... 446 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat analysisScript.m
```

```
tic

close all;

load(['C:\Users\mcdannal\Dropbox (McDannald Lab)\Manuscripts\Wright\vlpag record excite\CRCNS\cubeFile\','cube']); % point to folder containing 'cube' file

for ii = 1:size(vlPAGcube.tag,3)
   
   % Determine significance (h) and direction (d) of firing compared to baseline for cue100 trials 
    
   h = ttest(vlPAGcube.fire.raw.base2(1:6,1,ii),vlPAGcube.fire.raw.select.cueOnset(1:6,1,ii),'Alpha',0.05); % find significance
   d = sign((mean(vlPAGcube.fire.raw.select.cueOnset(1:6,1,ii)) - mean(vlPAGcube.fire.raw.base2(1:6,1,ii)))); % find direction
   vlPAGcube.fire.raw.select.dirSig(1,1,ii) = h*d; % multiply to find danger-excited vs. danger-inhibited neurons
   clear h d;
   
   if vlPAGcube.fire.raw.select.dirSig(1,1,ii) == 1 % select only danger-excited neurons and make a cube (exactly as was done for all neurons)
    
        dExc.tag(:,:,ii) = vlPAGcube.tag(:,:,ii);
        dExc.name(:,:,ii) = vlPAGcube.name(:,:,ii);
        dExc.poke.base(:,:,ii) = vlPAGcube.poke.base(:,:,ii);
[... 434 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . wv/bin/activate && python -c "
import fsspec,zipfile,io,scipy.io as sio, numpy as np
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/pag-1/live/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
b=z.read('data/mFiles/rf03101216epr38bSPK11a.mat')
print(b[:120])
m=sio.loadmat(io.BytesIO(b))
for k,v in m.items():
  if k.startswith('__'): continue
  print(k, type(v), getattr(v,'shape',None), getattr(v,'dtype',None), v.ravel()[:5] if hasattr(v,'ravel') and v.size<1e7 else '')
"
```

```
b'MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Sat Feb 17 16:25:23 2018                                        \x00\x00\x00\x00'
EVT01 <class 'numpy.ndarray'> (12, 1) float64 [1479.423375 1806.444075 2103.464725 3578.057875 3935.07865 ]
EVT02 <class 'numpy.ndarray'> (27, 1) float64 [1324.82305  1491.473425 1608.653675 1614.803675 1970.91445 ]
EVT08 <class 'numpy.ndarray'> (12, 1) float64 [1479.423375 1806.444075 2103.464725 3578.057875 3935.07865 ]
EVT09 <class 'numpy.ndarray'> (16, 1) float64 [1294.912975 1467.42335  2763.506125 2906.016425 3393.547475]
EVT11 <class 'numpy.ndarray'> (6, 1) float64 [1794.444025 2091.4647   3923.078625 4117.58905  4396.609675]
EVT12 <class 'numpy.ndarray'> (10, 1) float64 [1611.933675 1958.9544   2285.9751   2448.48545  2610.9958  ]
EVT13 <class 'numpy.ndarray'> (715, 1) float64 [1281.73295  1283.28295  1284.56295  1288.812975 1290.402975]
EVT14 <class 'numpy.ndarray'> (32, 1) float64 [1326.41305  1500.923425 1643.43375  1827.944125 1990.454475]
filename <class 'numpy.ndarray'> (1,) <U16 ['rf03101216epr38b']
neuron <class 'numpy.ndarray'> (1,) <U6 ['SPK11a']
spike <class 'numpy.ndarray'> (2383, 1) float64 [1275.360625 1291.386225 1291.5193   1291.7245   1292.0298  ]
wave <class 'numpy.ndarray'> (32, 1) float64 [0.0030474  0.00342852 0.00374638 0.00495453 0.00911916]
Shell cwd was reset to
```

**Agent**

Each of the 245 .mat files holds raw spike times, event timestamps and the mean waveform, so every claim can be computed from the raw data. Now reading the paper's Methods.

**Agent calls Bash**

```bash
grep -n -i "^#\|materials and methods\|suppression ratio\|z-score\|k-means\|cessation" paper/10.7554-elife.45013.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^## \|^### " paper/10.7554-elife.45013.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 557,620p paper/10.7554-elife.45013.txt; sed -n 1060,1125p paper/10.7554-elife.45013.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; sed -n 1,80p entries/fouke-2025/omr.py; python3 -c "import json;nb=json.load(open('entries/fouke-2025/reproduce_fouke_2025.ipynb'));print(len(nb['cells']));[print(c['cell_type'],c['metadata'],c['source'][:3]) for c in nb['cells'][:8]]"
```

```
Wed Nov 11 10:21:04 UTC 2026
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
  smoothing of positions (21 frames, order 2); rejection of trials whose absolute cumulative
  heading change exceeds 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or
  whose mean speed exceeds 100 mm/s; measures from 3 s to 35 s after the first tracked frame;
  10 pixels per mm (the code divides pixels per second by 10 to give mm/s); per fish the median
  over trials. The 3 s stationary phase and the 32 s of motion are in the Methods.
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/wright-2019 && cat > entries/wright-2019/pag.py <<'EOF'
"""Loading and measures for CRCNS data set pag-1 (Wright and McDannald 2019, eLife 8:e45013).

The data set is one zip, ``pag-1/live/data.zip``, in the public bucket crcnsarchive. It is
opened in place over HTTP range requests (fsspec and zipfile); nothing is written to disk.
Each of its 245 ``data/mFiles/*.mat`` files holds one unit: the spike times (``spike``, s),
the Plexon event channels of its session (``EVT01`` foot shock, ``EVT02`` pellet, ``EVT09``,
``EVT11`` and ``EVT12`` the three cues, ``EVT13`` nose poke, as listed in the data set's
``cubeScript.m``), the mean waveform (``wave``, 32 points over 0.8 ms), and the session name
(``filename``: rat, date mmddyy, behaviour program ``epr38a/b/c``) and unit name (``neuron``).
The program letter fixes which channel is danger, uncertainty and safety (cubeScript.m).

Where the parameters come from:

- Trial types, cue length (10 s), shock 2 s after cue offset (12 s after onset), 0.5 s long,
  the 32 trials per session: the paper, Materials and methods, Fear discrimination.
- Uncertainty shock and omission trials are told apart by a shock within 30 s of the cue onset,
  as in cubeScript.m (the data set's own script).
- Firing: counts in half-open bins (t0, t1], as cubeScript.m counts them. Raw rate in spikes/s.
- Interval Z firing (Methods, Z-score normalization, paragraph 2): per trial, firing in the
  interval minus the baseline, Z-scored over the 32 trials of the session. The baseline is the
  trial's own 2 s before onset (reading a of detail 4 of the claims file) or the trial type's
  mean 2 s baseline (reading b).
- 100 ms population firing (Methods, Z-score normalization, paragraph 1): per trial type, mean
  rate in 100 ms bins from 10 s before onset to 12 s after offset (320 bins), minus the trial
  type's mean 2 s baseline, Z-scored over all trial types and bins of the neuron.
- Suppression ratio (Methods, Calculating suppression ratios): (baseline rate - cue rate) /
  (baseline rate + cue rate), per trial. The baseline window is open (detail 1 of the claims
  file): 2 s or 10 s (the claims file's readings), or 20 s, the window of the data set's
  cubeScript.m, which the values of the Methods regression table also imply. A 0/0 ratio is
  open (detail 2): 0, left out (NaN), or 1 as cubeScript.m sets it.
"""

from __future__ import annotations

import io
import zipfile

import fsspec
import numpy as np
import scipy.io as sio

URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pag-1/live/data.zip"
CHECKSUMS_URL = "https://crcnsarchive.s3-us-west-2.amazonaws.com/pag-1/live/checksums.md5"

# cubeScript.m: event channel of each cue for behaviour programs a, b and c
CUE_CHANNELS = {
    "a": {"danger": "EVT09", "uncertainty": "EVT12", "safety": "EVT11"},
    "b": {"danger": "EVT11", "uncertainty": "EVT09", "safety": "EVT12"},
    "c": {"danger": "EVT12", "uncertainty": "EVT11", "safety": "EVT09"},
}
# trial types in the data description's row order: danger, uncertainty shock, uncertainty
# omission, safety (rows 1-6, 7-12, 13-22, 23-32)
TYPES = ("D", "US", "UO", "S")
PROB = {"D": 1.0, "US": 0.375, "UO": 0.375, "S": 0.0}
CUE_S = 10.0
SHOCK_ONSET_S = 12.0   # 2 s after cue offset
SHOCK_LEN_S = 0.5


def open_zip():
    f = fsspec.open(URL, block_size=2**20).open()
    return zipfile.ZipFile(f)


def checksums() -> dict:
    with fsspec.open(CHECKSUMS_URL, "rt") as f:
        return {line.split()[1]: line.split()[0] for line in f if line.strip()}


def _arr(m, key):
    return np.asarray(m[key], dtype=float).ravel() if key in m else np.zeros(0)


def load_units() -> list[dict]:
    """Every unit of the data set: spikes, the session's events and trials, and the waveform."""
    z = open_zip()
    names = sorted(n for n in z.namelist() if n.startswith("data/mFiles/") and n.endswith(".mat"))
    units = []
    for n in names:
        m = sio.loadmat(io.BytesIO(z.read(n)))
        session = str(m["filename"][0])
        program = session[15]
        ch = CUE_CHANNELS[program]
        shock = _arr(m, "EVT01")
        onsets, types = [], []
        for cue, chan in ch.items():
            for t in _arr(m, chan):
                if cue == "danger":
                    ty = "D"
                elif cue == "safety":
                    ty = "S"
                else:
                    ty = "US" if np.any((shock > t) & (shock <= t + 30)) else "UO"
                onsets.append(t)
                types.append(ty)
        onsets, types = np.array(onsets), np.array(types)
        # order trials by type (data description order), chronological within type
        key = np.array([TYPES.index(t) for t in types]) * 1e7 + onsets
        o = np.argsort(key)
        units.append(dict(
            file=n.split("/")[-1], session=session, rat=session[:4], program=program,
            unit=str(m["neuron"][0]), spikes=np.sort(_arr(m, "spike")),
            spikes_sorted=bool(np.all(np.diff(_arr(m, "spike")) >= 0)),
            onsets=onsets[o], types=types[o], shock=shock, pokes=_arr(m, "EVT13"),
            pellets=_arr(m, "EVT02"), wave=_arr(m, "wave"),
            channels=sorted(k for k in m if k.startswith("EVT")),
        ))
    return units


def counts(times: np.ndarray, onsets: np.ndarray, start: float, stop: float, width: float):
    """Counts in half-open bins (t0, t1] from onset+start to onset+stop, trials x bins."""
    nb = int(round((stop - start) / width))
    edges = start + width * np.arange(nb + 1)
    out = np.empty((len(onsets), nb))
    for i, t in enumerate(onsets):
        idx = np.searchsorted(times, t + edges, side="right")
        out[i] = np.diff(idx)
    return out


def interval_rate(u: dict, a: float, b: float, times_key: str = "spikes") -> np.ndarray:
    """Rate (events/s) in (onset+a, onset+b] for each of the 32 trials."""
    return counts(u[times_key], u["onsets"], a, b, b - a)[:, 0] / (b - a)


def zscore(x: np.ndarray) -> np.ndarray:
    """Z-score with the sample SD (MATLAB zscore); a constant vector gives zeros."""
    sd = np.std(x, ddof=1)
    return (x - np.mean(x)) / sd if sd > 0 else np.zeros_like(x)


def interval_z(u: dict, a: float, b: float, baseline: str = "trial") -> np.ndarray:
    """Interval Z firing over the 32 trials (Methods, Z-score normalization, paragraph 2).

    baseline "trial": the trial's own 2 s pre-cue rate (reading a of detail 4);
    "type": the trial type's mean 2 s pre-cue rate (reading b)."""
    r = interval_rate(u, a, b)
    base = interval_rate(u, -2.0, 0.0)
    if baseline == "type":
        base = np.array([base[u["types"] == t].mean() for t in u["types"]])
    return zscore(r - base)


def population_z100(u: dict, start: float = -10.0, stop: float = 22.0, split_uncertainty=False):
    """Z-scored 100 ms firing (Methods, Z-score normalization, paragraph 1).

    Returns dict trial type -> 320 bins. Cue analyses collapse uncertainty (D, U, S); post-cue
    analyses split it (D, US, UO, S)."""
    c = counts(u["spikes"], u["onsets"], start, stop, 0.1) * 10.0
    base = interval_rate(u, -2.0, 0.0)
    groups = {"D": ["D"], "U": ["US", "UO"], "S": ["S"]} if not split_uncertainty else \
        {t: [t] for t in TYPES}
    out = {}
    for g, ts in groups.items():
        m = np.isin(u["types"], ts)
        out[g] = c[m].mean(0) - base[m].mean()
    allv = np.concatenate(list(out.values()))
    mu, sd = allv.mean(), allv.std(ddof=1)
    return {g: (v - mu) / sd if sd > 0 else v * 0 for g, v in out.items()}


def suppression(base_rate: np.ndarray, cue_rate: np.ndarray, zero: str = "one") -> np.ndarray:
    """(baseline - cue) / (baseline + cue); 0/0 set to 1 ("one"), 0 ("zero") or NaN ("nan")."""
    num, den = base_rate - cue_rate, base_rate + cue_rate
    with np.errstate(invalid="ignore", divide="ignore"):
        r = num / den
    fill = {"one": 1.0, "zero": 0.0, "nan": np.nan}[zero]
    return np.where(den == 0, fill, r)


def poke_baseline(u: dict, window: float) -> np.ndarray:
    return interval_rate(u, -window, 0.0, "pokes")


def total_sr(u: dict, window: float, zero: str = "one") -> np.ndarray:
    """Suppression ratio over the whole 10 s cue, per trial."""
    return suppression(poke_baseline(u, window), interval_rate(u, 0.0, CUE_S, "pokes"), zero)


def interval_sr(u: dict, a: float, b: float, window: float, zero: str = "one") -> np.ndarray:
    """Suppression ratio of the interval (onset+a, onset+b], per trial."""
    return suppression(poke_baseline(u, window), interval_rate(u, a, b, "pokes"), zero)


def waveform_features(wave: np.ndarray, fs: float = 32 / 0.0008):
    """Half duration (ms) and amplitude ratio (n - p) / (n + p) of a mean waveform.

    Methods, K-means clustering: duration is the time from peak depolarization to the trough of
    the after-hyperpolarization, halved; p is the initial hyperpolarization and n the maximal
    depolarization. Read here as: n the largest absolute deflection of the main phase, p the
    absolute value of the extreme of opposite sign before it, and the after-hyperpolarization
    the extreme of opposite sign after it. The waveform's polarity is taken from the sign of its
    largest deflection (Plexon waveforms are usually negative-going)."""
    w = np.asarray(wave, float)
    i = int(np.argmax(np.abs(w)))
    s = np.sign(w[i]) if w[i] != 0 else 1.0
    v = w * s
    n = v[i]
    p = -v[:i].min() if i > 0 else 0.0
    p = max(p, 0.0)
    j = i + int(np.argmin(v[i:]))
    half = (j - i) / fs * 1000 / 2
    amp = (n - p) / (n + p) if (n + p) != 0 else np.nan
    return half, amp
EOF
cd $TMPDIR && . wv/bin/activate && cd entries/wright-2019 && time python -c "
import pag, numpy as np, collections, resource
U=pag.load_units()
print(len(U), resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
print(collections.Counter(u['rat'] for u in U))
print(len(set(u['session'] for u in U)))
print(collections.Counter(tuple(sorted(collections.Counter(u['types']).items())) for u in U))
print(collections.Counter(tuple(u['channels']) for u in U))
print(sum(not u['spikes_sorted'] for u in U))
print(collections.Counter(u['program'] for u in U))
"
```

```
245 0.177856 GB
Counter({'rf03': 86, 'rf02': 58, 'dr01': 48, 'dr02': 37, 'rf08': 9, 'rf01': 7})
88
Counter({((np.str_('D'), 6), (np.str_('S'), 10), (np.str_('UO'), 10), (np.str_('US'), 6)): 245})
Counter({('EVT01', 'EVT02', 'EVT08', 'EVT09', 'EVT11', 'EVT12', 'EVT13', 'EVT14'): 245})
0
Counter({'b': 151, 'a': 85, 'c': 9})

real	0m37.246s
user	0m2.552s
sys	0m0.417s
```

**Agent**

Data loads in about 40 s: 245 units, 88 sessions, 6 rats, 32 trials each (6/6/10/10), all as described. Now matching the Methods regression table to find the windows the authors used.

**Agent calls Bash**

```bash
cd $TMPDIR && . wv/bin/activate && cd entries/wright-2019 && python -c "
import pag, numpy as np
U=pag.load_units()
tz=np.array([2.32,0.51,0.81,1.56,1.41,2.92,0.81,-0.40,0.21,-0.70,-0.85,-0.70,-0.70,-0.70,-0.70,0.66,0.21,-0.70,-1.00,1.11,-0.09,-0.85,-0.70,-0.70,-0.70,-0.40,-0.70,-0.70,0.21,-0.85,0.06,-0.70])
tf=np.array([1.00,1.00,1.00,1.00,0.73,1.00,1.00,0.47,0.64,0.67,1.00,0.64,1.00,0.40,0.23,1.00,1.00,0.71,0.43,1.00,0.56,1.00,0.06,0.27,-0.04,0.14,0.54,0.03,0.47,1.00,0.20,-0.14])
fi=np.array([1,1,1,1,-1,1,1,-0.33,1,1,1,-1,1,-1,0,1,1,1,1,1,-0.6,1,-0.33,0,1,1,1,-0.5,1,1,1,1.0])
best=[]
for k,u in enumerate(U):
  for bl in ['trial','type']:
    z=pag.interval_z(u,0,1,bl)
    best.append((np.abs(np.sort(z)-np.sort(tz)).max(), np.abs(z-tz).max(),k,bl))
best.sort(); print(best[:5])
# total fear match across sessions / windows
res=[]
seen=set()
for k,u in enumerate(U):
  if u['session'] in seen: continue
  seen.add(u['session'])
  for w in [2,5,10,20,30,60]:
    f=pag.total_sr(u,w); i=pag.interval_sr(u,0,1,w)
    res.append((np.nanmax(np.abs(np.sort(f)-np.sort(tf))), np.nanmax(np.abs(f-tf)), np.nanmax(np.abs(i-fi)),w,u['session'],k))
res.sort(); print(res[:6])
"
```

```
[(np.float64(0.004483776413992946), np.float64(0.004483776413992946), 157, 'trial'), (np.float64(0.31739417788130675), np.float64(3.6373941778813066), 241, 'type'), (np.float64(0.35079827286904175), np.float64(2.12609357307829), 157, 'type'), (np.float64(0.3536609323617653), np.float64(3.2557903692326695), 53, 'type'), (np.float64(0.35812316406454553), np.float64(3.8927477328720723), 38, 'type')]
[(np.float64(0.0044827586206896905), np.float64(0.0044827586206896905), np.float64(0.8235294117647058), 20, 'rf03092316epr38b', 157), (np.float64(0.14), np.float64(0.16999999999999996), np.float64(0.888888888888889), 10, 'rf03092316epr38b', 157), (np.float64(0.19666666666666663), np.float64(1.1666666666666665), np.float64(2.0), 10, 'rf03092916epr38b', 164), (np.float64(0.20297297297297298), np.float64(0.20297297297297298), np.float64(0.6363636363636365), 30, 'rf03092316epr38b', 157), (np.float64(0.237037037037037), np.float64(1.1111111111111112), np.float64(2.0), 20, 'rf03092116epr38b', 154), (np.float64(0.24347826086956517), np.float64(1.1612903225806452), np.float64(2.0), 20, 'rf02092116epr38b', 98)]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . wv/bin/activate && cd entries/wright-2019 && python -c "
import pag, numpy as np
U=pag.load_units()
u=U[157]
fi=np.array([1,1,1,1,-1,1,1,-0.33,1,1,1,-1,1,-1,0,1,1,1,1,1,-0.6,1,-0.33,0,1,1,1,-0.5,1,1,1,1.0])
for w in [1,2,5,10,20]:
  for a in np.arange(-3,12,0.5):
    for L in [0.5,1]:
      i=pag.interval_sr(u,a,a+L,w)
      d=np.nanmax(np.abs(i-fi))
      if d<0.3: print(w,a,L,d)
print(np.round(pag.interval_sr(u,0,1,20),2))
print(pag.counts(u['pokes'],u['onsets'],-20,0,20)[:,0])
print(pag.counts(u['pokes'],u['onsets'],0,10,1).astype(int))
z1=pag.zscore(pag.interval_rate(u,0,1)-np.floor(pag.interval_rate(u,-2,0)))
print(np.round(z1,2))
"
```

```
2 0.0 1 0.0033333333333332993
[ 1.    1.    1.    1.   -0.21  1.    1.   -0.29  1.    1.    1.   -0.38
  1.   -0.18 -0.03  1.    1.    1.    1.    1.   -0.48  1.   -0.38 -0.18
  1.    1.    1.   -0.6   1.    1.    1.    1.  ]
[ 9. 12.  9. 17. 13.  7. 14. 11.  9. 10. 15.  9. 14. 14. 19. 16. 15. 12.
  5.  7. 14.  4.  9. 14. 11.  8. 20. 15. 11. 15.  3.  6.]
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [1 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [1 0 0 0 1 0 0 0 0 0]
 [0 0 0 0 1 0 0 0 0 0]
 [0 0 1 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [1 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [1 0 2 0 0 0 0 0 0 0]
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; sed -n 81,92p paper/10.7554-elife.45013.txt; sed -n 109,130p paper/10.7554-elife.45013.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && . wv/bin/activate && cd entries/wright-2019 && python -c "
import pag, numpy as np, collections
from scipy import stats
U=pag.load_units()
G={'D':['D'],'U':['US','UO'],'S':['S']}
def screen(u,a,b,floor=False):
  base=pag.interval_rate(u,-2,0); 
  if floor: base=np.floor(base)
  r=pag.interval_rate(u,a,b); hit=False
  for g,ts in G.items():
    m=np.isin(u['types'],ts)
    d=r[m]-base[m]
    if np.all(d==0): continue
    t,p=stats.ttest_rel(r[m],base[m])
    if p<0.017 and t>0: hit=True
  return hit
for fl in [False,True]:
  on=[k for k,u in enumerate(U) if screen(u,0,1,fl)]
  late=[k for k,u in enumerate(U) if k not in on and screen(u,9,10,fl)]
  print(fl,len(on),len(set(U[k]['rat'] for k in on)),len(late),len(set(U[k]['rat'] for k in late)))
  print(on); print(late)
br=np.array([pag.interval_rate(u,-2,0).mean() for u in U])
print(np.percentile(br,[0,25,50,75,90,100]))
"
```

```
False 29 5 17 4
[0, 7, 11, 15, 17, 26, 33, 37, 39, 43, 48, 58, 73, 78, 97, 103, 112, 148, 153, 154, 157, 158, 165, 170, 173, 181, 219, 222, 243]
[21, 28, 36, 47, 51, 65, 74, 98, 124, 163, 167, 185, 186, 205, 207, 209, 210]
True 31 6 19 4
[0, 7, 11, 15, 17, 26, 33, 37, 39, 43, 48, 58, 73, 78, 89, 97, 103, 112, 148, 153, 154, 157, 158, 165, 170, 173, 181, 196, 219, 222, 243]
[21, 28, 36, 47, 51, 65, 74, 77, 98, 124, 163, 167, 171, 185, 186, 205, 207, 209, 210]
[6.25000000e-02 5.79687500e+00 1.69531250e+01 3.87656250e+01
 8.43531250e+01 1.69921875e+02]
```

**Agent**

The Methods screen gives exactly 29 Onset neurons from 5 rats and 17 late-responsive neurons. Now the k-means clustering.

**Agent calls Bash**

```bash
cd $TMPDIR && . wv/bin/activate && cd entries/wright-2019 && python -c "
import pag, numpy as np
from sklearn.cluster import KMeans
" 2>&1 | tail -1; uv pip install -q scikit-learn 2>&1|tail -1; python -c "
import pag, numpy as np
from scipy import stats
from sklearn.cluster import KMeans
U=pag.load_units()
late=[21, 28, 36, 47, 51, 65, 74, 98, 124, 163, 167, 185, 186, 205, 207, 209, 210]
on=[0, 7, 11, 15, 17, 26, 33, 37, 39, 43, 48, 58, 73, 78, 97, 103, 112, 148, 153, 154, 157, 158, 165, 170, 173, 181, 219, 222, 243]
ba=np.array([pag.interval_rate(u,-2,0).mean() for u in U])
bs=np.array([len(u['spikes'])/(u['spikes'][-1]-u['spikes'][0]) for u in U])
W=np.array([pag.waveform_features(u['wave']) for u in U])
print('half',np.percentile(W[:,0],[0,50,100]),'amp',np.percentile(W[:,1],[0,50,100]))
print('wave sign', np.sum([u['wave'][np.argmax(np.abs(u['wave']))]<0 for u in U]))
for nm,b in [('trialbase',ba),('session',bs)]:
  for sc in ['raw','z']:
    X=np.c_[b,W]
    if sc=='z': X=(X-X.mean(0))/X.std(0,ddof=1)
    lab=KMeans(2,n_init=10,random_state=0).fit_predict(X)
    lo=0 if b[lab==0].mean()<b[lab==1].mean() else 1
    L=lab==lo
    Fs=[stats.f_oneway(v[L],v[~L]) for v in [b,W[:,0],W[:,1]]]
    print(nm,sc,L.sum(),(~L).sum(),[(round(f.statistic,2),f.pvalue) for f in Fs], 'onset in LFR',L[on].sum(),'late HFR',(~L)[late].sum())
"
```

```
ModuleNotFoundError: No module named 'sklearn'
half [0.0375 0.075  0.2875] amp [0.02468741 0.5811965  1.        ]
wave sign 239
trialbase raw 197 48 [(np.float64(835.01), np.float64(1.41574907533579e-80)), (np.float64(0.0), np.float64(0.967945353958092)), (np.float64(0.44), np.float64(0.5090692452891304))] onset in LFR 29 late HFR 3
trialbase z 198 47 [(np.float64(823.61), np.float64(5.1589500701237245e-80)), (np.float64(0.02), np.float64(0.8849437964693917)), (np.float64(1.47), np.float64(0.22705205991516506))] onset in LFR 29 late HFR 3
session raw 194 51 [(np.float64(902.86), np.float64(8.445307677615836e-84)), (np.float64(0.05), np.float64(0.8317911333710943)), (np.float64(0.75), np.float64(0.3859371310375819))] onset in LFR 29 late HFR 3
session z 194 51 [(np.float64(902.86), np.float64(8.445307677615836e-84)), (np.float64(0.05), np.float64(0.8317911333710943)), (np.float64(0.75), np.float64(0.3859371310375819))] onset in LFR 29 late HFR 3
```

**Agent calls Bash**

```bash
cat >> entries/wright-2019/pag.py <<'EOF'


# ---------------------------------------------------------------------------------------------
# Populations (Methods, Identifying cue-responsive vlPAG neurons; K-means clustering)

CUE_GROUPS = {"D": ["D"], "U": ["US", "UO"], "S": ["S"]}   # uncertainty collapsed in the cue
SCREEN_P = 0.017   # Methods: p < 0.017, Bonferroni for three cues


def screen(u: dict, a: float, b: float, floor_baseline: bool = False) -> bool:
    """Paired two-tailed t-test over a cue's trials of the raw rate (spikes/s) in the 2 s before
    onset against the interval (a, b]; True when any cue gives p < 0.017 with the cue higher.
    floor_baseline rounds the baseline rate down, as the data set's cubeScript.m does (variant).
    A cue whose differences are all zero has no test and counts as not responsive."""
    from scipy import stats
    base = interval_rate(u, -2.0, 0.0)
    if floor_baseline:
        base = np.floor(base)
    r = interval_rate(u, a, b)
    for ts in CUE_GROUPS.values():
        m = np.isin(u["types"], ts)
        if np.all(r[m] == base[m]):
            continue
        t, p = stats.ttest_rel(r[m], base[m])
        if p < SCREEN_P and t > 0:
            return True
    return False


def cluster_features(units, baseline: str = "pre-cue"):
    """Baseline rate (spikes/s), half duration (ms) and amplitude ratio for every unit.

    baseline "pre-cue": mean rate in the 2 s before onset over the 32 trials (reading a of
    detail 5); "session": spikes over the span of the unit's spike train (reading b)."""
    if baseline == "pre-cue":
        b = np.array([interval_rate(u, -2.0, 0.0).mean() for u in units])
    else:
        b = np.array([len(u["spikes"]) / (u["spikes"][-1] - u["spikes"][0]) for u in units])
    w = np.array([waveform_features(u["wave"]) for u in units])
    return np.c_[b, w]


def kmeans2(X: np.ndarray, scale: bool, seed: int = 0, replicates: int = 20):
    """k-means, k = 2, Lloyd's algorithm with k-means++ starts, best of `replicates` (a standard
    choice; the Methods name no initialisation). Returns True for the low-rate (LFR) cluster,
    the one whose centroid baseline rate (column 0) is lower."""
    from scipy.cluster.vq import kmeans2 as _km
    Z = (X - X.mean(0)) / X.std(0, ddof=1) if scale else X.copy()
    rng = np.random.default_rng(seed)
    best = None
    for _ in range(replicates):
        cent, lab = _km(Z, 2, minit="++", seed=rng)
        inertia = sum(((Z[lab == k] - cent[k]) ** 2).sum() for k in range(2))
        if best is None or inertia < best[0] - 1e-9:
            best = (inertia, lab)
    lab = best[1]
    low = 0 if X[lab == 0, 0].mean() < X[lab == 1, 0].mean() else 1
    return lab == low


# ---------------------------------------------------------------------------------------------
# Statistics

def rm_anova(Y: np.ndarray) -> dict:
    """Repeated-measures ANOVA without sphericity correction (the integer degrees of freedom the
    paper prints). Y is subjects x A or subjects x A x B. Returns {effect: (F, df1, df2, p)}."""
    from scipy import stats
    Y = np.asarray(Y, float)
    n = Y.shape[0]
    m = Y.mean()
    if Y.ndim == 2:
        a = Y.shape[1]
        ms, ma = Y.mean(1), Y.mean(0)
        ssa = n * ((ma - m) ** 2).sum()
        sse = ((Y - ms[:, None] - ma[None, :] + m) ** 2).sum()
        d1, d2 = a - 1, (a - 1) * (n - 1)
        F = (ssa / d1) / (sse / d2)
        return {"A": (F, d1, d2, stats.f.sf(F, d1, d2))}
    n, a, b = Y.shape
    ms = Y.mean((1, 2))
    ma, mb = Y.mean((0, 2)), Y.mean((0, 1))
    msa, msb, mab = Y.mean(2), Y.mean(1), Y.mean(0)
    out = {}
    ssa = n * b * ((ma - m) ** 2).sum()
    ssas = b * ((msa - ms[:, None] - ma[None, :] + m) ** 2).sum()
    ssb = n * a * ((mb - m) ** 2).sum()
    ssbs = a * ((msb - ms[:, None] - mb[None, :] + m) ** 2).sum()
    ssab = n * ((mab - ma[:, None] - mb[None, :] + m) ** 2).sum()
    ssabs = ((Y - msa[:, :, None] - msb[:, None, :] - mab[None] + ms[:, None, None]
              + ma[None, :, None] + mb[None, None, :] - m) ** 2).sum()
    for name, ss, sse, d1, d2 in [("A", ssa, ssas, a - 1, (a - 1) * (n - 1)),
                                  ("B", ssb, ssbs, b - 1, (b - 1) * (n - 1)),
                                  ("AxB", ssab, ssabs, (a - 1) * (b - 1), (a - 1) * (b - 1) * (n - 1))]:
        F = (ss / d1) / (sse / d2)
        out[name] = (F, d1, d2, stats.f.sf(F, d1, d2))
    return out


def mixed_anova(groups: list) -> dict:
    """Split-plot ANOVA: one between factor G (the list of arrays) and two within factors A, B.
    Each array is subjects x A x B. Sums of squares with weighted means (equal to the usual
    formulas when groups are equal). Returns {effect: (F, df1, df2, p)}."""
    from scipy import stats
    Y = np.concatenate(groups)
    g = np.concatenate([np.full(len(x), i) for i, x in enumerate(groups)])
    N, a, b = Y.shape
    k = len(groups)
    m = Y.mean()
    ma, mb, mab = Y.mean((0, 2)), Y.mean((0, 1)), Y.mean(0)
    mg = np.array([x.mean() for x in groups])
    mga = np.array([x.mean((0, 2)) for x in groups])
    mgb = np.array([x.mean((0, 1)) for x in groups])
    mgab = np.array([x.mean(0) for x in groups])
    ng = np.array([len(x) for x in groups])
    ms, msa, msb = Y.mean((1, 2)), Y.mean(2), Y.mean(1)
    ssg = a * b * (ng * (mg - m) ** 2).sum()
    sssg = a * b * ((ms - mg[g]) ** 2).sum()
    ssa = N * b * ((ma - m) ** 2).sum()
    ssag = b * (ng[:, None] * (mga - mg[:, None] - ma[None] + m) ** 2).sum()
    ssasg = b * ((msa - ms[:, None] - mga[g] + mg[g][:, None]) ** 2).sum()
    ssb = N * a * ((mb - m) ** 2).sum()
    ssbg = a * (ng[:, None] * (mgb - mg[:, None] - mb[None] + m) ** 2).sum()
    ssbsg = a * ((msb - ms[:, None] - mgb[g] + mg[g][:, None]) ** 2).sum()
    ssab = N * ((mab - ma[:, None] - mb[None] + m) ** 2).sum()
    ssabg = (ng[:, None, None] * (mgab - mga[:, :, None] - mgb[:, None, :] + mg[:, None, None]
                                  - mab[None] + ma[None, :, None] + mb[None, None, :] - m) ** 2).sum()
    ssabsg = ((Y - msa[:, :, None] - msb[:, None, :] + ms[:, None, None] - mgab[g]
               + mga[g][:, :, None] + mgb[g][:, None, :] - mg[g][:, None, None]) ** 2).sum()
    dS, dA, dB = N - k, a - 1, b - 1
    rows = [("G", ssg, k - 1, sssg, dS), ("A", ssa, dA, ssasg, dA * dS),
            ("AxG", ssag, dA * (k - 1), ssasg, dA * dS), ("B", ssb, dB, ssbsg, dB * dS),
            ("BxG", ssbg, dB * (k - 1), ssbsg, dB * dS), ("AxB", ssab, dA * dB, ssabsg, dA * dB * dS),
            ("AxBxG", ssabg, dA * dB * (k - 1), ssabsg, dA * dB * dS)]
    out = {}
    for name, ss, d1, sse, d2 in rows:
        F = (ss / d1) / (sse / d2)
        out[name] = (F, d1, d2, stats.f.sf(F, d1, d2))
    return out


def sign_test(x: np.ndarray, y: np.ndarray | None = None) -> tuple[int, int, float]:
    """Two-sided sign test of x - y (or x) against zero; ties dropped. (n positive, n, p)."""
    from scipy import stats
    d = np.asarray(x, float) - (0 if y is None else np.asarray(y, float))
    d = d[~np.isnan(d) & (d != 0)]
    k = int((d > 0).sum())
    return k, len(d), stats.binomtest(k, len(d), 0.5).pvalue if len(d) else np.nan


def ols(y: np.ndarray, X: np.ndarray):
    """OLS with a constant (MATLAB regress with a column of ones). X is trials x regressors.
    Rows with a NaN are dropped. Returns (betas without the constant, their two-sided p)."""
    from scipy import stats
    X = np.atleast_2d(np.asarray(X, float).T).T
    ok = ~np.isnan(y) & ~np.isnan(X).any(1)
    y, X = y[ok], X[ok]
    A = np.c_[np.ones(len(y)), X]
    beta, *_ = np.linalg.lstsq(A, y, rcond=None)
    dof = len(y) - A.shape[1]
    resid = y - A @ beta
    s2 = resid @ resid / dof if dof > 0 else np.nan
    cov = s2 * np.linalg.pinv(A.T @ A)
    se = np.sqrt(np.diag(cov))
    with np.errstate(invalid="ignore", divide="ignore"):
        p = 2 * stats.t.sf(np.abs(beta / se), dof)
    return beta[1:], p[1:]
EOF
cd $TMPDIR && . wv/bin/activate && uv pip install -q statsmodels && cd entries/wright-2019 && python -c "
import pag, numpy as np, pandas as pd
from statsmodels.stats.anova import AnovaRM
rng=np.random.default_rng(1)
Y=rng.normal(size=(8,3,5))+np.arange(5)[None,None,:]*0.3+np.arange(3)[None,:,None]*np.arange(5)[None,None,:]*0.2
df=pd.DataFrame([dict(s=i,a=j,b=k,y=Y[i,j,k]) for i in range(8) for j in range(3) for k in range(5)])
print(AnovaRM(df,'y','s',['a','b']).fit().anova_table)
print(pag.rm_anova(Y))
print(pag.mixed_anova([Y[:4],Y[4:]]))
"
```

```
Exit code 1
/bin/bash: line 1: entries/wright-2019/pag.py: No such file or directory
Traceback (most recent call last):
  File "<string>", line 8, in <module>
    print(pag.rm_anova(Y))
          ^^^^^^^^^^^^
AttributeError: module 'pag' has no attribute 'rm_anova'
       F Value  Num DF  Den DF        Pr > F
a     5.447956     2.0    14.0  1.778279e-02
b    24.432129     4.0    28.0  8.770719e-09
a:b   2.841235     8.0    56.0  1.012560e-02
```

**Agent calls Bash**

```bash
cd  && cat >> entries/wright-2019/pag.py <<'EOF'


# ---------------------------------------------------------------------------------------------
# Populations (Methods, Identifying cue-responsive vlPAG neurons; K-means clustering)

CUE_GROUPS = {"D": ["D"], "U": ["US", "UO"], "S": ["S"]}   # uncertainty collapsed in the cue
SCREEN_P = 0.017   # Methods: p < 0.017, Bonferroni for three cues


def screen(u: dict, a: float, b: float, floor_baseline: bool = False) -> bool:
    """Paired two-tailed t-test over a cue's trials of the raw rate (spikes/s) in the 2 s before
    onset against the interval (a, b]; True when any cue gives p < 0.017 with the cue higher.
    floor_baseline rounds the baseline rate down, as the data set's cubeScript.m does (variant).
    A cue whose differences are all zero has no test and counts as not responsive."""
    from scipy import stats
    base = interval_rate(u, -2.0, 0.0)
    if floor_baseline:
        base = np.floor(base)
    r = interval_rate(u, a, b)
    for ts in CUE_GROUPS.values():
        m = np.isin(u["types"], ts)
        if np.all(r[m] == base[m]):
            continue
        t, p = stats.ttest_rel(r[m], base[m])
        if p < SCREEN_P and t > 0:
            return True
    return False


def cluster_features(units, baseline: str = "pre-cue"):
    """Baseline rate (spikes/s), half duration (ms) and amplitude ratio for every unit.

    baseline "pre-cue": mean rate in the 2 s before onset over the 32 trials (reading a of
    detail 5); "session": spikes over the span of the unit's spike train (reading b)."""
    if baseline == "pre-cue":
        b = np.array([interval_rate(u, -2.0, 0.0).mean() for u in units])
    else:
        b = np.array([len(u["spikes"]) / (u["spikes"][-1] - u["spikes"][0]) for u in units])
    w = np.array([waveform_features(u["wave"]) for u in units])
    return np.c_[b, w]


def kmeans2(X: np.ndarray, scale: bool, seed: int = 0, replicates: int = 20):
    """k-means, k = 2, Lloyd's algorithm with k-means++ starts, best of `replicates` (a standard
    choice; the Methods name no initialisation). Returns True for the low-rate (LFR) cluster,
    the one whose centroid baseline rate (column 0) is lower."""
    from scipy.cluster.vq import kmeans2 as _km
    Z = (X - X.mean(0)) / X.std(0, ddof=1) if scale else X.copy()
    rng = np.random.default_rng(seed)
    best = None
    for _ in range(replicates):
        cent, lab = _km(Z, 2, minit="++", seed=rng)
        inertia = sum(((Z[lab == k] - cent[k]) ** 2).sum() for k in range(2))
        if best is None or inertia < best[0] - 1e-9:
            best = (inertia, lab)
    lab = best[1]
    low = 0 if X[lab == 0, 0].mean() < X[lab == 1, 0].mean() else 1
    return lab == low


# ---------------------------------------------------------------------------------------------
# Statistics

def rm_anova(Y: np.ndarray) -> dict:
    """Repeated-measures ANOVA without sphericity correction (the integer degrees of freedom the
    paper prints). Y is subjects x A or subjects x A x B. Returns {effect: (F, df1, df2, p)}."""
    from scipy import stats
    Y = np.asarray(Y, float)
    n = Y.shape[0]
    m = Y.mean()
    if Y.ndim == 2:
        a = Y.shape[1]
        ms, ma = Y.mean(1), Y.mean(0)
        ssa = n * ((ma - m) ** 2).sum()
        sse = ((Y - ms[:, None] - ma[None, :] + m) ** 2).sum()
        d1, d2 = a - 1, (a - 1) * (n - 1)
        F = (ssa / d1) / (sse / d2)
        return {"A": (F, d1, d2, stats.f.sf(F, d1, d2))}
    n, a, b = Y.shape
    ms = Y.mean((1, 2))
    ma, mb = Y.mean((0, 2)), Y.mean((0, 1))
    msa, msb, mab = Y.mean(2), Y.mean(1), Y.mean(0)
    out = {}
    ssa = n * b * ((ma - m) ** 2).sum()
    ssas = b * ((msa - ms[:, None] - ma[None, :] + m) ** 2).sum()
    ssb = n * a * ((mb - m) ** 2).sum()
    ssbs = a * ((msb - ms[:, None] - mb[None, :] + m) ** 2).sum()
    ssab = n * ((mab - ma[:, None] - mb[None, :] + m) ** 2).sum()
    ssabs = ((Y - msa[:, :, None] - msb[:, None, :] - mab[None] + ms[:, None, None]
              + ma[None, :, None] + mb[None, None, :] - m) ** 2).sum()
    for name, ss, sse, d1, d2 in [("A", ssa, ssas, a - 1, (a - 1) * (n - 1)),
                                  ("B", ssb, ssbs, b - 1, (b - 1) * (n - 1)),
                                  ("AxB", ssab, ssabs, (a - 1) * (b - 1), (a - 1) * (b - 1) * (n - 1))]:
        F = (ss / d1) / (sse / d2)
        out[name] = (F, d1, d2, stats.f.sf(F, d1, d2))
    return out


def mixed_anova(groups: list) -> dict:
    """Split-plot ANOVA: one between factor G (the list of arrays) and two within factors A, B.
    Each array is subjects x A x B. Sums of squares with weighted means (equal to the usual
    formulas when groups are equal). Returns {effect: (F, df1, df2, p)}."""
    from scipy import stats
    Y = np.concatenate(groups)
    g = np.concatenate([np.full(len(x), i) for i, x in enumerate(groups)])
    N, a, b = Y.shape
    k = len(groups)
    m = Y.mean()
    ma, mb, mab = Y.mean((0, 2)), Y.mean((0, 1)), Y.mean(0)
    mg = np.array([x.mean() for x in groups])
    mga = np.array([x.mean((0, 2)) for x in groups])
    mgb = np.array([x.mean((0, 1)) for x in groups])
    mgab = np.array([x.mean(0) for x in groups])
    ng = np.array([len(x) for x in groups])
    ms, msa, msb = Y.mean((1, 2)), Y.mean(2), Y.mean(1)
    ssg = a * b * (ng * (mg - m) ** 2).sum()
    sssg = a * b * ((ms - mg[g]) ** 2).sum()
    ssa = N * b * ((ma - m) ** 2).sum()
    ssag = b * (ng[:, None] * (mga - mg[:, None] - ma[None] + m) ** 2).sum()
    ssasg = b * ((msa - ms[:, None] - mga[g] + mg[g][:, None]) ** 2).sum()
    ssb = N * a * ((mb - m) ** 2).sum()
    ssbg = a * (ng[:, None] * (mgb - mg[:, None] - mb[None] + m) ** 2).sum()
    ssbsg = a * ((msb - ms[:, None] - mgb[g] + mg[g][:, None]) ** 2).sum()
    ssab = N * ((mab - ma[:, None] - mb[None] + m) ** 2).sum()
    ssabg = (ng[:, None, None] * (mgab - mga[:, :, None] - mgb[:, None, :] + mg[:, None, None]
                                  - mab[None] + ma[None, :, None] + mb[None, None, :] - m) ** 2).sum()
    ssabsg = ((Y - msa[:, :, None] - msb[:, None, :] + ms[:, None, None] - mgab[g]
               + mga[g][:, :, None] + mgb[g][:, None, :] - mg[g][:, None, None]) ** 2).sum()
    dS, dA, dB = N - k, a - 1, b - 1
    rows = [("G", ssg, k - 1, sssg, dS), ("A", ssa, dA, ssasg, dA * dS),
            ("AxG", ssag, dA * (k - 1), ssasg, dA * dS), ("B", ssb, dB, ssbsg, dB * dS),
            ("BxG", ssbg, dB * (k - 1), ssbsg, dB * dS), ("AxB", ssab, dA * dB, ssabsg, dA * dB * dS),
            ("AxBxG", ssabg, dA * dB * (k - 1), ssabsg, dA * dB * dS)]
    out = {}
    for name, ss, d1, sse, d2 in rows:
        F = (ss / d1) / (sse / d2)
        out[name] = (F, d1, d2, stats.f.sf(F, d1, d2))
    return out


def sign_test(x: np.ndarray, y: np.ndarray | None = None) -> tuple[int, int, float]:
    """Two-sided sign test of x - y (or x) against zero; ties dropped. (n positive, n, p)."""
    from scipy import stats
    d = np.asarray(x, float) - (0 if y is None else np.asarray(y, float))
    d = d[~np.isnan(d) & (d != 0)]
    k = int((d > 0).sum())
    return k, len(d), stats.binomtest(k, len(d), 0.5).pvalue if len(d) else np.nan


def ols(y: np.ndarray, X: np.ndarray):
    """OLS with a constant (MATLAB regress with a column of ones). X is trials x regressors.
    Rows with a NaN are dropped. Returns (betas without the constant, their two-sided p)."""
    from scipy import stats
    X = np.asarray(X, float)
    if X.ndim == 1:
        X = X[:, None]
    ok = ~np.isnan(y) & ~np.isnan(X).any(1)
    y, X = y[ok], X[ok]
    A = np.c_[np.ones(len(y)), X]
    beta, *_ = np.linalg.lstsq(A, y, rcond=None)
    dof = len(y) - A.shape[1]
    resid = y - A @ beta
    s2 = resid @ resid / dof if dof > 0 else np.nan
    cov = s2 * np.linalg.pinv(A.T @ A)
    se = np.sqrt(np.diag(cov))
    with np.errstate(invalid="ignore", divide="ignore"):
        p = 2 * stats.t.sf(np.abs(beta / se), dof)
    return beta[1:], p[1:]
EOF
cd $TMPDIR && . wv/bin/activate && cd entries/wright-2019 && python -c "
import pag, numpy as np, pandas as pd
from statsmodels.stats.anova import AnovaRM
import statsmodels.formula.api as smf, statsmodels.api as sm
rng=np.random.default_rng(1)
Y=rng.normal(size=(8,3,5))+np.arange(5)[None,None,:]*0.3+np.arange(3)[None,:,None]*np.arange(5)[None,None,:]*0.2
print(pag.rm_anova(Y))
print(pag.rm_anova(Y[:,:,0]))
df=pd.DataFrame([dict(s=i,a=j,y=Y[i,j,0]) for i in range(8) for j in range(3)])
print(AnovaRM(df,'y','s',['a']).fit().anova_table)
print(pag.mixed_anova([Y[:4],Y[4:]]))
# check mixed vs pingouin-like: compare with OLS on 2-group one-within design
x=rng.normal(size=20); X=np.c_[x, rng.normal(size=20)]; y=1+2*x+rng.normal(size=20)
print(pag.ols(y,X)); print(sm.OLS(y,sm.add_constant(X)).fit().pvalues)
"
```

```
{'A': (np.float64(5.44795590002391), 2, 14, np.float64(0.017782793802874734)), 'B': (np.float64(24.432128970390885), 4, 28, np.float64(8.770718921257547e-09)), 'AxB': (np.float64(2.8412348231974414), 8, 56, np.float64(0.010125598771201137))}
{'A': (np.float64(2.6696985235098896), 2, 14, np.float64(0.10418273189650268))}
    F Value  Num DF  Den DF    Pr > F
a  2.669699     2.0    14.0  0.104183
{'G': (np.float64(0.005842427416423193), 1, 6, np.float64(0.9415574297968219)), 'A': (np.float64(8.697504165574356), 2, 12, np.float64(0.004628560562172505)), 'AxG': (np.float64(5.175297721986572), 2, 12, np.float64(0.023952612581997944)), 'B': (np.float64(23.12539803053404), 4, 24, np.float64(6.150290013982977e-08)), 'BxG': (np.float64(0.6256111536541401), 4, 24, np.float64(0.648799337954293)), 'AxB': (np.float64(3.029105242434456), 8, 48, np.float64(0.007750604199375885)), 'AxBxG': (np.float64(1.4628596425476514), 8, 48, np.float64(0.19584583701409897))}
(array([2.13347882, 0.01814999]), array([1.84041845e-09, 9.35712049e-01]))
[3.35788230e-05 1.84041845e-09 9.35712049e-01]
```

**Agent**

The ANOVA helper matches statsmodels' AnovaRM. Fig 5 supplement 2 needs a three-way repeated-measures ANOVA, so I'm making the helper n-way.

**Agent calls Bash**

```bash
python3 - <<'EOF'
src=open('pag.py').read()
a=src.index('def rm_anova(')
b=src.index('def mixed_anova(')
new='''def rm_anova(Y: np.ndarray, names: tuple | None = None) -> dict:
    """Repeated-measures ANOVA over any number of within factors, without sphericity correction
    (the integer degrees of freedom the paper prints). Y is subjects x factor1 x factor2 ...
    Each effect is tested against its interaction with subjects. Returns
    {effect: (F, df1, df2, p)}, effects named by `names` joined with "x" (default A, B, C)."""
    from itertools import combinations
    from scipy import stats
    Y = np.asarray(Y, float)
    k = Y.ndim - 1
    names = names or tuple("ABCDE"[:k])
    axes = tuple(range(Y.ndim))

    def term(T):
        # interaction term of the axes in T, by inclusion-exclusion of marginal means
        t = 0.0
        for r in range(len(T) + 1):
            for R in combinations(T, r):
                rest = tuple(ax for ax in axes if ax not in R)
                t = t + (-1) ** (len(T) - r) * Y.mean(axis=rest, keepdims=True)
        return np.broadcast_to(t, Y.shape)

    out = {}
    for r in range(1, k + 1):
        for S in combinations(range(1, k + 1), r):
            ss = (term(S) ** 2).sum()
            sse = (term((0,) + S) ** 2).sum()
            d1 = int(np.prod([Y.shape[ax] - 1 for ax in S]))
            d2 = d1 * (Y.shape[0] - 1)
            F = (ss / d1) / (sse / d2)
            out["x".join(names[ax - 1] for ax in S)] = (F, d1, d2, stats.f.sf(F, d1, d2))
    return out


'''
open('pag.py','w').write(src[:a]+new+src[b:])
EOF
cd $TMPDIR && . wv/bin/activate && cd entries/wright-2019 && python -c "
import pag, numpy as np, pandas as pd
from statsmodels.stats.anova import AnovaRM
rng=np.random.default_rng(1)
Y=rng.normal(size=(8,3,5,2))+np.arange(5)[None,None,:,None]*0.3
df=pd.DataFrame([dict(s=i,a=j,b=k,c=l,y=Y[i,j,k,l]) for i in range(8) for j in range(3) for k in range(5) for l in range(2)])
print(AnovaRM(df,'y','s',['a','b','c']).fit().anova_table)
print(pag.rm_anova(Y))
U=pag.load_units(); u=U[157]
b2=pag.counts(u['pokes'],u['onsets'],-2,0,2)[:,0]; i1=pag.counts(u['pokes'],u['onsets'],0,1,1)[:,0]
print('0/0 trials', np.where((b2==0)&(i1==0))[0]+1)
print('b2',b2.astype(int)); print('i1',i1.astype(int))
"
```

```
F Value  Num DF  Den DF    Pr > F
a       0.022998     2.0    14.0  0.977301
b      10.110044     4.0    28.0  0.000034
c       0.563008     1.0     7.0  0.477509
a:b     0.322045     8.0    56.0  0.954298
a:c     0.703080     2.0    14.0  0.511724
b:c     1.393536     4.0    28.0  0.261728
a:b:c   2.947907     8.0    56.0  0.008018
{'A': (np.float64(0.02299832495093451), 2, 14, np.float64(0.9773009620056432)), 'B': (np.float64(10.110044102318334), 4, 28, np.float64(3.4123024113348964e-05)), 'C': (np.float64(0.5630080231497795), 1, 7, np.float64(0.47750855149093463)), 'AxB': (np.float64(0.3220452311098443), 8, 56, np.float64(0.9542978602265147)), 'AxC': (np.float64(0.7030797766868915), 2, 14, np.float64(0.5117236755365062)), 'BxC': (np.float64(1.3935362306486117), 4, 28, np.float64(0.26172764337115645)), 'AxBxC': (np.float64(2.9479069709781074), 8, 56, np.float64(0.008018324140189267))}
0/0 trials [ 6  9 11 16 19 20 22 26 27 31]
b2 [1 2 2 1 0 0 1 1 0 1 0 0 1 0 2 0 2 1 0 0 1 0 1 2 1 0 0 2 3 1 0 1]
i1 [0 0 0 0 1 0 0 1 0 0 0 1 0 1 1 0 0 0 0 0 2 0 1 1 0 0 0 3 0 0 0 0]
```

**Agent calls Bash**

```bash
date -u; mkdir -p $TMPDIR/build; cat > $TMPDIR/build/tonb.py <<'EOF'
import sys, re, nbformat
src = open(sys.argv[1]).read()
cells = []
for block in re.split(r'^# %%', src, flags=re.M)[1:]:
    head, _, body = block.partition('\n')
    tags = re.findall(r'"([^"]+)"', head.split('tags=')[1]) if 'tags=' in head else []
    body = body.strip('\n')
    if '[markdown]' in head:
        body = '\n'.join(l[2:] if l.startswith('# ') else l.lstrip('#') for l in body.split('\n'))
        c = nbformat.v4.new_markdown_cell(body)
    else:
        c = nbformat.v4.new_code_cell(body)
    if tags: c.metadata['tags'] = tags
    cells.append(c)
nb = nbformat.v4.new_notebook(cells=cells)
nb.metadata['kernelspec'] = {'name': 'python3', 'display_name': 'Python 3', 'language': 'python'}
nbformat.write(nb, sys.argv[2])
EOF
echo ok
```

```
Wed Nov 11 10:30:06 UTC 2026
ok
```

**Agent calls Bash**

```bash
cat > $TMPDIR/build/p1.py <<'EOF'
# %%
import time
import resource

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

import pag

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 40)
T0 = time.time()
units = pag.load_units()
print(f"{len(units)} units loaded in {time.time() - T0:.0f} s")

# %% [markdown]
# ## Data check
#
# The data set's description (version 0.5, 6 March 2019) says: 245 single units from 88 sessions
# of 6 rats, 32 trials per session (6 danger, 6 uncertainty shock, 10 uncertainty omission, 10
# safety), 10 s cues, foot shock 2 s after cue offset, waveforms of 32 points over 0.8 ms. Each
# check against the values is stated under its output.

# %% tags=["sanity"]
print("checksums.md5 of the data set:", pag.checksums())
info = pd.DataFrame([dict(file=u["file"], session=u["session"], rat=u["rat"], program=u["program"],
                          unit=u["unit"], n_spikes=len(u["spikes"]), n_pokes=len(u["pokes"]),
                          n_shocks=len(u["shock"]), n_trials=len(u["onsets"]),
                          **{t: int((u["types"] == t).sum()) for t in pag.TYPES})
                     for u in units])
print("units", len(info), "| sessions", info.session.nunique(), "| rats", info.rat.nunique())
print(info.groupby("rat").agg(units=("unit", "size"), sessions=("session", "nunique"),
                              program=("program", lambda s: "".join(sorted(set(s))))).to_string())
print("trials per type over units:", info[list(pag.TYPES)].drop_duplicates().to_dict("records"))
print("event channels in every file:", sorted({tuple(u["channels"]) for u in units}))
print("spike trains sorted in every file:", all(u["spikes_sorted"] for u in units))

# %% [markdown]
# Counts agree with the description: 245 units, 88 sessions, 6 rats, and every session has
# 6/6/10/10 trials once uncertainty trials are split by a shock within 30 s of onset. Three
# behaviour programs (a, b, c) assign the cue channels differently (counterbalancing of the
# auditory cues, data set's cubeScript.m). The files also hold EVT08 and EVT14, which cubeScript.m
# does not use; they are checked below.

# %% tags=["sanity"]
sess = {}
for u in units:
    sess.setdefault(u["session"], []).append(u)
same_events = all(all(np.array_equal(v[0]["onsets"], w["onsets"]) and np.array_equal(v[0]["pokes"], w["pokes"])
                      for w in v) for v in sess.values())
print("all units of a session share cue and poke times:", same_events)
lat = []
for v in sess.values():
    u = v[0]
    for t, ty in zip(u["onsets"], u["types"]):
        s = u["shock"][(u["shock"] > t) & (u["shock"] <= t + 30)]
        lat.append((ty, len(s), (s[0] - t) if len(s) else np.nan))
lat = pd.DataFrame(lat, columns=["type", "n_shock", "latency"])
print(lat.groupby("type").agg(trials=("n_shock", "size"), shocks=("n_shock", "sum"),
                             lat_min=("latency", "min"), lat_max=("latency", "max")).to_string())
gaps = np.concatenate([np.diff(np.sort(v[0]["onsets"])) for v in sess.values()])
print(f"time between cue onsets: min {gaps.min():.1f} s, median {np.median(gaps):.1f} s, max {gaps.max():.1f} s")
u0 = units[0]
print("EVT08 equal to EVT01 (shock) in every session:",
      all(np.array_equal(v[0]["shock"], pag.sio.loadmat(pag.io.BytesIO(pag.open_zip().read("data/mFiles/" + v[0]["file"])))["EVT08"].ravel()) for v in list(sess.values())[:5]),
      "(first 5 sessions)")

# %% [markdown]
# Shocks fall 12.0 s after onset on every danger and uncertainty shock trial (cue 10 s, shock 2 s
# after offset, as described), and never on safety or omission trials. Mean inter-onset time is
# consistent with the 3.5 min mean ITI. EVT08 repeats the shock channel.

# %% tags=["sanity"]
# duplicate recordings: identical or near-identical spike trains within a session, and across
# sessions identical trains
dups = []
for name, v in sess.items():
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            a, b = v[i]["spikes"], v[j]["spikes"]
            k = np.searchsorted(b, a)
            near = np.minimum(np.abs(a - b[np.clip(k, 0, len(b) - 1)]), np.abs(a - b[np.clip(k - 1, 0, len(b) - 1)]))
            frac = (near <= 0.0005).mean()
            if frac > 0.5:
                dups.append((name, v[i]["unit"], v[j]["unit"], round(frac, 3), len(a), len(b)))
print("unit pairs in a session sharing more than half their spikes (within 0.5 ms):", dups)
hashes = {}
for u in units:
    hashes.setdefault(hash(u["spikes"].tobytes()), []).append(u["file"])
print("identical spike trains in different files:", [v for v in hashes.values() if len(v) > 1])
date_rat = info.drop_duplicates("session").groupby(["rat", info.session.str[4:10]]).size()
print("sessions sharing a rat and date:", date_rat[date_rat > 1].to_dict())

# %% [markdown]
# No unit is deposited twice. Units are counted once each; the paper treats each unit as a
# separate neuron (electrodes advanced between sessions), and so does this notebook.

# %% tags=["sanity"]
rates = np.array([len(u["spikes"]) / (u["spikes"][-1] - u["spikes"][0]) for u in units])
wav = np.array([u["wave"] for u in units])
span = np.array([u["spikes"][-1] - u["spikes"][0] for u in units]) / 60
print(f"session span covered by spikes: {span.min():.0f} to {span.max():.0f} min (description: 93 min sessions)")
print(f"mean firing rate per unit: {rates.min():.2f} to {rates.max():.1f} spikes/s, median {np.median(rates):.1f}")
print(f"waveform values: {wav.min():.4f} to {wav.max():.4f} (no unit stated; 32 points = 0.8 ms at 40 kHz)")
print("units whose largest deflection is negative:", int((wav[np.arange(len(wav)), np.abs(wav).argmax(1)] < 0).sum()), "of", len(wav))
pk = np.concatenate([pag.counts(v[0]["pokes"], v[0]["onsets"], -20, 0, 20)[:, 0] * 3 for v in sess.values()])
print(f"nose pokes per minute in the 20 s before onset: median {np.median(pk):.0f}, max {pk.max():.0f}")

# %% [markdown]
# The waveform has no unit in the files or the description; the amplitude ratio used below is
# unit-free. Session spans are near the 93 min the description gives.
#
# **Shared clock.** Spikes, cues and pokes come from one Plexon file per session (description).
# The check below contrasts real cue onsets with onsets moved 60 s earlier, into the ITI: the
# cue-onset screen of the Methods finds many more responsive units at the true onsets, and poke
# rates fall during real cues but not in the shifted windows. Both streams therefore carry the cue
# on the trial table's clock.

# %% tags=["sanity"]
def n_responsive(shift):
    hit = 0
    for u in units:
        v = dict(u, onsets=u["onsets"] + shift)
        hit += pag.screen(v, 0.0, 1.0)
    return hit

for shift in (0.0, -60.0):
    sr = [np.mean(pag.total_sr(dict(v[0], onsets=v[0]["onsets"] + shift), 20.0)[v[0]["types"] == "D"]) for v in sess.values()]
    print(f"onsets shifted {shift:+.0f} s: units passing the onset screen {n_responsive(shift)}, "
          f"mean danger suppression ratio over sessions {np.mean(sr):.2f}")

# %% [markdown]
# ### The paper's example regression input
#
# The Methods (Single-unit, linear regression) print the full regression input of the first
# interval of one Onset neuron: Z firing, interval fear and total fear for its 32 trials. The
# claims file leaves open the nose poke baseline (detail 1), the 0/0 ratio (detail 2) and the
# firing baseline (detail 4). The cell below searches every unit and window for that table.

# %% tags=["sanity"]
TAB_Z = np.array([2.32, 0.51, 0.81, 1.56, 1.41, 2.92, 0.81, -0.40, 0.21, -0.70, -0.85, -0.70, -0.70, -0.70, -0.70, 0.66,
                  0.21, -0.70, -1.00, 1.11, -0.09, -0.85, -0.70, -0.70, -0.70, -0.40, -0.70, -0.70, 0.21, -0.85, 0.06, -0.70])
TAB_IF = np.array([1, 1, 1, 1, -1, 1, 1, -0.33, 1, 1, 1, -1, 1, -1, 0, 1, 1, 1, 1, 1, -0.6, 1, -0.33, 0, 1, 1, 1, -0.5,
                   1, 1, 1, 1.0])
TAB_TF = np.array([1, 1, 1, 1, 0.73, 1, 1, 0.47, 0.64, 0.67, 1, 0.64, 1, 0.40, 0.23, 1, 1, 0.71, 0.43, 1, 0.56, 1,
                   0.06, 0.27, -0.04, 0.14, 0.54, 0.03, 0.47, 1, 0.20, -0.14])
rows = []
for k, u in enumerate(units):
    for bl in ("trial", "type"):
        rows.append(dict(unit=k, file=u["file"], z_baseline=bl,
                         max_abs_diff=np.abs(pag.interval_z(u, 0, 1, bl) - TAB_Z).max()))
zmatch = pd.DataFrame(rows).sort_values("max_abs_diff").head(4)
print("Z firing, closest units:\n", zmatch.to_string(index=False))
k = int(zmatch.iloc[0].unit)
ex = units[k]
rows = []
for w in (2, 10, 20):
    for zero in ("one", "zero"):
        rows.append(dict(baseline_s=w, zero_over_zero=zero,
                         interval_fear_diff=np.abs(pag.interval_sr(ex, 0, 1, w, zero) - TAB_IF).max(),
                         total_fear_diff=np.abs(pag.total_sr(ex, w, zero) - TAB_TF).max()))
print(f"\nunit {ex['file']}: largest difference from the table by poke baseline window")
print(pd.DataFrame(rows).round(3).to_string(index=False))
b2 = pag.counts(ex["pokes"], ex["onsets"], -2, 0, 2)[:, 0]
i1 = pag.counts(ex["pokes"], ex["onsets"], 0, 1, 1)[:, 0]
zz = np.where((b2 == 0) & (i1 == 0))[0]
print("\ntrials (1-based) with no poke in the 2 s baseline or the first second:", (zz + 1).tolist(),
      "-> table interval fear", TAB_IF[zz].tolist())
zf = pag.zscore(pag.interval_rate(ex, 0, 1) - np.floor(pag.interval_rate(ex, -2, 0)))
print("Z firing with the baseline rate rounded down (cubeScript.m): largest difference", round(np.abs(zf - TAB_Z).max(), 3))
cs = pag.open_zip().read("data/cubeScript.m").decode("latin-1").splitlines()
print("\ndata/cubeScript.m, the data set's script:")
for line in cs:
    if "20-s baseline" in line or "replace NaN with 1" in line or "time.cue(iii,2)-20);" in line:
        print("   ", line.strip())

# %% [markdown]
# One unit (rf03092316, rat rf03) reproduces the table to its two printed decimals. Its Z firing
# is the trial's own 2 s baseline subtracted, not rounded (reading a of detail 4). Its interval
# fear uses the 2 s before onset as the poke baseline (reading a of detail 1), while its total
# fear uses the 20 s before onset, a window neither reading of detail 1 names, and the one the
# data set's cubeScript.m uses. Ratios of 0/0 are 1.00 in the table (and in cubeScript.m), a
# third reading of detail 2. The analysis below therefore takes as its primary reading the one
# the paper's own table fixes: total fear over a 20 s baseline, interval fear over a 2 s
# baseline, 0/0 set to 1, Z firing against the trial's own baseline (Methods, Single-unit,
# linear regression, the table). The claims file's readings are run beside it in every claim
# they bear on. The question is put to a reader in questions/wright-2019.yaml.
EOF
cd $TMPDIR && . wv/bin/activate && cd entries/wright-2019 && MPLBACKEND=Agg time python $TMPDIR/build/p1.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/build/p1.py", line 11, in <module>
    import pag
ModuleNotFoundError: No module named 'pag'
Command exited with non-zero status 1
2.39user 0.15system 0:02.33elapsed 108%CPU (0avgtext+0avgdata 166540maxresident)k
14088inputs+12824outputs (1major+32248minor)pagefaults 0swaps
```

**Agent calls Bash**

```bash
cd $TMPDIR && . wv/bin/activate && cd entries/wright-2019 && PYTHONPATH=. MPLBACKEND=Agg time python $TMPDIR/build/p1.py
```

```
245 units loaded in 34 s
checksums.md5 of the data set: {'data.zip': '5437f01d5071fe55a1baedbb146f56e0', 'docs/crcns_pag-1_data_description.docx': '0ac5a035f0c0521ccefcb410862e8792', 'docs/crcns_pag-1_data_description.pdf': '9ac2531d1605bc085e2fef87b446c6cb', 'filelist.txt': 'a45c303f4e9c12949c149fe2d9e16601'}
units 245 | sessions 88 | rats 6
      units  sessions program
rat                          
dr01     48        18       a
dr02     37        17       a
rf01      7         6       b
rf02     58        19       b
rf03     86        25       b
rf08      9         3       c
trials per type over units: [{'D': 6, 'US': 6, 'UO': 10, 'S': 10}]
event channels in every file: [('EVT01', 'EVT02', 'EVT08', 'EVT09', 'EVT11', 'EVT12', 'EVT13', 'EVT14')]
spike trains sorted in every file: True
all units of a session share cue and poke times: True
      trials  shocks   lat_min  lat_max
type                                   
D        528     528  11.99985  12.0001
S        880       0       NaN      NaN
UO       880       0       NaN      NaN
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p=open('/tmp/claude-1001/build/p1.py').read() if False else None
EOF
F=$TMPDIR/build/p1.py; python3 - "$F" <<'EOF'
import sys
f=sys.argv[1]; s=open(f).read()
s=s.replace('''u0 = units[0]
print("EVT08 equal to EVT01 (shock) in every session:",
      all(np.array_equal(v[0]["shock"], pag.sio.loadmat(pag.io.BytesIO(pag.open_zip().read("data/mFiles/" + v[0]["file"])))["EVT08"].ravel()) for v in list(sess.values())[:5]),
      "(first 5 sessions)")
''','''print(f"mean time between cue onsets {gaps.mean():.1f} s = {gaps.mean() / 60:.2f} min; "
      f"ITI from cue offset {(gaps.mean() - 10) / 60:.2f} min")
''')
s=s.replace('''consistent with the 3.5 min mean ITI. EVT08 repeats the shock channel.''','''not consistent with the "mean ITI of 3.5 min" of the paper and the description: onsets are
# 132 to 195 s apart (printed above), so no ITI reaches 3.5 min. This is recorded as a finding;
# no claim uses the ITI length.''')
s=s.replace('''# No unit is deposited twice. Units are counted once each; the paper treats each unit as a
# separate neuron (electrodes advanced between sessions), and so does this notebook.''','''# No file is deposited twice, and no two sessions share a rat and date. Five pairs of units
# recorded in the same session share 66 to 90% of the spikes of one of them (within 0.5 ms),
# which suggests one neuron sorted on two wires. The paper counts 245 units, so it kept both;
# the analysis follows the paper and counts them as given, and the claims that use the
# populations say whether any pair falls in them. Recorded as a finding.''')
open(f,'w').write(s)
EOF
grep -n "ITI\|five pairs\|Five pairs" $F | head
```

```
67:      f"ITI from cue offset {(gaps.mean() - 10) / 60:.2f} min")
72:# not consistent with the "mean ITI of 3.5 min" of the paper and the description: onsets are
73:# 132 to 195 s apart (printed above), so no ITI reaches 3.5 min. This is recorded as a finding;
74:# no claim uses the ITI length.
98:# No file is deposited twice, and no two sessions share a rat and date. Five pairs of units
120:# The check below contrasts real cue onsets with onsets moved 60 s earlier, into the ITI: the
```

**Agent calls Bash**

```bash
cat > $TMPDIR/build/p2.py <<'EOF'
# %% [markdown]
# ## Behaviour: one value per session
#
# The behavioural claims are per session (88), each counted once whatever the number of units.
# Readings of the claims file: poke baseline 2 s or 10 s (detail 1), 0/0 ratio set to 0 or left
# out (detail 2), the session value the mean of the per-trial ratios or the ratio of the session's
# mean rates (detail 3). Added from the Methods regression table (above): a 20 s baseline for
# total fear and 0/0 set to 1. Uncertainty shock and omission trials are collapsed in the cue
# (Methods, Population and single-unit firing analyses).

# %%
S_UNITS = [v[0] for v in sess.values()]
CUES = {"D": ["D"], "U": ["US", "UO"], "S": ["S"]}
WINDOWS = (2.0, 10.0, 20.0)
ZEROS = ("one", "zero", "nan")


def session_sr(u, a, b, window, zero, agg):
    """Session suppression ratio per cue for the interval (a, b] of the cue."""
    base = pag.poke_baseline(u, window)
    cue = pag.interval_rate(u, a, b, "pokes")
    out = {}
    for c, ts in CUES.items():
        m = np.isin(u["types"], ts)
        if agg == "trial mean":
            out[c] = np.nanmean(pag.suppression(base[m], cue[m], zero))
        else:
            out[c] = pag.suppression(np.array([base[m].mean()]), np.array([cue[m].mean()]), zero)[0]
    return out


def ttest_rel(x, y):
    ok = ~np.isnan(x) & ~np.isnan(y)
    return stats.ttest_rel(x[ok], y[ok])

# %% [markdown]
# ### fig1c-total-suppression
#
# > Over the 88 recording sessions, suppression ratio over the whole 10 s cue differs by cue, high
# > to danger (0.80), intermediate to uncertainty (0.53) and low to safety (0.03), and each cue
# > pair differs.
#
# Criterion: within tolerance (0.80 +- 0.08, 0.53 +- 0.053, 0.03 +- 0.05) under one reading, the
# repeated-measures ANOVA of cue at p < 0.05 and both paired t-tests at p < 0.05.

# %% tags=["claim:fig1c-total-suppression"]
rows = []
SR_TOTAL = {}
for w in WINDOWS:
    for zero in ZEROS:
        for agg in ("trial mean", "ratio of means"):
            if agg == "ratio of means" and zero != "one":
                continue   # the 0/0 rule matters only when a whole session has no poke
            vals = pd.DataFrame([session_sr(u, 0, 10, w, zero, agg) for u in S_UNITS])
            SR_TOTAL[(w, zero, agg)] = vals
            ok = vals.dropna()
            an = pag.rm_anova(ok[["D", "U", "S"]].to_numpy())["A"]
            t1, t2 = ttest_rel(vals.D.values, vals.U.values), ttest_rel(vals.U.values, vals.S.values)
            within = (abs(vals.D.mean() - 0.80) <= 0.08) & (abs(vals.U.mean() - 0.53) <= 0.053) & (abs(vals.S.mean() - 0.03) <= 0.05)
            tests = (an[3] < 0.05) & (t1.pvalue < 0.05) & (t1.statistic > 0) & (t2.pvalue < 0.05) & (t2.statistic > 0)
            rows.append(dict(baseline_s=w, zero=zero, session=agg, D=vals.D.mean(), U=vals.U.mean(), S=vals.S.mean(),
                             F=an[0], df=f"{an[1]},{an[2]}", p_anova=an[3], t_DU=t1.statistic, p_DU=t1.pvalue,
                             t_US=t2.statistic, p_US=t2.pvalue, means_ok=within, tests_ok=tests))
fig1c = pd.DataFrame(rows)
print(fig1c.to_string(index=False, float_format=lambda x: f"{x:.3g}"))
print("\nsessions:", len(S_UNITS))
prim = SR_TOTAL[(20.0, "one", "trial mean")]
print("\nprimary reading (20 s, 0/0 = 1, trial mean) by rat:")
print(prim.assign(rat=[u["rat"] for u in S_UNITS]).groupby("rat").agg(["mean", "size"]).round(2).to_string())

# %% [markdown]
# ### fig1c-nonlinear-scaling
#
# > Suppression scales non-linearly with shock probability. Uncertainty's shock probability is
# > closer to safety, but its mean suppression ratio is closer to danger.
#
# Criterion: the uncertainty mean exceeds the midpoint of the danger and safety means, under the
# reading fig1c-total-suppression matched on (every reading if none).

# %% tags=["claim:fig1c-nonlinear-scaling"]
fig1c["midpoint"] = (fig1c.D + fig1c.S) / 2
fig1c["U_above_midpoint"] = fig1c.U > fig1c.midpoint
print(fig1c[["baseline_s", "zero", "session", "D", "U", "S", "midpoint", "U_above_midpoint", "means_ok"]]
      .to_string(index=False, float_format=lambda x: f"{x:.3f}"))

# %% [markdown]
# ### fig1d-interval-suppression
#
# > Suppression ratios in each 1 s cue interval discriminate every cue pair in every interval,
# > with a cue effect and a cue x interval interaction.
#
# Criterion: two-way repeated-measures ANOVA (cue x interval) with cue and interaction at p <
# 0.05, and in all ten intervals danger > uncertainty and uncertainty > safety by paired t-tests
# at p < 0.005; partially reproduced with at least eight intervals each. Interval fear uses the 2 s
# baseline in the paper's table; the 10 s and 20 s windows are run too.

# %% tags=["claim:fig1d-interval-suppression"]
rows = []
for w in WINDOWS:
    for zero in ZEROS:
        for agg in ("trial mean", "ratio of means"):
            if agg == "ratio of means" and zero != "one":
                continue
            Y = np.array([[[session_sr(u, k, k + 1, w, zero, agg)[c] for k in range(10)] for c in "DUS"] for u in S_UNITS])
            ok = ~np.isnan(Y).any((1, 2))
            an = pag.rm_anova(Y[ok], ("cue", "interval"))
            nDU = nUS = 0
            tmin = [np.inf, np.inf]
            for k in range(10):
                a, b = ttest_rel(Y[:, 0, k], Y[:, 1, k]), ttest_rel(Y[:, 1, k], Y[:, 2, k])
                nDU += (a.pvalue < 0.005) & (a.statistic > 0)
                nUS += (b.pvalue < 0.005) & (b.statistic > 0)
                tmin = [min(tmin[0], a.statistic), min(tmin[1], b.statistic)]
            rows.append(dict(baseline_s=w, zero=zero, session=agg, n_sessions=int(ok.sum()),
                             F_cue=an["cue"][0], df_cue=f"{an['cue'][1]},{an['cue'][2]}", p_cue=an["cue"][3],
                             F_int=an["cuexinterval"][0], df_int=f"{an['cuexinterval'][1]},{an['cuexinterval'][2]}",
                             p_int=an["cuexinterval"][3], DU_sig_of_10=nDU, US_sig_of_10=nUS,
                             min_t_DU=tmin[0], min_t_US=tmin[1]))
print(pd.DataFrame(rows).to_string(index=False, float_format=lambda x: f"{x:.3g}"))

# %% [markdown]
# ### fig1s1a-nose-poke-rates
#
# > Baseline nose poke rates do not differ between trial types, and poking falls from baseline to
# > cue for danger and uncertainty but not for safety.
#
# Criterion: per session and trial type (four), mean baseline and cue poke rates. Baseline
# against cue by paired t-test at p < 0.05 (danger and both uncertainty types fall, safety does
# not); baseline across the four types by one-way repeated-measures ANOVA at p < 0.05 (no
# difference), pairwise t-tests as a variant.

# %% tags=["claim:fig1s1a-nose-poke-rates"]
for w in WINDOWS:
    B = np.array([[pag.poke_baseline(u, w)[u["types"] == t].mean() * 60 for t in pag.TYPES] for u in S_UNITS])
    C = np.array([[pag.interval_rate(u, 0, 10, "pokes")[u["types"] == t].mean() * 60 for t in pag.TYPES] for u in S_UNITS])
    an = pag.rm_anova(B)["A"]
    print(f"baseline {w:.0f} s: baseline across types F({an[1]},{an[2]}) = {an[0]:.2f}, p = {an[3]:.3g}; "
          "mean baseline (pokes/min) " + ", ".join(f"{t} {B[:, i].mean():.1f}" for i, t in enumerate(pag.TYPES)))
    for i, t in enumerate(pag.TYPES):
        r = stats.ttest_rel(B[:, i], C[:, i])
        print(f"   {t:2s}: baseline {B[:, i].mean():5.1f} -> cue {C[:, i].mean():5.1f} pokes/min, t(87) = {r.statistic:6.2f}, p = {r.pvalue:.3g}")
    pw = [(pag.TYPES[i], pag.TYPES[j], stats.ttest_rel(B[:, i], B[:, j]).pvalue) for i in range(4) for j in range(i + 1, 4)]
    print("   variant, baseline pairs p:", ", ".join(f"{a}-{b} {p:.3g}" for a, b, p in pw))

# %% [markdown]
# ### fig1s1b-sr-poke-correlation
#
# > Suppression ratio and cue nose poke rate are significantly correlated across sessions,
# > particularly for danger and uncertainty.
#
# Criterion: Pearson correlation over the 88 sessions of total cue suppression ratio and cue poke
# rate, per cue (reading a) or over all 264 points (reading b); reproduced when, under one
# reading, danger and uncertainty correlate negatively at p < 0.05 (and the pooled one under b).

# %% tags=["claim:fig1s1b-sr-poke-correlation"]
rows = []
CR = {c: np.array([pag.interval_rate(u, 0, 10, "pokes")[np.isin(u["types"], ts)].mean() * 60 for u in S_UNITS])
      for c, ts in CUES.items()}
for (w, zero, agg), vals in SR_TOTAL.items():
    r = {}
    for c in "DUS":
        ok = ~np.isnan(vals[c].values)
        r[c] = stats.pearsonr(vals[c].values[ok], CR[c][ok])
    allx = np.concatenate([vals[c].values for c in "DUS"])
    ally = np.concatenate([CR[c] for c in "DUS"])
    ok = ~np.isnan(allx)
    rp = stats.pearsonr(allx[ok], ally[ok])
    rows.append(dict(baseline_s=w, zero=zero, session=agg, **{f"r_{c}": r[c][0] for c in "DUS"},
                     **{f"p_{c}": r[c][1] for c in "DUS"}, r_all=rp[0], p_all=rp[1]))
print(pd.DataFrame(rows).to_string(index=False, float_format=lambda x: f"{x:.3g}"))
EOF
cat $TMPDIR/build/p1.py $TMPDIR/build/p2.py > $TMPDIR/build/dev.py; cd $TMPDIR && . wv/bin/activate && cd entries/wright-2019 && PYTHONPATH=. MPLBACKEND=Agg time python $TMPDIR/build/dev.py 2>&1 | sed -n '/fig1c\|baseline_s/,$p' | head -150
```

```
baseline_s zero_over_zero  interval_fear_diff  total_fear_diff
          2            one               0.003            1.730
          2           zero               1.000            1.730
         10            one               0.889            0.170
         10           zero               0.889            0.170
         20            one               0.824            0.004
         20           zero               0.824            0.004

trials (1-based) with no poke in the 2 s baseline or the first second: [6, 9, 11, 16, 19, 20, 22, 26, 27, 31] -> table interval fear [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
Z firing with the baseline rate rounded down (cubeScript.m): largest difference 0.125

data/cubeScript.m, the data set's script:
    % 20-s baseline
    aa = z(z>time.cue(iii,2)-20); % pokes occuring after cue onset - 20
    cer.cue(isnan(cer.cue))=1; % replace NaN with 1, occurs when baseline and cue period are 0, indicative of no poking and high fear
 baseline_s zero        session     D      U        S   F    df  p_anova  t_DU     p_DU  t_US     p_US  means_ok  tests_ok
          2  one     trial mean  0.56  0.203   -0.236 190 2,174 1.87e-44   8.7 1.85e-13    12 3.14e-20     False      True
          2  one ratio of means 0.748  0.459 -0.00948 263 2,174 2.43e-53   8.9 7.22e-14  15.7 3.49e-27     False      True
          2 zero     trial mean 0.348 0.0736   -0.248 116 2,174 1.15e-32  6.61 2.98e-09  10.2 1.63e-16     False      True
          2  nan     trial mean 0.464 0.0973   -0.252 120 2,174 2.03e-33  7.48  5.6e-11  9.96 4.96e-16     False      True
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat > $TMPDIR/build/p3.py <<'EOF'
# %% [markdown]
# ## Clusters and populations
#
# ### fig1e-two-clusters
#
# > K-means clustering (k = 2) of all 245 neurons on baseline firing rate, waveform half duration
# > and amplitude ratio splits them on baseline firing rate alone into a low firing rate cluster
# > of 199 and a high firing rate cluster of 46.
#
# Criterion: under one reading of detail 5 (baseline rate: 2 s pre-cue over the 32 trials, or
# the session mean; features raw or Z-scored), both cluster sizes within tolerance (199 +- 19.9,
# 46 +- 4.6), the ANOVA of baseline rate by cluster at p < 0.001, and those of amplitude ratio and
# duration at p > 0.05. Initialisation: k-means++ starts, 20 replicates, fixed seed (a standard
# choice). The waveform features follow the Methods; how the peaks are picked is in pag.py.

# %% tags=["claim:fig1e-two-clusters"]
rng_clu = 0
CLUSTERS = {}
rows = []
for base in ("pre-cue", "session"):
    X = pag.cluster_features(units, base)
    for scale in (False, True):
        lfr = pag.kmeans2(X, scale, seed=rng_clu)
        CLUSTERS[(base, scale)] = lfr
        f = [stats.f_oneway(X[lfr, i], X[~lfr, i]) for i in range(3)]
        rows.append(dict(baseline=base, scaled=scale, LFR=int(lfr.sum()), HFR=int((~lfr).sum()),
                         F_rate=f[0].statistic, p_rate=f[0].pvalue, F_halfdur=f[1].statistic, p_halfdur=f[1].pvalue,
                         F_ampratio=f[2].statistic, p_ampratio=f[2].pvalue,
                         rate_LFR=X[lfr, 0].mean(), rate_HFR=X[~lfr, 0].mean()))
fig1e = pd.DataFrame(rows)
print(fig1e.to_string(index=False, float_format=lambda x: f"{x:.3g}"))
X = pag.cluster_features(units, "pre-cue")
print(f"\nfeature ranges: baseline rate {X[:, 0].min():.2f} to {X[:, 0].max():.1f} spikes/s; half duration "
      f"{X[:, 1].min():.3f} to {X[:, 1].max():.3f} ms; amplitude ratio {X[:, 2].min():.2f} to {X[:, 2].max():.2f}")
fig, ax = plt.subplots(1, 2, figsize=(8, 3))
lfr = CLUSTERS[("pre-cue", False)]
ax[0].scatter(X[:, 1], X[:, 0], c=np.where(lfr, "k", "r"), s=8)
ax[0].set(xlabel="half duration (ms)", ylabel="baseline rate (spikes/s)")
ax[1].scatter(X[:, 2], X[:, 0], c=np.where(lfr, "k", "r"), s=8)
ax[1].set(xlabel="amplitude ratio")
plt.tight_layout()
plt.show()
print("all points shown; red = HFR cluster")

# %% [markdown]
# ### onset-population
#
# > 29 neurons (from 5 of 6 rats, about 12% of all) increase firing in the first 1 s of danger,
# > uncertainty or safety over the 2 s pre-cue baseline, and all of them are in the LFR cluster.
#
# Criterion: the Methods screen (paired two-tailed t-test over a cue's trials, raw rate in the 2 s
# before onset against the first 1 s, each cue, p < 0.017, cue higher), uncertainty collapsed;
# count 29 +- 2.9, five rats, all in the LFR cluster of fig1e (reading it matched on).

# %% tags=["claim:onset-population"]
ONSET = [k for k, u in enumerate(units) if pag.screen(u, 0.0, 1.0)]
print("Onset neurons:", len(ONSET), "| rats:", sorted({units[k]["rat"] for k in ONSET}))
print("per rat:", pd.Series([units[k]["rat"] for k in ONSET]).value_counts().sort_index().to_dict())
for key, lfr in CLUSTERS.items():
    print(f"in LFR cluster under reading {key}: {int(lfr[ONSET].sum())} of {len(ONSET)}")
onset_floor = [k for k, u in enumerate(units) if pag.screen(u, 0.0, 1.0, floor_baseline=True)]
print("variant, baseline rate rounded down as in cubeScript.m:", len(onset_floor), "neurons from",
      len({units[k]["rat"] for k in onset_floor}), "rats")
DUP_UNITS = {(d[0], d[1]) for d in dups} | {(d[0], d[2]) for d in dups}
print("Onset neurons in a pair sharing spikes (data check):",
      [units[k]["file"] for k in ONSET if (units[k]["session"], units[k]["unit"]) in DUP_UNITS])

# %% [markdown]
# ### ramping-population
#
# > Of the remaining neurons, 17 increase firing over baseline in the last 1 s of at least one
# > cue; three are in the HFR cluster, and the other 14 (from 4 of 6 rats, about 6%) are the
# > Ramping population.
#
# Criterion: the same test on the last 1 s, on the neurons that are not Onset neurons; counts 17
# +- 1.7, 3 +- 0.3, 14 +- 1.4, and four rats.

# %% tags=["claim:ramping-population"]
LATE = [k for k, u in enumerate(units) if k not in ONSET and pag.screen(u, 9.0, 10.0)]
print("late-responsive neurons:", len(LATE))
for key, lfr in CLUSTERS.items():
    r = [k for k in LATE if lfr[k]]
    print(f"cluster reading {key}: HFR {len(LATE) - len(r)}, LFR (Ramping) {len(r)} from rats {sorted({units[k]['rat'] for k in r})}")
LFR = CLUSTERS[("pre-cue", False)]
RAMP = [k for k in LATE if LFR[k]]
HFR_LATE = [k for k in LATE if not LFR[k]]
print("Ramping per rat:", pd.Series([units[k]["rat"] for k in RAMP]).value_counts().sort_index().to_dict())
late_floor = [k for k, u in enumerate(units) if k not in onset_floor and pag.screen(u, 9.0, 10.0, floor_baseline=True)]
print("variant, baseline rounded down:", len(late_floor), "late-responsive")
print("Ramping neurons in a pair sharing spikes:",
      [units[k]["file"] for k in RAMP if (units[k]["session"], units[k]["unit"]) in DUP_UNITS])
EOF
cat $TMPDIR/build/p1.py $TMPDIR/build/p2.py $TMPDIR/build/p3.py > $TMPDIR/build/dev.py; cd $TMPDIR && . wv/bin/activate && cd entries/wright-2019 && PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/build/dev.py 2>&1 | sed -n '/^ baseline  scaled/,$p'
```

```
Wed Nov 11 10:33:52 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && . wv/bin/activate && cd entries/wright-2019 && PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/build/dev.py 2>&1 | tail -30
```

```
10 zero     trial mean -0.602 -0.671 -0.301 5.63e-10 8.61e-13  0.0044 -0.764 8.02e-52
         10  nan     trial mean -0.654  -0.68 -0.302 4.98e-12 3.13e-13 0.00431 -0.767 1.76e-52
         20  one     trial mean -0.704 -0.721 -0.345    2e-14 2.35e-15 0.00099 -0.785 1.84e-56
         20  one ratio of means -0.733 -0.748 -0.336 4.64e-16 5.31e-17 0.00139 -0.788 3.73e-57
         20 zero     trial mean -0.685 -0.716 -0.342 1.85e-13 4.73e-15 0.00113 -0.783 5.22e-56
         20  nan     trial mean -0.702 -0.719 -0.343 2.52e-14 3.13e-15 0.00109 -0.785 2.63e-56
baseline  scaled  LFR  HFR  F_rate   p_rate  F_halfdur  p_halfdur  F_ampratio  p_ampratio  rate_LFR  rate_HFR
 pre-cue   False  197   48     835 1.42e-80    0.00162      0.968       0.437       0.509      14.9      92.8
 pre-cue    True  198   47     824 5.16e-80      0.021      0.885        1.47       0.227      15.2      93.5
 session   False  194   51     903 8.45e-84     0.0452      0.832       0.754       0.386      4.67      28.8
 session    True  194   51     903 8.45e-84     0.0452      0.832       0.754       0.386      4.67      28.8

feature ranges: baseline rate 0.06 to 169.9 spikes/s; half duration 0.037 to 0.287 ms; amplitude ratio 0.02 to 1.00
all points shown; red = HFR cluster
Onset neurons: 29 | rats: ['dr01', 'dr02', 'rf02', 'rf03', 'rf08']
per rat: {'dr01': 10, 'dr02': 4, 'rf02': 4, 'rf03': 10, 'rf08': 1}
in LFR cluster under reading ('pre-cue', False): 29 of 29
in LFR cluster under reading ('pre-cue', True): 29 of 29
in LFR cluster under reading ('session', False): 29 of 29
in LFR cluster under reading ('session', True): 29 of 29
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/build/p4.py <<'EOF'
# %% [markdown]
# ## Population firing during the cue
#
# Z-scored 100 ms firing (Methods, Z-score normalization, paragraph 1): 320 bins from 10 s before
# onset to 12 s after offset; bin i covers (-10 + 0.1 i, -10 + 0.1 (i + 1)] s from onset. The
# ANOVAs use the 110 bins from 1 s before onset to cue offset (bins 90 to 199). Interval Z
# firing per trial (paragraph 2) under readings a (trial's own baseline, the reading the
# Methods table fixes) and b (trial type's mean baseline) of detail 4.

# %%
Z100 = {k: pag.population_z100(units[k]) for k in ONSET + RAMP}
CUE_BINS = slice(90, 200)


def zcube(ks, bins=CUE_BINS, cues="DUS"):
    return np.array([[Z100[k][c][bins] for c in cues] for k in ks])


def cue_means(ks, a, b, baseline="trial"):
    """Per neuron, mean interval Z firing over each cue's trials (uncertainty collapsed)."""
    out = []
    for k in ks:
        z = pag.interval_z(units[k], a, b, baseline)
        out.append([z[np.isin(units[k]["types"], ts)].mean() for ts in CUES.values()])
    return pd.DataFrame(out, columns=list("DUS"), index=[units[k]["file"] for k in ks])


def by_rat(ks, df):
    return df.assign(rat=[units[k]["rat"] for k in ks]).groupby("rat").agg(["mean"]).round(2).assign(
        n=pd.Series([units[k]["rat"] for k in ks]).value_counts())


def fmt_anova(res):
    return "; ".join(f"{k}: F({v[1]},{v[2]}) = {v[0]:.2f}, p = {v[3]:.2g}" for k, v in res.items())


def paired(df, a, b):
    r = stats.ttest_rel(df[a], df[b])
    return r.statistic, r.pvalue

# %% [markdown]
# ### fig2a-onset-anova
#
# > Onset population firing (100 ms bins, 1 s before to the end of the cue) shows main effects
# > of cue and bin and a cue x bin interaction.
#
# Criterion: repeated-measures ANOVA over the 29 Onset neurons, both main effects and the
# interaction at p < 0.01.

# %% tags=["claim:fig2a-onset-anova"]
Y = zcube(ONSET)
print("Onset:", fmt_anova(pag.rm_anova(Y, ("cue", "bin"))))
print(f"Z range plotted: {Y.mean(0).min():.2f} to {Y.mean(0).max():.2f}")
t = np.arange(-1, 10, 0.1) + 0.1
fig, ax = plt.subplots(1, 2, figsize=(9, 3), sharey=False)
for i, (c, col) in enumerate(zip("DUS", "rmb")):
    ax[0].plot(t, Y.mean(0)[i], col, label=c)
ax[0].set(title="Onset (n = %d)" % len(ONSET), xlabel="s from cue onset", ylabel="Z firing")
ax[0].legend()
YR = zcube(RAMP)
for i, (c, col) in enumerate(zip("DUS", "rmb")):
    ax[1].plot(t, YR.mean(0)[i], col)
ax[1].set(title="Ramping (n = %d)" % len(RAMP), xlabel="s from cue onset")
plt.tight_layout()
plt.show()
print(f"Ramping Z range plotted: {YR.mean(0).min():.2f} to {YR.mean(0).max():.2f}; all points within the axes")

# %% [markdown]
# ### fig2b-onset-first-interval
#
# > In the first 1 s cue interval Onset neurons fire more to danger than to uncertainty; firing to
# > uncertainty is numerically but not significantly above safety, while an ANOVA over the first
# > 5 s of uncertainty and safety shows a cue x bin interaction.
#
# Criterion: danger > uncertainty by paired two-tailed t-test at p < 0.05; uncertainty above
# safety in mean with p >= 0.05; the ANOVA of 100 ms data for uncertainty and safety, 60 bins
# (1 s before onset to 5 s), with a cue x bin interaction at p < 0.05.

# %% tags=["claim:fig2b-onset-first-interval"]
for bl in ("trial", "type"):
    m = cue_means(ONSET, 0, 1, bl)
    print(f"Z baseline {bl}: means D {m.D.mean():.2f}, U {m.U.mean():.2f}, S {m.S.mean():.2f}; "
          "D vs U t(%d) = %.2f, p = %.3g; U vs S t = %.2f, p = %.3g" % ((len(m) - 1,) + paired(m, "D", "U") + paired(m, "U", "S")))
print("ANOVA U and S, 60 bins:", fmt_anova(pag.rm_anova(zcube(ONSET, slice(90, 150), "US"), ("cue", "bin"))))
print("by rat (trial baseline):\n", by_rat(ONSET, cue_means(ONSET, 0, 1)).to_string())

# %% [markdown]
# ### fig2b-onset-last-interval
#
# > Differential firing of Onset neurons is absent in the last 1 s cue interval, for danger
# > against uncertainty and uncertainty against safety.
#
# Criterion (absence): paired two-tailed t-tests at p < 0.05 on last-interval Z firing; reproduced
# when neither pair differs.

# %% tags=["claim:fig2b-onset-last-interval"]
for bl in ("trial", "type"):
    m = cue_means(ONSET, 9, 10, bl)
    d1, d2 = m.D - m.U, m.U - m.S
    print(f"Z baseline {bl}: means D {m.D.mean():.2f}, U {m.U.mean():.2f}, S {m.S.mean():.2f}; "
          "D vs U t = %.2f, p = %.3g (mean difference %.2f, dz %.2f); U vs S t = %.2f, p = %.3g (mean difference %.2f, dz %.2f)"
          % (*paired(m, "D", "U"), d1.mean(), d1.mean() / d1.std(ddof=1), *paired(m, "U", "S"), d2.mean(), d2.mean() / d2.std(ddof=1)))

# %% [markdown]
# ### fig2c-ramping-anova
#
# > Ramping population firing (100 ms bins over the cue) shows main effects of cue and bin and a
# > cue x bin interaction, with ramping greatest to danger, intermediate to uncertainty and absent
# > to safety.
#
# Criterion: as fig2a over the 14 Ramping neurons, all effects at p < 0.01, and the mean Z firing
# of the last 1 s orders danger > uncertainty > safety.

# %% tags=["claim:fig2c-ramping-anova"]
print("Ramping:", fmt_anova(pag.rm_anova(YR, ("cue", "bin"))))
last = YR[:, :, -10:].mean(2).mean(0)
print("mean Z (100 ms bins) in the last 1 s: D %.2f, U %.2f, S %.2f" % tuple(last))
print("mean Z (100 ms bins) 1 s before onset: D %.2f, U %.2f, S %.2f" % tuple(YR[:, :, :10].mean(2).mean(0)))

# %% [markdown]
# ### fig2d-ramping-first-interval
#
# > Ramping neurons show no differential firing in the first 1 s cue interval.
#
# Criterion (absence): paired two-tailed t-tests at p < 0.05 on first-interval Z firing.

# %% tags=["claim:fig2d-ramping-first-interval"]
for bl in ("trial", "type"):
    m = cue_means(RAMP, 0, 1, bl)
    d1, d2 = m.D - m.U, m.U - m.S
    print(f"Z baseline {bl}: means D {m.D.mean():.2f}, U {m.U.mean():.2f}, S {m.S.mean():.2f}; "
          "D vs U t(%d) = %.2f, p = %.3g (difference %.2f); U vs S t = %.2f, p = %.3g (difference %.2f)"
          % (len(m) - 1, *paired(m, "D", "U"), d1.mean(), *paired(m, "U", "S"), d2.mean()))

# %% [markdown]
# ### fig2d-ramping-last-interval
#
# > In the last 1 s cue interval Ramping neurons fire more to danger than to uncertainty and more
# > to uncertainty than to safety.
#
# Criterion: both differences significant by paired two-tailed t-tests at p < 0.05 in the stated
# direction (readings of detail 4).

# %% tags=["claim:fig2d-ramping-last-interval"]
for bl in ("trial", "type"):
    m = cue_means(RAMP, 9, 10, bl)
    print(f"Z baseline {bl}: means D {m.D.mean():.2f}, U {m.U.mean():.2f}, S {m.S.mean():.2f}; "
          "D vs U t(%d) = %.2f, p = %.3g; U vs S t = %.2f, p = %.3g" % (len(m) - 1, *paired(m, "D", "U"), *paired(m, "U", "S")))
print("by rat (trial baseline):\n", by_rat(RAMP, cue_means(RAMP, 9, 10)).to_string())

# %% [markdown]
# ### fig2e-departure-times
#
# > Ramping population firing departs from safety earlier for danger (2.8 s after cue onset at
# > p < 0.05, 5.8 s with Bonferroni correction) than for uncertainty (5.7 s, 6.5 s).
#
# Criterion: 1 s windows from cue onset in 100 ms steps; paired two-tailed t-test over the 14
# Ramping neurons of danger (or uncertainty) against safety; departure is the first window with p
# < 0.05 (or p < 0.00025). Readings of the measure: (a) mean of the 100 ms Z bins in the window;
# (b) interval Z firing of the window. Readings of the time: window start or end. Windows start
# at 0.0 to 9.9 s (100 per comparison, 0.05/200).

# %% tags=["claim:fig2e-departure-times"]
STARTS = np.round(np.arange(0, 10, 0.1), 1)


def window_firing(ks, measure):
    """neurons x cue (D, U, S) x window."""
    if measure == "a":
        return np.array([[[Z100[k][c][100 + int(round(s * 10)): 110 + int(round(s * 10))].mean() for s in STARTS]
                          for c in "DUS"] for k in ks])
    out = np.empty((len(ks), 3, len(STARTS)))
    for j, s in enumerate(STARTS):
        m = cue_means(ks, s, s + 1).to_numpy()
        out[:, :, j] = m
    return out


WF = {m: window_firing(RAMP, m) for m in "ab"}
rows, DEP = [], {}
for meas, W in WF.items():
    for ci, c in ((0, "D"), (1, "U")):
        r = stats.ttest_rel(W[:, ci], W[:, 2], axis=0)
        for thr in (0.05, 0.00025):
            hit = np.where(r.pvalue < thr)[0]
            j = hit[0] if len(hit) else None
            DEP[(meas, c, thr)] = j
            rows.append(dict(measure=meas, cue=c, threshold=thr, start=STARTS[j] if j is not None else np.nan,
                             end=STARTS[j] + 1 if j is not None else np.nan,
                             t_at_departure=r.statistic[j] if j is not None else np.nan,
                             windows_below=len(hit)))
dep = pd.DataFrame(rows)
print(dep.to_string(index=False))
EXPECT = {("D", 0.05): 2.8, ("D", 0.00025): 5.8, ("U", 0.05): 5.7, ("U", 0.00025): 6.5}
for meas in "ab":
    for when in ("start", "end"):
        d = dep[dep.measure == meas].set_index(["cue", "threshold"])[when]
        ok = all(abs(d[k] - v) <= 0.1 * v + 1e-9 for k, v in EXPECT.items())
        print(f"measure {meas}, time = window {when}: " + ", ".join(f"{k[0]} p<{k[1]} {d[k]:.1f} s" for k in EXPECT) + f" -> all within 10%: {ok}")
fig, ax = plt.subplots(figsize=(5, 3))
for ci, col in ((0, "r"), (1, "m")):
    ax.semilogy(STARTS, stats.ttest_rel(WF["a"][:, ci], WF["a"][:, 2], axis=0).pvalue, col)
ax.axhline(0.05, ls=":", c="k")
ax.set(xlabel="window start (s from onset)", ylabel="p, measure a")
plt.show()

# %% [markdown]
# ### fig2e-rate-no-difference
#
# > The rate of firing increase from the departure window to the last 1 s window does not differ
# > between danger and uncertainty, so the earlier departure, not a faster rise, separates them.
#
# Criterion (absence): per Ramping neuron and cue, (firing in the last 1 s window minus firing in
# the cue's departure window at p < 0.05) divided by the time between the two windows; paired
# t-test at p < 0.05, under the reading fig2e-departure-times matched on (every reading if none).

# %% tags=["claim:fig2e-rate-no-difference"]
for meas, W in WF.items():
    jd, ju = DEP[(meas, "D", 0.05)], DEP[(meas, "U", 0.05)]
    last = len(STARTS) - 10   # window 9.0 to 10.0 s
    if jd is None or ju is None:
        print(meas, "no departure")
        continue
    rd = (W[:, 0, last] - W[:, 0, jd]) / (STARTS[last] - STARTS[jd])
    ru = (W[:, 1, last] - W[:, 1, ju]) / (STARTS[last] - STARTS[ju])
    r = stats.ttest_rel(rd, ru)
    print(f"measure {meas}: departure D {STARTS[jd]} s, U {STARTS[ju]} s; rate D {rd.mean():.3f} +- {rd.std(ddof=1) / np.sqrt(len(rd)):.3f}, "
          f"U {ru.mean():.3f} +- {ru.std(ddof=1) / np.sqrt(len(ru)):.3f} Z/s; t({len(rd) - 1}) = {r.statistic:.2f}, p = {r.pvalue:.3g}")

# %% [markdown]
# ### fig2s1-single-trial
#
# > The population patterns hold trial by trial. Onset population firing in the first 1 s exceeds
# > baseline on every individual trial of every cue, and Ramping population firing in the last 1 s
# > exceeds baseline on danger and uncertainty trials but not safety trials.
#
# Criterion: per trial position within each type (D 1-6, US 1-6, UO 1-10, S 1-10), the population
# mean raw rate in the interval against that of the 2 s before onset. Onset exceeds at all 32
# positions; Ramping at all 22 danger and uncertainty positions and at no more than 5 of the 10
# safety positions.

# %% tags=["claim:fig2s1-single-trial"]
def per_position(ks, a, b):
    rows = []
    for t in pag.TYPES:
        n = int((units[ks[0]]["types"] == t).sum())
        for i in range(n):
            cue = np.mean([pag.interval_rate(units[k], a, b)[units[k]["types"] == t][i] for k in ks])
            base = np.mean([pag.interval_rate(units[k], -2, 0)[units[k]["types"] == t][i] for k in ks])
            rows.append(dict(type=t, position=i + 1, interval=cue, baseline=base, above=cue > base))
    return pd.DataFrame(rows)


po = per_position(ONSET, 0, 1)
pr = per_position(RAMP, 9, 10)
print("Onset, first 1 s: positions above baseline by type", po.groupby("type").above.agg(["sum", "size"]).to_dict("index"))
print("Ramping, last 1 s: positions above baseline by type", pr.groupby("type").above.agg(["sum", "size"]).to_dict("index"))
print("Ramping safety positions (interval - baseline, spikes/s):", np.round((pr.interval - pr.baseline)[pr.type == "S"].values, 2).tolist())
print("Onset smallest margin (spikes/s): %.2f" % (po.interval - po.baseline).min())
EOF
cat $TMPDIR/build/p1.py $TMPDIR/build/p2.py $TMPDIR/build/p3.py $TMPDIR/build/p4.py > $TMPDIR/build/dev.py; cd $TMPDIR && . wv/bin/activate && cd entries/wright-2019 && PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/build/dev.py 2>&1 | sed -n '/^Onset: cue/,$p'
```

```
Onset: cue: F(2,56) = 8.64, p = 0.00054; bin: F(109,3052) = 14.19, p = 1.8e-197; cuexbin: F(218,6104) = 1.89, p = 1.6e-13
Z range plotted: -0.50 to 4.28
Ramping Z range plotted: -0.99 to 2.67; all points within the axes
Z baseline trial: means D 0.63, U -0.09, S -0.23; D vs U t(28) = 5.05, p = 2.45e-05; U vs S t = 1.36, p = 0.185
Z baseline type: means D 0.61, U -0.09, S -0.23; D vs U t(28) = 5.06, p = 2.38e-05; U vs S t = 1.34, p = 0.192
ANOVA U and S, 60 bins: cue: F(1,28) = 2.31, p = 0.14; bin: F(59,1652) = 16.30, p = 1.6e-124; cuexbin: F(59,1652) = 1.41, p = 0.024
by rat (trial baseline):
          D     U     S   n
      mean  mean  mean    
rat                       
dr01  0.60  0.06 -0.46  10
dr02  0.21  0.05 -0.20   4
rf02  1.30 -0.25 -0.37   4
rf03  0.55 -0.23  0.04  10
rf08  0.81 -0.13 -0.27   1
Z baseline trial: means D 0.21, U -0.03, S -0.09; D vs U t = 1.94, p = 0.0619 (mean difference 0.24, dz 0.36); U vs S t = 0.58, p = 0.568 (mean difference 0.06, dz 0.11)
Z baseline type: means D 0.21, U -0.03, S -0.09; D vs U t = 1.82, p = 0.0795 (mean difference 0.24, dz 0.34); U vs S t = 0.50, p = 0.618 (mean difference 0.06, dz 0.09)
Ramping: cue: F(2,26) = 32.10, p = 9.5e-08; bin: F(109,1417) = 12.29, p = 2.4e-139; cuexbin: F(218,2834) = 4.29, p = 1.9e-73
mean Z (100 ms bins) in the last 1 s: D 1.93, U 1.20, S -0.10
mean Z (100 ms bins) 1 s before onset: D -0.31, U -0.31, S -0.35
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat > $TMPDIR/build/p5.py <<'EOF'
# %% [markdown]
# ### fig2s2-nose-poke-cessation
#
# > Onset and Ramping firing is not driven by nose poke cessation. Across neurons, firing to
# > danger (Onset first interval, Ramping last interval) is uncorrelated with firing to the first
# > second of an ITI poke cessation and is consistently greater.
#
# Criterion: cessation events are ITI pokes followed by at least 2 s without a poke; -1 is the
# 1 s interval of the poke, +1 the first no-poke second. Readings of the ITI: (a) outside cue,
# delay and shock (onset to 12.5 s after it); (b) also excluding the 10 s after cue offset (onset
# to 20 s after it). Readings of the measure: (a) raw rates (danger interval, cessation +1);
# (b) differential (danger interval minus its 2 s pre-cue baseline; +1 minus -1). Reproduced when,
# under one reading, the Pearson correlation across neurons has p >= 0.05 and a two-sided sign
# test finds danger greater at p < 0.05, for both populations. Here the -1 interval is the second
# that ends at the poke, (t - 1, t], and +1 is (t, t + 1] (a reading of the legend; the
# cessation window (t, t + 2] must hold no poke, and (t - 1, t + 2] must lie in the ITI).

# %% tags=["claim:fig2s2-nose-poke-cessation"]
def cessation_times(u, excl_after):
    p = u["pokes"]
    nxt = np.r_[p[1:], np.inf]
    cand = p[(nxt - p) > 2.0]
    on = u["onsets"]
    ok = np.ones(len(cand), bool)
    for t0 in on:
        ok &= ~((cand + 2.0 > t0) & (cand - 1.0 <= t0 + excl_after))
    ok &= (cand - 1.0 > u["spikes"][0]) & (cand + 2.0 < u["spikes"][-1])
    return cand[ok]


def rate_around(spk, times, a, b):
    idx_a = np.searchsorted(spk, times + a, side="right")
    idx_b = np.searchsorted(spk, times + b, side="right")
    return (idx_b - idx_a) / (b - a)


rows = []
for name, ks, (a, b) in (("Onset", ONSET, (0, 1)), ("Ramping", RAMP, (9, 10))):
    for iti, excl in (("a", 12.5), ("b", 20.0)):
        ev = {k: cessation_times(units[k], excl) for k in ks}
        for meas in "ab":
            dg, cs = [], []
            for k in ks:
                u = units[k]
                d = pag.interval_rate(u, a, b)[u["types"] == "D"]
                c1 = rate_around(u["spikes"], ev[k], 0, 1)
                if meas == "a":
                    dg.append(d.mean())
                    cs.append(c1.mean())
                else:
                    dg.append((d - pag.interval_rate(u, -2, 0)[u["types"] == "D"]).mean())
                    cs.append((c1 - rate_around(u["spikes"], ev[k], -1, 0)).mean())
            dg, cs = np.array(dg), np.array(cs)
            r = stats.pearsonr(dg, cs)
            k_, n_, ps = pag.sign_test(dg, cs)
            rows.append(dict(population=name, iti=iti, measure=meas, events_median=int(np.median([len(e) for e in ev.values()])),
                             r=r[0], R2=r[0] ** 2, p_r=r[1], danger_greater=f"{k_}/{n_}", p_sign=ps,
                             danger_mean=dg.mean(), cessation_mean=cs.mean()))
print(pd.DataFrame(rows).to_string(index=False, float_format=lambda x: f"{x:.3g}"))

# %% [markdown]
# ### fig3-onset-ramping-independent
#
# > In the four sessions with an Onset and a Ramping neuron recorded together, trial by trial
# > firing of the two is not negatively related; a significant negative beta appears for one
# > interval of one pair only.
#
# Criterion: four pairs; per pair and 1 s cue interval, regression with constant over the 32
# trials of the Onset neuron's interval Z firing on the Ramping neuron's. Reproduced when at most
# two of the 40 regressions give a negative beta with p < 0.05.

# %% tags=["claim:fig3-onset-ramping-independent"]
PAIRS = [(i, j) for i in ONSET for j in RAMP if units[i]["session"] == units[j]["session"]]
print("Onset-Ramping pairs in the same session:", len(PAIRS), [(units[i]["file"], units[j]["unit"]) for i, j in PAIRS])
for bl in ("trial", "type"):
    res = []
    for i, j in PAIRS:
        for k in range(10):
            b, p = pag.ols(pag.interval_z(units[i], k, k + 1, bl), pag.interval_z(units[j], k, k + 1, bl))
            res.append(dict(pair=units[i]["session"], interval=k + 1, beta=b[0], p=p[0]))
    res = pd.DataFrame(res)
    neg = res[(res.beta < 0) & (res.p < 0.05)]
    pos = res[(res.beta > 0) & (res.p < 0.05)]
    print(f"Z baseline {bl}: {len(res)} regressions; negative beta at p < 0.05: {len(neg)} {neg[['pair', 'interval']].values.tolist()}; "
          f"positive at p < 0.05: {len(pos)}; beta range {res.beta.min():.2f} to {res.beta.max():.2f}")

# %% [markdown]
# ## Single-unit biases and patterns
#
# ### fig4abc-onset-single-unit-biases
#
# > In the first 1 s interval, Onset single units' danger and uncertainty firing are correlated
# > and biased to danger; uncertainty and safety firing are correlated but the bias to
# > uncertainty is not significant; danger firing is biased to the first over the last interval,
# > with no correlation between them.
#
# Criterion: per Onset neuron, mean interval Z firing per cue; Pearson correlation and two-sided
# sign test per panel. A: correlation p < 0.05 and a danger bias; B: correlation p < 0.05 and sign
# test p >= 0.05; C: a first-interval bias and correlation p >= 0.05. Partially when two of three.

# %% tags=["claim:fig4abc-onset-single-unit-biases"]
def bias_panels(ks, a, b, first_last):
    out = {}
    for bl in ("trial", "type"):
        m = cue_means(ks, a, b, bl)
        f = cue_means(ks, 0, 1, bl).D
        l = cue_means(ks, 9, 10, bl).D
        rows = []
        for panel, x, y in (("D vs U", m.D, m.U), ("U vs S", m.U, m.S),
                            ("D first vs last" if first_last == "first" else "D last vs first",
                             f if first_last == "first" else l, l if first_last == "first" else f)):
            r = stats.pearsonr(x, y)
            k_, n_, ps = pag.sign_test(x, y)
            rows.append(dict(z_baseline=bl, panel=panel, r=r[0], R2=r[0] ** 2, p_r=r[1], first_greater=f"{k_}/{n_}", p_sign=ps))
        out[bl] = pd.DataFrame(rows)
    return pd.concat(out.values())


print(bias_panels(ONSET, 0, 1, "first").to_string(index=False, float_format=lambda x: f"{x:.3g}"))

# %% [markdown]
# ### fig4d-onset-patterns
#
# > The most common pattern of Onset neurons in the first 1 s interval is danger > uncertainty >
# > safety (14 neurons), the only pattern with more neurons than expected by chance.
#
# Criterion: each neuron placed by the order of its mean interval Z firing to the three cues;
# chance from 1000 shuffles, (a) the three values permuted within each neuron, or (b) each cue's
# values permuted across neurons; "above chance" (a) above the 95th percentile of the shuffled
# counts, or (b) above Q3 + 1.5 IQR. Judged on the four categories of the Methods (DUS, DSU, SUD,
# UDS); all six orders shown as a variant. Count 14 +- 1.4, the largest, the only one above chance.

# %% tags=["claim:fig4d-onset-patterns"]
ORDERS = ["DUS", "DSU", "SUD", "UDS", "USD", "SDU"]


def order_of(v):
    return "".join(np.array(list("DUS"))[np.argsort(-v, kind="stable")])


def patterns(ks, a, b, seed):
    rng = np.random.default_rng(seed)
    out = []
    for bl in ("trial", "type"):
        M = cue_means(ks, a, b, bl).to_numpy()
        obs = pd.Series([order_of(v) for v in M]).value_counts().reindex(ORDERS, fill_value=0)
        for sh in "ab":
            null = []
            for _ in range(1000):
                if sh == "a":
                    S = np.array([rng.permutation(v) for v in M])
                else:
                    S = np.column_stack([rng.permutation(M[:, c]) for c in range(3)])
                null.append(pd.Series([order_of(v) for v in S]).value_counts().reindex(ORDERS, fill_value=0).values)
            null = np.array(null)
            q1, q3 = np.percentile(null, [25, 75], axis=0)
            p95 = np.percentile(null, 95, axis=0)
            whisk = q3 + 1.5 * (q3 - q1)
            for i, o in enumerate(ORDERS):
                out.append(dict(z_baseline=bl, shuffle=sh, order=o, observed=obs[o], median=np.median(null[:, i]),
                                p95=p95[i], whisker=whisk[i], above_p95=obs[o] > p95[i], above_whisker=obs[o] > whisk[i]))
    return pd.DataFrame(out)


pat_on = patterns(ONSET, 0, 1, seed=4)
print(pat_on.to_string(index=False))


def pattern_verdict(df, target="DUS", four=ORDERS[:4]):
    rows = []
    for (bl, sh), g in df.groupby(["z_baseline", "shuffle"]):
        g4 = g[g.order.isin(four)].set_index("order")
        for rule in ("above_p95", "above_whisker"):
            above = g4.index[g4[rule]].tolist()
            rows.append(dict(z_baseline=bl, shuffle=sh, rule=rule, count=int(g4.loc[target, "observed"]),
                             largest=g4.observed.idxmax() == target and (g4.observed == g4.observed.max()).sum() == 1,
                             above_chance=above))
    return pd.DataFrame(rows)


print(pattern_verdict(pat_on).to_string(index=False))

# %% [markdown]
# ### fig4efg-ramping-single-unit-biases
#
# > In the last 1 s interval, Ramping single units' danger and uncertainty firing are correlated
# > and biased to danger; uncertainty and safety firing are not correlated but are biased to
# > uncertainty; danger firing is biased to the last over the first interval, with no correlation
# > between them.
#
# Criterion: as fig4abc on the 14 Ramping neurons and the last interval. E: correlation p < 0.05
# and a danger bias; F: correlation p >= 0.05 and an uncertainty bias; G: a last-interval bias and
# correlation p >= 0.05. Partially when two of three hold.

# %% tags=["claim:fig4efg-ramping-single-unit-biases"]
print(bias_panels(RAMP, 9, 10, "last").to_string(index=False, float_format=lambda x: f"{x:.3g}"))

# %% [markdown]
# ### fig4h-ramping-patterns
#
# > The most common pattern of Ramping neurons in the last 1 s interval is danger > uncertainty >
# > safety (11 neurons), the only pattern above chance.
#
# Criterion: as fig4d, on the 14 Ramping neurons and the last interval; count 11 +- 1.1.

# %% tags=["claim:fig4h-ramping-patterns"]
pat_ra = patterns(RAMP, 9, 10, seed=8)
print(pat_ra.to_string(index=False))
print(pattern_verdict(pat_ra).to_string(index=False))

# %% [markdown]
# ### fig1s5-hfr-units
#
# > The three late-responsive neurons of the HFR cluster each fire most to danger in the last 1 s
# > cue interval.
#
# Criterion: for each, mean last-interval firing (raw rate, and mean interval Z as a second
# reading) higher for danger than for uncertainty and safety; reproduced when this holds for all
# three under one reading.

# %% tags=["claim:fig1s5-hfr-units"]
print("HFR late-responsive neurons:", len(HFR_LATE))
for k in HFR_LATE:
    u = units[k]
    raw = {c: pag.interval_rate(u, 9, 10)[np.isin(u["types"], ts)].mean() for c, ts in CUES.items()}
    z = {c: pag.interval_z(u, 9, 10)[np.isin(u["types"], ts)].mean() for c, ts in CUES.items()}
    print(f"{u['file']} ({u['rat']}): raw D {raw['D']:.1f}, U {raw['U']:.1f}, S {raw['S']:.1f} spikes/s "
          f"-> danger highest {raw['D'] > max(raw['U'], raw['S'])}; Z D {z['D']:.2f}, U {z['U']:.2f}, S {z['S']:.2f} "
          f"-> danger highest {z['D'] > max(z['U'], z['S'])}")
EOF
cat $TMPDIR/build/p1.py $TMPDIR/build/p2.py $TMPDIR/build/p3.py $TMPDIR/build/p4.py $TMPDIR/build/p5.py > $TMPDIR/build/dev.py; cd $TMPDIR && . wv/bin/activate && cd entries/wright-2019 && PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/build/dev.py 2>&1 | sed -n '/^population iti/,$p'
```

```
Wed Nov 11 10:38:14 UTC 2026
population iti measure  events_median       r       R2      p_r danger_greater   p_sign  danger_mean  cessation_mean
     Onset   a       a            207   0.823    0.678 4.11e-08          28/29 1.12e-07         31.2            14.3
     Onset   a       b            207 -0.0241 0.000579    0.901          26/29 1.52e-05         17.3           0.706
     Onset   b       a            166    0.82    0.672 5.38e-08          28/29 1.12e-07         31.2              14
     Onset   b       b            166 -0.0606  0.00368    0.755          26/29 1.52e-05         17.3           0.662
   Ramping   a       a            241   0.786    0.618 0.000861          13/14  0.00183         28.5            14.2
   Ramping   a       b            241   0.483    0.233   0.0803          14/14 0.000122         16.8            2.68
   Ramping   b       a            193   0.781     0.61 0.000974          13/14  0.00183         28.5            13.9
   Ramping   b       b            193   0.505    0.255   0.0655          14/14 0.000122         16.8            2.69
Onset-Ramping pairs in the same session: 3 [('dr01101616epr38aSPK10a.mat', 'SPK14b'), ('dr01102316epr38aSPK05b.mat', 'SPK05a'), ('dr01102316epr38aSPK11a.mat', 'SPK05a')]
Z baseline trial: 30 regressions; negative beta at p < 0.05: 0 []; positive at p < 0.05: 1; beta range -0.33 to 0.42
Z baseline type: 30 regressions; negative beta at p < 0.05: 0 []; positive at p < 0.05: 0; beta range -0.28 to 0.34
z_baseline           panel      r     R2     p_r first_greater  p_sign
     trial          D vs U -0.469   0.22  0.0102         22/29 0.00813
     trial          U vs S -0.549  0.301 0.00205         17/29   0.458
     trial D first vs last  0.341  0.116  0.0704         22/29 0.00813
      type          D vs U -0.418  0.175   0.024         22/29 0.00813
      type          U vs S -0.571  0.327  0.0012         17/29   0.458
      type D first vs last  0.314 0.0985  0.0974         22/29 0.00813
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat > $TMPDIR/build/p6.py <<'EOF'
# %% [markdown]
# ## Single-unit regressions
#
# Per neuron and interval, OLS with a constant over the 32 trials of interval Z firing on interval
# fear, total fear and probability (1.00, 0.375, 0.00) (Methods, Single-unit, linear regression).
# Readings: the poke baseline (interval / total fear) 2 s / 20 s as the Methods table fixes
# (primary, labelled "table"), or 2 s / 2 s and 10 s / 10 s (the claims file's detail 1); 0/0 set
# to 1 (table), 0, or the trial left out (detail 2); Z firing against the trial's own baseline
# (table) or the type's mean (detail 4). That is 18 readings; each claim prints the primary one in
# full and, for every reading, whether its criterion holds.

# %%
POKE_READINGS = {"table": (2.0, 20.0), "2 s": (2.0, 2.0), "10 s": (10.0, 10.0)}
READINGS = [(w, zr, zb) for w in POKE_READINGS for zr in ("one", "zero", "nan") for zb in ("trial", "type")]
PRIMARY = ("table", "one", "trial")
PROB = np.array([pag.PROB[t] for t in units[0]["types"]])
CUE_IV = [(k, k + 1.0) for k in range(10)]
POST_IV = [(10 + 0.5 * k, 10.5 + 0.5 * k) for k in range(10) if k != 4]   # 500 ms, shock (12.0-12.5 s) left out
_cache = {}


def regressors(k, reading, iv):
    key = (k, reading, iv)
    if key not in _cache:
        u = units[k]
        w, zr, zb = reading
        wi, wt = POKE_READINGS[w]
        _cache[key] = dict(z=pag.interval_z(u, iv[0], iv[1], zb), IF=pag.interval_sr(u, iv[0], iv[1], wi, zr),
                           TF=pag.total_sr(u, wt, zr))
    return _cache[key]


def betas(ks, reading, ivs=CUE_IV, regs=("IF", "TF", "P"), prob=None):
    """neurons x intervals x regressors."""
    pr = PROB if prob is None else prob
    out = np.empty((len(ks), len(ivs), len(regs)))
    for i, k in enumerate(ks):
        for j, iv in enumerate(ivs):
            r = regressors(k, reading, iv)
            X = np.column_stack([pr if g == "P" else r[g] for g in regs])
            out[i, j] = pag.ols(r["z"], X)[0]
    return out


def tuning_prob(pu):
    p = PROB.copy()
    p[PROB == 0.375] = pu
    return p


def onesamp(x):
    return stats.ttest_1samp(x, 0.0)


def show_readings(fn):
    """Run a claim's check under every reading; fn returns a dict with a boolean 'holds'."""
    rows = [dict(poke=r[0], zero=r[1], z=r[2], **fn(r)) for r in READINGS]
    df = pd.DataFrame(rows)
    print(df.to_string(index=False, float_format=lambda x: f"{x:.3g}"))
    return df

# %% [markdown]
# ### fig5a-onset-probability-first-interval
#
# > In the first 1 s cue interval the Onset population's probability beta is positive and
# > significant and exceeds both fear betas, neither of which differs from zero.
#
# Criterion: probability beta exceeds each fear beta (paired two-tailed t-tests, p < 0.05), is
# above zero (single-sample t-test, p < 0.005), and neither fear beta differs from zero at p <
# 0.005; 0.05 shown as a variant.

# %% tags=["claim:fig5a-onset-probability-first-interval"]
def check5a(r, verbose=False):
    B = betas(ONSET, r, CUE_IV[:1])[:, 0]
    IF, TF, P = B.T
    tPT, tPI = stats.ttest_rel(P, TF), stats.ttest_rel(P, IF)
    zP, zT, zI = onesamp(P), onesamp(TF), onesamp(IF)
    if verbose:
        print(f"mean betas: interval fear {IF.mean():.3f}, total fear {TF.mean():.3f}, probability {P.mean():.3f} (n = {len(P)})")
        print(f"P vs TF t(28) = {tPT.statistic:.2f}, p = {tPT.pvalue:.3g}; P vs IF t = {tPI.statistic:.2f}, p = {tPI.pvalue:.3g}")
        print(f"against zero: P t = {zP.statistic:.2f}, p = {zP.pvalue:.3g}; TF t = {zT.statistic:.2f}, p = {zT.pvalue:.3g}; IF t = {zI.statistic:.2f}, p = {zI.pvalue:.3g}")
    holds = (tPT.statistic > 0) & (tPT.pvalue < 0.05) & (tPI.statistic > 0) & (tPI.pvalue < 0.05) & (zP.statistic > 0) & (zP.pvalue < 0.005) \
        & (zT.pvalue >= 0.005) & (zI.pvalue >= 0.005)
    return dict(P=P.mean(), TF=TF.mean(), IF=IF.mean(), p_PvTF=tPT.pvalue, p_PvIF=tPI.pvalue, p_P0=zP.pvalue,
                p_TF0=zT.pvalue, p_IF0=zI.pvalue, holds=holds, holds_at_005=holds & (zT.pvalue >= 0.05) & (zI.pvalue >= 0.05))


check5a(PRIMARY, verbose=True)
r5a = show_readings(check5a)
print("by rat, primary reading (mean betas IF, TF, P):")
print(pd.DataFrame(betas(ONSET, PRIMARY, CUE_IV[:1])[:, 0], columns=["IF", "TF", "P"]).assign(rat=[units[k]["rat"] for k in ONSET]).groupby("rat").agg(["mean", "size"]).round(2).to_string())

# %% [markdown]
# ### fig5bc-onset-beta-bias
#
# > Onset single-unit betas are positively biased for threat probability but not for total or
# > interval fear.
#
# Criterion: first-interval betas of the 29 Onset neurons; two-sided sign test of each against
# zero at p < 0.05. Probability biased positive; neither fear regressor (p >= 0.05).

# %% tags=["claim:fig5bc-onset-beta-bias"]
def check5bc(r):
    B = betas(ONSET, r, CUE_IV[:1])[:, 0]
    s = [pag.sign_test(B[:, i]) for i in range(3)]
    holds = (s[2][2] < 0.05) & (s[2][0] > s[2][1] / 2) & (s[0][2] >= 0.05) & (s[1][2] >= 0.05)
    return dict(IF_pos=f"{s[0][0]}/{s[0][1]}", p_IF=s[0][2], TF_pos=f"{s[1][0]}/{s[1][1]}", p_TF=s[1][2],
                P_pos=f"{s[2][0]}/{s[2][1]}", p_P=s[2][2], holds=holds)


r5bc = show_readings(check5bc)

# %% [markdown]
# ### fig5d-onset-all-intervals
#
# > Over the ten 1 s cue intervals, Onset threat probability signaling is highest in the first
# > interval, persists several seconds and diminishes, while total and interval fear account for
# > firing in no interval; an ANOVA shows a main effect of regressor and a regressor x interval
# > interaction.
#
# Criterion: repeated-measures ANOVA (regressor x interval), both effects at p < 0.01; mean
# probability beta largest in the first interval and above zero (p < 0.005) in it and in at least
# one later interval; no fear beta differs from zero at p < 0.005 in any interval.

# %% tags=["claim:fig5d-onset-all-intervals"]
def check5d(r, verbose=False):
    B = betas(ONSET, r)                       # n x 10 x 3
    an = pag.rm_anova(B.transpose(0, 2, 1), ("regressor", "interval"))
    pP = np.array([onesamp(B[:, j, 2]).pvalue for j in range(10)])
    tP = np.array([onesamp(B[:, j, 2]).statistic for j in range(10)])
    pF = np.array([[onesamp(B[:, j, i]).pvalue for j in range(10)] for i in range(2)])
    mP = B[:, :, 2].mean(0)
    if verbose:
        print(fmt_anova(an))
        print("mean probability beta by interval:", np.round(mP, 3).tolist())
        print("p against zero, probability:", [f"{p:.2g}" for p in pP])
        print("smallest p against zero, interval fear %.3g, total fear %.3g" % (pF[0].min(), pF[1].min()))
    holds = (an["regressor"][3] < 0.01) & (an["regressorxinterval"][3] < 0.01) & (mP.argmax() == 0) \
        & (pP[0] < 0.005) & (tP[0] > 0) & np.any((pP[1:] < 0.005) & (tP[1:] > 0)) & (pF.min() >= 0.005)
    return dict(F_reg=an["regressor"][0], p_reg=an["regressor"][3], F_int=an["regressorxinterval"][0],
                p_int=an["regressorxinterval"][3], peak_interval=int(mP.argmax()) + 1,
                P_sig_intervals=int(((pP < 0.005) & (tP > 0)).sum()), min_p_fear=pF.min(), holds=holds)


check5d(PRIMARY, verbose=True)
r5d = show_readings(check5d)

# %% [markdown]
# ### fig5s1-regressor-combinations
#
# > Onset neurons prioritize probability whatever the combination of regressors; a fear beta
# > reaches significance only when total fear is the sole regressor, and even then its relation is
# > weaker than that of probability.
#
# Criterion: regressions over the ten intervals with (A) P + TF, (B) P + IF, (C) IF, (D) TF,
# (E) P. "Significance for fear output": (a) a single-sample t-test of the mean beta against
# zero in any interval at p < 0.005, or (b) the main effect of interval in C to E at p < 0.05.
# Reproduced when, under one reading, no fear regressor is significant in A, B and C, total fear
# is in D, the D beta is below the E beta ("weaker": (a) first-interval means, (b) the largest
# mean over intervals), and A and B each show a main effect of regressor (p < 0.05) with the
# probability beta above the fear beta.

# %% tags=["claim:fig5s1-regressor-combinations"]
COMBOS = {"A": ("P", "TF"), "B": ("P", "IF"), "C": ("IF",), "D": ("TF",), "E": ("P",)}


def combo_check(ks, r, verbose=False):
    out = {}
    Bs = {c: betas(ks, r, regs=g) for c, g in COMBOS.items()}
    sig_a, sig_b = {}, {}
    for c, g in COMBOS.items():
        for i, reg in enumerate(g):
            ps = np.array([onesamp(Bs[c][:, j, i]).pvalue for j in range(10)])
            sig_a[(c, reg)] = bool((ps < 0.005).any())
        if len(g) == 1:
            an = pag.rm_anova(Bs[c][:, :, 0])["A"]
            sig_b[(c, g[0])] = an[3] < 0.05
            out[f"F_int_{c}"] = an[0]
            out[f"p_int_{c}"] = an[3]
    for c in "AB":
        an = pag.rm_anova(Bs[c].transpose(0, 2, 1), ("regressor", "interval"))
        out[f"p_reg_{c}"] = an["regressor"][3]
        out[f"P_above_{c}"] = Bs[c][:, :, 0].mean() > Bs[c][:, :, 1].mean()
    res = {}
    for rd, sig in (("a", sig_a), ("b", sig_b)):
        fearA = sig_a[("A", "TF")] if rd == "a" else False
        fearB = sig_a[("B", "IF")] if rd == "a" else False
        nofear = not fearA and not fearB and not sig[("C", "IF")]
        dsig = sig[("D", "TF")]
        res[rd] = dict(nofear_ABC=nofear, TF_sig_in_D=dsig)
    weaker = {"a": Bs["D"][:, 0, 0].mean() < Bs["E"][:, 0, 0].mean(),
              "b": Bs["D"][:, :, 0].mean(0).max() < Bs["E"][:, :, 0].mean(0).max()}
    AB = all(out[f"p_reg_{c}"] < 0.05 and out[f"P_above_{c}"] for c in "AB")
    holds = {}
    for rd in "ab":
        for wk in "ab":
            holds[f"sig{rd}_weak{wk}"] = res[rd]["nofear_ABC"] and res[rd]["TF_sig_in_D"] and weaker[wk] and AB
    if verbose:
        print("significance reading a (any interval p < 0.005):", {f"{c}:{g}": v for (c, g), v in sig_a.items()})
        print("significance reading b (interval effect p < 0.05):", {f"{c}:{g}": v for (c, g), v in sig_b.items()})
        print("D beta first interval %.3f vs E %.3f; largest D %.3f vs E %.3f" % (
            Bs["D"][:, 0, 0].mean(), Bs["E"][:, 0, 0].mean(), Bs["D"][:, :, 0].mean(0).max(), Bs["E"][:, :, 0].mean(0).max()))
        print({k: (round(v, 4) if isinstance(v, float) else v) for k, v in out.items()})
    return dict(**{k: v for k, v in out.items() if k.startswith("p_")}, AB_ok=AB, **holds,
                holds=any(holds.values()))


combo_check(ONSET, PRIMARY, verbose=True)
r5s1 = show_readings(lambda r: combo_check(ONSET, r))

# %% [markdown]
# ### fig5e-onset-tuning-curve
#
# > Varying the probability assigned to uncertainty from 0 to 1 in 0.125 steps, the Onset
# > population's mean probability beta in the first interval peaks at the actual 0.375, with the
# > flanking values next highest and betas falling off toward the extremes.
#
# Criterion: nine regressions per neuron with all three regressors; mean probability beta over
# the 29 neurons per assignment. Peak at 0.375 and the next two at 0.25 and 0.5; partially when
# the peak holds and the order of the next two differs.

# %% tags=["claim:fig5e-onset-tuning-curve"]
PU = np.arange(0, 1.0001, 0.125)


def tuning(ks, r, iv):
    return np.array([betas(ks, r, [iv], prob=tuning_prob(pu))[:, 0, 2].mean() for pu in PU])


def check_tuning(ks, iv, r, verbose=False):
    t = tuning(ks, r, iv)
    order = PU[np.argsort(-t)]
    if verbose:
        print("mean probability beta by uncertainty assignment:", dict(zip(PU.tolist(), np.round(t, 3).tolist())))
    return dict(peak=order[0], second=order[1], third=order[2],
                holds=(order[0] == 0.375) & (set(order[1:3]) == {0.25, 0.5}))


check_tuning(ONSET, CUE_IV[0], PRIMARY, verbose=True)
r5e = show_readings(lambda r: check_tuning(ONSET, CUE_IV[0], r))

# %% [markdown]
# ### fig5s2-binary-regressor
#
# > Onset firing is better captured by the actual shock probability (uncertainty 0.375) than by
# > a binary regressor equating uncertainty with safety, in the first interval and across the cue.
#
# Criterion: a second set of regressions with the binary regressor (danger 1, uncertainty and
# safety 0) in place of probability; repeated-measures ANOVA on betas with analysis, regressor and
# interval. Reproduced when the analysis x regressor x interval interaction (all ten intervals)
# and the analysis x regressor interaction (first interval) have p < 0.05 and the first-interval
# mean beta is larger for probability than for binary.

# %% tags=["claim:fig5s2-binary-regressor"]
def check5s2(r, verbose=False):
    Bp = betas(ONSET, r)
    Bb = betas(ONSET, r, prob=tuning_prob(0.0))
    Y = np.stack([Bp, Bb], 1).transpose(0, 1, 3, 2)          # n x analysis x regressor x interval
    an = pag.rm_anova(Y, ("analysis", "regressor", "interval"))
    an1 = pag.rm_anova(Y[:, :, :, 0], ("analysis", "regressor"))
    if verbose:
        print("all intervals:", fmt_anova(an))
        print("first interval:", fmt_anova(an1))
        print("first-interval mean beta: probability %.3f, binary %.3f" % (Bp[:, 0, 2].mean(), Bb[:, 0, 2].mean()))
    holds = (an["analysisxregressorxinterval"][3] < 0.05) & (an1["analysisxregressor"][3] < 0.05) & (Bp[:, 0, 2].mean() > Bb[:, 0, 2].mean())
    return dict(F3=an["analysisxregressorxinterval"][0], p3=an["analysisxregressorxinterval"][3],
                F2=an1["analysisxregressor"][0], p2=an1["analysisxregressor"][3],
                P=Bp[:, 0, 2].mean(), binary=Bb[:, 0, 2].mean(), holds=holds)


check5s2(PRIMARY, verbose=True)
r5s2 = show_readings(check5s2)

# %% [markdown]
# ### fig5f-ramping-last-interval
#
# > In the last 1 s cue interval, Ramping probability and total fear betas both exceed the
# > interval fear beta and do not differ from each other.
#
# Criterion: last-interval betas of the 14 Ramping neurons; both comparisons with interval fear
# significant (p < 0.05) in the stated direction, probability against total fear p >= 0.05.

# %% tags=["claim:fig5f-ramping-last-interval"]
def check5f(r, verbose=False):
    B = betas(RAMP, r, CUE_IV[9:])[:, 0]
    IF, TF, P = B.T
    a, b, c = stats.ttest_rel(P, IF), stats.ttest_rel(TF, IF), stats.ttest_rel(P, TF)
    if verbose:
        print(f"mean betas IF {IF.mean():.3f}, TF {TF.mean():.3f}, P {P.mean():.3f}")
        print(f"P vs IF t(13) = {a.statistic:.2f}, p = {a.pvalue:.3g}; TF vs IF t = {b.statistic:.2f}, p = {b.pvalue:.3g}; P vs TF t = {c.statistic:.2f}, p = {c.pvalue:.3g}")
    holds = (a.statistic > 0) & (a.pvalue < 0.05) & (b.statistic > 0) & (b.pvalue < 0.05) & (c.pvalue >= 0.05)
    return dict(IF=IF.mean(), TF=TF.mean(), P=P.mean(), p_PvIF=a.pvalue, p_TFvIF=b.pvalue, p_PvTF=c.pvalue, holds=holds)


check5f(PRIMARY, verbose=True)
r5f = show_readings(check5f)

# %% [markdown]
# ### fig5gh-ramping-beta-bias
#
# > Ramping single-unit betas in the last interval are biased positive for probability and total
# > fear, which are uncorrelated; they are not biased for interval fear, and the probability and
# > interval fear betas are negatively correlated.
#
# Criterion: sign tests against zero (two-sided, p < 0.05) and Pearson correlations (p < 0.05)
# across the 14 neurons. Four parts: P and TF biased positive; their correlation p >= 0.05; IF not
# biased; P and IF correlate negatively. Partially when three of four hold.

# %% tags=["claim:fig5gh-ramping-beta-bias"]
def check5gh(r):
    B = betas(RAMP, r, CUE_IV[9:])[:, 0]
    IF, TF, P = B.T
    sP, sT, sI = pag.sign_test(P), pag.sign_test(TF), pag.sign_test(IF)
    cPT, cPI = stats.pearsonr(P, TF), stats.pearsonr(P, IF)
    parts = [(sP[2] < 0.05) & (sP[0] > sP[1] / 2) & (sT[2] < 0.05) & (sT[0] > sT[1] / 2), cPT[1] >= 0.05,
             sI[2] >= 0.05, (cPI[0] < 0) & (cPI[1] < 0.05)]
    return dict(P_pos=f"{sP[0]}/{sP[1]}", p_P=sP[2], TF_pos=f"{sT[0]}/{sT[1]}", p_TF=sT[2], IF_pos=f"{sI[0]}/{sI[1]}",
                p_IF=sI[2], r_PTF=cPT[0], p_rPTF=cPT[1], r_PIF=cPI[0], p_rPIF=cPI[1], parts_held=int(sum(parts)),
                holds=all(parts))


r5gh = show_readings(check5gh)

# %% [markdown]
# ### fig5i-ramping-all-intervals
#
# > Over all ten cue intervals Ramping neurons prioritize probability (mean beta 0.58, against
# > 0.12 for total fear and -0.03 for interval fear); only the probability beta differs from zero
# > and it exceeds both fear betas, with a main effect of regressor and a regressor x interval
# > interaction.
#
# Criterion: per neuron, the mean of its betas over the ten intervals; means within 0.58 +- 0.14,
# 0.12 +- 0.10, -0.03 +- 0.05 under one reading; ANOVA effects p < 0.01; the probability mean
# differs from zero and exceeds both fear means at p < 0.05; the fear means do not differ from
# zero (p >= 0.05). Partially when the tests hold and a mean is outside tolerance.

# %% tags=["claim:fig5i-ramping-all-intervals"]
def check5i(r, verbose=False):
    B = betas(RAMP, r)
    M = B.mean(1)
    IF, TF, P = M.T
    an = pag.rm_anova(B.transpose(0, 2, 1), ("regressor", "interval"))
    zP, zT, zI = onesamp(P), onesamp(TF), onesamp(IF)
    a, b = stats.ttest_rel(P, TF), stats.ttest_rel(P, IF)
    means = (abs(P.mean() - 0.58) <= 0.14) & (abs(TF.mean() - 0.12) <= 0.10) & (abs(IF.mean() + 0.03) <= 0.05)
    tests = (an["regressor"][3] < 0.01) & (an["regressorxinterval"][3] < 0.01) & (zP.pvalue < 0.05) & (zP.statistic > 0) \
        & (a.statistic > 0) & (a.pvalue < 0.05) & (b.statistic > 0) & (b.pvalue < 0.05) & (zT.pvalue >= 0.05) & (zI.pvalue >= 0.05)
    if verbose:
        print(fmt_anova(an))
        print(f"mean over intervals: P {P.mean():.3f} +- {P.std(ddof=1) / np.sqrt(len(P)):.3f}, TF {TF.mean():.3f} +- {TF.std(ddof=1) / np.sqrt(len(P)):.3f}, "
              f"IF {IF.mean():.3f} +- {IF.std(ddof=1) / np.sqrt(len(P)):.3f}")
        print(f"against zero: P t(13) = {zP.statistic:.2f}, p = {zP.pvalue:.3g}; TF t = {zT.statistic:.2f}, p = {zT.pvalue:.3g}; IF t = {zI.statistic:.2f}, p = {zI.pvalue:.3g}")
        print(f"P vs TF t = {a.statistic:.2f}, p = {a.pvalue:.3g}; P vs IF t = {b.statistic:.2f}, p = {b.pvalue:.3g}")
    return dict(P=P.mean(), TF=TF.mean(), IF=IF.mean(), p_reg=an["regressor"][3], p_int=an["regressorxinterval"][3],
                p_P0=zP.pvalue, p_TF0=zT.pvalue, p_IF0=zI.pvalue, p_PvTF=a.pvalue, p_PvIF=b.pvalue,
                means_ok=means, tests_ok=tests, holds=means & tests)


check5i(PRIMARY, verbose=True)
r5i = show_readings(check5i)

# %% [markdown]
# ### fig5s1-ramping-regressor-combinations
#
# > For Ramping neurons, the prioritization of probability over all ten intervals holds when
# > probability is compared with total fear or interval fear alone, and when each regressor is
# > used in isolation.
#
# Criterion: regressions F (P + TF), G (P + IF), H (IF), I (TF), J (P); per neuron the mean beta
# over the ten intervals. In F and G the probability mean differs from zero (p < 0.05), the fear
# mean does not, probability exceeds fear (paired, p < 0.05), and the ANOVA (regressor x
# interval) has a main effect of regressor (p < 0.05); of H, I and J only J's mean differs from
# zero. Partially when F and G hold and H to J do not.

# %% tags=["claim:fig5s1-ramping-regressor-combinations"]
def check5s1r(r, verbose=False):
    Bs = {c: betas(RAMP, r, regs=g) for c, g in COMBOS.items()}
    fg = []
    out = {}
    for c, name in (("A", "F"), ("B", "G")):
        M = Bs[c].mean(1)
        P, Fe = M[:, 0], M[:, 1]
        an = pag.rm_anova(Bs[c].transpose(0, 2, 1), ("regressor", "interval"))
        zP, zF, d = onesamp(P), onesamp(Fe), stats.ttest_rel(P, Fe)
        ok = (zP.pvalue < 0.05) & (zP.statistic > 0) & (zF.pvalue >= 0.05) & (d.statistic > 0) & (d.pvalue < 0.05) & (an["regressor"][3] < 0.05)
        out.update({f"{name}_P": P.mean(), f"{name}_fear": Fe.mean(), f"{name}_pP0": zP.pvalue, f"{name}_pF0": zF.pvalue,
                    f"{name}_pdiff": d.pvalue, f"{name}_preg": an["regressor"][3]})
        fg.append(ok)
    single = {}
    for c, name in (("C", "H"), ("D", "I"), ("E", "J")):
        m = Bs[c].mean(1)[:, 0]
        z = onesamp(m)
        an = pag.rm_anova(Bs[c][:, :, 0])["A"]
        single[name] = z.pvalue < 0.05
        out.update({f"{name}_mean": m.mean(), f"{name}_p0": z.pvalue, f"{name}_F_int": an[0], f"{name}_p_int": an[3]})
    hij = single["J"] and not single["H"] and not single["I"]
    if verbose:
        print({k: round(float(v), 4) for k, v in out.items()})
    return dict(**out, FG_ok=all(fg), HIJ_ok=hij, holds=all(fg) and hij)


check5s1r(PRIMARY, verbose=True)
r5s1r = show_readings(check5s1r)

# %% [markdown]
# ### fig5j-ramping-tuning-curve
#
# > The Ramping population's tuning curve for the last interval is shifted right of the actual
# > probability, peaking at 0.625, consistent with mixed signaling of probability and fear.
#
# Criterion: as fig5e on the 14 Ramping neurons and the last interval; peak at 0.625; partially
# when at 0.5 or 0.75.

# %% tags=["claim:fig5j-ramping-tuning-curve"]
check_tuning(RAMP, CUE_IV[9], PRIMARY, verbose=True)
r5j = show_readings(lambda r: dict(peak=PU[np.argmax(tuning(RAMP, r, CUE_IV[9]))],
                                   holds=PU[np.argmax(tuning(RAMP, r, CUE_IV[9]))] == 0.625))
EOF
cat $TMPDIR/build/p{1,2,3,4,5,6}.py > $TMPDIR/build/dev.py; cd $TMPDIR && . wv/bin/activate && cd entries/wright-2019 && PYTHONPATH=. MPLBACKEND=Agg time python $TMPDIR/build/dev.py 2>&1 | sed -n '/^mean betas: interval/,$p'
```

```
Wed Nov 11 10:40:54 UTC 2026
mean betas: interval fear -0.034, total fear 0.024, probability 0.863 (n = 29)
P vs TF t(28) = 3.74, p = 0.000845; P vs IF t = 4.55, p = 9.6e-05
against zero: P t = 4.71, p = 6.18e-05; TF t = 0.27, p = 0.793; IF t = -0.56, p = 0.578
 poke zero     z     P      TF      IF   p_PvTF   p_PvIF     p_P0  p_TF0  p_IF0  holds  holds_at_005
table  one trial 0.863  0.0238 -0.0337 0.000845  9.6e-05 6.18e-05  0.793  0.578   True          True
table  one  type 0.794  0.0551  0.0609  0.00901  0.00221  0.00043  0.612  0.449   True          True
table zero trial 0.869 -0.0191  0.0451 0.000468 0.000337 5.73e-05  0.833   0.38   True          True
table zero  type  0.79  0.0497  0.0529  0.00831  0.00146 0.000376  0.638  0.217   True          True
table  nan trial 0.812  0.0731  0.0116   0.0442  0.00441  0.00242  0.624  0.856   True          True
table  nan  type 0.815   0.103  0.0555   0.0284  0.00265 0.000598  0.453  0.525   True          True
  2 s  one trial 0.846  0.0596 -0.0319 0.000351 0.000174  6.4e-05  0.193  0.622   True          True
  2 s  one  type  0.85 -0.0124  0.0895 0.000108  0.00121 6.54e-05  0.777  0.231   True          True
  2 s zero trial 0.836  0.0851 -0.0185 0.000833 0.000156  6.4e-05  0.235  0.812   True          True
  2 s zero  type 0.864 -0.0395  0.0977 0.000115 0.000534 3.51e-05  0.631  0.266   True          True
  2 s  nan trial 0.845  0.0693 -0.0383   0.0151 0.000585 0.000446   0.62  0.672   True          True
  2 s  nan  type  0.91  0.0116  0.0253   0.0055 0.000238 4.45e-05  0.945  0.845   True          True
 10 s  one trial 0.851  0.0326 -0.0495 0.000622 0.000163 7.18e-05  0.675  0.509   True          True
 10 s  one  type 0.803  0.0462  0.0591  0.00468  0.00251 0.000318   0.63  0.499   True          True
 10 s zero trial 0.868  0.0176 -0.0506 0.000285 0.000102 4.33e-05  0.821  0.507   True          True
[... 224 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cat > $TMPDIR/build/p7.py <<'EOF'
# %% [markdown]
# ## After cue offset
#
# ### fig6ab-post-cue-firing
#
# > In the 5 s after cue offset (delay, shock, post-shock; the shock itself excluded) Onset
# > neurons show no effects of trial type or bin, while Ramping neurons keep firing to danger and
# > uncertainty through the delay, with a trial x bin interaction, and the two populations differ.
#
# Criterion: Z-scored 100 ms firing for the four trial types, 45 bins from cue offset to 5 s
# after it without the shock (2.0 to 2.5 s after offset). Onset: no effect at p < 0.05; Ramping:
# both main effects and the interaction at p < 0.01; mixed ANOVA with neuron type: the three
# neuron-type interactions at p < 0.01. Partially when two of three parts hold.

# %% tags=["claim:fig6ab-post-cue-firing"]
POST_BINS = [i for i in range(200, 250) if not 220 <= i < 225]
Z100P = {k: pag.population_z100(units[k], split_uncertainty=True) for k in ONSET + RAMP}


def zpost(ks):
    return np.array([[Z100P[k][t][POST_BINS] for t in pag.TYPES] for k in ks])


YO, YRp = zpost(ONSET), zpost(RAMP)
print("bins:", len(POST_BINS))
print("Onset:", fmt_anova(pag.rm_anova(YO, ("trial", "bin"))))
print("Ramping:", fmt_anova(pag.rm_anova(YRp, ("trial", "bin"))))
mx = pag.mixed_anova([YO, YRp])
print("mixed (G = neuron type, A = trial type, B = bin):", fmt_anova(mx))
print("Ramping mean Z over the delay (0 to 2 s after offset): " + ", ".join(f"{t} {YRp[:, i, :20].mean():.2f}" for i, t in enumerate(pag.TYPES)))
print("Onset mean Z over the delay: " + ", ".join(f"{t} {YO[:, i, :20].mean():.2f}" for i, t in enumerate(pag.TYPES)))

# %% [markdown]
# ### fig6c-onset-post-cue-regression
#
# > After cue offset Onset neurons signal neither interval fear nor probability; no effect of
# > regressor or regressor x interval interaction, and no beta differs from zero.
#
# Criterion (absence): regressions per neuron in the nine 500 ms post-cue intervals (four of the
# delay, five after the shock) on interval fear (that 500 ms interval's suppression ratio) and
# probability; repeated-measures ANOVA at p < 0.05 and single-sample t-tests against zero at p <
# 0.005. Reproduced when neither ANOVA effect is significant and no beta differs from zero.

# %% tags=["claim:fig6c-onset-post-cue-regression"]
def post_check(ks, r, verbose=False):
    B = betas(ks, r, POST_IV, regs=("IF", "P"))       # n x 9 x 2
    an = pag.rm_anova(B.transpose(0, 2, 1), ("regressor", "interval"))
    p0 = np.array([[onesamp(B[:, j, i]).pvalue for j in range(9)] for i in range(2)])
    t0 = np.array([[onesamp(B[:, j, i]).statistic for j in range(9)] for i in range(2)])
    if verbose:
        print(fmt_anova(an))
        print("mean probability beta by interval:", np.round(B[:, :, 1].mean(0), 3).tolist())
        print("p against zero, probability:", [f"{p:.2g}" for p in p0[1]])
        print("p against zero, interval fear:", [f"{p:.2g}" for p in p0[0]])
    return B, an, p0, t0


def check6c(r, verbose=False):
    B, an, p0, t0 = post_check(ONSET, r, verbose)
    holds = (an["regressor"][3] >= 0.05) & (an["regressorxinterval"][3] >= 0.05) & (p0.min() >= 0.005)
    return dict(F_reg=an["regressor"][0], p_reg=an["regressor"][3], F_int=an["regressorxinterval"][0],
                p_int=an["regressorxinterval"][3], min_p0=p0.min(), holds=holds)


check6c(PRIMARY, verbose=True)
r6c = show_readings(check6c)

# %% [markdown]
# ### fig6d-ramping-post-cue-regression
#
# > Ramping neurons signal probability throughout the delay (the first four 500 ms intervals
# > after cue offset), and this signal diminishes after shock delivery, with a regressor x
# > interval interaction.
#
# Criterion: as fig6c on the 14 Ramping neurons. Reproduced when the interaction has p < 0.01,
# the mean probability beta is above zero at p < 0.005 in all four delay intervals, and the mean
# over the five post-shock intervals is below the mean over the delay; partially when the
# interaction holds and the probability beta is significant in one to three delay intervals.

# %% tags=["claim:fig6d-ramping-post-cue-regression"]
def check6d(r, verbose=False):
    B, an, p0, t0 = post_check(RAMP, r, verbose)
    nsig = int(((p0[1, :4] < 0.005) & (t0[1, :4] > 0)).sum())
    delay, post = B[:, :4, 1].mean(), B[:, 4:, 1].mean()
    holds = (an["regressorxinterval"][3] < 0.01) & (nsig == 4) & (post < delay)
    return dict(F_int=an["regressorxinterval"][0], p_int=an["regressorxinterval"][3], delay_sig_of_4=nsig,
                delay_mean=delay, post_mean=post, holds=holds,
                partial=(an["regressorxinterval"][3] < 0.01) & (1 <= nsig <= 3))


check6d(PRIMARY, verbose=True)
r6d = show_readings(check6d)

# %% [markdown]
# ### fig6ef-beta-correlations
#
# > Probability betas of the delay intervals correlate with those of the post-shock intervals in
# > 13 of 20 comparisons for Onset neurons but 4 of 20 for Ramping neurons, a significant
# > difference (6 and 1 of 20 after Bonferroni correction, also different).
#
# Criterion: per population, Pearson correlation across neurons of the probability beta of each
# delay interval with each post-shock interval (20 pairs), significant at p < 0.05 and at p <
# 0.01. Chi-square on the 2 x 2 counts, readings (a) Pearson chi-square x (N - 1) / N, (b)
# Pearson, (c) Yates. Reproduced when, under one reading, the chi-square has p < 0.05 at both
# thresholds and the four counts are within tolerance (13 +- 1.3, 4 +- 0.4, 6 +- 0.6, 1 +- 0.1);
# partially when Onset has more significant comparisons at both thresholds but a count or a test
# differs.

# %% tags=["claim:fig6ef-beta-correlations"]
def corr_counts(ks, r):
    B = betas(ks, r, POST_IV, regs=("IF", "P"))[:, :, 1]
    ps = np.array([[stats.pearsonr(B[:, i], B[:, j])[1] for j in range(4, 9)] for i in range(4)])
    return ps


def chi(a, b, n=20):
    tab = np.array([[a, n - a], [b, n - b]])
    out = {}
    if (tab.sum(0) == 0).any():
        return {"a": np.nan, "b": np.nan, "c": np.nan}, {"a": np.nan, "b": np.nan, "c": np.nan}
    c2 = stats.chi2_contingency(tab, correction=False)[0]
    N = tab.sum()
    out = {"a": c2 * (N - 1) / N, "b": c2, "c": stats.chi2_contingency(tab, correction=True)[0]}
    return out, {k: stats.chi2.sf(v, 1) for k, v in out.items()}


def check6ef(r, verbose=False):
    po, pr = corr_counts(ONSET, r), corr_counts(RAMP, r)
    res = {}
    for thr in (0.05, 0.01):
        a, b = int((po < thr).sum()), int((pr < thr).sum())
        c, p = chi(a, b)
        res[thr] = (a, b, c, p)
    counts_ok = (abs(res[0.05][0] - 13) <= 1.3) & (abs(res[0.05][1] - 4) <= 0.4) & (abs(res[0.01][0] - 6) <= 0.6) & (abs(res[0.01][1] - 1) <= 0.1)
    tests_ok = {k: (res[0.05][3][k] < 0.05) & (res[0.01][3][k] < 0.05) for k in "abc"}
    if verbose:
        print("Onset p (rows: delay intervals 1-4, columns: post-shock 6-10):\n", np.round(po, 3))
        print("Ramping p:\n", np.round(pr, 3))
        for thr, (a, b, c, p) in res.items():
            print(f"p < {thr}: Onset {a}/20, Ramping {b}/20; chi-square " + ", ".join(f"({k}) {c[k]:.2f}, p = {p[k]:.3g}" for k in "abc"))
    return dict(on05=res[0.05][0], ra05=res[0.05][1], on01=res[0.01][0], ra01=res[0.01][1],
                chi05_a=res[0.05][2]["a"], p05_a=res[0.05][3]["a"], chi01_a=res[0.01][2]["a"], p01_a=res[0.01][3]["a"],
                counts_ok=counts_ok, tests_ok_any=any(tests_ok.values()), holds=counts_ok & any(tests_ok.values()),
                partial=(res[0.05][0] > res[0.05][1]) & (res[0.01][0] > res[0.01][1]))


check6ef(PRIMARY, verbose=True)
r6ef = show_readings(check6ef)
EOF
cat $TMPDIR/build/p{1,2,3,4,5,6,7}.py > $TMPDIR/build/dev.py; cd $TMPDIR && . wv/bin/activate && cd entries/wright-2019 && PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/build/dev.py 2>&1 | sed -n '/^bins:/,$p'
```

```
Wed Nov 11 10:42:53 UTC 2026
bins: 45
Onset: trial: F(3,84) = 2.23, p = 0.091; bin: F(44,1232) = 1.23, p = 0.14; trialxbin: F(132,3696) = 0.84, p = 0.91
Ramping: trial: F(3,39) = 14.14, p = 2.2e-06; bin: F(44,572) = 7.11, p = 4.2e-32; trialxbin: F(132,1716) = 3.14, p = 1.6e-26
mixed (G = neuron type, A = trial type, B = bin): G: F(1,41) = 36.80, p = 3.5e-07; A: F(3,123) = 10.69, p = 2.7e-06; AxG: F(3,123) = 5.70, p = 0.0011; B: F(44,1804) = 5.39, p = 3.4e-26; BxG: F(44,1804) = 4.17, p = 8.1e-18; AxB: F(132,5412) = 1.91, p = 2.7e-09; AxBxG: F(132,5412) = 2.56, p = 3.9e-19
Ramping mean Z over the delay (0 to 2 s after offset): D 1.40, US 1.16, UO 1.26, S -0.10
Onset mean Z over the delay: D 0.18, US 0.33, UO 0.22, S -0.09
regressor: F(1,28) = 0.51, p = 0.48; interval: F(8,224) = 0.29, p = 0.97; regressorxinterval: F(8,224) = 0.61, p = 0.77
mean probability beta by interval: [0.053, 0.188, 0.218, 0.117, 0.015, 0.096, 0.154, 0.104, 0.084]
p against zero, probability: ['0.68', '0.094', '0.095', '0.39', '0.91', '0.43', '0.25', '0.37', '0.52']
p against zero, interval fear: ['0.077', '0.73', '0.92', '0.11', '0.34', '0.48', '0.48', '0.64', '0.23']
 poke zero     z  F_reg  p_reg  F_int  p_int  min_p0  holds
table  one trial  0.513   0.48   0.61  0.769  0.0768   True
table  one  type  0.223   0.64  0.906  0.512  0.0202   True
table zero trial  0.492  0.489  0.539  0.826  0.0093   True
table zero  type  0.949  0.338  0.705  0.687  0.0249   True
table  nan trial  0.541  0.468  0.965  0.464  0.0269   True
table  nan  type  0.925  0.344   1.09  0.373  0.0163   True
  2 s  one trial  0.513   0.48   0.61  0.769  0.0768   True
  2 s  one  type  0.223   0.64  0.906  0.512  0.0202   True
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/fouke-2025-01.yaml | head -150; ls questions | head; cat entries/fouke-2025/README.md | head -30
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
[... 169 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 150,400p attempts/fouke-2025-01.yaml | grep -v "^    - \|^      " | head -80; ls schemas; f=$(ls questions/*.yaml | head -1); head -40 $f
```

```
outcome: not_reproduced
  notebook: reproduce_fouke_2025.ipynb
  output: claim:fig1h-zf-higher-angular-acceleration
  notes: With angular acceleration as the Methods define it, DC are higher than ZF for all nine
    stimuli (medians 143 to 191 against 55.4 to 66.4 deg/s2, Kruskal-Wallis p below 0.05/9 for
    each), the reverse of the claim. Per-fish medians, and the files at 128 to 171 Hz alone
    (ZF 84.9, DC 178.6 deg/s2, p = 6.3e-05), give the same. The quantity Fig1-S1.ipynb computes
    gives ZF higher with p below 0.05/9 for 7 of 9 stimuli; it divides the heading change per
    frame by the file's mean frame interval, which in DC files is a median 8.73 times the frame
    interval (ZF 1.37), as DC files hold only trial frames. Part of the DC values may be tracking
    noise. In the 3 s stationary phase the DC median is 205 deg/s2, higher than the 171 during
    motion (per fish median ratio 1.24, p = 0.016), but ZF are also higher at rest (66.9 and 60.8,
    ratio 1.07, p = 0.00012), so this does not separate the species. In frames where the fish is
    still (below 1 mm/s) DC are higher than ZF (per-fish medians 72.4 and 34.9 deg/s2, Mann-Whitney
    p = 0.00014), and DC are higher in every speed band (at 5 mm/s or more, 207 and 85.8). The
    outputs cannot say whether the higher values in moving DC are noise or turning during
    continuous swimming. With the heading from the unwrapped `f0_theta` DC are higher still (218
    to 278 against ZF 61.8 to 77.3 deg/s2, 0 of 9). The reversal should not be read as evidence
    against the paper.
  deviations:
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n '/^findings:/,$p' attempts/fouke-2025-01.yaml | head -40; grep -l "crcns" attempts/*.yaml | head; head -3 questions/*.yaml | grep -v "^paper\|^questions\|^==\|^$" | sort | uniq -c | head; python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s['properties']['findings'],indent=0)[:1500]); print(s.get('required'))"
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
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,25p attempts/bruno-2017-01.yaml; cat entries/$(grep -h "^entry:" attempts/bruno-2017-01.yaml | awk '{print $2}')/entry.yaml; head -12 questions/$(ls questions | grep -i bruno || ls questions | sed -n 3p); grep -n "agent:\|harness\|protocol:" attempts/*.yaml | grep -i "pilot-14\|pilot-13" | head -4
```

```
schema_version: 3
id: bruno-2017-01
datasets:
- archive: crcns
  id: apl-1
  version: unversioned
  doi: 10.6080/K0SN074B
  relation: primary
paper: doi:10.7554/elife.27342
date: 2026-11-08
entry: bruno-2017
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-13
  runner:
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rn "questions" tools/*.py | head -15; grep -l "crcns\|^dataset:" questions/*.yaml | head -3; grep -h "^[a-z]*:" questions/*.yaml | sort | uniq -c
```

```
tools/agent_run.py:161:               "questions": paper_records.questions_file(key).relative_to(ROOT).as_posix(),
tools/build_site.py:191:    """A kind of record (claims, questions) with the datasets each is about: a paper's own file,
tools/build_site.py:414:    (papers/manifest.yaml), each claims file's last check, and each attempt's open questions."""
tools/build_site.py:417:    checks, questions, items, paper_checks, paper_questions = {}, {}, {}, {}, {}
tools/build_site.py:419:    paper_key = lambda path: path.stem if path.parent.name in ("claims", "questions") else path.parent.name
tools/build_site.py:431:    for path, keys in record_files("questions"):
tools/build_site.py:433:        q = q.get("questions", []) if isinstance(q, dict) else q
tools/build_site.py:436:            questions[key] = n_open
tools/build_site.py:438:        paper_questions[paper_key(path)] = paper_questions.get(paper_key(path), 0) + n_open
tools/build_site.py:439:    return {"papers": {key_of_dir(str(k)): v for k, v in papers.items()}, "checks": checks, "questions": questions,
tools/build_site.py:440:            "question_items": items, "paper_checks": paper_checks, "paper_questions": paper_questions}
tools/build_site.py:620:                  ("attempt", "Attempt"), ("questions", "Questions"), ("verified", "Verified")]
tools/build_site.py:662:    inputs = data.get("pipeline") or {"papers": {}, "checks": {}, "questions": {}}
tools/build_site.py:676:        open_q = inputs["questions"].get(d, 0)
tools/build_site.py:695:            "questions": ("todo", f"{open_q} open") if open_q else ("none", ""),
questions/dias-2025.yaml
questions/didion-gency-2024.yaml
questions/dimakopoulos-2022.yaml
      1 dandiset: "000006"
      1 dandiset: "000009"
[... 189 more lines not kept]
```

**Agent**

Writing the header and summary, then building the notebook and entry files.

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;c=yaml.safe_load(open('claims/wright-2019.yaml'));print(len(c['claims']));print([x['id'] for x in c['claims']])"; date -u
```

```
39
['fig1c-total-suppression', 'fig1c-nonlinear-scaling', 'fig1d-interval-suppression', 'fig1s1a-nose-poke-rates', 'fig1s1b-sr-poke-correlation', 'fig1e-two-clusters', 'onset-population', 'ramping-population', 'fig2a-onset-anova', 'fig2b-onset-first-interval', 'fig2b-onset-last-interval', 'fig2c-ramping-anova', 'fig2d-ramping-first-interval', 'fig2d-ramping-last-interval', 'fig2e-departure-times', 'fig2e-rate-no-difference', 'fig2s1-single-trial', 'fig2s2-nose-poke-cessation', 'fig3-onset-ramping-independent', 'fig4abc-onset-single-unit-biases', 'fig4d-onset-patterns', 'fig4efg-ramping-single-unit-biases', 'fig4h-ramping-patterns', 'fig5a-onset-probability-first-interval', 'fig5bc-onset-beta-bias', 'fig5d-onset-all-intervals', 'fig5s1-regressor-combinations', 'fig5e-onset-tuning-curve', 'fig5s2-binary-regressor', 'fig5f-ramping-last-interval', 'fig5gh-ramping-beta-bias', 'fig5i-ramping-all-intervals', 'fig5s1-ramping-regressor-combinations', 'fig5j-ramping-tuning-curve', 'fig6ab-post-cue-firing', 'fig6c-onset-post-cue-regression', 'fig6d-ramping-post-cue-regression', 'fig6ef-beta-correlations', 'fig1s5-hfr-units']
Wed Nov 11 10:45:06 UTC 2026
```

**Agent calls Bash**

```bash
cat > $TMPDIR/build/results.py <<'EOF'
R = {
"fig1c-total-suppression": "**Result: reproduced.** With the 20 s baseline the paper's table fixes (0/0 = 1, mean of trial ratios), the 88 sessions give danger 0.799, uncertainty 0.531 and safety 0.030, all within tolerance. The cue effect gives F(2,174) = 595, p = 1.6e-78, danger against uncertainty t = 12.3 (p = 9.1e-21), and uncertainty against safety t = 21.0 (p = 7.8e-36). The paper reports F = 592.00, t = 12.36 and t = 20.85. The 10 s readings also put all three means within tolerance. The 2 s readings do not (danger 0.35 to 0.75), though their tests hold. Danger 0.80 is also inside the tolerance of the legend's 0.83.",
"fig1c-nonlinear-scaling": "**Result: reproduced.** Under every reading on which fig1c-total-suppression matched, the uncertainty mean is above the midpoint of danger and safety (primary reading: 0.531 against 0.415).",
"fig1d-interval-suppression": "**Result: reproduced, resting on the reading the Methods table fixes (assumed).** With interval fear over a 2 s baseline and 0/0 = 1, the cue effect is F(2,174) = 493, p = 2.1e-72, and the cue x interval interaction F(18,1566) = 6.15, p = 9.5e-15. Danger exceeds uncertainty and uncertainty exceeds safety at p < 0.005 in 10 of 10 intervals each (smallest t 3.03 and 6.2). The paper reports F = 489.40, F = 6.21 and all t > 3.00. Readings that set 0/0 to 0 or leave it out, and the 10 s and 20 s windows with 0/0 = 1 and trial means, find 8 or 9 of 10 danger-uncertainty intervals.",
"fig1s1a-nose-poke-rates": "**Result: partially reproduced, resting on an assumed baseline window.** Under every window, poking falls from baseline to cue for danger and both uncertainty types (t(87) from 10.6 to 17.6, p < 1e-16) and not for safety (p 0.24 to 0.60). Baseline rates across the four trial types do not differ with a 2 s window (F(3,261) = 2.20, p = 0.088) or a 10 s window (p = 0.066). They do differ with the 20 s window (F = 3.47, p = 0.017), the window the paper's table uses for total fear and the one adopted here. The means are 39.6, 37.0, 39.1 and 37.8 pokes/min.",
"fig1s1b-sr-poke-correlation": "**Result: reproduced.** Under every reading, the total cue suppression ratio and the cue poke rate correlate negatively over the 88 sessions for danger (r -0.40 to -0.73) and uncertainty (r -0.36 to -0.75), all p < 0.001. Pooled over 264 points, r is -0.52 to -0.79. Under the primary reading the safety correlation is r = -0.35 (p = 0.001), weaker than the other two.",
"fig1e-two-clusters": "**Result: reproduced.** With the 2 s pre-cue baseline rate and raw features, k-means gives 197 LFR and 48 HFR neurons. The baseline rate differs by cluster (F(1,243) = 835, p = 1.4e-80; paper 829), and half duration (p = 0.97) and amplitude ratio (p = 0.51) do not. Z-scored features give 198 and 47. The session-mean rate gives 194 and 51, which puts HFR outside tolerance.",
"onset-population": "**Result: reproduced.** The Methods screen finds 29 Onset neurons from 5 rats (dr01 10, dr02 4, rf02 4, rf03 10, rf08 1), all 29 in the LFR cluster under every clustering reading. The data set script's rounded-down baseline would give 31 from 6 rats. One Onset neuron (dr02092716 SPK04a) shares 66% of its spikes with another unit of its session.",
"ramping-population": "**Result: reproduced.** Of the other neurons, 17 pass the screen on the last 1 s. Three are in the HFR cluster under every clustering reading, and the other 14 Ramping neurons come from 4 rats (dr01 4, dr02 2, rf02 1, rf03 7).",
"fig2a-onset-anova": "**Result: reproduced.** Over the 29 Onset neurons the cue effect is F(2,56) = 8.64 (p = 5.4e-4), the bin effect F(109,3052) = 14.19 (p = 1.8e-197), and the interaction F(218,6104) = 1.89 (p = 1.6e-13; paper 1.94), all p < 0.01.",
"fig2b-onset-first-interval": "**Result: reproduced.** In the first interval, danger is above uncertainty (t(28) = 5.05, p = 2.4e-5, trial baseline; paper t = 4.54). Uncertainty is above safety in mean (-0.09 against -0.23) without significance (t = 1.36, p = 0.185; paper 1.37, 0.18). The uncertainty and safety ANOVA over 60 bins gives a cue x bin interaction F(59,1652) = 1.41, p = 0.024 (paper 1.50, p = 0.01). The type-baseline reading gives the same.",
"fig2b-onset-last-interval": "**Result: reproduced.** In the last interval neither pair differs: danger against uncertainty t = 1.94, p = 0.062 (difference 0.24 Z, dz 0.36), and uncertainty against safety t = 0.58, p = 0.57. The type baseline gives p = 0.080 and 0.62.",
"fig2c-ramping-anova": "**Result: reproduced.** Over the 14 Ramping neurons the cue effect is F(2,26) = 32.10, the bin effect F(109,1417) = 12.29, and the interaction F(218,2834) = 4.29 (paper 4.33), all p < 1e-7. In the last 1 s, mean Z firing is danger 1.93, uncertainty 1.20 and safety -0.10.",
"fig2d-ramping-first-interval": "**Result: reproduced.** In the first interval neither pair differs: danger against uncertainty t(13) = 0.43, p = 0.67, and uncertainty against safety t = 0.49, p = 0.63. The type baseline gives p = 0.54 and 0.77.",
"fig2d-ramping-last-interval": "**Result: reproduced.** In the last interval danger exceeds uncertainty (t(13) = 3.14, p = 0.0078) and uncertainty exceeds safety (t = 8.09, p = 2.0e-6). The paper reports 3.17 and 8.26. The type baseline gives the same.",
"fig2e-departure-times": "**Result: partially reproduced.** Danger departs from safety before uncertainty at both thresholds under every reading. With window starts and measure b, three of the four times are within tolerance: danger 2.7 s at p < 0.05 (paper 2.8), uncertainty 5.2 s (5.7) and 6.4 s (6.5). The danger time at p < 0.00025 is 4.7 s against 5.8 +- 0.58. Measure a gives 2.7, 4.5, 5.1 and 6.4 s. Window ends put every time about 1 s later.",
"fig2e-rate-no-difference": "**Result: reproduced.** No reading of fig2e-departure-times matched in full, so every reading is shown. The rate of increase from the departure window to the last window does not differ between danger and uncertainty: measure a t(13) = -0.20, p = 0.84; measure b t = -0.49, p = 0.63.",
"fig2s1-single-trial": "**Result: partially reproduced.** Onset first-interval firing exceeds the population baseline at all 32 trial positions (smallest margin 5.3 spikes/s). Ramping last-interval firing exceeds baseline at all 22 danger and uncertainty positions, but also at 6 of the 10 safety positions, one more than the criterion's reading allows. The six margins range from 0.57 to 10.64 spikes/s, and four of them are below 3.4.",
"fig2s2-nose-poke-cessation": "**Result: reproduced.** With differential firing (measure b), firing to danger does not correlate with firing to cessation: Onset R2 = 0.0006, p = 0.90, and Ramping R2 = 0.23, p = 0.080. Danger is greater in 26 of 29 Onset neurons (sign test p = 1.5e-5) and 14 of 14 Ramping neurons (p = 1.2e-4; paper 1.22e-4). This holds under both ITI readings. With raw rates (measure a) the two correlate (R2 0.61 to 0.68, p < 0.001), because a neuron's overall rate sets both.",
"fig3-onset-ramping-independent": "**Result: partially reproduced.** Only three Onset-Ramping pairs share a session, in two sessions (dr01101616 and dr01102316), against the paper's four pairs in four sessions. None of the 30 interval regressions gives a negative beta at p < 0.05 (betas -0.33 to 0.42), so the independence holds for the pairs found.",
"fig4abc-onset-single-unit-biases": "**Result: reproduced.** A: danger and uncertainty correlate (r = -0.47, p = 0.010) and 22 of 29 neurons fire more to danger (sign p = 0.008). B: uncertainty and safety correlate (r = -0.55, p = 0.002) and the bias to uncertainty is not significant (17 of 29, p = 0.46). C: 22 of 29 fire more to danger in the first interval than in the last (p = 0.008), with no correlation (r = 0.34, p = 0.070). Both correlations are negative. Interval Z firing has mean zero over each neuron's 32 trials, so the cue means of a neuron trade off against each other. The type baseline gives the same outcome.",
"fig4d-onset-patterns": "**Result: reproduced under shuffle reading a.** The danger > uncertainty > safety pattern holds 14 of 29 Onset neurons, the largest of the four categories. With the three values permuted within each neuron it is the only category above the 95th percentile (8.05) and above the whisker (9.0). With each cue permuted across neurons (reading b), the chance median for this order is 15, and only safety > uncertainty > danger (4 against a whisker of 3.5) is above chance.",
"fig4efg-ramping-single-unit-biases": "**Result: partially reproduced.** E: 12 of 14 Ramping neurons fire more to danger than uncertainty (p = 0.013), but the correlation is not significant (r = -0.45, p = 0.11; type baseline p = 0.17). F: no correlation (p = 0.094) and a bias to uncertainty (14 of 14, p = 1.2e-4). G: 12 of 14 fire more in the last interval than the first (p = 0.013), with no correlation (p = 0.33). Two of three panels hold.",
"fig4h-ramping-patterns": "**Result: reproduced under shuffle reading a.** The danger > uncertainty > safety pattern holds 12 of 14 Ramping neurons, within 11 +- 1.1 and the largest. It is the only category above chance under within-neuron shuffles (95th percentile 5, whisker 6). Under across-neuron shuffles no category is above chance.",
"fig5a-onset-probability-first-interval": "**Result: reproduced.** First-interval mean betas over the 29 Onset neurons are probability 0.863, total fear 0.024 and interval fear -0.034. Probability exceeds total fear (t(28) = 3.74, p = 8.5e-4; paper 3.75) and interval fear (t = 4.55, p = 9.6e-5; paper 4.57). Probability is above zero (p = 6.2e-5) and neither fear beta differs from zero (p = 0.79, 0.58). All 18 readings meet the criterion, also at 0.05.",
"fig5bc-onset-beta-bias": "**Result: reproduced, resting on the reading the Methods table fixes (assumed).** Under the primary reading, 22 of 29 probability betas are positive (sign p = 0.008), while interval fear (14 of 29, p = 1.0) and total fear (17 of 29, p = 0.46) are not biased. 17 of 18 readings meet the criterion. The exception is the 20 s and 2 s baselines with 0/0 trials left out, where probability is 20 of 29 (p = 0.061).",
"fig5d-onset-all-intervals": "**Result: reproduced, resting on the reading the Methods table fixes (assumed).** The regressor effect is F(2,56) = 7.16 (p = 0.0017; paper 7.16) and the regressor x interval interaction F(18,504) = 2.35 (p = 0.0014; paper 2.38). The probability beta peaks in interval 1 (0.863) and declines to 0.24, and is above zero at p < 0.005 in intervals 1 to 4. No fear beta differs from zero in any interval (smallest p 0.156). 9 of 18 readings meet the criterion. The others fail by p between 0.01 and 0.05 for an effect, a fear beta below 0.005, or a peak in interval 2.",
"fig5s1-regressor-combinations": "**Result: reproduced, resting on the reading the Methods table fixes (assumed).** Under the primary reading no fear regressor reaches significance in A, B or C under either significance reading. Total fear alone (D) does (interval effect p = 0.0087, and a first-interval beta above zero at p < 0.005). Its first-interval and largest mean beta (0.41) is below that of probability alone (0.87). A and B show a main effect of regressor (p = 0.015 and 0.004) with probability above fear. With the type baseline, A's regressor effect is p = 0.12 and the claim fails there.",
"fig5e-onset-tuning-curve": "**Result: reproduced, resting on the reading the Methods table fixes (assumed).** The mean probability beta peaks at 0.375 (0.863), with 0.25 (0.838) and 0.5 (0.808) next, falling to 0.675 at 0 and 0.133 at 1. With 2 s total fear and 0/0 set to 1 or 0, the peak moves to 0.25.",
"fig5s2-binary-regressor": "**Result: reproduced, resting on the reading the Methods table fixes (assumed).** The analysis x regressor x interval interaction is F(18,504) = 2.49, p = 6.4e-4 (paper 2.51, 5.89e-4). The first-interval analysis x regressor interaction is F(2,56) = 7.75, p = 0.0011 (paper 7.80, 1.03e-3). The first-interval beta is 0.863 for probability against 0.675 for binary. Three readings with 2 s total fear miss one interaction at p < 0.05.",
"fig5f-ramping-last-interval": "**Result: reproduced, resting on the reading the Methods table fixes (assumed).** Last-interval betas over the 14 Ramping neurons are probability 0.777, total fear 0.478 and interval fear -0.064. Probability (t(13) = 3.62, p = 0.0031) and total fear (t = 4.62, p = 4.8e-4) exceed interval fear, and they do not differ from each other (t = 1.14, p = 0.28). The paper reports 3.61, 4.68 and 1.11. With 2 s total fear and 0/0 set to 1 or 0, the total fear beta falls to about 0 and the claim fails.",
"fig5gh-ramping-beta-bias": "**Result: reproduced, resting on the reading the Methods table fixes (assumed).** Under the primary reading probability and total fear are each biased positive (12 of 14, p = 0.013) and uncorrelated (r = -0.34, p = 0.24). Interval fear is not biased (6 of 14, p = 0.79), and probability and interval fear correlate negatively (r = -0.57, p = 0.035). 6 of 18 readings meet all four parts, the 2 s readings meet two, and the 10 s readings two or four.",
"fig5i-ramping-all-intervals": "**Result: reproduced.** Under the primary reading the per-neuron means over the ten intervals are probability 0.577 +- 0.136, total fear 0.120 +- 0.100 and interval fear -0.026 +- 0.050 (paper 0.58 +- 0.14, 0.12 +- 0.10, -0.03 +- 0.05). The regressor effect is F(2,26) = 9.14 (p = 9.9e-4) and the interaction F(18,234) = 2.19 (p = 0.0042). Probability differs from zero (t(13) = 4.24, p = 9.6e-4) and exceeds total fear (t = 2.35, p = 0.035) and interval fear (t = 4.37, p = 7.5e-4). The fear means do not differ from zero (p = 0.25, 0.61). The paper reports t = 4.21, 2.32 and 4.32.",
"fig5s1-ramping-regressor-combinations": "**Result: partially reproduced, resting on the reading the Methods table fixes (assumed).** F and G hold: probability means 0.58 and 0.66 differ from zero (p = 9.3e-4, 7.5e-5), fear means do not (p = 0.41, 0.92), probability exceeds fear (p = 0.029, 4.2e-5), and the regressor effects are p = 0.029 and 4.2e-5. Of the single-regressor models, probability alone (J, 0.66, p = 1.7e-4) differs from zero, and so does total fear alone (I, 0.37, p = 0.0067). Interval fear alone (H) does not (p = 0.14). With 2 s total fear, total fear alone is near zero and the claim holds in full.",
"fig5j-ramping-tuning-curve": "**Result: reproduced, resting on the reading the Methods table fixes (assumed).** The Ramping last-interval tuning curve peaks at 0.625 (0.866), just above 0.5 (0.858). With 2 s total fear and 0/0 set to 1 or 0, the peak is at 0.5.",
"fig6ab-post-cue-firing": "**Result: reproduced.** Onset neurons show no effect after cue offset: trial F(3,84) = 2.23, p = 0.091; bin p = 0.14; interaction p = 0.91 (paper Fs < 2.3, ps > 0.09). Ramping neurons show trial F(3,39) = 14.14, bin F(44,572) = 7.11, and trial x bin F(132,1716) = 3.14 (paper 3.14), all p < 1e-5. In the mixed ANOVA the neuron type interactions are trial F(3,123) = 5.70 (p = 0.0011), bin F(44,1804) = 4.17 and trial x bin F(132,5412) = 2.56, all p < 0.01. Ramping firing stays high through the delay on danger and uncertainty trials (Z 1.16 to 1.40) and not on safety trials (-0.10).",
"fig6c-onset-post-cue-regression": "**Result: reproduced.** Onset regressions after the cue show no regressor effect (F(1,28) = 0.51, p = 0.48; paper 1.02, 0.32) and no interaction (F(8,224) = 0.61, p = 0.77; paper 0.53, 0.83). No beta differs from zero at p < 0.005 (smallest p 0.077). Every reading gives the same, with smallest p from 0.0064 to 0.09.",
"fig6d-ramping-post-cue-regression": "**Result: reproduced.** For Ramping neurons the regressor x interval interaction is F(8,104) = 7.00, p = 2.3e-7 (paper 5.20). The probability beta is above zero in all four delay intervals (p from 2.7e-6 to 7.7e-4). Its mean falls from 0.715 over the delay to 0.020 over the five post-shock intervals. Every reading gives the same.",
"fig6ef-beta-correlations": "**Result: partially reproduced, resting on the reading the Methods table fixes (assumed).** Onset has more significant delay against post-shock correlations than Ramping at both thresholds, but far fewer than the paper reports: 3 of 20 against 0 at p < 0.05 (paper 13 and 4), and 1 against 0 at p < 0.01 (paper 6 and 1). No chi-square reading is significant (reading a 3.16, p = 0.075, and 1.00, p = 0.32). Across readings the Onset count is 1 to 5, and one reading gives Ramping more.",
"fig1s5-hfr-units": "**Result: reproduced.** Each of the three HFR late-responsive neurons fires most to danger in the last interval, by raw rate (141.5, 89.3 and 89.8 spikes/s against at most 120.9, 64.7 and 81.5) and by interval Z.",
}
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR/build && python3 - <<'EOF'
s=open('results.py').read()
rep=[
("Readings that set 0/0 to 0 or leave it out, and the 10 s and 20 s windows with 0/0 = 1 and trial means, find 8 or 9 of 10 danger-uncertainty intervals.",
 "Five of the twelve readings give 10 of 10 in both comparisons. The other seven give 8 or 9 danger-uncertainty intervals (partially reproduced there); all give 10 of 10 uncertainty-safety intervals and both ANOVA effects."),
("(interval effect p = 0.0087, and a first-interval beta above zero at p < 0.005)","(interval effect p = 0.0087, and a beta above zero at p < 0.005 in at least one interval)"),
("the 2 s readings meet two,","the 2 s readings one or two,"),
("9 of 18 readings meet the criterion. The others fail by p between 0.01 and 0.05 for an effect, a fear beta below 0.005, or a peak in interval 2.",
 "10 of 18 readings meet the criterion. The others fail by an ANOVA effect with p above 0.01, a fear beta below p = 0.005 in one interval, or a peak in interval 2."),
("The exception is the 20 s and 2 s baselines with 0/0 trials left out, where probability is 20 of 29 (p = 0.061).",
 "The exception is the table's windows with 0/0 trials left out and the trial baseline, where probability is 20 of 29 (p = 0.061)."),
("With 2 s total fear and 0/0 set to 1 or 0, the peak moves to 0.25.\"",
 "With 2 s total fear and 0/0 set to 1 or 0, the peak moves to 0.25. With the type baseline and 0/0 set to 0 or left out, the third value is 0.125 in place of 0.5.\""),
("the total fear beta falls to about 0 and the claim fails.","the total fear beta falls to 0.12 or less and the claim fails."),
("With 2 s total fear, total fear alone is near zero and the claim holds in full.","With 2 s total fear, total fear alone is near zero (0.005 to 0.063) and the claim holds in full."),
]
for a,b in rep:
    assert a in s, a[:40]
    s=s.replace(a,b)
open('results.py','w').write(s)
EOF
echo done
```

```
done
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/build/p0.py <<'EOF'
# %% [markdown]
# # Reproducing Wright and McDannald (2019) from CRCNS pag-1
#
# Paper. Wright KM, McDannald MA (2019). Ventrolateral periaqueductal gray neurons prioritize threat
# probability over fear output. eLife 8:e45013, doi:10.7554/eLife.45013. The claims file
# (claims/wright-2019.yaml) was written from the version of record (PMC6435320, Europe PMC full
# text): main text, Materials and methods and all figure legends.
#
# Dataset. CRCNS pag-1, "Ventrolateral periaqueductal gray single-unit activity during multi-cue
# fear discrimination in rats", doi:10.6080/K0R49P0V, data description version 0.5 (6 March 2019).
# CRCNS data sets have no versions. The bucket holds one copy, under pag-1/live/ (no pag-1/old/),
# so that copy is the one used, recorded as `unversioned`. The file read is data.zip, MD5
# 5437f01d5071fe55a1baedbb146f56e0 as listed in the data set's checksums.md5 (printed below), so
# a later change is detectable. It is opened in place over HTTP range requests and never written
# to disk. Inside it, the 245 per-unit files data/mFiles/*.mat hold the spike times, events and
# waveforms every claim is computed from. The data set's scripts data/cubeScript.m and
# data/analysisScript.m are read for two lines below; its precomputed cube (cubeFile/cube.mat) is
# not used.
#
# Method details. Every method comes from the claims file's criteria, or, where they leave a
# detail open, from the paper (cited where used, in pag.py's docstrings and below). The Methods
# print the full regression input of one Onset neuron. The data check finds that neuron and shows
# which readings of the open details reproduce it. That reading is the primary one here, and the
# claims file's readings are run beside it.
#
# Claims (39, all tested):
#
# | Claim | Tested |
# |---|---|
# | fig1c-total-suppression, fig1c-nonlinear-scaling, fig1d-interval-suppression, fig1s1a-nose-poke-rates, fig1s1b-sr-poke-correlation | tested (88 sessions) |
# | fig1e-two-clusters, onset-population, ramping-population, fig1s5-hfr-units | tested (245 units) |
# | fig2a to fig2s2, fig3, fig4abc to fig4h (14 claims) | tested (29 Onset, 14 Ramping neurons) |
# | fig5a to fig5j (11 claims) | tested |
# | fig6ab, fig6c, fig6d, fig6ef | tested |
EOF
cat > $TMPDIR/build/p8.py <<'EOF'
# %% [markdown]
# ## Summary
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# | Claim | Outcome |
# |---|---|
# | fig1c-total-suppression | reproduced |
# | fig1c-nonlinear-scaling | reproduced |
# | fig1d-interval-suppression | reproduced (assumed reading) |
# | fig1s1a-nose-poke-rates | partially reproduced (assumed reading) |
# | fig1s1b-sr-poke-correlation | reproduced |
# | fig1e-two-clusters | reproduced |
# | onset-population | reproduced |
# | ramping-population | reproduced |
# | fig2a-onset-anova | reproduced |
# | fig2b-onset-first-interval | reproduced |
# | fig2b-onset-last-interval | reproduced |
# | fig2c-ramping-anova | reproduced |
# | fig2d-ramping-first-interval | reproduced |
# | fig2d-ramping-last-interval | reproduced |
# | fig2e-departure-times | partially reproduced |
# | fig2e-rate-no-difference | reproduced |
# | fig2s1-single-trial | partially reproduced |
# | fig2s2-nose-poke-cessation | reproduced |
# | fig3-onset-ramping-independent | partially reproduced |
# | fig4abc-onset-single-unit-biases | reproduced |
# | fig4d-onset-patterns | reproduced |
# | fig4efg-ramping-single-unit-biases | partially reproduced |
# | fig4h-ramping-patterns | reproduced |
# | fig5a-onset-probability-first-interval | reproduced |
# | fig5bc-onset-beta-bias | reproduced (assumed reading) |
# | fig5d-onset-all-intervals | reproduced (assumed reading) |
# | fig5s1-regressor-combinations | reproduced (assumed reading) |
# | fig5e-onset-tuning-curve | reproduced (assumed reading) |
# | fig5s2-binary-regressor | reproduced (assumed reading) |
# | fig5f-ramping-last-interval | reproduced (assumed reading) |
# | fig5gh-ramping-beta-bias | reproduced (assumed reading) |
# | fig5i-ramping-all-intervals | reproduced |
# | fig5s1-ramping-regressor-combinations | partially reproduced (assumed reading) |
# | fig5j-ramping-tuning-curve | reproduced (assumed reading) |
# | fig6ab-post-cue-firing | reproduced |
# | fig6c-onset-post-cue-regression | reproduced |
# | fig6d-ramping-post-cue-regression | reproduced |
# | fig6ef-beta-correlations | partially reproduced (assumed reading) |
# | fig1s5-hfr-units | reproduced |
#
# How the analysis differs from the paper's. The nose poke baselines and the 0/0 rule are the
# ones the paper's printed regression input reproduces: 20 s for total fear, 2 s for interval
# fear, 0/0 = 1. The claims file named 2 s and 10 s and 0 or left out, and those readings are
# shown for every claim. Where they change an outcome, the outcome rests on the table's reading
# and is marked as assumed. The repeated-measures ANOVAs carry no sphericity correction, as the
# paper's integer degrees of freedom imply. k-means uses k-means++ starts and 20 replicates. The
# waveform features use the peak-picking described in pag.py. Interval Z firing is Z-scored per
# interval, as the Methods describe.
#
# What was found about the dataset:
#
# - The files hold everything the paper analysed: 245 units, 88 sessions, 6 rats, 32 trials each,
#   with spike times, cue, shock and poke times, and mean waveforms. With the paper's methods
#   they reproduce the population counts (29, 17, 3, 14) and most reported statistics to their
#   printed precision.
# - The data description says the cube's `poke.base` is the poke rate 2 s before the cue. The
#   data set's cubeScript.m computes it over 20 s, and sets 0/0 suppression ratios to 1. Neither
#   the paper nor the description states either choice; the paper's table implies both.
# - The cube's interval suppression ratios (cubeScript.m) use the 20 s baseline, while the
#   paper's interval fear, by its table and by Figure 1D's statistics, uses 2 s.
# - Cue onsets are 132 to 195 s apart, so no ITI reaches the "mean ITI of 3.5 min" of the paper
#   and the description.
# - Five unit pairs recorded in the same session share 66 to 90% of the spikes of one unit
#   (within 0.5 ms); one is an Onset neuron.
# - Only three Onset-Ramping pairs share a session, where the paper reports four.
# - Channels EVT08 (a copy of the shock channel) and EVT14 are in every file and not described.

# %%
print(f"run time {(time.time() - T0) / 60:.1f} min, peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")
EOF
cat > $TMPDIR/build/tonb.py <<'EOF'
import sys, re, nbformat
sys.path.insert(0, sys.argv[1].rsplit('/', 1)[0])
from results import R
src = open(sys.argv[1]).read()
cells = []
for block in re.split(r'^# %%', src, flags=re.M)[1:]:
    head, _, body = block.partition('\n')
    tags = re.findall(r'"([^"]+)"', head.split('tags=')[1]) if 'tags=' in head else []
    body = body.strip('\n')
    if '[markdown]' in head:
        body = '\n'.join(l[2:] if l.startswith('# ') else l.lstrip('#') for l in body.split('\n'))
        c = nbformat.v4.new_markdown_cell(body)
    else:
        c = nbformat.v4.new_code_cell(body)
    if tags: c.metadata['tags'] = tags
    cells.append(c)
out = []
for i, c in enumerate(cells):
    out.append(c)
    tag = next((t for t in c.metadata.get('tags', []) if t.startswith('claim:')), None)
    nxt = cells[i + 1] if i + 1 < len(cells) else None
    if tag and not (nxt is not None and tag in nxt.metadata.get('tags', [])):
        out.append(nbformat.v4.new_markdown_cell(R.pop(tag[6:])))
assert not R, R.keys()
nb = nbformat.v4.new_notebook(cells=out)
nb.metadata['kernelspec'] = {'name': 'python3', 'display_name': 'Python 3', 'language': 'python'}
nbformat.write(nb, sys.argv[2])
print(len(out), 'cells')
EOF
cd $TMPDIR/build && cat p0.py p1.py p2.py p3.py p4.py p5.py p6.py p7.py p8.py > all.py && . $TMPDIR/wv/bin/activate && python tonb.py $TMPDIR/build/all.py entries/wright-2019/reproduce_wright_2019.ipynb
```

```
140 cells
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/build && python3 - <<'EOF'
for f,a,b in [('p1.py',"does not use; they are checked below.","does not use; no claim needs them."),
              ('p8.py',"# - Channels EVT08 (a copy of the shock channel) and EVT14 are in every file and not described.\n","")]:
    s=open(f).read(); assert a in s; open(f,'w').write(s.replace(a,b))
EOF
cat p0.py p1.py p2.py p3.py p4.py p5.py p6.py p7.py p8.py > all.py && . $TMPDIR/wv/bin/activate && python tonb.py $TMPDIR/build/all.py entries/wright-2019/reproduce_wright_2019.ipynb
cd entries/wright-2019
cat > requirements.in <<'EOF'
aiohttp
fsspec
matplotlib
numpy
pandas
requests
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: wright-2019
type: reproduction
title: Threat probability in ventrolateral periaqueductal gray neurons (Wright and McDannald 2019)
description: Tests the findings of Wright and McDannald (2019) on CRCNS data set pag-1, which holds
  the spike times, event times and mean waveforms of 245 ventrolateral periaqueductal gray units
  recorded in 88 fear discrimination sessions of six rats. It recomputes suppression ratios, the
  k-means clusters, the Onset and Ramping populations, their population and single-unit firing,
  and the single-unit regressions on threat probability and fear output, under every reading of
  the details the paper leaves open and the reading the paper's printed regression input fixes.
license: Apache-2.0
notebooks:
- path: reproduce_wright_2019.ipynb
  title: Reproducing Wright and McDannald (2019) from CRCNS pag-1
  runtime_minutes: 5
helpers:
- pag.py
related:
- id: crcns:pag-1/unversioned
  relation: uses_data
- id: doi:10.7554/elife.45013
  relation: reproduces
EOF
cd  && sed -n 1,60p tools/entry.py | head -60; date -u
```

```
140 cells
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
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
python tools/entry.py lock entries/wright-2019 2>&1 | tail -5 && python tools/entry.py check entries/wright-2019 2>&1 | tail -20
```

```
wrote wright-2019/requirements.lock.txt (Python 3.13, with hashes)
error: entries/wright-2019/reproduce_wright_2019.ipynb: neither the notebook nor a helper names version unversioned of dataset pag-1, which entry.yaml pins
1 error(s)
```

**Agent calls Bash**

```bash
grep -n "names version\|def _names_dataset\|unversioned" tools/entry.py | head; grep -rn "unversioned\|apl-1" entries/bruno-2017/apl.py | head -5
```

```
237:                report.error(rel / name, f"neither the notebook nor a helper names version {version} "
1:"""Loading and measures for CRCNS data set apl-1 (Bruno & Frost 2017).
51:DATASET = "apl-1"            # CRCNS data set, doi:10.6080/K0SN074B
52:VERSION = "unversioned"      # CRCNS data sets are not versioned (docs/archives.md); MD5 sums are checked
53:BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com/apl-1/live/"
```

**Agent calls Bash**

```bash
cd entries/wright-2019 && python3 - <<'EOF'
s=open('pag.py').read()
a='URL = "https://crcnsarchive'
s=s.replace(a,'DATASET = "pag-1"            # CRCNS data set, doi:10.6080/K0R49P0V\nVERSION = "unversioned"      # CRCNS data sets are not versioned (docs/archives.md); MD5 in checksums.md5\n'+a,1)
open('pag.py','w').write(s)
EOF
cd ../.. && python tools/entry.py check entries/wright-2019 2>&1 | tail -5; date -u; time python tools/entry.py run entries/wright-2019 2>&1 | tail -15
```

```
0 error(s)
Wed Nov 11 10:47:36 UTC 2026
Installed kernelspec registry-wright-2019 in executed/wright-2019/.venv/share/jupyter/kernels/registry-wright-2019
pass  reproduce_wright_2019.ipynb  (97 s)

real	1m41.666s
user	1m2.627s
sys	0m3.505s
```

**Agent**

The notebook runs clean in 97 s. I'm checking the executed outputs against my development numbers, starting with k-means, since the notebook uses scipy and not sklearn.

**Agent calls Bash**

```bash
python3 - <<'EOF'
import nbformat
nb=nbformat.read('executed/wright-2019/reproduce_wright_2019.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    tags=c.metadata.get('tags',[])
    if any(t in tags for t in ['claim:fig1e-two-clusters','claim:onset-population','claim:ramping-population','claim:fig4d-onset-patterns','claim:fig1c-total-suppression']):
        for o in c.outputs:
            if 'text' in o: print(tags, o['text'][:1500])
EOF
```

```
['claim:fig1c-total-suppression']  baseline_s zero        session     D      U        S   F    df  p_anova  t_DU     p_DU  t_US     p_US  means_ok  tests_ok
          2  one     trial mean  0.56  0.203   -0.236 190 2,174 1.87e-44   8.7 1.85e-13    12 3.14e-20     False      True
          2  one ratio of means 0.748  0.459 -0.00948 263 2,174 2.43e-53   8.9 7.22e-14  15.7 3.49e-27     False      True
          2 zero     trial mean 0.348 0.0736   -0.248 116 2,174 1.15e-32  6.61 2.98e-09  10.2 1.63e-16     False      True
          2  nan     trial mean 0.464 0.0973   -0.252 120 2,174 2.03e-33  7.48  5.6e-11  9.96 4.96e-16     False      True
         10  one     trial mean 0.787  0.508  0.00288 504 2,174 3.83e-73  12.4 6.58e-21  18.9 1.32e-32      True      True
         10  one ratio of means 0.788  0.485  -0.0108 584 2,174 6.45e-78  14.4 8.67e-25  18.9  1.4e-32      True      True
         10 zero     trial mean 0.768  0.502 -0.00167 481 2,174 1.25e-71  11.5 3.88e-19    19 9.14e-33      True      True
         10  nan     trial mean 0.783  0.506 -0.00166 495 2,174 1.49e-72  12.3 1.05e-20    19  1.1e-32      True      True
         20  one     trial mean 0.799  0.531   0.0299 595 2,174 1.59e-78  12.3 9.05e-21    21 7.81e-36      True      True
         20  one ratio of means 0.788  0.483 -0.00785 643 2,174 4.11e-81  14.2 2.18e-24  20.3 1.08e-34      True      True
         20 zero     trial mean 0.793  0.529   0.0287 586 2,174 5.32e-78  12.1 2.22e-20  20.9 1.11e-35      True      True
         20  nan     tri
['claim:fig1e-two-clusters'] baseline  scaled  LFR  HFR  F_rate   p_rate  F_halfdur  p_halfdur  F_ampratio  p_ampratio  rate_LFR  rate_HFR
 pre-cue   False  197   48     835 1.42e-80    0.00162      0.968       0.437       0.509      14.9      92.8
 pre-cue    True  198   47     824 5.16e-80      0.021      0.885        1.47       0.227      15.2      93.5
 session   False  194   51     903 8.45e-84     0.0452      0.832       0.754       0.386      4.67      2
[... 45 more lines not kept]
```

**Agent**

Executed outputs are identical to development. Now the questions file, the attempt record and the README.

**Agent calls Bash**

```bash
cat > questions/wright-2019.yaml <<'EOF'
# Questions on claims/wright-2019.yaml, asked by the author of attempt wright-2019-01 (docs/protocol.md,
# "Author", step 1.6).
dataset: crcns:pag-1
paper: doi:10.7554/elife.45013
questions:
- claim: fig1c-total-suppression
  asked: 2026-11-11
  question: >-
    Details 1 and 2 of the opening comment give two readings each for the nose poke baseline of the
    suppression ratio (2 s or 10 s before onset) and for a 0/0 ratio (set to 0, or left out). The
    regression input the Methods print for one Onset neuron fixes all three, and none is among those
    readings. Total fear is computed over a 20 s baseline, interval fear over a 2 s baseline, and a
    0/0 ratio is 1.00. Should the opening comment and the criteria that cite details 1 and 2 name
    these as the paper's method, instead of leaving them open?
  passage: >-
    Methods, Single-unit, linear regression: "To better visualize the organization of the regression
    input, the complete regression input for first interval firing of an Onset neuron is shown
    below", followed by the table of 32 trials (Z firing, interval fear, total fear, probability).
    Methods, Calculating suppression ratios: "A ratio of '1' indicated high fear, '0' low fear".
  why: >-
    One unit of the data set (rf03092316epr38bSPK12a) reproduces the table to its two decimals, but
    only with these windows. Total fear with a 2 s or 10 s baseline differs from the table by up to
    1.73 and 0.17, and with 20 s by 0.004. Interval fear with 2 s differs by 0.003 and with 10 s or
    20 s by more than 0.8. Trials with no poke in either window are 1.00 in the table. These choices
    change outcomes. With a 2 s total fear baseline the session means of fig1c-total-suppression
    fall outside tolerance (danger 0.35 to 0.75 against 0.80). The Ramping total fear beta of
    fig5f-ramping-last-interval falls to about 0 and that claim fails. The tuning curve peaks of
    fig5e and fig5j move. The attempt ran the claims file's readings and adds the table's as a
    further reading, marked as an assumption where outcomes differ. It bears also on
    fig1d-interval-suppression, fig1s1a-nose-poke-rates (which baseline Figure 1, figure supplement
    1A plots) and every regression claim.
EOF
date -u
```

```
Wed Nov 11 10:49:48 UTC 2026
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items'];print(list(o['properties'].keys()), o.get('required'))
print(list(s['properties'].keys()))
print(json.dumps(s['properties']['provenance'])[:900])
print(json.dumps(s['properties']['datasets']['items'])[:600])"
```

```
['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'proposed'] ['claim', 'outcome']
['schema_version', 'id', 'datasets', 'missing_datasets', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
{"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties": {"kind": {"enum": ["agent", "person"]}, "accountable": {"description": "The person or organisation responsible for this attempt.", "type": "object", "additionalProperties": false, "required": ["name"], "properties": {"name": {"type": "string"}, "orcid": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]$"}, "ror": {"type": "string"}}}, "agent": {"description": "Required when kind is agent.", "type": "object", "additionalProperties": false, "required": ["harness", "model", "protocol"], "properties": {"harness": {"type": "string"}, "model": {"type": "string"}, "protocol": {"description": "Version of the reproduction protocol the agent followed.", "type": "string"}}}, "runner": {"description": "Where the attempt was run: the platform, and the run that wrote this record
{"description": "A dataset the attempt used: the archive, the dataset's identifier there, the pinned version, and how the paper relates to it.", "type": "object", "additionalProperties": false, "required": ["archive", "id", "version", "relation"], "properties": {"archive": {"description": "The archive that holds the dataset, in lower case: dandi, ebrains, openneuro, dryad, zenodo, figshare and so on.", "type": "string", "pattern": "^[a-z][a-z0-9-]*$"}, "id": {"description": "The dataset's identifier in that archive, e.g. 000003 on DANDI.", "type": "string", "minLength": 1}, "version": {"descri
```

**Agent calls Write**

```json
{
 "file_path": "attempts/wright-2019-01.yaml",
 "content": "schema_version: 3\nid: wright-2019-01\ndatasets:\n- archive: crcns\n  id: pag-1\n  version: unversioned\n  doi: 10.6080/K0R49P0V\n  relation: primary\npaper: doi:10.7554/elife.45013\ndate: 2026-11-11\nentry: wright-2019\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-14\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/43001997692\noutcomes:\n- claim: fig1c-total-suppression\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig1c-total-suppression\n  measured:\n  - 0.799\n  - 0.531\n  - 0.030\n  notes: >-\n    Over 88 sessions, with the poke baseline of the 20 s before onset, 0/0 set to 1 and the mean of\n    the per-trial ratios, danger is 0.799, uncertainty 0.531 and safety 0.030. The repeated-measures\n    ANOVA of cue gives F(2,174) = 595, p = 1.6e-78. Danger against uncertainty gives t(87) = 12.3,\n    p = 9.1e-21, and uncertainty against safety t = 21.0, p = 7.8e-36 (paper F = 592.00, t = 12.36,\n    t = 20.85). Every 10 s and 20 s reading puts the three means within tolerance. The first one the\n    criterion lists (10 s, 0/0 set to 0, trial mean) gives 0.768, 0.502 and -0.002. The 2 s\n    readings do not (danger 0.35 to 0.75), though all their tests hold. The legend's 0.83 is matched\n    as well. By rat, danger ranges from 0.29 (rf08, 3 sessions) to 0.94 (rf03).\n  deviations:\n  - >-\n    The 20 s baseline and the 0/0 rule are not among the claims file's readings. They are the ones\n    the Methods regression table fixes (Methods, Single-unit, linear regression; one unit of the\n    data set reproduces the table only with them; data check of the notebook). The measured values\n    are under that reading. The claims file's readings are all shown, and a question is in\n    questions/wright-2019.yaml.\n- claim: fig1c-nonlinear-scaling\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig1c-nonlinear-scaling\n  notes: >-\n    Under every reading on which fig1c-total-suppression matched (10 s and 20 s), the uncertainty\n    mean is above the midpoint of the danger and safety means; primary reading 0.531 against 0.415.\n- claim: fig1d-interval-suppression\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig1d-interval-suppression\n  notes: >-\n    With interval fear over the 2 s baseline, 0/0 set to 1 and trial means, the cue effect is\n    F(2,174) = 493 and the cue x interval interaction F(18,1566) = 6.15, p = 9.5e-15 (paper 489.40\n    and 6.21). Danger exceeds uncertainty and uncertainty exceeds safety at p < 0.005 in all ten\n    intervals (smallest t 3.03 and 6.2; paper all t > 3.00 and > 7.00). Five of the twelve readings\n    give 10 of 10 in both comparisons. The other seven give 8 or 9 of 10 danger-uncertainty\n    intervals, which would be partially reproduced. All readings give 10 of 10 uncertainty-safety\n    intervals and both ANOVA effects.\n  deviations:\n  - >-\n    The readings differ in outcome. The one adopted (2 s baseline for interval fear, 0/0 = 1) is\n    the reading the Methods regression table fixes for interval fear. The 2 s window is reading\n    (a) of detail 1, and 0/0 = 1 is not among the claims file's readings. Asked in\n    questions/wright-2019.yaml.\n- claim: fig1s1a-nose-poke-rates\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig1s1a-nose-poke-rates\n  notes: >-\n    Under every window, poking falls from baseline to cue for danger and both uncertainty types\n    (t(87) from 10.6 to 17.6, all p < 1e-16) and not for safety (p 0.24 to 0.60). Baseline rates\n    across the four trial types do not differ with the 2 s window (F(3,261) = 2.20, p = 0.088) or\n    the 10 s window (F = 2.43, p = 0.066). They do differ with the 20 s window adopted here\n    (F = 3.47, p = 0.017), where the means are 39.6, 37.0, 39.1 and 37.8 pokes/min. Under the claims\n    file's two readings the claim is reproduced.\n  deviations:\n  - >-\n    The supplement does not say which baseline it plots. The 20 s window is adopted as an\n    assumption because it is the baseline of total fear in the Methods regression table, and the\n    one the data set's cubeScript.m stores as poke.base. The 2 s and 10 s results are shown. The\n    question is for the paper's authors (findings).\n- claim: fig1s1b-sr-poke-correlation\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig1s1b-sr-poke-correlation\n  notes: >-\n    Under every reading the suppression ratio and the cue poke rate correlate negatively over the\n    88 sessions for danger (r -0.40 to -0.73) and uncertainty (r -0.36 to -0.75), all p < 0.001, and\n    over all 264 points (r -0.52 to -0.79). Under the primary reading the safety correlation is\n    r = -0.35, p = 0.001.\n- claim: fig1e-two-clusters\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig1e-two-clusters\n  measured:\n  - 245\n  - 197\n  - 48\n  notes: >-\n    With the mean rate in the 2 s before onset and raw features (reading a, a), k-means gives 197\n    LFR and 48 HFR neurons. The baseline rate differs by cluster (F(1,243) = 835, p = 1.4e-80;\n    paper 829), and half duration (p = 0.97) and amplitude ratio (p = 0.51) do not. Z-scored\n    features give 198 and 47 (also within tolerance). The session-mean rate gives 194 and 51, with\n    HFR outside tolerance.\n  deviations:\n  - >-\n    The Methods define the waveform features in words. The peaks are picked as described in pag.py\n    (largest deflection, the opposite extreme before and after it); the waveform has no unit. The\n    k-means initialisation (k-means++ starts, 20 replicates, seed 0) is a standard choice.\n- claim: onset-population\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:onset-population\n  measured:\n  - 29\n  - 5\n  notes: >-\n    The Methods screen finds 29 Onset neurons from 5 rats (dr01 10, dr02 4, rf02 4, rf03 10, rf08\n    1), all in the LFR cluster under every clustering reading. Rounding the baseline rate down, as\n    the data set's cubeScript.m does, would give 31 from 6 rats. One Onset neuron\n    (dr02092716epr38aSPK04a) shares 66% of its spikes with another unit of its session (findings).\n- claim: ramping-population\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:ramping-population\n  measured:\n  - 17\n  - 3\n  - 14\n  - 4\n  notes: >-\n    Of the other neurons, 17 pass the screen on the last 1 s. Three are in the HFR cluster under\n    every clustering reading, and the 14 Ramping neurons come from 4 rats (dr01 4, dr02 2, rf02 1,\n    rf03 7).\n- claim: fig2a-onset-anova\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig2a-onset-anova\n  notes: >-\n    Cue F(2,56) = 8.64, p = 5.4e-4; bin F(109,3052) = 14.19; cue x bin F(218,6104) = 1.89,\n    p = 1.6e-13 (paper 1.94).\n- claim: fig2b-onset-first-interval\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig2b-onset-first-interval\n  notes: >-\n    Danger above uncertainty t(28) = 5.05, p = 2.4e-5 (paper 4.54, 9.70e-5). Uncertainty -0.09\n    against safety -0.23, t = 1.36, p = 0.185 (paper 1.37, 0.18). The uncertainty and safety ANOVA\n    over 60 bins gives cue x bin F(59,1652) = 1.41, p = 0.024 (paper 1.50, 0.01). The type-baseline\n    reading gives the same outcome. By rat, danger exceeds uncertainty in all five rats.\n- claim: fig2b-onset-last-interval\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig2b-onset-last-interval\n  notes: >-\n    Danger against uncertainty t = 1.94, p = 0.062, difference 0.24 Z (dz 0.36); uncertainty\n    against safety t = 0.58, p = 0.57, difference 0.06 (paper p = 0.10 and 0.55). The type baseline\n    gives p = 0.080 and 0.62.\n- claim: fig2c-ramping-anova\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig2c-ramping-anova\n  notes: >-\n    Cue F(2,26) = 32.10, bin F(109,1417) = 12.29, cue x bin F(218,2834) = 4.29 (paper 4.33), all\n    p < 1e-7. Last 1 s mean Z firing is danger 1.93, uncertainty 1.20 and safety -0.10.\n- claim: fig2d-ramping-first-interval\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig2d-ramping-first-interval\n  notes: >-\n    Danger against uncertainty t(13) = 0.43, p = 0.67 (difference 0.06); uncertainty against safety\n    t = 0.49, p = 0.63 (0.04). The type baseline gives p = 0.54 and 0.77.\n- claim: fig2d-ramping-last-interval\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig2d-ramping-last-interval\n  notes: >-\n    Danger above uncertainty t(13) = 3.14, p = 0.0078; uncertainty above safety t = 8.09,\n    p = 2.0e-6 (paper 3.17 and 8.26). The type baseline gives the same.\n- claim: fig2e-departure-times\n  outcome: partially_reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig2e-departure-times\n  measured:\n  - 2.7\n  - 4.5\n  - 5.1\n  - 6.4\n  notes: >-\n    Danger departs from safety before uncertainty at both thresholds under every reading. With\n    measure a and window starts (the first readings listed, given as measured), the times are 2.7,\n    4.5, 5.1 and 6.4 s against 2.8, 5.8, 5.7 and 6.5. Measure b gives 2.7, 4.7, 5.2 and 6.4 s, with\n    three of four within tolerance. Under no reading is the danger time at p < 0.00025 within\n    5.8 +- 0.58. Window ends put every time 1 s later.\n- claim: fig2e-rate-no-difference\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig2e-rate-no-difference\n  notes: >-\n    No reading of fig2e-departure-times matched in full, so both measures are shown. Measure a gives\n    danger 0.275 and uncertainty 0.288 Z/s, t(13) = -0.20, p = 0.84. Measure b gives t = -0.49,\n    p = 0.63.\n- claim: fig2s1-single-trial\n  outcome: partially_reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig2s1-single-trial\n  notes: >-\n    Onset first-interval firing exceeds the population baseline at all 32 trial positions (smallest\n    margin 5.3 spikes/s). Ramping last-interval firing exceeds it at all 22 danger and uncertainty\n    positions and at 6 of the 10 safety positions, where the criterion's reading allows at most 5.\n    Four of the six safety margins are below 3.4 spikes/s and two are 9.0 and 10.6.\n  deviations:\n  - The paper gives no rule for \"not safety trials\"; the criterion's reading (at most half) is used.\n- claim: fig2s2-nose-poke-cessation\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig2s2-nose-poke-cessation\n  notes: >-\n    With differential firing (measure b), Onset danger firing does not correlate with cessation\n    firing (R2 = 0.0006, p = 0.90) and is greater in 26 of 29 neurons (sign p = 1.5e-5). Ramping\n    gives R2 = 0.23, p = 0.080, and 14 of 14 (p = 1.2e-4; paper 1.22e-4). This holds under both ITI\n    readings (median 166 to 241 events per neuron). With raw rates (measure a) the correlations are\n    significant (R2 0.61 to 0.68), as a neuron's overall rate sets both values.\n  deviations:\n  - >-\n    The -1 interval is read as the second ending at the poke and +1 as the second after it; the\n    window from 1 s before to 2 s after the poke must lie in the ITI. The legend does not fix these.\n- claim: fig3-onset-ramping-independent\n  outcome: partially_reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig3-onset-ramping-independent\n  measured:\n  - 3\n  notes: >-\n    Three Onset-Ramping pairs share a session, in two sessions (dr01101616, one pair; dr01102316,\n    two Onset neurons with one Ramping neuron), against four pairs in four sessions in the paper.\n    None of the 30 interval regressions gives a negative beta at p < 0.05 (betas -0.33 to 0.42),\n    under both Z readings. The independence holds for the pairs found, and the pair count does not\n    match. The criterion names neither case, so the outcome is partial.\n- claim: fig4abc-onset-single-unit-biases\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig4abc-onset-single-unit-biases\n  notes: >-\n    A: r = -0.47, p = 0.010, danger greater in 22 of 29 (p = 0.008). B: r = -0.55, p = 0.002,\n    uncertainty greater in 17 of 29 (p = 0.46). C: first greater in 22 of 29 (p = 0.008), r = 0.34,\n    p = 0.070. The type baseline gives the same outcome. Both significant correlations are negative.\n    Interval Z firing has mean zero over each neuron's 32 trials, so a neuron's cue means trade off.\n    The text gives no sign.\n- claim: fig4d-onset-patterns\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig4d-onset-patterns\n  measured:\n  - 14\n  notes: >-\n    14 of 29 Onset neurons are danger > uncertainty > safety, the largest of the four categories.\n    With the three values permuted within each neuron (shuffle a), it is the only category above\n    chance under both rules (95th percentile 8.05, whisker 9.0). With each cue permuted across\n    neurons (shuffle b), its chance median is 15, and only safety > uncertainty > danger (4 against\n    3.5) is above chance. The criterion asks for one reading; the claim holds under shuffle a.\n- claim: fig4efg-ramping-single-unit-biases\n  outcome: partially_reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig4efg-ramping-single-unit-biases\n  notes: >-\n    E: danger greater in 12 of 14 (p = 0.013), but the correlation is not significant (r = -0.45,\n    p = 0.11; type baseline p = 0.17). F: r = -0.46, p = 0.094, uncertainty greater in 14 of 14\n    (p = 1.2e-4). G: last greater in 12 of 14 (p = 0.013), r = 0.28, p = 0.33. Two of three panels\n    hold.\n- claim: fig4h-ramping-patterns\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig4h-ramping-patterns\n  measured:\n  - 12\n  notes: >-\n    12 of 14 Ramping neurons are danger > uncertainty > safety, the largest category. It is the only\n    category above chance under shuffle a (95th percentile 5, whisker 6). Under shuffle b no\n    category is above chance (chance median 11).\n- claim: fig5a-onset-probability-first-interval\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig5a-onset-probability-first-interval\n  notes: >-\n    Mean betas are probability 0.863, total fear 0.024 and interval fear -0.034. Probability exceeds\n    total fear (t(28) = 3.74, p = 8.5e-4; paper 3.75) and interval fear (t = 4.55, p = 9.6e-5;\n    paper 4.57). It is above zero (p = 6.2e-5), and the fear betas are not (p = 0.79, 0.58). All 18\n    readings of details 1, 2 and 4 meet the criterion, also at 0.05.\n- claim: fig5bc-onset-beta-bias\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig5bc-onset-beta-bias\n  notes: >-\n    Probability betas are positive in 22 of 29 (sign p = 0.008). Interval fear (14 of 29, p = 1.0)\n    and total fear (17 of 29, p = 0.46) are not biased. 17 of 18 readings agree. With the table's\n    windows, 0/0 trials left out and the trial baseline, probability is 20 of 29 (p = 0.061).\n  deviations:\n  - >-\n    Outcome under the reading the Methods regression table fixes (total fear 20 s, interval fear\n    2 s, 0/0 = 1, trial baseline); one other reading differs.\n- claim: fig5d-onset-all-intervals\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig5d-onset-all-intervals\n  notes: >-\n    Regressor F(2,56) = 7.16, p = 0.0017 (paper 7.16); regressor x interval F(18,504) = 2.35,\n    p = 0.0014 (paper 2.38). The probability beta peaks in interval 1 (0.863), declines to 0.24, and\n    is above zero at p < 0.005 in intervals 1 to 4. No fear beta differs from zero in any interval\n    (smallest p 0.156). 10 of 18 readings meet the criterion. The others miss by an ANOVA effect at\n    p above 0.01, a fear beta at p below 0.005 in one interval, or a peak in interval 2.\n  deviations:\n  - Outcome under the reading the Methods regression table fixes; eight other readings differ.\n- claim: fig5s1-regressor-combinations\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig5s1-regressor-combinations\n  notes: >-\n    Under the primary reading, no fear regressor reaches significance in A, B or C under either\n    significance reading. Total fear alone (D) does (interval effect p = 0.0087, and a beta above\n    zero at p < 0.005 in at least one interval). Its first-interval and largest mean beta (0.41) is\n    below that of probability alone (0.87). A and B show a main effect of regressor (p = 0.015 and\n    0.004) with probability above fear. With the type baseline, A's regressor effect is p = 0.12\n    and the claim fails. With 2 s total fear, reading b of significance fails for D.\n  deviations:\n  - Outcome under the reading the Methods regression table fixes; the type-baseline readings differ.\n- claim: fig5e-onset-tuning-curve\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig5e-onset-tuning-curve\n  measured:\n  - 0.375\n  notes: >-\n    The mean probability beta peaks at 0.375 (0.863), with 0.25 (0.838) and 0.5 (0.808) next. With\n    2 s total fear and 0/0 set to 1 or 0, the peak is at 0.25. With the type baseline and 0/0 set to\n    0 or left out, the third value is 0.125.\n  deviations:\n  - Outcome under the reading the Methods regression table fixes; six readings differ.\n- claim: fig5s2-binary-regressor\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig5s2-binary-regressor\n  notes: >-\n    Analysis x regressor x interval F(18,504) = 2.49, p = 6.4e-4 (paper 2.51, 5.89e-4). First\n    interval analysis x regressor F(2,56) = 7.75, p = 0.0011 (paper 7.80, 1.03e-3). First-interval\n    beta 0.863 for probability against 0.675 for binary. Three readings with 2 s total fear miss\n    one interaction at p < 0.05.\n  deviations:\n  - >-\n    Outcome under the reading the Methods regression table fixes; three readings differ. The ANOVA\n    is the three-way repeated-measures design the degrees of freedom imply.\n- claim: fig5f-ramping-last-interval\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig5f-ramping-last-interval\n  notes: >-\n    Betas are probability 0.777, total fear 0.478 and interval fear -0.064. Probability vs interval\n    fear t(13) = 3.62, p = 0.0031; total fear vs interval fear t = 4.62, p = 4.8e-4; probability vs\n    total fear t = 1.14, p = 0.28. The paper reports 3.61, 4.68 and 1.11. With 2 s total fear and\n    0/0 set to 1 or 0, the total fear beta is 0.12 or less and the claim fails.\n  deviations:\n  - Outcome under the reading the Methods regression table fixes; four readings differ.\n- claim: fig5gh-ramping-beta-bias\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig5gh-ramping-beta-bias\n  notes: >-\n    Probability and total fear are each positive in 12 of 14 (p = 0.013), and their correlation is\n    r = -0.34, p = 0.24. Interval fear is positive in 6 of 14 (p = 0.79). Probability and interval\n    fear correlate at r = -0.57, p = 0.035. All four parts hold in 6 of 18 readings. The 2 s\n    readings meet one or two parts, the 10 s readings two or four.\n  deviations:\n  - Outcome under the reading the Methods regression table fixes; twelve readings differ.\n- claim: fig5i-ramping-all-intervals\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig5i-ramping-all-intervals\n  measured:\n  - 0.577\n  - 0.120\n  - -0.026\n  notes: >-\n    The per-neuron means over ten intervals are probability 0.577 +- 0.136, total fear 0.120 +- 0.100\n    and interval fear -0.026 +- 0.050 (paper 0.58 +- 0.14, 0.12 +- 0.10, -0.03 +- 0.05).\n    Regressor F(2,26) = 9.14, p = 9.9e-4; interaction F(18,234) = 2.19, p = 0.0042. Probability vs\n    zero t(13) = 4.24, p = 9.6e-4; vs total fear t = 2.35, p = 0.035; vs interval fear t = 4.37,\n    p = 7.5e-4 (paper 4.21, 2.32, 4.32). The fear means do not differ from zero (p = 0.25, 0.61).\n    The 10 s readings also meet the criterion; the measured values are under the table's reading.\n- claim: fig5s1-ramping-regressor-combinations\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig5s1-ramping-regressor-combinations\n  notes: >-\n    F and G hold. Probability means are 0.58 and 0.66 (p = 9.3e-4, 7.5e-5 against zero), the fear\n    means are not different from zero (p = 0.41, 0.92), probability exceeds fear (p = 0.029,\n    4.2e-5), and the regressor effects are p = 0.029 and 4.2e-5. Among H to J, probability alone\n    (J, 0.66, p = 1.7e-4) differs from zero, but so does total fear alone (I, 0.37, p = 0.0067).\n    Interval fear alone (H) does not (p = 0.14). With 2 s total fear, total fear alone is 0.005 to\n    0.063 and the claim holds in full.\n  deviations:\n  - Outcome under the reading the Methods regression table fixes; the six 2 s readings differ.\n- claim: fig5j-ramping-tuning-curve\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig5j-ramping-tuning-curve\n  measured:\n  - 0.625\n  notes: >-\n    The tuning curve peaks at 0.625 (0.866), just above 0.5 (0.858). With 2 s total fear and 0/0\n    set to 1 or 0, the peak is at 0.5 (partially reproduced there).\n  deviations:\n  - Outcome under the reading the Methods regression table fixes; four readings differ.\n- claim: fig6ab-post-cue-firing\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig6ab-post-cue-firing\n  notes: >-\n    Onset trial F(3,84) = 2.23, p = 0.091; bin p = 0.14; interaction p = 0.91 (paper Fs < 2.3,\n    ps > 0.09). Ramping trial F(3,39) = 14.14, bin F(44,572) = 7.11, trial x bin F(132,1716) = 3.14\n    (paper 3.14), all p < 1e-5. In the mixed ANOVA the neuron type interactions are F(3,123) = 5.70\n    (p = 0.0011), F(44,1804) = 4.17 and F(132,5412) = 2.56, all p < 0.01.\n  deviations:\n  - >-\n    The mixed ANOVA uses sums of squares with weighted means for the unequal groups (29 and 14), a\n    standard choice the paper does not state.\n- claim: fig6c-onset-post-cue-regression\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig6c-onset-post-cue-regression\n  notes: >-\n    Regressor F(1,28) = 0.51, p = 0.48 (paper 1.02, 0.32); interaction F(8,224) = 0.61, p = 0.77\n    (paper 0.53, 0.83). No beta differs from zero at p < 0.005 (smallest p 0.077). Every reading\n    gives the same (smallest p 0.0064 to 0.09).\n- claim: fig6d-ramping-post-cue-regression\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig6d-ramping-post-cue-regression\n  notes: >-\n    Regressor x interval F(8,104) = 7.00, p = 2.3e-7 (paper 5.20). The probability beta is above\n    zero in all four delay intervals (p 2.7e-6 to 7.7e-4), and its mean falls from 0.715 over the\n    delay to 0.020 after the shock. Every reading gives the same.\n- claim: fig6ef-beta-correlations\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig6ef-beta-correlations\n  measured:\n  - 3\n  - 0\n  - 1\n  - 0\n  notes: >-\n    Onset has more significant delay against post-shock correlations than Ramping at both\n    thresholds, but far fewer than reported. At p < 0.05 Onset has 3 of 20 and Ramping 0 (paper 13\n    and 4), and at p < 0.01, 1 and 0 (paper 6 and 1). No chi-square reading is significant (reading\n    a 3.16, p = 0.075, and 1.00, p = 0.32). Across readings Onset has 1 to 5 at p < 0.05. One\n    reading (0/0 left out, type baseline) gives Ramping more, which would be not reproduced.\n  deviations:\n  - Outcome under the reading the Methods regression table fixes; one reading differs.\n- claim: fig1s5-hfr-units\n  outcome: reproduced\n  notebook: reproduce_wright_2019.ipynb\n  output: claim:fig1s5-hfr-units\n  measured:\n  - 3\n  notes: >-\n    Each of the three fires most to danger in the last interval: raw 141.5, 89.3 and 89.8 spikes/s\n    against at most 120.9, 64.7 and 81.5, and likewise by interval Z.\nfindings:\n- kind: metadata_error\n  statement: >-\n    The data description says the cube's poke.base is the nose poke rate 2 s before the cue. The\n    data set's cubeScript.m computes it over the 20 s before onset, and uses it for every\n    suppression ratio in the cube, including the 1 s and 500 ms intervals.\n- kind: methods_unavailable\n  statement: >-\n    Neither the paper nor the data description states the nose poke baseline or how a 0/0\n    suppression ratio is handled. The paper's printed regression input is reproduced by one unit\n    only with a 20 s baseline for total fear, a 2 s baseline for interval fear and 0/0 set to 1.\n    Several outcomes depend on these choices. Question for the authors: are these the windows used\n    throughout, and which baseline does Figure 1, figure supplement 1A plot?\n- kind: code_mismatch\n  statement: >-\n    The data set's cubeScript.m computes interval suppression ratios over the 20 s baseline, while\n    the paper's interval fear (its regression table, and the Figure 1D statistics) uses the 2 s\n    baseline. The script also rounds the 2 s baseline firing rate down to an integer; the paper's\n    table uses the unrounded rate, and the rounded one would change the Onset screen to 31 neurons.\n- kind: metadata_error\n  statement: >-\n    The paper and the description give a mean ITI of 3.5 min, but cue onsets are 132 to 195 s apart\n    (mean about 2.7 min) in all 88 sessions, so no interval between cues reaches 3.5 min.\n- kind: other\n  statement: >-\n    Five pairs of units recorded in the same session share 66 to 90% of the spikes of one unit\n    within 0.5 ms (dr01092016 SPK10a and SPK14a; dr02092716 SPK04a and SPK15b; rf02091816 SPK01a and\n    SPK04a; rf02110216 SPK08a and SPK13a; rf03110916 SPK04a and SPK14a). They may be one neuron\n    sorted twice. The paper counts all 245 units, and one of these (dr02092716 SPK04a) is an Onset\n    neuron.\n- kind: selection_undocumented\n  statement: >-\n    The paper reports four Onset-Ramping pairs in four sessions. With the populations that match\n    the paper's counts (29 and 14), only three pairs share a session, in two sessions. The paper's\n    lists of Onset and Ramping units (Figure 1, figure supplements 4 and 6) are in figures only,\n    and the data set does not mark which units the paper placed in each population.\n- kind: methods_unavailable\n  statement: >-\n    The shuffle behind the chance levels of Figure 4D and 4H is not defined beyond \"each neurons\n    firing pattern was shuffled\". Permuting within neurons reproduces the claims, and permuting each\n    cue across neurons does not. Question for the authors: which shuffle was used?\n- kind: methods_unavailable\n  statement: >-\n    The sliding-window departure times of Figure 2E depend on the firing measure and on whether a\n    window is timed by its start or end, which the paper does not state. No reading gives the\n    Bonferroni danger time of 5.8 s (4.5 to 4.7 s by window start). Question for the authors: which\n    measure and time point were used?\n"
}
```

```
File created successfully at: attempts/wright-2019-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  cat > entries/wright-2019/README.md <<'EOF'
# Wright and McDannald (2019) from CRCNS pag-1

Tests the findings of [Wright and McDannald (2019)](https://doi.org/10.7554/eLife.45013) on
[CRCNS pag-1](https://doi.org/10.6080/K0R49P0V), which holds the spike times, event times and mean
waveforms of 245 ventrolateral periaqueductal gray units recorded in 88 fear discrimination
sessions of six rats. All 39 claims of the claims file are tested.

| Claims | Outcome |
|---|---|
| Suppression ratios, poke correlations, clusters, Onset and Ramping populations (fig1c, fig1d, fig1s1b, fig1e, populations, fig1s5) | Reproduced |
| Population and single-unit firing of Onset and Ramping neurons (fig2a to fig2d, fig2e rate, fig2s2, fig4abc, fig4d, fig4h) | Reproduced |
| Single-unit regressions on probability and fear (fig5a to fig5j except one) and after the cue (fig6ab, fig6c, fig6d) | Reproduced |
| Baseline poke rates (fig1s1a), departure times (fig2e), single trials (fig2s1), Onset-Ramping pairs (fig3), Ramping biases (fig4efg), Ramping regressor combinations (fig5s1), delay against post-shock correlations (fig6ef) | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper leaves the nose poke baseline of the suppression ratio unstated. Its printed regression
input for one Onset neuron is reproduced by one unit of the data set only with a 20 s baseline for
total fear, a 2 s baseline for interval fear and 0/0 ratios set to 1. That reading is used as the
primary one, beside the claims file's readings; several regression outcomes rest on it. The
attempt record, with the reasons and the differences from the paper's method, is
[`attempts/wright-2019-01.yaml`](../../attempts/wright-2019-01.yaml).
EOF
date -u; python tools/entry.py all entries/wright-2019 2>&1 | tail -5
```

```
Wed Nov 11 10:51:34 UTC 2026
Installed kernelspec registry-wright-2019 in executed/wright-2019/.venv/share/jupyter/kernels/registry-wright-2019
0 error(s)
pass  reproduce_wright_2019.ipynb  (95 s)
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import nbformat
nb=nbformat.read('executed/wright-2019/reproduce_wright_2019.ipynb',4)
for c in nb.cells:
    if c.cell_type=='code' and 'sanity' in c.metadata.get('tags',[]):
        for o in c.outputs:
            t=o.get('text','')
            for l in t.splitlines():
                if 'cue onsets' in l or 'run time' in l: print(l)
    if c.cell_type=='code':
        for o in c.outputs:
            if 'run time' in o.get('text',''): print(o['text'])
            if o.get('output_type')=='error': print('ERR', o['ename'])
EOF
python tools/entry.py handover entries/wright-2019 2>&1 | tail -3; ls executed/wright-2019/handover/
```

```
time between cue onsets: min 132.5 s, median 162.5 s, max 194.5 s
mean time between cue onsets 163.2 s = 2.72 min; ITI from cue offset 2.55 min
run time 1.5 min, peak memory 0.36 GB

wrote executed/wright-2019/handover
pag.py
reproduce_wright_2019.ipynb
wright-2019.yaml
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;yaml.safe_load(open('questions/wright-2019.yaml'));a=yaml.safe_load(open('attempts/wright-2019-01.yaml'));import collections;print(collections.Counter(o['outcome'] for o in a['outcomes']), sum(1 for o in a['outcomes'] if o.get('assumed')))"; git status --short; grep -c "—\|rather" attempts/wright-2019-01.yaml questions/wright-2019.yaml entries/wright-2019/README.md entries/wright-2019/pag.py; date -u
```

```
Counter({'reproduced': 32, 'partially_reproduced': 7}) 12
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
?? attempts/wright-2019-01.yaml
?? entries/wright-2019/
?? questions/wright-2019.yaml
?? scripts
attempts/wright-2019-01.yaml:0
questions/wright-2019.yaml:0
entries/wright-2019/README.md:0
entries/wright-2019/pag.py:0
Wed Nov 11 10:53:45 UTC 2026
```

**Agent calls Bash**

```bash
cd  grep -c "—\|rather" entries/wright-2019/reproduce_wright_2019.ipynb; ls -la scripts .idea 2>/dev/null | head -5; git log -1 --format=%cd
```

```
0
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 11 10:14 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 11 10:14 scripts
Wed Nov 11 05:14:24 2026 -0500
```

**Agent**

I did steps 1 to 5 of the Author section and ran the handover (step 6). All 39 claims were tested: 32 are reproduced and 7 partially reproduced; none is blocked or not reproduced. `entry.py all` passes (0 errors, notebook runs in 95 s) and the verifier's package is in `executed/wright-2019/handover/`. Nothing is committed.

**(1) Outcome per claim** (A = the outcome rests on an assumed reading)

| Claim | Outcome |
|---|---|
| fig1c-total-suppression, fig1c-nonlinear-scaling, fig1s1b, fig1e, onset-population, ramping-population, fig1s5 | reproduced |
| fig1d-interval-suppression | reproduced (A) |
| fig1s1a-nose-poke-rates | partially (A): baseline rates differ across trial types with the 20 s window, p = 0.017 |
| fig2a, fig2b first and last, fig2c, fig2d first and last, fig2e-rate, fig2s2 | reproduced |
| fig2e-departure-times | partially: danger departure at the Bonferroni threshold is 4.5 to 4.7 s against 5.8 s |
| fig2s1-single-trial | partially: Ramping firing exceeds baseline on 6 of 10 safety trials, the criterion allows 5 |
| fig3-onset-ramping-independent | partially: 3 pairs against the paper's 4; no negative betas |
| fig4abc, fig4d, fig4h | reproduced (4d and 4h only with the within-neuron shuffle) |
| fig4efg | partially: the danger/uncertainty correlation in panel E has p = 0.11 |
| fig5a, fig5i | reproduced |
| fig5bc, fig5d, fig5s1 (Onset), fig5e, fig5s2, fig5f, fig5gh, fig5j | reproduced (A) |
| fig5s1-ramping-regressor-combinations | partially (A): total fear used alone also differs from zero |
| fig6ab, fig6c, fig6d | reproduced |
| fig6ef-beta-correlations | partially (A): 3/20 and 0/20 significant against the paper's 13/20 and 4/20 |

**(2) Dataset, assumptions and questions**
- **What it holds:** 245 units, 88 sessions, 6 rats, 32 trials each, with raw spike times, events and waveforms. The paper's methods reproduce most of its statistics to the printed digits, for example Fig 5D F = 7.16 against 7.16.
- **The example neuron:** one unit (rf03092316 SPK12a) reproduces the regression input printed in the Methods. It does so only with a 20 s poke baseline for total fear, a 2 s baseline for interval fear and 0/0 ratios set to 1. None of these is among the claims file's readings. I used it as the primary reading, ran every reading the claims file names beside it, and marked 12 outcomes as assumed where the readings disagree.
- **Findings recorded:**
  - The data description says `poke.base` is the 2 s baseline, but `cubeScript.m` computes it over 20 s.
  - The script rounds the firing baseline down and uses 20 s for interval suppression ratios, both against the paper.
  - Cue onsets are 132 to 195 s apart, so no ITI reaches the stated 3.5 min mean.
  - Five within-session unit pairs share 66 to 90% of their spikes; one of these units is an Onset neuron.
  - The data set does not mark which units the paper placed in each population.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings): the baseline windows and the 0/0 rule, the Fig 4D/4H shuffle, and the Fig 2E departure measure.
- **Question for a reader:** one, in `questions/wright-2019.yaml` on fig1c-total-suppression. It asks whether details 1 and 2 of the claims file should name the windows the Methods table fixes.

**(3) Where the protocol was unclear**
1. The Methods table showed a reading the claims file does not list. The protocol does not say whether an author may add a reading the paper fixes. I ran it as a reading taken from the paper, marked outcomes as assumed where readings differ, and asked the reader.
2. "Record the first reading the criterion lists" in `measured` sits badly with a reading added from the paper. I recorded the table reading and gave the first listed reading's values in the notes.
3. Some criteria give no rule for a mixed result (fig3: count wrong, effect present; fig1s1a: one part fails). I recorded partially reproduced.
4. The data set ships the authors' own scripts. The protocol ranks "code the paper links" but says nothing about code deposited only in the data set. I used it as evidence beside the paper, which takes precedence.
5. The protocol asks to count each recording once, but the overlapping unit pairs are not identical duplicates. I kept all 245 units, as the paper does, and reported the pairs.

**(4) Runtime and failures**
The run went from 10:16 to about 10:54 UTC, well before the 14:31 cutoff. The notebook takes 1.5 min and 0.36 GB at peak. Nothing failed.

## End of run

58 turns, 35 minutes, $6.59 at API prices, result: success.
