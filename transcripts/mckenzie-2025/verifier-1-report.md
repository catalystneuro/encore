## A. Outcomes

The claims file has 28 claims. I had no attempt record, so the counts and ids below come from the claims file only.

| Claim | Outcome | Reason |
|---|---|---|
| figs1a-desipramine, figs1b-yohimbine, fig1d-arena-decay, figs1e-univariate-covariates, fig1e-arena-time-from-transition, fig2c-track-time-from-transition, figs2-no-reward-modulation, fig3d-object-introduction, figs3-object-order-and-sampling, fig4b-novel-object-on-track, fig5d-decay-hastens-with-days, figs4-behavior-day1-day2, fig6-recent-history (13) | blocked (data_missing) | I checked the archive API. Version 0.230630.2304 has 117 assets, all `behavior+ecephys` or `raw_ecephys` NWB files from Huszar et al. There is no photometry. Nothing in these claims can be tested. |
| ne-and-settling-time-course | blocked (data_missing) | The NE half is not deposited (same check). The settling half is tested under fig7e, fig7f and fig7g, as the criterion says. |
| ephys-ensemble-size | reproduced | Reading (b), all units, 8 tested sessions: mean 259.38, range 191 to 363, within tolerance (cell 16). Over the 9 sessions with a novel run the mean is 253.78 and the range 191 to 363, which matches the paper exactly. Pyramidal units fall outside tolerance (mean 215.75, minimum 158). |
| figs6b-decorrelation-novel | not_reproduced | None of the 4 readings is significant (cell 18). The best is window b100 vs 540 s: +0.096 1/s, t(7)=1.30, p=0.23. Minute 1 is faster in only 3 to 6 of 8 sessions. |
| figs6d-decorrelation-familiar | reproduced | The judged reading (a) with minute 10 as 600 to 660 s gives +0.062 1/s, t(7)=0.78, p=0.46, which is not significant. The other readings give p from 0.40 to 0.72. |
| fig7ab-umap-embedding | partially_reproduced | Position is mapped in 7 or 8 of 8 sessions on every seed. The first minute is more peripheral in only 0 or 1 of 8 (cell 22); first-minute bins sit closer to the median (for example 1.15 vs 2.02). |
| fig7e-novel-settling | reproduced | 8 sessions, all bins, 600 s: −0.104, t(6)=−4.07, p=0.0066. Every combination gives p<0.05 (cell 25). The first-tracked-frame variant gives t(7)=−6.44, p=0.0004. |
| fig7f-familiar-settling | reproduced | −0.089, t(7)=−5.74, p=0.0007. All combinations give p ≤ 0.0053. |
| fig7g-familiar-more-similar-early | reproduced | All bins: +0.037, t(6)=2.58, p=0.042. Speed-filtered: +0.079, t(5)=4.56, p=0.006. On the 7 clock-checked sessions, all bins gives p=0.089 but speed-filtered gives p=0.017. The effect is weaker than the paper's t(7)=7.58. |
| figs7ab-in-field-out-field | partially_reproduced | Familiar passes under both readings: in-field slope up (p ≤ 0.017), out-of-field slope down (p ≤ 0.004). In the novel run the in-field slope rises (p ≤ 0.02), but the out-of-field slope is +0.0001 or +0.0017 (p=0.97 and 0.39), not negative (cell 31). |
| figs7cd-movement-not-time-locked | partially_reproduced | Familiar shows no relation, as claimed (main reading p=0.84 and 0.54). In the novel run both measures fall with time: dacc ρ=−0.103, p=0.0007; dvel ρ=−0.110, p=0.001. The novel effect is significant in nearly all readings (cell 33). The criterion needs both runs, so as a strict pass/fail it fails. |
| figs7ef-time-explains-similarity | not_reproduced | No reading meets the criterion (cell 35). Dropping velocity raises CVMSE significantly in every reading and both runs (p ≤ 0.03). Dropping time is not significant in the familiar run (p ≥ 0.38). |
| figs7gh-unconditioned-similarity | reproduced | Reading (a), 3 nearest neighbours: novel −0.024, p=0.020; familiar −0.038, p=0.002. The 540 s reading also passes (cell 37). Reading (b) is not significant, but it is degenerate (problem 5). |
| fig8b-late-moments-reactivated | not_reproduced | None of the 4 post readings run is significant (cell 6). Raw counts: +0.031 points, p=0.20. z-scored: −0.024, p=0.20. Five seeds agree (cell 7). Two combinations were not run (problem 3). |
| fig8d-familiar-no-difference | not_reproduced | The judged reading (E10 (a), z-scored, pool a) shows a difference: early above late, −0.026 points, t(7)=−3.72, p=0.0074, stable over 5 seeds (p from 0.004 to 0.007). The other readings are not significant (p from 0.15 to 0.74), so the result depends on the reading. |
| fig8-no-pre-reactivation | not_reproduced | The notebook's chance rate is 0.100% (cell 5), the same as the paper's false positive rate of 0.1%. Pre-ripple reactivation is above it: novel 0.133%, p=0.013; familiar 0.146%, p=5e-5. This holds on all seeds and readings (cell 11). The effect is small; post ripples are about 0.22%. |

