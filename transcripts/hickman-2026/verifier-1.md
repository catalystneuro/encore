# 000774 · verifier-1 · run 41232883765

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 388
drwxr-xr-x 6 runner runner    4096 Oct 31 19:19 .
drwxr-xr-x 7 runner runner    4096 Oct 31 19:19 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 31 19:09 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 31 19:09 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 31 19:19 .claude
-rw-r--r-- 1 runner runner       0 Oct 31 19:19 .env
-rw-r--r-- 1 runner runner       0 Oct 31 19:19 .env.development
-rw-r--r-- 1 runner runner       0 Oct 31 19:19 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 31 19:19 .env.local
-rw-r--r-- 1 runner runner       0 Oct 31 19:19 .env.production
-rw-r--r-- 1 runner runner       0 Oct 31 19:19 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 31 19:19 .env.test
-rw-r--r-- 1 runner runner       0 Oct 31 19:19 .env.test.local
drwx------ 2 runner runner    4096 Oct 31 19:19 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 31 19:09 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 31 19:09 .github
-rw-r--r-- 1 runner runner       0 Oct 31 19:19 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 31 19:09 .idea
[... 37 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1016-j.celrep.2026.117420.yaml"
}
```

```
1	# Claims for Hickman, Hughes, Sahai, Miles & Denman (2026), "Neural population dynamics of direct
2	# electrical stimulation of neocortex", Cell Reports 45, 117420, on dandiset 000774.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23, protocol
4	# pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read: the NIH author manuscript in Europe PMC / PMC (PMC13404931, NIHMS2190715), full text
7	# with Results, figure legends and STAR Methods, and Document S1 (supplement 1, 13 pages, legends of
8	# Figures S1 to S12). Table S1 (the "Statistics Table", the second supplementary file) is not in the
9	# text read: claims whose full model output is said to be there use only what the Results and
10	# legends print. The manuscript is based on the bioRxiv preprint of 2025-10-29 (10.1101/2025.10.28.685195).
11	#
12	# Data the paper used. Acute recordings: 9 C57BL6 mice, 9 recordings, awake and head-fixed, each with
13	# three Neuropixels 1.0 probes (A, B and C; 25 probes in all, probe A n = 7, B n = 9, C n = 9) inserted
14	# at 45 degrees around a 16-channel stimulating electrode (Neuronexus A1x16) in left V1, layer 5.
15	# Units sorted with Kilosort 2.5, registered to Allen CCF (region and coordinates per channel).
16	# Stimulation: single biphasic constant-current pulses, 100 us per phase, amplitudes 5, 25, 50 and
17	# 100 uA, cathodal-leading monopolar ("cathodal", negative amplitudes), anodal-leading monopolar
18	# ("anodal", positive amplitudes) and cathodal-leading bipolar ("bipolar"), 75 trials per condition,
19	# at least 2 s apart; other frequencies, depths and pulse widths were tested in some recordings and
20	# are in the dataset but not in the analyses. Measured variables: spike times of single units with
[... 970 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1016-j.celrep.2026.117420.yaml",
 "offset": 990
}
```

```
990	    value: 13.48
991	    tolerance: 1.35
992	  criterion: The modulation index MI = (r_resp - r_base)/(r_resp + r_base + eps) per bin. The sources
993	    disagree on its window - the Methods give a response window of 500 to 1000 ms with 5 ms bins, the
994	    Figure 6C legend a 500 ms window aligned to onset with 5 ms bins, and the code (figure7 cell 28)
995	    0 to 500 ms in 10 ms bins with the baseline the median rate from 1000 to 500 ms before onset.
996	    The "magnitude of modulation" is not defined in the paper; the code takes the trapezoid area of
997	    |MI| over bins (unit spacing), one value per unit, mean +- SD over units. As that area scales with
998	    the number of bins, the printed values are reached only with the code's 10 ms bins; readings (a)
999	    code, 0 to 500 ms, 10 ms bins, (b) legend, 0 to 500 ms, 5 ms bins, (c) Methods, 500 to 1000 ms,
1000	    5 ms bins, each with the code's baseline. Units good and stable, first 75 cathodal trials, regions
1001	    as the code's classify_region (cortical when the CCF name contains "area"). Two-way ANOVA
1002	    ols('AUC ~ Amplitude_mag * C(Region)'), type II, amplitude numeric; cortical against subcortical
1003	    per amplitude by t test, Student's (text) and Welch's (code) both run. Reproduced when under
1004	    reading (a) the four values are within tolerance and under every reading the region, amplitude
1005	    and interaction terms have p < 0.001, cortex grows more with amplitude than subcortex, and the 50
1006	    and 100 uA comparisons have p < 0.001.
1007	- id: fig6d-hva-subcortical
1008	  statement: At 100 uA higher visual areas, beyond the reach of direct activation, are more modulated
1009	    than subcortical units (15.82 against 13.48) although both lie at similar distances from the
[... 500 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c '^- id:' *.yaml; cat estim.py
```

```
10.1016-j.celrep.2026.117420.yaml:42
pnpm-lock.yaml:0
"""Loading and measures for dandiset 000774 (Hickman et al. 2026, Cell Reports 45, 117420).

The dandiset holds one NWB file per acute recording: spike times and Kilosort templates of the
units of three Neuropixels probes, with the CCF coordinates and region of each unit, and a trials
table of single electrical pulses (amplitude, polarity, pulse width, contacts and their CCF
coordinates). Files are streamed from the DANDI API at the pinned version; nothing is written to
disk.

Where each parameter comes from:

- The nine recordings of the paper are the nine sessions the paper's code loads
  (github.com/denmanlab/estim_populations at c4aaa608, figure4_figure5_figure6.ipynb cell 1);
  jlh41 is the tenth file of the dandiset and is left out (claims file header: 9 recordings,
  25 probes, probe A n = 7).
- Conditions (claims file header, "Method choices common to the claims on units"): single
  pulses (pulse_number 1) of 100 us per phase. In the files, "cathodal" is polarity
  "monopolar" with a negative amplitude, "anodal" monopolar with a positive amplitude, and
  "bipolar" bipolar with a negative amplitude (STAR Methods, Electrophysiological recordings:
[... 437 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_hickman_2026.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f'=== [{i}] {c[\"cell_type\"]} ===')
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--> '+''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--> '+''.join(d['text/plain']))
            else: print('--> [', list(d.keys()),']')
        elif o.get('output_type')=='error': print('ERR', o['ename'], o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1396 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	=== [0] markdown ===
2	# Reproducing Hickman et al. (2026) from dandiset 000774
3	
4	**Paper.** Hickman, Hughes, Sahai, Miles and Denman (2026), "Neural population dynamics of direct
5	electrical stimulation of neocortex", Cell Reports 45, 117420, doi:10.1016/j.celrep.2026.117420.
6	
7	**Dataset.** DANDI:000774, version `0.260520.1753` (doi:10.48324/dandi.000774/0.260520.1753),
8	streamed from the DANDI API. This is the version the paper cites in its key resources table, and the
9	only published version of the dandiset; the draft has the same ten assets.
10	
11	**Text the claims were written from.** The NIH author manuscript (PMC13404931) with the STAR Methods
12	and Document S1 (legends of Figures S1 to S12); Table S1 was not in the text read
13	(`claims/000774/10.1016-j.celrep.2026.117420.yaml`). Method details the claims file does not give
14	are taken from the paper and cited where used; where the paper is silent, from its code
15	(github.com/denmanlab/estim_populations at c4aaa608), as the claims file does.
16	
17	**What the dandiset holds.** Spike times, Kilosort templates, CCF coordinates and regions of the
18	units, and the table of electrical pulses, for ten acute recordings. The raw AP band, the LFP band
19	and the behaviour are not in it, as the paper says ("Raw data (LFP band, AP band, and NiDAQ binary
20	files) are not included in the NWB"), so the evoked-potential claims (Figures 1 to 3, S1, S2), the
[... 664 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 685,
 "limit": 720
}
```

```
685	Increase 5 to 100 uA in mean proportion: 2 ms 0.005, 5 ms 0.043, 10 ms 0.076
686	
687	Expected at 100 uA: 5 ms 0.092, 10 ms 0.175 (10%)
688	
689	=== [23] markdown ===
690	## fig5bc-amplitude-clusters
691	
692	> Clustering the direct responders by response probability across amplitude gives six clusters,
693	> broadly dose-dependent (58.6% of responders) or amplitude-selective, responding almost only at one
694	> amplitude (19.2% at 5 uA, 15.2% at 25 uA, 7.1% at 100 uA).
695	
696	The 99 responders of fig4j; Ward linkage, maxclust 6; features (a) the four nDRP values, as the code,
697	(b) each unit's vector divided by its maximum. A cluster is selective when its mean peaks at one
698	amplitude and is below half the peak at every other (the claims file's rule). The fractions are also
699	checked over every assignment of clusters to the four labels (the criterion's "some assignment"), and
700	over those in which a cluster labelled selective for an amplitude peaks at that amplitude.
701	=== [24] code ===
702	import itertools
703	EXP_AMP = {"dose": 0.586, 5: 0.192, 25: 0.152, 100: 0.071}
704	
[... 693 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000774/versions/0.260520.1753/assets/?page_size=100" | python3 -c "
import json,sys; r=json.load(sys.stdin); print(r['count'])
for a in r['results']: print(a['path'], a['size'], a['asset_id'])"; curl -s "https://api.dandiarchive.org/api/dandisets/000774/versions/0.260520.1753/" | python3 -c "
import json,sys; m=json.load(sys.stdin); print(json.dumps(m.get('assetsSummary'),indent=0)[:3000]); print(m.get('description','')[:2000])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000774/versions/" | python3 -c "
import json,sys; r=json.load(sys.stdin)
for v in r['results']: print(v['version'], v['status'], v.get('asset_count'), v.get('size'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np, estim, pandas as pd
from statsmodels.stats.multitest import multipletests
rng=np.random.default_rng(0)
for _ in range(5):
    p=rng.uniform(0,0.2,6); print(np.allclose(estim.holm_sidak(p), multipletests(p,method='holm-sidak')[1]))
# spike_prob
stims=np.arange(10)*2.0+1
train=np.sort(np.r_[stims[:5]+0.001, stims[:2]-0.006, stims[5]+0.0021, 30.0])
print(estim.spike_prob(train,stims))  # expect 0.5, 0.2, 0.3
print(estim.first_latencies(train,stims)[:7])
# PR
X=rng.normal(size=(1000,5)); print(estim.participation_ratio(X))
X=np.c_[rng.normal(size=1000), np.zeros((1000,4))]; print(estim.participation_ratio(X))
# signed distances: straight probe along dv, channels 0 deep, contact at ch 200
ch=np.arange(0,384,4); xyz=np.c_[np.full(len(ch),8000.), 3000-ch*10., np.full(len(ch),3000.)]
u=pd.DataFrame(dict(probe='A',ch=ch,ap=xyz[:,0],dv=xyz[:,1],ml=xyz[:,2]))
d,n=estim.signed_distances(u,np.array([8100.,1000.,3000.]))
print(n[ch==100], n[ch==200], n[ch==300], n[ch==0])
# classify
dur=np.r_[rng.normal(0.0003,0.00003,50), rng.normal(0.0007,0.0001,200)]
c=estim.classify_waveforms(dur, np.full(250,0.3), rng.normal(size=250))
print(pd.Series(c['kmeans'][:50]).value_counts().to_dict(), pd.Series(c['kmeans'][50:]).value_counts().to_dict())
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, estim, pandas as pd
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls /usr/bin/python3* /opt 2>/dev/null; which -a python python3 uv pip 2>/dev/null; ls ~/.venv* ~/venv 2>/dev/null | head
```

```
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.14
/usr/bin/python3.14-config

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
pipx_bin
post-generation
primer
runner-cache
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q v && . v/bin/activate && uv pip install -q numpy pandas scipy statsmodels requests h5py remfile 2>&1 | tail -2; python -c "import numpy, statsmodels; print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import numpy as np, estim, pandas as pd
from statsmodels.stats.multitest import multipletests
rng=np.random.default_rng(0)
print([np.allclose(estim.holm_sidak(p), multipletests(p,method='holm-sidak')[1]) for p in rng.uniform(0,0.2,(5,6))])
stims=np.arange(10)*2.0+1
train=np.sort(np.r_[stims[:5]+0.001, stims[:2]-0.006, stims[5]+0.0021, 30.0])
print(estim.spike_prob(train,stims))
print(estim.first_latencies(train,stims))
X=rng.normal(size=(1000,5)); print(estim.participation_ratio(X))
X=np.c_[rng.normal(size=1000), np.zeros((1000,4))]; print(estim.participation_ratio(X))
ch=np.arange(0,384,4); xyz=np.c_[np.full(len(ch),8000.), 3000-ch*10., np.full(len(ch),3000.)]
u=pd.DataFrame(dict(probe='A',ch=ch,ap=xyz[:,0],dv=xyz[:,1],ml=xyz[:,2]))
d,n=estim.signed_distances(u,np.array([8100.,1000.,3000.]))
print(n[ch==100], n[ch==200], n[ch==300], n[ch==0])
for seed in range(4):
  dur=np.r_[rng.normal(0.0003,0.00003,50), rng.normal(0.0007,0.0001,200)]
  c=estim.classify_waveforms(dur, rng.uniform(0.1,0.5,250), rng.normal(size=250),rng_seed=seed)
  print(pd.Series(c['kmeans'][:50]).value_counts().to_dict(), pd.Series(c['kmeans'][50:]).value_counts().to_dict())
# MI
st=np.arange(5,200,2.0); tr=np.sort(rng.uniform(0,202,4000)); 
mi=estim.modulation_index(tr,st,0,0.5,0.01); print(len(mi), np.trapezoid(np.abs(mi)))
"
```

```
[True, True, True, True, True]
(np.float64(0.5), np.float64(0.2), np.float64(0.3))
[1.  1.  1.  1.  1.  2.1]
(np.float64(4.965138904223215), 5)
(np.float64(1.0), 1)
[904.98756211] [-0.] [-904.98756211] [1902.49843945]
{'fs': 35, 'rs': 15} {'rs': 111, 'fs': 89}
{'fs': 26, 'rs': 24} {'rs': 102, 'fs': 98}
{'fs': 26, 'rs': 24} {'rs': 109, 'fs': 91}
{'fs': 28, 'rs': 22} {'rs': 102, 'fs': 98}
50 4.062215439637677
```

**Agent**

**Verification report, round 1: Hickman et al. 2026 against DANDI:000774 (0.260520.1753)**

The claims file has 42 claims. The notebook tests 18 and treats 24 as blocked. My outcomes: 10 reproduced, 5 partially reproduced, 3 not reproduced, 24 blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| fig4d-latency-trough | reproduced | The median trough over the four cathodal conditions is 1.95 ms (cell 10), and all 12 conditions have a higher bin before and after the trough. Taking "across parameters" as all 12 conditions gives 1.45 ms, which is outside tolerance; the criterion follows the code and uses cathodal only. |
| figs3cd-gmm-window | reproduced | The windows are 0.683, 1.139, 1.221 and 1.470 ms, with k = 4 chosen by BIC too (cell 12). No FDR-adjusted p is below 0.05 under any reading. This rests on 7 recordings, so the test of absence has little power; pooled over amplitudes, p = 0.0022. |
| fig4h-extent-constant | reproduced | ANOVA F = 1.250, p = 0.317 (cell 14), so the test of absence holds. With the dataset's coordinates the means at 50 and 100 µA are out of tolerance (813 and 452 µm); the criterion only reports the means. |
| fig4h-distance-decreases | partially_reproduced | With the dataset's coordinates: ANOVA p = 0.0094, Tukey 5–50 p = 0.013 and 5–100 p = 0.020. Means 414, 264, 129, 142 µm; the 25 µA mean (264 against 300 ± 30) is out of tolerance. The code's coordinates (outside input) give the paper's values exactly. |
| fig4h-ks-distinct | not_reproduced | With the dataset's coordinates, 5 against 100 µA has Holm-Sidak adjusted p = 0.11 (cell 18), so the first part fails. The other pairs are not significant. The code's coordinates give p = 0.0164, so the outcome depends on the coordinates. |
| fig4j-drp-increases | reproduced | 99 units; mean nDRP 0.116, 0.142, 0.194, 0.233; OLS F = 12.78, p = 0.00039 (cell 20). |
| figs3e-early-windows | partially_reproduced | At 100 µA the proportions are 0.058 and 0.106 (reading a) or 0.057 and 0.091 (reading b), against 0.092 and 0.175. Under reading a, both windows exceed 2 ms with FDR p = 0.021, and the rise with amplitude is larger for 5 and 10 ms. The direction holds; the values are 35–40% low. The criterion has no partial clause, so read strictly this is not_reproduced. |
| fig5bc-amplitude-clusters | reproduced | Reading a gives CCC 0.702, silhouette 0.352 and cluster sizes 15/19/40/13/7/5 (cell 24). One assignment of clusters to labels matches all four fractions. In it, the "100 µA-selective" cluster peaks at 50 µA, and the "25 µA" cluster is not selective (see B8). |
| fig5ef-polarity-clusters | reproduced | Reading a: n = 220, CCC 0.773, silhouette 0.538 (cell 26). Under the criterion's "some assignment" (clusters 2+5 bipolar 63/220 = 0.286, cluster 1 anodal 0.232, cluster 3 cathodal 0.186; each is that cluster's highest polarity), all three fractions are within tolerance. The notebook did not search assignments, and its half-maximum rule gives bipolar 0.205 (see B1). |
| fig5-fsrs-proportion | not_reproduced | No reading gets the proportions within tolerance: FS at 5 µA is 0.006 or 0.020 against 0.032, and RS at 100 µA is 0.022 against 0.037 (cell 28). The paper's F = 3.04 with p = 0.028 implies 3 df, so amplitude was categorical; with categorical amplitude, the amplitude term has p = 0.12. Under the k-means classes the class effect is significant (p = 0.028). Reading b, units within the evoked potential, was not run. |
| fig5j-fs-closer | reproduced | Threshold classes, dataset distances: waveform p = 0.009, amplitude p = 0.0097, FS mean 111 µm below RS 267 µm. FS at 5 µA is 205, RS at 5 µA 556 and RS at 100 µA 183, all within tolerance (cell 30). The Methods' k-means classes give waveform p = 0.087. |
| figs6b-fsrs-early-firing | reproduced | Threshold classes with 1 ms bins: Holm-Sidak p = 0.0056, 0.0038, 0.0127, 0.0127 (cell 32). The k-means classes and the 2 ms bins fail. |
| fig6c-modulation-cortex | partially_reproduced | Under reading a, the values and F statistics match the paper exactly (cell 34). The criterion also requires every reading to hold: under reading b the 50 µA t-test has p = 0.011, and under reading c the region term has p = 0.46, the amplitude term p = 0.00106, and the 50 and 100 µA comparisons are not significant. |
| fig6d-hva-subcortical | not_reproduced | Under the legend's groups, HVA is 13.91 (out of tolerance) and the Tukey test of HVA against subcortical gives p = 0.90 (cell 36). The code's groups give 15.82 and 13.68 with Tukey p = 0.020, but then the distance test gives p = 6e-8, where the paper says the distances do not differ. |
| fig6e-circuit-responders | partially_reproduced | Recomputed ZETA: cortical 0.125, 0.209, 0.520, 0.785 and subcortical 0.089 and 0.360. Two values (cortical at 5 µA, subcortical at 5 µA) fall just outside tolerance. Amplitude p = 7e-13 and region p = 2e-7 (cathodal model). Cortical exceeds 0.5 at 50 and 100 µA. The cached p-values agree with the recomputed ones (same decision for 97% of tests). |
| fig6f-no-propagating-wave | reproduced | Pearson r is −0.001 or 0.004 (p ≥ 0.92) for excitation and 0.047 (p = 0.24) for inhibition, n = 614 (cell 40). |
| figs9-state-drp | partially_reproduced | Reading a/i/x: DRP is higher on high-state trials at all four amplitudes, FDR p ≤ 0.0016. The values (0.012–0.017) are far from the expected 0.051–0.107. No reading gets the values. With nDRP the direction reverses. |
| fig6g-dimensionality-collapse | reproduced | With 2 ms bins, the middle-epoch PR and effective dimensionality are below 1 at every amplitude (0.98 down to 0.46). The largest bin in 0–20 ms is above 1 at 5, 25 and 50 µA (1.02, 1.09, 1.09), which is reading b. The window mean (reading a) never exceeds 1, and the 100 µA trace also exceeds 1 (see B10). |
| fig1l, figs1b, fig2g-extent-increases, fig2g-extent-sublinear, fig2-extent-polarity, fig2h, figs2gh, fig3c, fig3e, fig3fg, fig3h (11) | blocked: data_missing | I checked the archive: its metadata lists only `variableMeasured: Units, ElectrodeGroup`, with 10 files of 57–212 MB. That is far too small to hold the raw AP band of three Neuropixels probes, so there is no raw data. The draft has the same 10 assets. |
| fig4f-responders-within-ep, fig4i-proportion-within-ep, fig5i-fs-within-ep | blocked: data_missing | The evoked-potential boundaries need the raw AP band, which is not in the archive. They could be tested conditionally: the claims file points to the code's `EP_distances.pkl` as an outside input, and the unit side comes from the dataset (see B2). |
| fig7d, fig7e, fig7g, fig7h-pulses-detected, figs10c, fig7h-trains-better, fig7i, fig7j, no-learning-across-sessions, figs10e (10) | blocked: data_missing | The archive holds only the 10 files of the acute recordings; there are no behaviour files. Nothing in these claims can be tested. |

The paper states no chance levels for these selections.

### B. Problems

1. **[affects a conclusion]** Cell 26, fig5ef. The criterion makes the outcome rest on "fractions matching in some assignment of clusters to the labels". The notebook only applies the half-maximum rule and does no assignment search, although it does one for fig5bc in cell 24. Under the printed cluster sizes, a matching assignment exists, and each cluster in it is labelled with its own highest polarity.
2. **[affects a conclusion]** Cell 0 and cell 28. fig4f, fig4i, fig5i and reading b of fig5-fsrs are declared blocked without using the code's `EP_distances.pkl`. The claims file names it as an outside input to judge, and the notebook already uses other outside inputs from the same repository: `probe_coords_adj.pkl` and the cached ZETA p-values. The paper's fig5-fsrs proportions (about 0.03) look like the within-evoked-potential population, so the reading that was run is probably not the paper's.
3. **[affects a conclusion]** Cell 36, fig6d. The "legend" grouping still takes subcortical units from the code's SUBCORTICAL list, which has no CA1 or subiculum. The criterion's legend groups are CA1, subiculum, dentate gyrus and superior colliculus. Units in those two regions are left out of MIDF entirely (`sub_cort.notna()`), so the Tukey test under the legend's groups was never run as the criterion asks.
4. **[affects a conclusion]** `estim.classify_waveforms`. The k-means reading uses one `kmeans2` run (`minit='points'`, seed 0) on min-max normalised features. Its stability is never checked: the FS share is 332/1969 under k-means and 616/1968 under the threshold. The outcomes of fig5-fsrs, fig5j and figs6b differ between the two classifications, so the Methods reading rests on one initialisation.
5. **[affects a conclusion]** The dataset's coordinates and the code's disagree. The contact coordinates of jlh31 and jlh32 differ from the code's by 206 and 373 µm (cell 5). This alone decides fig4h-ks-distinct (adjusted p 0.11 against 0.016) and the 25 µA mean of fig4h-distance-decreases. The notebook reports both, but cannot say which coordinates are right.
6. **[affects a conclusion: unknown]** `estim.condition_trials`. Some cathodal conditions have 150 trials (jlh31, jlh34 in cell 4). The claims-file header asks for both readings, first run and layer 5 contact, wherever a recording has more than one matching run. Only the first run is used for cathodal pulses. For monopolar pulses the `contact_positive.nunique()` branch probably never filters, and the first 75 trials in time are taken. The layer 5 variant was run only for bipolar pulses in fig5ef. These two recordings hold 54 of the 99 responders.
7. **[does not affect a conclusion]** fig4d. The paper says "median across parameters"; over all 12 conditions that is 1.45 ms, outside tolerance. The claims file's restriction to cathodal comes from the code, so the claims file may misread the paper here. I report it and do not correct it.
8. **[does not affect a conclusion]** fig5bc. The only assignment that matches labels a cluster peaking at 50 µA ([−0.004, 0.021, 0.651, 0.343]) as "100 µA-selective". It labels a cluster with 0.27 at 5 µA and 0.47 at 25 µA as "25 µA-selective". The criterion's "some assignment" clause is lax enough to pass clusters that do not respond "almost only at one amplitude", as the claim says. This is a weakness in the claims file.
9. **[does not affect a conclusion]** Cell 40, fig6f. Peak picking leaves out the criterion's width ≥ 4 ms condition. The centre of mass covers ±5 ms rather than ±6 ms. Units without a prominent peak fall back to the argmax instead of being dropped. With r ≈ 0 at n = 614, the outcome is unlikely to change.
10. **[does not affect a conclusion]** Cell 44, fig6g. Reading b (largest bin in 0–20 ms above 1) does not discriminate: at 100 µA, where the paper reports no rise, the largest bin is also 1.04. No pre-stimulus noise floor is shown, and the 5 µA middle-epoch reduction (0.98) is not shown to exceed baseline variability.
11. **[does not affect a conclusion]** Cell 38, fig6e. The markdown says the trials are "restricted to single 100 µs pulses", but the code takes `tr[tr.run == run]` with no filter. The full Amplitude × Polarity × Region model is fitted only on the cached p-values; on the recomputed ones only the cathodal model is fitted.
12. **[does not affect a conclusion]** figs9. Raw DRP rises with spontaneous rate, so higher DRP on high-state trials is expected from baseline firing alone. Under nDRP the effect reverses (high below low, FDR p < 0.05). The criterion allows DRP, so the outcome stands, but the reading is fragile.
13. **[does not affect a conclusion]** Cathodal pulses exist in only 7 of the 9 recordings; jlh39 and jlh49v1 have bipolar pulses only. The exact matches (99 units, F = 12.78, the MI values) suggest the paper used the same 7, even though its legends say n = 9. Every test across recordings therefore has n = 7, where the smallest two-sided exact Wilcoxon p is 0.0156.
14. **Helper tests on synthetic inputs, all passed:** `holm_sidak` against statsmodels, `spike_prob` window edges, `first_latencies`, `participation_ratio` (isotropic data gives PR = 5, rank 1 gives 1), and the signs of `signed_distances`.

### C. What I could not check, and the output that would settle it

- **Cathodal runs:** whether the 150-trial cathodal conditions are one contact or two. Print `contact_negative` and `run` per condition, and run the cathodal layer 5 reading.
- **k-means stability:** print the FS fraction and the fig5j and figs6b outcomes across several seeds and initialisations.
- **fig6d with the legend's groups:** print the region-name counts and the Tukey test with CA1, subiculum, dentate gyrus and superior colliculus as subcortical.
- **fig5ef assignment search:** run it as cell 24 does for fig5bc.
- **The blocked boundary claims:** fig4f, fig4i, fig5i and fig5-fsrs reading b, run with the code's `EP_distances.pkl`.
- **fig6g noise floor:** print the pre-stimulus maximum of normalised effective dimensionality per amplitude.
- **ZETA runs:** print the trial composition (amplitude, pulse width, pulse_number) of each run used for ZETA.
- **fig6f as specified:** rerun with the width ≥ 4 ms filter and the ±6 ms centre of mass.
- **Correct coordinates:** I cannot tell whether the dataset's or the code's contact coordinates are right for jlh31 and jlh32; that needs the authors.
- **Stability flags:** the notebook does not compare its stability flags with the code's `slope_outlier` flags, and those flags are not available.

## End of run

14 turns, 5 minutes, result: success.
