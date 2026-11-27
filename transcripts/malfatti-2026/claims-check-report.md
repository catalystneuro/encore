I checked `claims/malfatti-2026.yaml` against the paper, made eight corrections, added two claims, and marked it ready (`ready: true`). Nothing is committed or pushed.

**Checker result:** `34 claims, 34 quotes, 71 statistical values, 41 problems`

All 41 are "value not found" notices, and none is a real error. The paper prints its p-values in scientific notation (for example 1.6e-02 for 0.016), in Supplemental Tables 1 to 6 and the supplement's figure text. I found each one by reading and they all match. All quotes pass.

**Changes, by claim**
- **supfig2i-baseline-lower:** the file said the p-value in Supplemental Figure 2I could not be assigned. The extracted text shows a single p = 1.2e-06 for that panel, so I recorded it, noting that the paper does not name the test.
- **supfig2j-phase-amplitudes:** one of its statistics comes from the Supplemental Figure 2 text, which the source did not cite. Source corrected.
- **New claim, supfig2j-control-training-decrease:** in control mice, activity on successful prehensions fell with training (p = 5.5e-03), and this was not seen in Cre+ mice. It is a reported finding that had no claim.
- **New claim, supfig2j-creplus-naive-failed:** in Cre+ mice in session 1, activity during failed prehensions was lower than before them (Wilcoxon, p = 6.5e-03). Also a reported finding with no claim.
- **fig2d-latency-accuracy:** the quote and its two exceptions come from the Supplemental Figure 5 text, not the main Results. Source corrected, and I added the session 2 accuracy by genotype interaction reported in that text.
- **fig3l-resilience:** the code's resilience formula can fall below 0 or above 1, while the Methods say it lies between 0 and 1. I named the conflict, kept the code's formula as the main reading, and added intersection over union as a variant.
- **fig4b-clz-improves-success:** the treatment tests' degrees of freedom do not fit a test across 5 and 6 mice. I named two readings: per-mouse means, or each mouse-session value counted as independent.
- **fig4d-theta-genotype:** I removed the reading that used sessions 8 to 13. Every session term in Supplemental Table 6 has 2 degrees of freedom, which means three sessions (11 to 13). I also noted that the genotype tests around prehensions imply 10 mice, against 11 outside prehensions.
- **supfig7-lfp-nonprehension:** I named the seven bands the figure plots. The Results say the interaction holds "across all frequency bands" but also that high theta showed no effects; that conflict is now stated in the criterion.

**Still open (recorded under `checks`)**
- Equation 1 (resilience) cannot be read from the extracted text, so the criterion relies on the code.
- Supplemental Tables 1M to 1P are missing from the supplement, so fig5d-pasta-drops and fig5i-ablation-prehension have no statistics.
- The paper gives conflicting group sizes: 11 or 13 mice for the LFP group, and 6 controls and 3 Cre+ or 8 and 6 for the ablation prehension task.

**Ready:** yes. Main findings are covered, every claim comes from this paper, and the code details I spot-checked match the cited commit (86efdf1).
