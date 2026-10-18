I did steps 1 to 5 of the protocol and ran the handover (step 6). The entry checks with 0 errors and the notebook runs from a clean environment in 290 s. Nothing is committed. I used the preprint's full text (bioRxiv v1, CC BY), saved under `paper/`.

**1. Outcome per claim** (25 claims; counts taken from the attempt record)

| Claim | Outcome |
|---|---|
| cohort-sizes | not reproduced (10 of 16 group counts match) |
| fig2-gaba-excited | reproduced (t = 3.86 and 9.19; paper 3.8 and 9.2) |
| fig2-gaba-frequency | reproduced (Friedman 21.00 and 18.15) |
| fig3b-da-stn-250ms-peak | partially reproduced (0.786 s in the window I fixed beforehand; a narrower window gives the paper's 0.492 ± 0.033 s) |
| fig3c-da-stn-duration | reproduced (12.93, p = 0.0048; paper 13.0, p = 0.005) |
| fig3d-da-stn-frequency-ns | reproduced (4.20, p = 0.24, as in the paper) |
| fig3g-da-ppn-duration | not reproduced (p ≥ 0.25 under every reading) |
| fig3h-da-ppn-frequency-ns | reproduced (F = 1.35, p = 0.29) |
| fig4cf-ts-dls-opposite | reproduced (F = 40.9 and 36.4, the paper's values) |
| fig4dg-ts-frequency | reproduced (6 of 6 tests) |
| fig4eh-dls-frequency | reproduced (6 of 6 tests) |
| fig4eh-dls-5hz-increase | not reproduced |
| fig4cf-dls-rebound | partially reproduced |
| figs3-terminals-opposite | reproduced |
| fig5-vglut2-excited | reproduced |
| fig5-vglut2-frequency | reproduced |
| fig5-anxa1-dls-inhibited | blocked, data missing |
| fig5-anxa1-dls-frequency | partially reproduced |
| fig5-anxa1-dls-rebound | partially reproduced |
| figs4-anxa1-soma-inhibited | partially reproduced |
| fig5-opposite-subtypes | reproduced |
| 4 human tissue claims (Fig 1, S1) | blocked, data missing |

Totals: 12 reproduced, 6 partially reproduced, 3 not reproduced, 4 blocked. All claims are `data: dandiset`; no outside inputs were used.

**2. What was found about the dandiset**
- **No published version.** Only the draft exists; I pinned the draft as modified 2026-09-01T15:27:47Z (290 assets).
- **Contents.** 258 NWB files from 120 mice. Each file holds the lab's dF/F, the 465 and 405 nm signals and the stimulation epochs. Recomputing the dF/F from the stored signals agrees (median r 0.9999 in duration sessions, 0.9988 in frequency sessions). No recording is deposited twice. The stimulus responses lock to the true onsets in 235 of 258 recordings, so the epoch tables share the dF/F clock.
- **Anxa1 DLS recordings appear to be missing for 9 of the 18 mice.** The dandiset has DLS recordings for 5 (STN) and 4 (PPN) mice where the paper has 8 and 10, and SNc recordings for 8 and 10 where the paper has 5 and 4.
  - The paper's cell-body t-values are matched exactly by the SNc recordings of the 9 mice that have both a DLS and an SNc file.
  - The 9 extra recordings, which have no site in their file names, look like SNc signals. Adding them to DLS does not reproduce the paper's terminal statistics.
- **Smaller gaps.**
  - DA terminals in DLS have 8 mice (paper 9) and Vglut2 with STN stimulation has 9 (paper 10).
  - C4608 has no 4 s frequency block.
  - The human tissue counts and histology are not in the dandiset.
- **Metadata errors.**
  - The dF/F is labelled "a.u." but is in percent.
  - Every session start time has a -00:01 offset, so the true time zone is lost.
  - The files' description of the frequency sessions gives a 10 s interval between trains; the data and the Methods give 20 s.
  - The modulation frequencies are described inconsistently within each file.
  - Eight subject ids are lower case.
- **Differences from the Methods.** 13 mice have 10 trials per condition (Methods: 5), and 30 mice have 16 s trains the paper does not mention.
- **Code and paper.**
  - The conversion code labels one block as 10 mW where the files say 5 mW.
  - The conversion repo's Python dF/F code drops the intercept that its own description of the lab's MATLAB scripts includes. Those MATLAB scripts are not public.
  - The paper has a likely copied statistic (F1,11 = 12.8 given twice with different p-values) and two Friedman values that do not fit their p-values.

**3. Where the protocol was unclear, wrong or missing something**
1. **No published version exists.** The protocol only allows drafts for repeat attempts. I pinned `draft`, recorded its modification time, and the notebook checks whether the draft has changed since.
2. **Expected values with a 10% tolerance don't suit test statistics** (t, W, F), which depend on analysis windows the paper does not state. Outcomes rest on direction and significance; the paper's statistics are printed next to mine. Recorded in the claims file's opening comment.
3. **The 10% tolerance doesn't fit counts of animals.** I used 0 and gave the reason.
4. **A selection-dependent block where data are missing.** At the dandiset's n of 5 and 4, the paper's Wilcoxon tests cannot reach p < 0.05. The protocol's "too few units" category is `other`, but the cause is missing recordings, so I used `data_missing`.
5. **Labels against counts.** The paper's counts suggest the Anxa1 site labels are wrong, but the signals suggest they are right. The protocol says to trust the data. I kept the dandiset's labels for outcomes and showed the other reading as a variant.
6. **The data check ran into claim territory.** To examine the label question I looked at Anxa1 response medians before writing criteria. I disclosed this in the claims file.
7. **The clock check has no recipe for evoked photometry.** I compared responses at true onsets with onsets shifted by ±3 s, and named the 23 recordings where this could not be shown.
8. **The source hierarchy didn't fit.** The lab's analysis code is not public; the dandiset links only the conversion repo, which describes the lab's MATLAB scripts and re-implements them in Python. I treated it as "other software" and used its description only to fill gaps the Methods leave. Where it disagrees with the Methods, I followed the Methods.
9. **Test choice.** The paper picked parametric or non-parametric tests after a Shapiro-Wilk test. I used the test the paper reports for each comparison.
10. **Independence of the work.** CatalystNeuro curated this dandiset and wrote the conversion code, and is also the accountable party for this attempt. The protocol does not address this.

**4. Runtime and failures**
- The notebook takes about 5 minutes: 73 s streaming, about 195 s recomputing the dF/F for the data check.
- Loading first took about 10 minutes because h5py serializes threads. I switched to a process pool.
- Two bugs found while preparing, both fixed before the final run:
  - Some files store timestamps instead of a sampling rate, which crashed the first load.
  - Shifted onsets for the clock check could fall outside the recording.
- The final lock, check, run and handover all passed with no errors.
