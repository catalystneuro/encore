# robotka-2023 · verifier-1 · run 43654219152

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat *.md 2>/dev/null | head -300
```

```
total 232
drwxr-xr-x 6 runner runner    4096 Nov 15 00:13 .
drwxr-xr-x 8 runner runner    4096 Nov 15 00:13 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 23:37 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 23:37 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 15 00:13 .claude
-rw-r--r-- 1 runner runner       0 Nov 15 00:12 .env
-rw-r--r-- 1 runner runner       0 Nov 15 00:12 .env.development
-rw-r--r-- 1 runner runner       0 Nov 15 00:12 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 15 00:12 .env.local
-rw-r--r-- 1 runner runner       0 Nov 15 00:12 .env.production
-rw-r--r-- 1 runner runner       0 Nov 15 00:12 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 15 00:12 .env.test
-rw-r--r-- 1 runner runner       0 Nov 15 00:12 .env.test.local
drwx------ 2 runner runner    4096 Nov 15 00:13 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 23:37 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 23:37 .github
-rw-r--r-- 1 runner runner       0 Nov 15 00:12 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 23:37 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 23:37 .mcp.json
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat robotka-2023.yaml
```

```
<persisted-output>
Output too large (54.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/9bc67b76-40e3-46fc-af47-1be7660f98a0/tool-results/becpxbd61.txt

Preview (first 2KB):
# Claims for Robotka, Thomas, Yu, Wood, Elie, Gahr & Theunissen (2023), Cell Reports 42, 112034,
# "Sparse ensemble neural code for a complete vocal repertoire", tested on CRCNS aa-5.
#
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-11,
# protocol pilot-14 as stated in docs/protocol.md (Reader). The criteria were written from the
# paper and its code alone; no data of the dataset were seen.
#
# Text read: the version of record (paper/10.1016-j.celrep.2023.112034.txt, extracted from the
# publisher PDF), with its STAR Methods and the Supplemental information (SI Figures 1 to 11 and
# their legends, which the PDF carries at its end). Table 1 was read from the text. Figures were
# not opened; no claim needed a value only printed in a figure.
#
# Code read: github.com/ftheunissen/Ensemble-Code-Cell-Reports-2022 at commit
# f2d237639217425e7fc81d694708f19428a3b026 (v1.0 in the key resources table, zenodo 7378502). It
# holds Jupyter notebooks with their printed outputs and decoders.py. GenerateReport.ipynb makes
# the per-unit summary (auditory test, per-call-type z, selectivity index); GenerateDataBase.ipynb
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/9bc67b76-40e3-46fc-af47-1be7660f98a0/tool-results/becpxbd61.txt"
}
```

```
1	# Claims for Robotka, Thomas, Yu, Wood, Elie, Gahr & Theunissen (2023), Cell Reports 42, 112034,
2	# "Sparse ensemble neural code for a complete vocal repertoire", tested on CRCNS aa-5.
3	#
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-11,
5	# protocol pilot-14 as stated in docs/protocol.md (Reader). The criteria were written from the
6	# paper and its code alone; no data of the dataset were seen.
7	#
8	# Text read: the version of record (paper/10.1016-j.celrep.2023.112034.txt, extracted from the
9	# publisher PDF), with its STAR Methods and the Supplemental information (SI Figures 1 to 11 and
10	# their legends, which the PDF carries at its end). Table 1 was read from the text. Figures were
11	# not opened; no claim needed a value only printed in a figure.
12	#
13	# Code read: github.com/ftheunissen/Ensemble-Code-Cell-Reports-2022 at commit
14	# f2d237639217425e7fc81d694708f19428a3b026 (v1.0 in the key resources table, zenodo 7378502). It
15	# holds Jupyter notebooks with their printed outputs and decoders.py. GenerateReport.ipynb makes
16	# the per-unit summary (auditory test, per-call-type z, selectivity index); GenerateDataBase.ipynb
17	# makes the per-trial table (response strength z, the PCA of trial-averaged KDE responses and the
18	# five PC weights per trial); decodingCallTypesNaiveBayes.ipynb and DataBaseMerge.ipynb run the
19	# single-unit decoder; decodingCallTypesNaiveBayesPart2.ipynb and decoders.py run the ensemble
20	# decoders; plotConfusions.ipynb makes Figure 4; GenerateMLFilters.ipynb makes the MRFs, the LDA,
[... 900 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('reproduce_robotka_2023.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--'); print(''.join(o['text'])[:6000])
        elif 'data' in o and 'text/plain' in o['data']: print('--OUT--'); print(''.join(o['data']['text/plain'])[:6000])
        elif o.get('output_type')=='error': print('--ERR--', o['ename'], o['evalue'])
EOF
```

```
<persisted-output>
Output too large (60.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/9bc67b76-40e3-46fc-af47-1be7660f98a0/tool-results/bzqohdw35.txt

Preview (first 2KB):
######## CELL 0 [markdown]
# Reproducing Robotka et al. (2023) from CRCNS aa-5

**Paper.** Robotka, Thomas, Yu, Wood, Elie, Gahr & Theunissen (2023), "Sparse ensemble neural code
for a complete vocal repertoire", Cell Reports 42, 112034, doi:10.1016/j.celrep.2023.112034.

**Dataset.** CRCNS aa-5, "Simultaneous extracellular recordings of avian auditory neurons in freely
behaving zebra finches...", doi:10.6080/K0TT4P5Q, read from the public bucket
`crcnsarchive/aa-5/live/`. CRCNS data sets are not versioned: the version is recorded as
`unversioned`, the one published version there is, and the MD5 sums of every file read (from the
data set's `checksums.md5`) are printed below so that a later change can be detected. The paper
cites this DOI and no version; the bucket holds a single copy (`live/`, data descriptor v0.6 of
29 Nov 2022), so that is what is pinned.

**Claims.** `claims/robotka-2023.yaml`, written from the version of record with its STAR Methods and
supplement, and the paper's code (github.com/ftheunissen/Ensemble-Code-Cell-Reports-2022 at commit
[... 26 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/9bc67b76-40e3-46fc-af47-1be7660f98a0/tool-results/bzqohdw35.txt"
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Reproducing Robotka et al. (2023) from CRCNS aa-5
4	
5	**Paper.** Robotka, Thomas, Yu, Wood, Elie, Gahr & Theunissen (2023), "Sparse ensemble neural code
6	for a complete vocal repertoire", Cell Reports 42, 112034, doi:10.1016/j.celrep.2023.112034.
7	
8	**Dataset.** CRCNS aa-5, "Simultaneous extracellular recordings of avian auditory neurons in freely
9	behaving zebra finches...", doi:10.6080/K0TT4P5Q, read from the public bucket
10	`crcnsarchive/aa-5/live/`. CRCNS data sets are not versioned: the version is recorded as
11	`unversioned`, the one published version there is, and the MD5 sums of every file read (from the
12	data set's `checksums.md5`) are printed below so that a later change can be detected. The paper
13	cites this DOI and no version; the bucket holds a single copy (`live/`, data descriptor v0.6 of
14	29 Nov 2022), so that is what is pinned.
15	
16	**Claims.** `claims/robotka-2023.yaml`, written from the version of record with its STAR Methods and
17	supplement, and the paper's code (github.com/ftheunissen/Ensemble-Code-Cell-Reports-2022 at commit
18	f2d2376). Method details the claims file lacks are taken from the paper and that code, cited in the
19	helper `aa5.py` and below.
20	
[... 695 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/9bc67b76-40e3-46fc-af47-1be7660f98a0/tool-results/bzqohdw35.txt",
 "offset": 716,
 "limit": 400
}
```

```
716	    print("  pairs among the two largest of their row:", n_ok, "of 4")
717	--OUT--
718	(a) exemplar, PCC_a
719	      Ag    Be    DC    Di    LT    Ne    So    Te    Th    Wh
720	Ag  40.1   9.8   5.9   4.7   3.0   6.2  10.2   1.0   0.8  18.4
721	Be   8.9  43.6   6.1   1.3  14.0   4.8   3.4   3.6   1.9  12.5
722	DC   5.2  10.0  35.9   4.2   8.6  10.5   4.6   9.0   3.5   8.6
723	Di  20.9   4.3  11.4  20.0   4.6   8.1  16.5   4.9   1.4   8.0
724	LT   3.7  15.4   8.1   0.9  21.6  13.7   1.7  19.1   4.1  11.7
725	Ne   4.3   3.9   6.6   2.2   8.0  36.3   3.4  19.3   6.3   9.7
726	So  11.2   6.4   7.2   5.6   1.6   6.3  52.6   1.0   0.4   7.7
727	Te   1.6   4.5   8.5   1.2  12.0  23.1   1.0  34.7   6.5   6.9
728	Th   2.2   6.6  10.5   1.4  10.8  29.8   2.0  18.2  11.3   7.2
729	Wh  12.9  10.4   7.9   1.3   8.7  16.6   4.1  11.8   2.2  24.0
730	  true Ne predicted Te: 19.3%, rank 1 of 9 off-diagonal entries (largest: Te 19.3%)
731	  true LT predicted Be: 15.4%, rank 2 of 9 off-diagonal entries (largest: Te 19.1%)
732	  true Th predicted Te: 18.2%, rank 2 of 9 off-diagonal entries (largest: Ne 29.8%)
733	  true Di predicted Ag: 20.9%, rank 1 of 9 off-diagonal entries (largest: Ag 20.9%)
734	  pairs among the two largest of their row: 4 of 4
735	(b) trial, 1 rep, PCC_b
[... 370 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "aa5.py"
}
```

```
1	"""Loading and measures for CRCNS aa-5, the awake playback data of Robotka et al. (2023).
2	
3	Robotka, Thomas, Yu, Wood, Elie, Gahr & Theunissen (2023), Cell Reports 42, 112034,
4	doi:10.1016/j.celrep.2023.112034. Data set: CRCNS aa-5, doi:10.6080/K0TT4P5Q (unversioned).
5	
6	The data set holds one tar.gz per recording site, each with one pickle per spike-sorted unit
7	(`goodPlayback-e<electrode>-c<cluster>.pkl`, data descriptor v0.6). A pickle holds a unit
8	dictionary and two pandas tables written with pandas 1.x; `pandas.compat.pickle_compat` reads
9	them. A tar.gz cannot be read out of order, so each site file is streamed once from the bucket
10	(decompressed with isal, which is faster than zlib), and each unit is reduced as it is read to
11	what the analysis uses: spike times per trial, the stored KDE (first 1000 samples), labels, and
12	the stimulus waveform of each stimulus once. The microphone recordings, most of every file, are
13	dropped. Nothing is written to disk.
14	
15	Where the parameters come from (the claims file's common methods C1 to C11 cite the paper and
16	its code, github.com/ftheunissen/Ensemble-Code-Cell-Reports-2022 at commit f2d2376):
17	
18	- `SNR_MIN = 5`: units with spike SNR above 5 (C1; GenerateDataBase.ipynb skips SpikeSNR < 5).
19	- `P_AUD = 0.01` and the 0 to 0.5 s minus -0.5 to 0 s spike-count difference (C1, SI Figure 2A
20	  legend; GenerateReport.ipynb calc_zscore_all, which uses all stimuli of the pickle, song
[... 582 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat paper/aa-5.data-description.txt; grep -n -i -E "field l|CLM|NCM|histolog|depth|region" paper/10.1016-j.celrep.2023.112034.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=aa-5/" | python3 -c "
import sys,re;t=sys.stdin.read();ks=re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',t,re.S);print(len(ks));[print(k,s) for k,s in ks if not k.endswith('.tar.gz')]; print('truncated' if 'NextContinuationToken' in t else 'complete')"; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/aa-5/live/filelist.txt" | head -80
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' 2>&1 | tail -30
import numpy as np, aa5
rng=np.random.default_rng(0)
# _rows leakage test: feature value encodes trial index
U,S,Tm=3,4,6
C=np.array([[6,3,2,1],[5,6,2,4],[1,2,6,6]])
F=np.full((U,S,Tm,1),np.nan)
for u in range(U):
    for s in range(S):
        F[u,s,:C[u,s],0]=np.arange(C[u,s])
skip=np.array([[2,1,0,-1],[4,5,1,-1],[0,1,3,-1]])
bad=0
for _ in range(2000):
    X,n=aa5._rows(F,C,rng,skip=skip)
    for s in range(S):
        for u in range(U):
            vals=X[s,:n[s],u]
            if skip[u,s]>=0 and np.any(vals==skip[u,s]): bad+=1
            if np.any(np.isnan(vals)): bad+=1000
print("leak/nan count",bad)
# chance on null data, both CV
y=np.repeat(np.arange(10),11)
for cv in ["trial","exemplar"]:
    ps=[];pm=[]
    for _ in range(200):
        Fz=rng.normal(size=(2,110,10,6)); Cz=np.full((2,110),10)
        conf,nt=aa5.decode(Fz,Cz,y,10,rng,code="ZT",cv=cv,nperm=1)
        ps.append(aa5.pcc_code(conf,nt)); pm.append(aa5.pcc_methods(conf,nt))
    print(cv,np.mean(ps),np.mean(pm))
# GNB vs sklearn
from sklearn.naive_bayes import GaussianNB
X=rng.normal(size=(300,4)); yy=rng.integers(0,3,300); Xt=rng.normal(size=(20,4))
g=GaussianNB(priors=[1/3]*3).fit(X,yy)
print("gnb max diff",np.abs(g.predict_proba(Xt)-aa5._gnb_posterior(X,yy,Xt,3)).max())
# SI
print(aa5.selectivity_index([1]*10), aa5.selectivity_index([1]+[0]*9))
# regression with ns large: F should approx standard F *neff/n
x=rng.normal(size=500); yv=0.3*x+rng.normal(size=500)
r=aa5.corrected_regression(x[:,None],yv,1000,1)
import scipy.stats as st; lr=st.linregress(x,yv); print(r['r2adj'], lr.rvalue**2, r['df'])
# eigh vs eig rule check: eigh on nonsymmetric uses lower triangle
EOF
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls /usr/bin/python3* ; which -a python python3; ls ~/.local/bin 2>/dev/null; python3 -m pip --version; uv --version 2>/dev/null
```

```
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.14
/usr/bin/python3.14-config
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/usr/bin/python3
/bin/python3
pip 26.3 from /opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/pip (python 3.13)
uv 0.13.8 (x86_64-unknown-linux-gnu)
```

**Agent calls Bash**

```bash
cd  /opt/hostedtoolcache/Python/3.13.18/x64/bin/python -c "import numpy, scipy, sklearn, pandas; print('ok')" 2>&1 || (uv venv -q $TMPDIR/v && uv pip install -q --python $TMPDIR/v/bin/python numpy scipy scikit-learn pandas 2>&1 | tail -2; echo done)
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy, scipy, sklearn, pandas; print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'numpy'
done
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF' 2>&1 | tail -30
import numpy as np, aa5
rng=np.random.default_rng(0)
U,S,Tm=3,4,6
C=np.array([[6,3,2,1],[5,6,2,4],[1,2,6,6]])
F=np.full((U,S,Tm,1),np.nan)
for u in range(U):
    for s in range(S):
        F[u,s,:C[u,s],0]=np.arange(C[u,s])
skip=np.array([[2,1,0,-1],[4,5,1,-1],[0,1,3,-1]])
bad=0
for _ in range(2000):
    X,n=aa5._rows(F,C,rng,skip=skip)
    for s in range(S):
        for u in range(U):
            vals=X[s,:n[s],u]
            if skip[u,s]>=0 and np.any(vals==skip[u,s]): bad+=1
            if np.any(np.isnan(vals)): bad+=1000
print("leak/nan count",bad)
y=np.repeat(np.arange(10),11)
for cv in ["trial","exemplar"]:
    ps=[];pm=[]
    for _ in range(200):
        Fz=rng.normal(size=(2,110,10,6)); Cz=np.full((2,110),10)
        conf,nt=aa5.decode(Fz,Cz,y,10,rng,code="ZT",cv=cv,nperm=1)
        ps.append(aa5.pcc_code(conf,nt)); pm.append(aa5.pcc_methods(conf,nt))
    print(cv,np.mean(ps),np.mean(pm))
# exemplar-specific signal with no call-type signal: trial CV vs exemplar CV
for cv in ["trial","exemplar"]:
    ps=[]
    for _ in range(100):
        stimmean=rng.normal(size=(2,110,1,6))*1.0
        Fz=stimmean+rng.normal(size=(2,110,10,6)); Cz=np.full((2,110),10)
        conf,nt=aa5.decode(Fz,Cz,y,10,rng,code="ZT",cv=cv,nperm=1)
        ps.append(aa5.pcc_code(conf,nt))
    print("exemplar-only signal",cv,np.mean(ps))
from sklearn.naive_bayes import GaussianNB
X=rng.normal(size=(300,4)); yy=rng.integers(0,3,300); Xt=rng.normal(size=(20,4))
g=GaussianNB(priors=[1/3]*3).fit(X,yy)
print("gnb max diff",np.abs(g.predict_proba(Xt)-aa5._gnb_posterior(X,yy,Xt,3)).max())
print(aa5.selectivity_index([1]*10), aa5.selectivity_index([1]+[0]*9))
x=rng.normal(size=500); yv=0.3*x+rng.normal(size=500)
r=aa5.corrected_regression(x[:,None],yv,1000,1)
import scipy.stats as st; lr=st.linregress(x,yv); print(r['r2adj'], lr.rvalue**2, r['df'])
d=np.array([.5,.1,.1,.05,.05,.05,.05,.04,.03,.03])
conf=np.diag(d); print(aa5.entropy_selectivity(conf,np.ones(10),True),aa5.entropy_selectivity(conf,np.ones(10),False))
EOF
```

```
leak/nan count 2000000
trial 9.995514647230268 9.995514647230268
exemplar 10.037336083844881 10.037336083844881
exemplar-only signal trial 18.273811124715472
exemplar-only signal exemplar 9.876594220238754
gnb max diff 2.7755575615628914e-16
0.0 1.0
0.07978264640239463 0.08162676935549593 (1, 998)
0.24198867797151136 0.24198867797151136
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF' 2>&1 | tail -30
import numpy as np, aa5
rng=np.random.default_rng(0)
U,S,Tm=3,4,6
C=np.array([[6,3,2,2],[5,6,2,4],[2,2,6,6]])
F=np.full((U,S,Tm,1),np.nan)
for u in range(U):
    for s in range(S):
        F[u,s,:C[u,s],0]=np.arange(C[u,s])
skip=np.array([[2,1,0,-1],[4,5,1,-1],[0,1,3,-1]])
bad=nan=0
for _ in range(2000):
    X,n=aa5._rows(F,C,rng,skip=skip)
    for s in range(S):
        for u in range(U):
            vals=X[s,:n[s],u]
            if skip[u,s]>=0 and np.any(vals==skip[u,s]): bad+=1
            if np.any(np.isnan(vals)): nan+=1
print("leak",bad,"nan",nan)
X,n=aa5._rows(F,C,rng,skip=skip); print(n); print(X[0,:n[0]].T)
EOF
```

```
leak 0 nan 0
[5 5 5 6]
[[0. 1. 3. 4. 5.]
 [0. 1. 2. 3. 3.]
 [1. 1. 1. 1. 1.]]
```

**Agent calls Bash**

```bash
cd  grep -n -i -E "SNR|730|292|signal-to-noise" paper/10.1016-j.celrep.2023.112034.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i -B3 -A8 "entropy selectivity" paper/10.1016-j.celrep.2023.112034.txt | sed -n 1,80p
```

Result: not kept, because it reads the paper's text.

**Agent**

**Verifier report, round 1: Robotka et al. 2023 on CRCNS aa-5**

The claims file has 30 claims. The notebook runs tests for 19 of them and treats 11 as blocked.

### A. Outcomes

| claim id | outcome | reason |
|---|---|---|
| stimulus-set-link | reproduced | Cell 14: 4 birds, 110 stimuli, and the counts per call type match the paper exactly (diff 0 for all 10). |
| paper-good-units-link | partially_reproduced | Cell 8/10: 91 of the 100 listed units are in the dataset, and all 91 are auditory with all 110 stimuli. The 9 missing units all come from the `ZF4F_2t_190613_101015.old` site folder, which is not in the archive. 91 is at least 90. |
| auditory-units | reproduced | Cell 16: 287 auditory units (292 ± 29.2). Under reading (b), counted as pickles with vocalization trials, the total is 726 (730 ± 73) and the fraction 39.5% (40.1 ± 4.01). Under (a) the SNR ≥ 5 units are 414 or 491, which is out of tolerance. |
| inhibited-units | reproduced | Cell 18: 47 of 287 = 16.4% (46 ± 4.6; 15.7 ± 1.57). |
| fig3c-peak-call-types | reproduced (code zCT reading only) | Cell 24, reading (b): Di ranks first and So second; peak counts Di 53 and So 58 are in tolerance; Ag, Be, So and Di are 4 of the top 5. Under the Methods reading (a) the ranking is So > Ag > Di, which would be not_reproduced. |
| fig4a-unit-z-vs-zt | reproduced | Cell 26: 187 units (191 ± 19.1). Every reading puts both means in tolerance; reading (a) gives Z 10.68, Z+T 12.05, paired t(186) = 7.17, p < 1e-5. |
| good-units-100 | partially_reproduced | Cell 28, reading (b): the designated single run gives 89, one below the tolerance band of 90–110. Ten other seeds give 87–101 (8 of 10 in tolerance), and 100 repetitions give 91. ZF6M has 10 good units against the paper's 16, out of tolerance in every run shown. Reading (a) gives 77. Applied strictly to the one designated run, the outcome would be not_reproduced. |
| fig4b-ensemble-20 | reproduced (code CV reading) | Cell 30, reading (b): Z+T 43.15 and Z 30.36, rising at every size step, corrected t(138) = 9.53. Under the Methods exemplar CV (a), Z+T is 32.0 and Z is 24.1, which is partially_reproduced. |
| fig4b-top-ensembles | reproduced (code CV reading) | Cell 33, reading (b): re-estimated mean 48.8 for the top 10% and 50.4 for the top 5%; best ≥ 55. Under reading (a) the mean is about 34, so not reproduced. |
| fig4b-confusions | reproduced | Cell 35: all four named pairs are among the two largest off-diagonal entries of their row, under both readings. |
| figs4-per-bird-and-sex | blocked (other) | Cell 37: the test needs ensembles of 15 within each bird. ZF6M has only 10 good units (9 under reading a), so the test cannot be run. It could have been run on the paper's own listed units (see B5). |
| figs6-primary-vs-secondary | blocked (metadata_insufficient) | The dataset gives each unit only bird, site depth and electrode number. The histology needed to assign brain areas is not deposited (archive listing checked). |
| fig5e-volume | reproduced | Cell 43, reading (b): 1797 ensembles pass the PCC > 30% filter (1746 ± 174.6); slope positive, p < 0.05. R2adj is in tolerance only with the code window and the code's eigh axes (0.094). The Methods readings give 0.12, which is outside the ±0.01 tolerance but rounds to the printed 0.1. |
| fig5f-si-unrelated | reproduced | Cell 45: p ≥ 0.12 under every reading; under the Methods SI (a) with reading (b), p = 0.85. |
| fig5g-entropy-selectivity | reproduced | Cell 47: the Methods ES (b) gives a negative slope with p < 0.05 under both CV readings. The code's ES (a) gives this only under exemplar CV (p = 0.046 / 0.0066). Under the code's own pipeline (CV b with ES a) the slope is +18.9, p = 0.79. |
| fig5h-neural-noise | partially_reproduced | Cell 49: the slope is negative and significant under every reading. R2adj is 0.13–0.27, never within 0.1 ± 0.01. |
| fig5-multiple-regression | reproduced (eigh LDA variant) | Cell 51, reading (b) with eigh axes: R2adj 0.235–0.241 (0.22 ± 0.022), p < 0.001. With the Methods "largest" axes R2adj is 0.246–0.252, just outside tolerance. |
| pcs-variance | reproduced | Cell 22: the first five PCs explain 0.9244 of the variance (paper about 0.90; code printed 0.922). |
| table1-snr | reproduced | Cell 20, reading (a): mean 6.84 (7.42 ± 0.742), median 6.07 (6.5 ± 0.65). Reading (b) also passes (6.97, 6.20). |
| figs5-region-anova | blocked (metadata_insufficient) | Same as figs6: no area per unit in the archive. |
| fig6a-acoustic-clusters | blocked (data_missing) | The vocalization database is not in aa-5 (archive listing: only the site tars, one GUI notebook and the docs). |
| acoustic-labels-decoding | blocked (data_missing) | The stimuli's acoustic cluster labels are not in aa-5. |
| fig6c-number-of-clusters | blocked (data_missing), part testable | The call-type half (mean 10.83, median 9) needs only aa-5, and the criterion says to judge it on its own, but it was not run (B6). |
| fig6c-ari-call-over-acoustic | blocked (data_missing) | Needs acoustic labels. |
| figs10-ensemble-size | blocked (data_missing) | Needs acoustic labels. |
| anesth-auditory-units | blocked (other: data elsewhere, CRCNS aa-4) | Not part of aa-5. |
| anesth-decoding-better | blocked (other: aa-4) | Not part of aa-5. |
| anesth-regressions | blocked (other: aa-4) | Not part of aa-5. |
| figs9-per-region-regressions | blocked (metadata_insufficient; aa-4) | The awake part needs areas, which are not deposited. |
| anesth-primary-secondary-rate | blocked (other: aa-4) | Not part of aa-5. |

**Chance level.** The paper gives 10%. The notebook's pre-onset control gives 9.89% (cell 12). My synthetic null gives 10.0% for both PCC definitions and both CV schemes.

### B. Problems

1. **[affects a conclusion]** `aa5.decode`, `cv="trial"`, cells 28–33. The code's cross-validation trains on other trials of the same exemplar that is tested. On synthetic data with only exemplar-specific signal and no call-type signal, I get 18.3% with trial CV against 9.9% with exemplar CV. good-units-100, fig4b-ensemble-20 and fig4b-top-ensembles reach tolerance only under this variant. Under the Methods' exemplar hold-out they give 77 units, 32.0% and 34%. The claims file makes the Methods reading the main one, so adopting the code reading has to be stated as an assumption.
2. **[affects a conclusion]** Cell 28. The good-unit count depends on the seed (87–101 across seeds) and the designated run gives 89. Per-bird counts are not printed for the 10 extra seeds. ZF6M (10 against 16) is the stable deficit. Of the 91 paper units present, only 70 pass the threshold here under (b) and 51 under (a).
3. **[affects a conclusion]** Claims file, C11 ES reading (b). The Methods ES formula gives negative values here (mean −0.12, cell 41), but the Figure 5G legend says ES "ranges between 0 and 1". That is the same argument the claims file used to rule out C2(a) for SI. ES_b also falls mechanically as single-unit PCC rises, which makes a negative slope nearly built in. Under the reading the legend supports (ES_a), fig5g holds only with exemplar CV.
4. **[does not affect a conclusion]** Cell 33. The "best ensemble" is the maximum of 1000 single-repetition re-estimates, each with about 110 test trials. That is biased upward: the re-estimated best (95.0) exceeds the best first draw (88.4). The 100-repetition ensembles of cell 40 give best values of 68.4 under (b) and 41.1 under (a), so the ≥ 55 verdict under (b) stands.
5. **[affects a conclusion]** Cell 37, figs4-per-bird-and-sex. The variant on the paper's listed units was not run. All 9 missing listed units are ZF4F, so ZF6M keeps all its listed units (presumably 16; per-bird counts of the listed units are not printed) and ZF4F has 34. The paper-good-units-link criterion allows exactly this variant. The printed message ("15 or fewer … undefined for ns = 15") also misstates the cause: the birds have 9, 10 and 14 units, below 15.
6. **[affects a conclusion]** fig6c-number-of-clusters. The call-type values (UMAP + Ward, ARI-optimal cut, C12) need only aa-5 and were not computed.
7. **[does not affect a conclusion]** Cells 43 and 51. fig5e reaches R2adj tolerance only with the code window and eigh axes; fig5-multiple-regression only with eigh. These are code variants under the claims file's rule, so a reproduced verdict here rests on them.
8. **[does not affect a conclusion]** Cell 26 / C5. The Methods unit rule (≥ 2 trials of every stimulus, 125 units) was never run. Only the code's rule (110 distinct stimuli, 187 units) was used. The 191 in the paper matches the code's rule.
9. **[does not affect a conclusion]** `kde_matrix` / C4. The stored `spikeKDE` is used without checking that it is a 30 ms kernel, and the `KDE_BW` values (0.2, 3, 5, …) are not 0.03. The match to the code's 0.922 suggests it is the same KDE the code used. Also, `kde_matrix` treats a stimulus as spikeless when the sum of its spike times is 0, rather than when it has no spikes.
10. **[does not affect a conclusion]** `unit_regressors`. MRF projections are scaled by one SD pooled over all good units. That only shifts log volume by a constant, but if the code scales per unit the result could differ. I could not verify which it does.
11. **[does not affect a conclusion]** Cell 11 still contains an author conclusion ("Result: partially reproduced").

**Helper checks.** On synthetic inputs, `_rows` never put a held-out trial into training (0 of 2000 draws, with no NaN padding when every unit has ≥ 2 trials). `_gnb_posterior` matches sklearn GaussianNB to 3e-16. `selectivity_index` gives 0 and 1 at its extremes. `corrected_regression` reduces to ordinary R2 when ns is large.

### C. Could not check

- **The paper's code** (pinned commit). It was not available to me, so I could not confirm: ES normalization, MRF scaling (per unit or pooled), eigh on the non-symmetric matrix, the PCC > 30 filter, or that `plotConfusionsBird` uses n = 2 per sex. Printing the relevant code lines, or the code's own intermediate values (for example the per-unit ES and SI of the listed units), would settle these.
- **The KDE kernel.** A cell that recomputes a 30 ms Gaussian KDE from the spike times and compares it with the stored `spikeKDE` would settle B9.
- **Whether the vocalization database is public.** The paper gives no deposit, and I did not look outside the aa-5 archive.
- **good-units-100.** Needed: per-bird counts for each of the 10 seeds, and per-bird counts of the 91 listed units present.
- **figs4.** Needed: the ensemble-of-15 test run on the listed units.
- **fig6c call-type half.** Needed: mean and median optimal cluster number against call-type labels.
- **Missing 9 units.** Needed: whether the 9 `.old` units match pickles in `ZF4F_2t_190613_101015` by spike train rather than by name.

## End of run

17 turns, 5 minutes, $1.76 at API prices, result: success.
