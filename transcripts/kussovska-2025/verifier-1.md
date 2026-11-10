# kussovska-2025 · verifier-1 · run 42787671158

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 532
drwxr-xr-x 6 runner runner    4096 Nov 10 09:30 .
drwxr-xr-x 7 runner runner    4096 Nov 10 09:30 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 09:04 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 09:04 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 10 09:30 .claude
-rw-r--r-- 1 runner runner       0 Nov 10 09:30 .env
-rw-r--r-- 1 runner runner       0 Nov 10 09:30 .env.development
-rw-r--r-- 1 runner runner       0 Nov 10 09:30 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 10 09:30 .env.local
-rw-r--r-- 1 runner runner       0 Nov 10 09:30 .env.production
-rw-r--r-- 1 runner runner       0 Nov 10 09:30 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 10 09:30 .env.test
-rw-r--r-- 1 runner runner       0 Nov 10 09:30 .env.test.local
drwx------ 2 runner runner    4096 Nov 10 09:30 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 09:04 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 09:04 .github
-rw-r--r-- 1 runner runner       0 Nov 10 09:30 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 09:04 .idea
[... 36 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "kussovska-2025.yaml"
}
```

```
1	# Claims for Kussovska, Kim & Rungratsameetaweemana (2025), "Neural heterogeneity shapes the
2	# temporal structure of human working memory", bioRxiv, doi:10.1101/2025.10.31.684900, tested on
3	# DANDI:000469 (reused; the paper analyses the dataset of Kyzar et al. 2024, ref. 59).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5	# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
6	#
7	# Text read. paper/10.1101-2025.10.31.684900.txt, the bioRxiv full-text page of the preprint
8	# posted 1 November 2025 (its header says "version of record"; the page says "New Results" and
9	# offers a "current version", so a later version may exist; it was not read). It holds the
10	# abstract, Introduction, Results, legends of Figures 1 to 6, Discussion, Methods, Data and Code
11	# availability and references. No PDF was supplied. The Extended Data figures (Extended Data
12	# Figs 1 to 5, behind "Supplementary Material") and their legends are not in the text read; the
13	# Source Data are not either. The main findings are all stated in the main text and legends, so
14	# claims were written; claims on Extended Data panels rest on the main-text sentences that cite
15	# them, and their sources say "(not in the text read)". Several equations of the Methods (the GLM
16	# link, the local-peak and prominence formulas of Burst detection) were lost in extraction.
17	#
18	# Code read. github.com/dariakussovska/heterogeneitywm at commit 5144fe8 (2025-10-26), the last
19	# commit before the preprint was posted. Later commits (REVISIONS/ and R2_REVISIONS/, 2026) are
20	# for a revised version and were not used. The repository holds Python scripts named by figure
[... 925 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "kussovska-2025.yaml",
 "offset": 946,
 "limit": 500
}
```

```
946	    and larger τrise (U = 13465, P = 2.58 × 10−9; Fig. 5f).
947	  statistics:
948	  - about: firing rate
949	    test: Mann-Whitney U (Wilcoxon rank-sum)
950	    statistic: U = 17294
951	    p: 1.42e-32
952	  - about: normalised mean ACG amplitude
953	    test: Mann-Whitney U (Wilcoxon rank-sum)
954	    statistic: U = 18522
955	    p: 2.16e-41
956	  - about: tau_rise
957	    test: Mann-Whitney U (Wilcoxon rank-sum)
958	    statistic: U = 13465
959	    p: 2.58e-9
960	  depends_on:
961	  - fig5c-cell-type-clusters
962	  criterion: Two-sided Mann-Whitney U tests of IN against PY on each feature, with Benjamini-Yekutieli
963	    FDR over the five metrics of Fig. 5d-h as in 05_cell_analysis/main_5d-h.py:49-63. Reproduced
964	    when IN is higher on all three with corrected p < 0.05. The features are those the clusters
965	    were formed on, so the claim follows from fig5c-cell-type-clusters by construction; the
[... 479 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" kussovska-2025.yaml; python3 - <<'EOF'
import json
nb=json.load(open('reproduce_kussovska_2025.ipynb'))
print(len(nb['cells']))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"===== [{i}] {c['cell_type']} =====")
    print(src[:3000])
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            t=o.get('text') or o.get('data',{}).get('text/plain','')
            t=''.join(t) if isinstance(t,list) else t
            print('--- out:'); print(t[:4000])
