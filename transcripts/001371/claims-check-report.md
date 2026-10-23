The claims file for DANDI:001371 is ready for an attempt (`ready: true`). I made seven corrections, all in criteria; no claim ids, statistics or expected values changed. Nothing is committed.

**Checker result:** `52 claims, 52 quotes, 105 statistical values, 5 problems`. All quotes match word for word. The 5 problems are p-values the checker could not find: 3.41e-11, 2.63e-08, 1.02e-07, 4.49e-05 and 1.33e-05. Each is the paper's own number with its trailing zero dropped (the paper prints 3.410e-11, and so on), so they are correct.

I checked every statistic, expected value and tolerance against the main text, Supplementary Tables 1 and 2, and the figure legends. All are the paper's own numbers.

**Changes, by claim**
- **trial-mix:** the paper's own trial counts do not give 65/25/10%. Supplementary Table 1 gives 76/17/7%, and the Results counts give 74/19/7%. Both are outside the tolerances, so the percentages are read as the task's programmed trial probabilities. The criterion now says so and asks for the actual fractions to be reported. The expected values are unchanged, so this claim will probably fail even on the paper's own numbers.
- **task-timing:** the paper does not say which trials the 6.02 s second delay covers. I added two readings: switch trials only, and switch and stay trials together.
- **sfig2f-all-trials-encoder:** the criterion assumed only a held-out 20% of trials was decoded. The legend's 4538 delay only trials is about 926 / 0.2, so the decoded trials do not look like a 20% test set. The split is now open, with both readings named.
- **fig4h-hpc-choice-switches** and **fig4h-hpc-choices-equal:** the Methods set the window at 0 to 1.5 s and the authors' code uses 0 to 2 s. The protocol puts the Methods first, so 0 to 1.5 s now decides the outcome and 0 to 2 s is shown as a variant.
- **fig6b-hpc-new-lower-incorrect:** the Methods fit the speed-and-rotation model (GLM) "across all trial types and animals"; the code fits it per session. The Methods version now decides and the code's version is a variant. I made the same change in the six claims that use these residuals: fig6b-hpc-initial-no-difference, fig6-hpc-pre-cue-initial-higher-incorrect, fig6d-pfc-new-lower-incorrect, fig6d-pfc-initial-no-difference, sfig12-delay-hpc-no-outcome-difference and sfig12-delay-pfc-outcome-difference.

**What remains open** (recorded in the `checks` entry)
- Six claims rest on measures and pass rules the first reader chose, because the paper reports no test for them: tuning-tiles-track, decoding-validation, fig1d-heading-switch, fig4d-pfc-precedes-movement, fig4g-hpc-slower-than-pfc and sfig7d-pfc-before-motor-single-trials. Their criteria say this.
- I did not re-read the authors' code (stephprince/update-project at d8557f0), so the code details quoted in the criteria are taken on trust.
- Four supplementary findings have no claim. None is a main finding:
  - theta segregation on delay only trials (Supplementary Fig. 6b);
  - equal CA1 and prefrontal choice decoding (Supplementary Fig. 9e);
  - the stay-trial difference over 0 to 0.5 s (Supplementary Fig. 10b, right);
  - performance against warm-up delay length (Supplementary Fig. 1c, which gives no numbers).

Every main finding in the paper has a claim, and all claims come from this paper.
