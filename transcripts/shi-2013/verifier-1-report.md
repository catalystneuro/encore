**Verifier report, round 1: Shi, Apker & Buneo 2013 on CRCNS ppc-1**

The claims file has 28 claims. The notebook marks 25 as tested and 3 as blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| behavior-mean-position-sessions | not_reproduced | Cell 24 gives 16.1% under both readings, against 6.9 ± 1.5%. Monkey X only (8 target percentages, not 16). This rests on record fields 19–21 being the trial mean over the hold, which was never checked (B2). |
| behavior-variability-sessions | not_reproduced | Cell 26: no centre and averaging combination puts all three axes within tolerance. Mean-centred gives 8.1, 8.1 and 7.0%; median-centred gives 0.4 to 0.7%. |
| table1-endpoint-means | partially_reproduced | Cell 28: all 48 monkey X means are within the Table 1 SDs. But the largest V vs NV difference is 0.150 cm (135°, y), above the 0.121 bound. Monkey B's 48 values cannot be tested. |
| table1-endpoint-sd | not_reproduced | Cell 30: 8.3% of SDs are within 10%. Data SDs are about 0.55 × Table 1 (0.32 to 0.67 cm against 0.50 to 1.28 cm). |
| fig3-example-neuron | not_reproduced | Cell 32: 8 units peak at 225° in both conditions with a position effect, but none matches. The closest has P_vis 0.364 and P_int 0.537. The paper's cell may be from monkey B, which the notebook could not find. |
| movement-epoch-tuning | not_reproduced | Cell 34: 187/359 (52.1%, 179 scaled to 343), against 139 ± 13.9, with code 8 read as onset. Reading (b) was not run. |
| hold-position-main-effect | reproduced | Cell 36: 141/359 (39.3%, 135 scaled to 343), against 135 ± 13.5. The PSTH variant agrees (142). |
| hold-vision-main-effect | reproduced | 49/359 (13.6%, 47 scaled to 343), against 44 ± 4.4, and fewer than position. The all-units variant (49 scaled) falls just outside. |
| hold-interaction | reproduced | 27/359 (7.5%, 26 scaled to 343), against 27 ± 2.7 (reading a). |
| hold-subepochs | not_reproduced | Cell 38, main population: 1 of 6 values within tolerance. The all-units variant gets 3 of 6, which would be partial. |
| hold-overall-effects | partially_reproduced | Cell 40: any position 40.4% (within 44 ± 4.4) and any vision 18.7% (within 19 ± 1.9), but both 13.1% (outside 11 ± 1.1). |
| correlation-endpoint-datasets | reproduced | Cell 42, reading (a): r = 0.924 and 0.915, permutation P = 0.469. Reading (b) (single trials) finds a difference (P = 0.025). Data set 1 is built from the MANOVA, which did not reproduce (16% significant). The ±0.093 tolerance on r is barely diagnostic. |
| fig4-indx1-negative | partially_reproduced | Main population: only "all cells" is within (77.8%); the other three groups are 68.4/75/75%, each 0.6 to 1.5 points below tolerance. Under the all-units variant all four are within (81.4/71.4/76.8/81.2). Group sizes are 98/44/20, against 110/38/27. Depends on V=4. |
| fig4-indx1-means | not_reproduced | Position Only is −12.0% (within), but Position/Vision is −24.2% against −31 ± 3.1, and it is not the most negative group (all cells −24.9%). |
| indx1-tuning-shift | not_reproduced | Cell 47: 33/44 same or adjacent, against 22/38. The other cells average −27.6%, against −40 ± 4. |
| indx2-means | not_reproduced | Cell 49: no reading has all three means within tolerance. The closest is all units, outliers on INDX2, reading (c): −2.0/−14.1/−9.9. |
| rate-variance-nv-higher | not_reproduced | Cell 51: 46.4 vs 23.1 (spikes/s)², against 56 ± 5.6 and 30 ± 3. The direction and the ≈2× ratio match. |
| fig5-fano-factor | not_reproduced | Cell 53, reading (a): FF 1.84 vs 3.19, P = 0.28. Reading (b): 0.98 vs 1.24, P = 0.02, but both FFs are outside tolerance. |
| cv2-larger-nv | reproduced | Cell 55, reading (a): median 0.737 NV vs 0.622 V, Kruskal-Wallis P = 0.024. Reading (b) gives P = 0.098. The direction rests on the V=4 assumption. |
| fig6-decoding-vv | not_reproduced | Cell 57: bootstrap 77.4 (a) and 73.3 (b), against 91.6 ± 9. The unbootstrapped full population gives 87.5, which is within tolerance but is not a criterion reading. |
| fig6-decoding-nvnv | not_reproduced | Bootstrap 63.7 (a) and 57.2 (b), against the lower bound of 63.9. A marginal miss. The full population gives 77.5. |
| decoding-v-better-than-nv | reproduced | Cell 58, main population: V > NV with P < 0.05 under all of (a), (b) and (c). Wholly dependent on the V=4 mapping: cell 58 shows the other mapping reverses it. |
| fig6-decoding-cross | reproduced | Bootstrap (a): 58.9 and 52.7, both within tolerance and both below V/V (77.4). Cross reading (b) also passes (62.1 and 56.8). |
| decoding-subepochs | not_reproduced | Cell 60: NV first 400 ms is 59.8 and last 400 ms is 42.8, paired t P = 0.007 and two-sample P = 0.017, so the first and last windows differ. The all-units variant passes under (a) and (c). |
| decoding-nonsignificant-cells | not_reproduced | Cell 62, main population: V 24.7 and NV 12.5 are both outside tolerance, and V vs NV is significant (P = 0.00016). |
| eye-position-no-difference | blocked (metadata_insufficient) | No documented eye channel. The archive does hold `.plxAnaAD` files for 607 sessions (16 AD channels). The notebook says none looks like a fixation trace but does not show it, so I cannot confirm the block. |
| aborted-trials-nv | blocked (metadata_insufficient) | The window size is undocumented (field 1 is a guess), and the V/NV labels were inferred from these same aborts, so the test would be circular. The mapping-free part (aborts rise as the window shrinks) could be tested only if field 1 is the window size. The cell 66 counts are non-monotonic for code 4 (13.9% at 8, 24.4% at 10, 3.6% at 12). |
| longer-hold-no-difference | blocked (metadata_insufficient) | No completed trial has field 11 ≥ 1200 (cell 68). Field 11's meaning as minimum hold is itself contradicted by the event timing (B3). |

