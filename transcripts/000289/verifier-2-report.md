# Round 2 verification: Kutschireiter et al. 2023 with DANDI:000289

I agree with all 13 outcomes. The notebook's printed outputs support every number in the conclusions, the summary, the README and the record's notes, except four sentences: one swapped pair of ratios, one value that is never printed, one unproven independence claim, and one wrong description of the noise diagnostic. The record states my round-1 reasons faithfully. One new point bears on the noise claim's explanation, but not on its outcome.

## 1. Outcomes and assumptions

The claims file and the attempt record each have 13 claims and 13 outcomes, with matching ids. Notebook cell numbers have shifted by about one since round 1.

| Claim | Record | Agree? |
|---|---|---|
| fig1-conflict-decreases-certainty | reproduced | Yes (cell 13: 6 of 6 under (a) and (b)) |
| fig2h-bump-tracks-circkf | reproduced | Yes (cell 16) |
| fig2i-accuracy-and-certainty-vs-reliability | reproduced | Yes (cell 19) |
| fig3b-bayesian-beats-conventional | reproduced | Yes (cell 22) |
| fig3c-update-weights | reproduced | Yes (cell 25) |
| fig3d-best-network-slow-decay | partially_reproduced | Yes. Condition 4 fails as written (cell 28). |
| fig3f-noise-drop-below-70 | reproduced | Yes (cell 31) |
| fig3f-retuning-reduces-drop | reproduced, measured 34.64 | Yes. 3 of 6 readings fall in 31.5 to 38.5%, and the SNR ratio is 1.05 to 3.00 (cell 34). |
| noise-effects-on-mu-and-kappa | partially_reproduced | Yes, as the criterion is written. Condition (2) fails in all 4 settings (cell 37). |
| fig4b-connectome-motifs | partially_reproduced, assumed | Yes. The criterion needs two sorts and only reading (a) can be formed (cells 6 and 40). |
| fig4gh-drosophila-network-matches | partially_reproduced | Yes. Reading (a) fails at 0.1, 0.2 and 0.3/s (cell 43). |
| figs2-performance-independent-of-n | not_reproduced | Yes. N = 16 at 0.1/s is 0.0414 off, both readings fail (cell 46). |
| prediction-bump-amplitude-cue-reliability | blocked (methods_underspecified) | Yes. dF/F with reading (b) gives p = 0.138; the other three combinations hold (cell 50). |

**Assumptions.** Only fig4b is marked `assumed: true`. Both of its assumptions are stated in the deviations and are reasonable:
- **Any synapse counts as a connection.** This is the legend's "total number of synaptic connections". The 3- and 5-synapse counts are shown alongside.
- **Offset measure.** The offset is the synapse-weighted circular mean of EPG targets minus that of EPG inputs (period 8 glomeruli). The paper gives no measure.

The raw-signal choices for the prediction claim are also the author's own, and they are listed as deviations. They cannot change that outcome, because the dF/F readings already disagree.

**Places where the claims file misreads or over-tightens the paper** (reported, not corrected):
- **Noise claim, criterion (2).** It tests the drift on the full network. SI §5 (Eqs. S121–S124) derives only the noise term's own contribution to dκ ("if the drift is not accounted for"). This is my round-1 B1; the record forwards it to a question for a reader.
- **fig4b, reading (b).** The criterion offers an ellipsoid-body or gall sort "in the name" that hemibrain names cannot provide, then requires both sorts. So the partial outcome comes from how the criterion is written, not from the connectome.
- **figs2.** The paper says "mostly independent", but the criterion requires every one of the 161 cells to be within 0.02. The not_reproduced outcome rests on one cell.

## 2. Sentences the numbers do not support

**Cell 51.** "p = 0.021 with raw fluorescence but p = 0.138 with dF/F (median high/low ratio 1.12 and 1.11)". Read in order, this gives raw 1.12 and dF/F 1.11. Cell 50 prints dF/F 1.120 and raw 1.112, so the ratios are swapped. The record's notes have them the right way round.

**Cells 38 and 37, and the record (noise notes and the code_mismatch finding).** Three related sentences go beyond what the diagnostic shows:
- Cell 38 says the run holds the inhibition "so that the noise is only one more input to otherwise unchanged dynamics as in SI section 5".
- The `bra.rnn_batch` docstring says "the other dynamics are unchanged".
- The record says "the fall comes from the noise raising the rectified sum".

