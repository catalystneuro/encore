# kim-2025 · verifier-2 · run 45002138435

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 700
drwxr-xr-x 6 runner runner    4096 Nov 22 09:38 .
drwxr-xr-x 8 runner runner    4096 Nov 22 09:38 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 22 08:07 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 22 08:07 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 22 09:38 .claude
-rw-r--r-- 1 runner runner       0 Nov 22 09:38 .env
-rw-r--r-- 1 runner runner       0 Nov 22 09:38 .env.development
-rw-r--r-- 1 runner runner       0 Nov 22 09:38 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 22 09:38 .env.local
-rw-r--r-- 1 runner runner       0 Nov 22 09:38 .env.production
-rw-r--r-- 1 runner runner       0 Nov 22 09:38 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 22 09:38 .env.test
-rw-r--r-- 1 runner runner       0 Nov 22 09:38 .env.test.local
drwx------ 2 runner runner    4096 Nov 22 09:38 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 22 08:07 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 22 08:07 .github
-rw-r--r-- 1 runner runner       0 Nov 22 09:38 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 22 08:07 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 22 08:07 .mcp.json
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; head -c 3000 kim-2025.yaml; echo; grep -n "^  - id:\|^- id:\|  id:" kim-2025.yaml | head -50
```

```
# Kim & Shin (2025) from dandiset 000248, with the Allen Visual Coding data

