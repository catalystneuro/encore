I've answered every point in the round-1 report and re-run the entry. `python tools/entry.py all` passes (0 errors, 23 min run), and round 1 is recorded under `verifications` in the attempt record. Nothing is committed.

**Outcome changes.** All three are the verifier's own outcomes, so it agrees with every outcome in the record now:
- `figs3-1-l4-nh-tuning`: not_reproduced → partially_reproduced. Every part holds except the 0-75 µm eBW absence test (p = 0.036). That test fails because the L2/3 eBW fraction is too high.
- `fig5eh-l23-correlation-gradient-at-edge`: reproduced → partially_reproduced. I added a test of the outside-minus-inside gradient. Signal is steeper in EN (p = 0.0002 / 0.0013); noise is not (p = 0.96 / 0.81).
- `figs5-1-row-and-arc-boundaries`: not_reproduced → partially_reproduced. Three of the four tests hold.

Totals are now 13 reproduced, 15 partially reproduced, 5 not reproduced, 1 blocked.

**Corrections.**
- **L4 neuropil rebuild.** Filtering the ROI and neuropil traces first and then subtracting (the descriptor's order) reproduces the stored L4 dF/F to within 0.012. The old subtract-first order missed by 0.21 to 0.60. Blank trials are now matched one to one at each field's own weight.
- **New data finding.** The blank mismatch of up to 2.29 came from three L4 fields where `sponTrace` starts 0.5 s after the blank onset. Every other field starts 0.5 s before. Their blank trials are now cut from the stored dF/F, and it is recorded as a `format_error`.
- **figs5-2.** The L4 response is now lower in EN at every weight. The across-column signal effect is lost at r = 0.7, as the paper says (p = 0.084). The claim stays not reproduced: the L2/3 tuning direction and the within-column noise effect at 0.7 still fail.
- **Random numbers shifted.** The blank-trial fix changed the random stream, so every p-value from the Methods' responsiveness test moved slightly. All conclusions, notes and measured values now match the new run. One consequence: `fig4b` now holds only with the stored p-values (Methods' CW test p = 0.056, was 0.048), so three outcomes rest on that variant.
- **Counting bug.** The "values within tolerance" count in fig4ae and the across-row claim combined true/false values as an OR, not a sum. With it fixed, fig4ae has 7 of 8 values within tolerance in the main reading. No outcome changed.
- **Decoder fit.** It now uses every training trial in each split; the numbers change only in the fourth decimal.

**Outputs the verifier asked for.**
- The total ROIs in C1-C3 (156 NH, 359 EN).
- Per-bin n, mean, SEM and p for fig2a.
- Robust slopes and a scatter for figs4-1. Theil-Sen gives EN 0.131 against NH 0.037, so the reversed slope is not caused by outliers.
- Leave-one-mouse-out barrel radii for figs2-2.
- An exploratory eBW cell. It prints the eBW counts per ROI and a one-sided test, which brings NH only to 87.5%. Requiring each eBW to be a responsive whisker gives 72.9 to 75.0%, near the paper's 67%. Even then EN L2/3 is not more CW-tuned (p = 0.84), so fig3a stays not reproduced. That reading is not in the paper and decides no outcome; I added it to the question for the paper's authors (the `methods_unavailable` finding).

**Question for a reader.** The verifier thinks the claims file misreads the fig4c spontaneous-activity measure; that is now in `questions/crcns-ssc-10.yaml`, and the claim is unchanged.

**Not done.**
- No test on "blank-normalised responses" for eBW: rescaling an ROI's trials by its blank mean and SD leaves that test's result unchanged.
- The fig2b map geometry and the pseudo-replication in the decoders are stated in the notes, not changed. The verifier found neither affects an outcome, and the criteria allow the current choices.
