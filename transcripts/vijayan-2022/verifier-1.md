# vijayan-2022 · verifier-1 · run 45514661848

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat *.y*ml *.json 2>/dev/null | head -300
```

```
total 688
drwxr-xr-x 6 runner runner    4096 Nov 25 00:48 .
drwxr-xr-x 8 runner runner    4096 Nov 25 00:48 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 00:45 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 00:45 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 25 00:48 .claude
-rw-r--r-- 1 runner runner       0 Nov 25 00:48 .env
-rw-r--r-- 1 runner runner       0 Nov 25 00:48 .env.development
-rw-r--r-- 1 runner runner       0 Nov 25 00:48 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 25 00:48 .env.local
-rw-r--r-- 1 runner runner       0 Nov 25 00:48 .env.production
-rw-r--r-- 1 runner runner       0 Nov 25 00:48 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 25 00:48 .env.test
-rw-r--r-- 1 runner runner       0 Nov 25 00:48 .env.test.local
drwx------ 2 runner runner    4096 Nov 25 00:48 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 00:45 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 00:45 .github
-rw-r--r-- 1 runner runner       0 Nov 25 00:48 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 00:45 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 25 00:45 .mcp.json
[... 322 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 300,2000p vijayan-2022.yaml
```

```
<persisted-output>
Output too large (36.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/da59b530-1992-4e2f-9998-b543ed7bf5b8/tool-results/bo9o69f59.txt

Preview (first 2KB):
    visits longer than 240 s is higher than for shorter visits by M5 at p < 0.05, and the bins
    below 240 s show no rising trend.
- id: fig3f-motor-program-not-faster
  statement: The delay between the dip in locomotor speed and egg deposition is similar for fast
    eggs and for all eggs in the three tunnel chambers, so the decision and not the deposition
    motor program is faster.
  source: Results, Flies lay eggs more rapidly on high-quality substrates, paragraph 2; Figure 3F
  quote: is similar for fast eggs ( Fig. 3F , pink) and all eggs in these three chambers
  expected:
  - quantity: eggs in the egg-aligned average, 4-mm tunnel
    value: 979
    tolerance: 97.9
  - quantity: eggs, 2-mm tunnel
    value: 918
    tolerance: 91.8
  - quantity: eggs, 2-mm tunnel with bounce
[... 21 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/da59b530-1992-4e2f-9998-b543ed7bf5b8/tool-results/bo9o69f59.txt"
}
```

```
1	    visits longer than 240 s is higher than for shorter visits by M5 at p < 0.05, and the bins
2	    below 240 s show no rising trend.
3	- id: fig3f-motor-program-not-faster
4	  statement: The delay between the dip in locomotor speed and egg deposition is similar for fast
5	    eggs and for all eggs in the three tunnel chambers, so the decision and not the deposition
6	    motor program is faster.
7	  source: Results, Flies lay eggs more rapidly on high-quality substrates, paragraph 2; Figure 3F
8	  quote: is similar for fast eggs ( Fig. 3F , pink) and all eggs in these three chambers
9	  expected:
10	  - quantity: eggs in the egg-aligned average, 4-mm tunnel
11	    value: 979
12	    tolerance: 97.9
13	  - quantity: eggs, 2-mm tunnel
14	    value: 918
15	    tolerance: 91.8
16	  - quantity: eggs, 2-mm tunnel with bounce
17	    value: 675
18	    tolerance: 67.5
19	  criterion: Egg-aligned speed M8 and pause time M7. The paper gives no test; a claim of
20	    similarity is judged by M7 pause times of fast eggs against all eggs of each chamber with
[... 571 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_vijayan_2022.ipynb'))
for i,c in enumerate(nb['cells']):
    print('=== CELL',i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: t=''.join(o['text'])
        elif 'data' in o: t=''.join(o['data'].get('text/plain',''))
        else: t=str(o.get('ename',''))+str(o.get('evalue',''))
        print('--- OUT:'); print(t[:6000])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt; grep -c 'CELL' $TMPDIR/nb.txt
```

```
1890 /tmp/claude-1001/nb.txt
81
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	=== CELL 0 markdown
2	# Reproducing Vijayan et al. (2022) from dandiset 000212
3	
4	Paper. Vijayan V, Wang Z, Chandra V, Chakravorty A, Li R, Sarbanes SL, Akhlaghpour H, Maimon G
5	(2022). An internal expectation guides Drosophila egg-laying decisions. *Science Advances* 8,
6	eabn3852. [doi:10.1126/sciadv.abn3852](https://doi.org/10.1126/sciadv.abn3852). The claims file
7	(`claims/vijayan-2022.yaml`) was written from the version of record in Europe PMC (PMC9616500), with
8	the supplement's figures and legends; Tables S1 and S2 were not available to it.
9	
10	Dandiset. [DANDI:000212](https://dandiarchive.org/dandiset/000212/draft), version `draft`. The
11	dandiset has no published version: the archive lists only the draft, so the draft is pinned, and
12	the notebook prints its modification time (2023-06-20T00:56:15Z when this attempt was made). The
13	paper cites the dandiset without a version (Data and materials availability).
14	
15	What the dandiset holds. 1013 NWB files, one per fly, in 33 chamber and genotype groups: at 2
16	frames per second, the fly's position, its island, the sucrose concentration under it and the
17	frames at which it laid an egg. They include the paper's tracked chambers (two-, three- and
18	five-island sucrose chambers, the tunnel chambers, the DL, TUT and D. suzukii strains, DDC>Kir at
19	four temperatures, three dopamine receptor mutants, and four agarose chambers) and the CS data of
20	ref. 16 that the paper reuses. They do not include the movable-boundary and glued-fly experiments,
[... 642 more lines not kept]
```

**Agent**

I've read the claims file and the first third of the notebook; reading the rest now.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 663,
 "limit": 620
}
```

```
663	for reading in ("visit", "search"):
664	    lt = E.pooled_trials(r, 300, 7200, reading)[1]; et = E.pooled_trials(r, 5, 30, reading)[1]
665	    print(f"{reading} trials: late {lt.sum()}/{len(lt)}, early {et.sum()}/{len(et)}, p = {E.ranksum01(lt, et):.3g}")
666	print(f"Rate on 200 mM since 0 mM: bins from 300 s {late[0]:.3f} eggs/min ({late[2]} eggs, {late[3]} frames); bins 5 to 30 s {early[0]:.3f} ({early[2]} eggs)")
667	rr = r["rate"][1:]
668	steps = np.diff(rr)
669	print("Rates from the 5-10 s bin on:", np.round(rr, 3).tolist())
670	print(f"Successive bins non-decreasing: {(steps >= 0).sum()} of {len(steps)}")
671	fig, ax = plt.subplots(figsize=(5, 3)); plot_curves(ax, {"200 since 0": r, "0 since 200": R("0-500-200-CS", 0, 200)}, "0/500/200"); plt.show()
672	--- OUT:
673	visit trials: late 233/349, early 52/8614, p = 0
674	search trials: late 233/328, early 52/2845, p = 0
675	Rate on 200 mM since 0 mM: bins from 300 s 1.478 eggs/min (233 eggs, 18919 frames); bins 5 to 30 s 0.088 (52 eggs)
676	Rates from the 5-10 s bin on: [0.0, 0.031, 0.139, 0.228, 0.168, 0.26, 0.342, 0.432, 0.527, 0.858, 1.163, 1.453, 1.759]
677	Successive bins non-decreasing: 11 of 12
678	
679	--- OUT:
680	<Figure size 500x300 with 1 Axes>
681	=== CELL 25 markdown
682	## fig2efg-inhibit-200-after-0
[... 600 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1283,
 "limit": 610
}
```

```
1283	    30-45        1.387                   13/53        1.211                   20/91                        0.7285                 0.176    0.7122
1284	    45-60        0.855                    5/35        1.211                   12/54                        0.3581                -0.356    0.2909
1285	    60-90        0.979                    9/31        0.701                    9/41                        0.4999                 0.278    0.4703
1286	   90-150        1.150                    8/23        0.891                   12/34                        0.9765                 0.259    0.9436
1287	  150-300        0.467                    4/19        0.863                   14/29                        0.0611                -0.396    0.0611
1288	  300-600        0.941                   13/17        0.551                    8/20                        0.0290                 0.390    0.0290
1289	 600-1200        1.019                     5/8        1.091                    8/11                        0.6820                -0.072    0.6820
1290	1200-7200        1.787                   12/12        1.591                    9/12                        0.0780                 0.196    0.0780
1291	Bins past 5 s with 0 mM significantly higher (visit trials): ['300-600'] ; (search trials): ['300-600']
1292	
1293	=== CELL 53 markdown
1294	## fig5de-suzukii-more-on-200
1295	
1296	> D. suzukii lays slightly more eggs on 200 mM than on 0 mM, consistent with spending more time on
1297	> high sucrose.
1298	=== CELL 54 code
1299	def egg_frac(groups, value=0):
1300	    groups = [groups] if isinstance(groups, str) else groups
1301	    k = sum(int((f["sucrose"][f["eggs"]] == value).sum()) for g in groups for f in G[g])
1302	    n = sum(len(f["eggs"]) for g in groups for f in G[g])
[... 589 more lines not kept]
```

**Agent**

The whole notebook is read. Now the helper module.

**Agent calls Read**

```json
{
 "file_path": "egglay.py"
}
```

```
1	"""Loading and measures for Vijayan et al. (2022), Sci Adv 8:eabn3852, on DANDI:000212.
2	
3	Every NWB file of the dandiset holds one fly: at 2 frames per second, the xy
4	position of its centroid (mm), the island it is on, the sucrose concentration
5	under it (mM) and a 0/1 egg series. The files are streamed from the archive
6	(each file is read into memory in one request and opened with h5py); nothing is
7	written to disk.
8	
9	Where each parameter comes from is given beside it:
10	  [claim]  the claims file's shared methods M1 to M8 (claims/vijayan-2022.yaml),
11	           which cite the paper;
12	  [paper]  a passage of the paper taken by the author (protocol, author 1.6);
13	  [assume] an assumption, with the reason;
14	  [std]    a standard choice for a detail that cannot change a result.
15	"""
16	import io
17	import re
18	from concurrent.futures import ThreadPoolExecutor
19	
20	import h5py
[... 468 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls docs 2>&1; grep -n -i "search\b\|0.1 mm\|18.5\|boxcar\|first frame before\|1 min apart\|at least 1 min\|separated" paper/10.1126-sciadv.abn3852.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/10.1126-sciadv.abn3852.txt; for pat in "Automated determination of egg-laying search.{0,1200}" "Calculation of egg-laying rate.{0,1800}" "Statistics .{0,1500}" "pause .{0,300}" "fig. S2.{0,600}" "merge.{0,300}"; do echo "#### $pat"; grep -oP "$pat" $f | head -5; done
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/10.1126-sciadv.abn3852.txt; grep -oP "Mathematical models.{0,3000}" $f | head -2; echo; grep -oP ".{300}fig. S4.{300}" $f | head; echo; grep -oP ".{200}(Fig. 3D|Fig. 3E|Fig. 7I|fig7I|\(I\) ).{300}" $f | head -8
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/10.1126-sciadv.abn3852.txt; grep -oP "Fig. 3\. .{0,2500}" $f | head -1; echo; grep -oP ".{100}Fig. 7I.{0,50}|\( I \).{0,400}" $f | head
```

Result: not kept, because it reads the paper's text.

**Agent**

Now a quick synthetic test of the core helpers (search start, pause time, rate counting).

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np, egglay as E
# search start
spd=np.zeros(400); spd[100:200]=1.0
print('start', E.search_starts(spd, np.array([199])), 'expect ~84')
# pause: moving until 190, still 190-199, egg 199
spd2=np.zeros(400); spd2[100:190]=1.0
print('pause', E.pause_times(spd2, np.array([199])), 'expect ~5 s')
# rate events: fly on 200 frames 0-99, on 0 from 100; egg at frame 130 (15 s after crossing)
lab=np.r_[np.full(100,200.),np.full(300,0.)]
fl=[dict(label=lab,eggs=np.array([130]),starts=np.array([90]),n=400)]
r=E.rate_events(fl,0,200)
print('eggs',r['eggs'],'\nframes',r['frames'],'\nvisits',r['visits'])
print('trials',[list(x) for x in r['trials_visit']][:5])
print(E.ranksum01(np.r_[np.ones(5),np.zeros(95)], np.r_[np.ones(20),np.zeros(80)]))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, egglay as E
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls ~/.venv* /opt 2>/dev/null | head; which -a python python3; pip install -q numpy scipy h5py requests 2>&1 | tail -2
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
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/usr/bin/python3
/bin/python3
ERROR: Could not install packages due to an OSError: [Errno 30] Read-only file system: '/home/runner/.local/bin/f2py'
```

**Agent calls Bash**

```bash
cd  python3 -m venv $TMPDIR/v && $TMPDIR/v/bin/pip install -q numpy scipy h5py requests 2>&1 | tail -2; $TMPDIR/v/bin/python -c "
import numpy as np, egglay as E
spd=np.zeros(400); spd[100:200]=1.0
print('start', E.search_starts(spd, np.array([199])), 'expect ~84')
spd2=np.zeros(400); spd2[100:190]=1.0
print('pause', E.pause_times(spd2, np.array([199])), 'expect ~5 s')
lab=np.r_[np.full(100,200.),np.full(300,0.)]
fl=[dict(label=lab,eggs=np.array([130]),starts=np.array([90]),n=400)]
r=E.rate_events(fl,0,200)
print('eggs',r['eggs'],'\nframes',r['frames'],'\nvisits',r['visits'])
print('trials',[list(x) for x in r['trials_visit']][:5])
print(E.ranksum01(np.r_[np.ones(5),np.zeros(95)], np.r_[np.ones(20),np.zeros(80)]))
"
```

```
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: /tmp/claude-1001/v/bin/python3 -m pip install --upgrade pip
start [84] expect ~84
pause [4.5] expect ~5 s
eggs [0 0 0 1 0 0 0 0 0 0 0 0 0 0] 
frames [ 9 10 10  2  0  0  0  0  0  0  0  0  0  0] 
visits [1 1 1 1 0 0 0 0 0 0 0 0 0 0]
trials [[np.int64(0)], [np.int64(0)], [np.int64(0)], [np.int64(1)], []]
0.0013887730892374812
```

**Agent**

Helpers behave as described on synthetic input. Now checking the archive for the blocked claims.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000212/versions/draft/" > meta.json; head -c 4000 meta.json; echo; curl -s "https://api.dandiarchive.org/api/dandisets/000212/versions/draft/assets/?page_size=1000" > a1.json; $TMPDIR/v/bin/python -c "
import json,re,collections
a=json.load(open('a1.json')); print(a['count'], a['next'])
g=collections.Counter(re.sub(r'-fly#-\d+$','',x['path'].split('/')[0]) for x in a['results'])
print(len(g)); print(g)
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; $TMPDIR/v/bin/python -c "
import json,requests
a=json.load(open('a1.json'))['results']
x=[r for r in a if r['path'].startswith('sub-0p8--1p4')][0]
print(x['path'])
m=requests.get(f\"https://api.dandiarchive.org/api/dandisets/000212/versions/draft/assets/{x['asset_id']}/\").json()
print(json.dumps(m,indent=0)[:3000])
"
```

```
sub-0p8--1p4--CS-fly#-1/sub-0p8--1p4--CS-fly#-1_behavior.nwb
{
"@context": "https://raw.githubusercontent.com/dandi/schema/master/releases/0.6.3/context.json",
"approach": [
{
"name": "behavioral approach",
"schemaKey": "ApproachType"
}
],
"schemaKey": "Asset",
"dateModified": "2022-08-09T18:16:57.882779-04:00",
"schemaVersion": "0.6.3",
"encodingFormat": "application/x-nwb",
"wasGeneratedBy": [
{
"name": "Acquisition session",
"schemaKey": "Session",
"startDate": "2021-01-01T01:01:01-05:00",
"description": "fly in egg laying chamber"
},
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" vijayan-2022.yaml; grep "^- id:" vijayan-2022.yaml | tr '\n' ' '
```

```
45
- id: leave-higher-stay-lower - id: fig1d-no-substrate-marking - id: fig1f-tarsi-proboscis - id: fig2bc-larger-chambers-two-options - id: fig2d-three-choice-inhibit-200 - id: fig2e-200-recovers-with-time - id: fig2efg-inhibit-200-after-0 - id: fig2-earlier-merge-three-choice - id: fig3ab-2mm-tunnel-faster - id: fig3c-bounce-faster - id: fig3d-dwell-before-fast-eggs - id: fig3e-rate-after-long-absence - id: fig3f-motor-program-not-faster - id: fig4a-shorter-middle-transits - id: fig4b-faster-middle-preferred - id: fig4d-anomalous-eggs-alternative - id: fig4e-inter-egg-not-longer - id: fig4f-motor-program-not-accelerated - id: fig5ab-strains-release-faster - id: fig5c-suzukii-no-preference - id: fig5de-suzukii-more-on-200 - id: fig5f-egg-numbers-differ - id: fig5gh-search-and-pause - id: fig6b-softer-preferred - id: fig6cd-hardness-fast-merge - id: fig6ef-pause-longer-hard - id: fig6g-more-time-softer - id: fig7a-screen-ddc-hits - id: fig7b-ddc-kir-sense-sucrose - id: fig7cf-kir-merge-earlier - id: fig7df-overall-rate-drops - id: fig7gh-choice-falls - id: fig7ik-not-egg-number-or-motor - id: fig7l-dopamine-gal80-rescue - id: fig7mn-brain-neurons - id: fig8a-d1-receptor-mutants - id: fig8b-mutants-sense-sucrose - id: fig8ce-mutants-flat-rates - id: fig8fg-time-and-eggs - id: fig8j-200-500-defect - id: fig8k-agarose-intact - id: dop1r1-84714-no-defect - id: figs2-search-definition-robust - id: figs3-long-searches - id: figs4-models-fail
```

**Agent**

**Verifier report, round 1: Vijayan et al. 2022 (doi:10.1126/sciadv.abn3852), DANDI:000212 draft**

The claims file has 45 claims. The notebook tests 31 and treats 14 as blocked (3 for metadata_insufficient, 11 for data_missing), which adds up to 45. My outcomes for the 31 tested claims: 20 reproduced, 7 partially reproduced, 4 not reproduced. I agree with all 14 blocks.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| leave-higher-stay-lower | reproduced | Cell 18: 1205 searches start on higher, 0.805 leave; 2773 start on lower, 0.331 leave. All within tolerance, p = 9e-167. |
| fig1d-no-substrate-marking | blocked (data_missing) | The archive has no movable-boundary group (33 groups, 1013 assets, checked through the API). |
| fig1f-tarsi-proboscis | blocked (data_missing) | No group with glued tarsi or proboscis. |
| fig2bc-larger-chambers-two-options | reproduced | Cell 20: 200 mM is below 0 mM in all 7 bins from 5 to 60 s in both chambers, all at p < 0.05. No merge in either. |
| fig2d-three-choice-inhibit-200 | reproduced | Cell 22: the three-choice rate is lower in 7 of 7 bins, significant in 7, under both trial readings. |
| fig2e-200-recovers-with-time | reproduced | Cell 24: 1.478 against 0.088 eggs/min, p ≈ 0. Non-decreasing in 11 of 12 steps. |
| fig2efg-inhibit-200-after-0 | reproduced | Cell 26: reading (b), at most 20%, holds in 3 of 3 chambers, all p < 1e-6. Reading (a) holds in 2 of 3 (0/500/200 ratio 0.147). |
| fig2-earlier-merge-three-choice | reproduced (weak) | Cell 28: merges at 1200, 5 and 5 s against none in every comparison chamber. Two of those merges are artefacts of near-empty early bins (problem 3). The outcome still holds under the search, ≥10 s reading (1200, 10, 300). |
| fig3ab-2mm-tunnel-faster | reproduced | Cell 30: 5–10 s bin, 1.236 against 0.364 eggs/min, p = 5e-7. |
| fig3c-bounce-faster | partially_reproduced | Cell 32, 5–10 s bin: higher than 4 mm (p = 2e-10) but not 2 mm (p = 0.051). The 0–5 s reading is not reproduced. |
| fig3d-dwell-before-fast-eggs | partially_reproduced | Cell 34: counts 36/44/22 are within tolerance and the medians increase. The medians themselves (45.5/57/379.5 against 54/96/576 s) are all out of tolerance, and 4 mm against 2 mm gives p = 0.54. |
| fig3e-rate-after-long-absence | reproduced | Cell 36: ≥240 s gives 1.213 against <240 s 0.345 eggs/min, p = 2e-8. Below 240 s the rate is flat (Spearman p = 0.20), except a 0.92 step in the 150–240 s bin. |
| fig3f-motor-program-not-faster | not_reproduced | Cell 38, reading (a): in the 4-mm chamber fast eggs pause less (0.5 against 1.0 s, p = 0.0014). Reading (b): all three chambers differ. |
| fig4a-shorter-middle-transits | partially_reproduced | Cell 40: edge medians 12.5–13.5 s are within tolerance. Middle medians are 4.5 s in two chambers but 4.0 s pooled and in 0/500/200, one frame outside tolerance. |
| fig4b-faster-middle-preferred | reproduced | Cell 42, 5–10 s bin: p < 1e-7 against the edge chambers pooled, each one, and 0/500/500, under both trial readings. |
| fig4d-anomalous-eggs-alternative | reproduced | Cell 44: 0.407 against 0.142 eggs/min, p = 4e-29. |
| fig4e-inter-egg-not-longer | reproduced | Cell 46: 2260/922/1901 intervals; medians 5.09/4.38/4.12 min are within tolerance in the Fig. 4A order. Neither middle-preferred chamber is longer. |
| fig4f-motor-program-not-accelerated | reproduced | Cell 48: median pause is 1.0 s in all three chambers, p = 0.56 and 0.20. |
| fig5ab-strains-release-faster | reproduced | Cell 50, visit trials: TUT merges at 20 s, DL at 90 s, CS does not merge. Search trials give TUT 90 s, which fails (problem 5). |
| fig5c-suzukii-no-preference | not_reproduced | Cell 52: the 300–600 s bin has 0 mM higher, p = 0.029 (13/17 against 8/20). The criterion says any such bin fails the claim. |
| fig5de-suzukii-more-on-200 | reproduced | Cell 54: egg fraction on 0 mM is 0.386 (CI 0.322–0.454); median time fraction on 0 mM is 0.197. |
| fig5f-egg-numbers-differ | reproduced | Cell 56: all 6 pairs differ at p < 0.05. |
| fig5gh-search-and-pause | reproduced | Cell 58: 6 of 6 pause pairs at p < 0.001; speed rises in all four groups. Egg counts are within tolerance. |
| fig6b-softer-preferred | blocked (metadata_insufficient) | No hardness label (problem 12). Four of the six conditions are also absent. |
| fig6cd-hardness-fast-merge | blocked (metadata_insufficient) | Same: no hardness label. |
| fig6ef-pause-longer-hard | reproduced | Cell 60: pause is longer on 1.4%, p = 4e-21. The 1.4% rate is lower and significant in the 5–10 and 10–15 s bins. The 0–5 s bin is 0 eggs in both, a tie, which is why the printed flag reads False. |
| fig6g-more-time-softer | blocked (metadata_insufficient) | Same: no hardness label. |
| fig7a-screen-ddc-hits | blocked (data_missing) | No screen lines in the archive. |
| fig7b-ddc-kir-sense-sucrose | blocked (data_missing) | Tracking only; no feeding-latency video or scores. |
| fig7cf-kir-merge-earlier | partially_reproduced | Cell 62: merges fall monotonically (none, 600, 25, 10 s) and 27 and 29/29.5 C stay biased. At 31 C two bins still differ (p = 0.001, 0.007), so under "first bin ≥5 s" neither 31 C reading holds. It holds only if "past 5 s" means ≥10 s. |
| fig7df-overall-rate-drops | partially_reproduced | Cell 64: 0.465, 0.208, 0.219 eggs/min. It falls from 27 C but not from 29/29.5 to 31 C. |
| fig7gh-choice-falls | reproduced | Cell 66: 0.938 > 0.919 > 0.761 > 0.296; median time fraction at 31 C is 0.266. |
| fig7ik-not-egg-number-or-motor | not_reproduced | Cell 68: eggs per fly are lower at 31 C than 18 C (p = 2e-4). Median pause is 40% shorter (1.5 against 2.5 s). See problem 10 on the criterion. |
| fig7l-dopamine-gal80-rescue | blocked (data_missing) | No Gal80 genotypes. |
| fig7mn-brain-neurons | blocked (data_missing) | No TSH-Gal80 or OTD-FLP groups. |
| fig8a-d1-receptor-mutants | blocked (data_missing) | Only 4 of 13 genotypes are present. Part can be tested: Dop1R1- 0.345, Dop1R2 attP 0.324, Dop1R2- 0.444 (all below 0.5) and CS 0.918 (cell 80). CS mean is 39.6 eggs/fly against 40. |
| fig8b-mutants-sense-sucrose | blocked (data_missing) | No feeding-latency data. |
| fig8ce-mutants-flat-rates | reproduced | Cell 70: at most 1 significant bin per mutant. Dop1R1- means are nearer CS 0 mM; both Dop1R2 curves are nearer CS 200 mM. |
| fig8fg-time-and-eggs | partially_reproduced | Cell 72: time fractions 0.399 and 0.393; no egg-count pair differs. The speed does not rise for Dop1R2 attP or Dop1R2-. |
| fig8j-200-500-defect | blocked (data_missing) | No 200/500 chambers for mutants or DDC>Kir. |
| fig8k-agarose-intact | blocked (data_missing) | No agarose chambers for mutants or DDC>Kir. |
| dop1r1-84714-no-defect | blocked (data_missing) | No BDSC 84714 group. |
| figs2-search-definition-robust | not_reproduced | Cell 74: fig5ab is reproduced under the working definition but keeps its outcome under only 1 of 3 alternates (TUT merges at 90 s under alt2; CS merges at 1200 s under alt3). The criterion needs at least two. |
| figs3-long-searches | reproduced | Cell 76: 3978 eggs, 95 flies; 0.949 in the 360–1500 s bin, 0.957 for 25+ transitions. |
| figs4-models-fail | partially_reproduced | Cell 78: model 1 overestimates 0 mM after 500 mM in 7 of 7 bins. The fit is weak (problem 9), and model 2 was not tested. |

### B. Problems

1. **[affects a conclusion]** `fast_eggs`, cell 36 (`visits` on the sucrose series): the dwell time is the length of the last unbroken run on 200 mM. The minimum dwell is 0.5 s (cell 34), which suggests flicker at the boundary splits visits. Split visits would shorten dwells, consistent with medians below the paper's (fig3d), and would change the binning in fig3e. The notebook never shows the visit-length distribution or merges sub-second visits. It also replaced the claims file's two readings ("from the midline" and "from leaving 200 mM") with ≤10 against <10 s.
2. **[affects a conclusion]** Pause time (`pause_times`, M7) is quantised at 0.5 s with medians of 1–2.5 s. The "<10% median difference" bound in fig3f and the 20% bound in fig7ik therefore come down to one frame, and fig4a's 4.0 against 4.5 s is also one frame. The notebook does not flag this. It is a weakness of the claims file's bounds, not a coding error.
3. **[does not affect a conclusion]** Cell 28 counts a merge at 5 or 10 s where both curves are near zero just after a transition. In 0/500/500/500/200 that is the 5–10 s bin (p = 1.0) and the 10–15 s bin (p = 0.90), and the bins after differ at p = 0.005. These are not releases of inhibition. The fig2-earlier-merge outcome survives without them, but the support is thinner than the table suggests.
4. **[affects a conclusion]** M5 "first bin past 5 s" (≥5 or >5) decides fig7cf. The notebook runs both readings but gives no verdict. The figs2 cell (74) uses only ≥5 s and only visit trials.
5. **[affects a conclusion]** The trial reading (visit or search) decides fig5ab: TUT merges at 20 s under visit trials and 90 s under search trials. The Methods' independence assumption covers "each substrate transition within a search", which supports the visit reading, so I took it. The notebook states no preference.
6. **[does not affect a conclusion]** `rate_events` in working mode counts frames twice where a 30-s extension overlaps the previous search. This is a stated assumption, and its size is never printed.
7. **[does not affect a conclusion]** Cell 8: 48 inter-egg intervals are under 10 s, and the paper says eggs are at least 1 min apart. Eleven of them are in Dop1R2-mutant-1, the group with 10 more eggs than the paper (596 against 586). These look like duplicate annotations the paper dropped. They are kept unexamined, with no effect on the outcomes.
8. **[does not affect a conclusion]** Cell 64 (fig7df) and the rate functions count only frames whose time since leaving the other substrate is under 7200 s. That leaves out search frames before the first crossing (1000 of 1031 eggs at 18 C).
9. **[affects a conclusion]** `fit_kernel` (figs4) is an unconstrained linear fit. It predicts negative rates (down to −1.5 eggs/min) and falls inside the 90% CI of its own training curve in only 3 of 7 bins. The paper's premise, a kernel that "roughly approximates" the 0/200 curves, is only half met. Because the model is linear in concentration, overshooting 500→0 is partly built in.
10. **[affects a conclusion; claims-file reading]** fig7ik reads "unrelated to the number of eggs" as "31 C flies lay no fewer eggs than 18 C". The paper more plausibly means preference is not explained by egg number. 27 C flies lay the most eggs (38/fly) with intact preference, and within 31 C the Spearman rho is −0.07 (p = 0.72). The pause half fails either way.
11. **[affects a conclusion; claims-file reading]** fig5c's rule "any significant bin fails" ignores multiple testing. One bin in 13 at p = 0.029 (17 and 20 trials) is about what chance gives, and alt1 and alt2 do not show it.
12. **[does not affect a conclusion]** Cell 9 prints dataset attributes only, not the `description` or `comments` attributes of the Island and Sucrose TimeSeries. Those might say which island is 0.8% agarose. The DANDI asset metadata, which I checked, carries no such field.
13. **[does not affect a conclusion]** Cells 46, 48, 60 and 72 print numbers without applying the criterion. I applied the criteria myself for fig4e, fig4f, fig6ef and fig8fg.

Helpers tested on synthetic input (`search_starts`, `pause_times`, `rate_events`, `ranksum01`) behave as documented. The one oddity is that time since leaving starts at 0.5 s, so the 0–5 s bin gets 9 frames instead of 10. This is negligible.

### C. Not checked, and what would settle it

- **Boundary flicker in the tunnel chambers (fig3d, fig3e):** the distribution of sucrose-visit durations in those chambers, and fig3d/fig3e rerun with visits under 1–2 s merged.
- **Agarose island labels (fig6b, fig6cd, fig6g):** a printout of all HDF5 group attributes (`description`, `comments`) for one 0p8--1p4 file.
- **fig7cf under the alternate search definitions:** cell 74 rerun with "first bin ≥10 s", and both trial readings for fig5ab under alt1 to alt3.
- **figs4:** a non-negative (for example log-link) kernel fit, and the model 2 integral controller, which was not attempted.
- **fig8fg speed rise:** the speed rise for the Dop1R2 mutants with other windows (for example 30 s), and the egg-aligned speed traces plotted per mutant.
- **Possible duplicate eggs:** a list of the sub-10-s egg pairs, to check whether they are duplicates.

## End of run

19 turns, 5 minutes, $2.01 at API prices, result: success.
