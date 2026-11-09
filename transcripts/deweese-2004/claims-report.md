I wrote the claims file at `claims/crcns-ac-2/10.1152-jn.00197.2004.yaml`, and the quote checker passes it: 23 claims, 23 quotes, 3 statistical values, 0 problems.

**Text read.** The version of record (PyMuPDF text under `paper/`), with its Methods, Results, Discussion and the legends of Figures 1 to 8. The paper has no supplement and links no code, so no code was read. I read the data descriptor only to know what the data set holds: the 33 anesthetized recordings with LFP, the 6 TTX recordings, and one awake recording that belongs to the 2006 paper and that no claim uses.

**Claims.**
- **Quotes:** all 23 claims have one. None needed `inferred`.
- **Criteria:** all 23 have one.
- **Statistics:** 3 claims have them.
  - The LFP CV comparison: Student's t-test, P > 0.5.
  - Private CV, large responses against all tones: "significantly lower". No test is named, so p < 0.05 is assumed from that wording.
  - Private variability, pentobarbital against urethane: "statistically significant". No test is named, so p < 0.05 is assumed.
- **Expected values:** most use the paper's SE as tolerance. Counts that identify a neuron, or that stand for "all but one", get a tolerance of 0 or 1, with the reason given.

**Details the paper leaves open, and the readings named:**
1. **Window for the PSP peak:** the whole trace after onset, or the 100 ms culling window.
2. **Span for the peak-to-trough culling threshold:** the 100 ms window or the whole trace.
3. **Variance in q:** N−1, with N as a variant.
4. **Negative scale factor rule:** applied to PSP-based culling too, or to LFP-based culling only.
5. **3 mV and 15 mV tone criteria:** applied before or after culling.
6. **Spike detection:** a standard threshold, named as a standard choice.
7. **Overfitting shuffle:** per neuron with 20 shuffles (standard choice), per tone as a variant.

Claim-specific open details:
- **Example neurons are not named.** Fig 2/3 is read as the lowest ⟨q⟩ with 26 tones above 3 mV. Fig 5/8 is the neuron with 63 trials of a tone. Fig 4 is the neuron where, for one tone, PSP-based culling removes 1 trace and LFP-based culling that trace and 3 others.
- **Tones that match no frequency in the set:** "32 kHz" is read as 31,118 or 34,448 Hz. "9.2 Hz" is read as 9,188 Hz.
- **LFP CV:** the more/less variable split is read as a rank split of 14/15 by total q. The CV is of LFP height, with the scale factor as a variant.
- **Veto correlation:** event size is either max minus min, or the peak relative to the 100 ms mean. The correlation is either per tone then averaged, or pooled with normalized heights.
- **Quantal comparison:** "within a factor of 2" is either ≤0.76 mV or 0.19 to 0.76 mV, against a reference of 0.38 or 0.39 mV.
- **Tests the paper does not name:** anesthesia (ANOVA or Kruskal-Wallis; t-test or Mann-Whitney), access resistance and depth (Pearson or Spearman), and the CV difference (unpaired or paired t-test).
- **Random culling control matched to both cullings:** read as the union of the trials the two remove. The neurons in the PSP-matched control could be 33 or 29, so both are run.
- **Private CV:** read as the square root of the residual variance divided by the mean height.
- **Rest potential:** the junction correction is 12 mV in the paper and 10 mV in the data set's notes. Each recording property also has an open measurement window.

**Missing from the paper that claims needed:**
- **No mEPSP detection method.** Detector, threshold and size measure are open, so `mepsp-size` rests on an assumed detector.
- **Garbled signs, and the PDF could not be rendered here.** The text prints =, <, >, minus and ± as a replacement character. Signs and relations are read from context: correlations as negative, "?15 mV" as above 15 mV, and value pairs as mean ± SE.
- **Anesthesia counts don't add up.** The Methods say 17 pentobarbital recordings, but the group sizes given with the values are 13, 3 and 17. I followed the group sizes.

Nothing was committed.
