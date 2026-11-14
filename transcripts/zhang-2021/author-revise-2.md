# zhang-2021 · author-revise-2 · run 43610164082

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/zhang-2021/verifier-2-report.md; ls entries/zhang-2021 questions paper | head -50
```

```
Sat Nov 14 15:33:10 UTC 2026
**Verifier report, round 2: zhang-2021-01**

The claims file has 11 claims and the attempt record has 11 outcomes, one per claim.

**1. Outcomes**

| claim | record | agree | assumption (`assumed: true`) |
|---|---|---|---|
| fig1-csi-s2 | reproduced | yes. Cell 17 prints R3 0.739, 0.717 and 0.676, all within tolerance and above every null value under both readings. R2 also passes. | Stated and reasonable. It does not decide the outcome, since R2 passes too. |
| att-csi-group | reproduced | yes. Cell 21 prints R3 means of 0.663, 0.730 and 0.525, and group reading (b) passes. | Stated and reasonable. |
| supp-csi-per-subject | reproduced | yes. Cell 24: 10 of 12 values within tolerance, and 12 of 12 have p < 0.01 under null (a). | Stated and reasonable. |
| att-passive-lower | not_reproduced | yes. Cell 27 counts 2 of 5 at the bound under every R3 combination, and at most 3 at p < 0.05. | none |
| att-classification | reproduced | yes. Cell 30: 43.7, 53.3 and 46.6% are within tolerance, and all four readings are above every null mean. | none |
| att-weights-cortex | reproduced | yes under the criterion: cell 34 gives 4 of 5 subjects under threshold (ii) for B, B_L and Q_S, and 3 of 5 under (i). The margin is thin; see 3. | Stated: atlas regions, a ridge parameter chosen per subject, a t test of r. Reasonable as a stand-in. The t test treats 5400 autocorrelated TRs as independent, which is liberal: 57 to 71% of region voxels pass (cell 33). |
| game-csi | reproduced | yes. Under reading (b), cell 38 gives 0.702 and 0.581. | none (lag +1 also passes, cell 39) |
| game-mutual-negative-projection | reproduced | yes under the dataset column order (cell 42). | Stated, and the reasoning is sound. The Table 1 order would give partially_reproduced, and the record says so. |
| fig3b-state-relations | reproduced | yes (cell 45). | none |
| game-classification | partially_reproduced | yes. Cell 48: S1 is above tolerance under every reading, and every
[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md
```

```
676 docs/protocol.md
1:# Protocol for an attempt
43:## Reader
45:### 1. Get the paper
59:### 2. Read the paper's code
69:### 3. Write the claims file
165:### 4. Data from outside the paper's own recordings
173:### 5. Check
186:### 6. Answer questions
199:## Author
215:### 1. Establish what can be tested
345:### 2. Check the data against its description
360:### 3. Write the entry
431:### 4. Lock, check and run
451:### 5. Record the attempt
524:### 6. Hand over for verification
562:## Repeat attempts
604:## Local and remote datasets
627:## Verifier
631:### Round 1: without the author's conclusions
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 199,215p docs/protocol.md; sed -n 431,562p docs/protocol.md; sed -n 656,676p docs/protocol.md
```

````
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
### 4. Lock, check and run

```bash
[... 150 more lines not kept]
````

**Agent calls Bash**

```bash
ls attempts | grep zhang; ls executed/zhang-2021 2>/dev/null; cat entries/zhang-2021/entry.yaml; cat entries/zhang-2021/README.md; wc -l entries/zhang-2021/statespace.py attempts/zhang-2021-01.yaml
```

```
zhang-2021-01.yaml
reproduce_zhang_2021.ipynb
result.json
schema_version: 1
name: zhang-2021
type: reproduction
title: Voxel-based state space modeling in a visual attention task and a video game (Zhang et al. 2021)
description: Tests the findings of Zhang, Gao, Cukur and Gallant (2021) on CRCNS data set vim-4, which
  holds deconvolved whole-cortex fMRI of five of the six subjects of a visual attention task and the
  BOLD data and behavioural state labels of the two subjects of a video game task. It recovers the
  supervised state space of each task, its cluster separation index, cross-validated classification
  and the projections between video game states. The functional ROIs behind the cortical maps are not
  in the data set; the cortical claims use public fsaverage atlases through the data set's mappers.
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_zhang_2021.ipynb
  title: Reproducing Zhang et al. (2021) from CRCNS vim-4
  runtime_minutes: 55
helpers:
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cat executed/zhang-2021/result.json; cd executed/zhang-2021 && python - <<'EOF'
import json
nb=json.load(open('reproduce_zhang_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"=== cell {i} [{c['cell_type']}] ===")
    print(src[:300])
EOF
```

```
{
 "entry": "zhang-2021",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_zhang_2021.ipynb",
   "ok": true,
   "seconds": 1465,
   "error": null
  }
 ]
}
=== cell 0 [markdown] ===
# Reproducing Zhang, Gao, Cukur & Gallant (2021) from CRCNS vim-4

Paper: Zhang T, Gao JS, Cukur T, Gallant JL (2021). Voxel-Based State Space Modeling Recovers
Task-Related Cognitive States in Naturalistic fMRI Experiments. Frontiers in Neuroscience
14:565976. doi:10.3389/fnins.2020.565976.

Claims
[... 373 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def \|zscore\|std(" entries/zhang-2021/statespace.py | head -80
```

```
63:def _open(path, block_size=2**24):
67:def read_hdf(path, keys=None):
74:def hdf_layout(path):
83:def npy_layout(path):
90:def load_attention_states():
95:def presence_code(states):
100:def gram_summary(Y):
102:    sd = Y.std(0)
109:def code_positions(X, Y, num_PCs=N_PCS):
123:    return stats.zscore(Y @ Q[:, :X.shape[1]])
126:def load_attention_gram(subject, X_check=None, keep=None):
147:def load_game(subject, keep=None):
178:def pca_scores(G, train, test=None, k=N_PCS):
205:def state_directions(Z, X):
218:def positions(Z, X, sign=None):
229:    pos = (pos - pos.mean(0)) / pos.std(0)
239:def _fit_normal(x):
245:def _logpdf(x, m, L):
251:def jsd(n1, n2, rng, samples=1000):
263:def csi(pos, members, rng, samples=1000):
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 95,240p entries/zhang-2021/statespace.py; sed -n 251,275p entries/zhang-2021/statespace.py; sed -n 540,604p entries/zhang-2021/statespace.py
```

```
def presence_code(states):
    """0 neither, 1 humans only, 2 vehicles only, 3 both (as in Example.ipynb)."""
    return (states[:, 0] + 2 * states[:, 1]).astype(int)


def gram_summary(Y):
    """Gram matrix and per-voxel summaries of a [TR x voxel] array."""
    sd = Y.std(0)
    return {"G": Y @ Y.T, "n_vox": Y.shape[1], "n_zero_vox": int((sd == 0).sum()),
            "vox_mean_range": (float(Y.mean(0).min()), float(Y.mean(0).max())),
            "vox_sd_range": (float(sd[sd > 0].min()), float(sd.max())),
            "n_nan": int(np.isnan(Y).sum())}


def code_positions(X, Y, num_PCs=N_PCS):
    """The paper's code, `extract_state_space_positions` (gallantlab/state-space
    at 6ffb3c3), on the full voxel data, kept as written to check the PC-space
    rewrite."""
    from scipy import stats
    from sklearn.decomposition import PCA
[... 216 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
for i in [10,11,13]:
    c=nb['cells'][i]
    print(f"=== cell {i} ===")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        print(''.join(o.get('text',''))[:3000])
EOF
grep -n -i "s7\b.*sd\|normali\|z-scor" attempts/zhang-2021-01.yaml | head -30
```

```
=== cell 10 ===
# Video game data
game = {}
for s in ss.GAME_SUBJECTS:
    t = time.time()
    g = ss.load_game(s, keep=game_keep.get(s))
    G = g["G"]
    Z, _, ve = ss.pca_scores(G, np.arange(len(G)))
    g["Z"], g["ve"] = Z, ve
    game[s] = g
    X = g["X"]
    nst = X.sum(1).astype(int)
    print(f"{s}: {X.shape[0]} TRs ({X.shape[0]*2.0045/60:.1f} min at TR 2.0045 s), {g['n_vox']} voxels "
          f"({g['n_zero_vox']} constant, {g['n_nan']} NaN), voxel means {g['vox_mean_range'][0]:.3f} to {g['vox_mean_range'][1]:.3f}, "
          f"SDs {g['vox_sd_range'][0]:.3f} to {g['vox_sd_range'][1]:.3f}; 24 PCs explain {ve:.1%}; {time.time()-t:.0f} s")
    print("   state labels (dataset order):", g["labels"])
    print("   TRs per state:", dict(zip(g["labels"], X.sum(0).astype(int))))
    print("   TRs with 0, 1, 2, 3 states:", np.bincount(nst, minlength=4))
    print("   TRs with exactly one state, per state:", dict(zip(g["labels"], X[nst == 1].sum(0).astype(int))))
    print("   safe explore and engage close together in", int(((X[:, g['labels'].index('safe explore')] > 0) & (X[:, g['labels'].index('engage close')] > 0)).sum()), "TRs")
[... 94 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims 2>/dev/null | grep zhang; f=$(ls claims/zhang-2021* 2>/dev/null || find . -path ./executed -prune -o -name "zhang-2021*.yaml" -print | grep -v attempts | head -3); echo $f
```

```
zhang-2021.yaml
claims/zhang-2021.yaml
```

**Agent calls Bash**

```bash
cd  grep -n "id:\|criterion" claims/zhang-2021.yaml | head -40; python -c "
import yaml;d=yaml.safe_load(open('claims/zhang-2021.yaml'))
for c in d['claims']:
  if c['id'] in ('att-weights-cortex','game-weights-two-groups'): print(yaml.dump(c,sort_keys=False,width=120))
"
```

```
74:- id: fig1-csi-s2
97:  criterion: State space as in the code (see the opening comment), fitted on S2's three
110:- id: att-csi-group
136:  criterion: Tolerances are the paper's stated spread across subjects. The CSI and permutation
145:- id: supp-csi-per-subject
195:  criterion: The values are read from the panels of Supplementary Figures 1 and 2 (S4, 0.64,
201:- id: att-passive-lower
215:  criterion: CSIs as in fig1-csi-s2. The paper does not give the form of this test. The
229:- id: att-classification
247:  criterion: Tolerance is the paper's stated spread across subjects. As in the Methods
261:- id: att-weights-cortex
273:  criterion: The ROIs were delineated per subject from functional localizer and retinotopic
291:- id: game-csi
310:  criterion: State space by the code's method on each subject's BOLD data (no deconvolution, as
319:- id: game-mutual-negative-projection
333:  criterion: State space as in game-csi. The code has no video game analysis, and two details
346:- id: fig3b-state-relations
362:  criterion: The figure's matrix was not available to this reader, so no per-pair result is
372:- id: game-classification
396:  criterion: Tolerances are the paper's stated spread across folds. Cross-validation as in
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "normaliz\|unit variance\|z-scor" paper/10.3389-fnins.2020.565976.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
for i in [33,34,35]:
    c=nb['cells'][i]
    print(f"=== cell {i} ===")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        print(''.join(o.get('text',''))[:6000])
        if 'data' in o and 'text/plain' in o['data']: print(''.join(o['data']['text/plain'])[:6000])
EOF
```

```
=== cell 33 ===
aw_rows, sem_fit = [], {}
for s in ss.ATT_SUBJECTS:
    t = time.time()
    r, alpha, n, mean_r = ss.semantic_model_r(s, sem, att_keep[s])
    p = ss.r_pvalue(r, n)
    sig = np.zeros(regmat[s].shape[0], bool)
    sig[att_keep[s][p < 0.05]] = True
    R_thr, nv_thr = ss.region_matrix(mappers[s], atlases, ss.ATT_REGIONS, voxel_mask=sig)
    sem_fit[s] = dict(alpha=alpha, n_vox=len(att_keep[s]), n_sig=int(sig.sum()))
    Yk = att[s]["Y_keep"].astype(np.float64)
    for thr, R in [("i", regmat[s]), ("ii", R_thr)]:
        W = ss.region_weights(att[s]["Z"], X_att, Yk @ R[att_keep[s]])
        for reading, w in W.items():
            for k, reg in enumerate(ss.ATT_REGIONS):
                aw_rows.append(dict(subject=s, threshold=thr, weights=reading, region=reg, human=w[k, 0], vehicle=w[k, 1]))
    print(f"{s}: WordNet model ridge parameter {alpha:g} (mean r per parameter {np.round(mean_r, 4).tolist()}), "
          f"{n} TRs; {sig.sum()} of {len(att_keep[s])} region voxels significant at p < 0.05 "
          f"({sig.sum() / len(att_keep[s]):.0%}); vertices per region after the threshold "
          f"{dict(zip(ss.ATT_REGIONS, nv_thr))}; {time.time()-t:.0f} s, peak memory {mem_gb():.1f} GB")
[... 145 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
for i in range(36,56):
    c=nb['cells'][i]
    print(f"=== cell {i} ===")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        print(''.join(o.get('text',''))[:5000])
EOF
```

```
<persisted-output>
Output too large (43.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d2a546e8-415d-49ec-b285-a9d65d8ab689/tool-results/b8yep80lr.txt

Preview (first 2KB):
=== cell 36 ===
## Video game task

States with no TRs are dropped (flash in S7; Supplementary Figure 4 shows no flash weights for
that subject), so S7's state space has 8 dimensions. Because the JSD is unchanged by affine maps,
the CSI does not depend on the order or signs of the dimensions; the dataset's column order is used.
=== cell 37 ===
### game-csi

> In the video game task the behavioural states are distinctly and significantly separated in the
> 9-dimensional state space, with CSI 0.72 in subject S1 and 0.62 in S7.
=== cell 38 ===
rng = np.random.default_rng(4)
exp_g = {"S1": (0.72, 0.072), "S7": (0.62, 0.062)}
game_csi = {}
for s in ss.GAME_SUBJECTS:
[... 22 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d2a546e8-415d-49ec-b285-a9d65d8ab689/tool-results/b8yep80lr.txt"
}
```

```
1	=== cell 36 ===
2	## Video game task
3	
4	States with no TRs are dropped (flash in S7; Supplementary Figure 4 shows no flash weights for
5	that subject), so S7's state space has 8 dimensions. Because the JSD is unchanged by affine maps,
6	the CSI does not depend on the order or signs of the dimensions; the dataset's column order is used.
7	=== cell 37 ===
8	### game-csi
9	
10	> In the video game task the behavioural states are distinctly and significantly separated in the
11	> 9-dimensional state space, with CSI 0.72 in subject S1 and 0.62 in S7.
12	=== cell 38 ===
13	rng = np.random.default_rng(4)
14	exp_g = {"S1": (0.72, 0.072), "S7": (0.62, 0.062)}
15	game_csi = {}
16	for s in ss.GAME_SUBJECTS:
17	    X, names = ss.game_matrix(game[s]["X"], game[s]["labels"], "dataset")
18	    Z = game[s]["Z"]
19	    pos = ss.positions(Z, X)
20	    for reading in "abc":
[... 578 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "GAME_REGIONS\|ATT_REGIONS" -A22 entries/zhang-2021/statespace.py | sed -n 1,70p; sed -n 604,669p entries/zhang-2021/statespace.py
```

```
39:  HCP-MMP1.0 areas (an assumption, listed in ATT_REGIONS and GAME_REGIONS); a
40-  region's mean of a voxel map is the mean over its fsaverage vertices that the
41-  mapper reaches. Weights per region are computed exactly from the
42-  region-averaged responses (region_weights). The encoding-model thresholds are
43-  the claims file's readings (ii), with the details stated in semantic_model_r
44-  and cv_ols_r.
45-"""
46-import fsspec
47-import h5py
48-import numpy as np
49-from scipy import linalg
50-
51-BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-4/live/"
52-DOI = "10.6080/K0668BDF"
53-VERSION = "unversioned"
54-ATT_SUBJECTS = ["S1", "S2", "S3", "S5", "S6"]  # S4 not released (data description)
55-GAME_SUBJECTS = ["S1", "S7"]
56-CONDITIONS = ["passive", "human", "vehicle"]  # stacking order of the code's Example.ipynb
57-N_PCS = 24  # Methods, "Voxel-Based State Space Modeling", paragraph 3
58-TABLE1_ORDER = ["dead", "round start", "safe explore", "unsafe explore", "kill",
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "_PFC" -B2 -A8 entries/zhang-2021/statespace.py | head -30; grep -n "regmat\|game_keep\|att_keep" executed/zhang-2021/reproduce_zhang_2021.ipynb | head; date -u
```

```
479-    "POS1 (HCP)": ("hcp", ["POS1"]),
480-}
481:_PFC = ["8C", "8Av", "i6-8", "s6-8", "SFL", "8BL", "9p", "9a", "8Ad", "p9-46v", "a9-46v", "46", "9-46d",
482-        "44", "45", "47l", "a47r", "p47r", "IFJa", "IFJp", "IFSa", "IFSp",
483-        "10d", "10pp", "a10p", "p10p", "11l", "13l", "OFC", "47m", "47s", "pOFC",
484-        "10r", "10v", "9m", "8BM", "p32", "d32", "s32", "a24", "25"]
485-GAME_REGIONS = {
486-    "TPJ": ("hcp", ["TPOJ1", "TPOJ2", "TPOJ3", "PGi", "PGs"]),
487-    "precuneus": ("hcp", ["7m", "PCV", "POS2", "31pd", "31pv"]),
488:    "prefrontal": ("hcp", _PFC),
489-    "motor": ("hcp", ["4"]),
490-    "premotor": ("hcp", ["6a", "6d", "6v", "6r", "55b", "PEF"]),
491-    "SMA": ("hcp", ["6ma", "6mp"]),
492-    "IPS": ATT_REGIONS["IPS"],
493-    "FEF": ("hcp", ["FEF"]),
494-    "SEF": ("hcp", ["SCEF"]),
495-}
496-
593:    "regmat, regvert = {}, {}\n",
595:    "    regmat[s], regvert[s] = ss.region_matrix(mappers[s], atlases, ss.ATT_REGIONS)\n",
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git diff --stat; git status --short; sed -n 1,45p entries/zhang-2021/statespace.py
```

```
tools/agent_run.py    | 15 +++++---
 tools/runner/chain.sh | 97 ++++++++++++++++++++++++++++++++-------------------
 2 files changed, 71 insertions(+), 41 deletions(-)
 M tools/agent_run.py
 M tools/runner/chain.sh
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
?? .zshrc
?? scripts
?? tools/replicates.py
"""Loading and state space measures for CRCNS vim-4 (Zhang, Gao, Cukur & Gallant 2021).

The data set is streamed from the public CRCNS bucket; nothing is written to disk.
[... 42 more lines not kept]
```

**Agent**

Now edit the helper: z-score the video game BOLD per voxel over the session (paper, Methods), keeping the as-stored summaries for the data check.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/zhang-2021/statespace.py",
 "old_string": "def load_game(subject, keep=None):\n    \"\"\"Stream one subject's video game BOLD (npy) and its state labels.\n\n    Also the voxel maps of the OLS weights B and denoised weights B_L of every state (data\n    set column order, states with no TRs dropped), for the correlation variant of\n    game-weights-two-groups, and with keep the responses of those voxels (float32).\n    \"\"\"\n    with _open(f\"VideoGame/Data/{subject}.npy\") as f:\n        np.lib.format.read_magic(f)\n        shape, fortran, dtype = np.lib.format.read_array_header_1_0(f)\n        Y = np.frombuffer(f.read(), dtype=dtype).reshape(shape).astype(np.float64)\n    out = gram_summary(Y)",
 "new_string": "def load_game(subject, keep=None, zscore=True):\n    \"\"\"Stream one subject's video game BOLD (npy) and its state labels.\n\n    With zscore, each voxel is z-scored over the session, as the paper's Methods say\n    (\"The detrended voxel responses were normalized to zero mean and unit variance\",\n    Preprocessing and Visualization) and as S1's deposited data already are; S7's are\n    not. The voxel summaries (means, SDs) are those of the data as stored.\n    Also the voxel maps of the OLS weights B and denoised weights B_L of every state (data\n    set column order, states with no TRs dropped), for the correlation variant of\n    game-weights-two-groups, and with keep the responses of those voxels (float32).\n    \"\"\"\n    with _open(f\"VideoGame/Data/{subject}.npy\") as f:\n        np.lib.format.read_magic(f)\n        shape, fortran, dtype = np.lib.format.read_array_header_1_0(f)\n        Y = np.frombuffer(f.read(), dtype=dtype).reshape(shape).astype(np.float64)\n    out = gram_summary(Y)\n    if zscore:\n        Y = (Y - Y.mean(0)) / Y.std(0)\n        out[\"G\"] = Y @ Y.T"
}
```

```
The file entries/zhang-2021/statespace.py has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/zhang-2021/statespace.py",
 "old_string": "    \"prefrontal\": (\"hcp\", _PFC),\n    \"motor\": (\"hcp\", [\"4\"]),\n    \"premotor\": (\"hcp\", [\"6a\", \"6d\", \"6v\", \"6r\", \"55b\", \"PEF\"]),\n    \"SMA\": (\"hcp\", [\"6ma\", \"6mp\"]),\n    \"IPS\": ATT_REGIONS[\"IPS\"],\n    \"FEF\": (\"hcp\", [\"FEF\"]),\n    \"SEF\": (\"hcp\", [\"SCEF\"]),\n}",
 "new_string": "    \"prefrontal\": (\"hcp\", _PFC),\n    \"motor\": (\"hcp\", [\"4\"]),\n    \"premotor\": (\"hcp\", [\"6a\", \"6d\", \"6v\", \"6r\", \"55b\", \"PEF\"]),\n    \"SMA\": (\"hcp\", [\"6ma\", \"6mp\"]),\n    \"IPS\": ATT_REGIONS[\"IPS\"],\n    \"FEF\": (\"hcp\", [\"FEF\"]),\n    \"SEF\": (\"hcp\", [\"SCEF\"]),\n    # variant, not used by the criterion: the medial prefrontal areas of _PFC only, the\n    # default-mode part of prefrontal cortex\n    \"medial prefrontal\": (\"hcp\", [\"10r\", \"10v\", \"10d\", \"9m\", \"8BM\", \"p32\", \"d32\", \"s32\", \"a24\", \"25\"]),\n}"
}
```

```
The file entries/zhang-2021/statespace.py has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/zhang-2021/statespace.py",
 "old_string": "        Y = (Y - Y.mean(0)) / Y.std(0)\n        out[\"G\"] = Y @ Y.T",
 "new_string": "        Y -= Y.mean(0)\n        Y /= Y.std(0)\n        out[\"G\"] = Y @ Y.T"
}
```

```
The file entries/zhang-2021/statespace.py has been updated successfully.
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('entries/zhang-2021/reproduce_zhang_2021.ipynb'))
print(len(nb['cells']))
for i in [6,10,13,33,34,52,53]:
    print(f"=== cell {i} ===")
    print(''.join(nb['cells'][i]['source'])[:3000])
