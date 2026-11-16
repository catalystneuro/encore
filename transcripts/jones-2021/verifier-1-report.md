**Verifier report: jones-2021 on DANDI:000165 (0.211118.1526), round 1**

There are 42 claims in the claims file. My outcomes: 3 reproduced, 4 partially reproduced, 28 not reproduced, 7 blocked. The rest notebook still has some author result cells (cells 41, 44 and 47), and so does the run notebook (cells 42 and 45). I did not use them.

**A. Outcomes**

| claim | outcome | reason |
|---|---|---|
| fig1-tables1-expression | blocked (data_missing) | The archive holds only 572 NWB files: 402 HomeCage and 170 LinearTrack ephys and position. There is no histology. |
| figs1ef-exvivo-cno | blocked (data_missing) | There are no slice recordings in the archive. |
| fig2ef-csd-sr | blocked (other) | The notebook gave "not run within this run's time" as the reason, which is not a data reason. The cohort 1 data are deposited: 62 single-shank files from 5 PV-Cre and 4 SST-Cre mice (rest cell 3). |
| fig3b-mua-during-swr | not_reproduced | CA1 shows no change, as claimed. But CA3 and DG MUA do not increase in either genotype: p from 0.09 to 0.80, with PV coefficients negative (cell 12). The deposited-time variant gives the same result. |
| fig3c-swr-rate-bidirectional | not_reproduced | The PV increase holds only under log reading (b) (p=1e-8). The SST effect is not significant in either reading (p=0.37/0.84). The genotype test is not significant (p=0.67/0.09) (cell 14). |
| fig3d-swr-chains | not_reproduced | PV p=0.48. SST p=0.0064 falls short of the Holm threshold; only the 5 SD variant reaches significance (cell 16). |
| fig3e-swr-length-sst | not_reproduced | The SST increase has p=0.011, which is not significant after Holm. The genotype test has p=0.30 (cell 18). |
| swr-longer-100ms-sst | not_reproduced | No reading has both values within tolerance and p<0.05. Under (a)(c): 38.1% vs 40.7%, p=0.03, with the CNO value outside 49.6±4.96 (cell 20). |
| fig3f-swr-frequency-pv | reproduced | PV increase p=4.5e-5 (reading a) and 3.6e-5 (reading b). SST p=0.06, not significant (cell 22). |
| fig3g-sw-amplitude-pv | not_reproduced | PV increases significantly. But SST also increases significantly (p=0.0020, under the 0.0021 threshold), and the genotype test has p=0.53 (cell 24). The measure itself is suspect (problem 5). |
| figs2a-swr-size-pv | reproduced | PV decrease p=2.1e-5 (reading a) and 1.4e-4 (reading b) (cell 26). |
| tables2-fast-ripples-pv | blocked (data_missing) | The LFP is 1 kHz and filtered at 300 Hz. Asset sizes average about 171 MB, which rules out deposited 30 kHz raw data. |
| tables2-detection-unchanged | not_reproduced | SST CA1 rest MUA comes out significant by the Wilcoxon test the criterion's rule picks: p=0.0494 (the t test gives 0.18). This is fragile, and only 14 of the paper's 16 mice per group are used (cell 28). |
| tables2-rest-sg-pv | partially_reproduced | The PV CA1 mean rise and the SD rise in all three regions hold under both readings. The SST absence fails in CA3 (p=0.0023) and DG (p=0.042). The expected µV² values are not matched under either reading or scale (cell 30). The criterion defines no partial outcome. |
| fig4d-swr-sg-power-pv | blocked (other) | Not run. It could be computed from the deposited LFP and the SWR times the notebook already has. |
| fig4e-swr-sg-coherence-pv | blocked (other) | Not run, though the data allow it. |
| figs2cd-sg-predicts-sw-frequency | blocked (other) | Depends on fig4d, which was not run. |
| ca3-swr-overlap | not_reproduced | 25.3% (mean over sessions) and 25.0% (pooled), against 37.18 ± 3.72 (cell 32). |
| figs3-ca3-swr-pv | not_reproduced | Only 1 of 6 tests holds under reading (a) (PV CA3 rate down) and 0 of 6 under (b) (cell 34). Partial needs 4. |
| figs3c-ca3-swr-rate-sst | not_reproduced | The SST coefficient is negative (p=0.05/0.35) (cell 36). |
| figs3-dentate-spikes | not_reproduced | Neither rate decreases (p=0.40, 0.07), and PV length does not increase (p=0.91). PV amplitude down and the four absences hold (cell 38). |
| fig5b-mua-run | not_reproduced | No CA3 or DG increase in either genotype, and the coefficients are negative. SST CA1 decreases significantly under reading (b) (run cell 11). |
| fig5d-sg-power-run | not_reproduced | The SST CA3 and DG decreases hold. The PV CA1 increase fails (coefficient −0.10, p=0.71), and all three genotype tests are not significant (run cell 13). |
| fig5e-sg-coherence-run | not_reproduced | PV CA1–CA3 SG coherence goes down, opposite to the claim, in both bin readings. Under the session reading the decrease is significant (p=2.4e-4) (run cell 15). |
| fig5f-sg-frequency-pv | not_reproduced | The PV decrease holds only in CA3 (p=1.5e-4, 7 of 8 mice). CA1 and DG are not significant (run cell 17). Partial requires CA1. |
| fig5g-sg-theta-modulation | not_reproduced | PV CA3 and DG go down (DG significantly), opposite to the claim. SST CA1 p=0.56, and the genotype tests are not significant (run cell 19). |
| fig6b-fg-power-sst | not_reproduced | SST CA1 is not significant, and SST DG decreases significantly (p=1.1e-5), opposite to the claim (run cell 21). |
| figs4e-sg-fg-inverse | not_reproduced | The correlations are positive (r=0.92 in CA3, 0.81 in DG) where the claim needs negative ones (run cell 23). |
| fig6e-sg-fg-ratio | not_reproduced | Only the PV increases in CA3 and DG hold. The CA1 parts and all genotype tests fail (run cell 25). |
| fig6f-fg-coherence-unchanged | reproduced | None of the 4 tests is significant under either bin reading (run cell 27). |
| fig6g-fg-frequency-sst | partially_reproduced | Holds in DG only (p=1.6e-6), using 5 of 7 SST mice. CA1 p=0.81, CA3 p=0.24 (run cell 29). |
| fig6h-fg-theta-modulation-sst | not_reproduced | SST CA1 p=0.085; genotype test p=0.15 (run cell 31). |
| figs4h-fg-theta-modulation-pv | partially_reproduced | The DG decrease is significant (p=2e-6). CA3 p=0.0098 goes the same way but is not significant after Holm (run cell 33). |
| figs5-theta-power-ca1 | not_reproduced | The CA1 coefficients are negative and not significant. SST DG decreases significantly (run cell 35). |
| figs5-theta-coherence-frequency | not_reproduced | The PV DG frequency rise holds, but PV CA3 theta frequency is also significant (p=0.0011, 7 mice) (run cell 37). |
| figs6-double-like-pv | not_reproduced | The claimed exceptions (theta–SG modulation, PV vs P/S, in CA3 and DG) are not significant: p=0.60 and 0.52 (run cell 44). |
| figs6-double-unlike-sst | not_reproduced | P/S CA1 FG power p=0.81, and P/S FG frequency rises in DG only. None of the seven computed "eight" SST vs P/S tests is significant (rest cell 46, run cell 44). |
| figs6-empty-vector-control | not_reproduced | Empty-vector mice change with CNO at rest (SWR rate, chains, size) and in 7 run features (rest cell 46, run cell 44). |
| running-speed-unchanged | not_reproduced | Speed differs significantly under reading (a): 4.70 vs 5.24 cm/s, t(29)=2.69, p=0.012, values within tolerance. Under reading (b): p=8e-6 (run cell 9). |
| tables4-genotype-baseline | partially_reproduced | CA3 SG frequency and both SG/FG ratios are significant in the stated directions, with means within tolerance. DG SG frequency has p=0.038 and fails Holm, with 5 of 7 SST mice (run cell 39). The criterion defines no partial outcome. |
| tables6-sex-swr-size | not_reproduced | Female minus male SWR size is −0.08 SD, p=0.52 (rest cell 40). |
| sex-stratified-effects | not_reproduced | None of the named exceptions has a significant sex interaction (rest cell 43, run cell 41). Power is low: 3 female SST mice at rest, 3 female and 4 male on the track. |

