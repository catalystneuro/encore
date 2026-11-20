**A. Outcomes** (26 claims in the claims file: 16 in vitro, 10 in vivo)

| Claim | Outcome | Reason |
|---|---|---|
| fig2d-chr2-ctz-excites | reproduced | Cell 40: blue light and CTZ give p ≈ 7.6e-12 with the median higher after (62 of 62 electrodes up). Vehicle gives p = 0.637 (paper 0.6498). n = 62, 62, 24 as in the paper. |
| fig2d-gtacr2-ctz-inhibits | reproduced | Cell 42: blue light and CTZ give p ≈ 1.1e-9 with all 49 electrodes down. Vehicle gives p = 0.5525 (paper 0.5594). |
| fig3c-uncut-responses | reproduced | Cell 44: all three conditions give p < 1e-9 with the median higher after. n = 63, 54, 51. |
| fig3c-cut-abolishes-ctz | reproduced | Cell 46: blue light p = 3.5e-11, higher after. Electrical stimulation p = 0.095 (paper 0.0965) and CTZ p = 0.733 (paper 0.7388). |
| figs4c-blockers-silence | reproduced | Cell 48: both Mann-Whitney tests give p ≈ 1.5e-10 to 1.8e-10, in the stated directions, n = 27. |
| fig4c-sb-ctz-activates | reproduced | Cell 50: SB + CTZ is above both other groups (p = 8e-12 and 4e-14). SB alone against SB + vehicle gives p = 0.7311 (paper 0.7305). |
| fig4e-late-ctz-no-effect | reproduced | Cell 52: p = 0.4024 (paper 0.4022), n = 18. |
| fig4e-stim-then-ctz-activates | reproduced | Cell 54: all three pairwise tests give p < 0.05 (5e-8, 2.4e-4, 2.8e-8) with stimulation + CTZ higher. |
| fig4e-stim-alone-no-effect | reproduced | Cell 56: p = 1.0 and 0.8079 (paper 0.9999 and 0.8553). Both are p ≥ 0.05. |
| fig5c-bont-blocks | reproduced | Cell 58: stimulation against stimulation + CTZ gives p = 0.659 (paper 0.7173). Blue light gives p = 9.5e-7 with the median higher during light. |
| figs5-bont-reduces-release | blocked (data_missing) | The IVIS images are not deposited. The archive holds only the 6 in vivo NWB files. |
| figs6-luciferase-in-dcvs | blocked (data_missing) | The confocal images are not deposited, neither in the dandiset nor in the Supplementary Data. |
| fig6c-green-light-abolishes | reproduced | Cell 60, reading (a): SB + CTZ p = 0.0375 (paper 0.0369), higher. Green light p = 5e-10, lower. Reading (a) matches the paper's p values; reading (b) gives 0.0011, which does not match the paper's "< 0.0001". |
| fig6f-nonfunctional-opsin-no-response | blocked (data_missing) | Cell 62: the source-data column "SB alone (after)" has 18 values, while the legend gives n = 21. It is identical to the Fig. 4e(i) column. On it the test gives p = 3.6e-10 against the paper's 0.7870, so the paper's comparison group is not in the sheet. Taken literally, the criterion would give not_reproduced. |
| figs3-ctz-acts-postsynaptically | blocked (data_missing) | The MEA recordings are not deposited. The archive has no in vitro files, and the Supplementary Data hold no Supp. Fig. 3 sheet. |
| figs2-cut-disrupts-synchrony | blocked (data_missing) | Same as figs3: no in vitro recordings anywhere. |
| fig7b-bioluminescence-both-groups | reproduced | Cell 18: all 5 imaged mice have a post mean above the bootstrap upper bound (ratios 1.07 to 1.71). Only the whole-frame reading (o2b) could be run, because the archive records no ROI. |
| fig7c-gamma-emerges-opsin-plus | reproduced | Cell 20: the rule holds in 4 of 4 readings (Opsin (+) 0.08 to 0.11 dB, Opsin (−) −0.09 dB). The support is weak; see problem 2. |
| fig7d-contacts-exceeding-baseline | not_reproduced | Cell 22: the rule holds in 0 of 16 readings. Opsin (−) has 25 to 29 contacts per mouse above baseline (paper 2.7 ± 2.5), and the Opsin (+) mean is not higher than Opsin (−) in 14 of 16 readings. |
| fig7d-superficial-layers | blocked (metadata_insufficient) | Cell 24: the two possible z orientations give opposite answers (16 of 16 readings against 0 of 16). The archive does not say which end of the probe is superficial. If z = 775 is the top, the claim holds under every reading. |
| fig7e-gamma-power-electrodes | partially_reproduced | Cell 26: KS and one-tailed Mann-Whitney give p < 0.05 in 4 of 4 readings. Both means are within tolerance, but the Opsin (+) median is −0.04 to 0.009 against 0.34 ± 0.034, and the Opsin (−) median is outside tolerance in the union rows. |
| fig7e-gamma-events-electrodes | partially_reproduced | Cell 28: the tests hold in 32 of 32 readings. The values are within tolerance in 0 of 32: Opsin (+) means are 28.7 to 33.6 against 213.6 ± 139.5. |
| fig7e-gamma-power-mice | partially_reproduced | Cell 30: U = 9 in 8 of 8 readings and both means are within tolerance. Neither median is (0.70 to 0.78 against 0.88 ± 0.088; 0.04 to 0.06 against 0.09 ± 0.009). |
| fig7e-gamma-events-mice | blocked (methods_underspecified) | Cell 32: U = 9 in 36 of 64 readings and U = 8 or 8.5 in 28, so the readings disagree. The criterion makes that blocked. No reading is near the values: Opsin (+) means are 39 to 52 against 327 ± 46. |
| fig7f-mua-electrodes | not_reproduced | Cell 34: the two-tailed Mann-Whitney test gives p = 0.67 to 0.97 in 16 of 16 readings. The Opsin (+) median is below the Opsin (−) median in every row. |
| fig7f-mua-mice-not-significant | blocked (methods_underspecified) | Cell 36: U is 6, 7 or 8 depending on the reading (16, 14 and 2 of 32), which puts readings on both sides of the not-reproduced/partial line, so the criterion makes it blocked. U = 9 never occurs, and the Opsin (−) mean is never within tolerance (61 to 77 against 27 ± 18). |

