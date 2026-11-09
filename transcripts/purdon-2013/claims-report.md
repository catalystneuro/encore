I wrote `claims/001285/10.1073-pnas.1221180110.yaml`. The quote checker passes: 22 claims, 22 quotes, 0 problems.

**Text read:** the version of record from PubMed Central (PMC3607036). That covers the main text, the figure legends, the Methods and the Supporting Information PDF (SI Methods and Figs. S1 to S3). The main PDF was not supplied, so I could not look at the main figures; every claim rests on a sentence of the text. Two equations were lost in extraction: the modal projection and the smoother's state variance. I read both from the words around them and say so in the criteria. The paper links no code, so none was read.

**Claims:** 22 findings, all with quotes.
- **Statistics:** 5 claims carry them. Four record the sign test (p < 0.05, 10 subjects) and two record the permutation test of the modal projection; one claim (`fig2-emergence-reverse`) has the sign test only. I left out the "P < 0.05 in 9 of 10 subjects" phase-amplitude tests, because there p is a per-subject threshold used to count subjects; the counts are under `expected` instead.
- **Criteria:** 22. 11 claims also have expected values: the 10/10, 6/10, 9/10, 8/10 and 9/10 subject counts, the five-number summaries of the EON to LOC and ROC to EOFF durations, the traveling-peak frequencies and bandwidths, and the more-than-10-fold rise in low-frequency power.
- **Tolerance:** 10% throughout, except subject counts, which get one subject either way. The reason is in each criterion.
- **Coverage:** behaviour (Fig. 1), spectra (Fig. 2), the traveling peak (Fig. 3, Fig. S2), coherent alpha modes (Fig. 4), the two phase-amplitude patterns (Fig. 5) and the broadband modulation of Fig. S3.

**Details the paper leaves open, with the readings named:**
- **A. What counts as a response:** (a) the button matches the stimulus type, or (b) any button press.
- **B. Point estimate of the response curves:** posterior median or posterior mean. The model's priors and sampler settings are only in refs. 31 and 74; standard choices will be recorded as deviations.
- **C. Baseline period:** (a) the recording before the infusion, or (b) the first 0 µg/mL level.
- **D. Baseline spectrum:** mean or median over the baseline windows.
- **E. Laplacian:** the 4 nearest neighbours with (a) inverse-distance or (b) equal weights. Standard positions with Euclidean distances stand in if the digitized positions and MRI are not in the dataset.
- **F. Excluded channels:** the dataset's bad-channel marks; Fz, or the nearest kept channel.
- **G. Sign-test sides:** cannot change the outcome, since with 10 subjects both versions need 9 of 10.
- **Band limits:** gamma and beta are given differently in the Results and in the figure legends; both definitions are run.
- **Spectral time windows:** what share of a window must be significant; the window for "at LOC"; the start and end points of the traveling-peak transitions.
- **Traveling peak:** how "total power-normalized" is combined with the group median.
- **Modal projection:** the unconscious segment, either the whole LOC to ROC period or the 5 min after LOC.
- **Phase-amplitude analysis:** the filter design and the permutation test are only in ref. 36. Readings are FIR or Butterworth filters, and a circular-shift shuffle scored by the Tort modulation index or by the largest bin. The windows "within 10 min of LOC" and "about 15 min before ROC" are read either as any 2-min epoch or as the pooled window.
- **Lag step of Fig. S3:** 0.1 s or 0.25 s.
- **My own thresholds:** "frontal", "distributed broadly", "moved" and the "Fig. S3 modulates" rule are not stated in the paper. Each criterion names its rule as such before any analysis is run.

**Missing:** no claim lacked text it needed. The main-figure PDF is not here, so the figures could not be checked visually. Refs. 31, 33, 36 and 74, where the paper puts some method details, are outside the text; the readings above cover what they would fix.
