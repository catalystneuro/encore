**Verifier report, round 1: Windolf et al. 2025, DANDI:001290 (version 0.260827.1449)**

The claims file has 34 claims: 4 use this dataset (`data: dataset`) and 30 use data held elsewhere (`data: elsewhere`).

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| edf3a-ap-dredge-slow-trend | reproduced, but only under step 1 reading (ii) | Cell 11: mean template correlation goes from 0.3023 unregistered to 0.3319 nonrigid (a) and 0.3338 rigid (b), with 70.8% and 67.5% of time bins improved. The displacement range and s.d. are reported (−104 to 123 µm, s.d. 33.7; −84 to 131 µm, s.d. 40.8) and the trace is plotted (cell 12). The criterion also requires reading (i), which was not run, so this is reproduced only under the readings that were run. |
| edf3b-hdbscan-clusters | reproduced (reading (ii) only) | Cell 16: at least two clusters in 16 of 16 combinations (6 to 41 clusters). The cluster count and sizes are reported for each. |
| edf3c-spline-subsecond | reproduced (reading (ii) only), but the test is uninformative | Cell 19: in 32 of 32 combinations the spline-corrected s.d. is below the 5th percentile of the scrambled s.d. My synthetic test shows this control also passes on pure noise (problem 1), so the pass carries almost no evidence. |
| edf3de-spline-improves-registration | partially_reproduced (reading (ii) only) | Cell 22: panel e s.d. is lower in 32 of 32, but that measure cannot fail (problem 3). Panel d template correlation is higher in 22 of 32: all 16 combinations using x, y, amplitude features improve; 6 of 16 using y, amplitude do (changes −0.012 to +0.119). The criterion's "partially reproduced" clause fits. "methods_underspecified" (readings disagree) could also be argued, because panel d depends on the feature reading. |
| 30 `data: elsewhere` claims | blocked: data_missing (not in this dandiset) | The archive API lists exactly one asset at this version: `sub-L11104/sub-L11104_ses-None_ecephys.nwb`, 7,378,434,120 bytes, a single macaque recording. The other claims need human, mouse, rat, simulated or other-macaque data. The two Fig. 2b claims are tied to a human recording, which is not here. No part of them can be tested on 001290. |

### B. Problems

1. **[affects a conclusion]** edf3c, cell 19 / `scrambled_traces`: the scrambled control comes from the claims file and is implemented faithfully, but it cannot tell real motion from no motion.
   - I simulated 34,000 spikes in 8 clusters with no motion. Both spline readings still pass: least squares gave 43.89 vs a scrambled 5th percentile of 45.82; penalized gave 44.83 vs 44.90.
   - A spline fitted in-sample always beats a permutation of itself, so "reproduced" here does not support the claim.
   - The notebook prints the evidence that would discriminate but does not use it. On the real data, GCV chose penalties of 0.01 to 1 (effective degrees of freedom about 1,000 to 1,400). On my pure-noise data it chose the largest penalty, 1e5 (effective degrees of freedom 66). That points to real sub-second structure, but it is not a held-out test.
2. **[affects a conclusion]** All four claims, header cell 0: the claims file says every combination includes step 1 reading (i) (IBL preprocessing plus DARTsort). It was not run.
   - The only justification is a runtime trial done outside the notebook (DARTsort subtraction not finished on 31 s in 13.5 min), which I cannot verify.
   - A cheaper partial check was not attempted: the IBL-style SpikeInterface preprocessing (phase shift, bad-channel removal, spatial high-pass) followed by the reading (ii) detector.
3. **[does not affect a conclusion]** edf3de panel e, cell 22: the within-cluster s.d. drops by construction, which the claims file itself notes. In my noise-only simulation it also dropped (44.89 to 43.89). So edf3de rests on panel d alone.
4. **[does not affect a conclusion]** edf3de panel d, cell 22: the template correlation uses a raster of mean amplitudes, which is dominated by the top-amplitude spikes the spline was fitted to. No template correlation on spikes left out of the fit is reported.
5. **[does not affect a conclusion]** `fit_spline`, least-squares reading: the trace reaches −14,518 to 4,367 µm (cell 19, y,amp, mcs 25). The docstring's claim that coefficients for knot intervals with no data stay "near zero" does not hold. The pass/fail pattern matches the penalized reading in every combination, so no outcome changes.
6. **[does not affect a conclusion, could shift panel d]** `template_correlation`: the Methods build the metric on "the two-dimensional spike raster described above", and that raster includes Gaussian smoothing at 1 µm and 1 s. The helper does not smooth, and the smoothed reading was not run. The smallest panel d failure is −0.0014 (0.3305 vs 0.3319), so a few results could flip.
7. **[does not affect a conclusion] Misreading in the claims file (reported, not corrected):** it says `dredge_ap.register` applies no smoothing by default. At ed236113, `motion_util.spike_raster` (lines 66–70 of the function) replaces None with the bin size, i.e. 1 µm and 1 s. That matches the Methods, and the notebook confirms a 0.0 µm difference (cell 10).
8. **[does not affect a conclusion]** edf3c: the criterion asks for the spline trace's power spectrum. Cell 19 gives only the fraction of power above 0.5 Hz (29–55%), with no spectrum or peak frequency, so a heartbeat peak cannot be checked.
9. **[does not affect a conclusion]** edf3b, cell 17: within-cluster depth s.d. is 22–135 µm, and one cluster of about 16,000 spikes appears in every combination. These are not unit-like clusters; the "at least two clusters" threshold set by the claims file passes trivially.
10. **[does not affect a conclusion]** edf3a, cell 11: the AP estimate is jumpy. Within-60-s s.d. is 21–45 µm, which is comparable to the slow trend (60-s means −34 to +38 µm), and the 99th percentile of 1-s changes is 41–51 µm. The criterion uses only the template correlation, so the outcome stands.
11. **[does not affect a conclusion]** Cell 8: the NWB session description (V1, static gratings at 8 orientations) differs from the Methods (noise at 40 Hz). The notebook notes this.
12. **Checked and found correct:**
    - Detection parameters match `ap_registration.ipynb`: threshold 6, both signs, monopolar triangulation, 75 µm radius, and detection radius 50 µm (the SpikeInterface default).
    - Registration parameters match step 2.
    - The spline sign convention is consistent between edf3c and edf3de.
    - On synthetic inputs, `template_correlation` gave 0.75 for a static raster and 0.17 with 30 µm jitter. `center_clusters` removed the one outlier and left a zero mean. `scrambled_traces` permuted the bins correctly.

### C. What I could not check, and the outputs that would settle it

- **Reading (i) runtime:** a log of the DARTsort trial, or a run of reading (i) on a 60-s segment.
- **Whether real sub-second motion is captured (edf3c):** a held-out version, i.e. a spline fitted on half the clusters or alternate time bins and evaluated on the rest. Also the same scrambled test on a no-motion surrogate (time-shuffled spikes), and the spline's power spectrum with its peak frequency.
- **Panel d leakage:** template correlation computed only on spikes not used to fit the spline, plus a variant using the Gaussian-smoothed raster.
- **What the clusters are:** depth centre, mean amplitude and time course of each cluster, especially the ~16,000-spike one, to see whether it is a unit, a region or an artefact. Also which channels have noise up to 323 µV.
