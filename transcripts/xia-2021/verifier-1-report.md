**Verifier report: Xia et al. 2021 (PNAS 118:e2023807118), round 1**

The claims file has 29 claims. The notebook tests 9 and treats 20 as blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig2d-hplc-yield | not_reproduced | The main-peak share is 66.6% (flat baseline) or 65.8% (0.5% detection), outside the 69.3–84.7% tolerance (cell 21). Reading (b) gives a negative share (−367%), which means nothing. The 7.58 mL main peak comes from a flow rate picked to match the paper (problem 1). The peaks elute in the right order: the second/main retention ratio is 1.191 against the paper's 1.213–1.227. The share failure is marginal and depends on where the outer peak limit is placed (problem 2). |
| fig2e-page-bands | reproduced | Ethidium lane 3 has two bands (rows 511 and 593) above lane 1's scaffold band (row 878). Lane 3's fluorescent bands at rows 783 and 861 carry AF647 at 8 and 10 SD above the gap between lanes (cell 23). The lane order matches the legends of Fig. 2E and S2C. |
| figs5-btx-staining | reproduced | By eye, cell 25's render shows discrete AF647 puncta spread over the ganglion and on the rims of GFP+ somata (low magnification). The supporting numbers are weak: puncta lie within 1 µm of GFP at or below chance in 3 of 4 images (problem 7). |
| fig3d-sensor-on-soma | partially_reproduced | Both channels show puncta, and pHAb puncta lie over the somata. But AF647/pHAb overlap is no better than with the pHAb mask shifted by 5 µm (0.84 vs 0.82, 0.98 vs 0.98, 0.85 vs 0.80; cell 27). The share inside the soma mask is at or below the mask's share of the field. Check (b) is below 0.5 in all 5 images (0.16–0.47). In the render, yellow spots sit mostly between or at the edges of somata. |
| fig4b-michaelis-menten | not_reproduced | None of 80 readings is within tolerance: Km 0.03–0.73 µM (paper 49.24 ± 5.84), Vmax 8.3–49.7 %/s (paper 281), R² ≤ 0.73. Rates do not rise steadily with concentration (2.7, 0.3, 1.9, 4.9, 16.3, 12.2, 3.6, 3.6 %/s; Spearman p = 0.17). Caveats: only one of three mice is deposited, there is no 7.14 mM point, and the onset is inferred from the data (problem 8). |
| fig4b-lod | not_reproduced | None of 160 crossings falls in 205–251 nM. Baseline noise is 1.77 ± 2.34% (SD) or 1.17% (step), against the paper's 0.088%. Signal-to-noise at 228 nM is 0.40 or 0.61, against 8.18 (cell 31). |
| fig5b-in-vivo-response | not_reproduced | dF/F at 15 s is 17.1–37.3%, against 3.33–4.07%; none of 72 readings and none of 34 cell-sized blocks fits on both dF/F and rate. sub-2 is still at 11–15% at 120 s. The 28 readings flagged "rate_ok" are an artefact (problem 3). The paper's three mice are not identified in the deposit. |
| fig6-vesamicol | partially_reproduced | Only one of four experiments is deposited. In it, the drug/washout ratio is 11.3–29.9% (24 of 48 readings within 15.3–18.7%), and the reduction is within 65–88% in 44 of 48 readings. Within-experiment paired t gives p ≤ 4.9e-11. The four-experiment mean and test (a) cannot be computed. Cell-sized blocks give 0 of 13 within tolerance (median 36.8%) (problem 13). |
| figs16-af647-stable | reproduced | In all 6 readings the AF647 maximum rise (0.38–3.70%) is within the pre-stimulus mean + 3 SD. The pHAb/AF647 rise ratio is 14–135, at least 5 (cell 37). This rests on the assumption that the left half is AF647. |
| fig2g-conjugation-ratios | blocked (data_missing) | Agree. The deposit has spectra of the sensor and the scaffold only, with no pure AChE or BTX spectra, and the criterion says the claim is untestable without them. |
| figs3-size, fig3bc-retention, figs4-stability, figs7b-in-vitro-reversibility, figs13-two-photon | blocked (data_missing) | Agree. The manifest has no AFM images, bare-DNA images, 0 h/5 h images, dialysis-fiber data or two-photon files. |
| figs6a-response-time | blocked (metadata_insufficient) | Agree. sub-1 keeps only the first frame's timestamp and no addition time, and the criterion forbids taking the onset from the response. |
| figs6b-unit-calibration, fig5c-ach-concentration | blocked (data_missing / dependency) | Agree. sub-1 is one channel (509×255) with no AF647 and no AF647 calibration. |
| fig4c-control-ph, fig5b-control-minimal, figs8-control-10v, figs10-control-8v | blocked (data_missing) | Agree. None of the six subjects in SPARC:108's subjects.xlsx is a control-nanosensor or pH experiment. |
| fig5c-voltage-dose, fig5d-pulse-dose, fig5e-reversibility | blocked (data_missing) | Agree. There is no 5 V recording; 10 V (sub-4) is a different mouse; no 10- or 50-pulse files are deposited. Whether sub-4 holds repeated stimulations was not shown (section C). |
| figs9-aqua-vs-roi | blocked | Agree that it is blocked, since the claim compares against AQuA by definition. The reason "not_runnable" is not one of the allowed reasons; it should be "other". |
| fig7-rostral-caudal, fig7-peak-timing | blocked | The 8 V recording (sub-3) is deposited, so part of each could be tested. Block-wise onset and peak times on sub-3 could test the onset order and the 10–15 s time to peak, though not with AQuA. The reason should be "other". |
| figs12-3v-propagation | blocked | Part could be tested. The amplitude comparison in the mouse stimulated at both voltages is already in cell 10: sub-2 at 3 V peaks at 27.1%, sub-3 at 8 V at 48.1%, so 3 V is lower. Propagation could only be checked in sub-2; the two 3 V-only mice are not identified in the deposit. |

