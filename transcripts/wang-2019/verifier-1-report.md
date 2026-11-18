**A. Outcomes** (25 claims in the claims file: 15 tested in the notebook, 10 blocked)

| Claim | Outcome | Reason |
|---|---|---|
| fig1a-rabbit-hr-increase | reproduced | Cell 13: n=5, 140.2 to 237.2 bpm, paired t p=0.0011, 5/5 hearts. The dataset gives one SNS value per heart, so the window readings can't be told apart. |
| fig1d-mouse-hr-increase | reproduced | Cell 13: n=5, 364.8 to 488.0 bpm, p=0.0033, 5/5 hearts. |
| fig1bc-rabbit-ap-cat-response | reproduced (substitute hearts, majority reading only) | Cell 15: CaTD80 and CaT amplitude hold under the paired t-test (p≤0.02). APD80 fails the paired t-test (p=0.13 at 20 s) but falls in 4/4 hearts. The data are the first 20 s of the Fig. 2 series, not the Fig. 1 hearts. |
| fig1ef-mouse-ap-cat-response | reproduced (substitute hearts) | Cell 16: all four variables move in the stated direction under every window, by paired t-test (APD80 p=0.0002, CaTD80 p=0.04) and in 5/5 or 6/6 hearts. |
| fig2a-rabbit-monotonic | not_reproduced | Cells 18–19: mean HR peaks at 20 s and falls to 194.75 by 60 s, and the 50→60 s step is significantly the wrong way (p=0.047). CaTD80 bottoms out at 25 s and then rises. No combination of readings passes for all three variables; only APD80 is monotonic. |
| fig2d-mouse-biphasic-apd | reproduced | Cell 22: 50.52, 61.18 and 49.54 ms, all within tolerance. Peak at 15 s in 5/5 hearts. 15 s vs 0 s p=0.0002 (Holm-Sidak 0.0018); 60 s vs 0 s p=0.47. HR and CaTD80 monotonic under both readings. |
| fig2cf-cat-amplitude-similar | reproduced | Cell 24: amplitude rises in both species (rabbit p=0.0006 and mouse p=0.0002 at their best times). Similarity reading (b) holds at every time (unpaired p≥0.16). Reading (a) fails at 5–15 s. |
| fig3abc-tyramine-na-mimic-sns | reproduced (one reading only, for noradrenaline) | Cell 27: tyramine passes under both monotonic readings. Noradrenaline passes only under reading (b): HR drops 26.75 bpm between 29.75 and 59.75 s (mean), and APD undershoots baseline at the end (−3.2 ms, p=0.046). |
| fig3d-propranolol-abolishes | not_reproduced (per the criterion's rule) | Cell 29: APD80 at 10 s differs from time 0 by paired t-test (+1.43 ms, p=0.0101), and the RM ANOVA for HR gives p=0.031. Under reading (ii) no post hoc comparison is significant (min Holm-Sidak p=0.0875). The changes are small next to SNS alone (HR +16.7 vs +87.4 bpm; APD +3.5 vs +10.7 ms). |
| fig3e-rate-step-biphasic | reproduced | Cell 31: both conditions rise to a peak at 10 s and fall back. The peak rise is larger with SNS (14.8 vs 9.3 ms, reading a). Reading (b) fails (p=0.126). The record ends at 35 s, not 60 s. |
| fig3f-constant-pacing-sns-prolongs | reproduced (reading (a) only, on an assumed pairing) | Cell 33: SNS is above no-SNS at 0–20 s by paired t-test (p 0.002–0.036), both series shorten (−11.5 and −13.8 ms), and SNS is not biphasic. Reading (b) fails, the Welch variant fails at every time, and the pairing assumes columns are the same hearts. |
| fig4g-5f-rabbit-base-apex | reproduced (borderline) | Cell 35: base − apex −10.15 ms, 4/4 hearts, paired p=0.0482, using the authors' regions. The "cause of reversal" part can't be tested. |
| fig7f-mouse-base-apex | reproduced | Cell 35: base − apex +7.42 ms, 5/5 hearts, p=0.0019 (below 0.01). |
| fig4ab-rabbit-paced-shortening | blocked: data_missing | The workbook has no Fig4 or Fig6 sheet and no paced rabbit series (cell 5). The free-rate comparison half exists; the paced half does not. |
| fig4cd-activation-unchanged | blocked: data_missing | No activation maps. The archive's `files/` holds only code, derivative and docs; there is no primary folder. |
| fig4e-rabbit-repolarization-reversal | blocked: data_missing | No repolarization maps and no per-heart reversal table. |
| fig5c-rabbit-free-rate-reversal | blocked: data_missing | Same as fig4e. |
| fig6ab-mouse-paced-apd-prolong | blocked: data_missing | No paced mouse 20 s table. Fig. 3F (paced at CL 100 ms, 60 s) is a different protocol. |
| fig6e-mouse-repolarization-unchanged | blocked: data_missing | No maps. |
| fig6fh-mouse-cat-ap-uncoupled | blocked: data_missing | Pixelwise maps are needed. The whole-field opposite signs are already covered in fig1ef. |
| fig7c-mouse-repolarization-late-shift | blocked: data_missing | No maps. |
| fig8e, fig8f, fig8ij, fig9 (simulations) | blocked: other (questionable; see B1) | The notebook says "not runnable: MATLAB". But SPARC:212 itself contains both models, the AP-clamp voltage inputs and per-species instructions labelled "for reproducing paper results … (Figure 8)". |

**B. Problems**

1. [affects a conclusion] Cell 0, simulation claims. The claims file marks fig8e, fig8f, fig8ij and fig9 as data "elsewhere" and says the code sits behind a registration form. In fact the dataset holds it: `files/code/{mouse,rabbit}`, including the `masterCompute`/ODE files, `exp_APc_data_5Hz.mat`, `AP_2Hz.mat` and `instructions_*.txt`. That is a misreading of the dataset by the claims file. "MATLAB code" is not a data reason for blocking. Whether the code runs under GNU Octave was not tried, so these four may be testable, at least the Fig. 8 ones.
2. [affects a conclusion] fig3d, the claims-file criterion. "Not reproduced when any time point differs under either test" means 27 uncorrected paired tests on n=3, so at least one false positive is likely even with no effect. The outcome flips on a single test: APD80 at 10 s, +1.43 ms, t=9.86 because the SD is tiny. I report the criterion as written and flag that the rule is fragile.
3. [affects a conclusion] Cell 33, fig3f. Pairing no-SNS with SNS by column position is assumed. The empty no-SNS column 2 suggests the columns are aligned by heart, but nothing confirms it. SNS is already higher at time 0 (+2.69 ms, p=0.036), so reading (a) may reflect a difference between recordings and not an SNS effect. The unpaired Welch test fails at every time. The outcome rests on this assumption.
4. [affects a conclusion] Cells 15–16, fig1bc and fig1ef. The data substitute the Fig. 2 60 s series for the Fig. 1 hearts; cell 10 shows these are different recordings (the baseline HRs differ). Rabbit APD80 passes only by the majority rule (paired p=0.13). This is a stated deviation, but the outcomes should carry it.
5. [affects a conclusion] Cells 26–27, fig3abc. For noradrenaline the result depends on monotonic reading (b), which with n=3–4 and a missing value at 12.33 s has little power to flag a fall. The mean HR falls 26.75 bpm at the end.
6. [does not affect a conclusion] `against_time0`. Holm-Sidak is applied to separate paired t-tests, not the pooled RM-ANOVA error term that SigmaPlot's post hoc uses, and there is no sphericity correction. This is stated as an assumption. It changes reading (ii) for rabbit APD80 at 60 s (paired p=0.021 vs Holm-Sidak 0.18), but fig2a fails on HR regardless. On synthetic input the helper's paired p-values match `scipy.ttest_rel`, and `monotonic` flags a single reversed step correctly.
7. [does not affect a conclusion] Cells 8–9 and 31, fig3e. The 5 s no-SNS value equals the 0 s value in all three hearts (carried over), both conditions share the time-0 value, and the record ends at 35 s. The peak (10 s) and the end-of-record comparison are unaffected.
8. [does not affect a conclusion] Cell 35. The claims file's region readings (thirds or quarters of the map) can't be applied; the authors' own base and apex regions are used. That's a reasonable deviation, but rabbit p=0.048 is borderline, and with n=4 the Wilcoxon test can't go below 0.125.
9. [does not affect a conclusion] Cell 11. The deposited mouse APD80 at 60 s (49.54 ± 4.94 ms) is not the Abstract's 46.5 ± 9.1, so the deposit is not exactly the data the paper summarised. The mean is within tolerance.
10. [does not affect a conclusion] Cell 24. Similarity reading (b) is a non-significant unpaired test at n=6, which is weak evidence of similarity. Reading (a) fails at 5–15 s, the peaks differ (rabbit 30 s, mouse 20 s), and the mouse rise at 60 s is not significant (p=0.08). The criterion is still met.

**C. What I could not check**

- The raw workbook cells behind each table. I didn't download the workbook, and the notebook prints only text cells and summaries. Printing the raw numeric blocks (at least Fig3F with all 10 columns, and the tyramine and noradrenaline blocks with column B) would settle the Fig3F pairing and the meaning of the unlabelled time-offset column.
- Whether the Fig. 8 code runs. Printing `instructions_mouse.txt` and `instructions_rabbit.txt`, plus an Octave trial run of each `masterCompute`, would show whether fig8e, fig8f, fig8ij and fig9 are testable. Fig9 (total ICaL) is not obviously among the instructed outputs.
- Which window the Fig1 "SNS" value is (20 s, mean or peak). No dataset text says; printing any Fig1 sheet notes beyond the text cells already shown would help.
- How time 0 is defined in Fig3F relative to SNS onset, which matters for problem 3. Printing the per-heart values at 0 s for both conditions would show whether the gap at time 0 is consistent across hearts.
- The archive API reports 61 files against 58 in the version manifest. The extra files appear to be under `revisions/1` (about 33 kB, likely metadata). I didn't open them, so a listing of `revisions/` would confirm it holds no data.
