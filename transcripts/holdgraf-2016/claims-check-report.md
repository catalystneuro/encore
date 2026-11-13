The claims file for CRCNS:ac-4 is ready for an attempt. I made seven changes and added one claim, and nothing I found shows the original file misreads the paper.

**Checker result:** `26 claims, 26 quotes, 27 statistical values, 1 problems`. The one problem is the behavioural t-test's P = 1e-5. The text prints it garbled ("P 1⁄4 1e �5"), so the checker can't match it; I confirmed the value by reading it.

**Figure 4 check:** The P-values are listed together in the extracted text, so I checked which belong to which panel using the label positions in the PDF. Panel a ("Coherence between conditions") prints P = 0.924, 0.000, 0.001, and panel b ("after mean subtracted") prints 0.920, 0.241, 0.006. That matches the file, so fig4a and fig4b are unchanged. The Results quote P = 0.006 for the panel a finding, which conflicts with the figure; the file already records this as a paper inconsistency.

**Changes, by claim:**
- **behav-context-enhancement:** The 4.53% no-context value can't come from group 1, which the paragraph before puts at 3.5%. I named which subjects give it as open: (a) group 2 after the BEFORE sound (Fig. 2b legend), or (b) group 1.
- **supp1a-linguistic-context:** The criterion judged t = 9.65 and t = 2.39, but neither was an expected value. I added both, with 10% tolerance. They can't go under `statistics`, which needs a p-value or an interval, and the legend gives neither.
- **fig3b-hfb-increase-after:** The Results test only Speech-R electrodes on temporal and perisylvian cortex, but the legend gives n = 92, which is all Speech-R electrodes. Both sets are now named as readings.
- **fig8-mtf-matches-filter:** The paper doesn't say in which modulation regions each filter's MTF should be higher. The criterion's regions are now marked as an assumption read from the filter definitions.
- **fig10c-stg-location:** "The majority of the increase" had a single made-up measure. I added a second reading: more than half of the electrodes with a positive difference are on the STG.
- **supp7-envelope-coherence:** The statement says frontal electrodes show no effects, but the criterion didn't test that; I added it. The theta range isn't defined for this figure, so I named 3 to 8 Hz and 2 to 12 Hz as readings.
- **New claim supp6a-after-closer-to-middle:** It covers a main-text finding that had no claim: in AFTER, coherence between electrodes is closer to its value for unfiltered speech. The paper gives no test, so the measure of "closer" is marked as an assumption.

**Still open:**
- I didn't re-read the ecogtools code that some criteria cite (bootstrap settings, `coh_to_bits`, `partial_corr`, `mps`). I used no network access.
- The P < 0.001 bound in behav-context-enhancement is the claims author's choice; the paper prints P = 1e-5 with no precision.

All three points are in the new `checks` entry at the end of the file, with `ready: true`. Only `claims/crcns-ac-4/10.1038-ncomms13654.yaml` was changed; nothing is committed.
