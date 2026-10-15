**Round 2 verification: Gerken, Darcher et al. 2025 on DANDI 001616 (0.260702.0824)**

The claims file has 20 claims and the attempt record has 20 outcomes:
- reproduced: 6
- partially_reproduced: 5
- blocked (methods_underspecified): 9

**1. Do I agree with each stated outcome?**

I agree with all 20.
- **dataset-composition (partially_reproduced):** Agree. Cell 5 gives 29 patients, 2286 units and 17 female patients, all exact. EC 493, PHC 293 and PIC 68 fall outside their tolerances.
- **The six responsive-unit claims (blocked):** Agree. These are fig2b-phc-camera-cuts, tables1-camera-cuts-regions, fig2b-phc-scene-cuts, tables1-few-semantic-responses, tables1-no-indoor-response and results-cluster-regions. Cell 18 now shows the null rate at each label's own number of onsets. The observed counts sit at that rate: Summer 44.31% observed against 44.05% at random times, Tom 51.36% against 50.26%, scene cuts 49.04% against 48.25%.
- **fig3b, fig3c-logreg-characters-location, fig3c-logreg-cuts-lower, fig3e, fig4-patients-below-pooled, fig4-named-patients (reproduced):** Agree. Cells 41, 44, 49, 52 and 55 meet each criterion.
  - Camera Cuts at 0.0961 clears its lower bound of 0.095 by only 0.001.
  - fig4-named-patients still assumes the subject ids are the paper's patient numbers.
- **fig5-region-decoding (partially_reproduced):** Agree. Three of four orderings hold (cell 58).
- **fig5-faces-presence (partially_reproduced):** Agree. One of three conditions holds (cell 61). The criterion was written before these labels were decoded.
- **fig6-responsive-subsets (blocked):** Agree. The subsets come from the uncalibrated test. The variant with only the non-responsive units that spike gives drops of 0.062 for camera cuts and 0.060 for Summer (cell 64).
- **fig7b-top500-overlap (partially_reproduced):** Agree. 95 common units against 78 ± 7.8, which is about 83 times chance (top_ranked_units cell 4).
- **fig7a-500-neurons (partially_reproduced):** Agree. The top 500 units give 0.375 against 0.357 for all units, but 229 units give a higher 0.394 (top_ranked_units cell 7).
- **fig3c-lstm-decoding and fig3d-temporal-shuffle (blocked):** Agree.

**2. Does the text match the printed numbers?**

Every "**Result:**" conclusion, the Summary and the attempt record's notes match the outputs, apart from these:
- **Main notebook, cell 21:** "now run for every unit and the 11 labels of Table S1 in the companion notebook `responsive_zeta.ipynb`".
  - No notebook has that name; the ZETA test is in `responsive_zeta_cuts.ipynb` and `responsive_zeta_labels.ipynb`.
  - Those two notebooks cover 9 labels. Tom Faces and Summer Faces are not run.
- **Main notebook, cell 65:** "so with active units alone the drop is no larger for camera cuts than for Summer". The printed drops are 0.062 and 0.060, so it is 0.002 larger. "About the same" would match the numbers.
- **ZETA notebooks (cuts cell 10, labels cell 8), cell 22, the README and the record call the ZETA test "calibrated".**
  - At alpha 0.01 the labels notebook flags 0.12 to 0.38% of units at random times, and 0.21% over all labels. That is conservative, not calibrated.
  - At 0.001, zero hits in 400 or 800 units cannot show calibration (0.4 to 0.8 would be expected).
  - "Conservative" or "not anticonservative" is what the outputs support.
- **README:**
  - "counts about 70% of units responsive even at random event times". That holds only with as many events as camera cuts (68.4%). With each other label's number of onsets the rate is 9.5 to 55.5% (cell 18).
  - "counts far fewer units than the paper". This is false for Outdoor (8 against 4), Indoor (2 against 0) and McKenzie (1 against 0) (labels notebook, cell 7).
  - It gives run times of about 22 and 14 minutes. The runs printed 15.2 and 9.7 minutes; minor.

My round-1 reasons are reported faithfully. Most are verbatim with the cell references removed. Several have accurate third-person summaries of my problem and not-checked lists appended ("It found…", "It asked…").

fig5-faces-presence and fig7a are recorded as agrees: false, although my own round-1 outcome was also blocked. The response explains this: I held the blocks avoidable and listed them as affecting a conclusion. I accept that reading.

**3. Which round-1 points are resolved?**

Resolved:
- **Point 1 (Wilcoxon test miscalibrated):** Handled. The claims stay blocked, and the record now gives the null rates by number of onsets plus the synthetic check.
- **Point 2:** The per-label null is now shown (cell 18).
- **Point 3:** The active and inactive split and the active-only variant were added (cell 64).
- **Point 4:** fig5-faces-presence and fig7a now have stand-ins with criteria written before the fits.
- **Point 6:** First segments are kept, and cell 16 asserts the onset rule.
- **Point 7:** `sample_windows` now extends the edges.
- **Point 8:** The scikit-learn ≥ 1.8 requirement is documented in `fit_logreg`. I could not see `requirements.in`.
- **Point 9:** The weak per-patient clock check is now stated (11 of 29) and backed by the per-patient shifted-label check (18 of 29).
- **Not-checked items:** Per-fold permutation p-values were added for fig4 and fig5.

Partly resolved:
- **Point 5:** ZETA now covers every unit and 9 labels, but still with 100 resamplings. 1000 were compared only for PHC and scene cuts (11 and 31 against 12 and 29).

Not resolved:
- The subject-id to patient-number mapping (the Figure 4 image could not be retrieved).

What remains that bears on a conclusion:
- **fig4-named-patients:** It still rests on the unconfirmed id mapping, and patient 15 is at 0.197, just under 0.2.
- **fig3c-logreg-cuts-lower:** It is reproduced by a 0.001 margin for Camera Cuts, and one Scene Cuts fold is at chance (p = 0.89). The notes state both; the outcome is fragile but follows the criterion.
- **fig7a-500-neurons:** The 500-unit advantage (0.018) is smaller than either SEM (0.026, 0.029). The criterion uses means, so the outcome stands.
- **ZETA as a test of the paper's counts:** Its conservatism at 0.01 means its counts are lower bounds. That does not change any outcome: the gap is 79 against 1025 for camera cuts, and ZETA is only a variant.
