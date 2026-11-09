**Verifier report, round 2: attempt 000015-chen-2017-01 (Chen et al. 2017, DANDI:000015 0.220126.1914)**

Counts are taken from the files. The claims file has 33 claims and the attempt record has 33 outcomes with the same ids: 13 reproduced, 3 partially reproduced, 7 not reproduced and 10 blocked. The round-1 verification block has 33 results, 32 of them marked "agrees". Cell numbers below are for the re-executed notebook. The notebook has been renumbered since round 1: early-lick is now cell 17, not cell 14.

### 1. Outcomes

I agree with all 33 stated outcomes. All of them now match what I gave in round 1. The one I disagreed with, fig8d-error-outnumber-correct, has been changed to not_reproduced. That follows cell 74 under V1: reading (b) is at −1.81 SD with T1 and −1.70 with T2, against a bound of 2.

Comments on some of them:
- **ephys-selective-counts and fig7d-ephys-area-distribution:** these are now blocked_by "other", where I said data_missing. I accept "other". The reason given is the registry's rule about data the claims file places in another archive. Cell 14 prints the DataCite placeholder record.
- **figs4-peak-shift (not reproduced):** I agree under the criterion as written, but the criterion misreads the paper (see section 3).
- **fig8d-pt-earlier-than-it (reproduced):** I agree only because the criterion accepts a single combination. In cell 68 it passes in 2 of 16 combinations, both with T2 bins, rule S2 and the bootstrap over cells.
- **figs5-single-coefficient, fig4a and fig4b (reproduced):** these pass on the criterion only. Cells 32 and 35 show the permuted labels pass as well. This is a weakness of the claims file.

### 2. Statements the printed numbers do not support

- **Cell 30, and the attempt notes for fraction-selective-alm-mm:**
  - Cell 30 says "Rule R2 … with T1 bins comes closest: ALM 2,877 (32.6%) and MM 1,755 (26.6%) in window W1". The notes repeat this and put the W1 values in `measured`.
  - Cell 29 shows that window W3 is slightly closer on both MM values: MM 1,736 (26.3%), with ALM 2,853 (32.3%) still within tolerance. I made the same mistake in round 1.
  - Cell 30 also says "Under V2 … no other reading comes closer". This is false: under V2, W3 gives MM 1,656 (28.3%) against 1,675 (28.6%) for W1.
  - The outcome does not change, because the MM fraction is out of tolerance in every reading.
- **README row:** "PT selectivity earlier than IT … Reproduced (under one onset rule and bootstrap only)". The Summary (cell 92) has the same omission: "matches the paper only under one onset rule (S2) and only with the bootstrap over cells".
  - Both leave out the third condition, T2 bins.
  - With S2 and the bootstrap over cells, T1 bins fail (p = 0.021 and 0.170, cell 68).
  - The Summary table row in cell 92 and the attempt notes do state all three conditions.
- **Cell 92 Summary:** "ALM purely lick-direction selective at most 6.2%". This holds for T1 only; with T2 the peak is 6.45% (cell 50, 0.0645).
- **Cell 78 and the Summary row for fig8d-mm-object-location** ("the PT part of (a) holds if PT are deep"):
  - This reports only part (a). It leaves out the (c) quantity printed in the same cell (77): the MM PT maximum of mean |β| before the go cue is 0.523, against 0.112 for ALM PT.
  - On the same PT-deep assumption, part (c) requires MM PT to be below half the ALM deep maximum. To pass, the ALM deep maximum would have to exceed about 1.05, roughly nine times the printed ALM PT 0.112.
  - The MM PT bootstrap SD (0.617) is about the size of its mean, so these values are probably driven by a few outlier ROIs (my round-1 problem 1).
  - This does not decide anything, because the claim is blocked, but the statement reads more favourably than the printed numbers.
