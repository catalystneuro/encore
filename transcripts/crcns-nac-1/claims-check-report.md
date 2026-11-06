The claims file is ready for an attempt. I corrected eight claims and marked it `ready: true`.

**Checker:** `34 claims, 34 quotes, 117 statistical values, 44 problems`. All 34 quotes match the text word for word. Every one of the 44 problems is a "VALUE NOT FOUND", and each comes from the text extraction, which prints minus signs and "x 10^" as a replacement character. I checked all 44 against the paper by reading and they all match.

**Changes, by claim:**
- **cue-responsive-193:** The paper says "at least seven" units per rat, which is a lower bound. The file had an expected value of 7 with tolerance 0.7, which would have required exactly 7. The criterion now requires every rat to have at least 7.
- **fig1c-acquisition:** The criterion checked the cue order in session 8 only, which the paper does not specify. Session 8 and the mean over all eight sessions are now named as open readings.
- **fig2-five-clusters:** Reading (b) claimed the Methods give firing in Hz. They only say "firing rate", so it is now described as a reading that wording allows.
- **fig3c-waveform-bimodal:**
  - The narrow/wide boundary had been fixed as the trough of the histogram, a method the paper does not give. It is now open, with two readings: the dashed line in Figure 3C, or the trough.
  - The Bidirectional Valence split band of 40 to 60% had no stated reason. It is now 45 to 55%, which is 10% of the paper's 50%.
- **fig7-tuning-curves:** The extreme of each tuning curve is now the assignment with the most extreme mean beta, as the Methods define it. Before, it was a most-negative or most-positive value chosen per population.
- **fig8ab-thi-exaggerated-threat:** The statement said exaggerated threat betas "exceeded fear output betas in magnitude". The paper only says the two differed at early cue but not late cue, and the statement now says that.
- **fig9efg-reward-cue-correlations:** The statement includes Threat Inhibited and Danger Excited results that the criterion never judged.
  - Those results now decide a partial outcome.
  - The Threat Inhibited danger correlation (p = 0.05, which the paper calls significant) is reported but not judged.
- **fig9hij-danger-safety-correlations:** The quote stopped in the middle of a number and did not state the finding. It now quotes the full sentence.

**Still open:**
- The value of the narrow/wide waveform boundary in Figure 3C is not in the text, and I could not render the PDF to read it.
- The Extended Data figures (1-1, 1-2, 2-1) are not under `paper/`.
- No analysis code was read. The first reader reported that the lab's resources page returns 404, so code cannot settle the open method details.
- All other claims check out against the paper: statements, sources, statistics, tolerances (paper CIs or 10%), and the degrees-of-freedom notes. The main findings are all covered.

Only the claims file was modified, and nothing was committed.
