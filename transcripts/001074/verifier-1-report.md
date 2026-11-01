**A. Outcomes** (47 claims in the claims file: 12 tested in the notebook, 35 blocked)

| Claim | My outcome | Reason |
|---|---|---|
| link-revision-well-order | reproduced | Cell 10: all 10 identification files have 11 wells of 93 frames and all dose files 15. Cell 11: 0.86 of cells rise most steeply in the first minute of a well, against a chance of 1/3; shifting the well onsets drops this to 0.23, 0.11 and 0.03. Cell 14: every sensor without crosstalk has 0.73 to 0.85 of its cells rising more in its own mixture. |
| fig1c-cells-per-gel | reproduced | Reading (b), curated masks (cell 16): 38 of 43 probes have a mean count in 90–220. Cell 17: cell centres fall in all three thirds of the depth in all 5 probes with an `mr-raw` file. Depth is bounded by the imaged z range (an assumption), and reading (a) cannot be tested. |
| fig1g-sensor-yield | partially_reproduced | Cell 19: median 9, 25th percentile 8 and 75th percentile 9 are all within tolerance. The cell count (559 in reading b, 382 in reading a, against 455–557) and cells per sensor per probe (6.82 and 4.72, against 5.42–6.62) are out under both labelling readings. |
| fig1g-all-ten-sensors-respond | not_reproduced | Cell 21: all 10 labels are present. But the mean trace is highest in its own or its partner's well for only 2 of 10 sensors by the per-well maximum, and 3 of 10 by the per-well mean. Even allowing the next well, CCK, NE and DA fail (DA peaks in the ATP well, which comes before the DA well). |
| fig1h-crosstalk-pairs | not_reproduced | Cell 23: NE–DA is the largest correlation (0.77), but AVP–OXT ranks 12th of 45 (14th with the 10-frame variant). 5HT–DA, DA–ACh and 5HT–NE all lie above it. |
| table1-ec50-on-target | not_reproduced | Cell 25: at most 2 of 10 within 10% under any reading (i to iv). Median \|log10 ratio\| is 0.12 to 1.49. |
| table1-ec50-off-target | not_reproduced | Cell 25: 0 of 4 within 10% under every reading. |
| table1-peak-dff-morse | not_reproduced | Cell 28: 4 of 14 (well reading a) and 5 of 14 (code's well, reading b) within 10%. MT is 0.56 against 0.30; CCK 0.49 against 0.40. |
| fig1j-ec50-consistent-across-probes | not_reproduced | Cell 30: reading (a) holds for 2 of 10 sensors and (b) for 6 of 10. Both fail, so this is not a split. With the noise cut, 7 and 8 of 10, still both fail. Per-probe values span orders of magnitude (DA from 69 nM to 1.05 mM). |
| figs3e-tau-on-under-one-minute | reproduced | Cell 32, with the CONSTANTS: 10 of 10 sensors under 60 s on dF/F0 and 8 of 10 on concentration. Both meet the 8-of-10 threshold. With the notebook's own fitted EC50s the variant gives 8 and 7 (a split), but those EC50s do not reproduce Table 1. |
| figs3f-depth-delay | not_reproduced | Cell 34: 5 of 10 slopes are positive in either depth orientation, against 9 needed. ATP is negative, but so are OXT, CCK, DA and ACh. |
| figs2f-cells-tracked | reproduced (marginal) | Cell 36: 44 of 72 probes (0.61) have a mean in 63–143, and the code's dipping set gives 8 of 10. Slice probes give only 5 of 11, and the probe set is not the paper's (see B11). |
| fig1d, fig1f, methods-revision-probe-stability, figs2c, slices-probe-stability | blocked (data_missing) | The archive holds only CaImAn traces and masks. There are no deformation fields or raw imaging. |
| figs6ef, fig4-ex-vivo-elevations, fig4-ex-vivo-two-orders-lower, figs6j, fig5gh, fig6, fig6c, figs6a | blocked (data_missing) | There are no photometry, ELISA, mass-spectrometry, choroid-plexus or histology files among the 713 assets. |
| 16 slice claims (fig2c ×2, fig2d, fig2e, fig2f, figs4de, slices-no-peptide-release, figs5c, figs5d, figs5f, figs5g, figs5i, fig2h, fig2i, fig2jk, fig2l) | blocked (metadata_insufficient) | 22 slice subjects exist, but there is no region label, wash-on, KCl, light or stimulation time, and no sensor label (cell 3: acquisition and stimulus are empty everywhere; timing is a 30 Hz placeholder). |
| fig3df, fig3h, fig4-ip-csf-concentrations, fig5ab, fig5cd | blocked (metadata_insufficient) | There are about 65 mouse subjects, but no injection times and no sensor labels. |
| fig3g-ten-sensor-yield | blocked (metadata_insufficient); part may be testable | It needs no timing, only labels on four ten-sensor in vivo recordings. Most mouse subjects have a post hoc `wells101` file (API listing). With the code's in vivo well order and probe list brought in, as the link claim did, the yield part could have been tried. The notebook does not discuss this. |

**B. Problems**

1. [affects a conclusion] `morse.label_clusters`: a cluster is labelled only if its mean derivative also peaks in the matched ligand's well. This rule is the author's own; it is not in the Methods and not in the stated assumptions (the module header states only the boxcar). It drops cells, so it drives the 382 and 559 cell counts and the cells-per-sensor figure in fig1g-sensor-yield. The administration boxcar (first minute of each well) is also an assumption.
2. [affects a conclusion] Cells 21, 23, 25, 28, 30, 32 and 34 use only the reading (b) labels (`LAB = lb`), although labelling was left open with two readings. Reading (a) is not carried into fig1g-all-ten-sensors-respond, fig1h, Table 1, fig1j, figs3e or figs3f. The large failures in fig1h and Table 1 are unlikely to flip, but this is unchecked.
3. [affects a conclusion] Cell 21 (fig1g-all-ten-sensors-respond): the per-well maximum or mean of a peak-normalized trace favours later wells when responses do not wash out between wells. The criterion as written is applied correctly, but the failure may come from carry-over rather than missing responses. DA peaking in the ATP well, before its own well, instead suggests poor DA labels; so do DA's high correlations with 5HT and ACh in cell 23. Label quality is never validated beyond cell 14.
4. [does not affect a conclusion] Cell 25, reading (iii): this is the Methods' reading, which the claims file says decides. It fits Eq. 9, which has no offset, to Eq. 28 plateaus whose low-dose value is not zero. It returns EC50s that sit on the fit's lower bound (shown as 0.0 to 1.5 nM). On synthetic data, an offset of 0.2 moves a true Kd of 700 nM to 262 nM. The reading is effectively broken, but every reading fails.
5. [does not affect a conclusion] Cell 25, off-target groups: they are normalized to their own peak well, not to the on-target maximum and the crosstalk ratio. Because F is free, this does not change Kd.
6. [does not affect a conclusion] Cell 30, reading (a): it is judged against the notebook's own consensus fits, some of which are degenerate (5HT 9.2 nM, MT 2.8 nM). Against Table 1 it still fails (5HT has a 1 nM probe; ATP reaches about 7 mM).
7. [does not affect a conclusion] `morse.tau_on` follows the code by fixing x∞ to the median of frames 47–78. On synthetic traces this underestimates long time constants: a true τ of 40 frames (77 s) is fitted as 24.7 frames (48 s). The bias favours "under 60 s" for figs3e. It is the specified method, but readers should know.
8. [does not affect a conclusion] `morse.remove_jumps`: the jump is measured at onset + 2 frames, after the decay has begun. On a synthetic jump of 0.5 it leaves a residual of up to 0.06.
9. [does not affect a conclusion] Cell 17 (fig1c): depth is tested on only 5 of 10 probes, and the gel thickness is taken as the imaged z range. The archive volumes have 15–26 planes, against the paper's 30.
10. [does not affect a conclusion] Cell 13: 559 of 829 matched cells are labelled. The paper reports 506 identified cells, so the cell pool differs from the paper's before any statistic is computed.
11. [affects a conclusion] Cell 36 (figs2f): two problems.
    - What a `matched<k>` file holds (one pair against a reference recording) is assumed and unverified. In probe 20230922-PL28 the "pair 0" files disagree (82, 96 and 99 cells).
    - The probe set covers all 72 probes, not the paper's S2F sets (dipping 40 recordings over 10 probes, slice 15, in vivo 25).

    The 0.61 result is marginal; with slice probes alone it is 5 of 11.
12. [does not affect a conclusion] Cell 0: the blocked reasons are stated only in the summary table. No cell shows per claim that the needed timing or labels are absent, beyond the global metadata survey in cell 3.

**C. What I could not check, and what output would have let me**

- Label validity. A per-cluster plot or table of the mean trace across the 11 wells, for both label readings, would have shown it. Also missing: downstream results under reading (a), and how many cells the "peak in matched well" rule drops.
- Whether the fig1g-all-ten-sensors-respond failure is carry-over. Per-sensor well-wise increments (the plateau of each well minus the previous well's plateau) would have shown it.
- Whether `mr-raw` really holds the curated masks and what `matched<k>` holds. The code's README, quoted, would have settled both. A cross-check of matched-cell counts against the code's printed counts per probe (morse_figs2_2 cell 4) would also have helped.
- fig3g. A listing of the mouse subjects that have post hoc `wells` files, with frame counts, would show whether the code's in vivo well order could be applied.
- The stability claims. The archive holds 13 revision-era in vivo subjects (2025, ZS…), matching the paper's "13/14 stable". This suggests only stable recordings were deposited, so no denominator can be tested; I did not confirm this.
- I did not re-run any cell or read any NWB content. All numbers above are taken from the notebook outputs. The helper functions were tested on synthetic inputs only.
