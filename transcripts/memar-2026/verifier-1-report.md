**A. Outcomes** (20 claims in the claims file: 11 iEEG claims tested, 9 EEG claims blocked)

| Claim | My outcome | Reason |
|---|---|---|
| intra-ieeg-mean | reproduced | Reading a gives 0.602 ± 0.058 and reading b gives 0.570 ± 0.066. Both fall inside 0.553 ± 0.068 (main nb cell 11), and five seeds give 0.598 to 0.602 (cell 13). Reading a sits near the upper edge (0.621). The m = 0 variant would be 0.712, which is outside (masking nb cell 6). |
| table2-ieeg-intra-subjects | partially_reproduced | 8 of 12 subjects are within tolerance under preprocessing reading b and 4 of 12 under reading a (cell 15). Spearman ρ is 0.78 and 0.71. The outcome depends on reading b. |
| cross-ieeg-mean | reproduced | The mean is 0.340 to 0.351 under all four readings (C from all or val trials, paired or concatenated), inside 0.389 ± 0.064 (cell 17). The SD across subjects (about 0.106) is larger than the paper's 0.064, and sub-12 (0.647) is an outlier. |
| table2-ieeg-cross-subjects | not_reproduced | 0 of 12 subjects are within tolerance under every reading, and Spearman ρ is 0.14 to 0.28 (cell 19). |
| cross-below-intra-ieeg | reproduced | Under every reading the cross average (0.34 to 0.35) is below intra (0.602), and cross-ieeg-mean is reproduced. 11 or 12 of 12 subjects have cross below intra (cell 21). |
| fig4a-mask-sweep-ieeg | reproduced | The average falls at every step: 0.712, 0.673, 0.650, 0.628, 0.602. All 12 subjects fall at every step, and the result holds with the round rule (masking nb cells 6, 8). |
| full-mask-above-zero-ieeg | reproduced | Reading b: the m = 1.0 average of 0.602 is above the phase-shuffle average of 0.201, in 12 of 12 subjects. Reading a also holds, with the smallest electrode at 0.226 (surrogates nb cell 12). |
| fig5a-coverage-ieeg | not_reproduced | All 0.712 > Non-local 0.602 > Local 0.567, so the required order All > Local > Non-local fails. Local beats Non-local in only 2 of 12 subjects (masking nb cell 10). Only one reading of the open trial details was run (problems 1 and 2). |
| lagged-ieeg-no-gain | reproduced | Lagged 0.603 against instantaneous 0.602. That is within 0.554 ± 0.067, and the difference is +0.3%, under the 10% bound (surrogates nb cell 14). |
| surrogate-ieeg | reproduced | Phase 0.201 (tolerance 0.181 ± 0.029), IAAFT 0.184 (0.232 ± 0.060) and block 0.229 (0.201 ± 0.168) are all within tolerance and all below the original (cell 8). Only reading a (no end matching) was run. |
| surrogate-order-ieeg | not_reproduced | IAAFT (0.184) is lowest, not phase (0.201). Phase is lowest in 0 of 12 subjects, and reading b's order also fails (cell 10). Only the surrogate reading without end matching was run (problem 3). |
| intra-eeg-mean | blocked (data_missing) | The EEG data are not in DANDI:000055 (see section C). |
| intra-eeg-above-ieeg | blocked (data_missing) | Needs the EEG values. The iEEG half (0.602 or 0.570) is available. |
| cross-eeg-mean | blocked (data_missing) | EEG not in the dataset. |
| transfer-penalty-larger-ieeg | blocked (data_missing) | Needs the EEG values. The iEEG half could have been computed but was not reported: ratio about 0.58, difference about 0.25 (0.35 / 0.602). |
| lagged-eeg-no-gain | blocked (data_missing) | EEG not in the dataset. |
| fig4b-mask-sweep-eeg | blocked (data_missing) | EEG not in the dataset. |
| fig5b-coverage-eeg | blocked (data_missing) | EEG not in the dataset. |
| surrogate-eeg | blocked (data_missing) | EEG not in the dataset. |
| surrogate-order-eeg | blocked (data_missing) | EEG not in the dataset. |

**Archive check for the blocked claims.** I queried the API for the version info and asset list of 000055 at 0.220127.0436. It has 55 assets, all `sub-XX_ses-N_behavior+ecephys.nwb` for 12 subjects. The measurement technique is extracellular electrophysiology and the measured variables are ElectricalSeries and Position. There is no scalp EEG. No EEG claim can be tested here. For intra-eeg-above-ieeg and transfer-penalty-larger-ieeg, only the iEEG side can be computed.

**B. Problems**

1. [affects a conclusion] Movement-event reading (b), movement plus rest trials, is never run and never mentioned as skipped. `smr.load_session` uses only `intervals/reaches`. The files hold `intervals/epochs` with labels (1427 rows in sub-01 ses-3, cell 3), so the reading was probably feasible. The claims file requires every reading. Under the "one reading" rule, the not_reproduced outcomes (table2-ieeg-cross-subjects, fig5a-coverage-ieeg, surrogate-order-ieeg) and the partial one (table2-ieeg-intra-subjects) are therefore provisional.
2. [affects a conclusion] Preprocessing reading (b), epoch-wise, is run only for intra-ieeg-mean and table2-ieeg-intra-subjects (main cell 10). It is not run for:
   - cross-subject (cell 17; donors are reading-a weights only)
   - the mask sweep and coverage (masking nb cells 6, 10)
   - surrogates and lagged (surrogates nb cells 6, 8, 14)

   Reading b moved table2-intra from 4/12 to 8/12, so it can matter. fig5a, surrogate-order-ieeg and table2-cross were judged on reading a only.
