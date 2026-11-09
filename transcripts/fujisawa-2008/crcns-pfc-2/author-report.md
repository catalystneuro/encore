I've finished the author steps (1 to 5) and built the handover package (step 6). The run took about 2 h 15 min, from 13:14 to 15:27 UTC. The notebook takes 17.6 min under `tools/entry.py all`, and the last two clean runs gave identical numbers. `check` reports 0 errors. Nothing is committed.

The files are `entries/crcns-pfc-2-fujisawa-2008/` (the notebook `reproduce_fujisawa_2008.ipynb`, the helper `pfc2.py`, README, lock file) and `attempts/crcns-pfc-2-fujisawa-2008-01.yaml`. The handover is in `executed/crcns-pfc-2-fujisawa-2008/handover/`.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| unit-count | reproduced (627 cells against 633) |
| task-performance | blocked, `data_missing` (the data hold correct trials only) |
| fig2c-synchrony-by-layer | partially reproduced (layer 5 20.3% matches; layer 2/3 12.6% against 10) |
| fig2-population-uniform | not reproduced |
| lifetime-width | reproduced |
| trajectory-divergence | not reproduced |
| side-arm-selectivity-by-layer | not reproduced (62% and 54% against 40% and 22%) |
| central-arm-selectivity | not reproduced |
| odor-selective-fraction | not reproduced (45% against 26%) |
| odor-unrelated-to-stem | reproduced |
| retrospective-coding-rare | reproduced |
| connection-counts | not reproduced |
| cell-type-fractions | not reproduced |
| pyr-pyr-connections | not reproduced |
| fig3b-session-connections | not reproduced |
| fig3d-hub | not reproduced |
| fig3f-distance | partially reproduced (connections reach 1,400 µm, not 1,200) |
| nearby-pyr-int-probability | not reproduced |
| connected-cells-trajectory-specific | partially reproduced (3 of 4 values match) |
| no-spatial-clustering | reproduced |
| position-dependent-transmission | not reproduced |
| fig5a-session-selective-connections | not reproduced |
| fig4-pair-156-136 | not reproduced (region 0.325 to 0.645 against 0.4 to 0.6) |
| fig5b-example-pairs | not reproduced |
| thinning-preserves-dependence | reproduced |
| fig6-depression-facilitation | not reproduced |
| fig6b-convergent-examples | partially reproduced (186 facilitates; 197 is not significant) |
| fig7-supralinear-coincidence | not reproduced (15 satellites, no supralinearity) |
| speed-not-correlated | reproduced |
| population-vector-width | reproduced, resting on an assumption |

**(2) What was found about the dataset**
- **Coverage:** it holds 13 working memory sessions from 3 of the paper's 4 rats (EE, FF, GG); rat H is missing. Only correct trials are listed. The layer 5 session with 142 neurons, used in Figure 2a and Supplementary Figure 11, is not in the dataset.
- **The example file is misplaced:** the description lists `EE188_example.mat` as a file in folder EE0708, but it is inside `EE.188.tar.gz`, about 2 GB into the gzip stream. It holds the paper's 117 cells and the authors' `pairs_all`. My connection test finds all 43 of those pairs. That 43-pair graph's largest component is exactly the paper's 39-cell hub, so Figure 3d shows only part of the connections, chosen in a way the paper does not describe.
- **Cell-type labels disagree:** the `CellsInfo` type column never uses "unknown" in the 12 zipped sessions or in `EE188_Behavior_PFC.mat`, but the example file of the same session does (33 pyramidal, 15 interneurons, 69 unknown).
- **Cell selection is undocumented:** the files keep 627 cells out of 1,495 sorted clusters.
- **Trial labels start early:** spikes are labelled from the first nose-poke, while the description defines the trial start as the end of the nose-poke.
- **Missing metadata:** in 10 of 13 sessions the second LED is not tracked, so head direction is unavailable there. No layer is given per rat.
- **Assumptions:**
  - Rats EE, FF and GG are the paper's E, F and G, taken from Supplementary Figure 1; this gives the layers.
  - The jitter test's global band leaves 1% on each side; the 0.5%-per-side reading is shown for the connection counts and does not change any outcome there.
  - For population vectors, each cell's PSTH is normalised by its peak. This is the only outcome marked `assumed`.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings): how the global band's 99% level is split between the two sides, the CCG bin width, how the Figure 3d subset was chosen, and whether rates were normalised before the population vector correlations.
- **Questions to a reader:** none.

**(3) Where the protocol was unclear**
1. The prompt asks for a pinned published version, but `archives.md` says CRCNS is unversioned. I recorded `unversioned` with the MD5 sums from the dataset's `checksums.md5`, as `archives.md` says.
2. `archives.md` covers zips only, but the key file is inside a `.tar.gz`. I streamed the tar sequentially until that member, which takes about 2 minutes.
3. Readings multiply across dependent claims (bin width × width rule × cell-type rule × band split). I ran every combination for the counts, and ran the expensive downstream claims on one set of connections, which finds all of the authors' pairs, with one alternative bin width where cheap. The protocol does not say how to handle this.
4. When the data lack some of a claim's subjects (the layer 5 session), the protocol has no rule for testing part of a claim. I tested the available part and said so. Where values were missing I left out `measured`, because it must have one value per expected value.
5. Whether `assumed` covers an assumption about the data (which rat is which) as well as about methods is not said. I recorded the rat mapping as a deviation only.
6. My development environment gave slightly different numbers from the locked one for one cell. I took every number from the executed copy and corrected the texts to match.

**(4) What failed**
One locked run failed because a loop variable overwrote the position grid `G`. I fixed it and re-ran.

Some tests were run more cheaply than the claims file names: the spike-order test used 100 surrogates and 500 permutations (instead of 1,000) for run time. The variant that jitters only the presynaptic cell was not run. The untracked dotfiles in the repository root are sandbox device mounts, not files I created.
