# 001261 · verifier-1 · run 41313381235

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 224
drwxr-xr-x 6 runner runner    4096 Nov  1 13:57 .
drwxr-xr-x 7 runner runner    4096 Nov  1 13:57 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 13:50 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 13:50 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  1 13:57 .claude
-rw-r--r-- 1 runner runner       0 Nov  1 13:57 .env
-rw-r--r-- 1 runner runner       0 Nov  1 13:57 .env.development
-rw-r--r-- 1 runner runner       0 Nov  1 13:57 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  1 13:57 .env.local
-rw-r--r-- 1 runner runner       0 Nov  1 13:57 .env.production
-rw-r--r-- 1 runner runner       0 Nov  1 13:57 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  1 13:57 .env.test
-rw-r--r-- 1 runner runner       0 Nov  1 13:57 .env.test.local
drwx------ 2 runner runner    4096 Nov  1 13:57 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 13:50 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 13:50 .github
-rw-r--r-- 1 runner runner       0 Nov  1 13:57 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 13:50 .idea
[... 37 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1002-cne.70001.yaml"
}
```

```
1	# Claims for Luo, Jiang, Desai et al. (2024), J. Comp. Neurol. 532, e70001, on dandiset 001261.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	#
5	# Text read: the version of record (open access, PMC11583843), as served by Europe PMC, in
6	# paper/10.1002-cne.70001.txt: Introduction, Materials and Methods, Results, Discussion, Table 1,
7	# the figure legends, and the supplement (CNE-532-e70001-s001.docx), whose legends are in the
8	# text file. There is no PDF, so the main figures (Figs. 2D, 4D, 7D and 9D, which show which
9	# features differ) could not be read. Four supplementary figures were read from the images in
10	# paper/10.1002-cne.70001.supp.docx, to see which features they mark as different: S2-2 (AP
11	# amplitude ***, CV-ISI **, sag **; AP width, upstroke and downstroke not marked), S4-1B (ten
12	# morphological features, none marked), S7-1 (AP amplitude **, CV-ISI ****, sag *, AP width **,
13	# upstroke ****, downstroke not marked) and S9-1B (seven morphological features, none marked).
14	#
15	# Code read: the analysis code the Methods link, doi:10.5281/zenodo.10975327, which is
16	# github.com/nsdesai/patch_clamp_analysis tag v1.0.1, commit 17a3265d280392e73916faee31ee9cea30500c7c
17	# (last modified 04/15/24). It holds 14 MATLAB functions that extract the electrophysiological
18	# features from one recording's current steps (analysis_of_neurophysiology_data.m calls
19	# sagpotential.m, inputresistance.m, rheobasecurrent.m, spikeproperties.m,
20	# afterhyperpolarization.m, ficurve.m, spikefrequencyadaptation.m), getindices.m (groups
[... 920 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "nbmsi.py"
}
```

```
1	"""Loading and electrophysiological features for dandiset 001261.
2	
3	Luo, Jiang, Desai et al. (2024), "Comparative Physiology and Morphology of BLA-Projecting NBM/SI
4	Cholinergic Neurons in Mouse and Macaque", J. Comp. Neurol. 532, e70001, doi:10.1002/cne.70001.
5	
6	Each NWB file holds one neuron: whole-cell current-clamp responses (`acquisition`,
7	CurrentClampSeries, volts, 10 kHz) to a family of current steps (`stimulus/presentation`, whose
8	values are in pA although the files label them amperes). The group of the neuron (species,
9	cholinergic or not) is in `session_description`. Files are read over HTTP into memory from the
10	archive at the pinned version; nothing is written to disk.
11	
12	Where the parameters come from. The claims file (claims/001261/10.1002-cne.70001.yaml, opening
13	comment, "Feature definitions F1 to F18") fixes each feature from Methods 2.5 and the paper's code,
14	github.com/nsdesai/patch_clamp_analysis at commit 17a3265d280392e73916faee31ee9cea30500c7c
15	(doi:10.5281/zenodo.10975327). Details it does not give are taken as follows:
16	
17	- Step onset and the 500 ms analysis window: the code (analysis_of_neurophysiology_data.m) finds
18	  the step from the largest current step and analyses only its first 500 ms. Here the onset is
19	  read from each sweep's own stimulus.
20	- Steps above 200 pA are left out: Methods 2.4, "a family of current steps (500 ms duration, -60
[... 536 more lines not kept]
```

**Agent**

Now the notebook.

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_luo_2024.ipynb'))
for i,c in enumerate(nb['cells']):
    print('=== CELL',i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--- OUT:'); print(''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--- OUT:'); print(''.join(d['text/plain']))
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1327 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	=== CELL 0 markdown
2	# Reproducing Luo, Jiang, Desai et al. (2024) from dandiset 001261
3	
4	**Paper.** Luo F, Jiang L, Desai NS, Bai L, Watkins GV, Eldridge MAG, et al. (2024). Comparative
5	physiology and morphology of BLA-projecting NBM/SI cholinergic neurons in mouse and macaque.
6	*J. Comp. Neurol.* 532, e70001. [doi:10.1002/cne.70001](https://doi.org/10.1002/cne.70001). The
7	claims file was written from the version of record (open access, PMC11583843), with its supplement.
8	
9	**Dandiset.** [DANDI:001261](https://dandiarchive.org/dandiset/001261/0.250917.2023), version
10	0.250917.2023. The paper cites no version (its Data Availability Statement gives only
11	https://dandiarchive.org/). This is the only published version, so it is pinned. The draft holds
12	the same 152 files (same checksums); it differs only in metadata (contributors, a related resource,
13	and the like), none of which the analysis uses. Files are read over HTTP into memory, not to disk.
14	
15	**What the dandiset holds.** One NWB file per neuron: whole-cell current-clamp responses to a
16	family of current steps, at 10 kHz, from mice and macaques, with the group of the neuron (species,
17	cholinergic or not) in `session_description`. It holds no morphology, no quality-control measures
18	and no slice identifiers.
19	
20	**Code.** The features follow the claims file, which takes them from Methods 2.5 and the paper's
[... 864 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 885
}
```

```
885	> A UMAP of the 18 electrophysiological features separates mouse cholinergic from
886	> noncholinergic BLA-projecting neurons almost completely, with only two neurons on the wrong
887	> side of the boundary.
888	
889	UMAP procedure U of the claims file on the 17 computable features (Methods readings), 10 seeds, 1000
890	label permutations per seed, under both readings of missing values.
891	=== CELL 35 code
892	U17 = ["sag", "rin", "tau", "rheobase", "threshold", "amplitude", "width", "latency", "upstroke", "downstroke", "ahp_amp", "ahp_latency", "ahp_width", "fi_slope", "max_rate", "adaptation", "cv_isi"]
893	def umap_runs(mask, ylab, seed):
894	    rng = np.random.default_rng(seed)
895	    X = feat.loc[mask, U17].to_numpy(float)
896	    y = (feat.loc[mask, "grp"] if ylab == "grp" else feat.loc[mask, "species"]).to_numpy()
897	    out = {}
898	    for miss in ["drop", "impute"]:
899	        out[miss] = nbmsi.umap_separation(X, y, miss, range(10), 1000, rng)
900	    return out
901	
902	t0 = time.time()
903	u_mouse = umap_runs(M, "grp", 20)
904	for miss, r in u_mouse.items():
[... 424 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "afterhyperpolar|AHP|adaptation index|maximal current|resting membrane|time constant|input resistance|step|rank|shuffl|Data Availab" 10.1002-cne.70001.txt | head -80
```

```
<persisted-output>
Output too large (84.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/24f81f7c-6ddd-4f43-ac92-e45021199644/tool-results/be4t4lumx.txt

Preview (first 2KB):
7:pmc J Comp Neurol J Comp Neurol 379 blackwellopen 0406041 CNE The Journal of Comparative Neurology 0021-9967 1096-9861 pmc-is-collection-domain yes pmc-collection-title Wiley Open Access Collection PMC11583843 PMC11583843.1 11583843 11583843 39576005 10.1002/cne.70001 CNE70001 1 Research Article Research Article Comparative Physiology and Morphology of BLA‐Projecting NBM/SI Cholinergic Neurons in Mouse and Macaque Luo Feng https://orcid.org/0000-0002-4167-8980 1 [removed: an e-mail address] Jiang Li https://orcid.org/0000-0001-9010-2534 2 Desai Niraj S. 1 Bai Li 1 Watkins Gabrielle V. 1 Eldridge Mark A. G. 3 Plotnikova Anya S. https://orcid.org/0009-0000-2451-5939 3 Mohanty Arya 3 Cummins Alex C. 3 Averbeck Bruno B. 3 Talmage David A. 2 Role Lorna W. 1 [removed: an e-mail address] 1 Section on Circuits, Synapses, and Molecular Signaling National Institute of Neurological Disorders and Stroke, National Institutes of Health Bethesda Maryland USA 2 Section on Genetics of Neuronal Signaling, National Institute of Neurological Disorders and Stroke, National Institutes of Health Bethesda Maryland USA 3 Laboratory of Neuropsychology National Institute of Mental Health, National Institutes of Health Bethesda Maryland USA * Correspondence: Lorna W. Role ( [removed: an e-mail address] ) | Feng Luo ( [removed: an e-mail address] ) 22 11 2024 11 2024 532 11 475575 10.1002/cne.v532.11 e70001 20 10 2024 13 8 2024 06 11 2024 22 11 2024 23 11 2024 23 09 2026 Published 2024. This article is a U.S. Government work and is in the public domain in the USA. The Journal of Comparative Neurology published by Wiley Periodicals LLC. https://creativecommons.org/licenses/by-nc/4.0/ This is an open access article under the terms of the http://creativecommons.org/licenses/by-nc/4.0/ License, which permits use, distribution and 
[... 2 more lines not kept]
```

**Agent**

Text is one long line; extract snippets.

**Agent calls Bash**

```bash
cd paper; python3 - <<'E'
import re
t=open('10.1002-cne.70001.txt').read()
for pat in [r"Electrophysiological features",r"\(12\)",r"\(14\)",r"\(16\)",r"\(17\)",r"Resting membrane",r"Data Availab",r"Neurolucida|Imaris",r"quality control|access resistance"]:
    for m in list(re.finditer(pat,t))[:2]:
        print('###',pat,':',t[max(0,m.start()-200):m.start()+900].replace('\n',' '));print()
E
```

```
### Electrophysiological features :  plots constructed from the rheobase current step were also used to illustrate differences in action potential kinetics (Figures 2B and S2‐1B ). The results are shown in Figures 2 and S2‐2 . FIGURE 2 Electrophysiological features consistent with the lower excitability of mouse cholinergic BLA‐projecting NBM/SI neurons compared with neighboring noncholinergic BLA‐projecting NBM/SI neurons. See Figures S2‐1 and S2‐2 . A. Sample traces at rheobase (left) and at maximum current injection (right; 200 pA) are shown for typical BLA‐projecting NBM/SI neurons (cholinergic: teal; noncholinergic: gray). B. Average phase plots illustrate differences in action potential kinetics comparing BLA‐projecting NBM/SI neurons (cholinergic: teal; noncholinergic: gray). C. Nondimensional (UMAP) plot of all 18 electrophysiological features comparing BLA‐projecting NBM/SI neurons (cholinergic: teal; noncholinergic: gray). D. Population scatter plus box plots of all data for the 12 features that most strongly distinguish BLA‐projecting NBM/SI cholinergic neurons ( n = 48) from their neighboring BLA‐projecting

### \(12\) : 0) upstroke (mV/ms), the maximum value of dV / dt on the upstroke of the first action potential; (11) downstroke (mV/ms), the minimum value of dV / dt on the downstroke of the first action potential; (12) afterhyperpolarization potential (AHP) amplitude (mV), measured after the first action potential and defined as the difference between threshold and the minimum potential 100 ms later; (13) AHP latency (ms), the time after spike threshold is crossed by the first action potential and the AHP minimum; (14) AHP width (ms), the time difference at half maximum of the first AHP; (15) f – I slope (Hz/pA), the slope of the initial linear section of the f – I curve; (16) max firing rate (Hz), the maximum firing rate produced by a current step between 0 and 200 pA, across the entire 500‐ms duration; (17) adaptation index (dimensionless), for the 
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/001261/versions/0.250917.2023/" -o v.json && python3 -c "
import json;d=json.load(open('v.json'))
print(json.dumps(d.get('assetsSummary'),indent=1)); print(d.get('description')); print([ (r.get('relation'),r.get('url'),r.get('name')) for r in d.get('relatedResource',[])])"
curl -s "https://api.dandiarchive.org/api/dandisets/001261/versions/0.250917.2023/assets/?page_size=1000" -o a.json && python3 -c "
import json,collections;d=json.load(open('a.json'));r=d['results'];print(d['count']);
print(collections.Counter(x['path'].rsplit('.',1)[-1] for x in r)); print(sorted(set(x['path'].split('/')[0] for x in r))[:60])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for q in "cne.70001" "NBM%2FSI" "BLA-projecting" "39576005"; do curl -s "https://api.dandiarchive.org/api/dandisets/?search=$q&page_size=50" | python3 -c "import json,sys;d=json.load(sys.stdin);print('$q',[(x['identifier'],(x.get('most_recent_published_version') or x['draft_version'])['name']) for x in d['results']])"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np
from scipy.stats import ranksums, mannwhitneyu
C={20.0: 4, 25.0: 1, 30.0: 5, 40.0: 8, 45.0: 2, 50.0: 1, 55.0: 1, 60.0: 4, 80.0: 7, 85.0: 1, 100.0: 4, 120.0: 1, 130.0: 1, 140.0: 1}
N={10.0: 3, 15.0: 1, 20.0: 8, 30.0: 7, 35.0: 1, 40.0: 12, 50.0: 7, 60.0: 2, 100.0: 1, 150.0: 1, 200.0: 1}
a=np.repeat(list(C),list(C.values()));b=np.repeat(list(N),list(N.values()))
print(len(a),len(b),a.mean(),b.mean(),ranksums(a,b).pvalue, mannwhitneyu(a,b,method='asymptotic',use_continuity=True).pvalue)
# synthetic: per-sweep onset when test pulse precedes step
i=np.zeros(20000); i[1000:1500]=-20; i[3000:8000]=100
nz=np.flatnonzero(i); print('amp',np.median(i[nz]),'onset sample',nz[0],'dur ms',nz.size*0.1)
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls -d .venv */.venv 2>/dev/null; which -a python3 uv pip 2>/dev/null; (uv run --no-project --with numpy --with scipy python -c "print(1)" 2>&1 | tail -2)
```

```
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.17/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.17/x64/bin/pip
/usr/bin/pip
/bin/pip
Installed 2 packages in 35ms
1
```

**Agent calls Bash**

```bash
cd  uv run -q --no-project --with numpy --with scipy python -c "
import numpy as np
from scipy.stats import ranksums, mannwhitneyu
C={20.0: 4, 25.0: 1, 30.0: 5, 40.0: 8, 45.0: 2, 50.0: 1, 55.0: 1, 60.0: 4, 80.0: 7, 85.0: 1, 100.0: 4, 120.0: 1, 130.0: 1, 140.0: 1}
N={10.0: 3, 15.0: 1, 20.0: 8, 30.0: 7, 35.0: 1, 40.0: 12, 50.0: 7, 60.0: 2, 100.0: 1, 150.0: 1, 200.0: 1}
a=np.repeat(list(C),list(C.values()));b=np.repeat(list(N),list(N.values()))
print(len(a),len(b),a.mean(),b.mean(),'ranksums',ranksums(a,b).pvalue,'tie-corrected',mannwhitneyu(a,b,method='asymptotic',use_continuity=True).pvalue)
i=np.zeros(20000); i[1000:1500]=-20; i[3000:8000]=100
nz=np.flatnonzero(i); print('amp',np.median(i[nz]),'onset sample',nz[0],'dur ms',nz.size*0.1)
"
```

```
41 44 59.63414634146341 42.04545454545455 ranksums 0.002342471832234102 tie-corrected 0.0021385964984600154
amp 100.0 onset sample 1000 dur ms 550.0
```

**Agent**

**Verifier report, round 1: Luo et al. 2024 (doi:10.1002/cne.70001) on DANDI:001261 v0.250917.2023**

The claims file has 29 claims. The notebook tests 18 and treats 11 as blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| sample-sizes | partially_reproduced | Cell 3 matches on files: 48 mouse C, 46 mouse NC, 46 macaque C, 27 mice, 9 macaques, and the sexes match Table 1. Cell 5 shows one of the 46 NC files is the same trace, sample for sample, as a C file (CG608_FL_S4C7). That leaves 45 distinct NC recordings, and the criterion's tolerance is 0. Slices are not recorded in the files. |
| fig2-mouse-c-nc-15-of-18 | not_reproduced | F1 can't be computed, so the range is 13 to 15 of 17. Cell 21 gives 11 or 12 under every reading (and with the last sweep of a repeat). Sag, AHP latency and, under reading a, adaptation also fail to differ. |
| fig2d-mouse-max-firing-rate | partially_reproduced | p = 1.1e-12 with NC higher. Both means fall just outside tolerance: C 6.33 against 6.57 to 8.03, NC 34.8 against 35.1 to 42.9 (cell 23). |
| fig2d-mouse-threshold-rheobase | partially_reproduced | Threshold holds: p = 6.4e-4, means -33.2 and -36.8 within tolerance. Rheobase has both means within tolerance (59.6, 42.0), but p = 2.3e-3 does not reach p < 0.001 (cell 25). Tie correction does not change this; I checked it at 2.1e-3. |
| fig2d-mouse-ahp | not_reproduced | AHP amplitude has p = 3.7e-12, but the NC mean is 16.35 against 12.4 ± 1.24. AHP width under the Methods window is reversed: C 158.9, NC 226.3, p = 0.02 (the window-only reading is also reversed, p = 2.6e-5). The tests do not hold, so this is not even partial. The code's window does reproduce it: 29.7 / 12.1 mV and 180.8 / 77.4 ms (cell 27). |
| fig2d-mouse-adaptation | reproduced | Under reading b (step with the most spikes): p = 0.011, C higher, means 0.884 and 0.606, both within tolerance. Reading a gives p = 0.68 (cell 29). |
| fig2d-mouse-passive | not_reproduced | F1 can't be computed (file names give it for only 8 of 48 C neurons, p = 0.35). Tau has p = 6.7e-5 in the right direction, but the means are far outside tolerance: C 60.95 against 34.6 ± 3.46, NC 28.6 against 22.3 ± 2.23 (cell 31). |
| figs2-2-mouse-amplitude-cv-sag | partially_reproduced | Amplitude: p = 1.6e-4, C larger. CV: p = 2.6e-3 under the most-spikes reading, C lower. Sag: p = 0.21, does not differ (cell 33). |
| fig2c-mouse-umap-separation | not_reproduced | The median count of misclassified neurons is 6 (drop) and 9.5 (impute), against at most 2, under both missing-value readings. It does beat every permutation (cell 35). |
| fig5a-mouse-lda-electrophysiology | reproduced | Accuracy is 1.00 (drop) and 0.936 (impute). That beats the 95th percentile of both shuffle types (about 0.75 to 0.78) and their maximum (at most 0.84), under both scalings (cell 37). |
| fig5b-mouse-lda-ahp-amplitude-top | reproduced | AHP amplitude ranks first under weight readings a and b and under both missing-value readings (cell 39). |
| fig7d-macaque-more-excitable | partially_reproduced | All three tests reach p < 1e-4 in the stated directions. Rheobase (22.5) and both f-I slopes (0.124 and 0.056) are within tolerance. Macaque maximum rate is 21.2 against 26.3 ± 2.63, outside tolerance (cell 41). |
| fig7d-macaque-threshold-ahp | partially_reproduced | Threshold (p = 3.5e-7, -39.6) and AHP amplitude (p = 5e-8, 20.5) hold. AHP width under the Methods window is 190.7 against 158.9, p = 0.27: wrong direction, not significant (cell 43). Two of three tests hold. |
| fig7-macaque-spike-width | not_reproduced | Means match (1.32 and 1.18), but p = 0.025 does not reach the criterion's p < 0.01 (cell 45). |
| figs7-1-macaque-amplitude-cv-sag-upstroke | partially_reproduced | Amplitude (p = 2.3e-3), CV (p = 3.2e-5 and 2.1e-6) and upstroke (p = 1.3e-5) hold, each larger in macaque. Sag gives p = 0.31. Downstroke differs (p = 0.015 under both F11 readings), which caps the claim at partial (cell 47). |
| fig7-macaque-mouse-feature-count | not_reproduced | 12 or 13 of 17 differ (cell 49). That is below the criterion's 14. The criterion does not lower the range when F1 is missing; if it were lowered as in the fig2 claim, 13 would sit on the edge. |
| fig7d-macaque-input-resistance | reproduced | Input resistance at -20 pA: macaque 584 against mouse 318 MΩ, p = 2.2e-5. Rheobase is lower in macaque, p = 8.6e-10 (cell 51). The code's slope variant gives p = 0.18, but it does not decide. |
| fig7c-macaque-mouse-umap-separation | blocked (methods_underspecified) | Reading b holds: every seed beats every permutation. Reading a fails: the median misclassified count is 9 and 10 (cell 53). The criterion assigns methods_underspecified to this case. |
| fig4d, figs4-1a, fig4c, fig5c, fig9-convex-hull, fig9-feature-count, fig9-branch-points, fig9c, fig10, fig10c, figs9-1a (11 claims) | blocked (data_missing) | I checked the archive: version 0.250917.2023 has 152 assets, all `.nwb`. The assets summary lists only CurrentClampSeries and CurrentClampStimulusSeries, and there are no related resources. A DANDI search (DOI, PMID, "NBM/SI", "BLA-projecting") finds only 001261. No part of these 11 claims can be tested. |

### B. Problems

1. [affects a conclusion, unverified] `nbmsi.load_file`: each sweep's onset is taken as `nz[0]`, the first non-zero stimulus sample. The -20 pA test pulse sits in the same sweep as the step. That is why the steps have 550 and 600 ms of non-zero samples (cell 7). Wherever the test pulse comes before the step, the 500 ms window is placed on the test pulse and the step is missed. I confirmed on a synthetic sweep that the amplitude (median) and the 550 ms duration still look normal in that case. This would explain the 8 "non-responsive" neurons in cells 9 and 10:
   - their steady state barely changes from the most negative to the largest step (-5 to 8 mV);
   - they fire no spikes;
   - the mouse C tau values are very large (CG250 401 ms, CG269 153 ms);
   - input resistance goes as low as -61 MΩ (cell 14).

   All 6 mouse neurons among them are cholinergic and come from one recording period, so the error is not random by group. They pull down the mouse C maximum rate (6.33, or 7.24 without them, which is within tolerance), inflate C tau, and leave 7 C neurons without spike features. They likely also change the fig2 and fig7 feature counts. The file-level onset `out["onset_s"]` (the largest step's first sample) is computed but never compared with the per-sweep onsets.
2. [affects a conclusion] Claims file, F12 to F14: the claims file makes the "Methods" AHP (rheobase step, 100 ms window) the deciding reading. Methods (12) only says "after the first action potential". The code's window reproduces the paper's numbers almost exactly: mouse 29.7 / 12.1 mV and 180.8 / 77.4 ms against 28.9 / 12.4 and 177.9 / 85.0; macaque 19.3 mV and 116 ms against 19.1 and 106.6. The Methods window reverses the AHP width direction. This is a likely misreading of what the paper computed. It decides fig2d-mouse-ahp and fig7d-macaque-threshold-ahp, and it affects the counts.
3. [affects a conclusion] `nbmsi._ahp_methods`: the main F14 searches for the half-level crossings to the end of the step. The claims file says "Window as in F12", which is closer to the `ahp_width_window` variant. The notebook states this as its own assumption, which is acceptable, and both readings give the same reversed direction. So this does not change an outcome, but the deciding reading is not the claims file's.
4. [affects a conclusion] Cell 14 drops the macaque file with the wrong scale (factor of 20) rather than rescaling it, and drops one NC copy of CG608. That gives 45 macaque C and 45 mouse NC against the paper's 46 and 46. The CG608 choice rests on "G+" in the file name, which is reasonable. Both are stated.
5. [does not affect a conclusion] `nbmsi.features`: F16 is capped at 200 pA, as Methods say. The code variant (macaque 23.8 ± 22.8) is closer to the paper's 26.3 ± 23.1 but still just outside tolerance.
6. [does not affect a conclusion] `ranksum_table` uses `scipy.stats.ranksums`, which has no tie correction, while MATLAB's ranksum has one. I checked rheobase: 2.34e-3 without the correction against 2.14e-3 with it.
7. [does not affect a conclusion] `lda_separation`: the 10-fold CV variant z-scores on all neurons before splitting, which leaks a little between training and test folds. It is a variant only.
8. [does not affect a conclusion] Sag: the claims file's rule for a saturated -60 pA step ("the next step up") is not implemented.
9. [does not affect a conclusion] Cell 21 `count()` counts a feature as differing without checking direction. AHP width is counted as differing at p = 0.02, but in the opposite direction to the paper.
10. [does not affect a conclusion] sample-sizes: the NC reading with ChAT-unknown neurons added is not addressed. The dataset has no such label, and the notebook does not say so.

### C. What I could not check

- Problem 1. I did not download the data. A per-sweep table of `onset_s` against the file onset (and against the stimulus's last non-zero run) for the 8 non-responsive neurons, plus a plot of one of their +200 pA sweeps showing both voltage and stimulus over the whole sweep, would settle it. If the onset is wrong, the feature table needs recomputing with the onset taken from the longest non-zero run.
- The tau fits. A plot or a fit-quality metric (R²) for the tau outliers above 150 ms would show whether these are failed fits or bad windows.
- `general/notes` and other per-file fields that might carry QC or slice information. The notebook prints `notes` into `info` but never displays it.
- UMAP parity with Meehan's run_umap. Only umap-learn with n_neighbors 15 and min_dist 0.3 was run, with no output showing that the outcome is insensitive to these parameters.

## End of run

14 turns, 3 minutes, result: success.
