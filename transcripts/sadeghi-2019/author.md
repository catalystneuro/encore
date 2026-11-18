# sadeghi-2019 · author · run 43495516371

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls entries claims attempts paper
```

```
<persisted-output>
Output too large (55KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/e9eb191a-8d7b-4aaf-a4ab-b5af6e6452e6/tool-results/bozxvcbmp.txt

Preview (first 2KB):
Fri Nov 13 19:53:10 UTC 2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/e9eb191a-8d7b-4aaf-a4ab-b5af6e6452e6/tool-results/bozxvcbmp.txt"
}
```

```
1	Fri Nov 13 19:53:10 UTC 2026
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
[... 1587 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/sadeghi-2019.yaml; cat paper/bst-2.data-description.txt; cat papers/datasets/sadeghi-2019.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/e9eb191a-8d7b-4aaf-a4ab-b5af6e6452e6/tool-results/b8p5romlj.txt"
}
```

```
1	# Claims for Sadeghi, Zhai, Stevenson & Escabi (2019), "A neural ensemble correlation code for
2	# sound category identification", PLoS Biol 17(10):e3000449, on CRCNS data set bst-2.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-11,
4	# protocol as stated in docs/protocol.md (Reader). The writer did not look at the data set's data or
5	# files; only its description (paper/bst-2.data-description.txt) was read, to know what it holds.
6	#
7	# Text read: the version of record (PMC6788721, Europe PMC full-text XML, flattened), with its
8	# Results, Discussion, Materials and methods, all figure legends (Figs 1 to 10, S1 to S10 Figs),
9	# and the supplement files S1 Text (s001, proofs on signal and noise correlations, and notes on
10	# S2 to S4 and S6 Figs), S1 Table (s026, the 195 model sounds) and S2 Table (s027, the 18 sounds
11	# of paradigm 3). No PDF was supplied. The extraction dropped every displayed equation (the
12	# shuffled and unshuffled correlograms, their normalization, the noise correlation, the MAP
13	# rule, the spectro-temporal model average, the 1/f filter, the SI and CDI formulas); the prose
14	# around each was read and the criteria below name where an equation would have settled a
15	# detail. The movies and sound files listed as supporting information were not read; no claim
16	# rests on them.
17	#
18	# Code: the paper links only the CRCNS deposit (doi:10.6080/K03X84V3), which holds MATLAB code
19	# (Code/MUACorrAnalysis, with rastermuashuffledxcovwinfastN.m; Code/AuditoryModelCorr, with
20	# Cochleogram.m and cochleogramdyncorr.m; Code/Examples, with NeuralExample.m for Fig 1 and
[... 1019 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/e9eb191a-8d7b-4aaf-a4ab-b5af6e6452e6/tool-results/b8p5romlj.txt",
 "offset": 1040
}
```

```
1040	/Code/MUACorrAnalysis/  
1041	- contains neural correlation analysis code 
1042	/Code/Examples/  
1043	 
1044	- contains example code for both the neural and sound analysis 
1045	 
1046	Neural data directories 
1047	/NeuralData/Paradigm1/ 
1048	- contains neural data for paradigm 1 
1049	/NeuralData/Paradigm2/ 
1050	- contains neural data for paradigm 2 
1051	/NeuralData/Paradigm3/  
1052	- contains neural data for paradigm 3 
1053	 
1054	Sound directory for neural recordings 
1055	/Sounds/Paradigm1/   
1056	- contains sounds for paradigm 1 
1057	/Sounds/Paradigm2/  
1058	- contains sounds for paradigm 2 
1059	/Sounds/Paradigm3/   
[... 325 more lines not kept]
```

**Agent**

Read the protocol and the claims file (27 claims). Now the archive guide and an example entry's format.

**Agent calls Bash**

```bash
grep -n -A60 "^## CRCNS" docs/archives.md | head -120; ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in
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
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/fouke-2025-01.yaml | head -150; cat entries/fouke-2025/README.md | head -30
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
[... 159 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=bst-2/" | python3 -c "
import sys,re
t=sys.stdin.read()
for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',t): print(s,k)
print(re.findall(r'<IsTruncated>(.*?)</IsTruncated>',t))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
B=https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-2/live; curl -s $B/checksums.md5; echo; curl -s $B/filelist.txt; curl -sI $B/data.tar.gz
```

```
916ae724cd3334a16a4396b861e4abe0  data.tar.gz
2aefb552cb1d522f6d3978fbb2f982f5  docs/crcns_bst-2_data_description.docx
81457299a36f12a18f2eb8afa5ef1862  docs/crcns_bst-2_data_description.pdf
2e45d8628e11fcc14627089027f17ee5  docs/FigureData.docx
d0a76ae42a544a60c02912762be2127b  docs/FigureData.pdf
0168f21f46432c8663f282bd817ee127  filelist.txt

# CRCNS.org 'bst-2' dataset files
# To use this for fetching files, comment out files that are
# not needed by putting a '#' as the first character on the line (default mode)
# or put a '+' as the first character to specifiy files to be fetched (+ mode).
# mode='default' (change to '+' for + mode).
 data.tar.gz	5341905669 (4.9 GB)
 docs/crcns_bst-2_data_description.docx	35356 (34.5 KB)
 docs/crcns_bst-2_data_description.pdf	94737 (92.5 KB)
 docs/FigureData.docx	117024 (114.2 KB)
 docs/FigureData.pdf	53764 (52.5 KB)
 checksums.md5	347
HTTP/1.1 200 OK
x-amz-id-2: RGpNjmTmQdwHu0fsNBGqJ4G2Ei/lwHazi6CgfXleBBNZYBPnAkW9MqIf/pA3X6wEUzpOuD+S6KA=
[... 10 more lines not kept]
```

**Agent**

The data are one 5.3 GB tar.gz (not a zip), so random access is impossible; I'll stream it once to list its members and time the pass.

**Agent calls Bash**

```bash
cd $TMPDIR && cat > list.py <<'EOF'
import fsspec, tarfile, time
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-2/live/data.tar.gz"
t=time.time()
f=fsspec.open(url, block_size=2**24).open()
tf=tarfile.open(fileobj=f, mode="r|gz")
for m in tf:
    print(m.size, m.name, round(f.tell()/1e6), round(time.time()-t,1), flush=True)
EOF
python3 -c "import fsspec" 2>&1; timeout 900 python3 list.py > members.txt; tail -3 members.txt; wc -l members.txt
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fsspec
ModuleNotFoundError: No module named 'fsspec'
Traceback (most recent call last):
  File "/tmp/claude-1001/list.py", line 1, in <module>
    import fsspec, tarfile, time
ModuleNotFoundError: No module named 'fsspec'
0 members.txt
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q fsspec aiohttp requests scipy numpy h5py scikit-learn matplotlib soundfile pandas && timeout 1200 python list.py > members.txt; tail -3 members.txt; wc -l members.txt
```

```
148231727 data/NeuralData/Paradigm2/P2_Site01.mat 4951 226.3
148147754 data/NeuralData/Paradigm2/P2_Site10.mat 5098 233.0
96552108 data/NeuralData/Paradigm2/P2_Site08.mat 5246 239.1
311 members.txt
Shell cwd was reset to
```

**Agent**

Full stream pass takes 4 minutes. Members:

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v ModelSounds members.txt; grep -c ModelSounds members.txt; grep ModelSounds members.txt | head -5
```

```
0 data 0 1.3
0 data/Docs 0 1.3
118935 data/Docs/FigureData.docx 0 1.3
26647 data/Docs/crcns_data_description.docx 0 1.3
0 data/Sounds 0 1.3
0 data/Sounds/Paradigm3 0 1.3
529280 data/Sounds/Paradigm3/S3_Sound_Fire5.wav 0 1.3
529280 data/Sounds/Paradigm3/S3_Sound_Water1.wav 1 1.3
529280 data/Sounds/Paradigm3/S3_Sound_Speech1.wav 1 1.3
529280 data/Sounds/Paradigm3/S3_Sound_Speech3.wav 2 1.3
529280 data/Sounds/Paradigm3/S3_Sound_Fire3.wav 2 1.3
529280 data/Sounds/Paradigm3/S3_Sound_Speech4.wav 3 1.3
529280 data/Sounds/Paradigm3/S3_Sound_Water2.wav 3 1.3
529280 data/Sounds/Paradigm3/S3_Sound_Speech5.wav 4 1.3
529280 data/Sounds/Paradigm3/S3_Sound_Water4.wav 4 1.3
529280 data/Sounds/Paradigm3/S3_Sound_Speech6.wav 5 1.3
529280 data/Sounds/Paradigm3/S3_Sound_Fire1.wav 5 1.3
529280 data/Sounds/Paradigm3/S3_Sound_Water5.wav 6 1.3
529280 data/Sounds/Paradigm3/S3_Sound_Water3.wav 6 1.3
529280 data/Sounds/Paradigm3/S3_Sound_Fire4.wav 7 1.3
[... 89 more lines not kept]
```

**Agent**

No tone-pip or raw-voltage recordings in the archive (only aMUA rasters), and the model sounds come first in the stream. Next: read the paper's MATLAB code and inspect one neural file.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > peek.py <<'EOF'
import fsspec, tarfile, io, scipy.io as sio, numpy as np
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-2/live/data.tar.gz"
f=fsspec.open(url, block_size=2**24).open()
tf=tarfile.open(fileobj=f, mode="r|gz")
import os
os.makedirs("code",exist_ok=True)
for m in tf:
    if m.name.endswith(".m") or m.name.endswith(".docx"):
        open("code/"+os.path.basename(m.name),"wb").write(tf.extractfile(m).read())
    if m.name.endswith("S1_Sound_Fire.wav") or m.name.endswith("Speech/Sound_1.wav") or m.name.endswith("Fig7/Water_1.wav"):
        b=tf.extractfile(m).read(); print(m.name, b[:44])
    if m.name.endswith("P3_Site09.mat"):
        b=tf.extractfile(m).read()
        print(b[:128])
        d=sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)
        D=d['Data']; print(d.keys(), D._fieldnames)
        print(D.Param._fieldnames, [getattr(D.Param,k) for k in D.Param._fieldnames])
        s=D.Sound; print(type(s), np.shape(s)); e=s[0].Exemplar; print(np.shape(e)); c=e[0].Channel; print(np.shape(c), c[0]._fieldnames)
        for k in range(3):
            for l in range(6):
                ch=s[k].Exemplar[l].Channel
                print(k,l,[np.shape(x.RAS) for x in ch][:2], ch[0].Fs, ch[0].RAS.dtype, float(ch[0].RAS.min()), float(ch[0].RAS.max()), float(ch[0].RAS.mean()))
        break
EOF
python peek.py; ls code
```

```
data/Sounds/Paradigm1/S1_Sound_Fire.wav b'RIFFx\x13\x08\x00WAVEfmt \x10\x00\x00\x00\x03\x00\x01\x00D\xac\x00\x00\x10\xb1\x02\x00\x04\x00 \x00fact\x04\x00\x00\x00'
data/Sounds/ModelSounds/Human_Speech/Sound_1.wav b'RIFFtu\r\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00D\xac\x00\x00\x88X\x01\x00\x02\x00\x10\x00dataPu\r\x00'
data/Code/Examples/ExampleSounds/Fig7/Water_1.wav b'RIFFp2$\x04WAVEfmt \x10\x00\x00\x00\x01\x00\x02\x00\x00w\x01\x00\x00\xca\x08\x00\x06\x00\x18\x00bextZ\x03\x00\x00'
b'MATLAB 7.3 MAT-file, Platform: MACI64, Created on: Tue Aug 13 18:01:06 2019 HDF5 schema 1.00 .                      \x00\x00\x00\x00\x00\x00\x00\x00\x00\x02IM'
Traceback (most recent call last):
  File "/tmp/claude-1001/peek.py", line 15, in <module>
    d=sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/scipy/io/matlab/_mio.py", line 241, in loadmat
    MR, _ = mat_reader_factory(f, **kwargs)
            ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/scipy/io/matlab/_mio.py", line 76, in mat_reader_factory
    raise NotImplementedError('Please use HDF reader for matlab v7.3 '
                              'files, e.g. h5py')
NotImplementedError: Please use HDF reader for matlab v7.3 files, e.g. h5py
FigureData.docx
ModelExample.m
NeuralExample.m
bandpass.m
cochleogram.m
cochleogramdyncorr.m
[... 16 more lines not kept]
```

**Agent**

Neural files are MATLAB 7.3 (HDF5). Reading the code:

**Agent calls Bash**

```bash
cd $TMPDIR/code && cat NeuralExample.m rastermuashuffledxcovwinfastN.m
```

```
%%
% This routine takes data from an example recording location and generates
% the signal and noise correlograms (both for temporal and spectral) from the
% multi-channel and multi-trial MUA responses as described in Sadeghi et al
% PLOS Bio 2019
%
% The example used is the sam as Fig. 1. The routine generates Panels
% B-M of that figure
%
% (C) X. Zhai & M.A. Escabi (2019)
%

%Load data for paradigm 1 site 04
load('../../NeuralData/Paradigm1/P1_Site04.mat', 'Data')

