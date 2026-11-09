# 001249 · author-answers · run 41304245373

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  ls entries/001249-ishii-2025 entries/001249-ishii-2025/*; cat questions/001249.yaml
```

```
Sun Nov  1 12:02:07 UTC 2026
entries/001249-ishii-2025/README.md
entries/001249-ishii-2025/entry.yaml
entries/001249-ishii-2025/mpoa.py
entries/001249-ishii-2025/reproduce_ishii_2025.ipynb
entries/001249-ishii-2025/requirements.in
entries/001249-ishii-2025/requirements.lock.txt

entries/001249-ishii-2025:
README.md
entry.yaml
mpoa.py
reproduce_ishii_2025.ipynb
requirements.in
requirements.lock.txt
# Questions from attempt 001249-ishii-2025-01 (author, 2026-11-01) about
# claims/001249/10.7554-elife.91765.yaml, asked under docs/protocol.md, Author, step 1.6. The claim was
# tested as the file has it.
dandiset: "001249"
paper: doi:10.7554/elife.91765
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -80
```

```
1:# Protocol for an attempt
40:## Reader
42:### 1. Get the paper
53:### 2. Read the paper's code
63:### 3. Write the claims file
148:### 4. Data from outside the paper's own recordings
156:### 5. Check
169:### 6. Answer questions
182:## Author
198:### 1. Establish what can be tested
325:### 2. Check the data against its description
340:### 3. Write the entry
398:### 4. Lock, check and run
409:### 5. Record the attempt
460:### 6. Hand over for verification
498:## Repeat attempts
540:## Local and remote datasets
563:## Verifier
567:### Round 1: without the author's conclusions
592:### Round 2: with the author's conclusions
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,40p docs/protocol.md; sed -n 169,540p docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-13`. Record this version in the attempt's provenance.

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
  only when it believes the file misreads the paper.
[... 392 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls attempts | grep 001249; cat attempts/001249*; grep -n "fig6c-decay-length" -A60 claims/001249/10.7554-elife.91765.yaml | head -90
```

```
<persisted-output>
Output too large (33.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/9d9fdf13-f154-4750-b6ec-ad08e1a2475c/tool-results/bqb1igwro.txt

Preview (first 2KB):
001249-ishii-2025-01.yaml
schema_version: 2
id: 001249-ishii-2025-01
dataset:
  archive: dandi
  id: "001249"
  version: 0.241109.2357
  doi: 10.48324/dandi.001249/0.241109.2357
paper: doi:10.7554/elife.91765
date: '2026-11-01'
entry: 001249-ishii-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "fig6c-decay-length" -B2 -A50 attempts/001249-ishii-2025-01.yaml | head -80; echo ----; grep -n "id: fig6c-decay-length" -A50 claims/001249/10.7554-elife.91765.yaml | head -70
```

```
269-    cells for intromission and anogenital sniffing (p < 0.0001); mount cells are below sniff cells for
270-    sniff (0.459 against 2.504) and below ejaculation cells for ejaculation (-0.517 against 5.902).
271:- claim: fig6c-decay-length
272-  outcome: not_reproduced
273-  notebook: reproduce_ishii_2025.ipynb
274:  output: claim:fig6c-decay-length
275-  notes: Reading (a), time from onset to the first sample below 0, Vgat 18.7 s against Vglut2 22.2 s,
276-    t = -0.608, p = 0.544. Reading (b), total time below 0, Vgat 53.9 s against 75.3 s, t = -2.641, p
277-    = 0.0089 (Vgat shorter). The deposited decay lengths give t = 3.040, p = 0.00266, the paper's value.
278-    A variant not among the claims file's readings, the time from the peak after onset to the first sample
279-    below 0 (120 s when the signal never falls below 0), equals the deposited values for 207 of 219 cells
280-    (r = 1.000) and gives 45.2 against 20.9 s, t = 3.037, p = 0.0027. It reads the Results' "the time
281-    for the increased calcium signal to return to baseline" as starting from the peak. Whether it should
282-    be a reading is asked of a reader (questions/001249.yaml); the outcome is the claims file's. The authors
283-    are asked for the definition (finding).
284-  deviations:
285-  - Decay length computed from the deposited -5 to +120 s ejaculation traces under the claims file's readings;
286-    the deposited precomputed values and the from-the-peak variant are shown.
287-- claim: fig6k-late-cluster-vgat
288-  outcome: reproduced
[... 88 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001249-ishii-2025; grep -n "decay" mpoa.py | head -40; python -c "
import json;nb=json.load(open('reproduce_ishii_2025.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source'])
  if 'decay' in s.lower() or 'fig6c' in s: print('=== cell',i,c['cell_type'],c['metadata'].get('tags'));print(s)
"
```

```
15:- The decay-length readings are those of the claims file (fig6c-decay-length).
156:def decay_length(long_trace, reading):
158:    (-5 to 0 s) subtracted first (Methods). Readings of the claims file (fig6c-decay-length):
=== cell 0 markdown None
# Reproducing Ishii et al. (2025) from dandiset 001249 and the authors' Figshare deposit

Paper: Ishii, Cortese, Leng, Lee, Bayless, Bhattacharya, Muir, Stuber (2025), "Post-ejaculatory
inhibition of female sexual drive via heterogeneous neuronal ensembles in the medial preoptic
area", eLife 12, RP91765, doi:10.7554/elife.91765.

Dataset: DANDI:001249, version 0.241109.2357 (doi:10.48324/dandi.001249/0.241109.2357), 14 NWB
files of whole-brain light-sheet volumes, one per brain. The paper does not cite a version of the
dandiset; this is the only published version (the draft has the same 14 assets and was last
modified before it was published), so it is the version pinned (protocol, author step 1.3).

Outside data: The claims file marks every claim outside Figure 2 `data: elsewhere`: the paper
deposited those data on Figshare, doi:10.6084/m9.figshare.27642768.v1 (version 1), read here in
place. The MD5 of each zip read is printed below and must match `mpoa.FIGSHARE_FILES`.

Text: The claims file was written from the version of record (eLife RP91765, 5 March 2025),
[... 222 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001249-ishii-2025; sed -n 1,30p mpoa.py; sed -n 150,195p mpoa.py
```

```
"""Loading and measures for Ishii et al. (2025), eLife RP91765, on dandiset 001249.

The dandiset holds the whole-brain light-sheet volumes of Figure 2 (one NWB file per brain).
All other figures rest on the authors' Figshare deposit, doi:10.6084/m9.figshare.27642768.v1,
read here in place with range requests (docs/archives.md, Figshare). Nothing is written to disk.

Where each parameter comes from:
- Peri-event windows, the 0 to +5 s magnitude, the -5 to 0 s baseline and the responder
  threshold of 2 come from the Methods ("In vivo calcium imaging experiments and analysis", "z-scored signal was
  collected from -5 to +15 s around the behavior onset ... The magnitude of z-scored signal was
  quantified by averaging 0 to +5 s from onset. Cells that had larger than 2 d z-scored signal
  were classified as 'responding' cells"), as the claims file gives them.
- The 10 Hz rate and onset at index 50 of the deposited arrays are the code's parameter_dict
  (signal_framerate 10, before_frames 50), read from the deposit.
- The decay-length readings are those of the claims file (fig6c-decay-length).
- The clustering procedure is the claims file's (fig6k-late-cluster-vgat), taken from the
  Methods and "Figure 5 Spectral clustering.ipynb" at commit 4e98c43; the random seed is a
  standard choice.
"""
import io
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls executed/001249-ishii-2025/ 2>/dev/null; python -c "
import json;nb=json.load(open('executed/001249-ishii-2025/reproduce_ishii_2025.ipynb'))
c=nb['cells'][54]
for o in c['outputs']: print(o.get('text',''))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import json;nb=json.load(open('executed/001249-ishii-2025/reproduce_ishii_2025.ipynb'))
                             ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'executed/001249-ishii-2025/reproduce_ishii_2025.ipynb'
```

**Agent calls Bash**

```bash
cd entries/001249-ishii-2025; cat entry.yaml; python -c "
import json;nb=json.load(open('reproduce_ishii_2025.ipynb'))
for i,c in enumerate(nb['cells'][:54]):
  s=''.join(c['source'])
  if c['cell_type']=='code' and ('mag =' in s or 'vg =' in s or 'import' in s): print('=== cell',i);print(s[:1500])
"
```

```
schema_version: 1
name: 001249-ishii-2025
type: reproduction
title: Post-ejaculatory inhibition of female sexual drive in the MPOA (Ishii et al. 2025)
description: Tests the findings of Ishii et al. (2025) on dandiset 001249, which holds the
  whole-brain light-sheet volumes of 14 TRAP2;Ai14 females behind Figure 2, and on the authors'
  Figshare deposit, which holds the data of every other figure (self-paced mating behavior, HCR in
  situ, calcium imaging of Vgat and Vglut2 MPOA neurons, chemogenetics). The Figure 2 claims are
  blocked, as the dandiset holds only raw volumes and computing the cell densities would need the
  1.38 TB streamed, registered and segmented with a classifier that is not deposited.
license: Apache-2.0
notebooks:
- path: reproduce_ishii_2025.ipynb
  title: Reproducing Ishii et al. (2025) from dandiset 001249 and its Figshare deposit
  runtime_minutes: 3
helpers:
- mpoa.py
related:
- id: dandi:001249/0.241109.2357
  relation: uses_data
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001249-ishii-2025; time python -c "
import numpy as np, pandas as pd, mpoa
from scipy import stats
F4='Figure 3, 4, 5, S6, S7, S8'
ca=mpoa.read_csv(F4,'data/male_analysis_magnitude.csv')
longer=mpoa.read_npy(F4,'data/Ejaculation_longer_all_norm_zscore_snip_array.npy')
resp=mpoa.magnitude(longer)>2; vg=(ca.Mouse_line=='Vgat-Cre').values
x=longer-longer[:50].mean(0); post=x[50:]
pk=post.argmax(0)/10
c=mpoa.decay_length(longer,'c')
cens=np.array([not (post[int(round(p*10)):,i]<0).any() for i,p in enumerate(pk)])
print(post.shape, 'censored responders', (cens&resp).sum(), (cens&resp&vg).sum(), (cens&resp&~vg).sum())
c2=np.where(cens,120-pk,c)
c3=c-pk  # wrong; just check
for lab,d,m in [('c',c,resp),('c to end',c2,resp),('c excl',c,resp&~cens)]:
  a,b=d[m&vg],d[m&~vg]; r=stats.ttest_ind(a,b); print(lab,len(a),len(b),a.mean(),b.mean(),r)
print(pd.Series(c[resp]).groupby([ca.Mouse_line.values[resp],ca.ID.values[resp]]).agg(['size','mean']).round(1))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, pandas as pd, mpoa
ModuleNotFoundError: No module named 'numpy'

real	0m0.027s
user	0m0.020s
sys	0m0.007s
```

**Agent calls Bash**

```bash
cd  ls -a; ls ~/.venv* .venv* 2>/dev/null | head; grep -n "venv\|def cmd_run\|def run" tools/entry.py | head -20
```

```
.
..
.bash_profile
.bashrc
.claude
.env
.env.development
.env.development.local
.env.local
.env.production
.env.production.local
.env.test
.env.test.local
.git
.gitconfig
.github
.gitignore
.gitmodules
.idea
.mcp.json
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd  uv venv -q --python 3.12 $TMPDIR/dv && uv pip install -q --python $TMPDIR/dv/bin/python -r entries/001249-ishii-2025/requirements.lock.txt 2>&1 | tail -3; echo done
```

```
done
```

**Agent calls Bash**

```bash
cd entries/001249-ishii-2025; time $TMPDIR/dv/bin/python -c "
import numpy as np, pandas as pd, mpoa
from scipy import stats
F4='Figure 3, 4, 5, S6, S7, S8'
ca=mpoa.read_csv(F4,'data/male_analysis_magnitude.csv')
longer=mpoa.read_npy(F4,'data/Ejaculation_longer_all_norm_zscore_snip_array.npy')
resp=mpoa.magnitude(longer)>2; vg=(ca.Mouse_line=='Vgat-Cre').values
x=longer-longer[:50].mean(0); post=x[50:]
pk=post.argmax(0)
c=mpoa.decay_length(longer,'c')
cens=np.array([not (post[p:,i]<0).any() for i,p in enumerate(pk)])
print(post.shape, 'censored responders', (cens&resp).sum(), (cens&resp&vg).sum(), (cens&resp&~vg).sum())
d1=c-pk/10
c2=np.where(cens,(post.shape[0]-pk)/10,c)
for lab,d,m in [('c',c,resp),('c to end',c2,resp),('c excl',c,resp&~cens),('peak->below, minus peak',d1,resp)]:
  a,b=d[m&vg],d[m&~vg]; r=stats.ttest_ind(a,b); print(lab,len(a),len(b),a.mean(),b.mean(),r)
tab=ca.Ejaculation_decay_length_seconds.values
print('c vs table equal', (abs(c-tab)<0.051)[resp].sum(), 'c-pk vs table', (abs(d1-tab)<0.051)[resp].sum())
print(pd.Series(c[resp]).groupby([ca.Mouse_line.values[resp],ca.ID.values[resp]]).agg(['size','mean']).round(1))
"
```

```
(1200, 793) censored responders 44 43 1
c 184 35 45.19347826086957 20.914285714285718 TtestResult(statistic=np.float64(3.0370867687770122), pvalue=np.float64(0.002681357547888613), df=np.float64(217.0))
c to end 184 35 28.894565217391307 20.63714285714286 TtestResult(statistic=np.float64(1.6024282278510593), pvalue=np.float64(0.11051555532242133), df=np.float64(217.0))
c excl 141 34 22.380141843971632 18.0 TtestResult(statistic=np.float64(1.0423330228131569), pvalue=np.float64(0.2987117065053729), df=np.float64(173.0))
peak->below, minus peak 184 35 20.3125 16.054285714285715 TtestResult(statistic=np.float64(0.710632926411741), pvalue=np.float64(0.4780747925788317), df=np.float64(217.0))
c vs table equal 207 c-pk vs table 1
                     size  mean
Vgat-Cre   Vgat_1      23  57.7
           Vgat_2      54  82.3
           Vgat_3      17  20.6
           Vgat_4      55  17.7
           Vgat_5      12  29.2
           Vgat_6      23  38.0
Vglut2-Cre Vglut2_1     6  28.0
           Vglut2_2     9  17.7
           Vglut2_3    15  23.0
           Vglut2_4     5  12.0

real	0m7.178s
user	0m4.339s
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001249-ishii-2025; $TMPDIR/dv/bin/python -c "
import numpy as np, pandas as pd, mpoa
F4='Figure 3, 4, 5, S6, S7, S8'
ca=mpoa.read_csv(F4,'data/male_analysis_magnitude.csv')
longer=mpoa.read_npy(F4,'data/Ejaculation_longer_all_norm_zscore_snip_array.npy')
resp=mpoa.magnitude(longer)>2
x=longer-longer[:50].mean(0); post=x[50:]
pk=post.argmax(0)
c=mpoa.decay_length(longer,'c')
cens=np.array([not (post[p:,i]<0).any() for i,p in enumerate(pk)])
tab=ca.Ejaculation_decay_length_seconds.values
m=resp&cens
print('table on censored:', np.unique(tab[m],return_counts=True))
print('censored equal to table', (abs(c-tab)<0.051)[m].sum(), 'of', m.sum())
mm=resp&(abs(c-tab)>=0.051)
print('mismatches: c, table, peak, cens'); print(np.c_[c[mm],tab[mm],pk[mm]/10,cens[mm]])
"
```

```
table on censored: (array([120.]), array([44]))
censored equal to table 44 of 44
mismatches: c, table, peak, cens
[[12.1 12.6  0.   0. ]
 [18.5 19.5  0.7  0. ]
 [ 4.   8.9  4.3  0. ]
 [ 3.8  5.3  0.1  0. ]
 [ 9.5 14.   4.3  0. ]
 [ 6.2  6.9  0.3  0. ]
 [ 3.   3.6  0.1  0. ]
 [ 8.2 13.3  4.1  0. ]
 [ 8.6 10.2  0.3  0. ]
 [ 6.2  6.5  0.   0. ]
 [ 3.5  4.6  0.6  0. ]
 [ 6.6 11.8  4.6  0. ]]
```

**Agent calls Bash**

```bash
cd  grep -n "decay\|fig6c\|not_reproduced\|not reproduced\|^[a-z_]*:" attempts/001249-ishii-2025-01.yaml | head -60; grep -n "decay\|fig6c\|failure to reproduce" entries/001249-ishii-2025/README.md
```

```
1:schema_version: 2
2:id: 001249-ishii-2025-01
3:dataset:
8:paper: doi:10.7554/elife.91765
9:date: '2026-11-01'
10:entry: 001249-ishii-2025
11:provenance:
22:inputs:
32:outcomes:
271:- claim: fig6c-decay-length
272:  outcome: not_reproduced
274:  output: claim:fig6c-decay-length
277:    = 0.0089 (Vgat shorter). The deposited decay lengths give t = 3.040, p = 0.00266, the paper's value.
296:    peak at 48.5 s, longest decay under readings a and c) holds 37 of 184 Vgat and 0 of 35 Vglut2 cells,
363:findings:
399:  statement: The decay length of Figure 6C is defined in the Methods as "the time the z-scored signal
403:    than Vglut2. The question for the authors is whether the decay length is measured from the peak, and
15:| Figure 6C, Vgat ejaculation responders decay more slowly | Not reproduced |
20:A failure to reproduce here may be a failure of this attempt, not of the paper: see the
25:that is not deposited. The decay length of Figure 6C is not reproduced under the readings the
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 360,460p attempts/001249-ishii-2025-01.yaml; cat entries/001249-ishii-2025/README.md
```

```
receptive score 0.836 against 0.653 (p = 0.0200); sniffing p = 0.697 and mounting p = 0.400, the legend's
    values. In the self-paced assay no measure changes with CNO in either group (smallest Bonferroni p
    0.117 by rank-sum, 0.100 by signed-rank).
findings:
- kind: metadata_error
  statement: Each NWB file stores the z planes of a brain as the frames of an ImageSeries (acquisition/TRAP
    and acquisition/background) with starting_time rate 4.0, the z step in micrometres given as a sampling
    rate, resolution 3.6 and unit "lumen". No voxel size, orientation, channel wavelength or description
    is given; the descriptions are "no description".
- kind: data_missing
  statement: The dandiset holds only the raw volumes of Figure 2. The registration to the atlas, the cell
    segmentation, the per-region counts and densities, and the trained ilastik classifier are not in it,
    so none of the Figure 2 results can be computed without rerunning the whole pipeline, and the classifier,
    trained on manual labels, cannot be rebuilt as it was. The per-region densities are only on Figshare
    (tdTomato_summary.csv), with no link to the volumes.
- kind: other
  statement: The volumes are stored uncompressed and unchunked, 1.38 TB for 14 brains. At the 56 MB/s
    measured here, streaming the TRAP channels once takes about 3.4 h and both channels 6.8 h, which puts
    any analysis of Figure 2 out of reach of a streamed notebook.
- kind: other
[... 86 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001249-ishii-2025; $TMPDIR/dv/bin/python - <<'EOF'
p='mpoa.py'; s=open(p).read()
old=s[s.index('def decay_length('):s.index('def elbow_pcs(')]
new='''def decay_length(long_trace, reading, unreturned="window"):
    """Decay length in seconds of -5 to +120 s ejaculation traces (time x cells), baseline
    (-5 to 0 s) subtracted first (Methods). Readings of the claims file (fig6c-decay-length):
    'a' time from onset to the first sample below 0;
    'b' total time below 0 between 0 and +120 s;
    'c' time from the peak after onset (0 to +120 s) to the first sample below 0 after it, the
    Results' "time for the increased calcium signal to return to baseline" (added to the claims
    file on the reader's answer of 2026-11-01).
    A trace that never falls below 0 (after onset for 'a', after the peak for 'c') is not fixed by
    the paper. unreturned="window" gives it the full 120 s window, the value the deposited table
    (male_analysis_magnitude.csv, Ejaculation_decay_length_seconds) holds for every such cell, an
    assumption; "to_end" gives the time from the start of the measure to the end of the window
    (the shortest value it can have); "drop" gives NaN. Both are shown as variants."""
    x = long_trace - long_trace[:ONSET].mean(0)
    post = x[ONSET:]
    below = post < 0
    if reading == "b":
        return below.sum(0) / RATE_HZ
    if reading == "a":
        start = np.zeros(post.shape[1], dtype=int)
    elif reading == "c":
        start = post.argmax(0)
    else:
        raise ValueError(reading)
    out = np.empty(post.shape[1])
    for i in range(post.shape[1]):
        after = np.where(below[start[i]:, i])[0]
        if len(after):
            out[i] = after[0]
        elif unreturned == "window":
            out[i] = post.shape[0]
        elif unreturned == "to_end":
            out[i] = post.shape[0] - start[i]
        elif unreturned == "drop":
            out[i] = np.nan
        else:
            raise ValueError(unreturned)
    return out / RATE_HZ


'''
s=s.replace(old,new)
s=s.replace("- The decay-length readings are those of the claims file (fig6c-decay-length).",
"- The decay-length readings are those of the claims file (fig6c-decay-length). The value given\n  to a trace that never returns below 0 (120 s) is an assumption, taken from the deposited table\n  (see decay_length).")
open(p,'w').write(s)
EOF
$TMPDIR/dv/bin/python -c "
import numpy as np, mpoa
F4='Figure 3, 4, 5, S6, S7, S8'
longer=mpoa.read_npy(F4,'data/Ejaculation_longer_all_norm_zscore_snip_array.npy')
for r in 'abc':
  for u in ['window','to_end','drop']: d=mpoa.decay_length(longer,r,u); print(r,u,np.nanmean(d),np.isnan(d).sum())
"
```

```
a window 6.366204287515764 0
a to_end 6.366204287515764 0
a drop 4.472307692307692 13
b window 63.80491803278688 0
b to_end 63.80491803278688 0
b drop 63.80491803278688 0
c window 28.308322824716267 0
c to_end 16.408448928121057 0
c drop 11.637108792846497 122
```

**Agent calls Bash**

```bash
cd entries/001249-ishii-2025; $TMPDIR/dv/bin/python - <<'EOF'
import json
p='reproduce_ishii_2025.ipynb'; nb=json.load(open(p))
def setsrc(i,s):
    nb['cells'][i]['source']=s.strip('\n').splitlines(keepends=True)
assert 'fig6c' in ''.join(nb['cells'][53]['source'])
setsrc(53,'''
### fig6c-decay-length

> Ejaculation-responding Vgat cells have a longer decay length than Vglut2 cells.

The -5 to +120 s trace, baseline (-5 to 0 s) subtracted. Readings of the claims file: (a) time
from onset to the first sample below 0, (b) total time below 0 in 0 to 120 s, and (c) time from
the peak after onset to the first sample below 0 after it. Reading (c) was added to the claims
file on a reader's answer (questions/001249.yaml, 2026-11-01), after the first run of this
attempt tested (a) and (b) and showed (c) as a variant. Student's t-test; reproduced when Vgat is
longer at p < 0.05 under a reading.

The paper does not say what value a trace that never falls below 0 takes. The main analysis gives
it the full 120 s window, the value the deposited table holds for every such cell (an
assumption). Two variants are shown: the time from the start of the measure to the end of the
window (the least it can be), and leaving such cells out. The table's precomputed decay length,
whose computation is not in the code, is shown too.
''')
setsrc(54,'''
resp = (mag.Ejaculation > 2).values
tabd_all = ca.Ejaculation_decay_length_seconds.values
rows = []
for lab, dl in [("(a) onset to first sample below 0", mpoa.decay_length(longer, "a")),
                ("(b) total time below 0", mpoa.decay_length(longer, "b")),
                ("(c) peak to first sample below 0", mpoa.decay_length(longer, "c")),
                ("(c) unreturned = peak to end of window", mpoa.decay_length(longer, "c", "to_end")),
                ("(c) unreturned left out", mpoa.decay_length(longer, "c", "drop")),
                ("(a) unreturned left out", mpoa.decay_length(longer, "a", "drop")),
                ("table column", tabd_all)]:
    x, y = dl[resp & vg], dl[resp & ~vg]
    x, y = x[~np.isnan(x)], y[~np.isnan(y)]
    r = stats.ttest_ind(x, y)
    rows.append(dict(reading=lab, n_vgat=len(x), n_vglut2=len(y), vgat_mean=np.mean(x), vglut2_mean=np.mean(y),
                     vgat_median=np.median(x), vglut2_median=np.median(y), diff=np.mean(x) - np.mean(y),
                     t=r.statistic, p=r.pvalue, at_120s=int((x >= 120).sum() + (y >= 120).sum()),
                     u_p=stats.mannwhitneyu(x, y).pvalue))
dc = pd.DataFrame(rows)
print(dc.to_string(index=False, float_format=lambda x: f"{x:.4g}"))
dlc = mpoa.decay_length(longer, "c")
unret_c = np.isnan(mpoa.decay_length(longer, "c", "drop"))
print("responders whose trace never falls below 0 after the peak: Vgat", int((resp & vg & unret_c).sum()),
      "of", int((resp & vg).sum()), "| Vglut2", int((resp & ~vg & unret_c).sum()), "of", int((resp & ~vg).sum()),
      "| table value for them:", sorted(set(tabd_all[resp & unret_c])))
tabd = tabd_all[resp]
for lab in "abc":
    dl = mpoa.decay_length(longer, lab)[resp]
    print(f"reading ({lab}) against the table column: r = {np.corrcoef(dl, tabd)[0, 1]:.3f}, equal (within 0.05 s) in "
          f"{int((abs(dl - tabd) < 0.051).sum())} of {int(resp.sum())} responders")
pk = longer[ONSET_IDX:].argmax(0)[resp] / 10 if False else None
by = (pd.DataFrame({"line": ca.Mouse_line.values, "ID": ca.ID.values, "c": dlc, "a": mpoa.decay_length(longer, "a")})[resp]
      .groupby(["line", "ID"]).agg(n=("c", "size"), mean_c=("c", "mean"), mean_a=("a", "mean")))
print("by animal (responders):"); print(by.round(1).to_string())
am = by.mean_c
ra = stats.ttest_ind(am[am.index.get_level_values(0) == "Vgat-Cre"], am[am.index.get_level_values(0) == "Vglut2-Cre"])
print(f"reading (c), animal means as units: Vgat {am['Vgat-Cre'].mean():.1f} s (6 mice) against Vglut2 "
      f"{am['Vglut2-Cre'].mean():.1f} s (4 mice), t = {ra.statistic:.3f}, p = {ra.pvalue:.3g}")
''')
s=''.join(nb['cells'][54]['source']).replace('pk = longer[ONSET_IDX:].argmax(0)[resp] / 10 if False else None\n','')
nb['cells'][54]['source']=s.splitlines(keepends=True)
nb['cells'][54]['outputs']=[]; nb['cells'][54]['execution_count']=None
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat
```

```
entries/001249-ishii-2025/mpoa.py                  | 50 ++++++++++++++--------
 .../001249-ishii-2025/reproduce_ishii_2025.ipynb   | 49 +++++++++++++++------
 2 files changed, 68 insertions(+), 31 deletions(-)
```

**Agent calls Bash**

```bash
cd entries/001249-ishii-2025; $TMPDIR/dv/bin/python - <<'EOF'
import json
nb=json.load(open('reproduce_ishii_2025.ipynb'))
pre='''
import numpy as np, pandas as pd, mpoa
from scipy import stats
F4='Figure 3, 4, 5, S6, S7, S8'
ca=mpoa.read_csv(F4,'data/male_analysis_magnitude.csv')
longer=mpoa.read_npy(F4,'data/Ejaculation_longer_all_norm_zscore_snip_array.npy')
mag=pd.DataFrame({'Ejaculation':mpoa.magnitude(longer)}); vg=(ca.Mouse_line=='Vgat-Cre').values
'''
exec(pre+''.join(nb['cells'][54]['source']))
EOF
```

```
reading  n_vgat  n_vglut2  vgat_mean  vglut2_mean  vgat_median  vglut2_median   diff       t        p  at_120s       u_p
     (a) onset to first sample below 0     184        35      18.67        22.21         5.15           22.1 -3.543 -0.6077    0.544       12  0.002783
                (b) total time below 0     184        35      53.89        75.29        49.15           89.6 -21.39  -2.641 0.008863        0   0.04323
      (c) peak to first sample below 0     184        35      45.19        20.91        19.55           18.9  24.28   3.037 0.002681       44    0.1866
(c) unreturned = peak to end of window     184        35      28.89        20.64        17.05           18.9  8.257   1.602   0.1105        0     0.817
               (c) unreturned left out     141        34      22.38           18         13.3          18.65   4.38   1.042   0.2987        0    0.4339
               (a) unreturned left out     173        34      12.22        19.33          4.1          20.95  -7.11  -1.841   0.0671        0 0.0004044
                          table column     184        35      45.31        21.06        19.55           18.9  24.25    3.04  0.00266       44    0.1851
responders whose trace never falls below 0 after the peak: Vgat 43 of 184 | Vglut2 1 of 35 | table value for them: [np.float64(120.0)]
reading (a) against the table column: r = 0.333, equal (within 0.05 s) in 14 of 219 responders
reading (b) against the table column: r = -0.814, equal (within 0.05 s) in 0 of 219 responders
reading (c) against the table column: r = 1.000, equal (within 0.05 s) in 207 of 219 responders
by animal (responders):
                      n  mean_c  mean_a
line       ID                          
Vgat-Cre   Vgat_1    23    57.7     4.3
           Vgat_2    54    82.3    34.0
           Vgat_3    17    20.6     7.7
           Vgat_4    55    17.7    19.0
           Vgat_5    12    29.2    18.6
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001249-ishii-2025; $TMPDIR/dv/bin/python - <<'EOF'
import json
p='reproduce_ishii_2025.ipynb'; nb=json.load(open(p))
s=''.join(nb['cells'][54]['source'])
s=s.replace('''"a": mpoa.decay_length(longer, "a")})[resp]
      .groupby(["line", "ID"]).agg(n=("c", "size"), mean_c=("c", "mean"), mean_a=("a", "mean")))''',
'''"a": mpoa.decay_length(longer, "a"),
                    "unreturned": unret_c})[resp]
      .groupby(["line", "ID"]).agg(n=("c", "size"), unreturned_c=("unreturned", "sum"), mean_c=("c", "mean"),
                                   mean_a=("a", "mean")))''')
nb['cells'][54]['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
$TMPDIR/dv/bin/python - <<'EOF' 2>&1 | tail -14
import json,os
os.chdir('entries/001249-ishii-2025')
nb=json.load(open('reproduce_ishii_2025.ipynb'))
pre='''
import numpy as np, pandas as pd, mpoa
from scipy import stats
F4='Figure 3, 4, 5, S6, S7, S8'
ca=mpoa.read_csv(F4,'data/male_analysis_magnitude.csv')
longer=mpoa.read_npy(F4,'data/Ejaculation_longer_all_norm_zscore_snip_array.npy')
mag=pd.DataFrame({'Ejaculation':mpoa.magnitude(longer)}); vg=(ca.Mouse_line=='Vgat-Cre').values
'''
exec(pre+''.join(nb['cells'][54]['source']))
EOF
```

```
by animal (responders):
                      n  unreturned_c  mean_c  mean_a
line       ID                                        
Vgat-Cre   Vgat_1    23             7    57.7     4.3
           Vgat_2    54            31    82.3    34.0
           Vgat_3    17             2    20.6     7.7
           Vgat_4    55             1    17.7    19.0
           Vgat_5    12             1    29.2    18.6
           Vgat_6    23             1    38.0     4.2
Vglut2-Cre Vglut2_1   6             0    28.0    36.4
           Vglut2_2   9             0    17.7    21.2
           Vglut2_3  15             1    23.0    24.5
           Vglut2_4   5             0    12.0     0.1
reading (c), animal means as units: Vgat 40.9 s (6 mice) against Vglut2 20.2 s (4 mice), t = 1.598, p = 0.149
```

**Agent calls Bash**

```bash
cd entries/001249-ishii-2025; $TMPDIR/dv/bin/python - <<'EOF'
import json
p='reproduce_ishii_2025.ipynb'; nb=json.load(open(p))
nb['cells'][55]['source']=["**Result: reproduced, resting on an assumption.** Under reading (c), added to the claims file on a reader's answer, Vgat responders take longer from the peak to fall below 0: 45.2 against 20.9 s, t = 3.037, p = 0.0027, close to the paper's t(217) = 3.040, p = 0.00266, and (c) equals the deposited decay lengths for 207 of 219 cells (r = 1.000). This rests on giving the 44 cells that never fall below 0 after the peak (43 Vgat, 1 Vglut2, 31 of them in mouse Vgat_2) the full 120 s, as the deposited table does for all 44. Counting them as the time from the peak to the end of the window gives 28.9 against 20.6 s (p = 0.111), and leaving them out gives 22.4 against 18.0 s (p = 0.299); the rank-sum test under (c) gives p = 0.187, and the animal means give 40.9 against 20.2 s (6 and 4 mice, p = 0.149). Under readings (a) and (b) Vgat cells do not decay later: (a) 18.7 against 22.2 s (t = -0.608, p = 0.544), (b) 53.9 against 75.3 s (t = -2.641, p = 0.0089, Vgat shorter)."]
s=''.join(nb['cells'][78]['source'])
old="| fig6c-decay-length | Figshare | not reproduced (a reading from the peak, asked of a reader, reproduces it) |"
assert old in s
s=s.replace(old,"| fig6c-decay-length | Figshare | reproduced under reading (c), from the peak, added on a reader's answer; rests on giving cells that never return below 0 the full 120 s |")
s=s.replace("The deposited decay lengths follow a definition the Methods do not give,","The deposited decay lengths follow a definition the Methods do not give (from the peak, with 120 s for a trace that never returns below 0),")
nb['cells'][78]['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff reproduce_ishii_2025.ipynb | tail -30
```

```
]
   },
   {
@@ -1123,7 +1146,7 @@
    "id": "e32dd212",
    "metadata": {},
    "source": [
-    "**Result: not reproduced.** Under the claims file's readings Vgat cells do not have the longer decay: (a) time to the first sample below 0 is 18.7 s in Vgat and 22.2 s in Vglut2 (t = -0.608, p = 0.544), and (b) total time below 0 is shorter in Vgat (53.9 against 75.3 s, t = -2.641, p = 0.0089). The variant (c), from the peak to the first sample below 0, equals the deposited decay lengths for 207 of 219 cells (r = 1.000) and gives the paper's result: 45.2 against 20.9 s, t = 3.037, p = 0.0027 (deposited column t = 3.040, p = 0.00266). Whether (c) is a reading of the paper is asked of a reader."
+    "**Result: reproduced, resting on an assumption.** Under reading (c), added to the claims file on a reader's answer, Vgat responders take longer from the peak to fall below 0: 45.2 against 20.9 s, t = 3.037, p = 0.0027, close to the paper's t(217) = 3.040, p = 0.00266, and (c) equals the deposited decay lengths for 207 of 219 cells (r = 1.000). This rests on giving the 44 cells that never fall below 0 after the peak (43 Vgat, 1 Vglut2, 31 of them in mouse Vgat_2) the full 120 s, as the deposited table does for all 44. Counting them as the time from the peak to the end of the window gives 28.9 against 20.6 s (p = 0.111), and leaving them out gives 22.4 against 18.0 s (p = 0.299); the rank-sum test under (c) gives p = 0.187, and the animal means give 40.9 against 20.2 s (6 and 4 mice, p = 0.149). Under readings (a) and (b) Vgat cells do not decay later: (a) 18.7 against 22.2 s (t = -0.608, p = 0.544), (b) 53.9 against 75.3 s (t = -2.641, p = 0.0089, Vgat shorter)."
    ]
   },
   {
@@ -1630,7 +1653,7 @@
     "| fig4i-ejaculation-responders | Figshare | reproduced |\n",
     "| fig5-ejaculation-specific | Figshare | reproduced |\n",
     "| fig5c-class-selectivity | Figshare | reproduced |\n",
-    "| fig6c-decay-length | Figshare | not reproduced (a reading from the peak, aske
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  $TMPDIR/dv/bin/python - <<'EOF'
p='entries/001249-ishii-2025/README.md'; s=open(p).read()
s=s.replace("| Figure 6C, Vgat ejaculation responders decay more slowly | Not reproduced |","| Figure 6C, Vgat ejaculation responders decay more slowly | Reproduced, resting on an assumption |")
old="""The decay length of Figure 6C is not reproduced under the readings the
claims file gives, and is reproduced by a reading from the peak that matches the deposited values;
a reader is asked about it."""
assert old in s
s=s.replace(old,"""The decay length of Figure 6C is reproduced
under the reading from the peak that a reader added to the claims file, which matches the deposited
values, provided cells that never return below 0 count as 120 s, as the deposited table has them;
the readings from onset do not reproduce it.""")
open(p,'w').write(s)
p='attempts/001249-ishii-2025-01.yaml'; s=open(p).read()
i=s.index("- claim: fig6c-decay-length"); j=s.index("- claim: fig6k-late-cluster-vgat")
new='''- claim: fig6c-decay-length
  outcome: reproduced
  assumed: true
  notebook: reproduce_ishii_2025.ipynb
  output: claim:fig6c-decay-length
  notes: Re-run on the reader's answer of 2026-11-01 (questions/001249.yaml), which added reading (c),
    the time from the peak after onset to the first sample below 0 after it, to the criterion; the first
    run of this attempt, on readings (a) and (b) only, gave not_reproduced. Under (c) Vgat responders
    take 45.2 s against 20.9 s in Vglut2, t = 3.037, p = 0.0027 (paper t(217) = 3.040, p = 0.00266), and
    (c) equals the deposited decay lengths for 207 of 219 cells (r = 1.000). The result rests on giving
    the 44 cells that never fall below 0 after the peak (43 Vgat, 1 Vglut2; 31 in mouse Vgat_2) the full
    120 s, as the deposited table does for all 44. Counting them as the time from the peak to the end of
    the window gives 28.9 against 20.6 s (p = 0.111); leaving them out gives 22.4 against 18.0 s (p =
    0.299). Under (c) the rank-sum test gives p = 0.187 and the animal means 40.9 against 20.2 s (6 and
    4 mice, p = 0.149). Reading (a), onset to the first sample below 0, gives 18.7 against 22.2 s, t =
    -0.608, p = 0.544, and reading (b), total time below 0, 53.9 against 75.3 s, t = -2.641, p = 0.0089
    (Vgat shorter). The authors are asked how the decay length is defined (finding).
  deviations:
  - Decay length computed from the deposited -5 to +120 s ejaculation traces under the claims file's three
    readings; the deposited precomputed values are shown as well.
  - Assumed, the paper not saying it, that a trace that never falls below 0 after the peak has a decay
    length of 120 s, the full window, because the deposited table (male_analysis_magnitude.csv, Ejaculation_decay_length_seconds)
    holds 120 for each of the 44 such cells. The outcome depends on it; the time to the end of the window
    and leaving the cells out are shown and give p = 0.111 and 0.299.
'''
s=s[:i]+new+s[j:]
old='''The question for the authors is whether the decay length is measured from the peak, and
    how the other 12 cells are computed.'''
assert old in s
s=s.replace(old,'''The deposited table gives 120 s to each of the 44 responders whose trace
    never falls below 0 after the peak; with the time to the end of the window, or with these cells left
    out, Vgat is not longer at p < 0.05. The questions for the authors are whether the decay length is
    measured from the peak, what value a trace that never returns below 0 takes and why, and how the
    other 12 cells are computed.''')
open(p,'w').write(s)
EOF
grep -n "fig6c\|question\|answer" attempts/001249-ishii-2025-01.yaml | head
```

```
271:- claim: fig6c-decay-length
275:  output: claim:fig6c-decay-length
276:  notes: Re-run on the reader's answer of 2026-11-01 (questions/001249.yaml), which added reading (c),
413:    out, Vgat is not longer at p < 0.05. The questions for the authors are whether the decay length is
```

**Agent calls Bash**

```bash
cd  sed -n 271,300p attempts/001249-ishii-2025-01.yaml | grep -n ".: .*: "; grep -n "answer" schemas/*attempt* | head; date -u
```

```
Sun Nov  1 12:04:43 UTC 2026
```

**Agent calls Bash**

```bash
cd  python tools/entry.py lock entries/001249-ishii-2025 2>&1 | tail -5 && time python tools/entry.py all entries/001249-ishii-2025 2>&1 | tail -20
```

```
wrote entries/001249-ishii-2025/requirements.lock.txt
Installed kernelspec registry-001249-ishii-2025 in executed/001249-ishii-2025/.venv/share/jupyter/kernels/registry-001249-ishii-2025
0 error(s)
pass  reproduce_ishii_2025.ipynb  (90 s)

real	1m41.386s
user	0m40.122s
sys	0m3.813s
```

**Agent calls Bash**

```bash
cd  git status --short; python -c "
import json;nb=json.load(open('executed/001249-ishii-2025/reproduce_ishii_2025.ipynb'))
for i in (54,57):
  for o in nb['cells'][i]['outputs']: print(o.get('text','')[:3000] if i==54 else ''.join(o.get('text',''))[:600])
"
```

```
M attempts/001249-ishii-2025-01.yaml
 M entries/001249-ishii-2025/README.md
 M entries/001249-ishii-2025/mpoa.py
 M entries/001249-ishii-2025/reproduce_ishii_2025.ipynb
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
['                               reading  n_vgat  n_vglut2  vgat_mean  vglut2_mean  vgat_median  vglut2_median   diff       t        p  at_120s       u_p\n', '     (a) onset to first sample below 0     184        35      18.67        22.21         5.15           22.1 -3.543 -0.6077    0.544       12  0.002783\n', '                (b) total time below 0     184        35      53.89        75.29        49.15           89.6 -21.39  -2.641 0.008863        0   0.04323\n', '      (c) peak to first sample below 0     184        35      45.19        20.91        19.55           18.9  24.28   3.037 0.002681       44    0.1866\n', '(c) unreturned = peak to end of window     184        35      28.89        20.64        17.05           18.9  8.257   1.602   0.1105        0     0.817\n', '               (c) unreturned left out     141        34      22.38           18         13.3          18.65   4.38   1.042   0.2987        0    0.4339\n', '               (a) unreturned left out     173        34      12.22        19.33          4.1          20.95  -7.11  -1.841   0.0671        0 0.0004044\n', '                          table column     184        35      45.31        21.06        19.55           18.9  24.25    3.04  0.00266       44    0.1851\n', 'responders whose trace never falls below 0 after the peak: Vgat 43 of 184 | Vglut2 1 of 35 | table value for them: [np.float64(120.0)]\n', 'reading (a) against the table column: r = 0.333, equal (within 0.05 s) in 14 of 219 responders\n', 'reading (b) against the table column: r = -0.814, equal (within 0.05 s) in 0 of 219 responders\n', 'reading (c) against the table column: r = 1.000, equal (within 0.05 s) in 207 of 219 responders\n'
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/entry.py handover entries/001249-ishii-2025 2>&1 | tail -5; python tools/entry.py check entries/001249-ishii-2025 2>&1 | tail -3
```

```
wrote executed/001249-ishii-2025/handover
0 error(s)
```

**Agent**

There was one answered question, on fig6c-decay-length. Claim fig6c-decay-length changes from **not_reproduced** to **reproduced**, marked `assumed: true`, but the result depends on how cells that never return to baseline are counted.

**The question.** I asked whether the decay length could be read as the time from the peak of the response to the first sample below 0. The claims file only allowed (a) the time from onset to the first sample below 0 and (b) the total time below 0.

**What the answer changed.** The reader agreed and added reading (c) to the criterion: the time from the peak after onset (0 to 120 s) to the first sample below 0 after it. The criterion now says the claim is reproduced when Vgat is longer at p < 0.05 under any one reading. The statement, expected values and statistics did not change.

**Outcome for fig6c-decay-length**

| Reading | Vgat vs Vglut2 (s) | t, p | Earlier |
|---|---|---|---|
| (a) onset to first sample below 0 | 18.7 vs 22.2 | -0.608, 0.544 | same, decided not_reproduced |
| (b) total time below 0 | 53.9 vs 75.3 (Vgat shorter) | -2.641, 0.0089 | same |
| (c) peak to first sample below 0 (new) | 45.2 vs 20.9 | 3.037, 0.0027 | shown only as a variant before |

The paper reports t(217) = 3.040, p = 0.00266. Reading (c) gives the same value as the deposited per-cell decay lengths for 207 of 219 cells.

**Why it is marked assumed.** 44 cells never fall below 0 after the peak: 43 Vgat and 1 Vglut2, and 31 of them come from one mouse, Vgat_2. The paper does not say what value they get. I gave them the full 120 s, because the deposited table has 120 for all 44. Under other choices the effect is not significant:

| Variant | Vgat vs Vglut2 (s) | p |
|---|---|---|
| unreturned cells counted to the end of the window | 28.9 vs 20.6 | 0.111 |
| unreturned cells left out | 22.4 vs 18.0 | 0.299 |
| rank-sum test under (c) | | 0.187 |
| per-animal means (6 and 4 mice) | 40.9 vs 20.2 | 0.149 |

I added this to the claim's notes and deviations, and to the existing finding that asks the authors how decay length is defined. It now also asks what value a trace that never returns below 0 gets.

**Files changed**
- `mpoa.py`: `decay_length` treats (c) as one of the claims file's readings, and takes an option for how unreturned cells are counted (120 s, to the end of the window, or left out).
- The notebook's fig6c section, its Result cell and the summary table.
- `README.md`.
- `attempts/001249-ishii-2025-01.yaml`: the outcome, notes, deviations and the finding.

No other claim changed. fig6k-late-cluster-vgat already used reading (c) with 120 s, and its re-run numbers are the same as before. fig7fg-activation-suppresses is still partially reproduced, so the "failure to reproduce" sentence stays in the README and the notebook summary.

**Entry runs.** Lock, check and run all passed with 0 errors; the notebook ran in 90 s. I checked that the executed notebook prints the numbers the conclusions quote. The handover is in `executed/001249-ishii-2025/handover`. I did not verify my own work, and nothing is committed or pushed.

## End of run

27 turns, 5 minutes, result: success.
