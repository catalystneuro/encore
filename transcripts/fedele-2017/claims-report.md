I wrote `claims/fedele-2017.yaml`: 20 claims. The quote checker reports 18 quotes, 19 statistical values and 0 problems. Nothing is committed.

**Text read**
- The version of record (PMC5653833, from the JATS XML): main text, Tables 1 and 2, figure legends and Methods.
- The supplement, which holds only Table S1 (per-channel rates). Its text kept the names and rates but lost the colours. I rendered the PDF page to read them: gray marks excluded channels, red marks resected channels, and green marks the HFO area of each HFO type.
- The linked repository, HFO-detect-matlab at commit f397367. It holds only the HFO detectors. There is no code for the FRandR overlap, the rates, the HFO area, the test-retest analysis, the outcome statistics or the spectral analysis, so those methods come from the paper alone.

**Claims**
- **Counts:** 20 claims, 18 with quotes. The other two (ripple and FR resection per patient, and the ripple and FR rows of Table 2) are marked `inferred`, read from the tables. 4 claims carry statistics and all 20 have criteria.
- **Coverage:**
  - The cohort, and nights and intervals per patient.
  - HFO amplitudes.
  - Follow-up time by outcome, a claim of absence (Wilcoxon p = 0.25).
  - Table S1 rates and HFO areas.
  - Patient 4 (Fig. 1), patient 17 (Fig. 2) and patient 1 (Fig. 3).
  - Whether the FRandR, ripple and FR areas were resected, patient by patient.
  - The Table 2 values for FRandR, ripples and FR, and that FRandR is more specific than ripples or FR.
  - The Engel class I results.
  - The seizure onset zone in the ETE patients.
  - Test-retest results for the whole group and by subgroup.
  - The spectral classes, and no TLE/ETE difference in them (a claim of absence).
  - Where the HFO area lay in patients 18 to 20.
- **Data:** every claim uses `data: dataset`. The resected channels come from Table S1 (red) unless the deposit marks them.

**Details the paper leaves open, with the readings named**
- **Channel rate over intervals:** (a) all events over total time, (b) mean of per-interval rates, (c) mean of per-night means, (d) a channel is in the area when it is in at least half of the per-interval areas. The Table S1 rates decide among (a) to (c); (d) is a variant.
- **Channels in the 95th percentile:** the non-gray channels or all channels. "Exceeds" is read as strictly greater; greater-or-equal is a variant. The percentile method is fixed by the paper (Matlab `prctile`).
- **HFO type behind the Table 1 test-retest values:** FRandR, ripples or FR.
- **Permutation null:** one per interval pair, or one pooled per patient.
- **Amplitude:** taken on the band-filtered or the raw signal, and pooled over all channels or only non-excluded ones.
- **Follow-up test:** rank-sum by normal approximation with continuity correction (main) or exact.
- **Chi-square test:** Pearson uncorrected, Yates, or Fisher. On the paper's counts, its p = 0.002 fits uncorrected Pearson, but its Engel p = 0.001 fits Yates or Fisher.
- **Confidence intervals:** Clopper-Pearson reproduces every printed interval except one bound (see below). The asymptotic method the Methods name for n > 10 is a variant.
- **Spectral analysis:** window centre, signal transformed, starting values for the gaussian fit, and what counts as a peak.
- **TLE/ETE spectral test:** the paper names none; chi-square is the main reading and a rank-sum test a variant.
- **TLE "irrespective of outcome":** read as all TLE patients pooled, because Table 1 itself gives 0.835 for the poor-outcome TLE patients.

**Inconsistencies in the paper, recorded in the opening comment**
- The specificity CI is 78–100% in the Results and 75–100% in the Discussion; Clopper-Pearson gives 75.
- The TLE test-retest median above conflicts with Table 1.
- The Fig. 1 legend labels PR as "posterior hippocampus left".
- Patient 19's grid is 4 × 8 in the Discussion and 8 × 4 in Table 1.

**Missing from the paper**
- The seizure onset zone channels are given only for patient 17 (Fig. 2B). The claims on the ETE patients' onset zone and on patient 17's onset zone need them; their criteria say so.
- The paper's own analysis code is not public.
