I've worked through every point in the round-1 report and re-run the entry. `python tools/entry.py all` passes: the notebook runs in 312 s and the checks report 0 errors. Every conclusion in the notebook, README and record matches the new outputs.

**Outcome changes (round 2 will review these):**

| Claim | Before | Now | Verifier |
|---|---|---|---|
| fig5a-trains-stronger | partially_reproduced | not_reproduced | not_reproduced |
| fig5a-packet-center-enhanced | not_reproduced | not_reproduced | not_reproduced |
| fig5b-rotation-center-peak | reproduced (assumed) | not_reproduced | not_reproduced |
| fig5c-normalized-contrast | reproduced (assumed) | blocked, methods_underspecified | not_reproduced |
| 11 Fig. 6–9 claims | blocked, other | blocked, data_missing | data_missing |

- **fig5a-trains:** at the e3 end the trains never exceed the packets (p = 0.27 to 0.86). That holds under every reading and every ROI shape tried, and the criterion needs all three places.
- **fig5b:** I dropped the two assumptions that had picked the LOESS centre and the unpaired test, because the criterion asks for every reading. No ROI shape gives both comparisons under every reading. With wider ROIs all unpaired tests hold, but the paired test on the rotated trains still gives p up to 0.09. Every difference points the way the paper says.
- **fig5c:** I disagree with the verifier's not_reproduced, and recorded why. Once the verifier's requested ROIs were run under every reading, the result turned on ROI width. With ROIs 3 steps wide the test holds under all 32 readings. With 1 step it fails in 5 of 32 (p = 0.051 to 0.082). The paper fixes the ROI length along the diagonal (about 65 µm) but not its width, so I blocked the claim as methods_underspecified. The width question is in the findings for the paper's authors.

**Added or corrected:**
- **ROI shape (points 2 and 4):** ROIs are now one step long, lie along the diagonal, and are 1, 3 or 5 steps wide. The outer end sits either at the edge of the electrode footprint seen in the image, or at a fixed distance worked out from the 1.5-mm needles, which does not depend on intensity. That gives six shapes, and every claim now runs under all readings in each. Because the main ROIs changed shape, the main numbers moved; for example the e1-end p-value for fig5a went from 0.059 to 0.083.
- **Trough bias (point 3):** added a variant that finds each dish's trough from the other dishes' mean. It changes no outcome.
- **dish2 (section C):** added full-resolution crops of the centre of each rotated-packet dish. In dish2, bright pixels cover 44.6% of the centre ROI, against 1.4 to 8.2% in the other four dishes. By eye they look like clusters of labelled cells, but the measure cannot rule out debris.
- **Per-dish values:** printed at widths 1, 3 and 5. The notebook now says why no paired test applies to trains against packets: they are different dishes.
- **Labels (points 5 and 6):** O2(b) is now named as the joined e1 and e2 end, and the O3(b) test is labelled as an assumption.
- **Record:** findings updated with the new numbers, and the round entered under `verifications`.

**Not done:**
- No new reader question: the verifier found no place where the claims file misreads the paper. The existing question about Figs. 6–9 stays.
- I did not open dandisets 000875, 001025, 001027 or 001028; under the claims file they are out of scope.
- Nothing is committed or pushed, as instructed.
