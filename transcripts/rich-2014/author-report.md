All 27 claims have an outcome. 14 are reproduced (one of them resting on an assumption), 6 partially reproduced (one resting on the assumption), 6 not reproduced (two resting on the assumption) and 1 blocked. The entry is locked, checked (0 errors) and ran clean in 2.8 min with 1.1 GB peak memory, and the handover is built in `executed/rich-2014/handover/`. Nothing is committed.

**1. Outcomes** (P-a and P-b are the claims file's two readings of a "pass" through a place field; F-b is the data set's own fields, shown as a variant)

| Claim | Outcome |
|---|---|
| cell-counts | reproduced (253 cells; 63, 58, 24, 57, 51 exactly) |
| figs3-cluster-quality | blocked, data_missing |
| fig1-recruitment-by-section, fig2-individual-poisson, fig2bc-population-bias | reproduced |
| figs6-few-field-cells-uniform | reproduced (assumed P-a) |
| fig3b-overdispersion, fig3b-negbin-fit (r 0.559, p 0.152), fig3c-recruitment-fraction, fig3c-extrapolation-500m (519 m) | reproduced |
| figs7a-mean-fields-per-animal | partially reproduced (3 of 5 animals) |
| fig3c-lomax-recruitment | partially reproduced (assumed P-a; KS 0.040 against 0.05) |
| fig3d-uniform-density | partially reproduced (KS 0.044 against 0.03, p > 0.05) |
| figs10-no-track-or-speed-influence | not reproduced (assumed P-a) |
| figs11-propensity-stationary, fig3e-memoryless-recruitment, figs16-anatomy, fig4a-pre-sleep-rate, figs8-silent-cells-form-fields, figs17-propensity-across-environments | reproduced |
| figs11-no-boundary-remapping | not reproduced (assumed P-a; p 0.03 at the boundary of sections 3 and 4) |
| figs12-pairs-uncorrelated | not reproduced (pairs of cells correlate by r about 0.01 to 0.03, above the null) |
| figs14-field-properties | not reproduced (one size correlation has p < 0.05 under every reading) |
| figs15-higher-threshold | partially reproduced (38 to 44% of fields kept, against 50%) |
| fig4b-single-field-proportion, fig4c-active-subsets | not reproduced under the claims file's criterion; both asked of a reader |
| figs5-silent-cells-low-rate | partially reproduced (silent-cell rate 0.018 Hz against 0.006) |

**2. The dataset, assumptions and questions**
- **What it holds.** `resSave.mat` (167 MB, MD5 matches `checksums.md5`) holds the paper's 253 cells and its own fields. Those fields reproduce the per-animal means of Fig. S7A exactly and give r 0.565, p 0.139.
- **My recomputed fields.** I recomputed fields by the Methods. They come out about 10% fewer than the data set's (791 against 887) and match 81% of them.
- **What is missing.** The L-ratio and isolation-distance fields are empty for every unit, and there are no unclustered spikes or waveforms. The track's scale model (its corners) is not included.
- **Units and codes.** No units are stated: positions are in inches, the open field in pixels, speed in inches per microsecond. The data set's maps use 1-inch bins where the Methods say 1 cm. The fields' direction code is undocumented, and the region is "N/A" for every unit of one animal.
- **Disagreements with the paper.** The section lengths are 3.7, 6.1, 11.5 and 26.9 m against the Methods' 3, 7, 12 and 26 m. The open field spans about 100–119 × 72–97 cm against the stated ~40 × 100 cm.
- **Checks that passed.** Spikes and position share a clock, as do the ripple periods. Units look like the same cells across epochs. No unit is deposited twice.
- **Version.** CRCNS does not version data sets, so it is recorded as `unversioned` with DOI 10.6080/K0BV7DT2 and the MD5. This is the only published state, and the paper cites none.
- **Assumption.** Where P-a and P-b give different outcomes (four claims), I adopted P-a. The Methods say passes "through the field", and the data set's own pass counts are closer to P-a (exact agreement 0.469 against 0.392). Under P-b those four claims would all be reproduced.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings): what counts as a pass, and how the corners of Fig. S10 are defined.
- **Questions for a reader** (`questions/rich-2014.yaml`):
  - fig4b: the "factor of 10" range is not in the paper, and the paper's own printed parameters only reach a factor of 5.5.
  - fig4c: whether the mean over environment pairs larger than 10 m, against the fitted equal rate, is a reading of the missing Fig. 4C.

**3. Protocol gaps**
1. The prompt says to pin "a published version", but CRCNS has none. I followed archives.md (`unversioned` plus MD5).
2. Some criteria name no outcome between "reproduced" and "not reproduced" (figs15, figs5). I used the protocol's general definition of `partially_reproduced` and said so in the notes.
3. Some criteria say "under one reading" while the opening comment says "the outcome all readings give". Where a criterion says "under one reading", I let that decide.
4. In a figs10 panel with only one applicable test reading, "fails under all of them" is ambiguous. I read it as failing under that one test.
5. The questions file format for non-DANDI datasets is not specified. I keyed it by `paper:` alone, without a `dandiset:` line.
6. Step 1.2 asks to show that a unit is the same across sessions, but gives no method. I used nearest mean peak amplitude on the same tetrode.

**4. Runtime and failures.** The notebook takes about 3 min; all work finished at about 00:54 UTC. One editing slip stripped the bold from the Result openers; I caught and restored it before the final run. Nothing failed in the final run.
