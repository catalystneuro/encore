**Round 2 verifier report: keles-2024-01**

**1. Outcomes**

The claims file has 31 claims. The attempt record gives 28 reproduced and 3 blocked. No outcome in the record is marked `assumed: true`, so there are no assumptions to judge.

- **The 27 dandiset claims that are reproduced:** I agree with all of them. Every measured value and every tolerance check matches the printed outputs.
- **memory-cells-significant:** ACC is now 22/186, the paper's count. In round 1 it was 21.
- **memory-cells-significant, memory-cells-not-significant, and the cell column of memory-modalities-differ:** I agree with the decisions, with one reservation, which is point 3a below.
- **scanner-questions, reproduced:** I now agree. The claims file's `where` field names exactly the code repository's `scanner_questionnaire.csv`. The notebook ([63], [65]), README, Summary and notes now say the result comes from that file, not the dandiset, and is counted apart. I could not read protocol step 1.4, which the author cites, because it is not among my materials.
- **fmri-motion, fmri-tsnr, fmri-isc, blocked with `blocked_by: not_runnable`:** I agree. The raw BIDS data are public on OpenNeuro. What stops the test is that the fMRIPrep derivatives are missing and fMRIPrep cannot be run here. That fits `not_runnable` better than my round-1 `data_missing`.

**2. Sentences the printed numbers do not support**

- **hfb nb [10]:** "with nothing before onset". Cell [7] prints a largest pre-onset value of 9% of the peak (micro), 7% (macro) and 10% (units).
- **hfb nb [10]:** "so the offset is right to about a bin or two of 50 ms".
- **hfb nb [32] (Summary):** "correct to about 100 ms".
  - The sweep in [7] does not peak at 10.0 s. The counts keep rising to 10.25 s: micro 650 → 693 → 695, macro 683 → 715 → 724. Shifting the onsets also moves the analysis window relative to the response, so the sweep bounds the offset only to roughly 9.9–10.25 s.
  - The latency comparison puts the macro HFB 100 ms *ahead of* the spikes (200 vs 300 ms). That is consistent with a residual offset of about 100 ms but does not show one under 100 ms.
  - None of this affects nwb-contents, which only needs 10 s rather than 0 s.
- **Attempt record, nwb-contents notes:** "with at most 9% of the peak before onset". This is true for the HFB but not for the spikes in the same sentence (10%).
- **README:** "About 45 minutes" for `hfb_keles_2024.ipynb`. hfb nb [30] prints "notebook run time so far: 53.9 min".
- **reproduce nb [66] (Summary):** "the quality metrics, behaviour and selectivity counts match to the reported precision". That holds only under the chosen readings. Reading (a) of isi-violations ([21]) and reading (b) of missing gaze ([36]) fall outside tolerance.
- **reproduce nb [38] and the gaze-similarity notes:** "lowers its correlation from 0.737 to 0.834 to 0.290 to 0.317". The numbers match [36], but the sentence is garbled; it means from 0.737–0.834 to 0.290–0.317.
- **Code line citations:** the round-1 responses cite `gen_figure3_eyetracking.py` lines 120 and 130 for sigma. I cannot check these because the code is not available to me.

Every other "**Result:**" conclusion, both Summaries and the remaining notes match the printed outputs.

**Round-1 reasons:** the attempt record states them faithfully and in my own words for all 31 claims. My B3 (the shared-resample shortcut is acceptable) and the HFB-intermediates point from C appear only in the deviations and responses, not in any claim's `reason`. That is acceptable.

**Claims file versus the paper:** the claims file's confidence-accuracy statement says "significantly higher", while the paper's Fig. 3c legend says "significantly different". This is my round-1 B7. It is still unchanged and has been referred to a reader. It does not change the outcome: high is above low in 18 of 22 sessions.

**3. Round-1 points**

Resolved:
- **B1:** the starting_time text and checks are corrected (hfb [5], [9], [10]; reproduce [3]).
- **B2:** scanner-questions is now labelled as data from outside the dandiset.
- **B4:** every permutation test uses seed 0 (reproduce [52], [58]; hfb [12], [18]).
- **B5:** the projection-distance gap is explained in [27]: 1266 − 26 + 2 = 1242.
- **B6 and C "gaze sigma":** with sigma from the 27 kept sessions r is 0.754 ± 0.123 ([37]).
- **C "confidence-accuracy exclusions":** a per-session table with the reason for each exclusion ([46]).
- **C "HFB intermediates":** [4] prints the line-noise ratios (60 Hz median 51.9/8.0 before the filters, 0.08 after) and per-channel HFB statistics (|mean| ≤ 0.0004, s.d. 0.67–0.99).
- **C "LFP clock":** the offset sweep and latency check were added, with the limits noted in section 2.
- **C "fidelity":** the literal port in [61] gives the same bootstrap p as `observed_selection` for all 1266 memory cells and all 1450 event cells. That port is the author's, though; I cannot compare it with the original code.

Still open, bearing on a conclusion:

a. **Observed and null tests use different inputs (memory cells).**
   - `observed_selection` now uses rates (count/1.5 s), so ties between resampled means become floating-point near-ties, as in the code. `perm_null_counts` still runs on integer counts, where those ties are exact (`bmovie.py` lines 381–403).
   - In the code both steps use rates. So the record's "each cell's null decision has the code's distribution" does not hold for memory cells.
   - I tested this on synthetic Poisson cells (17 vs 17 trials, 5,000 resamples, 1,500 null cells at each of 0.3, 1 and 3 spikes/s). The rate path marks 4–7% more null cells as selective than the count path: 5.73% vs 5.47%, 5.80% vs 5.60%, 7.07% vs 6.60%. That pushes the memory-cell area p-values down; it is anti-conservative.
   - This fits the pattern in the outputs. Every memory-cell p is below the paper's: 0.0065 vs 0.015, 0.0005 vs 0.002, 0.014 vs 0.016, 0.227 vs 0.30, 0.135 vs 0.17 (reproduce [52]). The event-cell p-values, which have no rate/count difference, are close to the paper's ([58]).
   - The size of the shift (about +1 null cell in amygdala) suggests the decisions hold. The absence claims are only made safer by it. But this has not been shown for vmPFC (14 observed against a null 95th percentile of 12).
   - Running the null on rates would settle it.

b. **Literal port.** The match to the code's bootstrap rests on the author's own port, not the original scripts. The agreement of the Fig. 6/7 p-values and the exact counts still supports it.
