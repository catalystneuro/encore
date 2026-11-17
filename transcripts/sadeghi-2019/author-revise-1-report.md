## Round-1 revision of sadeghi-2019-01

**The run.** I ran `python tools/entry.py all`, but it hit the tool's 2-hour limit before it finished. The classifier notebook (38 min) and the neural notebook (59 min) both completed, and both executed copies have no errors. The model notebook was cut off mid-run. With too little time left to re-run it, I restored its code to the committed version, so its executed copy from the first run still matches the code. I changed only its markdown.

Two consequences:
- **No stamp.** I wrote the conclusion cells after the run, so there is no clean-run stamp, and the next `run` will execute all three notebooks.
- **Classifier notebook timing.** It is about 40 minutes.

`tools/entry.py check` passes.

**What changed in the outcomes.** The verifier was right that the seven model-classifier claims were testable (B1). I built the classifier as a third notebook, `reproduce_sadeghi_2019_classifier.ipynb`. Only the held-out sound's category is refitted in each fold, as the verifier suggested. The seven claims are now tested:

| Claim | Outcome | Key numbers |
|---|---|---|
| fig9a, optimal resolution | reproduced, rests on readings (6b)(7b) | optima 141, 141 and 100 ms; other readings move them |
| fig9b, similar maximum | reproduced under the (7b) readings | 81.5, 82.1 and 80.5%; under (6a)(7a) one pair differs, p = 0.04 |
| fig9b, accumulation rate | partially reproduced | the order holds, the rise times do not |
| fig9c, time-averaged worse | partially reproduced | 15 to 37 points lower under reading (b), 5 under (a), never 25 |
| fig9e, category-specific | partially reproduced | 3 of 4 values; waves better spectral, wind better temporal |
| fig9, spectrum classifier lower | not reproduced | it matches the temporal classifier at the full duration |
| fig10, vocalization vs background | reproduced, rests on (6b)(7b), reading (a) | 93.3, 96.7 and −20.5; the spectral advantage is significant at only 1 of 10 durations |

At 141 ms, the PCs that explain 90% of the variance are 26 spectral and 8 temporal, the paper's counts.

None of the 21 neural and model-correlation outcomes changed. fig1k and figs9 are now marked as resting on an assumption.

**What I added or corrected in reply to the report.**
- **B2:** the aMUA split-half values for figs10 are now computed: 0.980 and 0.830, against the paper's 0.98 and 0.83. The claim stays blocked, because four of its six values need thresholded MUA, which needs raw voltages the data set lacks.
- **B3:** the fig1k cell now prints the window lines of NeuralExample.m, read from the deposit.
- **C:** the data check now lists every tar member and every field of the neural files. Only AnimalNo, BlockNo and RecordDate exist, which confirms both data_missing blocks.
- **B4:** figs9 now runs paradigm 2 reading (3b) and prints every site's a. Two more combinations pass, so I kept the outcome and noted that it depends on how a is chosen.
- **B5:** the notebook now flags the snake condition without tonotopy as significantly below chance (p = 0.012, against the paper's 0.92).
- **fig4 (C):** temporal r is now printed without lag 0 (0.888), without lags within 5 ms (0.693), and per channel. Lag 0 does not drive the high value. The outcome is unchanged.
- **Record:** the round is recorded under `verifications`, the README and summaries are updated, and I added a methods_unavailable finding about the classifier choices the Methods leave open. No question for a reader was needed: the verifier found no misreading of the claims file.

**What I did not do.**
- **B8:** I wrote the bandwidth variant for fig7i (the code's formula, 94 + 71 f^1.5) but removed it again, because there was no time left to re-run the model notebook. The verifier marked this point as not affecting a conclusion.
- **N_c search:** the cross-validated choice of N_c ran only at each classifier's optimum, over a subset of the 1 to 20 grid (1, 2, 3, 5, 8, 13, 20).
- **fig10 index pairing:** in the (6a)(7b) rows of fig10, the per-duration spectral-against-temporal tests pair two different optima by index, not by duration. The notes say so, and the outcome rests on the (6b)(7b) rows, where both classifiers are at the same optimum.
