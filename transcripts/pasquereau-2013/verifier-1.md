# 001636 · verifier-1 · run 39687315667

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 624
drwxr-xr-x 6 runner runner    4096 Oct 21 22:40 .
drwxr-xr-x 7 runner runner    4096 Oct 21 22:40 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 21 22:32 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 21 22:32 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 21 22:40 .claude
-rw-r--r-- 1 runner runner       0 Oct 21 22:40 .env
-rw-r--r-- 1 runner runner       0 Oct 21 22:40 .env.development
-rw-r--r-- 1 runner runner       0 Oct 21 22:40 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 21 22:40 .env.local
-rw-r--r-- 1 runner runner       0 Oct 21 22:40 .env.production
-rw-r--r-- 1 runner runner       0 Oct 21 22:40 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 21 22:40 .env.test
-rw-r--r-- 1 runner runner       0 Oct 21 22:40 .env.test.local
drwx------ 2 runner runner      40 Oct 21 22:40 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 21 22:32 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 21 22:32 .github
-rw-r--r-- 1 runner runner       0 Oct 21 22:40 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 21 22:32 .idea
[... 27 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.3389-fnsys.2013.00098.yaml"
}
```

```
1	# Claims for Pasquereau & Turner (2013) on dandiset 001636.
2	# Source: the full text in PubMed Central (PMC3840326, open access, CC BY), read from its Methods,
3	# Results, Table 1 and figure legends, and its supplementary data sheet (DataSheet1.PDF), whose
4	# table gives the neuronal results for each monkey separately.
5	# Quotes and statistics added 2026-10-19 from the full text (Europe PMC PMC3840326).
6	#
7	# When these criteria were written, the author had seen the data check only: the file list and
8	# metadata, the contents of the files, the counts of units by subject, MPTP state and projection
9	# type, the number of torque perturbations per direction (none in any monkey L file), the timing
10	# of the torque command against the trials table, the sign of the joint angle, which EMG channels
11	# hold data, and the cross-referenced and repeated files. These counts showed that the monkey V
12	# units with at least 5 perturbations per direction number 112 before and 159 after MPTP, with
13	# 49 and 54 PTNs and 31 and 48 CSNs, as in the supplementary table. No SDF, response detection,
14	# kinematic measure or EMG response had been computed.
15	#
16	# The dandiset marks no torque perturbation in any monkey L file, so every claim is tested on
17	# monkey V (elbow), and the expected values are the paper's monkey V values where it gives them
18	# (supplementary table). Where the paper gives only values pooled over both monkeys, these are
19	# the expected values and the difference is a deviation.
20	#
[... 760 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "stretch.py"
}
```

```
1	"""Loading and measures for the torque perturbation (muscle stretch) trials of dandiset 001636.
2	
3	Pasquereau & Turner (2013), Frontiers in Systems Neuroscience 7:98, doi:10.3389/fnsys.2013.00098.
4	
5	Each NWB file holds one recording session of one or more single units in M1 of monkey Venus (V,
6	elbow task) or Leu (L, wrist task): a trials table with the task events and the torque
7	perturbations, the manipulandum angle, the torque command and, in many Venus sessions, rectified
8	EMG. Files are streamed from the archive at the pinned version; nothing is written to disk.
9	
10	Sessions. In the draft of 2026-10-21, source files recorded on the same day and linked in the
11	lab's metadata table are merged into one session, and a unit is observed only during the trials
12	of its own source files (its obs_intervals). A unit's perturbations are therefore the perturbation
13	trials inside its obs_intervals (`load_session` stores them per unit).
14	
15	Clocks. The source files were trialized; the conversion placed the trials one after another with
16	3 s gaps. In version 0.260518.1819 the analog streams (angle, torque, EMG) were laid end to end by
17	their own sample counts and fell further behind the trials table with every trial. `realign` puts
18	each analog segment back at the start time of its trial; in the draft it moves nothing, which the
19	notebook shows (the lag it would correct is printed in the data check).
20	
[... 499 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_pasquereau_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
2276 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 800
}
```

```
1	==================== 0 markdown
2	# Reproducing Pasquereau & Turner (2013) from dandiset 001636
3	
4	Paper: Pasquereau B, Turner RS (2013). Primary motor cortex of the parkinsonian monkey: altered
5	neuronal responses to muscle stretch. *Frontiers in Systems Neuroscience* 7:98.
6	[doi:10.3389/fnsys.2013.00098](https://doi.org/10.3389/fnsys.2013.00098). The claims file was
7	written from the full text (open access, PubMed Central PMC3840326) and its supplementary data
8	sheet, whose table gives the neuronal results of each monkey separately.
9	
10	Dandiset: [DANDI:001636](https://dandiarchive.org/dandiset/001636/draft), version draft, as asked
11	for this attempt. The draft was last modified on 2026-10-21 at 20:16:41 UTC (the first cell prints
12	the modification time read at run time); a draft can change, and when it was read the archive
13	listed 4 uploads in progress. This is a repeat attempt: the earlier one,
14	`001636-pasquereau-2013-01`, used the published version 0.260518.1819. Since then the files were
15	reconverted to fix what that attempt found, and the fixes are not yet published, so the draft is
16	tested here. The paper (2013) cites no DANDI version.
17	
18	How the draft differs from 0.260518.1819, in what the analysis uses (shown in the data check): it
19	holds 439 files where the published version held 447. Source files recorded on the same day and
20	linked through a neuron recorded across them are merged into one session, and a unit is observed
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
800	    sign = np.where(s["pert_direction"] == "flexion", 1.0, -1.0)[:, None]
801	    rel = (w - np.nanmedian(w[:, (AX >= -100) & (AX < 0)], axis=1, keepdims=True)) * sign
802	    m = np.nanmean(rel, axis=0)
803	    command.append({"session": s["session_id"], "code": s["session_id"].split("++")[1], "post": s["post"],
804	                    "date": s["date"], "step": float(np.nanmedian(rel[:, (AX >= 10) & (AX < 40)])),
805	                    "width_ms": int((m > m.max() / 2).sum()), "after_pulse": float(m[(AX >= 70) & (AX < 150)].mean())})
806	command = pd.DataFrame(command)
807	command["level"] = np.round(command.step / command.step[command.step > 10].min()).astype(int)
808	print("\nTorque command step (units above the pre-onset level) by state; level = step in multiples of the smallest:")
809	print(pd.crosstab(command.level, command.post).to_string())
810	print(command.groupby(["post", "level"])[["step", "width_ms", "after_pulse"]].median().round(1).to_string())
811	# per-trial step, against the level of its session
812	trial_steps = []
813	for s, lv in zip(venus, command.level):
814	    w = s["windows"]["torque_cmd"]
815	    sign = np.where(s["pert_direction"] == "flexion", 1.0, -1.0)
816	    rel = (w - np.nanmedian(w[:, (AX >= -100) & (AX < 0)], axis=1, keepdims=True)) * sign[:, None]
817	    step = np.nanmedian(rel[:, (AX >= 10) & (AX < 40)], axis=1)
818	    trial_steps.append(pd.DataFrame({"post": s["post"], "session_level": lv,
819	                                     "trial_level": np.round(step / command.step[command.step > 10].min())}))
[... 730 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1550,
 "limit": 730
}
```

```
1550	                         "in_tol": abs(v - e) <= 0.1 * e, "n": int((x.state == st).sum())})
1551	mags = pd.DataFrame(rows)
1552	print(mags.round(2).to_string(index=False))
1553	print("\nWithin tolerance per reading (of 8):", mags.groupby("reading").in_tol.sum().to_dict())
1554	--OUT--
1555	      reading group direction state  value  expected  in_tol  n
1556	 a max change    M1   flexion   pre  40.21      42.4    True 49
1557	 a max change    M1   flexion  post  31.22      37.9   False 63
1558	 a max change    M1 extension   pre  47.65      50.9    True 40
1559	 a max change    M1 extension  post  33.20      42.6   False 52
1560	 a max change   PTN   flexion   pre  31.74      33.4    True 27
1561	 a max change   PTN   flexion  post  19.95      26.1   False 33
1562	 a max change   PTN extension   pre  36.22      38.8    True 23
1563	 a max change   PTN extension  post  23.79      29.3   False 26
1564	  b mean rate    M1   flexion   pre  37.24      42.4   False 49
1565	  b mean rate    M1   flexion  post  28.45      37.9   False 63
1566	  b mean rate    M1 extension   pre  37.40      50.9   False 40
1567	  b mean rate    M1 extension  post  28.06      42.6   False 52
1568	  b mean rate   PTN   flexion   pre  33.99      33.4    True 27
1569	  b mean rate   PTN   flexion  post  21.75      26.1   False 33
[... 708 more lines not kept]
```

**Agent**

Every claim downstream of the false-positive check needs the response selection, and the notebook runs them as tested. Next: synthetic tests of the helper and a check of the archive.

**Agent calls Bash**

```bash
cd  timeout 600 python3 -c "
import numpy as np, stretch
from scipy import stats
rng=np.random.default_rng(0)
# kernel / sdf sanity
x=stretch.sdfs([np.array([0.])])[0]
print('sdf of one spike at 0: sum',x.sum()/1000,'peak at',stretch.GRID[np.argmax(x)],'nonzero before 0',(x[stretch.GRID<0]>0).sum())
# constant rate 20 Hz -> sdf mean ~20
tr=[np.sort(rng.choice(np.arange(-1800,700),50,replace=False)).astype(float) for _ in range(10)]
X=stretch.sdfs(tr); print('mean sdf ~', X[:,stretch._mask(-500,0)].mean(), 'expected', 50/2.5)
# false positive rate of main detection, Poisson null
for rate in (2,10,30):
  hits=[];resp=[]
  for k in range(400):
    trains=[np.flatnonzero(rng.random(2500)<rate/1000)-1800. for _ in range(10)]
    d=stretch.detect(stretch.sdfs(trains)); hits.append(d['any_crossing_0_200']); resp.append(d['responds'])
  print('rate',rate,'FP any crossing',np.mean(hits),'resp 20-60',np.mean(resp))
# injected response at 30-80ms, +40 sp/s
trains=[np.r_[np.flatnonzero(rng.random(2500)<10/1000)-1800., 30+np.flatnonzero(rng.random(50)<40/1000)] for _ in range(10)]
trains=[np.sort(t) for t in trains]
d=stretch.detect(stretch.sdfs(trains)); print({k:d[k] for k in ('responds','sign','latency','offset','fwhm','max_change') if k in d})
# pseudo shift indexing
d=stretch.detect(stretch.sdfs(trains),shift_ms=-600); print('pseudo',d['responds'],d['any_crossing_0_200'])
# dsi
print(stretch.dsi({'max_change_signed':10,'responds':True,'sign':1},{'max_change_signed':-5,'responds':True,'sign':-1}))
print(stretch.dsi({'max_change_signed':10,'responds':True,'sign':1},{'max_change_signed':8,'responds':True,'sign':1}))
# emg
ax=np.arange(-500,501); tr=np.zeros((5,len(ax)))+rng.normal(0,1,(5,len(ax))); tr[:,(ax>=45)&(ax<100)]+=20
r=stretch.emg_response(tr,1); print('emg onset',r['onset_ms'],'dur',r['duration_ms'],'m1',round(r['m1'],2),'m2',round(r['m2'],2))
# kinematics: step displacement starting at 20ms
ang=np.where(ax>=20, np.minimum((ax-20)*0.1,5),0.)
print(stretch.kinematics(ang,'flexion',1))
# chi2 checks from claims
for t in ([[89,131-89],[35,114-35]],):
  print('chi2 yates PTN vs CSN paper counts', stats.chi2_contingency(np.array(t),correction=True)[:2])
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, stretch
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls node_modules; which -a python3 python; ls ~/.venv* /opt 2>/dev/null | head; pip --version 2>&1; uv --version 2>&1
```

```
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python
/opt/hostedtoolcache/Python/3.13.16/x64/python
/usr/bin/python
/bin/python
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
pip 26.2.1 from /opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/pip (python 3.13)
uv 0.13.4 (x86_64-unknown-linux-gnu)
```

**Agent calls Bash**

```bash
/usr/bin/python3 -c "import numpy, scipy, pandas; print('ok')" 2>&1; cd $TMPDIR && uv venv -q v 2>&1 | tail -2 && uv pip install -q -p v numpy scipy pandas h5py remfile dandi 2>&1 | tail -3; ls v/bin | head
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy, scipy, pandas; print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'numpy'
activate
activate.bat
activate.csh
activate.fish
activate.nu
activate.ps1
activate.xsh
activate_this.py
bids-validator-deno
bst
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  timeout 900 $TMPDIR/v/bin/python -c "
import numpy as np, stretch
from scipy import stats
rng=np.random.default_rng(0)
x=stretch.sdfs([np.array([0.])])[0]
print('sdf one spike: integral',x.sum()/1000,'peak at',stretch.GRID[np.argmax(x)],'nonzero before 0',(x[stretch.GRID<0]>0).sum())
tr=[np.sort(rng.choice(np.arange(-1800,700),50,replace=False)).astype(float) for _ in range(10)]
X=stretch.sdfs(tr); print('mean sdf', X[:,stretch._mask(-500,0)].mean(), 'expected', 50/2.5)
for rate in (2,10,30):
  hits=[];resp=[]
  for k in range(400):
    trains=[np.flatnonzero(rng.random(2500)<rate/1000)-1800. for _ in range(10)]
    d=stretch.detect(stretch.sdfs(trains)); hits.append(d['any_crossing_0_200']); resp.append(d['responds'])
  print('Poisson rate',rate,'FP any crossing',np.mean(hits),'resp 20-60',np.mean(resp))
trains=[np.sort(np.r_[np.flatnonzero(rng.random(2500)<10/1000)-1800., 30+np.flatnonzero(rng.random(50)<40/1000)]) for _ in range(10)]
d=stretch.detect(stretch.sdfs(trains)); print({k:d[k] for k in ('responds','sign','latency','offset','fwhm','max_change') if k in d})
d=stretch.detect(stretch.sdfs(trains),shift_ms=-600); print('pseudo',d['responds'],d['any_crossing_0_200'])
print(stretch.dsi({'max_change_signed':10,'responds':True,'sign':1},{'max_change_signed':-5,'responds':True,'sign':-1}))
print(stretch.dsi({'max_change_signed':10,'responds':True,'sign':1},{'max_change_signed':8,'responds':True,'sign':1}))
ax=np.arange(-500,501); tr=rng.normal(0,1,(5,len(ax))); tr[:,(ax>=45)&(ax<100)]+=20
r=stretch.emg_response(tr,1); print('emg onset',r['onset_ms'],'dur',r['duration_ms'],'m1',round(r['m1'],2),'m2',round(r['m2'],2))
ang=np.where(ax>=20, np.minimum((ax-20)*0.1,5),0.)
print(stretch.kinematics(ang,'flexion',1))
print('chi2 yates paper PTN vs CSN', stats.chi2_contingency(np.array([[89,42],[35,79]]),correction=True)[:2])
"
```

```
sdf one spike: integral 1.0 peak at 10 nonzero before 0 0
mean sdf 20.25031342777385 expected 20.0
Poisson rate 2 FP any crossing 0.2175 resp 20-60 0.065
Poisson rate 10 FP any crossing 0.15 resp 20-60 0.04
Poisson rate 30 FP any crossing 0.1775 resp 20-60 0.04
{'responds': True, 'sign': 1.0, 'latency': 40, 'offset': 106, 'fwhm': 60.0, 'max_change': 31.92048310101201}
pseudo False False
(1.5, 'reciprocal')
(0.19999999999999996, 'non-directional')
emg onset 45.0 dur 55.0 m1 -0.09 m2 18.02
{'valid': True, 'moving_before': True, 'latency_ms': 8.0, 'latency_causal_ms': 21.0, 'peak_velocity': 110.89713216440589, 'amplitude': 5.079627429394834}
chi2 yates paper PTN vs CSN (np.float64(32.3400842996932), np.float64(1.294159182258593e-08))
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "hamming|low-pass|lowpass|5 deg|single.trial|trial-by-trial|trial by trial|0\.1.?N|onset latenc|latencies of torque-induced|independent comparisons|gamma" 10.3389-fnsys.2013.00098.txt | cut -c1-400
```

```
7:642 frontsysneuro Frontiers in Systems Neuroscience Front Syst Neurosci Frontiers Media SA PMC3840326 3840326 3840326 24324412 10.3389/fnsys.2013.00098 Primary motor cortex of the parkinsonian monkey: altered neuronal responses to muscle stretch Pasquereau Benjamin 1 Turner Robert S 1 * 1 Department of Neurobiology, Center for Neuroscience and The Center for the Neural Basis of Cognition, Univer
48:10.1038/nn.3047 Hamming R. W. (1983). Digital Filters. Englewood Cliffs NJ: Prentice Hall Hammond P. H. (1955). Involuntary activity in biceps following the sudden application of velocity to the abducted forearm.
243:title=Digital Filters&author=R. W. Hamming&publication_year=1983&
```

**Agent calls Bash**

```bash
cd paper; wc -c 10.3389-fnsys.2013.00098.txt; grep -o -i -E ".{300}(Hamming|single trial|trial-by-trial|trial by trial|0\.1 Nm|0.1-Nm|independent comparisons|latencies of torque-induced).{300}" 10.3389-fnsys.2013.00098.txt | head -20
```

```
120971 10.3389-fnsys.2013.00098.txt
. The target then shifted to the left or right (chosen at random), and the animal moved the cursor to capture the lateral target. The animal received a drop of juice for successful completion of the task. On two-thirds of the trials (selected at random), single flexing or extending torque impulses (0.1 Nm–50 ms duration) were applied to the manipulandum by a DC brushless torque motor (TQ40W, Aerotech Inc., Pittsburgh PA) at an unpredictable time beginning 1–2 s (uniform randomized distribution) after initial capture of the center target. Each square-wave torque impulse induced an angular displacemen
ivity evoked by torque perturbation during the start-position hold period. The general features of task performance before and after MPTP have been reported previously (Pasquereau and Turner, 2011 ). The digitized signal reflecting manipulandum angle was filtered and differentiated [low-pass 25-Hz (Hamming, 1983 )]. The onset of torque-evoked movement, peak velocity, and movement termination were detected automatically using angle, velocity, and duration criteria. A velocity threshold of 5-deg/s was used to detect movement. Session-by-session means of kinematic measures were entered into Three-Way AN
 detected by comparing SDF values (millisecond-by-millisecond) during a post-torque epoch (200-ms) relative to a cell's baseline firing rate (2-tailed t -test). The threshold for significance was adjusted to account for multiple comparisons [ p < 0.01/(200-ms epoch/40-ms gamma filter half-width = 5 independent comparisons) = 0.002]. A neuron was judged to be torque-related if it generated a significant post-torque response for at least one movement direction. Response onset times, defined as the time at which the SDF first crossed the p = 0.002 threshold, were determined separately for each torque direction. For com
( F > 49, p < 0.01). More specifically, the mean peak velocity and the amplitude of torque-induced displacements averaged acr
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/001636/versions/draft/info/" | $TMPDIR/v/bin/python -c "
import json,sys; d=json.load(sys.stdin); m=d['metadata']
print(d.get('modified'), d.get('asset_count'), d.get('status'))
print(m.get('description','')[:6000])
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/v/bin/python -c "
import requests,collections
url='https://api.dandiarchive.org/api/dandisets/001636/versions/draft/assets/?page_size=1000'
paths=[]
while url:
    r=requests.get(url).json(); paths+= [a['path'] for a in r['results']]; url=r['next']
c=collections.Counter((p.split('/')[0], 'Post' if 'PostMPTP' in p else 'Pre') for p in paths)
print(len(paths),c)
print([p for p in paths if not p.endswith('.nwb')][:5])
" 2>&1 | tail -5
```

```
439 Counter({('sub-Venus', 'Pre'): 154, ('sub-Venus', 'Post'): 137, ('sub-Leu', 'Pre'): 98, ('sub-Leu', 'Post'): 50})
[]
Shell cwd was reset to
```

**Agent**

**A. Outcomes** (the claims file holds 28 claims)

| Claim | Outcome | Reason |
|---|---|---|
| cell-counts | reproduced | Cell 24: 115/157 cells, 51/54 PTNs, 32/48 CSNs, 3 dual, all within tolerance. Counting each merged unit from its first file only gives 112, 49 and 31 before MPTP. |
| monkey-l-perturbations | blocked (data_missing) | Every Leu trial is labelled `not_available` (cell 3). One hold-window command excursion appears in 2048 Leu trials (cell 9). The archive's draft description says "The Leu files contain no perturbation times". Only Leu unit counts could be tested (138/72 against 115/73), and they are not the claim. |
| baseline-rate | reproduced | Cell 27: all six means within tolerance. PTN Mann-Whitney p = 0.020 (< 0.05); CSN p = 0.65. The M1 test is reported (p = 0.0022). |
| ptn-faster-than-csn | reproduced | Cell 29: 18.5 against 3.5 spikes/s, p = 6e-12. |
| antidromic-latency | partially_reproduced | Cell 31: all four means are within tolerance and the PTN p is 0.68. The CSN p is 0.0190, above the criterion's 0.05/3 = 0.0167, so the CSN test fails. |
| false-positive-rate | not_reproduced | Cell 33: 0.228 of cell-directions cross the threshold at the pseudo onset (t-test variant 0.463). The criterion range is 0.0033 to 0.03. Unperturbed trials (0.19, cell 34) and Poisson simulations (0.17–0.21, cell 35; 0.15–0.22 in my own test) agree, so the procedure itself is at fault. |
| torque-related-fractions | blocked (methods_underspecified) | The claims file says these claims are blocked when the false-positive rate is above 0.03. For reference: 1 of 6 percentages within tolerance (cell 38). |
| prevalence-unchanged | blocked (methods_underspecified) | Same rule. For reference: none of the three p values is below 0.0167 (cell 40). |
| ptn-more-responsive | blocked (methods_underspecified) | Same rule. For reference: 70.5% against 16.2%, p = 7e-13; the CSN fraction is out of tolerance (cell 42). |
| one-direction-half | blocked (methods_underspecified) | Same rule. For reference: 52.2% against 44 ± 4.4 (cell 44). |
| excitatory-majority | blocked (methods_underspecified) | Same rule. For reference: 2 of 4 percentages within tolerance; PTN p = 0.34 (cell 46). |
| magnitude-unchanged | blocked (methods_underspecified) | Same rule. For reference: 12 of 12 tests have p < 0.05, with magnitudes smaller after MPTP (cell 48). |
| venus-response-magnitudes | blocked (methods_underspecified) | Same rule. For reference: at most 4 of 8 values within tolerance under any reading (cell 49). |
| latency-shorter | blocked (methods_underspecified) | Same rule. For reference: all 4 KS p < 0.013 and 8 of 8 means within tolerance (cell 51). The t-test variant finds no shortening (KS p 0.17–0.73). |
| latency-not-training | blocked (methods_underspecified) | Same rule. For reference: rho = −0.249, p = 0.0033 (cell 53). |
| fwhm-shorter-ptn | blocked (methods_underspecified) | Same rule. For reference: flexion p = 0.027, extension p = 0.37; 2 of 4 means within tolerance (cell 55). |
| dsi-reduced | blocked (methods_underspecified) | Same rule. For reference: −6.7 points, p = 0.127 (cell 57). |
| venus-dsi | blocked (methods_underspecified) | Same rule. For reference: 3 of 6 within tolerance (cell 58). |
| dsi-not-baseline | blocked (methods_underspecified) | Same rule. For reference: F = 0.40, p = 0.75 (cell 59). |
| kinematics-slower | not_reproduced | Cell 63: peak velocity rises 28% and amplitude 15% after MPTP, under both readings. |
| kinematic-latency-unchanged | not_reproduced | Cell 65: MPTP F = 1037, p ≈ 0 (latencies about 10 ms before MPTP, 3–6 ms after). |
| emg-m2-larger | reproduced | Cell 69: median m2 is higher after MPTP in all three triceps channels, KS p ≤ 5e-15. The torque-size confound in problem 3 still applies. |
| emg-duration-longer | partially_reproduced | Cell 71: 24.6 → 49.4 ms, KS p = 4e-36. Both means are outside 57 ± 6 and 79 ± 3. |
| emg-onset-unchanged | not_reproduced | Cell 71: onset 40.3 → 24.0 ms, KS p = 9e-21. |
| emg-m1-weak | partially_reproduced | Cell 73: after MPTP, m2 > m1 in 96.5% with median m1/m2 0.23. Before MPTP the share is 74.4%, just under the 75% the criterion asks for (median 0.10). |
| velocity-matched-magnitude | blocked (methods_underspecified) | Same rule. It would be untestable anyway: session mean peak velocities top out at 145 deg/s, leaving 0 pre and 1 post responses in 130–200 deg/s (cell 75). |
| session-correlations | blocked (methods_underspecified) | Same rule. For reference: p = 0.19 and 0.023, both above 0.0125 (cell 77). |
| trial-correlations | blocked (methods_underspecified) | The paper gives no single-trial latency; I checked the Methods text. |

Totals: 4 reproduced, 3 partially reproduced, 4 not reproduced, 17 blocked.

**B. Problems**

1. **[affects a conclusion]** Cells 0, 33, 37–59, 75 and 77: the claims file says response-dependent claims are blocked when the pseudo-onset rate is outside 0.0033–0.03. Cell 33 gives 0.228, yet the notebook still treats all 15 dependent claims as tested ("yes" in the cell 0 table). The t-test variant (0.463) does not rescue them.
2. **[affects a conclusion]** Cell 31: the CSN antidromic p (0.0190) is printed with no comparison against 0.05/3. It fails that threshold, which makes the claim partial rather than reproduced.
3. **[affects a conclusion: what the outcomes mean, not the criterion results]** Cell 19 and the kinematics/EMG cells: the torque command differs by state.
   - Before MPTP, 105 of 154 sessions use the smallest pulse (~46 units). After MPTP, 125 of 137 use the largest (~183 units), followed by an opposite swing.
   - This explains faster, larger displacements after MPTP and confounds the m2, EMG duration and EMG onset comparisons.
   - In the middle-size variant (43 pre, 12 post sessions) the m2 rise does not hold (longus 1: 47.6 → 1.3) and duration does not change (p = 0.94). The emg-m2-larger result is therefore not evidence of an MPTP effect.
4. **[affects a conclusion]** `stretch.kinematics`: a 101-tap FIR applied forwards and backwards smears motion about 50 ms backwards in time. In my synthetic test, a ramp starting at 20 ms is detected at 8 ms and flagged as `moving_before`. The data show 241 latencies of 0 ms and 503 trials moving before onset, so latencies are biased early and depend on the pulse shape. The forwards-backwards filter is the claims file's choice; the paper says only "low-pass 25-Hz". The causal variant is also significant (F = 791), so the outcome stands.
5. **[does not affect a conclusion]** Cells 71 and 73: the pre-MPTP "EMG responses" are mostly noise crossings (median duration 9 ms, 63% ≤ 10 ms, median m2 3–5 A/D units). The onset and duration comparisons therefore set noise against real responses. Median m1/m2 also includes channel-sessions with negative m2.
6. **[does not affect a conclusion]** `stretch.dsi` builds P and NP from the largest change over 0–200 ms, whether or not that falls in the response window. The claims file does not set this, so it is the author's choice.
7. **[does not affect a conclusion]** Cell 57: the 2×4 chi-square has a smallest expected count of 1.8. Cell 71's threshold variant drops responses that last to the end of the window.
8. **[does not affect a conclusion; claims-file reading]** The paper's Methods say SDF values were compared "relative to a cell's baseline firing rate (2-tailed t-test)". That reads closer to the t-test variant than to the claims file's main rule (mean ± t·SD, taken from Figure 3). Both give a false-positive rate far above 0.03, so the block holds either way.
9. **[does not affect a conclusion]** Cells 3 and 24: the draft's merged sessions change the counts slightly from the supplementary table (115 against 112 cells, 51 against 49 PTNs, 32 against 31 CSNs). This is explained in cell 6 and stays within tolerance.

**C. What I could not check**

- **Spike window against trial boundaries.** I could not tell whether the −1.8 s spike window, and the −1100 to −600 ms pseudo baseline, fall inside each trial. Spikes exist only inside trials, and trials are separated by gaps, so part of the window could be empty by construction. A printed distribution of (onset − trial start) would settle it. The unperturbed-trial null and the Poisson simulation make this unlikely to change the false-positive conclusion.
- **Per-cell results.** No per-cell table (baseline rate, threshold, latency, sign) is saved, so I could not recompute any group statistic independently.
- **Supplementary table values.** I did not check the claims file's expected values against the supplementary PDF table. Where I checked the main text against the claims file (the 0.002 threshold, the 25 Hz Hamming filter, the |rho| values, the Yates chi-square of 32.3 from 89/131 and 35/114), they match.
- **Command size by state.** Per-trial command step size against kinematics within each state, binned by level, is printed only in aggregate. Pre/post comparisons at matched trial-level step size would show whether any MPTP effect survives the torque confound.
- **Monkey L files.** I checked the archive's description and asset list but did not open any Leu file. Leu blocking rests on the notebook's file scan and the archive's own description.

## End of run

16 turns, 3 minutes, result: success.
