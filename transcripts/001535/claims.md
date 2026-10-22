# 001535 · claims · run 39594967114

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/001535 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -l paper/*.txt; head -40 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,140p claims/001453/*.yaml | tail -110; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cell.2025.02.001.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "statistics:" -A8 claims/001453/*.yaml | grep -E "about|ci|corrected|n:" | head -20; grep -rn "with_inputs\|elsewhere\|where:" claims/*/*.yaml | head -5; grep -l "open\b" claims/*/*.yaml | head
```

```
54-  - test: two-way ANOVA, main species effect
56-    p_relation: "<"
57-  criterion: Tested without stimulus names, over all 21 stimulus codes. For each fish and code
59-    of these values on species, code and their interaction. Reproduced when the species effect
61-- id: fig1d-median-velocity
68-  - test: two-way ANOVA, main species effect
70-    p_relation: "<"
72-  depends_on:
75-  - quantity: DC median velocity over whole-field stimuli
129-    p_relation: "<"
130-    n: 26 ZF and 12 DC fish
131-  criterion: Per stimulus, ZF against DC fish-by-stimulus median speeds with Tukey's HSD on the
149-    p_relation: "<"
151-  depends_on:
153-  criterion: For each fish, the mean of its median angular velocities for the rightward
167-    p_relation: "<"
168-    corrected: Bonferroni
170-  depends_on:
172-  criterion: Angular acceleration as the Methods define it (degrees per second squared), from
238-    p_relation: ">"
[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cell.2025.02.001.txt",
 "offset": 6,
 "limit": 60
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '{print NR": "length($0)": "substr($0,1,100)}' paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 7p paper/*.txt | fold -s -w 1000 > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 70
}
```

```
1	pmc Cell Cell 319 nihpa 0413066 Cell 0092-8674 1097-4172 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC11932800 PMC11932800.1 11932800 11932800 NIHMS2059472 40054446 10.1016/j.cell.2025.02.001 NIHMS2059472 NIHPA2059472 1 Article Sampling representational plasticity of simple imagined movements across-days enables long-term neuroprosthetic control Natraj N. 1 2 Seko S. 1 Abiri R. 1 Miao R. 1 * Yan H. 1 * Graham Y. 1 * Tu-Chan A. 1 2 Chang E. F. 3 Ganguly K. 1 2 1 Department of Neurology, Weill Institute for Neurosciences, University of California-San Francisco, San Francisco, California, USA. 2 VA San Francisco Healthcare System, San Francisco, California, USA. 3 Department of Neurological Surgery, Weill Institute for Neuroscience, University of California-San Francisco, San Francisco, California, USA. * these authors contributed equally Contributions N.N. designed the study, designed and implemented the real-time BCI signal processing system, decoders, 
2	the hDoF framework, performed experiments, analyzed data, and drafted the manuscript. S.S. implemented the real-time Kinova Jaco, the hDoF framework, performed experiments and aided in manuscript drafting. R.A. performed the initial calibration of the Kinova Jaco, performed experiments, and aided in real-time system design. H.Y., R.M. and Y.G. aided in data collection and analyses. A.T.C. conducted patient recruitment and patient care. E.F.C. performed the surgical implantation and patient care. K.G. conceived and supervised all aspects. Lead contact: [removed: an e-mail address] 06 3 2025 188 5 485051 1208 1225.e32 05 03 2025 06 03 2026 06 03 2026 26 03 2025 23 09 2026 This file is available for text mining. It may also be used consistent with the principles of fair use under the copyright law. Flexible regulation of representations on a drifting manifold enables long-term stable complex neuroprosthetic control 14 8 2023 2023.08.11.551770 bioRxiv 10.1101/2023.08.11.551770 PMC10462094
[... 68 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 71,
 "limit": 70
}
```

```
71	between movements’ neural distributions pairwise ( Fig. 1K – L ), each trial’s streaming power in the three frequency features were individually averaged in bins of non-overlapping 200ms bins and temporally smoothed, thereby down sampling the data. We then z-scored each feature’s down sampled data across all trials within each session, capturing normalized neural differences between movements independent of session-specific fluctuations. Down sampled and z-scored trials from all sessions were then concatenated together, forming the dataset for each movement that were then used for pairwise representational similarity analyses. Spatial feature extraction for somatotopic decoders, autoencoders and BCI experiments (MLP-based Fig. 2 – 6 and Fig. S3 ) For neural decoding using only spatial activity patterns with the MLP, we computed the binned power of the streaming neural activity in three frequency bands at each channel of the grid: δ ( 0.5 – 4 H z ) , β ( 13 – 30 H z ) and γ H ( 70 - 
72	150 H z ) . The temporal width of the bins was dependent on the decoder update rate, which typically was set at 5Hz, though we piloted a range between 5 and 10Hz. For example, a decoder running at 5Hz would bin neural activity with 200ms intervals. Third-order Butterworth Infinite Impulse Response band-pass filters were used to extract the neural features real-time. To compute power more accurately in the slower δ band, the real-time PC had a running circular 2s buffer that was updated with raw neural activity at the decoder update rate. The filter was then applied to the entire 2s buffer and the most recent bin-width of δ band filtered activity was extracted. To compute power at the channel level, each sample of the filtered signal within the bin was squared and then averaged over time with a log transform to get an estimate of binned δ power. For faster rhythms, we utilized a filter bank approach before computing power and without the need for a running buffer. β power at each 
7
[... 67 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 141,
 "limit": 70
}
```

```
File content (27539 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 141,
 "limit": 35
}
```

```
141	information-theoretic measure of decoder performance 101 , given by the following formula B R = l o g 2 ( C - 1 ) × m a x 0 , N a c c - N f a i l T where C is the total number of classes or targets, N acc is the number of trials that were correctly decoded within a block of trials, N fail is the number of trials that were inaccurately decoded within a block of trials and T is the total time taken within the block of trials including time taken for both accurate and inaccurate trials. Using regression analyses, we also assessed whether there was any linear slope in the evolution of the median decoding accuracy of each session across the PnP experimental window. This was done for both B1’s PnP experiments and for B3’s single PnP experiment ( Fig. S8C – E ). Coactivations of representations ( Fig. S8G ) Coactivated data representations were collected across multiple trials for combinations of imagined right hand movement with imagined left leg and imagined head movements as well as 
142	single movements. The successful performance of a decoder in each trial (discerning individual and dual coactivated movements) was ascertained by a max-vote strategy. A confusion matrix denoting performance from trials across sessions is shown in Fig. S8G . Representational analyses of denovo BCI velocity commands with the ReFit Kalman Filter ( Fig. S7 ) We performed latent-space representational analyses for end-effector velocity commands with the ReFit-KF in a manner analogous to discrete representations. This analyses was done only with B1. Similar to the well-rehearsed discrete movements, we built a daily autoencoder to capture neural representations of velocity commands to center-out targets in the 3D virtual workspace using a daily initialized ReFit-KF. We carried out five days of daily initialization with the ReFit-KF. We demarcated neural data into six labeled classes, for each of the six center-out targets in the 3D workspace. Given that continuous velocity commands span th
[... 33 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 176,
 "limit": 35
}
```

```
176	final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain. References 1. Rule ME , O’Leary T , and Harvey CD ( 2019 ). Causes and consequences of representational drift . Current opinion in neurobiology 58 , 141 – 147 . 31569062 10.1016/j.conb.2019.08.005 PMC7385530 2. Clopath C , Bonhoeffer T , Hübener M , and Rose T ( 2017 ). Variance and invariance of neuronal long-term representations . Philosophical Transactions of the Royal Society B: Biological Sciences 372 , 20160161 . 28093555 10.1098/rstb.2016.0161 PMC5247593 3. Schoonover CE , Ohashi SN , Axel R , and Fink AJ ( 2021 ). Representational drift in primary olfactory cortex . Nature 594 , 541 – 546 . 34108681 10.1038/s41586-021-03628-7 4. Miller KJ , Leuthardt EC , Schalk G , Rao RP , Anderson NR , Moran DW , Miller JW , and Ojemann JG ( 2007 ). Spectral changes in cortical surface potentials during motor 
177	movement . Journal of Neuroscience 27 , 2424 – 2432 . 17329441 10.1523/JNEUROSCI.3886-06.2007 PMC6673496 5. Lotze M , Erb M , Flor H , Huelsmann E , Godde B , and Grodd W ( 2000 ). fMRI evaluation of somatotopic representation in human primary motor cortex . Neuroimage 11 , 473 – 481 . 10806033 10.1006/nimg.2000.0556 6. Meier JD , Aflalo TN , Kastner S , and Graziano MS ( 2008 ). Complex organization of human primary motor cortex: a high-resolution fMRI study . Journal of neurophysiology 100 , 1800 – 1812 . 18684903 10.1152/jn.90531.2008 PMC2576195 7. Schellekens W , Petridou N , and Ramsey NF ( 2018 ). Detailed somatotopy in primary motor and somatosensory cortex revealed by Gaussian population receptive fields . Neuroimage 179 , 337 – 347 . 29940282 10.1016/j.neuroimage.2018.06.062 PMC6413921 8. Degenhart AD , Hiremath SV , Yang Y , Foldes S , Collinger JL , Boninger M , Tyler-Kabara EC , and Wang W ( 2018 ). Remapping cortical modulation for electrocorticographic brain–computer 
17
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001535/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:3000])"; curl -s "https://api.dandiarchive.org/api/dandisets/001535/versions/draft/" | python -c "import json,sys;d=json.load(sys.stdin);print(d.get('name'));print(d.get('description'));print(d.get('relatedResource'));print(d.get('version'))"
```

Result: the fetched text is not kept.

**Agent**

Full text is present (PMC author manuscript, Methods and supplementary legends included). The dataset holds B1's RNN training trials. Now checking the linked code on OSF.

**Agent calls Bash**

```bash
curl -s "https://api.osf.io/v2/nodes/tbdwg/" | python -c "import json,sys;d=json.load(sys.stdin)['data'];print(d['attributes']['title'],d['attributes']['date_modified'])"; curl -s "https://api.osf.io/v2/nodes/tbdwg/files/osfstorage/?page[size]=100" | python -c "
import json,sys
d=json.load(sys.stdin)
for f in d['data']: a=f['attributes'];print(a['kind'],a['name'],a.get('size'),a.get('date_modified'),f['links'].get('download'), f['relationships']['files']['links']['related']['href'] if a['kind']=='folder' else '')"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s -g "https://api.osf.io/v2/nodes/tbdwg/files/osfstorage/" | head -c 3000; echo; curl -s "https://api.osf.io/v2/nodes/tbdwg/children/" | head -c 1500
```

Result: the fetched text is not kept.

**Agent**

Let me walk the OSF tree recursively.

**Agent calls Bash**

```bash
cat > $TMPDIR/osf.py <<'EOF'
import json, urllib.request
def get(u):
    out=[]
    while u:
        d=json.load(urllib.request.urlopen(u))
        out+=d['data']; u=d['links'].get('next')
    return out
def walk(u, depth=0):
    for f in get(u):
        a=f['attributes']
        if a['kind']=='folder':
            print('  '*depth+a['name']+'/')
            walk(f['relationships']['files']['links']['related']['href']+'?page[size]=100', depth+1)
        else:
            print('  '*depth+a['name'], a['size'], a['date_modified'], f['links']['download'])
walk('https://api.osf.io/v2/nodes/tbdwg/files/osfstorage/?page[size]=100')
EOF
python $TMPDIR/osf.py
```

```
BCI/
  bci.zip 17742715 2025-02-26T18:16:20.247685 https://osf.io/download/4gdah/
```

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL -o bci.zip https://osf.io/download/4gdah/ && sha256sum bci.zip && unzip -o -q bci.zip -d bci && find bci -type f | grep -v __MACOSX | head -100; find bci -type f | wc -l
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/bci && find . -type f | grep -v __MACOSX | sed -n 100,400p | grep -v task_modules; find . -maxdepth 3 -type d | grep -v MACOSX
```

```
./bci/task_helpers/pool_features.m
./bci/task_helpers/OptimalCursorUpdate1D.m
./bci/task_helpers/OptimalCursorUpdate.m
./bci/task_helpers/LoadLQR2dDynamics.m
./bci/task_helpers/LoadFeatureMask.m
./bci/task_helpers/InTargetRobot3D2.m
./bci/task_helpers/InTargetRobot3D.m
./bci/task_helpers/InTargetRobot.m
./bci/task_helpers/InTargetRadial.m
./bci/task_helpers/InTargetMulti2D.m
./bci/task_helpers/InTargetKeyboard.m
./bci/task_helpers/InTargetGrid.m
./bci/task_helpers/InTargetCenterOut1D.m
./bci/task_helpers/InTargetCenterOut.m
./bci/task_helpers/InstructionScreen.m
./bci/task_helpers/HandDecoder.m
./bci/task_helpers/get_lstm_features_robotBatch.m
./bci/task_helpers/get_lstm_features_9DoF.m
./bci/task_helpers/get_lstm_features.m
./bci/task_helpers/GenerateCursorTraj1D.m
[... 297 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bci/bci/task_helpers && wc -l ToTrainDiscreteModel_7DoF_LSTM.m get_lstm_features*.m extract_lstm_features.m data_augment.m runningMode.m; cat ToTrainDiscreteModel_7DoF_LSTM.m
```

```
278 ToTrainDiscreteModel_7DoF_LSTM.m
  376 get_lstm_features.m
  441 get_lstm_features_9DoF.m
  370 get_lstm_features_robotBatch.m
   27 extract_lstm_features.m
   83 data_augment.m
   32 runningMode.m
 1607 total
%% FINE TUNING LSTM MODEL FOR A BATCH UPDATE ON ARROW DATA

clc;clear
addpath '[removed: a home directory path]/Projects/bci/task_helpers/'
addpath '[removed: a home directory path]/Projects/bci/clicker/'
addpath '[removed: a home directory path]/Projects/bci/lstm_models/'

root_path = '[removed: a home directory path]/Data/bravo1/';
foldernames = {'20230419'};
lstm_folder_path = '[removed: a home directory path]/Projects/bci/lstm_models/';
clicker_path = '[removed: a home directory path]/Projects/bci/clicker/';

[... 260 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bci/bci/task_helpers && cat get_lstm_features.m extract_lstm_features.m
```

```
function [XTrain,XTest,YTrain,YTest] = get_lstm_features(files,Params,lpFilt,chmap)



disp('Getting the data for LSTM')
% get the raw data
D1={};
D2={};
D3={};
D4={};
D5={};
D6={};
D7={};
for j=1:length(files)
    try
        load(files{j})
        file_loaded = true;
    catch
        file_loaded=false;
        disp(['Could not load ' files{j}]);
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bci/bci && cat task_helpers/runningMode.m; python - <<'EOF'
import zipfile,re
z=zipfile.ZipFile('README.docx');x=z.read('word/document.xml').decode()
print(re.sub(r'<[^>]+>',' ',x.replace('</w:p>','\n'))[:6000])
EOF
grep -rn "TargetID\b\|ReachTargets\|TargetID ==\|TargetID==" task_modules/Robot3DArrow/*.m | head -20
```

```
function modeVal = RunningMode(v)

n(1) = sum(v == 1);
n(2) = sum(v == 2);
n(3) = sum(v == 3);
n(4) = sum(v == 4);
n(5) = sum(v == 5);
n(6) = sum(v == 6);
n(7) = sum(v == 7);
n(8) = sum(v == 8);
n(9) = sum(v == 9);
n(10) = sum(v == 10);
n(11) = sum(v == 11);
n(12) = sum(v == 12);
n(13) = sum(v == 13);
n(14) = sum(v == 14);


maxVal = max(n);
idx = find(n == maxVal);
[... 115 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bci/bci && sed -n 160,180p task_modules/Robot3DArrow/GetParams.m; sed -n 320,345p task_modules/Robot3DArrow/GetParams.m; grep -n "ReachTargetPositions\|Thumb\|thumb\|Tongue\|tongue" task_modules/Robot3DArrow/GetParams.m | head; grep -rn "thumb\|Thumb" --include=*.m --include=*.py . | head -20
```

```
%% ADAPTIVE BASELINE FLAG 
% data is baseline to state 1 data
Params.AdaptiveBaseline = false;

%% POOLING CHANNELS FOR CONTROL
% set this 1 only during online control
Params.ChPooling = false; 

%% Targets: radial layout
Params.NumReachTargets   = 9;
Params.TargetSpacing     = 10; % px
Params.OuterCircleRadius = 350; % defines outer edge of target
Params.InnerCircleRadius = 150; % defines inner edge of target
% Params.ReachTargetRadius = .5*(Params.InnerCircleRadius + Params.OuterCircleRadius);

Params.ReachTargetRadius = 200;
dl    = Params.ReachTargetRadius/sqrt(2);


Params.ReachTargetPositions = [Params.ReachTargetRadius, 0, 0;...
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/bci/bci && sed -n 179,190p task_modules/Robot3DArrow/GetParams.m; sed -n 36,50p task_modules/RealRobotBatch/RunTrial.m; grep -rn "Head\|head\b" task_modules/Robot3DArrow/*.m RobotSim/interfaces.py | head; grep -n "TargetName\|Name =" task_modules/Robot3DArrow/*.m | head
```

```
Params.ReachTargetPositions = [Params.ReachTargetRadius, 0, 0;...
    0, Params.ReachTargetRadius, 0; ...
    -Params.ReachTargetRadius, 0, 0;...
    0, -Params.ReachTargetRadius, 0; ...
    0,0,Params.ReachTargetRadius;...
    0, 0,-Params.ReachTargetRadius;...
    0,0,0;...
    0.5*Params.ReachTargetRadius,0,40;... % wrist rotation
    -0.5*Params.ReachTargetRadius,0,40;...; % wrist rotation
    dl,-dl,0;...  %  diagonals
    dl, dl,0;
    -dl, dl, 0;...
ReachTargetPos = Data.TargetPosition;
TargetID = 0; % Target that cursor is in, 0 for no targets

% Output to Command Line
fprintf('\nTrial: %i\n',Data.Trial)

TargetName = {'Right Thumb', 'Left Leg', 'Left Thumb', 'Right Wrist', 'Lips', 'Tongue', 'Both Middle Fingers', 'Right Wrist', 'Left Wrist'};

[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,200p tools/claims_check.py
```

```
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path

[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
cat schemas/claims.schema.json | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1))" | head -250
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "dataset",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "The dataset the claims are tested on: the archive and the dataset's identifier there.",
   "type": "object",
   "additionalProperties": false,
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
cat schemas/claims.schema.json | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d['\$defs'],indent=1))"
```

```
{
 "expected": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "quantity",
   "value"
  ],
  "properties": {
   "quantity": {
    "type": "string"
   },
   "value": {
    "type": "number"
   },
   "tolerance": {
    "type": "number",
    "minimum": 0
   },
   "unit": {
[... 82 more lines not kept]
```

**Agent**

The code archive is the real-time BCI system: task modules, feature extraction, and the LSTM fine-tuning scripts. It does not contain the offline analysis code. Next I'm writing the claims file.

**Agent calls Bash**

```bash
cd $TMPDIR/bci/bci && sed -n 1,83p task_helpers/data_augment.m | head -40; grep -n "split\|0.8\|0.85\|randperm" task_helpers/get_lstm_features_robotBatch.m | head; grep -rn "log2\|bitrate\|BitRate" --include=*.m . | head -5; grep -n "Threshold\|RunningModeBinNum\|UpdateRate" task_modules/Robot3DArrow/GetParams.m | head
```

```
function [D1, D2, D3, D4, D5, D6, D7] =  data_augment(D1, D2, D3, D4, D5, D6, D7)



A=D1';
B=D2';
C=D3';
D=D4';
E=D5';
F=D6';
G=D7';

%%%augment the training data (feature by feature)
D11={};
D11 = cat(2,D11,A,B,C,D,E,F,G);
aug_factor=4; % can be changed
for i=1:length(D11)
    tmp = D11{i};
    len = size(tmp,1);
    % delta
[... 29 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/001535/10.1016-j.cell.2025.02.001.yaml",
 "content": "# Claims for Natraj, Seko, Abiri, Miao, Yan, Graham, Tu-Chan, Chang & Ganguly (2025), Cell 188,\n# 1208-1225, on dandiset 001535.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21, protocol\n# pilot-10 as stated in docs/protocol.md (Reader).\n#\n# Text read: the accepted author manuscript in PubMed Central (PMC11932800, NIHMS2059472), full\n# text as served by ncbi_pmc (paper/10.1016-j.cell.2025.02.001.txt): Results, Discussion, STAR\n# Methods, the main figure legends and the supplementary legends (Figures S1 to S9, Videos S1 to\n# S4, Supplementary Method S1). It is not the version of record. The supplement is present only as\n# its legends; Supplementary Method S1 (a timeline schematic) and the supplementary figures\n# themselves were not read, and no PDF was supplied. No claim needs a value that appears only in a\n# figure image.\n#\n# Code read: the paper links \"exemplar real-time BCI and neural signal processing code and\n# decoders\" at OSF (doi:10.17605/OSF.IO/TBDWG), one file BCI/bci.zip (17742715 bytes, modified\n# 2025-02-26, sha256 575149d40829d135557d17cd5247c85a0d333033467f8c25df281bef8ddb091a). It holds the\n# MATLAB real-time task modules (Robot3DArrow, RealRobotBatch, RobotR2GModeSwitch and others), the\n# feature pipeline (neuro/), Kalman filter code, the PyBullet robot simulator, trained decoders\n# (clicker/*.mat) and scripts that fine-tune the biLSTM (task_helpers/ToTrainDiscreteModel_7DoF_LSTM.m,\n# get_lstm_features.m, extract_lstm_features.m) and run the mode filter (runningMode.m). It holds no\n# offline analysis code: none of the statistics of Figures 1 to 7 (autoencoders, Mahalanobis\n# distances, CKA, mixed models, robust regression) is implemented there. Details the code settles\n# are cited as \"OSF code\" in the criteria. Where it disagrees with the Methods:\n#   - The RNN fine-tuning script splits segments 80% training and 20% validation; the Methods give\n#     85% and 15% for the initial RNN training.\n#   - RealRobotBatch/RunTrial.m names targets 1 to 7 as Right Thumb, Left Leg, Left Thumb, Right\n#     Wrist, Lips, Tongue, Both Middle Fingers, while Robot3DArrow/GetParams.m places targets 1 to 7\n#     at +X, +Y, -X, -Y, +Z, -Z and the origin, and the Methods map X+ to right thumb, X- to left\n#     thumb, Y+ to head, Y- to left leg, Z+ to tongue, Z- to lips and the origin to both middle\n#     fingers. The Methods come first; the code's names are a variant the author must check\n#     against whatever labels the dataset carries.\n#   - The code computes the high-gamma feature as the mean of the squared output of eight\n#     third-order Butterworth band-pass filters (70 to 150 Hz), low-pass filters the LFO with a\n#     fourth-order IIR at 25 Hz, resamples both from 1 kHz to 100 Hz, cuts 1000 ms segments starting\n#     every 500 ms plus a 0 to 100 ms jitter, replaces channels exceeding 15 (z units) with 1e-5\n#     Gaussian noise, and L2-normalizes the 128 high-gamma and 128 LFO columns separately. The\n#     Methods agree in substance (256-dimensional input, down-sampling by 10, artifact replacement,\n#     L2 norm of each feature matrix, segments of 800 to 1000 ms overlapping by at most 50%).\n#\n# The data the paper used (as the paper reports them):\n#   - Participants: B1 (male, 41, right-handed, 128-channel ECoG, 8x16 grid, 4 mm spacing, left\n#     sensorimotor cortex) and B3 (female, 47, 253-channel ECoG, 23x11 grid, 3 mm spacing), both\n#     with tetraparesis and anarthria from brainstem stroke. Signals at 1 kHz, common median\n#     referenced, z-scored to a 2 min resting baseline at the start of each session.\n#   - Figure 1 (imagined movement task, no BCI control): 30 actions in B1 (49 trials per action) and\n#     32 in B3 (48 trials per action); trial of 4 s text cue, 2 s red square (get ready), 4 s green\n#     square (imagine), 3 s ITI. Features delta (0.5 to 4 Hz), beta (13 to 30 Hz) and high gamma\n#     (70 to 150 Hz).\n#   - Figure 2 to 4 (daily initialized 7-action discrete control of a virtual Jaco arm): 10\n#     sessions in B1 and 11 in B3, each with OL, then CL1 (decoder from OL), then CL2 (decoder from\n#     OL and CL1). Actions: right thumb (X+), left thumb (X-), head (Y+), left leg (Y-), tongue (Z+),\n#     lips (Z-), both middle fingers (origin). Decoder at 5 Hz on 200 ms bins of delta, beta and\n#     high-gamma power; B1 features pooled 2x2 over the grid to 96 dimensions, B3 759 dimensions,\n#     each bin L2-normalized. A 9-action variant (adding wrist rotations) on two days in B1 (Figure\n#     S6). A ReFit Kalman filter comparison over five days in B1 (Figure S7).\n#   - Figure 5 (plug-and-play, fixed MLP): two experiments in B1 (28 and 38 days long) and one in B3\n#     (39 days); online trials only.\n#   - Figures 6 and 7 (B1 only): IBID continuous control of a virtual arm (center-out, diagonal,\n#     path tracing), a mode-switch reach-to-grasp virtual task, and real-world Kinova Jaco tasks\n#     (reach and rotate, wall task) with a fixed biLSTM decoder over up to 210 PnP days, then a\n#     recalibration.\n#   - The biLSTM was trained on all collected open-loop and closed-loop data from the hDoF\n#     experiments, about 14 h 48 min before augmentation and segmentation, as segments of\n#     low-frequency (below 25 Hz) and high-gamma activity on all 128 channels of B1.\n#\n# The dandiset's own description (title and description on the archive only; its files were not\n# opened): long-term ECoG training trials from the 128-channel grid of one tetraplegic participant\n# trying to access 7 directional targets (6 axial directions and the origin), collated from\n# several BCI contexts (virtual environment, physical robot, open and closed loop), with high-gamma\n# amplitude (70 to 150 Hz) and low-frequency motor potentials (below 25 Hz) down-sampled to 100 Hz.\n# That is the B1 RNN training set. The Figure 1 task, B3, the 200 ms band-power features (delta,\n# beta, high gamma) that the MLP and autoencoder analyses use, the online decoder outputs and the\n# robot task outcomes may not be in it; which claims it can test is the author's to establish.\n#\n# Statements of tolerance. Where the paper gives an interval for a value, the tolerance is the\n# larger of the two distances from the value to the bounds of that interval; where it gives a\n# spread (plus or minus), the tolerance is that spread; otherwise 10% of the value.\n#\n# A paper inconsistency to note: Results, Plug-and-play control, paragraph 3 reports the same\n# robust regression slope, z and p (b = 0.258, z = 6.474, p = 1.847e-10) for B1 (Figure 4F) and\n# B3 (Figure 4G); one of them is likely a copy. Both are recorded, and the criteria for B3 rest on\n# the sign and significance of the slope, not on its value.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001535\"\npaper: doi:10.1016/j.cell.2025.02.001\nclaims:\n- id: fig1g-somatotopy-b1\n  statement: In B1, high-gamma spatial maps of right-hand actions are more similar to each other\n    (Jaccard coefficient) than to maps of left-hand actions and than to maps of all other actions.\n  source: Results, Mesoscale representation of body parts, paragraph 2; Figure 1G\n  quote: 'maps of right-hand movements were somatotopically more similar to each other 20 , 27 , 28 than to left-handed or other whole-body movements (B1, Fig. 1G , Mann Whitney U tests between Jaccard similarity coefficients: within maps of Rt. Hand movements vs. between maps of Rt. and Lt. Hand movements, z = 3.724 , p = 1.964 × 10 – 4 , within maps of Rt. Hand movements vs. between maps of Rt. Hand and All other movements z = 4.435 , p = 9.2 × 10 – 6'\n  statistics:\n  - about: within right hand against right hand to left hand\n    test: Mann Whitney U\n    statistic: z = 3.724\n    p: 1.964e-4\n  - about: within right hand against right hand to all other actions\n    test: Mann Whitney U\n    statistic: z = 4.435\n    p: 9.2e-6\n  criterion: Methods (Analyses to identify significant neural responses; Representational\n    structure analyses). Per action, high-gamma (70 to 150 Hz, Hilbert envelope averaged over the\n    eight sub-bands, 4th order Butterworth filters) is z-scored per session to the first 2 min\n    baseline, epoched from 1000 ms before the get-ready cue to the end of the go period, and\n    z-scored per trial to the 1000 ms before the get-ready cue; time points whose z-scored value\n    across trials exceeds 3 are removed. At every channel and time point a one-sample t-test\n    (threshold 0.05) is cluster corrected with 750 bootstrap samples of mean-centered trials,\n    cluster mass the sum of squared t within clusters contiguous in time and channel neighbours,\n    tested at 0.05. A channel belongs to an action's map when it is part of any significant\n    cluster. Maps are binary vectors; the Jaccard coefficient is taken for every pair of right-hand\n    maps (within), every right-hand and left-hand pair, and every right-hand and other-action pair;\n    Mann Whitney U tests compare the within set with each between set. Open details, named as\n    readings. (1) Channel neighbourhood for clustering, which the paper does not define; readings\n    (a) 4-connected grid neighbours, (b) 8-connected grid neighbours. (2) Which actions count as\n    right hand, left hand and other; the paper names them only in Figure 1E-F, so the reading is\n    the action names' effector, as the dataset labels them. Reproduced when, under one reading of\n    (1), both tests give p < 0.05 with the within-right-hand similarity higher.\n- id: fig1h-somatotopy-b3\n  statement: In B3, high-gamma maps of right-hand actions are also more similar to each other than\n    to left-hand maps and than to all other actions' maps.\n  source: Results, Mesoscale representation of body parts, paragraph 2; Figure 1H\n  quote: 'B3, Fig. 1H : within maps of Rt. Hand movements vs. between maps of Rt. and Lt. Hand movements, z = 2.11 , p = 0.0345 , within maps of Rt. Hand movements vs. between maps of Rt. Hand and All other movements z = 3.7119 , p = 2.057 × 10 – 4'\n  statistics:\n  - about: within right hand against right hand to left hand\n    test: Mann Whitney U\n    statistic: z = 2.11\n    p: 0.0345\n  - about: within right hand against right hand to all other actions\n    test: Mann Whitney U\n    statistic: z = 3.7119\n    p: 2.057e-4\n  criterion: As fig1g-somatotopy-b1, on B3's 32 actions and 253 channels. Reproduced when, under\n    one reading of the channel neighbourhood, both tests give p < 0.05 with the within-right-hand\n    similarity higher.\n- id: fig1ij-within-effector-levels\n  statement: Actions of one effector differ in activation level at a shared channel, with a\n    hand-knob electrode showing different high-gamma responses to three hand actions and a ventral\n    precentral channel showing different responses to orofacial actions.\n  source: Results, Mesoscale representation of body parts, paragraph 2; Figure 1I-J\n  quote: 'an electrode in the ‘hand-knob’ area had significantly different γ H between three hand actions ( Fig. 1I , Fig. S1C ). Similarly, a ventral channel along the precentral gyrus 29 showed differential γ H response levels to orofacial movements ( Fig. 1J )'\n  criterion: Methods (Analyses to identify significant neural responses, paragraph on Fig. 1I-J).\n    At each time point a repeated measures ANOVA over trials compares the within-effector actions'\n    high-gamma ERPs at one channel; clusters of contiguous significant time points are summed in F\n    and compared with 750 bootstrap samples of mean-centered data (maximum cluster mass), at 0.05.\n    Open details. The two channels and the three hand and the orofacial actions are shown only in\n    the figure; readings (a) the channel the paper identifies as hand knob (Figure S1C) and the\n    channel in ventral precentral gyrus, if the dataset labels channels, (b) every channel\n    significant for the effector in fig1g, reported as the fraction with a significant cluster.\n    How an rmANOVA is formed over trials of different actions is not stated (trials are not paired\n    across actions); readings (a) one-way ANOVA across actions with trials as observations, (b)\n    trials paired by repetition index within block. Reproduced when under every reading at least\n    one cluster for the hand actions and one for the orofacial actions is significant at the\n    channels of reading (a), or a majority of channels under reading (b).\n- id: figs2-pairwise-distances-significant\n  statement: Almost all pairwise Mahalanobis distances between actions are greater than chance\n    (99.7% of pairs in B1, 100% in B3, FDR corrected).\n  source: Results, Mesoscale representation of body parts, paragraph 3; Figure S2E-F\n  quote: 'almost all the pairwise neural distances between movements were significantly greater than chance ( Fig. S2 , B1: 99.7% of all pairwise comparisons; B3: 100% of all comparisons, α = 0.05 level, FDR corrected)'\n  expected:\n  - quantity: fraction of significant pairwise distances, B1\n    value: 99.7\n    tolerance: 0.3\n    unit: percent\n  - quantity: fraction of significant pairwise distances, B3\n    value: 100\n    tolerance: 0.3\n    unit: percent\n  criterion: Methods (Representational structure analyses). Data are 200 ms non-overlapping bins\n    of delta, beta and high-gamma power from 600 to 3400 ms after the go cue on all channels\n    (384 features in B1, 759 in B3), temporally smoothed, z-scored per feature across all trials of\n    a session, and concatenated across sessions per action. The distance is (mu_a - mu_b)' ((C_a +\n    C_b)/2)^-1 (mu_a - mu_b). The null for each pair (Figure S2) fits one Gaussian to the pooled\n    samples of both actions, draws as many samples, splits them in two with k-means and takes the\n    distance between the clusters; the pair is significant when its distance exceeds the 95th\n    percentile, after FDR (Benjamini-Hochberg) over all pairs at 0.05. Open details. The number of\n    null iterations and the temporal smoothing kernel are not given; a standard choice (1000\n    iterations, no extra smoothing beyond binning) is used and reported. The tolerance of 0.3\n    points is one pair in B1's 435 pairs (0.23 points) rounded up, since 10% of a value near 100%\n    would admit 90%. Reproduced when both fractions are within tolerance; partially reproduced\n    when both are at least 90%.\n- id: fig1kl-b1-b3-correlation\n  statement: For the 30 actions common to both participants, the pairwise distances of B1 and B3\n    are correlated (r = 0.626), indicating a common representational structure.\n  source: Results, Mesoscale representation of body parts, paragraph 3; Figure 1K-L\n  quote: 'For the 30 common actions, the pairwise distances were significantly correlated between B1 and B3 ( r = 0.626 , p = 9.724 × 10 – 49 , on the off diagonals of matrices in Fig. 1K and 1L )'\n  statistics:\n  - test: correlation of upper-diagonal entries\n    statistic: r = 0.626\n    p: 9.724e-49\n    n: 435 pairs of 30 common actions\n  expected:\n    quantity: correlation of B1 and B3 pairwise distances\n    value: 0.626\n    tolerance: 0.0626\n  depends_on:\n  - figs2-pairwise-distances-significant\n  criterion: Methods (Representational structure analyses, last paragraph). Distances as in\n    figs2-pairwise-distances-significant; upper-diagonal entries for the 30 common actions are\n    correlated. The correlation type is not named; the Methods say \"correlated\" and the Results\n    give r, so the readings are (a) Pearson, (b) Spearman. Reproduced when under one reading r is\n    within tolerance and p < 0.05.\n- id: fig1mn-hierarchical-clustering\n  statement: Hierarchical clustering of the distance matrix groups actions by effector in both\n    participants.\n  source: Results, Mesoscale representation of body parts, paragraph 3; Figure 1M-N\n  quote: Relative comparisons within and across effectors are shown in Fig 1M – N for both\n    participants via hierarchical clustering of the pairwise distance matrix\n  depends_on:\n  - figs2-pairwise-distances-significant\n  criterion: Methods (Representational structure analyses). Complete-linkage hierarchical\n    clustering of each participant's distance matrix. The paper gives no measure of how well\n    clusters follow effectors. The test here, named as a standard choice and not the paper's, is\n    the fraction of actions whose nearest neighbour in the dendrogram (first merge) is an action of\n    the same effector, compared with 1000 permutations of effector labels. Reproduced when that\n    fraction exceeds the 95th percentile of the permutation null in both participants.\n- id: fig2-session-trial-counts\n  statement: Across the daily sessions (10 in B1, 11 in B3) the average number of trials per\n    session was 89 for OL, 62 for CL1 and 48 for CL2.\n  source: Results, Design of the BCI experiments and decoders, paragraph 2\n  quote: 'In B1 and B3, we respectively performed 10 and 11 sessions. For each session, the average number of OL trials was: 89 [95% C.I. 83 – 94], CL1 trials: 62 [95% C.I. 50 – 75] and CL2: 48 [95% C.I. 38 – 59]'\n  statistics:\n  - about: OL trials per session\n    ci:\n      level: 0.95\n      low: 83\n      high: 94\n  - about: CL1 trials per session\n    ci:\n      level: 0.95\n      low: 50\n      high: 75\n  - about: CL2 trials per session\n    ci:\n      level: 0.95\n      low: 38\n      high: 59\n  expected:\n  - quantity: mean OL trials per session\n    value: 89\n    tolerance: 6\n  - quantity: mean CL1 trials per session\n    value: 62\n    tolerance: 13\n  - quantity: mean CL2 trials per session\n    value: 48\n    tolerance: 11\n  criterion: The counts are over the 21 daily-initialization sessions pooled across B1 and B3, as\n    the sentence reads; a reading per participant is also shown. Reproduced when the three pooled\n    means are within tolerance.\n- id: fig2e-above-chance\n  statement: Decoding accuracy was above chance in every OL, CL1 and CL2 session in both\n    participants.\n  source: Results, Discriminability of representations with closed-loop control, paragraph 1;\n    Figure 2E; Figure S4A-B\n  quote: decoding accuracies across trials ( Fig. 2E ) were significantly above chance (binomial\n    distribution, FDR corrected, α = 0.05 level, Fig. S4A – B ) for every single session in B1 and B3\n  statistics:\n  - test: binomial\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n    n: 63 decoders (21 sessions, three contexts)\n  criterion: Methods (Action decoding in the perspective of a virtual 3D Jaco arm). OL accuracy is\n    cross-validated, 10 random splits of the day's OL trials into 68% training, 12% validation and\n    20% test, with an MLP of one hidden layer of 120 units (leaky ReLU, dropout 0.4, L2 0.0001,\n    Adam, batch 32, early stopping after six epochs without improvement in validation loss); each\n    test trial is classified by the most frequent decode over the bins of its active period\n    (max vote), and accuracies are averaged over splits. CL1 and CL2 accuracy is the max vote of the\n    online decodes per trial. The p-value is the binomial probability of K or fewer successes being\n    reached by chance, the area from 0 to N/m successes with m = 7, and FDR is applied over all\n    decoders. Open details. The binomial p as written (\"area from 0 to N/m successes\") is the\n    probability of chance-level or lower performance; the reading used is the usual upper tail\n    P(X >= K) under p = 1/7, with the paper's wording shown as a variant. Reproduced when every\n    session's three decoders pass FDR at 0.05.\n- id: fig2e-cl2-vs-ol-accuracy\n  statement: Decoding accuracy is higher in CL2 than in OL, by 11.04 percentage points on average.\n  source: Results, Discriminability of representations with closed-loop control, paragraph 1;\n    Figure 2E\n  quote: 'decoding accuracies were higher during CL1 and CL2 as compared to OL ( Fig. 2E , non-parametric linear mixed effect models, LMM, CL2 vs. OL: difference of 11.04%, t ( 40 ) = 4.59 , p = 0.001 , and Wilcoxon signed rank test, WSRT, z = 3.945 , p = 7.98 × 10 – 5'\n  statistics:\n  - test: nonparametric linear mixed effect model, permutation\n    statistic: t(40) = 4.59\n    p: 0.001\n    n: 21 sessions, B1 and B3\n  - test: Wilcoxon signed rank\n    statistic: z = 3.945\n    p: 7.98e-5\n  expected:\n    quantity: CL2 minus OL mean accuracy\n    value: 11.04\n    tolerance: 1.104\n    unit: percentage points\n  depends_on:\n  - fig2e-above-chance\n  criterion: Methods (Action decoding, paragraph on tests). Session accuracies as in\n    fig2e-above-chance. A linear mixed model of accuracy on experiment type (OL or CL2, fixed\n    effect) with a random intercept per participant, over the 42 session values (t with 40\n    degrees of freedom); its p is the fraction of 2000 permutations, labels shuffled within each\n    participant, whose |t| is at least the observed |t|. A Wilcoxon signed rank test over the 21\n    paired sessions. Reproduced when the difference is within tolerance and both tests give\n    p < 0.05; partially reproduced when the tests hold and the difference is positive but outside\n    tolerance.\n- id: fig2e-cl1-vs-ol-accuracy\n  statement: Decoding accuracy is higher in CL1 than in OL, by 6.325 percentage points on average.\n  source: Results, Discriminability of representations with closed-loop control, paragraph 1;\n    Figure 2E\n  quote: 'CL1 vs. OL: difference of 6.325%, LMM, t ( 40 ) = 2.4026 , p = 0.022 , and WSRT, z = 2.93 , p = 0.0033'\n  statistics:\n  - test: nonparametric linear mixed effect model, permutation\n    statistic: t(40) = 2.4026\n    p: 0.022\n  - test: Wilcoxon signed rank\n    statistic: z = 2.93\n    p: 0.0033\n  expected:\n    quantity: CL1 minus OL mean accuracy\n    value: 6.325\n    tolerance: 0.6325\n    unit: percentage points\n  depends_on:\n  - fig2e-above-chance\n  criterion: As fig2e-cl2-vs-ol-accuracy, for CL1 against OL.\n- id: fig2e-cl2-vs-cl1-accuracy\n  statement: CL2 accuracy is higher than CL1 accuracy, by 4.713 percentage points on average.\n  source: Results, Discriminability of representations with closed-loop control, paragraph 1;\n    Figure 2E\n  quote: CL2 had significantly greater mean decoding accuracies when compared to CL1 (difference of\n    4.713%, LMM, t ( 40 ) = 2.06 , p = 0.044 , and WSRT, z = 2.209 , p = 0.027 )\n  statistics:\n  - test: nonparametric linear mixed effect model, permutation\n    statistic: t(40) = 2.06\n    p: 0.044\n  - test: Wilcoxon signed rank\n    statistic: z = 2.209\n    p: 0.027\n  expected:\n    quantity: CL2 minus CL1 mean accuracy\n    value: 4.713\n    tolerance: 0.4713\n    unit: percentage points\n  depends_on:\n  - fig2e-above-chance\n  criterion: As fig2e-cl2-vs-ol-accuracy, for CL2 against CL1.\n- id: figs4ef-ol-accuracy-stable\n  statement: OL decoding accuracy shows no linear trend across days in either participant.\n  source: Results, Discriminability of representations with closed-loop control, paragraph 1;\n    Figure S4E-F\n  quote: 'Notably, OL accuracies remained stable and consistently lower across-sessions even with training ( Fig. S4E – F , linear fit of chronological OL decoding accuracy over days, B1: p = 0.354 ; B3:'\n  statistics:\n  - about: B1\n    test: linear regression slope\n    statistic: b = 0.0109 ± 0.011, t(8) = 0.983\n    p: 0.354\n  - about: B3\n    test: linear regression slope\n    statistic: b = 0.008 ± 0.006, t(9) = 1.3683\n    p: 0.204\n  depends_on:\n  - fig2e-above-chance\n  criterion: A claim of absence, judged on the paper's test (Methods, Action decoding, last\n    sentence). Ordinary least squares of each session's cross-validated OL accuracy on session\n    order, per participant; reproduced when the slope's p >= 0.05 in both participants, not\n    reproduced when it is below 0.05 in either. The slopes are reported either way.\n- id: figs4g-percent-change-accuracy\n  statement: Expressed as percentage change per session, CL1 improves accuracy over OL by 9.4%,\n    CL2 over OL by 16.3%, and CL2 over CL1 by 6.6%.\n  source: Figure S4G legend\n  quote: 'CL1 and CL2 had positively improved decoding performance relative to OL (CL1 increase relative to OL by 9.427 ± 3.89 % , t ( 20 ) = 2.423 , p = 0.029 ; CL2 increase relative to OL by 16.275 ± 5.47 % , t ( 20 ) = 2.975 , p = 0.011 ). CL2 in turn had greater improvements in decoding accuracy as compared as CL1 ( by 6.62 ± 2.637 % , t ( 20 ) = 2.519 , p = 0.014 )'\n  statistics:\n  - about: CL1 relative to OL\n    test: nonparametric mixed effect model, bootstrap\n    statistic: t(20) = 2.423\n    p: 0.029\n  - about: CL2 relative to OL\n    test: nonparametric mixed effect model, bootstrap\n    statistic: t(20) = 2.975\n    p: 0.011\n  - about: CL2 relative to CL1\n    test: nonparametric mixed effect model, bootstrap\n    statistic: t(20) = 2.519\n    p: 0.014\n  expected:\n  - quantity: mean percent change CL1 over OL\n    value: 9.427\n    tolerance: 3.89\n    unit: percent\n  - quantity: mean percent change CL2 over OL\n    value: 16.275\n    tolerance: 5.47\n    unit: percent\n  - quantity: mean percent change CL2 over CL1\n    value: 6.62\n    tolerance: 2.637\n    unit: percent\n  depends_on:\n  - fig2e-above-chance\n  criterion: Methods (Action decoding, paragraph on controls). Per session, 100 (CL - OL) / OL and\n    100 (CL2 - CL1) / CL1. A mixed model of the 21 values with an intercept and a random intercept\n    per participant; its p is the fraction of 1000 bootstrap samples of each participant's\n    mean-centered data whose |t| is at least the observed. The tolerance is the reported spread\n    (the paper does not say whether it is SD or SE). Reproduced when all three means are within\n    tolerance and all three p < 0.05.\n- id: figs4hi-feature-importance\n  statement: All three bands contribute to decoding, with delta and high gamma the most\n    informative.\n  source: Results, Discriminability of representations with closed-loop control, paragraph 1;\n    Figure S4H-I\n  quote: Offline analyses revealed that while all three neural features ( δ , β , γ H ) were\n    important for decoding, δ and γ H were most informative\n  criterion: Methods (Importance of neural features). Trials from all daily sessions per\n    participant, 15 random splits (the Methods print \"70% of trials for testing, 15% validation and\n    15% testing\"; the reading is 70% training), decoders on all three bands, each pair of bands\n    and each band alone; held-out trial accuracy per split. The paper gives no test. Read as\n    (i) all three bands together reach at least the median accuracy of every single band, and\n    (ii) delta alone and high gamma alone each have a higher median accuracy than beta alone, in\n    both participants. Reproduced when both hold in both participants.\n- id: fig2i-distance-cl-vs-ol\n  statement: Average pairwise Mahalanobis distance between actions in latent space is greater in\n    CL1 and in CL2 than in OL, in both participants.\n  source: Results, Changes in representational statistics with closed-loop control, paragraph 1;\n    Figure 2I\n  quote: 'CL demonstrated greater average Mahalanobis distances (all pairwise comparisons) than OL ( Fig 2I , LMM, combining B1 and B3, CL1 vs. OL: t ( 40 ) = 10.74 , p = 1 × 10 - 3 , CL2 vs. OL: t ( 40 ) = 11.73 , p = 1 × 10 - 3 ). This main effect was also present within B 1 and B3 individually'\n  statistics:\n  - about: CL1 against OL, both participants\n    test: nonparametric linear mixed effect model, permutation\n    statistic: t(40) = 10.74\n    p: 0.001\n  - about: CL2 against OL, both participants\n    test: nonparametric linear mixed effect model, permutation\n    statistic: t(40) = 11.73\n    p: 0.001\n  - about: B1, CL2 against OL\n    test: Wilcoxon signed rank\n    statistic: z = 2.8\n    p: 0.0051\n  - about: B1, CL1 against OL\n    test: Wilcoxon signed rank\n    statistic: z = 2.8\n    p: 0.0051\n  - about: B3, CL2 against OL\n    test: Wilcoxon signed rank\n    statistic: z = 2.934\n    p: 0.0033\n  - about: B3, CL1 against OL\n    test: Wilcoxon signed rank\n    statistic: z = 2.934\n    p: 0.0033\n  criterion: Methods (Autoencoder design; Analyses of representational statistics in latent\n    space). Per session, one autoencoder on that day's active-period bins of OL, CL1 and CL2, all\n    actions, labelled by the cued action; layers input, 48, 16, 2 (bottleneck), 16, 48, output,\n    ELU, dropout 0.3, plus a softmax classifier on the bottleneck, loss the sum of reconstruction\n    error and cross-entropy, Adam with learning rate 0.001, batch 32, split 80/10/10, early\n    stopping after six epochs, Gaussian augmentation per band (Data augmentation). All bins of each\n    context are projected to the bottleneck; for each pair of the 7 actions the Mahalanobis\n    distance with the pooled covariance (C_a + C_b)/2; the session value is the mean over the 21\n    pairs. Tests as in fig2e-cl2-vs-ol-accuracy with 1000 permutations, and Wilcoxon signed rank\n    per participant. Open details. (1) The reconstruction loss is not named; readings (a) mean\n    squared error, (b) mean absolute error. (2) The amount of augmentation (M) is not given;\n    readings (a) none, (b) training data doubled. Random seeds are a standard choice. Reproduced\n    when under one reading of each the LMM gives p < 0.05 for both contrasts and the signed rank\n    test gives p < 0.05 for both contrasts in each participant, with CL greater.\n- id: fig2i-distance-cl2-vs-cl1\n  statement: Latent-space distances between actions are greater in CL2 than in CL1, in both\n    participants.\n  source: Results, Changes in representational statistics with closed-loop control, paragraph 1;\n    Figure 2I\n  quote: 'Between the two closed-loop experiments, CL2 was characterized by greater mean distance separation between movements as compared to CL1 (LMM, Fig. 2I , t ( 40 ) = 3.7186 , p = 0.001 ). This effect was present in both B 1 and B 3 individually as well (WSRT, B1: z = 2.701 , p ='\n  statistics:\n  - about: both participants\n    test: nonparametric linear mixed effect model, permutation\n    statistic: t(40) = 3.7186\n    p: 0.001\n  - about: B1\n    test: Wilcoxon signed rank\n    statistic: z = 2.701\n    p: 0.0069\n  - about: B3\n    test: Wilcoxon signed rank\n    statistic: z = 2.7562\n    p: 0.0058\n  depends_on:\n  - fig2i-distance-cl-vs-ol\n  criterion: As fig2i-distance-cl-vs-ol, for CL2 against CL1.\n- id: fig2j-variance-cl-vs-ol\n  statement: Mean neural variance of actions in latent space is lower in CL1 and CL2 than in OL,\n    in both participants.\n  source: Results, Changes in representational statistics with closed-loop control, paragraph 1;\n    Figure 2J\n  quote: 'the mean neural variance (over movements) during both CL experiments were lower in comparison to OL ( Fig. 2J , LMM, CL2 vs. OL: t ( 40 ) = 9.427 , p = 0.001 , CL1 vs. OL: t ( 40 ) = 8.365 , p = 0.001 ), an effect that was present within B1 and B3 individually as well'\n  statistics:\n  - about: CL2 against OL, both participants\n    test: nonparametric linear mixed effect model, permutation\n    statistic: t(40) = 9.427\n    p: 0.001\n  - about: CL1 against OL, both participants\n    test: nonparametric linear mixed effect model, permutation\n    statistic: t(40) = 8.365\n    p: 0.001\n  - about: B1, CL2 and CL1 against OL\n    test: Wilcoxon signed rank\n    statistic: z = 2.803\n    p: 0.0051\n  - about: B3, CL2 and CL1 against OL\n    test: Wilcoxon signed rank\n    statistic: z = 2.934\n    p: 0.0033\n  depends_on:\n  - fig2i-distance-cl-vs-ol\n  criterion: Methods (Analyses of representational statistics in latent space, variance\n    paragraph). On the session autoencoders of fig2i-distance-cl-vs-ol, each action's variance is\n    the product of the eigenvalues of its 2x2 latent covariance (its determinant), averaged over the\n    7 actions per session and context; tests as in fig2i-distance-cl-vs-ol. Open detail. Figure 2J\n    says variances were scaled per subject, without saying how; this matters for the pooled LMM,\n    not the per-participant signed rank tests. Readings (a) no scaling, (b) divided by the\n    participant's maximum, (c) z-scored within participant. Reproduced when under one reading the\n    LMM gives p < 0.05 for both contrasts and the signed rank tests give p < 0.05 in each\n    participant, with CL lower.\n- id: fig2j-variance-cl2-vs-cl1\n  statement: CL2 has lower latent-space variance than CL1, in both participants.\n  source: Results, Changes in representational statistics with closed-loop control, paragraph 1;\n    Figure 2J\n  quote: 'Comparison of the two CL experiments revealed that CL2 had lower neural variances across-sessions on average than CL1 in B1 and B3 (LMM, t ( 40 ) = 2.517 , p = 0.015 , WSRT, B1: z = 2.803 p = 0.0051 ; B3: z = 2.8451 , p = 0.0044 )'\n  statistics:\n  - about: both participants\n    test: nonparametric linear mixed effect model, permutation\n    statistic: t(40) = 2.517\n    p: 0.015\n  - about: B1\n    test: Wilcoxon signed rank\n    statistic: z = 2.803\n    p: 0.0051\n  - about: B3\n    test: Wilcoxon signed rank\n    statistic: z = 2.8451\n    p: 0.0044\n  depends_on:\n  - fig2j-variance-cl-vs-ol\n  criterion: As fig2j-variance-cl-vs-ol, for CL2 against CL1, with the same readings of scaling.\n- id: figs5-channel-variance-reduction\n  statement: At the channel level, the standard deviation of each band's activity falls from OL to\n    CL1, from OL to CL2 and from CL1 to CL2 (high gamma by 32.6%, 38.4% and 10.5%; beta by 29.0%,\n    33.9% and 7.6%; delta by 31.0%, 36.1% and 7.2%).\n  source: Figure S5E-G legend; Results, Changes in representational statistics with closed-loop\n    control, paragraph 1\n  quote: 'we found that there were significantly greater reductions in variance when going from OL to CL1 across sessions (in terms of S.D., by - 32.59 % , t ( 20 ) = – 6.44 , p = 0.0001 ) , OL to CL2 (by – 38.39 % , t ( 20 ) = – 8.496 , p = 0.0001 ) and when going from CL1 to CL2 (by – 10.49 % , t ( 20 ) = – 3.969 , p = 0.002 )'\n  statistics:\n  - about: high gamma, OL to CL1\n    test: nonparametric mixed effect model, bootstrap\n    statistic: t(20) = -6.44\n    p: 0.0001\n  - about: high gamma, OL to CL2\n    test: nonparametric mixed effect model, bootstrap\n    statistic: t(20) = -8.496\n    p: 0.0001\n  - about: high gamma, CL1 to CL2\n    test: nonparametric mixed effect model, bootstrap\n    statistic: t(20) = -3.969\n    p: 0.002\n  - about: beta, OL to CL1\n    test: nonparametric mixed effect model, bootstrap\n    statistic: t(20) = -4.9626\n    p: 0.0001\n  - about: beta, OL to CL2\n    test: nonparametric mixed effect model, bootstrap\n    statistic: t(20) = -6.2811\n    p: 0.0001\n  - about: beta, CL1 to CL2\n    test: nonparametric mixed effect model, bootstrap\n    statistic: t(20) = -3.4612\n    p: 0.003\n  - about: delta, OL to CL1\n    test: nonparametric mixed effect model, bootstrap\n    statistic: t(20) = -5.428\n    p: 0.0001\n  - about: delta, OL to CL2\n    test: nonparametric mixed effect model, bootstrap\n    statistic: t(20) = -7.3651\n    p: 0.0001\n  - about: delta, CL1 to CL2\n    test: nonparametric mixed effect model, bootstrap\n    statistic: t(20) = -3.262\n    p: 0.005\n  expected:\n  - quantity: high gamma SD change OL to CL1\n    value: -32.59\n    tolerance: 3.259\n    unit: percent\n  - quantity: high gamma SD change OL to CL2\n    value: -38.39\n    tolerance: 3.839\n    unit: percent\n  - quantity: high gamma SD change CL1 to CL2\n    value: -10.49\n    tolerance: 1.049\n    unit: percent\n  - quantity: beta SD change OL to CL1\n    value: -29.003\n    tolerance: 2.9003\n    unit: percent\n  - quantity: beta SD change OL to CL2\n    value: -33.922\n    tolerance: 3.3922\n    unit: percent\n  - quantity: beta SD change CL1 to CL2\n    value: -7.605\n    tolerance: 0.7605\n    unit: percent\n  - quantity: delta SD change OL to CL1\n    value: -30.953\n    tolerance: 3.0953\n    unit: percent\n  - quantity: delta SD change OL to CL2\n    value: -36.091\n    tolerance: 3.6091\n    unit: percent\n  - quantity: delta SD change CL1 to CL2\n    value: -7.156\n    tolerance: 0.7156\n    unit: percent\n  depends_on:\n  - fig2i-distance-cl-vs-ol\n  criterion: Methods (Analyses of neural variance in high-dimensional channel-feature space).\n    Latent samples of each session's autoencoder are passed through its decoder layers to\n    reconstruct the features; for each channel, band and action, the SD over samples in each\n    context; the percent change of SD for each transition; the session value is the median over\n    channels and actions; a mixed model on the 21 session values (intercept, random intercept per\n    participant) with p from 1000 bootstrap samples of centered data. The values are on\n    reconstructed, L2-normalized features (Figure S5D). Reproduced when the nine session-mean\n    changes are negative with p < 0.05, and at least seven of the nine are within tolerance;\n    partially reproduced when all nine are negative and significant but fewer are within\n    tolerance.\n- id: figs5bc-somatotopy-preserved\n  statement: Each action's average spatial map is preserved (highly correlated) between OL, CL1 and\n    CL2 within a session.\n  source: Methods, Analyses of neural variance in high-dimensional channel-feature space; Figure\n    S5A-C\n  quote: Our result showed preserved somatotopy for each movement on average when transitioning\n    from open-loop to closed-loop control\n  depends_on:\n  - fig2i-distance-cl-vs-ol\n  criterion: Per session and action, the average reconstructed spatial map of each band is\n    flattened and correlated (Pearson, the paper's \"linear correlation\") between contexts. The\n    paper gives no threshold. Read as preserved when the median correlation over actions and\n    sessions exceeds 0.8 for each band and context pair in both participants; this threshold is a\n    standard choice, not the paper's, and the full distributions are reported.\n- id: figs6-nine-actions\n  statement: With nine actions (two wrist rotations added) on two days in B1, accuracy is higher in\n    CL1 (71.30%) and CL2 (80.86%) than in OL (65.60%), latent distances are larger and latent\n    variances smaller in CL than in OL and in CL2 than in CL1.\n  source: Figure S6D-F legend; Results, Changes in representational statistics with closed-loop\n    control, paragraph 1\n  quote: 'decoding accuracies tended to be higher in closed-loop control blocks (CL1, mean decoding accuracy of 71.30%, CL2 mean decoding accuracy of 80.86%) as compared to open-loop control blocks (OL, cross-validated mean decoding accuracy of 65.60%)'\n  statistics:\n  - about: distance, OL against CL1\n    test: Wilcoxon signed rank\n    p: 8.73e-11\n    n: 36 pairs on two days\n  - about: distance, OL against CL2\n    test: Wilcoxon signed rank\n    p: 2.91e-11\n  - about: distance, CL1 against CL2\n    test: Wilcoxon signed rank\n    p: 9.6e-10\n  - about: variance, OL against CL1\n    test: Wilcoxon signed rank\n    p: 0.0039\n    n: 9 actions on two days\n  - about: variance, OL against CL2\n    test: Wilcoxon signed rank\n    p: 0.0039\n  - about: variance, CL1 against CL2\n    test: Wilcoxon signed rank\n    p: 0.011\n  expected:\n  - quantity: OL cross-validated mean accuracy, 9 actions\n    value: 65.60\n    tolerance: 6.56\n    unit: percent\n  - quantity: CL1 mean accuracy, 9 actions\n    value: 71.30\n    tolerance: 7.13\n    unit: percent\n  - quantity: CL2 mean accuracy, 9 actions\n    value: 80.86\n    tolerance: 8.086\n    unit: percent\n  criterion: Methods (Replicating results with a larger action set). Accuracies as in\n    fig2e-above-chance with m = 9; the mean is over the two days. Distances are the 36 pairwise\n    latent distances per day, pooled over both days (the legend says 36 pairs across the two days;\n    the Methods say 36 pairs per day collated over both days, 72 values; readings (a) 72 values,\n    (b) 36 values averaged over days) compared with signed rank tests; variances are the 9 actions'\n    latent variances, pooled over the two days (18 values), compared with signed rank tests.\n    Reproduced when the three accuracies are within tolerance and, under one reading, all six\n    signed rank tests give p < 0.05 in the stated directions.\n- id: fig2kl-ol-distance-stable\n  statement: OL latent distances between actions show no trend across days in either participant.\n  source: Results, Changes in representational statistics with closed-loop control, paragraph 2;\n    Figure 2K-L\n  quote: 'while the average distances between movements in OL remained stable across-days (B1: β = 0.11 ± 0.137 , t ( 8 ) = 0.797 , p = 0.448 , Fig. 2 K ; B3: β = 0.65 ± 0.425 , t ( 9 ) = 1.536 , p = 0.158 , Fig. 2L )'\n  statistics:\n  - about: B1\n    test: linear regression slope\n    statistic: β = 0.11 ± 0.137, t(8) = 0.797\n    p: 0.448\n  - about: B3\n    test: linear regression slope\n    statistic: β = 0.65 ± 0.425, t(9) = 1.536\n    p: 0.158\n  depends_on:\n  - fig2i-distance-cl-vs-ol\n  criterion: A claim of absence, judged on the paper's test (Methods, Analyses of representational\n    statistics, trend paragraph). OLS of each session's mean OL latent distance on session order,\n    per participant. Reproduced when p >= 0.05 in both participants; not reproduced when p < 0.05\n    in either. Slopes are reported either way.\n- id: fig2kl-cl-distance-increase\n  statement: CL latent distances between actions increase across days in both participants (slope\n    1.655 in B1, 2.371 in B3).\n  source: Results, Changes in representational statistics with closed-loop control, paragraph 2;\n    Figure 2K-L\n  quote: 'CL was characterized by a striking increase in separability (via a random intercept LMM over CL1 and CL2, B1: β = 1.655 ± 0.563 , t ( 18 ) = 2.937, p = 0.0087 , Fig. 2 K ; B3: β = 2.371 ± 0.495 , t ( 20 ) = 4.786 , p = 1 × 10 – 3 , Fig. 2L )'\n  statistics:\n  - about: B1\n    test: random intercept linear mixed model slope, permutation\n    statistic: β = 1.655 ± 0.563, t(18) = 2.937\n    p: 0.0087\n  - about: B3\n    test: random intercept linear mixed model slope, permutation\n    statistic: β = 2.371 ± 0.495, t(20) = 4.786\n    p: 0.001\n  expected:\n  - quantity: B1 slope of CL mean distance on day\n    value: 1.655\n    tolerance: 0.563\n  - quantity: B3 slope of CL mean distance on day\n    value: 2.371\n    tolerance: 0.495\n  depends_on:\n  - fig2i-distance-cl-vs-ol\n  criterion: Methods (trend paragraph). Per participant, a mixed model of session mean latent\n    distance on session order over CL1 and CL2 together, with CL1 and CL2 as random intercepts;\n    p is the fraction of 1000 permutations (day order shuffled within CL1 and within CL2) whose |t|\n    is at least the observed. The slope is in the latent space's own units, which depend on each\n    autoencoder; the values are read as approximate. Reproduced when both slopes are positive with\n    p < 0.05 and within tolerance; partially reproduced when both are positive and significant but\n    outside tolerance.\n- id: figs6gh-highdim-trends\n  statement: In the full feature space, too, CL distances increase across days while OL distances\n    stay stable, in both participants.\n  source: Figure S6G-H legend; Results, Changes in representational statistics with closed-loop\n    control, paragraph 2\n  quote: 'A linear mixed effect (LME) model combining CL1 and CL2 showed a significant increase in the separation between movements across-days (magenta line with slope indicated, t ( 18 ) = 2.1213 , p = 0.048 )'\n  statistics:\n  - about: B1, CL1 and CL2 slope\n    test: linear mixed effect model\n    statistic: t(18) = 2.1213\n    p: 0.048\n  - about: B1, OL slope\n    test: linear regression\n    statistic: t(8) = 0.846\n    p: 0.422\n  - about: B3, CL1 and CL2 slope\n    test: linear mixed effect model\n    statistic: t(20) = 4.243\n    p: 3.397e-4\n  - about: B3, OL slope\n    test: linear regression\n    statistic: t(9) = 1.45\n    p: 0.18\n  criterion: As fig2kl-ol-distance-stable and fig2kl-cl-distance-increase, on the mean pairwise\n    Mahalanobis distance of each session's features (delta, beta and high gamma on all pooled\n    channels, 96 in B1 and 759 in B3) instead of latent values. Reproduced when the CL slope is\n    positive with p < 0.05 and the OL slope has p >= 0.05, in both participants.\n- id: fig2mn-distance-predicts-accuracy\n  statement: Across sessions, the mean latent distance between actions predicts the session's\n    decoding accuracy (leave-one-out logistic regression, better than permuted data), in both\n    participants.\n  source: Results, Changes in representational statistics with closed-loop control, paragraph 2;\n    Figure 2M-N\n  quote: 'These across-days increases in average distances were significantly predictive of improved decoding accuracies in B1 and B3 ( Fig. 2M and 2N , leave-one-out cross validated logistic regression with permutation B1: CV log loss of 0.51, p = 0.002 , B3: CV log loss of 0.392, p = 0.002 )'\n  statistics:\n  - about: B1\n    test: leave-one-out logistic regression, permutation\n    statistic: CV log loss 0.51\n    p: 0.002\n  - about: B3\n    test: leave-one-out logistic regression, permutation\n    statistic: CV log loss 0.392\n    p: 0.002\n  expected:\n  - quantity: B1 cross-validated log loss\n    value: 0.51\n    tolerance: 0.051\n  - quantity: B3 cross-validated log loss\n    value: 0.392\n    tolerance: 0.0392\n  depends_on:\n  - fig2i-distance-cl-vs-ol\n  - fig2e-above-chance\n  criterion: Methods (paragraph on logistic regression). Per participant, the points are the\n    sessions' OL, CL1 and CL2 values (the Methods say accuracy \"from each individual session\", and\n    the figure plots each session's distance against its accuracy); logistic regression of\n    accuracy (a proportion) on mean latent distance; leave-one-out log loss averaged over points;\n    p is the fraction of 1000 permutations of the accuracies whose log loss is smaller. Open\n    details. (1) Whether points are 30 and 33 (all three contexts) or 10 and 11 (one per session);\n    readings (a) all contexts, (b) CL2 only, (c) mean of the contexts. (2) The fit with a\n    fractional outcome; reading a binomial GLM with the proportion as response, unweighted.\n    Reproduced when under one reading of (1) both p < 0.05 and both losses are within tolerance;\n    partially reproduced when both p < 0.05 only.\n- id: fig3c-manifold-stable\n  statement: Daily autoencoder manifolds are similar across days (CKA); in B1, 80% of day pairs\n    have all five layers significantly similar and the rest at least four; in B3, 83.64% have all\n    five, 12.72% four and 3.64% three.\n  source: Results, Stability of action representations, paragraph 1; Figure 3C\n  quote: In B1, 80% of all pairwise comparisons had all 5 layers significantly similar; the\n    remaining 20% had at least 4 of 5 similar layers. In B3, 83.64% of all pairwise comparisons had\n    all layers similar; 12.72% had at least 4 of 5 similar layers and the remaining 3.64% had at\n    least 3 of the 5 similar layers\n  statistics:\n  - test: CKA against weight-shuffled null\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n    n: 45 day pairs in B1 and 55 in B3, five layers each\n  expected:\n  - quantity: B1 fraction of day pairs with 5 of 5 layers similar\n    value: 80\n    tolerance: 8\n    unit: percent\n  - quantity: B3 fraction of day pairs with 5 of 5 layers similar\n    value: 83.64\n    tolerance: 8.364\n    unit: percent\n  depends_on:\n  - fig2i-distance-cl-vs-ol\n  criterion: Methods (Representational stability analyses). For each pair of days, linear CKA\n    between the two autoencoders' activations at each of the five hidden layers (48, 16, 2, 16,\n    48 units), activations mean-centered; the null is 1000 CKA values after randomly shuffling the\n    weights and biases of the two layers compared; p is the fraction of null values at least the\n    observed; FDR at 0.05 over all layers and pairs. Open details. (1) Which samples are fed to\n    both networks, which CKA needs to match; readings (a) the pooled samples of both days, (b) day\n    X's samples through both networks and day Y's through both, averaging the two CKAs. (2) What\n    \"shuffled\" permutes; readings (a) entries of the layer's weight matrix and bias vector are\n    permuted, (b) the layer's units (rows) are permuted. Reproduced when under one combination of\n    readings both \"all 5\" fractions are within tolerance and no B1 pair has fewer than 4 similar\n    layers; partially reproduced when at least 75% of pairs in each participant have at least 4\n    similar layers.\n- id: figs7b-refit-less-discernible\n  statement: In B1, daily initialized ReFit-KF velocity commands are less discernible between\n    targets in latent space than the discrete actions; feedforward commands are more discernible\n    than all commands within 45 degrees.\n  source: Figure S7B legend; Results, Stability of action representations, paragraph 2\n  quote: daily initialized discrete representations had greater median Mahalanobis distances\n    between targets across sessions as compared to daily initialized early feedforward velocity\n    commands (first ~ 2.5 s , Mann Whitney U test p = 1.2 × 10 - 5 ) or all intended velocity\n    commands to the target within a 45 degree tolerance\n  statistics:\n  - about: discrete against feedforward\n    test: Mann Whitney U\n    p: 1.2e-5\n  - about: discrete against within 45 degrees\n    test: Mann Whitney U\n    p: 1.2e-5\n  - about: feedforward against within 45 degrees\n    test: Mann Whitney U\n    p: 7.685e-4\n  criterion: Methods (Representational analyses of denovo BCI velocity commands). Five days of\n    ReFit-KF data in B1, six target classes, daily autoencoders on OL, CL1 and CL2 bins, either the\n    first 2.5 s of each trial or all bins whose decoded velocity is within 45 degrees of the target;\n    the session value is the mean pairwise latent distance; CL1 and CL2 values are pooled and\n    compared with the discrete sessions' CL values by Mann Whitney U. Reproduced when all three\n    tests give p < 0.05 in the stated directions.\n- id: figs7cd-refit-less-stable\n  statement: In B1, the daily manifolds of ReFit-KF velocity commands are much less stable across\n    days than those of discrete actions; most day pairs (65%) share no similar layer, feedforward\n    commands never do, and commands within 45 degrees share 1.5 layers on average.\n  source: Figure S7C-D legend; Results, Stability of action representations, paragraph 2\n  quote: Specifically, the majority of the pairwise comparisons (65%, averaged for both types of\n    commands) between individual days’ autoencoders had no significantly similar layers between them\n  statistics:\n  - about: discrete against feedforward, layer CKA\n    test: Mann Whitney U\n    p: 1.115e-26\n  - about: discrete against within 45 degrees, layer CKA\n    test: Mann Whitney U\n    p: 1.18e-6\n  - about: feedforward against within 45 degrees, layer CKA\n    test: Mann Whitney U\n    p: 3.612e-10\n  expected:\n  - quantity: fraction of ReFit-KF day pairs with no similar layer, mean of the two command types\n    value: 65\n    tolerance: 6.5\n    unit: percent\n  - quantity: mean similar layers per day pair, commands within 45 degrees\n    value: 1.5\n    tolerance: 0.15\n    unit: layers\n  depends_on:\n  - fig3c-manifold-stable\n  - figs7b-refit-less-discernible\n  criterion: As fig3c-manifold-stable, with its readings, on the ReFit-KF daily autoencoders; the\n    layer-wise CKA values of all day pairs are compared between command types by Mann Whitney U.\n    Reproduced when, under one reading, the 65% and 1.5 values are within tolerance, no\n    feedforward day pair has a similar layer, and the three tests give p < 0.05 with discrete\n    highest.\n- id: figs7i-ibid-straighter-than-refit\n  statement: Trajectories to cardinal targets deviate less from the straight line under IBID than\n    under the ReFit-KF.\n  source: Figure S7I legend; Results, PnP control of a virtual robotic arm, paragraph 2\n  quote: Results revealed greater median error in trajectories when using ReFit-KF after\n    closed-loop decoder adaptation as compared to IBID after closed-loop decoder adaptation (Mann\n    Whitney U test, z = 6.967 , p = 3.2442 × 10 - 12 )\n  statistics:\n  - test: Mann Whitney U\n    statistic: z = 6.967\n    p: 3.2442e-12\n    n: 48 IBID and 18 ReFit-KF trials on one day\n  criterion: Methods (Robot kinematics analyses). Per trial, the square root of the summed squared\n    differences between decoded and ideal straight-line positions over all time points, divided\n    by the number of points; Mann Whitney U between IBID and ReFit-KF CL2 trials. Reproduced when\n    p < 0.05 with the ReFit-KF median higher.\n- id: fig4b-day-differences\n  statement: For right thumb OL trials in B1, the mean high-gamma map is preserved across three\n    days (average pairwise r = 0.88), but channel-level high-gamma means over M1/S1 differ between\n    days.\n  source: Results, Plug-and-play control in presence of distributional drift, paragraph 1;\n    Figure 4A-B\n  quote: 'Even with a preserved neural map and somatotopy (average pairwise r = 0.88 ), there was little distributional overlap between days ( Fig. 4B , permutation t – tests show significant differences in γ H mean over trials, Day 1 vs. Day 4, t ( 11 ) = 17.87 , p = 1 × 10 – 4'\n  statistics:\n  - about: day 1 against day 4\n    test: permutation t-test\n    statistic: t(11) = 17.87\n    p: 1e-4\n  - about: day 1 against day 8\n    test: permutation t-test\n    statistic: t(11) = 28.6\n    p: 1e-4\n  - about: day 4 against day 8\n    test: permutation t-test\n    statistic: t(11) = 2.93\n    p: 0.0138\n  expected:\n    quantity: average pairwise correlation of right thumb high-gamma maps across the three days\n    value: 0.88\n    tolerance: 0.088\n  criterion: Open details, as the paper names neither which three days (called \"three random\n    days\"; the tests name days 1, 4 and 8), nor which channels form the M1/S1 rectangle, nor what\n    the 12 observations behind t(11) are. Readings (a) days 1, 4 and 8 of the daily sessions,\n    channels the dataset marks as M1/S1 hand area, a paired permutation t-test over 12 channels of\n    trial-mean high gamma; (b) the same days, a two-sample permutation t-test over trials of the\n    mean over those channels. Reproduced when under one reading the mean pairwise map correlation\n    is within tolerance and day 1 differs from days 4 and 8 with p < 0.05; partially reproduced\n    when only the differences hold. The day 4 against day 8 result is reported.\n- id: fig4cd-day-decodable\n  statement: The recording day can be decoded from held-out OL samples on a common multi-day\n    manifold (90.96% in B1, chance 10%; 98.4% in B3, chance 9.09%).\n  source: Results, Plug-and-play control in presence of distributional drift, paragraph 1;\n    Figure 4C-D\n  quote: 'In general, the recording day could be classified from held-out samples on the common manifold ( Fig. 4C – D B1: cross-validated decoding accuracy of 90.96% [90.68% - 91.24%], chance = 10%, B3: cross-validated decoding accuracy of 98.4% [98.24% - 98.54%], chance = 9.09%)'\n  statistics:\n  - about: B1 accuracy\n    ci:\n      low: 90.68\n      high: 91.24\n      unit: percent\n  - about: B3 accuracy\n    ci:\n      low: 98.24\n      high: 98.54\n      unit: percent\n  expected:\n  - quantity: B1 day decoding accuracy\n    value: 90.96\n    tolerance: 0.28\n    unit: percent\n  - quantity: B3 day decoding accuracy\n    value: 98.4\n    tolerance: 0.16\n    unit: percent\n  criterion: Methods (Across-day drifts in centroids). OL samples of all days (about 22k), 40\n    random splits of 68% training, 12% validation and 20% test; an autoencoder as in\n    fig2i-distance-cl-vs-ol trained with day labels as additional class memberships; accuracy of\n    the classification layer for the day of recording on test samples, averaged over splits.\n    Open details. (1) How day labels enter; readings (a) the classifier layer has one unit per day,\n    (b) one unit per day and action combination, scored on day. (2) Whether samples are split by\n    sample or by trial; the Methods say samples, so (a) by sample, with (b) by trial shown as a\n    variant. The interval tolerances are the paper's own and very narrow; the claim is reproduced\n    when under one reading of (1) both accuracies are within their tolerance, and partially\n    reproduced when both are within 10% of the reported values and far above chance.\n- id: fig4cd-demeaned-chance\n  statement: After mean-centering each day's data, the recording day can no longer be decoded\n    (B1 10.03%, B3 8.77%, not different from chance).\n  source: Results, Plug-and-play control in presence of distributional drift, paragraph 1;\n    Figure 4C-D\n  quote: 'In contrast, centering and demeaning each day’ data before building a common manifold eliminated discernibility ( Fig. 4C , B1 decoding accuracy: 10.03% [9.71% - 10.37%], chance = 10%, WSR: p = 0.282 , Fig. 4D : decoding accuracy of 8.77% [8.617% - 9.138%], chance = 9.09%, WSR: p = 0.3 )'\n  statistics:\n  - about: B1, against chance 10%\n    test: Wilcoxon signed rank\n    p: 0.282\n    ci:\n      low: 9.71\n      high: 10.37\n      unit: percent\n  - about: B3, against chance 9.09%\n    test: Wilcoxon signed rank\n    p: 0.3\n    ci:\n      low: 8.617\n      high: 9.138\n      unit: percent\n  depends_on:\n  - fig4cd-day-decodable\n  criterion: A claim of absence, judged on the paper's test. As fig4cd-day-decodable after\n    subtracting each day's mean from its samples; a Wilcoxon signed rank test of the 40 split\n    accuracies against chance (10% in B1, 9.09% in B3). Reproduced when p >= 0.05 in both\n    participants; not reproduced when p < 0.05 in either. The accuracies are reported.\n- id: figs8ab-day-decodable-trials\n  statement: A two-layer MLP on the full feature space also decodes the recording day from\n    held-out trials, significantly above chance in both participants.\n  source: Results, Plug-and-play control in presence of distributional drift, paragraph 1;\n    Figure S8A-B\n  quote: A MLP in high-dimensional channel-feature space revealed similar significant trial-level\n    decoding accuracies ( Fig. S8A – B )\n  criterion: Methods (Across-day drifts, paragraph on the MLP). Trials of all days split 70/15/15\n    by trial, 10 random splits; MLP with two layers of 64 units, leaky ReLU, dropout 0.4, trained\n    on samples; trial-level day accuracy (the trial's label taken by max vote over its samples,\n    as for the other trial-level decoders) averaged over splits; p from the binomial with the\n    number of held-out trials and chance 1/10 (B1) or 1/11 (B3). Reproduced when p < 0.05 in both\n    participants.\n- id: fig4fg-sampling-days-increases-distance\n  statement: Distances between actions on held-out days increase linearly with the number of\n    prior days used to build the common manifold, in both participants.\n  source: Results, Plug-and-play control in presence of distributional drift, paragraph 2;\n    Figure 4F-G\n  quote: 'we found that the pairwise distances between actions on a given day linearly increased as a function of the number of prior days used to build the common manifold (robust linear regression on median Mahalanobis distances, B1: slope b = 0.258 , z = 6.474 , p = 1.847 × 10 – 10 , Fig. 4F'\n  statistics:\n  - about: B1\n    test: robust linear regression\n    statistic: b = 0.258, z = 6.474\n    p: 1.847e-10\n  - about: B3, as printed (identical to B1)\n    test: robust linear regression\n    statistic: b = 0.258, z = 6.474\n    p: 1.847e-10\n  expected:\n    quantity: B1 slope of median held-out distance on days used\n    value: 0.258\n    tolerance: 0.0258\n  criterion: Methods (Across-day drifts, paragraph on cumulative days). For k = 1 to n - 1 days,\n    an OL autoencoder is built on days 1 to k (as in fig2i-distance-cl-vs-ol); each held-out day\n    k+1 to n is projected and its mean pairwise latent distance taken; the median over held-out\n    days is regressed robustly on k. Open details. (1) The robust weighting is not named; readings\n    (a) bisquare (MATLAB robustfit default), (b) Huber. (2) The statistic is called z, which\n    suggests a normal approximation on 9 or 10 points; the p is taken from the fit as reported by\n    the software. B1 is held to its slope, B3 only to the sign and significance because its\n    printed values duplicate B1's. Reproduced when under one reading of (1) both slopes are\n    positive with p < 0.05 and the B1 slope is within tolerance; partially reproduced when both\n    are positive and significant only.\n- id: fig4i-boundary-convergence\n  statement: In B1, a boundary between two hand actions trained on more prior days generalizes\n    better to a new day, with decoding accuracy rising by 5.5 points per added day.\n  source: Results, Plug-and-play control in presence of distributional drift, paragraph 2;\n    Figure 4I\n  quote: 'in B1 trends in decoding performance assessed via linear regression, slope, b = 5.541 ± 0.966 , t ( 8 ) = 5.735 , p = 4.365 × 10 – 4'\n  statistics:\n  - test: linear regression slope\n    statistic: b = 5.541 ± 0.966, t(8) = 5.735\n    p: 4.365e-4\n  expected:\n    quantity: slope of held-out-day accuracy on number of training days\n    value: 5.541\n    tolerance: 0.966\n    unit: percentage points per day\n  criterion: Methods (Across-day drifts, last paragraph). A two-layer MLP in the common latent\n    space classifies left thumb against both middle fingers, trained on days 1 to k (k = 1 to 10)\n    and tested on a day distinct from the 10 daily sessions; OLS of accuracy on k. Open details.\n    The held-out day is not identified (\"a new day distinct from the 10 daily experimental days\");\n    the MLP width is not given (reading 64 units per layer, as for the day-decoding MLP). Reproduced\n    when the slope is positive with p < 0.05 and within tolerance.\n- id: fig5abc-pnp1-b1\n  statement: In B1's first PnP experiment (fixed MLP, 28 days) the average accuracy was 87.43%,\n    time to target 1.195 s and bit rate 1.72 bps.\n  source: Results, Plug-and-play control in presence of distributional drift, paragraph 3;\n    Figure 5A-C\n  quote: The average accuracy across the entire PnP period was 87.43% [84.0%–90.8%] and the average\n    time to target was 1.195 s [1.087s – 1.33s] ( Fig. 5A – B ). This resulted in a mean bitrate of\n    1.72 bps [1.51 – 1.94]\n  statistics:\n  - about: accuracy\n    ci:\n      low: 84.0\n      high: 90.8\n      unit: percent\n  - about: time to target\n    ci:\n      low: 1.087\n      high: 1.33\n      unit: s\n  - about: bit rate\n    ci:\n      low: 1.51\n      high: 1.94\n      unit: bps\n  expected:\n  - quantity: mean accuracy\n    value: 87.43\n    tolerance: 3.43\n    unit: percent\n  - quantity: mean time to target\n    value: 1.195\n    tolerance: 0.135\n    unit: s\n  - quantity: mean bit rate\n    value: 1.72\n    tolerance: 0.22\n    unit: bps\n  criterion: Methods (Discrete PnP experiments; PnP experiments, performance metrics). A trial's\n    output is the first non-zero output of the 5-bin mode filter (the action decoded in more than\n    50% of the accumulated above-threshold bins, ties giving none, OSF code runningMode.m); a trial\n    is accurate when that output is the cued action, and its time is from trial start to that\n    output; trials time out at 5 s. Bit rate per block is log2(C - 1) max(0, N_acc - N_fail) / T\n    with C = 7, T the block's total time. Open details. (1) Whether the averages are over blocks\n    or pooled over trials; readings (a) mean of block values, (b) pooled trials, (c) mean of daily\n    values. (2) Timed-out trials count as failures with 5 s, the reading the bit-rate formula\n    implies. Reproduced when under one reading of (1) all three values are within tolerance.\n- id: fig5def-pnp2-b1\n  statement: In B1's second PnP experiment (38 days, decoder updated with the first experiment's\n    data) the average accuracy was 80.71%, time to target 0.875 s and bit rate 1.848 bps.\n  source: Results, Plug-and-play control in presence of distributional drift, paragraph 3;\n    Figure 5D-F\n  quote: The average accuracy was 80.71% [77.6% – 83.5%] and the average time to target was 0.875\n    s [0.842 s – 0.917 s ] resulting in an effective mean bit rate of 1.848 bps [1.68 – 2.02]\n  statistics:\n  - about: accuracy\n    ci:\n      low: 77.6\n      high: 83.5\n      unit: percent\n  - about: time to target\n    ci:\n      low: 0.842\n      high: 0.917\n      unit: s\n  - about: bit rate\n    ci:\n      low: 1.68\n      high: 2.02\n      unit: bps\n  expected:\n  - quantity: mean accuracy\n    value: 80.71\n    tolerance: 3.11\n    unit: percent\n  - quantity: mean time to target\n    value: 0.875\n    tolerance: 0.042\n    unit: s\n  - quantity: mean bit rate\n    value: 1.848\n    tolerance: 0.172\n    unit: bps\n  criterion: As fig5abc-pnp1-b1, with its readings.\n- id: fig5-pnp-experiments-equal\n  statement: Bit rates do not differ between B1's two PnP experiments.\n  source: Results, Plug-and-play control in presence of distributional drift, paragraph 3\n  quote: There were no significant differences in performance between the two PnP experiments\n    (Mann-Whitney U test on bitrates z = – 0.9574 , p = 0.338 )\n  statistics:\n  - test: Mann-Whitney U\n    statistic: z = -0.9574\n    p: 0.338\n  depends_on:\n  - fig5abc-pnp1-b1\n  - fig5def-pnp2-b1\n  criterion: A claim of absence, judged on the paper's test. Mann-Whitney U on the block bit rates\n    of the two experiments; reproduced when p >= 0.05, not reproduced when p < 0.05. The\n    difference in medians is reported.\n- id: figs8cde-pnp-stable\n  statement: Daily median PnP accuracy shows no linear trend across days in either B1 experiment\n    or in B3.\n  source: Results, Plug-and-play control in presence of distributional drift, paragraph 3;\n    Figure S8C-E\n  quote: a linear fit to the daily median revealed stable performance across-days for both ( Fig.\n    S8C – D , p = 0.897 for PnP Exp 1 and p = 0.11 for PnP Exp 2)\n  statistics:\n  - about: B1 experiment 1\n    test: linear regression slope\n    statistic: t(5) = 0.136\n    p: 0.897\n  - about: B1 experiment 2\n    test: linear regression slope\n    statistic: t(8) = -1.79\n    p: 0.11\n  - about: B3\n    test: linear regression slope\n    statistic: t(7) = 1.035\n    p: 0.3348\n  criterion: A claim of absence, judged on the paper's test. OLS of each PnP day's median accuracy\n    (median over blocks) on day, per experiment. Reproduced when p >= 0.05 in all three\n    experiments; not reproduced when p < 0.05 in any. Slopes are reported.\n- id: fig5-pnp-b1-overall-bitrate\n  statement: Over both B1 PnP experiments the mean effective bit rate was 1.8 bps, with a maximum\n    of 3.351 bps.\n  source: Results, Plug-and-play control in presence of distributional drift, paragraph 3\n  quote: Across both experiments, the mean effective bit rate was 1.8 bps [1.66 – 1.93] and the\n    highest was 3.351 bps\n  statistics:\n  - ci:\n      low: 1.66\n      high: 1.93\n      unit: bps\n  expected:\n  - quantity: mean bit rate, both experiments\n    value: 1.8\n    tolerance: 0.14\n    unit: bps\n  - quantity: maximum block bit rate\n    value: 3.351\n    tolerance: 0.3351\n    unit: bps\n  depends_on:\n  - fig5abc-pnp1-b1\n  - fig5def-pnp2-b1\n  criterion: As fig5abc-pnp1-b1, pooling the blocks of both experiments; the maximum is over\n    blocks. Reproduced when both values are within tolerance under one reading.\n- id: fig5ghi-pnp-b3\n  statement: In B3's PnP experiment (39 days) the average accuracy was 84.9%, time to target 0.818\n    s and bit rate 2.22 bps (maximum 3.508 bps), and accuracy stayed stable across days.\n  source: Results, Plug-and-play control in presence of distributional drift, paragraph 4;\n    Figure 5G-I\n  quote: The average accuracy was 84.9% [82.14% – 87.43%], and the average time to target was 0.818\n    s [0.789 s – 0.848 s ] with a mean bit rate of 2.22 bps [2.046 bps – 2.394 bps ] (maximum of\n    3.508 bps )\n  statistics:\n  - about: accuracy\n    ci:\n      low: 82.14\n      high: 87.43\n      unit: percent\n  - about: time to target\n    ci:\n      low: 0.789\n      high: 0.848\n      unit: s\n  - about: bit rate\n    ci:\n      low: 2.046\n      high: 2.394\n      unit: bps\n  expected:\n  - quantity: mean accuracy\n    value: 84.9\n    tolerance: 2.76\n    unit: percent\n  - quantity: mean time to target\n    value: 0.818\n    tolerance: 0.030\n    unit: s\n  - quantity: mean bit rate\n    value: 2.22\n    tolerance: 0.174\n    unit: bps\n  - quantity: maximum block bit rate\n    value: 3.508\n    tolerance: 0.3508\n    unit: bps\n  criterion: As fig5abc-pnp1-b1, with its readings. Stability is claim figs8cde-pnp-stable.\n- id: fig6g-ibid-angular-error\n  statement: Under IBID, the angular error between integrated and ideal diagonal velocities is\n    centred on zero (mean 1.885 degrees, not different from zero), showing integrated off-axis\n    control.\n  source: Results, PnP control of a virtual robotic arm, paragraph 3; Figure 6G\n  quote: The mean of this circular distribution was 1.885 degrees [95% C.I. −1.44 degrees to 5.206\n    degrees] and not significantly different from zero (circular median, p = 0.348 )\n  statistics:\n  - test: circular median test\n    p: 0.348\n    ci:\n      level: 0.95\n      low: -1.44\n      high: 5.206\n      unit: degrees\n  expected:\n    quantity: circular mean angular error\n    value: 1.885\n    tolerance: 3.321\n    unit: degrees\n  criterion: A claim of absence, judged on the paper's test (Methods, Robot kinematics analyses),\n    the CircStat circular median test (circ_medtest) of the instantaneous angular errors between\n    IBID velocities and the ideal diagonal velocity, over all time points and trials to diagonal XY\n    targets; reproduced when p >= 0.05, not reproduced when p < 0.05. The circular mean and its\n    interval are reported (expected value with the paper's interval). Open detail. Whether\n    time points with zero velocity or before the first input are included; readings (a) all\n    time points, (b) only time points with non-zero velocity.\n- id: fig6g-velocity-covariation\n  statement: PCA of velocities during diagonal reaches shows covariation between X and Y velocity,\n    unlike the non-integrated null model whose components recapitulate the cardinal axes.\n  source: Results, PnP control of a virtual robotic arm, paragraph 3; Figure 6F-G\n  quote: In contrast, data revealed significant velocity covariation due to the integration in IBID\n    ( Fig. 6G , left, middle)\n  criterion: Methods (Robot kinematics analyses). PCA of 2D (X, Y) velocities over the diagonal\n    trials. The paper gives no test for \"significant\". Read as the first principal component's\n    angle from both cardinal axes exceeding 20 degrees and its loading on X and Y both above 0.3 in\n    absolute value; this threshold is a standard choice, not the paper's, and the loadings are\n    reported.\n- id: figs8hi-perspective-perturbation\n  statement: B1 used the PnP decoder proficiently under changed visual perspectives, with 86%\n    (allocentric) and 94% (left-handed) accuracy over 42 trials each.\n  source: Results, PnP control of a virtual robotic arm, paragraph 4; Figure S8H-I\n  quote: We found that B1 could immediately and proficiently use the decoder even with significant\n    visual perturbations, with 86% and 94% decoding accuracies when operating the PnP decoder from\n    either an allocentric or left-handed reference frame respectively (42 trials each\n  expected:\n  - quantity: accuracy, allocentric view\n    value: 86\n    tolerance: 8.6\n    unit: percent\n  - quantity: accuracy, left-handed view\n    value: 94\n    tolerance: 9.4\n    unit: percent\n  criterion: Trial accuracy as for the PnP experiments (fig5abc-pnp1-b1), over the 42 trials of\n    each perturbation. Reproduced when both are within tolerance.\n- id: figs8g-coactivation\n  statement: Imagined coactivations of two actions are discernible from the single actions.\n  source: Results, PnP control of a virtual robotic arm, paragraph 3; Figure S8G\n  quote: B1 was also able to access off-axis directions by coactivating multiple representations\n    simultaneously\n  criterion: Methods (Coactivations of representations). A decoder (3-layer MLP of 64 units, as for\n    the PnP decoder) classifies right thumb or right hand, left leg, head and the coactivations;\n    trial accuracy by max vote. The paper gives no test; read as a binomial test of trial accuracy\n    against 1/m (m the number of classes), at 0.05. Reproduced when it is significant.\n- id: fig7de-mode-switch-learned\n  statement: B1 reached 100% accuracy with the mode switch in the virtual reach-to-grasp and\n    transport task after about one week of practice, with a median completion time of 45 s.\n  source: Results, Flexible control of reaching and grasping, paragraph 2; Figure 7D-E\n  quote: B1 gained rapid proficiency in using the mode-switch with 100% accuracy after ~1 week of\n    practice ( Fig. 7D – E , median task completion time of 45s)\n  expected:\n  - quantity: success rate after about one week\n    value: 100\n    tolerance: 10\n    unit: percent\n  - quantity: median task completion time\n    value: 45\n    tolerance: 4.5\n    unit: s\n  criterion: Over the 10 sessions of the task. Open detail. Which sessions count as \"after ~1\n    week\" and which trials the median time is over; readings (a) sessions from day 7 on, (b) the\n    last session, (c) all sessions for the median time. Reproduced when under one reading the\n    success rate is within tolerance and the median time is within tolerance.\n- id: fig7ij-reach-rotate\n  statement: With the fixed RNN, B1 completed the real-world reach and rotate task with a median\n    success rate of 90% and completion times of 60.8 s.\n  source: Results, Long-term control of grasping and object manipulation using the Kinova Jaco\n    robot, paragraph 1; Figure 7I-J\n  quote: The median success rate was 90% with task completion times of 60.8 s [54.76 s – 76.95 s ]\n  statistics:\n  - about: completion time\n    ci:\n      low: 54.76\n      high: 76.95\n      unit: s\n  expected:\n  - quantity: median success rate\n    value: 90\n    tolerance: 9\n    unit: percent\n  - quantity: task completion time\n    value: 60.8\n    tolerance: 16.15\n    unit: s\n  criterion: Methods (Robot reach-to-grasp metrics). A trial succeeds only when all phases are\n    completed and the reoriented object is placed at the target; completion time runs from the\n    start of robot control to gripper release. Open details. (1) The median success rate is over\n    days or blocks; readings (a) per day, (b) per block. (2) Whether 60.8 s is a median or a mean\n    of successful trials; readings (a) median, (b) mean. Reproduced when under one reading both\n    values are within tolerance.\n- id: fig7k-wall-first-half\n  statement: In the wall task, B1 reached and grasped the object off the wall proficiently across\n    the whole PnP window (median success 100%, mean 94.6%, median time 38.053 s).\n  source: Results, Long-term control of grasping and object manipulation using the Kinova Jaco\n    robot, paragraph 1; Figure 7K top\n  quote: B1 was able to perform the first part (reach and grasp the target off the wall center)\n    proficiently across the entire PnP testing window and for all levels of approach difficulty (\n    Fig. 7K top, median success rate of 100%, mean of 94.6%, median time to reach and grasp object\n    38.053 s [26.825 s – 45.458 s ])\n  statistics:\n  - about: time to reach and grasp\n    ci:\n      low: 26.825\n      high: 45.458\n      unit: s\n  expected:\n  - quantity: median success rate, first half\n    value: 100\n    tolerance: 10\n    unit: percent\n  - quantity: mean success rate, first half\n    value: 94.6\n    tolerance: 9.46\n    unit: percent\n  - quantity: median time to reach and grasp\n    value: 38.053\n    tolerance: 11.228\n    unit: s\n  criterion: As fig7ij-reach-rotate, for the first part of the wall task (object grasped off the\n    wall), over all PnP days before recalibration, with the same readings of the median.\n- id: fig7k-wall-full-decline\n  statement: Full wall-task success declined after PnP day 35 (median 88.19% over the first 35 days\n    against 69.05% over days 35 to 210), with longer completion times.\n  source: Results, Long-term control of grasping and object manipulation using the Kinova Jaco\n    robot, paragraph 1; Figure 7K bottom, 7L\n  quote: 'Here, we observed a drop in performance after PnP day 35 (first 35 days median accuracy of 88.19%, total task completion time 75.52 s [70.22 s – 85.326 s ]; days 35–210 median accuracy of 69.05%, total task completion time 104.854 s [94.648 s – 126.639 s ])'\n  statistics:\n  - about: completion time, first 35 days\n    ci:\n      low: 70.22\n      high: 85.326\n      unit: s\n  - about: completion time, days 35 to 210\n    ci:\n      low: 94.648\n      high: 126.639\n      unit: s\n  expected:\n  - quantity: median success, first 35 days\n    value: 88.19\n    tolerance: 8.819\n    unit: percent\n  - quantity: median success, days 35 to 210\n    value: 69.05\n    tolerance: 6.905\n    unit: percent\n  - quantity: completion time, first 35 days\n    value: 75.52\n    tolerance: 9.806\n    unit: s\n  - quantity: completion time, days 35 to 210\n    value: 104.854\n    tolerance: 21.785\n    unit: s\n  criterion: As fig7ij-reach-rotate, for the full wall task. Open detail. Day 35 falls in both\n    ranges as printed; readings (a) day 35 in the first period, (b) in the second. Reproduced when\n    under one reading the four values are within tolerance and the later median success is\n    lower; partially reproduced when the later success is lower but values fall outside\n    tolerance.\n- id: fig7kl-recalibration-restores\n  statement: Recalibrating the RNN with about 8 min of data immediately restored full wall-task\n    success to 100%, with a median completion time of 80.73 s.\n  source: Results, Long-term control of grasping and object manipulation using the Kinova Jaco\n    robot, paragraph 2; Figure 7K-L\n  quote: Notably, recalibration of the RNN (data required for decoder update was ~8 min, Methods ),\n    immediately improved the success rate to 100% with a median completion time of 80.73 s [51.277\n    s – 108.247 s ]\n  statistics:\n  - about: completion time after recalibration\n    ci:\n      low: 51.277\n      high: 108.247\n      unit: s\n  expected:\n  - quantity: success rate after recalibration\n    value: 100\n    tolerance: 10\n    unit: percent\n  - quantity: median completion time after recalibration\n    value: 80.73\n    tolerance: 29.453\n    unit: s\n  criterion: As fig7ij-reach-rotate, over the wall-task trials after recalibration (day 0 in\n    Figure 7K). Reproduced when both values are within tolerance.\n- id: rnn-training-data-amount\n  statement: The biLSTM decoder was trained on about 14 hours and 48 minutes of open-loop and\n    closed-loop data from B1's virtual and real-world hDoF experiments, before augmentation and\n    segmentation.\n  source: Methods, RNN decoders based on spatiotemporal activity patterns, paragraph 2\n  quote: By the point we got to training a LSTM, we had already collected roughly 14 hours and 48\n    minutes of experimental open-loop and closed-loop data (prior to data augmentation and\n    segmentation) in the virtual 3D environment and with practice with the Kinova Jaco in the\n    real-world using the MLP\n  expected:\n    quantity: total duration of RNN training data\n    value: 888\n    tolerance: 88.8\n    unit: min\n  criterion: The total duration of the trials used to train the RNN, before segmentation. Open\n    detail. Which part of a trial counts; the RNN segments come from \"the active portions of the\n    task\" (Methods), and the OSF code (get_lstm_features.m) takes task states 2 and 3 and pads\n    from state 4; readings (a) the whole stored trial, (b) the active (cue and control) portion\n    only. The dataset may also hold the later real-world fine-tuning trials, which the 14 h 48 min\n    precede; when it labels contexts, the duration is shown with and without real-robot\n    fine-tuning trials. Reproduced when under one reading the duration is within tolerance.\n- id: figs3-spatial-pooling\n  statement: In B1, 2x2 spatial pooling of the grid makes single-trial high-gamma activity more\n    consistent and improves online decoding in pilot blocks.\n  source: Figure S3C and S3F legend\n  quote: A Mann Whitney U test revealed significant differences in median variance between pooled\n    and unpooled channels ( z = 8.721 , p = 2.748 × 10 - 18 )\n  statistics:\n  - about: single-trial variance, pooled against unpooled\n    test: Mann Whitney U\n    statistic: z = 8.721\n    p: 2.748e-18\n  - about: block decoding accuracy, pooled against unpooled\n    test: Mann Whitney U\n    statistic: z = 2.353\n    p: 0.0186\n    n: 10 blocks\n  criterion: Methods (Spatial feature extraction). Variance over time and trials of binned (200 ms)\n    high gamma during right thumb trials, per channel, for the 128 raw channels against the 32\n    channels after a 1 s running average and 2x2 pooling with stride 2; Mann Whitney U. The block\n    accuracy comparison uses online pilot blocks, which only the online decodes can give.\n    Reproduced when the variance test gives p < 0.05 with pooled lower; the accuracy part is\n    reported when testable.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001535/10.1016-j.cell.2025.02.001.yaml paper/10.1016-j.cell.2025.02.001.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -i 's/^    p: 1e-4$/    p: 1.0e-4/' claims/001535/10.1016-j.cell.2025.02.001.yaml && python tools/claims_check.py claims/001535/10.1016-j.cell.2025.02.001.yaml paper/10.1016-j.cell.2025.02.001.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/001535 && grep -n "—\|rather" *.yaml; python - <<'EOF'
import yaml
d=yaml.safe_load(open('10.1016-j.cell.2025.02.001.yaml'))
print(sum(1 for c in d['claims'] if 'statistics' in c), sum(1 for c in d['claims'] if 'criterion' in c), sum(1 for c in d['claims'] if 'expected' in c))
EOF
grep -n "^ *[a-z_]*: [^'\"].*: " 10.1016-j.cell.2025.02.001.yaml | head
```

```
41 52 29
```

**Agent**

I wrote the claims file at `claims/001535/10.1016-j.cell.2025.02.001.yaml`. It has 52 claims; the paper's text was complete enough that I didn't need to stop.

**Text read.** The accepted author manuscript from PubMed Central (PMC11932800), not the version of record. It includes the Results, Discussion, full Methods, the main figure legends and the supplementary legends (Figs S1 to S9, Videos S1 to S4). The supplementary figures exist only as legends, there was no PDF, and I did not see Supplementary Method S1 (a timeline schematic). No claim needs a value that appears only in a figure image.

**Code read.** The paper links an OSF project (doi:10.17605/OSF.IO/TBDWG) holding one file, `bci.zip`; I recorded its sha256 in the opening comment. It is the real-time system: task modules, the feature pipeline, Kalman filter code, the robot simulator, trained decoders, the scripts that fine-tune the RNN decoder, and the mode filter. It contains no offline analysis code, so none of the paper's statistics are implemented there. It disagrees with the Methods twice:
- **Data split:** the code fine-tunes the RNN on an 80/20 split, where the Methods give 85/15.
- **Action names:** the code's names for targets 1 to 7 don't match the Methods' mapping of actions to directions.

**Dataset.** From its title and description only, it holds B1's RNN training trials: 128 channels, high gamma and low-frequency signals at 100 Hz, 7 targets. That is probably not enough for most claims; one claim (the 14 h 48 min of RNN training data) is aimed directly at it.

**Counts**

| | Claims |
|---|---|
| Total | 52 |
| With quotes | 52 |
| With statistics | 41 (127 p-values and interval bounds) |
| With criteria | 52 |
| With expected values | 29 |

The quote checker finds all 52 quotes. It flags one value, p = 3.2442e-12 in `figs7i-ibid-straighter-than-refit`. I confirmed by reading that the paper prints exactly this; the checker only searches four significant digits.

**Details the paper leaves open, with the readings named**
- **Channel neighbours for cluster correction (Fig 1):** 4-connected or 8-connected.
- **Fig 1I-J:** which channels (the paper's hand-knob and ventral channels, or every significant channel), and how a repeated-measures ANOVA is formed over unpaired trials (one-way across actions, or trials paired by repetition).
- **Fig 1K-L correlation:** Pearson or Spearman.
- **Binomial chance test:** the usual upper tail, with the paper's wording ("area from 0 to N/m") shown as a variant.
- **Autoencoder:** reconstruction loss (mean squared or mean absolute error) and amount of augmentation (none, or doubled).
- **Per-subject variance scaling (Fig 2J):** none, divide by the maximum, or z-score.
- **Fig 2M-N points:** all three contexts, CL2 only, or the mean per session; the fit is a binomial model on the proportion.
- **CKA (Fig 3):** which samples go through both networks (pooled days, or each day through both), and what the shuffle permutes (weight entries or units).
- **Fig 4B:** which days, channels and observations underlie t(11).
- **Fig 4C-D:** how day labels enter the autoencoder (one unit per day, or per day and action) and whether splits are by sample or by trial.
- **Fig 4F-G robust regression:** bisquare or Huber weighting.
- **Fig 4I:** the held-out day isn't identified, and the classifier's width is not given (64 units assumed).
- **Fig S6 distances:** 72 pooled values or 36 averaged over the two days.
- **PnP averages (Fig 5):** over blocks, pooled trials, or days; timed-out trials count as failures.
- **Fig 6G angular error:** all time points, or only those with non-zero velocity.
- **Fig 7 metrics:** median over days or blocks; median or mean completion time; which sessions count as "after ~1 week"; whether day 35 belongs to the first period or the second.
- **RNN training duration:** the whole stored trial, or only its active portion.
- **No test given:** for Fig 1M-N clustering, Fig S5 map preservation, Fig 6G velocity covariation and Fig S8G coactivation, I set thresholds myself as standard choices and labelled them as not the paper's.

**Gaps in the paper**
- **Fig 4F-G:** the paper prints identical slope, z and p for B1 and B3, so one is likely a copy. B3 is held only to the slope's sign and significance.
- **Not stated anywhere:** the number of null iterations for the Fig S2 test, the temporal smoothing kernel, and whether the ± spreads in Fig S4G are SD or SE.
- **Never named:** the Fig 4B channels and the Fig 4I test day.

Nothing a claim needed was missing outright.

## End of run

33 turns, 8 minutes, result: success.