**B. Problems**

1. [affects a conclusion] Cell 62, fig6f. The "Synaptic blockers (After)" column has 18 values, not the legend's 21, and duplicates Fig. 4e(i). The notebook prints this but still runs the test on it, which gives the opposite of the paper's result. The Fig. 5c sheet has a 21-electrode "Synaptic blockers (After)" column (cell 38: n = 21, max 3) that may be the right one; it was not tried.
2. [does not affect a conclusion under the criterion as written] Cells 20 and 22, `db_rel_baseline`. A 5-taper estimate of P is biased: about −0.45 dB in theory, and −0.40 dB on white noise when I ran it through `mt_spectrogram` and `db_rel_baseline`. Cell 22 shows a baseline mean of −0.43 dB in every mouse. So 0 dB is not "no change". Measured against their own baselines, all three Opsin (−) mice rose by 0.20 to 0.51 dB, and per mouse the groups overlap (ctrl_5 at 0.078 is above interlum_4 at −0.049 and interlum_6 at 0.024). The "not seen in Opsin (−)" half of fig7c rests only on the group-mean comparison.
3. [affects a conclusion] Cell 22, fig7d contacts. The bootstrap resamples 180 overlapping 10 s windows in 1 s steps as if they were independent. This follows the claims file, but the confidence interval comes out far too narrow, so almost every contact "exceeds" in both groups. A block bootstrap might change the Opsin (−) count. The not_reproduced outcome rests on this choice.
4. [affects a conclusion] Cell 6, `onset_index`. The onset is fragile:
   - The two largest rises are nearly equal in interlum_4 (10.4 against 10.1, 33 s apart), interlum_ctrl_4 (17.2 against 16.8) and interlum_ctrl_5 (21.7 against 19.1).
   - In ctrl_4 the chosen onset falls 8 s before CTZ infusion starts, which is physically implausible.
   - Cell 9's cross-correlation with Supplementary Data 7 puts the paper's onsets up to tens of seconds away.
   
   No reading varies the onset. The onset sets the baseline and every window, so it could move the borderline mouse-level U values (events, MUA). The electrode-level and fig7d outcomes are unlikely to flip.
5. [affects a conclusion] Cell 24, fig7d-superficial. The notebook runs both orientations, but the orientation is a metadata gap rather than one of the claims file's readings, and the claims file's "probe map" is not in the archive.
6. [does not affect a conclusion] Cell 12, `errant`. The union rule excludes 4 contacts (28 kept), not 7 (25 kept), so n = 84 per group instead of 75. The Methods' "across all animals a total of seven" could also mean the sum of per-animal flags; here that sum is 11. Neither reading gives 7. The RMS span (whole recording) is the author's own choice, stated as an assumption.
7. [does not affect a conclusion] Cells 28 and 32. Gamma event counts are about 7× below the paper's in all 64 readings, which suggests a pipeline difference (envelope smoothing, threshold). It is consistent across readings, so the electrode-level outcome is partial either way.
8. [does not affect a conclusion] Cells 26 and 34. The direction check is inconsistent: means are used for gamma power, medians for MUA. The MUA outcome fails on the Mann-Whitney p regardless.
9. [does not affect a conclusion] Cell 18. interlum_4 is imaged for only 866 s after onset, so its post mean covers 808 frames, not 1200, with 58 blank frames dropped.
10. [does not affect a conclusion] Cells 56 and 58. Small p differences from the paper (0.8079 against 0.8553; 0.659 against 0.7173) are consistent with Prism's handling of ties and zeros differing from scipy's.
11. [does not affect a conclusion] Cell 0. The table says "fig7b to fig7f (11 claims)"; the claims file has 10.

**C. What I could not check**

- Probe orientation. An output printing the electrodes table's column descriptions, the ElectrodeGroup and Device descriptions, and the label-to-site map would have settled fig7d-superficial (or confirmed it cannot be settled).
- The right Fig. 6f comparison group. An output running the test with Fig. 5c's 21-value SB column, and printing the Fig. 6f sheet in full, would have.
- Onset sensitivity. Rerunning the mouse-level U values (cells 30, 32, 36) with the second-largest rise as onset, or with the lag that best matches Supplementary Data 7, would have.
- Fig. 7d bootstrap sensitivity. A version of cell 22 with a block bootstrap (for example 10 s blocks) would have.
- Mouse identity and the excluded contacts. Reading the Fig. 7d to 7f sheets of Supplementary Data 7 (per-contact and per-mouse source values) would have let me match the archive's mice to the paper's, check the 7 excluded contacts, and tell whether the event and MUA differences come from the pipeline or the data.
- Whether the ephys and image clocks are aligned (TTL). Nothing in the files lets me check this.
