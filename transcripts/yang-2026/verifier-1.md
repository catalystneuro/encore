# yang-2026 · verifier-1 · run 44895224713

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 256
drwxr-xr-x 6 runner runner    4096 Nov 21 11:21 .
drwxr-xr-x 8 runner runner    4096 Nov 21 11:21 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 10:34 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 10:34 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 21 11:21 .claude
-rw-r--r-- 1 runner runner       0 Nov 21 11:21 .env
-rw-r--r-- 1 runner runner       0 Nov 21 11:21 .env.development
-rw-r--r-- 1 runner runner       0 Nov 21 11:21 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 21 11:21 .env.local
-rw-r--r-- 1 runner runner       0 Nov 21 11:21 .env.production
-rw-r--r-- 1 runner runner       0 Nov 21 11:21 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 21 11:21 .env.test
-rw-r--r-- 1 runner runner       0 Nov 21 11:21 .env.test.local
drwx------ 2 runner runner    4096 Nov 21 11:21 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 10:34 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 10:34 .github
-rw-r--r-- 1 runner runner       0 Nov 21 11:21 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 21 10:34 .idea
[... 36 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "yang-2026.yaml"
}
```

```
1	# Claims for Yang (2026), "Form, Timing, and Behavioral Matching of the Population Response to
2	# ALM Photoinhibition", Research Square preprint doi:10.21203/rs.3.rs-11447300/v1, on DANDI
3	# 000363 (Mesoscale Activity Map, Chen et al. 2024, Cell 187:676-691), which the paper reuses.
4	#
5	# Provenance. Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub
6	# Actions"), 2026-11-21, protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).
7	#
8	# Text read. The preprint, version 1 (posted 2026-10-22), from
9	# paper/10.21203-rs.3.rs-11447300-v1.txt: abstract, Introduction, Results, Materials and
10	# Methods, Discussion, figure legends of Figures 1 to 3, Table 1, and the Extended Data legends
11	# (Figures 1-1, 2-1, 3-1). There is no separate supplement; the Extended Data are figures whose
12	# legends are in the text. No PDF was supplied and no figure was read. Values shown only in a
13	# figure (per-mouse points, curves) are not available; claims rest on the numbers the text and
14	# Table 1 print.
15	#
16	# Code read. None. Code Accessibility says the code "has been deposited in a private GitHub
17	# repository and will be made publicly available upon publication". No method detail below is
18	# settled by code. The analyses used Python 3.12, NumPy and scikit-learn logistic regression
19	# (lbfgs), and one random seed, 17, for splits, folds and match order (Methods, Code and data;
20	# Statistics).
[... 858 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_yang_2026.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain']))
        elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1735 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	==================== 0 markdown
2	# Reproducing Yang (2026) from dandiset 000363
3	
4	Paper. Yang Z (2026). Form, Timing, and Behavioral Matching of the Population Response to ALM
5	Photoinhibition. Research Square preprint,
6	[doi:10.21203/rs.3.rs-11447300/v1](https://doi.org/10.21203/rs.3.rs-11447300/v1), version 1 (posted
7	2026-10-22). The claims file (`claims/yang-2026.yaml`) was written from the full text of that
8	preprint: the main text, the Materials and Methods, the legends of Figures 1 to 3, Table 1 and the
9	Extended Data legends. The paper's code is in a private repository and was not read.
10	
11	Dandiset. [DANDI:000363](https://dandiarchive.org/dandiset/000363/0.231012.2129), the Mesoscale
12	Activity Map dataset of Chen et al. (2024), version 0.231012.2129. The paper names this version
13	in its Methods ("Dataset" and "Code and data") and in its acknowledgments, and it is also the most
14	recent published version, so it is pinned. The earlier published versions (0.221127.2345 to
15	0.230822.0128) list the same 174 assets at sizes of 19 to 67 GB in all, against 65.7 TB here; the
16	pinned version adds the raw electrical series. The analysis reads only the processed arrays
17	(trials, events, units, video keypoints), and the raw series are never read. The versions are
18	listed in the first data check.
19	
20	What is used. The 174 session files are surveyed for photoinhibition; the 112 late-delay
[... 694 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 715,
 "limit": 520
}
```

```
715	
716	==================== 25 markdown
717	## fig1-1c-fraction-vs-neurons
718	
719	> Joint fractions decrease with the number of neurons in a session.
720	==================== 26 code
721	fp = FR[FR.reading == ",".join(PRIMARY)]
722	rho, p = stats.spearmanr(fp.n_units, fp.joint)
723	print(f"pooled over regions: Spearman rho = {rho:.3f}, p = {p:.2g}, n = {len(fp)} region entries")
724	for r in mam.REGIONS:
725	    g = fp[fp.region == r]
726	    rr, pp = stats.spearmanr(g.n_units, g.joint)
727	    print(f"  {r:9s} rho = {rr:.3f}, p = {pp:.2g}, n = {len(g)}")
728	for rd in jt.index:
729	    g = FR[FR.reading == rd]
730	    print(f"reading {rd:20s} pooled rho = {stats.spearmanr(g.n_units, g.joint)[0]:.3f}")
731	--OUT--
732	pooled over regions: Spearman rho = -0.366, p = 3e-10, n = 278 region entries
733	  ALM       rho = -0.580, p = 1.1e-09, n = 93
734	  striatum  rho = -0.283, p = 0.051, n = 48
[... 500 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1235,
 "limit": 510
}
```

```
1235	seed +1000: regions inside 4 of 5
1236	seed +2000: regions inside 5 of 5
1237	seed +3000: regions inside 4 of 5
1238	seed +4000: regions inside 4 of 5
1239	
1240	==================== 49 markdown
1241	## Decoding (shared by table1-decoding-early-vs-prelick and fig2a-decoding-rises-after-go)
1242	
1243	Lick direction from laser and control trials together (M8 reading b). Reading a, laser trials
1244	alone, is counted first: no region entry has the 40 trials and 15 per direction that the
1245	Methods require of a session, since a session has at most 67 bilateral trials and a median of 36. The early and
1246	pre-lick windows choose the penalty inside each training fold; the Go-aligned curve uses C = 1.
1247	Units are those kept in the axes windows, the pre-lick window and every 100 ms Go bin. The claim
1248	seeds are used for the folds, and four more seeds for the seed check.
1249	==================== 50 code
1250	T4 = time.time()
1251	G100 = list(range(len(mam.go100_starts())))
1252	DEC_IN = []
1253	laser_only_ok = 0
1254	for s in S:
[... 482 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "mam.py"
}
```

```
1	"""Loading and measures for the late-delay photoinhibition sessions of dandiset 000363.
2	
3	Yang (2026), "Form, Timing, and Behavioral Matching of the Population Response to ALM
4	Photoinhibition", Research Square preprint doi:10.21203/rs.3.rs-11447300/v1, which reanalyses
5	the Mesoscale Activity Map dataset of Chen et al. (2024), DANDI 000363.
6	
7	Each NWB file holds one session: the trial table, behavioural events (Go cue, licks,
8	photostimulation onsets with a control code), the photostimulation sites, video keypoints, and
9	the units (spike times, a classifier label, the electrode of each unit). Files are streamed from
10	the archive at the pinned version; only the arrays needed are read, and nothing is written to disk.
11	The raw electrical series, which make up almost all of each file, are never read.
12	
13	Where the parameters come from. "Claims" is claims/yang-2026.yaml, whose shared methods M1 to M10
14	cite the paper; "Methods" is the paper's Materials and Methods.
15	
16	- Sessions, laser and control trials (claims M1; Methods, Dataset, paragraph 2): bilateral
17	  trials are those whose photostimulation control code has a site list with ALM on both sides;
18	  a session enters when the median bilateral onset is within 0.08 s of -0.5 s from Go; control
19	  trials have no photostimulation and no early lick. Whether laser trials with an early lick are
20	  kept is open; `LASER_EARLY` names the readings ("keep", "drop").
[... 646 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc -w *.txt; grep -n -i -E "seed|50 ms|early window|same pairs|decod|Example session|pre-specified|plane|principal|control-split|split" *.txt | cut -c1-600
```

```
7540 10.21203-rs.3.rs-11447300-v1.txt
10:Low-dimensional coding axes give a compact description of task-related population activity, but how they relate to the population change produced by a causal perturbation is less clear. We reanalyzed multi-probe Neuropixels recordings spanning anterior lateral motor cortex (ALM), striatum, thalamus, midbrain, and medulla in mice performing a memory-guided directional licking task, with bilateral ALM photoinhibition during the last 0.5 s of the delay. We compared the laser–control population difference with choice and action axes fit on control trials, and followed it from laser onset to the
43:than that between size-matched splits of control trials. After the Go cue, single trials became 
113:0.011; 19 mice, 93 sessions). In a pre-specified ALM session near that mouse mean, laser and 
120:population difference itself was large. Relative to a size-matched split of control trials, the laser 
122:8.7 in the other regions (Fig. 1E). After the control-split projection was removed, joint fractions 
129:Lick decoding rises without a matching rise on the choice axis 
131:before the lick than in the early window. Balanced accuracy rose from 0.567–0.611 early to 
134:bin centered 250 ms after Go it was 0.73–0.77 (Fig. 2A). The pre-lick window is aligned to the 
137:The choice-axis share of the laser-minus-control vector did not rise with decoding accuracy (Fig. 
143:Go-aligned grid remained about 0.04–0.08 through the delay. In the bin centered 250 ms after 
152:Decoding accuracy increased, and the action axis took a larger share after Go, while most of 
154:The early difference and the later rise in decoding could still reflect differences in lick direction or 
161:distance minus the distance between two control trials drawn from the same pairs. The primary 
180:and were closer again at Go (Fig. 3B). That plane held 25% of the session’s early matched 
181:difference. The first principal component of control-trial activity orthogonal t
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 105,190p *.txt; echo ----; sed -n 200,300p *.txt
```

```
Most of the population difference 20–120 ms after bilateral laser onset lay outside the axes that 
distinguish lick direction. Those axes were fit on control trials only: lick right minus lick left, from 
600 ms before Go until Go for the choice axis, and from Go to 300 ms after Go for the action 
axis. Jaw, nose, and tongue position were removed from the choice-axis fit. The early difference 
was laser minus control, 20–120 ms after laser onset, within instructed side (Fig. 1A). 
Across regions, the joint fraction of that difference inside the two-axis subspace was 0.052–
0.080 (Table 1; Fig. 1C,D). The choice axis alone held 0.030–0.059 and the action axis 0.021–
0.032. Thalamus had the highest joint fraction (0.080 ± 0.016) and ALM the lowest (0.052 ± 
0.011; 19 mice, 93 sessions). In a pre-specified ALM session near that mouse mean, laser and 
control means were separated mainly along the early difference orthogonal to both axes (Fig. 
1B). 

4 
The axes are not orthogonal. Their cosine ranged from 0.29 ± 0.04 in thalamus to 0.52 ± 0.03 in 
ALM, which is why the joint fraction, rather than the angle, is the summary (Fig. 1-1A). The 
population difference itself was large. Relative to a size-matched split of control trials, the laser 
difference was larger in every mouse. The median ratio across mice was 152 in ALM and 3.3–
8.7 in the other regions (Fig. 1E). After the control-split projection was removed, joint fractions 
remained low, with mouse means ranging from about 0.003 in medulla to 0.099 in thalamus 
(Fig. 1-1B). Joint fractions decreased with the number of neurons in a session (Fig. 1-1C). 
[... 168 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import numpy as np, mam
rng=np.random.default_rng(0)
# fractions
c=np.zeros(5);c[0]=1;a=np.zeros(5);a[0]=.6;a[1]=.8
Q,_=np.linalg.qr(np.c_[c,a]); d=np.array([1,1,1,0,0.])
print(mam.fractions(d,{"Q":Q,"choice":c,"action":a}))  # expect joint 2/3, choice 1/3, action (1.4^2)/3
# match
n=200
ts={"rt":rng.uniform(0.1,0.6,n),"lick_dir":rng.choice([-1,1],n),"instr":rng.choice([-1,1],n),
    "laser":np.r_[np.ones(40,bool),np.zeros(160,bool)],"control":np.r_[np.zeros(40,bool),np.ones(160,bool)],"sides":[-1,1]}
P=mam.match(ts,np.random.default_rng(1),"closest")
P=np.array(P); print(len(P), np.abs(ts["rt"][P[:,0]]-ts["rt"][P[:,1]]).max(),
 all(ts["lick_dir"][P[:,0]]==ts["lick_dir"][P[:,1]]), all(ts["instr"][P[:,0]]==ts["instr"][P[:,1]]),
 len(set(P[:,1])|set(P[P[:,2]>=0,2]))==len(P)+ (P[:,2]>=0).sum())
h=P[:,2]>=0; print("2nd ctrl dRT max", np.abs(ts["rt"][P[h,1]]-ts["rt"][P[h,2]]).max(), all(ts["lick_dir"][P[h,1]]==ts["lick_dir"][P[h,2]]))
# residual: identical distributions -> ~0
Z=rng.normal(size=(n,30)); print("resid null", mam.residual([Z],P)[0])
Z2=Z.copy(); Z2[:40]+=1; print("resid shift 1 in 30 units (expect >0)", mam.residual([Z2],P))
# control splits size
ts2=dict(ts); sp=mam.control_splits(Z,ts2,np.random.default_rng(2),20)
print("split energy", np.mean([v@v for v in sp]), "expected approx 30*2/20 =",30*2/20)
print(mam.mouse_summary({("m1","s1"):1.,("m1","s2"):3.,("m2","s3"):5.}))
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
ls /usr/bin/python3* ~/.local/bin 2>/dev/null; which -a python python3; for p in $(which -a python3 python 2>/dev/null); do $p -c "import numpy,sys;print(sys.executable,numpy.__version__)" 2>&1|tail -1; done; ls /opt /usr/local/bin 2>/dev/null | head -30
```

```
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.14
/usr/bin/python3.14-config

/home/runner/.local/bin:
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/usr/bin/python3
/bin/python3
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -m venv v >/dev/null 2>&1 && ./v/bin/pip install -q numpy 2>&1 | tail -2; ./v/bin/python -c "import numpy;print(numpy.__version__)"
```

```
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: /tmp/claude-1001/v/bin/python3 -m pip install --upgrade pip
2.5.5
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  mkdir -p $TMPDIR/stubs/dandi; touch $TMPDIR/stubs/h5py.py $TMPDIR/stubs/remfile.py $TMPDIR/stubs/dandi/__init__.py; echo "DandiAPIClient=None" > $TMPDIR/stubs/dandi/dandiapi.py
PYTHONPATH=$TMPDIR/stubs:. $TMPDIR/v/bin/python - <<'EOF'
import numpy as np, mam
rng=np.random.default_rng(0)
c=np.zeros(5);c[0]=1;a=np.zeros(5);a[0]=.6;a[1]=.8
Q,_=np.linalg.qr(np.c_[c,a]); d=np.array([1,1,1,0,0.])
print(mam.fractions(d,{"Q":Q,"choice":c,"action":a}), "expect joint .667 choice .333 action", 1.4**2/3)
n=200
ts={"rt":rng.uniform(0.1,0.6,n),"lick_dir":rng.choice([-1,1],n),"instr":rng.choice([-1,1],n),
    "laser":np.r_[np.ones(40,bool),np.zeros(160,bool)],"control":np.r_[np.zeros(40,bool),np.ones(160,bool)],"sides":[-1,1]}
P=np.array(mam.match(ts,np.random.default_rng(1),"closest"))
h=P[:,2]>=0
used=list(P[:,1])+list(P[h,2])
print(len(P), "max dRT",np.abs(ts["rt"][P[:,0]]-ts["rt"][P[:,1]]).max(), "same dir",all(ts["lick_dir"][P[:,0]]==ts["lick_dir"][P[:,1]]),
 "same side",all(ts["instr"][P[:,0]]==ts["instr"][P[:,1]]), "no reuse", len(set(used))==len(used))
print("2nd ctrl dRT max", np.abs(ts["rt"][P[h,1]]-ts["rt"][P[h,2]]).max(), all(ts["lick_dir"][P[h,1]]==ts["lick_dir"][P[h,2]]), all(ts["instr"][P[h,1]]==ts["instr"][P[h,2]]))
Z=rng.normal(size=(n,30)); print("resid null", mam.residual([Z],P)[0])
Z2=Z.copy(); Z2[:40]+=1; print("resid shift", mam.residual([Z2],P), "expected lc ~ sqrt(2*30+30)=",np.sqrt(90), "cc", np.sqrt(60))
sp=mam.control_splits(Z,ts,np.random.default_rng(2),20)
print("split energy", np.mean([v@v for v in sp]))
print(mam.mouse_summary({("m1","s1"):1.,("m1","s2"):3.,("m2","s3"):5.}))
# side_diff weighting
Zs=np.r_[np.ones((10,2)),np.zeros((10,2))]; instr=np.r_[np.ones(5),-np.ones(5),np.ones(5),-np.ones(5)]
la=np.r_[np.ones(10,bool),np.zeros(10,bool)]
print(mam._side_diff(Zs,la,~la,instr,[-1,1],la))
EOF
```

```
{'joint': 0.6666666666666666, 'choice': 0.3333333333333333, 'action': 0.6533333333333332, 'energy': 3.0} expect joint .667 choice .333 action 0.6533333333333332
40 max dRT 0.05609706655537855 same dir True same side True no reuse True
2nd ctrl dRT max 0.07304143644646244 True True
resid null 0.05743326754502842
resid shift (1.7076588692967967, 9.236072743654292, 7.528413874357495) expected lc ~ sqrt(2*30+30)= 9.486832980505138 cc 7.745966692414834
split energy 1.6330269154214019
(3.5, 1.4999999999999998, 2, 3, {'m1': 2.0, 'm2': 5.0})
[1. 1.]
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/pip install -q scikit-learn 2>&1 | grep -v notice; PYTHONPATH=$TMPDIR/stubs:. $TMPDIR/v/bin/python - <<'EOF'
import numpy as np, mam
rng=np.random.default_rng(3)
n=120; X=rng.normal(size=(n,50)); y=rng.choice([-1,1],n); instr=rng.choice([-1,1],n); ctrl=rng.random(n)<.6
print("null", np.mean([mam.decode(X,y,instr,ctrl,s) for s in range(5)]))
X2=X.copy(); X2[:,0]+=0.8*y
print("signal", mam.decode(X2,y,instr,ctrl,1), mam.decode(X2,y,instr,ctrl,1,fixed_C=1.0))
EOF
```

```
null 0.5190211345939933
signal 0.7497219132369299 0.6738042269187987
```

**Agent**

**Verifier report, round 1: Yang (2026) on DANDI:000363**

The claims file has 25 claims and the notebook tests all 25, with none blocked. My outcomes are 15 reproduced and 10 partially reproduced, with none not reproduced or blocked. I checked the helper functions on synthetic inputs and they behave as specified. `fractions` gives the right joint, choice and action values. `match` keeps the side and lick direction, stays within the 100 ms caliper and never reuses a control. `residual` is about 0 under the null and positive when shifted. `control_splits` gives the expected split energy. `mouse_summary` and `_side_diff` weight correctly. `decode` gives 0.52 on random labels and about 0.75 with a signal, so there is no label leakage.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| session-counts | reproduced | Cell 13: 168 photoinhibition sessions. With early-lick laser trials dropped, every region count equals Table 1 exactly (19/93, 13/48, 10/31, 16/71, 8/35). |
| table1-early-joint-fraction | reproduced | Cell 15: own,fill,licks gives 0.0549 / 0.0601 / 0.0844 / 0.0587 / 0.0521, 5/5 within tolerance, all below 0.10. Lowest is medulla, not ALM; the claim reports this but does not require it. |
| table1-early-axis-fractions | reproduced | Cell 18: 10/10 values within tolerance under both "fill" readings. |
| axes-cosine | reproduced | Cell 20, signed cosine: thalamus 0.297, ALM 0.523, and the other three regions lie between them. |
| fig1e-laser-vs-control-split | partially_reproduced | Cell 22: every mouse ratio is above 1 (minimum 1.16). ALM 147–156 and highest other 7.6–8.8 are within tolerance. Lowest other is 2.73–2.84 (striatum) against 3.3 ± 0.33, out under every reading and seed. |
| fig1-1b-corrected-joint-fraction | partially_reproduced | Cell 24: no combination of correction and reading puts both medulla and thalamus in tolerance; the nearest miss is thalamus 0.1094 against an upper bound of 0.1089. All region means are below 0.15. |
| fig1-1c-fraction-vs-neurons | reproduced | Cell 26: pooled Spearman ρ = −0.366, p = 3e-10, n = 278. |
| fig1-1d-without-video-regression | reproduced | Cell 28: thalamus 0.1158, within 0.109 ± 0.0109 and above 0.0844. Every region is below 0.15. |
| fig1b-example-session | partially_reproduced | Cell 64: ses-20200922T135318 has 130 units and joint fraction 0.0528, both within tolerance. The rule picks ses-20210419T161140 instead, by a distance margin of 0.0001 (0.00200 against 0.00210). |
| table1-decoding-early-vs-prelick | partially_reproduced | Cell 52: pre-lick accuracy exceeds early in every region, but only 7/10 values are within tolerance (6–7 across seeds; 8 needed). Early accuracies are low in ALM, striatum and medulla. Only M8 reading (b) was run (problem 1). |
| fig2a-decoding-rises-after-go | reproduced | Cell 54: the 250 ms bin is 0.721–0.782, delay bins 0.540–0.588, and the 250 ms bin is above every delay bin. Holds for both bin steps and all seeds. |
| matched-reaction-time | reproduced | Cell 34: median 0.2885 s, quartiles 0.2202 and 0.3848 s. |
| fig2d-choice-share-flat | partially_reproduced | Cell 56: early means fall outside 0.0315–0.0506 (thalamus 0.053 or 0.068, midbrain 0.0309) and striatum pre-lick (0.0248) is out. A rise beyond the SEM appears in medulla only. Midbrain's raw mean does rise (+0.006, below its SEM), so a literal "does not rise" reading would give not_reproduced (problem 5). |
| fig2e-action-share-rises | partially_reproduced | Cell 58: the rise holds in every region and medulla is largest (0.128, within tolerance). Lowest pre-lick (0.030 in thalamus) and lowest early (0.019–0.022) are out. |
| fig2b-go-aligned-joint-fraction | partially_reproduced | Cell 60, early-fraction entries: 5/5 values at 250 ms are within tolerance. Delay bins leave 0.036–0.088 (medulla 0.099 at −600 ms, thalamus 0.034–0.035) under both bin steps. |
| fig2-1-energy-outside-subspace | partially_reproduced | Cell 62: ALM peaks in the onset bin and falls after it in both readings. Reading (b) gives an onset bin of 25.8, within tolerance, but thalamus reaches 1.185 (above 1.1). Reading (a) keeps the other regions below 1.1, but its onset bin is 9.8. "Before onset" is 0.03–0.05 against 0.09 ± 0.009 in both. |
| fig3a-matched-pairs | reproduced | Cell 32: 2,667 pairs (each session counted once), median \|ΔRT\| 1.3 ms, largest 99.1 ms. |
| table1-prelick-residual | reproduced | Cell 36, closest/drop/mean: 1.552 / 1.358 / 2.912 / 0.762 / 0.528, 5/5 within tolerance, no mouse ≤ 0, for all five seeds. |
| fig3e-residual-ratio | reproduced | Cell 38: 5/5 within tolerance under both ratio readings. |
| fig3-1ab-distances-scale | reproduced | Cell 40: thalamus 20.0 above midbrain 12.07; Spearman ρ = 0.99, p ≈ 1e-216. |
| fig3-1d-matching-keeps-distance | reproduced | Cell 42: matched laser-control distance exceeds control-control in every region. Matching lowers the laser-control distance by 0.35–0.95. |
| fig3-1c-alm-early-residual | reproduced | Cell 44, on the two-50 ms-bin reading: 12.59 ± 2.00, ratio to pre-lick 8.1. On the single 20–120 ms window the claims file implies, it is 18.36, which would be partial (problem 3). |
| fig3c-residual-time-course | reproduced | Cell 46: 7/7 values within tolerance and every named peak bin holds, for all five seeds. |
| fig3c-late-residuals | reproduced | Cell 48: 5/5 regions inside the bounds at the claim seed, but only 4/5 at seeds +1000, +3000 and +4000 (problem 2). |
| fig3b-example-plane | partially_reproduced | Cell 66: the separation is smaller at Go in every variant. The plane fraction is 0.70–1.00 against 0.25 and PC1 is 0.035–0.085 against 0.04 ± 0.004; both are out. |

### B. Problems

1. **[affects a conclusion]** Cells 49/50, decoding. The markdown says no region entry passes the 40-trial / 15-per-direction rule with laser trials alone. The cell's own output says 26 entries do. So M8 reading (a), laser trials only, was never run, though it could have been for 26 entries. The Methods sentence "There is no paired trial without laser" points towards that reading. This leaves table1-decoding-early-vs-prelick (partial at 7/10), fig2a, and set (a) of fig2d/fig2e untested under one of the readings the claims file allows.
2. **[affects a conclusion]** `mam.seed`. Every random step uses `crc32("yang-2026/<claim>") + k`. The paper and the criteria name seed 17 (Methods, Statistics; claims M8 and M9, fig1e, fig3-1d). Seed 17 is never run, and the notebook does not state this as an assumption. Most results are stable across the five seeds. fig3c-late-residuals is not: it is reproduced at seed +0 and +2000 and partial at the other three.
3. **[affects a conclusion]** Cell 44, fig3-1c. The two-50 ms-bin early residual is the notebook's own reading. It rests on a Methods passage ("primary window … divided into 50 ms bins. The same pairs were scored in the early window"). The claims file does not list this as open, and its criterion ("M4, M5 window") reads as one 100 ms window, which gives 18.36. The reading is reasonable: it matches the paper's 12.6 ± 2.0 almost exactly. Still, the outcome turns on it, and the claims file misses an open detail here.
4. **[affects a conclusion]** Cell 64, fig1b-example-session. Selection is run only under the primary reading (own, fill, licks), and it is decided by 0.0001. Under the other M3/M5 readings both the ALM mouse mean and the session fractions change, so the rule might select ses-20200922T135318. Those readings were not run.
5. **[affects a conclusion]** fig2d criterion. The partial clause, "mouse-level choice fraction does not rise in at least four regions", does not say whether the SEM line applies. Midbrain rises by +0.006, less than its SEM of 0.006. The notebook's count of 4 non-rising regions uses the SEM rule. Without it the count is 3 and the outcome becomes not_reproduced. This is an ambiguity in the claims file, not a code error.
6. **[does not affect a conclusion]** Cell 11 onward. Only the early-lick-dropped reading of M1 is carried past the session counts. That follows the claims file's "best-matching combination first" rule, but reading (a), keeping them, is not run for any other claim.
7. **[does not affect a conclusion]** `decode`. z-scoring and the unit SD screen use all control trials, test fold included, before cross-validation. No labels are used, and the synthetic null gives 0.52.
8. **[does not affect a conclusion]** Cell 22. With 0 small sides, the "disjoint" and "independent" columns are the same method on different random draws, not two readings.
9. **[does not affect a conclusion]** Cell 49 markdown. "At most 67 bilateral trials and a median of 36" per session is printed by no cell.
10. **[does not affect a conclusion]** M5 "drop" reading (`axes`). Because the tongue is undetected in 82% of trials (cell 8), dropping trials without keypoints removes about 82% of control trials from the choice-axis fit, not just from the regression. That explains why the "drop" readings diverge. It is a legitimate reading of the claims file but worth knowing.

### C. What I could not check

- **Laser-only decoding:** accuracies for the 26 qualifying entries. Adding them would settle problem 1.
- **Seed 17:** results at seed 17 for the splits, folds and matching, for any claim. Above all for fig3c-late-residuals, along with which region fails at seeds +1000, +3000 and +4000; cell 48 prints only the count.
- **Example session under other readings:** the fig1b rule's selection and candidate distances under the other seven readings.
- **Bilateral trials per session:** a cell printing the per-session counts of bilateral and laser trials, to support the "67 / 36" statement.
- **The data:** I did not download it, as instructed. Every number derives from streamed arrays in cells 1–8, and the internal checks there look sound: the laser effect in ALM is in every session, the tongue detections line up with the lick times, and the onsets fall within 0.7 ms of the session median. Since no claim is blocked, no archive check was needed for step 4.

## End of run

15 turns, 4 minutes, $1.69 at API prices, result: success.
