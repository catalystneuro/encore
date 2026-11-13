**A. Outcomes (56 claims in the claims file)**

Tally: 22 reproduced, 20 partially reproduced, 7 not reproduced, 7 blocked.

| Claim | Outcome | Reason |
|---|---|---|
| source-data-1-link | reproduced | All 372 cells agree on trial count, CR @ US and baseline Hz. Shifting by ±1 gives 0 agreements. Depth is present for 270 cells (cell 10). |
| firing-rate-depth | reproduced | Reading a gives 68.3 Hz with Pearson r = 0.086, p = 0.16. The paper has 67 Hz, r = 0.085, p = 0.16 (cell 13). |
| fig1ijk-modulation-classes | not_reproduced | No reading gets all three counts within tolerance: a gives 80/23/167, a+ gives 62/13/195, b gives 88/31/151 (cell 15). |
| modulation-absolute-not-rate-dependent | not_reproduced | Absolute suppression is never significant (p ≥ 0.89). Relative facilitation is never significant with the printed sign. Only the facilitation absence and relative suppression (−0.207, reading a) hold (cell 17). |
| fig1l-cells-with-behavior | reproduced | 111 recordings, inside the 92.7–113.3 tolerance (cell 19). |
| fig1m-modulation-grows-with-training | partially_reproduced | The criterion holds (class a, day codes: facilitation r = 0.244, p = 0.029; suppression r = +0.228). Neither r is within tolerance of 0.413 or 0.354 under any reading (cell 21). |
| fig1no-modulation-more-with-behavior | partially_reproduced | Both chi-square tests give p < 0.05 under every reading, and suppression is 16/111 against 7/159, matching the paper. Facilitation is 42 against 38, outside 30 ± 3 (cell 23). |
| fig2a-facilitation-properties-ds1 | partially_reproduced | Both correlations are positive with p < 0.001 under every reading. Magnitude is never within 20.25–24.75 Hz (18.1–19.6). Under the claims-file readings, duration is also out (85, 79) (cell 25). |
| fig2b-facilitation-trial-correlations-ds1 | reproduced | Class a with x = a, y = us: 18 significant cells, 0 opposite, bootstrap p < 0.002. The base is 42 cells, against the paper's 30 (cell 28). |
| fig2b-lmm-ds1 | reproduced | Every slope is in 0.39–0.55 (inside 0.35–0.63) with p < 1e-10 (cell 30). |
| fig2d-facilitation-leads-eyelid-ds1 | partially_reproduced | Spikes lead with Wilcoxon p < 0.003, but the mean lag is 31.8–49.3 ms against 25 ± 2.5. Lags sit at the ±100 ms edge in 16–22 cells (cell 32; see B1). |
| fig2-s1-correlation-matrix-offsets | not_reproduced | Neither all eight offsets within tolerance nor the sign pattern holds under any reading. Suppression position offset in set 1 is at ±100 (cell 34). |
| fig2e-facilitation-ds2 | reproduced | 70 cells, magnitude 60.4 Hz (class a, 12–212 ms), both within tolerance (cell 36). |
| fig2f-facilitation-trial-correlations-ds2 | reproduced | 48–51 significant cells under every combination, inside 44.1–53.9 (cell 38). |
| fig2f-lmm-ds2 | reproduced | Under x reading c the slope is 0.627 or 0.620, inside 0.56–0.72. Readings a and b give 0.51–0.53, which is out (cell 40). |
| fig2h-facilitation-leads-eyelid-ds2 | partially_reproduced | Wilcoxon p ≈ 1e-11 with spikes leading, but the lag is about 73 ms against 33.4 ± 3.3. About 25 of 70 lags are at the edge (cell 42). |
| fig2-suppression-properties-ds1 | partially_reproduced | Reading a has the values within tolerance (10.3 Hz, 63.6 ms) but the %CR and amplitude correlations are not significant. Reading b has the correlations but the values are out (9.9 Hz, 53 ms) (cell 44). |
| suppression-smaller-shorter-than-facilitation | reproduced | Class b, all cells, peak z: amplitude p = 0.00016 and duration p = 0.013, suppression lower. The criterion only reports the values. This is the only one of 12 combinations where both tests hold (cell 46). |
| suppression-same-timing-as-facilitation | not_reproduced | On the cells of the adopted reading (class b, all), onset p = 0.00074 and peak time p = 0.036 are both significant (cell 48). |
| fig2j-suppression-trial-correlations-ds1 | reproduced | Class a with x = a, y = data or us: 16 cells, 4 significant (tolerance 2–4), 0 positive, slope −0.38 or −0.40 (inside −0.51 to −0.03), bootstrap p ≤ 0.002 (cell 50). |
| fig2l-suppression-no-lead-ds1 | not_reproduced | This is a claim of absence, but the Wilcoxon test is significant under every reading (lag 48–71 ms, p ≤ 0.004). Half the lags are at the edge (cell 52; B1). |
| fig2n-suppression-ds2 | not_reproduced | No reading puts the cell count in 14.4–17.6: 18/14/12/11/21/18 (cell 54). The rest of the claim was not run on the 0–212 ms window (B4). |
| ds2-stronger-facilitation-same-suppression | partially_reproduced | Both tests hold under every reading. First-dataset facilitation is 24.6–25.8 Hz against 30.1 ± 3.0 (cell 56). |
| fig2p-suppression-no-lead-ds2 | not_reproduced | Wilcoxon p < 0.0005 under every reading, so the absence fails (cell 58; B1). |
| ds2-modulation-proportion | reproduced | Class a, 12–212 ms: 88 modulated and 18 suppression cells, both within tolerance (cell 60). |
| fig3-optogenetic-inhibition-abolishes-crs | blocked (data_missing) | Confirmed in the archive (section C). |
| fig4b-cs-pause-ds1 | partially_reproduced | No reading gives 6–8 CS pause cells. drop/mean at 125 ms has the latency (84.6 ms) and Fisher test (p = 0.0003–0.0007) but 9 cells (cell 65). |
| fig4c-cs-pause-ds2 | partially_reproduced | mean/trough at 125 ms gives 37 cells (in tolerance) and Fisher p = 0.004, but 32 of them have facilitation against 39 ± 3.9 (cell 67). |
| fig4g-cs-pause-latency-cr-latency | reproduced | e.g. drop/trough with latency b: r = 0.560 (p = 1e-6) and 0.389 (p = 0.004), both within tolerance. The n is 66 and 52, against 45 and 41 (cell 69). |
| fig4s1-cs-peak-cells | reproduced | drop/mean: 4 cells in set 1, 0 in set 2, Fisher p = 0.0021 with class a (cell 71). |
| fig4s1-cs-peak-suppression-not-different | reproduced | No test is significant under any reading. The groups are 1–8 cells, so the test has almost no power (cell 73). |
| fig4h-transient-responses-after-day-3 | reproduced | drop/mean at 125 ms: 0 of 99 on days 1–3, 13 of 171 later, p = 0.0026 (cell 75). |
| fig5cd-cs-pause-faster-facilitation-ds1 | reproduced | drop readings with class b: p(a) = 0.014 and p(velocity) = 0.046, pause cells higher. Reading (b) values (44 against 15 Hz) fit the paper; velocities are about 2–4× the paper's (cell 77). |
| fig5hi-cs-pause-faster-facilitation-ds2 | reproduced | Under the drop readings, facilitation is not significant (p ≥ 0.24) and velocity is (p ≤ 0.0003). Under mean/trough, the reading that matches fig4c's count, velocity p = 0.055 (cell 79; B2). |
| fig5ej-cs-pause-cells-shallower | blocked (data_missing) | Second-dataset depth is NaN for all 102 cells in Source data 1, and CRCNS has no depth field. The first-dataset half holds only for 2 pause cells (p = 0.048 to 0.054), not under the drop readings with 7–9 cells (p = 0.13 to 0.34) (cell 81). |
| fig5s1-model-timing | blocked (data_missing) | No Purkinje recordings or model output in the archive or in Source data 1. |
| fig6-us-peak-prevalence | partially_reproduced | Count 214 and amplitude 104 or 97 Hz are within tolerance. Latency 11.8 ms is just outside 9.54–11.66 (cell 85). |
| fig6c-us-peak-declines-with-training | partially_reproduced | Early is higher (p = 0.002 or 1.5e-6), but the later mean is 75 or 59 Hz against 29 ± 2.9 (cell 87). |
| us-peak-anticorrelates-with-behavior | reproduced | r = −0.381 and −0.271, p < 1e-5. Both r values are slightly outside tolerance, which the criterion only reports (cell 89). |
| fig6d-us-peak-trial-correlations | partially_reproduced | Slope −2.16 or −2.10 is in tolerance and bootstrap p < 0.002. The counts are out: 72 cells against 62, and 16–20 significant against 13 (cell 92). |
| us-peak-cooccurs-with-facilitation | partially_reproduced | The Fisher test on facilitation among US peak cells holds (p ≤ 0.013). The test of trial correlations fails (p = 0.15–1) (cell 94). |
| fig6s1a-eyelid-opening-us-peak | reproduced | Reading b: 142 cells, 16 significant positive, bootstrap p < 0.002 (cell 96). |
| fig6s1bc-purkinje-us-complex-spike-opening | blocked (data_missing) | No Purkinje data in the archive. |
| us-pause-prevalence | reproduced | 99 cells, 28.6 ms, −48.9 or −51.7 Hz, all within tolerance (cell 100). |
| cs-pause-cells-have-us-pause | reproduced | Only under the author's 125+50 mean/trough variant: 6 of 6, p = 0.0022. Under the claims-file windows, the test holds only with 3–4 cells (cell 102; B2). |
| fig6b-us-peak-pause-overlap | partially_reproduced | 76, 138 and 33 are within tolerance; pause-only is 23, outside 25.2–30.8 (cell 104). |
| fig6g-us-response-depth | reproduced | Kruskal-Wallis p = 0.00067; order 1920 < 2061 < 2186 µm, all within tolerance (cell 106). |
| us-pause-declines-with-training | partially_reproduced | Both tests hold (chi-square p = 2.5e-5; magnitude p = 0.0014). Later-day pause count is 31, outside 35.1–42.9 (cell 108). |
| fig6h-us-pause-trial-correlations | partially_reproduced | 4 significant cells with bootstrap p = 0.014–0.02 meets the criterion. Slope is 0.37 against 0.66 ± 0.12; 35 cells against 41 (or 37 in the legend); 3 cells are significant the other way (cell 110). |
| fig7-second-us-peak | partially_reproduced | Peak time 43.9 ms and magnitude 61.4 Hz are within tolerance; the count is 105 or 109 against 83 ± 8.3 (cell 112). |
| fig7-second-us-peak-dynamics | partially_reproduced | Using the last-50 ms reference, 3 of 4 positive tests and the absence hold. The velocity test fails (p = 0.0525), and the early mean is 24.6 against 16 ± 1.6 (cell 114). |
| fig7c-second-peak-cells-lower-cr | partially_reproduced | Both Mann-Whitney tests hold. The set-2 counts are 16/21/19 against 9/24/11, all out of tolerance (cell 116). |
| fig7b-first-second-peak-correlated | partially_reproduced | The positive significant correlation holds. Slope 0.617 against 0.31 ± 0.08, and 58 significant cells against 14 (cell 118). |
| us-only-trials-ds2 | blocked (data_missing) | Confirmed in the archive and in Source data 1 (section C). |
| fig7s1c-us-only-second-peak-cs-pause-cells | blocked (data_missing) | US-only trials are absent. The notebook has no section for this claim. |
| fig7fg-us-pause-resembles-cs-pause | blocked (data_missing) | Same as above. |