`inh_fixed` replaces the whole term `w_quad·π/N·Σmax(r,0)` with a constant. That term is the only one that depends on amplitude: it is the decay that pulls the bump back to κ* = 1. Holding it fixed turns the first mode neutral (1.5 − 1 − 0.5 = 0), leaving a free 2-D random walk. That is why the end amplitude matches the Rice mean.

So the control changes two things at once: it removes the noise's effect on the inhibition, and it removes the restoring force. It shows that the SI's noise term is correct. It does not show that the noise's effect on the inhibition is what outweighs the drift in the full network. The numbers themselves (1.08, 1.33, 1.01 and 1.07, each within 1.5 SE of the Rice means) are correct.

**Cell 52, Summary.** "The ROI masks are 5 to 9 pixels on the PB midline". No cell prints the mask sizes; the figure appears only in a `bra.py` docstring.

**Cell 28 comment and cell 29.** "each cell is its own scan" is used to compute the SE of a difference between two grid cells (0.0026), which gives the "0.32 and 0.52 SE, within sampling error" verdict. Nothing printed shows that the grid cells use independent trajectories. If the scan reuses trajectories, that SE is too large.

**Minor imprecisions:**
- **Cell 11.** "lag 0 or 5 frames (0 to 0.55 s)". Sub-10 peaks at lag 5 and is imaged at 7.87 Hz, which is 0.64 s.
- **README.** "Not reproduced (one value of 161)". There are 161 cells, but only 160 values: one is NaN (cell 46).
- **Record, figs2 notes.** "about 1.2 values … expected" leaves out that the expectation covers N ≥ 8 only. The notebook says so.

**Checked and supported.** Everything else in the conclusions, the summary, the README and the record's notes matches the printed outputs. That covers fig1, fig2h, fig2i, fig3b, fig3c, fig3d, both fig3f claims, fig4b, fig4gh, figs2 and the prediction claim's counts, p-values and variant ranges. It also covers the README's run time (6.9 min, cell 53) and the description of the data.

**My round-1 reasons in the record.** The `verifications` block gives each of my 13 round-1 outcomes and reasons faithfully, including the B-points and the things I could not check. It correctly marks fig4b and figs2 as `agrees: false` against the original record.

## 3. Round-1 points

**Resolved:**
- **B2, MC error for fig4gh and figs2.** The SE is now shown. figs2 is 4.3 SE off, so it is not noise. fig4gh's differences are 1.16 to 1.95 SE. Both outcomes rest on the criterion's bounds, and the record says so.
- **B3, fig3d rises.** Resolved, subject to the independence caveat above.
- **B4, fig4b threshold.** The outcome was changed to partial, and the threshold dependence is stated.
- **B5, raw-signal variants.** 18 variants were added; the split follows division by F0.
- **B6, bump decoder.** The phase sign is now stated, and the spectral peak is at frequency 2 in all 15 flies (cell 49).
- **B7, weak comparison (a) in fig1.** Stated.
- **B8, NaN cell.** Printed as N = 128 at 100/s.
- **B9, "No claim is blocked" in cell 0.** Corrected.
- **C, unchecked code details.** The kappa_z = γ_z comment, the stats columns and the axis order are settled by the printed source lines and the array shapes.

**Remaining:**
- **B1 / noise claim, partly resolved.** The diagnostic was added, but it does not isolate the cause (section 2). This bears on the explanation in the noise conclusion and the code_mismatch finding, not on the outcome, which follows the criterion. A cleaner control would keep the inhibition at the value implied by the decoded amplitude alone.
- **New, on the fig3d SE.** The independence of the grid cells is assumed, not shown. This affects only the "within sampling error" reading; condition 4 fails as written either way.
- **B10, not changed.** The retuned performance is still a maximum over noisy grid cells, which biases it upward; the reduction values (34.64%) depend on it. The record keeps it because the paper's notebook does the same, which is acceptable.
- **Claims-file points.** The three in section 1 (noise criterion (2), fig4b reading (b), figs2 "mostly") are for the claims file's authors.