- **Cell 77, printed label:** "MM PT ROIs with F0 <= 0 on some trial: 47 of 334; by animal: an063 54 …, an064 280 …". The per-animal numbers are the totals of all MM PT ROIs (54 + 280 = 334), not of the 47. No conclusion uses this wrongly.
- **README:** "about fifteen minutes". Cell 93 prints a total runtime of 19.7 min.
- **README and Summary:** "never made public" (silicon probe data). The notebook shows only that the CRCNS DOI is a placeholder (cell 14). The attempt notes say no other copy was found, but that search is not run in the notebook.
- **Not checkable:** the Summary's statement that "five questions were answered, each with 'the paper does not say'". The questions file is not among my materials.

Every other "**Result:**" sentence, every attempt-record note and every finding I checked matches the printed outputs. I checked the counts, SD ratios, p-values, peak times, null values, per-mouse values, unit and trial counts and the DataCite text.

**My round-1 reasons in the attempt record:** they are faithful paraphrases. Where I gave no per-claim reason, the record fills in from my problem list:
- problem 1 is used under figs4-peak-shift and fig8d-error-outnumber-correct;
- problem 2 is used under fig4a and fig4c;
- problem 7 is used under fig4a;
- problem 8 is used under fig8d-pt-earlier-than-it.

Nothing is misstated. Two small points:
- The reasons cite the round-1 cell numbers, which no longer match this notebook.
- For the two ephys claims the record keeps my "data_missing" in the reason and marks "agrees: true", while it states blocked_by "other". This is consistent, since both say blocked.

### 3. Round-1 points

**Resolved:**
- **Problem 2 (chance-level selection measures):** the permuted-label null is now computed and disclosed for figs5 (cell 32, null 0.845–0.911 and above one half in all 59 bins), fig4a, fig4b and fig4c, and in the Summary.
- **Problem 3 (fig6-outcome-response-uniform (a) has no chance allowance):** disclosed in the notes.
- **Problem 5 (Li et al. baseline of two windows):** disclosed in cell 91 and the notes.
- **Problem 6 (testable parts not run):**
  - fig8ef: area is below projection type in every reading (cell 80), area above in 0.414 of resamples.
  - fig8d-mm-object-location (a) for PT is now run (cell 77).
  - Every text value of every plane is now printed and searched, and none gives depth or location (cell 7).
- **Problem 7 (no lick times):** BehavioralEvents holds only delay, go and sample in all 105 planes (cell 7).
- **Problem 8 (fig8d-pt-earlier-than-it fragility):** disclosed in cell 69, apart from the README omission in section 2.
- **Problem 10 (duplicate files):** three pairs were compared in full, and only the identifier and file creation date differ (cell 3).
- **Section C, CRCNS DOI:** the placeholder record is printed in cell 14.
- **Section C, V1 peak before the go cue:** now printed (cell 59).

**Remaining points that bear on a conclusion:**
1. **figs4-peak-shift window.** The paper says the peak "shifted from MM to ALM over the course of the delay epoch" (paper text, l. 326–327). The claims file's criterion leaves out "over the course of the delay epoch" and takes the peak over the whole −0.8 to 9.2 s window. I report this as a misreading by the claims file. If the peak is restricted to the delay or to before the go cue, MM peaks first in all four bin and dF/F combinations (V1 T1: 2.08 against 4.16 s). The other part holds in all eight combinations, so the outcome would become reproduced. The question has been asked and is not yet answered.
2. **dF/F outliers (problem 1).** These are accepted by the reader's answer, so V1 decides. Two outcomes are still sensitive to them:
   - fig8d-error-outnumber-correct passes under V2 with T1 bins (−2.20 SD).
   - fig8d-pt-contra-bias reaches 1.97 SD under V2.

   They probably also explain the implausibly large MM PT |α| and |β| in cell 77.
3. **Locations and depth.** These remain absent, so imaging-sample stays partial and the four depth claims stay blocked. That is correct as recorded.
4. **Rendered figures.** I still have not viewed them; I relied on the printed ranges.
