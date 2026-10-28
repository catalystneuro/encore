The claims file holds up well against the paper and is ready for an attempt. I made six small corrections and left two discrepancies open.

**Checker:** `24 claims, 23 quotes, 29 statistical values, 0 problems`, both before and after my edits.

**What holds up:**
- I checked all 24 claims against the text and Tables 1 to 3.
- I cloned the paper's code (`SwannLab/Jackson_2019` at commit `a7c89f5`) and checked the opening comment's description of it. It is accurate: the filter tap counts, the sharpness and steepness functions, how artifact marks are applied, the PAC formula, the Wilcoxon p-value method, and the Cohen's d formula. The code's printed values match the paper's Tables 1 and 2 and its Figure 3 correlations.
- The six-test multiple-comparison correction for Table 1 reproduces the printed corrected p-values.
- Every main finding has a claim.

**Changes, by claim:**
- **table1-alpha-shape-off-on** (and the opening comment): the alpha filter length was given only as the code's 3-cycle rule (192 taps), but the code holds no alpha analysis. I added the Methods' 231 ms for beta (118 samples) as a second reading.
- **fig2-steepness-off-on:** the uncorrected p is now labelled uncorrected, with its corrected value, as in the sharpness claim.
- **fig2c-topography-sensorimotor:** the paper does not say that F7, F8, T7 and T8 must be non-significant. I marked that condition, like the set of neighbouring electrodes, as this file's own reading.
- **fig1c-beta-alpha-peaks:** the paper does not say which electrodes the power spectra use. I marked this as open: C3 and C4 is the main reading ("as would be expected in sensorimotor EEG"), and all scalp electrodes is a variant.
- **q4-patient-counts:** the statement says eight patients have both electrodes in quadrant 4, but that number was missing from the expected values. I added it.
- **table3-q4-effect-size:** the Table 3 effect sizes were only to be reported and did not affect the outcome. Full reproduction now requires them to be within tolerance.

**Open:**
- Table 2 prints a corrected p of 1 for its three non-significant tests. The standard correction (Benjamini-Hochberg) over its six tests gives about 0.36. No outcome depends on this.
- For PAC in all patients, Table 3 gives an effect size of 0.75 and Table 1 gives 0.83 (0.83 is what the code computes on raw PAC). Computing it on log PAC, as the Methods say, probably explains 0.75, but the paper does not say so. The criterion already accepts either reading.

**Ready:** yes. The check entry is recorded under `checks` with `ready: true`. Nothing is committed.