## B. Problems

1. [affects a conclusion: possibly figs6b, fig8b, fig8d, fig7ab] Time 0 is set to the epoch start (`find_runs`, claims file E2). Cell 4 shows the first tracked frame comes 15 to 63 s after the epoch start in every run. In e13-26m1-211119's novel run there is no tracked bin in minute 1, so fig7e falls to t(6) where the paper has t(7). The first-tracked-frame variant (cell 27) restores t(7), which suggests the paper's transfer time is the first tracked frame. The claims file's reading of "placed in the maze" as the epoch start does not fit the data. I report this and do not correct it. The variant was run only for fig7e, fig7f and fig7g. For decorrelation (cell 18), UMAP periphery (cell 22) and reactivation (in `reactivation.ipynb`), minute 1 includes up to 63 s before the mouse is tracked. In one session all 600 "early" moments come before tracking.

2. [does not affect a conclusion] Session e16-3m2-211211 (cells 10, 12). Cell 12 says E1 readings (a) and (b) are identical because each session tracks only one novel run. That is wrong for this session. Its epochs include an open field (9559 s) and a linear track (15124 s). Cell 10 shows that the filed tracking passes the clock check only when moved onto the linear-track epoch (spatial information 0.656, peaking at zero shift). So E1 reading (b) was possible and was not run. The main 8-session set pairs open-field spikes with misaligned position in the location-conditioned analyses. The 7-session variants agree with the main results, except fig7g with all bins (p=0.089), where the speed-filtered reading still passes.

3. [affects a conclusion: unlikely to change fig8b] The reactivation readings are not fully crossed (`readings` in `reactivation.ipynb`). For post ripples, raw counts with pool (b) (under either pre window) were never run. Raw counts is the only reading with late above early (p=0.20). The claims file says readings are crossed ("under one combination").

4. [does not affect a conclusion] `fit_nn_model` with `form="exp"` follows the claims file's reading (a), but its sign constraints cannot describe the data. The fast term (b1 ≥ 0) can only decay downward from a positive start. The negative term has τ of 1000 to 10000 s (the rates are read as 1/s; the paper gives the bounds without units). So neither term can describe a rise in NN correlation over 3 to 4 minutes (cell 29). The linear form cannot describe saturation. Both underestimate time. The verdict stands because dropping velocity is significant in every reading.

5. [does not affect a conclusion] `nn_unconditioned`, figs7gh reading (b), is near zero by construction. Each unit is z-scored over the first 1000 s, so the sum of all vectors is about 0, and so is the mean correlation with all others (cell 37: about ±0.001). I confirmed this on synthetic data: with a planted rate difference between halves, the measure gave −0.0012 vs 0.0009 while the top-3 measure separated them. Reading (b) cannot test the claim.

6. [does not affect a conclusion] E9's main reading (detecting ripples from the broadband LFP) was not run; the deposited Huszar et al. ripples were used instead. The notebook gives file size as the reason and did not check whether a single channel could be streamed. For e15-13f1-220117 and e16-3m2-211211 the raw files are only 5.6 to 6.8 GB.

7. [does not affect a conclusion] `cell_types` compares only `spike_times_index` between the two versions. The markdown says the spike times themselves were compared "while preparing", but the notebook shows no such check.

8. [does not affect a conclusion] An observation, not a code error. The paper's ensemble numbers (253.8, 191 to 363) match all units over 9 sessions, including e13-26m1-211116, which has only 344 s of novel tracking. That conflicts with the paper's "only pyramidal" and N=8. All tests here use pyramidal units, as E3 says. The all-units variant was run only for fig7 (cell 26).

9. [does not affect a conclusion] The helpers passed my synthetic tests:
   - `decay_rate` recovers 1/τ to within 1%.
   - `nn_conditioned` uses only same-location neighbours and excludes the bin itself.
   - `reactivation` gives a null false positive rate of 0.0006 and detects a planted pattern.
   - `kalman_va` recovers a constant speed.
   - `path_length` skips the wrap of the figure-eight linearization.

   Significance in `reactivation` is `exceed < 1` (R above all 1000 shuffles), which is slightly stricter than "greater than 99.9%". It matches the paper's stated false positive rate and cell 5.

## C. What I could not check

- Whether sessions other than e16-3m2-211211 have two novel epochs. The later version's epoch labels are printed only for that session; e15-13f1-220118 and e15-13f1-220119 have 8 epochs. Printing `LABELS` for all 12 sessions would settle E1.
- figs6b, fig8b, fig8d and fig7ab with time 0 at the first tracked frame. Adding cell 27's offset to cells 18, 22 and 6/9 would settle problem 1.
- e16-3m2-211211 with the linear-track epoch and the realigned tracking as its novel run (E1 reading (b)) in the main tables.
- Reactivation with raw counts and pool (b).
- Equality of spike times across the two versions. An `np.array_equal` on `spike_times` in `cell_types` would settle it.
- Whether the LFP in the raw files can be streamed by channel. An h5py chunk-shape printout of `acquisition/.../data` for one raw file would answer it.
- The figure images; I read only the text outputs. In the familiar-run decorrelation cell (cell 19) the two curves look alike by their ranges, but I did not view the plot.
