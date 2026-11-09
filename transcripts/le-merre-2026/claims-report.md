I wrote `claims/001260/10.1038-s41593-025-02190-z.yaml`. The quote checker passes: 38 claims, 38 quotes, 0 problems. Nothing is committed. The dotfiles and `scripts/` that `git status` shows as untracked were not made by me.

**Text read.** The version of record (Nature Neuroscience, publisher HTML, open access) in full: main text, figure legends, Methods and the legends of Extended Data Figs. 1–9. There was no PDF, so values shown only inside figure panels were not seen; this includes most of the correlation coefficients. The bioRxiv preprint v1 was used only for comparison; no claim comes from it. The Supplementary Information file is missing (Supplementary Methods, Supplementary Figs. 1–2, Supplementary Tables 1–7), and so are the Source Data. I went ahead because the main findings rest on the main and Extended Data figures; each claim that cites a missing table says so.

**Code read.** github.com/hejDMC/pfcmap at commit 9ae52ed. It loads intermediate files from Zenodo 14205018. The code archive the paper cites (Zenodo 17559037) was not read.

**Counts.**
- 38 claims, all with quotes.
- 1 with a statistics entry: the only p-value printed in the text, R = 0.48, P = 0.002 (Fig. 5h).
- 38 with criteria, 10 with expected values.
- By data: 25 use the dataset, 9 use outside inputs (Harris and Gao hierarchy scores, IBL Passive), 4 use data held elsewhere (the IBL Brain Wide Map).

**Details left open, with the readings named:**
- **G1, groups for group control:** the code's five behavioral-setting groups (Opto merged into Passive), or six settings with Opto apart.
- **G2, which retrained category is which:** the code's ordering (memory rank, then a fixed permutation), or matching each cluster to the text's descriptions by its median metrics. Using the paper's own trained SOM from Zenodo is allowed only as a variant.
- **G3, unit quality:** the paper's criteria applied to the dataset's own quality metrics, or all units.
- **Waveform percentages:** 81.1% and 17.7% match a total of 23,667 units (the preprint's count), not the 24,248 given. Readings: all units, or ww plus nw only. This is recorded as a paper inconsistency.
- **ROI enrichment reference:** all PFC deep-layer units (the code), or all units.
- **Per-claim readings:**
  - "generally enriched": a positive summed E-score, or a significant category.
  - TH/HPF: each of categories 6–8, or any one of them.
  - "ILA-specific module": only ILA dataROIs, or all ILA dataROIs plus mostly ILA.
  - "recording session": one probe recording, or one session of up to 3 probes.
  - Stability: all transitions pooled, or averaged per transition.
  - Transition matrix: the P diagonal, or the coincidence-coefficient diagonal.
  - IBL grouping: none, or by recording.
- **Where Methods and code disagree:** the Methods are the main reading and the code is a variant. Cases:
  - the Harris correlation (code applies no group control);
  - ROI size (Methods 160–240 units, code 180–220);
  - the per-block minimum epochs;
  - extra conditions in the code's task-tuning test.
- **Settled by the code:** E-score significance is P < 0.05 two-tailed with no correction; regions and ROIs need more than 20 units; SOMs have 400 (ww) and 220 (nw) nodes. Seeds are not set in the code, so any seed is a standard choice.
- **Measures I fixed myself:** for figure-only claims (SOM gradients, PFC territory on the SOM) the paper gives no test, so the criterion uses a measure I chose and is marked as a deviation.

**Missing from the paper:**
- The test behind "firing metrics not different across behavioral settings" is not named anywhere in the text read. That claim is set to block as methods_underspecified unless a reader can name the test.
- The Supplementary Table 5 test (no hierarchy relationship within the PFC) is judged without knowing whether it was corrected for multiple comparisons.
- The ZETA test's resampling settings are given in neither the paper nor the code.
- Unit positions on the flatmap come from Gao et al.'s code, which is not public.
- The paper does not say which of the 99 recordings are in 001260 and which in 000473. The archive lists 74 files and 43 subjects for 001260, so it may hold only part of dataset KI.
