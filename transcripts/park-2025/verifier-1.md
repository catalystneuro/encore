# 001266 · verifier-1 · run 41330214783

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 680
drwxr-xr-x 6 runner runner    4096 Nov  1 17:32 .
drwxr-xr-x 7 runner runner    4096 Nov  1 17:32 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 17:11 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 17:11 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  1 17:32 .claude
-rw-r--r-- 1 runner runner       0 Nov  1 17:32 .env
-rw-r--r-- 1 runner runner       0 Nov  1 17:32 .env.development
-rw-r--r-- 1 runner runner       0 Nov  1 17:32 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  1 17:32 .env.local
-rw-r--r-- 1 runner runner       0 Nov  1 17:32 .env.production
-rw-r--r-- 1 runner runner       0 Nov  1 17:32 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  1 17:32 .env.test
-rw-r--r-- 1 runner runner       0 Nov  1 17:32 .env.test.local
drwx------ 2 runner runner    4096 Nov  1 17:32 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 17:11 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 17:11 .github
-rw-r--r-- 1 runner runner       0 Nov  1 17:32 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  1 17:11 .idea
[... 43 more lines not kept]
```

**Agent**

Two notebooks. Let me read the claims file first.

**Agent calls Read**

```json
{
 "file_path": "10.1038-s41467-025-55819-9.yaml"
}
```

```
1	# Claims for Park, Wong-Campos et al. (2025), "Dendritic excitations govern back-propagation via a
2	# spike-rate accelerometer", Nat Commun 16, 1333, on dandiset 001266.
3	#
4	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, protocol
5	# version pilot-10 as stated in docs/protocol.md (Reader).
6	#
7	# Text read: the version of record (PMC11794848, Europe PMC full text) with its Supplementary
8	# Information (Figs. S1 to S25, MOESM1), the Peer Review File (MOESM2), the Description of Additional
9	# Supplementary Files (MOESM3) and the Reporting Summary (MOESM9, no text extracted). The file
10	# paper/10.1101-2023.06.02.543490.txt is an earlier bioRxiv preprint with a different title and was
11	# not used.
12	#
13	# Code read: the paper links no analysis code ("All analysis was performed in MATLAB"; the analysis
14	# scripts are not published). It links simulation code only, as Supplementary Software, read from
15	# the journal's static content (no repository or commit exists):
16	#   Supplementary Software 1, 41467_2025_55819_MOESM7_ESM.zip (sha256 9eab52ac...7049249): the
17	#     NEURON conductance-based CA1 model (main.py, run_simulation.py, parameters_list.py, mod files,
18	#     MATLAB plotting of Figs. S19 and S20 phase diagrams).
19	#   Supplementary Software 2, 41467_2025_55819_MOESM8_ESM.zip (sha256 a5a1b593...0c6b6): the
20	#     two-compartment Izhikevich model, Two_compartment_Izhikevich.m. It differs from the Methods
[... 805 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1038-s41467-025-55819-9.yaml",
 "offset": 826
}
```

```
826	  statistics:
827	  - test: one-way ANOVA with Bonferroni's post hoc test
828	    p: 1.8e-8
829	    corrected: Bonferroni
830	    n: 4 Ni2+ cells from 4 animals and 11 vehicle cells from 8 animals
831	  data: dataset
832	  expected:
833	  - quantity: plateau AUC, Ni2+, percent of baseline
834	    value: 18
835	    tolerance: 5
836	    unit: "%"
837	  criterion: As fig6-dap5-reduces-plateau; reproduced when the mean is within tolerance and the
838	    Ni2+ comparison has p < 0.001.
839	- id: fig6-ttx-reduces-plateau
840	  statement: Blocking dendritic NaV channels with TTX (20 nM) also eliminated plateau potentials (26
841	    ± 8% of baseline, mean ± s.e.m.).
842	  source: Results, Plateau potentials are evoked by collision of synaptic inputs and dSpikes, paragraph 8; Figure 6a, 6b
843	  quote: Block of dendritic Na V channels by TTX (20 nM) also eliminated plateau potentials (AUC 26 ±
844	    8% of baseline, n = 4 cells from 3 animals, mean ± s.e.m.
845	  statistics:
[... 305 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c '^- id:' *.yaml; python3 - <<'EOF'
import json
for fn in ['reproduce_park_2025.ipynb','simulations_park_2025.ipynb']:
    nb=json.load(open(fn))
    print('=====',fn,len(nb['cells']))
    for i,c in enumerate(nb['cells']):
        src=''.join(c['source'])
        outs=[]
        for o in c.get('outputs',[]):
            if 'text' in o: outs.append(''.join(o['text']))
            elif 'data' in o:
                d=o['data']
                if 'text/plain' in d: outs.append(''.join(d['text/plain']))
                if 'image/png' in d: outs.append('[image]')
            elif o.get('output_type')=='error': outs.append('ERROR '+o['ename']+': '+o['evalue'])
        print(f'--- [{i}] {c["cell_type"]} src_len={len(src)} out_len={sum(len(x) for x in outs)}')
EOF
```

```
10.1038-s41467-025-55819-9.yaml:55
pnpm-lock.yaml:0
===== reproduce_park_2025.ipynb 63
--- [0] markdown src_len=3045 out_len=0
--- [1] code src_len=334 out_len=38
--- [2] markdown src_len=685 out_len=0
--- [3] code src_len=1251 out_len=709
--- [4] markdown src_len=13 out_len=0
--- [5] code src_len=1010 out_len=5079
--- [6] markdown src_len=858 out_len=0
--- [7] code src_len=1148 out_len=2422
--- [8] markdown src_len=391 out_len=0
--- [9] code src_len=648 out_len=859
--- [10] markdown src_len=465 out_len=0
--- [11] code src_len=1579 out_len=2736
--- [12] markdown src_len=801 out_len=0
--- [13] code src_len=976 out_len=7815
--- [14] markdown src_len=546 out_len=0
--- [15] markdown src_len=321 out_len=0
--- [16] code src_len=1235 out_len=186
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dump.py <<'EOF'
import json,sys
fn=sys.argv[1]; a=int(sys.argv[2]); b=int(sys.argv[3])
nb=json.load(open(fn))
for i,c in enumerate(nb['cells'][a:b],start=a):
    src=''.join(c['source'])
    print(f'=== [{i}] {c["cell_type"]}')
    print(src)
    for o in c.get('outputs',[]):
        if 'text' in o: print('>>>',''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('>>>',''.join(d['text/plain']))
            if 'image/png' in d: print('>>> [image]')
        elif o.get('output_type')=='error': print('>>> ERROR',o['ename'],o['evalue'])
EOF
python3 $TMPDIR/dump.py reproduce_park_2025.ipynb 0 14
```

```
<persisted-output>
Output too large (32.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/93eacf3c-abde-44d1-91fc-039e51eacac3/tool-results/bq1blbok7.txt

Preview (first 2KB):
=== [0] markdown
# Reproducing Park, Wong-Campos et al. (2025) from dandiset 001266

Paper. Park P, Wong-Campos JD, Itkis DG, Lee BH, Qi Y, Davis HC, Antin B, Pasarkar A, Grimm JB,
Plutkis SE, Holland KL, Paninski L, Lavis LD, Cohen AE (2025). Dendritic excitations govern
back-propagation via a spike-rate accelerometer. *Nature Communications* 16, 1333.
[doi:10.1038/s41467-025-55819-9](https://doi.org/10.1038/s41467-025-55819-9)

Dataset. [DANDI:001266](https://dandiarchive.org/dandiset/001266/0.250710.0758), version
0.250710.0758, streamed from the archive. The paper cites the dandiset without a version. Two
versions are published, 0.250106.0948 and 0.250710.0758; their 84 assets have the same asset
identifiers, paths and sizes, so they hold the same files, and the most recent one is pinned
(protocol, author step 1.3).

Claims. `claims/001266/10.1038-s41467-025-55819-9.yaml`, written from the version of record
(PMC11794848) with its Supplementary Information, Peer Review File and Source Data. The Source
[... 17 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/93eacf3c-abde-44d1-91fc-039e51eacac3/tool-results/bq1blbok7.txt"
}
```

```
1	=== [0] markdown
2	# Reproducing Park, Wong-Campos et al. (2025) from dandiset 001266
3	
4	Paper. Park P, Wong-Campos JD, Itkis DG, Lee BH, Qi Y, Davis HC, Antin B, Pasarkar A, Grimm JB,
5	Plutkis SE, Holland KL, Paninski L, Lavis LD, Cohen AE (2025). Dendritic excitations govern
6	back-propagation via a spike-rate accelerometer. *Nature Communications* 16, 1333.
7	[doi:10.1038/s41467-025-55819-9](https://doi.org/10.1038/s41467-025-55819-9)
8	
9	Dataset. [DANDI:001266](https://dandiarchive.org/dandiset/001266/0.250710.0758), version
10	0.250710.0758, streamed from the archive. The paper cites the dandiset without a version. Two
11	versions are published, 0.250106.0948 and 0.250710.0758; their 84 assets have the same asset
12	identifiers, paths and sizes, so they hold the same files, and the most recent one is pinned
13	(protocol, author step 1.3).
14	
15	Claims. `claims/001266/10.1038-s41467-025-55819-9.yaml`, written from the version of record
16	(PMC11794848) with its Supplementary Information, Peer Review File and Source Data. The Source
17	Data file (41467_2025_55819_MOESM10_ESM.xlsx, sha256 142a0621...0044774d), the outside input the
18	claims file names, maps each dandiset file to a figure panel; it is read here for that index
19	only.
20	
[... 446 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 $TMPDIR/dump.py reproduce_park_2025.ipynb 14 30 > $TMPDIR/p2.txt; wc -c $TMPDIR/p2.txt
```

```
34007 /tmp/claude-1001/p2.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p2.txt"
}
```

```
1	=== [14] markdown
2	The counts above identify the files. The legend's D2 of Fig. 3 (49 + 35 = 84 bAPs) is the file
3	named D4 (84 bAPs under the claims file's settings); the legend's soma and Soma + D2 are the
4	files named soma and D4+soma (161 to 167 and 165 to 170 bAPs with the 4 s.d. variant, 139 to 150
5	with 5 s.d.). The somatic threshold matters in these two burst files: at 5 robust s.d. some
6	closely spaced spikes fall below it, and the totals of the legend (167, 170) are met only at 4.
7	The index entry for Fig. 2 (file D3) gives 8 dSpikes, as its legend does.
8	=== [15] markdown
9	### Where the distal signal is
10	
11	Mean peak -dF/F per trunk segment for bAPs with and without dSpikes (claims file settings), in
12	three files. The difference between the classes is largest from 300 to about 370 µm; beyond
13	about 400 µm the traced line runs into dim tuft and background, so the variant region stops at
14	400 µm.
15	=== [16] code
16	def class_profiles(key, reading=("median", 5.0, np.inf)):
17	    o = cells[key]
18	    on, _ = D.stim_onsets(o["hdr"])
19	    df = calls[(key,) + reading]
20	    Y = D.bleach_correct(o["X"], o["t"])
[... 420 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 $TMPDIR/dump.py reproduce_park_2025.ipynb 30 46 > $TMPDIR/p3.txt; wc -c $TMPDIR/p3.txt
```

```
37537 /tmp/claude-1001/p3.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p3.txt"
}
```

```
1	=== [30] code
2	rows = []
3	for key in ["231620", "230335", "230952", "231405"]:
4	    for rd in D.READINGS:
5	        df = calls[(key,) + rd]
6	        by = df.groupby("order").agg(n=("dspike", "size"), dS=("dspike", "sum"))
7	        rows.append(dict(file=key, label=FILE_LABEL[key], reading=D.reading_name(*rd), bAPs=len(df),
8	                         **{f"bAP{i + 1}_dS/n": f"{int(by.dS.get(i, 0))}/{int(by.n.get(i, 0))}" for i in range(4)}))
9	fig3 = pd.DataFrame(rows)
10	print(fig3.to_string())
11	
12	
13	
14	>>>       file    label                         reading  bAPs bAP1_dS/n bAP2_dS/n bAP3_dS/n bAP4_dS/n
15	0   231620     soma     median, k=5, distal >300 um   150      0/54      3/51      2/41       0/3
16	1   231620     soma  median, k=5, distal 300-400 um   150      0/54      3/51      3/41       0/3
17	2   231620     soma     median, k=4, distal >300 um   165      0/54      0/54      5/51       0/5
18	3   231620     soma  median, k=4, distal 300-400 um   165      0/54      0/54      6/51       0/5
19	4   231620     soma     butter, k=5, distal >300 um   139      0/54      2/52      2/32       0/1
20	5   231620     soma  butter, k=5, distal 300-400 um   139      0/54      2/52      3/32       0/1
[... 523 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 $TMPDIR/dump.py reproduce_park_2025.ipynb 46 63 > $TMPDIR/p4.txt; wc -c $TMPDIR/p4.txt
```

```
30529 /tmp/claude-1001/p4.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p4.txt"
}
```

```
1	=== [46] code
2	from scipy import ndimage, signal
3	
4	def ca_spikes(key, rd, how):
5	    o = cells[key]
6	    on, off = D.stim_onsets(o["hdr"])
7	    thr = ocalls[(key,) + rd].attrs["dspike_threshold"]
8	    Y = D.bleach_correct(o["X"], o["t"])
9	    yd, _ = D.distal_trace(Y, o["dist"], 300, rd[2])
10	    k = int(0.151 * o["fs"]) | 1
11	    z = yd - ndimage.median_filter(yd, size=k, mode="nearest")
12	    z = ndimage.uniform_filter1d(z, 3)
13	    counts = []
14	    for s, e in zip(on, off):
15	        i0, i1 = np.searchsorted(o["t"], [s, e + 0.1])
16	        pk, _ = signal.find_peaks(z[i0:i1], height=thr, distance=int(0.02 * o["fs"]))
17	        n = 0
18	        for p in pk:
19	            if how == "fwhm":
20	                w = D.fwhm_ms(z[i0:i1], p, o["fs"], max_ms=200)
[... 451 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 $TMPDIR/dump.py simulations_park_2025.ipynb 0 10
```

```
=== [0] markdown
# Simulations of Park, Wong-Campos et al. (2025): the published NEURON model

Paper: [doi:10.1038/s41467-025-55819-9](https://doi.org/10.1038/s41467-025-55819-9). The model
claims use the paper's Supplementary Software 1 (41467_2025_55819_MOESM7_ESM.zip, sha256
9eab52ac...7049249, as in the claims file), downloaded from the journal and run here. It holds no
data from the dandiset (DANDI:001266, version 0.250710.0758, used by the other notebook of this
entry).

Changes needed to run it, none of which touches the model:
- NEURON 9 (the only version with wheels for this Python) refuses non-ASCII characters in mod
  files; they occur only in comments and are removed. The paper used NEURON 8.2.
- `run_morphology.py` calls `FullCA1Model(channel_params, morphology_file)`, but the class needs
  a third argument, `ka_cutoff`; the 100 µm that `run_simulation.py` passes is supplied.
- The scripts' plotting is not run; their simulation calls are, with the parameters of
  `main.py` and the two `parameters_list.py` files.

| Claim | Tested here |
|---|---|
| fig4f-g-model-accelerometer | tested |
[... 227 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "dendrite.py"
}
```

```
1	"""Loading and measures for dandiset 001266 (Park, Wong-Campos et al. 2025, Nat Commun 16, 1333).
2	
3	The dandiset holds raw camera movies of Voltron2 fluorescence (`acquisition/camera_1`, uint16
4	counts) and the DAQ channels recorded with them (100 kHz): the 594 nm and 488 nm laser
5	modulation, the EFS trigger, and, in the patch clamp files, the amplifier outputs. It holds no
6	regions of interest, structural images, stimulus masks or pixel size, so every region here is
7	found from the movie's mean image.
8	
9	Where each parameter comes from:
10	
11	- UM_PER_PX = 0.65: Methods, Kymographs, "Typical segment size was 10 pixels (6.5 µm with 10x
12	  objective)" (camera pixel 6.5 µm, 10x objective, Methods, Optical system).
13	- SEGMENT_PX = 10: the same passage (kymograph segments of 10 pixels).
14	- Bleach correction: Methods, Extracting fluorescence from movies, "Photobleaching was corrected
15	  by dividing the frames by a regression fit to the mean fluorescence". The form of the fit is
16	  not given; a cubic polynomial in time fitted to frames outside the stimulus epochs is a
17	  standard choice. Depolarization is -dF/F (claims file header; Voltron2 fluorescence falls).
18	- High-pass filter: the claims file header, open item (1). Reading "median": subtract a 20 ms
19	  moving median; reading "butter": zero-phase 2nd order Butterworth high-pass at 20 Hz.
20	- Somatic spike threshold: claims file header, item (4), 5 times the robust s.d. (1.4826 MAD) of
[... 521 more lines not kept]
```

**Agent**

Notebooks and helper read. Now checking the archive's file list to evaluate the blocked claims.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import requests,json
url="https://api.dandiarchive.org/api/dandisets/001266/versions/0.250710.0758/assets/?page_size=200"
out=[]
while url:
    r=requests.get(url,timeout=60).json(); out+=r['results']; url=r['next']
print(len(out))
for a in sorted(out,key=lambda a:a['path']):
    print(a['path'].split('/')[0][4:], round(a['size']/1e9,2))
json.dump(out,open('assets.json','w'))
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'requests'
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/001266/versions/0.250710.0758/assets/?page_size=200" -o a.json; python3 -c "
import json;d=json.load(open('a.json'));print(d['count'],d['next'])
for a in sorted(d['results'],key=lambda a:a['path']): print(a['path'].split('/')[0][4:], round(a['size']/1e9,2))
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 - <<'EOF'
import json,subprocess
d=json.load(open('a.json'))['results']
want=['194538','173841','174015','192452','134424','152103','211716','233448','145801','152100','171335','181403','084032','090755','142407','144213','150422','130550','134251','123242','125334','181648','183952','141936','144133','132253','163225','183639','175751','002415','153609','152756','232334']
for a in d:
    k=a['path'].split('/')[0][4:10]
    if k in want:
        m=json.loads(subprocess.run(['curl','-s',f"https://api.dandiarchive.org/api/dandisets/001266/versions/0.250710.0758/assets/{a['asset_id']}/"],capture_output=True,text=True).stdout)
        print(k, '|', m.get('wasGeneratedBy',[{}])[0].get('description') if m.get('wasGeneratedBy') else None, '|', [s.get('name') for s in m.get('wasGeneratedBy',[])][:2], '|', m.get('description'))
EOF
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; f=10.1038-s41467-025-55819-9.txt; wc -c $f; grep -o -i '.\{300\}F_\?ref.\{300\}' $f | head -5; echo ====; grep -o -i '.\{200\}ref.\{0,3\}F.\{300\}' $f | head -3; echo; echo ====PCA; grep -o -i '.\{400\}PCA.\{400\}' $f | head -6
```

```
237549 10.1038-s41467-025-55819-9.txt
====
ron2 trafficking), we normalized the fluorescence signal associated with a spike, ∆F, by the amplitude of the change in fluorescence during the passive return to baseline after a stimulus (i.e., ∆F/F ref ; Fig. 1d ). ∆F/F ref was used for all spike amplitude heatmaps and kymographs unless stated otherwise. By comparing two voltage-sensitive signals, this measure was insensitive to background and protein trafficking. Kymographs We manually drew a line along the apical dendrite and then determined the me

====PCA
ites were readily distinguishable from out-of-focus background and light scatter (Fig. S5 ). After functional recordings, we made high-resolution, three-dimensional structural images via 2-photon (2 P) microscopy. We mapped the functional recordings onto the independently measured cell morphology via a fit to a forward model of the microscope blurring function (Methods, Fig. S6 ). We further used PCA-based denoising similar to Ref. 38 (Methods, Fig. S7 ) to reduce the effect of pixel-wise shot noise. Together, these techniques produced simultaneously high spatial and temporal resolution two-dimensional (Supplementary Movie 1 , Fig. 1c–e ) and three-dimensional (Supplementary Movie 2 ) voltage maps which accounted for > 93% of the variance in the raw data, confirming that the procedure capture
baseline fluorescence. The full model jointly estimates these parameters along with the node voltages. We fit the model iteratively, alternating between estimating voltages and optimizing gains and offsets. This approach yields 3D voltage estimates v ^ for each frame (Fig. S6f, h ). We then passed these estimates through the microscope model M to create the reconstructed frame shown in Fig. S6g . PCA-based filtering Electrical length constants extended over many pixels, so we used Principal Component Analysis (PCA)-based filtering to remove pixel-wise shot noise, similar to the approach in Ref. 38 . We found that > 96% of the va
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; f=10.1038-s41467-025-55819-9.txt; grep -o -i 'PCA-based filtering Electrical.\{1200\}' $f; echo; echo ===; grep -o -i '.\{600\}passive return to baseline.\{100\}' $f|head -2; echo ===; grep -o -i 'Fig. 1d.\{0,10\}\(legend\)\?.\{300\}' $f | head -3; echo ===;  grep -o -i '.\{300\}noise-equivalent.\{300\}' $f | head
```

```
PCA-based filtering Electrical length constants extended over many pixels, so we used Principal Component Analysis (PCA)-based filtering to remove pixel-wise shot noise, similar to the approach in Ref. 38 . We found that > 96% of the variance in the recordings was contained within the first three principal components, whose spatial footprints broadly corresponded to the soma-proximal region, the dendritic trunk, and the distal dendrites, supporting the use of PCA to remove high spatial-frequency noise (Fig. S7 ). The first five temporal components contained signals related to neural activity and were used to resynthesize a denoised movie; the remaining components represented uncorrelated shot noise. To verify that the PCA filtering did not distort the underlying AP waveforms, we compared mean AP waveforms in subcellular compartments before and after the filtering steps. We observed no systematic deviations in the AP waveforms in the soma or dendrites (Fig. S7 ). Extracting fluorescence from movies Fluorescence values were extracted from raw movies in one of two ways. One approach used the maximum-likelihood pixel-weighting algorithm described previously 33 . Briefly, the fluorescence at each pixel was correlate

===
image, and the amplitude at each pixel was then set equal to the mean brightness at that pixel. For assembly of the color movies, the timing signal was assigned to a color map that was overlaid on a grayscale image of mean fluorescence. The optically stimulated region of the cell was highlighted in blue. Normalization to reference signal (∆F/F<sub>ref</sub>) To account for sub-cellular variations in voltage sensitivity (likely due to variations in Voltron2 trafficking), we normalized the fluorescence signal associated with a spike, ∆F, by the amplitude of the change in fluorescence during the passive return to baseline after a stimulus (i.e., ∆F/F ref ; Fig. 1d ). ∆F/F ref was used for all spike amplitude heatmaps an
===
Fig. 1d ). ∆F/F ref was used for 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; f=10.1038-s41467-025-55819-9.txt; grep -o -i '.\{200\}10.\{1,3\}20 ms.\{300\}' $f | head -5; echo ===S7; grep -o -i 'Fig. S7.\{0,5\}.\{0,300\}' 10.1038-s41467-025-55819-9.txt | head -3; ls;
```

```
===S7
Fig. S7 ) to reduce the effect of pixel-wise shot noise. Together, these techniques produced simultaneously high spatial and temporal resolution two-dimensional (Supplementary Movie 1 , Fig. 1c–e ) and three-dimensional (Supplementary Movie 2 ) voltage maps which accounted for > 93% of the variance in the raw d
Fig. S7 ). The first five temporal components contained signals related to neural activity and were used to resynthesize a denoised movie; the remaining components represented uncorrelated shot noise. To verify that the PCA filtering did not distort the underlying AP waveforms, we compared mean AP waveforms in 
Fig. S7 ). Extracting fluorescence from movies Fluorescence values were extracted from raw movies in one of two ways. One approach used the maximum-likelihood pixel-weighting algorithm described previously 33 . Briefly, the fluorescence at each pixel was correlated with the whole-field average fluorescence. Pix
10.1038-s41467-025-55819-9.supp1.pdf
10.1038-s41467-025-55819-9.supp2.pdf
10.1038-s41467-025-55819-9.supp3.pdf
10.1038-s41467-025-55819-9.supp4.pdf
10.1038-s41467-025-55819-9.txt
10.1101-2023.06.02.543490.txt
```

**Agent calls Bash**

```bash
cd paper; f=10.1038-s41467-025-55819-9.txt; grep -o -i 'Fig. 1.\{0,40\}Optical mapping.\{0,50\}' $f|head; grep -o -i '.\{100\}ref.\{0,40\}after.\{200\}' $f | head -5; echo ===; grep -o -i '.\{20\}d .\{0,100\}F *ref.\{400\}' $f | head -5
```

```
dingly numbered circled regions. ∆F spike , peak spike amplitude. F ref , mean amplitude during the reference time (from t = 10–20 ms after spike, Methods). e Spike delay map. f Sub-frame interpolation showing details of spike back-propagation (see also Supplementary Movie 3 ). Using patch clamp recordings, we verified that Optopatch-V d
===
respondingly numbered circled regions. ∆F spike , peak spike amplitude. F ref , mean amplitude during the reference time (from t = 10–20 ms after spike, Methods). e Spike delay map. f Sub-frame interpolation showing details of spike back-propagation (see also Supplementary Movie 3 ). Using patch clamp recordings, we verified that Optopatch-V did not perturb neuronal resting properties or excitability, in comparison to neighboring non-expressing neurons (Fig. S1 ). We then 
us. Right: normalized amplitude (∆F/F ref ) map for subthreshold depolarization (stimulus-triggered average from 54 trials). Amplitude heatmaps for the following panels share the same color scale. e Normalized amplitude (∆F/F ref ) map for back-propagating action potentials (bAPs) without dSpikes (-dSpikes; spike-triggered average from 56 spikes). Right: single-trial example of bAPs without a dSpike, sampled along the red line in ( d ) a
., ∆F/F ref ; Fig. 1d ). ∆F/F ref was used for all spike amplitude heatmaps and kymographs unless stated otherwise. By comparing two voltage-sensitive signals, this measure was insensitive to background and protein trafficking. Kymographs We manually drew a line along the apical dendrite and then determined the mean fluorescence time-course in equal-length segments along the line. Typical segment size was 10 pixels (6.5 µm with 1
```

**Agent calls Bash**

```bash
cd  python3 -c "import numpy, scipy, pandas; print('ok')" 2>&1; ls /usr/bin/python3* ; pip list 2>/dev/null | grep -i -E "numpy|scipy|pandas|h5py"
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy, scipy, pandas; print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'numpy'
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.14
/usr/bin/python3.14-config
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -m venv v >/dev/null 2>&1 && ./v/bin/pip install -q numpy scipy pandas 2>&1 | tail -2; ./v/bin/python -c "import numpy,scipy;print(numpy.__version__,scipy.__version__)"
```

```
2.5.4 1.18.1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t.py <<'EOF'
import sys, types
sys.modules['h5py']=types.ModuleType('h5py'); sys.modules['remfile']=types.ModuleType('remfile'); sys.modules['requests']=types.ModuleType('requests')
import numpy as np
from scipy import signal
import dendrite as D
rng=np.random.default_rng(0)
# 1 threshold
for nf,nd in [(100,10),(50,34),(20,60),(110,0)]:
    a=np.r_[rng.normal(1,.2,nf),rng.normal(3,.3,nd)]
    print('first_min',nf,nd,round(float(D.first_min_threshold(a)),3),'trough',D.trough_threshold(a))
# skewed unimodal
a=rng.gamma(2,0.5,120); print('gamma unimodal ->',D.first_min_threshold(a))
# 2 nan height
x=np.sin(np.linspace(0,20,500)); print('find_peaks nan height:',len(signal.find_peaks(x,height=np.nan)[0]))
# 3 fwhm of gaussian sigma=2 frames at 1kHz -> 4.71 ms
fs=1000.; t=np.arange(200); g=np.exp(-(t-100)**2/(2*2**2)); print('fwhm',D.fwhm_ms(g,100,fs))
# 4 exp fit
x=np.arange(10)*6.5+3.25; x=x[x<400]; x=np.arange(3.25,400,6.5)
y=np.exp(-x/255)+rng.normal(0,.02,len(x)); print('lam',D.exp_fit(x,y),D.exp_fit(x,y,True))
y2=0.6*np.exp(-x/255)+0.4; print('lam offset data, single fit',D.exp_fit(x,y2), 'offset fit',D.exp_fit(x,y2,True))
# 5 detect_spikes
z=rng.normal(0,1,10000); z[::500]+=8; pk,thr=D.detect_spikes(z,1000.); print('spikes',len(pk),thr)
# 6 highpass median width of 5ms event preserved?
e=np.zeros(1000); e[500:503]=1; h=D.highpass(e,1000.,'median'); print('median hp peak',h.max()); hb=D.highpass(e,1000.,'butter'); print('butter hp peak',round(hb.max(),3))
# 7 auc reading b with negative
EOF
$TMPDIR/v/bin/python $TMPDIR/t.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t.py", line 5, in <module>
    import dendrite as D
ModuleNotFoundError: No module named 'dendrite'
```

**Agent calls Bash**

```bash
PYTHONPATH=. $TMPDIR/v/bin/python $TMPDIR/t.py
```

```
first_min 100 10 2.011 trough (np.float64(2.0105401811219155), 2)
first_min 50 34 2.037 trough (np.float64(2.0356075853706175), 2)
first_min 20 60 nan trough (np.float64(1.7951892959500568), 2)
first_min 110 0 nan trough (np.float64(0.4974803980911549), 3)
gamma unimodal -> nan
find_peaks nan height: 0
fwhm 4.755863082722897
lam 257.2304338549041 261.2057736748646
lam offset data, single fit 600.9137813148784 offset fit 254.99999999912458
spikes 19 5.049813679538573
median hp peak 1.0
butter hp peak 0.869
```

**Agent**

**Verifier report, round 1: Park, Wong-Campos et al. 2025 on DANDI:001266 (0.250710.0758)**

There are 55 claims in the claims file. Notebook outputs are cited by cell index: `reproduce_park_2025.ipynb` as [n] and `simulations_park_2025.ipynb` as [S n].

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| source-data-index | reproduced | [11]: all 83 index names are found among the 81 subject folders (84 files); the sha256 matches. |
| fig2a-dspike-dichotomy | reproduced | [18]: 8 trials with a dSpike under both filters (k=5, >300 µm) and 0 on a first spike. However, 6 of the 8 dSpikes fall on a third detected spike (see B6). |
| fig2b-bimodal-distal-amplitudes | blocked (methods_underspecified) | [20]: the readings disagree on the distal amplitudes. Dip test p = 0.96–0.99 (unimodal), while BIC prefers 2 components (Δ 55–125). The soma is unimodal under both. |
| fig2e-f-dspike-maps | not_reproduced | [22]: beyond 300 µm, the −dSpike distal/soma ratio is 0.72, above the 0.5 limit. In the 300–400 µm variant the −dSpike ratio passes (0.50) but the +dSpike ratio is 0.81–0.86, below 1. The raw variant also fails (+dSpike 0.38). |
| fig2h-length-constant | not_reproduced | [24]: λ is about 1440–1490 µm for A·exp(−x/λ) and 54–58 µm with an offset, against 255 ± 10. The raw variant gives 356–404 µm. No reading comes near. |
| fig3-subthreshold-no-dendritic-initiation | not_reproduced (weak) | [26]: at the claims settings (k=5, >300 µm), 2–3 distal events have no somatic spike in the 15 ms before them (D4 at 20.7 ms; D4+soma at 126 and 170 ms). These events were never inspected (B7), and only 1 of the 17 neurons is in the dataset. |
| fig3-two-motifs-location-independent | not_reproduced | [28]: +dSpike profile pairs with r ≥ 0.9: 0/15 normalized and 12–13/15 raw. −dSpike: 7–9/15 normalized. +dSpike exceeds −dSpike in only 88–94% of distal segments in two files. |
| fig3h-dspike-peak-distance | blocked (data_missing), partly testable | The dandiset holds the Fig. 3 neuron's soma and branch recordings: 1 neuron of 17, several regions. |
| fig3g-later-bap-ratio | blocked (data_missing), partly testable | Same single neuron. |
| figs12-bap-velocity | blocked (data_missing), partly testable | The soma file of the one neuron gives 1 velocity, which can be compared with that neuron's per-neuron value in the Source Data sheet. |
| fig3e-soma-third-bap | not_reproduced | [30]: at k=5, 2–3 second bAPs carry dSpikes. The Butterworth filter fails in every variant (2/54 on the second bAP). Only median, k=4, 300–400 µm gives 0/0/6. |
| fig3d-distal-first-bap | blocked (methods_underspecified) | [30]: file D4 is identified by its 84 bAPs at k=5. Median gives 32/54, inside 31.5–38.5; Butterworth gives 31/54, just outside. The filter readings disagree. |
| fig3f-soma-plus-distal | not_reproduced | [30]: at the claims settings, third-bAP counts are 31 and 30 (below 48.6), and 26% of second bAPs carry dSpikes. It passes only at k=4 with the author's 300–400 µm region (51, 49). At k=4 and >300 µm it gives 46. |
| fig3i-distance-dependence | blocked (metadata_insufficient) | 4 dendrite stimulations of one neuron exist, but there are no stimulus masks or positions to give distances. |
| fig3-predepolarization-rule | not_reproduced | [32]: only 44–48% of dSpikes follow ≥15 ms of distal depolarization (90% required), and 87–89% of bAPs after <15 ms fail (90% required). |
| figs13-ramp-first-spike | blocked (data_missing), partly testable | Ramp files 141936, 144133 and 145100 (soma-step-ramp) exist: 2–3 cells. |
| fig4a-step-example | reproduced | [38]: one epoch reads FDDF… under all 8 readings. |
| fig4b-dspike-window | blocked (data_missing), partly testable | 180146 (already loaded) and 175751 (opto-D2) are step recordings. |
| fig4b-few-late-dspikes | blocked (data_missing), partly testable | The 180146 sequences in [38] already give the before/after-100 ms percentages. |
| fig4ce-period-doubling | blocked (data_missing), partly testable | 174900 is 1 of the 9 cells. [40] prints its last dSpike at 14–18 ms, far from 180 ms, but the detection there is unreliable (B1, B12). |
| fig4d-example-alternation | not_reproduced (inconclusive) | [40]: 0 of 5 epochs match FF(DF)×5, and most epochs are all failures. bAP counts swing 58–160 across readings, so detection is unvalidated. |
| figs15-stochastic | not_reproduced (inconclusive) | [42]: no dSpike beyond 300 µm in any reading, and spike-time spread per position is 14–85 ms against a 2 ms limit. Whether the 20 stimuli are true repeats was not checked (B13). |
| figs14-low-rate-attenuation | blocked (data_missing), partly testable | 192452 (Cell1-patch-freq) is one patch-pulse cell. |
| figs14-high-rate-window | blocked (data_missing), partly testable | Same file. |
| figs16-ba-increases-dspikes | blocked (data_missing), partly testable | The 145801/152100 pair (BaCl₂ 150 µM): 1 of 9 cells, comparable with the per-cell Source Data. |
| figs16-4ap-increases-dspikes | blocked (data_missing), partly testable | The 171335/181403 pair. |
| figs17-ttx-decreases-dspikes | blocked (data_missing), partly testable | The 084032/090755 pair (TTX 20 nM). |
| figs17e-ttx-high-dose | not_reproduced (inconclusive) | [44]: the baseline has 0 dSpikes in 7 of 8 readings. This is because its threshold is NaN, which turns into zero dSpikes (B1), not a measured absence. |
| figs18e-ni-no-effect-on-dspikes | blocked (data_missing), partly testable | 142407, 144213 and 150422: one cell at baseline, 100 µM and 500 µM Ni²⁺. |
| figs18-ni-blocks-calcium-spikes | blocked (data_missing), partly testable | The 130550/134251 pair (wide-field ramp, Ni²⁺ 500 µM). |
| figs18g-ba-increases-calcium-spikes | reproduced (fragile) | [46]: baseline 0, Ba²⁺ 2–3.75, Ba²⁺+Ni²⁺ 0 under every claims-setting reading. Each file has its own threshold, which confounds the comparison (B9). |
| fig4f-g-model-accelerometer | not_reproduced | [S5]: the soma step gives SSSSF, not F S S F…. Wide-field gives SSSFSFSFSFSFS, with no terminal run of failures. The run used NaV 48 rather than Table 1's 47 (B15). |
| figs20-model-robustness | blocked (too_large), disputed | [S9]: about 60 min for the 154 runs of Fig. S20c (23 s each). That is feasible, so this is not a convincing too_large. |
| figs20ab-model-patch-vs-opto | reproduced | [S7]: the patch run crosses 0 mV first at apic[23] and the soma never does. The optogenetic run crosses first in the axon, then the soma at 25.35 ms, and the stimulated site never crosses. |
| figs21-izhikevich | blocked (other), disputed | A two-compartment Izhikevich `.m` script can run in Octave or be ported in a few lines. |
| fig5a-plateau-collision | not_reproduced | [50]: duration 146 ms, outside 108–132. The spike-count and single-stimulus parts pass (9–14 vs 3 spikes; 9 and 33 ms). |
| fig5b-supralinear-auc | blocked (data_missing), partly testable and should have been tested | The notebook already loads about 10 cells with optical, combined and electrical epochs (9 Fig. S22 files plus 174622) [48], and the Source Data gives per-cell values. No fig5b ratio was computed. |
| fig5d-timing-window | blocked (data_missing), partly testable | The 30 ms series of one cell (194538, 194824, 195518, 195743) is deposited. |
| fig5d-single-bap-no-plateau | blocked (methods_underspecified) | [52]: window (a) gives ratios 2.58 and 3.77 (>2); window (b) gives max 1.59 but negative denominators (ratios −2.03 and −9.90). Only 1 of 5 cells. |
| fig5ef-late-efs-no-plateau | blocked (data_missing), partly testable | 173841 (3 s ramp + EFS): 1 cell. |
| fig5gh-weak-step-equal | blocked (data_missing), partly testable | 174015 (3 s constant step + EFS): 1 cell. |
| fig6-dap5-reduces-plateau | blocked (data_missing), partly testable | The 134424/152103 pair (one cell). |
| fig6-ni-reduces-plateau | blocked (data_missing), partly testable | The 232334/233448 pair. |
| fig6-ttx-reduces-plateau | blocked (data_missing), partly testable | The 204403/211716 pair. The likely vehicle pair is 152756/153417. |
| figs24-drugs-selective | blocked (data_missing), partly testable | The same pairs give per-cell drug/baseline AUC ratios. |
| figs23-dendrite-drives-soma | not_reproduced (measure unreliable) | [54]: longest persistence 206 ms against 270–330; the difference is positive in 8 of 9 cells. One cell (160204) gets 0 ms despite a +2.7% mean difference (B8). |
| figs25-temperature | blocked (data_missing), partly testable | 123242/125334 and 181648/183952 are 2 of the 6 cells. |
| figs1-no-perturbation | blocked (data_missing) | There are no patch recordings of non-expressing neighbour cells in the archive. |
| figs2-imaging-fidelity | not_reproduced | [60]: sensitivity passes (11.7%). Noise-equivalent voltage (NEV) fails: 3.5/3.3 mV at 1 kHz against 1.2 ± 0.5, and 11.4/5.2 mV at 2 kHz against 2.5 ± 0.8. At 1 kHz there are 6 false negatives and 19 false positives. |
| figs2d-frame-rate-same-sensitivity | reproduced | [62]: paired t-test p = 0.14 (the Source Data gives p = 0.87). |
| figs3-eyfp-dosimetry | blocked (data_missing) | There are no eYFP images and no intensity series for 18 cells. |
| figs4-stimulus-localization | blocked (data_missing), partly testable | 132253 (dmd-yaxis) and 163225 (soma-488-shift-yaxis) are single examples. Whether offsets are recoverable from the DAQ is unknown. |
| figs5-focal-selectivity | blocked (data_missing), partly testable | Transverse ROI shifts can be made on any loaded bAP recording, at the cost of hand-placing branches. |
| fig1-denoising-variance | not_reproduced (reading missing) | [34]: the first 5 components hold 10–30%, against ≥86.4% required. Only a pixel-centred PCA was run (B11). |
| fig3-cheriff-current | blocked (data_missing) | There are no eYFP images or Fig. S3e calibration data in the dandiset. |

### B. Problems

1. **[affects a conclusion]** `dendrite.first_min_threshold` returns NaN in two cases: when the dSpikes outnumber the failures, and when there is no density minimum above the main mode. NaN then silently means zero dSpikes, because `distal > nan` is False and `find_peaks(height=nan)` finds nothing.
   - I checked this on synthetic data. With 20 failures and 60 dSpikes it returns NaN, while the unused `trough_threshold` gives 1.80.
   - The rule also departs from the claims file's "trough between the two modes", and the notebook does not state this as an assumption.
   - It drives the zero results for figs17e (181900), figs15 (001459, >300 µm) and the Ni²⁺ file in figs18g, and probably fig4d.
2. **[affects a conclusion]** The claims file is wrong where it says, in shared-method item (4), that the 5-robust-s.d. somatic threshold "cannot change the outcome". In [13], k=5 finds 150 bAPs where the legend has 167 and 170, which shifts the bAP order. That changes fig3e and fig3f. The notebook ran k=4 as a variant, which is right.
3. **[affects a conclusion]** Trunk tracing (`trace_trunk`), cells [3], [15]: the author says the traced line leaves the trunk beyond about 400 µm. The claims-setting region (>300 µm) still includes those segments, so background is averaged into the "distal" region. No overlay image or coordinates validate the ROI. This affects fig2e-f, fig2h, fig3-two-motifs and fig3f, and the plateau files (>200 µm, trunk to 656 µm) as well.
4. **[affects a conclusion]** The notebook's summary table in [0] marks about 30 claims "blocked, pooled samples not deposited". The archive holds single-cell examples for most of them (file list in A). Most notably, fig5b's inputs are already loaded in [48] and never analysed.
5. **[affects a conclusion]** Both blocked simulation claims are blocked on weak grounds (figs20 and figs21; see the table).
6. **[does not affect a conclusion]** In fig2a [18], 6 of 8 dSpikes sit on order 2 (a third spike), and 9 trials have 3 spikes. The paper says two spikes per trial with the dSpike on the second. A dSpike echo may be counted as a somatic spike, or a distal peak more than 5 ms late may be assigned to a later spike. This was not investigated.
7. **[affects a conclusion]** fig3-subthreshold [26]: the orphan distal events were never plotted. The D4 one disappears at k=4, which points to a missed somatic spike.
8. **[affects a conclusion]** figs23 [54] has two problems:
   - Persistence is the first frame that comes back within 2 s.d. of baseline. That is noise-sensitive and gives 0.0 ms for 160204, whose mean difference is +2.7%.
   - The "largest plateau" region landed at 88–146 µm in 6 of 9 cells, which is proximal rather than distal dendrite.
9. **[affects a conclusion]** figs18g `ca_spikes` [46]: the thresholds differ about 2× between files of the same cell (1.60% baseline against 0.74% Ba²⁺), and the "time above threshold" duration reading depends on that threshold directly. The Ni²⁺ file's threshold is NaN under the median readings. A single shared threshold, as [44] uses for TTX, was not run.
10. **[affects a conclusion]** fig5d-single `auc` [52]: reading (b) gives negative optical and EFS areas (−0.041, −0.013), so the ratios are undefined. In reading (a) the denominators are tiny (0.007–0.015), which inflates the ratios.
11. **[affects a conclusion]** fig1 `pca_share` [34]: it subtracts the across-pixel mean waveform, which removes the shared signal, and it runs on unbinned shot-noise pixels. The paper's ">96% of the variance in the recordings" more plausibly means an uncentred SVD of pixel waveforms. That reading was not run.
12. **[affects a conclusion]** Somatic detection is unstable in the wide-field and ramp files ([36]: 174900 gives 58–160 bAPs, 181900 gives 18–62, 001459 gives 71–132). Nothing validates it, yet fig4d, figs15 and figs17e rest on it.
13. **[affects a conclusion]** figs15 [42] treats the 20 stimuli as repeats without checking that the 488 nm amplitude is equal across them.
14. **[affects a conclusion]** figs2 `patch_measures` [60] has three weaknesses:
    - Electrical spikes are 0 mV crossings at least 3 ms apart. That gives impossible maximum rates (333 and 263 Hz), and the total of 2265 against the paper's 2212 suggests false electrical spikes, which inflate the optical false negatives and false positives.
    - NEV reading (a) uses the first second of the recording, where bleaching is fastest.
    - The ROI is the top 20% of pixels, unweighted. Maximum-likelihood weighting, which the claims allow, was not run, and the NEV result may hinge on it.
15. **[affects a conclusion]** fig4f-g [S1–S5]: the criterion says Table 1 parameters (NaV 47). The run used `parameters_list.py` (48) under NEURON 9, and with only 85 and 100 ms runs. The NaV 47 run was not done.
16. **[does not affect a conclusion]** fig2h [24] drops fits with λ > 5000 µm (36–45 of 109 spikes) and fits only to 400 µm, both the author's choices. Every reading is far from 255 µm anyway.
17. **[does not affect a conclusion]** The Fig. S8a (80/12) and S8c-d (85/11) panels match neither file D1 (102/10) nor file D2 (98/9) [13], and the notebook leaves this unaddressed.
18. **[does not affect a conclusion]** fig2b [20] measures high-passed amplitudes rather than −dF/F at the peak.
19. **[does not affect a conclusion]** The clock check [7] fails for 184232. 0.65 µm/pixel is assumed from the Methods and never verified against the data.

### C. What I could not check, and the output that would settle it

- **ROI validity:** a mean image per file with the traced trunk, the soma disk and the 200/300/400 µm marks.
- **Thresholds:** a distal-amplitude histogram with the KDE and threshold for each file, especially 181900, 184232, 001459 and 174900. Also the counts of dSpikes rejected by the FWHM rule against the height rule.
- **fig3-subthreshold:** traces around each orphan distal event, soma and distal together.
- **figs15:** the 488 nm modulation amplitude per stimulus in 001459.
- **figs23 and fig5d-single:** the dendrite−soma difference traces with the 2 s.d. band, and the cumulative-AUC curves per epoch.
- **fig4f-g:** a run with Table 1's NaV 47 and longer step durations.
- **fig1:** the uncentred PCA share.
- **figs2:** NEV with maximum-likelihood weighting, and electrical spike rates after a refractory check.
- **Blocked claims:** fig5b ratios for the about 10 loaded plateau cells, compared with the Source Data, plus the single-cell tests listed in A.
- **Not seen by me:** the Source Data index rows themselves (I did not download the xlsx), and any figure image beyond its printed value range.

## End of run

26 turns, 7 minutes, result: success.