On the blocked claims, I checked the archive directly. The asset list confirms nothing exists for fig1, figs1ef or the fast ripples. fig2ef, fig4d, fig4e and figs2cd are testable from the deposited files. No chance levels apply to this paper. I found no misreading of the paper in the claims file. One thing it could have used: the CA3 SWR counts in Table S3 (82,196 for PV) match the notebook's reading (a) (all CA3 SWRs) and not reading (b).

**B. Problems**

1. **[affects a conclusion]** Four claims are marked blocked "other" for lack of time, though the data exist: fig2ef, fig4d, fig4e and figs2cd. The same gap leaves 7 of the 24 rest comparisons uncomputed for the figs6 claims.
2. **[affects a conclusion]** The alignment of run periods with the LFP on the track is not established. In run cell 5, the theta-power–speed correlation at zero lag (mean 0.030) is no higher than with speed shifted ±30 s (0.037, 0.052). The notebook goes ahead anyway.
   - `speed_trace` assumes the LFP starts at t=0 (`np.arange(n_lfp)/FS`) and never reads the ElectricalSeries `starting_time`.
   - The position end minus the LFP end ranges from −92 s to +1229 s across sessions.
   - Every run claim depends on this alignment.
3. **[affects a conclusion]** There is a bug in `process_track`. Instantaneous frequency is computed only when the region's MUA site (`freq_sites`) is also one of the region's analysis sites. Otherwise the mouse is silently dropped. I confirmed this with a synthetic site table: a DG MUA site labelled "dg-gc mua" is never visited.
   - This explains 7 of 8 PV mice in CA3 frequency and 5 of 7 SST mice in DG frequency.
   - Affected claims: fig5f, fig6g (its DG result), figs5-theta-coherence-frequency (the failing PV CA3 test) and tables4 (DG SG frequency).
