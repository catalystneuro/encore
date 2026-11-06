# crcns-ssc-3 · verifier-1 · run 42233525780

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 552
drwxr-xr-x 6 runner runner    4096 Nov  6 14:48 .
drwxr-xr-x 7 runner runner    4096 Nov  6 14:48 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  6 14:22 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  6 14:22 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  6 14:48 .claude
-rw-r--r-- 1 runner runner       0 Nov  6 14:48 .env
-rw-r--r-- 1 runner runner       0 Nov  6 14:48 .env.development
-rw-r--r-- 1 runner runner       0 Nov  6 14:48 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  6 14:48 .env.local
-rw-r--r-- 1 runner runner       0 Nov  6 14:48 .env.production
-rw-r--r-- 1 runner runner       0 Nov  6 14:48 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  6 14:48 .env.test
-rw-r--r-- 1 runner runner       0 Nov  6 14:48 .env.test.local
drwx------ 2 runner runner    4096 Nov  6 14:48 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  6 14:22 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  6 14:22 .github
-rw-r--r-- 1 runner runner       0 Nov  6 14:48 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  6 14:22 .idea
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1371-journal.pcbi.1004858.yaml
```

```
<persisted-output>
Output too large (30.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/d8f40f84-ed43-4617-b2e4-e04481222580/tool-results/b04ujtot3.txt

Preview (first 2KB):
# Claims for Timme, Ito, Myroshnychenko, Nigam, Shimono, Yeh, Hottowy, Litke & Beggs (2016),
# "High-Degree Neurons Feed Cortical Computations", PLoS Comput Biol 12(5), e1004858, on CRCNS ssc-3.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
# protocol as stated in docs/protocol.md (version pilot-13), Reader steps 1 to 4.
#
# Text read: the version of record, PMC4861348 (Europe PMC full-text XML, flattened), with its
# Materials and Methods, Results, Discussion, the legends of Figures 1 to 7, Table 1 and the legend
# of S1 Fig (the only supplement; it is a figure, so only its legend is text). No PDF was supplied,
# so no figure could be read. The flattened text has lost every displayed equation (Eqs 1 to 24).
# The information measures (Eqs 1 to 12) are described in words well enough to be rebuilt, and
# each criterion says how it reads them. The feedforward model is not: the binary-signal currents
# (Eqs 16 to 19), the form of the rewiring score (Eq 20) and the fitted score equations (Eqs 22 to
# 24) are given only as equations. The model claims below need these equations read from the
# version of record before they can be tested. Values shown only in figures (the binomial skew
# probabilities of Fig 5A and 5B, the fitted exponents and their 95% ranges in Fig 6, the means in
# Fig 7C and 7D) could not be read and are not claimed as numbers.
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/d8f40f84-ed43-4617-b2e4-e04481222580/tool-results/b04ujtot3.txt"
}
```

```
1	# Claims for Timme, Ito, Myroshnychenko, Nigam, Shimono, Yeh, Hottowy, Litke & Beggs (2016),
2	# "High-Degree Neurons Feed Cortical Computations", PLoS Comput Biol 12(5), e1004858, on CRCNS ssc-3.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
4	# protocol as stated in docs/protocol.md (version pilot-13), Reader steps 1 to 4.
5	#
6	# Text read: the version of record, PMC4861348 (Europe PMC full-text XML, flattened), with its
7	# Materials and Methods, Results, Discussion, the legends of Figures 1 to 7, Table 1 and the legend
8	# of S1 Fig (the only supplement; it is a figure, so only its legend is text). No PDF was supplied,
9	# so no figure could be read. The flattened text has lost every displayed equation (Eqs 1 to 24).
10	# The information measures (Eqs 1 to 12) are described in words well enough to be rebuilt, and
11	# each criterion says how it reads them. The feedforward model is not: the binary-signal currents
12	# (Eqs 16 to 19), the form of the rewiring score (Eq 20) and the fitted score equations (Eqs 22 to
13	# 24) are given only as equations. The model claims below need these equations read from the
14	# version of record before they can be tested. Values shown only in figures (the binomial skew
15	# probabilities of Fig 5A and 5B, the fitted exponents and their 95% ranges in Fig 6, the means in
16	# Fig 7C and 7D) could not be read and are not claimed as numbers.
17	#
18	# Code read: none. The paper links no analysis or model code. Its Data Availability names the
19	# deposit "http://dx.doi.org/10.6080/K07D2S2F" at CRCNS, which is ssc-3. The data descriptor
20	# (ssc-3 data description, version 0.8) was read only to know what the dataset holds; no claim
[... 366 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_timme_2016.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('ERR',o['ename'],o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1191 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	==================== 0 markdown
2	# Reproducing Timme et al. (2016) from CRCNS ssc-3
3	
4	**Paper.** Timme NM, Ito S, Myroshnychenko M, Nigam S, Shimono M, Yeh F-C, Hottowy P, Litke AM,
5	Beggs JM (2016). High-degree neurons feed cortical computations. *PLoS Comput Biol* 12(5): e1004858.
6	[doi:10.1371/journal.pcbi.1004858](https://doi.org/10.1371/journal.pcbi.1004858). The claims file
7	was written from the version of record (PMC4861348, Europe PMC full text). Its displayed
8	equations, missing from that flattened text, were read from the version of record's JATS XML.
9	The TE procedure the paper reuses is that of its reference [44], Timme et al. (2014), PLoS One 9:
10	e115764 (PMC4275261).
11	
12	**Data set.** [CRCNS ssc-3](https://doi.org/10.6080/K07D2S2F), `ssc-3/live/data.tar.gz` in the public
13	CRCNS bucket, streamed and decompressed in memory. CRCNS data sets are not versioned, so the version
14	is recorded as `unversioned`; the paper cites the data set by its DOI and no version, and this is
15	the only copy the bucket holds (`ssc-3/live/`, no `old/`). The MD5 sum of the archive, from the data
16	set's `checksums.md5`, is `1a5bd3d304c5442290a7c9c1f1b5def6`; the loading cell checks the streamed
17	bytes against it. The archive holds 25 MATLAB files, one per recording.
18	
19	**Claims.**
20	
[... 714 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 735
}
```

```
735	  (f, r): True
736	  (s, p): True
737	  (s, r): True
738	
739	==================== 24 markdown
740	## fig5cd-pooled-trends
741	
742	> Pooled over all neuron groups and recordings, synergy shows no trend with receiver in-degree and
743	> rises with transmitter out-degree, at both time scales.
744	==================== 25 code
745	rows = []
746	for reading in ["s", "f"]:
747	    for scale in hdn.TIME_SCALES:
748	        parts = [triple_data(scale, r["name"], reading) for r in recs]
749	        for panel in ["in", "out"]:
750	            x = np.concatenate([p[0] if panel == "in" else p[2] for p in parts])
751	            y = np.concatenate([p[1] if panel == "in" else p[3] for p in parts])
752	            d = pd.DataFrame({"deg": x, "syn": y}).groupby("deg").syn.agg(["count", "median"])
753	            d = d[d["count"] >= 20]
754	            rho, p = stats.spearmanr(d.index, d["median"]) if len(d) > 2 else (np.nan, np.nan)
[... 438 more lines not kept]
```

**Agent**

I've read the claims file and the executed notebook. Next I'm reading the helper module `hdn.py`.

**Agent calls Read**

```json
{
 "file_path": "hdn.py"
}
```

```
1	"""Loading and measures for CRCNS ssc-3, as used by Timme et al. (2016).
2	
3	Timme NM, Ito S, Myroshnychenko M, Nigam S, Shimono M, Yeh F-C, Hottowy P, Litke AM, Beggs JM
4	(2016). High-degree neurons feed cortical computations. PLoS Comput Biol 12(5): e1004858,
5	doi:10.1371/journal.pcbi.1004858. Data: CRCNS ssc-3, doi:10.6080/K07D2S2F.
6	
7	The data set is one archive, `ssc-3/live/data.tar.gz` in the public CRCNS bucket, holding 25
8	MATLAB files (`data/DataSet<n>.mat`), each with a structure `data`: spike times per neuron in
9	ms (`spikes`), `nNeurons`, `recordinglength` (ms), neuron positions `x` and `y` (um) and a
10	`recordingID`. CRCNS data sets are not versioned; the MD5 sum of the archive from the data set's
11	`checksums.md5` is `DATA_MD5`, and `load_all` checks the bytes it streamed against it. The archive
12	is streamed and decompressed in memory; nothing is written to disk.
13	
14	Where each parameter comes from. "Paper" is the version of record (PMC4861348); its displayed
15	equations, lost from the flattened text under paper/, were read from the version of record's
16	JATS XML (Europe PMC). "[44]" is Timme et al. (2014), PLoS One 9: e115764 (PMC4275261), whose TE
17	networks the paper says it reused ("The complete procedure for the TE analysis is described in
18	[44]", Methods, Effective Connectivity Detection, paragraph 1; "we used these same TE networks",
19	paragraph 4).
20	
[... 888 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "import numba, numpy, scipy; print(numba.__version__)"; grep -n -i -E "significant connections|connections per|density|average degree|total degree|number of connections" paper/10.1371-journal.pcbi.1004858.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent**

`numba` isn't installed, so I'll stub it (njit as a no-op, prange as range) and run `te_network` in pure Python on synthetic trains.

**Agent calls Bash**

```bash
cd  mkdir -p $TMPDIR/stub/numba; cat > $TMPDIR/stub/numba/__init__.py <<'EOF'
def njit(*a, **k):
    if a and callable(a[0]): return a[0]
    return lambda f: f
prange = range
class typed:
    List = list
EOF
mkdir -p $TMPDIR/stub/fsspec; echo "" > $TMPDIR/stub/fsspec/__init__.py
cat > $TMPDIR/t.py <<'EOF'
import numpy as np, hdn
rng=np.random.default_rng(0)
T=20000
# receiver: spikes in first half only; sender: spikes in second half only -> jitter never touches receiver
r=np.sort(rng.choice(np.arange(0,9000),300,replace=False))
s=np.sort(rng.choice(np.arange(11000,19990),300,replace=False))
# independent pair
r2=np.sort(rng.choice(T,300,replace=False)); s2=np.sort(rng.choice(T,300,replace=False))
for name,(a,b) in {"disjoint":(s,r),"independent":(s2,r2)}.items():
    trains=[np.unique(a).astype(np.int64),np.unique(b).astype(np.int64)]
    te,nte,ran,ex=hdn.te_network(trains,T,5000,5,1,10**9)
    print(name,"TE s->r",te[0,1],"surrogates run",ran[0,1],"exceed",ex[0,1],"significant",hdn.significant(ex)[0,1])
# independent many pairs: false positive rate
fp=0;n=0
for i in range(40):
    r2=np.sort(rng.choice(T,200,replace=False)); s2=np.sort(rng.choice(T,200,replace=False))
    te,nte,ran,ex=hdn.te_network([s2.astype(np.int64),r2.astype(np.int64)],T,1000,5,i+2,10**9)
    sg=hdn.significant(ex); fp+=sg.sum(); n+=2
print("independent pairs significant (1000 surr, <5 exceed => p<0.005):",fp,"of",n)
EOF
PYTHONPATH=$TMPDIR/stub:. timeout 3000 python3 $TMPDIR/t.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t.py", line 1, in <module>
    import numpy as np, hdn
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls .claude; which -a python python3; ls ~/.venv* /opt 2>/dev/null | head; uv --version 2>/dev/null; pip --version 2>/dev/null
```

```
agents
commands
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/usr/bin/python3
/bin/python3
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
uv 0.13.7 (x86_64-unknown-linux-gnu)
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
for p in /usr/bin/python3; do $p -c "import numpy, scipy; print(numpy.__version__)"; done; cd $TMPDIR && uv venv -q v && uv pip install -q -p v/bin/python numpy scipy 2>&1 | tail -2; v/bin/python -c "import numpy;print(numpy.__version__)"
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy, scipy; print(numpy.__version__)
    ^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'numpy'
2.5.4
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  PYTHONPATH=$TMPDIR/stub:. timeout 3000 $TMPDIR/v/bin/python $TMPDIR/t.py
```

```
Exit code 1
hdn.py:245: RuntimeWarning: overflow encountered in scalar add
  P1 += rP[t]
hdn.py:244: RuntimeWarning: overflow encountered in scalar add
  R1 += rF[t]
Traceback (most recent call last):
  File "/tmp/claude-1001/t.py", line 11, in <module>
    te,nte,ran,ex=hdn.te_network(trains,T,5000,5,1,10**9)
                  ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "hdn.py", line 281, in te_network
    real = te_from_counts(N, R1, P1, RP, S1[s], a, b, c)
  File "hdn.py", line 168, in te_from_counts
    n_ps, n1 = N - P1 - S1 + b, (R1 - RP) - (a - c)
               ~~^~~~
OverflowError: Python integer 19997 out of bounds for uint8
```

**Agent**

The overflow comes from running pure Python on uint8 arrays; numba would promote these sums to int64. For the test I'll use a copy of `hdn.py` with int64 arrays, which behaves the same way.

**Agent calls Bash**

```bash
cd  mkdir -p $TMPDIR/h; sed 's/np\.uint8)/np.int64)/g' hdn.py > $TMPDIR/h/hdn.py; PYTHONPATH=$TMPDIR/stub:$TMPDIR/h timeout 3000 $TMPDIR/v/bin/python $TMPDIR/t.py
```

```
/tmp/claude-1001/h/hdn.py:187: RuntimeWarning: overflow encountered in scalar multiply
  return x * np.uint64(2685821657736338717)
disjoint TE s->r 0.0006236665635967392 surrogates run 5000 exceed 0 significant True
independent TE s->r 3.216929075577577e-05 surrogates run 7 exceed 5 significant False
independent pairs significant (1000 surr, <5 exceed => p<0.005): 0 of 80
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/t2.py <<'EOF'
import numpy as np, hdn, warnings
warnings.filterwarnings("ignore")
rng=np.random.default_rng(1)
T=400000   # ~640 s of 1.6 ms bins
res=[]
for i in range(150):
    r=np.unique(rng.choice(T,1300,replace=False)).astype(np.int64)   # ~2 Hz
    s=np.unique(rng.choice(T,18,replace=False)).astype(np.int64)     # ~0.028 Hz, i.e. 100 spikes/h scaled
    te,nte,ran,ex=hdn.te_network([s,r],T,5000,5,i+3,10**9)
    res.append((ex[0,1]<5, ran[0,1], te[0,1]))
sig=np.array([x[0] for x in res]); ran=np.array([x[1] for x in res])
print("independent sparse sender->receiver significant:",sig.sum(),"of",len(sig))
print("of those, surrogates all run (no exceedance at all):",(sig&(ran==5000)).sum())
EOF
PYTHONPATH=$TMPDIR/stub:$TMPDIR/h timeout 6000 $TMPDIR/v/bin/python $TMPDIR/t2.py
```

```
independent sparse sender->receiver significant: 91 of 150
of those, surrogates all run (no exceedance at all): 91
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/t3.py <<'EOF'
import numpy as np, hdn, warnings
warnings.filterwarnings("ignore")
rng=np.random.default_rng(2)
T=400000
for ns in [18, 90, 360]:
  for nr in [130, 1300]:
    sig=0; n=40
    for i in range(n):
        r=np.unique(rng.choice(T,nr,replace=False)).astype(np.int64)
        s=np.unique(rng.choice(T,ns,replace=False)).astype(np.int64)
        te,nte,ran,ex=hdn.te_network([s,r],T,5000,5,1000+i,50)
        sig+=ex[0,1]<5
    print(f"sender {ns/T/0.0016:.2f} Hz, receiver {nr/T/0.0016:.2f} Hz: significant {sig}/{n}")
EOF
PYTHONPATH=$TMPDIR/stub:$TMPDIR/h timeout 6000 $TMPDIR/v/bin/python $TMPDIR/t3.py
```

```
sender 0.03 Hz, receiver 0.20 Hz: significant 38/40
sender 0.03 Hz, receiver 2.03 Hz: significant 25/40
sender 0.14 Hz, receiver 0.20 Hz: significant 34/40
sender 0.14 Hz, receiver 2.03 Hz: significant 5/40
sender 0.56 Hz, receiver 0.20 Hz: significant 14/40
sender 0.56 Hz, receiver 2.03 Hz: significant 1/40
```

**Agent calls Bash**

```bash
cd  sed -n 530,566p paper/10.1371-journal.pcbi.1004858.txt | cut -c1-3000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/t4.py <<'EOF'
import numpy as np, hdn, warnings
warnings.filterwarnings("ignore")
a,b=hdn.sigmoid_params(20)
for rule in ["random","hebbian","degree","firing_rate"]:
    rng=np.random.default_rng(5)
    conn=hdn.build_models(20,rule,rng,a,b,n_models=15)
    out=[]
    for runs in [2000, 50000]:
        d=hdn.model_correlations(conn,np.random.default_rng(9),a,b,runs)
        out.append((np.mean([x["mi"] for x in d]), np.mean([x["mi_given_b"] for x in d])))
    print(rule, "2000 runs: mi %.4f mi|b %.5f   50000 runs: mi %.4f mi|b %.5f" % (*out[0],*out[1]))
EOF
PYTHONPATH=$TMPDIR/stub:$TMPDIR/h timeout 6000 $TMPDIR/v/bin/python $TMPDIR/t4.py
```

```
random 2000 runs: mi 0.0230 mi|b 0.00223   50000 runs: mi 0.0226 mi|b 0.00159
hebbian 2000 runs: mi 0.0889 mi|b 0.00162   50000 runs: mi 0.0893 mi|b 0.00095
degree 2000 runs: mi 0.0307 mi|b 0.00159   50000 runs: mi 0.0307 mi|b 0.00085
firing_rate 2000 runs: mi 0.0709 mi|b 0.00166   50000 runs: mi 0.0704 mi|b 0.00096
```

**Agent**

**A. Outcomes**

None of the 14 claims is blocked. I take reading (s) (sub-networks) as primary, because the claims file says the paper's stated purpose supports it (M-SUB). Every data outcome below from fig4ac to fig6 depends on the significance test in problem 1, which I found to be anti-conservative.

| Claim | Outcome | Reason |
|---|---|---|
| data-recordings | reproduced | Cell 6 gives 25 recordings, 7735 neurons, 309.4 per recording, and 2.103 Hz (over 60 min) or 2.132 Hz (over recording length). All four are within tolerance, and the deposit already applies the 100-spike threshold. |
| fig4ac-te-lognormal | not_reproduced | Cell 12: the fit on the average distribution has R² of 0.08 to 0.61, against the 0.9 required, under both (f) and (s). The spread criterion passes. The low-TE mode (minimum 1.3e-9 bits, fitted σ of about 3 decades) is very likely spurious connections from problem 1, so this outcome is unreliable. |
| fig4bd-heavy-tailed-degree | reproduced (unreliable) | Cell 15: 21% (f) and 6% (s) of neurons lie above the random 99.9th percentile, against the 1% threshold, and the real maxima are well above the random ones. Problem 1 adds connections that depend on firing rate, which may shape the tail. |
| fig4bd-out-tail-longer | partially_reproduced | Cell 18: passes under (s) at both scales. Under (f) at 3.5–14 ms the largest in-degree (480) exceeds the largest out-degree (449). The Wilcoxon test is p ≤ 0.0015 everywhere. |
| fig5a-in-degree-uncorrelated | partially_reproduced | Cell 20, (s): 9 positive vs 41 negative (Pearson, binomial p = 2.8e-6) and 10 vs 40 (Spearman), so a significant negative skew, which the criterion grades as partial. Only (f, Spearman) is non-significant (20 vs 30, p = 0.10). The notebook has 50 correlations per panel; the paper has 40. |
| fig5b-out-degree-positive | reproduced | Cell 20, (s): 44/50 positive (p = 1.6e-8) and 39/50 (p = 4.5e-5). Under (f), Pearson is 35/50 (p = 0.003) and Spearman 26/50 (not significant). |
| fig5ab-correlations-beyond-null | reproduced | Cell 23: under (s), 94% to 100% of correlations lie beyond the null's 99th percentile. Under (f, Pearson) the in-degree panel is 84%, which fails. |
| fig5cd-pooled-trends | not_reproduced | Cell 25, (s): out-degree at 3.5–14 ms has ρ = 0.14 (p = 0.34). In-degree medians fall steeply (ρ = −0.96 and −0.94), which contradicts "no trend" even though the criterion only forbids a positive trend. Under (f), out-degree at 1.6–6.4 ms is negative. |
| fig6-information-gain-not-rising | reproduced | Cell 27: k < 0 at both scales under every reading of normalization and starting n, with no interval above zero. This was run only under (f), with sampled receivers and combinations. |
| table1-pid-examples | reproduced | Cell 29: all four checks are True. For example, synergy in the synergistic-and-redundant example is 0.4569 with II = 0.0001, and in the single-and-redundant example \|II\| = redundancy = 0.2502. |
| fig7b-connectivity-patterns | reproduced | Cell 33: upper-half fraction is 0.988 (Hebbian), 0.79 (firing rate) and 0.505 (degree). |
| fig7c-degree-modified-rule-matches | partially_reproduced | Cell 32: under (s) both modified rules match and the Hebbian and random rules do not. The firing-rate rule is nearer the real data than the degree rule (0.111 vs 0.169 for Pearson, 0.065 vs 0.142 for Spearman), so "degree-modified more closely" fails. The full criterion passes only under (f, Spearman). |
| fig7d-degree-rule-highest-conditioned-mi | not_reproduced | Cell 34: Hebbian has the highest unconditioned MI, but the random model has the highest conditioned MI (0.0023) and the degree rule the lowest (0.00153). I reran a few models at 50,000 runs and the ranking holds, so this is not estimator bias. |
| figs1-larger-model | not_reproduced | Cell 35, under both α/β readings: the degree rule's conditioned MI is below the random model's. The Hebbian and firing-rate conditioned MI are smaller at N = 40 than at N = 20, the opposite of the claim. |

**B. Problems**

1. **[affects a conclusion]** `hdn.te_network` / `significant`: the jitter test counts a surrogate only if its TE is strictly greater than the real TE. When jitter cannot change the counts, every surrogate ties and the pair is called significant. This happens when no sender spike falls near receiver activity, or when all relevant spikes are "same". I ran the helper on synthetic independent Poisson pairs (numba stubbed out):
   - Sender 0.03 Hz, receiver 0.2 Hz: 38/40 significant.
   - Sender 0.03 Hz, receiver 2 Hz: 25/40 significant (91/150 in a larger run, all with zero exceedances in 5000 surrogates).
   - Sender 0.14 Hz, receiver 2 Hz: 5/40.
   - Sender 0.56 Hz, receiver 2 Hz: 1/40.
   - Two disjoint trains were "significant" with TE of 6e-4 bits.

   The nominal rate is 0.001. This likely explains the densities of 2–33% (cell 9; the notebook's "expected_by_chance" of 0.1% does not hold), the log-TE mode near 1e-9 to 1e-8 bits that breaks the fig4ac fit, and rate-driven degrees feeding fig4bd through fig6. The cell 8 exact-vs-approximate check cannot catch this, because both versions share the tie rule.
2. **[affects a conclusion]** `PAST_BINS = (2, 3)`: the docstring says [44] is internally inconsistent. Its text gives bins t−1 and t−2; its Table 1 delays imply t−2 and t−3. Only (2, 3) was run, and the receiver's own past also excludes bin t−1. This open detail should have been run both ways.
3. **[affects a conclusion]** `pid_from_table`: redundancy takes the minimum over sources per state of I_F, weighted by p(i_F), as I_spec(i_F; {R, I_P}) − I_spec(i_F; I_P). The claims file's M-PID reading takes the minimum within each (i_F, i_P), weighted by p(i_F, i_P). The notebook attributes its form to Eq 8 of the version of record but does not flag the departure from the claims file, and the two give different synergy, which feeds all of fig5.
4. **[affects a conclusion]** `subnetworks`: only M-SUB reading (a) was run, with [44]'s replacement of unconnected neurons and the strongest edges by normalized TE. Reading (b) (random 75 edges) was not run. Groups with fewer than 75 significant edges are kept, not redrawn as the claims file says. At DataSet13's 1.9% density a 50-neuron group expects about 47 edges, and the edge count per sub-network is never printed.
5. **[affects a conclusion]** cell 31, `model_correlations`: in the degree rule, 56/100 (N = 20) and about 50/100 (N = 40) models have uniform degrees, so their correlations are NaN. Their means are taken over the remaining models only, a selected subset, which feeds the fig7c distance comparison.
6. **[does not affect a conclusion]** cell 34, `fig7d_ok`: `deg_beats` checks only FDR p < 0.001, not direction. It prints True although the degree rule's conditioned MI is the lowest. The criterion still fails through `top_c`.
7. **[does not affect a conclusion]** cells 26–27: fig6 used only reading (f), 30 receivers per recording and 20 combinations against the paper's 100. Reading (s) was feasible: 19,205 and 14,814 sub-network receivers have six or more inputs.
8. **[does not affect a conclusion]** cell 35 prints the figs1 verdict only for (s, Pearson). It fails on its other parts under every reading anyway.
9. **[does not affect a conclusion]** The model's conditioned MI from 2000 runs carries about 6–7e-4 bits of plug-in bias, roughly 40% of the reported values. In my rerun the ranking did not change at 50,000 runs.

**C. What I could not check, and the output that would have let me**

- **Size of problem 1 in the real data.** I could not measure it. The notebook should print, per recording and scale, how many significant pairs had zero exceedances over all 5000 surrogates (`ran == 5000 & exceed == 0`) and how many had no relevant sender spikes. It should also show the correlation of degree with firing rate, and the networks re-thresholded with ties counted as exceeding (≥).
- **Eqs 8, 16–24 and [44]'s details.** Neither the version of record's equations nor [44] is in my materials. That blocks checking the redundancy form, the model's currents and score (Eqs 16–20), the fitted coefficients in `RULES`, and [44]'s past bins, jitter width and sub-network rule. Printing the equations' text as read, and [44]'s Table 1 row, would let me check them.
- **Sub-network edge counts.** The distribution of edges per sub-network, and the number with fewer than 75, would settle problem 4.
- **Approximation at the longer scale.** The normal-approximation check covers only the 1.6 ms bins on two small recordings. The same check at 3.5 ms is needed.
- **Archive check.** No claim is blocked, so I made no archive query. The streamed archive's MD5 matches `checksums.md5` (cell 1).

## End of run

18 turns, 6 minutes, $1.43 at API prices, result: success.
