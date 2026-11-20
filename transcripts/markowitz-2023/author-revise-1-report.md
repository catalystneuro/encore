I've made the round-1 revision of `markowitz-2023-02`. Both notebooks re-ran from a clean environment with `tools/entry.py all` (photometry 1,756 s, optoda 347 s), and `tools/entry.py check` reports 0 errors. Nothing is committed.

**Outcome changes**
- **ed3c-keypoint-velocity: partially reproduced → reproduced.** The criterion says to process dLight as the fig_s03 notebook does, and that notebook fits the reference without an intercept. With that fit, r = −0.167 and −0.019, both within tolerance.
- **fig2g-usage-crosscorrelation: partially reproduced → not reproduced.** I now compare the observed peak with each shuffle's peak over all lags; this reading is recorded as an assumption. That gives P = 0.093 and 0.221. A circular-shift null that keeps the autocorrelation gives P = 0.68. This agrees with the verifier.
- **fig2k-dlight-predicts-sequence-variability: blocked → reproduced.** It is now tested, with details the claims file leaves open taken from the paper's code (dlight_06, fig_2k). The result is P = 0.001 at n = 5 and 10 under both binnings. The raw correlations are negative; they are positive only relative to the shuffles.
- **fig3i-optoda-entropy: reproduced → not reproduced.** I acted on the verifier's point about sample-size bias. With stimulation trials drawn down to the catch-trial count, the Opto-DA effect disappears (first-bin Holm P 0.86 to 1.0 across the five seeds). This is marked as an assumption.
- **fig3jk-post-predictable: partially reproduced → not reproduced.** The criterion has no partial case, and the intervals include 0 under all five seeds. This agrees with the verifier.
- **fig4i:** still blocked, but the reason changed from data missing to other, as the verifier said. The main block is the decoding models that were not run.

**Kept against the verifier's view**
- **fig1f-syllable-vs-movement-onset stays reproduced.** The verifier was right that most detections did not start from stillness. I now keep only detections preceded by relative stillness. With those, reading (a) gives 13 of 14 mice, P = 0.00024. Under either definition of movement initiation, one reading meets the criterion. The outcome is marked as resting on that stillness rule.
- **ed10i-no-place-preference stays reproduced** on the criterion's tests (P = 0.174 and 0.425). The verifier's point that the claims file misreads "experiment-wide" is now a question for a reader in `questions/markowitz-2023.yaml`. Under that reading P = 0.005.

**Corrections and added outputs**
- **Baseline set:** 38 dLight+ChrimsonR files are the baseline day of one target and the post day of another, and I had misclassified them. The fix brings the DLS baseline set to 164 experiments (from 145), and every DLS number was recomputed.
- **Clock check:** a per-mouse check shows the same best label shift (−3 samples) in both DLS groups and in DMS. The clock ranges are also printed.
- **Quality-control rule (b):** this reading was never run before. It leaves 64 DMS experiments, the paper's count. I ran it for fig1f, fig1h, ed7, ed7b and ed7d; no outcome changes.
- **Other fixes asked for:**
  - fig1e: fixed the shuffle count and added two variants (whole-second bin sizes, no sliding z-score).
  - fig2h: added a check that the window overlap does not explain the significant neighbouring offsets.
  - fig2e: the per-segment counts are now printed.
  - fig3e: added the Monday-baseline variant.
  - fig3e-learner-count: added the overlap with the paper's nine learners, fetched from its code at the pinned commit and listed under `inputs`.
  - fig3m: added trial counts and the light timing.
  - ed10i: the JSD now handles empty histograms, and arena coordinate ranges are printed.
  - fig2a: the spontaneous half is now computed.
  - ed10d: the stimulation counts behind the block are printed.
- **Finding withdrawn:** I removed a wrong finding. The 60 files with a light-to-detection gap are the 3-s pulsed files, so the gap is expected.
- **Record:** the full round-1 verification is recorded, and I added three questions for the paper's authors.

**Not done**
- fig1l: I did not run a reduced random forest. For a claim of absence, a smaller forest loses the power the test depends on.
- ed10-target-specific, the encoding and decoding models, the fig4 claims and fig5 remain blocked as not run.
- ed2a reading (b) is still not pooled across all open-field files.
- Five-seed ranges are still missing for several claims; the record says which.
- About an hour was lost when a test command hung on my own process check; that cost the time these remaining items would have taken.
