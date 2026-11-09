The claims file is ready for an attempt. After my edits the checker reports: `claims/crcns-pfc-2/10.1038-nn.2134.yaml: 30 claims, 30 quotes, 1 statistical values, 0 problems`.

The statements, quotes, sources and expected values match the paper. Thresholds used to count units (P < 0.05, P < 0.01, P < 0.10) are correctly left out of `statistics`. The paper's main findings each have a claim, and nothing comes from outside the paper. The only data-descriptor content is the session ID EE.188, in the opening comment.

**Changes, by claim:**
- **central-arm-selectivity:** the statement now says "apparently indistinguishable", as the paper does. Head directions already diverge at 0.24 (Supplementary Figure 3B).
- **odor-unrelated-to-stem:** the statement covers the stem and the side arms (Supplementary Figure 6B legend), but the criterion tested the stem only. It now tests positions 0.5 to 1 as well.
- **retrospective-coding-rare:** the criterion assumed the Figure 2a sessions, which Supplementary Figures 7 and 8 don't name. It now gives two readings: those sessions, or all sessions.
- **fig3f-distance:** the criterion asked for a connection at 1,000 µm or more. The paper says connections reach 1,200 µm, so the largest shank separation with a connection must now be 1,200 µm.
- **fig3b-session-connections:** the criterion now notes that the paper doesn't explain how its 1172 pairs relate to the 13,572 matrix points (117 × 116), or how the roughly 1422 layer 5 pairs relate to 142 neurons.
- **thinning-preserves-dependence:** "at least two pairs" is now marked as our reading of the paper's "several", not the paper's number.
- **fig7-supralinear-coincidence:** the satellite count of 14 was an expected value, but the criterion only reported it. The criterion now requires it.
- **lifetime-width:** which neurons to use is now open, with two readings: the Figure 2a sessions, or all units.
- **population-vector-width:** notes that Supplementary Figure 2A doesn't name its sessions, with all sessions as a variant.

**Still open (recorded under `checks`):**
- The source "paragraph 4" for connection-counts, cell-type-fractions and pyr-pyr-connections may be one short; the extracted text reads it as the fifth. I couldn't render the PDF to check because neither PyMuPDF nor poppler is installed. The quotes still locate the passages.
- The Supplementary Note puts putative interneurons at about 37% of the recorded population. That doesn't match the 12.5% against 32.5% split (28% of classified units) or the 2.82 ratio. No claim covers it, since it is not a main finding.

Nothing is committed.
