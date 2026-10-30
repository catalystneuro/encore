# 000469 · verifier-1 · run 41065746366

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 188
drwxr-xr-x 6 runner runner    4096 Oct 30 13:56 .
drwxr-xr-x 7 runner runner    4096 Oct 30 13:56 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 13:44 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 13:44 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 30 13:56 .claude
-rw-r--r-- 1 runner runner       0 Oct 30 13:56 .env
-rw-r--r-- 1 runner runner       0 Oct 30 13:56 .env.development
-rw-r--r-- 1 runner runner       0 Oct 30 13:56 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 30 13:56 .env.local
-rw-r--r-- 1 runner runner       0 Oct 30 13:56 .env.production
-rw-r--r-- 1 runner runner       0 Oct 30 13:56 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 30 13:56 .env.test
-rw-r--r-- 1 runner runner       0 Oct 30 13:56 .env.test.local
drwx------ 2 runner runner    4096 Oct 30 13:56 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 13:44 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 13:44 .github
-rw-r--r-- 1 runner runner       0 Oct 30 13:56 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 13:44 .idea
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1038-s41597-024-02943-8.yaml
```

```
# Claims for Kyzar, Kaminski, Brzezicka, Reed, Chung, Mamelak & Rutishauser (2024), Sci Data 11, 89,
# on dandiset 000469.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23, protocol
# as stated in docs/protocol.md.
#
# Text read: the version of record, as served by Europe PMC (PMC10796636), full text with Methods,
# Technical Validation, figure legends and Tables 1 to 3. The paper is a data descriptor and has
# no supplement. Its Methods are said to be abbreviated from refs 15 and 20 (Kaminski et al. 2017,
# Nat Neurosci; Kaminski et al. 2020, Neuron); those papers were not used here, as the protocol
# takes methods from this paper and the code it links.
#
# Code read: github.com/rutishauserlab/workingmem-release-NWB, branch main at commit f8594e0
# (2024-01-22). Its code is identical to tag v1.0.0 (commit 4a98f46, 2023-07-18); only README.md
# and CITATION.cff differ. A commit of 2024-01-12 (7d7b00f) that rewrote the selectivity code
# for another dataset was reverted the same day (3098793) and is not used. The repository holds
# MATLAB scripts. NWB_SB_import_main.m runs the analysis; NWB_calcSelective_SB.m and
# NWB_calcSelective_SC.m classify concept, maintenance and probe cells; NWB_QA_graphs.m computes
# the behaviour and the spike sorting metrics of Figs 1c,d and 3; NWB_SB_plotCell_Sternberg.m and
# NWB_SB_plotCell_Screening.m list the example units of Figs 4 and 5.
# Where the code and the Methods disagree, the Methods give the main criterion and the code's
[... 480 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat sternberg.py
```

```
"""Loading and measures for dandiset 000469 (human single neurons, screening and Sternberg tasks).

Kyzar, Kaminski, Brzezicka, Reed, Chung, Mamelak & Rutishauser (2024), Sci Data 11, 89,
doi:10.1038/s41597-024-02943-8. Its code is github.com/rutishauserlab/workingmem-release-NWB at
commit f8594e0 (MATLAB, read, not run); "the code" below means that commit.

Each subject has a screening file (ses-1) and a Sternberg file (ses-2). Only the small arrays
are read (spike times, unit and electrode tables, trials, stimulus presentation, TTL events);
the spike waveforms, which make most of each file, are not. Files are streamed from the archive
at the pinned version; nothing is written to disk.

Where the parameters come from:

- Areas: the electrode `location`, left and right merged, as translateArea_SB.m (condenseFlag 1)
  and NWB_countAreas.m do (claims sternberg-unit-yield). MTL is amygdala and hippocampus, MFC is
  dACC, pre-SMA and vmPFC, as the code's summary in NWB_SB_import_main.m groups them.
- Quality metrics (claims isi-violations to isolation-distance): as NWB_QA_graphs.m computes
  them. ISI violations, consecutive spike time differences below 3 ms over the whole file; rate,
  spikes over the time from first to last spike; CV2 by calcCV2.m with ignoreMode 1 (pairs with
  an ISI over 1 s left out).
[... 504 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_kyzar_2024.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f'===== CELL {i} [{c[\"cell_type\"]}] =====')
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--- out:'); print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--- out:'); print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('--- ERROR', o.get('ename'), o.get('evalue'))
"
```

```
<persisted-output>
Output too large (48.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/6227d9dc-854d-40bb-8b37-a00932c7837a/tool-results/b88k6q9fv.txt

Preview (first 2KB):
===== CELL 0 [markdown] =====
# Reproducing Kyzar et al. (2024) from dandiset 000469

Paper: Kyzar, Kamiński, Brzezicka, Reed, Chung, Mamelak & Rutishauser (2024), "Dataset of
human-single neuron activity during a Sternberg working memory task", Sci Data 11, 89,
doi:10.1038/s41597-024-02943-8.

Dataset: [DANDI:000469](https://dandiarchive.org/dandiset/000469/0.240123.1806), version
0.240123.1806 (doi:10.48324/dandi.000469/0.240123.1806). The paper cites the dandiset without a
version (ref. 46, "Kyzar M, 2023, DANDI Archive"), so the most recent published version is
pinned. The four published versions (0.231213.2047, 0.240122.1800, 0.240122.1812, 0.240123.1806)
and the draft list the same 41 assets with the same asset identifiers and sizes, so the choice
does not change the data read; the cell below checks this against the archive.

Text the claims file was written from: the version of record (Europe PMC, PMC10796636), with
Methods, Technical Validation, legends and Tables 1 to 3; the paper has no supplement. The
[... 29 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/6227d9dc-854d-40bb-8b37-a00932c7837a/tool-results/b88k6q9fv.txt"
}
```

```
1	===== CELL 0 [markdown] =====
2	# Reproducing Kyzar et al. (2024) from dandiset 000469
3	
4	Paper: Kyzar, Kamiński, Brzezicka, Reed, Chung, Mamelak & Rutishauser (2024), "Dataset of
5	human-single neuron activity during a Sternberg working memory task", Sci Data 11, 89,
6	doi:10.1038/s41597-024-02943-8.
7	
8	Dataset: [DANDI:000469](https://dandiarchive.org/dandiset/000469/0.240123.1806), version
9	0.240123.1806 (doi:10.48324/dandi.000469/0.240123.1806). The paper cites the dandiset without a
10	version (ref. 46, "Kyzar M, 2023, DANDI Archive"), so the most recent published version is
11	pinned. The four published versions (0.231213.2047, 0.240122.1800, 0.240122.1812, 0.240123.1806)
12	and the draft list the same 41 assets with the same asset identifiers and sizes, so the choice
13	does not change the data read; the cell below checks this against the archive.
14	
15	Text the claims file was written from: the version of record (Europe PMC, PMC10796636), with
16	Methods, Technical Validation, legends and Tables 1 to 3; the paper has no supplement. The
17	claims file also read the paper's code, github.com/rutishauserlab/workingmem-release-NWB at
18	commit f8594e0. Where a method detail below is taken from that code, the helper module
19	`sternberg.py` cites the file.
20	
[... 778 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_kyzar_2024.ipynb'))
c=nb['cells'][5]
for o in c['outputs']:
    t=''.join(o.get('text',''))
    i=t.find('trials with maintenance'); print(t[i:i+5000])
print(len(nb['cells']))
"; grep -n -i -E "chance|permut|concept cell|maintenance cell|probe cell|baseline" paper/10.1038-s41597-024-02943-8.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i -o -E ".{0,300}(chance|permut|concept cells? |maintenance cells|probe cells).{0,300}" paper/10.1038-s41597-024-02943-8.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/t.py <<'EOF'
import sys; sys.path.insert(0,'.')
import numpy as np, pandas as pd
from scipy import stats
import sternberg as sb
rng=np.random.default_rng(0)
# window_rates strict bounds
ts=np.array([0.2,0.5,1.0,1.1,2.2,2.9])
print("wr", sb.window_rates(ts,np.array([0.,2.]),(0.2,1.0)))  # expect [1/0.8 (0.5 only), 2/0.8 (2.2? 2.2 > 2.2 no ->2.9? no) ]
# anova_f vs scipy
y=rng.normal(size=60); lab=np.repeat(np.arange(5),12); y[lab==2]+=1
print("F", sb.anova_f(y,lab), stats.f_oneway(*[y[lab==g] for g in range(5)]).statistic)
perms=sb.perm_matrix(60,rng)
print("permanova", sb.perm_anova(y,lab,perms), stats.f_oneway(*[y[lab==g] for g in range(5)]).pvalue)
# perm anova false positive rate under null
fp=0
for i in range(300):
    y=rng.poisson(0.5,size=60).astype(float)
    fp+= sb.perm_anova(y,lab,sb.perm_matrix(60,rng,500))[1]<0.05
print("permanova FPR", fp/300)
# perm_ttest vs scipy
a=rng.normal(1,1,30); b=rng.normal(0,1,40)
print("pt", sb.perm_ttest(a,b,None,rng), stats.ttest_ind(a,b).pvalue, stats.ttest_ind(a,b,alternative='greater').pvalue)
# null FPR for sparse Poisson data: shuffle and flip, maint (2.5 s) vs fix (0.5 s)
for lam in (0.2,0.5,1,3):
    fs=ff=0; N=400
    for i in range(N):
        m=rng.poisson(lam*2.5,108)/2.5; f=rng.poisson(lam*0.5,108)/0.5
        fs+= sb.perm_ttest(m,f,None,rng,1000)[2]<0.05
        ff+= sb.signflip_test(m-f,rng,1000)<0.05
    print("rate",lam,"FPR shuffle",fs/N,"flip",ff/N)
# all zeros
z=np.zeros(50)
print("all-zero shuffle p", sb.perm_ttest(z,z,None,rng)[1:], "flip p", sb.signflip_test(z,rng))
# cv2
isi=np.array([0.1,0.3,2.0,0.2,0.2]); t=np.concatenate([[0],np.cumsum(isi)])
print("cv2", sb.cv2(t), np.mean([2*abs(0.3-0.1)/0.4, 0.0]))
# rm anova vs statsmodels
m=rng.normal(size=(21,3))+np.array([0,0.2,0.4])
print("rm", sb.rm_anova_load(m))
try:
    from statsmodels.stats.anova import AnovaRM
    df=pd.DataFrame([(i,l,m[i,l]) for i in range(21) for l in range(3)],columns=['s','l','y'])
    print(AnovaRM(df,'y','s',within=['l']).fit())
except Exception as e: print(e)
# encoding pooled
tr=pd.DataFrame({"timestamps_Encoding1":[0.,10.],"timestamps_Encoding2":[1.5,0.],"timestamps_Encoding3":[3.,0.]})
ts=np.array([0.5,2.0,3.5,3.6,10.5])
print("pooled", sb.encoding_rate_pooled(ts,tr), "code", sb.encoding_rate_pooled(ts,tr,True))
EOF
python3 $TMPDIR/t.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t.py", line 2, in <module>
    import numpy as np, pandas as pd
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls /opt /usr/local/bin 2>/dev/null | head; which -a python python3 conda uv pip 2>/dev/null; ls ~/.venv* ~/miniconda* 2>/dev/null | head
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
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
/opt/hostedtoolcache/Python/3.13.17/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.17/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.17/x64/bin/pip
/usr/bin/pip
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for p in /usr/bin/python3 /opt/hostedtoolcache/Python/3.13.17/x64/bin/python; do $p -c "import numpy,scipy,pandas;print('$p ok')" 2>&1 | tail -1; done
```

```
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
```

**Agent**

Neither Python on this machine has numpy, so I'm setting up a temporary environment to test the helper functions on synthetic data.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q v && uv pip install -q -p v/bin/python numpy scipy pandas statsmodels h5py 2>&1 | tail -3; v/bin/python -c "import numpy,scipy,pandas,statsmodels;print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  sed -i 's/^import sternberg as sb/import types; sys.modules["remfile"]=types.ModuleType("remfile"); d=types.ModuleType("dandi"); da=types.ModuleType("dandi.dandiapi"); da.DandiAPIClient=None; sys.modules["dandi"]=d; sys.modules["dandi.dandiapi"]=da\nimport sternberg as sb/' $TMPDIR/t.py; $TMPDIR/v/bin/python $TMPDIR/t.py
```

```
wr [1.25 1.25]
F 3.312352094176631 3.31235209417663
permanova (3.312352094176632, 0.022988505747126436) 0.016759083025178374
permanova FPR 0.06333333333333334
pt (0.9132021518680883, 0.0014992503748125937, 0.0014992503748125937) 0.0001955721442690425 9.778607213452124e-05
rate 0.2 FPR shuffle 0.055 flip 0.0525
rate 0.5 FPR shuffle 0.0675 flip 0.065
rate 1 FPR shuffle 0.065 flip 0.0625
rate 3 FPR shuffle 0.0625 flip 0.0675
all-zero shuffle p (0.0004997501249375312, 0.0004997501249375312) flip p 0.0004997501249375312
cv2 0.5000000000000001 0.49999999999999994
rm (1.9149159897977948, 2, 40, 0.1606215122710644)
             Anova
===============================
  F Value Num DF  Den DF Pr > F
-------------------------------
l  1.9149 2.0000 40.0000 0.1606
===============================

pooled [1.875 1.25 ] code [1.25 1.25]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/t2.py <<'EOF'
import numpy as np
rng=np.random.default_rng(1)
N=3000; P=1000
res={k:0 for k in ["sh_gt","sh_ge","fl_gt","fl_ge"]}
for lam in (0.3,1.0):
  res={k:0 for k in res}
  for i in range(N):
    m=rng.poisson(lam*2.5,108)/2.5; f=rng.poisson(lam*0.5,108)/0.5
    allv=np.concatenate([m,f]); perms=np.argsort(rng.random((P,216)),1); sh=allv[perms]
    diff=sh[:,:108].mean(1)-sh[:,108:].mean(1); obs=m.mean()-f.mean()
    res["sh_gt"]+=(np.sum(diff>obs)+1)/(P+1)<0.05; res["sh_ge"]+=(np.sum(diff>=obs-1e-12)+1)/(P+1)<0.05
    d=m-f; null=(rng.choice([-1.,1.],(P,108))*d).mean(1); o=d.mean()
    res["fl_gt"]+=(np.sum(null>o)+1)/(P+1)<0.05; res["fl_ge"]+=(np.sum(null>=o-1e-12)+1)/(P+1)<0.05
  print(lam,{k:v/N for k,v in res.items()})
EOF
$TMPDIR/v/bin/python $TMPDIR/t2.py
```

```
0.3 {'sh_gt': np.float64(0.071), 'sh_ge': np.float64(0.066), 'fl_gt': np.float64(0.07133333333333333), 'fl_ge': np.float64(0.06233333333333333)}
1.0 {'sh_gt': np.float64(0.06933333333333333), 'sh_ge': np.float64(0.06466666666666666), 'fl_gt': np.float64(0.067), 'fl_ge': np.float64(0.063)}
```

**Agent calls Bash**

```bash
cd  grep -n -o -E ".{0,400}P39CS.{0,400}" paper/10.1038-s41597-024-02943-8.txt | head -5; grep -o -i -E ".{0,200}(same patient|twice|two sessions|second session).{0,200}" paper/10.1038-s41597-024-02943-8.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000469/versions/0.240123.1806/assets/?page_size=200" | $TMPDIR/v/bin/python -c "
import json,sys,re; r=json.load(sys.stdin); p=[a['path'] for a in r['results']]
print(r['count'], len(p)); print(len({x.split('/')[0] for x in p}), sum('ses-1' in x for x in p), sum('ses-2' in x for x in p))"
```

Result: the fetched text is not kept.

**Agent**

**Verifier report, round 1: Kyzar et al. 2024 (doi:10.1038/s41597-024-02943-8), DANDI:000469 v0.240123.1806**

The claims file has 20 claims and the notebook tests all 20. My outcomes: 18 reproduced, 1 not_reproduced, 1 blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| subjects-sessions | reproduced | Cell 10: 21 subjects, 41 sessions, 21 Sternberg, 20 screening; only subject 19 (P47HMH) has no screening session. My own API query of the pinned version agrees: 41 assets, 21 subjects, 20 ses-1 and 21 ses-2. Ages are 17 to 70, matching Table 1. |
| sternberg-unit-yield | reproduced | Cell 12: 902 units (Hipp 190, Amg 259, dACC 171, pre-SMA 250, vmPFC 32). Every count is exact. |
| screening-unit-yield | reproduced | Cell 14: 907 units, MTL 421. 421 is within 10% of both 449 and 421, so it matches the 421 reading exactly. |
| behavior-accuracy | reproduced | Cell 17: mean over sessions 88.73%. |
| behavior-rt-load | reproduced | Cell 19, correct trials: F(2,40) = 7.92, p = 0.0013, and the mean of session medians rises 1.055 → 1.130 → 1.198 s. I checked `rm_anova_load` against statsmodels AnovaRM on synthetic data and it gives the same F. |
| behavior-accuracy-load | reproduced | Cell 21: accuracy falls monotonically, 91.22 → 88.62 → 86.35%. |
| isi-violations | reproduced | Cell 25: on all units, the mean (0.428) is in tolerance but the s.d. (0.625) is not. With the code's filter (units below 4%, n = 901) the values are 0.416 and 0.498, both in tolerance. The criterion accepts either reading. |
| firing-rate | reproduced | Cell 27: mean 2.546 Hz, min 0.108 Hz, max 33.824 Hz. |
| projection-distance | reproduced | Cell 29: 13.774 ± 7.325 (734 non-zero values). |
| waveform-snr | reproduced | Cell 31: `peak_snr` gives 6.625 ± 3.632. `mean_snr` (1.65 ± 0.95) does not match, but one reading is enough. |
| cv2 | reproduced | Cell 33: 0.938 ± 0.138. |
| isolation-distance | reproduced | Cell 35: median 31.138 over the 676 non-NaN units. |
| screening-concept-mtl | reproduced | Cell 38: 140 MTL units (33.25%) under both the two-sided and one-sided readings, so the readings agree and both are in tolerance. The code's parametric test gives exactly 138 (32.78%). |
| screening-concept-mfc | reproduced | Cell 40: 27 (5.56%) under both readings, well below the MTL's 33.25%. This one is fragile: seed 46911 gives 29 (5.97%), outside tolerance (problem 2). With 20,000 permutations near p = 0.05 it gives 26 (5.35%). |
| fig4-screening-examples | reproduced | Cell 42: all 5 units pass under both readings and the parametric test. |
| sternberg-concept-mtl | reproduced | Cell 44: 96 (21.38%) two-sided and 100 (22.27%) one-sided, both in tolerance (upper bounds 103.4 and 23.03%). Parametric gives exactly 94 (20.94%). |
| persistent-activity | not_reproduced | Cell 46, maintenance window (0 to 2500 ms), under both cell readings and both trial readings: p ≤ 1.7e-7 with preferred higher, but the preferred mean is 2.57 to 3.13 Hz against 4.76 ± 0.476. No reading puts all four values in tolerance, and the trial readings agree, so the criterion gives not reproduced. The variant (Encoding 1 window, Encoding 1 mask, all-area concept cells) matches all four values and the p-value (4.63/4.64/2.59/3.58, p = 8.6e-22; parametric 4.76/4.71/2.67/3.66, p = 1.4e-21). So the paper's numbers come from the encoding window, as the claims file anticipated. |
| fig5-sternberg-examples | reproduced | Cell 48: both units are concept cells in the amygdala under every test, with maintenance rate higher on preferred-shown trials (5.05 vs 1.43 Hz; 5.73 vs 4.17 Hz). |
| maintenance-cells-mfc | reproduced | Cell 50: all permutation × non-preferred readings give 139 to 144 (30.68 to 31.79%) out of 453 MFC units, all in tolerance. |
| probe-cells-mfc | blocked (methods_underspecified) | Cell 52: the readings disagree. Label shuffling with the Encoding 1 rate gives 104 to 105 (about 23%) and fails on every seed. Sign flipping gives 111 to 124 and is in tolerance. Label shuffling with the pooled rate gives 109 on the main seed (just out) and 110 to 111 on the other three (just in). The code's t-tests give exactly 122 (26.93%). |

### B. Problems

1. **[does not affect a conclusion] `perm_ttest`, `signflip_test`.** Both count exceedances with a strict `>`. With discrete spike counts that makes them anti-conservative, and identical inputs get p = 1/2001.
   - Synthetic null check (Poisson at 0.3 Hz, maintenance 2.5 s vs baseline 0.5 s, 108 trials, 3000 runs): false-positive rate is 7.1% with `>` and 6.6% with `>=` for shuffling; 7.1% vs 6.2% for flipping.
   - Shuffling follows permutationTest.m; the sign-flip test is the author's own.
   - Correcting it would lower maintenance and probe counts by a few units. Maintenance keeps a 10-unit margin. Probe stays blocked, because shuffle-Encoding 1 already fails.
2. **[does not affect a conclusion] Cell 40.** The screening MFC result depends on the seed: 27, 29, 28 and 27 across four seeds, and 29 (5.97%) is outside tolerance. The 20,000-permutation refinement (26) supports the pass, but the margin is about one unit.
3. **[does not affect a conclusion] Cell 52.** The extra seeds are printed without tolerance flags. Computed from the printed values, pooled shuffling passes on 3 of the 4 seeds. The blocked outcome rests on shuffle-Encoding 1, which fails on every seed.
4. **[does not affect a conclusion] Cell 44.** The Sternberg concept counts are not repeated across seeds. The one-sided reading (100) is 3.4 units from the upper bound.
5. **[does not affect a conclusion] Cell 5, `sternberg_rates`.** Anomalous trials are kept:
   - Subject 9 has a trial whose maintenance, probe and Encoding 1 end share one timestamp (0 s maintenance), so its maintenance window covers the probe and response.
   - One trial has 0 s from fixation to Encoding 1 (min 0.000), so its baseline window falls on the image.
   - Two trials out of 2673.
6. **[does not affect a conclusion] Cell 10.** Subjects 13 and 14 (P39CS and P39CS_2) share age, sex, year and diagnosis in Table 1. Without the "_2" suffix there are 20 native IDs, so the 21 "patients" may be 20 people. The claims file's criterion counts subject IDs, and Table 1 lists 21 rows, so the outcome stands. Neither the claims file nor the notebook says so.
7. **[does not affect a conclusion; affects interpretation] Cells 38, 40, 44, 46, 50, 52.** The paper's numbers come from the code's parametric tests: they reproduce the paper's figures exactly (138, 26, 94; 144 with the code's t-test; 122 with the code's probe test; persistent activity 4.76/4.71/2.67/3.66). Following the claims file, the notebook uses the Methods' permutation tests as the main reading. That is the stated rule, not a misreading. Note that the probe block exists only under that rule.
8. **[does not affect a conclusion] `isi_violation_pct`, `cv2`.** These run on stored spike times, which are unsorted in 1 Sternberg unit (one negative ISI). That matches the code and the effect is negligible.

**Helper checks on synthetic inputs:**
- `window_rates` uses strict bounds as documented.
- `anova_f` equals scipy `f_oneway`.
- `perm_anova` p-values agree with the parametric ones (0.023 vs 0.017).
- `cv2` with ignoreMode 1 is correct.
- `encoding_rate_pooled` and its Encoding 3-from-Encoding 2 variant are correct, provided onsets are greater than 0.
- `rm_anova_load` matches AnovaRM.

No leakage issues apply. Windows, trial selection and denominators (449, 453, 421 and 486) follow the claims file. The paper states no chance level for any selection.

The claims file does not misread the paper. The persistent-activity criterion follows the paper's text (maintenance period); the paper's own numbers appear to come from the encoding window.

### C. What I could not check

- **Blocked claims:** the notebook marks none as blocked, so step 4 does not apply. For probe-cells-mfc all the data are present; the block comes from the methods alone.
- **Effect of tie handling on real counts:** needs the maintenance and probe counts recomputed with `>=`, or the p-values printed, for units with p between 0.04 and 0.06.
- **Seed robustness of the Sternberg concept counts:** needs a seed repeat in cell 44, like those in cells 40 and 52.
- **Tolerance flags for the probe seeds:** cell 52 should print them for each extra seed.
- **The 0 s fixation-to-Encoding 1 trial:** it is not listed. Cell 5 should print trials with fixation-to-Encoding 1 under 0.5 s.
- **Encoding 2 and 3 timestamps when absent:** cell 5 should show they are 0 or NaN exactly when the load leaves them out, which `encoding_rate_pooled` relies on.
- **The RT figure in cell 19:** an image I did not inspect. It does not decide the claim.

## End of run

16 turns, 8 minutes, result: success.