3. [affects a conclusion] Surrogate reading (b), end-matched segmentation, is not run (surrogates nb cell 7). The stated reason, unequal lengths, is weak. Algorithm 4 shuffles each channel independently, so the time alignment across channels is already destroyed. The usual end-matching practice is to pick one fixed-length sub-segment per series, or one common length per trial, which gives equal-length trials. End matching removes the wrap-around discontinuity that phase randomisation creates. It could lower the phase-shuffle value (0.201) below IAAFT (0.184), and that is the comparison surrogate-order-ieeg turns on.
4. [does not affect a conclusion] The speed deviations (every 10th sample, 200 epochs) were checked on one subject, at m = 1.0 with the instantaneous model only (surrogates nb cell 16, difference 0.0003). The following were not checked:
   - the lagged model, with 5× the parameters
   - the Local model
   - surrogate fits

   With 200 epochs, an undertrained lagged model could understate a gain. A gain would have to exceed 10% to change the outcome, so the effect is unlikely to matter.
5. [does not affect a conclusion] In four files the `reaches` table and `ReachEvents` disagree by 8 to 24 h for some events (cell 3: sub-01 ses-7, sub-04 ses-3, sub-06 ses-3, sub-08 ses-4). The notebook drops only the events past the recording end and keeps the rest of the `reaches` times from those files without checking which table is right. If those times are wrong, trials are mislocated. The claims do not depend on movement locking, so the effect is likely small.
6. [does not affect a conclusion] `load_session` reads ElectricalSeries `starting_time` but never checks that it is 0 before computing `i0 = round(t·FS)`. The clock check (cell 8) supports alignment in 10 of 12 subjects. It shows no event-locked high-gamma change in sub-02 (|t| = 2.65 against a null 95th percentile of 3.30) or sub-09 (3.09 against 3.42), and the notebook does not discuss these.
7. [does not affect a conclusion] Overlapping 2 s windows from closely spaced reaches can put the same samples in both train and test (`split_64_16_20`), and in both the val and test halves in `cross_subject`. The trials are also z-scored across trials before the split (`zscore_trials`). This follows the paper's code, but the overlap was never quantified.
8. [does not affect a conclusion] Reading (b) trials are stored as float16 (`load_subject`), which loses precision before fitting. The effect on DistCorr is negligible.
9. [does not affect a conclusion] Electrodes without coordinates are dropped (16 in sub-03, 8 in sub-12; `drop_uncoordinated`). This is stated as the attempt's own choice, and it is reasonable.
10. [does not affect a conclusion] intra-ieeg-mean asks for its variants to be reported. The m = 0 variant (0.712, outside tolerance) appears only in the masking notebook and not in the intra-ieeg-mean section. The round variant is identical to ceil at m = 1.0. The atlas variant cannot be run: every `location` is "unknown" (cell 3), and I agree with that.
11. [does not affect a conclusion] The notebook's SD across electrodes (0.07 to 0.15, cell 11) is about 3× the paper's (0.02 to 0.04). That is a sign the pipelines differ, and the notebook does not discuss it.

**Helper tests on synthetic inputs** all passed:
- `dcor_rows` matches Eqs. 8 to 14 exactly.
- `mask_matrix` masks 0, 3, 5, 7 and 9 neighbours with ceil and 0, 2, 4, 7 and 9 with round, never lets the target predict itself, and Local has fan-in 9.
- `fit_smr` recovers a planted linear map (DistCorr 0.8 to 0.97).
- `features` gives lag offsets of 0, 10, 15, 25 and 30 samples, with zero padding.
- `surrogate`: phase keeps the amplitude spectrum exactly; IAAFT keeps the exact value distribution with about a 1% spectrum error; block keeps the values.
- `transfer` recovers M from a permuted copy of the same subject.

The claims file's reading of the paper (the (x, z) neighbourhood, Eq. 14 as unsquared dCor, the Local/Non-local definitions, the Table II legend) matches the text. I found no misreading.

**C. What I could not check, and the output that would have let me**

- Whether rest trials are available for event reading (b). The `intervals/epochs` label counts per file, and a run under that reading.
- Reading (b) results for cross-subject, the mask sweep, coverage, surrogates and lagged.
- End-matched phase surrogates. Their values per subject.
- Which event table is right in the four mismatched files. A per-event comparison of `reaches` and `ReachEvents` times in those files, and the ElectricalSeries `starting_time` for every file.
- The amount of train/test overlap. The fraction of trials per subject whose window overlaps another trial.
- Convergence of the lagged, Local and surrogate fits. Epochs run and median best epoch for those runs, as cell 11 gives for the instantaneous run.
- Cross-subject spread within a subject. The SD across electrodes for each subject, to compare with the paper's 0.004 to 0.016.
- Subject order against Figure 6. The text gives only the totals (5 right, 7 left), and those match the data's x signs. A per-subject electrode plot would allow the comparison.
- The iEEG half of intra-eeg-above-ieeg and transfer-penalty-larger-ieeg. The intra/cross ratio and difference, printed.
