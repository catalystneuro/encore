No outcome changed. The verifier agreed with all 13 (five tested, eight blocked as data_missing), and its points led to one bug fix, new outputs and clearer wording on the weak tests. The entry re-ran cleanly with `python tools/entry.py all` (77 s), `check` reports 0 errors, and the round is recorded under `verifications` in `attempts/002014-choi-2025-01.yaml`. Nothing is committed.

**Fixed**
- **Dopamine reference at V (`reference_at` in `chamber.py`):** when the sample at V was NaN, the old fallback averaged an uneven window and gave a 0.13 offset on a synthetic ramp. It now interpolates between the nearest valid samples on each side, if both are within 0.2 s. A new sanity cell tests this on a ramp: it fails with the old code (error 0.133) and passes with the new one (error 4e-15).
- **Effect on the numbers:** none of the 62 successful trials that are NaN at V has valid samples on both sides, so all 62 are now dropped. fig8b now reads 1.88 against 1.10, p = 0.0035, with 429 and 460 trials (23 and 39 dropped). It was 1.87 against 1.11, p = 0.0037.
- **Wrong denominator in fig8a:** the share of trials with a ratio above 1 counted trials without a ratio as below 1. Over the 889 trials that have one it is 64%, where it was given as 60%.

**Added**
- **fig8a:** trial 133's ratio is higher than 76.9% of the 889 ratios. The text now calls the test weak and says the criterion was written after trial 133's values had been printed.
- **fig8b:**
  - A permutation test that shuffles labels only within blocks of 50 consecutive trials, so slow drift across the session stays in the null: p = 0.0045 (RW to RW+3 s: p = 0.0010).
  - A variant without trial 1411: p = 0.0031.
  - A note on the "c8c" in the Zenodo list file names: Zenodo describes the lists as trial ids used for all its data sets, so the site name doesn't affect them.
- **fig9a:** the PSTH values per condition in 100 ms bins, and the 7 ms lag-corrected value (0.48) in the conclusion.
- **fig9bc:**
  - The detector's dead time: 1.562 ms against a 1.50 ms waveform.
  - The Plexon unit's ISIs below that dead time: 14 (0.015%).
  - The waveform dataset shapes.
  - A count of ISIs just above the dead time relative to 10 to 30 ms: 0.106 for the thresholded unit, 0.204 for Plexon.
  - The conclusion now says the criterion holds but the evidence for a single unit is weak.
- **fig9d:**
  - Trial-averaged normalized power with bootstrap 95% CIs: 0.839 for large and 0.885 for small, difference -0.046 (CI -0.125 to 0.036).
  - The within-block permutation test: p = 0.19.
  - The plot is limited to ±1.5 s to avoid the filter's edge distortion, and the edge values are printed.
- **Findings:** the clock finding now says the dandiset description ("all data are expressed relative to the start of the Neuralynx recording") is contradicted by the data. The README and notebook summary rows for fig8a and fig9bc carry the same caveats as the conclusions.

**Not done**
- I did not report the description mismatch upstream. It is recorded as a finding; opening an issue on a project we don't maintain needs your approval first.
- I did not change the fig9bc outcome. The criterion decides it and it holds; the verifier also gave "reproduced", with the same weak-evidence caveat.
- I did not save the paper text under `paper/`: I used no text beyond what the verifier had already saved, and the folder is not in this checkout.
- The repo root has untracked files I did not create (`.bashrc`, `.profile`, `.vscode`, `scripts` and others). I left them alone; they should not go into the workflow's commit.
