I checked the claims file for DANDI:001893 and made the changes below. I think it is ready for an attempt. Nothing was committed or pushed, and only `claims/001893/` was changed.

**Checker result:** `29 claims, 29 quotes, 24 statistical values, 2 problems`

Both problems are false alarms. They flag the value 0.0003 in `fig5g-switch-dorsal` and `fig6a-outcome-space`, but the paper prints it as "3.0 × 10 −4" and the checker looks for "3 × 10-4". I confirmed both values by reading the Results and the Figure 5g and 6a legends.

**Changes, by claim:**
- **`fig5jk-pl-switch`:** the source said paragraph 10. The section has nine paragraphs, and this result is in paragraph 9.
- **`fig5c-ignore-ventral`:** added the kNN cross-validated test from the Figure 5c legend (R2 = 5.57e-2, p = 8.4e-3), which the paper reports for the same finding.
- **`fig5g-switch-dorsal`:** added the kNN cross-validated test from the Figure 5g legend (R2 = -4.96e-2, p = 0.15). It is not significant, so leaving it out overstated the support.
- **`figs14k-tau-cortex-vs-spinal` and `figs14k-tau-cortex-vs-cerebellum`:** the IPFX settings are the first reader's own standard choice and could change the outcome. The test now also runs on the code's frozen per-cell values (the paper's own IPFX output). If the two give different outcomes, the claim is blocked as `methods_underspecified`.
- **New claims for coverage**, none testable on this dandiset:
  - `fig5d-ignore-on-anatomy-axes` and `fig5h-switch-on-anatomy-axes` (the r and p values from the Figure 5d and 5h legends)
  - `fig6h-outcome-groups-choice`
  - `figs4dg-cortical-coprojection`
- **Code:** I read `LCNE-patchseq-figures` at commit 79fa20a. Its `spikes.py` and `generate_S14jk.py` do what the waveform and time-constant criteria describe, including the two-sided Welch t-test.

The other claims match the paper: statements, sources, quotes, statistics and tolerances. The cell counts in `fig4g` are correctly left without statistics, because the t-test there only counts cells.

**Still open:**
- **`patchseq-ne-identity`:** the paper does not say how NE identity was confirmed. The marker readings in the criterion (Dbh, or four marker genes, detected at CPM > 0) are the first reader's own. The NeMO transcriptome collection is named only in the code's README, which says it was not used for the paper's figures.
- **Sweep inclusion:** the Methods' criteria need per-sweep bridge balance, bias current and noise. Whether the dandiset holds these is for the author to find out; the code applies none of them.
- **Minor findings without a claim:** the pupil results in Figure S16, Figures S15t and S17i, and Figure 4h. None is a main finding or in this dandiset.

**Ready:** yes. The checks entry is recorded with `ready: true`.
