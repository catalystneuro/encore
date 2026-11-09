**Verifier report: round 2, DANDI:001708 / doi:10.64898/2025.12.15.693905**

The claims file has 34 claims, and the attempt record has 34 outcomes (28 reproduced, 3 partially reproduced, 3 not reproduced) and 34 verification results. The ids match one to one. Ten outcomes carry `assumed: true`: fig3d-neutral-psd and the nine GP claims.

One general finding comes first. The record and the "**Result:**" cells of `evoked.ipynb` were written from an earlier execution than the one delivered. Nearly every model number differs from the printed output in the third digit. A few statements are now contradicted outright (section 2).

### 1. Outcomes

**I agree with all 34 stated outcomes.** On the printed outputs, the five claims I disputed in round 1 now meet their criteria on converged OFF fits, on both trial sets and under both priors:

- **fig1c-withdrawal-locked:** heat-aligned switch HDIs lie wholly after the withdrawal-aligned ones (evoked cell 55).
- **fig2h-off-linear-exponential:** linear+exp is the top OFF sigmoid model, by 5.09 (dse 3.58) with pinches and 2.85 (dse 3.53) without (cell 35).
- **figs1-completion-asymmetry:** OFF 90% fall at 0.073 s, HDIs disjoint in all four pairings (cell 47).
- **recovery-timing:** 4 of 4 inside in all four pairings (cell 49).
- **tables3-s7-withdrawal-steeper:** OFF k 2.729 vs 1.747, ON τ_pre 0.655 vs 1.309, HDIs disjoint on the same trial set (cell 53).

tables9 remains not reproduced on either trial set: the sigmoid is never higher for both recoveries (cell 41).

**Assumptions:**

