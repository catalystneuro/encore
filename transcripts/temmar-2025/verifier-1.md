# temmar-2025 · verifier-1 · run 43245219974

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat *claims* 2>/dev/null | head -300
```

```
total 444
drwxr-xr-x 6 runner runner    4096 Nov 12 16:00 .
drwxr-xr-x 8 runner runner    4096 Nov 12 16:00 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 15:12 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 15:12 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 12 16:00 .claude
-rw-r--r-- 1 runner runner       0 Nov 12 16:00 .env
-rw-r--r-- 1 runner runner       0 Nov 12 16:00 .env.development
-rw-r--r-- 1 runner runner       0 Nov 12 16:00 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 12 16:00 .env.local
-rw-r--r-- 1 runner runner       0 Nov 12 16:00 .env.production
-rw-r--r-- 1 runner runner       0 Nov 12 16:00 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 12 16:00 .env.test
-rw-r--r-- 1 runner runner       0 Nov 12 16:00 .env.test.local
drwx------ 2 runner runner    4096 Nov 12 16:00 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 15:12 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 15:12 .github
-rw-r--r-- 1 runner runner       0 Nov 12 16:00 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 15:12 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 15:12 .mcp.json
[... 25 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "temmar-2025.yaml"
}
```

```
1	# Claims for Temmar et al. (2025), "Long-term Intracortical Neural activity and Kinematics
2	# (LINK)", NeurIPS 2025 Datasets and Benchmarks track, on dandiset 001201.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
4	# 2026-11-12, protocol pilot-14 as stated in docs/protocol.md.
5	#
6	# Text read: the version of record (open-access PDF from the Curran Associates NeurIPS 2025
7	# proceedings, extracted to paper/10.52202-085713-4642.txt), main text, figure legends and
8	# checklist, and the supplement (Supplementary Materials and Appendices, from OpenReview):
9	# Appendix A (task, implants, feature extraction), B (curation, file format), C (analysis
10	# methods) and Figures S1 to S6. The paper reports no statistical test for any finding; its
11	# findings are slopes of linear fits, counts, R2 values and visual descriptions of figures.
12	#
13	# Code read: github.com/chesteklab/LINK_dataset at commit 5e1c36a1282f90abb8d96963920a8b1fdd27a6e7
14	# (2026-10-20). It holds the NWB-to-pickle converter (utils/), the signal-change analysis
15	# (data_processing/signal_changes: mean SBP per channel and day, active channels, participation
16	# ratio), single-channel tuning (data_processing/single_channel_tuning/tuning_utils.py), the
17	# population PCA analysis (data_processing/pop_level_analyses/population_level_analyses.py),
18	# single-day RR and LSTM decoders and their cross-day evaluation (data_processing/bci_decoding),
19	# the multi-day training (data_processing/stability/stability, which calls an outside library,
20	# "neuraldecoding", not in the repository) and the continual fine-tuning
[... 544 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dump.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    print(f"=== [{i}] {c['cell_type']}")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--'); print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--'); print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
EOF
python3 $TMPDIR/dump.py signals.ipynb
```

```
<persisted-output>
Output too large (47.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/c02fe5b5-dde9-4357-83bb-eeac4a3670cc/tool-results/boan7p5jf.txt

Preview (first 2KB):
=== [0] markdown
# Temmar et al. (2025), LINK: the dataset, neural signals and tuning over time

Paper: Temmar, Gill, Wang et al., "Long-term Intracortical Neural activity and Kinematics (LINK): An
intracortical neural dataset for chronic brain-machine interfaces, neuroscience, and machine learning",
NeurIPS 2025 Datasets and Benchmarks, doi:10.52202/085713-4642.

Dataset: DANDI:001201, version 0.261026.1912 (doi:10.48324/dandi.001201/0.261026.1912), streamed.
The paper cites no version, so the most recent published one is pinned. The dandiset has three
published versions (0.251023.2336, 0.261015.2153, 0.261026.1912); the cell below shows that the
three list the same 312 assets with the same asset identifiers, so the data the analysis uses do not
differ between them.

Claims file: `claims/temmar-2025.yaml`, written from the version of record (NeurIPS proceedings) and
the supplement (Appendices A to C, Figures S1 to S6). Code read for method details:
github.com/chesteklab/LINK_dataset at commit 5e1c36a1282f90abb8d96963920a8b1fdd27a6e7.
[... 23 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/c02fe5b5-dde9-4357-83bb-eeac4a3670cc/tool-results/boan7p5jf.txt"
}
```

```
1	=== [0] markdown
2	# Temmar et al. (2025), LINK: the dataset, neural signals and tuning over time
3	
4	Paper: Temmar, Gill, Wang et al., "Long-term Intracortical Neural activity and Kinematics (LINK): An
5	intracortical neural dataset for chronic brain-machine interfaces, neuroscience, and machine learning",
6	NeurIPS 2025 Datasets and Benchmarks, doi:10.52202/085713-4642.
7	
8	Dataset: DANDI:001201, version 0.261026.1912 (doi:10.48324/dandi.001201/0.261026.1912), streamed.
9	The paper cites no version, so the most recent published one is pinned. The dandiset has three
10	published versions (0.251023.2336, 0.261015.2153, 0.261026.1912); the cell below shows that the
11	three list the same 312 assets with the same asset identifiers, so the data the analysis uses do not
12	differ between them.
13	
14	Claims file: `claims/temmar-2025.yaml`, written from the version of record (NeurIPS proceedings) and
15	the supplement (Appendices A to C, Figures S1 to S6). Code read for method details:
16	github.com/chesteklab/LINK_dataset at commit 5e1c36a1282f90abb8d96963920a8b1fdd27a6e7.
17	
18	This notebook tests the claims on the dataset's contents, the neural signals over time (Figure 2,
19	S2, S4, S5) and single-channel tuning (Figure 3). The decoding claims (Figures 4 and 5) are in
20	`decoding.ipynb` and `multiday.ipynb`.
[... 798 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i -E "medial|lateral|bank|channel 7|channel 32|S1" paper/*.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 180,192p paper/*.txt; sed -n 295,315p paper/*.txt; sed -n 1140,1175p paper/*.txt; sed -n 1405,1440p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat link.py
```

```
"""Loading and measures for the LINK dataset (DANDI:001201), used by the notebooks of the
temmar-2025 entry, which test Temmar et al. (2025), NeurIPS Datasets and Benchmarks.

Where each parameter comes from is given next to it, as one of:
- "claim <id>": the claims file's criterion for that claim (claims/temmar-2025.yaml), which cites
  the paper or its code (github.com/chesteklab/LINK_dataset at 5e1c36a);
- "paper, <passage>": a detail the claims file lacks, taken from the paper (protocol, author 1.6);
- "assumption": a choice the paper leaves open, stated as such;
- "standard choice": a detail that cannot change a result.

The data are streamed from the archive (remfile + h5py); nothing is written to disk.
"""
from __future__ import annotations

import os
from functools import lru_cache

import h5py
import numpy as np
import pandas as pd
[... 402 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np, link, pandas as pd
r=np.random.default_rng(0)
th=np.radians(np.r_[170,175,180,-175,-170,-160, 160])
print(np.degrees(link.circ_median(th)), np.degrees(link.circ_iqr(th)))
# tuning: pos = sbp*a
x=r.normal(size=(5000,2)); pos=np.c_[ -0.5*x[:,0], -0.5*x[:,0]]+0.01*r.normal(size=(5000,2))
c=link.channel_tuning(x,pos); print(c, np.degrees(np.arctan2(c[:,1],c[:,0])))
# lag
y=np.zeros((5000,2)); y[3:,1]=x[:-3,1]; print(link.channel_tuning(x,y))
x=r.normal(size=(2000,5)); print(link.participation_ratio(x)[0])
t=pd.DataFrame({'index_target_position':[.5,.8,.5,.5,.2],'mrs_target_position':[.5,.8,.5,.8,.2]})
print(link.trial_directions(t))
v=np.r_[np.zeros(20)+0.001*r.normal(size=20), np.linspace(0,1,10)]
print(link.onset_and_jerk(v,1.0))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, link, pandas as pd
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls ~/.venv* /opt 2>/dev/null; which -a python python3; pip list 2>/dev/null | head; ls /home/runner/work/_temp
```

```
/opt:
actionarchivecache
az
containerd
google
hca
hostedtoolcache
microsoft
pipelinesagent-cache
pipx
pipx_bin
post-generation
primer
runner-cache
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/usr/bin/python3
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -m venv v && v/bin/pip -q install numpy pandas scipy 2>&1 | tail -2; v/bin/python -c "import numpy; print(numpy.__version__)"
```

```
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: /tmp/claude-1001/v/bin/python3 -m pip install --upgrade pip
2.5.4
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/pip -q install h5py remfile requests 2>&1 | grep -v notice; $TMPDIR/v/bin/python -c "
import numpy as np, link, pandas as pd
r=np.random.default_rng(0)
th=np.radians(np.r_[170,175,180,-175,-170,-160, 160])
print('cmed/ciqr', np.degrees(link.circ_median(th)), np.degrees(link.circ_iqr(th)))
x=r.normal(size=(5000,2)); pos=np.c_[ -0.5*x[:,0], -0.5*x[:,0]]+0.01*r.normal(size=(5000,2))
c=link.channel_tuning(x,pos); print(c, np.degrees(np.arctan2(c[:,1],c[:,0])))
y=np.zeros((5000,2)); y[3:,1]=x[:-3,1]; print(link.channel_tuning(x,y))
x=r.normal(size=(2000,5)); print('PR',link.participation_ratio(x)[0])
t=pd.DataFrame({'index_target_position':[.5,.8,.5,.5,.2],'mrs_target_position':[.5,.8,.5,.8,.2]})
print(link.trial_directions(t))
v=np.r_[0.001*r.normal(size=20), np.linspace(0,1,10)]
print(link.onset_and_jerk(v,1.0))
"
```

```
cmed/ciqr 180.0 14.999999999999982
[[-0.50332193 -0.50327718]
 [ 0.01464559  0.01459015]] [-135.00254742   44.89133756]
[[ 0.         -0.02871002]
 [ 0.          0.98970854]]
PR 4.97138416687092
[-1  1  5  2  5]
(3, 2)
```

**Agent calls Bash**

```bash
cd  python3 $TMPDIR/dump.py decoding.ipynb > $TMPDIR/dec.txt; wc -c $TMPDIR/dec.txt
```

```
24205 /tmp/claude-1001/dec.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/dec.txt"
}
```

```
1	=== [0] markdown
2	# Temmar et al. (2025), LINK: same-day and cross-day decoding (Figure 4, Appendix C.1)
3	
4	Paper: doi:10.52202/085713-4642. Dataset: DANDI:001201, version 0.261026.1912, streamed (the most recent
5	published version; the paper cites none, and the three published versions hold the same assets, see
6	`signals.ipynb`). Claims file: `claims/temmar-2025.yaml`. Code read: github.com/chesteklab/LINK_dataset at
7	5e1c36a.
8	
9	| Claim | Tested here |
10	|---|---|
11	| fig4a-sameday-stable | RR on all 312 sessions, the LSTM on every 16th session |
12	| fig4a-lstm-beats-rr | on the LSTM sessions |
13	| fig4bc-dof-accuracy | RR on all sessions, LSTM on its sessions |
14	| fig4d-cross-day-decay | RR and LSTM decoders of the LSTM sessions, tested on every session within 100 days |
15	| suppc1-shuffle-baseline | RR on all sessions, LSTM on its sessions |
16	| fig2a-irregular-shifts | all days, with the R2 above |
17	
18	Why a subset for the LSTM. One LSTM of the paper's size (2000 iterations, batch 64, 20 bins, 300 hidden
19	units) takes about 105 s to train alone on one CPU thread of this runner, and about 200 s when four train at once
20	(timed while preparing; the cell below prints the time of each fit). 312 of them, four at a time, take
[... 429 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 $TMPDIR/dump.py multiday.ipynb > $TMPDIR/md.txt; wc -c $TMPDIR/md.txt
```

```
14263 /tmp/claude-1001/md.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/md.txt"
}
```

```
1	=== [0] markdown
2	# Temmar et al. (2025), LINK: multi-day training and fine-tuning (Figure 5)
3	
4	Paper: doi:10.52202/085713-4642. Dataset: DANDI:001201, version 0.261026.1912, streamed (the most recent
5	published version; the paper cites none, and the three published versions hold the same assets, see
6	`signals.ipynb`). Claims file: `claims/temmar-2025.yaml`. Code read: github.com/chesteklab/LINK_dataset at
7	5e1c36a.
8	
9	| Claim | Here |
10	|---|---|
11	| fig5a-multiday-short-term | tested on 12 day-0 sessions, 1 and 5 training sessions |
12	| fig5a-long-term-decay | tested on the same models |
13	| fig5b-finetune | blocked, too large (the estimate is computed below) |
14	
15	Why a subset. Each LSTM takes about 195 s to train when four train at once on this runner
16	(`decoding.ipynb` prints the times). The paper trains 5 LSTMs on each of 283 day-0 sessions, 1415 fits,
17	about 19 hours here. The criteria of both Figure 5A claims compare only 1 and 5 training sessions, so
18	only those two are trained, on 12 day-0 sessions spread evenly over the eligible ones, chosen before
19	any result was seen: 24 fits.
20	=== [1] code
[... 247 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i -E "normaliz|z-score|Figure 5|Figure 4|R2|R 2|shuffl" paper/*.txt | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 314,345p paper/*.txt; sed -n 372,420p paper/*.txt; sed -n 1330,1370p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.52202-085713-4642.pdf",
 "pages": "9-10"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/pip -q install pymupdf 2>&1 | grep -v notice; $TMPDIR/v/bin/python -c "
import fitz
d=fitz.open('paper/10.52202-085713-4642.pdf')
for p in (8,9):
    d[p].get_pixmap(dpi=110).save('$TMPDIR/p%d.png'%p)
d=fitz.open('paper/10.52202-085713-4642.supp-Supplementary_Material.pdf')
print(len(d))
for i,pg in enumerate(d):
    if 'S5' in pg.get_text() or 'S1:' in pg.get_text(): print(i)
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p8.png"
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
d=fitz.open('paper/10.52202-085713-4642.pdf')
for p in range(len(d)):
    t=d[p].get_text()
    if 'Figure 3:' in t or 'Figure 1:' in t: print(p)
" 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import pymupdf as fitz
d=fitz.open('paper/10.52202-085713-4642.pdf')
d[7].get_pixmap(dpi=170, clip=fitz.Rect(0,0,612,450)).save('$TMPDIR/p7.png')
d[2].get_pixmap(dpi=130).save('$TMPDIR/p2.png')
s=fitz.open('paper/10.52202-085713-4642.supp-Supplementary_Material.pdf')
s[1].get_pixmap(dpi=130).save('$TMPDIR/s1.png')
" 2>/dev/null
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p7.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import pymupdf as fitz
d=fitz.open('paper/10.52202-085713-4642.pdf')
d[7].get_pixmap(dpi=170, clip=fitz.Rect(0,380,612,560)).save('$TMPDIR/p7b.png')
" 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p7b.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd  grep -n -A3 "within three weeks" paper/*.txt; grep -n -i -B2 -A6 "throughput" paper/*.txt | sed -n 1,60p
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import link, pandas as pd
A=link.assets(); print(len(A), A['size'].sum()/1e9,'GB', A['size'].min()/1e6, A['size'].max()/1e6)
S=['2020-07-08','2020-10-02','2020-12-12','2021-02-27','2021-04-05','2021-05-05','2021-06-16','2021-07-09','2021-07-29','2021-08-19','2021-09-14','2021-10-27','2022-01-17','2022-02-21','2022-04-01','2022-04-21','2022-06-01','2022-08-05','2022-09-01','2022-09-30']
d=set(A['date']); print(sum(pd.Timestamp(x) in d for x in S))
c=A.groupby('date').size(); print(c[c>1].index.date.tolist())
m=link.version_metadata(); print(m.get('assetsSummary'))
"
```

```
312 12.563287466 GB 33.98229 57.29309
20
[datetime.date(2021, 10, 15), datetime.date(2022, 2, 25), datetime.date(2022, 4, 8), datetime.date(2022, 4, 15), datetime.date(2022, 4, 29), datetime.date(2022, 5, 13), datetime.date(2022, 8, 10), datetime.date(2022, 9, 21), datetime.date(2022, 11, 2)]
{'species': [{'name': 'Macaca mulatta - Rhesus monkey', 'schemaKey': 'SpeciesType', 'identifier': 'http://purl.obolibrary.org/obo/NCBITaxon_9544'}], 'approach': [{'name': 'electrophysiological approach', 'schemaKey': 'ApproachType'}], 'schemaKey': 'AssetsSummary', 'dataStandard': [{'name': 'Neurodata Without Borders (NWB)', 'schemaKey': 'StandardsType', 'identifier': 'RRID:SCR_015242'}], 'numberOfBytes': 12563287466, 'numberOfFiles': 312, 'numberOfSubjects': 1, 'variableMeasured': ['ElectrodeGroup', 'ElectricalSeries'], 'measurementTechnique': [{'name': 'surgical technique', 'schemaKey': 'MeasurementTechniqueType'}, {'name': 'multi electrode extracellular electrophysiology recording technique', 'schemaKey': 'MeasurementTechniqueType'}]}
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import pymupdf as fitz
d=fitz.open('paper/10.52202-085713-4642.pdf')
d[9].get_pixmap(dpi=300, clip=fitz.Rect(180,70,450,130)).save('$TMPDIR/leg.png')
" 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/leg.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd  grep -n -i -E "2024|january|february" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent**

**A. Outcomes** (24 claims, counted from the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| dataset-sessions | reproduced | signals [11]: 312 files, 303 days, span 1242 days, 9 two-session days (all CO+RD), and every session has 375 trials. No implant date in the files, so the comparison with days 349 to 1591 is skipped, as the criterion allows. |
| dataset-contents | partially_reproduced | signals [13]: all series, trials columns and electrode columns are present except `imp`, which is missing in 81 of 312 files. Bins are 0.02 s apart (±1 ms) with gaps between runs. Velocity matches the forward difference of position everywhere except the 72 bins before gaps. Appendix A.2 says impedances are left out when none was measured within 3 weeks of a session (see B13). |
| figs2-throughput-improves | reproduced | signals [15]: the slope is positive with p < 0.05 under all three readings (a: +0.24 bits/s per year, p = 6e-8; b: p = 8e-37; c: p = 3e-20). |
| fig2a-sbp-decline | reproduced | signals [17]: reading (b) applies, because the stored unit is volts with conversion 1e-6, so stored values are microvolts. That gives −0.0338 µV/month (tolerance −0.033 ± 0.0033) and −1.110e-3 per day, the supplement's number. Reading (a) gives −0.0084. |
| fig2a-irregular-shifts | partially_reproduced | decoding [20]: the shift part holds (38 of 42 days in the window have ≥5 shifting channels). RR's median in the window (0.321) lies inside its 10th–90th percentile range. The LSTM's median (0.652, from 3 sessions) lies just above its 90th percentile (0.651, from 20 sessions), so the second part fails. |
| fig2b-active-channels-decrease | reproduced | signals [19]: slope −0.0177 channels/day, p = 2.6e-12. The first 30 days average 44.6 active channels, the last 30 average 25.9. |
| fig2c-pr-decline | reproduced | signals [21]: −0.0708 PR/month (tolerance −0.07 ± 0.007). The every-session variant gives −0.0720. |
| fig2c-ten-dimensions | reproduced | signals [23]: reading (a) holds on 0.848 of days and reading (b) on 1.000. Reading (c) holds on only 0.446. |
| figs4-bank-slopes | reproduced | signals [25], stored-µV reading: lateral −5.84e-4, medial 1 −1.34e-3, medial 2 −1.40e-3, all channels −1.11e-3, all within tolerance. Lateral mean SBP (2.19) is below both medial banks (2.55, 3.57). |
| figs5-active-inactive-slopes | not_reproduced | signals [27]: the active slope (−1.261e-3) is within tolerance, and inactive channels have lower SBP. The inactive slope is −0.536e-3 against an expected +0.54e-3, so it is outside tolerance under both fit readings. Its size matches to 1% with the opposite sign (see B1). |
| fig2d-population-drift | partially_reproduced | signals [29]: the centroid moves 17.0 between the first and last quarter, against a within-quarter SD of 2.02, so movement holds. Three quarters (2021Q1, 2022Q3, 2023Q2) are more than 25% from the median SD, where the rule allows at most two, so stable spread fails. 2023Q2 misses by only 0.01. |
| fig2e-trajectories-separable | reproduced | signals [31], main alignment: accuracy 0.212 in 2020 and 0.220 in 2023, against chance 1/8 (binomial p < 1e-200 both years). Accuracy is also above the majority class (0.16–0.18) and permuted labels (~0.12). The code variant also holds. |
| fig3b-two-channels | reproduced | signals [35]: channel 7's median angle is 81°, its circular IQR 18.6°, and its strength 0.0245 (median over channels 0.0070). Channel 32's IQR is 146.9°, above the median IQR of 46.9°. Mean TCR is 3.1 Hz for channel 7 and 36.5 Hz for channel 32. |
| fig3cd-tuning-stable | reproduced | signals [37]: under the 90° reading, 0.771 of all channels and 0.774 of active channels have a small IQR. Under the 45° reading it is 0.479 and 0.453. |
| fig3d-weak-channels-low-tcr | reproduced | signals [39]: Spearman ρ = 0.925 (p = 3e-41). Mann-Whitney p = 5e-11 (median TCR 0.40 Hz vs 0.87 Hz). |
| fig3e-array-tuning | not_reproduced | signals [41]: only 3% of medial channels fall in the flexion sector, and only 6% of lateral channels in the extension sector. Medial medians cluster at about −130°, lateral ones at 0–90°. This is the reverse of the sentence in Section 4.2, but it matches the paper's own Figures 3C and 3E (see B2). |
| fig4a-sameday-stable | reproduced | decoding [9]: neither slope is negative with p < 0.05 (RR over 312 sessions +0.002/yr, p = 0.58; LSTM over 20 sessions +0.006/yr, p = 0.56). The RR–LSTM Pearson r is 0.582 (p = 0.007), but only over 20 sessions. |
| fig4a-lstm-beats-rr | reproduced | decoding [11]: the LSTM beats RR on 20 of 20 sessions, by at least 0.223. The highest RR R2 on any of the 312 sessions (0.467) is below the lowest LSTM R2 (0.514), but 292 sessions have no LSTM (see B5). |
| fig4bc-dof-accuracy | reproduced | decoding [13]: for both decoders, both position medians exceed both velocity medians, and MRS exceeds IDX for position and velocity. |
| fig4d-cross-day-decay | reproduced | decoding [16]: holds only under absolute offsets with test-day normalisation. There the LSTM is better at every offset, the short-term drop is 0.207 against a later drop of 0.190, and r = 0.903. Signed offsets with test-day normalisation fail narrowly (drops 0.19 vs 0.21, r = 0.887). Training-day normalisation gives RR R2 of about −13. |
| suppc1-shuffle-baseline | partially_reproduced | decoding [18], reading (a): the LSTM median is −0.154, within tolerance. The RR median is −0.223, outside −0.166 ± 0.017. Reading (b) gives −0.60 and −0.41, both outside. All values are negative, consistent with the paper's chance reference. |
| fig5a-multiday-short-term | reproduced | multiday [8], 12 of 283 day-0 sessions, training-day normalisation. Days 1–5 mean R2 is −0.25 with 5 sessions against −0.50 with 1. The drop from day 0 is 0.79 against 1.09. Day-0 R2 is 0.540 against 0.587 (lower in 11 of 12 pairs). All these R2 values are far below Figure 5A (see B3). |
| fig5a-long-term-decay | not_reproduced | multiday [10]: the initial rate is not more negative for 1 session (+0.18 vs +0.013), and the predicted day-0-to-5 drop is not larger for 1 session. The long-term intervals overlap. Both fits are degenerate (see B4), so this outcome tells us little. |
| fig5b-finetune | blocked (too_large) | multiday [12]: the full run is estimated at 6.3 h. The archive holds all 20 seed days and all 312 files (12.6 GB), so no data are missing, and part of the claim could have been run (see section C). |

**B. Problems**

1. [affects a conclusion] figs5 / claims file. The paper prints "0.54 × 10⁻³" for inactive channels, calls it "near 0", and says in Section 4.1 that all categories decreased. The claims file reads the value as positive. The data give −0.536e-3, which suggests a dropped minus sign. Under that reading the claim would be reproduced. I report this and do not correct it.
2. [affects a conclusion] fig3e / claims file. The criterion follows the text of Section 4.2 ("medial … MRS flexion, lateral … extension"). The paper's Figure 3E panels are labelled the other way: Lateral is tuned to flexion, Medial 1 and 2 to −135°. Figure 3C agrees with the panels (channels 0–31 tuned near 0–90°, channels 32–95 near −135 to −180°). The file labels (bank A = Lateral) agree with the Figure S4 slopes. So the data reproduce the figure but not the sentence. The claims file does not mention the contradiction.
3. [affects a conclusion] multiday [6]/[8], fig5a both claims. The criterion requires the code variant (normalisation refit on the test day) to be shown, and it was not run. With training-day normalisation, mean R2 after day 0 is about −0.5. Figure 5A shows about 0.2–0.4, and Figure 4D matches the notebook's test-day normalisation (LSTM 0.39 at days 1–5, 0.18 at days 90–100). So the reading used is probably not what the figure plotted, and the 1-vs-5 comparisons could change under the variant. Only 12 day-0 sessions were run, giving 16 evaluations at days 1–5.
4. [affects a conclusion] multiday [10], fig5a-long-term-decay. The k=1 fit has a near-zero-amplitude component (c ≈ 0, d = 0.18), and that component is labelled the "initial decay". The k=5 fit has two almost equal rates with ±1.5 standard errors, so it cannot be identified. The starting values (positive rates) come from the criterion, but the paper's legend shows negative rates (0.229e^−0.183x + 0.268e^−0.006x and 0.134e^−0.140x + 0.374e^−0.004x). No fit was run from the legend's values. The outcome mostly reflects a noisy, negative mean curve (residual RMS 0.40–0.65).
5. [affects a conclusion] decoding [0]/[7]. The LSTM was trained on 20 of 312 sessions. That is weak support for the universal "every day" claim (fig4a-lstm-beats-rr), and it puts the shared-shift correlation and the LSTM side of fig2a-irregular-shifts on n = 20 and n = 3. The stated reason (4.3 h at 200 s per fit) conflicts with the measured 77 s per fit, which is about 1.7 h. The multiday intro likewise says 195 s per fit, against 73–76 s measured.
6. [affects a conclusion] decoding [20], fig2a-irregular-shifts. The shift rule (the criterion's) flags ≥5 channels on 237 of 243 days outside the window, so it cannot pick out the July–November 2022 period, and the shift part holds trivially. The LSTM part fails by 0.001, on 3 sessions, and in the "better" direction.
7. [affects a conclusion] decoding [16], fig4d. The pass depends on one of four reading pairs, and on margins of 0.017 (sharp-then-stable) and 0.003 (r against 0.9), with 20 decoders. Cross-day R2 is scored on every 5th test bin.
8. [affects a conclusion] signals [29], fig2d. Stable spread fails on 3 quarters where at most 2 are allowed. 2023Q2 is 25.5% from the median, and 2020Q2 is a single session. The partial outcome is marginal.
9. [does not affect a conclusion] link.onset_and_jerk with k_sd = 1, fig2e main alignment. Noise leaves ±1 SD about a third of the time, so onset is almost always the first bin after the baseline. The "alignment" then falls inside the first 10% of the trial, so trajectories are in effect aligned to trial start. This follows the paper's stated method. The 2-SD variant drops 92,544 of 116,683 trials.
10. [does not affect a conclusion] signals [5]/[31], fig2e. A PCA is fitted per day, and trials from about 43 days are pooled into one classifier. PC signs and rotations differ between days, which can only lower accuracy, and accuracy is still above chance.
11. [does not affect a conclusion] link.throughput. 998 trials shorter than the 750 ms hold become NaN under readings (a) and (c). That is under 1% of trials; reading (b) has none and is also significant.
12. [does not affect a conclusion] multiday [1]/[3]. Two-session days are left out of the test sets as well as the day-0 choices. The criterion excludes them only as days, which is ambiguous.
13. [does not affect a conclusion] The 81 files without impedances fit the paper's own rule in Appendix A.2, which the dataset-contents criterion does not account for. Also, the claims file's header says the data run to "February 2024", but the data end on 2023-06-22, which fits the 1242-day span.
14. [does not affect a conclusion] I tested the helpers on synthetic inputs and they behave correctly: circ_median/circ_iqr across the ±180° wrap, channel_tuning (angle −135° recovered, lag 3 found), participation_ratio (about 5 for 5 independent channels), and trial_directions sectors. I found no train/test leakage in decoding: normalisers and output z-scoring are fitted on training bins only.

**C. What I could not check, and what output would have let me**

- **fig5a under the code's normalisation.** The 1-vs-5 summary and the double-exponential fits recomputed with input normalisation refit on each test day, plus a fit started from the paper's legend values, would show whether either Figure 5A claim depends on the reading.
- **fig5b.** The 30 s arm alone (20 seed fits plus 1,146 fine-tunes of 50 iterations, about 15–25 min for both normalisation readings at the measured 0.037 s per iteration) could have tested half of the criterion. A subset of seeds would have made 120 s and 300 s feasible. Neither was run.
- **fig4a-lstm-beats-rr.** LSTM R2 on all 312 sessions (about 1.7 h measured), or at least on the sessions with the highest RR R2.
- **suppc1.** The number of sessions where both shuffled R2 values fall within tolerance, which matters because the paper used a single unnamed session.
- **fig3e labels.** Printing channel 47's `array_name`, `row` and `col` would have checked the file labels against Figure S1 ("channel 47 is on the medial array, row 5, column 5"). I did not read the NWB files.
- **fig2a-irregular-shifts.** Per-day shift counts compared with a baseline rate, and the reading where the 30-day window counts sessions rather than calendar days.

## End of run

32 turns, 5 minutes, $1.95 at API prices, result: success.
