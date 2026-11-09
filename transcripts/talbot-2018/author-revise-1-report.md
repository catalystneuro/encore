I've revised the attempt for every point in the round-1 report. `python tools/entry.py all entries/crcns-hc-16-talbot-2018` passes the check with 0 errors, the notebook runs in 79 s, and two consecutive runs give identical outputs. Nothing is committed.

**Outcomes changed (three, all where the verifier disagreed)**
- **unit-and-cell-counts:** not reproduced → blocked (data missing). The data set has 15 of the paper's 21 mice, so its counts cannot test the paper's.
- **interneuron-proportion:** not reproduced → partially reproduced. Fmr1-null has the larger share of interneurons under every reading, but the percentages are far from the paper's.
- **fig5b-frame-specific-ipos:** reproduced (resting on an assumption) → partially reproduced. The room-frame difference is significant only when cells are classified in the same-day stationary session (p = 0.012), and that result depends on one mouse: leaving out M37 gives p = 0.13. With the other classification p = 0.25. The outcome no longer depends on choosing between the two.
- **locomotion-similar** stays reproduced, now marked as resting on an assumption: that the large box and stationary arena recordings are pooled. Within each environment the genotype × half interaction is significant, in opposite directions. I added a question for the paper's authors on which recordings Figure S5B uses.

**Added or corrected**
- **Pass rule (problem 1):**
  - The reading "expected count at least mean rate × 5 s" now runs as a variant for both overdispersion claims and both covariance claims. Under it, overdispersion-passes meets its criterion in R2 (variances 5.28 and 4.66, both within tolerance; F and Levene p < 0.001).
  - The outcome stays on the claims file's literal rule. The question is in the new file `questions/crcns-hc-16.yaml` for a reader. The other three pass claims keep their outcomes under either rule.
- **Isolation (problem 2):** a full TS header is printed; it holds no isolation measure and no scale in cm. A refractory filter (at most 0.5% of intervals below 2 ms) runs as a proxy and removes 70 of 774 clusters. It removes the firing-rate effect in figs3 and makes the interneuron difference non-significant in R1 (p = 0.092). It changes no outcome.
- **Spatial scale (problem 3):** the single-cell measures and classes also run on the code's 32 × 32 grid, which needs no scale. 45 clusters change class and no outcome changes.
- **Other points:**
  - The low-speed mask now requires low speed across the whole bin.
  - The Ipos 10-visit minimum now counts position samples, as the code does.
  - A code cell shows why figs4 is blocked.
  - The split-file mismatch is explained: one position sample at the split is in neither part, and it holds the missing spike.
  - The Kendall place-cell result is the same without M16.
  - Per-cell Ipos values are printed.
- Round 1 is recorded under `verifications`, with the verifier's reasons and my responses. The notebook, README and summary match the new numbers.

**Not changed, with the disagreement recorded**
- **figs4-remapping-similar:** I kept the block reason as data missing; the verifier gave "metadata insufficient". The paper's comparison fits small-box sessions recorded on arena days (Table S2), and those are not in the data set.
- **Tukey test in figs6 (problem 9):** left as it is. The paired t-test variant that accounts for repeated measures is already shown and gives the same pattern.
- **Claims file:** I changed no claim.
