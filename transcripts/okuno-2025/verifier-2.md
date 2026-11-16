# okuno-2025 · verifier-2 · run 43783253967

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 912
drwxr-xr-x 6 runner runner    4096 Nov 16 01:42 .
drwxr-xr-x 8 runner runner    4096 Nov 16 01:42 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 16 00:54 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 16 00:54 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 16 01:42 .claude
-rw-r--r-- 1 runner runner       0 Nov 16 01:42 .env
-rw-r--r-- 1 runner runner       0 Nov 16 01:42 .env.development
-rw-r--r-- 1 runner runner       0 Nov 16 01:42 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 16 01:42 .env.local
-rw-r--r-- 1 runner runner       0 Nov 16 01:42 .env.production
-rw-r--r-- 1 runner runner       0 Nov 16 01:42 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 16 01:42 .env.test
-rw-r--r-- 1 runner runner       0 Nov 16 01:42 .env.test.local
drwx------ 2 runner runner    4096 Nov 16 01:42 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 16 00:54 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 16 00:54 .github
-rw-r--r-- 1 runner runner       0 Nov 16 01:42 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 16 00:54 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 16 00:54 .mcp.json
[... 98 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; echo ====; cat okuno-2025-01.yaml
```

```
<persisted-output>
Output too large (53.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/7b6eae39-d9a7-4731-995f-d8b64a025bb6/tool-results/bpxngmraz.txt

Preview (first 2KB):
# Okuno, Woodward, Okano & Hata (2025) from dandiset 000727

Tests the findings of [Okuno et al. (2025)](https://doi.org/10.7554/elife.107990.1) on
[DANDI:000727](https://dandiarchive.org/dandiset/000727/0.240106.0043), the whole-brain two-photon
imaging of nine walking flies (Brezovec et al.) that the paper reuses. The FC computed here from the
raw imaging is compared with the paper's published FlyEM and FlyWire SC matrices (its code at
commit 4b92add and Zenodo record 15532272).

| Claim | Outcome |
|---|---|
| FlyEM gives a higher FC-SC correlation than FlyWire (0.73 against 0.68) | Partially reproduced |
| FlyEM is higher in 58 of 63 regions | Reproduced |
| Regional FC-SC correlation rises with cholinergic and falls with GABAergic output share | Not reproduced |
| Unsegregated synapses give a higher FC-SC correlation than random samples | Reproduced |
| Segregated synapses give a lower FC-SC correlation than random samples | Reproduced |
| Reciprocal synapses give a higher FC-SC correlation than random samples | Reproduced |
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,400p okuno-2025-01.yaml
```

```
<persisted-output>
Output too large (30.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/7b6eae39-d9a7-4731-995f-d8b64a025bb6/tool-results/b1vw2o4pq.txt

Preview (first 2KB):
schema_version: 3
id: okuno-2025-01
datasets:
- archive: dandi
  id: '000727'
  version: 0.240106.0043
  doi: 10.48324/dandi.000727/0.240106.0043
  relation: reuses
paper: doi:10.7554/elife.107990.1
date: '2026-11-10'
entry: okuno-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 20,200p README.md
```

```
| Smoothing, nuisance removal and ROI-count analyses on SCKm and DistKm ROIs (nine claims) | Blocked: atlases not published |
| FlyEM confidence thresholds, FlyEM permutation tests | Blocked: SC not published |
| PPSSI distribution over FlyWire neurons | Partially reproduced |
| Reciprocal synapse distances; the Wedge-AVLP GABA neuron's PPSSI and connections | Reproduced |
| Segregation index biased toward 0 | Not reproduced |
| PPSSI rankings (FlyWire half holds), APL similarity | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/okuno-2025-01.yaml`](../../attempts/okuno-2025-01.yaml).
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/7b6eae39-d9a7-4731-995f-d8b64a025bb6/tool-results/b1vw2o4pq.txt"
}
```

```
1	schema_version: 3
2	id: okuno-2025-01
3	datasets:
4	- archive: dandi
5	  id: '000727'
6	  version: 0.240106.0043
7	  doi: 10.48324/dandi.000727/0.240106.0043
8	  relation: reuses
9	paper: doi:10.7554/elife.107990.1
10	date: '2026-11-10'
11	entry: okuno-2025
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-14
20	  runner:
[... 381 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/7b6eae39-d9a7-4731-995f-d8b64a025bb6/tool-results/b1vw2o4pq.txt",
 "offset": 401
}
```

```
401
```

**Agent calls Bash**

```bash
cd  wc -l okuno-2025-01.yaml; sed -n 401,700p okuno-2025-01.yaml
```

```
725 okuno-2025-01.yaml
  - tCompCor (claims file M3). The 1000 highest-SD voxels are taken among native voxels inside the template's field of view,
    not among template voxels after warping, an assumption made to avoid warping every volume. Their SD is taken on the mean-centred
    series before detrending, as lib/getNuisancetCompCor.m does (the claims file's M3 says after detrending; the code it cites
    is followed).
  - Subjects. The code's subject list [1 2 3 4 5 6 8 9] is applied to the flies in name order, which the notebook confirms
    by reproducing the code's per-volume speed and walking regressor (data/behavior.mat) fly by fly to 1e-5; the seventh fly
    is fly-100. Nine flies are shown as a variant.
  - Left-right orientation. The files do not state it, and a symmetric brain cannot fix it. No flip is assumed; with left
    and right swapped the matrix-level FC-SC correlations are lower (FlyEM 0.514 against 0.603), which supports the choice.
    The swapped result is shown for every claim.
- claim: figs4-1-flyem-permutation
  outcome: blocked
  blocked_by: data_missing
  notes: Needs the FlyEM selected-synapse and null SC matrices (hb0sr80 targets and nulls). Neither the code repository nor
    Zenodo 15532272 holds them, and rebuilding them needs the FlyEM synapses in the template, which are not published.
- claim: fig4h-reciprocal-distances
  outcome: reproduced
  notebook: connectome_okuno_2025.ipynb
  output: claim:fig4h-reciprocal-distances
[... 281 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 700,725p okuno-2025-01.yaml; grep -n "^  - id:\|^- id:\|^  id:" okuno-2025.yaml | head -50; head -60 okuno-2025.yaml
```

```
outcome: blocked
    reason: Blocked in the notebook, without justification. results/neuralsc/wire0sr140_reciprocalDistances.mat is deposited,
      and the claim is FlyWire-only. Untested.
    response: 'Problem 5: tested in the companion notebook on the deposited distances; outcome changed from blocked to reproduced
      (mode 1 to 2 um, ACh plus GABA 0.756).'
  - claim: fig5b-walking-activation
    agrees: true
    outcome: reproduced
    reason: Under the hemibrain atlas, LAL, FB, IPS and GNG all pass readings (a) and (b) with the graded regressor.
    response: 'Problem 4: the paper''s deposited second level is now loaded and compared (cluster 416,801 voxels, per-neuropil
      r = 0.447). In this re-run reading (b) fails for LAL; reading (a) holds, so the outcome is unchanged.'
  - claim: fig5b-walking-suppression
    agrees: true
    outcome: not_reproduced
    reason: No voxel is below -3.24 (minimum t = -1.01). WED(R) and AVLP(R) are 100 % and 95 % positive-significant. At the
      README's negative peaks the notebook finds t = +3.01 and +4.03.
    response: 'Problem 4: the paper''s deposited second-level t map is now read and printed at the README peaks (-6.14 and
      -5.65, against 3.32 and 4.62 here) and over WED and AVLP, which separates a processing effect from a data effect. Tukey
      pre-whitening and motion correction were not added. Outcome unchanged.'
  - claim: fig5-wagn
[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dump.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    if c['cell_type']=='code' and len(src)>1500 and sys.argv[2:]==['short']:
        print(src[:1500]+'\n...[truncated]')
    else: print(src)
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--\n'+''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT(data)--\n'+''.join(d['text/plain'])[:3000])
        elif o.get('output_type')=='error': print('--ERR--', o.get('ename'), o.get('evalue'))
EOF
python3 $TMPDIR/dump.py reproduce_okuno_2025.ipynb short > $TMPDIR/r.txt; python3 $TMPDIR/dump.py connectome_okuno_2025.ipynb short > $TMPDIR/c.txt; wc -l $TMPDIR/*.txt; grep -n "######## CELL" $TMPDIR/r.txt | wc -l; python3 -c "
import yaml;r=yaml.safe_load(open('okuno-2025-01.yaml'));c=yaml.safe_load(open('okuno-2025.yaml'))
print(len(r['outcomes']),len(c['claims']) if 'claims' in c else c.keys())
from collections import Counter;print(Counter(o['outcome'] for o in r['outcomes']))
print(set(x['id'] for x in c['claims'])^set(o['claim'] for o in r['outcomes']))
print(len(r['verifications'][0]['results']))"
```

```
581 /tmp/claude-1001/c.txt
  1119 /tmp/claude-1001/r.txt
  1700 total
56
30 30
Counter({'blocked': 14, 'reproduced': 10, 'partially_reproduced': 3, 'not_reproduced': 3})
set()
30
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/r.txt"
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Reproducing Okuno et al. (2025) from dandiset 000727
4	
5	Paper. Okuno T, Woodward A, Okano H, Hata J (2025). Functional connectivity, structural
6	connectivity, and inter-individual variability in *Drosophila melanogaster*. eLife reviewed
7	preprint 107990 version 1, [doi:10.7554/elife.107990.1](https://doi.org/10.7554/elife.107990.1).
8	The claims file was written from the publisher's HTML of version 1 (main text, Methods, figure
9	legends and the legends of the Extended Data figures); no PDF was available.
10	
11	Dandiset. [DANDI:000727](https://dandiarchive.org/dandiset/000727/0.240106.0043), version
12	0.240106.0043, the version the paper's Methods and Data availability cite. It is also the only
13	published version; the draft lists the same 18 assets with the same total size.
14	
15	What the dandiset holds. The whole-brain two-photon imaging of Brezovec et al. that the paper
16	reuses: 9 flies, one NWB file each, with the raw GCaMP6f and tdTomato volumes (256 x 128 x 49 voxels,
17	3384 volumes at 1.88 Hz), anatomical stacks, a green series already registered to the FDA space by
18	Brezovec et al. (high-pass filtered and z-scored), and FicTrac walking data at 50 Hz.
19	
20	Outside inputs (the claims file says the paper relies on them; both are pinned):
[... 649 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/r.txt",
 "offset": 670,
 "limit": 460
}
```

```
670	reading b (both sides at 0.9 or more) needs an SC rebuilt from the synapse table; not run here
671	
672	
673	######## CELL 33 [markdown]
674	**Result: reproduced under reading (a).** The segregated SC (the code's target) has a lower FC-SC
675	correlation than the null for neuron SC (0.579 against 0.584, z = -5.6, p = 2e-8) and synapse SC
676	(0.529 against 0.545, z = -11.7); the paper's deposited values give z = -7.7 and -24.4. Nine flies
677	and left and right swapped agree; without nuisance removal the neuron SC is not different from the
678	null (p = 0.93). Reading (b) was not run.
679	
680	
681	######## CELL 34 [code]
682	show_perm("fig4i-reciprocal-higher")
683	r7, n7, r9, n9 = perm_res["fig4i-reciprocal-higher"]["main"]
684	print("MAIN: neuron above null with p < 0.05/6:", r7 > n7.mean() and flyfc.normal_p(r7, n7)[0] < 0.05 / 6,
685	      "| synapse:", r9 > n9.mean() and flyfc.normal_p(r9, n9)[0] < 0.05 / 6)
686	--OUT--
687	paper (deposited R) neuron r=0.7331 null 0.6888+-0.0018 z=+24.8 p=8.97e-136 (null range 0.6853 to 0.6928) | synapse r=0.7041 null 0.6776+-0.0022 z=+11.8 p=2.72e-32
688	main                neuron r=0.6198 null 0.5808+-0.0016 z=+24.2 p=5.52e-129 (null range 0.5771 to 0.5843) | synapse r=0.5633 null 0.5552+-0.0021 z=+3.8 p=0.000142
689	no nuisance         neuron r=0.6030 null 0.5939+-0.0021 z=+4.4 p=1.3e-05 (null range 0.5892 to 0.5989) | synapse r=0.5810 null 0.5882+-0.0032 z=-2.3 p=0.0232
[... 431 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/c.txt"
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Okuno et al. (2025): connectome-only claims from the paper's deposits
4	
5	A companion to `reproduce_okuno_2025.ipynb`. It tests the claims that rest on the FlyWire connectome
6	alone (data elsewhere), or the FlyWire half of a claim, from the paper's Zenodo record
7	[10.5281/zenodo.15532272](https://doi.org/10.5281/zenodo.15532272) (version of 2025-05-28). The record
8	holds the PPSSI the paper computed for each FlyWire neuron (`data/flywire783_neuron_sepidx0sr140_3000mi1.mat`,
9	stored as int16 times 10,000, negative where no value; plotNeuralFC.m reads it so), the DBSCAN
10	clusters behind it (`results/neuralsc/wire0sr140_neuralDBScan3000mi1.mat`), the closest reciprocal
11	synapse distances (`results/neuralsc/wire0sr140_reciprocalDistances.mat`) and the FlyWire synapse
12	table with locations (`data/flywire783_synapse.mat`, `data/flywire783_sypreloc.mat`,
13	`data/flywire783_sypostloc.mat`). Each analysis follows the paper's code (github
14	takuto-okuno-riken/flywalk at commit 4b92add), and the cited lines are printed from it. Cell types
15	come from the FlyWire annotation table of Schlegel et al. (2024), `Supplemental_file1_neuron_annotations.tsv`
16	of github flyconnectome/flywire_annotations at commit a83b277, which the deposits do not hold. The
17	FlyEM halves need a hemibrain DBSCAN that is not deposited and are not tested here. No random
18	numbers are drawn.
19	
20	| Claim | Data | Status |
[... 562 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 60,137p okuno-2025.yaml; sed -n 321,420p okuno-2025.yaml; sed -n 494,700p okuno-2025.yaml
```

```
#    (extractROItimeseries.m; code names s10 to s300 for 1 to 30 voxels).
# M3 Nuisance removal and FC (Methods, Generation of ROIs; code). Poly-tCompCor is 7 polynomial
#    regressors (two linear ramps, four quadratic terms and a constant,
#    lib/getNuisancePolynomial.m) plus 6 principal components of the 1000 voxels with the
#    highest temporal SD after polynomial detrending (lib/getNuisancetCompCor.m). Each voxel of
#    an ROI is mean-centred and regressed on these by OLS; the ROI time series is the mean of
#    the residuals; FC is the Pearson correlation between ROI time series per fly,
#    Fisher-z-transformed (atanh) and averaged over the 8 flies; infinite values (the diagonal)
#    are set to the largest finite value.
# M4 FC-SC correlation and detection (Methods, FC-SC detection and correlation;
#    analyzeFuncConnectivity.m). SC (neuron) is the count of neurons with post-synapses in one ROI
#    and pre-synapses in the other, SC (synapse) the count of their synapses (FlyEM confidence
#    0.8, FlyWire cleft score 140 unless stated). Both are the code's second SC layer
#    (ncountMat(:,:,2), sycountMat(:,:,2), "Traced"), which every plotting function uses (rows 7
#    and 9 of R and A): for FlyEM only neurons of Traced status (makeSCcountMatrix.m), for
#    FlyWire synapses whose pre and post neurons both have ids (makeSCcountMatrixFw.m); the
#    first layer, which adds FlyEM orphan bodies, is not what the figures show.
#    FC-SC correlation is the Pearson r between
#    log10(SC), with log of zero set to 0, and the code's |mean z-FC|, over every element of the
#    n x n matrices including the diagonal. FC-SC detection is the mean over 100 thresholds (the
[... 365 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def \|flip\|random_seed\|repeat" flyfc.py | head -80
```

```
31:  dorsoventral (y) and anteroposterior (z) axes run the same way, so no flip is
33:  correlation after an affine registration is printed for the eight flips); no flip
91:def list_assets():
109:def open_nwb(s3):
119:    def __init__(self, s3, h5, path=GREEN, threads=16):
133:    def _get(self, ci):
148:    def slices(self, zs):
157:            def submit(z):
171:    def mean_image(self, tstarts):
189:def code_file(name):
202:def code_nifti(name):
214:def zenodo_member(name):
223:def load_mat(b):
239:def load_sc(b):
248:def hemiroi_masks():
257:def hemiroi_names():
266:def _flip(a, fl):
270:def choose_flip(mean, tmpl_img, seed=1):
271:    """Correlation with the template after an affine registration, for each flip."""
276:        mov = ants.from_numpy(_flip(mean, fl).astype(np.float32), spacing=NATIVE_SPACING_MM)
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p flyfc.py; sed -n 266,336p flyfc.py; sed -n 383,450p flyfc.py
```

```
"""Loading and measures for testing Okuno et al. (2025) on dandiset 000727.

The dandiset holds the whole-brain two-photon imaging of Brezovec et al.: one NWB
file per fly with the raw GCaMP6f (green) and tdTomato (red) volumes, a processed
green series in the FDA space, and FicTrac walking data at 50 Hz.

The paper's structural connectivity (SC) and its ROI atlases are outside the
dataset. They come from

- the paper's code, github.com/takuto-okuno-riken/flywalk at commit 4b92add
  (CODE_COMMIT): the resized FDA template, brain mask, fibre mask, the hemibrain
  neuropil atlas (atlas/hemiroi, 114 ROIs), the ROI names (data/hemiroi.mat) and
  the FlyEM cf0.8 SC of the 114 ROIs (results/sc/hemiroi_connectlist.mat);
- the paper's Zenodo record 10.5281/zenodo.15532272 (ZENODO_URL), the version of
  2025-05-28 that the code's README cites: the FlyWire sc140 SC matrices of the
  hemibrain ROIs, the selected-synapse SC matrices, the 99 null SC matrices of each
  permutation test, per-ROI transmitter counts and post-synapse counts.

Where each parameter comes from:

[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "416\|396982\|396,982\|20\.9\|0\.447\|0\.363" $TMPDIR/r.txt | head; python3 - <<'EOF'
import json
nb=json.load(open('reproduce_okuno_2025.ipynb'))
for i in [19,29,43]:
    print(i, ''.join(nb['cells'][i]['source'])[1400:])
print(nb['metadata'])
EOF
```

```
298:fraction of volumes at or above b + th (binary walking): [0.562 0.299 0.208 0.176 0.363 0.329 0.604 0.503 0.15 ]
858:(396,982 voxels; the paper's deposited map 416,801) with maximum t = 20.9 (paper 14.7). LAL, FB,
861:correlates with the paper's deposited map at r = 0.447.
956:The two maps correlate voxel by voxel at r = 0.363 (0.390 with this attempt's map flipped left and
1087:| figs4-1ij-segregation-index-biased (companion notebook) | not reproduced: FlyWire mean 0.363, above 0.25 |
19 ompCor, 8 flies: FlyEM", round(signed[0], 4), "FlyWire", round(signed[1], 4))
r_em, r_fw = rows[4][3], rows[4][4]
print(f"MAIN: FlyEM r = {r_em:.4f} (tolerance 0.657 to 0.803, within: {0.657 <= r_em <= 0.803}); "
      f"FlyWire r = {r_fw:.4f} (0.612 to 0.748, within: {0.612 <= r_fw <= 0.748}); FlyEM higher: {r_em > r_fw}")
# per fly
for i, f in enumerate(flies):
    Fi = flyfc.mean_zfc([series["poltcomp"][i]])
    print(f["subject"], "single-fly FC: FlyEM", round(flyfc.fcsc_r(em_nc, Fi, ids), 4), "FlyWire", round(flyfc.fcsc_r(fw_nc, Fi, ids), 4))
print("second registration (another seed), Poly-tCompCor, 8 flies: FlyEM", round(flyfc.fcsc_r(em_nc, F_rep, ids), 4), "FlyWire", round(flyfc.fcsc_r(fw_nc, F_rep, ids), 4))

29 d R)"] = (t_[6], nl[:, 6], t_[8], nl[:, 8])
    perm_res[claim] = d
    print(claim, "| target", tgt, "synapse total", int(d["tot"]), "neuron total", int(d["ntot"]), "| null", null, "n =", len(nulls),
          "synapse totals mean", int(d["null_tot"].mean()), "SD", int(d["null_tot"].std(ddof=1)),
          "| totals test p =", round(flyfc.normal_p(d["tot"], d["null_tot"])[0], 3), flush=True)
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "NATIVE_SPACING_MM\s*=\|mode=\|def glm_smooth" -A3 flyfc.py | head -20
```

```
87:NATIVE_SPACING_MM = (0.00261117299, 0.00261117299, 0.005)  # NWB grid_spacing (m -> mm)
88-
89-
90-# --------------------------------------------------------------------------- archive
--
194:        t = tarfile.open(fileobj=io.BytesIO(b), mode="r:gz")
195-        _code = {}
196-        for m in t.getmembers():
197-            if m.isfile():
--
631:def glm_smooth(vol, fwhm_vox=8.0):
632-    """Gaussian of FWHM n voxels along y (2.28 um) and the same width along x and z
633-    (extractROItimeseries.m / glmFlyMB1st.m), filter size 2*ceil(2*sigma)+1."""
634-    from scipy.ndimage import gaussian_filter
--
643:                              truncate=trunc[ax], mode="constant")
644-    out[:] = tmp
645-    return out
646-
```

**Agent**

## Verifier report: Okuno et al. 2025 on DANDI:000727, round 2

Counts are taken from the files. The claims file has 30 claims. The attempt record has 30 outcomes: 14 blocked, 10 reproduced, 3 partially reproduced and 3 not reproduced. Eight outcomes carry `assumed: true`: fig3d-flyem-vs-flywire, fig3e, fig3g, fig4e, fig4f, fig4i, fig5b-walking-activation and fig5b-walking-suppression.

The main finding of this round is that the notebook was re-executed but its text was not updated. Almost every FC and GLM number in the "Result:" cells, the Summary and the record's notes and `measured` fields comes from an earlier run. The numbers in this run's printed output are different. Every outcome still holds on this run's output, but the stated values do not match it.

### 1. Outcomes

I agree with all 30 outcomes as stated, with these remarks:

- **fig3d (partially reproduced), agree.** Cell 19 prints FlyEM 0.5925 and FlyWire 0.5557: FlyEM is higher, and both values are below tolerance. The record's `measured` values (0.6161, 0.5808) are not this run's.
- **fig3e (reproduced), agree, but it is fragile.** Cell 23 prints 55. Across runs the count has been 54 (round 1), 53 (record) and 55 (now), against a lower bound of 52.2. It falls out of tolerance with left and right swapped (44) and with no nuisance removal (48). The record's `measured: 53` is not this run's value.
- **fig3g (not reproduced), agree.** Cell 26 prints ACh r = −0.072 (p = 0.573) and GABA r = −0.067 (p = 0.601). The record's `measured` values (0.033, −0.17) are not this run's.
- **fig4e, fig4f (reading a) and fig4i (reproduced), agree.** In cells 30, 32 and 34 the MAIN line is True/True for all three. For fig4i, the synapse p = 1.4e‑4 is below 8.3e‑3.
- **fig5b-walking-activation (reproduced), agree under reading (a).** Cell 38 prints True for all four neuropils, both atlases and both regressors.
- **fig5b-walking-suppression (not reproduced), agree.** Cell 41: no voxel is below −3.24 (minimum −1.45).
- **fig3a (partially reproduced), fig3c, figs3-1a and fig3f (reproduced), agree.** Cells 46–53 print values consistent with the notes.
- **fig4b (partially reproduced), agree with reservations.** The criterion defines no partial outcome for this claim, and the claims-file misreading I raised in round 1 is still open.
- **fig4h (reproduced), agree.** The mode is the 1–2 µm bin, and ACh plus GABA make up 0.756. The criterion says "pairs", but each reciprocal synapse is counted from both of its neurons. The presynaptic-only split (0.761) gives the same outcome.
- **fig4a and fig4c (blocked), agree.** The FlyWire halves hold (connectome notebook cells 10 and 13). `blocked_by: other` is honest: the FlyEM synapses are public but the DBSCAN was not run.
- **figs4-1ij (not reproduced), agree.** The FlyWire mean is 0.363, which is closer to 0.5 than to 0. The claim fails whatever the 0.25 bound and whatever the untested FlyEM half gives.
- **fig5-wagn (reproduced under reading b), agree.** The values are PPSSI 0.1332 and 22 ascending neurons at sc50 with at least 5 synapses each. At sc140 they are 212 synapses from the ANs, 65 to WPNb and a closest distance of 852.3 nm.
- **The 14 blocked outcomes, agree.** figs3-2cd is now `not_runnable` with a stated reason.

**The assumptions are stated.** Each of the eight outcomes lists them as deviations: the registration with no M1 motion or slice-timing correction, tCompCor taken from native voxels, the subject order, the left-right orientation, no Tukey taper, smoothing applied to the betas, and the README's cluster extent. Two of them are weaker than the record says:

- **Registration repeatability.** Cell 2 says repeated registrations "differed slightly" and that results "can move in the second or third decimal". Cell 9 contradicts this: a second seed moves native voxels by a median of 0.88–25.4 µm per fly, and the ROI series of the two registrations correlate at a median of 0.41–0.98. The changes between runs (fig3d r by about 0.024, fig3e by 2 regions, per-region r by about 0.07) confirm it.
- **Orientation.** The per-region check supports no flip: r = 0.637 as registered against 0.404 swapped (cell 23). The voxel-wise GLM comparison in cell 43 points the other way, at 0.373 as registered against 0.40 flipped. Neither the notebook nor the record mentions this.

A smaller point: the deviation "Native voxel size from the NWB grid_spacing (2.55 to 2.61 by 2.61 to 2.68 by 5 um)" implies a per-fly spacing. `NATIVE_SPACING_MM` (flyfc.py:87) is fly-087's spacing, used for every fly.

### 2. Statements the printed numbers do not support

**reproduce_okuno_2025.ipynb**

- **Cell 21:**
  - "r is 0.616 for FlyEM and 0.581 for FlyWire": printed 0.5925 and 0.5557.
  - "no nuisance removal 0.630 against 0.592": printed 0.6310 and 0.5987.
  - "nine flies 0.608 against 0.573": printed 0.5973 and 0.5604.
  - "synapse SC 0.562 against 0.535": printed 0.5405 and 0.5162.
  - "second registration (0.611 against 0.570)": printed 0.5991 and 0.559.
- **Cell 24:**
  - "53 of 63 … 53 with nine flies and 55 with the second registration": printed 55, 54 and 56.
  - "swapped … 43": printed 44.
  - "without nuisance removal it is 50": printed 48.
  - "r = 0.704 as registered and 0.414": printed 0.637 and 0.404.
- **Cell 27:** "r = 0.033, p = 0.80" and "r = −0.170, p = 0.18": printed −0.072 (p = 0.573) and −0.067 (p = 0.601).
- **Cell 31:**
  - "0.636 against 0.598, z = +23.9, p = 3e-126": printed 0.6147 against 0.5777, z = +22.6, p = 1.4e‑113.
  - "0.586 against 0.570, z = +6.6, p = 3e-11": printed 0.5660 against 0.5513, z = +6.4, p = 1.3e‑10.
  - "z = −9.0 and −10.6": printed −6.0 and −8.4.
  - "p = 5e-45" and "p = 0.88": printed 1.95e‑44 and 0.935.
- **Cell 33:**
  - "0.579 against 0.584, z = −5.6, p = 2e-8": printed 0.5553 against 0.5592, z = −5.3, p = 1e‑7.
  - "0.529 against 0.545, z = −11.7": printed 0.5118 against 0.5256, z = −10.0.
  - "(p = 0.93)": printed 0.827.
- **Cell 35:**
  - "0.640 against 0.601, z = +23.9": printed 0.6198 against 0.5808, z = +24.2.
  - "0.582 against 0.574 … p = 0.00016": printed 0.5633 against 0.5552, p = 1.4e‑4.
  - "Without nuisance removal the synapse SC is below the null (p = 0.0002)": printed p = 0.0232, which is not significant at 0.05/6.
  - "(p = 0.00025)": printed 2.9e‑4.
- **Cell 40:**
  - "396,982 voxels": printed 389,784.
  - "maximum t = 20.9": printed 18.18.
  - "the paper's deposited map 416,801": no cell prints the deposited positive cluster.
  - "Reading (b) fails for LAL (rank 23 of 63 at best)": cell 38 prints reading (b) True for LAL with the graded regressor (ranks 19 and 17). It fails only with the binary regressor, and for GNG with the graded regressor under JFRC2010.
  - "r = 0.447": printed 0.565.
- **Cell 44:**
  - "the lowest t is −1.74": printed −1.45.
  - "87 to 100%": printed 88–100 %.
  - "t = 3.32 and 4.62": printed 3.67 and 4.04.
  - "r = 0.363 (0.390 …)": printed 0.373 (0.40).
- **Cell 54 (Summary):**
  - "53 of 63": printed 55.
  - "0.581 against 0.684": printed 0.5557.
  - "r = 0.36 voxel by voxel": printed 0.373.
  - "median of 3 to 35 um": printed 0.88–25.4.
  - "median of 0.30 to 0.98": printed 0.41–0.98.
  - "8 ROIs partly outside … AL(L) 59% inside": cells 7–8 print 30 ROIs, AL(L) 0.05 and ROB(R) 0.00.
- **Cell 2:** "differed slightly … second or third decimal" is contradicted by cell 9.

**Attempt record notes.** The same stale values appear in:

- the notes and `measured` fields of fig3d, fig3e, fig3g, fig4e, fig4f, fig4i, fig5b-walking-activation and fig5b-walking-suppression;
- the orientation deviation, "(FlyEM 0.514 against 0.603)": printed 0.5103 and 0.5925;
- the registration deviation, "3 to 35 um";
- findings `methods_unavailable` ("0.581") and the fly-100 `other` finding ("8 hemibrain ROIs partly outside … AL(L) 59%"), and the deposited-GLM finding ("one positive cluster of 416,801 voxels", which is not printed).

The fig3d response's "tested on one fly (sub-voxel in-plane motion)" has no output in either notebook.

**Supported by the printed output:** connectome_okuno_2025.ipynb cells 4, 8, 11, 14, 17 and 20, and reproduce_okuno_2025.ipynb cells 47, 49, 51 and 53.

**README.** The outcome table agrees with the record, and its rows account for all 30 claims. It quotes no numbers that could be stale.

**Round-1 reasons.** The `verifications` block states my round-1 reasons for all 30 claims, condensed and faithful to my wording.

### 3. Round-1 points

**Resolved:**

- 5: the unjustified blocks are now tested (fig4h, fig5-wagn, figs4-1ij, and the FlyWire halves of fig4a and fig4c).
- 7: the FlyEM confidence-0 gap in fig3a is now stated.
- The cell 6 wording of point 2.
- The C items on the suppression map and the permutation tests: the paper's deposited t map and R values are now loaded and compared.

**Partly resolved:**

- 1 (motion and slice-timing correction): now stated everywhere, but not applied.
- 2 (orientation): the per-region check supports it, but the voxel-wise GLM comparison points the other way and is not mentioned.
- 3 (fragile permutation outcomes): the fragility is stated, and the deposited z values are shown.
- 4 (GLM differences): compared with the deposited map, but the Tukey taper and motion correction are still missing.
- C (registration repeatability): tested, and the variation is large.

**Open:** point 6 (fig4b count) is referred to a question for a reader, as is appropriate.

**What remains that bears on a conclusion:**

1. **The text describes another run.** The conclusions, Summary and record must be regenerated from this execution, or the notebook must be made deterministic. The outcomes do not change, but the fig4i no-nuisance statement and the fig5b-activation reading (b) statement reverse.
2. **The registration is unstable.** The second seed moves voxels by up to about 25 µm (median), and fig3e sits 1–3 regions above its bound across runs. fig3e's "reproduced" is therefore not robust. Its note should say so in terms of this instability, not "second or third decimal".
3. **Motion and slice-timing correction (M1) are still missing.** fig3d, fig3g, fig4e/f/i and fig5b-suppression all rest on uncorrected data. Whether the raw series needs the correction is still not shown in any output.
4. **The orientation evidence conflicts.** As registered: per-region r 0.637 against 0.404 swapped. Voxel-wise GLM: 0.373 against 0.40 flipped. fig3e and fig4e's synapse result depend on this choice.
5. **fig4b:** the claims file's quantity, neurons with a PPSSI = 139,255 with tolerance 0, may misread the paper's count of neurons the index was applied to.

## End of run

18 turns, 2 minutes, $1.50 at API prices, result: success.
