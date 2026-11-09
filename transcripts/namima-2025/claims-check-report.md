**Checker result:** `27 claims, 27 quotes, 10 statistical values, 0 problems`. It started at 12 statistical values; I removed two that were thresholds used to count neurons.

**Changes, by claim**
- **Header:** the paper names "Pype2; Mazer, 2013" and gives no link. The header now says that the pype3 repository the first reader read is a later version.
- **ex-m2p6-cluster:** I removed the statistics entry. The p < 0.05 there is the cutoff used to count neurons, not a result. I also replaced the made-up rule "at least 7 of neurons 1 to 9". The criterion now asks for the paper's set (neurons 1 to 9, 14 and 17, with one neuron of slack from the count's tolerance) and for their negative slopes.
- **ex-m2p6-invariance:** the rule that unreliable values count as not above 0.5 now cites the Fig. 4F legend, which plots an unreliable value at 0.
- **ex-csd-sinks:** the paper gives no criterion for "no other sink deeper" in M1p12. That part is now marked open: the CSD profile is shown but not judged.
- **pop-significant-isimilarity:** I removed the statistics entry, because the p < 0.05 is the cutoff behind the 344 count.
- **pop-asymptote-20-percent and texture-asymptote-20-percent:** I removed the "partially reproduced" outcome for a 10 to 30% band, which the paper never gives.
- **orientation-sf-isimilarity:** I added reading (c), Fourier power in orientation × spatial-frequency bands, because the paper cites David et al. 2006 for this model.
- **orientation-auc-coarse-clusters:** "switching" had been narrowed to a single change along depth, which the paper doesn't say. I loosened it and stated that both kinds of penetration are plain readings, not definitions from the paper.
- **apc-example-m2p51:** the partial-outcome rule now says the curvature correlation must be "not significantly positive". It is significantly negative (p = 0.012).
- **gyrus-penetrations-consistent:** both of its tests were invented (a Mann-Whitney test and the 10 to 30% band). The 18 penetrations are now judged against the paper's stated level of about 20%, within that claim's tolerance. The Mann-Whitney test stays only as a variant and does not decide the outcome.
- **position-examples-invariant:** its only measure was the first reader's own. I marked it open and added a second reading from the paper's own cluster measure (Isimilarity at each position). If the two readings disagree, the claim is blocked as `methods_underspecified`.

**Still open** (all recorded under `checks`)
- **gyrus-penetrations-consistent:** the paper compares the 18 penetrations with the rest only by eye. Those 18 can only be identified from the dataset.
- **orientation-auc-coarse-clusters and position-examples-invariant:** both rest on readings the paper doesn't define. I couldn't render the PDF here (no PyMuPDF or poppler), so I can't say whether Fig. 6C is M2p6 or M1p5.
- **Penetration names:** the paper never maps M2p6, M1p12, M2p9, M2p28, M2p51 or M1p5 to sessions. They have to be found by neuron counts.
- **Texture contrast invariance:** the abstract claims it, but the Results report no number for it, so no claim covers it.

**Ready:** yes. I set `ready: true`. Every main finding has a claim, and every remaining gap is named as open with the readings the paper allows. Nothing is committed.
