**A. Outcomes**

The claims file has 33 claims. The notebook tests 5 and blocks 28.

| Claim | Outcome | Reason |
|---|---|---|
| table-s1-recordings | not_reproduced | Only 489 and 503 are in the archive, which I confirmed with the API (2 assets, draft identical). Both unit counts miss (61 vs 65, 43 vs 48) and both OL counts miss (249+251 vs 266+265; 230+283 vs 305+304) (cell 23). Trial totals match (1000 intact rows, 1027), but neither the full nor the partial rule can be met. |
| figs1-running-speed | not_reproduced | 503 gives 5.93 cm/s under (a) and 12.95 under (b), against 21 ± 4. Reading (c) is computable for only 2 of 19 animals and gives 16.56. No habituation sessions exist (cell 25). |
| fig2a-success-rate | not_reproduced | Success is 0.61 to 0.69 under all 8 criterion readings, against the 0.855 needed (cell 27). The 100% "running" variant (n = 94) is the author's own and not a criterion reading. |
| fig2b-lateral-spread | not_reproduced | Under (b) the t = 0 SD is 0.84 cm against 0.55 ± 0.055, so even the partial rule fails, although the widening holds. The 2 s and 3 s SDs miss under (c), (d) and (e). Reading (a) is degenerate: always 0 at t = 0, and it resets at the next trial (cell 29). |
| fig4-ddm-fit | partially_reproduced (low confidence) | GDDM BIC is below DDM BIC in all 4 readings fitted. NDT is 0.000 to 0.005 s in every fit against 0.12 ± 0.012 (cell 33). The NDT failure is probably an artefact (problem 1). |
| fig1lm-staged-modulation, fig1n-epoch-rates, fig1jk-all-units, fig1n-ramp-slope, fig1o-trial-end-ramp, fig1-ramp-contralateral-only, fig2m-dimensionality-collapse, fig4b-ddm-matches-ramp, fig5e-slope-across-animals, fig4f-varce-example-unit, fig4g-varce-population, fig4j-corce, fig4k-streak-index, fig5b-epochs-in-subpopulations, fig5cd-other-animals, fig5e-principal-vs-neighbor | blocked (metadata_insufficient) | I agree. At the stored onsets there is no trial-locked modulation, and spike counts decode trial type at chance (cells 15–16). The best lag drifts by seconds to tens of seconds (cells 18–19). The SI says LabVIEW TTLs were used for sync, but the archive's asset metadata lists only "Units" and the files hold no sync signal. Some parts can be tested without the clock (see the note under this table). |
| fig2c-psychometric, fig2d-turn-angle, fig2f-whisking-params, fig2i-ft-rt, fig2jk-glm-mixed-tuning, figs12-tuning-lost-during-decision, fig2-epoch2-at-first-touch, fig2l-running-vs-sitting, fig3-wall-kinematics, fig3c-touch-statistics, fig3ijkl-whisking-across-epochs | blocked (data_missing) | I confirmed this against the archive: two assets only, and the acquisition holds only ball tracking (cell 3). There are no wall, whisker, touch or gait series, and animals 474, 475, 480, 499, 518, 573, 579 and 589 are absent. |
| fig3-not-sensory-drive | blocked (data_missing) | It depends on fig3c-touch-statistics (data missing) and fig1lm-staged-modulation (blocked). |

Parts of blocked claims that could be tested without the spike clock:
- fig5b-epochs-in-subpopulations: the layer and FS/RS counts can be checked. They miss: L2/3 7 vs 10, L6 12 vs 13, FS 30 vs 43, RS 31 vs 22 (cell 23).
- fig1jk-all-units: the 65 units and 531 trials can be checked, and both miss (61 units, 500 trials).
- fig2i-ft-rt: RT alone is available for the ephys animals (cell 31), but the claim's animals and first-touch times are not.

These parts do not change the blocked outcomes.

**B. Problems**

1. [affects a conclusion] `fit_ddm` / cell 31: the NDT result is almost certainly set by a few very early RTs. The cell 33 histogram shows about 5 OL_L RTs between 0 and 0.03 s (min 0.007 s), while the rest of the distribution starts near 0.15 s. A DDM gives zero likelihood to any RT below the NDT, so NDT is pinned under the minimum RT, which fits the 0.000 to 0.005 s found in every fit. The edge rule drops only maxima within 5 ms of 0. I checked this with a synthetic trial: an early bump at 0.009 s plus the main push at 0.3 s gives `reaction_time` = 0.007 s. The model also has no lapse or mixture overlay (PyDDM's usual way to absorb outliers). So the NDT mismatch, and with it the partial outcome, is not established.
2. [does not affect a conclusion] `fit_ddm`: the GDDM leak sits at its lower bound (−9.9 to −10) in all 4 fits. The ranges are the author's own, not the paper's. The GDDM was fitted only for sigma = 0.25 and the 0 to 1 s window. Sigma is scale-redundant (the sigma-free and fixed DDMs give the same K/B), and the BIC gap is about 240, so the BIC comparison likely holds anyway.
3. [does not affect a conclusion] Cells 18–21: the author did not try a clock-drift model (offset plus rate) fitted from the speed correlation. In 503 that correlation drifts smoothly from 12.9 to 19.8 s over 0 to 5200 s (r 0.3 to 0.6). Such a model is independent of the turn response and could have allowed coarse tests in 503. In 489, the key animal, the correlation is weak (|r| ≤ 0.17), so the 489 claims stay blocked either way. The statement that z of 3.1 to 9.9 "can be reached by chance" over 16,000 lags is asserted with no null.
4. [does not affect a conclusion] `figs1-running-speed` / cell 25: running is classified per row over CL and OL rows together. For 503 this gives a run fraction of 27.7% against Table S1's 52.8%. Together with the unit and OL count mismatches, this suggests the deposited 503 session or curation differs from the one analysed in the paper. The notebook does not say so.
5. [does not affect a conclusion] `lateral_traces` / cell 29: `n` is the number of rows, not the number of non-NaN values. `_on_grid` returns NaN when the first kept sample is after the grid time, and `nanmean`/`nanstd` hide that count.
6. [does not affect a conclusion] `decode_accuracy`: z-scoring uses all trials before the CV split (mild leakage). It is used only for the clock check, which came out at chance.
7. [does not affect a conclusion] Cells 7–8, table-s1: the claim that the 1000 intact rows "are the 1000 trials of Table S1" is an assumption. The file holds 1611 real rows (305 extra turns), and those fail the 10% tolerance.
8. I found no misreading of the paper in the claims file in the parts I checked. The header could note that the SI says TTL sync was recorded.

**C. What I could not check**

- Whether the NWB files hold a sync signal anywhere outside `acquisition`, `units` and `intervals/trials` (`processing/`, other `intervals/`, `stimulus/`, `general/notes`). A full recursive HDF5 key listing in cell 3 would settle this.
- Whether NDT approaches 0.12 s once early RTs are handled. Needed: the number of OL_L RTs below 0.1 s, and refits that exclude RT < 0.1 s or add `OverlayUniformMixture`.
- How many values are NaN at each time in the cell 29 traces (per-time non-NaN counts).
- Whether the epoch 1 rate of 2 Hz is compatible with the data at all. Needed: the population rate per unit averaged over the CL rows of 489 under a speed-derived clock, or at least its session-wide value (mean unit rate is 5.9 Hz). This is one clock-independent check of fig1n-epoch-rates.
- Whether a piecewise-linear clock from the 503 speed correlation produces any trial-locked structure. Needed: a PSTH under that clock, with a shuffled-onset null.