**B. Problems**

1. **[affects a conclusion]** `ipn.xcorr_lag` (cells 32, 42, 52, 58). The lag is the argmax of a Pearson r recomputed on a re-cut eyelid window at each lag. That normalization is the author's choice and is not stated as an assumption. When the traces are ramp-shaped, r is flat across lags and the argmax takes the first tie. In a synthetic test, a true +20 ms lag on ramps came back as −30 ms. In the real data, 16–26 lags per group sit at the ±100 ms edge. The four lag claims (fig2d, fig2h, fig2l, fig2p) rest on an estimator that is not defined for these traces, and no alternative was run (for example, a mean-subtracted full-trace cross-correlation or a narrower lag range).
2. **[affects a conclusion]** CS-transient readings (cells 65–81, 102). Each claim passes under a different reading, and no single reading reproduces the CS-pause results together:
   - drop/mean at 125 ms gives fig4b 9 cells and fig4s1/fig4h.
   - mean/trough matches fig4c's count but fails fig5hi (p = 0.055).
   - 125+50 mean/trough passes cs-pause-cells-have-us-pause but gives fig4b Fisher p = 1.0.
   
   The per-claim outcomes overstate how well these results reproduce as a set.
3. **[affects a conclusion]** Cell 25 and cells 15–28. Reading a+ is the author's own (stated in cell 0). It is the reading closest to the paper for fig1ijk (facilitation 62) and fig2a. Under the claims-file readings, fig2a misses more of its values. My outcomes do not rely on a+ alone.
4. **[affects a conclusion]** Second-dataset window (cells 6 and 54). Cell 6 shows that the deposited per-trial `facilitation` for set 2 equals reading b over 0–212 ms exactly (0.0 Hz difference), so the authors computed over the whole CS-US interval. The claims file lists only 0–200 and 12–212. Under 0–212, class a gives 16 suppression cells, which is fig2n's number, but the notebook ran 0–212 only as a cell count, not the magnitude, significant count and slope. This is a gap in the claims file to report, not to correct. It could change fig2n and ds2-modulation-proportion.
5. **[does not affect a conclusion]** `WIN2` (cell 11). The 0–200 ms reading is run only for fig2e, fig2n and ds2-modulation-proportion. fig2f, fig2f-lmm, fig2h, fig2p, fig4c, fig5hi and ds2-stronger use 12–212 only.
6. **[does not affect a conclusion]** `ipn.modulation` docstring and cell 6 say the deposited `facilitation` "is" reading b. For set 1 the median maximum difference is 4.5 Hz (50–250 ms) or 8.9 Hz (0–250 ms), so it does not match. Trial reading c therefore uses an unknown window for set 1.
7. **[does not affect a conclusion]** `ipn.mixedlm` (cells 40, 50, 54). Convergence, singular-covariance and non-positive-definite Hessian warnings are not tied to table rows. The `converged` column is always True even where SE is NaN (cell 50). The fig2n slopes come from singular random-intercept fits.
8. **[does not affect a conclusion]** Velocity, the first difference of the 1 ms SDF, is a claims-file reading. Its values are 2–6× the paper's (fig5cd, fig5hi, and 3.5 against 0.55 Hz/ms in fig7). The one test that fails on it, fig7-dynamics at p = 0.0525, uses a measure on a different scale from the paper's.
9. **[does not affect a conclusion]** fig7b (cell 118). The two 30 ms trial windows overlap in 40 of 105 cells, which inflates the correlations. The notebook reports this.
10. **[does not affect a conclusion]** The Methods' trial exclusions (Grubbs, eye half open) are never applied; cell 3 counts 282 and 402 trials they would hit. This is justified by Source data 1's `# Valid Trials` matching every cell (cell 10), but the notebook never states that inference.
11. **[does not affect a conclusion]** fig7s1c and fig7fg have no section; their status appears only in the cell-0 table. Cell 6 has a no-op loop (`for rd ...: pass`).

