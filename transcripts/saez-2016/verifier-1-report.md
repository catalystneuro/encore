**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| dataset-size | reproduced | The Summary sheets mark exactly 14 IC, 14 VC and 26 VCB cells as included, and 9, 11 and 12 as excluded (cells 7 and 23), which matches the paper and the Methods. The VCB test files are in pA, so the bicuculline cells are voltage clamp. The archive itself holds complete recordings for only 10 IC and 10 VC of the 28 control cells; that limits the claims below, not this count. |
| fig1c-control-outcomes | partially_reproduced | Only 20 control cells could be measured: 2–4 LTP, 3–4 LTD and 12–14 NC depending on reading (cell 25). The counts out of 28 meet the partial clause (6 plastic, 22 NC) only under (a,a), (c,a) and (c,b), and only if the 8 missing cells are filled in from the authors' sheet values. Measured on its own, the plastic fraction is 6–8 of 20, about twice the paper's 4 of 28. |
| fig1-control-no-net-plasticity | reproduced | One-sample t-test on n=20: p = 0.65, 0.75 and 0.54 under (P) a, b and c (cell 27), so no reading finds an effect. This rests on using the last 120 baseline sweeps; with the first 120, p = 0.0496 and 0.035 in (a) and (c). |
| fig1-control-mean-change | partially_reproduced | Under (c), VC −4.36, IC +0.46 and combined −1.95 are all within tolerance, but the SD of 14.13 is outside 10.26 ± 1.03 (cell 29). Computed on 20 of 28 cells. |
| fig1-vc-ic-same | reproduced | No reading has any of the four tests below 0.05; the smallest p is Shapiro-Wilk on IC, 0.15 (cell 31). n = 10 + 10. |
| fig1fh-control-no-dependence-on-initial | reproduced | Pearson p ranges from 0.099 to 0.285 across modes and readings (cell 33). |
| fig1d-example-nc | reproduced | IC6 gives −0.94% (p = 0.47) under (a) and −1.07% (p = 0.41) under (c), both within −1 ± 0.1% (cell 35). With the first-120 baseline variant, IC6 is −22%. |
| fig2a-bicuculline-outcomes | partially_reproduced | No reading gives exactly 7/9/10. (a,a) gives 8/8/10, and (a,b), (c,a) and (c,b) also meet the partial clause (cell 37). |
| bicuculline-increases-plastic-fraction | partially_reproduced | The bicuculline fraction is larger in every reading. The bicuculline count is within tolerance in four readings (16 or 15 of 26), but the control count, at 6–9 of 28, is never within 4 ± 0.4 (cell 39). |
| fig2-subgroup-changes | partially_reproduced | At most 2 of 3 means are within tolerance: LTD and NC are, but the LTP mean is 80–89% against 39.9% (cell 41). VCB17's +400% causes the LTP failure (see B1). |
| fig2-mean-unchanged-variance-increased | partially_reproduced | The t-test p is 0.45–0.52 in every reading (equal means hold), and the F-test p is far below 0.01 with the bicuculline variance larger. The bicuculline mean (+10 to +13) and SD (about 84) are far outside tolerance, again because of VCB17 (cell 43). |
| fig2cd-example-ltp-ltd | reproduced | VCB29 gives +60.1% (p ≈ 3e-65) under (a,a), and VCB10 gives −36.9% (p ≈ 1e-34) (cell 45). |
| fig2f-bicuculline-no-dependence-on-initial | reproduced | Pearson p = 0.44, 0.44 and 0.48 under (P) a, b and c (cell 47). |
| fig3a-ks-scs-vs-ecs | blocked (data_missing) | I listed the bucket myself. `pvc-9/` holds only `live/` (abfload.m, checksums.md5, data.tar.gz, filelist.txt, docs/) and `ftpup/crcns_data_description.docx`, and filelist.txt agrees. The tar contains only the three ECS folders and three xls files (cell 49). Every test in this claim needs the SCS data, so no part can be run. |
| fig3c-random-mixing-narrower | blocked (data_missing) | Same reason: both the simulation and the input count need the SCS strengths. |
| fig3b-segregation-near-complete | blocked (data_missing) | Same reason. |

**B. Problems**

