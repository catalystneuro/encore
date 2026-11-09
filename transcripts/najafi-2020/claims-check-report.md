I checked the claims file for DANDI:000016 and corrected nine claims. It is ready for an attempt, with four open problems recorded in the file.

**Checker result** (same before and after my edits): `38 claims, 38 quotes, 10 statistical values, 0 problems`

The paper's code is not in the repository, so I cloned it at the commit the file cites (b7352acd) to spot-check the criteria that cite it. The settings the file quotes match the code, except for one misnamed file (fixed under fig8ab below).

**Changes, by claim**
- **fig2bc-fraction-selective-similar**: the statement now says the difference is significant in mouse 4, as the Figure 2C star and the Figure S3D legend report.
- **fig3hi-mixed-no-advantage**: the file only failed the claim if the mixed population did better. The paper says the two accuracies were "similar", so a significant difference in either direction now counts against it.
- **figs6ab-previous-choice-stimulus**: the criterion let mouse 4 differ between excitatory and inhibitory populations. The S6B legend actually excepts mouse 4 from the weak stimulus-category signal, not from that comparison. The exception is now in the statement, the comparison covers every mouse, and it is partially reproduced if one mouse differs.
- **figs6c-outcome-decoding**: "significant in at least two mice" was invented. It is now the direction in every mouse (the paper's "small but consistent"), with the t-test reported. The end of the post-reward window has two readings.
- **fig5bc-selective-models-match**: the criterion tested that inhibitory accuracy rises faster in all three models, which the statement did not say. I added that to the statement and the matching Results sentence to the quote.
- **fig6a-same-selectivity-correlations**: the statement includes the pre-trial (spontaneous) result, but the criterion had no rule for it. It is now judged by the same test.
- **fig8ab-learning-accuracy**: corrected the name of the code file that sets the easy-trial threshold.
- **fig8de-learning-parallel**: "late accuracy exceeds early" now names its test, the same t-test as the rest of the criterion.
- **fig8f-correlations-decrease**: "significant in at least two of three mice" was invented. It now requires significance in every learning mouse, with a partial outcome if only the direction holds.

**Open**
- **fig3df-weights-similar**: the Figure 3F legend marks significant differences in mice the text does not name, and the main-figure PDF is not under `paper/`. The paper's own result may only reach the criterion's "partially reproduced" band.
- **figs3e-correct-error-correlation**: the paper gives no minimum number of error trials. The file's threshold of 10 is the code's threshold for correct trials, carried over as the only reading.
- **figs1b-trial-history**: the Methods' worked example contradicts its own definition of the long-ITI bin. The criterion follows the definition and the code, which agree.
- **fig5bc-selective-models-match**: "about the same" is read as the two curves crossing within a factor of 2 of a ratio of 1. That is a single reading the paper does not fix.

Every main finding has a claim, and all claims come from this paper.

**Ready**: yes (`ready: true`). Nothing was committed.
