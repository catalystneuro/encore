I've revised the attempt for every point in the round-1 report. No outcome changed. I re-ran the entry with `python tools/entry.py all`: both notebooks pass (about 24 and 27 minutes) and the checks report 0 errors. Every conclusion was checked against the new outputs. Nothing is committed.

**Outcomes:** edf3a, edf3b and edf3c stay reproduced and edf3de stays partially reproduced, all still marked as assumed. The verifier agreed with all four. The 30 claims on data held in other archives stay blocked as recorded (`too_large`, and `not_runnable` for edf1). The verifier gave `data_missing`, but protocol step 1.4 forbids that reason for claims whose data are in other archives, so I recorded the disagreement and kept them.

**What I added or corrected:**
- **Reading (i) (problem 2):** I added a second notebook, `ibl_preprocessing_variant.ipynb`. It runs the IBL preprocessing before the reading (ii) detector on the whole recording, which is the cheaper check the verifier suggested. All four outcomes come out the same.
  - For edf3de, panel d again improves in 22 of 32 combinations, but different ones fail. Under reading (ii) the failures are runs without lateral position. Here they are runs with the top 25% amplitude cut. The question to the paper's authors now names the amplitude cut as well.
  - The record no longer gives any number from the DARTsort trial run outside the notebook.
- **edf3c control (problems 1 and 8):** I ran the claims file's control on a surrogate with shuffled spike times and no motion. It passes there too, in 32 of 32, which confirms it cannot fail. I added two held-out checks:
  - Fit on half of each cluster's spikes, the penalized spline lowers the spread of the other half in 32 of 32 cases, and in 0 of 32 on the surrogate.
  - Fit on half of the clusters, it lowers the spread of the others in 22 of 32 cases.
  - The least-squares spline overfits.
  - I also added the power spectra. The spline peaks at 0.26 to 0.27 Hz. The spikes themselves peak at 0.25 Hz and its harmonics, and at 2.0 or 2.3 Hz.
- **Panel d leakage and smoothing (problems 4 and 6):** On a raster of only the spikes the spline was not fit to, panel d improves in 22 of 32. On the smoothed raster it improves in 24 of 32, and edf3a also holds there. Panel e drops on the surrogate as well, so the conclusion now says it cannot fail (problem 3).
- **Other outputs asked for:**
  - A per-cluster table: the 16,000-spike cluster sits at 2,322 µm on 11 channels and looks like several neighbouring units.
  - The noisy channel: 86, at 323 µV. I added a finding that the electrode table marks no bad channels.
  - The wrong `fit_spline` comment is fixed.
- **Questions file:** `questions/001290.yaml` now asks a reader two things: the claims file's misreading of the smoothing default (problem 7), and whether the edf3c control should be held out.
- **Record:** the `verifications` round is filled in with the verifier's reasons and my responses, and the README is updated.

**Not done:**
- Reading (i) itself is still not run: DARTsort isn't in the locked environment and was far too slow on this CPU.
- The re-run gives slightly different registration figures from round 1: 70.7% and 66.7% of time bins improved, against 70.8% and 67.5%. The mean correlations are unchanged, and the record says so.
- `tools/build_site.py` was already modified before this run. I didn't touch it.
