## Check of DANDI:001687 claims (doi:10.1016/j.neuron.2026.05.027)

**Checker result:** `41 claims, 41 quotes, 40 statistical values, 0 problems`. Before my edits it also had 0 problems, with 39 statistical values.

I read the main text, the Methods, the legends and the supplement. I also cloned the paper's code at commit b1a9f3c to check the details the file cites. The classification, decoder settings, whisker-cutting tests, Fig. 5D masks and test direction, model defaults and the Poly2 probe filter all match what the file says. Nothing is committed, and only `claims/001687/` was changed.

**Changes, by claim**
- **Opening comment, figs2-tungsten-responsiveness, fig2-wall-responsive-counts, fig2-distance-tuned-counts, telc-unit-yield:** The Methods test responsiveness at uncorrected p < 0.05, while the code applies a BH-FDR correction across distances. The file had made the code the main reading. The protocol puts the Methods first, so claims are now judged on the uncorrected test, and the code's result is shown as a variant. Every claim that classifies units by the opening comment follows this.
- **fig2f-tuning-categories:** Added that the Methods count 112 units as wall-responsive but not tuned. This supports reading (b).
- **figs1f-angle-awake-vs-anesthetized:** The code computes the midpoint angle by heavy smoothing (its envelope method is commented out). That is now named as a variant of the Methods' envelope midpoint.
- **figs1d-bending-larger-closer:** Noted that the cited panels show one example whisker in one mouse, and that the criterion uses the across-mouse panels S1F and S1J.
- **fig3a-decoding-above-controls:** Changed the rank-sum test from one-sided to two-sided. The code uses MATLAB's two-sided default, and Table S2's p = 1.83e-4 is exactly the two-sided value when 10 subsamples are fully separated from 10.
- **figs5c-single-neuron-decoders:** Added the 11 mm test (p = 0.02). The criterion requires it, but it was not recorded.
- **figs5fg-cut-decoding:** The criterion compared a drop summed over seven distances with one summed over two, which favours the far range by construction. It now compares mean drops per distance and requires the largest drop to be at 11 mm or farther.
- **figs6-opto-local-inhibition-gain:** Removed an invented threshold (12 of 16 units keeping their preferred distance). The readings are now "all of them" and "more than half". The paper does not say which passes the tuning is classified on (laser-off or all), so that is now named as open.
- **figs6l-telc-increase-at-close-distances:** The 7 mm tolerance was 2.68. By the criterion's own rule (the larger half of the confidence interval) it is 2.71.
- **fig4-cut-baseline-unchanged:** Noted that the code's per-unit baseline is the mean of the per-distance means.

**What remains open**
- Figure 2F's counts (119 suppressed-only, 177 untuned) cannot be reconciled with the 656 tuned units given in the text. Both readings stay in the claim.
- A few minor descriptive findings have no claim: the Figure S4M shifts in preferred distance across time windows, the SVM error values in Table S3, and the receptive-field split of the tungsten units. I judged none of them a main finding.
- Tables S1 and S6 are named in the paper but are not in the supplement that was read. Test details that may be in S6 stay open.

**Ready:** yes. The `checks` entry records `ready: true`.
