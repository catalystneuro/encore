**Verifier report, round 2: Robotka et al. 2023 on CRCNS aa-5 (attempt robotka-2023-01)**

The claims file has 30 claims, and the attempt record has 30 outcomes: 14 reproduced, 2 partially reproduced, 1 not reproduced and 13 blocked. Five outcomes are marked `assumed: true`: fig3c-peak-call-types, fig4b-ensemble-20, fig4b-top-ensembles, fig5e-volume and fig5-multiple-regression.

### 1. Outcomes and assumptions

I agree with all 30 stated outcomes. Three of them changed since round 1:

- **good-units-100 (not_reproduced).** I now agree, and withdraw my round-1 partially_reproduced. The criterion takes the count from one run and has no partial outcome when the total is outside tolerance. That run gives 89 under the code reading and 77 under the Methods reading (cell 37), both outside 90–110. The outcome depends on the seed: 8 of the 10 other seeds land in tolerance. ZF6M has 8–14 good units in every run, never within 16 ± 1.6.
- **fig5e-volume and fig5-multiple-regression (reproduced, assumed).** Both now match my round-1 outcome.

The blocked outcomes and their `blocked_by` reasons are right:

- figs4 is blocked as other. ZF6M has 10 good units, below the 16 the test needs.
- The area claims are blocked as metadata_insufficient.
- The acoustic claims are blocked as data_missing.
- The aa-4 claims are blocked as other.

The five assumptions are stated, with the other readings shown and the reason given:

- **fig3c, the code's zCT.** Reasonable: it is what Figure 3C plots. Under the Methods' zCT, So ranks first (cell 30), so the claim would not be reproduced.
- **fig4b-ensemble-20 and fig4b-top-ensembles, the code's cross-validation.** Stated and defensible: the paper's printed values match the code's scheme and not the Methods'. The record now says plainly that this scheme credits responses specific to one exemplar: 78.2% against 9.8% on synthetic data (cell 43). Under the Methods' scheme the claims are partially reproduced (32.0 / 24.1) and not reproduced (33.96).
- **fig5e, the code's sound window and eigh axes.** Stated, and fragile. R2adj is in tolerance only for the code window with eigh axes (0.0938, cell 62). The eigh axes are the smallest eigenvalues of a non-symmetric matrix. With the Methods' window and the largest-eigenvalue axes R2adj is 0.120, and the outcome would be partially_reproduced.
- **fig5-multiple-regression, the eigh axes.** Stated. With the largest-eigenvalue axes R2adj is 0.2515 or 0.2481 (cell 74), just outside tolerance.

fig5g needs no assumption, because the Methods' ES (reading b) holds under both cross-validations. But that outcome rests on a claims-file reading I still question (point 3 below).

### 2. Conclusions, Summary, README and record notes against the outputs

Almost every number checks against the printed outputs: cells 8–78, the Summary (cell 79), the README table and the record notes. The exceptions:

- **KDE_BW finding** (record `metadata_error` finding; Summary, cell 79; pcs-variance notes). "its values range from 0.2 to 10, which can only be milliseconds." Cell 5 prints only the first five values, [0.2, 3.0, 5.0, 5.2, 5.4], so the range 0.2–10 is not printed (10.0 appears only in the descriptor's example). Nothing printed shows the values must be milliseconds. The descriptor says this convolution gives a "coarse" rate used to cut out motion-artefact epochs, for which bandwidths of 0.2–10 s are plausible. This finding is not supported.
- **README.** "the whole notebook ran in 47 minutes". Cell 74 prints a total run time of 37.7 min and cell 77 adds 3.7 min of clustering, about 41.5 min in all.
- **fig5-multiple-regression notes.** "The Methods' SI changes R2adj by less than 0.002." This holds under the code's cross-validation (at most 0.0009, cell 74). Under the Methods' cross-validation the change reaches 0.0025 (0.4841 against 0.4866).
- **fig4b-top-ensembles.** The criterion takes the best ensemble "among the Figure 4B ensembles of 20". The best is now taken from the 1,800 Figure 5 ensembles (cell 59). The notes say so, but it is not listed as a deviation. It does not change the verdict: 68.4 ≥ 55.
- **Summary, fig6c row.** It reports only the code reading's units (median 10, outside 9 ± 0.9). The Methods reading's units, the main reading under the claims file, give mean 10.16 and median 9, both within tolerance (cell 77). The record notes give both.
- **Cosmetic.** Cells 31, 39, 44, 47, 50, 54, 63, 66, 69, 72 and 75 end with a stray closing `**`.

**Round-1 reasons in the record.** They state my round-1 reasons accurately and in my words, nearly verbatim from my table, with the matching problem points attached to each claim. The `agrees: false` entries (good-units-100, fig5e, fig5-multiple-regression) and the outcome I gave for each are recorded correctly.

**Claims-file points (reported, not corrected):**

- **C11 ES reading (b).** The Methods' ES formula gives negative values here (−0.18 to −0.07), against the Figure 5G legend's range of 0 to 1. The claims file used the same range argument to rule out C2(a) for SI. ES (b) also falls as single-unit PCC rises, so a negative slope is close to built in. The author has passed this to a reader.
- **C12.** The claims file says the code cuts the tree between the smallest and largest linkage distance. The author reports that the code takes the minimum and maximum over the whole linkage matrix, including its index and count columns. I cannot check this without the code. If the author is right, the claims file misreads the code. One consequence: the helper's thresholds can never yield 1 cluster (minimum 2–3, cell 77), while the paper's range starts at 1. The claim is blocked, so no outcome changes.

### 3. Round-1 points

**Resolved:**

- **B1 (cross-validation leakage).** Stated as an assumption, shown on synthetic data, and put to the authors as a question.
- **B2 (good-unit count).** Per-bird counts are now printed for every seed and for the listed units.
- **B4 (best ensemble biased upward).** Now taken from 100-repetition decodings.
- **B5 (figs4 variant).** The variant on the paper's listed units has been run (p = 0.696 and 0.796), and the message has been corrected.
- **B6 (fig6c call-type half).** Now computed.
- **B7 (fig5 code variants).** Now marked as assumptions.
- **B8 (Methods unit rule).** The 125-unit variant is in tolerance.
- **B9 (KDE kernel).** The stored KDE matches a 30 ms kernel (107 of 114 rows above r = 0.99). The test for spikeless stimuli is fixed, and the PCA is unchanged.
- **B10 (MRF scaling).** The code's `stdz = np.std(allz)` is printed, though the print does not show which units `allz` covers.
- **B11 (cell 11).** Fixed.
- **C items.** The code lines for ES normalisation, eigh, the PCC > 30 filter and n0 = n1 = 2 are now printed. The record states that no deposit exists for the vocalization database.

**Still open, bearing on a conclusion:**

- **B3 / C11, fig5g.** The outcome holds only under the Methods' ES (b). That reading's support from the paper is doubtful, and under the code's ES (a) with the code's cross-validation the slope is +18.9, p = 0.79. A reader's answer could reverse this outcome.
- **fig5e and fig5-multiple-regression.** Both rest on the code's eigh axes, and fig5e also on the code's sound window. Without them the outcomes are partially_reproduced (0.120; 0.248–0.252).
- **good-units-100.** The outcome follows the criterion but depends on the seed: 8 of 10 other seeds fall in tolerance.
