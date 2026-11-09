# 001074 · verifier-1 · run 41346856342

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 208
drwxr-xr-x 6 runner runner   4096 Nov  1 20:41 .
drwxr-xr-x 7 runner runner   4096 Nov  1 20:41 ..
crw-rw-rw- 1 nobody nogroup  1, 3 Nov  1 20:26 .bash_profile
crw-rw-rw- 1 nobody nogroup  1, 3 Nov  1 20:26 .bashrc
drwxr-xr-x 5 runner runner   4096 Nov  1 20:41 .claude
-rw-r--r-- 1 runner runner      0 Nov  1 20:41 .env
-rw-r--r-- 1 runner runner      0 Nov  1 20:41 .env.development
-rw-r--r-- 1 runner runner      0 Nov  1 20:41 .env.development.local
-rw-r--r-- 1 runner runner      0 Nov  1 20:41 .env.local
-rw-r--r-- 1 runner runner      0 Nov  1 20:41 .env.production
-rw-r--r-- 1 runner runner      0 Nov  1 20:41 .env.production.local
-rw-r--r-- 1 runner runner      0 Nov  1 20:41 .env.test
-rw-r--r-- 1 runner runner      0 Nov  1 20:41 .env.test.local
drwx------ 2 runner runner   4096 Nov  1 20:41 .git
crw-rw-rw- 1 nobody nogroup  1, 3 Nov  1 20:26 .gitconfig
crw-rw-rw- 1 nobody nogroup  1, 3 Nov  1 20:26 .github
-rw-r--r-- 1 runner runner      0 Nov  1 20:41 .gitmodules
crw-rw-rw- 1 nobody nogroup  1, 3 Nov  1 20:26 .idea
[... 37 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1016-j.neuron.2026.07.008.yaml"
}
```

```
1	# Claims for Kalugin, Soden, ... Lehtinen & Andermann (2026), Neuron, doi:10.1016/j.neuron.2026.07.008,
2	# on dandiset 001074 ("Multiplexed optical recording of sensors on a micro-endoscope (MORSE)",
3	# most recent published version 0.260928.0807; title and description read, no data or asset list read).
4	#
5	# Provenance. Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions),
6	# 2026-10-22, protocol pilot-10 as stated in docs/protocol.md (Reader, steps 1 to 4).
7	#
8	# Text read. The accepted author manuscript in PubMed Central (PMC13568791, NIHMS2202779), as
9	# fetched to paper/10.1016-j.neuron.2026.07.008.txt: Summary, Introduction, Results, Discussion,
10	# STAR Methods (including "Quantification and statistical analysis"), figure legends of Figures 1
11	# to 6, Table 1, the key resources table and the video legends (S1 to S16); and the supplement
12	# NIHMS2202779-supplement-1.pdf (Figures S1 to S6 with legends), extracted into the same file.
13	# The version of record was not read. The paper reports no statistical test and no p-value: all
14	# support is means with SEM, counts, and figures. No claim therefore has `statistics`.
15	#
16	# Code read. github.com/pkalugin/kalugin-et-al-morse at commit fa4526ac02eaa2c5a24c4cfdcaab5c36ed5ae4ed
17	# (2026-08-06; the paper also cites Zenodo doi:10.5281/zenodo.21142692, not read). It holds
18	# microscope motor control (1_), Cellpose probability maps (2_), demons deformation fields (3_, 4_),
19	# CaImAn mask extraction, curation and cross-recording matching (5_), and the trace analyses by
20	# figure in 6_trace_analysis/ (Jupyter notebooks with printed outputs). Cells cited below are
[... 787 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1016-j.neuron.2026.07.008.yaml",
 "offset": 808
}
```

```
808	  source: Results, MORSE detects regionalized neuromodulator release in brain slices, paragraph 4;
809	    Figure 2I legend
810	  quote: In fact, discrete 100–300 nM increments in the concentrations of both ligands were evident
811	    after each of the first several trains of optogenetic stimulation
812	  expected:
813	  - quantity: per-train increment, lower bound
814	    value: 100
815	    tolerance: 10
816	    unit: nM
817	  - quantity: per-train increment, upper bound
818	    value: 300
819	    tolerance: 30
820	    unit: nM
821	  criterion: The example probe of Figure 2H-I. The NE and DA concentration (CONC, Eq. 19) with a
822	    5-frame median filter (morse_fig2_rev cell 205), train onsets from the stimulation record (45
823	    trains 20 s apart). The increment is open. Readings (a) the code's, concentration from 4 to 15
824	    frames after the train onset minus the value 4 frames after (cells 224-231); (b) the value at
825	    the next train's onset minus that at this train's onset. Over the first 5 trains, reproduced
826	    when the increments of both ligands lie in 90 to 330 nM. The legend's "100-200 nM" (90 to
827	    220 nM) is reported as a second range. The paper names no number of trains; "several" is read
[... 366 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_kalugin_2026.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain'])[:3000])
        elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
932 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	==================== 0 markdown
2	# Reproducing Kalugin et al. (2026) from dandiset 001074
3	
4	Paper. Kalugin PN, et al. (2026). Simultaneous, real-time tracking of many neuromodulatory
5	signals with multiplexed optical recording of sensors on a micro-endoscope. *Neuron*.
6	[doi:10.1016/j.neuron.2026.07.008](https://doi.org/10.1016/j.neuron.2026.07.008). The claims file
7	was written from the accepted author manuscript in PubMed Central (PMC13568791) with its
8	supplement (Figures S1 to S6); the version of record was not read.
9	
10	Dandiset. [DANDI:001074](https://dandiarchive.org/dandiset/001074/0.260928.0807), version
11	0.260928.0807. The paper cites the dandiset without a version. Three versions are published
12	(0.260804.2042, 0.260807.0137, 0.260928.0807); their asset lists hold the same 713 paths with the
13	same blobs and sizes (checked through the API while preparing), so they do not differ in anything
14	the analysis uses. The most recent is pinned, as the protocol asks when the paper cites none.
15	
16	What the dandiset holds. For each MORSE recording, the CaImAn output of the paper's pipeline:
17	a trace per cell mask (the denoised trace and its residual) and the 3D masks. There are no sensor
18	labels, no well, wash-on, injection or stimulation times, no region or experiment labels, and no
19	deformation fields, raw imaging, photometry, ELISA, histology or choroid plexus traces. Subjects
20	are named by date and probe, with the context (`wells`, `slice`, `mouse`).
[... 707 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 727
}
```

```
727	    for p in range(10):
728	        r = (LAB == g[0]) & (grp == p)
729	        if r.sum() > 1:
730	            keep = M.noise_keep(M.normalized_dose_trace(DX[r], g))
731	            if keep.sum() > 1:
732	                c, y = M.group_points(PLm[r][keep], g, "code")
733	                kn.append(M.fit_group(c, y)[0])
734	    kn = np.array(kn)
735	    consn = FITS[("iv", g)][0]
736	    mean, sem = kds.mean(), kds.std(ddof=1) / np.sqrt(len(kds))
737	    rows.append({"sensor": g[0], "probes": len(kds), "consensus nM": round(cons * 1e9, 1),
738	                 "per-probe nM": np.round(kds * 1e9, 0).tolist(), "mean nM": round(mean * 1e9, 0), "SEM nM": round(sem * 1e9, 0),
739	                 "(a) all within 10x": bool(np.all((kds > cons / 10) & (kds < cons * 10))),
740	                 "(a) probes within": int(np.sum((kds > cons / 10) & (kds < cons * 10))),
741	                 "(b) SEM < mean/2": bool(sem < mean / 2),
742	                 "noise cut: probes": len(kn),
743	                 "noise cut (a)": bool(np.all((kn > consn / 10) & (kn < consn * 10))),
744	                 "noise cut (b)": bool(kn.std(ddof=1) / np.sqrt(len(kn)) < kn.mean() / 2) if len(kn) > 1 else False})
745	J = pd.DataFrame(rows)
746	print(J.to_string(index=False))
[... 187 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "morse.py"
}
```

```
1	"""Loading and measures for dandiset 001074 (Kalugin et al. 2026, MORSE).
2	
3	The dandiset holds, for each MORSE recording, the CaImAn output of the paper's
4	pipeline: a trace per cell mask (RoiResponseSeries, the denoised trace C, and
5	`residuals`, the residual YrA) and the dense 3D masks. It holds no sensor
6	labels, no stimulus or well timing, and placeholder timing metadata (every
7	file says 30 Hz and starts at 0). What this module adds, and where each part
8	comes from:
9	
10	- Well timing. Every well lasts 93 frames, 3 min at 31 frames per minute.
11	  Source: the paper's code, morse_figs3_rev cells 1, 8 (`mean_factor` 31,
12	  well onsets every `3*mean_factor` frames) and Methods "3-5 min/well". The
13	  frame counts of the files are multiples of 93 (checked in the notebook).
14	- Well order of the revision probes (the ten ten-sensor probes of Figure 1G-J
15	  and Table 1) and the mixture concentrations: morse_figs3_rev cells 0-2
16	  (well lists), 338 and 345 (`c_offset_rev`, concentrations 10**(k - offset) M
17	  for the k-th of the seven wells of a mixture). Outside input, pinned at
18	  commit fa4526ac02eaa2c5a24c4cfdcaab5c36ed5ae4ed.
19	- dF/F0 with F0 the mean of the lowest 10% of the trace: Methods Eq. 27.
20	- Peak normalization by Eq. 28 (lowest and highest 10%): Methods.
[... 467 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;d=yaml.safe_load(open('10.1016-j.neuron.2026.07.008.yaml'))
print(len(d['claims']));print([c['id'] for c in d['claims']])"; python3 -c "
import json,urllib.request
url='https://api.dandiarchive.org/api/dandisets/001074/versions/0.260928.0807/assets/?page_size=1000'
out=[]
while url:
  d=json.load(urllib.request.urlopen(url)); out+=d['results']; url=d.get('next')
print(len(out))
import collections,re
subs=sorted(set(a['path'].split('/')[0] for a in out))
print(len(subs)); print([s for s in subs if 'slice' in s or 'mouse' in s])
print([s for s in subs if not ('slice' in s or 'mouse' in s or 'wells' in s)])
"
```

```
47
['fig1c-cells-per-gel', 'fig1d-collagen-reduces-warping', 'fig1f-koh-stability', 'methods-revision-probe-stability', 'fig1g-sensor-yield', 'fig1g-all-ten-sensors-respond', 'fig1h-crosstalk-pairs', 'table1-ec50-on-target', 'table1-ec50-off-target', 'table1-peak-dff-morse', 'fig1j-ec50-consistent-across-probes', 'figs3e-tau-on-under-one-minute', 'figs3f-depth-delay', 'figs2c-stabilization', 'figs2f-cells-tracked', 'fig2c-dlgn-kcl-activates-sensors', 'fig2c-dlgn-da-explained-by-ne', 'fig2d-dlgn-robust-counts', 'fig2e-dlgn-peak-concentrations', 'fig2f-dlgn-5ht-delay', 'figs4de-deconvolution', 'slices-no-peptide-release', 'figs5c-kcl-no-direct-effect', 'figs5d-pvh-ne-alone', 'figs5f-pvh-robust-counts', 'figs5g-pvh-dose-dependence', 'figs5i-pvh-ne-concentration', 'fig2h-lc-ne-da-peaks', 'fig2i-lc-increments', 'fig2jk-lc-robust-counts', 'fig2l-lc-ne-delay', 'slices-probe-stability', 'fig3df-ip-responses', 'figs6ef-photometry-kinetics', 'fig3g-ten-sensor-yield', 'fig3h-each-sensor-responds-ip', 'fig4-ip-csf-concentrations', 'fig4-ex-vivo-elevations', 'fig4-ex-vivo-two-orders-lower', 'figs6j-serum-dipping-matches-elisa', 'fig5ab-spontaneous-5ht', 'fig5cd-spontaneous-5ht-dynamics', 'fig5gh-chp-calcium', 'fig6-chp-grab-similar-time-courses', 'fig6c-ip-5ht-reaches-chp-fast-enough', 'figs6a-no-implant-inflammation', 'link-revision-well-order']
713
207
['sub-20230801-SL1PL35-slice', 'sub-20230817-SL1PL55-slice', 'sub-20230822-SL2PL52-slice', 'sub-20230824-SL1PL60-slice', 'sub-20230829-SL1PL56-slice', 'sub-20230830-SL1PL28-slice', 'sub-20230831-SL1PL55-slice', 'sub-220216-PK25PL8-mouse', 'sub-220311-PK24PL9-mouse', 'sub-220406-PK24PL10-mouse', 'sub-220408-PK27PL20-mouse', 'sub-220427-PK27PL20-mouse', 'sub-220622-PK44PL17-mouse', 'sub-220624-PK45PL13-mouse', 'sub-220701-PK49PL18-mouse', 'sub-220903-PK63PL34-mouse', 'sub-221018-PS10PL24-mouse', 'sub-230519-DG41PL52-mouse', 'sub-230525-DG42PL39-mouse', 'sub-230526-PK84PL50-mouse', 'sub-230601-PK85PL53-mouse', 'sub-230614-DG63PL54-
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json,urllib.request
url='https://api.dandiarchive.org/api/dandisets/001074/versions/0.260928.0807/assets/?page_size=1000'
out=[]
while url:
  d=json.load(urllib.request.urlopen(url)); out+=d['results']; url=d.get('next')
a=[x for x in out if 'ZS55ZS17' in x['path']][0]
m=json.load(urllib.request.urlopen('https://api.dandiarchive.org/api/dandisets/001074/versions/0.260928.0807/assets/'+a['asset_id']+'/'))
print(json.dumps({k:m[k] for k in m if k not in ('digest','contentUrl','identifier')},indent=1)[:3000])
import collections
probes=collections.defaultdict(set)
import re
for x in out:
  s=x['path'].split('/')[0][4:]
  probes[re.sub(r'-(wells\d*|slice|mouse\d?)$','',s)].add(re.search(r'(wells\d*|slice|mouse\d?)$',s).group(1) if re.search(r'(wells\d*|slice|mouse\d?)$',s) else s)
for p,v in sorted(probes.items()):
  if any(k.startswith('mouse') or k=='slice' for k in v): print(p,sorted(v))
v=json.load(urllib.request.urlopen('https://api.dandiarchive.org/api/dandisets/001074/versions/0.260928.0807/'))
print(v['metadata'].get('description','')[:2000])
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 19, in <module>
    print(v['metadata'].get('description','')[:2000])
          ~^^^^^^^^^^^^
KeyError: 'metadata'
{
 "id": "dandiasset:4d600fa4-9d4f-4420-ba24-17df73ac9fdb",
 "path": "sub-ZS55ZS17-250929-mouse/sub-ZS55ZS17-250929-mouse_ses-ch0-means-movie-nobg-cnmf-mr-m-raw-refit_ophys.nwb",
 "access": [
  {
   "schemaKey": "AccessRequirements",
   "status": "dandi:OpenAccess"
  }
 ],
 "@context": "https://raw.githubusercontent.com/dandi/schema/master/releases/0.7.0/context.json",
 "approach": [
  {
   "name": "microscopy approach; cell population imaging",
   "schemaKey": "ApproachType"
[... 170 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np, morse as M
t=np.arange(93.)
for tau in [5,15,40]:
  tr=np.r_[np.zeros(93), 1-np.exp(-t/tau)]
  print('tau',tau,'fit',round(M.tau_on(tr,93),2))
c=10.0**(np.arange(7)-10); kd=7e-7
y=1.05/(1+kd/c)
print('ec50',M.fit_ec50(np.tile(c,5),np.tile(y,5)+np.random.default_rng(0).normal(0,.03,35)))
# offset case like eq28: baseline 0.2
y2=0.2+0.8/(1+kd/c)
print('ec50 offset',M.fit_ec50(c,y2))
# percentiles
print(M.yield_stats(np.array(['A','B','','A']),np.array([0,0,1,1]),2))
# median filter smear effect on tau
from scipy.ndimage import median_filter
tr=np.r_[np.zeros(93), 1-np.exp(-t/15)]
sm=median_filter(tr[None],size=(1,31),mode='nearest')[0]
print('tau after 31 medfilt', M.tau_on(sm,93))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, morse as M
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls /usr/bin/python3* ; for p in python3 python3.11 python3.12; do $p -c "import numpy,scipy;print('$p ok')" 2>/dev/null; done; pip install --quiet numpy scipy h5py remfile 2>&1 | tail -2
```

```
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.14
/usr/bin/python3.14-config
ERROR: Could not install packages due to an OSError: [Errno 30] Read-only file system: '/home/runner/.local/bin/f2py'
```

**Agent calls Bash**

```bash
cd  python3 -m venv $TMPDIR/v && $TMPDIR/v/bin/pip install --quiet numpy scipy h5py remfile 2>&1 | tail -2; $TMPDIR/v/bin/python -c "
import numpy as np, morse as M
t=np.arange(93.)
for tau in [5,15,40]:
  tr=np.r_[np.zeros(93), 1-np.exp(-t/tau)]
  print('tau',tau,'fit',round(M.tau_on(tr,93),2))
c=10.0**(np.arange(7)-10); kd=7e-7
y=1.05/(1+kd/c)
print('ec50',M.fit_ec50(np.tile(c,5),np.tile(y,5)+np.random.default_rng(0).normal(0,.03,35)))
y2=0.2+0.8/(1+kd/c)
print('ec50 offset',M.fit_ec50(c,y2))
print(M.yield_stats(np.array(['A','B','','A']),np.array([0,0,1,1]),2))
from scipy.ndimage import median_filter
tr=np.r_[np.zeros(93), 1-np.exp(-t/15)]
sm=median_filter(tr[None],size=(1,31),mode='nearest')[0]
print('tau15 after 31 medfilt', M.tau_on(sm,93))
x=np.ones((1,279))*1.0; x[0,93:]+=0.5*np.exp(-np.arange(186)/15.5)
print('jump removal residual max', np.abs(M.remove_jumps(x)-1).max())
"
```

```
tau 5 fit 5.0
tau 15 fit 14.35
tau 40 fit 24.73
ec50 (np.float64(7.040774714985978e-07), np.float64(1.048078250767805))
ec50 offset (np.float64(2.6153280550839087e-07), np.float64(0.9576823486910259))
{'cells': 3, 'sensors_per_probe': [2, 1], 'median': 1.5, 'p25': 1.25, 'p75': 1.75, 'cells_per_sensor_per_probe': np.float64(1.0)}
tau15 after 31 medfilt 14.34815385573027
jump removal residual max 0.06052719399799389
```

**Agent**

**A. Outcomes** (47 claims in the claims file: 12 tested in the notebook, 35 blocked)

| Claim | My outcome | Reason |
|---|---|---|
| link-revision-well-order | reproduced | Cell 10: all 10 identification files have 11 wells of 93 frames and all dose files 15. Cell 11: 0.86 of cells rise most steeply in the first minute of a well, against a chance of 1/3; shifting the well onsets drops this to 0.23, 0.11 and 0.03. Cell 14: every sensor without crosstalk has 0.73 to 0.85 of its cells rising more in its own mixture. |
| fig1c-cells-per-gel | reproduced | Reading (b), curated masks (cell 16): 38 of 43 probes have a mean count in 90–220. Cell 17: cell centres fall in all three thirds of the depth in all 5 probes with an `mr-raw` file. Depth is bounded by the imaged z range (an assumption), and reading (a) cannot be tested. |
| fig1g-sensor-yield | partially_reproduced | Cell 19: median 9, 25th percentile 8 and 75th percentile 9 are all within tolerance. The cell count (559 in reading b, 382 in reading a, against 455–557) and cells per sensor per probe (6.82 and 4.72, against 5.42–6.62) are out under both labelling readings. |
| fig1g-all-ten-sensors-respond | not_reproduced | Cell 21: all 10 labels are present. But the mean trace is highest in its own or its partner's well for only 2 of 10 sensors by the per-well maximum, and 3 of 10 by the per-well mean. Even allowing the next well, CCK, NE and DA fail (DA peaks in the ATP well, which comes before the DA well). |
| fig1h-crosstalk-pairs | not_reproduced | Cell 23: NE–DA is the largest correlation (0.77), but AVP–OXT ranks 12th of 45 (14th with the 10-frame variant). 5HT–DA, DA–ACh and 5HT–NE all lie above it. |
| table1-ec50-on-target | not_reproduced | Cell 25: at most 2 of 10 within 10% under any reading (i to iv). Median \|log10 ratio\| is 0.12 to 1.49. |
| table1-ec50-off-target | not_reproduced | Cell 25: 0 of 4 within 10% under every reading. |
| table1-peak-dff-morse | not_reproduced | Cell 28: 4 of 14 (well reading a) and 5 of 14 (code's well, reading b) within 10%. MT is 0.56 against 0.30; CCK 0.49 against 0.40. |
| fig1j-ec50-consistent-across-probes | not_reproduced | Cell 30: reading (a) holds for 2 of 10 sensors and (b) for 6 of 10. Both fail, so this is not a split. With the noise cut, 7 and 8 of 10, still both fail. Per-probe values span orders of magnitude (DA from 69 nM to 1.05 mM). |
| figs3e-tau-on-under-one-minute | reproduced | Cell 32, with the CONSTANTS: 10 of 10 sensors under 60 s on dF/F0 and 8 of 10 on concentration. Both meet the 8-of-10 threshold. With the notebook's own fitted EC50s the variant gives 8 and 7 (a split), but those EC50s do not reproduce Table 1. |
| figs3f-depth-delay | not_reproduced | Cell 34: 5 of 10 slopes are positive in either depth orientation, against 9 needed. ATP is negative, but so are OXT, CCK, DA and ACh. |
| figs2f-cells-tracked | reproduced (marginal) | Cell 36: 44 of 72 probes (0.61) have a mean in 63–143, and the code's dipping set gives 8 of 10. Slice probes give only 5 of 11, and the probe set is not the paper's (see B11). |
| fig1d, fig1f, methods-revision-probe-stability, figs2c, slices-probe-stability | blocked (data_missing) | The archive holds only CaImAn traces and masks. There are no deformation fields or raw imaging. |
| figs6ef, fig4-ex-vivo-elevations, fig4-ex-vivo-two-orders-lower, figs6j, fig5gh, fig6, fig6c, figs6a | blocked (data_missing) | There are no photometry, ELISA, mass-spectrometry, choroid-plexus or histology files among the 713 assets. |
| 16 slice claims (fig2c ×2, fig2d, fig2e, fig2f, figs4de, slices-no-peptide-release, figs5c, figs5d, figs5f, figs5g, figs5i, fig2h, fig2i, fig2jk, fig2l) | blocked (metadata_insufficient) | 22 slice subjects exist, but there is no region label, wash-on, KCl, light or stimulation time, and no sensor label (cell 3: acquisition and stimulus are empty everywhere; timing is a 30 Hz placeholder). |
| fig3df, fig3h, fig4-ip-csf-concentrations, fig5ab, fig5cd | blocked (metadata_insufficient) | There are about 65 mouse subjects, but no injection times and no sensor labels. |
| fig3g-ten-sensor-yield | blocked (metadata_insufficient); part may be testable | It needs no timing, only labels on four ten-sensor in vivo recordings. Most mouse subjects have a post hoc `wells101` file (API listing). With the code's in vivo well order and probe list brought in, as the link claim did, the yield part could have been tried. The notebook does not discuss this. |

**B. Problems**

1. [affects a conclusion] `morse.label_clusters`: a cluster is labelled only if its mean derivative also peaks in the matched ligand's well. This rule is the author's own; it is not in the Methods and not in the stated assumptions (the module header states only the boxcar). It drops cells, so it drives the 382 and 559 cell counts and the cells-per-sensor figure in fig1g-sensor-yield. The administration boxcar (first minute of each well) is also an assumption.
2. [affects a conclusion] Cells 21, 23, 25, 28, 30, 32 and 34 use only the reading (b) labels (`LAB = lb`), although labelling was left open with two readings. Reading (a) is not carried into fig1g-all-ten-sensors-respond, fig1h, Table 1, fig1j, figs3e or figs3f. The large failures in fig1h and Table 1 are unlikely to flip, but this is unchecked.
3. [affects a conclusion] Cell 21 (fig1g-all-ten-sensors-respond): the per-well maximum or mean of a peak-normalized trace favours later wells when responses do not wash out between wells. The criterion as written is applied correctly, but the failure may come from carry-over rather than missing responses. DA peaking in the ATP well, before its own well, instead suggests poor DA labels; so do DA's high correlations with 5HT and ACh in cell 23. Label quality is never validated beyond cell 14.
4. [does not affect a conclusion] Cell 25, reading (iii): this is the Methods' reading, which the claims file says decides. It fits Eq. 9, which has no offset, to Eq. 28 plateaus whose low-dose value is not zero. It returns EC50s that sit on the fit's lower bound (shown as 0.0 to 1.5 nM). On synthetic data, an offset of 0.2 moves a true Kd of 700 nM to 262 nM. The reading is effectively broken, but every reading fails.
5. [does not affect a conclusion] Cell 25, off-target groups: they are normalized to their own peak well, not to the on-target maximum and the crosstalk ratio. Because F is free, this does not change Kd.
6. [does not affect a conclusion] Cell 30, reading (a): it is judged against the notebook's own consensus fits, some of which are degenerate (5HT 9.2 nM, MT 2.8 nM). Against Table 1 it still fails (5HT has a 1 nM probe; ATP reaches about 7 mM).
7. [does not affect a conclusion] `morse.tau_on` follows the code by fixing x∞ to the median of frames 47–78. On synthetic traces this underestimates long time constants: a true τ of 40 frames (77 s) is fitted as 24.7 frames (48 s). The bias favours "under 60 s" for figs3e. It is the specified method, but readers should know.
8. [does not affect a conclusion] `morse.remove_jumps`: the jump is measured at onset + 2 frames, after the decay has begun. On a synthetic jump of 0.5 it leaves a residual of up to 0.06.
9. [does not affect a conclusion] Cell 17 (fig1c): depth is tested on only 5 of 10 probes, and the gel thickness is taken as the imaged z range. The archive volumes have 15–26 planes, against the paper's 30.
10. [does not affect a conclusion] Cell 13: 559 of 829 matched cells are labelled. The paper reports 506 identified cells, so the cell pool differs from the paper's before any statistic is computed.
11. [affects a conclusion] Cell 36 (figs2f): two problems.
    - What a `matched<k>` file holds (one pair against a reference recording) is assumed and unverified. In probe 20230922-PL28 the "pair 0" files disagree (82, 96 and 99 cells).
    - The probe set covers all 72 probes, not the paper's S2F sets (dipping 40 recordings over 10 probes, slice 15, in vivo 25).

    The 0.61 result is marginal; with slice probes alone it is 5 of 11.
12. [does not affect a conclusion] Cell 0: the blocked reasons are stated only in the summary table. No cell shows per claim that the needed timing or labels are absent, beyond the global metadata survey in cell 3.

**C. What I could not check, and what output would have let me**

- Label validity. A per-cluster plot or table of the mean trace across the 11 wells, for both label readings, would have shown it. Also missing: downstream results under reading (a), and how many cells the "peak in matched well" rule drops.
- Whether the fig1g-all-ten-sensors-respond failure is carry-over. Per-sensor well-wise increments (the plateau of each well minus the previous well's plateau) would have shown it.
- Whether `mr-raw` really holds the curated masks and what `matched<k>` holds. The code's README, quoted, would have settled both. A cross-check of matched-cell counts against the code's printed counts per probe (morse_figs2_2 cell 4) would also have helped.
- fig3g. A listing of the mouse subjects that have post hoc `wells` files, with frame counts, would show whether the code's in vivo well order could be applied.
- The stability claims. The archive holds 13 revision-era in vivo subjects (2025, ZS…), matching the paper's "13/14 stable". This suggests only stable recordings were deposited, so no denominator can be tested; I did not confirm this.
- I did not re-run any cell or read any NWB content. All numbers above are taken from the notebook outputs. The helper functions were tested on synthetic inputs only.

## End of run

13 turns, 3 minutes, result: success.
