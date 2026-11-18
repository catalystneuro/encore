I've written `claims/mcguire-2016.yaml`. The quote checker reports 37 claims, 37 quotes, 10 statistical values and 0 problems. I made no commit.

**Text read.** The version of record, open access (PMC5004814, Europe PMC JATS full text). It includes the main text, the Methods, and the legends of S1 to S7 Figs, S1 Table and S1/S2 Data. No PDF was supplied. The paper links no code: its Methods name Matlab for the regression and Python with scikit-learn for the decoders, but publish neither.

**Claims.** 37 findings, every one with a quote and none inferred. 7 claims carry statistics (10 values), 37 have a criterion and 20 have expected values. They cover:
- **Behaviour:** Figure 2, S2 Fig, and the d-prime range of 0.5 to 1.5.
- **FSFS/SFFS task (Figure 3):** `data: elsewhere`, from S1 Data, because those rats were not recorded.
- **Recordings:** unit counts, baseline rates, temporal modulation, evoked modulation and latency by layer.
- **Regression:** the 204 significant units, the four unit classes, and their laminar fractions.
- **Fast and Medium units:** coding and adaptation (Figure 7, S4 Fig).
- **Slow units:** choice coding (Figure 8, S5 Fig), plus S6 head movement (`data: elsewhere`, from S2 Data) and S7 unit types.
- **Decoders:** Figure 9B to 9G.

**Details the paper leaves open, with the readings named:**
- **Temporal modulation window:** the Methods say 0 to 180 ms after nose poke entry, but also call it the stimulus period, and the stimulus starts 75 to 100 ms after entry. Readings: after entry, or after stimulus onset.
- **Permutation statistic:** not named. Readings: PSTH variance across bins, or summed squared deviation from the permuted PSTH.
- **Which units are classed:** the class counts sum to 305 (all modulated units), but only 204 had a significant regression. Readings: classify all 305, or only the 204.
- **The 55 ms window:** Medium in the Results, Slow in the Figure 6D legend. Both readings are named.
- **Evoked modulation:** signed or absolute extreme; impulses pooled, or one value per impulse and sequence.
- **Impulse-responsive t test:** one-sided or two-sided.
- **Latency summary:** mean or median across units.
- **Pre-sequence baseline window:** the 25 ms before onset, or 0 to 10 ms before.
- **Adaptation ratio:** mean of per-unit ratios, or ratio of population means. Test: one-sample t test against 1, or paired t test of pulse N against pulse 1.
- **Proportion test for FMS against SMF:** with or without continuity correction; and which trials count.
- **"Strongly related" (Figure 2C):** ordering by mean speed, or a Pearson r above 0.8.
- **Gradual firing decrease:** the slope of a linear fit, or the end of the period against baseline.
- **Sliding t-test window:** 10 ms in 1 ms steps, or 5 ms bins; "earliest withdrawal" as the minimum or the 1st percentile.
- **Decoder:**
  - Regularisation: scikit-learn defaults, or C chosen by 5-fold cross-validation.
  - Output normalisation: probabilities divided by their sum, or none.
  - Test against chance (Slow decoder, p = 0.47): fraction of repeats at or below 25%, or a binomial test.
  - "Abolished" (time-scrambled): not above chance, or below 32%.
  - Choice-decoder summary: mean of the four stimulus accuracies, or all trials pooled; test trials of each choice drawn balanced or in proportion.
  - "Primarily L5b" (Figure 9G): highest group mean, or majority of the top 10% of units.
- **Absence claims with no test in the paper** (Medium units, Slow Positive across sequences, S5 Fig): each uses a standard test (paired t test or repeated-measures ANOVA at 0.05), and each criterion says that choice is not the paper's.

**Missing from what was supplied:**
- **No PDF:** Figure 8D's three p-values (0.022, 9.5e-4, 7.5e-5) cannot be matched to layers from the text. They are recorded without that assignment.
- **Garbled Table 1:** its sequence columns don't line up with their headers. I read them as interpulse interval, duration, mean speed and rewarded port, and the opening comment says so.
- **Not in the text:** the contents of S1 Table and of S1/S2 Data. No claim rests on them alone, except the two `data: elsewhere` claims, which take their data from S1 Data and S2 Data.
- **Typo in the paper:** the Methods' "-Euclidean norm" is read as the L2 norm.
