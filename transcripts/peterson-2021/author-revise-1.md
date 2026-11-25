# peterson-2021 · author-revise-1 · run 45576478524

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls entries/peterson-2021 transcripts/peterson-2021 questions 2>/dev/null | head -50; wc -l docs/protocol.md transcripts/peterson-2021/verifier-1-report.md
```

```
Wed Nov 25 08:36:56 UTC 2026
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
entries
executed
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
[... 64 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "transcripts/peterson-2021/verifier-1-report.md"
}
```

```
1	**Verifier report, round 1: Peterson et al. 2021 on DANDI:000055 (0.261123.1703)**
2	
3	The claims file has 25 claims and the notebook tests all 25. My outcomes: 14 reproduced, 9 partially reproduced, 1 not reproduced, 1 blocked. I checked the archive API: the version exists and holds 55 files, 845.87 GB, which matches cell 2. I ran the helper functions on synthetic inputs and they behave as documented: the angle folding, the day-balanced splits, the band statistics, the one-hot design matrix and the Morlet bank (a sine at 11, 76 and 121 Hz peaks at its own frequency, and every wavelet spans ±0.2 s).
4	
5	### A. Outcomes
6	
7	| Claim | My outcome | Reason |
8	|---|---|---|
9	| subject-days | reproduced | Cell 17: subjects 01–12 have exactly the paper's days, 55 subject-days. |
10	| roi-projection-link | reproduced | Cells 7–8: after the code's row rule, the rows equal the electrodes with positions in all 12 subjects. The largest-weight region is the nearest centroid for 36–55% of electrodes, against a shuffle maximum of 8–14, for every seed. For S03 and S12 the criterion's "rows = electrodes" holds only when electrodes without positions are left out (problem 6). The eight regions with density > 3 match the claims file. |
11	| cohort | partially_reproduced | Cell 19: six of seven quantities are within tolerance. The dataset has 7 subjects with depth-labelled groups; the paper says 5. |
12	| fig2-event-counts | not_reproduced | Cell 21: the minimum is 211 (reading a) and 210 (reading b) against 151 ± 15.1. The median is 770.5 under reading a (outside tolerance) and 691 under reading b (inside). |
13	| fig2-features-differ-across-subjects | reproduced | Cell 23: every p is below 1e-32 under both readings. |
14	| fig2-reach-shape | partially_reproduced | Cell 25: the duration and magnitude parts hold in 12 of 12 subjects and pooled. The angle part holds in 0 of 12: the KDE peaks sit near ±60–75°, outside the 15° window. |
15	| fig2-bimanual-skew | reproduced | Cell 28
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md
```

```
1:# Protocol for an attempt
43:## Reader
45:### 1. Get the paper
59:### 2. Read the paper's code
69:### 3. Write the claims file
165:### 4. Data from outside the paper's own recordings
173:### 5. Check
186:### 6. Answer questions
199:## Author
215:### 1. Establish what can be tested
370:### 2. Check the data against its description
385:### 3. Write the entry
470:### 4. Lock, check and run
490:### 5. Record the attempt
599:### 6. Hand over for verification
637:## Repeat attempts
703:## Local and remote datasets
726:## Verifier
730:### Round 1: without the author's conclusions
755:### Round 2: with the author's conclusions
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,42p docs/protocol.md; sed -n 199,240p docs/protocol.md; sed -n 370,779p docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-18`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim's statement, expected values or criterion. A method detail the file
  lacks it takes from the paper, citing the passage, and it asks a reader
  only when it believes the file misreads the paper.
[... 474 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep peterson; wc -l attempts/peterson-2021-02.yaml claims/peterson-2021* entries/peterson-2021/*; ls executed/peterson-2021/ 2>/dev/null; cat questions/peterson-2021.yaml 2>/dev/null | head -50; cat entries/peterson-2021/entry.yaml
```

```
peterson-2021-02.yaml
   436 attempts/peterson-2021-02.yaml
   685 claims/peterson-2021.yaml
    41 entries/peterson-2021/README.md
   668 entries/peterson-2021/ajile.py
    24 entries/peterson-2021/entry.yaml
  2036 entries/peterson-2021/reproduce_peterson_2021.ipynb
     9 entries/peterson-2021/requirements.in
  1283 entries/peterson-2021/requirements.lock.txt
  5182 total
reproduce_peterson_2021.ipynb
result.json
schema_version: 1
name: peterson-2021
type: reproduction
title: Behavioral and neural variability of naturalistic arm movements (Peterson et al. 2021)
description: Tests the findings of Peterson, Singh, Wang, Rao and Brunton (2021) on dandiset 000055
  (AJILE12), which holds the ECoG, pose and wrist movement events of the paper's 12 subjects over 55
  days. It checks the cohort and the events, the behavioural features of Figure 2, the movement-related
  spectral power of Figures 3 to 5 and Table 1, projected to regions with the paper's projection
[... 16 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/peterson-2021-02.yaml"
}
```

```
1	schema_version: 3
2	id: peterson-2021-02
3	datasets:
4	- archive: dandi
5	  id: "000055"
6	  version: 0.261123.1703
7	  doi: 10.48324/dandi.000055/0.261123.1703
8	  relation: primary
9	paper: doi:10.1523/eneuro.0007-21.2021
10	date: 2026-11-25
11	entry: peterson-2021
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-18
20	  runner:
[... 417 more lines not kept]
```

**Agent calls Bash**

```bash
cat executed/peterson-2021/result.json | head -50; ls -la executed/peterson-2021/
```

```
{
 "entry": "peterson-2021",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_peterson_2021.ipynb",
   "ok": true,
   "seconds": 2175,
   "error": null
  }
 ]
}
total 428
drwxr-xr-x 3 runner runner   4096 Nov 25 08:17 .
drwxr-xr-x 3 runner runner   4096 Nov 25 08:36 ..
-rw-r--r-- 1 runner runner    321 Nov 25 08:17 .clean-run.json
drwxr-xr-x 5 runner runner   4096 Nov 25 07:40 .venv
-rw-r--r-- 1 runner runner 413849 Nov 25 08:17 reproduce_peterson_2021.ipynb
-rw-r--r-- 1 runner runner    175 Nov 25 08:17 result.json
```

**Agent**

Starting point: the full notebook takes about 36 minutes to run, so I'll make all fixes first, test them on subsets, and run the whole entry once. Next I'll read the helper and the notebook.

**Agent calls Read**

```json
{
 "file_path": "entries/peterson-2021/ajile.py"
}
```

```
1	"""Loading and measures for Peterson et al. (2021) on DANDI:000055 (AJILE12).
2	
3	Everything is streamed from the archive at a pinned version; nothing is written to disk.
4	
5	Where each parameter comes from:
6	
7	- Spectral method (claims file, opening comment, from the paper's Methods and code): Morlet
8	  wavelet power at 1 to 121 Hz in 5 Hz steps with n_cycles = frequency / 4, MNE's wavelet
9	  definition (sigma_t = n_cycles / (2 pi f), support of 5 sigma_t on each side, normalised;
10	  zero_mean False, the MNE 0.19 default of the code), decimated by 50 samples (10 Hz bins at
11	  500 Hz) aligned on the event, 10*log10 power. Because n_cycles / f is the same at every
12	  frequency, every wavelet spans +-0.2 s, so power is computed only at the time bins used here
13	  (-1.5 s to +1.0 s around onset); this gives the same values as convolving the whole 10 s
14	  segment.
15	- Baseline: each event's mean over the bins -1.5 to -1 s (inclusive) is subtracted, per
16	  electrode and frequency (claims file).
17	- Band power: bins 0 to 0.5 s (inclusive), LFB 11-31 Hz bins, HFB 76-96 Hz bins (claims file).
18	  The band mean (Methods) and the band median (code: median over time, then over frequency)
19	  are both returned.
20	- Segment rejection (Methods, "ECoG-event synchronization and segmentation": "discarding
[... 649 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python -c "
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    print(i,c['cell_type'],c.get('metadata',{}).get('tags'),len(s.splitlines()),'|',s[:150].replace('\n',' / '))
"
```

```
0 markdown None 53 | # Reproducing Peterson et al. (2021) from DANDI:000055 /  / Paper: Peterson, Singh, Wang, Rao and Brunton (2021), "Behavioral and Neural Variability of / Na
1 code None 17 | import os, re, time, zlib, resource / os.environ.setdefault("OMP_NUM_THREADS", "1") / import numpy as np / import pandas as pd / from scipy import stats / impor
2 code None 4 | # LOAD-META: list the assets of the pinned version and read every file's small datasets (streamed) / assets = ajile.list_assets() / metas = ajile.load_all
3 code ['sanity'] 19 | ev_all = ajile.event_table(metas) / subjects = sorted(ev_all.subject.unique()) / print("subjects:", subjects) / days = ev_all.groupby("subject").day.unique(
4 code ['sanity'] 27 | # Checks of the description against the values / m0 = metas[0] / print("ECoG unit:", m0["ecog_unit"], "conversion:", m0["ecog_conversion"], "rate:", m0["e
5 code ['sanity'] 10 | # Coarse behavioural labels (epochs) at the event times. The Methods exclude movements during / # sleep, unrelated experiments and private times. / lab = 
6 markdown None 9 | ## Projection matrices (outside input) and claim `roi-projection-link` /  / > The rows of the paper's projection matrices from electrodes to the eight reg
7 code ['claim:roi-projection-link'] 35 | files, fig_meta = ajile.figshare_files() / print("Figshare item", fig_meta["id"], "version", fig_meta["version"], fig_meta["doi"]) / proj, cents, link_row
8 code ['claim:roi-projection-link'] 39 | # Largest-weight region against the nearest region centroid, with mirrored MNI positions / rng = np.random.default_rng(seed("roi-projection-link")) / def 
9 markdown None 7 | **Result: reproduced.** The paper's code rule (keep the non-zero rows, drop the first) leaves as / many rows as electrodes with a position in all 12 sub
10 markdown None 6 | ## Spectral power of every event (streamed) /  / For each file, the chunk index of the ECoG series is read from the file's B-tree, and the chunks / holding 
11 code None 12 |
[... 86 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && python -c "
import json
nb=json.load(open('executed/peterson-2021/reproduce_peterson_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    out=''
    for o in c.get('outputs',[]):
        if 'text' in o: out+=''.join(o['text'])
    ex=c['metadata'].get('execution',{})
    print('=====',i, ex.get('iopub.execute_input'), ex.get('shell.execute_reply'))
    if i in (4,11,12,76,95,97): print(out[:3000])
"
```

```
===== 1 2026-11-25T07:40:50.055938Z 2026-11-25T07:40:54.960308Z
===== 2 2026-11-25T07:40:54.962591Z 2026-11-25T07:42:04.578164Z
===== 3 2026-11-25T07:42:04.580248Z 2026-11-25T07:42:04.609366Z
===== 4 2026-11-25T07:42:04.611277Z 2026-11-25T07:42:04.641915Z
ECoG unit: volts conversion: 1e-06 rate: 500.0 start: 0.0 chunks: (84375, 1)
pose unit: meters rate: 30.0 series: ['L_Ear', 'L_Elbow', 'L_Shoulder', 'L_Wrist', 'Nose', 'R_Ear', 'R_Elbow', 'R_Shoulder', 'R_Wrist']
all ECoG at 500 Hz: True ; all pose at 30 Hz: True
ElectricalSeries rows = electrodes table: True
ReachEvents timestamps = reaches start_time (max diff, s): 86400.0
S01: positions identical across files True; electrodes without position 0; bad per file [np.int64(9), np.int64(3), np.int64(3), np.int64(3)]; bad in every file 3; bad in any file 9
S02: positions identical across files True; electrodes without position 0; bad per file [np.int64(1), np.int64(1), np.int64(5), np.int64(6)]; bad in every file 1; bad in any file 7
S03: positions identical across files True; electrodes without position 16; bad per file [np.int64(17), np.int64(25), np.int64(20), np.int64(17)]; bad in every file 17; bad in any file 27
S04: positions identical across files True; electrodes without position 0; bad per file [np.int64(17), np.int64(4), np.int64(3), np.int64(2), np.int64(7)]; bad in every file 1; bad in any file 26
S05: positions identical across files True; electrodes without position 0; bad per file [np.int64(2), np.int64(2), np.int64(6)]; bad in every file 1; bad in any file 7
S06: positions identical across files True; electrodes without position 0; bad per file [np.int64(10), np.int64(10), np.int64(4), np.int64(6), np.int64(1)]; bad in every file 1; bad in any file 18
S07: positions identical across files True; electrodes without position 0; bad per file [np.int64(1), np.int64(1), np.int64(1), np.int64(1), np.int64(3)]; bad in every file 1; bad in any file 3
S08: positions identical across files True; electrodes withou
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python -c "
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
for i in [0,4,7,8,11,12,21,24,30,46,64,67,70,73,75,76,84,87,90,93,95,96]:
    print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
<persisted-output>
Output too large (34.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/6b785fe7-6d25-4c03-83bc-ff4e4c8e839d/tool-results/b45b1c4fk.txt

Preview (first 2KB):
===== 0
# Reproducing Peterson et al. (2021) from DANDI:000055

Paper: Peterson, Singh, Wang, Rao and Brunton (2021), "Behavioral and Neural Variability of
Naturalistic Arm Movements", eNeuro 8(3), ENEURO.0007-21.2021, doi:10.1523/eneuro.0007-21.2021.

Dataset: DANDI:000055 (AJILE12), version 0.261123.1703 (doi:10.48324/dandi.000055/0.261123.1703).
This version was asked for in the prompt of this attempt, a repeat attempt that tests what the
dataset holds now. It holds 55 NWB files, one per subject and recording day, with ECoG at 500 Hz,
pose at 30 Hz, the contralateral wrist movement events and their features. Every file is streamed;
nothing is downloaded.

Claims: `claims/peterson-2021.yaml`, written from the version of record (Europe PMC, PMC8225404)
and checked by a second reader. Method details the claims file does not give are taken from the
paper's Methods and its code (github.com/BruntonUWBio/naturalistic_arm_movements_ecog, commit
04c6faf2f219586fa834d10c614ef48a694cec55), cited where they are used. Outside input: the paper's
[... 21 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/6b785fe7-6d25-4c03-83bc-ff4e4c8e839d/tool-results/b45b1c4fk.txt"
}
```

```
1	===== 0
2	# Reproducing Peterson et al. (2021) from DANDI:000055
3	
4	Paper: Peterson, Singh, Wang, Rao and Brunton (2021), "Behavioral and Neural Variability of
5	Naturalistic Arm Movements", eNeuro 8(3), ENEURO.0007-21.2021, doi:10.1523/eneuro.0007-21.2021.
6	
7	Dataset: DANDI:000055 (AJILE12), version 0.261123.1703 (doi:10.48324/dandi.000055/0.261123.1703).
8	This version was asked for in the prompt of this attempt, a repeat attempt that tests what the
9	dataset holds now. It holds 55 NWB files, one per subject and recording day, with ECoG at 500 Hz,
10	pose at 30 Hz, the contralateral wrist movement events and their features. Every file is streamed;
11	nothing is downloaded.
12	
13	Claims: `claims/peterson-2021.yaml`, written from the version of record (Europe PMC, PMC8225404)
14	and checked by a second reader. Method details the claims file does not give are taken from the
15	paper's Methods and its code (github.com/BruntonUWBio/naturalistic_arm_movements_ecog, commit
16	04c6faf2f219586fa834d10c614ef48a694cec55), cited where they are used. Outside input: the paper's
17	projection matrices from electrodes to regions, Figshare item 12114408 version 1
18	(doi:10.6084/m9.figshare.12114408.v1).
19	
20	The notebook runs for about 40 minutes: about 12 minutes to stream the ECoG around 8088 events
[... 571 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && sed -n 1,60p claims/peterson-2021.yaml; grep -n -i "bad\|variant\|log(onset\|seed" claims/peterson-2021.yaml | head -60
```

```
# Claims for Peterson, Singh, Wang, Rao & Brunton (2021), eNeuro 8(3), ENEURO.0007-21.2021,
# "Behavioral and Neural Variability of Naturalistic Arm Movements", on dandiset 000055.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read. The version of record as served by Europe PMC (PMC8225404), from
# paper/10.1523-eneuro.0007-21.2021.txt: main text, Materials and Methods, figure legends,
# Tables 1 and 2, the legends of the Extended Data figures, and the review history. No PDF was
# supplied. The Extended Data figures (1-1, 2-1 to 2-4, 3-1, 4-1 to 4-7, 5-1, 6-1, 6-2) are
# EPS downloads and are not in the text; only their legends are. Claims that rest on them are
# taken from their legends and from the Results sentences that cite them. The per-subject
# electrode table (Extended Data Figure 1-1) and the per-subject feature confidence intervals
# (Extended Data Figures 2-3 and 2-4) could not be read.
#
# Code read. github.com/BruntonUWBio/naturalistic_arm_movements_ecog at commit
# 04c6faf2f219586fa834d10c614ef48a694cec55 (17 March 2021), Python 3.6 (MNE 0.19) and MATLAB.
# It holds compute_spectral_power.py and tfr_utils.py (Morlet power, baseline, bootstrap
# masking, projection to regions), the MATLAB projection of electrodes onto AAL regions
# (project_ecog_to_rois.m, EEGLAB 13.5.4b, Measure Projection Toolbox 1.661),
# fit_regression_models.py and regression_utils.py (regression), and notebooks for Figures 2,
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json
nb=json.load(open('executed/peterson-2021/reproduce_peterson_2021.ipynb'))
for i in [7,8,21,24,30,46,53,67]:
    c=nb['cells'][i]
    out=''
    for o in c.get('outputs',[]):
        if 'text' in o: out+=''.join(o['text'])
    print('=====',i); print(out[:4000])
"; grep -n -i "0\.5 s\|4 s\|false.positive\|spectrogram\|−1\.5\|-1.5" paper/*.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,400p /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/6b785fe7-6d25-4c03-83bc-ff4e4c8e839d/tool-results/bg3a43lae.txt | cut -c1-250 | grep -v "^S[0-9][0-9]: G\|^$" | head -150
```

```
===== 7
Figshare item 12114408 version 1 10.6084/m9.figshare.12114408.v1
    subject  csv_rows  electrodes  with_position  nonzero_rows                                   code_rule  matched
0         1        99          94             94            95    94 rows for 94 electrodes with positions     True
1         2        87          86             86            87    86 rows for 86 electrodes with positions     True
2         3        97          96             80            81    80 rows for 80 electrodes with positions     True
3         4        85          84             84            85    84 rows for 84 electrodes with positions     True
4         5       107         106            106           107  106 rows for 106 electrodes with positions     True
5         6        81          80             80            81    80 rows for 80 electrodes with positions     True
6         7        65          64             64            65    64 rows for 64 electrodes with positions     True
7         8        93          92             92            93    92 rows for 92 electrodes with positions     True
8         9       127         126            126           127  126 rows for 126 electrodes with positions     True
9        10       127         126            126           127  126 rows for 126 electrodes with positions     True
10       11       107         106            106           107  106 rows for 106 electrodes with positions     True
11       12       125         124            116           117  116 rows for 116 electrodes with positions     True
S01: rows after the first sum per region to (first 6 regions): [1. 1. 1. 1. 1. 1.]
mean density of the eight regions: {'Frontal_Mid_L': 4.42, 'Precentral_L': 5.15, 'Postcentral_L': 8.27, 'Parietal_Inf_L': 4.14, 'SupraMarginal_L': 4.28, 'Temporal_Sup_L': 4.45, 'Temporal_Mid_L': 9.23, 'Temporal_Inf_L': 5.33}
regions with mean density > 3: ['Precentral_L', 'Frontal_Mid_L', 'Postcentral_L', 'Parietal_Inf_L', 'SupraMargi
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && timeout 600 python -c "
import ajile, numpy as np
files,_=ajile.figshare_files()
assets=ajile.list_assets()
for s in [1,3,12]:
    m,c=ajile.load_projection(s,files)
    a=m.values.astype(float)
    nz=np.flatnonzero(a.mean(1)!=0)
    print(s, a.shape, 'zero rows', np.flatnonzero(a.mean(1)==0), 'first nonzero', nz[0])
    aid=assets[assets.subject==s].asset_id.iloc[0]
    meta=ajile.load_session_meta(aid)
    el=meta['electrodes']
    print('  no position idx', np.flatnonzero(el.x.isna().values), 'groups', el.group_name.unique())
" 2>&1 | tail -20
```

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import ajile, numpy as np
  File "entries/peterson-2021/ajile.py", line 43, in <module>
    import h5py
ModuleNotFoundError: No module named 'h5py'
```

**Agent calls Bash**

```bash
PY=../../executed/peterson-2021/.venv/bin/python; ls ../../executed/peterson-2021/.venv/bin | head; timeout 600 $PY -c "
import ajile, numpy as np
files,_=ajile.figshare_files()
assets=ajile.list_assets()
for s in [1,3,12]:
    m,c=ajile.load_projection(s,files)
    a=m.values.astype(float)
    nz=np.flatnonzero(a.mean(1)!=0)
    print(s, a.shape, 'zero rows', np.flatnonzero(a.mean(1)==0), 'first nonzero', nz[0])
    aid=assets[assets.subject==s].asset_id.iloc[0]
    meta=ajile.load_session_meta(aid)
    el=meta['electrodes']
    print('  no position idx', np.flatnonzero(el.x.isna().values), 'groups', el.group_name.unique(), 'ecog samples', meta['ecog_shape'])
