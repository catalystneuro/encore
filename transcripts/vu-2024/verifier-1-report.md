**A. Outcomes**

The claims file has 26 claims. The notebook tests 21 and marks 5 blocked, all with data held only on Zenodo.

| Claim | Outcome | Reason |
|---|---|---|
| fig1c-isosbestic-control | reproduced | Cell 43, session 2022-11-23: the 470/405 SD ratio is above 1 in 61/61 fibers, with median 3.01. The variant session gives 2.84. |
| figs2d-correlation-distance | reproduced | Cell 45: median pairwise r is 0.163 (below 0.3). r with tip distance is −0.190, p = 2.8e-16. |
| figs2ef-no-bundle-crosstalk | reproduced | Cell 47: the bundle-distance coefficient is −3.4e-5 per pixel, 95% CI −2.7e-4 to 2.0e-4, p = 0.77. The variant session gives p = 0.41. The CI still allows a change in r of about ±0.1 across the bundle. |
| fig1d-chronic-reward-stability | partially_reproduced | Cell 49: the weekly medians are 1.00, 0.90, 0.93 and 1.20, all inside 0.7 to 1.3. Only weeks 5 to 8 can be tested because sessions with 25 or fewer rewards end on 2021-09-21, so week 12 is never reached. With all rewards included, the median falls to 0.39 to 0.63 from week 9. |
| fig4-link-published-results | reproduced | Cell 19: raw light averages match exactly in all mice. Raw tone averages match exactly in all mice but DL18, and DL18's 14 matched tones also match exactly. Pooled spline r is 0.9957 (light) and 0.9922 (tone), and significance agrees on 0.936 of fiber and stimulus pairs. Per-mouse r falls below 0.99 for DL29 light (0.979) and DL27/DL29 tone. |
| fig4e-light-increases-widespread | reproduced | Cell 21: 240/280 fibers (86%) increase and 38 decrease. The notebook's chance rate is 0.024 per fiber, about 7 expected false positives. |
| fig4e-light-anterior-posterior-gradient | partially_reproduced | Cell 23: (a) rho = 0.168, p = 0.0047 holds and (c) Mann-Whitney p = 0.0013 holds. (b) fails: 0.83 of tail fibers increase against 0.86 elsewhere, Fisher p = 0.38, at all three tail boundaries. |
| fig4f-tone-tail-increase-anterior-decrease | reproduced | Cell 25: tail median 0.0092 against −0.0026 anterior, p = 5.5e-13, and 10/10 of the top fibers are in the tail. Anterior decreases outnumber increases 103 to 60, binomial p = 4.7e-4. The result holds with the code's lags and with DL18's 14 tones. |
| fig4f-decreases-lateral-ventral | partially_reproduced | Cell 27: DV holds (p = 0.003) but ML fails (p = 0.43). 79/245 anterior fibers (32%) show both a light increase and a tone decrease, which meets the "many" threshold. |
| figs4ac-patterns-consistent-across-mice | partially_reproduced | Cell 29: the tone correlation is negative in 7/7 mice. The light correlation is positive in only 4/7; the criterion needs 5. |
| figs4eh-patterns-not-movement | partially_reproduced | Cell 31: light holds (r = 0.873). Tone has r = 0.784, but in the deceleration split the anterior median is +0.0042, so the tone pattern fails. |
| figs5-isosbestic-no-pattern | partially_reproduced | Cell 33: light holds (415/470 median ratio 0.49; 2 significant fibers against 45). Tone fails on amplitude (ratio 0.68) even though significance drops from 18 fibers to 1. |
| fig5ab-response-latencies | partially_reproduced | Cell 35, Methods indexing: means are 187.5 ms (outside 221.6 ± 22.2), 271.7 ms (just outside 305.4 ± 30.5) and 393.2 ms (inside 428.3 ± 42.8). The order holds. The code's +1-frame variant gives 220.8, 305.0 and 426.5 ms, matching the paper to within 2 ms. |
| fig5g-light-latency-gradient | reproduced | Cell 37: rho(AP, relative latency) = −0.285, p = 7e-6, n = 240. |
| fig5h-tone-latency-gradient | reproduced | Cell 39: rho = +0.254, p = 3.3e-4, n = 196. |
| figs6cd-gradients-individual-mice | partially_reproduced | Cell 41: the tone correlation is positive in 6/7 mice. The light correlation is negative in 4/7; the criterion needs 5. |
| fig6-inclusion-counts | partially_reproduced | Cell 51: 22 locations (inside 24 ± 2.4) and 20 responders (inside 22 ± 2.2). Only 14 of 19 stimulated sites respond elsewhere, outside 18 ± 1.8. The striatal-label variant gives 24, 16 and 22, so it is still partial. |
| fig6gh-release-decays-with-distance | reproduced | Cell 53: b = −1.096 per mm, bootstrap 95% interval −1.325 to −0.890. Spearman rho on |ML|, |AP| and |DV| is negative with p ≤ 1e-5 on each axis. |
| fig6g-dorsal-spread | partially_reproduced | Cell 55: b is −0.971 dorsal against −1.403 ventral, in the claimed order. The difference has a 95% interval of −0.094 to 0.969, which includes 0. |
| fig6-tdtomato-control-no-response | reproduced | Cell 57: 0/304 (Opto4) and 0/203 (Opto9) significant increases, against 142/619 in Opto2 with the same test. The archive has 25 sessions; the paper reports 26 stimulations. |
| figs7a-photoswitch-confined | reproduced | Cell 59: the stimulated fiber increases significantly in 3/3 sessions, and 0 of 21 other fibers respond in each. The files label UG21's indicator as tdTomato (see B9). |
| figs1-no-tissue-damage | blocked (data_missing) | The archive's 180 assets are only .nwb and .avi files, with no histology. |
| figs3-targeting-errors | blocked (data_missing) | No CT or planned-target files. The fiber table holds the localized tips; whether it also holds planned targets is not shown (see C). |
| fig3-freely-moving-signals | blocked (data_missing) | None of the 16 subjects is a freely moving miniscope mouse. |
| fig7d-ventral-not-dorsal-jaw | blocked (data_missing) | No OptoD1 subjects in the asset list. |
| fig7ef-single-ventral-fiber | blocked (data_missing) | Same as fig7d. |

