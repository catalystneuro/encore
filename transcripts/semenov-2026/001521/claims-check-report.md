The checker's result after my edits: `27 claims, 27 quotes, 8 statistical values, 0 problems`. It gave the same line before them.

The quotes, sources and statistics match the paper. Most of what I changed was in the criteria. Several used windows or bounds the paper doesn't give without saying so, and some didn't test parts of their own statements. All edits are in `claims/001521/10.1016-j.bioelechem.2026.109283.yaml`; nothing is committed.

**Changes, by claim**
- **fig6a-ca-entry-1000-1200, fig6b-train-threshold:** The comparison behind "a clear peak", both rules for a "strong response", and 90% for "nearly all" are now marked as choices made in the file, since the paper gives none of them.
- **fig1-pole-leakage-pattern:** The 45 to 60 degree band is marked as a choice. The paper only says regions near the equator "may polarize more" than the poles, so that comparison is now reported and no longer required.
- **fig2a-fluovolt-saturation:** Added a criterion for the part about stronger fields, which the expected values alone didn't judge.
- **fig2a-fluovolt-stable-within-set, fig2b-di8-decline-within-set:** The "first 10 pulses" window is now cited to Fig. 4B, and the "last 10" is marked as a choice. Judging the decline at the cathodic pole is now cited to the Discussion, point (a).
- **fig2cd-stable-then-drop:** The comparison is now with the first set at the same field, as in the Fig. 2D legend. Added the legend's "≤20%" as a second reading of the drop, next to the Results' "about 20%".
- **fig2c-1000-within-set-trend:** Removed the test name from the statistics, because the paper doesn't name the test behind "p > 0.05". Added a criterion for this absence claim, with two readings of "beginning" and "end" of the set.
- **fig4a-fluovolt-maximum:** The 45 to 50% range was set as 47.5 ± 7. The protocol widens each bound by 10%, so it is now 47.75 ± 7.25. Added a criterion.
- **fig4b-di8-maximum:** Added a criterion for "measured IMP fell below the calculated value" at 570 V/cm.
- **fig4b-cathodic-asymmetry:** "Within one s.e. of zero" came from nowhere in the paper. It is now a one-sample t-test, a test the Methods name, marked as chosen here.
- **fig4c-equator-cosine:** The fit linking charging time to cell radius comes from the paper's ref. 20 and isn't printed here, so it is now named as an outside input. The 30 degree window and "more than half of the angles" (it said "most angles") are marked as choices.
- **fig5a-gd-extends-anodic:** Added a criterion. It gives two readings of how the group maximum is formed, and a bound (marked as a choice) for "nearly identical to the calculated IMP down to -780 mV".
- **fig5b-conductivity-calibration:** Named the main reading of the IMP reduction and a variant.
- **fig5c-gd-reduces-conductivity:** The expected value (2.5 ± 0.6) didn't match the criterion's 1.8 to 3.3. It is now 2.55 ± 0.75. Which datapoints count is named as open.
- **fig7a, fig7b (both claims), fig7c:** Added the missing criteria: the cosine-fit part of fig7a; normalization, the linear line and the test for the conditioning pulse; two readings of the legend's "two-sided t-test" against the undamaged membrane; the absence parts (up to 760 V/cm, and 1000 V/cm); and the resealing part of fig7c.

**Still open (recorded in `checks`)**
- The paper doesn't name the test or the time window behind "not statistically significant" at 780 V/cm (Fig. 6A). The readings in the file's opening comment stand.
- Working Eq. 2 with the paper's constants gives about a 1.3% reduction for a 10-fold conductivity increase, against the paper's "~2%". fig5b may fail on that rounding. I left the paper's value as it is.
- The abstract gives a 1000 V/cm charging limit for 0.3-µs pulses, but no sentence in the Results states it, so it has no claim of its own.
- The test behind fig5a's p < 0.001 isn't named in the sentence; the "2-tailed t-test" recorded comes from the Fig. 5A legend.

**Ready:** yes. Every main finding has a claim, every claim comes from this paper, and the last check entry is marked `ready: true`.
