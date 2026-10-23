The claims file is ready for an attempt. The last check says `ready: true`, and all changes are in `claims/000688/`; nothing is committed.

**Checker result:** `claims/000688/10.1016-j.neuron.2018.09.030.yaml: 28 claims, 27 quotes, 30 statistical values, 0 problems`. It was also 0 problems before my edits, with one fewer statistical value.

The PDF pages could not be rendered as images here, so I read the figures by parsing the PDF drawing data: text positions and colour swatches. That way I matched each printed p-value and asterisk to its model in Figures 3E, 6E, S5F, S6D/E, S7A/B, S7D, S7E and S7F. Every assignment in the claims is correct.

**Changes, by claim:**
- **figs2-covariance-preserved-example:** the Results call the r values one representative session. The Figure S2E legend says they cover all nine CF sessions. The criterion now names both readings and judges both.
- **figs3a-covariance-like-baseline-split:** rewrote a garbled note. The Baseline subsample is now read as two random halves of Baseline, as Figure S2D describes.
- **figs3b-covariance-preserved-vr:** the source now says the Results cite Figure S2B, but the VR covariance summary is in Figure S3B.
- **fig6c-null-leads-potent:** the statement says output-null also led at the end of Force, but the criterion did not test that. It now also requires a negative mean lag at the end of Force.
- **fig6e-planning-change-in-null:**
  - The movement window ends at 0.40 s after the go cue, not 0.45 s; the bar in Figure 6D ends at the 0.4 tick.
  - The movement-window asterisk is on the M1 bars, going by the legend colours. I added that p < 0.05 entry, and the criterion now tests the M1 part of the statement.
- **fig5-washout-null-m1:** which Baseline trials train the Washout models is now named as open, with two readings: all Baseline reward trials, or the last 50% of them.
- **figs7cd-single-neuron-models:** the Methods say the Figure S7C,D control used velocity inputs only, and the legends don't say. The kinematic covariates are now an open detail with two readings.

**Still open (recorded in the file):**
- **No test in the paper:** for fig2d, fig7bc, figs3a, figs4c, fig4c and figs7e, the paper gives no test. The session counts, t-tests and thresholds in their criteria are the first reader's own judging rules.
- **figs5e-pot-null-similar-training:** the Kolmogorov-Smirnov test is borrowed from a different comparison in the paper.
- **figs5f-rpr2-distributions:** the legend calls p = 0.04 significant, while the paper's threshold for these comparisons is 0.01.
- **Session counts:** the Figure 2C and Figure 7 legends list 7 CF and 5 VR sessions, against 9 and 7 in the Methods. The claims use the Methods counts.

Every main finding listed in the Discussion has a claim, and every claim comes from this paper.