### B. Problems

1. **[affects a conclusion]** Cells 20–21, fig2d. The 0.5 mL/min flow rate was chosen as "the rate at which the peaks fall at the paper's volumes". The main-peak volume test is therefore circular. The paper gives the column (Superdex 200 Increase 10/300) but no flow rate, so only the retention ratio is actually tested.
2. **[affects a conclusion]** Cell 21, `peak_limits`.
   - The outer limit is where the signal returns to pre-injection + 3 SD, which is 29.76 min. That attributes a low tail (about 0.2 over roughly 9 min, by eye from the plot) to the second peak.
   - Ending the second peak at the end of its own descent (about 21 min) would move the share to roughly 69–70%, at the tolerance edge (my estimate; not computed).
   - Reading (b) draws a straight line from the 5.3-high valley to 29.76 min, which produces negative areas. No sensible variant of (b) was run.
3. **[does not affect a conclusion]** Cells 33 and 35, `initial_rate` k2–k5. The windows start at frame 19, but the responses start at frames 23–34 (cell 10). The k-rates therefore measure baseline or the post-stimulus dip (as low as −7 %/s). The "rate_ok" flags in fig5b come from averaging such values.
4. **[does not affect a conclusion]** Cell 33, `response`. Bleach reading (a) treats frames from 120 s after onset as recovered, but sub-2 is still at 11–15% there, so the exponential fit absorbs part of the response.
5. **[does not affect a conclusion]** `dff`, all movie cells. No camera offset or background is subtracted, even though off-tissue pixels sit at about 1,550 counts. This understates dF/F; correcting it would move fig5b further from 3.7%.
6. **[affects a conclusion]** Cell 27, `background_threshold`. Defining the background as the pixels at or below the median puts 32–48% of the field above the pHAb threshold, so "overlap" is nearly guaranteed. The shifted null shows this, and fig3d should not count as reproduced on the overlap numbers.
7. **[does not affect a conclusion]** Cell 25, `puncta`. The detector finds 2,122–26,603 "puncta" (up to 64 per 100 µm² in one plane), which is mostly noise. The near-GFP shares therefore do not test the claim; the by-eye judgement carries it.
8. **[does not affect a conclusion]** Cell 14 / 29. The onset is the frame before the largest one-frame rise. That is the same inference the claims file calls circular for figs6a, and at 0.00714 and 0.0714 µM there is no step, so the onset is noise. The 0.000714 µM recording rises 23% in one frame, more than 0.714 µM, which suggests the steps may be artefacts of adding ACh. Km is off by more than 60-fold under every reading, so the outcome stands, but it is weakly founded.
9. **[does not affect a conclusion]** Cell 31. LLOD reading (c), the split shown in Fig. 4B(ii), was not run, though the claims file names it. The fitted rates make a crossing near 228 nM unlikely.
10. **[affects a conclusion]** Cell 0 table. "not_runnable" is not an allowed blocked reason. As listed in section A, figs12's amplitude part and parts of the two fig7 claims are testable from the deposit.
11. **[does not affect a conclusion]** Cell 35, test (b). A paired t test over 219–241 autocorrelated frames treats frames as independent replicates, so the p-values (down to 1e-103) say nothing about significance. It is still the claims file's reading.
12. **[does not affect a conclusion]** In `xia2021.py`, the module docstring says the ROIs are blocks of "`BLOCK` pixels", but `BLOCK` is the 1 MiB read size (`BLOCK_PX` = 40 is the block size). The 0.43 µm per pixel estimate is unverified; the files carry no spatial scale.
13. **[affects a conclusion]** Cell 35, fig6. The example ratio depends on the ROI: tissue with a mean baseline gives 22%, the whole frame 15.6%. The paper's ROI is a single cell (Fig. 6A), and the cell-sized blocks give 0 of 13 within tolerance (13–45% among responsive blocks). The 17% part is reading-dependent, which is one reason the outcome is partial.
14. **[does not affect a conclusion]** Cell 11. The left/right channel assignment is inferred from the response; the files do not label channels. figs16 is not circular, because a rise in both halves would still fail the test.

Helper checks on synthetic data: `initial_rate`, `fit_mm`, `two_line_crossing`, `bleach_correct` and `dff` all recovered the known values. The claims file does not misread the paper anywhere I checked: the 17% and 76.59% for fig6, the 3.7% and 0.294 %/s for fig5b, and the gel lane legends.

### C. What I could not check, and the output that would have let me

- **fig2d:** the pHAb-channel share with the second peak ending where its descent ends, and a linear-baseline variant with sensible limits. Also the signal level from 20 to 30 min.
- **fig3d:** I could not see the paper's Fig. 3D (no PDF renderer here), so my by-eye judgement compares against a downscaled render. A full-resolution crop with each channel shown separately would help, as would the top-hat overlap against its own shifted null.
- **fig4b:** a plot of each sub-1 tissue trace with the inferred onset marked, to see whether the one-frame steps are responses or artefacts of adding ACh.
- **fig5c / fig5e:** the full tissue trace of sub-4 (10 V), to see whether it holds one stimulation or three repeats. That would decide whether any part of fig5e can be tested.
- **fig7 / figs12:** per-block onset and peak times for sub-3 and sub-2 as a map. That would test onset order, time to peak (9–16.5 s) and the 3 V propagation direction without AQuA.
- **All movie cells:** the dark-pixel (camera offset) level per file, to judge how much the missing background subtraction matters.
