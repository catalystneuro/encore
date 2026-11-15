# zhang-2021 · verifier-2 · run 43607034185

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 444
drwxr-xr-x 6 runner runner    4096 Nov 14 15:22 .
drwxr-xr-x 8 runner runner    4096 Nov 14 15:22 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 14:51 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 14:51 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 14 15:22 .claude
-rw-r--r-- 1 runner runner       0 Nov 14 15:22 .env
-rw-r--r-- 1 runner runner       0 Nov 14 15:22 .env.development
-rw-r--r-- 1 runner runner       0 Nov 14 15:22 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 14 15:22 .env.local
-rw-r--r-- 1 runner runner       0 Nov 14 15:22 .env.production
-rw-r--r-- 1 runner runner       0 Nov 14 15:22 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 14 15:22 .env.test
-rw-r--r-- 1 runner runner       0 Nov 14 15:22 .env.test.local
drwx------ 2 runner runner    4096 Nov 14 15:22 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 14:51 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 14:51 .github
-rw-r--r-- 1 runner runner       0 Nov 14 15:22 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 14:51 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 14:51 .mcp.json
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; head -50 zhang-2021.yaml; echo ----; cat zhang-2021-01.yaml
```

```
<persisted-output>
Output too large (34.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/ce595db4-280d-4c5f-9a97-6bea4ca6c207/tool-results/b4bjel888.txt

Preview (first 2KB):
# Zhang et al. (2021) on CRCNS vim-4

Tests the findings of Zhang, Gao, Cukur and Gallant (2021), "Voxel-Based State Space Modeling
Recovers Task-Related Cognitive States in Naturalistic fMRI Experiments", Frontiers in Neuroscience
14:565976, on CRCNS data set vim-4 (doi:10.6080/K0668BDF), streamed from the public CRCNS bucket.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

- `reproduce_zhang_2021.ipynb`: the data check and one section per claim.
- `statespace.py`: loading, the state space of the paper's code (computed in the space of the 24
  principal components), the cluster separation index, the classifiers, and the atlas regions and
  encoding models of the two cortical claims.

