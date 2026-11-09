I've checked the claims file and corrected 15 claims. I think it is ready for an attempt, and its last check says so (`ready: true`). Nothing was committed.

**Checker result:** `26 claims, 24 quotes, 1 statistical values, 0 problems`. The first run reported 4 statistical values; I removed 3 of them, as explained below.

**Changes, by claim**
- **fig8-nbta-differ, fig9-nbta-not-concatenated-1bta:** I removed the ANOVA and t-test p < 0.01 entries. They are significance levels used to count sessions, not results. In fig8, the statement no longer says every bursting cell's peaks grow higher and wider with n. The paper shows that for the example cell only, and says in Qualitative description, paragraph 6, that some cells differ.
- **direct-method-comparison:** I put the tolerance on R (0.95) back to the default 10% (0.095). The stated reason for narrowing it, that 10% would allow values above 1, did not hold up.
- **fig8-latency-decreases:** the criterion required both readings to hold. The protocol says any one reading is enough, so I changed it.
- **fig8e-sigma-minimum:** the 7 ms minimum comes from the example cell (with its 0.33 ms), not the population; the statement now says so. I added the paper's second population value (about 0.05 times the inverse cutoff). The window searched for the minimum is not stated in the paper, so it is now two readings.
- **firing-rate-uniform:** the reason given for testing only the kept sessions misread the paragraph order. Both the 86 kept sessions and all 132 are now readings.
- **data-sessions-and-trials:** I added the reported 6 Hz average of the trial-to-trial firing-rate SD.
- **table1-sessions-per-protocol:** the note now says why "recorded sessions" are read as the 86 kept ones: the seven counts add up to 86.
- **fig3-correlation-shape:** the criterion said the Methods give each cell two stimuli; paragraph 1 says two or more. "Sharper peaks" was measured by peak height alone; it now allows height or narrowness. Which panels have a clear first peak is now cited from Results paragraph 4, and 3 dB is added as having none.
- **model-matches-classification:** the 25 and 50 ms filter lengths were made up. Eq. 2 integrates up to T, which the Methods define as the stimulus duration, so that is now the main reading and 25 ms the second.
- **fig7ab-information-per-burst-increases:** I added an open choice. Eq. 10 as printed and the per-event form in Eq. 3 give I_n(1) values that differ by a factor of T.
- **fig7cd-occurrence-decreases:** the Figure 7C legend says "number of occurrences" where the text says "frequency of occurrence". The note says the slope is the same on a log scale.
- **fig9c-population-nbta:** the peak width is not defined in the paper, so it is now two readings.
- **fig5-burst-probability-vs-stimulus:** the order of the n = 2 and 3 probabilities is now shown, since the statement also claims it.

**What remains open**
- The paper gives three different counts of bursting sessions: 63 in Table 1, 59 for Figure 7 and 58 for Figure 8, with no reason given. The file's opening comment already lists both readings.
- Several cut-offs for "partially reproduced" (for example 16 of 19 values, or 90%) are the file's own rules, not the paper's. I left them as written.
- Two sentences are garbled in the text: "no <69%" in fig7gh-information-rate and the sigma ratio in sigma-n-below-sta-sigma. No PDF was supplied to check them.

Every main finding has a claim, and none comes from outside the paper.
