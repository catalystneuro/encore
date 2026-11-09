**Verifier report: DANDI:000931 v0.261011.1559, Dehaqani et al. 2024 (round 1)**

The claims file has 37 claims. The notebook marks all 37 as blocked for missing data (cell 0, and cell 7's output: "Claims: 37 ; testable on this file: 0"). I agree with every one.

**A. Outcomes**

| Claim id | My outcome | Reason |
|---|---|---|
| inhalation-sorting | blocked (data_missing) | Needs the nasal airflow signal, or inhalation times, from about eight mice. Cell 5 shows `/acquisition`, `/processing` and `/stimulus` are empty, and the API lists 1 subject. |
| figs1a-phase-decoding | blocked (data_missing) | Phase runs from each inhalation's onset to its offset, and the file has no inhalation times (cell 7, "breathing NOT HELD"). |
| figs1b-speed-decoding-single-mice | blocked (data_missing) | Needs slow and fast labels on odorless inhalations; none are in the file (cell 7). |
| fig1-odor-responsive-fraction | blocked (data_missing) | Every reading needs odor onset times with odor and concentration. There is no `/intervals` and no stimulus (cell 5). The claim pools 6 mice; the file has 1. |
| fig1hi-sniff-changes-responses | blocked (data_missing) | Needs odor trials and inhalation onsets with speed labels (cell 7). |
| fig1h-direction-of-change | blocked (data_missing) | Same as fig1hi. |
| figs1c-early-70ms | blocked (data_missing) | Same as fig1hi. |
| figs1d-rs-fs-similar | blocked (data_missing) | Also needs unit waveforms; the units table has no `waveform_mean` (cell 5). |
| fig1j-sniff-change-larger-than-concentration | blocked (data_missing) | Needs odor trials and inhalation speed labels (cell 7). |
| fig1l-cdi-mixed-lower | blocked (data_missing) | Same as fig1j. |
| fig2-glm-variance | blocked (data_missing) | The GLM needs counts aligned to inhalations, plus each inhalation's speed and concentration (cell 7). |
| fig2c-interaction-small | blocked (data_missing) | Same as fig2-glm-variance. |
| fig2d-mixed-sensitivities | blocked (data_missing) | Depends on the fig2c weights. |
| figs2ab-rs-fs-heterogeneous | blocked (data_missing) | Needs the GLM weights and waveforms. |
| figs2c-waveform-no-prediction | blocked (data_missing) | Needs waveforms and the encoding weights. |
| figs2d-70ms-similar | blocked (data_missing) | Same as fig2c. |
| fig3c-airflow-tuning-anesthetized | blocked (data_missing) | Needs the suction pulse times and rates from the 3 tracheostomized mice. The file is one awake "Concentration Series" mouse (cell 5). |
| fig3b-latency-shortens | blocked (data_missing) | Same as fig3c. |
| fig3f-airflow-tuning-awake | blocked (data_missing) | Needs peak airflow per inhalation in the 10 control mice. Neither the signal nor those mice are present. |
| figs3-aen-neurectomy | blocked (data_missing) | The neurectomy mice and the breathing signal are absent. |
| figs4-bulbectomy-no-odor-no-phase | blocked (data_missing) | The bulbectomized mice, odor trials and breathing are absent. |
| fig4-sniff-preferring-fraction | blocked (data_missing) | Needs first-sniff and slow inhalation onsets in the control and bulbectomized mice. |
| fig4e-sniff-response-smaller | blocked (data_missing) | Same as fig4. |
| fig4f-sniff-response-more-variable | blocked (data_missing) | Same as fig4. |
| fig4g-sniff-decoding-reduced | blocked (data_missing) | Same as fig4. |
| fig4d-pre-sniff-rise | blocked (data_missing) | Same as fig4. |
| figs4-motor-cortex-sniff | blocked (data_missing) | Needs motor-cortex units with area labels, which the file lacks (no electrodes table), and inhalation times. |
| fig5b-pc1-speed-pc23-concentration | blocked (data_missing) | Needs odor and inhalation events from the 4-mouse pseudo-population. The file is at most one of those mice and has no events. |
| fig5c-encoding-angles | blocked (data_missing) | Same as fig5b. |
| fig5d-sniff-invariant-decoding | blocked (data_missing) | Same as fig5b. |
| figs5gh-other-windows-and-codes | blocked (data_missing) | Same as fig5b. The per-mouse schemes also need breathing phase. |
| fig5ef-correlated-subpopulations | blocked (data_missing) | Needs the linear-model weights, which come from inhalation events. |
| fig5gh-mechanosensitive-as-good | blocked (data_missing) | Same as fig5ef. |
| fig5i-time-course-similar | blocked (data_missing) | Same as fig5ef. |
| figs5i-coefficients-similar | blocked (data_missing) | Same as fig5ef. |
| fig6-simulation-mechanosensory-rescues | blocked (data_missing) | Needs fitted linear-model coefficients, which cannot be fitted without events. |
| figs6h-waveforms-homogeneous | blocked (data_missing) | Needs waveforms from units across experimental conditions. The file has neither waveforms nor more than one condition. |

**Archive check (step 4).** I queried the API myself:
- There are 4 versions (draft, 0.240305.0939, 0.240305.0945, 0.261011.1559). All hold one asset, `46205384-…`, `sub-001/sub-001.nwb`, 177,095,408 bytes.
- The asset metadata gives `variableMeasured` as only "Units", 1 subject (P56D, male), and one session dated 2021-10-27.
- A search for "Iurilli" returns only 000931, so there is no companion dandiset.

With spike times alone and no event times, no part of any claim can be computed under its criterion. No claim states a chance level that applies here.

**B. Problems**

1. [does not affect a conclusion] `mechano.CLAIM_NEEDS` lists `odor_trials` for fig3f, figs3-aen (no), fig4*, figs4-motor and figs4-bulbectomy-phase. Most of those use the 10 control mice, which had no odor. There, "odorless inhalations" may need no odor trials at all. The claim stays blocked anyway, because breathing is missing. So cell 7's count of 31 claims missing odor trial times is overstated.
2. [does not affect a conclusion] `CLAIM_NEEDS["figs1b-speed-decoding-single-mice"]` leaves out `other_groups`. The criterion requires "every mouse", and the claim pools the six Figure 1 mice.
3. [does not affect a conclusion] Cell 7 reads the claims file from `../../claims/...`, which is not in this bundle. On a synthetic test the helpers worked, apart from the issue in item 4. So the claim-id cross-check ("every one listed … True") holds only in the author's tree.
4. [does not affect a conclusion] In cells 15 and 16, `rate_spectrum` with an argmax over 1 to 15 Hz can report a harmonic. A synthetic 3 Hz spike train gave a peak at 6.0 Hz. The 2.78 Hz "breathing" reading in cell 16 is labelled as a consistency check only. The claim that depth ≤ 1000 µm "would be" the PCx rests on a Kilosort depth convention the notebook never checks.
5. [does not affect a conclusion] `streams_present` looks for breathing only as a group under acquisition, processing or stimulus. It would miss inhalation times stored as columns elsewhere. Cell 5's full listing shows nothing of the kind, so the result stands.
6. [does not affect a conclusion] Other helpers checked on synthetic data behaved correctly: `isi_violation_rate` gives 0 for a regular train, `presence_ratio` is right, and `duplicates` counts identical trains and the coincident fraction correctly (0.504 for a 50% shared train).

**C. What I could not check**

- I could not read the file's HDF5 tree myself, because the task forbids downloading. I relied on cell 5's listing and the asset metadata, which agree with each other. A printed `f["units"].attrs["colnames"]` would make the column check self-contained, and so would a full `visititems` listing that includes `/specifications`, in case an extension namespace holds events.
- Nothing else is needed to settle the outcomes.
