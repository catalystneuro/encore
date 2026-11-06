I've revised the attempt after the round-1 verifier report. `python tools/entry.py all entries/crcns-ear-1-farrell-2020` passes with 0 errors and runs in 44 s, and every conclusion matches the numbers in the executed copy. Nothing is committed.

**Main change.** The verifier's main point (B1) was that one XE991 bin of two cells (mean ΔVmin 0.80 V; file 57 has CLW 0.48 pF) was kept for some claims and not for others. I now leave out bins and groups whose mean ΔVmin is not between 0 and 0.4 V, for every Eq. 3a fit and every group built on the Fig. 3a and S4 data. This is recorded as an assumption, taken from two passages of the paper: the Fig. S4 legend fits only ΔVmin < 0.4 V, and the Discussion treats V0.5 as independent of ΔVmin above 0.3 V. The notebook still shows the result with all bins kept, and with the limit applied to cells before binning. The limit removes no bin from the main Fig. 3a fit without XE991, so that result is unchanged.

**Outcome changes (now 23 reproduced, 7 partially reproduced, 11 not reproduced, 7 blocked):**
- **fig3a-xe991-fit:** not reproduced → reproduced. Vd 0.0505 V, R2 0.847, slope −0.377, R2 0.921, all within tolerance.
- **table3-pathway-energies:** partially reproduced → reproduced. All six values are within tolerance on the 5 pF groups.
- **low-chloride-similar:** not reproduced → partially reproduced. Two of the three cells meet all three conditions.
- **fig4d-cleq-two-limits:** reproduced → not reproduced. With the bin out, the lower limit is 0.6496 aF, outside the tolerance by 0.0006 aF. The verifier had agreed with reproduced but called it fragile; I changed it so the limit is applied the same way everywhere.
- **xe991-voltage-clamp, fig4a-vh-rises-vd-constant, capacitance-asymmetry:** partially reproduced → not reproduced. These are the verifier's outcomes: none of their criteria has a partial tier. The verifier's written tally doesn't match its own table; I followed the table.

**Added or corrected:**
- **fig3b:** the notebook now prints the per-bin table and every cell's dC, and runs the second CLn reading (at or below −0.15 V). The positive slope came from one cell whose dC of −5.0 pF made its CLWn negative (−0.95 pF). Without that bin the slope is negative (−0.40 for the first reading), but no reading gets both Vd and the slope within tolerance, so it stays not reproduced.
- **mean-slope-half:** the mean is now −0.407, still outside −0.48 ± 0.048. Across the 16 combinations of readings, 7 fall within tolerance, so I marked the outcome as resting on the choice of reading.
- **CLn check:** I added a table of capacitance over the first eight ramp points. It shows no settling effect raising the first two points; they sit below the next six in 80 of 89 cells.
- **Length gradient:** I ran the end-to-end gradient the verifier described as a variant. It gives 0.95 to 1.43 µm/mV, also outside 0.63 to 0.77, so the outcome doesn't change. The claims file doesn't list this reading, so I added it to `questions/crcns-ear-1.yaml` as a question for a reader, without changing the claim.
- **Smaller fixes:**
  - The data check no longer says the stored surface area has the same form as the one Corbitt uses.
  - The data check now shows the effect of the six cells with an estimated bundle capacitance (root 5.137 against 5.104 pF).
  - It also prints one cell's I-V steps and currents, which confirm conductances in the nS range.
  - The question for the paper's authors now also asks about the ΔVmin limit.
  - The attempt record has a round-1 entry under `verifications`, with the verifier's reasons and my responses.

**Not done:**
- I kept the degrees of freedom in the uncentred R2 of fig1-charge-not-linear and added a comment explaining them. The residual has n − 1, and a total taken about zero has n because no mean is estimated. That reading fails either way.
- Table S3's numbers and the Corbitt et al. (2012) rule still can't be checked here.
