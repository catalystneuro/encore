# 001960 · verifier-1 · run 42179756263

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 412
drwxr-xr-x 6 runner runner    4096 Nov  6 08:09 .
drwxr-xr-x 7 runner runner    4096 Nov  6 08:09 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  6 07:15 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  6 07:15 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  6 08:09 .claude
-rw-r--r-- 1 runner runner       0 Nov  6 08:09 .env
-rw-r--r-- 1 runner runner       0 Nov  6 08:09 .env.development
-rw-r--r-- 1 runner runner       0 Nov  6 08:09 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  6 08:09 .env.local
-rw-r--r-- 1 runner runner       0 Nov  6 08:09 .env.production
-rw-r--r-- 1 runner runner       0 Nov  6 08:09 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  6 08:09 .env.test
-rw-r--r-- 1 runner runner       0 Nov  6 08:09 .env.test.local
drwx------ 2 runner runner    4096 Nov  6 08:09 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  6 07:15 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  6 07:15 .github
-rw-r--r-- 1 runner runner       0 Nov  6 08:09 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  6 07:15 .idea
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.64898-2026.10.05.756595.yaml | head -400
```

```
# Claims for Qi, Parot, Wang, Pomeroy (SEP), Lavis & Cohen, "Large-scale all-optical
# electrophysiology links excitability and connectivity to circuit dynamics in vivo"
# (doi:10.64898/2026.10.05.756595) on dandiset 001960.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the bioRxiv preprint, version 1, full text flattened from the bioRxiv JATS XML
# (paper/10.64898-2026.10.05.756595.txt): main text, figure legends, Discussion and Methods,
# with the supplementary information PDF (media-5.pdf: Supplementary Movies 1 to 4 and
# Supplementary Figures 1 to 26) extracted into the same file. Pages 16, 39, 41 and 43 of the
# supplement PDF were rendered to read the significance marks of Supplementary Figures 10H,
# 24E, 25 and 26, which the extracted text garbles. The equations of the Methods (signal
# model, P(spk|V), the mixed model, balanced accuracy, the cross-STA definition) are lost in
# the flattened text; only their surrounding words survive. The movies were not seen.
#
# Code read: https://github.com/adamcohenlab/Qi2026WideAreaL1 at commit
# 181ad475520224c44d27903e7522d3e2aa76857d (2026-10-01). It holds figure_reproduction/, one
# MATLAB script and one NWB loader per figure (Figures 2 to 6), which rebuild the panels from
# the deposited NWB files, and tutorials/ 1 to 5 (movie to spikes, intrinsic properties, IPSP
# detection and fitting, spikelet detection, and the pre/post mixed model of Figures 3L and
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 400,1400p 10.64898-2026.10.05.756595.yaml
```

```
<persisted-output>
Output too large (54.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/e44dabac-3f66-4091-9a3c-f105f6dc8344/tool-results/bd4puylif.txt

Preview (first 2KB):
  criterion: The paper and code do not say how the 50% point was estimated beyond "n = 100
    neuron-pairs from each mouse, near detection cutoff". Readings (a) for the 100 pairs per
    mouse whose statistic lies nearest the Benjamini-Hochberg cutoff, the amplitude of each,
    mean +/- s.d.; (b) for those pairs, the amplitude of a scaled template added to null
    waveforms that is detected in half of the null draws. Reproduced when the mean is within
    tolerance under one reading.
- id: gap-junction-connection-counts
  statement: Spikelet mapping found 3,553 directed electrical connections among 7,280 tested
    pairs in one mouse and 2,199 among 7,032 in the other, 10 +/- 6 outgoing and 10 +/- 5
    incoming per cell, a pairwise probability of 41 +/- 15%; the median spikelet was 1.2% of a
    spike.
  source: Results, Gap junction coupling, paragraphs 2 and 3
  quote: We identified 3,553 statistically significant directed functional electrical
    connections out of 7,280 pairs tested in one mouse, and 2,199 of 7,032 in a second mouse.
    This corresponds to 10 ± 6 outgoing connections per cell and 10 ± 5 incoming connections
    per cell ... the pair-wise probability of unidirectional gap junction connections above our
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^- id:" 10.64898-2026.10.05.756595.yaml; wc -l 10.64898-2026.10.05.756595.yaml; python3 -c "
import json
for f in ['qi2026_excitability_connectivity.ipynb','qi2026_excitability_spontaneous.ipynb','qi2026_spontaneous.ipynb']:
    nb=json.load(open(f)); print(f,len(nb['cells']), nb.get('metadata',{}).keys())
"
```

```
90:- id: jf608-brighter
117:- id: targeting-signal-to-background
139:- id: spike-snr-and-detection-errors
165:- id: snr-decay-one-hour
180:- id: fig1d-stimulation-fold-change
197:- id: off-target-length-constants
218:- id: l1-sampling-density
237:- id: adaptation-vadp-correlation
258:- id: fig2c-three-bins
278:- id: fig2gk-bin-profiles
296:- id: two-mice-intrinsic-distributions
320:- id: synaptic-connection-counts
359:- id: ipsp-median-amplitude
382:- id: detection-limits
406:- id: gap-junction-connection-counts
444:- id: hadamard-stimulation-rates
473:- id: spikelet-not-scatter
490:- id: highmag-footprint
510:- id: lasso-off-target-correction
538:- id: connection-distance-structure
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dump.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--- OUT:\n'+''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--- OUT(data):\n'+''.join(d['text/plain'])[:5000])
            if 'image/png' in d: print('--- [image]')
        elif o.get('output_type')=='error': print('--- ERROR', o['ename'], o['evalue'])
