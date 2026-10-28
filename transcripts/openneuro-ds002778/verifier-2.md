# openneuro-ds002778 · verifier-2 · run 40602990927

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 516
drwxr-xr-x 6 runner runner    4096 Oct 27 23:39 .
drwxr-xr-x 7 runner runner    4096 Oct 27 23:39 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 27 23:29 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 27 23:29 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 27 23:39 .claude
-rw-r--r-- 1 runner runner       0 Oct 27 23:39 .env
-rw-r--r-- 1 runner runner       0 Oct 27 23:39 .env.development
-rw-r--r-- 1 runner runner       0 Oct 27 23:39 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 27 23:39 .env.local
-rw-r--r-- 1 runner runner       0 Oct 27 23:39 .env.production
-rw-r--r-- 1 runner runner       0 Oct 27 23:39 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 27 23:39 .env.test
-rw-r--r-- 1 runner runner       0 Oct 27 23:39 .env.test.local
drwx------ 2 runner runner      40 Oct 27 23:39 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 27 23:29 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 27 23:29 .github
-rw-r--r-- 1 runner runner       0 Oct 27 23:39 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 27 23:29 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 27 23:29 .mcp.json
[... 88 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat openneuro-ds002778-jackson-2019-01.yaml
```

```
<persisted-output>
Output too large (33.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/91ebaddc-9ff4-4c2f-a2f2-6e4923b32ff6/tool-results/b3nj02fs0.txt

Preview (first 2KB):
# Jackson, Cole, Voytek & Swann (2019) from OpenNeuro ds002778

Tests the findings of [Jackson et al. (2019)](https://doi.org/10.1523/ENEURO.0151-19.2019) on
[OpenNeuro ds002778](https://openneuro.org/datasets/ds002778/versions/1.0.5), snapshot 1.0.5, which
holds the resting EEG of 15 patients with Parkinson's disease off and on medication and 16 controls.
The paper's manual artifact marks and excluded electrodes are not in the dataset, so the analysis
rejects no samples and keeps all 32 scalp electrodes.

| Claim | Outcome |
|---|---|
| Beta sharpness ratio, steepness ratio and PAC fall with medication (C3/C4) | Partially reproduced (each test holds; one value per claim out of tolerance) |
| The same with a bipolar montage | Reproduced |
| No medication effect at F7/F8 or at T7/T8 | Reproduced |
| Topographies consistent with a sensorimotor origin | Partially reproduced |
| Off against controls: no difference in sharpness ratio or PAC | Reproduced |
| Off against controls: steepness ratio higher | Not reproduced (z and d match, FDR p 0.053) |
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat openneuro-ds002778-jackson-2019-01.yaml
```

```
<persisted-output>
Output too large (30.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/91ebaddc-9ff4-4c2f-a2f2-6e4923b32ff6/tool-results/bbb7gff25.txt

Preview (first 2KB):
schema_version: 2
id: openneuro-ds002778-jackson-2019-01
dataset:
  archive: openneuro
  id: ds002778
  version: 1.0.5
  doi: 10.18112/openneuro.ds002778.v1.0.5
paper: doi:10.1523/eneuro.0151-19.2019
date: 2026-10-27
entry: openneuro-ds002778-jackson-2019
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 36 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "openneuro-ds002778-jackson-2019-01.yaml"
}
```

```
1	schema_version: 2
2	id: openneuro-ds002778-jackson-2019-01
3	dataset:
4	  archive: openneuro
5	  id: ds002778
6	  version: 1.0.5
7	  doi: 10.18112/openneuro.ds002778.v1.0.5
8	paper: doi:10.1523/eneuro.0151-19.2019
9	date: 2026-10-27
10	entry: openneuro-ds002778-jackson-2019
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-12
19	  runner:
20	    platform: GitHub Actions
[... 561 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1523-eneuro.0151-19.2019.yaml"
}
```

```
1	# Claims for Jackson, Cole, Voytek & Swann (2019), eNeuro 6(3) ENEURO.0151-19.2019, on OpenNeuro ds002778.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-27,
3	# protocol as stated in docs/protocol.md.
4	#
5	# Text read: the version of record, full text from Europe PMC PMC6553574 (main text, Methods, figure
6	# legends, Tables 1 to 3). The only supplement is Extended Data 1, the analysis code, which is the
7	# GitHub repository read below. Figures were not opened; no claim needs a value read off a figure.
8	#
9	# Code read: https://github.com/SwannLab/Jackson_2019 at commit a7c89f50106aa4ccec76ace18bbfa45a5440545e
10	# (2020-05-19). It holds utils.py (loading the preprocessed traces, shape and PAC per recording),
11	# shape.py (zero crossings, peaks and troughs, sharpness, steepness), pac.py (normalized modulation
12	# index, Ozkurt and Schnitzler 2011) and notebooks Figure_1, Figures_2,3 and Figure_4. The notebooks
13	# print the Wilcoxon, rank sum, Spearman and Cohen's d values of Tables 1 and 2 (beta) and Figure 3.
14	# The code starts from preprocessed MATLAB files (AVG_motor.mat, rejectscombined.mat) that are not in
15	# the repository: the MATLAB preprocessing, the manual artifact marks, the mu/alpha analysis, the
16	# bipolar and CSD analyses, the F7/F8 and T7/T8 tests, the power spectra, the topographies and the Q4
17	# effect sizes (Table 3) are not in the code.
18	#
19	# Data the paper used (Methods, Participants and Data collection): resting scalp EEG from a dataset
20	# first published by George et al. (2013) and reanalysed by Swann et al. (2015). 15 PD patients (8
[... 621 more lines not kept]
```

**Agent**

Read the claims file (24 claims) and the attempt record (24 outcomes, round-1 responses included). Next I'm going through the notebook outputs.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_jackson_2019.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"===== CELL {i} [{c['cell_type']}]")
    src=''.join(c['source'])
    if c['cell_type']=='code' and len(src)>1500: src=src[:1500]+'\n...[truncated src]'
    print(src)
    for o in c.get('outputs',[]):
        if 'text' in o: print('--- out:'); print(''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d and 'image/png' not in d: print('--- out:'); print(''.join(d['text/plain']))
            elif 'image/png' in d: print('--- [image]')
        elif o.get('output_type')=='error': print('--- ERROR', o['ename'], o['evalue'])
EOF
wc -l $TMPDIR/nb.txt; grep -c "CELL" $TMPDIR/nb.txt
```

```
1911 /tmp/claude-1001/nb.txt
85
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	===== CELL 0 [markdown]
2	# Reproducing Jackson, Cole, Voytek & Swann (2019) from OpenNeuro ds002778
3	
4	**Paper.** Jackson N, Cole SR, Voytek B, Swann NC (2019). Characteristics of waveform shape in
5	Parkinson's disease detected with scalp electroencephalography. *eNeuro* 6(3)
6	ENEURO.0151-19.2019. [doi:10.1523/ENEURO.0151-19.2019](https://doi.org/10.1523/ENEURO.0151-19.2019).
7	The claims file was written from the version of record (Europe PMC PMC6553574: main text,
8	Methods, legends, Tables 1 to 3) and the paper's code, SwannLab/Jackson_2019 at commit a7c89f5.
9	
10	**Dataset.** [OpenNeuro ds002778](https://openneuro.org/datasets/ds002778/versions/1.0.5),
11	"UC San Diego Resting State EEG Data from Patients with Parkinson's Disease", snapshot 1.0.5,
12	DOI 10.18112/openneuro.ds002778.v1.0.5. The paper (2019) predates the dataset (first snapshot
13	1.0.0, 2020-05-05) and cites no version. 1.0.5 is the most recent published snapshot. Its
14	CHANGES list fixes to the README, citations, a medication entry of sub-pd22 (1.0.1) and Beck
15	scores (1.0.5); none changes the EEG files, so no earlier snapshot matches the paper better.
16	Files are read from the URLs the OpenNeuro API gives for this snapshot, into memory.
17	
18	**What the dataset holds.** Resting EEG (BioSemi, 32 scalp electrodes and 8 external
19	channels, 512 Hz) of 15 patients off and on medication and 16 controls, with UPDRS and other
20	scores in per-session JSON files. It holds no artifact marks and no bad-channel marks, which
[... 428 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 449,
 "limit": 450
}
```

```
449	print("\nSampling rate values:", rec_tab.sfreq.unique().tolist())
450	print("Duration equals sidecar RecordingDuration + 1 sample in all:",
451	      bool(np.allclose(rec_tab.dur_s, rec_tab.sidecar_dur_s)))
452	p
453	...[truncated src]
454	--- out:
455	 sub ses  sfreq  dur_s  sidecar_dur_s  n_chan  scalp_names_ok  status_all_good units  highcut  raw_mean_abs_uv  raw_max_abs_sum_uv  pre_sd_min  pre_sd_median  pre_sd_max max_sd_chan min_sd_chan
456	 hc1  hc  512.0  192.0          192.0      41            True             True    µV    104.0         11059.66          358934.899        5.57          11.53        46.0         Fp1         FC1
457	hc10  hc  512.0  201.0          201.0      41            True             True    µV    104.0          4338.66           56646.614        5.50           9.97        27.0         Fp1         FC1
458	hc18  hc  512.0  186.0          186.0      41            True             True    µV    104.0          5100.94          125518.862        4.42           5.74        14.6         Fp1         FC1
459	 hc2  hc  512.0  194.0          194.0      41            True             True    µV    104.0          4981.58           59388.984        3.99           8.83        32.2         Fp1         FC2
460	hc20  hc  512.0  184.0          184.0      41            True             True    µV    104.0          2411.02           32135.753        3.33           5.45         8.8          T8          C3
461	hc21  hc  512.0  189.0          189.0      41            True             True    µV    104.0         10933.62          313871.608        4.87          11.66        39.6         Fp1         FC1
462	hc24  hc  512.0  192.0          192.0      41            True             True    µV    104.0          3702.07          108801.924        4.93           9.96        40.7         Fp2         FC1
463	hc25  hc  512.0  202.0          202.0      41            True             True    µV    104.0          6974.91           67398.438        4.29           6.67  
[... 435 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 899,
 "limit": 500
}
```

```
899	    print(t.round(4).to_string(index=False), "\n")
900	print("Paper bound: p < 0.004 FDR corrected for each measure.")
901	--- out:
902	                 test  n    W      p  p_exact  off>on      d  mean_off  mean_on  p_fdr3
903	          bipolar ShR 15 15.0 0.0106   0.0084      13 0.5508    0.0375   0.0268  0.0106
904	          bipolar StR 15  4.0 0.0015   0.0004      13 0.8939    0.0857   0.0469  0.0044
905	bipolar PAC (methods) 15 12.0 0.0064   0.0043      12 0.7470    0.0240   0.0150  0.0096 
906	
907	              test  n    W      p  p_exact  off>on      d  mean_off  mean_on  p_fdr3
908	       bipolar ShR 15 15.0 0.0106   0.0084      13 0.5508    0.0375   0.0268  0.0106
909	       bipolar StR 15  4.0 0.0015   0.0004      13 0.8939    0.0857   0.0469  0.0044
910	bipolar PAC (code) 15 11.0 0.0054   0.0034      13 0.7402    0.0236   0.0147  0.0081 
911	
912	Paper bound: p < 0.004 FDR corrected for each measure.
913	
914	===== CELL 26 [markdown]
915	**Result: reproduced.** With the bipolar pairs all three measures are higher off than on (13,
916	13 and 12 or 13 of 15 patients), and all three FDR corrected p-values are below 0.05 under
917	both PAC filter readings (largest 0.0106). None is below the paper's bound of 0.004 after
918	correction (steepness 0.0044, sharpness 0.0106, PAC 0.0096 or 0.0081); uncorrected, only
[... 480 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1399,
 "limit": 520
}
```

```
1399	    adj[m + " over 6"] = ws.p_adjust(t2m.p.values, m)
1400	alpha3 = t2m.test.str.startswith("alpha").values
1401	adj["bh over the 3 alpha tests"] = np.full(len(t2m), np.nan)
1402	adj["bh over the 3 alpha tests"][alpha3] = ws.fdr_bh(t2m.p.values[alpha3])
1403	print(pd.DataFrame(adj, index=t2m.test).round(4).to_string())
1404	
1405	--- out:
1406	                                           z       p       d  p_fdr_min  p_fdr_max
1407	test      alpha_shape_taps alpha_pac                                              
1408	alpha PAC 118              a192       1.8974  0.0578  0.5785     0.1156     0.1156
1409	                           b231       1.7788  0.0753  0.6440     0.1506     0.1506
1410	                           c118       1.2649  0.2059  0.4185     0.4118     0.4118
1411	          192              a192       1.8974  0.0578  0.5785     0.1156     0.1156
1412	                           b231       1.7788  0.0753  0.6440     0.1506     0.1506
1413	                           c118       1.2649  0.2059  0.4185     0.4118     0.4118
1414	alpha ShR 118              a192       0.3558  0.7220  0.1411     0.7220     0.7220
1415	                           b231       0.3558  0.7220  0.1411     0.7220     0.7220
1416	                           c118       0.3558  0.7220  0.1411     0.7220     0.7220
1417	          192              a192       0.7115  0.4768  0.1866     0.5721     0.5721
1418	                           b231       0.7115  0.4768  0.1866     0.5721     0.5721
[... 494 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 25,200p README.md; grep -n "def fdr_bh\|def p_adjust\|def signed_rank\|def rank_sum\|def cohen_d" waveshape.py
```

```
| Sensorimotor waveforms mostly in Q4, in patients and in controls | Reproduced |
| Q4 patient counts | Not reproduced (13 patients against 9) |
| F7/F8 waveform shape more variable | Reproduced |
| Effect sizes rise in Q4 patients | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/openneuro-ds002778-jackson-2019-01.yaml`](../../attempts/openneuro-ds002778-jackson-2019-01.yaml).

- `reproduce_jackson_2019.ipynb`: the analysis. It takes about two minutes, most of it reading the
  46 BDF files (0.57 GB) into memory.
- `waveshape.py`: listing and reading the pinned snapshot, the preprocessing, sharpness and
  steepness ratios, peak-to-trough and rise-to-fall ratios, PAC, the CSD transform and the
  statistics, with where each parameter comes from. Other notebooks on this dataset can import it.
371:def signed_rank(a, b, method: str = "approx"):
385:def rank_sum(a, b):
390:def cohen_d(m1, m2) -> float:
396:def fdr_bh(p) -> np.ndarray:
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import numpy as np
from scipy import stats
subs="pd3 pd5 pd6 pd9 pd11 pd12 pd13 pd14 pd16 pd17 pd19 pd22 pd23 pd26 pd28".split()
d={'shr':("0.0545  0.0363  0.0659  0.0159  0.0473  0.0418  0.0257  0.0735  0.0325  0.0473  0.0293  0.0496  0.0489  0.0258  0.0202","0.0087  0.0612  0.0603  0.0041  0.0154  0.0152  0.0135  0.0593  0.0243  0.0526  0.0193  0.0161  0.0302  0.0224  0.0076"),
'str':("0.0810  0.0639  0.1417  0.0454  0.1755  0.0194  0.0941  0.1100  0.0707  0.1422  0.1068  0.0240  0.1290  0.0744  0.0281","0.0108  0.0046  0.0560  0.0059  0.0487  0.0056  0.0468  0.1064  0.1227  0.1336  0.0703  0.0293  0.0943  0.0794  0.0069"),
'pac':("0.0297  0.0127  0.0587  0.0013  0.0398  0.0183  0.0357  0.0350  0.0221  0.0456  0.0154  0.0192  0.0339  0.0196  0.0154","0.0062  0.0283  0.0237  0.0036  0.0098  0.0055  0.0128  0.0340  0.0053  0.0443  0.0111  0.0095  0.0126  0.0189  0.0042")}
def cd(a,b): return (a.mean()-b.mean())/np.sqrt((a.var(ddof=1)+b.var(ddof=1))/2)
V={k:(np.array(v[0].split(),float),np.array(v[1].split(),float)) for k,v in d.items()}
keep=np.array([s not in("pd6","pd16") for s in subs])
for k,(o,n) in V.items():
    r=stats.wilcoxon(o[keep],n[keep],method="approx",correction=False); print(k,r.statistic,round(r.pvalue,4),round(cd(o[keep],n[keep]),3))
for k in['shr','str']:
    for i,s in enumerate(['off','on']):
        print(k,s,stats.spearmanr(V[k][i],V['pac'][i]), stats.spearmanr(V[k][i][keep],V['pac'][i][keep]))
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
ls node_modules; which uv pip3 python3; python3 -c "import sys;print(sys.version)"; ls ~/.local/bin 2>/dev/null; timeout 60 pip3 install --user -q numpy scipy 2>&1 | tail -2
```

```
/opt/hostedtoolcache/Python/3.13.16/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.16/x64/bin/pip3
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python3
3.13.16 (main, Oct  1 2026, 02:37:39) [GCC 15.2.0]
[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: pip install --upgrade pip
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import numpy as np
from scipy import stats
subs="pd3 pd5 pd6 pd9 pd11 pd12 pd13 pd14 pd16 pd17 pd19 pd22 pd23 pd26 pd28".split()
d={'shr':("0.0545  0.0363  0.0659  0.0159  0.0473  0.0418  0.0257  0.0735  0.0325  0.0473  0.0293  0.0496  0.0489  0.0258  0.0202","0.0087  0.0612  0.0603  0.0041  0.0154  0.0152  0.0135  0.0593  0.0243  0.0526  0.0193  0.0161  0.0302  0.0224  0.0076"),
'str':("0.0810  0.0639  0.1417  0.0454  0.1755  0.0194  0.0941  0.1100  0.0707  0.1422  0.1068  0.0240  0.1290  0.0744  0.0281","0.0108  0.0046  0.0560  0.0059  0.0487  0.0056  0.0468  0.1064  0.1227  0.1336  0.0703  0.0293  0.0943  0.0794  0.0069"),
'pac':("0.0297  0.0127  0.0587  0.0013  0.0398  0.0183  0.0357  0.0350  0.0221  0.0456  0.0154  0.0192  0.0339  0.0196  0.0154","0.0062  0.0283  0.0237  0.0036  0.0098  0.0055  0.0128  0.0340  0.0053  0.0443  0.0111  0.0095  0.0126  0.0189  0.0042")}
def cd(a,b): return (a.mean()-b.mean())/np.sqrt((a.var(ddof=1)+b.var(ddof=1))/2)
V={k:(np.array(v[0].split(),float),np.array(v[1].split(),float)) for k,v in d.items()}
keep=np.array([s not in("pd6","pd16") for s in subs])
for k,(o,n) in V.items():
    r=stats.wilcoxon(o[keep],n[keep],method="approx",correction=False); print(k,r.statistic,round(r.pvalue,4),round(cd(o[keep],n[keep]),3))
for k in['shr','str']:
    for i,s in enumerate(['off','on']):
        a=stats.spearmanr(V[k][i],V['pac'][i]); b=stats.spearmanr(V[k][i][keep],V['pac'][i][keep])
        print(k,s,round(a[0],4),round(a[1],4),round(b[0],4),round(b[1],4))
# BH check table2
from statsmodels.stats.multitest import multipletests
EOF
python3 -c "
import numpy as np
p=np.array([0.4768,0.0143,0.0578,0.6353,0.0177,0.3230])
o=np.argsort(p);r=p[o]*6/np.arange(1,7);r=np.minimum.accumulate(r[::-1])[::-1];print(dict(zip(o,r.round(4))))"
```

```
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ModuleNotFoundError: No module named 'scipy'
{np.int64(1): np.float64(0.0531), np.int64(4): np.float64(0.0531), np.int64(2): np.float64(0.1156), np.int64(5): np.float64(0.4845), np.int64(0): np.float64(0.5722), np.int64(3): np.float64(0.6353)}
```

**Agent calls Bash**

```bash
cd  timeout 120 pip3 install --user -q scipy 2>&1 | grep -v notice | tail -2; python3 -c "import scipy;print(scipy.__version__)"
```

```
1.18.1
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import numpy as np
from scipy import stats
subs="pd3 pd5 pd6 pd9 pd11 pd12 pd13 pd14 pd16 pd17 pd19 pd22 pd23 pd26 pd28".split()
d={'shr':("0.0545  0.0363  0.0659  0.0159  0.0473  0.0418  0.0257  0.0735  0.0325  0.0473  0.0293  0.0496  0.0489  0.0258  0.0202","0.0087  0.0612  0.0603  0.0041  0.0154  0.0152  0.0135  0.0593  0.0243  0.0526  0.0193  0.0161  0.0302  0.0224  0.0076"),
'str':("0.0810  0.0639  0.1417  0.0454  0.1755  0.0194  0.0941  0.1100  0.0707  0.1422  0.1068  0.0240  0.1290  0.0744  0.0281","0.0108  0.0046  0.0560  0.0059  0.0487  0.0056  0.0468  0.1064  0.1227  0.1336  0.0703  0.0293  0.0943  0.0794  0.0069"),
'pac':("0.0297  0.0127  0.0587  0.0013  0.0398  0.0183  0.0357  0.0350  0.0221  0.0456  0.0154  0.0192  0.0339  0.0196  0.0154","0.0062  0.0283  0.0237  0.0036  0.0098  0.0055  0.0128  0.0340  0.0053  0.0443  0.0111  0.0095  0.0126  0.0189  0.0042")}
def cd(a,b): return (a.mean()-b.mean())/np.sqrt((a.var(ddof=1)+b.var(ddof=1))/2)
V={k:(np.array(v[0].split(),float),np.array(v[1].split(),float)) for k,v in d.items()}
keep=np.array([s not in("pd6","pd16") for s in subs])
for k,(o,n) in V.items():
    r=stats.wilcoxon(o[keep],n[keep],method="approx",correction=False); print(k,r.statistic,round(r.pvalue,4),round(cd(o[keep],n[keep]),3))
for k in['shr','str']:
    for i,s in enumerate(['off','on']):
        a=stats.spearmanr(V[k][i],V['pac'][i]); b=stats.spearmanr(V[k][i][keep],V['pac'][i][keep])
        print(k,s,round(a[0],4),round(a[1],4),round(b[0],4),round(b[1],4))
EOF
```

```
shr 11.0 0.0159 0.811
str 5.0 0.0046 0.752
pac 13.0 0.0231 0.732
shr off 0.5796 0.0235 0.5014 0.0809
shr on 0.7893 0.0005 0.8681 0.0001
str off 0.7882 0.0005 0.7318 0.0045
str on 0.4464 0.0953 0.6374 0.0191
```

**Agent calls Bash**

```bash
cd  grep -n "assumed" openneuro-ds002778-jackson-2019-01.yaml; grep -c "^- claim:" openneuro-ds002778-jackson-2019-01.yaml; grep -c "^- id:" 10.1523-eneuro.0151-19.2019.yaml; grep -n "  outcome:" openneuro-ds002778-jackson-2019-01.yaml | awk '{print $3}' | sort | uniq -c
```

```
24
24
     12 not_reproduced
     18 partially_reproduced
     18 reproduced
```

**Agent calls Bash**

```bash
cd paper; grep -n -i "Q4\|quadrant\|Table 3\|nine\|eight" 10.1523-eneuro.0151-19.2019.txt | head -40
```

```
24:We analyzed a previously published data set, from another laboratory (George et al., 2013). This same data were analyzed in another published report which showed elevated PAC between β phase and broadband γ amplitude in PD patients off medication compared to the same patients on medication and compared to a group of healthy, age-matched, control participants (Swann et al., 2015). This dataset includes EEG data from 15 PD patients (eight female, mean age = 63.2 ± 8.2 years) on and off dopaminergic medication and 16 healthy, age-matched, control participants (nine female, mean age = 63.5 ± 9.6 years). All PD patients had been diagnosed by a movement disorder specialist at Scripps clinic in La Jolla, California. Participants were right-handed and provided written consent in accordance to the Institutional Review Board of the University of California, San Diego and the Declaration of Helsinki. For additional patient information, see George et al. (2013).
88:Steepness and sharpness measures can be considered together to categorize waveforms into different shapes. Previous reports have shown that certain shapes may dominate for certain recording types (Cole et al., 2017). Here, we observed qualitative differences in waveform shape in sensorimotor electrodes which differed from electrodes closer to temporalis muscles (F7 and F8; Fig. 4). In general, sensorimotor electrode oscillations had a sharper peak with a steeper decay, falling in quadrant 4 (Q4) in Figure 4. In contrast, electrodes closest to temporalis muscles had a more variable waveform shape pattern, perhaps consistent with contributions from both EEG and EMG, and/or the general lack of a consistent dominant waveform pattern. Note that here, our goal was to show qualitatively the overall shape of the data, so we have included in Figure 4 data from each electrode (C3 and C4) as well as data from patients on and off; thus, dependent samples are included. Although not shown, control participant data exhibited the
[... 5 more lines not kept]
```

**Agent**

**Verification report, round 2: Jackson et al. 2019 (eNeuro 0151-19.2019) on OpenNeuro ds002778 v1.0.5**

**Counts.** The claims file has 24 claims and the attempt record gives 24 outcomes: 9 reproduced, 9 partially reproduced, 6 not reproduced, none blocked. These are the outcomes I gave in round 1.

**How I checked this round.**
- I read every printed output of the re-executed notebook (cells 0–84).
- From the printed per-patient values, I recomputed the new variants without pd6 and pd16:
  - Beta sharpness: W 11, p 0.0159, d 0.811.
  - Beta steepness: W 5, p 0.0046, d 0.752.
  - Beta PAC (Methods filters): W 13, p 0.0231, d 0.732.
  - Spearman r on/off with and without the two patients.
  - All match to rounding.
- I recomputed the BH correction for Table 2 from the printed p-values (0.0531 for both steepness tests).
- I checked the Q4 counts in the paper's text (paragraph 90): C3 9, C4 8, both 8, so 9 with at least one. The claims file reads them correctly.

### 1. Outcomes and assumptions

I agree with all 24 outcomes.

- **Three outcomes changed after round 1.** offctrl-steepness, table1-alpha-pac-null and table2-alpha-offctrl are now not_reproduced. Each follows from its criterion:
  - Both non-failing outcomes of the two Table 2 claims need the average-reference result to survive FDR correction, and it gives 0.0531 under every reading. The correction-procedure table (cells 39 and 59) shows Holm, Bonferroni and BY are further from 0.05.
  - The alpha PAC readings disagree (a192 0.0609, b231 0.0783, c118 0.0356; cell 56). The criterion takes the outcome that all readings give.
- **Outcomes that rest on a judgement:**
  - fig2-pac-off-on applies the stricter reading of a criterion that contradicts itself. The record says so and puts the question to a reader.
  - pac-beta-larger-than-alpha is marked partially reproduced, but its criterion has no partial clause. Partial is a reasonable default (test holds, W 17–18 against 9.9–12.1), but the claims file does not define it.
- **Assumptions.** No outcome carries `assumed: true`; the earlier assumption of a 192-tap alpha filter was removed. The judgements the outcomes rest on are all stated, as notes or deviations:
  - no artifact rejection;
  - CSD computed with MNE on template positions;
  - "Total UPDRS" read as Part III;
  - the stricter fig2-pac reading.

  All are reasonable. The CSD one is the least tested (see section 3).

### 2. Sentences the numbers do not support

1. **Cell 84 (Summary), and the end of "What was found about the dataset":** "Without artifact rejection the main off against on results hold, with statistics close to the paper's."
   - Steepness W is 16 against the paper's 9 (cell 19), and sharpness d is 0.73 against 0.86 (cell 16).
   - Two of the three main claims have a value out of tolerance, so "close" overstates the match.
2. **Cell 84 (Summary):** "It holds the 15 patients … and 16 controls …, each recording once." Patients were recorded twice, off and on (cell 4). The sentence probably means no recording is duplicated (cell 10), but as written it is wrong.
3. **Cell 84 (Sensitivity):** "Without sub-pd6 and sub-pd16 … the off against on tests keep their direction and significance."
   - The exclusion is printed only for the three beta tests at C3/C4 (uncorrected) and for alpha PAC.
   - Alpha shape, bipolar and FDR-corrected values without the two patients are not shown.
   - Under reading c, alpha PAC is significant after correction (0.0356) but has uncorrected p 0.064 without the two patients (cell 56), so not every test keeps its significance.
   - "Dropping the filtered edges … changes no test" is likewise shown only for the beta off-against-on test at C3/C4 (cell 22).
4. **Cell 34 and the fig2c record notes:** "with the code's filters the smallest p is at Fz (0.020)". Cell 33 prints Fz and CP6 tied at 0.0199, and CP6 is in the sensorimotor set. The outcome does not change, since sharpness fails either way.
5. **Cell 74:** "points that decide membership (pd12, pd22, pd26, pd28, pd3 and pd9 on medication)".
   - pd9's C4 off point is in Q1 (0.027, 0.075), far from any axis. Its C3 points would have to cross both axes. So pd9's near-axis points do not decide its membership.
   - pd5 (C3 on, RDR −0.0023; C4 on, RDR 0.0070) and pd11 (C4 on) do decide membership and are not listed.
6. **Minor:**
   - Cell 23 and the record say edge-dropping "changes PAC by 5% at most". Cell 22 prints a ratio of 0.9487, which is 5.1%.
   - Cell 45 says CSD PAC is "higher off under every variant". The variant rows print p only, so the direction is shown for the main m = 3 CSD only.
   - Summary row for table3 says "two values above tolerance". That holds under log10 PAC with the Methods' filters. Under raw PAC, the all-patient PAC d (0.85, above 0.825) is a third.

The other "**Result:" cells, the README rows and the record notes match the printed outputs.

**Round-1 reasons in the record.** The record states my round-1 reasons in my words, and accurately. Problems 4, 6 and 7 and the Section C items are attached to the claims they concern. Problems 5 (pd6/pd16) and 8 (artifact rejection) are not quoted as reasons. Neither bore on an outcome, and the record answers both: problem 8 in the deviations and findings, problem 5 in the exclusion variants and the findings.

### 3. Round-1 points

**Resolved:**
- **2:** alpha PAC reading disagreement. The outcome was changed and the notebook now prints that the readings disagree.
- **3:** the Q4 subset is now stated as 13 patients against the paper's 9, with the patients listed.
- **4:** cell 12 now says 1 to 14.
- **5:** exclusion variants now cover PAC, the correlations, Q4 and Table 3. They show that the steepness–PAC on-medication miss rests on pd6 and pd16.
- **6:** edge-dropping changes PAC by at most 5.1% per recording and leaves W unchanged.
- **Section C, Table 2 FDR sensitivity:** the misses are not an artefact of BH.
- **Section C, Q4 per-patient values:** now printed.

**Still open and bearing on a conclusion:**
- **Problem 1, fig2-pac-off-on.** The criterion still contradicts itself. The outcome is partially reproduced or reproduced depending on which sentence governs, and it now waits on a reader.
- **Problem 7, offctrl-pac-csd.** The spline variants all miss (p 0.105–0.30), but MNE has not been compared with the CSD toolbox. CSD roughly doubles the ratio of 50–150 Hz power to beta power at C3/C4. That raises gamma, which the PAC amplitude uses, and the toolbox's output may behave differently.
- **Problem 8, artifact rejection.** It cannot be done with this dataset. It remains the likely cause of the out-of-tolerance W and d values and of the Q4 count gap: 16 of 60 points lie within 0.01 of an axis.
- **pac-beta-larger-than-alpha.** The criterion has no partial clause, so the claims file should define it.

**Still open, not bearing on a conclusion:** the summary and cell wording in section 2, items 1–6. Item 1 matters most, because the summary states a better match to the paper than the outputs show.

## End of run

19 turns, 3 minutes, result: success.