EOF
```

```
56
=== cell 6 ===
# Cortical regions on fsaverage, for att-weights-cortex and game-weights-two-groups. The paper's ROIs are
# not public; two public atlases on fsaverage are read into memory and checked against their published
# checksums (visfAtlas, Rosenke et al. 2021; HCP-MMP1.0, Glasser et al. 2016, on fsaverage), and mapped
# to each subject's voxels with the data set's own mappers. A region's mean of a voxel map is the mean
# over the region's fsaverage vertices that the mapper reaches (helper, region_matrix).
atlases = ss.load_atlases()
mappers = {s: ss.load_mapper(s) for s in ss.ATT_SUBJECTS + ["S7"]}
regmat, regvert = {}, {}
for s in ss.ATT_SUBJECTS:
    regmat[s], regvert[s] = ss.region_matrix(mappers[s], atlases, ss.ATT_REGIONS)
regmat["game", "S7"], regvert["game", "S7"] = ss.region_matrix(mappers["S7"], atlases, ss.GAME_REGIONS)
print("fsaverage vertices per region (both hemispheres) in each atlas:",
      {k: int(sum(np.isin(atlases[a][h], areas).sum() for h in ("lh", "rh"))) for k, (a, areas) in {**ss.ATT_REGIONS, **ss.GAME_REGIONS}.items()})
