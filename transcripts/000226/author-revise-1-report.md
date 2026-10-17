Round 1 is handled. The verifier agreed with all 28 outcomes and none changed: 14 reproduced, 3 partially reproduced, 11 blocked. I re-ran `python tools/entry.py all entries/000226-severson-2017` after the last analysis change and it passed in 21 minutes. I then checked every conclusion and the summary against the new numbers. `entry.py check` also passes after the attempt-record and header edits.

**What I added or corrected, by verifier point:**
- **B1 (tolerance check):** the fig5 cell, and the fig2c rate cell, now check against the claim's tolerance (the paper's IQR), and both checks pass. The 10% check is still printed but labelled "not the criterion".
- **B2 (fig5e, Rayleigh p = 0.047):** I added other ways of estimating each afferent's preferred phase. Using the circular mean of the tuning curve gives p = 0.062, which would be "reproduced". Taking the highest of 20 bins gives p = 0.023, and of 60 bins p = 0.046. The criterion fixes the highest of 30 bins, so the outcome stays partially reproduced. The notes say it sits on the threshold and depends on the estimator.
- **B3 (fig3d best pair):** I fitted all 45 pairs again with lambda 100, and again on held-out frames (fit on one half, scored on the other). M0 and M0' still rank second behind M0 and velocity in both: 0.589 against 0.600, and 0.620 against 0.630. The outcome stays partially reproduced.
- **B4 (phase convention):** position by phase is no longer all NaN, and it peaks next to phase 0 in all 60 files. I added a cosine correlation (median 0.9999, against sine -0.9999), which shows the stored phase is the negative of the Hilbert phase, not shifted by pi. I reworded the finding.
- **B5 (viscoelastic bounds):** `fit_visco` now reports which parameters end at a bound, on the scale it fits. 7 of 25 fits do (eps_lim in 6, E in 1, eta in 2). The text now says the parameter values are not interpreted.
- **B8 (cut-whisker files):** 199B and 209A hold distance-to-pole series and some contact frames (5,014 and 32). I recorded this as a new `metadata_insufficient` finding.
- **B10 (archive check for blocked claims):** a new cell lists each asset's archive metadata (`variableMeasured`), every group and dataset in every file, and the size per trial. No file has anything in acquisition, analysis or stimulus. Nothing is named for EMG, optogenetics, whisker length or manual labels. 7A, 8A and 9A have no Units.
- **fig7f lower bound (from the "Not checked" list):** I computed it, but it says nothing useful. 4 of the 5 cut-whisker afferents are anticorrelated with the nasolabialis curve (mean r -0.277). As a stand-in that is not the criterion, the better of each afferent's correlations with its own positive or negative velocity curve averages 0.753, against the paper's 0.76. The claim stays blocked because the criterion needs the intrinsic protractor EMG, which is not in the dandiset.
- **Table S1 transcription:** I downloaded the supplement (mmc1.pdf) from the publisher's file server. All 60 rows match `merkel.TABLE_S1` on every column the analysis uses. I noted this under `inputs`.
- **Runtime:** updated to about 21 minutes in the README, `entry.yaml` and the notebook header.

The round is recorded under `verifications` with all 28 results (`agrees: true`), the verifier's reasons and my responses.

**What I did not change:**
- **fig7d-cut-emg:** the verifier gave the block as `metadata_insufficient`. I kept `data_missing` as the main reason, because no labelling of the trials would supply the missing EMG. That difference is recorded in the verification entry.
- **B6, B7 and B9:** no changes. Fitting and scoring on the same frames, and requiring whisking for contact, both follow the claims file. B9 is a remark about readings that do not discriminate, and the notes already give every reading.

The downloaded paper text and supplement are in `paper/`, which git does not track. Nothing is committed.
