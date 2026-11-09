# crcns-fcx-3 · verifier-1 · run 42527046925

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 632
drwxr-xr-x 6 runner runner    4096 Nov  8 22:15 .
drwxr-xr-x 7 runner runner    4096 Nov  8 22:15 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  8 21:48 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  8 21:48 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  8 22:15 .claude
-rw-r--r-- 1 runner runner       0 Nov  8 22:15 .env
-rw-r--r-- 1 runner runner       0 Nov  8 22:15 .env.development
-rw-r--r-- 1 runner runner       0 Nov  8 22:15 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  8 22:15 .env.local
-rw-r--r-- 1 runner runner       0 Nov  8 22:15 .env.production
-rw-r--r-- 1 runner runner       0 Nov  8 22:15 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  8 22:15 .env.test
-rw-r--r-- 1 runner runner       0 Nov  8 22:15 .env.test.local
drwx------ 2 runner runner    4096 Nov  8 22:15 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  8 21:48 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  8 21:48 .github
-rw-r--r-- 1 runner runner       0 Nov  8 22:15 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  8 21:48 .idea
[... 24 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.3389-fnsys.2018.00065.yaml"
}
```

```
1	# Claims for Johnson, King-Stephens, Weber, Laxer, Lin & Knight (2019), Front. Syst. Neurosci. 12,
2	# 65, "Spectral Imprints of Working Memory for Everyday Associations in the Frontoparietal Network",
3	# doi:10.3389/fnsys.2018.00065, on CRCNS data set fcx-3 (doi:10.6080/K06971S9).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-13.
6	#
7	# Text read: the version of record, PMC6333050 (open access), full text from Europe PMC JATS XML as
8	# supplied under paper/: Introduction, Materials and Methods, Results, Discussion, Table 1 and the
9	# legends of Figures 1 to 5. The paper has no supplement. No PDF was supplied, so values shown only
10	# inside figures (per-subject accuracy and RT of Fig. 1B, per-subject PSI of Fig. 4A and 4C, the
11	# time courses of Fig. 5) were not read; claims on those figures rest on the Results and legends.
12	# The CRCNS data descriptor was read only to know which experiments the data set holds; no claim or
13	# method comes from it.
14	#
15	# Code. The paper's Data Availability says its custom MATLAB code is deposited at CRCNS with the
16	# data. By the data descriptor it is the analysis_scripts directory of data set fcx-3 itself. It is
17	# one of the data set's files, which this reader does not open, so it was not read and no commit is
18	# recorded. Every method below is from the paper's text. Where the scripts settle a detail named as
19	# open below, the author may follow them (protocol, Reader step 2) and should say so.
20	#
[... 592 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('reproduce_johnson_2019.ipynb'))
print(len(nb['cells']))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"=== [{i}] {c['cell_type']} ===")
    print(src)
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if 'text' in o: t=''.join(o['text'])
            elif 'data' in o: t=''.join(o['data'].get('text/plain',''))+(' [IMAGE]' if 'image/png' in o['data'] else '')
            elif o.get('output_type')=='error': t='ERROR '+o['ename']+o['evalue']
            else: t=''
            print('--- out ---'); print(t[:6000])
