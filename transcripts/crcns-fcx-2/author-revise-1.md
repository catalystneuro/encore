# crcns-fcx-2 · author-revise-1 · run 42540236683

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/crcns-fcx-2/verifier-1-report.md; ls entries/crcns-fcx-2-johnson-2018 entries/crcns-fcx-2-johnson-2018/*;
```

```
Mon Nov  9 00:33:46 UTC 2026
I checked the notebook and helper module against the claims file and the paper, and re-tested helper functions on synthetic data. None of the 21 claims is fully reproduced. Four are reproduced (the two behaviour/electrode counts pairs and the PLV peak), two are partially reproduced, and 15 are not reproduced. The biggest problem is that every PAC result depends on a unit selection that marks most pure-noise pairs as significant.

**A. Outcomes**

| claim | outcome | reason |
|---|---|---|
| behavior-proficient | reproduced | Cell 16, all 120 trials: lowest 0.792, highest 0.967, every subject between 0.711 and 1.0. |
| behavior-no-difficulty-difference | partially_reproduced | Accuracy shows no effect under either reading (numeric term F 0.16, p 0.70; F 0.44, p 0.51). Response time shows no effect only with the `summary_file.csv` values (F 2.41, p 0.13). With the per-trial tables it does differ (F 12.3, p 0.0015 all trials; F 11.5, p 0.002 kept trials), and the two sources disagree in 7 of 10 subjects (cell 13). |
| electrode-counts | reproduced | Cell 20: 36/116/102, and 9 and 7 subjects, all exact. |
| correct-trial-counts | reproduced | Cell 22: means 100.9, 32.9, 34.8, 33.2 and 10.2 are within tolerance; per-subject ranges equal the paper's exactly. |
| erp-no-condition-difference | not_reproduced | The criterion is no electrode below p 0.05. Cell 24 finds 1 of 254 electrodes with the subject-wide null and 13 with the per-electrode null. Both counts are at or below the expected false-positive count (25.4), so the data are consistent with no effect, but the rule as written fails. |
| power-theta-sustained | not_reproduced | Cell 26: theta is sustained in 0 of 10, 0 of 9 and 0 of 9 subjects (electrodes: 1/36, 1/116, 11/102). MTL alpha is desynchronised in 0 of 10 subjects. |
| power-condition-exclusions | not_reproduced | Cell 28: 12 electrodes (6 PFC, 5 OFC, 1 MTL) in 5 subjects with the subject-wide null, and 69 with the per-electrode
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md
```

```
625 docs/protocol.md
1:# Protocol for an attempt
40:## Reader
42:### 1. Get the paper
56:### 2. Read the paper's code
66:### 3. Write the claims file
151:### 4. Data from outside the paper's own recordings
159:### 5. Check
172:### 6. Answer questions
185:## Author
201:### 1. Establish what can be tested
328:### 2. Check the data against its description
343:### 3. Write the entry
411:### 4. Lock, check and run
422:### 5. Record the attempt
473:### 6. Hand over for verification
511:## Repeat attempts
553:## Local and remote datasets
576:## Verifier
580:### Round 1: without the author's conclusions
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts/ 2>/dev/null | grep fcx; ls; find . -path ./node_modules -prune -o -name "*crcns-fcx-2*" -print | head -30
```

```
crcns-fcx-1-watson-2016-01.yaml
crcns-fcx-2-johnson-2018-01.yaml
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 185,
 "limit": 440
}
```

```
185	## Author
186	
187	The workflow puts the paper under `paper/`, as for the reader. Read it to
188	understand the claims, their data and their figures. The claims file still
189	decides what is tested: do not change a claim's statement, expected values or
190	criterion. A method detail the claims file lacks is taken from the paper
191	(step 6).
192	
193	**Time.** An author run is stopped five hours after it starts, and whatever
194	is not recorded by then is lost. The prompt says when the run started and the
195	time by which to finish. Check the clock (`date -u`) between steps. When that
196	time comes, stop analysing and finish: record each claim not yet tested as
197	blocked, `too_large` where the computation is what stopped it, saying how far
198	it got, then write the attempt record and run the entry's checks. A record
199	with some claims blocked for time is worth more than a run that is cut off.
200	
201	### 1. Establish what can be tested
202	
203	Do this before any analysis.
204	
[... 420 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l attempts/crcns-fcx-2-johnson-2018-01.yaml entries/crcns-fcx-2-johnson-2018/* claims/crcns-fcx-2/* questions/crcns-fcx-2.yaml; ls transcripts/crcns-fcx-2 paper; ls executed 2>/dev/null
```

```
Exit code 2
   460 attempts/crcns-fcx-2-johnson-2018-01.yaml
    35 entries/crcns-fcx-2-johnson-2018/README.md
    21 entries/crcns-fcx-2-johnson-2018/entry.yaml
   959 entries/crcns-fcx-2-johnson-2018/fcx2.py
  1427 entries/crcns-fcx-2-johnson-2018/reproduce_johnson_2018.ipynb
     7 entries/crcns-fcx-2-johnson-2018/requirements.in
    74 entries/crcns-fcx-2-johnson-2018/requirements.lock.txt
   861 claims/crcns-fcx-2/10.1371-journal.pbio.2004274.yaml
    33 questions/crcns-fcx-2.yaml
  3877 total
paper:
10.1371-journal.pbio.2004274.txt
fcx-2.data-description.pdf
fcx-2.data-description.txt

transcripts/crcns-fcx-2:
answer-report.md
answer.md
author-answers-report.md
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/crcns-fcx-2-johnson-2018-01.yaml"
}
```

```
1	schema_version: 2
2	id: crcns-fcx-2-johnson-2018-01
3	dataset:
4	  archive: crcns
5	  id: fcx-2
6	  version: unversioned
7	  doi: 10.6080/K0VX0DQD
8	paper: doi:10.1371/journal.pbio.2004274
9	date: 2026-11-08
10	entry: crcns-fcx-2-johnson-2018
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-13
19	  runner:
20	    platform: GitHub Actions
[... 441 more lines not kept]
```

**Agent**

I've read the verifier's report and the attempt record. Next I'll look at the helper, the notebook and how long a full run takes, then plan which points I can address in the time available.

**Agent calls Bash**

```bash
cat transcripts/crcns-fcx-2/author-answers-report.md | head -60; grep -n -i "minute\|runtime\|took\|elapsed" transcripts/crcns-fcx-2/author-report.md transcripts/crcns-fcx-2/author-answers-report.md | head
```

```
The one answered question flipped behavior-no-difficulty-difference from not reproduced to reproduced. That result depends on which of the dataset's two response-time sources is used. The entry passes `check`, the full notebook ran clean in 31.6 minutes with no errors, and the handover package is built. Nothing is committed or pushed, and I did not verify my own work.

## The question

behavior-no-difficulty-difference: should the criterion include the reading where condition enters the models as one numeric term?

**What the answer changed.** The reader amended the claims file. The criterion now judges the claim on reading (c): condition as one numeric term, coded identity 1, spatial 2, temporal 3. That coding is stated as an assumption, because the paper does not give it. The reader's grounds are that the paper's printed F(1,28) fits only this model on 30 subject-condition values. Readings (a) and (b) are still reported but no longer decide the outcome.

**Outcome: reproduced, resting on assumptions (was: not reproduced).**
- **Accuracy:** no condition effect under (c). Over all trials F(1,28) = 0.16, p = 0.70; over kept trials F = 0.44, p = 0.51. The paper gives F < 0.10, p > 0.75, so the effect is absent here too, but our F is above the paper's bound.
- **Response time from `docs/summary_file.csv`:** F(1,28) = 2.41, p = 0.13, against the paper's F < 2.55, p > 0.12. This file's condition means (1659, 1335, 1475 ms) are the ones the paper prints.
- **The weak point:** the dataset's own trial tables give different response times in 7 of 10 subjects. With those, reading (c) finds an effect (F = 12.33, p = 0.0015 over all trials; 11.48, p = 0.0021 over kept trials), and the claim would be not reproduced. I judged on `summary_file.csv` because its means and SDs are the paper's, and recorded that choice as an assumption (`assumed: true`).
- **Readings not judged:**
  - Under (a) and (b), response time still differs by condition in both sources (`summary_file.csv`: 3-le
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py"
}
```

```
1	"""Loading and measures for CRCNS fcx-2 (Johnson et al. 2018, PLoS Biology 16, e2004274).
2	
3	The data set holds, per subject, a tar.gz with the filtered continuous data (data_primary.mat),
4	the preprocessed bipolar data (data_derived.mat, MATLAB 7.3, FieldTrip structures data_pre,
5	data_encmain and data_proc), a per-trial table (summary_file_trial.csv) and electrode
6	coordinates. The tar files are streamed from the public S3 bucket and read member by member in
7	memory; nothing is written to disk. Only the derived data of the analysed channels
8	(docs/summary_channel_analysis.csv) are kept.
9	
10	Where the parameters come from. "Code" is the analysis code deposited with the data
11	(analysis_scripts.tar.gz in the data set, scripts dated 2018-02-22 to 2018-04-03); "Methods" is
12	the paper's Materials and methods; M1 to M10 are the shared method details of the claims file.
13	
14	- Segment windows (M1): encoding and precue [0, 1.5] s of data_encmain, precue delay
15	  [0.6, 1.5] s of data_encmain, postcue delay [0.3, 1.2] s of data_proc, baseline [0.65, 0.85] s
16	  of data_pre. Code: power_compute.m, psi_compute.m, cspsi_compute.m ("cfgt.latency"). The
17	  precue delay is M1 reading (a), which the code settles.
18	- Filter bank (M2): the 24 band edges of power_compute.m (`BANDS`), the last band dropped for the
19	  512 Hz subjects s8 and s9 (code). Two-pass FIR filters designed as FieldTrip's default for
20	  `bpfilttype = 'fir'` (fir1 with a Hamming window, order 3 * fix(fs / low edge), capped at a
[... 940 more lines not kept]
```

**Agent calls Bash**

```bash
grep -o "s[0-9]*: analysed in [^\"]*" -r transcripts/crcns-fcx-2/ | head -30; ls executed 2>&1
```

```
Exit code 2
transcripts/crcns-fcx-2/author.md:s8: analysed in 88 s; erp 1, power 80, power_test 80, plv 82, psi 88, pac 88
transcripts/crcns-fcx-2/author.md:s8: analysed in 18 s; erp 1, power 9, power_test 10, plv 12, psi 17, pac 18
transcripts/crcns-fcx-2/author.md:s2: analysed in 116 s; erp 6, power 54, power_test 56, plv 73, psi 114, pac 116
transcripts/crcns-fcx-2/author.md:s8: analysed in 17 s; erp 1, power 9, power_test 10, plv 12, psi 15, pac 17
transcripts/crcns-fcx-2/author.md:s8: analysed in 17 s; erp 1, power 9, power_test 10, plv 12, psi 15, pac 17
transcripts/crcns-fcx-2/author.md:s1: analysed in 90 s; erp 3, power 35, power_test 36, plv 46, psi 58, pac 90
transcripts/crcns-fcx-2/author.md:s2: analysed in 177 s; erp 6, power 46, power_test 50, plv 67, psi 91, pac 177
transcripts/crcns-fcx-2/author.md:s3: analysed in 33 s; erp 2, power 11, power_test 12, plv 15, psi 20, pac 33
transcripts/crcns-fcx-2/author.md:s4: analysed in 122 s; erp 5, power 35, power_test 37, plv 50, psi 67, pac 122
transcripts/crcns-fcx-2/author.md:s5: analysed in 206 s; erp 7, power 46, power_test 49, plv 65, psi 88, pac 206
transcripts/crcns-fcx-2/author.md:s6: analysed in 270 s; erp 11, power 83, power_test 87, plv 114, psi 158, pac 270
transcripts/crcns-fcx-2/author.md:s7: analysed in 124 s; erp 6, power 40, power_test 42, plv 55, psi 75, pac 124
transcripts/crcns-fcx-2/author.md:s9: analysed in 80 s; erp 3, power 22, power_test 25, plv 33, psi 44, pac 80
transcripts/crcns-fcx-2/author.md:s10: analysed in 669 s; erp 12, power 95, power_test 99, plv 147, psi 198, pac 669
ls: cannot access 'executed': No such file or directory
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-2-johnson-2018 && python -c "
import json
nb=json.load(open('reproduce_johnson_2018.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    print(f'=== [{i}] {c[\"cell_type\"]} tags={c[\"metadata\"].get(\"tags\")} len={len(s)}')
    print(s[:300])
"
```

```
=== [0] markdown tags=None len=3527
# Reproducing Johnson et al. (2018) from CRCNS fcx-2

**Paper.** Johnson EL, Adams JN, Solbakk A-K, Endestad T, Larsson PG, Ivanovic J, Meling TR, Lin JJ,
Knight RT (2018). Dynamic frontotemporal systems process space and time in working memory. *PLoS
Biology* 16, e2004274. [doi:10.1371/journal.pbio
=== [1] code tags=None len=424
import time
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy import stats

import fcx2

warnings.filterwarnings("ignore")
pd.set_option("display.width", 220)
[... 370 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && curl -s -o as.tgz https://crcnsarchive.s3-us-west-2.amazonaws.com/fcx-2/live/analysis_scripts.tar.gz && mkdir -p as && tar xzf as.tgz -C as && find as -type f | head -50
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/as/analysis_scripts && cat erp_compute.m subfunctions/psianalysis.m && grep -n "latency\|baseline\|toilim" *.m subfunctions/*.m
```

```
% Compute task-induced ERPs and compare conditions. Requires fieldtrip 
% toolbox.
%
% Key:
% subid = 's1' (required)
% elecs = {'LOF1','LOF2','LHH1'} (optional)
%
% E. L. Johnson, PhD
% Copyright (c) 2017
% UC Berkeley
% [removed: an e-mail address]

function [] = erp_compute(subid, elecs)
% erp_compute('s1', {'LOF1','LOF2','LHH1'});

% INPUT PATH TO DATA DIRECTORY
path = %%INSERT%%

dataDir = [path '/Johnson_PB_2018/data_indiv/'];
saveDir = [path '/Johnson_PB_2018/erp/'];
[... 205 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "column\|epoch\|pre-trial\|pretrial\|onset\|start screen\|fixation\|-1.5\|1500" paper/fcx-2.data-description.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 20,40p paper/fcx-2.data-description.txt; sed -n 100,160p paper/fcx-2.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "^- id:\|^  - id:\|id: " claims/crcns-fcx-2/*.yaml | head -40; grep -n "behavior-no-difficulty-difference" -A45 claims/crcns-fcx-2/*.yaml | head -70
```

```
121:  id: fcx-2
125:- id: behavior-proficient
144:- id: behavior-no-difficulty-difference
205:- id: electrode-counts
236:- id: correct-trial-counts
265:- id: erp-no-condition-difference
286:- id: power-theta-sustained
308:- id: power-condition-exclusions
340:- id: plv-theta-peak
359:- id: psi-theta-shift
395:- id: crossspectral-shift
469:- id: phase-directing-counts
513:- id: crossspectral-equal-strength
542:- id: theta-peak-bands
568:- id: pac-mtl-spatial
609:- id: pac-frontal-no-condition
631:- id: pac-mtl-pfc-spatial
678:- id: pac-mtl-pfc-temporal
696:- id: pac-pfc-mtl-no-condition
716:- id: pac-mtl-ofc-spatial
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,120p claims/crcns-fcx-2/*.yaml; sed -n 189,205p claims/crcns-fcx-2/*.yaml; sed -n 265,470p claims/crcns-fcx-2/*.yaml
```

```
# Claims for Johnson, Adams, Solbakk, Endestad, Larsson, Ivanovic, Meling, Lin & Knight (2018),
# PLoS Biology 16, e2004274, "Dynamic frontotemporal systems process space and time in working
# memory", doi:10.1371/journal.pbio.2004274, on CRCNS data set fcx-2 (doi:10.6080/K0VX0DQD).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record, open access, PMC5895055, as supplied under paper/ (Europe PMC
# full-text XML, flattened): Introduction, Results, Discussion, Materials and methods, the legends
# of Figures 1 to 8 and the captions of the supporting information. No PDF was supplied. The
# supporting information is S1 and S2 Fig (legends read) and S1 to S4 Table (DOCX files: group
# mixed-effects model outputs with degrees of freedom). Only the captions of the four tables were
# supplied; their contents were not read. Every claim below rests on a p-value the main text
# prints, so no claim needs the tables, but the full model outputs (degrees of freedom, F values
# of the PAC models) they hold were not available. Values shown only in figures (the percentages
# of Fig 4B, the grand means of Fig 8A, the per-subject PSI of Fig 3B) were not read.
#
# Code. The Data Availability statement says the "custom-built MATLAB codes" are deposited with
# the data on CRCNS (doi:10.6080/K0VX0DQD). The data descriptor says they are in the data set's
# analysis_scripts directory (one <metric>_compute script per analysis, with subfunctions, using
# FieldTrip). Being among the data set's files, they were not read in this run. Where a criterion
[... 323 more lines not kept]
```

**Agent calls Bash**

```bash
cd  curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?prefix=fcx-2/live/data_indiv/" | grep -o "<Key>[^<]*</Key><LastModified>[^<]*</LastModified><ETag>[^<]*</ETag><Size>[0-9]*" | sed 's/<[^>]*>/ /g'; nproc; free -g; date -u
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python -c "import h5py, statsmodels, scipy; print('ok')"; cat entries/crcns-fcx-2-johnson-2018/requirements.in entries/crcns-fcx-2-johnson-2018/entry.yaml
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import h5py, statsmodels, scipy; print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'h5py'
h5py
matplotlib
numpy
pandas
requests
scipy
statsmodels
schema_version: 1
name: crcns-fcx-2-johnson-2018
type: reproduction
title: Frontotemporal theta systems in working memory (Johnson et al. 2018)
description: Tests the findings of Johnson, Adams, Solbakk, Endestad, Larsson, Ivanovic, Meling, Lin and
  Knight (2018) on CRCNS data set fcx-2, which holds the preprocessed intracranial EEG of the 10
  subjects (254 bipolar MTL, PFC and OFC electrodes) in the visuospatial working memory task, their
  trial tables and the paper's analysis scripts. It checks behaviour, electrode and trial counts,
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p tools/entry.py | head -80; ls ~/.cache 2>/dev/null; ls -d .venv* entries/crcns-fcx-2-johnson-2018/.venv 2>/dev/null; which uv
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
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.13 dev && uv pip install -q -p dev/bin/python -r entries/crcns-fcx-2-johnson-2018/requirements.lock.txt && dev/bin/python -c "import h5py; print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/crcns-fcx-2-johnson-2018 && cat > $TMPDIR/load.py <<'EOF'
import sys, pickle, time, os
sys.path.insert(0, '.')
import fcx2
chtab = fcx2.read_channel_table()
for sid in sys.argv[1:]:
    t = time.time()
    ch = chtab[chtab.subject == sid].reset_index(drop=True)
    sub = fcx2.load_subject(sid, ch.label.tolist())
    pickle.dump((sub, ch), open(os.path.join(os.environ['TMPDIR'], f'{sid}.pkl'), 'wb'))
    print(sid, time.time() - t, {k: v['x'].shape for k, v in sub['seg'].items()})
EOF
$TMPDIR/dev/bin/python $TMPDIR/load.py s3 s8
```

```
s3 15.29069709777832 {'pre': (115, 7, 4501), 'encmain': (115, 7, 4498), 'proc': (115, 7, 4501)}
s8 8.731775283813477 {'pre': (90, 9, 2305), 'encmain': (90, 9, 2304), 'proc': (90, 9, 2305)}
```

**Agent calls Bash**

```bash
$TMPDIR/dev/bin/python -c "
import pickle, os, numpy as np
for sid in ['s3','s8']:
    sub, ch = pickle.load(open(os.environ['TMPDIR']+f'/{sid}.pkl','rb'))
    t = sub['trials']; fs = sub['seg']['encmain']['fs']
    print(sid, fs, {k:(v['time'][0], v['time'][-1]) for k,v in sub['seg'].items()})
    for j in (900,1150):
        m = t.jitter==j
        print(' jitter', j, 'H-G', np.unique(np.round((t.enc_start-t.pre_start)[m]/fs,3))[:5], 'I-H', np.unique(np.round((t.post_start-t.enc_start)[m]/fs,3))[:5])
    ti = sub['seg']['encmain']['trialinfo']; si = {k: v['sampleinfo'][:,0] for k,v in sub['seg'].items()}
    T = t.set_index('trial').loc[ti[:,0].astype(int)]
    print(' pre-G', np.unique((si['pre']-T.pre_start.values))[:4]/fs, 'enc-H', np.unique(si['encmain']-T.enc_start.values)[:4]/fs, 'proc-I', np.unique(si['proc']-T.post_start.values)[:4]/fs)
    print(' enc - pre sampleinfo', np.unique(si['encmain']-si['pre'])[:6]/fs, 'proc-enc', np.unique(si['proc']-si['encmain'])[:6]/fs)
"
```

```
s3 1000.0 {'pre': (np.float64(-1.5), np.float64(3.0)), 'encmain': (np.float64(-1.5), np.float64(2.997)), 'proc': (np.float64(-1.5), np.float64(3.0))}
 jitter 900 H-G [1.906 1.907] I-H [2.3   2.301]
 jitter 1150 H-G [1.906 1.907] I-H [2.551 2.552]
 pre-G [0.104 0.105] enc-H [0.] proc-I [-0.3]
 enc - pre sampleinfo [1.801 1.802] proc-enc [2.    2.001 2.251 2.252]
s8 512.0 {'pre': (np.float64(-1.5), np.float64(3.0)), 'encmain': (np.float64(-1.5), np.float64(2.998046875)), 'proc': (np.float64(-1.5), np.float64(3.0))}
 jitter 900 H-G [1.869 1.879 1.887 1.889 1.891] I-H [2.299]
 jitter 1150 H-G [1.869 1.871 1.879 1.887 1.889] I-H [2.549]
 pre-G [0.09960938] enc-H [0.] proc-I [-0.30078125]
 enc - pre sampleinfo [1.76953125 1.77148438 1.77929688 1.78710938 1.7890625  1.79101562] proc-enc [1.99804688 2.24804688]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/jit.py <<'EOF'
import pickle, os, sys, numpy as np
sys.path.insert(0, '.')
import fcx2
from scipy import stats
for sid in sys.argv[1:]:
    sub, ch = pickle.load(open(os.environ['TMPDIR']+f'/{sid}.pkl','rb'))
    for seg in ('encmain','pre','proc'):
        d = sub['seg'][seg]; fs = d['fs']; x = d['x']; ti = d['trialinfo']
        a = fcx2._filter_chunks(x, fs, np.arange(x.shape[-1]), np.array([[70.0,150.0]]), 'abs')[:,:,0]
        e = fcx2.lowpass_erp(x, fs, np.arange(x.shape[-1]))
        edges = np.arange(-1.5, 3.0001, 0.05); idx = np.digitize(d['time'], edges)-1
        def binz(v): return np.stack([v[..., idx==j].mean(-1) for j in range(len(edges)-1)], -1)
        A = binz(np.log(a)); E = binz(e)
        j9 = ti[:,4]==900
        tA = stats.ttest_ind(A[j9], A[~j9]).statistic   # ch, bins
        tE = stats.ttest_ind(E[j9], E[~j9]).statistic
        # also deviation from pre-segment mean (event response) in hg
        print(sid, seg, 'n', j9.sum(), (~j9).sum())
        for name, t in (('hg', tA), ('erp', tE)):
            m = np.abs(t).max(0)
            print(f'  {name} max|t| over ch by 250ms:', ' '.join(f'{edges[k]:+.2f}:{m[k:k+5].max():.1f}' for k in range(0, len(m), 5)))
EOF
$TMPDIR/dev/bin/python $TMPDIR/jit.py s3 s8
```

```
s3 encmain n 58 57
  hg max|t| over ch by 250ms: -1.50:2.4 -1.25:2.1 -1.00:2.9 -0.75:1.7 -0.50:2.2 -0.25:2.9 +0.00:2.2 +0.25:2.5 +0.50:2.8 +0.75:2.1 +1.00:2.0 +1.25:2.8 +1.50:2.4 +1.75:2.3 +2.00:2.5 +2.25:2.0 +2.50:2.8 +2.75:3.8
  erp max|t| over ch by 250ms: -1.50:2.5 -1.25:2.2 -1.00:2.1 -0.75:1.8 -0.50:1.6 -0.25:2.0 +0.00:1.9 +0.25:2.0 +0.50:2.9 +0.75:2.1 +1.00:2.3 +1.25:2.3 +1.50:2.7 +1.75:2.5 +2.00:2.5 +2.25:2.4 +2.50:2.5 +2.75:3.0
s3 pre n 58 57
  hg max|t| over ch by 250ms: -1.50:2.1 -1.25:2.1 -1.00:2.3 -0.75:2.8 -0.50:2.2 -0.25:2.5 +0.00:1.9 +0.25:2.4 +0.50:2.2 +0.75:3.0 +1.00:2.4 +1.25:2.2 +1.50:2.9 +1.75:2.2 +2.00:2.5 +2.25:2.0 +2.50:2.8 +2.75:2.3
  erp max|t| over ch by 250ms: -1.50:2.3 -1.25:2.5 -1.00:3.9 -0.75:2.1 -0.50:2.1 -0.25:1.7 +0.00:2.2 +0.25:2.5 +0.50:2.3 +0.75:2.1 +1.00:1.8 +1.25:1.6 +1.50:2.0 +1.75:1.8 +2.00:2.0 +2.25:2.9 +2.50:2.1 +2.75:2.4
s3 proc n 58 57
  hg max|t| over ch by 250ms: -1.50:2.6 -1.25:2.6 -1.00:1.8 -0.75:2.1 -0.50:2.6 -0.25:2.3 +0.00:2.3 +0.25:3.1 +0.50:2.1 +0.75:2.9 +1.00:3.5 +1.25:2.8 +1.50:2.3 +1.75:2.5 +2.00:2.8 +2.25:2.4 +2.50:2.1 +2.75:2.6
  erp max|t| over ch by 250ms: -1.50:2.1 -1.25:2.1 -1.00:2.5 -0.75:2.6 -0.50:2.4 -0.25:2.5 +0.00:2.2 +0.25:1.7 +0.50:1.9 +0.75:1.9 +1.00:2.8 +1.25:3.0 +1.50:2.8 +1.75:1.6 +2.00:2.4 +2.25:2.0 +2.50:1.8 +2.75:2.2
s8 encmain n 46 44
  hg max|t| over ch by 250ms: -1.50:2.8 -1.25:1.7 -1.00:2.9 -0.75:2.9 -0.50:2.8 -0.25:2.6 +0.00:2.5 +0.25:3.5 +0.50:2.1 +0.75:2.8 +1.00:3.2 +1.25:3.3 +1.50:2.6 +1.75:2.3 +2.00:2.1 +2.25:2.4 +2.50:2.5 +2.75:2.9
  erp max|t| over ch by 250ms: -1.50:1.9 -1.25:2.5 -1.00:2.9 -0.75:2.5 -0.50:2.9 -0.25:2.1 +0.00:2.2 +0.25:3.9 +0.50:3.5 +0.75:3.1 +1.00:2.3 +1.25:2.4 +1.50:2.1 +1.75:3.5 +2.00:2.4 +2.25:2.8 +2.50:4.5 +2.75:2.9
s8 pre n 46 44
  hg max|t| over ch by 250ms: -1.50:2.3 -1.25:1.9 -1.00:2.6 -0.75:2.7 -0.50:2.2 -0.25:2.2 +0.00:3.2 +0.25:3.3 +0.50:2.0 +0.75:2.5 +1.00:3.5 +1.25:3.4 +1.50:2.9 +1.75:2.5 +2.00:3.4 +2.25:2.2 +2.50:2.4 +2.75:2.4
  erp max|t| over ch b
[... 3 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py",
 "old_string": "    out[\"hg\"] = hg\n    out[\"evoked_edges\"]",
 "new_string": "    out[\"hg\"] = hg\n    # per electrode: t of the 900 against the 1150 ms trials in each 50 ms bin, for log high-gamma\n    # amplitude and the 30 Hz low-passed signal. The test cue comes 250 ms later after the long\n    # delay, so an electrode that responds to it parts the two groups from the cue's onset on:\n    # at 0 s of encmain under the trial table's placement, at 1.5 s under the code's.\n    jt = {}\n    for k in (\"pre\", \"encmain\", \"proc\"):\n        d = seg[k]\n        x = d[\"x\"]\n        ln = np.log(_filter_chunks(x, d[\"fs\"], np.arange(x.shape[-1]), np.array([[70.0, 150.0]]), \"abs\")[:, :, 0])\n        lp = lowpass_erp(x, d[\"fs\"], np.arange(x.shape[-1]))\n        edges = np.arange(-1.5, 3.0001, 0.05)\n        idx = np.digitize(d[\"time\"], edges) - 1\n        j9 = d[\"trialinfo\"][:, 4] == 900\n        for name, v in ((\"hg\", ln), (\"erp\", lp)):\n            b = np.stack([v[..., idx == j].mean(axis=-1) for j in range(len(edges) - 1)], axis=-1)\n            jt[(k, name)] = stats.ttest_ind(b[j9], b[~j9], axis=0).statistic.astype(np.float32)\n            if name == \"hg\":\n                # trial-mean log amplitude per electrode and bin, minus its segment mean\n                m = b.mean(axis=0)\n                jt[(k, \"hg_mean\")] = (m - m.mean(axis=-1, keepdims=True)).astype(np.float32)\n        del ln, lp\n    out[\"jitter_t\"] = jt\n    out[\"evoked_edges\"]"
}
```

```
The file entries/crcns-fcx-2-johnson-2018/fcx2.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py",
 "old_string": "WIN = {\"enc\": (\"encmain\", 0.0, 1.5), \"pre\": (\"encmain\", 0.6, 1.5), \"post\": (\"proc\", 0.3, 1.2),\n       \"base\": (\"pre\", 0.65, 0.85)}",
 "new_string": "WIN = {\"enc\": (\"encmain\", 0.0, 1.5), \"pre\": (\"encmain\", 0.6, 1.5), \"post\": (\"proc\", 0.3, 1.2),\n       \"base\": (\"pre\", 0.65, 0.85)}\n# The same windows placed by the trial table and the descriptor: the first sample of each\n# segment (time -1.5 s) is the table's epoch start (encmain at column H, first stimulus onset;\n# proc 0.3 s before column I, test cue offset; pre about 0.1 s after column G, 1 s before the\n# start screen), so every window lies 1.5 s earlier than the code takes it.\nSHIFT_DESC = -1.5\nWIN_DESC = {k: (s, t0 + SHIFT_DESC, t1 + SHIFT_DESC) for k, (s, t0, t1) in WIN.items()}"
}
```

```
The file entries/crcns-fcx-2-johnson-2018/fcx2.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py",
 "old_string": "- Segment windows (M1): encoding and precue [0, 1.5] s of data_encmain, precue delay\n  [0.6, 1.5] s of data_encmain, postcue delay [0.3, 1.2] s of data_proc, baseline [0.65, 0.85] s\n  of data_pre. Code: power_compute.m, psi_compute.m, cspsi_compute.m (\"cfgt.latency\"). The\n  precue delay is M1 reading (a), which the code settles.",
 "new_string": "- Segment windows (M1): encoding and precue [0, 1.5] s of data_encmain, precue delay\n  [0.6, 1.5] s of data_encmain, postcue delay [0.3, 1.2] s of data_proc, baseline [0.65, 0.85] s\n  of data_pre. Code: power_compute.m, psi_compute.m, cspsi_compute.m (\"cfgt.latency\"). The\n  precue delay is M1 reading (a), which the code settles. The trial table and the descriptor\n  place every window 1.5 s earlier (`WIN_DESC`); ERPs, power and theta PSI are also computed\n  there, as a variant."
}
```

```
The file entries/crcns-fcx-2-johnson-2018/fcx2.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py",
 "old_string": "    # ---- ERPs (erp_compute.m): 30 Hz low-pass, baseline from the trial mean of [0.65, 0.85] s\n    _, bsel = segment(sub, \"base\")\n    _, esel = segment(sub, \"enc\")\n    _, psel = segment(sub, \"post\")\n    base = lowpass_erp(xs[\"pre\"], fs, bsel).mean(axis=(0, 2))\n    erp_enc = lowpass_erp(xs[\"enc\"], fs, esel) - base[None, :, None]\n    erp_post = lowpass_erp(xs[\"proc\"], fs, psel) - base[None, :, None]\n    rng = np.random.default_rng(seed_for(\"erp-no-condition-difference\", sid))\n    res[\"erp_enc\"] = cluster_test(erp_enc[:, :, None, :], tic[:, 2], \"t\", rng, nperm_cluster)\n    res[\"erp_post\"] = cluster_test(erp_post[:, :, None, :], tic[:, 3], \"F\", rng, nperm_cluster)\n    res[\"erp_mean\"] = {\"enc\": erp_enc.mean(axis=0), \"post\": erp_post.mean(axis=0)}\n    del erp_enc, erp_post\n    res[\"timing\"][\"erp\"] = time.time() - T0",
 "new_string": "    # ---- ERPs (erp_compute.m): 30 Hz low-pass, baseline from the trial mean of [0.65, 0.85] s\n    # (the code subtracts nanmean(pretrial.trial), the mean over trials of the per-trial baseline\n    # means). Variants: each trial's own baseline mean subtracted, and the windows of WIN_DESC.\n    _, bsel = segment(sub, \"base\")\n    _, esel = segment(sub, \"enc\")\n    _, psel = segment(sub, \"post\")\n    lp = {k: lowpass_erp(xs[k], fs, np.arange(xs[k].shape[-1])) for k in (\"pre\", \"enc\", \"proc\")}\n    for tag, win in ((\"\", WIN), (\"_desc\", WIN_DESC)):\n        sl = {k: window_index(sub[\"seg\"][s][\"time\"], t0, t1) for k, (s, t0, t1) in win.items()}\n        btr = lp[\"pre\"][..., sl[\"base\"]].mean(axis=-1)                     # (trials, ch)\n        for btag, base in ((\"\", btr.mean(axis=0)[None, :, None]), (\"_trial\", btr[:, :, None])):\n            if tag == \"_desc\" and btag:\n                continue\n            erp_enc = lp[\"enc\"][..., sl[\"enc\"]] - base\n            erp_post = lp[\"proc\"][..., sl[\"post\"]] - base\n            rng = np.random.default_rng(seed_for(f\"erp-no-condition-difference{tag}{btag}\", sid)\n                                        if tag or btag else seed_for(\"erp-no-condition-difference\", sid))\n            res[f\"erp_enc{tag}{btag}\"] = cluster_test(erp_enc[:, :, None, :], tic[:, 2], \"t\", rng, nperm_cluster)\n            res[f\"erp_post{tag}{btag}\"] = cluster_test(erp_post[:, :, None, :], tic[:, 3], \"F\", rng, nperm_cluster)\n            if not tag and not btag:\n                res[\"erp_mean\"] = {\"enc\": erp_enc.mean(axis=0), \"post\": erp_post.mean(axis=0)}\n            del erp_enc, erp_post\n    del lp\n    res[\"timing\"][\"erp\"] = time.time() - T0"
}
```

```
The file entries/crcns-fcx-2-johnson-2018/fcx2.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py",
 "old_string": "    out_kind: \"power\" (amplitude squared), \"abs\", \"angle\" or \"complex\". Returns float32 or\n    complex64 (trials, ch, nband, len(sel)).\n    \"\"\"\n    pad = Padder(x.shape[-1], fs)\n    dtype = np.complex64 if out_kind == \"complex\" else np.float32\n    out = np.empty(x.shape[:2] + (len(bands), len(sel)), dtype=dtype)\n    gains = [bandpass_gain(lo, hi, fs, pad.nfft, pad.npad) for lo, hi in bands]\n    for c0 in range(0, x.shape[1], chunk):\n        X = pad.fft(x[:, c0:c0 + chunk].astype(np.float64))\n        for k, g in enumerate(gains):\n            y = pad.back(X * g, analytic=True)[..., sel]\n            if out_kind == \"power\":\n                y = np.abs(y) ** 2\n            elif out_kind == \"abs\":\n                y = np.abs(y)\n            elif out_kind == \"angle\":\n                y = np.angle(y)\n            out[:, c0:c0 + chunk, k, :] = y\n    return out",
 "new_string": "    out_kind: \"power\" (amplitude squared), \"abs\", \"angle\" or \"complex\". Returns float32 or\n    complex64 (trials, ch, nband, len(sel)); with a list of index arrays for `sel`, a list of\n    such arrays from one filtering pass.\n    \"\"\"\n    sels = sel if isinstance(sel, list) else [sel]\n    pad = Padder(x.shape[-1], fs)\n    dtype = np.complex64 if out_kind == \"complex\" else np.float32\n    outs = [np.empty(x.shape[:2] + (len(bands), len(s)), dtype=dtype) for s in sels]\n    gains = [bandpass_gain(lo, hi, fs, pad.nfft, pad.npad) for lo, hi in bands]\n    for c0 in range(0, x.shape[1], chunk):\n        X = pad.fft(x[:, c0:c0 + chunk].astype(np.float64))\n        for k, g in enumerate(gains):\n            yall = pad.back(X * g, analytic=True)\n            for s, out in zip(sels, outs):\n                y = yall[..., s]\n                if out_kind == \"power\":\n                    y = np.abs(y) ** 2\n                elif out_kind == \"abs\":\n                    y = np.abs(y)\n                elif out_kind == \"angle\":\n                    y = np.angle(y)\n                out[:, c0:c0 + chunk, k, :] = y\n    return outs if isinstance(sel, list) else outs[0]"
}
```

```
The file entries/crcns-fcx-2-johnson-2018/fcx2.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py",
 "old_string": "    rng = np.random.default_rng(seed_for(\"power\", sid))\n    bpow = _filter_chunks(xs[\"pre\"], fs, bsel, bands, \"power\")\n    bmean, bsd = baseline_bootstrap(bpow, int(correct.sum()), rng)\n    del bpow\n    zs = {}\n    for name, x, sel in ((\"enc\", xs[\"enc\"], esel), (\"post\", xs[\"proc\"], psel)):\n        p = _filter_chunks(x, fs, sel, bands, \"power\")\n        z = (p - bmean[None, :, :, None]) / bsd[None, :, :, None]\n        del p\n        zs[name] = resample_20hz(z, fs).astype(np.float32)\n        if name == \"enc\":\n            res[\"enc_time_mean_z\"] = z.mean(axis=(0, 3))          # (ch, band), trials and time\n        del z\n    res[\"power_z_mean\"] = {k: v.mean(axis=0) for k, v in zs.items()}  # (ch, band, t20)\n    res[\"timing\"][\"power\"] = time.time() - T0\n    rng = np.random.default_rng(seed_for(\"power-condition-exclusions\", sid))\n    res[\"pow_enc\"] = cluster_test(zs[\"enc\"], tic[:, 2], \"t\", rng, nperm_cluster)\n    res[\"pow_post\"] = cluster_test(zs[\"post\"], tic[:, 3], \"F\", rng, nperm_cluster)\n    del zs",
 "new_string": "    # the windows of WIN_DESC come from the same filtering pass\n    _, bsel_d = segment(sub, \"base\", WIN_DESC)\n    _, esel_d = segment(sub, \"enc\", WIN_DESC)\n    _, psel_d = segment(sub, \"post\", WIN_DESC)\n    rng = np.random.default_rng(seed_for(\"power\", sid))\n    rng_d = np.random.default_rng(seed_for(\"power|desc\", sid))\n    bpow, bpow_d = _filter_chunks(xs[\"pre\"], fs, [bsel, bsel_d], bands, \"power\")\n    bmean, bsd = baseline_bootstrap(bpow, int(correct.sum()), rng)\n    bmean_d, bsd_d = baseline_bootstrap(bpow_d, int(correct.sum()), rng_d)\n    del bpow, bpow_d\n    zs, zs_d = {}, {}\n    for name, x, sel, sel_d in ((\"enc\", xs[\"enc\"], esel, esel_d), (\"post\", xs[\"proc\"], psel, psel_d)):\n        p, p_d = _filter_chunks(x, fs, [sel, sel_d], bands, \"power\")\n        z = (p - bmean[None, :, :, None]) / bsd[None, :, :, None]\n        del p\n        zs[name] = resample_20hz(z, fs).astype(np.float32)\n        if name == \"enc\":\n            res[\"enc_time_mean_z\"] = z.mean(axis=(0, 3))          # (ch, band), trials and time\n        del z\n        p_d -= bmean_d[None, :, :, None]\n        p_d /= bsd_d[None, :, :, None]\n        zs_d[name] = resample_20hz(p_d, fs).astype(np.float32)\n        del p_d\n    res[\"power_z_mean\"] = {k: v.mean(axis=0) for k, v in zs.items()}  # (ch, band, t20)\n    res[\"power_z_mean_desc\"] = {k: v.mean(axis=0) for k, v in zs_d.items()}\n    res[\"timing\"][\"power\"] = time.time() - T0\n    rng = np.random.default_rng(seed_for(\"power-condition-exclusions\", sid))\n    res[\"pow_enc\"] = cluster_test(zs[\"enc\"], tic[:, 2], \"t\", rng, nperm_cluster)\n    res[\"pow_post\"] = cluster_test(zs[\"post\"], tic[:, 3], \"F\", rng, nperm_cluster)\n    rng = np.random.default_rng(seed_for(\"power-condition-exclusions|desc\", sid))\n    res[\"pow_enc_desc\"] = cluster_test(zs_d[\"enc\"], tic[:, 2], \"t\", rng, nperm_cluster)\n    res[\"pow_post_desc\"] = cluster_test(zs_d[\"post\"], tic[:, 3], \"F\", rng, nperm_cluster)\n    del zs, zs_d"
}
```

```
The file entries/crcns-fcx-2-johnson-2018/fcx2.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py",
 "old_string": "def segment(sub, name):\n    segname, t0, t1 = WIN[name]",
 "new_string": "def segment(sub, name, win=WIN):\n    segname, t0, t1 = win[name]"
}
```

```
The file entries/crcns-fcx-2-johnson-2018/fcx2.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -n "PSI (M5) between MTL" -A40 fcx2.py | head -5; grep -n "def cross_spectra" fcx2.py
```

```
792:    # PSI (M5) between MTL and frontal electrodes, and cross-spectral PSI (M6)
793-    nab = n_amp_bands(fs)
794-    amp_bands = BANDS[AMP_BANDS[:nab]]
795-    psi, cs, keep_th = {}, {}, {}
796-    for w, (x, sel) in wins.items():
450:def cross_spectra(A, B):
```

**Agent**

Now the PSI section: cross-spectral PSI under sliding windows (B4), trial-shuffled calibration surrogates (B3), and theta PSI at the descriptor's windows (B1).

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py",
 "old_string": "    psi, cs, keep_th = {}, {}, {}\n    for w, (x, sel) in wins.items():\n        env = _filter_chunks(x, fs, sel, amp_bands, \"abs\")   # filtered on the full segment\n        for mode in (\"mtmfft\", \"sliding\"):\n            rng = np.random.default_rng(seed_for(f\"psi|{w}|{mode}\", sid))\n            th = theta_fourier(x[..., sel].astype(np.float64), fs, mode)          # (n, ch, 5, w)\n            S, PA, PB = cross_spectra(th, th)\n            raw, z = psi_z(S, PA[:, None, :], PB[None, :, :], rng)              # (ch, ch)\n            psi[(w, mode)] = {\"raw\": raw, \"z\": z}\n            if mode == \"mtmfft\":\n                code_raw = np.full(raw.shape, np.nan)\n                code_z = np.full(raw.shape, np.nan)\n                ij = [(a, b) for g in (\"MTL-PFC\", \"MTL-OFC\") for a, b in pairs[g]]\n                if ij:\n                    ia, ib = np.array(ij).T\n                    o, zc = psi_code(th[:, ia], th[:, ib], rng)\n                    code_raw[ia, ib], code_z[ia, ib] = o, zc\n                psi[(w, \"code\")] = {\"raw\": code_raw, \"z\": code_z}\n            if mode != \"mtmfft\":\n                continue\n            # cross-spectral: theta of each amplitude envelope (code's single window)\n            rng = np.random.default_rng(seed_for(f\"cspsi|{w}|{mode}\", sid))\n            ea = env\n            n, nch, nbb, T = ea.shape\n            the = theta_fourier(ea.reshape(n, nch * nbb, T).astype(np.float64), fs, mode)\n            the = the.reshape(n, nch, nbb, 5, the.shape[-1])\n            Sx = np.einsum(\"rafw,rbcgw->abcfg\", th, np.conj(the)) / (n * th.shape[-1])\n            PBx = (np.abs(the) ** 2).mean(axis=(0, 4))                          # (ch, nbb, 5)\n            rawx, zx = psi_z(Sx, PA[:, None, None, :], PBx[None, :, :, :], rng)  # (ch, ch, nbb)\n            cs[(w, mode)] = {\"raw\": rawx, \"z\": zx}\n            if mode == \"mtmfft\":\n                keep_th[w] = (th, the)\n        del env\n    res[\"psi\"], res[\"cspsi\"] = psi, cs\n    res[\"timing\"][\"psi\"] = time.time() - T0",
 "new_string": "    psi, cs, keep_th, cs_shuf, keep_shuf = {}, {}, {}, {}, {}\n    ij = [(a, b) for g in (\"MTL-PFC\", \"MTL-OFC\") for a, b in pairs[g]]\n    for w, (x, sel) in wins.items():\n        env = _filter_chunks(x, fs, sel, amp_bands, \"abs\")   # filtered on the full segment\n        for mode in (\"mtmfft\", \"sliding\"):\n            rng = np.random.default_rng(seed_for(f\"psi|{w}|{mode}\", sid))\n            th = theta_fourier(x[..., sel].astype(np.float64), fs, mode)          # (n, ch, 5, w)\n            S, PA, PB = cross_spectra(th, th)\n            raw, z = psi_z(S, PA[:, None, :], PB[None, :, :], rng)              # (ch, ch)\n            psi[(w, mode)] = {\"raw\": raw, \"z\": z}\n            if mode == \"mtmfft\":\n                psi[(w, \"code\")] = _psi_code_pairs(th, ij, raw.shape, rng)\n            # cross-spectral: theta of each amplitude envelope\n            rng = np.random.default_rng(seed_for(f\"cspsi|{w}|{mode}\", sid))\n            n, nch, nbb, T = env.shape\n            the = theta_fourier(env.reshape(n, nch * nbb, T).astype(np.float64), fs, mode)\n            the = the.reshape(n, nch, nbb, 5, the.shape[-1])\n            Sx = cross_spectra_x(th, the)\n            PBx = (np.abs(the) ** 2).mean(axis=(0, 4))                          # (ch, nbb, 5)\n            rawx, zx = psi_z(Sx, PA[:, None, None, :], PBx[None, :, :, :], rng)  # (ch, ch, nbb)\n            cs[(w, mode)] = {\"raw\": rawx, \"z\": zx}\n            if mode == \"mtmfft\":\n                keep_th[w] = (th, the)\n            if w == \"post\":\n                # calibration: the second signal's trials shuffled against the first's, which\n                # removes any trial-by-trial coupling; z should then fall above 1.96 in about\n                # 2.5% of pairs\n                rng = np.random.default_rng(seed_for(f\"psi-shuffle|{mode}\", sid))\n                perm = rng.permutation(n)\n                S0, _, PB0 = cross_spectra(th, th[perm])\n                psi[(w, mode, \"shuf\")] = dict(zip((\"raw\", \"z\"), psi_z(S0, PA[:, None, :], PB0[None, :, :], rng)))\n                if mode == \"mtmfft\":\n                    psi[(w, \"code\", \"shuf\")] = _psi_code_pairs(th, ij, raw.shape, rng, perm)\n                the_p = the[perm]\n                cs_shuf[mode] = psi_z(cross_spectra_x(th, the_p), PA[:, None, None, :],\n                                      PBx[None, :, :, :], rng)[1]\n                if mode == \"mtmfft\":\n                    keep_shuf = (th, the_p)\n                del the_p\n            del the\n        del env\n    # theta PSI with the windows of WIN_DESC (the trial table's placement)\n    _, pre_sel_d = segment(sub, \"pre\", WIN_DESC)\n    _, psel_d = segment(sub, \"post\", WIN_DESC)\n    for w, (x, sel) in {\"pre\": (xe[\"enc\"], pre_sel_d), \"post\": (xe[\"proc\"], psel_d)}.items():\n        for mode in (\"mtmfft\", \"sliding\"):\n            rng = np.random.default_rng(seed_for(f\"psi|{w}|{mode}|desc\", sid))\n            th = theta_fourier(x[..., sel].astype(np.float64), fs, mode)\n            S, PA, PB = cross_spectra(th, th)\n            raw, z = psi_z(S, PA[:, None, :], PB[None, :, :], rng)\n            psi[(w, mode, \"desc\")] = {\"raw\": raw, \"z\": z}\n            if mode == \"mtmfft\":\n                psi[(w, \"code\", \"desc\")] = _psi_code_pairs(th, ij, raw.shape, rng)\n    res[\"psi\"], res[\"cspsi\"] = psi, cs\n    res[\"timing\"][\"psi\"] = time.time() - T0"
}
```

```
The file entries/crcns-fcx-2-johnson-2018/fcx2.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py",
 "old_string": "def psi_z(S, PA, PB, rng, nperm=1000):",
 "new_string": "def cross_spectra_x(th, the):\n    \"\"\"Trial- and window-averaged cross-spectra of theta (n, a, 5, w) with envelope theta\n    (n, b, c, 5, w). Returns (a, b, c, 5, 5), as cross_spectra, one matrix product per\n    frequency pair.\"\"\"\n    n, na, nf, nw = th.shape\n    nb, nc = the.shape[1:3]\n    A2 = th.transpose(2, 1, 0, 3).reshape(nf, na, n * nw)\n    B2 = np.conj(the).transpose(3, 0, 4, 1, 2).reshape(nf, n * nw, nb * nc)\n    S = np.empty((na, nb * nc, nf, nf), dtype=complex)\n    for f in range(nf):\n        for g in range(nf):\n            S[:, :, f, g] = A2[f] @ B2[g]\n    return S.reshape(na, nb, nc, nf, nf) / (n * nw)\n\n\ndef psi_z(S, PA, PB, rng, nperm=1000):"
}
```

```
The file entries/crcns-fcx-2-johnson-2018/fcx2.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py",
 "old_string": "    return obs, (obs - null.mean(axis=-1)) / null.std(axis=-1, ddof=1)\n\n\n# ---------------------------------------------------------------- PAC",
 "new_string": "    return obs, (obs - null.mean(axis=-1)) / null.std(axis=-1, ddof=1)\n\n\ndef _psi_code_pairs(th, ij, shape, rng, perm=None):\n    \"\"\"psi_code for the electrode pairs `ij` of theta coefficients th (n, ch, 5, 1), as\n    (ch, ch) arrays of raw and z (NaN off the pairs). `perm` shuffles the second signal's trials.\"\"\"\n    out = {\"raw\": np.full(shape, np.nan), \"z\": np.full(shape, np.nan)}\n    if ij:\n        ia, ib = np.array(ij).T\n        B = th[:, ib] if perm is None else th[perm][:, ib]\n        out[\"raw\"][ia, ib], out[\"z\"][ia, ib] = psi_code(th[:, ia], B, rng)\n    return out\n\n\n# ---------------------------------------------------------------- PAC"
}
```

```
The file entries/crcns-fcx-2-johnson-2018/fcx2.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py",
 "old_string": "        u[\"zf_post_mtmfft\"] = cs[(\"post\", \"mtmfft\")][\"z\"][u[\"ph\"], u[\"amp\"], :16].copy()\n        for w, (th, the) in keep_th.items():\n            rng = np.random.default_rng(seed_for(f\"cspsi-code|{w}|{u['ph']}|{u['amp']}\", sid))\n            nbb = the.shape[2]\n            A = np.repeat(th[:, [u[\"ph\"]]], nbb, axis=1)\n            o, zc = psi_code(A, the[:, u[\"amp\"]], rng)\n            u[f\"z_{w}_code\"], u[f\"raw_{w}_code\"] = float(zc.mean()), float(o.mean())\n            if w == \"post\":\n                u[\"zf_post_code\"] = zc[:16].copy()",
 "new_string": "        u[\"zf_post_mtmfft\"] = cs[(\"post\", \"mtmfft\")][\"z\"][u[\"ph\"], u[\"amp\"], :16].copy()\n        for mode, zsh in cs_shuf.items():\n            u[f\"z_post_{mode}_shuf\"] = float(zsh[u[\"ph\"], u[\"amp\"], :].mean())\n        for w, (th, the) in list(keep_th.items()) + [(\"post_shuf\", keep_shuf)]:\n            rng = np.random.default_rng(seed_for(f\"cspsi-code|{w}|{u['ph']}|{u['amp']}\", sid))\n            nbb = the.shape[2]\n            A = np.repeat(th[:, [u[\"ph\"]]], nbb, axis=1)\n            o, zc = psi_code(A, the[:, u[\"amp\"]], rng)\n            u[f\"z_{w}_code\"], u[f\"raw_{w}_code\"] = float(zc.mean()), float(o.mean())\n            if w == \"post\":\n                u[\"zf_post_code\"] = zc[:16].copy()\n        u[\"z_post_code_shuf\"] = u.pop(\"z_post_shuf_code\")\n        u.pop(\"raw_post_shuf_code\")"
}
```

```
The file entries/crcns-fcx-2-johnson-2018/fcx2.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py",
 "old_string": "    res[\"excluded\"] = excl\n    keep = ~excl",
 "new_string": "    res[\"excluded\"] = excl\n    res[\"excluded_desc\"] = (np.minimum(res[\"pow_enc_desc\"].p_subject, res[\"pow_post_desc\"].p_subject) < 0.05).to_numpy()\n    keep = ~excl"
}
```

```
The file entries/crcns-fcx-2-johnson-2018/fcx2.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py",
 "old_string": "    pdir = sorted({i for u in units if u[\"z_post_code\"] > 1.96 for i in (u[\"ph\"], u[\"amp\"])})\n    if pdir:\n        pkb = res[\"enc_time_mean_z\"][pdir][:, PEAK_BANDS].mean(axis=0)\n        res[\"peak_curve_dir_code\"], res[\"peak_band_dir_code\"] = pkb, int(PEAK_BANDS[np.argmax(pkb)])\n    else:\n        res[\"peak_curve_dir_code\"], res[\"peak_band_dir_code\"] = None, None",
 "new_string": "    for key in (\"code\", \"sliding\"):\n        pdir = sorted({i for u in units if u[f\"z_post_{key}\"] > 1.96 for i in (u[\"ph\"], u[\"amp\"])})\n        if pdir:\n            pkb = res[\"enc_time_mean_z\"][pdir][:, PEAK_BANDS].mean(axis=0)\n            res[f\"peak_curve_dir_{key}\"], res[f\"peak_band_dir_{key}\"] = pkb, int(PEAK_BANDS[np.argmax(pkb)])\n        else:\n            res[f\"peak_curve_dir_{key}\"], res[f\"peak_band_dir_{key}\"] = None, None"
}
```

```
The file entries/crcns-fcx-2-johnson-2018/fcx2.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev.py <<'EOF'
import pickle, os, sys, time, resource, numpy as np
sys.path.insert(0, '.')
import fcx2
for sid in sys.argv[1:]:
    sub, ch = pickle.load(open(os.environ['TMPDIR']+f'/{sid}.pkl','rb'))
    t = time.time(); san = fcx2.sanity_subject(sub); print('sanity', time.time()-t)
    r = fcx2.analyse_subject(sub, ch)
    r['sanity'] = san; r['chans'] = ch
    pickle.dump(r, open(os.environ['TMPDIR']+f'/{sid}_res.pkl','wb'))
    U = r['units']
    for k in ('z_post_mtmfft','z_post_sliding','z_post_code','z_post_mtmfft_shuf','z_post_sliding_shuf','z_post_code_shuf','z_pre_sliding'):
        v = np.array([u[k] for u in U]); print(k, len(v), 'sd %.2f >1.96 %.2f <-1.96 %.2f' % (v.std(), (v>1.96).mean(), (v<-1.96).mean()))
    print('excl', r['excluded'].sum(), 'desc', r['excluded_desc'].sum())
    print('maxrss GB', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
$TMPDIR/dev/bin/python $TMPDIR/dev.py s8 2>&1 | tail -20
```

```
sanity 1.2559573650360107
s8: analysed in 21 s; erp 2, power 10, power_test 12, plv 14, psi 18, pac 21
z_post_mtmfft 13 sd 0.30 >1.96 0.00 <-1.96 0.00
z_post_sliding 13 sd 0.77 >1.96 0.00 <-1.96 0.00
z_post_code 13 sd 18.52 >1.96 0.31 <-1.96 0.62
z_post_mtmfft_shuf 13 sd 0.33 >1.96 0.00 <-1.96 0.00
z_post_sliding_shuf 13 sd 0.66 >1.96 0.00 <-1.96 0.00
z_post_code_shuf 13 sd 15.22 >1.96 0.31 <-1.96 0.62
z_pre_sliding 13 sd 0.67 >1.96 0.00 <-1.96 0.00
excl 2 desc 1
maxrss GB 0.6306
```

**Agent calls Bash**

```bash
grep -n "hg = {}" -A12 fcx2.py | head -14; grep -n "jt = {}" -A8 fcx2.py
```

```
1012:    hg = {}
1013-    for k in ("pre", "encmain", "proc"):
1014-        d = seg[k]
1015-        a = _filter_chunks(d["x"], d["fs"], np.arange(d["x"].shape[-1]), np.array([[70.0, 150.0]]), "abs")[:, :, 0]
1016-        a = a / a.mean(axis=(0, 2), keepdims=True)
1017-        edges = np.arange(-1.5, 3.0001, 0.05)
1018-        idx = np.digitize(d["time"], edges) - 1
1019-        for jit in (900, 1150):
1020-            m = a[d["trialinfo"][:, 4] == jit].mean(axis=(0, 1))
1021-            hg[(k, jit)] = np.array([m[idx == j].mean() if np.any(idx == j) else np.nan for j in range(len(edges) - 1)])
1022-    out["hg"] = hg
1023-    # per electrode: t of the 900 against the 1150 ms trials in each 50 ms bin, for log high-gamma
1024-    # amplitude and the 30 Hz low-passed signal. The test cue comes 250 ms later after the long
1027:    jt = {}
1028-    for k in ("pre", "encmain", "proc"):
1029-        d = seg[k]
1030-        x = d["x"]
1031-        ln = np.log(_filter_chunks(x, d["fs"], np.arange(x.shape[-1]), np.array([[70.0, 150.0]]), "abs")[:, :, 0])
1032-        lp = lowpass_erp(x, d["fs"], np.arange(x.shape[-1]))
1033-        edges = np.arange(-1.5, 3.0001, 0.05)
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; $TMPDIR/dev/bin/python $TMPDIR/dev.py s3 2>&1 | tail -12
```

```
Mon Nov  9 00:41:27 UTC 2026
sanity 2.6943089962005615
s3: analysed in 52 s; erp 4, power 24, power_test 25, plv 28, psi 37, pac 52
z_post_mtmfft 15 sd 0.73 >1.96 0.00 <-1.96 0.00
z_post_sliding 15 sd 0.75 >1.96 0.00 <-1.96 0.00
z_post_code 15 sd 26.33 >1.96 0.67 <-1.96 0.27
z_post_mtmfft_shuf 15 sd 0.33 >1.96 0.00 <-1.96 0.00
z_post_sliding_shuf 15 sd 0.60 >1.96 0.00 <-1.96 0.00
z_post_code_shuf 15 sd 28.59 >1.96 0.53 <-1.96 0.33
z_pre_sliding 15 sd 0.64 >1.96 0.00 <-1.96 0.00
excl 0 desc 0
maxrss GB 1.0856
```

**Agent**

The clock reads 00:41, so there are about four hours left. On s3 the revised analysis takes 52 s against 33 s before; I'll profile the power step before estimating the full run.

**Agent calls Bash**

```bash
cat > $TMPDIR/prof.py <<'EOF'
import pickle, os, sys, cProfile, pstats
sys.path.insert(0, '.')
import fcx2
sub, ch = pickle.load(open(os.environ['TMPDIR']+'/s3.pkl','rb'))
cProfile.run('fcx2.analyse_subject(sub, ch, pac=False)', os.environ['TMPDIR']+'/prof.out')
pstats.Stats(os.environ['TMPDIR']+'/prof.out').sort_stats('cumulative').print_stats(25)
EOF
$TMPDIR/dev/bin/python $TMPDIR/prof.py 2>&1 | grep -E "cumtime|fcx2|numpy|scipy" | head -40
```

```
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.755    0.755   38.287   38.287 entries/crcns-fcx-2-johnson-2018/fcx2.py:691(analyse_subject)
        7    3.071    0.439   16.148    2.307 entries/crcns-fcx-2-johnson-2018/fcx2.py:643(_filter_chunks)
      259    2.498    0.010   12.522    0.048 entries/crcns-fcx-2-johnson-2018/fcx2.py:233(back)
      413   11.473    0.028   11.474    0.028 /tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/fft/_pocketfft.py:58(_raw_fft)
        4    0.130    0.032   10.499    2.625 entries/crcns-fcx-2-johnson-2018/fcx2.py:264(resample_20hz)
        2    0.000    0.000   10.361    5.180 /tmp/claude-1001/dev/lib/python3.13/site-packages/scipy/signal/_signaltools.py:3884(resample_poly)
        2    0.000    0.000   10.361    5.180 /tmp/claude-1001/dev/lib/python3.13/site-packages/scipy/signal/_upfirdn.py:108(upfirdn)
        2   10.360    5.180   10.361    5.180 /tmp/claude-1001/dev/lib/python3.13/site-packages/scipy/signal/_upfirdn.py:91(apply_filter)
      259    0.002    0.000   10.023    0.039 /tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/fft/_pocketfft.py:219(ifft)
       10    0.146    0.015    4.742    0.474 entries/crcns-fcx-2-johnson-2018/fcx2.py:351(cluster_test)
    20/12    3.243    0.162    3.785    0.315 entries/crcns-fcx-2-johnson-2018/fcx2.py:412(theta_fourier)
    15015    0.960    0.000    2.680    0.000 entries/crcns-fcx-2-johnson-2018/fcx2.py:331(_cluster_sums)
      210    1.449    0.007    1.778    0.008 entries/crcns-fcx-2-johnson-2018/fcx2.py:303(_stat)
    15015    0.959    0.000    1.078    0.000 /tmp/claude-1001/dev/lib/python3.13/site-packages/scipy/ndimage/_measurements.py:43(label)
       17    0.038    0.002    0.970    0.057 entries/crcns-fcx-2-johnson-2018/fcx2.py:228(fft)
      148    0.000    0.000    0.958    0.006 /tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/fft/_pocketfft.py:120(fft)
       50    0.599    0.012    0.783    0.016 entries/cr
[... 6 more lines not kept]
```

**Agent**

Profiling shows nothing new is costly; most of the time is the resampling matrices, which are cached across subjects. I estimate the full run at 40 to 45 minutes. Now the notebook cells.

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('reproduce_johnson_2018.ipynb'))
for i in [0,7,9,10,11,12,13,14,18,19,20]:
    print(f'=== [{i}]'); print(''.join(nb['cells'][i]['source']))
EOF
```

```
=== [0]
# Reproducing Johnson et al. (2018) from CRCNS fcx-2

**Paper.** Johnson EL, Adams JN, Solbakk A-K, Endestad T, Larsson PG, Ivanovic J, Meling TR, Lin JJ,
Knight RT (2018). Dynamic frontotemporal systems process space and time in working memory. *PLoS
Biology* 16, e2004274. [doi:10.1371/journal.pbio.2004274](https://doi.org/10.1371/journal.pbio.2004274).
The claims file was written from the version of record (PMC5895055, full text with Methods and
figure legends; the supplementary tables were not supplied).

**Data set.** CRCNS [fcx-2](https://crcns.org/data-sets/pfc/fcx-2),
[doi:10.6080/K0VX0DQD](https://doi.org/10.6080/K0VX0DQD), read from the public bucket
`crcnsarchive` under `fcx-2/live/`. CRCNS data sets are not versioned, so the version is recorded
as `unversioned`. The paper cites the data set by its DOI and no version. The bucket holds the live
files and, under `fcx-2/orig/ver_0_6/`, only the documents and scripts of version 0.6; the data
files exist once, under `live/`, which is the published version 0.61 (descriptor of April 4, 2018,
whose change from 0.6 is an updated `psianalysis.m`). This is the only version of the data, so it is
pinned. MD5 sums of the files read, from the data set's `checksums.md5`:

| file | md5 |
|---|---|
[... 259 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/rt.py <<'EOF'
import pickle, os, sys, numpy as np, pandas as pd
sys.path.insert(0, '.')
import fcx2
summ = fcx2.read_summary_file().set_index('subject')
for sid in ['s3','s8']:
    r = pickle.load(open(os.environ['TMPDIR']+f'/{sid}_res.pkl','rb'))
    t = r['sanity']['trials']; ti = r['trialinfo']
    k = pd.DataFrame({'accuracy': ti[:,1], 'condition': ti[:,3], 'rt': ti[:,5]})
    print(sid, 'doc', summ.loc[sid, ['rt_identity','rt_spatial','rt_temporal']].round(1).tolist())
    for name, src in (('table', t), ('kept', k)):
        for c in (1,2,3):
            tc = src[src.condition==c]; cr = tc[tc.accuracy==1].rt
            print(' ', name, c, 'mean corr %.1f med %.1f mean all %.1f med all %.1f n %d' % (cr.mean(), cr.median(), tc.rt.mean(), tc.rt.median(), len(cr)),
                  'trim3sd %.1f' % cr[np.abs(cr-cr.mean())<=3*cr.std()].mean(), 'trim2sd %.1f' % cr[np.abs(cr-cr.mean())<=2*cr.std()].mean(), 'min/max', cr.min(), cr.max())
EOF
$TMPDIR/dev/bin/python $TMPDIR/rt.py
```

```
s3 doc [2248.9, 1432.2, 1481.5]
  table 1 mean corr 2100.4 med 1826.0 mean all 2277.8 med all 1911.5 n 37 trim3sd 1984.3 trim2sd 1927.2 min/max 1211 6279
  table 2 mean corr 1285.1 med 799.0 mean all 1928.5 med all 861.0 n 31 trim3sd 1076.1 trim2sd 961.6 min/max 437 7555
  table 3 mean corr 1303.3 med 816.0 mean all 1506.9 med all 992.0 n 30 trim3sd 1106.8 trim2sd 1106.8 min/max 442 7002
  kept 1 mean corr 2100.4 med 1826.0 mean all 2134.2 med all 1859.0 n 37 trim3sd 1984.3 trim2sd 1927.2 min/max 1211.0 6279.0
  kept 2 mean corr 1285.1 med 799.0 mean all 1942.1 med all 849.0 n 31 trim3sd 1076.1 trim2sd 961.6 min/max 437.0 7555.0
  kept 3 mean corr 1355.7 med 833.5 mean all 1566.3 med all 998.0 n 28 trim3sd 1146.6 trim2sd 1146.6 min/max 442.0 7002.0
s8 doc [1469.2, 1037.1, 989.3]
  table 1 mean corr 1469.2 med 1299.0 mean all 1578.1 med all 1319.5 n 36 trim3sd 1336.1 trim2sd 1336.1 min/max 835 4063
  table 2 mean corr 1037.1 med 764.0 mean all 1074.1 med all 796.5 n 39 trim3sd 945.2 trim2sd 886.6 min/max 583 4529
  table 3 mean corr 989.3 med 789.0 mean all 1021.4 med all 792.0 n 39 trim3sd 934.7 trim2sd 897.9 min/max 499 3063
  kept 1 mean corr 1489.3 med 1319.0 mean all 1574.0 med all 1351.0 n 26 trim3sd 1386.3 trim2sd 1386.3 min/max 906.0 4063.0
  kept 2 mean corr 968.8 med 726.5 mean all 1022.1 med all 733.0 n 28 trim3sd 836.9 trim2sd 836.9 min/max 591.0 4529.0
  kept 3 mean corr 982.2 med 774.5 mean all 982.2 med all 774.5 n 32 trim3sd 915.0 trim2sd 915.0 min/max 499.0 3063.0
```

**Agent calls Bash**

```bash
cat > $TMPDIR/tables.py <<'EOF'
import sys, os, tarfile, requests, pandas as pd, pickle, time
sys.path.insert(0, '.')
import fcx2
out = {}
for sid in fcx2.SUBJECTS:
    t0 = time.time()
    with requests.get(f"{fcx2.BASE}/data_indiv/{sid}.tar.gz", stream=True, timeout=120) as resp:
        tf = tarfile.open(fileobj=resp.raw, mode="r|gz")
        for m in tf:
            if m.name.endswith("summary_file_trial.csv"):
                out[sid] = pd.read_csv(tf.extractfile(m), header=None, names=fcx2.TRIAL_COLS); break
    print(sid, time.time()-t0, flush=True)
pickle.dump(out, open(os.environ['TMPDIR']+'/tables.pkl','wb'))
EOF
timeout 900 $TMPDIR/dev/bin/python $TMPDIR/tables.py
```

```
s1 16.39287042617798
s2 11.822993516921997
s3 13.123469352722168
s4 13.475054264068604
s5 40.259002685546875
s6 21.098921537399292
s7 19.107939958572388
s8 7.989145278930664
s9 26.05242347717285
s10 21.489364624023438
```

**Agent calls Bash**

```bash
cat > $TMPDIR/rt2.py <<'EOF'
import pickle, os, sys, numpy as np, pandas as pd, itertools
sys.path.insert(0, '.')
import fcx2
summ = fcx2.read_summary_file().set_index('subject')
T = pickle.load(open(os.environ['TMPDIR']+'/tables.pkl','rb'))
doc = summ[['rt_identity','rt_spatial','rt_temporal']]
def stats_for(t):
    out = {}
    for c in (1,2,3):
        tc = t[t.condition==c]; cr = tc[tc.accuracy==1].rt
        out[c] = {'mean_corr': cr.mean(), 'med_corr': cr.median(), 'mean_all': tc.rt.mean(), 'med_all': tc.rt.median(),
                  'mean_inc': tc[tc.accuracy==0].rt.mean(),
                  'first30': cr.iloc[:30].mean(), 'gmean': np.exp(np.log(cr).mean())}
    return out
S = {s: stats_for(t) for s, t in T.items()}
# exact matches anywhere
for s in doc.index:
    for ci, col in enumerate(doc.columns):
        v = doc.loc[s, col]
        hits = [(s2, c, k) for s2 in S for c in S[s2] for k, x in S[s2][c].items() if abs(x - v) < 0.06]
        print(s, col, round(v,1), 'own mean_corr', round(S[s][ci+1]['mean_corr'],1), 'hits', hits)
EOF
$TMPDIR/dev/bin/python $TMPDIR/rt2.py
```

```
s1 rt_identity 1948.0 own mean_corr 2348.3 hits []
s1 rt_spatial 1844.5 own mean_corr 1060.6 hits []
s1 rt_temporal 1556.9 own mean_corr 1575.1 hits []
s2 rt_identity 1155.1 own mean_corr 1324.4 hits []
s2 rt_spatial 1092.2 own mean_corr 1095.1 hits []
s2 rt_temporal 1169.4 own mean_corr 940.9 hits []
s3 rt_identity 2248.9 own mean_corr 2100.4 hits []
s3 rt_spatial 1432.2 own mean_corr 1285.1 hits []
s3 rt_temporal 1481.5 own mean_corr 1303.3 hits []
s4 rt_identity 1562.4 own mean_corr 2108.0 hits []
s4 rt_spatial 1740.3 own mean_corr 1304.4 hits []
s4 rt_temporal 2069.6 own mean_corr 1271.4 hits []
s5 rt_identity 3174.5 own mean_corr 2743.9 hits []
s5 rt_spatial 2535.3 own mean_corr 2997.7 hits []
s5 rt_temporal 3142.2 own mean_corr 2712.3 hits []
s6 rt_identity 1685.7 own mean_corr 1685.7 hits [('s6', 1, 'mean_corr')]
s6 rt_spatial 962.9 own mean_corr 962.9 hits [('s6', 2, 'mean_corr'), ('s6', 2, 'mean_all')]
s6 rt_temporal 1088.4 own mean_corr 1088.4 hits [('s6', 3, 'mean_corr')]
s7 rt_identity 779.4 own mean_corr 1010.0 hits []
s7 rt_spatial 740.1 own mean_corr 549.0 hits []
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/rt2.py <<'EOF'
print('---- other splits')
for s, t in T.items():
    cr = t[t.accuracy==1]
    blocks = [cr[(cr.trial>40*i)&(cr.trial<=40*(i+1))].rt.mean() for i in range(3)]
    print(s, 'doc', doc.loc[s].round(1).tolist(), 'overall corr', round(cr.rt.mean(),1), 'doc avg', round(doc.loc[s].mean(),1),
          'blocks', np.round(blocks,1).tolist(), 'by type', cr.groupby('trial_type').rt.mean().round(1).tolist(),
          'cond counts', t.condition.value_counts().sort_index().tolist(), 'trial order head', t.condition.tolist()[:12])
EOF
$TMPDIR/dev/bin/python $TMPDIR/rt2.py | sed -n '/----/,$p'
```

```
---- other splits
s1 doc [1948.0, 1844.5, 1556.9] overall corr 1651.8 doc avg 1783.1 blocks [1266.5, 1867.9, 1836.9] by type [2348.3, 1303.6] cond counts [40, 40, 40] trial order head [3, 2, 3, 3, 2, 1, 3, 3, 2, 3, 3, 3]
s2 doc [1155.1, 1092.2, 1169.4] overall corr 1118.4 doc avg 1138.9 blocks [1167.9, 1084.9, 1103.5] by type [1324.4, 1018.0] cond counts [40, 40, 40] trial order head [2, 3, 1, 1, 1, 2, 3, 1, 3, 3, 3, 1]
s3 doc [2248.9, 1432.2, 1481.5] overall corr 1598.5 doc avg 1720.9 blocks [2147.9, 1532.2, 1169.2] by type [2100.4, 1294.0] cond counts [40, 40, 40] trial order head [2, 3, 2, 3, 3, 2, 3, 1, 2, 3, 2, 3]
s4 doc [1562.4, 1740.3, 2069.6] overall corr 1558.7 doc avg 1790.8 blocks [1376.0, 2003.4, 1319.9] by type [2108.0, 1287.7] cond counts [40, 40, 40] trial order head [3, 3, 3, 3, 2, 3, 2, 2, 1, 3, 3, 1]
s5 doc [3174.5, 2535.3, 3142.2] overall corr 2819.4 doc avg 2950.7 blocks [2527.3, 2841.3, 3138.4] by type [2743.9, 2859.6] cond counts [40, 40, 40] trial order head [3, 1, 2, 2, 1, 3, 3, 2, 1, 2, 1, 2]
s6 doc [1685.7, 962.9, 1088.4] overall corr 1238.2 doc avg 1245.7 blocks [1125.6, 1226.8, 1358.8] by type [1685.7, 1023.2] cond counts [40, 40, 40] trial order head [2, 2, 2, 2, 3, 3, 2, 1, 1, 3, 3, 3]
s7 doc [779.4, 740.1, 647.6] overall corr 690.7 doc avg 722.4 blocks [846.6, 596.9, 636.5] by type [1010.0, 545.2] cond counts [40, 40, 40] trial order head [3, 1, 2, 3, 1, 1, 2, 3, 3, 3, 3, 3]
s8 doc [1469.2, 1037.1, 989.3] overall corr 1157.2 doc avg 1165.2 blocks [1153.2, 1060.6, 1255.3] by type [1469.2, 1013.2] cond counts [40, 40, 40] trial order head [1, 3, 3, 3, 3, 2, 2, 2, 3, 2, 3, 1]
s9 doc [1700.1, 1308.8, 1797.5] overall corr 1604.1 doc avg 1602.1 blocks [1658.5, 1662.4, 1492.9] by type [1700.1, 1553.2] cond counts [40, 40, 40] trial order head [1, 3, 3, 1, 3, 1, 1, 1, 1, 3, 2, 2]
s10 doc [869.8, 661.3, 811.4] overall corr 806.2 doc avg 780.8 blocks [780.1, 838.4, 798.4] by type [951.6, 739.2] cond counts [40, 40, 40] trial order head [2, 3, 2,
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('reproduce_johnson_2018.ipynb'))
for i in range(27,60):
    print(f'=== [{i}]'); print(''.join(nb['cells'][i]['source']))
EOF
```

```
=== [27]
## erp-no-condition-difference

> ERPs did not differ between identity, spatial and temporal conditions in any electrode, over
> encoding, precue or postcue intervals.

The test is run per subject as `erp_compute.m` does (all of a subject's analysed electrodes in one
test, so the null is the largest cluster over the subject's electrodes), and per electrode (the
Methods' "clustered per electrode") as a variant.
=== [28]
rows = []
for sid, r in R.items():
    for test in ("erp_enc", "erp_post"):
        d = r[test]
        rows.append({"subject": sid, "test": test, "n_el": len(d), "sig_subject_null": int((d.p_subject < 0.05).sum()),
                     "sig_electrode_null": int((d.p_electrode < 0.05).sum()), "min_p_subject": round(d.p_subject.min(), 3),
                     "min_p_electrode": round(d.p_electrode.min(), 3)})
erp = pd.DataFrame(rows)
print(erp.to_string(index=False))
n_el = len(chtab)
[... 494 more lines not kept]
```

**Agent**

I'm adding a helper that reads the deposited scripts from the archive so the notebook can quote the lines that settle the baseline, latency and PSI questions (verifier section C).

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py",
 "old_string": "TRIAL_COLS = [",
 "new_string": "def read_scripts():\n    \"\"\"The deposited analysis scripts (analysis_scripts.tar.gz), as {file name: text}; read to\n    quote the lines a method detail is taken from, not run.\"\"\"\n    raw = requests.get(f\"{BASE}/analysis_scripts.tar.gz\", timeout=120).content\n    out = {}\n    with tarfile.open(fileobj=io.BytesIO(raw), mode=\"r:gz\") as tf:\n        for m in tf:\n            if m.isfile() and m.name.endswith(\".m\"):\n                out[m.name.split(\"/\")[-1]] = tf.extractfile(m).read().decode(\"latin-1\")\n    return out\n\n\nTRIAL_COLS = ["
}
```

```
The file entries/crcns-fcx-2-johnson-2018/fcx2.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR/as/analysis_scripts; grep -n "" subfunctions/psianalysis.m | sed -n 25,75p | head -5; grep -n "mtmfft\|taper\|t_ftimwin\|foi\|pad\b\|cfgf.pad\|subtracterp\|fourier" psi_compute.m cspsi_compute.m | head -30; grep -n "baseline\|nanmean\|latency\|avgovertime" erp_compute.m
```

```
25:
26:% compute cross-spectral density
27:csd = zeros(ntrials, nchan, nchan, nfidx);
28:for e = 1:nchan
29:    csd(:,e,:,:) = repmat(data.fourierspctrm(:,e,:), [1 nchan 1]).*data2.fourierspctrm;
psi_compute.m:30:cfg.method = 'mtmfft';
psi_compute.m:31:cfg.taper = 'hanning';
psi_compute.m:32:cfg.foi = 3:1:7; % 3-7 Hz
psi_compute.m:34:cfg.pad = 4; % pad to 4 s
psi_compute.m:35:cfg.t_ftimwin = 3./cfg.foi; % frequency-dependent time window
psi_compute.m:36:cfg.output = 'fourier';
psi_compute.m:53:encmain = subtracterp(encmain, 1); % subtract ERP
psi_compute.m:59:proc = subtracterp(proc, 1); % subtract ERP
cspsi_compute.m:30:cfg.method = 'mtmfft';
cspsi_compute.m:31:cfg.taper = 'hanning';
cspsi_compute.m:32:cfg.foi = 3:1:7; % 3-7 Hz
cspsi_compute.m:34:cfg.pad = 4; % pad to 4 s
cspsi_compute.m:35:cfg.t_ftimwin = 3./cfg.foi; % frequency-dependent time window
cspsi_compute.m:36:cfg.output = 'fourier';
cspsi_compute.m:49:cfgfilt.padding = 4; % pad to 4 s
[... 14 more lines not kept]
```

**Agent**

Now the notebook edits, done with a script that rewrites the code cells and inserts the new ones.

**Agent calls Bash**

```bash
cd entries/crcns-fcx-2-johnson-2018 && cat > $TMPDIR/edit_nb.py <<'PYEOF'
import json, sys
P = 'reproduce_johnson_2018.ipynb'
nb = json.load(open(P))
C = nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s): C[i]['source'] = s.splitlines(keepends=True)
def code(s, tags=None):
    return {"cell_type": "code", "execution_count": None, "metadata": ({"tags": tags} if tags else {}), "outputs": [], "source": s.splitlines(keepends=True)}
def md(s):
    return {"cell_type": "markdown", "metadata": {}, "source": s.splitlines(keepends=True)}
# sanity: anchor checks
assert src(11).startswith('edges = R["s1"]')
assert src(13).startswith('# behaviour tables')
assert src(28).startswith('rows = []\nfor sid, r in R.items():\n    for test in ("erp_enc"')
assert src(31).startswith('TH = [2, 3, 4, 5]')
assert src(34).startswith('rows = []')
assert src(40).startswith('def pair_table')
assert src(43).startswith('units = []')
assert src(46).startswith('EXP = ')
assert src(52).startswith('names = ')

# ---- cell 11: add the per-electrode jitter check
setsrc(11, src(11) + '''
# per electrode: t of the 900 against the 1150 ms trials in 50 ms bins (fcx2.sanity_subject).
# Without a task-locked response to the test cue, about 5% of electrode bins pass |t| > 1.96.
print("\\nPer electrode, 900 against 1150 ms delay trials: fraction of electrode bins with |t| > 1.96, and the")
print("largest |t| over electrodes, in 250 ms windows from -1.5 s (test cue onset: 0 s under the trial")
print("table's placement, 1.5 s under the code's)")
wins = np.arange(-1.5, 3.0, 0.25)
for seg in ("pre", "encmain", "proc"):
    for name in ("hg", "erp"):
        allt = np.concatenate([r["sanity"]["jitter_t"][(seg, name)] for r in R.values()])     # (electrodes, bins)
        frac = [np.nanmean(np.abs(allt[:, (centres >= w0) & (centres < w0 + 0.25)]) > 1.96) for w0 in wins]
        mx = [np.nanmax(np.abs(allt[:, (centres >= w0) & (centres < w0 + 0.25)])) for w0 in wins]
        print(f"  {seg:8s}{name:4s} frac " + " ".join(f"{v:.2f}" for v in frac))
        print(f"  {'':12s} max  " + " ".join(f"{v:4.1f}" for v in mx))
print("  window starts (s):", " ".join(f"{w:+.2f}" for w in wins))
# the electrode with the largest high-gamma modulation in encmain, per subject
rows = []
for sid, r in R.items():
    hm = r["sanity"]["jitter_t"][("encmain", "hg_mean")][:, 1:]          # first bin is the segment edge
    rng_ = hm.max(axis=1) - hm.min(axis=1)
    e = int(np.argmax(rng_))
    rows.append({"subject": sid, "electrode": r["chans"].label[e], "region": r["chans"].region[e],
                 "log_amp_range": round(float(rng_[e]), 3), "peak_at_s": round(float(centres[1:][np.argmax(hm[e])]), 2),
                 "trough_at_s": round(float(centres[1:][np.argmin(hm[e])]), 2),
                 "curve_100ms": np.round(hm[e][::2], 2).tolist()})
print(pd.DataFrame(rows).to_string(index=False))
''')

# ---- new cell after 12: the deposited scripts' lines
scripts_cell = code('''# the deposited analysis scripts, read to quote the lines the windows, the ERP baseline and the
# PSI are taken from (not run)
SCRIPTS = fcx2.read_scripts()


def quote(name, first, last):
    lines = SCRIPTS[name].splitlines()
    print(f"--- {name}, lines {first}-{last}")
    for k in range(first - 1, last):
        print(f"{k + 1:4d}  {lines[k]}")


print("files:", sorted(SCRIPTS))
quote("erp_compute.m", 44, 47)        # baseline window
quote("erp_compute.m", 74, 97)        # baseline correction and segment latencies
for name in ("power_compute.m", "psi_compute.m", "cspsi_compute.m", "plv_compute.m", "pac_compute.m", "dirpac_compute.m"):
    for k, line in enumerate(SCRIPTS[name].splitlines()):
        if "latency" in line:
            print(f"{name}:{k + 1}  {line.strip()}")
quote("psi_compute.m", 29, 36)        # spectral step
quote("psianalysis.m", 26, 30)        # cross-spectral density, no conjugate
quote("psianalysis.m", 46, 72)        # per-trial PSI, trial mean, frequency-shuffled null
''', tags=['sanity'])
scripts_md = md('''`erp_compute.m` (lines 84 to 88) subtracts `nanmean(pretrial.trial)`, the mean over trials of each
trial's baseline mean, so one value per electrode is subtracted from every trial; the ERP section
follows it, and subtracting each trial's own baseline mean is run as a variant. Every script cuts
the same latencies from the derived segments ([0 1.5] of `encmain`, [0.6 1.5] for the precue
delay, [0.3 1.2] of `proc`, [0.65 0.85] of `pre`, commented "-250 to 50 ms pretrial"). The PSI
script uses FieldTrip `mtmfft` with a Hanning taper and `t_ftimwin` set, which `mtmfft` ignores, so
the spectrum comes from one window over the 900 ms segment. `psianalysis.m` multiplies the Fourier
coefficients without a conjugate, takes the trial mean of per-trial PSI as the observed value, and
z-scores it against PSI computed from the trial-mean normalised cross-spectrum with its frequencies
shuffled.
''')

# ---- cell 13: response-time provenance
setsrc(13, src(13) + '''
# where do the response times of summary_file.csv come from? Candidate summaries of the trial
# tables, per subject and condition, against the file (a match is within 0.05 ms)
cands = {}
for sid, r in R.items():
    t = r["sanity"]["trials"]
    ti = r["trialinfo"]
    k = pd.DataFrame({"accuracy": ti[:, 1], "condition": ti[:, 3], "rt": ti[:, 5], "trial": ti[:, 0]})
    for c in (1, 2, 3):
        tc, kc = t[t.condition == c], k[k.condition == c]
        cr = tc[tc.accuracy == 1]
        cands[(sid, c)] = {"mean correct": cr.rt.mean(), "median correct": cr.rt.median(), "mean all": tc.rt.mean(),
                           "median all": tc.rt.median(), "mean incorrect": tc[tc.accuracy == 0].rt.mean(),
                           "mean kept correct": kc[kc.accuracy == 1].rt.mean(), "mean kept all": kc.rt.mean(),
                           "median kept correct": kc[kc.accuracy == 1].rt.median(),
                           "geometric mean correct": np.exp(np.log(cr.rt).mean()),
                           "mean correct, by trial type": t[(t.accuracy == 1) & (t.trial_type == (1 if c == 1 else 2))].rt.mean()}
    cr = t[t.accuracy == 1]
    for b in range(3):
        cands[(sid, f"block{b + 1}")] = {"mean correct, trials of block": cr[(cr.trial > 40 * b) & (cr.trial <= 40 * (b + 1))].rt.mean()}
doc = summary.set_index("subject")
rows = []
for sid in R:
    for c, name in ((1, "identity"), (2, "spatial"), (3, "temporal")):
        v = doc.loc[sid, f"rt_{name}"]
        hits = [f"{s2}/{c2}: {k}" for (s2, c2), d in cands.items() for k, x in d.items() if abs(x - v) < 0.05]
        rows.append({"subject": sid, "condition": name, "summary_file": round(v, 1),
                     "mean_correct": round(cands[(sid, c)]["mean correct"], 1),
                     "median_correct": round(cands[(sid, c)]["median correct"], 1),
                     "mean_all": round(cands[(sid, c)]["mean all"], 1), "matches": hits or "none"})
prov = pd.DataFrame(rows)
print("\\nsummary_file.csv response times against summaries of the trial tables (any subject, condition or block):")
print(prov.to_string(index=False))
print("subject-condition values matched by some summary:", int((prov.matches != "none").sum()), "of", len(prov),
      "; subjects with all three matched:", sorted(prov.groupby("subject").matches.apply(lambda s: (s != "none").all()).loc[lambda s: s].index.tolist()))
''')

# ---- cell 28: ERP variants
setsrc(28, '''rows = []
for tag, label in (("", "code: trial-mean baseline"), ("_trial", "variant: per-trial baseline"), ("_desc", "variant: trial table's windows")):
    for sid, r in R.items():
        for test in ("erp_enc", "erp_post"):
            d = r[test + tag]
            rows.append({"reading": label, "subject": sid, "test": test, "n_el": len(d),
                         "sig_subject_null": int((d.p_subject < 0.05).sum()),
                         "sig_electrode_null": int((d.p_electrode < 0.05).sum()), "min_p_subject": round(d.p_subject.min(), 3),
                         "min_p_electrode": round(d.p_electrode.min(), 3)})
erp = pd.DataFrame(rows)
print(erp[erp.reading.str.startswith("code")].to_string(index=False))
n_el = len(chtab)
for tag, label in (("", "code: trial-mean baseline"), ("_trial", "variant: per-trial baseline"), ("_desc", "variant: trial table's windows")):
    for null in ("p_subject", "p_electrode"):
        sig_any = sum(int(((R[s]["erp_enc" + tag][null] < 0.05).to_numpy() | (R[s]["erp_post" + tag][null] < 0.05).to_numpy()).sum()) for s in R)
        where = [(s, R[s]["chans"].label[i]) for s in R for i in np.where((R[s]["erp_enc" + tag][null] < 0.05).to_numpy() | (R[s]["erp_post" + tag][null] < 0.05).to_numpy())[0]]
        print(f"{label}, {null}: electrodes with a significant cluster in either test: {sig_any} of {n_el}"
              + (f" {where}" if null == "p_subject" else ""))
print(f"expected false positives at alpha 0.05 over {n_el} electrodes and two tests, per-electrode null: {0.05 * 2 * n_el:.1f}")
''')

# ---- cell 31: power, both placements
s31 = src(31)
s31 = s31.replace('''def zcurve(r, idx, bands):
    zs = np.concatenate([r["power_z_mean"]["enc"][idx][:, bands].mean(axis=1),
                         r["power_z_mean"]["post"][idx][:, bands].mean(axis=1)], axis=-1)
    return zs                                                # (electrodes, 50 time points)


rows, el_rows = [], []
for sid, r in R.items():''', '''def zcurve(r, idx, bands, key="power_z_mean"):
    zs = np.concatenate([r[key]["enc"][idx][:, bands].mean(axis=1),
                         r[key]["post"][idx][:, bands].mean(axis=1)], axis=-1)
    return zs                                                # (electrodes, 50 time points)


def power_table(key):
  rows = []
  for sid, r in R.items():''')
assert 'def power_table' in s31
# re-indent the loop body by two spaces
head, body = s31.split("  for sid, r in R.items():\n", 1)
loop, rest = body.split("pw = pd.DataFrame(rows)\n", 1)
loop = "".join(("  " + l if l.strip() else l) for l in loop.splitlines(keepends=True))
loop = loop.replace("th = zcurve(r, idx, TH)", "th = zcurve(r, idx, TH, key)").replace("al = zcurve(r, idx, AL)", "al = zcurve(r, idx, AL, key)")
loop = loop.replace('r["power_z_mean"]', 'r[key]')
rest_new = '''  return pd.DataFrame(rows)


for key, label in (("power_z_mean", "code's windows"), ("power_z_mean_desc", "trial table's windows (1.5 s earlier)")):
  pw = power_table(key)
  print(f"=== {label}")
  if key == "power_z_mean":
      print(pw.round(3).to_string(index=False))
''' + "".join(("  " + l if l.strip() else l) for l in rest.splitlines(keepends=True))
setsrc(31, head + "  for sid, r in R.items():\n" + loop + rest_new)

# ---- cell 34: exclusions, both placements
setsrc(34, '''rows = []
for tag in ("", "_desc"):
    for sid, r in R.items():
        c = r["chans"]
        for null in ("p_subject", "p_electrode"):
            sig = (np.minimum(r["pow_enc" + tag][null], r["pow_post" + tag][null]) < 0.05).to_numpy()
            for i in np.where(sig)[0]:
                rows.append({"windows": "trial table" if tag else "code", "null": null, "subject": sid, "label": c.label[i],
                             "region": c.region[i], "p_enc": round(r["pow_enc" + tag][null][i], 3),
                             "p_post": round(r["pow_post" + tag][null][i], 3)})
ex = pd.DataFrame(rows)
print(ex[(ex.windows == "code") & (ex.null == "p_subject")].to_string(index=False))
print(ex[(ex.windows == "trial table") & (ex.null == "p_subject")].to_string(index=False))
for w in ("code", "trial table"):
    for null in ("p_subject", "p_electrode"):
        d = ex[(ex.windows == w) & (ex.null == null)]
        print(f"{w} windows, {null}: {len(d)} electrodes ({d.region.value_counts().to_dict()}) in {d.subject.nunique()} subjects; expected 8 (5 PFC, 3 OFC) in 4")
''')

# ---- cell 40: PSI theta, both placements and calibration
s40 = src(40)
s40 = s40.replace('''def pair_table(key):
    rows = []
    for sid, r in R.items():
        for g in ("MTL-PFC", "MTL-OFC"):
            for a, b in r["pairs"][g]:
                for w in ("pre", "post"):
                    d = r["psi"][(w, key)]''', '''def desc_pairs(r):
    """Same-hemisphere MTL-frontal pairs after the exclusions of the trial table's windows."""
    c, keep = r["chans"], ~r["excluded_desc"]
    out = {"MTL-PFC": [], "MTL-OFC": []}
    for a in np.where((c.region == "MTL").to_numpy() & keep)[0]:
        for b in np.where(keep & (c.hemi == c.hemi[a]).to_numpy() & c.region.isin(["PFC", "OFC"]).to_numpy())[0]:
            out[f"MTL-{c.region[b]}"].append((a, b))
    return out


def pair_table(key, desc=False):
    rows = []
    for sid, r in R.items():
        pairs = desc_pairs(r) if desc else r["pairs"]
        for g in ("MTL-PFC", "MTL-OFC"):
            for a, b in pairs[g]:
                for w in ("pre", "post"):
                    d = r["psi"][(w, key, "desc") if desc else (w, key)]''')
assert 'def desc_pairs' in s40
s40 = s40.replace('''rows = []
for key in ("mtmfft", "sliding", "code"):
    pt = pair_table(key)''', '''rows = []
for key, desc in [(k, d) for d in (False, True) for k in ("mtmfft", "sliding", "code")]:
    pt = pair_table(key, desc)''')
s40 = s40.replace('''rows.append({"reading": key, "net": g,''', '''rows.append({"reading": key + (" / table" if desc else ""), "net": g,''')
s40 = s40.replace('''print("expected pairs: MTL-PFC 172 +- 17.2, MTL-OFC 303 +- 30.3")''', '''print("expected pairs: MTL-PFC 172 +- 17.2, MTL-OFC 303 +- 30.3")
for rd in ps.reading.unique():
    for y in ("z", "raw"):
        d = ps[(ps.reading == rd) & (ps.response == y)]
        p1 = (d.pre_mean_z < 0) & (d.pre_below > d.pre_above)
        p2 = (d.post_minus_pre > 0) & (d.p < 0.05)
        print(f"{rd:16s} {y:3s}: part (1) holds in {int(p1.sum())} of 2 networks, part (2) in {int(p2.sum())} of 2 "
              f"({', '.join(d.net[p2]) or 'none'})")
# calibration: postcue z with the second electrode's trials shuffled against the first's (no
# trial-by-trial coupling left), over the same pairs, against the real postcue z
rows = []
for key in ("mtmfft", "sliding", "code"):
    real = np.concatenate([[r["psi"][("post", key)]["z"][a, b] for g in ("MTL-PFC", "MTL-OFC") for a, b in r["pairs"][g]] for r in R.values()])
    shuf = np.concatenate([[r["psi"][("post", key, "shuf")]["z"][a, b] for g in ("MTL-PFC", "MTL-OFC") for a, b in r["pairs"][g]] for r in R.values()])
    for name, v in (("real", real), ("trials shuffled", shuf)):
        rows.append({"form": key, "data": name, "pairs": len(v), "z_sd": np.std(v), "frac_above_1.96": np.mean(v > 1.96),
                     "frac_below_-1.96": np.mean(v < -1.96)})
print("\\ntheta PSI, postcue: calibration (nominal 0.025 in each tail)")
print(pd.DataFrame(rows).round(3).to_string(index=False))''')
setsrc(40, s40)

# ---- cell 43: cross-spectral, add sliding and calibration
s43 = src(43)
s43 = s43.replace('''for key in ("mtmfft", "code"):
    for sname in SYSTEMS:''', '''for key in ("mtmfft", "sliding", "code"):
    for sname in SYSTEMS:''', 1)
s43 = s43.replace('''for key in ("mtmfft", "code"):
    for y in ("z", "raw"):''', '''for key in ("mtmfft", "sliding", "code"):
    for y in ("z", "raw"):''')
s43 += '''# calibration: postcue z with the amplitude electrode's trials shuffled against the phase
# electrode's, against the real postcue z, every unit (nominal 0.025 above 1.96)
rows = []
for key in ("mtmfft", "sliding", "code"):
    for sname in SYSTEMS:
        d = U[U.system == sname]
        for name, col in (("real", f"z_post_{key}"), ("trials shuffled", f"z_post_{key}_shuf")):
            rows.append({"form": key, "system": sname, "data": name, "units": len(d), "z_sd": d[col].std(),
                         "frac_above_1.96": (d[col] > 1.96).mean()})
cal = pd.DataFrame(rows)
print("\\ncross-spectral PSI, postcue: calibration")
print(cal.pivot_table(index=["form", "system"], columns="data", values="frac_above_1.96").round(3).to_string())
print(cal.groupby(["form", "data"]).apply(lambda g: pd.Series({"units": g.units.sum(), "z_sd_mean": g.z_sd.mean(),
      "frac_above_1.96": np.average(g["frac_above_1.96"], weights=g.units)})).round(3).to_string())
print("paper's selection rates (counts of phase-directing-counts over the units of crossspectral-shift):",
      {k: round(v / n, 2) for (k, v), n in zip({"MTL": 13, "PFC": 52, "OFC": 38, "MTL->PFC": 56, "PFC->MTL": 85, "MTL->OFC": 93, "OFC->MTL": 115}.items(),
                                                (36, 111, 99, 172, 172, 303, 303))})
'''
setsrc(43, s43)

# ---- cell 46
setsrc(46, src(46).replace('for key in ("mtmfft", "code"):', 'for key in ("mtmfft", "sliding", "code"):'))

# ---- cell 52
s52 = src(52)
s52 = s52.replace('''                 "b_directing_code_psi":''', '''                 "b_directing_sliding_psi": names.get(r["peak_band_dir_sliding"], "none") if r["peak_band_dir_sliding"] else "no electrodes",
                 "b_directing_code_psi":''')
s52 = s52.replace('for col in ("a_all_electrodes", "b_directing_methods_psi", "b_directing_code_psi"):', 'for col in ("a_all_electrodes", "b_directing_methods_psi", "b_directing_sliding_psi", "b_directing_code_psi"):')
setsrc(52, s52)

C.insert(13, scripts_md)
C.insert(13, scripts_cell)
json.dump(nb, open(P, 'w'), indent=1, ensure_ascii=False)
open(P, 'a').write('\n')
print('ok', len(C))
PYEOF
python $TMPDIR/edit_nb.py && python -c "
import json; nb=json.load(open('reproduce_johnson_2018.ipynb')); print(''.join(nb['cells'][33]['source']))"
```

```
ok 62
TH = [2, 3, 4, 5]
AL = [6, 7, 8]
HI = [i for i, c in enumerate(fcx2.CENTRES) if c > 16]


def zcurve(r, idx, bands, key="power_z_mean"):
    zs = np.concatenate([r[key]["enc"][idx][:, bands].mean(axis=1),
                         r[key]["post"][idx][:, bands].mean(axis=1)], axis=-1)
    return zs                                                # (electrodes, 50 time points)


def power_table(key):
  rows = []
  for sid, r in R.items():
      c = r["chans"]
      for reg in ("MTL", "PFC", "OFC"):
          idx = np.where(c.region == reg)[0]
          if len(idx) == 0:
              continue
[... 28 more lines not kept]
```

**Agent**

I'll clean up that cell: it prints the table twice and uses 2-space indentation.

**Agent calls Bash**

```bash
cat > $TMPDIR/fix31.py <<'PYEOF'
import json
P = 'reproduce_johnson_2018.ipynb'
nb = json.load(open(P)); C = nb['cells']
s = ''.join(C[33]['source'])
head, tail = s.split("def power_table(key):\n", 1)
out = []
for l in tail.splitlines(keepends=True):
    n = len(l) - len(l.lstrip(' '))
    if l.strip() and n % 2 == 0 and n > 0:
        # 2-space blocks become 4-space: depth = levels of the loop nesting
        pass
    out.append(l)
tail = "".join(out)
tail = tail.replace('''  if key == "power_z_mean":
      print(pw.round(3).to_string(index=False))
  print(pw.round(3).to_string(index=False))
''', '''  print(pw.round(3).to_string(index=False))
''')
# convert indentation: lines starting with 2-space units -> double them
conv = []
for l in tail.splitlines(keepends=True):
    stripped = l.lstrip(' ')
    n = len(l) - len(stripped)
    if stripped.strip():
        # body written as 2 + 4k spaces -> 4 + 4k
        if n % 4 == 2:
            n = n + 2
        conv.append(' ' * n + stripped)
    else:
        conv.append(l)
s = head + "def power_table(key):\n" + "".join(conv)
C[33]['source'] = s.splitlines(keepends=True)
json.dump(nb, open(P, 'w'), indent=1, ensure_ascii=False); open(P, 'a').write('\n')
print(s[s.index('def power_table'):])
PYEOF
python $TMPDIR/fix31.py
```

```
def power_table(key):
    rows = []
    for sid, r in R.items():
        c = r["chans"]
        for reg in ("MTL", "PFC", "OFC"):
            idx = np.where(c.region == reg)[0]
            if len(idx) == 0:
                continue
            th = zcurve(r, idx, TH, key)
            al = zcurve(r, idx, AL, key)
            hi = np.concatenate([r[key]["enc"][idx][:, [h for h in HI if h < r[key]["enc"].shape[1]]],
                               r[key]["post"][idx][:, [h for h in HI if h < r[key]["post"].shape[1]]]], axis=-1)
            rows.append({"subject": sid, "region": reg, "n": len(idx),
                       "theta_frac_above": (th.mean(axis=0) > 1.96).mean(), "theta_median_z": np.median(th.mean(axis=0)),
                       "alpha_frac_below": (al.mean(axis=0) < -1.96).mean(), "alpha_median_z": np.median(al.mean(axis=0)),
                       "el_theta_sustained": ((th > 1.96).mean(axis=1) >= 0.5).mean(),
                       "el_alpha_desync": ((al < -1.96).mean(axis=1) >= 0.5).mean(),
                       "el_any_high_above": int((hi > 1.96).any(axis=(1, 2)).sum()),
                       "theta_z_range": (round(th.min(), 1), round(th.max(), 1))})
    return pd.DataFrame(rows)
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json; nb=json.load(open('reproduce_johnson_2018.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if c['cell_type']=='code' and i>33 and any(k in s for k in ('pw[','pw.','ex[','ex.','erp[','ps[','cx[','centres')): print(i, s[:80])
"
```

```
36 rows = []
for tag in ("", "_desc"):
    for sid, r in R.items():
        c = r["
39 cent = fcx2.CENTRES[fcx2.PLV_BANDS]
print("filter centres:", cent.tolist())
rows
42 def desc_pairs(r):
    """Same-hemisphere MTL-frontal pairs after the exclusions
45 units = []
for sid, r in R.items():
    for i, u in enumerate(r["units"]):
```

**Agent**

Now a quick test of the notebook on the two cached subjects, with the loading cells swapped for the saved results.

**Agent calls Bash**

```bash
uv pip install -q -p $TMPDIR/dev/bin/python ipykernel nbconvert nbclient 2>&1 | tail -2; cat > $TMPDIR/mk_test.py <<'PYEOF'
import json, os
nb = json.load(open('reproduce_johnson_2018.ipynb'))
C = nb['cells']
T = os.environ['TMPDIR']
C[2]['source'] = f"import pickle\nfor sid in ['s3', 's8']:\n    R[sid] = pickle.load(open('{T}/' + sid + '_res.pkl', 'rb'))\n"
for i in (3, 4, 5):
    C[i]['source'] = "pass\n"
json.dump(nb, open(f'{T}/test_nb.ipynb', 'w'))
PYEOF
python $TMPDIR/mk_test.py && python -c "
import json; nb=json.load(open('reproduce_johnson_2018.ipynb')); print(''.join(nb['cells'][1]['source']))"
```

```
import time
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from scipy import stats

import fcx2

warnings.filterwarnings("ignore")
pd.set_option("display.width", 220)
pd.set_option("display.max_columns", 60)
pd.set_option("display.max_rows", 400)

started = time.time()
chtab = fcx2.read_channel_table()
summary = fcx2.read_summary_file()
R = {}
```

**Agent calls Bash**

```bash
$TMPDIR/dev/bin/python -m ipykernel install --user --name devfcx >/dev/null 2>&1; timeout 1200 $TMPDIR/dev/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=devfcx --ExecutePreprocessor.timeout=1200 --allow-errors $TMPDIR/test_nb.ipynb --output $TMPDIR/test_out.ipynb 2>&1 | tail -3; python - <<'EOF'
import json, os
nb = json.load(open(os.environ['TMPDIR'] + '/test_out.ipynb'))
for i, c in enumerate(nb['cells']):
    for o in c.get('outputs', []):
        if o.get('output_type') == 'error':
            print('ERR', i, o['ename'], o['evalue'][:300])
EOF
```

```
_validate(nbdict, ref, version, version_minor, relax_add_props)
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 118440 bytes to /tmp/claude-1001/test_out.ipynb
ERR 1 ModuleNotFoundError No module named 'fcx2'
ERR 2 NameError name 'R' is not defined
ERR 7 NameError name 'R' is not defined
ERR 9 NameError name 'R' is not defined
ERR 11 NameError name 'R' is not defined
ERR 13 NameError name 'fcx2' is not defined
ERR 15 NameError name 'R' is not defined
ERR 18 NameError name 'R' is not defined
ERR 21 NameError name 'R' is not defined
ERR 24 NameError name 'chtab' is not defined
ERR 27 NameError name 'R' is not defined
ERR 30 NameError name 'R' is not defined
ERR 33 NameError name 'fcx2' is not defined
ERR 36 NameError name 'R' is not defined
ERR 39 NameError name 'fcx2' is not defined
ERR 42 NameError name 'R' is not defined
ERR 45 NameError name 'R' is not defined
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cp $TMPDIR/test_nb.ipynb ./_test_nb.ipynb && timeout 1200 $TMPDIR/dev/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=devfcx --ExecutePreprocessor.timeout=1200 --allow-errors _test_nb.ipynb --output $TMPDIR/test_out.ipynb 2>&1 | grep -v WARN | tail -1; rm -f _test_nb.ipynb; python - <<'EOF'
import json, os
nb = json.load(open(os.environ['TMPDIR'] + '/test_out.ipynb'))
for i, c in enumerate(nb['cells']):
    for o in c.get('outputs', []):
        if o.get('output_type') == 'error':
            print('ERR', i, o['ename'], o['evalue'][:300])
EOF
```

```
[NbConvertApp] Writing 140571 bytes to /tmp/claude-1001/test_out.ipynb
ERR 11 KeyError 's1'
ERR 42 KeyError "None of [Index(['pre', 'post'], dtype='str', name='interval')] are in the [columns]"
ERR 45 KeyError "None of [Index(['pre', 'post'], dtype='str', name='interval')] are in the [columns]"
ERR 51 ValueError need at least one array to stack
ERR 57 ValueError need at least one array to stack
ERR 58 NameError name 'PM' is not defined
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json, os
nb = json.load(open(os.environ['TMPDIR'] + '/test_out.ipynb'))
for i in (13, 15, 30, 33, 36, 42, 45):
    print(f'##### [{i}]')
    for o in nb['cells'][i].get('outputs', []):
        t = o.get('text') or ''.join(o.get('traceback', []))[-1500:]
        print(''.join(t)[:4000])
EOF
```

```
##### [13]
files: ['circ_corrcl.m', 'cspsi_compute.m', 'dirpac_compute.m', 'erp_compute.m', 'hilbertanalysis.m', 'pac_compute.m', 'pacanalysis.m', 'plv_compute.m', 'plvanalysis.m', 'power_compute.m', 'psi_compute.m', 'psianalysis.m', 'psianalysis_ver0_6.m', 'resamplemtx.m', 'subtracterp.m', 'zbaseline.m']
--- erp_compute.m, lines 44-47
  44  % set up baseline correction
  45  cfgb = [];
  46  cfgb.latency = [0.65 0.85]; % -250 to 50 ms pretrial
  47  cfgb.avgovertime = 'yes';
--- erp_compute.m, lines 74-97
  74  % compute pretrial baseline temporal mean
  75  pretrial = ft_timelockanalysis(cfgf, pretrial); % ERP
  76  pretrial = ft_selectdata(cfgb, pretrial); % average over time
  77  
  78  % compute ERPs
  79  encmain = ft_selectdata(cfgc, encmain); % select trials
  80  encmain = ft_timelockanalysis(cfgf, encmain); % ERP
  81  proc = ft_selectdata(cfgc, proc);
  82  proc = ft_timelockanalysis(cfgf, proc);
  83  
  84  % absolute baseline correction
  85  encmain.trial = encmain.trial - ...
[... 167 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
P='reproduce_johnson_2018.ipynb'
nb=json.load(open(P)); C=nb['cells']
s=''.join(C[42]['source'])
old='''    w = d.pivot_table(index="pair", columns="interval", values=y)
'''
assert old in s
s=s.replace(old, '''    if len(d) == 0:
        return np.nan, np.nan, np.nan
    w = d.pivot_table(index="pair", columns="interval", values=y)
''')
C[42]['source']=s.splitlines(keepends=True)
json.dump(nb, open(P,'w'), indent=1, ensure_ascii=False); open(P,'a').write('\n')
EOF
date -u; cp reproduce_johnson_2018.ipynb $TMPDIR/full_in.ipynb; cp reproduce_johnson_2018.ipynb _full_in.ipynb; (time timeout 4000 $TMPDIR/dev/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=devfcx --ExecutePreprocessor.timeout=4000 --allow-errors _full_in.ipynb --output $TMPDIR/full_out.ipynb) 2>&1 | grep -v WARN | tail -4; rm -f _full_in.ipynb; date -u
```

```
Mon Nov  9 00:49:51 UTC 2026

real	38m6.255s
user	42m39.369s
sys	5m44.647s
Mon Nov  9 01:27:57 UTC 2026
```

**Agent calls Bash**

```bash
ls -la $TMPDIR/full_out.ipynb; python - <<'EOF'
import json, os
nb = json.load(open(os.environ['TMPDIR'] + '/full_out.ipynb'))
for i, c in enumerate(nb['cells']):
    for o in c.get('outputs', []):
        if o.get('output_type') == 'error':
            print('ERR', i, o['ename'], o['evalue'][:300])
for i in (2,3,4,5,11,15):
    print(f'##### [{i}]')
    for o in nb['cells'][i].get('outputs', []):
        print(''.join(o.get('text', ''))[-6000:])
EOF
```

```
-rw-r--r-- 1 runner runner 194492 Nov  9 01:27 /tmp/claude-1001/full_out.ipynb
##### [2]
s1: analysed in 105 s; erp 8, power 41, power_test 43, plv 53, psi 72, pac 105

s2: analysed in 199 s; erp 13, power 54, power_test 59, plv 76, psi 115, pac 199

s3: analysed in 40 s; erp 4, power 13, power_test 15, plv 18, psi 27, pac 40

s4: analysed in 140 s; erp 10, power 41, power_test 44, plv 57, psi 87, pac 140
4 subjects done after 9.6 min

##### [3]
s5: analysed in 228 s; erp 14, power 53, power_test 57, plv 74, psi 112, pac 228

s6: analysed in 315 s; erp 23, power 95, power_test 103, plv 129, psi 205, pac 315
6 subjects done after 20.4 min

##### [4]
s7: analysed in 144 s; erp 12, power 47, power_test 51, plv 64, psi 96, pac 144

[... 86 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py",
 "old_string": "        j9 = d[\"trialinfo\"][:, 4] == 900\n        for name, v in ((\"hg\", ln), (\"erp\", lp)):\n            b = np.stack([v[..., idx == j].mean(axis=-1) for j in range(len(edges) - 1)], axis=-1)\n            jt[(k, name)] = stats.ttest_ind(b[j9], b[~j9], axis=0).statistic.astype(np.float32)",
 "new_string": "        j9 = d[\"trialinfo\"][:, 4] == 900\n        rng = np.random.default_rng(seed_for(f\"jitter|{k}\", sub[\"subject\"]))\n        perms = [rng.permutation(j9) for _ in range(200)]\n        for name, v in ((\"hg\", ln), (\"erp\", lp)):\n            b = np.stack([v[..., idx == j].mean(axis=-1) for j in range(len(edges) - 1)], axis=-1)\n            jt[(k, name)] = stats.ttest_ind(b[j9], b[~j9], axis=0).statistic.astype(np.float32)\n            # null: the same count of electrode bins with |t| > 1.96 per bin, jitter labels permuted\n            jt[(k, name, \"null\")] = np.stack([(np.abs(stats.ttest_ind(b[p], b[~p], axis=0).statistic) > 1.96).sum(axis=0)\n                                              for p in perms]).astype(np.int16)        # (200, bins)"
}
```

```
The file entries/crcns-fcx-2-johnson-2018/fcx2.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/jit_all.py <<'EOF'
import sys, os, pickle, time
sys.path.insert(0, '.')
import fcx2
chtab = fcx2.read_channel_table()
out = {}
for sid in fcx2.SUBJECTS:
    t = time.time()
    ch = chtab[chtab.subject == sid].reset_index(drop=True)
    sub = fcx2.load_subject(sid, ch.label.tolist())
    san = fcx2.sanity_subject(sub)
    out[sid] = {"jitter_t": san["jitter_t"], "edges": san["evoked_edges"], "chans": ch}
    del sub
    print(sid, round(time.time() - t), flush=True)
pickle.dump(out, open(os.environ['TMPDIR'] + '/jit_all.pkl', 'wb'))
EOF
date -u; $TMPDIR/dev/bin/python $TMPDIR/jit_all.py; date -u
```

```
Mon Nov  9 01:29:03 UTC 2026
s1 25
s2 25
s3 18
s4 24
s5 60
s6 66
s7 30
s8 12
s9 24
s10 46
Mon Nov  9 01:34:36 UTC 2026
```

**Agent calls Bash**

```bash
cat > $TMPDIR/jit_an.py <<'EOF'
import pickle, os, numpy as np
D = pickle.load(open(os.environ['TMPDIR'] + '/jit_all.pkl', 'rb'))
edges = D['s1']['edges']; centres = edges[:-1] + 0.025
wins = np.arange(-1.5, 3.0, 0.25)
first = {"pre": (1.8, None), "encmain": (0.0, 1.5), "proc": (-0.3, 1.2)}
for seg in ("pre", "encmain", "proc"):
    for name in ("hg", "erp"):
        obs = sum((np.abs(D[s]['jitter_t'][(seg, name)]) > 1.96).sum(axis=0) for s in D)        # (bins,)
        null = sum(D[s]['jitter_t'][(seg, name, 'null')].astype(int) for s in D)                 # (200, bins)
        nel = sum(D[s]['jitter_t'][(seg, name)].shape[0] for s in D)
        line_p, line_f = [], []
        for w0 in wins:
            m = (centres >= w0) & (centres < w0 + 0.25)
            o = obs[m].sum(); nl = null[:, m].sum(axis=1)
            line_f.append(o / (nel * m.sum())); line_p.append((np.sum(nl >= o) + 1) / 201)
        print(f"{seg:8s}{name:4s} frac " + " ".join(f"{v:.2f}" for v in line_f))
        print(f"{'':12s} p    " + " ".join(f"{v:.2f}" for v in line_p))
print("windows", " ".join(f"{w:+.2f}" for w in wins))
EOF
$TMPDIR/dev/bin/python $TMPDIR/jit_an.py
```

```
pre     hg   frac 0.04 0.05 0.06 0.05 0.05 0.07 0.05 0.06 0.04 0.07 0.05 0.05 0.06 0.06 0.05 0.07 0.05 0.06
             p    0.97 0.71 0.26 0.51 0.41 0.03 0.69 0.40 0.84 0.05 0.34 0.49 0.14 0.37 0.59 0.02 0.45 0.16
pre     erp  frac 0.07 0.05 0.05 0.05 0.06 0.04 0.04 0.06 0.06 0.04 0.05 0.07 0.04 0.05 0.07 0.08 0.07 0.06
             p    0.07 0.47 0.44 0.61 0.43 0.93 0.83 0.32 0.23 0.79 0.61 0.05 0.95 0.62 0.11 0.01 0.03 0.16
encmain hg   frac 0.06 0.06 0.06 0.06 0.05 0.06 0.06 0.05 0.07 0.05 0.06 0.05 0.05 0.08 0.09 0.08 0.09 0.08
             p    0.21 0.39 0.20 0.17 0.59 0.18 0.29 0.55 0.03 0.64 0.23 0.69 0.64 0.00 0.00 0.00 0.00 0.00
encmain erp  frac 0.05 0.05 0.04 0.05 0.06 0.03 0.05 0.08 0.08 0.07 0.07 0.05 0.05 0.08 0.08 0.08 0.11 0.07
             p    0.62 0.54 0.75 0.42 0.24 1.00 0.44 0.01 0.01 0.07 0.01 0.38 0.40 0.01 0.03 0.02 0.00 0.05
proc    hg   frac 0.05 0.06 0.04 0.05 0.05 0.07 0.08 0.07 0.06 0.06 0.06 0.05 0.05 0.06 0.05 0.06 0.05 0.05
             p    0.62 0.10 0.99 0.76 0.45 0.01 0.01 0.05 0.15 0.23 0.11 0.54 0.71 0.25 0.55 0.23 0.48 0.65
proc    erp  frac 0.05 0.05 0.06 0.05 0.05 0.07 0.11 0.12 0.08 0.08 0.05 0.06 0.04 0.05 0.05 0.05 0.06 0.05
             p    0.56 0.56 0.28 0.44 0.40 0.05 0.00 0.00 0.02 0.02 0.57 0.29 0.94 0.69 0.35 0.44 0.20 0.39
windows -1.50 -1.25 -1.00 -0.75 -0.50 -0.25 +0.00 +0.25 +0.50 +0.75 +1.00 +1.25 +1.50 +1.75 +2.00 +2.25 +2.50 +2.75
```

**Agent calls Bash**

```bash
grep -n "WIN_DESC\|_desc\|\"desc\"\|wins = \|pre_sel\|# PLV\|plv = {}\|res\[\"plv\"\]\|for w, (x, sel) in wins.items\|units = \[\]\|res\[\"units\"\]" fcx2.py
```

```
18:  place every window 1.5 s earlier (`WIN_DESC`); ERPs, power and theta PSI are also computed
98:WIN_DESC = {k: (s, t0 + SHIFT_DESC, t1 + SHIFT_DESC) for k, (s, t0, t1) in WIN.items()}
728:    # means). Variants: each trial's own baseline mean subtracted, and the windows of WIN_DESC.
733:    for tag, win in (("", WIN), ("_desc", WIN_DESC)):
737:            if tag == "_desc" and btag:
752:    # the windows of WIN_DESC come from the same filtering pass
753:    _, bsel_d = segment(sub, "base", WIN_DESC)
754:    _, esel_d = segment(sub, "enc", WIN_DESC)
755:    _, psel_d = segment(sub, "post", WIN_DESC)
776:    res["power_z_mean_desc"] = {k: v.mean(axis=0) for k, v in zs_d.items()}
782:    res["pow_enc_desc"] = cluster_test(zs_d["enc"], tic[:, 2], "t", rng, nperm_cluster)
783:    res["pow_post_desc"] = cluster_test(zs_d["post"], tic[:, 3], "F", rng, nperm_cluster)
788:    res["excluded_desc"] = (np.minimum(res["pow_enc_desc"].p_subject, res["pow_post_desc"].p_subject) < 0.05).to_numpy()
798:    _, pre_sel = segment(sub, "pre")
799:    wins = {"pre": (xe["enc"], pre_sel), "post": (xe["proc"], psel)}
811:    # PLV (plv_compute.m bands 1-3 ... 12-20 Hz)
812:    plv = {}
813:    for w, (x, sel) in wins.items():
828:    res["plv"] = plv
836:    for w, (x, sel) in wins.items():
[... 8 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py",
 "offset": 786,
 "limit": 135
}
```

```
786	    excl = (np.minimum(res["pow_enc"].p_subject, res["pow_post"].p_subject) < 0.05).to_numpy()
787	    res["excluded"] = excl
788	    res["excluded_desc"] = (np.minimum(res["pow_enc_desc"].p_subject, res["pow_post_desc"].p_subject) < 0.05).to_numpy()
789	    keep = ~excl
790	
791	    # ---- individual theta peak (M8), reading (a): all kept analysed electrodes
792	    pk = res["enc_time_mean_z"][keep][:, PEAK_BANDS].mean(axis=0)
793	    res["peak_curve_all"] = pk
794	    res["peak_band_all"] = int(PEAK_BANDS[np.argmax(pk)])
795	
796	    # ---- phase measures on ERP-subtracted delay data (subtracterp.m, ncond = 1)
797	    xe = {k: v - v.mean(axis=0, keepdims=True) for k, v in (("enc", xs["enc"]), ("proc", xs["proc"]))}
798	    _, pre_sel = segment(sub, "pre")
799	    wins = {"pre": (xe["enc"], pre_sel), "post": (xe["proc"], psel)}
800	
801	    mtl = np.where((regions == "MTL") & keep)[0]
802	    pairs = {"MTL-MTL": [], "MTL-PFC": [], "MTL-OFC": []}
803	    for a in mtl:
804	        for b in np.where(keep & (hemis == hemis[a]))[0]:
805	            if regions[b] == "MTL" and b > a:
[... 115 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/refactor.py <<'PYEOF'
P = 'fcx2.py'
s = open(P).read()
start = s.index('    excl = (np.minimum(res["pow_enc"].p_subject')
end = s.index('    # theta peak reading (b): phase-directing electrodes only')
new = '''    excl = (np.minimum(res["pow_enc"].p_subject, res["pow_post"].p_subject) < 0.05).to_numpy()
    res["excluded"] = excl
    res["excluded_alt"] = (np.minimum(res["pow_enc_alt"].p_subject, res["pow_post_alt"].p_subject) < 0.05).to_numpy()
    keep = ~excl

    # ---- individual theta peak (M8), reading (a): all kept analysed electrodes
    pk = res["enc_time_mean_z"][keep][:, PEAK_BANDS].mean(axis=0)
    res["peak_curve_all"] = pk
    res["peak_band_all"] = int(PEAK_BANDS[np.argmax(pk)])

    # ---- phase measures on ERP-subtracted delay data (subtracterp.m, ncond = 1), in the main
    # windows (with the main exclusions) and in the code's windows (with that placement's own)
    xe = {k: v - v.mean(axis=0, keepdims=True) for k, v in (("enc", xs["enc"]), ("proc", xs["proc"]))}
    nab = n_amp_bands(fs)
    amp_bands = BANDS[AMP_BANDS[:nab]]
    for tag, win, kp in (("", WIN, keep), ("_alt", WIN_ALT, ~res["excluded_alt"])):
        _, pre_sel = segment(sub, "pre", win)
        _, post_sel = segment(sub, "post", win)
        wins = {"pre": (xe["enc"], pre_sel), "post": (xe["proc"], post_sel)}
        pairs = _make_pairs(regions, hemis, kp)
        res["pairs" + tag] = pairs
        res["plv" + tag] = _plv(wins, pairs, fs)
        res["timing"]["plv" + tag] = time.time() - T0
        psi, cs, keep_th, cs_shuf, keep_shuf = _psi_block(wins, pairs, fs, amp_bands, sid, tag, calibrate=not tag)
        res["psi" + tag], res["cspsi" + tag] = psi, cs
        res["units" + tag] = _make_units(regions, hemis, labels, kp, pairs, cs, keep_th, cs_shuf, keep_shuf, sid, tag)
        res["timing"]["psi" + tag] = time.time() - T0
    pairs, units = res["pairs"], res["units"]

'''
s = s[:start] + new + s[end:]

helpers = '''def _make_pairs(regions, hemis, keep):
    """Same-hemisphere pairs of kept electrodes: MTL-MTL, MTL-PFC and MTL-OFC (PLV section)."""
    pairs = {"MTL-MTL": [], "MTL-PFC": [], "MTL-OFC": []}
    for a in np.where((regions == "MTL") & keep)[0]:
        for b in np.where(keep & (hemis == hemis[a]))[0]:
            if regions[b] == "MTL" and b > a:
                pairs["MTL-MTL"].append((a, b))
            elif regions[b] in ("PFC", "OFC"):
                pairs[f"MTL-{regions[b]}"].append((a, b))
    return pairs


def _plv(wins, pairs, fs):
    """PLV readings per window and pair group (plv_compute.m bands 1-3 ... 12-20 Hz)."""
    plv = {}
    for w, (x, sel) in wins.items():
        A = _filter_chunks(x, fs, sel, BANDS[PLV_BANDS], "complex")
        U = A / np.abs(A)
        out = {}
        for g, pl in pairs.items():
            vals = {"implv": [], "pli": [], "code": []}
            for a, b in pl:
                d = U[:, a] * np.conj(U[:, b])                   # (trials, band, T)
                vals["implv"].append(np.abs(np.imag(d.mean(axis=0))).mean(axis=-1))
                vals["pli"].append(np.abs(np.sign(np.imag(d)).mean(axis=0)).mean(axis=-1))
                dd = np.exp(1j * (np.imag(A[:, a]) - np.imag(A[:, b])))
                vals["code"].append(np.abs(dd.mean(axis=0)).mean(axis=-1))
            out[g] = {k: np.array(v) for k, v in vals.items()}
        plv[w] = out
        del A, U
    return plv


def _psi_block(wins, pairs, fs, amp_bands, sid, tag, calibrate):
    """Theta PSI (M5) and cross-spectral PSI (M6) in the two delay windows, single window
    (mtmfft) and sliding windows, the code's form for the MTL-frontal pairs, and, when
    `calibrate`, the same with the second signal's trials shuffled."""
    psi, cs, keep_th, cs_shuf, keep_shuf = {}, {}, {}, {}, None
    ij = [(a, b) for g in ("MTL-PFC", "MTL-OFC") for a, b in pairs[g]]
    for w, (x, sel) in wins.items():
        env = _filter_chunks(x, fs, sel, amp_bands, "abs")   # filtered on the full segment
        for mode in ("mtmfft", "sliding"):
            rng = np.random.default_rng(seed_for(f"psi|{w}|{mode}{tag}", sid))
            th = theta_fourier(x[..., sel].astype(np.float64), fs, mode)          # (n, ch, 5, w)
            S, PA, PB = cross_spectra(th, th)
            raw, z = psi_z(S, PA[:, None, :], PB[None, :, :], rng)              # (ch, ch)
            psi[(w, mode)] = {"raw": raw, "z": z}
            if mode == "mtmfft":
                psi[(w, "code")] = _psi_code_pairs(th, ij, raw.shape, rng)
            # cross-spectral: theta of each amplitude envelope
            rng = np.random.default_rng(seed_for(f"cspsi|{w}|{mode}{tag}", sid))
            n, nch, nbb, T = env.shape
            the = theta_fourier(env.reshape(n, nch * nbb, T).astype(np.float64), fs, mode)
            the = the.reshape(n, nch, nbb, 5, the.shape[-1])
            Sx = cross_spectra_x(th, the)
            PBx = (np.abs(the) ** 2).mean(axis=(0, 4))                          # (ch, nbb, 5)
            rawx, zx = psi_z(Sx, PA[:, None, None, :], PBx[None, :, :, :], rng)  # (ch, ch, nbb)
            cs[(w, mode)] = {"raw": rawx, "z": zx}
            if mode == "mtmfft":
                keep_th[w] = (th, the)
            if w == "post" and calibrate:
                # calibration: the second signal's trials shuffled against the first's, which
                # removes any trial-by-trial coupling; z should then fall above 1.96 in about
                # 2.5% of pairs
                rng = np.random.default_rng(seed_for(f"psi-shuffle|{mode}", sid))
                perm = rng.permutation(n)
                S0, _, PB0 = cross_spectra(th, th[perm])
                psi[(w, mode, "shuf")] = dict(zip(("raw", "z"), psi_z(S0, PA[:, None, :], PB0[None, :, :], rng)))
                if mode == "mtmfft":
                    psi[(w, "code", "shuf")] = _psi_code_pairs(th, ij, raw.shape, rng, perm)
                the_p = the[perm]
                cs_shuf[mode] = psi_z(cross_spectra_x(th, the_p), PA[:, None, None, :],
                                      PBx[None, :, :, :], rng)[1]
                if mode == "mtmfft":
                    keep_shuf = (th, the_p)
                del the_p
            del the
        del env
    return psi, cs, keep_th, cs_shuf, keep_shuf


def _make_units(regions, hemis, labels, keep, pairs, cs, keep_th, cs_shuf, keep_shuf, sid, tag):
    """Units for cross-spectral directionality and PAC: each kept electrode (phase and
    amplitude from it) and each MTL-frontal pair in both directions, with their mean z and raw
    cross-spectral PSI per window and form."""
    units = []
    for e in np.where(keep)[0]:
        units.append({"system": regions[e], "ph": e, "amp": e})
    for g in ("MTL-PFC", "MTL-OFC"):
        fr = g.split("-")[1]
        for a, b in pairs[g]:
            units.append({"system": f"MTL->{fr}", "ph": a, "amp": b})
            units.append({"system": f"{fr}->MTL", "ph": b, "amp": a})
    extra = [("post_shuf", keep_shuf)] if keep_shuf is not None else []
    for u in units:
        for (w, mode), d in cs.items():
            u[f"z_{w}_{mode}"] = float(d["z"][u["ph"], u["amp"], :].mean())
            u[f"raw_{w}_{mode}"] = float(d["raw"][u["ph"], u["amp"], :].mean())
        u["zf_post_mtmfft"] = cs[("post", "mtmfft")]["z"][u["ph"], u["amp"], :16].copy()
        for mode, zsh in cs_shuf.items():
            u[f"z_post_{mode}_shuf"] = float(zsh[u["ph"], u["amp"], :].mean())
        for w, (th, the) in list(keep_th.items()) + extra:
            rng = np.random.default_rng(seed_for(f"cspsi-code|{w}|{u['ph']}|{u['amp']}{tag}", sid))
            nbb = the.shape[2]
            A = np.repeat(th[:, [u["ph"]]], nbb, axis=1)
            o, zc = psi_code(A, the[:, u["amp"]], rng)
            u[f"z_{w}_code"], u[f"raw_{w}_code"] = float(zc.mean()), float(o.mean())
            if w == "post":
                u["zf_post_code"] = zc[:16].copy()
        if extra:
            u["z_post_code_shuf"] = u.pop("z_post_shuf_code")
            u.pop("raw_post_shuf_code")
        u["ph_label"], u["amp_label"] = labels[u["ph"]], labels[u["amp"]]
        u["hemi"] = hemis[u["ph"]]
    return units


def analyse_subject('''
s = s.replace('def analyse_subject(', helpers, 1)

# frames: main = trial table's placement, alt = the code's windows
old_win = s[s.index('WIN = {"enc": ("encmain", 0.0, 1.5)'):s.index('PAD_S = 7.5')]
s = s.replace(old_win, '''# The deposited code's windows (cfgt.latency in every *_compute.m script).
WIN_CODE = {"enc": ("encmain", 0.0, 1.5), "pre": ("encmain", 0.6, 1.5), "post": ("proc", 0.3, 1.2),
            "base": ("pre", 0.65, 0.85)}
# The same windows placed by the trial table and the descriptor: the first sample of each
# segment (time -1.5 s) is the table's epoch start (encmain at column H, first stimulus onset;
# proc 0.3 s before column I, test cue offset; pre about 0.1 s after column G, 1 s before the
# start screen), so every window lies 1.5 s earlier than the code takes it. The main reading:
# the 900 and 1150 ms delay trials part where this placement puts the first event that depends
# on the delay, in each segment (sanity_subject, "jitter_t").
SHIFT_TABLE = -1.5
WIN = {k: (s, t0 + SHIFT_TABLE, t1 + SHIFT_TABLE) for k, (s, t0, t1) in WIN_CODE.items()}
WIN_ALT = WIN_CODE
''')
# rename the remaining desc pieces (ERP and power) to alt
s = s.replace('("_desc", WIN_DESC)', '("_alt", WIN_ALT)').replace('tag == "_desc"', 'tag == "_alt"')
s = s.replace('the windows of WIN_DESC', 'the windows of WIN_ALT').replace('segment(sub, "base", WIN_DESC)', 'segment(sub, "base", WIN_ALT)')
s = s.replace('segment(sub, "enc", WIN_DESC)', 'segment(sub, "enc", WIN_ALT)').replace('segment(sub, "post", WIN_DESC)', 'segment(sub, "post", WIN_ALT)')
s = s.replace('"power|desc"', '"power|alt"').replace('power_z_mean_desc', 'power_z_mean_alt').replace('pow_enc_desc', 'pow_enc_alt').replace('pow_post_desc', 'pow_post_alt')
s = s.replace('"power-condition-exclusions|desc"', '"power-condition-exclusions|alt"')
open(P, 'w').write(s)
PYEOF
python $TMPDIR/refactor.py && grep -n "desc\|DESC" fcx2.py
```

```
17:  precue delay is M1 reading (a), which the code settles. The trial table and the descriptor
18:  place every window 1.5 s earlier (`WIN_DESC`); ERPs, power and theta PSI are also computed
47:  `t_ftimwin` for mtmfft. The Methods describe sliding 3-cycle windows, which cannot be placed
94:# The same windows placed by the trial table and the descriptor: the first sample of each
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/crcns-fcx-2-johnson-2018/fcx2.py",
 "old_string": "- Segment windows (M1): encoding and precue [0, 1.5] s of data_encmain, precue delay\n  [0.6, 1.5] s of data_encmain, postcue delay [0.3, 1.2] s of data_proc, baseline [0.65, 0.85] s\n  of data_pre. Code: power_compute.m, psi_compute.m, cspsi_compute.m (\"cfgt.latency\"). The\n  precue delay is M1 reading (a), which the code settles. The trial table and the descriptor\n  place every window 1.5 s earlier (`WIN_DESC`); ERPs, power and theta PSI are also computed\n  there, as a variant.",
 "new_string": "- Segment windows (M1): the code (power_compute.m, psi_compute.m, cspsi_compute.m,\n  \"cfgt.latency\") takes encoding and precue as [0, 1.5] s of data_encmain, the precue delay as\n  [0.6, 1.5] s of data_encmain (M1 reading (a)), the postcue delay as [0.3, 1.2] s of data_proc\n  and the baseline as [0.65, 0.85] s of data_pre (`WIN_CODE`). The trial table and the\n  descriptor place each segment's first sample (-1.5 s) at the table's epoch start, which puts\n  the same events 1.5 s earlier: encoding [-1.5, 0], precue [-0.9, 0], postcue [-1.2, -0.3],\n  baseline [-0.85, -0.65] s (`WIN`). The main reading is the table's placement, an assumption\n  resting on the data: the 900 and 1150 ms delay trials part where it puts the first event that\n  depends on the delay, in all three segments, and not where the code's windows put it\n  (sanity_subject). ERPs, power, PLV and both PSI measures are also computed in the code's\n  windows (`WIN_ALT`), as a variant; PAC is computed in the main windows only."
}
```

```
The file entries/crcns-fcx-2-johnson-2018/fcx2.py has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent calls Bash**

```bash
sed -i 's/excluded_desc/excluded_alt/' $TMPDIR/dev.py && $TMPDIR/dev/bin/python $TMPDIR/dev.py s8 2>&1 | tail -12 && $TMPDIR/dev/bin/python -c "
import pickle,os; r=pickle.load(open(os.environ['TMPDIR']+'/s8_res.pkl','rb')); print(sorted(k for k in r if not k.startswith('erp_mean'))); print(len(r['units']), len(r['units_alt']), sorted(r['units_alt'][0]))"
```

```
sanity 2.702558994293213
s8: analysed in 27 s; erp 3, power 10, power_test 12, plv 14, psi 19, plv_alt 21, psi_alt 25, pac 27
z_post_mtmfft 16 sd 0.18 >1.96 0.00 <-1.96 0.00
z_post_sliding 16 sd 0.65 >1.96 0.00 <-1.96 0.00
z_post_code 16 sd 14.55 >1.96 0.25 <-1.96 0.56
z_post_mtmfft_shuf 16 sd 0.22 >1.96 0.00 <-1.96 0.00
z_post_sliding_shuf 16 sd 0.62 >1.96 0.00 <-1.96 0.00
z_post_code_shuf 16 sd 15.54 >1.96 0.38 <-1.96 0.62
z_pre_sliding 16 sd 0.72 >1.96 0.00 <-1.96 0.00
excl 1 desc 2
maxrss GB 0.626472
['chans', 'cspsi', 'cspsi_alt', 'enc_time_mean_z', 'erp_enc', 'erp_enc_alt', 'erp_enc_trial', 'erp_post', 'erp_post_alt', 'erp_post_trial', 'excluded', 'excluded_alt', 'pac', 'pairs', 'pairs_alt', 'peak_band_all', 'peak_band_dir', 'peak_band_dir_code', 'peak_band_dir_sliding', 'peak_curve_all', 'peak_curve_dir', 'peak_curve_dir_code', 'peak_curve_dir_sliding', 'plv', 'plv_alt', 'pow_enc', 'pow_enc_alt', 'pow_post', 'pow_post_alt', 'power_z_mean', 'power_z_mean_alt', 'psi', 'psi_alt', 'sanity', 'subject', 'theta_band_used', 'timing', 'trialinfo', 'units', 'units_alt']
16 13 ['amp', 'amp_label', 'hemi', 'ph', 'ph_label', 'raw_post_code', 'raw_post_mtmfft', 'raw_post_sliding', 'raw_pre_code', 'raw_pre_mtmfft', 'raw_pre_sliding', 'system', 'z_post_code', 'z_post_mtmfft', 'z_post_sliding', 'z_pre_code', 'z_pre_mtmfft', 'z_pre_sliding', 'zf_post_code', 'zf_post_mtmfft']
```

**Agent**

The refactor works on s8: 27 s, against 20 s before. I estimate the full run at about 46 minutes. Now updating the notebook cells for the new frames.

**Agent calls Bash**

```bash
cat > $TMPDIR/edit2.py <<'PYEOF'
import json
P = 'reproduce_johnson_2018.ipynb'
nb = json.load(open(P)); C = nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s): C[i]['source'] = s.splitlines(keepends=True)
def find(prefix):
    hits = [i for i, c in enumerate(C) if c['cell_type'] == 'code' and src(i).startswith(prefix)]
    assert len(hits) == 1, (prefix, hits); return hits[0]

# sanity jitter cell: add the permutation null and the predicted onsets
i = find('edges = R["s1"]')
s = src(i)
old_start = s.index('# per electrode: t of the 900')
old_end = s.index('# the electrode with the largest high-gamma modulation')
s = s[:old_start] + '''# per electrode: t of the 900 against the 1150 ms trials in 50 ms bins (fcx2.sanity_subject),
# pooled over subjects: the fraction of electrode bins with |t| > 1.96 per 250 ms window, and its p
# against 200 permutations of the jitter labels (the same permutation index summed over subjects)
print("\\nPer electrode, 900 against 1150 ms delay trials, in 250 ms windows from -1.5 s")
FIRST = {"pre": ("test cue onset", 1.8, None), "encmain": ("test cue onset", 0.0, 1.5),
         "proc": ("response screen", -0.3, 1.2)}
for seg in ("pre", "encmain", "proc"):
    ev, t_tab, t_code = FIRST[seg]
    print(f"{seg}: first event that depends on the delay, {ev}: {t_tab:+.2f} s by the trial table, "
          + (f"{t_code:+.2f} s by the code's windows" if t_code is not None else "after the segment's end by the code's windows"))
    for name in ("hg", "erp"):
        obs = sum((np.abs(r["sanity"]["jitter_t"][(seg, name)]) > 1.96).sum(axis=0) for r in R.values())
        null = sum(r["sanity"]["jitter_t"][(seg, name, "null")].astype(int) for r in R.values())
        nel = sum(r["sanity"]["jitter_t"][(seg, name)].shape[0] for r in R.values())
        frac, pv = [], []
        for w0 in WINS:
            m = (centres >= w0) & (centres < w0 + 0.25)
            frac.append(obs[m].sum() / (nel * m.sum()))
            pv.append((np.sum(null[:, m].sum(axis=1) >= obs[m].sum()) + 1) / (null.shape[0] + 1))
        print(f"  {name:4s} frac " + " ".join(f"{v:.2f}" for v in frac))
        print(f"  {'':4s} p    " + " ".join(f"{v:.2f}" for v in pv))
print("  windows   " + " ".join(f"{w:+.2f}" for w in WINS))
''' + s[old_end:]
s = s.replace('# per electrode: t of the 900', 'WINS = np.arange(-1.5, 3.0, 0.25)\n# per electrode: t of the 900', 1)
setsrc(i, s)

# ERP
i = find('rows = []\nfor tag, label in (("", "code: trial-mean baseline")')
s = src(i)
s = s.replace('(("", "code: trial-mean baseline"), ("_trial", "variant: per-trial baseline"), ("_desc", "variant: trial table\'s windows"))',
              '(("", "main: trial-mean baseline (code)"), ("_trial", "variant: per-trial baseline"), ("_alt", "variant: code\'s windows"))')
s = s.replace('erp.reading.str.startswith("code")', 'erp.reading.str.startswith("main")')
setsrc(i, s)

# power theta
i = find('TH = [2, 3, 4, 5]')
s = src(i).replace('(("power_z_mean", "code\'s windows"), ("power_z_mean_desc", "trial table\'s windows (1.5 s earlier)"))',
                   '(("power_z_mean", "trial table\'s windows (main)"), ("power_z_mean_alt", "code\'s windows (1.5 s later)"))')
s = s.replace('def zcurve(r, idx, bands, key="power_z_mean"):', 'def zcurve(r, idx, bands, key):')
setsrc(i, s)

# exclusions
i = find('rows = []\nfor tag in ("", "_desc"):')
s = src(i).replace('for tag in ("", "_desc"):', 'for tag in ("", "_alt"):')
s = s.replace('"trial table" if tag else "code"', '"code" if tag else "trial table"')
s = s.replace('''print(ex[(ex.windows == "code") & (ex.null == "p_subject")].to_string(index=False))
print(ex[(ex.windows == "trial table") & (ex.null == "p_subject")].to_string(index=False))
for w in ("code", "trial table"):''', '''print(ex[(ex.windows == "trial table") & (ex.null == "p_subject")].to_string(index=False))
print(ex[(ex.windows == "code") & (ex.null == "p_subject")].to_string(index=False))
for w in ("trial table", "code"):''')
setsrc(i, s)

# PLV
i = find('cent = fcx2.CENTRES[fcx2.PLV_BANDS]')
s = src(i)
s = s.replace('''rows = []
for sid, r in R.items():
    for g in ("MTL-MTL", "MTL-PFC", "MTL-OFC"):
        if len(r["pairs"][g]) == 0:
            continue
        for rd in ("implv", "pli", "code"):
            spec = (r["plv"]["pre"][g][rd].mean(axis=0) + r["plv"]["post"][g][rd].mean(axis=0)) / 2''', '''rows = []
for tag in ("", "_alt"):
  for sid, r in R.items():
    for g in ("MTL-MTL", "MTL-PFC", "MTL-OFC"):
        if len(r["pairs" + tag][g]) == 0:
            continue
        for rd in ("implv", "pli", "code"):
            spec = (r["plv" + tag]["pre"][g][rd].mean(axis=0) + r["plv" + tag]["post"][g][rd].mean(axis=0)) / 2''')
s = s.replace('''            rows.append({"subject": sid, "group": g, "reading": rd, "pairs": len(r["pairs"][g]),''',
              '''            rows.append({"windows": "code" if tag else "table", "subject": sid, "group": g, "reading": rd, "pairs": len(r["pairs" + tag][g]),''')
s = s.replace('''print(pl.drop(columns="spectrum").to_string(index=False))
print(pl.groupby(["reading", "group"]).theta_peak.agg(["sum", "size"]).to_string())
print(pl[pl.reading == "implv"][["subject", "group", "spectrum"]].to_string(index=False))''', '''print(pl[pl.windows == "table"].drop(columns="spectrum").to_string(index=False))
print(pl.groupby(["windows", "reading", "group"]).theta_peak.agg(["sum", "size"]).to_string())
print(pl[(pl.reading == "implv") & (pl.windows == "table")][["subject", "group", "spectrum"]].to_string(index=False))''')
setsrc(i, s)

# PSI theta
i = find('def desc_pairs(r):')
s = src(i)
s = s[s.index('def pair_table'):]
s = s.replace('''def pair_table(key, desc=False):
    rows = []
    for sid, r in R.items():
        pairs = desc_pairs(r) if desc else r["pairs"]
        for g in ("MTL-PFC", "MTL-OFC"):
            for a, b in pairs[g]:
                for w in ("pre", "post"):
                    d = r["psi"][(w, key, "desc") if desc else (w, key)]''', '''def pair_table(key, tag=""):
    rows = []
    for sid, r in R.items():
        for g in ("MTL-PFC", "MTL-OFC"):
            for a, b in r["pairs" + tag][g]:
                for w in ("pre", "post"):
                    d = r["psi" + tag][(w, key)]''')
s = s.replace('''for key, desc in [(k, d) for d in (False, True) for k in ("mtmfft", "sliding", "code")]:
    pt = pair_table(key, desc)''', '''for key, tag in [(k, t) for t in ("", "_alt") for k in ("mtmfft", "sliding", "code")]:
    pt = pair_table(key, tag)''')
s = s.replace('''rows.append({"reading": key + (" / table" if desc else ""), "net": g,''', '''rows.append({"reading": key + (" / code win" if tag else ""), "net": g,''')
assert 'desc' not in s, s
setsrc(i, s)

# cross-spectral
i = find('units = []\nfor sid, r in R.items():')
s = src(i)
s = s.replace('''units = []
for sid, r in R.items():
    for i, u in enumerate(r["units"]):
        units.append({"subject": sid, "uid": f"{sid}-{u['ph']}-{u['amp']}", "pair": f"{sid}-{min(u['ph'], u['amp'])}-{max(u['ph'], u['amp'])}",
                      "idx": i, **{k: v for k, v in u.items() if not k.startswith("zf")}})
U = pd.DataFrame(units)''', '''def unit_frame(tag):
    units = []
    for sid, r in R.items():
        for i, u in enumerate(r["units" + tag]):
            units.append({"subject": sid, "uid": f"{sid}-{u['ph']}-{u['amp']}", "pair": f"{sid}-{min(u['ph'], u['amp'])}-{max(u['ph'], u['amp'])}",
                          "idx": i, **{k: v for k, v in u.items() if not k.startswith("zf")}})
    return pd.DataFrame(units)


U, U_ALT = unit_frame(""), unit_frame("_alt")''')
s = s.replace('''rows = []
for key in ("mtmfft", "sliding", "code"):
    for sname in SYSTEMS:
        d = U[U.system == sname]''', '''rows = []
for key in ["mtmfft", "sliding", "code", "mtmfft / code win", "sliding / code win", "code / code win"]:
    UU = U_ALT if "code win" in key else U
    k0 = key.split(" /")[0]
    for sname in SYSTEMS:
        d = UU[UU.system == sname].rename(columns=lambda c: c.replace(f"_{k0}", f"_{key}") if c.startswith(("z_", "raw_")) and c.endswith(f"_{k0}") else c)''', 1)
s = s.replace('''for key in ("mtmfft", "sliding", "code"):
    for y in ("z", "raw"):''', '''for key in ["mtmfft", "sliding", "code", "mtmfft / code win", "sliding / code win", "code / code win"]:
    for y in ("z", "raw"):''')
setsrc(i, s)

# phase-directing counts
i = find('EXP = ')
s = src(i)
s = s.replace('''for key in ("mtmfft", "sliding", "code"):
    for sname in SYSTEMS:
        d = U[(U.system == sname) & (U[f"z_post_{key}"] > 1.96)]''', '''for key in ["mtmfft", "sliding", "code", "mtmfft / code win", "sliding / code win", "code / code win"]:
    UU = U_ALT if "code win" in key else U
    k0 = key.split(" /")[0]
    for sname in SYSTEMS:
        d = UU[(UU.system == sname) & (UU[f"z_post_{k0}"] > 1.96)]''')
setsrc(i, s)
json.dump(nb, open(P, 'w'), indent=1, ensure_ascii=False); open(P, 'a').write('\n')
print('ok')
PYEOF
python $TMPDIR/edit2.py && grep -c "desc" reproduce_johnson_2018.ipynb
```

```
ok
9
```

**Agent calls Bash**

```bash
grep -n "desc" reproduce_johnson_2018.ipynb | cut -c1-150; python - <<'EOF'
import json
P='reproduce_johnson_2018.ipynb'
nb=json.load(open(P)); C=nb['cells']
for i,c in enumerate(C):
    s=''.join(c['source'])
    if s.startswith('cent = fcx2.CENTRES'):
        a=s.index('for tag in ("", "_alt"):\n'); b=s.index('pl = pd.DataFrame(rows)')
        block=s[a:b].splitlines(keepends=True)
        out=[block[0]]
        for l in block[1:]:
            st=l.lstrip(' '); n=len(l)-len(st)
            if l.startswith('  for sid'): out.append('    '+st)
            elif st.strip(): out.append(' '*(n+4 if n>=4 else n)+st)
            else: out.append(l)
        s=s[:a]+''.join(out)+s[b:]
        c['source']=s.splitlines(keepends=True); print(s)
json.dump(nb, open(P,'w'), indent=1, ensure_ascii=False); open(P,'a').write('\n')
EOF
```

```
21:    "files exist once, under `live/`, which is the published version 0.61 (descriptor of April 4, 2018,\n",
199:    "The descriptor says the derived structures have `fsample: 1000`; s8 and s9 are at 512 Hz, as its\n",
245:    "pretrial\"), which places stimulus onset at 0 s, 1.5 s after the table's column H. The descriptor\n",
250:    "data and the code therefore disagree with the descriptor by 1.5 s on where the events are. The\n",
325:    "time axes of the derived data, as the deposited code does; the descriptor's placement of the\n",
459:    "as its descriptor says. Its response times do not equal the mean over correct trials of the\n",
461:    "ms), although the descriptor says they are \"calculated on all correct trials\"; the paper's\n",
463:    "paper's description (37 ± 13 years, 22 to 69, 7 males). No subject's data appear twice."
1574:    "descriptor place the events 1.5 s earlier and no task-locked response could settle it; the\n",
cent = fcx2.CENTRES[fcx2.PLV_BANDS]
print("filter centres:", cent.tolist())
rows = []
for tag in ("", "_alt"):
    for sid, r in R.items():
        for g in ("MTL-MTL", "MTL-PFC", "MTL-OFC"):
            if len(r["pairs" + tag][g]) == 0:
                continue
            for rd in ("implv", "pli", "code"):
                spec = (r["plv" + tag]["pre"][g][rd].mean(axis=0) + r["plv" + tag]["post"][g][rd].mean(axis=0)) / 2
                peaks = [cent[i] for i in range(1, len(spec) - 1) if spec[i] > spec[i - 1] and spec[i] > spec[i + 1]]
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
$TMPDIR/dev/bin/python $TMPDIR/dev.py s3 2>&1 | grep analysed; python $TMPDIR/mk_test.py && cp $TMPDIR/test_nb.ipynb ./_test_nb.ipynb && timeout 1200 $TMPDIR/dev/bin/jupyter nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=devfcx --ExecutePreprocessor.timeout=1200 --allow-errors _test_nb.ipynb --output $TMPDIR/test_out.ipynb 2>&1 | grep -v WARN | tail -1; rm -f _test_nb.ipynb; python - <<'EOF'
import json, os
nb = json.load(open(os.environ['TMPDIR'] + '/test_out.ipynb'))
for i, c in enumerate(nb['cells']):
    for o in c.get('outputs', []):
        if o.get('output_type') == 'error':
            print('ERR', i, o['ename'], o['evalue'][:300])
for i in (11, 39, 42, 45, 48):
    print(f'##### [{i}]')
    for o in nb['cells'][i].get('outputs', []):
        print(''.join(o.get('text', ''))[-3000:])
EOF
```

```
s3: analysed in 60 s; erp 4, power 24, power_test 25, plv 29, psi 38, plv_alt 41, psi_alt 50, pac 60
[NbConvertApp] Writing 153695 bytes to /tmp/claude-1001/test_out.ipynb
ERR 11 KeyError 's1'
ERR 51 ValueError need at least one array to stack
ERR 57 ValueError need at least one array to stack
ERR 58 NameError name 'PM' is not defined
##### [11]

##### [39]
filter centres: [2.0, 2.75, 3.5, 4.5, 5.5, 6.5, 8.0, 9.5, 11.5, 13.5, 16.0]
windows subject   group reading  pairs  theta_peak               peaks_Hz  max_at_Hz  alpha_over_theta
  table      s3 MTL-MTL   implv      1        True                  [6.5]       6.50          0.191527
  table      s3 MTL-MTL     pli      1        True                  [6.5]       6.50          0.212656
  table      s3 MTL-MTL    code      1        True                  [4.5]      16.00          1.761619
  table      s3 MTL-PFC   implv      4        True                  [6.5]       6.50          0.405374
  table      s3 MTL-PFC     pli      4        True                  [6.5]       6.50          0.425723
  table      s3 MTL-PFC    code      4       False                 [2.75]      16.00          4.579552
  table      s8 MTL-MTL   implv      3       False                  [9.5]       2.00          1.017299
  table      s8 MTL-MTL     pli      3        True       [2.75, 6.5, 9.5]       2.75          0.953003
  table      s8 MTL-MTL    code      3       False                 [11.5]      16.00          1.606554
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
P='reproduce_johnson_2018.ipynb'
nb=json.load(open(P)); C=nb['cells']
for c in C:
    s=''.join(c['source'])
    if 'cal = pd.DataFrame(rows)' in s:
        s=s.replace('print(cal.groupby(["form", "data"]).apply(', 'print(cal[cal.units > 0].groupby(["form", "data"]).apply(')
        c['source']=s.splitlines(keepends=True)
json.dump(nb, open(P,'w'), indent=1, ensure_ascii=False); open(P,'a').write('\n')
EOF
grep -n "runtime_minutes" entry.yaml; sed -i 's/runtime_minutes: 45/runtime_minutes: 50/' entry.yaml; cd  && date -u && python tools/entry.py all entries/crcns-fcx-2-johnson-2018 2>&1 | tail -15; date -u
```

```
14:  runtime_minutes: 45
Mon Nov  9 01:38:57 UTC 2026
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
Installed kernelspec registry-crcns-fcx-2-johnson-2018 in executed/crcns-fcx-2-johnson-2018/.venv/share/jupyter/kernels/registry-crcns-fcx-2-johnson-2018
0 error(s)
pass  reproduce_johnson_2018.ipynb  (2753 s)
Mon Nov  9 02:24:58 UTC 2026
```

**Agent**

The official run passed in 46 minutes (2753 s) with 0 errors. Reading the outputs now.

**Agent calls Bash**

```bash
cd  python - <<'EOF' > $TMPDIR/out.txt
import json
nb = json.load(open('executed/crcns-fcx-2-johnson-2018/reproduce_johnson_2018.ipynb'))
for i, c in enumerate(nb['cells']):
    if c['cell_type'] != 'code': continue
    print(f'##### [{i}]')
    for o in c.get('outputs', []):
        if o.get('output_type') == 'error': print('ERROR', o['ename'], o['evalue'])
        t = o.get('text') or ''
        print(''.join(t))
EOF
wc -l $TMPDIR/out.txt; sed -n '/##### \[11\]/,/##### \[13\]/p' $TMPDIR/out.txt | head -60
```

```
957 /tmp/claude-1001/out.txt
##### [11]
pre: high-gamma amplitude relative to its mean, 900 ms delay trials, 100 ms steps from -1.5 s:
   1.29 0.99 1.00 1.00 1.01 1.00 1.00 1.01 1.00 1.00 1.00 1.00 0.99 0.99 0.99 0.99 0.99 0.99 0.99 1.00 0.99 0.98 0.98 0.98 0.98 0.99 0.99 0.99 0.99 0.99 0.99 0.99 0.99 1.00 1.00 1.00 1.00 0.99 0.99 1.00 1.00 1.00 1.00 1.01 1.00
   1150 ms delay trials:
   1.30 0.99 1.00 1.00 0.99 1.00 1.00 1.00 0.99 1.00 0.99 0.99 0.99 0.99 1.00 0.99 0.99 0.99 0.99 1.00 1.00 0.99 0.98 0.99 0.99 0.99 1.00 1.00 0.98 0.99 0.99 0.99 1.00 0.99 0.99 0.99 0.99 0.99 0.98 0.99 0.99 0.99 0.99 0.99 0.99
   evoked RMS over channels relative to its mean:
   0.90 0.90 1.01 0.82 0.99 1.15 1.15 0.94 0.89 0.92 1.01 1.02 1.10 1.07 1.03 0.97 0.92 1.05 0.92 0.98 1.10 1.21 1.13 1.13 1.02 1.04 1.09 1.04 1.08 1.10 1.18 0.94 1.01 0.97 0.98 0.86 0.86 1.03 0.99 0.94 0.95 0.89 1.00 0.87 0.86
   range of the high-gamma curves 0.980 to 1.304; largest 900 vs 1150 difference 0.023 at 2.48 s
encmain: high-gamma amplitude relative to its mean, 900 ms delay trials, 100 ms steps from -1.5 s:
   1.28 1.00 1.00 0.99 0.99 0.98 0.99 0.99 1.00 0.99 0.99 1.00 0.99 0.99 1.00 1.00 1.00 1.00 1.00 1.00 0.99 1.00 1.01 1.00 1.01 1.01 1.00 1.00 1.00 0.99 1.00 1.00 0.99 0.99 0.99 0.98 0.98 0.98 0.98 0.99 0.99 0.99 0.99 0.99 1.01
   1150 ms delay trials:
   1.28 1.00 1.00 0.99 0.99 0.99 0.99 0.99 1.00 1.00 0.99 0.99 0.99 0.99 1.00 1.00 1.00 1.00 0.99 0.99 0.99 0.99 0.99 0.99 0.99 1.00 0.99 0.99 0.99 1.00 0.99 0.99 0.99 0.99 0.99 0.99 0.98 0.99 1.00 0.99 0.99 0.99 0.99 0.99 0.99
   evoked RMS over channels relative to its mean:
   0.94 0.92 1.04 1.19 1.16 1.25 1.10 1.05 1.01 1.02 1.07 1.10 1.18 0.91 1.03 0.99 0.97 0.84 0.87 1.04 0.97 1.01 0.98 0.90 1.00 0.93 0.87 1.01 0.97 0.91 0.99 0.85 0.92 0.92 1.03 0.90 0.89 1.02 1.04 1.13 1.02 1.06 0.99 1.01 1.04
   range of the high-gamma curves 0.978 to 1.284; largest 900 vs 1150 difference 0.022 at 0.68 s
proc: high-gamma amplitude relative to its mean, 900 m
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/##### \[21\]/,/##### \[39\]/p' $TMPDIR/out.txt | grep -v "^ *s[0-9]* *\(MTL\|PFC\|OFC\) " | head -150
```

```
##### [21]
--- all 120 trials (a): mean and SD over subjects
       acc               rt         
      mean    std      mean      std
cond                                
1     0.90  0.035  1744.146  581.949
2     0.92  0.086  1237.449  663.860
3     0.89  0.090  1292.217  625.457

  elogit: {'spatial_vs_identity_p': np.float64(0.0228), 'temporal_vs_identity_p': np.float64(0.6603), 'three_level_chi2': 5.8321, 'three_level_p': 0.0541, 'numeric_slope': np.float64(0.0617), 'numeric_z': np.float64(0.394), 'numeric_p': np.float64(0.6936), 'numeric_F': np.float64(0.1552), 'numeric_p_F128': np.float64(0.6966)}
  rt: {'spatial_vs_identity_p': np.float64(0.0), 'temporal_vs_identity_p': np.float64(0.0), 'three_level_chi2': 26.5562, 'three_level_p': 0.0, 'numeric_slope': np.float64(-225.9646), 'numeric_z': np.float64(-3.5113), 'numeric_p': np.float64(0.0004), 'numeric_F': np.float64(12.3294), 'numeric_p_F128': np.float64(0.0015)}
--- kept trials (b): mean and SD over subjects
        acc               rt         
       mean    std      mean      std
cond                                 
1     0.908  0.049  1756.292  587.745
2     0.921  0.082  1224.706  667.893
3     0.904  0.094  1296.786  629.930

  elogit: {'spatial_vs_identity_p': np.float64(0.1599), 'temporal_vs_identity_p': np.float64(0.5002), 'three_level_chi2': 1.9765, 'three_level_p': 0.3722, 'numeric_slope': np.float64(0.0979), 'numeric_z': np.float64(0.6651), 'numeric_p': np.float64(0.506), 'numeric_F': np.float64(0.4423), 'numeric_p_F128': np.float64(0.5114)}
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/##### \[36\]/,/##### \[45\]/p' $TMPDIR/out.txt | sed -n '/p_electrode: /,$p' | grep -v "^ *s[0-9]* *MTL-\(MTL\|PFC\|OFC\) *\[" | head -150
```

```
trial table windows, p_electrode: 57 electrodes ({'OFC': 25, 'PFC': 23, 'MTL': 9}) in 10 subjects; expected 8 (5 PFC, 3 OFC) in 4
code windows, p_subject: 12 electrodes ({'PFC': 6, 'OFC': 5, 'MTL': 1}) in 5 subjects; expected 8 (5 PFC, 3 OFC) in 4
code windows, p_electrode: 69 electrodes ({'PFC': 38, 'OFC': 28, 'MTL': 3}) in 9 subjects; expected 8 (5 PFC, 3 OFC) in 4

##### [39]
filter centres: [2.0, 2.75, 3.5, 4.5, 5.5, 6.5, 8.0, 9.5, 11.5, 13.5, 16.0]
windows subject   group reading  pairs  theta_peak               peaks_Hz  max_at_Hz  alpha_over_theta
  table      s1 MTL-PFC   implv      8        True             [5.5, 9.5]       2.00          1.087557
  table      s1 MTL-PFC     pli      8        True             [5.5, 9.5]       2.00          1.099862
  table      s1 MTL-PFC    code      8        True      [2.75, 6.5, 11.5]       2.75          0.999914
  table      s1 MTL-OFC   implv      5       False                  [8.0]       2.00          0.973915
  table      s1 MTL-OFC     pli      5       False                  [8.0]       2.00          0.924153
  table      s1 MTL-OFC    code      5        True       [2.75, 4.5, 8.0]       8.00          1.015522
  table      s2 MTL-MTL   implv     21        True             [3.5, 5.5]       3.50          0.706073
  table      s2 MTL-MTL     pli     21        True                  [3.5]       3.50          0.713320
  table      s2 MTL-MTL    code     21       False                 [11.5]      11.50          1.138217
  table      s2 MTL-PFC   implv     28       False      [2.75, 8.0, 13.5]       2.75          0.956866
  table      s2 MTL-PFC     pli     28       False      [2.75, 8.0, 13.5]       2.75          0.950792
  table      s2 MTL-PFC    code     28        True            [4.5, 11.5]      11.50          1.084985
  table      s3 MTL-MTL   implv      1        True                  [6.5]       6.50          0.191527
[... 129 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/##### \[45\]/,/##### \[51\]/p' $TMPDIR/out.txt | head -150
```

```
##### [45]
           reading   system  units  subjects response  pre_mean_z  post_mean_z  pre_above_1.96  pre_frac_above  post_minus_pre        F      p
            mtmfft      MTL     34        10        z     -0.3290      -0.3040               0          0.0000          0.0249   0.0546 0.8167
            mtmfft      MTL     34        10      raw     -0.3290      -0.3040               0          0.0000          0.0186   3.2792 0.0793
            mtmfft      PFC    115         9        z     -0.2333      -0.2972               0          0.0000         -0.0639   1.8215 0.1798
            mtmfft      PFC    115         9      raw     -0.2333      -0.2972               0          0.0000         -0.0009   0.5893 0.4443
            mtmfft      OFC     98         9        z     -0.6037      -0.6224               0          0.0000         -0.0187   0.0794 0.7786
            mtmfft      OFC     98         9      raw     -0.6037      -0.6224               0          0.0000         -0.0027   0.9585 0.3300
            mtmfft MTL->PFC    170         9        z     -0.1228      -0.0796               0          0.0000          0.0432   1.5943 0.2084
            mtmfft MTL->PFC    170         9      raw     -0.1228      -0.0796               0          0.0000          0.0006   1.1572 0.2836
            mtmfft PFC->MTL    170         9        z     -0.2741      -0.2505               0          0.0000          0.0236   0.2720 0.6027
            mtmfft PFC->MTL    170         9      raw     -0.2741      -0.2505               0          0.0000         -0.0033   3.1731 0.0767
            mtmfft MTL->OFC    289         7        z     -0.1419      -0.1507               0          0.0000         -0.0088   0.0791 0.7787
            mtmfft MTL->OFC    289         7      raw     -0.1419      -0.1507               0          0.0000          0.0001   0.0286 0.8658
            mtmfft OFC->MTL    289         7        z     -0.1451      -0.1109               0          0.0000          0.0342   1
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/##### \[48\]/,$p' $TMPDIR/out.txt | sed -n '16,200p' | cut -c1-260
```

```
sliding OFC->MTL      2       115         False         1                  5                                                                               {'s9': 2}
              code      MTL     14        13          True         5                  8                                          {'s2': 5, 's10': 3, 's4': 2, 's5': 2, 's7': 2}
              code      PFC     49        52          True         9                  8      {'s7': 13, 's6': 8, 's2': 7, 's5': 6, 's9': 5, 's1': 3, 's4': 3, 's3': 2, 's8': 2}
              code      OFC     47        38         False         8                  8             {'s10': 19, 's5': 11, 's6': 8, 's1': 3, 's7': 3, 's2': 1, 's3': 1, 's9': 1}
              code MTL->PFC    105        56         False         9                  9 {'s7': 22, 's5': 20, 's2': 17, 's4': 16, 's9': 14, 's6': 11, 's1': 3, 's3': 1, 's8': 1}
              code PFC->MTL     76        85         False         9                  9    {'s2': 19, 's7': 19, 's4': 13, 's5': 8, 's9': 6, 's6': 4, 's1': 3, 's3': 3, 's8': 1}
              code MTL->OFC    189        93         False         7                  5                    {'s10': 133, 's5': 32, 's9': 10, 's6': 9, 's1': 2, 's7': 2, 's4': 1}
              code OFC->MTL    170       115         False         6                  5                              {'s10': 141, 's5': 19, 's1': 3, 's6': 3, 's7': 2, 's9': 2}
 mtmfft / code win      MTL      0        13         False         0                  8                                                                                      {}
 mtmfft / code win      PFC      0        52         False         0                  8                                                                                      {}
 mtmfft / code win      OFC      0        38         False         0                  8                                                                                      {}
 mtmfft / code win MTL->PFC      0        56         False         0       
[... 137 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas; grep -n "verifications" -A60 schemas/attempt*.json | head -120; grep -ln "verifications:" attempts/*.yaml | head -3
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
334:    "verifications": {
335-      "type": "array",
336-      "items": {
337-        "type": "object",
338-        "additionalProperties": false,
339-        "required": [
340-          "date",
341-          "kind",
342-          "by",
343-          "results"
344-        ],
345-        "properties": {
346-          "date": {
347-            "type": "string",
348-            "format": "date"
349-          },
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 394,420p schemas/attempt.schema.json; grep -n "verifications:" -A14 attempts/000005-yu-2016-01.yaml | head -30; grep -n "phase-directing-counts" -A40 claims/crcns-fcx-2/*.yaml | grep -n "criterion" -A10 | head -14; date -u
```

```
}
          },
          "reviewed": {
            "description": "What was reviewed, e.g. a commit, when the attempt changed afterwards.",
            "type": "string"
          }
        }
      }
    },
    "findings": {
      "description": "What the attempt found about the dataset itself, whatever the outcomes. These roll up into the per-dataset report.",
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "kind",
          "statement"
        ],
        "properties": {
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 505,512p claims/crcns-fcx-2/*.yaml; sed -n 542,570p claims/crcns-fcx-2/*.yaml | grep -A8 criterion; cat entries/crcns-fcx-2-johnson-2018/README.md
```

```
- quantity: subjects with phase-directing MTL to OFC pairs
    value: 5
    tolerance: 0
  criterion: Postcue mean cross-spectral PSI z > 1.96 (M6). Each count within 10%. The subject
    counts the Methods give (8 MTL, 8 PFC, 8 OFC, 9 MTL to PFC, 9 PFC to MTL, 5 MTL to OFC, 5 OFC
    to MTL) are reported; two are listed as expected values and must match exactly. Reproduced
    when at least five of the seven electrode and pair counts are within tolerance; partially
    reproduced for three or four. The 5 of 7 is a choice made here.
  criterion: Peak as in M8. The paper does not say which electrodes are averaged; readings (a) all
    of a subject's analysed electrodes, (b) only the electrodes entering the PAC analysis
    (phase-directing). Counts of subjects must match exactly (10% of a count of 2 or 3 is below
    one). Reproduced when, under one reading, all four counts match. The paper gives no
    per-subject assignment, so partial agreement is judged on the counts alone; partially
    reproduced when the sum over the four bands of the smaller of the paper's and the attempt's
    count is at least 7 (a threshold chosen here).
- id: pac-mtl-spatial
  statement: Within the MTL, theta PAC was greater for spatial than identity information, with
# Johnson et al. (2018) from CRCNS fcx-2

Tests the findings of [Johnson et al. (2018)](https://doi.org/10.1371/journal.pbio.2004274) on
[... 32 more lines not kept]
```

**Agent**

Writing the notebook's markdown now: method notes, conclusions and summary.

**Agent calls Bash**

```bash
cd entries/crcns-fcx-2-johnson-2018; python -c "
import json; nb=json.load(open('reproduce_johnson_2018.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='markdown': print(i, ''.join(c['source'])[:90].replace('\n',' '))"
```

```
0 # Reproducing Johnson et al. (2018) from CRCNS fcx-2  **Paper.** Johnson EL, Adams JN, Sol
6 ## Data check
8 The descriptor says the derived structures have `fsample: 1000`; s8 and s9 are at 512 Hz, 
10 The three derived segments of a trial are cut from one continuous recording: placed by the
12 Pooled over subjects, the high-gamma amplitude (70 to 150 Hz) and the evoked response show
14 `erp_compute.m` (lines 84 to 88) subtracts `nanmean(pretrial.trial)`, the mean over trials
16 The accuracies of `docs/summary_file.csv` equal those of the per-trial tables over all 120
17 ## behavior-proficient  > All ten subjects performed the task well above chance, with accu
19 **Result: reproduced.** Over all 120 trials (reading a) accuracy runs from 0.792 to 0.967,
20 ## behavior-no-difficulty-difference  > Accuracy and correct-trial response time did not d
22 **Result: reproduced, resting on two assumptions.** Under reading (c), the one the criteri
23 ## electrode-counts  > After bipolar rereferencing there were 254 electrodes, 36 MTL, 116 
25 **Result: reproduced.** The channel table lists 36 MTL, 116 PFC and 102 OFC electrodes (25
26 ## correct-trial-counts  > The final data held on average 100 correct trials per subject, 
28 **Result: reproduced.** The kept trials hold on average 100.9 correct trials per subject (
29 ## erp-no-condition-difference  > ERPs did not differ between identity, spatial and tempor
31 **Result: not reproduced.** With the code's subject-wide null, one electrode of 254 (in s5
32 ## power-theta-sustained  > Task-induced power showed sustained theta band (3 to 7 Hz) act
34 **Result: not reproduced.** No subject has a region-average theta z above 1.96 over half t
35 ## power-condition-exclusions  > Power did not differ between conditions at any time and f
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/md.py <<'PYEOF'
import json
P = 'reproduce_johnson_2018.ipynb'
nb = json.load(open(P)); C = nb['cells']
def setmd(i, start, text):
    s = ''.join(C[i]['source']); assert C[i]['cell_type'] == 'markdown' and s.startswith(start), (i, s[:60])
    C[i]['source'] = text.strip('\n').splitlines(keepends=True)
def replace_in(i, old, new):
    s = ''.join(C[i]['source']); assert old in s, (i, old[:50]); C[i]['source'] = s.replace(old, new).splitlines(keepends=True)

# header: data set description and the claims table
replace_in(0, "(`data_derived.mat`: segments `pre`, `encmain` and `proc` with 1.5 s of data on each side, and a\ntrial table per segment)",
           "(`data_derived.mat`: segments `pre`, `encmain` and `proc`, each 4.5 s long with a time axis from -1.5\nto 3 s, and a trial table per segment)")
s = ''.join(C[0]['source'])
tab_start = s.index('| claim | tested |')
s = s[:tab_start] + '''Every window is placed by the trial table and the descriptor (the main reading), 1.5 s earlier
on the derived time axes than the deposited code places it; the data check below shows why. ERPs,
power, PLV and both PSI measures are also run with the code's windows.

| claim | tested | rests on an assumption |
|---|---|---|
| behavior-proficient | yes | |
| behavior-no-difficulty-difference | yes | numeric coding of condition; response time from summary_file.csv; accuracy model on subject-level logits |
| electrode-counts | yes | |
| correct-trial-counts | yes | |
| erp-no-condition-difference | yes | baseline as erp_compute.m subtracts it (trial mean) |
| power-theta-sustained | yes | |
| power-condition-exclusions | yes | |
| plv-theta-peak | yes | |
| psi-theta-shift | yes | window placement of the trial table |
| crossspectral-shift | yes | |
| phase-directing-counts | yes | |
| crossspectral-equal-strength | blocked (methods_underspecified) | |
| theta-peak-bands | yes | |
| pac-* (8 claims) | blocked (methods_underspecified) | |
'''
C[0]['source'] = s.splitlines(keepends=True)

setmd(10, 'The three derived segments', '''
The three derived segments of a trial are cut from one continuous recording: placed by their
`sampleinfo`, their overlapping samples are identical (largest difference 0) in every subject. In
nine subjects the first sample of `encmain` is the trial table's column H ("encoding and pre-cue
delay epoch start"), the first sample of `proc` is 0.3 s before column I ("post-cue delay epoch
start") and the first sample of `pre` is about 0.1 s after column G ("pretrial epoch start, 1000 ms
before trial start"; 98 to 108 samples at 1 kHz, 51 at 512 Hz). In s10 the offsets are not whole samples and vary over trials (the table's columns
for s10 are not on the derived data's sample grid; for two trials `pre` is 114 samples after G), so
for s10 the table does not place the derived segments exactly. In every subject `trialinfo` is the
same in the three segments and equals the trial table's columns, except s10, where the
trial-table check fails as printed above.

This bears on where time 0 is. Each derived segment runs from -1.5 s to 3.0 s, and its first sample
(-1.5 s) is the table's epoch start. The analysis code takes encoding as [0, 1.5] s of `encmain`, the
postcue delay as [0.3, 1.2] s of `proc` and the baseline as [0.65, 0.85] s of `pre` ("-250 to 50 ms
pretrial"), which places stimulus onset at 0 s, 1.5 s after the table's column H. The descriptor
places stimulus onset at column H itself, 1.5 s earlier, and the table's columns agree with the
task's timing (H minus G is 1.9 s, the 1 s fixation, 800 ms start screen and 100 ms fixation; I
minus H is 600 ms plus the delay plus the 800 ms test cue). While preparing the first run, a
derived trial of s8 was compared with the monopolar data in `data_primary.mat` (not run here, as it
streams the primary files): the bipolar `CL_02` and `BR_03` traces equal the difference of
adjacent contacts from sample H on, so `sampleinfo` indexes the primary data as the table does.
The check below decides between the two placements from the data.
''')
setmd(12, 'Pooled over subjects', '''
Pooled over all channels, the high-gamma amplitude (70 to 150 Hz) and the evoked response show no
task-locked modulation large enough to place the events (the curves stay within a few percent of
their mean apart from the first bin, the edge of the segment). The per-electrode test of the 900
against the 1150 ms delay trials does place them. The two groups can only differ from the first
event whose time depends on the delay. In `proc` the ERPs part from -0.25 s to 0.75 s (fraction of
electrode bins with |t| > 1.96 of 0.07 to 0.12, p 0.05 to below 0.005 against 200 permutations),
which is where the trial table puts the response screen (-0.3 s), and not at 1.2 s, where the
code's windows put it (p 0.29 to 0.94 from 1.0 to 1.75 s); high gamma parts at -0.25 to 0.25 s (p
0.01 to 0.05). In `encmain` the ERPs part from 0.25 s (p 0.01 at 0.25, 0.5 and 1.0 s), after the
test cue at 0 s by the table and before 1.5 s, where the code puts it. In `pre` they part at 2.25
to 2.5 s (p 0.01 and 0.03), after the test cue at 1.8 s by the table; by the code's windows `pre`
holds no event that depends on the delay. So the data are consistent with the trial table's
placement and not with the code's, and every window below is placed by the table: encoding
[-1.5, 0] s and the precue delay [-0.9, 0] s of `encmain`, the postcue delay [-1.2, -0.3] s of
`proc` and the baseline [-0.85, -0.65] s of `pre`. The encoding window then starts at the first
sample of `encmain`, so its first few hundred ms carry the filters' edge effects. ERPs, power, PLV
and both PSI measures are also computed with the code's windows. The electrode with the largest
high-gamma range per subject is printed for reference; in 9 of 10 subjects its peak is the last bin
(2.98 s), the segment's edge.
''')
setmd(16, 'The accuracies of', '''
The accuracies of `docs/summary_file.csv` equal those of the per-trial tables over all 120 trials,
as its descriptor says. Its response times do not equal the mean over correct trials of the
per-trial tables in 7 of 10 subjects (they do in s6, s8 and s9; for s1, identity, 1948 against 2348
ms), although the descriptor says they are "calculated on all correct trials"; the paper's
condition means (1659, 1335, 1475 ms) are those of `summary_file.csv`. No other summary of the
trial tables tried here gives them either (medians, all trials, kept trials, other subjects'
rows, blocks of 40 trials, trial type): 9 of 30 values are matched, all by the mean over correct
trials of s6, s8 and s9. Age and sex match the paper's description (37 ± 13 years, 22 to 69, 7
males). No subject's data appear twice.
''')
setmd(22, '**Result: reproduced, resting on two assumptions.**', '''
**Result: reproduced, resting on two assumptions.** Under reading (c), the one the criterion
judges, neither model finds a condition effect on the data whose condition means are the paper's:
accuracy gives F(1,28) = 0.16, p = 0.70 over all trials (0.44, p = 0.51 over kept trials), and the
response times of `summary_file.csv` give F(1,28) = 2.41, p = 0.13, against the paper's F < 2.55,
p > 0.12. The accuracy F is above the paper's bound of 0.10, though far from an effect. The outcome
rests on the numeric coding of condition, which the criterion states as an assumption, and on
judging response time on `summary_file.csv`, whose values none of the trial-table summaries above
reproduces for 7 of 10 subjects: with the trial tables' response times, (c) finds an effect
(F(1,28) = 12.33, p = 0.0015 over all trials; 11.48, p = 0.0021 over kept trials). The condition
means are within the paper's SDs (accuracy 0.900, 0.920, 0.890; response time 1659, 1335, 1475 ms
from `summary_file.csv` and 1744, 1237, 1292 ms from the trial tables). Under the readings reported
but not judged, response time differs by condition in both sources (summary_file.csv 3-level p =
0.0076, spatial against identity p = 0.0018), and accuracy over all trials differs between spatial
and identity (p = 0.023) though not under the 3-level term (p = 0.054).
''')
setmd(29, '## erp-no-condition-difference', '''
## erp-no-condition-difference

> ERPs did not differ between identity, spatial and temporal conditions in any electrode, over
> encoding, precue or postcue intervals.

The test is run per subject as `erp_compute.m` does (all of a subject's analysed electrodes in one
test, so the null is the largest cluster over the subject's electrodes), and per electrode (the
Methods' "clustered per electrode") as a variant. The baseline subtracted is the trial mean of
each trial's baseline mean, as `erp_compute.m` does it (lines 84 to 88, quoted above); each trial's
own baseline mean is a variant, and so are the code's windows.
''')
setmd(31, '**Result: not reproduced.** With the code', '''
**Result: not reproduced, resting on the baseline of the code.** With the subject-wide null and the
code's baseline, one electrode of 254 (s9, FORA_11, encoding t test, cluster p = 0.036) has a
significant cluster, and the criterion allows none; with the code's windows one electrode does too
(s5, OFG14). Subtracting each trial's own baseline mean leaves no electrode significant under the
subject-wide null, which the criterion would call reproduced. With a per-electrode null 27, 22 and
13 electrodes have a significant cluster (code's baseline, per-trial baseline, code's windows),
against 25.4 expected by chance over two tests, so the effect is no larger than chance.
''')
setmd(32, '## power-theta-sustained', ''.join(C[32]['source']).replace(
    "Time\npoints: the 31 points of encoding and precue (0 to 1.5 s) and the 19 of the postcue delay, at 50 ms.",
    "Time\npoints: the 31 points of encoding and precue and the 19 of the postcue delay, at 50 ms, in the\ntrial table's windows and, as a variant, the code's."))
setmd(34, '**Result: not reproduced.** No subject', '''
**Result: not reproduced.** In the trial table's windows the region-average theta z is above 1.96
over half the time points in 1 of 10 subjects for MTL, 0 of 9 for PFC and 0 of 9 for OFC, and no
subject shows MTL alpha below -1.96 over half the time points (0 of 10). Per electrode, 3 of 36 MTL,
4 of 116 PFC and 8 of 102 OFC electrodes meet the theta rule. In the code's windows the counts are
0, 0 and 0 subjects (1, 1 and 11 electrodes) and 0 of 10 for alpha. All 254 electrodes have some z
above 1.96 above 16 Hz (239 in the code's windows).
''')
setmd(37, '**Result: not reproduced.** The code', '''
**Result: not reproduced.** In the trial table's windows the subject-wide null finds 7 electrodes
(2 MTL, 1 PFC, 4 OFC) in 4 subjects (s1, s6, s8, s10), against 8 (5 PFC, 3 OFC) in 4; in the code's
windows it finds 12 (6 PFC, 5 OFC, 1 MTL) in 5 subjects. The per-electrode null finds many more (57
and 69). The 7 are excluded from the analyses that follow, which leaves 34 MTL, 115 PFC and 98 OFC
electrodes (the code's windows exclude their own 12).
''')
setmd(40, '**Result: reproduced.**', '''
**Result: reproduced.** In the trial table's windows, the imaginary PLV (reading a) has a local
maximum in 3 to 7 Hz in 4 of 8 subjects for MTL to MTL pairs, 7 of 9 for MTL to PFC and 5 of 7 for
MTL to OFC; the phase-lag index gives 6 of 8, 8 of 9 and 5 of 7. In the code's windows the imaginary
PLV gives 7 of 9, 8 of 9 and 4 of 7. The rule asks for one subject per group, a weak test; the peaks
are often one of several local maxima, and the largest value is in 3 to 7 Hz in fewer subjects
(column max_at_Hz).
''')
setmd(41, '## psi-theta-shift', '''
## psi-theta-shift

> Theta-band PSI showed frontal-to-MTL leads during the precue delay and shifted toward MTL leads (a
> bidirectional network) after the test cue, for MTL to PFC and MTL to OFC pairs.

Readings of the spectral step: sliding 3-cycle windows, as M5 of the claims file gives the
Methods (main; at 3 Hz the 1 s window runs into the zero padding of the 900 ms segment), the code's
single Hanning window (`mtmfft`, `psi_compute.m`), and the code's own form of PSI (`psianalysis.m`,
per-trial PSI against a null of trial-mean coherency). Readings of M7: the response is the PSI z or
the raw PSI. Each in the trial table's windows and in the code's ("/ code win"). Positive PSI means
the MTL leads. The calibration table gives each form's postcue z with the second electrode's trials
shuffled, which removes any trial-by-trial coupling.
''')
setmd(43, '**Result: not reproduced.** With the PSI of the Methods and the code', '''
**Result: not reproduced, resting on the window placement.** With sliding windows in the trial
table's windows, neither part holds in either network: precue mean z is 0.25 (MTL-PFC) and 0.01
(MTL-OFC), with fewer pairs below -1.96 than above (45 against 55, 82 against 87), and postcue does
not exceed precue (MTL-PFC raw p = 0.27; MTL-OFC raw PSI falls, p < 0.0001). The code's single
window gives part (2) for MTL-PFC on raw PSI only (p = 0.014, while the z falls), with MTL-OFC raw
PSI falling (p = 0.001), which the criterion would call partial. In the code's windows, sliding
windows give part (1) in both networks and part (2) for MTL-OFC on raw PSI only (p = 0.027), also
partial, and the single window gives neither. The code's own form of PSI gives both parts in both
networks in the code's windows and part of them in the table's, but it is not calibrated: with
trials shuffled 57% of pairs pass z > 1.96 (z SD 44), as many as on the real data (57%). The
sliding-window z is also too wide (SD 2.3 with trials shuffled, 24% above 1.96), which bears on
part (1) only; the single window is near nominal (SD 0.92, 2.2% above). The pair counts are 170 and
289 (expected 172 and 303, within tolerance).
''')
setmd(44, '## crossspectral-shift', '''
## crossspectral-shift

> Theta phase to amplitude directionality (cross-spectral PSI) was absent in the precue delay and
> shifted to theta phase leading amplitude after the test cue, within MTL, PFC and OFC and in all four
> interregional directions.

Readings: the PSI of the Methods (Nolte et al. 2008) from sliding 3-cycle windows (M5, main) and
from the code's single window, and the code's own form of PSI as a variant; M7 response z or raw;
each in the trial table's windows and in the code's. The calibration table below gives each form's
postcue z with the amplitude electrode's trials shuffled against the phase electrode's.
''')
setmd(46, '**Result: not reproduced.** With the PSI of the Methods no precue', '''
**Result: not reproduced.** With the PSI of the Methods and sliding windows, at most 1% of precue
units per system pass z > 1.96 (part 2 holds), but postcue exceeds precue at p < 0.05 in 1 of 7
systems (OFC to MTL) on z and on raw PSI, and MTL to OFC falls. The single window gives 0 of 7 on z
and 1 of 7 on raw PSI; the code's form 3 of 7, with 36% to 46% of precue units above 1.96. In the
code's windows the counts are 1, 2 and 2 of 7. No reading reaches the four systems that partial
needs. The models hold 34 MTL, 115 PFC and 98 OFC electrodes (expected 36, 111 and 99, all within
tolerance). Calibration: with trials shuffled, the code's form passes 57% of units (z SD 23), as
many as on the real data (56%); the Methods' forms pass 0% (single window) and 0.1% (sliding).
''')
setmd(49, '**Result: not reproduced.** With the PSI of the Methods no electrode', '''
**Result: not reproduced.** With the PSI of the Methods and sliding windows the postcue counts are
0 MTL, 0 PFC, 0 OFC, 0 MTL to PFC, 1 PFC to MTL, 3 MTL to OFC and 2 OFC to MTL (0 of 7 within 10%);
the single window selects none. The code's form gives 14, 49, 47, 105, 76, 189 and 170 (expected
13, 52, 38, 56, 85, 93, 115), 2 of 7 within 10%, with MTL electrodes in 5 subjects and MTL to OFC
pairs in 7 (expected 8 and 5); in the code's windows 1 of 7. The code's form passes as many units
with trials shuffled (57%) as on the real data, and its rates (36% to 65% per system) are of the
order of the paper's (31% to 49%), so its counts are not evidence of phase direction.
''')
setmd(50, '## crossspectral-equal-strength', '''
## crossspectral-equal-strength

> Among phase-directing pairs, the strength of theta phase directionality did not differ across
> amplitude frequencies or between the MTL to frontal and frontal to MTL directions.

**Blocked (methods_underspecified).** The claim is about the phase-directing pairs. The Methods'
PSI selects 0 MTL to PFC pairs and 1 PFC to MTL pair (sliding windows; none with the single
window), too few for the model. The code's form selects 57% of pairs with trials shuffled, against
the 2.5% its z > 1.96 threshold implies, so it does not select phase-directing pairs, and no
selection with a defensible basis is left. The model on the code's selection is shown below as
a variant, not judged. Frequency (16 levels) is within pair, direction between pairs. With random
intercepts and every pair having all 16 frequencies, the mixed model's tests of frequency and
frequency x direction are the within-pair F tests computed by `fcx2.within_unit_anova`; the
direction main effect is tested on the pair means with a subject random intercept.
''')
setmd(52, '**Result: not reproduced.** On the pairs', '''
**Result: blocked.** On the pairs the code's form selects (not judged), frequency x direction is
significant in both networks (p = 2e-05 and 0.00019), frequency in MTL-OFC (p = 2e-09) and
direction in both (p = 0.020 and 0.0057).
''')
setmd(53, '## theta-peak-bands', ''.join(C[53]['source']) + '''
Reading (b) is shown for the electrodes of the Methods' PSI (single window and sliding windows) and
of the code's form.
''')
setmd(55, '**Result: not reproduced.** Over all analysed', '''
**Result: not reproduced.** Over all analysed electrodes (reading a) the maxima are at 1.5-4 Hz in 4
subjects, 3-6 Hz in 3, 2-5 Hz in 1, 5-8 Hz in 1 and 6-10 Hz in 1: 5 subjects peak outside the
paper's four bands, and the overlap with the paper's counts is 4 of 10 (partial needs 7). For
reading (b) the Methods' single-window PSI selects no electrodes, its sliding-window PSI selects
electrodes in 3 subjects (overlap 0 of 10), and the code's form gives an overlap of 4 of 10. The
power curves are flat in most subjects (z mostly within -0.9 to 2.2; s9 up to 5.5), so the maxima
are weak.
''')
setmd(56, '## PAC (claims', '''
## PAC (claims pac-mtl-spatial to pac-mtl-ofc-direction)

**All eight PAC claims are blocked (methods_underspecified).** They are about the theta-phase
directing electrodes and pairs. The Methods' PSI selects 0 MTL, 0 PFC, 0 OFC, 0 MTL to PFC, 1 PFC to
MTL, 3 MTL to OFC and 2 OFC to MTL units (sliding windows; none with the single window), too few for
any model, and the code's form, which selects enough, passes as many units with trials shuffled
(57%) as on the real data, against the 2.5% its threshold implies. The models below run on the
code's selection and are shown as a variant, not judged.

PAC z is computed for every unit that is phase-directing under the single-window PSI or the code's
form, in the trial table's postcue window. Readings of the surrogate: (a) amplitudes permuted across
trials (code), (b) amplitude bands shuffled within trials. Models as in M10, computed as within-unit
F tests (`fcx2.within_unit_anova`); a direction main effect on unit means with a subject random
intercept.
''')
setmd(59, '**Result: none of the eight PAC claims', '''
**Result: blocked, all eight claims.** On the code's selection (not judged) none of the eight
patterns appears under either surrogate reading: the MTL spatial condition effect is p = 0.56 (a),
the frontal and PFC to MTL models have condition effects below 0.05/7 (PFC spatial condition x
frequency p = 8.3e-05, PFC to MTL spatial condition p = 0.0004), the MTL to PFC condition effects are
p = 0.23 (spatial) and 0.61 (temporal), the MTL to OFC spatial condition effect is p = 0.18, and the
direction models have effects below 0.05/15 in every network and model.
''')
setmd(60, '## Summary', '''
## Summary

Outcomes are in the attempt record: 5 claims reproduced (behaviour, electrode and trial counts, PLV
peak), 7 not reproduced and 9 blocked. The analysis follows the claims file and, for details it
lacks, the paper's Methods and the analysis code deposited with the data. The main differences from
the paper's method: the windows are placed by the trial table, 1.5 s earlier on the derived time
axes than the deposited code places them, because the 900 and 1150 ms delay trials part where the
table puts the delay-dependent events and not where the code does; the code's windows are run as a
variant. The phase-directing units on which crossspectral-equal-strength and the eight PAC claims
rest cannot be selected: the Methods' PSI selects at most 3 per system, and the code's form selects
as many units with trials shuffled as on the real data. The behaviour claim is judged with
condition as one numeric term, as the amended claims file says, on the response times of
`summary_file.csv`, whose condition means are the paper's; the trial tables' response times differ
in 7 of 10 subjects, no summary of them reproduces the file's values, and they would show a
condition effect. The mixed models use random intercepts.

What was found about the data set: the trial table and the derived time axes disagree with the
deposited code's windows by 1.5 s; the response times of `summary_file.csv` do not follow from the
trial tables in 7 of 10 subjects; s10's trial table is not on the derived sample grid; s8 and s9 are
at 512 Hz, not the 1000 Hz the descriptor gives; and the deposited PSI and PAC scripts depart from
the Methods (PSI without the conjugate and with a null of another statistic; PAC scripts that cannot
run as given).

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.
''')
json.dump(nb, open(P, 'w'), indent=1, ensure_ascii=False); open(P, 'a').write('\n')
print('ok')
PYEOF
python $TMPDIR/md.py
```

```
ok
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
P='reproduce_johnson_2018.ipynb'
nb=json.load(open(P)); C=nb['cells']
fixes = [
 ("partial, and the single window gives neither. The code's own form of PSI gives both parts in both\nnetworks in the code's windows and part of them in the table's, but it is not calibrated:",
  "partial, and the single window gives part (1) in one network and part (2) in neither. The code's\nown form of PSI gives both parts in both networks in the code's windows, and part (1) and part (2)\nin one network each in the table's (MTL-OFC postcue above precue, p = 0.0028 on z), but it is not\ncalibrated:"),
 ("the code's form 3 of 7, with 36% to 46% of precue units above 1.96. In the\ncode's windows the counts are 1, 2 and 2 of 7.",
  "the code's form 3 of 7, with 36% to 47% of precue units above 1.96. In the\ncode's windows the most any reading gives is 1 (single window), 2 (sliding) and 2 (code's form) of 7."),
 ("its rates (36% to 65% per system)", "its rates (41% to 65% per system)"),
 ("(fraction of\nelectrode bins with |t| > 1.96 of 0.07 to 0.12, p 0.05 to below 0.005 against 200 permutations)",
  "(fraction of\nelectrode bins with |t| > 1.96 of 0.07 to 0.12, p from 0.05 down to 0.005, the smallest 200\npermutations can give)"),
 ("(p 0.29 to 0.94 from 1.0 to 1.75 s)", "(p 0.29 to 0.94 in the windows from 1.0 to 2.0 s)"),
]
for old, new in fixes:
    hit = 0
    for c in C:
        s = ''.join(c['source'])
        if old in s:
            c['source'] = s.replace(old, new).splitlines(keepends=True); hit += 1
    assert hit == 1, old[:60]
json.dump(nb, open(P,'w'), indent=1, ensure_ascii=False); open(P,'a').write('\n')
print('ok')
EOF
grep -c "0.0028" $TMPDIR/out.txt
```

```
ok
1
```

**Agent calls Bash**

```bash
date -u; python - <<'EOF'
import nbformat, json
P='reproduce_johnson_2018.ipynb'
nb = json.load(open(P))
print(nb['nbformat'], nb['nbformat_minor'], sum('id' in c for c in nb['cells']), len(nb['cells']))
EOF
```

```
Mon Nov  9 02:28:25 UTC 2026
4 5 60 62
```

**Agent**

It's 02:28, so there's time to write the record before the final run. First, adding ids to the two new cells.

**Agent calls Bash**

```bash
python - <<'EOF'
import json, uuid
P='reproduce_johnson_2018.ipynb'
nb=json.load(open(P))
for c in nb['cells']:
    if 'id' not in c: c['id'] = uuid.uuid4().hex[:8]
json.dump(nb, open(P,'w'), indent=1, ensure_ascii=False); open(P,'a').write('\n')
EOF
cd  && git diff --stat
```

```
entries/crcns-fcx-2-johnson-2018/entry.yaml        |   2 +-
 entries/crcns-fcx-2-johnson-2018/fcx2.py           | 409 +++++++++----
 .../reproduce_johnson_2018.ipynb                   | 653 ++++++++++++++-------
 3 files changed, 727 insertions(+), 337 deletions(-)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']
print(o.get('required'), list(o['properties']))
print(o['properties']['blocked_by'])
print(list(s['properties']))
EOF
```

```
['claim', 'outcome'] ['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'proposed']
{'description': 'Required when outcome is blocked.', 'enum': ['data_missing', 'metadata_insufficient', 'methods_underspecified', 'data_unreadable', 'too_large', 'not_runnable', 'other']}
['schema_version', 'id', 'dataset', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
```

**Agent calls Bash**

```bash
git log -1 --format=%cd --date=short e04867e3b1; grep -n "by:\|reviewed:" attempts/000005-yu-2016-01.yaml | head -4; head -30 transcripts/crcns-fcx-2/verifier-1.md | cut -c1-200
```

````
2026-11-09
162:  blocked_by: metadata_insufficient
225:  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
227:  reviewed: The handover of the first run, the executed notebook with the conclusions and summary
316:  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
# crcns-fcx-2 · verifier-1 · run 42536254025

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Re

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 260
drwxr-xr-x 6 runner runner    4096 Nov  9 00:19 .
drwxr-xr-x 7 runner runner    4096 Nov  9 00:19 ..
[... 15 more lines not kept]
````

**Agent**

Writing the attempt record now.

**Agent calls Bash**

```bash
cat > $TMPDIR/rec_outcomes.yaml <<'EOF'
outcomes:
- claim: behavior-proficient
  outcome: reproduced
  notebook: reproduce_johnson_2018.ipynb
  output: claim:behavior-proficient
  measured:
  - 0.792
  - 0.967
  notes: >-
    Over all 120 trials (reading a) accuracy runs from 0.792 (s5) to 0.967 (s2), every subject in
    0.711 to 1.0. Over the trials kept in the derived data (reading b) it runs from 0.792 to 1.000,
    also within tolerance. The trial tables give the same accuracies as docs/summary_file.csv.
- claim: behavior-no-difficulty-difference
  outcome: reproduced
  assumed: true
  notebook: reproduce_johnson_2018.ipynb
  output: claim:behavior-no-difficulty-difference
  measured:
  - 0.900
  - 0.920
  - 0.890
  - 1659
  - 1335
  - 1475
  notes: >-
    Judged on reading (c) of the amended criterion, condition as one numeric term (identity 1,
    spatial 2, temporal 3) on 30 subject-condition values, F the squared t of the slope with p from
    F(1,28). Accuracy (empirical logit) gives F(1,28) = 0.16, p = 0.70 over all trials and 0.44, p =
    0.51 over kept trials; the paper gives F < 0.10, p > 0.75, so the effect is absent here too but
    the F is above the paper's bound. Response time from docs/summary_file.csv, whose condition
    means and SDs are the paper's (1659 +- 701, 1335 +- 574, 1475 +- 734 ms), gives F(1,28) = 2.41,
    p = 0.13, against the paper's F < 2.55, p > 0.12. The outcome rests on two assumptions: the
    numeric coding, which the criterion states, and judging response time on summary_file.csv.
    With the trial tables' response times (condition means 1744, 1237, 1292 ms, also within the
    paper's SDs) reading (c) finds an effect (F(1,28) = 12.33, p = 0.0015 over all trials; 11.48, p
    = 0.0021 over kept trials), and the outcome would be not reproduced. The revision searched for
    the source of the file's response times among summaries of the trial tables (means and medians
    over correct, all or kept trials, other subjects' rows, blocks of 40 trials, trial type): 9 of
    30 values are matched, all by the mean over correct trials of s6, s8 and s9, and none of the
    other 7 subjects' values. Reported, not judged: under (a) and (b) response time differs by
    condition in both sources (summary_file.csv spatial against identity p = 0.0018, 3-level p =
    0.0076; trial tables p < 0.001), and accuracy over all trials differs between spatial and
    identity (p = 0.023) but not under the 3-level term (p = 0.054; 0.37 over kept trials). What the
    answer changed. The first run judged the claim on readings (a) and (b), found a response-time
    effect under both and recorded not reproduced, and asked whether the numeric reading should be
    named (questions/crcns-fcx-2.yaml). The reader amended the criterion to judge on (c), on the
    printed F(1,28), and kept (a) and (b) as reported. Under (c) the outcome is reproduced, with
    assumed set because it depends on the response-time source.
  deviations:
  - >-
    Accuracy enters the logit model as the empirical logit of each subject and condition, log((k +
    0.5) / (n - k + 0.5)), in a linear mixed model on 30 rows, as some subjects are at 100% in a
    condition; the paper does not specify its logit model further.
  - >-
    The response times of the trial tables differ from those of summary_file.csv in 7 of 10
    subjects, and no summary of the trial tables tried gives the file's values for those 7. Both
    were tested. The outcome is judged on summary_file.csv, as an assumption: its condition means
    and SDs are the ones the paper prints (Results, paragraph 2), so it holds the values the paper's
    models were fitted to, while the trial tables' means are not the paper's.
  - >-
    The F of reading (c) is the squared t of the condition slope in a REML linear mixed model with a
    subject random intercept (statsmodels), with p from F(1,28), the residual degrees of freedom
    the criterion names; MATLAB's fitlme, which the criterion cites, was not run.
- claim: electrode-counts
  outcome: reproduced
  notebook: reproduce_johnson_2018.ipynb
  output: claim:electrode-counts
  measured:
  - 36
  - 116
  - 102
  - 9
  - 7
  notes: >-
    docs/summary_channel_analysis.csv lists 36 MTL, 116 PFC and 102 OFC bipolar channels (254), all
    present in the derived data. MTL and PFC share a hemisphere in 9 subjects, MTL and OFC in 7. Per
    subject 3.6 +- 2.0 (1 to 7) MTL, 11.6 +- 8.3 (4 to 28 in 9 subjects) PFC and 10.2 +- 14.4 (1 to
    47 in 9 subjects) OFC, as the paper gives them.
- claim: correct-trial-counts
  outcome: reproduced
  notebook: reproduce_johnson_2018.ipynb
  output: claim:correct-trial-counts
  measured:
  - 100.9
  - 32.9
  - 34.8
  - 33.2
  - 10.2
  notes: >-
    From the trialinfo of the derived data. Per subject 100.9 +- 7.3 correct trials, 32.9 +- 3.3
    identity (26 to 37), 34.8 +- 3.7 spatial (28 to 39), 33.2 +- 2.7 temporal (28 to 37) and 10.2 +-
    8.1 incorrect (0 to 25), the paper's ranges exactly.
- claim: erp-no-condition-difference
  outcome: not_reproduced
  assumed: true
  notebook: reproduce_johnson_2018.ipynb
  output: claim:erp-no-condition-difference
  notes: >-
    With the code's subject-wide cluster null (all of a subject's electrodes in one test, as
    erp_compute.m runs it) and the code's baseline, 1 of 254 electrodes has a significant cluster in
    the trial table's windows (s9 FORA_11, encoding t test, p = 0.036), and the criterion allows
    none; in the code's windows 1 does too (s5 OFG14). Subtracting each trial's own baseline mean
    leaves 0 electrodes significant under the subject-wide null, which would be reproduced, so the
    outcome rests on the baseline as the code subtracts it. With a per-electrode null 27, 22 and 13
    electrodes are significant (code's baseline, per-trial baseline, code's windows), against 25.4
    expected by chance over two tests. The effect is small and isolated, but the criterion is no
    electrode.
  deviations:
  - &timeaxis >-
    Assumed, the windows placed by the trial table and the descriptor (encoding [-1.5, 0] s and the
    precue delay [-0.9, 0] s of encmain, postcue [-1.2, -0.3] s of proc, baseline [-0.85, -0.65] s of
    pre), 1.5 s earlier than the deposited code's latencies ([0, 1.5], [0.6, 1.5], [0.3, 1.2], [0.65,
    0.85]). The first sample of each derived segment is the table's epoch start, and the 900 and 1150
    ms delay trials part where the table puts the first delay-dependent event in each segment (proc
    ERPs from -0.25 to 0.75 s, p down to 0.005 against 200 permutations, around the response screen
    at -0.3 s) and not where the code's windows put it (proc 1.0 to 2.0 s, p 0.29 to 0.94). The
    code's windows are run as a variant for ERPs, power, PLV and both PSI measures.
  - >-
    The baseline subtracted is the mean over trials of each trial's baseline mean, as erp_compute.m
    does (lines 84 to 88, nanmean(pretrial.trial)); the claims file's "subtracting the temporal mean
    of the baseline" is also read per trial, as a variant.
  - >-
    FieldTrip's filters and cluster test are reimplemented in Python (fir1 design, two-pass,
    zero padding to 7.5 s; cluster sums, 1000 permutations, p doubled for the two-tailed t test).
- claim: power-theta-sustained
  outcome: not_reproduced
  notebook: reproduce_johnson_2018.ipynb
  output: claim:power-theta-sustained
  notes: >-
    Baseline-z power averaged over trials (code zbaseline.m). In the trial table's windows the
    region-average theta z is above 1.96 over half of the 50 encoding and delay time points in 1 of
    10 subjects for MTL, 0 of 9 for PFC and 0 of 9 for OFC; per electrode 3 of 36 MTL, 4 of 116 PFC
    and 8 of 102 OFC meet the rule. MTL alpha is below -1.96 over half the time points in 0 of 10
    subjects (2 of 36 electrodes). In the code's windows the counts are 0, 0 and 0 subjects (1, 1
    and 11 electrodes) and 0 of 10 for alpha. All 254 electrodes have some z above 1.96 above 16 Hz
    (239 in the code's windows; reported, not judged).
  deviations:
  - *timeaxis
- claim: power-condition-exclusions
  outcome: not_reproduced
  notebook: reproduce_johnson_2018.ipynb
  output: claim:power-condition-exclusions
  measured:
  - 7
  - 1
  - 4
  - 4
  notes: >-
    In the trial table's windows the code's subject-wide null finds 7 electrodes (1 PFC, 4 OFC, 2
    MTL) in 4 subjects (s1, s6, s8, s10), against 8 (5 PFC, 3 OFC) in 4; in the code's windows 12 (6
    PFC, 5 OFC, 1 MTL) in 5 subjects. A per-electrode null finds 57 and 69. The measured values are
    total, PFC, OFC and subjects in the trial table's windows. The z and raw readings give the same
    test, as the z is an affine map of power shared by all trials. The 7 are excluded from the later
    analyses, leaving 34 MTL, 115 PFC and 98 OFC electrodes.
  deviations:
  - *timeaxis
- claim: plv-theta-peak
  outcome: reproduced
  notebook: reproduce_johnson_2018.ipynb
  output: claim:plv-theta-peak
  notes: >-
    Imaginary PLV (reading a), averaged over time and the two delays, in the trial table's windows:
    a local maximum at 3.5 to 6.5 Hz in 4 of 8 subjects for MTL-MTL, 7 of 9 for MTL-PFC and 5 of 7
    for MTL-OFC pairs; the phase-lag index (reading b) gives 6 of 8, 8 of 9 and 5 of 7. In the
    code's windows the imaginary PLV gives 7 of 9, 8 of 9 and 4 of 7. The rule needs one subject per
    group, a weak test; the largest value of the spectrum is often outside theta, and theta is often
    one of several local maxima. The alpha synchrony is not judged.
  deviations:
  - *timeaxis
- claim: psi-theta-shift
  outcome: not_reproduced
  assumed: true
  notebook: reproduce_johnson_2018.ipynb
  output: claim:psi-theta-shift
  measured:
  - 170
  - 289
  notes: >-
    Judged with the PSI of the Methods (Nolte, trial-averaged cross-spectrum, frequencies of one
    signal shuffled for the null) from sliding 3-cycle windows, as M5 gives it, in the trial
    table's windows. Neither part holds in either network: precue mean z is 0.25 (MTL-PFC) and 0.01
    (MTL-OFC), with 45 against 55 and 82 against 87 pairs below -1.96 and above 1.96, and postcue does
    not exceed precue (MTL-PFC raw p = 0.27; MTL-OFC raw PSI falls, p < 0.0001). Other readings. The
    code's single window gives part (2) for MTL-PFC on raw PSI only (p = 0.014) with MTL-OFC raw PSI
    falling (p = 0.001), which the criterion calls partial. In the code's windows sliding windows
    give part (1) in both networks and part (2) for MTL-OFC on raw PSI only (p = 0.027), also
    partial, and the single window gives part (2) in neither. The code's own form of PSI gives both
    parts in both networks in the code's windows and part (1) and part (2) in one network each in
    the table's, but with trials shuffled it passes 57% of pairs (z SD 44), as many as on the real
    data, so it is not used. The sliding-window z is also too wide (SD 2.3 with trials shuffled),
    which bears on part (1) only; the single window is near nominal (SD 0.92, 2.2% above 1.96). The
    outcome rests on the window placement: in the code's windows the claims file's sliding reading
    would be partial. The pair counts are 170 and 289 (expected 172 and 303).
  deviations:
  - >-
    The sliding 3-cycle windows of M5 cannot be placed inside a 900 ms segment at 3 Hz (a 1 s
    window); here they run into the zero padding of the 4 s segment. The code's single Hanning
    window over the segment (psi_compute.m, FieldTrip mtmfft, which ignores t_ftimwin) is a variant,
    and so is the code's own form of PSI (psianalysis.m, conjugate added), which averages per-trial
    PSI and z-scores it against a null built from trial-averaged coherency.
  - >-
    The mixed model with random intercepts for subject and pair is computed as the within-pair F
    test of interval (equal for two intervals per pair), with all pairs after the 7 exclusions.
  - *timeaxis
- claim: crossspectral-shift
  outcome: not_reproduced
  notebook: reproduce_johnson_2018.ipynb
  output: claim:crossspectral-shift
  measured:
  - 34
  - 115
  - 98
  notes: >-
    With the PSI of the Methods from sliding windows in the trial table's windows, at most 1% of
    precue units per system pass z > 1.96 (part 2 holds), but postcue exceeds precue at p < 0.05 in
    1 of 7 systems (OFC to MTL) on z and on raw PSI, and MTL to OFC falls (p = 0.0035 on z). The
    single window gives 0 of 7 on z and 1 of 7 on raw PSI, and the code's form 3 of 7, with 36% to
    47% of precue units above 1.96. In the code's windows the most any reading gives is 1 (single
    window), 2 (sliding) and 2 (code's form) of 7. No reading reaches the four systems partial
    needs. With trials shuffled the code's form passes 57% of units (z SD 23) and the Methods' forms
    0% and 0.1%. The models hold 34 MTL, 115 PFC and 98 OFC electrodes (expected 36, 111, 99) and
    170 and 289 pairs.
  deviations:
  - >-
    Cross-spectral PSI is judged with the sliding windows of M5 (running into the zero padding at
    the lowest frequencies, as for psi-theta-shift); the code's single window and the code's form
    are variants.
  - *timeaxis
- claim: phase-directing-counts
  outcome: not_reproduced
  notebook: reproduce_johnson_2018.ipynb
  output: claim:phase-directing-counts
  measured:
  - 0
  - 0
  - 0
  - 0
  - 1
  - 3
  - 2
  - 0
  - 1
  notes: >-
    With the PSI of the Methods from sliding windows in the trial table's windows the postcue counts
    are 0 MTL, 0 PFC, 0 OFC, 0 MTL to PFC, 1 PFC to MTL, 3 MTL to OFC and 2 OFC to MTL (0 of 7 within
    10%), with directing MTL electrodes in 0 subjects and MTL to OFC pairs in 1; the single window
    selects none. The code's form gives 14, 49, 47, 105, 76, 189 and 170 (expected 13, 52, 38, 56,
    85, 93, 115), 2 of 7 within 10%, with MTL electrodes in 5 subjects and MTL to OFC pairs in 7
    (expected 8 and 5); in the code's windows 1 of 7. The code's form passes as many units with
    trials shuffled (57%) as on the real data (56%), and its rates per system (41% to 65%) are of
    the order of the paper's (31% to 49%), so its counts are not evidence of phase direction. The
    measured values are those of the sliding-window reading.
  deviations:
  - *timeaxis
- claim: crossspectral-equal-strength
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_johnson_2018.ipynb
  output: claim:crossspectral-equal-strength
  notes: >-
    The claim is about the phase-directing pairs, and none can be selected with a defensible basis.
    The Methods' PSI selects 0 MTL to PFC and 1 PFC to MTL pair (sliding windows) or none (single
    window), too few for the model (also too few units under the claim's own rule). The code's
    form selects 57% of pairs with trials shuffled, against the 2.5% its z > 1.96 threshold implies,
    so by the protocol's rule on chance levels its procedure is not the paper's stated one. On the
    code's selection (not judged; 105 MTL to PFC and 76 PFC to MTL, 189 MTL to OFC and 170 OFC to
    MTL pairs) frequency x direction is significant in both networks (p = 2e-05 and 0.00019),
    frequency in MTL-OFC (p = 2e-09) and direction in both (p = 0.020 and 0.0057). Which form of PSI
    selected the paper's pairs is asked of the authors under findings.
  deviations:
  - *timeaxis
- claim: theta-peak-bands
  outcome: not_reproduced
  notebook: reproduce_johnson_2018.ipynb
  output: claim:theta-peak-bands
  measured:
  - 1
  - 3
  - 0
  - 1
  notes: >-
    In the trial table's windows, over all analysed electrodes (reading a), the maxima of the 6
    filters fall at 1.5-4 Hz in 4 subjects, 3-6 Hz in 3, 2-5 Hz in 1, 5-8 Hz in 1 and 6-10 Hz in 1;
    5 subjects peak outside the paper's four bands and the overlap with its counts is 4 of 10
    (partial needs 7). For reading (b) the Methods' single-window PSI selects no electrodes, its
    sliding-window PSI selects electrodes in 3 subjects (overlap 0 of 10), and the code's form gives
    an overlap of 4 of 10. The curves are flat in most subjects (trial-, time- and electrode-averaged
    z mostly within -0.9 to 2.2; s9 up to 5.5). The measured values are the counts at 2-5, 3-6, 4-7
    and 5-8 Hz under reading (a).
  deviations:
  - The paper's visual confirmation of the peaks is not reproducible and is left out.
  - *timeaxis
- claim: pac-mtl-spatial
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_johnson_2018.ipynb
  output: claim:pac-mtl-spatial
  notes: >-
    &pacblock The PAC claims are about the theta-phase directing electrodes and pairs. The Methods'
    PSI selects 0 MTL, 0 PFC, 0 OFC, 0 MTL to PFC, 1 PFC to MTL, 3 MTL to OFC and 2 OFC to MTL units
    (sliding windows; none with the single window), too few for the models. The code's form, which
    selects enough, passes as many units with trials shuffled (57%) as on the real data, against
    the 2.5% its threshold implies, so it does not select phase-directing units and no defensible
    selection is left. Which form selected the paper's units is asked of the authors under findings.
    On the code's selection (not judged), in the trial table's postcue window: MTL spatial condition
    p = 0.56 (surrogate a), spatial below identity.
  deviations:
  - &pacmodel >-
    PAC as computed for the variant: the individual theta band of reading (a) of theta-peak-bands
    (a 1.5-4 Hz or 6-10 Hz maximum mapped to 2-5 or 5-8 Hz, an assumption), per condition with the
    condition's trial mean removed (the code's subtracterp.m selects the temporal trials by column
    5 == 2, which no trial meets; the Methods' condition 3 is used). Mixed models with random
    intercepts computed as the within-unit F tests of the balanced 2 x 16 x 19 design; the direction
    main effect on unit means with a subject random intercept.
  - *timeaxis
- claim: pac-frontal-no-condition
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_johnson_2018.ipynb
  output: claim:pac-frontal-no-condition
  notes: >-
    Blocked for the reason given under pac-mtl-spatial (no defensible selection of phase-directing
    units). On the code's selection (not judged; 49 PFC and 47 OFC electrodes) the PFC spatial model
    has a condition x frequency effect below 0.05/7 (p = 8.3e-05, surrogate a).
  deviations:
  - *pacmodel
  - *timeaxis
- claim: pac-mtl-pfc-spatial
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_johnson_2018.ipynb
  output: claim:pac-mtl-pfc-spatial
  notes: >-
    Blocked for the reason given under pac-mtl-spatial. On the code's selection (not judged; 105 MTL
    to PFC pairs) the spatial condition effect is p = 0.23 (surrogate a).
  deviations:
  - *pacmodel
  - *timeaxis
- claim: pac-mtl-pfc-temporal
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_johnson_2018.ipynb
  output: claim:pac-mtl-pfc-temporal
  notes: >-
    Blocked for the reason given under pac-mtl-spatial. On the code's selection (not judged; 105 MTL
    to PFC pairs) the temporal condition effect is p = 0.61 (surrogate a), temporal below identity.
  deviations:
  - *pacmodel
  - *timeaxis
- claim: pac-pfc-mtl-no-condition
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_johnson_2018.ipynb
  output: claim:pac-pfc-mtl-no-condition
  notes: >-
    Blocked for the reason given under pac-mtl-spatial. On the code's selection (not judged; 76 PFC
    to MTL pairs) the spatial condition effect is p = 0.0004 (surrogate a), below 0.05/7.
  deviations:
  - *pacmodel
  - *timeaxis
- claim: pac-mtl-ofc-spatial
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_johnson_2018.ipynb
  output: claim:pac-mtl-ofc-spatial
  notes: >-
    Blocked for the reason given under pac-mtl-spatial. On the code's selection (not judged; 189 MTL
    to OFC pairs) the spatial condition effect is p = 0.18 (surrogate a).
  deviations:
  - *pacmodel
  - *timeaxis
- claim: pac-mtl-pfc-direction
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_johnson_2018.ipynb
  output: claim:pac-mtl-pfc-direction
  notes: >-
    Blocked for the reason given under pac-mtl-spatial. On the code's selection (not judged; 105 MTL
    to PFC and 76 PFC to MTL pairs) the direction effect is p = 0.26 (spatial) and 0.38 (temporal),
    surrogate a, and both models have other effects below 0.05/15.
  deviations:
  - *pacmodel
  - *timeaxis
- claim: pac-mtl-ofc-direction
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_johnson_2018.ipynb
  output: claim:pac-mtl-ofc-direction
  notes: >-
    Blocked for the reason given under pac-mtl-spatial. On the code's selection (not judged; 189 MTL
    to OFC and 170 OFC to MTL pairs) the spatial condition x direction effect is p = 0.00018
    (surrogate a), and both models have effects below 0.05/15.
  deviations:
  - *pacmodel
  - *timeaxis
EOF
echo done
```

```
done
```

**Agent calls Bash**

```bash
sed -i 's/    &pacblock The PAC claims/    The PAC claims/' $TMPDIR/rec_outcomes.yaml; sed -n 469,507p claims/crcns-fcx-2/*.yaml | grep "quantity"
```

```
- quantity: phase-directing MTL electrodes
  - quantity: phase-directing PFC electrodes
  - quantity: phase-directing OFC electrodes
  - quantity: phase-directing MTL to PFC pairs
  - quantity: phase-directing PFC to MTL pairs
  - quantity: phase-directing MTL to OFC pairs
  - quantity: phase-directing OFC to MTL pairs
  - quantity: subjects with phase-directing MTL electrodes
  - quantity: subjects with phase-directing MTL to OFC pairs
```

**Agent**

Now the findings and the `verifications` block, then assembling the record.

**Agent calls Bash**

```bash
cat > $TMPDIR/rec_tail.yaml <<'EOF'
verifications:
- date: 2026-11-09
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
    notebook)
  reviewed: The handover of the run after author-answers, the executed notebook with the
    conclusions and summary removed, the helper module and the claims file; the verifier also read
    the paper under paper/ and listed the archive.
  results:
  - claim: behavior-proficient
    agrees: true
    outcome: reproduced
    reason: >-
      Cell 16, all 120 trials, lowest 0.792, highest 0.967, every subject between 0.711 and 1.0.
    response: No change of outcome.
  - claim: behavior-no-difficulty-difference
    agrees: false
    outcome: partially_reproduced
    reason: >-
      Accuracy shows no effect under either reading (numeric term F 0.16, p 0.70; F 0.44, p 0.51).
      Response time shows no effect only with the summary_file.csv values (F 2.41, p 0.13). With the
      per-trial tables it does differ (F 12.3, p 0.0015 all trials; F 11.5, p 0.002 kept trials),
      and the two sources disagree in 7 of 10 subjects. The summary_file.csv values are of unknown
      provenance and were chosen because they match the paper (B2).
    response: >-
      Outcome kept as reproduced, resting on the response-time source (assumed), and the
      disagreement recorded. Added the provenance check the verifier asked for: means and medians
      over correct, all and kept trials, other subjects' rows, blocks of 40 trials and trial type
      reproduce 9 of 30 values (s6, s8 and s9, by the mean over correct trials) and none of the
      other 7 subjects'. The file's condition means and SDs are the paper's, so it holds the values
      the paper's model was fitted to, and the criterion asks whether that model finds an effect;
      the trial tables' result is reported in the notes as the outcome it would give.
  - claim: electrode-counts
    agrees: true
    outcome: reproduced
    reason: >-
      Cell 20, 36/116/102, and 9 and 7 subjects, all exact.
    response: No change of outcome.
  - claim: correct-trial-counts
    agrees: true
    outcome: reproduced
    reason: >-
      Cell 22, means 100.9, 32.9, 34.8, 33.2 and 10.2 are within tolerance; per-subject ranges equal
      the paper's exactly.
    response: No change of outcome.
  - claim: erp-no-condition-difference
    agrees: true
    outcome: not_reproduced
    reason: >-
      The criterion is no electrode below p 0.05. Cell 24 finds 1 of 254 electrodes with the
      subject-wide null and 13 with the per-electrode null. Both counts are at or below the expected
      false-positive count (25.4), so the data are consistent with no effect, but the rule as written
      fails. The baseline subtracted is the trial-averaged baseline, which leaves the between-trial
      tests unchanged; per-trial correction would change the test, and the deposited script was not
      shown (B5).
    response: >-
      Outcome kept, now marked assumed. The notebook quotes erp_compute.m (lines 84 to 88), which
      subtracts nanmean(pretrial.trial), the trial mean, so the main reading follows the code. The
      per-trial baseline was run as a variant and leaves 0 electrodes significant under the
      subject-wide null, so the outcome rests on the code's baseline. In the trial table's windows,
      now the main reading, 1 electrode (s9) is significant.
  - claim: power-theta-sustained
    agrees: true
    outcome: not_reproduced
    reason: >-
      Cell 26, theta is sustained in 0 of 10, 0 of 9 and 0 of 9 subjects (electrodes 1/36, 1/116,
      11/102). MTL alpha is desynchronised in 0 of 10 subjects. Every neural outcome rests on the
      unchecked time-axis choice (B1).
    response: >-
      No change of outcome. Both window placements are now run; in the trial table's windows, now
      the main reading, theta is sustained in 1 of 10, 0 of 9 and 0 of 9 subjects and MTL alpha in 0
      of 10.
  - claim: power-condition-exclusions
    agrees: true
    outcome: not_reproduced
    reason: >-
      Cell 28, 12 electrodes (6 PFC, 5 OFC, 1 MTL) in 5 subjects with the subject-wide null, and 69
      with the per-electrode null; expected 8 (5 PFC, 3 OFC) in 4.
    response: >-
      No change of outcome. In the trial table's windows, now the main reading, 7 electrodes (1 PFC,
      4 OFC, 2 MTL) in 4 subjects; the 12 of the code's windows are shown as a variant.
  - claim: plv-theta-peak
    agrees: true
    outcome: reproduced
    reason: >-
      Cell 30, imaginary PLV, a 3 to 7 Hz local maximum in MTL-MTL 7/9, MTL-PFC 8/9 and MTL-OFC 4/7
      subjects. The one-subject rule is lenient, a noisy 11-bin spectrum often has a local maximum
      among the four theta bins.
    response: >-
      No change of outcome. In the trial table's windows the counts are 4/8, 7/9 and 5/7; the
      leniency of the one-subject rule is stated in the notes.
  - claim: psi-theta-shift
    agrees: false
    outcome: partially_reproduced
    reason: >-
      Cell 32. Single-window (Methods) PSI, the post-versus-pre test fails in both networks (p 0.27,
      0.56). Sliding-window PSI on raw values, OFC passes (p 0.027), PFC fails (p 0.079), which is
      the criterion's partial case. The code's PSI form passes both networks on raw PSI (p < 1e-4),
      but its z part rests on a miscalibrated null (B3).
    response: >-
      Outcome kept as not reproduced, now judged on the sliding windows of M5 (the reading the
      verifier used) and marked assumed, and the disagreement recorded. The verifier's partial
      result is in the deposited code's windows; the per-electrode jitter test added for B1 places
      the events where the trial table puts them, and in those windows the sliding reading finds no
      shift in either network (MTL-PFC raw p = 0.27, MTL-OFC raw PSI falls). The code's single
      window there gives the partial pattern (MTL-PFC raw p = 0.014), shown as a variant. A
      trial-shuffle calibration of each PSI form was added.
  - claim: crossspectral-shift
    agrees: true
    outcome: not_reproduced
    reason: >-
      Cell 34, post greater than pre at p < 0.05 in 1 of 7 systems (single-window PSI) and 2 of 7
      (code form); 4 are needed for partial. The claims file's sliding-window reading was not run
      (B4).
    response: >-
      No change of outcome. Cross-spectral PSI is now computed with sliding windows (the claims
      file's M5) and judged on them, in both window placements: 1 of 7 systems in the trial table's
      windows, at most 2 of 7 in the code's.
  - claim: phase-directing-counts
    agrees: true
    outcome: not_reproduced
    reason: >-
      Cell 36, 0 units in every system with single-window PSI; with the code form only 1 of 7 counts
      is within 10% (OFC 38), and MTL to OFC is 200 against 93.
    response: >-
      No change of outcome. The sliding-window reading gives 0, 0, 0, 0, 1, 3 and 2 units; a
      trial-shuffle calibration shows that the code's form selects 57% of units with the coupling
      removed.
  - claim: crossspectral-equal-strength
    agrees: true
    outcome: not_reproduced
    reason: >-
      Cell 38, frequency p 0.016 (MTL-PFC) and 7e-5 (MTL-OFC); frequency x direction p 1.6e-4. This
      is only on units picked by the miscalibrated code form (B3), so it is weak evidence.
    response: >-
      Changed to blocked (methods_underspecified). The calibration the verifier asked for shows the
      code's form selects as many units with trials shuffled (57%) as on the real data, against the
      2.5% its threshold implies, so by the protocol's rule on chance levels it is not the paper's
      stated procedure; the Methods' PSI selects 0 and 1 pairs per direction. The model on the
      code's selection is kept as a variant, not judged.
  - claim: theta-peak-bands
    agrees: true
    outcome: not_reproduced
    reason: >-
      Cell 40, overlap with the paper's counts is 4 of 10 (all electrodes) and 5 of 10
      (code-selected electrodes); 7 are needed for partial.
    response: >-
      No change of outcome. In the trial table's windows the overlap is 4 of 10 (all electrodes),
      0 of 10 (sliding-window selection) and 4 of 10 (code's selection).
  - claim: pac-mtl-spatial
    agrees: true
    outcome: not_reproduced
    reason: >-
      Cell 42/43, condition p 0.00717 against a threshold of 0.00714 (borderline), condition x
      frequency p 0.20, peak at 38.5 Hz. Units are code-selected (B3).
    response: &pacresp >-
      Changed to blocked (methods_underspecified). The unit selection rests on the code's PSI form,
      which the added calibration shows selects 57% of units with trials shuffled, as many as on the
      real data; the Methods' PSI selects at most 3 units per system. The PAC models on the code's
      selection are kept as a variant, not judged. PAC on all units without selection, which the
      verifier also suggested, was not run: it tests another population than the claim's and would
      have taken the run past the hour the notebook may take.
  - claim: pac-frontal-no-condition
    agrees: true
    outcome: not_reproduced
    reason: >-
      Condition effects fall below 0.05/7, PFC spatial condition x time 3.7e-6, PFC temporal
      three-way 2.9e-6, OFC spatial condition 1.8e-6. The within-unit F tests are anti-conservative
      on autocorrelated PAC maps, which biases claims of absence toward failing (B7).
    response: *pacresp
  - claim: pac-mtl-pfc-spatial
    agrees: true
    outcome: not_reproduced
    reason: >-
      Condition p 0.19 (a) and 0.17 (b); the spatial minus identity difference is negative.
    response: *pacresp
  - claim: pac-mtl-pfc-temporal
    agrees: true
    outcome: not_reproduced
    reason: >-
      Condition p 0.36 and 0.45; the difference is negative.
    response: *pacresp
  - claim: pac-pfc-mtl-no-condition
    agrees: true
    outcome: not_reproduced
    reason: >-
      Temporal model condition p 5.8e-6 (a) and 7.7e-7 (b), both below 0.05/7.
    response: *pacresp
  - claim: pac-mtl-ofc-spatial
    agrees: true
    outcome: not_reproduced
    reason: >-
      Condition p 0.015 (a) and 0.031 (b), above 0.05/7. The peak at 9.5 Hz does match.
    response: *pacresp
  - claim: pac-mtl-pfc-direction
    agrees: true
    outcome: not_reproduced
    reason: >-
      Condition x direction is significant but larger for PFC to MTL (the wrong direction).
      Direction p 0.32 and 0.96, with MTL to PFC higher.
    response: *pacresp
  - claim: pac-mtl-ofc-direction
    agrees: true
    outcome: not_reproduced
    reason: >-
      Spatial model, direction p 0.13, condition x direction p 0.17. The temporal model has effects
      below 0.05/15.
    response: *pacresp
findings:
- kind: metadata_error
  statement: >-
    The derived data's time axes put each segment's first sample at -1.5 s, and that sample is the
    trial table's epoch start (encmain at column H, first stimulus onset; proc 0.3 s before column
    I, test cue offset; pre about 0.1 s after column G), so the task events lie 1.5 s earlier on the
    time axes than 0 s suggests. The deposited scripts cut their windows from the time axes as if 0
    s were stimulus onset, test cue offset minus 0.3 s and start screen minus 0.9 s. The data side
    with the table: the 900 and 1150 ms delay trials part where the table puts the first
    delay-dependent event of each segment (proc ERPs from -0.25 to 0.75 s, p down to 0.005 against
    200 permutations) and not where the scripts' windows put it (proc 1.0 to 2.0 s, p 0.29 to 0.94).
- kind: metadata_error
  statement: >-
    The response times of docs/summary_file.csv, which the descriptor says are "calculated on all
    correct trials", differ from the mean over correct trials of the per-trial tables in 7 of 10
    subjects (s1 identity 1948 against 2348 ms), and no other summary of the trial tables tried
    (medians, all or kept trials, other subjects' rows, blocks of 40 trials, trial type) gives them.
    The paper's condition means are those of summary_file.csv. Its accuracies do equal the per-trial
    tables.
- kind: metadata_error
  statement: >-
    For s10 the trial table's epoch columns are not on the derived data's sample grid (offsets of
    97.1 to 98.1 samples from column G, about 114 for two trials, and fractional offsets for H and I),
    and its trialinfo does not equal the trial table's columns.
- kind: metadata_error
  statement: >-
    The descriptor gives fsample 1000 for the derived structures; s8 and s9 are at 512 Hz (as its
    note on the trial table says).
- kind: code_mismatch
  statement: >-
    The deposited psianalysis.m multiplies the Fourier coefficients without conjugating one of them,
    so its "cross-spectral density" and phase slope are not the PSI of Nolte et al. that the Methods
    cite. It also z-scores the trial mean of per-trial PSI against a null built from trial-averaged
    coherency, a different statistic; with the conjugate added, this form passes z > 1.96 for 57% of
    electrodes and pairs when one signal's trials are shuffled against the other's, as many as on
    the real data (56%), and its selection rates are of the order of the paper's counts of
    phase-directing units (31% to 49%). The Methods' PSI passes 0% to 0.1% with trials shuffled.
- kind: code_mismatch
  statement: >-
    subtracterp.m with ncond = 3 selects the temporal trials by trialinfo column 5 == 2 (the delay
    length column, 900 or 1150), so the temporal condition is empty; pacanalysis.m sizes its
    amplitude matrix with an undefined variable `freq`; and dirpac_compute.m calls pacanalysis with
    six arguments while it takes four, so the deposited PAC scripts cannot run as given.
- kind: paper_inconsistency
  statement: >-
    The Methods describe PSI from sliding 3-cycle windows (dt = 3/f) at 3 to 7 Hz on 900 ms segments;
    a 3-cycle window at 3 Hz is 1 s long and cannot be placed in the segment. The deposited code uses
    one Hanning window over the segment.
- kind: paper_inconsistency
  statement: >-
    The behavioural models are said to have "3 condition-fixed effects" but are reported as F(1,28);
    with one value per subject and condition, F(1,28) is what condition as a single numeric term
    gives, and on summary_file.csv that reading gives the paper's p > 0.12 for response time.
- kind: methods_unavailable
  statement: >-
    Question for the authors. Were the behavioural mixed models fitted with condition as one numeric
    term (and if so, with which coding), on the per-subject values of docs/summary_file.csv, and how
    were those response times computed? The printed F(1,28) fits a numeric term on 30
    subject-condition values. On summary_file.csv that model finds no response-time effect (p =
    0.13); on the trial tables' response times it finds one (p = 0.0015), so the outcome of
    behavior-no-difficulty-difference rests on these choices.
- kind: methods_unavailable
  statement: >-
    Question for the authors. Which form of PSI produced the reported PSI z values and the counts of
    phase-directing electrodes (the Methods' Nolte PSI on the trial-averaged cross-spectrum, or the
    code's mean of per-trial PSI against trial-averaged coherency), with which spectral window, and
    were the analysis windows cut 1.5 s later on the derived time axes than the trial table places
    the events, as the deposited scripts do? The Methods' PSI selects at most 3 phase-directing units
    per system here, and the code's form selects as many with trials shuffled as on the real data,
    so crossspectral-equal-strength and the PAC claims are blocked.
EOF
python - <<'EOF'
import os
T = os.environ['TMPDIR']
src = open('attempts/crcns-fcx-2-johnson-2018-01.yaml').read()
head = src[:src.index('outcomes:\n')]
out = head + open(f'{T}/rec_outcomes.yaml').read() + open(f'{T}/rec_tail.yaml').read()
open('attempts/crcns-fcx-2-johnson-2018-01.yaml', 'w').write(out)
import yaml; d = yaml.safe_load(out); print(len(d['outcomes']), len(d['verifications'][0]['results']), [o['outcome'] for o in d['outcomes']].count('blocked'))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent**

Record assembled: 21 outcomes, 21 verification results, 9 blocked. Next, the README.

**Agent calls Bash**

```bash
date -u; python - <<'EOF'
P='entries/crcns-fcx-2-johnson-2018/README.md'
s=open(P).read()
a=s.index('| Claim | Outcome |'); b=s.index('A failure to reproduce')
s = s[:a] + '''| Claim | Outcome |
|---|---|
| All subjects proficient (accuracy 0.79 to 0.97) | Reproduced |
| Accuracy and response time do not differ by condition | Reproduced, resting on assumptions |
| 254 electrodes, 36 MTL, 116 PFC, 102 OFC | Reproduced |
| About 100 correct trials per subject | Reproduced |
| ERPs do not differ by condition | Not reproduced, resting on an assumption |
| Sustained theta power in all regions | Not reproduced |
| 8 electrodes with power condition effects | Not reproduced |
| PLV peaks in theta | Reproduced |
| Theta PSI shifts from frontal to MTL leads | Not reproduced, resting on an assumption |
| Cross-spectral PSI shifts after the test cue | Not reproduced |
| Counts of theta phase-directing electrodes and pairs | Not reproduced |
| Equal cross-spectral strength across frequencies and directions | Blocked (methods underspecified) |
| Individual theta peak bands | Not reproduced |
| Theta PAC by condition (eight claims) | Blocked (methods underspecified) |

''' + s[b:]
c = s.index('The trial table and the descriptor place')
s = s[:c] + '''The analysis windows are placed by the trial table and the descriptor, 1.5 s earlier on the
derived time axes than the paper's deposited code places them: the trials with the two delay
lengths part where the table puts the delay-dependent events, and not where the code does. The
code's windows are run as a variant. The phase-directing units that the equal-strength and PAC
claims rest on cannot be selected: the PSI of the paper's Methods selects at most 3 per system, and
the deposited code's own form of PSI selects as many units with trials shuffled as on the real
data. The behaviour claim is reproduced with condition as one numeric term, as the amended claims
file judges it, on the response times of `summary_file.csv`; the trial tables' response times
differ from those in 7 of 10 subjects, no summary of them gives the file's values, and they would
show a condition effect. The attempt record, with the reasons and the differences from the paper's
method, is
[`attempts/crcns-fcx-2-johnson-2018-01.yaml`](../../attempts/crcns-fcx-2-johnson-2018-01.yaml).
'''
open(P,'w').write(s)
EOF
grep -rn "rather\|—" entries/crcns-fcx-2-johnson-2018/README.md attempts/crcns-fcx-2-johnson-2018-01.yaml entries/crcns-fcx-2-johnson-2018/reproduce_johnson_2018.ipynb entries/crcns-fcx-2-johnson-2018/fcx2.py | head; python tools/entry.py check entries/crcns-fcx-2-johnson-2018 2>&1 | tail -5
```

```
Mon Nov  9 02:30:55 UTC 2026
0 error(s)
```

**Agent**

Check passes. Adding one deviation for the verifier's B6 (frequency-resolved PSI not run), then starting the final full run.

**Agent calls Bash**

```bash
python - <<'EOF'
P='attempts/crcns-fcx-2-johnson-2018-01.yaml'
s=open(P).read()
old='''  - >-
    The mixed model with random intercepts for subject and pair is computed as the within-pair F
    test of interval (equal for two intervals per pair), with all pairs after the 7 exclusions.'''
assert old in s
s=s.replace(old, old + '''
  - >-
    PSI is one value per pair over 3 to 7 Hz, and the null pairs one signal's coherency at each
    frequency with the other's at a shuffled frequency. The Methods' "electrode pair and
    frequency-resolved" PSI with a 2 Hz bandwidth, and a null that shuffles the order of the
    coherency spectrum, were not run.''')
open(P,'w').write(s)
EOF
date -u; python tools/entry.py all entries/crcns-fcx-2-johnson-2018 2>&1 | grep -v "MissingIDField\|_validate" | tail -5; date -u
```

```
Mon Nov  9 02:31:08 UTC 2026
Installed kernelspec registry-crcns-fcx-2-johnson-2018 in executed/crcns-fcx-2-johnson-2018/.venv/share/jupyter/kernels/registry-crcns-fcx-2-johnson-2018
0 error(s)
pass  reproduce_johnson_2018.ipynb  (2823 s)
Mon Nov  9 03:18:19 UTC 2026
```

**Agent**

The final run passed in 47 minutes (2823 s). Checking that its outputs match the run the conclusions were written from.

**Agent calls Bash**

```bash
python - <<'EOF' > $TMPDIR/out2.txt
import json
nb = json.load(open('executed/crcns-fcx-2-johnson-2018/reproduce_johnson_2018.ipynb'))
for i, c in enumerate(nb['cells']):
    if c['cell_type'] != 'code': continue
    print(f'##### [{i}]')
    for o in c.get('outputs', []):
        if o.get('output_type') == 'error': print('ERROR', o['ename'], o['evalue'])
        print(''.join(o.get('text') or ''))
EOF
diff <(grep -v "analysed in\|subjects done after\|total run time\|load_s\|^ *s[0-9]* .* [0-9]*$" $TMPDIR/out.txt) <(grep -v "analysed in\|subjects done after\|total run time\|load_s\|^ *s[0-9]* .* [0-9]*$" $TMPDIR/out2.txt) | head -20; diff $TMPDIR/out.txt $TMPDIR/out2.txt | wc -l
```

```
261a262
> 
270d270
< 
273a274
> 
282a284
> 
74
```

**Agent calls Bash**

```bash
diff $TMPDIR/out.txt $TMPDIR/out2.txt | grep "^[<>]" | grep -v "analysed in\|subjects done\|total run time" | head -30
```

```
<      s2 1000.0 [1000.0]              31        25           120             113              109 (4501, 4501) (4502, 4503) (4501, 4501)    (-1.5, 3.001)        True    -116.7     181.2      15
<      s3 1000.0 [1000.0]              14         7           120             115               96 (4501, 4501) (4498, 4499) (4501, 4501)    (-1.5, 2.997)        True    -208.6     191.9      15
<      s4 1000.0 [1000.0]              34        19           120             118              110 (4501, 4501) (4502, 4504) (4501, 4501)    (-1.5, 3.001)        True    -763.3     642.5      15
<      s5 1000.0 [1000.0]             118        28           120             120               95 (4501, 4501) (4496, 4498) (4501, 4501)    (-1.5, 2.995)        True    -840.7     733.7      47
<      s6 1000.0 [1000.0]              74        48           120             108              103 (4501, 4501) (4505, 4506) (4501, 4501)    (-1.5, 3.004)        True    -621.2    1053.4      27
<      s7 1000.0 [1000.0]              57        24           120             100              100 (4501, 4501) (4498, 4499) (4501, 4501)    (-1.5, 2.997)        True    -557.6     399.6      21
>      s2 1000.0 [1000.0]              31        25           120             113              109 (4501, 4501) (4502, 4503) (4501, 4501)    (-1.5, 3.001)        True    -116.7     181.2      14
>      s3 1000.0 [1000.0]              14         7           120             115               96 (4501, 4501) (4498, 4499) (4501, 4501)    (-1.5, 2.997)        True    -208.6     191.9      16
>      s4 1000.0 [1000.0]              34        19           120             118              110 (4501, 4501) (4502, 4504) (4501, 4501)    (-1.5, 3.001)        True    -763.3     642.5      16
>      s5 1000.0 [1000.0]             118        28           120             120               95 (4501, 4501) (4496, 4498) (4501, 4501)    (-1.5, 2.995)        True    -840.7     733.7      48
>      s6 1000.0 [1000.0]              74        4
[... 7 more lines not kept]
```

**Agent**

The two runs give identical numbers; only the per-subject load times differ. Final check of the working tree:

**Agent calls Bash**

```bash
git status --short; python tools/entry.py check entries/crcns-fcx-2-johnson-2018 2>&1 | tail -1; date -u
```

```
M attempts/crcns-fcx-2-johnson-2018-01.yaml
 M entries/crcns-fcx-2-johnson-2018/README.md
 M entries/crcns-fcx-2-johnson-2018/entry.yaml
 M entries/crcns-fcx-2-johnson-2018/fcx2.py
 M entries/crcns-fcx-2-johnson-2018/reproduce_johnson_2018.ipynb
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
?? scripts
0 error(s)
Mon Nov  9 03:18:40 UTC 2026
```

**Agent**

Round 1 of verification is answered. Of 21 claims, 5 are now reproduced, 7 not reproduced and 9 blocked; before this round it was 5, 16 and 0. The entry re-ran clean with `python tools/entry.py all` (47 minutes, check 0 errors), and two full runs gave identical numbers. Nothing is committed.

**What changed in the outcomes**
- **Time axis (verifier's B1), now the main reading.** I added a per-electrode test comparing the 900 ms and 1150 ms delay trials, with a 200-permutation null. In all three segments the two groups differ where the trial table puts the first delay-dependent event, and not where the deposited code's windows put it. The clearest case: in the postcue segment the ERPs differ from −0.25 to 0.75 s (p down to 0.005), around the response screen at −0.3 s; at 1.0 to 2.0 s, where the code puts it, p is 0.29 to 0.94. Every window is now placed 1.5 s earlier than the code places it. The code's windows still run as a variant for ERP, power, PLV and both PSI measures.
- **Nine claims changed from not reproduced to blocked (`methods_underspecified`):** crossspectral-equal-strength and the 8 PAC claims. I added a calibration with one signal's trials shuffled, which removes any real coupling (B3). Under it the code's PSI form still passes 57% of units, the same rate as on the real data (56%), against the 2.5% its threshold implies. The Methods' PSI selects at most 3 units per system, too few for the models. The protocol's chance-level rule therefore blocks these claims. The results on the code's selection stay in the notebook as an unjudged variant.
- **Kept, with the disagreement recorded:**
  - behavior-no-difficulty-difference stays reproduced (assumed); the verifier gave partial. I searched for where the `summary_file.csv` response times come from. Means over correct trials explain 9 of 30 values (s6, s8 and s9 only); medians, all or kept trials, other subjects' rows, blocks of 40 trials and trial type explain none of the rest. I kept the outcome because the file's condition means and SDs are the paper's.
  - psi-theta-shift stays not reproduced (assumed); the verifier gave partial. It is now judged on the claims file's sliding windows (B4), placed by the trial table, where neither network shifts. The verifier's partial pattern appears only in the code's windows.
- **erp-no-condition-difference** stays not reproduced, now marked assumed. The deposited `erp_compute.m`, now quoted in the notebook, subtracts the trial-mean baseline (B5). A per-trial baseline leaves 0 significant electrodes, so the outcome depends on that choice.

**What I added or corrected**
- Cross-spectral PSI with sliding windows for crossspectral-shift, phase-directing-counts and theta-peak-bands.
- Calibration tables for every PSI form.
- Script excerpts streamed from `analysis_scripts.tar.gz`.
- The response-time source search.
- Updated conclusions, summary and README.
- Revised findings: the time-axis finding now reports the jitter evidence, and the PSI code finding the calibration.
- The `verifications` block, one entry per claim with the verifier's reason and my response.

**Not done**
- PAC on all units without selection (verifier section C). It tests a different population from the claims', and it would push the notebook past its 60-minute limit (it already takes 47).
- PSI resolved by frequency with a 2 Hz bandwidth (B6). The verifier marked it as not affecting a conclusion, and it is recorded as a deviation.
- No new reader questions: the report found no place where the claims file misreads the paper.

## End of run

94 turns, 165 minutes, $8.30 at API prices, result: success.
