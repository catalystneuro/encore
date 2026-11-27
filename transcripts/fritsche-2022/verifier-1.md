# fritsche-2022 · verifier-1 · run 44877058619

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat *.md 2>/dev/null | head -300
```

```
total 292
drwxr-xr-x 6 runner runner    4096 Nov 21 07:01 .
drwxr-xr-x 8 runner runner    4096 Nov 21 07:01 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 06:45 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 06:45 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 21 07:01 .claude
-rw-r--r-- 1 runner runner       0 Nov 21 07:01 .env
-rw-r--r-- 1 runner runner       0 Nov 21 07:01 .env.development
-rw-r--r-- 1 runner runner       0 Nov 21 07:01 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 21 07:01 .env.local
-rw-r--r-- 1 runner runner       0 Nov 21 07:01 .env.production
-rw-r--r-- 1 runner runner       0 Nov 21 07:01 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 21 07:01 .env.test
-rw-r--r-- 1 runner runner       0 Nov 21 07:01 .env.test.local
drwx------ 2 runner runner    4096 Nov 21 07:01 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 06:45 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 06:45 .github
-rw-r--r-- 1 runner runner       0 Nov 21 07:01 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 06:45 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 06:45 .mcp.json
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat fritsche-2022.yaml
```

```
<persisted-output>
Output too large (50.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/d2718702-7f79-44bb-80e1-3fe7896992a6/tool-results/bodemzoan.txt

Preview (first 2KB):
# Claims for Fritsche, Solomon & de Lange (2022), "Brief Stimuli Cast a Persistent Long-Term Trace
# in Visual Cortex", J Neurosci 42(10):1999-2010, doi:10.1523/JNEUROSCI.1350-21.2021, on dandiset
# 000021 (Allen Institute, Visual Coding, Neuropixels, Brain Observatory 1.1 Stimulus Set), which the
# paper reuses.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-21,
# protocol as stated in docs/protocol.md (pilot-18).
#
# Text read. The version of record, full text from PubMed Central (PMC8916757), in
# paper/10.1523-jneurosci.1350-21.2021.txt: abstract, Introduction, Materials and Methods, Results,
# Discussion, the legends of Figures 1 to 8 and Tables 1 and 2. The paper has no supplement. The
# extracted text drops the display equations; these were read from the MathML of the same PMC page
# (pmc.ncbi.nlm.nih.gov/articles/PMC8916757). They are (1) adaptation ratio = fr_repeat /
# fr_orthogonal; (2) the double exponential, printed as r(n) = 1 - a_fast * exp(-(n-1)/tau_fast) +
# a_slow * exp(-(n-1)/tau_slow); (3) the single exponential r(n) = 1 - a * exp(-(n-1)/tau); (4) OSI =
# (fr_preferred - fr_non-preferred) / (fr_preferred + fr_non-preferred); (5) the cumulative ratio of
# Fig. 4, ar_2-8 = product over n = 2 to 8 of ar_n. Figures were not opened (there is no PDF under
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "fritsche-2022.yaml"
}
```

```
1	# Claims for Fritsche, Solomon & de Lange (2022), "Brief Stimuli Cast a Persistent Long-Term Trace
2	# in Visual Cortex", J Neurosci 42(10):1999-2010, doi:10.1523/JNEUROSCI.1350-21.2021, on dandiset
3	# 000021 (Allen Institute, Visual Coding, Neuropixels, Brain Observatory 1.1 Stimulus Set), which the
4	# paper reuses.
5	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-21,
6	# protocol as stated in docs/protocol.md (pilot-18).
7	#
8	# Text read. The version of record, full text from PubMed Central (PMC8916757), in
9	# paper/10.1523-jneurosci.1350-21.2021.txt: abstract, Introduction, Materials and Methods, Results,
10	# Discussion, the legends of Figures 1 to 8 and Tables 1 and 2. The paper has no supplement. The
11	# extracted text drops the display equations; these were read from the MathML of the same PMC page
12	# (pmc.ncbi.nlm.nih.gov/articles/PMC8916757). They are (1) adaptation ratio = fr_repeat /
13	# fr_orthogonal; (2) the double exponential, printed as r(n) = 1 - a_fast * exp(-(n-1)/tau_fast) +
14	# a_slow * exp(-(n-1)/tau_slow); (3) the single exponential r(n) = 1 - a * exp(-(n-1)/tau); (4) OSI =
15	# (fr_preferred - fr_non-preferred) / (fr_preferred + fr_non-preferred); (5) the cumulative ratio of
16	# Fig. 4, ar_2-8 = product over n = 2 to 8 of ar_n. Figures were not opened (there is no PDF under
17	# paper/); no number below is read from a figure.
18	#
19	# Code. The paper links its analysis code at the Donders Repository, doi:10.34973/kpt9-y956
20	# (collection DSC_3018000.01_830, version 1). Its file list can be read without a login. It holds
[... 853 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" fritsche-2022.yaml; grep "^- id:" fritsche-2022.yaml; cat adaptation.py
```

```
31
- id: units-responsive-count
- id: fig1d-v1-1back
- id: fig1d-extrastriate-1back
- id: fig1d-thalamus-1back
- id: fig1e-consistent-across-mice
- id: fig2-v1-tuning-main-effect
- id: fig2-v1-tuning-interaction
- id: fig2-v1-adaptation-at-all-orientations
- id: fig2-thalamus-no-tuning-dependence
- id: fig3a-v1-long-term
- id: fig3a-v1-double-exponential
- id: fig3a-v1-half-life
- id: fig4-cumulative-adaptation
- id: fig4b-linear-accumulation
- id: fig3b-thalamus-short-term
- id: v1-vs-thalamus-welch
- id: fig3c-mice-long-term
- id: decay-cortex-double-better
- id: table1-extrastriate-tau-slow
[... 478 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_fritsche_2022.ipynb'))
print(len(nb['cells']))
for i,c in enumerate(nb['cells']):
    print('=== CELL',i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--- OUT'); print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--- OUT'); print(''.join(d['text/plain'])[:6000])
        elif o.get('output_type')=='error': print('ERR', o['ename'], o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
2333 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 800
}
```

```
1	84
2	=== CELL 0 markdown
3	# Fritsche, Solomon & de Lange (2022) on DANDI:000021
4	
5	Paper: Fritsche, Solomon & de Lange (2022), "Brief Stimuli Cast a Persistent Long-Term Trace in
6	Visual Cortex", J Neurosci 42(10):1999-2010, doi:10.1523/JNEUROSCI.1350-21.2021. The paper reuses
7	the Allen Brain Observatory Visual Coding Neuropixels data.
8	
9	Dataset: DANDI:000021 (Allen Institute, Visual Coding, Neuropixels, Brain Observatory 1.1
10	stimulus set), version 0.251116.2246, doi:10.48324/dandi.000021/0.251116.2246. The paper names
11	the dandiset but no version. This is the only published version, and it is the most recent;
12	the draft has the same 214 assets and size. It holds the 32 sessions (one per mouse) the paper
13	describes, so no earlier version could match the claims file better.
14	
15	Claims: claims/fritsche-2022.yaml, written from the version of record (PMC8916757; no
16	supplement). The paper's code (doi:10.34973/kpt9-y956) is restricted and was not read.
17	
18	Data are streamed from the archive; nothing is downloaded. Loading reduces each session to spike
19	counts per unit and presentation (about 2 to 3 minutes for the 32 files with four processes).
20	
[... 780 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 800,
 "limit": 750
}
```

```
800	def consistency(g, label):
801	    above = int((g.orth > g.rep).sum()); n = len(g)
802	    p = stats.binomtest(above, n, 0.5).pvalue if n else np.nan
803	    ok_a = above == n and n > 0
804	    ok_b = (p < 0.05) and above > n / 2
805	    print(f"{label}: {n} mice, {above} with orthogonal above repeat, sign test p = {p:.2g}, "
806	          f"median orth - rep {np.median(g.orth - g.rep):.3f} Hz; (a) {ok_a}, (b) {ok_b}")
807	    return ok_a, ok_b
808	=== CELL 26 code
809	for grp, name in [(A.THALAMUS, "thalamus"), (A.CORTEX, "cortex")]:
810	    g = mouse_rates(DG, grp, [1], A.DG_WIN)[0]
811	    consistency(g, f"drifting 1-back, {name}")
812	    print(f"  rates {g[['rep', 'orth']].min().min():.2f} to {g[['rep', 'orth']].max().max():.2f} Hz")
813	--- OUT
814	drifting 1-back, thalamus: 23 mice, 21 with orthogonal above repeat, sign test p = 6.6e-05, median orth - rep 2.156 Hz; (a) False, (b) True
815	  rates 7.76 to 42.70 Hz
816	drifting 1-back, cortex: 32 mice, 32 with orthogonal above repeat, sign test p = 4.7e-10, median orth - rep 1.912 Hz; (a) True, (b) True
817	  rates 7.55 to 17.14 Hz
818	
819	=== CELL 27 markdown
[... 730 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1549,
 "limit": 800
}
```

```
File content (27037 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1549,
 "limit": 400
}
```

```
1549	4        region    2-10            [2, 4, 9]                 [3]            []           []        4
1550	5        region    2-50                   []                 [3]            []         [44]        1
1551	
1552	V1 against LGN, normalized by region (b), n = 2 to 10
1553	    n      t       p  p_fdr
1554	0   2  3.020  0.0029  0.021
1555	1   3  1.161    0.25   0.37
1556	2   4  2.874  0.0046  0.021
1557	3   5 -0.152    0.88   0.88
1558	4   6  0.588    0.56   0.72
1559	5   7 -1.890   0.061   0.14
1560	6   8 -1.192    0.23   0.37
1561	7   9  2.719  0.0073  0.022
1562	8  10  0.426    0.67   0.75
1563	
1564	V1 against LP, normalized by region (b), n = 2 to 10
1565	    n      t        p  p_fdr
1566	0   2  0.954     0.34   0.41
1567	1   3  3.774  0.00023  0.002
1568	2   4  2.508    0.013   0.06
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1948,
 "limit": 390
}
```

```
1948	print(f"extrastriate: {ex6.ratio.min():.3f} to {ex6.ratio.max():.3f}, all in [0.801, 1.023]: "
1949	      f"{bool(ex6.ratio.between(0.801, 1.023).all())}, largest corrected p {ex6.p_fdr.max():.2g}")
1950	for a_, (lo, hi), n_paper in [("LGN", (0.93 - 0.093, 0.98), 60), ("LP", (0.85 - 0.085, 0.96), 16)]:
1951	    row = r6[r6.area == a_].iloc[0]
1952	    print(f"{a_}: ratio {row.ratio:.3f}, widened CI [{lo:.3f}, {hi}], match {lo <= row.ratio <= hi}; "
1953	          f"p {row.p:.2g} (corrected {row.p_fdr:.2g}); units {row.n_units} against {n_paper}")
1954	tab6["ex_min"] = tab6[["LM", "AL", "RL", "PM", "AM"]].min(axis=1)
1955	tab6["ex_max"] = tab6[["LM", "AL", "RL", "PM", "AM"]].max(axis=1)
1956	print(tab6[["O1", "O2", "blanks", "blocks", "ex_min", "ex_max", "LGN", "LP"]].to_string())
1957	--- OUT
1958	extrastriate: 0.891 to 0.930, all in [0.801, 1.023]: True, largest corrected p 1.7e-09
1959	LGN: ratio 0.957, widened CI [0.837, 0.98], match True; p 0.0025 (corrected 0.0029); units 61 against 60
1960	LP: ratio 0.900, widened CI [0.765, 0.96], match True; p 0.0045 (corrected 0.0045); units 17 against 16
1961	             O1    O2  blanks  blocks  ex_min  ex_max    LGN     LP
1962	0        pooled   geo    hold  within   0.891   0.930  0.957  0.900
1963	1        pooled  mean    hold  within   0.898   0.937  0.962  0.907
1964	2       per_ori   geo    hold  within   0.855   0.878  0.960  0.903
1965	3       per_ori  mean    hold  within   0.863   0.887  0.966  0.910
1966	4   per_ori_geo   geo    hold  within   0.782   0.828  0.945  0.893
1967	5   per_ori_geo  mean    hold  within   0.800   0.841  0.953  0.899
[... 367 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np, importlib
for m in ['statsmodels','pingouin','scipy','remfile','h5py']:
    try: importlib.import_module(m); print(m,'ok')
    except Exception as e: print(m,'missing')
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, importlib
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls ~/.venv* /opt 2>/dev/null; which -a python3 python; pip --version 2>&1; uv --version 2>&1
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
pipx
pipx_bin
post-generation
primer
runner-cache
volume-initializer
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/python
/usr/bin/python
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -m venv $TMPDIR/v && $TMPDIR/v/bin/pip -q install numpy scipy pandas statsmodels pingouin h5py 2>&1 | tail -2; $TMPDIR/v/bin/python -c "import numpy, pingouin; print('ok')"
```

```
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: /tmp/claude-1001/v/bin/python3 -m pip install --upgrade pip
ok
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/t.py <<'EOF'
import sys, types
sys.modules['remfile']=types.ModuleType('remfile')
sys.path.insert(0,'.')
import numpy as np, pandas as pd, pingouin as pg
from statsmodels.stats.multitest import multipletests
import adaptation as A
rng=np.random.default_rng(0)
# FDR
p=rng.uniform(0,0.1,20)
print('fdr max diff', np.abs(A.fdr(p)[0]-multipletests(p,method='fdr_bh')[1]).max())
# mixed anova unbalanced
N=[40,35,25]; Y=[];g=[]
for i,n in enumerate(N):
    Y.append(rng.normal(0,1,(n,3))+np.array([0,0.2*i,0.5*i])+rng.normal(0,1,(n,1))); g+= [i]*n
Y=np.vstack(Y); g=np.array(g)
r=A.mixed_anova(Y,g)
df=pd.DataFrame(dict(y=Y.ravel(), subj=np.repeat(np.arange(len(Y)),3), rel=np.tile([0,1,2],len(Y)), grp=np.repeat(g,3)))
a=pg.mixed_anova(df,dv='y',within='rel',between='grp',subject='subj',correction=False)
print({k:(round(v[0],4),v[1]) for k,v in r.items()}); print(a[['Source','F','p_unc']])
# pair masks / nback on synthetic sequence with known adaptation
ori=np.array([0,0,90,np.nan,90,0,45,135,45])
blk=np.array([0,0,0,0,0,1,1,1,1])
rep,orth,bl=A.pair_masks(ori,blk,1)
print('rep',rep.astype(int),'orth',orth.astype(int),'blank',bl.astype(int))
# simulate neuron with 1-back repeat reduction 0.8, deterministic, check ratio at n=1 recovers 0.8
L=600; o=rng.choice([0,45,90,135],L).astype(float); o[rng.choice(L,30,replace=False)]=np.nan
tab=pd.DataFrame(dict(start_time=np.arange(L)*3.0, orientation=o, stimulus_block=np.repeat([0,1,2],200)))
ori_,blk_,order=A.sequence(tab,None)
r1,_,_=A.pair_masks(ori_,blk_,1); rep1=np.r_[False,r1]
c=np.where(rep1,8.0,10.0)[None,:]
nb,_=A.nback_rates(c,tab,5)
for h in ['pooled','per_ori','per_ori_geo']: print(h, np.round(A.ratios(nb,h)[0],4))
# fit recovery
n=np.arange(1,51.)
y=np.log(A.model_double(n,0.14,0.85,0.035,6.8))
d,s=A.fit_models(y); print('fit',np.round(d[0],4), 'single',np.round(s[0],4))
EOF
$TMPDIR/v/bin/python $TMPDIR/t.py
```

```
fdr max diff 1.3877787807814457e-17
{'within': (np.float64(2.366), np.float64(0.09656007635110875)), 'interaction': (np.float64(4.5684), np.float64(0.0015088783426900714)), 'between': (np.float64(1.5102), np.float64(0.22600379559613393))}
        Source         F     p_unc
0          grp  1.510240  0.226004
1          rel  2.365984  0.096560
2  Interaction  4.568437  0.001509
rep [1 0 0 0 0 0 0 0] orth [0 1 0 0 0 0 1 1] blank [0 0 0 1 0 0 0 0]
pooled [0.8    1.0037 1.0056 1.0052 0.9953]
per_ori [0.8    1.0049 1.009  1.0053 0.9961]
per_ori_geo [0.8    1.0042 1.0082 1.0051 0.996 ]
fit [0.14  0.85  0.035 6.8  ] single [0.1709 1.4407]
```

**Agent calls Bash**

```bash
cd  grep -n -i -E "invalid|AllenSDK|subsampl|randomly|blank|noise|simulat" paper/*.txt | cut -c1-600
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '229p;248p;289,291p;321p;327p' paper/*.txt | cut -c1-2500
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i -A12 "^Table 1" paper/*.txt | cut -c1-1500 | head -60
```

Result: not kept, because it reads the paper's text.

**Agent**

**A. Outcomes**

The claims file holds 31 claims, and the notebook tests all 31; none is treated as blocked. My outcomes: 26 reproduced, 3 partially reproduced, 2 not reproduced.

| Claim | Outcome | Reason |
|---|---|---|
| units-responsive-count | reproduced | Cell 14, reading ace with `good` units only: total 2422, V1 580, LGN 142, LP 91, all within tolerance, and the 8 named regions are kept. Reading ade without the `good` filter also passes. |
| fig1d-v1-1back | reproduced | Cell 19: V1 ratio 0.821, inside [0.81, 0.84]; p = 6e-58 (FDR 2.4e-57); 580 units. |
| fig1d-extrastriate-1back | reproduced | Cell 21: ratios 0.795 to 0.876, all in [0.72, 0.968]; largest FDR p 2e-24. |
| fig1d-thalamus-1back | reproduced | Cell 23: LGN 0.935 (CI [0.91, 0.96]), p 6.7e-7; LP 0.833 (CI [0.79, 0.88]), p 1.7e-10. |
| fig1e-consistent-across-mice | partially_reproduced | Cell 26: cortex 32/32 mice meet (a). Thalamus 21/23 fails (a), but the sign test passes (p 6.6e-5), so only (b) holds there. The criterion makes that partial. |
| fig2-v1-tuning-main-effect | reproduced | Cell 29: main effect p 3.1e-9 (log ratios, 45° pooled) and p < 1e-9 in all four readings; the 0° ratio is lowest (0.799 < 0.875 < 0.927). |
| fig2-v1-tuning-interaction | reproduced | Cell 31: interaction p 0.011 (log) to 6e-7 (ratio). The spread across orientations is largest in the high-OSI tertile (0.248, against 0.057 and 0.125). |
| fig2-v1-adaptation-at-all-orientations | reproduced | Cell 33, 45° pooled with BH over the 9 V1 cells or over all 72 cells: 8/8 cells below 1, and the high-OSI 90° cell has p 0.92 (ratio 0.993). |
| fig2-thalamus-no-tuning-dependence | reproduced | Cell 35: no main effect or interaction is significant under any reading (LGN p_rel 0.073 to 0.28; LP ≥ 0.66). |
| fig3a-v1-long-term | reproduced | Cell 38, main reading: significant at 1 to 8, 8-back FDR p 0.022, 9-back p 0.09. |
| fig3a-v1-double-exponential | reproduced | Cell 41: a_fast 14.21, tau_fast 0.816, a_slow 3.755, tau_slow 6.714, all inside the Table 1 CIs (sign reading a). |
| fig3a-v1-half-life | reproduced | Cell 43: 6.714 trials × 3 s × ln 2 = 13.96 s, within 14 ± 1.4 s. |
| fig4-cumulative-adaptation | reproduced | Cell 45, main reading: 1-back reduction 17.88% (target 17 ± 1.7), 2- to 8-back 20.36% (target 19 ± 1.9), and the cumulative value is larger. |
| fig4b-linear-accumulation | reproduced | Cell 48, baseline (c): all 7 predicted values fall inside the bootstrap CIs, under seed +0 and 4 other seeds. Baseline (d) fails at pair 1-2. |
| fig3b-thalamus-short-term | reproduced (fragile) | Cell 50: the main reading fails because RL's largest significant n is 5. Only the pooled/hold/across reading passes (RL 6, LGN 1, LP 2). See problem 1. |
| v1-vs-thalamus-welch | reproduced | Cell 52: with region normalization over n 2 to 10, V1 > LGN at exactly 2, 4, 9 and V1 > LP at 3. The unnormalized test also passes all four. |
| fig3c-mice-long-term | reproduced | Cell 54: cortex 31/32 mice, sign test p 1.5e-8, so (b) holds. Thalamus 14/23, p 0.4, so neither (a) nor (b) holds. |
| decay-cortex-double-better | reproduced | Cell 56: F test p < 0.05 in V1, LM, AL, PM and AM under both F variants; RL p 0.22, as in the paper. |
| table1-extrastriate-tau-slow | reproduced | Cell 58: all 5 extrastriate tau_slow inside the Table 1 CIs; the six bootstrap CIs overlap under all 5 seeds; V1 has the largest tau_slow. The other Table 1 parameters are also inside their CIs. |
| decay-thalamus-single | reproduced | Cell 60: F test p 0.81 (LGN) and 0.57 (LP). LGN tau 0.031, a 6.48%; LP tau 0.712, a 16.85%; all inside their CIs. |
| fig5-repeat-suppression | not_reproduced | Cell 63: orthogonal/blank at 2-back is below 1 under both readings, every seed and the 100-draw average (0.972, CI [0.957, 0.986], FDR p 9e-4). The criterion forbids that. The repeat/blank 8-back value is also not significant under the claim's seed. |
| fig6c-static-v1-1back | reproduced | Cell 65: ratio 0.897, in [0.89, 0.91]; p 4e-85; 545 units (target 530 ± 53). |
| fig6c-static-other-areas-1back | reproduced | Cell 67: extrastriate 0.891 to 0.930; LGN 0.957 (p 0.0025, 61 units); LP 0.900 (p 0.0045, 17 units). All match under the widened rule. |
| fig6d-static-consistent-across-mice | partially_reproduced | Cell 69: cortex 32/32 mice; thalamus 15/17 (sign test p 0.0023), so only (b) holds there. |
| fig7a-static-v1-long-term | reproduced | Cell 71, FDR family 1 to 20: 20-back is significant and is the largest significant n. All four Table 2 estimates are inside their CIs (tau_slow 9.47). |
| fig7b-static-cortex-decay | reproduced | Cell 73: every F test p ≤ 1.4e-5; all 5 extrastriate tau_slow inside the Table 2 CIs; the CIs overlap. |
| fig7-static-lgn-single | reproduced | Cell 75: F test p 0.20; tau 2.77 in [1.36, 7.32]; a 4.00% in [1.80, 6.59]. |
| fig7b-static-areas-long-term | reproduced | Cell 77, family 1 to 20 with reading (c): V1, AL, PM and AM reach 20. The thalamus (5 and 9) is below every cortical area (smallest 15). See problem 4. |
| fig7c-static-long-term-across-mice | partially_reproduced | Cell 79: cortex 30/32 and V1 29/32 mice, sign test p ≤ 2.6e-6, so only (b) holds. Read as fig1e's rule requires, that is partial. A looser reading ("holds" as in fig3c) would make it reproduced. |
| fig8-no-spurious-long-term | not_reproduced | Cell 81: under the claim's seed, no reading meets the full rule or the partial rule. The Poisson static run excludes 1 at 5- and 6-back (0.986, 0.987); the no-noise drifting run excludes 1 at 2- and 6-back (0.996, 1.003). Only seed +1000 of five passes, under (a, c). See problem 2. |
| robust-threshold-preferred-window | reproduced | Cell 83: all 7 variants meet the reading (V1 significant beyond 1-back, double exponential better, LGN no later than 2). |

**B. Problems**

1. [affects a conclusion] **fig3b, cells 37 and 50.** The claim passes only under the pooled/hold/across reading. Every other claim uses hold/within. That passing reading has RL at exactly the threshold of 6. `nback_tests` counts an n as significant only when the ratio is below 1. Under that same reading, LGN 9-back is significant with a ratio above 1 (`LGN_any [1, 9]`). If two-tailed significance in either direction counts, as the paper's black borders likely do, the outcome drops to partially reproduced.
2. [affects a conclusion] **fig8, cell 81, and the claims file.** The paper says the simulated points are "centered on an adaptation ratio of one". The claims file turns that into "every CI over 9 or 49 n contains 1", which noise alone breaks: about 0.45 exclusions are expected per stimulus set over 9 n, and about 2.5 over 49 n. That fits the 1 seed in 5 that passes. Every excluded ratio is within 0.015 of 1 (empirical V1 2-back: 0.918). The not_reproduced outcome therefore comes from the claims file's misreading of the paper, not from the data. The notebook checked the partial rule on seed +0 only.
3. [does not affect a conclusion] **fig5, cell 62.** The unit bootstrap and t tests treat units as independent, but within a session they share one trial subsample, so the CIs are too narrow. The orthogonal/blank 2-back failure persists in the 100-draw average, so the outcome holds either way.
4. [does not affect a conclusion] **fig7a and fig7b-static-areas, cells 71 and 77.** With the 1-to-20 family, the largest significant n cannot exceed 20, so the 18-to-22 test is partly met by construction. With 1 to 50, isolated late n are significant (V1: 26, 41, 46, 49). That points to scattered significance, or anticonservative tests, rather than a clean bound at 20. This is the claims file's reading, reported here, not corrected.
5. [does not affect a conclusion] **Fig. 2, `tuning_cells` in cell 28.** OSI tertiles are assigned before units with a non-finite log ratio in any cell are dropped. V1 loses 78 units, mostly from the high-OSI tertile (116 left, against 194 and 192). That shifts the composition of the critical high-OSI 90° cell.
6. [does not affect a conclusion] **Unit selection, cells 12 and 15.** The main O4 reading was picked by matching the paper's counts, which "under one reading" allows, and is then used consistently. The `noise`-label filter is an assumption beyond the Methods' three metrics. It is reasonable (AllenSDK's `filter_by_validity` does this), and cell 17 shows the results are unchanged without it.
7. [does not affect a conclusion] **`invalid_times`, cells 6 and 10.** These intervals are not applied, though they overlap the grating epochs in several sessions (e.g. 715093703: 4 drifting, 4 static). The paper is silent on them, and whether the AllenSDK would drop those presentations was not checked.
8. [does not affect a conclusion] **`adaptation._boot_task`.** It does not pass `sign`, so every bootstrap uses sign −1. That is harmless here, because reading (a) is the one used.

I tested the helpers on synthetic inputs:
- `fdr` matches statsmodels' BH to 1e-17.
- `mixed_anova` matches pingouin's `mixed_anova` exactly on unbalanced groups.
- `pair_masks` handles blanks and block boundaries correctly.
- `nback_rates` / `ratios` recover a planted 1-back ratio of 0.8 exactly.
- `fit_models` recovers planted double-exponential parameters exactly.
- The hard-coded Table 1 CIs match the paper's text.

**C. What I could not check, and which output would settle it**

- **Effect of `invalid_times`.** The 1-back ratios and unit counts recomputed with presentations inside invalid intervals excluded.
- **Fig. 2 drop pattern.** Units dropped per tertile × relative-orientation cell, and the high-OSI 90° t test with zero-count units kept on the ratio scale.
- **fig3b direction.** The LGN 9-back ratio and p value under pooled/hold/across, and a two-sided significance column per area for every reading.
- **fig8 seed dependence.** The fraction of, say, 200 Poisson seeds meeting each reading, and the number of exclusions expected by chance.
- **fig1e, fig6d, fig7c.** Thalamic unit counts for each mouse that fails reading (a).
- **fig5 clustering.** A session-level (cluster) bootstrap for the orthogonal/blank 2-back value.
- **The authors' choices.** I could not check their actual readings of O1 to O5: the paper's code (doi:10.34973/kpt9-y956) is restricted, and figure values were not available.

## End of run

18 turns, 5 minutes, $1.93 at API prices, result: success.
