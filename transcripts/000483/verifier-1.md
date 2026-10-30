# 000483 · verifier-1 · run 41099814565

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 456
drwxr-xr-x 6 runner runner    4096 Oct 30 18:53 .
drwxr-xr-x 7 runner runner    4096 Oct 30 18:53 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 17:33 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 17:33 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 30 18:53 .claude
-rw-r--r-- 1 runner runner       0 Oct 30 18:53 .env
-rw-r--r-- 1 runner runner       0 Oct 30 18:53 .env.development
-rw-r--r-- 1 runner runner       0 Oct 30 18:53 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 30 18:53 .env.local
-rw-r--r-- 1 runner runner       0 Oct 30 18:53 .env.production
-rw-r--r-- 1 runner runner       0 Oct 30 18:53 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 30 18:53 .env.test
-rw-r--r-- 1 runner runner       0 Oct 30 18:53 .env.test.local
drwx------ 2 runner runner    4096 Oct 30 18:53 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 17:33 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 17:33 .github
-rw-r--r-- 1 runner runner       0 Oct 30 18:53 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 17:33 .idea
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1038-s41467-023-37704-5.yaml
```

```
<persisted-output>
Output too large (45.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/15ce0801-782d-43f0-b4f4-ccf64a60e0af/tool-results/b8lxednwo.txt

Preview (first 2KB):
# Claims for Sit & Goard (2023), Nature Communications 14:1992, on dandiset 000483.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record (publisher's PDF supplied by a person, extracted to text):
# main text, figure legends, Methods and Statistical information. The Supplementary Information
# (Figures S1 to S7 and Table S1) was not in the paper store and was not read. The main
# findings and their statistics are all stated in the main text; the supplement holds the
# detail of three of them (Figure S5, Figure S6 and Table S1), and the claims that rest on it
# say so. The figures could not be opened (no PDF renderer), so no number below is read from a
# figure.
#
# Code read: the repository the paper links, given there as
# github.com/ucsb-goard-lab/Neurotar-HDExperiments; the repository is in fact
# github.com/ucsb-goard-lab/Neurotar-HD-Experiments, commit c6344f5 (2023-03-14). It holds
# MATLAB classes, not figure scripts: Cue.m (tuning curves, preferred direction, flip score,
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1038-s41467-023-37704-5.yaml"
}
```

```
1	# Claims for Sit & Goard (2023), Nature Communications 14:1992, on dandiset 000483.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	#
5	# Text read: the version of record (publisher's PDF supplied by a person, extracted to text):
6	# main text, figure legends, Methods and Statistical information. The Supplementary Information
7	# (Figures S1 to S7 and Table S1) was not in the paper store and was not read. The main
8	# findings and their statistics are all stated in the main text; the supplement holds the
9	# detail of three of them (Figure S5, Figure S6 and Table S1), and the claims that rest on it
10	# say so. The figures could not be opened (no PDF renderer), so no number below is read from a
11	# figure.
12	#
13	# Code read: the repository the paper links, given there as
14	# github.com/ucsb-goard-lab/Neurotar-HDExperiments; the repository is in fact
15	# github.com/ucsb-goard-lab/Neurotar-HD-Experiments, commit c6344f5 (2023-03-14). It holds
16	# MATLAB classes, not figure scripts: Cue.m (tuning curves, preferred direction, flip score,
17	# Gaussian fits), ControlledRotation.m (trial segmentation and the heading-selection test),
18	# FreelyMoving.m (the Rayleigh-vector test), LightDarkExperiment.m and its subclasses (light and
19	# dark segmentation), Separator.m, and _ReviewerCode/reviewer_reclassify_attempt.m (a GMM
20	# clustering run). No code for the V-tests, the coherent-remapping offsets, the flip-score
[... 701 more lines not kept]
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
        if 'text' in o: print('--OUT--\n'+''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--\n'+''.join(d['text/plain'])[:5000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('--ERR--', o['ename'], o['evalue'])
EOF
for f in single_cue somata axons rotation_remapping directions; do python3 $TMPDIR/dump.py $f.ipynb > $TMPDIR/$f.txt; wc -c $TMPDIR/$f.txt; done
```

```
29133 /tmp/claude-1001/single_cue.txt
35055 /tmp/claude-1001/somata.txt
20955 /tmp/claude-1001/axons.txt
28934 /tmp/claude-1001/rotation_remapping.txt
12776 /tmp/claude-1001/directions.txt
```

**Agent calls Bash**

```bash
cat $TMPDIR/single_cue.txt
```

```
######## CELL 0 [markdown]
# Sit & Goard (2023) on dandiset 000483: single-cue rotation (Figure 1)

**Paper.** Sit KK, Goard MJ (2023). Coregistration of heading to visual cues in retrosplenial
cortex. *Nature Communications* 14:1992.
[doi:10.1038/s41467-023-37704-5](https://doi.org/10.1038/s41467-023-37704-5). The claims file
(`claims/000483/10.1038-s41467-023-37704-5.yaml`) was written from the version of record (main
text, legends, Methods; the Supplementary Information was not available).

**Dataset.** [DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321), version
0.230421.2321. The paper cites no version of the dandiset (it cites a Dryad deposit and the
dandiset by its description), so the most recent published version is pinned, and the only one:
the draft has the same 128 assets and size and was last modified two months later, on metadata.

This notebook covers the single-cue controlled-rotation experiments (Figure 1). The head-rotation
and remapping claims are in `rotation_remapping.ipynb`, the dual-cue claims in
`axons.ipynb` and `somata.ipynb`, and Figures S5 and S6 in `directions.ipynb`.

| Claim | Here |
|---|---|
[... 440 more lines not kept]
```

**Agent calls Bash**

```bash
cat $TMPDIR/rotation_remapping.txt
```

```
######## CELL 0 [markdown]
# Sit & Goard (2023) on dandiset 000483: head rotation and remapping (Figures 2 and 3)

**Paper.** Sit KK, Goard MJ (2023), *Nature Communications* 14:1992,
[doi:10.1038/s41467-023-37704-5](https://doi.org/10.1038/s41467-023-37704-5); claims file
written from the version of record without its supplement.

**Dataset.** [DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321), version
0.230421.2321, the only published version (the paper cites none). See `single_cue.ipynb` for the
data check of all files.

| Claim | Here |
|---|---|
| fig2f-head-chamber-same-preference | tested |
| fig3c-coherent-remapping | tested |

Activity is inferred spikes computed from the raw fluorescence (no neuropil correction; see
`rsc.py`). Cells are selected by the heading-selection test with the centred fit, the reading
adopted in `single_cue.ipynb` (the code's uncentred fit only passes cells whose peak lies near
one heading, so preferred headings cannot be compared across conditions with it).
[... 393 more lines not kept]
```

**Agent calls Bash**

```bash
cat $TMPDIR/axons.txt
```

```
######## CELL 0 [markdown]
# Sit & Goard (2023) on dandiset 000483: ADN and visual axons, light and dark (Figure 4)

**Paper.** Sit KK, Goard MJ (2023), *Nature Communications* 14:1992,
[doi:10.1038/s41467-023-37704-5](https://doi.org/10.1038/s41467-023-37704-5); claims file
written from the version of record without its supplement.

**Dataset.** [DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321), version
0.230421.2321, the only published version (the paper cites none). See `single_cue.ipynb` for the
data check of all files.

| Claim | Here |
|---|---|
| fig4-axons-light-on-shape | tested |
| fig4-axons-light-off | tested |
| fig5-three-classes | tested |
| fig5-class-proportions | tested |
| fig5e-alignment-peaks-coregistered | tested |
| fig5f-heading-flip-unchanged | tested |
| fig5gh-landmark-alignment-flip-drop | tested |
[... 301 more lines not kept]
```

**Agent calls Bash**

```bash
cat $TMPDIR/somata.txt
```

```
<persisted-output>
Output too large (34.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/15ce0801-782d-43f0-b4f4-ccf64a60e0af/tool-results/bjz4705qg.txt

Preview (first 2KB):
######## CELL 0 [markdown]
# Sit & Goard (2023) on dandiset 000483: RSC somata with dual cues, light and dark (Figure 5)

**Paper.** Sit KK, Goard MJ (2023), *Nature Communications* 14:1992,
[doi:10.1038/s41467-023-37704-5](https://doi.org/10.1038/s41467-023-37704-5); claims file
written from the version of record without its supplement.

**Dataset.** [DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321), version
0.230421.2321, the only published version (the paper cites none). See `single_cue.ipynb` for the
data check of all files.

| Claim | Here |
|---|---|
| fig4-axons-light-on-shape | tested |
| fig4-axons-light-off | tested |
| fig5-three-classes | tested |
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cat $TMPDIR/directions.txt
```

```
######## CELL 0 [markdown]
# Sit & Goard (2023) on dandiset 000483: rotation direction and arena control (Figures S5, S6)

**Paper.** Sit KK, Goard MJ (2023), *Nature Communications* 14:1992,
[doi:10.1038/s41467-023-37704-5](https://doi.org/10.1038/s41467-023-37704-5); claims file
written from the version of record without its supplement, so Figures S5 and S6 were not read.

**Dataset.** [DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321), version
0.230421.2321, the only published version (the paper cites none). See `single_cue.ipynb` for the
data check of all files.

| Claim | Here |
|---|---|
| figs5-rotation-direction | tested |
| figs6-arena-control | tested |

The claims file gives two readings of what the bootstrapped KS test compares: (a) differences in
preferred heading between the two conditions for heading-selective cells, against the same
differences with cells paired at random; (b) the correlation of each cell's tuning curves in the
two conditions, against randomly paired cells. p is one minus the fraction of 1000 bootstrap
[... 202 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,400p $TMPDIR/somata.txt | tail -n +40
```

```
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.metrics import silhouette_score
from sklearn.mixture import GaussianMixture

import rsc

warnings.filterwarnings("ignore")
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 30)
started = time.time()
cat = rsc.catalog(full=False)
sub = cat[cat.experiment.isin(["soma_dual", "adn_axons", "vis_axons"])].reset_index(drop=True)
recs = rsc.load_many(sub.url.tolist())
with Pool(4) as pool:
    for r in recs:
        r["dff"] = rsc.dff(r["F"])
        r["sp"] = rsc.spikes(r["dff"], pool)
        del r["F"]
print(f"dandiset {rsc.DANDISET_ID} version {rsc.DANDISET_VERSION}: {len(sub)} files loaded and deconvolved "
      f"in {time.time() - started:.0f} s")
[... 341 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 400,800p $TMPDIR/somata.txt
```

```
SKKS089        416      121        15
SKKS090        181       17         9
SKKS091        203       27        12
SKKS100        245        9        12


######## CELL 13 [markdown]
## fig5e-alignment-peaks-coregistered

> In alignment cells the single light-off peak is always at the location of one of the two
> light-on peaks, so landmark and heading responses are coregistered.

Per alignment cell (no outlier step), offset of the light-off peak bin from the nearer of the two
light-on peaks (the peak bin, and the peak bin of the other half circle), V-test against 0.

######## CELL 14 [code]
def peak_offsets(L, D):
    out = []
    for l, d in zip(L, D):
        p1 = int(np.argmax(l))
[... 129 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "rsc.py"
}
```

```
1	"""Loading and measures for dandiset 000483 (Sit & Goard 2023, Nat Commun 14:1992).
2	
3	Each NWB file is one two-photon recording of retrosplenial cortex (somata) or of axon
4	terminals in it, made in a floating chamber (Neurotar). Each file holds the raw two-photon
5	video (not read here), the raw fluorescence of each ROI (`raw-fluorescence`, frames x ROIs, at
6	10 Hz), the ROI masks, and the chamber heading (degrees) and position (mm), one sample per
7	imaging frame. No neuropil trace, dF/F or inferred spikes are stored. The kind of experiment is
8	given only by the file's `identifier` (for example `..._DualCue_3rpm_SKKS088-DualCue-001`).
9	Files are streamed from the archive at the pinned version; nothing is written to disk.
10	
11	Where the parameters come from ("claims" is claims/000483/10.1038-s41467-023-37704-5.yaml; "code"
12	is github.com/ucsb-goard-lab/Neurotar-HD-Experiments at commit c6344f5):
13	
14	- dF/F = (F - F0)/F0 with F0 the mode of the fluorescence density (Methods, eq. 2). The Methods
15	  subtract a neuropil trace first (eq. 1); the dataset holds none, so F is used as it is
16	  (deviation). The mode is the peak of a Gaussian kernel density with
17	  Silverman's bandwidth, computed on a 1024-bin histogram (a standard choice).
18	- Inferred spikes: OASIS with an AR(1) kernel on dF/F (Methods, Analysis of calcium data), with
19	  its parameters estimated from the trace, as the call left in Cue.m
20	  (deconvolveCa(dff, 'ar1', 'foopsi', 'optimize_pars')) does (claims, opening comment). The
[... 597 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/syn.py <<'EOF'
import numpy as np, sys
sys.path.insert(0,'.')
import rsc
rng=np.random.default_rng(0)
# (1) fig5e peak_offset fold artefact: uniform random light-off peaks
L=np.zeros((2000,60)); D=np.zeros((2000,60))
for i in range(2000):
    L[i,14]=1; L[i,44]=0.5; D[i,rng.integers(60)]=1
def peak_offsets(L, D):
    out = []
    for l, d in zip(L, D):
        p1 = int(np.argmax(l))
        other = [(p1 + 30 + k) % 60 for k in range(-15, 16)]
        p2 = other[int(np.argmax(l[other]))]
        pd_ = int(np.argmax(d))
        o = [rsc.wrap180((pd_ - p) * 6) for p in (p1, p2)]
        out.append(o[int(np.argmin(np.abs(o)))])
    return np.array(out)
off=peak_offsets(L,D); print("fig5e null: V,p,n",rsc.vtest(off),"share<=18",np.mean(np.abs(off)<=18))
# (2) flip score sanity
x=np.arange(60)
uni=np.exp(-((x-14)/4.)**2); bi=uni+np.exp(-((x-44)/4.)**2)
print("flip uni",rsc.flip_score(uni[None]),"bi",rsc.flip_score(bi[None]))
# (3) vtest vs circstat formula check: V32=14.1 -> p
from scipy import stats
print("V32=14.1 p", 1-stats.norm.cdf(14.1*np.sqrt(2/32)))
EOF
python3 $TMPDIR/syn.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/syn.py", line 1, in <module>
    import numpy as np, sys
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls /usr/bin/python3* ; which -a python python3; ls ~/.venv ~/venv /opt 2>/dev/null; pip --version 2>&1 | head -1
```

```
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.14
/usr/bin/python3.14-config
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
/opt/hostedtoolcache/Python/3.13.17/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python3
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
cd $TMPDIR && python -m venv v && v/bin/pip -q install numpy scipy pandas h5py remfile dandi 2>&1 | tail -2; echo done
```

```
done
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python $TMPDIR/syn.py
```

```
fig5e null: V,p,n (np.float64(1269.7819705394731), np.float64(0.0), 2000) share<=18 0.2345
flip uni [-0.21776457] bi [1.9979681]
V32=14.1 p 0.00021174139572344153
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/syn2.py <<'EOF'
import numpy as np, sys
sys.path.insert(0,'.')
import rsc
rng=np.random.default_rng(1)
n_cells, n_tr, fpt = 300, 13, 150
tr=np.zeros((n_cells,60,n_tr))
for t in range(n_tr):
    h=np.linspace(-180,180,fpt,endpoint=False)
    act=(rng.random((fpt,n_cells))<0.02)*rng.exponential(1,(fpt,n_cells))
    tr[:,:,t]=rsc.bin_tuning(act,h)
for c in (True,False):
    r=rsc.selection_test(tr,"single",np.random.default_rng(2),centre=c)
    print("centre",c,"reliable",r.reliable.mean(),"is_hd",r.is_hd.mean())
EOF
time $TMPDIR/v/bin/python $TMPDIR/syn2.py
```

```
centre True reliable 0.16666666666666666 is_hd 0.07666666666666666
centre False reliable 0.16666666666666666 is_hd 0.05333333333333334

real	0m20.033s
user	0m38.256s
sys	0m0.484s
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000483/versions/0.230421.2321/assets/?page_size=200" -o assets.json; v/bin/python -c "
import json;d=json.load(open('assets.json'));print(d['count'])
for a in d['results']: print(a['path'], a['size'])
" | head -140
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for p in sub-SKKS125_ses-20220810T125750 sub-SKKS127_ses-20220811T120611; do id=$(v/bin/python -c "
import json;d=json.load(open('assets.json'))
print([a['asset_id'] for a in d['results'] if '$p' in a['path']][0])"); curl -s "https://api.dandiarchive.org/api/dandisets/000483/versions/0.230421.2321/assets/$id/" | v/bin/python -c "
import json,sys;d=json.load(sys.stdin)
ws=d.get('wasGeneratedBy');print(d['path']);print(json.dumps(ws,indent=0)[:1500]); print(d.get('variableMeasured'))"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "shuffl|cue card|0°|matched|derotat|visual cue only|suspend|false floor" 10.1038-s41467-023-37704-5.txt | head -60
```

```
132:neuron as a function of the angular position of the cue card, revealing
157:in front of the mouse near 0° (Fig. 1H). Together, these results suggest
162:Previous research has emphasized the importance of vestibular information for the function of the heading network58, so we next investigated whether the same neurons exhibit matched tuning during head
179:matched ROIs on average have the same heading preference with
182:for nonuniformity against 0°; Fig. 2F). Not all cells retain the same
233:cue card
370:p = 4.9 × 10−6, V-test for nonuniformity against 0°; Fig. 3C).
412:shown with a dashed gray capped line. In both cases, this causes the visual cue card
413:to move across the visual field in the same direction. C Example of derotation
418:three matched ROIs from the recordings. Purple denotes greater brightness in the
424:the difference in peak heading preference across recordings for matched ROIs. The
426:similar heading angles independent of head- or chamber-rotation. Shuffled distribution is shown in gray. ***p = 2.5 × 10−4, V-test for circular nonuniformity
427:against 0°.
436:curve, with peaks separated by approximately 180° due to the symmetry of the visual stimulus (Fig. 4C).
512:each recording. Shuffled distribution is shown in gray. ***p = 4.9 × 10−6, V-test for
513:circular nonuniformity against 0°.
521:visual contributions to tuning were retained in visual cue only rotation,
540:systematic overrepresentation of 180° errors due to the symmetric
541:visual cues. To prevent 180° decoding errors from biasing the performance metric, we opted to measure performance using “decoder
556:The single white cue card has been replaced with paired symmetric cues on the
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 1210,1240p 10.1038-s41467-023-37704-5.txt; sed -n 1270,1282p 10.1038-s41467-023-37704-5.txt; sed -n 405,428p 10.1038-s41467-023-37704-5.txt
```

```
Nature Communications|  (2023) 14:1992 
11

=== page 12 ===
calculated for each trial using the spike rate of the cell at each heading
bin, smoothed by a 15° moving average filter. The overall tuning curve
was calculated by averaging the responses across all trials.
Next, we determined whether each cell (or axon terminal) was
significantly heading selective. First, the reliability each cell’s heading
preference across trials was calculated by randomly splitting the trials
into two groups and calculating the correlation coefficient between
the resulting tuning curves. Then, each trial’s activity was circularly
shifted prior to calculating the correlation coefficient. This was repeated 1000 times for each cell, creating a real and shuffled distribution,
which was compared via a two-sample Kolmogorov–Smirnov test.
Cohen’s d was calculated to gauge the separation between the two
distributions. A cell was considered reliable if it passed the two-sample
Kolmogorov–Smirnov test at p < 0.1 and had a Cohen’s d > 0.8. In
addition, A single-term (for single cue) or two-term (for dual cue)
Gaussian was fit to the trial averaged tuning curve as well as the trial
averaged shuffled tuning curves. As before, the tuning curves were
[... 48 more lines not kept]
```

**Agent**

**A. Outcomes**

The claims file has 24 claims. The notebooks report outputs for 15 of them and treat one as blocked. The other 8 (fig5k and the seven fig6 claims) are said to be "recorded in the attempt record", which I don't have.

| Claim | Outcome | Reason |
|---|---|---|
| fig1-free-heading-fraction | blocked (data_missing) | Every one of the 128 assets is classified (single_cue cell 3). All 16 single-cue files rotate at a steady 3–8 rpm (motor-driven, cell 6). The only animal-controlled files are 2022 dual-cue recordings. The API listing (128 assets) agrees. |
| fig1g-rotation-heading-fraction | reproduced | With the centred fit, 485/3179 = 15.26% (cell 11), inside 14.2 ± 1.42 and 452 ± 45. The code's uncentred fit gives 10.85%, but it only passes cells whose peak is near −90° (cell 18), which contradicts Fig. 1H, so the centred reading is reasonable. Caveat: the test also passes untuned noise (B1). |
| selection-shuffled-control | not_reproduced | The paper says data were shuffled *before* running the procedure, and the criterion says "before the test". That reading (the notebook's "once" variant) passes 165/3179 = 5.19%, above the 1% limit (cell 16). The 0% "each" reading cannot fail by construction (B2). |
| fig1h-preferred-headings-tile | partially_reproduced | Tiling holds under both readings: (a) 60/60 bins and (b) every quadrant ≥ 0.181 (cell 18). The overrepresentation can't be judged because where the cue sits in the heading frame is unknown (metadata_insufficient). At dataset heading 0 the share is 0.247, below the uniform 0.25. The densest window (−102°, 0.40) depends on the mouse: SKKS090 and SKKS091 peak about 180° away from it. |
| fig2f-head-chamber-same-preference | partially_reproduced | p < 0.05 with V > 0 appears only when the chamber-rotation heading is mirrored (an assumption the notebook adds) and only 5 of 7 pairs are used: V = 34.6, n = 228, p = 5.9e-4 (cell 6). V is outside 14.1 ± 1.41; V/n is 0.15 against the paper's 0.44. One pair (SKKS116, n = 115) drives it; the other four have V ≤ 0.3. Randomly paired ROIs give a higher V (mean 46.2, cell 7) than the matched ROIs, so there is no evidence that matched ROIs keep their preference. |
| fig3c-coherent-remapping | partially_reproduced | All 8 readings give p < 0.05 with V > 0 (cell 9). V (47.0 at n = 85, or 208.9 at n = 830) is outside 25.6 ± 2.56. The main reading is only just above the paper's own random-pairing null (95th percentile 44.6, from just 100 draws). |
| fig4-axons-light-on-shape | reproduced | Under reading (b), all axons: mean-curve flip score is ADN −0.207 and visual 1.875; single-axon means are −0.109 vs 0.506, KS p = 1.6e-24 (axons cell 8). Reading (a) fails: the ADN mean-curve flip score is 0.277 (centred) or 1.132 (code fit). |
| fig4-axons-light-off | partially_reproduced | Visual axons lose tuning (light-off/light-on range 0.05–0.11). The ADN fraction selective in light-off is higher, but the per-recording comparison is not significant (Mann-Whitney p = 0.35); only the Fisher variant is (p = 0.035). The ADN light-off peak is 24–30° from the light-on peak under readings (a) centred and (b), so within 18° holds only under the code-fit reading (cell 10). |
| figs5-rotation-direction | reproduced | Reading (b), selective cells: bootstrapped KS p = 0.002, median correlation 0.210 real vs 0.118 random (directions cell 6). Reading (a) gives p = 0.16. The data are 4 files over 3 mice, not 2. |
| figs6-arena-control | reproduced (fragile) | Reading (b) gives p = 0.026, with median correlation 0.027 real vs −0.011 random. Reading (a) gives p = 0.89 (cell 8). It uses 5 pairs over 4 mice, and 112 of the 381 cells come from a file that visits 6 of 60 heading bins (B10). |
| fig5-three-classes | not_reproduced | The silhouette at k = 3 is not a local maximum under either reading: (a) 0.019 vs 0.272 (k = 2) and 0.032 (k = 4); (b) 0.120 vs 0.190 and −0.052 (somata cell 10). Only the reviewer-code variant, (a) centred on each curve's own peak, peaks at 3 (0.393). |
| fig5-class-proportions | not_reproduced | Tuned cells match (12.10% mean over recordings). The classes do not: landmark 7.4%, alignment 75.3%, heading 13.3% (counts 67, 1150, 202 against 522/552, 409, 332), and the order fails under every reading (cell 12). |
| fig5e-alignment-peaks-coregistered | not_reproduced | The V-test passes (V = 743.5, p ≈ 0), but this measure gives the same V/n under random light-off peaks (B3). Only 29.2% of offsets are within 18°, against about 0.21–0.23 by chance. This is far from "always", and lower than the "heading" (0.475) and "landmark" (0.537) classes (cell 14). |
| fig5f-heading-flip-unchanged | partially_reproduced | The criterion is met: p = 0.14 (cell 16). But the cells are not the paper's heading class: n = 202, and this class's light-on archetype is bimodal (a2/a1 = 0.70). |
| fig5gh-landmark-alignment-flip-drop | partially_reproduced | Both classes are lower in light-off (landmark F = 44.3, p = 2.8e-11; alignment F = 135, p = 2.7e-31), so the criterion is met. The classes come from a failed clustering and differ in size from the paper's (67 and 1150 cells). |
| fig5i-axons-in-clusters | partially_reproduced | The criterion is met as written: ADN axons inside the heading ellipse 0.88 / 0.72, visual axons inside the landmark ellipse 0.83 / 0.555 (cell 18). The ellipses don't separate the groups, though: visual axons fall more often inside the heading (0.93) and alignment (0.96) ellipses than the landmark one, and LDA assigns 85–98% of all axons to alignment. The classes come from fig5-class-proportions, which failed. |
| fig5k-visual-cue-only | no outcome: no notebook output | Not blocked by data. Two "Suspended" files exist (SKKS125 2022-08-10, SKKS127 2022-08-11, 15050 frames each). Each is the only file of its day, so whether matched standard-rotation ROIs exist inside them is unknown. |
| fig6a-population-light-on | no outcome: no notebook output | The inputs are in the archive: somata, heading, and light/dark from the hard-coded segments. Not data_missing. |
| fig6a-population-light-off | no outcome: no notebook output | Same as above. |
| fig6b-heading-cells | no outcome: no notebook output | Same as above. |
| fig6b-landmark-cells | no outcome: no notebook output | Same as above. |
| fig6b-alignment-cells | no outcome: no notebook output | Same as above. |
| fig6b-180-errors | no outcome: no notebook output | Same as above. |
| fig6-heading-below-population | no outcome: no notebook output | Same as above. |

No chance level from the paper applies to the claims that were tested. The 0.18 or 0.10 chance level belongs to the decoding claims, which weren't run.

**B. Problems**

1. **[affects a conclusion]** `rsc.selection_test` passes untuned cells. I ran it on 300 synthetic cells with sparse random activity, 13 trials and no tuning: 7.7% passed with the centred fit and 5.3% uncentred, and 16.7% passed the reliability step. The KS test on 1000 overlapping split-halves of the same trials counts heavily dependent values as independent, which inflates it. About half of the 15.3% in fig1g could therefore be chance, and the same holds for every selection-based claim. The paper says shuffled data pass no cells, so either the implementation differs from the original or the original test is equally liberal. The notebook doesn't check which.
2. **[affects a conclusion]** `selection_test(pre_shuffle="each")`, single_cue cell 15. The "real" trials are shuffled afresh in every iteration, so they have the same distribution as the null and no cell can pass. The claim's own wording ("before the test") and the paper's ("pre-shuffled data") match the "once" variant (5.19%), which the notebook files as a variant.
3. **[affects a conclusion]** `peak_offsets`, somata cell 14. Taking the nearer of two peaks 180° apart folds the offsets into ±90°, which biases the V-test towards 0. On synthetic data with uniformly random light-off peaks, V/n = 0.63 with p ≈ 0; the alignment cells give 0.65.
4. **[affects a conclusion]** rotation_remapping cells 5–7, fig2f. Mirroring the chamber-rotation heading and dropping 2 pairs are the notebook's own choices. They are stated and loosely supported by the Fig. 2B legend, but no data were used to check them. The random-pairing null, which is the paper's own comparison (Fig. 2F legend, "Shuffled distribution"), exceeds the real V, yet this isn't weighed in reaching an outcome. Head-rotation files show implausibly many selective cells: 52–85% (e.g. 247 of 384). One head-rotation file has 3.19 spikes/s while its chamber-rotation partner has 0.071 for the same ROIs. Heading-locked artefacts from derotation are not ruled out.
5. **[affects a conclusion]** somata cell 12, how classes are named. All three GMM light-on archetypes are bimodal (a2/a1 between 0.70 and 0.80), so no component is a unimodal "heading" class. The names come from a heuristic the notebook makes up, and fig5e, fig5f, fig5gh and fig5i all inherit them.
6. **[affects a conclusion]** somata cell 18, fig5i. The 95% ellipses overlap so much that "more than half inside" doesn't distinguish the groups. The notebook prints this (LDA assignments) but doesn't weigh it.
7. **[affects a conclusion]** single_cue cell 8, clock check. The peak lag is +6, −6, +6, +4 frames across the files that rotate both ways. That is inconsistent, and a negative lag means activity leading heading, which is implausible, so the alignment of heading and activity is not established. This matters most for fig2f, which compares two files whose offsets may differ.
8. **[affects a conclusion]** axons cell 10. The light-off selective fraction is computed over all axons only, not for reading (a) as the criterion asks. The per-recording test, which is the primary one, is not significant.
9. **[affects a conclusion]** fig1h. Where the cue sits in the heading frame is never worked out, although the claims file assigns that to the author. The notebook does show that the code's uncentred fit puts nearly all preferences at about −90° in the dataset frame (cell 18). That is a hint, but it is never followed up.
10. **[affects a conclusion]** directions cell 8, figs6. The pair SKKS125-FR-003 visits 6 of 60 heading bins, and `bin_tuning` sets unvisited bins to 0. Its 112 cells (29% of n) still enter the correlation test. No run without it is shown.
11. **[does not affect a conclusion]** `trial_segments` drops a segment only when a percentile has |p| < 40. The claims file's rule, "more than 50 degrees from ±90", would also drop |p| > 140. This is unverified against the MATLAB code.
12. **[does not affect a conclusion]** `_smoothdata` assumes MATLAB's `smoothdata` default window is n/4 = 15 bins, but MATLAB chooses it heuristically. The flip score itself behaves sensibly on synthetic curves: −0.22 unimodal, 2.00 bimodal.
13. **[does not affect a conclusion]** Stated deviations, all reasonable: dF/F without neuropil correction (the dataset has no neuropil trace); 3-bin (18°) smoothing instead of 15°; the Python OASIS port.
14. **[does not affect a conclusion]** fig3c includes the SKKS091 210504 pair, whose two files are both labelled context 1 ("Remapping-1-001" and "-1-002"), so it may not be a remapping pair. It only enters the "either" readings.
15. **[does not affect a conclusion]** Counts differ from the paper: 35 dual-cue soma recordings instead of 36; figs5 uses 4 files over 3 mice instead of 2; figs6 uses 5 pairs over 4 mice instead of 7 over 3. They are reported but not reconciled.

**C. What I could not check**

- **MATLAB code:** whether `calculateHeadDirection` centres the curve before fitting, whether the `_shuff` variant reshuffles in every iteration, `getTrialResponses`' percentile rule, and `smoothdata`'s window. The repository wasn't available to me. Outputs that would help: the selection test on time-shifted spikes or noise (to show its false-positive rate), and the excerpts of the cited code.
- **Light/dark timing:** the files have no markers. The per-segment spike sums support it for visual axons only. Printing mean visual-axon activity per 1250-frame block across all files would help.
- **Cue location in the heading frame (fig1h):** a per-mouse or per-session note of the cue position would settle it, or a check against the free-chamber code's convention.
- **fig5k and the seven fig6 claims:** I couldn't judge these at all. The notebook needs their outputs: the decoding means, 95% intervals and bootstrapped t-tests under each reading of the decoder and of chance, and the trial structure of the two visual-only files.
- **fig2f:** per-pair random-pairing nulls, and spike rates and selection fractions of head-rotation vs chamber-rotation files for the same ROIs, to test for derotation artefacts.
- **figs6:** a run without the 6-bin pair.
- **fig5e:** a null for its V statistic, e.g. light-off curves of other cells paired at random.

## End of run

22 turns, 6 minutes, result: success.