EOF
for f in qi2026_*.ipynb; do python3 $TMPDIR/dump.py $f > $TMPDIR/${f%.ipynb}.txt; wc -l $TMPDIR/${f%.ipynb}.txt; done
```

```
1700 /tmp/claude-1001/qi2026_excitability_connectivity.txt
249 /tmp/claude-1001/qi2026_excitability_spontaneous.txt
925 /tmp/claude-1001/qi2026_spontaneous.txt
```

**Agent**

The materials are three notebooks (plus helper `l1opto.py`) covering a 56-claim file. Reading them now.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/qi2026_excitability_connectivity.txt"
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Reproducing Qi et al. (2026) from dandiset 001960
4	
5	Paper. Qi, Parot, Wang, Pomeroy, Lavis and Cohen, "Large-scale all-optical electrophysiology
6	links excitability and connectivity to circuit dynamics in vivo", bioRxiv preprint
7	doi:10.64898/2026.10.05.756595 (version 1). The claims file `claims/001960/10.64898-2026.10.05.756595.yaml`
8	was written from the full text of that preprint (main text, figure legends, Methods) and its
9	supplementary information PDF, and checked by a second reader.
10	
11	Dataset. DANDI:001960, version 0.261013.2016 (doi:10.48324/dandi.001960/0.261013.2016),
12	streamed from the archive. The paper's Data availability statement names the dandiset without a
13	version, and this is the only published version (the draft has the same 7 assets and the same
14	size, 505,494,176,572 bytes), so the most recent published version is pinned, as the protocol
15	asks when no version is cited.
16	
17	Code read for methods. The paper's code, https://github.com/adamcohenlab/Qi2026WideAreaL1 at
18	commit 181ad475520224c44d27903e7522d3e2aa76857d, which the claims file cites for many criteria.
19	Every method detail is cited in the helper `l1opto.py` or in the cell that uses it.
20	
[... 718 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/qi2026_excitability_connectivity.txt",
 "offset": 739,
 "limit": 500
}
```

```
739	highmag-footprint needs 7.5x recordings the dandiset does not hold. detection-limits needs the
740	per-pair null distributions (10,000 and 5,000 draws of pulses or spikes per pair), and
741	lasso-off-target-correction needs per-trial evoked spike counts and the lasso penalty; neither the
742	per-trial IPSP responses nor the penalty and the selection of the 1755 pairs are given.
743	
744	######## CELL 29 [markdown]
745	### connection-distance-structure
746	> Synaptic connectivity had an exponential degree distribution, a connection probability of 24% for
747	> cells under 150 um apart and a length constant of about 105 um; gap junction probability was 83%
748	> under 150 um with a 159 um length constant.
749	
750	Probability = connected over tested ordered QC pairs, by distance, both mice pooled (per mouse
751	shown). Probability under 150 um over pairs from 0 um (synaptic) or 60 um (gap junction) to 150 um.
752	Length constant: readings (a) A exp(-r/lambda) by least squares on binned probability, (b) a line
753	on log probability; bins of 30 or 60 um, from 60 um (gap) or 0 um (synaptic) to 400 um. Degree
754	distribution: exponential when an exponential fits the in- and out-degree histograms better than a
755	power law (lower residual on log counts).
756	
757	######## CELL 30 [code]
758	def binned_prob(kind, lo, width, mice=L.MICE):
[... 480 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/qi2026_excitability_connectivity.txt",
 "offset": 1238,
 "limit": 470
}
```

```
1238	### fig5e-inhibition-in-spontaneous-voltage, fig5e-inhibition-in-spontaneous-rate, fig5g-gap-junction-synchrony
1239	> Relative to distance-matched unconnected controls, a presynaptic spike is followed 15 to 30 ms later
1240	> by a postsynaptic hyperpolarization of -2.1% of a spike height for the strongest quintile of
1241	> connections and -1% at median strength; unconnected control pairs instead rise by 1% of a spike
1242	> height from -20 to -5 ms to 15 to 30 ms.
1243	
1244	> For the strongest quintile of synaptic connections, a presynaptic spike lowers the postsynaptic
1245	> rate by 0.18 Hz 5 to 13 ms later, a loss of 7e-3 spikes over the IPSP; near median strength, by
1246	> 0.083 Hz, a loss of 2.7e-3 spikes.
1247	
1248	> Gap-junction coupling raises spontaneous spike synchrony; for the strongest quintile, synchronous
1249	> firing (lag <= 2.5 ms) exceeds near-synchronous firing by 0.86 Hz more than in unconnected
1250	> neighbours, and by 0.32 Hz at median coupling.
1251	
1252	Stored `spontaneous_cross_spike_sta` and `spontaneous_spike_cross_correlogram` of the sparsePulseHad
1253	sessions (lag 0 at index 140). Connected QC pairs 60 to 400 um, quintiles of IPSP amplitude or
1254	spikelet amplitude per mouse (code, quintileConnectivityAverages), pooled over mice. Controls for a
1255	connected pair (i, j): pairs (i, k) with k within 400 um of both i and j and unconnected to i
1256	(Methods, Estimating cross STAs), 60 to 400 um from i (code). Measures (Methods, Effect of
1257	connections): voltage suppression = mean of frames 12 to 25 minus mean of frames -17 to -4; rate
[... 444 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.64898-2026.10.05.756595.yaml",
 "offset": 440,
 "limit": 400
}
```

```
440	    Methods). The connection counts are taken in the 60 to 400 um band, as the code settles
441	    (loadFigure5SessionFromNWB.m lines 15 to 23 give 3553 for M-YQ0201-27 and 2199 for
442	    M-YQ0201-29 in that band); all pairs within 400 um is a variant. For "pairs tested" the
443	    readings of synaptic-connection-counts apply, with or without pairs under 60 um.
444	- id: hadamard-stimulation-rates
445	  statement: During Hadamard-coded stimulation, stimulated cells fired at 25.4 +/- 16.6 Hz and
446	    non-stimulated cells at 3.9 +/- 4.5 Hz; each cell received about 640 stimuli and fired
447	    about 12,380 evoked spikes in total.
448	  source: Results, Gap junction coupling, paragraph 1
449	  quote: Stimulated cells spiked rapidly (25.4 ± 16.6 Hz, mean ± s.d.) compared to
450	    non-stimulated cells (3.9 ± 4.5 Hz), and evoked spikes were largely uncorrelated between
451	    cells. Each cell received on average 640 stimuli, which elicited on average a cumulative
452	    12,380 spikes per cell
453	  expected:
454	  - quantity: rate of stimulated cells
455	    value: 25.4
456	    tolerance: 16.6
457	    unit: Hz
458	  - quantity: rate of non-stimulated cells
459	    value: 3.9
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.64898-2026.10.05.756595.yaml",
 "offset": 839,
 "limit": 660
}
```

```
839	    Direction from the phase gradient (Hilbert phase, 325 um Gaussian smoothing, 160 um grid).
840	    Reproduced when the mean speed and the event count are within tolerance under one reading
841	    and the circular mean direction lies in the medial-posterior quadrant.
842	- id: spike-synchrony-localized
843	  statement: Spike-rate cross-correlograms peak sharply in space (length constants of 277 um
844	    quiet and 270 um whisking) and time (50% decay by 2.5 ms lag), unlike subthreshold
845	    correlations (2.4 mm, full width at half maximum 80 ms).
846	  source: Results, Spontaneous spikes and subthreshold voltages, paragraph 5; Figure 4C, 4D;
847	    Supplementary Figure 20F, G
848	  quote: While the subthreshold cross-correlations decayed slowly over space (quiet-state
849	    length constant 2.4 mm) and time (quiet-state full-width at half-maximum 80 ms), the
850	    spike-rate cross-correlogram had a peak that was sharply localized in space (length
851	    constants of 277 and 270 μm for quiet and whisking state respectively) and time (decayed by
852	    50% at lags of just 2.5 ms
853	  expected:
854	  - quantity: spike synchrony length constant, quiet
855	    value: 277
856	    tolerance: 27.7
857	    unit: um
858	  - quantity: spike synchrony length constant, whisking
[... 640 more lines not kept]
```

