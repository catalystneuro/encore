# 000129 · verifier-1 · run 40774224505

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat *.y*ml *.md 2>/dev/null | head -300
```

```
total 188
drwxr-xr-x 6 runner runner   4096 Oct 28 22:13 .
drwxr-xr-x 7 runner runner   4096 Oct 28 22:13 ..
crw-rw-rw- 1 nobody nogroup  1, 3 Oct 28 21:41 .bash_profile
crw-rw-rw- 1 nobody nogroup  1, 3 Oct 28 21:41 .bashrc
drwxr-xr-x 5 runner runner   4096 Oct 28 22:13 .claude
-rw-r--r-- 1 runner runner      0 Oct 28 22:13 .env
-rw-r--r-- 1 runner runner      0 Oct 28 22:13 .env.development
-rw-r--r-- 1 runner runner      0 Oct 28 22:13 .env.development.local
-rw-r--r-- 1 runner runner      0 Oct 28 22:13 .env.local
-rw-r--r-- 1 runner runner      0 Oct 28 22:13 .env.production
-rw-r--r-- 1 runner runner      0 Oct 28 22:13 .env.production.local
-rw-r--r-- 1 runner runner      0 Oct 28 22:13 .env.test
-rw-r--r-- 1 runner runner      0 Oct 28 22:13 .env.test.local
drwx------ 2 runner runner   4096 Oct 28 22:13 .git
crw-rw-rw- 1 nobody nogroup  1, 3 Oct 28 21:41 .gitconfig
crw-rw-rw- 1 nobody nogroup  1, 3 Oct 28 21:41 .github
-rw-r--r-- 1 runner runner      0 Oct 28 22:13 .gitmodules
crw-rw-rw- 1 nobody nogroup  1, 3 Oct 28 21:41 .idea
crw-rw-rw- 1 nobody nogroup  1, 3 Oct 28 21:41 .mcp.json
[... 323 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 300,900p 10.1088-1741-2552-aa9e95.yaml
```

```
for KFobs and the UKF.
  source: Results, The rEFH against its nearest rivals, all session and monkeys, paragraph 3;
    Figure 4
  quote: the best-decoded kinematic variable is velocity for the rEFH, but position for KFobs and
    the UKF
  criterion: Session-weighted mean SNR, averaged over x and y, at 64 ms. Reproduced when velocity
    has the highest SNR of the three variables for the rEFH (+KF) and position the highest for
    KFobs and for the UKF. The ordering in each session is reported.
- id: fig4-task-similar
  statement: The relative advantage of the rEFH (+KF) does not differ visibly between the
    center-out task (monkey C) and the point-to-point task (monkeys I and L); monkey L's
    sessions differ most.
  source: Results, Reaching task, paragraph 1; Figure 4
  quote: But across tasks, the relative advantage of the rEFH (+KF) does not differ visibly (there
    are too few sessions from monkey C for a statistical test)
  data: elsewhere
  where: Monkey C data, Dyer et al. 2016, biorxiv.org/content/early/2016/10/14/080861 (reference
    6); no archive identifier is given in the paper
  criterion: The paper runs no test. Per session at 64 ms, the SNR difference rEFH (+KF) minus
    KFobs and minus UKF for velocity and acceleration. Reproduced when monkey C's two sessions
[... 336 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" 10.1088-1741-2552-aa9e95.yaml; python3 - <<'EOF'
import json
for fn in ['reproduce_makin_2018.ipynb','binwidth_training_neurons.ipynb']:
    nb=json.load(open(fn))
    print('#'*30,fn)
    for i,c in enumerate(nb['cells']):
        print(f'---- [{i}] {c["cell_type"]}')
        print(''.join(c['source']))
        for o in c.get('outputs',[]):
            if 'text' in o: print('>>',''.join(o['text']))
            elif 'data' in o:
                d=o['data']
                print('>>', ''.join(d.get('text/plain','')) if 'text/plain' in d else list(d))
EOF
```

```
<persisted-output>
Output too large (53.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/8ac11715-2bcd-4596-9a01-fc725f2ebd11/tool-results/b00hk4rd3.txt

Preview (first 2KB):
31
############################## reproduce_makin_2018.ipynb
---- [0] markdown
# Reproducing Makin et al. (2018) from dandiset 000129: decoders at 64 ms

**Paper.** Makin JG, O'Doherty JE, Cardoso MMB, Sabes PN (2018). Superior arm-movement decoding
from cortex with a new, unsupervised-learning algorithm. *J. Neural Eng.* 15, 026010.
[doi:10.1088/1741-2552/aa9e95](https://doi.org/10.1088/1741-2552/aa9e95)

**Dataset.** [DANDI:000129](https://dandiarchive.org/dandiset/000129/0.241017.1444) version
0.241017.1444 (doi:10.48324/dandi.000129/0.241017.1444), "MC_RTT", streamed from the archive. The
paper cites no version of the dandiset; 0.241017.1444 is the only published version (the draft
holds the same two assets, 50,965,512 bytes, and differs only in its title), so it is pinned.

**Claims.** `claims/000129/10.1088-1741-2552-aa9e95.yaml`, written from the version of record
(main text, Methods and legends; the paper has no supplement) and the paper's code
[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/8ac11715-2bcd-4596-9a01-fc725f2ebd11/tool-results/b00hk4rd3.txt"
}
```

```
1	31
2	############################## reproduce_makin_2018.ipynb
3	---- [0] markdown
4	# Reproducing Makin et al. (2018) from dandiset 000129: decoders at 64 ms
5	
6	**Paper.** Makin JG, O'Doherty JE, Cardoso MMB, Sabes PN (2018). Superior arm-movement decoding
7	from cortex with a new, unsupervised-learning algorithm. *J. Neural Eng.* 15, 026010.
8	[doi:10.1088/1741-2552/aa9e95](https://doi.org/10.1088/1741-2552/aa9e95)
9	
10	**Dataset.** [DANDI:000129](https://dandiarchive.org/dandiset/000129/0.241017.1444) version
11	0.241017.1444 (doi:10.48324/dandi.000129/0.241017.1444), "MC_RTT", streamed from the archive. The
12	paper cites no version of the dandiset; 0.241017.1444 is the only published version (the draft
13	holds the same two assets, 50,965,512 bytes, and differs only in its title), so it is pinned.
14	
15	**Claims.** `claims/000129/10.1088-1741-2552-aa9e95.yaml`, written from the version of record
16	(main text, Methods and legends; the paper has no supplement) and the paper's code
17	(github.com/jgmakin/rbmish at commit 700062f5).
18	
19	**What the dataset holds.** One session of monkey I (Indy), M1 array only, from the Neural Latents
20	Benchmark: a training file with 649.1 s of sorted-unit spikes and kinematics, and a test file with
[... 903 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/8ac11715-2bcd-4596-9a01-fc725f2ebd11/tool-results/b00hk4rd3.txt",
 "offset": 923
}
```

```
923	rows = []
924	for w in widths:
925	    S = SNR[("bin", w)]
926	    for v in ("vel", "acc"):
927	        db, pc, who = advantage(S, v)
928	        rows.append(dict(width=w, var=v, refh_kf=S.loc["refh_kf", v], best_other=who, adv_dB=db, adv_pct=pc))
929	A = pd.DataFrame(rows)
930	print(A.round(2).to_string(index=False))
931	def rises(vals, tol):
932	    vals = np.asarray(vals)
933	    return bool(vals[-1] > vals[0] and np.all(np.diff(vals) >= -tol))
934	verdict = {}
935	for reading, col, tol in (("a dB", "adv_dB", 0.2), ("b percent", "adv_pct", 2.0)):
936	    ok = True
937	    for v in ("vel", "acc"):
938	        sub = A[A["var"] == v]
939	        snr_ok, adv_ok = rises(sub.refh_kf, 0.2), rises(sub[col], tol)
940	        print(f"reading {reading}, {v}: rEFH (+KF) SNR rises {snr_ok}; advantage rises {adv_ok}")
941	        ok &= snr_ok and adv_ok
942	    verdict[reading] = ok
[... 194 more lines not kept]
```

**Agent**

I've read both notebooks; now reading the helper module.

**Agent calls Read**

```json
{
 "file_path": "makin.py"
}
```

```
1	"""Loading and decoders for Makin, O'Doherty, Cardoso & Sabes (2018) on dandiset 000129.
2	
3	Where each choice comes from is marked in the docstrings:
4	  [claims]  the criterion or the header of claims/000129/10.1088-1741-2552-aa9e95.yaml
5	  [paper]   a passage of the paper (Methods unless said otherwise)
6	  [code]    the paper's code, https://github.com/jgmakin/rbmish at commit 700062f5
7	  [assumed] an assumption, with the reason
8	  [standard] a standard choice for a detail that cannot change a result
9	
10	The dandiset holds one session of monkey I (Indy, M1 array only). Its training file
11	holds 649.1 s of spikes and kinematics; its test file holds spikes only (the Neural
12	Latents Benchmark withholds the behaviour), so only the training file is used.
13	"""
14	import os
15	
16	import h5py
17	import numpy as np
18	import remfile
19	import requests
20	from scipy.signal import butter, filtfilt
[... 689 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -R .claude | head; cat .claude/*.md 2>/dev/null | head -50
```

```
.claude:
agents
commands

.claude/agents:

.claude/commands:
```

**Agent**

The code review is mostly done. Next I'm checking a few paper passages and querying the DANDI API for the archive contents.

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "standardiz|standard-normal|standard normal|hash|0\.5 Hz|subsampl|1/100|percent of|Butterworth|nearest|best-decoded" *.txt | head -60
```

```
163:nearest competitor in signal-to-noise ratio of 0.14 dB (position), 1.60 dB (velocity) and 1.2 dB (acceleration)—although 
217:with a causal IIR bandpass filter (fourth-order Butterworth; 
227:threshold crossings to up to four units per channel. For all sessions we preserved an unsorted ‘noise’ or ‘hash’ unit for each 
233:Finally, units with spike rates below 0.5 Hz were discarded. This left between 171 and 413 units for monkey I, and 
244:After acquisition, the position data were non-causally lowpass filtered to reject sensor noise (4th order Butterworth; 
247:state (position, velocity, acceleration) was subsampled, and 
253:we removed neurons firing below 0.5 Hz, as for the other animals, resulting in 75 and 91 units for monkey C’s two sessions.
364:convergence (a cross entropy decrease less than 1/100 of a 
365:percent of the total decrease) or for 100 epochs, whichever 
729:and kinematic state subsampled at 15.625 Hz, i.e. 64 ms bins, 
874:KFobs—and nearly twice that of its nearest rival, which is 
919:against its nearest rivals (abscissa), the KF (top row) and the UKF (bottom row), for all sessions and animals, and 64 ms bins. The lines are 
936:The rEFH against its nearest rivals, all session and monkeys
938:directly compare the rEFH (+KF) and its nearest rivals, the 
959:note that the best-decoded kinematic variable is velocity for 
1122:by first standardizing the data (separately for each neuron), 
1123:and then treating each unit as a standard normal variate [12]. 
1129:rEFH’s nearest rival), and then averaging across animals, sessions, and x and y coordinates. The three progressively darker 
1131:units from decoding; the use of standard-normal rather than 
1137:or by training rEFHs with standard-normal emissions; but the 
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000129/versions/0.241017.1444/assets/?page_size=100" | python3 -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000129/versions/0.241017.1444/info/" | python3 -c "import json,sys; d=json.load(sys.stdin); m=d['metadata']; print(m.get('name')); print(m.get('description')); print(json.dumps(m.get('assetsSummary'),indent=1))"; curl -s "https://api.dandiarchive.org/api/dandisets/000129/versions/" | python3 -m json.tool | grep -E '"version"|"name"|"size"'
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; sed -n 240,250p *.txt; sed -n 358,368p *.txt; sed -n 1118,1125p *.txt; sed -n 955,962p *.txt
```

```
mirror reflected visual input from a projector so that visual 
cues appeared in the plane of the reaching hand, while an 
opaque barrier prevented direct vision of the arm. Fingertip 
position was monitored with a six-axis electromagnetic position sensor (Polhemus Liberty, Colchester, VT) at 250 Hz. 
After acquisition, the position data were non-causally lowpass filtered to reject sensor noise (4th order Butterworth; 
Fcutoff = 10 Hz). Velocity and acceleration were then computed by discrete derivative (differences times sampling 
rate). Before applying the decoding algorithms, the kinematic 
state (position, velocity, acceleration) was subsampled, and 
spikes were counted, in non-overlapping 64 ms bins. For 
some experiments (noted below), we applied smaller and 
larger bins.
an LGDS scales quadratically in the number of neurons and 
states, due to the covariance terms. Therefore, to avoid overfitting, we follow Kao and colleagues [15] in requiring the 
state-transition and state-observation noise variables to have 
diagonal covariance matrices. This reduces the number of 
parameters to a linear function of the number of neurons.
EM was initialized with a factor analysis and run until 
convergence (a cross entropy decrease less than 1/100 of a 
percent of the total decrease) or for 100 epochs, whichever 
came first. These parameters were selected to match the 
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import numpy as np, makin as M
rng=np.random.default_rng(0)
# kinematics: circle 1 kHz, radius 50 mm, 0.5 Hz -> speed = 2*pi*0.5*50 = 157 mm/s, acc = (pi)^2*50=493
t=np.arange(0,20,0.001); p=np.c_[50*np.cos(np.pi*t),50*np.sin(np.pi*t)]
k=M.kinematics(p,"methods"); mid=slice(500,4500)
print("speed",np.hypot(k[mid,2],k[mid,3]).mean(),"acc",np.hypot(k[mid,4],k[mid,5]).mean())
# bin alignment
d=dict(finger_pos=p,cursor_pos=p,t0=0.0,spikes=[np.array([0.0,0.063,0.064,0.127])])
R,X,e=M.bin_data(d,64); print(R[:3,0], "X last sample time vs bin end:", X[0,0], 50*np.cos(np.pi*0.060))
# KF vs covariance form
n,N,T=3,10,200
A=0.9*np.eye(n);a=np.zeros(n);Q=np.eye(n)*.1;C=rng.normal(size=(N,n));c=rng.normal(size=N);Rr=np.eye(N)*.5
z=np.zeros(n);Y=[]
for i in range(T): z=A@z+rng.multivariate_normal(a,Q); Y.append(C@z+c+rng.multivariate_normal(np.zeros(N),Rr))
Y=np.array(Y); mu0=np.zeros(n);S0=np.eye(n)
mf=M.kf_pass(A,a,Q,C,c,np.linalg.inv(Rr),mu0,S0,Y)[0]
m,S=mu0,S0;out=[]
for i in range(T):
    if i>0: m=A@m+a;S=A@S@A.T+Q
    K=S@C.T@np.linalg.inv(C@S@C.T+Rr); m=m+K@(Y[i]-C@m-c); S=S-K@C@S; out.append(m)
print("KF max diff",np.abs(mf-np.array(out)).max())
print("rsq perfect", M.rsq(Y,Y)[:2], "snr(0.5)",M.snr(np.array([0.5])))
# unit filter: duplicate detection
Rf=rng.poisson(1,(100,4)).astype(float); Rf[:,3]=Rf[:,1]; print(M.unit_filter(Rf,64,50))
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
cd  ls /usr/bin/python3* ; which -a python python3 uv pip 2>/dev/null; ls ~/.venv* /opt 2>/dev/null | head
```

```
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.14
/usr/bin/python3.14-config
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
/bin/pip
/opt:
actionarchivecache
az
containerd
google
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  uv venv -q $TMPDIR/v && VIRTUAL_ENV=$TMPDIR/v uv pip install -q numpy scipy h5py remfile requests 2>&1 | tail -3; $TMPDIR/v/bin/python -c "import numpy, scipy; print(numpy.__version__)"
```

```
2.5.4
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF'
import numpy as np, makin as M
rng=np.random.default_rng(0)
t=np.arange(0,20,0.001); p=np.c_[50*np.cos(np.pi*t),50*np.sin(np.pi*t)]
k=M.kinematics(p,"methods"); mid=slice(500,4500)
print("speed (expect 157)",np.hypot(k[mid,2],k[mid,3]).mean(),"acc (expect 493)",np.hypot(k[mid,4],k[mid,5]).mean())
d=dict(finger_pos=p,cursor_pos=p,t0=0.0,spikes=[np.array([0.0,0.063,0.064,0.127])])
R,X,e=M.bin_data(d,64); print(R[:3,0], "X[0,0]", X[0,0], "pos at 60 ms", 50*np.cos(np.pi*0.060))
n,N,T=3,10,200
A=0.9*np.eye(n);a=np.zeros(n);Q=np.eye(n)*.1;C=rng.normal(size=(N,n));c=rng.normal(size=N);Rr=np.eye(N)*.5
z=np.zeros(n);Y=[]
for i in range(T): z=A@z+rng.multivariate_normal(a,Q); Y.append(C@z+c+rng.multivariate_normal(np.zeros(N),Rr))
Y=np.array(Y); mu0=np.zeros(n);S0=np.eye(n)
mf=M.kf_pass(A,a,Q,C,c,np.linalg.inv(Rr),mu0,S0,Y)[0]
m,S=mu0,S0;out=[]
for i in range(T):
    if i>0: m=A@m+a;S=A@S@A.T+Q
    K=S@C.T@np.linalg.inv(C@S@C.T+Rr); m=m+K@(Y[i]-C@m-c); S=S-K@C@S; out.append(m)
print("KF max diff",np.abs(mf-np.array(out)).max())
print("snr(0.5)",M.snr(np.array([0.5])))
Rf=rng.poisson(1,(100,4)).astype(float); Rf[:,3]=Rf[:,1]; print("dup filter",M.unit_filter(Rf,64,50))
# EM stopping: how many epochs on this toy
p_,nep,lls=M.lgds_em(Y,3,seed=0); print("EM epochs",nep, "rel last gain", (lls[-1]-lls[-2])/(lls[-1]-lls[0]))
EOF
```

```
speed (expect 157) 157.078599133206 acc (expect 493) 493.4737261311335
[2. 2. 0.] X[0,0] 49.130500659868545 pos at 60 ms 49.114362536434435
KF max diff 3.219646771412954e-14
snr(0.5) [3.01029996]
dup filter [ True  True  True False]
EM epochs 100 rel last gain 4.377986985153663e-06
```

**Agent**

**A. Outcomes** (31 claims in the claims file; the notebooks test 18 and treat 13 as blocked)

| Claim | My outcome | Reason |
|---|---|---|
| units-monkey-i | not_reproduced | 111 units above 0.5 Hz, outside 153.9 to 454.3 (nb1 cell 18). The file has no hash units (ids end in 1 to 4, 82 channels), and its session date, 2017-02-02, is not in the paper's list (cell 5). Adding hash units could reach the range, so this does not contradict the paper. |
| fig2-refh-kf-best | blocked (data_missing) | The bootstrap needs 49 sessions. The mean part is testable on one session and holds: rEFH (+KF) is highest for pos, vel and acc (5.90, 5.16, 2.37; nb1 cell 14). The notebook does not report this. |
| intro-gain-over-nearest | blocked (data_missing) | The p-value needs sessions. The gains are testable on one session but not reported. Reading (b), UKF: 0.27, 1.34 and 1.26 dB, so position and velocity fall outside tolerance. Reading (a): acceleration is 1.03 dB (over WF). Neither reading gets all three gains within tolerance. |
| fig2-velocity-boost | not_reproduced | KFobs ratio is 1.97, below the required 2; UKF ratio 1.55 is inside 1.5 to 2.2 (cell 20). Only the UKF part holds, which the criterion does not count as partial. It is borderline: the rEFH seeds give 1.92 to 1.99, and the code-kinematics variant passes (2.12). |
| fig2-kflatent-dynamic-little-effect | reproduced | Differences of 0.18, 0.21 and 0.09 dB, all under 0.5 (cell 22). Also holds with code kinematics. |
| fig2-refh-static-vel-acc | reproduced | Static rEFH beats the best other decoder by 0.12 dB for vel (UKF) and 0.53 dB for acc (WF). Holds for all seeds and variants (cell 24). One session only, and the velocity margin is small. |
| fig2-position-dynamic-gain | not_reproduced | Gain is 4.41 dB against 3 ± 0.5. Every seed and variant gives 4.38 to 4.45 (cell 26). |
| fig2-sagittal-better | reproduced | y beats x in 24 of 24 pairs; one rEFH seed gives 23 (cell 28). The static rEFH velocity and linear velocity margins are only 0.01 to 0.04 dB. |
| fig2-linear-worst | reproduced | Every decoder is above linear regression for every variable; smallest margin 0.46 dB (cell 30). |
| fig2-gross-failures | reproduced (vacuous) | No negative R2 at 64 ms (cell 32), so the criterion holds trivially. See problem 9. |
| fig4-vel-acc-every-session | partially_reproduced | The per-session part holds: 8 of 8 comparisons favour the rEFH (+KF), smallest margin 1.08 dB across seeds (cell 34). The across-session bootstrap cannot be tested (one session). |
| fig4-advantage-grows | blocked (data_missing) | The regression is over sessions and axes; one session gives two points. Archive confirmed below. |
| fig4-position | blocked (data_missing) | Bootstrap needs sessions. The point differences are testable but not reported: +0.90 dB over KFobs and +0.27 dB over UKF. |
| fig4-best-variable | not_reproduced | Position is the best variable for rEFH (+KF) (5.90 vs 5.16), and this holds for all seeds and the code reading (cell 36). |
| fig4-task-similar | blocked (data_missing) | Monkey C is not on the archive, and there is only one monkey I session. |
| fig5-vel-acc-all-bins | blocked (data_missing) | Bootstrap needs sessions. The point estimates are testable but not reported: at 16 ms the WF beats rEFH (+KF) for vel (3.30 vs 2.96) and acc (1.39 vs 0.95). The direction holds at 32, 64 and 128 ms. |
| fig5-position-bins | blocked (data_missing) | Only the direction can be tested: UKF exceeds rEFH (+KF) at 16 ms (4.68 vs 4.42). The "no difference" parts need the test. |
| fig5-advantage-with-binwidth | reproduced | rEFH (+KF) SNR and its advantage both rise under both readings (nb2 cell 8). |
| fig5-derivative-order | partially_reproduced | Holds at 3 of 4 widths; fails at 16 ms (nb2 cell 10). |
| fig6-training-time | blocked (data_missing) | Part (ii) needs the test. On point values, (i) holds at 80, 160 and 320 s. For (iii), rEFH (+KF) is above KFobs at 320 s (5.90 vs 5.00) and below it at 80 s (2.48 vs 2.73), as the paper says (nb2 cell 6). |
| fig7-vel-acc-neurons | blocked (data_missing) | Bootstrap needs sessions. On point values, velocity at f = 1/4 ties the WF (1.56 vs 1.56). The percent gain in acc over the best rival falls from f = 1/2 (about 95%) to f = 1 (78%). |
| fig7-position-neurons | blocked (data_missing) | Only the direction can be tested: rEFH (+KF) is highest at f = 1/4 and 1/2. |
| fig7-affine-position | not_reproduced | All rho values are within tolerance, but the lowest is WF under reading (a) and static rEFH under (b), never static KFlatent (nb2 cell 14). |
| fig7-kinematic-model-saturates | reproduced | Holds under reading (b) (1/8 to 1/2); fails under (a) (nb2 cell 16). See problem 10. |
| fig8-velocity-variants | not_reproduced | Losses of 0.21 and 0.05 dB against the text's 0.7 and 0.4 (and the figure's about 0.3 and 0.4) (cell 40). The dynamic part holds (0.25 and 0.27 dB). |
| fig8-position-variants | blocked (data_missing) | The dynamic part needs the test. The static part holds on this session (1.49 > 1.43 and 1.41), but the notebook does not mark it. |
| fig8-gaussian-still-beats-ukf | reproduced | Standardized-count variant (paper l. 1122, "standardizing ... separately for each neuron"): +1.07 dB vel and +1.13 dB acc over the UKF (cell 42). The code-transform variant fails (−0.37 vel). |
| fig9-taps | blocked (methods not run) | No tapped decoders are implemented. Parts (i) and (iii) are single-session comparisons that could have been tested; only (ii) needs sessions. |
| kflatent-modest | reproduced | Holds under readings (a) and (b), fails under (c) (cell 38). The KFlatent margin is 0.10 dB from one EM run (problems 1 and 5). With code kinematics only (c) holds. |
| advantage-grows-with-derivative | reproduced | Percent advantage rises pos < vel < acc at 80, 160 and 320 s, under both test-set readings (nb2 cell 12). |
| static-refh-position-worse | blocked (data_missing) | The test needs sessions. The direction holds strongly: static rEFH 1.49 vs UKF 5.63 dB. |

Archive check: I queried the DANDI API for 000129 at version 0.241017.1444. It holds 2 assets and 1 subject: a training file and a test file whose behaviour is withheld. No other sessions, monkey L or monkey C are present, so every claim that needs a bootstrap or regression across sessions is data_missing. Fig9-taps is the exception: it was not run, but its point comparisons are testable.

**B. Problems**

1. [affects a conclusion] `lgds_em` stops when the gain is below `tol*1e-2` with `tol=1e-4`, a threshold of 1e-6. The paper (l. 364) and the docstring say 1/100 of a percent, which is 1e-4. On a synthetic LGDS it ran to the 100-epoch cap with a relative gain of 4.4e-6, where the paper's rule would have stopped earlier. Epoch counts are never printed. This affects KFlatent results, and kflatent-modest rests on a 0.10 dB margin.
2. [affects a conclusion] Blocked claims with parts testable on one session were not evaluated (cell 0 table): fig2-refh-kf-best, intro-gain-over-nearest, fig4-position, fig5-vel-acc-all-bins, fig5-position-bins, fig6-training-time, fig7-vel-acc-neurons, fig7-position-neurons, fig8-position-variants and static-refh-position-worse. This is inconsistent with testing other mean claims on one session. Some of these point estimates go against the paper: the 16 ms WF advantage, intro-gain velocity at 1.34 dB, and the fig7 acc percent falling.
3. [affects a conclusion] fig9-taps: the tapped rEFH and UKF are never implemented in `makin.py`. The stated block reason, "bootstrap", covers only part (ii).
4. [affects a conclusion] Mean-over-49-session claims are graded on one session. The claims header says only per-session statements can be checked on a single session. The notebook labels this a deviation, but outcomes with small margins carry one session's noise: fig2-velocity-boost at 1.97 vs 2, and the kflatent-modest and fig2-refh-static-vel-acc margins. The session is also outside the paper's list and has no hash units (111 units vs 171 to 413), which per figure 7 lowers SNR.
5. [affects a conclusion] Only the rEFH seed is varied (cell 16). The KFlatent EM/FA seed is never varied, so kflatent-modest rests on one EM run at a 0.10 dB margin. The fig8 standard-normal loss of 0.05 dB is within the 0.13 dB rEFH seed spread; this does not change that verdict.
6. [does not affect a conclusion] `dec_ukf` re-implements the UKF; Li's UKF2 package is not used. This is stated as an assumption and looks reasonable, but the UKF is the reference in several claims and was not checked against the original.
7. [does not affect a conclusion] `dec_wf`: at the start of the test set the WF history is zero-padded instead of using the last training bins. At most 6 bins are affected.
8. [does not affect a conclusion] `kinematics`: the 1 kHz series is reduced to 250 Hz with `[::4]` at an arbitrary phase, and forward differences reach about 4 ms past the bin end. Synthetic test: speed and acceleration come out correct (157.08 vs 157, 493.5 vs 493 mm/s and mm/s²). Bin counts and alignment are also correct. The KF information-form update matches a covariance-form KF to 3e-14, and the duplicate-unit filter works.
9. [does not affect a conclusion under the criterion] fig2-gross-failures: outside 64 ms, negative SNR (that is, negative R2) appears for linear regression, static KFlatent and static rEFH at f = 1/8, and for linear regression acc at 80 s (nb2 cell 6). The paper says "in our experiments"; the claims file's restriction to 64 ms may be a narrower reading than the paper's.
10. [does not affect a conclusion] fig7-kinematic-model-saturates passes under reading (b) partly because of KFlatent (+KF)'s failure at f = 1/8 (−2.56 dB). KFobs, UKF and rEFH (+KF) all drop from 1/8 to 1/4.
11. [does not affect a conclusion] fig5-derivative-order: the claims criterion drops the paper's clause "except for the rEFH, which is best at velocity". That clause fails at every width (nb2 cell 10, `refh_kf_best_var` = pos), consistent with fig4-best-variable.

**C. Not checked, and outputs that would settle it**

- The rbmish code details (WF refit on 80%, rEFH learning schedule, the filterDecoder penalty, SLMD) are not in my materials. Line references to the code would let me check them.
- `refh_decode` uses ridge penalty (nv/ns)^(10/3), about 0.005 for about 1000 features on 5000 bins, which is effectively unregularized. The second KF's noise is fitted on in-sample static outputs. This may inflate the dynamic position gain (4.4 vs 3 dB). Printing training-set vs test R2 of the static rEFH map would settle it.
- KFlatent EM epoch counts and log-likelihood traces per configuration.
- Per-decoder R2 tables for the 16 ms, 80 s and fraction configurations, to attribute the negative R2 values.
- KFlatent results under 2 to 3 seeds.
- One-session values for the testable parts of the blocked claims, and an implementation of the tapped decoders.

## End of run

15 turns, 4 minutes, result: success.