%Some parameters
RASNFire=Data.Sound(1);                 %Fire sound response
RASNWater=Data.Sound(4);                %Water sound response
NChan=length(RASNFire.Channel);         %16 channel
Fsd=RASNFire.Channel(1).Fs;             %Raster sampling rate
[... 322 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && cat rastermuashuffledxcovwinfast.m; grep -v "^\s*%" rastermuashuffledxcorrwinfast.m | head -80
```

```
%
%function [CovWinData]=rastermuashuffledxcovwinfast(RAS1,RAS2,Fsd,T0,Tw,MaxTau,Mean,Diag,DiagVar)
%
%   FILE NAME       : RASTER MUA SHUFFLED XCOV WIN FAST
%   DESCRIPTION     : Windowed shuffled crosscorrelation covariance using raster data 
%                     of MUA. The correlation is computed only for a
%                     windowed segment of the Raster. The window is
%                     centered at position T0 and has a duration Tw. For
%                     simplicity we are using a square window.
%
%	RAS1            : Rastergram 1 (NTrials x SamplePoints, pre-loaded using "LOADMUARAS")
%   RAS2            : Rastergram 2 (NTrials x SamplePoints, pre-loaded using "LOADMUARAS")
%   Fsd             : Sampling rate of raster to compute raster-corr (pre-loaded using "LOADMUARAS"). 
%   T0              : Window center time point (msec).
%   Tw              : Window duration in msec. For the winow correlation to
%                     work it is required that the window not overlap the
%                     delay region at the edges (to avoid edge artifacts).
%                     This explicitly requires that
%
%                       T0+TW/2 < T - MaxLag
[... 162 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -v "^\s*%" rastermuashuffledxcorrwinfast.m | sed -n 80,200p
```

```
E2Diag1 = E2Diag1 + RAS1(k,:)*RAS1(k,:)'/(Nw-1);                   %Diagonal terms for RAS1
         E2Diag2 = E2Diag2 + xcorr(W.^2,RAS2(k,:).^2,MaxLag)/(Nw-1);        %Diagonal terms for RAS2, delay dependent
    end
    Var1 = E21 - M1.^2 - (E2Diag1 - M2Diag1);
    Var2 = E22 - M2.^2 - (E2Diag2 - M2Diag2);
    
    Var1 = Var1/NT1/(NT1-1);                  %Normalizing by number of trials - diagonal removed
    Var2 = Var2/NT1/(NT1-1);                  %Normalizing by number of trials - diagonal removed
    E21  = E21/NT1/(NT1-1); 
    E22  = E22/NT1/(NT1-1);
    M1=M1/NT1;
    M2=M2/NT1;
else
    Var1= (E21-M1^2)/NT1^2;                     %Normalizing by number of trials - variance from diagonal and nondiagonal terms - nondiagonal contribute most (N*(N-1) versus N)
    Var1diag= (E21diag*NT1-M1^2)/NT1^2;         %Normalizing by number of trials - variance of diagonal terms - contains both singal and noise correlations for a given trial
    Var2= (E22-M2.^2)/NT1^2;                    %Normalizing by number of trials - variance from diagonal and nondiagonal terms - nondiagonal contribute most (N*(N-1) versus N)
    Var2diag= (E22diag*NT1-M2.^2)/NT1^2;        %Normalizing by number of trials - variance of diagonal terms - contains both singal and noise correlations for a given trial
    E21 = E21/NT1^2; 
    E22 = E22/NT1^2;
    M1=M1/NT1;
[... 36 more lines not kept]
```

**Agent**

Core neural correlation code is clear; I'll port it to numpy. Now the auditory-model code.

**Agent calls Bash**

```bash
cd $TMPDIR/code && grep -v "^\s*%%%" ModelExample.m | head -150
```

```
%%
% This routine illustrates how to generate the dynamic short-term 
% correlations (spectral, temporal, spectro-temporal) of a sound as 
% described in Sedaghi et al PLOS Bio 2019.
%
% The example used is the sam as Fig. 5. The routine generates Panels
% A-H of that figure
%
% (C) M. Sadeghi & M.A. Escabi (2019)
%


clear all

%Parameters
SoundName='./ExampleSounds/Fig7/Speech_1';
dx=1/8;     %Spacing between Spectral Filters
f1=100;     %Lower frequency to compute spectral decomposition
fN=16000;   %Upper frequency to compute spectral decomposition
Fm=500;     %Maximum Modulation frequency 
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code && for f in cochleogram.m cochleogramdyncorr.m xcorrst.m gammatonefilter.m lowpass.m h.m criticalbandwidth.m erb.m bandpass.m fdesignkdt.m fdesignh.m finddtdfw.m xcorrstsym.m; do echo "=== $f"; grep -v "^\s*%" $f | grep -v "^\s*$"; done
```

```
=== cochleogram.m
function [CochData]=cochleogram(data,Fs,dX,f1,fN,Fm,OF,Norm,dis,ATT,FilterType,BWType)
if nargin<8 | isempty(Norm)
    Norm='Amp';         %MAE, May 2018
end
if nargin<9 | isempty(dis)
	dis='n';
end
if nargin<10 | isempty(ATT)
	ATT=60;
end
if nargin<11 | isempty(FilterType)
   FilterType='GammaTone'; 
end
if nargin<12 | isempty(BWType)  %Added ERB as default, March 2019
    BWType='erb';
end
X1=0;
XN=log2(fN/f1);
L=floor(XN/dX);
[... 337 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > peek2.py <<'EOF'
import fsspec, tarfile, io, h5py, numpy as np, time
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-2/live/data.tar.gz"
f=fsspec.open(url, block_size=2**24).open()
tf=tarfile.open(fileobj=f, mode="r|gz")
for m in tf:
    if m.name.endswith("P3_Site09.mat"):
        b=tf.extractfile(m).read(); break
h=h5py.File(io.BytesIO(b),'r')
def show(g,ind=0):
    for k,v in g.items():
        print(' '*ind+k, type(v).__name__, getattr(v,'shape',''), getattr(v,'dtype',''), dict(v.attrs) if len(v.attrs)<4 else list(v.attrs))
        if isinstance(v,h5py.Group) and ind<6: show(v,ind+2)
show(h)
D=h['Data']
P=D['Param']
for k in P: 
    x=P[k][()]; print(k, x.dtype, x.shape, x.ravel()[:20])
S=D['Sound']; print(list(S.keys()))
ex=S['Exemplar']; print(ex.shape, ex.dtype)
r=h[ex[0,0]]; print(list(r.keys()))
ch=r['Channel']; print(ch.shape)
c0=h[ch[0,0]]; print(list(c0.keys()) if isinstance(c0,h5py.Group) else c0)
EOF
python peek2.py
```

```
<persisted-output>
Output too large (65.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/e9eb191a-8d7b-4aaf-a4ab-b5af6e6452e6/tool-results/b65gdp3e0.txt

Preview (first 2KB):
#refs# Group   {}
  0 Dataset (1, 1) float64 {'H5PATH': np.bytes_(b'/#refs#/0'), 'MATLAB_class': np.bytes_(b'double')}
  0b Dataset (1, 1) float64 {'H5PATH': np.bytes_(b'/#refs#/0b'), 'MATLAB_class': np.bytes_(b'double')}
  0c Dataset (1, 1) float64 {'H5PATH': np.bytes_(b'/#refs#/0c'), 'MATLAB_class': np.bytes_(b'double')}
  0d Dataset (6104, 20) float64 {'H5PATH': np.bytes_(b'/#refs#/0d'), 'MATLAB_class': np.bytes_(b'double')}
  0e Dataset (6104, 20) float64 {'H5PATH': np.bytes_(b'/#refs#/0e'), 'MATLAB_class': np.bytes_(b'double')}
  0f Dataset (6104, 20) float64 {'H5PATH': np.bytes_(b'/#refs#/0f'), 'MATLAB_class': np.bytes_(b'double')}
  0g Group   {'H5PATH': np.bytes_(b'/#refs#/0g'), 'MATLAB_class': np.bytes_(b'struct'), 'MATLAB_fields': array([array([b'R', b'A', b'S'], dtype='|S1'),
       array([b'F', b's'], dtype='|S1')], dtype=object)}
    Fs Dataset (16, 1) object {}
    RAS Dataset (16, 1) object {}
  0h Dataset (1, 1) float64 {'H5PATH': np.bytes_(b'/#refs#/0h'), 'MATLAB_class': np.bytes_(b'double')}
  0i Dataset (1, 1) float64 {'H5PATH': np.bytes_(b'/#refs#/0i'), 'MATLAB_class': np.bytes_(b'double')}
  1 Dataset (1, 1) float64 {'H5PATH': np.bytes_(b'/#refs#/1'), 'MATLAB_class': np.bytes_(b'double')}
  1b Dataset (6104, 20) float64 {'H5PATH': np.bytes_(b'/#refs#/1b'), 'MATLAB_class': np.bytes_(b'double')}
  1c Dataset (6104, 20) float64 {'H5PATH': np.bytes_(b'/#refs#/1c'), 'MATLAB_class': np.bytes_(b'double')}
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v "^  [0-9a-zA-Z]* \|^    \(Fs\|RAS\)" /home/runner/.claude/projects/-home-runner-work-encore-encore/e9eb191a-8d7b-4aaf-a4ab-b5af6e6452e6/tool-results/b65gdp3e0.txt | head -60
```

```
#refs# Group   {}
Data Group   {'MATLAB_class': np.bytes_(b'struct'), 'MATLAB_fields': array([array([b'S', b'o', b'u', b'n', b'd'], dtype='|S1'),
AnimalNo uint16 (7, 1) [48 52 49 55 48 49 53]
BlockNo uint16 (3, 1) [48 52 55]
RecordDate uint16 (7, 1) [ 77  97 121  50  48  49  57]
['Exemplar']
(3, 1) object
['Channel']
(6, 1)
['Fs', 'RAS']
```

**Agent**

Rasters are stored samples x trials (6104 x 20 at 2 kHz). Now reading the paper's Methods on the neural classifier, the correlations and the SNR.

**Agent calls Bash**

```bash
cd paper && wc -c *.txt; grep -n "^#\|^[A-Z][a-z].*$" 10.1371-journal.pbio.3000449.txt | awk 'length($0)<90' | head -80
```

```
188735 10.1371-journal.pbio.3000449.txt
 11411 bst-2.data-description.txt
200146 total
2:Version: version of record, PMC6788721 (open access)
3:Source: europepmc fullTextXML
4:Stored: 2026-11-06
5:Extracted: JATS XML flattened
9:## Abstract
13:## Introduction
21:## Results
23:## Decoding neural ensemble correlation statistics to recognize sounds
31:## Neural ensemble correlation statistics for an auditory midbrain penetration site.
45:## Average stimulus-driven and noise-driven neural correlations.
53:## Using neural ensemble correlation statistics to identify sounds.
61:## Differences in correlations statistics are not due to sound spectrum alone
79:## Correlation statistics of natural and man-made sound categories
83:## Average correlation statistics and diversity
89:## Measuring the average correlation structure of natural sounds.
97:## Sound-correlation statistics for the 13 sound categories and white noise.
103:## Short-term correlation statistics and stationarity
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 21,60p 10.1371-journal.pbio.3000449.txt
```

```
## Results

## Decoding neural ensemble correlation statistics to recognize sounds

We used multichannel, multiunit neural recordings in the auditory midbrain (IC) of unanesthetized rabbits to characterize and determine whether neural correlations between recording sites in the IC are affected by the correlation structure of natural sounds and whether such neural ensemble statistics could potentially contribute to sound recognition.

The spatiotemporal correlation statistics from an example penetration site demonstrate the diversity of neural ensemble correlation statistics observed in a frequency-organized recording site. As expected for the principal nucleus of the IC, frequency responses areas are tonotopically organized, varying from low to high frequency with recording depth ( Fig 1A ; approximately 0.5–8 kHz; low frequencies more dorsal, high frequencies more ventral), and, for this reason, spatial correlations are referred to as spectral correlations in what follows. Response neurograms (averaged across trials) are shown for a fire sound ( Fig 1B ) and a water sound ( Fig 1E ) for this recording site, and the stimulus-driven ensemble correlations are estimated by correlating the outputs of each recording channel across independent response trials ( Fig 1C, 1D, 1F and 1G ; Materials and Methods). In general, neural correlation statistics to natural sound are highly diverse across sounds. The stimulus-driven spectral correlation matrix (at zero time lag) reflects the instantaneous correlation of the neural activity between different frequency-organized recording sites ( Fig 1C for fire; 1F for water; cochleograms and corresponding neural activity patterns are shown for this site in S1 Fig ). In contrast, the trial-shuffled autocorrelograms for each recording site reflect the temporal correlation structure of the neural activity at different recording locations ( Fig 1D for fire; 1G for water).

Neural ensemble correlation statistics for an auditory midbrain pen
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 213,300p 10.1371-journal.pbio.3000449.txt
```

```
## Sound paradigm 1

Next, across N = 13 recording locations ( N = 4 and 9 across two animals), we delivered a sequence of five environmental noises with distinct structural properties to determine whether the ensemble activity of the auditory midbrain reflected frequency-dependent correlation statistics present in the sounds and to determine whether such neural population statistics can be used identify the individual sounds. Each sound is 3 s duration and is delivered in a block-randomized fashion with a 100-ms interstimulus interval between sounds. To avoid broadband transients, the sounds have b-spline onset and offset ramps (20 ms rise–decay time) and are delivered at an RMS SPL of 65 dB RMS SPL; 87 dB peak SPL over all sounds. Each recording had 5 sound conditions in which each sound had at least 18 trials (range 18–39), with a 3-s duration for each trial. The sounds included crackling fire, bird chorus, outdoor crowd, running water, and a rattling snake sound. These sounds each contain unique time-frequency correlation statistics, allowing us to test and quantify whether such statistics are potentially encoded by the auditory midbrain and ultimately represented in the neural ensemble activity. For instance, the water sounds have minimal across-frequency channel correlation because the air bubbles and droplets responsible for this sound are relatively narrow-band and occur randomly in time, thus activating frequency channels independently [ 8 ]. Sounds such as crackling fire, by comparison, have strong frequency-dependent correlations because of crackling embers, which produced brief impulsive “pops” that span multiple frequency channels simultaneously. The temporal correlations of these five sounds are also quite varied. For instance, the water sound has a very brief impulsive correlation structure lasting just a few milliseconds, whereas the bird chorus and the outdoor crowd, which contains multispeaker speech babble, have a broader and slower temporal corre
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; sed -n 300,372p paper/10.1371-journal.pbio.3000449.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Clock is 20:02, so about 4 h of work time. Writing the helper.

**Agent calls Write**

```json
{
 "file_path": "entries/sadeghi-2019/sadeghi.py",
 "content": "\"\"\"Loading and measures for Sadeghi, Zhai, Stevenson & Escabi (2019) on CRCNS bst-2.\n\nThe data set is one gzip-compressed tar file (bst-2/live/data.tar.gz, 5.3 GB) in the public\nS3 bucket crcnsarchive. A gzip stream cannot be read at random, so `stream_members` reads it\nonce from the start over HTTP and hands each wanted member to the caller in memory; nothing\nis written to disk. The neural files are MATLAB 7.3 (HDF5) files, read with h5py from memory.\n\nWhere each parameter comes from:\n\n- Correlations (`window_corr`) port the paper's own MATLAB code in the data set,\n  Code/MUACorrAnalysis/rastermuashuffledxcorrwinfast.m and rastermuashuffledxcovwinfast.m\n  (Materials and methods, \"Neural ensemble stimulus-driven correlation\" and \"Neural ensemble\n  noise correlation\", whose equations the text lost): square window of Nw samples centred at\n  T0, PSTH-based shuffled correlogram with the within-trial terms removed, noise correlogram\n  as unshuffled minus shuffled, all normalised by the unshuffled (signal plus noise) variances\n  (R12_sh, R12_ush, R12_noise of the code). Maximum delay 100 ms (Noiseless neural classifier,\n  paragraph 6, and NeuralExample.m).\n- Single-trial correlations (`single_trial_features`) are the same code applied to one trial\n  with the within-trial terms kept (the \"unshuffled correlations for individual trials\" of\n  \"Single-trial neural classifier\").\n- Classifier (`classify`): half split, 1000 ms model windows for the single-trial and 500 ms\n  for the noiseless classifier, validation windows of 62.5 to 1000 ms in half octave steps,\n  100 random time samples, PCA fitted on the model data, naive Bayes with axis-aligned\n  Gaussians, equal priors, MAP (claims file, opening comment, citing \"Noiseless neural\n  classifier\" and \"Single-trial neural classifier\"). The readings (1) to (5) of the claims file\n  are options of `classify`. The PC grid (1 to 40) and the variance floor of the Gaussians\n  (1e-9 of the largest feature variance, as scikit-learn's GaussianNB) are standard choices.\n- Random seeds are standard choices; each caller passes its own generator.\n\"\"\"\nimport io\nimport tarfile\n\nimport fsspec\nimport h5py\nimport numpy as np\n\nURL = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-2/live/data.tar.gz\"\nP1_SOUNDS = [\"fire\", \"bird\", \"crowd\", \"water\", \"snake\"]  # data description, paradigm 1\nP3_CATEGORIES = [\"fire\", \"water\", \"speech\"]  # data description, paradigm 3\nDURATIONS_MS = 62.5 * 2 ** (np.arange(9) / 2)  # 62.5 to 1000 ms in half octave steps\nFS = 2000.0  # aMUA sampling rate (Electrophysiology, paragraph 3); checked against the files' Fs\n\n\ndef stream_members(want, url=URL, block_size=2**24):\n    \"\"\"Yield (name, bytes) for each tar member for which want(name) is true, streaming once.\"\"\"\n    f = fsspec.open(url, block_size=block_size).open()\n    tf = tarfile.open(fileobj=f, mode=\"r|gz\")\n    for m in tf:\n        if m.isfile() and want(m.name):\n            yield m.name, tf.extractfile(m).read()\n    f.close()\n\n\ndef _chars(ds):\n    return \"\".join(chr(c) for c in np.asarray(ds[()]).ravel())\n\n\ndef _channels(h, group_ref):\n    \"\"\"Read a Channel struct array: returns (rasters list of (trials, samples) float32, fs list).\"\"\"\n    g = h[group_ref]\n    ras = [np.asarray(h[r][()], dtype=np.float32).T for r in g[\"RAS\"][()].ravel()]\n    fs = [float(np.asarray(h[r][()]).ravel()[0]) for r in g[\"Fs\"][()].ravel()]\n    return ras, fs\n\n\ndef read_site(name, raw):\n    \"\"\"Parse one P<x>_Site<zz>.mat file. Returns a dict with param, fs and\n    ras[(a, b)] = array (16 channels, trials, samples), where (a, b) is (sound, 0) for\n    paradigm 1, (sound, condition) for paradigm 2 (condition 0 = 1/f, 1 = original; data\n    description) and (category, exemplar) for paradigm 3, all indices from 0.\"\"\"\n    h = h5py.File(io.BytesIO(raw), \"r\")\n    D = h[\"Data\"]\n    P = D[\"Param\"]\n    out = {\"name\": name.split(\"/\")[-1][:-4],\n           \"param\": {k: _chars(P[k]) for k in P.keys()}, \"ras\": {}, \"fs\": set(), \"ntrials_ch\": {}}\n    snd = D[\"Sound\"]\n    sub = [k for k in snd.keys()][0]  # 'Channel', 'Condition' or 'Exemplar'\n    for a, ref in enumerate(snd[sub][()].ravel()):\n        if sub == \"Channel\":\n            items = [(0, ref, True)]\n        else:\n            g = h[ref]\n            items = [(b, r, False) for b, r in enumerate(g[\"Channel\"][()].ravel())]\n        for b, r, direct in items:\n            if direct:\n                ras, fs = _channels(h, snd.ref) if False else _channels_direct(h, snd, a)\n            else:\n                ras, fs = _channels(h, r)\n            nt = [x.shape[0] for x in ras]\n            ns = [x.shape[1] for x in ras]\n            out[\"ntrials_ch\"][(a, b)] = nt\n            n, s = min(nt), min(ns)\n            out[\"ras\"][(a, b)] = np.stack([x[:n, :s] for x in ras])\n            out[\"fs\"].update(fs)\n    h.close()\n    return out\n\n\ndef _channels_direct(h, snd, a):\n    \"\"\"Paradigm 1: Data.Sound(k).Channel(m) is stored as a struct array whose field\n    'Channel' holds one reference per sound to a Channel struct array.\"\"\"\n    ref = snd[\"Channel\"][()].ravel()[a]\n    return _channels(h, ref)\n\n\n# ---------------------------------------------------------------- correlations (paper's code)\n\ndef _xcorr(a, b, maxlag):\n    \"\"\"MATLAB xcorr(a, b, maxlag) along the last axis: R(m) = sum_n a(n+m) b(n), m = -maxlag..maxlag.\"\"\"\n    n = a.shape[-1]\n    nfft = 1 << int(np.ceil(np.log2(2 * n)))\n    A = np.fft.rfft(a, nfft)\n    B = np.fft.rfft(b, nfft)\n    r = np.fft.irfft(A * np.conj(B), nfft)\n    return np.concatenate([r[..., nfft - maxlag:], r[..., :maxlag + 1]], axis=-1)\n\n\ndef window_geometry(T0_ms, Tw_ms, maxtau_ms=100.0, fs=FS):\n    maxlag = int(np.ceil(maxtau_ms / 1000 * fs))\n    N0 = int(round(T0_ms / 1000 * fs))\n    Nw = int(np.floor(fs * Tw_ms / 1000 / 2) * 2 + 1)\n    N1 = N0 - int(np.ceil(Nw / 2)) - maxlag\n    N2 = N0 + int(np.ceil(Nw / 2)) + maxlag\n    return maxlag, Nw, N1 - 1, N2  # python slice [N1-1:N2] equals MATLAB N1:N2\n\n\ndef window_corr(R1, R2, T0_ms, Tw_ms, maxtau_ms=100.0, fs=FS):\n    \"\"\"Port of rastermuashuffledxcorrwinfast + rastermuashuffledxcovwinfast with\n    Mean='y', Diag='y', DiagVar='n'. R1, R2: (..., trials, samples); leading axes broadcast.\n    Returns dict of R12_sh, R12_ush, R12_noise over lags -maxlag..maxlag (last axis).\"\"\"\n    maxlag, Nw, s0, s1 = window_geometry(T0_ms, Tw_ms, maxtau_ms, fs)\n    if s0 < 0 or s1 > R1.shape[-1]:\n        raise ValueError(\"window plus lags outside the raster\")\n    X = R1[..., s0:s1].astype(np.float64)\n    Y = R2[..., s0:s1].astype(np.float64)\n    L = X.shape[-1]\n    Nw2 = (Nw - 1) // 2\n    c = (L - 1) // 2\n    W = np.zeros(L)\n    W[c - Nw2:c + Nw2 + 1] = 1.0\n    X = X * W\n    NT = X.shape[-2]\n    P1 = X.sum(-2)\n    P2 = Y.sum(-2)\n    FX = np.fft.rfft(X, 1 << int(np.ceil(np.log2(2 * L))))\n    FY = np.fft.rfft(Y, FX.shape[-1] * 2 - 2)\n    nfft = FX.shape[-1] * 2 - 2\n\n    def back(F):\n        r = np.fft.irfft(F, nfft)\n        return np.concatenate([r[..., nfft - maxlag:], r[..., :maxlag + 1]], axis=-1)\n\n    R12 = back(FX.sum(-2) * np.conj(FY.sum(-2)))\n    Rdiag = back((FX * np.conj(FY)).sum(-2))\n    R12 = R12 - Rdiag\n    R12noise = Rdiag / NT / Nw - R12 / NT / (NT - 1) / Nw\n    R12 = R12 / NT / (NT - 1) / Nw\n    R12diag = Rdiag / NT / Nw\n    M1 = P1.sum(-1) / Nw\n    E21diag = (X ** 2).sum((-1, -2)) / (Nw - 1)\n    M2 = _xcorr(np.broadcast_to(W, P2.shape), P2, maxlag) / Nw\n    E22diag = _xcorr(np.broadcast_to(W, Y.shape), Y ** 2, maxlag).sum(-2) / (Nw - 1)\n    Var1diag = (E21diag * NT - M1 ** 2) / NT ** 2\n    Var2diag = (E22diag * NT - M2 ** 2) / NT ** 2\n    M1 = M1 / NT\n    M2 = M2 / NT\n    R12 = R12 - M1[..., None] * M2\n    R12diag = R12diag - M1[..., None] * M2\n    den = np.sqrt(Var1diag[..., None] * Var2diag)\n    return {\"sh\": R12 / den, \"ush\": R12diag / den, \"noise\": R12noise / den,\n            \"tau_ms\": np.arange(-maxlag, maxlag + 1) / fs * 1000}\n\n\ndef site_correlations(ras, T0_ms, Tw_ms, maxtau_ms=100.0):\n    \"\"\"Spectral (zero-lag, channels x channels) and temporal (channels x lags) shuffled,\n    unshuffled and noise correlations for ras (channels, trials, samples).\"\"\"\n    C = ras.shape[0]\n    tem = window_corr(ras, ras, T0_ms, Tw_ms, maxtau_ms)\n    spec = {}\n    zl = None\n    for k in range(C):\n        r = window_corr(ras[k][None], ras, T0_ms, Tw_ms, 0.0)  # lag 0 only, channel k against all\n        for key in (\"sh\", \"ush\", \"noise\"):\n            spec.setdefault(key, np.zeros((C, C)))[k] = r[key][:, 0]\n    return {\"spec\": spec, \"temp\": {k: tem[k] for k in (\"sh\", \"ush\", \"noise\")}, \"tau_ms\": tem[\"tau_ms\"]}\n\n\ndef whole_window(nsamples, maxtau_ms=100.0, fs=FS):\n    \"\"\"Window over the whole response, as NeuralExample.m sets it for a half raster:\n    T0 at the centre, Tw = (NS - 2 MaxLag - 2) samples.\"\"\"\n    maxlag = int(np.ceil(maxtau_ms / 1000 * fs))\n    T0 = np.floor(nsamples / fs * 1000 / 2)\n    Tw = np.floor((nsamples - maxlag * 2 - 2) / fs * 1000) - 2\n    return T0, Tw\n\n\n# ---------------------------------------------------------------- single-trial features\n\ndef _single(seg, Nw, maxlag):\n    \"\"\"seg: (channels, L) one trial, L = Nw + 2 + 2 maxlag. Code formulas with NT = 1 and\n    the within-trial terms kept (unshuffled correlation). Returns spectral (C, C) zero-lag\n    and temporal (C, 2 maxlag + 1) autocorrelations, and the window mean of each channel.\"\"\"\n    L = seg.shape[-1]\n    Nw2 = (Nw - 1) // 2\n    c = (L - 1) // 2\n    x = seg[:, c - Nw2:c + Nw2 + 1]\n    M1 = x.sum(-1) / Nw\n    E21 = (x ** 2).sum(-1) / (Nw - 1)\n    var1 = E21 - M1 ** 2\n    # spectral, lag 0\n    R0 = x @ x.T / Nw\n    spec = (R0 - np.outer(M1, M1)) / np.sqrt(np.outer(var1, var1))\n    # temporal, lags -maxlag..maxlag, shifted windows of the same channel\n    W = np.zeros(L)\n    W[c - Nw2:c + Nw2 + 1] = 1\n    R = _xcorr(seg * W, seg, maxlag) / Nw\n    cs = np.concatenate([np.zeros((seg.shape[0], 1)), np.cumsum(seg, -1)], -1)\n    cs2 = np.concatenate([np.zeros((seg.shape[0], 1)), np.cumsum(seg ** 2, -1)], -1)\n    lags = np.arange(-maxlag, maxlag + 1)\n    st = (c - Nw2) - lags  # window over b shifted: indices j - m\n    M2 = (cs[:, st + Nw] - cs[:, st]) / Nw\n    E22 = (cs2[:, st + Nw] - cs2[:, st]) / (Nw - 1)\n    var2 = E22 - M2 ** 2\n    temp = (R - M1[:, None] * M2) / np.sqrt(var1[:, None] * var2)\n    return spec, temp, M1\n\n\ndef single_trial_features(ras, n, Tw_ms, t_range_ms, rng, maxtau_ms=100.0, trial_pool=None):\n    \"\"\"n random (trial, time) samples; each a single-trial window of Tw_ms centred at a\n    random time whose window plus lags lie inside t_range_ms = (start, end) of the raster.\n    Returns spec (n, C*(C-1)/2) upper triangle without the diagonal (equal to 1 for one\n    trial), temp (n, C, lags), rate (n, C).\"\"\"\n    C, NT, NS = ras.shape\n    maxlag = int(np.ceil(maxtau_ms / 1000 * FS))\n    Nw = int(np.floor(FS * Tw_ms / 1000 / 2) * 2 + 1)\n    L = Nw + 2 + 2 * maxlag\n    lo = int(round(t_range_ms[0] / 1000 * FS))\n    hi = int(round(t_range_ms[1] / 1000 * FS)) - L\n    iu = np.triu_indices(C, 1)\n    pool = np.arange(NT) if trial_pool is None else np.asarray(trial_pool)\n    trials = rng.choice(pool, n)\n    starts = rng.integers(lo, hi + 1, n)\n    S = np.empty((n, len(iu[0])))\n    T = np.empty((n, C, 2 * maxlag + 1))\n    Rt = np.empty((n, C))\n    for i in range(n):\n        seg = ras[:, trials[i], starts[i]:starts[i] + L].astype(np.float64)\n        s, t, m = _single(seg, Nw, maxlag)\n        S[i] = s[iu]\n        T[i] = t\n        Rt[i] = m\n    return {\"spec\": S, \"temp\": T, \"rate\": Rt}\n\n\ndef shuffled_features(ras, n, Tw_ms, t_range_ms, rng, maxtau_ms=100.0):\n    \"\"\"Noiseless classifier features: shuffled (stimulus-driven) correlations over all trials\n    (window_corr R12_sh), n random window centres. spec: upper triangle with diagonal.\"\"\"\n    C, NT, NS = ras.shape\n    maxlag, Nw, _, _ = window_geometry(0, Tw_ms, maxtau_ms)\n    half = (Nw + 1) / 2 + maxlag + 1\n    lo = t_range_ms[0] + half / FS * 1000\n    hi = t_range_ms[1] - half / FS * 1000\n    iu = np.triu_indices(C)\n    S, T = [], []\n    for t0 in rng.uniform(lo, hi, n):\n        t0 = round(t0 * FS / 1000) / FS * 1000\n        tem = window_corr(ras, ras, t0, Tw_ms, maxtau_ms)[\"sh\"]\n        _, Nw_, s0, s1 = window_geometry(t0, Tw_ms, 0.0)\n        X = ras[:, :, s0:s1].astype(np.float64)\n        sp = _shuffled_zero_lag(X)\n        S.append(sp[iu])\n        T.append(tem)\n    return {\"spec\": np.array(S), \"temp\": np.array(T)}\n\n\ndef _shuffled_zero_lag(X):\n    \"\"\"Zero-lag R12_sh of the code for all channel pairs at once; X (C, NT, Nw+2) with the\n    square window of Nw samples in the middle (MaxLag = 0).\"\"\"\n    C, NT, L = X.shape\n    Nw = L - 2\n    W = np.zeros(L)\n    W[1:-1] = 1\n    X = X * W\n    P = X.sum(1)\n    R12 = P @ P.T\n    Rdiag = np.einsum(\"ktn,ltn->kl\", X, X)\n    R12 = (R12 - Rdiag) / NT / (NT - 1) / Nw\n    M1 = P.sum(-1) / Nw\n    E2diag = (X ** 2).sum((1, 2)) / (Nw - 1)\n    var = (E2diag * NT - M1 ** 2) / NT ** 2\n    M1 = M1 / NT\n    return (R12 - np.outer(M1, M1)) / np.sqrt(np.outer(var, var))\n\n\n# ---------------------------------------------------------------- classifier\n\nclass GaussNB:\n    \"\"\"Naive Bayes with axis-aligned Gaussian likelihoods and equal priors.\"\"\"\n\n    def fit(self, X, y):\n        self.classes = np.unique(y)\n        self.mu = np.array([X[y == c].mean(0) for c in self.classes])\n        v = np.array([X[y == c].var(0) for c in self.classes])\n        self.var = v + 1e-9 * X.var(0).max()\n        return self\n\n    def loglik(self, X):\n        \"\"\"(n, classes) log-likelihoods.\"\"\"\n        return -0.5 * (((X[:, None, :] - self.mu) ** 2) / self.var + np.log(2 * np.pi * self.var)).sum(-1)\n\n\nclass PCA:\n    def fit(self, X):\n        self.mean = X.mean(0)\n        U, s, Vt = np.linalg.svd(X - self.mean, full_matrices=False)\n        self.comp = Vt\n        self.evr = s ** 2 / (s ** 2).sum()\n        return self\n\n    def transform(self, X, k):\n        return (X - self.mean) @ self.comp[:k].T\n\n\ndef flat(f, kind):\n    if kind == \"temp\":\n        return f[\"temp\"].reshape(len(f[\"temp\"]), -1)\n    return f[kind]\n\n\ndef loglik_grid(Xm, ym, Xv, kmax=40):\n    \"\"\"Log-likelihoods of validation features for every number of PCs 1..kmax.\n    Returns array (kmax, n_val, classes).\"\"\"\n    p = PCA().fit(Xm)\n    kmax = min(kmax, Xm.shape[1], Xm.shape[0] - 1)\n    Zm = p.transform(Xm, kmax)\n    Zv = p.transform(Xv, kmax)\n    out = []\n    for k in range(1, kmax + 1):\n        nb = GaussNB().fit(Zm[:, :k], ym)\n        out.append(nb.loglik(Zv[:, :k]))\n    return np.array(out)\n\n\ndef log_posterior(ll):\n    m = ll.max(-1, keepdims=True)\n    return ll - (m + np.log(np.exp(ll - m).sum(-1, keepdims=True)))\n"
}
```

```
File created successfully at: entries/sadeghi-2019/sadeghi.py (file state is current in your context — no need to Read it back)
```

**Agent**

Cleaning up a leftover in `read_site`:

**Agent calls Bash**

```bash
cd entries/sadeghi-2019 && python3 - <<'EOF'
s=open('sadeghi.py').read()
old=s[s.index('    for a, ref in enumerate(snd[sub][()].ravel()):'):s.index('    h.close()\n    return out')]
new='''    for a, ref in enumerate(snd[sub][()].ravel()):
        if sub == "Channel":
            items = [(0, ref)]
        else:
            items = list(enumerate(h[ref]["Channel"][()].ravel()))
        for b, r in items:
            ras, fs = _channels(h, r)
            nt = [x.shape[0] for x in ras]
            ns = [x.shape[1] for x in ras]
            out["ntrials_ch"][(a, b)] = (nt, ns)
            n, s = min(nt), min(ns)
            out["ras"][(a, b)] = np.stack([x[:n, :s] for x in ras])
            out["fs"].update(fs)
'''
s=s.replace(old,new)
i=s.index('def _channels_direct'); j=s.index('# ----------------------------------------------------------------', i)
s=s[:i]+s[j:]
open('sadeghi.py','w').write(s)
EOF
grep -n "_channels_direct" sadeghi.py
```

```
(Bash completed with no output)
```

**Agent**

Dev test on P3_Site09 (first neural file) and P1_Site04 (the example site): structure, correlations, timing.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > dev1.py <<'EOF'
import sys, time, numpy as np, resource
sys.path.insert(0,'entries/sadeghi-2019')
import sadeghi as S
t=time.time()
for name, raw in S.stream_members(lambda n: n.endswith(("P3_Site09.mat","P1_Site04.mat"))):
    d=S.read_site(name, raw); print(name, d['param'], d['fs'], time.time()-t)
    for k,v in list(d['ras'].items())[:3]: print(k, v.shape, d['ntrials_ch'][k][0][:3], v.dtype, float(v.min()), float(v.max()))
    print(len(d['ras']))
    if 'P1' in name: break
np.save('/dev/null', 0)
ras=d['ras']
r=ras[(0,0)]
t=time.time()
T0,Tw=S.whole_window(r.shape[-1]); print('T0 Tw',T0,Tw)
c=S.site_correlations(r, T0, Tw); print('corr time', time.time()-t)
print('spec diag sh', np.round(np.diag(c['spec']['sh']),2)); print('diag total', np.round(np.diag(c['spec']['ush']),3))
tm=c['temp']['sh'].mean(0); tau=c['tau_ms']; print('temp sh at 0', tm[200], tm[195:206].round(3))
rng=np.random.default_rng(0)
t=time.time(); f=S.single_trial_features(r, 100, 1000, (0,1500), rng); print('st feat 100', time.time()-t, f['spec'].shape, f['temp'].shape, f['temp'][:, :, 200].mean())
t=time.time(); f=S.shuffled_features(r, 20, 500, (0,1500), rng); print('sh feat 20', time.time()-t, f['spec'].shape, f['temp'].shape)
print('maxrss MB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
EOF
python dev1.py
```

```
data/NeuralData/Paradigm3/P3_Site09.mat {'AnimalNo': '0417015', 'BlockNo': '047', 'RecordDate': 'May2019'} {2034.5052083333333} 20.423326015472412
(0, 0) (16, 20, 6104) [20, 20, 20] float32 2.0047593116760254 289.1049499511719
(0, 1) (16, 20, 6104) [20, 20, 20] float32 2.6631879806518555 293.3170166015625
(0, 2) (16, 20, 6104) [20, 20, 20] float32 1.2497637271881104 226.43309020996094
18
data/NeuralData/Paradigm1/P1_Site04.mat {'AnimalNo': '0315011', 'BlockNo': '004', 'RecordDate': 'Sept2016'} {2034.5052083333333} 149.49411606788635
(0, 0) (16, 27, 6104) [27, 27, 27] float32 2.178123950958252 162.1326446533203
(1, 0) (16, 27, 6104) [27, 27, 27] float32 2.1963751316070557 129.4314422607422
(2, 0) (16, 27, 6104) [27, 27, 27] float32 2.3126232624053955 161.56385803222656
5
T0 Tw 1526.0 2849.0
corr time 2.8372998237609863
spec diag sh [0.16 0.19 0.26 0.31 0.34 0.41 0.45 0.5  0.53 0.51 0.44 0.36 0.26 0.22
 0.23 0.22]
diag total [0.998 0.999 0.999 0.999 0.999 0.999 0.999 0.999 0.999 0.999 0.999 0.999
 0.998 0.998 0.998 0.998]
temp sh at 0 0.33700859749464535 [0.148 0.185 0.226 0.271 0.315 0.337 0.315 0.271 0.226 0.185 0.147]
st feat 100 0.14517474174499512 (100, 120) (100, 16, 401) 0.9962256799120933
sh feat 20 0.8903102874755859 (20, 136) (20, 16, 401)
maxrss MB 908.244
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019 && python3 - <<'EOF'
s=open('sadeghi.py').read()
s=s.replace('FS = 2000.0  # aMUA sampling rate (Electrophysiology, paragraph 3); checked against the files\' Fs',
 'FS = 12207.03125 / 6  # aMUA sampling rate of the files (2034.5 Hz); the paper says 2 kHz\n# (Electrophysiology, paragraph 3). The notebook checks every file against this value.')
s+='''

KINDS = ("spec", "temp", "temp_shuf", "rate")


def _features(f, kind, rng=None):
    """Feature matrix of one kind. temp_shuf permutes the channels of each sample afresh
    (Noiseless neural classifier, paragraph 7: the validation channels are reordered at
    random, the model data keep their order)."""
    if kind == "temp_shuf":
        T = f["temp"]
        perm = np.argsort(rng.random((T.shape[0], T.shape[1])), axis=1)
        return np.take_along_axis(T, perm[:, :, None], 1).reshape(len(T), -1)
    if kind == "temp":
        return f["temp"].reshape(len(f["temp"]), -1)
    return f[kind]


def _acc_1a(ll, y):
    return (ll.argmax(-1) == y).mean(-1)


def _acc_1b(ll, y, groups):
    """Reading (1)(b): log-likelihoods summed over the samples of each group (a sound in a
    fold), one decision per group."""
    out = []
    for g in np.unique(groups):
        m = groups == g
        out.append((ll[..., m, :].sum(-2).argmax(-1) == y[m][0]))
    return np.mean(out, 0)


def classify(folds, classes, kinds=("spec", "temp", "temp_shuf"), rng=None, kmax=40,
             alphas=np.round(np.arange(0, 1.01, 0.1), 1)):
    """folds: list of (model, val) where model = (features dict, labels) and val is a list,
    one per duration, of (features dict, labels). Returns accuracies under readings
    (1)(a)/(b) x (2)(a)/(b), per duration and per class, the chosen PCs and the mixing
    coefficient a (claims file readings (1), (2), (5); a chosen on (a) model or (b)
    validation log-likelihood, claim figs9-mixing-coefficient)."""
    nd = len(folds[0][1])
    LL = {k: [] for k in kinds}       # per fold: (kmax, n_val_total, classes)
    LLin = {k: [] for k in kinds}     # in-sample model log-likelihoods, for a (a)
    LLinner = {k: [] for k in kinds}  # inner split of the model data, for reading (2)(b)
    Y, D, G = [], [], []
    Ym = []
    for fi, (model, vals) in enumerate(folds):
        fm, ym = model
        yv = np.concatenate([v[1] for v in vals])
        dv = np.concatenate([np.full(len(v[1]), i) for i, v in enumerate(vals)])
        Y.append(yv); D.append(dv); G.append(fi * 1000 + dv * 10 + yv)
        Ym.append(ym)
        half = np.zeros(len(ym), bool)
        for c in np.unique(ym):
            idx = np.flatnonzero(ym == c)
            half[rng.permutation(idx)[: len(idx) // 2]] = True
        for k in kinds:
            Xm = _features(fm, "temp" if k == "temp_shuf" else k)
            Xv = np.concatenate([_features(v[0], k, rng) for v in vals])
            Xin_v = _features(fm, k, rng)
            grid = loglik_grid(Xm, ym, np.concatenate([Xv, Xin_v]), kmax)
            LL[k].append(grid[:, : len(yv)])
            LLin[k].append(grid[:, len(yv):])
            LLinner[k].append((loglik_grid(Xm[half], ym[half], Xin_v[~half], kmax), ym[~half]))
    kk = {k: min(x.shape[0] for x in LL[k]) for k in kinds}
    res = {"pcs": {}, "alpha": {}, "acc": {}, "acc_class": {}}
    Yc, Dc, Gc = np.concatenate(Y), np.concatenate(D), np.concatenate(G)

    def per_duration(ll, rule):
        a = np.zeros((ll.shape[0], nd)) if ll.ndim == 3 else np.zeros(nd)
        cls = np.zeros((nd, len(classes)))
        for d in range(nd):
            m = Dc == d
            if rule == "1a":
                a[..., d] = _acc_1a(ll[..., m, :], Yc[m])
                if ll.ndim == 2:
                    for ci in range(len(classes)):
                        mc = m & (Yc == ci)
                        cls[d, ci] = (ll[mc].argmax(-1) == ci).mean()
            else:
                a[..., d] = _acc_1b(ll[..., m, :], Yc[m], Gc[m])
                if ll.ndim == 2:
                    for ci in range(len(classes)):
                        mc = m & (Yc == ci)
                        cls[d, ci] = _acc_1b(ll[mc], Yc[mc], Gc[mc])
        return a, cls

    for rule in ("1a", "1b"):
        for sel in ("2a", "2b"):
            key = rule + sel
            chosen = {}
            for k in kinds:
                ll = np.concatenate([x[: kk[k]] for x in LL[k]], axis=1)
                if sel == "2a":
                    curve, _ = per_duration(ll, rule)
                    chosen[k] = int(curve.mean(1).argmax())
                else:
                    inner = np.mean([(g[: kk[k]].argmax(-1) == yy).mean(-1) for g, yy in LLinner[k]], 0)
                    chosen[k] = int(inner.argmax())
                a, cls = per_duration(ll[chosen[k]], rule)
                res["acc"][(key, k)] = a
                res["acc_class"][(key, k)] = cls
                res["pcs"][(key, k)] = chosen[k] + 1
            if "spec" in kinds and "temp" in kinds:
                ls = np.concatenate([x[chosen["spec"]] for x in LL["spec"]])
                lt = np.concatenate([x[chosen["temp"]] for x in LL["temp"]])
                lsi = np.concatenate([x[chosen["spec"]] for x in LLin["spec"]])
                lti = np.concatenate([x[chosen["temp"]] for x in LLin["temp"]])
                ymc = np.concatenate(Ym)
                for asel in ("a", "b"):
                    best, bestv = None, -np.inf
                    for al in alphas:
                        if asel == "a":
                            lp = log_posterior(al * lsi + (1 - al) * lti)
                            v = lp[np.arange(len(ymc)), ymc].sum()
                        else:
                            lp = log_posterior(al * ls + (1 - al) * lt)
                            v = lp[np.arange(len(Yc)), Yc].sum()
                        if v > bestv:
                            best, bestv = al, v
                    a, cls = per_duration(best * ls + (1 - best) * lt, rule)
                    res["acc"][(key, "st_" + asel)] = a
                    res["acc_class"][(key, "st_" + asel)] = cls
                    res["alpha"][(key, asel)] = best
    return res
'''
open('sadeghi.py','w').write(s)
EOF
echo ok
```

```
ok
```

**Agent**

Now a fold builder per paradigm, then a test on the example site.

**Agent calls Bash**

```bash
cat >> sadeghi.py <<'EOF'


def _cat(fs):
    return {k: np.concatenate([f[k] for f in fs]) for k in fs[0]}


def half_ranges(nsamples):
    """First and second halves of the raster in ms (NeuralExample.m: NS2 = floor(NS/2))."""
    h = np.floor(nsamples / 2) / FS * 1000
    return [(0.0, h), (h, nsamples / FS * 1000)]


def build_folds(model_ras, val_ras, model_ranges, val_ranges, rng, n=100, model_ms=1000.0,
                durations=DURATIONS_MS, maker=single_trial_features):
    """model_ras / val_ras: lists over classes of lists of rasters (channels, trials, samples)
    (one raster per sound, or several exemplars per category). Fold i uses model_ranges[i]
    of the model rasters and val_ranges[i] of the validation rasters. n samples per raster."""
    folds = []
    for mr, vr in zip(model_ranges, val_ranges):
        fm, ym = [], []
        for c, rs in enumerate(model_ras):
            for r in rs:
                fm.append(maker(r, n, model_ms, mr, rng))
                ym.append(np.full(n, c))
        vals = []
        for d in durations:
            fv, yv = [], []
            for c, rs in enumerate(val_ras):
                for r in rs:
                    fv.append(maker(r, n, d, vr, rng))
                    yv.append(np.full(n, c))
            vals.append((_cat(fv), np.concatenate(yv)))
        folds.append(((_cat(fm), np.concatenate(ym)), vals))
    return folds
EOF
cd $TMPDIR && . dev/bin/activate && cat > dev2.py <<'EOF'
import sys, time, numpy as np, resource
sys.path.insert(0,'entries/sadeghi-2019')
import importlib, sadeghi as S
for name, raw in S.stream_members(lambda n: n.endswith("P1_Site04.mat")):
    d=S.read_site(name, raw); break
rng=np.random.default_rng(1)
ras=[[d['ras'][(k,0)]] for k in range(5)]
NS=ras[0][0].shape[-1]; hr=S.half_ranges(NS)
t=time.time()
folds=S.build_folds(ras, ras, hr, hr[::-1], rng)
print('features', time.time()-t)
t=time.time()
res=S.classify(folds, S.P1_SOUNDS, kinds=("spec","temp","temp_shuf","rate"), rng=rng)
print('classify', time.time()-t)
for k,v in res['acc'].items(): print(k, np.round(v*100,0), res['pcs'].get(k))
print(res['alpha'])
print('maxrss MB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
EOF
python dev2.py
```

```
features 7.207837104797363
classify 2.3914272785186768
('1a2a', 'spec') [41. 46. 50. 53. 59. 68. 69. 74. 78.] 3
('1a2a', 'temp') [33. 36. 42. 46. 48. 53. 56. 62. 64.] 4
('1a2a', 'temp_shuf') [23. 23. 26. 28. 28. 29. 33. 34. 39.] 3
('1a2a', 'rate') [79. 81. 86. 88. 91. 93. 94. 95. 96.] 4
('1a2a', 'st_a') [40. 46. 52. 55. 62. 69. 72. 78. 80.] None
('1a2a', 'st_b') [41. 48. 52. 56. 63. 71. 74. 81. 84.] None
('1a2b', 'spec') [30. 35. 39. 42. 48. 57. 63. 71. 81.] 37
('1a2b', 'temp') [30. 32. 36. 39. 42. 46. 49. 53. 53.] 5
('1a2b', 'temp_shuf') [23. 24. 26. 29. 29. 30. 30. 30. 32.] 4
('1a2b', 'rate') [78. 80. 84. 88. 90. 91. 94. 94. 94.] 6
('1a2b', 'st_a') [31. 35. 40. 43. 52. 62. 71. 79. 84.] None
('1a2b', 'st_b') [31. 32. 37. 42. 47. 52. 57. 63. 67.] None
('1b2a', 'spec') [50. 50. 50. 50. 80. 80. 80. 80. 90.] 3
('1b2a', 'temp') [20. 20. 20. 50. 60. 60. 70. 80. 70.] 3
('1b2a', 'temp_shuf') [20. 20. 20. 20. 20. 20. 50. 50. 60.] 3
('1b2a', 'rate') [100. 100. 100. 100. 100. 100. 100. 100. 100.] 3
('1b2a', 'st_a') [40. 40. 40. 40. 60. 80. 90. 90. 90.] None
('1b2a', 'st_b') [40. 40. 40. 40. 60. 80. 90. 90. 90.] None
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019 && python3 - <<'EOF'
s=open('sadeghi.py').read()
i=s.index('def site_correlations'); j=s.index('def whole_window')
s=s[:i]+'''def zero_lag_all(X):
    """Zero-lag R12_sh, R12_ush and R12_noise of the code for all channel pairs at once.
    X: (channels, trials, Nw + 2) segment (MaxLag = 0), the square window in the middle."""
    C, NT, L = X.shape
    Nw = L - 2
    X = X.astype(np.float64).copy()
    X[..., 0] = 0
    X[..., -1] = 0
    P = X.sum(1)
    Rdiag = np.einsum("ktn,ltn->kl", X, X)
    R12 = (P @ P.T - Rdiag) / NT / (NT - 1) / Nw
    Rd = Rdiag / NT / Nw
    noise = Rd - R12
    M1 = P.sum(-1) / Nw
    E2diag = (X ** 2).sum((1, 2)) / (Nw - 1)
    var = (E2diag * NT - M1 ** 2) / NT ** 2
    M1 = M1 / NT
    den = np.sqrt(np.outer(var, var))
    mm = np.outer(M1, M1)
    return {"sh": (R12 - mm) / den, "ush": (Rd - mm) / den, "noise": noise / den}


def site_correlations(ras, T0_ms, Tw_ms, maxtau_ms=100.0):
    """Spectral (zero-lag, channels x channels) and temporal (channels x lags) shuffled
    (stimulus-driven), unshuffled (total) and noise correlations for ras (channels, trials,
    samples), one square window of Tw_ms centred at T0_ms (paper's code)."""
    tem = window_corr(ras, ras, T0_ms, Tw_ms, maxtau_ms)
    _, _, s0, s1 = window_geometry(T0_ms, Tw_ms, 0.0)
    spec = zero_lag_all(ras[:, :, s0:s1])
    return {"spec": spec, "temp": {k: tem[k] for k in ("sh", "ush", "noise")}, "tau_ms": tem["tau_ms"]}


WINDOW_READINGS = ("whole", "w1000", "code_half")


def correlation_readings(ras):
    """Readings of the window T (claims file, fig1k-example-temporal-widths (ii)):
    whole = one window over the whole response (lags kept inside the raster);
    w1000 = 1000 ms windows centred at 0.6, 1.5 and 2.4 s, averaged (standard choice of
    centres); code_half = the first half of the raster, as NeuralExample.m computes Fig 1."""
    NS = ras.shape[-1]
    out = {}
    T0, Tw = whole_window(NS)
    out["whole"] = site_correlations(ras, T0, Tw)
    parts = [site_correlations(ras, c, 1000.0) for c in (600.0, 1500.0, 2400.0)]
    out["w1000"] = {"spec": {k: np.mean([p["spec"][k] for p in parts], 0) for k in parts[0]["spec"]},
                    "temp": {k: np.mean([p["temp"][k] for p in parts], 0) for k in parts[0]["temp"]},
                    "tau_ms": parts[0]["tau_ms"]}
    NS2 = NS // 2
    T0, Tw = whole_window(NS2)
    out["code_half"] = site_correlations(ras[:, :, :NS2], T0, Tw)
    return out


'''+s[j:]
s=s.replace('''    Tw = np.floor((nsamples - maxlag * 2 - 2) / fs * 1000) - 2
    return T0, Tw''','''    Tw = np.floor((nsamples - maxlag * 2 - 2) / fs * 1000) - 2  # 2 ms less, so that the
    return T0, Tw  # window plus lags stay inside the raster at the files' 2034.5 Hz rate''')
s=s.replace('''        tem = window_corr(ras, ras, t0, Tw_ms, maxtau_ms)["sh"]
        _, Nw_, s0, s1 = window_geometry(t0, Tw_ms, 0.0)
        X = ras[:, :, s0:s1].astype(np.float64)
        sp = _shuffled_zero_lag(X)''','''        tem = window_corr(ras, ras, t0, Tw_ms, maxtau_ms)["sh"]
        _, Nw_, s0, s1 = window_geometry(t0, Tw_ms, 0.0)
        sp = zero_lag_all(ras[:, :, s0:s1])["sh"]''')
i=s.index('def _shuffled_zero_lag'); j=s.index('# ---------------------------------------------------------------- classifier')
s=s[:i]+s[j:]
s+='''

def clock_check(ras, shift_ms=250.0):
    """Stimulus locking: per channel, Pearson r between the PSTHs of odd and even trials,
    with true alignment and with the even trials shifted circularly by shift_ms."""
    sh = int(round(shift_ms / 1000 * FS))
    a = ras[:, 0::2].mean(1)
    b = ras[:, 1::2].mean(1)
    r_true = [np.corrcoef(a[c], b[c])[0, 1] for c in range(len(a))]
    r_shift = [np.corrcoef(a[c], np.roll(b[c], sh))[0, 1] for c in range(len(a))]
    return np.median(r_true), np.median(r_shift)
'''
open('sadeghi.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cat > dev3.py <<'EOF'
import sys, time, numpy as np
sys.path.insert(0,'entries/sadeghi-2019')
import sadeghi as S
for name, raw in S.stream_members(lambda n: n.endswith("P3_Site09.mat")):
    d=S.read_site(name, raw); break
r=d['ras'][(0,0)]
t=time.time(); c=S.correlation_readings(r); print('readings', time.time()-t)
# compare vectorised zero lag to window_corr lag 0
T0,Tw=S.whole_window(r.shape[-1]); x=S.window_corr(r[3][None], r, T0, Tw, 0.0)
print(np.abs(x['sh'][:,0]-c['whole']['spec']['sh'][3]).max(), np.abs(x['noise'][:,0]-c['whole']['spec']['noise'][3]).max())
print(np.diag(c['whole']['spec']['sh']+c['whole']['spec']['noise']).round(3))
print(S.clock_check(r))
EOF
python dev3.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dev3.py", line 7, in <module>
    t=time.time(); c=S.correlation_readings(r); print('readings', time.time()-t)
                     ~~~~~~~~~~~~~~~~~~~~~~^^^
  File "entries/sadeghi-2019/sadeghi.py", line 208, in correlation_readings
    parts = [site_correlations(ras, c, 1000.0) for c in (600.0, 1500.0, 2400.0)]
             ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "entries/sadeghi-2019/sadeghi.py", line 190, in site_correlations
    tem = window_corr(ras, ras, T0_ms, Tw_ms, maxtau_ms)
  File "entries/sadeghi-2019/sadeghi.py", line 123, in window_corr
    raise ValueError("window plus lags outside the raster")
ValueError: window plus lags outside the raster
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019 && sed -i 's/for c in (600.0, 1500.0, 2400.0)\]/for c in (610.0, 1500.0, 2390.0)]/; s/w1000 = 1000 ms windows centred at 0.6, 1.5 and 2.4 s/w1000 = 1000 ms windows centred at 0.61, 1.5 and 2.39 s/' sadeghi.py && cd $TMPDIR && . dev/bin/activate && python dev3.py
```

```
readings 0.4351499080657959
1.5487611193520934e-14 3.723688024592775e-13
[0.999 0.999 0.999 0.999 0.999 0.999 0.999 0.999 0.999 0.999 0.999 0.999
 0.999 0.999 0.999 0.999]
(np.float64(0.8019528139291818), np.float64(0.026418608473070423))
Shell cwd was reset to
```

**Agent**

Fast and consistent with the per-channel port. Now per-paradigm processing functions.

**Agent calls Bash**

```bash
cd entries/sadeghi-2019 && cat >> sadeghi.py <<'EOF'


def raster_hash(a):
    """Hash of a raster's values, to find recordings deposited more than once."""
    import hashlib
    return hashlib.md5(np.ascontiguousarray(a[:, :2]).tobytes()).hexdigest()


def describe(d):
    """Counts, ranges and hashes of one site, for the data check."""
    out = {"param": d["param"], "fs": sorted(d["fs"]), "cond": {}}
    for key, r in d["ras"].items():
        nt, ns = d["ntrials_ch"][key]
        out["cond"][key] = {"channels": r.shape[0], "trials": r.shape[1], "samples": r.shape[2],
                            "trials_equal": len(set(nt)) == 1, "samples_equal": len(set(ns)) == 1,
                            "min": float(r.min()), "max": float(r.max()), "mean": float(r.mean()),
                            "hash": [raster_hash(r[c]) for c in range(r.shape[0])],
                            "clock": clock_check(r)}
    return out


def process_p1(d, rng, noiseless=False):
    """Paradigm 1 site: correlations under each window reading, and the single-trial
    classifier (spectral, temporal, temporal without tonotopy, spectrum) with the half split;
    the noiseless classifier at 1 s when asked (example site only)."""
    ras = [d["ras"][(k, 0)] for k in range(5)]
    out = {"corr": [correlation_readings(r) for r in ras]}
    hr = half_ranges(min(r.shape[-1] for r in ras))
    folds = build_folds([[r] for r in ras], [[r] for r in ras], hr, hr[::-1], rng)
    out["single"] = classify(folds, P1_SOUNDS, kinds=KINDS, rng=rng)
    if noiseless:
        folds = build_folds([[r] for r in ras], [[r] for r in ras], hr, hr[::-1], rng,
                            model_ms=500.0, durations=[1000.0], maker=shuffled_features)
        out["noiseless"] = classify(folds, P1_SOUNDS, kinds=("spec", "temp", "temp_shuf"), rng=rng)
    return out


def process_p2(d, rng):
    """Paradigm 2 site (condition 0 = 1/f, 1 = original). Models from the original sounds;
    validation on the 1/f sounds under reading (3)(a) (half split) and (3)(b) (whole
    responses), and on the original sounds with the half split (control)."""
    orig = [d["ras"][(k, 1)] for k in range(5)]
    eq = [d["ras"][(k, 0)] for k in range(5)]
    out = {"corr_orig": [correlation_readings(r) for r in orig],
           "corr_eq": [correlation_readings(r) for r in eq]}
    ns = min(r.shape[-1] for r in orig + eq)
    hr = half_ranges(ns)
    whole = [(0.0, ns / FS * 1000)]
    out["eq_3a"] = classify(build_folds([[r] for r in orig], [[r] for r in eq], hr, hr[::-1], rng),
                            P1_SOUNDS, kinds=KINDS, rng=rng)
    out["eq_3b"] = classify(build_folds([[r] for r in orig], [[r] for r in eq], whole, whole, rng),
                            P1_SOUNDS, kinds=KINDS, rng=rng)
    out["orig"] = classify(build_folds([[r] for r in orig], [[r] for r in orig], hr, hr[::-1], rng),
                           P1_SOUNDS, kinds=KINDS, rng=rng)
    return out


def summarize_classifier(res, duration_index=-1):
    """Accuracies (%) at one duration, by reading and classifier."""
    return {k: 100 * v[duration_index] for k, v in res["acc"].items()}
EOF
echo; date -u
```

```
Fri Nov 13 20:22:02 UTC 2026
```

**Agent**

Now the notebook for paradigms 1 and 2, written as a percent-format script and converted with jupytext.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q jupytext nbconvert ipykernel nbclient && echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/sadeghi-2019/src_neural.py",
 "content": "# %% [markdown]\n# # Sadeghi et al. (2019): neural claims, paradigms 1 and 2 (CRCNS bst-2)\n#\n# HEADER\n\n# %%\nimport time, resource\nimport numpy as np\nfrom scipy import stats\nimport matplotlib.pyplot as plt\nimport sadeghi as S\n\nT_START = time.time()\nP1_EXAMPLE, P2_EXAMPLE = \"P1_Site04\", \"P2_Site11\"  # data set's FigureData list (finding aid)\nSEED = {\"P1\": 101, \"P2\": 202}  # standard choices; one generator per site, from these\n\n# %% [markdown]\n# ## Loading\n#\n# One pass over the tar stream. Each paradigm 1 and 2 file is parsed in memory, reduced to\n# its correlations and classifier results, and released before the next one is read. The\n# paradigm 3 files come first in the stream and are skipped here (second notebook).\n\n# %%\ndesc, R1, R2 = {}, {}, {}\nfor name, raw in S.stream_members(lambda n: \"/Paradigm1/P1_\" in n or \"/Paradigm2/P2_\" in n):\n    d = S.read_site(name, raw)\n    del raw\n    site = d[\"name\"]\n    desc[site] = S.describe(d)\n    i = int(site[-2:])\n    if site.startswith(\"P1\"):\n        R1[site] = S.process_p1(d, np.random.default_rng(SEED[\"P1\"] * 100 + i), noiseless=(site == P1_EXAMPLE))\n    else:\n        R2[site] = S.process_p2(d, np.random.default_rng(SEED[\"P2\"] * 100 + i))\n    del d\n    print(f\"{site} done at {time.time() - T_START:.0f} s\", flush=True)\nP1_SITES, P2_SITES = sorted(R1), sorted(R2)\nprint(\"peak memory (GB):\", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6)\n\n# %% [markdown]\n# ## Data check\n\n# %% tags=[\"sanity\"]\nprint(\"files:\", len(P1_SITES), \"paradigm 1 sites,\", len(P2_SITES), \"paradigm 2 sites\")\nfs_all = sorted({f for s in desc.values() for f in s[\"fs\"]})\nprint(\"sampling rates in the files (Hz):\", fs_all, \"; helper uses\", S.FS, \"; the paper states 2000\")\nfor site in P1_SITES + P2_SITES:\n    s = desc[site]\n    conds = s[\"cond\"]\n    tr = [c[\"trials\"] for c in conds.values()]\n    ns = sorted({c[\"samples\"] for c in conds.values()})\n    ok = all(c[\"trials_equal\"] and c[\"samples_equal\"] and c[\"channels\"] == 16 for c in conds.values())\n    rng_ = (min(c[\"min\"] for c in conds.values()), max(c[\"max\"] for c in conds.values()))\n    clock = np.array([c[\"clock\"] for c in conds.values()])\n    print(f\"{site} animal {s['param']['AnimalNo']} date {s['param']['RecordDate']} block {s['param']['BlockNo']}\"\n          f\" | conditions {len(conds)} trials {min(tr)}-{max(tr)} samples {ns} ({ns[0] / S.FS:.3f} s)\"\n          f\" | equal across channels {ok} | aMUA range {rng_[0]:.2f} to {rng_[1]:.1f}\"\n          f\" | odd/even PSTH r {np.median(clock[:, 0]):.2f}, shifted 250 ms {np.median(clock[:, 1]):.2f}\")\nfor p, sites in ((\"P1\", P1_SITES), (\"P2\", P2_SITES)):\n    an = {}\n    for site in sites:\n        an.setdefault(desc[site][\"param\"][\"AnimalNo\"], []).append(site)\n    print(p, \"sites per animal:\", {k: len(v) for k, v in an.items()})\n    t = [c[\"trials\"] for site in sites for c in desc[site][\"cond\"].values()]\n    print(p, \"trials per sound, range\", min(t), \"to\", max(t))\n# recordings deposited more than once: identical channel rasters (first two trials hashed)\nseen = {}\nfor site in P1_SITES + P2_SITES:\n    for key, c in desc[site][\"cond\"].items():\n        for ch, h in enumerate(c[\"hash\"]):\n            seen.setdefault(h, []).append((site, key, ch))\ndups = [v for v in seen.values() if len(v) > 1]\nprint(\"identical rasters found:\", len(dups), dups[:5])\n\n# %% [markdown]\n# The aMUA values are positive envelopes (arbitrary units). Every raster is 6104 samples at\n# 2034.5 Hz, 3.0 s, so the files' rate, not the paper's 2 kHz, gives the stated sound\n# duration. Responses are locked to the trial start: the PSTHs of odd and even trials\n# correlate strongly with true alignment and near zero when one is shifted by 250 ms, at\n# every site and condition (printed above), so the rasters share the clock of the trials.\n\n# %% [markdown]\n# ## Shared measures\n\n# %%\ndef width_at(curve, tau, frac):\n    \"\"\"Full width (ms) of the contiguous region around the peak where curve >= frac * peak,\n    with linear interpolation of the crossings.\"\"\"\n    i0 = int(np.argmax(curve))\n    thr = frac * curve[i0]\n    def cross(step):\n        i = i0\n        while 0 <= i + step < len(curve) and curve[i + step] >= thr:\n            i += step\n        if not (0 <= i + step < len(curve)):\n            return tau[i]\n        a, b = curve[i], curve[i + step]\n        return tau[i] + (tau[i + step] - tau[i]) * (a - thr) / (a - b)\n    return cross(1) - cross(-1)\n\n\ndef side_peak(curve, tau, min_lag=10.0):\n    \"\"\"Lag (ms) of the largest local maximum at positive lags beyond min_lag.\"\"\"\n    m = tau > min_lag\n    c, t = curve[m], tau[m]\n    loc = [i for i in range(1, len(c) - 1) if c[i] > c[i - 1] and c[i] >= c[i + 1]]\n    if not loc:\n        return np.nan, np.nan\n    j = max(loc, key=lambda i: c[i])\n    return t[j], c[j]\n\n\ndef within(v, e, tol):\n    return abs(v - e) <= tol + 1e-9\n\n\ndef ttest_chance(x, chance):\n    t, p2 = stats.ttest_1samp(x, chance)\n    return t, p2, (p2 / 2 if t > 0 else 1 - p2 / 2)\n\n\nREAD = [\"1a2a\", \"1a2b\", \"1b2a\", \"1b2b\"]\nREAD_TXT = {\"1a2a\": \"(1a) each sample a decision, (2a) PCs on validation\",\n            \"1a2b\": \"(1a) each sample a decision, (2b) PCs on an inner split\",\n            \"1b2a\": \"(1b) 100 samples summed, (2a) PCs on validation\",\n            \"1b2b\": \"(1b) 100 samples summed, (2b) PCs on an inner split\"}\nTAU = R1[P1_SITES[0]][\"corr\"][0][\"whole\"][\"tau_ms\"]\nDUR = S.DURATIONS_MS\nprint(\"durations (ms):\", np.round(DUR, 1))\n\n# %% [markdown]\n# ## fig1k-example-temporal-widths\n#\n# > At the example paradigm 1 site, stimulus-driven temporal correlations are fast for crowd,\n# > water and fire (3.0, 3.0 and 3.9 ms wide at 50% of maximum; 5.9, 6.9 and 11.8 ms at 10%),\n# > the bird chorus has a sharp peak (5.9 ms half width) and a slow component (161.2 ms at\n# > 10%), and the snake has a 7.9 ms half width, 20.6 ms at 10%, and a periodic pattern of about\n# > 50 ms period at high-frequency sites.\n#\n# Stimulus-driven (shuffled) temporal correlations c_kk(tau), lags within 100 ms. The lag\n# step is 0.49 ms at the files' rate. Channel order is not documented in the data set, so\n# \"upper eight channels\" is run as channels 9 to 16 and, as a variant, 1 to 8; reading (b) of\n# the period (best frequency above 2 kHz) needs best frequencies, which the data set lacks.\n\n# %% tags=[\"claim:fig1k-example-temporal-widths\"]\nEXP_W = {(\"crowd\", 0.5): (3.0, 0.5), (\"water\", 0.5): (3.0, 0.5), (\"fire\", 0.5): (3.9, 0.5),\n         (\"crowd\", 0.1): (5.9, 0.59), (\"water\", 0.1): (6.9, 0.69), (\"fire\", 0.1): (11.8, 1.18),\n         (\"bird\", 0.5): (5.9, 0.59), (\"bird\", 0.1): (161.2, 16.1), (\"snake\", 0.5): (7.9, 0.79),\n         (\"snake\", 0.1): (20.6, 2.06)}\nex = R1[P1_EXAMPLE][\"corr\"]\nfig1k = {}\nfor win in S.WINDOW_READINGS:\n    for curve_r in (\"mean\", \"median\"):\n        vals, hits = {}, 0\n        for (snd, frac), (e, tol) in EXP_W.items():\n            T = ex[S.P1_SOUNDS.index(snd)][win][\"temp\"][\"sh\"]\n            if curve_r == \"mean\":\n                v = width_at(T.mean(0), TAU, frac)\n            else:\n                v = np.median([width_at(T[c], TAU, frac) for c in range(16)])\n            vals[(snd, frac)] = v\n            hits += within(v, e, tol)\n        Ts = ex[4][win][\"temp\"][\"sh\"]\n        per = {\"9-16\": side_peak(Ts[8:].mean(0), TAU), \"1-8\": side_peak(Ts[:8].mean(0), TAU)}\n        hits_p = {k: within(p[0], 50, 5) for k, p in per.items()}\n        order = vals[(\"crowd\", 0.5)] < vals[(\"fire\", 0.5)] and vals[(\"water\", 0.5)] < vals[(\"fire\", 0.5)]\n        fig1k[(win, curve_r)] = (vals, hits, per, hits_p, order)\n        print(f\"window {win:9s} curve {curve_r:6s}: \" + \", \".join(f\"{s} {int(f*100)}% {v:.1f}\" for (s, f), v in vals.items()))\n        print(f\"    snake side peak, channels 9-16 {per['9-16'][0]:.1f} ms (height {per['9-16'][1]:.3f}),\"\n              f\" channels 1-8 {per['1-8'][0]:.1f} ms (height {per['1-8'][1]:.3f})\")\n        print(f\"    widths within tolerance {hits}/10; with the period (9-16) {hits + hits_p['9-16']}/11,\"\n              f\" (1-8) {hits + hits_p['1-8']}/11; crowd and water narrower than fire at 50%: {order}\")\nbest = max(fig1k.items(), key=lambda kv: kv[1][1] + max(kv[1][3].values()))\nprint(\"best reading:\", best[0], \"count\", best[1][1] + max(best[1][3].values()), \"of 11\")\n\nfig, ax = plt.subplots(1, 5, figsize=(14, 2.6), sharey=True)\nfor k, snd in enumerate(S.P1_SOUNDS):\n    T = ex[k][\"whole\"][\"temp\"][\"sh\"]\n    ax[k].plot(TAU, T.mean(0), \"k\")\n    ax[k].plot(TAU, T[8:].mean(0), \"r\", lw=0.8)\n    ax[k].set_title(snd); ax[k].set_xlabel(\"lag (ms)\")\nax[0].set_ylabel(\"stimulus-driven corr.\")\nplt.tight_layout(); plt.show()\nprint(\"plotted range:\", float(min(ex[k][\"whole\"][\"temp\"][\"sh\"].mean(0).min() for k in range(5))),\n      \"to\", float(max(ex[k][\"whole\"][\"temp\"][\"sh\"].mean(0).max() for k in range(5))))\n\n# %% [markdown]\n# **Result: RES_FIG1K**\n\n# %% [markdown]\n# ## fig1-snr-noise-stronger\n#\n# > Noise correlations are generally stronger than the stimulus-driven correlations, with\n# > spectral SNR from -26.0 to -0.9 dB (mean -11.0, SD 7.2) and temporal SNR from -26.1 to -4.1\n# > dB (mean -6.0, SD 8.2).\n#\n# SNR = 10 log10 of summed squared stimulus-driven over summed squared noise correlation,\n# readings (a) all entries, (b) without the zero-lag diagonal; (c) one value per site and\n# sound, (d) per site averaged over sounds; (e) 13 sites, (f) the example site; and the\n# window readings.\n\n# %% tags=[\"claim:fig1-snr-noise-stronger\"]\ndef snr_site_sound(c, excl):\n    sp_s, sp_n = c[\"spec\"][\"sh\"].copy(), c[\"spec\"][\"noise\"].copy()\n    te_s, te_n = c[\"temp\"][\"sh\"].copy(), c[\"temp\"][\"noise\"].copy()\n    if excl:\n        off = ~np.eye(16, dtype=bool)\n        sp_s, sp_n = sp_s[off], sp_n[off]\n        keep = np.abs(TAU) > 1e-9\n        te_s, te_n = te_s[:, keep], te_n[:, keep]\n    return (10 * np.log10((sp_s ** 2).sum() / (sp_n ** 2).sum()),\n            10 * np.log10((te_s ** 2).sum() / (te_n ** 2).sum()))\n\nsnr_rows = []\nfor win in S.WINDOW_READINGS:\n    for excl in (False, True):\n        V = np.array([[snr_site_sound(R1[s][\"corr\"][k][win], excl) for k in range(5)] for s in P1_SITES])  # sites, sounds, 2\n        for unit in (\"c\", \"d\"):\n            for rec in (\"e\", \"f\"):\n                X = V if rec == \"e\" else V[[P1_SITES.index(P1_EXAMPLE)]]\n                X = X.reshape(-1, 2) if unit == \"c\" else X.mean(1)\n                if rec == \"f\" and unit == \"d\":\n                    continue  # one value only\n                sp, te = X[:, 0], X[:, 1]\n                hits_m = within(sp.mean(), -11.0, 7.2) + within(te.mean(), -6.0, 8.2)\n                hits_b = (within(sp.min(), -26.0, 2.6) + within(sp.max(), -0.9, 0.09)\n                          + within(te.min(), -26.1, 2.61) + within(te.max(), -4.1, 0.41))\n                neg = ((sp < 0).mean(), (te < 0).mean())\n                snr_rows.append((win, \"b\" if excl else \"a\", unit, rec, sp, te, hits_m, hits_b, neg))\n                print(f\"{win:9s} ({'b' if excl else 'a'})({unit})({rec}) n={len(sp):2d} | spectral mean {sp.mean():6.1f} SD {sp.std(ddof=1) if len(sp) > 1 else 0:4.1f}\"\n                      f\" range {sp.min():6.1f} to {sp.max():5.1f} | temporal mean {te.mean():6.1f} SD {te.std(ddof=1) if len(te) > 1 else 0:4.1f}\"\n                      f\" range {te.min():6.1f} to {te.max():5.1f} | means in tol {hits_m}/2, bounds {hits_b}/4,\"\n                      f\" fraction < 0 dB {neg[0]:.2f}, {neg[1]:.2f}\")\nmatch = [r[:4] for r in snr_rows if r[6] == 2 and r[7] >= 3]\npart = [r[:4] for r in snr_rows if r[6] == 2 and min(r[8]) > 0.5]\nprint(\"readings meeting the reproduced rule:\", match)\nprint(\"readings with both means in tolerance and SNR mostly negative:\", part)\n\n# %% [markdown]\n# **Result: RES_SNR**\n\n# %% [markdown]\n# ## fig2-noise-restricted\n#\n# > Across the 13 paradigm 1 sites, noise correlations are more restricted in frequency and\n# > time and more consistent across sounds than stimulus-driven correlations, which are broader\n# > and stimulus dependent (a slow component for the bird chorus and a 20 Hz periodic\n# > component for the snake).\n\n# %% tags=[\"claim:fig2-noise-restricted\"]\ndef collapse(c, kind):\n    M = c[\"spec\"][kind]\n    sp = np.array([np.mean(np.concatenate([np.diag(M, o), np.diag(M, -o)])) if o else np.mean(np.diag(M)) for o in range(16)])\n    te = c[\"temp\"][kind].mean(0)\n    return sp / sp[0], te / te[np.argmin(np.abs(TAU))]\n\nOFF = np.arange(16.0)\nfig2 = {}\nfor win in S.WINDOW_READINGS:\n    cur = {kind: np.array([[collapse(R1[s][\"corr\"][k][win], kind) for k in range(5)] for s in P1_SITES], dtype=object)\n           for kind in (\"sh\", \"noise\")}\n    avg = {kind: (np.mean([[cur[kind][i, k][0] for k in range(5)] for i in range(len(P1_SITES))], 0),\n                  np.mean([[cur[kind][i, k][1] for k in range(5)] for i in range(len(P1_SITES))], 0)) for kind in cur}\n    res = {}\n    for kind in (\"sh\", \"noise\"):\n        sp, te = avg[kind]  # (sounds, offsets), (sounds, lags)\n        res[kind] = {\"sp_w\": [width_at(np.concatenate([sp[k][::-1], sp[k][1:]]), np.concatenate([-OFF[::-1], OFF[1:]]), 0.5) for k in range(5)],\n                     \"te_w\": [width_at(te[k], TAU, 0.5) for k in range(5)],\n                     \"sp_far\": [sp[k][3:].mean() for k in range(5)],\n                     \"te_far\": [te[k][np.abs(TAU) > 10].mean() for k in range(5)],\n                     \"sp_sd\": sp.std(0, ddof=1).sum(), \"te_sd\": te.std(0, ddof=1).sum()}\n    fig2[win] = (res, avg)\n    for meas, lab in ((\"w\", \"width at 50% (channels / ms)\"), (\"far\", \"mean beyond 2 channels / beyond 10 ms\")):\n        a_s = res[\"sh\"][\"sp_\" + meas]; a_n = res[\"noise\"][\"sp_\" + meas]\n        b_s = res[\"sh\"][\"te_\" + meas]; b_n = res[\"noise\"][\"te_\" + meas]\n        ns_ = sum(n < s for n, s in zip(a_n, a_s)); nt_ = sum(n < s for n, s in zip(b_n, b_s))\n        print(f\"{win:9s} {lab}: spectral stim {np.round(a_s, 2)} noise {np.round(a_n, 2)} -> noise smaller {ns_}/5;\"\n              f\" temporal stim {np.round(b_s, 2)} noise {np.round(b_n, 2)} -> noise smaller {nt_}/5\")\n    print(f\"{win:9s} SD across sounds summed: spectral stim {res['sh']['sp_sd']:.2f} noise {res['noise']['sp_sd']:.2f};\"\n          f\" temporal stim {res['sh']['te_sd']:.2f} noise {res['noise']['te_sd']:.2f}\")\nres, avg = fig2[\"whole\"]\nprint(\"bird chorus stimulus-driven temporal correlation (whole window) at 50 ms lag:\",\n      round(float(avg[\"sh\"][1][1][np.argmin(np.abs(TAU - 50))]), 3), \"; noise:\", round(float(avg[\"noise\"][1][1][np.argmin(np.abs(TAU - 50))]), 3))\nprint(\"snake stimulus-driven side peak:\", side_peak(avg[\"sh\"][1][4], TAU), \"; noise:\", side_peak(avg[\"noise\"][1][4], TAU))\nfig, ax = plt.subplots(1, 4, figsize=(14, 2.6))\nfor k, snd in enumerate(S.P1_SOUNDS):\n    ax[0].plot(OFF, avg[\"sh\"][0][k], label=snd); ax[1].plot(OFF, avg[\"noise\"][0][k])\n    ax[2].plot(TAU, avg[\"sh\"][1][k]); ax[3].plot(TAU, avg[\"noise\"][1][k])\nfor a, t in zip(ax, [\"spectral, stimulus\", \"spectral, noise\", \"temporal, stimulus\", \"temporal, noise\"]):\n    a.set_title(t)\nax[0].legend(fontsize=7); plt.tight_layout(); plt.show()\nprint(\"plotted ranges:\", [(round(float(np.min(x)), 2), round(float(np.max(x)), 2)) for x in (avg[\"sh\"][0], avg[\"noise\"][0], avg[\"sh\"][1], avg[\"noise\"][1])])\n\n# %% [markdown]\n# **Result: RES_FIG2**\n\n# %% [markdown]\n# ## Single-trial classifier, paradigm 1\n#\n# Accuracy at each duration, per site, for every reading of (1) and (2); the spectro-temporal\n# classifier is shown with a chosen on (a) the model or (b) the validation log-likelihood.\n\n# %%\nCLF = [\"st_a\", \"st_b\", \"spec\", \"temp\", \"temp_shuf\", \"rate\"]\ndef acc_table(R, sites, key=\"single\", di=-1):\n    return {(r, c): np.array([100 * R[s][key][\"acc\"][(r, c)][di] for s in sites]) for r in READ for c in CLF}\nA1 = acc_table(R1, P1_SITES)\nA1_short = acc_table(R1, P1_SITES, di=0)\nfor r in READ:\n    print(READ_TXT[r])\n    for c in CLF:\n        print(f\"   {c:9s} mean at 1 s {A1[(r, c)].mean():5.1f} (SD {A1[(r, c)].std(ddof=1):4.1f}), at 62.5 ms {A1_short[(r, c)].mean():5.1f}\")\n\n# %% [markdown]\n# ## fig3a-example-tonotopy-removal\n#\n# > At the example site, randomizing the channel order of the temporal classifier lowers its\n# > single-trial accuracy at 1 s from 72% to 35%.\n\n# %% tags=[\"claim:fig3a-example-tonotopy-removal\"]\ni_ex = P1_SITES.index(P1_EXAMPLE)\nfor r in READ:\n    t, ts = A1[(r, \"temp\")][i_ex], A1[(r, \"temp_shuf\")][i_ex]\n    print(f\"{READ_TXT[r]}: temporal {t:.1f}% (PCs {R1[P1_EXAMPLE]['single']['pcs'][(r, 'temp')]}),\"\n          f\" without tonotopy {ts:.1f}%; within tolerance: {within(t, 72, 7.2)}, {within(ts, 35, 3.5)}; drop {t - ts:.1f} points\")\nprint(\"chance 20%\")\n\n# %% [markdown]\n# **Result: RES_FIG3A_TONO**\n\n# %% [markdown]\n# ## fig3a-example-classifier-order\n#\n# > At the example site, the spectro-temporal classifier performs best, followed by the\n# > spectral and temporal classifiers; the noiseless classifier exceeds the single-trial one\n# > for the spectral and spectro-temporal classifiers, while for the temporal classifier the\n# > two are similar.\n#\n# The noiseless classifier is run at the example site at 1 s only (500 ms shuffled model\n# windows, 1000 ms shuffled validation windows), which is what the criterion compares.\n\n# %% tags=[\"claim:fig3a-example-classifier-order\"]\nNL = R1[P1_EXAMPLE][\"noiseless\"]\nfor r in READ:\n    for st in (\"st_a\", \"st_b\"):\n        s_ = {c: A1[(r, c)][i_ex] for c in (st, \"spec\", \"temp\")}\n        n_ = {c: 100 * NL[\"acc\"][(r, c)][-1] for c in (st, \"spec\", \"temp\")}\n        order = s_[st] >= s_[\"spec\"] >= s_[\"temp\"]\n        nl_ok = (n_[st] - s_[st] >= 5) and (n_[\"spec\"] - s_[\"spec\"] >= 5) and abs(n_[\"temp\"] - s_[\"temp\"]) < 5\n        print(f\"{READ_TXT[r]}, a ({st[-1]}): single-trial st {s_[st]:.1f} spec {s_['spec']:.1f} temp {s_['temp']:.1f} | \"\n              f\"noiseless st {n_[st]:.1f} spec {n_['spec']:.1f} temp {n_['temp']:.1f} | order {order}, noiseless rule {nl_ok}\")\n\n# %% [markdown]\n# **Result: RES_FIG3A_ORDER**\n\n# %% [markdown]\n# ## fig3b-population-above-chance\n#\n# > Across the 13 paradigm 1 sites, all four single-trial classifiers (spectro-temporal,\n# > spectral, temporal, temporal without tonotopy) perform above chance at 1 s, improve with\n# > sound duration, and the temporal classifier is degraded substantially when tonotopy is\n# > removed.\n\n# %% tags=[\"claim:fig3b-population-above-chance\"]\nfor r in READ:\n    for st in (\"st_a\", \"st_b\"):\n        line, above = [], 0\n        for c in (st, \"spec\", \"temp\", \"temp_shuf\"):\n            t, p2, p1 = ttest_chance(A1[(r, c)], 20)\n            up = A1[(r, c)].mean() > A1_short[(r, c)].mean()\n            above += (p1 < 0.01) and (p2 < 0.01)\n            line.append(f\"{c} {A1[(r, c)].mean():.1f}% (p1 {p1:.1e}, p2 {p2:.1e}; 62.5 ms {A1_short[(r, c)].mean():.1f})\")\n        tp = stats.ttest_rel(A1[(r, \"temp\")], A1[(r, \"temp_shuf\")])\n        drop = (A1[(r, \"temp\")] - A1[(r, \"temp_shuf\")]).mean()\n        print(f\"{READ_TXT[r]}, a ({st[-1]}): \" + \"; \".join(line))\n        print(f\"    above chance at p < 0.01 (both sidednesses): {above}/4; tonotopy drop {drop:.1f} points, paired t = {tp.statistic:.2f}, p = {tp.pvalue:.1e}\")\nby_animal = {}\nfor s in P1_SITES:\n    by_animal.setdefault(desc[s][\"param\"][\"AnimalNo\"], []).append(P1_SITES.index(s))\nfor an, idx in by_animal.items():\n    print(\"animal\", an, f\"({len(idx)} sites), reading 1a2a, 1 s:\", {c: round(float(A1[(\"1a2a\", c)][idx].mean()), 1) for c in (\"st_a\", \"spec\", \"temp\", \"temp_shuf\")})\n\nfig, ax = plt.subplots(1, 4, figsize=(14, 2.6), sharey=True)\nfor a, c in zip(ax, (\"st_a\", \"spec\", \"temp\", \"temp_shuf\")):\n    M = np.array([100 * R1[s][\"single\"][\"acc\"][(\"1a2a\", c)] for s in P1_SITES])\n    a.errorbar(DUR, M.mean(0), M.std(0, ddof=1), color=\"r\"); a.set_xscale(\"log\"); a.axhline(20, color=\"gray\", ls=\":\")\n    a.set_title(c); a.set_xlabel(\"duration (ms)\")\nax[0].set_ylabel(\"% correct (1a2a)\"); plt.tight_layout(); plt.show()\n\n# %% [markdown]\n# **Result: RES_FIG3B**\n\n# %% [markdown]\n# ## figs6-per-sound-above-chance\n#\n# > Single-trial accuracy at 1 s exceeds chance for every sound and classifier except the snake\n# > sound with the temporal classifiers (p = 0.15 with tonotopy, 0.92 without).\n\n# %% tags=[\"claim:figs6-per-sound-above-chance\"]\nfor r in READ:\n    for st in (\"st_a\", \"st_b\"):\n        n_ok, snake = 0, {}\n        rows = []\n        for c in (st, \"spec\", \"temp\", \"temp_shuf\"):\n            M = np.array([100 * R1[s][\"single\"][\"acc_class\"][(r, c)][-1] for s in P1_SITES])  # sites, sounds\n            ps = []\n            for k, snd in enumerate(S.P1_SOUNDS):\n                t, p2, p1 = ttest_chance(M[:, k], 20)\n                ps.append((M[:, k].mean(), p2, p1))\n                if snd == \"snake\" and c in (\"temp\", \"temp_shuf\"):\n                    snake[c] = (M[:, k].mean(), p2, p1)\n                else:\n                    n_ok += (p2 < 0.05) and (t > 0)\n            rows.append(f\"{c}: \" + \", \".join(f\"{snd} {m:.0f}% p={p2:.2g}\" for snd, (m, p2, p1) in zip(S.P1_SOUNDS, ps)))\n        snake_ns = all(v[1] >= 0.05 or v[0] <= 20 for v in snake.values())\n        print(f\"{READ_TXT[r]}, a ({st[-1]}): {n_ok}/18 other conditions above chance (two-sided p < 0.05);\"\n              f\" snake temporal not above chance: {snake_ns}\")\n        for row in rows:\n            print(\"     \", row)\n\n# %% [markdown]\n# **Result: RES_FIGS6**\n\n# %% [markdown]\n# ## Paradigm 2 classifier\n\n# %%\nA2 = {}\nfor mode in (\"eq_3a\", \"eq_3b\", \"orig\"):\n    for di, lab in ((-1, \"1s\"), (0, \"short\")):\n        A2[(mode, lab)] = acc_table(R2, P2_SITES, key=mode, di=di)\nfor mode in (\"eq_3a\", \"eq_3b\", \"orig\"):\n    print(mode, {r: {c: round(float(A2[(mode, '1s')][(r, c)].mean()), 1) for c in CLF} for r in READ})\n\n# %% [markdown]\n# ## fig4-example-original-vs-equalized\n#\n# > At the example paradigm 2 site, neural correlations for the original and 1/f\n# > spectrum-equalized sounds are very similar (Pearson r = 0.92 +/- 0.01 spectral, 0.72 +/-\n# > 0.07 temporal, over five sounds).\n\n# %% tags=[\"claim:fig4-example-original-vs-equalized\"]\ndef r_pair(co, ce, diag):\n    if diag:\n        a, b = co[\"spec\"][\"sh\"].ravel(), ce[\"spec\"][\"sh\"].ravel()\n    else:\n        off = ~np.eye(16, dtype=bool)\n        a, b = co[\"spec\"][\"sh\"][off], ce[\"spec\"][\"sh\"][off]\n    return np.corrcoef(a, b)[0, 1], np.corrcoef(co[\"temp\"][\"sh\"].ravel(), ce[\"temp\"][\"sh\"].ravel())[0, 1]\n\ndef se(x):\n    return np.std(x, ddof=1) / np.sqrt(len(x))\n\nfor win in S.WINDOW_READINGS:\n    for diag in (True, False):\n        V = np.array([r_pair(R2[P2_EXAMPLE][\"corr_orig\"][k][win], R2[P2_EXAMPLE][\"corr_eq\"][k][win], diag) for k in range(5)])\n        print(f\"{win:9s} diagonal {'in ' if diag else 'out'}: spectral r {V[:, 0].mean():.3f} +/- {se(V[:, 0]):.3f},\"\n              f\" temporal r {V[:, 1].mean():.3f} +/- {se(V[:, 1]):.3f} | per sound spectral {np.round(V[:, 0], 2)}, temporal {np.round(V[:, 1], 2)}\"\n              f\" | within tol {within(V[:, 0].mean(), 0.92, 0.01)}, {within(V[:, 1].mean(), 0.72, 0.07)};\"\n              f\" within 10% {within(V[:, 0].mean(), 0.92, 0.092)}, {within(V[:, 1].mean(), 0.72, 0.072)}\")\n\n# %% [markdown]\n# **Result: RES_FIG4**\n\n# %% [markdown]\n# ## fig4e-population-original-vs-equalized\n#\n# > Across the 11 paradigm 2 sites, neural correlations for original and 1/f sounds correlate\n# > at r = 0.95 +/- 0.02 (spectral) and 0.80 +/- 0.02 (temporal) for the same sound, and less\n# > across different sounds (0.85 +/- 0.02 and 0.57 +/- 0.01).\n\n# %% tags=[\"claim:fig4e-population-original-vs-equalized\"]\nEXP4E = [(0.95, 0.02), (0.80, 0.02), (0.85, 0.02), (0.57, 0.01)]\nfor win in S.WINDOW_READINGS:\n    for diag in (True, False):\n        same, across = [], []\n        for s in P2_SITES:\n            co, ce = R2[s][\"corr_orig\"], R2[s][\"corr_eq\"]\n            same.append([r_pair(co[k][win], ce[k][win], diag) for k in range(5)])\n            across.append([r_pair(co[k][win], ce[j][win], diag) for k in range(5) for j in range(5) if j != k])\n        same, across = np.array(same), np.array(across)  # sites, pairs, 2\n        for avg in (\"a\", \"b\"):\n            if avg == \"a\":\n                v = [same[:, :, 0].mean(1), same[:, :, 1].mean(1), across[:, :, 0].mean(1), across[:, :, 1].mean(1)]\n            else:\n                v = [same[:, :, 0].ravel(), same[:, :, 1].ravel(), across[:, :, 0].ravel(), across[:, :, 1].ravel()]\n            m = [x.mean() for x in v]\n            hits = sum(within(mm, e, t) for mm, (e, t) in zip(m, EXP4E))\n            hits10 = sum(within(mm, e, 0.1 * e) for mm, (e, t) in zip(m, EXP4E))\n            print(f\"{win:9s} diag {'in ' if diag else 'out'} ({avg}): same spectral {m[0]:.3f}+/-{se(v[0]):.3f}, temporal {m[1]:.3f}+/-{se(v[1]):.3f};\"\n                  f\" across spectral {m[2]:.3f}+/-{se(v[2]):.3f}, temporal {m[3]:.3f}+/-{se(v[3]):.3f} | in tol {hits}/4, within 10% {hits10}/4,\"\n                  f\" same > across {m[0] > m[2] and m[1] > m[3]}\")\n\n# %% [markdown]\n# **Result: RES_FIG4E**\n\n# %% [markdown]\n# ## fig4f-example-equalized-classification\n#\n# > At the example paradigm 2 site, classifiers trained on the original sounds and tested on\n# > the 1/f sounds keep high accuracy (63% spectral, 63% temporal, 71% spectro-temporal, above\n# > chance), while the spectrum (rate) classifier falls from about 94% on the original sounds to\n# > chance.\n\n# %% tags=[\"claim:fig4f-example-equalized-classification\"]\ni2 = P2_SITES.index(P2_EXAMPLE)\nfor mode in (\"eq_3a\", \"eq_3b\"):\n    for r in READ:\n        for st in (\"st_a\", \"st_b\"):\n            v = {c: A2[(mode, \"1s\")][(r, c)][i2] for c in (\"spec\", \"temp\", st, \"rate\")}\n            v_orig_rate = A2[(\"orig\", \"1s\")][(r, \"rate\")][i2]\n            hits = within(v[\"spec\"], 63, 6.3) + within(v[\"temp\"], 63, 6.3) + within(v[st], 71, 7.1) + within(v_orig_rate, 94, 9.4)\n            pc = R2[P2_EXAMPLE][mode][\"acc_class\"]\n            tt = {}\n            for c in (\"spec\", \"temp\", st):\n                per_sound = 100 * pc[(r, c)][-1]\n                tt[c] = ttest_chance(per_sound, 20)[1]\n            pattern = min(v[\"spec\"], v[\"temp\"], v[st]) > 40 and v[\"rate\"] < 30\n            print(f\"{mode} {r} a({st[-1]}): 1/f spec {v['spec']:.0f} temp {v['temp']:.0f} st {v[st]:.0f} rate {v['rate']:.0f};\"\n                  f\" original rate {v_orig_rate:.0f} | in tol {hits}/4, 1/f rate < 30 {v['rate'] < 30}, pattern {pattern} |\"\n                  f\" t test over 5 sounds p: \" + \", \".join(f\"{c} {p:.2g}\" for c, p in tt.items()))\n# reading (b) of the within-site test: over the classification iterations (samples), reading (1a)\nfor mode in (\"eq_3a\", \"eq_3b\"):\n    for c in (\"spec\", \"temp\"):\n        a = A2[(mode, \"1s\")][(\"1a2a\", c)][i2] / 100\n        n = 100 * 5 * (2 if mode == \"eq_3a\" else 1)\n        z = (a - 0.2) / np.sqrt(0.2 * 0.8 / n)\n        print(f\"{mode} {c}: over {n} samples, accuracy {100 * a:.0f}%, one-sample z against 20% = {z:.1f}\")\n\n# %% [markdown]\n# **Result: RES_FIG4F**\n\n# %% [markdown]\n# ## fig4h-population-equalized-classification\n#\n# > Across 11 paradigm 2 sites, the correlation classifiers stay above chance on the 1/f\n# > sounds at 1 s (spectral 48%, temporal 49%, spectro-temporal 58%), while the spectrum\n# > classifier exceeds all three correlation classifiers on the original sounds (90.0 +/-\n# > 2.0%) but falls to 27.0 +/- 1.0% on the 1/f sounds and does not substantially improve with\n# > duration.\n\n# %% tags=[\"claim:fig4h-population-equalized-classification\"]\nfor mode in (\"eq_3a\", \"eq_3b\"):\n    for r in READ:\n        for st in (\"st_a\", \"st_b\"):\n            T = A2[(mode, \"1s\")]\n            v = {c: T[(r, c)] for c in (\"spec\", \"temp\", st, \"rate\")}\n            vo = A2[(\"orig\", \"1s\")][(r, \"rate\")]\n            ps = {c: ttest_chance(v[c], 20) for c in (\"spec\", \"temp\", st)}\n            tests = all(p[1] < 0.01 and p[0] > 0 for p in ps.values())\n            hits = (within(v[\"spec\"].mean(), 48, 4.8) + within(v[\"temp\"].mean(), 49, 4.9) + within(v[st].mean(), 58, 5.8)\n                    + within(vo.mean(), 90, 2) + within(v[\"rate\"].mean(), 27, 1))\n            below = v[\"rate\"].mean() < min(v[\"spec\"].mean(), v[\"temp\"].mean(), v[st].mean())\n            rate_short = A2[(mode, \"short\")][(r, \"rate\")].mean()\n            orig_corr = {c: A2[(\"orig\", \"1s\")][(r, c)].mean() for c in (\"spec\", \"temp\", st)}\n            print(f\"{mode} {r} a({st[-1]}): 1/f spec {v['spec'].mean():.1f} temp {v['temp'].mean():.1f} st {v[st].mean():.1f}\"\n                  f\" (p2 {', '.join(f'{p[1]:.1e}' for p in ps.values())}) | rate 1/f {v['rate'].mean():.1f}+/-{se(v['rate']):.1f}\"\n                  f\" (62.5 ms {rate_short:.1f}), rate original {vo.mean():.1f}+/-{se(vo):.1f}; original correlation classifiers\"\n                  f\" {', '.join(f'{c} {x:.1f}' for c, x in orig_corr.items())} | tests {tests}, in tol {hits}/5, rate lowest on 1/f {below}\")\n\n# %% [markdown]\n# **Result: RES_FIG4H**\n\n# %% [markdown]\n# ## Mixing coefficient a, paradigms 1 and 2 (used by figs9-mixing-coefficient)\n#\n# The claim is decided in the paradigm 3 notebook, which also has the paradigm 3 values; the\n# paradigm 1 and 2 values are printed here and recomputed there from the same rule on this\n# notebook's printed output only for the record (the outcome uses both notebooks' outputs).\n\n# %% tags=[\"claim:figs9-mixing-coefficient\"]\nfor r in READ:\n    for asel in (\"a\", \"b\"):\n        a1 = np.array([R1[s][\"single\"][\"alpha\"][(r, asel)] for s in P1_SITES])\n        a2 = np.array([R2[s][\"eq_3a\"][\"alpha\"][(r, asel)] for s in P2_SITES])\n        a2b = np.array([R2[s][\"eq_3b\"][\"alpha\"][(r, asel)] for s in P2_SITES])\n        pooled = np.concatenate([a1, a2])\n        print(f\"{r} a chosen on ({asel}): P1 median {np.median(a1):.2f} (quartiles {np.percentile(a1, 25):.2f}, {np.percentile(a1, 75):.2f});\"\n              f\" P2 (3a) median {np.median(a2):.2f}; P2 (3b) median {np.median(a2b):.2f}; pooled 24 sites median {np.median(pooled):.2f}\"\n              f\" (quartiles {np.percentile(pooled, 25):.2f}, {np.percentile(pooled, 75):.2f})\")\n        print(\"     P1 values\", a1, \" P2 (3a) values\", a2)\n\n# %% [markdown]\n# ## Summary\n#\n# SUMMARY\n\n# %%\nprint(f\"total run time {(time.time() - T_START) / 60:.1f} min\")\n"
}
```

```
File created successfully at: entries/sadeghi-2019/src_neural.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019 && python3 - <<'EOF'
s=open('sadeghi.py').read()
old=s[s.index('        for k in kinds:\n            Xm = _features(fm, "temp" if k == "temp_shuf" else k)'):s.index('    kk = {k: min(x.shape[0] for x in LL[k]) for k in kinds}')]
new='''        base = [k for k in kinds if k != "temp_shuf"]
        for k in base:
            Xm = _features(fm, k)
            group = [k] + (["temp_shuf"] if k == "temp" and "temp_shuf" in kinds else [])
            Xvs = [np.concatenate([_features(v[0], g, rng) for v in vals]) for g in group]
            Xin_v = _features(fm, k, rng)
            grid = loglik_grid(Xm, ym, np.concatenate(Xvs + [Xin_v]), kmax)
            for gi, g in enumerate(group):
                LL[g].append(grid[:, gi * len(yv):(gi + 1) * len(yv)])
                LLin[g].append(grid[:, len(group) * len(yv):])
            inner = (loglik_grid(Xm[half], ym[half], Xin_v[~half], kmax), ym[~half])
            for g in group:
                LLinner[g].append(inner)
'''
s=s.replace(old,new)
# float32 temporal features
s=s.replace('''    S = np.empty((n, len(iu[0])))
    T = np.empty((n, C, 2 * maxlag + 1))''','''    S = np.empty((n, len(iu[0])))
    T = np.empty((n, C, 2 * maxlag + 1), dtype=np.float32)''')
s+='''

def process_p3(d, rng, n=100):
    """Paradigm 3 site: three categories, six exemplars, leave one exemplar out (five train,
    the sixth is tested, for every category at once). Reading (a): model and validation
    windows anywhere in the whole response; reading (b): the half split on top (model from
    one half of the training exemplars, validation from the other half of the held-out one)."""
    ras = {k: v for k, v in d["ras"].items()}
    ns = min(r.shape[-1] for r in ras.values())
    whole = (0.0, ns / FS * 1000)
    hr = half_ranges(ns)
    out = {}
    for reading, ranges in (("a", [whole]), ("b", hr)):
        fm = {(c, e, h): single_trial_features(ras[(c, e)], n, 1000.0, ranges[h], rng)
              for c in range(3) for e in range(6) for h in range(len(ranges))}
        fv = {(c, e, h, di): single_trial_features(ras[(c, e)], n, dd, ranges[h], rng)
              for c in range(3) for e in range(6) for h in range(len(ranges)) for di, dd in enumerate(DURATIONS_MS)}
        folds = []
        for e_out in range(6):
            for h in range(len(ranges)):
                hv = h if reading == "a" else 1 - h
                model = (_cat([fm[(c, e, h)] for c in range(3) for e in range(6) if e != e_out]),
                         np.concatenate([np.full(n, c) for c in range(3) for e in range(6) if e != e_out]))
                vals = [(_cat([fv[(c, e_out, hv, di)] for c in range(3)]), np.concatenate([np.full(n, c) for c in range(3)]))
                        for di in range(len(DURATIONS_MS))]
                folds.append((model, vals))
        out[reading] = classify(folds, P3_CATEGORIES, kinds=KINDS, rng=rng)
        del fm, fv, folds
    return out


def p3_example_pca(d, rng, n=100):
    """Variance explained by the first two PCs of the training-set feature vectors
    (100 observations x 6 exemplars x 3 categories, Fig 8 legend) under the readings of
    claim fig8b-example-pca-variance, and a nearest-centroid leave-one-exemplar-out accuracy
    in the two-PC space."""
    ras = d["ras"]
    ns = min(r.shape[-1] for r in ras.values())
    whole = (0.0, ns / FS * 1000)
    feats = {}
    for lab, maker, ms in (("a_sh500", shuffled_features, 500.0), ("b_st1000", single_trial_features, 1000.0),
                           ("b_sh1000", shuffled_features, 1000.0)):
        feats[lab] = {(c, e): maker(ras[(c, e)], n, ms, whole, rng) for c in range(3) for e in range(6)}
    C = 16
    iu_d = np.triu_indices(C)
    out = {}
    for lab, F in feats.items():
        for spec_r in ("c", "d"):
            for kind in ("spec", "temp"):
                def X_of(f):
                    if kind == "temp":
                        return f["temp"].reshape(len(f["temp"]), -1).astype(np.float64)
                    if lab.startswith("b_st"):  # single trial: upper triangle without the diagonal (all 1)
                        M = np.zeros((len(f["spec"]), C, C))
                        iu = np.triu_indices(C, 1)
                        M[:, iu[0], iu[1]] = f["spec"]
                        M = M + M.transpose(0, 2, 1) + np.eye(C)
                    else:
                        M = np.zeros((len(f["spec"]), C, C))
                        M[:, iu_d[0], iu_d[1]] = f["spec"]
                        M = M + np.triu(M, 1).transpose(0, 2, 1)
                    if spec_r == "c":
                        return M[:, iu_d[0], iu_d[1]]
                    return M.reshape(len(M), -1)
                if kind == "temp" and spec_r == "d":
                    continue
                Xs = {k: X_of(f) for k, f in F.items()}
                X = np.concatenate([Xs[(c, e)] for c in range(3) for e in range(6)])
                y = np.concatenate([np.full(len(Xs[(c, e)]), c) for c in range(3) for e in range(6)])
                ex = np.concatenate([np.full(len(Xs[(c, e)]), e) for c in range(3) for e in range(6)])
                ev_all = PCA().fit(X).evr[:2].sum()
                ev_f, acc = [], []
                for e_out in range(6):
                    p = PCA().fit(X[ex != e_out])
                    ev_f.append(p.evr[:2].sum())
                    Z = p.transform(X, 2)
                    cents = np.array([Z[(ex != e_out) & (y == c)].mean(0) for c in range(3)])
                    zt = Z[ex == e_out]
                    pred = np.argmin(((zt[:, None] - cents) ** 2).sum(-1), 1)
                    acc.append((pred == y[ex == e_out]).mean())
                out[(lab, spec_r, kind)] = {"ev_all6": 100 * ev_all, "ev_folds": 100 * np.mean(ev_f),
                                            "nc_acc": 100 * np.mean(acc)}
    return out
'''
open('sadeghi.py','w').write(s)
EOF
echo done
```

```
done
```

**Agent**

Timing paradigm 3 on its first site:

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > dev4.py <<'EOF'
import sys, time, numpy as np, resource
sys.path.insert(0,'entries/sadeghi-2019')
import sadeghi as S
for name, raw in S.stream_members(lambda n: n.endswith("P3_Site09.mat")):
    d=S.read_site(name, raw); break
del raw
rng=np.random.default_rng(3)
t=time.time(); out=S.process_p3(d, rng); print('p3', time.time()-t)
for rd in out:
    for k,v in out[rd]['acc'].items():
        if k[0]=='1a2a' or k[0]=='1b2b': print(rd, k, np.round(100*v,0))
    print(out[rd]['alpha'])
print('maxrss MB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
t=time.time(); pc=S.p3_example_pca(d, rng); print('pca', time.time()-t)
for k,v in pc.items(): print(k, {a: round(b,1) for a,b in v.items()})
print('maxrss MB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
EOF
python dev4.py
```

```
p3 73.75976943969727
a ('1a2a', 'spec') [51. 58. 65. 72. 78. 83. 87. 92. 95.]
a ('1a2a', 'temp') [69. 75. 80. 84. 87. 90. 93. 96. 97.]
a ('1a2a', 'temp_shuf') [70. 75. 78. 84. 86. 89. 91. 94. 96.]
a ('1a2a', 'rate') [75. 79. 83. 87. 89. 92. 92. 92. 91.]
a ('1a2a', 'st_a') [54. 60. 69. 77. 82. 86. 90. 94. 96.]
a ('1a2a', 'st_b') [69. 75. 80. 85. 88. 90. 93. 96. 97.]
a ('1b2b', 'spec') [ 89.  89.  94.  94.  94. 100. 100. 100. 100.]
a ('1b2b', 'temp') [50. 56. 72. 89. 94. 94. 94. 94. 94.]
a ('1b2b', 'temp_shuf') [67. 83. 83. 94. 94. 94. 94. 94. 94.]
a ('1b2b', 'rate') [72. 72. 78. 83. 89. 89. 89. 94. 89.]
a ('1b2b', 'st_a') [ 89.  89.  94.  94.  94. 100. 100. 100. 100.]
a ('1b2b', 'st_b') [ 72.  94.  94.  94.  94.  94.  94. 100. 100.]
{('1a2a', 'a'): np.float64(0.9), ('1a2a', 'b'): np.float64(0.1), ('1a2b', 'a'): np.float64(1.0), ('1a2b', 'b'): np.float64(0.8), ('1b2a', 'a'): np.float64(0.8), ('1b2a', 'b'): np.float64(0.2), ('1b2b', 'a'): np.float64(1.0), ('1b2b', 'b'): np.float64(0.8)}
b ('1a2a', 'spec') [53. 59. 68. 74. 80. 86. 88. 92. 95.]
b ('1a2a', 'temp') [72. 77. 81. 85. 88. 92. 94. 95. 97.]
b ('1a2a', 'temp_shuf') [70. 76. 81. 83. 86. 89. 91. 91. 93.]
b ('1a2a', 'rate') [74. 78. 80. 84. 86. 87. 89. 89. 91.]
b ('1a2a', 'st_a') [53. 59. 68. 74. 80. 86. 88. 92. 95.]
b ('1a2a', 'st_b') [68. 74. 80. 84. 88. 91. 93. 95. 97.]
[... 20 more lines not kept]
```

**Agent**

Paradigm 3 costs 74 s per site; the whole neural notebook should take about 35 minutes. Adding the paradigm 3 sections to the notebook.

**Agent calls Bash**

```bash
cd entries/sadeghi-2019 && python3 - <<'EOF'
s=open('src_neural.py').read()
s=s.replace("# Sadeghi et al. (2019): neural claims, paradigms 1 and 2 (CRCNS bst-2)","# Sadeghi et al. (2019): neural claims (CRCNS bst-2)")
s=s.replace('''P1_EXAMPLE, P2_EXAMPLE = "P1_Site04", "P2_Site11"  # data set's FigureData list (finding aid)
SEED = {"P1": 101, "P2": 202}''','''P1_EXAMPLE, P2_EXAMPLE, P3_EXAMPLE = "P1_Site04", "P2_Site11", "P3_Site04"  # data set's FigureData list (finding aid)
SEED = {"P1": 101, "P2": 202, "P3": 303, "P3pca": 304}''')
s=s.replace('''# One pass over the tar stream. Each paradigm 1 and 2 file is parsed in memory, reduced to
# its correlations and classifier results, and released before the next one is read. The
# paradigm 3 files come first in the stream and are skipped here (second notebook).''','''# One pass over the tar stream. Each neural file is parsed in memory, reduced to its
# correlations and classifier results, and released before the next one is read.''')
s=s.replace('''desc, R1, R2 = {}, {}, {}
for name, raw in S.stream_members(lambda n: "/Paradigm1/P1_" in n or "/Paradigm2/P2_" in n):''','''desc, R1, R2, R3 = {}, {}, {}, {}
for name, raw in S.stream_members(lambda n: "/NeuralData/Paradigm" in n and n.endswith(".mat")):''')
s=s.replace('''    else:
        R2[site] = S.process_p2(d, np.random.default_rng(SEED["P2"] * 100 + i))
    del d''','''    elif site.startswith("P2"):
        R2[site] = S.process_p2(d, np.random.default_rng(SEED["P2"] * 100 + i))
    else:
        R3[site] = S.process_p3(d, np.random.default_rng(SEED["P3"] * 100 + i))
        if site == P3_EXAMPLE:
            PCA3 = S.p3_example_pca(d, np.random.default_rng(SEED["P3pca"]))
    del d''')
s=s.replace('P1_SITES, P2_SITES = sorted(R1), sorted(R2)','P1_SITES, P2_SITES, P3_SITES = sorted(R1), sorted(R2), sorted(R3)')
s=s.replace('''print("files:", len(P1_SITES), "paradigm 1 sites,", len(P2_SITES), "paradigm 2 sites")''','''print("files:", len(P1_SITES), "paradigm 1 sites,", len(P2_SITES), "paradigm 2 sites,", len(P3_SITES), "paradigm 3 sites")''')
s=s.replace('''for site in P1_SITES + P2_SITES:
    s = desc[site]''','''for site in P1_SITES + P2_SITES + P3_SITES:
    s = desc[site]''')
s=s.replace('''for p, sites in (("P1", P1_SITES), ("P2", P2_SITES)):''','''for p, sites in (("P1", P1_SITES), ("P2", P2_SITES), ("P3", P3_SITES)):''')
s=s.replace('''seen = {}
for site in P1_SITES + P2_SITES:''','''seen = {}
for site in P1_SITES + P2_SITES + P3_SITES:''')
s=s.replace('''print("identical rasters found:", len(dups), dups[:5])''','''print("identical rasters found:", len(dups), dups[:5])
same_block = {}
for site in P2_SITES + P3_SITES:
    p = desc[site]["param"]
    same_block.setdefault((p["AnimalNo"], p["RecordDate"]), []).append((site, p["BlockNo"]))
print("paradigm 2 and 3 files by animal and date (site, block):", same_block)''')
# cut figs9 section from current place
i=s.index('# %% [markdown]\n# ## Mixing coefficient a, paradigms 1 and 2')
j=s.index('# %% [markdown]\n# ## Summary')
s=s[:i]+open('/dev/stdin').read() if False else s[:i]+'''#P3SECTIONS#
'''+s[j:]
p3='''# %% [markdown]
# ## fig8b-example-pca-variance
#
# > At the example paradigm 3 site, the first two principal components explain 95.6% of the
# > variance of the spectral and 85.9% of the temporal neural correlations, and the three
# > categories form distinct clusters.
#
# Readings: (a) 500 ms shuffled (stimulus-driven) windows, (b) 1000 ms windows, run with
# single-trial correlations and, as a variant, shuffled ones; (e) all six exemplars, (f) the
# five-exemplar training sets averaged over folds; spectral features (c) upper triangle with
# diagonal, (d) full matrix. 100 windows per exemplar over the whole response.

# %% tags=["claim:fig8b-example-pca-variance"]
for lab in ("a_sh500", "b_st1000", "b_sh1000"):
    for sr in ("c", "d"):
        sp = PCA3[(lab, sr, "spec")]
        te = PCA3[(lab, "c", "temp")]
        for tr in ("ev_all6", "ev_folds"):
            ok = within(sp[tr], 95.6, 9.56) and within(te[tr], 85.9, 8.59)
            print(f"{lab} spectral ({sr}) training set {'(e) six' if tr == 'ev_all6' else '(f) five, folds'}:"
                  f" spectral {sp[tr]:.1f}%, temporal {te[tr]:.1f}% | both in tolerance {ok} |"
                  f" nearest-centroid accuracy in 2 PCs: spectral {sp['nc_acc']:.1f}%, temporal {te['nc_acc']:.1f}% (chance 33.3%)")

# %% [markdown]
# **Result: RES_FIG8B**

# %% [markdown]
# ## Paradigm 3 classifier

# %%
A3 = {rd: {} for rd in ("a", "b")}
for rd in ("a", "b"):
    for di, lab in ((-1, "1s"), (0, "short")):
        A3[rd][lab] = {(r, c): np.array([100 * R3[s][rd]["acc"][(r, c)][di] for s in P3_SITES]) for r in READ for c in CLF}
for rd in ("a", "b"):
    for r in READ:
        print(f"reading ({rd}) {r}:", {c: round(float(A3[rd]['1s'][(r, c)].mean()), 1) for c in CLF})

# %% [markdown]
# ## fig8e-example-categorization
#
# > At the example paradigm 3 site, all correlation classifiers approach 100% correct
# > categorization at 1 s, and the spectrum (rate) classifier reaches 94%.

# %% tags=["claim:fig8e-example-categorization"]
i3 = P3_SITES.index(P3_EXAMPLE)
for rd in ("a", "b"):
    for r in READ:
        for st in ("st_a", "st_b"):
            v = {c: A3[rd]["1s"][(r, c)][i3] for c in (st, "spec", "temp", "rate")}
            v0 = {c: A3[rd]["short"][(r, c)][i3] for c in (st, "spec", "temp")}
            ok90 = all(v[c] >= 90 for c in (st, "spec", "temp"))
            up = all(v[c] > v0[c] for c in (st, "spec", "temp"))
            print(f"({rd}) {r} a({st[-1]}): 1 s st {v[st]:.0f} spec {v['spec']:.0f} temp {v['temp']:.0f} rate {v['rate']:.0f};"
                  f" 62.5 ms st {v0[st]:.0f} spec {v0['spec']:.0f} temp {v0['temp']:.0f} | all >= 90 {ok90}, rise {up},"
                  f" rate in tol {within(v['rate'], 94, 9.4)}")

# %% [markdown]
# **Result: RES_FIG8E**

# %% [markdown]
# ## fig8f-population-categorization
#
# > Across 11 paradigm 3 sites, at 1 s the spectro-temporal classifier categorizes 96% of
# > trials correctly, the temporal 95%, the spectral 91% and the spectrum (rate) classifier 91%,
# > all above chance, and performance improves with duration.

# %% tags=["claim:fig8f-population-categorization"]
for rd in ("a", "b"):
    for r in READ:
        for st in ("st_a", "st_b"):
            T = A3[rd]["1s"]
            v = {c: T[(r, c)] for c in (st, "temp", "spec", "rate")}
            exp = {st: (96, 9.6), "temp": (95, 9.5), "spec": (91, 9.1), "rate": (91, 9.1)}
            hits = sum(within(min(v[c].mean(), 100), *exp[c]) or (v[c].mean() >= exp[c][0] - exp[c][1]) for c in v)
            ps = {c: ttest_chance(v[c], 100 / 3) for c in v}
            tests = all(p[1] < 0.01 and p[0] > 0 for p in ps.values())
            up = all(v[c].mean() > A3[rd]["short"][(r, c)].mean() for c in v)
            print(f"({rd}) {r} a({st[-1]}): " + ", ".join(f"{c} {v[c].mean():.1f}+/-{se(v[c]):.1f} (p2 {ps[c][1]:.1e}; 62.5 ms {A3[rd]['short'][(r, c)].mean():.1f})" for c in v)
                  + f" | in tol {hits}/4, tests {tests}, rise {up}")
by_animal = {}
for s in P3_SITES:
    by_animal.setdefault(desc[s]["param"]["AnimalNo"], []).append(P3_SITES.index(s))
for an, idx in by_animal.items():
    print("animal", an, f"({len(idx)} sites), reading (a) 1a2a, 1 s:", {c: round(float(A3["a"]["1s"][("1a2a", c)][idx].mean()), 1) for c in ("st_a", "spec", "temp", "rate")})

# %% [markdown]
# **Result: RES_FIG8F**

# %% [markdown]
# ## figs9-mixing-coefficient
#
# > The optimal spectro-temporal classifier weights spectral and temporal cues about equally,
# > with a median mixing coefficient of 0.6 (quartiles 0.5 and 0.7) for paradigms 1 and 2 and
# > 0.5 (25th percentile 0.4) for paradigm 3.
#
# a in 0 to 1 in steps of 0.1, per site, chosen to maximise the log-posterior of the true
# sound summed over (a) the model data or (b) the validation data. Paradigm 2 uses its
# original-to-1/f classifier, reading (3)(a); paradigm 3 its readings (a) and (b).

# %% tags=["claim:figs9-mixing-coefficient"]
for r in READ:
    for asel in ("a", "b"):
        a1 = np.array([R1[s]["single"]["alpha"][(r, asel)] for s in P1_SITES])
        a2 = np.array([R2[s]["eq_3a"]["alpha"][(r, asel)] for s in P2_SITES])
        pooled = np.concatenate([a1, a2])
        line = (f"{r} a on ({asel}) data: P1 median {np.median(a1):.2f}, P2 median {np.median(a2):.2f},"
                f" pooled 24 sites median {np.median(pooled):.2f} (quartiles {np.percentile(pooled, 25):.2f}, {np.percentile(pooled, 75):.2f})")
        for rd in ("a", "b"):
            a3 = np.array([R3[s][rd]["alpha"][(r, asel)] for s in P3_SITES])
            ok_c = within(np.median(pooled), 0.6, 0.1) and within(np.median(a3), 0.5, 0.1)
            ok_d = within(np.median(a1), 0.6, 0.1) and within(np.median(a2), 0.6, 0.1) and within(np.median(a3), 0.5, 0.1)
            line += (f" | P3 ({rd}) median {np.median(a3):.2f} (25th pct {np.percentile(a3, 25):.2f});"
                     f" pooled rule {ok_c}, per-paradigm rule {ok_d}")
        print(line)

# %% [markdown]
# **Result: RES_FIGS9**

'''
s=s.replace('#P3SECTIONS#\n',p3)
open('src_neural.py','w').write(s)
EOF
grep -n "Mixing coefficient a, paradigms" src_neural.py; date -u
```

```
Fri Nov 13 20:30:46 UTC 2026
```

**Agent**

Subset run of the whole neural notebook (2 sites per paradigm, including the example sites where reachable early) to exercise every cell:

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && E=entries/sadeghi-2019 && python - <<'EOF'
s=open('entries/sadeghi-2019/src_neural.py').read()
s=s.replace('lambda n: "/NeuralData/Paradigm" in n and n.endswith(".mat")','lambda n: n.split("/")[-1][:-4] in ("P3_Site09","P3_Site04","P1_Site09","P1_Site04","P2_Site04","P2_Site05")')
s=s.replace('P2_EXAMPLE, P3_EXAMPLE = "P1_Site04", "P2_Site11", "P3_Site04"','P2_EXAMPLE, P3_EXAMPLE = "P1_Site04", "P2_Site05", "P3_Site04"')
s=s.replace('    print(f"{site} done at {time.time() - T_START:.0f} s", flush=True)','    print(f"{site} done at {time.time() - T_START:.0f} s", flush=True)\n    if site == "P2_Site05": break')
open('dev_neural.py','w').write(s)
EOF
jupytext --to ipynb -q dev_neural.py -o dev_neural.ipynb && cp $E/sadeghi.py . && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 dev_neural.ipynb --output dev_neural_out.ipynb 2>&1 | tail -5
```

```
[NbConvertApp] Converting notebook dev_neural.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 324945 bytes to dev_neural_out.ipynb

real	13m30.087s
user	13m17.772s
sys	0m14.532s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
import json
nb=json.load(open('dev_neural_out.ipynb'))
for c in nb['cells']:
    if c['cell_type']!='code': continue
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain')
        if t:
            t=''.join(t); print(t[:3500]); print('-----')
EOF
```

```
<persisted-output>
Output too large (42.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/e9eb191a-8d7b-4aaf-a4ab-b5af6e6452e6/tool-results/bh0xw3ko1.txt

Preview (first 2KB):
P3_Site09 done at 94 s

-----
P3_Site04 done at 305 s

-----
P1_Site09 done at 538 s

-----
P1_Site04 done at 706 s

-----
P2_Site04 done at 773 s

-----
P2_Site05 done at 805 s
[... 23 more lines not kept]
```

**Agent**

The subset run worked end to end (13.5 min). Paradigm 1 sites took far longer than in the earlier test, so I'll profile `process_p1` on rasters from the first file.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > prof.py <<'EOF'
import sys, time, numpy as np, cProfile, pstats
sys.path.insert(0,'entries/sadeghi-2019')
import sadeghi as S
for name, raw in S.stream_members(lambda n: n.endswith("P3_Site09.mat")):
    d=S.read_site(name, raw); break
fake={"ras":{(k,0): d["ras"][(k%3,k)] for k in range(5)}}
t=time.time()
cProfile.run('S.process_p1(fake, np.random.default_rng(0))','prof.out')
print(time.time()-t)
pstats.Stats('prof.out').sort_stats('cumtime').print_stats(15)
EOF
python prof.py 2>&1 | head -50
```

```
10.6419837474823
Fri Nov 13 20:45:23 2026    prof.out

         751401 function calls (751188 primitive calls) in 10.640 seconds

   Ordered by: cumulative time
   List reduced from 584 to 15 due to restriction <15>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     12/1    0.000    0.000   10.640   10.640 {built-in method builtins.exec}
        1    0.003    0.003   10.635   10.635 <string>:1(<module>)
        4    0.001    0.000    8.561    2.140 /opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/asyncio/base_events.py:1981(_run_once)
      100    0.058    0.001    7.051    0.071 entries/sadeghi-2019/sadeghi.py:258(single_trial_features)
    10000    0.984    0.000    6.864    0.001 entries/sadeghi-2019/sadeghi.py:229(_single)
    30250    5.774    0.000    5.785    0.000 /tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/fft/_pocketfft.py:58(_raw_fft)
    10050    0.390    0.000    5.625    0.001 entries/sadeghi-2019/sadeghi.py:98(_xcorr)
        1    0.000    0.000    4.440    4.440 entries/sadeghi-2019/sadeghi.py:498(build_folds)
    20150    0.010    0.000    4.385    0.000 /tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/fft/_pocketfft.py:324(rfft)
        5    0.000    0.000    2.097    0.419 entries/sadeghi-2019/sadeghi.py:199(correlation_readings)
       25    0.001    0.000    2.096    0.084 entries/sadeghi-2019/sadeghi.py:186(site_correlations)
[... 5 more lines not kept]
```

**Agent**

Profiled alone, `process_p1` takes 10 s, so the slowness lies elsewhere. Timing each step on a real paradigm 1 file:

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > prof2.py <<'EOF'
import sys, time, numpy as np
sys.path.insert(0,'entries/sadeghi-2019')
import sadeghi as S
t=time.time()
for name, raw in S.stream_members(lambda n: n.endswith("P1_Site09.mat")):
    print('stream', time.time()-t); t=time.time()
    d=S.read_site(name, raw); print('read', time.time()-t); t=time.time()
    ds=S.describe(d); print('describe', time.time()-t); t=time.time()
    ras=[d["ras"][(k,0)] for k in range(5)]
    c=[S.correlation_readings(r) for r in ras]; print('corr', time.time()-t); t=time.time()
    hr=S.half_ranges(6104); rng=np.random.default_rng(0)
    folds=S.build_folds([[r] for r in ras], [[r] for r in ras], hr, hr[::-1], rng); print('feat', time.time()-t); t=time.time()
    res=S.classify(folds, S.P1_SOUNDS, kinds=S.KINDS, rng=rng); print('classify', time.time()-t)
    break
EOF
python prof2.py
```

```
stream 124.16843247413635
read 0.5403470993041992
describe 0.03450584411621094
corr 4.28023099899292
feat 7.142427921295166
classify 1.4583637714385986
Shell cwd was reset to
```

**Agent**

Each step is fast (13 s per site); the gap was in streaming. The full run should take 30 to 40 minutes. Checking the subset outputs for errors:

**Agent calls Bash**

```bash
sed -n 1,400p /home/runner/.claude/projects/-home-runner-work-encore-encore/e9eb191a-8d7b-4aaf-a4ab-b5af6e6452e6/tool-results/bh0xw3ko1.txt | cut -c1-400 | sed -n 30,200p
```

```
P1 sites per animal: {'0315011': 1, '0116012': 1}
P1 trials per sound, range 27 to 39
P2 sites per animal: {'0417015': 2}
P2 trials per sound, range 20 to 20
P3 sites per animal: {'0417015': 2}
P3 trials per sound, range 10 to 20
identical rasters found: 0 []
paradigm 2 and 3 files by animal and date (site, block): {('0417015', 'May2019'): [('P2_Site04', '029'), ('P2_Site05', '033'), ('P3_Site04', '030'), ('P3_Site09', '047')]}

-----
durations (ms): [  62.5   88.4  125.   176.8  250.   353.6  500.   707.1 1000. ]

-----
window whole     curve mean  : crowd 50% 2.8, water 50% 3.3, fire 50% 4.4, crowd 10% 5.7, water 10% 7.9, fire 10% 10.9, bird 50% 5.4, bird 10% 138.8, snake 50% 6.9, snake 10% 18.8
    snake side peak, channels 9-16 52.1 ms (height 0.070), channels 1-8 52.1 ms (height 0.010)
    widths within tolerance 7/10; with the period (9-16) 8/11, (1-8) 8/11; crowd and water narrower than fire at 50%: True
window whole     curve median: crowd 50% 2.7, water 50% 3.3, fire 50% 4.1, crowd 10% 5.1, water 10% 7.1, fire 10% 12.0, bird 50% 5.7, bird 10% 51.4, snake 50% 6.9, snake 10% 19.3
    snake side peak, channels 9-16 52.1 ms (height 0.070), channels 1-8 52.1 ms (height 0.010)
    widths within tolerance 7/10; with the period (9-16) 8/11, (1-8) 8/11; crowd and water narrower than fire at 50%: True
window w1000     curve mean  : crowd 50% 2.8, water 50% 3.2, fire 50% 4.3, crowd 10% 5.7, water 10% 7.6, fire 10% 10.8, bird 50% 5.3, bird 10% 50.2, snake 50% 6.7, snake 10% 18.4
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,400p /home/runner/.claude/projects/-home-runner-work-encore-encore/e9eb191a-8d7b-4aaf-a4ab-b5af6e6452e6/tool-results/bh0xw3ko1.txt | cut -c1-330 | grep -v "^      " | head -90; date -u
```

```
(1b) 100 samples summed, (2a) PCs on validation, a (a): 11/18 other conditions above chance (two-sided p < 0.05); snake temporal not above chance: True
(1b) 100 samples summed, (2a) PCs on validation, a (b): 12/18 other conditions above chance (two-sided p < 0.05); snake temporal not above chance: True
(1b) 100 samples summed, (2b) PCs on an inner split, a (a): 10/18 other conditions above chance (two-sided p < 0.05); snake temporal not above chance: True
-----
eq_3a {'1a2a': {'st_a': 53.8, 'st_b': 57.9, 'spec': 53.8, 'temp': 58.3, 'temp_shuf': 52.6, 'rate': 31.8}, '1a2b': {'st_a': 47.5, 'st_b': 53.0, 'spec': 47.8, 'temp': 42.4, 'temp_shuf': 37.6, 'rate': 32.0}, '1b2a': {'st_a': 60.0, 'st_b': 70.0, 'spec': 55.0, 'temp': 60.0, 'temp_shuf': 45.0, 'rate': 35.0}, '1b2b': {'st_a': 55.0, 'st
eq_3b {'1a2a': {'st_a': 81.2, 'st_b': 73.2, 'spec': 56.7, 'temp': 82.0, 'temp_shuf': 69.5, 'rate': 33.3}, '1a2b': {'st_a': 79.9, 'st_b': 80.9, 'spec': 54.2, 'temp': 82.0, 'temp_shuf': 69.5, 'rate': 25.4}, '1b2a': {'st_a': 90.0, 'st_b': 80.0, 'spec': 60.0, 'temp': 90.0, 'temp_shuf': 80.0, 'rate': 30.0}, '1b2b': {'st_a': 80.0, 'st
orig {'1a2a': {'st_a': 80.8, 'st_b': 85.8, 'spec': 82.8, 'temp': 78.7, 'temp_shuf': 65.8, 'rate': 90.8}, '1a2b': {'st_a': 76.5, 'st_b': 80.2, 'spec': 84.4, 'temp': 64.6, 'temp_shuf': 51.5, 'rate': 90.3}, '1b2a': {'st_a': 85.0, 'st_b': 90.0, 'spec': 90.0, 'temp': 80.0, 'temp_shuf': 65.0, 'rate': 95.0}, '1b2b': {'st_a': 80.0, 'st_

-----
whole     diagonal in : spectral r 0.650 +/- 0.238, temporal r 0.877 +/- 0.048 | per sound spectral [ 0.99  0.62  0.95  0.96 -0.26], temporal [0.99 0.79 0.94 0.93 0.74] | within tol False, False; within 10% False, False
whole     diagonal out: spectral r 0.661 +/- 0.235, temporal r 0.877 +/- 0.048 | per sound spectral [ 0.99  0.66  0.95  0.96 -0.25], temporal [0.99 0.79 0.94 0.93 0.74] | within tol False, False; within 10% False, False
w1000     diagonal in : spectral r 0.652 +/- 0.237, temporal r 0.881 +/- 0.046 | per sound spe
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019 && python3 - <<'EOF'
s=open('src_neural.py').read()
s=s.replace("""def within(v, e, tol):
    return abs(v - e) <= tol + 1e-9""","""def within(v, e, tol):
    return bool(abs(v - e) <= tol + 1e-9)""")
open('src_neural.py','w').write(s)
EOF
grep -n "def within" -A1 src_neural.py; sed -n 300,330p ../../paper/10.1371-journal.pbio.3000449.txt >/dev/null; grep -n "half width\|CDI =\|SI =\|141\|Fig 9C\|25%" ../../paper/10.1371-journal.pbio.3000449.txt | cut -c1-600 | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "entries/sadeghi-2019/model.py",
 "content": "\"\"\"Cochlear model and short-term correlations for Sadeghi et al. (2019), from the Methods\n(\"Auditory model\", \"Nonstationary spectro-temporal correlation statistics\", \"Stationarity and\nensemble diversity indices\") and the paper's MATLAB code in the data set\n(Code/AuditoryModelCorr: cochleogram.m, cochleogramdyncorr.m, xcorrst.m, xcorrstsym.m,\nfdesignkdt.m, finddtdfw.m, gammatonefilter.m, lowpass.m, fdesignh.m, h.m).\n\nWhere each parameter comes from:\n- 58 gammatone filters of order 3, phase 0, centre frequencies from 100 Hz to 16 kHz in 1/8\n  octave steps (Methods; centres placed as cochleogram.m does, Xc = (0.5 .. L-0.5)/L log2(fN/f1)).\n- Bandwidths b = 25 + 75 (1 + 1.4 f^2)^0.69, f in kHz (Methods). The code's ModelExample.m uses\n  criticalbandwidth.m, 94 + 71 f^1.5, which differs; the Methods are followed (protocol, reader\n  step 2) and the difference is recorded as a finding.\n- Passband gain 1 (Methods; gammatonefilter.m divides by the peak of |FFT|).\n- Envelope: magnitude of the analytic signal, low-pass at 500 Hz with 125 Hz transition and 60 dB\n  attenuation (Methods), designed as lowpass.m/fdesignh.m/h.m do, negative values set to 0\n  (cochleogram.m), then resampled to 1 kHz (Methods; the code's ModelExample.m keeps 3675 Hz).\n- The sound is normalised to unit SD first (cochleogramdyncorr.m).\n- Short-term correlation: Kaiser window, beta from 40 dB attenuation (fdesignkdt.m gives 3.395,\n  the Methods say 3.4), length chosen so that two SDs of the window (finddtdfw.m) equal tau_W;\n  normalised as a correlation coefficient with time- and delay-dependent means and variances\n  (xcorrst.m, RxyN), symmetrised over the two channel orders (xcorrstsym.m).\n- Delays: up to half the window resolution tau_W (Methods); for SI and CDI, M = 99 lags (Methods),\n  that is -49 to 49 ms at tau_W = 100 ms.\n- Time step of the short-term correlation: tau_W / 4. The code steps at 8 x 4 x the window's 3 dB\n  bandwidth (xcorrst.m with OFc = 8), finer than this; a time average of a slowly varying\n  quantity does not depend on the step once it is below the window length, so this is a\n  standard choice made for speed.\n\"\"\"\nimport io\n\nimport numpy as np\nfrom scipy import signal\nfrom scipy.io import wavfile\n\nFS_SOUND = 44100\nFS_ENV = 1000\n\n\ndef read_wav(raw):\n    fs, x = wavfile.read(io.BytesIO(raw))\n    x = x.astype(np.float64)\n    if x.ndim > 1:\n        x = x[:, 0]\n    return fs, x\n\n\ndef centre_frequencies(f1=100.0, fN=16000.0, dx=1 / 8):\n    XN = np.log2(fN / f1)\n    L = int(np.floor(XN / dx))\n    return f1 * 2 ** ((np.arange(L) + 0.5) / L * XN)\n\n\ndef bandwidth_methods(fc):\n    f = fc / 1000\n    return 25 + 75 * (1 + 1.4 * f ** 2) ** 0.69\n\n\ndef gammatone(fc, b, fs=FS_SOUND, n=3):\n    t = np.arange(0, int(0.05 * fs) + 1) / fs\n    h = t ** (n - 1) * np.exp(-2 * np.pi * b * t) * np.cos(2 * np.pi * fc * t)\n    return h / np.abs(np.fft.fft(h, 1024 * 64)).max()\n\n\ndef lowpass_fir(fc=500.0, tw=125.0, fs=FS_SOUND, att=60.0):\n    \"\"\"lowpass.m / fdesignh.m / h.m.\"\"\"\n    wc = 2 * np.pi * fc / fs\n    TW = 2 * np.pi * tw / fs\n    P = 13 / (1 + (126 / att) ** 1.6) - .7\n    N = int(round(max((24.3 / (1 + (149 / att) ** 1.6) - 0.085) / TW * np.pi - 1, P * np.pi / wc / 0.95)))\n    alpha = P * np.pi / (N + 1) / wc\n    n = np.arange(-N, N + 1)\n    H = wc / np.pi * np.sinc(wc * n / np.pi)\n    W = np.sinc(alpha * wc * n / P / np.pi) ** P\n    return H * W\n\n\ndef cochleogram(x, fs=FS_SOUND):\n    \"\"\"(58 channels, samples at 1 kHz) envelopes.\"\"\"\n    x = x / x.std()\n    fc = centre_frequencies()\n    bw = bandwidth_methods(fc)\n    he = lowpass_fir(fs=fs)\n    ne = (len(he) - 1) // 2\n    out = []\n    for f, b in zip(fc, bw):\n        y = signal.fftconvolve(x, gammatone(f, b, fs))[: len(x)]\n        y = np.abs(signal.hilbert(y))\n        y = np.maximum(0, signal.fftconvolve(y, he)[ne: ne + len(x)])\n        out.append(y)\n    S = np.array(out)\n    S = signal.resample_poly(S, FS_ENV, fs, axis=1)\n    return np.maximum(S, 0)\n\n\ndef kaiser_for(tau_w_s, fs=FS_ENV, att=40.0):\n    \"\"\"fdesignkdt.m: Kaiser window whose 2 SD width (finddtdfw.m) is closest to tau_w.\"\"\"\n    beta = .5842 * (att - 21) ** .4 + .07886 * (att - 21)\n    TW = 2 / tau_w_s / fs\n    N = int(np.ceil((att - 7.95) / 14.36 / TW * np.pi))\n    best = None\n    for n in range(N - int(np.ceil(0.25 * N)), N + 1):\n        w = np.kaiser(n, beta)\n        wn = w / np.sqrt((w ** 2).sum() / fs)\n        t = np.arange(1, n + 1) / fs\n        m = (t * wn ** 2).sum() / fs\n        dT = 2 * np.sqrt(((t - m) ** 2 * wn ** 2).sum() / fs)\n        if best is None or abs(dT - tau_w_s) < best[0]:\n            best = (abs(dT - tau_w_s), n)\n    n = best[1] // 2 * 2 + 1\n    return np.kaiser(n, beta), beta\n\n\ndef short_term(S, tau_w_ms, maxlag, step=None, pairs=\"all\"):\n    \"\"\"Short-term correlation c_kl(t, tau) of xcorrst.m (RxyN), symmetrised as xcorrstsym.m.\n    pairs = \"all\" gives (T, C, C, 2 maxlag + 1); \"auto\" gives the autocorrelations (T, C, lags);\n    \"zero\" gives the zero-lag matrices (T, C, C). Yields one time point at a time when\n    iterate=True is used through short_term_iter.\"\"\"\n    return np.array(list(short_term_iter(S, tau_w_ms, maxlag, step, pairs)))\n\n\ndef short_term_iter(S, tau_w_ms, maxlag, step=None, pairs=\"all\"):\n    K, _ = kaiser_for(tau_w_ms / 1000)\n    W = np.sqrt(K)\n    N = (len(W) - 1) // 2\n    maxlag = min(maxlag, N)\n    nw = 2 * N + 1\n    step = step or max(1, int(round(tau_w_ms / 4)))\n    C, T = S.shape\n    lags = np.arange(-maxlag, maxlag + 1)\n    for k in range(2 * N, T - 2 * N, step):\n        X = S[:, k - N: k + N + 1]\n        XW = X * W\n        MX = XW.mean(1)\n        VX = XW.var(1, ddof=1)\n        # Y shifted by each lag: Ysh[lag, c, j] = S[c, k - N + j - lag]\n        idx = (k - N + np.arange(nw))[None, :] - lags[:, None]\n        Ysh = S[:, idx].transpose(1, 0, 2)  # lags, C, nw\n        MY = (Ysh * W).sum(-1) / nw  # lags, C\n        E2Y = (Ysh ** 2 * K).sum(-1) / nw\n        VY = E2Y - MY ** 2\n        XK = X * K\n        if pairs == \"auto\":\n            R = np.einsum(\"cj,lcj->cl\", XK, Ysh) / nw  # C, lags\n            c = (R - MX[:, None] * MY.T) / np.sqrt(VX[:, None] * VY.T)\n            yield (c + c[:, ::-1]) / 2\n        elif pairs == \"zero\":\n            i0 = maxlag\n            R = XK @ Ysh[i0].T / nw\n            c = (R - np.outer(MX, MY[i0])) / np.sqrt(np.outer(VX, VY[i0]))\n            yield (c + c.T) / 2\n        else:\n            R = (XK @ Ysh.reshape(-1, nw).T).reshape(C, len(lags), C) / nw  # k, lag, l\n            c = (R - MX[:, None, None] * MY[None]) / np.sqrt(VX[:, None, None] * VY[None])\n            c = c.transpose(0, 2, 1)  # k, l, lag\n            yield (c + c.transpose(1, 0, 2)[:, :, ::-1]) / 2\n\n\ndef long_term_auto(S, maxlag):\n    \"\"\"Long-term normalised autocorrelation of each whole envelope (mean removed), lags\n    -maxlag..maxlag.\"\"\"\n    X = S - S.mean(1, keepdims=True)\n    n = X.shape[1]\n    nfft = 1 << int(np.ceil(np.log2(2 * n)))\n    F = np.fft.rfft(X, nfft)\n    r = np.fft.irfft(F * np.conj(F), nfft)\n    r = np.concatenate([r[:, nfft - maxlag:], r[:, : maxlag + 1]], 1)\n    return r / r[:, maxlag: maxlag + 1]\n\n\ndef width_at(curve, lags_ms, frac=0.5):\n    i0 = int(np.argmax(curve))\n    thr = frac * curve[i0]\n    def cross(step):\n        i = i0\n        while 0 <= i + step < len(curve) and curve[i + step] >= thr:\n            i += step\n        if not (0 <= i + step < len(curve)):\n            return lags_ms[i]\n        a, b = curve[i], curve[i + step]\n        return lags_ms[i] + (lags_ms[i + step] - lags_ms[i]) * (a - thr) / (a - b)\n    return cross(1) - cross(-1)\n"
}
```

```
File created successfully at: entries/sadeghi-2019/model.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > devm.py <<'EOF'
import sys, time, numpy as np
sys.path.insert(0,'entries/sadeghi-2019')
import sadeghi as S, model as M
t=time.time(); snd={}
for name, raw in S.stream_members(lambda n: "/ModelSounds/" in n and n.endswith(".wav")):
    snd[name]=raw
    if len(snd)==195: break
print('read', len(snd), time.time()-t)
cats=sorted({n.split('/')[-2] for n in snd}); print(cats)
k=[n for n in snd if 'Human_Speech/Sound_1.wav' in n][0]
fs,x=M.read_wav(snd[k]); print(fs, x.shape, x.dtype, x.std())
t=time.time(); C=M.cochleogram(x); print('coch', time.time()-t, C.shape, C.min(), C.max())
K,b=M.kaiser_for(0.1); print('kaiser len', len(K), b)
t=time.time(); c=M.short_term(C, 100, 49, pairs="all"); print('st all', time.time()-t, c.shape)
t=time.time(); a=M.short_term(C, 566, 283, pairs="auto"); print('st auto 566', time.time()-t, a.shape)
lag=np.arange(-283,284); print('speech width', M.width_at(a.mean(0).mean(0), lag), np.median([M.width_at(a.mean(0)[ch], lag) for ch in range(58)]))
la=M.long_term_auto(C,283); print('longterm', M.width_at(la.mean(0), lag))
print('diag zero lag', c[0][np.arange(58),np.arange(58),49][:5])
EOF
python devm.py
```

```
read 195 4.7059326171875
['Automobile_Engines', 'Bell', 'Bird_Chorus', 'Cat_Meowing', 'Dog_Barking', 'Fire', 'Flowing_Water', 'Human_Speech', 'Single_Bird_Songs', 'Speech_Babble', 'Thunder_Rain', 'Wave', 'Wind']
44100 (441000,) float64 32.74165692251978
coch 1.6333670616149902 (58, 10000) 0.0 5.38147267974241
kaiser len 269 3.3953210522614574
st all 3.750912666320801 (379, 58, 58, 99)
st auto 566 12.921186923980713 (50, 58, 567)
speech width 64.46106323511714 70.03767460120568
longterm 81.10762106676725
diag zero lag [0.99813953 0.99813953 0.99813953 0.99813953 0.99813953]
Shell cwd was reset to
```

**Agent**

The speech example's half width comes out at 64.5 ms (paper: 64 ms). The short-term correlation is slower than it needs to be, so I'll precompute the sliding window sums.

**Agent calls Bash**

```bash
cd entries/sadeghi-2019 && python3 - <<'EOF'
s=open('model.py').read()
i=s.index('def short_term_iter'); j=s.index('def long_term_auto')
s=s[:i]+'''def short_term_iter(S, tau_w_ms, maxlag, step=None, pairs="all"):
    K, _ = kaiser_for(tau_w_ms / 1000)
    W = np.sqrt(K)
    N = (len(W) - 1) // 2
    maxlag = min(maxlag, N)
    nw = 2 * N + 1
    step = step or max(1, int(round(tau_w_ms / 4)))
    C, T = S.shape
    lags = np.arange(-maxlag, maxlag + 1)
    # sliding sums over every window start s: sum_j W[j] S[c, s + j] and sum_j K[j] S[c, s + j]^2
    SW = signal.fftconvolve(S, W[None, ::-1], mode="valid", axes=1) / nw
    SK2 = signal.fftconvolve(S ** 2, K[None, ::-1], mode="valid", axes=1) / nw
    L = nw + 2 * maxlag
    nfft = 1 << int(np.ceil(np.log2(L + nw)))
    for k in range(2 * N, T - 2 * N, step):
        X = S[:, k - N: k + N + 1]
        XW = X * W
        MX = XW.mean(1)
        VX = XW.var(1, ddof=1)
        st = k - N - lags  # window start of Y shifted by each lag
        MY = SW[:, st].T  # lags, C
        VY = SK2[:, st].T - MY ** 2
        XK = X * K
        if pairs == "all":
            idx = (k - N + np.arange(nw))[None, :] - lags[:, None]
            Ysh = S[:, idx].transpose(1, 0, 2)  # lags, C, nw
            R = (XK @ Ysh.reshape(-1, nw).T).reshape(C, len(lags), C) / nw  # k, lag, l
            c = (R - MX[:, None, None] * MY[None]) / np.sqrt(VX[:, None, None] * VY[None])
            c = c.transpose(0, 2, 1)  # k, l, lag
            yield (c + c.transpose(1, 0, 2)[:, :, ::-1]) / 2
        elif pairs == "zero":
            i0 = maxlag
            R = XK @ S[:, k - N: k + N + 1].T / nw
            c = (R - np.outer(MX, MY[i0])) / np.sqrt(np.outer(VX, VY[i0]))
            yield (c + c.T) / 2
        else:
            seg = S[:, k - N - maxlag: k + N + maxlag + 1]
            r = np.fft.irfft(np.fft.rfft(seg, nfft) * np.conj(np.fft.rfft(XK, nfft)), nfft)
            # r[c, d] = sum_j XK[c, j] seg[c, j + d]; lag tau = maxlag - d
            R = r[:, :2 * maxlag + 1][:, ::-1] / nw  # C, lags (-maxlag..maxlag)
            c = (R - MX[:, None] * MY.T) / np.sqrt(VX[:, None] * VY.T)
            yield (c + c[:, ::-1]) / 2


'''+s[j:]
open('model.py','w').write(s)
EOF
cd $TMPDIR && . dev/bin/activate && cat > devm2.py <<'EOF'
import sys, time, numpy as np
sys.path.insert(0,'entries/sadeghi-2019')
import sadeghi as S, model as M
for name, raw in S.stream_members(lambda n: n.endswith("Human_Speech/Sound_1.wav")):
    fs,x=M.read_wav(raw); break
C=M.cochleogram(x)
t=time.time(); c=M.short_term(C, 100, 49, pairs="all"); print('st all', time.time()-t, c.shape)
t=time.time(); a=M.short_term(C, 566, 283, pairs="auto"); print('st auto 566', time.time()-t, a.shape)
lag=np.arange(-283,284); print('speech width', M.width_at(a.mean(0).mean(0), lag))
a1=M.short_term(C, 100, 49, pairs="auto"); print('auto vs all diag', np.abs(a1 - c[:, np.arange(58), np.arange(58), :]).max())
z=M.short_term(C, 100, 49, pairs="zero"); print('zero vs all', np.abs(z - c[:, :, :, 49]).max())
EOF
python devm2.py
```

```
st all 2.19565749168396 (379, 58, 58, 99)
st auto 566 0.1745595932006836 (50, 58, 567)
speech width 64.46106323511711
auto vs all diag 8.545941732052142e-14
zero vs all 6.161737786669619e-15
Shell cwd was reset to
```

**Agent**

Both paths agree with the full computation, and the cost is now about 2 s per sound. Writing the model notebook:

**Agent calls Write**

```json
{
 "file_path": "entries/sadeghi-2019/src_model.py",
 "content": "# %% [markdown]\n# # Sadeghi et al. (2019): auditory model claims (CRCNS bst-2)\n#\n# HEADER\n\n# %%\nimport time, resource\nimport numpy as np\nfrom scipy import stats\nimport matplotlib.pyplot as plt\nimport sadeghi as S\nimport model as M\n\nT_START = time.time()\nSEED_NOISE = 505  # standard choice, white noise control\n\n# %% [markdown]\n# ## Loading\n#\n# The 195 model sounds are the first members of the tar stream after the paradigm sounds; the\n# stream is closed once they are read. White noise, which the data set does not hold, is\n# generated (15 Gaussian noises of 10 s, as in the claims file).\n\n# %%\nraw = {}\nfor name, b in S.stream_members(lambda n: \"/Sounds/ModelSounds/\" in n and n.endswith(\".wav\")):\n    raw[name] = b\n    if len(raw) == 195:\n        break\nCATS = sorted({n.split(\"/\")[-2] for n in raw})\nsounds = {}\nfor n, b in raw.items():\n    fs, x = M.read_wav(b)\n    sounds[(n.split(\"/\")[-2], int(n.split(\"_\")[-1][:-4]))] = (fs, x, b[:44])\nrng = np.random.default_rng(SEED_NOISE)\nfor i in range(1, 16):\n    sounds[(\"White_Noise\", i)] = (44100, rng.standard_normal(441000) * 0.001, b\"\")\nprint(\"read\", len(raw), \"files in\", round(time.time() - T_START), \"s\")\n\n# %% tags=[\"sanity\"]\nprint(\"categories:\", len(CATS), CATS)\nfor c in CATS:\n    keys = sorted(k for k in sounds if k[0] == c)\n    fss = {sounds[k][0] for k in keys}\n    lens = {len(sounds[k][1]) / sounds[k][0] for k in keys}\n    sds = [sounds[k][1].std() for k in keys]\n    print(f\"{c:20s} sounds {len(keys):2d} (numbers {keys[0][1]}-{keys[-1][1]}) fs {fss} duration (s) {sorted(lens)}\"\n          f\" SD (int16 units) {min(sds):.1f}-{max(sds):.1f}\")\nhdr = sounds[(CATS[0], 1)][2]\nprint(\"WAV header of one file: format tag\", int.from_bytes(hdr[20:22], \"little\"), \"bits\", int.from_bytes(hdr[34:36], \"little\"),\n      \"(1 = integer PCM; the data description says double precision, normalised to SD 0.001)\")\nprint(\"SD as a fraction of full scale, all model sounds:\",\n      round(min(sounds[k][1].std() for k in sounds if k[0] != \"White_Noise\") / 32768, 5), \"to\",\n      round(max(sounds[k][1].std() for k in sounds if k[0] != \"White_Noise\") / 32768, 5))\n\n# %% [markdown]\n# The files are 16 bit integer PCM, not double precision as the data description says; their SD\n# as a fraction of full scale is about 0.001, as it says. Every sound is 10 s at 44.1 kHz and\n# every category has 15, as the Methods state.\n\n# %% [markdown]\n# ## Model correlations of every sound\n#\n# Per sound: the cochlear envelopes (58 channels, 1 kHz); the short-term spectro-temporal\n# correlation at tau_W = 100 ms with 99 lags (for SI, CDI and the spectral breadth); the\n# time-averaged short-term autocorrelations at tau_W = 566 ms (lags within 283 ms); and the\n# long-term autocorrelation of the whole envelopes (lags within 283 ms).\n\n# %%\nLAG566 = np.arange(-283, 284).astype(float)\ncbar, si_terms, auto566, autolong, zero_long = {}, {}, {}, {}, {}\nt0 = time.time()\nfor i, key in enumerate(sorted(sounds)):\n    fs, x, _ = sounds[key]\n    Sg = M.cochleogram(x, fs)\n    n, s1, s2 = 0, 0.0, 0.0\n    acc = None\n    for c in M.short_term_iter(Sg, 100, 49, pairs=\"all\"):\n        v = c.astype(np.float64)\n        acc = v.copy() if acc is None else acc + v\n        s2 += (v ** 2).sum()\n        n += 1\n    cbar[key] = (acc / n).astype(np.float32)\n    si_terms[key] = (s2 / n, float((cbar[key].astype(np.float64) ** 2).sum()), n)\n    auto566[key] = np.mean(list(M.short_term_iter(Sg, 566, 283, pairs=\"auto\")), 0)\n    autolong[key] = M.long_term_auto(Sg, 283)\n    X = Sg - Sg.mean(1, keepdims=True)\n    zero_long[key] = np.corrcoef(X)\n    if i % 30 == 0:\n        print(i, key, f\"{time.time() - t0:.0f} s\", flush=True)\nprint(\"time points per sound at 100 ms:\", sorted({v[2] for v in si_terms.values()}))\nprint(f\"done in {(time.time() - t0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\n# %% [markdown]\n# ## fig5-speech-water-widths\n#\n# > In the cochlear model, the example speech sound has broad spectral correlations and a slow\n# > temporal correlation (64 ms half width), while the example water sound has diagonal\n# > spectral correlations and a fast temporal correlation (4 ms half width).\n#\n# Readings: window (ii)(a) time average of the short-term correlation at tau_W = 566 ms,\n# (ii)(b) long-term correlation of the whole envelopes; width (iii)(a) full width at 50% of the\n# channel-averaged autocorrelation, (iii)(b) median over channels. Spectral breadth is the mean\n# off-diagonal zero-lag correlation (time-averaged at 100 ms, and long-term).\n\n# %% tags=[\"claim:fig5-speech-water-widths\"]\ndef widths(curves):\n    return M.width_at(curves.mean(0), LAG566, 0.5), float(np.median([M.width_at(c, LAG566, 0.5) for c in curves]))\n\ndef breadth(key):\n    off = ~np.eye(58, dtype=bool)\n    return float(cbar[key][:, :, 49][off].mean()), float(zero_long[key][off].mean())\n\nSP, WA = (\"Human_Speech\", 1), (\"Flowing_Water\", 1)\nfor lab, src in ((\"(ii)(a) 566 ms short-term\", auto566), (\"(ii)(b) long-term\", autolong)):\n    ws, wa = widths(src[SP]), widths(src[WA])\n    for j, wl in enumerate((\"(iii)(a) mean curve\", \"(iii)(b) median of channels\")):\n        print(f\"{lab}, {wl}: speech {ws[j]:.1f} ms (64 +/- 6.4: {abs(ws[j] - 64) <= 6.4}), water {wa[j]:.1f} ms (4 +/- 1: {abs(wa[j] - 4) <= 1})\")\nprint(\"spectral breadth (100 ms time average, long-term): speech\", np.round(breadth(SP), 3), \"water\", np.round(breadth(WA), 3))\nprint(\"variant, every sound of the category, (ii)(a)(iii)(a):\")\nfor cat in (\"Human_Speech\", \"Flowing_Water\"):\n    v = [widths(auto566[(cat, i)])[0] for i in range(1, 16)]\n    print(f\"   {cat}: {np.round(v, 1)}\")\nfig, ax = plt.subplots(1, 2, figsize=(9, 2.6))\nfor a, key in zip(ax, (SP, WA)):\n    a.plot(LAG566, auto566[key].mean(0), label=\"566 ms short-term\"); a.plot(LAG566, autolong[key].mean(0), label=\"long-term\")\n    a.set_title(key[0] + \" 1\"); a.set_xlabel(\"lag (ms)\")\nax[0].legend(fontsize=7); plt.tight_layout(); plt.show()\nprint(\"plotted range:\", round(float(min(auto566[SP].mean(0).min(), autolong[WA].mean(0).min())), 3), \"to 1\")\n\n# %% [markdown]\n# **Result: RES_FIG5**\n\n# %% [markdown]\n# ## fig6-category-half-widths\n#\n# > Water and wind sounds have fast temporal correlations (half widths 3.9 and 3.6 ms) and\n# > diagonal spectral correlations, while vocalizations have slow ones (speech 64.9 ms, dogs\n# > 76.3 ms, cats 117.3 ms) and more extensive spectral correlations.\n\n# %% tags=[\"claim:fig6-category-half-widths\"]\nEXP6 = {\"Flowing_Water\": (3.9, 1), \"Wind\": (3.6, 1), \"Human_Speech\": (64.9, 6.49), \"Dog_Barking\": (76.3, 7.63), \"Cat_Meowing\": (117.3, 11.73)}\nVOC = [\"Single_Bird_Songs\", \"Cat_Meowing\", \"Dog_Barking\", \"Human_Speech\"]\nfor lab, src in ((\"(ii)(a) 566 ms short-term\", auto566), (\"(ii)(b) long-term\", autolong)):\n    avg = {c: np.mean([src[(c, i)] for i in range(1, 16)], 0) for c in CATS + [\"White_Noise\"]}\n    for j, wl in enumerate((\"(iii)(a) mean curve\", \"(iii)(b) median of channels\")):\n        w = {c: widths(avg[c])[j] for c in avg}\n        hits = sum(abs(w[c] - e) <= t for c, (e, t) in EXP6.items())\n        pooled = widths(np.mean([avg[c] for c in (\"Flowing_Water\", \"Wave\", \"Thunder_Rain\")], 0))[j]\n        sep = min(w[c] for c in VOC) > max(w[\"Flowing_Water\"], w[\"Wind\"])\n        print(f\"{lab}, {wl}: \" + \", \".join(f\"{c} {w[c]:.1f}\" for c in EXP6) + f\" | in tol {hits}/5 | every vocalization wider than water and wind: {sep}\"\n              f\" | pooled water, waves, rain {pooled:.1f} | all: \" + \", \".join(f\"{c} {w[c]:.1f}\" for c in avg if c not in EXP6))\ncat_breadth = {c: np.mean([breadth((c, i))[0] for i in range(1, 16)]) for c in CATS + [\"White_Noise\"]}\nprint(\"mean off-diagonal zero-lag correlation by category (100 ms):\", {c: round(float(v), 3) for c, v in sorted(cat_breadth.items(), key=lambda kv: kv[1])})\n\n# %% [markdown]\n# **Result: RES_FIG6**\n\n# %% [markdown]\n# ## fig6c-category-diversity\n#\n# > White noise has the lowest category diversity index; among natural sounds speech is lowest\n# > (CDI 0.12), crowd noise 0.15, wind 0.18, dogs 0.21, bird songs 0.29 and fire highest\n# > (0.39), with no clear trend between classes.\n#\n# Time-averaged spectro-temporal correlation per sound at tau_W = 100 ms, 99 lags, 58 x 58\n# channels; readings (a) E||c_n - E c||^2 / ||E c||^2, (b) E||c_n - E c||^2 / E||c_n||^2, (c)\n# the same with norms not squared.\n\n# %% tags=[\"claim:fig6c-category-diversity\"]\nEXPC = {\"Human_Speech\": 0.12, \"Speech_Babble\": 0.15, \"Wind\": 0.18, \"Dog_Barking\": 0.21, \"Single_Bird_Songs\": 0.29, \"Fire\": 0.39}\ncdi = {r: {} for r in (\"a\", \"b\", \"a_c\", \"b_c\")}\nfor c in CATS + [\"White_Noise\"]:\n    V = np.array([cbar[(c, i)].ravel().astype(np.float64) for i in range(1, 16)])\n    m = V.mean(0)\n    d2 = ((V - m) ** 2).sum(1)\n    n2 = (V ** 2).sum(1)\n    cdi[\"a\"][c] = d2.mean() / (m ** 2).sum()\n    cdi[\"b\"][c] = d2.mean() / n2.mean()\n    cdi[\"a_c\"][c] = np.sqrt(d2).mean() / np.sqrt((m ** 2).sum())\n    cdi[\"b_c\"][c] = np.sqrt(d2).mean() / np.sqrt(n2).mean()\nfor r, v in cdi.items():\n    hits = sum(abs(v[c] - e) <= 0.1 * e + 1e-9 for c, e in EXPC.items())\n    nat = {c: x for c, x in v.items() if c != \"White_Noise\"}\n    order = [c for c in sorted(EXPC, key=lambda c: v[c])]\n    print(f\"({r}): \" + \", \".join(f\"{c} {v[c]:.3f}\" for c in EXPC) + f\" | in tol {hits}/6 | lowest natural {min(nat, key=nat.get)},\"\n          f\" white noise {v['White_Noise']:.3f} (rank {sorted(v.values()).index(v['White_Noise']) + 1} of 14) | rank order of the six kept:\"\n          f\" {order == list(EXPC)}\")\n    print(\"      all:\", {c: round(float(x), 3) for c, x in sorted(v.items(), key=lambda kv: kv[1])})\n\n# %% [markdown]\n# **Result: RES_FIG6C**\n\n# %% [markdown]\n# ## fig7i-stationarity\n#\n# > Environmental sounds other than fire (running water, waves, thunder, wind) are the most\n# > stationary natural sounds (SI = 0.49 +/- 0.04), vocalizations less so (0.28 +/- 0.04),\n# > speech is the least stationary category and white noise the most.\n#\n# SI per sound from the short-term correlation at tau_W = 100 ms, 99 lags: (a) 1 -\n# <||c(t) - <c>||^2> / ||<c>||^2, (b) 1 - <||c(t) - <c>||^2> / <||c(t)||^2>.\n\n# %% tags=[\"claim:fig7i-stationarity\"]\nSI = {\"a\": {}, \"b\": {}}\nfor k, (e2, m2, n) in si_terms.items():\n    var = e2 - m2\n    SI[\"a\"][k] = 1 - var / m2\n    SI[\"b\"][k] = 1 - var / e2\nENV_C = [\"Flowing_Water\", \"Wave\", \"Thunder_Rain\", \"Wind\"]\nGROUPS = {\"c\": (ENV_C, VOC), \"d\": (ENV_C + [\"Bird_Chorus\", \"Speech_Babble\"], VOC)}\nfor r in (\"a\", \"b\"):\n    catm = {c: np.mean([SI[r][(c, i)] for i in range(1, 16)]) for c in CATS + [\"White_Noise\"]}\n    print(f\"({r}) category means: \" + \", \".join(f\"{c} {v:.3f}\" for c, v in sorted(catm.items(), key=lambda kv: kv[1])))\n    for g, (env, voc) in GROUPS.items():\n        for unit in (\"e\", \"f\"):\n            if unit == \"e\":\n                ev, vv = [catm[c] for c in env], [catm[c] for c in voc]\n            else:\n                ev = [SI[r][(c, i)] for c in env for i in range(1, 16)]\n                vv = [SI[r][(c, i)] for c in voc for i in range(1, 16)]\n            se = lambda x: np.std(x, ddof=1) / np.sqrt(len(x))\n            ok = abs(np.mean(ev) - 0.49) <= 0.04 and abs(np.mean(vv) - 0.28) <= 0.04\n            nat = {c: v for c, v in catm.items() if c != \"White_Noise\"}\n            print(f\"   ({r})({g})({unit}): environmental {np.mean(ev):.3f} +/- {se(ev):.3f}, vocalizations {np.mean(vv):.3f} +/- {se(vv):.3f}\"\n                  f\" | both in tol {ok} | lowest category {min(nat, key=nat.get)}, highest overall {max(catm, key=catm.get)}\")\n    print(f\"   ({r}) example sounds: speech 1 {SI[r][('Human_Speech', 1)]:.3f}, water 1 {SI[r][('Flowing_Water', 1)]:.3f}\")\n\n# %% [markdown]\n# **Result: RES_FIG7I**\n\n# %% [markdown]\n# ## Model classification claims: cost estimate\n#\n# Claims fig9a-optimal-resolution, fig9b-similar-maximum, fig9b-accumulation-rate,\n# fig9c-time-averaged-worse, fig9e-category-specific, fig9-spectrum-classifier-lower and\n# fig10-vocalization-background need the leave-one-sound-out GMM classifier at ten window\n# resolutions (25 to 566 ms) for three correlation classifiers and the spectrum classifier.\n# This cell times the parts on a subset and estimates the whole, under the cheapest readings:\n# the reported PC and component counts used at every resolution (reading (7)(b), no search over\n# N_c = 1 to 20), and training observations every tau_W / 4 or, cheaper still, at\n# non-overlapping windows.\n\n# %% tags=[\"claim:fig9a-optimal-resolution\"]\nfrom sklearn.mixture import GaussianMixture\nfrom sklearn.decomposition import PCA as skPCA\nRES = 25 * 2 ** (np.arange(10) / 2)\nfs, x, _ = sounds[(\"Human_Speech\", 1)]\nSg = M.cochleogram(x, fs)\nt_feat = []\nfor tw in RES:\n    t1 = time.time()\n    z = np.array(list(M.short_term_iter(Sg, tw, 0, pairs=\"zero\")))\n    a = np.array(list(M.short_term_iter(Sg, tw, int(tw / 2), pairs=\"auto\")))\n    t_feat.append(time.time() - t1)\ncoch_t = []\nfor key in [(\"Fire\", 1), (\"Wind\", 2)]:\n    t1 = time.time(); M.cochleogram(sounds[key][1], 44100); coch_t.append(time.time() - t1)\nfeat_total = 195 * (np.sum(t_feat) + np.mean(coch_t))\nprint(\"feature time for one sound over the ten resolutions (s):\", np.round(t_feat, 2), \"; cochleogram\", np.round(np.mean(coch_t), 2))\nprint(f\"features for 195 sounds at ten resolutions: {feat_total / 60:.1f} min\")\niu = np.triu_indices(58, 1)\nrng_t = np.random.default_rng(7)\nfit_t = {}\nfor step_lab, per_sound in ((\"tau_W/4 at 141 ms\", int(10000 / (141 / 4))), (\"non-overlapping 141 ms\", int(10000 / 141))):\n    Xc = rng_t.standard_normal((14 * per_sound, 26))\n    t1 = time.time()\n    GaussianMixture(8, covariance_type=\"diag\", random_state=0, max_iter=100).fit(Xc)\n    fit_t[step_lab] = time.time() - t1\nnfits = 195 * 13 * 3 * 10\nfor k, v in fit_t.items():\n    print(f\"one GMM fit (8 diagonal components, 26 PCs, {k} training observations of one category): {v:.2f} s;\"\n          f\" {nfits} fits (195 folds x 13 categories x 3 classifiers x 10 resolutions): {nfits * v / 60:.0f} min\")\nprint(f\"elapsed so far in this notebook: {(time.time() - T_START) / 60:.1f} min\")\n\n# %% [markdown]\n# **Result: RES_FIG9COST**\n\n# %% [markdown]\n# ## Summary\n#\n# SUMMARY\n\n# %%\nprint(f\"total run time {(time.time() - T_START) / 60:.1f} min\")\n"
}
```

```
File created successfully at: entries/sadeghi-2019/src_model.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/sadeghi-2019 && sed -i 's/^# %% tags=\["claim:fig9a-optimal-resolution"\]$/# %%/' src_model.py && cd $TMPDIR && . dev/bin/activate && python - <<'EOF'
s=open('entries/sadeghi-2019/src_model.py').read()
s=s.replace('for i, key in enumerate(sorted(sounds)):','for i, key in enumerate(sorted(k for k in sounds if k[1] <= 15)):')
open('dev_model.py','w').write(s)
EOF
cp entries/sadeghi-2019/*.py . && jupytext --to ipynb -q dev_model.py -o dev_model.ipynb && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 dev_model.ipynb --output dev_model_out.ipynb 2>&1 | tail -2 && python - <<'EOF'
import json
nb=json.load(open('dev_model_out.ipynb'))
for c in nb['cells']:
    if c['cell_type']!='code': continue
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain')
        if t: print(''.join(t)[:6000]); print('-----')
EOF
```

```
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 91679 bytes to dev_model_out.ipynb

real	14m31.018s
user	39m2.406s
sys	0m6.220s
read 195 files in 5 s

-----
categories: 13 ['Automobile_Engines', 'Bell', 'Bird_Chorus', 'Cat_Meowing', 'Dog_Barking', 'Fire', 'Flowing_Water', 'Human_Speech', 'Single_Bird_Songs', 'Speech_Babble', 'Thunder_Rain', 'Wave', 'Wind']
Automobile_Engines   sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 13.3-52.0
Bell                 sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 31.8-52.1
Bird_Chorus          sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 23.0-51.4
Cat_Meowing          sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 9.4-48.0
Dog_Barking          sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 24.4-42.0
Fire                 sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 26.1-50.0
Flowing_Water        sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 32.4-34.7
Human_Speech         sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 28.9-37.0
Single_Bird_Songs    sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 29.7-45.2
Speech_Babble        sounds 15 (numbers 1-15) fs {44100} duration (s) [10.0] SD (int16 units) 26.4-38.5
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && . dev/bin/activate && cp entries/sadeghi-2019/*.py . && jupytext --to ipynb -q src_neural.py -o full_neural.ipynb && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=5000 full_neural.ipynb --output full_neural_out.ipynb 2>&1 | tail -1; date -u
```

```
Fri Nov 13 21:07:04 UTC 2026
[NbConvertApp] Writing 338452 bytes to full_neural_out.ipynb

real	32m31.634s
user	47m36.402s
sys	0m37.214s
Fri Nov 13 21:39:36 UTC 2026
Shell cwd was reset to
```

**Agent**

Full neural run: 32.5 minutes. Reading the outputs:

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python - > full_neural_out.txt <<'EOF'
import json
nb=json.load(open('full_neural_out.ipynb'))
for c in nb['cells']:
    if c['cell_type']!='code': continue
    for o in c.get('outputs',[]):
        if o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
        t=o.get('text') or o.get('data',{}).get('text/plain')
        if t: print(''.join(t)); print('-----')
EOF
grep -n ERROR full_neural_out.txt; sed -n 1,80p full_neural_out.txt | cut -c1-420
```

```
P3_Site09 done at 102 s

-----
P3_Site11 done at 191 s

-----
P3_Site04 done at 399 s

-----
P3_Site05 done at 509 s

-----
P3_Site10 done at 588 s

-----
P3_Site06 done at 666 s

-----
P3_Site08 done at 838 s

[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "done at\|^-----$\|^$" full_neural_out.txt | grep -v "^      " | cut -c1-400 | sed -n 1,140p
```

```
peak memory (GB): 3.620584
files: 13 paradigm 1 sites, 11 paradigm 2 sites, 11 paradigm 3 sites
sampling rates in the files (Hz): [2034.5052083333333] ; helper uses 2034.5052083333333 ; the paper states 2000
P1_Site01 animal 0315011 date Aug2016 block 006 | conditions 5 trials 20-20 samples [6104] (3.000 s) | equal across channels True | aMUA range 1.62 to 1318.7 | odd/even PSTH r 0.41, shifted 250 ms -0.01
P1_Site02 animal 0315011 date Aug2016 block 011 | conditions 5 trials 21-21 samples [6104] (3.000 s) | equal across channels True | aMUA range 2.20 to 232.3 | odd/even PSTH r 0.60, shifted 250 ms 0.01
P1_Site03 animal 0315011 date Sept2016 block 002 | conditions 5 trials 20-20 samples [6104] (3.000 s) | equal across channels True | aMUA range 1.57 to 210.8 | odd/even PSTH r 0.66, shifted 250 ms -0.01
P1_Site04 animal 0315011 date Sept2016 block 004 | conditions 5 trials 27-27 samples [6104] (3.000 s) | equal across channels True | aMUA range 1.41 to 171.2 | odd/even PSTH r 0.83, shifted 250 ms -0.00
P1_Site05 animal 0116012 date Jan2017 block 005 | conditions 5 trials 18-18 samples [6104] (3.000 s) | equal across channels True | aMUA range 0.35 to 1629.1 | odd/even PSTH r 0.46, shifted 250 ms 0.01
P1_Site06 animal 0116012 date Jan2017 block 009 | conditions 5 trials 22-22 samples [6104] (3.000 s) | equal across channels True | aMUA range 0.48 to 169.7 | odd/even PSTH r 0.84, shifted 250 ms -0.01
P1_Site07 animal 0116012 date Jan2017 block 020 | conditions 5 trials 20-20 samples [6104] (3.000 s) | equal across channels True | aMUA range 0.12 to 124.5 | odd/even PSTH r 0.74, shifted 250 ms 0.02
P1_Site08 animal 0116012 date Jan2017 block 022 | conditions 5 trials 36-36 samples [6104] (3.000 s) | equal across channels True | aMUA range 1.24 to 254.1 | odd/even PSTH r 0.51, shifted 250 ms 0.00
P1_Site09 animal 0116012 date Jan2017 block 025 | conditions 5 trials 39-39 samples [6104] (3.000 s) | equal across channels True | aMUA range 1.39 to 266.4 | odd/even PSTH r 0
[... 129 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "done at\|^-----$\|^$" full_neural_out.txt | grep -v "^      " | cut -c1-430 | sed -n 141,330p
```

```
(1b) 100 samples summed, (2b) PCs on an inner split, a (a): single-trial st 100.0 spec 90.0 temp 70.0 | noiseless st 60.0 spec 90.0 temp 40.0 | order True, noiseless rule False
(1b) 100 samples summed, (2b) PCs on an inner split, a (b): single-trial st 70.0 spec 90.0 temp 70.0 | noiseless st 100.0 spec 90.0 temp 40.0 | order False, noiseless rule False
(1a) each sample a decision, (2a) PCs on validation, a (a): st_a 77.8% (p1 7.7e-10, p2 1.5e-09; 62.5 ms 35.7); spec 76.9% (p1 5.9e-10, p2 1.2e-09; 62.5 ms 36.2); temp 68.7% (p1 2.0e-08, p2 4.0e-08; 62.5 ms 30.9); temp_shuf 43.1% (p1 3.9e-07, p2 7.8e-07; 62.5 ms 24.3)
    above chance at p < 0.01 (both sidednesses): 4/4; tonotopy drop 25.6 points, paired t = 7.87, p = 4.4e-06
(1a) each sample a decision, (2a) PCs on validation, a (b): st_b 81.0% (p1 3.2e-10, p2 6.4e-10; 62.5 ms 37.2); spec 76.9% (p1 5.9e-10, p2 1.2e-09; 62.5 ms 36.2); temp 68.7% (p1 2.0e-08, p2 4.0e-08; 62.5 ms 30.9); temp_shuf 43.1% (p1 3.9e-07, p2 7.8e-07; 62.5 ms 24.3)
    above chance at p < 0.01 (both sidednesses): 4/4; tonotopy drop 25.6 points, paired t = 7.87, p = 4.4e-06
(1a) each sample a decision, (2b) PCs on an inner split, a (a): st_a 78.8% (p1 4.6e-10, p2 9.2e-10; 62.5 ms 32.0); spec 77.3% (p1 9.3e-10, p2 1.9e-09; 62.5 ms 30.0); temp 65.7% (p1 5.5e-08, p2 1.1e-07; 62.5 ms 29.8); temp_shuf 37.6% (p1 1.6e-06, p2 3.1e-06; 62.5 ms 23.4)
    above chance at p < 0.01 (both sidednesses): 4/4; tonotopy drop 28.1 points, paired t = 8.26, p = 2.7e-06
(1a) each sample a decision, (2b) PCs on an inner split, a (b): st_b 77.6% (p1 7.9e-10, p2 1.6e-09; 62.5 ms 32.3); spec 77.3% (p1 9.3e-10, p2 1.9e-09; 62.5 ms 30.0); temp 65.7% (p1 5.5e-08, p2 1.1e-07; 62.5 ms 29.8); temp_shuf 37.6% (p1 1.6e-06, p2 3.1e-06; 62.5 ms 23.4)
    above chance at p < 0.01 (both sidednesses): 4/4; tonotopy drop 28.1 points, paired t = 8.26, p = 2.7e-06
(1b) 100 samples summed, (2a) PCs on validation, a (a): st_a 85.4% (p1 1.3e-08, p2 2.5e-08; 62.5 ms 48.5); spec 93.8% (p1 1.5
[... 141 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "claim\b\|^  - \|outcome:\|blocked_by\|assumed\|measured\|verifications\|questions\|findings:\|about:\|kind:" attempts/fouke-2025-01.yaml | head -60; sed -n '/^findings:/,$p' attempts/fouke-2025-01.yaml | head -60; ls schemas; cat tools/entry.py | head -60 | grep -n "def \|usage\|argv"
```

```
13:  kind: agent
27:    for the link claim, and the DC pairs its printed Tukey test for Figure 1D finds significant,
36:- claim: stimulus-code-link
37:  outcome: reproduced
39:  output: claim:stimulus-code-link
46:    code's (first 35 s of the code-20 block, measured from 3 s), and no fish median is exactly 0,
54:  - The code's filter on a `vel` column is not applied to DC trials, as the DC files have no such
57:  - The timing of the DC stimulus labels could not be confirmed from the turning response (the
60:- claim: fig1d-dc-faster-all-codes
61:  outcome: reproduced
63:  output: claim:fig1d-dc-faster-all-codes
70:  - Tested over all stimulus codes without their names; the paper's figure uses nine whole-field
72:  - The comparison assumes one spatial scale for all rigs, which the files do not state.
73:- claim: fig1d-median-velocity
74:  outcome: reproduced
76:  output: claim:fig1d-median-velocity
77:  measured:
78:  - 9.87
79:  - 6.41
82:    measured), (c) median of fish medians 9.36 and 6.33, (d) median of trials 9.88 and 6.28.
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']; print(json.dumps(o,indent=0)[:2500]); print(list(s['properties'].keys())); print(s.get('required'))
print(json.dumps(s['properties']['findings'],indent=0)[:1200]); print(json.dumps(s['properties']['datasets'],indent=0)[:800])"; sed -n '/^verifications\|^inputs/,+3p' attempts/fouke-2025-01.yaml | head; grep -n "blocked_by" attempts/*.yaml | head -3; grep -rn "too_large" attempts/*.yaml | head -2
```

```
{
"type": "object",
"additionalProperties": false,
"required": [
"claim",
"outcome"
],
"properties": {
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
[... 194 more lines not kept]
```

**Agent calls Bash**

```bash
grep -ln "archive: crcns" attempts/*.yaml | head -2; f=$(grep -ln "archive: crcns" attempts/*.yaml | head -1); sed -n 1,25p $f; d=$(basename $f -01.yaml); ls entries/ | grep crcns | head -3; cat entries/fujisawa-2008-crcns-pfc-2/entry.yaml
```

```
attempts/brinke-2017-01.yaml
attempts/bruno-2017-01.yaml
schema_version: 3
id: brinke-2017-01
datasets:
- archive: crcns
  id: cb-1
  version: unversioned
  doi: 10.6080/K0B85697
  relation: primary
paper: doi:10.7554/elife.28132
date: '2026-11-13'
entry: brinke-2017
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
[... 30 more lines not kept]
```

**Agent**

Writing the entry metadata and the notebook conclusions now.

**Agent calls Bash**

```bash
cd entries/sadeghi-2019 && cat > entry.yaml <<'EOF'
schema_version: 1
name: sadeghi-2019
type: reproduction
title: A neural ensemble correlation code for sound category identification (Sadeghi et al. 2019)
description: Tests the findings of Sadeghi, Zhai, Stevenson and Escabi (2019) on CRCNS bst-2, which
  holds the analog multiunit activity of 35 inferior colliculus recordings in unanesthetized rabbits
  (13 sites listening to five natural sounds, 11 to their 1/f spectrum-equalized variants, 11 to six
  exemplars of three categories) and the 195 sounds of the paper's auditory model. It recomputes the
  stimulus-driven and noise correlations with a port of the paper's code, the single-trial
  correlation classifiers, and the model's correlation widths, stationarity and diversity.
license: Apache-2.0
notebooks:
- path: reproduce_sadeghi_2019_neural.ipynb
  title: Neural ensemble correlations and classifiers, paradigms 1 to 3
  runtime_minutes: 35
- path: reproduce_sadeghi_2019_model.ipynb
  title: Auditory model correlations of the 195 model sounds
  runtime_minutes: 16
helpers:
- sadeghi.py
- model.py
related:
- id: crcns:bst-2/unversioned
  relation: uses_data
- id: doi:10.1371/journal.pbio.3000449
  relation: reproduces
EOF
printf "aiohttp\nfsspec\nh5py\nmatplotlib\nnumpy\nrequests\nscikit-learn\nscipy\n" > requirements.in; cat ../fujisawa-2008-crcns-pfc-2/requirements.in; date -u
```

```
aiohttp
fsspec
matplotlib
networkx
numba
numpy
requests
scipy
Fri Nov 13 21:40:56 UTC 2026
```

**Agent calls Bash**

```bash
cat > $TMPDIR/fill_neural.py <<'PYEOF'
s=open('src_neural.py').read()
HEADER='''# Paper: Sadeghi M, Zhai X, Stevenson IH, Escabi MA (2019). A neural ensemble correlation code for
# sound category identification. PLoS Biol 17(10):e3000449, doi:10.1371/journal.pbio.3000449. The
# claims file (claims/sadeghi-2019.yaml) was written from the version of record (PMC6788721) with
# its supplement.
#
# Dataset: CRCNS bst-2 (doi:10.6080/K03X84V3), read from the public bucket crcnsarchive at
# bst-2/live/data.tar.gz. CRCNS data sets are not versioned, so the version is recorded as
# `unversioned`; the paper cites the data set's DOI and no version, and this is the only copy the
# bucket holds (last modified 2026-02-11). The MD5 sums from bst-2/live/checksums.md5 for the files
# read: data.tar.gz 916ae724cd3334a16a4396b861e4abe0; docs/crcns_bst-2_data_description.pdf
# 81457299a36f12a18f2eb8afa5ef1862; docs/FigureData.pdf d0a76ae42a544a60c02912762be2127b. The
# data description (version 0.6, 26 August 2019) and its figure list were read first.
#
# This notebook tests the neural claims; the auditory model claims are in
# reproduce_sadeghi_2019_model.ipynb.
#
# | Claim | Tested here |
# |---|---|
# | fig1k-example-temporal-widths | tested |
# | fig1-snr-noise-stronger | tested |
# | fig1-s5-model-predicts-neural | blocked: data missing (no tone-pip responses, so no best frequencies) |
# | fig2-noise-restricted | tested |
# | fig3a-example-tonotopy-removal | tested |
# | fig3a-example-classifier-order | tested |
# | fig3b-population-above-chance | tested |
# | figs6-per-sound-above-chance | tested |
# | figs9-mixing-coefficient | tested |
# | figs10-amua-tmua | blocked: data missing (no raw voltage traces, so no thresholded MUA) |
# | fig4-example-original-vs-equalized | tested |
# | fig4e-population-original-vs-equalized | tested |
# | fig4f-example-equalized-classification | tested |
# | fig4h-population-equalized-classification | tested |
# | fig8b-example-pca-variance | tested |
# | fig8e-example-categorization | tested |
# | fig8f-population-categorization | tested |
#
# Method: the correlations port the paper's MATLAB code in the data set
# (Code/MUACorrAnalysis/rastermuashuffledxcorrwinfast.m); the classifier follows the Methods
# ("Noiseless neural classifier", "Single-trial neural classifier") with the readings (1) to (5)
# that the claims file names. Every reading is run and printed; the readings are labelled
# (1a) each of the 100 random samples is one decision, (1b) the 100 samples' log-likelihoods are
# summed for one decision; (2a) the number of PCs chosen on validation accuracy, (2b) on an inner
# split of the model data; st_a and st_b are the spectro-temporal classifier with a chosen on the
# model or the validation log-likelihood. The aMUA sampling rate is the files' 2034.5 Hz.'''
s=s.replace('# HEADER', HEADER)
R={
'RES_FIG1K':'''Result: under the code's window (the first half of the raster, as NeuralExample.m computes Fig 1) and the channel-averaged curve, all ten widths are within tolerance (crowd 2.8, water 3.1, fire 4.4 ms at 50%; 5.5, 7.1, 12.2 ms at 10%; bird 5.6 and 156.8 ms; snake 7.6 and 20.6 ms), and crowd and water are narrower than fire. The snake side peak is at 60.9 ms, outside 50 +/- 5 ms, so 10 of 11 values match. Under the claims file's two windows (the whole response, 1000 ms windows) 6 to 8 of 11 match; the bird's 10% width there is 138.8 or 50.2 ms.**''',
'RES_SNR':'''Result: both mean SNRs are within tolerance under most readings (13 sites, one value per site and sound, whole window: spectral -11.8 dB, temporal -8.1 dB), and the SNR is below 0 dB for 97% of spectral and 88% of temporal values. No reading puts three of the four range bounds within tolerance (at most 2 of 4; whole window, per site and sound: spectral -34.0 to 1.0 dB, temporal -29.3 to 7.7 dB). At the example site alone the means are -4.3 and -1.9 dB.**''',
'RES_FIG2':'''Result: in every window reading the noise correlations are narrower than the stimulus-driven ones at 50% of the maximum for 5 of 5 sounds in both domains (whole window, spectral 1.8 to 2.0 against 6.6 to 9.1 channels; temporal 1.2 against 4.8 to 7.5 ms), and their SD across sounds is smaller in both domains (spectral 0.33 against 0.68, temporal 3.63 against 48.67). The bird chorus keeps a stimulus-driven correlation of 0.22 at 50 ms (noise 0.05), and the snake's stimulus-driven curve has a side peak at 55 ms.**''',
'RES_FIG3A_TONO':'''Result: removing tonotopy lowers the temporal classifier at 1 s by 20 to 40 points under every reading, but no reading puts both values within tolerance: reading (1a)(2a) gives 78.4% with tonotopy (in tolerance) and 45.1% without (outside 35 +/- 3.5%); reading (1b)(2b) gives 70% and 30%.**''',
'RES_FIG3A_ORDER':'''Result: the single-trial order spectro-temporal >= spectral >= temporal holds under 5 of the 8 reading combinations (for example (1a)(2b) with a on the model data, 86.4, 77.7 and 64.4%), but the noiseless rule holds under none: the noiseless spectral classifier exceeds the single-trial one by 12 to 21 points under the (1a) readings, but the noiseless spectro-temporal classifier is not always 5 points higher, and the noiseless temporal classifier is 13 to 30 points below the single-trial one, not similar.**''',
'RES_FIG3B':'''Result: under every reading, all four single-trial classifiers exceed 20% at 1 s across the 13 sites (reading (1a)(2a): spectro-temporal 77.8%, spectral 76.9%, temporal 68.7%, without tonotopy 43.1%; largest two-sided p 7.8e-07), each is higher at 1 s than at 62.5 ms, and removing tonotopy lowers the temporal classifier by 25.6 points (paired t = 7.87, p = 4.4e-06). Both animals show the same pattern.**''',
'RES_FIGS6':'''Result: under the (1a) readings, 18 of the 18 non-snake-temporal conditions exceed chance at p < 0.05 with PCs chosen on validation (16 of 18 with the inner split) and the two snake temporal conditions do not. Under the (1b) readings 16 to 18 of 18 exceed chance but a snake temporal condition does too.**''',
'RES_FIG4':'''Result: at the example site the spectral correlations of original and 1/f responses agree as reported (whole window, r = 0.930 +/- 0.019 against 0.92 +/- 0.01), but the temporal correlations agree more closely than reported (r = 0.898 +/- 0.022 against 0.72 +/- 0.07), outside the tolerance and outside 10% under every reading.**''',
'RES_FIG4E':'''Result: same-sound correlations exceed across-sound ones in both domains under every reading, but none of the four values is within its stated SE: whole window, same sound spectral 0.879 and temporal 0.917 (reported 0.95 and 0.80), across sounds 0.818 and 0.639 (0.85 and 0.57). At most 3 of the 4 are within 10% (first-half window).**''',
'RES_FIG4F':'''Result: at the example site the correlation classifiers trained on the original sounds stay above 40% on the 1/f sounds under the (1a) readings, and the spectrum classifier falls from 86 to 90% on the original sounds to 25 to 31% on the 1/f sounds. With the half split and (1a)(2a), a on the validation data, the four values are within tolerance (spectral 58, temporal 65, spectro-temporal 65, spectrum on original 90%) but the spectrum classifier on 1/f is 31%, not below 30%; with (1a)(2b) it is 29% and three of the four values are within tolerance.**''',
'RES_FIG4H':'''Result: across the 11 sites the correlation classifiers stay above chance on the 1/f sounds at 1 s under every reading (half split, (1a)(2a): spectral 50.4, temporal 54.0, spectro-temporal 54.4%, two-sided p < 1e-06), and the spectrum classifier falls from 90.0 +/- 2.2% on the original sounds to 30.0 +/- 1.3% on the 1/f sounds, below every correlation classifier. At most 3 of the 5 values are within tolerance (spectral, temporal and the spectrum classifier on the original sounds).**''',
'RES_FIG8B':'''Result: with 1000 ms windows (single-trial correlations) two PCs explain 96.3% of the spectral and 85.3% of the temporal variance, both within tolerance, and a nearest-centroid rule in the two-PC space classifies 88.6% (spectral) and 85.6% (temporal) of held-out exemplar windows correctly (chance 33.3%). With 500 ms shuffled windows the temporal value is 77.0%, just outside 85.9 +/- 8.59%.**''',
'RES_FIG8E':'''Result: at the example site all three correlation classifiers reach at least 93% at 1 s under every reading (for example reading (a), (1a)(2a): spectro-temporal 95, spectral 93, temporal 98%), each higher than at 62.5 ms (50 to 83%), and the spectrum classifier reaches 91 to 94%.**''',
'RES_FIG8F':'''Result: across the 11 sites, under every reading, the four classifiers are within tolerance at 1 s and above 33.3% (reading (a), (1a)(2a): spectro-temporal 94.8, temporal 94.8, spectral 92.2, spectrum 93.3%; two-sided p < 1e-12), and each is higher at 1 s than at 62.5 ms. Both animals show the same values.**''',
'RES_FIGS9':'''Result: the medians of a depend strongly on how a is chosen. One reading puts both medians within tolerance: (1b)(2a) with a chosen on the validation data, pooled 24 sites median 0.70 (quartiles 0.40, 0.90) and paradigm 3 (whole response) median 0.50. With a chosen on the model data, the paradigm 1 and 2 medians are 0.50 to 0.60 but the paradigm 3 medians are 0.80 to 0.90; with a chosen on the validation data and the (1a) readings, the paradigm 3 medians are 0.00 to 0.40.**''',
}
for k,v in R.items():
    assert '**Result: '+k+'**' in s, k
    s=s.replace('**Result: '+k+'**', '**'+v)
SUMMARY='''# | Claim | Outcome |
# |---|---|
# | fig1k-example-temporal-widths | reproduced (code's window; 6 to 8 of 11 under the claims file's windows) |
# | fig1-snr-noise-stronger | partially reproduced (means hold, range bounds do not) |
# | fig1-s5-model-predicts-neural | blocked, data missing |
# | fig2-noise-restricted | reproduced |
# | fig3a-example-tonotopy-removal | partially reproduced |
# | fig3a-example-classifier-order | partially reproduced |
# | fig3b-population-above-chance | reproduced |
# | figs6-per-sound-above-chance | reproduced |
# | figs9-mixing-coefficient | reproduced under one reading of many |
# | figs10-amua-tmua | blocked, data missing |
# | fig4-example-original-vs-equalized | not reproduced |
# | fig4e-population-original-vs-equalized | not reproduced |
# | fig4f-example-equalized-classification | partially reproduced |
# | fig4h-population-equalized-classification | partially reproduced |
# | fig8b-example-pca-variance | reproduced |
# | fig8e-example-categorization | reproduced |
# | fig8f-population-categorization | reproduced |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# How the analysis differs from the paper's: the aMUA rate is the files' 2034.5 Hz, not 2 kHz;
# the classifier's open details (how the 100 time samples enter a decision, how the PCs are
# chosen, how a is fitted, how paradigm 2 and 3 data are split) are run under every reading the
# claims file names, as printed above; the noiseless classifier is run at the example site and
# at 1 s only; the spectrum (rate) classifier uses the mean aMUA of each channel in the window.
#
# What was found about the dataset: the files hold aMUA rasters only, with no tone-pip responses
# (best frequencies) and no raw voltage (thresholded MUA); the sampling rate is 2034.5 Hz where the
# paper states 2 kHz; the channel order along the probe (which channels are high frequency) is not
# documented; one paradigm 2 site (P2_Site08) has 13 trials where the paper states 14; the site,
# animal and trial counts otherwise match the paper (13 sites, 4 and 9 per animal; 11 and 11, 3
# and 8), no raster is deposited twice, and every raster is locked to the trial start.'''
s=s.replace('# SUMMARY', SUMMARY)
open('src_neural.py','w').write(s)
PYEOF
python3 $TMPDIR/fill_neural.py && grep -c "RES_" src_neural.py
```

```
Exit code 1
0
```

**Agent**

Filled. Correcting two counts I misread (classifier order holds under 4 of 8 combinations; the three fig4h values in tolerance) and one p bound:

**Agent calls Bash**

```bash
python3 - <<'EOF'
s=open('src_neural.py').read()
for a,b in [("holds under 5 of the 8 reading combinations","holds under 4 of the 8 reading combinations"),
 ("At most 3 of the 5 values are within tolerance (spectral, temporal and the spectrum classifier on the original sounds).","At most 3 of the 5 values are within tolerance (spectral 50.4%, spectro-temporal 54.4% and the spectrum classifier on the original sounds; temporal 54.0% is just outside 49 +/- 4.9% and the spectrum classifier on 1/f, 30.0%, outside 27 +/- 1%)."),
 ("spectrum 93.3%; two-sided p < 1e-12)","spectrum 93.3%; two-sided p < 1e-10)")]:
    assert a in s, a; s=s.replace(a,b)
open('src_neural.py','w').write(s)
EOF
echo ok
```

```
ok
```

**Agent**

Now the model notebook's header, conclusions and the cost cell's reading (7)(a) estimate:

**Agent calls Bash**

```bash
cat > $TMPDIR/fill_model.py <<'PYEOF'
s=open('src_model.py').read()
s=s.replace('''print(f"elapsed so far in this notebook: {(time.time() - T_START) / 60:.1f} min")''','''# reading (7)(a): N_c chosen by cross-validated likelihood over 1 to 20 components, at least one
# 5-fold search per category, classifier and resolution, with fits whose cost grows with N_c
n_search = 13 * 3 * 10 * 20 * 5
for k, v in fit_t.items():
    print(f"reading (7)(a) adds at least {n_search} fits ({k}): {n_search * v * 10.5 / 8 / 60:.0f} min")
print(f"elapsed so far in this notebook: {(time.time() - T_START) / 60:.1f} min")''')
HEADER='''# Paper: Sadeghi M, Zhai X, Stevenson IH, Escabi MA (2019). A neural ensemble correlation code for
# sound category identification. PLoS Biol 17(10):e3000449, doi:10.1371/journal.pbio.3000449. The
# claims file (claims/sadeghi-2019.yaml) was written from the version of record (PMC6788721) with
# its supplement.
#
# Dataset: CRCNS bst-2 (doi:10.6080/K03X84V3), bst-2/live/data.tar.gz in the public bucket
# crcnsarchive, `unversioned` (CRCNS does not version data sets; the paper cites the DOI only, and
# this is the bucket's only copy). MD5 of data.tar.gz from bst-2/live/checksums.md5:
# 916ae724cd3334a16a4396b861e4abe0. The model sounds are data/Sounds/ModelSounds/<category>/Sound_<n>.wav.
#
# This notebook tests the auditory model claims; the neural claims are in
# reproduce_sadeghi_2019_neural.ipynb.
#
# | Claim | Tested here |
# |---|---|
# | fig5-speech-water-widths | tested |
# | fig6-category-half-widths | tested |
# | fig6c-category-diversity | tested |
# | fig7i-stationarity | tested |
# | fig9a-optimal-resolution | blocked: too large for this run (estimate below) |
# | fig9b-similar-maximum | blocked: too large (same classifier) |
# | fig9b-accumulation-rate | blocked: too large (same classifier) |
# | fig9c-time-averaged-worse | blocked: too large (same classifier) |
# | fig9e-category-specific | blocked: too large (same classifier) |
# | fig9-spectrum-classifier-lower | blocked: too large (same classifier) |
# | fig10-vocalization-background | blocked: too large (same classifier) |
#
# Method: the cochlear model and short-term correlations follow the Methods ("Auditory model",
# "Nonstationary spectro-temporal correlation statistics", "Stationarity and ensemble diversity
# indices") and port the paper's code in the data set (Code/AuditoryModelCorr); model.py says
# where each parameter comes from. White noise is generated, as the data set does not hold it.'''
s=s.replace('# HEADER', HEADER)
R={'RES_FIG5':'''Result: with the time-averaged short-term autocorrelation at tau_W = 566 ms, the speech example's half width is 64.5 ms and the water example's 4.0 ms (median over channels 70.0 and 4.1 ms), all within tolerance; with the long-term correlation of the whole envelopes speech is 81.1 ms, outside it. The speech example's spectral correlations are broader than the water example's (mean off-diagonal zero-lag correlation 0.464 against 0.259).**''',
'RES_FIG6':'''Result: with the 566 ms short-term reading and the channel-averaged curve, four of five category half widths are within tolerance (flowing water 3.9, wind 3.9, speech 67.9, dogs 82.4 ms); cats are 160.9 ms against 117.3 +/- 11.7 ms. Every vocalization is wider than water and wind under every reading. Spectral breadth is highest for dogs, bells and speech (0.484, 0.436, 0.429) and lowest for flowing water (0.265), with single bird songs (0.273) low as well.**''',
'RES_FIG6C':'''Result: with norms not squared (reading (c)), five of the six CDIs are within tolerance (speech 0.123, crowd noise 0.144, wind 0.171, dogs 0.222, fire 0.381; single bird songs 0.373 against 0.29 +/- 0.029), speech is the lowest of the 13 categories, white noise is lower still (0.042), and the six keep the paper's rank order. With squared norms (readings (a) and (b)) the values are about ten times smaller (speech 0.016) and none is within tolerance.**''',
'RES_FIG7I':'''Result: speech has the lowest category mean SI and white noise the highest under both readings, and environmental sounds are more stationary than vocalizations, but the values are not those reported: reading (a) gives 0.719 +/- 0.048 for the environmental categories and 0.358 +/- 0.089 for vocalizations (reported 0.49 +/- 0.04 and 0.28 +/- 0.04), reading (b) 0.792 and 0.621, and adding bird chorus and speech babble gives 0.654 under (a).**''',
'RES_FIG9COST':'''Result: the leave-one-sound-out classifier needs features at ten resolutions (13.6 min for 195 sounds) and at least 76050 GMM fits even with the reported PC and component counts (18 min with non-overlapping training windows, 61 min with windows every tau_W / 4), and choosing N_c by cross-validation as the Methods say adds about as much again. With the 14.5 min of correlations above, the notebook would take 46 to 150 min, and building and running the classifier does not fit the time left in this run; the seven classification claims are blocked as too large.**'''}
for k,v in R.items():
    assert '**Result: '+k+'**' in s, k
    s=s.replace('**Result: '+k+'**', '**'+v)
SUMMARY='''# | Claim | Outcome |
# |---|---|
# | fig5-speech-water-widths | reproduced |
# | fig6-category-half-widths | reproduced |
# | fig6c-category-diversity | reproduced (norms not squared) |
# | fig7i-stationarity | not reproduced (order holds, values do not) |
# | fig9a, fig9b (two), fig9c, fig9e, fig9 spectrum, fig10 | blocked, too large for this run |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# How the analysis differs from the paper's: the Methods' critical bandwidths are used where the
# code (criticalbandwidth.m) has another formula; envelopes are at 1 kHz as the Methods say (the
# code's example keeps 3675 Hz); the short-term correlation is sampled every tau_W / 4; white noise
# is generated. What was found about the dataset: the 195 sounds, 15 per category, 10 s at
# 44.1 kHz, are all there, as 16 bit integer WAV files where the description says double
# precision; white noise is not included.'''
s=s.replace('# SUMMARY', SUMMARY)
open('src_model.py','w').write(s)
PYEOF
cd entries/sadeghi-2019 && python3 $TMPDIR/fill_model.py && . $TMPDIR/dev/bin/activate && jupytext --to ipynb -q src_neural.py -o reproduce_sadeghi_2019_neural.ipynb && jupytext --to ipynb -q src_model.py -o reproduce_sadeghi_2019_model.ipynb && mv src_neural.py src_model.py $TMPDIR/ && python - <<'EOF'
import json
for f in ("reproduce_sadeghi_2019_neural.ipynb","reproduce_sadeghi_2019_model.ipynb"):
    nb=json.load(open(f)); nb['metadata'].pop('jupytext',None)
    nb['metadata']['kernelspec']={"display_name":"Python 3","language":"python","name":"python3"}
    json.dump(nb,open(f,'w'),indent=1)
    print(f, len(nb['cells']), [c['metadata'].get('tags') for c in nb['cells'] if c['metadata'].get('tags')])
EOF
ls
```

```
reproduce_sadeghi_2019_neural.ipynb 62 [['sanity'], ['claim:fig1k-example-temporal-widths'], ['claim:fig1-snr-noise-stronger'], ['claim:fig2-noise-restricted'], ['claim:fig3a-example-tonotopy-removal'], ['claim:fig3a-example-classifier-order'], ['claim:fig3b-population-above-chance'], ['claim:figs6-per-sound-above-chance'], ['claim:fig4-example-original-vs-equalized'], ['claim:fig4e-population-original-vs-equalized'], ['claim:fig4f-example-equalized-classification'], ['claim:fig4h-population-equalized-classification'], ['claim:fig8b-example-pca-variance'], ['claim:fig8e-example-categorization'], ['claim:fig8f-population-categorization'], ['claim:figs9-mixing-coefficient']]
reproduce_sadeghi_2019_model.ipynb 25 [['sanity'], ['claim:fig5-speech-water-widths'], ['claim:fig6-category-half-widths'], ['claim:fig6c-category-diversity'], ['claim:fig7i-stationarity']]
__pycache__
entry.yaml
model.py
reproduce_sadeghi_2019_model.ipynb
reproduce_sadeghi_2019_neural.ipynb
requirements.in
sadeghi.py
```

**Agent**

Notebooks are built with their tags. Locking and running the entry from a clean environment (about 50 minutes):

**Agent calls Bash**

```bash
cd  && rm -rf entries/sadeghi-2019/__pycache__ && date -u && python tools/entry.py lock entries/sadeghi-2019 2>&1 | tail -5 && python tools/entry.py check entries/sadeghi-2019 2>&1 | tail -15
```

```
Fri Nov 13 21:42:41 UTC 2026
wrote sadeghi-2019/requirements.lock.txt (Python 3.13, with hashes)
error: entries/sadeghi-2019/reproduce_sadeghi_2019_neural.ipynb: neither the notebook nor a helper names version unversioned of dataset bst-2, which entry.yaml pins
error: entries/sadeghi-2019/reproduce_sadeghi_2019_model.ipynb: neither the notebook nor a helper names version unversioned of dataset bst-2, which entry.yaml pins
2 error(s)
```

**Agent calls Bash**

```bash
grep -n "unversioned" entries/fujisawa-2008-crcns-pfc-2/*.py entries/fujisawa-2008-crcns-pfc-2/*.ipynb | head -5
```

```
entries/fujisawa-2008-crcns-pfc-2/pfc2.py:57:DATASET = "crcns:pfc-2/unversioned"  # CRCNS data sets are not versioned (docs/archives.md)
entries/fujisawa-2008-crcns-pfc-2/reproduce_fujisawa_2008.ipynb:15:    "Dataset: CRCNS pfc-2, doi:10.6080/K01V5BWK (dataset `crcns:pfc-2/unversioned`). CRCNS data sets\n",
entries/fujisawa-2008-crcns-pfc-2/reproduce_fujisawa_2008.ipynb:16:    "are not versioned (docs/archives.md), so the version pinned is `unversioned`: the files as they\n",
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='entries/sadeghi-2019/sadeghi.py'
s=open(p).read()
s=s.replace('URL = "https://crcnsarchive','DATASET = "crcns:bst-2/unversioned"  # CRCNS data sets are not versioned (docs/archives.md)\nURL = "https://crcnsarchive',1)
open(p,'w').write(s)
for f in ("entries/sadeghi-2019/reproduce_sadeghi_2019_neural.ipynb","entries/sadeghi-2019/reproduce_sadeghi_2019_model.ipynb"):
    s=open(f).read()
    s=s.replace("CRCNS data sets are not versioned, so the version is recorded as\\n\",\n    \"`unversioned`","CRCNS data sets are not versioned, so the version is recorded as\\n\",\n    \"`unversioned` (dataset `crcns:bst-2/unversioned`)")
    s=s.replace("crcnsarchive, `unversioned` (CRCNS","crcnsarchive, `crcns:bst-2/unversioned` (CRCNS")
    open(f,'w').write(s)
EOF
grep -c "crcns:bst-2/unversioned" entries/sadeghi-2019/*.ipynb; python tools/entry.py check entries/sadeghi-2019 2>&1 | tail -8
```

```
entries/sadeghi-2019/reproduce_sadeghi_2019_model.ipynb:1
entries/sadeghi-2019/reproduce_sadeghi_2019_neural.ipynb:1
0 error(s)
```

**Agent**

Checks pass. Writing the entry README before the run (it is part of the entry):

**Agent calls Write**

```json
{
 "file_path": "entries/sadeghi-2019/README.md",
 "content": "# Sadeghi, Zhai, Stevenson & Escabi (2019) from CRCNS bst-2\n\nTests the findings of [Sadeghi et al. (2019)](https://doi.org/10.1371/journal.pbio.3000449) that\ncan be tested on [CRCNS bst-2](https://doi.org/10.6080/K03X84V3), which holds the analog multiunit\nactivity of 35 inferior colliculus recordings in unanesthetized rabbits (13 sites for paradigm 1,\n11 for paradigm 2, 11 for paradigm 3), the paradigms' sounds and the 195 sounds of the paper's\nauditory model, with the paper's MATLAB code.\n\n| Claim | Outcome |\n|---|---|\n| Example site temporal correlation widths (Fig 1K) | Reproduced |\n| Noise correlations stronger than stimulus-driven ones (SNR) | Partially reproduced |\n| Model spectral correlations predict neural ones (S5 Fig) | Blocked: data missing |\n| Noise correlations more restricted and consistent (Fig 2) | Reproduced |\n| Example site, tonotopy removal lowers the temporal classifier (72 to 35%) | Partially reproduced |\n| Example site, classifier order and noiseless bound | Partially reproduced |\n| Paradigm 1 population classifiers above chance (Fig 3B) | Reproduced |\n| Per-sound accuracy above chance except snake temporal (S6 Fig) | Reproduced |\n| Mixing coefficient near 0.5 to 0.6 (S9 Fig) | Reproduced |\n| aMUA against thresholded MUA (S10 Fig) | Blocked: data missing |\n| Example site, original and 1/f correlations similar (Fig 4A to D) | Not reproduced |\n| Population, original and 1/f correlations (Fig 4E) | Not reproduced |\n| Example site, classification of 1/f sounds (Fig 4F) | Partially reproduced |\n| Population, classification of 1/f sounds (Fig 4G, H) | Partially reproduced |\n| Example site, two PCs explain most variance (Fig 8B, D) | Reproduced |\n| Example site, three-category classification (Fig 8E) | Reproduced |\n| Population, three-category classification (Fig 8F) | Reproduced |\n| Model, speech and water widths (Fig 5) | Reproduced |\n| Model, category half widths (Fig 6A, B) | Reproduced |\n| Model, category diversity index (Fig 6C) | Reproduced |\n| Model, stationarity index (Fig 7I) | Not reproduced |\n| Model classifiers (Figs 9 and 10, seven claims) | Blocked: too large for the run |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe data set is one 5.3 GB tar.gz file; the notebooks stream it once and parse each member in\nmemory. The neural notebook takes about 35 minutes, the model notebook about 16. The attempt\nrecord, with the reasons and the differences from the paper's method, is\n[`attempts/sadeghi-2019-01.yaml`](../../attempts/sadeghi-2019-01.yaml).\n"
}
```

```
File created successfully at: entries/sadeghi-2019/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u && python tools/entry.py all entries/sadeghi-2019 2>&1 | tail -20; date -u
```

```
Fri Nov 13 21:43:11 UTC 2026
Installed kernelspec registry-sadeghi-2019 in executed/sadeghi-2019/.venv/share/jupyter/kernels/registry-sadeghi-2019
0 error(s)
pass  reproduce_sadeghi_2019_neural.ipynb  (1787 s)
pass  reproduce_sadeghi_2019_model.ipynb  (873 s)
Fri Nov 13 22:27:38 UTC 2026
```

**Agent**

Both notebooks pass (30 and 15 minutes). Confirming the executed numbers match the ones the conclusions quote:

**Agent calls Bash**

```bash
ls executed/sadeghi-2019/ && python3 - <<'EOF' > $TMPDIR/exec_out.txt
import json
for f in ("reproduce_sadeghi_2019_neural.ipynb","reproduce_sadeghi_2019_model.ipynb"):
    nb=json.load(open('executed/sadeghi-2019/'+f))
    for c in nb['cells']:
        if c['cell_type']!='code': continue
        for o in c.get('outputs',[]):
            if o.get('output_type')=='error': print('ERROR', o['ename'])
            t=o.get('text') or o.get('data',{}).get('text/plain')
            if t: print(''.join(t))
EOF
cd $TMPDIR && python3 - <<'EOF'
import json
nb=json.load(open('dev_model_out.ipynb'))
out=[]
for c in nb['cells']:
    if c['cell_type']!='code': continue
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain')
        if t: out.append(''.join(t))
open('dev_model_out.txt','w').write('\n'.join(out))
EOF
cat full_neural_out.txt dev_model_out.txt | grep -v "done at\|^-----$\|^$\|s$\|min\|time\|elapsed\|GMM\|feature\|read 195\|^[0-9]* (" > a.txt; grep -v "done at\|^$\|s$\|min\|time\|elapsed\|GMM\|feature\|read 195\|^[0-9]* (" exec_out.txt > b.txt; diff a.txt b.txt | head -20; wc -l a.txt b.txt; grep -n "elapsed\|GMM\|feature time\|reading (7)" exec_out.txt
```

```
reproduce_sadeghi_2019_model.ipynb
reproduce_sadeghi_2019_neural.ipynb
result.json
1c1
< peak memory (GB): 3.620584
---
> peak memory (GB): 3.627208
   367 a.txt
   367 b.txt
   734 total
498:feature time for one sound over the ten resolutions (s): [0.29 0.22 0.26 0.19 0.25 0.22 0.27 0.23 0.3  0.29] ; cochleogram 1.53
500:one GMM fit (8 diagonal components, 26 PCs, tau_W/4 at 141 ms training observations of one category): 0.05 s; 76050 fits (195 folds x 13 categories x 3 classifiers x 10 resolutions): 61 min
501:one GMM fit (8 diagonal components, 26 PCs, non-overlapping 141 ms training observations of one category): 0.01 s; 76050 fits (195 folds x 13 categories x 3 classifiers x 10 resolutions): 17 min
502:reading (7)(a) adds at least 39000 fits (tau_W/4 at 141 ms): 41 min
503:reading (7)(a) adds at least 39000 fits (non-overlapping 141 ms): 11 min
504:elapsed so far in this notebook: 14.5 min
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n "features for 195" $TMPDIR/exec_out.txt; sed -n 1,80p tools/entry.py | grep -n "stamp\|fresh\|per notebook" ; grep -n "def cmd_run\|stamp" tools/entry.py | head -20
```

```
499:features for 195 sounds at ten resolutions: 13.2 min
25:`run` builds a fresh virtual environment from the lock file and executes each
30:A run that passes leaves a stamp beside the executed copies (.clean-run.json):
33:so, without executing anything; --fresh executes all the same.
30:A run that passes leaves a stamp beside the executed copies (.clean-run.json):
520:    """The stamp of executed copies that a run now would only make again: made from this hash, each copy still as
523:        stamp = json.loads((output_dir / STAMP).read_text())
525:        if stamp["hash"] != entry_hash(entry_dir) or time.time() - stamp["finished"] > REUSE_DAYS * 86400:
527:        if [n["path"] for n in entry["notebooks"]] != [r["notebook"] for r in stamp["results"]]:
529:        for r in stamp["results"]:
532:        return stamp
539:    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
540:    if stamp:
541:        when = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(stamp["finished"]))
542:        for r in stamp["results"]:
545:              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
f='entries/sadeghi-2019/reproduce_sadeghi_2019_model.ipynb'
nb=json.load(open(f))
done=0
for c in nb['cells']:
    src=''.join(c['source'])
    if 'print(f"elapsed so far in this notebook' in src:
        src=src.replace('print(f"elapsed so far in this notebook: {(time.time() - T_START) / 60:.1f} min")',
'''elapsed = (time.time() - T_START) / 60
v_lo, v_hi = min(fit_t.values()), max(fit_t.values())
lo = elapsed + feat_total / 60 + (nfits + n_search * 10.5 / 8) * v_lo / 60
hi = elapsed + feat_total / 60 + (nfits + n_search * 10.5 / 8) * v_hi / 60
print(f"elapsed so far in this notebook: {elapsed:.1f} min; with the classifier the notebook would take about {lo:.0f} to {hi:.0f} min")''')
        c['source']=src.splitlines(True); done+=1
    if src.startswith('**Result: the leave-one-sound-out'):
        c['source']=['**Result: the leave-one-sound-out classifier needs features at ten resolutions (about 13 min for 195 sounds) and at least 76050 GMM fits even with the reported PC and component counts (about 17 min with non-overlapping training windows, about 61 min with windows every tau_W / 4); choosing N_c by cross-validation, as the Methods say, adds about 11 to 41 min. With the correlations above, the notebook would take about 56 to 130 min (printed above), over the 60 minute limit except under the cheapest readings, and building and running the classifier does not fit the time left in this run. The seven classification claims are blocked as too large.**']
        done+=1
json.dump(nb,open(f,'w'),indent=1)
print(done)
EOF
date -u; python tools/entry.py all entries/sadeghi-2019 2>&1 | tail -4; date -u
```

```
2
Fri Nov 13 22:28:13 UTC 2026
Installed kernelspec registry-sadeghi-2019 in executed/sadeghi-2019/.venv/share/jupyter/kernels/registry-sadeghi-2019
0 error(s)
pass  reproduce_sadeghi_2019_neural.ipynb  (1957 s)
pass  reproduce_sadeghi_2019_model.ipynb  (912 s)
Fri Nov 13 23:16:11 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF' > $TMPDIR/exec2.txt
import json
for f in ("reproduce_sadeghi_2019_neural.ipynb","reproduce_sadeghi_2019_model.ipynb"):
    nb=json.load(open('executed/sadeghi-2019/'+f))
    for c in nb['cells']:
        if c['cell_type']!='code': continue
        for o in c.get('outputs',[]):
            if o.get('output_type')=='error': print('ERROR', o['ename'])
            t=o.get('text') or o.get('data',{}).get('text/plain')
            if t: print(''.join(t))
EOF
cd $TMPDIR && grep -v "done at\|^$\|s$\|min\|time\|elapsed\|GMM\|feature\|read 195\|^[0-9]* (\|peak memory" exec2.txt > c.txt; grep -v "peak memory" b.txt | diff - c.txt | head; grep -n "ERROR\|elapsed\|features for\|reading (7)\|GMM fit" exec2.txt; date -u
```

```
499:features for 195 sounds at ten resolutions: 14.9 min
500:one GMM fit (8 diagonal components, 26 PCs, tau_W/4 at 141 ms training observations of one category): 0.06 s; 76050 fits (195 folds x 13 categories x 3 classifiers x 10 resolutions): 73 min
501:one GMM fit (8 diagonal components, 26 PCs, non-overlapping 141 ms training observations of one category): 0.02 s; 76050 fits (195 folds x 13 categories x 3 classifiers x 10 resolutions): 20 min
502:reading (7)(a) adds at least 39000 fits (tau_W/4 at 141 ms): 49 min
503:reading (7)(a) adds at least 39000 fits (non-overlapping 141 ms): 13 min
504:elapsed so far in this notebook: 15.1 min; with the classifier the notebook would take about 63 to 152 min
Fri Nov 13 23:16:17 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
f='entries/sadeghi-2019/reproduce_sadeghi_2019_model.ipynb'
nb=json.load(open(f))
for c in nb['cells']:
    src=''.join(c['source'])
    if src.startswith('**Result: the leave-one-sound-out'):
        c['source']=['**Result: the leave-one-sound-out classifier needs features at ten resolutions and at least 76050 GMM fits even with the reported PC and component counts, and choosing N_c by cross-validation, as the Methods say, adds at least 39000 more. The cell prints the estimated duration of this notebook with the classifier, which is of the order of one to two and a half hours and depends on the machine; under the more expensive readings it is well over the 60 minute limit, and building and running the classifier does not fit the time left in this run. The seven classification claims are blocked as too large.**']
json.dump(nb,open(f,'w'),indent=1)
EOF
python tools/entry.py check entries/sadeghi-2019 2>&1 | tail -2; date -u
```

```
0 error(s)
Fri Nov 13 23:16:44 UTC 2026
```

**Agent**

Writing the attempt record:

**Agent calls Write**

```json
{
 "file_path": "attempts/sadeghi-2019-01.yaml",
 "content": "schema_version: 3\nid: sadeghi-2019-01\ndatasets:\n- archive: crcns\n  id: bst-2\n  version: unversioned\n  doi: 10.6080/K03X84V3\n  relation: primary\npaper: doi:10.1371/journal.pbio.3000449\ndate: '2026-11-13'\nentry: sadeghi-2019\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-15\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/43495516371\noutcomes:\n- claim: fig1k-example-temporal-widths\n  outcome: reproduced\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:fig1k-example-temporal-widths\n  measured: [2.8, 3.1, 4.4, 5.5, 7.1, 12.2, 5.6, 156.8, 7.6, 20.6, 60.9]\n  notes: At P1_Site04, with the window of the paper's code (the first half of the raster, as\n    NeuralExample.m computes Fig 1) and the channel-averaged stimulus-driven temporal correlation,\n    all ten widths are within tolerance and crowd and water are narrower than fire at 50%. The\n    snake's side peak is at 60.9 ms (channels 9 to 16), outside 50 +/- 5 ms, so 10 of 11 values\n    match. Under the two windows the claims file names, the whole response and 1000 ms windows,\n    6 to 8 of 11 values match (partially reproduced by the criterion); the bird's 10% width is\n    then 138.8 or 50.2 ms. With the median over channels, 7 to 8 of 11 match under every window.\n  deviations:\n  - The window is taken from the paper's code, Code/Examples/NeuralExample.m, which computes Fig 1\n    from the first half of each raster (T0 at its centre, Tw = NS - 2 MaxLag - 2 samples), as the\n    claims file's opening comment allows; the claims file's two readings are shown as variants.\n  - The aMUA is at the files' 2034.5 Hz, so the lag step is 0.49 ms where the paper's 2 kHz gives\n    0.5 ms.\n  - The channel order along the probe is not documented, so the high-frequency channels for the\n    period are read as channels 9 to 16 and, as a variant, 1 to 8 (52 to 62 ms either way);\n    reading (b), best frequency above 2 kHz, cannot be run without best frequencies.\n- claim: fig1-snr-noise-stronger\n  outcome: partially_reproduced\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:fig1-snr-noise-stronger\n  measured: [-11.8, -8.1, -34.0, 1.0, -29.3, 7.7]\n  notes: Reading (a)(c)(e), whole window, 65 site and sound values, spectral SNR mean -11.8 dB (SD\n    8.0, range -34.0 to 1.0) and temporal mean -8.1 dB (SD 9.0, range -29.3 to 7.7); 97% and 88% of\n    the values are below 0 dB. Both means are within tolerance under 15 of the 18 readings, but no\n    reading puts more than two of the four range bounds within tolerance (per site averages,\n    spectral -26.8 to -1.4 and temporal -26.6 to 1.2 dB in the whole window). At the example site\n    alone the means are -4.3 and -1.9 dB.\n  deviations:\n  - The SNR formula is not in the text; the readings of the claims file (squared stimulus-driven\n    over squared noise correlations, with and without the zero-lag diagonal, per site and sound or\n    per site, all sites or the example) are all run, under three windows.\n- claim: fig1-s5-model-predicts-neural\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The test needs each recording channel's best frequency, from the tone-pip frequency\n    response areas (Fig 1A, S5 Fig legend). The data set holds only the aMUA rasters to the natural\n    sounds; its file list (data.tar.gz members) and description have no tone-pip recordings or best\n    frequencies, and the channel order along the probe is not documented, so the model channels\n    cannot be matched to recording channels.\n- claim: fig2-noise-restricted\n  outcome: reproduced\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:fig2-noise-restricted\n  notes: Over the 13 paradigm 1 sites, with widths at 50% of the maximum (reading (a)), the noise\n    correlations are narrower than the stimulus-driven ones for 5 of 5 sounds in both domains under\n    every window (whole window, spectral 1.8 to 2.0 against 6.6 to 9.1 channels, temporal 1.2\n    against 4.8 to 7.5 ms), and their SD across sounds is smaller in both domains (spectral 0.33\n    against 0.68, temporal 3.63 against 48.67). Under reading (b), the mean beyond 2 channels or 10\n    ms, noise is lower for 5 of 5 sounds spectrally but for 2 of 5 temporally, as the stimulus-driven\n    temporal correlations of fire, water and snake fall below zero beyond 10 ms. The bird chorus\n    keeps a stimulus-driven correlation of 0.22 at 50 ms (noise 0.05) and the snake a side peak at\n    55 ms.\n  deviations:\n  - Each site's collapsed curves are normalised by their value at offset 0 or lag 0 before\n    averaging (the claims file's open step).\n- claim: fig3a-example-tonotopy-removal\n  outcome: partially_reproduced\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:fig3a-example-tonotopy-removal\n  measured: [78.4, 45.1]\n  notes: At P1_Site04, at 1 s, randomising the validation channel order lowers the temporal\n    classifier by 20 to 40 points under every reading ((1a)(2a) 78.4 to 45.1%, (1a)(2b) 64.4 to\n    31.3%, (1b)(2a) 80 to 60%, (1b)(2b) 70 to 30%). The value with tonotopy is within tolerance under\n    two readings, the value without it under none. Chance is 20%.\n  deviations:\n  - The decision rule (reading 1) and the choice of PCs (reading 2) are not settled by the paper;\n    all four combinations are run. Reading (4) concerns the spectrum classifier only.\n- claim: fig3a-example-classifier-order\n  outcome: partially_reproduced\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:fig3a-example-classifier-order\n  notes: The single-trial order spectro-temporal >= spectral >= temporal holds under 4 of 8 reading\n    combinations (for example (1a)(2b), a on the model data, 86.4, 77.7 and 64.4%). The noiseless\n    rule holds under none; the noiseless spectral classifier is 12 to 21 points above the\n    single-trial one under the (1a) readings, but the noiseless temporal classifier is 13 to 30\n    points below the single-trial one, not similar, and the noiseless spectro-temporal classifier\n    is not always 5 points higher (60 to 100% depending on how a is chosen).\n  deviations:\n  - The noiseless classifier is run at the example site at 1 s only (500 ms shuffled model windows,\n    1000 ms shuffled validation windows, 100 each), which is what the criterion compares.\n- claim: fig3b-population-above-chance\n  outcome: reproduced\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:fig3b-population-above-chance\n  notes: Under every reading, across the 13 sites, the four single-trial classifiers exceed 20% at 1\n    s ((1a)(2a) spectro-temporal 77.8%, spectral 76.9%, temporal 68.7%, without tonotopy 43.1%;\n    largest two-sided p 7.8e-07), each is higher at 1 s than at 62.5 ms, and removing tonotopy\n    lowers the temporal classifier by 25.6 points (paired t = 7.87, p = 4.4e-06; 25.4 to 31.5 points\n    under the other readings). The 4 sites of one animal and the 9 of the other show the same\n    pattern.\n- claim: figs6-per-sound-above-chance\n  outcome: reproduced\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:figs6-per-sound-above-chance\n  notes: Under reading (1a) with PCs chosen on validation, all 18 non-snake-temporal conditions\n    exceed 20% at p < 0.05 across the 13 sites and the two snake temporal conditions do not (16 of\n    18 with the inner split). Under the (1b) readings, 16 to 18 of 18 exceed chance but a snake\n    temporal condition does too, so the claim holds under the (1a) readings only.\n  deviations:\n  - The decision rule is not settled by the paper (reading 1); the outcome holds under (1a) and not\n    under (1b), and the criterion takes any reading.\n- claim: figs9-mixing-coefficient\n  outcome: reproduced\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:figs9-mixing-coefficient\n  measured: [0.7, 0.5]\n  notes: One reading puts both medians within tolerance, (1b)(2a) with a chosen on the validation\n    data, the 24 paradigm 1 and 2 sites pooled (median 0.70, quartiles 0.40 and 0.90) and paradigm 3\n    with whole responses (median 0.50, 25th percentile 0.25). The result depends strongly on how a\n    is chosen; with a fitted on the model data the paradigm 1 and 2 medians are 0.50 to 0.60, as\n    reported, but the paradigm 3 medians are 0.80 to 0.90; with a fitted on the validation data and\n    the (1a) readings the paradigm 3 medians are 0.00 to 0.40. No reading matches per paradigm.\n  deviations:\n  - The paper says only that a maximises the log-likelihood; a is chosen on the summed log-posterior\n    of the true sound, on the model data or on the validation data, over a grid of 0 to 1 in steps\n    of 0.1, and both are shown. Paradigm 2 uses its half split classifier (reading 3a).\n- claim: figs10-amua-tmua\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Thresholded MUA needs the raw voltage traces (events 2 SDs above the noise floor). The\n    data set holds only the aMUA envelopes downsampled to 2034.5 Hz; neither its file list nor its\n    description has voltage traces or spike times.\n- claim: fig4-example-original-vs-equalized\n  outcome: not_reproduced\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:fig4-example-original-vs-equalized\n  measured: [0.93, 0.898]\n  notes: At P2_Site11, over the five sounds, original against 1/f stimulus-driven correlations give\n    spectral r = 0.930 +/- 0.019 (within 0.92 +/- 0.01) and temporal r = 0.898 +/- 0.022, higher\n    than the reported 0.72 +/- 0.07 and outside 10% of it under every reading (0.875 to 0.900). The\n    correlations are as similar as the statement says, or more, but the temporal value differs from\n    the reported one.\n- claim: fig4e-population-original-vs-equalized\n  outcome: not_reproduced\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:fig4e-population-original-vs-equalized\n  measured: [0.879, 0.917, 0.818, 0.639]\n  notes: Across the 11 sites (whole window, per-site means), same sound 0.879 +/- 0.033 spectral and\n    0.917 +/- 0.007 temporal, across sounds 0.818 +/- 0.035 and 0.639 +/- 0.011. Same-sound exceeds\n    across-sound in both domains under every reading, but no value is within its stated SE and at\n    most 3 of 4 are within 10% (first-half window), so neither rule of the criterion is met. The\n    spectral values are lower and the temporal ones higher than reported.\n- claim: fig4f-example-equalized-classification\n  outcome: partially_reproduced\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:fig4f-example-equalized-classification\n  measured: [58, 65, 79, 90]\n  notes: At P2_Site11, with the half split (3a) and reading (1a)(2a), the classifiers trained on the\n    original sounds give 58% spectral, 65% temporal and 79% (a on model data) or 65% (a on validation\n    data) spectro-temporal on the 1/f sounds, and the spectrum classifier gives 90% on the original\n    sounds; with a on the validation data all four values are within tolerance, but the spectrum\n    classifier on the 1/f sounds is 31%, not below 30%. With (1a)(2b) it is 29% and three of four\n    values are within tolerance. The pattern (correlation classifiers above 40%, spectrum below 30%\n    on 1/f) holds under (1a)(2b) with the half split and under (1a) with whole responses (3b). The\n    within-site t tests over the five sounds give p 0.016 to 0.033 for spectral and temporal under\n    (1a)(2a).\n- claim: fig4h-population-equalized-classification\n  outcome: partially_reproduced\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:fig4h-population-equalized-classification\n  measured: [50.4, 54.0, 54.4, 90.0, 30.0]\n  notes: Across the 11 sites the three correlation classifiers exceed 20% on the 1/f sounds at 1 s\n    under every reading (two-sided p < 0.003), and the spectrum classifier falls from 90.0 +/- 2.2%\n    on the original sounds to 30.0 +/- 1.3% on the 1/f sounds ((1a)(2a), half split), below every\n    correlation classifier. At most 3 of the 5 values are within tolerance; temporal 54.0% is just\n    outside 49 +/- 4.9% and the spectrum classifier on 1/f sounds is outside 27 +/- 1% under most\n    readings (24.5 to 38.2%). The spectrum classifier rises from 24.7% at 62.5 ms to 30.0% at 1 s.\n    With whole responses (3b) the temporal classifier reaches 76 to 84% on the 1/f sounds.\n- claim: fig8b-example-pca-variance\n  outcome: reproduced\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:fig8b-example-pca-variance\n  measured: [96.3, 85.3]\n  notes: At P3_Site04, with 1000 ms windows of single-trial correlations (reading b), two PCs explain\n    96.3% of the spectral and 85.3% of the temporal variance of the six-exemplar training set (96.3\n    and 85.5% over the five-exemplar folds), and a nearest-centroid rule in two PCs classifies 88.6%\n    and 85.6% of held-out exemplar windows (chance 33.3%). With 1000 ms shuffled windows the values\n    are 98.3 and 88.3%; with 500 ms shuffled windows (reading a) the temporal value is 77.0%, just\n    outside the tolerance, and the spectral nearest-centroid accuracy 76.1%.\n- claim: fig8e-example-categorization\n  outcome: reproduced\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:fig8e-example-categorization\n  measured: 94\n  notes: At P3_Site04, under every reading, the three correlation classifiers reach 93 to 100% at 1 s\n    and are higher than at 62.5 ms (50 to 83%); the spectrum classifier gives 91 to 94%. Under\n    reading (a), (1a)(2a), spectro-temporal 95, spectral 93, temporal 98 and spectrum 94%.\n- claim: fig8f-population-categorization\n  outcome: reproduced\n  notebook: reproduce_sadeghi_2019_neural.ipynb\n  output: claim:fig8f-population-categorization\n  measured: [94.8, 94.8, 92.2, 93.3]\n  notes: Across the 11 sites, under every reading, the four classifiers are within tolerance at 1 s\n    and above 33.3% (reading (a), (1a)(2a), spectro-temporal 94.8, temporal 94.8, spectral 92.2,\n    spectrum 93.3%; two-sided p < 1e-10), and each is higher at 1 s than at 62.5 ms. The 3 and 8\n    sites of the two animals give the same values.\n- claim: fig5-speech-water-widths\n  outcome: reproduced\n  notebook: reproduce_sadeghi_2019_model.ipynb\n  output: claim:fig5-speech-water-widths\n  measured: [64.5, 4.0]\n  notes: With the time average of the short-term autocorrelations at tau_W = 566 ms (reading ii a)\n    and the channel-averaged curve, Human_Speech Sound_1 has a 64.5 ms and Flowing_Water Sound_1 a\n    4.0 ms half width (median over channels 70.0 and 4.1 ms). With the long-term correlation of the\n    whole envelopes speech is 81.1 ms, outside the tolerance. The speech example's mean off-diagonal\n    zero-lag correlation is 0.464 against 0.259 for water. Across the 15 speech sounds the widths\n    are 57.3 to 86.3 ms, across water 3.5 to 7.3 ms.\n  deviations:\n  - Bandwidths follow the Methods' formula, 25 + 75(1 + 1.4 f^2)^0.69, where the paper's example\n    code uses criticalbandwidth.m (94 + 71 f^1.5); envelopes are resampled to 1 kHz as the Methods\n    say, where the example code keeps 3675 Hz.\n  - The short-term correlation is sampled every tau_W / 4, a standard choice for a time average.\n- claim: fig6-category-half-widths\n  outcome: reproduced\n  notebook: reproduce_sadeghi_2019_model.ipynb\n  output: claim:fig6-category-half-widths\n  measured: [3.9, 3.9, 67.9, 82.4, 160.9]\n  notes: With the 566 ms short-term reading and the channel-averaged category mean curve, four of\n    five half widths are within tolerance (flowing water 3.9, wind 3.9, speech 67.9, dogs 82.4 ms);\n    cats are 160.9 ms against 117.3 +/- 11.7. Every vocalization is wider than water and wind under\n    all four readings. The statement's spectral part is mixed; dogs, speech and cats have high mean\n    off-diagonal correlations (0.484, 0.429, 0.388) and flowing water the lowest (0.265), but single\n    bird songs are low (0.273), below wind (0.315).\n  deviations:\n  - As in fig5-speech-water-widths.\n- claim: fig6c-category-diversity\n  outcome: reproduced\n  notebook: reproduce_sadeghi_2019_model.ipynb\n  output: claim:fig6c-category-diversity\n  measured: [0.123, 0.144, 0.171, 0.222, 0.373, 0.381]\n  notes: With norms not squared (reading c on a), five of six CDIs are within tolerance (single bird\n    songs 0.373 against 0.29 +/- 0.029), speech is the lowest of the 13 categories, white noise is\n    lower still (0.042), and the six keep the paper's rank order. With squared norms (readings a\n    and b) the values are about ten times smaller (speech 0.016, fire 0.162) and none is within\n    tolerance, though the rank order is the same.\n  deviations:\n  - White noise is generated (15 Gaussian noises of 10 s, fixed seed), as the data set does not hold\n    it.\n  - The CDI equation is lost from the text; the claims file's readings are all run, and only the one\n    with norms not squared matches the reported values.\n- claim: fig7i-stationarity\n  outcome: not_reproduced\n  notebook: reproduce_sadeghi_2019_model.ipynb\n  output: claim:fig7i-stationarity\n  measured: [0.719, 0.358]\n  notes: Under reading (a), with environmental sounds flowing water, waves, thunder and rain, and wind,\n    mean SI 0.719 +/- 0.048 against 0.49 +/- 0.04 reported, vocalizations 0.358 +/- 0.089 against\n    0.28 +/- 0.04; reading (b) gives 0.792 and 0.621, and adding bird chorus and speech babble gives\n    0.654 under (a). Speech has the lowest category mean and white noise the highest under both\n    readings, and environmental sounds are more stationary than vocalizations, but neither value is\n    within tolerance under any reading.\n  deviations:\n  - As in fig5-speech-water-widths; the SI equation is lost from the text and the claims file's two\n    readings are run.\n- claim: fig9a-optimal-resolution\n  outcome: blocked\n  blocked_by: too_large\n  notes: Not run. The model classifier needs short-term spectral and temporal features of the 195\n    sounds at ten resolutions and a leave-one-sound-out GMM classifier for three correlation\n    classifiers and the spectrum classifier. The model notebook's cost cell measured, on this\n    runner, about 13 to 15 min for the features and at least 76050 GMM fits (17 to 73 min) with the\n    reported PC and component counts (reading 7b), and at least 39000 more fits (11 to 49 min) to\n    choose N_c by cross-validation (reading 7a); with the correlations the notebook already\n    computes, it would take about 56 to 152 min, over the 60 minute limit except under the cheapest\n    readings, and writing and running it did not fit the time left in this run after the neural and\n    model correlation analyses. The model correlations, the 195 sounds and the paper's code are all\n    in the data set, so a later attempt can test it.\n- claim: fig9b-similar-maximum\n  outcome: blocked\n  blocked_by: too_large\n  notes: Not run; it needs the classifier of fig9a-optimal-resolution at each classifier's optimum\n    (see that claim's notes for the estimate).\n- claim: fig9b-accumulation-rate\n  outcome: blocked\n  blocked_by: too_large\n  notes: Not run; it needs the performance curves of fig9b-similar-maximum, from the classifier of\n    fig9a-optimal-resolution (see that claim's notes for the estimate).\n- claim: fig9c-time-averaged-worse\n  outcome: blocked\n  blocked_by: too_large\n  notes: Not run; it needs the classifier of fig9a-optimal-resolution and a time-averaged variant\n    (see that claim's notes for the estimate).\n- claim: fig9e-category-specific\n  outcome: blocked\n  blocked_by: too_large\n  notes: Not run; it needs the per-category results of the classifier of fig9a-optimal-resolution\n    (see that claim's notes for the estimate).\n- claim: fig9-spectrum-classifier-lower\n  outcome: blocked\n  blocked_by: too_large\n  notes: Not run; it needs the spectrum classifier at ten resolutions and the correlation classifiers\n    of fig9a-optimal-resolution (see that claim's notes for the estimate).\n- claim: fig10-vocalization-background\n  outcome: blocked\n  blocked_by: too_large\n  notes: Not run; it needs the classifier of fig9a-optimal-resolution in a two-class task (see that\n    claim's notes for the estimate).\nfindings:\n- kind: metadata_error\n  statement: The aMUA rasters are sampled at 2034.5 Hz (12207.03 Hz divided by 6, the Fs field of\n    every file), where the paper states 2 kHz; 6104 samples per trial make the stated 3 s only at the\n    files' rate. The data description gives no rate.\n- kind: data_missing\n  statement: The data set holds only the aMUA rasters to the natural sounds. The tone-pip recordings\n    and best frequencies behind Fig 1A and S5 Fig, and the raw voltage traces behind the thresholded\n    MUA of S10 Fig, are not deposited, so those analyses cannot be repeated.\n- kind: metadata_insufficient\n  statement: The order of the 16 channels along the probe (which end is dorsal, low frequency) is not\n    documented, so the channels cannot be assigned to frequencies, and the Param.RecordDate field\n    holds values such as May2019 and May2019C2 without explanation.\n- kind: metadata_error\n  statement: P2_Site08 has 13 trials per sound, where the paper states one paradigm 2 site with 14\n    trials and all others with 20. The other trial and site counts match the paper (paradigm 1 18 to\n    39 trials, 13 sites, 4 and 9 per animal; paradigms 2 and 3 11 sites each, 3 and 8 per animal).\n- kind: metadata_error\n  statement: The data description says all sound files are double precision WAV; the 195 model\n    sounds are 16 bit integer PCM and the paradigm sounds 32 bit float. The model sounds' SD is 0.0003\n    to 0.0022 of full scale, where the description says they are normalised to 0.001.\n- kind: other\n  about: data\n  statement: The whole data set is one 5.3 GB tar.gz file, which cannot be read at random; reading\n    any neural file means decompressing the stream from the start (about 4 minutes for the whole\n    file here). The white noise control of the model analyses is not included.\n- kind: code_mismatch\n  statement: The paper's model example code (ModelExample.m) builds the cochleogram with\n    criticalbandwidth.m, b = 94 + 71 f^1.5 (f in kHz), where the Methods give b = 25 + 75(1 +\n    1.4 f^2)^0.69, and it keeps the envelopes at 3675 Hz (oversampling factor 4) where the Methods\n    say 1 kHz. The Methods are followed here.\n- kind: methods_unavailable\n  statement: For the authors. The neural classifier's Methods leave open how the 100 random time\n    samples enter a decision (each sample a decision, or log-likelihoods summed over the 100 samples\n    for one decision), how the number of PCs that \"maximize the classifier performance\" is chosen\n    (on the validation data or within the model data), and on which data the mixing coefficient a\n    is fitted. The per-sound result of S6 Fig holds only when each sample is a decision, and the\n    median a of S9 Fig changes from 0.0 to 0.9 with these choices. Which rules were used?\n- kind: methods_unavailable\n  statement: For the authors. The CDI of Fig 6C matches the reported values only when the norms are\n    not squared (speech 0.123 against 0.12), while the Methods' prose (variance normalised by power)\n    reads as squared norms, which give values ten times smaller. The SI of Fig 7I under either\n    squared reading gives higher values than reported (environmental 0.72 against 0.49). Which\n    forms of the SI and CDI were used?\n"
}
```

```
File created successfully at: attempts/sadeghi-2019-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u; python tools/entry.py check entries/sadeghi-2019 2>&1 | tail -5; ls tools | head -40; grep -n "def cmd\|add_parser\|'check'" tools/entry.py | head
```

```
Fri Nov 13 23:18:14 UTC 2026
0 error(s)
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
contributors.py
conversion_issue.py
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
ls tools | sed -n 40,80p; grep -ln "attempt.schema" tools/*.py | head
```

```
tools/build_site.py
```

**Agent calls Bash**

```bash
ls tests | head; grep -rln "attempts/" tests/*.py 2>/dev/null | head -3; cd $TMPDIR && . dev/bin/activate && uv pip install -q jsonschema pyyaml && python - <<'EOF'
import json, yaml, jsonschema, re
s=json.load(open('schemas/attempt.schema.json'))
a=yaml.safe_load(open('attempts/sadeghi-2019-01.yaml'))
v=jsonschema.Draft202012Validator(s) if '2020' in s.get('$schema','') else jsonschema.Draft7Validator(s)
errs=list(v.iter_errors(a)); print(len(errs)); [print(e.message[:200], list(e.path)) for e in errs[:10]]
c=yaml.safe_load(open('claims/sadeghi-2019.yaml'))
ids=[x['id'] for x in c['claims']]; got=[o['claim'] for o in a['outcomes']]
print(set(ids)-set(got), set(got)-set(ids), len(ids), len(got))
for o in a['outcomes']:
    cl=[x for x in c['claims'] if x['id']==o['claim']][0]
    if 'expected' in cl and o['outcome']!='blocked':
        m=o.get('measured'); n=1 if not isinstance(m,list) else len(m)
        if n!=len(cl['expected']): print('count mismatch', o['claim'], n, len(cl['expected']))
txt=open('attempts/sadeghi-2019-01.yaml').read()
print('emdash', '—' in txt, 'rather' in txt.lower())
EOF
```

```
test_agent_run.py
test_build_site.py
test_build_targets.py
test_claims_check.py
test_datasets.py
test_encore.py
test_entry_tool.py
test_flagged.py
test_notify.py
test_paper_match.py
tests/test_agent_run.py
tests/test_encore.py
0
set() set() 28 28
emdash False False
Shell cwd was reset to
```

**Agent**

Record is schema-valid and covers all 28 claims. Checking prose rules in the entry, then the handover:

**Agent calls Bash**

```bash
grep -l "—" entries/sadeghi-2019/* attempts/sadeghi-2019-01.yaml; grep -il "rather" entries/sadeghi-2019/*.ipynb entries/sadeghi-2019/*.py entries/sadeghi-2019/README.md; grep -o '\*\*[^R][^*]*\*\*' entries/sadeghi-2019/*.ipynb entries/sadeghi-2019/README.md | head; python tools/entry.py handover entries/sadeghi-2019 2>&1 | tail -5; ls executed/sadeghi-2019/handover; date -u
```

```
grep: entries/sadeghi-2019/__pycache__: Is a directory
entries/sadeghi-2019/reproduce_sadeghi_2019_neural.ipynb:** 2).sum() / (sp_n **
entries/sadeghi-2019/reproduce_sadeghi_2019_neural.ipynb:** 2).sum() / (te_n **
wrote executed/sadeghi-2019/handover
model.py
reproduce_sadeghi_2019_model.ipynb
reproduce_sadeghi_2019_neural.ipynb
sadeghi-2019.yaml
sadeghi.py
Fri Nov 13 23:18:46 UTC 2026
```

**Agent calls Bash**

```bash
rm -rf entries/sadeghi-2019/__pycache__; grep -c "Result:" executed/sadeghi-2019/handover/*.ipynb; grep -c "## Summary" executed/sadeghi-2019/handover/*.ipynb; git status --short | head
```

```
executed/sadeghi-2019/handover/reproduce_sadeghi_2019_model.ipynb:0
executed/sadeghi-2019/handover/reproduce_sadeghi_2019_neural.ipynb:0
executed/sadeghi-2019/handover/reproduce_sadeghi_2019_model.ipynb:0
executed/sadeghi-2019/handover/reproduce_sadeghi_2019_neural.ipynb:0
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
```

**Agent**

I did steps 1 to 6 of the Author section for sadeghi-2019 on CRCNS bst-2. Both notebooks pass `tools/entry.py all` (neural 33 min, model 15 min), and the handover is built in `executed/sadeghi-2019/handover/`. Nothing is committed.

**One caveat first.** After the last run I reworded one conclusion cell in the model notebook (the cost-estimate result) and did not re-run. Its timings change with the machine (56 to 130 min in one run, 63 to 152 in the next), so the old wording quoted numbers the latest output does not show. The new wording relies only on what the cell prints. The executed copy still has the old wording and its stamp is stale, so the next run will execute the entry again. The handover strips conclusions, so the verifier's first round is unaffected.

**1. Outcomes (28 claims)**

| Claim | Outcome |
|---|---|
| fig1k-example-temporal-widths | reproduced (10 of 11 values under the paper code's first-half window; 6 to 8 under the claims file's two windows) |
| fig1-snr-noise-stronger | partially reproduced (means match, range bounds do not) |
| fig1-s5-model-predicts-neural | blocked, data_missing (no best frequencies) |
| fig2-noise-restricted | reproduced |
| fig3a-example-tonotopy-removal | partially reproduced (drop of 20 to 40 points; values outside tolerance) |
| fig3a-example-classifier-order | partially reproduced |
| fig3b-population-above-chance | reproduced |
| figs6-per-sound-above-chance | reproduced (only when each time sample is one decision) |
| figs9-mixing-coefficient | reproduced, under 1 of many reading combinations |
| figs10-amua-tmua | blocked, data_missing (no raw voltage) |
| fig4-example-original-vs-equalized | not reproduced (temporal r 0.90 against 0.72) |
| fig4e-population-original-vs-equalized | not reproduced |
| fig4f-example-equalized-classification | partially reproduced |
| fig4h-population-equalized-classification | partially reproduced |
| fig8b, fig8e, fig8f (paradigm 3) | reproduced |
| fig5, fig6 (model widths) | reproduced |
| fig6c-category-diversity | reproduced (only with norms not squared) |
| fig7i-stationarity | not reproduced (the order holds, the values do not) |
| fig9a, fig9b (two claims), fig9c, fig9e, fig9-spectrum, fig10 | blocked, too_large |

The seven model classifier claims were not run. The notebook's cost cell estimates 56 to 152 minutes for the classifier, and writing and running it did not fit the time left in this run.

**2. Dataset, assumptions and questions**
- The files' sampling rate is 2034.5 Hz, not the 2 kHz the paper states.
- There are no tone-pip recordings (so no best frequencies) and no raw voltage traces.
- The channel order along the probe is undocumented.
- P2_Site08 has 13 trials where the paper states 14.
- The model WAVs are 16-bit integer, not the double precision the description says; white noise is not included.
- Otherwise the site, animal and trial counts match the paper, no recording is deposited twice, and every raster is locked to the trial start.
- The paper's own code disagrees with its Methods on the cochlear filter bandwidths and the envelope sampling rate; I followed the Methods.
- No outcome rests on an assumption: every open detail was run under all readings the claims file names, or taken from the paper's code.
- Two questions for the paper's authors are recorded as `methods_unavailable` findings:
  - How the 100 time samples enter a decision, how the number of principal components is chosen, and on which data the mixing coefficient is fitted.
  - Which forms of the stationarity and category diversity indices were used.
- I asked no questions of a reader.

**3. Where the protocol was unclear, wrong or missing something**
1. `docs/archives.md` assumes zip files; bst-2 is a single 5.3 GB tar.gz that cannot be read at random. I streamed it once from the start with `tarfile` (about 4 min per pass), parsing each member in memory.
2. "Develop on a subset" costs a full stream pass whenever the wanted file is late in the archive, and caching to disk is not allowed. I accepted the streaming time on each development run.
3. "Reproduced under one reading" combined with many crossed readings makes weak matches count (figs9 matches in 1 of 32 combinations). The protocol says nothing about this; I reported the fragility in the notes.
4. The claims file lets the author follow the paper's code, but the code's window for Fig 1 is not one of the criterion's listed readings. I adopted the code's window and showed the listed readings as variants.
5. A criterion with no rule for partial reproduction (fig7i) conflicts with the protocol's general definition of partially reproduced. I followed the criterion: not reproduced.
6. `too_large` is defined by compute against limits; here the binding limit was the author's remaining time to build and run the analysis. I used "over the time left" and stated the measured estimate.
7. A conclusion quoting timing numbers cannot stay backed across runs. I reworded it after the last run (see the caveat above).
8. CRCNS is unversioned and the bucket object was modified in 2026, after the 2019 description. I recorded the MD5 sums from `checksums.md5`.

**4. Runtime and failures**
The session took about 3 h 30 min (19:48 to 23:19 UTC). Nothing failed in the final runs; peak memory was 3.6 GB.

## End of run

77 turns, 206 minutes, $8.60 at API prices, result: success.