The two cortical claims use two public fsaverage atlases in place of the paper's ROIs, which are
not deposited: visfAtlas (Rosenke et al. 2021, doi:10.1093/cercor/bhaa246) and HCP-MMP1.0 on
[... 16 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "zhang-2021-01.yaml"
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

**Agent calls Read**

```json
{
 "file_path": "zhang-2021.yaml"
}
```

```
1	# Claims for Zhang, Gao, Cukur & Gallant (2021), Frontiers in Neuroscience 14:565976,
2	# "Voxel-Based State Space Modeling Recovers Task-Related Cognitive States in Naturalistic fMRI
3	# Experiments", doi:10.3389/fnins.2020.565976, on CRCNS data set vim-4 (doi:10.6080/K0668BDF).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-14.
6	#
7	# Text read: the version of record (PMC8145286, open access), as JATS XML flattened to text under
8	# paper/: main text, Materials and Methods, figure legends, Table 1, and the supplement
9	# (Data_Sheet_1.DOCX, legends of Supplementary Figures 1 to 5). No PDF was supplied. The
10	# per-subject CSI values of the attention task are printed only inside the images of
11	# Supplementary Figures 1 and 2; they were read from the images in the supplement file (S1
12	# 0.51, 0.79, 0.64; S3 0.70, 0.71, 0.05; S4 0.64, 0.69, 0.47; S5 0.66, 0.74, 0.59; S6 0.60, 0.71,
13	# 0.61, for attend-humans, attend-vehicles and passive). The images of Figures 1 to 4 of the main
14	# text were not available, so the pattern of Figure 3B is not known here. Two inconsistencies of
15	# the paper, noted where they matter. (1) The means of the six per-subject CSIs in Figure 1 and
16	# the supplement (0.64, 0.72, 0.51) are not exactly the means the Results give (0.66, 0.74, 0.53).
17	# (2) The Figure 1 legend says blue is "only humans present" and green "only vehicles present";
18	# the supplement legend and the plotted positions say the reverse (green humans, blue vehicles).
19	# The video game subjects are S1 and S7 in the text and C1 and C2 in the legends of Figure 3 and
20	# Supplementary Figure 4; C1 is S1 (CSI 0.72 in both) and C2 is S7.
[... 441 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('reproduce_zhang_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"=== CELL {i} [{c['cell_type']}] ===")
    print(src)
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if 'text' in o: print('--OUT--\n'+''.join(o['text']))
            elif 'data' in o:
                d=o['data']
                if 'text/plain' in d and 'image/png' not in d: print('--OUT--\n'+''.join(d['text/plain']))
                elif 'image/png' in d: print('--IMG--')
            elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
EOF
```

```
<persisted-output>
Output too large (152.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/ce595db4-280d-4c5f-9a97-6bea4ca6c207/tool-results/boi9zkygw.txt

Preview (first 2KB):
=== CELL 0 [markdown] ===
# Reproducing Zhang, Gao, Cukur & Gallant (2021) from CRCNS vim-4

Paper: Zhang T, Gao JS, Cukur T, Gallant JL (2021). Voxel-Based State Space Modeling Recovers
Task-Related Cognitive States in Naturalistic fMRI Experiments. Frontiers in Neuroscience
14:565976. doi:10.3389/fnins.2020.565976.

Claims: `claims/zhang-2021.yaml`, written from the version of record (PMC8145286) and its
supplement (Data_Sheet_1.DOCX), with the paper's code, gallantlab/state-space at commit 6ffb3c3.

Dataset: CRCNS vim-4, "Whole-brain BOLD activity recorded by fMRI during a visual attention task
and a video game task", doi:10.6080/K0668BDF, streamed from the public bucket
`s3://crcnsarchive/vim-4/live/`. Version: `unversioned`. CRCNS data sets have no versions; the
files read are those under `vim-4/live/` as of 2026-11-14 (data description version 0.8 of
2026-04-06), which is the only published copy of the data files (`vim-4/old/` holds only older
versions of the description). The paper cites the data set by its DOI, with no version. The MD5
[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/ce595db4-280d-4c5f-9a97-6bea4ca6c207/tool-results/boi9zkygw.txt",
 "limit": 700
}
```

```
1	=== CELL 0 [markdown] ===
2	# Reproducing Zhang, Gao, Cukur & Gallant (2021) from CRCNS vim-4
3	
4	Paper: Zhang T, Gao JS, Cukur T, Gallant JL (2021). Voxel-Based State Space Modeling Recovers
5	Task-Related Cognitive States in Naturalistic fMRI Experiments. Frontiers in Neuroscience
6	14:565976. doi:10.3389/fnins.2020.565976.
7	
8	Claims: `claims/zhang-2021.yaml`, written from the version of record (PMC8145286) and its
9	supplement (Data_Sheet_1.DOCX), with the paper's code, gallantlab/state-space at commit 6ffb3c3.
10	
11	Dataset: CRCNS vim-4, "Whole-brain BOLD activity recorded by fMRI during a visual attention task
12	and a video game task", doi:10.6080/K0668BDF, streamed from the public bucket
13	`s3://crcnsarchive/vim-4/live/`. Version: `unversioned`. CRCNS data sets have no versions; the
14	files read are those under `vim-4/live/` as of 2026-11-14 (data description version 0.8 of
15	2026-04-06), which is the only published copy of the data files (`vim-4/old/` holds only older
16	versions of the description). The paper cites the data set by its DOI, with no version. The MD5
17	sums of the files read, from the data set's `checksums.md5`, are:
18	
19	| file | MD5 |
20	|---|---|
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/ce595db4-280d-4c5f-9a97-6bea4ca6c207/tool-results/boi9zkygw.txt",
 "offset": 700,
 "limit": 700
}
```

```
700	2       S1   vehicle    0.745       0.008      0.762    0.730     0.790  0.716         0.053         0.041         0.088         0.067
701	3       S2   passive    0.676       0.005      0.657    0.638     0.681  0.632         0.062         0.042         0.352         0.332
702	4       S2     human    0.739       0.005      0.723    0.683     0.784  0.664         0.040         0.030         0.322         0.283
703	5       S2   vehicle    0.717       0.005      0.718    0.684     0.779  0.668         0.056         0.036         0.326         0.303
704	6       S3   passive    0.062       0.003      0.059    0.042     0.082  0.028         0.065         0.047         0.099         0.063
705	7       S3     human    0.695       0.006      0.703    0.669     0.761  0.647         0.048         0.033         0.339         0.301
706	8       S3   vehicle    0.758       0.004      0.728    0.699     0.807  0.674         0.043         0.033         0.303         0.272
707	9       S5   passive    0.613       0.006      0.622    0.602     0.657  0.592         0.094         0.045         0.347         0.284
708	10      S5     human    0.763       0.005      0.694    0.661     0.775  0.640         0.042         0.031         0.126         0.090
709	11      S5   vehicle    0.731       0.005      0.698    0.646     0.753  0.626         0.096         0.082         0.340         0.292
710	12      S6   passive    0.652       0.005      0.637    0.605     0.672  0.599         0.066         0.050         0.297         0.269
711	13      S6     human    0.606       0.007      0.627    0.595     0.687  0.575         0.048         0.033         0.292         0.265
712	14      S6   vehicle    0.700       0.004      0.735    0.709     0.796  0.689         0.046         0.033         0.321         0.283
713	null p-values are at most 1/1001 = 0.0010 when the observed CSI exceeds every null value
714	elapsed 309 s, peak memory 4.7 GB
715	
716	=== CELL 16 [markdown] ===
717	### fig1-csi-s2
718	
7
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/ce595db4-280d-4c5f-9a97-6bea4ca6c207/tool-results/boi9zkygw.txt",
 "offset": 1399,
 "limit": 800
}
```

```
1399	    pos = ss.positions(Z, X)
1400	    for reading in "abc":
1401	        mem, nm, dropped = ss.game_members(X, names, reading)
1402	        vals = [ss.csi(pos, mem, np.random.default_rng(k)) for k in range(10)]
1403	        null = []
1404	        for _ in range(N_PERM):
1405	            Xp = X[rng.permutation(len(X))]
1406	            memp, _, _ = ss.game_members(Xp, names, reading)
1407	            null.append(ss.csi(ss.positions(Z, Xp), memp, rng))
1408	        null = np.array(null)
1409	        game_csi[s, reading] = np.mean(vals)
1410	        e, tol = exp_g[s]
1411	        print(f"{s} reading {reading}: {len(mem)} clusters (sizes {[int(m.sum()) for m in mem]}; dropped {dropped}); "
1412	              f"CSI {np.mean(vals):.3f} (seed SD {np.std(vals):.3f}); expected {e} +/- {tol}, within: {abs(np.mean(vals)-e) <= tol}; "
1413	              f"null mean {null.mean():.3f}, max {null.max():.3f}; above every null value: {np.mean(vals) > null.max()}")
1414	print(f"elapsed {time.time()-T0:.0f} s")
1415	--OUT--
1416	S1 reading a: 8 clusters (sizes [72, 183, 488, 812, 53, 141, 208, 64]; dropped [('flash', 9)]); CSI 0.694 (seed SD 0.003); expected 0.72 +/- 0.072, within: True; null mean 0.192, max 0.258; above every null value: True
1417	
1418	--OUT--
[... 661 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def \|zscore\|z-score\|std(\|/ sd\|mean(0)" statespace.py | head -80
```

```
13:  = responses x those columns, z-scored per dimension over the TRs fitted.
63:def _open(path, block_size=2**24):
67:def read_hdf(path, keys=None):
74:def hdf_layout(path):
83:def npy_layout(path):
90:def load_attention_states():
95:def presence_code(states):
100:def gram_summary(Y):
102:    sd = Y.std(0)
104:            "vox_mean_range": (float(Y.mean(0).min()), float(Y.mean(0).max())),
109:def code_positions(X, Y, num_PCs=N_PCS):
123:    return stats.zscore(Y @ Q[:, :X.shape[1]])
126:def load_attention_gram(subject, X_check=None, keep=None):
147:def load_game(subject, keep=None):
168:    out["BL_vox"] = ((Y - Y.mean(0)).T @ ((Z / (Z ** 2).sum(0)) @ coef.T)).T
178:def pca_scores(G, train, test=None, k=N_PCS):
205:def state_directions(Z, X):
218:def positions(Z, X, sign=None):
229:    pos = (pos - pos.mean(0)) / pos.std(0)
239:def _fit_normal(x):
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 140,178p statespace.py; sed -n 540,680p statespace.py
```

```
out["code_coef_norm"] = np.linalg.norm(np.linalg.pinv(P.T @ P) @ (P.T @ Y), axis=1)
    if keep is not None:
        out["Y_keep"] = Y[:, keep].astype(np.float32)
    del Y
    return out


def load_game(subject, keep=None):
    """Stream one subject's video game BOLD (npy) and its state labels.

    Also the voxel maps of the OLS weights B and denoised weights B_L of every state (data
    set column order, states with no TRs dropped), for the correlation variant of
    game-weights-two-groups, and with keep the responses of those voxels (float32).
    """
    with _open(f"VideoGame/Data/{subject}.npy") as f:
        np.lib.format.read_magic(f)
        shape, fortran, dtype = np.lib.format.read_array_header_1_0(f)
        Y = np.frombuffer(f.read(), dtype=dtype).reshape(shape).astype(np.float64)
    out = gram_summary(Y)
    st = read_hdf(f"VideoGame/Stimuli/{subject}.hdf")
[... 149 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 96,135p statespace.py; grep -n "z-scor\|normaliz" statespace.py reproduce_zhang_2021.ipynb | head -30
```

```
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
    parameters = np.ones([X.shape[0], X.shape[1] + 1])
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "z-scor\|zero mean\|unit variance\|normaliz" paper/10.3389-fnins.2020.565976.txt paper/vim-4.data-description.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent**

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
| game-classification | partially_reproduced | yes. Cell 48: S1 is above tolerance under every reading, and every reading is significant. | none |
| game-weights-two-groups | not_reproduced | I agree only conditionally. The outcome rests on S7 alone (cell 53). | The atlas assumption is stated. One assumption that bears on the outcome is not stated: S7's BOLD goes into the analysis without z-scoring (see 3). |

**2. Text against the printed outputs**

This notebook's outputs come from a later execution than the one the conclusions and the record were written from. The R3 values and everything derived from them differ from the text:

- Cell 19 says "0.743 (attend-humans), 0.721 (attend-vehicles) and 0.675 (passive)". Cell 17 prints 0.739, 0.717 and 0.676. The record's measured values (0.743, 0.721, 0.675) and its response to round 1 ("This run gives 0.743, 0.721 and 0.675") are wrong in the same way.
- Cell 13 says "S2 attend-humans 0.740 in the first run, 0.743 in this one". Cell 15 prints 0.739.
- Cell 22 says "0.665 +/- 0.104 ..., 0.731 +/- 0.023 ... and 0.524 +/- 0.260" and "S3's CSI (0.061)". Cell 21 prints 0.663, 0.730 and 0.525, and cell 15 prints 0.062. The record's measured values (0.665, 0.731, 0.524) are wrong in the same way.
- Cell 25 says "S3 passive (0.061 ...)", "S5 attend-humans (0.767 ...)" and "Under reading (b) S3 passive has p = 0.045". Cell 24 prints 0.062, 0.763 and p_b = 0.039. Eleven of the twelve values in the record's measured list for supp-csi-per-subject differ from cell 24's R3 column (for example S1 attend-humans 0.515 against 0.512); only S6 attend-vehicles (0.700) matches.
- Cell 28 says "in 2 or 3 of the 5 subjects under every combination of reading and null run with the code's positions". Cell 27 prints 2 under every R3 combination, for both reading (a) and reading (b), so "or 3" has no support. The same applies to the Summary row in cell 55 ("2 or 3 of 5 subjects at the bound reached") and to the record's "2 or 3 under reading (b)".
- Further stale values in cell 28 and the record's notes for att-passive-lower:
  - "S1 0.515 against 0.620": printed 0.512 and 0.621.
  - "S6 0.605 against 0.651": printed 0.606 and 0.652.
  - "mean differences 0.668 and 0.135": printed 0.665 and 0.134.
  - "S2's mean difference, 0.057": printed 0.0525.
  - "99th percentile (0.042 to 0.055)": printed 0.0416 to 0.0562.
  - "maximum (0.052 to 0.084)": printed 0.0526 to 0.0840. S2's 0.0525 now sits just below the 0.0526 maximum (matched, null ii).
  - "p = 0.001 to 0.010": the printed p_mean ranges from 0.002 to 0.015.
  - "p 0.30 to 0.51": the printed R3 values range from 0.34 to 0.51.
- Cell 31 says "53.8% (contiguous, density)" and "Per subject the accuracy is 39.9 to 60.6%". Cell 30 prints 53.3 and a per-subject range of 40.4 to 60.6. The record's notes also give 53.8. The statement that the first run gave 53.4% "with the same code and seeds" now differs from this run by only 0.1.
- The README says the notebook "runs in about 55 minutes". The last printed elapsed time is 1430 s (cell 48), and the remaining cells are short, so nothing printed supports 55 minutes.
- Everything else I checked matches the printed numbers: cells 35, 40, 43, 46, 50 and 54, the rest of the Summary, the record's notes for att-weights-cortex, game-csi, game-mutual-negative-projection, fig3b-state-relations, game-classification and game-weights-two-groups, and the record's findings.
- The record states my round-1 reasons accurately, and mostly in my words. Several are verbatim (att-csi-group, supp-csi-per-subject, game-mutual-negative-projection). Problem 9, the permutation bound, is not attributed to a claim, but it does not affect a conclusion.

**3. Round-1 points**

Resolved:

- **Problem 1:** cell 7 prints the norm of the code's attention coefficients, about 1e-13.
- **Problem 2:** cell 26 states the mismatch, and cell 27 prints the null quantiles.
- **Problem 3:** both claims are now tested with atlas regions, and the superseded mappers are checked (cell 10).
- **Problem 4:** cell 11 shows the run structure, and the game-classification notes now draw on it.
- **Problem 5:** cells 39 and 49 add the lag +1 variants.
- **Problem 7:** the scoring is fixed.
- **Problem 8:** the centred test is added.
- **Problem 6:** stated, but folds with a gap at their edges were not run. That does not affect a conclusion.
- **Problem 9:** accepted as before.

All of the "Not checked" items have been addressed.

Remaining points that bear on a conclusion:

1. **Stale numbers.** The numbers listed in section 2 need to be updated from this notebook. This includes the measured values for three claims and the "2 or 3" count. The outcomes do not change.
2. **S7 game data are not normalized (new).** The paper says responses were "normalized to zero mean and unit variance". `load_game` uses S7's BOLD as stored (voxel SDs 0.094 to 1.009), with no z-scoring before the PCA, the OLS or the region means. The record reports this as a data finding but does not list it as a deviation. game-weights-two-groups is decided by S7 alone, so its not_reproduced outcome rests on this unstated choice. It also affects the S7 values in game-csi, game-mutual-negative-projection, fig3b-state-relations and game-classification.
3. **att-weights-cortex has a thin margin.** The 4 of 5 count holds only under threshold (ii). Under (i), the B and B_L readings fail in S3 by a near-tie in EBA (human 0.313, vehicle 0.314, cell 34). The values under (ii) are not printed, so the margin there cannot be judged. Threshold (ii) relies on a t test that assumes independent TRs. The conclusion should say the outcome hinges on this.
4. **game-weights-two-groups regions (minor).** The "prefrontal" region covers 57,895 vertices, which is most of the frontal lobe, so the S7 failure also depends on how coarsely the regions are drawn.

## End of run

13 turns, 2 minutes, $1.51 at API prices, result: success.