print("vertices per region that each subject's mapper reaches (attention regions):")
print(pd.DataFrame({s: regvert[s] for s in ss.ATT_SUBJECTS}, index=list(ss.ATT_REGIONS)).T.to_string())
print("S7, video game regions:", dict(zip(ss.GAME_REGIONS, regvert["game", "S7"])))
att_keep = {s: np.nonzero((regmat[s] != 0).any(1))[0] for s in ss.ATT_SUBJECTS}
game_keep = {"S7": np.nonzero((regmat["game", "S7"] != 0).any(1))[0]}
[... 171 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
p='entries/zhang-2021/reproduce_zhang_2021.ipynb'
nb=json.load(open(p))
C=nb['cells']
def get(i): return ''.join(C[i]['source'])
def put(i,s): C[i]['source']=s.splitlines(keepends=True)
# cell 10: label z-scoring
s=get(10)
s=s.replace("# Video game data\n", "# Video game data. Each voxel is z-scored over the session, as the paper's Methods say (helper, load_game);\n# the voxel means and SDs printed are those of the data as stored.\n",1)
put(10,s)
# cell 33: Bonferroni variant
s=get(33)
old='''    R_thr, nv_thr = ss.region_matrix(mappers[s], atlases, ss.ATT_REGIONS, voxel_mask=sig)
'''
new='''    R_thr, nv_thr = ss.region_matrix(mappers[s], atlases, ss.ATT_REGIONS, voxel_mask=sig)
    # variant, not a reading of the claims file: Bonferroni over the region voxels, a far stricter test,
    # since the t test of r treats the 5400 autocorrelated TRs as independent
    sig_b = np.zeros(regmat[s].shape[0], bool)
    sig_b[att_keep[s][p < 0.05 / len(att_keep[s])]] = True
    R_b, nv_b = ss.region_matrix(mappers[s], atlases, ss.ATT_REGIONS, voxel_mask=sig_b)
'''
assert old in s; s=s.replace(old,new)
s=s.replace('for thr, R in [("i", regmat[s]), ("ii", R_thr)]:','for thr, R in [("i", regmat[s]), ("ii", R_thr), ("ii-bonf", R_b)]:')
old='''          f"({sig.sum() / len(att_keep[s]):.0%}); vertices per region after the threshold "
          f"{dict(zip(ss.ATT_REGIONS, nv_thr))}; {time.time()-t:.0f} s, peak memory {mem_gb():.1f} GB")'''
new='''          f"({sig.sum() / len(att_keep[s]):.0%}); vertices per region after the threshold "
          f"{dict(zip(ss.ATT_REGIONS, nv_thr))}; Bonferroni variant: {sig_b.sum()} voxels, vertices per region "
          f"{dict(zip(ss.ATT_REGIONS, nv_b))}; {time.time()-t:.0f} s, peak memory {mem_gb():.1f} GB")'''
assert old in s; s=s.replace(old,new)
put(33,s)
# cell 34: print threshold (ii) and Bonferroni-variant weights
s=get(34)
old='''print("\\nmean weights, threshold (i), OLS weights B (human / vehicle):")
t_ = aw[(aw.threshold == "i") & (aw.weights == "B")]
print(t_.assign(hv=[f"{h:+.3f} / {v:+.3f}" for h, v in zip(t_.human, t_.vehicle)])
      .pivot(index="region", columns="subject", values="hv").loc[list(ss.ATT_REGIONS)].to_string())
'''
new='''for thr in ["i", "ii", "ii-bonf"]:
    print(f"\\nmean weights, threshold ({thr}), OLS weights B (human / vehicle):")
    t_ = aw[(aw.threshold == thr) & (aw.weights == "B")]
    print(t_.assign(hv=[f"{h:+.3f} / {v:+.3f}" for h, v in zip(t_.human, t_.vehicle)])
          .pivot(index="region", columns="subject", values="hv").loc[list(ss.ATT_REGIONS)].to_string())
print("\\nEBA, human minus vehicle weight per subject (the region the outcome rests on):")
eba = aw[aw.region == "EBA"].assign(diff=lambda d: d.human - d.vehicle)
print(eba.pivot_table(index=["threshold", "weights"], columns="subject", values="diff").round(4).to_string())
'''
assert old in s; s=s.replace(old,new)
put(34,s)
# cell 53: medial prefrontal variant
s=get(53)
old='''gwc = pd.DataFrame(rows)
print("S7: dimensions failing the grouping (one may fail):")
print(gwc.to_string(index=False))
'''
new='''gwc = pd.DataFrame(rows)
print("S7: dimensions failing the grouping (one may fail):")
print(gwc.to_string(index=False))
def grouping_fails(gw_, r1):
    out = {}
    for (thr, reading), g in gw_.groupby(["threshold", "weights"]):
        t_ = g.pivot(index="state", columns="region", values="w")
        out[thr, reading] = [st_ for st_ in t_.index
                             if not (lambda own, other: (t_.loc[st_, own] > 0).all() and t_.loc[st_, own].mean() > t_.loc[st_, other].mean())(
                                 *((r1, R2_) if st_ in G1 else (R2_, r1)))]
    return out
# Variant not from the paper: the medial prefrontal areas only in place of the whole prefrontal region
print("\\nS7, medial prefrontal in place of prefrontal: dimensions failing (one may fail)")
for k, v in grouping_fails(gw, ["TPJ", "precuneus", "medial prefrontal"]).items():
    print(f"  threshold {k[0]:3s} {k[1]:14s} {len(v)} failing: {v}")
'''
assert old in s; s=s.replace(old,new)
put(53,s)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat entries/
```

```
entries/zhang-2021/reproduce_zhang_2021.ipynb | 37 ++++++++++++++++++++++-----
 entries/zhang-2021/statespace.py              | 13 +++++++++-
 2 files changed, 42 insertions(+), 8 deletions(-)
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
p='entries/zhang-2021/reproduce_zhang_2021.ipynb'
nb=json.load(open(p))
src='''# Variant: S7's video game BOLD as stored, without the z-scoring per voxel the paper describes (the analysis
# of the first two rounds, asked by the verifier to see what rests on it). The same measures for S7, with
# fewer permutations: game-csi (200), the two projections (2000), fig3b pair counts (2000, own sign, zero
# centre), game-classification (200) and the grouping of game-weights-two-groups.
t = time.time()
rng = np.random.default_rng(71)
raw = ss.load_game("S7", keep=game_keep["S7"], zscore=False)
raw["Z"] = ss.pca_scores(raw["G"], np.arange(len(raw["G"])))[0]
X, names = ss.game_matrix(raw["X"], raw["labels"], "dataset")
pos = ss.positions(raw["Z"], X)
for reading in "abc":
    mem = ss.game_members(X, names, reading)[0]
    v = np.mean([ss.csi(pos, mem, np.random.default_rng(k)) for k in range(10)])
    null = np.array([ss.csi(ss.positions(raw["Z"], Xp), ss.game_members(Xp, names, reading)[0], rng)
                     for Xp in (X[rng.permutation(len(X))] for _ in range(200))])
    print(f"S7 as stored, game-csi reading {reading}: CSI {v:.3f} (z-scored: {game_csi['S7', reading]:.3f}); "
          f"within 0.62 +/- 0.062: {abs(v - 0.62) <= 0.062}; null max {null.max():.3f}")
for order in ["dataset", "table1"]:
    Xo, nameso = ss.game_matrix(raw["X"], raw["labels"], order)
    perms = [rng.permutation(len(Xo)) for _ in range(2000)]
    M = ss.projection_matrix(ss.positions(raw["Z"], Xo, "own"), Xo)
    null = np.array([ss.projection_matrix(ss.positions(raw["Z"], Xo[q], "own"), Xo[q]) for q in perms])
    i, j = nameso.index("engage close"), nameso.index("safe explore")
    pl = [(1 + (null[:, a, b] <= M[a, b]).sum()) / 2001 for a, b in [(i, j), (j, i)]]
    d = len(nameso)
    p0 = (1 + (np.abs(null) >= np.abs(M)[None]).sum(0)) / 2001
    sig = (p0 < 0.01 / (d * (d - 1))) & ~np.eye(d, dtype=bool)
    print(f"S7 as stored, order {order}: engage close on safe explore {M[i, j]:.3f} (p {pl[0]:.4f}), safe explore on "
          f"engage close {M[j, i]:.3f} (p {pl[1]:.4f}); fig3b significant off-diagonal pairs (Bonferroni a, own sign, "
          f"zero centre, smallest p {1/2001:.1e}) {int(sig.sum())}, one direction only {int((sig != sig.T).sum() // 2)}")
game["S7 as stored"] = raw
gr = pd.DataFrame(game_classification("S7 as stored", X, names, rng, 200)[0])
gr["within"] = (gr.bal_acc - 30.4).abs() <= 4.2
print(gr[["folds", "labels", "rule", "bal_acc", "null_max", "p", "within"]].round(3).to_string(index=False))
Yr = raw["Y_keep"].astype(np.float64)
pr = ss.r_pvalue(ss.cv_ols_r(Yr, X), len(X))
sig_r = np.zeros(raw["n_vox"], bool)
sig_r[game_keep["S7"][pr < 0.05 / raw["n_vox"]]] = True
rows = []
for thr, R in [("i", regmat["game", "S7"]), ("ii", ss.region_matrix(mappers["S7"], atlases, ss.GAME_REGIONS, voxel_mask=sig_r)[0])]:
    S = Yr @ R[game_keep["S7"]]
    for order in ["dataset", "table1"]:
        Xo, nameso = ss.game_matrix(raw["X"], raw["labels"], order)
        for reading, w in ss.region_weights(raw["Z"], Xo, S).items():
            if reading != "Q_S" and order == "table1":
                continue
            rows += [dict(threshold=thr, weights=reading if reading != "Q_S" else f"Q_S ({order})", state=st_, region=reg, w=w[k, j])
                     for j, st_ in enumerate(nameso) for k, reg in enumerate(ss.GAME_REGIONS)]
print(f"S7 as stored, game-weights-two-groups ({sig_r.sum()} region voxels pass threshold ii): dimensions failing (one may fail)")
for k, v in grouping_fails(pd.DataFrame(rows), R1_).items():
    print(f"  threshold {k[0]:3s} {k[1]:14s} {len(v)} failing: {v}")
del game["S7 as stored"], raw, Yr
print(f"{time.time()-t:.0f} s; elapsed {time.time()-T0:.0f} s, peak memory {mem_gb():.1f} GB")
'''
cell={"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":src.splitlines(keepends=True)}
nb['cells'].insert(54,cell)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
python -c "import json;json.load(open('entries/zhang-2021/reproduce_zhang_2021.ipynb'))" && tail -c 200 entries/zhang-2021/reproduce_zhang_2021.ipynb | od -c | tail -3; git show HEAD:entries/zhang-2021/reproduce_zhang_2021.ipynb | tail -c 50 | od -c | tail -3
```

```
0000260  \n       "   n   b   f   o   r   m   a   t   _   m   i   n   o
0000300   r   "   :       5  \n   }  \n
0000310
0000040   o   r   m   a   t   _   m   i   n   o   r   "   :       5  \n
0000060   }  \n
0000062
```

**Agent calls Bash**

```bash
cd  date -u; timeout 7000 python tools/entry.py all entries/zhang-2021 2>&1 | tail -30; date -u
```

```
Sat Nov 14 15:35:49 UTC 2026
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
Installed kernelspec registry-zhang-2021 in executed/zhang-2021/.venv/share/jupyter/kernels/registry-zhang-2021
0 error(s)
pass  reproduce_zhang_2021.ipynb  (1458 s)
Sat Nov 14 16:00:18 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('entries/zhang-2021/reproduce_zhang_2021.ipynb'))
print(nb['nbformat'],nb['nbformat_minor'],[('id' in c) for c in nb['cells']][:5], 'id' in nb['cells'][54])
EOF
```

```
4 5 [True, True, True, True, True] False
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
for i in [7,15,17,21,24,27,30]:
    c=nb['cells'][i]
    print(f"=== cell {i} ===")
    for o in c.get('outputs',[]):
        print(''.join(o.get('text',''))[:6000])
        if 'data' in o and 'text/plain' in o['data']: print(''.join(o['data']['text/plain'])[:4000])
EOF
```

```
=== cell 7 ===
S1: 51608 voxels (14 constant, 0 NaN), voxel means -0.284 to 0.291, SDs 0.405 to 1.213; 24 PCs explain 84.1%; |weights| in PC space human 117, vehicle 106, attention 1.24e-14; the code's own OLS coefficients in voxel space, norm per row (human, vehicle, attention, intercept) [1.177e+02 1.063e+02 9.729e-14 8.956e+01]; |r| rewrite vs code per axis [1.     1.     0.2469]; mean r of same-frame TRs {'passive-human': 0.11415670411988853, 'passive-vehicle': 0.11058380055559039, 'human-vehicle': 0.23843833730092892}; 21 s, peak memory 3.1 GB

S2: 48819 voxels (0 constant, 0 NaN), voxel means -0.301 to 0.306, SDs 0.894 to 1.203; 24 PCs explain 89.7%; |weights| in PC space human 121, vehicle 123, attention 1.98e-14; the code's own OLS coefficients in voxel space, norm per row (human, vehicle, attention, intercept) [1.211e+02 1.236e+02 1.262e-13 9.676e+01]; |r| rewrite vs code per axis [1.     1.     0.1513]; mean r of same-frame TRs {'passive-human': 0.09946298979776792, 'passive-vehicle': 0.07050453268014109, 'human-vehicle': 0.2569188841368312}; 19 s, peak memory 3.2 GB

S3: 47512 voxels (0 constant, 0 NaN), voxel means -0.086 to 0.095, SDs 0.816 to 1.119; 24 PCs explain 68.4%; |weights| in PC space human 93.7, vehicle 102, attention 1.34e-14; the code's own OLS coefficients in voxel space, norm per row (human, vehicle, attention, intercept) [9.440e+01 1.029e+02 1.439e-13 9.746e+01]; |r| rewrite vs code per axis [1.     1.     0.0426]; mean r of same-frame TRs {'passive-human': 0.0072509360900333145, 'passive-vehicle': 0.005253922148821594, 'human-vehicle': 0.29216465972261224}; 41 s, peak memory 3.3 GB

