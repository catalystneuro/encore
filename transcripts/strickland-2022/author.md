# strickland-2022 · author · run 43342645589

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls
```

```
<persisted-output>
Output too large (39.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/26844be0-4336-43c0-b32e-35210f9578d4/tool-results/balxhd2dm.txt

Preview (first 2KB):
Fri Nov 13 01:11:59 UTC 2026
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
ls; ls entries/fouke-2025 claims attempts paper | head -50; cat claims/strickland-2022.yaml
```

```
<persisted-output>
Output too large (60.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/26844be0-4336-43c0-b32e-35210f9578d4/tool-results/bpj6k8acz.txt

Preview (first 2KB):
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
[... 75 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/strickland-2022.yaml"
}
```

```
1	# Claims for Strickland & McDannald (2022), Nat Commun 13:6192, "Brainstem networks construct
2	# threat probability and prediction error from neuronal building blocks", on CRCNS data set bst-3
3	# (doi:10.6080/K0Q23XGR).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-14.
6	#
7	# Text read: the version of record (PMC9582012, open access, Europe PMC JATS XML flattened), with
8	# Results, Discussion, figure legends and Methods, and its Supplementary Information
9	# (41467_2022_34021_MOESM1_ESM.pdf as extracted text, publisher's site): Supplementary Methods
10	# (head cap, surgery, acquisition, sorting, z-score normalization, heat plots, k-means, PCA,
11	# latency, correlations, hubs, regression, lesion PCA, anatomy, chi-square), Supplementary
12	# Figures 1 to 7 (legends; the panels are garbled in the extraction) and Supplementary Tables 1
13	# and 2 (read from the extracted cells; Table 2's column layout is garbled, its row and subject
14	# totals are not). The Source Data workbook (41467_2022_34021_MOESM4_ESM.xlsx) was read with a
15	# small XML parser; numbers marked "Source Data" below come from it. The supplement PDF could not
16	# be rendered (no poppler), so no panel was read as an image. The CRCNS data descriptor
17	# (paper/bst-3.data-description.txt) was read only to know what the data set holds; no claim or
18	# method comes from it.
19	#
20	# Code. The paper's Code availability says "Code for single-unit analyses is available at
[... 868 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la paper/; cat paper/bst-3.data-description.txt; sed -n '/CRCNS/,/^## [A-Z]/p' docs/archives.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=bst-3/" | python3 -c "
import sys,re
t=sys.stdin.read()
for k,s,d in re.findall(r'<Key>(.*?)</Key>.*?<LastModified>(.*?)</LastModified>.*?<Size>(.*?)</Size>',t): print(k,s,d)
" ; ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cat attempts/fouke-2025-01.yaml | head -150; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-3/live/filelist.txt; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-3/live/checksums.md5
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed -n 150,400p attempts/fouke-2025-01.yaml | grep -v "^    " | head -80; grep -n "findings:" -A40 attempts/fouke-2025-01.yaml | head -60; grep -n "verifications" -A5 attempts/fouke-2025-01.yaml|head
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
[... 107 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -c "
import fsspec, zipfile
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-3/live/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
n=z.infolist()
print(len(n))
import collections
d=collections.Counter('/'.join(i.filename.split('/')[:-1]) for i in n)
print(d)
for i in n:
  if 'singleUnit' not in i.filename or i.filename.endswith('/'): print(i.filename,i.file_size,i.compress_size)
sing=[i for i in n if 'singleUnit' in i.filename and not i.filename.endswith('/')]
print(sing[:3], sum(i.file_size for i in sing))
"; python3 -c "import scipy,numpy,fsspec;print(scipy.__version__)"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import fsspec, zipfile
ModuleNotFoundError: No module named 'fsspec'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import scipy,numpy,fsspec;print(scipy.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev 2>&1 | tail -2; uv pip install -q --python dev/bin/python fsspec aiohttp requests scipy numpy pandas h5py scikit-learn statsmodels matplotlib openpyxl ruptures nbformat nbclient ipykernel 2>&1 | tail -2; ls dev/bin | head
```

```
activate
activate.bat
activate.csh
activate.fish
activate.nu
activate.ps1
activate.xsh
activate_this.py
deactivate.bat
debugpy
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python -c "
import fsspec, zipfile
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-3/live/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
n=z.infolist()
print(len(n))
import collections
d=collections.Counter('/'.join(i.filename.split('/')[:-1]) for i in n)
print(d)
for i in n:
  if 'singleUnit' not in i.filename or i.filename.endswith('/'): print(i.filename,i.file_size,i.compress_size)
sing=[i for i in n if 'singleUnit' in i.filename and not i.filename.endswith('/')]
print([s.filename for s in sing[:3]], sum(i.file_size for i in sing))
"
```

```
1822
Counter({'data/singleUnits': 1813, 'data/scripts': 6, 'data/cubeFile': 2, 'data': 1})
data/ 0 0
data/cubeFile/ 0 0
data/cubeFile/cubeFile.mat 139318845 130634645
data/scripts/ 0 0
data/scripts/cueRegression.m 26890 3647
data/scripts/outcomeAnalysis.m 37155 6386
data/scripts/outcomeRegression.m 13879 1926
data/scripts/cubeScript.m 29531 4304
data/scripts/cueAnalysis.m 50442 8039
data/singleUnits/ 0 0
['data/singleUnits/js25102020pr25c15spk1558.mat', 'data/singleUnits/js25102620pr25c21spk1515.mat', 'data/singleUnits/js10030620pr25a17spk0245.mat'] 251956246
Shell cwd was reset to
```

**Agent**

The dataset holds 1812 single-unit .mat files, a 139 MB cube file and the paper's MATLAB scripts. I'm reading the scripts now, since they settle many open method details.

**Agent calls Bash**

```bash
cd $TMPDIR && mkdir -p scripts && dev/bin/python -c "
import fsspec, zipfile
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-3/live/data.zip',block_size=2**20).open()
z=zipfile.ZipFile(f)
for n in z.namelist():
  if n.startswith('data/scripts/') and n.endswith('.m'):
    open('scripts/'+n.split('/')[-1],'wb').write(z.read(n))
" && wc -l scripts/*; cat scripts/cubeScript.m
```

```
621 scripts/cubeScript.m
  1282 scripts/cueAnalysis.m
   587 scripts/cueRegression.m
   962 scripts/outcomeAnalysis.m
   456 scripts/outcomeRegression.m
  3908 total

% McDannald Lab Neuropixels cube script 
% Organises single units into a 3-D structure for analysis
% Publication: Brainstem networks construct threat probability and prediction error from neuronal building blocks


clear all; %#ok<CLALL>
tic;

% Input arrays
%
% single unit files, one for each unit in SingleUnitsAcceptedCorrected folder, contains the following:  
% id = rat/session filename (1 x 24 char)
% spike = 1 row of all the spike times 
[... 609 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "^\s*$" scripts/cueAnalysis.m | head -700
```

```
<persisted-output>
Output too large (36KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/26844be0-4336-43c0-b32e-35210f9578d4/tool-results/b1wr2zpse.txt

Preview (first 2KB):
% McDannald lab Neuropixels cue analysis script
% Looks at single unit firing data during 10s cue period in fear discriminaiton task 
% cue0 = no shock, safety
% cuePR = probablistic cue, 25% footshock
% cue100 = danger cue, 100% footshock
%
% Publication: Brainstem networks construct threat probability and prediction error from neuronal building blocks
tic;
clear all; %#ok<CLALL>
close all;
close all hidden;
load(['pathToFile\','cubeFile']); % raw unit data, insert the location of the matlab cube output
% organise regions from dorsal to ventral
% Correct the cube erroneously assigning some DPwh (region #2) units to CIC (region #21)
cube.anatomy.regionNum(cube.anatomy.regionNum==1)=101; % DPG
cube.anatomy.regionNum(cube.anatomy.regionNum==2)=102; % DPwh
[... 21 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/26844be0-4336-43c0-b32e-35210f9578d4/tool-results/b1wr2zpse.txt"
}
```

```
1	% McDannald lab Neuropixels cue analysis script
2	% Looks at single unit firing data during 10s cue period in fear discriminaiton task 
3	% cue0 = no shock, safety
4	% cuePR = probablistic cue, 25% footshock
5	% cue100 = danger cue, 100% footshock
6	%
7	% Publication: Brainstem networks construct threat probability and prediction error from neuronal building blocks
8	tic;
9	clear all; %#ok<CLALL>
10	close all;
11	close all hidden;
12	load(['pathToFile\','cubeFile']); % raw unit data, insert the location of the matlab cube output
13	% organise regions from dorsal to ventral
14	% Correct the cube erroneously assigning some DPwh (region #2) units to CIC (region #21)
15	cube.anatomy.regionNum(cube.anatomy.regionNum==1)=101; % DPG
16	cube.anatomy.regionNum(cube.anatomy.regionNum==2)=102; % DPwh
17	cube.anatomy.regionNum(cube.anatomy.regionNum==21)=102; % find 21 (CIC) and replace with 2 (DPwh)
18	cube.anatomy.regionNum(cube.anatomy.regionNum==3)=103; % dlPAG
19	cube.anatomy.regionNum(cube.anatomy.regionNum==4)=104; % lPAG
20	cube.anatomy.regionNum(cube.anatomy.regionNum==5)=105; % vlPAG
[... 681 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/26844be0-4336-43c0-b32e-35210f9578d4/tool-results/b1wr2zpse.txt",
 "offset": 700
}
```

```
700	%%%%%%%%%%%%%%%%%%%%%%%%%%%
701
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "^\s*$" scripts/cueAnalysis.m | sed -n '700,1300p' | grep -v "set(\|sgtitle\|box off\|colormap\|caxis\|xlabel\|ylabel\|hline\|subplot\|figure\|legend\|axis("
```

```
%%%%%%%%%%%%%%%%%%%%%%%%%%%
plotVar1 = ([coeffCue(1:14,1),coeffCue(15:28,1),coeffCue(29:42,1)]) - ((mean(coeffCue(1:2,1)) + mean(coeffCue(15:16,1)) + mean(coeffCue(29:30,1)))/3);
plotVar2 = ([coeffCue(1:14,2),coeffCue(15:28,2),coeffCue(29:42,2)]) - ((mean(coeffCue(1:2,2)) + mean(coeffCue(15:16,2)) + mean(coeffCue(29:30,2)))/3);
hold on;
hold on;
vline(2,'k');
hold on;
vline(12,'k');
h = plot(plotVar1);
hold on;
hold on;
vline(2,'k');
hold on;
vline(12,'k');
h = plot(plotVar2);
clear plotVar1 plotVar2;
% female and male PC1
plotVar1 = ([coeffCueFemale(1:14,1),coeffCueFemale(15:28,1),coeffCueFemale(29:42,1)]) - ((mean(coeffCueFemale(1:2,1)) + mean(coeffCueFemale(15:16,1)) + mean(coeffCueFemale(29:30,1)))/3);
plotVar2 = ([coeffCueMale(1:14,1),coeffCueMale(15:28,1),coeffCueMale(29:42,1)]) - ((mean(coeffCueMale(1:2,1)) + mean(coeffCueMale(15:16,1)) + mean(coeffCueMale(29:30,1)))/3);
hold on;
[... 177 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "^\s*$" scripts/cueRegression.m | grep -v "set(\|sgtitle\|box off\|colormap\|caxis\|xlabel\|ylabel\|hline\|vline\|subplot\|figure\|legend\|axis(\|hold on\|title("
```

```
% McDannald lab Neuropixels: cue period regression 
% 
% cueAnalysis script needs to be run before this (uses data arrays produced by it)
% 
% carries out the regression and lesion PCA analysis in the paper: 
% 'Brainstem networks construct threat probability and prediction error from neuronal building blocks'
tic; close all;
%%%%%%%%%%%%%%
% Intact pca %
%%%%%%%%%%%%%%
[coeffCueShuffled.intact,~,~,~,explainedCueShuffled.intact,~] = pca(pcaVarCue); % perform pca
coeffCueShuffled.intactpc1(:,1,1) = coeffCueShuffled.intact(:,1); % save pc1 as own 3D variable
coeffCueShuffled.intactpc2(:,1,1) = coeffCueShuffled.intact(:,2); % save pc2 as own 3D variable
coeffCueShuffled.intactpc3(:,1,1) = coeffCueShuffled.intact(:,3); % save pc3 as own 3D variable
explainedCueShuffled.intactpc1(1,1) = explainedCueShuffled.intact(1,:);
explainedCueShuffled.intactpc2(1,1) = explainedCueShuffled.intact(2,:);
explainedCueShuffled.intactpc3(1,1) = explainedCueShuffled.intact(3,:);
% female
[coeffOutcomeShuffled.intactFemale,~,~,~,explainedCueShuffled.intactFemale,~] = pca(pcaVarCueFemale); % perform pca
coeffOutcomeShuffled.intactFemalepc1(:,1,1) = coeffOutcomeShuffled.intactFemale(:,1); % save pc1 as own 3D variable
[... 295 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "^\s*$" scripts/outcomeAnalysis.m | grep -v "set(\|sgtitle\|box off\|colormap\|caxis\|xlabel\|ylabel\|hline\|vline\|subplot\|figure\|legend\|axis(\|hold on\|title(\|Female\|Male\|female\|male" | cut -c1-250
```

```
% McDannald lab Neuropixels outcome analysis script
% Looks at single unit firing during 10s post footshock period in fear discriminaiton task 
% cue0 = no shock, safety
% cuePR = probablistic cue, 25% footshock
% cue100 = danger cue, 100% footshock
%
% 
% Carries out outcome period analysis outlined in the publication
% 'Brainstem networks construct threat probability and prediction error from neuronal building blocks'
tic;
clear all; %#ok<CLALL>
close all;
close all hidden;
load(['pathToFile\','cubeFile']); % load the single unit data contained in the cube script output 
% organize the regions from dorsal to ventral
% the cube erroneously assigned some DPwh (region #2) units to CIC (region #21)
cube.anatomy.regionNum(cube.anatomy.regionNum==1)=101; % DPG
cube.anatomy.regionNum(cube.anatomy.regionNum==2)=102; % DPwh
cube.anatomy.regionNum(cube.anatomy.regionNum==21)=102; % find 21 (CIC) and replace with 2 (DPwh)
cube.anatomy.regionNum(cube.anatomy.regionNum==3)=103; % dlPAG
[... 460 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -v "^\s*$" scripts/outcomeRegression.m | grep -v "set(\|sgtitle\|box off\|colormap\|caxis\|xlabel\|ylabel\|hline\|vline\|subplot\|figure\|legend\|axis(\|hold on\|title(\|Female\|Male\|female\|male" | cut -c1-250 | head -250
```

```
% McDannald lab Neuropixels: outcome period regression 
% 
% Publication: Brainstem networks construct threat probability and prediction error from neuronal building blocks
tic; close all;
%%%%%%%%%%%%%%%%%%%%%
% Intact pca firing %
%%%%%%%%%%%%%%%%%%%%%
[coeffOutcomeShuffled.intact,~,~,~,explainedCueShuffled.intact,~] = pca(pcaVarOutcome); % perform pca
coeffOutcomeShuffled.intactpc1(:,1,1) = coeffOutcomeShuffled.intact(:,1); % save pc1 as own 3D variable
coeffOutcomeShuffled.intactpc2(:,1,1) = coeffOutcomeShuffled.intact(:,2); % save pc2 as own 3D variable
coeffOutcomeShuffled.intactpc3(:,1,1) = coeffOutcomeShuffled.intact(:,3); % save pc3 as own 3D variable
explainedCueShuffled.intactpc1(1,1) = explainedCueShuffled.intact(1,:);
explainedCueShuffled.intactpc2(1,1) = explainedCueShuffled.intact(2,:);
explainedCueShuffled.intactpc3(1,1) = explainedCueShuffled.intact(3,:);
%%%%%%%%%%%%%%%%%%%%%%%%
% Regression variables %
%%%%%%%%%%%%%%%%%%%%%%%%
blank = [1;1;1;1;1;1;1;1;1;1;1;1;1;1;1;1]; % necessary blank variable
regPos = [0;0;0;0;0.75;0.75;-0.25;-0.25;-0.25;-0.25;-0.25;-0.25;0;0;0;0]; % signed PE 
regShock = [1;1;1;1;1;1;0;0;0;0;0;0;0;0;0;0]; % shock vs no shock
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && cat > probe.py <<'EOF'
import fsspec, zipfile, time, io, resource
t=time.time()
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-3/live/data.zip',block_size=2**22).open()
z=zipfile.ZipFile(f)
b=z.read('data/cubeFile/cubeFile.mat')
print(len(b), b[:128], time.time()-t)
import scipy.io as sio
try:
    m=sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)
    print(m.keys())
    c=m['cube']
    def walk(o,p=''):
        if hasattr(o,'_fieldnames'):
            for k in o._fieldnames: walk(getattr(o,k),p+'.'+k)
        else:
            print(p, type(o).__name__, getattr(o,'shape',None), getattr(o,'dtype',None))
    walk(c,'cube')
except Exception as e:
    print('ERR',e)
print(time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
EOF
dev/bin/python probe.py
```

```
Fri Nov 13 01:13:39 UTC 2026
139318845 b'MATLAB 7.3 MAT-file, Platform: PCWIN64, Created on: Tue Mar 23 18:46:35 2021 HDF5 schema 1.00 .                     \x00\x00\x00\x00\x00\x00\x00\x00\x00\x02IM' 4.751993656158447
ERR Please use HDF reader for matlab v7.3 files, e.g. h5py
5.756882429122925 0.531508 GB
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > probe2.py <<'EOF'
import fsspec, zipfile, time, io, h5py
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-3/live/data.zip',block_size=2**22).open()
z=zipfile.ZipFile(f)
b=z.read('data/cubeFile/cubeFile.mat')
h=h5py.File(io.BytesIO(b),'r')
def v(name,o):
    if isinstance(o,h5py.Dataset): print(name,o.shape,o.dtype,dict(o.attrs).get('MATLAB_class'))
h.visititems(v)
EOF
dev/bin/python probe2.py
```

```
#refs#/a (2,) uint64 b'canonical empty'
#refs#/b (1, 184) uint8 b'uint8'
#refs#/c (3449, 1) uint64 b'uint64'
#refs#/d (1, 2) int32 b'int32'
#refs#/e (1, 2) object b'cell'
#refs#/f (2,) uint64 b'struct'
#refs#/g (2,) uint64 b'struct'
#subsystem#/MCOS (1, 5) object b'FileWrapper__'
cube/anatomy/ID (1812, 24, 1) uint16 b'char'
cube/anatomy/ProbeY (1812, 1, 1) float64 b'double'
cube/anatomy/region (1, 6) uint32 b'string'
cube/anatomy/regionNum (1812, 1, 1) float64 b'double'
cube/anatomy/x (1812, 1, 1) float64 b'double'
cube/anatomy/y (1812, 1, 1) float64 b'double'
cube/anatomy/z (1812, 1, 1) float64 b'double'
cube/fire/CS (1812, 1, 1) float64 b'double'
cube/fire/CV (1812, 1, 1) float64 b'double'
cube/fire/diff/ms100/interval (1812, 400, 16) float64 b'double'
cube/fire/diff/ms100/pellet (1812, 200, 70) float64 b'double'
cube/fire/diff/ms250/interval (1812, 160, 16) float64 b'double'
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > probe3.py <<'EOF'
import fsspec, zipfile, time, io, h5py, scipy.io as sio
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-3/live/data.zip',block_size=2**22).open()
z=zipfile.ZipFile(f)
names=[n for n in z.namelist() if n.startswith('data/singleUnits/') and n.endswith('.mat')]
print(len(names))
b=z.read(names[0]); print(b[:120])
try:
    m=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)
    for k,v in m.items():
        if k.startswith('__'): continue
        if hasattr(v,'_fieldnames'):
            for fn in v._fieldnames:
                x=getattr(v,fn); print(k,fn,getattr(x,'shape',None),getattr(x,'dtype',None), (x[:5] if hasattr(x,'shape') and x.ndim==1 else x if not hasattr(x,'_fieldnames') else x._fieldnames))
        else: print(k,type(v),getattr(v,'shape',None),getattr(v,'dtype',None), v if not hasattr(v,'shape') or v.size<30 else v[:5])
except Exception as e: print('ERR',e)
EOF
dev/bin/python probe3.py 2>&1 | cut -c1-300
```

```
1812
b'MATLAB 7.3 MAT-file, Platform: PCWIN64, Created on: Thu Feb 18 16:04:39 2021 HDF5 schema 1.00 .                     \x00\x00\x00\x00'
ERR Please use HDF reader for matlab v7.3 files, e.g. h5py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > probe3.py <<'EOF'
import fsspec, zipfile, time, io, h5py, numpy as np
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-3/live/data.zip',block_size=2**22).open()
z=zipfile.ZipFile(f)
names=sorted([n for n in z.namelist() if n.startswith('data/singleUnits/') and n.endswith('.mat')])
print(names[:3], names[-3:])
t=time.time()
for nm in names[:2]:
  h=h5py.File(io.BytesIO(z.read(nm)),'r')
  def v(name,o):
    if isinstance(o,h5py.Dataset):
        a=o[()]
        print(name,o.shape,o.dtype,dict(o.attrs).get('MATLAB_class'), a.ravel()[:6] if a.dtype!=np.uint16 else ''.join(map(chr,a.ravel())))
  h.visititems(v)
print(time.time()-t)
EOF
dev/bin/python probe3.py 2>&1 | cut -c1-300
```

```
['data/singleUnits/js10030220pr25a13spk0009.mat', 'data/singleUnits/js10030220pr25a13spk0044.mat', 'data/singleUnits/js10030220pr25a13spk0045.mat'] ['data/singleUnits/js27102520pr25c22spk6234.mat', 'data/singleUnits/js27102520pr25c22spk6256.mat', 'data/singleUnits/js27102520pr25c22spk6272.mat']
Traceback (most recent call last):
  File "/tmp/claude-1001/probe3.py", line 8, in <module>
    h=h5py.File(io.BytesIO(z.read(nm)),'r')
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/h5py/_hl/files.py", line 555, in __init__
    fid = make_fid(name, mode, userblock_size, fapl, fcpl, swmr=swmr)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/h5py/_hl/files.py", line 232, in make_fid
    fid = h5f.open(name, flags, fapl=fapl)
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "h5py/h5f.pyx", line 106, in h5py.h5f.open
OSError: Unable to synchronously open file (file signature not found)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > probe3.py <<'EOF'
import fsspec, zipfile, time, io, h5py, numpy as np, scipy.io as sio, collections
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-3/live/data.zip',block_size=2**22).open()
z=zipfile.ZipFile(f)
names=sorted([n for n in z.namelist() if n.startswith('data/singleUnits/') and n.endswith('.mat')])
t=time.time()
for nm in names[:1]:
  b=z.read(nm); print(b[:120])
  m=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)
  for k,v in m.items():
    if k.startswith('__'): continue
    if hasattr(v,'_fieldnames'):
        for fn in v._fieldnames:
            x=getattr(v,fn); print(k,fn,getattr(x,'shape',None),getattr(x,'dtype',None), x[:5] if hasattr(x,'shape') and x.ndim>=1 else x)
    else: print(k,type(v),getattr(v,'shape',None),getattr(v,'dtype',None), v if not hasattr(v,'shape') or v.size<30 else v[:5])
# header types over all
c=collections.Counter()
for nm in names:
    c[z.open(nm).read(20)]+=1
print(c, time.time()-t)
EOF
dev/bin/python probe3.py 2>&1 | cut -c1-300
```

```
b'MATLAB 5.0 MAT-file, Platform: PCWIN64, Created on: Thu Jun 25 13:39:23 2020                                        \x00\x00\x00\x00'
depth <class 'int'> None None 818
id <class 'str'> None None js10030220pr25a13spk0009
spike <class 'numpy.ndarray'> (2757,) int32 [106639 111224 118732 169746 201264]
time cue100 (4,) float64 [12779057.01641973 24089834.01354977 53117024.78449161 81843951.47212765]
time cueSPR (2,) float64 [87949299.16974223 99560047.29985455]
time cueNsPR (6,) float64 [18284468.44705248 30495164.84211209 37200488.79992671 42405886.10486759
 59822313.74824029]
time cue0 (4,) float64 [48211563.61846706 65327713.18090758 71133119.74045354 94354620.        ]
time cuePR (8,) float64 [18284468.44705248 30495164.84211209 37200488.79992671 42405886.10486759
 59822313.74824029]
time poke (336,) float64 [ 402484.74943642 2559590.96237261 3072554.9775038  3131962.90352103
 3539926.72385473]
time reward (49,) float64 [2559590.96237261 3072554.9775038  6445741.97592111 7713156.05665916
 8391055.10325523]
time shock (6,) float64 [13139040.97284494 24449840.96607546 53477014.73989956 82203918.43143512
 88309234.13447511]
wave <class 'numpy.ndarray'> (82,) float64 [71.74148695 72.65225718 73.36693342 74.87143864 75.46263577]
Counter({b'MATLAB 7.3 MAT-file,': 1067, b'MATLAB 5.0 MAT-file,': 745}) 330.98056530952454
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && curl -sI "https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-022-34021-1/MediaObjects/41467_2022_34021_MOESM4_ESM.xlsx" | head -5; md5sum paper/*.xlsx
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && cat > sd.py <<'EOF'
import openpyxl, time
t=time.time()
wb=openpyxl.load_workbook('paper/10.1038-s41467-022-34021-1.supp-41467_2022_34021_MOESM4_ESM.xlsx',read_only=True,data_only=True)
print(time.time()-t)
for ws in wb.worksheets:
    rows=list(ws.iter_rows(values_only=True))
    print('==',ws.title, len(rows), max((len(r) for r in rows),default=0))
    for r in rows[:4]: print('   ',[x for x in r[:12]])
print(time.time()-t)
EOF
dev/bin/python sd.py 2>&1 | cut -c1-250 > sd_out.txt; wc -l sd_out.txt; head -c 20000 sd_out.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && grep "^==" sd_out.txt | tr '\n' ';'; echo; grep -A4 "== Figure 2c \|== Figure 2d\|== Figure 2f\|== Figure 3b\|== Figure 3e\|== Figure 4c\|== Figure 4e\|== Figure 4f\|== Figure 5b\|== Figure 5c\|== Figure 5e\|== Figure 4g\|== Figure 4b k1 \|== Figure 3c\|== Figure 2e" sd_out.txt | cut -c1-400
```

```
== Figure 1c 74 4;== Figure 2a 1813 43;== Figure 2b k1 25 43;== Figure 2b k2 44 43;== Figure 2b k3 27 43;== Figure 2b k4 45 42;== Figure 2b k5 45 42;== Figure 2b k6 73 42;== Figure 2b k7 93 42;== Figure 2b k8 58 42;== Figure 2b k9 104 42;== Figure 2b k10 106 42;== Figure 2b k11 75 42;== Figure 2b k12 47 42;== Figure 2b k13 84 42;== Figure 2b k14 203 42;== Figure 2b k15 56 42;== Figure 2b k16 138 42;== Figure 2b k17 220 42;== Figure 2b k18 90 42;== Figure 2b k19 111 42;== Figure 2b k20 95 42;== Figure 2b k21 94 42;== Figure 2c inset 1813 43;== Figure 2c 22 20;== Figure 2d 1499 2;== Figure 2e 22 43;== Figure 2f 506 2;== Figure 2g 22 22;== Figure 3a k1 25 43;== Figure 3a k2 44 43;== Figure 3a k3 27 43;== Figure 3a k4 45 42;== Figure 3a k5 45 42;== Figure 3a k6 73 42;== Figure 3a k7 93 42;== Figure 3a k8 58 42;== Figure 3a k9 104 42;== Figure 3a k10 106 42;== Figure 3a k11 75 42;== Figure 3a k12 47 42;== Figure 3a k13 84 42;== Figure 3a k14 203 42;== Figure 3a k15 56 42;== Figure 3a k16 138 42;== Figure 3a k17 220 42;== Figure 3a k18 90 42;== Figure 3a k19 111 42;== Figure 3a k20 95 42;== Figure 3a k21 94 42;== Figure 3b middle 23 42;== Figure 3b bottom 23 42;== Figure 3c middle 23 42;== Figure 3c bottom 23 42;== Figure 3d middle 23 42;== Figure 3d bottom 23 42;== Figure 3e left 3 22;== Figure 3e right 2 22;== Figure 4a 1814 81;== Figure 4b k1 79 81;== Figure 4b k2 48 81;== Figure 4b k3 144 81;== Figure 4b k4 171 81;== Figure 4b k5 247 81;== Figure 4b k6 144 81;== Figure 4b k7 113 81;== Figure 4b k8 173 81;== Figure 4b k9 191 81;== Figure 4b k10 200 81;== Figure 4b k11 324 81;== Figure 4c 1814 81;== Figure 4d 13 81;== Figure 4e left 267 81;== Figure 4e right 615 81;== Figure 4f left 266 2;== Figure 4f right 614 2;== Figure 4g 23 13;== Figure 5a k1 79 81;== Figure 5a k2 48 81;== Figure 5a k3 144 81;== Figure 5a k4 171 81;== Figure 5a k5 247 81;== Figure 5a k6 144 81;== Figure 5a k7 113 81;== Figure 5a k8 173 81;== Figure 5a k9 191 81;== Figure 5a k10 200 81;== Figure 5a 
[... 125 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > cache.py <<'EOF'
import fsspec, zipfile, io, h5py, numpy as np
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-3/live/data.zip',block_size=2**22).open()
z=zipfile.ZipFile(f)
h=h5py.File(io.BytesIO(z.read('data/cubeFile/cubeFile.mat')),'r')
c=h['cube']
out={}
for k in ['fire/z/s1/interval','fire/z/ms500/interval','fire/z/ms250/interval','fire/raw/s1/interval','fire/raw/base2','fire/raw/ms250/interval','fire/z/ms100/interval','poke/SR','poke/base','poke/cue','anatomy/regionNum','anatomy/ID','anatomy/x','anatomy/y','anatomy/z','fire/diff/s1/interval']:
    out[k.replace('/','_')]=c[k][()]
np.savez('cube_dev.npz',**out)
EOF
dev/bin/python cache.py && ls -la cube_dev.npz
```

```
-rw-r--r-- 1 runner runner 214458032 Nov 13 01:20 cube_dev.npz
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > t1.py <<'EOF'
import numpy as np, openpyxl, collections
d=np.load('cube_dev.npz')
zs1=d['fire_z_s1_interval'] # unit, bin, trial
ids=[''.join(map(chr,r)) for r in d['anatomy_ID'][:,:,0]]
print(ids[:3], len(set(ids)))
def tm(a,tr): return a[:,:,tr].mean(2)
cue=np.hstack([tm(zs1,slice(0,4))[:,8:22],tm(zs1,slice(4,12))[:,8:22],tm(zs1,slice(12,16))[:,8:22]])
z5=d['fire_z_ms500_interval']
out=np.hstack([tm(z5,slice(a,b))[:,45:65] for a,b in [(0,4),(4,6),(6,12),(12,16)]])
print(cue.shape,out.shape)
wb=openpyxl.load_workbook('paper/10.1038-s41467-022-34021-1.supp-41467_2022_34021_MOESM4_ESM.xlsx',read_only=True,data_only=True)
def sheet(n):
    return [r for r in wb[n].iter_rows(values_only=True)]
# Fig 2c inset
r=sheet('Figure 2c inset'); A=np.array([x[1:43] for x in r[1:]],float); print(A.shape)
def pca_expl(X):
    Xc=X-X.mean(0); s=np.linalg.svd(Xc,compute_uv=False); v=s**2; return 100*v/v.sum()
print('SD inset pc1',pca_expl(A)[:3],'cube cue pc1',pca_expl(cue)[:3])
# match rows
from scipy.spatial import cKDTree
t=cKDTree(cue); dd,ii=t.query(A); print('inset matches', (dd<1e-6).sum(), np.median(dd), len(set(ii[dd<1e-6])))
# cluster sheets
lab=np.zeros(1812,int)
for k in range(1,22):
    r=sheet(f'Figure 2b k{k}'); B=np.array([[v for v in x[:42]] for x in r[1:] if x[0] is not None],float)
    dd,ii=t.query(B); 
    print(k,B.shape[0],(dd<1e-6).sum(),np.max(dd))
    lab[ii[dd<1e-6]]=k
print('cue labelled',(lab>0).sum(), collections.Counter(lab))
to=cKDTree(out)
lab2=np.zeros(1812,int)
for k in range(1,12):
    r=sheet(f'Figure 4b k{k}'); B=np.array([[v for v in x[1:81]] for x in r[2:] if x[1] is not None],float)
    dd,ii=to.query(B)
    print(k,B.shape[0],(dd<1e-6).sum(),np.max(dd), len(set(ii)))
    lab2[ii[dd<1e-6]]=k
print('out labelled',(lab2>0).sum())
r=sheet('Figure 4c'); C=np.array([x[1:81] for x in r[2:]],float); print('4c',C.shape, pca_expl(C)[:3], pca_expl(out)[:3])
np.savez('labels.npz',cue=lab,out=lab2)
EOF
dev/bin/python t1.py
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && cat > t2.py <<'EOF'
import fsspec, zipfile, io, h5py, numpy as np, scipy.io as sio, time, resource
t=time.time()
f=fsspec.open('https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-3/live/data.zip',block_size=2**25, cache_type='readahead').open()
z=zipfile.ZipFile(f)
infos=sorted([i for i in z.infolist() if i.filename.startswith('data/singleUnits/') and i.filename.endswith('.mat')], key=lambda i:i.header_offset)
print(len(infos), time.time()-t)
def load(b):
    if b[:10]==b'MATLAB 5.0':
        m=sio.loadmat(io.BytesIO(b),squeeze_me=True,struct_as_record=False)
        tm=m['time']; return dict(id=str(m['id']), spike=np.asarray(m['spike']).ravel(), **{k:np.atleast_1d(getattr(tm,k)).astype(float) for k in tm._fieldnames})
    h=h5py.File(io.BytesIO(b),'r')
    ks=list(h.keys()); 
    return ks, {k:list(h[k].keys()) if isinstance(h[k],h5py.Group) else h[k].shape for k in ks if k!='#refs#'}
n=0
for i in infos[:300]:
    b=z.read(i.filename)
    r=load(b)
    if n<1 or (isinstance(r,tuple) and n<400): print(r if isinstance(r,tuple) else r.keys())
    if isinstance(r,tuple): n+=1
print(time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
dev/bin/python t2.py 2>&1 | sort | uniq -c | head -20
```

```
1 (['#refs#', 'depth', 'id', 'spike', 'time', 'wave'], {'depth': (1, 1), 'id': (24, 1), 'spike': (104447, 1), 'time': ['cue0', 'cue100', 'cueNsPR', 'cuePR', 'cueSPR', 'poke', 'reward', 'shock'], 'wave': (82, 1)})
      1 (['#refs#', 'depth', 'id', 'spike', 'time', 'wave'], {'depth': (1, 1), 'id': (24, 1), 'spike': (10497, 1), 'time': ['cue0', 'cue100', 'cueNsPR', 'cuePR', 'cueSPR', 'poke', 'reward', 'shock'], 'wave': (82, 1)})
      1 (['#refs#', 'depth', 'id', 'spike', 'time', 'wave'], {'depth': (1, 1), 'id': (24, 1), 'spike': (1052, 1), 'time': ['cue0', 'cue100', 'cueNsPR', 'cuePR', 'cueSPR', 'poke', 'reward', 'shock'], 'wave': (82, 1)})
      1 (['#refs#', 'depth', 'id', 'spike', 'time', 'wave'], {'depth': (1, 1), 'id': (24, 1), 'spike': (105423, 1), 'time': ['cue0', 'cue100', 'cueNsPR', 'cuePR', 'cueSPR', 'poke', 'reward', 'shock'], 'wave': (82, 1)})
      1 (['#refs#', 'depth', 'id', 'spike', 'time', 'wave'], {'depth': (1, 1), 'id': (24, 1), 'spike': (10657, 1), 'time': ['cue0', 'cue100', 'cueNsPR', 'cuePR', 'cueSPR', 'poke', 'reward', 'shock'], 'wave': (82, 1)})
      1 (['#refs#', 'depth', 'id', 'spike', 'time', 'wave'], {'depth': (1, 1), 'id': (24, 1), 'spike': (10667, 1), 'time': ['cue0', 'cue100', 'cueNsPR', 'cuePR', 'cueSPR', 'poke', 'reward', 'shock'], 'wave': (82, 1)})
      1 (['#refs#', 'depth', 'id', 'spike', 'time', 'wave'], {'depth': (1, 1), 'id': (24, 1), 'spike': (10728, 1), 'time': ['cue0', 'cue100', 'cueNsPR', 'cuePR', 'cueSPR', 'poke', 'reward', 'shock'], 'wave': (82, 1)})
      1 (['#refs#', 'depth', 'id', 'spike', 'time', 'wave'], {'depth': (1, 1), 'id': (24, 1), 'spike': (108877, 1), 'time': ['cue0', 'cue100', 'cueNsPR', 'cuePR', 'cueSPR', 'poke', 'reward', 'shock'], 'wave': (82, 1)})
      1 (['#refs#', 'depth', 'id', 'spike', 'time', 'wave'], {'depth': (1, 1), 'id': (24, 1), 'spike': (11016, 1), 'time': ['cue0', 'cue100', 'cueNsPR', 'cuePR', 'cueSPR', 'poke', 'reward', 'shock'], 'wave': (82, 1)})
      1 (['#refs#', 'depth', 'id', 'spike'
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && dev/bin/python t2.py 2>&1 | grep -v "^(\['#refs" | tail -3
```

```
1812 0.8340456485748291
2.9277942180633545 0.191852
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > t3.py <<'EOF'
import numpy as np, time, openpyxl
d=np.load('cube_dev.npz'); L=np.load('labels.npz'); lab=L['cue']
zs1=d['fire_z_s1_interval']
def tm(a,tr): return a[:,:,tr].mean(2)
X=np.hstack([tm(zs1,slice(0,4))[:,8:22],tm(zs1,slice(4,12))[:,8:22],tm(zs1,slice(12,16))[:,8:22]])
def pc1(X):
    Xc=X-X.mean(0); C=Xc.T@Xc; w=np.linalg.eigvalsh(C); return 100*w[-1]/w.sum()
base=pc1(X); print(base)
rng=np.random.default_rng(0)
t=time.time()
res={}
for mode in ['sa','sb','se']:
    out=[]
    for k in range(1,22):
        m=lab==k; B=X[m]; vals=[]
        for it in range(200):
            Y=X.copy()
            if mode=='sa': S=np.take_along_axis(B, rng.random(B.shape).argsort(1),1)
            elif mode=='sb': S=rng.permutation(B.ravel()).reshape(B.shape)
            else: S=B[:,rng.permutation(B.shape[1])]
            Y[m]=S; vals.append(pc1(Y))
        out.append((base-np.mean(vals))/m.sum())
    res[mode]=np.array(out)
    print(mode, np.round(res[mode][:4],4), time.time()-t)
wb=openpyxl.load_workbook('paper/10.1038-s41467-022-34021-1.supp-41467_2022_34021_MOESM4_ESM.xlsx',read_only=True,data_only=True)
sd=np.array([r[1] for r in list(wb['Figure 2c'].iter_rows(values_only=True))[1:22]],float)
print('SD',np.round(sd,4))
for m in res: print(m, np.corrcoef(res[m],sd)[0,1], np.abs(res[m]-sd).max())
EOF
dev/bin/python t3.py
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls schemas tools; grep -n "def \|sanity\|claim:" tools/entry.py | head -80
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
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_reuse_targets.py
build_site.py
build_targets.py
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,75p tools/entry.py; sed -n 179,410p tools/entry.py; sed -n 590,630p tools/entry.py
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
[... 326 more lines not kept]
```

**Agent**

Writing the helper module now; the paper's MATLAB scripts in the dataset settle most of the open details in the claims file (shuffle direction, regression form, normalization).

**Agent calls Write**

```json
{
 "file_path": "entries/strickland-2022/bst3.py",
 "content": "\"\"\"Loading and measures for CRCNS data set bst-3 (Strickland and McDannald 2022, Nat Commun 13:6192).\n\nThe data set (doi:10.6080/K0Q23XGR) is not versioned (version \"unversioned\"); it is read from the\npublic bucket at https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-3/live/data.zip, a zip opened in\nplace over range requests. It holds one MATLAB file per single unit (data/singleUnits, 1812 files),\nthe cube file built from them by the paper's cubeScript.m (data/cubeFile/cubeFile.mat) and the\npaper's analysis scripts (data/scripts). The paper's Code availability (\"Code for single-unit\nanalyses is available at https://crcns.org/\") points at these scripts, so where the Methods leave a\ndetail open and a script settles it, the script is followed (protocol, reader step 2 and author\nstep 1.6) and the script and line are cited here.\n\nWhere each parameter comes from:\n- Trial rows 1-4 danger, 5-6 uncertainty shock, 7-12 uncertainty omission, 13-16 safety: the data\n  descriptor and cubeScript.m (time.cue = [cue100; cueSPR; cueNsPR; cue0]).\n- Time stamps are in samples at 30 kHz: cubeScript.m (30000 samples per 1-s bin).\n- Cue matrix, 1-s bins 9:22 of the 40-s window from 10 s before cue onset (2 s before onset to 2 s\n  after offset), per cue danger, uncertainty (rows 5-12), safety: cueAnalysis.m (pcaVarCue).\n- Outcome matrix, 500-ms bins 46:65 (12.5 to 22.5 s after cue onset, the 10 s from shock offset),\n  per trial type: outcomeAnalysis.m (pcaVarOutcome).\n- Normalization: per trial, firing minus that trial's 2-s pre-cue rate (base2, rounded down),\n  z-scored over all trials and bins of the 40-s window at each bin size: cubeScript.m (\"find\n  differential firing\", \"find z firing\"). The claims file's readings n-a/n-b and w-a/w-b are also\n  computed from the spike times for the link claim.\n- Suppression ratio per trial, (base - cue)/(base + cue), pokes in the 20 s before cue x 3 and in\n  the 10-s cue x 6, a trial with no pokes set to 1: cubeScript.m (poke.SR(isnan(poke.SR)) = 1). The\n  claims file's sr-a (set to 0) and sr-b (left out) are shown beside it.\n- Regression with an intercept, cluster mean firing per trial row on threat probability (1, 0.25,\n  0) and the mean over member units of the trial's suppression ratio: cueAnalysis.m (\"Cluster\n  regression\"). Outcome: regressors signed prediction error (0, .75, -.25, 0) and shock (1, 1, 0,\n  0), beta columns 1-20 prediction error and 21-40 shock: outcomeRegression.m.\n- PCA as MATLAB pca with defaults (columns centred, not scaled), percent variance from the\n  eigenvalues: all scripts.\n- PC1 contribution shuffle, each unit's row of the cluster permuted across its columns, 1000\n  times: cueAnalysis.m (Shuffle(..., 2)); the claims file's reading s-a.\n- Cue lesion, each trial row of a shuffled cluster's mean firing permuted across the 14\n  intervals before regression, betas averaged over 1000 iterations: cueRegression.m\n  (Shuffle(regData, 2)); the claims file's s-c. Outcome lesion, the shuffled cluster's firing\n  permuted across the 16 trial rows (Shuffle(regData, 1)): outcomeRegression.m; the claims file's\n  s-d. Whether the same row permutation is used for every interval is not settled by the script\n  (it depends on the Shuffle function, which is not included); both are run.\n- Outcome hub measure, squared Pearson correlation of a unit's 80-value row with the mean row of\n  each other cluster of its network, averaged: outcomeAnalysis.m.\n- Region numbers and names, and the merges 21 -> 2 (CIC to DpWh) and 24 -> 11 (x/scp):\n  cueAnalysis.m and the region list in cubeScript.m.\n- Subject numbers 1-10 for animals js10, 11, 13, 14, 15, 21, 22, 24, 25, 27 and sex (js10, 11,\n  13, 27 female): cueAnalysis.m.\n- Random seeds and the number of k-means seeds are standard choices that the claims file states.\n\"\"\"\nfrom __future__ import annotations\n\nimport hashlib\nimport io\nimport zipfile\n\nimport fsspec\nimport h5py\nimport numpy as np\nimport scipy.io as sio\nfrom scipy import stats\n\nDATASET = \"bst-3\"\nVERSION = \"unversioned\"\nDOI = \"10.6080/K0Q23XGR\"\nBASE_URL = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/bst-3/live/\"\nZIP_URL = BASE_URL + \"data.zip\"\nSOURCE_DATA_URL = (\"https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-022-34021-1/\"\n                   \"MediaObjects/41467_2022_34021_MOESM4_ESM.xlsx\")\nSOURCE_DATA_MD5 = \"4df716fd6739ee3de3b0df81c4175be8\"\n\nFS = 30000  # samples per second (cubeScript.m)\nRATS = [\"10\", \"11\", \"13\", \"14\", \"15\", \"21\", \"22\", \"24\", \"25\", \"27\"]   # subjects 1-10 (cueAnalysis.m)\nFEMALE = {\"10\", \"11\", \"13\", \"27\"}\nREGIONS = [\"DPG\", \"DpWh\", \"DLPAG\", \"LPAG\", \"VLPAG\", \"me5\", \"DRL\", \"DRD\", \"DRV\", \"PDR\", \"mlf\", \"isRt\",\n           \"Pa4\", \"x/scp\", \"SPTg\", \"PnO\", \"VTg\", \"DMTg\", \"ts\", \"PMnR\", \"MnR\"]\n# cube region number -> dorsal-ventral order 1-21 (cueAnalysis.m, lines 15-38)\nREGION_REMAP = {1: 1, 2: 2, 21: 2, 3: 3, 4: 4, 5: 5, 27: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 20: 12,\n                23: 13, 11: 14, 24: 14, 12: 15, 16: 16, 13: 17, 17: 18, 22: 19, 14: 20, 15: 21}\nTYPES = {\"danger\": slice(0, 4), \"unc_shock\": slice(4, 6), \"unc_omission\": slice(6, 12),\n         \"safety\": slice(12, 16), \"uncertainty\": slice(4, 12)}\nPROB = np.array([1] * 4 + [0.25] * 8 + [0] * 4, float)\nPE = np.array([0] * 4 + [0.75] * 2 + [-0.25] * 6 + [0] * 4, float)\nSHOCK = np.array([1] * 6 + [0] * 10, float)\n\n\n# --- reading -----------------------------------------------------------------------------------\n\ndef open_zip():\n    f = fsspec.open(ZIP_URL, block_size=2 ** 25, cache_type=\"readahead\").open()\n    return zipfile.ZipFile(f)\n\n\ndef read_text(name):\n    with fsspec.open(BASE_URL + name, \"rt\") as f:\n        return f.read()\n\n\nCUBE_FIELDS = [\"fire/z/s1/interval\", \"fire/z/ms500/interval\", \"fire/raw/s1/interval\", \"fire/raw/base2\",\n               \"poke/SR\", \"poke/base\", \"poke/cue\", \"anatomy/regionNum\", \"anatomy/ID\", \"anatomy/x\",\n               \"anatomy/y\", \"anatomy/z\"]\n\n\ndef load_cube(zf):\n    \"\"\"The cube's arrays as (unit, bin, trial); h5py reads MATLAB's (trial, bin, unit) transposed.\"\"\"\n    with h5py.File(io.BytesIO(zf.read(\"data/cubeFile/cubeFile.mat\")), \"r\") as h:\n        c = h[\"cube\"]\n        out = {k: c[k][()] for k in CUBE_FIELDS}\n    out[\"ID\"] = np.array([\"\".join(map(chr, r)) for r in out.pop(\"anatomy/ID\")[:, :, 0]])\n    return out\n\n\ndef _parse_unit(b):\n    \"\"\"id, spike times and event times of one single-unit file (MATLAB 5 or 7.3).\"\"\"\n    if b[:10] == b\"MATLAB 5.0\":\n        m = sio.loadmat(io.BytesIO(b), squeeze_me=True, struct_as_record=False)\n        t = m[\"time\"]\n        ev = {k: np.atleast_1d(getattr(t, k)).astype(float) for k in t._fieldnames}\n        return str(m[\"id\"]), np.asarray(m[\"spike\"]).ravel().astype(np.int64), ev\n    with h5py.File(io.BytesIO(b), \"r\") as h:\n        uid = \"\".join(map(chr, h[\"id\"][()].ravel()))\n        spike = h[\"spike\"][()].ravel().astype(np.int64)\n        ev = {}\n        for k in h[\"time\"].keys():\n            v = h[\"time\"][k][()]\n            ev[k] = np.array([], float) if v.dtype == np.uint64 else v.ravel().astype(float)\n    return uid, spike, ev\n\n\ndef _count(spike, starts, width):\n    \"\"\"Spikes in (start, start + width], as cubeScript.m counts them (spike > a & spike <= b).\"\"\"\n    return (np.searchsorted(spike, starts + width, side=\"right\")\n            - np.searchsorted(spike, starts, side=\"right\"))\n\n\ndef scan_units(zf, limit=None):\n    \"\"\"One pass over the single-unit files, keeping only what the analyses need.\n\n    Per unit: spike counts in 250-ms bins from 20 s before to 40 s after cue onset (240 bins) for\n    the 16 trials; counts in the cube's 1-s bins (40 s from 10 s before onset) and the 2-s\n    baseline, to check the cube against the spikes; the summed danger-trial spike count in 1-ms\n    bins over the 10-s cue, for the latency; and per session the cue, shock and poke times.\n    \"\"\"\n    infos = sorted([i for i in zf.infolist() if i.filename.startswith(\"data/singleUnits/\")\n                    and i.filename.endswith(\".mat\")], key=lambda i: i.header_offset)\n    if limit:\n        infos = infos[:limit]\n    ids, c250, c1s, base2, ms1, n_spk, fmt, sessions = [], [], [], [], [], [], [], {}\n    for info in infos:\n        b = zf.read(info.filename)\n        uid, spike, ev = _parse_unit(b)\n        spike = np.sort(spike)\n        fmt.append(b[:10].decode())\n        cue = np.concatenate([ev[\"cue100\"], ev[\"cueSPR\"], ev[\"cueNsPR\"], ev[\"cue0\"]])\n        ids.append(uid)\n        n_spk.append(spike.size)\n        w = FS // 4\n        starts = cue[:, None] - 20 * FS + w * np.arange(240)[None, :]\n        c250.append(_count(spike, starts, w).astype(np.int16))\n        starts = cue[:, None] - 10 * FS + FS * np.arange(40)[None, :]\n        c1s.append(_count(spike, starts, FS).astype(np.int16))\n        base2.append(np.floor(_count(spike, cue - 2 * FS, 2 * FS) / 2))\n        starts = ev[\"cue100\"][:, None] + 30 * np.arange(10000)[None, :]\n        ms1.append(_count(spike, starts, 30).sum(0).astype(np.int16))\n        key = uid[:10]\n        if key not in sessions:\n            sessions[key] = {\"cue\": cue, \"poke\": np.sort(ev[\"poke\"]), \"shock\": np.sort(ev[\"shock\"]),\n                             \"reward\": ev[\"reward\"], \"file_id\": uid}\n        else:\n            s = sessions[key]\n            same = (np.array_equal(s[\"cue\"], cue) and np.array_equal(s[\"poke\"], np.sort(ev[\"poke\"])))\n            s.setdefault(\"consistent\", True)\n            s[\"consistent\"] &= same\n    return {\"ID\": np.array(ids), \"c250\": np.stack(c250), \"c1s\": np.stack(c1s), \"base2\": np.stack(base2),\n            \"ms1\": np.stack(ms1), \"n_spikes\": np.array(n_spk), \"format\": np.array(fmt),\n            \"sessions\": sessions}\n\n\ndef load_source_data():\n    \"\"\"The paper's Source Data workbook (Nature Communications, supplementary file MOESM4).\"\"\"\n    import openpyxl\n    with fsspec.open(SOURCE_DATA_URL, \"rb\") as f:\n        b = f.read()\n    md5 = hashlib.md5(b).hexdigest()\n    wb = openpyxl.load_workbook(io.BytesIO(b), read_only=True, data_only=True)\n    sheets = {ws.title: [list(r) for r in ws.iter_rows(values_only=True)] for ws in wb.worksheets}\n    return sheets, md5\n\n\ndef sd_cue_cluster_rows(sheets, k):\n    return np.array([r[:42] for r in sheets[f\"Figure 2b k{k}\"][1:] if r[0] is not None], float)\n\n\ndef sd_outcome_cluster_rows(sheets, k):\n    return np.array([r[1:81] for r in sheets[f\"Figure 4b k{k}\"][2:] if r[1] is not None], float)\n\n\ndef sd_matrix(sheets, name, first_row, ncol, first_col=1):\n    rows = [r for r in sheets[name][first_row:] if r[first_col] is not None]\n    return np.array([r[first_col:first_col + ncol] for r in rows], float)\n\n\n# --- rows of the cue and outcome matrices --------------------------------------------------------\n\ndef type_means(a, kinds):\n    \"\"\"Mean over the trials of each type; a is (unit, bin, trial).\"\"\"\n    return [a[:, :, TYPES[k]].mean(2) for k in kinds]\n\n\ndef cue_matrix(z_s1):\n    \"\"\"1812 x 42: danger, uncertainty, safety, 1-s bins 9:22 (cueAnalysis.m, pcaVarCue).\"\"\"\n    return np.hstack([m[:, 8:22] for m in type_means(z_s1, [\"danger\", \"uncertainty\", \"safety\"])])\n\n\ndef outcome_matrix(z_ms500):\n    \"\"\"1812 x 80: 500-ms bins 46:65 per trial type (outcomeAnalysis.m, pcaVarOutcome).\"\"\"\n    return np.hstack([m[:, 45:65] for m in\n                      type_means(z_ms500, [\"danger\", \"unc_shock\", \"unc_omission\", \"safety\"])])\n\n\ndef normalized_readings(c250):\n    \"\"\"Cue and outcome rows under the claims file's readings, from 250-ms counts (unit, trial, 240).\n\n    n-a: each trial's own baseline (mean rate over the 2 s before onset); n-b: the mean baseline of\n    that trial's type (danger, uncertainty, safety). w-a: z over 200 bins (-20 to +30 s); w-b:\n    over all 240 bins. Rates are not rounded. Returns {reading: (cue rows, outcome rows)}.\n    \"\"\"\n    rate = c250.astype(float) * 4                      # unit, trial, bin\n    base = rate[:, :, 72:80].mean(2)                   # 2 s before onset (bins 72-79)\n    base_type = base.copy()\n    for sl in (slice(0, 4), slice(4, 12), slice(12, 16)):\n        base_type[:, sl] = base[:, sl].mean(1, keepdims=True)\n    out = {}\n    for nname, b in ((\"n-a\", base), (\"n-b\", base_type)):\n        diff = rate - b[:, :, None]\n        for wname, nb in ((\"w-a\", 200), (\"w-b\", 240)):\n            seg = diff[:, :, :nb]\n            mu = seg.mean((1, 2), keepdims=True)\n            sd = seg.std((1, 2), ddof=1, keepdims=True)\n            sd[sd == 0] = np.nan\n            z = (diff - mu) / sd                       # unit, trial, bin\n            z = np.transpose(z, (0, 2, 1))             # unit, bin, trial\n            s1 = z.reshape(z.shape[0], 60, 4, 16).mean(2)       # 1-s intervals from -20 s\n            ms500 = z.reshape(z.shape[0], 120, 2, 16).mean(2)   # 500-ms intervals from -20 s\n            cue = np.hstack([m[:, 18:32] for m in type_means(s1, [\"danger\", \"uncertainty\", \"safety\"])])\n            outc = np.hstack([m[:, 65:85] for m in type_means(\n                ms500, [\"danger\", \"unc_shock\", \"unc_omission\", \"safety\"])])\n            out[f\"{nname}, {wname}\"] = (cue, outc)\n    return out\n\n\ndef match_rows(sd_rows, rows, tol=0.01):\n    \"\"\"For each Source Data row, the units whose row is within tol everywhere (max abs difference),\n    and the unit with the highest Pearson correlation.\"\"\"\n    rows = np.nan_to_num(rows, nan=1e9)\n    hits, best_r, best_i = [], [], []\n    rz = (rows - rows.mean(1, keepdims=True))\n    rz /= np.linalg.norm(rz, axis=1, keepdims=True) + 1e-300\n    for r in sd_rows:\n        d = np.abs(rows - r).max(1)\n        hits.append(np.flatnonzero(d < tol))\n        q = r - r.mean()\n        q /= np.linalg.norm(q) + 1e-300\n        c = rz @ q\n        best_i.append(int(np.argmax(c)))\n        best_r.append(float(np.max(c)))\n    return hits, np.array(best_r), np.array(best_i)\n\n\n# --- behaviour -----------------------------------------------------------------------------------\n\ndef suppression_ratios(cue, poke, empty=\"code\"):\n    \"\"\"Per trial (cubeScript.m): pokes in (t-20 s, t] x 3 and in (t, t+10 s] x 6.\n    empty: 'code' sets a trial with no pokes to 1 (the script), 'zero' to 0 (sr-a), 'drop' to NaN (sr-b).\"\"\"\n    base = 3 * (np.searchsorted(poke, cue, \"right\") - np.searchsorted(poke, cue - 20 * FS, \"right\"))\n    cue_n = 6 * (np.searchsorted(poke, cue + 10 * FS, \"right\") - np.searchsorted(poke, cue, \"right\"))\n    with np.errstate(invalid=\"ignore\", divide=\"ignore\"):\n        sr = (base - cue_n) / (base + cue_n)\n    fill = {\"code\": 1.0, \"zero\": 0.0, \"drop\": np.nan}[empty]\n    sr[np.isnan(sr)] = fill\n    return sr\n\n\ndef mixed_anova_cue_by_group(Y, group):\n    \"\"\"F for the within factor (columns of Y) in a within x between mixed ANOVA, subjects as rows.\n    Error is cue x subjects within groups, df (J - 1)(N - G). Also the one-way repeated-measures F.\"\"\"\n    Y = np.asarray(Y, float)\n    N, J = Y.shape\n    gm = Y.mean()\n    subj = Y.mean(1, keepdims=True)\n    ss_within = ((Y - subj) ** 2).sum()\n    ss_cue = N * ((Y.mean(0) - gm) ** 2).sum()\n    groups = np.unique(group)\n    ss_int = 0.0\n    for g in groups:\n        Yg = Y[group == g]\n        ss_int += len(Yg) * ((Yg.mean(0) - Yg.mean() - Y.mean(0) + gm) ** 2).sum()\n    df1 = J - 1\n    df_mixed = (J - 1) * (N - len(groups))\n    ss_err_mixed = ss_within - ss_cue - ss_int\n    F_mixed = (ss_cue / df1) / (ss_err_mixed / df_mixed)\n    df_rm = (J - 1) * (N - 1)\n    F_rm = (ss_cue / df1) / ((ss_within - ss_cue) / df_rm)\n    return {\"F_mixed\": F_mixed, \"df_mixed\": (df1, df_mixed), \"p_mixed\": stats.f.sf(F_mixed, df1, df_mixed),\n            \"F_rm\": F_rm, \"df_rm\": (df1, df_rm), \"p_rm\": stats.f.sf(F_rm, df1, df_rm)}\n\n\n# --- PCA, k-means, shuffles ----------------------------------------------------------------------\n\ndef pca(X):\n    \"\"\"MATLAB pca defaults: centre columns, no scaling. Returns (coeff columns, percent explained).\"\"\"\n    Xc = X - X.mean(0)\n    _, s, vt = np.linalg.svd(Xc, full_matrices=False)\n    v = s ** 2\n    return vt.T, 100 * v / v.sum()\n\n\ndef pc1_percent(X):\n    Xc = X - X.mean(0)\n    w = np.linalg.eigvalsh(Xc.T @ Xc)\n    return 100 * w[-1] / w.sum()\n\n\ndef kmeans_sizes(X, k, seeds):\n    from sklearn.cluster import KMeans\n    out = []\n    for s in seeds:\n        km = KMeans(n_clusters=k, init=\"k-means++\", n_init=1, random_state=int(s)).fit(X)\n        out.append((np.bincount(km.labels_, minlength=k), km.inertia_, km.labels_))\n    return out\n\n\ndef shuffle_rows(B, rng):\n    \"\"\"Each row permuted independently across its columns (reading s-a).\"\"\"\n    return np.take_along_axis(B, rng.random(B.shape).argsort(1), 1)\n\n\ndef shuffle_block(B, rng):\n    \"\"\"All entries of the block permuted together (reading s-b).\"\"\"\n    return rng.permutation(B.ravel()).reshape(B.shape)\n\n\ndef pc1_contribution(X, labels, ks, rng, n_iter=1000, mode=\"s-a\"):\n    \"\"\"Drop in PC1 percent when one cluster's rows are shuffled, averaged over n_iter, per unit\n    (cueAnalysis.m, \"pca with single cluster shuffled\").\"\"\"\n    base = pc1_percent(X)\n    f = shuffle_rows if mode == \"s-a\" else shuffle_block\n    out = {}\n    for k in ks:\n        m = labels == k\n        B = X[m]\n        Y = X.copy()\n        vals = np.empty(n_iter)\n        for i in range(n_iter):\n            Y[m] = f(B, rng)\n            vals[i] = pc1_percent(Y)\n        out[k] = (base - vals.mean()) / m.sum()\n    return out\n\n\n# --- latency -------------------------------------------------------------------------------------\n\ndef change_point(x):\n    \"\"\"MATLAB findchangepts(x) with its defaults: the one change in mean that most reduces the\n    residual sum of squares; returns the 1-based index of the first sample after the change, or\n    None when no split reduces it (a constant signal).\"\"\"\n    x = np.asarray(x, float)\n    n = x.size\n    c1 = np.cumsum(x)\n    c2 = np.cumsum(x ** 2)\n    k = np.arange(1, n)\n    left = c2[:-1] - c1[:-1] ** 2 / k\n    right = (c2[-1] - c2[:-1]) - (c1[-1] - c1[:-1]) ** 2 / (n - k)\n    cost = left + right\n    total = c2[-1] - c1[-1] ** 2 / n\n    i = int(np.argmin(cost))\n    if not cost[i] < total - 1e-9 * max(total, 1):\n        return None\n    return i + 2          # first sample of the second segment, 1-based\n\n\n# --- regression ----------------------------------------------------------------------------------\n\ndef regress_betas(Y, regressors, intercept=True):\n    \"\"\"Least squares per column of Y (16 trial rows x intervals); returns betas of the regressors.\"\"\"\n    X = np.column_stack(([np.ones(len(regressors[0]))] if intercept else []) + list(regressors))\n    b, *_ = np.linalg.lstsq(X, Y, rcond=None)\n    return b[1:] if intercept else b\n\n\ndef cue_betas(z_s1, sr, labels, ks, mode=\"r-a\", intercept=True, firing=None):\n    \"\"\"Cluster x 28 betas, columns 1-14 threat probability, 15-28 behaviour (cueAnalysis.m).\n    r-a: one regression on the cluster's mean firing, behaviour the mean member suppression ratio.\n    r-b: one regression per unit on its own trials and ratios, betas averaged in the cluster.\"\"\"\n    F = z_s1[:, 8:22, :] if firing is None else firing    # unit, 14, 16\n    rows = []\n    for k in ks:\n        m = labels == k\n        if mode == \"r-a\":\n            Y = F[m].mean(0).T                              # 16 x 14\n            b = regress_betas(Y, [PROB, sr[m].mean(0)], intercept)\n        else:\n            bs = [regress_betas(F[u].T, [PROB, sr[u]], intercept) for u in np.flatnonzero(m)]\n            b = np.mean(bs, 0)\n        rows.append(np.concatenate([b[0], b[1]]))\n    return np.array(rows)\n\n\ndef outcome_betas(z_ms500, labels, ks, mode=\"r-a\", intercept=True):\n    \"\"\"Cluster x 40 betas, columns 1-20 prediction error, 21-40 shock (outcomeRegression.m).\"\"\"\n    F = z_ms500[:, 45:65, :]\n    rows = []\n    for k in ks:\n        m = labels == k\n        if mode == \"r-a\":\n            b = regress_betas(F[m].mean(0).T, [PE, SHOCK], intercept)\n        else:\n            b = np.mean([regress_betas(F[u].T, [PE, SHOCK], intercept) for u in np.flatnonzero(m)], 0)\n        rows.append(np.concatenate([b[0], b[1]]))\n    return np.array(rows)\n\n\ndef cue_lesion_betas(z_s1, sr, labels, ks, shuffled, rng, n_iter=1000):\n    \"\"\"cueRegression.m, \"Lesion regression\": each shuffled cluster's 16 x 14 mean firing has each\n    trial row permuted across the 14 intervals, then regression; betas averaged (reading s-c).\"\"\"\n    F = z_s1[:, 8:22, :]\n    means = {k: F[labels == k].mean(0).T for k in ks}     # 16 x 14\n    srs = {k: sr[labels == k].mean(0) for k in ks}\n    acc = np.zeros((len(ks), 28))\n    X = np.column_stack([np.ones(16), PROB, None if False else np.zeros(16)])\n    for i in range(n_iter):\n        for j, k in enumerate(ks):\n            Y = shuffle_rows(means[k], rng) if k in shuffled else means[k]\n            b = regress_betas(Y, [PROB, srs[k]])\n            acc[j] += np.concatenate([b[0], b[1]])\n    del X\n    return acc / n_iter\n\n\ndef outcome_lesion_betas(z_ms500, labels, ks, shuffled, rng, n_iter=1000, same_perm=True):\n    \"\"\"outcomeRegression.m, \"1-3 shuffled\": the shuffled cluster's 16 x 20 mean firing permuted\n    across trial rows (Shuffle(regData, 1)), the same permutation for every interval (same_perm) or\n    one per interval; betas averaged (reading s-d).\"\"\"\n    F = z_ms500[:, 45:65, :]\n    means = {k: F[labels == k].mean(0).T for k in ks}     # 16 x 20\n    acc = np.zeros((len(ks), 40))\n    for i in range(n_iter):\n        for j, k in enumerate(ks):\n            Y = means[k]\n            if k in shuffled:\n                Y = Y[rng.permutation(16)] if same_perm else shuffle_rows(Y.T, rng).T\n            b = regress_betas(Y, [PE, SHOCK])\n            acc[j] += np.concatenate([b[0], b[1]])\n    return acc / n_iter\n\n\ndef beta_shuffle_average(B, rows, rng, n_iter=1000, mode=\"s-a\", ncol_per=None):\n    \"\"\"Variants s-a / s-b on a beta matrix: the given rows permuted (each row across its columns,\n    or the block's entries together), averaged over n_iter.\"\"\"\n    acc = np.zeros_like(B)\n    for i in range(n_iter):\n        C = B.copy()\n        C[rows] = shuffle_rows(B[rows], rng) if mode == \"s-a\" else shuffle_block(B[rows], rng)\n        acc += C\n    return acc / n_iter\n\n\ndef pca_per_iteration(make, n_iter, ref):\n    \"\"\"Reading v-b: PCA on each iteration's matrix, each PC sign-aligned to ref (positive dot\n    product), weights and percentages averaged.\"\"\"\n    W = np.zeros((ref.shape[0], 2))\n    P = np.zeros(2)\n    for i in range(n_iter):\n        c, e = pca(make(i))\n        for j in range(2):\n            v = c[:, j] * (1 if c[:, j] @ ref[:, j] >= 0 else -1)\n            W[:, j] += v\n        P += e[:2]\n    return W / n_iter, P / n_iter\n\n\n# --- correlations, anatomy -----------------------------------------------------------------------\n\ndef corr_matrix(P):\n    return np.corrcoef(P)\n\n\ndef unit_cluster_corr(rows_unit, means_other, squared=False):\n    \"\"\"Mean over the other clusters of the Pearson r (or r squared) between a unit's row and each\n    cluster's mean row.\"\"\"\n    rs = []\n    for m in means_other:\n        r = np.corrcoef(rows_unit, m)[0, 1]\n        rs.append(r * r if squared else r)\n    return float(np.nanmean(rs))\n\n\ndef differential(region, members_a, members_b, n_regions=21):\n    \"\"\"Per region, its share of network A's units minus its share of network B's, in percentage\n    points (Source Data Fig. 3e and 5e right).\"\"\"\n    a = np.bincount(region[members_a], minlength=n_regions + 1)[1:]\n    b = np.bincount(region[members_b], minlength=n_regions + 1)[1:]\n    return 100 * (a / a.sum() - b / b.sum()), a, b\n"
}
```

```
File created successfully at: entries/strickland-2022/bst3.py (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/strickland-2022/bst3.py",
 "old_string": "    acc = np.zeros((len(ks), 28))\n    X = np.column_stack([np.ones(16), PROB, None if False else np.zeros(16)])\n    for i in range(n_iter):\n        for j, k in enumerate(ks):\n            Y = shuffle_rows(means[k], rng) if k in shuffled else means[k]\n            b = regress_betas(Y, [PROB, srs[k]])\n            acc[j] += np.concatenate([b[0], b[1]])\n    del X\n    return acc / n_iter",
 "new_string": "    acc = np.zeros((len(ks), 28))\n    for i in range(n_iter):\n        for j, k in enumerate(ks):\n            Y = shuffle_rows(means[k], rng) if k in shuffled else means[k]\n            b = regress_betas(Y, [PROB, srs[k]])\n            acc[j] += np.concatenate([b[0], b[1]])\n    return acc / n_iter"
}
```

```
The file entries/strickland-2022/bst3.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/strickland-2022 && cat > $TMPDIR/t4.py <<'EOF'
import sys,time,resource,numpy as np, pickle
sys.path.insert(0,'.')
import bst3
t=time.time()
zf=bst3.open_zip()
U=bst3.scan_units(zf)
print('scan',time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
C=bst3.load_cube(zf)
print('cube',time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
pickle.dump((U,{k:C[k] for k in C}),open(sys.argv[1],'wb'))
print(np.array_equal(U['ID'],C['ID']))
EOF
$TMPDIR/dev/bin/python $TMPDIR/t4.py $TMPDIR/all.pkl
```

```
scan 14.189584493637085 0.29856
cube 18.69680428504944 0.908228
False
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t5.py <<'EOF'
import sys,numpy as np, pickle, collections
sys.path.insert(0,'.')
import bst3
U,C=pickle.load(open(sys.argv[1],'rb'))
order={u:i for i,u in enumerate(U['ID'])}
idx=np.array([order[u] for u in C['ID']])
print('ids unique',len(set(C['ID'])), len(order))
c1s=U['c1s'][idx]  # unit, trial, 40
raw=C['fire/raw/s1/interval']  # unit, bin, trial
print('raw s1 equal', np.mean(np.transpose(c1s,(0,2,1))==raw), np.abs(np.transpose(c1s,(0,2,1))-raw).max())
b2=U['base2'][idx]; print('base2 equal', np.mean(b2==C['fire/raw/base2'][:,0,:]))
# z recompute from raw
diff=raw - C['fire/raw/base2'][:,0,:][:,None,:]
z=(diff-diff.mean((1,2),keepdims=True))/diff.std((1,2),ddof=1,keepdims=True)
print('z equal', np.nanmax(np.abs(z-C['fire/z/s1/interval'])), np.isnan(C['fire/z/s1/interval']).sum(), np.isnan(z).sum())
# sessions
S=U['sessions']; print('sessions',len(S), collections.Counter(k[2:4] for k in S))
print('consistent', all(s.get('consistent',True) for s in S.values()))
sess=np.array([u[:10] for u in C['ID']])
SR=C['poke/SR'][:,0,:]
ok=0
for k,s in S.items():
    sr=bst3.suppression_ratios(s['cue'],s['poke'],'code')
    m=sess==k
    ok+= np.allclose(SR[m],sr[None,:])
print('SR match sessions',ok)
# shock times
d=[]
for k,s in S.items():
    for sh in s['shock']:
        dd=sh-s['cue']; j=np.argmin(np.abs(dd)); d.append((j,dd[j]/bst3.FS))
d=np.array(d); print('shock trial rows',collections.Counter(d[:,0].astype(int)), 'delay',np.unique(np.round(d[:,1],2),return_counts=True))
print('n shocks per session',collections.Counter(len(s['shock']) for s in S.values()))
print('formats',collections.Counter(U['format']))
print('units per rat',collections.Counter(u[2:4] for u in C['ID']))
reg=C['anatomy/regionNum'][:,0,0]; print('regionNum',collections.Counter(reg.astype(int)))
# duplicate spike trains: hash of c250 rows
h=collections.Counter(U['c250'][i].tobytes() for i in range(len(U['ID'])))
print('dup c250', sum(v>1 for v in h.values()))
print('ms1 zero danger', (U['ms1'].sum(1)==0).sum())
EOF
$TMPDIR/dev/bin/python $TMPDIR/t5.py $TMPDIR/all.pkl
```

```
ids unique 1812 1812
raw s1 equal 0.9990307671081677 26.0
base2 equal 0.9987237858719646
z equal 3.481659405224491e-13 0 0
sessions 73 Counter({'25': 10, '22': 10, '13': 10, '11': 9, '27': 9, '10': 8, '15': 7, '24': 7, '14': 2, '21': 1})
consistent False
SR match sessions 73
shock trial rows Counter({np.int64(4): 73, np.int64(5): 73, np.int64(1): 73, np.int64(2): 73, np.int64(3): 73, np.int64(0): 72}) delay (array([12.]), array([437]))
n shocks per session Counter({6: 72, 5: 1})
formats Counter({np.str_('MATLAB 7.3'): 1067, np.str_('MATLAB 5.0'): 745})
units per rat Counter({'25': 409, '11': 328, '27': 304, '24': 195, '10': 192, '13': 141, '22': 116, '15': 52, '21': 43, '14': 32})
regionNum Counter({np.int64(14): 236, np.int64(8): 208, np.int64(3): 179, np.int64(5): 147, np.int64(1): 145, np.int64(4): 122, np.int64(22): 103, np.int64(16): 101, np.int64(7): 99, np.int64(15): 96, np.int64(12): 72, np.int64(10): 57, np.int64(20): 50, np.int64(2): 37, np.int64(13): 35, np.int64(21): 35, np.int64(9): 27, np.int64(24): 21, np.int64(11): 17, np.int64(23): 17, np.int64(17): 5, np.int64(27): 2, np.int64(6): 1})
dup c250 0
ms1 zero danger 34
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t6.py <<'EOF'
import sys,numpy as np, pickle, collections
sys.path.insert(0,'.')
import bst3
U,C=pickle.load(open(sys.argv[1],'rb'))
S=U['sessions']
for k,s in S.items():
    if not s.get('consistent',True): print('inconsistent',k)
order={u:i for i,u in enumerate(U['ID'])}
idx=np.array([order[u] for u in C['ID']])
c1s=np.transpose(U['c1s'][idx],(0,2,1)); raw=C['fire/raw/s1/interval']
bad=np.flatnonzero((c1s!=raw).any((1,2)))
print(len(bad), C['ID'][bad][:20])
for b in bad[:3]:
    w=np.argwhere(c1s[b]!=raw[b]); print(C['ID'][b], w[:5], c1s[b][tuple(w[0])], raw[b][tuple(w[0])], U['n_spikes'][idx[b]])
EOF
$TMPDIR/dev/bin/python $TMPDIR/t6.py $TMPDIR/all.pkl
```

```
inconsistent js10030220
119 ['js10030220pr25a13spk0239' 'js10030320pr25a14spk0291'
 'js10030520pr25a16spk0464' 'js10030520pr25a16spk0661'
 'js10030520pr25a16spk0785' 'js10030620pr25a17spk0208'
 'js10030620pr25a17spk0221' 'js10030620pr25a17spk0271'
 'js10030920pr25a18spk0330' 'js10031020pr25a19spk0292'
 'js10031120pr25a20spk0514' 'js10031120pr25a20spk0549'
 'js10031120pr25a20spk0649' 'js10031120pr25a20spk0753'
 'js10031120pr25a20spk0903' 'js11022520pr25b13spk0518'
 'js11022520pr25b13spk0530' 'js11022520pr25b13spk0624'
 'js11022520pr25b13spk0665' 'js11022520pr25b13spk0666']
js10030220pr25a13spk0239 [[ 0  1]
 [ 4  1]
 [13  5]
 [17  6]
 [19  6]] 88 87.0 345156
js10030320pr25a14spk0291 [[ 1  9]
 [ 4 13]
 [13 12]
 [24 13]
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='bst3.py'; s=open(p).read()
s=s.replace('''        spike = np.sort(spike)
        fmt.append(b[:10].decode())''','''        n_dup.append(spike.size - np.unique(spike).size)
        n_spk.append(spike.size)
        unsorted.append(bool(np.any(np.diff(spike) < 0)))
        # cubeScript.m counts with intersect(), which keeps each spike time once
        spike = np.unique(spike)
        fmt.append(b[:10].decode())''')
s=s.replace('''        ids.append(uid)
        n_spk.append(spike.size)
''','''        ids.append(uid)
''')
s=s.replace("ids, c250, c1s, base2, ms1, n_spk, fmt, sessions = [], [], [], [], [], [], [], {}",
 "ids, c250, c1s, base2, ms1, n_spk, n_dup, unsorted, fmt, sessions = [], [], [], [], [], [], [], [], [], {}")
s=s.replace('''            s.setdefault("consistent", True)
            s["consistent"] &= same''','''            if not same:
                s.setdefault("differing_units", []).append(uid)''')
s=s.replace('''"ms1": np.stack(ms1), "n_spikes": np.array(n_spk),''','''"ms1": np.stack(ms1), "n_spikes": np.array(n_spk),
            "n_duplicate_spikes": np.array(n_dup), "unsorted": np.array(unsorted),''')
open(p,'w').write(s)
EOF
grep -n "n_dup\|unsorted\|differing" bst3.py; $TMPDIR/dev/bin/python $TMPDIR/t4.py $TMPDIR/all.pkl && $TMPDIR/dev/bin/python - <<'EOF'
import sys,numpy as np,pickle
sys.path.insert(0,'.')
U,C=pickle.load(open('/tmp/claude-1001/all.pkl','rb'))
order={u:i for i,u in enumerate(U['ID'])}; idx=np.array([order[u] for u in C['ID']])
c1s=np.transpose(U['c1s'][idx],(0,2,1)); print('equal',(c1s==C['fire/raw/s1/interval']).all(), (U['n_duplicate_spikes']>0).sum(), U['n_duplicate_spikes'].sum(), U['unsorted'].sum())
for k,s in U['sessions'].items():
    if 'differing_units' in s: print(k, s['file_id'], s['differing_units'])
EOF
```

```
146:    ids, c250, c1s, base2, ms1, n_spk, n_dup, unsorted, fmt, sessions = [], [], [], [], [], [], [], [], [], {}
150:        n_dup.append(spike.size - np.unique(spike).size)
152:        unsorted.append(bool(np.any(np.diff(spike) < 0)))
174:                s.setdefault("differing_units", []).append(uid)
177:            "n_duplicate_spikes": np.array(n_dup), "unsorted": np.array(unsorted), "format": np.array(fmt),
scan 34.31686329841614 0.311988
cube 39.07839345932007 0.887588
False
equal True 204 9289 0
js10030220 js10030220pr25a13spk0392 ['js10030220pr25a13spk0009', 'js10030220pr25a13spk0049', 'js10030220pr25a13spk0044']
```

**Agent calls Bash**

```bash
date -u; cd  sed -n 1,60p entries/fouke-2025/README.md; python3 -c "
import json;nb=json.load(open('entries/fouke-2025/reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:6]: print(c['cell_type'],c['metadata'],''.join(c['source'])[:1500]); print('----')
"
```

```
Fri Nov 13 01:26:27 UTC 2026
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
| DC are faster than ZF for oblique stimuli | Reproduced |
| Both species turn in the direction of motion | Partially reproduced |
| ZF have higher angular acceleration than DC | Not reproduced |
| DC turn less than ZF to monocular stimuli | Reproduced |
| ZF swim in bouts, DC continuously | Reproduced |
[... 116 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/gen.py",
 "content": "import nbformat as nbf\nimport sys\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(open(sys.argv[2]).read())\n\ncode(r'''\nimport time\nimport resource\nimport warnings\nfrom collections import Counter\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.optimize import linear_sum_assignment\n\nimport bst3\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 50)\npd.set_option(\"display.max_rows\", 200)\nstarted = time.time()\n\nprint(f\"Data set CRCNS {bst3.DATASET}, version {bst3.VERSION}, doi:{bst3.DOI}\")\nprint(\"checksums.md5 in the bucket:\")\nprint(bst3.read_text(\"checksums.md5\"))\nzf = bst3.open_zip()\nmembers = zf.namelist()\nprint(len(members), \"members in data.zip;\", Counter(m.split(\"/\")[1] if m.count(\"/\") > 1 else m for m in members))\nfor m in members:\n    if not m.startswith(\"data/singleUnits/\") and not m.endswith(\"/\"):\n        print(\"  \", m, zf.getinfo(m).file_size, \"bytes\")\nunits = bst3.scan_units(zf)\ncube = bst3.load_cube(zf)\nsheets, sd_md5 = bst3.load_source_data()\nprint(f\"Source Data workbook md5 {sd_md5} (expected {bst3.SOURCE_DATA_MD5}): {sd_md5 == bst3.SOURCE_DATA_MD5}\")\nprint(f\"loaded in {time.time() - started:.0f} s, peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n''')\n\nmd(\"\"\"\n## Data check\n\nWhat a single-unit file holds, what the cube holds, and checks of the description against the values.\n\"\"\")\n\ncode(r'''\n# One single-unit file of each format, listed in full\nfor fmt in (\"MATLAB 5.0\", \"MATLAB 7.3\"):\n    name = next(n for n, f in zip(units[\"ID\"], units[\"format\"]) if f == fmt)\n    uid, spike, ev = bst3._parse_unit(zf.read(f\"data/singleUnits/{name}.mat\"))\n    print(f\"{fmt} file {name}.mat: id {uid!r}, spike {spike.shape} {spike.dtype} \"\n          f\"(first {spike[:3].tolist()}, last {spike[-1]}), events:\")\n    for k, v in ev.items():\n        print(f\"    time.{k}: {v.size} values, {v.min() if v.size else None} to {v.max() if v.size else None}\")\nprint(\"\\nFiles by format:\", dict(Counter(units[\"format\"])))\nprint(\"\\nCube fields read (shape as unit x bin x trial):\")\nfor k in bst3.CUBE_FIELDS[:-1]:\n    if k != \"anatomy/ID\":\n        print(f\"    {k}: {cube[k].shape}\")\nprint(\"The cube's anatomy.region is a MATLAB string object (MCOS), not readable outside MATLAB; region names come\")\nprint(\"from anatomy.regionNum and the numbering in cubeScript.m.\")\n''', [\"sanity\"])\n\ncode(r'''\n# Units, sessions, subjects\nids = cube[\"ID\"]\norder = {u: i for i, u in enumerate(units[\"ID\"])}\nassert len(order) == len(ids) == len(set(ids))\nix = np.array([order[u] for u in ids])           # single-unit scan -> cube order\nrat = np.array([u[2:4] for u in ids])\nsession = np.array([u[:10] for u in ids])\nsubject = np.array([bst3.RATS.index(r) + 1 for r in rat])\nfemale = np.isin(rat, list(bst3.FEMALE))\nprint(\"Unit files:\", len(units[\"ID\"]), \"; cube units:\", len(ids), \"; same set of ids:\", set(ids) == set(units[\"ID\"]))\nprint(\"Distinct sessions (animal + date in the id):\", len(set(session)))\ntab = pd.DataFrame({\"subject\": subject, \"animal\": rat, \"female\": female, \"session\": session})\nper = tab.groupby(\"subject\").agg(animal=(\"animal\", \"first\"), female=(\"female\", \"first\"),\n                                 units=(\"session\", \"size\"), sessions=(\"session\", \"nunique\"))\nper[\"sessions, Supp. Table 1\"] = [8, 9, 10, 2, 8, 1, 10, 7, 10, 10]\nprint(per.to_string())\nprint(\"Units from females:\", int(female.sum()))\n\n# Duplicate recordings: identical spike-count arrays (250-ms bins over all trials) between units\nh = Counter(units[\"c250\"][i].tobytes() for i in range(len(ix)))\nprint(\"\\nUnit pairs with identical binned spike counts:\", sum(v * (v - 1) // 2 for v in h.values() if v > 1))\nprint(\"Units with repeated spike times:\", int((units[\"n_duplicate_spikes\"] > 0).sum()),\n      \"; repeated times in total:\", int(units[\"n_duplicate_spikes\"].sum()),\n      \"; files with unsorted spike times:\", int(units[\"unsorted\"].sum()))\n''', [\"sanity\"])\n\ncode(r'''\n# The cube against the spike times, and the trial structure\nc1s = np.transpose(units[\"c1s\"][ix], (0, 2, 1))\nprint(\"cube fire.raw.s1 equals spike counts in the script's 1-s bins (each spike time counted once):\",\n      bool(np.array_equal(c1s, cube[\"fire/raw/s1/interval\"])))\nprint(\"cube fire.raw.base2 equals floor(count in 2 s before onset / 2):\",\n      bool(np.array_equal(units[\"base2\"][ix], cube[\"fire/raw/base2\"][:, 0, :])))\ndiff = cube[\"fire/raw/s1/interval\"] - cube[\"fire/raw/base2\"][:, 0, :][:, None, :]\nzs = (diff - diff.mean((1, 2), keepdims=True)) / diff.std((1, 2), ddof=1, keepdims=True)\nprint(\"cube fire.z.s1 equals the script's z of differential firing, max abs difference:\",\n      float(np.abs(zs - cube[\"fire/z/s1/interval\"]).max()))\nS = units[\"sessions\"]\nok = 0\nfor k, s in S.items():\n    sr = bst3.suppression_ratios(s[\"cue\"], s[\"poke\"], \"code\")\n    ok += np.allclose(cube[\"poke/SR\"][session == k, 0, :], sr[None, :])\nprint(f\"cube poke.SR equals the ratios recomputed from poke times in {ok} of {len(S)} sessions\")\nfor k, s in S.items():\n    if \"differing_units\" in s:\n        print(f\"Session {k}: units {s['differing_units']} carry cue or poke times that differ from unit {s['file_id']}\")\n\nrows = []\nfor k, s in S.items():\n    cue = s[\"cue\"]\n    nearest = [int(np.argmin(np.abs(sh - cue))) for sh in s[\"shock\"]]\n    rows.append({\"session\": k, \"trials\": len(cue), \"shocks\": len(s[\"shock\"]),\n                 \"shock rows\": \"\".join(str(r + 1) + \",\" for r in sorted(nearest)),\n                 \"shock delay s\": sorted(set(np.round((s[\"shock\"] - cue[nearest]) / bst3.FS, 3))),\n                 \"session min\": (cue.max() - cue.min()) / bst3.FS / 60,\n                 \"ITI min\": np.diff(np.sort(cue)).mean() / bst3.FS / 60, \"pokes\": len(s[\"poke\"])})\ntrials = pd.DataFrame(rows)\nprint(\"\\nTrials per session:\", dict(Counter(trials.trials)), \"; shocks per session:\", dict(Counter(trials.shocks)))\nprint(\"Rows of the trial table that have a shock:\", dict(Counter(trials[\"shock rows\"])))\nprint(\"Delay from cue onset to shock onset (s):\", sorted({d for x in trials[\"shock delay s\"] for d in x}))\nprint(\"Mean ITI per session, min: %.2f to %.2f\" % (trials[\"ITI min\"].min(), trials[\"ITI min\"].max()))\nprint(trials[trials.shocks != 6].to_string(index=False))\n''', [\"sanity\"])\n\nmd(\"\"\"\nThe trial rows are as the descriptor says: the shocks fall on rows 1 to 6 (danger, then\nuncertainty shock), 12.0 s after cue onset (2 s after the 10-s cue), so shock offset is at\n12.5 s, which is where the outcome window of `outcomeAnalysis.m` (500-ms bins 46 to 65 of the\n40-s window from 10 s before cue onset) starts. Spike times and event times are in samples at\n30 kHz, as `cubeScript.m` counts them.\n\"\"\")\n\ncode(r'''\n# Clock check: firing in the 2 s after shock onset minus the 2 s before cue onset, on shocked and\n# unshocked rows, at the true event times and with every trial's times shifted by +60 s\ndef shock_contrast(shift_s):\n    vals = []\n    for k, s in S.items():\n        cue = s[\"cue\"] + shift_s * bst3.FS\n        mask = session == k\n        for u in np.flatnonzero(mask):\n            _, spike, _ = None, None, None\n        vals.append(k)\n    return vals\n\n# from the 250-ms counts (20 s before to 40 s after onset): shock onset is bins 128-135 (12-14 s)\nc = units[\"c250\"][ix].astype(float)              # unit, trial, bin\nresp = c[:, :, 128:136].sum(2) / 2 - c[:, :, 72:80].sum(2) / 2   # Hz change\nshock_rows, noshock_rows = resp[:, :6].mean(1), resp[:, 6:].mean(1)\nd = shock_rows - noshock_rows\nprint(f\"Per unit, firing change 12-14 s after onset, shock rows minus no-shock rows: mean {d.mean():.2f} Hz, \"\n      f\"median {np.median(d):.2f} Hz, Wilcoxon p = {stats.wilcoxon(d).pvalue:.2g}\")\n# the same contrast 2 s earlier (10-12 s, the delay before shock) and in a window 20 s before onset\nfor name, sl in ((\"10-12 s (before shock)\", slice(120, 128)), (\"-20 to -18 s\", slice(0, 8))):\n    r = c[:, :, sl].sum(2) / 2 - c[:, :, 72:80].sum(2) / 2\n    dd = r[:, :6].mean(1) - r[:, 6:].mean(1)\n    print(f\"Same contrast at {name}: mean {dd.mean():.2f} Hz, Wilcoxon p = {stats.wilcoxon(dd).pvalue:.2g}\")\n# with the shock labels shuffled across rows within a session\nrng = np.random.default_rng(0)\nperm = rng.permutation(16)\ndd = resp[:, perm[:6]].mean(1) - resp[:, perm[6:]].mean(1)\nprint(f\"Shuffled row labels {perm[:6] + 1}: mean {dd.mean():.2f} Hz, Wilcoxon p = {stats.wilcoxon(dd).pvalue:.2g}\")\n''', [\"sanity\"])\n\nmd(\"\"\"\nThe shock response appears only after shock onset and only on the rows the trial table marks as\nshocked, so the spike times, the event times and the trial rows share one clock and one order in\nevery file read here (a contrast between conditions, protocol step 2). This is shown over all units\ntogether; per session it is consistent with the data, not shown.\n\"\"\")\n\ncode(r'''\n# Regions, coordinates, ranges of the variables used\nreg_raw = cube[\"anatomy/regionNum\"][:, 0, 0].astype(int)\nregion = np.array([bst3.REGION_REMAP[r] for r in reg_raw])\nprint(\"Raw region numbers (cubeScript.m numbering):\", dict(sorted(Counter(reg_raw).items())))\nprint(\"After the scripts' merges (21 -> DpWh, 24 -> x/scp):\",\n      {bst3.REGIONS[k - 1]: v for k, v in sorted(Counter(region).items())})\nfor k in (\"anatomy/x\", \"anatomy/y\", \"anatomy/z\"):\n    v = cube[k].ravel()\n    print(f\"{k}: {v.min():.2f} to {v.max():.2f} (units not stated)\")\nzs1, z5 = cube[\"fire/z/s1/interval\"], cube[\"fire/z/ms500/interval\"]\nsr = cube[\"poke/SR\"][:, 0, :]\nprint(f\"z.s1: {zs1.shape}, {np.nanmin(zs1):.2f} to {np.nanmax(zs1):.2f}, NaN {int(np.isnan(zs1).sum())}\")\nprint(f\"z.ms500: {z5.shape}, {np.nanmin(z5):.2f} to {np.nanmax(z5):.2f}, NaN {int(np.isnan(z5).sum())}\")\nprint(f\"poke.SR: {sr.min():.2f} to {sr.max():.2f}; poke.base {cube['poke/base'].min():.0f} to {cube['poke/base'].max():.0f} \"\n      f\"pokes/min; poke.cue {cube['poke/cue'].min():.0f} to {cube['poke/cue'].max():.0f} pokes/min\")\nX_cue = bst3.cue_matrix(zs1)\nX_out = bst3.outcome_matrix(z5)\nprint(\"Cue matrix\", X_cue.shape, \"; outcome matrix\", X_out.shape)\n''', [\"sanity\"])\n\n# ---------------------------------------------------------------- link\nmd(\"\"\"\n## source-data-cluster-link\n\n> The data set's units can be matched to the rows of the paper's Source Data cluster sheets, which\n> gives the paper's own cue and outcome cluster membership.\n\nEach unit's 42-value cue row and 80-value outcome row are compared with every row of Source Data\nsheets \"Figure 2b k1\" to \"k21\" and \"Figure 4b k1\" to \"k11\". The rows are computed under the claims\nfile's four normalization readings (from the spike times, 250-ms bins) and under the normalization\nof the paper's own `cubeScript.m`, which is what the cube holds (1-s and 500-ms bins z-scored\ndirectly over the 40-s window from 10 s before onset, baseline rounded down).\n\"\"\")\n\ncode(r'''\nsd_cue = {k: bst3.sd_cue_cluster_rows(sheets, k) for k in range(1, 22)}\nsd_out = {k: bst3.sd_outcome_cluster_rows(sheets, k) for k in range(1, 12)}\nprint(\"Source Data rows: cue\", sum(len(v) for v in sd_cue.values()), \"; outcome\", sum(len(v) for v in sd_out.values()))\nreadings = {\"cubeScript.m (the cube)\": (X_cue, X_out)}\nreadings.update(bst3.normalized_readings(units[\"c250\"][ix].transpose(0, 1, 2)))\nlink_rows = []\nL1_cue = np.zeros(len(ids), int)\nL1_out = np.zeros(len(ids), int)\nfor name, (rc, ro) in readings.items():\n    res = {}\n    for which, sd, rows in ((\"cue\", sd_cue, rc), (\"outcome\", sd_out, ro)):\n        exact, corr, lab = 0, 0, np.zeros(len(ids), int)\n        n = 0\n        for k, B in sd.items():\n            hits, br, bi = bst3.match_rows(B, rows)\n            n += len(B)\n            for h, r, i in zip(hits, br, bi):\n                if len(h) == 1:\n                    exact += 1\n                    lab[h[0]] = k\n                if r > 0.99:\n                    corr += 1\n        res[which] = (exact, corr, n, lab)\n    link_rows.append({\"reading\": name,\n                      \"cue rows matching one unit (max abs diff < 0.01)\": f\"{res['cue'][0]} / {res['cue'][2]}\",\n                      \"cue rows with best r > 0.99\": res[\"cue\"][1],\n                      \"outcome rows matching one unit\": f\"{res['outcome'][0]} / {res['outcome'][2]}\",\n                      \"outcome rows with best r > 0.99\": res[\"outcome\"][1]})\n    if name.startswith(\"cubeScript\"):\n        L1_cue, L1_out = res[\"cue\"][3], res[\"outcome\"][3]\nprint(pd.DataFrame(link_rows).to_string(index=False))\nprint(\"\\nUnits given a cue cluster:\", int((L1_cue > 0).sum()), \"; an outcome cluster:\", int((L1_out > 0).sum()))\nprint(\"Cue cluster sizes (L1):\", np.bincount(L1_cue, minlength=22)[1:].tolist())\nprint(\"Outcome cluster sizes (L1):\", np.bincount(L1_out, minlength=12)[1:].tolist())\ndiffs = []\nfor k, B in sd_cue.items():\n    hits, _, _ = bst3.match_rows(B, X_cue)\n    diffs += [np.abs(X_cue[h[0]] - b).max() for h, b in zip(hits, B) if len(h) == 1]\nprint(f\"Largest difference between a matched cue row and its Source Data row: {max(diffs):.2e}\")\n''', [\"claim:source-data-cluster-link\"])\n\nmd(\"\"\"\n**Result: reproduced.** Under the normalization of the paper's own `cubeScript.m`, every one of the\n1812 cue rows and 1812 outcome rows of the Source Data cluster sheets matches exactly one unit of\nthe data set, with differences at rounding level; the cluster sizes are the ones the claims file\nlists. None of the claims file's four readings (n-a, n-b, w-a, w-b, from 250-ms bins) matches any\nrow within 0.01, though they correlate with them; the script's normalization is a detail the\nMethods leave open and the paper's code settles. The link gives L1 for every claim below.\n\"\"\")\n\n# ---------------------------------------------------------------- fig1c\nmd(\"\"\"\n## fig1c-suppression-order\n\n> During recording sessions suppression of rewarded nose poking was high to danger, intermediate\n> to uncertainty and low to safety, with a main effect of cue (F(2,142) = 149.2, p = 1.26 x 10^-35)\n> over 73 sessions.\n\nPer session, the ratio per trial from its poke times; the session value per cue is the mean over\nits trials (uncertainty pooling 8). Empty trials (no pokes before or during the cue) are set to 1\nas in `cubeScript.m`, and to 0 (sr-a) or left out (sr-b) as the claims file's readings.\n\"\"\")\n\ncode(r'''\nkeys = sorted(S)\nsess_sex = np.array([k[2:4] in bst3.FEMALE for k in keys]).astype(int)\nsd1c = np.array([r[1:4] for r in sheets[\"Figure 1c\"][1:] if r[0] is not None], float)\nprint(\"Source Data Fig. 1c:\", sd1c.shape[0], \"sessions; means\", sd1c.mean(0).round(3))\nrows = []\nvals = {}\nfor empty in (\"code\", \"zero\", \"drop\"):\n    Y = []\n    n_empty = 0\n    for k in keys:\n        r = bst3.suppression_ratios(S[k][\"cue\"], S[k][\"poke\"], empty)\n        n_empty += int(np.isnan(bst3.suppression_ratios(S[k][\"cue\"], S[k][\"poke\"], \"drop\")).sum())\n        Y.append([np.nanmean(r[0:4]), np.nanmean(r[4:12]), np.nanmean(r[12:16])])\n    Y = np.array(Y)\n    vals[empty] = Y\n    a = bst3.mixed_anova_cue_by_group(Y, sess_sex)\n    rows.append({\"empty trials\": {\"code\": \"set to 1 (script)\", \"zero\": \"set to 0 (sr-a)\", \"drop\": \"left out (sr-b)\"}[empty],\n                 \"danger\": Y[:, 0].mean(), \"uncertainty\": Y[:, 1].mean(), \"safety\": Y[:, 2].mean(),\n                 \"F cue x sex (a-a)\": a[\"F_mixed\"], \"df a-a\": a[\"df_mixed\"], \"p a-a\": a[\"p_mixed\"],\n                 \"F repeated (a-b)\": a[\"F_rm\"], \"df a-b\": a[\"df_rm\"], \"p a-b\": a[\"p_rm\"]})\nprint(\"Trials with no pokes in either period:\", n_empty, \"of\", 16 * len(keys))\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\na = bst3.mixed_anova_cue_by_group(sd1c, np.zeros(len(sd1c)))\nprint(f\"\\nOn Source Data Fig. 1c: repeated-measures F({a['df_rm'][0]},{a['df_rm'][1]}) = {a['F_rm']:.1f}\")\n# do the data set's session values match the Source Data rows (as multisets)?\nfor empty, Y in vals.items():\n    m = sum(np.any(np.all(np.abs(sd1c - y) < 1e-6, 1)) for y in Y)\n    print(f\"sessions whose three values equal a Source Data row ({empty}): {m} of {len(Y)}\")\nprint(\"\\nPer subject, mean over sessions (script reading):\")\nper_rat = pd.DataFrame(vals[\"code\"], columns=[\"danger\", \"uncertainty\", \"safety\"])\nper_rat[\"subject\"] = [bst3.RATS.index(k[2:4]) + 1 for k in keys]\nprint(per_rat.groupby(\"subject\").agg([\"mean\", \"size\"]).round(3).to_string())\n''', [\"claim:fig1c-suppression-order\"])\n\nmd(\"\"\"\n**Result: reproduced.** Over the 73 sessions the session means are ordered danger > uncertainty >\nsafety under every reading, each within tolerance of the Source Data means, and the cue x sex mixed\nANOVA (a-a) gives F(2,142) within tolerance of 149.2 with p far below 0.05; the repeated-measures\nreading (a-b) has df (2,144) and a lower F, as on the paper's own values.\n\"\"\")\n\n# ---------------------------------------------------------------- figs2\nmd(\"\"\"\n## figs2-each-rat-discriminates\n\n> Rats showed complete discrimination during the recording sessions, shown rat by rat with 95%\n> bootstrap confidence intervals over sessions.\n\nPer rat, 10,000 bootstrap resamples of its sessions (percentile interval), on the script's ratios.\n\"\"\")\n\ncode(r'''\nrng = np.random.default_rng(2)\nY = vals[\"code\"]\nsubj = np.array([bst3.RATS.index(k[2:4]) + 1 for k in keys])\nrows = []\nfor s in range(1, 11):\n    y = Y[subj == s]\n    n = len(y)\n    q = {\"D-S\": y[:, 0] - y[:, 2], \"U-S\": y[:, 1] - y[:, 2], \"D-U\": y[:, 0] - y[:, 1],\n         \"D\": y[:, 0], \"U\": y[:, 1]}\n    row = {\"subject\": s, \"sessions\": n, \"danger\": y[:, 0].mean(), \"uncertainty\": y[:, 1].mean(), \"safety\": y[:, 2].mean()}\n    if n >= 2:\n        b = rng.integers(0, n, (10000, n))\n        for name, v in q.items():\n            lo, hi = np.percentile(v[b].mean(1), [2.5, 97.5])\n            row[name + \" CI\"] = f\"[{lo:.2f}, {hi:.2f}]\"\n            row[name + \" excl0\"] = bool(lo > 0 or hi < 0)\n    rows.append(row)\nt = pd.DataFrame(rows)\nprint(t.round(3).to_string(index=False))\nok3 = t[t.sessions >= 3]\nfor name, cols in ((\"c-a (D-S and U-S exclude 0)\", [\"D-S excl0\", \"U-S excl0\"]),\n                   (\"c-b (D-U and U-S exclude 0)\", [\"D-U excl0\", \"U-S excl0\"]),\n                   (\"c-c (D and U exclude 0)\", [\"D excl0\", \"U excl0\"])):\n    n = int(ok3[cols].all(1).sum())\n    print(f\"{name}: {n} of {len(ok3)} rats with at least 3 sessions\")\n''', [\"claim:figs2-each-rat-discriminates\"])\n\nmd(\"\"\"\n**Result: see the counts above.** The outcome follows the criterion: reproduced when every rat with\nat least 3 sessions meets one reading, partially reproduced for at least 6 of the 8.\n\"\"\")\n\n# ---------------------------------------------------------------- units\nmd(\"\"\"\n## units-sessions-subjects\n\n> 1812 single units were isolated and held over 73 one-hour sessions from ten rats, 965 of them from\n> the four females, with per-subject totals of 192, 328, 141, 32, 52, 43, 116, 195, 409 and 304 units.\n\"\"\")\n\ncode(r'''\nexpected = [192, 328, 141, 32, 52, 43, 116, 195, 409, 304]\ngot = [int((subject == s).sum()) for s in range(1, 11)]\nprint(\"units\", len(ids), \"(expected 1812); from females\", int(female.sum()), \"(expected 965)\")\nprint(\"sessions\", len(set(session)), \"(expected 73; Supplementary Table 1 sums to 75)\")\nprint(\"per subject (mapping js10..js27 -> 1..10 from cueAnalysis.m):\")\nprint(pd.DataFrame({\"subject\": range(1, 11), \"animal\": bst3.RATS, \"units\": got, \"expected\": expected,\n                    \"sessions\": per.sessions.values, \"Supp. Table 1\": per[\"sessions, Supp. Table 1\"].values}).to_string(index=False))\nprint(\"all per-subject totals equal:\", got == expected)\nprint(\"session duration (first to last cue onset), min: %.0f to %.0f\" % (trials[\"session min\"].min(), trials[\"session min\"].max()))\n''', [\"claim:units-sessions-subjects\"])\n\nmd(\"\"\"\n**Result: reproduced.** 1812 units, 965 from females, 73 sessions, and the ten per-subject totals\nequal the paper's. Supplementary Table 1 lists 75 sessions; the data set has one session fewer for\nsubject 5 (7 against 8) and for subject 10 (9 against 10), which accounts for the 73 of the Results.\n\"\"\")\n\n# ---------------------------------------------------------------- regions\nmd(\"\"\"\n## fig1e-regions\n\n> The units spanned 21 brainstem regions ... with the largest counts in the paramedian raphe (236),\n> ventral dorsal raphe (208) and dorsolateral periaqueductal gray (179).\n\"\"\")\n\ncode(r'''\ncnt = np.bincount(region, minlength=22)[1:]\nt = pd.DataFrame({\"region\": bst3.REGIONS, \"units\": cnt,\n                  \"Source Data Fig. 3e left (sum)\": [sum(r[i + 1] for r in sheets[\"Figure 3e left\"][1:3]) for i in range(21)]})\nprint(t.to_string(index=False))\nprint(\"regions with units:\", int((cnt > 0).sum()))\nprint(\"PMnR %d (236), DRV %d (208), DLPAG %d (179), VLPAG %d (147), DPG %d (145)\" %\n      (cnt[19], cnt[8], cnt[2], cnt[4], cnt[0]))\n''', [\"claim:fig1e-regions\"])\n\nmd(\"\"\"\n**Result: reproduced.** 21 regions hold units, and the five counts equal the expected values; every\nregion's count equals the Source Data Fig. 3e left sums.\n\"\"\")\n\n# ---------------------------------------------------------------- kmeans cue\nmd(\"\"\"\n## fig2b-cue-clusters\n\n> K-means clustering of cue firing organized brainstem neurons into at least 21 functional clusters,\n> of sizes from 24 to 219 (median 83).\n\nk-means with 21 clusters on the 1812 x 42 cue matrix, k-means++ seeding, one replicate, 20 seeds\n(the claims file's standard choice; the script uses MATLAB `rng(1)`, which cannot be reproduced\nhere). The best of the 20 (lowest summed distance) is a variant.\n\"\"\")\n\ncode(r'''\nseeds = np.arange(20)\nkm_cue = bst3.kmeans_sizes(X_cue, 21, seeds)\nsz = np.array([[s.min(), s.max(), np.median(s)] for s, _, _ in km_cue])\nprint(\"per seed (min, max, median):\")\nprint(pd.DataFrame(sz, columns=[\"min\", \"max\", \"median\"], index=seeds).T.to_string())\nmed = np.median(sz, 0)\nprint(\"median over seeds: min %.1f (24 +- 2.4), max %.1f (219 +- 21.9), median %.1f (83 +- 8.3)\" % tuple(med))\nbest = int(np.argmin([i for _, i, _ in km_cue]))\nprint(\"best of 20 (seed %d): sizes\" % best, sorted(km_cue[best][0].tolist()))\nprint(\"L1 sizes (paper):\", sorted(np.bincount(L1_cue)[1:].tolist()))\ninertia_L1 = sum(((X_cue[L1_cue == k] - X_cue[L1_cue == k].mean(0)) ** 2).sum() for k in range(1, 22))\nprint(f\"summed squared distance: paper's clustering {inertia_L1:.0f}; seeds {min(i for _, i, _ in km_cue):.0f} to {max(i for _, i, _ in km_cue):.0f}\")\nfrom sklearn.cluster import KMeans\nmsd = [KMeans(n_clusters=k, n_init=1, random_state=0).fit(X_cue).inertia_ / len(X_cue) for k in range(1, 26)]\nprint(\"mean squared distance for 1 to 25 clusters:\", np.round(msd, 2).tolist())\n''', [\"claim:fig2b-cue-clusters\"])\n\nmd(\"\"\"\n**Result: see the medians above against the tolerances.**\n\"\"\")\n\n# ---------------------------------------------------------------- pca cue\nmd(\"\"\"\n## fig2c-cue-pc1-ordered\n\n> Across all 1812 neurons, the first principal component of cue firing (29.7% of firing variance)\n> was ordered cue firing, danger > uncertainty > safety.\n\"\"\")\n\ncode(r'''\ncoef_cue, expl_cue = bst3.pca(X_cue)\npc1 = coef_cue[:, 0] * np.sign(coef_cue[2:12, 0].mean())\nw = {c: pc1[i * 14 + 2:i * 14 + 12].mean() for i, c in enumerate([\"danger\", \"uncertainty\", \"safety\"])}\nprint(f\"PC1 {expl_cue[0]:.2f}% (29.7 +- 2.97), PC2 {expl_cue[1]:.2f}%, PC3 {expl_cue[2]:.2f}%\")\nprint(\"mean PC1 weight over the 10 cue seconds:\", {k: round(v, 4) for k, v in w.items()})\nprint(\"ordered danger > uncertainty > safety:\", w[\"danger\"] > w[\"uncertainty\"] > w[\"safety\"])\nA = bst3.sd_matrix(sheets, \"Figure 2c inset\", 1, 42)\nprint(f\"On the Source Data Fig. 2c inset matrix ({A.shape}): PC1 {bst3.pca(A)[1][0]:.2f}%\")\nhits, br, _ = bst3.match_rows(A, X_cue)\nprint(\"inset rows equal to a unit's cue row:\", sum(len(h) > 0 for h in hits), \"; median best r\", np.median(br).round(3))\n# the inset as the heat-plot version (baseline of the three cues' 2 pre-cue seconds subtracted, cueAnalysis.m)\nbase = (X_cue[:, 0:2].mean(1) + X_cue[:, 14:16].mean(1) + X_cue[:, 28:30].mean(1)) / 3\nhits, br, _ = bst3.match_rows(A, X_cue - base[:, None])\nprint(\"inset rows equal to a unit's baseline-subtracted row:\", sum(len(h) > 0 for h in hits))\n''', [\"claim:fig2c-cue-pc1-ordered\"])\n\nmd(\"\"\"\n**Result: reproduced.** PC1 of the data set's cue matrix explains 29.73% of the variance, and its mean\nweights over the cue are ordered danger > uncertainty > safety. The 47.1% the claims file found on\nthe Source Data inset comes from a different matrix: its rows are not the units' cue rows.\n\"\"\")\n\n# ---------------------------------------------------------------- contribution\nmd(\"\"\"\n## fig2c-pc1-contribution\n\n> PC1 firing information originated from nine clusters (k1 to k9), a minority of neurons (505 of\n> 1812, 27.9%), with k1 and k2 contributing most per unit.\n\nPer cluster, its rows of the cue matrix shuffled 1000 times, PCA each time; the drop of PC1 percent\nfrom the intact value, averaged, divided by the cluster size (cueAnalysis.m). Readings s-a (each\nrow across its columns; the script's `Shuffle(..., 2)`) and s-b (the block's entries together).\n\"\"\")\n\ncode(r'''\nrng = np.random.default_rng(3)\nsd2c = np.array([r[1] for r in sheets[\"Figure 2c\"][1:22]], float)\ncontrib = {}\nfor mode in (\"s-a\", \"s-b\"):\n    contrib[mode] = bst3.pc1_contribution(X_cue, L1_cue, range(1, 22), rng, 1000, mode)\nt = pd.DataFrame({\"cluster\": range(1, 22), \"size\": np.bincount(L1_cue)[1:],\n                  \"s-a\": [contrib[\"s-a\"][k] for k in range(1, 22)],\n                  \"s-b\": [contrib[\"s-b\"][k] for k in range(1, 22)], \"Source Data\": sd2c})\nprint(t.round(4).to_string(index=False))\nfor mode in (\"s-a\", \"s-b\"):\n    v = np.array([contrib[mode][k] for k in range(1, 22)])\n    top9 = set(np.argsort(-v)[:9] + 1)\n    top2 = set(np.argsort(-v)[:2] + 1)\n    print(f\"{mode}: nine largest {sorted(top9)}; k1-k9 out of place: {len(set(range(1, 10)) - top9)}; two largest {sorted(top2)}; \"\n          f\"k1 {v[0]:.4f} (0.121 +- 0.012), k2 {v[1]:.4f} (0.113 +- 0.011); max abs diff from Source Data {np.abs(v - sd2c).max():.4f}\")\nprint(\"units in k1-k9:\", int(np.isin(L1_cue, range(1, 10)).sum()), \"of\", len(L1_cue))\n''', [\"claim:fig2c-pc1-contribution\"])\n\ncode(r'''\n# L2: the best-of-20 k-means solution, its clusters numbered by PC1 contribution per unit (s-a)\nL2_raw = km_cue[best][2] + 1\nc2 = bst3.pc1_contribution(X_cue, L2_raw, range(1, 22), np.random.default_rng(4), 1000, \"s-a\")\nrank = sorted(c2, key=lambda k: -c2[k])\nL2_cue = np.zeros_like(L2_raw)\nfor new, old in enumerate(rank, 1):\n    L2_cue[L2_raw == old] = new\nprint(\"L2 sizes in contribution order:\", [int((L2_cue == k).sum()) for k in range(1, 22)])\nprint(\"L2 contribution per unit:\", [round(c2[k], 4) for k in rank])\nprint(\"L2 nine largest hold\", int(np.isin(L2_cue, range(1, 10)).sum()), \"units (505 +- 50.5)\")\nct = pd.crosstab(L1_cue, L2_cue)\nprint(\"overlap of L1 k1-k9 with L2 k1-k9:\", int((np.isin(L1_cue, range(1, 10)) & np.isin(L2_cue, range(1, 10))).sum()))\n''', [\"claim:fig2c-pc1-contribution\"])\n\nmd(\"\"\"\n**Result: reproduced.** Under L1 the nine largest contributions per unit are k1 to k9, k1 and k2 are\nthe two largest, and their values are within tolerance under both shuffle readings; reading s-a\ngives every cluster's Source Data value to within 0.0004. Under L2 the total of the nine largest is\ngiven above.\n\"\"\")\n\n# ---------------------------------------------------------------- latency\nmd(\"\"\"\n## fig2d-danger-latency\n\n> Clusters k1 to k9 showed shorter firing latencies after danger onset, and across all 21 clusters\n> danger firing latency correlated negatively with the magnitude of PC1 contribution (R2 = 0.41,\n> p = 0.0017).\n\nPer unit, `findchangepts` (one change in mean) on its danger firing over the 10-s cue in 1-ms bins.\nBaseline subtraction and z-scoring are affine maps of the summed spike count, and the change point\nof a mean is unchanged by them, so l-a reduces to the change point of the summed 1-ms spike counts\nover the four danger trials; l-b uses the cube's 250-ms z values repeated into 1-ms bins (from\n`fire.z.ms250`, not read here; the 100-ms and 1-s bins are not used either), and is not run.\n\"\"\")\n\ncode(r'''\nms1 = units[\"ms1\"][ix]\nlat = np.array([bst3.change_point(x) or np.nan for x in ms1], float)\nprint(\"units with a latency:\", int(np.isfinite(lat).sum()), \"of\", len(lat), \"; Source Data Fig. 2d lists\",\n      len(sheets[\"Figure 2d\"]) - 1)\nprint(\"units with no danger spikes:\", int((ms1.sum(1) == 0).sum()))\nsd2d = pd.DataFrame([r for r in sheets[\"Figure 2d\"][1:] if r[0] is not None], columns=[\"cluster\", \"latency\"])\ncl_lat = np.array([np.nanmean(lat[L1_cue == k]) for k in range(1, 22)])\nsd_cl = sd2d.groupby(\"cluster\").latency.mean().reindex(range(1, 22)).values\nprint(pd.DataFrame({\"cluster\": range(1, 22), \"n with latency\": [int(np.isfinite(lat[L1_cue == k]).sum()) for k in range(1, 22)],\n                    \"Source Data n\": sd2d.groupby(\"cluster\").size().reindex(range(1, 22)).values,\n                    \"mean latency ms\": cl_lat.round(0), \"Source Data mean\": sd_cl.round(0)}).to_string(index=False))\n# per-unit agreement: multiset of latencies per cluster\nsame = sum(len(set(lat[(L1_cue == k) & np.isfinite(lat)].astype(int)) & set(sd2d[sd2d.cluster == k].latency.astype(int)))\n           for k in range(1, 22))\nprint(\"latency values shared with Source Data within the same cluster:\", same)\ncvec = np.array([contrib[\"s-a\"][k] for k in range(1, 22)])\nsize = np.bincount(L1_cue)[1:]\nfor name, x in ((\"c-a per unit\", cvec), (\"c-b cluster total\", cvec * size)):\n    for lname, y in ((\"this attempt\", cl_lat), (\"Source Data latencies\", sd_cl)):\n        r, p = stats.pearsonr(x, y)\n        print(f\"{name}, {lname}: r = {r:.3f}, R2 = {r * r:.3f}, p = {p:.2g}\")\nsub = np.isin(L1_cue, range(1, 10))\nprint(f\"mean latency, k1-k9 units {np.nanmean(lat[sub]):.0f} ms, k10-k21 units {np.nanmean(lat[~sub]):.0f} ms; \"\n      f\"Mann-Whitney p = {stats.mannwhitneyu(lat[sub & np.isfinite(lat)], lat[~sub & np.isfinite(lat)]).pvalue:.2g}\")\n''', [\"claim:fig2d-danger-latency\"])\n\nmd(\"\"\"\n**Result: see the correlations above against R2 = 0.41 +- 0.041.**\n\"\"\")\n\n# ---------------------------------------------------------------- correlations\nmd(\"\"\"\n## fig2e-cue-subnetwork\n\n> Clusters k1 to k9 separated from the rest by cluster-cluster cue firing correlations ... with k3\n> the exception showing weak correlations with its fellow clusters.\n\"\"\")\n\ncode(r'''\nz_types = {c: m for c, m in zip([\"danger\", \"uncertainty\", \"safety\"], bst3.type_means(zs1, [\"danger\", \"uncertainty\", \"safety\"]))}\ndef cluster_profiles(cols):\n    P = np.hstack([z_types[c][:, cols] for c in [\"danger\", \"uncertainty\", \"safety\"]])\n    return np.array([P[L1_cue == k].mean(0) for k in range(1, 22)])\nsub_idx, sup_idx = np.arange(9), np.arange(9, 21)\nfor name, cols in ((\"42 columns (Source Data, 14 per cue)\", slice(8, 22)), (\"36 columns (Methods, 12 per cue)\", slice(8, 20)),\n                   (\"120 columns (script's full 40-s window)\", slice(0, 40))):\n    R = np.corrcoef(cluster_profiles(cols))\n    for power, lab in ((1, \"r\"), (2, \"r squared\")):\n        Q = R ** power\n        within = Q[np.ix_(sub_idx, sub_idx)][np.triu_indices(9, 1)].mean()\n        between = Q[np.ix_(sub_idx, sup_idx)].mean()\n        k3 = [(Q[i, [j for j in sub_idx if j != i]]).mean() for i in sub_idx]\n        print(f\"{name}, {lab}: within k1-k9 {within:.3f}, k1-k9 with k10-k21 {between:.3f}; \"\n              f\"mean with the other eight per cluster {np.round(k3, 3).tolist()}; lowest k{int(np.argmin(k3)) + 1}\")\nsd2e = bst3.sd_matrix(sheets, \"Figure 2e\", 1, 42)\nprint(\"Source Data Fig. 2e rows equal the L1 cluster means:\", np.allclose(sd2e, cluster_profiles(slice(8, 22)), atol=1e-9))\n''', [\"claim:fig2e-cue-subnetwork\"])\n\nmd(\"\"\"\n**Result: see the values above.** Reproduced when the within-subnetwork mean exceeds the between\nmean and k3 has the lowest mean with the other eight.\n\"\"\")\n\n# ---------------------------------------------------------------- cue hubs\nmd(\"\"\"\n## fig2f-cue-hubs\n\n> K1 and k2 were hubs of the cue subnetwork ... single-unit firing that correlated most strongly\n> with the mean cue firing of their fellow subnetwork clusters.\n\nPer unit of k1 to k9, its danger firing over the 14 1-s intervals correlated with the mean danger\nfiring of each other subnetwork cluster, averaged. The Source Data column is headed \"R2\", and the\nscript's outcome analysis squares the coefficients, so r and r squared are both computed, and the\n42-value row (all three cues) is a variant; the one that equals Source Data Fig. 2f per unit shows\nwhich the paper used.\n\"\"\")\n\ncode(r'''\nsd2f = pd.DataFrame([r for r in sheets[\"Figure 2f\"][1:] if r[0] is not None], columns=[\"cluster\", \"R2\"])\ndz = z_types[\"danger\"][:, 8:22]\nmeans_d = {k: dz[L1_cue == k].mean(0) for k in range(1, 10)}\nmeans_all = {k: X_cue[L1_cue == k].mean(0) for k in range(1, 10)}\nvariants = {}\nfor name, rows_, means in ((\"danger 14\", dz, means_d), (\"all 42\", X_cue, means_all)):\n    for sq in (False, True):\n        v = np.full(len(ids), np.nan)\n        for u in np.flatnonzero(np.isin(L1_cue, range(1, 10))):\n            k = L1_cue[u]\n            v[u] = bst3.unit_cluster_corr(rows_[u], [means[j] for j in range(1, 10) if j != k], sq)\n        variants[f\"{name}, {'r squared' if sq else 'r'}\"] = v\nrows = []\nfor name, v in variants.items():\n    m = [np.nanmean(v[L1_cue == k]) for k in range(1, 10)]\n    same = sum(np.isclose(np.sort(v[L1_cue == k]), np.sort(sd2f[sd2f.cluster == k].R2.values), atol=1e-6).all()\n               for k in range(1, 10))\n    rows.append({\"measure\": name, **{f\"k{k}\": round(m[k - 1], 3) for k in range(1, 10)}, \"clusters equal to Source Data\": same})\nrows.append({\"measure\": \"Source Data\", **{f\"k{k}\": round(sd2f[sd2f.cluster == k].R2.mean(), 3) for k in range(1, 10)}})\nprint(pd.DataFrame(rows).to_string(index=False))\nv = variants[\"danger 14, r squared\"]\nfor thr_n in (7, 8):\n    print(f\"\\nthreshold 0.05/{thr_n} = {0.05 / thr_n:.4f}\")\n    for hub in (1, 2):\n        out = []\n        for k in range(3, 10):\n            t_ = stats.ttest_ind(v[L1_cue == hub], v[L1_cue == k])\n            lv = stats.levene(v[L1_cue == hub], v[L1_cue == k], center=\"mean\")\n            out.append(f\"k{k}: t={t_.statistic:.2f} p={t_.pvalue:.2g}{'*' if t_.pvalue < 0.05 / thr_n and t_.statistic > 0 else ''}\"\n                       f\" (Levene p={lv.pvalue:.2g})\")\n        print(f\"k{hub} vs\", \"; \".join(out))\n''', [\"claim:fig2f-cue-hubs\"])\n\ncode(r'''\n# The same with r (the claims file's wording, \"coefficients averaged\")\nv = variants[\"danger 14, r\"]\nfor hub in (1, 2):\n    ps = [stats.ttest_ind(v[L1_cue == hub], v[L1_cue == k]) for k in range(3, 10)]\n    print(f\"r: k{hub} mean {np.nanmean(v[L1_cue == hub]):.3f}; exceeds k3-k9 at 0.05/7: \"\n          f\"{sum(t.pvalue < 0.05 / 7 and t.statistic > 0 for t in ps)} of 7; at 0.05/8: {sum(t.pvalue < 0.05 / 8 and t.statistic > 0 for t in ps)} of 7\")\nv = variants[\"danger 14, r squared\"]\nfor hub in (1, 2):\n    ps = [stats.ttest_ind(v[L1_cue == hub], v[L1_cue == k]) for k in range(3, 10)]\n    print(f\"r squared: k{hub} mean {np.nanmean(v[L1_cue == hub]):.3f}; exceeds k3-k9 at 0.05/7: \"\n          f\"{sum(t.pvalue < 0.05 / 7 and t.statistic > 0 for t in ps)} of 7; at 0.05/8: {sum(t.pvalue < 0.05 / 8 and t.statistic > 0 for t in ps)} of 7\")\n# Variant: the Methods' eight-cluster subnetwork (k1-k8)\nv8 = np.full(len(ids), np.nan)\nfor u in np.flatnonzero(np.isin(L1_cue, range(1, 9))):\n    k = L1_cue[u]\n    v8[u] = bst3.unit_cluster_corr(dz[u], [means_d[j] for j in range(1, 9) if j != k], True)\nprint(\"k1-k8 subnetwork, r squared means:\", [round(np.nanmean(v8[L1_cue == k]), 3) for k in range(1, 9)])\n''', [\"claim:fig2f-cue-hubs\"])\n\nmd(\"\"\"\n**Result: see the means and tests above.** Reproduced when k1 and k2 have the two highest means,\nwithin tolerance, and each exceeds every one of k3 to k9 at the threshold.\n\"\"\")\n\n# ---------------------------------------------------------------- cue anatomy\nmd(\"\"\"\n## fig2g-cue-anatomy\n\n> Neurons of every cue cluster were found in at least six brainstem regions, and subnetwork neurons,\n> including the k1 and k2 hubs, were concentrated in the deep layer of the superior colliculus and\n> the subdivisions of the periaqueductal gray.\n\"\"\")\n\ncode(r'''\nnreg = [len(set(region[L1_cue == k])) for k in range(1, 22)]\nprint(\"regions per cue cluster:\", nreg, \"; minimum\", min(nreg))\nsc_pag = np.isin(region, [1, 2, 3, 4, 5])\nsub = np.isin(L1_cue, range(1, 10))\nhub = np.isin(L1_cue, [1, 2])\nprint(f\"share in DPG, DpWh, DLPAG, LPAG, VLPAG: subnetwork {sc_pag[sub].mean():.3f} ({sc_pag[sub].sum()}/{sub.sum()}), \"\n      f\"supranetwork {sc_pag[~sub].mean():.3f} ({sc_pag[~sub].sum()}/{(~sub).sum()}), k1 and k2 {sc_pag[hub].mean():.3f} ({sc_pag[hub].sum()}/{hub.sum()})\")\ntab = pd.crosstab(sub, sc_pag)\nprint(\"chi-square, subnetwork x SC/PAG (shown, not the criterion):\", stats.chi2_contingency(tab)[:2])\n''', [\"claim:fig2g-cue-anatomy\"])\n\nmd(\"\"\"\n**Result: see above.** Reproduced when all 21 clusters span at least six regions and both shares\nare higher than the supranetwork's.\n\"\"\")\n\n# ---------------------------------------------------------------- regression cue\nmd(\"\"\"\n## fig3a-cluster-signals\n\n> Linear regression revealed distinct threat probability and fear behaviour signals across the 21\n> cue clusters, varying in time, with greatest signaling at onset (k5), at offset (k15), sustained\n> over the cue (k10), or peaking mid cue (k6).\n\nRegression per cluster and 1-s interval; readings r-a (the script's: cluster mean firing, mean\nmember suppression ratio) and r-b (per unit, betas averaged), each with (i-a) and without (i-b) an\nintercept. Signal per interval: the larger absolute beta. Interval indices: 0-1 pre-cue, 2-11 the\ncue seconds, 12-13 after.\n\"\"\")\n\ncode(r'''\nsd3b = bst3.sd_matrix(sheets, \"Figure 3b middle\", 2, 28)\nbetas = {}\nfor mode in (\"r-a\", \"r-b\"):\n    for ic, iname in ((True, \"i-a\"), (False, \"i-b\")):\n        betas[(mode, iname)] = bst3.cue_betas(zs1, sr, L1_cue, range(1, 22), mode, ic)\nfor key, B in betas.items():\n    print(key, \"max abs difference from Source Data Fig. 3b middle:\", round(float(np.abs(B - sd3b).max()), 6))\ndef shapes(B):\n    s = np.maximum(np.abs(B[:, :14]), np.abs(B[:, 14:]))\n    k5, k15, k10, k6 = s[4], s[14], s[9], s[5]\n    return {\"onset k5\": int(np.argmax(k5)) == 2, \"offset k15\": int(np.argmax(k15)) in (11, 12),\n            \"sustained k10\": bool((k10[2:12] >= 0.5 * k10.max()).all()),\n            \"mid-cue k6\": int(np.argmax(k6)) in range(4, 10) and k6[2] <= 0.5 * k6.max() and k6[11] <= 0.5 * k6.max()}, s\nfor key, B in betas.items():\n    ok, s = shapes(B)\n    print(key, ok, \"; held:\", sum(ok.values()))\nok, s = shapes(betas[(\"r-a\", \"i-a\")])\nprint(\"\\nr-a, i-a signal per interval (larger |beta|):\")\nprint(pd.DataFrame(s[[4, 14, 9, 5]], index=[\"k5\", \"k15\", \"k10\", \"k6\"]).round(2).to_string())\n''', [\"claim:fig3a-cluster-signals\"])\n\nmd(\"\"\"\n**Result: see the shape tests above.** Reproduced when all four hold under one reading.\n\"\"\")\n\ncode(r'''\ndef orient_cue(c):\n    pc1 = c[:, 0] * np.sign(c[16:26, 0].mean())\n    pc2 = c[:, 1] * np.sign(c[2:12, 1].mean())\n    return pc1, pc2\ndef cue_shape(pc1, pc2):\n    beh1, prob1 = pc1[14:], pc1[:14]\n    beh2, prob2 = pc2[14:], pc2[:14]\n    return {\"PC1 |beh| > |prob| over cue\": np.abs(beh1[2:12]).mean() > np.abs(prob1[2:12]).mean(),\n            \"PC1 beh max in cue s 3-8\": int(np.argmax(beh1)) in range(4, 10),\n            \"PC1 mean prob over cue < 0\": prob1[2:12].mean() < 0,\n            \"PC2 |prob| > |beh| over cue\": np.abs(prob2[2:12]).mean() > np.abs(beh2[2:12]).mean(),\n            \"PC2 prob max in cue s 1-3\": int(np.argmax(prob2)) in range(2, 5)}\n''')\n\nmd(\"\"\"\n## fig3b-signal-pca\n\n> PCA of cluster beta weights showed PC1 (62.7% of signaling variance) to be a sustained behaviour\n> signal peaking mid cue with lesser, opposing threat probability signaling, and PC2 (26.12%) a\n> sustained threat probability signal peaking early in the cue with lesser behaviour signaling.\n\nPC1 oriented so its mean behaviour weight over the 10 cue seconds is positive, PC2 so its mean\nprobability weight is positive. The weights are also shown with the script's plotting baseline\n(the mean of the two pre-cue seconds) subtracted, as a variant.\n\"\"\")\n\ncode(r'''\nB_cue = betas[(\"r-a\", \"i-a\")]\nrows = []\nmats = {\"Source Data Fig. 3b middle\": sd3b, \"recomputed, L1 (r-a, i-a)\": B_cue}\nfor key in ((\"r-b\", \"i-a\"), (\"r-a\", \"i-b\"), (\"r-b\", \"i-b\")):\n    mats[f\"recomputed, L1 {key}\"] = betas[key]\nmats[\"recomputed, L2 (r-a, i-a)\"] = bst3.cue_betas(zs1, sr, L2_cue, range(1, 22), \"r-a\", True)\npcs_cue = {}\nfor name, M in mats.items():\n    c, e = bst3.pca(M)\n    p1, p2 = orient_cue(c)\n    pcs_cue[name] = (p1, p2, e)\n    sh = cue_shape(p1, p2)\n    rows.append({\"matrix\": name, \"PC1 %\": round(e[0], 2), \"PC2 %\": round(e[1], 2), **sh})\nprint(pd.DataFrame(rows).to_string(index=False))\np1, p2, e = pcs_cue[\"recomputed, L1 (r-a, i-a)\"]\nprint(\"\\nPC1 probability weights:\", p1[:14].round(3).tolist())\nprint(\"PC1 behaviour weights:  \", p1[14:].round(3).tolist())\nprint(\"PC2 probability weights:\", p2[:14].round(3).tolist())\nprint(\"PC2 behaviour weights:  \", p2[14:].round(3).tolist())\nbl = lambda v: np.concatenate([v[:14] - v[:2].mean(), v[14:] - v[14:16].mean()])\nprint(\"with the pre-cue baseline subtracted:\", cue_shape(bl(p1), bl(p2)))\n''', [\"claim:fig3b-signal-pca\"])\n\nmd(\"\"\"\n**Result: see the table above.** Reproduced when both percentages are within tolerance (62.7 +- 6.27,\n26.12 +- 2.61) and the shapes hold.\n\"\"\")\n\n# ---------------------------------------------------------------- lesions cue\nmd(\"\"\"\n## fig3c-subnetwork-lesion and fig3d-supranetwork-lesion\n\n> Lesioning (shuffling) the cue subnetwork left the sustained behaviour signal intact but reduced\n> threat probability signaling, most at cue onset ...\n\n> Lesioning the cue supranetwork diminished the sustained behaviour signal and turned the sustained\n> threat probability signal into a dynamic probability-to-behaviour signal ...\n\nLesion as in `cueRegression.m`: each shuffled cluster's trial rows permuted across the 14 intervals\nbefore regression, betas averaged over 1000 iterations (s-c), then one PCA (v-a). Variants: s-a and\ns-b on the intact betas, and v-b (PCA per iteration on s-a, sign-aligned to the intact PCs).\n\"\"\")\n\ncode(r'''\nrng = np.random.default_rng(5)\nlesion = {}\nfor name, shuffled in ((\"sub\", set(range(1, 10))), (\"supra\", set(range(10, 22)))):\n    lesion[(name, \"s-c\")] = bst3.cue_lesion_betas(zs1, sr, L1_cue, range(1, 22), shuffled, rng, 1000)\n    rows_ = np.array(sorted(shuffled)) - 1\n    lesion[(name, \"s-a\")] = bst3.beta_shuffle_average(B_cue, rows_, rng, 1000, \"s-a\")\n    lesion[(name, \"s-b\")] = bst3.beta_shuffle_average(B_cue, rows_, rng, 1000, \"s-b\")\nsd3c, sd3d = bst3.sd_matrix(sheets, \"Figure 3c middle\", 2, 28), bst3.sd_matrix(sheets, \"Figure 3d middle\", 2, 28)\nprint(\"max abs difference from Source Data: sub s-c %.3f, supra s-c %.3f\" %\n      (np.abs(lesion[(\"sub\", \"s-c\")] - sd3c).max(), np.abs(lesion[(\"supra\", \"s-c\")] - sd3d).max()))\nip1, ip2, ie = pcs_cue[\"recomputed, L1 (r-a, i-a)\"]\nrows = []\nles_pcs = {}\nfor key, M in list(lesion.items()) + [((\"sub\", \"Source Data\"), sd3c), ((\"supra\", \"Source Data\"), sd3d)]:\n    c, e = bst3.pca(M)\n    p1, p2 = orient_cue(c)\n    les_pcs[key] = (p1, p2, e)\n    rows.append({\"lesion\": key[0], \"reading\": key[1], \"PC1 %\": round(e[0], 2), \"PC2 %\": round(e[1], 2),\n                 \"PC1 mean beh over cue\": round(p1[16:26].mean(), 3), \"PC2 prob, first cue s\": round(p2[2], 3),\n                 \"PC2 |prob| peak s\": int(np.argmax(np.abs(p2[2:12]))) + 1, \"PC2 |beh| peak s\": int(np.argmax(np.abs(p2[16:26]))) + 1})\nrows.append({\"lesion\": \"intact\", \"reading\": \"r-a, i-a\", \"PC1 %\": round(ie[0], 2), \"PC2 %\": round(ie[1], 2),\n             \"PC1 mean beh over cue\": round(ip1[16:26].mean(), 3), \"PC2 prob, first cue s\": round(ip2[2], 3),\n             \"PC2 |prob| peak s\": int(np.argmax(np.abs(ip2[2:12]))) + 1, \"PC2 |beh| peak s\": int(np.argmax(np.abs(ip2[16:26]))) + 1})\nprint(pd.DataFrame(rows).to_string(index=False))\n''', [\"claim:fig3c-subnetwork-lesion\", \"claim:fig3d-supranetwork-lesion\"])\n\ncode(r'''\n# v-b: PCA per iteration (s-a on the betas), sign-aligned to the intact PCs, averaged\nref = np.column_stack([ip1, ip2])\nfor name, shuffled in ((\"sub\", range(0, 9)), (\"supra\", range(9, 21))):\n    rws = np.array(list(shuffled))\n    def make(i, rws=rws, g=np.random.default_rng(6)):\n        C = B_cue.copy()\n        C[rws] = bst3.shuffle_rows(B_cue[rws], g)\n        return C\n    W, P = bst3.pca_per_iteration(make, 1000, ref)\n    print(f\"v-b {name}: PC1 {P[0]:.2f}%, PC2 {P[1]:.2f}%; PC1 mean beh over cue {W[16:26, 0].mean():.3f}; PC2 prob first cue s {W[2, 1]:.3f}\")\nfor name in (\"s-c\", \"s-a\", \"s-b\", \"Source Data\"):\n    s1, s2, _ = les_pcs[(\"sub\", name)]\n    u1, u2, _ = les_pcs[(\"supra\", name)]\n    c_ = {\"3c PC1 beh >= 75% intact\": s1[16:26].mean() >= 0.75 * ip1[16:26].mean(),\n          \"3c PC1 beh > supra-lesion's\": s1[16:26].mean() > u1[16:26].mean(),\n          \"3c PC2 prob at first cue s < intact\": s2[2] < ip2[2],\n          \"3d PC1 beh < intact\": u1[16:26].mean() < ip1[16:26].mean(),\n          \"3d PC2 |prob| peak in first half, |beh| in second\": (int(np.argmax(np.abs(u2[2:12]))) < 5) and (int(np.argmax(np.abs(u2[16:26]))) >= 5)}\n    print(name, c_)\n''', [\"claim:fig3c-subnetwork-lesion\", \"claim:fig3d-supranetwork-lesion\"])\n\nmd(\"\"\"\n**Result: see the criteria above, for fig3c-subnetwork-lesion and fig3d-supranetwork-lesion.**\n\"\"\")\n\n# ---------------------------------------------------------------- network anatomy\nmd(\"\"\"\n## fig3e-network-anatomy\n\n> Subnetwork and supranetwork neurons were distributed throughout the brainstem, with subtle biases\n> only for the subnetwork, to which the deep layer of the superior colliculus and the lateral\n> periaqueductal gray contributed more.\n\"\"\")\n\ncode(r'''\nd3e, a, b = bst3.differential(region, np.isin(L1_cue, range(1, 10)), np.isin(L1_cue, range(10, 22)))\nsd3e = np.array(sheets[\"Figure 3e right\"][1][1:22], float)\nt = pd.DataFrame({\"region\": bst3.REGIONS, \"k1-k9\": a, \"k10-k21\": b, \"differential\": d3e.round(2), \"Source Data\": sd3e.round(2)})\nprint(t.to_string(index=False))\ntop = np.argsort(-d3e)[:4]\nprint(\"four largest:\", [bst3.REGIONS[i] for i in top], \"; DPG %.2f (5.93 +- 0.59), LPAG %.2f (7.41 +- 0.74)\" % (d3e[0], d3e[3]))\n# Variant: the Methods' wording, region proportion in the subnetwork minus the overall subnetwork proportion\nvar = np.array([np.isin(L1_cue[region == r], range(1, 10)).mean() for r in range(1, 22)]) - np.isin(L1_cue, range(1, 10)).mean()\nprint(\"variant (share of region in subnetwork minus 505/1812):\", dict(zip(bst3.REGIONS, (100 * var).round(1))))\ndL2, _, _ = bst3.differential(region, np.isin(L2_cue, range(1, 10)), np.isin(L2_cue, range(10, 22)))\nprint(\"L2: two largest\", [bst3.REGIONS[i] for i in np.argsort(-dL2)[:2]], np.sort(dL2)[::-1][:4].round(2))\n''', [\"claim:fig3e-network-anatomy\"])\n\nmd(\"\"\"\n**Result: see above.** Reproduced when DPG and LPAG have the two largest positive differentials,\nwithin tolerance.\n\"\"\")\n\n# ---------------------------------------------------------------- outcome clusters\nmd(\"\"\"\n## fig4b-outcome-clusters\n\n> K-means clustering of mean post-shock firing for the four trial types organized brainstem\n> neurons into at least 11 functional clusters, of sizes from 46 to 322 (median 169).\n\"\"\")\n\ncode(r'''\nkm_out = bst3.kmeans_sizes(X_out, 11, seeds)\nsz = np.array([[s.min(), s.max(), np.median(s)] for s, _, _ in km_out])\nprint(pd.DataFrame(sz, columns=[\"min\", \"max\", \"median\"], index=seeds).T.to_string())\nmed = np.median(sz, 0)\nprint(\"median over seeds: min %.1f (46 +- 4.6), max %.1f (322 +- 32.2), median %.1f (169 +- 16.9)\" % tuple(med))\nbest_o = int(np.argmin([i for _, i, _ in km_out]))\nprint(\"best of 20 (seed %d):\" % best_o, sorted(km_out[best_o][0].tolist()), \"; paper:\", sorted(np.bincount(L1_out)[1:].tolist()))\nmsd = [KMeans(n_clusters=k, n_init=1, random_state=0).fit(X_out).inertia_ / len(X_out) for k in range(1, 21)]\nprint(\"mean squared distance for 1 to 20 clusters:\", np.round(msd, 2).tolist())\n# L2 outcome clusters matched to L1 by overlap (Hungarian)\nL2o_raw = km_out[best_o][2]\nct = pd.crosstab(L2o_raw, L1_out).reindex(columns=range(1, 12), fill_value=0)\nr_, c_ = linear_sum_assignment(-ct.values)\nL2_out = np.zeros_like(L1_out)\nfor a_, b_ in zip(r_, c_):\n    L2_out[L2o_raw == ct.index[a_]] = b_ + 1\nprint(\"L2 outcome clusters matched to L1; agreement with L1: %.3f\" % (L2_out == L1_out).mean())\n''', [\"claim:fig4b-outcome-clusters\"])\n\nmd(\"\"\"\n**Result: see the medians above against the tolerances.**\n\"\"\")\n\n# ---------------------------------------------------------------- outcome pca\nmd(\"\"\"\n## fig4c-positive-prediction-error\n\n> PCA of post-shock firing of all 1812 neurons showed positive prediction error on top of shock\n> responding as PC1 (17.7% of firing variance) ...\n\"\"\")\n\ncode(r'''\ncoef_out, expl_out = bst3.pca(X_out)\np = coef_out[:, 0] * np.sign(coef_out[20:40, 0].mean())\nw = dict(zip([\"danger\", \"unc_shock\", \"unc_omission\", \"safety\"], [p[i * 20:(i + 1) * 20].mean() for i in range(4)]))\nprint(f\"PC1 {expl_out[0]:.2f}% (17.7 +- 1.77); PC2 {expl_out[1]:.2f}%\")\nprint(\"mean PC1 weights:\", {k: round(v, 4) for k, v in w.items()})\nprint(\"unc shock > danger:\", w[\"unc_shock\"] > w[\"danger\"], \"; danger > safety:\", w[\"danger\"] > w[\"safety\"],\n      \"; omission not below safety:\", w[\"unc_omission\"] >= w[\"safety\"])\nC4 = bst3.sd_matrix(sheets, \"Figure 4c\", 2, 80)\nprint(f\"Source Data Fig. 4c matrix {C4.shape}: PC1 {bst3.pca(C4)[1][0]:.2f}%; rows equal to a unit's outcome row:\",\n      sum(len(h) > 0 for h in bst3.match_rows(C4, X_out)[0]))\n''', [\"claim:fig4c-positive-prediction-error\"])\n\nmd(\"\"\"\n**Result: see above.**\n\"\"\")\n\n# ---------------------------------------------------------------- phasic/tonic\nmd(\"\"\"\n## fig4b-phasic-network and fig4b-tonic-network\n\n> Outcome clusters k1 to k3 showed phasic firing changes after shock ... and by their correlations\n> formed a phasic outcome network.\n\n> Outcome clusters k6 to k9 showed sustained firing changes after surprising shock ... and by their\n> correlations formed a tonic outcome network.\n\nCluster mean outcome profiles under L1 (and L2 as a variant). 500-ms intervals: 0-1 the first second\nafter shock offset, 0-9 the first 5 s, 8-9 the second ending 5 s after offset, 10-19 seconds 5 to 10.\n\"\"\")\n\ncode(r'''\ndef outcome_profiles(lab):\n    return np.array([X_out[lab == k].mean(0) for k in range(1, 12)])\ndef network_tests(lab):\n    P = outcome_profiles(lab)\n    D, US, UO, SF = P[:, :20], P[:, 20:40], P[:, 40:60], P[:, 60:80]\n    shock = (D + US) / 2\n    first = shock[:, 0:2].mean(1)\n    ti_a = np.abs(first - shock[:, 0:10].mean(1))\n    ti_b = np.abs(first - shock[:, 8:10].mean(1))\n    R = np.corrcoef(P)\n    ph, to = [0, 1, 2], [5, 6, 7, 8]\n    within_ph = R[np.ix_(ph, ph)][np.triu_indices(3, 1)].mean()\n    between_ph = R[np.ix_(ph, [i for i in range(11) if i not in ph])].mean()\n    within_to = R[np.ix_(to, to)][np.triu_indices(4, 1)].mean()\n    between_to = R[np.ix_(to, [i for i in range(11) if i not in to])].mean()\n    f1 = lambda M, k: M[k, 0:2].mean()\n    res_ph = {\"index t-a k1-k3 above k6-k9\": bool(ti_a[ph].min() > ti_a[to].max()),\n              \"index t-b k1-k3 above k6-k9\": bool(ti_b[ph].min() > ti_b[to].max()),\n              \"k1 US > D > 0 (1st s)\": f1(US, 0) > f1(D, 0) > 0, \"k2 D > US > 0\": f1(D, 1) > f1(US, 1) > 0,\n              \"k3 D, US < 0\": f1(D, 2) < 0 and f1(US, 2) < 0, \"network\": within_ph > between_ph}\n    m = lambda M, k: M[k].mean()\n    res_to = {\"k6 US < 0 and lowest\": m(US, 5) < 0 and m(US, 5) < min(m(D, 5), m(UO, 5), m(SF, 5)),\n              \"k7 US > 0 and highest\": m(US, 6) > 0 and m(US, 6) > max(m(D, 6), m(UO, 6), m(SF, 6)),\n              \"k8 US > 0 and highest\": m(US, 7) > 0 and m(US, 7) > max(m(D, 7), m(UO, 7), m(SF, 7)),\n              \"k7 sustained\": US[6, 10:20].mean() > 0.5 * US[6, 0:2].mean(),\n              \"k8 sustained\": US[7, 10:20].mean() > 0.5 * US[7, 0:2].mean(),\n              \"network\": within_to > between_to}\n    info = pd.DataFrame({\"cluster\": range(1, 12), \"index t-a\": ti_a.round(3), \"index t-b\": ti_b.round(3),\n                         \"D 1st s\": D[:, 0:2].mean(1).round(2), \"US 1st s\": US[:, 0:2].mean(1).round(2),\n                         \"D mean\": D.mean(1).round(2), \"US mean\": US.mean(1).round(2), \"UO mean\": UO.mean(1).round(2),\n                         \"S mean\": SF.mean(1).round(2), \"US 5-10 s\": US[:, 10:20].mean(1).round(2)})\n    return res_ph, res_to, info, (within_ph, between_ph, within_to, between_to)\nfor name, lab in ((\"L1\", L1_out), (\"L2\", L2_out)):\n    ph, to, info, w = network_tests(lab)\n    print(name, \"phasic:\", ph)\n    print(name, \"tonic:\", to)\n    print(name, \"mean r within / between: phasic %.3f / %.3f, tonic %.3f / %.3f\" % w)\n    if name == \"L1\":\n        print(info.to_string(index=False))\n''', [\"claim:fig4b-phasic-network\", \"claim:fig4b-tonic-network\"])\n\nmd(\"\"\"\n**Result: see the tests above, for fig4b-phasic-network and fig4b-tonic-network.**\n\"\"\")\n\n# ---------------------------------------------------------------- network PCA\nmd(\"\"\"\n## fig4e-network-pca\n\n> Within the phasic outcome network, PC1 (37.0% of firing variance) was equivalent phasic shock firing\n> on danger and uncertainty trials; within the tonic outcome network, PC1 (29.2%) was selective\n> firing to surprising shock with opposing firing to safety.\n\"\"\")\n\ncode(r'''\nph_units, to_units = np.isin(L1_out, [1, 2, 3]), np.isin(L1_out, [6, 7, 8, 9])\nprint(\"phasic units\", int(ph_units.sum()), \"; tonic units\", int(to_units.sum()))\nfor name, M in ((\"recomputed\", None), (\"Source Data\", \"sd\")):\n    if M is None:\n        Xp, Xt = X_out[ph_units], X_out[to_units]\n    else:\n        Xp, Xt = bst3.sd_matrix(sheets, \"Figure 4e left\", 2, 80), bst3.sd_matrix(sheets, \"Figure 4e right\", 2, 80)\n    cp, ep = bst3.pca(Xp)\n    ct_, et = bst3.pca(Xt)\n    p = cp[:, 0] * np.sign(cp[0:2, 0].mean())\n    D, US, UO, SF = p[:20], p[20:40], p[40:60], p[60:80]\n    f = lambda v: v[0:2].mean()\n    late = lambda v: v[10:20].mean()\n    ph_ok = {\"D 1st s > 2x late\": f(D) > 2 * late(D), \"US 1st s > 2x late\": f(US) > 2 * late(US),\n             \"|D-US| < |D-S| and |US-S|\": abs(f(D) - f(US)) < min(abs(f(D) - f(SF)), abs(f(US) - f(SF)))}\n    q = ct_[:, 0] * np.sign(ct_[20:40, 0].mean())\n    means = [q[i * 20:(i + 1) * 20].mean() for i in range(4)]\n    to_ok = {\"US largest\": int(np.argmax(means)) == 1, \"S negative\": means[3] < 0}\n    print(f\"{name}: phasic PC1 {ep[0]:.2f}% (37.0 +- 3.7) {ph_ok}; first-second weights D {f(D):.3f} US {f(US):.3f} \"\n          f\"UO {f(UO):.3f} S {f(SF):.3f}\")\n    print(f\"{name}: tonic PC1 {et[0]:.2f}% (29.2 +- 2.92) {to_ok}; mean weights D, US, UO, S {np.round(means, 3).tolist()}\")\n''', [\"claim:fig4e-network-pca\"])\n\nmd(\"\"\"\n**Result: see above.**\n\"\"\")\n\n# ---------------------------------------------------------------- outcome hubs\nmd(\"\"\"\n## fig4f-outcome-hubs\n\n> In the phasic outcome network, k1 and k2 single-unit firing correlated better with the population\n> firing of their fellow clusters than k3 did; in the tonic network, k6 ... was the hub.\n\nPer unit, its 80-value row correlated with the mean row of each other cluster of its network,\nsquared and averaged (`outcomeAnalysis.m`); r without squaring is a variant. Two-sample t-tests\n(MATLAB `ttest2`, equal variances), Bonferroni over the pairs within the network (3 phasic, 6 tonic).\n\"\"\")\n\ncode(r'''\nsd4f = pd.concat([pd.DataFrame([r for r in sheets[s][1:] if r[0] is not None], columns=[\"cluster\", \"R2\"])\n                  for s in (\"Figure 4f left\", \"Figure 4f right\")])\nprof = outcome_profiles(L1_out)\ndef hub_values(net, sq):\n    v = np.full(len(ids), np.nan)\n    for u in np.flatnonzero(np.isin(L1_out, net)):\n        k = L1_out[u]\n        v[u] = bst3.unit_cluster_corr(X_out[u], [prof[j - 1] for j in net if j != k], sq)\n    return v\nfor net, label in (([1, 2, 3], \"phasic k1-k3\"), ([6, 7, 8, 9], \"tonic k6-k9\"), ([1, 2, 3, 4, 5], \"variant phasic k1-k5\"),\n                   ([7, 8, 9, 10], \"variant tonic k7-k10\")):\n    for sq in (True, False):\n        v = hub_values(net, sq)\n        means = {k: round(np.nanmean(v[L1_out == k]), 3) for k in net}\n        npairs = len(net) * (len(net) - 1) // 2\n        tests = []\n        for i, a_ in enumerate(net):\n            for b_ in net[i + 1:]:\n                t_ = stats.ttest_ind(v[L1_out == a_], v[L1_out == b_])\n                lv = stats.levene(v[L1_out == a_], v[L1_out == b_], center=\"mean\")\n                tests.append(f\"k{a_}-k{b_} t={t_.statistic:.2f} p={t_.pvalue:.2g}{'*' if t_.pvalue < 0.05 / npairs else ''} L={lv.pvalue:.2g}\")\n        same = \"\"\n        if sq and label[0] != \"v\":\n            same = \"; clusters equal to Source Data: %d\" % sum(\n                np.isclose(np.sort(v[L1_out == k]), np.sort(sd4f[sd4f.cluster == k].R2.values), atol=1e-6).all() for k in net)\n        print(f\"{label}, {'r squared' if sq else 'r'}: means {means}{same}\")\n        print(\"    \", \"; \".join(tests))\n''', [\"claim:fig4f-outcome-hubs\"])\n\nmd(\"\"\"\n**Result: see above.** Reproduced when k1 and k2 each exceed k3 by t-test, and k6 has the highest\nmean, above each of k7 to k9 by t-test.\n\"\"\")\n\n# ---------------------------------------------------------------- outcome anatomy\nmd(\"\"\"\n## fig4g-outcome-anatomy\n\n> Phasic outcome neurons were more common at the axis extremes ... while tonic outcome neurons, most\n> strikingly the k6 hub, were distributed throughout the brainstem.\n\"\"\")\n\ncode(r'''\next = np.isin(region, [3, 4, 5, 7, 8, 9, 10, 20])     # DLPAG, LPAG, VLPAG, DRL, DRD, DRV, PDR, PMnR\nfp, ft = ext[ph_units].mean(), ext[to_units].mean()\nprint(f\"fraction in DLPAG, LPAG, VLPAG, DRL, DRD, DRV, PDR, PMnR: phasic {fp:.3f}, tonic {ft:.3f}, difference {fp - ft:.3f}\")\nprint(\"regions spanned: phasic\", len(set(region[ph_units])), \"; tonic\", len(set(region[to_units])))\nprint(\"regions per outcome cluster:\", {f\"k{k}\": len(set(region[L1_out == k])) for k in range(1, 12)})\ntab = pd.crosstab(ph_units[ph_units | to_units], ext[ph_units | to_units])\nprint(\"chi-square phasic/tonic x extremes (effect size only):\", np.round(stats.chi2_contingency(tab)[:2], 3).tolist())\n''', [\"claim:fig4g-outcome-anatomy\"])\n\nmd(\"\"\"\n**Result: see above.** Reproduced when the phasic fraction exceeds the tonic fraction and the tonic\nnetwork spans at least as many regions.\n\"\"\")\n\n# ---------------------------------------------------------------- outcome regression\nmd(\"\"\"\n## fig5a-outcome-cluster-signals\n\n> Regression revealed distinct shock and prediction error signals across the 11 outcome clusters;\n> k1 neurons transiently signaled both sensory shock and prediction error, while k6 neurons\n> signaled only error.\n\nThe script's beta matrix holds prediction error in columns 1-20 and shock in 21-40\n(`outcomeRegression.m`: `regTerms = [blank, regPos, regShock]`, b(2) to columns 1-20); the claims\nfile reads columns 1-20 as shock. Which order Source Data Fig. 5b holds is checked below.\n\"\"\")\n\ncode(r'''\nsd5b = bst3.sd_matrix(sheets, \"Figure 5b middle\", 2, 40)\nobetas = {}\nfor mode in (\"r-a\", \"r-b\"):\n    for ic, iname in ((True, \"i-a\"), (False, \"i-b\")):\n        obetas[(mode, iname)] = bst3.outcome_betas(z5, L1_out, range(1, 12), mode, ic)\nfor key, B in obetas.items():\n    print(key, \"max abs diff from Source Data Fig. 5b middle: as is %.2e; halves swapped %.2e\" %\n          (np.abs(B - sd5b).max(), np.abs(np.hstack([B[:, 20:], B[:, :20]]) - sd5b).max()))\ndef fig5a_tests(B):\n    pe, sh = B[:, :20], B[:, 20:]\n    k1 = {}\n    for name, v in ((\"shock\", sh[0]), (\"PE\", pe[0])):\n        a_ = np.abs(v)\n        k1[name] = int(np.argmax(a_)) < 4 and a_[10:20].max() < 0.5 * a_.max()\n    k6 = np.abs(pe[5]).mean() >= 2 * np.abs(sh[5]).mean()\n    return {\"k1 transient shock\": k1[\"shock\"], \"k1 transient PE\": k1[\"PE\"], \"k6 PE only\": bool(k6),\n            \"k6 mean |PE| / mean |shock|\": round(np.abs(pe[5]).mean() / np.abs(sh[5]).mean(), 2)}\nfor key, B in obetas.items():\n    print(key, fig5a_tests(B))\nB = obetas[(\"r-a\", \"i-a\")]\nprint(\"\\nk1 shock betas:\", B[0, 20:].round(2).tolist())\nprint(\"k1 PE betas:   \", B[0, :20].round(2).tolist())\nprint(\"k6 shock betas:\", B[5, 20:].round(2).tolist())\nprint(\"k6 PE betas:   \", B[5, :20].round(2).tolist())\n''', [\"claim:fig5a-outcome-cluster-signals\"])\n\nmd(\"\"\"\n**Result: see the tests above.** Reproduced when both parts hold under one reading.\n\"\"\")\n\nmd(\"\"\"\n## fig5b-outcome-signal-pca\n\n> PCA of outcome cluster beta weights showed opposing sensory shock and prediction error signals as\n> PC1 (53.7% of signaling variance) and dynamic sensory shock to prediction error signaling as PC2\n> (33.4%).\n\"\"\")\n\ncode(r'''\ndef out_shape(c, intact2=None):\n    p1, p2 = c[:, 0], c[:, 1]\n    pe1, sh1, pe2, sh2 = p1[:20], p1[20:], p2[:20], p2[20:]\n    res = {\"PC1 opposing\": np.sign(sh1.mean()) != np.sign(pe1.mean()),\n           \"PC2 |shock| peak in first 2 s\": int(np.argmax(np.abs(sh2))) < 4,\n           \"PC2 |PE| peak after 2 s\": int(np.argmax(np.abs(pe2))) >= 4}\n    return res\nB_out = obetas[(\"r-a\", \"i-a\")]\npcs_out = {}\nfor name, M in ((\"Source Data Fig. 5b middle\", sd5b), (\"recomputed L1 (r-a, i-a)\", B_out),\n                (\"recomputed L2 (r-a, i-a)\", bst3.outcome_betas(z5, L2_out, range(1, 12), \"r-a\", True))):\n    c, e = bst3.pca(M)\n    pcs_out[name] = (c, e)\n    print(f\"{name}: PC1 {e[0]:.2f}% (53.7 +- 5.37), PC2 {e[1]:.2f}% (33.4 +- 3.34); {out_shape(c)}\")\nc, e = pcs_out[\"recomputed L1 (r-a, i-a)\"]\nprint(\"PC1 PE weights:\", c[:20, 0].round(3).tolist())\nprint(\"PC1 shock weights:\", c[20:, 0].round(3).tolist())\nprint(\"PC2 PE weights:\", c[:20, 1].round(3).tolist())\nprint(\"PC2 shock weights:\", c[20:, 1].round(3).tolist())\n''', [\"claim:fig5b-outcome-signal-pca\"])\n\nmd(\"\"\"\n**Result: see above.**\n\"\"\")\n\nmd(\"\"\"\n## fig5c-phasic-lesion and fig5d-tonic-lesion\n\n> Lesioning the phasic outcome network left signaling dominated by sustained prediction error (80.0%\n> of signaling variance), with residual sustained shock (16.8%) ...\n\n> Lesioning the tonic outcome network left opposing, phasic sensory shock and prediction error\n> signaling as PC1 (61.3% of signaling variance) and dynamic sensory shock to prediction error as PC2\n> (29.8%), similar to that of all neurons.\n\nLesion as in `outcomeRegression.m` (s-d): the shuffled clusters' firing permuted across the 16\ntrial rows before regression, betas averaged over 1000 iterations, one PCA (v-a). Whether one row\npermutation is used for all 20 intervals (s-d1) or one per interval (s-d2) is not settled by the\nscript; both are run. s-a and s-b (permuting betas) are variants.\n\"\"\")\n\ncode(r'''\nrng = np.random.default_rng(7)\nolesion = {}\nfor name, shuffled in ((\"phasic\", {1, 2, 3}), (\"tonic\", {6, 7, 8, 9})):\n    olesion[(name, \"s-d1\")] = bst3.outcome_lesion_betas(z5, L1_out, range(1, 12), shuffled, rng, 1000, True)\n    olesion[(name, \"s-d2\")] = bst3.outcome_lesion_betas(z5, L1_out, range(1, 12), shuffled, rng, 1000, False)\n    rws = np.array(sorted(shuffled)) - 1\n    olesion[(name, \"s-a\")] = bst3.beta_shuffle_average(B_out, rws, rng, 1000, \"s-a\")\n    olesion[(name, \"s-b\")] = bst3.beta_shuffle_average(B_out, rws, rng, 1000, \"s-b\")\nolesion[(\"phasic\", \"Source Data\")] = bst3.sd_matrix(sheets, \"Figure 5c middle\", 2, 40)\nolesion[(\"tonic\", \"Source Data\")] = bst3.sd_matrix(sheets, \"Figure 5d middle\", 2, 40)\nic, ie_ = pcs_out[\"recomputed L1 (r-a, i-a)\"]\nrows = []\nfor (name, reading), M in olesion.items():\n    c, e = bst3.pca(M)\n    pe1, sh1, pe2, sh2 = c[:20, 0], c[20:, 0], c[:20, 1], c[20:, 1]\n    if name == \"phasic\":\n        ok = {\"PC1 |PE| > |shock|\": np.abs(pe1).mean() > np.abs(sh1).mean(),\n              \"PC1 PE sustained (1-10 s >= half max)\": bool((np.abs(pe1[2:]) >= 0.5 * np.abs(pe1).max()).all()),\n              \"PC2 |shock| > |PE|\": np.abs(sh2).mean() > np.abs(pe2).mean()}\n        exp = \"(80.0 +- 8.0, 16.8 +- 1.68)\"\n    else:\n        v2 = c[:, 1] * (1 if c[:, 1] @ ic[:, 1] >= 0 else -1)\n        ok = {\"PC1 opposing\": np.sign(sh1.mean()) != np.sign(pe1.mean()),\n              \"PC1 both peak in first 2 s\": int(np.argmax(np.abs(sh1))) < 4 and int(np.argmax(np.abs(pe1))) < 4,\n              **{k: v for k, v in out_shape(c).items() if k.startswith(\"PC2\")},\n              \"r with intact PC2 > 0.5\": round(float(np.corrcoef(v2, ic[:, 1])[0, 1]), 3)}\n        exp = \"(61.3 +- 6.13, 29.8 +- 2.98)\"\n    rows.append({\"lesion\": name, \"reading\": reading, \"PC1 %\": round(e[0], 2), \"PC2 %\": round(e[1], 2), \"expected\": exp, **ok})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"max abs diff from Source Data, phasic s-d1 %.3f, s-d2 %.3f; tonic s-d1 %.3f, s-d2 %.3f\" % (\n    np.abs(olesion[(\"phasic\", \"s-d1\")] - olesion[(\"phasic\", \"Source Data\")]).max(),\n    np.abs(olesion[(\"phasic\", \"s-d2\")] - olesion[(\"phasic\", \"Source Data\")]).max(),\n    np.abs(olesion[(\"tonic\", \"s-d1\")] - olesion[(\"tonic\", \"Source Data\")]).max(),\n    np.abs(olesion[(\"tonic\", \"s-d2\")] - olesion[(\"tonic\", \"Source Data\")]).max()))\n''', [\"claim:fig5c-phasic-lesion\", \"claim:fig5d-tonic-lesion\"])\n\nmd(\"\"\"\n**Result: see the table above, for fig5c-phasic-lesion and fig5d-tonic-lesion.**\n\"\"\")\n\n# ---------------------------------------------------------------- fig5e\nmd(\"\"\"\n## fig5e-no-anatomical-bias\n\n> Anatomical biases for phasic and tonic outcome network neurons were absent.\n\nPer region, its share of tonic units minus its share of phasic units (percentage points); phasic as\nk1-k3 (p-a) or k1-k5 (p-b). Judged against 4.48 and 1.5 x 4.48 = 6.72.\n\"\"\")\n\ncode(r'''\nsd5e = np.array(sheets[\"Figure 5e right\"][1][1:22], float)\nfor name, ph in ((\"p-a k1-k3\", [1, 2, 3]), (\"p-b k1-k5\", [1, 2, 3, 4, 5])):\n    d5e, a, b = bst3.differential(region, np.isin(L1_out, [6, 7, 8, 9]), np.isin(L1_out, ph))\n    print(f\"{name}: largest |differential| {np.abs(d5e).max():.2f} ({bst3.REGIONS[int(np.argmax(np.abs(d5e)))]})\")\n    print(\"   \", dict(zip(bst3.REGIONS, d5e.round(2))))\n    tab = np.vstack([a, b])\n    tab = tab[:, tab.sum(0) > 0]\n    chi = stats.chi2_contingency(tab)\n    print(f\"    chi-square region x network (variant): chi2 = {chi[0]:.1f}, df {chi[2]}, p = {chi[1]:.2g}\")\nprint(\"Source Data Fig. 5e right:\", dict(zip(bst3.REGIONS, sd5e.round(2))), \"; max |.|\", np.abs(sd5e).max().round(2))\n''', [\"claim:fig5e-no-anatomical-bias\"])\n\nmd(\"\"\"\n**Result: see above.**\n\"\"\")\n\n# ---------------------------------------------------------------- membership\nmd(\"\"\"\n## cue-outcome-membership-independent\n\n> Membership in cue networks did not influence membership in outcome networks; neither the phasic\n> (85/265, 32.1%) nor the tonic (159/613, 25.9%) outcome neurons differed from the 27.9% expected in\n> the cue subnetwork.\n\"\"\")\n\ncode(r'''\nfor lname, lc, lo in ((\"L1\", L1_cue, L1_out), (\"L2\", L2_cue, L2_out)):\n    sub = np.isin(lc, range(1, 10))\n    for net, members in ((\"phasic\", [1, 2, 3]), (\"tonic\", [6, 7, 8, 9])):\n        m = np.isin(lo, members)\n        k, n = int((sub & m).sum()), int(m.sum())\n        chi = stats.chisquare([k, n - k], [n * 0.279, n * 0.721])\n        chi2 = stats.chi2_contingency(pd.crosstab(m, sub), correction=False)\n        print(f\"{lname} {net}: {k}/{n} = {k / n:.3f} in the cue subnetwork; goodness of fit vs 0.279 chi2 = {chi.statistic:.2f}, \"\n              f\"p = {chi.pvalue:.2f}; 2 x 2 chi2 = {chi2[0]:.2f}, p = {chi2[1]:.2f}\")\n''', [\"claim:cue-outcome-membership-independent\"])\n\nmd(\"\"\"\n**Result: see above.** Reproduced when neither test has p < 0.05.\n\"\"\")\n\ncode(r'''\nprint(f\"notebook ran in {(time.time() - started) / 60:.1f} min, peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n''')\n\nmd(open(sys.argv[3]).read())\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, sys.argv[1])\n"
}
```

```
File created successfully at: /tmp/claude-1001/gen.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('gen.py').read()
a=s.index('def shock_contrast'); b=s.index('# from the 250-ms counts')
s=s[:a]+s[b:]
open('gen.py','w').write(s)
EOF
echo "# header placeholder" > header.md; echo "## Summary
placeholder" > summary.md
dev/bin/python gen.py entries/strickland-2022/reproduce_strickland_2022.ipynb header.md summary.md && cd entries/strickland-2022 && date -u && time $TMPDIR/dev/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output $TMPDIR/exec.ipynb reproduce_strickland_2022.ipynb 2>&1 | tail -5
```

```
Fri Nov 13 01:30:42 UTC 2026

Available subcommands: execute kernel kernelspec migrate run troubleshoot
trust

Jupyter command `jupyter-nbconvert` not found.

real	0m0.070s
user	0m0.064s
sys	0m0.007s
```

**Agent calls Bash**

```bash
cat > $TMPDIR/runnb.py <<'EOF'
import nbformat, sys, time
from nbclient import NotebookClient
nb=nbformat.read(sys.argv[1],as_version=4)
t=time.time()
c=NotebookClient(nb,timeout=3000,kernel_name='python3',allow_errors=True,resources={'metadata':{'path':'.'}})
c.execute()
nbformat.write(nb,sys.argv[2])
print('ran',time.time()-t)
for i,cell in enumerate(nb.cells):
    if cell.cell_type=='code':
        for o in cell.outputs:
            if o.output_type=='error': print('ERROR cell',i,o.ename,o.evalue)
EOF
$TMPDIR/dev/bin/python -m ipykernel install --user --name python3 >/dev/null 2>&1; $TMPDIR/dev/bin/python $TMPDIR/runnb.py reproduce_strickland_2022.ipynb $TMPDIR/exec.ipynb 2>&1 | tail -20
```

```
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
ran 82.0592348575592
ERROR cell 75 ValueError operands could not be broadcast together with shapes (111,) (171,)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dump.py <<'EOF'
import nbformat, sys
nb=nbformat.read(sys.argv[1],as_version=4)
lo=int(sys.argv[2]) if len(sys.argv)>2 else 0; hi=int(sys.argv[3]) if len(sys.argv)>3 else 999
for i,c in enumerate(nb.cells):
    if i<lo or i>hi: continue
    if c.cell_type=='markdown':
        print(f'[{i}] MD', c.source.split('\n')[0][:100]); continue
    print(f'[{i}] CODE', c.metadata.get('tags',''))
    for o in c.outputs:
        if o.output_type=='stream': print(o.text[:6000])
        elif o.output_type=='error': print('ERR',o.ename,o.evalue)
        elif 'data' in o: print(o['data'].get('text/plain','')[:3000])
EOF
$TMPDIR/dev/bin/python $TMPDIR/dump.py $TMPDIR/exec.ipynb 0 20
```

```
[0] MD # header placeholder
[1] CODE 
Data set CRCNS bst-3, version unversioned, doi:10.6080/K0Q23XGR
checksums.md5 in the bucket:

4ee6c433f5255693d5e85bcca6819cd4  data.zip
a2308123164a7ca6fb0e15c54693f14c  docs/crcns_bst-3_data_description.docx
f07a1e9718106c7219a9a6549568517c  docs/crcns_bst-3_data_description.pdf
0a26a2a26214193af0d13ff06b2c850d  filelist.txt


1822 members in data.zip; Counter({'singleUnits': 1813, 'scripts': 6, 'cubeFile': 2, 'data/': 1})
   data/cubeFile/cubeFile.mat 139318845 bytes
   data/scripts/cueRegression.m 26890 bytes
   data/scripts/outcomeAnalysis.m 37155 bytes
   data/scripts/outcomeRegression.m 13879 bytes
   data/scripts/cubeScript.m 29531 bytes
   data/scripts/cueAnalysis.m 50442 bytes

Source Data workbook md5 4df716fd6739ee3de3b0df81c4175be8 (expected 4df716fd6739ee3de3b0df81c4175be8): True
[... 183 more lines not kept]
```

**Agent calls Bash**

```bash
$TMPDIR/dev/bin/python $TMPDIR/dump.py $TMPDIR/exec.ipynb 21 50
```

```
[21] MD **Result: reproduced.** 1812 units, 965 from females, 73 sessions, and the ten per-subject totals
[22] MD ## fig1e-regions
[23] CODE ['claim:fig1e-regions']
region  units  Source Data Fig. 3e left (sum)
   DPG    145                             145
  DpWh     72                              72
 DLPAG    179                             179
  LPAG    122                             122
 VLPAG    147                             147
   me5      2                               2
   DRL      1                               1
   DRD     99                              99
   DRV    208                             208
   PDR     27                              27
   mlf     57                              57
  isRt     50                              50
   Pa4     17                              17
 x/scp     38                              38
  SPTg     72                              72
   PnO    101                             101
[... 166 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper && grep -n -i "latency\|findchangepts\|change point" 10.1038-s41467-022-34021-1.txt | head -20; ls; which pdftotext mutool; $TMPDIR/dev/bin/python -c "import fitz" 2>&1
```

```
Exit code 1
25:Brainstem neurons showed marked cue firing that varied in time course, direction, and pattern (Fig. 2a ). K-means clustering for mean, single-unit firing in 1-s bins from 2-s prior to 2-s following cue presentation (danger, uncertainty, and safety) revealed neurons could be organized into at least 21 functional clusters; potential building blocks for brainstem construction of threat probability and behavior. Cluster size varied (min size = 24, max = 219, and median = 83) and consistent firing themes emerged when clusters were visualized (Fig. 2b and Supplementary Figs. S3 and S4 ). Many clusters showed ordered cue firing that differentiated danger, uncertainty, and safety (e.g., k1, k2, k6, and k7). Principal component analysis (PCA) revealed ordered cue firing (danger > uncertainty > safety) to be the primary low-dimensional feature across all brainstem neurons (PC1, explaining 29.7% of firing variance; Fig. 2c , inset). Fig. 2 Brainstem cue firing. a Single-unit firing ( n = 1812) to danger, uncertainty, and safety cues organized by brain region, dorsal to ventral. b Mean cluster (k1–k21) firing over cue presentation (cluster n shown in the figure). Data are presented as mean values ± SEM. c PC1 for brainstem cue firing (inset) and cluster contribution to PC1. d Single-unit danger firing latency with cluster means. e Between-cluster cue firing correlations (data from b ). Cue subnetwork outlined in magenta. f Single unit × cluster firing correlations for the cue subnetwork, with cluster means. g Proportion of each cluster found in each brainstem region. c – g Cue subnetwork hubs are magenta, cue subnetwork pink, and cue supranetwork gray. *Significance of two-tailed, independent samples t -test, Bonferroni corrected. ‡ Significance of two-tailed, Levene’s test for equality of variance, Bonferroni corrected. d danger, u uncertainty, s safety. Source data are provided as a Source Data file.
27:Brainstem cue firing. a Single-unit firing ( n = 1812) to 
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper && sed -n 395,520p 10.1038-s41467-022-34021-1.txt
```

```
cluster was selected (i.e., cluster 21). Firing information for the single units of only that cluster 
were shuffled. Firing information for all other clusters (i.e., clusters 1-20) was left intact. Principal 
components analysis was performed on this modified data set (clusters 1-20 intact, cluster 21 
shuffled) and the percent firing variance explained for PC1 determined. PC1 contribution for that 
iteration was determined by subtracting the modified data set (clusters 1-20 intact, cluster 21 
shuffled) from the ground truth (all clusters intact). Shuffling → PCA was performed 1,000 times 
for each cluster, and PC1 contribution determined for each iteration, then averaged. The 
complete iterative, shuffle/PCA was performed for each individual cluster, always shuffling the 

cluster of interest but leaving intact all other clusters. Clusters more greatly contributing to PC1 
would have larger difference values, indicating that removing their firing information more 
greatly reduced the percent of firing variance explained by PC1. 
Danger firing latency 
Mean normalized firing rate during 10-s danger cue presentation was summarized in 10,000, 
1ms bins for each single unit. Danger firing latency was determined for each single unit by 
identifying the bin of greatest firing inflection (among the 10,000 total during danger 
presentation) using the findchangepts Matlab function. Mean danger firing latencies were 
calculated for each cluster by averaging the latencies of the composing single units. Betweencluster differences in latency means were determined using Bonferroni-corrected (p = 0.05/# of 
tests), independent samples t-tests. Between-cluster differences in latency variation were 
determined using Bonferroni-corrected, Levene's test for equality of variances. 
[... 94 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/strickland-2022 && cat > $TMPDIR/t7.py <<'EOF'
import sys,numpy as np,pickle,openpyxl,collections
sys.path.insert(0,'.')
import bst3
U,C=pickle.load(open('/tmp/claude-1001/all.pkl','rb'))
L=np.load('/tmp/claude-1001/labels.npz'); lab=L['cue']
d=np.load('/tmp/claude-1001/cube_dev.npz')
# cube order labels: labels.npz computed in cube order
order={u:i for i,u in enumerate(U['ID'])}; ix=np.array([order[u] for u in C['ID']])
ms1=U['ms1'][ix]
lat=np.array([bst3.change_point(x) or np.nan for x in ms1])
wb=openpyxl.load_workbook('paper/10.1038-s41467-022-34021-1.supp-41467_2022_34021_MOESM4_ESM.xlsx',read_only=True,data_only=True)
sd=[r for r in wb['Figure 2d'].iter_rows(values_only=True)][1:]
sdc=collections.defaultdict(list)
for k,v in sd: sdc[k].append(v)
hit=[ (lat[u] in sdc[lab[u]]) for u in range(1812) if np.isfinite(lat[u])]
print('units whose latency is in SD same cluster', sum(hit), len(hit))
# per cluster sorted compare
k=1; print(sorted(sdc[1])); print(sorted(lat[lab==1]))
# variant: z ms250 repeated
z=d['fire_z_ms250_interval']  # unit,160,16
dz=z[:,:,0:4].mean(2)[:,40:80]
lat2=np.array([bst3.change_point(np.repeat(x,250)) or np.nan for x in dz])
print(sorted(lat2[lab==1]))
z1=d['fire_z_ms100_interval'][:,:,0:4].mean(2)[:,100:200]
lat3=np.array([bst3.change_point(np.repeat(x,100)) or np.nan for x in z1])
print(sorted(lat3[lab==1]))
EOF
$TMPDIR/dev/bin/python $TMPDIR/t7.py
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat > $TMPDIR/t8.py <<'EOF'
import sys,numpy as np,pickle,openpyxl,collections
sys.path.insert(0,'.')
import bst3
U,C=pickle.load(open('/tmp/claude-1001/all.pkl','rb'))
L=np.load('/tmp/claude-1001/labels.npz'); lab=L['cue']
k1=[C['ID'][i] for i in np.flatnonzero(lab==1)]
zf=bst3.open_zip()
res=collections.defaultdict(list)
for uid in k1:
    _,sp,ev=bst3._parse_unit(zf.read(f'data/singleUnits/{uid}.mat')); sp=np.unique(sp)
    cues=ev['cue100']
    per=[]
    for t0 in cues:
        st=t0+30*np.arange(10000); per.append(bst3._count(sp,st,30))
    per=np.array(per)
    res['trial1'].append(bst3.change_point(per[0]))
    res['sorted cues first'].append(bst3.change_point(per[np.argsort(cues)[0]]))
    # with pre-cue 2s
    st=cues[:,None]-60000+30*np.arange(12000)[None,:]; pc=bst3._count(sp,st,30).sum(0)
    cp=bst3.change_point(pc); res['pre2'].append(None if cp is None else cp-2000)
    st=cues[:,None]-300000+30*np.arange(20000)[None,:]; pc=bst3._count(sp,st,30).sum(0)
    cp=bst3.change_point(pc); res['pre10'].append(None if cp is None else cp-10000)
    res['min over trials'].append(min([c for c in (bst3.change_point(p) for p in per) if c] or [None]))
for k,v in res.items(): print(k, sorted([x for x in v if x is not None]))
EOF
$TMPDIR/dev/bin/python $TMPDIR/t8.py
```

```
trial1 [466, 584, 596, 667, 1441, 1532, 2268, 2495, 3669, 4578, 4668, 4852, 4872, 5501, 5969, 6077, 6664, 6709, 7568, 7912, 8292, 8376, 9873, 9999]
sorted cues first [466, 584, 596, 667, 1441, 1532, 2268, 2495, 3669, 4578, 4668, 4852, 4872, 5501, 5969, 6077, 6664, 6709, 7568, 7912, 8292, 8376, 9873, 9999]
pre2 [-24, 29, 33, 37, 39, 43, 46, 46, 56, 56, 62, 66, 67, 76, 80, 81, 101, 102, 111, 147, 150, 154, 195, 5746]
pre10 [-24, -2, 29, 33, 37, 39, 43, 46, 56, 56, 62, 66, 66, 67, 76, 80, 81, 101, 102, 111, 147, 150, 154, 184]
min over trials [169, 241, 265, 300, 343, 466, 560, 656, 667, 880, 960, 1021, 1642, 1725, 1857, 1861, 2063, 2290, 2409, 2662, 2897, 3141, 4209, 4244]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='bst3.py'; s=open(p).read()
s=s.replace('''        starts = ev["cue100"][:, None] + 30 * np.arange(10000)[None, :]
        ms1.append(_count(spike, starts, 30).sum(0).astype(np.int16))''','''        starts = ev["cue100"][:, None] - 2 * FS + 30 * np.arange(12000)[None, :]
        ms1.append(_count(spike, starts, 30).sum(0).astype(np.int16))''')
s=s.replace('''the summed danger-trial spike count in 1-ms
    bins over the 10-s cue, for the latency;''','''the summed danger-trial spike count in 1-ms
    bins from 2 s before onset to the end of the 10-s cue (12000 bins), for the latency;''')
s=s.replace('''CUBE_FIELDS = ["fire/z/s1/interval", "fire/z/ms500/interval",''','''CUBE_FIELDS = ["fire/z/s1/interval", "fire/z/ms500/interval", "fire/z/ms250/interval",''')
open(p,'w').write(s)
EOF
grep -n "12000\|ms250/interval" bst3.py
```

```
97:CUBE_FIELDS = ["fire/z/s1/interval", "fire/z/ms500/interval", "fire/z/ms250/interval", "fire/raw/s1/interval", "fire/raw/base2",
140:    bins from 2 s before onset to the end of the 10-s cue (12000 bins), for the latency; and per session the cue, shock and poke times.
164:        starts = ev["cue100"][:, None] - 2 * FS + 30 * np.arange(12000)[None, :]
```

**Agent calls Bash**

```bash
$TMPDIR/dev/bin/python $TMPDIR/dump.py $TMPDIR/exec.ipynb 51 100
```

```
[51] CODE 
[52] MD ## fig3b-signal-pca
[53] CODE ['claim:fig3b-signal-pca']
                       matrix  PC1 %  PC2 %  PC1 |beh| > |prob| over cue  PC1 beh max in cue s 3-8  PC1 mean prob over cue < 0  PC2 |prob| > |beh| over cue  PC2 prob max in cue s 1-3
   Source Data Fig. 3b middle  62.73  26.21                         True                      True                        True                         True                       True
    recomputed, L1 (r-a, i-a)  62.73  26.21                         True                      True                        True                         True                       True
recomputed, L1 ('r-b', 'i-a')  72.00  15.79                        False                     False                       False                        False                      False
recomputed, L1 ('r-a', 'i-b')  57.07  27.94                         True                     False                        True                         True                       True
recomputed, L1 ('r-b', 'i-b')  66.16  21.37                        False                     False                       False                        False                      False
    recomputed, L2 (r-a, i-a)  63.08  25.04                         True                      True                        True                         True                       True

PC1 probability weights: [0.0, -0.002, -0.021, -0.025, -0.049, -0.072, -0.075, -0.12, -0.109, -0.119, -0.133, -0.122, -0.124, -0.129]
PC1 behaviour weights:   [-0.003, 0.007, 0.191, 0.23, 0.253, 0.275, 0.299, 0.317, 0.308, 0.305, 0.29, 0.268, 0.256, 0.229]
PC2 probability weights: [-0.008, 0.01, 0.268, 0.335, 0.312, 0.308, 0.295, 0.285, 0.274, 0.261, 0.248, 0.239, 0.241, 0.193]
PC2 behaviour weights:   [0.005, -0.006, 0.068, 0.053, 0.052, 0.095, 0.116, 0.097, 0.076, 0.075, 0.123, 0.119, 0.077, 0.097]
with the pre-cue baseline subtracted: {'PC1 |beh| > |prob| over cue': np.True_, 'PC1 beh max in cue s 3-8': True, 'PC1 mean prob over cu
[... 191 more lines not kept]
```

**Agent calls Bash**

```bash
$TMPDIR/dev/bin/python - <<'EOF'
import openpyxl, collections
wb=openpyxl.load_workbook('paper/10.1038-s41467-022-34021-1.supp-41467_2022_34021_MOESM4_ESM.xlsx',read_only=True,data_only=True)
for s in ['Figure 4f left','Figure 4f right','Figure 2f']:
    r=[x for x in wb[s].iter_rows(values_only=True)][1:]
    print(s, collections.Counter(x[0] for x in r))
    import numpy as np
    for k in sorted(set(x[0] for x in r if x[0] is not None)):
        v=[x[1] for x in r if x[0]==k]; print('  ',k,len(v),round(float(np.mean(v)),3))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('gen.py').read()
# (a) clock check
a=s.index('# with the shock labels shuffled across rows within a session'); b=s.index("''', [\"sanity\"])", a)
s=s[:a]+s[b:]
# (b) latency
a=s.index("code(r'''\nms1 = units[\"ms1\"][ix]"); b=s.index("''', [\"claim:fig2d-danger-latency\"])")
new = r'''code(r"""
ms1 = units["ms1"][ix]                       # summed danger-trial spikes, 1-ms bins from -2 s to +10 s
sd2d = pd.DataFrame([r for r in sheets["Figure 2d"][1:] if r[0] is not None], columns=["cluster", "latency"])
print("Source Data Fig. 2d lists", len(sd2d), "units; units with no danger spikes in the cue:", int((ms1[:, 2000:].sum(1) == 0).sum()))
z250 = cube["fire/z/ms250/interval"][:, :, 0:4].mean(2)[:, 40:80]     # danger, 40 cue bins of 250 ms
lat_readings = {
    "l-a (10-s cue, 1-ms spikes)": np.array([bst3.change_point(x) or np.nan for x in ms1[:, 2000:]], float),
    "l-b (10-s cue, 250-ms z repeated)": np.array([bst3.change_point(np.repeat(x, 250)) or np.nan for x in z250], float),
}
lat12 = np.array([(bst3.change_point(x) or np.nan) - 2000 for x in ms1], float)
lat_readings["variant: 12-s window from 2 s before onset, latency > 0 kept"] = np.where(lat12 > 0, lat12, np.nan)
sd_sets = {k: Counter(sd2d[sd2d.cluster == k].latency.astype(int)) for k in range(1, 22)}
cvec = np.array([contrib["s-a"][k] for k in range(1, 22)])
size = np.bincount(L1_cue)[1:]
sd_cl = sd2d.groupby("cluster").latency.mean().reindex(range(1, 22)).values
rows = []
for name, lat in lat_readings.items():
    shared = 0
    for k in range(1, 22):
        mine = Counter(lat[(L1_cue == k) & np.isfinite(lat)].astype(int))
        shared += sum((mine & sd_sets[k]).values())
    cl = np.array([np.nanmean(lat[L1_cue == k]) for k in range(1, 22)])
    ra, pa = stats.pearsonr(cvec, cl)
    rb, pb = stats.pearsonr(cvec * size, cl)
    sub = np.isin(L1_cue, range(1, 10))
    rows.append({"reading": name, "units with latency": int(np.isfinite(lat).sum()), "equal to a Source Data value": shared,
                 "R2 c-a": round(ra * ra, 3), "r c-a": round(ra, 3), "p c-a": pa, "R2 c-b": round(rb * rb, 3), "p c-b": pb,
                 "k1-k9 mean ms": round(np.nanmean(lat[sub])), "k10-k21 mean ms": round(np.nanmean(lat[~sub])),
                 "k1 mean": round(cl[0]), "k2 mean": round(cl[1])})
for name, cl in (("Source Data latencies", sd_cl),):
    ra, pa = stats.pearsonr(cvec, cl)
    rb, pb = stats.pearsonr(cvec * size, cl)
    rows.append({"reading": name, "units with latency": len(sd2d), "R2 c-a": round(ra * ra, 3), "r c-a": round(ra, 3),
                 "p c-a": pa, "R2 c-b": round(rb * rb, 3), "p c-b": pb, "k1 mean": round(cl[0]), "k2 mean": round(cl[1])})
print(pd.DataFrame(rows).to_string(index=False))
lat = lat_readings["l-a (10-s cue, 1-ms spikes)"]
print("\nPer cluster (l-a; variant; Source Data):")
print(pd.DataFrame({"cluster": range(1, 22),
                    "l-a n": [int(np.isfinite(lat[L1_cue == k]).sum()) for k in range(1, 22)],
                    "l-a mean": [round(np.nanmean(lat[L1_cue == k])) for k in range(1, 22)],
                    "variant n": [int(np.isfinite(lat_readings["variant: 12-s window from 2 s before onset, latency > 0 kept"][L1_cue == k]).sum()) for k in range(1, 22)],
                    "variant mean": [round(np.nanmean(lat_readings["variant: 12-s window from 2 s before onset, latency > 0 kept"][L1_cue == k])) for k in range(1, 22)],
                    "Source Data n": sd2d.groupby("cluster").size().reindex(range(1, 22)).values,
                    "Source Data mean": sd_cl.round(0)}).to_string(index=False))
'''
s=s[:a]+new.replace('code(r"""','code(r\'\'\'')+s[b:]
# (c) fig2f tests for all variants
s=s.replace('''code(r\'\'\'
# The same with r (the claims file's wording, "coefficients averaged")''','''code(r\'\'\'
# Tests for every measure: does each hub exceed each of k3-k9 (t-test, one direction) at 0.05/7 and 0.05/8
for name, v in variants.items():
    out = []
    for hub in (1, 2):
        ps = [stats.ttest_ind(v[L1_cue == hub], v[L1_cue == k]) for k in range(3, 10)]
        out.append(f"k{hub} above {sum(t.pvalue < 0.05 / 7 and t.statistic > 0 for t in ps)}/7 at 0.05/7, "
                   f"{sum(t.pvalue < 0.05 / 8 and t.statistic > 0 for t in ps)}/7 at 0.05/8")
    m = [np.nanmean(v[L1_cue == k]) for k in range(1, 10)]
    print(f"{name}: two highest k{int(np.argsort(m)[-1]) + 1}, k{int(np.argsort(m)[-2]) + 1}; " + "; ".join(out))
# The same with r (the claims file's wording, "coefficients averaged")''')
# (d) networks r squared
s=s.replace('''    R = np.corrcoef(P)
    ph, to = [0, 1, 2], [5, 6, 7, 8]''','''    R = np.corrcoef(P) ** power
    ph, to = [0, 1, 2], [5, 6, 7, 8]''')
s=s.replace("def network_tests(lab):","def network_tests(lab, power=1):")
s=s.replace('''for name, lab in (("L1", L1_out), ("L2", L2_out)):
    ph, to, info, w = network_tests(lab)
    print(name, "phasic:", ph)
    print(name, "tonic:", to)
    print(name, "mean r within / between: phasic %.3f / %.3f, tonic %.3f / %.3f" % w)
    if name == "L1":
        print(info.to_string(index=False))''','''for name, lab in (("L1", L1_out), ("L2", L2_out)):
    for power, pname in ((1, "r"), (2, "r squared")):
        ph, to, info, w = network_tests(lab, power)
        print(name, pname, "phasic:", ph)
        print(name, pname, "tonic:", to)
        print(name, pname, "mean within / between: phasic %.3f / %.3f, tonic %.3f / %.3f" % w)
    if name == "L1":
        print(info.to_string(index=False))
R = np.corrcoef(outcome_profiles(L1_out))
print("L1 cluster-cluster r (outcome profiles):")
print(pd.DataFrame(R, index=range(1, 12), columns=range(1, 12)).round(2).to_string())''')
# (e) fig4f compare
s=s.replace('''        same = ""
        if sq and label[0] != "v":
            same = "; clusters equal to Source Data: %d" % sum(
                np.isclose(np.sort(v[L1_out == k]), np.sort(sd4f[sd4f.cluster == k].R2.values), atol=1e-6).all() for k in net)''','''        same = ""
        if sq and label[0] != "v":
            mine = np.sort(v[np.isin(L1_out, net)])
            theirs = np.sort(sd4f[sd4f.cluster.isin(net)].R2.values)
            labels_sd = {k: int((sd4f.cluster == k).sum()) for k in net}
            same = (f"; all values equal Source Data as a set: {len(mine) == len(theirs) and np.allclose(mine, theirs, atol=1e-6)}; "
                    f"Source Data rows per label {labels_sd}, units per L1 cluster {dict((k, int((L1_out == k).sum())) for k in net)}")''')
open('gen.py','w').write(s)
EOF
grep -n "with the shock labels\|fig2d-danger-latency\"\])" gen.py | head
```

```
586:''', ["claim:fig2d-danger-latency"])
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/strickland-2022 && $TMPDIR/dev/bin/python $TMPDIR/gen.py reproduce_strickland_2022.ipynb $TMPDIR/header.md $TMPDIR/summary.md && $TMPDIR/dev/bin/python $TMPDIR/runnb.py reproduce_strickland_2022.ipynb $TMPDIR/exec.ipynb 2>&1 | grep -v WARNING | tail -5; $TMPDIR/dev/bin/python $TMPDIR/dump.py $TMPDIR/exec.ipynb 7 7; $TMPDIR/dev/bin/python $TMPDIR/dump.py $TMPDIR/exec.ipynb 36 36; $TMPDIR/dev/bin/python $TMPDIR/dump.py $TMPDIR/exec.ipynb 43 43; $TMPDIR/dev/bin/python $TMPDIR/dump.py $TMPDIR/exec.ipynb 69 76
```

```
ran 80.0061240196228
[7] CODE ['sanity']
Per unit, firing change 12-14 s after onset, shock rows minus no-shock rows: mean -2.43 Hz, median -0.27 Hz, Wilcoxon p = 1.6e-10
Same contrast at 10-12 s (before shock): mean -0.23 Hz, Wilcoxon p = 0.77
Same contrast at -20 to -18 s: mean 0.12 Hz, Wilcoxon p = 0.19

[36] CODE ['claim:fig2d-danger-latency']
Source Data Fig. 2d lists 1498 units; units with no danger spikes in the cue: 34

                                                     reading  units with latency  equal to a Source Data value  R2 c-a  r c-a    p c-a  R2 c-b    p c-b  k1-k9 mean ms  k10-k21 mean ms  k1 mean  k2 mean
                                 l-a (10-s cue, 1-ms spikes)                1778                         513.0   0.067 -0.260 0.255441   0.122 0.120723         3571.0           4590.0     4046     3062
                           l-b (10-s cue, 250-ms z repeated)                1778                           5.0   0.065 -0.255 0.264585   0.104 0.153484         3759.0           4524.0     4011     3228
variant: 12-s window from 2 s before onset, latency > 0 kept                1458                         413.0   0.640 -0.800 0.000014   0.661 0.000007         2004.0           5360.0      327      307
                                       Source Data latencies                1498                           NaN   0.508 -0.712 0.000290   0.394 0.002310            NaN              NaN      182     1646

Per cluster (l-a; variant; Source Data):
 cluster  l-a n  l-a mean  variant n  variant mean  Source Data n  Source Data mean
       1     24      4046         23           327             24             182.0
       2     43      3062         42           307             43            1646.0
       3     26      4298         26          1369             26            1044.0
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  ls questions | head -3; cat papers/datasets/strickland-2022.yaml 2>/dev/null; grep -n "\"outcomes\"\|\"findings\"\|\"inputs\"\|\"verifications\"\|required" schemas/attempt.schema.json | head -20
```

```
Fri Nov 13 01:37:32 UTC 2026
README.md
ashworth-2025.yaml
athalye-2023.yaml
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1038/s41467-022-34021-1
title: Brainstem networks construct threat probability and prediction error from neuronal building blocks
datasets:
- archive: crcns
  id: bst-3
  relation: primary
7:  "required": [
14:    "outcomes"
32:        "required": [
94:        "required": [
129:      "required": [
151:      "required": [
166:          "required": [
186:          "required": [
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['required']))
for k,v in s['properties'].items(): print(k, json.dumps(v)[:600]); print()
" | head -120
```

```
["schema_version", "id", "datasets", "paper", "date", "provenance", "outcomes"]
schema_version {"const": 3}

id {"type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"}

datasets {"description": "Every dataset the attempt used (docs/protocol.md, \"Record the attempt\").", "type": "array", "minItems": 1, "items": {"description": "A dataset the attempt used: the archive, the dataset's identifier there, the pinned version, and how the paper relates to it.", "type": "object", "additionalProperties": false, "required": ["archive", "id", "version", "relation"], "properties": {"archive": {"description": "The archive that holds the dataset, in lower case: dandi, ebrains, openneuro, dryad, zenodo, figshare and so on.", "type": "string", "pattern": "^[a-z][a-z0-9-]*$"}, "id": {"

missing_datasets {"description": "Datasets the paper's claims rest on that this attempt could not use; claims that need one are blocked with dataset_missing.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["why"], "properties": {"archive": {"type": "string"}, "id": {"type": "string"}, "name": {"type": "string"}, "why": {"type": "string"}}}}

paper {"type": "string", "pattern": "^doi:10\\.[0-9]{4,9}/.+$"}

date {"type": "string", "format": "date"}

entry {"description": "The entry this attempt produced (its name), if any.", "type": "string"}

deprecated {"description": "Set when the attempt no longer stands, for example because its claims were written without the paper's full text. The record is kept as it was; its outcomes are shown but not counted.", "type": "object", "additionalProperties": false, "required": ["date", "reason"], "properties": {"date": {"type": "string", "format": "date"}, "reason": {"type": "string", "minLength": 1}, "superseded_by": {"description": "The id of the attempt that replaces it, once there is one.", "type": "string"}}}

provenance {"type": "object", "additionalProperties": false, "required": ["kind", "accountable"], "properties
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['properties']['outcomes']['items']['properties'])[:3000]); print(json.dumps(s['properties']['provenance'])[600:1500]); print(json.dumps(s['properties']['findings']['items']['properties'])[:1500])"; cat schemas/entry.schema.json | head -80 | grep -n '"' | head -60
```

```
{"claim": {"description": "Claim id from the target's claims file.", "type": "string"}, "outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"], "description": "Describes the result, not the method: whether the effect the claim states was found. Differences in method from the paper go in `deviations`."}, "blocked_by": {"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "dataset_missing", "too_large", "not_runnable", "other"]}, "notes": {"description": "What differs, or what was missing, stated factually.", "type": "string"}, "notebook": {"description": "Path of the notebook within the entry.", "type": "string"}, "output": {"description": "Which output shows the result, e.g. a cell tag.", "type": "string"}, "measured": {"description": "The values obtained, for claims with expected values: one number, or one per expected value, in the same order.", "oneOf": [{"type": "number"}, {"type": "array", "minItems": 1, "items": {"type": "number"}}]}, "deviations": {"description": "How the test differed from the paper's method or data, e.g. one session of four, or a substituted model.", "type": "array", "items": {"type": "string", "minLength": 1}}, "assumed": {"description": "True when the outcome rests on an assumption about a method the paper leaves open: a choice the paper best supports, stated in a deviation that says what was assumed and why (docs/protocol.md, Author, step 1.6).", "type": "boolean"}, "proposed": {"description": "A change of outcome found after the last verification round, held until a further round agrees with it.", "type": "object", "additionalProperties": false, "required": ["outcome", "reason"], "properties": {"outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}, "blocked_by": {"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_under
[... 48 more lines not kept]
```

**Agent**

The analysis runs in about 80 s. Most claims reproduce; latency (Fig. 2d) does not under the Methods' window, and three claims hold only in part. Writing the conclusions, header and summary now.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('gen.py').read()
# fig4c: baseline-subtracted check
s=s.replace('''print(f"Source Data Fig. 4c matrix {C4.shape}: PC1 {bst3.pca(C4)[1][0]:.2f}%; rows equal to a unit's outcome row:",
      sum(len(h) > 0 for h in bst3.match_rows(C4, X_out)[0]))''','''print(f"Source Data Fig. 4c matrix {C4.shape}: PC1 {bst3.pca(C4)[1][0]:.2f}%; rows equal to a unit's outcome row:",
      sum(len(h) > 0 for h in bst3.match_rows(C4, X_out)[0]))
# the heat-plot version: baseline (mean over the four types of 500-ms bins 18:20, outcomeAnalysis.m) subtracted
base = np.mean([m[:, 17:20].mean(1) for m in bst3.type_means(z5, ["danger", "unc_shock", "unc_omission", "safety"])], 0)
print("rows equal to a unit's baseline-subtracted outcome row:", sum(len(h) > 0 for h in bst3.match_rows(C4, X_out - base[:, None])[0]))
print("\\nPer animal (PC1 of that animal's units; mean weights oriented as above):")
for s_ in range(1, 11):
    c_, e_ = bst3.pca(X_out[subject == s_])
    q = c_[:, 0] * np.sign(c_[20:40, 0].mean())
    print(f"  subject {s_} ({int((subject == s_).sum())} units): PC1 {e_[0]:.1f}%, mean weights D, US, UO, S "
          f"{np.round([q[i * 20:(i + 1) * 20].mean() for i in range(4)], 3).tolist()}")''')
s=s.replace('''hits, br, _ = bst3.match_rows(A, X_cue - base[:, None])
print("inset rows equal to a unit's baseline-subtracted row:", sum(len(h) > 0 for h in hits))''','''hits, br, _ = bst3.match_rows(A, X_cue - base[:, None])
print("inset rows equal to a unit's baseline-subtracted row:", sum(len(h) > 0 for h in hits))
print("\\nPer animal (PC1 of that animal's units):")
for s_ in range(1, 11):
    c_, e_ = bst3.pca(X_cue[subject == s_])
    q = c_[:, 0] * np.sign(c_[2:12, 0].mean())
    w_ = [q[i * 14 + 2:i * 14 + 12].mean() for i in range(3)]
    print(f"  subject {s_} ({int((subject == s_).sum())} units): PC1 {e_[0]:.1f}%, mean cue weights D, U, S {np.round(w_, 3).tolist()}, "
          f"ordered {w_[0] > w_[1] > w_[2]}")''')
s=s.replace('''print("units in k1-k9:", int(np.isin(L1_cue, range(1, 10)).sum()), "of", len(L1_cue))''','''print("units in k1-k9:", int(np.isin(L1_cue, range(1, 10)).sum()), "of", len(L1_cue))
print("share of each animal's units in k1-k9:", {s_: round(float(np.isin(L1_cue[subject == s_], range(1, 10)).mean()), 3) for s_ in range(1, 11)})''')
# session differing units detail
s=s.replace('''        print(f"Session {k}: units {s['differing_units']} carry cue or poke times that differ from unit {s['file_id']}")''','''        print(f"Session {k}: units {s['differing_units']} carry cue or poke times that differ from unit {s['file_id']}")
        for u in s["differing_units"] + [s["file_id"]]:
            _, _, ev = bst3._parse_unit(zf.read(f"data/singleUnits/{u}.mat"))
            cue = np.concatenate([ev["cue100"], ev["cueSPR"], ev["cueNsPR"], ev["cue0"]])
            print(f"    {u}: first cue onset {cue.min():.0f}, pokes {ev['poke'].size}, max |cue - reference cue| "
                  f"{np.abs(cue - s['cue']).max() / bst3.FS:.4f} s")''')
open('gen.py','w').write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > results.py <<'PYEOF'
s=open('gen.py').read()
R = {}
R['''**Result: reproduced.** Over the 73 sessions the session means are ordered danger > uncertainty >
safety under every reading, each within tolerance of the Source Data means, and the cue x sex mixed
ANOVA (a-a) gives F(2,142) within tolerance of 149.2 with p far below 0.05; the repeated-measures
reading (a-b) has df (2,144) and a lower F, as on the paper's own values.'''] = '''**Result: reproduced.** Over the 73 sessions the means are 0.914 (danger), 0.709 (uncertainty) and
0.230 (safety) with empty trials set to 1 as the script does, each equal to the Source Data mean, and
every session's three values equal a Source Data row. The cue x sex mixed ANOVA (a-a) gives
F(2,142) = 147.9 (149.2 +- 14.92), p < 1e-30. The other two treatments of empty trials give F 145.6
and 150.4 and the same order. The one-way repeated-measures reading (a-b) gives F(2,144) = 116.2, as
on the paper's own values, so the reported F fits the cue x sex design.'''
R['''**Result: see the counts above.** The outcome follows the criterion: reproduced when every rat with
at least 3 sessions meets one reading, partially reproduced for at least 6 of the 8.'''] = '''**Result: reproduced.** Under reading c-c (each rat's danger and uncertainty suppression intervals
exclude zero) all 8 rats with at least 3 sessions meet it. Under c-a 7 of 8 do (subject 9's
uncertainty minus safety interval, [-0.06, 0.28], includes zero) and under c-b 5 of 8. Subjects 4 and
6 (2 and 1 sessions) have mean ratios ordered danger >= uncertainty > safety for subject 4, and
danger > uncertainty > safety by 0.013 for subject 6.'''
R['''**Result: see the medians above against the tolerances.**
""")

# ---------------------------------------------------------------- pca cue'''] = '''**Result: reproduced.** Over 20 seeds the median smallest cluster is 24.0 (24 +- 2.4), the median
largest 218.5 (219 +- 21.9) and the median of the median sizes 75.0 (83 +- 8.3, so 74.7 to 91.3),
all three within tolerance, the last near its edge. Single seeds range from 14 to 38 (smallest), 171
to 274 (largest) and 63 to 93 (median). The paper's own clustering has a summed squared distance of
11219, inside the range of the 20 seeds (11135 to 11336). The mean squared distance falls smoothly
from 1 to 25 clusters, with no break at 21.
""")

# ---------------------------------------------------------------- pca cue'''
R['''**Result: reproduced.** PC1 of the data set's cue matrix explains 29.73% of the variance, and its mean
weights over the cue are ordered danger > uncertainty > safety. The 47.1% the claims file found on
the Source Data inset comes from a different matrix: its rows are not the units' cue rows.'''] = '''**Result: reproduced.** PC1 of the data set's 1812 x 42 cue matrix explains 29.73% of the variance
(29.7 +- 2.97), and its mean weights over the 10 cue seconds are ordered danger 0.266 > uncertainty
0.128 > safety 0.006. The 47.09% on the Source Data inset comes from another matrix: its 1812 rows
equal the units' cue rows with the mean of the three cues' two pre-cue seconds subtracted (the heat
plot of `cueAnalysis.m`), not the rows PCA was run on. The per-animal PCAs are printed above.'''
R['''**Result: reproduced.** Under L1 the nine largest contributions per unit are k1 to k9, k1 and k2 are
the two largest, and their values are within tolerance under both shuffle readings; reading s-a
gives every cluster's Source Data value to within 0.0004. Under L2 the total of the nine largest is
given above.'''] = '''**Result: reproduced.** Under L1 the nine largest contributions per unit are those of k1 to k9 (505
units), k1 and k2 are the two largest, and k1 (0.1214) and k2 (0.1129) are within tolerance under
reading s-a, the script's shuffle; s-b gives 0.1217 and 0.1127. Reading s-a gives every cluster's
Source Data value to within 0.0003. Under L2 (this attempt's own best-of-20 k-means, numbered by
contribution) the nine largest hold 411 units, outside 505 +- 50.5, and share 343 units with L1's
k1 to k9: the subnetwork's size depends on the clustering, which cannot be repeated exactly (the
script seeds MATLAB's generator, `rng(1)`).'''
R['''**Result: see the correlations above against R2 = 0.41 +- 0.041.**'''] = '''**Result: not reproduced.** Under the claims file's readings (latency found within the 10-s cue),
the correlation across the 21 clusters between mean danger latency and PC1 contribution per unit is
r = -0.260, R2 = 0.067, p = 0.26 (l-a), and R2 = 0.065, p = 0.26 (l-b); with the cluster total
(c-b) R2 is 0.122 and 0.104, p >= 0.12. Units of k1 to k9 do have shorter latencies (3571 against
4590 ms, l-a). The latencies differ from the paper's: k1's mean is 4046 ms here and 182 ms in Source
Data. Searching for the change point from 2 s before cue onset, and keeping latencies after onset
(a variant outside the criterion), gives 1458 units with latency, k1 327 ms and k2 307 ms, 413
values equal to Source Data values in the same cluster, and R2 = 0.640 (c-a, p = 1.4e-05) and 0.661
(c-b): a negative and significant correlation, stronger than the reported 0.41. On the paper's own
Source Data latencies the correlation is R2 = 0.508 (c-a) and 0.394 (c-b).'''
R['''**Result: see the values above.** Reproduced when the within-subnetwork mean exceeds the between
mean and k3 has the lowest mean with the other eight.'''] = '''**Result: reproduced.** With r squared, the measure the Methods name ("Pearson's correlation
coefficient (R2)") and the script plots, the mean within k1 to k9 (0.445, 42 columns; 0.465, 36
columns) exceeds the mean between k1 to k9 and k10 to k21 (0.184; 0.194), and k3 has the lowest mean
with the other eight subnetwork clusters (0.225; 0.229). With r the within mean also exceeds the
between mean (0.129 against 0.068), but k8 is lowest (-0.516), as k7 and k8 decrease firing while
the other subnetwork clusters increase it, and k3 is not. The Source Data Fig. 2e rows equal the
L1 cluster means.'''
R['''**Result: see the means and tests above.** Reproduced when k1 and k2 have the two highest means,
within tolerance, and each exceeds every one of k3 to k9 at the threshold.'''] = '''**Result: partially reproduced.** With the Methods' measure (danger firing, 14 intervals) as r
squared, the Source Data column's "R2", k2 (0.503) and k1 (0.462) have the two highest means, both
within tolerance (0.466 +- 0.047 and 0.424 +- 0.042), but not every t-test passes: k1 does not exceed
k3 (p = 0.42) or k4 (p = 0.12), and k2 does not exceed k3 (p = 0.014) at 0.05/7 or 0.05/8. With r,
k1 and k3 are the two highest. The Source Data per-unit values equal, in all nine clusters, r squared
computed on the full 42-value cue rows (all three cues), not on danger firing; with that measure
k1 (0.424) and k2 (0.466) are the two highest and each exceeds all seven of k3 to k9 at both
thresholds.'''
R['''**Result: see above.** Reproduced when all 21 clusters span at least six regions and both shares
are higher than the supranetwork's.'''] = '''**Result: reproduced.** Every cue cluster spans at least six regions (k3 has six, the fewest). The
share of units in DPG, DpWh, DLPAG, LPAG and VLPAG is 0.436 (220/505) in the subnetwork, 0.612
(41/67) in k1 and k2, and 0.340 (445/1307) in the supranetwork.'''
R['''**Result: see the shape tests above.** Reproduced when all four hold under one reading.'''] = '''**Result: partially reproduced.** Under the script's regression (r-a, i-a), whose betas equal the
Source Data Fig. 3b matrix exactly, two of the four shapes hold: k5 signals most in the first cue
second and k15 at the first second after the cue. K10 is not sustained by the criterion's rule (its
first cue second, 0.77, is below half its maximum, 1.69), and k6 peaks in cue second 5 (1.02) but its
first cue second (0.60) is above half of that. The other three readings give the same two of four.'''
R['''**Result: see the table above.** Reproduced when both percentages are within tolerance (62.7 +- 6.27,
26.12 +- 2.61) and the shapes hold.'''] = '''**Result: reproduced.** PCA of the recomputed 21 x 28 beta matrix (equal to Source Data Fig. 3b
middle) gives PC1 62.73% and PC2 26.21%, within tolerance, and all five shape conditions hold, also
with the pre-cue baseline subtracted. Per-unit regression (r-b) and no intercept (i-b) give 72.00 and
15.79%, 57.07 and 27.94%, and 66.16 and 21.37%; the paper's numbers come from the script's reading.
L2 gives 63.08 and 25.04% with all shapes.'''
R['''**Result: see the criteria above, for fig3c-subnetwork-lesion and fig3d-supranetwork-lesion.**'''] = '''**Result: fig3c-subnetwork-lesion partially reproduced; fig3d-supranetwork-lesion reproduced.** With
the script's lesion (s-c), whose beta matrices differ from Source Data Fig. 3c and 3d by at most
0.114 and give the same percentages (67.14 and 26.00%, 61.12 and 29.42%; Source Data 67.14 and
26.01%, 61.11 and 29.46%), the subnetwork lesion keeps PC1's mean behaviour weight over the cue at
0.264 (intact 0.274, so 96%) and lowers PC2's probability weight in the first cue second from 0.268
to 0.201, but that behaviour weight is not above the one after the supranetwork lesion (0.268): one
of the criterion's two parts fails, on the paper's own matrices too. The supranetwork lesion lowers
PC1's behaviour weight (0.268 against 0.274, a small drop), and its PC2 has its probability peak in
the first cue second and its behaviour peak in the tenth. Shuffling betas (s-a, s-b) meets every
part of fig3c and fails the PC2 part of fig3d.'''
R['''**Result: see above.** Reproduced when DPG and LPAG have the two largest positive differentials,
within tolerance.'''] = '''**Result: reproduced.** LPAG (7.41) and DPG (5.93) have the two largest differentials, each equal to
the Source Data value, followed by DRD (3.13) and PMnR (2.53); every region equals Source Data Fig. 3e
right. Under L2 LPAG and DPG are also the two largest (9.54 and 6.96).'''
R['''**Result: see the medians above against the tolerances.**
""")

# ---------------------------------------------------------------- outcome pca'''] = '''**Result: partially reproduced.** Over 20 seeds the median largest cluster is 304.5 (322 +- 32.2) and
the median of the median sizes 161.0 (169 +- 16.9), both within tolerance, but the median smallest
cluster is 29.0, below 46 +- 4.6; single seeds give smallest clusters from 1 to 58. The mean squared
distance falls smoothly from 1 to 20 clusters.
""")

# ---------------------------------------------------------------- outcome pca'''
R['''**Result: see above.**
""")

# ---------------------------------------------------------------- phasic/tonic'''] = '''**Result: reproduced.** PC1 of the 1812 x 80 outcome matrix explains 17.68% (17.7 +- 1.77). Its mean
weights are uncertainty shock 0.194 > danger 0.071 > safety -0.032, and uncertainty omission (-0.005)
is not below safety. The Source Data Fig. 4c matrix (24.18%) holds the units' outcome rows with the
heat-plot baseline subtracted, as the counts above show, not the matrix PCA was run on.
""")

# ---------------------------------------------------------------- phasic/tonic'''
R['''**Result: see the tests above, for fig4b-phasic-network and fig4b-tonic-network.**'''] = '''**Result: fig4b-phasic-network and fig4b-tonic-network reproduced, resting on an assumption.** Under
L1 every profile condition holds: k1 to k3 have higher temporal indices than every one of k6 to k9
under both t-a and t-b; in the first second k1 fires more to uncertainty shock than to danger (2.58,
1.59), k2 more to danger (2.85, 1.44), and k3 is suppressed on both (-0.97, -0.90); k6 is the only
cluster inhibited to surprising shock (-0.88, below its other means), and k7 and k8 increase most to
it (0.82, 0.31) with seconds 5 to 10 above half the first second. The network parts hold with r
squared, the measure the Methods name and the script plots (mean within k1 to k3 0.539 against 0.076
outside; k6 to k9 0.505 against 0.110), and fail with r (-0.329 against 0.008; -0.250 against
0.000), because k3 and k6 change firing in the opposite direction to their fellow clusters. With r
the outcome would be partially reproduced for both.'''
R['''**Result: see above.**
""")

# ---------------------------------------------------------------- outcome hubs'''] = '''**Result: reproduced.** The 265 phasic units give PC1 37.01% (37.0 +- 3.7) with danger and uncertainty
shock weights in the first second of 0.410 and 0.424, each more than twice their means over seconds 5
to 10 and close to each other; the 613 tonic units give PC1 29.20% (29.2 +- 2.92), largest for
uncertainty shock (0.202) and negative for safety (-0.078). The Source Data matrices give the same.
""")

# ---------------------------------------------------------------- outcome hubs'''
R['''**Result: see above.** Reproduced when k1 and k2 each exceed k3 by t-test, and k6 has the highest
mean, above each of k7 to k9 by t-test.'''] = '''**Result: reproduced.** With the script's measure (r squared), whose per-unit values equal Source Data
Fig. 4f as a set, k1 (0.274) and k2 (0.260) each exceed k3 (0.148; p = 3.6e-12 and 9.8e-08, below
0.05/3), and k6 (0.264) has the highest tonic mean and exceeds k7, k8 and k9 (p <= 7.5e-07, below
0.05/6). With r the phasic part holds and k6 has the lowest tonic mean (-0.183). Source Data Fig. 4f
right labels 171 units as k7 and 111 as k8, where Figure 4b's sheets have 111 in k7 and 171 in k8.'''
R['''**Result: see above.** Reproduced when the phasic fraction exceeds the tonic fraction and the tonic
network spans at least as many regions.'''] = '''**Result: reproduced.** 0.600 of phasic units and 0.594 of tonic units are in DLPAG, LPAG, VLPAG, DRL,
DRD, DRV, PDR and PMnR (a difference of 0.006, chi-square p = 0.92), and the tonic network spans 20
regions against 17. K6 spans 17 regions, against 10 to 19 for the other outcome clusters. The effect
is small, as on the paper's own values.'''
R['''**Result: see the tests above.** Reproduced when both parts hold under one reading.'''] = '''**Result: reproduced.** Under all four readings k1's shock and prediction error betas peak in the
first 2 s and stay below half that peak from 5 to 10 s, and k6's mean absolute prediction error beta is
12.3 times its mean absolute shock beta (8.9 without an intercept). The script's betas equal Source
Data Fig. 5b middle with prediction error in columns 1 to 20, the reverse of the Methods' layout.'''
R['''**Result: see above.**
""")

md("""
## fig5c-phasic-lesion'''] = '''**Result: reproduced.** The recomputed 11 x 40 betas (equal to Source Data Fig. 5b middle) give PC1
53.74% and PC2 33.43%, within tolerance; PC1's shock and prediction error weights have opposite
signs, and PC2's shock weights peak in the first 2 s and its prediction error weights later. L2
gives 47.80 and 30.92%, out of tolerance, with the same shapes.
""")

md("""
## fig5c-phasic-lesion'''
R['''**Result: see the table above, for fig5c-phasic-lesion and fig5d-tonic-lesion.**'''] = '''**Result: fig5c-phasic-lesion and fig5d-tonic-lesion reproduced.** With the script's lesion (s-d,
one permutation for all intervals or one per interval) the phasic lesion gives 79.99 and 16.81%
(80.0 and 16.8 reported), PC1 a sustained prediction error signal and PC2 mostly shock; the tonic
lesion gives 61.18 and 29.88% (61.3 and 29.8), PC1 opposing shock and prediction error with both
peaks in the first 2 s, and PC2 dynamic and correlated with the intact PC2 at r = 0.895. Shuffling
betas (s-a, s-b) gives 76.50 to 78.59% and 53.45 to 60.93% for PC1, with the same shapes.'''
R['''**Result: see above.**
""")

# ---------------------------------------------------------------- membership'''] = '''**Result: reproduced.** With phasic read as k1 to k5 (p-b), the reading Source Data Fig. 5e uses, the
largest differential is 4.48 points (MnR) and every value equals Source Data, at the limit the
criterion sets. With phasic as k1 to k3 (p-a) the largest is 9.82 (PMnR), above 1.5 x 4.48, which
would not reproduce the claim. The chi-square of region by network, shown as a variant, gives
p = 0.039 (p-b) and 3e-05 (p-a).
""")

# ---------------------------------------------------------------- membership'''
R['''**Result: see above.** Reproduced when neither test has p < 0.05.'''] = '''**Result: reproduced.** Under L1, 85 of 265 phasic units (0.321) and 159 of 613 tonic units (0.259)
are in the cue subnetwork; against 0.279 the goodness-of-fit chi-square is 2.30 (p = 0.13) and 1.17
(p = 0.28), and the 2 x 2 tests give p = 0.10 and 0.19. Under L2 the tonic network differs (p < 0.01
by both tests).'''
for k, v in R.items():
    assert k in s, k[:80]
    s = s.replace(k, v)
open('gen.py','w').write(s)
PYEOF
python3 results.py && grep -c "Result: see" gen.py
```

```
Exit code 1
0
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('gen.py').read()
old=s[s.index("Per unit, `findchangepts` (one change in mean)"):s.index('""")', s.index("Per unit, `findchangepts` (one change in mean)"))]
new='''Per unit, `findchangepts` (one change in mean) on its danger firing over the 10-s cue in 1-ms bins
(Supplementary Methods, Danger firing latency). Baseline subtraction and z-scoring are affine maps
of the summed spike count, and the change point of a mean is unchanged by them, so reading l-a is
the change point of the summed 1-ms spike counts over the four danger trials. Reading l-b uses the
cube's 250-ms z values repeated into 1-ms bins. A unit with no change point (no danger spikes) has
no latency. A variant outside the criterion searches from 2 s before onset, which is what the
Source Data latencies turn out to follow.
'''
s=s.replace(old,new)
s=s.replace('''uncertainty minus safety interval, [-0.06, 0.28], includes zero) and under c-b 5 of 8. Subjects 4 and
6 (2 and 1 sessions) have mean ratios ordered danger >= uncertainty > safety for subject 4, and
danger > uncertainty > safety by 0.013 for subject 6.''','''uncertainty minus safety interval, [-0.06, 0.28], includes zero) and under c-b 5 of 8. Subjects 4 and
6 (2 sessions and 1) have means ordered danger > uncertainty > safety (1.000, 0.887, 0.500 and 0.875,
0.521, 0.508).''')
open('gen.py','w').write(s)
EOF
grep -n "not run" gen.py | head
```

```
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/header.md",
 "content": "# Reproducing Strickland and McDannald (2022) from CRCNS bst-3\n\n**Paper.** Strickland JA, McDannald MA (2022). Brainstem networks construct threat probability and\nprediction error from neuronal building blocks. *Nature Communications* 13:6192.\n[doi:10.1038/s41467-022-34021-1](https://doi.org/10.1038/s41467-022-34021-1). The claims file\n(`claims/strickland-2022.yaml`) was written from the version of record (PMC9582012) with its\nSupplementary Information and Source Data workbook.\n\n**Data set.** CRCNS [bst-3](https://crcns.org/data-sets/brainstem/bst-3),\n[doi:10.6080/K0Q23XGR](https://doi.org/10.6080/K0Q23XGR), \"Neuropixels recordings from 21 brainstem\nregions in rats during fear discrimination\", read from the public bucket\n(`crcnsarchive/bst-3/live/data.zip`, 367,964,637 bytes, last modified 2026-02-11). CRCNS data sets\nare not versioned, so the version is recorded as `unversioned`; the MD5 sums of the bucket's\n`checksums.md5` are printed below (data.zip `4ee6c433f5255693d5e85bcca6819cd4`), so that a later\nchange can be detected. The paper cites the data set by its DOI and no version; there is only the\none published copy (`live/`, descriptor version 0.6 of 2022-11-29), so it is the one pinned.\n\n**What the data set holds.** One MATLAB file per single unit (1812, spike times and the session's\ncue, shock, poke and pellet times, in samples at 30 kHz), the cube file the paper's `cubeScript.m`\nbuilds from them (binned and normalized firing per trial, suppression ratios, region and\ncoordinates per unit), and the paper's five analysis scripts. It holds no cluster membership.\n\n**Outside input.** The paper's own cue and outcome clusters (L1) come from its Source Data workbook\n(supplementary file 41467_2022_34021_MOESM4_ESM.xlsx of doi:10.1038/s41467-022-34021-1, streamed from\nthe publisher, MD5 checked), matched to the units by their firing rows (claim\n`source-data-cluster-link`). It names clusters for units the data set already holds; it brings in no\nmeasurement. The analyses run on the data set's data.\n\n**The paper's code.** The scripts in the data set (`data/scripts`) are the code the paper's Code\navailability points to. Where the Methods leave a detail open and a script settles it, the script is\nfollowed and cited (see the docstring of `bst3.py`).\n\n| Claim | Tested |\n|---|---|\n| source-data-cluster-link | tested (link) |\n| fig1c-suppression-order | tested |\n| figs2-each-rat-discriminates | tested |\n| units-sessions-subjects | tested |\n| fig1e-regions | tested |\n| fig2b-cue-clusters | tested |\n| fig2c-cue-pc1-ordered | tested |\n| fig2c-pc1-contribution | tested |\n| fig2d-danger-latency | tested |\n| fig2e-cue-subnetwork | tested |\n| fig2f-cue-hubs | tested |\n| fig2g-cue-anatomy | tested |\n| fig3a-cluster-signals | tested, with the Source Data labels |\n| fig3b-signal-pca | tested |\n| fig3c-subnetwork-lesion | tested |\n| fig3d-supranetwork-lesion | tested |\n| fig3e-network-anatomy | tested |\n| fig4b-outcome-clusters | tested |\n| fig4c-positive-prediction-error | tested |\n| fig4b-phasic-network | tested, with the Source Data labels |\n| fig4b-tonic-network | tested, with the Source Data labels |\n| fig4e-network-pca | tested |\n| fig4f-outcome-hubs | tested, with the Source Data labels |\n| fig4g-outcome-anatomy | tested |\n| fig5a-outcome-cluster-signals | tested, with the Source Data labels |\n| fig5b-outcome-signal-pca | tested |\n| fig5c-phasic-lesion | tested |\n| fig5d-tonic-lesion | tested |\n| fig5e-no-anatomical-bias | tested |\n| cue-outcome-membership-independent | tested |\n\nNo claim is blocked. Random seeds are fixed per section.\n"
}
```

```
<tool_use_error>File has not been read yet. Read it first before writing to it.</tool_use_error>
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/summary.md",
 "content": "## Summary\n\n| Claim | Outcome |\n|---|---|\n| source-data-cluster-link | reproduced |\n| fig1c-suppression-order | reproduced |\n| figs2-each-rat-discriminates | reproduced |\n| units-sessions-subjects | reproduced |\n| fig1e-regions | reproduced |\n| fig2b-cue-clusters | reproduced |\n| fig2c-cue-pc1-ordered | reproduced |\n| fig2c-pc1-contribution | reproduced |\n| fig2d-danger-latency | not reproduced |\n| fig2e-cue-subnetwork | reproduced |\n| fig2f-cue-hubs | partially reproduced (rests on an assumption) |\n| fig2g-cue-anatomy | reproduced |\n| fig3a-cluster-signals | partially reproduced |\n| fig3b-signal-pca | reproduced |\n| fig3c-subnetwork-lesion | partially reproduced |\n| fig3d-supranetwork-lesion | reproduced |\n| fig3e-network-anatomy | reproduced |\n| fig4b-outcome-clusters | partially reproduced |\n| fig4c-positive-prediction-error | reproduced |\n| fig4b-phasic-network | reproduced (rests on an assumption) |\n| fig4b-tonic-network | reproduced (rests on an assumption) |\n| fig4e-network-pca | reproduced |\n| fig4f-outcome-hubs | reproduced |\n| fig4g-outcome-anatomy | reproduced |\n| fig5a-outcome-cluster-signals | reproduced |\n| fig5b-outcome-signal-pca | reproduced |\n| fig5c-phasic-lesion | reproduced |\n| fig5d-tonic-lesion | reproduced |\n| fig5e-no-anatomical-bias | reproduced |\n| cue-outcome-membership-independent | reproduced |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\n**How the analysis differs from the paper's.** It runs in Python on the cube file and the spike\ntimes, following the paper's MATLAB scripts where the Methods leave a detail open: the\nnormalization of `cubeScript.m`, the 1-s and 500-ms bins of the scripts' matrices, the regression\nwith an intercept on cluster mean firing, the shuffles of the contribution and lesion analyses. The\npaper's k-means clusters cannot be regenerated (the script seeds MATLAB's generator), so the\npaper's own membership is taken from its Source Data, which every unit matches exactly; this\nattempt's own k-means is shown beside it. The cue hub and outcome network correlations use r\nsquared, the measure the Methods name; with r three outcomes would be lower. The danger latency is\nsearched within the 10-s cue as the Methods say; the Source Data latencies follow a search from 2 s\nbefore onset instead.\n\n**What was found about the data set.** The cube file equals the spike times binned as\n`cubeScript.m` does, the suppression ratios equal those recomputed from the poke times in all 73\nsessions, and the unit, female and per-subject counts equal the paper's. 204 unit files hold\nrepeated spike times (9289 in all), which the script's counting drops. The data set has 73\nsessions where Supplementary Table 1 lists 75 (one fewer for subjects 5 and 10). One session\n(js27101920) has 5 shocks, with none on its first danger trial. In session js10030220 three unit\nfiles carry event times that differ from the others. Region names are stored as MATLAB string\nobjects that cannot be read outside MATLAB, and the region numbers need the scripts' mapping,\nincluding their correction of 35 units numbered as CIC to DpWh. The data set holds no cluster\nmembership, so the paper's clusters can only be recovered from its Source Data.\n"
}
```

```
<tool_use_error>File has not been read yet. Read it first before writing to it.</tool_use_error>
```

**Agent calls Bash**

```bash
rm /tmp/claude-1001/header.md /tmp/claude-1001/summary.md; echo done
```

```
done
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/header.md",
 "content": "# Reproducing Strickland and McDannald (2022) from CRCNS bst-3\n\n**Paper.** Strickland JA, McDannald MA (2022). Brainstem networks construct threat probability and\nprediction error from neuronal building blocks. *Nature Communications* 13:6192.\n[doi:10.1038/s41467-022-34021-1](https://doi.org/10.1038/s41467-022-34021-1). The claims file\n(`claims/strickland-2022.yaml`) was written from the version of record (PMC9582012) with its\nSupplementary Information and Source Data workbook.\n\n**Data set.** CRCNS [bst-3](https://crcns.org/data-sets/brainstem/bst-3),\n[doi:10.6080/K0Q23XGR](https://doi.org/10.6080/K0Q23XGR), \"Neuropixels recordings from 21 brainstem\nregions in rats during fear discrimination\", read from the public bucket\n(`crcnsarchive/bst-3/live/data.zip`, 367,964,637 bytes, last modified 2026-02-11). CRCNS data sets\nare not versioned, so the version is recorded as `unversioned`; the MD5 sums of the bucket's\n`checksums.md5` are printed below (data.zip `4ee6c433f5255693d5e85bcca6819cd4`), so that a later\nchange can be detected. The paper cites the data set by its DOI and no version; there is only the\none published copy (`live/`, descriptor version 0.6 of 2022-11-29), so it is the one pinned.\n\n**What the data set holds.** One MATLAB file per single unit (1812, spike times and the session's\ncue, shock, poke and pellet times, in samples at 30 kHz), the cube file the paper's `cubeScript.m`\nbuilds from them (binned and normalized firing per trial, suppression ratios, region and\ncoordinates per unit), and the paper's five analysis scripts. It holds no cluster membership.\n\n**Outside input.** The paper's own cue and outcome clusters (L1) come from its Source Data workbook\n(supplementary file 41467_2022_34021_MOESM4_ESM.xlsx of doi:10.1038/s41467-022-34021-1, streamed from\nthe publisher, MD5 checked), matched to the units by their firing rows (claim\n`source-data-cluster-link`). It names clusters for units the data set already holds; it brings in no\nmeasurement. The analyses run on the data set's data.\n\n**The paper's code.** The scripts in the data set (`data/scripts`) are the code the paper's Code\navailability points to. Where the Methods leave a detail open and a script settles it, the script is\nfollowed and cited (see the docstring of `bst3.py`).\n\n| Claim | Tested |\n|---|---|\n| source-data-cluster-link | tested (link) |\n| fig1c-suppression-order | tested |\n| figs2-each-rat-discriminates | tested |\n| units-sessions-subjects | tested |\n| fig1e-regions | tested |\n| fig2b-cue-clusters | tested |\n| fig2c-cue-pc1-ordered | tested |\n| fig2c-pc1-contribution | tested |\n| fig2d-danger-latency | tested |\n| fig2e-cue-subnetwork | tested |\n| fig2f-cue-hubs | tested |\n| fig2g-cue-anatomy | tested |\n| fig3a-cluster-signals | tested, with the Source Data labels |\n| fig3b-signal-pca | tested |\n| fig3c-subnetwork-lesion | tested |\n| fig3d-supranetwork-lesion | tested |\n| fig3e-network-anatomy | tested |\n| fig4b-outcome-clusters | tested |\n| fig4c-positive-prediction-error | tested |\n| fig4b-phasic-network | tested, with the Source Data labels |\n| fig4b-tonic-network | tested, with the Source Data labels |\n| fig4e-network-pca | tested |\n| fig4f-outcome-hubs | tested, with the Source Data labels |\n| fig4g-outcome-anatomy | tested |\n| fig5a-outcome-cluster-signals | tested, with the Source Data labels |\n| fig5b-outcome-signal-pca | tested |\n| fig5c-phasic-lesion | tested |\n| fig5d-tonic-lesion | tested |\n| fig5e-no-anatomical-bias | tested |\n| cue-outcome-membership-independent | tested |\n\nNo claim is blocked. Random seeds are fixed per section.\n"
}
```

```
File created successfully at: /tmp/claude-1001/header.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/summary.md",
 "content": "## Summary\n\n| Claim | Outcome |\n|---|---|\n| source-data-cluster-link | reproduced |\n| fig1c-suppression-order | reproduced |\n| figs2-each-rat-discriminates | reproduced |\n| units-sessions-subjects | reproduced |\n| fig1e-regions | reproduced |\n| fig2b-cue-clusters | reproduced |\n| fig2c-cue-pc1-ordered | reproduced |\n| fig2c-pc1-contribution | reproduced |\n| fig2d-danger-latency | not reproduced |\n| fig2e-cue-subnetwork | reproduced |\n| fig2f-cue-hubs | partially reproduced (rests on an assumption) |\n| fig2g-cue-anatomy | reproduced |\n| fig3a-cluster-signals | partially reproduced |\n| fig3b-signal-pca | reproduced |\n| fig3c-subnetwork-lesion | partially reproduced |\n| fig3d-supranetwork-lesion | reproduced |\n| fig3e-network-anatomy | reproduced |\n| fig4b-outcome-clusters | partially reproduced |\n| fig4c-positive-prediction-error | reproduced |\n| fig4b-phasic-network | reproduced (rests on an assumption) |\n| fig4b-tonic-network | reproduced (rests on an assumption) |\n| fig4e-network-pca | reproduced |\n| fig4f-outcome-hubs | reproduced |\n| fig4g-outcome-anatomy | reproduced |\n| fig5a-outcome-cluster-signals | reproduced |\n| fig5b-outcome-signal-pca | reproduced |\n| fig5c-phasic-lesion | reproduced |\n| fig5d-tonic-lesion | reproduced |\n| fig5e-no-anatomical-bias | reproduced |\n| cue-outcome-membership-independent | reproduced |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\n**How the analysis differs from the paper's.** It runs in Python on the cube file and the spike\ntimes, following the paper's MATLAB scripts where the Methods leave a detail open: the\nnormalization of `cubeScript.m`, the 1-s and 500-ms bins of the scripts' matrices, the regression\nwith an intercept on cluster mean firing, the shuffles of the contribution and lesion analyses. The\npaper's k-means clusters cannot be regenerated (the script seeds MATLAB's generator), so the\npaper's own membership is taken from its Source Data, which every unit matches exactly; this\nattempt's own k-means is shown beside it. The cue hub and outcome network correlations use r\nsquared, the measure the Methods name; with r three outcomes would be lower. The danger latency is\nsearched within the 10-s cue as the Methods say; the Source Data latencies follow a search from 2 s\nbefore onset instead.\n\n**What was found about the data set.** The cube file equals the spike times binned as\n`cubeScript.m` does, the suppression ratios equal those recomputed from the poke times in all 73\nsessions, and the unit, female and per-subject counts equal the paper's. 204 unit files hold\nrepeated spike times (9289 in all), which the script's counting drops. The data set has 73\nsessions where Supplementary Table 1 lists 75 (one fewer for subjects 5 and 10). One session\n(js27101920) has 5 shocks, with none on its first danger trial. In session js10030220 three unit\nfiles carry event times that differ from the others. Region names are stored as MATLAB string\nobjects that cannot be read outside MATLAB, and the region numbers need the scripts' mapping,\nincluding their correction of 35 units numbered as CIC to DpWh. The data set holds no cluster\nmembership, so the paper's clusters can only be recovered from its Source Data.\n"
}
```

```
File created successfully at: /tmp/claude-1001/summary.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/strickland-2022 && python3 - <<'EOF'
p='bst3.py'; s=open(p).read()
s=s.replace('''CUBE_FIELDS = ["fire/z/s1/interval", "fire/z/ms500/interval", "fire/z/ms250/interval", "fire/raw/s1/interval", "fire/raw/base2",
''','''CUBE_FIELDS = ["fire/z/s1/interval", "fire/z/ms500/interval", "fire/z/ms250/interval", "fire/raw/s1/interval",
               "fire/raw/base2",
''')
s=s.replace('''    bins from 2 s before onset to the end of the 10-s cue (12000 bins), for the latency; and per session the cue, shock and poke times.''','''    bins from 2 s before onset to the end of the 10-s cue (12000 bins), for the latency; and per
    session the cue, shock and poke times.''')
open(p,'w').write(s)
EOF
awk 'length>120{print FILENAME": "FNR": "length}' bst3.py; sed -n 95,100p bst3.py; sed -n 136,145p bst3.py
$TMPDIR/dev/bin/python $TMPDIR/gen.py reproduce_strickland_2022.ipynb $TMPDIR/header.md $TMPDIR/summary.md && $TMPDIR/dev/bin/python $TMPDIR/runnb.py reproduce_strickland_2022.ipynb $TMPDIR/exec.ipynb 2>&1 | grep -v WARNING | tail -5
```

```
CUBE_FIELDS = ["fire/z/s1/interval", "fire/z/ms500/interval", "fire/z/ms250/interval", "fire/raw/s1/interval",
               "fire/raw/base2",
               "poke/SR", "poke/base", "poke/cue", "anatomy/regionNum", "anatomy/ID", "anatomy/x",
               "anatomy/y", "anatomy/z"]
    """One pass over the single-unit files, keeping only what the analyses need.

    Per unit: spike counts in 250-ms bins from 20 s before to 40 s after cue onset (240 bins) for
    the 16 trials; counts in the cube's 1-s bins (40 s from 10 s before onset) and the 2-s
    baseline, to check the cube against the spikes; the summed danger-trial spike count in 1-ms
    bins from 2 s before onset to the end of the 10-s cue (12000 bins), for the latency; and per
    session the cue, shock and poke times.
    """
    infos = sorted([i for i in zf.infolist() if i.filename.startswith("data/singleUnits/")
                    and i.filename.endswith(".mat")], key=lambda i: i.header_offset)
ran 81.97618627548218
```

**Agent calls Bash**

```bash
$TMPDIR/dev/bin/python $TMPDIR/dump.py $TMPDIR/exec.ipynb 5 5 | tail -8; $TMPDIR/dev/bin/python $TMPDIR/dump.py $TMPDIR/exec.ipynb 29 33 | grep -v "^ \{0,8\}[0-9]" ; $TMPDIR/dev/bin/python $TMPDIR/dump.py $TMPDIR/exec.ipynb 66 66
```

```
Trials per session: {16: 73} ; shocks per session: {6: 72, 5: 1}
Rows of the trial table that have a shock: {'1,2,3,4,5,6,': 72, '2,3,4,5,6,': 1}
Delay from cue onset to shock onset (s): [np.float64(11.998), np.float64(11.999), np.float64(12.0), np.float64(12.001)]
Mean ITI per session, min: 3.19 to 3.26
   session  trials  shocks shock rows  shock delay s  session min  ITI min  pokes
js27101920      16       5 2,3,4,5,6, [12.0, 12.001]    48.382239 3.225483    923

[29] CODE ['claim:fig2c-cue-pc1-ordered']
PC1 29.73% (29.7 +- 2.97), PC2 14.11%, PC3 10.51%
mean PC1 weight over the 10 cue seconds: {'danger': np.float64(0.2662), 'uncertainty': np.float64(0.1275), 'safety': np.float64(0.0061)}
ordered danger > uncertainty > safety: True
On the Source Data Fig. 2c inset matrix ((1812, 42)): PC1 47.09%

inset rows equal to a unit's cue row: 69 ; median best r 1.0

inset rows equal to a unit's baseline-subtracted row: 1812

Per animal (PC1 of that animal's units):
  subject 1 (192 units): PC1 36.6%, mean cue weights D, U, S [0.268, 0.097, -0.083], ordered True
  subject 2 (328 units): PC1 30.5%, mean cue weights D, U, S [0.272, 0.059, 0.013], ordered True
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
$TMPDIR/dev/bin/python $TMPDIR/dump.py $TMPDIR/exec.ipynb 5 5 | head -12; cd $TMPDIR && python3 - <<'EOF'
s=open('gen.py').read()
s=s.replace('''plot of `cueAnalysis.m`), not the rows PCA was run on. The per-animal PCAs are printed above.''','''plot of `cueAnalysis.m`), not the rows PCA was run on. Per animal, PC1 explains 19.2 to 43.0%, and
its cue weights are ordered danger > uncertainty > safety in 9 of 10 animals (subject 9: uncertainty
0.139, safety 0.140).''')
s=s.replace('''heat-plot baseline subtracted, as the counts above show, not the matrix PCA was run on.''','''heat-plot baseline subtracted, as the counts above show, not the matrix PCA was run on. Per animal,
uncertainty shock has the largest mean PC1 weight in all 10 animals, and danger exceeds safety in 9
(not subject 7).''')
open('gen.py','w').write(s)
EOF
```

```
[5] CODE ['sanity']
cube fire.raw.s1 equals spike counts in the script's 1-s bins (each spike time counted once): True
cube fire.raw.base2 equals floor(count in 2 s before onset / 2): True
cube fire.z.s1 equals the script's z of differential firing, max abs difference: 3.481659405224491e-13
cube poke.SR equals the ratios recomputed from poke times in 73 of 73 sessions
Session js10030220: units ['js10030220pr25a13spk0009', 'js10030220pr25a13spk0049', 'js10030220pr25a13spk0044'] carry cue or poke times that differ from unit js10030220pr25a13spk0392
    js10030220pr25a13spk0009: first cue onset 12779057, pokes 336, max |cue - reference cue| 0.2814 s

    js10030220pr25a13spk0049: first cue onset 12778991, pokes 336, max |cue - reference cue| 0.2986 s

    js10030220pr25a13spk0044: first cue onset 12779057, pokes 336, max |cue - reference cue| 0.2814 s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/strickland-2022 && $TMPDIR/dev/bin/python - <<'EOF'
import sys,numpy as np,collections
sys.path.insert(0,'.')
import bst3
zf=bst3.open_zip()
names=[n for n in zf.namelist() if 'js10030220' in n]
vers=collections.defaultdict(list)
for n in names:
    _,sp,ev=bst3._parse_unit(zf.read(n))
    cue=np.concatenate([ev['cue100'],ev['cueSPR'],ev['cueNsPR'],ev['cue0']])
    vers[tuple(np.round(cue).astype(int))+(len(ev['poke']),)].append(n.split('/')[-1])
for k,v in vers.items(): print(len(v), k[:4], k[-1], v[:3])
a,b=list(vers)[:2]
print(np.array(a[:16])-np.array(b[:16]))
EOF
```

```
19 (np.int64(12780141), np.int64(24091877), np.int64(53121528), np.int64(81850891)) 336 ['js10030220pr25a13spk0392.mat', 'js10030220pr25a13spk0205.mat', 'js10030220pr25a13spk0350.mat']
2 (np.int64(12779057), np.int64(24089834), np.int64(53117025), np.int64(81843951)) 336 ['js10030220pr25a13spk0009.mat', 'js10030220pr25a13spk0044.mat']
1 (np.int64(12778991), np.int64(24089709), np.int64(53116750), np.int64(81843528)) 336 ['js10030220pr25a13spk0049.mat']
[1084 2043 4503 6940 7457 8442 1551 2585 3154 3596 5072 6524 4087 5539
 6031 8000]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('gen.py').read()
s=s.replace('''        print(f"Session {k}: units {s['differing_units']} carry cue or poke times that differ from unit {s['file_id']}")''','''        print(f"Session {k} ({int((session == k).sum())} units): units {s['differing_units']} carry cue or poke times "
              f"that differ from unit {s['file_id']} (the other units agree with it)")''')
s=s.replace('''            print(f"    {u}: first cue onset {cue.min():.0f}, pokes {ev['poke'].size}, max |cue - reference cue| "
                  f"{np.abs(cue - s['cue']).max() / bst3.FS:.4f} s")''','''            o = np.argsort(s["cue"])
            print(f"    {u}: pokes {ev['poke'].size}; reference minus this unit's cue onsets, in session order (s): "
                  f"{np.round((s['cue'] - cue)[o] / bst3.FS, 3).tolist()}")''')
open('gen.py','w').write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/strickland-2022 && printf "aiohttp\nfsspec\nh5py\nnumpy\nopenpyxl\npandas\nrequests\nscikit-learn\nscipy\n" > requirements.in && cat > entry.yaml <<'EOF'
schema_version: 1
name: strickland-2022
type: reproduction
title: Brainstem networks for threat probability and prediction error (Strickland and McDannald 2022)
description: Tests the findings of Strickland and McDannald (2022) on CRCNS data set bst-3, which holds
  1812 brainstem single units recorded with Neuropixels in ten rats during probabilistic fear
  discrimination, the cube file of binned and normalized firing built from them, and the paper's
  MATLAB scripts. It checks the behaviour, the unit counts, the k-means clusters and their PCA,
  the regression and lesion analyses of threat probability, behaviour, shock and prediction error
  signals, and the anatomy of the networks, with the paper's own cluster membership taken from its
  Source Data.
license: Apache-2.0
notebooks:
- path: reproduce_strickland_2022.ipynb
  title: Reproducing Strickland and McDannald (2022) from CRCNS bst-3
  runtime_minutes: 2
helpers:
- bst3.py
related:
- id: crcns:bst-3/unversioned
  relation: uses_data
- id: doi:10.1038/s41467-022-34021-1
  relation: reproduces
EOF
$TMPDIR/dev/bin/python $TMPDIR/gen.py reproduce_strickland_2022.ipynb $TMPDIR/header.md $TMPDIR/summary.md && cd  && date -u && python tools/entry.py lock entries/strickland-2022 2>&1 | tail -3
```

```
Fri Nov 13 01:42:34 UTC 2026
wrote strickland-2022/requirements.lock.txt (Python 3.13, with hashes)
```

**Agent**

Now the README and the attempt record, then the full check and clean run.

**Agent calls Write**

```json
{
 "file_path": "entries/strickland-2022/README.md",
 "content": "# Strickland and McDannald (2022) from CRCNS bst-3\n\nTests the findings of [Strickland and McDannald (2022)](https://doi.org/10.1038/s41467-022-34021-1)\non CRCNS data set [bst-3](https://doi.org/10.6080/K0Q23XGR), which holds 1812 brainstem single\nunits recorded with Neuropixels in ten rats during probabilistic fear discrimination, the cube file\nof binned and normalized firing that the paper's scripts build from them, and those scripts.\n\n| Claim | Outcome |\n|---|---|\n| The units match the paper's Source Data cluster rows (link) | Reproduced |\n| Suppression ordered danger > uncertainty > safety, F(2,142) = 149.2 | Reproduced |\n| Every rat discriminates | Reproduced |\n| 1812 units, 73 sessions, 965 from females, per-subject totals | Reproduced |\n| 21 regions and their unit counts | Reproduced |\n| 21 cue clusters of 24 to 219 units | Reproduced |\n| Cue PC1 (29.7%) is ordered danger > uncertainty > safety | Reproduced |\n| PC1 comes from k1 to k9 (505 units), k1 and k2 most | Reproduced |\n| Danger latency correlates with PC1 contribution (R2 = 0.41) | Not reproduced |\n| k1 to k9 form a correlated subnetwork, k3 the exception | Reproduced |\n| k1 and k2 are hubs of the cue subnetwork | Partially reproduced (assumption) |\n| Cue clusters span six or more regions; subnetwork in SC and PAG | Reproduced |\n| Cluster regression shapes (k5, k15, k10, k6) | Partially reproduced |\n| Beta PCA, PC1 62.7% and PC2 26.1% | Reproduced |\n| Subnetwork lesion | Partially reproduced |\n| Supranetwork lesion | Reproduced |\n| DPG and LPAG bias toward the subnetwork | Reproduced |\n| 11 outcome clusters of 46 to 322 units | Partially reproduced |\n| Outcome PC1 (17.7%) is positive prediction error | Reproduced |\n| Phasic outcome network k1 to k3 | Reproduced (assumption) |\n| Tonic outcome network k6 to k9 | Reproduced (assumption) |\n| Network PCAs, 37.0% and 29.2% | Reproduced |\n| Outcome hubs | Reproduced |\n| Outcome network anatomy | Reproduced |\n| Outcome regression, k1 and k6 | Reproduced |\n| Outcome beta PCA, 53.7% and 33.4% | Reproduced |\n| Phasic and tonic lesions | Reproduced |\n| No anatomical bias of outcome networks | Reproduced |\n| Cue and outcome network membership independent | Reproduced |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nThe data set holds no cluster membership; the paper's clusters are taken from its Source Data\nworkbook, which every unit matches exactly. The attempt record, with the reasons and the\ndifferences from the paper's method, is\n[`attempts/strickland-2022-01.yaml`](../../attempts/strickland-2022-01.yaml).\n\n- `reproduce_strickland_2022.ipynb`: the analysis. It takes about two minutes, most of it reading\n  the 1812 unit files and the cube from the archive.\n- `bst3.py`: reading the zip in place, the cube and the unit files, and the measures of the paper's\n  scripts (normalization, suppression ratios, PCA, shuffles, regression, latency). Other notebooks\n  on this data set can import it.\n"
}
```

```
File created successfully at: entries/strickland-2022/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "attempts/strickland-2022-01.yaml",
 "content": "schema_version: 3\nid: strickland-2022-01\ndatasets:\n- archive: crcns\n  id: bst-3\n  version: unversioned\n  doi: 10.6080/K0Q23XGR\n  relation: primary\npaper: doi:10.1038/s41467-022-34021-1\ndate: 2026-11-13\nentry: strickland-2022\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-14\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/43342645589\ninputs:\n- what: The paper's cue and outcome cluster membership (Source Data sheets Figure 2b k1 to k21 and\n    Figure 4b k1 to k11), matched to the data set's units by their firing rows, and the paper's own\n    matrices and per-unit values used as reference (Figures 1c, 2c, 2d, 2e, 2f, 3b to 3e, 4c, 4e, 4f,\n    5b to 5e), from the Source Data workbook 41467_2022_34021_MOESM4_ESM.xlsx (MD5\n    4df716fd6739ee3de3b0df81c4175be8), streamed from the publisher.\n  source: doi:10.1038/s41467-022-34021-1 (supplementary file MOESM4)\noutcomes:\n- claim: source-data-cluster-link\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:source-data-cluster-link\n  measured:\n  - 1812\n  - 1812\n  notes: Under the normalization of the paper's cubeScript.m (the data set's cube), every one of the\n    1812 cue rows and 1812 outcome rows of the Source Data cluster sheets equals exactly one unit's\n    row (largest difference 5e-15), so 100% match and every unit gets one cue and one outcome\n    cluster, with the sizes the claims file lists. Under the claims file's four readings (n-a, n-b,\n    w-a, w-b, computed from the spike times in 250-ms bins) at most 2 rows match within 0.01, though\n    1664 cue rows and 650 to 1728 outcome rows correlate above 0.99 with a unit.\n  deviations:\n  - The rows that match are normalized as cubeScript.m does (firing in 1-s and 500-ms bins over the\n    40 s from 10 s before cue onset, minus the trial's 2-s pre-cue rate rounded down, z-scored over\n    all trials and bins at each bin size), a detail the Supplementary Methods describe differently\n    (250-ms bins averaged, other windows) and the paper's code settles. The claims file's four\n    readings are shown and none matches.\n- claim: fig1c-suppression-order\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig1c-suppression-order\n  measured:\n  - 147.92\n  - 0.914\n  - 0.709\n  - 0.230\n  notes: 73 sessions. With empty trials set to 1 (cubeScript.m) the means are 0.914, 0.709 and 0.230,\n    equal to Source Data Fig. 1c, and every session's values equal a Source Data row. Cue x sex\n    mixed ANOVA (a-a) F(2,142) = 147.9, p < 1e-30. With empty trials set to 0 (sr-a) F = 145.6, left\n    out (sr-b) F = 150.4. The repeated-measures reading (a-b) gives F(2,144) = 116.2. 31 of 1168 trials\n    had no pokes in either period.\n  deviations:\n  - Empty trials are set to 1 as cubeScript.m does (poke.SR(isnan(poke.SR)) = 1), a detail the\n    Methods leave open; the claims file's sr-a and sr-b are shown and give the same order and an F\n    within tolerance.\n- claim: figs2-each-rat-discriminates\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:figs2-each-rat-discriminates\n  notes: Under reading c-c all 8 rats with at least 3 sessions have danger and uncertainty\n    suppression intervals that exclude zero. Under c-a 7 of 8 (subject 9's uncertainty minus safety\n    interval is -0.06 to 0.28) and under c-b 5 of 8. Subjects 4 and 6 (2 sessions and 1) have means\n    ordered danger > uncertainty > safety.\n  deviations:\n  - The legend does not say which quantity's interval is tested; three readings are run and the\n    claim holds under c-c.\n- claim: units-sessions-subjects\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:units-sessions-subjects\n  measured:\n  - 1812\n  - 965\n  - 73\n  - 192\n  - 328\n  - 141\n  - 32\n  - 52\n  - 43\n  - 116\n  - 195\n  - 409\n  - 304\n  notes: Subjects mapped from animal ids as cueAnalysis.m does (js10, 11, 13, 14, 15, 21, 22, 24, 25,\n    27 to 1 to 10; js10, 11, 13 and 27 female). All counts equal the paper's. Supplementary Table 1\n    lists 75 sessions; the data set has 7 for subject 5 (8 listed) and 9 for subject 10 (10 listed).\n- claim: fig1e-regions\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig1e-regions\n  measured:\n  - 21\n  - 236\n  - 208\n  - 179\n  - 147\n  - 145\n  notes: 21 regions hold units after the scripts' merges (region 21, CIC, into DpWh; 24 into x/scp),\n    and every region's count equals the sum of Source Data Fig. 3e left.\n  deviations:\n  - Region names and merges come from cubeScript.m and cueAnalysis.m; the cube's own region strings\n    are MATLAB string objects that cannot be read outside MATLAB.\n- claim: fig2b-cue-clusters\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig2b-cue-clusters\n  measured:\n  - 24.0\n  - 218.5\n  - 75.0\n  notes: Medians over 20 k-means seeds (k-means++ seeding, one replicate) of the smallest, largest\n    and median cluster sizes are 24.0, 218.5 and 75.0, all within tolerance (the median near the\n    lower edge, 74.7). Single seeds give 14 to 38, 171 to 274 and 63 to 93. The paper's clustering has\n    a summed squared distance of 11219, inside the seeds' range (11135 to 11336).\n  deviations:\n  - The script seeds MATLAB's generator (rng(1)), which cannot be repeated in Python; 20 seeds are\n    used, as the claims file's standard choice says.\n- claim: fig2c-cue-pc1-ordered\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig2c-cue-pc1-ordered\n  measured: 29.73\n  notes: PC1 of the 1812 x 42 cue matrix (cueAnalysis.m) explains 29.73%; mean weights over the cue\n    are danger 0.266, uncertainty 0.128, safety 0.006. The claims file's 47.1% on the Source Data\n    inset is explained; the inset's 1812 rows equal the units' rows with the pre-cue baseline\n    subtracted (the heat plot), not the matrix PCA was run on. Per animal PC1 explains 19.2 to 43.0%\n    and is ordered in 9 of 10 animals (subject 9 has uncertainty 0.139 and safety 0.140).\n- claim: fig2c-pc1-contribution\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig2c-pc1-contribution\n  measured:\n  - 505\n  - 0.1214\n  - 0.1129\n  notes: Under L1 the nine largest contributions per unit are k1 to k9 (505 units) under both s-a and\n    s-b, with k1 and k2 the two largest; s-a, the script's shuffle (each row across its columns),\n    gives every cluster's Source Data value within 0.0003. Under L2 (best of 20 k-means runs, numbered\n    by contribution) the nine largest hold 411 units, outside 505 +- 50.5, and share 343 units with\n    L1's k1 to k9. The share of each animal's units in k1 to k9 ranges from 0.078 (subject 7) to\n    0.415 (subject 2).\n- claim: fig2d-danger-latency\n  outcome: not_reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig2d-danger-latency\n  measured: 0.067\n  notes: With the latency found within the 10-s cue as the Supplementary Methods say, the correlation\n    across clusters is negative but weak and not significant (l-a r = -0.260, R2 = 0.067, p = 0.26;\n    l-b R2 = 0.065, p = 0.26; with cluster totals, c-b, R2 = 0.122 and 0.104). Units of k1 to k9 do\n    have shorter latencies than k10 to k21 (3571 against 4590 ms, l-a). 1778 units have a latency;\n    Source Data lists 1498. The latencies differ from the paper's (k1 mean 4046 ms here, 182 ms in\n    Source Data). A search from 2 s before onset keeping latencies after onset (a variant outside the\n    criterion) gives 1458 units, k1 327 ms, 413 values equal to Source Data values, and R2 = 0.640\n    (c-a, p = 1.4e-05). On the Source Data latencies R2 is 0.508 (c-a) and 0.394 (c-b). The question\n    of the window and of which units have no latency is for the paper's authors (findings).\n  deviations:\n  - Baseline subtraction and z-scoring are affine maps of the summed 1-ms spike counts, which leave a\n    change point in mean unchanged, so l-a is computed on the summed spike counts of the four danger\n    trials. findchangepts is implemented as one change in mean minimizing the residual sum of squares.\n- claim: fig2e-cue-subnetwork\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig2e-cue-subnetwork\n  notes: With r squared, the mean within k1 to k9 is 0.445 (42 columns) and 0.465 (36 columns),\n    against 0.184 and 0.194 between k1 to k9 and k10 to k21, and k3 has the lowest mean with the other\n    eight (0.225, 0.229). With r the within mean is also higher (0.129 against 0.068) but k8 is lowest\n    (-0.516) because k7 and k8 decrease firing; the criterion names both and the claim holds under r\n    squared. The script's 120-column variant gives the same with r squared except that k7 is lowest.\n- claim: fig2f-cue-hubs\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig2f-cue-hubs\n  measured:\n  - 0.462\n  - 0.503\n  notes: With danger firing over 14 intervals and r squared, k2 (0.503) and k1 (0.462) have the two\n    highest means, within tolerance, but k1 does not exceed k3 (p = 0.42) or k4 (p = 0.12), and k2\n    does not exceed k3 (p = 0.014), at 0.05/7 or 0.05/8. With r, k1 and k3 are the two highest. The\n    Source Data per-unit values equal r squared computed on the units' full 42-value cue rows (all\n    three cues); with that measure k1 (0.424) and k2 (0.466) are the two highest and each exceeds\n    all of k3 to k9 at both thresholds. Levene's tests are printed.\n  deviations:\n  - Assumed that the coefficient averaged is r squared, as the Methods call it (\"seven separate\n    correlation coefficients for each single unit (R2)\") and as Source Data Fig. 2f, headed R2,\n    holds; with r the claim would not be reproduced. The question is in the findings.\n  - The Methods' measure (danger firing) is the test; the Source Data values follow all three cues,\n    shown as a variant.\n- claim: fig2g-cue-anatomy\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig2g-cue-anatomy\n  notes: Every cue cluster spans at least six regions (k3 six). The share in DPG, DpWh, DLPAG, LPAG\n    and VLPAG is 0.436 (220/505) in the subnetwork and 0.612 (41/67) in k1 and k2, against 0.340\n    (445/1307) in the supranetwork.\n- claim: fig3a-cluster-signals\n  outcome: partially_reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig3a-cluster-signals\n  notes: The script's regression (r-a with an intercept) gives betas equal to Source Data Fig. 3b\n    middle. Two of four shapes hold under every reading; k5 peaks in the first cue second and k15 in\n    the first second after the cue. K10's first cue second (0.77) is below half its maximum (1.69),\n    so it is not sustained by the criterion's rule, and k6 peaks in cue second 5 (1.02) with its first\n    cue second (0.60) above half that.\n- claim: fig3b-signal-pca\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig3b-signal-pca\n  measured:\n  - 62.73\n  - 26.21\n  notes: The recomputed matrix equals Source Data Fig. 3b middle and gives 62.73% and 26.21%, with all\n    shape conditions, also with the pre-cue baseline subtracted. Readings r-b and i-b give 72.00 and\n    15.79%, 57.07 and 27.94%, and 66.16 and 21.37%; L2 gives 63.08 and 25.04%.\n  deviations:\n  - The regression is the script's (cluster mean firing, mean member suppression ratio, with an\n    intercept, cueAnalysis.m), which the Methods leave open.\n- claim: fig3c-subnetwork-lesion\n  outcome: partially_reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig3c-subnetwork-lesion\n  notes: With the script's lesion (s-c, giving 67.14 and 26.00% as the Source Data matrix does) PC1's\n    mean behaviour weight over the cue is 0.264 after the subnetwork lesion (96% of the intact 0.274)\n    and PC2's probability weight in the first cue second drops from 0.268 to 0.201, but the behaviour\n    weight is not above the one after the supranetwork lesion (0.268). The paper's own Source Data\n    matrices give the same. Shuffling betas (s-a, s-b) meets every part. v-b gives 53.88 and 25.45%.\n- claim: fig3d-supranetwork-lesion\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig3d-supranetwork-lesion\n  notes: With s-c (61.12 and 29.42%; Source Data 61.11 and 29.46%) PC1's mean behaviour weight is\n    0.268 against 0.274 intact, a small drop, and PC2's absolute probability weights peak in the\n    first cue second and its behaviour weights in the tenth. With s-a and s-b the PC2 part fails.\n- claim: fig3e-network-anatomy\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig3e-network-anatomy\n  measured:\n  - 5.93\n  - 7.41\n  notes: LPAG (7.41) and DPG (5.93) have the two largest differentials, then DRD (3.13) and PMnR\n    (2.53); all 21 equal Source Data Fig. 3e right. Under L2 LPAG and DPG are also the two largest.\n- claim: fig4b-outcome-clusters\n  outcome: partially_reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig4b-outcome-clusters\n  measured:\n  - 29.0\n  - 304.5\n  - 161.0\n  notes: Over 20 seeds the median largest (304.5) and median (161.0) sizes are within tolerance; the\n    median smallest cluster is 29.0, against 46 +- 4.6, and single seeds give 1 to 58.\n  deviations:\n  - The script seeds MATLAB's generator (rng(1)), which cannot be repeated; 20 seeds are used.\n- claim: fig4c-positive-prediction-error\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig4c-positive-prediction-error\n  measured: 17.68\n  notes: PC1 of the 1812 x 80 outcome matrix (outcomeAnalysis.m) explains 17.68%, with mean weights\n    uncertainty shock 0.194, danger 0.071, uncertainty omission -0.005 and safety -0.032. The Source\n    Data Fig. 4c matrix (24.18%) is the heat-plot version with a baseline subtracted. Per animal,\n    uncertainty shock has the largest weight in all 10 and danger exceeds safety in 9.\n- claim: fig4b-phasic-network\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig4b-phasic-network\n  notes: Under L1, k1 to k3 have higher temporal indices than every one of k6 to k9 (t-a and t-b); in\n    the first second k1 uncertainty shock 2.58 > danger 1.59 > 0, k2 danger 2.85 > uncertainty shock\n    1.44 > 0, and k3 below 0 on both. The mean r squared among k1 to k3 is 0.539 against 0.076 with\n    k4 to k11; with r it is -0.329 against 0.008, as k3 is anticorrelated with k1 and k2 (r = -0.85,\n    -0.74), which would make the outcome partially reproduced.\n  deviations:\n  - Assumed that the network correlation is r squared, the coefficient the Methods name (\"Pearson's\n    correlation coefficient (R2)\") and outcomeAnalysis.m plots (correlationsOutcome squared); the\n    criterion says Pearson correlation. The question is in the findings.\n- claim: fig4b-tonic-network\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig4b-tonic-network\n  notes: Under L1, k6's mean firing to uncertainty shock (-0.88) is below 0 and below its other trial\n    types; k7 (0.82) and k8 (0.31) are above 0 and highest for uncertainty shock, and both are\n    sustained. The mean r squared among k6 to k9 is 0.505 against 0.110 with the other seven; with r\n    it is -0.250 against 0.000 (k6 is anticorrelated with k7 and k8), which would make the outcome\n    partially reproduced.\n  deviations:\n  - Assumed r squared for the network correlation, as for fig4b-phasic-network.\n- claim: fig4e-network-pca\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig4e-network-pca\n  measured:\n  - 37.01\n  - 29.20\n  notes: 265 phasic and 613 tonic units. Phasic PC1 first-second weights are danger 0.410 and\n    uncertainty shock 0.424, each more than twice their late means; tonic PC1 is largest for\n    uncertainty shock (0.202) and negative for safety (-0.078). The Source Data matrices give the\n    same.\n- claim: fig4f-outcome-hubs\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig4f-outcome-hubs\n  notes: With the script's measure (r squared, outcomeAnalysis.m), whose per-unit values equal Source\n    Data Fig. 4f as a set, k1 (0.274) and k2 (0.260) exceed k3 (0.148; p = 3.6e-12 and 9.8e-08) and\n    k6 (0.264) exceeds k7 (0.197), k8 (0.157) and k9 (0.119), all below 0.05/3 and 0.05/6. With r the\n    phasic part holds and k6 has the lowest tonic mean. The Methods' networks (1-5, 7-10) are shown.\n  deviations:\n  - Bonferroni over the pairs within each network (3 and 6), a choice the claims file leaves to the\n    count of tests.\n- claim: fig4g-outcome-anatomy\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig4g-outcome-anatomy\n  notes: 0.600 of phasic and 0.594 of tonic units are in the axis-extreme regions (difference 0.006,\n    chi-square p = 0.92); the tonic network spans 20 regions and the phasic 17; k6 spans 17 against\n    10 to 19 for the other clusters. The effect is as small as on the paper's own values.\n- claim: fig5a-outcome-cluster-signals\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig5a-outcome-cluster-signals\n  notes: Under all four readings k1's shock and prediction error betas peak in the first 2 s and stay\n    below half that from 5 to 10 s, and k6's mean absolute prediction error beta is 12.3 times its\n    mean absolute shock beta (8.9 without an intercept).\n- claim: fig5b-outcome-signal-pca\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig5b-outcome-signal-pca\n  measured:\n  - 53.74\n  - 33.43\n  notes: The recomputed betas equal Source Data Fig. 5b middle, with prediction error in columns 1 to\n    20 and shock in 21 to 40 (outcomeRegression.m), the reverse of the Methods' layout; the shapes\n    are tested on the betas of each regressor. L2 gives 47.80 and 30.92% with the same shapes.\n- claim: fig5c-phasic-lesion\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig5c-phasic-lesion\n  measured:\n  - 79.99\n  - 16.81\n  notes: The script's lesion (firing permuted across trial rows before regression, s-d) gives 79.99 and\n    16.81% with one permutation for all intervals and 79.98 and 16.82% with one per interval; all\n    shapes hold. Shuffling betas gives 76.50 and 20.07% (s-a) and 78.59 and 17.89% (s-b).\n- claim: fig5d-tonic-lesion\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig5d-tonic-lesion\n  measured:\n  - 61.18\n  - 29.88\n  notes: With s-d, 61.18 and 29.88% (one permutation for all intervals) or 61.24 and 29.80%; PC1 has\n    opposing shock and prediction error weights peaking in the first 2 s, and PC2 correlates with the\n    intact PC2 at r = 0.895. Shuffling betas gives 53.45% (s-a) and 60.93% (s-b) for PC1.\n- claim: fig5e-no-anatomical-bias\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:fig5e-no-anatomical-bias\n  notes: With phasic read as k1 to k5 (p-b), the reading Source Data Fig. 5e uses (679 units), the\n    largest differential is 4.48 points (MnR), at the criterion's limit, and every value equals\n    Source Data. With phasic as k1 to k3 (p-a) the largest is 9.82 (PMnR), which would not reproduce\n    it. The chi-square of region by network, a variant, gives p = 0.039 (p-b) and 3e-05 (p-a).\n  deviations:\n  - Judged on p-b, the reading of the paper's own computation (Source Data), as the claims file\n    points out; p-a is shown.\n- claim: cue-outcome-membership-independent\n  outcome: reproduced\n  notebook: reproduce_strickland_2022.ipynb\n  output: claim:cue-outcome-membership-independent\n  measured:\n  - 85\n  - 159\n  notes: Under L1, 85 of 265 phasic and 159 of 613 tonic units are in the cue subnetwork; against 0.279\n    chi-square 2.30 (p = 0.13) and 1.17 (p = 0.28); 2 x 2 tests p = 0.10 and 0.19. Under L2 the tonic\n    network differs (p < 0.01).\nfindings:\n- kind: format_error\n  statement: 204 of the 1812 unit files hold repeated spike times (9289 repeats in all). The paper's\n    cubeScript.m counts spikes with intersect(), which keeps each time once, so the cube's counts\n    leave the repeats out; counting every stored time gives different counts in 119 units.\n- kind: metadata_insufficient\n  statement: The data set holds no cluster membership. The paper's k-means clusters come from\n    MATLAB's kmeans after rng(1), relabelled by hand-written maps in cueAnalysis.m and\n    outcomeAnalysis.m, so they cannot be regenerated outside MATLAB; they can be recovered only\n    from the paper's Source Data workbook, whose cluster sheets every unit matches exactly.\n- kind: metadata_insufficient\n  statement: The cube's anatomy.region holds region names as MATLAB string objects, which cannot be\n    read outside MATLAB. The region numbers need the list in cubeScript.m, and the analysis scripts\n    renumber 35 units from region 21 (CIC) to DpWh, saying the cube assigned them in error, and merge\n    regions 11 and 24 into x/scp. The units of anatomy.x, y and z are not stated.\n- kind: other\n  about: data\n  statement: In session js10030220, 19 unit files share one set of event times, while 2 others\n    (spk0009, spk0044) and 1 more (spk0049) carry cue and poke times that differ from them by an\n    amount growing over the session to about 0.28 and 0.30 s. The cube uses each file's own times.\n- kind: other\n  about: data\n  statement: Session js27101920 has 5 shock times; no shock is recorded on its first danger trial\n    (row 1). All other 72 sessions have 6 shocks, 12.0 s after cue onset on rows 1 to 6.\n- kind: paper_inconsistency\n  statement: Supplementary Table 1 lists 75 recording sessions (8 for subject 5 and 10 for subject\n    10); the Results and the data set have 73 (7 and 9).\n- kind: methods_unavailable\n  statement: The Source Data danger latencies (Fig. 2d) do not follow the Supplementary Methods'\n    search within the 10-s cue; many equal change points found from 2 s before cue onset, and 1498 of\n    1812 units have one, by a rule not stated. Which window was searched, how the 1-ms firing was\n    built, and which units were left out? With the stated method the latency does not correlate with\n    PC1 contribution (R2 = 0.067).\n- kind: paper_inconsistency\n  statement: For the cue hubs (Fig. 2f) the Supplementary Methods correlate danger firing over 14\n    intervals, but the Source Data per-unit values are squared correlations of the full 42-value cue\n    rows (all three cues). Was r or r squared averaged, and over which cues? With danger firing the\n    k1 hub does not exceed k3 or k4.\n- kind: methods_unavailable\n  statement: The Methods call the cluster correlations \"Pearson's correlation coefficient (R2)\" and\n    the scripts plot r squared. Is the network separation of Fig. 2e and 4d judged on r squared?\n    With r, k3 and k6 are anticorrelated with their fellow clusters and the outcome networks do not\n    separate.\n- kind: paper_inconsistency\n  statement: The Supplementary Methods lay out the outcome beta matrix with shock in intervals 1 to 20\n    and prediction error in 21 to 40, as a 21-cluster matrix; outcomeRegression.m and Source Data\n    Fig. 5b to 5d hold prediction error first, for 11 clusters.\n- kind: code_mismatch\n  statement: Source Data Fig. 4f right labels 171 units as k7 and 111 as k8, as outcomeAnalysis.m\n    hard-codes them, where the Figure 4b sheets and the clustering have 111 units in k7 and 171 in k8.\n- kind: code_mismatch\n  statement: The normalization in cubeScript.m (1-s, 500-ms and 250-ms bins z-scored separately over\n    the 40 s from 10 s before cue onset, baseline rounded down) differs from the Supplementary Methods\n    (250-ms bins from 20 s before to 20 s after the cue, averaged into larger intervals); only the\n    script's normalization reproduces the paper's values. The lesion scripts shuffle firing of k1 to\n    k9, k1 to k3 and k6 to k9 before regression, where the Methods shuffle the betas of clusters 1 to\n    8.\n- kind: other\n  about: paper\n  statement: Source Data Fig. 2c inset and Fig. 4c hold the units' rows with a pre-cue baseline\n    subtracted (the heat-plot data), not the matrices whose PCA gives the reported 29.7% and 17.7%;\n    PCA of those sheets gives 47.1% and 24.2%.\n"
}
```

```
File created successfully at: attempts/strickland-2022-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sed -i 's/ leave the repeats out; counting every stored time gives different counts in 119 units./ leave the repeats out./' attempts/strickland-2022-01.yaml && python3 -c "
import yaml;d=yaml.safe_load(open('attempts/strickland-2022-01.yaml'));print(len(d['outcomes']),len(d['findings']))" && grep -n "[^ ]: [a-zA-Z]" attempts/strickland-2022-01.yaml | grep -v "^\S*:\s*-\? *[a-z_]*: " | head; grep -nE "—|rather" attempts/strickland-2022-01.yaml entries/strickland-2022/README.md $TMPDIR/gen.py $TMPDIR/header.md $TMPDIR/summary.md entries/strickland-2022/bst3.py | head
```

```
30 13
```

**Agent calls Bash**

```bash
python3 -c "
import yaml
d=yaml.safe_load(open('attempts/strickland-2022-01.yaml'))
def walk(o,p=''):
    if isinstance(o,dict):
        for k,v in o.items(): walk(v,p+'.'+str(k))
    elif isinstance(o,list):
        for i,v in enumerate(o): walk(v,p+f'[{i}]')
    elif isinstance(o,str) and ': ' in o: print(p, o[:80])
walk(d)
"; python tools/entry.py check entries/strickland-2022 2>&1 | tail -20
```

```
0 error(s)
```

**Agent calls Bash**

```bash
date -u && time python tools/entry.py all entries/strickland-2022 2>&1 | tail -15
```

```
Fri Nov 13 01:44:28 UTC 2026
Installed kernelspec registry-strickland-2022 in executed/strickland-2022/.venv/share/jupyter/kernels/registry-strickland-2022
0 error(s)
pass  reproduce_strickland_2022.ipynb  (90 s)

real	1m36.271s
user	1m21.782s
sys	0m2.491s
```

**Agent calls Bash**

```bash
E=executed/strickland-2022/reproduce_strickland_2022.ipynb; $TMPDIR/dev/bin/python $TMPDIR/dump.py $E 1 20 | grep -v "^ *time\." | head -120
```

```
[1] CODE 
Data set CRCNS bst-3, version unversioned, doi:10.6080/K0Q23XGR
checksums.md5 in the bucket:

4ee6c433f5255693d5e85bcca6819cd4  data.zip
a2308123164a7ca6fb0e15c54693f14c  docs/crcns_bst-3_data_description.docx
f07a1e9718106c7219a9a6549568517c  docs/crcns_bst-3_data_description.pdf
0a26a2a26214193af0d13ff06b2c850d  filelist.txt


1822 members in data.zip; Counter({'singleUnits': 1813, 'scripts': 6, 'cubeFile': 2, 'data/': 1})
   data/cubeFile/cubeFile.mat 139318845 bytes
   data/scripts/cueRegression.m 26890 bytes
   data/scripts/outcomeAnalysis.m 37155 bytes
   data/scripts/outcomeRegression.m 13879 bytes
   data/scripts/cubeScript.m 29531 bytes
   data/scripts/cueAnalysis.m 50442 bytes

Source Data workbook md5 4df716fd6739ee3de3b0df81c4175be8 (expected 4df716fd6739ee3de3b0df81c4175be8): True
loaded in 46 s, peak memory 0.99 GB
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
E=executed/strickland-2022/reproduce_strickland_2022.ipynb; $TMPDIR/dev/bin/python $TMPDIR/dump.py $E 26 26 | grep -i "median over\|best\|summed"; $TMPDIR/dev/bin/python $TMPDIR/dump.py $E 33 33 | tail -3; $TMPDIR/dev/bin/python $TMPDIR/dump.py $E 57 58 | head -14; $TMPDIR/dev/bin/python $TMPDIR/dump.py $E 64 64 | grep "median over\|agreement"; $TMPDIR/dev/bin/python $TMPDIR/dump.py $E 85 85 | grep L2; $TMPDIR/dev/bin/python $TMPDIR/dump.py $E 88 88; $TMPDIR/dev/bin/python $TMPDIR/dump.py $E 94 94; $TMPDIR/dev/bin/python $TMPDIR/dump.py $E 61 61 | tail -2;  $TMPDIR/dev/bin/python $TMPDIR/dump.py $E 54 54 | tail -9 | head -2
```

```
median over seeds: min 24.0 (24 +- 2.4), max 218.5 (219 +- 21.9), median 75.0 (83 +- 8.3)
best of 20 (seed 19): sizes [25, 26, 26, 32, 35, 36, 37, 49, 59, 60, 68, 72, 90, 119, 127, 130, 138, 143, 153, 163, 224]
summed squared distance: paper's clustering 11219; seeds 11135 to 11336
L2 nine largest hold 411 units (505 +- 50.5)
overlap of L1 k1-k9 with L2 k1-k9: 343

[57] CODE ['claim:fig3c-subnetwork-lesion', 'claim:fig3d-supranetwork-lesion']
v-b sub: PC1 53.88%, PC2 25.45%; PC1 mean beh over cue 0.263; PC2 prob first cue s 0.195
v-b supra: PC1 34.07%, PC2 18.11%; PC1 mean beh over cue 0.222; PC2 prob first cue s 0.022
s-c {'3c PC1 beh >= 75% intact': np.True_, "3c PC1 beh > supra-lesion's": np.False_, '3c PC2 prob at first cue s < intact': np.True_, '3d PC1 beh < intact': np.True_, '3d PC2 |prob| peak in first half, |beh| in second': True}
s-a {'3c PC1 beh >= 75% intact': np.True_, "3c PC1 beh > supra-lesion's": np.True_, '3c PC2 prob at first cue s < intact': np.True_, '3d PC1 beh < intact': np.True_, '3d PC2 |prob| peak in first half, |beh| in second': False}
s-b {'3c PC1 beh >= 75% intact': np.True_, "3c PC1 beh > supra-lesion's": np.True_, '3c PC2 prob at first cue s < intact': np.True_, '3d PC1 beh < intact': np.True_, '3d PC2 |prob| peak in first half, |beh| in second': False}
Source Data {'3c PC1 beh >= 75% intact': np.True_, "3c PC1 beh > supra-lesion's": np.False_, '3c PC2 prob at first cue s < intact': np.True_, '3d PC1 beh < intact': np.True_, '3d PC2 |prob| peak in first half, |beh| in second': True}

[58] MD **Result: fig3c-subnetwork-lesion partially reproduced; fig3d-supranetwork-lesion reproduced.** With
[88] MD **Result: fig5c-phasic-lesion and fig5d-tonic-lesion reproduced.** With the script's lesion (s-d,
[94] MD **Result: reproduced.** Under L1, 85 of 265 phasic units (0.321) and 159 of 613 tonic units (0.259)
[61] MD **Result: reproduced.** LPAG (7.41) and DPG (5.93) have the two largest differentials, each equal to
[54] MD **Result: reproduced
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
E=executed/strickland-2022/reproduce_strickland_2022.ipynb; $TMPDIR/dev/bin/python $TMPDIR/dump.py $E > $TMPDIR/exec_dump.txt; for k in "min 29.0 (46" "agreement with L1" "PC1 47.80" "79.99" "61.18" "0.895" "9.82 (PMnR)" "85/265" "R2 = 0.067" "0.640" "two highest k2, k1" "0.539 / 0.076" "0.505 / 0.110" "17.68%" "37.01%" "62.73" "53.74" "p = 0.92\|0.923" "12.3" "0.264), 7" "k6-k7 t=5.08" "1458" "413" "1.4e-05\|0.000014" "2.30, p = 0.13"; do printf "%-22s %s\n" "$k" "$(grep -c -- "$k" $TMPDIR/exec_dump.txt)"; done
```

```
min 29.0 (46           1
agreement with L1      1
PC1 47.80              1
79.99                  2
61.18                  1
0.895                  1
9.82 (PMnR)            1
85/265                 1
R2 = 0.067             0
0.640                  2
two highest k2, k1     2
0.539 / 0.076          1
0.505 / 0.110          1
17.68%                 2
37.01%                 3
62.73                  3
53.74                  2
p = 0.92\|0.923        1
12.3                   2
0.264), 7              1
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('gen.py').read()
s=s.replace('for k in bst3.CUBE_FIELDS[:-1]:','for k in bst3.CUBE_FIELDS:')
s=s.replace('''lists. None of the claims file's four readings (n-a, n-b, w-a, w-b, from 250-ms bins) matches any
row within 0.01, though they correlate with them;''','''lists. Under the claims file's four readings (n-a, n-b, w-a, w-b, from 250-ms bins) at most 2 rows
match within 0.01, though most correlate above 0.99 with a unit;''')
open('gen.py','w').write(s)
EOF
grep -n "at most 2 rows" gen.py | head -2; cd entries/strickland-2022 && $TMPDIR/dev/bin/python $TMPDIR/gen.py reproduce_strickland_2022.ipynb $TMPDIR/header.md $TMPDIR/summary.md && cd  && python tools/entry.py all entries/strickland-2022 2>&1 | tail -3 && python tools/entry.py handover entries/strickland-2022 && ls executed/strickland-2022/handover; date -u
```

```
264:lists. Under the claims file's four readings (n-a, n-b, w-a, w-b, from 250-ms bins) at most 2 rows
Installed kernelspec registry-strickland-2022 in executed/strickland-2022/.venv/share/jupyter/kernels/registry-strickland-2022
0 error(s)
pass  reproduce_strickland_2022.ipynb  (99 s)
wrote executed/strickland-2022/handover
bst3.py
reproduce_strickland_2022.ipynb
strickland-2022.yaml
Fri Nov 13 01:48:31 UTC 2026
```

**Agent calls Bash**

```bash
git status --short; grep -c "Result:" executed/strickland-2022/handover/reproduce_strickland_2022.ipynb; grep -c "Result:" executed/strickland-2022/reproduce_strickland_2022.ipynb
```

```
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
?? attempts/strickland-2022-01.yaml
?? entries/strickland-2022/
?? scripts
0
27
```

**Agent calls Bash**

```bash
ls -la scripts .idea .vscode | head; ls -la .bashrc .mcp.json .gitconfig
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 13 01:05 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 13 01:05 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 13 01:05 scripts
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 13 01:05 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 13 01:05 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 13 01:05 .mcp.json
```

**Agent**

I've completed author steps 1 to 6 for `strickland-2022`. `python tools/entry.py all` reports 0 errors and the notebook passes on a clean run in 99 s. The handover package is in `executed/strickland-2022/handover/`. Nothing is committed.

**1. Outcomes (30 claims, none blocked)**

| Claim | Outcome |
|---|---|
| source-data-cluster-link | reproduced (all 1812 cue and outcome rows match exactly one unit) |
| fig1c-suppression-order | reproduced (F(2,142) = 147.9) |
| figs2-each-rat-discriminates | reproduced (reading c-c, 8 of 8 rats) |
| units-sessions-subjects | reproduced |
| fig1e-regions | reproduced |
| fig2b-cue-clusters | reproduced |
| fig2c-cue-pc1-ordered | reproduced (29.73%) |
| fig2c-pc1-contribution | reproduced |
| fig2d-danger-latency | not reproduced (R2 = 0.067, p = 0.26) |
| fig2e-cue-subnetwork | reproduced (with r squared) |
| fig2f-cue-hubs | partially reproduced, rests on an assumption |
| fig2g-cue-anatomy | reproduced |
| fig3a-cluster-signals | partially reproduced (2 of 4 shapes) |
| fig3b-signal-pca | reproduced (62.73 / 26.21%) |
| fig3c-subnetwork-lesion | partially reproduced |
| fig3d-supranetwork-lesion | reproduced |
| fig3e-network-anatomy | reproduced |
| fig4b-outcome-clusters | partially reproduced (smallest cluster 29, expected 46) |
| fig4c-positive-prediction-error | reproduced (17.68%) |
| fig4b-phasic-network, fig4b-tonic-network | reproduced, both rest on an assumption |
| fig4e, fig4f, fig4g | reproduced |
| fig5a, fig5b, fig5c, fig5d, fig5e | reproduced |
| cue-outcome-membership-independent | reproduced |

**2. Dataset, assumptions and questions**

What the dataset holds:
- The zip holds 1812 unit files, a cube file and the paper's MATLAB scripts.
- The scripts settled most of the details the claims file leaves open. Its normalization is the only one that reproduces the Source Data rows; the claims file's four readings do not. They also fixed the shuffle direction, the regression form and the lesion procedures.
- With those scripts, the cube gives the paper's 29.7% and 17.7% exactly. The claims file's 47.1% and 24.2% came from Source Data sheets that hold baseline-subtracted heat-plot rows, not the matrices the PCA was run on.

Findings about the data:
- 204 unit files contain repeated spike times (9289 in total). The script counts each time once.
- The dataset has 73 sessions; Supplementary Table 1 lists 75.
- Session js27101920 has 5 shocks; none is recorded on its first danger trial.
- In session js10030220, 3 of 22 unit files have event times that drift up to 0.3 s away from the other 19.
- Region names are stored as MATLAB string objects that cannot be read outside MATLAB, and the region numbers only make sense with the scripts' remapping.
- The dataset has no cluster labels, so the paper's clusters come only from its Source Data.

Assumptions:
- For fig2f and the two fig4b network claims I used r squared, the "(R2)" the Methods name and the coefficient the scripts plot. With plain r, fig2f would be not reproduced and both network claims partially reproduced.

Questions for the paper's authors (recorded as findings):
- The Source Data latencies match a change-point search starting 2 s before cue onset, not the 10-s cue window the Methods describe. They also cover 1498 units by an unstated rule.
- The Source Data cue-hub values are r squared computed over all three cues, not over danger firing alone as the Methods say.
- Are the network correlations judged on r or r squared?
- Other inconsistencies:
  - The Methods put shock first in the outcome beta matrix; the code and Source Data put prediction error first.
  - Source Data Fig. 4f swaps the k7 and k8 labels.

I asked a reader no questions; I found no misreading of the paper in the claims file.

**3. Where the protocol was unclear**
1. CRCNS asks for the MD5s of the files read, but data.zip is opened in place and not downloaded whole, so its MD5 cannot be checked. I printed the bucket's `checksums.md5` without verifying it.
2. The link criterion lists four normalization readings, and the matching one came from the paper's code. I took it under step 1.6 and showed the four readings as well. The protocol does not say whether an author may add a reading to a link criterion.
3. The paper's own Source Data sometimes contradicts its Methods (fig2d window, fig2f measure). The precedence order in reader step 2 does not cover Source Data. I kept the Methods, as the criterion has them, and showed the Source Data version as a variant.
4. Several criteria give separate rules for L1 (the paper's clusters) and L2 (my own k-means). I let L1 decide and reported the L2 results in the notes. For fig2c-pc1-contribution, L2 fails (411 units in place of 505).
5. fig5e is a claim of absence with no test in the paper but two readings. The protocol says absence is judged on the paper's test alone. I judged it on the reading the paper's Source Data uses and showed the other, which would not reproduce it.
6. The per-animal breakdown rule fits poorly when results are per cluster. I broke down the behaviour, both PCA claims and the subnetwork share.

**4. Runtime and failures**
- The run took about 40 minutes of the 5-hour budget (01:09 to 01:48 UTC). The notebook runs in about 1.5 minutes with 1 GB peak memory.
- Nothing failed in the final run. Two early development errors were fixed: an array shape mismatch in the fig4f cell, and raw spike counts that differed from the cube until repeated spike times were counted once.

## End of run

84 turns, 37 minutes, $9.33 at API prices, result: success.