- **fig3d (10% prominence threshold):** stated and reasonable. The outcome holds at 10% and 20% but not at 5%, and the record says so.
- **GP settings (100 inducing points, p_noise 0.01, 5000 iterations instead of the criterion's 200 / 0.001 / 10000):** stated, and well supported. Stored fits have noise_prob 0.01 and match cell by cell (Spearman r 0.948–0.999, gp cell 6).
- **Null GP (code's contamination range, 0..max count, instead of the criterion's "same likelihood"):** stated in fig5b-train-r2's deviation, and reasonable given the null-likelihood match. Two outcomes depend on it:
  - fig5b-test-r2: with the criterion's same-likelihood null, NEUTRAL p is 0.052 (gp cell 16), so the outcome would be partially reproduced. The record says this.
  - fig5b-test-group-differences: holds under that null too.
- **Multi-start MAP chain start (not flagged as an assumption):** reasonable to treat as a sampler setting. The lower mode is about 238 log-posterior units down. Note that 7 of 9 MAP starts land in that mode (cell 20).

### 2. Sentences the printed outputs do not support

**evoked.ipynb**

- **Cell 24 / record figs8 notes:**
  - "converges (r_hat at most 1.007), except OFF_erf_linear with pinches (r_hat 1.148)". The record says "at most 1.008".
  - Printed (cell 20): OFF_erf_linear has r̂ 1.017 with 80 divergences; OFF_erf_double has 1.009.
  - **OFF_erf_linear_np has r̂ 1.393, ESS 9, 572 divergences and an lp spread of 3.2, so it is not converged.**
- **Cell 63 (Summary) "With that start every fit converges"; record responses "All fits now converge":** contradicted by OFF_erf_linear_np.
- **Cell 42 / record tables9 notes**, against cell 41:

  | Statement | Printed |
  |---|---|
  | with pinches, sigmoid below erf by 0.08 (double) | above by 0.10 |
  | with pinches, below by 0.61 (dse 1.71) (linear) | −0.89 |
  | 0.42 against the target_accept 0.95 fit | −0.44 |
  | without pinches, above by 0.17 (double) | −0.08 |
  | without pinches, below by 0.88 (linear) | **+0.96** |
  | "here, without pinches, −6263.89 against −6264.77" | −6265.65 (erf) against −6264.68, i.e. the sigmoid is higher, against an unconverged erf fit |

  The record's finding "here by 0.53, dse 1.84" appears in no output.
- **Cell 30, the record's fig2g notes, and the deviation repeated in 10 outcomes:** "−0.636 s", "r_hat 1.69", "three chains", "1121 divergences". Printed (cells 20, 29): 0.198 s, r̂ 1.750, **two** chains at −6557.9, 78 divergences. These are the numbers I saw in round 1.
- **Cell 30 / record fig2g:** OFF 1.331 s (0.844–1.894); log-k 1.369 and 1.336. Printed: 1.337 (0.849–1.916); 1.371 and 1.349.
- **Cell 33 / record fig2c:** 0.656, 4.231, 164.8; without pinches 0.653, 4.165, 164.5; r̂ 1.004 and 1.006. Printed (cell 32): 0.655, 4.239, 164.601; 0.654, 4.161, 164.782; r̂ 1.004 and 1.002.
- **Cell 36 / record fig2h:** 5.08 (dse 3.56) and 2.64 (dse 3.54); log-k gap 0.16. Printed: 5.09 (3.58), **2.85** (3.53), 0.11.
- **Cell 39 / record fig2d:** k 2.731, τ 4.450 (3.230–5.653); log-k 2.873 / 4.404 and 2.861 / 4.779. Printed (cell 38): 2.729, 4.401 (3.185–5.570); 2.882 / 4.394 and 2.872 / 4.746.
- **Cells 46, 48, 50, 54 and 56:** each misstates printed values in the third digit:
  - Cell 46: −1.533 / −1.692 / −0.636 printed as −1.535 / −1.689 / −0.635.
  - Cell 48: −0.251 / 0.072 printed as −0.250 / 0.073.
  - Cell 50: 224.7 / 19.3 printed as 224.472 / 19.350.
  - Cell 54: heat k 1.742 (1.431–2.047), τ_pre 1.305 / 1.279, "r_hat at most 1.008". Printed: 1.747 (1.436–2.072), 1.309 / 1.277, max 1.005.
  - Cell 56: 8.704 / 11.686 / 8.693 / 11.717 printed as 8.708 / 11.689 / 8.691 / 11.716.

  The record's `measured` values for fig2g, fig2c, fig2d, figs1-*, recovery-timing and tables3 carry the same unprinted values.

**gp.ipynb**

- **Record fig5b-train-no-difference:** "every variant but the two above finds a difference". The 2500-iteration run with blocks by animal gives Bonferroni 0.075 and KW 0.058, which is no difference (gp cell 13).

**ongoing.ipynb**

- **Record fig3d:** "highest low-frequency peak is at 2486 s, the record length". NEUTRAL records are 960 s and 1800–3368 s (ongoing cell 3). 2486 s is a frequency-grid bin, not a record length.

**README**

- The runtimes (about 27, 27, 27 and 35 min) do not match the printed 22.3, 20.1, 22.3 and 28.9 min.

**Everything else checks out.** The other Result sentences and notes, and the ongoing and gp/gp_methods Summaries, match the outputs.

**Round-1 reasons:** the record states them in my wording, nearly verbatim, with correct agree flags. The "reviewed" text correctly says I disagreed on five claims.

### 3. Round-1 points

**Resolved:**

- **B1:** for the OFF sigmoid fits, via the MAP start.
- **B2, B3:** every model is now on both trial sets. The no-pinch ELPDs match the paper's within 0.3.
- **B5:** the code's null line is printed and the same-likelihood null is run as a variant.
- **B6, B9, B10, B11, B12:** resolved.
- **B7, B8:** passed to a reader; still open as claims-file issues.
- **Section C:** the heart-rate spectrum (cleaned beats, bootstrap) and a per-cell comparison with the stored GP fits now exist.

**Remaining, bearing on a conclusion:**

1. **OFF_erf_linear_np is unconverged** (r̂ 1.393, ESS 9). The without-pinch tables9 reading rests on it. The outcome does not change, since the with-pinch reading alone fails, but the text and finding must be corrected.
2. **The evoked Result cells and the record's model numbers do not come from the delivered execution.** The default-start description is wrong in substance (two chains, 78 divergences, r̂ 1.75, t_switch 0.198 s). Fit results therefore vary between runs at fixed seeds, and the record should quote the delivered outputs.
3. **fig5b-train-no-difference (not reproduced) depends on the NEUTRAL inputs.**
   - The paper's stored NEUTRAL medians (train 0.0281) are closer to the code's 1500 s segments (0.0303, KW p 0.098 against the paper's 0.117) than to the criterion's whole-recording reading (0.0216).
   - The cell-by-cell match was made only against the segment fits. A match of the stored NEUTRAL rows against the whole-recording fits would show which input the paper used.
   - If it was the segments, the claims file's main reading does not produce the reported result. Its own rule ("except where the Methods' value cannot produce the reported result") would then apply. I report this as a possible claims-file issue; I have not corrected it.
4. **The GP main reading (200 / 0.001 / 10000 iterations) was run only to 2500 iterations.** ON outputscale is still rising (17.9 → 22.5 between 1250 and 2500; 22.7 → 32.1 under the code's settings). The latent-variance order holds at every snapshot.
5. **fig5b-test-r2 rests on the code's null contamination range.** Under the criterion's "same likelihood" it would be partially reproduced (NEUTRAL p 0.052).
