I've handled the round-2 report. The verifier agreed with all 30 outcomes, so none changed and none is proposed. I re-ran the entry with `python tools/entry.py all entries/robotka-2023` and it passed in 3,281 s (about 55 min). Every number the outcomes rest on is the same as in the round-1 run, and the executed copy matches the entry. The checks report 0 errors, and nothing is committed.

**Corrections**
- **KDE_BW finding: withdrawn.** The verifier was right that nothing printed supported "can only be milliseconds", and the descriptor's description fits the values. The data-check cell now prints every KDE_BW value with its count (0.2 to 10.0, with 646 of the 872 pickles at 10) and the range of RateThreshold. The pcs-variance notes and the Summary now say only that KDE_BW is the bandwidth of the coarse rate used for the rate threshold, not that of spikeKDE.
- **README run time:** the wrong "47 minutes" now reads "about 55 minutes".
- **fig5-multiple-regression notes:** the Methods' SI changes R2adj by at most 0.0009 under the code's cross-validation and at most 0.0025 under the Methods' (0.4841 against 0.4866).
- **fig4b-top-ensembles:** taking the best ensemble from the 1,800 Figure 5 ensembles is now a deviation, and the Summary says so too.
- **Stray `**`:** removed from the ends of the 11 conclusion cells.

**Added**
- **The code's lines:** the notebook now prints the lines that fill `allz` (every trial of the good units) and the code's clustering threshold lines (`delta = (clustered.max()-clustered.min())/500`, `start_thresh = clustered.min()`). This confirms the C12 point: the code takes the minimum and maximum over the whole linkage matrix, not just the distances.
- **The code's threshold grid as a variant on fig6c (still blocked):** it is cut on the same trees as the C12 grid. Under the C12 grid both unit readings give a median of 10, outside 9 ± 0.9, and means of 10.42 and 10.28. Under the code's grid the medians are 9 and the means 9.91 and 9.76, all within tolerance. The conclusion, Summary row and notes now give both unit readings.
- **A second question for a reader** in `questions/robotka-2023.yaml`, on how C12 describes the threshold grid. The C11 entropy-selectivity question from round 1 is still open.
- **Round 2 recorded under `verifications`:** the verifier's reasons in its own words, with my response for each claim.

**Not done, and why**
- **UMAP values moved:** in the first re-run they shifted slightly from round 1, for example the Methods reading's median went from 9 to 10, while the Ward values stayed the same. The second re-run gave identical numbers, and UMAP gave identical results twice on this machine in a quick test, so I think the difference comes from the machine. I did not confirm that, and a re-run elsewhere may move these values a little.
- **Still open from the verifier, with no change possible in this round:**
  - good-units-100 depends on the seed: 8 of the 10 other seeds fall within tolerance.
  - fig5e-volume and fig5-multiple-regression rest on the code's window and LDA axes. Without them both would be partially reproduced.
  - fig5g-entropy-selectivity depends on the reader's answer about the entropy-selectivity reading, which could reverse it.

  All of these are already stated in the notes and the questions.
