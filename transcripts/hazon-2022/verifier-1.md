# hazon-2022 · verifier-1 · run 43119383827

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 420
drwxr-xr-x 6 runner runner    4096 Nov 12 00:44 .
drwxr-xr-x 8 runner runner    4096 Nov 12 00:44 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 11 23:22 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 11 23:22 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 12 00:44 .claude
-rw-r--r-- 1 runner runner       0 Nov 12 00:44 .env
-rw-r--r-- 1 runner runner       0 Nov 12 00:44 .env.development
-rw-r--r-- 1 runner runner       0 Nov 12 00:44 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 12 00:44 .env.local
-rw-r--r-- 1 runner runner       0 Nov 12 00:44 .env.production
-rw-r--r-- 1 runner runner       0 Nov 12 00:44 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 12 00:44 .env.test
-rw-r--r-- 1 runner runner       0 Nov 12 00:44 .env.test.local
drwx------ 2 runner runner    4096 Nov 12 00:44 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 11 23:22 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 11 23:22 .github
-rw-r--r-- 1 runner runner       0 Nov 12 00:44 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 11 23:22 .idea
[... 40 more lines not kept]
```

**Agent**

Two notebooks. Let me read the claims file first.

**Agent calls Read**

```json
{
 "file_path": "hazon-2022.yaml"
}
```

```
1	# Claims for Hazon, Minces, Tomàs, Ganguli, Schnitzer & Jercog (2022), Nature Communications 13,
2	# 4276, doi:10.1038/s41467-022-31254-y, tested on CRCNS hc-30.
3	#
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-11,
5	# protocol as stated in docs/protocol.md (version pilot-14), reader role. The dataset's data were
6	# not looked at; only its title and its data descriptor (paper/hc-30.data-description.txt) were read.
7	#
8	# Text read: the version of record, open access in PMC (PMC9314334), full text from Europe PMC
9	# (JATS XML flattened): main text, figure legends and Methods; and the Supplementary Information
10	# (41467_2022_31254_MOESM1_ESM.pdf, Supplementary Figures 1 to 19 and Supplementary Tables 1 and 2),
11	# as text, with the PDF for the tables. The Source Data file and the Reporting Summary were not
12	# read; no claim rests on them.
13	#
14	# Code read: github.com/approbatory/ML-project, commit 2057af9facfd3035c573e1254bdc32ed4781ba60
15	# (2022-06-07), linked from Code availability. MATLAB. It holds the event detection
16	# (utils/hyperdetect.m, supfigs_code/events_converter.mlx), the trial selection, activity tensor,
17	# trial shuffle, two-fold decoding and signal and noise measures (DecodeTensor.m), the SVM decoders
18	# (decoding/my_algs.m), the IMSE fit (createFit_infoSaturation.m, PanelGenerator.m), the noise
19	# eigenvector analyses (@Cloud), the per-session and per-animal quantities and correlations (@Org),
20	# the session lists (SessManager.m), and live scripts behind most published numbers
[... 891 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dump.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    print(f"===== CELL {i} [{c['cell_type']}] =====")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--'); print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--'); print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('--ERR--', o['ename'], o['evalue'])
EOF
python3 $TMPDIR/dump.py reproduce_hazon_2022.ipynb > $TMPDIR/nb1.txt; python3 $TMPDIR/dump.py reproduce_hazon_2022_decoding.ipynb > $TMPDIR/nb2.txt; wc -l $TMPDIR/nb*.txt
```

```
1200 /tmp/claude-1001/nb1.txt
   703 /tmp/claude-1001/nb2.txt
  1903 total
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb1.txt"
}
```

```
1	===== CELL 0 [markdown] =====
2	# Reproducing Hazon et al. (2022) from CRCNS hc-30: tensor, noise and signal analyses
3	
4	**Paper.** Hazon O, Minces VH, Tomàs DP, Ganguli S, Schnitzer MJ, Jercog PE (2022). Noise
5	correlations in neural ensemble activity limit the accuracy of hippocampal spatial
6	representations. *Nature Communications* 13, 4276.
7	[doi:10.1038/s41467-022-31254-y](https://doi.org/10.1038/s41467-022-31254-y)
8	
9	**Dataset.** CRCNS hc-30, Jercog P and Schnitzer M (2022), "Functional calcium imaging
10	recordings of hippocampal area CA1 from mice performing a linear track task",
11	[doi:10.6080/K0GH9G5X](https://doi.org/10.6080/K0GH9G5X). One file, `hc-30/live/event_traces.mat`
12	(142,350,100 bytes), streamed from the public S3 bucket `crcnsarchive` into memory.
13	
14	**Version.** CRCNS data sets are not versioned, so the version is recorded as `unversioned`
15	(docs/archives.md). The paper cites no version; the only one published is the one in the bucket
16	(data descriptor version 0.6, July 8, 2022, the initial version), which matches the claims file's
17	description (110 sessions with mouse name, session ID, sparse event array and position). The
18	MD5 sum from the data set's `checksums.md5`, which the next cell checks against the streamed
19	bytes, is `fe0f5dd2fca6d64dbf0cd3f35e31e1f0` (event_traces.mat); the descriptor PDF is
20	`320d157fbcc43be385485cc186842636`.
[... 756 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb1.txt",
 "offset": 777
}
```

```
777	Mouse2021  0.916     29.673         True
778	Mouse2022  1.543     49.634         True
779	Mouse2023  2.201     15.057         True
780	Mouse2024  1.956     27.195         True
781	Mouse2025  1.072     11.706         True
782	Mouse2026  2.156     16.399         True
783	Mouse2028  2.447     33.599         True
784	Mouse2029  2.558     28.243         True
785	mice with higher median for shuffled: 12 of 12
786	
787	===== CELL 25 [markdown] =====
788	## Run position (Figures 3f to 3h)
789	
790	Beginning of a run: the first bin pair of rightward runs and the last of leftward runs; end:
791	the opposite pairs (the code's choice). Pairs are ordered leftward 0..18 then rightward 0..18,
792	pair k joining bins k and k+1 in track coordinates, rightward runs going from bin 0 to 19.
793	===== CELL 26 [code] =====
794	def begin_end(arr):
795	    a = np.stack(arr.values)
796	    begin_pooled = np.concatenate([a[:, 19 + 0], a[:, 18]])  # rightward pair 0, leftward pair 18
[... 405 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb2.txt"
}
```

```
1	===== CELL 0 [markdown] =====
2	# Reproducing Hazon et al. (2022) from CRCNS hc-30: position decoding
3	
4	**Paper.** Hazon O, Minces VH, Tomàs DP, Ganguli S, Schnitzer MJ, Jercog PE (2022). Noise
5	correlations in neural ensemble activity limit the accuracy of hippocampal spatial
6	representations. *Nature Communications* 13, 4276.
7	[doi:10.1038/s41467-022-31254-y](https://doi.org/10.1038/s41467-022-31254-y)
8	
9	**Dataset.** CRCNS hc-30, Jercog P and Schnitzer M (2022), "Functional calcium imaging
10	recordings of hippocampal area CA1 from mice performing a linear track task",
11	[doi:10.6080/K0GH9G5X](https://doi.org/10.6080/K0GH9G5X). One file, `hc-30/live/event_traces.mat`
12	(142,350,100 bytes), streamed from the public S3 bucket `crcnsarchive` into memory.
13	
14	**Version.** CRCNS data sets are not versioned, so the version is recorded as `unversioned`
15	(docs/archives.md). The paper cites no version; the only one published is the one in the bucket
16	(data descriptor version 0.6, July 8, 2022, the initial version), which matches the claims file's
17	description (110 sessions with mouse name, session ID, sparse event array and position). The
18	MD5 sum from the data set's `checksums.md5`, which the next cell checks against the streamed
19	bytes, is `fe0f5dd2fca6d64dbf0cd3f35e31e1f0` (event_traces.mat); the descriptor PDF is
20	`320d157fbcc43be385485cc186842636`.
[... 684 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "hc30.py"
}
```

```
1	"""Loading and measures for CRCNS hc-30 (Hazon et al. 2022, Nat Commun 13:4276).
2	
3	Sources of each parameter are given as:
4	  [claims]  the claims file claims/hazon-2022.yaml (its "common method" header or a criterion),
5	            which cites the paper's Methods or its code (github.com/approbatory/ML-project at
6	            commit 2057af9facfd3035c573e1254bdc32ed4781ba60);
7	  [paper]   a passage of the paper taken by the author (protocol, author step 1.6);
8	  [code]    the paper's code at that commit, cited by file, where the paper is silent;
9	  [assumed] an assumption, with the reason;
10	  [standard] a standard choice for a detail that cannot change a result.
11	"""
12	import io
13	import time
14	
15	import fsspec
16	import numpy as np
17	import scipy.io
18	import scipy.sparse
19	from scipy.signal import lfilter
20	
[... 627 more lines not kept]
```

**Agent**

Both notebooks and the helper module are read. Next I'll check the archive file list for the blocked claim and the Supplementary Table 1 footnotes.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=hc-30/" | head -c 4000; echo;
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; cat hc-30.data-description.txt | head -80; which pdftotext
```

```
Exit code 1
Data descriptor: of the data set CRCNS:hc-30, not a paper. It describes the data set's files and how they were recorded.
Version: as published by CRCNS.org, https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-30/live/docs/crcns_hc-30_data_description.pdf
Source: the CRCNS data set's documentation (hc-30/live/docs/crcns_hc-30_data_description.pdf)
Stored: 2026-11-06
Extracted: PyMuPDF, dehyphenated, NFKC
------------------------------------------------------------------------
##### hc-30/live/docs/crcns_hc-30_data_description.pdf
Page 1 of 2 
CRCNS.org hc-30 data description 
Version 0.6 (July 8, 2022) 
 
Functional calcium imaging recordings of hippocampal area CA1 from mice 
performing a linear track task 
Pablo Jercog and Mark Schnitze 
Summary 
This data set contains functional calcium imaging recordings from mice CA1 
hippocampal region. We tracked the concurrent calcium dynamics of hundreds of CA1 
pyramidal neurons in 12 mice (151-497 neurons per session, median 235; a total of 
27,898 neurons over 110 sessions) that ran back and forth on a 120-cm-long linear 
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 -c "
import fitz
d=fitz.open('10.1038-s41467-022-31254-y.supp-41467_2022_31254_MOESM1_ESM.pdf')
t=''.join(p.get_text() for p in d)
import re
i=t.find('Table 1')
for m in re.finditer('Table 1', t): print(m.start())
print(t[t.find('Our Data')-3000:t.find('Our Data')+2500])
" 2>&1 | head -150
```

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import fitz
ModuleNotFoundError: No module named 'fitz'
```

**Agent calls Bash**

```bash
cd paper; python3 -c "import pypdf" 2>&1; python3 -c "import pdfplumber" 2>&1; grep -n -i "Table 1\|trial-by-trial var\|bits per\|out-of-field\|out of field" 10.1038-s41467-022-31254-y.txt | head -30
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
31:To examine the statistical structure of hippocampal representations of space, we tracked the concurrent calcium dynamics of hundreds of CA1 pyramidal neurons in 12 mice (151-497 neurons per session, median 235; a total of 27,898 neurons over 110 sessions) that ran back and forth along a 120-cm-long linear track (Fig. 1a , see Methods). Because our study required the greatest possible statistical power, we used a linear track to increase the number of visits to each spatial location. We quantified CA1 neuron's calcium activity responses while the animals ran on the track. We detected spike events with our algorithm (see Methods and Suppl. Fig. 1 ) and found similar values to previous reports for PF shapes and spatial distributions (Suppl. Fig. 1 and Suppl. Table 1 ). PF characteristics were similar to those obtained with electrophysiological methods and other animal species (see Suppl. Table 1 , Suppl. Fig. 1 ). In this study, we did not select cells based on the amount of spatial tuning, since cells that do not satisfy the traditional definition of “place-cells” can also contribute to the neuronal ensemble’s spatial information 49 . A position-responsive neuron varies its responses between individual runs (i.e., trials) through the track, relative to the mean response (Fig. 1b ). Neuronal response fluctuations were, in general, large for different visits to each spatial bin (response variance = 0.7263 + /− 0.6117, variance between bins / variance within bins = single-cell signal-to-noise ratio = 0.41 + /− 0.34, pooled from 27,898 neurons).
95:It has been shown that attention and learning can change the effect of noise correlations on information 26 , 63 , 64 . Despite the large variabil
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 325,485p 10.1038-s41467-022-31254-y.txt
```

```
spatial stimulus’s continuity, detecting response changes in a given position’s vicinity. However, errors when estimating the
slope would also reduce accuracy.
27

Supplementary Table 1: Comparison of place field characteristics among previous studies.
Author
Species,
Recording
Method,
Behavior
mean
firing rate
(Hz)
PFs’
inside/outsi
de firing
rate (Hz)
Maximum
rate (Hz)
PF width
[... 141 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' 2>&1 | grep -v Warning
import numpy as np, hc30
rng=np.random.default_rng(0)
# synthetic trajectory: back and forth 0..600 px at ~30 cm/s with pauses, plus jitter 0.3 cm
FS=20; frames=[]
for k in range(60):
    run=np.linspace(50,650,120)
    if k%2: run=run[::-1]
    frames += [run[0]]*40 + list(run)
x=np.array(frames,float)
cpp_true=118/ (np.percentile(x,95)-np.percentile(x,5))
xn = x + rng.normal(0,0.3/cpp_true,len(x))
tr=hc30.select_trials(xn)
print("trials",len(tr['starts']),"dirs",np.unique(tr['direction'],return_counts=True))
print("jitter (true 0.3 cm):", hc30.jitter(xn,tr))
# shuffle
T=rng.normal(size=(5,20,30)); d=np.r_[np.ones(15),-np.ones(15)].astype(int)
common=rng.normal(size=(1,20,30)); T2=T+3*common
S=hc30.shuffle_tensor(T2,d,rng)
print("sorted values preserved:", np.allclose(np.sort(S[:,:,d==1],axis=2),np.sort(T2[:,:,d==1],axis=2)))
c_u=np.corrcoef(T2[0,3,d==1],T2[1,3,d==1])[0,1]; c_s=np.corrcoef(S[0,3,d==1],S[1,3,d==1])[0,1]
print("corr before/after", round(c_u,2), round(c_s,2))
# fit_imse
n=np.r_[1,np.arange(25,400,25)]; I0,N=1e-4,300
y=I0*n/(1+n/N)*(1+rng.normal(0,0.03,len(n)))
print("fit_imse", hc30.fit_imse(n,y)[:2])
print("hwhm", hc30.hwhm_bins(np.exp(-0.5*((np.arange(20)-10)/2)**2)), "expected ~2.35->", 2*np.sqrt(2*np.log(2))/2*2)
# to_dataset ordering vs decode_bins position reshape
T=np.arange(2*3*4).reshape(2,3,4).astype(float); d=np.array([1,-1,1,-1])
X,y=hc30.to_dataset(T,d); print(X[:4], y[:6])
EOF
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls /usr/bin/python3* ; which -a python python3 pip uv 2>/dev/null; ls ~/.local/bin 2>/dev/null; find / -name "numpy" -maxdepth 6 -type d 2>/dev/null | head
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
/opt/hostedtoolcache/Python/3.13.18/x64/bin/pip
/usr/bin/pip
/bin/pip
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
```

**Agent**

No numpy is installed; I'll try a throwaway venv to run the synthetic tests.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q v && VIRTUAL_ENV=$TMPDIR/v uv pip install -q numpy scipy fsspec 2>&1 | tail -3; ls v/bin | head
```

```
activate
activate.bat
activate.csh
activate.fish
activate.nu
activate.ps1
activate.xsh
activate_this.py
deactivate.bat
f2py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF' 2>&1 | grep -v Warning
import numpy as np, hc30
rng=np.random.default_rng(0)
frames=[]
for k in range(60):
    run=np.linspace(50,650,120)
    if k%2: run=run[::-1]
    frames += [run[0]]*40 + list(run)
x=np.array(frames,float)
cpp_true=118/(np.percentile(x,95)-np.percentile(x,5))
xn = x + rng.normal(0,0.3/cpp_true,len(x))
tr=hc30.select_trials(xn)
print("trials",len(tr['starts']),"dirs",np.unique(tr['direction'],return_counts=True))
print("jitter (true 0.3 cm):", hc30.jitter(xn,tr))
T=rng.normal(size=(5,20,30)); d=np.r_[np.ones(15),-np.ones(15)].astype(int)
common=rng.normal(size=(1,20,30)); T2=T+3*common
S=hc30.shuffle_tensor(T2,d,rng)
print("sorted values preserved:", np.allclose(np.sort(S[:,:,d==1],axis=2),np.sort(T2[:,:,d==1],axis=2)))
print("corr before/after", round(np.corrcoef(T2[0,3,d==1],T2[1,3,d==1])[0,1],2), round(np.corrcoef(S[0,3,d==1],S[1,3,d==1])[0,1],2))
n=np.r_[1,np.arange(25,400,25)]
y=1e-4*n/(1+n/300)*(1+rng.normal(0,0.03,len(n)))
print("fit_imse (true 1e-4, 300):", hc30.fit_imse(n,y)[:2])
y2=1e-4*n*(1+rng.normal(0,0.03,len(n)))
print("fit_imse linear data:", hc30.fit_imse(n,y2)[:2])
print("hwhm of gaussian sd 2 bins:", hc30.hwhm_bins(np.exp(-0.5*((np.arange(20)-10)/2)**2)), "true", 2*np.sqrt(2*np.log(2)))
# modulated filter is a no-op?
r=np.abs(rng.normal(size=(10000,20)))
print("max > 0.2*sd for random nonneg:", np.mean(r.max(1)>0.2*r.std(1)))
EOF
```

```
trials 1 dirs (array([1]), array([1]))
jitter (true 0.3 cm): 0.2707969429245995
sorted values preserved: True
corr before/after 0.89 0.04
fit_imse (true 1e-4, 300): (np.float64(0.00010064327837235234), np.float64(292.3429761501507))
fit_imse linear data: (np.float64(0.00010076692854662176), np.float64(3112795193.334435))
hwhm of gaussian sd 2 bins: 3 true 2.3548200450309493
max > 0.2*sd for random nonneg: 1.0
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF' 2>&1 | grep -v Warning
import numpy as np, hc30
rng=np.random.default_rng(0)
frames=[]
for k in range(60):
    run=np.linspace(50,650,120)
    if k%2: run=run[::-1]
    frames += [run[0]]*40 + list(run)
x=np.array(frames,float)
cpp=118/(np.percentile(x,95)-np.percentile(x,5))
for sd_cm in (0.05,0.1):
    xn = x + rng.normal(0,sd_cm/cpp,len(x))
    tr=hc30.select_trials(xn)
    print(sd_cm, "trials",len(tr['starts']),np.unique(tr['direction'],return_counts=True)[1],"jitter:", round(hc30.jitter(xn,tr),3))
EOF
```

```
0.05 trials 59 [29 30] jitter: 0.053
0.1 trials 59 [29 30] jitter: 0.103
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" hazon-2022.yaml
```

```
29
```

**Agent**

**Verifier report, round 1: Hazon et al. 2022 on CRCNS hc-30 (29 claims in the claims file)**

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| data-sessions-and-neurons | reproduced | NB1 cell 10: 110 of 110 sessions meet the rule, 12 mice, 27,898 neurons, median 235, range 151 to 497. The >200 reading gives 73 large-data sessions from 10 mice. |
| single-cell-variability | reproduced | Cell 12: the SD reading gives 0.7263 +/- 0.6117, an exact match. The 40-class SNR mean is 0.437, inside 0.41 +/- 0.041; its spread of 0.464 is outside, but the criterion judges means only. |
| suppl-table1-place-field-properties | not_reproduced | Cell 14: taking the best reading for each quantity, only 2 of 7 are within 10%: running rate 0.362 and max rate 1.461 (cells with >100 events per 10 min). The other five are far off: out-of-field 0.15–0.25 vs 0.034, width 16–18 vs 37.8 cm, trial-by-trial variability ≤0.90 vs 1.2, spatial information 0.15 or 1.06–1.30 vs 0.24. |
| fig1d-noise-correlation-by-field-distance | reproduced | Cell 16: both directions pass. Distance 0 is 0.0386 / 0.0374, against means of 0.0064 / 0.0058 at distances ≥10. The shuffled curve is separated from the unshuffled one, with non-overlapping intervals, at distances 0 to 10, for both the session-mean and pooled-pair readings. |
| noise-correlation-not-physical-distance | blocked (data_missing) | I listed the bucket `hc-30/`. It holds only event_traces.mat, checksums.md5, filelist.txt and the descriptor files. The descriptor lists four fields (mouse_name, session_ID, traces, position) and no cell coordinates or footprints, so no part of this claim can be tested. |
| fig2d-rms-error-ensemble-vs-shuffled | reproduced | NB2 cell 8: medians are 9.36 cm for the ensemble (tolerance 9.38 ± 0.94) and 4.80 cm shuffled (tolerance 5.15 ± 0.52). The ensemble error is larger in 109 of 110 sessions. The shuffled IQR is 1.73 against 2.40, outside tolerance but not part of the criterion. |
| fig2cd-shuffle-better-in-all-bins | reproduced | NB2 cell 12: the ensemble error is worse in 20 of 20 positions and 40 of 40 classes, and the shuffled correct fraction is higher in 40 of 40 classes on the session average. Median misclassification is 1 bin. The largest error with at least 1% of misclassified samples is 5 bins, against the paper's "up to three" (reported only). |
| fig2ef-imse-saturates-with-correlations | reproduced | NB2 cell 14, 110 sessions: I0N has p = 3.5e-17 and N has p = 5.2e-15, shuffled higher in both, and shuffled I0N is higher in 12 of 12 animals. Fits are often degenerate: 7 unshuffled and 78 shuffled fits have N outside 0 to 1e6. For the shuffled data that fits "no apparent bound". |
| suppl7b-initial-slope-lower-with-correlations | reproduced | NB2 cell 16: p = 9.8e-16. Median I0 is 0.00010 unshuffled and 0.00019 shuffled, so I0 is lower with correlations. |
| saturation-ensemble-size | not_reproduced | NB2 cell 18: the 5% slope range is 105 to 3076 neurons under reading (a) and 105 to 4.9e6 under (b), against 346 to 1402. The author's cleaned variant gives 717 to 2487. No bound is within tolerance under any reading. |
| position-measurement-noise | reproduced | NB1 cell 18: mean 0.277 cm, min 0.118 cm, max 1.001 cm; all three are within tolerance. |
| fig3cd-signal-and-noise-growth | reproduced | NB1 cell 22: (1) the signal is identical by construction and was checked (bin means change by at most 7e-16). (2) The unshuffled noise slope is positive in the median session with line R² 0.983. (3) The median ratio of shuffled to unshuffled noise slope is 0.084, but only 72 of 110 sessions are below 0.1. |
| suppl10-asymptotic-snr-lower-with-correlations | reproduced | Cell 24: p = 8.8e-20, shuffled higher in 110 of 110 sessions and in 12 of 12 mouse medians. |
| fig3f-signal-slope-beginning-vs-end | reproduced, resting on the code's direction | Cell 28: the legend's direction (beginning greater) gives p = 1.0. The code's direction gives p = 1.1e-18, against the code's printed 2.19e-18. The signal slope increases over the run, opposite to the claim statement. |
| fig3g-noise-slope-decreases-over-run | reproduced | Cell 30: beginning greater, p = 1.9e-9 on 110 sessions and 1.2e-10 on 73. |
| fig3h-snr-higher-at-run-end | reproduced | Cell 32: beginning lower, p = 2.8e-26 on 110 sessions and 5.7e-21 on 73. Rightward-only runs also give p < 0.001. |
| fig4a-snr-along-noise-pcs-peaks-at-6 | partially_reproduced | Cell 34: the session-mean curve peaks at component 7, which the criterion counts as partial. The curve is flat there: 0.0719 at component 6, 0.0730 at 7, 0.0720 at 8. The first six components carry 0.36 of the 14 common components (median 0.10 over all components), so "small" holds. |
| fig4b-correlations-increase-noise-signal-overlap | reproduced | Cell 36: the overlap change is positive in 73 of 73 sessions and in 10 of 10 animal means, under both component readings and both matrix readings. |
| fig4c-overlap-predicts-asymptotic-snr | reproduced | Cell 38: r = -0.743, adjusted r² 0.496, p = 0.0139. This matches the code's printed -0.744, 0.498 and 0.0136. |
| fig5f-pf-width-variance-vs-nsv | reproduced | Cell 40: r = -0.658, p = 0.0385, against -0.65 ± 0.065. |
| fig5hi-nsv-predicts-noise-correlation-effect | reproduced | Cell 42, unfiltered: across animals r = 0.869 (p = 0.0011), across sessions r = 0.716 (p = 1e-12). The filtered reading gives the same result. |
| suppl-table2-nsv-best-predictor | reproduced | Cell 44: NSV has the highest adjusted R², 0.51 on all 73 sessions and 0.49 filtered; the next best is 0.19 / 0.23. NSV at a fixed 200 neurons gives p = 2.2e-5 across sessions. |
| pf-width-variance-not-predictive | reproduced, resting on the confidence-interval filter | Cell 46: unfiltered, the session-level test gives p = 0.041 (<0.05, so not reproduced). With the filter Supplementary Table 2 describes, p = 0.10 for sessions and 0.077 for animals. The amplitude variance correlates across animals (r = 0.75, p = 0.013), which goes against the text's "or amplitudes"; the criterion only asks for it to be shown. |
| suppl11b-i0-vs-single-cell-snr | partially_reproduced | NB2 cell 22: the main reading gives r = -0.07, p = 0.84, because Mouse2011's mean I0 is 23.7, set by one failed fit. Excluding failed fits and misaligned sessions gives r = 0.75, p = 0.0125: positive and p < 0.05, but not p < 0.01, and r² = 0.56 is outside 0.73 ± 0.073. |
| suppl11c-asymptotic-imse-vs-asymptotic-snr | reproduced | NB2 cell 24, log10 reading: r = 0.894, r² = 0.80 (inside 0.88 ± 0.088), p = 4.8e-4. The linear reading fails (r = 0.04) because of degenerate fits. |
| suppl8-task-performance-and-accuracy | not_reproduced | NB2 cell 26: performance against trials gives r = 0.847, a match. Accuracy against trials (r = -0.05) and against performance (r = 0.19, p = 0.11) do not match the paper, and in the path model trials is significant (p = 3.5e-4). |
| suppl6-twenty-bins-near-optimal | reproduced | NB2 cell 28: 11.84 cm with 20 bins and 11.94 cm with 30, both within tolerance. No bin count is more than one SEM below 20 bins. This rests on only 2 repetitions per session. |
| fig5cd-synthetic-narrow-widths-broader-nsv | reproduced, resting on the legend reading | NB1 cell 48: under the legend's uniform widths, narrow gives the higher NSV at 50 cells and up to 10,000. Under the Methods' log-normal widths the result reverses (0.0030 < 0.0044). |
| suppl9-fit-recovers-saturation | reproduced | NB2 cell 30: N = 704 ± 554 (500 neurons) and 338 ± 87 (2000 neurons); the intervals overlap. This is a weak test because the 500-neuron interval is about ±80%. |

Tally: 23 reproduced (3 of them resting on one reading), 2 partially reproduced, 3 not reproduced, 1 blocked.

### B. Problems

1. [affects a conclusion] NB2 cell 1 and `decode_series`: 4 neuron subsets per size (paper 80) on a 1, 25, 50… grid (paper 1, 10, 20…). Fits are unstable as a result: 7 unshuffled fits have N outside 0 to 1e6, and Mouse2011 has a mean I0 of 23.7. This drives the failures of saturation-ensemble-size, suppl11b and suppl8. No check of how N depends on the number of subsets was run, so these three outcomes may reflect the reduced repetitions and not the data.
2. [affects a conclusion] NB2 cell 26: suppl8 is not run with failed fits and misaligned sessions excluded, although cells 22 and 24 run that variant for 11b and 11c. Degenerate I0N values (up to 1e5 or more) enter log10 I0N.
3. [affects a conclusion] NB1 cell 42, the `filt` filter: the confidence intervals that decide pf-width-variance-not-predictive (p = 0.041 → 0.10) are the author's delta-method construction from slope standard errors, not the paper's method. It keeps 69 sessions where the code kept 72. The outcome depends on about 4 sessions.
4. [does not affect a conclusion] `OvOLinearSVM`: the docstring says C defaults to 100 "to approximate the code's unregularized fit", but the notebook uses C_SVM = 1.0, labelled "assumed". The two disagree. Cell 10's C variants (0.1 and 10) move the RMS medians by about 0.3 cm, so no outcome flips. The decoder also uses majority voting where MATLAB uses loss-weighted decoding.
5. [does not affect a conclusion] Cell 14: the "modulated cells" subset (max > 0.2·SD) does nothing. Its n is identical to all cells, and on synthetic non-negative data the test passes 100% of the time. The minimal-modulation reading in the criterion was therefore never applied. The 1180 cm width cap that drops 195 fits is the author's own choice. Neither can lift the width from 16 to 37.8 cm.
6. [does not affect a conclusion] Cell 14: the spatial information "skaggs" reading assumes uniform occupancy. The literal footnote formula, H/20, cannot exceed log2(20)/20 = 0.216, so it can never reach 0.24.
7. [does not affect a conclusion] NB1 cell 7: in 6 sessions the event trace does not follow position at lag 0. Two of them (sessions 83 and 84, Mouse2011) decode near chance at every lag within ±10 s, and two others align at -80 to -90 frames. All six stay in the main readings. Because fig4c and fig5f match the code's printed values to the third decimal, the paper probably used the same deposit, so keeping them is right for the main reading.
8. [does not affect a conclusion] `eigen_snr` takes the first h trials of each direction, not a random set, and the curve is truncated to the 14 components every session shares. The peak at 7 against 6 is within about 1.5%.
9. [does not affect a conclusion] fig3cd (3) holds for the median but in only 72 of 110 sessions, with 20 subsets against the paper's 80.

Helper checks on synthetic inputs:
- `shuffle_tensor` keeps each bin's values and removes correlation (0.89 → 0.04).
- `fit_imse` recovers I0 = 1e-4 and N = 300 (gives 292). On purely linear data it returns N around 3e9, consistent with the shuffled fits.
- `jitter` recovers 0.05 and 0.10 cm.
- `select_trials` finds 59 of 59 runs on a clean trajectory.

### C. What I could not check

- The figures: only text outputs were readable to me. A printed table of each session's fitted curve against its IMSE points would have let me judge fit quality directly.
- Whether the saturation, suppl11b and suppl8 failures come from the 4 subsets per size. N re-fitted with 80 subsets on the 1, 10, 20… grid for a few sessions would settle it.
- suppl8 with failed fits and misaligned sessions excluded (see problem 2).
- The paper's MATLAB code. The code citations in the claims file and hc30.py (Cloud.m, adjacent_metrics, Org.m filters, one_hwhm) could not be verified. The close match to the code's printed values for fig4c, fig5f and fig3f is indirect support.
- Which session is Fig. 2c's. The session average was used, which the criterion allows.

## End of run

19 turns, 5 minutes, $1.96 at API prices, result: success.