EOF
```

```
<persisted-output>
Output too large (178.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/2cba135d-9a90-48f3-8a90-6a60c8d80513/tool-results/b98mv5t8o.txt

Preview (first 2KB):
45
107
===== [0] markdown =====
# Reproducing Kussovska, Kim and Rungratsameetaweemana (2025) from dandiset 000469

Paper. Kussovska D, Kim R, Rungratsameetaweemana N (2025). Neural heterogeneity shapes the
temporal structure of human working memory. bioRxiv,
[doi:10.1101/2025.10.31.684900](https://doi.org/10.1101/2025.10.31.684900). The claims file
(`claims/kussovska-2025.yaml`) was written from the bioRxiv full text posted on 1 November 2025
(main text, figure legends and Methods; the Extended Data figures and their legends were not in
the text read).

Dandiset. [DANDI:000469](https://dandiarchive.org/dandiset/000469/0.231213.2047), version
0.231213.2047 (Kyzar et al. 2024, human single neurons during a Sternberg working memory task).
This is the version the paper cites (Methods, Participants and data source, and Data
availability). The four published versions (0.231213.2047, 0.240122.1800, 0.240122.1812,
[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/2cba135d-9a90-48f3-8a90-6a60c8d80513/tool-results/b98mv5t8o.txt",
 "limit": 700
}
```

```
1	45
2	107
3	===== [0] markdown =====
4	# Reproducing Kussovska, Kim and Rungratsameetaweemana (2025) from dandiset 000469
5	
6	Paper. Kussovska D, Kim R, Rungratsameetaweemana N (2025). Neural heterogeneity shapes the
7	temporal structure of human working memory. bioRxiv,
8	[doi:10.1101/2025.10.31.684900](https://doi.org/10.1101/2025.10.31.684900). The claims file
9	(`claims/kussovska-2025.yaml`) was written from the bioRxiv full text posted on 1 November 2025
10	(main text, figure legends and Methods; the Extended Data figures and their legends were not in
11	the text read).
12	
13	Dandiset. [DANDI:000469](https://dandiarchive.org/dandiset/000469/0.231213.2047), version
14	0.231213.2047 (Kyzar et al. 2024, human single neurons during a Sternberg working memory task).
15	This is the version the paper cites (Methods, Participants and data source, and Data
16	availability). The four published versions (0.231213.2047, 0.240122.1800, 0.240122.1812,
17	0.240123.1806) hold the same 41 assets with the same asset identifiers and sizes, which the data
18	check below confirms, so the version the paper's code downloads (0.240123.1806) gives the same
19	data.
20	
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/2cba135d-9a90-48f3-8a90-6a60c8d80513/tool-results/b98mv5t8o.txt",
 "offset": 700,
 "limit": 700
}
```

```
700	preSMA 250           40   16.000      12.50 0.000 0.000
701	 vmPFC  32            2    6.250       1.60 0.464 0.464
702	
703	each trial's own RT; trials all, permutation within:
704	 group   n  significant  percent  null_mean     p  p_BH
705	   AMY 259           28   10.811      12.95 0.000 0.000
706	   HPC 190           18    9.474       9.50 0.017 0.021
707	  dACC 171           21   12.281       8.55 0.001 0.002
708	preSMA 250           35   14.000      12.50 0.000 0.000
709	 vmPFC  32            2    6.250       1.60 0.450 0.450
710	
711	variant, subject 1's RT vector (the code); trials matched, permutation shared:
712	 group   n  significant  percent  null_mean     p  p_BH
713	   AMY 259           15    5.792      12.95 0.326 0.699
714	   HPC 190            4    2.105       9.50 0.966 0.966
715	  dACC 171            8    4.678       8.55 0.559 0.699
716	preSMA 250           20    8.000      12.50 0.080 0.400
717	 vmPFC  32            2    6.250       1.60 0.463 0.699
718	
719	variant, subject 1's RT vector (the code); trials matched, permutation within:
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/2cba135d-9a90-48f3-8a90-6a60c8d80513/tool-results/b98mv5t8o.txt",
 "offset": 1399,
 "limit": 700
}
```

```
1399	--- out:
1400	trial reading code:
1401	    pair_ms  diff_%    p_a    p_b  p_a_BH  p_b_BH
1402	 750 vs 250   36.67 0.0020 0.0010  0.0060  0.0020
1403	1000 vs 250   46.67 0.0010 0.0010  0.0060  0.0020
1404	1000 vs 500   16.67 0.0529 0.0929  0.0794  0.1394
1405	 500 vs 250   30.00 0.0050 0.0010  0.0100  0.0020
1406	1000 vs 750   10.00 0.2547 0.3027  0.3057  0.3632
1407	 750 vs 500    6.67 0.4975 0.4805  0.4975  0.4805
1408	trial reading rank:
1409	    pair_ms  diff_%    p_a    p_b  p_a_BH  p_b_BH
1410	 750 vs 250   23.33 0.0150 0.0160  0.0450  0.0480
1411	1000 vs 250   26.67 0.0090 0.0060  0.0450  0.0360
1412	1000 vs 500   10.00 0.2418 0.3217  0.3626  0.4825
1413	 500 vs 250   16.67 0.0689 0.0709  0.1379  0.1419
1414	1000 vs 750    3.33 1.0000 0.7193  1.0000  0.7193
1415	 750 vs 500    6.67 0.4785 0.4935  0.5742  0.5922
1416	paper: 750 vs 250 P = 0.026, 1000 vs 250 P = 0.004, 1000 vs 500 P = 0.032; the other three P > 0.05
1417	
1418	===== [52] markdown =====
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/2cba135d-9a90-48f3-8a90-6a60c8d80513/tool-results/b98mv5t8o.txt",
 "offset": 2098,
 "limit": 900
}
```

```
File content (26626 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/2cba135d-9a90-48f3-8a90-6a60c8d80513/tool-results/b98mv5t8o.txt",
 "offset": 2098,
 "limit": 450
}
```

```
2098	
2099	
2100	for g in ["All902", "AllFit"]:
2101	    print(f"\n{g}, load 1 (medians are bursts per window; q is BH over the 10 pairs):")
2102	    print(epoch_table(g, 1).to_string(index=False))
2103	x = EPB[(EPB.group == "All902") & (EPB.load == 1) & (EPB.mread == "methods")]
2104	dur = np.mean([T[s][T[s].load == 1].maint_dur.mean() for s in x["sub"].unique()]) - 2.0
2105	print(f"\nM3 under reading (a) lasts {dur:.2f} s on average; its median rate per second, all neurons, prominence: "
2106	      f"{(x[(x.grule == 'code') & (x.rule == 'prominence')].M3 / dur).median():.1f} against M1 {x[(x.grule == 'code') & (x.rule == 'prominence')].M1.median():.1f}")
2107	--- out:
2108	
2109	All902, load 1 (medians are bursts per window; q is BH over the 10 pairs):
2110	                     reading  n  med_enc  med_M1  med_M2  med_M3  med_probe   q_M1   q_M2   q_M3  q_probe  min_q_other  q_M1-M2  q_M1-M3
2111	          code/height/M-code 20     41.5    42.0    38.5    37.0       41.0 0.4377 0.6169 0.4377   0.6429       0.3632   0.4916   0.3632
2112	       code/height/M-methods 20     41.5    46.5    44.5    28.0       41.0 0.0024 0.0038 0.0003   0.7117       0.0003   0.8089   0.0003
2113	      code/prominence/M-code 20      6.0    14.0    14.0    15.0        5.5 0.0003 0.0003 0.0003   0.6800       0.0003   0.8103   0.2073
2114	   code/prominence/M-methods 20      6.0    17.0    14.0    11.5        5.5 0.0003 0.0003 0.0352   0.6120       0.0003   0.0551   0.0003
2115	       methods/height/M-code 20     41.5    42.0    38.5    37.0       41.0 0.4377 0.6169 0.4377   0.6429       0.3632   0.4916   0.3632
2116	    methods/height/M-methods 20     41.5    46.5    44.5    28.0       41.0 0.0024 0.0038 0.0003   0.7117       0.0003   0.8089   0.0003
2117	   methods/prominence/M-code 20      6.0    14.0    14.0    15.0        5.5 0.0003 0.0003 0.0003   0.6800       0.0003   0.8103   0.2073
[... 430 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/2cba135d-9a90-48f3-8a90-6a60c8d80513/tool-results/b98mv5t8o.txt",
 "offset": 2548,
 "limit": 400
}
```

```
2548	load, trials matched, permutation shared:
2549	     group   n  significant  percent  null_mean     p
2550	        IN 215           30   13.953     10.839 0.001
2551	IN concept  16            3   18.750      0.806 0.042
2552	        PY 102            6    5.882      5.226 0.426
2553	PY concept  11            0    0.000      0.561 1.000
2554	load, trials matched, permutation within:
2555	     group   n  significant  percent  null_mean     p
2556	        IN 215           28   13.023     10.832 0.000
2557	IN concept  16            3   18.750      0.808 0.045
2558	        PY 102            6    5.882      5.226 0.423
2559	PY concept  11            0    0.000      0.558 1.000
2560	load, trials all, permutation within:
2561	     group   n  significant  percent  null_mean     p
2562	        IN 215           37   17.209     10.814 0.000
2563	IN concept  16            4   25.000      0.805 0.006
2564	        PY 102            8    7.843      5.204 0.157
2565	PY concept  11            0    0.000      0.562 1.000
2566	variant, types of reading (b), matched trials, shared permutation:
2567	     group   n  significant  percent  null_mean     p
[... 314 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('reproduce_kussovska_2025.ipynb'))
for i in [34,40,42]:
    c=nb['cells'][i]
    print(f"===== [{i}] =====")
    if i==40: print(''.join(c['source'])[2900:])
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain','')
        t=''.join(t) if isinstance(t,list) else t
        print(t[3500:] if i==34 else t)
EOF
```

```
===== [34] =====
      9              0.58  True  True  True          True          True
 599   14    AMY            9              0.70  True  True  True          True          True
 601   14    AMY            9              0.42  True False False         False         False
 602   14    AMY            9              0.08 False False False         False         False
 606   14    AMY            9              0.18 False False False         False         False
 609   14    AMY            9              0.10 False False False         False         False
 616   14    HPC            9              0.66  True  True  True          True          True
 618   14    HPC            9              0.20  True False False         False         False
 620   14    HPC            9              0.14  True False False         False         False
 677   15    HPC            9              0.02 False False False         False         False
 702   16    AMY            7              0.30  True  True  True         False          True
 709   16    AMY            7              0.10 False False False         False         False
 715   16    AMY            7              0.00 False False False         False         False
 717   16    AMY            7              0.26  True  True  True         False          True
 732   16    HPC            7              0.00 False False False         False         False
 767   18    AMY            9              0.10 False  True False         False         False
 773   18    AMY            9              0.02 False False False         False         False
 781   18    AMY            9              0.32  True  True False         False         False
 783   18    AMY            9              0.40  True  True  True         False          True
[... 85 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "wm.py"
}
```

```
1	"""Loading and shared measures for DANDI:000469 (Kyzar et al. 2024), as used by Kussovska, Kim and
2	Rungratsameetaweemana (2025), "Neural heterogeneity shapes the temporal structure of human working
3	memory" (bioRxiv doi:10.1101/2025.10.31.684900).
4	
5	The data are streamed from the archive at a pinned version (DANDISET_VERSION, the version the paper
6	cites in Methods, Participants and data source). Only the Sternberg file of each subject is read
7	(sub-<n>_ses-2), as the paper's code does (01_data_extraction.py:417 of
8	github.com/dariakussovska/heterogeneitywm at commit 5144fe8); only the spike times, the electrode
9	locations and the trials table are read, not the waveforms or the stimulus images.
10	"""
11	from concurrent.futures import ThreadPoolExecutor
12	
13	import h5py
14	import numpy as np
15	import pandas as pd
16	import remfile
17	import requests
18	
19	DANDISET_ID = "000469"
20	DANDISET_VERSION = "0.231213.2047"
[... 689 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('reproduce_kussovska_2025.ipynb'))
for i in [67,70,84,86]:
    c=nb['cells'][i]
    print(f"===== [{i}] =====")
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain','')
        t=''.join(t) if isinstance(t,list) else t
        print(t[3800:] if i in (67,70) else t[3500:])
EOF
```

```
===== [67] =====

11  3.0 0.0047 0.0126
    code/prominence/d2/own    HighACG 12         11.5         10.0           9 23.0 0.2094 0.2094
    code/prominence/d2/own ShortDecay 12         19.0         17.1          10  8.0 0.0150 0.0240
    code/prominence/d2/own  LongDecay 12         15.5         13.6           7 23.0 0.2094 0.2094
    code/prominence/d2/own    Concept  9         27.0         21.6           7  3.0 0.0209 0.0278
    code/prominence/d2/own         PY 12         29.0         23.3          11  1.0 0.0029 0.0115
    code/prominence/d2/own         IN 19         11.0          7.6          15 28.0 0.0070 0.0140
    code/prominence/d2/own     AllFit 12          6.5          3.5          10  6.0 0.0096    NaN
   code/prominence/d2/real     All902 20          6.0          2.9          18  9.0 0.0003 0.0027
   code/prominence/d2/real     LowACG 12         29.0         24.4          10  4.0 0.0060 0.0161
   code/prominence/d2/real    HighACG 12         11.5          9.4           8 27.0 0.3465 0.3465
   code/prominence/d2/real ShortDecay 12         19.0         18.5          10 13.0 0.0414 0.0552
   code/prominence/d2/real  LongDecay 12         15.5         12.9           8 22.0 0.1823 0.2084
   code/prominence/d2/real    Concept  9         27.0         24.6           8  4.0 0.0284 0.0454
   code/prominence/d2/real         PY 12         29.0         19.7          12  0.0 0.0022 0.0089
   code/prominence/d2/real         IN 19         11.0          7.2          14 31.0 0.0100 0.0200
   code/prominence/d2/real     AllFit 12          6.5          3.1          10  6.0 0.0096    NaN
    methods/height/d1/real     All902 20         41.5         33.4          16 14.0 0.0007 0.0054
[... 172 more lines not kept]
```

**Agent calls Bash**

```bash
cd  timeout 600 python3 - <<'EOF'
import numpy as np, wm
rng=np.random.default_rng(0)
# count_in
s=np.array([0.1,0.2,0.5,1.0,1.5])
print("count_in", wm.count_in(s,np.array([0,0.5]),np.array([0.5,1.5])))
# concept_test false-positive rate under null
for reading in ["methods","code"]:
    fp=0
    for k in range(300):
        imgs=np.repeat(np.arange(1,6),27)
        r=rng.poisson(5,len(imgs))/0.8
        fp+=wm.concept_test(r,imgs,rng,reading=reading)[2]
    print(reading,"null FP rate",fp/300)
# glm_groups null calibration
n=200; Y=[rng.poisson(3,96) for _ in range(n)]; x=np.repeat([1,2,3],32).astype(float)
P=[np.array([rng.permutation(96) for _ in range(200)])]*n
real,null=wm.glm_fit(Y,[x]*n,P)
df,_=wm.glm_groups(real,null,{"all":np.arange(n)})
print(df)
# epoch_burst_counts methods mapping: one burst at 0.5s in each 3s trial
tr=[[np.r_[np.full(30,0.5)+rng.normal(0,0.005,30), rng.uniform(0,2.5,5)]] for _ in range(20)]
nt=[[t[0] for t in tr]]
c=wm.epoch_burst_counts({"enc":nt,"probe":nt,"maint":nt},"prominence",2,"methods")
print(c)
c=wm.epoch_burst_counts({"enc":nt,"probe":nt,"maint":nt},"prominence",2,"code")
print(c)
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
ls /usr/bin/python3* /usr/local/bin/python* 2>/dev/null; which -a python python3 conda mamba uv pip 2>/dev/null; ls ~/.local/bin ~/miniconda3/bin ~/venv 2>/dev/null | head
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
/opt/hostedtoolcache/Python/3.13.18/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.18/x64/bin/pip
/usr/bin/pip
/bin/pip
/home/runner/.local/bin:
```

**Agent calls Bash**

```bash
for p in /opt/hostedtoolcache/Python/3.13.18/x64/bin/python /usr/bin/python3.14; do $p -c "import numpy, scipy, pandas, statsmodels; print('$p ok')" 2>&1 | tail -1; done
```

```
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd $TMPDIR && /opt/hostedtoolcache/Python/3.13.18/x64/bin/uv venv -q v && ./v/bin/python -m ensurepip -q 2>/dev/null; /opt/hostedtoolcache/Python/3.13.18/x64/bin/uv pip install -q --python ./v/bin/python numpy scipy pandas statsmodels h5py remfile requests 2>&1 | tail -3; ./v/bin/python -c "import numpy, scipy, statsmodels; print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  timeout 900 $TMPDIR/v/bin/python - <<'EOF'
import numpy as np, wm
rng=np.random.default_rng(0)
s=np.array([0.1,0.2,0.5,1.0,1.5])
print("count_in", wm.count_in(s,np.array([0,0.5]),np.array([0.5,1.5])))
for reading in ["methods","code"]:
    fp=0
    for k in range(400):
        imgs=np.repeat(np.arange(1,6),27)
        r=rng.poisson(5,len(imgs))/0.8
        fp+=wm.concept_test(r,imgs,rng,reading=reading)[2]
    print(reading,"null FP rate",fp/400)
n=200; Y=[rng.poisson(3,96) for _ in range(n)]; x=np.repeat([1,2,3],32).astype(float)
P=[np.array([rng.permutation(96) for _ in range(200)])]*n
real,null=wm.glm_fit(Y,[x]*n,P)
df,_=wm.glm_groups(real,null,{"all":np.arange(n)})
print(df)
tr=[np.sort(np.r_[0.5+rng.normal(0,0.005,30), rng.uniform(0,2.5,5)]) for _ in range(20)]
nt=[tr]
print("methods", wm.epoch_burst_counts({"enc":nt,"probe":nt,"maint":nt},"prominence",2,"methods"))
print("code", wm.epoch_burst_counts({"enc":nt,"probe":nt,"maint":nt},"prominence",2,"code"))
# burst null calibration with gap: Poisson spikes on [0,2.5] in a 2.8 window
G=[[np.sort(rng.uniform(0,2.5,rng.poisson(5))) for _ in range(45)] for _ in range(10)]
G2=[[np.sort(rng.uniform(0,2.8,rng.poisson(5))) for _ in range(45)] for _ in range(10)]
for name,g in [("gap 2.5 in 2.8",G),("no gap",G2)]:
    r=[wm.group_bursts(g,2.8,np.random.default_rng(i),"prominence",2,"real",50)[:2] for i in range(5)]
    print(name, r)
EOF
```

```
count_in [2 2]
methods null FP rate 0.005
code null FP rate 0.0125
  group    n  significant  percent  null_mean      p
0   all  200            7      3.5      10.18  0.905
methods {'enc': 13, 'probe': 13, 'M1': 22, 'M2': 2, 'M3': 4}
code {'enc': 13, 'probe': 13, 'M1': 11, 'M2': 9, 'M3': 8}
gap 2.5 in 2.8 [(54, 41.34), (54, 40.08), (54, 40.86), (54, 40.92), (54, 40.28)]
no gap [(40, 45.42), (40, 43.8), (40, 43.9), (40, 45.46), (40, 45.42)]
```

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000469/versions/0.231213.2047/info/" | head -c 1500; echo; curl -s "https://api.dandiarchive.org/api/dandisets/000469/versions/0.231213.2047/assets/?page_size=100" | $TMPDIR/v/bin/python -c "import json,sys; r=json.load(sys.stdin); print(r['count']); print([a['path'] for a in r['results'] if 'sub-14' in a['path']])"
```

Result: the fetched text is not kept.

**Agent calls Grep**

```json
{
 "pattern": "chance|label-shuffled|TRIAL_WIN|probe period",
 "path": "paper/10.1101-2025.10.31.684900.txt",
 "output_mode": "content"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF'
import re
t=open('paper/10.1101-2025.10.31.684900.txt').read()
for kw in ["chance","label-shuffled","probe window","1 s window","Burst detection"]:
    for m in re.finditer(kw,t):
        print(kw,"::",t[max(0,m.start()-250):m.start()+250].replace("\n"," "))
        print('---')
EOF
```

Result: not kept, because it reads the paper's text.

**Agent**

**Verifier report, round 1: Kussovska et al. 2025 on DANDI:000469 (0.231213.2047)**

The claims file has 45 claims; all appear below. I queried the archive: the pinned version is valid, with 41 assets including 21 Sternberg `ses-2` files. It holds every input the three dPCA claims need (spike times and trial tables), and the notebook streamed those in 14 s.

### A. Outcomes

| claim id | outcome | reason |
|---|---|---|
| units-by-region | reproduced | 902 units from 21 patients; AMY 259, HPC 190, dACC 171, preSMA 250, vmPFC 32, all exact (cell 16). |
| behavior-accuracy | reproduced | 88.73% ± 1.25 (s.e.m.), exact (cell 18). |
| fig1c-accuracy-load1-vs-load3 | reproduced | Load 1 median 94.4% against 86.7% at load 3. Rank-sum raw p = 0.009, Bonferroni p = 0.027, which equals the paper (cell 20). |
| behavior-rt | reproduced | (a) 1.120 s (s.d. 0.252); (c) 1.097 s. Both are inside 0.78–1.34 (cell 22). |
| rt-in-vs-out-memory | reproduced | In-memory probes faster; p = 0.001–0.002 under all four readings (cell 24). |
| rt-correct-vs-incorrect | reproduced | Correct trials faster in 20 of 21 participants; p = 0.001 under both readings (cell 26). |
| fig1e-load-modulated-neurons | reproduced | Matched trials, shared permutation: preSMA 20.4%, vmPFC 18.75%, dACC 10.53%. All within tolerance, p = 0.000 / 0.009 / 0.025 (cell 28). |
| fig1f-rt-modulation-not-significant | not_reproduced | With each trial's own RT (the main reading), preSMA, AMY and dACC have BH p < 0.05 under every trial reading (cell 30). The paper's numbers (AMY 5.79%, preSMA 8.00%, vmPFC 6.25%, none significant) come out exactly only under the code's bug, which uses subject 1's RT vector for every neuron. |
| concept-cells-count | reproduced | Code reading gives 57–60 cells over seeds, with AMY 70.7% and HPC 19.0%. The Methods reading gives 49–54. Per participant 4.14 ± 3.66 (cell 32). |
| fig2ab-single-cells-not-persistent | reproduced | 50 of 58 cells are not persistent under (a), 48 of 58 under (b) (cell 34). |
| fig2c-population-persistence | reproduced | Load 1: preferred trace above nonpreferred in 100% of bins, all bins significant (cell 36). |
| ext1bc-persistence-by-load | reproduced | Significant bins: 1.00 at load 1, 1.00 at load 2, 0.60 at load 3 (cell 38). |
| fig2d-cross-temporal-localized | reproduced | 17 encoding or early-maintenance training bins generalize. The largest fraction of maintenance test bins reached from a maintenance training bin is 0.14–0.18 (cell 40). See problem 6. |
| ext1de-cross-temporal-load23 | reproduced | Off-diagonal kept pairs: load 1 217/280, load 2 6–10, load 3 0, under every rule and label (cell 42). |
| fig2e-maintenance-decoding-amy-mtl | reproduced | Methods reading: AMY 35.63%, MTL 33.61%. Code reading: 34.33% and 32.89%. All p = 0.001 (cell 44). |
| ext1f-maintenance-decoding-load2 | partially_reproduced | Both groups are significant and MTL is in tolerance (26.67 / 29.56%). AMY is above tolerance under both readings: 26.43 / 27.89% against 21.2–25.9 (cell 46). |
| fig2f-bin-width-decoding | partially_reproduced | All widths are significant and accuracy rises with width. But no reading has all four accuracies in tolerance: code 250 ms gives 30.0% (36–44); rank reading 250 ms gives 50.0% and 500 ms gives 66.67% (cell 48). |
| fig2f-bin-width-pairwise | not_reproduced | 1000 vs 500 ms is not significant under any reading (BH 0.08–0.48). Under the code trial reading, 500 vs 250 ms is significant (cell 51). The criterion's partial condition is not met either. |
| ext1g-bin-width-load2 | reproduced | Load 2 range is 16 points (code) or 4 points (rank), both below 20, and load 2 is below load 1 at every width (cell 53). |
| fig3abc-trajectory-complexity | blocked (too_large), contested | Nothing was computed. The data are present; the block rests on run time only (problem 1). |
| fig3d-encoding-vs-maintenance-separability | blocked (too_large), contested | Same as above. |
| fig3h-early-vs-late-maintenance | blocked (too_large), contested | Same as above. |
| fig4c-encoding-bursts-vs-poisson | reproduced | Only under methods groups / height rule / real threshold (d1 and d2). There, All902 has BH p = 0.0054 and LowACG 0.038 / 0.048, and the other four groups are not significant (cells 67–68). The LowACG result is marginal. |
| fig4d-maintenance-bursts-vs-poisson | reproduced (weak) | Under the 2.8 s window, the five named groups exceed the null and concept cells do not, in 8 of 12 readings (cell 70). With each trial's own maintenance length (cell 71), ShortDecay fails (BH p = 0.114). See problem 3. |
| fig4-acg-group-differences | partially_reproduced | With the prominence rule, low ACG exceeds high ACG in both epochs (p = 0.0005). Short τdecay never exceeds long in encoding (p = 0.086–0.20). With the height rule the low/high direction reverses (cell 73). |
| fig4f-all-cells-epochs | partially_reproduced | Encoding to M1, M2 and M3 rises with q < 0.05 under the prominence rule. Encoding to probe is not significant under any reading (q = 0.61–0.71; medians 6.0 vs 5.5) (cell 75). |
| fig4hj-group-epochs | partially_reproduced | Under `*/prominence/M-code`, long τdecay rises at M1, M2 and M3, and low ACG, short τdecay and concept cells have 0 significant pairs. High ACG never rises to the probe (cell 78). |
| ext2-bursts-loads23 | reproduced | `methods/prominence/M-code` holds for all three groups at loads 1, 2 and 3 (cell 80). |
| acg-fit-yield | reproduced | 317 (all spikes) and 298 (trial spikes); tolerance 264.6–323.4 (cell 57). |
| fig5c-cell-type-clusters | reproduced | Reading (b) gives PY 100 and IN 198, both in tolerance. Reading (a) has PY 102, outside 82.8–101.2 (cell 59). |
| fig5dfh-cluster-features | reproduced | IN is higher on all three features, BY p ≤ 8e-5 under both readings (cell 61). |
| fig5gh-burst-index-cv2 | reproduced | Reading (b) types with the plain ISI CV of session spikes, medians: burst index 0.947 / 0.622 and CV 1.593 / 1.322, all in tolerance; p = 5e-3 and 1e-4 (cell 63). Holt's CV2 (1.18 / 0.93) never matches; the paper's "CV2" is a plain CV. |
| supp4-rodent-validation | reproduced | On the code's shipped features (data elsewhere): 333 of 343 correct, 1 PY and 9 IN misassigned (cell 65). |
| fig5kl-concept-cell-types | reproduced | Reading (b): PY 11, IN 14. Burst index 0.949 > 0.390 and Holt CV2 1.217 > 0.991. Reading (a) gives 16 IN concept cells, out of tolerance (cell 82). |
| fig6ab-celltype-bursts-vs-null | partially_reproduced | No reading meets all four parts. With the Poisson null and prominence rule, IN encoding is also elevated (q = 0.02–0.03). With the height rule, PY encoding fails (q = 0.06–0.11). With the label-shuffle null, IN maintenance fails (q = 0.063) (cell 84). |
| fig6cd-celltype-epochs | not_reproduced | IN encoding to probe has q = 0.73–0.80 under every reading. PY is stable at all loads only under M-code. The criterion's partial condition (load 1 only) does not apply (cells 86–87). |
| ext5bd-in-load-dependence | reproduced (weak) | The measure rises from load 1 to 3 (3.67 → 6.33) only under `prominence/M-code`, 2 of 8 readings (cell 89). |
| fig6e-load-modulation-in | partially_reproduced | IN 13.95% with p = 0.001 in tolerance; PY groups p ≥ 0.157. IN concept is 18.75% or 25.0% (tolerance 19.3–23.6). Under the (b) types it is 14.29% with p = 0.15 (cell 91). |
| fig6f-rt-modulation-in-concept | not_reproduced | With own RT, IN concept is 12.5% (p = 0.19), while all IN and PY are significant (cell 93). Only the code's subject-1 RT variant gives IN concept 31.25% with p = 0.001. |
| fig6gh-in-concept-cv2 | not_reproduced | IN preferred, maintenance vs encoding: p = 0.86 (load 1) and 0.13 (all loads) (cell 95). |
| ext5gh-py-decay-preferred | not_reproduced | PY preferred vs nonpreferred: p = 0.13–0.73 in every epoch and load set (cell 97). |
| fig6i-py-bin-width-decoding | not_reproduced | 750 and 1000 ms have BH p = 0.072 and 0.060; 250 ms gives 33.3%, outside 24.0–29.3 (cell 99). |
| fig6j-in-bin-width-decoding | partially_reproduced | Every width is significant (BH p = 0.002). Two of four accuracies are out of tolerance under each reading (code: 46.67 and 53.33 at 750 ms) (cell 101). |
| fig6kl-cross-temporal-by-type | reproduced | PY has 0 significant pairs; IN has 162–230 kept off-diagonal pairs (cell 103). |
| ext5ij-load2-decoding-by-type | reproduced | IN has BH p ≤ 0.013 at all widths; PY has none below 0.49 (cell 105). |

### B. Problems

1. **[affects a conclusion]** Cells 54–55: the block on fig3abc, fig3d and fig3h is about compute time, not data. The estimate is 127 min of serial dPCA fits, while the notebook took 19.2 min. The splits are independent, and `wm.pmap` (4 workers) is already used elsewhere; that alone would bring this to about 35 min. fig3abc needs only a handful of fits, and could have been decided on a reduced number of splits.

2. **[affects a conclusion]** Cells 59 and 67 onward: everything downstream uses `TY = TYPES["a"]`. That reading's PY count (102) is outside tolerance, and it yields 16 IN concept cells against the paper's 14. Reading (b) matches fig5c and fig5kl, but was carried into only one GLM configuration (cell 91). Claims never run with the (b) types: fig6ab, fig6cd, ext5bd, fig6f, fig6gh, ext5gh, fig6i, fig6j, fig6kl, ext5ij, and the PY/IN burst groups. The cell type is an open detail that can change these outcomes, e.g. IN concept 3/14 = 21.4% in fig6e.

3. **[affects a conclusion]** `wm.group_bursts`, cells 67, 70 and 84: with the 2.8 s maintenance window, real spikes stop at the probe (2.5–2.8 s), so each trial has a silent tail. The surrogates spread spikes uniformly over the full 2.8 s and fill that tail. I tested this on synthetic homogeneous Poisson data (spikes on [0, 2.5] in a 2.8 s stride): real 54 bursts against a null of about 41. Without the gap: real 40 against about 44. So "maintenance exceeds the Poisson null" (fig4d; fig6ab maintenance) can arise from the windowing alone, and encoding (no gap) cannot show it. The criterion's own-duration reading was run only for `code/prominence/real` (cell 71), and there fig4d fails.

4. **[does not affect a conclusion]** `wm.epoch_burst_counts` with the Methods M-reading: M3 counts include the 0.2–0.5 s empty tail, so M3 bursts are deflated. This produces the spurious M3 decreases under the height rule (cells 75, 77, 86). The rate per second was printed only for All902. Outcomes were decided on M-code readings, where this does not arise.

5. **[affects a conclusion]** `wm.fit_acg`, cell 57: the scipy fit agrees with the shipped MATLAB values for only 48% of R2, 7% of τrise and 11% of τdecay (within 1%). The fitted yield is 317 against 294, and τrise is a clustering feature, so the cell types differ (feeds problem 2). This is not stated as a limitation.

6. **[does not affect a conclusion]** `ct_analysis`, cells 40 and 42: the Methods cluster rule is degenerate. No shuffled map had any BH-significant pair (`null95_extent` = 0), so every real cluster is kept. The one-sided and two-sided tests are also identical, because of the `acc > 0.2` filter.

7. **[does not affect a conclusion]** Chance level: the paper states 20%. The notebook's LOOCV label-shuffled nulls average 9–17% for the pseudo-population and about 18% within participant (cells 44, 48, 99, 101). All p values are taken against this lower empirical null, which is never compared with the paper's 20%. This matters only for borderline cases such as PY at 250 ms (33%), which is not significant after BH anyway.

8. **[does not affect a conclusion]** Cell 32 onward: the downstream concept set is a single draw (code reading, seed 0). Counts range 57–60 over seeds, and the Methods reading (49–54 cells) is not carried downstream.

9. **[does not affect a conclusion]** Cell 49: at 1000 ms, accuracy on random six-per-image trial draws ranges 56.7–86.7%. The fig2f tolerances (±10%) are narrower than this trial-selection spread, so in-tolerance or out-of-tolerance results there carry little weight.

10. **[does not affect a conclusion]** Cell 7: one subject-9 trial has 0 s maintenance and 0 s fixation. It is kept in every analysis (fixation statistics, maintenance windows) and never excluded or checked.

11. **[does not affect a conclusion]** Different claims pass under different readings. fig4c passes only with the height rule, under which low ACG has fewer bursts than high ACG (contradicting fig4-acg-group-differences). The prominence-based claims pass with the opposite rule. Each criterion allows "one reading", but no single burst reading supports Fig. 4 as a whole.

12. **[does not affect a conclusion]** `cv2_cell` and `decay_cell`, cells 95 and 97: both build ISIs and ACGs from trial-concatenated spikes, which adds artificial cross-trial intervals. The ext5gh τdecay fits are made on ACGs of 25–34 spikes per cell, so that reading (taken from the claims file) is close to uninformative.

### C. Not checked, and what would have allowed it

- I could not check the code repository, so I cannot confirm three implementation choices said to follow it:
  - z-scoring window counts with fixation rate statistics in `zcounts` and `psth_z`;
  - drawing surrogate spike times on [0, TRIAL_WIN];
  - the 3 s window used for maintenance burst counts.
- **Would decide whether problem 3 is a code artefact or this notebook's:** the code's own surrogate output, or a run on Poisson-shuffled real data (a real-vs-null comparison on data with no true bursts).
- **Would settle problem 2:** fig6ab–ext5ij rerun with `TYPES["b"]`, plus the burst groups built from the (b) features.
- **fig4d and fig6ab maintenance:** the own-maintenance-duration burst variant under every reading, and M3 rates per second for every group.
- **Blocked dPCA claims:** at least the fig3abc fits, and H and Dunn tests on a parallel or reduced set of splits.
- **Problem 7:** decoding p values against the 20% binomial chance alongside the empirical-null p.
- **Problem 6:** the observed largest cluster extent, and the per-map significant-pair counts of the shuffled cross-temporal maps.

## End of run

22 turns, 6 minutes, $2.73 at API prices, result: success.
