**Checker result:** `claims/001750/10.1038-s41556-026-02009-4.yaml: 34 claims, 34 quotes, 19 statistical values, 0 problems`. Before my changes it was 30 claims, 15 statistical values, 0 problems.

I read the paper (Results, legends, Methods) and the paper's code repository at commit 44cd8a6. The code details the Fig. 4d criteria cite do match the repository: the 17-step limit (`nTraces = 17`), the `ranksum` and `ttest2` tests, the absolute value in pA, and a table of 35 cells (14 VEN, 21 PC).

**Changes, by claim**
- **fig4d-sodium-current-lower:** I rewrote baseline reading (a2) to match `Fig4d_plotNaCurrent.m`. The code subtracts the mean of the first 100 samples of a cut that starts 2 ms before the step. That is 2 ms of baseline at 50 kHz and only 1 ms at 100 kHz, not "the 2 ms before onset".
- **model-sd-na-density:** The statement said the 55 to 80 pS/um² range was "set by the recordings". The Extended Data Fig. 7c legend says it was "defined by experimental data and previous publications", so I corrected it.
- **model-na-ratio:** The criterion now cites that same legend: 55 pS/um² may not come from the recorded ratio alone.
- **fig5-ven-sparse-connectivity:** I added "no input from interneurons (IN-to-VEN, 0 of 55)" to the statement and the quote, as the Results report it.
- **fig7c-tau-rna-distance:** The criterion now says which pairs enter: all projection types with mapped Patch-seq neurons, following "Pooling the pairs across all clusters". The paper gives no minimum number of cells per type.
- **New claims** for main findings that had none:
  - `ext7d-ais-length-no-effect`: AIS length has no effect on AP shape in the models.
  - `ext7i-basal-dendrite-diameter`: VENs have thicker basal dendrites, which the Results give as the likely cause of their stronger response to deep-layer input.
  - `fig2df-l23-it-tau-width`: L2/3 IT HPCAL1 neurons have a small time constant and narrow APs.
  - `fig3f-ais-distance-types`: AIS distance from the soma compared across Patch-seq subclasses.

**Open**
- **ext7d:** The Results say AIS length had no significant effect "in either model". The Extended Data Fig. 7e legend gives p = 0.0038 for PC AP width. The claim records both, and the PC width slope does not decide it.
- **model-na-ratio:** The medians in the code's own table (14.9 pA VEN, 29.3 pA PC) give a ratio of about 0.51, outside the tolerance around 55/80 ≈ 0.69. The paper does not say whether 55 pS/um² was set from the ratio alone.
- **fig3c-ais-distance-length:** The legend does not name the factors of its two-way ANOVA, and the code only plots the data, so both readings stay.
- **fig4j-eepsp-amplitude:** The Fig. 4j script runs no ANOVA, so the repeated-measures question stays open with both readings.
- Supplementary Tables 1 to 12 were not in the text, so the values for `ven-firing-rate-variability` and the new Fig. 2 and Fig. 3f claims cannot be read.

**Ready:** yes. The last check entry has `ready: true`. Only the claims file was changed; nothing is committed or pushed.
