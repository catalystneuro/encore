# 000139 · verifier-1 · run 40766027299

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat *claims* 2>/dev/null | head -300
```

```
total 412
drwxr-xr-x 6 runner runner    4096 Oct 28 20:56 .
drwxr-xr-x 7 runner runner    4096 Oct 28 20:56 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 20:44 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 20:44 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 28 20:56 .claude
-rw-r--r-- 1 runner runner       0 Oct 28 20:56 .env
-rw-r--r-- 1 runner runner       0 Oct 28 20:56 .env.development
-rw-r--r-- 1 runner runner       0 Oct 28 20:56 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 28 20:56 .env.local
-rw-r--r-- 1 runner runner       0 Oct 28 20:56 .env.production
-rw-r--r-- 1 runner runner       0 Oct 28 20:56 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 28 20:56 .env.test
-rw-r--r-- 1 runner runner       0 Oct 28 20:56 .env.test.local
drwx------ 2 runner runner    4096 Oct 28 20:56 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 20:44 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 20:44 .github
-rw-r--r-- 1 runner runner       0 Oct 28 20:56 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 20:44 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 28 20:44 .mcp.json
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1016-j.neuron.2010.09.015.yaml
```

```
<persisted-output>
Output too large (37.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/79dfa217-9cd3-4b15-99ce-322cf0b4ed65/tool-results/bp72t5wtc.txt

Preview (first 2KB):
# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset 000139.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
# protocol as stated in docs/protocol.md (version pilot-12).
#
# Text read: the NIH author manuscript in PubMed Central (PMC2991102), as extracted to
# paper/10.1016-j.neuron.2010.09.015.txt, with its Results, Methods, figure legends and the one
# supplement (NIHMS240235-supplement-01.pdf: Supplemental Figures 1 to 5, Supplemental Text and
# Supplemental Experimental Procedures). Not the version of record. The figures themselves are not
# in the text; values plotted only in Figures 4, 6 and 7 are not available and no claim rests on
# them. The paper links no code, so every method below comes from the Methods, the legends or the
# supplement.
#
# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental
# Procedures). Three adult male rhesus monkeys (A, B, J), delayed reaches from a central touch spot
# to a target on a fronto-parallel screen. Trial events: target onset (the target jitters), go cue
# (jitter stops and the touch spot disappears), movement onset. Delays about 0 to 1000 ms; only
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1016-j.neuron.2010.09.015.yaml"
}
```

```
1	# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset 000139.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
3	# protocol as stated in docs/protocol.md (version pilot-12).
4	#
5	# Text read: the NIH author manuscript in PubMed Central (PMC2991102), as extracted to
6	# paper/10.1016-j.neuron.2010.09.015.txt, with its Results, Methods, figure legends and the one
7	# supplement (NIHMS240235-supplement-01.pdf: Supplemental Figures 1 to 5, Supplemental Text and
8	# Supplemental Experimental Procedures). Not the version of record. The figures themselves are not
9	# in the text; values plotted only in Figures 4, 6 and 7 are not available and no claim rests on
10	# them. The paper links no code, so every method below comes from the Methods, the legends or the
11	# supplement.
12	#
13	# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental
14	# Procedures). Three adult male rhesus monkeys (A, B, J), delayed reaches from a central touch spot
15	# to a target on a fronto-parallel screen. Trial events: target onset (the target jitters), go cue
16	# (jitter stops and the touch spot disappears), movement onset. Delays about 0 to 1000 ms; only
17	# trials with delays above 400 ms analysed. Four datasets. Monkeys A and B, speed task, 28
18	# conditions (7 directions, 2 distances, 2 instructed speeds), single electrodes, 64 and 74
19	# single units. Monkey J, maze task, single electrodes, 172 single units, recorded on four sets of
20	# 27 conditions each (about 53 neurons per set; population analyses done per set, then averaged).
[... 513 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat maze.py
```

```
"""Loading and measures for dandiset 000139 (MC_Maze_Medium), used to test
Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400.

Where each parameter comes from:

- Version: the only published version of the dandiset (``VERSION``).
- Trials kept: delays above 400 ms (claims file, opening comment, from Methods,
  Task design and behavior). Trials whose horizontal and vertical velocity
  profiles correlate with a reference proto-trial at r > 0.9 (Supplemental
  Experimental Procedures, Task design and behavioral control). The
  proto-trial and how the two profiles are combined are open; the claims file
  names the readings, implemented in ``proto_keep``. The window over which the
  profiles are correlated is not given; 150 ms before to 800 ms after movement
  onset (the maze-task peri-movement window of Methods, PCA-based spaces) is
  used, an assumption.
- Movement onset: reading (a) the dataset's ``move_onset_time``; reading (b)
  the first time after the go cue at which hand speed exceeds 10% of the
  trial's peak speed (the threshold is a standard choice; the paper does not
  give one).
- Rates: spike trains smoothed with a Gaussian of 20 ms standard deviation
[... 386 more lines not kept]
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
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain'])[:4000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1438 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	==================== 0 markdown
2	# Churchland et al. (2010) on dandiset 000139 (MC_Maze_Medium)
3	
4	**Paper.** Churchland MM, Cunningham JP, Kaufman MT, Ryu SI, Shenoy KV (2010). Cortical preparatory
5	activity: representation of movement or first cog in a dynamical machine? *Neuron* 68, 387-400.
6	doi:10.1016/j.neuron.2010.09.015.
7	
8	**Dataset.** DANDI:000139, "MC_Maze_Medium", version **0.220113.0408**, streamed from the archive.
9	This is the only published version of the dandiset (the other is the draft), so it is pinned; the
10	paper cites no version. The dandiset holds one session of monkey Jenkins (2009-09-29) on the maze
11	task, recorded with two Utah arrays, cut for the Neural Latents Benchmark into 250 training and
12	validation trials (with behaviour and trial labels) and 100 test trials (700 ms segments, no
13	condition labels, held-in units only).
14	
15	**Claims.** `claims/000139/10.1016-j.neuron.2010.09.015.yaml`, written from the NIH author manuscript
16	(PMC2991102) with its supplement, and checked by a second reader. Methods the claims file leaves
17	open are taken from the paper (cited where used) or, where the paper is silent, run under every
18	reading the claims file names.
19	
20	| Claim | Tested here |
[... 741 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 762,
 "limit": 700
}
```

```
762	print(curve_tab.to_string())
763	task_tab = pd.Series({k: v.mean() for k, v in F6["task"].items()}).round(3)
764	dims = {k: v.shape[1] for k, v in F6["spaces"].items()}
765	print()
766	print(pd.DataFrame({"dim": dims, "mean_perf": task_tab}).to_string())
767	--OUT--
768	Neurons fitted: 76 | by array: {1: 35, 2: 41}
769	Reach end (ms after onset) over conditions: 251 to 619
770	Mean performance over neurons, by k:
771	                                1      2      3      4      5      6      7      8      9      10     11     12     13     14
772	peri | S a                  -0.006  0.045  0.052  0.091  0.100  0.117  0.102  0.061  0.026 -0.008 -0.184 -0.396 -0.574 -0.980
773	upper | S a                 -0.014  0.054  0.026  0.056  0.068  0.061  0.050 -0.028 -0.099 -0.252 -0.281 -0.394 -0.549 -0.838
774	upper incl. neuron | S a     0.009  0.096  0.102  0.148  0.165  0.176  0.178  0.122  0.103  0.048  0.029 -0.016 -0.064 -0.097
775	kinematic win a rep a | S a  0.008  0.016  0.013  0.016 -0.005 -0.040 -0.070 -0.128 -0.176 -0.216 -0.328 -0.480 -0.696 -2.005
776	kinematic win a rep b | S a  0.008  0.016  0.013  0.016 -0.005 -0.040 -0.071 -0.128 -0.176 -0.216 -0.329 -0.481 -0.694 -2.011
777	kinematic win b rep a | S a  0.011  0.022  0.018  0.017 -0.004 -0.036 -0.070 -0.128 -0.175 -0.214 -0.216 -0.430 -0.506 -2.317
778	kinematic win b rep b | S a  0.011  0.022  0.018  0.017 -0.004 -0.036 -0.070 -0.128 -0.175 -0.214 -0.217 -0.431 -0.506 -2.319
779	peri | S b                  -0.004  0.056  0.065  0.108  0.129  0.145  0.195  0.203  0.205  0.205  0.221  0.225  0.226  0.226
780	upper | S b                 -0.015  0.058  0.042  0.080  0.103  0.115  0.144  0.184  0.172  0.165  0.157  0.151  0.138  0.098
781	upper incl. neuron | S b     0.004  0.092  0.091  0.151  0.181  0.205  0.236  0.277  0.275  0.282  0.289  0.297  0.300  0.299
[... 658 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "spikes/s|1\.5|upper limit|proto|leave-one|cross-valid|2166|2155|146|108|anterior|array" 10.1016-j.neuron.2010.09.015.txt | head -80; pdftotext 10.1016-j.neuron.2010.09.015.supp.pdf $TMPDIR/supp.txt && wc -l $TMPDIR/supp.txt
```

```
Exit code 127
7:Neuron 319 nihpa 8809320 Neuron 0896-6273 1097-4199 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC2991102 PMC2991102.1 2991102 2991102 NIHMS240235 21040842 10.1016/j.neuron.2010.09.015 NIHMS240235 NIHPA240235 1 Article Cortical preparatory activity: representation of movement or first cog in a dynamical machine? Churchland MM 1 Cunningham JP 1 3 Kaufman MT 2 Ryu SI 1 4 Shenoy KV 1 2 5 1 Dept. of Electrical Engineering, Stanford University, Stanford CA, 94305, USA 2 Neurosciences Program, Stanford University, Stanford CA, 94305, USA 3 Dept. of Engineering, University of Cambridge, Cambridge, UK 4 Dept. of Neurosurgery, Palo Alto Medical Foundation, Palo Alto CA, 94301, USA 5 Dept. of Bioengineering, Stanford University, Stanford CA, 94705, USA 4 11 2010 68 3 191982 387 400 06 10 2010 04 11 2011 04 11 2011 06 10 2011 14 10 2026 This file is available for text mining. It may also be used consistent with the principles of fair use under the copyright law. Summary The motor cortices are active during both movement and movement preparation. A common assumption is that preparatory activity constitutes a sub-threshold form of movement activity: a neuron active during rightwards movements becomes modestly active during preparation of a rightwards movement. We asked whether this pattern of activity is in fact observed. We found that it was not: at the level of a single neuron, preparatory tuning was weakly correlated with movement-period tuning. Yet somewhat paradoxically, preparatory tuning could be captured by a preferred direction in an abstract ‘space’ that described the population-level pattern of movement activity. In fact, this relationship accounted for preparatory responses better than did traditional tuning models. These results are expected if preparatory activity provides the initial state of a dynamical system whose evolution produces movement activity. Our results thus suggest that preparatory activity may not repr
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 - <<'EOF'
import re
t=open('10.1016-j.neuron.2010.09.015.txt').read()
for kw in ['spikes/s','1.5 times','upper limit','proto','left out','remaining conditions','2166','2155','anterior','posterior','random halves','J-array','Figure 7C','with replacement','90%']:
    for m in re.finditer(re.escape(kw),t):
        print('##',kw,':',t[max(0,m.start()-400):m.end()+400].replace('\n',' '))
        print()
EOF
```

```
<persisted-output>
Output too large (29.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/79dfa217-9cd3-4b15-99ce-322cf0b4ed65/tool-results/bpf45dsha.txt

Preview (first 2KB):
## spikes/s : uided by stereotaxic critera, the known response properties of M1 and PMd, and the effects of microstimulation. Recordings were medial to the arcuate spur and lateral to – or in a few instances within the lateral bank of – the precentral dimple. Few if any recordings were made within rostral PMd, near the arcuate sulcus. Analysis of preparatory responses was restricted to neurons with at least 10 spikes/s of preparatory tuning. Electrode arrays were implanted in PMd and surface M1 ( Supp. Fig. 3 ). The resulting dataset involved simultaneous recordings and much larger trial counts per neuron (2155). However, isolations were only occasionally of the same high isolation quality as for the single-electrode recordings. Many array recordings were of contaminated single-unit isolations or isolations of 

## spikes/s : ality as for the single-electrode recordings. Many array recordings were of contaminated single-unit isolations or isolations of two or more neurons. Still, some array-based isolations were of high quality, including those in Figure 3E,F . Firing rate modulation was typically lower for the array recordings, presumably due to the lack of selection bias. We thus used a lower inclusion criterion: >5 spikes/s of preparatory tuning, which was acceptable given the higher signal-to-noise ratio provided by the higher trial count. Correlations between preparatory and peri-movement tuning For the preparatory epoch, firing rate was averaged from 200 ms before the go cue until 100 ms after. For the peri-movement epoch, activity was averaged from 100 ms before movement onset until 350 ms after. The vector of p

...
</persisted-output>
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/79dfa217-9cd3-4b15-99ce-322cf0b4ed65/tool-results/bpf45dsha.txt"
}
```

```
1	## spikes/s : uided by stereotaxic critera, the known response properties of M1 and PMd, and the effects of microstimulation. Recordings were medial to the arcuate spur and lateral to – or in a few instances within the lateral bank of – the precentral dimple. Few if any recordings were made within rostral PMd, near the arcuate sulcus. Analysis of preparatory responses was restricted to neurons with at least 10 spikes/s of preparatory tuning. Electrode arrays were implanted in PMd and surface M1 ( Supp. Fig. 3 ). The resulting dataset involved simultaneous recordings and much larger trial counts per neuron (2155). However, isolations were only occasionally of the same high isolation quality as for the single-electrode recordings. Many array recordings were of contaminated single-unit isolations or isolations of 
2	
3	## spikes/s : ality as for the single-electrode recordings. Many array recordings were of contaminated single-unit isolations or isolations of two or more neurons. Still, some array-based isolations were of high quality, including those in Figure 3E,F . Firing rate modulation was typically lower for the array recordings, presumably due to the lack of selection bias. We thus used a lower inclusion criterion: >5 spikes/s of preparatory tuning, which was acceptable given the higher signal-to-noise ratio provided by the higher trial count. Correlations between preparatory and peri-movement tuning For the preparatory epoch, firing rate was averaged from 200 ms before the go cue until 100 ms after. For the peri-movement epoch, activity was averaged from 100 ms before movement onset until 350 ms after. The vector of p
4	
5	## 1.5 times :  tuning For the preparatory epoch, firing rate was averaged from 200 ms before the go cue until 100 ms after. For the peri-movement epoch, activity was averaged from 100 ms before movement onset until 350 ms after. The vector of preparatory rates (one per condition) was correlated with the vector of peri-movement rates. Analy
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000139/versions/0.220113.0408/assets/" | python3 -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000139/versions/0.220113.0408/" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('description')); print(json.dumps(d.get('assetsSummary'),indent=1)); print(d.get('wasGeneratedBy')); print([r.get('url') for r in d.get('relatedResource',[])])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000139/versions/0.220113.0408/assets/7ef450a8-8684-42e2-8598-cd38ca2b2e50/" | python3 -c "import json,sys; d=json.load(sys.stdin); [d.pop(k,None) for k in ['contentUrl','digest']]; print(json.dumps(d,indent=1)[:3000])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import numpy as np, maze as M
rng=np.random.default_rng(0)
# 1. recompute projection vs explicit PCA
c=27; T=rng.standard_normal((c,40)); x=rng.standard_normal(c)
G=T@T.T; ks=[1,3,6]
perf=M.pd_performance_pca(x,G,ks,True)
pred=np.zeros((3,c))
for l in range(c):
    tr=np.delete(np.arange(c),l); mu=T[tr].mean(0); Tc=T[tr]-mu
    U,s,Vt=np.linalg.svd(Tc,full_matrices=False)
    Str=Tc@Vt.T; sl=(T[l]-mu)@Vt.T
    for i,k in enumerate(ks):
        A=np.column_stack([np.ones(c-1),Str[:,:k]]); coef=np.linalg.lstsq(A,x[tr],rcond=None)[0]
        pred[i,l]=coef[0]+sl[:k]@coef[1:]
print("recompute helper",perf.round(4),"explicit",(1-((pred-x)**2).mean(1)/x.var()).round(4))
# 2. chance level of LOO performance in a random fixed space
for k in [2,3,4,6,11]:
    v=[M.pd_performance_fixed(rng.standard_normal(c), rng.standard_normal((c,k))) for _ in range(2000)]
    print("chance k",k,"mean",np.mean(v).round(3),"95th pct",np.percentile(v,95).round(3))
# 3. untuned Poisson neurons: range of condition means of 0.3 s window, ~8.5 trials/cond
for rate in [5,10,20]:
    n=np.array([8]*13+[9]*14)
    passes=[]
    for _ in range(2000):
        m=np.array([rng.poisson(rate*0.3,k).mean()/0.3 for k in n])
        passes.append(m.max()-m.min()>5)
    print("untuned rate",rate,"Hz: fraction passing range>5:",np.mean(passes))
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls; which -a python python3; ls ~/.venv* /opt 2>/dev/null | head; pip --version 2>&1 | head -2
```

```
10.1016-j.neuron.2010.09.015.yaml
bunfig.toml
maze.py
node_modules
package-lock.json
package.json
paper
pnpm-lock.yaml
reproduce_churchland_2010.ipynb
scripts
yarn.lock
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
/opt/hostedtoolcache/Python/3.13.17/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt:
actionarchivecache
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
for p in /usr/bin/python3 /opt/hostedtoolcache/Python/3.13.17/x64/bin/python3; do $p -c "import numpy; print('$p', numpy.__version__)" 2>&1 | tail -1; done; ls /opt/hostedtoolcache/Python/
```

```
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
3.11.17
3.12.15
3.13.17
3.14.9
3.15.1
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -m venv v && ./v/bin/pip install -q numpy scipy pandas 2>&1 | tail -2; ./v/bin/python -c "import numpy, scipy, pandas; print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  mkdir -p $TMPDIR/stubs; for m in requests h5py remfile pynwb; do echo "" > $TMPDIR/stubs/$m.py; done; PYTHONPATH=$TMPDIR/stubs:. $TMPDIR/v/bin/python - <<'EOF'
import numpy as np, maze as M
rng=np.random.default_rng(0)
c=27; T=rng.standard_normal((c,40)); x=rng.standard_normal(c)
G=T@T.T; ks=[1,3,6]
perf=M.pd_performance_pca(x,G,ks,True)
pred=np.zeros((3,c))
for l in range(c):
    tr=np.delete(np.arange(c),l); mu=T[tr].mean(0); Tc=T[tr]-mu
    U,s,Vt=np.linalg.svd(Tc,full_matrices=False)
    Str=Tc@Vt.T; sl=(T[l]-mu)@Vt.T
    for i,k in enumerate(ks):
        A=np.column_stack([np.ones(c-1),Str[:,:k]]); coef=np.linalg.lstsq(A,x[tr],rcond=None)[0]
        pred[i,l]=coef[0]+sl[:k]@coef[1:]
print("recompute helper",perf.round(4),"explicit",(1-((pred-x)**2).mean(1)/x.var()).round(4))
for k in [2,3,4,6,11]:
    v=[M.pd_performance_fixed(rng.standard_normal(c), rng.standard_normal((c,k))) for _ in range(2000)]
    print("chance k",k,"mean",np.mean(v).round(3),"95th pct",np.percentile(v,95).round(3))
# peri-like PCA space chance (reading a), random T
for R in [False,True]:
    v=np.array([M.pd_performance_pca(rng.standard_normal(c), (lambda T:T@T.T)(rng.standard_normal((c,200))), [2,6,13], R) for _ in range(500)])
    print("random PCA space, recompute",R,"mean perf k=2,6,13",v.mean(0).round(3))
n=np.array([8]*13+[9]*14)
for rate in [5,10,20]:
    passes=[]
    for _ in range(2000):
        m=np.array([rng.poisson(rate*0.3,k).mean()/0.3 for k in n])
        passes.append(m.max()-m.min()>5)
    print("untuned rate",rate,"Hz: fraction passing range>5:",np.mean(passes))
# kinematic gram replicate check & task spaces: segment length sanity
EOF
```

```
recompute helper [-0.0923 -0.0296 -0.054 ] explicit [-0.0923 -0.0296 -0.054 ]
chance k 2 mean -0.177 95th pct 0.015
chance k 3 mean -0.235 95th pct 0.007
chance k 4 mean -0.283 95th pct 0.021
chance k 6 mean -0.435 95th pct -0.019
chance k 11 mean -0.993 95th pct -0.179
random PCA space, recompute False mean perf k=2,6,13 [-0.175 -0.45  -1.339]
random PCA space, recompute True mean perf k=2,6,13 [-0.086 -0.097 -0.126]
untuned rate 5 Hz: fraction passing range>5: 0.66
untuned rate 10 Hz: fraction passing range>5: 0.993
untuned rate 20 Hz: fraction passing range>5: 1.0
```

**Agent**

**A. Outcomes** (23 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| j-array-recordings | partially_reproduced | 152 units, within 146 ± 14.6. There are 27 conditions (9 mazes × 3 versions), not 108, and 250 trials (cell 13). The criterion gives "partial" when units match and conditions are a subset. Caveat: the paper says J-array interleaved all 108 conditions, so this 27-condition session (2009-09-29) is almost certainly a different recording, and the unit match is a coincidence. |
| fig4d-mean-correlation-j-array | partially_reproduced | Mean r is 0.14–0.21 across the 8 selection readings (main reading 0.172, t-test p = 0.042) with p < 0.05 in 5 of 8. That is inside 0.054–0.231 but outside 0.13 ± 0.013. The one reading with both means in tolerance (b/medoid/separate: 0.141, 0.119) has p ≥ 0.08 (cell 15). |
| fig4abc-mean-correlation-other-datasets | blocked (data_missing) | The archive API lists 2 assets, both one Jenkins array session. There are no speed-task or single-electrode data. |
| fig4-broad-unimodal | reproduced | In every reading r runs from about −0.5 to 0.68, mean 0.14–0.21, and the dip test p ≥ 0.195. No neuron has \|r\| > 0.8 (cell 17). With n = 15–20 the dip test has little power. |
| fig4e-correlation-time-course | reproduced (borderline) | 22 of 32 readings meet the criterion. The value at onset is 0.02–0.15, and the decline starts at −257 to −325 ms, at the edge of the −300 to −100 window. In the main selection only splice reading (a) with both thresholds passes (cell 19). |
| suppfig1-population-psth-weak-movement-tuning | reproduced (nominal) | The onset difference is smaller than the preparatory difference in 16/16 readings and less than half in 12/16. With the main reading's Figure-4 neurons the ratio is 0.94 (cell 21). See problem 6. |
| fig6d-perimovement-best-j-array | reproduced | Under every S, kinematic-window and replication reading, the peri-movement best (0.117 for S a, 0.226 for S b) beats the kinematic best (≤ 0.024) and the task best (0.030) (cell 25). One selection reading (a/medoid/separate) fails, and there all spaces are ≤ 0 (cell 27). |
| fig6-perimovement-best-each-dimensionality | reproduced | The peri-movement space wins 90.9–95.5% of comparisons in every reading, above the 80% line (cell 29). |
| fig6-dimensionality-peak | partially_reproduced | It holds under S reading (a): best k = 6, k = 14 at −0.98. It fails under S (b): best k = 13, k = 14 equals the best, and best k is 11–14 in every selection reading (cell 31). The result rests on an open reading. |
| fig6-maze-task-spaces | reproduced (marginal) | Main selection: segment directions (time-split) 0.008 > 0, initial velocity 0.030 > 0, endpoints + max speed −0.045, below both references (cell 33). The notebook's "blocked, methods_underspecified" is not supported, because the criterion supplies the readings. It is fragile: segment directions are > 0 in only 2 of 8 selection readings, and the length-split variant fails. |
| fig6abc-perimovement-best-other-datasets | blocked (data_missing) | Confirmed on the archive: monkeys A and B, single-electrode J and EMG are absent. |
| fig6e-summary-rank | blocked (data_missing) | Needs A, B, J and EMG, all absent from the archive. |
| fig6-preparatory-dimensionality | not_reproduced | 12–19 PCs reach 90% in all 32 readings, against 6.3–11 (cell 39). The shuffled-label reference gives 17, so the count is dominated by noise from about 9 trials per condition (problem 1). |
| fig7a-shuffled-space-poor | reproduced | Shuffled best is −0.069 (S a) and −0.010 (S b), below the peri-movement best and below the kinematic and task bests (cell 41). |
| fig7b-window-start-slide | reproduced | Fractions are 0.911 / 0.853 / 0.962 / 0.937. Three are within 0.97 ± 0.097 and all four are within 0.846–1.067 (cell 43). |
| ap-location-no-effect-j-array | reproduced | Regression on array gives p = 0.53–0.91 in every reading (cell 46). The p-value does not depend on which array is anterior, so the unverified labelling (problem 3) does not matter here. Power is low (n = 15–20). |
| ap-location-no-effect-other-datasets | blocked (data_missing) | Single-electrode data are absent from the archive. |
| fig7c-anterior-posterior-performance | not_reproduced | "Within 10% of random halves" fails under every reading (cell 50). Raw 6-D performance for the posterior half is −0.060 (S a) and 0.049 (S b). Its "normalized > 0" pass under S a only comes from dividing two negative numbers (−0.060 / −0.107). The normalizer and the array labels are both questionable (problems 2 and 3). |
| prep-activity-more-anterior | blocked (metadata_insufficient) | The direction depends on which id prefix is PMd. The electrode x, y, z are NaN and every unit points at a PMd row, so the file cannot say. As labelled, the range measure gives fewer passing units anterior; swapping the labels reverses that. No reading reaches Fisher p < 0.05 (cell 48). The archive API metadata hold no electrode locations either. |
| fig7d-pd-consistency | reproduced | The peri-movement space has the higher mean in all comparisons: 0.698 vs 0.597, 0.613 vs 0.605, 0.615 vs 0.542, 0.729 vs 0.670. The segment-directions (time-split) gap is negligible (Wilcoxon p = 0.90) (cell 52). |
| some-neurons-better-elsewhere | reproduced | 60/76 neurons (S a) and 44/76 (S b) do better in some other space (cell 37). This is expected from noise when one value is compared with the best of 12 alternatives. |
| high-dimensional-task-spaces-underperform | reproduced | Kitchen sink (−0.24 / −0.22) and segment directions are below the peri-movement space at the same k and at the best k, under both S readings (cell 35). |
| fig8-linear-dynamics-simulation | reproduced | Under the 360-step reading, the central 95% of r over 1000 draws (about −0.40 to 0.40) contains 0.08, and performance is 1.0 (cell 54). The check is weak: the distribution is centred on 0 and very wide. |

**B. Problems**

1. **[affects a conclusion] cell 9 / `neuron_sets`: the 5 spikes/s threshold.** The paper says the lower 5 spikes/s array threshold was "acceptable given the higher signal-to-noise ratio provided by the higher trial count" (about 20 trials per condition). This dataset has about 9. I simulated untuned Poisson units with 8–9 trials per condition in a 300 ms window: 99% of 10 Hz units pass a range above 5 spikes/s, and 66% of 5 Hz units do. So most of the 76 "tuned" neurons may be untuned; median split-half r is 0.37 (cell 9). This dilutes every Figure 6 and 7 magnitude and drives the 12–19 PC count, which is close to the shuffle reference of 17. The notebook never flags it.
2. **[affects a conclusion] cell 50 / `half_perf`: the Figure 7C normalizer.** The upper limit there excludes the fitted neuron. The Supplemental Experimental Procedures say the preparatory T-matrix holds "every neuron", which corresponds to the notebook's own "upper incl. neuron" curve (0.176 at 6-D). The excluding version is not an upper limit on this data (0.061 < 0.117 for the peri-movement space). It produces denominators at or below zero and meaningless ratios (8.0, −0.71). The paper's reading was never run for 7C.
3. **[affects a conclusion] cells 44, 48, 50: array labels.** "Prefix 1 = PMd" rests only on the PMd group being listed first in the electrode table. It is unverified, and the direction of prep-activity-more-anterior and of 7C's "anterior higher" depends on it.
4. **[affects a conclusion] cell 0 / notebook header: fig6-maze-task-spaces marked blocked.** The criterion supplies its readings, and the run meets it under one of them (segment directions split by time, main selection).
5. **[affects a conclusion] cells 23 and 31: chance levels.** Neither the paper's chance statement nor a null is checked. My simulation with c = 27 gives chance for a fixed k-D space of −0.18 (k = 2), −0.44 (k = 6) and −0.99 (k = 11), which supports the paper's "above zero is better than chance". A random PCA space under S (b) gives about −0.1 flat across k, against −0.18 to −1.34 under S (a). So the missing decline above k = 10 under (b) partly reflects how out-of-sample projection shrinks the left-out condition's scores, and the two S readings are not on the same footing for fig6-dimensionality-peak.
6. **[affects a conclusion] cell 21 / `supp1`: ranking bias.** Conditions are ranked by the same noisy preparatory rates used to measure the preparatory difference. Regression to the mean therefore inflates that difference but not the onset difference, which favours the claim. With split-half r of about 0.37 the bias is large; ranking on odd trials and measuring on even trials would remove it.
7. **[affects a conclusion] cell 13: wrong recording.** The dataset is not the paper's J-array recording (108 interleaved conditions, about 2166 trials), yet the unit count is compared as if it were. The notebook never addresses identity, which the claims file left to the author.
8. **[does not affect a conclusion] cell 19 / `fig4e_traces`.** Splice reading (a) maps the go-locked trace using the median RT (354 ms). This is an author choice and is not labelled an assumption. The decline times under (a) (about −260 ms) sit next to the splice at −254 ms, but reading (b) gives similar values.
9. **[does not affect a conclusion] cells 9 and 15: SD tuning measure.** Applying the 5 spikes/s value to the SD measure leaves 0 neurons for the correlations, so that reading is degenerate rather than tested. This is partly an issue in the claims file.
10. **[does not affect a conclusion] cell 15.** "any_test_p<0.05" takes the smallest p of three tests. The criterion allows this, but the main reading passes only on the t-test (p = 0.042; Wilcoxon p = 0.071).
11. **[does not affect a conclusion] `kinematic_gram`.** Velocity enters unsmoothed while acceleration comes from smoothed velocity. This is minor.
12. **Helpers verified on synthetic input.** `pd_performance_pca(recompute=True)` matches an explicit PCA-and-project computation exactly (−0.0923, −0.0296, −0.054 both ways). Windows and bin offsets in `window_mean`, `PREP`/`PERI`/`TMAT` and the 7A reflection are correct.

**C. What I could not check**

- **Which array is PMd.** Neither the file's electrode table nor the DANDI metadata says. A notebook output of the units table's raw `location` and description fields, if present, would settle it.
- **Whether the 27 mazes (ids 12–14, 20–22, 83–85) are a subset of the paper's 108.** The paper does not list maze ids.
- **The figures.** I did not inspect the plotted images, only the printed values.
- **Outputs that would have settled conclusions:**
  - per-neuron SEs or a condition-shuffled null for each space in Figure 6;
  - Figure 7C rerun with the "upper incl. neuron" normalizer;
  - a cross-validated split for Supplemental Figure 1;
  - the fraction of units passing the 5 spikes/s threshold with condition labels shuffled;
  - a noise-corrected 90%-variance dimensionality, for example cross-validated PCA on split halves.

## End of run

18 turns, 6 minutes, result: success.
