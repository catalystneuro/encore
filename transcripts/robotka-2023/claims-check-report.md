I checked `claims/robotka-2023.yaml` against the paper and the paper's code at the pinned commit (f2d2376), corrected what I could show was wrong, and marked it ready. Nothing is committed.

**Checker result:** before my changes, `28 claims, 27 quotes, 22 statistical values, 0 problems`; after, `29 claims, 28 quotes, 25 statistical values, 0 problems`.

**Changes, by claim**
- **Header, readings:** many criteria said "reproduced when, under one reading", which accepts a match under any reading. The protocol allows that only when a reported number can be read more than one way. Where the Methods and the code disagree on a method, the Methods reading comes first and the code's is a variant. I added a paragraph after C12 saying which readings are which.
- **Header, C3:** the Methods selectivity index is now built on the code's Z, which does not subtract the mean. With the mean-subtracted Z, the index would be about 1.11 for every unit, outside the 0 to 1 range the Figure 5F legend gives.
- **fig5f-si-unrelated:** the judged test now uses the Methods selectivity index; the code's version is a variant.
- **good-units-100:** "the count is the mean over 10 runs" came from neither the paper nor the code. The count now comes from one run, as in the code, and the range over 10 seeds is reported.
- **figs4-per-bird-and-sex:** the criterion described a t-test on the four birds' mean PCC, which is not the paper's test. It now uses the test in `plotConfusionsBird.ipynb`: ensembles of 15 units, sex means weighted by effective sample size, pooled corrected SD, 2 df. That code prints the paper's t(2) = 0.6757, p = 0.5689.
- **figs6-primary-vs-secondary:** rate and efficiency were never defined. I took the definitions from the SI Figure 6 legend and `plotConfusionsArea.ipynb`.
- **acoustic-labels-decoding:** the text says 1,746 ensembles, but the code compares 10,000 ensembles (38.07 against 42.28). Both are now readings.
- **fig3c-peak-call-types, fig4b-confusions, fig6c-ari-call-over-acoustic, figs10-ensemble-size:** the rules for "bias toward the longer calls", "most misclassifications", "large majority" (75%) and "increases with size" are now marked as readings, not from the paper. The 75% rule was stated two ways and is now stated once.
- **New claim, anesth-primary-secondary-rate** (data elsewhere, CRCNS aa-4): in the anesthetized data, the firing rate is lower and decoding per spike higher in the secondary pallium. The Results and Discussion state this and it had no claim.

**Confirmed unchanged:** all quotes, p-values, counts and test statistics. In the code, the decoder's cross-validation, the PCC > 30 filter that gives 1,746 ensembles, the eigh call for the discriminant axes, the log volume and the Ward linkage on UMAP all match the file. The 42.3% and 29.6% are means over the 10,000 Figure 4B ensembles, as the file reads them.

**Still open**
- **fig6a-acoustic-clusters** is marked `with_inputs`, but it uses no data from the dataset; it runs entirely on the lab's vocalization database, for which the paper gives no deposit. It should be `elsewhere` if that database is public, or `dataset` blocked as `data_missing` if not. I did not find out which.
- **Degrees of freedom:** several printed values match none of the paper's unit counts (anesthetized F(1,343), F(2,341), t(303); SI Figure 9 F(4,125), F(4,170)). The claims judge the effect sizes instead.
- **Tolerance:** R2adj = 0.1 is printed to one digit, so the default 10% tolerance (±0.01) may be stricter than the paper's number warrants.

**Ready:** yes, `ready: true` in the new `checks` entry.