EOF
```

```
<persisted-output>
Output too large (105.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/488f881d-d550-40bd-858a-ea297ffaf32c/tool-results/btwf1uhlk.txt

Preview (first 2KB):
44
=== [0] markdown ===
# Reproducing Johnson et al. (2019) from CRCNS data set fcx-3

**Paper.** Johnson EL, King-Stephens D, Weber PB, Laxer KD, Lin JJ, Knight RT (2019). Spectral
imprints of working memory for everyday associations in the frontoparietal network. *Frontiers in
Systems Neuroscience* 12, 65. [doi:10.3389/fnsys.2018.00065](https://doi.org/10.3389/fnsys.2018.00065).
The claims file was written from the version of record (PMC6333050, open access); the paper has no
supplement.

**Data set.** CRCNS fcx-3, [doi:10.6080/K06971S9](https://doi.org/10.6080/K06971S9), read from the
public bucket `crcnsarchive` under `fcx-3/live/`. CRCNS data sets are not versioned, so the version
is recorded as `unversioned` (docs/archives.md). The paper cites no version; `live/` is the only
copy the bucket holds (there is no `old/`), with its files dated 2026-02-11 and the data
description version 0.5 of 2019-01-04, the original version. The MD5 sums of the files read, from
the data set's `checksums.md5`, are printed below, so that a later change is detectable.
[... 17 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/488f881d-d550-40bd-858a-ea297ffaf32c/tool-results/btwf1uhlk.txt"
}
```

```
1	44
2	=== [0] markdown ===
3	# Reproducing Johnson et al. (2019) from CRCNS data set fcx-3
4	
5	**Paper.** Johnson EL, King-Stephens D, Weber PB, Laxer KD, Lin JJ, Knight RT (2019). Spectral
6	imprints of working memory for everyday associations in the frontoparietal network. *Frontiers in
7	Systems Neuroscience* 12, 65. [doi:10.3389/fnsys.2018.00065](https://doi.org/10.3389/fnsys.2018.00065).
8	The claims file was written from the version of record (PMC6333050, open access); the paper has no
9	supplement.
10	
11	**Data set.** CRCNS fcx-3, [doi:10.6080/K06971S9](https://doi.org/10.6080/K06971S9), read from the
12	public bucket `crcnsarchive` under `fcx-3/live/`. CRCNS data sets are not versioned, so the version
13	is recorded as `unversioned` (docs/archives.md). The paper cites no version; `live/` is the only
14	copy the bucket holds (there is no `old/`), with its files dated 2026-02-11 and the data
15	description version 0.5 of 2019-01-04, the original version. The MD5 sums of the files read, from
16	the data set's `checksums.md5`, are printed below, so that a later change is detectable.
17	
18	**What the data set holds.** For each of the 7 subjects: the filtered continuous iEEG
19	(`data_primary.mat`), channel names, electrode positions, the preprocessed epochs
20	(`data_derived.mat`: pretrial, encoding and maintenance, and processing epochs of every channel
[... 591 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "fcx3.py"
}
```

```
1	"""Loading and measures for CRCNS data set fcx-3 (Johnson et al. 2019, Front. Syst. Neurosci. 12, 65,
2	doi:10.3389/fnsys.2018.00065).
3	
4	The data set (doi:10.6080/K06971S9) holds, per subject, a tar.gz with the filtered continuous iEEG
5	(data_primary.mat), the channel names (elec_labels.mat), electrode positions (s<n>_MNI_grid.csv),
6	the preprocessed epochs (data_derived.mat, FieldTrip structures data_pre, data_encmain and
7	data_proc, MATLAB 7.3) and a trial table (summary_file_trial.csv). The tar files are streamed from
8	the public bucket and decompressed in memory, one subject at a time; nothing is written to disk.
9	A tar.gz cannot be read at random, so each subject's file is read once, start to end.
10	
11	Where the parameters come from:
12	
13	- Channels analysed, by region and hemisphere: docs/summary_channel_analysis.csv of the data set.
14	  The derived epochs carry more channels; only the listed ones are kept.
15	- Analysis windows, in the time axis of the derived epochs: processing [0.3, 1.2] s of data_proc,
16	  maintenance [0.6, 1.5] s of data_encmain, baseline [0.65, 0.85] s of data_pre. These are the
17	  latencies of the paper's deposited scripts (power_compute.m, erp_compute.m, psi_compute.m); the
18	  notebook checks them against the trial table and the continuous data.
19	- Power: Hanning-tapered windows of 3 cycles (3/f s), 2 to 40 Hz in 1-Hz steps, 10-ms steps
20	  (Methods, Spectral Decomposition; power_compute.m). The derived epochs run from -1.5 to 3.0 s,
[... 835 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/488f881d-d550-40bd-858a-ea297ffaf32c/tool-results/btwf1uhlk.txt",
 "offset": 611,
 "limit": 760
}
```

```
File content (27278 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/488f881d-d550-40bd-858a-ea297ffaf32c/tool-results/btwf1uhlk.txt",
 "offset": 611,
 "limit": 400
}
```

```
611	s2      spatial      0.368     0.461  0.344
612	        temporal     0.053     0.093  0.033
613	s3      spatial      0.839     0.680  0.847
614	        temporal     0.273     0.466  0.254
615	s4      spatial      0.220     0.236  0.135
616	        temporal     0.218     0.232  0.134
617	s5      spatial      0.247     0.028  0.267
618	        temporal     0.100     0.214  0.076
619	s6      spatial      0.341     0.303  0.198
620	        temporal     0.198     0.227  0.098
621	s7      spatial      0.192     0.196  0.106
622	        temporal     0.125     0.125  0.053
623	adjacent: subject-contrasts with a cluster p < 0.05: 0, < 0.025: 0; smallest p 0.053; subject-contrasts with p <= 0.10 (paper: all p > 0.10): 2 of 14
624	distance: subject-contrasts with a cluster p < 0.05: 1, < 0.025: 0; smallest p 0.028; subject-contrasts with p <= 0.10 (paper: all p > 0.10): 2 of 14
625	none: subject-contrasts with a cluster p < 0.05: 1, < 0.025: 0; smallest p 0.033; subject-contrasts with p <= 0.10 (paper: all p > 0.10): 4 of 14
626	
627	=== [24] markdown ===
628	## fig2-spatial-power and fig3-temporal-power
629	
630	> In the identity against spatial contrast of processing-interval power, 5 of 7 subjects showed
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/488f881d-d550-40bd-858a-ea297ffaf32c/tool-results/btwf1uhlk.txt",
 "offset": 1010,
 "limit": 360
}
```

```
1010	              f" pooled pairs {pooled.mean():.2f} +- {pooled.std(ddof=1):.2f}; pairs below -1.96 {int((pooled < -1.96).sum())}/{len(pooled)},"
1011	              f" above 1.96 {int((pooled > 1.96).sum())}; within tolerance or beyond: (a) {v.mean() <= exp + tol}, (b) {pooled.mean() <= exp + tol}")
1012	--- out ---
1013	fig4-maintenance-parietal-led: expected delta-theta -40.03 (tol 4.0 or more negative), alpha-beta -30.37 (tol 3.04 or more negative)
1014	  (a) trial-averaged coherency, delta-theta: subjects below -1.96: 0/7; mean over subjects 0.03 +- 0.36; pooled pairs -0.17 +- 1.64; pairs below -1.96 170/1135, above 1.96 116; within tolerance or beyond: (a) False, (b) False
1015	  (a) trial-averaged coherency, alpha-beta: subjects below -1.96: 0/7; mean over subjects -0.12 +- 0.23; pooled pairs 0.02 +- 1.19; pairs below -1.96 49/1135, above 1.96 58; within tolerance or beyond: (a) False, (b) False
1016	  (b) per-trial PSI averaged, delta-theta: subjects below -1.96: 4/7; mean over subjects -0.31 +- 10.67; pooled pairs -4.38 +- 28.71; pairs below -1.96 563/1135, above 1.96 458; within tolerance or beyond: (a) False, (b) False
1017	  (b) per-trial PSI averaged, alpha-beta: subjects below -1.96: 0/7; mean over subjects 2.12 +- 2.07; pooled pairs 0.59 +- 17.42; pairs below -1.96 493/1135, above 1.96 538; within tolerance or beyond: (a) False, (b) False
1018	  deposited code (no conjugate), delta-theta: subjects below -1.96: 0/7; mean over subjects 58.54 +- 11.36; pooled pairs 58.05 +- 46.00; pairs below -1.96 0/1135, above 1.96 1134; within tolerance or beyond: (a) False, (b) False
1019	  deposited code (no conjugate), alpha-beta: subjects below -1.96: 0/7; mean over subjects 69.33 +- 9.67; pooled pairs 75.35 +- 26.85; pairs below -1.96 0/1135, above 1.96 1135; within tolerance or beyond: (a) False, (b) False
1020	  deposited code, parietal first, sign reversed, delta-theta: subjects below -1.96: 7/7; mean over subjects -55.56 +- 6.79; pooled pairs -57.02 +- 45.90
[... 345 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "baseline|shuffl|phase slope|PSI|neighbo|zero-pad|padded|trial-wise" 10.3389-fnsys.2018.00065.txt | head -60
```

```
23:Working memory task design and behavior. (A) Single-trial working memory task design. Following a 1-s pretrial fixation interval (−250 to −50 ms pretrial epoch used as baseline), subjects were directed to focus on either IDENTITY or RELATION information. Then, two common shapes were presented for 200 ms each in a specific spatiotemporal configuration (i.e., top/bottom spatial and first/second temporal positions). After a 900- or 1,150-ms jittered pre-cue fixation delay (“maintenance”), the test cue appeared (i.e., one word presented on screen for 800 ms), followed by a post-cue fixation delay of the same length (“processing”). Working memory was tested in a two-alternative forced choice test (0.5 chance rate). In the identity test (top), subjects indicated whether the pair was the SAME pair they just studied (correct response in this example: no). In the spatiotemporal relation test (bottom), subjects indicated which shape fit the TOP/BOTTOM spatial or FIRST/SECOND temporal relation cue (correct response for cue TOP or SECOND: circle). (B) Mean and per-subject task accuracy (top) and response time (RTs; bottom). *Significant result; error bars, SEM; S, subject; orange, spatial trials; blue, identity trials; pink, temporal trials.
25:Working memory task design and behavior. (A) Single-trial working memory task design. Following a 1-s pretrial fixation interval (−250 to −50 ms pretrial epoch used as baseline), subjects were directed to focus on either IDENTITY or RELATION information. Then, two common shapes were presented for 200 ms each in a specific spatiotemporal configuration (i.e., top/bottom spatial and first/second temporal positions). After a 900- or 1,150-ms jittered pre-cue fixation delay (“maintenance”), the test cue appeared (i.e., one word presented on screen for 800 ms), followed by a post-cue fixation delay of the same length (“processing”). Working memory was tested in a two-alternative forced choice test (0.5 chance rate). In the identity test (to
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/t.py <<'EOF'
import numpy as np, fcx3
rng=np.random.default_rng(1)
fs=1000.; ntr=33; npair=60; T=4501
time=np.arange(T)/fs-1.5
def run(x_a,x_b,foi,label):
    Fa,_=fcx3.fft_segment(x_a,time,fs,fcx3.PROC_WIN,foi)
    Fb,_=fcx3.fft_segment(x_b,time,fs,fcx3.PROC_WIN,foi)
    Fa=Fa-Fa.mean(0,keepdims=True); Fb=Fb-Fb.mean(0,keepdims=True)
    z=fcx3.psi_measures(Fa,Fb,np.random.default_rng(2),n_perm=300,deposited=True)
    for k,v in z.items():
        print(label,k,'mean %.2f sd %.2f frac|z|>1.96 %.2f'%(v.mean(),v.std(),(abs(v)>1.96).mean()))
foi=np.arange(2,8)
# null: independent pink-ish noise (smoothed)
from scipy import signal
b,a=signal.butter(2,30,fs=fs)
def noise(): return signal.lfilter(b,a,rng.standard_normal((ntr,npair,T)),axis=-1)
run(noise(),noise(),foi,'indep dt')
# coupled: B = A delayed 30 ms (A leads), plus noise
A=noise(); lag=30
B=np.roll(A,lag,axis=-1)+0.5*noise()
run(A,B,foi,'A leads 30ms dt')
run(A,B,np.arange(9,25),'A leads 30ms ab')
EOF
python3 $TMPDIR/t.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t.py", line 1, in <module>
    import numpy as np, fcx3
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls -d /home/runner/work/*/ ; which -a python3 python uv; ls ~/.local/bin 2>/dev/null | head
```

```
/home/runner/work/_PipelineMapping/
/home/runner/work/_actions/
/home/runner/work/_temp/
/home/runner/work/encore/
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q v && uv pip install -q -p v/bin/python numpy scipy pandas fsspec h5py statsmodels 2>&1 | tail -2; cd  && $TMPDIR/v/bin/python $TMPDIR/t.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t.py", line 1, in <module>
    import numpy as np, fcx3
ModuleNotFoundError: No module named 'fcx3'
```

**Agent calls Bash**

```bash
PYTHONPATH=. $TMPDIR/v/bin/python $TMPDIR/t.py
```

```
indep dt a mean 0.14 sd 1.52 frac|z|>1.96 0.20
indep dt b mean -0.85 sd 14.12 frac|z|>1.96 0.82
indep dt code mean 25.85 sd 69.91 frac|z|>1.96 1.00
indep dt code_rev mean -18.70 sd 17.99 frac|z|>1.96 0.92
A leads 30ms dt a mean 18.36 sd 6.51 frac|z|>1.96 1.00
A leads 30ms dt b mean 10.60 sd 6.36 frac|z|>1.96 1.00
A leads 30ms dt code mean 27.33 sd 33.27 frac|z|>1.96 1.00
A leads 30ms dt code_rev mean -30.16 sd 30.63 frac|z|>1.96 1.00
A leads 30ms ab a mean 2.39 sd 0.09 frac|z|>1.96 1.00
A leads 30ms ab b mean 1.94 sd 0.34 frac|z|>1.96 0.50
A leads 30ms ab code mean 36.89 sd 16.21 frac|z|>1.96 1.00
A leads 30ms ab code_rev mean -44.75 sd 17.67 frac|z|>1.96 1.00
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/c.py <<'EOF'
import numpy as np, fcx3
from scipy import ndimage
rng=np.random.default_rng(0)
nb={"none":np.zeros((0,2),int),"adj":np.array([(i,i+1) for i in range(7)])}
fp={k:0 for k in nb}; R=200
for r in range(R):
    X=ndimage.gaussian_filter1d(rng.standard_normal((40,8,1,60)),3,axis=-1)
    g=np.zeros(40,bool); g[:20]=True
    res,_=fcx3.cluster_test(X,g,nb,rng,n_perm=200)
    for k in nb:
        pm=min([p for _,p,_ in res[k]['pos']]+[p for _,p,_ in res[k]['neg']]+[1])
        fp[k]+= pm<0.05
print({k:v/R for k,v in fp.items()})
# planted effect
X=ndimage.gaussian_filter1d(rng.standard_normal((40,8,1,60)),3,axis=-1); X[:20,2:4,:,20:40]+=0.6
res,_=fcx3.cluster_test(X,g,nb,rng,n_perm=200)
print([(round(m,1),p,mk.any(axis=(1,2)).nonzero()[0].tolist()) for m,p,mk in res['adj']['pos'][:2]])
EOF
PYTHONPATH=. $TMPDIR/v/bin/python $TMPDIR/c.py
```

```
{'none': 0.125, 'adj': 0.08}
[(240.7, 0.0, [2, 3]), (21.8, 0.195, [0])]
```

**Agent**

**Verifier report, round 1: Johnson et al. 2019 (doi:10.3389/fnsys.2018.00065) on CRCNS fcx-3**

The claims file has 17 claims, and the notebook tests all of them; none is treated as blocked, so step 4 did not apply. I ran the helper's PSI and cluster-test code on synthetic data, using a scratch environment in `$TMPDIR` and no dataset files. I did not download the dataset or re-run the notebook.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| table1-electrodes | partially_reproduced | Cell 15 finds 187 channels against the paper's 192, because s4 has 5 parietal channels where Table 1 lists 10. It finds 1135 pairs against 1129. Both totals are within 10%, and the PFC mean is 19.0. |
| trial-counts | reproduced | Cell 17: correct trials 95.7 per subject; identity 32.1, spatial 32.9, temporal 30.7, all with ranges matching. Incorrect trials under reading (b) average 17.3 (4 to 25). |
| fig1b-accuracy | reproduced | Per-subject, per-condition accuracy runs from 0.625 to 0.975 (reading b). The logit mixed model on single trials gives p = 0.28, or 0.16 with two dummy terms. Both are above 0.05, though below the paper's p > 0.50. |
| fig1b-rt-identity-slower | reproduced | Reading (a): omnibus F(1,19) = 6.04, p = 0.024. Identity against spatial p = 0.005, identity against temporal p = 0.010, with identity longer in 7 of 7 subjects. Spatial against temporal p = 0.25. The F values sit just below the paper's bounds (6.50, 13.78, 10.95). |
| erp-no-condition-difference | reproduced | With adjacent neighbours, none of the 14 subject-contrasts has a cluster at p < 0.05 (smallest 0.053). With 0.025 per tail, none has one under any neighbour reading. With 0.05 per tail, the distance and no-neighbour readings each give one (0.028 and 0.033). 2 to 4 of 14 have p ≤ 0.10, against the paper's "all p > 0.10". |
| fig2-spatial-power | partially_reproduced | Counts of 5 and 2 match under the adjacent and distance readings. The percentages do not: 39.7 and 22.5 (adjacent) or 49.7 and 28.4 (distance), against 54 and 36. Every significant effect has p < 0.04. |
| fig3-temporal-power | partially_reproduced | Counts of 4 and 2 match only with adjacent neighbours, 0.025 per tail and assignment (b). The percentages are about 39 and 23 against 68 and 37. Other readings give counts within one subject. |
| power-difficulty-subjects | reproduced | Under reading (b)(i), every subject with an identity > other effect (s1, s4, s7, depending on the neighbour reading) has longer identity RT and lower identity accuracy. s3 also has both, so reading (ii) fails. This rests on power claims that are only partially reproduced. |
| power-low-frequencies | reproduced | Only one combination of the six (distance neighbours, mask reading (b)) meets every condition: 2–24 Hz larger than 25–40 Hz, and local maxima in both bands for all three effects. The result is fragile (problem 9). |
| fig4-maintenance-parietal-led | not_reproduced | Under P1 readings (a) and (b), the subject means are 0.03 and −0.12 (reading a) or −0.31 and 2.12 (reading b). No subject is below −1.96 in alpha-beta. Only the "code_rev" variant reaches the targets, and it is not a valid reading (problem 2). |
| fig4a-delta-theta-shift | partially_reproduced (by the letter of the criterion) | Reading (a): F = 1.2, p = 0.27, and 2 of 7 subjects above zero. Reading (b): processing exceeds maintenance (F = 59, p = 2e-14), with 4 of 7 subjects above zero and a mean of −0.17 against the paper's F of 1936 and mean of 6.01. Reading (b)'s z is uncalibrated (problem 1). |
| fig4c-alpha-beta-shift | not_reproduced | Under readings (a) and (b), 5 of 7 subjects are below zero (the partial bar needs 6). The means are −0.03 and −1.89 against −12.6. Again, only "code_rev" passes. |
| directional-pairs | reproduced (by the letter of the criterion) | Reading (b) gives 1014 delta-theta and 1043 alpha-beta pairs, within tolerance; reading (a) gives 264 and 118. But independent noise under reading (b) gives about 82% of pairs with \|z\| > 1.96 (problem 1), so the match carries no evidence of real directionality. |
| fig5a-delta-theta-epochs | not_reproduced | Reading (a) finds no significant time points. Reading (b) finds sustained runs at 110–230, 300–400 and 460–600 ms (spatial) and 120–250, 290–390 and 680–840 ms (temporal). There is no early epoch starting at 0, and the late epochs have the wrong sign. |
| fig5a-identity-direction | not_reproduced | None of the four epoch values meets the criterion under any averaging reading (a, b, c, B) for either P1 reading. Examples: 0.35 against > 2.62, and 4.44 against < −3.57. |
| fig5a-spatiotemporal-bidirectional | not_reproduced | Under reading (b), the reading whose pair selection matches directional-pairs, the grand mean passes \|z\| ≥ 1.96 at 42 and 40 of 91 points (maximum 5.44 and 6.36). Under reading (a) every \|z\| < 1.96, but (a) shows nothing anywhere, including where the paper reports \|z\| ≈ 40, so the absence there is uninformative. |
| fig5b-alpha-beta-no-sustained | reproduced | Reading (b): 66 and 75 of 91 points are FDR-significant, and the longest same-sign runs are 80 and 90 ms, so nothing is sustained. Reading (a) gives no significant points, which would be partial. |

### B. Problems

1. **[affects a conclusion]** `fcx3.psi_measures`: the null does not compute the same statistic as the observed PSI, so z is not calibrated under either reading.
   - In reading (b), the observed value is the mean over trials of per-trial unit-phasor slopes, while the null is the slope of the bin-shuffled trial-mean phasor, whose magnitude is about 1/√trials.
   - In reading (a), the observed value sums nf−1 adjacent bins, while the null sums nf randomly paired bins.
   - On independent filtered noise (33 trials, 60 pairs, delta-theta), the share of pairs with \|z\| > 1.96 is 20% under (a) (SD 1.5) and 82% under (b) (SD 14).
   - The paper says it "shuffled the frequencies in one signal and re-computed PSI". This bears on directional-pairs, fig4a, fig4c, fig4-maintenance and all four fig5 claims.
2. **[affects a conclusion]** `psi_measures(deposited=True)`, cells 33–36: the "code" and "code_rev" variants compute X·Y/√(X²·conj(Y²)), which equals ±e^{2iφ_Y}. That depends only on the second channel's phase.
   - Its sign is fixed by which channel is placed second.
   - Independent noise gives 92–100% "significant" pairs.
   - These variants must not count as a reading. They are the only route to the fig4-maintenance and fig4c targets.
   - If the paper's own code has this bug, it may explain the paper's very large z values. That is worth reporting, not testing.
3. **[does not affect a conclusion]** `psi_measures(null_per_bin=True)` averages nf identical replicate nulls. It is not a per-frequency null, despite the docstring and the paper's "at each … frequency point".
4. **[affects a conclusion]** Cells 22–26 and the `neighbours` function: the notebook says it read `analysis_scripts.zip`, but it never reports what the scripts set for neighbours or for the per-tail cluster alpha. Both decide the ERP and power outcomes; for example, the fig3 counts match under only one combination.
5. **[affects a conclusion]** `analyse_subject`, ERP section: the baseline is one mean per channel, taken over all trials and time. That constant cannot change the t-test, so the baseline has no effect.
   - The paper's "processing minus pretrial mean" also allows a per-trial baseline, which was not run.
   - The Results say "1–30 Hz bandpass" while the Methods give a 30-Hz low-pass; only the low-pass was run.
6. **[affects a conclusion]** `tfr_fourier`, power and time-resolved PSI: windows at low frequencies (up to ±750 ms at 2 Hz) take in data outside the 900-ms segment.
   - Processing windows reach back into the cue and forward into the response period, and identity RT is longer, so condition differences can leak in.
   - Baseline windows reach into the start screen.
   - The paper and both S1 readings describe zero-padded segments. The notebook cites power_compute.m for this choice, which I could not check, and runs neither S1 reading.
7. **[does not affect a conclusion]** Cell 10, jitter check: the 70–150 Hz processing-window response in 1150-ms trials is shifted by +0.21 to +0.26 s against 900-ms trials in s2, s3 and s4 ("clear"), and by +0.28 to +0.35 s, not clear, in s1, s5 and s6. s4's encoding window also shifts. The processing epochs may be misaligned for about half the trials. The notebook does not resolve this; whatever it said was in the removed summary.
8. **[does not affect a conclusion]** Claims-file misreading: P2 and fig5b say sustained means "at least 100 ms", but the Figure 5 legend says ">100 ms". No outcome changes either way.
9. **[does not affect a conclusion]** Cell 30: the local-maximum rule counts the 2-Hz edge as a maximum, and the claim passes in only one of six combinations. It is fragile.
10. **[does not affect a conclusion]** `paired_lme` treats 1135 pairs that share electrodes as independent. This follows the paper's degrees of freedom, but it inflates F and p in fig4 and fig5.

### C. What I could not check

- **The deposited scripts.** I could not see psianalysis.m (conjugate, null construction), power_compute.m (padding), erp_compute.m (baseline) or subtracterp.m. The notebook should print the relevant script lines and the cluster-test settings (neighbours, alpha per tail).
- **PSI calibration on the real data.** A surrogate run, such as PSI computed between trial-shuffled PFC and parietal data with its rate of \|z\| > 1.96 printed, would show whether readings (a) and (b) hold 5% on the real data.
- **The jitter shift.** Cue-locked 70–150 Hz traces per delay group, and a rerun of the processing analyses on 900-ms trials only, would show whether it matters.
- **Per-subject power percentages.** Only the adjacent reading is printed per subject. I could not compare with the paper's per-subject figure values, which the claims file did not read either.

## End of run

15 turns, 5 minutes, $1.72 at API prices, result: success.