**Agent**

First notebook read (connectivity, Fig 2, 3, 5E–G, 6 subtype claims). Now the other two notebooks.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/qi2026_spontaneous.txt"
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Reproducing Qi et al. (2026) from dandiset 001960: spontaneous sessions
4	
5	Paper. Qi, Parot, Wang, Pomeroy, Lavis and Cohen, "Large-scale all-optical electrophysiology
6	links excitability and connectivity to circuit dynamics in vivo", bioRxiv preprint
7	doi:10.64898/2026.10.05.756595 (version 1); the claims file was written from its full text and
8	supplement. Dataset. DANDI:001960 version 0.261013.2016, the only published version (see the
9	first notebook, `qi2026_excitability_connectivity.ipynb`, for the choice and the full data check).
10	
11	This notebook tests the claims that use the two spontaneous (behavior) sessions:
12	
13	| Claim | Tested here |
14	|---|---|
15	| spike-snr-and-detection-errors, snr-decay-one-hour | tested |
16	| subthreshold-correlation-length, subthreshold-low-dimensional, quiet-state-oscillations, spike-synchrony-localized, voltage-to-spike-sigmoid, fig4g-private-depolarizations, fig4hi-self-sta-diverges | tested |
17	| traveling-waves | blocked, methods underspecified |
18	| npy-fraction-and-similarity, npy-subthreshold-similar, npy-umap-groups, npy-whisking-onset-rates, npy-oscillation-peak-rates, npy-state-dependent-excitability | tested |
19	
20	######## CELL 1 [code]
[... 689 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/qi2026_spontaneous.txt",
 "offset": 709,
 "limit": 220
}
```

```
709	from sklearn.cluster import KMeans
710	counts = []
711	for seed in range(10):
712	    tot = np.zeros((2, 2), int)  # rows group 1, 2; columns NPY-, NPY+
713	    for m in L.MICE:
714	        R = BEH[m]
715	        Xb = R["umap_counts"][R["umap_binmask"]].T  # cells x bins
716	        Zb = (Xb - Xb.mean(1, keepdims=True)) / Xb.std(1, ddof=1, keepdims=True)
717	        Zb = np.nan_to_num(Zb)
718	        uu, ss, _ = np.linalg.svd(Zb, full_matrices=False)
719	        emb = umap.UMAP(n_neighbors=20, n_components=2, random_state=seed).fit_transform(uu * ss)
720	        grp = KMeans(2, n_init=1, random_state=seed).fit_predict(emb) + 1
721	        rates = R["umap_counts"].T
722	        gm = np.vstack([rates[grp == 1].mean(0), rates[grp == 2].mean(0)])
723	        tm = np.vstack([rates[~R["gfp"]].mean(0), rates[R["gfp"]].mean(0)])
724	        cc = np.corrcoef(np.vstack([gm, tm]))[:2, 2:]
725	        if cc[0, 1] + cc[1, 0] > cc[0, 0] + cc[1, 1]:
726	            grp = 3 - grp
727	        for gi in (1, 2):
728	            tot[gi - 1, 0] += np.sum((grp == gi) & ~R["gfp"])
[... 198 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/qi2026_excitability_spontaneous.txt"
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Reproducing Qi et al. (2026) from dandiset 001960: intrinsic properties and spontaneous firing
4	
5	Paper. Qi, Parot, Wang, Pomeroy, Lavis and Cohen, "Large-scale all-optical electrophysiology
6	links excitability and connectivity to circuit dynamics in vivo", bioRxiv preprint
7	doi:10.64898/2026.10.05.756595 (version 1); the claims file was written from its full text and
8	supplement. Dataset. DANDI:001960 version 0.261013.2016, the only published version (see the
9	first notebook, `qi2026_excitability_connectivity.ipynb`, for the choice and the full data check).
10	
11	| Claim | Tested here |
12	|---|---|
13	| fig5a-rheobase-predicts-spontaneous-excitability, supp22-rheobase-correlations, fig5b-adaptation-dvdt, fig5c-adp-bursting | tested |
14	
15	######## CELL 1 [code]
16	import os
17	os.environ.setdefault("OMP_NUM_THREADS", "4")
18	import time
19	import numpy as np
20	import pandas as pd
[... 230 more lines not kept]
```

**Agent**

Third notebook read. Now the helper module.

**Agent calls Read**

```json
{
 "file_path": "l1opto.py"
}
```

```
1	"""Loading and measures for dandiset 001960 (Qi, Parot, Wang, Pomeroy, Lavis and Cohen 2026).
2	
3	Wide-area all-optical electrophysiology of about 320 layer 1 interneurons in each of two
4	NDNF-Cre::NPY-GFP mice (M-YQ0201-27 and M-YQ0201-29), with three sessions per mouse:
5	``behavior`` (spontaneous activity), ``sparseOpto`` (intrinsic excitability mapping) and
6	``sparsePulseHad`` (connectivity mapping), plus a raw-movie excerpt of one behavior session.
7	
8	Files are streamed from the DANDI Archive with remfile and h5py; nothing is downloaded to disk.
9	The large voltage arrays are stored time x cell in blocks of 10,000 frames, so they are read in
10	time blocks over all cells, and reduced as they are read.
11	
12	Where a parameter comes from is said at each function: "claims" for the claim's criterion
13	(which cites the paper or its code), "paper" with the passage for a detail taken from the paper
14	(protocol, author step 1.6), "code" for the paper's code, https://github.com/adamcohenlab/
15	Qi2026WideAreaL1 at commit 181ad475520224c44d27903e7522d3e2aa76857d, "assumption" for a choice
16	the paper leaves open, and "standard" for a detail that cannot change a result.
17	"""
18	from __future__ import annotations
19	
20	import functools
[... 653 more lines not kept]
```

**Agent**

Helper read. Checking specific paper passages: the SNR definition, the IPSP duration, the traveling-wave methods, and the detection limits.

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "shot noise|1\.4826|median absolute|SNR" 10.64898-2026.10.05.756595.txt | head -40
```

```
39:In previous Optopatch constructs, the voltage-sensitive microbial rhodopsin was very dim, requiring high-intensity laser illumination (> 10 W/mm 2 ) and a high numerical aperture (NA > 0.7) objective 12 – 14 , which together constrained measurements to < 10 neurons simultaneously. The chemigenetic GEVIs Voltron1 and Voltron2 are ∼500-fold brighter than the pure opsin-based GEVIs 28 , leveraging fluorescence from a palette of bright and stable organic HaloTag-Ligand dyes 2, 29 . We sought a bioavailable, red-shifted dye to combine with a blue-shifted channelrhodopsin, CheRiff 30 . While the commonly used Janelia Fluor (JF) 585 HaloTag ligand (HTL) is viable in vivo , we found the redder JF608-HTL to be 3.6 times brighter, with similar voltage sensitivity, leading to a 50% increase in signal-to-noise ratio (SNR) in vivo (Supplementary Fig. 1A-E). We developed an Optopatch construct for Cre-dependent co-expression of soma-targeted channelrhodopsin, CheRiff, and soma-targeted Voltron1 ( Fig. 1A ). An analogous construct made with Voltron2 performed similarly in our experiments.
61:The single-spike SNR (spike-height:baseline shot noise) was 4.5 ± 0.7 (mean ± s.d.). Using a fitted mixture model, we estimated the spike-detection false-discovery proportion to be 17 ± 13% across all neurons, and false-negative rate to be 28 ± 19% (Supplementary Fig. 7). After 1 h of continuous voltage imaging at 16 mW/mm 2 , the spike SNR decreased to 76 ± 13% of its initial value (Supplementary Fig. 8). To facilitate comparisons between cells, we normalized the signal for each cell by its mean initial spike height (Methods). Thus, all fluorescence signals are reported in units of Spike Height (SH). This measure does not readily convert to mV on account of the slightly nonlinear and non-instantaneous response of the voltage indicator and finite exposure time of the camera, which together blunted spike heights relative to slower subthreshold voltages.
257:L1 NDNF interneurons have two gene
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "wave propagation|3\.5 times|traveling|travelling" 10.64898-2026.10.05.756595.txt | head; echo ----; grep -n -i -E "detection probability|near detection cutoff|IPSP duration|durations were" 10.64898-2026.10.05.756595.txt | head
```

```
35:Population voltage recordings also revealed broadly correlated subthreshold activity and traveling waves, alongside more localized and more transient spike synchrony. NPY-positive and NPY-negative populations had similar average subthreshold voltages but dramatically different spiking responses to whisking. These differences were traced to opposing behavioral state-dependent changes in the voltage-to-spiking relationships. Together, these findings illustrate how all-optical measurements of excitability, connectivity, and voltage dynamics can connect multiple levels of circuit function in vivo .
201:In the quiet state – but not the whisking state – the subthreshold dynamics often showed global oscillations between 1 and 10 Hz (Supplementary Fig. 21A). These oscillations corresponded to large-scale wave propagation (Movie 4). We tracked the wavefronts (Methods) and observed a variety of propagation directions and speeds (Supplementary Fig. 21D-H), with a slight bias toward the medial-posterior direction and an average speed of 18.2 ± 8.3 mm/s (mean ± s.d., n = 3858 events, 2 mice). For a typical 5 Hz oscillation, the wavelength was ∼4 mm (Supplementary Fig. 21H). Similar state-dependent oscillations have been reported by in vivo patch clamp studies in cortex 58 – 62 , and similar traveling wave dynamics have also been reported via local field potential and meso-scale GEVI and Ca 2+ recordings 63 – 65 .
307:Both patch clamp and local field potential (LFP) recordings previously reported state-dependent low-frequency oscillations 62 , 70 – 73 ; and traveling waves of brain activity have been reported in multiple species 74 . These prior measurements probed population ensemble activities measured either extracellularly as field potentials 63 , 75 , or optically via ensemble-average voltage imaging 70 , 71 . By measuring the subthreshold voltages at single-cell resolution, we unambiguously showed that traveling waves are collective traveling oscillations of membrane pot
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/001960/versions/0.261013.2016/assets/?page_size=100" -o assets.json; python3 -c "
import json;d=json.load(open('assets.json'))
for a in d['results']: print(a['path'],a['size'],a['asset_id'])
"; curl -s "https://api.dandiarchive.org/api/dandisets/001960/versions/0.261013.2016/" -o ver.json; python3 -c "
import json;d=json.load(open('ver.json'));print(d.get('name'));print(d.get('description')[:3000]);print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for id in 20f36138-2e20-4823-b80d-418bad0c65c4 d27cf030-acbe-476b-9026-6a8ef4cb0243; do curl -s "https://api.dandiarchive.org/api/assets/$id/" | python3 -c "
import json,sys;d=json.load(sys.stdin)
for k in ['variableMeasured','measurementTechnique','wasGeneratedBy','description']:
  print(k, json.dumps(d.get(k))[:1500])
"; echo ======; done
```

Result: the fetched text is not kept.

**Agent**

Checking a few helpers on synthetic inputs (conduction-speed fit grid, `matlab_prctile`, the length-constant fits, `spike_frames`).

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' 2>&1 | grep -v Warning
import numpy as np, sys, types
sys.modules['remfile']=types.ModuleType('remfile')
import l1opto as L
# matlab_prctile vs known MATLAB: prctile(1:10, 90) = 9.5 ; prctile(1:5,1)=1
print("prctile", L.matlab_prctile(np.arange(1,11),90), L.matlab_prctile(np.arange(1,6),1), L.matlab_prctile(np.arange(1,6),50))
# exp fits
r=np.arange(15,400,30.); p=0.3*np.exp(-r/105)
print("exp fits", L.exp_fit_least_squares(r,p)[1], L.exp_length_constant_loglinear(r,p))
# spike_frames
ts=np.arange(100)*1.27e-3; st=ts[[3,50,99]]+0.0004
print("spike_frames", L.spike_frames(st,ts))
# speed_fit copy from notebook
DT=1.27e-3
def speed_fit(traces):
    nT=traces.shape[0]; c0=nT//2; tau=np.arange(nT)-c0
    out=[]
    for i in range(traces.shape[1]):
        loc=np.zeros(nT); w=slice(max(0,c0-16),min(nT,c0+17)); loc[w]=traces[w,i]
        pk=int(np.argmax(loc)); ff=pk+np.arange(-2,5)
        co=np.polyfit(tau[ff],traces[ff,i],3); grid=np.linspace(-2,4,10000)
        out.append(grid[np.argmax(np.polyval(co,grid))])
    return np.array(out)
t=np.arange(281)-140
true=np.array([0.3,0.8,1.3,1.8,2.6,3.5])
tr=np.stack([np.exp(-(t-d)**2/(2*1.0**2)) for d in true],1)
print("true delays", true, "fit", speed_fit(tr).round(2))
# chunk guard
print("chunk_guard", np.nonzero(L.chunk_guard(30,10,1))[0])
EOF
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls /home/runner/work/encore 2>/dev/null; which -a python3 python; ls ~/.local/bin 2>/dev/null | head; uv --version 2>/dev/null; pip --version 2>/dev/null
```

```
encore
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/python
/usr/bin/python
/bin/python
uv 0.13.7 (x86_64-unknown-linux-gnu)
pip 26.2.2 from /opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/pip (python 3.13)
```

**Agent calls Bash**

```bash
for p in /usr/bin/python3; do $p -c "import numpy, scipy; print(numpy.__version__, scipy.__version__)"; done 2>&1; cd $TMPDIR && uv venv -q v 2>&1 | tail -1 && uv pip install -q -p v numpy scipy h5py requests 2>&1 | tail -2; ls v/bin | head -3
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy, scipy; print(numpy.__version__, scipy.__version__)
    ^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'numpy'
activate
activate.bat
activate.csh
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF' 2>&1 | grep -v Warning
import numpy as np, sys, types
sys.modules['remfile']=types.ModuleType('remfile')
import l1opto as L
print("prctile", L.matlab_prctile(np.arange(1,11),90), L.matlab_prctile(np.arange(1,6),1), L.matlab_prctile(np.arange(1,6),50))
r=np.arange(15,400,30.); p=0.3*np.exp(-r/105)
print("exp fits", L.exp_fit_least_squares(r,p)[1], L.exp_length_constant_loglinear(r,p))
ts=np.arange(100)*1.27e-3; st=ts[[3,50,99]]+0.0004
print("spike_frames", L.spike_frames(st,ts))
def speed_fit(traces):
    nT=traces.shape[0]; c0=nT//2; tau=np.arange(nT)-c0
    out=[]
    for i in range(traces.shape[1]):
        loc=np.zeros(nT); w=slice(max(0,c0-16),min(nT,c0+17)); loc[w]=traces[w,i]
        pk=int(np.argmax(loc)); ff=pk+np.arange(-2,5)
        co=np.polyfit(tau[ff],traces[ff,i],3); grid=np.linspace(-2,4,10000)
        out.append(grid[np.argmax(np.polyval(co,grid))])
    return np.array(out)
t=np.arange(281)-140
true=np.array([0.3,0.8,1.3,1.8,2.6,3.5])
tr=np.stack([np.exp(-(t-d)**2/(2*1.0**2)) for d in true],1)
print("true delays", true, "fit", speed_fit(tr).round(2))
print("chunk_guard", np.nonzero(L.chunk_guard(30,10,1))[0])
# CrossedLMM: synthetic crossed design, check variance recovery
rng=np.random.default_rng(0)
npre,npost,n=150,150,1200
pre=rng.integers(0,npre,n); post=rng.integers(0,npost,n)
y=1+rng.normal(0,np.sqrt(0.15),npre)[pre]+rng.normal(0,np.sqrt(0.05),npost)[post]+rng.normal(0,np.sqrt(0.14),n)
X=np.ones((n,1))
f=L.CrossedLMM(y,X,pre,post).fit()
print("LMM true 0.15/0.05/0.14 ->", round(f['s2_pre'],3), round(f['s2_post'],3), round(f['s2_resid'],3), f['converged'])
EOF
```

```
prctile 9.5 1.0 3.0
exp fits 105.00000000000001 104.99999999999996
spike_frames [ 3 50 99]
true delays [0.3 0.8 1.3 1.8 2.6 3.5] fit [-0.08  0.58  0.92  1.58  2.45  3.11]
chunk_guard [ 0  1  9 10 11 19 20 21 29]
LMM true 0.15/0.05/0.14 -> 0.168 0.048 0.145 True
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF'
import numpy as np
t=np.arange(281)-140
for w in (1.0,1.5):
  for d in [0.3,0.8,1.3,1.8,2.6]:
    y=np.exp(-(t-d)**2/(2*w**2)); pk=int(np.argmax(np.where(abs(t)<=16,y,-1))); ff=pk+np.arange(-2,5)
    co=np.polyfit(t[ff],y[ff],3)
    g_abs=np.linspace(-2,4,10000); g_rel=t[pk]+np.linspace(-2,4,10000)
    print(w,d, "abs grid", round(g_abs[np.argmax(np.polyval(co,g_abs))],2), "grid around peak", round(g_rel[np.argmax(np.polyval(co,g_rel))],2))
EOF
```

```
1.0 0.3 abs grid -0.08 grid around peak -0.08
1.0 0.8 abs grid 0.58 grid around peak 0.58
1.0 1.3 abs grid 0.92 grid around peak 0.92
1.0 1.8 abs grid 1.58 grid around peak 1.58
1.0 2.6 abs grid 2.45 grid around peak 2.45
1.5 0.3 abs grid -0.02 grid around peak -0.02
1.5 0.8 abs grid 0.56 grid around peak 0.56
1.5 1.3 abs grid 0.98 grid around peak 0.98
1.5 1.8 abs grid 1.56 grid around peak 1.56
1.5 2.6 abs grid 2.41 grid around peak 2.41
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "dV/dt|d ?V ?/ ?d ?t|6 ms|after-?depolarization was|burst rate|10 ms before" 10.64898-2026.10.05.756595.txt | cut -c1-900 | head -20
```

```
221:Intrinsic properties and local connectivity shape network dynamics. (A) Optical rheobase affects excitability during spontaneous activity. Top: spike rates conditioned on subthreshold voltage, V , during optogenetic ramp stimulus, sorted by quintiles of optical rheobase, V R ℎ . Bottom: spike rates conditioned on V during spontaneous activity, sorted by quintiles of V R ℎ . (B) Spike-rate adaptation affects sensitivity to voltage upstroke velocity during spontaneous activity. Top: mean spike rate during optogenetic step stimulation, sorted by quintiles of spike-rate adaptation ( ADPT ). Bottom: spike rates conditioned on dV / dt during spontaneous activity, sorted by quintiles of ADPT . (C) Spike after-depolarization affects bursting during spontaneous activity. Top: mean STA waveform, sorted by quintiles of spike afterdepolarization, V adp . Bottom: Spike autocorrelograms during spo
227:(B) Spike-rate adaptation affects sensitivity to voltage upstroke velocity during spontaneous activity. Top: mean spike rate during optogenetic step stimulation, sorted by quintiles of spike-rate adaptation ( ADPT ). Bottom: spike rates conditioned on dV / dt during spontaneous activity, sorted by quintiles of ADPT .
239:Under step-wise optogenetic stimulation, cells showed variable amounts of spike-rate adaptation ( Fig. 2A ), a feature not captured by the simple excitability curves calculated in Fig. 5A . Spike-rate adaptation captures the degree to which the cell acts as a high-pass filter, converting a step input into a transient output. We thus hypothesized that spike-rate adaptation might correlate with response to the rate of upswing of the subthreshold voltage, dV/dt. We divided the cells into five bins of spike-rate adaptation under step-wise optogenetic stimulation, and for each bin we calculated the mean conditional firing rate as a function of dV/dt during quiet-state spontaneous activity. Cells with higher spike-rate adaptation preferentially spiked in response to r
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "P\(spk ?\| ?V\)|conditioned on (the )?subthreshold|preceding 10|10 ms" 10.64898-2026.10.05.756595.txt | cut -c1-700 | head; grep -n -i "Effect of connections" -A4 10.64898-2026.10.05.756595.txt | cut -c1-1500 | head -12
```

```
175:Threshold nonlinearities and private excursions block correlation transfer from subthreshold to spikes. (A) Fluorescence recordings were split into subthreshold and spiking traces. Subthreshold voltages (top) showed population-wide correlations, whereas spiking (bottom) was less correlated. (B) Mean subthreshold cross-correlation functions resolved by pairwise distance (quiet state). Each plot corresponds to a 60 μm-wide bin. Cell pairs in the 0 – 60 μm bin were omitted due to fluorescence scatter. (C) Mean spike-rate cross-correlograms, resolved by pairwise distance (quiet state). Bins are as in (B). (D) Distance-dependent decay of subthreshold equal-time cross-correlation (left axis) a
187:(E) Histograms of subthreshold voltage at (top) all times and (bottom) 10 ms interval prior to spikes.
191:(G) Probability distributions of subthreshold voltage of cell j conditioned on the subthreshold voltage of cell i for all ( i , j ) pairs < 200 μm apart. n = 505 cells, N = 2 mice. Red line has slope of 1.
209:First, for each cell, we determined an empirical voltage-to-spike relationship from the spontaneous activity data. We calculated the distribution of all subthreshold voltages during spontaneous activity; and the distribution of subthreshold voltages in the 10 ms preceding spike times (Methods, Fig. 4E ). The ratio of these two distributions yielded an estimate of the conditional spike rate as a function of subthreshold voltage, i.e. the voltage-to-spike relationship. To avoid arousal-related effects, we only used quiet state epochs for this analysis. These curves all had a characteristic sigmoidal shape, with substantial cell-to-cell variations in threshold and maximum firing rate ( Fig.
221:Intrinsic properties and local connectivity shape network dynamics. (A) Optical rheobase affects excitability during spontaneous activity. Top: spike rates conditioned on subthreshold voltage, V , during optogenetic ramp stimulus, sorted by quintiles of optical rheobase, V R ℎ
[... 8 more lines not kept]
```

**Agent**

**Verifier report, round 1: Qi et al. 2026, DANDI:001960 v0.261013.2016**

The claims file has 56 claims. The attempt tests 45 and blocks 11, across three notebooks (`qi2026_excitability_connectivity` = EC, `qi2026_spontaneous` = SP, `qi2026_excitability_spontaneous` = ES). My outcomes: 31 reproduced, 7 partially reproduced, 5 not reproduced, 13 blocked.

### A. Outcomes

| claim id | my outcome | reason |
|---|---|---|
| jf608-brighter | blocked (data_missing) | The archive API lists 7 assets (3 sessions × 2 mice plus a raw excerpt). There is no JF585/JF608 comparison. |
| targeting-signal-to-background | blocked (data_missing) | There are no wide-field and targeted images of the same field. The excerpt is a targeted-illumination movie. |
| spike-snr-and-detection-errors | not_reproduced | SNR (1/noise) is 3.18–3.45 under every reading (SP cell 6), below 4.5 ± 0.7. The Methods' definition (s.d. of the 1-frame difference, no √2) matches the notebook's. The false-discovery and false-negative rates were not computed. |
| snr-decay-one-hour | reproduced | Mean of ratios is 72.9% (QC) and 77.3% (all); ratio of means is 69.8% and 73.4%. All are within 76 ± 13 (SP cell 8). |
| fig1d-stimulation-fold-change | blocked (data_missing) | No 76-cell periodic-stimulation session in the asset list. |
| off-target-length-constants | blocked (data_missing) | No lattice experiment. |
| l1-sampling-density | blocked (data_missing) | No z-stack, only a GFP maximum projection. |
| adaptation-vadp-correlation | reproduced | Reading (a): R = 0.232, p = 4.5e-8, n = 543 (EC cell 13). |
| fig2c-three-bins | reproduced | Cluster sizes are exactly {94, 110, 116} (EC cell 15). |
| fig2gk-bin-profiles | reproduced | 8 of 8 orderings hold under both readings (EC cell 17). |
| two-mice-intrinsic-distributions | blocked (methods_underspecified) | The named readings disagree: all cells give 4/5 (time constant p = 0.101), QC cells give 5/5 (time-constant p = 0.048). The header rule therefore blocks it. See problem 5. |
| synaptic-connection-counts | reproduced | 802/7280 and 667/7032 in 60–400 µm (828/7426 and 679/7150 within 400 µm). Per cell: 2.62 out, 25.3 tested, 10.8% (EC cell 21). |
| ipsp-median-amplitude | partially_reproduced | The pooled median IPSP of −0.0297 is within tolerance. The cross-STA fluctuation averages 0.234 (0.217 and 0.250 per mouse) against 0.20 ± 0.02 (EC cell 23). |
| detection-limits | blocked (other) | Blocked as methods_underspecified, but the claims file gives readings. What is missing is the per-pair statistic or null, which could be rebuilt from stored data (problem 3). |
| gap-junction-connection-counts | reproduced | 3553 and 2199; 9.99 out, 9.99 in, 40.9%; median spikelet 0.0120 (EC cell 25). |
| hadamard-stimulation-rates | reproduced | 26.5 Hz on, 3.6 Hz off, 12,929 evoked spikes. There are 650 stimuli if "stimuli" means 750 ms on-steps (the Methods' step); 360 if it means on-blocks (EC cell 27). |
| spikelet-not-scatter | blocked (too_large) | The excerpt is 356.8 GB (API), but a subset of frames would allow a partial test (problem 10). |
| highmag-footprint | blocked (data_missing) | No 7.5× recordings. |
| lasso-off-target-correction | blocked (other) | The stated block reason is wrong: 1755 = 955 + 800 stored synaptic flags, the penalty readings are in the claims file, and per-trial responses can be derived from the stored data (problem 2). |
| connection-distance-structure | partially_reproduced | Probabilities 23.5% and 83.0% match; gap-junction λ under (b) is 156–161 µm. Synaptic λ is 151–362 µm under every reading against 105, and M-YQ0201-29 out-degree fits a power law better (EC cell 30). |
| fig3eg-amplitude-falls-with-distance | reproduced | Nearest bin median exceeds farthest for both measures in both mice; Spearman ρ < 0, p ≪ 0.05 (EC cell 32). |
| fig3h-conduction-speed | reproduced | Pooled 0.265 m/s, within 0.28 ± 0.028 (EC cell 34). |
| amplitudes-log-normal | not_reproduced | Spikelet log-skew is 0.73, above 0.5 (EC cell 36). The selection deviates from the claims file, so this is provisional (problem 4). |
| interaction-kernel | not_reproduced | Peak 33.0 ms is in range, but the decay of 39.4 or 47.9 ms, FWHM 22.7 ms and λ of 72 or 96 µm are all outside tolerance (EC cell 38). |
| fig3jk-presynaptic-sets-amplitude | reproduced | R = 0.609 and 0.263, n = 497 and 482: exact (EC cell 40). |
| fig3mn-postsynaptic-sets-decay | reproduced | Incoming R = 0.330 (p = 4.7e-18); outgoing R = 0.075, p = 0.056 (EC cell 40). |
| fig3lo-variance-components | reproduced (fragile) | Amplitude pre > post in 100%; decay post > pre in 99.95% of converged refits. Non-converged refits were excluded (problem 6). |
| gap-junction-no-identity-effect | not_reproduced | R = 0.214, 0.298, 0.268, 0.314; three of four are ≥ 0.26 (EC cell 44). |
| subthreshold-correlation-length | reproduced | 0.638 / 0.518; 2.42 / 4.03 mm (SP cell 10). |
| subthreshold-low-dimensional | reproduced | Reading (a), averaged: 70.7% quiet, 67.5% whisking, quiet > whisking (SP cell 12). |
| quiet-state-oscillations | reproduced | Quiet/whisking 1–10 Hz power ratio is 4.94 and 2.92 (SP cell 14). |
| traveling-waves | blocked (other) | No analysis was run although the data and a Methods procedure exist (problem 1). |
| spike-synchrony-localized | partially_reproduced | Reading (a): 277.1 and 270.7 µm, half-width 2.54 ms. FWHM averaged over mice is 71.1 ms against 80 ± 8 (M-YQ0201-27 alone, 78.7, would pass) (SP cell 17). |
| voltage-to-spike-sigmoid | reproduced (marginal) | At the spike frame, 52% of cells have R² ≥ 0.9 and both CVs are > 0.2 (SP cell 19). The Methods (V(t_s)) and the code agree on this reading; the −8-frame variant fails at 24%. |
| fig4g-private-depolarizations | reproduced | Slope ratio 2.89 pooled (SP cell 21). |
| fig4hi-self-sta-diverges | reproduced | Increase 0.176 and 0.182 against s.d. 0.015 and 0.007; self above cross at −30 ms (SP cell 23). |
| fig5a-rheobase-predicts-spontaneous-excitability | reproduced | ρ = −1.00 in both conditions for M-YQ0201-27 code bins (ES cell 5). |
| supp22-rheobase-correlations | reproduced | Reading (a): R = −0.573 and −0.311, n = 543 (ES cell 7). |
| fig5b-adaptation-dvdt | reproduced | R = 0.274 (Methods reading) and 0.262 (code reading); M-YQ0201-27 top bin is highest (ES cell 9). |
| fig5c-adp-bursting | reproduced | Main reading R = 0.546 (ES cell 11). |
| fig5e-inhibition-in-spontaneous-voltage | partially_reproduced | Under (c), −0.0213 and −0.0095 with p ≪ 0.05. The controls' +1% rise is not matched: control medians are 0.003–0.008, means 0.012–0.019 (EC cell 46). |
| fig5e-inhibition-in-spontaneous-rate | partially_reproduced | Under (a), rates are 0.190 and 0.083 Hz, but spikes lost fail under every reading (EC cell 46). |
| fig5g-gap-junction-synchrony | partially_reproduced | Under (a), 0.80 and 0.29 Hz, but spikes gained (0.0022 and 0.0009) fail (EC cell 46). |
| inhibition-gap-balance | blocked (methods_underspecified) | Readings give ratios of 6.96, inf, 1.37 and −0.19 (EC cell 48); reading (c) gives about 1.96. Its inputs did not reproduce. |
| npy-fraction-and-similarity | reproduced | NPY+ counts are within tolerance in every session; SNR and rate similar; KS p ≥ 0.08 (SP cell 25). |
| npy-intrinsic-differences | reproduced | 5 of 5 at p ≤ 0.001 (EC cell 51). |
| npy-classifier | reproduced | 76.8% against chance 50.0% (paper: 78% against 50% [46, 55]; the notebook's chance CI is [42.2, 57.5]). V_adp is top under both readings (EC cell 53). |
| npy-connection-probability | reproduced | 13.7% against 7.4%, n = 307 and 269, p = 1.4e-9 (EC cell 55). |
| npy-ipsp-amplitude | reproduced | −0.0372 (977 pairs) against −0.0311 (490 pairs), p = 8e-7: counts exact (EC cell 55). |
| npy-ipsp-duration | reproduced (fragile) | QC 60–400 µm: 77.4 against 65.2 ms, n = 760 and 709, p = 3e-13. The NPY− count is just inside 646 ± 65 (problem 13). |
| npy-gap-junction-no-difference | not_reproduced | Consistent-direction outgoing effects in probability and spikelet amplitude, and incoming effects in amplitude (EC cell 57). |
| npy-subthreshold-similar | reproduced | M-YQ0201-29: R = 0.973, slope 0.933 or 1.015 (SP cell 27). |
| npy-umap-groups | reproduced | Medians over seeds 158.5/205 and 201/300; Fisher p ~1e-23 (SP cell 29). |
| npy-whisking-onset-rates | reproduced | NPY+ 1.06 → 2.20 Hz (p = 6e-8); NPY− 1.27 → 1.50 Hz (p = 0.76) (SP cell 31). |
| npy-oscillation-peak-rates | blocked (methods_underspecified) | Reading (b) passes. Reading (a) fails because the voltage differs (p = 0.022) (SP cell 33). |
| npy-state-dependent-excitability | reproduced | All four comparisons hold at p ≤ 0.05 (SP cell 35). |

### B. Problems

1. **[affects a conclusion]** SP cell 15, traveling-waves: blocked with no analysis run. The voltage, coordinates and masks are already in memory, and the Methods give events, the speed slope and the phase-gradient direction. The open details should have been run under the readings the paper allows.
2. **[affects a conclusion]** EC cell 28, lasso-off-target-correction: the block reason is factually wrong. 1755 equals the total stored synaptic flags (955 + 800, EC cell 6). The claims file gives the penalty readings. Per-trial evoked spikes and IPSP responses can be derived from `spike_times`, `blue_stimulation_per_cell` and `normalized_voltage`.
3. **[affects a conclusion]** EC cell 28, detection-limits: the notebook never lists the full contents of `analysis/pairwise_connectivity_metrics`, so whether per-pair statistics are stored is unchecked. The null (pulses aimed at cells more than 800 µm away) could be rebuilt from stored data for the ~200 pairs near the cutoff.
4. **[affects a conclusion]** EC cell 36, amplitudes-log-normal: it uses all stored flags (7443 spikelet pairs, including non-QC cells and pairs under 60 µm). The header requires QC cells and drops pairs under 60 µm from gap-junction analyses (5752 pairs). The excluded close pairs are the scatter-contaminated largest ones, and the log-skew of 0.73 is near the 0.5 cut.
5. **[affects a conclusion]** EC cells 5 and 19, two-mice-intrinsic-distributions: M-YQ0201-27 has 7 membrane time constants of exactly 0 (EC cell 5), which look like failed fits. They are kept as values in reading (a), where the time-constant p = 0.101; treating them as missing may make the two readings agree.
6. **[affects a conclusion]** EC cell 42 / `bootstrap_variances`, fig3lo-variance-components: the fractions count converged refits only (1971 and 1969 of 2000). For decay, 1 of 1969 already has pre > post, and the 99.9% threshold allows at most 2 of 2000. Two adverse non-converged refits out of 31 would flip it, and their variances are not shown.
7. **[affects a conclusion]** SP cell 5, spike-snr-and-detection-errors: it says the matched-filter output and mixture fit are not stored. The raw-excerpt asset's DANDI metadata says it holds "the demixing and spike-finding products"; the excerpt's contents were not checked for them.
8. **[affects a conclusion]** SP cell 19, voltage-to-spike-sigmoid: the pass is marginal (262 of 505 cells). The caption variant is implemented as one sample 8 frames before the spike, not the caption's "10 ms interval". The fitted maxima have CV 4.54, which means the tops are unconstrained extrapolations that pass the CV test by default.
9. **[affects a conclusion]** EC cell 46, fig5e-inhibition-in-spontaneous-voltage: the controls' rise is never measured on the control-average waveform (`vsupp(cavg)`). Only medians and means of per-control values are printed.
10. **[affects a conclusion]** EC cell 28, spikelet-not-scatter: "too_large" assumes the whole 357 GB movie must be read. A subset of blocks or frames (at the measured ~45 MB/s, one block of ~90 GB) would give a scatter STA for a partial test.
11. **[does not affect a conclusion]** EC cell 38, interaction-kernel: the FWHM baseline is the median of lags outside ±40 frames on a trace with a slow hump, which gives 22.7 ms. The decay and λ fail anyway.
12. **[does not affect a conclusion]** EC cell 53, npy-classifier: features are z-scored on all cells before the train/test split (mild leakage).
13. **[affects a conclusion]** EC cell 55, npy-ipsp-duration: the header-consistent selection (QC cells, all flags within 400 µm, no 60 µm cut) was not run. It adds ~38 pairs and would likely push NPY− above 711. Means include fits capped at 0.4 s. No selection reproduces 699/646.
14. **[does not affect a conclusion]** SP cell 17, spike-synchrony-localized: averaging FWHM over mice is an unstated aggregation choice. M-YQ0201-27 alone meets all four values.
15. **[does not affect a conclusion]** Claims-file misreadings, reported not corrected:
    - voltage-to-spike-sigmoid says "the Methods/caption say V in the 10 ms before spikes". The Methods say V(t_s), the voltage at spike times; only the Results and the Fig. 4E caption say "10 ms".
    - fig5e-inhibition-in-spontaneous-voltage's criterion requires "both values" while its expected values list three quantities.
    - lasso-off-target-correction says the 1755 pairs are not given; they are the stored flags.
    - synaptic-connection-counts and npy-ipsp-amplitude cite "800" connections for M-YQ0201-27 in the 60–400 µm band. The data have 802 flags there, 800 of them with a finite amplitude.
16. **[does not affect a conclusion]** Helpers checked on synthetic inputs, all correct: `matlab_prctile` (9.5, 1, 3), both exponential fits (λ = 105 recovered), `spike_frames`, `chunk_guard`, and `CrossedLMM` (true 0.15/0.05/0.14, fitted 0.168/0.048/0.145). The speed-fit grid being absolute rather than peak-relative makes no difference for delays of 0–2.6 frames. The cubic over −2 to +4 frames has a sub-frame bias of up to −0.4 frames, which comes from the code's method.

### C. Could not check

- Any number against the data itself; I did not stream the files.
- Whether `analysis/pairwise_connectivity_metrics` and the raw excerpt hold per-pair p-values, nulls, matched-filter traces or mixture fits. A cell listing all their HDF5 datasets would settle problems 3 and 7.
- Problem 6: the share of pre > post (and post > pre) over all 2000 refits, non-converged ones included.
- Problem 5: two-mice-intrinsic-distributions rerun with time constant = 0 treated as missing.
- Problem 4: amplitudes-log-normal on QC pairs in 60–400 µm.
- Problem 13: npy-ipsp-duration on QC pairs within 400 µm, and with the fig3mn time-constant mask.
- Problem 9: `vsupp` of the weighted control average.
- The raw excerpt's HDF5 chunk layout and a timing for one block, to judge whether a subset test of spikelet-not-scatter is feasible.
- A run of traveling-waves under the Methods procedure with its open parameters varied.

## End of run

26 turns, 9 minutes, $3.21 at API prices, result: success.
