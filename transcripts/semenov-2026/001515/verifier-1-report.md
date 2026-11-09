**A. Outcomes**

The claims file holds 34 claims (34 `- id:` entries). The notebook tests one and treats 33 as blocked (`data_missing`). Its table in cell 0 accounts for all 34.

| Claim | My outcome | Reason |
|---|---|---|
| fig5b-conductivity-calibration | partially_reproduced | In cell 15 the 100-fold rise gives 11.87% under reading (a) and 11.75% under (b), both inside 12 ± 1.2. The 10-fold rise gives 1.33% (a) and 1.20% (b), both outside 2 ± 0.2. The criterion needs both values inside tolerance under one reading, so the claim as written fails; the 100-fold value and the qualitative statement ("barely affects charging") hold. This matches the 1.3% the claims-file header computed. |
| fig2a-fluovolt-saturation, fig2a-fluovolt-stable, fig4a-fluovolt-cathodic-decline | blocked, data_missing | Cell 5 shows 70-frame files with one amplitude per subject. There are no sets of 40 baseline plus 60 pulse images and no within-cell field escalation (Methods 2.3). |
| fig3-dye-sensitivity, fig3-fluovolt-nonlinear, fig4a-fluovolt-limits | blocked, data_missing | No Di-8-ANEPPS files (cell 5: dye is FluoVolt in all 292). The FluoVolt half also fails: no frame delays, no V/cm, and no tau fit from [20], so IMPC (impedance) cannot be computed. |
| fig1-schwan-pattern, fig1-pole-dimming, fig2b-di8-climbs-to-570, fig2b-di8-bleaching, fig2b-di8-decline-within-set, fig2cd-stable-before-electroporation, fig2c-1000-within-set, fig2d-lasting-reduction, fig4b-di8-limits, fig4b-first-10-pulses, fig4b-cathodic-asymmetry, fig4b-poles-alike-570-780, fig4c-equator-follows-cosine | blocked, data_missing | Every criterion needs Di-8-ANEPPS recordings. All 292 files are FluoVolt (cell 5). |
| fig4d-short-pulses-same-limit | blocked, data_missing | All files use 1-µs pulses (`pulse_us` is 1.0 in all 292). |
| fig5a-gd-extends-anodic, fig5a-gd-linear, fig5a-gd-cathodic, fig5a-gd-differences, fig5c-gd-reduces-conductivity | blocked, data_missing | No Gd3+ group or parallel controls, and no Di-8-ANEPPS. |
| fig6a-ca-single-pulse, fig6b-ca-train-responders, fig6b-ca-650 | blocked, data_missing | No Fluo-4 imaging; every file is a FluoVolt StrobeImaging series. |
| fig7a-cosine-profiles, fig7b-charging-during-pulse, fig7ab-test-pulse-recovery, fig7c-fast-conductivity-drop, fig7c-full-reseal-mild | blocked, data_missing | No two-pulse recordings and no Di-8-ANEPPS escalation (the source of the Fig. 7B top panel). |

**Archive check.** I queried the DANDI API myself:
- Version 0.261006.1841 holds 292 assets, all `.nwb`, 7.47 GB in total. The only other version is the draft, with the same count and size.
- The dandiset metadata describes charging and discharging time courses versus cell size and field strength. That is the protocol of reference [20], not this paper's.
- The notebook's `assets()` keeps only `.nwb` files, but the API confirms there are no other files.

No part of any blocked claim can be tested under its criterion:
- Each subject has one amplitude.
- The electrode spacing is 1.00 mm, not the paper's 1.6 mm.
- The files record neither the frame delay nor the field in V/cm.
- The stated anode side does not fix the sign of the response consistently across sessions (cell 11), so the cathode-facing pole cannot be placed from the metadata.

**B. Problems**

1. [does not affect a conclusion] `strobe.f_factor`: I checked it against the paper's Eq. (2) (Methods 2.3, with the λm + ½λi term) and against an independent re-implementation. Both give the same results: f(3e-7 S/m) = 1.498, and f → 1.5 as d → 0. Reductions are 1.328% (10-fold) and 11.865% (100-fold). The code is correct; the mismatch at 10-fold lies in the paper's "~2%", not in the code.
2. [does not affect a conclusion] Cells 16–17: the grid over R and d is labelled a variant. It shows that no R in 5–15 µm with d in 3–7 nm puts both values inside tolerance. That supports a discrepancy inside the paper rather than an error in this analysis. The notebook does not test a different λi, λo or intact λm, but the criterion fixes those values.
3. [does not affect a conclusion] Cell 10: the estimate of about 50 ns per frame and 3.5 µs in total rests on an assumption (that the half-peak frames span the 1-µs pulse). The notebook says this is not shown by the data. It is used for no claim, and it cannot locate the 900-ns frame.
4. [does not affect a conclusion] `polarization_trace` and `response_window` use the notebook's own parameters (5th-percentile background, top-10% mask, top-minus-bottom index). The module docstring labels them as such, and they serve only the data check. I could not run them on synthetic stacks: numpy and h5py are not installed here.
5. [does not affect a conclusion] Data-quality findings, cells 7 and 11:
   - One file under subject CHO-20230926-c1 has a 2024-12-16 session start and a different field of view.
   - Nine files have the sign of the opposite stated anode side.
   - The species field names two species, and the age "P1D" is given for a cell line.

   These are metadata defects only; they matter for no claim, since all of those are blocked.
6. [does not affect a conclusion] Claims file: it does not misread the paper on any claim tested here. Its header expected Di-8-ANEPPS and 900-ns escalation sets in this dandiset. The notebook correctly finds the dandiset holds the FluoVolt time-course protocol of reference [20] instead.

**C. What I could not check**

- I could not run the pixel-level helpers myself (no numpy or h5py in this environment, and I was not allowed to download). So cells 7–13 (cell counts, signs, the amplitude ordering with Spearman ρ = 1.0) are taken on the notebook's word. Two additions would have let me verify them independently:
  - a printed per-file table of `peak`, `peak_frame` and `n_cells`;
  - a figure of one file's mean image with the mask overlaid.
- The notebook does not print the full set of distinct session-description strings. That list would confirm directly that no file mentions Di-8-ANEPPS, Gd3+, a second pulse or a sine exposure, rather than relying on the regex fields of `parse_description`. My count of the dye field rests on the regex.
- I did not look at whether the sister dandisets 001516–001518 (named in the claims-file header) hold the missing series; they are outside this round's scope.
