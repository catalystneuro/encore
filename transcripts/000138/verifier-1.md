# 000138 · verifier-1 · run 40765331104

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 312
drwxr-xr-x 6 runner runner    4096 Oct 28 20:48 .
drwxr-xr-x 7 runner runner    4096 Oct 28 20:48 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 20:40 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 20:40 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 28 20:48 .claude
-rw-r--r-- 1 runner runner       0 Oct 28 20:48 .env
-rw-r--r-- 1 runner runner       0 Oct 28 20:48 .env.development
-rw-r--r-- 1 runner runner       0 Oct 28 20:48 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 28 20:48 .env.local
-rw-r--r-- 1 runner runner       0 Oct 28 20:48 .env.production
-rw-r--r-- 1 runner runner       0 Oct 28 20:48 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 28 20:48 .env.test
-rw-r--r-- 1 runner runner       0 Oct 28 20:48 .env.test.local
drwx------ 2 runner runner    4096 Oct 28 20:48 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 20:40 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 20:40 .github
-rw-r--r-- 1 runner runner       0 Oct 28 20:48 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 20:40 .idea
[... 38 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1016-j.neuron.2010.09.015.yaml"
}
```

```
1	# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset 000138.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
3	# protocol pilot-12 as stated in docs/protocol.md.
4	#
5	# Text read: the NIH author manuscript in PubMed Central (PMC2991102, NIHMS240235), main text,
6	# Methods and figure legends, with its one supplement file (NIHMS240235-supplement-01.pdf:
7	# Supplemental Figures 1 to 5, Supplemental Text, Supplemental Experimental Procedures). This is
8	# the accepted manuscript, not the copyedited version of record. The main-text PDF was not
9	# available, so Figure 6A-D, the range of dimensionalities plotted there and the per-dataset
10	# values in Figures 6 and 7 could not be read. The paper links no analysis code, so no code was
11	# read.
12	#
13	# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental
14	# Procedures). Three adult male rhesus monkeys (A, B, J) made delayed reaches on a fronto-parallel
15	# screen. Speed task (monkeys A, B): 7 directions, 2 distances, 2 instructed speeds, 28 conditions.
16	# Maze task (monkey J): straight reaches, or reaches curving around virtual barriers, with or
17	# without distractor targets, 108 conditions in all. Four datasets: A (64 single units), B (74), J
18	# (172 single units by single electrode, in four sets of 27 conditions, about 53 neurons each,
19	# analysed per set and then averaged), and J-array (two 96-electrode arrays, one in caudal PMd and
20	# one in surface M1, 146 single- and multi-unit isolations, all 108 conditions interleaved). Mean
[... 408 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "prepspace.py"
}
```

```
1	"""Loading and measures for dandiset 000138 (MC_Maze_Large), for Churchland, Cunningham, Kaufman,
2	Ryu & Shenoy (2010), Neuron 68:387-400, doi:10.1016/j.neuron.2010.09.015.
3	
4	The dandiset holds one session of monkey J (Jenkins, 2009-10-06) on the maze task: 500 successful
5	trials over 27 conditions (9 mazes, `trial_type`, each in 3 versions, `trial_version`), 162 sorted
6	units from two 96-electrode arrays, and hand position and velocity at 1 kHz. Files are streamed
7	from the archive at the pinned version; nothing is written to disk.
8	
9	Where the parameters come from. "Claims file" means the shared methods at the top of
10	claims/000138/10.1016-j.neuron.2010.09.015.yaml, which cite the paper; "paper" means a passage
11	taken here (protocol, author, step 1.6); "assumption" and "standard choice" are said as such.
12	
13	- `MIN_DELAY_MS` = 400: only trials with delays over 400 ms (claims file; Methods, Task design).
14	- `PROTO_R` = 0.9: maze trials kept when their horizontal and vertical velocity profiles
15	  correlate with a reference proto-trial at r > 0.9 (claims file; Supplemental Experimental
16	  Procedures, Task design). The proto-trial is the condition's mean profile (reading a) or its
17	  elementwise median profile (reading b). The window of the profile is not given; the window of
18	  the peri-movement T-matrix (`T_WINDOW`) is used (assumption: it is the window the paper
19	  analyses). Whether horizontal and vertical are each required to pass (`each`) or are
20	  correlated as one concatenated profile (`concat`) is not said; both are run.
[... 495 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_churchland_2010.ipynb'))
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
"
```

```
<persisted-output>
Output too large (91.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/38500b39-7ba4-4396-a798-8a6feda0c30f/tool-results/bz6s1vks8.txt

Preview (first 2KB):
==================== 0 markdown
# Reproducing Churchland et al. (2010) from dandiset 000138

**Paper.** Churchland MM, Cunningham JP, Kaufman MT, Ryu SI, Shenoy KV (2010). Cortical
preparatory activity: representation of movement or first cog in a dynamical machine? *Neuron*
68:387-400. [doi:10.1016/j.neuron.2010.09.015](https://doi.org/10.1016/j.neuron.2010.09.015). The
claims file (`claims/000138/10.1016-j.neuron.2010.09.015.yaml`) was written from the NIH author
manuscript in PubMed Central (PMC2991102) with its supplement; the main-text figure panels were
not available to its reader.

**Dandiset.** [DANDI:000138](https://dandiarchive.org/dandiset/000138/0.220113.0407), version
0.220113.0407 (MC_Maze_Large, Neural Latents Benchmark). The paper (2010) predates the dandiset
and cites no version. This is the only published version, and the draft holds the same two files
(same blobs, checked below), so the most recent published version is pinned.

**What it holds.** One session of monkey J (2009-10-06) on the maze task: 500 successful trials
[... 16 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/38500b39-7ba4-4396-a798-8a6feda0c30f/tool-results/bz6s1vks8.txt"
}
```

```
1	==================== 0 markdown
2	# Reproducing Churchland et al. (2010) from dandiset 000138
3	
4	**Paper.** Churchland MM, Cunningham JP, Kaufman MT, Ryu SI, Shenoy KV (2010). Cortical
5	preparatory activity: representation of movement or first cog in a dynamical machine? *Neuron*
6	68:387-400. [doi:10.1016/j.neuron.2010.09.015](https://doi.org/10.1016/j.neuron.2010.09.015). The
7	claims file (`claims/000138/10.1016-j.neuron.2010.09.015.yaml`) was written from the NIH author
8	manuscript in PubMed Central (PMC2991102) with its supplement; the main-text figure panels were
9	not available to its reader.
10	
11	**Dandiset.** [DANDI:000138](https://dandiarchive.org/dandiset/000138/0.220113.0407), version
12	0.220113.0407 (MC_Maze_Large, Neural Latents Benchmark). The paper (2010) predates the dandiset
13	and cites no version. This is the only published version, and the draft holds the same two files
14	(same blobs, checked below), so the most recent published version is pinned.
15	
16	**What it holds.** One session of monkey J (2009-10-06) on the maze task: 500 successful trials
17	over 27 conditions, 162 sorted units from two Utah arrays, hand, cursor and eye position, and hand
18	velocity. The paper's J-array dataset had 108 conditions, 146 units and a mean 2166 trials per
19	neuron; the dandiset is a 500-trial subset of a session, and nothing in it or the paper says
20	whether this session is the one the paper used. The single-electrode datasets (monkeys A, B and
[... 797 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/38500b39-7ba4-4396-a798-8a6feda0c30f/tool-results/bz6s1vks8.txt",
 "offset": 818,
 "limit": 700
}
```

```
818	                        for norm in ps.READINGS["norm"]:
819	                            peri_rows.append({**base, "t_units": t_units, "fold": fold, "start": start,
820	                                              "k": k, "norm": norm, "perf": pf[norm]})
821	        for fold in ps.READINGS["fold"]:
822	            for kin_end in ps.READINGS["kin_end"]:
823	                err = ps.kinematic_errors(ctx, inc, fold, kin_end)
824	                for k in range(1, 15):
825	                    pf = ps.perf_both(err[:, k - 1], X)
826	                    for norm in ps.READINGS["norm"]:
827	                        kin_rows.append({**base, "fold": fold, "kin_end": kin_end, "k": k, "norm": norm, "perf": pf[norm]})
828	        for task_end in ps.READINGS["task_end"]:
829	            for split in ps.READINGS["split"]:
830	                errs, dims = ps.task_errors(ctx, inc, task_end, split)
831	                for name, err in errs.items():
832	                    pf = ps.perf_both(err, X)
833	                    for norm in ps.READINGS["norm"]:
834	                        task_rows.append({**base, "task_end": task_end, "split": split, "space": name,
835	                                          "k": dims[name], "norm": norm, "perf": pf[norm]})
836	peri_df, kin_df, task_df = pd.DataFrame(peri_rows), pd.DataFrame(kin_rows), pd.DataFrame(task_rows)
837	print(f"Grid computed in {time.time() - t0:.0f} s: {len(peri_df)} peri-movement, {len(kin_df)} kinematic, "
[... 671 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_churchland_2010.ipynb'))
c=nb['cells'][50]
for o in c['outputs']:
    t=o.get('text') or o.get('data',{}).get('text/plain','')
    print(''.join(t)[-2500:])
"; grep -n -i -E "cross-valid|upper limit|leave-one|gray interval|shuffled|anterior|AP location" paper/10.1016-j.neuron.2010.09.015.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  tail -c 600 /home/runner/.claude/projects/-home-runner-work--temp-work/38500b39-7ba4-4396-a798-8a6feda0c30f/tool-results/ba3bgmz5y.txt | head -5; echo; for p in "cross-valid" "upper limit" "leave-one" "gray interval" "shuffled-space" "Figure 7C" "median AP" "proto-trial" "2166" "108 conditions" "Figure 8" "PD performance"; do echo "### $p"; grep -o -i -E ".{0,300}$p.{0,400}" paper/10.1016-j.neuron.2010.09.015.txt | head -4; done
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 660,720p paper/10.1016-j.neuron.2010.09.015.txt | cut -c1-1500; for p in "de-nois" "Supplemental Figure 4" "Figure 7 ." "Figure 6 \(" "gray line" ; do echo "### $p"; grep -o -i -E ".{0,300}$p.{0,500}" paper/10.1016-j.neuron.2010.09.015.txt | head -5; done
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np, prepspace as ps
rng=np.random.default_rng(0)
c,t,k=27,40,5
T=rng.normal(size=(c,t)); x=rng.normal(size=c)
# brute force LOO fixed
Tc=T-T.mean(0); U,s,Vt=np.linalg.svd(Tc,full_matrices=False); S=U[:,:k]*s[:k]
e=[]
for i in range(c):
    tr=np.r_[0:i,i+1:c]; D=np.column_stack([np.ones(c-1),S[tr]]); b=np.linalg.lstsq(D,x[tr],rcond=None)[0]
    e.append(x[i]-b[0]-S[i]@b[1:])
print('fixed', np.abs(np.array(e)-ps.loo_errors_fixed(S,x[None])[0]).max())
# compare once via gram
Sg=ps._scores_from_gram(ps.centre_gram(T@T.T),k)[0]
print('gram vs svd (abs)', np.abs(np.abs(Sg)-np.abs(S)).max())
# refit brute
e=[]
for i in range(c):
    tr=np.r_[0:i,i+1:c]; m=T[tr].mean(0); U,s,Vt=np.linalg.svd(T[tr]-m,full_matrices=False)
    Str=(T[tr]-m)@Vt[:k].T; ti=(T[i]-m)@Vt[:k].T
    D=np.column_stack([np.ones(c-1),Str]); b=np.linalg.lstsq(D,x[tr],rcond=None)[0]
    e.append(x[i]-b[0]-ti@b[1:])
print('refit', np.abs(np.array(e)-ps.loo_errors_refit_gram(T@T.T,x,k)[k-1]).max())
# peri_errors excludes neuron's own contribution
n=6; move=rng.normal(size=(n,c,1450)).astype(np.float32); prep=rng.normal(size=(n,c))
inc=np.array([1,1,0,1,0,1],bool)
err=ps.peri_errors({'move':move,'prep':prep},inc,'all','once',3)
j=1; u=np.nonzero(inc)[0][j]
others=[v for v in range(n) if v!=u]
TT=np.concatenate([ps.t_matrix(move)[v] for v in others],1)
Tc=TT-TT.mean(0); U,s,_=np.linalg.svd(Tc,full_matrices=False); S=U[:,:3]*s[:3]
print('peri excl self', np.abs(err[j,2]-ps.loo_errors_fixed(S,prep[u][None])[0]).max())
# smoothing: gaussian of single spike integrates to 1 spike
r=ps.smoothed_rate(np.array([0.5]),1000); print('rate integral (spikes)', r.sum()/1000, 'peak', r.max())
print(ps.performance(np.zeros((1,5)),rng.normal(size=(1,5))))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, prepspace as ps
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls ~/.venv* /opt 2>/dev/null | head; which -a python python3 uv pip 2>/dev/null; python3 -m pip --version 2>&1 | head -1
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
[... 2 more lines not kept]
```

**Agent**

I've read the notebook, the helper module and the claims file. Next I'm installing numpy/scipy in a temporary venv so I can test the PD helper functions on synthetic data.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q v && . v/bin/activate && uv pip install -q numpy scipy pandas h5py 2>&1 | tail -2; python -c "import numpy, scipy; print(numpy.__version__)"
```

```
2.5.4
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/t.py <<'EOF'
import sys, types
for m in ["remfile"]: sys.modules[m]=types.ModuleType(m)
dd=types.ModuleType("dandi"); da=types.ModuleType("dandi.dandiapi"); da.DandiAPIClient=None
sys.modules["dandi"]=dd; sys.modules["dandi.dandiapi"]=da
import numpy as np, prepspace as ps
rng=np.random.default_rng(0)
c,t,k=27,40,5
T=rng.normal(size=(c,t)); x=rng.normal(size=c)
Tc=T-T.mean(0); U,s,Vt=np.linalg.svd(Tc,full_matrices=False); S=U[:,:k]*s[:k]
e=[]
for i in range(c):
    tr=np.r_[0:i,i+1:c]; D=np.column_stack([np.ones(c-1),S[tr]]); b=np.linalg.lstsq(D,x[tr],rcond=None)[0]
    e.append(x[i]-b[0]-S[i]@b[1:])
print('fixed', np.abs(np.array(e)-ps.loo_errors_fixed(S,x[None])[0]).max())
Sg=ps._scores_from_gram(ps.centre_gram(T@T.T),k)[0]
print('gram vs svd (abs)', np.abs(np.abs(Sg)-np.abs(S)).max())
e=[]
for i in range(c):
    tr=np.r_[0:i,i+1:c]; m=T[tr].mean(0); U,s,Vt=np.linalg.svd(T[tr]-m,full_matrices=False)
    Str=(T[tr]-m)@Vt[:k].T; ti=(T[i]-m)@Vt[:k].T
    D=np.column_stack([np.ones(c-1),Str]); b=np.linalg.lstsq(D,x[tr],rcond=None)[0]
    e.append(x[i]-b[0]-ti@b[1:])
print('refit', np.abs(np.array(e)-ps.loo_errors_refit_gram(T@T.T,x,k)[k-1]).max())
n=6; move=rng.normal(size=(n,c,1450)).astype(np.float32); prep=rng.normal(size=(n,c))
inc=np.array([1,1,0,1,0,1],bool)
err=ps.peri_errors({'move':move,'prep':prep},inc,'all','once',3)
j=1; u=np.nonzero(inc)[0][j]
TT=np.concatenate([ps.t_matrix(move)[v] for v in range(n) if v!=u],1)
Tc=TT-TT.mean(0); U,s,_=np.linalg.svd(Tc,full_matrices=False); S=U[:,:3]*s[:3]
print('peri excl self', np.abs(err[j,2]-ps.loo_errors_fixed(S,prep[u][None])[0]).max())
r=ps.smoothed_rate(np.array([0.5]),1000); print('rate integral (spikes)', r.sum()/1000)
# leverage: once vs refit at high k with c=27
T=rng.normal(size=(c,200)); x=rng.normal(size=c)
G=T@T.T
for kk in [5,10,14]:
    Sg=ps._scores_from_gram(ps.centre_gram(G),kk)[0]
    eo=ps.loo_errors_fixed(Sg,x[None]); er=ps.loo_errors_refit_gram(G,x,kk)[kk-1]
    print(kk,'noise perf once',ps.performance(eo,x[None])[0].round(3),'refit',ps.performance(er[None],x[None])[0].round(3))
# oscillator: mean over full cycle
a=2*np.pi/360; W=np.array([[1,-a],[a,1]]); M=np.zeros((2,2)); P=np.eye(2)
for s_ in range(360): P=W@P; M+=P/360
print('mean-over-cycle map', M.round(4))
EOF
. $TMPDIR/v/bin/activate; python $TMPDIR/t.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t.py", line 5, in <module>
    import numpy as np, prepspace as ps
ModuleNotFoundError: No module named 'prepspace'
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/v/bin/activate; PYTHONPATH= python $TMPDIR/t.py
```

```
fixed 2.886579864025407e-15
gram vs svd (abs) 5.617728504603292e-14
refit 4.218847493575595e-15
peri excl self 2.19824158875781e-14
rate integral (spikes) 1.0000000000000002
5 noise perf once -0.431 refit -0.162
10 noise perf once 0.01 refit -0.094
14 noise perf once -0.501 refit 0.043
mean-over-cycle map [[ 0.     0.009]
 [-0.009  0.   ]]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/t2.py <<'EOF'
import sys, types
sys.modules["remfile"]=types.ModuleType("remfile"); da=types.ModuleType("dandi.dandiapi"); da.DandiAPIClient=None
sys.modules["dandi"]=types.ModuleType("dandi"); sys.modules["dandi.dandiapi"]=da
import numpy as np, prepspace as ps
rng=np.random.default_rng(1); c=27
# structured T (decaying spectrum), responses: pure noise, and signal in 3 leading PCs + noise
L=rng.normal(size=(c,30))*(0.7**np.arange(30)); T=L@rng.normal(size=(30,300))
G=T@T.T
S=ps._scores_from_gram(ps.centre_gram(G),14)[0]
for name,X in [("noise",rng.normal(size=(200,c))),("signal",(S[:,:3]/S[:,:3].std(0))@rng.normal(size=(3,200)) .T.T if False else ((S[:,:3]/S[:,:3].std(0))@rng.normal(size=(3,200))).T+rng.normal(size=(200,c)))]:
    out=[]
    for k in [3,6,10,12,14]:
        eo=ps.loo_errors_fixed(S[:,:k],X)
        er=np.stack([ps.loo_errors_refit_gram(G,x,k)[k-1] for x in X])
        out.append((k,ps.performance(eo,X).mean().round(3),ps.performance(er,X).mean().round(3)))
    print(name,out)
EOF
. $TMPDIR/v/bin/activate; PYTHONPATH=. python $TMPDIR/t2.py
```

```
noise [(3, np.float64(-0.241), np.float64(-0.211)), (6, np.float64(-0.48), np.float64(-0.468)), (10, np.float64(-0.875), np.float64(-0.857)), (12, np.float64(-1.12), np.float64(-1.042)), (14, np.float64(-1.597), np.float64(-1.435))]
signal [(3, np.float64(0.59), np.float64(0.585)), (6, np.float64(0.522), np.float64(0.526)), (10, np.float64(0.388), np.float64(0.394)), (12, np.float64(0.315), np.float64(0.339)), (14, np.float64(0.12), np.float64(0.188))]
```

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000138/versions/0.220113.0407/assets/?page_size=100" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['count']); [print(a['path'],a['size']) for a in d['results']]"; curl -s "https://api.dandiarchive.org/api/dandisets/000138/versions/0.220113.0407/" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  grep -o -i -E ".{0,200}(viapoint|via-point|halfpoint|orthogonal excursion).{0,400}" paper/10.1016-j.neuron.2010.09.015.txt | head -4
```

Result: not kept, because it reads the paper's text.

**Agent**

**Verifier report, round 1: Churchland et al. 2010 (doi:10.1016/j.neuron.2010.09.015) on DANDI:000138 v0.220113.0407**

**A. Outcomes** (15 claims, from the claims file)

| Claim id | My outcome | Reason |
|---|---|---|
| fig4abc-tuning-correlation-single-electrode | blocked (data_missing) | The archive lists 2 assets, both from one subject (sub-Jenkins, array data). The single-electrode recordings of monkeys A, B and J are not there, so no part can be tested. |
| fig4d-tuning-correlation-j-array | partially_reproduced | Main reading (cell 23): mean r 0.195 and Spearman 0.212, both outside 0.13±0.013 and 0.11±0.011. Mean r is above zero at p = 0.023 (t-test). No reading puts both means within tolerance. Spearman is never within tolerance (0.146 to 0.212). |
| fig4e-correlation-time-course | not_reproduced | The mean correlation at movement onset is 0.13 to 0.22 under all 8 readings, above the 0.1 bound (cell 26). The other two conditions hold: the decline begins about −250 to −200 ms, and the curve only nears zero by about +200 ms. |
| results-ap-location-no-effect | reproduced (J-array only) | p = 0.43 to 0.84 under all 8 readings (cell 29), using array membership as AP location. A, B and J are data_missing. This is a claim of absence tested on 20 units, so power is low. |
| supp-preparatory-dimensionality | reproduced (assumption) | k90 = 11 with all units and 10 to 11 with included units (range reading), inside 6.3–11 (cell 31). The value sits at the upper edge: all units under `each` give 12. |
| fig6-peri-movement-space-best | reproduced (J-array only) | Main reading: peri-movement 0.351 at k = 10, against kitchen sink 0.250 and kinematic 0.103 (cell 36). The peri-movement space is best in 1468 of 2048 combinations. |
| fig6-each-dimensionality | reproduced (assumption) | Main reading wins 20 of 22 comparisons (0.909) and beats endpoints + max speed at k = 3 (0.126 vs 0.000). Only 1074 of 2048 combinations meet the criterion, mostly failing under fold=once with combine=each (cell 38). |
| fig6-dimensionality-trend | reproduced (assumption, depends on fold reading) | fold=once: best k = 10, then a fall to −0.456 at k = 14. fold=refit: performance rises steadily to 0.461 at k = 14, and only 6% of combinations meet the criterion (cell 40). See problem 1. |
| fig6-pd-adequate-all-spaces | reproduced | Peri-movement 0.351 and kinematic 0.103 are above zero, and 7 of 8 task spaces are above zero. Holds in 1936 of 2048 combinations (cell 42). |
| fig6e-summary-rank | blocked (data_missing) | Needs A, B and J single-electrode data plus EMG. The archive has neither. |
| fig7a-shuffled-space-poor | reproduced (assumption) | Main reading: shuffled best 0.014, below peri-movement at every k and below kinematic best 0.103 (cell 44). Fails under fold=refit (0.178 > 0.160) and under combine=each. |
| fig7b-window-start-onset | reproduced | Main-reading ratio 0.908, within 0.873–1.067. Median ratio over all combinations 0.917 (cell 46). Only reading (a) of the claims file, J-array against 0.97, is possible here. |
| fig7c-anterior-posterior | not_reproduced | Main reading: posterior/random 0.62 to 0.94 and anterior/random 0.67 to 0.97, outside the 10% bound (cell 48). Only 2 of 16 rows pass, both using fold=refit with the neuron's own rate in the upper-limit space (see problem 2). |
| fig7d-pd-consistency | reproduced | Peri-movement consistency is higher in every comparison, for all 8 variants and both axis scalings (cell 50). |
| fig8-oscillator-model | reproduced | 0.08 lies inside the central 95% of r (about −0.40 to 0.39) under all 4 readings; median r is about 0. PD leave-one-out performance is 1.0 (cell 52). |

**B. Problems**

1. [affects a conclusion] Cells 35 and 40, `loo_pca_space` fold reading: fig6-dimensionality-trend passes only under fold=once (91% of combinations vs 6% under refit). I checked both fold implementations against brute-force PCA and regression on synthetic data, and they are correct to 1e-14. On this dataset the fall at k ≥ 12 under once comes from leverage: k = 14 PCs from a 27-row matrix. The paper's J-array had 108 conditions. "Once" is the more natural reading of the Methods (leave out a condition, refit the PD), so I keep reproduced, but the result rests on that reading. Fig7a and fig6-each also flip under refit.
2. [does not affect a conclusion] Cell 48 `subset_scores`, `self_in_upper=True`: the Supplemental Procedures justify the upper limit with "whatever one neuron is tuned for, it ought to be shared with at least some of the other neurons". That implies leaving out the neuron being fit. Putting its own preparatory rate into the space it is regressed on is not a reading the paper allows. The only 2 rows that meet the fig7c criterion use it. With it excluded, fig7c fails under every variant.
3. [does not affect a conclusion] Cells 44 and 48: refit variants use 5 shuffle draws and 4 random-half draws, not the 20 the claims file sets.
4. [does not affect a conclusion] The data are probably not the paper's J-array session. The dandiset has 27 conditions and about 14 trials per condition after selection, while the paper's J-array had 108 conditions and about 2166 trials per neuron. The notebook says this (cell 0), but every tolerance is judged against a different dataset. It also bears on fig7d: drawing 25 of 27 conditions with replacement gives heavily overlapping draws.
5. [does not affect a conclusion] Cells 7, 28 and 47: every unit's electrode reference points to PMd, and the electrode coordinates are NaN. Mapping id prefix 1 to PMd is an assumption, supported only by stronger preparatory tuning in that prefix. The AP regression p-value and the fig7c criterion are symmetric in the labelling. Only the "anterior better" direction depends on it.
6. [does not affect a conclusion] Cell 26 uses only the movement-locked trace, not the spliced trace. All time points in the criterion (−400 to 0 ms) lie inside `MOVE_TRACE`, so the result is unaffected.
7. [does not affect a conclusion] Cell 31: k90 = 11 sits at the bound, and split-half k90 is 13 to 14, so trial noise inflates the count. supp-preparatory-dimensionality is fragile.
8. [does not affect a conclusion] Cell 23: fig4d's mean r depends on the 1.5× peri-movement criterion (0.106 to 0.202 for ratios 1.0 to 2.0, cell 24) and rests on 20 units.

Checked with no problem found: the helper functions (`loo_errors_fixed`, `loo_errors_refit_gram`, `_scores_from_gram`, `peri_errors` leaving out the fitted neuron, `smoothed_rate` normalisation) against brute force; the analysis windows, inclusion thresholds and task-space definitions against the Methods; units (mm, mm/s, spikes/s); the oscillator's mean-over-cycle map, which is ≈[[0, .009], [−.009, 0]], so r is the sampling correlation of the two initial coordinates, consistent with r = 0.08 from a single draw. The test file is not used, and none of the analyses train and test on different trial sets, so there is no leakage to check. Leave-one-condition-out is applied correctly.

**C. What I could not check**

- Whether this session is the paper's J-array session. Nothing in the files or the paper identifies it.
- Which id prefix is which array. NLB documentation of the unit-id scheme, or the archive's per-unit array labels, would settle it.
- Whether the fig7c differences are within noise. The spread (SD) of normalised performance across random-half draws is not printed, so the 10% bound cannot be judged against sampling noise.
- Whether fig6-each and fig6-trend fail under fold=refit for a real reason or a degenerate one. Printing the refit curves and the number of comparisons won under the main reading with refit would show this.
- Per-condition trial counts after selection for each reading. Only the min and max are printed (cell 15).

Cell 0 still contains the author's outcome table. I did not use it.

## End of run

18 turns, 15 minutes, result: success.
