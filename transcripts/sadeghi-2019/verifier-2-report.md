# Verifier report, round 2: sadeghi-2019-01

The claims file has 28 claims and the attempt record has 28 outcomes. I found no place where the claims file misreads the paper. I checked the Fig 9A legend's "144 ms", the "in all instances" wording and the time-averaged classifier passages.

## 1. Outcomes

**Neural and model claims (21).** I agree with all 21. The four claims marked `assumed: true` have their assumption stated, and each is reasonable:
- **fig1k:** uses the code's window. Neural cell 10 now prints NeuralExample.m lines 73–87.
- **figs9:** a is chosen on the validation data. This is stated as fragile.
- **fig9a, fig9b, fig9c and fig10:** discussed with the classifier claims below.

**fig1-s5 and figs10** stay blocked (data_missing). I agree. Neural cell 5 lists all 281 tar members and the Param fields, and none holds tone-pip or raw-voltage data. figs10 needs 5 of its 6 values, and only the 2 aMUA values can be computed.

**Classifier claims** (classifier notebook; "(7b)(b)" in its code means readings (6b)(7b)):
- **fig9b-similar-maximum: reproduced** (assumed, stated). I agree. Under the (7b) readings all three values are in tolerance and p ≥ 0.43 (cell 12).
- **fig9b-accumulation-rate: partially reproduced.** I agree. The order holds under (6a)(7b), where every optimum is unique, so it does not depend on the tie below.
- **fig9c: partially reproduced** (assumed, stated). I agree. It rests on reading (b), which is a claims-file reading, and the record says its test feature does not match the training features.
- **fig9e: partially reproduced.** I agree (cell 21).
- **fig9a: reproduced** (assumed). **I do not agree as recorded.**
  - Under (6b)(7b), the spectro-temporal classifier scores 81.5% at 100, 141 and 283 ms alike (cell 7: `74.9 80.5 80.0 79.0 81.5 81.5 81.0 81.5 …`).
  - 100 ms is picked only because `argmax` takes the first maximum (cell 8: "ties go to the first").
  - Taking 141 ms instead would give partially reproduced; taking 283 ms would give not reproduced.
  - The record does not mention the tie. At minimum it has to be stated and the outcome marked as resting on that tie-break. My view is that the data do not pick out 100 ms.
- **fig10: reproduced** (assumed). **I do not agree as recorded.**
  - Reading (d) is the only value that passes: −20.5 against a window of −20 ± 2.
  - Cell 27 computes it as `np.mean(tm[:k_] - voc[:k_])`. That pairs the temporal curve (141 ms optimum, 381 ms spacing) with the spectro-temporal curve (the tied 100 ms, 269 ms spacing) by window index, not by duration.
  - This is under (6b)(7b), the reading the outcome rests on. The record's remark that "(6b)(7b) rows are at the same optimum" holds only for spectral against temporal.
  - The spectral advantage is significant at 1 of 10 durations (p = 9.1e-03, Bonferroni corrected).
  - Before any verdict, the difference has to be recomputed with matched durations.
- **fig9-spectrum-classifier-lower: not reproduced.** I agree under the criterion. However:
  - At full duration the spectrum classifier exactly ties the temporal one (80.0 = 80.0 under (6a)(7b); 80.5 = 80.5 under (6b)(7b), cells 7 and 24). So the partial rule fails by zero points.
  - Its PC and component counts (PCs for 90%, 8 components) are the author's own; the paper does not give them.
  - The outcome rests on those counts, so it should be marked `assumed: true`.

## 2. Statements the printed outputs do not support

- **fig1k "6 to 8 of 11"** (neural cell 11, Summary cell 63, record notes, README via the Summary): cell 10 prints 8, 7, 8 and 8 of 11 under the claims file's windows, so the range is 7 to 8. The record's "With the median over channels, 7 to 8 of 11 match under every window" is wrong too: it is 8/11 under each window.
- **figs9, "with a fitted on the model data the paradigm 1 and 2 medians are 0.50 to 0.60"** (neural cell 59, record notes): cell 58 prints paradigm 2 medians of 0.20 to 0.50 and pooled medians of 0.40 to 0.60.
- **figs9 record notes:**
  - "No reading matches per paradigm" contradicts the same note's (1a)(2a) 3b combination, which meets the per-paradigm rule (cell 58).
  - "The passing medians sit at the edge of the tolerance" does not hold for (1b)(2a) 3b, which has pooled 0.65 and paradigm 3 0.50.
- **Neural Summary cell 63, figs9 "reproduced under one reading of many":** three combinations pass (cell 58).
- **fig6c, "about ten times smaller"** (model cell 16, record notes, the CDI finding's "ten times smaller"): model cell 15 shows speech 0.123 against 0.016 (7.7×), and fire and bird songs about 2.4× smaller.
- **fig9a, "spectro-temporal one at 100 ms (81.5%)"** (classifier cell 10, Summary cell 31, record notes): this omits the three-way tie in cell 7.
- **fig10, "the (6b)(7b) rows are at the same optimum (141 ms)"** (classifier cell 28, record notes): true only for spectral and temporal; spectro-temporal is at 100 ms, and reading (d) pairs by index.
- **Run times:**
  - Record verifications: "(38 min)". README: "model classifier notebook about 40". Classifier cell 32 prints 22.2 min.
  - README: neural "35 to 60 minutes". Neural cell 64 prints 29.9 min.
  - README: model "15 to 25". Model cell 24 prints 14.1 min.

All other sentences I checked in the Result cells, the Summaries, the README and the record notes match the printed outputs.

**My round-1 reasons:** the record's `reason` fields state them in my own words, faithfully, including points 5 to 8. For the fig9 claims, `agrees: false` with "blocked" correctly records that I rejected the "too_large" blocking.

## 3. Round-1 points

**Resolved:**
- **1:** the classifier was built and run.
- **2:** aMUA split-half values computed: 0.980 and 0.830 (neural cell 61).
- **3:** the code lines are printed. The line that defines `RASNA` is not shown, but the `sA` comment "First half (1.5 s)" supports the reading.
- **4:** reading 3b was run.
- **5:** the snake condition below chance is now flagged.
- **9:** P2_Site08's trial count is now in the findings.
- **Section C items:** tar listing, Param fields, fig4 temporal r per lag and per channel, and per-site a values.

**Acknowledged, unchanged, and no effect on any conclusion:** points 6 and 7.

**Still open and bearing on a conclusion:**
- **Point 8:** the criticalbandwidth.m variant for fig7i was written but not run. The model notebook is still the first-run execution, so whether the code's bandwidth would close the SI gap is untested. The record says so.
- **New, fig9a:** the tied spectro-temporal optimum (above).
- **New, fig10:** the index-paired difference in reading (d), resting on the tied 100 ms optimum (above).
- **New, fig9-spectrum:** the unmarked assumption about the spectrum classifier's counts, and the zero-point margin at full duration.
