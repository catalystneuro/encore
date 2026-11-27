# costabile-2023 · verifier-1 · run 45738560660

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 284
drwxr-xr-x 6 runner runner    4096 Nov 26 02:34 .
drwxr-xr-x 8 runner runner    4096 Nov 26 02:34 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 26 01:51 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 26 01:51 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 26 02:34 .claude
-rw-r--r-- 1 runner runner       0 Nov 26 02:34 .env
-rw-r--r-- 1 runner runner       0 Nov 26 02:34 .env.development
-rw-r--r-- 1 runner runner       0 Nov 26 02:34 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 26 02:34 .env.local
-rw-r--r-- 1 runner runner       0 Nov 26 02:34 .env.production
-rw-r--r-- 1 runner runner       0 Nov 26 02:34 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 26 02:34 .env.test
-rw-r--r-- 1 runner runner       0 Nov 26 02:34 .env.test.local
drwx------ 2 runner runner    4096 Nov 26 02:34 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 26 01:51 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 26 01:51 .github
-rw-r--r-- 1 runner runner       0 Nov 26 02:34 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 26 01:51 .idea
[... 39 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "costabile-2023.yaml"
}
```

```
1	# Claims for Costabile, Balakrishnan, Schwinn & Haesemeyer (2023), "Model discovery to link neural
2	# activity to behavioral tasks", eLife 12:e83289, tested on DANDI:000235, 000236, 000237 and 000238.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-25,
4	# protocol as stated in docs/protocol.md (version pilot-19, Reader).
5	#
6	# Text read. The version of record (eLife, published 6 June 2023), paper/10.7554-elife.83289.txt,
7	# extracted from the publisher PDF (also under paper/): main text, the legends of Figures 1 to 7,
8	# Table 1, Methods, Data availability. The PDF was opened only to read Figure 6 (panels F and G)
9	# and Figure 7 (panel E), whose values the text does not give. eLife's figure supplements
10	# (Figure 1, 2, 3, 4, 5, 6 and 7, figure supplement 1) are online only: neither their panels nor
11	# their legends are in the PDF or the text. The Results state what each of them shows, and the
12	# claims that rest on them (region enrichments, Figure 6, figure supplement 1D, E, G to I;
13	# Figure 7, figure supplement 1A to E) are written from those Results sentences and from the
14	# code that draws them. Supplementary file 1 (Z-Brain region abbreviations) and the MDAR checklist
15	# are not under paper/; neither holds results.
16	#
17	# Code read. github.com/haesemeyer/mine_pub at commit 368d75650a1de92d9dd6c7dd1aadff24be6ba379,
18	# the revision the paper archives (Software Heritage, Haesemeyer 2023). It holds the CNN
19	# (model.py), the Taylor routines (taylorDecomp.py), the MINE interface (mine.py), the simulation
20	# scripts for Figures 1 to 4 (cnn_fit_test.py, cnn_nonlin_test.py, cnn_sta_test.py, mine_edf.py,
[... 852 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" costabile-2023.yaml; python3 -c "
import json
nb=json.load(open('reproduce_costabile_2023.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
"
```

```
<persisted-output>
Output too large (60.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/c87e3b04-4415-4582-ad0d-56e754466f66/tool-results/buesug5nc.txt

Preview (first 2KB):
35
==================== 0 markdown
# Reproducing Costabile et al. (2023) from dandisets 000235, 000236, 000237 and 000238

**Paper.** Costabile JD, Balakrishnan KA, Schwinn S, Haesemeyer M (2023). Model discovery to link
neural activity to behavioral tasks. *eLife* 12:e83289.
[doi:10.7554/eLife.83289](https://doi.org/10.7554/eLife.83289)

**Datasets.** DANDI:000235 "Thermoregulatory Responses Forebrain" version 0.230316.1600,
DANDI:000236 "Midbrain" version 0.230316.2031, DANDI:000237 "Hindbrain" version 0.230316.1655 and
DANDI:000238 "Thermoregulatory Responses Reticulospinal system" version 0.230316.1519. The paper
cites no version (its data list names the dandisets only). Each dandiset has a single published
version, all made on 2023-03-16, and the draft of each has the same asset count and size; the
published versions are pinned because they are the only fixed ones and the most recent.

**Claims.** `claims/costabile-2023.yaml`, written from the version of record (eLife, 6 June 2023)
[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/c87e3b04-4415-4582-ad0d-56e754466f66/tool-results/buesug5nc.txt"
}
```

```
1	35
2	==================== 0 markdown
3	# Reproducing Costabile et al. (2023) from dandisets 000235, 000236, 000237 and 000238
4	
5	**Paper.** Costabile JD, Balakrishnan KA, Schwinn S, Haesemeyer M (2023). Model discovery to link
6	neural activity to behavioral tasks. *eLife* 12:e83289.
7	[doi:10.7554/eLife.83289](https://doi.org/10.7554/eLife.83289)
8	
9	**Datasets.** DANDI:000235 "Thermoregulatory Responses Forebrain" version 0.230316.1600,
10	DANDI:000236 "Midbrain" version 0.230316.2031, DANDI:000237 "Hindbrain" version 0.230316.1655 and
11	DANDI:000238 "Thermoregulatory Responses Reticulospinal system" version 0.230316.1519. The paper
12	cites no version (its data list names the dandisets only). Each dandiset has a single published
13	version, all made on 2023-03-16, and the draft of each has the same asset count and size; the
14	published versions are pinned because they are the only fixed ones and the most recent.
15	
16	**Claims.** `claims/costabile-2023.yaml`, written from the version of record (eLife, 6 June 2023)
17	and checked by a second reader. The paper's code is github.com/haesemeyer/mine_pub at commit
18	368d756; the tail-processing code it names is bitbucket.org/jcostabile/2p, read here at commit
19	5ffaa2d.
20	
[... 677 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/c87e3b04-4415-4582-ad0d-56e754466f66/tool-results/buesug5nc.txt",
 "offset": 698
}
```

```
698	planes whose tail time starts before -10 s or ends after 500 s:
699	dandiset fish_short  plane  tail_n     tail_t0    tail_t1
700	  000235     Fish31     12  125303   -5.433369 623.799658
701	  000235     Fish31     29  125349   -5.461372 623.815622
702	  000235     Fish47     13  125355 -133.554176 495.803029
703	  000235     Fish47     22  125286   -5.527056 623.794162
704	  000235     Fish58      0  125110   -5.456032 623.809114
705	  000235     Fish58      7  125200   -5.347788 623.801286
706	  000235     Fish58      8  125247   -5.394603 623.794453
707	  000236     Fish10      5  125316   -5.444556 623.792484
708	  000236     Fish36     11  125273 -133.416849 495.804142
709	  000237     Fish39     16  125319   -5.373356 623.819701
710	tail start time (s) over all planes, percentiles 1/50/99: [-5.61 -5.42 -5.31] ; end: [495.78 495.8  495.95]
711	temperature trace minus imaging duration (s): median 10.53, range -0.07 to 10.95
712	planes whose temperature exceeds 30 C (paper: 22 to 30 C): 10 of 925; highest 31.57 C; {'Fish01': 2, 'Fish03': 1, 'Fish18': 1, 'Fish24': 1, 'Fish32': 1, 'Fish33': 1, 'Fish36': 1, 'Fish37': 1, 'Fish39': 1}
713	
714	==================== 21 markdown
715	The attempt record states which of these are findings.
716	==================== 22 markdown
717	## 3. data-zebrafish-coverage
[... 232 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat mine_data.py; echo =====; cat mine_cnn.py
```

```
"""Loading and per-plane measures for the zebrafish data of Costabile et al. (2023), eLife 12:e83289.

The four dandisets (000235 forebrain, 000236 midbrain, 000237 hindbrain, 000238 reticulospinal
backfills) hold one NWB file per fish. Each file has, for each imaging plane Z<k>: the raw
two-channel two-photon movie (acquisition/Z<k>_0 GCaMP, Z<k>_1 red), CaImAn's segmentation
(pixel masks), CaImAn's inferred calcium (CaUnitRespones_Z<k>) and dF/F, the temperature stimulus
at 20 Hz, and the 250 Hz tail tracking (segment angles and their sum, the cumulative tail angle).

Where each parameter comes from:
- Versions: the only published version of each dandiset (see VERSIONS).
- 5 Hz time base, interpolation, temperature at 20 Hz, bout-start binning, per-bout sums placed at
  the bout's start bin: the paper's code, github.com/haesemeyer/mine_pub at commit 368d756,
  rwave_data_fit.py (interp_times, bin_bout_starts, bin_time_discrete), as the claims file's
  opening comment states.
- Brightness criterion (mean photon count over imaging time of each component, below 0.1
  excluded): Methods, "Processing of zebrafish data", paragraph 2 ("all components for which the
  average brightness across imaging time was <0.1 photons were excluded"), computed as
  Experiment2P.avg_component_brightness in mine_pub/experiment.py (the unweighted mean of the
  time-average projection over the component's pixels). Assumption: the projection is taken of the
  movie the NWB files hold; whether it is CaImAn's motion-corrected movie is not stated.
[... 430 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np, mine_data as md
from scipy.ndimage import gaussian_filter1d
rng=np.random.default_rng(0)
T=2478
x=gaussian_filter1d(rng.standard_normal(T),25); x/=x.std()
Y=[]
for lag in [5,15,30]:  # samples (1,3,6 s)
    y=np.roll(x,lag)+0.5*rng.standard_normal(T); y=gaussian_filter1d(y,2.5); Y.append(y)
Y=np.array(Y).T
ho=md.heldout_shift_r(x,Y,md.CLOCK_OFFSETS)
for o,r in zip(md.CLOCK_OFFSETS*0.2,ho): print(o, np.round(r,3))
# bouts
s=np.zeros(1000); s[100:130]=8; s[500:503]=8
print(md.detect_bouts(s,10,5))
" 2>&1 | tail -20
```

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, mine_data as md
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls /usr/bin/python3* ; which -a python python3; ls ~/.venv* /opt 2>/dev/null; pip --version 2>&1
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
/opt:
actionarchivecache
az
containerd
google
hca
hostedtoolcache
microsoft
pipelinesagent-cache
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for p in /usr/bin/python3.14 /usr/bin/python; do $p -c "import numpy,scipy;print('$p ok')" 2>&1|tail -1; done; python -m venv $TMPDIR/v && $TMPDIR/v/bin/pip -q install numpy scipy h5py remfile requests 2>&1 | tail -2
```

```
ModuleNotFoundError: No module named 'numpy'
ModuleNotFoundError: No module named 'numpy'
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: /tmp/claude-1001/v/bin/python -m pip install --upgrade pip
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import numpy as np, mine_data as md
from scipy.ndimage import gaussian_filter1d
rng=np.random.default_rng(0)
T=2478
x=gaussian_filter1d(rng.standard_normal(T),25); x/=x.std()
Y=[]
for lag in [5,15,30]:
    y=np.roll(x,lag)+0.5*rng.standard_normal(T); y=gaussian_filter1d(y,2.5); Y.append(y)
Y=np.array(Y).T
ho=md.heldout_shift_r(x,Y,md.CLOCK_OFFSETS)
for o,r in zip(md.CLOCK_OFFSETS*0.2,ho): print(o, np.round(r,3))
s=np.zeros(1000); s[100:130]=8; s[500:503]=8
print(md.detect_bouts(s,10,5))
"
```

```
-30.0 [0.021 0.036 0.031]
-20.0 [0.067 0.031 0.03 ]
-10.0 [0.831 0.681 0.209]
-5.0 [0.952 0.847 0.859]
-2.0 [0.976 0.972 0.887]
-1.0 [0.98  0.971 0.978]
0.0 [0.98  0.976 0.979]
1.0 [0.98  0.976 0.979]
2.0 [0.98  0.976 0.979]
5.0 [0.979 0.976 0.979]
10.0 [0.851 0.925 0.974]
20.0 [0.43  0.371 0.54 ]
30.0 [0.546 0.536 0.523]
[]
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import numpy as np, mine_data as md
from scipy.ndimage import gaussian_filter1d
rng=np.random.default_rng(0)
T=2478
x=gaussian_filter1d(rng.standard_normal(T),25); x=(x-x.min())/x.std()  # 
x[:]=x - np.linspace(0,0,T)
x[:150]=x[:150]*0  # baseline at start like 22 C before the wave
x[-1]=x[-1]; 
Y=[]
for lag in [5,15]:
    y=np.roll(x,lag)+0.5*rng.standard_normal(T); y=gaussian_filter1d(y,2.5); Y.append(y)
Y=np.array(Y).T
print('start,end of x',x[:3],x[-3:])
ho=md.heldout_shift_r(x,Y,md.CLOCK_OFFSETS)
for o,r in zip(md.CLOCK_OFFSETS*0.2,ho): print(o, np.round(r,3))
"
```

```
start,end of x [0. 0. 0.] [2.31644157 2.31364997 2.3122227 ]
-30.0 [-0.004 -0.014]
-20.0 [0.3   0.181]
-10.0 [0.968 0.908]
-5.0 [0.98  0.974]
-2.0 [0.98  0.975]
-1.0 [0.98  0.975]
0.0 [0.98  0.976]
1.0 [0.98  0.976]
2.0 [0.98  0.976]
5.0 [0.939 0.971]
10.0 [0.578 0.717]
20.0 [-0.085 -0.1  ]
30.0 [0.426 0.324]
```

**Agent calls Bash**

```bash
cd $TMPDIR; for d in 000235:0.230316.1600 000236:0.230316.2031 000237:0.230316.1655 000238:0.230316.1519; do id=${d%%:*}; v=${d##*:}; curl -s "https://api.dandiarchive.org/api/dandisets/$id/versions/$v/assets/?page_size=200" | $TMPDIR/v/bin/python -c "import json,sys;j=json.load(sys.stdin);print('$id',j['count'],[a['path'].split('/')[-1][:40] for a in j['results']][:3])"; curl -s "https://api.dandiarchive.org/api/dandisets/$id/versions/draft/" | $TMPDIR/v/bin/python -c "import json,sys;j=json.load(sys.stdin);print(' draft',j['assetsSummary'].get('numberOfFiles'), j['assetsSummary'].get('variableMeasured'), j['assetsSummary'].get('dataStandard',[{}])[0].get('name'))"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  curl -s "https://api.dandiarchive.org/api/dandisets/000238/versions/0.230316.1519/assets/?page_size=200" | $TMPDIR/v/bin/python -c "
import json,sys,urllib.request
j=json.load(sys.stdin); a=j['results'][0]
m=json.load(urllib.request.urlopen('https://api.dandiarchive.org/api/assets/%s/'%a['asset_id']))
print(a['path']); print(json.dumps({k:m.get(k) for k in ['variableMeasured','measurementTechnique','wasAttributedTo']},indent=0)[:1500])"
```

Result: the fetched text is not kept.

**Agent calls Grep**

```json
{
 "pattern": "2\\.5 Hz|largely uncorrelated|empirically determined|<0\\.1 photons|0\\.1 photons",
 "path": "paper/10.7554-elife.83289.txt",
 "output_mode": "content",
 "-C": 1
}
```

Result: not kept, because it reads the paper's text.

**Agent**

**Verifier report, round 1: Costabile et al. 2023 (eLife 83289) on DANDI:000235 to 000238**

I count 35 claims in the claims file. The notebook tests 2 of them and treats the other 33 as blocked (9 simulation, 5 mouse, 12 on the CNN fits, 6 anatomical, and fig6f). The notebook still contains its summary cell (cell 30). I did not use it; every outcome below comes from the outputs.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| data-zebrafish-coverage | reproduced | Cell 23: 25 fish and 750 planes, both exact. 706,543 components, exact. 434,651 components have brightness ≥0.1, against 432,882 expected (+0.41%, tolerance 43,288). The counts come from the NWB files; the pixel-mask orientation was checked in cell 10 (r 0.83 one way, 0.01 the other). |
| figs6-train-test-uncorrelated | reproduced (criterion as written; see B4) | Cells 26–27: the largest \|median\| inter-trial r across the four predictors is 0.051, under every bout reading. That passes reading (b), <0.1. On a stricter variant the notebook also shows, the temperature median \|r\| is 0.266, with a 5th to 95th percentile of −0.62 to 0.54. |
| fig1f-mine-fits-ground-truth, fig2bcd-complexity-scores, fig2e-linearity-roc, fig2s1-nonlinearity-metrics-agree, fig3-receptive-fields-slow-stimuli, fig3-effective-degrees-of-freedom, fig3s1-white-noise-benchmark, fig3s1-training-length, fig4-taylor-metric-ranks-predictors | blocked (other: data elsewhere, generated by the paper's code; not attempted) | Claims file: `data: elsewhere`. The notebook's own estimates (cell 29) undercut its "too_large" reason: 0.1 h on 4 threads for fig1f and fig4, 0.1 h for fig3, 1.0 h for fig2e. The notebook had run 36 min by then. |
| fig5c-cortex-components-fit, fig5d-cortex-largely-linear, fig5e-uninstructed-movements-dominate, fig5fh-cortex-maps, fig5i-cortex-receptive-fields | blocked (data_missing) | The mouse widefield data are in the CSHL repository (doi:10.14224/1.38599), not in these dandisets. The notebook's "too_large" (1.4 h on 4 threads) is not the binding reason. |
| figs6-shuffle-enrichment, fig6d-mine-identifies-more-than-lm, figs6-mine-more-at-every-cutoff, fig6e-functional-classes, fig6e-mixed-selectivity-exists, fig6g-linear-model-bias, fig7b-receptive-field-clusters, fig7d-mixed-integration-modes, fig7e-complexity-by-cluster, lm-recovers-fewer-clusters, temperature-nonlinear-behavior-linear, interaction-terms-small | blocked (too_large) | The full analysis needs 432,882 CNN fits, plus as many on rotated controls: about 36 h, and 73 h with the controls, on 4 threads (cell 29). Parts were testable at small cost (B3): the linear-model side of fig6d and figs6-mine-more-at-every-cutoff, and subsample estimates of fractions. The swim, vigor and direction predictors also depend on bout thresholds chosen by the author (B8). |
| figs6-stimulus-neuron-regions, figs6-behavior-neuron-regions, figs6-mixed-neuron-regions, fig7a-behavior-feature-regions, fig7c-receptive-field-types, fig7f-complexity-anatomy | blocked (data_missing) | These need each neuron's Z-Brain region. I checked the archive API: each pinned version holds only NWB files (8, 9, 8 and 6, the same as the drafts). Their variableMeasured lists only OpticalChannel, PlaneSegmentation, TwoPhotonSeries, ImagingPlane, ProcessingModule and BehavioralTimeSeries. Cell 19 shows no registration and no reference images. The registered centroids are on Zenodo (`with_inputs`). |
| fig6f-reticulospinal-behavior | blocked (data_missing) | The hand-drawn backfill annotation is not in 000238. Cell 19 shows the segmentation has only a `pixel_mask` column and empty reference_images; the asset metadata agrees. It would also need fits (too_large) on the 218,257 components of 000238. |

### B. Problems

1. **[affects a conclusion] Cells 0 and 29: wrong block reason for the 14 data-elsewhere claims.** All 14 are called "too_large for the time left", but the notebook's own estimates for the simulation claims are 0.1 to 1.0 h on 4 threads. They were simply not attempted. For the mouse claims the real block is that the data are not in these dandisets.
2. **[affects a conclusion] Section 5 and the table in cell 0: wrong primary reason for the 6 anatomical claims and fig6f.** These are given as too_large through their dependence on the fits. The binding constraint is missing data: no Z-Brain registration, and no backfill annotation. They would stay blocked even with unlimited compute.
3. **[affects a conclusion, on partial testability] Cell 29: nothing of the 12 fit claims was tested.**
   - The linear comparison model is a closed-form Ridge regression. `heldout_shift_r` already runs a temperature-only Ridge on every bright component in the plane pass. A four-predictor version over all 434k components would have given the linear model's count for fig6d and its curve for figs6-mine-more-at-every-cutoff.
   - A random subsample of a few thousand MINE fits (under 1 h on 4 threads at 1.2 s per fit) would have estimated:
     - the fig6d fractions;
     - the fractions in temperature-nonlinear-behavior-linear;
     - the interaction metrics in interaction-terms-small;
     - roughly, the shuffle enrichment ratio.
4. **[does not affect a conclusion under the claims file; a weakness of the claims file] figs6-train-test-uncorrelated: the criterion tests \|median\| of the signed correlations.** Any distribution centred on zero passes, however large the individual correlations are. The temperature inter-trial correlations run from −0.91 to 0.87, with a median \|r\| of 0.27, which fails both levels on the stricter variant. I report this rather than correct it; the claim passes as the criterion is written.
5. **[does not affect a tested conclusion; relevant to any future fits] The clock check in `plane_pass` and `heldout_shift_r` (cells 14–15) is misread.**
   - The notebook takes the collapse of held-out r from 0.649 at 0 s to 0.198 at −1 s as "calcium never precedes temperature". That inference does not hold for this method. With the temperature advanced by 1 s, the 10 s window still covers lags −1 to 8.8 s.
   - On synthetic data I checked this. With a slow stimulus and a causal response at a 1 to 6 s lag, `heldout_shift_r` gives r of 0.85 to 0.98 for advances of 1 to 5 s. Adding a baseline step at the start of the trace did not change this.
   - The real-data collapse is therefore an unexplained anomaly.
   - Related: the temperature trace runs about 10.5 s longer than imaging. The notebook assumes that the temperature trace's time 0 is the start of imaging and never checks it. Only 5.3% of planes have their best displacement at 0 s.
6. **[does not affect a conclusion] `behavior_5hz` overwrites vigor and direction when two bouts start in the same 0.2 s bin.** It uses `out[1,bi] = ...` and `out[2,bi] = ...`, while the swim count adds with `+=`.
7. **[does not affect a conclusion] Cell 20: 10 planes have odd tail timestamps.** About 125k samples span roughly 629 s (−133 s, or up to 623.8 s), against about 501 s elsewhere at the same 4.0 ms median step. This means a gap or jump in the timestamps, and it is not investigated. Bouts in those planes are placed by raw timestamps.
8. **[does not affect a conclusion] Bout thresholds of 5 and 10 rad/s are the author's choice.** The paper says only "empirically determined", and the notebook states this as an assumption. The choice is reasonable: the code's default of 2 rad/s gives 4.9 bouts/s and sits within the noise of the 0.1 rad tracking steps. The default is also run, and the train-test result is the same under all four readings.
9. **[does not affect a conclusion] Brightness is computed on the movie the NWB files hold.** Whether that is CaImAn's motion-corrected movie is not stated; this is a declared assumption. The count is within 0.41% of the paper's, and its sensitivity to the cut (0.05 to 0.15) is shown.

### C. What I could not check

- **rwave_plot_panels.py.** It is not available here, so I could not confirm that the paper's inter-trial correlations use raw rather than orthogonalized behavior predictors, or the same per-plane trimming. Adding the orthogonalized-predictor variant to cell 26 would settle this.
- **Clock alignment.** The notebook should print the `starting_time` values and rates of the Temperature, CaUnitRespones and tail series. It should also say which end of the temperature trace carries the extra 10.5 s, and give a held-out r curve at 0.2 s steps from −10 to +10 s for a few planes.
- **Red channel in 000238.** `movie_shape_red` was computed but never printed for 000238. It would show whether Texas-Red images exist from which a backfill mask could at least be approximated.
- **Tail timestamps in the 10 odd planes.** Printing the largest `np.diff(tail_t)` and where it falls would show whether behavior is misplaced there.
- **Fit timing.** The estimate rests on 3 fits (median 1.21 s; the first took 5.55 s) and does not state the machine's core count. Timing about 20 fits and printing the core count would firm up the too_large estimate.
- **Channel 0 is GCaMP.** This is inferred from the mask correlation. Printing the Ch0 and Ch1 description fields would confirm it.

## End of run

15 turns, 4 minutes, $1.34 at API prices, result: success.
