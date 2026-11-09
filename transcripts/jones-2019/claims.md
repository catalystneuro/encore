# jones-2019 · claims · run 42716800690

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/ | head; ls claims | grep jones
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,192p docs/protocol.md; ls paper; ls claims/jones-2019.yaml
```

```
Exit code 2
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
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim's statement, expected values or criterion. A method detail the file
  lacks it takes from the paper, citing the passage, and it asks a reader
[... 154 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 85,120p docs/protocol.md
```

```
reader check the statement against the paper without opening it. For a
     finding shown only in a figure, quote the legend or the sentence of the
     Results that cites the panel.
   - `inferred`: every finding has a quote or, when no sentence of the paper
     states it (numbers only in a table, a result spread over several
     legends), a short note under `inferred` saying so. The statement is
     then a reading of the paper, and the note says what it was
     read from.
   - `statistics`: the statistical support the paper reports for the
     finding, one entry per test or interval: what it compares (`about`,
     when there is more than one), the `test` and `statistic` as named, the
     `p`-value as a number (a bound such as "p < 0.05" is `p: 0.05` with
     `p_relation: "<"`; a printed "P = 0" is recorded as 0), any `corrected`
     for multiple comparisons, a confidence interval (`ci`), and `n` in
     words. It records the paper; the
     numbers the attempt must match, with tolerances, stay in `expected`.
     Record only tests whose result is the finding. A significance threshold
     used to select or count units, cells or pairs ("238 of 288 neurons were
     better fit, p < 0.05") is a method, not a result, and is left out.
     Leave the field out when the paper reports no test or interval for the
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/fouke-2025.yaml | head -150; wc -l claims/fouke-2025.yaml paper/*.txt; cat papers/datasets/jones-2019.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 150,330p claims/fouke-2025.yaml
```

```
data: with_labels
  depends_on:
  - stimulus-code-link
  criterion: For each fish, the mean of its median angular velocities for the rightward
    stimuli (right, forward right, backward right) minus the mean for the leftward stimuli
    (left, forward left, backward left). Reproduced when this difference is greater than zero
    in each species by a one-sided Wilcoxon signed-rank test at p < 0.05; partially reproduced
    when it holds in one species only. The per-stimulus species medians are reported as well.
- id: fig1h-zf-higher-angular-acceleration
  statement: Across directional stimuli ZF have higher angular acceleration than DC, and the
    distributions of the two species differ for every stimulus.
  source: Results, Optic flow induces angular matching and turns in DC, paragraph 2; Figure 1H
    (Kruskal-Wallis test with Bonferroni correction)
  quote: Across directional stimuli, ZF maintained higher angular acceleration than DC
  statistics:
  - test: Kruskal-Wallis test
    p: 0.05
    p_relation: "<"
    corrected: Bonferroni
  data: with_labels
[... 152 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2019.10.056.txt",
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2019.10.056.txt",
 "offset": 700,
 "limit": 1000
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2019.10.056.txt",
 "offset": 1700,
 "limit": 760
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text, Methods, supplement (Figures S1 to S4, Tables S1, S3, S4) and Table S2 are all present. Next: the dataset description and the paper's code.

**Agent calls Bash**

```bash
cd  cat paper/hc-26.data-description.txt; cd $TMPDIR && git clone -q https://github.com/emilyasterjones/SWR-predictions && cd SWR-predictions && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -100
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/SWR-predictions; cat README.md; echo ======; cat "SWR abundance/runcalcriprates.m" "SWR abundance/calcriprates2.m" "SWR abundance/getvalidrips.m"
```

```
# Jones et al, 2019 [![DOI](https://www.zenodo.org/badge/DOI/10.5281/zenodo.4285621.svg)](https://doi.org/10.5281/zenodo.4285621)

MATLAB and Python scripts used to generate "Early Hippocampal Sharp-Wave Ripple Deficits Predict Later Learning and Memory Impairments in an Alzheimer’s Disease Mouse Model"

Preprint: https://www.biorxiv.org/content/10.1101/596569v1.full
Publication: https://www.cell.com/cell-reports/fulltext/S2211-1247(19)31370-1
Dataset: http://crcns.org/data-sets/hc/hc-26/about-hc-26

Requires the following libraries:
NeuroQuery: https://bitbucket.org/mkarlsso/neuroquery/src/master/
Trodes: https://bitbucket.org/mkarlsso/trodes/src/master/
Chronux: http://chronux.org/ 
======
% Construct filter
 figopt=2;
 clearvars -except figopt f

E3 = {'r1_01_', 'r1_12_', 'r1_18_', 'r1_21_', 'r1_29_', 'r1_33_', 'r1_34_',  'r1_39_',...
    'r2_06_', 'r2_17_', 'r2_28_',...
    'r3_02_', 'r3_11_'};
[... 260 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SWR-predictions; cat Preprocessing/ej_rippledayprocess.m Preprocessing/ag_extractripples.m Preprocessing/dayprocess_trodes.m | head -400; ls -la Preprocessing
```

```
function ej_rippledayprocess(directoryname,fileprefix,day,epoch)
%RIPPLEDAYPROCESS(directoryname,fileprefix,days, options)
%
%Applies a ripple filter to all epochs for each day and saves the data in
%in the EEG subdirectory of the directoryname folder.
%
%directoryname - example '/data99/user/animaldatafolder', a folder
%                containing processed matlab data for the animal
%
%fileprefix -    animal specific prefix for each datafile (e.g. 'fre')
%
%days -          a vector of experiment day numbers

% load('C:\Users\HuangShared\Documents\MATLAB\Filters\agripplefilter3.mat'); % 125-250
load('C:\Users\HuangShared\Documents\MATLAB\Filters\agripplefilter.mat'); %150-250

minint = -32768;

% create the list of files for this day that we should filter
flist = dir(sprintf('%s/*eeg%02d-%d-*.mat', directoryname, day, epoch));
[... 308 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SWR-predictions; cat "SG Power/runRTS.m" "SG Power/RTspecgram3.m"; sed -n 1,200p "SG Power/plotRTSstats.m"
```

```
myCluster = parcluster('local');
myCluster.NumWorkers = 6;
saveProfile(myCluster);

E3 = {'r1_01_', 'r1_12_', 'r1_18_', 'r1_21_', 'r1_29_', 'r1_33_', 'r1_34_',  'r1_39_',...
    'r2_06_', 'r2_17_', 'r2_28_',...
    'r3_02_', 'r3_11_'};
E4 = {'r1_05_', 'r1_24_', 'r1_31_', 'r1_35_', ...
    'r2_08_', 'r2_13_', 'r2_14_', 'r2_26_', 'r2_27_', 'r2_36_', 'r2_38_',...
    'r3_04_', 'r3_09_', 'r3_20_', 'r3_32_', 'r3_40_'};
animals = [E3 E4];

analysisdir = 'E:\\LFP Data\CRCNS\Cohort 1\Preprocessed Data';
group = 'Cohort 1';

epochfilter = [];
epochfilter{1} = {'task','(~strcmp($env, ''FAIL'') && ~strcmp($descript, ''FAIL''))'};

datafilter = [];  % load all channels...use embedded filter in run function to get specific ones
datafilter{1} = {'chinfo','(~isequal($area,''dead''))'};
[... 365 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SWR-predictions; cat loocv.m fit_train_to_test.m pull_apa_metrics.py; grep -n -i "gauss\|smooth\|std" Preprocessing/pos_trodes.m Preprocessing/ag_addvelocity.m | head -30
```

```
% Leave-one-out cross-validation
% Calculates mean & stdev of R and p values after deleting each value
% (stats rows 1 - 4) plus the number of combinations in which the p value
% fell below significance (stats row 5)

%replace x and y_mat with data
x = zeros(10,1);
y_mat = zeros(10,5);

R = NaN(size(y_mat,1),size(y_mat,2));
p = NaN(size(y_mat,1),size(y_mat,2));
for i = 1:size(y_mat,2)
    y = y_mat(:,i);
    for a = 1:length(y_mat)
        y_sub = y;
        y_sub(a,:) = [];
        x_sub = x;
        x_sub(a,:) = [];
        [R(a,i),p(a,i)] = corr(x_sub,y_sub,'rows','complete');
    end
[... 314 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/claims_check.py; grep -n "kind\|allowed\|KEYS\|keys" tools/claims_check.py | head -40; ls docs; grep -l "crcns" claims/*.yaml | head -3
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

[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; head -30 claims/bruno-2017.yaml
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
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 211 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:5000]); print(list(s['properties']))"
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
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SWR-predictions; grep -rn "600\|immobil" --include=*.m . | grep -v "^./Preprocessing/read" | head -20; sed -n 1,40p rainbow_plots.m; sed -n 100,130p Preprocessing/pos_trodes.m
```

```
./MUA/runRTMUA.m:13:timefilter{1} = {'<function> get2dstate <argname> immobilecutoff <argval> 1','($immobilitytime > 30)'}; %sleep
./MUA/extract_spikes.m:68:    mua{day}{epoch}{i}.descript = 'MUA extracted with exportSpikes, 600-6000Hz filtered, CC reference';
./SWR abundance/runcalcriprates.m:20:timefilter{1} = {'<function> get2dstate <argname> immobilecutoff <argval> 1','($immobilitytime > 30)'};
./SG Power/runRTS.m:23:timefilter{1} = {'<function> get2dstate <argname> immobilecutoff <argval> 1','($immobilitytime > 30)'};
% Input: animkey = animal names for entire cohort sorted by a feature
% animnames = animal names for this expt
% x = data, where x(:,1) = feature & x(:,2-end) = behavior
% Output: scatterplots for all feature x behaviors
% Update points & axis sizes to match Illustrator files
% Manually update axes limits to match Illustrator files

% animnames = cell(1,1);
% animkey = cell(1,1);
% x = zeros(0,0);

rgb = colormap(jet(length(animkey)));
colorhash = containers.Map(animkey,1:length(animkey));

cmap = [];
for i = 1:length(animnames)
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
from scipy import stats
import numpy as np
for k,n in [(9,88),(8,40),(5,30)]:
    print(k,n,stats.binom.sf(k-1,n,0.05), stats.binomtest(k,n,0.05).pvalue)
def p(F,d): return stats.f.sf(F,1,d)
def hs(ps):
    ps=np.array(ps);o=np.argsort(ps);m=len(ps);adj=np.empty(m);run=0
    for i,j in enumerate(o):
        a=1-(1-ps[j])**(m-i);run=max(run,a);adj[j]=min(run,1)
    return adj
swr=[p(7.51,9),p(5.45,9),p(6.66,9),p(13.39,9)];print('swr raw',swr,hs(swr))
sg=[p(32.64,8),p(13.48,8),p(7.61,8),p(6.02,8),p(8.27,8)];print('sg raw',sg,hs(sg))
print('sg+swr',hs(swr+sg))
apa=[p(5.81,8),p(16.42,8),p(7.33,8)];print('apa',apa,hs(apa))
apa2=[p(32.53,7),p(9.04,7)];print('apa2',apa2,hs(apa2), hs(apa2+[p(6.74,7)]))
print('apaall',hs(apa+apa2+[p(6.74,7)]))
f4=[p(5.82,9),p(11.08,9),p(10.89,9)];print('f4',f4,hs(f4))
f4b=[p(13.21,8),p(6.74,8)];print(f4b,hs(f4b),hs(f4b+[p(4.25,8)]))
print('f4all', hs(f4+f4b))
print('f4 all5 +night', hs(f4+[p(2.30,9)]))
print('f4 apa3',hs(f4b+[p(4.25,8)]))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    from scipy import stats
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Bash**

```bash
cd $TMPDIR; (python3 -m venv v && v/bin/pip -q install scipy numpy) >/dev/null 2>&1; v/bin/python -c "import scipy;print(scipy.__version__)"
```

```
1.18.1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
$TMPDIR/v/bin/python -c "
from scipy import stats
import numpy as np
for k,n in [(9,88),(8,40),(5,30)]:
    print(k,n,stats.binom.sf(k-1,n,0.05), stats.binomtest(k,n,0.05).pvalue)
def p(F,d): return stats.f.sf(F,1,d)
def hs(ps):
    ps=np.array(ps);o=np.argsort(ps);m=len(ps);adj=np.empty(m);run=0
    for i,j in enumerate(o):
        a=1-(1-ps[j])**(m-i);run=max(run,a);adj[j]=min(run,1)
    return np.round(adj,3)
swr=[p(7.51,9),p(5.45,9),p(6.66,9),p(13.39,9)];print('swr raw',np.round(swr,4),hs(swr))
sg=[p(32.64,8),p(13.48,8),p(7.61,8),p(6.02,8),p(8.27,8)];print('sg raw',np.round(sg,4),hs(sg))
print('sg+swr',hs(swr+sg))
apa=[p(5.81,8),p(16.42,8),p(7.33,8)];print('apa',np.round(apa,4),hs(apa))
apa2=[p(32.53,7),p(9.04,7)];print('apa2',hs(apa2), hs(apa2+[p(6.74,7)]))
print('apaall',hs(apa+apa2+[p(6.74,7)]))
f4=[p(5.82,9),p(11.08,9),p(10.89,9)];print('f4',np.round(f4,4),hs(f4))
f4b=[p(13.21,8),p(6.74,8)];print(f4b,hs(f4b),hs(f4b+[p(4.25,8)]))
print('f4all', hs(f4+f4b))
print('f4 +night', hs(f4+[p(2.30,9)]))
for F,d in [(11.4,9),(27.3,11),(14.3,14),(30.1,8),(23.7,8),(19.2,7),(8.9,9),(8.9,8),(19.7,8)]:
  print(F,d,'r2',F/(F+d))
"
```

```
9 88 0.03192402252828655 0.042880659325692634
8 40 0.0007115084380675609 0.0007115084380675609
5 30 0.01563551012853307 0.01563551012853307
swr raw [0.0228 0.0444 0.0297 0.0052] [0.067 0.067 0.067 0.021]
sg raw [0.0004 0.0063 0.0247 0.0397 0.0206] [0.002 0.025 0.061 0.061 0.061]
sg+swr [0.118 0.118 0.118 0.041 0.004 0.043 0.118 0.118 0.118]
apa [0.0425 0.0037 0.0268] [0.053 0.011 0.053]
apa2 [0.001 0.02 ] [0.002 0.039 0.039]
apaall [0.078 0.018 0.078 0.004 0.077 0.078]
f4 [0.0391 0.0088 0.0092] [0.039 0.026 0.026]
[np.float64(0.006641076807377943), np.float64(0.03180752290886787)] [0.013 0.032] [0.02  0.063 0.073]
f4all [0.063 0.035 0.035 0.033 0.063]
f4 +night [0.077 0.035 0.035 0.164]
11.4 9 r2 0.5588235294117647
27.3 11 r2 0.7127937336814623
14.3 14 r2 0.5053003533568905
30.1 8 r2 0.7900262467191601
23.7 8 r2 0.7476340694006309
19.2 7 r2 0.732824427480916
8.9 9 r2 0.4972067039106146
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/pip -q install pymupdf >/dev/null 2>&1; $TMPDIR/v/bin/python -c "
import fitz
d=fitz.open('paper/10.1016-j.celrep.2019.10.056.pdf')
for i in [21,23,3]:
    d[i].get_pixmap(dpi=110).save('$TMPDIR/p%d.png'%(i+1))
print(len(d))"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p22.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p24.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import pymupdf as fitz
d=fitz.open('paper/10.1016-j.celrep.2019.10.056.pdf')
for i in [2,3,4,6,8]:
    d[i].get_pixmap(dpi=120).save('$TMPDIR/p%d.png'%(i+1))
" 2>/dev/null; ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p5.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p4.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p7.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p9.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import pymupdf as fitz
d=fitz.open('paper/10.1016-j.celrep.2019.10.056.pdf')
d[17].get_pixmap(dpi=120).save('$TMPDIR/p18.png')
d[19].get_pixmap(dpi=100).save('$TMPDIR/p20.png')
" 2>/dev/null
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p18.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR/SWR-predictions; cat MUA/runRTMUA.m | head -60; grep -v "^\s*%" MUA/RTMUA.m | head -120
```

```
E3 = {'r1_01_', 'r1_12_', 'r1_18_', 'r1_21_', 'r1_29_', 'r1_33_', 'r1_34_',  'r1_39_',...
    'r2_06_', 'r2_17_', 'r2_28_',...
    'r3_02_', 'r3_11_'};
E4 = {'r1_05_', 'r1_24_', 'r1_31_', 'r1_35_', ...
    'r2_08_', 'r2_13_', 'r2_14_', 'r2_26_', 'r2_27_', 'r2_36_', 'r2_38_',...
    'r3_04_', 'r3_09_', 'r3_20_', 'r3_32_', 'r3_40_'};
animals = [E3 E4];

epochfilter = [];
datafilter = [];  %only works with single channel specified
datafilter{1} = {'chinfo','(~isequal($area,''dead''))'};
timefilter = [];
timefilter{1} = {'<function> get2dstate <argname> immobilecutoff <argval> 1','($immobilitytime > 30)'}; %sleep

trigcrit = '(isequal($area,''ca1'') && contains($layer,''**pyr 1**''))';
probecrit = trigcrit;

epochfilter{1} = {'task','(isequal($treatment, ''Veh'') && ~isequal($env,''FAIL''))'};
f = createfilter('animal', animals, 'epochs', epochfilter, 'data', datafilter, 'excludetime', timefilter);
f = setfilterfunction(f, 'RTMUA', {'mua','ripples','chinfo'},'minstd',3,'trig',trigcrit,'probe',probecrit);
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/SWR-predictions; sed -n 60,140p MUA/runRTMUA.m
```

```
for t = 1:length(results{1}{e}.baserate)
                for p = 1:length(siteinds)%1:length(results{1}{e}.baserate{t})
                    [sites{a},siteinds] = intersect(results{1}{e}.probeindex(:,3),sites{a});
                    fullbaserate{a} = [fullbaserate{a}; results{1}{e}.fullbaserate{t}{p}];
                    baserate{a} = [baserate{a}; results{1}{e}.baserate{t}{siteinds(p)}];
                    sdfullbaserate{a} = [sdfullbaserate{a}; results{1}{e}.sdfullbaserate{t}{p}];
                    sdbaserate{a} = [sdbaserate{a}; results{1}{e}.sdbaserate{t}{p}];
                    psth{a} = [psth{a}; results{1}{e}.psth{t}{p}];
                    normpsth{a} = [normpsth{a}; (results{1}{e}.psth{t}{p}-results{1}{e}.baserate{t}{p})./results{1}{e}.sdbaserate{t}{p}];
                    timebase{a} = [timebase{a}; results{1}{e}.psth{t}{p}(:,5)];
                    wave{a} = [wave{a}; results{1}{e}.wave{t}{p}];
                    peakrate{a} = [peakrate{a}; results{1}{e}.peakrate{t}{p}];%(:,1)
                    SWRrate{a} = [SWRrate{a}; results{1}{e}.SWRrate{t}{siteinds(p)}];
                    normrate{a} = [normrate{a}; results{1}{e}.normrate{t}{siteinds(p)}];                    
                end
            end
        end
    end
    animnames = [animnames; f(a).animal(3)];
    animgeno = [animgeno; f(a).animal(4)];
[... 2 more lines not kept]
```

**Agent**

I have what I need. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/jones-2019.yaml",
 "content": "# Claims for Jones, Gillespie, Yoon, Frank & Huang (2019), Cell Reports 29, 2123-2133, \"Early\n# Hippocampal Sharp-Wave Ripple Deficits Predict Later Learning and Memory Impairments in an\n# Alzheimer's Disease Mouse Model\", doi:10.1016/j.celrep.2019.10.056, on CRCNS data set hc-26\n# (doi:10.6080/K0D798NB).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-09,\n# protocol as stated in docs/protocol.md (Reader), version pilot-14.\n#\n# Text read: the version of record with its supplemental information, as text extracted from the\n# PDF under paper/ (main text, STAR Methods, Figures S1 to S4 with legends, Tables S1, S3 and S4),\n# and Table S2 (mmc2.xlsx, three sheets), appended to the same text. The PDF was opened only to\n# read numbers printed inside figure panels (R and p of the scatter plots, Figures 2, 3, 4 and S1,\n# and the directions in Figures S3 and S4); these are marked \"read from the panel\". The data set's\n# description (paper/hc-26.data-description.txt) was read only to know what it holds.\n#\n# Code read: https://github.com/emilyasterjones/SWR-predictions, commit ca056a8 (2023-05-06),\n# linked from the Key Resources Table and Data and Code Availability. MATLAB in the Frank lab\n# filter framework (needs NeuroQuery, Trodes, Chronux; the framework functions get2dstate,\n# createfilter, extracteventsnew's caller are not all in the repository). Preprocessing/ (ripple\n# filtering ej_rippledayprocess.m, detection ag_extractripples.m, positions pos_trodes.m), SWR\n# abundance/ (runcalcriprates.m, calcriprates2.m, getvalidrips.m), SG Power/ (runRTS.m,\n# RTspecgram3.m, plotRTSstats.m), MUA/ (runRTMUA.m, RTMUA.m; the plotting part refers to fields\n# RTMUA.m does not produce), Dentate Spikes/, loocv.m (leave-one-out check), fit_train_to_test.m\n# (screen model applied to replication data), rainbow_plots.m, and pull_apa_metrics.py (APA\n# distance per movement bout). The behavioral metrics other than distance per bout were taken from\n# Ethovision, Tracker and Excel, which are not code.\n#\n# Data the paper used. Female apoE3-KI (E3) and apoE4-KI (E4) mice, two cohorts (Table S1).\n# Screen cohort (Cohort 1): recordings at 12-18 months, 13 E3 and 16 E4 (CA3 SG power 11 and 13);\n# MWM at 13-19 months, 20 E3 and 19 E4. Replication cohort (Cohort 2): recordings at 5-8 months\n# (13 E3, 17 E4; CA3 12 and 16), 9-11 months (12, 17; CA3 11, 16) and 13-17 months (9, 15; CA3 9,\n# 14); MWM at 6-9 months (13, 13); open field, elevated plus maze and MWM at 14-18 months (12, 15);\n# APA and hot plate at 15-20 months (12, 13). Some behavior-only mice were added to Cohort 2.\n# Each recording time point is 5 daily 60 min home-cage sessions, LFP from a 32-site probe in right\n# dorsal hippocampus (CA1, CA3, DG), with 30 Hz position tracking; MUA in Cohort 1 only. Behavior\n# results are in the data set's Behavior Excel file with MWM and APA tracking. The correlations use\n# the E4 mice that have both measures: screen n = 16 (SWR abundance) and 13 (CA3); replication MWM\n# n = 11 and 10; APA n = 10 and 9; Figure 4 n = 11 (MWM) and 10 (APA).\n#\n# Methods fixed for all claims, with their sources.\n# (A) SWR detection and abundance. Methods (Analysis of Neural Data): LFP 0.1-300 Hz at 1 kHz\n# (as deposited); equiripple band-pass 150-250 Hz (the code's agripplefilter.mat; 125-250 Hz is\n# agripplefilter3.mat); detection on the CA1 site closest to the centre of stratum pyramidale (the\n# code takes the chinfo site with area ca1 and layer containing \"pyr 1\"); an SWR is the envelope\n# exceeding 5 SD above baseline for at least 15 ms. The code smooths the envelope with a 4 ms\n# Gaussian and takes baseline and SD as the mean and SD of that envelope over the whole session\n# (ag_extractripples.m); the Methods do not say, so the code settles it. The code detects events\n# above 3 SD for 15 ms and keeps those whose peak reaches 5 SD (runcalcriprates.m, bins [5 50]);\n# the Methods read as above 5 SD for 15 ms. The Methods reading is the main one, the code's the\n# variant. The code also drops events within 0.4 s of the session's start or end and events that\n# coincide with events on 16 or more channels (getvalidrips.m); the Methods are silent, so these\n# follow the code. Immobility (Methods; code runcalcriprates.m) is Gaussian-smoothed velocity\n# (the deposited pos.vel, 500 ms Gaussian) below 1 cm/s, counted only after it has lasted 30 s.\n# Sessions with less than 10 min of such immobility are excluded (Methods). Abundance is SWRs per\n# second of immobility in each session, averaged over the mouse's sessions (Methods, last\n# paragraph; code calcriprates2.m and runcalcriprates.m figopt 1).\n# (B) SWR-associated SG power. Methods: multitaper SWR-triggered spectrogram per site, 100 ms\n# window, z-scored; the mean z-scored power over 30-50 Hz in the window 0-100 ms after detection,\n# averaged over SWRs and over sites in the region; CA3 is its stratum pyramidale and radiatum\n# sites, CA1-sr the stratum radiatum sites, DG the hilus and granule cell sites with confirmed\n# dentate spikes. The code (runRTS.m, RTspecgram3.m, plotRTSstats.m) settles: 3 tapers (time-\n# bandwidth 3), non-overlapping 100 ms windows from -0.4 to 0.4 s around the threshold crossing,\n# the window centred at 50 ms; z-score per frequency against the mean and SD of the same\n# spectrogram of the immobile LFP of the session. Two code choices differ from the Methods and are\n# variants: the code triggers on all events above 3 SD (minstd 3), where the Methods and Table S2\n# (the main CA3 values equal its 5 SD column) use the 5 SD SWRs; and the code's frequency bins 4\n# to 7 of a 7.8 Hz grid (31.3, 39.1, 46.9, 54.7 Hz) include 54.7 Hz, where the Methods' 30-50 Hz\n# holds 31.3, 39.1 and 46.9 Hz. Open, could change values: the Methods analyse per session and\n# average over sessions, the code pools the SWRs of all sessions per site; both are to be run.\n# (C) MWM metrics (Methods, Analysis of Behavioral Data): escape latency is the mean of the 4\n# daily trials; slope over days 1 to k is the slope of a first-degree polynomial fitted to the\n# daily means; overnight change (\"Night 1 Learning\") is latency on day 2 trial 1 minus day 1\n# trial 4 (Figure S1C); probe area under the distance-to-platform curve over the first 5 s, by the\n# trapezoid method; percent time in target quadrant and target crossings as exported.\n# (D) APA metrics on training days 1-4 after the habituation day (Methods, Behavior): entrances,\n# latency to first entrance, path length, percent time in the quadrant opposite the shock zone,\n# and distance from the shock zone per movement bout (pull_apa_metrics.py: 1 s steps, a bout is\n# movement of 2 cm/s or more; \"Avg Travel Away from SZ (cm)\").\n# (E) Performance scores (Quantification and Statistical Analysis): z-score each metric, invert\n# the sign where higher is worse (latencies, slopes, overnight change, probe area under the curve,\n# entrances, distance per bout), average. MWM learning score: slope days 1-2 and 1-3, latency day\n# 3, overnight change days 1-2; MWM memory precision: percent time in target quadrant probes 1\n# and 2, crossings probe 1, area under the curve probes 1 and 2; APA learning: latency to first\n# entrance, path length, percent time opposite, day 2; APA memory precision: entrances day 2,\n# distance per bout days 2 and 3. Open, could change the scores: the population of the z-score\n# (\"Z scored across the population\"): (i) the E4 mice in the correlation, (ii) all mice of the\n# cohort of both genotypes; both are to be run.\n# (F) Tests (Quantification and Statistical Analysis; figure legends): correlations are Pearson\n# (Spearman where stated), reported as F(1, n-2) of the regression, two-sided, alpha 0.05. In the\n# replication cohort p is adjusted with Holm-Sidak. The family is not stated; the printed adjusted\n# p are reproduced, from the printed F, by step-down Sidak without enforced monotonicity (as\n# Prism prints it) within the planned metrics of one SWR property: the 4 MWM learning metrics for\n# SWR abundance, the 5 MWM probe metrics for CA3 SG power, and the 5 APA day 2 metrics for each\n# property. The criteria use that family.\n# (G) Predicted scores (Figures 2N, 2R, 3F, 3I, 4I, 4L): a linear regression of the screen\n# cohort's score on its z-scored SWR property, applied to the replication cohort's z-scored\n# property, correlated (Pearson) with the actual score. The printed F and percent of variance are\n# those of this Pearson correlation (for example 0.56 = 11.4/(11.4+9)); they do not depend on the\n# regression coefficients. fit_train_to_test.m also computes an out-of-sample F against the test\n# mean; that is shown as a variant.\nschema_version: 2\npaper: doi:10.1016/j.celrep.2019.10.056\nclaims:\n- id: fig1e-swr-abundance-genotype\n  statement: In the aged screen cohort, apoE4-KI mice have lower SWR abundance than apoE3-KI mice.\n  source: Results, Aged ApoE4-KI Mice Show SWR Deficits, paragraph 1; Figure 1E\n  quote: apoE4-KI mice had reduced SWR abundance and associated SG power in CA1, CA3, and DG (Figures 1E\n    and 1F)\n  statistics:\n  - test: unpaired t test\n    statistic: t(27) = 8.42\n    p: 0.0001\n    p_relation: \"<\"\n    n: 13 apoE3-KI and 16 apoE4-KI mice, aged 12-18 months\n  criterion: SWR abundance by method (A) per mouse of Cohort 1; a two-tailed unpaired t test of E3\n    against E4. Reproduced when E4 is lower with p < 0.0001; partially reproduced when E4 is lower\n    with p < 0.05.\n- id: fig1f-sg-power-genotype\n  statement: In the aged screen cohort, SWR-associated SG power is lower in apoE4-KI than in apoE3-KI\n    mice in CA1 stratum radiatum, CA3 and the dentate gyrus.\n  source: Results, Aged ApoE4-KI Mice Show SWR Deficits, paragraph 1; Figure 1F\n  quote: apoE4-KI mice had reduced SWR abundance and associated SG power in CA1, CA3, and DG\n  statistics:\n  - about: CA1 stratum radiatum\n    test: unpaired t test\n    statistic: t(27) = 5.17\n    p: 0.0001\n    p_relation: \"<\"\n    n: 13 apoE3-KI and 16 apoE4-KI mice\n  - about: CA3\n    test: unpaired t test\n    statistic: t(22) = 4.91\n    p: 0.0001\n    p_relation: \"<\"\n    n: 11 apoE3-KI and 13 apoE4-KI mice\n  - about: dentate gyrus\n    test: Mann-Whitney\n    statistic: U = 45\n    p: 0.0087\n    n: 13 apoE3-KI and 16 apoE4-KI mice\n  criterion: SG power by method (B) for each region, per mouse of Cohort 1; the tests as in the\n    legend (unpaired t tests for CA1-sr and CA3, Mann-Whitney for DG). Reproduced when E4 is lower\n    with p < 0.05 in all three regions under one of the readings of method (B); partially\n    reproduced for two regions.\n- id: figs1a-mua-during-swrs\n  statement: Multi-unit activity in CA1 stratum pyramidale rises from before to during SWRs in both\n    genotypes, with no genotype difference before or during SWRs.\n  source: Results, Aged ApoE4-KI Mice Show SWR Deficits, paragraph 1; Figure S1A\n  quote: We also observed an increase in multi-unit activity in CA1 stratum pyramidale (Figure S1A) during\n    SWRs, which was not different between genotypes\n  statistics:\n  - about: before against during, apoE3-KI\n    test: paired t test\n    statistic: t(12) = 5.54\n    p: 0.0001\n    n: 13 apoE3-KI mice\n  - about: before against during, apoE4-KI\n    test: paired t test\n    statistic: t(15) = 4.56\n    p: 0.0004\n    n: 16 apoE4-KI mice\n  - about: genotype, before SWRs\n    test: t test\n    statistic: t(27) = 0.78\n    p: 0.21\n  - about: genotype, during SWRs\n    test: t test\n    statistic: t(27) = 0.67\n    p: 0.94\n  criterion: Cohort 1 MUA spike times (above 75 uV, 600-6000 Hz, corpus callosum reference, as\n    deposited) on the SWR detection site; rate during SWRs in 0-100 ms after detection (Figure S1A\n    legend; RTMUA.m bin 5). The baseline \"400 ms before SWR detection\" is open; readings (a) the\n    whole 400 ms before detection, (b) the 100 ms bin from -400 to -300 ms (RTMUA.m bins). Per\n    mouse, the mean over SWRs and sessions. Reproduced when the paired t test gives p < 0.05 in\n    each genotype with the rate higher during, and unpaired t tests between genotypes give p >=\n    0.05 both before and during. The absence part is judged on the t tests alone.\n- id: fig1g-mwm-impaired\n  statement: Aged apoE4-KI mice of the screen cohort learn the hidden platform location more slowly\n    on the MWM than apoE3-KI mice, with higher escape latencies, significant on hidden days 1, 3\n    and 5.\n  source: Results, Aged ApoE4-KI Mice Show SWR Deficits, paragraph 1; Figure 1G\n  quote: as well as impaired MWM learning (Figure 1G)\n  statistics:\n  - about: genotype effect\n    test: two-way repeated-measures ANOVA of aligned rank transformed data\n    statistic: F(1,37) = 13.08\n    p: 0.0009\n    n: 20 apoE3-KI and 19 apoE4-KI mice, aged 13-19 months\n  - about: hidden day 1\n    test: post hoc Mann-Whitney U test\n    statistic: U = 95\n    p: 0.033\n    corrected: Sidak\n  - about: hidden day 3\n    test: post hoc Mann-Whitney U test\n    statistic: U = 95\n    p: 0.034\n    corrected: Sidak\n  - about: hidden day 5\n    test: post hoc Mann-Whitney U test\n    statistic: U = 92\n    p: 0.026\n    corrected: Sidak\n  criterion: Daily mean escape latency (method C) of all Cohort 1 mice with MWM data; aligned rank\n    transform (ARTool, Wobbrock et al. 2011) and a two-way repeated-measures ANOVA on genotype and\n    day; post hoc Mann-Whitney U tests per day with Sidak adjustment over the 5 days. Reproduced\n    when the genotype effect has p < 0.05 with E4 slower and the post hoc tests are significant on\n    days 1, 3 and 5; partially reproduced when the genotype effect holds and one or two of those\n    days are not significant.\n- id: screen-88-comparisons\n  statement: In the screen cohort, 9 of 88 comparisons of 22 MWM metrics against 4 SWR properties\n    are significant at alpha 0.05 in apoE4-KI mice, more than chance by a binomial test.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 1; Table S2\n    (sheet ApoE4-KI)\n  quote: We began with a screen assessing the predictability of 22 behavioral metrics by 4 SWR properties\n    for a total of 88 comparisons, 9 of which were significant with a = 0.05; far more than would\n    be predicted by chance (p < 0.00032, binomial test\n  statistics:\n  - test: binomial test\n    p: 0.00032\n    p_relation: \"<\"\n    n: 88 comparisons\n  expected:\n  - quantity: significant comparisons of 88\n    value: 9\n    tolerance: 1\n  criterion: The 22 metrics of Table S2 (slopes days 1-2 to 1-5, latency days 1-5, nights 1-4,\n    and percent time, crossings and area under the curve for probes 1-3, by method C) against SWR\n    abundance and CA3, CA1-sr and DG SG power (methods A and B), Pearson, in the E4 mice of Cohort\n    1. Reproduced when the count is within tolerance and a one-sided binomial test of the count\n    against 0.05 gives p < 0.05. The same test reproduces the paper's p for Tables S3 and S4 (8 of\n    40 gives 0.00071, 5 of 30 gives 0.016), but 9 of 88 gives 0.032, not below 0.00032; the\n    printed bound is noted as a likely misprint and is not required. The count tolerance of 1 is\n    used because a count cannot be widened by 10%.\n- id: fig2b-swr-slope-days-1-2\n  statement: In aged apoE4-KI mice of the screen cohort, higher SWR abundance predicts a steeper\n    (more negative) slope of the escape latency curve over hidden days 1-2.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 2; Figure 2B\n  quote: In aged apoE4-KI mice, SWR abundance (events/second) predicted the slope of the escape latency\n    curve over the first 2 or first 3 hidden days (Figures 2B and S1B)\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,14) = 6.41\n    p: 0.024\n    n: 16 apoE4-KI mice\n  expected:\n  - quantity: Pearson R\n    value: -0.56\n    tolerance: 0.056\n  criterion: Rule for all correlations of the screen cohort, used by the claims that point here.\n    SWR property by method A or B, behavior metric by method C or D, Pearson correlation across the\n    E4 mice of Cohort 1 with both, two-sided. Reproduced when R has the paper's sign with p < 0.05\n    and R is within tolerance; partially reproduced when sign and p hold but R is outside\n    tolerance; not reproduced otherwise. R from Table S2.\n- id: figs1b-swr-slope-days-1-3\n  statement: In aged apoE4-KI mice of the screen cohort, SWR abundance predicts the slope of the\n    escape latency curve over hidden days 1-3.\n  source: Figure S1B; Table S2\n  quote: SWR abundance predicts slope of escape latency over hidden days 1–3 (F(1,14) = 10.91), n = 16\n    mice\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,14) = 10.91\n    p: 0.0052\n    n: 16 apoE4-KI mice\n  expected:\n  - quantity: Pearson R\n    value: -0.66\n    tolerance: 0.066\n  criterion: As fig2b-swr-slope-days-1-2, slope over days 1-3.\n- id: fig2c-swr-latency-day-3\n  statement: In aged apoE4-KI mice of the screen cohort, higher SWR abundance predicts lower escape\n    latency on hidden day 3.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 2; Figure 2C\n  quote: SWR abundance also predicted escape latency on hidden day 3 (Figure 2C), a measure of approach\n    efficacy\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,14) = 4.77\n    p: 0.046\n    n: 16 apoE4-KI mice\n  expected:\n  - quantity: Pearson R\n    value: -0.5\n    tolerance: 0.05\n  criterion: As fig2b-swr-slope-days-1-2, mean latency on hidden day 3.\n- id: fig2d-swr-overnight\n  statement: In aged apoE4-KI mice of the screen cohort, higher SWR abundance predicts more overnight\n    improvement (a more negative change in escape latency from day 1 trial 4 to day 2 trial 1).\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 2; Figure 2D\n  quote: SWR abundance predicted the extent of behavioral improvement over the first night (Figure 2D),\n    where high SWR abundance predicted improved performance overnight while lower SWR abundance predicted\n    worse performance\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,14) = 9.76\n    p: 0.0075\n    n: 16 apoE4-KI mice\n  expected:\n  - quantity: Pearson R\n    value: -0.64\n    tolerance: 0.064\n  criterion: As fig2b-swr-slope-days-1-2, overnight change by method C.\n- id: fig2e-learning-score\n  statement: In aged apoE4-KI mice of the screen cohort, z-scored SWR abundance accounts for 51% of\n    the variance of the MWM learning performance score.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 3; Figure 2E\n  quote: SWR abundance (also Z scored) accounted for 51% of the variance of the learning performance\n    score\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,14) = 14.3\n    p: 0.002\n    n: 16 apoE4-KI mice\n  expected:\n  - quantity: variance explained (R squared)\n    value: 0.51\n    tolerance: 0.051\n  - quantity: Pearson R (read from the panel)\n    value: 0.711\n    tolerance: 0.071\n  depends_on:\n  - fig2b-swr-slope-days-1-2\n  - figs1b-swr-slope-days-1-3\n  - fig2c-swr-latency-day-3\n  - fig2d-swr-overnight\n  criterion: MWM learning score by method E under both z-score readings, against SWR abundance\n    z-scored over the same mice; Pearson. Reproduced when R is positive with p < 0.05 and R squared\n    is within tolerance under one reading. The p (0.002) is read from the panel.\n- id: screen-features-independent\n  statement: In aged apoE4-KI mice of the screen cohort, SWR abundance and SWR-associated CA3 SG power\n    are not correlated, and measures of early learning speed and of probe memory are not correlated.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 4\n  quote: SWR abundance and associated SG power in CA3 were not correlated, and, similarly, measures of\n    early learning speed and of probe memory were not correlated\n  criterion: A claim of absence; the paper names no test, and its correlations are Pearson at alpha\n    0.05 (Quantification and Statistical Analysis). Pearson between SWR abundance and CA3 SG power\n    across the 13 E4 mice of Cohort 1 with CA3 sites; and between the MWM learning score and the\n    MWM memory precision score (method E). Reproduced when neither has p < 0.05; not reproduced\n    when either does; R is reported. The 20 correlations between the four learning metrics and the\n    five probe metrics are shown as a variant.\n- id: fig2f-ca3-probe1-quadrant\n  statement: In aged apoE4-KI mice of the screen cohort, higher SWR-associated CA3 SG power predicts\n    more time in the target quadrant on probe 1.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 4; Figure 2F\n  quote: SWR-associated SG power in CA3 predicted the percent time spent exploring the quadrant that previously\n    contained the platform on probes 1 and 2 (Figures 2F and S1D\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,11) = 15.75\n    p: 0.0022\n    n: 13 apoE4-KI mice\n  expected:\n  - quantity: Pearson R\n    value: 0.77\n    tolerance: 0.077\n  criterion: As fig2b-swr-slope-days-1-2, CA3 SG power (method B) against percent time in target\n    quadrant, probe 1, in the 13 E4 mice with CA3 sites.\n- id: figs1d-ca3-probe2-quadrant\n  statement: In aged apoE4-KI mice of the screen cohort, CA3 SG power during SWRs predicts percent time\n    in the target quadrant on probe 2.\n  source: Figure S1D; Table S2\n  quote: CA3 SG power during SWRs predicts percent time spent in quadrant that previously contained the\n    platform on probe 2 (F(1,11) = 5.34), n = 13 mice\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,11) = 5.34\n    p: 0.041\n    n: 13 apoE4-KI mice\n  expected:\n  - quantity: Pearson R\n    value: 0.57\n    tolerance: 0.057\n  criterion: As fig2f-ca3-probe1-quadrant, probe 2.\n- id: fig2g-ca3-probe1-crossings\n  statement: In aged apoE4-KI mice of the screen cohort, CA3 SG power during SWRs predicts the number\n    of target crossings on probe 1.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 4; Figure 2G\n  quote: CA3 SG power during SWRs predicted the number of target crossings on probe 1 (Figure 2G)\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,11) = 17.3\n    p: 0.0016\n    n: 13 apoE4-KI mice\n  expected:\n  - quantity: Pearson R\n    value: 0.78\n    tolerance: 0.078\n  criterion: As fig2f-ca3-probe1-quadrant, target crossings on probe 1.\n- id: fig2h-ca3-probe1-auc\n  statement: In aged apoE4-KI mice of the screen cohort, higher CA3 SG power during SWRs predicts a\n    smaller area under the distance-to-platform curve in the first 5 s of probe 1.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 4; Figure 2H\n  quote: CA3 SG power during SWRs predicted this metric for probes 1 and 2 (Figures 2H and S1F\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,11) = 6.55\n    p: 0.027\n    n: 13 apoE4-KI mice\n  expected:\n  - quantity: Pearson R\n    value: -0.61\n    tolerance: 0.061\n  criterion: As fig2f-ca3-probe1-quadrant, area under the curve on probe 1 by method C.\n- id: figs1f-ca3-probe2-auc\n  statement: In aged apoE4-KI mice of the screen cohort, CA3 SG power during SWRs predicts the area\n    under the distance-to-platform curve in the first 5 s of probe 2.\n  source: Figure S1F; Table S2\n  quote: CA3 SG power during SWRs predicts area under the curve of the distance to the prior platform location\n    during the first 5 seconds of probe 2 (F(1,11) = 6.01), n = 13 mice\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,11) = 6.01\n    p: 0.032\n    n: 13 apoE4-KI mice\n  expected:\n  - quantity: Pearson R\n    value: -0.59\n    tolerance: 0.059\n  criterion: As fig2f-ca3-probe1-quadrant, area under the curve on probe 2.\n- id: fig2i-memory-precision-score\n  statement: In aged apoE4-KI mice of the screen cohort, z-scored CA3 SG power during SWRs accounts\n    for 77% of the variance in the MWM memory precision performance score.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 4; Figure 2I\n  quote: CA3 SG power during SWRs accounted for 77% of the variance in the memory precision score\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,11) = 27.3\n    p: 0.0003\n    n: 13 apoE4-KI mice\n  expected:\n  - quantity: Pearson R (read from the panel)\n    value: 0.844\n    tolerance: 0.084\n  - quantity: variance explained (R squared), as the text states\n    value: 0.77\n    tolerance: 0.077\n  depends_on:\n  - fig2f-ca3-probe1-quadrant\n  - figs1d-ca3-probe2-quadrant\n  - fig2g-ca3-probe1-crossings\n  - fig2h-ca3-probe1-auc\n  - figs1f-ca3-probe2-auc\n  criterion: MWM memory precision score by method E under both z-score readings against z-scored\n    CA3 SG power; Pearson. The printed R (0.844) and F (27.3, n = 13) both give R squared 0.71, not\n    77%. Reproduced when R is positive with p < 0.05 and R is within its tolerance under one\n    reading; the R squared is reported and compared with both 0.71 and 0.77.\n- id: rep-mwm-swr-slope-days-1-2\n  statement: In the replication cohort (apoE4-KI, recorded at 13-17 months, MWM at 14-18 months), SWR\n    abundance again predicts the slope of escape latency over hidden days 1-2.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 5; Figure 2K\n  quote: In this replication cohort, studied 2 years—thus several generations of mice—later, we found\n    that all relationships identified in the screen cohort remained significant (Figures 2J–2R and S1G–\n    S1I\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,9) = 7.51\n    p: 0.067\n    corrected: Holm-Sidak\n    n: 11 apoE4-KI mice\n  expected:\n  - quantity: Pearson R (read from the panel)\n    value: -0.675\n    tolerance: 0.068\n  criterion: Rule for all replication correlations, used by the claims that point here. As\n    fig2b-swr-slope-days-1-2, in the E4 mice of Cohort 2 recorded at 13-17 months, with the\n    behavior at 14-18 months (MWM) or 15-20 months (APA). The paper calls every replication\n    relationship significant, though some adjusted p exceed 0.05, so significance is read on the\n    unadjusted p. Reproduced when R has the paper's sign with unadjusted p < 0.05 and R within\n    tolerance; partially reproduced when sign and p hold and R is outside tolerance. The\n    Holm-Sidak adjusted p, in the family of method F, is reported against the printed value.\n- id: rep-mwm-swr-latency-day-3\n  statement: In the replication cohort, SWR abundance predicts escape latency on hidden day 3.\n  source: Figure 2L\n  quote: SWR abundance predicts (K) slope of escape latency over hidden days 1–2 (F(1,9) = 7.51, adjusted\n    p = 0.067), (L) average escape latency on hidden day 3 (F(1,9) = 5.45, adjusted p = 0.044)\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,9) = 5.45\n    p: 0.044\n    corrected: Holm-Sidak\n    n: 11 apoE4-KI mice\n  expected:\n  - quantity: Pearson R (read from the panel)\n    value: -0.614\n    tolerance: 0.061\n  criterion: As rep-mwm-swr-slope-days-1-2.\n- id: rep-mwm-swr-overnight\n  statement: In the replication cohort, SWR abundance predicts the overnight change in escape latency\n    between hidden days 1 and 2.\n  source: Figure 2M\n  quote: (M) change in escape latency between the last trial of hidden day 1 and the first trial of hidden\n    day 2 (F(1,9) = 6.66, adjusted p = 0.059); n = 11 mice\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,9) = 6.66\n    p: 0.059\n    corrected: Holm-Sidak\n    n: 11 apoE4-KI mice\n  expected:\n  - quantity: Pearson R implied by F(1,9) = 6.66\n    value: -0.652\n    tolerance: 0.065\n  criterion: As rep-mwm-swr-slope-days-1-2. The panel prints R = -0.425 with p = 0.030; F(1,9) =\n    6.66 and p = 0.030 imply R = -0.652, so the panel's R is taken as a misprint and the implied R\n    is expected.\n- id: rep-mwm-swr-slope-days-1-3\n  statement: In the replication cohort, SWR abundance predicts the slope of escape latency over hidden\n    days 1-3.\n  source: Figure S1G\n  quote: In a replication experiment in a separate cohort of animals, SWR abundance predicts slope of escape\n    latency over hidden days 1–3 (F(1,9) = 13.39, adjusted p = 0.021), n = 11 mice\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,9) = 13.39\n    p: 0.021\n    corrected: Holm-Sidak\n    n: 11 apoE4-KI mice\n  expected:\n  - quantity: Pearson R implied by F(1,9) = 13.39\n    value: -0.773\n    tolerance: 0.077\n  criterion: As rep-mwm-swr-slope-days-1-2. The panel prints R = -0.598 with p = 0.005; the F and\n    the adjusted p imply R = -0.773 (p = 0.005), so the implied R is expected.\n- id: fig2n-rep-learning-score\n  statement: In the replication cohort, the learning performance score predicted from SWR abundance by\n    the screen cohort's model captures 56% of the variance of the actual score.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 6; Figure 2N\n  quote: These predictions were remarkably accurate, capturing 56% of the variance in the actual learning\n    performance score and 79% of the variance in the actual memory precision performance score\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,9) = 11.4\n    p: 0.008\n    n: 11 apoE4-KI mice\n  expected:\n  - quantity: variance explained (R squared)\n    value: 0.56\n    tolerance: 0.056\n  depends_on:\n  - fig2e-learning-score\n  criterion: Method G with the MWM learning score (method E, both z-score readings, each cohort\n    z-scored within itself) and SWR abundance. Reproduced when the correlation of predicted and\n    actual scores is positive with p < 0.05 and R squared is within tolerance under one reading.\n    The p (0.008) is read from the panel. The out-of-sample F of fit_train_to_test.m is shown.\n- id: rep-mwm-ca3-probe1-quadrant\n  statement: In the replication cohort, CA3 SG power during SWRs predicts percent time in the target\n    quadrant on probe 1.\n  source: Figure 2O\n  quote: CA3 SG power during SWRs predicts (O) percent time spent in quadrant that previously contained\n    the platform (F(1,8) = 32.64, adjusted p = 0.002)\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,8) = 32.64\n    p: 0.002\n    corrected: Holm-Sidak\n    n: 10 apoE4-KI mice\n  expected:\n  - quantity: Pearson R (read from the panel)\n    value: 0.896\n    tolerance: 0.09\n  criterion: As rep-mwm-swr-slope-days-1-2, CA3 SG power in the 10 E4 mice with CA3 sites.\n- id: rep-mwm-ca3-probe1-crossings\n  statement: In the replication cohort, CA3 SG power during SWRs predicts target crossings on probe 1.\n  source: Figure 2P\n  quote: (P) number of times crossing the previous platform location (F(1,8) = 13.48, adjusted p = 0.025\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,8) = 13.48\n    p: 0.025\n    corrected: Holm-Sidak\n    n: 10 apoE4-KI mice\n  expected:\n  - quantity: Pearson R (read from the panel)\n    value: 0.792\n    tolerance: 0.079\n  criterion: As rep-mwm-ca3-probe1-quadrant.\n- id: rep-mwm-ca3-probe1-auc\n  statement: In the replication cohort, CA3 SG power during SWRs predicts the area under the distance\n    curve in the first 5 s of probe 1.\n  source: Figure 2Q\n  quote: (Q) area under the curve of the distance to the prior platform location during the first 5 s of\n    probe (F(1,8) = 7.61, adjusted p = 0.049); n = 10 mice\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,8) = 7.61\n    p: 0.049\n    corrected: Holm-Sidak\n    n: 10 apoE4-KI mice\n  expected:\n  - quantity: Pearson R (read from the panel)\n    value: -0.698\n    tolerance: 0.07\n  criterion: As rep-mwm-ca3-probe1-quadrant.\n- id: rep-mwm-ca3-probe2\n  statement: In the replication cohort, CA3 SG power during SWRs predicts percent time in the target\n    quadrant and the area under the distance curve on probe 2.\n  source: Figure S1H and S1I\n  quote: CA3 SG power during SWRs predicts (H) percent time spent in quadrant that previously contained\n    the platform (F(1,8) = 6.02, adjusted p = 0.04) and (I) area under the curve of the distance to the\n    prior platform location during the first 5 seconds of probe 2 (F(1,8) = 8.27, adjusted p = 0.06\n  statistics:\n  - about: percent time in target quadrant, probe 2\n    test: Pearson correlation\n    statistic: F(1,8) = 6.02\n    p: 0.04\n    corrected: Holm-Sidak\n    n: 10 apoE4-KI mice\n  - about: area under the curve, probe 2\n    test: Pearson correlation\n    statistic: F(1,8) = 8.27\n    p: 0.06\n    corrected: Holm-Sidak\n    n: 10 apoE4-KI mice\n  expected:\n  - quantity: Pearson R, percent time in target quadrant, probe 2 (read from the panel)\n    value: 0.655\n    tolerance: 0.066\n  - quantity: Pearson R, area under the curve, probe 2 (read from the panel)\n    value: -0.713\n    tolerance: 0.071\n  criterion: As rep-mwm-ca3-probe1-quadrant, for each metric; reproduced when both hold, partially\n    reproduced when one does.\n- id: fig2r-rep-memory-score\n  statement: In the replication cohort, the memory precision score predicted from CA3 SG power by the\n    screen cohort's model captures 79% of the variance of the actual score.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 6; Figure 2R\n  quote: capturing 56% of the variance in the actual learning performance score and 79% of the variance\n    in the actual memory precision performance score (Figures 2N and 2R)\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,8) = 30.1\n    p: 0.0006\n    n: 10 apoE4-KI mice\n  expected:\n  - quantity: variance explained (R squared)\n    value: 0.79\n    tolerance: 0.079\n  depends_on:\n  - fig2i-memory-precision-score\n  criterion: As fig2n-rep-learning-score, with the MWM memory precision score and CA3 SG power. The\n    p (0.0006) is read from the panel.\n- id: rep-all-replicated\n  statement: All the predictive relationships found in the screen cohort remain significant in the\n    replication cohort, more than chance would give.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 5\n  quote: we found that all relationships identified in the screen cohort remained significant (Figures\n    2J–2R and S1G–S1I), far more than would be predicted by chance (p = 0, binomial test\n  statistics:\n  - test: binomial test\n    p: 0\n    n: 9 relationships\n  depends_on:\n  - rep-mwm-swr-slope-days-1-2\n  - rep-mwm-swr-latency-day-3\n  - rep-mwm-swr-overnight\n  - rep-mwm-swr-slope-days-1-3\n  - rep-mwm-ca3-probe1-quadrant\n  - rep-mwm-ca3-probe1-crossings\n  - rep-mwm-ca3-probe1-auc\n  - rep-mwm-ca3-probe2\n  criterion: Reproduced when all 9 relationships reproduce (each with unadjusted p < 0.05 and the\n    paper's sign) and a one-sided binomial test of 9 of 9 against 0.05 gives p < 0.001; partially\n    reproduced when 7 or 8 do.\n- id: cohort-swr-differences\n  statement: The two cohorts differ in mean SWR abundance (0.12 against 0.20 Hz) and in mean SWR\n    baseline (16.2 against 11.5 uV), though the predictive relationships hold in both.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 5\n  quote: These predictive relationships were consistent across the two cohorts despite differences in\n    the mean values of SWR abundance (m = 0.12 Hz versus 0.20 Hz; unpaired t test, t(29) = 4.75, p <\n    0.0001) and in mean values of SWR baseline (m = 16.2 mV versus 11.5 mV; unpaired t test, t(25)\n    = 5.41, p < 0.0001\n  statistics:\n  - about: SWR abundance\n    test: unpaired t test\n    statistic: t(29) = 4.75\n    p: 0.0001\n    p_relation: \"<\"\n  - about: SWR baseline\n    test: unpaired t test\n    statistic: t(25) = 5.41\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n  - quantity: mean SWR abundance, first value\n    value: 0.12\n    tolerance: 0.012\n    unit: Hz\n  - quantity: mean SWR abundance, second value\n    value: 0.2\n    tolerance: 0.02\n    unit: Hz\n  - quantity: mean SWR baseline, first value\n    value: 16.2\n    tolerance: 1.62\n    unit: uV\n  - quantity: mean SWR baseline, second value\n    value: 11.5\n    tolerance: 1.15\n    unit: uV\n  criterion: The text does not say which cohort is which or which mice; t(29) fits the 16 screen\n    and 15 replication (13-17 months) E4 mice. The order is read as screen then replication (the\n    order of the text; the screen E4 mean is near 0.12 Hz in Figure 1E); the reverse is reported.\n    The baseline is the session mean of the smoothed ripple envelope (ag_extractripples.m, as in\n    Figure S4C), averaged over sessions; the 27 mice of t(25) are not identified, and readings are\n    (a) E4 mice of both cohorts with a baseline, (b) all mice of both cohorts in the comparison.\n    Reproduced when, under one reading, the means are within tolerance and both t tests give p <\n    0.0001; partially reproduced when the direction holds with p < 0.05. Units of the deposited\n    int16 LFP are the author's to establish.\n- id: robust-single-point\n  statement: None of the paper's significant correlations is driven by a single data point; each stays\n    significant when any one point is removed.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 7; Quantification\n    and Statistical Analysis\n  quote: All significant correlations reported in this paper were confirmed to be not driven by a single\n    data point by measuring the significance of each relationship after removing each data point\n  criterion: As loocv.m, for every correlation claim reproduced here, the Pearson p after removing\n    each mouse in turn. Reproduced when every leave-one-out p is below 0.05 for every reproduced\n    correlation; partially reproduced when at most one removal per correlation raises p above\n    0.05; the number of failing removals is reported.\n- id: robust-detection-parameters\n  statement: In aged apoE4-KI mice of the screen cohort, the predictive relationships hold whether SWRs\n    are detected at 150-250 or 125-250 Hz and at a 3 or 5 SD threshold.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 7; Table S2\n    (sheet ApoE4-KI SWR Freq. and Thresh.)\n  quote: All relationships remained significant regardless of the frequency band (150–250 Hz versus 125–250\n    Hz) or threshold (3 SD versus 5 SD) used for SWR detection (Table S2\n  criterion: The 4 SWR abundance and 5 CA3 SG relationships of Table S2's third sheet, each with\n    ripple band 150-250 or 125-250 Hz (agripplefilter.mat, agripplefilter3.mat) and threshold 3 or\n    5 SD (method A), 36 correlations, Pearson. Reproduced when all 36 have the sign of Table S2 with\n    p < 0.05; partially reproduced when at least 32 do.\n- id: age-no-correlation\n  statement: Age within the cohort does not significantly correlate with SWR properties or MWM\n    performance.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 7\n  quote: as age within this cohort did not significantly correlated with SWR properties or MWM performance\n  criterion: A claim of absence, Pearson at alpha 0.05 (the paper's test for correlations). \"This\n    cohort\" is open; readings (a) the screen cohort, whose age range is 12-18 months, (b) the\n    replication cohort at 13-17 months. In the E4 mice, age at recording (task metadata) against\n    SWR abundance and CA3 SG power, and against the MWM metrics that enter the learning and memory\n    precision scores. Reproduced under a reading when none has p < 0.05; not reproduced when any\n    does; R and p are reported for both readings.\n- id: figs2-nonspatial-no-difference\n  statement: In the replication cohort there are no genotype differences in open field, elevated plus\n    maze, hot plate or visible-platform MWM performance.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 7; Figure S2\n  quote: there were no genotype differences in anxiety or exploratory drive as measured by open field and\n    elevated plus maze tests, in pain response as measured by a hot plate test, or in visual acuity as\n    measured by MWM trials with the platform marked (Figure S2\n  statistics:\n  - about: percent time in centre of open field\n    test: unpaired t test\n    statistic: t(25) = 1.19\n    p: 0.24\n  - about: open field movements, total\n    test: unpaired t test\n    statistic: t(25) = 0.54\n    p: 0.6\n  - about: percent time in open arm\n    test: unpaired t test\n    statistic: t(25) = 0.84\n    p: 0.41\n  - about: elevated plus maze distance, open arms\n    test: Mann-Whitney\n    statistic: U = 72.5\n    p: 0.41\n  - about: hot plate latency\n    test: Mann-Whitney\n    statistic: U = 66\n    p: 0.54\n    n: 12 apoE3-KI and 13 apoE4-KI mice\n  - about: visible trial escape latency\n    test: unpaired t test\n    statistic: t(25) = 1.26\n    p: 0.22\n    n: 12 apoE3-KI and 15 apoE4-KI mice\n  criterion: A claim of absence, on the tests of the Figure S2 legend, from the Behavior Excel file\n    (Cohort 2) - unpaired t tests for open field time in centre, fine, ambulatory and total\n    movements, open arm time, closed arm and total distance and visible-trial latency, and\n    Mann-Whitney for open arm distance and hot plate latency. Reproduced when none of the 10 tests\n    has p < 0.05; not reproduced when any does; each difference is reported.\n- id: nonspatial-not-correlated\n  statement: None of the non-spatial behaviors correlates significantly with spatial task performance or\n    with SWR properties.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 7\n  quote: Moreover, none of these non-spatial behaviors significantly correlated with spatial task performance\n    or with SWR properties at a = 0.05\n  depends_on:\n  - figs2-nonspatial-no-difference\n  criterion: A claim of absence at alpha 0.05 with Pearson correlations (the paper's test), in the E4\n    mice of Cohort 2. The spatial measures are not named; the reading is the four performance\n    scores (MWM and APA learning and memory precision, method E), and SWR abundance and CA3 SG power\n    at 13-17 months, against the 10 non-spatial measures of Figure S2. Reproduced when none has p <\n    0.05; not reproduced otherwise; the number significant is reported against the number expected\n    by chance.\n- id: ca1-dg-not-predictive\n  statement: SWR-associated SG power in CA1 stratum radiatum and in the dentate gyrus does not\n    consistently and significantly predict memory performance in apoE4-KI mice.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 8; Table S2\n  quote: SWR-associated SG power in CA1 and in DG did not consistently and significantly predict memory\n    performance (Table S2\n  criterion: A claim of absence on the paper's test, Pearson at alpha 0.05, for the 22 MWM metrics\n    of Table S2 against CA1-sr and DG SG power (method B) in the E4 mice of Cohort 1 (n = 16).\n    Table S2 shows none of the 44 significant. Reproduced when none has p < 0.05; not reproduced\n    when any does; R and p are reported.\n- id: e3-relationships\n  statement: In apoE3-KI mice, SWR abundance predicts escape latency on hidden day 2 in both cohorts,\n    while it does not predict day 3 latency, whose relationship holds in apoE4-KI mice; apoE3-KI\n    SWR abundance does not overlap that of apoE4-KI mice.\n  source: Results, SWR Deficits Predict Spatial Approach Task Impairments, paragraph 9; Figure S1J\n    to S1L; Table S2 (sheet ApoE3-KI)\n  quote: The one relationship that did replicate across both apoE3-KI cohorts was that SWR abundance predicted\n    escape latency on the second day (Figures S1K and S1L\n  statistics:\n  - about: screen cohort, day 2 latency\n    test: Pearson correlation\n    statistic: F(1,11) = 6.19\n    p: 0.03\n    n: 13 apoE3-KI mice\n  - about: replication cohort, day 2 latency\n    test: Pearson correlation\n    statistic: F(1,7) = 8.79\n    p: 0.021\n    n: 9 apoE3-KI mice\n  - about: screen cohort, day 3 latency, apoE3-KI\n    test: Pearson correlation\n    p: 0.78\n    n: 13 apoE3-KI mice\n  expected:\n  - quantity: Pearson R, screen apoE3-KI, day 2 latency\n    value: -0.6\n    tolerance: 0.06\n  - quantity: Pearson R, replication apoE3-KI, day 2 latency (read from the panel)\n    value: -0.746\n    tolerance: 0.075\n  criterion: As fig2b-swr-slope-days-1-2 and rep-mwm-swr-slope-days-1-2, in the E3 mice (13 at\n    12-18 months, 9 at 13-17 months), day 2 mean latency. The day 3 correlation in screen E3 mice\n    is a claim of absence, reproduced when p >= 0.05 (Table S2 R = -0.08, p = 0.78; the legend's\n    F(1,11) = 0.80 does not fit R = -0.08 and is not used). Non-overlap is the E3 minimum above the\n    E4 maximum of screen SWR abundance (Figure S1J); reported. Reproduced when both day 2\n    correlations hold and day 3 shows no correlation; partially reproduced when one day 2\n    correlation holds.\n- id: fig3b-apa-entrances-day1\n  statement: Aged apoE4-KI mice make more entrances into the APA shock zone than apoE3-KI mice on\n    training day 1.\n  source: Results, SWR Deficits Predict Spatial Avoidance Task Impairments, paragraph 1; Figure 3B\n  quote: apoE4-KI mice task acquisition was significantly impaired on day 1 - mice had greater number\n    of entrances into the shock zone (Figure 3B\n  statistics:\n  - test: unpaired t test with Sidak's multiple-comparison adjustment\n    statistic: t(23) = 3.43\n    p: 0.009\n    corrected: Sidak\n    n: 12 apoE3-KI and 13 apoE4-KI mice, aged 15-20 months\n  criterion: Entrances per training day (Behavior Excel, Cohort 2); unpaired t tests per day with\n    Sidak adjustment over the 4 days (Figure 3B legend). Reproduced when E4 is higher on day 1 with\n    adjusted p < 0.05; partially reproduced when only unadjusted p < 0.05.\n- id: figs3-apa-day1-and-probe\n  statement: On APA day 1 apoE4-KI mice travel less, spend less time opposite the shock zone and move\n    further from it per bout, and on the probe they receive more pseudoshocks per entrance than\n    apoE3-KI mice.\n  source: Results, SWR Deficits Predict Spatial Avoidance Task Impairments, paragraph 1; Figure S3A to\n    S3D\n  quote: traveled less distance (Figure S3A), spent less time in the quadrant opposite the shock zone (Figure\n    S3B), and moved further from the shock zone in bouts of movement (Figure S3C). Performance on the probe\n    trial, in which ... the shock was inactivated, was also impaired (Figure S3D\n  statistics:\n  - about: path length, day 1\n    test: unpaired t test\n    statistic: t(23) = 4.64\n    p: 0.0004\n  - about: percent time opposite, day 1\n    test: unpaired t test\n    statistic: t(23) = 2.27\n    p: 0.033\n  - about: distance per bout, day 1\n    test: Mann Whitney\n    statistic: U = 30\n    p: 0.008\n  - about: pseudoshocks per entrance, probe\n    test: unpaired t test\n    statistic: t(18) = 2.76\n    p: 0.013\n  criterion: The four metrics (method D; pseudoshocks per entrance from the Excel file, mice without\n    a probe entrance excluded) with the tests of the legend. Directions from the panels - E4 lower\n    path length and time opposite, higher distance per bout and pseudoshocks per entrance.\n    Reproduced when all four hold with p < 0.05; partially reproduced when two or three do.\n- id: apa-40-comparisons\n  statement: Of 40 comparisons of 5 APA metrics over 4 days against 2 SWR properties, 8 are significant\n    at alpha 0.05, more than chance, most of them on day 2.\n  source: Results, SWR Deficits Predict Spatial Avoidance Task Impairments, paragraph 2; Table S3\n  quote: In total, we compared 5 behavioral metrics over 4 days against 2 SWR properties for a total of\n    40 comparisons, 8 of which were significant with a = 0.05; far more than would be predicted by chance\n    (p < 0.00071, binomial test\n  statistics:\n  - test: binomial test\n    p: 0.00071\n    p_relation: \"<\"\n    n: 40 comparisons\n  expected:\n  - quantity: significant comparisons of 40\n    value: 8\n    tolerance: 1\n  criterion: Table S3's 40 Pearson correlations in E4 mice of Cohort 2, SWR abundance and CA3 SG\n    power at 13-17 months against the five APA metrics (method D) on days 1-4. Reproduced when the\n    count is within tolerance, a one-sided binomial test against 0.05 gives p < 0.05, and day 2 has\n    more significant comparisons than any other day. Tolerance of 1 as for screen-88-comparisons.\n- id: apa-day2-variance\n  statement: Variance across mice of shock zone entrances is higher on APA day 2 than day 1 (15.76\n    against 33.82).\n  source: Results, SWR Deficits Predict Spatial Avoidance Task Impairments, paragraph 2\n  quote: found that day 2 variances were higher (mean entrances day 1 s2 = 15.76 versus day 2 s2 = 33.82\n  expected:\n  - quantity: variance of entrances, day 1\n    value: 15.76\n    tolerance: 1.58\n  - quantity: variance of entrances, day 2\n    value: 33.82\n    tolerance: 3.38\n  criterion: Sample variance of entrances across mice. Which mice is open; readings (a) the 13 E4\n    mice (the analysis is of E4 variability), (b) the 10 E4 mice of the correlations, (c) all 25\n    mice. Reproduced when, under one reading, both values are within tolerance; partially\n    reproduced when day 2 variance is higher but the values are outside tolerance.\n- id: figs3fg-day2-predicts-later\n  statement: In apoE4-KI mice, entrances on APA day 2 predict entrances on days 3 and 4, and the top\n    50% of day 2 performers keep learning on days 3 and 4 while the bottom 50% do not.\n  source: Results, SWR Deficits Predict Spatial Avoidance Task Impairments, paragraph 2; Figure S3F and\n    S3G\n  quote: day 2 performance predicted day 3 and 4 performance, and apoE4-KI mice separated out into two\n    distinct performance populations on day 2 such that the top 50% of performers on day 2 continued to\n    learn on days 3 and 4 and that the bottom 50% did not\n  statistics:\n  - about: day 2 against day 3 entrances\n    test: Pearson correlation\n    statistic: F(1,11) = 49.27\n    p: 0.0001\n    p_relation: \"<\"\n    n: 13 apoE4-KI mice\n  - about: day 2 against day 4 entrances\n    test: Pearson correlation\n    statistic: F(1,11) = 16.32\n    p: 0.002\n    n: 13 apoE4-KI mice\n  - about: top against bottom half, day 1\n    test: unpaired t test with Sidak adjustment\n    statistic: t(44) = 1.66\n    p: 0.36\n  - about: top against bottom half, day 3\n    test: unpaired t test with Sidak adjustment\n    statistic: t(44) = 6.06\n    p: 0.0001\n    p_relation: \"<\"\n  - about: top against bottom half, day 4\n    test: unpaired t test with Sidak adjustment\n    statistic: t(44) = 5.28\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n  - quantity: Pearson R, day 2 against day 3 (read from the panel)\n    value: 0.904\n    tolerance: 0.09\n  - quantity: Pearson R, day 2 against day 4 (read from the panel)\n    value: 0.773\n    tolerance: 0.077\n  criterion: The 13 E4 mice of the APA (Cohort 2). Pearson of day 2 entrances against days 3 and 4.\n    Split by day 2 entrances into 7 top and 6 bottom mice; the tests on days 1, 3 and 4 with Sidak\n    adjustment over the 3 days. The df 44 is that of a pooled error over days; readings (a) unpaired\n    t tests per day (11 df), (b) post hoc tests of a two-way ANOVA of group and day (44 df, as the\n    printed df). Reproduced when both correlations are positive with p < 0.05, R within tolerance,\n    and the groups differ on days 3 and 4 (p < 0.05) but not on day 1, under one reading.\n- id: fig3c-swr-latency-first-entrance\n  statement: In the replication cohort, SWR abundance measured 2 months before APA predicts latency to\n    first shock zone entrance on day 2.\n  source: Results, SWR Deficits Predict Spatial Avoidance Task Impairments, paragraph 3; Figure 3C\n  quote: SWR abundance measured 2 months before task training predicted the latency to first entrance on\n    day 2\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,8) = 5.81\n    p: 0.043\n    n: 10 apoE4-KI mice\n  - test: Pearson correlation\n    statistic: F(1,8) = 5.81\n    p: 0.12\n    corrected: Holm-Sidak\n    n: 10 apoE4-KI mice\n  expected:\n  - quantity: Pearson R\n    value: 0.65\n    tolerance: 0.065\n  criterion: As rep-mwm-swr-slope-days-1-2, latency to first entrance on day 2; R from Table S3.\n- id: fig3de-swr-path-and-quadrant\n  statement: In the replication cohort, SWR abundance predicts path length and percent time in the\n    quadrant opposite the shock zone on APA day 2.\n  source: Results, SWR Deficits Predict Spatial Avoidance Task Impairments, paragraph 3; Figure 3D and\n    3E\n  quote: SWR abundance also predicted path length and percent time in the quadrant opposite the target on\n    day 2 (Figures 3D and 3E\n  statistics:\n  - about: path length\n    test: Pearson correlation\n    statistic: F(1,8) = 16.42\n    p: 0.018\n    corrected: Holm-Sidak\n    n: 10 apoE4-KI mice\n  - about: percent time opposite\n    test: Pearson correlation\n    statistic: F(1,8) = 7.33\n    p: 0.1\n    corrected: Holm-Sidak\n    n: 10 apoE4-KI mice\n  expected:\n  - quantity: Pearson R, path length\n    value: 0.82\n    tolerance: 0.082\n  - quantity: Pearson R, percent time opposite\n    value: 0.69\n    tolerance: 0.069\n  criterion: As rep-mwm-swr-slope-days-1-2, for each metric; R from Table S3. Reproduced when both\n    hold, partially when one does.\n- id: fig3f-apa-learning-score\n  statement: The APA learning performance score predicted from SWR abundance by the screen cohort's\n    model accounts for 75% of the variance in the actual score.\n  source: Results, SWR Deficits Predict Spatial Avoidance Task Impairments, paragraph 3; Figure 3F\n  quote: The relationship between the predicted and actual learning performance scores was very strong,\n    with the predicted score accounting for 75% of the variance in the actual score\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,8) = 23.7\n    p: 0.001\n    n: 10 apoE4-KI mice\n  expected:\n  - quantity: variance explained (R squared)\n    value: 0.75\n    tolerance: 0.075\n  depends_on:\n  - fig2e-learning-score\n  criterion: As fig2n-rep-learning-score, with the APA learning score. The metrics are open; the text\n    says the metrics of Figures 3D and 3E (path length and percent time opposite), the Methods add\n    latency to first entrance; both readings are run, each under both z-score readings. The p\n    (0.001) is read from the panel.\n- id: fig3g-ca3-entrances\n  statement: In the replication cohort, higher CA3 SG power during SWRs predicts fewer shock zone\n    entrances on APA day 2, and also on days 3 and 4.\n  source: Results, SWR Deficits Predict Spatial Avoidance Task Impairments, paragraph 4; Figure 3G;\n    Table S3\n  quote: This SWR property predicted the number of shock zone entrances—a metric that requires precise memory\n    of shock zone boundaries—on day 2 (Figure 3G) as well as on days 3 and 4\n  statistics:\n  - about: day 2\n    test: Pearson correlation\n    statistic: F(1,7) = 32.53\n    p: 0.003\n    corrected: Holm-Sidak\n    n: 9 apoE4-KI mice\n  - about: day 3\n    test: Pearson correlation\n    statistic: F 9.49\n    p: 0.02\n    n: 9 apoE4-KI mice\n  - about: day 4\n    test: Pearson correlation\n    statistic: F 7.48\n    p: 0.03\n    n: 9 apoE4-KI mice\n  expected:\n  - quantity: Pearson R, day 2\n    value: -0.91\n    tolerance: 0.091\n  - quantity: Pearson R, day 3\n    value: -0.76\n    tolerance: 0.076\n  - quantity: Pearson R, day 4\n    value: -0.72\n    tolerance: 0.072\n  criterion: As rep-mwm-swr-slope-days-1-2, CA3 SG power in the 9 E4 mice with CA3 sites, entrances\n    on days 2, 3 and 4; R from Table S3. Reproduced when all three hold; partially reproduced when\n    day 2 holds and one of days 3 and 4 does.\n- id: fig3h-ca3-distance-per-bout\n  statement: In the replication cohort, mice with lower CA3 SG power during SWRs move further from the\n    shock zone per movement bout on APA days 2 and 3.\n  source: Results, SWR Deficits Predict Spatial Avoidance Task Impairments, paragraph 4; Figure 3H and\n    S3H\n  quote: CA3 SG power during SWRs further predicted the distance mice traveled away from the shock zone\n    during bouts of movement on days 2 and 3 (Figures 3H and S3H\n  statistics:\n  - about: day 2\n    test: Pearson correlation\n    statistic: F(1,7) = 9.04\n    p: 0.077\n    corrected: Holm-Sidak\n    n: 9 apoE4-KI mice\n  - about: day 3\n    test: Pearson correlation\n    statistic: F(1,7) = 6.74\n    p: 0.036\n    n: 9 apoE4-KI mice\n  expected:\n  - quantity: Pearson R, day 2\n    value: -0.75\n    tolerance: 0.075\n  - quantity: Pearson R, day 3\n    value: -0.7\n    tolerance: 0.07\n  criterion: As fig3g-ca3-entrances, distance per bout (method D, pull_apa_metrics.py) on days 2\n    and 3; reproduced when both hold, partially when one does.\n- id: fig3i-apa-memory-score\n  statement: The APA memory precision score predicted from CA3 SG power by the screen cohort's model\n    accounts for 73% of the variance in the actual score.\n  source: Results, SWR Deficits Predict Spatial Avoidance Task Impairments, paragraph 5; Figure 3I\n  quote: Predicted score accounted for 73% of the variance in the actual score (Figure 3I\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,7) = 19.2\n    p: 0.003\n    n: 9 apoE4-KI mice\n  expected:\n  - quantity: variance explained (R squared)\n    value: 0.73\n    tolerance: 0.073\n  depends_on:\n  - fig2i-memory-precision-score\n  criterion: As fig2n-rep-learning-score, with the APA memory precision score (entrances day 2,\n    distance per bout days 2 and 3; text and Methods agree) and CA3 SG power. The p (0.003) is\n    read from the panel.\n- id: figs3ij-mwm-predicts-apa\n  statement: In apoE4-KI mice, MWM performance scores predict the corresponding APA scores, learning\n    against learning and memory precision against memory precision.\n  source: Results, SWR Deficits Predict Spatial Avoidance Task Impairments, paragraph 5; Figure S3I and\n    S3J\n  quote: We further noted that the performance scores of the MWM task predicted the performance scores\n    of the APA task (Figures S3I and S3J\n  statistics:\n  - about: learning scores\n    test: Pearson correlation\n    statistic: F(1,8) = 6.34\n    p: 0.035\n    n: 10 apoE4-KI mice\n  - about: memory precision scores\n    test: Pearson correlation\n    statistic: F(1,7) = 11.1\n    p: 0.012\n    n: 9 apoE4-KI mice\n  expected:\n  - quantity: Pearson R, learning scores (read from the panel)\n    value: 0.665\n    tolerance: 0.067\n  - quantity: Pearson R, memory precision scores (read from the panel)\n    value: 0.783\n    tolerance: 0.078\n  criterion: Scores by method E (both z-score readings; the APA learning score under both metric\n    readings of fig3f-apa-learning-score), MWM at 14-18 months against APA, in the E4 mice of the\n    correlations (10 and 9, as the legend gives). Reproduced when both are positive with p < 0.05\n    and R within tolerance under one reading; partially when one holds.\n- id: figs4ab-young-deficits\n  statement: In the replication cohort, apoE4-KI mice have lower SWR abundance and lower CA3 SG power\n    during SWRs than apoE3-KI mice already at 5-8 months and at every age tested.\n  source: Results, SWR Deficits at Younger Ages, paragraph 1; Figure S4A and S4B\n  quote: Young apoE4-KI mice already had reduced SWR abundance and associated SG power in CA3 when compared\n    to young apoE3-KI mice (Figures S4A and S4B\n  statistics:\n  - about: SWR abundance, genotype effect\n    test: two-way mixed-effects analysis of aligned rank transformed data\n    statistic: F(1,28) = 43.99\n    p: 0.0001\n    p_relation: \"<\"\n  - about: SWR abundance, 5-8 months\n    test: post-hoc Mann-Whitney U test\n    statistic: U = 43\n    p: 0.012\n    corrected: Sidak\n    n: 13 apoE3-KI and 17 apoE4-KI mice\n  - about: SWR abundance, 9-11 months\n    test: post-hoc Mann-Whitney U test\n    statistic: U = 26\n    p: 0.0012\n    corrected: Sidak\n  - about: SWR abundance, 13-17 months\n    test: post-hoc Mann-Whitney U test\n    statistic: U = 5\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: Sidak\n  - about: CA3 SG power, genotype effect\n    test: two-way mixed-effects analysis of aligned rank transformed data\n    statistic: F(1,26) = 12.86\n    p: 0.0014\n  - about: CA3 SG power, 5-8 months\n    test: post-hoc Mann-Whitney U test\n    statistic: U = 31\n    p: 0.0054\n    corrected: Sidak\n    n: 12 apoE3-KI and 16 apoE4-KI mice\n  - about: CA3 SG power, 9-11 months\n    test: post-hoc Mann-Whitney U test\n    statistic: U = 35\n    p: 0.024\n    corrected: Sidak\n  - about: CA3 SG power, 13-17 months\n    test: post-hoc Mann-Whitney U test\n    statistic: U = 31\n    p: 0.0456\n    corrected: Sidak\n  criterion: SWR abundance and CA3 SG power (methods A and B) per mouse and age in Cohort 2; aligned\n    rank transform and a two-way mixed-effects model of genotype and age (mice as random effects),\n    post hoc Mann-Whitney U tests per age with Sidak adjustment over the 3 ages. Reproduced when\n    both genotype effects have p < 0.05 with E4 lower and E4 is lower at 5-8 months for both\n    measures (adjusted p < 0.05); partially reproduced when the genotype effects hold but a 5-8\n    month comparison does not.\n- id: figs4ab-aging-increase\n  statement: Over aging, SWR abundance increases in apoE3-KI mice, and CA3 SG power during SWRs\n    increases in both genotypes.\n  source: Results, SWR Deficits at Younger Ages, paragraph 1; Figure S4A and S4B\n  quote: Interestingly, SWR abundance increased in apoE3-KI mice over aging ... Increases in CA3 SG power\n    during SWRs were seen in both groups over aging (Figure S4B\n  statistics:\n  - about: SWR abundance, apoE3-KI, 5-8 against 13-17 months\n    test: unpaired t test with Sidak adjustment\n    statistic: t(19) = 2.926\n    p: 0.028\n  - about: CA3 SG power, apoE3-KI\n    test: unpaired t test with Sidak adjustment\n    statistic: t(18) = 3.14\n    p: 0.017\n  - about: CA3 SG power, apoE4-KI\n    test: unpaired t test with Sidak adjustment\n    statistic: t(28) = 5.66\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: Per genotype, 5-8 against 13-17 months, unpaired t tests with Sidak adjustment (Figure\n    S4 legend, \"all comparisons unpaired t tests with Sidak adjustment\"; the family is not stated,\n    readings (a) the age pairs of one genotype and measure, 3 tests, (b) no more than the pairs\n    printed). Reproduced when all three increases have adjusted p < 0.05 under one reading;\n    partially when two do.\n- id: figs4cd-baseline-sd-swr-band\n  statement: Baseline in the SWR frequency band falls over aging in both genotypes, and its SD falls in\n    apoE4-KI but not apoE3-KI mice.\n  source: Results, SWR Deficits at Younger Ages, paragraph 1; Figure S4C and S4D\n  quote: although there was also a decrease in SWR baseline power (Figure S4C) that, along with a preserved\n    SD of SWR power (Figure S4D), could have contributed to this increase\n  statistics:\n  - about: baseline, apoE3-KI, 5-8 against 13-17 months\n    test: unpaired t test with Sidak adjustment\n    statistic: t(19) = 4.60\n    p: 0.0006\n  - about: baseline, apoE4-KI, 5-8 against 13-17 months\n    test: unpaired t test with Sidak adjustment\n    statistic: t(30) = 7.25\n    p: 0.0001\n    p_relation: \"<\"\n  - about: SD, apoE4-KI, 5-8 against 13-17 months\n    test: unpaired t test with Sidak adjustment\n    statistic: t(30) = 4.34\n    p: 0.0004\n  - about: SD, apoE3-KI, 5-8 against 13-17 months\n    test: unpaired t test with Sidak adjustment\n    statistic: t(19) = 0.25\n    p: 0.99\n  criterion: Baseline and SD are the mean and SD of the smoothed ripple envelope of each session on\n    the detection site (ag_extractripples.m; runcalcriprates.m figopt 2), averaged over sessions.\n    Tests as figs4ab-aging-increase. Reproduced when baseline falls (adjusted p < 0.05) in both\n    genotypes, SD falls in E4, and the E3 SD test gives p >= 0.05 (absence on the paper's test);\n    partially when two of the three decreases hold.\n- id: figs4ef-ca3-sg-baseline-stable\n  statement: Baseline and SD in the SG band in CA3 do not change over aging in either genotype.\n  source: Results, SWR Deficits at Younger Ages, paragraph 1; Figure S4E and S4F\n  quote: Increases in CA3 SG power during SWRs were seen in both groups over aging (Figure S4B) without\n    concomitant changes in baseline or SD (Figures S4E and S4F\n  statistics:\n  - about: baseline, apoE3-KI\n    test: unpaired t test with Sidak adjustment\n    statistic: t(18) = 0.18\n    p: 1.0\n  - about: baseline, apoE4-KI\n    test: Mann Whitney test with Sidak adjustment\n    statistic: U = 88\n    p: 0.7\n  - about: SD, apoE3-KI\n    test: unpaired t test with Sidak adjustment\n    statistic: t(18) = 0.50\n    p: 0.95\n  - about: SD, apoE4-KI\n    test: Mann Whitney U test with Sidak adjustment\n    statistic: U = 98\n    p: 0.93\n  criterion: A claim of absence on the legend's tests (t tests for E3, Mann-Whitney for E4, 5-8\n    against 13-17 months, Sidak adjusted). Baseline and SD are the mean and SD over windows of the\n    immobile-time spectrogram used for z-scoring (RTspecgram3.m meanPprobe and stdPprobe), averaged\n    over the SG bins and CA3 sites and over sessions (plotRTSstats.m figopt 4, with the bins of\n    method B). Reproduced when none of the four tests gives p < 0.05; not reproduced when any does.\n- id: figs4g-young-no-deficit\n  statement: Young (6-9 month) apoE4-KI mice show no MWM learning deficit.\n  source: Results, SWR Deficits at Younger Ages, paragraph 2; Figure S4G\n  quote: young apoE4-KI mice showed no detectable learning deficits (Figure S4G\n  criterion: A claim of absence. The legend names no test; the paper's test for the same curve in\n    aged mice is a two-way repeated-measures ANOVA of aligned rank transformed daily latencies\n    (Figure 1G legend), used here on the 13 E3 and 13 E4 mice of Cohort 2 at 6-9 months.\n    Reproduced when the genotype effect has p >= 0.05; not reproduced when p < 0.05; the effect is\n    reported.\n- id: table-s4-young-no-prediction\n  statement: SWR abundance and CA3 SG power at 5-8 months do not predict MWM behavior tested 1 month\n    later.\n  source: Results, SWR Deficits at Younger Ages, paragraph 2; Table S4 (6-9 mo MWM rows)\n  quote: SWR abundance and associated CA3 SG power measured at 5–8 months did not predict behavior tested\n    1 month later (Table S4\n  criterion: A claim of absence on the paper's test, Pearson at alpha 0.05, for the 9 MWM metrics of\n    Table S4 at 6-9 months against SWR abundance (n = 13) and CA3 SG power (n = 12) at 5-8 months\n    in E4 mice. Reproduced when none of the 18 has p < 0.05; not reproduced when any does.\n- id: fig4bc-swr-not-stable\n  statement: SWR abundance is not significantly correlated across ages within mice, in either genotype.\n  source: Results, SWR Deficits at Younger Ages, paragraph 3; Figure 4B and 4C\n  quote: We found that while SWR abundance was not significantly correlated across ages in either apoE3-KI\n    or apoE4-KI mice (Figures 4B and 4C\n  statistics:\n  - about: apoE3-KI, 9-11 against 5-8 months\n    test: Pearson correlation\n    statistic: F(1,10) = 2.12\n    p: 0.18\n    n: 12 apoE3-KI mice\n  - about: apoE3-KI, 9-11 against 13-17 months\n    test: Pearson correlation\n    statistic: F(1,7) = 0.82\n    p: 0.4\n    n: 9 apoE3-KI mice\n  - about: apoE4-KI, 9-11 against 5-8 months\n    test: Spearman correlation\n    p: 0.49\n    n: 17 apoE4-KI mice\n  - about: apoE4-KI, 9-11 against 13-17 months\n    test: Spearman correlation\n    p: 0.66\n    n: 15 apoE4-KI mice\n  criterion: A claim of absence on the paper's tests (Pearson for E3, Spearman for E4), SWR abundance\n    at 9-11 months against 5-8 and against 13-17 months, the same mice. Reproduced when none of the\n    four gives p < 0.05; not reproduced when any does. The p values are read from the panels.\n- id: fig4de-ca3-sg-stable\n  statement: CA3 SG power during SWRs at 9-11 months correlates with that at 5-8 and at 13-17 months in\n    the same mice, in both genotypes.\n  source: Results, SWR Deficits at Younger Ages, paragraph 3; Figure 4D and 4E\n  quote: CA3 SG power during SWRs was significantly correlated across ages in both genotypes (Figures 4D\n    and 4E\n  statistics:\n  - about: apoE3-KI, 5-8 months\n    test: Pearson correlation\n    statistic: F(1,9) = 13.54\n    p: 0.005\n    n: 11 apoE3-KI mice\n  - about: apoE3-KI, 13-17 months\n    test: Pearson correlation\n    statistic: F(1,7) = 48.52\n    p: 0.0002\n    n: 9 apoE3-KI mice\n  - about: apoE4-KI, 5-8 months\n    test: Pearson correlation\n    statistic: F(1,14) = 8.71\n    p: 0.011\n    n: 16 apoE4-KI mice\n  - about: apoE4-KI, 13-17 months\n    test: Pearson correlation\n    statistic: F(1,12) = 15.71\n    p: 0.002\n    n: 14 apoE4-KI mice\n  expected:\n  - quantity: Pearson R, apoE3-KI, 9-11 against 5-8 months (read from the panel)\n    value: 0.775\n    tolerance: 0.078\n  - quantity: Pearson R, apoE3-KI, 9-11 against 13-17 months (read from the panel)\n    value: 0.935\n    tolerance: 0.094\n  - quantity: Pearson R, apoE4-KI, 9-11 against 5-8 months (read from the panel)\n    value: 0.619\n    tolerance: 0.062\n  - quantity: Pearson R, apoE4-KI, 9-11 against 13-17 months (read from the panel)\n    value: 0.753\n    tolerance: 0.075\n  criterion: CA3 SG power (method B) per mouse and age, Pearson. Reproduced when all four are\n    positive with p < 0.05 and R within tolerance; partially when all four are positive with p <\n    0.05 but some R are outside tolerance, or when three hold.\n- id: ca3-sg-5-8-vs-13-17\n  statement: CA3 SG power at 5-8 months does not significantly predict CA3 SG power at 13-17 months,\n    indicating slow individual changes.\n  source: Results, SWR Deficits at Younger Ages, paragraph 3\n  quote: CA3 SG power at 5–8 months did not significantly predict CA3 SG power at 13–17 months, however\n    (e.g., for apoE3-KI mice, R = 0.2, F(1,12) = 0.5, p = 0.49\n  statistics:\n  - about: apoE3-KI, as printed\n    test: Pearson correlation\n    statistic: R = 0.2, F(1,12) = 0.5\n    p: 0.49\n  criterion: A claim of absence, Pearson at alpha 0.05. F(1,12) needs 14 mice, but only 9 E3 mice\n    have CA3 power at 13-17 months; readings (a) E3 mice (9), (b) E4 mice (14, which fits the df).\n    Judged on the E3 test as printed; reproduced when its p >= 0.05, not reproduced otherwise. The\n    E4 test is shown as a variant, with R and p of both.\n- id: fig4g-young-ca3-slope-days-1-2\n  statement: CA3 SG power during SWRs at 5-8 months predicts the slope of escape latency over hidden\n    days 1-2 on the MWM at 14-18 months in apoE4-KI mice.\n  source: Results, SWR Deficits at Younger Ages, paragraph 4; Figure 4G; Table S4\n  quote: CA3 SG power during SWRs measured at 5–8 months predicted escape latency on the third hidden day\n    and the slope of the escape latency curve for the first 2 or first 3 days on the MWM task at 14–18 months\n    (Figures 4G, 4H, S4H; Table S4\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,9) = 5.82\n    p: 0.039\n    n: 11 apoE4-KI mice\n  - test: Pearson correlation\n    statistic: F(1,9) = 5.82\n    p: 0.077\n    corrected: Holm-Sidak\n    n: 11 apoE4-KI mice\n  expected:\n  - quantity: Pearson R\n    value: -0.63\n    tolerance: 0.063\n  criterion: As rep-mwm-swr-slope-days-1-2, with CA3 SG power at 5-8 months and MWM at 14-18 months\n    in the 11 E4 mice with both; R from Table S4.\n- id: fig4h-young-ca3-latency-day-3\n  statement: CA3 SG power during SWRs at 5-8 months predicts escape latency on hidden day 3 at 14-18\n    months in apoE4-KI mice.\n  source: Figure 4H; Table S4\n  quote: (H) average escape latency on hidden day 3 (F(1,9) = 11.08, adjusted p = 0.035) on MWM task at\n    14–18 months\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,9) = 11.08\n    p: 0.035\n    corrected: Holm-Sidak\n    n: 11 apoE4-KI mice\n  expected:\n  - quantity: Pearson R\n    value: -0.74\n    tolerance: 0.074\n  criterion: As fig4g-young-ca3-slope-days-1-2.\n- id: figs4h-young-ca3-slope-days-1-3\n  statement: CA3 SG power during SWRs at 5-8 months predicts the slope of escape latency over hidden\n    days 1-3 at 14-18 months in apoE4-KI mice.\n  source: Figure S4H; Table S4\n  quote: CA3 SG power during SWRs measured at 5–8 months predicts slope of escape latency over hidden days\n    1–3 (F(1,9) = 10.89 on MWM task at 14–18 months\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,9) = 10.89\n    p: 0.027\n    corrected: Holm-Sidak\n    n: 11 apoE4-KI mice\n  expected:\n  - quantity: Pearson R\n    value: -0.74\n    tolerance: 0.074\n  criterion: As fig4g-young-ca3-slope-days-1-2.\n- id: fig4i-young-mwm-learning-score\n  statement: The MWM learning score at 14-18 months predicted from CA3 SG power at 5-8 months by the\n    screen cohort's model accounts for 50% of the variance in the actual score.\n  source: Results, SWR Deficits at Younger Ages, paragraph 5; Figure 4I\n  quote: the relationship derived from the screen cohort effectively predicted behavioral deficits, accounting\n    for 50% and 71% of the variance in the actual learning performance score with CA3 SG power during\n    SWRs measured 10–11 months previously\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,8) = 8.9\n    p: 0.015\n    n: 11 apoE4-KI mice\n  expected:\n  - quantity: variance explained (R squared)\n    value: 0.5\n    tolerance: 0.05\n  depends_on:\n  - fig2e-learning-score\n  criterion: As fig2n-rep-learning-score, with the MWM learning score at 14-18 months and CA3 SG\n    power at 5-8 months z-scored, through the model of Figure 2E. The printed F(1,8) does not fit n\n    = 11; F = 8.9 with 9 df gives R squared 0.50, as stated. The p (0.015) is read from the panel.\n- id: fig4jk-young-ca3-apa\n  statement: CA3 SG power during SWRs at 5-8 months predicts latency to first shock zone entrance and\n    path length on APA day 2 at 15-20 months in apoE4-KI mice.\n  source: Results, SWR Deficits at Younger Ages, paragraph 4; Figure 4J and 4K; Table S4\n  quote: CA3 SG power during SWRs also predicts (J) latency to first shock zone entrance (F(1,8) = 13.21,\n    adjusted p = 0.033) and (K) total path length (F(1,8) = 6.74, adjusted p = 0.12) on APA task at 15–20\n    months\n  statistics:\n  - about: latency to first entrance\n    test: Pearson correlation\n    statistic: F(1,8) = 13.21\n    p: 0.033\n    corrected: Holm-Sidak\n    n: 10 apoE4-KI mice\n  - about: path length\n    test: Pearson correlation\n    statistic: F(1,8) = 6.74\n    p: 0.12\n    corrected: Holm-Sidak\n    n: 10 apoE4-KI mice\n  expected:\n  - quantity: Pearson R, latency to first entrance\n    value: 0.79\n    tolerance: 0.079\n  - quantity: Pearson R, path length\n    value: 0.68\n    tolerance: 0.068\n  criterion: As fig4g-young-ca3-slope-days-1-2, APA day 2 in the 10 E4 mice; R from Table S4. The\n    Results text says \"the number of entries into the shock zone and path length\", but Figure 4J\n    and Table S4 give latency to first entrance (entrances R = -0.09, p = 0.80); the figure and\n    table are followed. Reproduced when both hold, partially when one does.\n- id: fig4l-young-apa-learning-score\n  statement: The APA learning score at 15-20 months predicted from CA3 SG power at 5-8 months by the\n    screen cohort's model accounts for 71% of the variance in the actual score.\n  source: Results, SWR Deficits at Younger Ages, paragraph 5; Figure 4L\n  quote: and all 3 APA metrics into an APA learning performance score (Figure 4L\n  statistics:\n  - test: Pearson correlation\n    statistic: F(1,8) = 19.7\n    p: 0.002\n    n: 10 apoE4-KI mice\n  expected:\n  - quantity: variance explained (R squared)\n    value: 0.71\n    tolerance: 0.071\n  depends_on:\n  - fig2e-learning-score\n  criterion: As fig4i-young-mwm-learning-score, with the APA learning score of the 3 day 2 metrics\n    (latency to first entrance, path length, percent time opposite; text and Methods agree here).\n    The p (0.002) is read from the panel.\n- id: table-s4-30-comparisons\n  statement: Of 30 comparisons of 15 later behavioral metrics against the two SWR properties at 5-8\n    months, 5 are significant at alpha 0.05, more than chance.\n  source: Results, SWR Deficits at Younger Ages, paragraph 4; Table S4\n  quote: in total, we compared 15 behavioral metrics against 2 SWR properties for a total of 30 comparisons,\n    5 of which were significant with a = 0.05; far more than would be predicted by chance (p < 0.016,\n    binomial test\n  statistics:\n  - test: binomial test\n    p: 0.016\n    p_relation: \"<\"\n    n: 30 comparisons\n  expected:\n  - quantity: significant comparisons of 30\n    value: 5\n    tolerance: 1\n  criterion: The 9 MWM metrics at 14-18 months and 6 APA metrics at 15-20 months of Table S4 against\n    SWR abundance and CA3 SG power at 5-8 months, Pearson, E4 mice. Reproduced when the count is\n    within tolerance and a one-sided binomial test against 0.05 gives p < 0.05. Tolerance of 1 as\n    for screen-88-comparisons.\n- id: figs4i-young-ca3-predicts-later-swr\n  statement: In apoE4-KI but not apoE3-KI mice, CA3 SG power during SWRs at 5-8 months predicts SWR\n    abundance at 13-17 months in the same mouse.\n  source: Results, SWR Deficits at Younger Ages, paragraph 6; Figure S4I\n  quote: CA3 SG power during SWRs in young apoE4-KI mice strongly predicted SWR abundance 8 months later\n    (Figure S4I). This was not true for young apoE3-KI mice\n  statistics:\n  - about: apoE4-KI\n    test: Pearson correlation\n    statistic: F(1,13) = 27.19\n    p: 0.0002\n    n: 15 apoE4-KI mice\n  - about: apoE3-KI\n    test: Pearson correlation\n    statistic: F(1,7) = 2.52\n    p: 0.16\n    n: 9 apoE3-KI mice\n  expected:\n  - quantity: Pearson R, apoE4-KI (read from the panel)\n    value: 0.823\n    tolerance: 0.082\n  criterion: CA3 SG power (method B) at 5-8 months against SWR abundance (method A) at 13-17 months,\n    Pearson, per genotype. Reproduced when the E4 correlation is positive with p < 0.05 and R within\n    tolerance and the E3 correlation has p >= 0.05 (absence on the paper's test); partially\n    reproduced when the E4 part holds and the E3 correlation is significant.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/jones-2019.yaml",
 "old_string": "  quote: apoE4-KI mice task acquisition was significantly impaired on day 1 - mice had greater number\n    of entrances into the shock zone (Figure 3B",
 "new_string": "  quote: apoE4-KI mice task acquisition was significantly impaired on day 1 ... mice had greater number\n    of entrances into the shock zone (Figure 3B"
}
```

```
The file claims/jones-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/jones-2019.yaml paper/10.1016-j.celrep.2019.10.056.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i "rather" claims/jones-2019.yaml; grep -n "—" claims/jones-2019.yaml | grep -v "quote:" ; grep -nE "^\s+[^#].*[^\"]: .*: " claims/jones-2019.yaml | head; git status --short
```

```
1047:    of shock zone boundaries—on day 2 (Figure 3G) as well as on days 3 and 4
 M tools/build_site.py
 M tools/get_papers.sh
 M tools/paper_records.py
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
?? claims/jones-2019.yaml
?? scripts
?? tools/build_reuse_targets.py
```

**Agent**

I wrote `claims/jones-2019.yaml`. The quote checker passes it: 65 claims, 65 quotes, 110 statistical values, 0 problems. Nothing was committed.

**Text read:** the version of record, with its supplement (Figures S1 to S4, Tables S1, S3 and S4) and Table S2 from the xlsx. I opened the PDF only to read R and p values printed inside figure panels, and the directions in Figures S3 and S4. Those values are marked "read from the panel". I also read the paper's code, emilyasterjones/SWR-predictions at commit ca056a8. Nothing a claim needed was missing.

**Counts:** all 65 claims have quotes, so none needed an `inferred` note. 56 have statistics and every claim has a criterion. 12 are claims of absence, each judged on the paper's own test.

**Details the paper leaves open, and the readings named:**
- **Ripple threshold:** the Methods say above 5 SD for 15 ms. The code detects above 3 SD for 15 ms and keeps events peaking at 5 SD. The Methods are the main reading and the code is the variant.
- **Slow gamma (SG) power:**
  - The code triggers on all events above 3 SD; the Methods and Table S2 use the 5 SD events.
  - The code's frequency bins include 54.7 Hz; the Methods' 30 to 50 Hz does not.
  - The Methods average per session and then over sessions; the code pools all events.
- **Z-score population for the performance scores:** either the apoE4-KI mice in the correlation, or all mice of the cohort.
- **Metrics in the APA learning score (Fig 3F):** two metrics in the text, three in the Methods.
- **MUA baseline:** either the whole 400 ms before detection, or the bin from -400 to -300 ms.
- **Cohort comparison (0.12 vs 0.20 Hz, 16.2 vs 11.5 µV):** the text doesn't say which cohort is which, or which mice the baseline t(25) covers.
- **Day 1 vs day 2 variance in APA shock-zone entrances:** which mice are included.
- **"This cohort" in the age claim:** the screen or the replication cohort.
- **Fig S3G test:** the df of 44 suggests ANOVA post hoc tests, but separate t tests per day are also possible.
- **Holm-Sidak families:** these are not stated. I found the family that reproduces every printed adjusted p from the printed F values (one per SWR property's planned metrics) and fixed that in the file.
- **Significance in the replication cohort:** read on unadjusted p. The paper calls every replication significant, but several adjusted p are above 0.05.

**Inconsistencies in the paper, recorded in the criteria:**
- The 9-of-88 binomial test prints p < 0.00032, but the test that reproduces the other two binomial values gives 0.032.
- Fig 2I says 77% of variance, but its R and F both give 71%.
- The panel R values in Fig 2M and S1G don't fit their F and p, so I used the R implied by F.
- Fig 4I prints F(1,8) for n = 11.
- The Fig S1J legend gives F = 0.80 where Table S2 implies about 0.08.
- In the text "R = 0.2, F(1,12)" for apoE3-KI mice, F(1,12) needs 14 mice but only 9 have the measure.
- The Results say young CA3 SG power predicts "entries" into the shock zone, but Figure 4J and Table S4 show latency to first entrance; I followed the figure.

Untracked dotfiles such as `.bashrc` and `.mcp.json`, plus `scripts/`, have appeared in the repo root. I didn't create them and left them alone.

## End of run

37 turns, 9 minutes, $3.41 at API prices, result: success.
