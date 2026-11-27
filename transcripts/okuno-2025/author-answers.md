# okuno-2025 · author-answers · run 42781826260

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  cat questions/okuno-2025.yaml; ls entries/okuno-2025 entries/okuno-2025/*; grep -n "Author" docs/protocol.md | head
```

```
Tue Nov 10 08:26:24 UTC 2026
cat: questions/okuno-2025.yaml: No such file or directory
entries/okuno-2025/README.md
entries/okuno-2025/connectome_okuno_2025.ipynb
entries/okuno-2025/entry.yaml
entries/okuno-2025/flyfc.py
entries/okuno-2025/reproduce_okuno_2025.ipynb
entries/okuno-2025/requirements.in
entries/okuno-2025/requirements.lock.txt

entries/okuno-2025:
README.md
connectome_okuno_2025.ipynb
entry.yaml
flyfc.py
reproduce_okuno_2025.ipynb
requirements.in
requirements.lock.txt
199:## Author
```

**Agent calls Bash**

```bash
cd  ls; ls questions* 2>/dev/null; find . -path ./node_modules -prune -o -name "*okuno*" -print | grep -v "^./.git/" | head -30; git show --stat HEAD | head -30
```

```
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
schemas
scripts
[... 148 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat transcripts/okuno-2025/answer-report.md; ls transcripts/okuno-2025; git show HEAD~1 --stat | head -30; cat questions/README.md | head -60
```

```
I made no changes because there are no questions to answer. `questions/okuno-2025.yaml` does not exist, and git history shows no version of it on any branch.

The author's report confirms why: `transcripts/okuno-2025/author-report.md:53` says "**Questions to a reader:** none." The only open question from the author is for the paper's authors, not for a reader. It asks which SPM12 and ANTs settings and which NIfTI voxel size were used. It is already recorded as a `methods_unavailable` finding in `attempts/okuno-2025-01.yaml` (around line 486), and it falls under Author, step 1.6, so it is not mine to settle.

I did not create an empty questions file or edit `claims/okuno-2025.yaml`, and I did not run `tools/claims_check.py`, since no claim changed. If a verifier later raises questions, they need to be written to `questions/okuno-2025.yaml` before a reader run can answer them.
answer-report.md
answer.md
author-report.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
claims.md
commit 0477b527e6b511443b41ea5f76de18120cc6fb4b
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Tue Nov 10 08:06:08 2026 +0000

    Agent run on okuno-2025: author (success)
    
    Run: https://github.com/catalystneuro/encore/actions/runs/42760211426
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 199,420p docs/protocol.md
```

```
## Author

The workflow puts the paper under `paper/`, as for the reader. Read it to
understand the claims, their data and their figures. The claims file still
decides what is tested: do not change a claim's statement, expected values or
criterion. A method detail the claims file lacks is taken from the paper
(step 6).

**Time.** An author run is stopped five hours after it starts, and whatever
is not recorded by then is lost. The prompt says when the run started and the
time by which to finish. Check the clock (`date -u`) between steps. When that
time comes, stop analysing and finish: record each claim not yet tested as
blocked, `too_large` where the computation is what stopped it, saying how far
it got, then write the attempt record and run the entry's checks. A record
with some claims blocked for time is worth more than a run that is cut off.

### 1. Establish what can be tested

Do this before any analysis.

[... 203 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat transcripts/okuno-2025/author-report.md; git log --oneline -3 -- claims/okuno-2025.yaml attempts/okuno-2025-01.yaml entries/okuno-2025
```

```
I've finished steps 1 to 5 of the Author section and run the handover (step 6). Of the 33 claims, 13 were tested: 7 reproduced, 3 partially reproduced and 3 not reproduced. The other 20 are blocked. `tools/entry.py check` passes with 0 errors. The main notebook ran cleanly from a clean environment in 1053 s.

## 1. Outcomes

| Claim | Data | Outcome |
|---|---|---|
| fig1-poltcomp-optimal, fig2b, figs2-1b, fig2c, figs2-1d, fig2d-log-decline, fig2d-fly-values, fig2d-ten-thousand-rois, discussion-twenty-rois | with_inputs | blocked, `data_missing` (the SCKm and DistKm atlases are not published) |
| fig3d-confidence-threshold | with_inputs | blocked, `data_missing` (FlyEM SC at confidence 0.5, 0.6, 0.7 and 0.9 is not published) |
| fig3d-flyem-vs-flywire | with_inputs | partially reproduced: FlyEM 0.616 against FlyWire 0.575, so FlyEM is higher, but both are below tolerance |
| fig3e-flyem-higher-most-regions | with_inputs | reproduced: 55 of 63 regions (`assumed`, depends on left-right orientation) |
| fig3g-transmitter-correlation | with_inputs | not reproduced: ACh r = 0.013, GABA r = -0.157 |
| fig4e-unsegregated-higher | with_inputs | reproduced; selected total 2,373,104, null-totals p = 0.832 |
| fig4f-segregated-lower | with_inputs | reproduced under reading (a); reading (b) not run |
| fig4i-reciprocal-higher | with_inputs | reproduced |
| figs4-1-flyem-permutation | with_inputs | blocked, `data_missing` |
| fig5b-walking-activation | with_inputs | reproduced under reading (a) |
| fig5b-walking-suppression | with_inputs | not reproduced: no negative cluster (lowest t is -0.82) |
| fig3a-postsynapse-counts | elsewhere | partially reproduced: FlyEM at confidence 0 is not in the deposited table |
| fig3c, figs3-1a, fig3f | elsewhere | reproduced, from the paper's own per-ROI tables |
| fig4b-ppssi-distribution | elsewhere | partially reproduced: mean 0.471 fits, but 138,144 neurons have a PPSSI, not 139,255 |
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/entry.py --help 2>&1 | head -40; grep -n "author-answers\|handover" docs/protocol.md | head -20; git status --short
```

```
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES] [--python PYTHON]
                [--before BEFORE]
                {lock,check,run,all,handover,upgrade-python} entry [entry ...]

Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
tied to the data:
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls executed 2>&1 | head; python tools/entry.py lock entries/okuno-2025 2>&1 | tail -5; git status --short entries/
```

```
ls: cannot access 'executed': No such file or directory
wrote okuno-2025/requirements.lock.txt (Python 3.13, with hashes)
```

**Agent**

The lock file came out unchanged. The full run took about 18 minutes last time, which fits well within the time left.

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/okuno-2025 2>&1 | tail -30; date -u
```

```
Tue Nov 10 08:26:47 UTC 2026
Installed kernelspec registry-okuno-2025 in executed/okuno-2025/.venv/share/jupyter/kernels/registry-okuno-2025
0 error(s)
pass  reproduce_okuno_2025.ipynb  (1202 s)
pass  connectome_okuno_2025.ipynb  (7 s)
Tue Nov 10 08:47:06 UTC 2026
```

**Agent**

Both notebooks passed (1202 s and 7 s). Next I'll check that the re-run's numbers match the recorded conclusions, since ANTs registration is not exactly repeatable.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json,re
nb=json.load(open('executed/okuno-2025/reproduce_okuno_2025.ipynb'))
for c in nb['cells']:
    tags=c.get('metadata',{}).get('tags',[])
    if c['cell_type']=='code' and any(t.startswith('claim:') for t in tags):
        txt=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]) if o.get('output_type')=='stream')
        print('==',tags); print(txt[:1500])
EOF
```

```
== ['claim:fig3d-flyem-vs-flywire']
ROIs with a left-right partner: 50
paper's own output for this setting (Zenodo auc file, FlyWire): R(7) = 0.6835 R(9) = 0.6405
nuisance  flies orientation          EM neuron FW neuron  EM syn  FW syn
none      8     as registered           0.6334    0.5944  0.6057  0.5698
none      8     left-right swapped      0.5230    0.5288  0.4908  0.5063
none      9     as registered           0.6364    0.5995  0.6055  0.5702
none      9     left-right swapped      0.5351    0.5401  0.5006  0.5135
poltcomp  8     as registered           0.6029    0.5633  0.5509  0.5226
poltcomp  8     left-right swapped      0.5136    0.5054  0.4587  0.4682
poltcomp  9     as registered           0.6067    0.5670  0.5534  0.5254
poltcomp  9     left-right swapped      0.5158    0.5076  0.4597  0.4695
signed FC variant (O3), Poly-tCompCor, 8 flies: FlyEM 0.6028 FlyWire 0.5632
MAIN: FlyEM r = 0.6029 (tolerance 0.657 to 0.803, within: False); FlyWire r = 0.5633 (0.612 to 0.748, within: False); FlyEM higher: True
fly-087 single-fly FC: FlyEM 0.274 FlyWire 0.2609
fly-089 single-fly FC: FlyEM 0.2576 FlyWire 0.2466
fly-094 single-fly FC: FlyEM 0.2641 FlyWire 0.2503
fly-097 single-fly FC: FlyEM 0.2641 FlyWire 0.2515
fly-098 single-fly FC: FlyEM 0.2543 FlyWire 0.243
fly-099 single-fly FC: FlyEM 0.2519 FlyWire 0.2404
[... 124 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "0\.616\|0\.575\|55 of 63\|0\.013\|0\.157\|0\.832\|0\.82\|repeatab\|nondetermin\|not repeat" attempts/okuno-2025-01.yaml entries/okuno-2025/README.md entries/okuno-2025/entry.yaml | head -60
```

```
attempts/okuno-2025-01.yaml:131:  - 0.5753
attempts/okuno-2025-01.yaml:134:    r = 0.616 and FlyWire r = 0.575, so FlyEM is higher but both are below the tolerances (0.657 to 0.803
attempts/okuno-2025-01.yaml:136:    flies 0.608 against 0.568, signed FC (O3) 0.616 against 0.575, left and right swapped 0.531 against
attempts/okuno-2025-01.yaml:146:    this choice. The registration is not exactly repeatable between runs, so values can move in the second
attempts/okuno-2025-01.yaml:159:    0.616), which supports the choice. The swapped result is shown for every claim.
attempts/okuno-2025-01.yaml:169:  notes: FlyEM has the higher per-region FC-SC correlation in 55 of 63 regions (tolerance 52.2 to 63.8),
attempts/okuno-2025-01.yaml:180:    this choice. The registration is not exactly repeatable between runs, so values can move in the second
attempts/okuno-2025-01.yaml:191:    0.616), which supports the choice. The swapped result is shown for every claim.
attempts/okuno-2025-01.yaml:197:  - 0.013
attempts/okuno-2025-01.yaml:198:  - -0.157
attempts/okuno-2025-01.yaml:201:    r = 0.013 (p = 0.92) and GABA r = -0.157 (p = 0.22). No variant (no nuisance removal, nine flies,
attempts/okuno-2025-01.yaml:213:    this choice. The registration is not exactly repeatable between runs, so values can move in the second
attempts/okuno-2025-01.yaml:224:    0.616), which supports the choice. The swapped result is shown for every claim.
attempts/okuno-2025-01.yaml:318:    (expected 2,373,100 +- 237,310), and the null totals do not differ from it (p = 0.832, the paper's
attempts/okuno-2025-01.yaml:328:    this choice. The registration is not exactly repeatable between runs, so values can move in the second
attempts/okuno-2025-01.yaml:339:    0.616), which supports the choice. The swapped result is shown for every claim.
attempts/okuno-2025-01.yaml:359:    this choice. The registration is not exactly repeatable between runs, so values can move in the second
attempts/okuno-2025-01.yaml:370: 
[... 6 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/okuno-2025-01.yaml",
 "offset": 100,
 "limit": 420
}
```

```
100	- claim: fig2d-ten-thousand-rois
101	  outcome: blocked
102	  blocked_by: data_missing
103	  notes: The claim rests on the SCKm or DistKm ROI atlases (k-means parcellations of the hemibrain voxels),
104	    which are in neither the code repository at 4b92add nor Zenodo 15532272 (both versions were listed;
105	    the later code commits hold no atlas either). Zenodo holds the SC connect lists of these atlases but
106	    not the voxel-to-ROI assignment, so the dataset's FC cannot be put in the same ROIs. makeVoxelROIatlas.m
107	    rebuilds them by k-means, which would not reproduce the published ROIs, and a new SC would need the
108	    FlyEM synapse positions in the template, which are not published.
109	- claim: discussion-twenty-rois
110	  outcome: blocked
111	  blocked_by: data_missing
112	  notes: The claim rests on the SCKm or DistKm ROI atlases (k-means parcellations of the hemibrain voxels),
113	    which are in neither the code repository at 4b92add nor Zenodo 15532272 (both versions were listed;
114	    the later code commits hold no atlas either). Zenodo holds the SC connect lists of these atlases but
115	    not the voxel-to-ROI assignment, so the dataset's FC cannot be put in the same ROIs. makeVoxelROIatlas.m
116	    rebuilds them by k-means, which would not reproduce the published ROIs, and a new SC would need the
117	    FlyEM synapse positions in the template, which are not published.
118	- claim: fig3d-confidence-threshold
119	  outcome: blocked
[... 389 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF' > $TMPDIR/out.txt
import json
nb=json.load(open('executed/okuno-2025/reproduce_okuno_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    tags=c.get('metadata',{}).get('tags',[])
    src=''.join(c['source'])
    if c['cell_type']=='markdown':
        print(f'#### [{i}] MD', tags); print(src)
    else:
        txt=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]) if o.get('output_type')=='stream')
        txt+=''.join(''.join(o.get('data',{}).get('text/plain','')) for o in c.get('outputs',[]) if o.get('output_type') in('execute_result',))
        print(f'#### [{i}] CODE', tags, '\n--- out:'); print(txt)
EOF
wc -l $TMPDIR/out.txt; grep -n "^#### " $TMPDIR/out.txt | head -100
```

```
561 /tmp/claude-1001/out.txt
1:#### [0] MD []
53:#### [1] CODE [] 
58:#### [2] MD []
67:#### [3] CODE ['sanity'] 
83:#### [4] MD []
87:#### [5] CODE ['sanity'] 
101:#### [6] MD []
110:#### [7] CODE ['sanity'] 
123:#### [8] CODE ['sanity'] 
129:#### [9] MD []
134:#### [10] CODE ['sanity'] 
149:#### [11] MD []
154:#### [12] CODE ['sanity'] 
166:#### [13] MD []
168:#### [14] CODE ['sanity'] 
174:#### [15] MD []
182:#### [16] CODE [] 
199:#### [17] MD []
208:#### [18] CODE ['claim:fig3d-flyem-vs-flywire'] 
[... 34 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/out.txt"
}
```

```
1	#### [0] MD []
2	# Reproducing Okuno et al. (2025) from dandiset 000727
3	
4	Paper. Okuno T, Woodward A, Okano H, Hata J (2025). Functional connectivity, structural
5	connectivity, and inter-individual variability in *Drosophila melanogaster*. eLife reviewed
6	preprint 107990 version 1, [doi:10.7554/elife.107990.1](https://doi.org/10.7554/elife.107990.1).
7	The claims file was written from the publisher's HTML of version 1 (main text, Methods, figure
8	legends and the legends of the Extended Data figures); no PDF was available.
9	
10	Dandiset. [DANDI:000727](https://dandiarchive.org/dandiset/000727/0.240106.0043), version
11	0.240106.0043, the version the paper's Methods and Data availability cite. It is also the only
12	published version; the draft lists the same 18 assets with the same total size.
13	
14	What the dandiset holds. The whole-brain two-photon imaging of Brezovec et al. that the paper
15	reuses: 9 flies, one NWB file each, with the raw GCaMP6f and tdTomato volumes (256 x 128 x 49 voxels,
16	3384 volumes at 1.88 Hz), anatomical stacks, a green series already registered to the FDA space by
17	Brezovec et al. (high-pass filtered and z-scored), and FicTrac walking data at 50 Hz.
18	
19	Outside inputs (the claims file says the paper relies on them; both are pinned):
20	- the paper's code, github.com/takuto-okuno-riken/flywalk at commit 4b92add: the resized FDA
[... 542 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/okuno-2025; grep -n "seed\|THREAD\|thread\|registration(" flyfc.py | head -30
```

```
119:    def __init__(self, s3, h5, path=GREEN, threads=16):
127:        self.threads = threads
129:        adapter = requests.adapters.HTTPAdapter(pool_connections=threads, pool_maxsize=threads)
154:        with ThreadPoolExecutor(self.threads) as ex:
177:        with ThreadPoolExecutor(self.threads) as ex:
270:def choose_flip(mean, tmpl_img, seed=1):
277:        r = ants.registration(tmpl_img, mov, type_of_transform="Affine", random_seed=seed)
282:def register(mean, tmpl_img, fl, seed=1):
300:        r = ants.registration(tmpl_img, mov, type_of_transform="Affine", aff_metric=metric,
301:                              random_seed=seed, aff_iterations=(2100, 1200, 1200, 10),
306:    r = ants.registration(tmpl_img, mov, type_of_transform="SyNOnly",
307:                          initial_transform=aff[best][1], random_seed=seed)
```

**Agent calls Bash**

```bash
cd  grep -n "reading\|rank" claims/okuno-2025.yaml | grep -i -A2 -B2 "fig5\|rank" | head -30; grep -n "0\.\|%" entries/okuno-2025/README.md | head; grep -n "rank\|reading_b\|quarter\|0\.4" entries/okuno-2025/flyfc.py | head
```

```
14:# correlation score, cPPSSI, PPSSI and the two ranking scores); they are taken from the code
100:#    Unsegregated ranking score (1 - PPSSI) * log10(W), segregated ranking score PPSSI *
120:#    regressor (1 for volumes at or above b + th, else 0) is the reading the words "divided into
206:  criterion: The code's ranksum block (plotFuncConnectivity.m checkLargeSmoothingPoltcompByRoinum,
308:    Reproduced when, under one reading, both values are within tolerance. Rests on O2 and O3.
430:    bL, etc.)" is open; readings (a) aL and bL, (b) every mushroom body ROI among the 63 primary ROIs of the
510:- id: fig4a-unsegregated-ranking
511:  statement: The unsegregated ranking puts APL and CT1 cells in the top four places in FlyWire,
519:  criterion: Ranking by (1 - PPSSI) log10(W) (M7). Reproduced when ranks 1 to 4 in FlyWire are all
520:    APL or CT1 cells and rank 1 in FlyEM is APL.
521:- id: fig4c-segregated-ranking
522:  statement: The segregated ranking puts OA-AL2b2 cells first and second in FlyWire, and AOTU019_R
525:  quote: Segregated first (OA-AL2b2 cell) and second (OA-AL2b2 cell) ranking in FlyWire (sc140)
589:    readings (a) the code's (target sp90db3000mi1, rtype 0 in makeSCcountMatrixFw.m), every
592:    of fig4e-unsegregated-higher read. The code's reading is the main one. Reproduced when the FC-SC correlation is below the null mean with p <
650:    0.001 and the code's cluster extent. Neuropils by O4. "Strong" is not defined; readings (a)
652:    least half the brain-wide maximum, (b) each neuropil's mean t ranks in the top third of
653:    neuropils. Reproduced when all four hold under one reading and one atlas; partially
700:    the 212 AN synapses, the 65 WPNb synapses and the 852.3 nm distance were counted; readings
702:    use. Reproduced when every value is within tolerance under one reading.
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat entries/okuno-2025/README.md; sed -n 1,40p attempts/okuno-2025-01.yaml
```

```
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
| LAL, FB, IPS and GNG are active during walking | Reproduced |
| WED and AVLP are inactive or suppressed during walking | Not reproduced |
| Connectome counts per region and transmitter shares (four claims, data elsewhere) | Three reproduced, one partially |
| Smoothing, nuisance removal and ROI-count analyses on SCKm and DistKm ROIs (nine claims) | Blocked: atlases not published |
[... 49 more lines not kept]
```

**Agent**

README has no numbers to change. Now I'll rewrite the conclusion cells in the source notebook and apply the same text to the executed copy.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/md.py <<'EOF'
import json,sys
new = {}
new[20] = """**Result: FlyEM gives the higher FC-SC correlation, but both values are below the paper's.**
With the code's eight flies and Poly-tCompCor, r is 0.603 for FlyEM and 0.563 for FlyWire, below
the lower bounds of the tolerances (0.657 and 0.612), so the claim is partially reproduced. FlyEM
is higher in every as-registered variant (no nuisance removal 0.633 against 0.594, nine flies
0.607 against 0.567, signed FC the same as the main values, synapse SC 0.551 against 0.523). The
paper's own output file for the FlyWire setting gives 0.684 with the same SC, so the gap is in
this attempt's FC, not in the SC. Swapping left and right lowers both correlations (FlyEM 0.514,
FlyWire 0.505), which supports the orientation assumed. An earlier run of the same code gave
0.616 and 0.575 (the registration is not repeatable between runs); the outcome is the same."""
new[23] = """**Result: reproduced, resting on the left-right orientation.** FlyEM is higher in 56 of 63
regions under the main setting (tolerance 52.2 to 63.8) and in 55 with nine flies. FlyWire is
higher in AB(R), AME(R), FB, SLP(R), SMP(R), AB(L) and BU(L), five of them by 0.02 or less. With
left and right swapped the count is 43, outside the tolerance, and without nuisance removal it is
50 (48 with nine flies); the swapped orientation also gives the lower matrix-level FC-SC
correlation (fig3d), so the orientation used is the better supported one. This attempt's
per-region FlyWire values correlate with the paper's own (Zenodo) at r = 0.684. An earlier run of
the same code gave 55 (swapped 49, per-region correlation with the paper's 0.72)."""
new[26] = """**Result: not reproduced.** With this attempt's FC the per-region FC-SC correlation does not rise
with the cholinergic share (r = -0.024, p = 0.85) and its relation to the GABAergic share is not
significant (r = -0.108, p = 0.40); no variant gives a significant ACh or GABA correlation. The
paper's own per-region values from its Zenodo file, run through the same transmitter table, give
the paper's numbers (ACh r = 0.395, p = 0.0014; GABA r = -0.252, p = 0.047), so the difference
comes from the FC computed here, not from the transmitter table. An earlier run of the same code
gave ACh r = 0.013 and GABA r = -0.157, also not significant."""
new[30] = """**Result: reproduced.** Under the main setting the unsegregated SC has a higher FC-SC correlation
than the null for neuron SC (0.623 against 0.584 +- 0.002, p = 2e-128) and synapse SC (0.575
against 0.558 +- 0.002, p = 1e-13). The selected total is 2,373,104 (expected 2,373,100) and the
null totals do not differ from it (p = 0.832, as in the paper). Without nuisance removal the
direction reverses (both below the null, p = 2e-19 and 6e-25), so the result depends on
Poly-tCompCor. With nine flies both are still above the null; with left and right swapped the
neuron SC is above it (p = 9e-53) but the synapse SC is not different from it (p = 0.22). In an
earlier run of the same code the swapped synapse SC was above the null (p = 0.0021)."""
new[32] = """**Result: reproduced under reading (a).** The segregated SC (the code's target) has a lower FC-SC
correlation than the null for neuron SC (0.563 against 0.567 +- 0.001, p = 3e-6) and synapse SC
(0.517 against 0.532 +- 0.001, p = 9e-25). The same holds with nine flies and with left and right
swapped; without nuisance removal the neuron SC is not different from the null (p = 0.64) and the
synapse SC is below it (p = 1e-6). Reading (b) was not run."""
new[34] = """**Result: reproduced.** The reciprocal-synapse SC has a higher FC-SC correlation than the null for
neuron SC (0.627 against 0.587 +- 0.002, p = 3e-136) and synapse SC (0.572 against 0.562 +- 0.002,
p = 5e-7, below 0.05/6 = 0.0083). With nine flies both still hold. Without nuisance removal the
neuron SC is above the null without reaching 0.05/6 (p = 0.029) and the synapse SC is below it
(p = 0.00017); with left and right swapped the neuron SC stays above (p = 6e-46) and the synapse
SC is below the null (p = 0.0021). In an earlier run of the same code the swapped synapse SC was
below the null without reaching 0.05/6 (p = 0.0195)."""
new[39] = """**Result: reproduced.** The second level gives one large positive cluster (400,097 voxels; the
code's README prints 416,801) with maximum t = 16.9 (README 14.7). LAL, FB, IPS and GNG all lie
in it with peak t above half the maximum (reading a) under both atlases and both regressors. With
the graded regressor and the hemibrain atlas all four also hold under reading (b) (FB rank 13 of
63 by mean t); reading (b) fails for LAL with JFRC2010 and with the binary regressor. In an
earlier run of the same code reading (b) failed for FB (rank 26 of 63); the claim holds under
reading (a) in both runs."""
new[41] = """**Result: not reproduced.** No voxel in the brain mask falls below the negative height threshold
(the lowest t is -0.66), so there is no negative cluster. WED and AVLP are positive: 86 to 100% of
their voxels are above the positive threshold under both atlases and both regressors, and the
README's two negative peaks have t = 3.78 and 4.76 here. An earlier run of the same code gave a
lowest t of -0.82 and the same outcome."""
for path in sys.argv[1:]:
    nb=json.load(open(path))
    for i,t in new.items():
        c=nb['cells'][i]; assert c['cell_type']=='markdown' and ''.join(c['source']).startswith('**Result'), (path,i)
        lines=t.split('\n'); c['source']=[l+'\n' for l in lines[:-1]]+[lines[-1]]
    s=nb['cells'][51]; src=''.join(s['source'])
    old1="(0.575 against 0.684 for\nFlyWire)"; assert old1 in src; src=src.replace(old1,"(0.563 against 0.684 for\nFlyWire)")
    old2="""The registration is
not exactly repeatable, so numbers can move slightly between runs."""
    assert old2 in src
    src=src.replace(old2,"""The registration is
not repeatable between runs: an earlier run of the same code gave 0.575 for FlyWire, and some
variants moved by more (see each claim), though no outcome changed.""")
    old3="""coverage of a hemibrain ROI (AL(L) 65% inside the field of view in this run), which fits the
paper's reason for leaving one fly out; fly-105 also has ROIs partly outside."""
    assert old3 in src
    src=src.replace(old3,"""coverage of the hemibrain ROIs (20 ROIs partly outside the field of view in this run, AL(L)
12% inside; 65% in an earlier run), which fits the paper's reason for leaving one fly out.""")
    lines=src.split('\n'); s['source']=[l+'\n' for l in lines[:-1]]+[lines[-1]]
    json.dump(nb,open(path,'w'),indent=1,ensure_ascii=False); open(path,'a').write('\n')
EOF
cp entries/okuno-2025/reproduce_okuno_2025.ipynb $TMPDIR/bak.ipynb
python $TMPDIR/md.py entries/okuno-2025/reproduce_okuno_2025.ipynb executed/okuno-2025/reproduce_okuno_2025.ipynb && git diff --stat
```

```
entries/okuno-2025/reproduce_okuno_2025.ipynb | 89 +++++++++++++++------------
 1 file changed, 50 insertions(+), 39 deletions(-)
```

**Agent calls Bash**

```bash
cd  git diff entries/ | grep "^[-+]" | grep -v '^[-+] *"\*\*Result\|^[-+] *"' | head; git diff entries/ | head -20
```

```
--- a/entries/okuno-2025/reproduce_okuno_2025.ipynb
+++ b/entries/okuno-2025/reproduce_okuno_2025.ipynb
diff --git a/entries/okuno-2025/reproduce_okuno_2025.ipynb b/entries/okuno-2025/reproduce_okuno_2025.ipynb
index 8b634b140d..cb8fa00b77 100644
--- a/entries/okuno-2025/reproduce_okuno_2025.ipynb
+++ b/entries/okuno-2025/reproduce_okuno_2025.ipynb
@@ -455,13 +455,14 @@
    "metadata": {},
    "source": [
     "**Result: FlyEM gives the higher FC-SC correlation, but both values are below the paper's.**\n",
-    "With the code's eight flies and Poly-tCompCor, r is 0.616 for FlyEM and 0.575 for FlyWire, below\n",
+    "With the code's eight flies and Poly-tCompCor, r is 0.603 for FlyEM and 0.563 for FlyWire, below\n",
     "the lower bounds of the tolerances (0.657 and 0.612), so the claim is partially reproduced. FlyEM\n",
-    "is higher in every as-registered variant (no nuisance removal 0.638 against 0.606, nine flies\n",
-    "0.608 against 0.568, signed FC the same as the main values). The paper's own output file for the\n",
-    "FlyWire setting gives 0.684 with the same SC, so the gap is in this attempt's FC, not in the SC.\n",
-    "Swapping left and right lowers both correlations (FlyEM 0.531, FlyWire 0.520), which supports the\n",
-    "orientation assumed."
+    "is higher in every as-registered variant (no nuisance removal 0.633 against 0.594, nine flies\n",
+    "0.607 against 0.567, signed FC the same as the main values, synapse SC 0.551 against 0.523). The\n",
[... 2 more lines not kept]
```

**Agent**

The notebook diff touches only the conclusion cells. Next I'll update the attempt record.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/okuno-2025-01.yaml'; s=open(p).read()
def rep(old,new,count=1):
    global s
    n=s.count(old); assert n==count,(old[:60],n); s=s.replace(old,new)
# left-right deviation, repeated in 8 claims
rep("""assumed; with left and right swapped the matrix-level FC-SC correlations are lower (FlyEM 0.531 against
    0.616), which supports the choice.""","""assumed; with left and right swapped the matrix-level FC-SC correlations are lower (FlyEM 0.514 against
    0.603), which supports the choice.""",6)
rep("""or third decimal.""","""or third decimal, and some variants moved more (see the notes).""",8)
# fig3d
rep("""  - 0.6159
  - 0.5753""","""  - 0.6029
  - 0.5633""")
rep("""  notes: '63 primary ROIs, no smoothing, Poly-tCompCor, code''s eight flies, SC neuron layer 2. FlyEM
    r = 0.616 and FlyWire r = 0.575, so FlyEM is higher but both are below the tolerances (0.657 to 0.803
    and 0.612 to 0.748). FlyEM is higher in every variant: no nuisance removal 0.638 against 0.606, nine
    flies 0.608 against 0.568, signed FC (O3) 0.616 against 0.575, left and right swapped 0.531 against
    0.520. Synapse SC gives 0.561 against 0.530. The paper''s own output file for the FlyWire setting
    (Zenodo, results/auc/poltcomparhemiroi_fw0sr140-fcauc.mat) gives R(7) = 0.684 with the same SC, so
    the shortfall is in the FC computed here, not in the SC.'""",
"""  notes: '63 primary ROIs, no smoothing, Poly-tCompCor, code''s eight flies, SC neuron layer 2. FlyEM
    r = 0.603 and FlyWire r = 0.563, so FlyEM is higher but both are below the tolerances (0.657 to 0.803
    and 0.612 to 0.748). FlyEM is higher in every variant: no nuisance removal 0.633 against 0.594, nine
    flies 0.607 against 0.567, signed FC (O3) 0.603 against 0.563, left and right swapped 0.514 against
    0.505. Synapse SC gives 0.551 against 0.523. The paper''s own output file for the FlyWire setting
    (Zenodo, results/auc/poltcomparhemiroi_fw0sr140-fcauc.mat) gives R(7) = 0.684 with the same SC, so
    the shortfall is in the FC computed here, not in the SC. No reader question was asked on this claim,
    so the claims file is unchanged; the values are those of the re-run of 2026-11-10 08:27 UTC, made
    without any change to the code. The first run gave 0.616 and 0.575 (the registration is not repeatable
    between runs), with the same outcome.'""")
# fig3e
rep("""  measured: 55
  assumed: true
  notes: FlyEM has the higher per-region FC-SC correlation in 55 of 63 regions (tolerance 52.2 to 63.8),
    and 55 with nine flies. FlyWire is higher in AB(R), AME(R), FB, PLP(R), SLP(R), SMP(R), AB(L) and
    BU(L), most by less than 0.02. The count depends on the orientation and the nuisance removal; with
    left and right swapped it is 49 and without nuisance removal 50, both outside the tolerance. The per-region
    FlyWire values correlate with the paper's own (Zenodo auc file) at r = 0.72.""",
"""  measured: 56
  assumed: true
  notes: FlyEM has the higher per-region FC-SC correlation in 56 of 63 regions (tolerance 52.2 to 63.8),
    and 55 with nine flies. FlyWire is higher in AB(R), AME(R), FB, SLP(R), SMP(R), AB(L) and BU(L),
    five of them by 0.02 or less. The count depends on the orientation and the nuisance removal; with
    left and right swapped it is 43 and without nuisance removal 50, both outside the tolerance. The per-region
    FlyWire values correlate with the paper's own (Zenodo auc file) at r = 0.684. No reader question was
    asked on this claim, so the claims file is unchanged; the values are those of the re-run of 2026-11-10,
    made without any change to the code. The first run gave 55 (swapped 49, per-region correlation with
    the paper's 0.72), with the same outcome.""")
# fig3g
rep("""  - 0.013
  - -0.157""","""  - -0.024
  - -0.108""")
rep("""  notes: With this attempt's per-region FlyWire FC-SC correlation, the acetylcholine output share gives
    r = 0.013 (p = 0.92) and GABA r = -0.157 (p = 0.22).""","""  notes: With this attempt's per-region FlyWire FC-SC correlation, the acetylcholine output share gives
    r = -0.024 (p = 0.85) and GABA r = -0.108 (p = 0.40).""")
rep("""    per-region values correlate with the paper's at r = 0.72).
  deviations:""","""    per-region values correlate with the paper's at r = 0.684). No reader question was asked on this claim,
    so the claims file is unchanged; the values are those of the re-run of 2026-11-10, made without any
    change to the code. The first run gave ACh r = 0.013 and GABA r = -0.157, with the same outcome.
  deviations:""")
# fig4e
rep("""    eight flies. Neuron SC r = 0.634 against null 0.593 +- 0.0015 (p = 1e-153); synapse SC r = 0.583 against
    0.564 +- 0.0023 (p = 2e-17); both above the null at p < 0.05/6. The selected synapse total is 2,373,104
    (expected 2,373,100 +- 237,310), and the null totals do not differ from it (p = 0.832, the paper's
    value). Nine flies and left-right swapped give the same direction at p < 0.05/6 (swapped synapse p
    = 0.0021). Without nuisance removal both are below the null (p = 3e-6 and 6e-15), so the result needs
    Poly-tCompCor.""","""    eight flies. Neuron SC r = 0.623 against null 0.584 +- 0.0016 (p = 2e-128); synapse SC r = 0.575 against
    0.558 +- 0.0023 (p = 1e-13); both above the null at p < 0.05/6. The selected synapse total is 2,373,104
    (expected 2,373,100 +- 237,310), and the null totals do not differ from it (p = 0.832, the paper's
    value). Nine flies give the same direction at p < 0.05/6; with left and right swapped the neuron SC
    is above the null (p = 9e-53) and the synapse SC is not different from it (p = 0.22). Without nuisance
    removal both are below the null (p = 2e-19 and 6e-25), so the result needs Poly-tCompCor. No reader
    question was asked on this claim, so the claims file is unchanged; the values are those of the re-run
    of 2026-11-10, made without any change to the code. The first run gave neuron r = 0.634 and synapse
    r = 0.583, with the swapped synapse SC above the null (p = 0.0021); the main outcome is the same.""")
# fig4f
rep("""  notes: Reading (a), the code's target sp90db3000mi1, against the 99 rd1560-80 null SC matrices. Neuron
    SC r = 0.574 against null 0.578 +- 0.0008 (p = 4e-8); synapse SC r = 0.524 against 0.540 +- 0.0013
    (p = 6e-35); both below the null at p < 0.05/6. Nine flies and left-right swapped agree. Without nuisance
    removal the neuron SC is not different from the null (p = 0.48) and the synapse SC is below it (p
    = 7e-12). The null totals match the selected total (p = 0.64). Reading (b), both sides at 0.9 or more,
    needs an SC rebuilt from the synapse table and was not run.""","""  notes: Reading (a), the code's target sp90db3000mi1, against the 99 rd1560-80 null SC matrices. Neuron
    SC r = 0.563 against null 0.567 +- 0.0008 (p = 3e-6); synapse SC r = 0.517 against 0.532 +- 0.0014
    (p = 9e-25); both below the null at p < 0.05/6. Nine flies and left-right swapped agree. Without nuisance
    removal the neuron SC is not different from the null (p = 0.64) and the synapse SC is below it (p
    = 1e-6). The null totals match the selected total (p = 0.64). Reading (b), both sides at 0.9 or more,
    needs an SC rebuilt from the synapse table and was not run. No reader question was asked on this claim,
    so the claims file is unchanged; the values are those of the re-run of 2026-11-10, made without any
    change to the code. The first run gave neuron r = 0.574 (p = 4e-8) and synapse r = 0.524 (p = 6e-35),
    with the same outcome.""")
# fig4i
rep("""  notes: Reciprocal SC (code target rc20_only1) against the 99 rd140-15 null SC matrices. Neuron SC r
    = 0.636 against null 0.596 +- 0.0016 (p = 2e-143); synapse SC r = 0.577 against 0.568 +- 0.0021 (p
    = 3e-6, below 0.05/6). Nine flies agree. Without nuisance removal the synapse SC is below the null
    (p = 0.0034); with left and right swapped it is below the null without reaching 0.05/6 (p = 0.0195),
    while the neuron SC stays above at p = 1e-58. The null totals match the selected total (p = 0.852).""",
"""  notes: Reciprocal SC (code target rc20_only1) against the 99 rd140-15 null SC matrices. Neuron SC r
    = 0.627 against null 0.587 +- 0.0016 (p = 3e-136); synapse SC r = 0.572 against 0.562 +- 0.0021 (p
    = 5e-7, below 0.05/6). Nine flies agree. Without nuisance removal the neuron SC is above the null without
    reaching 0.05/6 (p = 0.029) and the synapse SC is below it (p = 0.00017); with left and right swapped
    the synapse SC is below the null (p = 0.0021), while the neuron SC stays above at p = 6e-46. The null
    totals match the selected total (p = 0.852). No reader question was asked on this claim, so the claims
    file is unchanged; the values are those of the re-run of 2026-11-10, made without any change to the
    code. The first run gave neuron r = 0.636 and synapse r = 0.577 (p = 3e-6), with the swapped synapse
    SC below the null at p = 0.0195; the main outcome is the same.""")
# fig5b activation
rep("""    df 56, the README's value). One positive cluster of 399,973 voxels (README 416,801), maximum t = 16.1
    (README 14.7). LAL, FB, IPS and GNG all lie in it with peak t at least half the maximum (reading a)
    under the hemibrain and JFRC2010 atlases and with the binary regressor. Reading (b) fails for FB (mean-t
    rank 26 of 63, hemibrain atlas; 31 of 75, JFRC2010) and for LAL with JFRC2010. The claim holds under
    reading (a).""","""    df 56, the README's value). One positive cluster of 400,097 voxels (README 416,801), maximum t = 16.9
    (README 14.7). LAL, FB, IPS and GNG all lie in it with peak t at least half the maximum (reading a)
    under the hemibrain and JFRC2010 atlases and with the binary regressor. With the graded regressor and
    the hemibrain atlas all four also hold under reading (b) (FB mean-t rank 13 of 63); reading (b) fails
    for LAL with JFRC2010 and with the binary regressor. No reader question was asked on this claim, so
    the claims file is unchanged; the values are those of the re-run of 2026-11-10, made without any change
    to the code. The first run gave a cluster of 399,973 voxels, maximum t = 16.1, and reading (b) failing
    for FB (rank 26 of 63); the claim holds under reading (a) in both runs.""")
# fig5b suppression
rep("""  notes: 'No voxel in the brain mask falls below -3.242 (the lowest t is -0.82), so there is no negative
    cluster, under either regressor. WED(R) and AVLP(R) are mostly positive: 87 to 95% of their voxels
    are above the positive threshold (hemibrain atlas), 85 to 100% with JFRC2010. At the README''s negative
    peaks, (82,78,12) and (174,80,15), t = 3.28 and 4.09 here. The paper''s code found two small negative
    clusters (406 and 260 voxels); without the Tukey taper and the paper''s motion correction, this attempt
    finds none.'""","""  notes: 'No voxel in the brain mask falls below -3.242 (the lowest t is -0.66), so there is no negative
    cluster, under either regressor. WED(R) and AVLP(R) are mostly positive: 89 to 97% of their voxels
    are above the positive threshold (hemibrain atlas), 86 to 100% with JFRC2010. At the README''s negative
    peaks, (82,78,12) and (174,80,15), t = 3.78 and 4.76 here. The paper''s code found two small negative
    clusters (406 and 260 voxels); without the Tukey taper and the paper''s motion correction, this attempt
    finds none. No reader question was asked on this claim, so the claims file is unchanged; the values
    are those of the re-run of 2026-11-10, made without any change to the code. The first run gave a lowest
    t of -0.82 and peak t of 3.28 and 4.09, with the same outcome.'""")
# findings
rep("""    motion correction and obtains a FlyWire FC-SC correlation of 0.575 on the 63 primary ROIs where the""",
"""    motion correction and obtains a FlyWire FC-SC correlation of 0.563 (0.575 in a first run) on the 63 primary ROIs where the""")
rep("""to imaging. The seventh fly in that order (fly-100), the one the code leaves out, has a hemibrain
    ROI (AL(L)) only 65% inside the field of view after registration in this run, the lowest coverage
    of any fly, consistent with the paper's stated reason.""","""to imaging. The seventh fly in that order (fly-100), the one the code leaves out, has the lowest coverage
    of any fly after registration (in the re-run of 2026-11-10, 20 hemibrain ROIs partly outside the field
    of view, AL(L) 12% inside; 65% in the first run), consistent with the paper's stated reason.""")
open(p,'w').write(s)
EOF
grep -n "fig5b-walking-suppression" -A4 attempts/okuno-2025-01.yaml | head; grep -n "^- claim: fig5b-walking-suppression" -A30 attempts/okuno-2025-01.yaml | grep -n "First-level GLM without"
```

```
466:- claim: fig5b-walking-suppression
467-  outcome: not_reproduced
468-  notebook: reproduce_okuno_2025.ipynb
469:  output: claim:fig5b-walking-suppression
470-  assumed: true
471-  notes: 'No voxel in the brain mask falls below -3.242 (the lowest t is -0.66), so there is no negative
472-    cluster, under either regressor. WED(R) and AVLP(R) are mostly positive: 89 to 97% of their voxels
473-    are above the positive threshold (hemibrain atlas), 86 to 100% with JFRC2010. At the README''s negative
29:494-  - First-level GLM without the Tukey-taper pre-whitening, smoothing on the beta maps, and the README's
```

**Agent calls Bash**

```bash
cd  grep -n "0\.616\|0\.575\|0\.72\b\|0\.82\|399,973\|16\.1" attempts/okuno-2025-01.yaml entries/okuno-2025/reproduce_okuno_2025.ipynb | grep -v "first run\|earlier run\|first\|earlier" ; python tools/entry.py check entries/okuno-2025 2>&1 | tail -5
```

```
attempts/okuno-2025-01.yaml:179:    the paper's 0.72), with the same outcome.
attempts/okuno-2025-01.yaml:324:    eight flies. Neuron SC r = 0.623 against null 0.584 +- 0.0016 (p = 2e-128); synapse SC r = 0.575 against
attempts/okuno-2025-01.yaml:478:    t of -0.82 and peak t of 3.28 and 4.09, with the same outcome.'
entries/okuno-2025/reproduce_okuno_2025.ipynb:465:    "0.616 and 0.575 (the registration is not repeatable between runs); the outcome is the same."
entries/okuno-2025/reproduce_okuno_2025.ipynb:520:    "the same code gave 55 (swapped 49, per-region correlation with the paper's 0.72)."
entries/okuno-2025/reproduce_okuno_2025.ipynb:665:    "than the null for neuron SC (0.623 against 0.584 +- 0.002, p = 2e-128) and synapse SC (0.575\n",
entries/okuno-2025/reproduce_okuno_2025.ipynb:913:    "lowest t of -0.82 and the same outcome."
0 error(s)
```

**Agent**

The remaining matches are the intended earlier-run values, and the check passes with 0 errors. Next is the handover.

**Agent calls Bash**

```bash
cd  python tools/entry.py handover entries/okuno-2025 2>&1 | tail -8; ls executed/okuno-2025/handover; grep -c "earlier run\|\*\*Result" executed/okuno-2025/handover/*.ipynb; git status --short | grep -v "^??"; date -u
```

```
wrote executed/okuno-2025/handover
connectome_okuno_2025.ipynb
flyfc.py
okuno-2025.yaml
reproduce_okuno_2025.ipynb
executed/okuno-2025/handover/connectome_okuno_2025.ipynb:0
executed/okuno-2025/handover/reproduce_okuno_2025.ipynb:0
 M attempts/okuno-2025-01.yaml
 M entries/okuno-2025/reproduce_okuno_2025.ipynb
Tue Nov 10 08:49:46 UTC 2026
```

**Agent**

There were no questions to answer. `questions/okuno-2025.yaml` does not exist, and the answer run reported the same thing: the first author run asked a reader nothing, so the claims file was not amended. No claim needed re-running because of an answer.

## What I ran
- **Lock:** `entry.py lock` left the lock file unchanged.
- **Run:** `entry.py all` passed. The check gave 0 errors; `reproduce_okuno_2025.ipynb` took 1202 s and `connectome_okuno_2025.ipynb` 7 s. A second `check` after my edits also gave 0 errors.
- **Handover:** `entry.py handover` wrote `executed/okuno-2025/handover/`, with the conclusions removed.

## What changed anyway: the re-run gave different numbers
The code was unchanged, but the numbers moved. The registration is not repeatable between runs: the helper seeds ANTs but does not limit ITK's threads. In some variants the shift is well past the "second or third decimal" the record allowed for. fly-100's registration changed the most: 20 ROIs are now partly outside the field of view, with AL(L) 12% inside, against 65% in the first run.

The verifier gets this run's executed copy, so I updated the numbers in the notebook's conclusion cells, the summary, the attempt record's notes, `measured` values and two findings to match it. Each claim's notes say no question was asked, the claims file is unchanged, and what the first run gave. Statements, criteria and outcomes are untouched. I did not change the code.

| Claim | Before (first run) | Now (re-run) | Outcome |
|---|---|---|---|
| fig3d-flyem-vs-flywire | FlyEM 0.616, FlyWire 0.575 | 0.603, 0.563 | partially reproduced, unchanged |
| fig3e-flyem-higher-most-regions | 55 of 63 (swapped 49) | 56 of 63 (swapped 43) | reproduced, unchanged |
| fig3g-transmitter-correlation | ACh 0.013, GABA -0.157 | -0.024, -0.108 | not reproduced, unchanged |
| fig4e-unsegregated-higher | swapped-orientation synapse SC above the null (p = 0.0021) | swapped synapse SC not different from the null (p = 0.22) | reproduced, unchanged (main setting holds) |
| fig4f-segregated-lower | neuron 0.574, synapse 0.524 | 0.563, 0.517 | reproduced (reading a), unchanged |
| fig4i-reciprocal-higher | swapped synapse SC below the null at p = 0.0195 | below the null at p = 0.0021 | reproduced, unchanged |
| fig5b-walking-activation | reading (b) failed for FB (rank 26 of 63) | reading (b) holds for all four with the graded regressor and hemibrain atlas | reproduced, unchanged |
| fig5b-walking-suppression | lowest t -0.82 | lowest t -0.66 | not reproduced, unchanged |

The claims tested on the paper's own tables did not change: fig3a, fig3c, figs3-1a, fig3f and fig4b. Neither did any blocked claim.

The swapped-orientation and no-nuisance variants of the permutation tests, and fig5b's reading (b), depend on the run. CI will re-execute the notebook and can shift the numbers again. Making the registration deterministic, for example by fixing ITK's thread count, would need a code change and another full run, which I left for a later attempt.

Nothing is committed or pushed. The modified files are `attempts/okuno-2025-01.yaml` and `entries/okuno-2025/reproduce_okuno_2025.ipynb`.

## End of run

22 turns, 24 minutes, $1.27 at API prices, result: success.
