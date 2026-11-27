I've checked `claims/gable-2026.yaml` against the paper and corrected ten claims. I think the file is ready for an attempt, and I've recorded `ready: true` in the new `checks` entry.

**Checker result** (the same before and after my edits): `claims/gable-2026.yaml: 34 claims, 33 quotes, 52 statistical values, 0 problems`

**Changes, by claim**
- **figs4-high-couplers-correlated:** the statement no longer says the difference grows with coupling. No sentence in the paper says that, and the criterion did not judge it. The Table 5 values are still in the statement.
- **fig2j-tsa-dendrite-specific:** I removed the reading of "at least 5× larger" as an increase over a pre-spike baseline, because the paper never defines such a baseline. The ratio is now the spiking-dendrite mean over the other-dendrite mean, in both windows.
- **Three claims whose criteria did not test part of their statement.** Each criterion now does, using the paper's own test:
  - **fig2n-abrupt-input-dendrite-specific:** the "no pre/post difference" clause (Table 1, p = 0.75).
  - **fig3f-sc-most-active-at-spike:** the "NC and WC do not differ" clause (Table 6, p = 0.7).
  - **fig4h-outcome-nc:** the "WC exceeds SC" clause (Table 7).
- **Values printed with one significant figure.** For these the file elsewhere uses the rounding interval of the printed digit, so I applied the same rule here:
  - **fig5b-spike-go-mode-sc-wc:** the tolerance on 0.002 goes from 0.0002 to 0.0005.
  - **fig5d-spike-outcome-nc:** both tolerances on 0.001 go from 0.0001 to 0.0005, and I added the −50 to 150 ms window to the quantities.
  - **figs1c-tuft-spikes-rare:** the tolerance on the "≈0.01 Hz" rate goes from 0.001 to 0.005.
- **figs1c-tuft-spikes-rare** and **fig2c-dendrite-correlation-bimodal:** the ratio range of 50 to 200, the use of medians, and the antimode range of 0.3 to 0.5 come from the previous author, not the paper. The criteria now say so.
- **figs2ab-correlation-declines-with-distance:** I reworded "fitted decay is negative", which could be read either way, as "the fit decreases with distance".
- **Figure S4 method (no change):** I checked it against the paper's code at commit 688e662. It matches: the 7 percentile bins, independent session resampling with the acceptance rule, one-tailed tests and Holm correction. The code also shows that the 6,586 different-range pairs in Table 5 are summed over the 7 bins.

**What remains open**
- The paper names the Holm correction families for Tables 1 and 6 by measure. It doesn't say whether the male and female rows belong to those families. This affects table1-both-sexes and fig3f-sc-most-active-at-spike.
- The paper's remark that the Table 6 result showed "no indication that this observation was sex specific" has no claim of its own. It is a minor point.

The file is otherwise complete: every main finding has a claim, and every claim comes from this paper. Only `claims/gable-2026.yaml` was changed, and nothing has been committed or pushed.