Tests the findings of [Kim & Shin (2025)](https://doi.org/10.1101/2025.06.30.662469) on
[DANDI:000248](https://dandiarchive.org/dandiset/000248/0.240502.2344), the Allen OpenScope
Illusion recordings the paper uses for its Isomap pictures (`reproduce_kim_2025.ipynb`). The
paper's main analyses use the Allen Visual Coding Neuropixels sessions; those claims are tested,
as data elsewhere, on the copies in [DANDI:000021](https://dandiarchive.org/dandiset/000021/0.251116.2246)
and [DANDI:000022](https://dandiarchive.org/dandiset/000022/0.251116.2247)
(`reproduce_kim_2025_allen.ipynb`, with decoding and the shuffled comparisons in
`reproduce_kim_2025_decoding.ipynb`).

| Claim | Data | Outcome |
|---|---|---|
| Dandiset 000248 holds the Illusion block, stimuli and units the paper's code uses | 000248 | Reproduced |
| Isomap manifolds: discontinuous at slope 0, overlapping at slope 2 | 000248 | Reproduced |
| Orthogonal variance of Lc1 larger toward faraway Ic1 than nearby Tre2 | 000248 | Reproduced |
| Geometry changes with slope as in the natural scenes data | 000248 | Reproduced |
| Unit and session counts; across-neuron slope near 1 | elsewhere | Reproduced (assumed AllenSDK "good" unit label, used in every Allen analysis) |
| Across-stimulus slope, behavioural state, higher visual areas | elsewhere | Reproduced |
| Noise correlations, dimensionality, occupancy, overlap, continuity | elsewhere | Reproduced |
[... 74 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "kim-2025-01.yaml"
}
```

```
1	schema_version: 3
2	id: kim-2025-01
3	datasets:
4	- archive: dandi
5	  id: 000248
6	  version: 0.240502.2344
7	  doi: 10.48324/dandi.000248/0.240502.2344
8	  relation: reuses
9	paper: doi:10.1101/2025.06.30.662469
10	date: '2026-11-21'
11	entry: kim-2025
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-18
20	  runner:
[... 749 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dump.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"===== [{i}] {c['cell_type']}")
    if c['cell_type']=='markdown':
        print(src)
    else:
        print(src[:int(sys.argv[2]) if len(sys.argv)>2 else 400])
        for o in c.get('outputs',[]):
            if 'text' in o: print('--OUT:', ''.join(o['text'])[:6000])
            elif 'data' in o and 'text/plain' in o['data']: print('--OUT:', ''.join(o['data']['text/plain'])[:4000])
            elif o.get('output_type')=='error': print('--ERR', o.get('ename'), o.get('evalue'))
EOF
python3 $TMPDIR/dump.py reproduce_kim_2025.ipynb 300 > $TMPDIR/nb1.txt; python3 $TMPDIR/dump.py reproduce_kim_2025_allen.ipynb 300 > $TMPDIR/nb2.txt; python3 $TMPDIR/dump.py reproduce_kim_2025_decoding.ipynb 600 > $TMPDIR/nb3.txt; wc -l $TMPDIR/nb*.txt
```

```
347 /tmp/claude-1001/nb1.txt
   549 /tmp/claude-1001/nb2.txt
   226 /tmp/claude-1001/nb3.txt
  1122 total
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb1.txt"
}
```

```
1	===== [0] markdown
2	# Reproducing Kim & Shin (2025) on dandiset 000248: the OpenScope Illusion data
3	
4	Paper: Kim, J. H. & Shin, H. (2025). "Neural variability structure in primary visual cortex is optimal for robust representation of visual similarity", bioRxiv doi:10.1101/2025.06.30.662469 (preprint of July 2025, the text the claims file was written from; the registry lists the later title "Intrinsic geometry of trial-to-trial variability in primary visual cortex is optimal for robust representation of visual similarity").
5	
6	Dataset: DANDI 000248, "Allen Institute Openscope - Illusion project", version 0.240502.2344, streamed from the archive. The paper cites the dandiset without a version. This is the only published version, so it is pinned. The paper's code read a post-processed copy dated 2024-01-30 ("OpenScopeData_00248_v240130_postprocessed"), before this version was published on 2024-05-02; no other published version exists to compare with.
7	
8	The paper uses this dandiset only for the Isomap pictures of Figures 1C, 3A, 3E and 3F and for one sentence of the Methods. Its main analyses are on the Allen Visual Coding Neuropixels data, which are tested in the second notebook of this entry (`reproduce_kim_2025_allen.ipynb`).
9	
10	| Claim | Data | Tested here |
11	|---|---|---|
12	| illusion-data-link | with_labels | yes |
13	| illusion-fig1c-isomap-geometry | dataset | yes |
14	| illusion-fig3a-orthogonal-variance-example | dataset | yes |
15	| illusion-geometry-similar-across-datasets | dataset | yes |
16	| all other claims | elsewhere (Allen Visual Coding Neuropixels) | second notebook |
17	
18	No result here depends on random draws (Isomap uses its dense eigensolver, and the decoding check uses unshuffled folds), so no seed is needed.
19	===== [1] code
20	import time
[... 328 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb2.txt"
}
```

```
1	===== [0] markdown
2	# Reproducing Kim & Shin (2025) on its main dataset: Allen Visual Coding Neuropixels natural scenes
3	
4	Paper: Kim, J. H. & Shin, H. (2025), bioRxiv doi:10.1101/2025.06.30.662469 (July 2025 preprint, the text the claims file was written from).
5	
6	The registry tests this paper on dandiset 000248, which the paper uses only for pictures (first notebook). Its findings rest on the Allen Brain Observatory Visual Coding Neuropixels data, "Brain Observatory 1.1" sessions, which the paper reads through AllenSDK without naming a release. These claims are `data: elsewhere`. Here they are tested on the same sessions as deposited on DANDI: dandiset 000021, "Allen Institute - Visual Coding - Neuropixels (Brain Observatory 1.1 Stimulus Set)", version 0.251116.2246 (doi:10.48324/dandi.000021/0.251116.2246), the only published version, streamed from the archive. The 32 session files it holds match the paper's 32 Brain Observatory 1.1 sessions in number.
7	
8	Units: those whose peak channel lies in the area (VISp for V1; VISl, VISrl, VISal, VISpm, VISam for LM, RL, AL, PM, AM), that pass the Allen quality criteria of the Methods (isi_violations < 0.5, amplitude_cutoff < 0.1, presence_ratio > 0.9) and whose `quality` label is "good". The label is an assumption: the Methods name only the three criteria, but the paper read the data through AllenSDK, whose default units table also keeps only units labelled "good" (`filter_by_validity`, allensdk/brain_observatory/ecephys/probes.py, lines 128 to 129, at commit a56bd8ea7613a812334602b64746cdd30c325a96), and the paper's unit counts match only with it. It is applied in every analysis; the Methods' three criteria alone are shown as a variant for the unit counts, the slope fits, behavioural state, higher visual areas and the movie data. The measures under slope manipulation were run with the Methods' criteria alone in the first round of this attempt and are not repeated here, for lack of time. Counts are spikes in the 
[... 425 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb2.txt",
 "offset": 433
}
```

```
433	===== [52] code
434	rsm_sp = lambda A, B: spearmanr(A.ravel(), B.ravel(), nan_policy="omit").statistic
435	r_4e = o1(across("rsm", rsm_sp), "RSM similarity across sessions", "session pairs")
436	--OUT: RSM similarity across sessions (n = 435 session pairs): {'peak_slope': 1.1, 'peak_mean': np.float64(0.3878), 'mean_asis': np.float64(0.3978), 'mean_slope0': np.float64(0.3483), 'mean_slope1': np.float64(0.3827), 'mean_slope2': np.float64(0.1862), 'p_slope0': 1.26e-51, 'p_slope2': 1.49e-70, 'ends_lower': True, 'reading_a': True, 'reading_b': True}
437	   curve: 0.0:0.348 0.1:0.348 0.2:0.349 0.3:0.350 0.4:0.352 0.5:0.355 0.6:0.358 0.7:0.363 0.8:0.369 0.9:0.376 1.0:0.383 1.1:0.388 1.2:0.385 1.3:0.366 1.4:0.336 1.5:0.305 1.6:0.276 1.7:0.250 1.8:0.227 1.9:0.205 2.0:0.186
438	
439	===== [53] markdown
440	**Result: fig4e-rsm-similarity-across-mice reproduced.** Over the 435 session pairs the mean RSM correlation peaks at slope 1.1 (0.388); slope 0 (0.348) and slope 2 (0.186) are lower than as-is (0.398), p = 1.3e-51 and 1.5e-70. The as-is value is higher than at any changed slope. Under the four further seeds the peak is at 1.1 each time (seed check at the end of `reproduce_kim_2025_decoding.ipynb`).
441	===== [54] code
442	def near_max(df, n_label):
443	    m, se = df[SLOPES].mean(), df[SLOPES].sem()
444	    peak = m.idxmax()
445	    a = bool(m[1.0] >= m.max() - se[peak])
446	    b = bool(0.8 <= peak <= 1.2)
447	    b2 = bool(0.7 <= peak <= 1.3)
448	    return dict(n=len(df), peak=peak, mean_at_1=round(m[1.0], 4), max=round(m.max(), 4), sem_
449	--OUT: LM within curve: 0.0:0.257 0.1:0.260 0.2:0.262 0.3:0.262 0.4:0.261 0.5:0.260 0.6:0.259 0.7:0.257 0.8:0.256 0.9:0.255 1.0:0.255 1.1:0.252 1.2:0.244 1.3:0.227 1.4:0.205 1.5:0.179 1.6:0.154 1.7:0.132 1.8:0.113 1.9:0.097 2.0:0.084
450	LM across curve: 0.0:0.215 0.1:0.214 0.2:0.214 0.3:0.214 0.4:0.214 0.5:0.215 0.6:0.216 0.7:0.217 0.8:0.220 0.9:0.223 1.0:0.227 1.1:0.230 1.2:0.230 1.3:0.222 1.4:0.206 1.5:0.184 1.6:0.159 1.7:0.1
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('reproduce_kim_2025_allen.ipynb'))
for i in (3,7,21,29,54,57):
    c=nb['cells'][i]; print(f'==== [{i}]'); print(''.join(c['source']))
c=nb['cells'][3]
for o in c['outputs']:
    if 'text' in o: print(''.join(o['text'])[-3500:])
EOF
```

```
==== [3]
with ProcessPoolExecutor(4, mp_context=mp.get_context("fork")) as ex:
    SQ = list(ex.map(K.abo_session, paths))     # units by the Methods' three criteria
S = [K.restrict(s, s["good"]) for s in SQ]      # main reading: also labelled "good", as AllenSDK serves them
print(f"loaded in {(time.time() - T0) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB")
rows = []
for i, (s, sq) in enumerate(zip(S, SQ)):
    v1 = s["area"] == "V1"
    lab = s["labels"]
    _, n = np.unique(lab, return_counts=True)
    rows.append(dict(index=i, session=s["info"]["path"].split("/")[0], trials=s["info"]["trials"], stimuli=len(n),
                     repeats_min=n.min(), repeats_max=n.max(),
                     **{f"{a}_q": int((sq["area"] == a).sum()) for a in K.ABO_AREAS},
                     **{f"{a}_g": int((s["area"] == a).sum()) for a in K.ABO_AREAS},
                     V1_all=s["info"]["area_units_all"]["V1"],
                     silent_V1=round(K.silent_fraction(s["X"][:, v1]), 4),
                     silent_V1_q=round(K.silent_fraction(sq["X"][:, sq["area"] == "V1"]), 4),
                     speed_mean=round(float(np.nanmean(s["speed"])), 2), eye=s["info"]["eye_tracking"]))
tab = pd.DataFrame(rows).set_index("index")
tab["included"] = tab.silent_V1 <= K.SILENT_TRIAL_LIMIT
[... 139 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "kim-2025.yaml",
 "offset": 30
}
```

```
30	#     "Brain Observatory 1.1" sessions, "natural scenes" block, read through AllenSDK. 32
31	#     sessions, one mouse each; 2 excluded for V1 (more than 10% of natural scenes trials with no
32	#     spikes in any unit), leaving 30 (the code drops session indices 0 and 6). 119 stimuli (118
33	#     natural scenes and a gray image), 250 ms each, no interval, 50 repeats in random order (one
34	#     session 47 to 50 repeats, subsampled to 47 for decoding and RSA). Spike counts in the 250 ms
35	#     from onset. Units kept when isi_violations < 0.5, amplitude_cutoff < 0.1 and presence_ratio
36	#     > 0.9. V1 has 64 +- 25 units per session (14 to 110). Higher visual areas LM, RL, AL, PM, AM
37	#     (one RL session also excluded). Running speed (moving when the trial mean speed is >= 1
38	#     cm/s) and pupil area (tertiles of the trial mean) for Figure S2. Natural movie one (30 s,
39	#     60 repeats) from 23 of 26 "Functional Connectivity" sessions, in 12-frame (400 ms) bins, 75
40	#     bins, for Figure S5A and S5B.
41	# (2) Allen Institute OpenScope Illusion dataset, dandiset 000248, used only for the Isomap
42	#     pictures of Figures 1C (bottom), 3A, 3E (left) and 3F (left). V1 spike counts in the 400
43	#     ms from stimulus onset, all stimuli with 400 repeats in the "ICwcfg1" block of one example
44	#     session. In the paper's code the data come from a post-processed MATLAB copy (folder
45	#     "OpenScopeData_00248_v240130_postprocessed") with 11 subjects, sub_619296, sub_620333,
46	#     sub_620334, sub_625545, sub_625554, sub_625555, sub_630506, sub_631510, sub_631570,
47	#     sub_633229 and sub_637484; the example is index 6, sub_630506. V1 units are those whose
48	#     location contains "VISp" and not "VISpm"; spike counts are the stored rate times 0.4 s; no
49	#     unit quality filter is applied in the code (a waveform-duration filter is commented out).
[... 640 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb3.txt"
}
```

```
1	===== [0] markdown
2	# Kim & Shin (2025) on the Allen Visual Coding Neuropixels data: decoding and shuffled noise correlations
3	
4	Paper: Kim, J. H. & Shin, H. (2025), bioRxiv doi:10.1101/2025.06.30.662469 (July 2025 preprint, the text the claims file was written from).
5	
6	Data: the Allen Brain Observatory Visual Coding Neuropixels "Brain Observatory 1.1" sessions as deposited in dandiset 000021, version 0.251116.2246 (doi:10.48324/dandi.000021/0.251116.2246), the only published version, streamed. These claims are `data: elsewhere`. Sessions, units and spike counts are those of the second notebook (`reproduce_kim_2025_allen.ipynb`), which also holds the data checks: V1 units passing the Methods' three quality criteria and labelled "good" (an assumption, stated there), spikes in the 250 ms from each natural scenes onset, and the 30 sessions left after the Methods' exclusion of sessions with more than 10% of trials silent in all V1 units.
7	
8	| Claim | Tested here |
9	|---|---|
10	| fig2b-decoding-falls-with-slope | blocked as too large; run in part, at as-is and slopes 0 and 1. On a four-session test run (four decodings in parallel on the runner's 4 CPUs) one 10-fold decoding took a median of 46 s as-is, 17 s at slope 0, 38 s at slope 1 and 521 s at slope 2 (up to 724 s), so slope 2 alone over 30 sessions would take about 65 minutes and the 22 conditions of the criterion several hours, over the sixty-minute limit of a notebook. The times of this run are printed below. |
11	| figs4c-shuffling-alters-dependence | decoding at as-is and slope 0; RSM similarity within and across mice (Figures 4C and 4E) at every slope |
12	
13	Seeds: each claim's generator is seeded with `zlib.crc32(b"kim-2025/<claim id>")`; a second generator of a claim adds 1. The decoding and the shuffled RSM comparison are run under the claim's seed only, for lack of time. The seed check of the RSM-based results of the second notebook (fig4c, fig4e, figs6), under the seed plus 1000, 2000, 3000 a
[... 214 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def decode_session" -A40 kim2025.py; grep -n "def shuffle_within_stimulus" -A15 kim2025.py
```

```
657:def decode_session(X, labels, target, seed, n_splits=10, shuffle_neurons=False):
658-    """Linear SVC (sklearn SVC, kernel linear, default C) accuracy of stimulus identity, 10-fold
659-    StratifiedKFold without shuffling after a random reordering of trials within stimulus, counts
660-    centred by the training mean per fold (RSA_decoding.py, decode_ABO). Trials are cut to the
661-    smallest repeat count. With shuffle_neurons, each neuron's trials are permuted within
662-    stimulus before the slope change (Figure S4C). target None is the as-is data."""
663-    from sklearn.model_selection import StratifiedKFold
664-    from sklearn.svm import SVC
665-    rng = np.random.default_rng(seed)
666-    stims, n = np.unique(labels, return_counts=True)
667-    R = n.min()
668-    T = np.stack([X[labels == c][:R] for c in stims])           # S x R x N
669-    if shuffle_neurons:
670-        for j in range(T.shape[2]):            # one permutation per neuron, as the code
671-            T[:, :, j] = T[:, rng.permutation(R), j]
672-    Xc = T.reshape(-1, T.shape[2])
673-    lab = np.repeat(stims, R)
674-    if target is not None:
675-        Xc = manipulate(Xc, lab, target)
676-    T = Xc.reshape(len(stims), R, -1)
[... 37 more lines not kept]
```

**Agent**

# Round 2 verification: Kim & Shin (2025), attempt kim-2025-01

## 1. Outcomes and assumptions

The claims file has 28 claims and the attempt record has 28 outcomes:
- 24 reproduced
- 4 blocked: fig2b (too_large), figs1 (other), fig2d (other)

I agree with all 28 outcomes. Notes on the ones that depend on a reading:

- **The `assumed: true` outcomes.** These are data-v1-units, fig1b-across-neuron, figs4ab, fig1d, figs5c, fig2a, fig2c, fig3bc, fig3d, fig3e, fig3f, fig4a, fig4c, fig4d, fig4e, figs6 and figs4c. Each states its assumption: the "good" unit label, plus the dependence on a blocked claim for figs4c. The assumption is reasonable. The paper's counts match only with the label (nb2 cell 7). The slope measures were not rerun with the Methods criteria alone, but in round 1 they all came out the same under that reading.
- **figs5a: reproduced.** I agree, but the outcome should be marked `assumed: true`. The count of 23 sessions (tolerance 0) is reached only by reading the paper's code: AllenSDK's invalid-presentation rule and ascending session-id order. The record's own finding says the Methods' word "truncated" does not describe this. The reading is well supported: sub-769319621 is the only one of the 26 sessions with invalid-interval frames, its longest repeat is 30.719 s and its longest frame gap 0.133 s (nb2 cell 57).
- **figs4c: reproduced.** I agree. One caveat: original and shuffled decoding use different seeds (SEED_2B and SEED_4C in `decode_session`), so the trial order and folds also differ. The slope-0 difference (0.787 against 0.765, p = 0.035, nb3 cell 9) is small, from one seed, and could partly reflect fold noise. As-is (p = 5e-05) and both RSM analyses are robust.
- **figs6: reproduced under reading (a).** This is correct by the criterion, and the weakness is disclosed (nb2 cell 54).
- **fig2b: blocked as too_large.** The claim is blocked, which I agree with. I cannot check the category against the protocol.

## 2. Text checked against printed outputs

Unsupported or wrong sentences:

- **nb2 cell 0:** "(decoding at as-is and slopes 0, 1 and 2 only)". Slope 2 was not run (nb3 cell 6: "slope 2 not run").
- **nb3 cell 0:** "The times of this run are printed below." The four-session test run is not in the notebook; cell 5 prints only the 30-session times. The attempt record itself says that run is "not in the entry".
- **Record, fig2b notes:** "the 150 decodings took 14.1 minutes … (median 22 s as-is … up to 105 s)". Cell 5 of nb3 prints 14.4 min, an as-is median of 21 s, and maxima of 100 s (original) and 119 s (shuffled).
- **Record, figs3 notes:** "The counts over all 32 sessions match the paper's". nb2 cell 59 says the same ("the sessions per higher visual area match the paper"). RL is 28 against the paper's 27 (nb2 cell 18). It matches only after the paper's one excluded RL session, which the notebook does not apply.
- **Record, figs5a notes, and nb2 cell 58:** "these are the sessions whose files hold an invalid_times interval tagged stimulus that overlaps natural movie one". This is shown only for the 26 sessions in 000022 (cell 57). Nothing printed checks sub-718643564 or sub-719828686.
- **nb2 cell 8, record data-v1-units, and nb2 cell 59:** "the first and seventh by session id" and "removes the same two sessions as the paper's code". Cell 3 prints DANDI indices 0 and 9 only; the session-id order is not printed. I confirmed it on the archive in round 1.
- **nb1 cell 21:** "The same holds in each of the 12 sessions". This is supported for slopes 0, 1 and 2 (cell 20 table), but not "every 0.1 step" per session. This is minor.

Everything else in the "Result" cells, the three Summaries, the README and the record notes matches the printed numbers.

My round-1 reasons are stated faithfully in my own terms in `verifications.results`.

## 3. Round-1 points

Resolved:
- **1 (unit reading):** the "good" units are now used throughout; the slope measures are marked assumed.
- **2 (figs5a session count):** the third excluded session is identified; one residual item below.
- **3 (figs5c grid):** compute_percent_filled is cited and the plateau is described.
- **4 (figs6 criterion):** reported, and a reader has been asked.
- **6 (trio component):** a full-graph column is added.
- **8 (shuffle):** the shuffle is now per neuron and used.
- **9, 10 and 11:** addressed.
- **7:** needed no action.

Partly resolved:
- **5 (figs4c and fig2b):** figs4c is now tested and fig2b was run in part.

What remains that bears on a conclusion:
- **figs5a:** add `assumed: true`, and print the invalid_times check for the two sessions in 000021.
- **fig2b:** the too_large estimate rests on a test run that is not in the entry. Slope 2 alone was estimated at about 65 min on 4 CPUs, and in its own notebook it would have allowed the criterion's "partial" judgement.
- **figs4c decoding:** the seed confound at slope 0 described above. Using the same seed for original and shuffled decoding would settle it.

## 4. Critical findings

The record's `findings` list has none rated `critical`. Finding 1 is major, 2 is minor, 3 is none, and findings 4 and 5 (methods_unavailable) carry no severity.

None of them describes a data error that would qualify. Finding 3's no-defect statements are supported by the clock and duplicate checks in nb1 cells 3, 5 and 6.

## End of run

12 turns, 3 minutes, $1.46 at API prices, result: success.
