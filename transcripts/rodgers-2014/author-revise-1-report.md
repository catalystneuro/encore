I answered every point in the round-1 report, recorded the round under `verifications`, and re-ran the entry. The final run of `python tools/entry.py all entries/crcns-pfc-1-rodgers-2014` passed with 0 errors in 233 s. The fixed seeds give the same numbers as before, and the handover copy no longer contains any "Result" text.

**Outcome changes**
- **fig8-model**: changed from `partially_reproduced` to `reproduced`, marked `assumed: true`. The verifier gave this outcome, and the new outputs support it. At SNR 0.25, performance is at least 99% from task signal/noise 0.32 to 10. That covers 90% of Figure 8B's plotted positive axis and 97% of the linear range from 0 to 10. On the code's narrow linear sweep, 38 of 40 positive gains reach 99%. "Most positive task signals" is now read over the range the figure plots. If you count the log-spaced broad sweep sample by sample, the second condition still fails (25%). The notebook shows that count and the record states it as a deviation.
- All other 34 outcomes are unchanged. The verifier agreed with all of them.

**Outputs added for the verifier's requests**
- **fig2d**: a crosstab of fold position against the block column. The 80-trial blocks line up exactly with the fold, and no position holds two block values.
- **evoked-beyond-baseline-rare**: the bootstrap p values for all 43 A1 units under three seeds. Every seed gives 6 units after Benjamini-Hochberg correction, 4 of them from CR12B and all 4 higher in pitch discrimination. The unit ranked 7th has adjusted p = 0.063.
- **fig6e**: a chance level from shuffled labels, about 0.54 in A1 and 0.52 in mPFC. A1 scores are clearly above it; mPFC scores are barely above it (by 0.003, p = 0.094). The notes now say the mPFC block comparisons are made on scores near chance.
- **fig5ab**: medians with the 9 invalid-interval units left out. Both regions give 0.650 s, which is outside tolerance in A1. I kept the outcome because the criterion takes the median over all units, as the code's `main4.py` does. The dependence is now stated.
- **Small-sample claims of absence**: power and 95% intervals added for figs5fg (with 9 mPFC units, only |r| ≥ 0.82 is detectable), posture-equalized-magnitude and figs2gh.

**Corrections**
- The audresp-prevalence conclusion wrongly said the responsive units had not been recomputed from the spikes. It now says that recomputing gives 46 and 61, both outside tolerance, so the claim holds only with the code's unit table.
- The summary, README and notes now say which outcomes depend on the code's own choices:
  - response windows (audresp-prevalence and figs5e-latency)
  - smoother (fig5ab)
  - Benjamini-Hochberg correction (evoked-beyond-baseline-rare)
  - reading (a) (fig5d)
- Four conclusions sat inside section headers, so the handover had kept them. I moved them into their own cells.
- I added the notebook header the protocol requires (paper, dataset, source text, claims table). It was missing.
- The README no longer carries the failure-to-reproduce sentence, since no outcome is partial or failed now.

**Not done**
- I added no reader questions. The verifier noted that the claims file leaves the fig8 reading open, but it did not report a misreading of the paper.
- I did not change any claim.