**B. Problems**

1. [affects a conclusion] Cell 31 (figs4eh): the split values are the signed extreme of raw DF/F over 0 to 1 s, with no pre-onset baseline subtracted. Each fiber's offset is therefore part of both splits, which inflates r(acc, dec). It also lets a baseline shift flip the sign of the anterior tone median, which is why tone fails in the deceleration split. This follows the criterion, but the tone failure may come from baseline level, not the response.
2. [affects a conclusion] Cells 23, 37 and 39 (fig4e gradient (a), fig5g, fig5h): the Spearman tests pool fibers across mice and ignore which mouse each fiber came from. Per mouse, the light correlations have mixed signs (4/7 positive for amplitude, 4/7 negative for latency). Relative latency is measured against the fastest fiber in each mouse, so its spread grows with the number of fibers. The pooled p-values are therefore optimistic, and a between-mouse confound was never ruled out.
3. [affects a conclusion] fig5ab is decided only by the indexing convention. The paper's means match the code's +1-frame indexing almost exactly, which suggests that is what the paper used. Under the criterion's Methods convention the claim is partial.
4. [does not affect a conclusion] `counts` (cell 51): `responders` includes the stimulated fiber's own significance, which can be photoswitching. That could inflate the 20 "responding recording locations". The count would need to drop to 19 or fewer to leave the tolerance, and the outcome stays partial either way.
5. [does not affect a conclusion] fig6-inclusion-counts: only 19 of the 29 single-site Opto2 sessions (21 in the striatal-label variant) stimulate an included fiber. The paper reports 24 stimulated locations, so the denominators differ and the "18" count cannot be compared directly.
6. [does not affect a conclusion] `stim_response`: the null pool excludes laser frames above 0.5 (epochs are detected at 0.4) and windows ending at each onset. It keeps the post-offset response windows, which makes the test slightly conservative.
7. [does not affect a conclusion] Chance level: the paper states p < 1e-6 for the 3-consecutive-frame test. The notebook's empirical rate is 0.024 per fiber (cell 21), so the paper's figure does not describe the test as run. It does not change fig4e (240 against about 7 expected).
8. [does not affect a conclusion] `spline_basis` at 18 Hz gives 9 basis functions, not the 13 in the Methods (checked on synthetic input), so the figs5 GLM is not the 13-df model. The figs5 amplitude criterion also compares medians of |signed peak|, which has a positive noise floor, so the 415/470 ratio cannot get close to 0 when the 470 signal is small (tone).
9. [does not affect a conclusion] Cell 15 text says 15 fibers carry the artefact in Opto2 230320f; the cell 13 table shows 13. UG21 is listed as tdTomato in the files and is treated as rDAm3.0 on circumstantial evidence. The paper's reward-response inclusion for that control cannot be applied, because UG21 has no reward events.
10. [does not affect a conclusion] Cell 19: the DL18 tone spline r and significance agreement are computed against a 44-tone fit, while the paper's fit uses 14 tones. They are not recomputed with the matched 14.
11. Checked and fine:
    - `half_max_latency`, `runs_of`, `nearest_index`, `laser_epochs`, `loco_lags` (lag sign) and `CueGLM` behave as described on synthetic inputs; a known response is recovered to within 0.007.
    - The 13-function basis at 30 Hz sums to 1.
    - Exact raw-average matches confirm the 11-frame tone shift and the fiber order.
    - The decoder's leave-one-out z-scoring has no leakage.

**C. Not checked**

- figs3: whether the fiber table holds planned target coordinates. Printing the FiberPhotometryTable column names would settle it. I did not open any NWB file.
- B4: a per-fiber list of Opto2 responders that leaves out the session in which the fiber itself was stimulated.
- B2: per-mouse or mixed-model versions of the AP tests, or the pooled Spearman after centering within each mouse.
- B1: the figs4eh splits with the pre-onset baseline subtracted.
- figs5: whether the paper's code uses 13 basis functions at 18 Hz. A run with 13 would show whether the tone amplitude ratio is sensitive to this.
- fig4-link: DL18 tone spline r and significance agreement with the 14 matched tones.
- The supplementary figure legends (S2, S4 to S7) were not available to me. I read the PMC author manuscript (saved in `paper/`).