### B. Problems

1. **Population not reconciled with the paper** (cells 11–13). [affects a conclusion] All 359 kept sessions have monkey X's geometry, but the paper has only 219 monkey X sessions, and the data descriptor says 124 cells are from monkey B. Either about 140 sessions are not in the paper, or the geometry argument for "no monkey B" is wrong. The notebook does not address this. It affects every count, decoding and index claim.
2. **Endpoint position never validated** (`ppc.trial_table`, fields 19–21; cells 24, 28, 30). [affects a conclusion]
   - The record is assumed to be the trial's mean position over the 800 ms hold (Fig. 2 legend). It could just as well be a single sample.
   - The MANOVA rejects in 16% of pairs. In my simulation, `hotelling2` rejects 4.7% of the time under the null at n = 5 per group. Session SDs are about half of Table 1's.
   - Whether V and NV trials are interleaved or blocked in time (drift would inflate the MANOVA) was not checked.
3. **Analysis window not shown to lie inside the hold** (`ppc.WINDOWS`, cells 10, 68). [affects a conclusion]
   - The shortest code 10 to code 12 interval is 0.832 s, both in sessions with field 11 = 900 and with 1000. That is shorter than the field-11 "minimum hold". So either code 12 is not the end of the hold, or field 11 is not the minimum hold.
   - In short trials, the 800 ms window ending at code 12 starts about 30 ms after target offset, before fixation is acquired, so it includes the saccade.
   - This most affects the first 400 ms. It fits the high first-400 ms position count (35.7% against 31%) and the NV first vs last decoding difference (hold-subepochs, decoding-subepochs).
4. **V=4 / NV=7 mapping** (`ppc.V_CODE`, cell 16). [affects a conclusion] Reasonable: aborts after code 10 are 29% more frequent on code 7 (P ≈ 7e−30), and the inference is independent of the neural data. But the direction of decoding-v-better-than-nv, cv2-larger-nv, fig5-fano-factor, rate-variance-nv-higher and INDX1/INDX2 rests entirely on it, and it makes aborted-trials-nv circular.
5. **Main population is "first sorted unit per session"** (cell 22). [affects a conclusion] This is the author's own choice, stated as such. The all-units variant flips fig4-indx1-negative to within tolerance (and hold-subepochs to partial, decoding-subepochs to passing). The paper's actual rule for picking one cell per session is unknown.
6. **Fano-factor outlier readings** (cell 53). [affects a conclusion] Reading (a), removing the 5 Fig. 4 cells, keeps variances up to 2188. The paper's Fig. 5 axes stop at 80 (from the text extraction). This suggests the paper trimmed more heavily, and the claims file's reading (a) may be wrong. Reading (b) removes 64 cells. Neither reproduces.
7. **Decoder chance level** (`ppc.decode`). [does not affect a conclusion] Leave-one-out Poisson decoding of random data gave 7.5% in my test, not 12.5%. The notebook uses 12.5% as chance, which is the more conservative choice, so "above chance" still holds.
8. **Bootstrap t-test is pseudo-replicated** (decoding t-test reading (b), cells 58, 60, 62). [does not affect a conclusion] A t-test over 200 bootstrap means always gives tiny P values. It is a criterion reading, but conclusions should rest on (a) and (c), which I did.
9. **Unused branch in `ppc.decode`**. [does not affect a conclusion] `same = train is test` is never true, because each `C[:, tr]` slice is a new object. The `np.delete` branch that runs instead is equivalent.
10. **Helpers checked on synthetic data**. [does not affect a conclusion]
    - `anova2` and `hotelling2` match statsmodels exactly (OLS type II ANOVA; MANOVA, all four statistics).
    - `decode` is perfect on separable data, and leave-one-out shows no leakage.
    - Spike units (ms ÷ 1000) are confirmed against the `.plx` file in cell 7.

### C. What I could not check, and what would settle it

- **Whether the analog files hold eye or arm position.** Needed: a per-channel summary of one session's `.plxAnaAD.mat` (range, SD, correlation with target during the hold). This would decide the eye-position block, movement-epoch reading (b), and the meaning of fields 19–21.
- **Whether fields 19–21 are a hold mean.** Needed: within-session SD of fields 19–21 per target, compared with Table 1, and their relation to the analog arm channels if present.
- **Monkey identity.** Needed: kept sessions by date, with the target-geometry statistics per date (a histogram), to see whether a block of about 124 sessions differs.
- **Hold window placement.** Needed: per-trial code 10 to code 12 intervals against field 11, and the fraction of trials where (code 12 − 0.8 s) falls within about 250 ms of code 10.
- **Trial ordering.** Needed: the sequence of field-14 codes within a few sessions, to tell interleaved from blocked conditions.
- **Clock alignment per session.** Needed: the cell 19 check run per session rather than pooled.
