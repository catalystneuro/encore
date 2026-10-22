The checked file is fit for an attempt, and the last check has `ready: true`.

**Checker result:** `claims/001676/10.1038-s41586-025-10096-w.yaml: 32 claims, 32 quotes, 34 statistical values, 0 problems`. The first run, before my edits, gave 31 claims, 35 statistical values and 0 problems.

**Changes, by claim**
- **fig1f-example-stable:** the source said Results paragraph 3 was paragraph 2; fixed.
- **edf1e-hd-proportion:** the entry labelled "animals 1 to 5" held only animal 1's ROI mean. I added the ROI means for animals 2 to 5 and the recording count for each animal, which the criterion already said must match.
- **edf1h-ring:** the criterion now says its circular-correlation test is the reader's, not the paper's, and is recorded as a deviation.
- **edf4c-previous-session:** added the per-animal V values from Extended Data Fig. 4d, and a criterion that uses them.
- **edf4g-pairwise-offset-stable:** tolerances were 10%, but the legend gives an s.d. with each median, and the protocol says to use the stated spread first. I switched to the s.d., as fig2e and edf7 already do, and dropped the reader's 3-degree-bin clause.
- **fig2h-coherent-remapping:** the test now uses only the three same-room environment pairs of Fig. 2i, where the paper measures alignment in room coordinates. The open field becomes a variant. The 80% and 30° thresholds are now marked as the reader's.
- **fig3e-mvl-delay:** the source now includes Fig. 3d, where the mvl values are printed.
- **fig3fg-probe-drift:** the criterion called the legend's ±0.1 a standard error, but the legend says s.d. I reworded it to say so. The 10% tolerance stays, with its reason given, and the ±0.1 band is also to be shown.
- **edf9-interference:** removed the statistics entry. It recorded p < 0.05, a value the paper never prints.
- **fig4d-single-visit-memory:** removed the CellReg 0.6 reading, because the Methods allow 0.6 only for Fig. 3. I named the shuffle the Methods use and gave median and mean over the shuffles as the two readings.
- **edf10c-environment-identity:** n now reads "10 values, read as 5 mice by 2 environments". W = 7 with p = 1.0 fits 5 pairs.
- **edf2ab-jaccard (new):** the Results say the Jaccard index stayed high regardless of the delay between sessions, and no claim covered that.

All the paper's other main findings already have claims, and every claim comes from this paper.

**Still open (also listed in `checks`)**
- **Reader-set thresholds:** several criteria rest on thresholds the reader chose where the paper gives no test. These are roi-counts, edf4ef, fig1k ("up to 20 days except one"), edf4ij, the edf9 "reduced retention" comparison, the fig2g splits and the edf2ab 80%. They are recorded as deviations but can't be settled from the paper.
- **Animal order:** Extended Data Fig. 1g names animal 4 as the Fig. 1 mouse. But that mouse's V (17.06) matches the second value in Extended Data Fig. 4b, not the fourth (14.6), so the animal order there can't be settled.
- **fig3fg tolerance:** the legend's s.d. of 0.1 for both drift rates is implausibly small for four mice.
- **edf1e tolerances:** the proportions are printed to one decimal, but their s.d. values (0.03 to 0.05) are smaller than that rounding.
- **Supplementary Tables 1 and 2** are not under `paper/`. No claim rests on them.

Nothing was committed or pushed.
