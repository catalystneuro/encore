I've completed author steps 1 to 6 for `strickland-2022`. `python tools/entry.py all` reports 0 errors and the notebook passes on a clean run in 99 s. The handover package is in `executed/strickland-2022/handover/`. Nothing is committed.

**1. Outcomes (30 claims, none blocked)**

| Claim | Outcome |
|---|---|
| source-data-cluster-link | reproduced (all 1812 cue and outcome rows match exactly one unit) |
| fig1c-suppression-order | reproduced (F(2,142) = 147.9) |
| figs2-each-rat-discriminates | reproduced (reading c-c, 8 of 8 rats) |
| units-sessions-subjects | reproduced |
| fig1e-regions | reproduced |
| fig2b-cue-clusters | reproduced |
| fig2c-cue-pc1-ordered | reproduced (29.73%) |
| fig2c-pc1-contribution | reproduced |
| fig2d-danger-latency | not reproduced (R2 = 0.067, p = 0.26) |
| fig2e-cue-subnetwork | reproduced (with r squared) |
| fig2f-cue-hubs | partially reproduced, rests on an assumption |
| fig2g-cue-anatomy | reproduced |
| fig3a-cluster-signals | partially reproduced (2 of 4 shapes) |
| fig3b-signal-pca | reproduced (62.73 / 26.21%) |
| fig3c-subnetwork-lesion | partially reproduced |
| fig3d-supranetwork-lesion | reproduced |
| fig3e-network-anatomy | reproduced |
| fig4b-outcome-clusters | partially reproduced (smallest cluster 29, expected 46) |
| fig4c-positive-prediction-error | reproduced (17.68%) |
| fig4b-phasic-network, fig4b-tonic-network | reproduced, both rest on an assumption |
| fig4e, fig4f, fig4g | reproduced |
| fig5a, fig5b, fig5c, fig5d, fig5e | reproduced |
| cue-outcome-membership-independent | reproduced |

**2. Dataset, assumptions and questions**

What the dataset holds:
- The zip holds 1812 unit files, a cube file and the paper's MATLAB scripts.
- The scripts settled most of the details the claims file leaves open. Its normalization is the only one that reproduces the Source Data rows; the claims file's four readings do not. They also fixed the shuffle direction, the regression form and the lesion procedures.
- With those scripts, the cube gives the paper's 29.7% and 17.7% exactly. The claims file's 47.1% and 24.2% came from Source Data sheets that hold baseline-subtracted heat-plot rows, not the matrices the PCA was run on.

Findings about the data:
- 204 unit files contain repeated spike times (9289 in total). The script counts each time once.
- The dataset has 73 sessions; Supplementary Table 1 lists 75.
- Session js27101920 has 5 shocks; none is recorded on its first danger trial.
- In session js10030220, 3 of 22 unit files have event times that drift up to 0.3 s away from the other 19.
- Region names are stored as MATLAB string objects that cannot be read outside MATLAB, and the region numbers only make sense with the scripts' remapping.
- The dataset has no cluster labels, so the paper's clusters come only from its Source Data.

Assumptions:
- For fig2f and the two fig4b network claims I used r squared, the "(R2)" the Methods name and the coefficient the scripts plot. With plain r, fig2f would be not reproduced and both network claims partially reproduced.

Questions for the paper's authors (recorded as findings):
- The Source Data latencies match a change-point search starting 2 s before cue onset, not the 10-s cue window the Methods describe. They also cover 1498 units by an unstated rule.
- The Source Data cue-hub values are r squared computed over all three cues, not over danger firing alone as the Methods say.
- Are the network correlations judged on r or r squared?
- Other inconsistencies:
  - The Methods put shock first in the outcome beta matrix; the code and Source Data put prediction error first.
  - Source Data Fig. 4f swaps the k7 and k8 labels.

I asked a reader no questions; I found no misreading of the paper in the claims file.

**3. Where the protocol was unclear**
1. CRCNS asks for the MD5s of the files read, but data.zip is opened in place and not downloaded whole, so its MD5 cannot be checked. I printed the bucket's `checksums.md5` without verifying it.
2. The link criterion lists four normalization readings, and the matching one came from the paper's code. I took it under step 1.6 and showed the four readings as well. The protocol does not say whether an author may add a reading to a link criterion.
3. The paper's own Source Data sometimes contradicts its Methods (fig2d window, fig2f measure). The precedence order in reader step 2 does not cover Source Data. I kept the Methods, as the criterion has them, and showed the Source Data version as a variant.
4. Several criteria give separate rules for L1 (the paper's clusters) and L2 (my own k-means). I let L1 decide and reported the L2 results in the notes. For fig2c-pc1-contribution, L2 fails (411 units in place of 505).
5. fig5e is a claim of absence with no test in the paper but two readings. The protocol says absence is judged on the paper's test alone. I judged it on the reading the paper's Source Data uses and showed the other, which would not reproduce it.
6. The per-animal breakdown rule fits poorly when results are per cluster. I broke down the behaviour, both PCA claims and the subnetwork share.

**4. Runtime and failures**
- The run took about 40 minutes of the 5-hour budget (01:09 to 01:48 UTC). The notebook runs in about 1.5 minutes with 1 GB peak memory.
- Nothing failed in the final run. Two early development errors were fixed: an array shape mismatch in the fig4f cell, and raw spike counts that differed from the cube until repeated spike times were counted once.