" 2>&1 | tail -20
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
1 (99, 116) zero rows [95 96 97 98] first nonzero 0
  no position idx [] groups <StringArray>
['GRID', 'LID', 'LAT', 'LMT', 'LPT', 'LTO']
Length: 6, dtype: str ecog samples (43200000, 94)
3 (97, 116) zero rows [81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96] first nonzero 0
  no position idx [80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95] groups <StringArray>
['GRID', 'LAT', 'LMT', 'LAD', 'LPD']
Length: 5, dtype: str ecog samples (43200000, 96)
12 (125, 116) zero rows [73 74 75 76 77 78 79 80] first nonzero 0
  no position idx [72 73 74 75 76 77 78 79] groups <StringArray>
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper; grep -n -o -i ".\{200\}\(0\.5 and 4\|0\.5–4\|0\.5-4\|between 0\.5\|spectrogram\).\{200\}" paper/*.txt | head; grep -n -i "Figure 3\." paper/*.txt | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -o -i "Figure 3\. Group-level.\{1200\}" paper/*.txt | head -2; grep -o -i ".\{300\}decrease in low-frequency.\{100\}" paper/*.txt | head -3; grep -o -i ".\{200\}movement onset.\{0,40\}s.\{200\}" paper/*.txt | grep -i "−\|–" | head -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python -c "
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
for i in [1,3,13,50,53,56,59,61,78,81]:
    print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
===== 1
import os, re, time, zlib, resource
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import ajile

KEY = "peterson-2021"
def seed(claim):
    """Seed of a claim's generator (protocol, author step 3)."""
    return zlib.crc32(f"{KEY}/{claim}".encode())
SEED_OFFSETS = [0, 1000, 2000, 3000, 4000]
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 40)
T0 = time.time()
print("dandiset", ajile.DANDISET, "version", ajile.VERSION)
===== 3
ev_all = ajile.event_table(metas)
[... 167 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python - <<'EOF'
import re
p='ajile.py'; s=open(p).read()
s=s.replace('''- Good electrodes: the `good` column of each session's electrodes table (Methods: bad
  electrodes removed). It differs between sessions of a subject; each event uses the flags of
  its own session (assumption, stated in the notebook).''','''- Good electrodes: the `good` column of the electrodes tables (Methods: bad electrodes
  removed). It differs between sessions of a subject. The claims file's opening comment says
  bad electrodes get weight 0 and the weights are renormalised per subject, so the electrodes
  good in every file of the subject are used for the segment rejection, the projection and the
  regression (assumption, stated in the notebook). The flags of each event's own file are a
  variant for the projection.''')
s=s.replace('''  electrodes by order, bad electrodes weight 0, each region's weights renormalised to sum 1.''','''  electrodes by order, bad electrodes weight 0, each region's weights renormalised to sum 1.
  An electrode whose power is not finite somewhere in an event's window (a stretch of zeros
  gives -inf dB) gets weight 0 in that event, and the region's weights are renormalised again
  (standard choice; the counts are printed in the notebook).''')
s=s.replace('''def session_spectral(asset_id, event_times, good, weights, n_threads=6, batch_chunks=6,
                     wrist_names=("L_Wrist", "R_Wrist")):
    """Spectral measures, segment checks and wrist windows for the events of one file.

    good: bool (n_ch,) good electrodes of this session. weights: (n_ch, n_roi) projection
    weights with bad electrodes already 0 and columns summing to 1.
    Returns a dict of arrays, one row per event.
    """''','''def project(weights, db):
    """Region power of one event: db (n_ch, n_freq, n_bins), weights (n_ch, n_roi) with bad
    electrodes 0. Electrodes with any non-finite value get weight 0 and each region's weights
    are renormalised. Returns (region power (n_roi, n_freq, n_bins), weighted electrodes dropped)."""
    fin = np.isfinite(db).all(axis=(1, 2))
    w = weights * fin[:, None]
    w = w / w.sum(axis=0)
    dropped = int(((weights > 0).any(axis=1) & ~fin).sum())
    return np.einsum("cr,cfb->rfb", w, np.where(np.isfinite(db), db, 0.0)), dropped


def session_spectral(asset_id, event_times, good, weights, weights_alt=None, n_threads=6, batch_chunks=6,
                     wrist_names=("L_Wrist", "R_Wrist")):
    """Spectral measures, segment checks and wrist windows for the events of one file.

    good: bool (n_ch,) good electrodes (here those good in every file of the subject).
    weights: (n_ch, n_roi) projection weights with bad electrodes already 0 and columns summing
    to 1; weights_alt: a second set (the variant with the file's own flags).
    Returns a dict of arrays, one row per event.
    """''')
s=s.replace('''    region = np.full((n_ev, nr, nf, nb), np.nan, np.float32)
''','''    region = np.full((n_ev, nr, nf, nb), np.nan, np.float32)
    region_alt = np.full((n_ev, nr, nf, nb), np.nan, np.float32) if weights_alt is not None else None
    n_dropped = np.zeros(n_ev, int)      # weighted electrodes with non-finite power in the event
    n_zero_el = np.zeros(n_ev, int)      # good electrodes with any exact zero sample in the segment
''')
s=s.replace('''                allzero[i] = bool(np.all(seg[good] == 0, axis=0).any())
''','''                allzero[i] = bool(np.all(seg[good] == 0, axis=0).any())
                n_zero_el[i] = int((seg[good] == 0).any(axis=1).sum())
''')
s=s.replace('''                dbg = np.where(np.isfinite(db), db, 0.0)
                region[i] = np.einsum("cr,cfb->rfb", weights, dbg)
''','''                region[i], n_dropped[i] = project(weights, db)
                if weights_alt is not None:
                    region_alt[i] = project(weights_alt, db)[0]
''')
s=s.replace('''    return dict(region=region, elec=elec, seg_db=seg_db, hf_db=hf_db, inside=inside, allzero=allzero,
                wrist=wrist, wrist_t=k / prate)''','''    return dict(region=region, region_alt=region_alt, elec=elec, seg_db=seg_db, hf_db=hf_db, inside=inside,
                allzero=allzero, n_dropped=n_dropped, n_zero_el=n_zero_el, wrist=wrist, wrist_t=k / prate)''')
s=s.replace('''def _spectral_job(args):
    import os
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    asset_id, times, good, weights = args
    return session_spectral(asset_id, times, good, weights)


def run_spectral(jobs, workers=8):
    """jobs: list of (asset_id, event_times, good, weights). Runs files in parallel processes."""''','''def _spectral_job(args):
    import os
    os.environ.setdefault("OMP_NUM_THREADS", "1")
    asset_id, times, good, weights, weights_alt = args
    return session_spectral(asset_id, times, good, weights, weights_alt)


def run_spectral(jobs, workers=8):
    """jobs: list of (asset_id, event_times, good, weights, weights_alt). Runs files in parallel processes."""''')
# regression: variant mode
s=s.replace('''    seed, target names, which targets get Delta R2. Returns a list of per-model dicts."""''','''    seed, target names, which targets get Delta R2. With variant True, only the 90/10 fits and
    the Methods' Delta R2 are run (for the variants). Returns a list of per-model dicts."""''')
s=s.replace('''                row["r2_80"] = fit_models(X, names, y, splits80, chosen)["r2"]
''','''                if not args.get("variant"):
                    row["r2_80"] = fit_models(X, names, y, splits80, chosen)["r2"]
''')
s=s.replace('''                    row["delta_code"] = fit_models(X, names, y, splits80, chosen, delta=True, shuffle_rng=shuf,
                                                   code_shuffle=True)["delta"]''','''                    if not args.get("variant"):
                        row["delta_code"] = fit_models(X, names, y, splits80, chosen, delta=True, shuffle_rng=shuf,
                                                       code_shuffle=True)["delta"]''')
open(p,'w').write(s)
EOF
grep -n "region_alt\|variant\|n_zero_el" ajile.py | head -30
```

```
/bin/bash: line 1: cd: entries/peterson-2021: No such file or directory
```

**Agent calls Bash**

```bash
pwd; grep -n "region_alt\|variant\|n_zero_el" ajile.py | head -30
```

```
entries/peterson-2021
```

**Agent calls Bash**

```bash
cat > $TMPDIR/patch1.py <<'EOF'
p='ajile.py'; s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a[:80]
    s=s.replace(a,b)
rep('''- Good electrodes: the `good` column of each session's electrodes table (Methods: bad
  electrodes removed). It differs between sessions of a subject; each event uses the flags of
  its own session (assumption, stated in the notebook).''','''- Good electrodes: the `good` column of the electrodes tables (Methods: bad electrodes
  removed). It differs between sessions of a subject. The claims file's opening comment says
  bad electrodes get weight 0 and the weights are renormalised per subject, so the electrodes
  good in every file of the subject are used for the segment rejection, the projection and the
  regression (assumption, stated in the notebook). The flags of each event's own file are a
  variant for the projection.''')
rep('''  electrodes by order, bad electrodes weight 0, each region's weights renormalised to sum 1.''','''  electrodes by order, bad electrodes weight 0, each region's weights renormalised to sum 1.
  An electrode whose power is not finite somewhere in an event's window (a stretch of zeros
  gives -inf dB) gets weight 0 in that event, and the region's weights are renormalised again
  (standard choice; the counts are printed in the notebook).''')
rep('''def session_spectral(asset_id, event_times, good, weights, n_threads=6, batch_chunks=6,
                     wrist_names=("L_Wrist", "R_Wrist")):
    """Spectral measures, segment checks and wrist windows for the events of one file.

    good: bool (n_ch,) good electrodes of this session. weights: (n_ch, n_roi) projection
    weights with bad electrodes already 0 and columns summing to 1.
    Returns a dict of arrays, one row per event.
    """''','''def project(weights, db):
    """Region power of one event: db (n_ch, n_freq, n_bins), weights (n_ch, n_roi) with bad
    electrodes 0. Electrodes with any non-finite value get weight 0 and each region's weights
    are renormalised. Returns (region power (n_roi, n_freq, n_bins), weighted electrodes dropped)."""
    fin = np.isfinite(db).all(axis=(1, 2))
    w = weights * fin[:, None]
    w = w / w.sum(axis=0)
    dropped = int(((weights > 0).any(axis=1) & ~fin).sum())
    return np.einsum("cr,cfb->rfb", w, np.where(np.isfinite(db), db, 0.0)), dropped


def session_spectral(asset_id, event_times, good, weights, weights_alt=None, n_threads=6, batch_chunks=6,
                     wrist_names=("L_Wrist", "R_Wrist")):
    """Spectral measures, segment checks and wrist windows for the events of one file.

    good: bool (n_ch,) good electrodes (here those good in every file of the subject).
    weights: (n_ch, n_roi) projection weights with bad electrodes already 0 and columns summing
    to 1; weights_alt: a second set (the variant with the file's own flags).
    Returns a dict of arrays, one row per event.
    """''')
rep('''    region = np.full((n_ev, nr, nf, nb), np.nan, np.float32)
''','''    region = np.full((n_ev, nr, nf, nb), np.nan, np.float32)
    region_alt = np.full((n_ev, nr, nf, nb), np.nan, np.float32) if weights_alt is not None else None
    n_dropped = np.zeros(n_ev, int)      # weighted electrodes with non-finite power in the event
    n_zero_el = np.zeros(n_ev, int)      # good electrodes with any exact zero sample in the segment
''')
rep('''                allzero[i] = bool(np.all(seg[good] == 0, axis=0).any())
''','''                allzero[i] = bool(np.all(seg[good] == 0, axis=0).any())
                n_zero_el[i] = int((seg[good] == 0).any(axis=1).sum())
''')
rep('''                dbg = np.where(np.isfinite(db), db, 0.0)
                region[i] = np.einsum("cr,cfb->rfb", weights, dbg)
''','''                region[i], n_dropped[i] = project(weights, db)
                if weights_alt is not None:
                    region_alt[i] = project(weights_alt, db)[0]
''')
rep('''    return dict(region=region, elec=elec, seg_db=seg_db, hf_db=hf_db, inside=inside, allzero=allzero,
                wrist=wrist, wrist_t=k / prate)''','''    return dict(region=region, region_alt=region_alt, elec=elec, seg_db=seg_db, hf_db=hf_db, inside=inside,
                allzero=allzero, n_dropped=n_dropped, n_zero_el=n_zero_el, wrist=wrist, wrist_t=k / prate)''')
rep('''    asset_id, times, good, weights = args
    return session_spectral(asset_id, times, good, weights)


def run_spectral(jobs, workers=8):
    """jobs: list of (asset_id, event_times, good, weights). Runs files in parallel processes."""''','''    asset_id, times, good, weights, weights_alt = args
    return session_spectral(asset_id, times, good, weights, weights_alt)


def run_spectral(jobs, workers=8):
    """jobs: list of (asset_id, event_times, good, weights, weights_alt). Runs files in parallel processes."""''')
rep('''    seed, target names, which targets get Delta R2. Returns a list of per-model dicts."""''','''    seed, target names, which targets get Delta R2. With "variant" set, only the 90/10 fits and
    the Methods' Delta R2 are run (for the variants). Returns a list of per-model dicts."""''')
rep('''                row["r2_80"] = fit_models(X, names, y, splits80, chosen)["r2"]
''','''                if not args.get("variant"):
                    row["r2_80"] = fit_models(X, names, y, splits80, chosen)["r2"]
''')
rep('''                    row["delta_code"] = fit_models(X, names, y, splits80, chosen, delta=True, shuffle_rng=shuf,
                                                   code_shuffle=True)["delta"]''','''                    if not args.get("variant"):
                        row["delta_code"] = fit_models(X, names, y, splits80, chosen, delta=True, shuffle_rng=shuf,
                                                       code_shuffle=True)["delta"]''')
open(p,'w').write(s)
EOF
python $TMPDIR/patch1.py && grep -n "region_alt\|variant\|n_zero_el" ajile.py | head -30
```

```
34:  variant for the projection.
329:    to 1; weights_alt: a second set (the variant with the file's own flags).
345:    region_alt = np.full((n_ev, nr, nf, nb), np.nan, np.float32) if weights_alt is not None else None
347:    n_zero_el = np.zeros(n_ev, int)      # good electrodes with any exact zero sample in the segment
399:                n_zero_el[i] = int((seg[good] == 0).any(axis=1).sum())
426:                    region_alt[i] = project(weights_alt, db)[0]
446:    return dict(region=region, region_alt=region_alt, elec=elec, seg_db=seg_db, hf_db=hf_db, inside=inside,
447:                allzero=allzero, n_dropped=n_dropped, n_zero_el=n_zero_el, wrist=wrist, wrist_t=k / prate)
611:    seed, target names, which targets get Delta R2. With "variant" set, only the 90/10 fits and
612:    the Methods' Delta R2 are run (for the variants). Returns a list of per-model dicts."""
633:                if not args.get("variant"):
640:                    if not args.get("variant"):
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nbpatch.py <<'EOF'
import json
P='reproduce_peterson_2021.ipynb'
nb=json.load(open(P))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s): C[i]['source']=s.splitlines(True)
def rep(i,a,b):
    s=src(i); assert s.count(a)==1,(i,a[:60]); setsrc(i,s.replace(a,b))
def tags(i): return C[i].get('metadata',{}).get('tags')
assert tags(4)==['sanity'] and tags(7)==['claim:roi-projection-link'] and tags(21)==['claim:cohort']
# cell 4: event time mismatch per file
rep(4,'''print("ReachEvents timestamps = reaches start_time (max diff, s):",
      max(np.abs(m["event_times"] - m["reaches"].start_time.values).max() for m in metas))
''','''print("ReachEvents timestamps = reaches start_time (max diff, s):",
      max(np.abs(m["event_times"] - m["reaches"].start_time.values).max() for m in metas))
for m in metas:
    d = np.abs(m["event_times"] - m["reaches"].start_time.values)
    if (d > 1).any():
        k = np.flatnonzero(d > 1)
        print(f"  S{int(m['subject_id']):02d} day {m['session_id']}: {len(k)} event(s) differ by more than 1 s; ReachEvents",
              m["event_times"][k].round(1), "s, start_time", m["reaches"].start_time.values[k].round(1), "s; ECoG length",
              m["ecog_shape"][0] / m["ecog_rate"], "s")
print("events differing by more than 1 s, all files:",
      sum(int((np.abs(m["event_times"] - m["reaches"].start_time.values) > 1).sum()) for m in metas))
''')
# cell 7: where the zero rows sit
rep(7,'''    dens_rows.append(first)
''','''    dens_rows.append(first)
    # rows after the density row, in order: are the zero rows those of the electrodes without a position?
    after = a[np.flatnonzero(a.mean(axis=1) != 0)[0] + 1:]
    zero = np.flatnonzero(after.mean(axis=1) == 0)
    nopos = np.flatnonzero(el_first[s].x.isna().values)
    n_el = len(el_first[s])
    print(f"S{s:02d}: zero rows among the first {n_el} after the density row at", list(zero[zero < n_el]),
          "; electrodes without a position at", list(nopos), "; same:", np.array_equal(zero[zero < n_el], nopos),
          "; zero rows past the last electrode:", int((zero >= n_el).sum()))
''')
# cell 8: shift test
rep(8,'''n_ok = int((link.matched & res_link.beats_all_shuffles).sum())''','''# Shifted alignment: rows applied k places later or earlier (an offset the shuffle null cannot detect)
def shift_match(s, k):
    names, a = proj[s]
    c = cents[s].values.astype(float)
    el = el_first[s]
    known = el.x.notna().values
    pos = el[["x", "y", "z"]].values[known].copy()
    pos[:, 0] = -np.abs(pos[:, 0])
    W = a[known]
    valid = np.isfinite(c).all(axis=1) & (np.abs(c).sum(axis=1) > 0)
    d = np.linalg.norm(pos[:, None, :] - c[None, :, :], axis=2)
    d[:, ~valid] = np.inf
    near = d.argmin(axis=1)
    i = np.arange(len(W)); j = i + k
    ok = (j >= 0) & (j < len(W))
    Wk = W[j[ok]]
    has = Wk.sum(axis=1) > 0
    top = np.where(valid[None, :], Wk, -np.inf).argmax(axis=1)
    return float((near[i[ok]][has] == top[has]).mean())
shifts = pd.DataFrame({k: [shift_match(s, k) for s in subjects] for k in range(-3, 4)}, index=[f"S{s:02d}" for s in subjects])
print("fraction of electrodes whose largest-weight region is the nearest, rows shifted by k:")
print(shifts.round(3).to_string())
print("subjects where the unshifted rows give the highest fraction:", int((shifts.idxmax(axis=1) == 0).sum()), "of 12")
n_ok = int((link.matched & res_link.beats_all_shuffles).sum())''')
# cell 11: subject-level good electrodes, per-file flags as a variant
rep(11,'''jobs = []
for m in metas:
    s = int(m["subject_id"])
    good = m["electrodes"].good.values.astype(bool)
    w = ajile.session_weights(proj[s][1][:, roi_idx], good)
    jobs.append((m["asset_id"], m["event_times"], good, w))''','''# Electrodes good in every file of the subject (main); each file's own flags (variant, projection only)
GOOD_ALL = {s: np.all([m["electrodes"].good.values.astype(bool) for m in metas if int(m["subject_id"]) == s], axis=0)
            for s in subjects}
W_MAIN = {s: ajile.session_weights(proj[s][1][:, roi_idx], GOOD_ALL[s]) for s in subjects}
jobs = []
for m in metas:
    s = int(m["subject_id"])
    w_file = ajile.session_weights(proj[s][1][:, roi_idx], m["electrodes"].good.values.astype(bool))
    jobs.append((m["asset_id"], m["event_times"], GOOD_ALL[s], W_MAIN[s], w_file))''')
# cell 12
rep(12,'''ev["hf_db"] = np.concatenate([r["hf_db"] for r in spec])
REG = np.concatenate([r["region"] for r in spec])          # (event, region, freq, bin), dB, no baseline
REG_BS = REG - REG[..., ajile.BASE].mean(axis=-1, keepdims=True)''','''ev["hf_db"] = np.concatenate([r["hf_db"] for r in spec])
ev["n_dropped"] = np.concatenate([r["n_dropped"] for r in spec])
ev["n_zero_el"] = np.concatenate([r["n_zero_el"] for r in spec])
ev["event_time"] = np.concatenate([m["event_times"] for m in metas])
REG = np.concatenate([r["region"] for r in spec])          # (event, region, freq, bin), dB, no baseline
REG_BS = REG - REG[..., ajile.BASE].mean(axis=-1, keepdims=True)
REG_ALT = np.concatenate([r["region_alt"] for r in spec])  # variant: each file's own good-electrode flags
for r in spec:
    r["region"] = r["region_alt"] = None''')
rep(12,'''ev["keep"] = ev.inside & ~ev.nan_data & ~ev.allzero & ~ev.low_power & ~ev.hf_bad
drop = ev.groupby("subject").agg(events=("keep", "size"), no_ecog=("inside", lambda x: int((~x).sum())),''','''# The ECoG and pose windows use the ReachEvents time, the features the reaches table's start_time;
# an event where they disagree (data check) cannot be placed, and counts as missing data.
ev["time_mismatch"] = (ev.event_time - ev.start_time).abs() > 1
ev["keep"] = ev.inside & ~ev.nan_data & ~ev.allzero & ~ev.low_power & ~ev.hf_bad & ~ev.time_mismatch
drop = ev.groupby("subject").agg(events=("keep", "size"), no_ecog=("inside", lambda x: int((~x).sum())),
                                 time_mismatch=("time_mismatch", "sum"),''')
rep(12,'''print("NaN region values among kept events:", int(np.isnan(REG[ev.keep.values]).sum()))''','''print("NaN region values among kept events:", int(np.isnan(REG[ev.keep.values]).sum()), "; variant:",
      int(np.isnan(REG_ALT[ev.keep.values]).sum()))
kk = ev[ev.keep]
print("kept events with a good electrode holding exact zeros in the segment:", int((kk.n_zero_el > 0).sum()), "of", len(kk),
      "; per subject:", kk[kk.n_zero_el > 0].groupby("subject").size().to_dict())
print("kept events with a weighted electrode whose power is not finite (weight 0 in that event):", int((kk.n_dropped > 0).sum()),
      "; electrodes dropped in such events, largest:", int(kk.n_dropped.max()))''')
# cell 13: clock check with the main weights
rep(13,'''        good = m["electrodes"].good.values.astype(bool)
        w = ajile.session_weights(proj[s][1][:, roi_idx], good)[:, 1]
        w = np.nan_to_num(w)''','''        w = np.nan_to_num(W_MAIN[s][:, 1])''')
rep(13,'''# same segments (same electrodes, same events). Precentral-weighted mean over good electrodes.''','''# same segments (same electrodes, same events). Precentral-weighted mean over the subject's good electrodes.''')
# cell 21: grid-only variant
rep(21,'''# variant: the grid only as surface (a reading of 'surface' the data do not settle)''','''# variant: the grid only as surface (a reading of 'surface' the data do not settle)
grid_n = []
for s in subjects:
    m = [x for x in metas if int(x["subject_id"]) == s][0]
    gdesc = m["electrodes"].group_name.map(m["groups"]).fillna("")
    grid_n.append(int(gdesc.str.contains("grid", case=False).sum()))
grid_n = np.array(grid_n)
print("grid electrodes per subject:", dict(zip(subjects, grid_n)), f"; mean {grid_n.mean():.2f} (SD {grid_n.std(ddof=1):.2f}),",
      "expected 87.0 +- 12.9:", "within" if abs(grid_n.mean() - 87.0) <= 12.9 else "OUTSIDE")''')
# cell 24: 0.5-4 s duration filter variant
rep(24,'''    print(f"{col}: min {c.min()}, max {c.max()}, median {c.median()} -> all three within tolerance: {ok}")''','''    print(f"{col}: min {c.min()}, max {c.max()}, median {c.median()} -> all three within tolerance: {ok}")
# not a reading of the criterion: the Methods keep events lasting 0.5 to 4 s
for name, E in (("a_all", EVA), ("b_kept", EVB)):
    c = E[E.duration.between(0.5, 4)].groupby("subject").size()
    print(f"{name} with 0.5-4 s durations: per subject {c.to_dict()}; min {c.min()}, max {c.max()}, median {c.median()};",
          f"events removed {len(E) - c.sum()}")''')
# cell 30: density at fixed angles
rep(30,'''# reading a as a variant''','''# density of the folded angle at fixed angles (the kernel density has no boundary correction at +-90)
dt = pd.DataFrame({f"{x:+d}": [stats.gaussian_kde(g.angle.values)(x)[0] for _, g in list(EVB.groupby("subject")) + [("pooled", EVB)]]
                   for x in (-90, -75, 0, 75, 90)}, index=[f"S{s:02d}" for s in subjects] + ["pooled"])
print("density of the folded angle (per degree):"); print(dt.round(5).to_string())
print("fraction of events within 15 degrees of -90 / +90, pooled:", round(float((EVB.angle <= -75).mean()), 3),
      round(float((EVB.angle >= 75).mean()), 3))
# reading a as a variant''')
# cell 46: mask_group takes the arrays
rep(46,'''def mask_group(rng, n_boot=2000):
    masked = np.zeros_like(GROUP)
    for r in range(GROUP.shape[0]):
        S = SUBJ_MED[:, r]                                   # (subj, f, b)''','''def mask_group(rng, n_boot=2000, group=None, subj_med=None):
    group = GROUP if group is None else group
    subj_med = SUBJ_MED if subj_med is None else subj_med
    masked = np.zeros_like(group)
    for r in range(group.shape[0]):
        S = subj_med[:, r]                                   # (subj, f, b)''')
rep(46,'''        obs = GROUP[r]''','''        obs = group[r]''')
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
python $TMPDIR/nbpatch.py && echo ok; tail -c 300 reproduce_peterson_2021.ipynb | head -5; git -C . status 2>&1 | head -2
```

```
ok
:.1f} min; peak memory of this process \"\n",
    "      f\"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")"
   ]
  }
 ],
fatal: not a git repository (or any of the parent directories): .git
```

**Agent calls Bash**

```bash
grep -n '\\"region\\"\]\|region_alt' reproduce_peterson_2021.ipynb | head
```

```
423:    "REG = np.concatenate([r[\"region\"] for r in spec])          # (event, region, freq, bin), dB, no baseline\n",
425:    "REG_ALT = np.concatenate([r[\"region_alt\"] for r in spec])  # variant: each file's own good-electrode flags\n",
427:    "    r[\"region\"] = r[\"region_alt\"] = None\n",
1762:    "MAIN[\"region\"] = [region_of(s, e) for s, e in zip(MAIN.subject, MAIN.electrode)]\n",
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nbpatch2.py <<'EOF'
import json, copy
P='reproduce_peterson_2021.ipynb'
nb=json.load(open(P))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s): C[i]['source']=s.splitlines(True)
assert C[56]['metadata']['tags']==['claim:fig4-precentral-subject-variability']
s=src(56)
s=s.replace('P = SUBJ_MED[:, 1].copy()','P = subj_med[:, 1].copy()').replace('print(','out(')
body=''.join('    '+l if l.strip() else l for l in s.splitlines(True))
s=('def fig4_parts(subj_med, show=True):\n    out = print if show else (lambda *a, **k: None)\n'+body.rstrip('\n')+
   '\n    return [part1, part2, part3, part4], p1, width\nparts4, p1, width = fig4_parts(SUBJ_MED)\n')
setsrc(56,s)
def code(source, tags):
    return {"cell_type":"code","execution_count":None,"metadata":{"tags":tags},"outputs":[],"source":source.splitlines(True)}
def md(source):
    return {"cell_type":"markdown","metadata":{},"source":source.splitlines(True)}
assert C[74]['source'][0].startswith('**Result: reproduced.** The largest deviation')
variant_md = md('''## Region results with each file's own good-electrode flags (variant)

The main analysis projects every event with the electrodes good in every file of the subject (the
claims file's opening comment: bad electrodes get weight 0 and the weights are renormalised per
subject). Here the region claims are recomputed with the flags of each event's own file, the
assumption of the first round of this attempt. The bootstrap mask uses the generator of claim
fig3-group-lfb-decrease-hfb-increase plus 1. This variant does not decide an outcome.
''')
variant_code = code('''REG_ALT_BS = REG_ALT - REG_ALT[..., ajile.BASE].mean(axis=-1, keepdims=True)
SUBJ_MED_A = np.stack([np.nanmedian(REG_ALT_BS[kbv & (subj_v == s)], axis=0) for s in subjects])
GROUP_A = SUBJ_MED_A.mean(axis=0)
GROUP_A = GROUP_A - GROUP_A[..., ajile.BASE].mean(axis=-1, keepdims=True)
MASKED_A = mask_group(np.random.default_rng(seed("fig3-group-lfb-decrease-hfb-increase") + 1), group=GROUP_A, subj_med=SUBJ_MED_A)
tA = fig3_outcome(MASKED_A)
print("fig3-group: named regions holding under a:", int(tA.loc[named3, "holds_a"].sum()), "; under b:", int(tA.loc[named3, "holds_b"].sum()))
print(tA.loc[named3, ["low_a", "high_a"]].round(3).to_dict())
_, rA = largest(MASKED_A)
print("fig3-sensorimotor:", {k: (v[0], v[1], v[2]) for k, v in rA.items()})
_, _, aA, bA, pA = widespread(MASKED_A)
print("fig3-lfb-more-widespread: (a)", aA, "; (b)", np.round(bA, 3), "; supramarginal / superior temporal:", pA)
partsA, p1A, _ = fig4_parts(SUBJ_MED_A, show=False)
print("fig4: parts holding", parts4 and partsA, "; subjects without the part 1 pattern:", list(p1A.index[~p1A.holds]),
      p1A[~p1A.holds].round(3).to_dict("index"))
stA = ajile.band_stats(REG_ALT_BS[:, 1])
EA = ev.copy()
for k, v in stA.items():
    EA["pre_" + k] = v
EA = EA[EA.keep]
print("fig5-band-power: H (band mean) LFB", round(stats.kruskal(*[x.pre_lfb_mean.values for _, x in EA.groupby("subject")]).statistic, 1),
      "HFB", round(stats.kruskal(*[x.pre_hfb_mean.values for _, x in EA.groupby("subject")]).statistic, 1))
inA, agA, devA = 0, 0, []
for s, g in EA.groupby("subject"):
    for bi, band in enumerate(("lfb", "hfb")):
        lo, hi_ = T1[s][bi]
        inA += lo <= g[f"pre_{band}_mean"].mean() <= hi_
        p = stats.kruskal(*[x[f"pre_{band}_mean"].values for _, x in g.groupby("day")]).pvalue
        agA += (p < 0.05) == (s in paper_sig[band])
        dm = g.groupby("day")[f"pre_{band}_mean"].mean()
        devA.append((dm - g[f"pre_{band}_mean"].mean()).abs().max())
print("table1: inside (mean of band mean)", inA, "of 24; fig5-recording-day-effects: pairs agreeing (band mean)", agA,
      "of 24; discussion: largest day deviation", round(float(max(devA)), 3), "dB")
''', ["claim:fig3-group-lfb-decrease-hfb-increase","claim:fig3-sensorimotor-largest","claim:fig3-lfb-more-widespread",
      "claim:fig4-precentral-subject-variability","claim:fig5-band-power-differs-across-subjects","claim:table1-subject-band-power-ci",
      "claim:fig5-recording-day-effects","claim:discussion-day-changes-small"])
C.insert(75, variant_md); C.insert(76, variant_code)
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
python $TMPDIR/nbpatch2.py && python -c "
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
print(''.join(nb['cells'][56]['source']))
for i in range(74,80): print(i, nb['cells'][i]['source'][0][:80])"
```

```
def fig4_parts(subj_med, show=True):
    out = print if show else (lambda *a, **k: None)
    P = subj_med[:, 1].copy()                                     # precentral (subj, f, b), unmasked
    P = P - P[..., ajile.BASE].mean(axis=-1, keepdims=True)
    spec4 = P[..., ajile.WIN].mean(axis=-1)                        # (subj, f)
    F = ajile.FREQS
    tab4 = pd.DataFrame(spec4, index=[f"S{s:02d}" for s in subjects], columns=[int(f) for f in F])
    out(tab4.round(2).to_string())
    p1 = pd.DataFrame({"lfb_8_32": spec4[:, ajile.LFB].mean(1), "hfb_76_100": spec4[:, ajile.HFB].mean(1)}, index=tab4.index)
    p1["holds"] = (p1.lfb_8_32 < 0) & (p1.hfb_76_100 > 0)
    out(p1.round(3).to_string())
    part1 = bool(p1.holds.all())
    i116, i121 = list(F).index(116), list(F).index(121)
    part2_rows = {s: (spec4[subjects.index(s), i116] > 0 and spec4[subjects.index(s), i121] > 0) for s in [3, 6, 7, 8, 11]}
    part2 = all(part2_rows.values())
    hi = F >= 56
    p3 = {}
    for s in [9, 12]:
        v = spec4[subjects.index(s)]
        fmax = F[hi][np.argmax(v[hi])]; top = v[hi].max()
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nbpatch3.py <<'EOF'
import json
P='reproduce_peterson_2021.ipynb'
nb=json.load(open(P))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s): C[i]['source']=s.splitlines(True)
def rep(i,a,b):
    s=src(i); assert s.count(a)==1,(i,a[:60]); setsrc(i,s.replace(a,b))
rep(76,'''print("fig4: parts holding", parts4 and partsA, "; subjects''','''print("fig4: parts holding", sum(partsA), "of 4", partsA, "; subjects''')
rep(78,'''def regression_jobs(seed0, include_bad=False):''','''def regression_jobs(seed0, include_bad=False, log_speed=False):''')
rep(78,'''        X, names = ajile.design_matrix(Ek)''','''        X, names = ajile.design_matrix(Ek, log_speed=log_speed)''')
i=97
assert src(i).startswith('# Seed sensitivity of the regression')
setsrc(i,'''# Variants of the Figure 6 models. Each refits the models with R2 > 0.03 under the main fits (all
# models that pass 0.05 come from these), with the Methods' 90/10 splits and Delta R2 where R2 > 0.05.
def fig6_summary(df):
    """Per band: models with R2 > 0.05, the two features with the largest median Delta R2
    (fig6c), the median reach angle coefficient (fig6d-upward) and the two largest median
    coefficient magnitudes (fig6d-largest, reading a)."""
    out = {}
    for band in ("lfb", "hfb"):
        M = df[(df.band == band) & (df.r2 > 0.05)]
        D = pd.DataFrame([d for d in M.delta if isinstance(d, dict)]).median().sort_values(ascending=False)
        Cf = pd.DataFrame(list(M.coef))
        ca = Cf.abs().median().sort_values(ascending=False)
        out[band] = dict(n=len(M), top_delta=list(D.index[:2]), angle_coef=round(float(Cf.angle.median()), 3),
                         top_coef=list(ca.index[:2]))
    return out
def variant_jobs(jobs0, models, **kw):
    jobs = []
    for j in jobs0:
        es = set(models[models.subject == j["subject"]].electrode)
        k = np.array([e in es for e in j["electrodes"]])
        if not k.any():
            continue
        jj = dict(j); jj["Y"] = j["Y"][:, k][:, :, :2]; jj["electrodes"] = j["electrodes"][k]
        jj["targets"] = ["lfb_mean", "hfb_mean"]; jj["variant"] = True
        jj.update(kw)
        jobs.append(jj)
    return jobs
def run_variant(jobs):
    R = pd.DataFrame(ajile.run_regression(jobs, workers=4))
    R["band"] = R.target.str[:3]
    return R
print("main fits:", fig6_summary(MAIN))
# Seeds: the splits and shuffles of the claim's seed + 1000 ... + 4000
t = time.time()
top = MAIN[MAIN.r2 > 0.03][["subject", "electrode"]].drop_duplicates()
print("models refit per variant:", len(top), "electrodes, both bands")
sens = {}
for off in SEED_OFFSETS[1:]:
    R = run_variant(variant_jobs(JOBS, top, seed=REG_SEED + off))
    sens[off] = R
    print(f"seed + {off}: largest R2 {R.r2.max():.4f};", fig6_summary(R))
print(f"{time.time() - t:.0f} s")
''')
C[i]['metadata']['tags']=["claim:fig6-r2-at-most-025","claim:fig6b-best-models-sensorimotor","claim:fig6c-angle-and-day-most-informative",
    "claim:fig6d-upward-reaches-enhance-pattern","claim:fig6d-angle-and-day-largest-coefficients"]
new = '''# log(onset speed + 1) as the code encodes it (claims file, opening comment)
t = time.time()
R_log = run_variant(variant_jobs(regression_jobs(REG_SEED, log_speed=True), top))
print("log(onset speed + 1): largest R2", round(R_log.r2.max(), 4), ";", fig6_summary(R_log))
# Bad electrodes included, as the code fits them (claims file, opening comment): the main fits plus
# the electrodes bad in at least one file of the subject
JOBS_BAD = regression_jobs(REG_SEED, include_bad=True)
extra = []
for j in JOBS_BAD:
    k = ~j["good_all"][j["electrodes"]]
    jj = dict(j); jj["Y"] = j["Y"][:, k][:, :, :2]; jj["electrodes"] = j["electrodes"][k]
    jj["targets"] = ["lfb_mean", "hfb_mean"]; jj["variant"] = True
    extra.append(jj)
print("electrodes bad in at least one file with finite power:", {j["subject"]: len(j["electrodes"]) for j in extra},
      "; dropped for non-finite power:", {j["subject"]: j["dropped_nonfinite"] for j in JOBS_BAD})
R_bad = run_variant([j for j in extra if len(j["electrodes"])])
R_all = pd.concat([MAIN[["subject", "electrode", "band", "r2", "coef", "delta"]], R_bad[["subject", "electrode", "band", "r2", "coef", "delta"]]])
print("bad electrodes: models with R2 > 0.05 among them", R_bad.groupby("band").r2.apply(lambda x: int((x > 0.05).sum())).to_dict(),
      "; largest R2", round(R_bad.r2.max(), 4))
print("all electrodes (main + bad):", fig6_summary(R_all))
print(f"{time.time() - t:.0f} s")
'''
C.insert(i+1, {"cell_type":"code","execution_count":None,"metadata":{"tags":list(C[i]['metadata']['tags'][2:])},"outputs":[],"source":new.splitlines(True)})
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
python $TMPDIR/nbpatch3.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
ls ../../executed/peterson-2021/.venv/bin | grep -i "jupyter\|papermill\|nbclient" | head; date -u
```

```
jupyter
jupyter-dejavu
jupyter-execute
jupyter-kernel
jupyter-kernelspec
jupyter-migrate
jupyter-nbconvert
jupyter-run
jupyter-troubleshoot
jupyter-trust
Wed Nov 25 08:42:09 UTC 2026
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/sub && cp ajile.py $TMPDIR/sub/ && python - <<EOF
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
c=nb['cells'][2]
c['source']=c['source']+['\n# SUBSET TEST\n','for m in metas:\n','    n = 40\n','    keep = np.r_[0:n, len(m["reaches"]) - 5:len(m["reaches"])]\n','    keep = np.unique(keep[(keep >= 0) & (keep < len(m["reaches"]))])\n','    m["reaches"] = m["reaches"].iloc[keep].reset_index(drop=True); m["event_times"] = m["event_times"][keep]\n']
json.dump(nb,open('$TMPDIR/sub/nb.ipynb','w'),indent=1)
EOF
cd $TMPDIR/sub && time timeout 3000 ~/work/encore-registry/encore-registry/executed/peterson-2021/.venv/bin/jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3000 nb.ipynb --output out.ipynb 2>&1 | tail -3
```

```
/tmp/claude-1001/sub/ajile.py:414: RuntimeWarning: invalid value encountered in subtract
  sh = band_stats(dbs - dbs[:, :, BASE].mean(axis=-1, keepdims=True))
[NbConvertApp] Writing 436693 bytes to out.ipynb

real	21m27.545s
user	66m48.366s
sys	1m39.366s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR/sub && python -c "
import json
from datetime import datetime as D
nb=json.load(open('out.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    ex=c['metadata'].get('execution',{})
    a,b=ex.get('iopub.execute_input'),ex.get('shell.execute_reply')
    dt=(D.fromisoformat(b[:-1])-D.fromisoformat(a[:-1])).total_seconds() if a and b else None
    err=[o for o in c['outputs'] if o['output_type']=='error']
    print(i, dt, 'ERROR '+err[0]['ename']+': '+err[0]['evalue'][:300] if err else '')
"
```

```
Wed Nov 25 09:03:45 UTC 2026
1 2.497918 
2 92.053391 
3 0.023561 
4 0.027973 
5 0.084831 
7 33.185329 
8 0.508072 
11 252.576839 
12 0.09312 
13 0.051262 
14 0.075784 
16 0.002227 
18 0.003876 
21 0.017507 
24 0.007693 
27 0.035051 
30 0.054685 
31 0.481563 
34 0.014623 
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sub && python -c "
import json
nb=json.load(open('out.ipynb'))
for i in [4,7,8,12,21,24,30,56,76,97,98]:
    c=nb['cells'][i]
    out=''
    for o in c.get('outputs',[]):
        if 'text' in o: out+=''.join(o['text'])
        if o['output_type']=='error': out+='\n'.join(o['traceback'][-3:])
    print('=====',i); print(out[-2500:])
" | grep -v Warning | grep -v "sh = band\|bs = db"
```

```
===== 4
64(3), np.int64(10), np.int64(5), np.int64(20)]; bad in every file 1; bad in any file 32
S10: positions identical across files True; electrodes without position 0; bad per file [np.int64(5), np.int64(5), np.int64(9), np.int64(5), np.int64(20)]; bad in every file 2; bad in any file 30
S11: positions identical across files True; electrodes without position 0; bad per file [np.int64(3), np.int64(3), np.int64(1), np.int64(1), np.int64(1)]; bad in every file 1; bad in any file 4
S12: positions identical across files True; electrodes without position 8; bad per file [np.int64(12), np.int64(9), np.int64(11), np.int64(11), np.int64(13)]; bad in every file 6; bad in any file 21
columns of the reaches table: ['Bimanual_class', 'Bimanual_overlap', 'Bimanual_ratio', 'Onset_speed_px_per_sec', 'Reach_angle_degrees', 'Reach_magnitude_px', 'Speech_ratio', 'id', 'start_time', 'stop_time']
columns of the electrodes table: ['filtering', 'good', 'group_name', 'high_freq_R2', 'id', 'imp', 'kurtosis', 'location', 'low_freq_R2', 'median_deviation', 'standard_deviation', 'x', 'y', 'z']
columns of the epochs table: ['id', 'labels', 'start_time', 'stop_time']
                   count        mean         std         min         25%        50%         75%          max
duration          2385.0    1.182362    0.525856    0.233333    0.833333   1.100000    1.400000     3.833333
magnitude         2385.0   96.825306   69.081657    4.070751   48.134479  84.026044  124.903263   680.562436
angle_raw         2385.0  -30.785772   99.273297 -179.732653 -106.865688 -64.710374   50.703547   179.795000
onset_speed       2385.0  128.510790  121.873818    0.000000   52.066696  94.833528  162.917067  1492.069915
speech_ratio      2385.0    0.286657    0.126072    0.000000    0.185506   0.277840    0.373764     0.709118
Bimanual_ratio    2385.0    0.275315    0.280570    0.000000    0.025753   0.167747    0.487127     1.000000
bimanual_overlap  2385.0    0.617135    0.588838    0.000000    0.000000   0.
[... 214 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python - <<'EOF'
p='ajile.py'; s=open(p).read()
a='''    n_zero_el = np.zeros(n_ev, int)      # good electrodes with any exact zero sample in the segment
'''
b='''    n_zero_el = np.zeros(n_ev, int)      # good electrodes with any exact zero sample in the segment
    n_zero_run = np.zeros(n_ev, int)     # good electrodes with a run of at least 25 zero samples (50 ms)
'''
assert s.count(a)==1; s=s.replace(a,b)
a='''                n_zero_el[i] = int((seg[good] == 0).any(axis=1).sum())
'''
b='''                z = seg[good] == 0
                n_zero_el[i] = int(z.any(axis=1).sum())
                cz = np.concatenate([np.zeros((z.shape[0], 1), int), np.cumsum(z, axis=1)], axis=1)
                n_zero_run[i] = int(((cz[:, 25:] - cz[:, :-25]) == 25).any(axis=1).sum())
'''
assert s.count(a)==1; s=s.replace(a,b)
a='allzero=allzero, n_dropped=n_dropped, n_zero_el=n_zero_el,'
assert s.count(a)==1; s=s.replace(a,'allzero=allzero, n_dropped=n_dropped, n_zero_el=n_zero_el, n_zero_run=n_zero_run,')
open(p,'w').write(s)
import json
P='reproduce_peterson_2021.ipynb'
nb=json.load(open(P)); C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def rep(i,a,b):
    s=src(i); assert s.count(a)==1,(i,a[:60]); C[i]['source']=s.replace(a,b).splitlines(True)
rep(12,'''ev["n_zero_el"] = np.concatenate([r["n_zero_el"] for r in spec])''','''ev["n_zero_el"] = np.concatenate([r["n_zero_el"] for r in spec])
ev["n_zero_run"] = np.concatenate([r["n_zero_run"] for r in spec])''')
rep(12,'''print("kept events with a good electrode holding exact zeros in the segment:", int((kk.n_zero_el > 0).sum()), "of", len(kk),
      "; per subject:", kk[kk.n_zero_el > 0].groupby("subject").size().to_dict())''','''print("kept events with a good electrode holding any exact zero sample in the segment:", int((kk.n_zero_el > 0).sum()), "of", len(kk),
      "; per subject:", kk[kk.n_zero_el > 0].groupby("subject").size().to_dict())
print("kept events with a good electrode holding a run of at least 25 zero samples (50 ms):", int((kk.n_zero_run > 0).sum()),
      "; per subject:", kk[kk.n_zero_run > 0].groupby("subject").size().to_dict(), "; electrodes in such events, largest:",
      int(kk.n_zero_run.max()))''')
rep(97,'''        Cf = pd.DataFrame(list(M.coef))
        ca = Cf.abs().median().sort_values(ascending=False)
''','''        if len(M) == 0:
            out[band] = dict(n=0)
            continue
        Cf = pd.DataFrame(list(M.coef))
        ca = Cf.abs().median().sort_values(ascending=False)
''')
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
cp ajile.py $TMPDIR/sub/ && cd $TMPDIR/sub && ~/work/encore-registry/encore-registry/executed/peterson-2021/.venv/bin/python -c "
import numpy as np, ajile
# synthetic check of the new pieces
db=np.random.randn(5,25,26); w=np.zeros((5,8)); w[:,0]=[.2,.2,.2,.2,.2]; w[:,1:]=1/5
db[2,3,4]=-np.inf
r,d=ajile.project(w,db); print(d, np.allclose(r[0], db[[0,1,3,4]].mean(0)))
"
```

```
1 True
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import numpy as np
seg=np.random.randn(3,5000); seg[1,100:130]=0; seg[2,7]=0
z=seg==0
cz=np.concatenate([np.zeros((z.shape[0],1),int),np.cumsum(z,axis=1)],axis=1)
print(((cz[:,25:]-cz[:,:-25])==25).any(axis=1), z.any(axis=1))
"; date -u
```

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
Wed Nov 25 09:04:15 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
executed/peterson-2021/.venv/bin/python -c "
import numpy as np
seg=np.random.randn(3,5000); seg[1,100:130]=0; seg[2,7]=0
z=seg==0
cz=np.concatenate([np.zeros((z.shape[0],1),int),np.cumsum(z,axis=1)],axis=1)
print(((cz[:,25:]-cz[:,:-25])==25).any(axis=1), z.any(axis=1))
"; grep -n "fresh\|def cmd_\|argparse\|add_parser" tools/entry.py | head -20
```

```
[False  True False] [False  True  True]
25:`run` builds a fresh virtual environment from the lock file and executes each
33:so, without executing anything; --fresh executes all the same.
47:import argparse
531:    if lock(entry_dir, version) or run(entry_dir, output_dir, timeout, max_minutes, fresh=True):
596:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
598:    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
604:              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
696:    parser = argparse.ArgumentParser(description=__doc__,
697:                                     formatter_class=argparse.RawDescriptionHelpFormatter)
705:    parser.add_argument("--fresh", action="store_true",
754:    return run(entry_dir, output_dir, args.timeout, args.max_minutes, args.fresh)
```

**Agent**

Subset run works (all new cells execute; the per-file variant, the zero-row alignment check and the shift test print as intended). Starting the full run now; it takes about 40 minutes.

**Agent calls Bash**

```bash
date -u; timeout 7000 python tools/entry.py all entries/peterson-2021 > $TMPDIR/run1.log 2>&1; echo exit $?; date -u; tail -20 $TMPDIR/run1.log
```

```
Wed Nov 25 09:04:24 UTC 2026
exit 0
Wed Nov 25 09:42:21 UTC 2026
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
Installed kernelspec registry-peterson-2021 in executed/peterson-2021/.venv/share/jupyter/kernels/registry-peterson-2021
0 error(s)
pass  reproduce_peterson_2021.ipynb  (2271 s)
```

**Agent calls Bash**

```bash
executed/peterson-2021/.venv/bin/python -c "
import json
nb=json.load(open('executed/peterson-2021/reproduce_peterson_2021.ipynb'))
print('nbformat', nb['nbformat'], nb['nbformat_minor'], 'ids', sum('id' in c for c in nb['cells']), len(nb['cells']))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    out=''
    for o in c.get('outputs',[]):
        if 'text' in o: out+=''.join(o['text'])
        if o['output_type']=='error': out+='ERROR'+o['evalue']
    if i in (2,3,5,14,31,47): continue
    print('=====',i); print(out[-3500:] if i!=4 else out[:1200])
" | grep -v "Warning\|sh = band\|bs = db" > $TMPDIR/out1.txt; wc -c $TMPDIR/out1.txt
```

```
62064 /tmp/claude-1001/out1.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/out1.txt"
}
```

```
1	nbformat 4 5 ids 101 101
2	===== 1
3	dandiset 000055 version 0.261123.1703
4	
5	===== 4
6	ECoG unit: volts conversion: 1e-06 rate: 500.0 start: 0.0 chunks: (84375, 1)
7	pose unit: meters rate: 30.0 series: ['L_Ear', 'L_Elbow', 'L_Shoulder', 'L_Wrist', 'Nose', 'R_Ear', 'R_Elbow', 'R_Shoulder', 'R_Wrist']
8	all ECoG at 500 Hz: True ; all pose at 30 Hz: True
9	ElectricalSeries rows = electrodes table: True
10	ReachEvents timestamps = reaches start_time (max diff, s): 86400.0
11	  S08 day 4: 1 event(s) differ by more than 1 s; ReachEvents [40.3] s, start_time [86440.3] s; ECoG length 86400.0 s
12	events differing by more than 1 s, all files: 1
13	S01: positions identical across files True; electrodes without position 0; bad per file [np.int64(9), np.int64(3), np.int64(3), np.int64(3)]; bad in every file 3; bad in any file 9
14	S02: positions identical across files True; electrodes without position 0; bad per file [np.int64(1), np.int64(1), np.int64(5), np.int64(6)]; bad in every file 1; bad in any file 7
15	S03: positions identical across files True; electrodes without position 16; bad per file [np.int64(17), np.int64(25), np.int64(20), np.int64(17)]; bad in every file 17; bad in any file 27
16	S04: positions identical across files True; electrodes without position 0; bad per file [np.int64(17), np.i
17	===== 7
18	positions     True
19	8         9       127         126            126           127  126 rows for 126 electrodes with positions     True
20	9        10       127         126            126           127  126 rows for 126 electrodes with positions     True
[... 544 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/out1.txt",
 "offset": 564
}
```

```
564	
565	===== 73
566	    subject band  max_dev  day_range   level_uV     level_V
567	0         1  lfb    0.943      1.162  36.488998  -83.511002
568	1         1  hfb    0.208      0.354  16.306999 -103.693001
569	2         2  lfb    0.190      0.354  33.153999  -86.846001
570	3         2  hfb    0.039      0.070  17.471001 -102.528999
571	4         3  lfb    1.023      1.754  33.509998  -86.489998
572	5         3  hfb    0.269      0.439  17.801001 -102.198997
573	6         4  lfb    0.466      0.621  33.240002  -86.760002
574	7         4  hfb    0.375      0.605  18.007000 -101.992996
575	8         5  lfb    0.293      0.423  34.118999  -85.880997
576	9         5  hfb    0.042      0.054  19.368000 -100.632004
577	10        6  lfb    1.307      2.044  35.521000  -84.478996
578	11        6  hfb    1.491      1.717  22.855000  -97.144997
579	12        7  lfb    0.344      0.629  36.851002  -83.149002
580	13        7  hfb    0.227      0.343  18.908001 -101.092003
581	14        8  lfb    0.110      0.203  32.683998  -87.316002
582	15        8  hfb    0.249      0.489  21.888000  -98.112000
583	16        9  lfb    0.403      0.655  32.167999  -87.832001
[... 136 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; executed/peterson-2021/.venv/bin/python -c "
import yaml
d=yaml.safe_load(open('claims/peterson-2021.yaml'))
cl=d['claims'] if isinstance(d,dict) else d
for c in cl:
    if c['id'] in ('table1-subject-band-power-ci','fig5-recording-day-effects','fig4-precentral-subject-variability','extfig5-1-baseline-reduces-day-variability','fig2-reach-shape','fig2-event-counts'):
        print('==',c['id']); print({k:v for k,v in c.items() if k not in ('id',)})
"
```

```
Exit code 1
Wed Nov 25 09:42:34 UTC 2026
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'
```

**Agent calls Bash**

```bash
cd  for id in table1-subject-band-power-ci fig5-recording-day-effects fig4-precentral-subject-variability fig2-reach-shape; do n=$(grep -n "id: $id" claims/peterson-2021.yaml | cut -d: -f1); sed -n "${n},$((n+40))p" claims/peterson-2021.yaml | awk 'NR>1 && /^- id:/{exit} {print}'; done
```

```
- id: table1-subject-band-power-ci
  statement: Each subject's precentral band power lies in the 95% bootstrap interval Table 1
    gives; LFB power is below baseline and HFB power above it for most subjects.
  source: Table 1
  inferred: Values read from Table 1; no sentence states them. The statement is a reading of the
    table.
  data: with_inputs
  depends_on:
  - roi-projection-link
  criterion: 'Table 1 intervals (dB), LFB then HFB. S01 -1.87 to -1.29, 0.03 to 0.23; S02 -1.12
    to -0.31, 0.07 to 0.64; S03 -2.11 to -1.73, 1.39 to 1.67; S04 -0.17 to 0.01, 0.32 to 0.52;
    S05 -0.7 to -0.38, 0.2 to 0.48; S06 -1.63 to -1.11, 2.02 to 2.37; S07 -0.84 to -0.51, 1.14
    to 1.34; S08 -0.3 to 0.04, 0.36 to 0.63; S09 -0.57 to -0.08, -0.11 to 0.23; S10 -0.87 to
    -0.35, 0.01 to 0.3; S11 -2.3 to -1.86, 0.09 to 0.34; S12 -0.66 to -0.44, 0.06 to 0.2. The
    table does not say which statistic the interval is for. Readings are (a) the mean and (b)
    the median over the subject''s events of banded precentral power. Band power is taken as
    the band mean (Methods) or the band median (code), giving four readings in all. Reproduced
    when, under one reading, the point estimate lies inside the paper''s interval for all 24
    subject and band pairs. Partially reproduced when it does for at least 18. The attempt''s own
    5000-replicate bootstrap intervals are shown beside the paper''s.'
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for id in fig5-recording-day-effects extfig5-1-baseline-reduces-day-variability; do n=$(grep -n "id: $id" claims/peterson-2021.yaml | cut -d: -f1); sed -n "${n},$((n+70))p" claims/peterson-2021.yaml | awk 'NR>1 && /^- id:/{exit} {print}' | grep -v "^  - about\|test: Kruskal\|^    p:\|p_relation" ; done
```

```
- id: fig5-recording-day-effects
  statement: Precentral band power differs significantly across recording days in LFB for
    subjects 03, 05, 06, 07, 08 and 11, and in HFB for subjects 03, 04, 07, 08 and 10, despite
    baseline subtraction.
  source: Results, Intracortical spectral power during naturalistic movements, paragraph 4;
    Figure 5; Table 2
  quote: We also found a significant effect of recording day in LFBs for subjects 03 ( p <
    0.001, Kruskal–Wallis test), 05 ( p = 0.013), 06 ( p < 0.001), 07 ( p = 0.041), 08 ( p =
    0.013), and 11 ( p < 0.001), as well as in HFBs for subjects 03 ( p = 0.002), 04 ( p <
    0.001), 07 ( p < 0.001), 08 ( p = 0.004), and 10 ( p = 0.006).
  statistics:
  data: with_inputs
  depends_on:
  - roi-projection-link
  criterion: Per subject and band, a one-way Kruskal-Wallis test of banded precentral power
    across the subject's recording days, uncorrected, at p < 0.05 (Figure 5 legend; the notebook
    uses pingouin's uncorrected p). Band mean as the main result, band median (code) as a
    variant. The paper's pattern is the 11 significant pairs above and the 13 other subject and
    band pairs not significant. Reproduced when all 24 pairs agree; partially reproduced when at
    least 20 agree. Each p is reported, with the per-day 95% intervals of Table 2 for
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python -c "
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
print(''.join(nb['cells'][34]['source'])[-600:])
print([ (i,c.get('id')) for i,c in enumerate(nb['cells']) if 'id' not in c])
"
```

```
per.overlap_skew > 0).sum()), "of 12; class part:", class_ok, int((per.class_frac_bimanual > 0.5).sum()), "of 12")
print("five highest median ratios:", top_ratio, "-> S02, S04, S05 among them:", less_ratio)
print("five lowest overlap skewness:", low_skew, "-> S02, S04, S05 among them:", less_over)
print("bimanual ratio range", EVB.bimanual_ratio.min(), EVB.bimanual_ratio.max(), "; overlap range",
      EVB.bimanual_overlap.min(), EVB.bimanual_overlap.max(), "(the description says a fraction of the contralateral movement)")
print("overlap values above 1:", int((EVB.bimanual_overlap > 1).sum()))
[(75, None), (76, None), (98, None)]
```

**Agent calls Bash**

```bash
python -c "
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if c['cell_type']=='markdown' and (s.startswith('**Result') or i in (10,15,45,58,77)):
        print('=====',i); print(s)
"
```

```
===== 9
**Result: reproduced.** The paper's code rule (keep the non-zero rows, drop the first) leaves as
many rows as electrodes with a position in all 12 subjects; the dropped first row is the electrode
density of each region, and the regions whose mean density exceeds 3 are exactly the eight of the
claims file. For every subject the largest-weight region is the nearest region centroid for 36 to
55% of electrodes, against at most 14 electrodes in 200 shuffles of the electrode order, under all
five seeds. The 16 electrodes of S03 and the 8 of S12 without positions have no row; they get no
weight.
===== 10
## Spectral power of every event (streamed)

For each file, the chunk index of the ECoG series is read from the file's B-tree, and the chunks
holding the 10 s around each event are fetched and decoded. The helper's docstring gives the source
of every parameter. Every event's segment is checked by the Methods' rule, and its power is
projected to the eight regions with the weights of that file's good electrodes.
===== 15
## Event sets

Reading (a): every event in the reaches tables. Reading (b): the events left after the Methods'
segment rejection (no ECoG for the whole 10 s segment, zeroed data, power below 0 dB, or 115-125 Hz
[... 138 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && python3 -c "
import json
nb=json.load(open('executed/peterson-2021/reproduce_peterson_2021.ipynb'))
for i in [64,70]:
    out=''.join(''.join(o.get('text','')) for o in nb['cells'][i]['outputs'])
    print('=====',i); print(out[:6000])
" | cut -c1-260
```

```
===== 64
    subject band  paper_lo  paper_hi  mean_of_bandmean  in_mean_of_bandmean  median_of_bandmean  in_median_of_bandmean ci_median_bandmean  mean_of_bandmedian  in_mean_of_bandmedian  median_of_bandmedian  in_median_of_bandmedian ci_median_bandmedian
0         1  lfb     -1.87     -1.29            -1.369                 True              -1.289                  False      [-1.69, -1.0]              -1.350                   True                -1.330                     True       [-1.74, -0.97]
1         1  hfb      0.03      0.23             0.058                 True               0.035                   True      [-0.02, 0.13]               0.096                   True                 0.111                     True         [0.03, 0.19]
2         2  lfb     -1.12     -0.31            -0.260                False              -0.263                  False       [-0.5, 0.01]               0.061                  False                -0.103                    False        [-0.27, 0.17]
3         2  hfb      0.07      0.64             0.050                False              -0.027                  False      [-0.19, 0.14]               0.420                   True                 0.456                     True         [0.25, 0.66]
4         3  lfb     -2.11     -1.73            -1.827                 True              -1.780                   True     [-2.07, -1.49]              -1.689                  False                -1.584                    False       [-1.84, -1.37]
5         3  hfb      1.39      1.67             0.876                False               0.936                  False       [0.81, 1.07]               0.965                  False                 1.044                    False         [0.92, 1.18]
6         4  lfb     -0.17      0.01            -0.093                 True              -0.073                   True     [-0.17, -0.01]              -0.031                   True                 0.005                     True        [-0.14, 0.11]
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python3 -c "
import json
nb=json.load(open('reproduce_peterson_2021.ipynb'))
print(''.join(nb['cells'][99]['source']))
print(''.join(nb['cells'][0]['source'])[-900:])
"
```

```
## Summary

| Claim | Outcome |
|---|---|
| subject-days | reproduced |
| roi-projection-link | reproduced |
| cohort | partially reproduced (depth electrodes in 7 subjects, not 5) |
| fig2-event-counts | not reproduced (210 to 976 events per subject, median 691) |
| fig2-features-differ-across-subjects | reproduced |
| fig2-reach-shape | partially reproduced (no angle density peaks within 15 degrees of +-90) |
| fig2-bimanual-skew | reproduced |
| extfig2-1c-contralateral-larger | reproduced |
| extfig2-2-feature-correlations | partially reproduced (5 of 6) |
| fig2-days-and-waking | partially reproduced (S04's busiest day holds 40%) |
| fig3-group-lfb-decrease-hfb-increase | reproduced |
| fig3-sensorimotor-largest | reproduced |
| fig3-lfb-more-widespread | blocked, methods underspecified (the two readings disagree) |
| fig4-precentral-subject-variability | partially reproduced (3 of 4 parts; S09 has no HFB increase) |
| fig5-band-power-differs-across-subjects | reproduced |
| table1-subject-band-power-ci | partially reproduced (21 of 24) |
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/nbtext.py <<'EOF'
import json, uuid
P='reproduce_peterson_2021.ipynb'
nb=json.load(open(P)); C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s): C[i]['source']=s.rstrip('\n').splitlines(True)
def rep(i,a,b):
    s=src(i); assert s.count(a)==1,(i,a[:60]); setsrc(i,s.replace(a,b))
def setres(i, s):
    assert src(i).startswith('**Result'), i
    setsrc(i, s)
for c in C:
    if 'id' not in c: c['id']=uuid.uuid4().hex[:8]
# header
rep(0,'''The notebook runs for about 40 minutes: about 12 minutes to stream the ECoG around 8088 events
(about 150 GB of compressed chunks) and about 25 minutes for the 3904 regression models.''','''The notebook runs for about 40 minutes: about 10 minutes to stream the ECoG around 8088 events
(about 150 GB of compressed chunks), about 17 minutes for the 3904 regression models and about 9
minutes for the regression variants.''')
rep(0,'''| fig4-precentral-subject-variability | yes | partially reproduced |''','''| fig4-precentral-subject-variability | yes | partially reproduced |''')
rep(0,'''| fig5-recording-day-effects | yes | partially reproduced |''','''| fig5-recording-day-effects | yes | not reproduced |''')
rep(0,'''Assumptions (the paper leaves these open; each is stated where it is used): how the segment
rejection pools power over electrodes and frequencies; that each event uses the good-electrode flags
of its own file for the region projection, and that the regression and electrode-level analyses use
the electrodes good in every file of the subject.''','''Assumptions (the paper leaves these open; each is stated where it is used): how the segment
rejection pools power over electrodes and frequencies; and that the good electrodes of a subject are
those marked good in every one of its files, for the segment rejection, the region projection, the
regression and the electrode-level analyses (the claims file's opening comment renormalises the
weights per subject). The flags of each event's own file are shown as a variant for the region claims.''')
rep(10,'''Every event's segment is checked by the Methods' rule, and its power is
projected to the eight regions with the weights of that file's good electrodes.''','''Every event's segment is checked by the Methods' rule, and its power is
projected to the eight regions with the weights of the electrodes good in every file of the subject;
the weights of each file's own good electrodes are kept as a variant. An electrode whose power is not
finite in an event gets weight 0 in that event, and the region's weights are renormalised.''')
rep(15,'''power more than 3 SD above the subject's segments).''','''power more than 3 SD above the subject's segments), and the one event whose ReachEvents time and
reaches start_time disagree (data check).''')
rep(34,'''print("overlap values above 1:", int((EVB.bimanual_overlap > 1).sum()))''','''print("overlap values above 1:", int((EVB.bimanual_overlap > 1).sum()), "of", len(EVB), "; in all events:",
      int((EVA.bimanual_overlap > 1).sum()), "of", len(EVA))''')
setres(9,'''**Result: reproduced.** The paper's code rule (keep the non-zero rows, drop the first) leaves as
many rows as electrodes with a position in all 12 subjects; the dropped first row is the electrode
density of each region, and the regions whose mean density exceeds 3 are exactly the eight of the
claims file. After the density row, the zero rows of S03 (16) and S12 (8) sit exactly at the indices
of the electrodes without a position, and the 4 extra zero rows of S01 come after its last electrode.
For every subject the largest-weight region is the nearest region centroid for 36 to 55% of
electrodes, against at most 14 electrodes in 200 shuffles of the electrode order, under all five
seeds, and shifting the rows by 1 to 3 places lowers that fraction in all 12 subjects.''')
setres(22,'''**Result: partially reproduced.** Twelve subjects, 8 male, mean age 29.42 years (SD 7.94), 84.83 surface
electrodes on average and 5 right-hemisphere implants match. Electrode groups described as depth
are in 7 subjects, not 5 (S01, S02, S03, S09, S10, S11, S12), with 23.71 depth electrodes on
average, within the stated SD of 23.2. Counting only the grid as surface gives 63.08 electrodes on
average, outside 87.0 +- 12.9, so the group descriptions are the reading kept.''')
setres(25,'''**Result: not reproduced.** Under no reading are all three values within tolerance. All events: 211
to 996, median 770.5. After the segment rejection: 210 to 976, median 692.0. Events with ECoG and
no missing samples: 211 to 986, median 700.5. The paper gives 151 to 947, median 640; the fewest
events are 210 or more in every reading, outside 151 +- 15.1. Keeping only events of 0.5 to 4 s
(the Methods' filter, not a reading of the criterion) still leaves at least 207 per subject.''')
setres(28,'''**Result: reproduced.** All ten features differ across subjects (Kruskal-Wallis), with the largest p
7.0e-33 (reach duration) on the events of reading (b), and p < 0.001 for all ten on all events.''')
setres(32,'''**Result: partially reproduced.** Most reaches last under 2 s (88 to 95% per subject, 91.8% pooled)
and cover under 200 pixels (59 to 100% per subject, 91.3% pooled), in all 12 subjects. The angle
part fails: the density of the folded angle has its two highest maxima within 15 degrees of -90 and
+90 with a lower density at 0 in none of the 12 subjects and not pooled. Pooled, the maxima are at
-71.5 and +75 degrees, and the density at 0 (0.00407) is above the lower maximum (0.004). The
density at +75 degrees is above that at +90 in every subject, which the kernel's smoothing at the
boundary can cause; but only 6.4% of events lie within 15 degrees of -90 (19.7% of +90), and pooled
the density at -75 degrees (0.00395) is below that at 0. Reading (a) gives the same outcome.''')
setres(35,'''**Result: reproduced.** The median bimanual ratio is below 0.5 and the overlap skewness positive in
12 of 12 subjects and pooled (0.14 and 1.11); more than half of the events are bimanual in 12 of 12
(73% pooled). S02, S04 and S05 are among the five subjects with the highest median ratio and among
the five with the lowest overlap skewness.''')
setres(41,'''**Result: partially reproduced.** Five of the six correlations are within 10% of the paper's under
both event sets. Reach magnitude and duration correlate at r = 0.232 (reading b), below 0.26 - 0.026.''')
setres(44,'''**Result: partially reproduced.** Events are mostly in waking hours: 64 to 96% of each subject's events
fall between 08:00 and 24:00. The busiest day holds more than half of the events for S05 (0.606) and
S09 (0.519) and for no other subject; for S04 it holds 0.400, so the day part does not hold.''')
setres(48,'''**Result: reproduced.** In precentral, postcentral and inferior parietal regions the masked group
power over 4-30 Hz is below 0 and over 50-120 Hz above 0, both over 0 to 0.5 s (for example
precentral -0.728 and 0.411 dB) and at the bin of 0 s, under all five seeds. Middle frontal shows
the same pattern; in supramarginal and the temporal regions the masked high-frequency values are at
most 0.008 dB. With each file's own good-electrode flags (variant) all three named regions hold too.''')
setres(51,'''**Result: reproduced.** Under all three readings and all five seeds the three largest regions are
postcentral, precentral and inferior parietal, and each temporal region is below all three (for
reading a, 0.429, 0.418 and 0.251 dB against at most 0.034). The variant with each file's flags gives
the same under all three readings.''')
setres(54,'''**Result: blocked (methods underspecified).** The readings disagree. Reading (b), bins per frequency
bin, gives 36.0 significant negative low-frequency bins against 22.2 positive high-frequency bins,
and holds under all five seeds. Reading (a), regions with any significant bin, gives 8 against 8
(not larger), and 7 or 8 against 8 under the other seeds. Supramarginal (30 bins) and superior
temporal (27 bins) do have significant low-frequency decreases. The variant with each file's flags
gives 7 against 8 and 34.6 against 24.0, the same disagreement.''')
setres(57,'''**Result: partially reproduced.** Two of four parts hold. Part 2: S03, S06, S07, S08 and S11 have
positive power at 116 and 121 Hz. Part 3: S09 and S12 peak at 76 and 66 Hz with means over 101-121 Hz
below half the peak. Part 4 fails: the narrowest low-frequency decreases are S07 and S09 (2 bins),
and S04 and S08 are among six subjects tied at 3 bins, so they are not among the three fewest. Part 1
fails in one subject: S09 has a mean of -0.039 dB over 76-100 Hz. With each file's own flags
(variant) parts 2 to 4 hold and part 1 fails for S09 only.''')
setres(62,'''**Result: reproduced.** Precentral band power differs across the 12 subjects in both bands, for band
means and band medians (Kruskal-Wallis H = 740 to 1028, p below the smallest double).''')
setres(65,'''**Result: partially reproduced.** Under the best reading (median over events of the band median), 18
of 24 subject and band values lie in Table 1's intervals; the other readings give 14, 16 and 16.
Outside are S02 LFB (-0.103 against -1.12 to -0.31), S03 LFB (-1.584 against -2.11 to -1.73), S03 HFB
(1.044 against 1.39 to 1.67), S06 LFB (-0.647 against -1.63 to -1.11), S06 HFB (1.874 against 2.02
to 2.37) and S10 LFB (-0.196 against -0.87 to -0.35). The median band mean is below 0 for LFB in 12
of 12 subjects and above 0 for HFB in 11 of 12. With each file's own flags (variant) the mean of the
band mean puts 21 of 24 inside.''')
setres(68,'''**Result: not reproduced.** With band means 18 of 24 subject and band pairs agree with the paper, and
18 with band medians, below the 20 the criterion asks. The day effect is significant where the paper
finds none for S01 LFB (p = 0.043), S01 HFB (p = 0.022) and S06 HFB (p = 6.9e-11), and not
significant for S07 HFB (p = 0.073), S08 LFB (p = 0.31) and S10 HFB (p = 0.054), where the paper
finds one. The outcome rests on the choice of good electrodes: with each file's own flags (variant)
20 of 24 agree, which would be partially reproduced.''')
setres(71,'''**Result: reproduced.** Baseline subtraction lowers the SD of day means in 10 of 12 subjects for LFB
and 12 of 12 for HFB (reading a), and at 91.3% and 90.2% of electrodes (reading b). Variability
remains: day effects are significant in 11 subject and band pairs (fig5-recording-day-effects), with
SDs of 0.03 to 0.83 dB after subtraction.''')
setres(74,'''**Result: reproduced.** The largest deviation of a day mean from the subject mean is 1.49 dB (S06 HFB),
at most 2.2 dB in every subject and band (1.49 dB with each file's flags too). Without baseline
subtraction the precentral band power is 11.7 to 36.9 dB in microvolts squared, within 9 to 55 dB;
in volts squared it would be about -108 to -83 dB.''')
rep(77,'''fig6b-best-models-sensorimotor, the 80/20 splits its seed + 1 and the shuffles its seed + 2; the
other Figure 6 claims use these same fits.''','''fig6b-best-models-sensorimotor, the 80/20 splits its seed + 1 and the shuffles its seed + 2; the
other Figure 6 claims use these same fits. Forward selection on all events lets the test events of
each split take part in choosing the features, as the code does and the claims file prescribes; this
can raise R2 a little. After the claim sections, the models with R2 > 0.03 are refit under the four
other seeds and with log(onset speed + 1), and the electrodes bad in at least one file are fit as
the code does; Delta R2 and coefficients are recomputed for each.''')
setres(81,'''**Result: reproduced.** The largest split-averaged withheld R2 is 0.177 (S07, HFB), at most 0.275. It is
0.184 with 80/20 splits and 0.158 with band medians, 0.167 to 0.182 under the other four seeds, 0.174
with log(onset speed + 1), and 0.151 at most among the electrodes bad in at least one file.''')
setres(84,'''**Result: reproduced.** Of the models with R2 > 0.05 (14 per band), all LFB and 13 of 14 HFB electrodes
are in the five frontoparietal regions, and the median R2 of sensorimotor electrodes is above that
of temporal ones in both bands (LFB -0.0093 against -0.0150, HFB -0.0117 against -0.0157). Projected
onto the regions, the three highest are precentral, postcentral and middle frontal in both bands.
Under the other seeds 12 to 14 models per band pass 0.05.''')
setres(87,'''**Result: reproduced.** Over the 14 LFB models with R2 > 0.05, recording day (median Delta R2 0.037) and
reach angle (0.031) are the two most informative features; the other eight have medians of at most
0.0001. In HFB the same two lead (0.062 and 0.022), and under the code's Delta R2 and the code's
selection by LFB R2 too (with that selection the HFB order is angle, then day). Under the four other
seeds, with log(onset speed + 1) and with the bad electrodes included, the top two are day and angle
in both bands.''')
setres(90,'''**Result: partially reproduced.** Reach angle is the most often retained feature in precentral,
postcentral and inferior parietal regions for both bands (0.52 averaged over these). The order of the
next four does not hold: over the sensorimotor regions it is magnitude (0.356), speech ratio (0.355),
duration (0.354) and onset speed (0.350), and over all regions speech ratio, bimanual class, bimanual
ratio and onset speed.''')
setres(93,'''**Result: reproduced.** Over models with R2 > 0.05 the median reach angle coefficient is -0.71 for LFB
(13 of 14 negative) and +0.53 for HFB (13 of 14 positive); with the code's selection by LFB R2 the
HFB median is +0.23. It is -0.59 to -0.72 (LFB) and +0.51 to +0.53 (HFB) under the other seeds,
-0.70 and +0.53 with log(onset speed + 1), and -0.47 and +0.39 with the bad electrodes included.''')
setres(96,'''**Result: reproduced.** Under both readings, recording day (SD of its one-hot coefficients) and reach
angle have the two largest coefficient magnitudes in both bands: LFB 0.97 and 0.71, HFB 0.71 and 0.53
(the next is magnitude, 0.28). The code's selection by LFB R2 gives the same two (HFB 0.24 and 0.23),
and so do the four other seeds, log(onset speed + 1) and the bad electrodes included (reading a).''')
s=src(99)
s=s.replace('| fig2-event-counts | not reproduced (210 to 976 events per subject, median 691) |','| fig2-event-counts | not reproduced (210 to 976 events per subject, median 692) |')
s=s.replace('| fig4-precentral-subject-variability | partially reproduced (3 of 4 parts; S09 has no HFB increase) |','| fig4-precentral-subject-variability | partially reproduced (2 of 4 parts; S09 has no HFB increase, S04 and S08 tied for the narrowest decrease) |')
s=s.replace('| table1-subject-band-power-ci | partially reproduced (21 of 24) |','| table1-subject-band-power-ci | partially reproduced (18 of 24) |')
s=s.replace('| fig5-recording-day-effects | partially reproduced (20 of 24) |','| fig5-recording-day-effects | not reproduced (18 of 24; 20 with each file\'s own electrode flags) |')
a=s.index('How the analysis differs')
s=s[:a]+'''How the analysis differs from the paper's. The paper started from its own curated epochs and
spectral power (Figshare); here everything is computed from the dataset's continuous ECoG, with the
Methods' spectral method and the code's parameters. The segment rejection pools power over the good
electrodes and 1-200 Hz (an assumption). The good-electrode flags differ between a subject's files;
the electrodes good in every file of the subject are used throughout (an assumption), and each
file's own flags are shown as a variant for the region claims. That choice decides
fig5-recording-day-effects (18 of 24 pairs agree with it, 20 with each file's flags). The dataset
has no false-positive flag, so none are removed beyond what it holds. The regression's Delta R2 is
computed only where R2 > 0.05 (the only models the claims use), and the code's Delta R2 variant is
run with the code's 80/20 splits. The seed, log(onset speed + 1) and bad-electrode variants refit
the models with R2 > 0.03 under the main fits, and the bad electrodes, with the Methods' splits.

What was found about the dataset (numbers above):

- The subjects and days are those of the paper, and the paper's projection matrices match the
  electrodes in all 12 subjects. The event features, the pose and the ECoG agree with one another:
  the stored reach magnitude equals the one computed from the pose (ratio 1.007), and event-locked
  power changes at the true onsets differ from those at pseudo-onsets 3 s earlier (Wilcoxon p < 0.05)
  in 10 of 12 subjects for LFB and 8 of 12 for HFB. For S09 neither band differs, so the neural data
  could not establish the alignment there.
- The ECoG of three files ends hours before the day ends (S01 day 7, S04 day 3, S06 day 3), while the
  pose and the events go on: 237 events have no ECoG. Another 125 events fall on NaN samples.
- In S09 and S10 every analysed event has, on at least one electrode marked good in every file, a
  run of at least 25 exact zero samples (50 ms) in its 10 s segment; no electrode's wavelet power
  becomes infinite in the analysis window.
- The dataset holds more events than the paper analysed (8088; 211 to 996 per subject, median 770.5,
  against 151 to 947, median 640).
- Undocumented conventions: the reach angle is in image coordinates (y down); the bimanual overlap,
  described as a fraction of the movement, is in seconds (1661 of all 8088 events above 1); the pose
  is labelled meters but is in pixels; good-electrode flags differ between a subject's files; 24
  electrodes (S03, S12) have no position; the electrodes table carries R2 columns without a
  description.
- One event (S08 day 4) is at 40.3 s in ReachEvents and at 86440.3 s in the reaches table, past the
  end of the 86400 s recording; it is left out of reading (b).
- Electrode groups described as depth are in 7 subjects, where the paper reports 5.
'''
setsrc(99,s)
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
python3 $TMPDIR/nbtext.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
timeout 900 ../../executed/peterson-2021/.venv/bin/python -c "
import ajile, numpy as np
a=ajile.list_assets(); m=ajile.load_all_meta(a)
ev=ajile.event_table(m)
print(len(ev), int((ev.bimanual_overlap>1).sum()), ev.bimanual_overlap.max())
" 2>&1 | tail -2; date -u
```

```
8088 1708 3.833333333
Wed Nov 25 09:46:27 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
P='reproduce_peterson_2021.ipynb'
nb=json.load(open(P)); C=nb['cells']
s=''.join(C[99]['source'])
a='described as a fraction of the movement, is in seconds (1661 of all 8088 events above 1); the pose'
assert a in s
s=s.replace(a,'described as a fraction of the movement, is in seconds (1708 of all 8088 events above 1); the pose')
C[99]['source']=s.rstrip('\n').splitlines(True)
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
grep -c "1708" reproduce_peterson_2021.ipynb; cat ../../questions/peterson-2021.yaml 2>/dev/null | head -40; ls ../../questions | grep peter; head -60 ../../questions/README.md
```

```
1
# Questions

`<dandiset>.yaml` holds an attempt's questions to a reader: places where the author or a verifier
believes the claims file misreads the paper (docs/protocol.md, "Author", step 1.6, and "Hand over for
verification"), and the reader's answers ("Reader", step 6), which say whether the claims file was
amended and why. Each question has `claim`, `question`, `passage`, `why` (how the misreading could
change the outcome), and, once answered, `answer` and `answered` (a date). Method details the claims
file lacks are not asked here: the author takes them from the paper, and a detail the paper does not
settle is a question for the paper's authors, recorded in the claim's notes and as a
`methods_unavailable` finding in the attempt. Files from before protocol `pilot-11` also hold
questions about method details, asked under the earlier rule.
```

**Agent calls Bash**

```bash
cd ../../questions; head -30 asari-2009.yaml; grep -l "claims_file\|^- claim" *.yaml | head -3; grep -rn "questions" ../schemas/*.json 2>/dev/null | head -3; ls ../schemas
```

```
questions:
- claim: fig2-example-long-context
  question: The criterion says the example cell and probe are not identified and accepts any
    current-clamp cell with seven natural sound fragments and a probe tested after silence and
    two other fragments. Does the Figure 2 legend identify them? Figure 2A gives the cell's
    reliability (0.61 +/- 0.07 over its stimuli) and the probe's (0.74 +/- 0.08), and Figure 2B
    says its red trace is "the one shown in A". In the data set only 20051222-ha1-001-002 has
    those values (0.611 +/- 0.081, and 0.737 for probe 4), so its probe 4 would be the example.
    Should the criterion test that probe?
  passage: 'Figure 2 legend, "The neuron showed high trial-to-trial reliability (correlation
    coefficients across trials to this particular probe stimulus, 0.74 +- 0.08; and across trials
    across all natural sound stimuli examined in this cell, 0.61 +- 0.07; mean +- SD). B: the mean
    responses to the probe stimulus in 3 different contexts: red line for the one shown in A and
    blue and green lines for the one in response to the same probe stimulus but preceded by
    "silence" and another conditioning stimulus, respectively."'
  why: Under the criterion as written the claim is reproduced by probe 4 of 20060105-ha1-001-002,
    one of 20 candidates, from a cell whose mean reliability is 0.309, so it cannot be the paper's
    example. Probe 4 of 20051222-ha1-001-002 is significant up to 1.60 s, not from 1.60 to 3.97 s,
    and again from 3.97 to 4.60 s; its run at 3.97 s starts 30 ms inside the 2 to 4 s window, so
    it fails the strict test. Read as identifying that probe, the outcome would turn on how the
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd ..; n=$(grep -n "id: roi-projection-link" claims/peterson-2021.yaml | cut -d: -f1); sed -n "${n},$((n+40))p" claims/peterson-2021.yaml | awk 'NR>1 && /^- id:/{exit} {print}'; n=$(grep -n "id: fig2-event-counts" claims/peterson-2021.yaml | cut -d: -f1); sed -n "${n},$((n+30))p" claims/peterson-2021.yaml | awk 'NR>1 && /^- id:/{exit} {print}'
```

```
- id: roi-projection-link
  kind: link
  statement: The rows of the paper's projection matrices from electrodes to the eight regions,
    deposited on Figshare, can be matched one to one to the dataset's electrodes, and their weights
    fit the electrodes' positions.
  source: Methods, Projecting power into regions of interest; Figshare item 12114408 version 1
    (aal_XX_elecs2ROI.csv and aal_XX_ROIcentroids_Lside.csv)
  data: with_inputs
  criterion: Added by the author (protocol, author step 4). Rows are matched to the electrodes of
    each subject's NWB file by order, as the paper's code (load_project_spectral_power) applies them
    to its power files; where a file has more rows than electrodes, the code's rule (drop all-zero
    rows) is used. The link holds (reproduced) when for all 12 subjects the rows used equal the
    electrodes in number, and the region with the largest weight is the region whose centroid
    (aal_XX_ROIcentroids_Lside.csv) is nearest the electrode's mirrored MNI position for more
    electrodes than with the electrode order shuffled (200 shuffles). Partially reproduced when this
    holds for 9 to 11 subjects. The eight regions with mean density above 3 are also checked against
    those the claims file names.
- id: fig2-event-counts
  statement: Each subject contributed between 151 and 947 movement events (median 640 across
    subjects).
[... 19 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "questions/peterson-2021.yaml",
 "content": "questions:\n- claim: roi-projection-link\n  question: The criterion gives the code's rule for matching the rows of the projection matrices\n    to electrodes as \"drop all-zero rows\". The code also drops the first of the rows that are not\n    all zero. Should the criterion give the code's full rule?\n  passage: 'tfr_utils.load_project_spectral_power (commit 04c6faf), `np.nonzero(df.transpose().mean().values\n    != 0)[0][1:]`; Methods, \"Projecting power into regions of interest\".'\n  why: Under the rule as worded, every subject keeps one row more than it has electrodes (the\n    first row holds the electrode density of each region), so the counts never match and the\n    claim would fail. The attempt used the code's full rule, under which the rows match the\n    electrodes with a position in all 12 subjects. The verifier of round 1 reported this.\n- claim: fig2-reach-shape\n  question: The criterion evaluates a Gaussian kernel density with Scott's bandwidth on the folded\n    angle and asks for its two highest maxima within 15 degrees of -90 and +90. The folded angle\n    ends at +-90, and a kernel density without boundary correction moves a maximum that sits at\n    the boundary inward by about one bandwidth. Should the window allow for this, or should the\n    criterion use a boundary-corrected density or a histogram?\n  passage: 'Results, Behavior during naturalistic movements, paragraph 3, \"For reach angle, the\n    distributions tend to be bimodal, with peaks at +-90\"; Figure 2 (seaborn kdeplot).'\n  why: The angle part decides the outcome (partially reproduced). In every subject the density at\n    +75 degrees is above that at +90, and the pooled maxima are at -71.5 and +75 degrees, just\n    outside the window. A boundary-corrected reading could pass the +90 side. The -90 side may\n    still fail, as only 6.4% of the pooled events lie within 15 degrees of -90 and the density at\n    -75 degrees is below that at 0. The verifier of round 1 reported this.\n- claim: fig2-event-counts\n  question: The Methods keep only movement events lasting 0.5 to 4 s. The criterion's readings\n    count all events in the dataset, or those left after the segment rejection, and neither\n    applies this filter. Should the readings include it?\n  passage: 'Methods, \"In addition, we only retained movement events where (1) movement durations\n    were between 0.5-4 s; (2) the confidence scores from DeepLabCut were >0.4 ... and (3) wrist\n    movements followed a parabolic trajectory\".'\n  why: The dataset holds events as short as 0.233 s. With the filter the fewest events in a\n    subject are 208 (all events) or 207 (after the segment rejection), still outside 151 +- 15.1,\n    so the outcome (not reproduced) would not change here; it could for another dataset version.\n    The verifier of round 1 reported this.\n"
}
```

```
File created successfully at: questions/peterson-2021.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat entries/peterson-2021/README.md; python3 -c "import yaml; yaml.safe_load(open('questions/peterson-2021.yaml')); print('yaml ok')"
```

```
# Peterson, Singh, Wang, Rao & Brunton (2021) from dandiset 000055

Tests the findings of [Peterson et al. (2021)](https://doi.org/10.1523/eneuro.0007-21.2021) on
[DANDI:000055](https://dandiarchive.org/dandiset/000055/0.261123.1703) (AJILE12), which holds the
ECoG, pose and wrist movement events of the paper's 12 subjects over 55 days. The ECoG around each
of 8088 events is streamed from the archive, and region power uses the paper's projection matrices
from [Figshare](https://doi.org/10.6084/m9.figshare.12114408.v1).

| Claim | Outcome |
|---|---|
| Subjects and days are the paper's | Reproduced |
| The Figshare projection matrices match the electrodes | Reproduced |
| Cohort: sex, age, electrodes, hemispheres | Partially reproduced |
| 151 to 947 events per subject, median 640 | Not reproduced |
| All ten features differ across subjects | Reproduced |
| Reach duration and magnitude small, angles peak at +-90 | Partially reproduced |
| Bimanual features skewed toward unimanual | Reproduced |
| Contralateral wrist moves more than ipsilateral | Reproduced |
| Feature correlations | Partially reproduced |
| Events even across days except S04, S05, S09; mostly waking | Partially reproduced |
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peterson-2021 && python3 - <<'EOF'
p='README.md'; s=open(p).read()
a='| Recording-day effects per subject | Partially reproduced |'
assert a in s; s=s.replace(a,'| Recording-day effects per subject | Not reproduced |')
open(p,'w').write(s)
EOF
cd ../.. && date -u && timeout 7000 python tools/entry.py all entries/peterson-2021 > $TMPDIR/run2.log 2>&1; echo exit $?; date -u; tail -4 $TMPDIR/run2.log
```

```
Wed Nov 25 09:47:01 UTC 2026
exit 0
Wed Nov 25 10:25:02 UTC 2026
Installed kernelspec registry-peterson-2021 in executed/peterson-2021/.venv/share/jupyter/kernels/registry-peterson-2021
0 error(s)
pass  reproduce_peterson_2021.ipynb  (2275 s)
```

**Agent calls Bash**

```bash
python3 -c "
import json
nb=json.load(open('executed/peterson-2021/reproduce_peterson_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    out=''.join(''.join(o.get('text','')) for o in c['outputs'] if o['output_type']=='stream' and o.get('name')=='stdout')
    print('=====',i); print(out)
" > $TMPDIR/out2.txt; grep -v "^  " $TMPDIR/out1.txt > $TMPDIR/a1; grep -v "^  " $TMPDIR/out2.txt > $TMPDIR/a2; diff <(grep -v "s$\| s;\|min;\|spectral pass\|regression [0-9]" $TMPDIR/a1) <(grep -v "s$\| s;\|min;\|spectral pass\|regression [0-9]" $TMPDIR/a2) | head -30
```

```
1d0
< nbformat 4 5 ids 101 101
4a4,66
> ===== 2
> 55 files, 845.869916389 GB in all
> 
> ===== 3
> subjects: [np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7), np.int64(8), np.int64(9), np.int64(10), np.int64(11), np.int64(12)]
> days per subject: {1: [np.int64(3), np.int64(4), np.int64(5), np.int64(7)], 2: [np.int64(3), np.int64(4), np.int64(5), np.int64(6)], 3: [np.int64(3), np.int64(4), np.int64(5), np.int64(6)], 4: [np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)], 5: [np.int64(3), np.int64(4), np.int64(7)], 6: [np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)], 7: [np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)], 8: [np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)], 9: [np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)], 10: [np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)], 11: [np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)], 12: [np.int64(3), np.int64(4), np.int64(5), np.int64(6), np.int64(7)]}
> session_description: All times are the hospital's local wall-clock times. The recording dates were removed to de-identify the participants, and the dates are shifted to January 2000. The offset of the times from UTC is unknown, so session_start_time is given with a +00:00 offset. The session starts at midnight of the recording day, and every time in the file counts from that midnight.
> 0         1    3   M  P44Y  2000-01-03   24.000000    94          94    85            0     156     r_wrist        24.0                      0
> 1         1    4   M  P44Y  2000-01-04   24.000000    94          94    91            0     196     r_wrist        24.0                      0
> 2         1    5   M  P44Y  2000-01-05   24.000000    94          94    91            0     199     r_wrist        24.0                      0
> 3         1    7   M  P44Y  2000-01-07   15.477107    94          94    91            0     190     r_wri
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; for k in "overlap values above" "pairs agreeing" "in_median_of_bandmedian" "parts holding" "(a) regions with any" "largest split" "seed + 4000: largest" "all electrodes (main" "table1: inside" "kept events with" "LFB: (a)" "largest day deviation" "notebook run time" "reading a: 8088"; do grep -h -F "$k" out2.txt | head -2; done
```

```
overlap values above 1: 1622 of 7649 ; in all events: 1708 of 8088
pairs agreeing, band mean: 18 of 24; band median: 18 of 24
table1: inside (mean of band mean) 21 of 24; fig5-recording-day-effects: pairs agreeing (band mean) 20 of 24; discussion: largest day deviation 1.487 dB
    subject band  paper_lo  paper_hi  mean_of_bandmean  in_mean_of_bandmean  median_of_bandmean  in_median_of_bandmean ci_median_bandmean  mean_of_bandmedian  in_mean_of_bandmedian  median_of_bandmedian  in_median_of_bandmedian ci_median_bandmedian
in_median_of_bandmedian 18 of 24
parts holding: 2 of 4
fig4: parts holding 3 of 4 [False, True, True, True] ; subjects without the part 1 pattern: ['S09'] {'S09': {'lfb_8_32': -0.25, 'hfb_76_100': -0.029999999329447746, 'holds': False}}
(a) regions with any: low 8 high 8 -> low larger: False
largest split-averaged withheld R2 (90/10, band mean): 0.1770 (S07, electrode 10, hfb)
seed + 4000: largest R2 0.1819; {'lfb': {'n': 12, 'top_delta': [np.str_('day'), np.str_('angle')], 'angle_coef': -0.59, 'top_coef': [np.str_('day'), np.str_('angle')]}, 'hfb': {'n': 13, 'top_delta': [np.str_('day'), np.str_('angle')], 'angle_coef': 0.505, 'top_coef': [np.str_('day'), np.str_('angle')]}}
all electrodes (main + bad): {'lfb': {'n': 21, 'top_delta': [np.str_('day'), np.str_('angle')], 'angle_coef': -0.473, 'top_coef': [np.str_('day'), np.str_('angle')]}, 'hfb': {'n': 21, 'top_delta': [np.str_('day'), np.str_('angle')], 'angle_coef': 0.388, 'top_coef': [np.str_('day'), np.str_('angle')]}}
table1: inside (mean of band mean) 21 of 24; fig5-recording-day-effects: pairs agreeing (band mean) 20 of 24; discussion: largest day deviation 1.487 dB
kept events with a good electrode holding any exact zero sample in the segment: 1019 of 7649 ; per subject: {1: 6, 2: 1, 3: 4, 4: 2, 5: 4, 6: 9, 7: 4, 8: 6, 9: 210, 10: 746, 11: 10, 12: 17}
kept events with a good electrode holding a run of at least 25 zero samples (50 ms): 956 ; per subject: {9: 210, 10: 746} ; electrodes in suc
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json
s=json.load(open('schemas/attempt.schema.json'))
def find(o,path=''):
    if isinstance(o,dict):
        for k,v in o.items():
            if k in ('verifications','proposed','findings'): print(path+'/'+k, json.dumps(v)[:2500]); print()
            find(v,path+'/'+k)
    elif isinstance(o,list):
        for i,v in enumerate(o): find(v,path+f'[{i}]')
find(s)
" | head -60; grep -l "verifications:" attempts/*.yaml | head -3
```

```
/properties/outcomes/items/properties/proposed {"description": "A change of outcome found after the last verification round, held until a further round agrees with it.", "type": "object", "additionalProperties": false, "required": ["outcome", "reason"], "properties": {"outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}, "blocked_by": {"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "dataset_missing", "too_large", "not_runnable", "other"]}, "reason": {"type": "string", "minLength": 1}}}

/properties/verifications {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["date", "kind", "by", "results"], "properties": {"date": {"type": "string", "format": "date"}, "kind": {"enum": ["agent", "person", "paper_author"]}, "by": {"type": "string"}, "results": {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["claim", "agrees"], "properties": {"claim": {"type": "string"}, "agrees": {"type": "boolean"}, "reason": {"description": "The verifier's reason, in its own words.", "type": "string"}, "response": {"description": "What the author changed or replied, kept apart from the verifier's reason.", "type": "string"}, "outcome": {"description": "The outcome the verifier would give.", "enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}}}}, "reviewed": {"description": "What was reviewed, e.g. a commit, when the attempt changed afterwards.", "type": "string"}, "findings": {"description": "From protocol pilot-18, in round 2: what the verifier said of each finding the record rates `critical` (docs/protocol.md, the attempt record).", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["finding", "agrees"], "properties": {"finding": {"description": "The finding's number in this record's `findings`, from 1.", "type": "inte
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A12 "^verifications:" attempts/andrews-2024-01.yaml | head -30
```

```
285:verifications:
286-- date: '2026-11-10'
287-  kind: agent
288-  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
289-  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
290-    module and the claims file, with the paper's full text under paper/. The verifier queried the
291-    DANDI API for the version's assets and metadata, checked Table 1 against cell 16 by hand, and
292-    tested light_steps, window_rates and reduce_chunk on synthetic inputs.
293-  results:
294-  - claim: table1-cohort
295-    agrees: true
296-    outcome: partially_reproduced
297-    reason: Cells 5 and 16 give 12 slices and 7 patients (patient read from the slice-name letter),
```

**Agent**

Re-run reproduces the first full run's numbers exactly. Now writing the attempt record with the round-1 verification block.

**Agent calls Bash**

```bash
sed -n 355,437p attempts/peterson-2021-02.yaml > $TMPDIR/findings_old.yaml; date -u
```

```
Wed Nov 25 10:25:21 UTC 2026
```

**Agent**

Now the outcomes section (lines 28 to 354) is rewritten in full.

**Agent calls Bash**

```bash
cat > $TMPDIR/outcomes.yaml <<'EOF'
outcomes:
- claim: subject-days
  outcome: reproduced
  notebook: reproduce_peterson_2021.ipynb
  output: claim:subject-days
  notes: The dataset's subjects 01 to 12 have exactly the days of Table 2 (S01 days 3, 4, 5 and 7;
    S02 and S03 days 3 to 6; S05 days 3, 4 and 7; the others days 3 to 7), 55 subject-days. The
    subjects are taken as S01 to S12 in order.
- claim: roi-projection-link
  outcome: reproduced
  notebook: reproduce_peterson_2021.ipynb
  output: claim:roi-projection-link
  notes: The paper's code rule (keep the rows that are not all zero and drop the first of them,
    tfr_utils.load_project_spectral_power) leaves exactly as many rows as electrodes with a
    position in all 12 subjects. The dropped first row is the electrode density of each region (the
    other rows sum to 1 per region), and the regions with mean density above 3 are exactly the eight
    of the claims file. After the density row, the zero rows of S03 (16) and S12 (8) sit exactly at
    the indices of the electrodes without a position, and S01's 4 extra zero rows follow its last
    electrode. The largest-weight region is the region whose centroid is nearest the mirrored
    electrode position for 36 to 55% of electrodes per subject, against at most 14 electrodes in 200
    shuffles of the electrode order; all 12 subjects beat every shuffle under all five seeds.
    Shifting the rows by 1 to 3 places lowers the fraction in all 12 subjects.
  deviations:
  - The criterion's rule as worded (drop all-zero rows) leaves one row too many in every subject and
    drops the zero rows of the 24 electrodes without a position in S03 and S12. The code's rule
    (tfr_utils.load_project_spectral_power, commit 04c6faf, `np.nonzero(df.transpose().mean().values
    != 0)[0][1:]`) also drops the first non-zero row; it is used, and the rows are applied in order
    to the electrodes with a position. Electrodes without a position get no weight. The wording is
    asked about in questions/peterson-2021.yaml.
- claim: cohort
  outcome: partially_reproduced
  notebook: reproduce_peterson_2021.ipynb
  output: claim:cohort
  measured:
  - 12
  - 8
  - 29.42
  - 84.83
  - 7
  - 23.71
  - 5
  notes: Twelve subjects, 8 male, mean age 29.42 years (SD 7.94), 84.83 surface electrodes on average
    (SD 11.61) and 5 right-hemisphere implants match. Electrode groups described in the files as
    depth are in 7 subjects (S01 8, S02 16, S03 16, S09 28, S10 48, S11 18, S12 32), not 5; their mean
    of 23.71 (SD 13.39) is within the stated 23.2 +- 12.1. Counting only the grid as surface gives
    63.08 electrodes on average (SD 3.18), outside 87.0 +- 12.9, so that reading is not kept. The
    ages are the files' ages, which may not be the ages at recording.
  deviations:
  - Surface and depth electrodes are told apart by the description of each electrode group (depth
    when it says depth). The hemisphere is the side of the mean MNI x of the subject's electrodes.
- claim: fig2-event-counts
  outcome: not_reproduced
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig2-event-counts
  measured:
  - 211
  - 996
  - 770.5
  notes: Under reading (a), all events in the files, the counts per subject are 211 to 996 with median
    770.5. Under reading (b), after the segment rejection, they are 210 to 976 with median 692. With
    only the events that have ECoG without missing samples, 211 to 986, median 700.5. Under reading
    (b) the median and the largest count are within tolerance, but in every reading the fewest events
    (210 or 211, in S09) are outside 151 +- 15.1. The dataset has no false-positive flag, so reading
    (b) cannot drop those events. Keeping only events of 0.5 to 4 s, as the Methods do (not a reading
    of the criterion), leaves 208 to 984 (median 735.5) and 207 to 964 (median 670); the fewest are
    still outside the tolerance.
  deviations:
  - The dataset has no flag for the events the paper removed as false positives; none are dropped
    for it.
  - Reading (b) uses the assumed pooling of the segment rejection (see the deviation of
    fig3-group-lfb-decrease-hfb-increase); 125 events with NaN ECoG samples, 237 without ECoG and
    1 whose two event times disagree count as missing data.
- claim: fig2-features-differ-across-subjects
  outcome: reproduced
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig2-features-differ-across-subjects
  notes: One-way Kruskal-Wallis across the 12 subjects on the 7649 events of reading (b) gives
    p < 0.001 for all ten features; the largest p is 7.0e-33 (reach duration). Reading (a), all 8088
    events, gives the same.
  deviations:
  - Time of day is the event time in hours after the file's midnight (the files' session
    description); reach duration is stop_time minus start_time; reach angle is the stored angle
    negated and folded to -90..90, as the code does, because the stored angle is in image
    coordinates (checked against the pose).
- claim: fig2-reach-shape
  outcome: partially_reproduced
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig2-reach-shape
  notes: Most reaches last under 2 s (88 to 95% per subject, 91.8% pooled) and cover under 200 pixels
    (59 to 100% per subject, 91.3% pooled), in 12 of 12 subjects. The angle part holds in 0 of 12
    subjects and not pooled. Pooled, the two highest maxima of the folded-angle density are at -71.5
    and +75 degrees, and the density at 0 degrees (0.00407) is above the lower maximum (0.004). The
    density at +75 degrees is above that at +90 in every subject, which the kernel's smoothing at
    the boundary can cause; but only 6.4% of pooled events lie within 15 degrees of -90 (19.7% of
    +90), and the pooled density at -75 degrees (0.00395) is below that at 0. Reading (a) gives the
    same outcome. Whether the criterion should allow for the boundary is asked in
    questions/peterson-2021.yaml.
  deviations:
  - The density is evaluated on a 0.5 degree grid, and the end points of the grid count as maxima
    when they exceed their neighbour (standard choices, stated in the notebook).
- claim: fig2-bimanual-skew
  outcome: reproduced
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig2-bimanual-skew
  notes: The median bimanual ratio is below 0.5 in 12 of 12 subjects (0.14 pooled) and the overlap
    skewness positive in 12 of 12 (1.11 pooled); more than half the events are bimanual in 12 of 12
    (73% pooled). The five highest median ratios are S04, S07, S05, S02 and S03, and the five lowest
    overlap skewnesses S07, S05, S02, S03 and S04, so S02, S04 and S05 are among both.
  deviations:
  - The files hold no missing bimanual ratios, so the code's fill value of 0.5 is never used.
- claim: extfig2-1c-contralateral-larger
  outcome: reproduced
  notebook: reproduce_peterson_2021.ipynb
  output: claim:extfig2-1c-contralateral-larger
  notes: In all 12 subjects and under both readings of the rest position, the peak over 0 to 1.5 s of
    the median contralateral displacement exceeds that of the ipsilateral wrist. The ratio is 1.06 to
    42.0 under reading (b) and 1.12 to 38.1 under reading (a); it is smallest for S05 and S04 (1.06
    to 1.30), a margin the criterion does not judge. The contralateral wrist is the one the
    ReachEvents description of each file names. 56 of 7649 events have missing pose in the window
    and are left out of the medians.
- claim: extfig2-2-feature-correlations
  outcome: partially_reproduced
  notebook: reproduce_peterson_2021.ipynb
  output: claim:extfig2-2-feature-correlations
  measured:
  - 0.232
  - 0.605
  - 0.508
  - 0.5
  - 0.493
  - 0.597
  notes: Five of the six Pearson correlations over the pooled events of reading (b) are within 10% of
    the paper's; reach magnitude and duration correlate at 0.232, below 0.234. Reading (a) gives 0.231
    for that pair and the same five matches.
- claim: fig2-days-and-waking
  outcome: partially_reproduced
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig2-days-and-waking
  notes: The waking part holds; 64 to 96% of each subject's events fall between 08:00 and 24:00. The
    busiest day holds more than half of the events for S05 (0.606, day 7) and S09 (0.519, day 5) and
    for none of the other subjects; for S04 it holds 0.400 (day 7), so the day part does not hold.
    Reading (a) gives the same two subjects.
- claim: fig3-group-lfb-decrease-hfb-increase
  outcome: reproduced
  assumed: true
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig3-group-lfb-decrease-hfb-increase
  notes: Over 0 to 0.5 s the masked group power over 4-30 Hz and 50-120 Hz is -0.728 and +0.411 dB in
    precentral, -0.743 and +0.426 in postcentral, and -0.556 and +0.200 in inferior parietal; at the
    bin of 0 s the signs are the same. All three hold under both readings, all five seeds, unmasked,
    and with each file's own good-electrode flags (variant). Middle frontal shows the pattern too;
    in supramarginal and the temporal regions the masked high-frequency values are at most 0.008 dB.
  deviations:
  - Spectral power is computed from the dataset's continuous ECoG, not from the paper's curated
    Figshare epochs, with the Methods' and the code's parameters (helper docstring).
  - Assumed, as the Methods do not say how power is pooled for the segment rejection; Welch power of
    the 10 s segment averaged over the subject's good electrodes, 10*log10 of its mean over 1-200 Hz
    (below 0 dB drops) and over 115-125 Hz (above the subject's mean + 3 SD drops). Segments with
    NaN samples or without ECoG count as missing data, and so does the one event whose ReachEvents
    time and start_time disagree. 75 events drop for high-frequency power and 1 for low power; the
    rest of the 439 dropped events have no ECoG, NaN samples or the time disagreement.
  - Assumed, as the good-electrode flags differ between a subject's files; the good electrodes are
    those marked good in every file of the subject, for the segment rejection, the projection and
    the regression, as the claims file's opening comment renormalises the weights per subject. The
    weights are renormalised to sum 1 per region (code). The flags of each event's own file, the
    assumption of round 1, are shown as a variant for every region claim.
  - An electrode whose wavelet power is not finite in an event gets weight 0 in that event and the
    weights are renormalised (standard choice); no kept event needed it.
  - The bootstrap mask's Benjamini-Hochberg correction runs over the bins computed here (-1.5 to +1.0
    s in 0.1 s steps, 25 frequencies); the paper's time range is not stated.
- claim: fig3-sensorimotor-largest
  outcome: reproduced
  assumed: true
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig3-sensorimotor-largest
  notes: Under readings (a), (b) and (c) and all five seeds, the three largest regions are postcentral,
    precentral and inferior parietal, and each temporal region is below all three. Reading (a) gives
    0.429, 0.418 and 0.251 dB for the three, 0.177 for middle frontal, and at most 0.034 for the
    temporal regions. The variant with each file's flags gives the same under all three readings.
  deviations:
  - The same spectral method and assumptions as fig3-group-lfb-decrease-hfb-increase.
- claim: fig3-lfb-more-widespread
  outcome: blocked
  blocked_by: methods_underspecified
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig3-lfb-more-widespread
  notes: The two readings the criterion names disagree, so the claim is blocked as the criterion
    says. Reading (b), significant bins per frequency bin over 0 to 0.5 s summed over the eight
    regions, gives 36.0 for low-frequency decreases against 22.2 for high-frequency increases, and
    holds under all five seeds (35.8 to 36.6 against 22.1 to 22.4). Reading (a), regions with any
    significant bin, gives 8 against 8 under the claim's seed, and 7 or 8 against 8 under the
    others, so the low count is never larger. Supramarginal (30 bins) and superior temporal (27
    bins) have significant low-frequency decreases. With each file's flags (variant) the readings
    give 7 against 8 and 34.6 against 24.0, the same disagreement. The question of which measure
    the paper meant is recorded for its authors.
  deviations:
  - The same spectral method and assumptions as fig3-group-lfb-decrease-hfb-increase.
- claim: fig4-precentral-subject-variability
  outcome: partially_reproduced
  assumed: true
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig4-precentral-subject-variability
  notes: Two of four parts hold. Part 2, S03, S06, S07, S08 and S11 have positive power at 116 and
    121 Hz. Part 3, S09 and S12 peak among 56-121 Hz at 76 and 66 Hz, with means over 101-121 Hz below
    half the peak. Part 4 fails; the narrowest low-frequency decreases are S07 and S09 (2 bins), and
    S04 and S08 are among six subjects tied at 3 bins, so they are not among the three fewest. Part 1
    fails in one subject; S09 has a mean of -0.039 dB over 76-100 Hz (its 8-32 Hz mean is -0.09). The
    other 11 subjects show the pattern. With each file's own flags (variant), parts 2 to 4 hold and
    part 1 fails for S09 only, also partially reproduced.
  deviations:
  - The same spectral method and assumptions as fig3-group-lfb-decrease-hfb-increase.
- claim: fig5-band-power-differs-across-subjects
  outcome: reproduced
  assumed: true
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig5-band-power-differs-across-subjects
  notes: Kruskal-Wallis across the 12 subjects on 7649 events gives H = 740 (LFB) and 1028 (HFB) for
    band means, and 786 and 953 for band medians, with p printed as 0 (below the smallest double).
    With each file's flags, H = 747 and 1052.
  deviations:
  - The same spectral method and assumptions as fig3-group-lfb-decrease-hfb-increase.
- claim: table1-subject-band-power-ci
  outcome: partially_reproduced
  assumed: true
  notebook: reproduce_peterson_2021.ipynb
  output: claim:table1-subject-band-power-ci
  notes: Under the best of the four readings (the median over events of the band median), 18 of 24
    subject and band values lie inside Table 1's intervals; the other readings give 14 (mean of band
    mean), 16 and 16. Outside are S02 LFB (-0.103 against -1.12 to -0.31), S03 LFB (-1.584 against
    -2.11 to -1.73), S03 HFB (1.044 against 1.39 to 1.67), S06 LFB (-0.647 against -1.63 to -1.11),
    S06 HFB (1.874 against 2.02 to 2.37) and S10 LFB (-0.196 against -0.87 to -0.35). The median band
    mean is below 0 for LFB in 12 of 12 subjects and above 0 for HFB in 11 of 12. With each file's
    own flags (variant) the mean of the band mean puts 21 of 24 inside. The attempt's own
    5000-replicate bootstrap intervals are printed beside the paper's.
  deviations:
  - The same spectral method and assumptions as fig3-group-lfb-decrease-hfb-increase.
- claim: fig5-recording-day-effects
  outcome: not_reproduced
  assumed: true
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig5-recording-day-effects
  notes: With band means 18 of 24 subject and band pairs agree with the paper, and 18 with band
    medians, below the 20 the criterion asks for a partial reproduction. A day effect is found where
    the paper has none for S01 LFB (p = 0.043), S01 HFB (p = 0.022) and S06 HFB (p = 6.9e-11), and is
    not found for S07 HFB (p = 0.073), S08 LFB (p = 0.31) and S10 HFB (p = 0.054), where the paper
    reports one. The other eight significant pairs of the paper are significant here. The outcome
    rests on the choice of good electrodes; with each file's own flags (variant, the main analysis
    of round 1) 20 of 24 agree, which would be partially reproduced. S01 lost 132 events of day 7,
    where its ECoG ends early.
  deviations:
  - The same spectral method and assumptions as fig3-group-lfb-decrease-hfb-increase.
- claim: extfig5-1-baseline-reduces-day-variability
  outcome: reproduced
  assumed: true
  notebook: reproduce_peterson_2021.ipynb
  output: claim:extfig5-1-baseline-reduces-day-variability
  notes: Reading (a), baseline subtraction lowers the SD of the precentral day means in 10 of 12
    subjects for LFB and 12 of 12 for HFB. Reading (b), it lowers it at 91.3% of good electrodes for
    LFB and 90.2% for HFB. Variability remains; 11 subject and band pairs have a significant day effect
    (fig5-recording-day-effects), and the SDs after subtraction are 0.03 to 0.83 dB.
  deviations:
  - The same spectral method and assumptions as fig3-group-lfb-decrease-hfb-increase. Reading (b)
    uses the electrodes good in every file of the subject.
- claim: discussion-day-changes-small
  outcome: reproduced
  assumed: true
  notebook: reproduce_peterson_2021.ipynb
  output: claim:discussion-day-changes-small
  notes: The largest deviation of a day mean from the subject's mean is 1.49 dB (S06 HFB), and every
    subject and band is at most 2.2 dB (1.49 dB with each file's flags too); the largest range of day
    means is 2.04 dB (S06 LFB). Without baseline subtraction the precentral band power is 11.7 to 36.9
    dB in microvolts squared (the files' stored unit), inside 9 to 55 dB; in volts squared it would be
    -108 to -83 dB.
  deviations:
  - The same spectral method and assumptions as fig3-group-lfb-decrease-hfb-increase.
- claim: fig6b-best-models-sensorimotor
  outcome: reproduced
  assumed: true
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig6b-best-models-sensorimotor
  notes: 14 LFB and 14 HFB models have withheld R2 above 0.05, of 976 per band. Reading (a), all 14 LFB
    and 13 of 14 HFB electrodes are in the five frontoparietal regions (the other in superior
    temporal), and the median R2 of sensorimotor electrodes exceeds that of temporal ones (LFB -0.0093
    against -0.0150, HFB -0.0117 against -0.0157). Reading (b), the three regions with the highest
    projected R2 are precentral, postcentral and middle frontal in both bands. Under the four other
    seeds 12 to 14 models per band pass 0.05 (12 LFB at seed + 4000); their regions were not
    recomputed.
  deviations:
  - Assumed, as the good-electrode flags differ between a subject's files; the models use the
    electrodes good in every file of the subject (976 electrodes), on the 7649 events of reading (b).
    The paper reports 4.9 +- 4.9 surface electrodes removed per subject; the files mark 1 to 17 bad in
    every file and 3 to 32 in at least one.
  - Forward selection over single design columns starting from an adjusted R2 of 0, on all of the
    subject's events, as the code does (_forward_selected_new) and the claims file prescribes; the
    test events of each split take part in choosing the features, which can raise R2 a little. 200
    day-balanced splits with 10% test events (Methods). The splits use the seed of this claim, and
    the other Figure 6 claims use the same fits.
  - The variants refit the models with R2 above 0.03 under the main fits (45 electrodes, both bands)
    with the Methods' splits; models below 0.03 are taken not to pass 0.05 under them.
- claim: fig6-r2-at-most-025
  outcome: reproduced
  assumed: true
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig6-r2-at-most-025
  measured: 0.177
  notes: The largest split-averaged withheld R2 is 0.177 (S07, HFB), at most 0.275. It is 0.184 with
    the code's 80/20 splits, 0.158 with band medians, 0.167 to 0.182 under the four other seeds,
    0.174 with log(onset speed + 1), and at most 0.151 at the electrodes bad in at least one file. No
    Huber fit failed to converge. This is an upper bound and is easy to pass.
  deviations:
  - As for fig6b-best-models-sensorimotor.
- claim: fig6c-angle-and-day-most-informative
  outcome: reproduced
  assumed: true
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig6c-angle-and-day-most-informative
  notes: Over the 14 LFB models with R2 above 0.05, recording day (median Delta R2 0.0374) and reach
    angle (0.0307) rank first and second; the eight other features have medians of at most 0.0001. In
    HFB the same two lead (0.0616 and 0.0224). The code's Delta R2 (80/20, test events shuffled) and
    the code's selection by LFB R2 give the same two in both bands (with selection by LFB R2 the HFB
    order is angle, then day). The same two lead in both bands under the four other seeds, with
    log(onset speed + 1), and with the code's inclusion of bad electrodes (21 models per band).
  deviations:
  - As for fig6b-best-models-sensorimotor. The code's Delta R2 variant is run with the code's 80/20
    splits, combining two of the criterion's variants.
- claim: extfig6-2-angle-most-retained
  outcome: partially_reproduced
  assumed: true
  notebook: reproduce_peterson_2021.ipynb
  output: claim:extfig6-2-angle-most-retained
  notes: Reach angle has the highest retention probability in precentral, postcentral and inferior
    parietal regions for both bands (0.516 averaged over these). The order of the next four does not
    hold under either reading; over the three sensorimotor regions it is magnitude (0.356), speech
    ratio (0.355), duration (0.354) and onset speed (0.350), and over all eight regions speech ratio,
    bimanual class, bimanual ratio and onset speed.
  deviations:
  - As for fig6b-best-models-sensorimotor. Forward selection runs once per model on all events (the
    code runs it in every split on all events, which gives the same selection each time), so the
    retention does not depend on the seed.
- claim: fig6d-upward-reaches-enhance-pattern
  outcome: reproduced
  assumed: true
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig6d-upward-reaches-enhance-pattern
  notes: Over models with R2 above 0.05, the median reach angle coefficient is -0.712 for LFB (13 of 14
    negative) and +0.531 for HFB (13 of 14 positive). With the code's selection by LFB R2 the HFB median
    is +0.231. It is -0.59 to -0.72 (LFB) and +0.51 to +0.53 (HFB) under the four other seeds, -0.70
    and +0.53 with log(onset speed + 1), and -0.47 and +0.39 with the bad electrodes included.
    Positive angles are upward because the stored image-coordinate angle is negated before folding,
    as the code does; the convention was checked against the pose.
  deviations:
  - As for fig6b-best-models-sensorimotor.
- claim: fig6d-angle-and-day-largest-coefficients
  outcome: reproduced
  assumed: true
  notebook: reproduce_peterson_2021.ipynb
  output: claim:fig6d-angle-and-day-largest-coefficients
  notes: Under both readings, recording day (SD of its one-hot coefficients) and reach angle have the
    two largest magnitudes in both bands; LFB 0.969 and 0.712, HFB 0.713 and 0.531 (the next is
    magnitude, 0.283). With the code's selection by LFB R2 the same two lead (HFB 0.241 and 0.231).
    Under reading (a) the same two lead under the four other seeds, with log(onset speed + 1), and
    with the bad electrodes included.
  deviations:
  - As for fig6b-best-models-sensorimotor.
EOF
python3 -c "import yaml; d=yaml.safe_load(open('$TMPDIR/outcomes.yaml')); print(len(d['outcomes']))"
```

```
25
```

**Agent calls Bash**

```bash
cat > $TMPDIR/findings.yaml <<'EOF'
findings:
- kind: selection_undocumented
  about: data
  severity: major
  statement: The files hold 8088 movement events, 211 to 996 per subject (median 770.5), where the
    paper analysed 151 to 947 per subject (median 640). Nothing in the files marks the events the
    paper used or the false positives it removed, so the paper's event set cannot be rebuilt;
    dropping the events without usable ECoG still leaves 210 to 976 per subject (median 692).
- kind: data_missing
  severity: minor
  statement: The ECoG of three files ends hours before the day ends while the pose and the events go
    on to 24 h; sub-01 day 7 (15.5 h), sub-04 day 3 (15.7 h) and sub-06 day 3 (15.9 h). 237 events
    (132, 22 and 83) have no neural data.
- kind: metadata_insufficient
  severity: minor
  statement: The ECoG holds stretches of NaN samples, which the files do not describe; 125 events
    have NaN samples within 5 s of onset (47 of them in sub-10).
- kind: metadata_error
  severity: minor
  statement: The bimanual overlap is described as a fraction of the contralateral movement duration,
    but 1708 of 8088 values are above 1 (up to 3.83); the values are consistent with seconds.
- kind: metadata_error
  severity: minor
  statement: The pose series are labelled in meters, but the values are pixels; the reach magnitudes
    computed from the pose equal the stored pixel magnitudes (median ratio 1.007).
- kind: metadata_insufficient
  severity: minor
  statement: The reach angle has no stated convention. It is the angle in image coordinates (y
    downward), -180 to 180 degrees, matching the pose to a median of 1.6 degrees, so upward reaches
    are negative. The paper's code negates and folds it.
- kind: metadata_insufficient
  severity: minor
  statement: The `good` flags of the electrodes differ between the files of a subject (bad in at least
    one file 3 to 32 per subject, bad in every file 1 to 17), and nothing says how they were set or
    which applies to the subject's analyses. The paper reports 4.9 +- 4.9 surface electrodes removed
    per subject.
- kind: metadata_insufficient
  severity: minor
  statement: The electrodes table carries low_freq_R2 and high_freq_R2 columns with no description of
    the model or data they come from.
- kind: identifier_missing
  severity: minor
  statement: 24 electrodes have no position (NaN x, y, z), the 16 depth electrodes of sub-03 and 8 of
    sub-12; the paper's projection matrices give them all-zero rows at their places.
- kind: metadata_error
  severity: minor
  statement: One event of sub-08 day 4 is at 40.3 s in ReachEvents and at 86440.3 s in the reaches
    table, past the end of the 86400 s recording; the other 8087 agree to 1 ms.
- kind: other
  about: data
  severity: minor
  statement: Electrode groups described as depth electrodes are in 7 subjects (sub-01, 02, 03, 09, 10,
    11 and 12), where the paper reports depth electrodes in 5.
- kind: other
  about: data
  severity: minor
  statement: The coarse behavioural labels (epochs) are empty at 4767 of the 8088 event times, and 17
    events fall in epochs labelled sleep or blocklist, which the Methods say were excluded.
- kind: other
  about: data
  severity: none
  statement: Checks that passed. The subjects and days are the paper's; the paper's projection
    matrices match the electrodes of all 12 subjects; ECoG is at 500 Hz in microvolts and pose at 30 Hz.
    Band power at the event onsets differs from that at pseudo-onsets 3 s earlier in the same segments
    in 10 of 12 subjects for LFB and 8 of 12 for HFB, consistent with ECoG and events sharing a clock;
    for sub-09 neither band differs, so the alignment could not be established there.
- kind: methods_unavailable
  statement: Question for the authors. The Methods drop segments with power below 0 dB or with
    115-125 Hz power more than 3 SD above all segments, but do not say how power is pooled over
    electrodes and frequencies, or whether the SD is per subject. This attempt assumed the Welch power
    of the 10 s segment averaged over the subject's good electrodes, 1-200 Hz for the 0 dB test and
    115-125 Hz for the 3 SD test per subject; it drops 76 events. Please confirm or correct.
- kind: methods_unavailable
  statement: Question for the authors. The Results say low-frequency decreases are more spatially
    widespread than high-frequency increases (Figure 3) without a measure. Counting regions with any
    significant bin gives a tie (8 against 8), and counting significant bins per frequency bin favours
    the low frequencies (36.0 against 22.2). Which measure was meant?
- kind: methods_unavailable
  statement: Question for the authors. The dataset's good-electrode flags differ between a subject's
    days. Were bad electrodes removed per day or per subject, and did the analyses use the electrodes
    good on every day? This attempt used the electrodes good on every day for the projection and the
    regression; with each day's own flags, the recording-day effects of 20 of 24 subject and band
    pairs agree with the paper, against 18.
- kind: metadata_insufficient
  severity: minor
  statement: In sub-09 and sub-10 every analysed event has, on 1 to 15 electrodes marked good in
    every file, a run of at least 25 exact zero samples (50 ms) within the 10 s around it; no other
    subject has such runs. The files do not say what the zeros mean.
EOF
python3 -c "import yaml; d=yaml.safe_load(open('$TMPDIR/findings.yaml')); print(len(d['findings']))"
```

```
17
```

**Agent calls Bash**

```bash
cat > $TMPDIR/verif.yaml <<'EOF'
verifications:
- date: '2026-11-25'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
    module and the claims file, with the paper's full text under paper/. The verifier checked the
    version's 55 files and 845.87 GB on the DANDI API and tested the angle folding, the day-balanced
    splits, the band statistics, the one-hot design matrix and the Morlet bank on synthetic inputs.
  results:
  - claim: subject-days
    agrees: true
    outcome: reproduced
    reason: Subjects 01-12 have exactly the paper's days, 55 subject-days.
    response: No change.
  - claim: roi-projection-link
    agrees: true
    outcome: reproduced
    reason: After the code's row rule the rows equal the electrodes with positions in all 12
      subjects; the largest-weight region is the nearest centroid for 36-55% of electrodes against a
      shuffle maximum of 8-14, for every seed, and the eight regions with density > 3 match. For S03
      and S12 the criterion's "rows = electrodes" holds only when electrodes without positions are
      left out. The notebook never checks that the zero rows of S03 and S12 sit at the indices of the
      electrodes without positions, the full-permutation null could not detect a shift of one or a
      few rows, and the claims file describes the code's rule as "drop all-zero rows" only, which
      misreads the code.
    response: Added the check; after the density row, the zero rows of S03 and S12 sit exactly at the
      electrodes without a position, and S01's 4 extra zero rows follow its last electrode. Added a
      test with the rows shifted by 1 to 3 places, which lowers the agreement in all 12 subjects. The
      wording of the criterion is asked about in questions/peterson-2021.yaml; the claim is unchanged.
  - claim: cohort
    agrees: true
    outcome: partially_reproduced
    reason: Six of seven quantities are within tolerance; the dataset has 7 subjects with
      depth-labelled groups where the paper says 5. Depth electrodes are identified from group
      descriptions, and the commented "grid only as surface" variant is not run.
    response: Ran the grid-only variant; it gives 63.08 surface electrodes on average, outside 87.0
      +- 12.9, so the group descriptions stay the reading used. Outcome unchanged.
  - claim: fig2-event-counts
    agrees: true
    outcome: not_reproduced
    reason: The minimum is 211 (reading a) and 210 (reading b) against 151 +- 15.1. The Methods keep
      only events lasting 0.5-4 s and the dataset's durations go down to 0.233 s, but this filter is
      not one of the criterion's readings; it would lower counts but is unlikely to bring S09 down to
      151.
    response: Printed the counts after the 0.5-4 s filter as a variant (fewest 208 and 207), which does
      not change the outcome. Asked a reader whether the readings should include the filter
      (questions/peterson-2021.yaml). Outcome unchanged.
  - claim: fig2-features-differ-across-subjects
    agrees: true
    outcome: reproduced
    reason: Every p is below 1e-32 under both readings.
    response: No change beyond the re-run (largest p 7.0e-33).
  - claim: fig2-reach-shape
    agrees: true
    outcome: partially_reproduced
    reason: The duration and magnitude parts hold in 12 of 12 subjects and pooled; the angle part holds
      in 0 of 12, the KDE peaks sitting near +-60-75 degrees. The criterion's Scott KDE is evaluated
      on the folded -90 to 90 range with no boundary correction, which pulls peaks of mass at +-90
      inward, so the test can fail by construction; this failure decides the partial outcome. The KDE
      plots exist only as images.
    response: Printed the density at -90, -75, 0, +75 and +90 degrees per subject and pooled, and the
      fraction of events within 15 degrees of each end. The density at +75 is above that at +90 in
      every subject, but only 6.4% of events lie within 15 degrees of -90 and the pooled density at
      -75 is below that at 0, so the -90 side fails beyond the boundary effect. The criterion is kept
      and the question is put to a reader (questions/peterson-2021.yaml). Outcome unchanged.
  - claim: fig2-bimanual-skew
    agrees: true
    outcome: reproduced
    reason: Ratio, overlap and class each hold in 12 of 12 subjects and pooled; S02, S04 and S05 are
      in both top-5 sets.
    response: No change.
  - claim: extfig2-1c-contralateral-larger
    agrees: true
    outcome: reproduced
    reason: Holds in 12 of 12 subjects under both readings. The ratio is only 1.06-1.30 for S04 and
      S05, which the criterion does not judge.
    response: The notes now give the small ratios of S04 and S05. Outcome unchanged.
  - claim: extfig2-2-feature-correlations
    agrees: true
    outcome: partially_reproduced
    reason: 5 of 6 correlations are within tolerance; magnitude vs duration is r = 0.229 against 0.26
      +- 0.026.
    response: No change beyond the re-run (r = 0.232).
  - claim: fig2-days-and-waking
    agrees: true
    outcome: partially_reproduced
    reason: The busiest day holds more than half of the events for S05 and S09 but not S04 (0.40), so
      the day part fails; the waking part holds in all 12 subjects.
    response: No change.
  - claim: fig3-group-lfb-decrease-hfb-increase
    agrees: true
    outcome: reproduced
    reason: Holds in all three named regions under both readings, for all 5 seeds and also unmasked.
      Region power is built with each file's own good-electrode flags, while the claims header says
      the zeroing and renormalisation are per subject. Non-finite dB on a single electrode is set to 0
      before weighting without renormalising. Benjamini-Hochberg runs only over the bins computed,
      -1.5 to +1.0 s, where the criterion says all time bins; with about 60% of bins significant this
      does not change the outcome.
    response: The main analysis now uses the electrodes good in every file of the subject, for the
      segment rejection and the projection, with each file's flags as a variant. An electrode with
      non-finite power gets weight 0 in that event and the weights are renormalised; no kept event
      needed it, and the counts of events with exact zeros on good electrodes are printed. The
      Benjamini-Hochberg range is unchanged, as the paper does not state the spectrograms' time
      range. Outcome unchanged; it holds under both electrode choices.
  - claim: fig3-sensorimotor-largest
    agrees: true
    outcome: reproduced
    reason: Under readings a, b and c the top three regions are postcentral, precentral and inferior
      parietal, and the temporal regions are below all three, for all seeds.
    response: Re-run with the electrodes good in every file; same result, and the same with each
      file's flags.
  - claim: fig3-lfb-more-widespread
    agrees: true
    outcome: blocked
    reason: The readings disagree. Under (a) the region counts are 7 vs 7, or 6-8 vs 8 across seeds,
      so low frequencies are never more widespread; under (b) the bin counts are 34.2 vs 23.9. The
      criterion says to block when the readings disagree.
    response: Re-run with the electrodes good in every file; (a) 8 against 8 (7 or 8 against 8 under
      the other seeds) and (b) 36.0 against 22.2, the same disagreement, and the same with each
      file's flags. Outcome unchanged.
  - claim: fig4-precentral-subject-variability
    agrees: true
    outcome: partially_reproduced
    reason: Parts 2, 3 and 4 hold. Part 1 fails for S09, whose HFB value is -0.030 dB.
    response: With the electrodes good in every file, part 4 now fails too (S04 and S08 are tied at 3
      bins with four other subjects, behind S07 and S09 at 2), and part 1 fails for S09 (-0.039 dB), so
      two of four parts hold; with each file's flags three hold. Partially reproduced either way.
  - claim: fig5-band-power-differs-across-subjects
    agrees: true
    outcome: reproduced
    reason: p is about 0 in both bands, for both band statistics.
    response: Re-run; H = 740 to 1028. Outcome unchanged.
  - claim: table1-subject-band-power-ci
    agrees: true
    outcome: partially_reproduced
    reason: The best reading (mean of band mean) puts 21 of 24 inside the paper's intervals; S03 HFB,
      S06 LFB and S06 HFB fall outside. The subject-level electrode reading was not run.
    response: With the electrodes good in every file the best reading is the median of the band median,
      18 of 24 inside (the mean of the band mean gives 14); with each file's flags 21 of 24. Still
      partially reproduced.
  - claim: fig5-recording-day-effects
    agrees: true
    outcome: partially_reproduced
    reason: 20 of 24 pairs agree with the band mean, exactly at the threshold, and 19 of 24 with the
      median variant. The electrode flags differ a lot between days (S04 has 17 bad on day 3 and 2 on
      day 6), so the precentral electrode mix changes from day to day, which can create or hide day
      effects; the subject-level reading was not run for this claim, which sits at 20/24.
    response: Changed to not_reproduced. With the electrodes good in every file of the subject, which
      the claims file's per-subject renormalisation supports and which keeps the electrode mix the
      same across days, 18 of 24 pairs agree under both band statistics, below the criterion's 20.
      Each file's own flags, the round-1 analysis, give 20 of 24 and are shown as a variant; the
      outcome is marked as resting on the assumption.
  - claim: extfig5-1-baseline-reduces-day-variability
    agrees: true
    outcome: reproduced
    reason: The SD drops with baseline in 10/12 (LFB) and 11/12 (HFB) subjects, and in 91% and 90% of
      electrodes; day effects remain.
    response: Re-run with the electrodes good in every file; 10 of 12 and 12 of 12 subjects, 91.3% and
      90.2% of electrodes, day effects in 11 pairs. Outcome unchanged.
  - claim: discussion-day-changes-small
    agrees: true
    outcome: reproduced
    reason: The largest day deviation is 1.48 dB (limit 2.2); levels are 12.2-36.5 dB in the uV^2
      reading.
    response: Re-run; 1.49 dB under both electrode choices, levels 11.7 to 36.9 dB. Outcome unchanged.
  - claim: fig6b-best-models-sensorimotor
    agrees: true
    outcome: reproduced
    reason: Under (a), 14 of 14 (LFB) and 13 of 14 (HFB) models with R2 > 0.05 are frontoparietal and
      the sensorimotor median R2 exceeds the temporal one; under (b) the top three regions are
      frontoparietal in both bands. Both medians are negative. Forward selection runs on all events
      before the splits, which leaks test data into model selection; this is the code's choice and
      the claims file prescribes it, and it inflates R2 slightly for every Figure 6 claim.
    response: The leakage is stated in the notebook and the deviations; the claims file prescribes the
      method, so it is kept. Outcome unchanged.
  - claim: fig6-r2-at-most-025
    agrees: true
    outcome: reproduced
    reason: The largest R2 is 0.177 (0.184 with the 80/20 split); an upper-bound claim, easy to pass.
    response: Added the R2 under log(onset speed + 1) (0.174) and at the bad electrodes (at most
      0.151). Outcome unchanged.
  - claim: fig6c-angle-and-day-most-informative
    agrees: true
    outcome: reproduced
    reason: In LFB the top two are day and angle (n = 14), and also in HFB and in every variant that
      was run. The bad-electrode variant was never run, the log(onset speed + 1) variant was not run,
      and the seed check covers R2 only; at seed + 4000 the LFB selection drops to 12 models and the
      Delta R2 rankings were not refit.
    response: Ran the three variants. Under the four other seeds, with log(onset speed + 1) and with
      the bad electrodes included, day and angle are the top two in both bands. Outcome unchanged.
  - claim: extfig6-2-angle-most-retained
    agrees: true
    outcome: partially_reproduced
    reason: The angle part holds in all 6 region-band cells; the order part fails under both readings
      because speech ratio ranks second.
    response: Re-run; the order part still fails (magnitude, speech ratio, duration and onset speed
      over the sensorimotor regions). Outcome unchanged.
  - claim: fig6d-upward-reaches-enhance-pattern
    agrees: true
    outcome: reproduced
    reason: The median angle coefficient is -0.70 for LFB and +0.54 for HFB; the sign convention is
      confirmed against the pose. The bad-electrode variant was not run.
    response: Ran the seed, log(onset speed + 1) and bad-electrode variants; the signs hold in all
      (LFB -0.47 to -0.72, HFB +0.39 to +0.53). Outcome unchanged.
  - claim: fig6d-angle-and-day-largest-coefficients
    agrees: true
    outcome: reproduced
    reason: Day and angle are the top two under both readings, in both bands and both selections. The
      bad-electrode variant was not run.
    response: Ran the seed, log(onset speed + 1) and bad-electrode variants; day and angle lead in
      all. Outcome unchanged.
EOF
python3 -c "import yaml; d=yaml.safe_load(open('$TMPDIR/verif.yaml')); print(len(d['verifications'][0]['results']))"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 - <<'EOF'
import os
T=os.environ.get('TMPDIR','/tmp/claude-1001')
v=open(f'{T}/verif.yaml').read()
a='''    response: Printed the counts after the 0.5-4 s filter as a variant (fewest 208 and 207), which does
      not change the outcome.'''
assert a in v
v=v.replace(a,'''    response: Printed the counts after the 0.5-4 s filter as a variant (fewest 208 and 207), which does
      not change the outcome. The data check now counts the events whose ReachEvents time and
      start_time differ by more than 1 s; there is one (S08 day 4, 40.3 s against 86440.3 s), and it
      is left out of reading (b).''')
head=open('attempts/peterson-2021-02.yaml').read().split('\noutcomes:\n')[0]
rec=head+'\n'+open(f'{T}/outcomes.yaml').read()+open(f'{T}/findings.yaml').read()+v
open('attempts/peterson-2021-02.yaml','w').write(rec)
import yaml; d=yaml.safe_load(rec); print(list(d.keys()))
EOF
python tools/entry.py check entries/peterson-2021 2>&1 | tail -15
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'entry', 'provenance', 'inputs', 'outcomes', 'findings', 'verifications']
0 error(s)
```

**Agent calls Bash**

```bash
grep -rln "attempt.schema" tools scripts package.json 2>/dev/null | head; grep -n "plain scalar\|': '\|\": \"" tools/*.py | head -5
```

```
tools/build_site.py
tools/agent_run.py:47:TEMPLATES = {"paper-match": "paper-match", "claims": "claims", "claims-check": "claims-check", "answer": "answer",
tools/agent_run.py:48:             "author": "author", "author-answers": "author-answers",
tools/agent_run.py:49:             "verifier-1": "verifier-1", "author-revise-1": "author-revise",
tools/agent_run.py:50:             "verifier-2": "verifier-2", "author-revise-2": "author-revise",
tools/agent_run.py:51:             "verifier-3": "verifier-3", "author-revise-3": "author-revise-3",
```

**Agent calls Bash**

```bash
grep -n "def .*valid\|argparse\|add_argument\|jsonschema" tools/build_site.py | head -20; ls tests | head
```

```
39:import argparse
4786:    parser = argparse.ArgumentParser(description=__doc__,
4787:                                     formatter_class=argparse.RawDescriptionHelpFormatter)
4788:    parser.add_argument("--output", type=Path, default=ROOT / "site")
4789:    parser.add_argument("--demo", type=int, metavar="N",
4791:    parser.add_argument("--issues", type=Path, metavar="JSON",
4793:    parser.add_argument("--queue", type=Path, metavar="JSON",
4795:    parser.add_argument("--responses", type=Path, metavar="JSON",
4797:    parser.add_argument("--noindex", action="store_true",
4799:    parser.add_argument("--notebooks-from", metavar="URL",
4802:    parser.add_argument("--analytics", metavar="TOKEN", default="",
conftest.py
test_build_osf_targets.py
test_build_site.py
test_build_targets.py
test_build_zenodo_targets.py
test_intake.py
test_notify.py
test_protocol_pin.py
test_readme_row.py
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "attempt.schema" tools/build_site.py | head -3; python3 -c "
import json, yaml, jsonschema
s=json.load(open('schemas/attempt.schema.json'))
d=yaml.safe_load(open('attempts/peterson-2021-02.yaml'))
jsonschema.validate(d, s); print('schema ok')
"; python3 - <<'EOF'
# plain scalars containing ': '
import yaml
for f in ['attempts/peterson-2021-02.yaml','questions/peterson-2021.yaml']:
    t=open(f).read()
    for ev in yaml.parse(t):
        if isinstance(ev, yaml.ScalarEvent) and ev.style is None and ': ' in ev.value:
            print(f, ev.value[:80])
print('scan done')
EOF
```

```
147:# What a finding is about when its record does not say (schemas/attempt.schema.json, `about`): the paper for these
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    jsonschema.validate(d, s); print('schema ok')
    ~~~~~~~~~~~~~~~~~~~^^^^^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/jsonschema/validators.py", line 1332, in validate
    raise error
jsonschema.exceptions.ValidationError: datetime.date(2026, 11, 25) is not of type 'string'

Failed validating 'type' in schema['properties']['date']:
    {'type': 'string', 'format': 'date'}

On instance['date']:
    datetime.date(2026, 11, 25)
scan done
```

**Agent calls Bash**

```bash
python3 -c "
import json, yaml, jsonschema
s=json.load(open('schemas/attempt.schema.json'))
d=yaml.load(open('attempts/peterson-2021-02.yaml'), Loader=yaml.BaseLoader)
" ; python3 -c "
import json, yaml, jsonschema, datetime
s=json.load(open('schemas/attempt.schema.json'))
d=yaml.safe_load(open('attempts/peterson-2021-02.yaml'))
d['date']=str(d['date'])
jsonschema.validate(d, s); print('schema ok')
"; ls tools | head -40
```

```
schema ok
__pycache__
agent_run.py
archive_transcripts.sh
archives
author_notes.py
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_osf_targets.py
build_reuse_targets.py
build_site.py
build_sparc_targets.py
build_targets.py
build_zenodo_targets.py
changed_entries.py
claims_check.py
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "attempts/\|def check_attempt\|verifications" tools/entry.py | head -10; python tools/entry.py handover entries/peterson-2021 2>&1 | tail -3; date -u
```

```
380:        for r, rnd in enumerate(attempt.get("verifications") or [], 1):
388:        for rnd in (attempt.get("verifications") or [])[1:]:
wrote executed/peterson-2021/handover
Wed Nov 25 10:27:57 UTC 2026
```

**Agent**

I've worked through every point in the round-1 report and re-run the entry twice with `python tools/entry.py all entries/peterson-2021`. Both runs passed in about 38 minutes and gave the same numbers. `tools/entry.py check` reports 0 errors and the record validates against the schema. Nothing is committed.

**Outcome changes**

- **fig5-recording-day-effects: partially reproduced → not reproduced.** The verifier's problem 1 was that region power used each file's own good-electrode flags, while the claims file renormalises per subject. The main analysis now uses the electrodes good in every file of the subject, for the segment rejection, the projection and the regression. With that choice 18 of 24 subject and band pairs agree with the paper, below the criterion's 20. The outcome is marked as resting on this assumption. Each file's own flags, the round-1 choice, give 20 of 24 and are shown as a variant.
- The other 24 outcomes are unchanged. Some numbers moved:
  - **table1:** the best reading is now 18 of 24 inside the paper's intervals (21 with each file's flags), still partially reproduced.
  - **fig4:** two of four parts now hold (three with each file's flags), still partially reproduced.
  - **fig3-lfb-more-widespread:** the two readings still disagree (8 against 8 regions; 36.0 against 22.2 bins), so it stays blocked.

**Added or corrected**

- Region power is renormalised over electrodes with finite power in each event; no kept event needed it. The notebook now counts events with exact zeros on good electrodes. In S09 and S10 every analysed event has runs of at least 50 ms of zeros on 1 to 15 good electrodes; this is a new minor finding at the end of the list.
- The one event whose two time stamps disagree (S08 day 4, 40.3 s against 86440.3 s, past the end of the recording) is counted and left out of reading (b).
- The regression variants that were missing are now run: the four other seeds with Delta R² and coefficients refit, log(onset speed + 1), and the code's inclusion of bad electrodes. Day and angle stay on top, and the angle signs hold, in all of them.
- Projection rows: the zero rows of S03 and S12 sit exactly at the electrodes without a position. Shifting the rows by 1 to 3 places lowers the agreement with the nearest region in all 12 subjects.
- New printed outputs:
  - a table of the angle density at ±90, ±75 and 0 degrees per subject;
  - event counts after the Methods' 0.5–4 s filter (fewest 207, still outside the tolerance);
  - the grid-only surface count (63.08, outside the tolerance, so the group-description reading stays).
- The forward-selection leakage is now stated in the notebook and the deviations. The claims file prescribes the method, so it is kept.
- One finding's number was wrong: 1708 of 8088 bimanual overlap values are above 1, not 1661 (that figure came from the analysed subset). The findings that describe the clock check, the segment rejection, the spread measure and the electrode flags now give the new numbers.
- I added three questions for a reader in `questions/peterson-2021.yaml`:
  - the "drop all-zero rows" wording for roi-projection-link;
  - the 15° window on a density with no boundary correction for fig2-reach-shape;
  - the 0.5–4 s filter for fig2-event-counts.

  No claim was changed.
- The round is recorded under `verifications`, with all 25 claims. I also updated the notebook conclusions, the summary, the header, the helper docstring and the README.

**Not done**

- The Benjamini–Hochberg correction still runs over the −1.5 to +1.0 s bins only. The paper does not state the spectrograms' time range, and the verifier found it changes no outcome.
- Under the other seeds, the variants refit only the models with R² above 0.03 under the main fits. The regions of the models that pass 0.05 under those seeds were not recomputed.

## End of run

68 turns, 111 minutes, $5.72 at API prices, result: success.
