I've worked through every point in the verifier's round-1 report and re-run the entry. `python tools/entry.py all entries/002020-nakamuta-2025` passes: 0 errors, notebook run in 362 s. Nothing is committed.

**Outcome changes**
- **fig2c-locality-spectrum:** reproduced (assumed) → blocked, `methods_underspecified`. Only the M2/L1 reading of the locality measure holds; M1 and L2 fail (12 of 56 readings hold). The claims file says to block when readings disagree, which is what the verifier advised.
- **fig2b-spatial-structure** (was not_reproduced), **fig2d-locality-slope** (was partially reproduced) and **fig2d-shuffle-locality** (was partially reproduced) → all blocked, `methods_underspecified`. Each depends on fig2c, and the protocol blocks a claim whose dependency is blocked. The verifier would give partially_reproduced, not_reproduced and partially_reproduced; I recorded those disagreements in the record.
- **fig1e-example-dish, fig1f-transition-15div, fig1f-exponent-1p2:** still blocked, but the main reason is now `methods_underspecified`, as the verifier gave. The missing days in vitro (DIV) stay in the notes.
- Everything else is unchanged: 2 reproduced (assumed), 2 not_reproduced, the rest blocked.

**Added or corrected**
- **Question for a reader**, in a new `questions/002020.yaml`, on the claims file's reading of the fit: x as the PC rank cannot produce b on the paper's 0.1 scale.
  - An uncorrelated Poisson null at the recorded rates gives the same b as the data.
  - b ≥ 0.1 would need λ1/λ100 of about 19,930; the largest here is 5,503.
  - New finding: fitting rank as a function of variance, the axes the Figure 1D legend describes, gives b ≥ 0.1 in 0.86 of early recordings and 0.20 from 15 DIV. It is shown only as a variant; the claim stays as the claims file has it.
- **New outputs the verifier asked for:**
  - the NWB description fields; they say "Days in vitro are unknown".
  - eigenvalue ratios, and the share of b values at the bound 0 for each reading.
  - fig3c complete: both shift readings, both selections, every dish kept, and dishes that never shift counted as latest. None of the 56 readings meets the criterion.
  - fig1e exponent readings (b) and (c), and figs1 reading (b).
  - d0 = 4 and 5, plus two per-dish readings anchored on each dish's first active recording. fig1b still holds under all of them and fails only at d0 = 1.
  - for fig2b, ties broken toward the later recording too; for fig2c, locality as a share of electrodes.
  - for the time scales, an interpolated variant, tie shares and percentiles. no-temporal-structure is still not reproduced.
  - for fig3d, correlations without the values at the bound. They are positive and significant only under S1 F1. This is a variant, so the outcome is unchanged.
- **Helper fixes:** the F2 fit now keeps zero-count cascade sizes, firing rates exclude spikes after 1,800 s, and the unused `fit_power` is now used.
- **Corrected an error from round 1:** the text said five dishes are active on their first recording. The outputs show four (19880 and 23302 start on day 2, 23317 on day 1).
- Round 1 is recorded under `verifications`, with the verifier's reasons and my responses. The README, header and summary are updated.

**Not done**
- I did not change fig1d-power-law-emerges to not_reproduced, although the verifier pointed out that the claims file's rule would allow it. The verifier itself kept the claim blocked, and the question to a reader may change the fit.
- The two model claims are still not run, because the model is not specified.
