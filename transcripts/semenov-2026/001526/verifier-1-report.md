**A. Outcomes** (30 claims in the claims file. The notebook tests 5 and treats 25 as blocked.)

| Claim | Outcome | Reason |
|---|---|---|
| fig2cd-nonelectroporating-stable | partially_reproduced | The result depends on the background reading. With no subtraction (section 2.3 as written), 0 of 12 pre-exposure comparisons reach p<0.05 (smallest 0.057). With the annulus it is 1 of 12 (p=0.047), and with the background file 2 of 12 (cell 15). In every reading the cathodic 150 V/cm sets fall 26–39% below the first set (p 0.034–0.20), which does not look "constant". |
| fig2c-1000-within-set | reproduced (fragile) | Only with images 1–10 vs 51–60 and background subtraction: annulus gives 31.9→21.0%, p=0.051; background file gives 30.1→20.5%, p=0.126 (cell 18). It fails with no subtraction (12.6→8.2%), with F0 taken from images 2–40 (start 29.6%), and with windows (a) and (c), where p ≤ 0.01. |
| fig2d-lasting-reduction | partially_reproduced | Averaging both poles, the reduction is significant in every variant (p 0.011–0.042) but its size is 27–28% (sets 21–33%), outside 18–22%. The one literal pass (annulus, anodic pole, mean 18.0%, cell 20) averages per-set reductions of 2, 11, 30 and 29%. In that same background reading a cathodic pre-exposure set differs (p=0.047). |
| fig4d-short-pulses-same-limit | not_reproduced | Maximum pole \|dF\| is 34.9% cathodic and 34.0% anodic with the annulus, and 15.0% and 16.7% with no subtraction, against 53±4 at both poles (cell 22). The decline beyond the maximum, larger at the cathodic pole (0.82 vs 0.49), does hold. |
| fig5b-eq2-sensitivity | partially_reproduced | Eq. (2) is transcribed correctly; I checked it independently and get f=1.498 at the intact conductivity. A 100-fold increase gives 11.87% (within 10.8–13.2). A 10-fold increase gives 1.33% (outside 1.8–2.2); 2% needs about a 15-fold increase. The criterion has no partial clause. |
| fig1-pattern-poles-leaky, fig4b-di8-threshold-570, fig4b-first10-cathodic, fig4b-asymmetric-decline, fig4c-equator-cosine, fig7b-conditioning-sublinear | blocked (data_missing) | Confirmed in the archive: there is no 1 µs escalation. The 1 µs amplitudes are only 50, 70 and 250 V. |
| fig2a-fluovolt-saturation, fig2a-fluovolt-baseline-stable, fig2a-fluovolt-stable-electroporating, fig4a-fluovolt-limits | blocked (data_missing) | Confirmed: all 243 assets say Di-8-ANEPPS, as does the dandiset description. |
| fig2b-di8-climbs-to-570, fig2b-di8-bleaching-43, fig2b-di8-decline-within-set | blocked (data_missing) | Confirmed: there is no 43–1400 V/cm escalation group. The only 1000 V/cm 1 µs set belongs to the Fig. 2C group. |
| fig3-dye-slopes | blocked (data_missing), partly testable | The FluoVolt half cannot be tested. The Di-8-ANEPPS slope under reading (b) ("every cell of the dye at those fields") could be partly tested on the 150 and 230 V/cm sets of 11 cells. That needs an assumed pixel size (16 µm iXon pixel / 60× ≈ 0.267 µm). τ matters little at 900 ns (1−e^(−t/τ) ≈ 0.95–0.98 for τ ≈ 200–300 ns). |
| fig3-fluovolt-nonlinear | blocked (data_missing) | No FluoVolt, and no non-electroporating Di-8-ANEPPS data out to ±500 mV. |
| fig5a-gd-anodic-extension, fig5a-gd-linear-to-780, fig5a-gd-cathodic, fig5a-gd-significant-points, fig5c-gd-reduces-conductivity | blocked (data_missing) | Confirmed: no Gd³⁺ in any asset description. |
| fig6a-single-pulse-ca, fig6b-train-ca | blocked (data_missing) | Confirmed: no Fluo-4 recordings. |
| fig7a-test-pulse-cosine, fig7b-test-pulse-recovery, fig7c-fast-resealing | blocked (data_missing) | Confirmed: every asset is a single pulse per set; there are no two-pulse recordings. |