Synthetic tests of `modulation`, `classify`, `duration_onset_peak`, `us_responses`, `cs_transients`, `corr_matrix`/`optimal_offset` (a +80 ms lag came back as +80) and the `bootstrap_count` random null (2.1% per direction, against an expected 2.5%) all behaved as documented. Two consequences of the claims-file readings, not bugs:
- Under the "trough" rebound, a dip that just returns to baseline counts as a rebound.
- Under the "drop" reading, the rebound after a pause counts as a CS-peak upstroke, which is why drop/trough finds 31 and 32 CS peaks.

**C. What I could not check, and what would have let me**

- **Blocked claims, checked in the archive.** The S3 listing of `cb-1/live/` holds one data file (`eLife_dataset.mat`), the `.m` example, the docs and the checksums. The description lists only paired CS-US trials of IpN units, with no trial-type field, so the optogenetics, Purkinje and US-only data are absent. I also read Source data 1's 51 variable names (MD5 3ca8f91c… matches the notebook): none are US-only or optogenetic, and Depth is NaN for all 102 set-2 cells. No part of fig3, fig5s1, fig6s1bc, us-only-trials-ds2, fig7s1c or fig7fg is testable. fig5ej is testable for the first dataset only.
- **Per-cell values.** I could not re-run anything on the dataset, so the cell table is unverified. An exported per-cell table (classes, `cr_pct`, US-response flags) compared against Source data 1 would have settled several readings. Source data 1 holds the authors' own values:
  - `CR Yes/no?` gives exactly 103 set-1 recordings with ≥20% CRs, against the notebook's 111. A per-trial comparison would show whether the CR rule explains the selection gaps in fig6d (72 against 62) and fig6h (35 against 41).
  - The authors' `Mean Facil Hz` ≥ 5 gives 84 set-1 cells, and `Mean Supp Hz` ≥ 5 gives 34. A plain 5 Hz cutoff on the authors' own values does not give 60/23 either, so fig1ijk needs a criterion that neither the claims file nor the notebook names. Printing this comparison would have shown it.
- **fig2n on 0–212 ms.** The full fig2n table on that window was not run (B4).
- **Lag estimator.** Per-cell cross-correlation curves, or the number of tied or flat maxima, would show whether the lag results are artefacts of the estimator (B1).
- **Mixed-model fits.** Per-row convergence status would show which fits are usable (B7).
- **Stored mean traces.** The stored `ephysMean` differs from the trial mean in 26 recordings, by up to 158 Hz (cell 5). Showing which recordings, and whether trials were dropped there, would rule out a mismatch in the deposited trials.