1. [affects a conclusion] **VCB17 is mismeasured** (`peak_amplitudes`; cells 15, 17, 41, 43). VCB17's response after the stimulus is less than twice the same measure taken before it (cell 14). Its measured baseline amplitude is 98 pA, against −579 pA in the authors' sheet. Its change comes out at +400%, against the sheet's +62.9%.
   - On synthetic white noise (SD 30 pA, no response at all), the peak-in-window measure returns 83–99 pA. So VCB17's 98 pA is roughly what noise alone would give, and its +400% is not a credible measurement.
   - This one cell sets the bicuculline mean and SD and the LTP subgroup mean.
   - Without VCB17, reading (b) gives mean −1.77, SD 31.56, t p = 0.93 and F p = 0.0026. All parts of fig2-mean-unchanged would then pass.
   - Without VCB17, the LTP mean is within tolerance in every reading. Substituting the sheet's +62.9% for VCB17 gives an (a,a) LTP mean of about 37.9%, which together with the LTD and NC means would also reproduce fig2-subgroup-changes.
   - The notebook flags VCB17 but keeps it and has no rule for an unmeasurable response. Two outcomes depend on this choice.

2. [affects a conclusion] **Eight missing control cells are filled in from sheet values** (cell 25, `fig1c` and `bicuculline-increases-plastic-fraction`). The notebook classes the 8 cells it cannot measure from the authors' sheet changes, not from data. Elsewhere the sheet and the notebook's measure disagree by more than 5 points in 12 of 46 cells; IC13, for example, is −12.8% in the sheet and +20.8% measured. The partial outcome for fig1c exists only because of this fill-in. The notebook states it as a deviation.

3. [does not affect a conclusion] **The pre-pairing epoch is an author choice, not a claims-file reading** (`cell_epochs`, `pre_reading="last"`; cell 19). The Methods wording and the sheets (3.8% vs 23.8% median difference) support using the last 120 sweeps, so the assumption is reasonable. But under the first-120 variant, no-net-plasticity fails (p < 0.05) and the control mean drops to about −11%. Readers should know the control-group outcomes depend on this choice.

4. [does not affect a conclusion, unverified] **The stimulus can be located at the artifact's offset** (`stimulus_indices`). It takes the largest |diff| in the window. On a synthetic square artifact it located the offset in 2 of 5 sweeps. That shifts alignment by 0.5 ms and pulls artifact samples into the 10 ms baseline: the amplitude came out at 5.0 instead of 2.7. Cell 12 reports stimulus times rounded to 1 ms, which cannot show this jitter.

5. [does not affect a conclusion] **Inclusion is read from red fill only** (`read_summary`, `_is_red`). Any row that is not red counts as included; green fill is never checked. The counts match the paper exactly, so this is low risk.

6. [does not affect a conclusion] **IC13 is unexplained** (cells 16 and 25). It is +20.8% measured against −12.8% in the sheet, has only 77 post-pairing sweeps, and is LTP under every (T)(b) reading. No trace inspection was done.

7. [does not affect a conclusion] **Possible VC/IC label swap in the paper** (cell 29). The sheets' own IC values (−5.79 ± 9.51, n = 14) match the paper's "V-clamp" figure (−5.67 ± 9.47) more closely than its "I-clamp" one. The claims file does not raise this. Under (c) the outcome is unchanged either way.

The claims file reads the paper faithfully. I found no misreading beyond the label question in point 7. The paper states no chance levels for any selection.

**C. What I could not check**

- **Whether VCB17 has a real response.** Adding a per-sweep plot of its median trace and holding current, plus its measured amplitude with a longer baseline, would settle it. A rule-based exclusion (for example, after/before ratio below 2) with all outcomes rerun under it would show how much the bicuculline claims depend on this cell.
- **Alignment jitter.** Stimulus times at 0.05 ms resolution, and the sign of the detected step (onset vs offset), would show whether point 4 occurs in the real data.
- **The IC13 discrepancy.** Its per-sweep amplitude series, pre and post, with the sheet's green-marked sweeps, would explain it.
- **Inclusion marking.** A per-row fill-colour table (green, red or none) for the three Summary sheets would confirm it.
- **Whether control classes depend on the sheet-based fill-in.** A per-cell table of the sheet's one-tailed p and change for all 28 control cells, set against the measured classes for the 20, would show this.