**B. Problems**

1. **[affects a conclusion]** Cell selection, cells 12–20 and `extract`. All 11 cells are used where the paper reports n=8. The notebook makes no attempt to find the paper's 8 and runs no sensitivity check. Four cells break the stated protocol: c3 and c4 before exposure, c1 and c11 after. The key p-values (0.047, 0.051, 0.030) are borderline, so leaving cells out could flip fig2cd, fig2c and fig2d. The same applies to the Fig. 4D session (8 cells against the paper's 10).
2. **[affects a conclusion]** Cell c4, `central_cell`. The analysed cell is the one nearest the image centre, an assumption the notebook never checks. c4 has the smallest radius (21 px), the weakest cosine amplitude (2.1) and a 150 V/cm cathodic dF of −2.2%. It may be the wrong cell or a cell that does not respond. It also produces the meaningless per-cell reductions (72%, 82%) in cell 20.
3. **[affects a conclusion]** Background reading, cells 9–22. Background is about 52% of the trace intensity, so subtracting it roughly doubles dF. No single reading reproduces fig2cd, fig2c and fig2d together: fig2cd passes only without subtraction, fig2c only with it. The notebook runs every reading but never says this.
4. **[affects a conclusion]** fig2d, cell 20. The only pass of the size criterion is a mean over per-set reductions that disagree (2–30%), chosen from 30 combinations of background × pole × summary.
5. **[does not affect a conclusion]** Field labels, `FIELD_1US` and `FIELD_03US`. Mapping amplitudes to labels by order gives V/cm per volt of 3.0, 3.3 and 4.0 (1 µs) and 3.6–4.15 (0.3 µs). That is not proportional, as a linear Sim4Life model would be. The files also give 1.00 mm electrode spacing against the paper's 1.6 mm. The Fig. 4D labels are said to come from the figure, which the claims file says was not read, and I could not check them. No outcome depends on the exact labels.
6. **[does not affect a conclusion]** `session_phase`. One median cathode angle is applied to every cell in a session, but the per-cell phases spread over 73–94°, wider than the ±5° arc. The loss is small (cos 10° ≈ 0.985).
7. **[does not affect a conclusion]** `trace_coords`. Points are 1° of polar angle apart, whereas section 2.3 resamples evenly along the perimeter length. This is a stated deviation and minor for round cells.
8. **[does not affect a conclusion]** Claims file. For fig2d, the legend says "≤20%" but the tolerance is symmetric (18–22%). Here the observed reductions are above 20%, so this does not change the outcome.

The helper functions pass synthetic tests: `cosine_phase`, `pole_index`, `per_image_pole_df` (with and without background), `profile_df`, `central_cell` and `membrane` on a ring image, `shift_between` and `parse_description`. The PEF onset at image 41 is confirmed by the step in pole contrast in the PEF files and its absence in the sham files (cell 8).

**C. What I could not check**

- **Whether the trace sits on the intended cell's membrane.** An overlay of each cell's traced perimeter and pole arcs on its baseline image would settle this, especially for c4.
- **Which 8 cells the paper used.** Re-running fig2cd, fig2c and fig2d without c3 and c4, and without all four cells that break the protocol, would show how much rests on cell choice.
- **The Fig. 4D axis labels.** The PDF could not be rendered here (no poppler).
- **The camera offset.** There is no dark frame in the data. Printing the baseline counts of a cell-free region, set against the camera's documented offset, would show which background reading is physically right.
- **The plotted figures.** I relied on the printed tables rather than the PNG outputs.
