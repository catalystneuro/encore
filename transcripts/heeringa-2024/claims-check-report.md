The claims file is ready for an attempt (`ready: true`). I checked it against the paper and against the paper's code (Zenodo 10370064: `check_dataset_metadata.m`, `check_dataset_units.m`, `checkAN.m`, `makePSTH.m`). The code-based details in the criteria match the code: age cut-offs, BF fallback to CF, spontaneous-rate order, vector-strength selection, click selection, recording counts, and the bin edges for Figs. 6a and 6b. The paper reports no statistical tests, so no claim has statistics.

**Checker:** `22 claims, 22 quotes, 0 statistical values, 0 problems` before my changes; `23 claims, 23 quotes, 0 statistical values, 0 problems` after.

**Changes, by claim**
- **header:** the list of code read named 18 of the record's 21 files. I added the other three, which no criterion uses.
- **isi-exclusion:** the criterion passed if any one reading matched. Which recordings the short intervals are pooled over is a method detail, so the readings must all agree, or the claim is blocked as `methods_underspecified`. I also noted that `checkAN.m` counts short intervals per recording.
- **rlf-monotonic:** the statement said the dataset's rate-level functions all have the three standard shapes. The paper only says auditory nerve rate-level functions typically have those shapes and that the shapes were checked. The statement now says that.
- **table1-age-abr-weight:** the criterion said the ranges were "checked" but gave them no part in the outcome. It now says the outcome rests on the means alone.
- **fig6c-sr-distributions:** the criterion now says the paper does not define a "cluster", and that its rule (largest peak below 18 spikes/s) is a reading.
- **old-success-rate:** it had no expected values. I added 43% and 88%, each with the default 10% tolerance.
- **psth-primary-like (new claim):** the paper names three checks that a unit came from the auditory nerve. The third (non-primary-like response shapes at 20 and 30 dB above threshold) had no claim. Like the other two visual checks, it is blocked as `methods_underspecified`.

**Still open** (recorded under `checks`)
- **fig7a and fig7b:** the paper reports no test. The pass rules (correlation p < 0.05, median CF/BF within 10% of 1) come from the claims file, not the paper.
- **fig7ab-representative-sampling:** the KS test and the 10% median rule are not from the paper. With hundreds of units, the KS test may find a difference the paper's visual comparison would not.
- **no-prepotentials, rlf-monotonic, psth-primary-like:** these were visual checks with no rule in the paper or its code. They stay blocked unless someone supplies a rule.

Only `claims/001262/10.1038-s41597-024-03259-3.yaml` was changed; nothing is committed or pushed.
