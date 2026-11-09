There was one question, on **fig2-60-fold-co-counter** (background reading), and I changed the claims file for it.

**Answer:** Reading (a), the ROI intensity with no correction, is not a reading the paper allows. Methods 4.4 says the footprints were measured "To account for 'spontaneous' YP uptake", so the values the paper reports are corrected for that uptake. The paper does not say how it corrected them, so the criteria now use subtraction of the same dish's mean footprint intensity, reading (b), because it is the standard correction for a measured background. Reading (a) stays in the file as a reported variant that decides no outcome.

**What changed in `claims/000631/`:**
- **Opening comment:** the background item now says the above.
- **Figure 2 claims:** I removed the rule that blocked a claim when readings (a) and (b) disagree from all five that carried it: fig2-180-cancellation, fig2-crossover-angle, fig2-facilitation-plateau, fig2-frequency-dependence and fig2-60-fold-co-counter.
- **Two claims the question did not name:** fig3-770khz-co-enhanced and fig4-unipolar-pattern had the same rule, and I changed them for the same reason.
- **Unchanged:** fig3-1hz-co-equals-cross and fig3-770khz-cross-same-as-1hz already let (b) decide. No expected values, tolerances, statements or quotes changed.

`python tools/claims_check.py` reports 12 claims, 12 quotes and 0 problems. The question is marked `answered: 2026-10-31`. Nothing is committed.