S5: 52044 voxels (4 constant, 0 NaN), voxel means -0.280 to 0.291, SDs 0.425 to 1.198; 24 PCs explain 89.1%; |weights| in PC space human 114, vehicle 111, attention 1.84e-14; the code's own OLS coefficients in voxel space, norm per row (human, vehicle, attention, intercept) [1.139e+02 1.115e+02 1.226e-13 9.529e+01]; |r| rewrite vs code per axis [1.     1.    
[... 191 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
p='entries/zhang-2021/reproduce_zhang_2021.ipynb'
nb=json.load(open(p))
print([c['id'] for c in nb['cells'][:3]])
nb['cells'][54]['id']='s7-as-stored'
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
for i in list(range(33,35))+[10]:
    c=nb['cells'][i]
    print(f"=== cell {i} ===")
    for o in c.get('outputs',[]):
        print(''.join(o.get('text',''))[:9000])
EOF
```

```
['1cc3c57c', '03b59e49', '20a7d072']
=== cell 33 ===
S1: WordNet model ridge parameter 10000 (mean r per parameter [0.023000000044703484, 0.03909999877214432, 0.050700001418590546, 0.05079999938607216, 0.04450000077486038]), 5400 TRs; 3835 of 5965 region voxels significant at p < 0.05 (64%); vertices per region after the threshold {'FFA': 1670, 'OFA': 618, 'EBA': 3737, 'MT+': 789, 'PPA': 2530, 'OPA': 1080, 'RSC': 872, 'LO': 1735, 'FO': 2625, 'IFS': 1288, 'IPS': 10473, 'FEF': 1097, 'SEF': 978, 'LOS-bodies': 1194, 'ITG-bodies': 1598, 'MTG-bodies': 945, 'OTS-bodies': 535, 'FFC (HCP)': 1462, 'PHA1-3 (HCP)': 2103, 'POS1 (HCP)': 1285}; Bonferroni variant: 2266 voxels, vertices per region {'FFA': 1240, 'OFA': 446, 'EBA': 2989, 'MT+': 661, 'PPA': 1590, 'OPA': 843, 'RSC': 290, 'LO': 1530, 'FO': 533, 'IFS': 631, 'IPS': 6485, 'FEF': 690, 'SEF': 242, 'LOS-bodies': 1124, 'ITG-bodies': 1358, 'MTG-bodies': 507, 'OTS-bodies': 226, 'FFC (HCP)': 1088, 'PHA1-3 (HCP)': 969, 'POS1 (HCP)': 568}; 72 s, peak memory 5.8 GB

S2: WordNet model ridge parameter 10000 (mean r per parameter [0.023900000378489494, 0.0364999994635582, 0.04670000076293945, 0.04740000143647194, 0.04179999977350235]), 5400 TRs; 3745 of 5908 region voxels significant at p < 0.05 (63%); vertices per region after the threshold {'FFA': 1578, 'OFA': 570, 'EBA': 4107, 'MT+': 867, 'PPA': 2400, 'OPA': 980, 'RSC': 565, 'LO': 1610, 'FO': 1891, 'IFS': 1375, 'IPS': 10747, 'FEF': 1227, 'SEF': 1058, 'LOS-bodies': 1119, 'ITG-bodies': 1453, 'MTG-bodies': 1535, 'OTS-bodies': 673, 'FFC (HCP)': 1478, 'PHA1-3 (HCP)': 1830, 'POS1 (HCP)': 1269}; Bonferroni variant: 2056 voxels, vertices per region {'FFA': 1182, 'OFA': 418, 'EBA': 3203, 'MT+': 776, 'PPA': 1779, 'OPA': 757, 'RSC': 84, 'LO': 1347, 'FO': 122, 'IFS': 469, 'IPS': 5658, 'FEF': 915, 'SEF': 225, 'LOS-bodies': 988, 'ITG-bodies': 1027, 'MTG-bodies': 1188, 'OTS-bodies': 278, 'FFC (HCP)': 1105, 'PHA1-3 (HCP)': 944, 'POS1 (HCP)': 761}; 71 s, peak memory 5.8 GB

S3: WordNet model ridge p
[... 199 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
for i in [11,12,38,39,42]+list(range(48,56)):
    c=nb['cells'][i]
    if c['cell_type']!='code': continue
    print(f"=== cell {i} ===")
    for o in c.get('outputs',[]):
        t=''.join(o.get('text',''))
        if i==53: t=t[:2600]
        print(t[:7000])
EOF
```

```
=== cell 11 ===
S1: 1950 TRs; consecutive-TR correlation median 0.318, 1st percentile 0.079; the 8 lowest at the start of TRs [172, 325, 650, 869, 975, 1300, 1625, 1739] (values [-0.027, -0.462, -0.469, 0.007, -0.477, -0.467, -0.441, 0.005]); gaps between them [172, 153, 325, 219, 106, 325, 325, 114, 211]
S7: 1320 TRs; consecutive-TR correlation median 0.377, 1st percentile 0.097; the 8 lowest at the start of TRs [30, 31, 66, 237, 243, 440, 880, 1036] (values [0.051, -0.178, 0.004, 0.037, 0.057, -0.082, -0.027, 0.034]); gaps between them [30, 1, 35, 171, 6, 197, 440, 156, 284]

=== cell 12 ===
lag        -10    -4     -2     -1      0      1      2      3     4     6      10
subject                                                                           
S1       0.514  0.538  0.569  0.629  0.691  0.729  0.687  0.606  0.60  0.59  0.518
S7       0.454  0.464  0.500  0.510  0.550  0.566  0.553  0.558  0.53  0.53  0.537
lag of the peak per subject: {'S1': 1, 'S7': 1}

=== cell 38 ===
S1 reading a: 8 clusters (sizes [72, 183, 488, 812, 53, 141, 208, 64]; dropped [('flash', 9)]); CSI 0.694 (seed SD 0.003); expected 0.72 +/- 0.072, within: True; null mean 0.192, max 0.258; above every null value: True

S1 reading b: 7 clusters (sizes [58, 142, 477, 762, 41, 141, 208]; dropped [('flash', 1), ('kill', 0)]); CSI 0.702 (seed SD 0.004); expected 0.72 +/- 0.072, within: True; null mean 0.202, max 0.270; above every null value: True

S1 reading c: 3 clusters (sizes [488, 72, 1390]; dropped []); CSI 0.513 (seed SD 0.008); expected 0.72 +/- 0.072, within: False; null mean 0.133, max 0.268; above every null value: True

S7 reading a: 8 clusters (sizes [160, 199, 265, 414, 16, 75, 176, 119]; dropped []); CSI 0.549 (seed SD 0.003); expected 0.62 +/- 0.062, within: False; null mean 0.232, max 0.295; above every null value: True

[... 169 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
p='entries/zhang-2021/reproduce_zhang_2021.ipynb'
nb=json.load(open(p))
c=nb['cells'][54]; s=''.join(c['source'])
reps=[("the two projections (2000), fig3b pair counts (2000, own sign, zero\n# centre)","the two projections and fig3b pair counts (20,000, own sign, zero\n# centre, Bonferroni a)"),
("perms = [rng.permutation(len(Xo)) for _ in range(2000)]","perms = [rng.permutation(len(Xo)) for _ in range(N_PERM_G)]"),
("pl = [(1 + (null[:, a, b] <= M[a, b]).sum()) / 2001 for a, b in [(i, j), (j, i)]]","pl = [(1 + (null[:, a, b] <= M[a, b]).sum()) / (N_PERM_G + 1) for a, b in [(i, j), (j, i)]]"),
("p0 = (1 + (np.abs(null) >= np.abs(M)[None]).sum(0)) / 2001","p0 = (1 + (np.abs(null) >= np.abs(M)[None]).sum(0)) / (N_PERM_G + 1)"),
("(p {pl[0]:.4f})","(p {pl[0]:.5f})"),("(p {pl[1]:.4f})","(p {pl[1]:.5f})"),
('f"zero centre, smallest p {1/2001:.1e}) {int(sig.sum())}','f"zero centre) {int(sig.sum())}'),
]
for a,b in reps:
    assert a in s,a; s=s.replace(a,b)
c['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
print(s[:1800])
EOF
```

```
# Variant: S7's video game BOLD as stored, without the z-scoring per voxel the paper describes (the analysis
# of the first two rounds, asked by the verifier to see what rests on it). The same measures for S7, with
# fewer permutations: game-csi (200), the two projections and fig3b pair counts (20,000, own sign, zero
# centre, Bonferroni a), game-classification (200) and the grouping of game-weights-two-groups.
t = time.time()
rng = np.random.default_rng(71)
raw = ss.load_game("S7", keep=game_keep["S7"], zscore=False)
raw["Z"] = ss.pca_scores(raw["G"], np.arange(len(raw["G"])))[0]
X, names = ss.game_matrix(raw["X"], raw["labels"], "dataset")
pos = ss.positions(raw["Z"], X)
for reading in "abc":
    mem = ss.game_members(X, names, reading)[0]
    v = np.mean([ss.csi(pos, mem, np.random.default_rng(k)) for k in range(10)])
    null = np.array([ss.csi(ss.positions(raw["Z"], Xp), ss.game_members(Xp, names, reading)[0], rng)
                     for Xp in (X[rng.permutation(len(X))] for _ in range(200))])
    print(f"S7 as stored, game-csi reading {reading}: CSI {v:.3f} (z-scored: {game_csi['S7', reading]:.3f}); "
          f"within 0.62 +/- 0.062: {abs(v - 0.62) <= 0.062}; null max {null.max():.3f}")
for order in ["dataset", "table1"]:
    Xo, nameso = ss.game_matrix(raw["X"], raw["labels"], order)
    perms = [rng.permutation(len(Xo)) for _ in range(N_PERM_G)]
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; timeout 7000 python tools/entry.py all entries/zhang-2021 2>&1 | tail -4; date -u; python - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
for i in [15,17,42,48,54]:
    for o in nb['cells'][i].get('outputs',[]):
        print(''.join(o.get('text',''))[:2500])
EOF
```

```
Sat Nov 14 16:00:58 UTC 2026
Installed kernelspec registry-zhang-2021 in executed/zhang-2021/.venv/share/jupyter/kernels/registry-zhang-2021
0 error(s)
pass  reproduce_zhang_2021.ipynb  (1416 s)
Sat Nov 14 16:24:42 UTC 2026
S1 done in 28 s

S2 done in 28 s

S3 done in 28 s

S5 done in 27 s

S6 done in 27 s
   subject condition  R3_code  R3_seed_sd  R2_median  R2_5pct  R2_95pct  R1_2d  null3d_max_a  null2d_max_a  null3d_max_b  null2d_max_b
0       S1   passive    0.621       0.007      0.638    0.616     0.658  0.609         0.055         0.035         0.334         0.315
1       S1     human    0.512       0.007      0.543    0.503     0.609  0.483         0.045         0.037         0.336         0.297
2       S1   vehicle    0.745       0.008      0.762    0.730     0.790  0.716         0.053         0.041         0.088         0.067
3       S2   passive    0.676       0.005      0.657    0.638     0.681  0.632         0.062         0.042         0.352         0.332
4       S2     human    0.739       0.005      0.723    0.683     0.784  0.664         0.040         0.030         0.322         0.283
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
for i in [27,45]:
    for o in nb['cells'][i].get('outputs',[]):
        t=''.join(o.get('text',''))
        print(t[4500:] if i==27 else t[:5200])
EOF
```

```
78     0.0343  0.0411   0.0160     0.0649  0.0190       False       False  False   True
     S5      R1  global    i   0.5918 0.6396   0.6261   0.0478     0.0343  0.0411   0.0519     0.1239  0.0549       False       False  False  False
     S5      R1  global   ii   0.5918 0.6396   0.6261   0.0478     0.0343  0.0411   0.0689     0.1189  0.0619       False       False  False  False
     S6      R3 matched    i   0.6517 0.6060   0.6998  -0.0457     0.0481  0.0012   0.9780     0.0170  0.4635       False       False  False  False
     S6      R3 matched   ii   0.6517 0.6060   0.6998  -0.0457     0.0481  0.0012   0.9750     0.0260  0.4605       False       False  False  False
     S6      R3  global    i   0.6517 0.6060   0.6998  -0.0457     0.0481  0.0012   0.9500     0.0470  0.5085       False       False  False  False
     S6      R3  global   ii   0.6517 0.6060   0.6998  -0.0457     0.0481  0.0012   0.9530     0.0410  0.5025       False       False  False  False
     S6      R1 matched    i   0.5994 0.5755   0.6889  -0.0239     0.0896  0.0328   0.8212     0.0010  0.0390       False       False  False   True
     S6      R1 matched   ii   0.5994 0.5755   0.6889  -0.0239     0.0896  0.0328   0.8601     0.0010  0.0509       False       False  False  False
     S6      R1  global    i   0.5994 0.5755   0.6889  -0.0239     0.0896  0.0328   0.7942     0.0010  0.0849       False       False  False  False
     S6      R1  global   ii   0.5994 0.5755   0.6889  -0.0239     0.0896  0.0328   0.8112     0.0020  0.1039       False       False  False  False

subjects of 5 with passive significantly lower:
                      a_at_bound  b_at_bound  a_p05  b_p05
variant scheme  null                                      
R1      global  i              1           1      1      1
                ii             1           1      1      1
        matched i              1           1      1      4
                ii             1           1      1      3
R3      global  i            
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
t=''.join(o.get('text','') for o in nb['cells'][45]['outputs'])
i=t.find('smallest'); print(t[i:i+2500])
t=''.join(o.get('text','') for o in nb['cells'][53]['outputs'])
print(t[2400:5200])
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
TypeError: sequence item 0: expected str instance, list found
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
J=lambda c: ''.join(''.join(o.get('text','')) for o in c['outputs'])
t=J(nb['cells'][45]); i=t.find('smallest'); print(t[i:i+2500])
t=J(nb['cells'][53]); print(t[2400:5600])
EOF
```

```
smallest attainable p: 5.00e-05
order table1  sign own  centre zero      Bonferroni a: S1 45, S7 25, shared 19, sets differ: True
order table1  sign own  centre null mean Bonferroni a: S1 44, S7 26, shared 19, sets differ: True
order table1  sign own  centre zero      Bonferroni b: S1 45, S7 25, shared 19, sets differ: True
order table1  sign own  centre null mean Bonferroni b: S1 44, S7 26, shared 19, sets differ: True
order table1  sign diag centre zero      Bonferroni a: S1 45, S7 25, shared 19, sets differ: True
order table1  sign diag centre null mean Bonferroni a: S1 45, S7 26, shared 20, sets differ: True
order table1  sign diag centre zero      Bonferroni b: S1 45, S7 25, shared 19, sets differ: True
order table1  sign diag centre null mean Bonferroni b: S1 45, S7 26, shared 20, sets differ: True
order dataset sign own  centre zero      Bonferroni a: S1 48, S7 21, shared 12, sets differ: True
order dataset sign own  centre null mean Bonferroni a: S1 48, S7 22, shared 12, sets differ: True
order dataset sign own  centre zero      Bonferroni b: S1 48, S7 21, shared 12, sets differ: True
order dataset sign own  centre null mean Bonferroni b: S1 48, S7 22, shared 12, sets differ: True
order dataset sign diag centre zero      Bonferroni a: S1 48, S7 21, shared 12, sets differ: True
order dataset sign diag centre null mean Bonferroni a: S1 48, S7 22, shared 12, sets differ: True
order dataset sign diag centre zero      Bonferroni b: S1 48, S7 21, shared 12, sets differ: True
order dataset sign diag centre null mean Bonferroni b: S1 48, S7 22, shared 12, sets differ: True

S1, Table 1 order, own sign: mean position of row state's TRs on column dimension
                dead  round start  safe explore  unsafe explore  kill  engage close  engage far  flash  run away
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
J=lambda c: ''.join(''.join(o.get('text','')) for o in c['outputs'])
t=J(nb['cells'][53]); i=t.find('S7 BL maps'); print(t[i:i+300])
t=J(nb['cells'][45]); i=t.find('S1 significant pairs'); print(t[i-1500:i])
print(J(nb['cells'][9])[-1500:])
EOF
```

```
S7 BL maps: clusters {1: ['safe explore', 'unsafe explore'], 2: ['engage close', 'engage far', 'run away', 'dead', 'round start', 'kill']}
                engage close  engage far  safe explore  unsafe explore  run away  dead  round start  kill
engage close            1.00        0.32         -0.61 
         -0.25  1.19          0.15        0.10  -0.01      0.01
engage close   -1.19        -0.80         -0.70           -0.01 -0.01          0.84       -0.05   0.00     -0.04
engage far     -0.92        -0.69         -0.53            0.21  0.26          0.24        0.84  -0.00     -0.02
flash          -0.59         0.93         -0.72            0.54  0.11          0.62        0.46   1.89      1.31
run away       -1.08        -0.52         -0.75            0.90  0.52          0.24       -0.04  -0.15      1.48

S7, Table 1 order, own sign
                dead  round start  safe explore  unsafe explore  kill  engage close  engage far  run away
dead            0.88         0.16         -0.14           -0.18  0.03          0.04       -0.05      0.00
round start     0.23         0.80          0.09           -0.09  0.05         -0.02       -0.08     -0.02
safe explore   -0.45         0.11          0.78            0.00  0.04         -0.02       -0.09     -0.02
unsafe explore -0.22        -0.21         -0.02            0.46  0.01          0.00       -0.05     -0.00
kill            0.44        -0.10         -0.62           -0.80  0.37          0.28        0.09      0.05
engage close    0.32        -0.10         -0.56           -0.60  0.10          0.66       -0.10      0.03
engage far      0.31        -0.45         -0.56           -0.22 -0.33         -0.46        0.62     -0.01
run away        0.63        -0.19         -0.79           -0.85  0.73          0.71       -1.05      1.54

[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('entries/zhang-2021/reproduce_zhang_2021.ipynb'))
for i in [19,22,25,26,28,31]:
    print(f"=== cell {i} ===");print(''.join(nb['cells'][i]['source']))
EOF
```

```
=== cell 19 ===
**Result: reproduced, resting on an assumption about the third axis.** With the paper's code (R3)
the S2 CSIs are 0.743 (attend-humans), 0.721 (attend-vehicles) and 0.675 (passive), all within
tolerance of 0.75, 0.69 and 0.67, and each exceeds every one of 1000 null values under both
permutation readings (null maxima 0.040 to 0.062 under (a), 0.322 to 0.352 under (b); p <= 0.001,
the bound 1000 permutations reach, not the paper's 1e-5). The median over random third axes (R2)
also matches (0.723, 0.718, 0.657). In the human-vehicle plane alone (R1) the attend-humans CSI is
0.664, outside tolerance. The third axis of the state space has no weight in these data, so the
values depend on it: over random third axes the attend-humans CSI ranges from 0.683 to 0.784 (5 to
95%), within tolerance throughout.
=== cell 22 ===
**Result: reproduced, resting on an assumption about the third axis.** Over the five released
subjects, R3 gives mean CSIs of 0.665 +/- 0.104 (attend-humans), 0.731 +/- 0.023 (attend-vehicles)
and 0.524 +/- 0.260 (passive), all within the paper's spreads of 0.66 +/- 0.09, 0.74 +/- 0.03 and
0.53 +/- 0.24; R2 gives 0.658, 0.728 and 0.523. Under group reading (b), each mean exceeds the
maximum of the mean null CSIs (at most 0.110). Under reading (a), every subject is significant in
the attentive conditions but not in passive, where S3's CSI (0.061) does not exceed its null. In
the plane alone (R1) the attend-vehicles mean, 0.675, is outside tolerance. The second reference,
the means of the paper's own per-subject values over these subjects (0.644, 0.728, 0.512), is also
close to the R3 means.
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('entries/zhang-2021/reproduce_zhang_2021.ipynb'))
s=''.join(nb['cells'][13]['source']); print(s[s.find('- Labels and BOLD'):])
print("=== 55 ===");print(''.join(nb['cells'][55]['source']))
EOF
```

```
- Labels and BOLD share a clock as far as shifted labels show: the attention CSI peaks at lag 0,
  as deconvolved data should. The game CSI peaks at lag +1 TR in both subjects (S1 0.729 against
  0.691 at lag 0; S7 0.569 against 0.547), as a hemodynamic delay in data that are not deconvolved
  would give. The paper does not say whether the game labels were shifted; lag 0 is used, and the
  game CSI and classification are also shown at lag +1. This is consistent with, not proof of,
  aligned labels.
- Video game: S7 has 1320 TRs (44 min, the paper's 45 min). S1 has 1950 TRs, 65 min, where the
  paper says one subject played 90 min in six 15-min runs. The correlation of consecutive TRs
  drops to -0.44 to -0.48 exactly at TRs 325, 650, 975, 1300 and 1625, so S1's data are six
  blocks of 325 TRs (10.9 min each), as six runs of the 325-volume length the paper gives for its
  acquisitions would be. The deposited S1 data are therefore six whole runs, consistent with the
  paper's six runs but not with its 15 minutes per run. In S7 the dips at TRs 440 and 880 are
  weaker (-0.08 and -0.03), consistent with three runs of 440 TRs (14.7 min). The S7 data are float32 and not exactly
  z-scored per voxel over the session; S1's are. No flash TRs in S7, as the paper says. The S1
  game data have 73,594 voxels, which matches no mapper (S1's mapper has 51,608, as the S1
  attention data), nor any of the superseded mappers in `Mappers/old` (S1 81,137, S5 84,038, S6
  86,842), so S1's game weights cannot be put on fsaverage with the files given. S7's
  data match S7's mapper. The game state columns are not in the order of Table 1.
- No recording is deposited twice: same-frame TRs of different conditions are only weakly
  correlated (printed above), and the subjects' voxel counts all differ.
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('entries/zhang-2021/reproduce_zhang_2021.ipynb'))
for i in [35,36,40,43,46,50,51,56]:
    print(f"=== cell {i} ===");print(''.join(nb['cells'][i]['source']))
EOF
```

```
=== cell 35 ===
**Result: reproduced under one reading, resting on assumptions about the regions.** With the
encoding-model threshold (ii), the human-presence weight is positive and above the vehicle-presence
weight in FFA, OFA and EBA, and the reverse holds in RSC, PPA and OPA, in 4 of 5 subjects under
each of the three weight readings (B, B_L, Q_S); S2 fails in EBA. Without a threshold (i) the
pattern holds in 3 of 5 under each reading: EBA fails in S2 and S3 (B, B_L) or S1 and S2 (Q_S).
FFA, OFA, RSC, PPA and OPA hold in all five subjects under every reading; the outcome rests on EBA,
whose atlas definition (the lateral body areas of visfAtlas) is an assumption: LOS-bodies alone
holds in 5 of 5 under (ii). Of the other regions the claim names, MT+ (4 of 5) and LO (4 or 5)
follow the human-presence dimension and IPS (5 of 5) the vehicle-presence dimension; SEF, FEF, FO
and IFS are mixed (counts above). The regions are group-atlas areas, not the subjects' localizer
ROIs, and the WordNet model's ridge parameter was chosen per subject (1e3 or 1e4); 57 to 71% of
the region voxels pass its threshold.
=== cell 36 ===
## Video game task

States with no TRs are dropped (flash in S7; Supplementary Figure 4 shows no flash weights for
that subject), so S7's state space has 8 dimensions. Because the JSD is unchanged by affine maps,
the CSI does not depend on the order or signs of the dimensions; the dataset's column order is used.
=== cell 40 ===
[... 105 more lines not kept]
```

**Agent**

Now I'll write all text updates.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/edit_md.py <<'PYEOF'
import json
p='entries/zhang-2021/reproduce_zhang_2021.ipynb'
nb=json.load(open(p))
C=nb['cells']
def rep(i, pairs):
    s=''.join(C[i]['source'])
    for a,b in pairs:
        assert a in s, (i,a)
        s=s.replace(a,b)
    C[i]['source']=s.splitlines(keepends=True)
def put(i, s):
    assert C[i]['cell_type']=='markdown'
    C[i]['source']=s.strip('\n').splitlines(keepends=True)

rep(13,[("code's third axis is set by rounding too. The R3 values below therefore move slightly between\n  runs (S2 attend-humans 0.740 in the first run, 0.743 in this one).",
"code's third axis is set by rounding too. The R3 values below can therefore move slightly between\n  runs on different machines (S2 attend-humans 0.740 in the first run, 0.739 in this one); two\n  runs of this revision on the same machine gave identical values."),
("(S1 0.729 against\n  0.691 at lag 0; S7 0.569 against 0.547)","(S1 0.729 against\n  0.691 at lag 0; S7 0.566 against 0.550)"),
("The S7 data are float32 and not exactly\n  z-scored per voxel over the session; S1's are.",
"The S7 data are float32 and not z-scored\n  per voxel over the session (voxel SDs 0.094 to 1.009); S1's are. The paper says the responses\n  were normalized to zero mean and unit variance (Methods, Preprocessing and Visualization), so\n  both subjects' data are z-scored per voxel over the session here; S7 as stored is shown as a\n  variant after game-weights-two-groups."),
])

put(19,"""**Result: reproduced, resting on an assumption about the third axis.** With the paper's code (R3)
the S2 CSIs are 0.739 (attend-humans), 0.717 (attend-vehicles) and 0.676 (passive), all within
tolerance of 0.75, 0.69 and 0.67, and each exceeds every one of 1000 null values under both
permutation readings (null maxima 0.040 to 0.062 under (a), 0.322 to 0.352 under (b); p <= 0.001,
the bound 1000 permutations reach, not the paper's 1e-5). The median over random third axes (R2)
also matches (0.723, 0.718, 0.657). In the human-vehicle plane alone (R1) the attend-humans CSI is
0.664, outside tolerance. The third axis of the state space has no weight in these data, so the
values depend on it: over random third axes the attend-humans CSI ranges from 0.683 to 0.784 (5 to
95%), within tolerance throughout.""")

put(22,"""**Result: reproduced, resting on an assumption about the third axis.** Over the five released
subjects, R3 gives mean CSIs of 0.663 +/- 0.104 (attend-humans), 0.730 +/- 0.023 (attend-vehicles)
and 0.525 +/- 0.260 (passive), all within the paper's spreads of 0.66 +/- 0.09, 0.74 +/- 0.03 and
0.53 +/- 0.24; R2 gives 0.658, 0.728 and 0.523. Under group reading (b), each mean exceeds the
maximum of the mean null CSIs (at most 0.110). Under reading (a), every subject is significant in
the attentive conditions but not in passive, where S3's CSI (0.062) does not exceed its null. In
the plane alone (R1) the attend-vehicles mean, 0.675, is outside tolerance. The second reference,
the means of the paper's own per-subject values over these subjects (0.644, 0.728, 0.512), is also
close to the R3 means.""")

put(25,"""**Result: reproduced, resting on an assumption about the third axis.** With R3, 10 of the 12
per-subject CSIs are within 10% of the values in Supplementary Figures 1 and 2 (11 of 12 with R2,
10 of 12 with R1). The two outside are S3 passive (0.062 against 0.05, a tolerance of 0.005) and
S5 attend-humans (0.763 against 0.66, within tolerance under R2 at 0.694). Under permutation
reading (a) all 12 R3 CSIs are significant at p < 0.01: eleven exceed every null value
(p = 0.001) and S3 passive has p = 0.002. Under reading (b) S3 passive has p = 0.039, so 11 of 12
are significant. The R1 counts are printed above. S3's passive CSI is close to the floor of the
measure, as in the paper (0.05).""")

put(28,"""**Result: not reproduced.** At the threshold that 1000 permutations allow (the difference
exceeding every null value), the passive CSI is significantly lower than the attentive CSIs in 2
of the 5 subjects (S3 and S5) under every combination of reading and null run with the code's
positions (R3), and in 1 with the plane (R1), where the criterion needs 4 of 5. At p < 0.05 the
counts are at most 3 with R3 and at most 4 with R1 (reading b, matched permutation, refitted). S3
and S5 show the effect clearly (mean differences 0.665 and 0.134, above every null value). In S1
and S6 the attend-humans CSI is below the passive one (S1 0.512 against 0.621; S6 0.606 against
0.652), as in the paper's own figure values for these subjects, and the mean of the two attentive
CSIs is within 0.008 of passive (p 0.34 to 0.51). S2's mean difference, 0.0525, lies above the
null's 99th percentile under three of the four nulls (0.0416 to 0.0504) and below it under the
fourth (0.0562, global, null ii), and below the null's maximum under all four (0.0526 to 0.0840;
the closest, 0.0526, under matched permutation and null ii); p = 0.002 to 0.015. The counts are
the same under null (ii), which is computed as the observed values are.""")

put(31,"""**Result: reproduced.** The mean accuracy over the five subjects is 43.7% (contiguous folds,
Euclidean), 53.3% (contiguous, density), 46.6% (random, Euclidean) and 56.3% (random, density),
against 48.4 +/- 7.6%; three of the four readings are within tolerance, and all four exceed every
one of 1000 mean null accuracies (maxima 9.7 to 12.5%). Chance under this procedure, the mean of
the null, is 7.8 to 9.1%, close to the paper's 8.3%. Per subject the accuracy is 40.4 to 60.6%.
The first run gave 44.4% and 53.4% for the contiguous readings; the likeliest cause of the
difference is rounding in the third axis of each fold's state space, which carries little weight.""")

put(35,"""**Result: reproduced under one reading, resting on assumptions about the regions and on the
encoding-model threshold.** With the encoding-model threshold (ii), the human-presence weight is
positive and above the vehicle-presence weight in FFA, OFA and EBA, and the reverse holds in RSC,
PPA and OPA, in 4 of 5 subjects under each of the three weight readings (B, B_L, Q_S); S2 fails in
EBA (human minus vehicle weight -0.041 for B, -0.048 for B_L). Without a threshold (i) the pattern
holds in 3 of 5 under each reading: EBA fails in S2 and S3 (B, B_L) or S1 and S2 (Q_S); S3's
failure under B is a near tie (0.313 against 0.314). The outcome therefore hinges on the threshold.
Under (ii) the margins in EBA of the subjects that pass are small in S1 and S3 (B 0.079 and 0.044,
B_L 0.065 and 0.030) and large in S5 and S6 (0.24 to 0.40). The t test behind threshold (ii)
treats the 5400 TRs as independent, which they are not, so it passes many voxels (57 to 71% of the
region voxels). In a variant not in the claims file, a far stricter threshold, Bonferroni over each
subject's region voxels (1638 to 2724 voxels pass), the pattern holds in 5 of 5 subjects for B and
B_L and in 4 of 5 for Q_S (S6 fails in RSC), and EBA holds in all five under every reading; so the
outcome does not rest on the liberal test, but it does rest on thresholding the voxels by the
encoding model at all. FFA, OFA, PPA and OPA hold in all five subjects under every reading, and RSC
under every reading but one; EBA's atlas definition (the lateral body areas of visfAtlas) is an
assumption: LOS-bodies alone holds in 5 of 5 under (ii). Of the other regions the claim names, MT+
(4 of 5) and LO (4 or 5) follow the human-presence dimension and IPS (5 of 5) the vehicle-presence
dimension; SEF, FEF, FO and IFS are mixed (counts above). The regions are group-atlas areas, not
the subjects' localizer ROIs, and the WordNet model's ridge parameter was chosen per subject (1e3
or 1e4).""")

put(36,"""## Video game task

States with no TRs are dropped (flash in S7; Supplementary Figure 4 shows no flash weights for
that subject), so S7's state space has 8 dimensions. Because the JSD is unchanged by affine maps,
the CSI does not depend on the order or signs of the dimensions; the dataset's column order is used.
Both subjects' BOLD is z-scored per voxel over the session, as the paper's Methods say ("The
detrended voxel responses were normalized to zero mean and unit variance", Preprocessing and
Visualization); S1's data are already z-scored, S7's are not. S7 as stored, the analysis of the
earlier rounds, is shown as a variant after game-weights-two-groups.""")

put(40,"""**Result: reproduced under one reading of the clusters.** With one cluster per state from TRs
that have exactly one state (reading b), the CSI is 0.702 in S1 and 0.582 in S7, within tolerance
of 0.72 and 0.62, and both exceed every null value (null maxima 0.270 and 0.259). With every TR in
the cluster of each of its states (reading a), S1 is within (0.694) and S7 just outside (0.549,
tolerance down to 0.558). With the three groups of Figure 3A (reading c), both are lower (0.513 and
0.386). All six values exceed their nulls. With the labels moved one TR later, where the CSI
peaks, readings (a) and (b) are within tolerance in both subjects (S1 0.728 and 0.760, S7 0.564
and 0.584, each above all 200 null values) and reading (c) is not (0.593 and 0.416). With S7 as
stored, not z-scored, the S7 values are 0.549, 0.581 and 0.388 (variant below): the same
conclusions.""")

put(43,"""**Result: reproduced, resting on an assumption about the order of the variables.** With the
variables in the order of the data set's columns, engage-close TRs lie at -1.187 (S1) and -0.190
(S7) on the safe-explore dimension, and safe-explore TRs at -0.399 (S1) and -0.550 (S7) on the
engage-close dimension, all with p = 5e-5, the bound of 20,000 permutations, under both sign
readings. With the order of Table 1, S1 holds (-0.697 and -0.068, p = 5e-5) but in S7 safe explore
lies at -0.016 on the engage-close dimension (p = 0.952), so the claim would hold in one subject
only. The sign readings give the same values. With S7 as stored the values are -0.191 and -0.548
(data set order, p = 5e-5) and -0.018 (Table 1 order, p = 0.936): the same conclusions.""")

put(46,"""**Result: reproduced.** Under every sign, order, Bonferroni and null-centre reading, both
subjects have significant off-diagonal projections (S1 44 to 48 pairs, S7 21 to 26), some pairs are
significant in one direction only (9 to 20), and the two subjects' sets of significant pairs
differ (12 to 20 shared). Centring the two-sided test on the null's mean in place of zero changes
the counts by at most one pair. With S7 as stored (own sign, zero centre, Bonferroni a, a separate
set of 20,000 permutations) S7 has 26 (Table 1 order) and 23 (data set order) significant pairs, 10
and 13 of them in one direction only. The figure's own matrix was not available to compare pair by
pair.""")

put(50,"""**Result: partially reproduced.** Every reading is far above its null (p = 0.001; chance under
this procedure 10.8 to 16.4%, against the paper's 11%). S7's balanced accuracy is within the
paper's 30.4 +/- 4.2% with contiguous folds (26.9 to 34.1%) and above it with random folds (36.9 to
46.5%). S1's is above the paper's 32.8 +/- 3.8% under every reading (42.8 to 54.6%), so no reading
puts both subjects within tolerance. With the labels one TR later the accuracies rise (S1 45.7 to
60.5%, S7 28.4 to 52.2%) and the same holds. With S7 as stored, S7 gives 26.4 to 33.8% (contiguous)
and 36.4 to 47.1% (random), so the outcome is the same. Random folds put neighbouring,
autocorrelated TRs in training and test sets and give higher values than contiguous folds; the
outcome does not depend on this, since S1 is above tolerance under both. S1's data are six whole
runs of 325 TRs (65 min, data check), where the paper reports 90 min, so the S1 data may differ
from those the paper analysed, which could account for S1 being above the paper's value.""")

rep(51,[("fail. A stricter variant asks every own region to be above every other region.",
"fail. A stricter variant asks every own region to be above every other region. The prefrontal\nregion is large (most of the frontal lobe outside motor and premotor cortex); as a variant, the\nmedial prefrontal areas alone (the default-mode part) replace it.")])

put(55,"""**Result: not reproduced in S7, resting on assumptions about the regions; S1 cannot be placed on
the cortex.** In S7 three to five of the eight dimensions fail the grouping under every reading,
where one may fail: dead, safe explore and unsafe explore under every reading, and engage far,
run away, round start or engage close under some. Safe explore has negative OLS weights in all
nine regions (-0.008 to -0.241, threshold i). With the denoised weights, and with the Bonferroni
threshold (ii) and the OLS weights, three fail. With the medial prefrontal areas in place of the
whole prefrontal region the same dimensions fail under every reading, so the result does not rest
on how coarsely the prefrontal region is drawn, within these two choices. With S7 as stored, not
z-scored, three to five fail as well (four with the denoised weights at threshold i), so the
outcome does not rest on the normalization either. S1's game data match no mapper, so S1 and the
consistency between the two subjects could not be tested, and the outcome rests on S7 alone. In
the variant not taken from the paper, the correlation of S1's denoised weight maps across voxels
splits the nine dimensions into exactly the paper's two groups (flash, safe explore, unsafe
explore, dead, round start; engage close, engage far, run away, kill), while S7's maps split into
safe and unsafe explore against the rest. The regions are HCP-MMP1.0 areas chosen to match the
names in the paper, not the paper's ROIs.""")

rep(56,[("| att-passive-lower | not reproduced (2 or 3 of 5 subjects at the bound reached) |","| att-passive-lower | not reproduced (2 of 5 subjects at the bound reached) |"),
("| att-weights-cortex | reproduced under the encoding-model threshold (4 of 5 subjects), 3 of 5 without it; atlas regions in place of the paper's ROIs |",
 "| att-weights-cortex | reproduced under the encoding-model threshold (4 of 5 subjects; 5 of 5 under a stricter Bonferroni variant), 3 of 5 without it; atlas regions in place of the paper's ROIs |"),
("| game-weights-two-groups | not reproduced: fails in S7 under every reading (atlas regions); S1 cannot be mapped |",
 "| game-weights-two-groups | not reproduced: fails in S7 under every reading (atlas regions), with S7 z-scored or as stored; S1 cannot be mapped |"),
("- The game labels are used at lag 0; the CSI peaks at lag +1, shown as a variant.",
 "- The game labels are used at lag 0; the CSI peaks at lag +1, shown as a variant.\n- The video game BOLD is z-scored per voxel over the session, as the paper's Methods say; S7's\n  deposited data are not, and S7 as stored is shown as a variant."),
("so the R3 CSIs\n  move slightly from run to run.","so the R3 CSIs\n  can move slightly between runs on different machines."),
])
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
print("ok")
PYEOF
python $TMPDIR/edit_md.py
```

```
ok
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
J=lambda c: ''.join(''.join(o.get('text','')) for o in c['outputs'])
t=J(nb['cells'][53]); i=t.find('medial prefrontal in place'); print(t[i:i+1200])
EOF
```

```
medial prefrontal in place of prefrontal: dimensions failing (one may fail)
  threshold i   B              4 failing: ['dead', 'engage far', 'safe explore', 'unsafe explore']
  threshold i   B_L            3 failing: ['dead', 'safe explore', 'unsafe explore']
  threshold i   Q_S (dataset)  5 failing: ['dead', 'engage far', 'run away', 'safe explore', 'unsafe explore']
  threshold i   Q_S (table1)   5 failing: ['dead', 'engage close', 'run away', 'safe explore', 'unsafe explore']
  threshold ii  B              3 failing: ['dead', 'safe explore', 'unsafe explore']
  threshold ii  B_L            3 failing: ['dead', 'safe explore', 'unsafe explore']
  threshold ii  Q_S (dataset)  5 failing: ['dead', 'round start', 'run away', 'safe explore', 'unsafe explore']
  threshold ii  Q_S (table1)   5 failing: ['dead', 'engage close', 'run away', 'safe explore', 'unsafe explore']

S1 B maps: clusters {1: ['flash', 'engage close', 'engage far', 'safe explore', 'unsafe explore', 'run away', 'dead', 'round start'], 2: ['kill']}
                flash  engage close  engage far  safe explore  unsafe explore  run away  dead  round start  kill
flash            1.00          0.03       -0.00          0.2
```

**Agent calls Bash**

```bash
cd  sed -i 's/runs in about 55 minutes with 6 GB of memory/runs in about 25 minutes with 6 GB of memory/' entries/zhang-2021/README.md; sed -i 's/  runtime_minutes: 55/  runtime_minutes: 25/' entries/zhang-2021/entry.yaml; grep -n "minutes" entries/zhang-2021/README.md entries/zhang-2021/entry.yaml; cat attempts/zhang-2021-01.yaml
```

```
<persisted-output>
Output too large (29.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d2a546e8-415d-49ec-b285-a9d65d8ab689/tool-results/b6dk81hxs.txt

Preview (first 2KB):
entries/zhang-2021/README.md:20:The notebook streams about 16 GB and runs in about 25 minutes with 6 GB of memory.
entries/zhang-2021/entry.yaml:16:  runtime_minutes: 25
schema_version: 3
id: zhang-2021-01
datasets:
- archive: crcns
  id: vim-4
  version: unversioned
  doi: 10.6080/K0668BDF
  relation: primary
paper: doi:10.3389/fnins.2020.565976
date: 2026-11-14
entry: zhang-2021
provenance:
  kind: agent
  accountable:
[... 31 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/zhang-2021-01.yaml"
}
```

```
1	schema_version: 3
2	id: zhang-2021-01
3	datasets:
4	- archive: crcns
5	  id: vim-4
6	  version: unversioned
7	  doi: 10.6080/K0668BDF
8	  relation: primary
9	paper: doi:10.3389/fnins.2020.565976
10	date: 2026-11-14
11	entry: zhang-2021
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-15
20	  runner:
[... 412 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 145,200p claims/zhang-2021.yaml | grep -n -A20 "expected" | head -40
```

```
14:  expected:
15-  - quantity: CSI, S1, attend-humans
16-    value: 0.51
17-    tolerance: 0.051
18-  - quantity: CSI, S1, attend-vehicles
19-    value: 0.79
20-    tolerance: 0.079
21-  - quantity: CSI, S1, passive
22-    value: 0.64
23-    tolerance: 0.064
24-  - quantity: CSI, S3, attend-humans
25-    value: 0.70
26-    tolerance: 0.07
27-  - quantity: CSI, S3, attend-vehicles
28-    value: 0.71
29-    tolerance: 0.071
30-  - quantity: CSI, S3, passive
31-    value: 0.05
32-    tolerance: 0.005
33-  - quantity: CSI, S5, attend-humans
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/edit_rec.py <<'PYEOF'
p='attempts/zhang-2021-01.yaml'
s=open(p).read()
def R(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:80])
    s=s.replace(a,b)
# fig1
R("""  - 0.743
  - 0.721
  - 0.675
  notes: With the paper's code run on the full voxel data (R3), S2's CSIs are 0.743 (attend-humans), 0.721 (attend-vehicles)
    and 0.675 (passive),""","""  - 0.739
  - 0.717
  - 0.676
  notes: With the paper's code run on the full voxel data (R3), S2's CSIs are 0.739 (attend-humans), 0.717 (attend-vehicles)
    and 0.676 (passive),""")
R("""so its third axis is set by rounding and the R3 values move slightly between runs (0.740, 0.718, 0.676 in the
    first run).""","""so its third axis is set by rounding and the R3 values can move slightly between runs on different machines (0.740,
    0.718, 0.676 in the first run); two runs of the final revision on the same machine gave identical values.""")
# group
R("""  - 0.665
  - 0.731
  - 0.524
  notes: Over the five released subjects (R3) the mean CSIs are 0.665 +/- 0.104, 0.731 +/- 0.023 and 0.524 +/- 0.260""",
"""  - 0.663
  - 0.73
  - 0.525
  notes: Over the five released subjects (R3) the mean CSIs are 0.663 +/- 0.104, 0.730 +/- 0.023 and 0.525 +/- 0.260""")
R("but S3's passive CSI (0.061) does not exceed every null value.","but S3's passive CSI (0.062) does not exceed every null value.")
# supp
R("""  - 0.515
  - 0.744
  - 0.62
  - 0.696
  - 0.761
  - 0.061
  - 0.767
  - 0.73
  - 0.614
  - 0.605
  - 0.699
  - 0.651
  notes: With R3, 10 of 12 values are within 10% of the supplement's; outside are S3 passive (0.061 against 0.05,
    tolerance 0.005) and S5 attend-humans (0.767 against 0.66). Under permutation reading (a) all 12 are significant
    at p < 0.01 (S3 passive p = 0.002, the others 0.001); under reading (b) S3 passive has p = 0.045.""",
"""  - 0.512
  - 0.745
  - 0.621
  - 0.695
  - 0.758
  - 0.062
  - 0.763
  - 0.731
  - 0.613
  - 0.606
  - 0.7
  - 0.652
  notes: With R3, 10 of 12 values are within 10% of the supplement's; outside are S3 passive (0.062 against 0.05,
    tolerance 0.005) and S5 attend-humans (0.763 against 0.66). Under permutation reading (a) all 12 are significant
    at p < 0.01 (S3 passive p = 0.002, the others 0.001); under reading (b) S3 passive has p = 0.039.""")
# passive lower
R("""    CSI is significantly lower in 2 of 5 subjects under reading (a) with the code's positions (S3, S5), and 2 or
    3 under reading (b), for every null (refitted or not) and both permutation schemes; the criterion needs 4 of
    5. At p < 0.05 the counts are at most 3 (R3) and at most 4 (R1, reading b, matched, refitted). In S1 and S6
    attend-humans is below passive (0.515 against 0.620; 0.605 against 0.651), as in the paper's own figure values
    for these subjects, and the mean attentive CSI is within 0.010 of passive (p 0.30 to 0.51). S2's mean difference,
    0.057, lies above its null's 99th percentile (0.042 to 0.055) and below or near its maximum (0.052 to 0.084),
    p 0.001 to 0.010. Null (ii)""","""    CSI is significantly lower in 2 of 5 subjects (S3, S5) with the code's positions under both readings, every
    null (refitted or not) and both permutation schemes; the criterion needs 4 of 5. At p < 0.05 the counts are
    at most 3 (R3) and at most 4 (R1, reading b, matched, refitted). S3 and S5 have mean differences of 0.665 and
    0.134. In S1 and S6 attend-humans is below passive (0.512 against 0.621; 0.606 against 0.652), as in the paper's
    own figure values for these subjects, and the mean attentive CSI is within 0.008 of passive (p 0.34 to 0.51).
    S2's mean difference, 0.0525, lies above its null's 99th percentile under three of the four nulls (0.0416 to
    0.0504) and below it under the fourth (0.0562), and below the null maximum under all four (0.0526 to 0.0840),
    p 0.002 to 0.015. Null (ii)""")
# classification
R("""  notes: Mean accuracy over the five subjects is 43.7% (contiguous folds, Euclidean), 53.8% (contiguous, density),""",
"""  notes: Mean accuracy over the five subjects is 43.7% (contiguous folds, Euclidean), 53.3% (contiguous, density),""")
R("""mean) is 7.8 to 9.1%, close to the paper's 8.3%. Per subject 39.9 to 60.6%. The first run gave 44.4% and 53.4%
    for the contiguous readings with the same code and seeds; the cause was not traced, the likeliest being rounding
    in the third axis of each fold's state space.""","""mean) is 7.8 to 9.1%, close to the paper's 8.3%. Per subject 40.4 to 60.6%. The first run gave 44.4% and 53.4%
    for the contiguous readings; the likeliest cause of the difference is rounding in the third axis of each fold's
    state space.""")
# weights cortex
R("""reading (OLS B, denoised B_L, Q_S); S2 fails in EBA (human 0.335, vehicle 0.416 with B, no threshold). Without
    a threshold (i) the pattern holds in 3 of 5 under each reading, EBA failing in S2 and S3 (B, B_L) or S1 and
    S2 (Q_S). FFA, OFA, RSC, PPA and OPA hold in all five subjects under every reading, so the outcome rests on
    EBA and on the threshold; LOS-bodies alone holds in 5 of 5 under (ii).""","""reading (OLS B, denoised B_L, Q_S); S2 fails in EBA (human minus vehicle -0.041 with B under threshold ii).
    Without a threshold (i) the pattern holds in 3 of 5 under each reading, EBA failing in S2 and S3 (B, B_L) or
    S1 and S2 (Q_S); S3's failure under B is a near tie (0.313 against 0.314). The outcome therefore hinges on the
    threshold. Under (ii) the EBA margins of the passing subjects are small in S1 and S3 (B 0.079 and 0.044) and
    0.24 to 0.40 in S5 and S6. The t test of threshold (ii) treats the 5400 TRs as independent and passes 57 to 71%
    of the region voxels; in a variant not in the claims file, Bonferroni over each subject's region voxels (1638
    to 2724 voxels pass), the pattern holds in 5 of 5 subjects with B and B_L and 4 of 5 with Q_S (S6 fails in
    RSC), with EBA holding in all five. So the outcome does not rest on the liberal test, but it does rest on thresholding
    by the encoding model. FFA, OFA, RSC, PPA and OPA hold in all five subjects under every reading of the claims
    file; LOS-bodies alone holds in 5 of 5 under (ii).""")
# game csi
R("""  - 0.702
  - 0.581
  notes: With one cluster per state from TRs with exactly one state (reading b), the CSI is 0.702 (S1) and 0.581
    (S7), within tolerance of 0.72 and 0.62 and above every one of 1000 null values (maxima 0.270 and 0.258). With
    multi-membership clusters (reading a) S1 is 0.694 and S7 0.549, just below tolerance (0.558); with the three
    groups of Figure 3A (reading c) 0.513 and 0.388.""","""  - 0.702
  - 0.582
  notes: With one cluster per state from TRs with exactly one state (reading b), the CSI is 0.702 (S1) and 0.582
    (S7), within tolerance of 0.72 and 0.62 and above every one of 1000 null values (maxima 0.270 and 0.259). With
    multi-membership clusters (reading a) S1 is 0.694 and S7 0.549, just below tolerance (0.558); with the three
    groups of Figure 3A (reading c) 0.513 and 0.386.""")
R("""where the CSI peaks in both subjects, readings (a) and (b) are within tolerance in both subjects (S1 0.728 and
    0.760, S7 0.566 and 0.583) and reading (c) is not; the paper does not say whether the game labels were shifted.
  deviations:
  - S7 has no flash TRs, so its state space has 8 dimensions.""","""where the CSI peaks in both subjects, readings (a) and (b) are within tolerance in both subjects (S1 0.728 and
    0.760, S7 0.564 and 0.584) and reading (c) is not; the paper does not say whether the game labels were shifted.
    With S7's BOLD as stored, not z-scored, S7 gives 0.549, 0.581 and 0.388 under readings (a) to (c), the same
    conclusions.
  deviations:
  - S7 has no flash TRs, so its state space has 8 dimensions.
  - Each voxel of the video game BOLD is z-scored over the session, as the paper's Methods say ("The detrended voxel
    responses were normalized to zero mean and unit variance", Preprocessing and Visualization); S1's deposited data
    are already z-scored, S7's are not. Rounds 1 and 2 used S7 as stored; that analysis is shown as a variant.""")
# mutual
R("""  notes: With the variables in the data set's column order, engage-close TRs lie at -1.187 (S1) and -0.191 (S7)
    on the safe-explore dimension and safe-explore TRs at -0.399 and -0.548 on the engage-close dimension, each
    p = 5e-5 (the bound of 20,000 permutations), under both sign readings. With Table 1's order S1 holds (-0.697,
    -0.068, p = 5e-5) but S7's safe-explore TRs lie at -0.018 on the engage-close dimension (p = 0.937), which would
    make the claim hold in one subject only.""","""  notes: With the variables in the data set's column order, engage-close TRs lie at -1.187 (S1) and -0.190 (S7)
    on the safe-explore dimension and safe-explore TRs at -0.399 and -0.550 on the engage-close dimension, each
    p = 5e-5 (the bound of 20,000 permutations), under both sign readings. With Table 1's order S1 holds (-0.697,
    -0.068, p = 5e-5) but S7's safe-explore TRs lie at -0.016 on the engage-close dimension (p = 0.952), which would
    make the claim hold in one subject only. With S7 as stored, not z-scored, the S7 values are -0.191 and -0.548
    (p = 5e-5) and -0.018 under Table 1's order (p = 0.936).""")
R("""    would be partially reproduced.
- claim: fig3b-state-relations""","""    would be partially reproduced.
  - S7's BOLD z-scored per voxel over the session, as for game-csi.
- claim: fig3b-state-relations""")
# fig3b
R("""  notes: Under every sign, order, Bonferroni and null-centre reading, S1 has 44 to 48 and S7 20 to 33 significant
    off-diagonal projections (p < 0.01 corrected, 20,000 permutations, smallest p 5e-5), 10 to 20 pairs are significant
    in one direction only, and the subjects share 12 to 27 of their significant pairs. Centring the two-sided test
    on the null's mean in place of zero changes the counts by at most one pair. The paper's matrix could not be
    compared pair by pair.""","""  notes: Under every sign, order, Bonferroni and null-centre reading, S1 has 44 to 48 and S7 21 to 26 significant
    off-diagonal projections (p < 0.01 corrected, 20,000 permutations, smallest p 5e-5), 9 to 20 pairs are significant
    in one direction only, and the subjects share 12 to 20 of their significant pairs. Centring the two-sided test
    on the null's mean in place of zero changes the counts by at most one pair. With S7 as stored (own sign, zero
    centre, Bonferroni a) S7 has 26 and 23 significant pairs (Table 1 and data set order). The paper's matrix could
    not be compared pair by pair.
  deviations:
  - S7's BOLD z-scored per voxel over the session, as for game-csi.""")
# game classification
R("""  - 46.5
  - 33.8
  notes: Every reading is above its null (p = 0.001; chance under this procedure 10.8 to 16.4%, against the paper's
    11%). S7 is within 30.4 +/- 4.2% with contiguous folds (26.4 to 33.8%) and above it with random folds (36.8
    to 46.5%). S1 is above 32.8 +/- 3.8% under every reading (42.8 to 54.6%), so no reading puts both within tolerance;
    with the labels one TR later the same holds (S1 45.7 to 60.5%, S7 28.4 to 50.9%).""","""  - 46.5
  - 33.7
  notes: Every reading is above its null (p = 0.001; chance under this procedure 10.8 to 16.4%, against the paper's
    11%). S7 is within 30.4 +/- 4.2% with contiguous folds (26.9 to 34.1%) and above it with random folds (36.9
    to 46.5%). S1 is above 32.8 +/- 3.8% under every reading (42.8 to 54.6%), so no reading puts both within tolerance;
    with the labels one TR later the same holds (S1 45.7 to 60.5%, S7 28.4 to 52.2%). With S7 as stored, not z-scored,
    S7 gives 26.4 to 33.8% (contiguous) and 36.4 to 47.1% (random).""")
R("""    a recall of 0.
- claim: game-weights-two-groups""","""    a recall of 0.
  - S7's BOLD z-scored per voxel over the session, as for game-csi.
- claim: game-weights-two-groups""")
# game weights
R("""    explore under every reading, and engage far, run away, round start or engage close under some (4 fail with OLS
    or denoised weights and no threshold, 3 with the Bonferroni threshold, 5 with Q_S under either order). Safe
    explore has negative OLS weights in all nine regions (-0.008 to -0.240). Since the criterion asks for the pattern
    in both subjects, failing in S7 decides the outcome.""","""    explore under every reading, and engage far, run away, round start or engage close under some (4 fail with OLS
    weights and no threshold, 3 with denoised weights or with the Bonferroni threshold, 5 with Q_S under either order).
    Safe explore has negative OLS weights in all nine regions (-0.008 to -0.241). Since the criterion asks for the
    pattern in both subjects, failing in S7 decides the outcome, which rests on S7 alone. With the medial prefrontal
    areas in place of the whole prefrontal region (57,895 vertices) the same dimensions fail under every reading.
    With S7 as stored, not z-scored, three to five fail as well (4 with denoised weights and no threshold).""")
R("""  - S1 could not be placed on the cortex; S7 has no flash dimension.""","""  - S1 could not be placed on the cortex; S7 has no flash dimension.
  - S7's BOLD z-scored per voxel over the session, as for game-csi; the weights are those of the z-scored responses.""")
open(p,'w').write(s)
print('ok')
PYEOF
python $TMPDIR/edit_rec.py
```

```
ok
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
J=lambda c: ''.join(''.join(o.get('text','')) for o in c['outputs'])
t=J(nb['cells'][6]); i=t.find("'TPJ'"); print(t[i:i+400]); i=t.find("S7, video"); print(t[i:i+400])
EOF
date -u
```

```
'TPJ': 11146, 'precuneus': 7604, 'prefrontal': 57895, 'motor': 7870, 'premotor': 10840, 'SMA': 5071, 'medial prefrontal': 12185}
vertices per region that each subject's mapper reaches (attention regions):
     FFA  OFA   EBA  MT+   PPA   OPA   RSC    LO    FO   IFS    IPS   FEF   SEF  LOS-bodies  ITG-bodies  MTG-bodies  OTS-bodies  FFC (HCP)  PHA1-3 (HCP)  POS1 (HCP)
S1  1975  703  4745  899  3016
S7, video game regions: {'TPJ': 11146, 'precuneus': 7604, 'prefrontal': 57676, 'motor': 7870, 'premotor': 10840, 'SMA': 5071, 'IPS': 14832, 'FEF': 1682, 'SEF': 2004, 'medial prefrontal': 12113}
voxels the regions reach: {'S1': 5965, 'S2': 5908, 'S3': 5982, 'S5': 5945, 'S6': 6065} | S7 video game: 16509

Sat Nov 14 16:27:23 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/zhang-2021-01.yaml'
s=open(p).read()
a="With the medial prefrontal\n    areas in place of the whole prefrontal region (57,895 vertices)"
assert a in s
s=s.replace(a,"With the medial prefrontal\n    areas (12,185 vertices) in place of the whole prefrontal region (57,895 vertices)")
open(p,'w').write(s)
import json
p='entries/zhang-2021/reproduce_zhang_2021.ipynb'
nb=json.load(open(p)); c=nb['cells'][55]; t=''.join(c['source'])
a="With the medial prefrontal areas in place of the\nwhole prefrontal region"
if a not in t:
    a="With the medial prefrontal areas in place of the whole prefrontal region"
print(a in t, repr(t[t.find('With the medial'):t.find('With the medial')+120]))
EOF
```

```
True 'With the medial prefrontal areas in place of the\nwhole prefrontal region the same dimensions fail under every reading, s'
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
p='entries/zhang-2021/reproduce_zhang_2021.ipynb'
nb=json.load(open(p)); c=nb['cells'][55]; t=''.join(c['source'])
t=t.replace("With the medial prefrontal areas in place of the\nwhole prefrontal region the same","With the medial prefrontal areas (12,185 fsaverage vertices) in place\nof the whole prefrontal region (57,895) the same",1)
c['source']=t.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat
```

```
attempts/zhang-2021-01.yaml                   | 146 ++++++++------
 entries/zhang-2021/README.md                  |   2 +-
 entries/zhang-2021/entry.yaml                 |   2 +-
 entries/zhang-2021/reproduce_zhang_2021.ipynb | 272 +++++++++++++++++++-------
 entries/zhang-2021/statespace.py              |  13 +-
 tools/agent_run.py                            |  15 +-
 tools/runner/chain.sh                         |  97 +++++----
 7 files changed, 365 insertions(+), 182 deletions(-)
```

**Agent calls Bash**

```bash
cd  cat >> attempts/zhang-2021-01.yaml <<'EOF'
- date: '2026-11-14'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: The full executed notebook of the round-1 revision (commit bea4220), with its conclusions and summary,
    the helper module, the claims file, the attempt record and the paper's full text. The verifier did not re-run
    the notebook.
  results:
  - claim: fig1-csi-s2
    agrees: true
    outcome: reproduced
    reason: 'Cell 17 prints R3 0.739, 0.717 and 0.676, all within tolerance and above every null value under both
      readings. R2 also passes. The assumption is stated and reasonable, and does not decide the outcome, since R2
      passes too. The text and the record give 0.743, 0.721 and 0.675, stale values from an earlier execution.'
    response: 'Re-ran the entry twice on the same machine, which gave identical values (0.739, 0.717, 0.676); the
      notebook, the measured values and the notes now give them, and the data check says the R3 values can move between
      machines. Outcome unchanged.'
  - claim: att-csi-group
    agrees: true
    outcome: reproduced
    reason: 'Cell 21 prints R3 means of 0.663, 0.730 and 0.525, and group reading (b) passes. The assumption is stated
      and reasonable. Cell 22 and the record give 0.665, 0.731 and 0.524 and S3''s CSI as 0.061, where cells 21 and
      15 print 0.663, 0.730, 0.525 and 0.062.'
    response: Updated the text, measured values and notes to 0.663, 0.730, 0.525 and S3 passive 0.062. Outcome unchanged.
  - claim: supp-csi-per-subject
    agrees: true
    outcome: reproduced
    reason: 'Cell 24: 10 of 12 values within tolerance, and 12 of 12 have p < 0.01 under null (a). The assumption
      is stated and reasonable. Cell 25 gives S3 passive 0.061, S5 attend-humans 0.767 and p = 0.045 under reading
      (b), where cell 24 prints 0.062, 0.763 and 0.039; eleven of the twelve measured values in the record differ
      from cell 24''s R3 column.'
    response: Replaced the twelve measured values with cell 24's R3 column and corrected the text (0.062, 0.763, p
      = 0.039). Outcome unchanged.
  - claim: att-passive-lower
    agrees: true
    outcome: not_reproduced
    reason: 'Cell 27 counts 2 of 5 at the bound under every R3 combination, and at most 3 at p < 0.05. "2 or 3" in
      cell 28, the Summary and the record has no support, and several values are stale (S1 0.512 and 0.621, S6 0.606
      and 0.652, mean differences 0.665 and 0.134, S2 0.0525, 99th percentile 0.0416 to 0.0562, maximum 0.0526 to
      0.0840, p_mean 0.002 to 0.015, R3 p 0.34 to 0.51). S2''s 0.0525 now sits just below the 0.0526 maximum (matched,
      null ii).'
    response: 'Changed "2 or 3" to 2 (S3 and S5) in the conclusion, the Summary and the record, and updated every
      value to cell 27. S2''s mean difference is now described as above the 99th percentile under three of the four
      nulls and below it under the fourth, and below the maximum under all four, the closest 0.0526. Outcome unchanged.'
  - claim: att-classification
    agrees: true
    outcome: reproduced
    reason: 'Cell 30: 43.7, 53.3 and 46.6% are within tolerance, and all four readings are above every null mean.
      Cell 31 and the record say 53.8% and a per-subject range of 39.9 to 60.6%, where cell 30 prints 53.3 and 40.4
      to 60.6. The statement that the first run gave 53.4% "with the same code and seeds" now differs from this run
      by only 0.1.'
    response: Corrected to 53.3% and 40.4 to 60.6%, and shortened the note on the first run to its values and the
      likeliest cause. Outcome unchanged.
  - claim: att-weights-cortex
    agrees: true
    outcome: reproduced
    reason: 'Agrees under the criterion: cell 34 gives 4 of 5 subjects under threshold (ii) for B, B_L and Q_S, and
      3 of 5 under (i). The margin is thin. The atlas assumption is stated and reasonable as a stand-in. The t test
      treats 5400 autocorrelated TRs as independent, which is liberal: 57 to 71% of region voxels pass. Under (i),
      B and B_L fail in S3 by a near tie in EBA (human 0.313, vehicle 0.314). The values under (ii) are not printed,
      so the margin there cannot be judged. The conclusion should say the outcome hinges on this.'
    response: 'Printed the mean weights under threshold (ii) and the human minus vehicle EBA weight per subject under
      every threshold and reading: under (ii) S2 fails by -0.041 (B) and S1 and S3 pass by 0.079 and 0.044 (B). Added
      a stricter threshold as a variant, Bonferroni over each subject''s region voxels (1638 to 2724 voxels pass):
      the pattern holds in 5 of 5 subjects for B and B_L and 4 of 5 for Q_S, with EBA holding in all five. The conclusion
      and notes now say the outcome hinges on thresholding by the encoding model (3 of 5 without), and that it does
      not rest on the liberal test. Outcome unchanged.'
  - claim: game-csi
    agrees: true
    outcome: reproduced
    reason: 'Under reading (b), cell 38 gives 0.702 and 0.581; lag +1 also passes (cell 39). The S7 game data are
      not normalized: the paper says responses were "normalized to zero mean and unit variance", and load_game uses
      S7''s BOLD as stored (voxel SDs 0.094 to 1.009), with no z-scoring before the PCA, the OLS or the region means.
      This also affects the S7 values in game-csi.'
    response: 'Adopted the paper''s normalization: each voxel of the video game BOLD is now z-scored over the session
      (Methods, Preprocessing and Visualization), stated as a deviation, and S7 as stored is kept as a variant. Reading
      (b) gives 0.702 and 0.582 (as stored 0.581); every reading keeps its result. Outcome unchanged.'
  - claim: game-mutual-negative-projection
    agrees: true
    outcome: reproduced
    reason: 'Agrees under the dataset column order (cell 42). The assumption is stated and the reasoning is sound;
      the Table 1 order would give partially_reproduced, and the record says so. The S7 values are affected by the
      unnormalized S7 data.'
    response: With S7 z-scored the data set order gives -0.190 and -0.550 in S7 (p = 5e-5), and the Table 1 order
      -0.016 (p = 0.952); as stored, -0.191, -0.548 and -0.018. Outcome unchanged.
  - claim: fig3b-state-relations
    agrees: true
    outcome: reproduced
    reason: Agrees (cell 45). The S7 values are affected by the unnormalized S7 data.
    response: With S7 z-scored, S7 has 21 to 26 significant pairs under the readings (as stored, in a separate set
      of 20,000 permutations, 23 and 26); updated the counts in the text and record. Outcome unchanged.
  - claim: game-classification
    agrees: true
    outcome: partially_reproduced
    reason: 'Cell 48: S1 is above tolerance under every reading, and every reading is significant. The S7 values
      are affected by the unnormalized S7 data.'
    response: With S7 z-scored, S7 gives 26.9 to 34.1% with contiguous folds and 36.9 to 46.5% with random folds (as
      stored 26.4 to 33.8% and 36.4 to 47.1%); S1 is unchanged. Outcome unchanged.
  - claim: game-weights-two-groups
    agrees: true
    outcome: not_reproduced
    reason: 'Agrees only conditionally: the outcome rests on S7 alone (cell 53). The atlas assumption is stated. One
      assumption that bears on the outcome is not stated: S7''s BOLD goes into the analysis without z-scoring. Also
      (minor), the "prefrontal" region covers 57,895 vertices, most of the frontal lobe, so the S7 failure also depends
      on how coarsely the regions are drawn.'
    response: 'S7 is now z-scored as the paper says, stated as a deviation; three to five of the eight dimensions
      still fail under every reading, and with S7 as stored (variant) three to five fail as well. Added a variant
      with the medial prefrontal areas (12,185 vertices) in place of the whole prefrontal region: the same dimensions
      fail under every reading. The notes say the outcome rests on S7 alone. Outcome unchanged.'
EOF
date -u
```

```
Sat Nov 14 16:28:06 UTC 2026
```

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('attempts/zhang-2021-01.yaml'));print(len(d['verifications']), [o['measured'] if 'measured' in o else None for o in d['outcomes']])"; python tools/entry.py check entries/zhang-2021 2>&1 | tail -15
```

```
2 [[0.739, 0.717, 0.676], [0.663, 0.73, 0.525], [0.512, 0.745, 0.621, 0.695, 0.758, 0.062, 0.763, 0.731, 0.613, 0.606, 0.7, 0.652], 2, 43.7, 4, [0.702, 0.582], None, None, [46.5, 33.7], None]
0 error(s)
```

**Agent calls Bash**

```bash
cd  ls tools; python tools/entry.py --help 2>&1 | head -20
```

```
__pycache__
agent_run.py
archive_transcripts.sh
archives
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_reuse_targets.py
build_site.py
build_targets.py
changed_entries.py
claims_check.py
colab.py
contributors.py
conversion_issue.py
datasets.py
entry.py
[... 38 more lines not kept]
```

**Agent**

Check passes. Now the final run with the text in place.

**Agent calls Bash**

```bash
cd  date -u; timeout 7000 python tools/entry.py all entries/zhang-2021 2>&1 | tail -4; date -u
```

```
Sat Nov 14 16:28:22 UTC 2026
Installed kernelspec registry-zhang-2021 in executed/zhang-2021/.venv/share/jupyter/kernels/registry-zhang-2021
0 error(s)
pass  reproduce_zhang_2021.ipynb  (1401 s)
Sat Nov 14 16:51:51 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
J=lambda c: ''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
allt=''.join(J(c) for c in nb['cells'])
keys=["CSI 0.739","CSI 0.717","CSI 0.676","mean 0.663 +/- 0.104","mean 0.730 +/- 0.023","mean 0.525 +/- 0.260",
"0.763    False","0.039","S2 matched null ii: observed 0.0525; null median 0.0009, 95% 0.0287, 99% 0.0416, max 0.0526",
"53.3 +/- 4.7","40.41","Bonferroni variant: 1638 voxels","Bonferroni variant: 2724 voxels","ii-bonf    B          5",
"S7 reading b: 6 clusters","CSI 0.582","-0.18978","-0.55017","0.95195","S7 order table1  sign own  centre zero      Bonferroni a (56 tests, threshold 1.79e-04): 25",
"33.7230","34.0622","26.8852","36.8980","46.4929","lag +1 reading a: CSI 0.564","S7 lag +1 reading b: CSI 0.584",
"engage close on safe explore -0.191 (p 0.00005)","safe explore on engage close -0.018 (p 0.93575)","(Bonferroni a, own sign, zero centre) 23, one direction only 13",
"(Bonferroni a, own sign, zero centre) 26, one direction only 10","36.385","47.061","threshold i   B_L            4 failing","52.1730","0.566  0.550"]
for k in keys: print(k in allt, k)
print([l for l in allt.splitlines() if 'elapsed' in l][-1])
EOF
```

```
True CSI 0.739
True CSI 0.717
True CSI 0.676
True mean 0.663 +/- 0.104
True mean 0.730 +/- 0.023
True mean 0.525 +/- 0.260
False 0.763    False
True 0.039
True S2 matched null ii: observed 0.0525; null median 0.0009, 95% 0.0287, 99% 0.0416, max 0.0526
True 53.3 +/- 4.7
True 40.41
True Bonferroni variant: 1638 voxels
True Bonferroni variant: 2724 voxels
True ii-bonf    B          5
True S7 reading b: 6 clusters
True CSI 0.582
True -0.18978
True -0.55017
True 0.95195
True S7 order table1  sign own  centre zero      Bonferroni a (56 tests, threshold 1.79e-04): 25
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
J=lambda c: ''.join(''.join(o.get('text','')) for o in c.get('outputs',[]))
print(J(nb['cells'][12])); t=J(nb['cells'][24]); print(t[:700])
EOF
```

```
lag        -10    -4     -2     -1      0      1      2      3     4     6      10
subject                                                                           
S1       0.514  0.538  0.569  0.629  0.691  0.729  0.687  0.606  0.60  0.59  0.518
S7       0.454  0.464  0.500  0.510  0.550  0.566  0.553  0.558  0.53  0.53  0.537
lag of the peak per subject: {'S1': 1, 'S7': 1}

R3_code
subject condition  expected  measured  within  null_max_a      p_a  null_max_b      p_b
     S1     human      0.51     0.512    True       0.045 0.000999       0.336 0.000999
     S1   vehicle      0.79     0.745    True       0.053 0.000999       0.088 0.000999
     S1   passive      0.64     0.621    True       0.055 0.000999       0.334 0.000999
     S3     human      0.70     0.695    True       0.048 0.000999       0.339 0.000999
     S3   vehicle      0.71     0.758    True       0.043 0.000999       0.303 0.000999
     S3   passive      0.05     0.062   False       0.065 0.001998       0.099 0.038961
     S5     human      0.66     0.763   False       0.042 0.000999       0.1
```

**Agent**

I've worked through every point in the round-2 report and re-run the entry. No outcome changed and nothing is under `proposed`: none of the new analyses supports a different outcome. `python tools/entry.py all entries/zhang-2021` passes (0 errors, about 23 min). Nothing is committed.

**Stale numbers (point 1).** The text had been written from an earlier run on a different machine. I ran the entry three times here and the attention results came out identical each time, so this setup is deterministic. The notebook, the summary and the record now match this run:
- **fig1-csi-s2:** 0.739, 0.717, 0.676.
- **att-csi-group:** 0.663, 0.730, 0.525.
- **supp-csi-per-subject:** all 12 measured values replaced from cell 24; S3 passive under reading (b) is now p = 0.039.
- **att-passive-lower:** "2 or 3" is now 2 (S3 and S5) everywhere, with the null quantiles and p-values updated.
- **att-classification:** 53.3%, and a per-subject range of 40.4 to 60.6%.
- **README:** the runtime now says about 25 minutes, not 55.

**S7 not normalized (point 2).** The paper's Methods say responses were "normalized to zero mean and unit variance", so the video game data are now z-scored per voxel over the session. This is recorded as a deviation on all five game claims, citing that passage. A new variant cell repeats the S7 analyses on the data as stored. Results with S7 z-scored:
- **game-csi:** 0.582, against 0.581 as stored.
- **game-mutual-negative-projection:** -0.190 and -0.550.
- **fig3b-state-relations:** 21 to 26 significant pairs in S7.
- **game-classification:** S7 is 26.9 to 34.1% with contiguous folds.
- **game-weights-two-groups:** 3 to 5 dimensions still fail in S7.

Every outcome holds either way.

**att-weights-cortex margin (point 3).** The notebook now prints the mean weights under threshold (ii) and the EBA margin for each subject. Under (ii), S2 fails by -0.041, and S1 and S3 pass by 0.079 and 0.044.
- I added a much stricter threshold as a variant: Bonferroni over each subject's region voxels. The pattern then holds in 5 of 5 subjects for the OLS (B) and denoised (B_L) weights, and 4 of 5 for the state directions (Q_S).
- The conclusion now says the outcome depends on filtering voxels by the encoding model (3 of 5 without that filter). It does not depend on the liberal t test.

**Coarse prefrontal region (point 4).** I added a variant using only the medial prefrontal areas (12,185 vertices, against 57,895 for the whole region). The same dimensions fail under every reading. The notes now also say the game-weights outcome rests on S7 alone.

**Round 2 in the record.** It is under `verifications`, with the verifier's reasons quoted or closely paraphrased and my responses. For game-weights-two-groups I recorded `agrees: true`, with the reason starting "Agrees only conditionally", as the report puts it.

**Not done:**
- **Questions file:** I added nothing to `questions/zhang-2021.yaml`, because the report names no place where the claims file misreads the paper.
- **Problem 9:** the report notes that the round-1 permutation-bound point is not tied to a claim. I left it as it was, since the verifier says it affects no conclusion.

## End of run

53 turns, 79 minutes, $3.55 at API prices, result: success.
