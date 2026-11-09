I checked the claims file for DANDI:001708 against the paper. It is ready for an attempt (`ready: true`). I made no commit.

**Checker:** `34 claims, 34 quotes, 54 statistical values, 1 problems`. The one problem is `VALUE NOT FOUND fig2g-switch-times -0.27`, and it is not an error. The text gives the ON interval as "0.27–0.095 s before" withdrawal, and the file records that as -0.27 to -0.095 s. Every quote matches the text word for word, including the new one.

**Changes, by claim:**
- **fig1c-psth-counts:** the window start was only the code's -30 s. The Methods give -10 s, so both are now readings, each ending at the Results' 150 s. **figs3-neutral-unmodulated** uses the same two readings.
- **fig1c-withdrawal-locked:** the paper never measures the lag, so the criterion now says using the switch times is a reading. I replaced a made-up margin with "the 97% intervals do not overlap", the way the paper compares these fits elsewhere. I also corrected the source paragraph from 6 to 9.
- **figs8-null-model-worse:** the statement now says "significantly", as the paper does.
- **fig2g-switch-times:** I added a note that the Discussion puts the OFF nadir more than 2 s after withdrawal, against 1.35 s in the Results. The Results' value is the one tested.
- **fig2g-on-double-exponential:** I dropped a two-standard-error margin that the paper doesn't state. The claim is now judged on the higher model score alone, like the matching OFF claim.
- **figs1-departure-timing:** I replaced a made-up partial rule ("before -1 s") with the rule the other timing claims use.
- **figs1-completion-asymmetry:** I replaced a made-up 97% paired-draws test with the paper's own comparison, non-overlapping 97% intervals.
- **fig3bc-psd-peaks:** I added the supplement's rat-level bootstrap as a reading for the peak and its width. The supplement takes precedence over the code.
- **fig4-nlml-minima:** the NEUTRAL limit was off by one. It is now 4 cells, since 1 plus 10% of 32 is 4.2.
- **fig5b-train-r2:**
  - NEUTRAL cells now use the full recording, as the Methods say, with the code's 1500 s segment as the variant.
  - The sign flips are now grouped by animal, as the Results say, with the code's grouping by file as a variant.
  - These changes carry to **fig5b-test-r2** and **fig5c-dispersion**.
- **fig5b-train-no-difference:** I added grouping by animal as a variant, since Figures S6 and S7 say "within animals". This carries to **fig5b-test-group-differences**.
- **fig6c-coherence-counts:** I added each cell's whole recording as a reading, since the Methods say only "the recording".
- **fig6d-heart-rate-peaks:** the "highest peak below 0.01 Hz" rule is now marked as not from the paper. The first half of the statement, about peak coherence frequencies, is now reported.
- **methods-heart-rate:** `expected` is now a list, like every other claim.
- **fig5d-phase-profiles:** this is a new claim, because Figure 5d's finding had none. Its measure and comparison are marked as open.

**What remains open:**
- Several claims rest on tests or bounds that the paper never gives, because it only inspects plots: fig3d-neutral-psd, figs3-neutral-unmodulated, figs2-phase-latency and fig5d-phase-profiles. Each is marked as open, but they are still the reader's choices.
- dataset-composition: the Methods and Table S11 disagree on the number of animals. Both readings are kept.
- fig6c-coherence-counts: the partial rule ("within 2 of each count") is not in the paper.
- I could not check any detail the first reader took from the code (notebook values, function names, the priors on log k), because the code repository was not available here.
