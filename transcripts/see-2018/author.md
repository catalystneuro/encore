# see-2018 · author · run 43360769126

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries claims attempts paper | head -100
```

```
Fri Nov 13 03:49:45 UTC 2026
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
[... 112 more lines not kept]
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
ls paper entries/fouke-2025 docs; cat claims/see-2018.yaml
```

```
<persisted-output>
Output too large (49.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/5b7cec4c-0eda-4653-a203-33880f8bbc57/tool-results/bf391nc5x.txt

Preview (first 2KB):
docs:
agents
archives.md
conversion-tracker.md
design.md
encore.md
fixing-conversions.md
paper-first.md
pilot-notes
pilot-notes.md
pipeline.md
protocol.md
queue.md

entries/fouke-2025:
README.md
[... 33 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/see-2018.yaml"
}
```

```
1	# Claims for See, Atencio, Sohal & Schreiner (2018), eLife 7, e35587, on CRCNS ac-3.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-11,
3	# protocol pilot-14 as stated in docs/protocol.md. The writer did not look at the dataset's data or
4	# files; only its description on crcns.org (paper/ac-3.data-description.txt) was read, for what
5	# the dataset is meant to hold.
6	#
7	# Text read: the version of record (PMC6017807, Europe PMC full-text XML, flattened), with its
8	# figure legends, figure supplement legends and Materials and methods; and Supplementary file 1
9	# (elife-35587-supp1-v2.xlsx, the table of statistical tests with test, N and exact p for each
10	# panel), which the text file reproduces at its end. No PDF was supplied; every value used here is
11	# printed in the text, a legend or Supplementary file 1. Figure axes were not read.
12	#
13	# Code read: the paper links one repository, the dichotomized Gaussian (DG) implementation of
14	# Macke et al., https://github.com/mackelab/CorBinian, read at commit 8ebb12d (2021-07-26; the
15	# paper cites the 2017 state, which is not pinned). It holds the DG fit (findLatentGaussian01.m)
16	# and sampler (sampleDichGauss01.m) for binary vectors with given means and covariances. The
17	# paper's own analysis code (MATLAB) is not linked; the PCA/ICA code was supplied privately by
18	# Lopes-dos-Santos (Acknowledgements). The dataset's sample STRF code is the dataset's, not the
19	# paper's, and was not read.
20	#
[... 814 more lines not kept]
```

**Agent calls Bash**

```bash
cat paper/ac-3.data-description.txt; grep -n -A60 "## CRCNS" docs/archives.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=ac-3/" | python3 -c "
import sys,re
t=sys.stdin.read()
for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',t): print(s,k)
print('trunc',re.findall(r'<IsTruncated>(.*?)<',t))"
```

Result: the fetched text is not kept.

**Agent**

Listed the bucket: Data.zip is only 4.9 MB, Stimulus.zip 760 MB. Checking contents now.

**Agent calls Bash**

```bash
B=https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-3/live; curl -s $B/checksums.md5; curl -s $B/filelist.txt; python3 -c "
import fsspec,zipfile
for z in ['Data.zip','Stimulus.zip','Codes.zip']:
    f=fsspec.open('$B/'+z,block_size=2**20).open()
    for i in zipfile.ZipFile(f).infolist(): print(z,i.filename,i.file_size,i.compress_size)
"
```

```
Exit code 1
2eb66e0691862b40dd09449ff5b7c45c  Codes.zip
3140d6178de9c044932901795a4cc817  Data.zip
6c076e1642771fd58091af266d0217ce  docs/crcns_ac-3_data_description.docx
96664dd364166ac7c9458882fb3d82be  docs/crcns_ac-3_data_description.pdf
a737203b6574bff9951cc42e76576994  filelist.txt
ce43beade196882598cecddff5520d7b  Stimulus.zip
# CRCNS.org 'ac-3' dataset files
# To use this for fetching files, comment out files that are
# not needed by putting a '#' as the first character on the line (default mode)
# or put a '+' as the first character to specifiy files to be fetched (+ mode).
# mode='default' (change to '+' for + mode).
 Codes.zip	3543 (3.4 KB)
 Data.zip	4863542 (4.6 MB)
 docs/crcns_ac-3_data_description.docx	25718 (25.1 KB)
 docs/crcns_ac-3_data_description.pdf	59228 (57.8 KB)
 Stimulus.zip	761465924 (726.1 MB)
 checksums.md5	324
Traceback (most recent call last):
  File "<string>", line 2, in <module>
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q env && . env/bin/activate && uv pip install -q fsspec aiohttp requests scipy numpy h5py scikit-learn pandas matplotlib 2>&1 | tail -2; B=https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-3/live; python -c "
import fsspec,zipfile
for z in ['Data.zip','Stimulus.zip','Codes.zip']:
    f=fsspec.open('$B/'+z,block_size=2**20).open()
    for i in zipfile.ZipFile(f).infolist(): print(z,i.filename,i.file_size,i.compress_size)
"
```

```
Data.zip Data/ 0 0
Data.zip Data/site2-rn16.mat 383369 382382
Data.zip Data/site12-rn16.mat 286671 285652
Data.zip Data/site14-rn16.mat 261525 260848
Data.zip Data/site13-rn1.mat 231267 229947
Data.zip Data/site7-rn1.mat 333690 332811
Data.zip Data/site8-rn16.mat 385907 384946
Data.zip Data/site5-rn1.mat 199735 199147
Data.zip Data/site1-rn1.mat 295872 295151
Data.zip Data/site9-rn1.mat 404197 403254
Data.zip Data/site4-rn16.mat 470869 469613
Data.zip Data/site6-rn16.mat 171751 171318
Data.zip Data/site10-rn16.mat 459736 458594
Data.zip Data/site16-rn16.mat 291465 290782
Data.zip Data/site15-rn1.mat 193459 193008
Data.zip Data/site3-rn1.mat 229799 229273
Data.zip Data/site11-rn1.mat 274821 274002
Stimulus.zip Stimulus/ 0 0
Stimulus.zip Stimulus/rn1-param.mat 1000159 1000176
Stimulus.zip Stimulus/rn16-matrix.mat 374051687 372279827
[... 8 more lines not kept]
```

**Agent**

16 penetrations, one stimulus each; no repeats or 64-channel data. Opening a data file and the code.

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate; B=https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-3/live; python -c "
import fsspec,zipfile,scipy.io as sio,numpy as np,io
z=zipfile.ZipFile(fsspec.open('$B/Data.zip',block_size=2**20).open())
tot=0
for n in sorted(z.namelist()):
    if not n.endswith('.mat'): continue
    m=sio.loadmat(io.BytesIO(z.read(n)),squeeze_me=True,struct_as_record=False)
    keys=[k for k in m if not k.startswith('__')]
    spk=m['spk']; tr=m['trigger']
    tot+=len(spk)
    st=np.concatenate([s.spiketimes for s in spk])
    print(n,keys,len(spk),'trig',len(tr),tr[:2],tr[-1], 'spk ms',st.min(),st.max(), 'pos',sorted(set(np.round([s.position for s in spk]))) [:3],'..',max(s.position for s in spk),'depth',set(s.depth for s in spk),'stim',set(s.stim for s in spk),'fs',set(s.fs for s in spk))
    if n.endswith('site1-rn1.mat'):
        s=spk[0]; print(s._fieldnames); 
        for f in s._fieldnames: v=getattr(s,f); print(' ',f,type(v),np.shape(v), v if np.size(v)<5 else '')
print('total',tot)
"; python -c "
import fsspec,zipfile
z=zipfile.ZipFile(fsspec.open('$B/Codes.zip').open())
for n in z.namelist():
  if n.endswith('.m'): print('=====',n); print(z.read(n).decode())
"
```

```
Traceback (most recent call last):
  File "<string>", line 12, in <module>
    print(n,keys,len(spk),'trig',len(tr),tr[:2],tr[-1], 'spk ms',st.min(),st.max(), 'pos',sorted(set(np.round([s.position for s in spk]))) [:3],'..',max(s.position for s in spk),'depth',set(s.depth for s in spk),'stim',set(s.stim for s in spk),'fs',set(s.fs for s in spk))
                                                                                                 ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'numpy.ndarray'
===== Codes/calc_and_plot_STRFs.m

% Load rn1 stimulus matrix
fprintf('\nLoading files...\n')
load('..\Stimulus\rn1-matrix.mat')

% Load rn1 stimulus parameter file
load('..\Stimulus\rn1-param.mat')

% Load sample data set
load('..\Data\site1-rn1.mat')

% Bin spike train in 0.5 ms time bins (to match stimulus matrix)
fprintf('\nCreating spike train matrix...\n')
spktrain_mat = create_spktrain_from_stim_mat(spk, stim_mat, trigger);
[... 184 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate; B=https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-3/live; python -c "
import fsspec,zipfile,scipy.io as sio,numpy as np,io
z=zipfile.ZipFile(fsspec.open('$B/Data.zip',block_size=2**20).open())
tot=0
for n in sorted(z.namelist(), key=lambda x:(len(x),x)):
    if not n.endswith('.mat'): continue
    m=sio.loadmat(io.BytesIO(z.read(n)),squeeze_me=True,struct_as_record=False)
    keys=[k for k in m if not k.startswith('__')]
    spk=np.atleast_1d(m['spk']); tr=np.asarray(m['trigger'])
    tot+=len(spk)
    st=np.concatenate([np.atleast_1d(s.spiketimes) for s in spk])
    pos=np.array([s.position for s in spk],dtype=float)
    print(n.split('/')[1],keys,len(spk),'trig',len(tr),tr[:2],tr[-1],'dtrig',np.unique(np.diff(tr))[:4], 'spk ms %.0f %.0f'%(st.min(),st.max()),'pos %s-%s'%(pos.min(),pos.max()),'nposuniq',len(np.unique(pos)),'depth',np.unique([s.depth for s in spk]),'stim',np.unique([str(s.stim) for s in spk]),'fs',np.unique([s.fs for s in spk]),'chan',np.unique([s.probechan for s in spk]).size)
    if n.endswith('site1-rn1.mat'):
        s=spk[0]
        for f in s._fieldnames: v=getattr(s,f); print('  ',f,type(v).__name__,np.shape(v), v if np.size(v)<6 else str(v)[:80])
print('total',tot)
"
```

```
site1-rn1.mat ['spk', 'trigger'] 31 trig 1795 [20001 26668] 11979880 dtrig [6666 6667] spk ms 32 621139 pos -50.0-650.0 nposuniq 12 depth [800] stim ['rn1'] fs [20000] chan 18
   chan int () 3
   model int () 0
   depth int () 800
   position ndarray (2,) [ 50 250]
   stim str () rn1
   header str () # Model 0, number of model points = 80, number of spikes = 3731
   spiketimes ndarray (3731,) [6.05084839e+02 6.44655640e+02 1.01774237e+03 ... 6.20548312e+05
 6.20907312e+05
   outliers ndarray (273,) [   735.998047   6671.749023   8195.005859  10025.645508  11870.554688
  14334.7
   fs int () 20000
   probechan int () 32
   meanwaveform ndarray (80, 2) [[-1.00e+00  0.00e+00]
 [-9.50e-01  0.00e+00]
 [-9.00e-01 -1.30e+01]
 [-8.50e-01
site3-rn1.mat ['spk', 'trigger'] 37 trig 1795 [20001 26667] 11979896 dtrig [6666 6667] spk ms 18 621173 pos -50.0-650.0 nposuniq 13 depth [800] stim ['rn1'] fs [20000] chan 21
site5-rn1.mat ['spk', 'trigger'] 16 trig 1795 [20001 26667] 11979896 dtrig [6666 6667] spk ms 16 621180 pos -50.0-650.0 nposuniq 9 depth [800] stim ['rn1'] fs [20000] chan 10
site7-rn1.mat ['spk', 'trigger'] 43 trig 1795 [20001 26668] 11979896 dtrig [6666 6667] spk ms 12 620568 pos -50.0-650.0 nposuniq 13 depth [800] stim ['rn1'] fs [20000] chan 24
[... 14 more lines not kept]
```

**Agent**

All 655 units in 16 files, matching the paper. Now reading the paper's Methods.

**Agent calls Bash**

```bash
wc -c paper/10.7554-elife.35587.txt; grep -n -i "penetration\|ripple\|DMR\|position\|depth" paper/10.7554-elife.35587.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '{print NR": "length($0)": "substr($0,1,90)}' paper/10.7554-elife.35587.txt | head -400
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '27p;35p;37p;41p;43p;47p;55p;57p;61p;73p;77p;81p;85p;87,91p;95,103p;113p;117p;119p;123p;131,135p;139p;145p' paper/10.7554-elife.35587.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/5b7cec4c-0eda-4653-a203-33880f8bbc57/tool-results/bbmt1xd8u.txt"
}
```

```
1	We used high-density recording electrodes ( Figure 1A ) to simultaneously record the activity of populations of neurons across supragranular and granular laminae within AI columns. Presenting dynamic, broadband stimuli with varying statistics (dynamic moving ripple (DMR) or ripple noise (RN); see Materials and methods) allowed us to estimate the spectro-temporal receptive fields (STRFs) of identified neurons ( Figure 1C ). STRFs of neurons from the same columnar penetration showed general similarities in characteristic frequency and frequency tuning, and displayed minor variations in spectral and temporal details (see example in Figure 1C ), similar to cat cortical columnar recordings ( Atencio and Schreiner, 2010a ).
2	We first examined response synchrony between simultaneously recorded single units using Pearson’s correlation analysis at 10-ms temporal resolution. Pairs of neurons in the same column with similar STRFs could nonetheless exhibit widely differing pairwise correlation (PWC) functions ( Figure 1D ). For example, the PWC between pairs of neurons with similar receptive fields, recorded from channels of equal intra-pair distances, could differ in peak correlation magnitude, width and delay ( Figure 1C and D ). Pearson’s correlation values (or correlation coefficients), PWC absolute peak delays and sharpness are depicted in Figure 2A for one neuron (#15) with all other recorded neurons in the same penetration. Significant PWCs were evident for most pairs in this penetration but low correlation coefficients and broader correlation widths were dominant. Across all penetrations, PWCs were fairly heterogeneous but sharpness and delay covaried with correlation coefficients, accounting for ~50% of the variance ( Figure 2B–2D ).
3	Methods for calculating neuronal correlation. ( A ) An example neuron’s (#15) correlation with other neurons in a dataset of 31 neurons measured in three different ways. The node labels (outer circle numbers) represent the neuron numb
[... 36 more lines not kept]
```

**Agent**

Now the Methods section.

**Agent calls Bash**

```bash
sed -n '325,373p' paper/10.7554-elife.35587.txt | grep -v '^$'; sed -n '249,259p' paper/10.7554-elife.35587.txt | grep -v '^$'
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; cd entries/fouke-2025; cat entry.yaml requirements.in README.md; head -c 3000 omr.py; python3 -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
print(nb['metadata'])
for c in nb['cells'][:12]: print('----',c['cell_type'],c.get('metadata'),''.join(c['source'])[:600])
"
```

```
Fri Nov 13 03:50:48 UTC 2026
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
[... 211 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat papers/datasets/see-2018.yaml; grep -n see-2018 papers/keys.yaml; ls questions | head; cat attempts/fouke-2025-01.yaml | head -150
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.7554/elife.35587
title: Coordinated neuronal ensembles in primary auditory cortical columns
datasets:
- archive: crcns
  id: ac-3
  relation: primary
333:  10.7554/elife.35587: see-2018
README.md
ashworth-2025.yaml
athalye-2023.yaml
bech-2026.yaml
bellvila-2026.yaml
bennett-2024.yaml
berg-2020.yaml
boran-2022.yaml
bouchard-2013.yaml
brudner-2026.yaml
schema_version: 3
[... 149 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '150,400p' attempts/fouke-2025-01.yaml | grep -n -A40 "^findings\|^verifications\|blocked" | head -120; ls schemas;
```

```
50:  outcome: blocked
51:  blocked_by: metadata_insufficient
52-  notes: The numbers come from single representative fish and trials. Fig1-S1.ipynb selects them
53-    by the index of a data folder and a trial number (for example DC folder 29, trial 79), and the
54-    dandiset gives no mapping from those folders to its subjects, nor the original file names.
55-- claim: fig2d-shared-architecture
56:  outcome: blocked
57:  blocked_by: data_missing
58-  notes: The two-photon imaging data are not in the dandiset, which holds only freely swimming
59-    tracking. The GitLab repository the paper names for "all behavioral and imaging data" holds
60-    notebooks only, and no other dandiset of this lab or paper was found on the archive.
61-- claim: fig2g-dsi-similar
62:  outcome: blocked
63:  blocked_by: data_missing
64-  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
65-- claim: fig2h-fewer-motion-responsive
66:  outcome: blocked
67:  blocked_by: data_missing
68-  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
69-- claim: fig2k-more-monocular
[... 104 more lines not kept]
```

**Agent**

Data layout is clear. Now the stimulus files.

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate; B=https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-3/live; time python -c "
import fsspec,zipfile,scipy.io as sio,numpy as np,io
z=zipfile.ZipFile(fsspec.open('$B/Stimulus.zip',block_size=2**22).open())
for n in ['Stimulus/rn1-param.mat','Stimulus/rn16-param.mat']:
    m=sio.loadmat(io.BytesIO(z.read(n)),squeeze_me=True)
    for k,v in m.items():
        if k.startswith('__'): print(k,v if k=='__header__' else ''); continue
        print(n,k,type(v).__name__,np.shape(v),np.asarray(v).dtype, v if np.size(v)<4 else (np.min(v),np.max(v), np.asarray(v).ravel()[:5]))
f=z.open('Stimulus/rn1-matrix.mat'); print(f.read(200))
"
```

```
__header__ b'MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Tue Mar 27 14:15:38 2018'
__version__ 
__globals__ 
Stimulus/rn1-param.mat FM ndarray (65536,) float64 (np.float64(-39.99979497515828), np.float64(39.99948742560462), array([5.22252916, 5.1617934 , 5.09980767, 5.03660035, 4.97219984]))
Stimulus/rn1-param.mat MaxFM int () int64 40
Stimulus/rn1-param.mat MaxRD int () int64 4
Stimulus/rn1-param.mat NF int () int64 64
Stimulus/rn1-param.mat NT int () int64 667
Stimulus/rn1-param.mat RD ndarray (65536,) float64 (np.float64(0.0), np.float64(3.9999497812603817), array([2.08449538, 2.08375426, 2.08300606, 2.08225087, 2.08148878]))
Stimulus/rn1-param.mat f1 int () int64 500
Stimulus/rn1-param.mat f2 int () int64 40000
Stimulus/rn1-param.mat faxis ndarray (64,) float64 (np.float64(500.0), np.float64(40000.00000000001), array([500.        , 536.01603504, 574.62637965, 616.0179073 ,
       660.39095238]))
Stimulus/rn1-param.mat taxis ndarray (667,) float64 (np.float64(0.0), np.float64(0.333), array([0.    , 0.0005, 0.001 , 0.0015, 0.002 ]))
__header__ b'MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Tue Mar 27 14:17:32 2018'
__version__ 
__globals__ 
Stimulus/rn16-param.mat FM ndarray (16, 65536) float64 (np.float64(-40.0), np.float64(40.0), array([-21.25176894, -20.53788234, -19.82030508, -19.09921921,
       -18.3748098 ]))
Stimulus/rn16-param.mat MaxFM int () int64 40
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate; B=https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-3/live; /usr/bin/time -v python -c "
import fsspec,zipfile,scipy.io as sio,numpy as np,io,time
t=time.time()
z=zipfile.ZipFile(fsspec.open('$B/Stimulus.zip',block_size=2**24).open())
b=z.read('Stimulus/rn1-matrix.mat'); print('read',time.time()-t, len(b))
m=sio.loadmat(io.BytesIO(b)); del b
s=m['stim_mat']; print(s.shape,s.dtype,s.min(),s.max(),s[:,:3].ravel()[:5], time.time()-t)
print(s.shape[1]/667, np.unique(np.round(s[:, :2000].ravel(),3))[:10])
" 2>&1 | egrep -v "^\s+(Page|Vol|Invol|Swaps|File|Socket|Signals|Average|Exit|Minor|Major|Percent|Elapsed \(wall|System|User)"
```

```
read 9.1439208984375 373658601
(64, 1197265) float64 -20.0 19.99999999999998 [ 0.65438151  0.95509648  1.25559449 19.50128645 19.56577346] 12.24635100364685
1795.0 [-20.    -19.999 -19.998 -19.997 -19.996 -19.995 -19.994 -19.993 -19.992
 -19.991]
	Command being timed: "python -c 
import fsspec,zipfile,scipy.io as sio,numpy as np,io,time
t=time.time()
z=zipfile.ZipFile(fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-3/live/Stimulus.zip',block_size=2**24).open())
b=z.read('Stimulus/rn1-matrix.mat'); print('read',time.time()-t, len(b))
m=sio.loadmat(io.BytesIO(b)); del b
s=m['stim_mat']; print(s.shape,s.dtype,s.min(),s.max(),s[:,:3].ravel()[:5], time.time()-t)
print(s.shape[1]/667, np.unique(np.round(s[:, :2000].ravel(),3))[:10])
"
	Maximum resident set size (kbytes): 1414732
Shell cwd was reset to
```

**Agent**

Stimulus streams in about 12 s (64 × 1,197,265 at 0.5 ms, ±20 dB). Checking unit positions next.

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate; B=https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-3/live; python -c "
import fsspec,zipfile,scipy.io as sio,numpy as np,io
z=zipfile.ZipFile(fsspec.open('$B/Data.zip',block_size=2**20).open())
for n in ['Data/site1-rn1.mat','Data/site10-rn16.mat','Data/site13-rn1.mat','Data/site14-rn16.mat']:
    spk=np.atleast_1d(sio.loadmat(io.BytesIO(z.read(n)),squeeze_me=True,struct_as_record=False)['spk'])
    P=np.array([s.position for s in spk]); ch=np.array([s.chan for s in spk]); pc=np.array([s.probechan for s in spk])
    print(n, sorted(set(map(tuple,np.c_[P,pc].tolist())))) 
    print('  chan',sorted(set(zip(ch.tolist(),pc.tolist()))))
    print('  nspk',[len(np.atleast_1d(s.spiketimes)) for s in spk][:40])
    print('  sorted?',all(np.all(np.diff(s.spiketimes)>=0) for s in spk),'header',spk[0].header,'model',[s.model for s in spk][:20])
"
```

```
Data/site1-rn1.mat [(-50, 300, 4), (-50, 350, 5), (-50, 400, 6), (-50, 450, 7), (-50, 500, 8), (-50, 550, 9), (-50, 600, 10), (0, 450, 14), (0, 550, 13), (0, 600, 21), (0, 650, 12), (50, 250, 32), (50, 300, 29), (50, 450, 26), (50, 500, 25), (50, 550, 24), (50, 600, 23), (50, 650, 22)]
  chan [(1, 24), (3, 32), (5, 29), (6, 25), (7, 23), (8, 21), (9, 22), (14, 26), (17, 4), (18, 14), (20, 7), (22, 6), (23, 10), (24, 12), (25, 8), (27, 5), (28, 9), (29, 13)]
  nspk [3731, 5518, 2328, 620, 1998, 3101, 1685, 2162, 852, 4176, 581, 1111, 2256, 977, 904, 425, 906, 1035, 890, 531, 2919, 6513, 3919, 953, 589, 755, 1298, 6737, 5016, 6355, 1399]
  sorted? True header # Model 0, number of model points = 80, number of spikes = 3731 model [0, 1, 1, array([1, 2], dtype=uint8), 3, array([0, 1], dtype=uint8), 2, 3, array([0, 1], dtype=uint8), 2, 0, 1, 5, 3, 4, 1, 2, 2, 0, 0]
Data/site10-rn16.mat [(-50, 160, 3), (-50, 210, 2), (-50, 260, 1), (-50, 310, 4), (-50, 360, 5), (-50, 410, 6), (-50, 460, 7), (-50, 510, 8), (-50, 560, 9), (-50, 610, 10), (-50, 660, 11), (0, 410, 19), (0, 560, 13), (0, 610, 21), (0, 660, 12), (50, 160, 30), (50, 260, 32), (50, 360, 28), (50, 410, 27), (50, 460, 26), (50, 510, 25), (50, 560, 24), (50, 610, 23), (50, 660, 22)]
  chan [(1, 24), (2, 19), (3, 32), (6, 25), (7, 23), (8, 21), (9, 22), (10, 27), (11, 28), (12, 30), (14, 26), (17, 4), (19, 11), (20, 7), (21, 3), (22, 6), (23, 10), (24, 12), (25, 8), (26, 2), (27, 5), (28, 9), (29, 13), (30, 1)]
  nspk [729, 9137, 347, 594, 893, 801, 3014, 932, 1841, 8094, 565, 109, 193, 1819, 3494, 2125, 399, 3847, 3627, 4904, 2791, 2911, 891, 3866, 5805, 14425, 142, 3833, 152, 14509, 977, 1211, 381, 299, 3101, 1589, 2116, 9656]
  sorted? True header # Model 0, number of model points = 80, number of spikes = 729 model [array([0, 2, 3, 1], dtype=uint8), array([1, 0], dtype=uint8), array([2, 3], dtype=uint8), 0, 2, 0, 1, 1, 2, 0, array([0, 1], dtype=uint8), 3, 0, 2, 2, array([0, 4, 2], dtype=uint8), 6, array([0, 1, 2, 3
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate; B=https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-3/live; python -c "
import fsspec,zipfile,scipy.io as sio,numpy as np,io
z=zipfile.ZipFile(fsspec.open('$B/Data.zip',block_size=2**20).open())
def L(i):
    n=[x for x in z.namelist() if x.split('/')[-1].startswith('site%d-'%i)][0]
    return np.atleast_1d(sio.loadmat(io.BytesIO(z.read(n)),squeeze_me=True,struct_as_record=False)['spk'])
for a in range(1,17):
  for b in range(a+1,17):
    A,Bb=L(a),L(b)
    best=[]
    for u in A:
        wa=np.asarray(u.meanwaveform,float); wa=wa[:,1] if wa.ndim==2 else wa
        cs=[]
        for v in Bb:
            if v.probechan!=u.probechan: continue
            wb=np.asarray(v.meanwaveform,float); wb=wb[:,1] if wb.ndim==2 else wb
            cs.append(np.corrcoef(wa,wb)[0,1])
        best.append(max(cs) if cs else np.nan)
    best=np.array(best)
    if np.nanmean(best>0.99)>0.3 or (b==a+1 and a%2==1): print(a,b,'units',len(A),len(Bb),'frac A units with r>0.99 waveform on same chan: %.2f'%np.nanmean(best>0.99), 'median best r %.3f'%np.nanmedian(best), 'identical wf', np.nansum(best>0.99999))
"
```

```
1 2 units 31 53 frac A units with r>0.99 waveform on same chan: 0.00 median best r 0.834 identical wf 0
3 4 units 37 61 frac A units with r>0.99 waveform on same chan: 0.00 median best r 0.778 identical wf 0
5 6 units 16 25 frac A units with r>0.99 waveform on same chan: 0.00 median best r 0.822 identical wf 0
7 8 units 43 61 frac A units with r>0.99 waveform on same chan: 0.00 median best r 0.850 identical wf 0
9 10 units 41 38 frac A units with r>0.99 waveform on same chan: 0.00 median best r 0.852 identical wf 0
11 12 units 42 45 frac A units with r>0.99 waveform on same chan: 0.00 median best r 0.774 identical wf 0
13 14 units 40 44 frac A units with r>0.99 waveform on same chan: 0.00 median best r 0.645 identical wf 0
15 16 units 29 49 frac A units with r>0.99 waveform on same chan: 0.00 median best r 0.843 identical wf 0
Shell cwd was reset to
```

**Agent**

No unit is deposited twice (no waveform matches across files), though site pairs share tip depths. Writing the helper module now.

**Agent calls Bash**

```bash
date -u; nproc; free -g | head -2; ls tools; grep -n "def \|argparse\|add_parser" tools/entry.py | head -60
```

```
Fri Nov 13 03:54:36 UTC 2026
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          11           0           2          14
__pycache__
agent_run.py
archive_transcripts.sh
archives
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_reuse_targets.py
build_site.py
build_targets.py
changed_entries.py
claims_check.py
colab.py
[... 53 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "tools/entry.py",
 "offset": 179,
 "limit": 230
}
```

```
179	def check(entry_dir: Path) -> Report:
180	    report = Report()
181	    rel = entry_dir.relative_to(ROOT)
182	    entry = validate(report, entry_dir / "entry.yaml", "entry")
183	    if entry is None:
184	        return report
185	    if entry.get("name") != entry_dir.name:
186	        report.error(rel / "entry.yaml", f"name {entry.get('name')!r} must match the directory name")
187	
188	    listed = [n["path"] for n in entry.get("notebooks", [])]
189	    present = sorted(p.name for p in entry_dir.glob("*.ipynb"))
190	    for name in sorted(set(present) - set(listed)):
191	        report.error(rel / name, "notebook is not listed in entry.yaml")
192	    for name in sorted(set(listed) - set(present)):
193	        report.error(rel / "entry.yaml", f"listed notebook {name!r} does not exist")
194	    helpers = entry.get("helpers", [])
195	    for name in helpers:
196	        if not (entry_dir / name).is_file():
197	            report.error(rel / "entry.yaml", f"listed helper {name!r} does not exist")
198	
[... 210 more lines not kept]
```

**Agent**

Now writing the helper module.

**Agent calls Write**

```json
{
 "file_path": "entries/see-2018/cne.py",
 "content": "\"\"\"Loading and cNE measures for CRCNS ac-3 (See, Atencio & Schreiner), used by See et al. (2018).\n\nSee JZ, Atencio CA, Sohal VS, Schreiner CE (2018). Coordinated neuronal ensembles in primary\nauditory cortical columns. eLife 7:e35587, doi:10.7554/eLife.35587.\n\nThe data set CRCNS ac-3 (doi:10.6080/K09021X1) is not versioned; it is read as `unversioned`\nfrom the public bucket crcnsarchive, under ac-3/live/, by opening the zip files in place over\nrange requests. Nothing is written to disk. Data.zip holds one MATLAB file per recording\n(`site<k>-<stim>.mat`, 16 files): `spk`, one struct per unit (spike times in ms, `position` as\n[lateral offset, depth below the surface] in um, `probechan`, `meanwaveform`), and `trigger`,\nthe stimulus triggers in samples at 20 kHz. Stimulus.zip holds the stimulus envelopes\n(`stim_mat`, 64 carriers by 0.5-ms columns, 667 columns per trigger) for rn1 (the DMR) and rn16\n(the RN, the sum of 16 DMRs).\n\nWhere the parameters come from:\n\n- cNE detection (`detect`) follows the claims file's opening comment, from Materials and\n  methods, Detection of coordinated neuronal ensembles: 10-ms bins, z-scored rows, eigenvalues\n  of the correlation matrix above the Marcenko-Pastur bound (1 + sqrt(n/T))^2 (the claims file's\n  reading, Lopes-dos-Santos et al. 2013), fastICA on the significant PCs, membership at the mean\n  plus or minus 1.5 SD of the IC weights from 100 circular shuffles (ICA on the N largest PCs of\n  each), activity threshold at the 99.9th percentile of the real ICs projected on the shuffles.\n  The fastICA settings (logcosh contrast, unit-variance whitening, at most 1000 iterations,\n  tolerance 1e-6) and the random seeds are standard choices that the paper does not fix.\n- IC scale and sign, and the activity projection, have the two readings each of the claims file\n  (`SIGN_READINGS`, `PROJECTIONS`).\n- The analysis window of each recording is the stimulus: from the first trigger to one stimulus\n  period (667 columns) after the last. Spikes outside it are left out. Spike times are put on the\n  stimulus clock (`to_stim_ms`), interpolating between triggers, so that every binned train is\n  aligned with the stimulus columns; this clock runs 0.05% slower than the recording clock.\n- PWCs (`pwc`) are histograms of spike-time differences on the recording clock, with the lag\n  bins and ranges of the claims file (1 ms over +-50 or +-100 ms). Sharpness is the median of\n  the absolute lag from the peak, weighted by the counts (Figure 6G to I legend); peak delay is\n  the absolute lag of the maximum, the first maximum on ties.\n- STRFs are spike- or event-triggered averages of the stimulus envelope. The window and\n  resolution are not given by the paper. The data set's own STRF code (Codes.zip,\n  calc_and_plot_STRFs.m, written by the first author) uses 0.5-ms columns and 100 lags (50 ms);\n  its segment code notes that \"for AI cells, and 5 ms bins, nlags = 20 is sufficient\". Here the\n  stimulus is averaged to `STRF_BIN_MS` = 5-ms bins with `STRF_LAGS` = 20 lags (100 ms), the\n  first author's stated choice, an assumption stated in the notebook. The temporal profiles of\n  Figure 6B, E use a 1-ms version (`strf_1ms`), 50 lags, as in the sample code's 50 ms.\n- STRF mutual information (`strf_mi`) follows Materials and methods, STRF mutual information:\n  projections z = s . STRF, P(z) from all stimulus segments, P(z|event) from the segments before\n  events, both normalised by the mean and SD of P(z), MI extrapolated from 20 random subsamples at\n  90, 95, 97.5, 99 and 100% of the events against the inverse fraction. The projection bins,\n  `MI_BINS` = 25 equal bins over -5 to 5 SD with the tails pooled into the end bins, are a\n  standard choice.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport io\nimport re\nimport zipfile\n\nimport fsspec\nimport numpy as np\nimport scipy.io as sio\nfrom scipy import stats\nfrom sklearn.decomposition import FastICA\n\nDATASET = \"ac-3\"\nVERSION = \"unversioned\"\nBASE = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-3/live\"\nFS = 20000.0              # trigger sampling rate, data descriptor\nNT = 667                  # stimulus columns per trigger, rnX-param.mat\nCOL_MS = 0.5              # stimulus column width on the stimulus clock, taxis in rnX-param.mat\nBIN_MS = 10               # cNE detection bin, Materials and methods\nN_SHUFFLES = 100          # Materials and methods\nMEMBER_SD = 1.5           # Materials and methods\nACTIVITY_PCT = 99.9       # Materials and methods\nSTRF_BIN_MS = 5           # assumption, the first author's sample code (see docstring)\nSTRF_LAGS = 20\nMI_BINS = np.linspace(-5, 5, 26)\nMI_FRACTIONS = (0.90, 0.95, 0.975, 0.99, 1.0)   # Materials and methods\nMI_ITER = 20\nSIGN_READINGS = (\"a\", \"b\")      # (a) largest |weight| positive; (b) as fastICA returns it\nPROJECTIONS = (\"quadratic\", \"linear\")\n\n\n# --- loading ---------------------------------------------------------------------------------\n\ndef _zip(name: str) -> zipfile.ZipFile:\n    return zipfile.ZipFile(fsspec.open(f\"{BASE}/{name}\", block_size=2**22).open())\n\n\ndef load_sites() -> list[dict]:\n    \"\"\"All 16 recordings of Data.zip, in site order, reduced to what the analysis uses.\"\"\"\n    z = _zip(\"Data.zip\")\n    sites = []\n    for name in z.namelist():\n        m = re.search(r\"site(\\d+)-(rn\\d+)\\.mat$\", name)\n        if not m:\n            continue\n        mat = sio.loadmat(io.BytesIO(z.read(name)), squeeze_me=True, struct_as_record=False)\n        spk = np.atleast_1d(mat[\"spk\"])\n        trig = np.asarray(mat[\"trigger\"], dtype=float).ravel()\n        units = []\n        for s in spk:\n            pos = np.asarray(s.position, dtype=float).ravel()\n            units.append({\"spikes_ms\": np.asarray(s.spiketimes, dtype=float).ravel(),\n                          \"x\": pos[0], \"depth\": pos[1], \"probechan\": int(s.probechan),\n                          \"chan\": int(s.chan), \"tip_depth\": float(s.depth), \"stim\": str(s.stim),\n                          \"fs\": float(s.fs)})\n        sites.append({\"site\": int(m.group(1)), \"stim\": m.group(2), \"file\": name.split(\"/\")[-1],\n                      \"trigger\": trig, \"units\": units})\n    return sorted(sites, key=lambda s: s[\"site\"])\n\n\ndef load_stimulus(name: str) -> np.ndarray:\n    \"\"\"The stimulus envelope `stim_mat` of rn1 or rn16 (64 carriers by 0.5-ms columns), float32.\"\"\"\n    z = _zip(\"Stimulus.zip\")\n    raw = z.read(f\"Stimulus/{name}-matrix.mat\")\n    stim = sio.loadmat(io.BytesIO(raw))[\"stim_mat\"]\n    del raw\n    return np.asarray(stim, dtype=np.float32)\n\n\ndef load_params(name: str) -> dict:\n    z = _zip(\"Stimulus.zip\")\n    m = sio.loadmat(io.BytesIO(z.read(f\"Stimulus/{name}-param.mat\")), squeeze_me=True)\n    return {k: v for k, v in m.items() if not k.startswith(\"__\")}\n\n\ndef downsample(stim: np.ndarray, bin_ms: float) -> np.ndarray:\n    \"\"\"Average 0.5-ms columns into bins of `bin_ms` on the stimulus clock; a partial last bin is dropped.\"\"\"\n    k = int(round(bin_ms / COL_MS))\n    n = stim.shape[1] // k\n    return stim[:, :n * k].reshape(stim.shape[0], n, k).mean(axis=2)\n\n\n# --- clocks and binning ------------------------------------------------------------------------\n\ndef to_stim_ms(site: dict, spikes_ms: np.ndarray) -> np.ndarray:\n    \"\"\"Spike times (recording ms) to the stimulus clock: ms since the first trigger, measured in\n    0.5-ms stimulus columns, interpolated between triggers. Times outside the stimulus are NaN.\"\"\"\n    trig_ms = site[\"trigger\"] / FS * 1000.0\n    period = np.median(np.diff(trig_ms))\n    knots = np.append(trig_ms, trig_ms[-1] + period)\n    cols = np.interp(spikes_ms, knots, np.arange(len(knots)) * NT, left=np.nan, right=np.nan)\n    return cols * COL_MS\n\n\ndef stim_duration_ms(site: dict) -> float:\n    return len(site[\"trigger\"]) * NT * COL_MS\n\n\ndef binned(site: dict, bin_ms: float, units=None, t_range=None) -> np.ndarray:\n    \"\"\"Spike counts (units by bins) on the stimulus clock.\"\"\"\n    dur = stim_duration_ms(site)\n    lo, hi = t_range if t_range is not None else (0.0, dur)\n    n = int(np.floor((hi - lo) / bin_ms))\n    edges = lo + np.arange(n + 1) * bin_ms\n    us = site[\"units\"] if units is None else [site[\"units\"][i] for i in units]\n    out = np.zeros((len(us), n), dtype=np.float32)\n    for i, u in enumerate(us):\n        t = u[\"stim_ms\"]\n        out[i] = np.histogram(t[np.isfinite(t)], edges)[0]\n    return out\n\n\ndef prepare(site: dict) -> None:\n    \"\"\"Add stimulus-clock spike times to every unit.\"\"\"\n    for u in site[\"units\"]:\n        u[\"stim_ms\"] = to_stim_ms(site, u[\"spikes_ms\"])\n\n\n# --- cNE detection -----------------------------------------------------------------------------\n\ndef zscore(counts: np.ndarray) -> np.ndarray:\n    m = counts.mean(axis=1, keepdims=True)\n    s = counts.std(axis=1, keepdims=True)\n    s[s == 0] = 1.0\n    return ((counts - m) / s).astype(np.float32)\n\n\ndef mp_bound(n: int, t: int) -> float:\n    return (1.0 + np.sqrt(n / t)) ** 2\n\n\ndef _ica_weights(z: np.ndarray, vecs: np.ndarray, seed: int) -> np.ndarray:\n    \"\"\"fastICA on the projection of z onto the PCs `vecs` (n by N); IC weights (n by N), unit length.\"\"\"\n    proj = vecs.T @ z\n    if vecs.shape[1] == 1:\n        w = vecs.copy()\n    else:\n        ica = FastICA(n_components=vecs.shape[1], whiten=\"unit-variance\", fun=\"logcosh\",\n                      max_iter=1000, tol=1e-6, random_state=seed)\n        ica.fit(proj.T)\n        w = vecs @ ica.components_.T\n    return w / np.linalg.norm(w, axis=0, keepdims=True)\n\n\ndef orient(w: np.ndarray, reading: str) -> np.ndarray:\n    \"\"\"Reading (a): sign set so that the largest absolute weight is positive. Reading (b): unchanged.\"\"\"\n    if reading == \"b\":\n        return w\n    s = np.sign(w[np.abs(w).argmax(axis=0), np.arange(w.shape[1])])\n    s[s == 0] = 1\n    return w * s\n\n\ndef pcs(z: np.ndarray):\n    c = (z @ z.T) / z.shape[1]\n    vals, vecs = np.linalg.eigh(c)\n    order = np.argsort(vals)[::-1]\n    return vals[order], vecs[:, order]\n\n\ndef n_cnes(counts: np.ndarray) -> int:\n    \"\"\"Number of eigenvalues above the Marcenko-Pastur bound (the number of cNEs).\"\"\"\n    keep = counts.std(axis=1) > 0\n    z = zscore(counts[keep])\n    vals, _ = pcs(z)\n    return int((vals > mp_bound(z.shape[0], z.shape[1])).sum())\n\n\ndef circular_shuffle(counts: np.ndarray, rng: np.random.Generator) -> np.ndarray:\n    t = counts.shape[1]\n    shifts = rng.integers(1, t, size=counts.shape[0])\n    idx = (np.arange(t)[None, :] - shifts[:, None]) % t\n    return np.take_along_axis(counts, idx, axis=1)\n\n\ndef activity(z: np.ndarray, w: np.ndarray, projection: str) -> np.ndarray:\n    \"\"\"cNE activity (N by T). Quadratic: z' P z with P = w w' and its diagonal set to zero\n    (Lopes-dos-Santos et al. 2013). Linear: w . z.\"\"\"\n    lin = w.T @ z\n    if projection == \"linear\":\n        return lin\n    return lin ** 2 - (w ** 2).T @ (z ** 2)\n\n\ndef detect(counts: np.ndarray, seed: int, n_shuffles: int = N_SHUFFLES, null: bool = True,\n           activity_null: bool = True) -> dict:\n    \"\"\"cNE detection of the claims file's opening comment on a units-by-bins count matrix.\n\n    Returns the number of cNEs, the raw IC weights (reading b), and, with `null`, per sign reading\n    the membership thresholds and the members, and the shuffled IC weights (for the\n    interleaved-halves null); with `activity_null`, the 99.9th percentile activity thresholds per\n    projection reading. Units without spikes are left out and reported in `kept`.\"\"\"\n    rng = np.random.default_rng(seed)\n    keep = np.flatnonzero(counts.std(axis=1) > 0)\n    z = zscore(counts[keep])\n    n, t = z.shape\n    vals, vecs = pcs(z)\n    k = int((vals > mp_bound(n, t)).sum())\n    out = {\"n\": k, \"kept\": keep, \"n_units\": counts.shape[0], \"eigenvalues\": vals,\n           \"bound\": mp_bound(n, t)}\n    if k == 0:\n        out[\"w\"] = np.zeros((n, 0))\n        return out\n    w = _ica_weights(z, vecs[:, :k], seed)\n    out[\"w\"] = w\n    if not null:\n        return out\n    shuf_w = []\n    act = {p: [] for p in PROJECTIONS}\n    oriented = {r: orient(w, r) for r in SIGN_READINGS}\n    for i in range(n_shuffles):\n        zs = circular_shuffle(z, rng)\n        _, sv = pcs(zs)\n        shuf_w.append(_ica_weights(zs, sv[:, :k], seed + 1 + i))\n        if activity_null:\n            for p in PROJECTIONS:\n                act[p].append(activity(zs, oriented[\"a\"], p))\n    out[\"shuffled_w\"] = shuf_w\n    out[\"members\"], out[\"thresholds\"] = {}, {}\n    for r in SIGN_READINGS:\n        null_w = np.concatenate([orient(sw, r).ravel() for sw in shuf_w])\n        lo = null_w.mean() - MEMBER_SD * null_w.std()\n        hi = null_w.mean() + MEMBER_SD * null_w.std()\n        wr = oriented[r]\n        out[\"thresholds\"][r] = (lo, hi)\n        out[\"members\"][r] = [{\"pos\": keep[wr[:, j] > hi], \"neg\": keep[wr[:, j] < lo]} for j in range(k)]\n    if activity_null:\n        out[\"act_threshold\"] = {p: np.percentile(np.concatenate(act[p], axis=1), ACTIVITY_PCT, axis=1)\n                                for p in PROJECTIONS}\n    return out\n\n\ndef member_sets(det: dict, reading: str = \"a\") -> list[np.ndarray]:\n    \"\"\"Members (positive and negative) of each cNE, as unit indices of the recording.\"\"\"\n    return [np.union1d(m[\"pos\"], m[\"neg\"]) for m in det[\"members\"][reading]]\n\n\ndef events_from_activity(act: np.ndarray, threshold: float, reading: str) -> np.ndarray:\n    \"\"\"Indices of events. Reading (a): every sample above threshold. Reading (b): one per run of\n    samples above threshold, at its peak.\"\"\"\n    above = act > threshold\n    if reading == \"a\":\n        return np.flatnonzero(above)\n    d = np.diff(np.r_[0, above.astype(int), 0])\n    starts, ends = np.flatnonzero(d == 1), np.flatnonzero(d == -1)\n    return np.array([s + np.argmax(act[s:e]) for s, e in zip(starts, ends)], dtype=int)\n\n\ndef interp_activity(act: np.ndarray, bin_ms: float, n_ms: int) -> np.ndarray:\n    \"\"\"Activity on bins of `bin_ms` linearly interpolated to 1 ms (Materials and methods, STRF MI),\n    each value placed at its bin centre.\"\"\"\n    centres = (np.arange(len(act)) + 0.5) * bin_ms\n    return np.interp(np.arange(n_ms) + 0.5, centres, act)\n\n\n# --- pairwise correlation functions ------------------------------------------------------------\n\ndef pwc(a: np.ndarray, b: np.ndarray, max_lag: float, bin_ms: float = 1.0) -> np.ndarray:\n    \"\"\"Histogram of b - a spike-time differences in bins of `bin_ms` centred on 0, over +-max_lag.\"\"\"\n    edges = np.arange(-max_lag - bin_ms / 2, max_lag + bin_ms, bin_ms)\n    b = np.sort(b)\n    idx = np.searchsorted(b, a[:, None] + edges[None, :])\n    return np.diff(idx, axis=1).sum(axis=0)\n\n\ndef pwc_measures(counts: np.ndarray, bin_ms: float = 1.0) -> tuple[float, float]:\n    \"\"\"(sharpness, absolute peak delay) in ms: the PWC folded at its peak, sharpness the lag from the\n    peak at the median of the folded count distribution (Figure 6G to I).\"\"\"\n    lags = (np.arange(len(counts)) - (len(counts) - 1) / 2) * bin_ms\n    if counts.sum() == 0:\n        return np.nan, np.nan\n    peak = lags[np.argmax(counts)]\n    dist = np.abs(lags - peak)\n    order = np.argsort(dist, kind=\"stable\")\n    cum = np.cumsum(counts[order])\n    sharp = dist[order][np.searchsorted(cum, cum[-1] / 2.0)]\n    return float(sharp), float(abs(peak))\n\n\n# --- STRFs and mutual information --------------------------------------------------------------\n\ndef segment_index(times_ms: np.ndarray, bin_ms: float, n_bins: int, lags: int) -> np.ndarray:\n    \"\"\"Stimulus bin indices of the last bin before each time, kept when a full window precedes it.\"\"\"\n    idx = np.floor(times_ms / bin_ms).astype(int) - 1\n    return idx[(idx >= lags - 1) & (idx < n_bins)]\n\n\ndef sta(stim: np.ndarray, idx: np.ndarray, lags: int) -> np.ndarray:\n    \"\"\"Spike- or event-triggered average (carriers by lags, last lag nearest the event).\"\"\"\n    if len(idx) == 0:\n        return np.zeros((stim.shape[0], lags), dtype=np.float32)\n    out = np.zeros((stim.shape[0], lags), dtype=np.float64)\n    for j in range(lags):\n        out[:, j] = stim[:, idx - (lags - 1 - j)].sum(axis=1)\n    return (out / len(idx)).astype(np.float32)\n\n\ndef projections(stim_fft: np.ndarray, strf: np.ndarray, n_bins: int) -> np.ndarray:\n    \"\"\"z(t) = s(t) . STRF for every stimulus segment ending at bin t (valid for t >= lags - 1).\"\"\"\n    nf, lags = strf.shape\n    nfft = (stim_fft.shape[1] - 1) * 2\n    k = np.zeros((nf, nfft), dtype=np.float32)\n    k[:, :lags] = strf[:, ::-1]\n    full = np.fft.irfft((stim_fft * np.fft.rfft(k, axis=1)).sum(axis=0), n=nfft)\n    return full[:n_bins]\n\n\ndef stim_fft(stim: np.ndarray) -> np.ndarray:\n    nfft = 1 << int(np.ceil(np.log2(stim.shape[1] + 64)))\n    return np.fft.rfft(stim, n=nfft, axis=1).astype(np.complex64)\n\n\ndef mi_bits(x_all: np.ndarray, x_ev: np.ndarray) -> float:\n    p = np.histogram(np.clip(x_all, MI_BINS[0], MI_BINS[-1]), MI_BINS)[0].astype(float)\n    q = np.histogram(np.clip(x_ev, MI_BINS[0], MI_BINS[-1]), MI_BINS)[0].astype(float)\n    p /= p.sum()\n    q /= q.sum()\n    ok = (q > 0) & (p > 0)\n    return float((q[ok] * np.log2(q[ok] / p[ok])).sum())\n\n\ndef strf_mi(z_all: np.ndarray, z_ev: np.ndarray, rng: np.random.Generator) -> float:\n    \"\"\"MI between STRF projections and events, extrapolated to infinite data (Materials and methods).\"\"\"\n    mu, sd = z_all.mean(), z_all.std()\n    x_all, x_ev = (z_all - mu) / sd, (z_ev - mu) / sd\n    means = []\n    for f in MI_FRACTIONS:\n        m = max(int(round(f * len(x_ev))), 1)\n        vals = [mi_bits(x_all, x_ev if f == 1.0 else rng.choice(x_ev, m, replace=False))\n                for _ in range(MI_ITER if f < 1.0 else 1)]\n        means.append(np.mean(vals))\n    slope, intercept = np.polyfit(1.0 / np.array(MI_FRACTIONS), means, 1)\n    return float(intercept)\n\n\n# --- dichotomized Gaussian ---------------------------------------------------------------------\n\n_GL_X, _GL_W = np.polynomial.legendre.leggauss(40)\n\n\ndef bvn_cdf(h: np.ndarray, k: np.ndarray, r: np.ndarray) -> np.ndarray:\n    \"\"\"P(X < h, Y < k) for standard bivariate normals with correlation r (|r| < 1), by Gauss-Legendre\n    quadrature of Plackett's identity d/dr Phi2 = phi2(h, k; r).\"\"\"\n    h, k, r = np.broadcast_arrays(np.asarray(h, float), np.asarray(k, float), np.asarray(r, float))\n    s = 0.5 * r[..., None] * (_GL_X + 1.0)\n    dens = np.exp(-(h[..., None] ** 2 - 2 * h[..., None] * k[..., None] * s + k[..., None] ** 2)\n                  / (2 * (1 - s ** 2))) / (2 * np.pi * np.sqrt(1 - s ** 2))\n    return stats.norm.cdf(h) * stats.norm.cdf(k) + 0.5 * r * (dens * _GL_W).sum(axis=-1)\n\n\ndef fit_dg(binary: np.ndarray) -> tuple[np.ndarray, np.ndarray]:\n    \"\"\"Dichotomized Gaussian fit to binary trains (units by bins): thresholds gamma and latent\n    correlation matrix, matching each unit's mean and each pair's covariance (Macke et al. 2009, as\n    findLatentGaussian01 of CorBinian does), by bisection on each pair's latent correlation. The\n    latent matrix is made positive definite by clipping its eigenvalues at 1e-4 and rescaling to a\n    unit diagonal, as the fit may not be.\"\"\"\n    p = binary.mean(axis=1).clip(1e-6, 1 - 1e-6)\n    gamma = stats.norm.ppf(p)\n    joint = (binary @ binary.T) / binary.shape[1]\n    n = len(p)\n    iu = np.triu_indices(n, 1)\n    target = joint[iu]\n    lo, hi = np.full(len(target), -0.999), np.full(len(target), 0.999)\n    for _ in range(40):\n        mid = (lo + hi) / 2\n        val = bvn_cdf(gamma[iu[0]], gamma[iu[1]], mid)\n        up = val < target\n        lo = np.where(up, mid, lo)\n        hi = np.where(up, hi, mid)\n    lam = np.eye(n)\n    lam[iu] = (lo + hi) / 2\n    lam[(iu[1], iu[0])] = (lo + hi) / 2\n    vals, vecs = np.linalg.eigh(lam)\n    lam = (vecs * np.maximum(vals, 1e-4)) @ vecs.T\n    d = np.sqrt(np.diag(lam))\n    return gamma, lam / np.outer(d, d)\n\n\ndef sample_dg(gamma: np.ndarray, lam: np.ndarray, n_bins: int, rng: np.random.Generator) -> np.ndarray:\n    chol = np.linalg.cholesky(lam)\n    x = (rng.standard_normal((n_bins, len(gamma)), dtype=np.float32) @ chol.T.astype(np.float32))\n    return (x > -gamma[None, :].astype(np.float32)).T.astype(np.float32)\n"
}
```

```
File created successfully at: entries/see-2018/cne.py (file state is current in your context — no need to Read it back)
```

**Agent**

Quick timing test of detection on the 38-unit site.

**Agent calls Bash**

```bash
cd entries/see-2018 && . $TMPDIR/env/bin/activate && python -c "
import time,resource,numpy as np,cne
t=time.time(); sites=cne.load_sites(); print('load',time.time()-t)
for s in sites: cne.prepare(s)
print([(s['site'],len(s['units'])) for s in sites])
s=[x for x in sites if len(x['units'])==38]; print([x['site'] for x in s]); s=s[0]
c=cne.binned(s,10); print(c.shape, c.sum(1)[:5])
t=time.time(); d=cne.detect(c,seed=1); print('detect',time.time()-t,'N',d['n'],'bound',d['bound'],d['eigenvalues'][:12])
for r in 'ab':
  print(r,d['thresholds'][r],[ (len(m['pos']),len(m['neg'])) for m in d['members'][r]])
print({p:v for p,v in d['act_threshold'].items()})
print('maxrss MB',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024)
"
```

```
/tmp/claude-1001/env/lib/python3.13/site-packages/sklearn/decomposition/_fastica.py:132: ConvergenceWarning: FastICA did not converge. Consider increasing tolerance or the maximum number of iterations.
  warnings.warn(
load 1.033322811126709
[(1, 31), (2, 53), (3, 37), (4, 61), (5, 16), (6, 25), (7, 43), (8, 61), (9, 41), (10, 38), (11, 42), (12, 45), (13, 40), (14, 44), (15, 29), (16, 49)]
[10]
(38, 59996) [ 708. 8843.  331.  566.  859.]
detect 47.64652967453003 N 9 bound 1.0509672829517196 [2.376296  1.4961538 1.2106696 1.1398108 1.1160066 1.1010299 1.0925652
 1.068628  1.0565784 1.0508611 1.029589  1.0256015]
a (np.float32(-0.22828545), np.float32(0.25653103)) [(3, 2), (5, 0), (2, 0), (5, 2), (4, 0), (4, 0), (3, 0), (3, 0), (5, 0)]
b (np.float32(-0.24346744), np.float32(0.24319662)) [(2, 3), (0, 5), (0, 2), (5, 0), (5, 0), (0, 4), (0, 3), (0, 3), (5, 0)]
{'quadratic': array([10.8636055, 16.633804 ,  6.913759 , 12.525021 , 12.214594 ,
       13.353638 , 13.895765 , 16.295374 , 13.122597 ], dtype=float32), 'linear': array([ 8.692194 ,  7.090989 , 13.794824 ,  7.399017 ,  4.5831623,
        6.077045 ,  7.9101324,  6.583518 ,  7.304801 ], dtype=float32)}
maxrss MB 1107.8671875
```

**Agent calls Bash**

```bash
python - <<'EOF'
import re
p='cne.py'; s=open(p).read()
s=s.replace('''def _ica_weights(z: np.ndarray, vecs: np.ndarray, seed: int) -> np.ndarray:
    """fastICA on the projection of z onto the PCs `vecs` (n by N); IC weights (n by N), unit length."""''','''def _ica_weights(z: np.ndarray, vecs: np.ndarray, seed: int, max_iter: int = 1000,
                 tol: float = 1e-6) -> np.ndarray:
    """fastICA on the projection of z onto the PCs `vecs` (n by N); IC weights (n by N), unit length."""''')
s=s.replace('''max_iter=1000, tol=1e-6, random_state=seed)''','''max_iter=max_iter, tol=tol, random_state=seed)''')
s=s.replace('''shuf_w.append(_ica_weights(zs, sv[:, :k], seed + 1 + i))''','''shuf_w.append(_ica_weights(zs, sv[:, :k], seed + 1 + i, SHUFFLE_ICA_ITER, 1e-4))''')
s=s.replace('''MEMBER_SD = 1.5           # Materials and methods''','''MEMBER_SD = 1.5           # Materials and methods
SHUFFLE_ICA_ITER = 200    # standard choice (sklearn's default); fastICA does not converge on shuffles''')
s=s.replace('''  The fastICA settings (logcosh contrast, unit-variance whitening, at most 1000 iterations,
  tolerance 1e-6) and the random seeds are standard choices that the paper does not fix.''','''  The fastICA settings (logcosh contrast, unit-variance whitening, at most 1000 iterations,
  tolerance 1e-6 on the data; sklearn's defaults of 200 iterations and 1e-4 on the shuffles, which
  have no independent sources, so that fastICA does not converge on them under any setting) and
  the random seeds are standard choices that the paper does not fix.''')
open(p,'w').write(s)
EOF
. $TMPDIR/env/bin/activate && python -W ignore -c "
import time,numpy as np,cne
sites=cne.load_sites()
for s in sites: cne.prepare(s)
s=sites[9]; c=cne.binned(s,10)
t=time.time(); d=cne.detect(c,seed=1); print('detect',time.time()-t,'N',d['n'])
for r in 'ab': print(r,d['thresholds'][r],[ (len(m['pos']),len(m['neg'])) for m in d['members'][r]])
t=time.time(); d=cne.detect(c,seed=2,activity_null=False); print('detect no act',time.time()-t,'N',d['n'], [ (len(m['pos']),len(m['neg'])) for m in d['members']['a']])
s=sites[3]; c=cne.binned(s,10); t=time.time(); d=cne.detect(c,seed=1); print('61 units detect',time.time()-t,'N',d['n'])
"
```

```
detect 29.068050384521484 N 9
a (np.float32(-0.22779796), np.float32(0.25690398)) [(3, 2), (5, 0), (2, 0), (5, 2), (4, 0), (4, 0), (3, 0), (3, 0), (5, 0)]
b (np.float32(-0.24324062), np.float32(0.24342358)) [(2, 3), (0, 5), (0, 2), (5, 0), (5, 0), (0, 4), (0, 3), (0, 3), (5, 0)]
detect no act 26.74237298965454 N 9 [(3, 2), (3, 0), (5, 1), (4, 0), (3, 0), (5, 0), (5, 0), (4, 0), (2, 0)]
61 units detect 29.524415493011475 N 9
```

**Agent**

Detection still costs about 27 s per site, mostly fastICA on the 100 shuffles. Checking whether fewer shuffle iterations change the membership thresholds.

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python -W ignore -c "
import time,numpy as np,cne
sites=cne.load_sites()
for s in sites: cne.prepare(s)
for si in [9,3]:
  s=sites[si]; c=cne.binned(s,10)
  for it in [200,25,5]:
    cne.SHUFFLE_ICA_ITER=it
    t=time.time(); d=cne.detect(c,seed=1,activity_null=False); 
    print(s['site'],it,'%.1fs'%(time.time()-t),'N',d['n'],{r:np.round(d['thresholds'][r],4) for r in 'ab'}, [len(m) for m in cne.member_sets(d,'a')])
"
```

```
10 200 26.6s N 9 {'a': array([-0.2278,  0.2569], dtype=float32), 'b': array([-0.2432,  0.2434], dtype=float32)} [5, 5, 2, 7, 4, 4, 3, 3, 5]
10 25 24.1s N 9 {'a': array([-0.2279,  0.2568], dtype=float32), 'b': array([-0.2432,  0.2435], dtype=float32)} [5, 5, 2, 7, 4, 4, 3, 3, 5]
10 5 18.6s N 9 {'a': array([-0.2301,  0.2551], dtype=float32), 'b': array([-0.2441,  0.2425], dtype=float32)} [5, 5, 2, 6, 4, 4, 3, 3, 5]
4 200 28.8s N 9 {'a': array([-0.1856,  0.198 ], dtype=float32), 'b': array([-0.1922,  0.1919], dtype=float32)} [7, 4, 4, 6, 5, 7, 6, 7, 6]
4 25 25.5s N 9 {'a': array([-0.1855,  0.1981], dtype=float32), 'b': array([-0.1928,  0.1913], dtype=float32)} [7, 4, 4, 6, 5, 7, 6, 7, 6]
4 5 19.8s N 9 {'a': array([-0.1855,  0.1982], dtype=float32), 'b': array([-0.1917,  0.1924], dtype=float32)} [7, 4, 4, 6, 5, 7, 6, 7, 6]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python -W ignore -c "
import cProfile,pstats,numpy as np,cne
sites=cne.load_sites()
s=sites[9]; cne.prepare(s); c=cne.binned(s,10)
cProfile.run('cne.detect(c,seed=1,n_shuffles=20,activity_null=False)','/tmp/claude-1001/prof')
pstats.Stats('/tmp/claude-1001/prof').sort_stats('cumtime').print_stats(18)
" 2>&1 | tail -30
```

```
Fri Nov 13 04:01:44 2026    /tmp/claude-1001/prof

         157118 function calls (157066 primitive calls) in 5.729 seconds

   Ordered by: cumulative time
   List reduced from 403 to 18 due to restriction <18>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    5.729    5.729 {built-in method builtins.exec}
        1    0.002    0.002    5.728    5.728 <string>:1(<module>)
        1    0.009    0.009    5.727    5.727 entries/see-2018/cne.py:238(detect)
       21    0.012    0.001    5.217    0.248 entries/see-2018/cne.py:184(_ica_weights)
       21    0.001    0.000    5.204    0.248 /tmp/claude-1001/env/lib/python3.13/site-packages/sklearn/base.py:1381(wrapper)
       21    0.000    0.000    5.193    0.247 /tmp/claude-1001/env/lib/python3.13/site-packages/sklearn/decomposition/_fastica.py:726(fit)
       21    0.120    0.006    5.193    0.247 /tmp/claude-1001/env/lib/python3.13/site-packages/sklearn/decomposition/_fastica.py:553(_fit_transform)
       21    2.013    0.096    3.437    0.164 /tmp/claude-1001/env/lib/python3.13/site-packages/sklearn/decomposition/_fastica.py:111(_ica_par)
       42    0.001    0.000    1.582    0.038 /tmp/claude-1001/env/lib/python3.13/site-packages/scipy/linalg/_decomp_svd.py:37(svd)
       42    1.580    0.038    1.580    0.038 {built-in method scipy.linalg._batched_linalg._svd}
      742    1.054    0.001    1.268    0.002 /tmp/claude-1001/env/lib/python3.13/site-packages/sklearn/decomposition/_fastica.py:143(_logcosh)
       20    0.192    0.010    0.426    0.021 entries/see-2018/cne.py:222(circular_shuffle)
[... 6 more lines not kept]
```

**Agent**

sklearn's FastICA spends most of its time re-whitening via SVD. I'll use a direct symmetric fastICA (logcosh) on the PC projections, which are already decorrelated, and run sites in parallel.

**Agent calls Bash**

```bash
python - <<'EOF'
p='cne.py'; s=open(p).read()
old_start=s.index('def _ica_weights(')
old_end=s.index('def orient(')
new='''def fastica(x: np.ndarray, seed: int, max_iter: int, tol: float) -> np.ndarray:
    """Symmetric fastICA with the logcosh contrast (Hyvarinen and Oja 1997; the algorithm of
    sklearn's FastICA) on whitened data x (N by T). Returns the unmixing matrix W (N by N)."""
    rng = np.random.default_rng(seed)
    n, t = x.shape
    w = _sym_decorrelate(rng.standard_normal((n, n)))
    for _ in range(max_iter):
        g = np.tanh(w.astype(np.float32) @ x)
        w1 = (g @ x.T) / t - (1.0 - g ** 2).mean(axis=1)[:, None] * w
        w1 = _sym_decorrelate(w1.astype(np.float64))
        lim = np.max(np.abs(np.abs(np.einsum("ij,ij->i", w1, w)) - 1.0))
        w = w1
        if lim < tol:
            break
    return w


def _sym_decorrelate(w: np.ndarray) -> np.ndarray:
    s, u = np.linalg.eigh(w @ w.T)
    s = np.clip(s, np.finfo(w.dtype).tiny, None)
    return (u * (1.0 / np.sqrt(s))) @ u.T @ w


def _ica_weights(z: np.ndarray, vals: np.ndarray, vecs: np.ndarray, seed: int,
                 max_iter: int = 1000, tol: float = 1e-6) -> np.ndarray:
    """fastICA on the projection of z onto the PCs `vecs` (n by N) with eigenvalues `vals`, which
    are already uncorrelated, so whitening divides each by the square root of its eigenvalue.
    Returns the IC weights in unit space (n by N), each of unit length."""
    if vecs.shape[1] == 1:
        return vecs / np.linalg.norm(vecs, axis=0, keepdims=True)
    scale = 1.0 / np.sqrt(vals)
    x = (vecs.T.astype(np.float32) @ z) * scale[:, None].astype(np.float32)
    w = fastica(x, seed, max_iter, tol)
    weights = vecs @ (w * scale[None, :]).T
    return weights / np.linalg.norm(weights, axis=0, keepdims=True)


'''
s=s[:old_start]+new+s[old_end:]
s=s.replace("w = _ica_weights(z, vecs[:, :k], seed)","w = _ica_weights(z, vals[:k], vecs[:, :k], seed)")
s=s.replace("""        _, sv = pcs(zs)
        shuf_w.append(_ica_weights(zs, sv[:, :k], seed + 1 + i, SHUFFLE_ICA_ITER, 1e-4))""","""        sl, sv = pcs(zs)
        shuf_w.append(_ica_weights(zs, sl[:k], sv[:, :k], seed + 1 + i, SHUFFLE_ICA_ITER, 1e-4))""")
s=s.replace("from sklearn.decomposition import FastICA\n","")
s=s.replace("""  The fastICA settings (logcosh contrast, unit-variance whitening, at most 1000 iterations,
  tolerance 1e-6 on the data; sklearn's defaults of 200 iterations and 1e-4 on the shuffles, which
  have no independent sources, so that fastICA does not converge on them under any setting) and
  the random seeds are standard choices that the paper does not fix.""","""  fastICA is the symmetric algorithm with the logcosh contrast (`fastica`, as in sklearn and the
  FastICA package). Its settings (at most 1000 iterations and tolerance 1e-6 on the data; at most
  200 iterations and tolerance 1e-4, sklearn's defaults, on the shuffles, which hold no
  independent sources) and the random seeds are standard choices that the paper does not fix.""")
open(p,'w').write(s)
EOF
grep -n "FastICA\|_ica_weights" cne.py; . $TMPDIR/env/bin/activate && python -W ignore -c "
import time,numpy as np,cne
sites=cne.load_sites()
for si in [9,3]:
  s=sites[si]; cne.prepare(s); c=cne.binned(s,10)
  t=time.time(); d=cne.detect(c,seed=1); 
  print(s['site'],'%.1fs'%(time.time()-t),'N',d['n'],{r:np.round(d['thresholds'][r],4) for r in 'ab'}, [len(m) for m in cne.member_sets(d,'a')],[len(m) for m in cne.member_sets(d,'b')])
"
```

```
24:  FastICA package). Its settings (at most 1000 iterations and tolerance 1e-6 on the data; at most
185:    sklearn's FastICA) on whitened data x (N by T). Returns the unmixing matrix W (N by N)."""
206:def _ica_weights(z: np.ndarray, vals: np.ndarray, vecs: np.ndarray, seed: int,
279:    w = _ica_weights(z, vals[:k], vecs[:, :k], seed)
289:        shuf_w.append(_ica_weights(zs, sl[:k], sv[:, :k], seed + 1 + i, SHUFFLE_ICA_ITER, 1e-4))
10 12.7s N 9 {'a': array([-0.228 ,  0.2567]), 'b': array([-0.2432,  0.2435])} [3, 4, 2, 5, 3, 4, 5, 7, 5] [3, 4, 2, 5, 3, 4, 5, 5, 5]
4 15.8s N 9 {'a': array([-0.1849,  0.1986]), 'b': array([-0.1913,  0.1928])} [6, 5, 7, 4, 4, 6, 7, 7, 6] [6, 6, 7, 4, 4, 7, 7, 8, 6]
```

**Agent calls Bash**

```bash
cat >> cne.py <<'EOF'


# --- per-recording analyses, run in worker processes ------------------------------------------
# The notebook sets SITES (and STIM, the 5-ms and 1-ms stimuli by name) before forking workers.

SITES: list[dict] = []
STIM: dict = {}
BIN_SIZES = (2, 5, 8, 10, 15, 20, 35, 50)   # Materials and methods, STRF mutual information
N_EVENTS_5A = 5000                          # Materials and methods
PR_BINS = 15                                # Materials and methods, Simulated spike trains


def run_main(i: int, seed: int) -> dict:
    """cNE detection at 10 ms with membership and activity thresholds."""
    det = detect(binned(SITES[i], BIN_MS), seed)
    det.pop("eigenvalues")
    return det


def run_halves(i: int, seed: int) -> dict:
    """Detection on two interleaved halves (10 equal parts; odd parts A, even parts B)."""
    c = binned(SITES[i], BIN_MS)
    parts = np.array_split(np.arange(c.shape[1]), 10)
    a = np.concatenate(parts[0::2])
    b = np.concatenate(parts[1::2])
    out = {}
    for name, idx in (("A", a), ("B", b)):
        d = detect(c[:, idx], seed + (0 if name == "A" else 5000), activity_null=False)
        out[name] = {"w": d["w"], "shuffled_w": d.get("shuffled_w", []), "kept": d["kept"], "n": d["n"]}
    return out


def run_traintest(i: int, seed: int) -> dict:
    """Detection on the first (training) and second (test) halves; both IC sets projected onto the
    z-scored test half; correlations of training with test activities, per projection reading."""
    c = binned(SITES[i], BIN_MS)
    half = c.shape[1] // 2
    tr, te = c[:, :half], c[:, half:]
    keep = np.flatnonzero((tr.std(axis=1) > 0) & (te.std(axis=1) > 0))
    dtr = detect(tr[keep], seed, null=False)
    dte = detect(te[keep], seed + 1, null=False)
    zte = zscore(te[keep])
    out = {"n_train": dtr["n"], "n_test": dte["n"]}
    for p in PROJECTIONS:
        if dtr["n"] == 0 or dte["n"] == 0:
            out[p] = np.zeros((dtr["n"], dte["n"]))
            continue
        a = activity(zte, orient(dtr["w"], "a"), p)
        b = activity(zte, orient(dte["w"], "a"), p)
        out[p] = np.corrcoef(a, b)[:dtr["n"], dtr["n"]:]
    return out


def unit_strfs(site: dict, stim: np.ndarray, bin_ms: float, lags: int) -> list[np.ndarray]:
    return [sta(stim, segment_index(u["stim_ms"][np.isfinite(u["stim_ms"])], bin_ms, stim.shape[1], lags), lags)
            for u in site["units"]]


def run_binsizes(i: int, seed: int) -> dict:
    """Detection at each bin size (number, sizes) and, per cNE, the STRF MI of Figure 5A: activity
    interpolated to 1 ms, the 5000 largest samples (event reading a) or the 5000 largest local
    peaks (event reading b) as events, STRF by event-triggered average."""
    site = SITES[i]
    stim = STIM[(site["stim"], STRF_BIN_MS)]
    sfft = stim_fft(stim)
    rng = np.random.default_rng(seed)
    n_ms = int(stim_duration_ms(site))
    out = {}
    for b in BIN_SIZES:
        c = binned(site, b)
        d = detect(c, seed + b, activity_null=False)
        res = {"n": d["n"], "sizes_a": [len(m) for m in member_sets(d, "a")] if d["n"] else [],
               "sizes_b": [len(m) for m in member_sets(d, "b")] if d["n"] else [], "mi": {}}
        if d["n"]:
            z = zscore(c[d["kept"]])
            w = orient(d["w"], "a")
            for p in PROJECTIONS:
                act = activity(z, w, p)
                for er in ("a", "b"):
                    mis = []
                    for j in range(d["n"]):
                        a1 = interp_activity(act[j], b, n_ms)
                        if er == "a":
                            ev = np.argsort(a1)[-N_EVENTS_5A:]
                        else:
                            peaks = np.flatnonzero((a1[1:-1] > a1[:-2]) & (a1[1:-1] >= a1[2:])) + 1
                            ev = peaks[np.argsort(a1[peaks])[-N_EVENTS_5A:]]
                        idx = segment_index(ev + 0.5, STRF_BIN_MS, stim.shape[1], STRF_LAGS)
                        strf = sta(stim, idx, STRF_LAGS)
                        zall = projections(sfft, strf, stim.shape[1])
                        mis.append(strf_mi(zall[STRF_LAGS - 1:], zall[idx], rng))
                    res["mi"][(p, er)] = mis
        out[b] = res
    return out


def pair_table(i: int, det: dict, reading: str = "a") -> list[dict]:
    """All unit pairs of a recording with PWC measures (both lag readings), correlation coefficient
    at 10 ms, distances, and whether they share a cNE."""
    site = SITES[i]
    units = site["units"]
    c = binned(site, BIN_MS)
    r = np.corrcoef(c)
    sets = member_sets(det, reading) if det["n"] else []
    rows = []
    for a in range(len(units)):
        ta = units[a]["spikes_ms"]
        for b in range(a + 1, len(units)):
            tb = units[b]["spikes_ms"]
            h = pwc(ta, tb, 100.0)
            s100, d100 = pwc_measures(h)
            s50, d50 = pwc_measures(h[50:151])
            shared = sum(1 for m in sets if a in m and b in m)
            in_any = (any(a in m for m in sets), any(b in m for m in sets))
            rows.append({"site": site["site"], "a": a, "b": b, "r": r[a, b],
                         "sharp_50": s50, "delay_50": d50, "sharp_100": s100, "delay_100": d100,
                         "count_50": int(h[50:151].sum()),
                         "depth_diff": abs(units[a]["depth"] - units[b]["depth"]),
                         "euclid": float(np.hypot(units[a]["x"] - units[b]["x"],
                                                  units[a]["depth"] - units[b]["depth"])),
                         "n_shared": shared, "both_members": all(in_any)})
    return rows


def run_pairs(i: int, det: dict) -> list[dict]:
    return pair_table(i, det)


def run_strf_profiles(i: int) -> list[np.ndarray]:
    """1-ms STRFs (50 lags), for the temporal profiles of Figure 6B, E."""
    site = SITES[i]
    stim = STIM[(site["stim"], 1)]
    return unit_strfs(site, stim, 1, 50)


def cne_events_10ms(det: dict, z: np.ndarray, projection: str, reading: str) -> list[np.ndarray]:
    """Event times (ms, stimulus clock, the centre of the 10-ms bin) of each cNE: activity above the
    99.9th percentile threshold; reading (a) every bin, (b) the peak bin of each run."""
    act = activity(z, orient(det["w"], "a"), projection)
    thr = det["act_threshold"][projection]
    return [(events_from_activity(act[j], thr[j], reading) + 0.5) * BIN_MS for j in range(det["n"])]


def _strf_measures(times: np.ndarray, stim: np.ndarray, sfft: np.ndarray, rng) -> tuple[float, float, int]:
    idx = segment_index(times, STRF_BIN_MS, stim.shape[1], STRF_LAGS)
    strf = sta(stim, idx, STRF_LAGS)
    zall = projections(sfft, strf, stim.shape[1])
    return float(strf.max() - strf.min()), strf_mi(zall[STRF_LAGS - 1:], zall[idx], rng), len(idx)


def run_cne_vs_members(i: int, det: dict, seed: int) -> list[dict]:
    """Figure 10B, C: STRF PTD and MI of each cNE and each of its members, after subsampling the
    larger of the event and spike trains to equal counts."""
    site = SITES[i]
    stim = STIM[(site["stim"], STRF_BIN_MS)]
    sfft = stim_fft(stim)
    rng = np.random.default_rng(seed)
    if det["n"] == 0:
        return []
    z = zscore(binned(site, BIN_MS)[det["kept"]])
    rows = []
    sets = member_sets(det, "a")
    for p in PROJECTIONS:
        for er in ("a", "b"):
            evs = cne_events_10ms(det, z, p, er)
            for j, members in enumerate(sets):
                for m in members:
                    sp = site["units"][m]["stim_ms"]
                    sp = sp[np.isfinite(sp)]
                    ev = evs[j]
                    k = min(len(sp), len(ev))
                    if k < 2:
                        continue
                    ev_s = np.sort(rng.choice(ev, k, replace=False))
                    sp_s = np.sort(rng.choice(sp, k, replace=False))
                    ptd_c, mi_c, _ = _strf_measures(ev_s, stim, sfft, rng)
                    ptd_n, mi_n, _ = _strf_measures(sp_s, stim, sfft, rng)
                    rows.append({"site": site["site"], "cne": j, "unit": m, "projection": p,
                                 "events": er, "count": k, "ptd_cne": ptd_c / 1.0, "ptd_unit": ptd_n,
                                 "mi_cne": mi_c, "mi_unit": mi_n})
    return rows


def random_groups(members: np.ndarray, others: list[np.ndarray], n_units: int, n_groups: int,
                  rng: np.random.Generator, max_draws: int = 20000) -> tuple[list[tuple], int]:
    """Random groups of the cNE's size (Materials and methods, MI comparisons): `level` members of the
    cNE and the rest from non-members, with at most `level` units from any other cNE; the level is
    raised until `n_groups` unique groups are found within `max_draws` draws (a standard choice)."""
    size = len(members)
    non = np.setdiff1d(np.arange(n_units), members)
    for level in range(1, size + 1):
        if size - level > len(non):
            continue
        found = set()
        for _ in range(max_draws):
            g = tuple(sorted(np.r_[rng.choice(members, level, replace=False),
                                   rng.choice(non, size - level, replace=False)].tolist()))
            if g == tuple(sorted(members.tolist())):
                continue
            if any(len(np.intersect1d(g, o)) > level for o in others):
                continue
            found.add(g)
            if len(found) >= n_groups:
                return sorted(found), level
    return sorted(found), level


def run_random_groups(i: int, det: dict, seed: int, n_groups: int = 500) -> list[dict]:
    """Figure 10-figure supplement 1: PTD and STRF MI of the summed spikes of each cNE's members and
    of random groups, all subsampled to the fewest spikes; sets under 200 spikes left out."""
    site = SITES[i]
    stim = STIM[(site["stim"], STRF_BIN_MS)]
    sfft = stim_fft(stim)
    rng = np.random.default_rng(seed)
    if det["n"] == 0:
        return []
    sets = member_sets(det, "a")
    spikes = [u["stim_ms"][np.isfinite(u["stim_ms"])] for u in site["units"]]
    rows = []
    for j, members in enumerate(sets):
        if len(members) < 2:
            continue
        others = [s for k, s in enumerate(sets) if k != j]
        groups, level = random_groups(members, others, len(spikes), n_groups, rng)
        trains = [np.concatenate([spikes[m] for m in members])] + \
                 [np.concatenate([spikes[m] for m in g]) for g in groups]
        k = min(len(t) for t in trains)
        if k < 200:
            rows.append({"site": site["site"], "cne": j, "size": len(members), "n_groups": len(groups),
                         "level": level, "count": k, "excluded": True})
            continue
        ptd, mi = [], []
        for t in trains:
            p_, m_, _ = _strf_measures(np.sort(rng.choice(t, k, replace=False)), stim, sfft, rng)
            ptd.append(p_)
            mi.append(m_)
        ptd, mi = np.array(ptd), np.array(mi)
        rows.append({"site": site["site"], "cne": j, "size": len(members), "n_groups": len(groups),
                     "level": level, "count": k, "excluded": False,
                     "ptd_cne": ptd[0], "ptd_rand_median": float(np.median(ptd[1:])),
                     "ui_ptd": float((ptd >= ptd[0]).mean()),
                     "mi_cne": mi[0], "mi_rand_median": float(np.median(mi[1:])),
                     "ui_mi": float((mi >= mi[0]).mean())})
    return rows


# --- models (Figure 11C, D and its supplement 3) ---------------------------------------------

def pr_setup(site: dict, model_bin: float) -> list[dict]:
    """Per unit, for the PR model on bins of `model_bin` ms: the STRF projection class (one of 15
    equal bins over the full range of projection values) of the stimulus segment before each bin,
    and the unit's spike count in each class. Units without spikes in the stimulus get no model."""
    stim = STIM[(site["stim"], STRF_BIN_MS)]
    sfft = stim_fft(stim)
    n_bins = int(stim_duration_ms(site) // BIN_MS) * int(BIN_MS // model_bin)
    starts = np.arange(n_bins) * model_bin
    seg = np.floor(starts / STRF_BIN_MS).astype(int) - 1     # last stimulus bin before the model bin
    ok = seg >= STRF_LAGS - 1
    out = []
    for u in site["units"]:
        t = u["stim_ms"][np.isfinite(u["stim_ms"])]
        strf = sta(stim, segment_index(t, STRF_BIN_MS, stim.shape[1], STRF_LAGS), STRF_LAGS)
        z = projections(sfft, strf, stim.shape[1])[np.clip(seg, 0, None)]
        z[~ok] = np.nan
        edges = np.linspace(np.nanmin(z), np.nanmax(z), PR_BINS + 1)
        cls = np.clip(np.digitize(z, edges[1:-1]), 0, PR_BINS - 1)
        cls[~ok] = -1
        counts = np.histogram(t, np.r_[starts, starts[-1] + model_bin])[0]
        members = [np.flatnonzero(cls == k) for k in range(PR_BINS)]
        spikes = [int(counts[m].sum()) for m in members]
        out.append({"members": members, "spikes": spikes, "n_bins": n_bins,
                    "strf": strf, "dropped": int(counts[~ok].sum())})
    return out


def pr_sample(setup: list[dict], rng: np.random.Generator, units=None) -> np.ndarray:
    """PR trains: each spike assigned to a random time bin of its projection class."""
    units = range(len(setup)) if units is None else units
    out = np.zeros((len(units), setup[0]["n_bins"]), dtype=np.float32)
    for r, u in enumerate(units):
        s = setup[u]
        for m, k in zip(s["members"], s["spikes"]):
            if k and len(m):
                np.add.at(out[r], m[rng.integers(0, len(m), k)], 1)
    return out


def rebin(c: np.ndarray, k: int) -> np.ndarray:
    n = c.shape[1] // k
    return c[:, :n * k].reshape(c.shape[0], n, k).sum(axis=2)


def model_trains(name: str, ctx: dict, rng: np.random.Generator) -> np.ndarray:
    """One model matrix at 10 ms: 'shuffled', 'pr10', 'pr5' or 'dg'."""
    if name == "shuffled":
        return circular_shuffle(ctx["real"], rng)
    if name == "pr10":
        return pr_sample(ctx["pr10"], rng)
    if name == "pr5":
        return rebin(pr_sample(ctx["pr5"], rng), 2)
    if name == "dg":
        return rebin(sample_dg(ctx["gamma"], ctx["lam"], ctx["n5"], rng), 2)
    raise ValueError(name)


MODELS = ("shuffled", "pr10", "pr5", "dg")


def model_context(site: dict) -> dict:
    real = binned(site, BIN_MS)
    b5 = np.minimum(binned(site, 5), 1)
    gamma, lam = fit_dg(b5)
    return {"real": real, "pr10": pr_setup(site, 10), "pr5": pr_setup(site, 5),
            "gamma": gamma, "lam": lam, "n5": b5.shape[1]}


def run_models(i: int, det: dict, seed: int, n_iter: int) -> dict:
    """Number and mean size of cNEs in `n_iter` runs of each model. Membership uses the recording's
    own thresholds (sign reading a) from the shuffles of the real data."""
    site = SITES[i]
    ctx = model_context(site)
    lo, hi = det["thresholds"]["a"]
    out = {}
    for mi_, name in enumerate(MODELS):
        rng = np.random.default_rng(seed + 1000 * mi_)
        ns, sizes = [], []
        for it in range(n_iter):
            c = model_trains(name, ctx, rng)
            keep = np.flatnonzero(c.std(axis=1) > 0)
            z = zscore(c[keep])
            vals, vecs = pcs(z)
            k = int((vals > mp_bound(*z.shape)).sum())
            ns.append(k)
            if k:
                w = orient(_ica_weights(z, vals[:k], vecs[:, :k], seed + it), "a")
                sizes.append(float(np.mean(((w > hi) | (w < lo)).sum(axis=0))))
            else:
                sizes.append(np.nan)
        out[name] = {"n": np.array(ns), "size": np.array(sizes)}
    return out


def run_strf_similarity(i: int, seed: int, n_iter: int) -> dict:
    """Correlation of each unit's model STRF with its real STRF, both from trains binned as the
    model is (10 ms; 5 ms for pr5), spikes placed at bin centres."""
    site = SITES[i]
    stim = STIM[(site["stim"], STRF_BIN_MS)]
    ctx = model_context(site)
    rng = np.random.default_rng(seed)
    out = {}

    def strfs(c, bin_ms):
        res = []
        for row in c:
            nz = np.flatnonzero(row)
            t = np.repeat((nz + 0.5) * bin_ms, row[nz].astype(int))
            res.append(sta(stim, segment_index(t, STRF_BIN_MS, stim.shape[1], STRF_LAGS), STRF_LAGS).ravel())
        return res

    real10 = strfs(ctx["real"], 10)
    real5 = strfs(binned(site, 5), 5)
    for name in MODELS:
        vals = []
        for it in range(n_iter):
            if name == "pr5":
                c, ref, bm = pr_sample(ctx["pr5"], rng), real5, 5
            elif name == "dg":
                c, ref, bm = sample_dg(ctx["gamma"], ctx["lam"], ctx["n5"], rng), real5, 5
            else:
                c, ref, bm = model_trains(name, ctx, rng), real10, 10
            for a, b in zip(strfs(c, bm), ref):
                if a.std() > 0 and b.std() > 0:
                    vals.append(float(np.corrcoef(a, b)[0, 1]))
        out[name] = np.array(vals)
    return out


def coincidence_ratio(binary: np.ndarray) -> float:
    """Bins where all units spike over bins where the unit with the lowest rate spikes."""
    low = binary[np.argmin(binary.sum(axis=1))]
    return float(np.all(binary, axis=0).sum() / low.sum()) if low.sum() else np.nan


def run_cr(i: int, groups: list[tuple], seed: int, n_iter: int) -> list[dict]:
    """Real and model CRs (median over `n_iter` runs) for groups of units of this recording."""
    site = SITES[i]
    ctx = model_context(site)
    rng = np.random.default_rng(seed)
    real = ctx["real"] > 0
    units = sorted({u for g in groups for u in g})
    pos = {u: k for k, u in enumerate(units)}
    sims = {m: [] for m in MODELS}
    sub_gamma = ctx["gamma"][units]
    sub_lam = ctx["lam"][np.ix_(units, units)]
    for it in range(n_iter):
        t = ctx["real"].shape[1]
        shifts = rng.integers(1, t, size=len(units))
        sims["shuffled"].append(np.stack([np.roll(real[u], s) for u, s in zip(units, shifts)]))
        sims["pr10"].append(pr_sample(ctx["pr10"], rng, units) > 0)
        sims["pr5"].append(rebin(pr_sample(ctx["pr5"], rng, units), 2) > 0)
        sims["dg"].append(rebin(sample_dg(sub_gamma, sub_lam, ctx["n5"], rng), 2) > 0)
    rows = []
    for g in groups:
        row = {"site": site["site"], "group": g, "size": len(g), "real": coincidence_ratio(real[list(g)])}
        idx = [pos[u] for u in g]
        for m in MODELS:
            row[m] = float(np.nanmedian([coincidence_ratio(s[idx]) for s in sims[m]]))
        rows.append(row)
    return rows
EOF
. $TMPDIR/env/bin/activate && python -c "import ast;ast.parse(open('cne.py').read())"
```

```
(Bash completed with no output)
```

**Agent**

Fixing `run_cr` to compute CRs per iteration instead of holding all model trains in memory.

**Agent calls Bash**

```bash
python - <<'EOF'
p='cne.py'; s=open(p).read()
a=s.index('    units = sorted({u for g in groups for u in g})')
b=s.index('    return rows\n', a)
s=s[:a]+'''    units = sorted({u for g in groups for u in g})
    pos = {u: k for k, u in enumerate(units)}
    idx = [[pos[u] for u in g] for g in groups]
    sub_gamma = ctx["gamma"][units]
    sub_lam = ctx["lam"][np.ix_(units, units)]
    t = ctx["real"].shape[1]
    crs = {m: np.full((n_iter, len(groups)), np.nan) for m in MODELS}
    for it in range(n_iter):
        shifts = rng.integers(1, t, size=len(units))
        sims = {"shuffled": np.stack([np.roll(real[u], s) for u, s in zip(units, shifts)]),
                "pr10": pr_sample(ctx["pr10"], rng, units) > 0,
                "pr5": rebin(pr_sample(ctx["pr5"], rng, units), 2) > 0,
                "dg": rebin(sample_dg(sub_gamma, sub_lam, ctx["n5"], rng), 2) > 0}
        for m in MODELS:
            crs[m][it] = [coincidence_ratio(sims[m][ix]) for ix in idx]
    rows = []
    for k, g in enumerate(groups):
        row = {"site": site["site"], "group": g, "size": len(g), "real": coincidence_ratio(real[list(g)])}
        for m in MODELS:
            row[m] = float(np.nanmedian(crs[m][:, k]))
        rows.append(row)
'''+s[b:]
open(p,'w').write(s)
EOF
cat > $TMPDIR/t1.py <<'EOF'
import time, resource, warnings, numpy as np, cne
warnings.filterwarnings("ignore")
cne.SITES = cne.load_sites()
for s in cne.SITES: cne.prepare(s)
t=time.time()
raw = cne.load_stimulus("rn16")
cne.STIM[("rn16",5)] = cne.downsample(raw,5); cne.STIM[("rn16",1)] = cne.downsample(raw,1); del raw
print("stim", time.time()-t, cne.STIM[("rn16",5)].shape)
i = 9  # site 10, rn16
T=lambda: time.time()
t=T(); det = cne.run_main(i, 1); print("main", T()-t, det["n"])
t=T(); rows = cne.run_pairs(i, det); print("pairs", T()-t, len(rows))
t=T(); h = cne.run_halves(i, 2); print("halves", T()-t, h["A"]["n"], h["B"]["n"])
t=T(); tt = cne.run_traintest(i, 3); print("traintest", T()-t, tt["n_train"], tt["n_test"], np.round(tt["quadratic"],2))
t=T(); pr = cne.run_strf_profiles(i); print("profiles", T()-t, pr[0].shape)
t=T(); cm = cne.run_cne_vs_members(i, det, 4); print("cne vs members", T()-t, len(cm))
import pandas as pd; d=pd.DataFrame(cm); print(d.groupby(["projection","events"])[["count","ptd_cne","ptd_unit","mi_cne","mi_unit"]].median())
print("maxrss MB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024)
t=T(); ctx = cne.model_context(cne.SITES[i]); print("model ctx", T()-t)
t=T(); m = cne.run_models(i, det, 5, 3); print("models 3 iters", T()-t, {k:(v['n'],v['size']) for k,v in m.items()})
print("maxrss MB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024)
EOF
. $TMPDIR/env/bin/activate && python $TMPDIR/t1.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t1.py", line 1, in <module>
    import time, resource, warnings, numpy as np, cne
ModuleNotFoundError: No module named 'cne'
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && PYTHONPATH=. python $TMPDIR/t1.py
```

```
stim 11.25021481513977 (64, 119993)
main 12.961902141571045 9
pairs 7.253767967224121 703
halves 9.637819766998291 7 7
traintest 0.1990199089050293 8 7 [[ 0.7   0.    0.03  0.   -0.02  0.29 -0.  ]
 [ 0.01 -0.01  0.67  0.02  0.01  0.03  0.02]
 [-0.02 -0.01  0.01 -0.    0.   -0.01  0.87]
 [ 0.11  0.01  0.03  0.04  0.03 -0.02  0.02]
 [-0.01 -0.06  0.01  0.71 -0.02  0.1   0.02]
 [-0.03  0.03  0.09 -0.04  0.   -0.03  0.02]
 [ 0.03  0.9  -0.   -0.    0.01 -0.   -0.  ]
 [ 0.03  0.    0.03 -0.07  0.8   0.08 -0.02]]
profiles 0.47411656379699707 (64, 50)
cne vs members 53.211451292037964 152
                   count   ptd_cne  ptd_unit    mi_cne   mi_unit
projection events                                               
linear     a       170.0  6.166426  5.664361  1.933624  1.864579
           b       169.0  6.166426  5.493799  1.858253  2.050366
quadratic  a       302.5  4.343820  4.595333  1.263259  1.102729
           b       291.0  4.419225  4.512341  1.229463  1.135339
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; python - <<'EOF'
p='cne.py'; s=open(p).read()
a=s.index('def mi_bits('); b=s.index('# --- dichotomized Gaussian')
s=s[:a]+'''def _hist(x: np.ndarray) -> np.ndarray:
    idx = np.clip(np.searchsorted(MI_BINS, x, side="right") - 1, 0, len(MI_BINS) - 2)
    h = np.bincount(idx, minlength=len(MI_BINS) - 1).astype(float)
    return h / h.sum()


def mi_bits(p: np.ndarray, x_ev: np.ndarray) -> float:
    """MI (bits) from the prior P(x) (histogram `p`) and the projections before events."""
    q = _hist(x_ev)
    ok = (q > 0) & (p > 0)
    return float((q[ok] * np.log2(q[ok] / p[ok])).sum())


def strf_mi(z_all: np.ndarray, z_ev: np.ndarray, rng: np.random.Generator) -> float:
    """MI between STRF projections and events, extrapolated to infinite data (Materials and methods).
    Projections are binned in `MI_BINS` after normalising by the mean and SD of P(z); values beyond
    the outer edges fall in the end bins."""
    mu, sd = z_all.mean(), z_all.std()
    p = _hist((z_all - mu) / sd)
    x_ev = (z_ev - mu) / sd
    means = []
    for f in MI_FRACTIONS:
        m = max(int(round(f * len(x_ev))), 1)
        vals = [mi_bits(p, x_ev if f == 1.0 else rng.choice(x_ev, m, replace=False))
                for _ in range(MI_ITER if f < 1.0 else 1)]
        means.append(np.mean(vals))
    slope, intercept = np.polyfit(1.0 / np.array(MI_FRACTIONS), means, 1)
    return float(intercept)


'''+s[b:]
open(p,'w').write(s)
EOF
cat > $TMPDIR/t2.py <<'EOF'
import time, warnings, numpy as np, cne, cProfile, pstats
warnings.filterwarnings("ignore")
cne.SITES = cne.load_sites()
for s in cne.SITES: cne.prepare(s)
raw = cne.load_stimulus("rn16"); cne.STIM[("rn16",5)] = cne.downsample(raw,5); del raw
i=9; det=cne.run_main(i,1)
t=time.time(); cm=cne.run_cne_vs_members(i, det, 4); print("cne vs members", time.time()-t)
t=time.time(); rg=cne.run_random_groups(i, det, 6, n_groups=20); print("random groups 20", time.time()-t, rg[:2])
cProfile.run('cne.run_models(i, det, 5, 3)', '/tmp/claude-1001/p2')
pstats.Stats('/tmp/claude-1001/p2').sort_stats('tottime').print_stats(12)
EOF
. $TMPDIR/env/bin/activate && PYTHONPATH=. python $TMPDIR/t2.py 2>&1 | tail -40
```

```
Fri Nov 13 04:07:14 UTC 2026
cne vs members 24.783313035964966
random groups 20 18.32659387588501 [{'site': 10, 'cne': 0, 'size': 3, 'n_groups': 20, 'level': 1, 'count': 1225, 'excluded': False, 'ptd_cne': np.float64(2.256502151489258), 'ptd_rand_median': 2.2858471870422363, 'ui_ptd': 0.5238095238095238, 'mi_cne': np.float64(0.31012413782304654), 'mi_rand_median': 0.2898490654502778, 'ui_mi': 0.3333333333333333}, {'site': 10, 'cne': 1, 'size': 4, 'n_groups': 20, 'level': 1, 'count': 3485, 'excluded': False, 'ptd_cne': np.float64(1.9274424314498901), 'ptd_rand_median': 1.6369426250457764, 'ui_ptd': 0.3333333333333333, 'mi_cne': np.float64(0.12778397796500315), 'mi_rand_median': 0.11756692521501172, 'ui_mi': 0.38095238095238093}]
Fri Nov 13 04:08:32 2026    /tmp/claude-1001/p2

         73752 function calls in 7.787 seconds

   Ordered by: internal time
   List reduced from 211 to 12 due to restriction <12>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      154    3.953    0.026    3.954    0.026 /tmp/claude-1001/env/lib/python3.13/site-packages/numpy/fft/_pocketfft.py:58(_raw_fft)
       76    1.626    0.021    5.566    0.073 entries/see-2018/cne.py:373(projections)
     6619    0.491    0.000    0.491    0.000 {method 'reduce' of 'numpy.ufunc' objects}
      380    0.432    0.001    0.432    0.001 {method 'searchsorted' of 'numpy.ndarray' objects}
       76    0.247    0.003    0.364    0.005 entries/see-2018/cne.py:363(sta)
        3    0.237    0.079    0.241    0.080 entries/see-2018/cne.py:461(sample_dg)
        3    0.181    0.060    0.209    0.070 entries/see-2018/cne.py:183(fastica)
     2826    0.114    0.000    0.114    0.000 {method 'at' of 'numpy.ufunc' objects}
      393    0.098    0.000    0.098    0.000 {built-in method numpy.zeros}
[... 3 more lines not kept]
```

**Agent**

Model iterations are cheap; the FFT projection dominates. Replacing it with one small matmul plus shifted sums.

**Agent calls Bash**

```bash
python - <<'EOF'
p='cne.py'; s=open(p).read()
a=s.index('def projections('); b=s.index('def _hist(')
s=s[:a]+'''def projections(stim: np.ndarray, strf: np.ndarray) -> np.ndarray:
    """z(t) = s(t) . STRF for every stimulus segment ending at bin t (valid for t >= lags - 1; the
    first lags - 1 values are partial sums)."""
    nf, lags = strf.shape
    m = strf.T @ stim
    z = np.zeros(stim.shape[1], dtype=np.float64)
    for j in range(lags):
        shift = lags - 1 - j
        z[shift:] += m[j, :stim.shape[1] - shift]
    return z


'''+s[b:]
s=s.replace('''def stim_fft(stim: np.ndarray) -> np.ndarray:
    nfft = 1 << int(np.ceil(np.log2(stim.shape[1] + 64)))
    return np.fft.rfft(stim, n=nfft, axis=1).astype(np.complex64)


''','')
s=s.replace("zall = projections(sfft, strf, stim.shape[1])","zall = projections(stim, strf)")
s=s.replace("z = projections(sfft, strf, stim.shape[1])[np.clip(seg, 0, None)]","z = projections(stim, strf)[np.clip(seg, 0, None)]")
s=s.replace("def _strf_measures(times: np.ndarray, stim: np.ndarray, sfft: np.ndarray, rng)","def _strf_measures(times: np.ndarray, stim: np.ndarray, rng)")
s=s.replace("_strf_measures(ev_s, stim, sfft, rng)","_strf_measures(ev_s, stim, rng)").replace("_strf_measures(sp_s, stim, sfft, rng)","_strf_measures(sp_s, stim, rng)").replace("_strf_measures(np.sort(rng.choice(t, k, replace=False)), stim, sfft, rng)","_strf_measures(np.sort(rng.choice(t, k, replace=False)), stim, rng)")
s=s.replace("    sfft = stim_fft(stim)\n","")
open(p,'w').write(s)
EOF
grep -n "sfft\|stim_fft" cne.py; . $TMPDIR/env/bin/activate && PYTHONPATH=. python -c "
import numpy as np,cne,time
st=np.random.default_rng(0).standard_normal((64,120000)).astype(np.float32); f=np.random.default_rng(1).standard_normal((64,20)).astype(np.float32)
t=time.time(); z=cne.projections(st,f); print(time.time()-t)
t0=100; print(z[t0], (st[:,t0-19:t0+1]*f).sum())
"
```

```
0.007303714752197266
19.85915744304657 19.859163
```

**Agent**

Projection now takes 7 ms and matches the direct dot product. Timing the bin-size analysis (the heaviest) on one site.

**Agent calls Bash**

```bash
cat > $TMPDIR/t3.py <<'EOF'
import time, warnings, numpy as np, cne
warnings.filterwarnings("ignore")
cne.SITES = cne.load_sites()
for s in cne.SITES: cne.prepare(s)
raw = cne.load_stimulus("rn16"); cne.STIM[("rn16",5)] = cne.downsample(raw,5); del raw
i=9
t=time.time(); r=cne.run_binsizes(i, 4); print("binsizes", time.time()-t)
for b,v in r.items(): print(b, v["n"], np.mean(v["sizes_a"]) if v["sizes_a"] else None, {k:np.round(np.mean(x),3) for k,x in v["mi"].items()})
det=cne.run_main(i,1)
t=time.time(); rg=cne.run_random_groups(i, det, 6, n_groups=100); print("random groups 100", time.time()-t)
t=time.time(); m=cne.run_models(i, det, 5, 10); print("models 10", time.time()-t, {k:(v['n'].mean(),np.nanmean(v['size'])) for k,v in m.items()})
EOF
. $TMPDIR/env/bin/activate && PYTHONPATH=. python $TMPDIR/t3.py
```

```
binsizes 190.9269986152649
2 12 3.0 {('quadratic', 'a'): np.float64(0.263), ('quadratic', 'b'): np.float64(0.092), ('linear', 'a'): np.float64(0.22), ('linear', 'b'): np.float64(0.095)}
5 11 3.272727272727273 {('quadratic', 'a'): np.float64(0.439), ('quadratic', 'b'): np.float64(0.079), ('linear', 'a'): np.float64(0.339), ('linear', 'b'): np.float64(0.084)}
8 9 4.0 {('quadratic', 'a'): np.float64(0.555), ('quadratic', 'b'): np.float64(0.073), ('linear', 'a'): np.float64(0.455), ('linear', 'b'): np.float64(0.077)}
10 9 4.111111111111111 {('quadratic', 'a'): np.float64(0.606), ('quadratic', 'b'): np.float64(0.063), ('linear', 'a'): np.float64(0.52), ('linear', 'b'): np.float64(0.075)}
15 8 3.75 {('quadratic', 'a'): np.float64(0.722), ('quadratic', 'b'): np.float64(0.064), ('linear', 'a'): np.float64(0.623), ('linear', 'b'): np.float64(0.073)}
20 7 4.142857142857143 {('quadratic', 'a'): np.float64(0.722), ('quadratic', 'b'): np.float64(0.056), ('linear', 'a'): np.float64(0.648), ('linear', 'b'): np.float64(0.069)}
35 5 4.8 {('quadratic', 'a'): np.float64(0.691), ('quadratic', 'b'): np.float64(0.056), ('linear', 'a'): np.float64(0.688), ('linear', 'b'): np.float64(0.059)}
50 4 4.5 {('quadratic', 'a'): np.float64(0.664), ('quadratic', 'b'): np.float64(0.07), ('linear', 'a'): np.float64(0.694), ('linear', 'b'): np.float64(0.069)}
random groups 100 31.602596044540405
models 10 4.627218723297119 {'shuffled': (np.float64(0.8), np.float64(5.857142857142857)), 'pr10': (np.float64(1.0), np.float64(3.3)), 'pr5': (np.float64(1.1), np.float64(3.8)), 'dg': (np.float64(8.3), np.float64(3.9916666666666663))}
```

**Agent**

Bin sizes take about 190 s per site (about 13 min over 16 sites on 4 workers), 100 random groups about 30 s per site, models about 0.5 s per iteration. That fits. Writing the notebook now (04:15).

**Agent calls Bash**

```bash
python - <<'EOF'
p='cne.py'; s=open(p).read()
s=s.replace('''                          "fs": float(s.fs)})''','''                          "fs": float(s.fs),
                          "waveform": np.asarray(s.meanwaveform, dtype=float)})''')
open(p,'w').write(s)
EOF
cat > $TMPDIR/py2nb.py <<'EOF'
"""Convert a '# %%' script to a notebook. '# %% [markdown]' starts a markdown cell; '# %% tags=a,b' sets tags."""
import sys, nbformat
src = open(sys.argv[1]).read().split("\n# %%")
nb = nbformat.v4.new_notebook()
nb.metadata = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
               "language_info": {"name": "python"}}
for chunk in src:
    if not chunk.strip():
        continue
    head, _, body = chunk.partition("\n")
    head = head.lstrip("# %").strip()
    tags = []
    if "tags=" in head:
        tags = head.split("tags=")[1].split()[0].split(",")
    if head.startswith("[markdown]"):
        text = "\n".join(l[2:] if l.startswith("# ") else l.lstrip("#") for l in body.strip("\n").split("\n"))
        c = nbformat.v4.new_markdown_cell(text)
    else:
        c = nbformat.v4.new_code_cell(body.strip("\n"))
    if tags:
        c.metadata["tags"] = tags
    nb.cells.append(c)
nbformat.write(nb, sys.argv[2])
EOF
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb.py",
 "content": "# %% [markdown]\n# # Reproducing See et al. (2018) from CRCNS ac-3\n#\n# **Paper.** See JZ, Atencio CA, Sohal VS, Schreiner CE (2018). Coordinated neuronal ensembles in\n# primary auditory cortical columns. *eLife* 7:e35587,\n# [doi:10.7554/eLife.35587](https://doi.org/10.7554/eLife.35587). The claims file\n# (`claims/see-2018.yaml`) was written from the version of record (PMC6017807) with its figure\n# legends, Materials and methods, and Supplementary file 1.\n#\n# **Data set.** [CRCNS ac-3](https://doi.org/10.6080/K09021X1) (See, Atencio & Schreiner 2018),\n# read from the public bucket `crcnsarchive` under `ac-3/live/`, zip files opened in place.\n# CRCNS data sets are not versioned, so the version is recorded as `unversioned`, the only one\n# published; the paper cites the data set by its DOI and no version. The files read have these MD5\n# sums in the data set's `checksums.md5`: `Data.zip` 3140d6178de9c044932901795a4cc817,\n# `Stimulus.zip` ce43beade196882598cecddff5520d7b (the notebook prints the listing it read).\n# The data descriptor is version 0.6 (March 28, 2018).\n#\n# **What the data set holds.** 16 recordings (`site1` to `site16`), 8 with the DMR (`rn1`) and 8\n# with the RN (`rn16`), 655 units, the 10-min stimuli and their triggers: the 32-channel columnar\n# recordings behind Figures 1 to 7, 10 and 11C to F. It does not hold the 50 repeats of the 5-s\n# segments (Figure 9 and its supplements), the 15 repeats of the 10-min RN (Figure 11A, B and the\n# 'repeat' CRs of Figure 11E, F) or the 64-channel recordings with spontaneous and evoked epochs\n# (Figure 8).\n#\n# | Claim | Tested here |\n# |---|---|\n# | fig2bd-pwc-measures-covary | tested |\n# | fig2eg-distance-weak | tested |\n# | fig4-example-nine-cnes | tested |\n# | fig4s2-interleaved-halves-stable | tested |\n# | fig4s3-train-test-83pct | tested |\n# | fig5a-mi-peaks-10-15ms | tested |\n# | fig5b-number-decreases-with-bin | tested |\n# | fig5c-size-increases-with-bin | tested |\n# | fig6c-spike-pwc-narrower-than-strf-pwc | tested |\n# | fig6j-sharpness-cne-pairs | tested |\n# | fig6-member-pwc-sharpness-delay | tested |\n# | fig7-totals, fig7a, fig7b, fig7-negative-weights, fig7c, fig7d, fig7e, fig7f | tested |\n# | fig8-spont-evoked-72pct | blocked: the 64-channel recordings are not in the data set |\n# | fig9c-cne-events-more-mi, fig9s1-cne-mi-above-random-groups, fig9s2-noise-correlations | blocked: the 5-s repeats are not in the data set |\n# | fig10b-ptd-higher, fig10c-strf-mi-higher, fig10s1-random-group-strfs | tested |\n# | fig11ab-real-vs-surrogate | blocked: the 15 repeats of the 10-min RN are not in the data set |\n# | fig11c-models-number, fig11d-models-size | tested |\n# | fig11ef-coincidence-ratios | tested on the three models; the 'repeat' CR needs the repeats |\n# | fig11s3b-pr-strf-similarity | tested |\n#\n# Loading and measures are in `cne.py`; its docstring says where each parameter comes from.\n# Heavy steps run in four worker processes, one recording each. Every section has its own seed.\n\n# %%\nimport os\nfor _v in (\"OMP_NUM_THREADS\", \"OPENBLAS_NUM_THREADS\", \"MKL_NUM_THREADS\"):\n    os.environ[_v] = \"1\"\nimport itertools\nimport multiprocessing as mp\nimport resource\nimport time\nimport warnings\nfrom concurrent.futures import ProcessPoolExecutor\nfrom urllib.request import urlopen\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\n\nimport cne\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\nstarted = time.time()\n\nprint(f\"data set {cne.DATASET}, version {cne.VERSION}, from {cne.BASE}\")\nprint(urlopen(f\"{cne.BASE}/checksums.md5\").read().decode())\ncne.SITES = cne.load_sites()\nfor s in cne.SITES:\n    cne.prepare(s)\nparams = {n: cne.load_params(n) for n in (\"rn1\", \"rn16\")}\nstim_info = {}\nfor name in (\"rn1\", \"rn16\"):\n    raw = cne.load_stimulus(name)\n    stim_info[name] = {\"shape\": raw.shape, \"min\": float(raw.min()), \"max\": float(raw.max()),\n                       \"mean\": float(raw.mean())}\n    cne.STIM[(name, cne.STRF_BIN_MS)] = cne.downsample(raw, cne.STRF_BIN_MS)\n    cne.STIM[(name, 1)] = cne.downsample(raw, 1)\n    del raw\nIDX = list(range(len(cne.SITES)))\nSITE_IDS = [s[\"site\"] for s in cne.SITES]\n\n\ndef pmap(fn, *args):\n    with ProcessPoolExecutor(4, mp_context=mp.get_context(\"fork\")) as ex:\n        return list(ex.map(fn, *args))\n\n\nprint(f\"loaded {len(cne.SITES)} recordings and 2 stimuli in {time.time() - started:.0f} s; \"\n      f\"peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\n# %% [markdown]\n# ## Data check\n#\n# Each check of the descriptor against the values is stated under its output.\n\n# %% tags=sanity\nrows = []\nfor s in cne.SITES:\n    trig_ms = s[\"trigger\"] / cne.FS * 1000\n    sp = np.concatenate([u[\"spikes_ms\"] for u in s[\"units\"]])\n    st = np.concatenate([u[\"stim_ms\"] for u in s[\"units\"]])\n    rows.append({\"site\": s[\"site\"], \"file\": s[\"file\"], \"stim\": s[\"stim\"],\n                 \"unit_stim\": \",\".join(sorted({u[\"stim\"] for u in s[\"units\"]})),\n                 \"units\": len(s[\"units\"]), \"tip_depth_um\": \",\".join(str(int(v)) for v in sorted({u[\"tip_depth\"] for u in s[\"units\"]})),\n                 \"fs\": \",\".join(str(int(v)) for v in sorted({u[\"fs\"] for u in s[\"units\"]})),\n                 \"triggers\": len(s[\"trigger\"]),\n                 \"trig_interval_ms\": f\"{np.diff(trig_ms).min():.2f}-{np.diff(trig_ms).max():.2f}\",\n                 \"first_trig_s\": round(trig_ms[0] / 1000, 2),\n                 \"stim_s\": round(cne.stim_duration_ms(s) / 1000, 1),\n                 \"spikes\": len(sp), \"spike_s\": f\"{sp.min() / 1000:.1f}-{sp.max() / 1000:.1f}\",\n                 \"in_stimulus\": round(float(np.isfinite(st).mean()), 3),\n                 \"depth_um\": f\"{min(u['depth'] for u in s['units']):.0f}-{max(u['depth'] for u in s['units']):.0f}\",\n                 \"lateral_um\": \",\".join(str(int(v)) for v in sorted({u[\"x\"] for u in s[\"units\"]})),\n                 \"sorted\": all(np.all(np.diff(u[\"spikes_ms\"]) >= 0) for u in s[\"units\"])})\ninfo = pd.DataFrame(rows)\nprint(info.to_string(index=False))\nprint(\"\\nrecordings\", len(info), \"| units\", info.units.sum(), \"| by stimulus\", info.groupby(\"stim\").units.agg([\"count\", \"sum\"]).to_dict())\nfor name, p in params.items():\n    print(f\"{name}: NF {p['NF']}, NT {p['NT']}, taxis step {np.diff(p['taxis'])[0] * 1000:.2f} ms over \"\n          f\"{p['taxis'][-1] * 1000:.0f} ms, f1 {p['f1']} Hz, f2 {p['f2']} Hz, MaxFM {p['MaxFM']} Hz, \"\n          f\"MaxRD {p['MaxRD']} cyc/oct, FM shape {np.shape(p['FM'])}\")\nfor name, v in stim_info.items():\n    n_trig = sorted(set(info[info.stim == name].triggers))\n    print(f\"{name} stim_mat {v['shape']}, {v['shape'][1] / cne.NT:.1f} trigger periods (triggers in its files: {n_trig}); \"\n          f\"range {v['min']:.1f} to {v['max']:.1f}, mean {v['mean']:.2f}\")\n\n# %% [markdown]\n# The descriptor's counts and units hold. There are 16 files, 8 per stimulus, and the `stim` field\n# of every unit matches its file name. The 655 units match the paper's total. Every `fs` is\n# 20 kHz. The triggers come every 333.3 ms (6666 or 6667 samples), which is the parameter files'\n# `taxis` of 667 columns of 0.5 ms. Each stimulus matrix has exactly 667 columns per trigger of\n# its files (1795 for rn1, 1799 for rn16), so it covers about 598 s, the \"10-min\" stimulus. The\n# envelope runs from -20 to 20 dB, the 40 dB modulation depth of the Methods, over 64 carriers\n# from 500 Hz to 40 kHz. Spike times are in ms and sorted. They run from about 0 to 622 s, and 96\n# to 98% of the spikes fall within the stimulus. `position` is a pair: a lateral offset of -50, 0\n# or 50 um (the three shanks' columns of the a1x32-poly3) and a depth of 153 to 662 um below the\n# surface, 150 um above the tip at the deepest. Sites 13 and 14 have one first trigger at 1.02 s\n# where the others have 1.00 s. Site pairs (1, 2), (3, 4) and so on share a tip depth, so they may\n# be one penetration recorded with both stimuli; the next cell tests whether any unit appears in\n# two files.\n\n# %% tags=sanity\n# Units deposited twice: identical spike trains, or the same mean waveform on the same probe channel.\ndups, best = [], []\nfor a, b in itertools.combinations(range(len(cne.SITES)), 2):\n    A, B = cne.SITES[a], cne.SITES[b]\n    for ua in A[\"units\"]:\n        for ub in B[\"units\"]:\n            if len(ua[\"spikes_ms\"]) == len(ub[\"spikes_ms\"]) and np.allclose(ua[\"spikes_ms\"], ub[\"spikes_ms\"]):\n                dups.append((A[\"site\"], B[\"site\"]))\n    if A[\"site\"] % 2 == 1 and B[\"site\"] == A[\"site\"] + 1:\n        rs = []\n        for ua in A[\"units\"]:\n            cands = [np.corrcoef(ua[\"waveform\"][:, -1], ub[\"waveform\"][:, -1])[0, 1]\n                     for ub in B[\"units\"] if ub[\"probechan\"] == ua[\"probechan\"]]\n            rs.append(max(cands) if cands else np.nan)\n        best.append({\"sites\": f\"{A['site']}-{B['site']}\", \"units_with_same_channel\": int(np.isfinite(rs).sum()),\n                     \"median_best_waveform_r\": round(float(np.nanmedian(rs)), 3),\n                     \"r_above_0.99\": int(np.nansum(np.array(rs) > 0.99))})\nwithin = sum(1 for s in cne.SITES for ua, ub in itertools.combinations(s[\"units\"], 2)\n             if len(ua[\"spikes_ms\"]) == len(ub[\"spikes_ms\"]) and np.allclose(ua[\"spikes_ms\"], ub[\"spikes_ms\"]))\nprint(\"identical spike trains across files:\", len(dups), \"| within files:\", within)\nprint(pd.DataFrame(best).to_string(index=False))\n\n# %% [markdown]\n# No spike train appears twice, within or across files. No unit of one file has a mean waveform\n# correlated above 0.99 with a unit on the same probe channel of the paired file. The paired files\n# share a tip depth, but their units were sorted separately and cannot be matched, so each file is\n# counted as one recording, as the paper counts 16 penetrations.\n\n# %% tags=sanity\n# Clock check: the STRF of each unit with its spikes on the stimulus clock against the same spikes\n# shifted by 30 s (circularly within the stimulus). A shared clock gives a structured STRF only when\n# aligned, with its peak at the 10 to 30 ms latency of AI (Methods, Electrophysiology).\nrng_clock = np.random.default_rng(11)\nrows = []\nfor s in cne.SITES:\n    stim = cne.STIM[(s[\"stim\"], cne.STRF_BIN_MS)]\n    dur = cne.stim_duration_ms(s)\n    for k, u in enumerate(s[\"units\"]):\n        t = u[\"stim_ms\"][np.isfinite(u[\"stim_ms\"])]\n        out = {\"site\": s[\"site\"], \"unit\": k}\n        for label, tt in ((\"aligned\", t), (\"shifted_30s\", (t + 30000) % dur)):\n            st = cne.sta(stim, cne.segment_index(tt, cne.STRF_BIN_MS, stim.shape[1], cne.STRF_LAGS), cne.STRF_LAGS)\n            out[f\"ptd_{label}\"] = float(st.max() - st.min())\n            prof = np.abs(st - st.mean()).max(axis=0)\n            out[f\"peak_lag_ms_{label}\"] = (cne.STRF_LAGS - 1 - int(prof.argmax())) * cne.STRF_BIN_MS + cne.STRF_BIN_MS / 2\n        rows.append(out)\nclock = pd.DataFrame(rows)\nclock[\"ratio\"] = clock.ptd_aligned / clock.ptd_shifted_30s\nsummary = clock.groupby(\"site\").agg(units=(\"unit\", \"size\"), median_ptd_ratio=(\"ratio\", \"median\"),\n                                    frac_ratio_above_1_5=(\"ratio\", lambda r: (r > 1.5).mean()),\n                                    median_peak_lag_aligned=(\"peak_lag_ms_aligned\", \"median\"),\n                                    median_peak_lag_shifted=(\"peak_lag_ms_shifted_30s\", \"median\"))\nprint(summary.round(2).to_string())\nprint(\"\\nall units: median PTD ratio aligned/shifted %.2f; units with ratio > 1.5: %d of %d; peak lags of \"\n      \"units with ratio > 1.5, median %.1f ms (IQR %.1f-%.1f)\" % (\n          clock.ratio.median(), (clock.ratio > 1.5).sum(), len(clock),\n          clock[clock.ratio > 1.5].peak_lag_ms_aligned.median(),\n          *clock[clock.ratio > 1.5].peak_lag_ms_aligned.quantile([0.25, 0.75])))\n\n# %% [markdown]\n# CLOCK_CONCLUSION\n\n# %% [markdown]\n# ## cNE detection on the 16 recordings\n#\n# The detection of the claims file's opening comment, at 10 ms, with 100 circular shuffles for the\n# membership and activity thresholds. Membership uses IC sign reading (a) unless a claim says\n# otherwise; reading (b) is shown where the claims file names it. Units without spikes inside the\n# stimulus would be left out; the count is printed.\n\n# %%\nt0 = time.time()\nmain = dict(zip(SITE_IDS, pmap(cne.run_main, IDX, [1000 + s for s in SITE_IDS])))\nprint(f\"detection on {len(main)} recordings in {time.time() - t0:.0f} s\")\nprint(\"units left out for having no spikes:\", sum(d[\"n_units\"] - len(d[\"kept\"]) for d in main.values()))\nrows = []\nfor s in cne.SITES:\n    d = main[s[\"site\"]]\n    n = len(s[\"units\"])\n    rows.append({\"site\": s[\"site\"], \"stim\": s[\"stim\"], \"units\": n, \"cnes\": d[\"n\"],\n                 \"mp_bound\": round(d[\"bound\"], 3),\n                 \"member_threshold_a\": tuple(np.round(d[\"thresholds\"][\"a\"], 3)),\n                 \"member_threshold_b\": tuple(np.round(d[\"thresholds\"][\"b\"], 3)),\n                 \"1.5/sqrt(n)\": round(1.5 / np.sqrt(n), 3),\n                 \"sizes_a\": [len(m) for m in cne.member_sets(d, \"a\")],\n                 \"sizes_b\": [len(m) for m in cne.member_sets(d, \"b\")]})\nper_site = pd.DataFrame(rows)\nprint(per_site.to_string(index=False))\n\n# %% [markdown]\n# The membership thresholds are close to plus or minus 1.5/sqrt(n), the spread of the weights of a\n# random unit vector over n units: the shuffled ICs carry no structure, as the Methods expect.\n\n# %% [markdown]\n# ## fig7-totals\n#\n# > Across 16 penetrations, 104 cNEs were identified from 655 isolated neurons, an average of\n# > 6.5 +/- 2.0 cNEs per penetration.\n\n# %% tags=claim:fig7-totals\nprint(\"penetrations:\", len(per_site), \"| units:\", per_site.units.sum())\nprint(\"cNEs in total:\", per_site.cnes.sum())\nprint(\"cNEs per penetration: mean %.2f, SD %.2f (n-1), SD %.2f (n); range %d to %d\" % (\n    per_site.cnes.mean(), per_site.cnes.std(), per_site.cnes.std(ddof=0), per_site.cnes.min(), per_site.cnes.max()))\nprint(per_site.groupby(\"stim\").cnes.agg([\"count\", \"sum\", \"mean\"]).to_string())\n\n# %% [markdown]\n# RESULT_fig7-totals\n\n# %% [markdown]\n# ## fig4-example-nine-cnes\n#\n# > In an example columnar recording with 38 isolated neurons, the cNE detection found nine cNEs,\n# > with 2 to 6 member neurons each.\n\n# %% tags=claim:fig4-example-nine-cnes\nex = per_site[per_site.units == 38]\nprint(\"recordings with 38 units:\", ex.site.tolist())\nfor site in ex.site:\n    d = main[site]\n    for r in cne.SIGN_READINGS:\n        sizes = [len(m) for m in cne.member_sets(d, r)]\n        pos = [len(m[\"pos\"]) for m in d[\"members\"][r]]\n        print(f\"site {site}, sign reading ({r}): {d['n']} cNEs; sizes {sorted(sizes)} (range {min(sizes)}-{max(sizes)}); \"\n              f\"positive members only {sorted(pos)}\")\n# Seed dependence of the example: the detection with five other seeds\nfor k in range(5):\n    d = cne.detect(cne.binned(cne.SITES[SITE_IDS.index(ex.site.iloc[0])], cne.BIN_MS), 50 + k, activity_null=False)\n    print(f\"seed {50 + k}: {d['n']} cNEs, sizes (a) {sorted(len(m) for m in cne.member_sets(d, 'a'))}\")\nd = main[ex.site.iloc[0]]\nfig, ax = plt.subplots(figsize=(7, 3))\nax.imshow(cne.orient(d[\"w\"], \"a\"), aspect=\"auto\", cmap=\"RdBu_r\", vmin=-1, vmax=1)\nax.set_xlabel(\"cNE\"); ax.set_ylabel(\"unit\"); ax.set_title(f\"IC weights, site {ex.site.iloc[0]} (all within -1 to 1)\")\nplt.show()\n\n# %% [markdown]\n# RESULT_fig4-example-nine-cnes\n\n# %% [markdown]\n# ## fig7a-number-vs-neurons\n#\n# > The number of cNEs per penetration increased with the number of isolated neurons (R2 = 0.74),\n# > and was about 15% of the number of recorded neurons.\n\n# %% tags=claim:fig7a-number-vs-neurons\nfit = stats.linregress(per_site.units, per_site.cnes)\nprint(\"least-squares line of cNEs on units: slope %.3f, intercept %.2f, R2 %.3f, F-test p %.2g (n = %d)\" % (\n    fit.slope, fit.intercept, fit.rvalue ** 2, fit.pvalue, len(per_site)))\nprint(\"fraction (a) mean of cNEs/units: %.1f%%\" % (100 * (per_site.cnes / per_site.units).mean()))\nprint(\"fraction (b) slope: %.1f%%\" % (100 * fit.slope))\nprint(\"fraction (c) total cNEs / total units: %.1f%%\" % (100 * per_site.cnes.sum() / per_site.units.sum()))\nfig, ax = plt.subplots(figsize=(4, 3))\nax.plot(per_site.units, per_site.cnes, \"o\")\nax.set_xlabel(\"units\"); ax.set_ylabel(\"cNEs\"); plt.show()\n\n# %% [markdown]\n# RESULT_fig7a-number-vs-neurons\n\n# %% [markdown]\n# ## fig7b-size-vs-neurons\n#\n# > The mean cNE size was 7.4 +/- 2.5 neurons, about 17% of the recorded neurons, and increased\n# > with the number of isolated neurons, more weakly than the number of cNEs (R2 = 0.33).\n\n# %% tags=claim:fig7b-size-vs-neurons\nfor r in cne.SIGN_READINGS:\n    sizes = per_site[f\"sizes_{r}\"]\n    pooled = np.concatenate([np.array(x, float) for x in sizes])\n    pooled_frac = np.concatenate([np.array(x, float) / n for x, n in zip(sizes, per_site.units)])\n    site_mean = np.array([np.mean(x) for x in sizes])\n    fit_b = stats.linregress(per_site.units, site_mean)\n    print(f\"sign reading ({r})\")\n    print(\"  size (a) pooled over %d cNEs: mean %.2f, SD %.2f; (b) mean of per-penetration means %.2f, SD %.2f\" % (\n        len(pooled), pooled.mean(), pooled.std(ddof=1), site_mean.mean(), site_mean.std(ddof=1)))\n    print(\"  fraction of units: (a) pooled %.1f%%; (b) per penetration %.1f%%\" % (\n        100 * pooled_frac.mean(), 100 * (site_mean / per_site.units).mean()))\n    print(\"  per-penetration mean size on units: slope %.3f, R2 %.3f, F-test p %.2g\" % (\n        fit_b.slope, fit_b.rvalue ** 2, fit_b.pvalue))\n    print(\"  sizes range %d to %d\" % (pooled.min(), pooled.max()))\n\n# %% [markdown]\n# RESULT_fig7b-size-vs-neurons\n\n# %% [markdown]\n# ## fig7-negative-weights\n#\n# > The IC weights of almost all cNE members were positive; 9 cNEs (8.3%) had at least one member\n# > with a negative weight.\n\n# %% tags=claim:fig7-negative-weights\nfor r in cne.SIGN_READINGS:\n    pos = sum(len(m[\"pos\"]) for d in main.values() for m in d[\"members\"][r])\n    neg = sum(len(m[\"neg\"]) for d in main.values() for m in d[\"members\"][r])\n    with_neg = sum(1 for d in main.values() for m in d[\"members\"][r] if len(m[\"neg\"]))\n    total = sum(d[\"n\"] for d in main.values())\n    print(f\"sign reading ({r}): cNEs with a negative-weight member {with_neg} of {total} ({100 * with_neg / total:.1f}%); \"\n          f\"member weights positive {pos} of {pos + neg} ({100 * pos / (pos + neg):.1f}%)\")\n\n# %% [markdown]\n# RESULT_fig7-negative-weights\n\n# %% [markdown]\n# ## fig7c-membership\n#\n# > Of the 655 isolated neurons, about 68% belonged to a single cNE, about 9% to none and about 23%\n# > to more than one.\n\n# %% tags=claim:fig7c-membership\nfor r in cne.SIGN_READINGS:\n    counts = []\n    for s in cne.SITES:\n        sets = cne.member_sets(main[s[\"site\"]], r)\n        counts += [sum(1 for m in sets if k in m) for k in range(len(s[\"units\"]))]\n    counts = np.array(counts)\n    print(f\"sign reading ({r}), {len(counts)} units: one cNE {100 * (counts == 1).mean():.1f}%, none \"\n          f\"{100 * (counts == 0).mean():.1f}%, more than one {100 * (counts > 1).mean():.1f}%; most cNEs of one unit: {counts.max()}\")\n\n# %% [markdown]\n# RESULT_fig7c-membership\n\n# %% [markdown]\n# ## fig7d-pairs-within-200um\n#\n# > About 82% of pairs of neurons in the same cNE were recorded on channels less than 200 um\n# > apart, so cNEs are mostly spatially confined.\n\n# %% tags=claim:fig7d-pairs-within-200um\npair_rows = []\nfor s in cne.SITES:\n    for j, m in enumerate(cne.member_sets(main[s[\"site\"]], \"a\")):\n        for a, b in itertools.combinations(m, 2):\n            ua, ub = s[\"units\"][a], s[\"units\"][b]\n            pair_rows.append({\"site\": s[\"site\"], \"cne\": j, \"a\": a, \"b\": b,\n                              \"depth_diff\": abs(ua[\"depth\"] - ub[\"depth\"]),\n                              \"euclid\": float(np.hypot(ua[\"x\"] - ub[\"x\"], ua[\"depth\"] - ub[\"depth\"]))})\ncpairs = pd.DataFrame(pair_rows)\nuniq = cpairs.drop_duplicates([\"site\", \"a\", \"b\"])\nfor label, df in ((\"once per cNE\", cpairs), (\"each pair once\", uniq)):\n    for dist in (\"depth_diff\", \"euclid\"):\n        print(f\"{label}, {dist}: {100 * (df[dist] < 200).mean():.1f}% of {len(df)} pairs under 200 um \"\n              f\"(range {df[dist].min():.0f} to {df[dist].max():.0f} um)\")\nprint(\"\\nby recording, depth difference, once per cNE:\")\nprint(cpairs.groupby(\"site\").depth_diff.apply(lambda d: round(100 * (d < 200).mean(), 1)).to_string())\n\n# %% [markdown]\n# RESULT_fig7d-pairs-within-200um\n\n# %% [markdown]\n# ## fig7e-no-depth-bias\n#\n# > cNEs and their member neurons were found across the whole explored depth with no bias to any\n# > depth; the depths of cNE members and of all recorded neurons were similarly distributed.\n\n# %% tags=claim:fig7e-no-depth-bias\nall_depth, mem_depth, cne_depth = [], [], []\nfor s in cne.SITES:\n    sets = cne.member_sets(main[s[\"site\"]], \"a\")\n    inany = set().union(*[set(m.tolist()) for m in sets]) if sets else set()\n    all_depth += [u[\"depth\"] for u in s[\"units\"]]\n    mem_depth += [s[\"units\"][k][\"depth\"] for k in sorted(inany)]\n    cne_depth += [np.median([s[\"units\"][k][\"depth\"] for k in m]) for m in sets if len(m)]\nall_depth, mem_depth, cne_depth = map(np.array, (all_depth, mem_depth, cne_depth))\nks = stats.ks_2samp(mem_depth, all_depth)\nmw = stats.mannwhitneyu(mem_depth, all_depth)\nprint(f\"members {len(mem_depth)}, all units {len(all_depth)}, cNEs {len(cne_depth)}\")\nprint(\"median depth: members %.0f, all %.0f, difference %.0f um; cNE depth range %.0f to %.0f um (units %.0f to %.0f)\" % (\n    np.median(mem_depth), np.median(all_depth), np.median(mem_depth) - np.median(all_depth),\n    cne_depth.min(), cne_depth.max(), all_depth.min(), all_depth.max()))\nprint(\"(a) two-sample KS: D = %.3f, p = %.3g\" % (ks.statistic, ks.pvalue))\nprint(\"(b) Mann-Whitney U: U = %.0f, p = %.3g\" % (mw.statistic, mw.pvalue))\nnonmem = np.setdiff1d(np.arange(len(all_depth)), [])  # variant: members against non-members\nnon_depth = []\nfor s in cne.SITES:\n    sets = cne.member_sets(main[s[\"site\"]], \"a\")\n    inany = set().union(*[set(m.tolist()) for m in sets]) if sets else set()\n    non_depth += [u[\"depth\"] for k, u in enumerate(s[\"units\"]) if k not in inany]\nprint(\"variant, members against non-members (%d): KS p = %.3g, MWU p = %.3g\" % (\n    len(non_depth), stats.ks_2samp(mem_depth, non_depth).pvalue, stats.mannwhitneyu(mem_depth, non_depth).pvalue))\n\n# %% [markdown]\n# RESULT_fig7e-no-depth-bias\n\n# %% [markdown]\n# ## fig7f-span-200um\n#\n# > Most cNEs (about 70%) spanned 200 um of cortical depth or less, though a few spanned most of\n# > the recorded column.\n\n# %% tags=claim:fig7f-span-200um\nspans = []\nfor s in cne.SITES:\n    for m in cne.member_sets(main[s[\"site\"]], \"a\"):\n        d = [s[\"units\"][k][\"depth\"] for k in m]\n        spans.append(max(d) - min(d))\nspans = np.array(spans)\nprint(f\"{len(spans)} cNEs: span <= 200 um {100 * (spans <= 200).mean():.1f}%; median {np.median(spans):.0f} um; \"\n      f\"max {spans.max():.0f} um; over 400 um: {(spans > 400).sum()}\")\nfor r in (\"b\",):\n    sp_b = np.array([max(s[\"units\"][k][\"depth\"] for k in m) - min(s[\"units\"][k][\"depth\"] for k in m)\n                     for s in cne.SITES for m in cne.member_sets(main[s[\"site\"]], r) if len(m)])\n    print(f\"sign reading ({r}): span <= 200 um {100 * (sp_b <= 200).mean():.1f}% of {len(sp_b)}\")\n\n# %% [markdown]\n# RESULT_fig7f-span-200um\n\n# %% [markdown]\n# ## Pairwise correlation functions\n#\n# For every pair of units of a recording: the PWC (1-ms lag bins, +-100 ms and its central\n# +-50 ms), its sharpness and absolute peak delay, the correlation coefficient of the 10-ms binned\n# trains, the depth difference and Euclidean distance of the channels, and whether the pair shares\n# a cNE (sign reading a).\n\n# %%\nt0 = time.time()\npairs = pd.DataFrame([r for rows in pmap(cne.run_pairs, IDX, [main[s] for s in SITE_IDS]) for r in rows])\nprint(f\"{len(pairs)} pairs in {time.time() - t0:.0f} s; pairs without any spike difference within +-50 ms: \"\n      f\"{(pairs.count_50 == 0).sum()}\")\nprint(pairs[[\"r\", \"sharp_50\", \"delay_50\", \"sharp_100\", \"delay_100\", \"depth_diff\", \"euclid\"]].describe().round(3).to_string())\n\n# %% [markdown]\n# ## fig2bd-pwc-measures-covary\n#\n# > Across all penetrations, the sharpness and peak delay of pairwise correlation (PWC) functions\n# > covaried with the pairs' spike train correlation coefficients, accounting for about 50% of the\n# > variance.\n\n# %% tags=claim:fig2bd-pwc-measures-covary\ndef r2(x, y, log=False):\n    x, y = np.asarray(x, float), np.asarray(y, float)\n    ok = np.isfinite(x) & np.isfinite(y)\n    if log:\n        ok &= (x > 0) & (y > 0)\n        x, y = np.log10(x), np.log10(y)\n    f = stats.linregress(x[ok], y[ok])\n    return f.rvalue ** 2, f.slope, int(ok.sum())\n\n\nrows = []\nfor lag in (50, 100):\n    for log in (False, True):\n        rs, ss, ns = r2(pairs.r, pairs[f\"sharp_{lag}\"], log)\n        rd, sd, nd = r2(pairs.r, pairs[f\"delay_{lag}\"], log)\n        rows.append({\"lags\": f\"+-{lag} ms\", \"axes\": \"log\" if log else \"linear\", \"R2_sharpness\": round(rs, 3),\n                     \"slope_sharpness\": round(ss, 3), \"pairs_sharpness\": ns, \"R2_delay\": round(rd, 3),\n                     \"slope_delay\": round(sd, 3), \"pairs_delay\": nd})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"\\nR2 of sharpness against delay, +-50 ms, linear: %.3f\" % r2(pairs.sharp_50, pairs.delay_50)[0])\nfig, axs = plt.subplots(1, 2, figsize=(8, 3))\naxs[0].plot(pairs.r, pairs.sharp_50, \".\", ms=1); axs[0].set_xlabel(\"r (10 ms)\"); axs[0].set_ylabel(\"sharpness (ms), +-50\")\naxs[1].plot(pairs.r, pairs.delay_50, \".\", ms=1); axs[1].set_xlabel(\"r (10 ms)\"); axs[1].set_ylabel(\"|peak delay| (ms), +-50\")\nplt.tight_layout(); plt.show()\nprint(\"plotted: r %.3f to %.3f; sharpness %.0f to %.0f ms; delay %.0f to %.0f ms (all points within the axes)\" % (\n    pairs.r.min(), pairs.r.max(), pairs.sharp_50.min(), pairs.sharp_50.max(), pairs.delay_50.min(), pairs.delay_50.max()))\n\n# %% [markdown]\n# RESULT_fig2bd-pwc-measures-covary\n\n# %% [markdown]\n# ## fig2eg-distance-weak\n#\n# > The correlation between the pairwise synchrony measures (sharpness, peak delay, correlation\n# > coefficient) and the distance between the pair's channels explained only about 10 to 30% of\n# > the variance.\n\n# %% tags=claim:fig2eg-distance-weak\nrows = []\nfor dist in (\"depth_diff\", \"euclid\"):\n    for lag in (50, 100):\n        vals = {\"sharpness\": r2(pairs[dist], pairs[f\"sharp_{lag}\"]), \"delay\": r2(pairs[dist], pairs[f\"delay_{lag}\"]),\n                \"r\": r2(pairs[dist], pairs.r)}\n        rows.append({\"distance\": dist, \"lags\": f\"+-{lag} ms\", **{f\"R2_{k}\": round(v[0], 3) for k, v in vals.items()},\n                     \"in_0.09_0.33\": sum(0.09 <= v[0] <= 0.33 for v in vals.values())})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"\\nvariant, log axes for the measures (pairs with positive values), depth difference, +-50 ms:\",\n      {k: round(r2(pairs.depth_diff, pairs[c], True)[0], 3) for k, c in ((\"sharpness\", \"sharp_50\"), (\"delay\", \"delay_50\"))})\n\n# %% [markdown]\n# RESULT_fig2eg-distance-weak\n\n# %% [markdown]\n# ## fig6j-sharpness-cne-pairs\n#\n# > In every penetration, spike train PWCs were significantly sharper (narrower) for pairs of\n# > neurons in the same cNE than for pairs not in the same cNE.\n\n# %% tags=claim:fig6j-sharpness-cne-pairs\npairs[\"cne_pair\"] = pairs.n_shared > 0\nrows = []\nfor lag in (50, 100):\n    for site, g in pairs.groupby(\"site\"):\n        a = g[g.cne_pair][f\"sharp_{lag}\"].dropna()\n        b = g[~g.cne_pair][f\"sharp_{lag}\"].dropna()\n        p = stats.mannwhitneyu(a, b).pvalue if len(a) and len(b) else np.nan\n        rows.append({\"lags\": lag, \"site\": site, \"cne_pairs\": len(a), \"non_cne_pairs\": len(b),\n                     \"median_cne\": a.median(), \"median_non\": b.median(), \"p\": p,\n                     \"sharper_p<0.001\": bool(p < 0.001 and a.median() < b.median())})\nsj = pd.DataFrame(rows)\nprint(sj.round(4).to_string(index=False))\nprint(\"\\npenetrations with cNE pairs sharper at p < 0.001:\", sj.groupby(\"lags\")[\"sharper_p<0.001\"].sum().to_dict())\nprint(\"cNE / non-cNE pairs in total:\", int(pairs.cne_pair.sum()), int((~pairs.cne_pair).sum()),\n      \"(paper, Supplementary file 1: 3087 / 8838)\")\n\n# %% [markdown]\n# RESULT_fig6j-sharpness-cne-pairs\n\n# %% [markdown]\n# ## fig6-member-pwc-sharpness-delay\n#\n# > PWCs between members of the same cNE are sharp, with a median sharpness of about 2 ms, a mean\n# > sharpness of 3.39 +/- 1.21 ms and a mean absolute peak delay of 0.76 +/- 1.74 ms.\n\n# %% tags=claim:fig6-member-pwc-sharpness-delay\ncp = pairs[pairs.cne_pair]\nrows = []\nfor lag in (50, 100):\n    s_, d_ = cp[f\"sharp_{lag}\"].dropna(), cp[f\"delay_{lag}\"].dropna()\n    rows.append({\"lags\": lag, \"reading\": \"(a) pooled\", \"median_sharp\": s_.median(), \"mean_sharp\": s_.mean(),\n                 \"sd_sharp\": s_.std(), \"mean_abs_delay\": d_.mean(), \"sd_delay\": d_.std(), \"pairs\": len(s_)})\n    g = cp.groupby(\"site\")\n    ms, md, mm = g[f\"sharp_{lag}\"].mean(), g[f\"delay_{lag}\"].mean(), g[f\"sharp_{lag}\"].median()\n    rows.append({\"lags\": lag, \"reading\": \"(b) per penetration\", \"median_sharp\": mm.mean(), \"mean_sharp\": ms.mean(),\n                 \"sd_sharp\": ms.std(), \"mean_abs_delay\": md.mean(), \"sd_delay\": md.std(), \"pairs\": len(ms)})\nprint(pd.DataFrame(rows).round(2).to_string(index=False))\nprint(\"\\nfraction of cNE pairs with peak delay 0 or 1 ms (+-50): %.2f\" % (cp.delay_50 <= 1).mean())\nprint(\"non-cNE pairs, +-50 ms: median sharpness %.1f ms, mean %.1f ms\" % (\n    pairs[~pairs.cne_pair].sharp_50.median(), pairs[~pairs.cne_pair].sharp_50.mean()))\n\n# %% [markdown]\n# RESULT_fig6-member-pwc-sharpness-delay\n\n# %% [markdown]\n# ## fig6c-spike-pwc-narrower-than-strf-pwc\n#\n# > For pairs of neurons in the same cNE, spike train PWCs were much narrower than the PWCs of their\n# > STRFs' temporal profiles, while for pairs not in the same cNE the spike train PWCs were often as\n# > wide as the STRF PWCs.\n#\n# STRFs at 1 ms with 50 lags (as in the data set's sample code, 50 ms); the temporal profile is the\n# mean over frequency at each lag (Figure 6B, E legend); the STRF PWC is the cross-correlation of\n# the two profiles (lags -49 to 49 ms), its sharpness measured as for spike PWCs, with negative\n# values set to zero, as a count histogram cannot be negative (a standard choice). The spike PWCs\n# use the +-50 ms reading.\n\n# %% tags=claim:fig6c-spike-pwc-narrower-than-strf-pwc\nt0 = time.time()\nstrf1 = dict(zip(SITE_IDS, pmap(cne.run_strf_profiles, IDX)))\nprof = {s: [st.mean(axis=0) - st.mean() for st in v] for s, v in strf1.items()}\nsh = []\nfor row in pairs.itertuples():\n    xc = np.correlate(prof[row.site][row.a], prof[row.site][row.b], mode=\"full\")\n    sh.append(cne.pwc_measures(np.clip(xc, 0, None))[0])\npairs[\"strf_sharp\"] = sh\npairs[\"ratio\"] = pairs.sharp_50 / pairs.strf_sharp\nprint(f\"STRFs and STRF PWCs in {time.time() - t0:.0f} s; pairs without a positive STRF PWC: {pairs.strf_sharp.isna().sum()}\")\nfor lab, g in ((\"cNE pairs\", pairs[pairs.cne_pair]), (\"non-cNE pairs\", pairs[~pairs.cne_pair])):\n    ok = g.dropna(subset=[\"ratio\"])\n    print(f\"{lab}: {len(ok)}; spike PWC sharper than STRF PWC in {100 * (ok.sharp_50 < ok.strf_sharp).mean():.1f}%; \"\n          f\"median spike sharpness {ok.sharp_50.median():.1f} ms, STRF PWC {ok.strf_sharp.median():.1f} ms, \"\n          f\"median ratio {ok.ratio.median():.3f}\")\na = pairs[pairs.cne_pair].ratio.dropna(); b = pairs[~pairs.cne_pair].ratio.dropna()\nprint(\"ratio, cNE against non-cNE pairs: Mann-Whitney U p = %.3g (one-sided, cNE lower: %.3g)\" % (\n    stats.mannwhitneyu(a, b).pvalue, stats.mannwhitneyu(a, b, alternative=\"less\").pvalue))\nby = pairs.dropna(subset=[\"ratio\"]).groupby([\"site\", \"cne_pair\"]).apply(lambda g: (g.sharp_50 < g.strf_sharp).mean()).unstack()\nprint(\"\\nfraction with spike PWC sharper, by recording:\\n\", by.round(2).to_string())\n\n# %% [markdown]\n# RESULT_fig6c-spike-pwc-narrower-than-strf-pwc\n\n# %% [markdown]\n# ## fig4s2-interleaved-halves-stable\n#\n# > cNEs detected independently in two interleaved halves of a recording were the same, with about\n# > 96% of the ICs of one half having a significant match in the other.\n\n# %% tags=claim:fig4s2-interleaved-halves-stable\nt0 = time.time()\nhalves = dict(zip(SITE_IDS, pmap(cne.run_halves, IDX, [2000 + s for s in SITE_IDS])))\nprint(f\"halves in {time.time() - t0:.0f} s\")\n\n\ndef full(w, kept, n):\n    out = np.zeros((n, w.shape[1]))\n    out[kept] = w\n    return out\n\n\ndef abscorr(x, y):\n    if x.shape[1] == 0 or y.shape[1] == 0:\n        return np.zeros((x.shape[1], y.shape[1]))\n    return np.abs(np.corrcoef(x.T, y.T)[:x.shape[1], x.shape[1]:])\n\n\nrows = []\nfor s in cne.SITES:\n    h, n = halves[s[\"site\"]], len(s[\"units\"])\n    A, B = full(h[\"A\"][\"w\"], h[\"A\"][\"kept\"], n), full(h[\"B\"][\"w\"], h[\"B\"][\"kept\"], n)\n    sA = [full(w, h[\"A\"][\"kept\"], n) for w in h[\"A\"][\"shuffled_w\"]]\n    sB = [full(w, h[\"B\"][\"kept\"], n) for w in h[\"B\"][\"shuffled_w\"]]\n    real = abscorr(A, B)\n    null_a = np.concatenate([abscorr(x, y).ravel() for x, y in zip(sA, sB)])\n    null_b = np.concatenate([abscorr(A, y).ravel() for y in sB] + [abscorr(B, x).ravel() for x in sA])\n    for reading, null in ((\"a\", null_a), (\"b\", null_b)):\n        thr = np.percentile(null, 99) if len(null) else np.nan\n        mA = (real.max(axis=1) > thr) if real.size else np.zeros(A.shape[1], bool)\n        mB = (real.max(axis=0) > thr) if real.size else np.zeros(B.shape[1], bool)\n        rows.append({\"site\": s[\"site\"], \"reading\": reading, \"ICs_A\": A.shape[1], \"ICs_B\": B.shape[1],\n                     \"threshold\": thr, \"matched_A\": int(mA.sum()), \"matched_B\": int(mB.sum())})\nhv = pd.DataFrame(rows)\nprint(hv.round(3).to_string(index=False))\nfor reading, g in hv.groupby(\"reading\"):\n    tot = g.ICs_A.sum() + g.ICs_B.sum()\n    print(f\"reading ({reading}): {g.matched_A.sum() + g.matched_B.sum()} of {tot} ICs matched \"\n          f\"({100 * (g.matched_A.sum() + g.matched_B.sum()) / tot:.1f}%); thresholds {g.threshold.min():.3f}-{g.threshold.max():.3f}\")\n\n# %% [markdown]\n# RESULT_fig4s2-interleaved-halves-stable\n\n# %% [markdown]\n# ## fig4s3-train-test-83pct\n#\n# > cNEs detected in the first half of a recording predicted cNE activity in the second half; of\n# > 102 training cNEs, about 83% had significant matches to test cNE activity.\n\n# %% tags=claim:fig4s3-train-test-83pct\nt0 = time.time()\ntt = dict(zip(SITE_IDS, pmap(cne.run_traintest, IDX, [3000 + s for s in SITE_IDS])))\nprint(f\"train/test in {time.time() - t0:.0f} s; training cNEs {sum(v['n_train'] for v in tt.values())}, \"\n      f\"test cNEs {sum(v['n_test'] for v in tt.values())}\")\nfor p in cne.PROJECTIONS:\n    matched, null = [], []\n    for v in tt.values():\n        c = v[p]\n        if c.size == 0:\n            matched += [-np.inf] * v[\"n_train\"]\n            continue\n        rmax, cmax = c.argmax(axis=1), c.argmax(axis=0)\n        is_max = np.zeros_like(c, bool)\n        is_max[np.arange(c.shape[0]), rmax] = True\n        is_max[cmax, np.arange(c.shape[1])] = True\n        matched += list(c.max(axis=1))\n        null += list(c[~is_max])\n    thr = np.percentile(null, 95)\n    matched = np.array(matched)\n    print(f\"projection {p}: threshold (95th percentile of {len(null)} non-matched) {thr:.3f}; \"\n          f\"{(matched > thr).sum()} of {len(matched)} training cNEs matched ({100 * (matched > thr).mean():.1f}%); \"\n          f\"matched correlations median {np.median(matched[np.isfinite(matched)]):.3f}\")\n    # variant: null of values that are not the row maximum only (the Results' wording)\n    null2 = []\n    for v in tt.values():\n        c = v[p]\n        if c.size:\n            m = np.ones_like(c, bool); m[np.arange(c.shape[0]), c.argmax(axis=1)] = False\n            null2 += list(c[m])\n    print(f\"   variant, null of all non-row-maximum values: threshold {np.percentile(null2, 95):.3f}, \"\n          f\"{100 * (matched > np.percentile(null2, 95)).mean():.1f}% matched\")\n\n# %% [markdown]\n# RESULT_fig4s3-train-test-83pct\n\n# %% [markdown]\n# ## Bin sizes (Figure 5)\n#\n# Detection at 2, 5, 8, 10, 15, 20, 35 and 50 ms, with 100 shuffles each. For Figure 5A, each\n# cNE's activity is interpolated to 1 ms and given 5000 events, under both projection readings and\n# both event readings: (a) the 5000 largest 1-ms samples, (b) the 5000 largest local peaks. The\n# STRF is the event-triggered average (5-ms stimulus bins, 20 lags), and its MI is as in\n# `cne.strf_mi`.\n\n# %%\nt0 = time.time()\nbins = dict(zip(SITE_IDS, pmap(cne.run_binsizes, IDX, [4000 + s for s in SITE_IDS])))\nprint(f\"bin sizes in {time.time() - t0:.0f} s\")\nrows = []\nfor site, v in bins.items():\n    for b, r in v.items():\n        rows.append({\"site\": site, \"bin\": b, \"n\": r[\"n\"], \"mean_size_a\": np.mean(r[\"sizes_a\"]) if r[\"sizes_a\"] else np.nan,\n                     \"mean_size_b\": np.mean(r[\"sizes_b\"]) if r[\"sizes_b\"] else np.nan})\nbt = pd.DataFrame(rows)\nprint(\"check: number of cNEs at 10 ms here and in the main detection agree in\",\n      sum(bt[(bt.site == s) & (bt.bin == 10)].n.iloc[0] == main[s][\"n\"] for s in SITE_IDS), \"of 16 recordings\")\n\n# %% [markdown]\n# ## fig5a-mi-peaks-10-15ms\n#\n# > The mutual information between cNE STRFs and the stimulus peaked at bin sizes of about 10 to\n# > 15 ms.\n\n# %% tags=claim:fig5a-mi-peaks-10-15ms\nrows = []\nfor b in cne.BIN_SIZES:\n    for p in cne.PROJECTIONS:\n        for er in (\"a\", \"b\"):\n            vals = np.concatenate([np.array(v[b][\"mi\"].get((p, er), [])) for v in bins.values()])\n            rows.append({\"bin\": b, \"projection\": p, \"events\": er, \"cnes\": len(vals),\n                         \"mean\": vals.mean(), \"median\": vals.median() if hasattr(vals, \"median\") else np.median(vals)})\nmi5 = pd.DataFrame(rows)\nfor (p, er), g in mi5.groupby([\"projection\", \"events\"]):\n    print(f\"projection {p}, events ({er}):\")\n    print(\"   \" + g[[\"bin\", \"cnes\", \"mean\", \"median\"]].round(3).to_string(index=False).replace(\"\\n\", \"\\n   \"))\n    print(f\"   peak of the mean at {g.loc[g['mean'].idxmax(), 'bin']} ms, of the median at {g.loc[g['median'].idxmax(), 'bin']} ms\")\n\n# %% [markdown]\n# RESULT_fig5a-mi-peaks-10-15ms\n\n# %% [markdown]\n# ## fig5b-number-decreases-with-bin\n#\n# > The number of detected cNEs decreased as the bin size increased.\n\n# %% tags=claim:fig5b-number-decreases-with-bin\nnb_ = bt.groupby(\"bin\").n.agg([\"mean\", \"std\", \"min\", \"max\"])\nprint(nb_.round(2).to_string())\nrho = stats.spearmanr(nb_.index, nb_[\"mean\"])\nprint(\"Spearman rho (mean number against bin size, 8 sizes) %.3f, p = %.3g; 2 ms %.2f against 50 ms %.2f\" % (\n    rho.correlation, rho.pvalue, nb_[\"mean\"].loc[2], nb_[\"mean\"].loc[50]))\nprint(\"recordings with fewer cNEs at 50 than at 2 ms:\", int((bt[bt.bin == 50].set_index(\"site\").n < bt[bt.bin == 2].set_index(\"site\").n).sum()), \"of 16\")\n\n# %% [markdown]\n# RESULT_fig5b-number-decreases-with-bin\n\n# %% [markdown]\n# ## fig5c-size-increases-with-bin\n#\n# > The mean number of member neurons per cNE increased as the bin size increased.\n\n# %% tags=claim:fig5c-size-increases-with-bin\nfor r in (\"a\", \"b\"):\n    ms_ = bt.groupby(\"bin\")[f\"mean_size_{r}\"].agg([\"mean\", \"std\", \"count\"])\n    rho = stats.spearmanr(ms_.index, ms_[\"mean\"])\n    print(f\"sign reading ({r}):\\n\" + ms_.round(2).to_string())\n    print(\"   Spearman rho %.3f, p = %.3g; 2 ms %.2f against 50 ms %.2f\" % (\n        rho.correlation, rho.pvalue, ms_[\"mean\"].loc[2], ms_[\"mean\"].loc[50]))\n\n# %% [markdown]\n# RESULT_fig5c-size-increases-with-bin\n\n# %% [markdown]\n# ## fig10b-ptd-higher and fig10c-strf-mi-higher\n#\n# Each cNE against each of its members (sign reading a). cNE events are the 10-ms bins of activity\n# above its 99.9th percentile threshold, at the bin centre: reading (a) every such bin, (b) the\n# peak bin of each run; under both projection readings. The larger of the event and spike trains\n# is subsampled to the smaller count. STRFs on 5-ms bins with 20 lags.\n\n# %%\nt0 = time.time()\ncvm = pd.DataFrame([r for rows in pmap(cne.run_cne_vs_members, IDX, [main[s] for s in SITE_IDS],\n                                       [5000 + s for s in SITE_IDS]) for r in rows])\nprint(f\"cNE against member STRFs in {time.time() - t0:.0f} s; pairs per reading:\")\nprint(cvm.groupby([\"projection\", \"events\"]).agg(pairs=(\"count\", \"size\"), median_count=(\"count\", \"median\"),\n                                                min_count=(\"count\", \"min\")).to_string())\nn_members = sum(len(m) for d in main.values() for m in cne.member_sets(d, \"a\"))\nprint(\"cNE and member pairs available:\", n_members, \"(paper: 703)\")\n\n# %% [markdown]\n# ## fig10b-ptd-higher\n#\n# > cNE STRFs had stronger excitatory and inhibitory subfields than those of their member neurons,\n# > with a higher peak-trough difference.\n\n# %% tags=claim:fig10b-ptd-higher\nfor (p, er), g in cvm.groupby([\"projection\", \"events\"]):\n    w = stats.wilcoxon(g.ptd_cne, g.ptd_unit)\n    print(f\"projection {p}, events ({er}): {len(g)} pairs; PTD cNE median {g.ptd_cne.median():.3f}, member \"\n          f\"{g.ptd_unit.median():.3f}; cNE higher in {100 * (g.ptd_cne > g.ptd_unit).mean():.1f}%; signed-rank p = {w.pvalue:.3g}\")\n    print(\"   by recording, % cNE higher:\", g.groupby(\"site\").apply(lambda x: round(100 * (x.ptd_cne > x.ptd_unit).mean())).to_dict())\n\n# %% [markdown]\n# RESULT_fig10b-ptd-higher\n\n# %% [markdown]\n# ## fig10c-strf-mi-higher\n#\n# > cNEs had higher mutual information between their STRFs and single events than member neurons\n# > had between their STRFs and single spikes.\n\n# %% tags=claim:fig10c-strf-mi-higher\nfor (p, er), g in cvm.groupby([\"projection\", \"events\"]):\n    w = stats.wilcoxon(g.mi_cne, g.mi_unit)\n    print(f\"projection {p}, events ({er}): {len(g)} pairs; MI cNE median {g.mi_cne.median():.3f} bits, member \"\n          f\"{g.mi_unit.median():.3f}; cNE higher in {100 * (g.mi_cne > g.mi_unit).mean():.1f}%; signed-rank p = {w.pvalue:.3g}\")\n    print(\"   by recording, % cNE higher:\", g.groupby(\"site\").apply(lambda x: round(100 * (x.mi_cne > x.mi_unit).mean())).to_dict())\n\n# %% [markdown]\n# RESULT_fig10c-strf-mi-higher\n\n# %% [markdown]\n# ## fig10s1-random-group-strfs\n#\n# > Multi-unit STRFs of cNE members had higher PTD and higher STRF MI than those of random groups of\n# > neurons of the same size, with uniqueness indices skewed towards 0.\n#\n# 100 random groups per cNE, not the paper's 500, to fit the time limit (a deviation); the UI is\n# the share of the 101 values at or above the cNE's.\n\n# %% tags=claim:fig10s1-random-group-strfs\nt0 = time.time()\nrg = pd.DataFrame([r for rows in pmap(cne.run_random_groups, IDX, [main[s] for s in SITE_IDS],\n                                      [6000 + s for s in SITE_IDS], [100] * len(IDX)) for r in rows])\nprint(f\"random groups in {time.time() - t0:.0f} s; cNEs {len(rg)}, excluded for under 200 spikes {int(rg.excluded.sum())}; \"\n      f\"groups per cNE {rg.n_groups.min()}-{rg.n_groups.max()}; levels used {sorted(rg.level.unique())}\")\nok = rg[~rg.excluded]\nfor m in (\"ptd\", \"mi\"):\n    w = stats.wilcoxon(ok[f\"{m}_cne\"], ok[f\"{m}_rand_median\"])\n    ks = stats.kstest(ok[f\"ui_{m}\"], \"uniform\")\n    print(f\"{m}: cNE median {ok[f'{m}_cne'].median():.3f}, random median {ok[f'{m}_rand_median'].median():.3f}; \"\n          f\"cNE higher in {100 * (ok[f'{m}_cne'] > ok[f'{m}_rand_median']).mean():.1f}% of {len(ok)}; signed-rank p = {w.pvalue:.3g}; \"\n          f\"UI median {ok[f'ui_{m}'].median():.3f}, KS against uniform D = {ks.statistic:.3f}, p = {ks.pvalue:.3g}\")\n\n# %% [markdown]\n# RESULT_fig10s1-random-group-strfs\n\n# %% [markdown]\n# ## Models (Figure 11C, D)\n#\n# 200 runs of each model per recording, as the Methods. Shuffled: each 10-ms train shifted\n# circularly. PR: each spike assigned to a random time bin of the same projection class (15 equal\n# classes over the full range of the unit's STRF projections), on (a) 10-ms or (b) 5-ms bins, the\n# latter summed to 10 ms. DG: binary 5-ms trains (counts above one set to one) fitted for means and\n# pairwise covariances (`cne.fit_dg`, a Python port of the method of CorBinian's\n# findLatentGaussian01, not the MATLAB code itself), sampled and summed to 10 ms. Membership in\n# model runs uses the recording's thresholds from the shuffles of the real data, as the shuffled IC\n# weights follow 1.5/sqrt(n) and do not depend on the data (printed above): an assumption, to fit\n# the time limit.\n\n# %%\nt0 = time.time()\nmodels = dict(zip(SITE_IDS, pmap(cne.run_models, IDX, [main[s] for s in SITE_IDS],\n                                 [7000 + s for s in SITE_IDS], [200] * len(IDX))))\nprint(f\"models in {time.time() - t0:.0f} s\")\nrows = []\nfor s in SITE_IDS:\n    real_size = np.mean([len(m) for m in cne.member_sets(main[s], \"a\")]) if main[s][\"n\"] else np.nan\n    row = {\"site\": s, \"real_n\": main[s][\"n\"], \"real_size\": real_size}\n    for m in cne.MODELS:\n        row[f\"{m}_n\"] = models[s][m][\"n\"].mean()\n        row[f\"{m}_size\"] = np.nanmean(models[s][m][\"size\"]) if np.isfinite(models[s][m][\"size\"]).any() else np.nan\n        row[f\"{m}_size0\"] = np.nan_to_num(models[s][m][\"size\"], nan=0.0).mean()\n        row[f\"{m}_runs_without_cne\"] = int((models[s][m][\"n\"] == 0).sum())\n    rows.append(row)\nmt = pd.DataFrame(rows)\nprint(mt.round(2).to_string(index=False))\n\n# %% [markdown]\n# ## fig11c-models-number\n#\n# > Surrogate spike trains from the 'shuffled' and 'preserved receptive field' (PR) models gave\n# > fewer cNEs than the real data, while the dichotomized Gaussian (DG) model gave more.\n\n# %% tags=claim:fig11c-models-number\nfor pr in (\"pr10\", \"pr5\"):\n    print(f\"PR reading {'(a) 10-ms' if pr == 'pr10' else '(b) 5-ms'} bins:\")\n    for m in (\"shuffled\", pr, \"dg\"):\n        t = stats.ttest_rel(mt[f\"{m}_n\"], mt.real_n)\n        print(f\"   {m}: mean {mt[f'{m}_n'].mean():.2f} against real {mt.real_n.mean():.2f}; t = {t.statistic:.2f}, \"\n              f\"p = {t.pvalue:.3g}, Bonferroni (x3) p = {min(1, 3 * t.pvalue):.3g}; recordings with model fewer: \"\n              f\"{int((mt[f'{m}_n'] < mt.real_n).sum())} of 16\")\n\n# %% [markdown]\n# RESULT_fig11c-models-number\n\n# %% [markdown]\n# ## fig11d-models-size\n#\n# > All three models, including the DG model, gave cNEs with fewer member neurons than the real\n# > data.\n\n# %% tags=claim:fig11d-models-size\nfor zero in (False, True):\n    print(\"runs without cNEs counted as size 0\" if zero else \"runs without cNEs left out\")\n    for pr in (\"pr10\", \"pr5\"):\n        for m in (\"shuffled\", pr, \"dg\"):\n            col = f\"{m}_size0\" if zero else f\"{m}_size\"\n            ok = mt[[col, \"real_size\"]].dropna()\n            t = stats.ttest_rel(ok[col], ok.real_size)\n            print(f\"   {m}: {len(ok)} recordings; mean {ok[col].mean():.2f} against real {ok.real_size.mean():.2f}; \"\n                  f\"t = {t.statistic:.2f}, Bonferroni (x3) p = {min(1, 3 * t.pvalue):.3g}\")\n\n# %% [markdown]\n# RESULT_fig11d-models-size\n\n# %% [markdown]\n# ## fig11s3b-pr-strf-similarity\n#\n# > The PR model preserved the neurons' STRFs (median STRF similarity with the real spike trains\n# > about 0.74), while the shuffled and DG models gave STRF similarities close to zero.\n#\n# Five runs of each model per recording; the real STRF is from the real train binned as the model\n# is (10 ms; 5 ms for PR reading b and for DG), spikes at bin centres.\n\n# %% tags=claim:fig11s3b-pr-strf-similarity\nt0 = time.time()\nsim = pmap(cne.run_strf_similarity, IDX, [8000 + s for s in SITE_IDS], [5] * len(IDX))\nprint(f\"STRF similarity in {time.time() - t0:.0f} s\")\nfor m in cne.MODELS:\n    v = np.concatenate([x[m] for x in sim])\n    print(f\"{m}: median {np.median(v):.3f} (IQR {np.percentile(v, 25):.3f} to {np.percentile(v, 75):.3f}) over {len(v)} unit runs\")\n\n# %% [markdown]\n# RESULT_fig11s3b-pr-strf-similarity\n\n# %% [markdown]\n# ## fig11ef-coincidence-ratios\n#\n# > Normalized to the real data, the coincidence ratios of groups of 2 and 3 cNE members were\n# > significantly below one for the 'repeat' data and the shuffled, PR and DG models.\n#\n# Reading (b) of the criterion, the only one the data set allows: groups from the cNEs of the 16\n# recordings (sign reading a), real and model CRs at 10 ms. 400 unique groups of 2 and of 3 members\n# of one cNE are drawn from all such groups. Each model is run 200 times per recording, not the\n# paper's 1000, to fit the time limit (a deviation); the median CR over runs is used. The 'repeat'\n# CR needs the repeated 10-min RN, which the data set does not hold.\n\n# %% tags=claim:fig11ef-coincidence-ratios\nrng_cr = np.random.default_rng(9000)\ngroups = {}\nfor size in (2, 3):\n    allg = sorted({(s, g) for s in SITE_IDS for m in cne.member_sets(main[s], \"a\") for g in itertools.combinations(sorted(m.tolist()), size)})\n    pick = rng_cr.choice(len(allg), min(400, len(allg)), replace=False)\n    groups[size] = [allg[k] for k in pick]\n    print(f\"groups of {size}: {len(allg)} available, {len(groups[size])} drawn, from {len({s for s, _ in groups[size]})} recordings\")\nby_site = {s: [g for size in (2, 3) for (ss, g) in groups[size] if ss == s] for s in SITE_IDS}\nt0 = time.time()\ncr = pd.DataFrame([r for rows in pmap(cne.run_cr, IDX, [by_site[s] for s in SITE_IDS],\n                                      [9000 + s for s in SITE_IDS], [200] * len(IDX)) for r in rows])\ncr[\"key\"] = list(zip(cr.site, cr.group))\nprint(f\"CRs in {time.time() - t0:.0f} s\")\nfor size in (2, 3):\n    g = cr[cr[\"size\"] == size]\n    keep = g.real > 0\n    print(f\"\\ngroups of {size}: {len(g)}; real CR median {g.real.median():.3f}; groups with real CR 0 left out: {(~keep).sum()}\")\n    g = g[keep]\n    for m in cne.MODELS:\n        t = stats.ttest_rel(g[m], g.real)\n        norm = g[m] / g.real\n        print(f\"   {m}: normalised CR median {norm.median():.3f}, mean {norm.mean():.3f}, below one in \"\n              f\"{100 * (norm < 1).mean():.1f}%; paired t = {t.statistic:.2f}, p = {t.pvalue:.3g}, \"\n              f\"Bonferroni x4 p = {min(1, 4 * t.pvalue):.3g}\")\n\n# %% [markdown]\n# RESULT_fig11ef-coincidence-ratios\n\n# %% [markdown]\n# ## Summary\n#\n# SUMMARY\n\n# %%\nprint(f\"notebook ran in {(time.time() - started) / 60:.1f} min; peak memory of the main process \"\n      f\"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb.py (file state is current in your context — no need to Read it back)
```

**Agent**

Notebook drafted. Running it on a 3-site subset with reduced iterations to debug.

**Agent calls Bash**

```bash
sed -i 's/^nonmem = .*$//' $TMPDIR/nb.py && . $TMPDIR/env/bin/activate && uv pip install -q nbconvert ipykernel nbformat 2>&1 | tail -1; 
sed -e 's/^IDX = list(range(len(cne.SITES)))/cne.SITES = [cne.SITES[k] for k in (0, 9, 13)]\nIDX = list(range(len(cne.SITES)))/' -e 's/\[200\] \* len(IDX)/[4] * len(IDX)/g' -e 's/\[100\] \* len(IDX)/[10] * len(IDX)/' -e 's/\[5\] \* len(IDX)/[1] * len(IDX)/' $TMPDIR/nb.py > $TMPDIR/dev.py && python $TMPDIR/py2nb.py $TMPDIR/dev.py $TMPDIR/dev.ipynb && cp cne.py $TMPDIR/ && cd $TMPDIR && date -u && time jupyter nbconvert --to notebook --execute dev.ipynb --output dev_out.ipynb --ExecutePreprocessor.timeout=3000 2>&1 | tail -5
```

```
Fri Nov 13 04:17:21 UTC 2026
[NbConvertApp] Converting notebook dev.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 186083 bytes to dev_out.ipynb

real	5m36.393s
user	11m38.851s
sys	0m17.958s
Shell cwd was reset to
```

**Agent**

Dev run completed without errors in 5.6 min. Reading its outputs.

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python -c "
import nbformat
nb=nbformat.read('dev_out.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain','')
        if t: print('-----',c.metadata.get('tags',''),'\n',t[:3000])
" | cut -c1-250
```

```
-----  
 data set ac-3, version unversioned, from https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-3/live

-----  
 2eb66e0691862b40dd09449ff5b7c45c  Codes.zip
3140d6178de9c044932901795a4cc817  Data.zip
6c076e1642771fd58091af266d0217ce  docs/crcns_ac-3_data_description.docx
96664dd364166ac7c9458882fb3d82be  docs/crcns_ac-3_data_description.pdf
a737203b6574bff9951cc42e76576994  filelist.txt
ce43beade196882598cecddff5520d7b  Stimulus.zip


-----  
 loaded 3 recordings and 2 stimuli in 25 s; peak memory 1.87 GB

----- ['sanity'] 
  site            file stim unit_stim  units tip_depth_um    fs  triggers trig_interval_ms  first_trig_s  stim_s  spikes   spike_s  in_stimulus depth_um lateral_um  sorted
    1   site1-rn1.mat  rn1       rn1     31          800 20000      1795    333.30-333.35          1.00   598.6   72240 0.0-621.1        0.959  250-650   -50,0,50    True
   10 site10-rn16.mat rn16      rn16     38          810 20000      1799    333.30-333.35          1.00   600.0  116119 0.0-622.8        0.961  160-660   -50,0,50    True
   14 site14-rn16.mat rn16      rn16     44          803 20000      1799    313.35-333.35          1.02   600.0   59335 0.0-622.7        0.963  153-653   -50,0,50    True
[... 388 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='nb.py'; s=open(p).read()
s=s.replace('''sh = []
for row in pairs.itertuples():
    xc = np.correlate(prof[row.site][row.a], prof[row.site][row.b], mode="full")
    sh.append(cne.pwc_measures(np.clip(xc, 0, None))[0])
pairs["strf_sharp"] = sh
pairs["ratio"] = pairs.sharp_50 / pairs.strf_sharp
print(f"STRFs and STRF PWCs in {time.time() - t0:.0f} s; pairs without a positive STRF PWC: {pairs.strf_sharp.isna().sum()}")
for lab, g in (("cNE pairs", pairs[pairs.cne_pair]), ("non-cNE pairs", pairs[~pairs.cne_pair])):
    ok = g.dropna(subset=["ratio"])
    print(f"{lab}: {len(ok)}; spike PWC sharper than STRF PWC in {100 * (ok.sharp_50 < ok.strf_sharp).mean():.1f}%; "
          f"median spike sharpness {ok.sharp_50.median():.1f} ms, STRF PWC {ok.strf_sharp.median():.1f} ms, "
          f"median ratio {ok.ratio.median():.3f}")
a = pairs[pairs.cne_pair].ratio.dropna(); b = pairs[~pairs.cne_pair].ratio.dropna()
print("ratio, cNE against non-cNE pairs: Mann-Whitney U p = %.3g (one-sided, cNE lower: %.3g)" % (
    stats.mannwhitneyu(a, b).pvalue, stats.mannwhitneyu(a, b, alternative="less").pvalue))
by = pairs.dropna(subset=["ratio"]).groupby(["site", "cne_pair"]).apply(lambda g: (g.sharp_50 < g.strf_sharp).mean()).unstack()
print("\\nfraction with spike PWC sharper, by recording:\\n", by.round(2).to_string())''','''sh_clip, sh_min = [], []
for row in pairs.itertuples():
    xc = np.correlate(prof[row.site][row.a], prof[row.site][row.b], mode="full")
    sh_clip.append(cne.pwc_measures(np.clip(xc, 0, None))[0])
    sh_min.append(cne.pwc_measures(xc - xc.min())[0])
pairs["strf_sharp_clip"], pairs["strf_sharp_min"] = sh_clip, sh_min
print(f"STRFs and STRF PWCs in {time.time() - t0:.0f} s; pairs without a positive STRF PWC: {pairs.strf_sharp_clip.isna().sum()}")
for reading, col in (("(i) negative values set to zero", "strf_sharp_clip"), ("(ii) minimum subtracted", "strf_sharp_min")):
    print(f"STRF PWC made non-negative by {reading}:")
    ratio = pairs.sharp_50 / pairs[col]
    for lab, sel in (("cNE pairs", pairs.cne_pair), ("non-cNE pairs", ~pairs.cne_pair)):
        ok = pairs[sel & ratio.notna()]
        print(f"   {lab}: {len(ok)}; spike PWC sharper than STRF PWC in {100 * (ok.sharp_50 < ok[col]).mean():.1f}%; "
              f"median spike sharpness {ok.sharp_50.median():.1f} ms, STRF PWC {ok[col].median():.1f} ms, "
              f"median ratio {ratio[sel].median():.3f}")
    a, b = ratio[pairs.cne_pair].dropna(), ratio[~pairs.cne_pair].dropna()
    print("   ratio, cNE against non-cNE pairs: Mann-Whitney U p = %.3g (one-sided, cNE lower: %.3g)" % (
        stats.mannwhitneyu(a, b).pvalue, stats.mannwhitneyu(a, b, alternative="less").pvalue))
    by = pairs.assign(sharper=pairs.sharp_50 < pairs[col]).groupby(["site", "cne_pair"]).sharper.mean().unstack()
    print("   fraction with spike PWC sharper, by recording (columns: cNE pair):\\n", by.round(2).T.to_string())''')
s=s.replace('''"of 16 recordings")''','''f"of {len(SITE_IDS)} recordings")''')
s=s.replace('''# the two profiles (lags -49 to 49 ms), its sharpness measured as for spike PWCs, with negative
# values set to zero, as a count histogram cannot be negative (a standard choice). The spike PWCs
# use the +-50 ms reading.''','''# the two profiles (lags -49 to 49 ms), its sharpness measured as for spike PWCs. A count
# histogram cannot be negative and a cross-correlation can, so the STRF PWC is made non-negative
# in one of two ways, both run: (i) negative values set to zero, (ii) its minimum subtracted. The
# spike PWCs use the +-50 ms reading.''')
open(p,'w').write(s)
EOF
grep -n "strf_sharp\b\|\"ratio\"" $TMPDIR/nb.py | head; mkdir -p entries/see-2018; cat > entries/see-2018/requirements.in <<'EOF'
aiohttp
fsspec
matplotlib
numpy
pandas
requests
scipy
EOF
cat > entries/see-2018/entry.yaml <<'EOF'
schema_version: 1
name: see-2018
type: reproduction
title: Coordinated neuronal ensembles in rat auditory cortex columns (See et al. 2018)
description: Tests the findings of See, Atencio, Sohal and Schreiner (2018) on CRCNS ac-3, which holds
  the 16 columnar recordings (655 units) made with the 10-min DMR and RN stimuli, and the
  stimuli. It detects coordinated neuronal ensembles (cNEs) by PCA and ICA and tests their number,
  size, membership, depth, stability, pairwise correlation functions, bin size dependence, STRFs,
  and comparison with surrogate models. The 5-s repeats, the 15 repeats of the 10-min RN and the
  64-channel recordings are not in the data set.
license: Apache-2.0
notebooks:
- path: reproduce_see_2018.ipynb
  title: Reproducing See et al. (2018) from CRCNS ac-3
  runtime_minutes: 35
helpers:
- cne.py
related:
- id: crcns:ac-3/unversioned
  relation: uses_data
- id: doi:10.7554/elife.35587
  relation: reproduces
EOF
python3 $TMPDIR/py2nb.py $TMPDIR/nb.py entries/see-2018/reproduce_see_2018.ipynb && date -u && python tools/entry.py lock entries/see-2018 2>&1 | tail -3
```

```
200:clock["ratio"] = clock.ptd_aligned / clock.ptd_shifted_30s
201:summary = clock.groupby("site").agg(units=("unit", "size"), median_ptd_ratio=("ratio", "median"),
202:                                    frac_ratio_above_1_5=("ratio", lambda r: (r > 1.5).mean()),
Fri Nov 13 04:23:42 UTC 2026
python: can't open file '/tmp/claude-1001/tools/entry.py': [Errno 2] No such file or directory
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cp $TMPDIR/entries/see-2018/requirements.in $TMPDIR/entries/see-2018/entry.yaml entries/see-2018/ && python3 $TMPDIR/py2nb.py $TMPDIR/nb.py entries/see-2018/reproduce_see_2018.ipynb && rm -rf $TMPDIR/entries && ls entries/see-2018 && python tools/entry.py lock entries/see-2018 2>&1 | tail -3 && cat entries/see-2018/entry.yaml | grep python
```

```
__pycache__
cne.py
entry.yaml
reproduce_see_2018.ipynb
requirements.in
wrote see-2018/requirements.lock.txt (Python 3.13, with hashes)
python: "3.13"
```

**Agent**

Locked for Python 3.13. Starting the full run (estimate about 35 min).

**Agent calls Bash**

```bash
rm -rf entries/see-2018/__pycache__; date -u; time python tools/entry.py all entries/see-2018 2>&1 | tail -15; date -u
```

```
Fri Nov 13 04:23:51 UTC 2026
Installed kernelspec registry-see-2018 in executed/see-2018/.venv/share/jupyter/kernels/registry-see-2018
0 error(s)
pass  reproduce_see_2018.ipynb  (2046 s)

real	34m13.819s
user	113m57.963s
sys	1m38.393s
Fri Nov 13 04:58:04 UTC 2026
```

**Agent**

Full run passed in 34 min. Reading the results.

**Agent calls Bash**

```bash
ls executed/see-2018/; . $TMPDIR/env/bin/activate && python -c "
import nbformat
nb=nbformat.read('executed/see-2018/reproduce_see_2018.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain','')
        if t and 'Figure size' not in t: print('-----',c.metadata.get('tags',''),'\n',t[:6000])
" | cut -c1-260 > $TMPDIR/out1.txt; wc -l $TMPDIR/out1.txt; head -150 $TMPDIR/out1.txt
```

```
reproduce_see_2018.ipynb
result.json
535 /tmp/claude-1001/out1.txt
-----  
 data set ac-3, version unversioned, from https://crcnsarchive.s3-us-west-2.amazonaws.com/ac-3/live

-----  
 2eb66e0691862b40dd09449ff5b7c45c  Codes.zip
3140d6178de9c044932901795a4cc817  Data.zip
6c076e1642771fd58091af266d0217ce  docs/crcns_ac-3_data_description.docx
96664dd364166ac7c9458882fb3d82be  docs/crcns_ac-3_data_description.pdf
a737203b6574bff9951cc42e76576994  filelist.txt
ce43beade196882598cecddff5520d7b  Stimulus.zip


-----  
 loaded 16 recordings and 2 stimuli in 25 s; peak memory 1.93 GB

----- ['sanity'] 
  site            file stim unit_stim  units tip_depth_um    fs  triggers trig_interval_ms  first_trig_s  stim_s  spikes   spike_s  in_stimulus depth_um lateral_um  sorted
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,535p $TMPDIR/out1.txt
```

```
----- ['claim:fig7d-pairs-within-200um'] 
 once per cNE, depth_diff: 88.5% of 1025 pairs under 200 um (range 0 to 500 um)
once per cNE, euclid: 88.5% of 1025 pairs under 200 um (range 0 to 510 um)
each pair once, depth_diff: 88.3% of 1012 pairs under 200 um (range 0 to 500 um)
each pair once, euclid: 88.3% of 1012 pairs under 200 um (range 0 to 510 um)

by recording, depth difference, once per cNE:
site
1     100.0
2      98.8
3      91.1
4      95.4
5     100.0
6     100.0
7      98.0
8      88.3
9      77.2
10     92.2
11     70.3
12     95.2
[... 364 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; grep -n -i "data availab\|deposited\|crcns\|10.6080\|available at\|github" paper/10.7554-elife.35587.txt | cut -c1-400; . $TMPDIR/env/bin/activate && cd entries/see-2018 && python -W ignore -c "
import numpy as np,cne
S=cne.load_sites()
for s in S:
  for k,u in enumerate(s['units']):
    d=np.diff(u['spikes_ms'])
    if (d<0).any(): print('site',s['site'],'unit',k,'inversions',(d<0).sum(),'of',len(d),'min diff ms %.2f'%d.min(), 'at index',np.flatnonzero(d<0)[:5], 'dup times', (d==0).sum())
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat > $TMPDIR/t4.py <<'EOF'
import os
for v in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS"): os.environ[v]="1"
import multiprocessing as mp, numpy as np, pandas as pd, warnings
from concurrent.futures import ProcessPoolExecutor
from scipy import stats
import cne
warnings.filterwarnings("ignore")
cne.SITES = cne.load_sites()
for s in cne.SITES: cne.prepare(s)
for name in ("rn1","rn16"):
    raw = cne.load_stimulus(name); cne.STIM[(name,5)] = cne.downsample(raw,5); del raw
IDX=list(range(16)); SITE_IDS=[s["site"] for s in cne.SITES]
def pmap(fn,*a):
    with ProcessPoolExecutor(4, mp_context=mp.get_context("fork")) as ex: return list(ex.map(fn,*a))
main = dict(zip(SITE_IDS, pmap(cne.run_main, IDX, [1000+s for s in SITE_IDS])))
rg = pd.DataFrame([r for rows in pmap(cne.run_random_groups, IDX, [main[s] for s in SITE_IDS], [6000+s for s in SITE_IDS], [100]*16) for r in rows])
print(rg[rg.n_groups<100][["site","cne","size","n_groups","level","count"]])
for s in rg[rg.n_groups<100].site.unique(): print(s, len(cne.SITES[SITE_IDS.index(s)]["units"]), [len(m) for m in cne.member_sets(main[s],"a")])
ok = rg[~rg.excluded & (rg.n_groups > 0)]
for m in ("ptd","mi"):
    w = stats.wilcoxon(ok[f"{m}_cne"], ok[f"{m}_rand_median"]); ks = stats.kstest(ok[f"ui_{m}"], "uniform")
    print(m, len(ok), ok[f"{m}_cne"].median(), ok[f"{m}_rand_median"].median(), (ok[f"{m}_cne"] > ok[f"{m}_rand_median"]).mean(), w.pvalue, ok[f"ui_{m}"].median(), ks.statistic, ks.pvalue)
EOF
. $TMPDIR/env/bin/activate && PYTHONPATH=. python $TMPDIR/t4.py
```

```
site  cne  size  n_groups  level  count
14     3    0     2         0      2    608
30     5    1     2         0      2  24079
31     5    2     2         0      2    867
33     6    1     2         0      2   1092
52     9    0     2         0      2  13415
56     9    4     2         0      2  25065
60    10    1     2         0      2   1255
81    13    1     2         0      2   4580
87    14    2     2         0      2   2573
92    15    1     2         0      2   3126
3 37 [2, 6, 5, 4, 7, 3]
5 16 [3, 2, 2]
6 25 [4, 2, 1, 3]
9 41 [2, 5, 7, 6, 2, 3, 4]
10 38 [6, 2, 5, 5, 3, 4, 3, 5, 4]
13 40 [6, 2, 4, 3, 5]
14 44 [4, 7, 2, 7, 6, 4]
15 29 [4, 2, 4, 3, 3]
ptd 93 3.1520156860351562 2.694771647453308 0.5698924731182796 0.002964447397939833 0.31683168316831684 0.24677951666134357 1.7873149167039685e-05
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='cne.py'; s=open(p).read()
old=s[s.index('def random_groups('):s.index('def run_random_groups(')]
new='''def random_groups(members: np.ndarray, others: list[np.ndarray], n_units: int, n_groups: int,
                  rng: np.random.Generator, max_draws: int = 20000) -> tuple[list[tuple], int]:
    """Random groups of the cNE's size (Materials and methods, MI comparisons): `level` members of the
    cNE and the rest from non-members, with at most `level` units from any other cNE; the level is
    raised until `n_groups` unique groups are found within `max_draws` draws (a standard choice).
    When no level reaches `n_groups` (a 2-unit cNE has too few possible groups), the largest set
    found is used, at the lowest level that gave it (a standard choice; the Methods do not say)."""
    size = len(members)
    non = np.setdiff1d(np.arange(n_units), members)
    best, best_level = [], 1
    for level in range(1, size + 1):
        if size - level > len(non):
            continue
        found = set()
        for _ in range(max_draws):
            g = tuple(sorted(np.r_[rng.choice(members, level, replace=False),
                                   rng.choice(non, size - level, replace=False)].tolist()))
            if g == tuple(sorted(members.tolist())):
                continue
            if any(len(np.intersect1d(g, o)) > level for o in others):
                continue
            found.add(g)
            if len(found) >= n_groups:
                return sorted(found), level
        if len(found) > len(best):
            best, best_level = sorted(found), level
    return best, best_level


'''
s=s.replace(old,new)
open(p,'w').write(s)
EOF
. $TMPDIR/env/bin/activate && PYTHONPATH=. python $TMPDIR/t4.py
```

```
site  cne  size  n_groups  level  count
14     3    0     2         0      2    608
30     5    1     2         0      2  24079
31     5    2     2         0      2    867
33     6    1     2         0      2   1092
52     9    0     2         0      2  13415
56     9    4     2         0      2  25065
60    10    1     2         0      2   1255
81    13    1     2         0      2   4580
87    14    2     2         0      2   2573
92    15    1     2         0      2   3126
3 37 [2, 6, 5, 4, 7, 3]
5 16 [3, 2, 2]
6 25 [4, 2, 1, 3]
9 41 [2, 5, 7, 6, 2, 3, 4]
10 38 [6, 2, 5, 5, 3, 4, 3, 5, 4]
13 40 [6, 2, 4, 3, 5]
14 44 [4, 7, 2, 7, 6, 4]
15 29 [4, 2, 4, 3, 3]
ptd 93 3.1520156860351562 2.694771647453308 0.5698924731182796 0.002964447397939833 0.31683168316831684 0.24677951666134357 1.7873149167039685e-05
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python -W ignore -c "
import numpy as np,cne
S=cne.load_sites(); s=S[2]; cne.prepare(s)
d=cne.detect(cne.binned(s,10),1003,activity_null=False)
sets=cne.member_sets(d,'a'); print([list(m) for m in sets])
m=sets[0]; others=[x for k,x in enumerate(sets) if k!=0]
g,l=cne.random_groups(m,others,37,100,np.random.default_rng(1)); print(len(g),l,g[:3])
"
```

```
[[np.int64(0), np.int64(3)], [np.int64(1), np.int64(4), np.int64(5), np.int64(11), np.int64(12), np.int64(15)], [np.int64(26), np.int64(29), np.int64(32), np.int64(34), np.int64(36)], [np.int64(8), np.int64(17), np.int64(23), np.int64(30)], [np.int64(9), np.int64(10), np.int64(11), np.int64(15), np.int64(17), np.int64(18), np.int64(25)], [np.int64(27), np.int64(33), np.int64(35)]]
70 1 [(0, 1), (0, 2), (0, 4)]
```

**Agent calls Bash**

```bash
grep -c best_level cne.py; . $TMPDIR/env/bin/activate && PYTHONPATH=. python $TMPDIR/t4.py 2>&1 | tail -8
```

```
3
6 25 [4, 2, 1, 3]
9 41 [2, 5, 7, 6, 2, 3, 4]
10 38 [6, 2, 5, 5, 3, 4, 3, 5, 4]
13 40 [6, 2, 4, 3, 5]
14 44 [4, 7, 2, 7, 6, 4]
15 29 [4, 2, 4, 3, 3]
ptd 93 3.1520156860351562 2.694771647453308 0.5698924731182796 0.002964447397939833 0.31683168316831684 0.24677951666134357 1.7873149167039685e-05
mi 93 0.2635988591189626 0.20772049116462438 0.6666666666666666 5.172167307016384e-06 0.26732673267326734 0.30054295752155863 6.02011828403219e-08
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && PYTHONPATH=. python $TMPDIR/t4.py 2>&1 | head -14; python -c "import cne;print(cne.__file__)"
```

```
site  cne  size  n_groups  level  count
14     3    0     2         0      2    608
30     5    1     2         0      2  24079
31     5    2     2         0      2    867
33     6    1     2         0      2   1092
52     9    0     2         0      2  13415
56     9    4     2         0      2  25065
60    10    1     2         0      2   1255
81    13    1     2         0      2   4580
87    14    2     2         0      2   2573
92    15    1     2         0      2   3126
3 37 [2, 6, 5, 4, 7, 3]
5 16 [3, 2, 2]
6 25 [4, 2, 1, 3]
entries/see-2018/cne.py
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python -W ignore -c "
import numpy as np,cne,inspect
cne.SITES=cne.load_sites(); s=cne.SITES[2]; cne.prepare(s)
raw=cne.load_stimulus('rn1'); cne.STIM[('rn1',5)]=cne.downsample(raw,5); del raw
d=cne.run_main(2,1003)
r=cne.run_random_groups(2,d,6003,100); print([(x['cne'],x['size'],x['n_groups'],x['level']) for x in r])
print(inspect.getsource(cne.run_random_groups)[:1500])
"
```

```
[(0, 2, 70, 1), (1, 6, 100, 1), (2, 5, 100, 1), (3, 4, 100, 1), (4, 7, 100, 1), (5, 3, 100, 1)]
def run_random_groups(i: int, det: dict, seed: int, n_groups: int = 500) -> list[dict]:
    """Figure 10-figure supplement 1: PTD and STRF MI of the summed spikes of each cNE's members and
    of random groups, all subsampled to the fewest spikes; sets under 200 spikes left out."""
    site = SITES[i]
    stim = STIM[(site["stim"], STRF_BIN_MS)]
    rng = np.random.default_rng(seed)
    if det["n"] == 0:
        return []
    sets = member_sets(det, "a")
    spikes = [u["stim_ms"][np.isfinite(u["stim_ms"])] for u in site["units"]]
    rows = []
    for j, members in enumerate(sets):
        if len(members) < 2:
            continue
        others = [s for k, s in enumerate(sets) if k != j]
        groups, level = random_groups(members, others, len(spikes), n_groups, rng)
        trains = [np.concatenate([spikes[m] for m in members])] + \
                 [np.concatenate([spikes[m] for m in g]) for g in groups]
        k = min(len(t) for t in trains)
[... 11 more lines not kept]
```

**Agent**

The script was importing an old copy of `cne.py` left in the temp directory. Removing it and rerunning.

**Agent calls Bash**

```bash
rm -f $TMPDIR/cne.py; . $TMPDIR/env/bin/activate && PYTHONPATH=. python $TMPDIR/t4.py 2>&1; date -u
```

```
site  cne  size  n_groups  level  count
14     3    0     2        70      1    347
30     5    1     2        28      1  11398
31     5    2     2        28      1    867
33     6    1     2        46      1    717
52     9    0     2        78      1   6215
56     9    4     2        78      1  12302
60    10    1     2        72      1    217
81    13    1     2        76      1   1102
87    14    2     2        84      1    566
92    15    1     2        54      1   1035
3 37 [2, 6, 5, 4, 7, 3]
5 16 [3, 2, 2]
6 25 [4, 2, 1, 3]
9 41 [2, 5, 7, 6, 2, 3, 4]
10 38 [6, 2, 5, 5, 3, 4, 3, 5, 4]
13 40 [6, 2, 4, 3, 5]
14 44 [4, 7, 2, 7, 6, 4]
15 29 [4, 2, 4, 3, 3]
ptd 103 3.2091376781463623 2.7575244903564453 0.5825242718446602 0.0007024624190302647 0.3465346534653465 0.25012015764683265 3.650440449985693e-06
[... 2 more lines not kept]
```

**Agent**

Fixed: all 103 cNEs now get random groups (the paper also reports 103), and both signed-rank tests give p < 0.001. Writing the conclusions into the notebook now (05:19), then the final run.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='nb.py'; s=open(p).read()
R = {}
R["CLOCK_CONCLUSION"] = """In all 16 recordings the STRFs are stronger with the spikes on the stimulus clock than with the
same spikes shifted by 30 s (median PTD ratio 1.03 to 2.79 per recording, 1.40 over 655 units).
In the aligned STRFs the peak falls at a median lag of 12.5 to 32.5 ms per recording, within or
near the 10 to 30 ms latency of AI. In the shifted STRFs it falls at 42.5 to 62.5 ms, the middle
of the window, where a peak with no structure lands. For the 289 units with a ratio above 1.5 the
median peak lag is 12.5 ms. The triggers and spike times therefore share a clock, and the mapping
of 667 stimulus columns to each trigger interval is consistent with the data. The check is weak
in sites 9, 15 and 13 (median ratios 1.03 to 1.13; 2 to 17% of units above 1.5), where few units
have strong STRFs."""
R["RESULT_fig7-totals"] = """**Result: reproduced.** The data set holds 16 recordings and 655 units, the paper's counts. The
detection finds 104 cNEs, 6.50 +/- 1.97 per recording (range 3 to 10), against the paper's 104 and
6.5 +/- 2.0."""
R["RESULT_fig4-example-nine-cnes"] = """**Result: reproduced.** Site 10 is the only recording with 38 units. The detection finds 9 cNEs
with 2 to 6 members under sign reading (a), the paper's 9 and 2 to 6, and the same with five
other seeds. Under reading (b) the sizes are 2 to 5, within the tolerance of one."""
R["RESULT_fig7a-number-vs-neurons"] = """**Result: reproduced.** The number of cNEs rises with the number of units: slope 0.140, R2 0.745,
F-test p = 1.7e-05 (paper R2 0.74, p = 1.68e-5). The fraction is 16.1% (a), 14.0% (b) or 15.9% (c),
all within 15 +/- 1.5%."""
R["RESULT_fig7b-size-vs-neurons"] = """**Result: not reproduced.** Mean cNE size rises with the number of units (slope 0.078,
p = 2.3e-06). But the cNEs are smaller than the paper's: 4.58 +/- 1.84 members pooled and 4.34
per recording, against 7.4 +/- 2.5. They are 10.7% of the units, against 17%. The fit is also
tighter, with R2 0.807 against 0.33. Only the positive slope with p < 0.05 holds. Sign reading (b)
gives the same picture (mean 4.73, R2 0.745)."""
R["RESULT_fig7-negative-weights"] = """**Result: not reproduced.** Under sign reading (a), 24 of 104 cNEs (23.1%) have a member below
the lower threshold, against the paper's 9. 90.8% of member weights are positive, which passes the
90% reading of "vast majority". Under reading (b), 65 cNEs have one."""
R["RESULT_fig7c-membership"] = """**Result: not reproduced.** Under sign reading (a), 59.2% of the 655 units belong to one cNE,
34.4% to none and 6.4% to more than one. The paper has 68%, 9% and 23%. Reading (b) gives 61.2%,
32.1% and 6.7%. None of the three values is within tolerance under either reading. Fewer units are
members than in the paper, which fits the smaller cNEs of fig7b."""
R["RESULT_fig7d-pairs-within-200um"] = """**Result: reproduced.** 88.5% of the 1025 member pairs (88.3% of 1012 unique pairs) are less
than 200 um apart, by depth difference and by Euclidean distance alike. This is within 82 +/- 8.2%.
Per recording it ranges from 61.4% to 100%."""
R["RESULT_fig7e-no-depth-bias"] = """**Result: reproduced (resting on the choice of test).** The 430 members and all 655 units have
median depths of 460 and 450 um. Neither test finds a difference: KS p = 0.999, Mann-Whitney
p = 0.474. Members against non-members also show none (KS p = 0.498, MWU p = 0.116). cNE depths
run from 200 to 662 um, against 150 to 662 um for the units. The paper names no test, so the
outcome rests on these."""
R["RESULT_fig7f-span-200um"] = """**Result: not reproduced.** 80.8% of the 104 cNEs span 200 um or less (78.8% under sign reading
(b)), above the 63 to 77% the tolerance allows. Two cNEs span more than 400 um, up to 500 um. The
cNEs are more confined than the paper's, as expected of smaller cNEs."""
R["RESULT_fig2bd-pwc-measures-covary"] = """**Result: not reproduced.** Sharpness and peak delay both decrease with the correlation
coefficient. The R2 values are 0.13 and 0.11 (+-50 ms, linear), 0.15 and 0.17 (log), 0.17 and 0.09
(+-100 ms, linear) and 0.22 and 0.23 (log). All are well below 0.5 +/- 0.05."""
R["RESULT_fig2eg-distance-weak"] = """**Result: not reproduced.** Distance explains even less of the variance than the paper says.
The R2 values are 0.006 to 0.060 for sharpness and delay and 0.032 to 0.037 for the correlation
coefficient, under both distances and both lag ranges. All fall below the 0.09 to 0.33 interval.
The statement's "only" holds, but its range does not."""
R["RESULT_fig6j-sharpness-cne-pairs"] = """**Result: partially reproduced.** With +-50 ms lags, cNE pairs have sharper PWCs at p < 0.001 in
14 of 16 recordings. The two exceptions have few cNE pairs: site 5 (5 pairs, p = 0.023) and site 6
(10 pairs, p = 0.054); cNE pairs still have the lower median sharpness in both. With +-100 ms it
holds in 12. There are 1012 cNE pairs and 13162 non-cNE pairs, against the paper's 3087 and 8838:
with smaller cNEs there are fewer member pairs."""
R["RESULT_fig6-member-pwc-sharpness-delay"] = """**Result: not reproduced.** For the 1012 cNE pairs (+-50 ms) the median sharpness is 12.0 ms and
the mean 12.42 +/- 5.59 ms, against about 2 ms and 3.39 +/- 1.21 ms. The mean absolute peak delay of
1.64 ms is within 0.76 +/- 1.74 ms. Per recording the values are 12.2, 12.5 and 1.49 ms. With
+-100 ms the sharpness is larger still (33 ms). In 80% of cNE pairs the PWC peaks at 0 or 1 ms. The
large sharpness comes from the flat base of the histogram, which the half-count width includes."""
R["RESULT_fig6c-spike-pwc-narrower-than-strf-pwc"] = """**Result: reproduced, resting on an assumption.** The outcome depends on how the STRF PWC is made
non-negative. With its minimum subtracted (ii), the spike PWC is sharper than the STRF PWC in 63.2%
of cNE pairs and 43.8% of non-cNE pairs. The spike/STRF sharpness ratio is lower for cNE pairs
(median 0.778 against 1.062, Mann-Whitney p = 4.3e-53). With negative values set to zero (i), the
STRF PWCs have a median sharpness of 4.0 ms, so spike PWCs are sharper in only 6.5% of cNE pairs,
although the ratio is still lower for cNE pairs (p = 6.3e-59). Reading (ii) is adopted, as the
Results describe "PWCs between the temporal profiles of STRFs" as "broad"; under (i) they are
narrower than the spike PWCs."""
R["RESULT_fig4s2-interleaved-halves-stable"] = """**Result: reproduced.** 192 of 205 ICs of the two interleaved halves (93.7%) have a match above the
99th percentile of the shuffled null, under both null readings (thresholds 0.32 to 0.62). The
paper has about 96%. Every recording matches at least 6 of 9 of its ICs (site 16: 13 of 16)."""
R["RESULT_fig4s3-train-test-83pct"] = """**Result: not reproduced.** There are 102 training cNEs, the paper's number. But 100 of them
(98.0%, quadratic projection) or 101 (99.0%, linear) match a test cNE above the 95th percentile of
the non-matched correlations, against about 83% (74.7 to 91.3% allowed). With the null taken as
every non-row-maximum value, the figure is 95.1% or 99.0%. The training cNEs predict the test
activity better than the paper reports. The criterion counts a correct count with an out-of-range
percentage as not reproduced."""
R["RESULT_fig5a-mi-peaks-10-15ms"] = """**Result: not reproduced.** No reading puts the largest MI at 10 or 15 ms. With the 5000 largest
1-ms samples as events (a), MI rises with bin size and peaks at 35 ms under both projections and
both summaries (mean 0.698 linear, 0.730 quadratic). It is nearly flat from 15 ms on (0.668 to 0.698
linear). With the 5000 largest peaks (b), MI is highest at 2 ms and falls with bin size. The STRF
resolution (5 ms, 20 lags) and the MI bins are this attempt's choices."""
R["RESULT_fig5b-number-decreases-with-bin"] = """**Result: reproduced.** The mean number of cNEs falls from 11.06 at 2 ms to 3.75 at 50 ms,
monotonically over the eight sizes (Spearman rho = -1.0). Every one of the 16 recordings has fewer
at 50 ms than at 2 ms."""
R["RESULT_fig5c-size-increases-with-bin"] = """**Result: reproduced.** The mean cNE size rises from 3.88 at 2 ms to 5.11 at 50 ms (Spearman
rho = 0.952, p = 0.00026) under sign reading (a). Under (b) it rises from 3.91 to 5.51
(rho = 1.0). The rise is not strictly monotonic under (a), with small dips at 8 and 20 ms."""
R["RESULT_fig10b-ptd-higher"] = """**Result: reproduced.** cNE STRFs have a higher PTD than their members' under all four readings.
The signed-rank p is 8.0e-12 (linear, events a), 3.8e-09 (linear, b), 5.6e-04 (quadratic, a) and
2.4e-05 (quadratic, b). The cNE is higher in 54 to 62% of the 476 pairs; the paper has 703 pairs,
as its cNEs are larger."""
R["RESULT_fig10c-strf-mi-higher"] = """**Result: not reproduced.** cNE STRF MI is higher than the members' in 53 to 56% of the 476 pairs
under every reading, but no reading reaches p < 0.001. The signed-rank p is 0.0015 (linear, a),
0.0076 (linear, b), 0.049 (quadratic, a) and 0.185 (quadratic, b). The paper has p = 1.6e-59 over
703 pairs."""
R["RESULT_fig10s1-random-group-strfs"] = """FIG10S1"""
R["RESULT_fig11c-models-number"] = """**Result: reproduced.** Over the 16 recordings (real mean 6.50 cNEs), the shuffled model gives
0.23 cNEs and PR 1.41 (10-ms bins) or 1.52 (5-ms bins), fewer in every recording. DG gives 8.00,
more in 15 of 16. All three Bonferroni-corrected paired t-tests give p < 0.001 (4.6e-09, 3.1e-08 or
4.6e-08, and 1.5e-04), under both PR readings."""
R["RESULT_fig11d-models-size"] = """**Result: not reproduced.** The model cNEs are not smaller than the real ones (mean 4.34 members).
With runs without cNEs left out, the shuffled model gives 4.95 (larger, corrected p = 0.055), PR
3.80 or 3.84 (p = 0.20 or 0.24) and DG 4.30 (p = 1). With such runs counted as size 0, the shuffled
model is smaller (1.11, p = 1.4e-07), but PR (3.74 or 3.83) and DG are not. At most one of the
three comparisons holds."""
R["RESULT_fig11s3b-pr-strf-similarity"] = """**Result: reproduced, resting on an assumption.** The median STRF similarity is 0.737 for PR on
5-ms bins and 0.645 for PR on 10-ms bins, against 0.74 +/- 0.074; it is 0.022 for both the shuffled
and DG models, below 0.1. The 10-ms reading falls just outside the tolerance. The 5-ms reading is
adopted, as it is the resolution of the STRFs (an assumption of this attempt) that the PR model
shuffles on, and it is the DG model's bin in the Methods."""
R["RESULT_fig11ef-coincidence-ratios"] = """**Result: partially reproduced.** For the 400 groups of 2, the normalised CRs have medians of
0.159 (shuffled), 0.215 or 0.223 (PR) and 0.776 (DG). For the 372 groups of 3 with a real CR above
zero (28 left out), they are 0.000, 0.000 and 0.730. Every comparison is below one with
Bonferroni p < 1e-35. The 'repeat' comparison cannot be run, as the data set does not hold the
repeated stimulus; by the criterion, the claim is partially reproduced."""
for k,v in R.items():
    assert k in s, k
    s=s.replace("# "+k, "\n".join("# "+l for l in v.split("\n")) if k.startswith("RESULT") or k=="CLOCK_CONCLUSION" else v)
open(p,'w').write(s)
EOF
grep -n "RESULT_\|FIG10S1\|SUMMARY" $TMPDIR/nb.py
```

```
940:# FIG10S1
1090:# SUMMARY
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p='nb.py'; s=open(p).read()
s=s.replace("""# **Result: reproduced.** 192 of 205 ICs of the two interleaved halves (93.7%) have a match above the
# 99th percentile of the shuffled null, under both null readings (thresholds 0.32 to 0.62). The
# paper has about 96%. Every recording matches at least 6 of 9 of its ICs (site 16: 13 of 16).""","""# **Result: reproduced.** 192 of 205 ICs of the two interleaved halves (93.7%) have a match above the
# 99th percentile of the shuffled null, under both null readings (thresholds 0.32 to 0.62). The
# paper has about 96%. Per recording the share runs from 81% (site 16, 13 of 16) to 100%.""")
s=s.replace("# FIG10S1","""# **Result: reproduced.** The test covers 103 cNEs, the paper's 103, with 100 random groups each;
# the ten 2-member cNEs allow only 28 to 84. The summed spikes of cNE members give a higher PTD than
# the median random group (3.21 against 2.76; signed-rank p = 7.0e-04) and a higher STRF MI (0.275
# against 0.209 bits; p = 3.1e-06). The UIs have medians of 0.347 (PTD) and 0.267 (MI) and differ
# from uniform (KS p = 3.7e-06 and 3.1e-09). The PTD comparison is near the 0.001 threshold, and
# it uses 100 random groups where the paper uses 500.""")
s=s.replace("""ok = rg[~rg.excluded]
for m in ("ptd", "mi"):""","""print(rg[rg.n_groups < 100][["site", "cne", "size", "n_groups", "level", "count"]].to_string(index=False))
ok = rg[~rg.excluded & (rg.n_groups > 0)]
for m in ("ptd", "mi"):""")
s=s.replace("""info = pd.DataFrame(rows)
print(info.to_string(index=False))""","""info = pd.DataFrame(rows)
print(info.to_string(index=False))
for s in cne.SITES:
    for k, u in enumerate(s["units"]):
        d = np.diff(u["spikes_ms"])
        if (d < 0).any():
            print(f"site {s['site']} unit {k}: {(d < 0).sum()} decreasing steps of {len(d)} (largest {-d.min():.2f} ms), "
                  f"{(d == 0).sum()} repeated times")""")
s=s.replace("""# envelope runs from -20 to 20 dB, the 40 dB modulation depth of the Methods, over 64 carriers
# from 500 Hz to 40 kHz. Spike times are in ms and sorted.""","""# envelope runs from -20 to 20 dB, the 40 dB modulation depth of the Methods, over 64 carriers
# from 500 Hz to 40 kHz. Spike times are in ms, and sorted except in two units (site 4 unit 17 and
# site 7 unit 21), whose few steps back are under 0.1 ms and which also repeat spike times; no
# measure here depends on the order.""")
summary = """# | Claim | Outcome |
# |---|---|
# | fig2bd-pwc-measures-covary | not reproduced (R2 0.09 to 0.23, against 0.5) |
# | fig2eg-distance-weak | not reproduced (R2 0.006 to 0.06, below 10 to 30%) |
# | fig4-example-nine-cnes | reproduced (9 cNEs, 2 to 6 members) |
# | fig4s2-interleaved-halves-stable | reproduced (93.7%) |
# | fig4s3-train-test-83pct | not reproduced (102 training cNEs, but 98% matched) |
# | fig5a-mi-peaks-10-15ms | not reproduced (peak at 35 ms or 2 ms) |
# | fig5b-number-decreases-with-bin | reproduced |
# | fig5c-size-increases-with-bin | reproduced |
# | fig6c-spike-pwc-narrower-than-strf-pwc | reproduced, resting on an assumption |
# | fig6j-sharpness-cne-pairs | partially reproduced (14 of 16 recordings) |
# | fig6-member-pwc-sharpness-delay | not reproduced (median sharpness 12 ms, against 2) |
# | fig7-totals | reproduced (16, 655, 104, 6.5 +/- 2.0) |
# | fig7a-number-vs-neurons | reproduced (R2 0.745) |
# | fig7b-size-vs-neurons | not reproduced (mean size 4.6, against 7.4) |
# | fig7-negative-weights | not reproduced (24 cNEs, against 9) |
# | fig7c-membership | not reproduced (59/34/6%, against 68/9/23%) |
# | fig7d-pairs-within-200um | reproduced (88.5%) |
# | fig7e-no-depth-bias | reproduced, resting on an assumption (the test) |
# | fig7f-span-200um | not reproduced (80.8%, against 70%) |
# | fig8-spont-evoked-72pct | blocked, data missing |
# | fig9c-cne-events-more-mi, fig9s1, fig9s2 | blocked, data missing |
# | fig10b-ptd-higher | reproduced |
# | fig10c-strf-mi-higher | not reproduced (p = 0.0015 at best) |
# | fig10s1-random-group-strfs | reproduced |
# | fig11ab-real-vs-surrogate | blocked, data missing |
# | fig11c-models-number | reproduced |
# | fig11d-models-size | not reproduced |
# | fig11ef-coincidence-ratios | partially reproduced (models only) |
# | fig11s3b-pr-strf-similarity | reproduced, resting on an assumption |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# How the analysis differs from the paper's:
#
# - The detection follows the Methods, but the Marcenko-Pastur bound, the fastICA settings, IC sign,
#   the activity projection and the event definition are this attempt's readings (claims file and
#   `cne.py`). The number of cNEs matches the paper in total (104) and in its dependence on the
#   number of units. The cNEs are smaller (4.6 against 7.4 members), so the membership threshold or
#   IC scaling probably differs from the authors'. The membership claims (fig7b, fig7c, fig7f,
#   fig7-negative-weights) and the pair counts depend on it.
# - PWC sharpness, as the half-count width of a raw histogram over +-50 or +-100 ms, includes the
#   flat base and cannot give the paper's 2 ms. The paper's lag range or baseline handling is not
#   stated.
# - STRFs use 5-ms bins and 20 lags (and 1 ms with 50 lags for the temporal profiles), from the
#   data set's sample code by the first author; the paper gives no STRF parameters. The MI
#   projection bins are a standard choice.
# - Fewer iterations than the paper, for time: 100 random groups per cNE (paper 500) and 200 model
#   runs for the CRs (paper 1000). Membership in model runs uses the real data's thresholds.
# - The DG model is a Python port of the CorBinian fit (bisection on each pair's latent
#   correlation), not the MATLAB code.
#
# What was found about the data set: it holds the 16 columnar recordings and 655 units of
# Figures 1 to 7, 10 and 11C to F, with the stimuli, and its counts, units and clocks are
# consistent with the descriptor. It does not hold the 5-s repeats (Figure 9), the 15 repeats of
# the 10-min RN (Figure 11A, B, and the 'repeat' CRs) or the 64-channel recordings (Figure 8).
# Paired files (sites 1 and 2, 3 and 4, and so on) share a tip depth and may be one penetration
# recorded with both stimuli; the descriptor does not say, and no unit can be matched across them.
# Two units have spike times out of order by under 0.1 ms."""
s=s.replace("# SUMMARY", summary)
open(p,'w').write(s)
EOF
python3 $TMPDIR/py2nb.py $TMPDIR/nb.py entries/see-2018/reproduce_see_2018.ipynb && cp $TMPDIR/nb.py $TMPDIR/nb_final_src.py && rm -rf entries/see-2018/__pycache__ && date -u
```

```
Exit code 1
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/__init__.py", line 204, in write
    fp.write(s)
    ^^^^^^^^
AttributeError: 'str' object has no attribute 'write'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/tmp/claude-1001/py2nb.py", line 23, in <module>
    nbformat.write(nb, sys.argv[2])
    ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/__init__.py", line 208, in write
    with Path(fp).open("w", encoding="utf8") as f:
         ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/pathlib/_local.py", line 537, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'entries/see-2018/reproduce_see_2018.ipynb'
```

**Agent calls Bash**

```bash
python3 $TMPDIR/py2nb.py $TMPDIR/nb.py entries/see-2018/reproduce_see_2018.ipynb && rm -rf entries/see-2018/__pycache__ && date -u && time python tools/entry.py all entries/see-2018 2>&1 | tail -5; date -u
```

```
Fri Nov 13 05:20:06 UTC 2026
Installed kernelspec registry-see-2018 in executed/see-2018/.venv/share/jupyter/kernels/registry-see-2018
0 error(s)
pass  reproduce_see_2018.ipynb  (2053 s)

real	34m21.711s
user	114m42.030s
sys	1m37.074s
Fri Nov 13 05:54:27 UTC 2026
```

**Agent**

Final run passed (34 min). Checking that the outputs match the conclusions.

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python -c "
import nbformat
nb=nbformat.read('executed/see-2018/reproduce_see_2018.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain','')
        if t and 'Figure size' not in t: print('-----',c.metadata.get('tags',''),'\n',t[:6000])
" | cut -c1-260 > $TMPDIR/out2.txt; diff <(grep -v " in [0-9]* s\|ran in\|peak memory" $TMPDIR/out1.txt) <(grep -v " in [0-9]* s\|ran in\|peak memory" $TMPDIR/out2.txt)
```

```
32a33,34
> site 4 unit 17: 1 decreasing steps of 1851 (largest 0.03 ms), 8 repeated times
> site 7 unit 21: 28 decreasing steps of 2707 (largest 0.09 ms), 107 repeated times
449,450c451,463
< ptd: cNE median 3.150, random median 2.695; cNE higher in 51.5% of 103; signed-rank p = nan; UI median 0.416, KS against uniform D = 0.211, p = 0.000163
< mi: cNE median 0.263, random median 0.208; cNE higher in 60.2% of 103; signed-rank p = nan; UI median 0.366, KS against uniform D = 0.261, p = 1.17e-06
---
>  site  cne  size  n_groups  level  count
>     3    0     2        70      1    347
>     5    1     2        28      1  11398
>     5    2     2        28      1    867
>     6    1     2        46      1    717
>     9    0     2        78      1   6215
>     9    4     2        78      1  12302
>    10    1     2        72      1    217
>    13    1     2        76      1   1102
>    14    2     2        84      1    566
>    15    1     2        54      1   1035
> ptd: cNE median 3.209, random median 2.758; cNE higher in 58.3% of 103; signed-rank p = 0.000702; UI median 0.347, KS against uniform D = 0.250, p = 3.65e-06
> mi: cNE median 0.275, random median 0.209; cNE higher in 67.0% of 103; signed-rank p = 3.08e-06; UI median 0.267, KS against uniform D = 0.309, p = 3.15e-09
```

**Agent**

Both runs agree, and the random-group numbers match the conclusion. Writing the attempt record now (05:56). Checking the schema first.

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required')); p=s['properties']
for k in ['outcomes','findings','datasets','provenance','missing_datasets']:
  print(k, json.dumps(p.get(k),indent=None)[:1500])
print(json.dumps(s.get('\$defs',{}),indent=None)[:4000])
"
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
outcomes {"description": "One per claim attempted.", "type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["claim", "outcome"], "properties": {"claim": {"description": "Claim id from the target's claims file.", "type": "string"}, "outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"], "description": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`."}, "blocked_by": {"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "dataset_missing", "too_large", "not_runnable", "other"]}, "notes": {"description": "What differs, or what was missing, stated factually.", "type": "string"}, "notebook": {"description": "Path of the notebook within the entry.", "type": "string"}, "output": {"description": "Which output shows the result, e.g. a cell tag.", "type": "string"}, "measured": {"description": "The values obtained, for claims with expected values: one number, or one per expected value, in the same order.", "oneOf": [{"type": "number"}, {"type": "array", "minItems": 1, "items": {"type": "number"}}]}, "deviations": {"description": "How the test differed from the paper's method or data, e.g. one session of four, or a substituted model.", "type": "array", "items": {"type": "string", "minLength": 1}}, "assumed": {"description": "True w
findings {"description": "What the attempt found, whatever the outcomes: about the dataset itself (`about: data`, for its owner and the archive, shown on the dataset's page) or about the paper (`about: paper`, shown on the paper's page).", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["kind", "statement"], "properties": {"kind": {"enum": ["metadata_error", "data_mi
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/rec && cat > $TMPDIR/rec/make.py <<'EOF'
import yaml
NB = "reproduce_see_2018.ipynb"
def o(claim, outcome, notes, measured=None, deviations=None, assumed=None, blocked_by=None, tag=True):
    d = {"claim": claim, "outcome": outcome}
    if blocked_by: d["blocked_by"] = blocked_by
    if tag:
        d["notebook"] = NB; d["output"] = f"claim:{claim}"
    if measured is not None: d["measured"] = measured
    if assumed: d["assumed"] = True
    d["notes"] = notes
    if deviations: d["deviations"] = deviations
    return d

DET = ("cNE detection details the paper does not fix are this attempt's readings, from the claims file's opening comment "
       "and cne.py (Marcenko-Pastur bound (1 + sqrt(n/T))^2, symmetric fastICA with logcosh, sign reading (a) for membership, "
       "spikes inside the stimulus period only).")
PWC = ("PWC lag bins of 1 ms over +-50 and +-100 ms, the claims file's readings; the paper does not fix them.")
STRF = ("STRFs are event- or spike-triggered averages on 5-ms stimulus bins with 20 lags (100 ms), an assumption taken from the "
        "data set's sample code by the first author (Codes.zip, create_stim_segments_from_stim_mat.m, 'for AI cells, and 5 ms bins, "
        "nlags = 20 is sufficient'); the paper gives no STRF parameters. MI projection bins (25 bins over -5 to 5 SD) are a standard choice.")
outcomes = [
 o("fig2bd-pwc-measures-covary", "not_reproduced",
   "R2 of sharpness and of peak delay on the 10-ms correlation coefficient over 14174 pairs are 0.130 and 0.110 (+-50 ms, linear "
   "axes; given as measured), 0.149 and 0.173 (log), 0.173 and 0.094 (+-100 ms, linear) and 0.219 and 0.234 (log). No reading "
   "comes near 0.5 +/- 0.05. Both measures fall as the correlation rises, as in the paper.",
   [0.130, 0.110], [PWC]),
 o("fig2eg-distance-weak", "not_reproduced",
   "Under both distances (depth difference, Euclidean distance on the probe) and both lag ranges, R2 is 0.006 to 0.060 for "
   "sharpness and delay and 0.032 to 0.037 for the correlation coefficient. None is in 0.09 to 0.33. Distance explains even "
   "less than the paper says. The measured value is the largest of the three R2 under the first reading (depth difference, "
   "+-50 ms).", 0.056, [PWC]),
 o("fig4-example-nine-cnes", "reproduced",
   "Site 10 is the only recording with 38 units. The detection finds 9 cNEs with 2 to 6 members (sign reading a), the "
   "same with five other seeds; under reading (b) the sizes are 2 to 5.", [9, 2, 6], [DET]),
 o("fig4s2-interleaved-halves-stable", "reproduced",
   "192 of 205 ICs of the two interleaved halves (93.7%) have a match above the 99th percentile of the null, under both null "
   "readings (a, shuffled against shuffled; b, real against shuffled); per recording 81 to 100%.", 93.7, [DET,
   "Units without spikes in a half are left out of that half's detection and given weight 0 when the ICs are correlated (none "
   "in this data set at 10 ms)."]),
 o("fig4s3-train-test-83pct", "not_reproduced",
   "There are 102 training cNEs, the paper's number, but 100 (98.0%, quadratic projection; given as measured) or 101 (99.0%, "
   "linear) match above the 95th percentile of the non-matched correlations (606 values that are neither a row nor a column "
   "maximum, legend C). With every non-row-maximum value as the null, 95.1% or 99.0%. The training cNEs predict the test "
   "half better than the paper reports; by the criterion, a correct count with an out-of-range percentage is not reproduced.",
   [102, 98.0], [DET, "The test half is z-scored on itself and both IC sets are projected onto it; units silent in either half "
   "would be left out (none here)."]),
 o("fig5a-mi-peaks-10-15ms", "not_reproduced",
   "No reading puts the largest MI at 10 or 15 ms. With the 5000 largest 1-ms samples of the interpolated activity as events "
   "(event reading a), the mean and median MI rise with bin size and peak at 35 ms under both projections (mean 0.698 bits "
   "linear, 0.730 quadratic), nearly flat from 15 ms. With the 5000 largest local peaks (event reading b), MI is highest at "
   "2 ms and falls with bin size. The result rests on the STRF resolution and MI bins, which the paper does not give.",
   None, [DET, STRF, "Each cNE's 5000 events are taken as its 5000 largest 1-ms activity samples or local peaks, readings of "
   "'a threshold such that each cNE had 5000 events' (Materials and methods, STRF mutual information)."]),
 o("fig5b-number-decreases-with-bin", "reproduced",
   "The mean number of cNEs over the 16 recordings falls from 11.06 at 2 ms to 3.75 at 50 ms, monotonically (Spearman rho "
   "-1.0); every recording has fewer at 50 than at 2 ms.", None, [DET]),
 o("fig5c-size-increases-with-bin", "reproduced",
   "The mean of per-recording mean sizes rises from 3.88 at 2 ms to 5.11 at 50 ms (Spearman rho 0.952, p = 0.00026; sign "
   "reading a), with small dips at 8 and 20 ms; under reading (b) from 3.91 to 5.51 (rho 1.0).", None, [DET]),
 o("fig6c-spike-pwc-narrower-than-strf-pwc", "reproduced",
   "Assumed, the STRF PWC (cross-correlation of the two temporal profiles) made non-negative by subtracting its minimum, as the "
   "Results call STRF PWCs 'broad' (cNEs are not fully accounted for by stimulus synchronization, paragraph 5). Then the spike "
   "PWC (+-50 ms) is sharper than the STRF PWC in 63.2% of 1012 cNE pairs and 43.8% of non-cNE pairs, and the spike/STRF "
   "sharpness ratio is lower for cNE pairs (median 0.778 against 1.062, Mann-Whitney p = 4.3e-53). With negative values set to "
   "zero, the STRF PWCs are 4 ms wide and spike PWCs are sharper in only 6.5% of cNE pairs, though the ratio is still lower for "
   "cNE pairs (p = 6.3e-59). Question for the authors, how the STRF PWC was computed and compared (recorded as a finding).",
   None, [DET, "STRFs for the temporal profiles at 1 ms with 50 lags, the data set's sample code's 50 ms; profile = mean over "
   "frequency of the STRF minus its mean (Figure 6B, E legend).",
   "Assumption, the STRF PWC is made non-negative by subtracting its minimum; the paper does not say, and the other reading "
   "(negative values set to zero) gives the opposite result on the first part of the criterion."], assumed=True),
 o("fig6j-sharpness-cne-pairs", "partially_reproduced",
   "With +-50 ms lags, cNE pairs have sharper PWCs at p < 0.001 in 14 of 16 recordings; the exceptions are site 5 (5 cNE pairs, "
   "p = 0.023) and site 6 (10 pairs, p = 0.054), where cNE pairs are still sharper in median. With +-100 ms, 12 of 16. Over all "
   "recordings there are 1012 cNE and 13162 non-cNE pairs, against the paper's 3087 and 8838; the paper's per-recording cNE "
   "pair counts are larger than the cNE sizes it reports allow if each pair is counted once, so it may count pairs differently.",
   None, [DET, PWC]),
 o("fig6-member-pwc-sharpness-delay", "not_reproduced",
   "Pooled over 1012 cNE pairs (+-50 ms; given as measured), the median sharpness is 12.0 ms and the mean 12.42 +/- 5.59 ms, "
   "against about 2 and 3.39 +/- 1.21 ms; the mean absolute peak delay 1.64 ms is within 0.76 +/- 1.74 ms. Per recording 12.2, "
   "12.5 and 1.49 ms; with +-100 ms the sharpness is about 33 ms. 80% of cNE pairs peak at 0 or 1 ms; the half-count width of a "
   "raw histogram includes its flat base, which a 2-ms median would need removed. One of three values holds.",
   [12.0, 12.42, 1.64], [DET, PWC]),
 o("fig7-totals", "reproduced",
   "16 recordings and 655 units, the paper's counts, one file per penetration and stimulus. 104 cNEs, 6.50 +/- 1.97 per "
   "recording (range 3 to 10). Each recording has one stimulus file, so the reading of which file was used does not arise.",
   [16, 655, 104, 6.5], [DET]),
 o("fig7a-number-vs-neurons", "reproduced",
   "Slope 0.140 cNEs per unit, R2 0.745, F-test p = 1.7e-05 (paper 0.74, p = 1.68e-5). The fraction is 16.1% (a, given as "
   "measured), 14.0% (b) and 15.9% (c), all within tolerance.", [0.745, 16.1], [DET]),
 o("fig7b-size-vs-neurons", "not_reproduced",
   "Mean size 4.58 +/- 1.84 pooled over 104 cNEs (given as measured) and 4.34 per recording, against 7.4 +/- 2.5; 10.7% of the "
   "units against 17%; per-recording mean size on units R2 0.807 (slope 0.078, p = 2.3e-06), against 0.33. Only the positive "
   "slope with p < 0.05 holds. Sign reading (b) gives a mean of 4.73 and R2 0.745. The cNEs are smaller than the paper's while "
   "their number matches, which points at the membership threshold or IC scaling (a question for the authors).",
   [4.58, 0.807, 10.7], [DET]),
 o("fig7-negative-weights", "not_reproduced",
   "Under sign reading (a), 24 of 104 cNEs (23.1%) have a member below the lower threshold, against 9; 90.8% of member weights "
   "are positive. Under reading (b), 65.", 24, [DET]),
 o("fig7c-membership", "not_reproduced",
   "Under sign reading (a) (given as measured), 59.2% of 655 units are in one cNE, 34.4% in none and 6.4% in more than one; "
   "under (b), 61.2%, 32.1% and 6.7%. None is within tolerance (68, 9 and 23%).", [59.2, 34.4, 6.4], [DET]),
 o("fig7d-pairs-within-200um", "reproduced",
   "88.5% of 1025 member pairs counted once per cNE (88.3% of 1012 unique pairs) are under 200 um apart, by depth difference and "
   "Euclidean distance alike; per recording 61.4 to 100%.", 88.5, [DET]),
 o("fig7e-no-depth-bias", "reproduced",
   "Median depth 460 um for the 430 members and 450 um for all 655 units (difference 10 um); KS p = 0.999, Mann-Whitney "
   "p = 0.474; members against non-members KS p = 0.498, MWU p = 0.116. cNE median depths run from 200 to 662 um (units 150 "
   "to 662). The tests are the claims file's readings; the paper names none.", None,
   [DET, "Neither test is the paper's, which names none (claims file)."], assumed=True),
 o("fig7f-span-200um", "not_reproduced",
   "80.8% of 104 cNEs span 200 um or less (78.8% under sign reading b), above 70 +/- 7%; two span more than 400 um (up to "
   "500 um). Smaller cNEs than the paper's span less.", 80.8, [DET]),
 o("fig8-spont-evoked-72pct", "blocked",
   "The eight 64-channel recordings with spontaneous and evoked epochs are not in CRCNS ac-3, which holds only the 16 "
   "32-channel files; the paper's data availability statement names only ac-3, and no other public copy was found.",
   blocked_by="data_missing", tag=False),
 o("fig9c-cne-events-more-mi", "blocked",
   "The 50 repeats of the 5-s DMR and RN segments are not in CRCNS ac-3 (Data.zip holds one 10-min recording per site, with "
   "1795 or 1799 triggers of the continuous stimulus and no repeat trials); the paper names no other deposit.",
   blocked_by="data_missing", tag=False),
 o("fig9s1-cne-mi-above-random-groups", "blocked",
   "Needs the 5-s repeats, which are not in the data set (see fig9c-cne-events-more-mi).", blocked_by="data_missing", tag=False),
 o("fig9s2-noise-correlations", "blocked",
   "Needs the 50 trials of the 5-s repeats, which are not in the data set (see fig9c-cne-events-more-mi).",
   blocked_by="data_missing", tag=False),
 o("fig10b-ptd-higher", "reproduced",
   "Over 476 cNE and member pairs (the paper has 703, its cNEs being larger), cNE STRFs have a higher PTD under all four "
   "readings, signed-rank p = 8.0e-12 (linear projection, every bin above threshold), 3.8e-09 (linear, peak per run), 5.6e-04 "
   "(quadratic, every bin) and 2.4e-05 (quadratic, peak); cNE higher in 54 to 62% of pairs.", None,
   [DET, STRF, "cNE events are the 10-ms bins above the 99.9th percentile threshold, placed at the bin centre; the paper does not "
   "say how events are timed for STRFs.", "PTD is the maximum minus the minimum of the averaged STRF, which equals the legend's "
   "(max - min) of the summed STRF divided by the count."]),
 o("fig10c-strf-mi-higher", "not_reproduced",
   "cNE STRF MI exceeds the member's in 53 to 56% of 476 pairs, but no reading reaches p < 0.001: signed-rank p = 0.0015 "
   "(linear, every bin), 0.0076 (linear, peak), 0.049 (quadratic, every bin), 0.185 (quadratic, peak). The paper has "
   "p = 1.6e-59 over 703 pairs. The MI rests on the STRF resolution and projection bins chosen here.", None,
   [DET, STRF, "Events as in fig10b-ptd-higher."]),
 o("fig10s1-random-group-strfs", "reproduced",
   "Over 103 cNEs (the paper's 103; one 1-member cNE has no groups), the members' summed spikes give a higher PTD than the "
   "median random group (3.21 against 2.76, signed-rank p = 7.0e-04) and a higher STRF MI (0.275 against 0.209 bits, "
   "p = 3.1e-06); the UIs have medians 0.347 and 0.267 and differ from uniform (KS p = 3.7e-06 and 3.1e-09). No set fell "
   "under 200 spikes. The PTD test is near the 0.001 threshold.", None,
   [DET, STRF, "100 random groups per cNE, not the paper's 500, to fit the time limit; the UI is out of 101 values.",
   "The ten 2-member cNEs allow only 28 to 84 unique groups with one member; the Methods' next level (two members) gives the cNE "
   "itself, so the groups found at one member are used, a choice the Methods do not make."]),
 o("fig11ab-real-vs-surrogate", "blocked",
   "The 15 repetitions of the 10-min RN are not in CRCNS ac-3, which holds one presentation per site; the paper names no other "
   "deposit.", blocked_by="data_missing", tag=False),
 o("fig11c-models-number", "reproduced",
   "Mean over 200 runs per recording; real 6.50 cNEs. Shuffled 0.23 and PR 1.41 (10-ms bins) or 1.52 (5-ms bins), fewer in "
   "all 16 recordings; DG 8.00, more in 15. Bonferroni (x3) paired t-test p = 4.6e-09, 3.1e-08 or 4.6e-08, and 1.5e-04, under "
   "both PR readings.", None,
   [DET, STRF, "The DG model is a Python port of the CorBinian fit (bisection on each pair's latent correlation with Gauss-Legendre "
   "bivariate normal probabilities, eigenvalues clipped to make it positive definite), not the MATLAB code the paper used.",
   "PR assigns each spike to a random time bin of its projection class (15 equal bins over the range of the unit's STRF "
   "projections), the stimulus segment being the one before the bin's start."]),
 o("fig11d-models-size", "not_reproduced",
   "Real mean size 4.34. With runs without cNEs left out, shuffled 4.95 (larger, corrected p = 0.055), PR 3.80 or 3.84 "
   "(p = 0.20, 0.24), DG 4.30 (p = 1). Counting such runs as size 0, shuffled 1.11 (smaller, p = 1.4e-07), PR 3.74 or 3.83 "
   "(p = 0.13, 0.23), DG 4.30. At most one of three comparisons holds under any reading.", None,
   [DET, "Membership in model runs uses each recording's thresholds from the shuffles of its real data, not shuffles of every "
   "model run, to fit the time limit; the thresholds are within 0.03 of 1.5/sqrt(n) in every recording, the spread of a random "
   "unit vector, so they do not depend on the data.", "Model details as in fig11c-models-number."]),
 o("fig11ef-coincidence-ratios", "partially_reproduced",
   "Reading (b) of the criterion, the only one the data set allows. 400 groups of 2 and 400 of 3 from 1012 and 1397 possible; "
   "28 groups of 3 with a real CR of 0 left out. Median normalised CR, pairs, shuffled 0.159, PR 0.215 or 0.223, DG 0.776; "
   "triplets 0.000, 0.000 and 0.730. Every comparison has the CR below one with Bonferroni (x4) p < 1e-35. The 'repeat' CR "
   "needs the repeated 10-min RN, which the data set lacks, so the claim holds on the models only.", None,
   [DET, "200 runs of each model, not the paper's 1000, to fit the time limit; the median over runs is used.",
   "CR bin 10 ms, the claims file's assumption.", "Model details as in fig11c-models-number."]),
 o("fig11s3b-pr-strf-similarity", "reproduced",
   "Assumed, PR on 5-ms bins, the STRF resolution used here and the DG model's bin in the Methods. Median STRF similarity "
   "over 3275 unit runs (5 runs per recording), PR 0.737 (5 ms; given as measured) or 0.645 (10 ms, outside 0.666 to 0.814), "
   "shuffled 0.022, DG 0.022. Under the 10-ms reading the PR part fails.", 0.737,
   [DET, STRF, "Assumption, PR on 5-ms bins; the paper does not give the PR bin, and the 10-ms reading falls just outside the "
   "tolerance.", "The real STRF is computed from the real train binned as the model is, spikes at bin centres."], assumed=True),
]
meth = "Not fixed by the paper; a question for its authors, so that they can confirm or correct the choice. "
findings = [
 {"kind": "data_missing", "statement": "The data set holds the 16 columnar recordings made with the 10-min DMR and RN (Figures 1 to "
  "7, 10 and 11C to F). It does not hold the 50 repeats of the 5-s segments (Figure 9 and its supplements), the 15 repeats of "
  "the 10-min RN (Figure 11A, B and the 'repeat' coincidence ratios) or the eight 64-channel recordings with spontaneous and "
  "evoked epochs (Figure 8), although the paper's data availability statement points to this data set for its data."},
 {"kind": "metadata_insufficient", "statement": "The descriptor does not say that rn1 is the dynamic moving ripple and rn16 the "
  "ripple noise (the paper's names), that `position` is a pair of a lateral offset and a depth below the surface in um, or "
  "whether files with the same tip depth (sites 1 and 2, 3 and 4, and so on) are one penetration recorded with both stimuli. "
  "Their units were sorted separately and cannot be matched."},
 {"kind": "format_error", "statement": "Two units have spike times out of order, site 4 unit 17 (1 step back of 0.03 ms, 8 "
  "repeated times) and site 7 unit 21 (28 steps back of up to 0.09 ms, 107 repeated times), against sorted times in the other "
  "653."},
 {"kind": "methods_unavailable", "statement": meth + "How IC weights were scaled and membership thresholds set. With the "
  "Methods' detection, the number of cNEs matches the paper (104, 6.5 per recording, R2 0.745 against units), but the cNEs are "
  "smaller (4.6 against 7.4 members), 34% of units belong to none (paper 9%) and 24 cNEs have a negative member (paper 9)."},
 {"kind": "methods_unavailable", "statement": meth + "The lag bin, lag range and any baseline correction of the pairwise "
  "correlation functions. The half-count width of a 1-ms histogram over +-50 ms gives a median of 12 ms for cNE pairs, not "
  "about 2 ms, and the R2 against the correlation coefficient is 0.1 to 0.2, not about 0.5."},
 {"kind": "methods_unavailable", "statement": meth + "The STRF window and resolution, the MI projection bins, and how cNE events "
  "are timed for STRFs. With 5-ms bins and 20 lags (the data set's sample code), STRF MI over bin sizes peaks at 35 ms or 2 ms "
  "depending on how the 5000 events are taken, not at 10 to 15 ms, and cNE STRF MI exceeds member MI only at p = 0.0015."},
 {"kind": "methods_unavailable", "statement": meth + "How the STRF PWC of Figure 6 was computed and how its sharpness was "
  "measured, given that a cross-correlation of temporal profiles has negative values. Subtracting its minimum (assumed here) "
  "makes spike PWCs sharper for 63% of cNE pairs; clipping at zero makes the STRF PWCs 4 ms wide and reverses this. Also the "
  "time bin of the PR model (5 ms assumed; 10 ms gives a median STRF similarity of 0.645, not 0.74)."},
 {"kind": "other", "about": "paper", "statement": "The per-recording cNE pair counts in Supplementary file 1 (Figure 6J and its "
  "supplement, 3087 cNE pairs in all) exceed the number of member pairs the reported cNE sizes allow if each pair is counted "
  "once (for example 365 cNE pairs in a recording), so the paper may count cNE pairs per ordered pair or per cNE; this attempt "
  "finds 1012 unique pairs."},
]
rec = {
 "schema_version": 3, "id": "see-2018-01",
 "datasets": [{"archive": "crcns", "id": "ac-3", "version": "unversioned", "doi": "10.6080/K09021X1", "relation": "primary"}],
 "paper": "doi:10.7554/elife.35587", "date": "2026-11-13", "entry": "see-2018",
 "provenance": {"kind": "agent", "accountable": {"name": "CatalystNeuro"},
   "agent": {"harness": "Claude Code", "model": "claude-opus-5-5", "protocol": "pilot-14"},
   "runner": {"platform": "GitHub Actions", "url": "https://github.com/catalystneuro/encore/actions/runs/43360769126"}},
 "outcomes": outcomes, "findings": findings,
}
yaml.safe_dump(rec, open("attempts/see-2018-01.yaml", "w"), sort_keys=False, width=110, allow_unicode=True)
EOF
. $TMPDIR/env/bin/activate && uv pip install -q pyyaml && python $TMPDIR/rec/make.py && grep -c "claim:" attempts/see-2018-01.yaml; grep -n "^- claim\|  claim" attempts/see-2018-01.yaml | wc -l
```

```
57
31
```

**Agent**

31 outcomes, one per claim. Fixing one overstated number (the threshold deviation is within 0.04 of 1.5/√n under reading (a), not 0.03), then the README.

**Agent calls Bash**

```bash
sed -i 's/thresholds are within 0.03 of 1.5\/sqrt(n) in every recording/thresholds are within 0.04 of 1.5\/sqrt(n) in every recording (0.003 under sign reading (b))/' $TMPDIR/rec/make.py && . $TMPDIR/env/bin/activate && python $TMPDIR/rec/make.py && grep -n "within 0.0" attempts/see-2018-01.yaml; sed -n 495,531p tools/entry.py; date -u
```

```
401:    every model run, to fit the time limit; the thresholds are within 0.04 of 1.5/sqrt(n) in every recording (0.003
def file_hash(path: Path) -> str:
    import hashlib
    return hashlib.sha256(path.read_bytes()).hexdigest()


def entry_hash(entry_dir: Path) -> str:
    """A hash of everything a run of the entry's notebooks reads from the repository: every file of the entry (its
    notebooks, helpers, lock and entry.yaml, which names the Python and the dataset versions), the packages `run`
    adds, and RUN_VERSION. Two runs from the same hash execute the same code on the same data versions."""
    import hashlib
    h = hashlib.sha256(f"run {RUN_VERSION}; harness {' '.join(HARNESS)}; python {python_of(entry_dir)}\n".encode())
    for path in sorted(p for p in entry_dir.rglob("*") if p.is_file()):
        rel = path.relative_to(entry_dir)
        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
            continue
        h.update(f"{rel.as_posix()}\0{file_hash(path)}\n".encode())
    return h.hexdigest()


[... 20 more lines not kept]
```

**Agent**

README is part of the entry hash, so adding it means one more full run; there is time for it (05:56). Writing the README.

**Agent calls Write**

```json
{
 "file_path": "entries/see-2018/README.md",
 "content": "# See, Atencio, Sohal & Schreiner (2018) from CRCNS ac-3\n\nTests the findings of [See et al. (2018)](https://doi.org/10.7554/eLife.35587) that can be tested\non [CRCNS ac-3](https://doi.org/10.6080/K09021X1). The data set holds the 16 columnar recordings\n(655 units) made in rat primary auditory cortex with the 10-min dynamic moving ripple and ripple\nnoise, and the stimuli. It does not hold the 5-s repeats (Figure 9), the 15 repeats of the 10-min\nripple noise (Figure 11A, B) or the 64-channel recordings (Figure 8).\n\n| Claim | Outcome |\n|---|---|\n| 16 penetrations, 655 neurons, 104 cNEs, 6.5 per penetration | Reproduced |\n| Example recording: 9 cNEs of 2 to 6 neurons | Reproduced |\n| Number of cNEs grows with the number of neurons (R2 0.74, about 15%) | Reproduced |\n| Mean cNE size 7.4 neurons, R2 0.33 against neurons | Not reproduced |\n| 9 cNEs with a negative-weight member | Not reproduced |\n| 68% of neurons in one cNE, 9% in none, 23% in several | Not reproduced |\n| 82% of cNE pairs within 200 um | Reproduced |\n| No depth bias of cNE members | Reproduced (on an assumed test) |\n| 70% of cNEs span 200 um or less | Not reproduced |\n| PWC sharpness and delay explain about 50% of the variance of the correlation | Not reproduced |\n| Distance explains 10 to 30% of the variance of the synchrony measures | Not reproduced |\n| cNE pairs have sharper PWCs in every penetration | Partially reproduced |\n| Member PWC sharpness about 2 ms, delay 0.76 ms | Not reproduced |\n| Spike PWCs narrower than STRF PWCs for cNE pairs | Reproduced (on an assumption) |\n| cNEs of interleaved halves match (96%) | Reproduced |\n| Training cNEs predict test activity (102 cNEs, 83%) | Not reproduced |\n| STRF MI peaks at 10 to 15 ms bins | Not reproduced |\n| Fewer and larger cNEs with larger bins | Reproduced |\n| cNE STRFs have a higher peak-trough difference than members' | Reproduced |\n| cNE STRFs have a higher MI than members' | Not reproduced |\n| cNE members' STRFs beat random groups | Reproduced |\n| Shuffled and PR models give fewer cNEs, DG more | Reproduced |\n| All models give smaller cNEs | Not reproduced |\n| Coincidence ratios below the real data | Partially reproduced (models only) |\n| PR model keeps STRFs (similarity 0.74) | Reproduced (on an assumption) |\n| Figures 8, 9 and 11A, B (five claims) | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe number of cNEs matches the paper closely, but they are smaller, which bears on the membership\nclaims. The paper does not give its STRF parameters or the lag range of its pairwise correlation\nfunctions, and several outcomes rest on the choices made here. The attempt record, with the\nreasons and the differences from the paper's method, is\n[`attempts/see-2018-01.yaml`](../../attempts/see-2018-01.yaml).\n\n- `reproduce_see_2018.ipynb`: the analysis. It takes about 35 minutes on four processes, most of\n  it the detection at eight bin sizes and the model runs.\n- `cne.py`: loading from the bucket, the cNE detection, pairwise correlation functions, STRFs and\n  their mutual information, and the shuffled, PR and DG models. Other notebooks on this data set\n  can import it.\n"
}
```

```
File created successfully at: entries/see-2018/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/see-2018 2>&1 | tail -10; python tools/claims_check.py --help 2>&1 | head -3
```

```
0 error(s)
Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]
```

**Agent**

Check passes. Scanning my text for disallowed words and characters, then the final run.

**Agent calls Bash**

```bash
grep -n -i "rather\|—\|genuinely\|actually\|worth noting\|that said" attempts/see-2018-01.yaml entries/see-2018/README.md entries/see-2018/cne.py $TMPDIR/nb.py | head; date -u; time python tools/entry.py all entries/see-2018 2>&1 | tail -3; date -u
```

```
Fri Nov 13 05:56:36 UTC 2026
Installed kernelspec registry-see-2018 in executed/see-2018/.venv/share/jupyter/kernels/registry-see-2018
0 error(s)
pass  reproduce_see_2018.ipynb  (2059 s)

real	34m28.081s
user	115m22.067s
sys	1m39.152s
Fri Nov 13 06:31:04 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && python -c "
import nbformat
nb=nbformat.read('executed/see-2018/reproduce_see_2018.ipynb',4)
for c in nb.cells:
    if c.cell_type!='code': continue
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain','')
        if t and 'Figure size' not in t: print('-----',c.metadata.get('tags',''),'\n',t[:6000])
    for o in c.get('outputs',[]):
        if o.get('output_type')=='error': print('ERROR',o.get('ename'))
" | cut -c1-260 > $TMPDIR/out3.txt; diff <(grep -v " in [0-9]* s\|ran in\|peak memory" $TMPDIR/out2.txt) <(grep -v " in [0-9]* s\|ran in\|peak memory" $TMPDIR/out3.txt) && echo identical; python tools/entry.py handover entries/see-2018 2>&1 | tail -3; ls executed/see-2018/handover; git status --short | head -20
```

```
identical
wrote executed/see-2018/handover
cne.py
reproduce_see_2018.ipynb
see-2018.yaml
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
?? attempts/see-2018-01.yaml
?? entries/see-2018/
?? scripts
```

**Agent calls Bash**

```bash
ls -a entries/see-2018; git check-ignore -v executed/see-2018 | head -2; date -u
```

```
.
..
.claude
README.md
__pycache__
cne.py
entry.yaml
reproduce_see_2018.ipynb
requirements.in
requirements.lock.txt
.gitignore:6:executed/	executed/see-2018
Fri Nov 13 06:31:32 UTC 2026
```

**Agent calls Bash**

```bash
ls -la entries/see-2018/.claude; git check-ignore -v entries/see-2018/.claude entries/see-2018/__pycache__
```

```
total 12
drwxr-xr-x 3 runner runner 4096 Nov 13 03:57 .
drwxr-xr-x 4 runner runner 4096 Nov 13 05:56 ..
drwx------ 2 runner runner 4096 Nov 13 03:57 .cc-writes
.gitignore:1:__pycache__/	entries/see-2018/__pycache__
```

**Agent**

I ran steps 1 to 6 of the Author protocol on CRCNS ac-3. `entry.py all` passes with 0 errors, and the notebook runs in 34 min (peak memory 1.9 GB). It ran three times on the full data. The last two runs gave identical outputs. The handover is built in `executed/see-2018/handover/`. Nothing is committed.

**1. Outcomes (31 claims)**

| Claim | Outcome | Key numbers (paper) |
|---|---|---|
| fig7-totals | reproduced | 16 recordings, 655 units, 104 cNEs, 6.50 ± 1.97 per recording (identical) |
| fig4-example-nine-cnes | reproduced | site 10: 9 cNEs of 2 to 6 members |
| fig7a-number-vs-neurons | reproduced | R² 0.745, p = 1.7e-5 (0.74, 1.68e-5); 16.1% of units |
| fig7d-pairs-within-200um | reproduced | 88.5% (82%) |
| fig7e-no-depth-bias | reproduced, assumed | KS p = 0.999, MWU p = 0.47; the tests are the claims file's, the paper names none |
| fig4s2-interleaved-halves-stable | reproduced | 93.7% (96%) |
| fig5b-number-decreases-with-bin, fig5c-size-increases-with-bin | reproduced | monotonic trends |
| fig6c-spike-pwc-narrower-than-strf-pwc | reproduced, assumed | 63% of cNE pairs; reverses under the other reading |
| fig10b-ptd-higher | reproduced | p from 8e-12 to 6e-4 under all four readings; 476 pairs (703) |
| fig10s1-random-group-strfs | reproduced | 103 cNEs (103); PTD p = 7.0e-4, MI p = 3.1e-6 |
| fig11c-models-number | reproduced | shuffled 0.23, PR 1.4, DG 8.0 cNEs, against real 6.5 |
| fig11s3b-pr-strf-similarity | reproduced, assumed | PR 0.737 on 5-ms bins (0.645 on 10-ms bins) |
| fig6j-sharpness-cne-pairs | partially reproduced | p < 0.001 in 14 of 16 recordings |
| fig11ef-coincidence-ratios | partially reproduced | all three models below 1; the 'repeat' data are missing |
| fig2bd-pwc-measures-covary | not reproduced | R² 0.09 to 0.23 (0.5) |
| fig2eg-distance-weak | not reproduced | R² 0.006 to 0.06 (0.10 to 0.30) |
| fig4s3-train-test-83pct | not reproduced | 102 training cNEs (102), but 98% matched (83%) |
| fig5a-mi-peaks-10-15ms | not reproduced | MI peaks at 35 ms or 2 ms, depending on the event reading |
| fig6-member-pwc-sharpness-delay | not reproduced | median sharpness 12 ms (2 ms) |
| fig7b, fig7c, fig7f, fig7-negative-weights | not reproduced | mean cNE size 4.6 (7.4); 34% of units in no cNE (9%); 24 cNEs with a negative member (9); 80.8% of cNEs span 200 µm or less (70%) |
| fig10c-strf-mi-higher | not reproduced | best p = 0.0015 |
| fig11d-models-size | not reproduced | model cNEs are not consistently smaller |
| fig8, fig9c, fig9s1, fig9s2, fig11ab | blocked: data_missing | |

**2. Dataset, assumptions and questions**
- **What the data set holds:** 16 files (8 with the DMR stimulus `rn1`, 8 with the RN stimulus `rn16`), 655 units, and the stimuli. The triggers, the stimulus columns and the spike clock all agree, checked by STRF strength and latency against spikes shifted by 30 s.
- **What it lacks:** the 5-s repeats, the 15 repeats of the 10-min RN, and the 64-channel recordings, although the paper points to this data set for its data.
- **Other data findings:**
  - Two units have spike times slightly out of order.
  - The descriptor does not name rn1 and rn16 as DMR and RN, and does not say that `position` is a pair (lateral offset, depth).
  - Paired files share a tip depth and may be one penetration recorded twice. No unit matches across them, so each file counts once.
- **Assumptions:**
  - STRFs use 5-ms bins and 20 lags, from the data set's sample code by the first author.
  - The STRF cross-correlation is made non-negative by subtracting its minimum (fig6c).
  - The PR model uses 5-ms bins (fig11s3b).
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - How IC weights were scaled and membership thresholds set; the number of cNEs matches but they are smaller.
  - The lag range, bin and any baseline correction of the pairwise correlation functions.
  - The STRF parameters, MI bins and how cNE events are timed.
  - How the STRF cross-correlation was computed, and the PR model's time bin.
- **Questions to a reader:** none.

**3. Where the protocol was unclear or missing something**
1. CRCNS has no versions, so step 1.3's pinning does not fit. I recorded `unversioned` with the MD5 sums from `checksums.md5`, as archives.md says.
2. Any edit to the entry, including the README, forces a full re-run, and conclusions can only be written after a run. With a 34-min notebook that meant at least two full runs, and I made three. I wrote all text before the last run.
3. The protocol does not say whether the readings in the claims file's opening comment (IC sign, activity projection, event definition) should be crossed with every claim's own readings. I ran the ones that matter for each claim.
4. The protocol has no rule for cutting iterations to fit the time limit, short of blocking as `too_large`. I recorded these cuts as deviations: 100 random groups (paper 500), 200 CR runs (paper 1000), and the real data's membership thresholds reused for model runs, justified by the thresholds following ±1.5/√n.
5. The source order (Methods, paper's code, other software) does not mention a data set's own code. I used it only as the basis for a stated assumption.
6. Gaps in the criteria:
   - fig4s3's criterion does not cover a correct count with an out-of-range percentage; I judged it not reproduced.
   - fig2eg expects a range but `measured` takes one number; I gave the largest R² under the first reading.
   - When no reading matches, the protocol does not say which reading goes under `measured`; I gave the first one listed.

**4. Runtime and failures**
- The session took about 2 h 50 min (03:43 to 06:32 UTC).
- Each full notebook run took 34 min on 4 processes.
- Bugs I found and fixed before the final runs:
  - 2-member cNEs got no random groups, which made the fig10s1 test give p = nan.
  - A stale copy of the helper in the temp directory shadowed the real one in a dev script.
- An empty `entries/see-2018/.claude/.cc-writes` directory left by the harness is in the entry. I can't remove it, and git does not track empty directories.
- Nothing else failed.

## End of run

67 turns, 162 minutes, $7.46 at API prices, result: success.