4. **[affects a conclusion]** Instantaneous frequency is taken from one site per region. This is not stated as an assumption, and Method M averages a region over all its sites. Table S3's data-point counts imply the paper pooled peaks over sites: for PV CA1 SG, 1,038,019 against 347,369 here; for theta, 308,329 against 76,244.
5. **[affects a conclusion]** SW amplitude (`process_homecage`, `sw_taps`) has a median of 3273 file units (cell 24). Table S4 gives vehicle means of 375 and 385 µV. File units otherwise match µV: the ripple-band mean is 71.3 here against 72.39 µV in Table S2. The 0–30 Hz envelope is taken with no baseline or mean removal, so slow or offset components likely dominate it. This affects fig3g and the SW-amplitude parts of the sex and figs6 claims.
6. **[affects a conclusion]** The spike-clock correction (`mua_lag`, `mua_measures`) is an assumption: the per-session lag is chosen to maximise CA1 MUA around SWRs, which is partly circular for the CA1 part, and it drops 50 sessions. The rest outcomes do not change under the deposited-time variants. However, no spike-clock check was done on the track, and run MUA (fig5b) uses 100 ms bins. The home-cage lags (median −0.145 s, up to 2 s) are larger than that bin size.
7. **[does not affect a conclusion]** Rest cell 7 says file units are 0.195 µV ADC steps. The ripple-band match with Table S2 points to µV. This only affects the rest-SG expected values, which fail under both scales.
8. **[does not affect a conclusion]** Run spectra use non-overlapping 1 s bins that lie wholly in run. That gives about 5× fewer data points than the paper's counts (6,133 against 31,496 for PV CA1). Coherence is averaged over site pairs, where the paper's counts indicate one value per pair. With random slopes per animal this matters little.
9. **[does not affect a conclusion]** `genotype_test` uses χ² with 9 df, following Table S3, on a model with 5 effective extra parameters. This is conservative. In the cases I checked, the 5-df p-values do not cross the Holm thresholds either (fig3c LR 14.9 gives p=0.011; sgfg_ca3 LR 17.6 gives p=0.0035).
10. **[does not affect a conclusion]** Run cell 41 silently skips the P/S group in the sex interaction on the track. The "either or both" MUA exception is therefore untested for P/S.
11. **[does not affect a conclusion]** Dentate-spike amplitude is in z units, where Table S4 reports µV. A related check: the detector finds 9.9 events/s in pure 1/f noise, which looks alarming, but the data rate of 8.6/s matches the paper's 9.18 Hz and its per-mouse counts, so it follows the paper.

Helper checks I ran on synthetic inputs:
- `fit_lmm`/`treatment_test`: the cell-statistics likelihood equals a full-data maximum-likelihood fit exactly (log-likelihood −364.6803 both ways).
- `holm`: correct.
- `region_sites`/`freq_sites`: reproduces the bug in item 3.

**C. What I could not check, and the output that would settle it**

- **Track alignment (item 2):** each session's `starting_time` for the ElectricalSeries and the first position timestamp, and the theta-power–speed cross-correlation over lags of ±60 s in 1 s steps.
- **SW amplitude (item 5):** per-session median raw LFP at the SW site, SW amplitude after subtracting a pre-event baseline, and vehicle group means set against Table S4's 375/385 µV.
- **Missing mice (item 3):** the label of each region's MUA site per session, and the number of mice per run feature and group.
- **Track spike clock (item 6):** an MUA lag check on track sessions, for example the MUA cross-correlogram against theta troughs or against SWRs during track pauses.
- **Treatment order:** all cohort-3 mice are labelled vehicle ×3 then CNO ×3, where the paper says the treatments alternated, and the deposited start times put all six track sessions on one day, minutes apart. I could not tell whether the labels or the order are wrong. Per-session-number means of the run features for the empty-vector mice would show whether a session-order trend explains their CNO "effects" and the uniformly negative run coefficients.
- **Genotype tests with 5 df:** the `p_df5` values are computed but never printed with Holm decisions.
