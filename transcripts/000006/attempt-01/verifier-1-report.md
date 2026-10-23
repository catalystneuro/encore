**A. Outcomes** (9 claims in the claims file; no attempt record was among my materials, so the count comes from the claims file only)

| Claim | My outcome | Reason |
|---|---|---|
| pt-types-transcriptomic | blocked: data_missing | The archive holds only 53 NWB ephys files (variables Units, ElectrodeGroup, BehavioralEvents; 140 MB). No RNA-seq (the paper puts it in GEO GSE119182) and no reconstructions. |
| pt-types-shared-targets | blocked: data_missing | There is no anatomy in the dandiset or the asset metadata. The units only carry `cell_type` labels. |
| pt-upper-thalamus-projection | blocked: data_missing | `PTupper` is a label only. Neither the files nor the asset metadata name an injection site or projection target, and the label-to-target mapping comes from external MATLAB code (cell 4). |
| pt-lower-medulla-projection | blocked: data_missing | Same as above. |
| pt-preparatory-activity | reproduced | Cell 15: 72 of 100 units are delay-selective. The shuffle null has median 0.010 and 99th percentile 0.040, p = 0.001. This holds for each type, in all 12 animals (0.25 to 0.85), at thresholds 0.05 to 0.001, and in both variants. Depths are reported (430–1600 µm); layer cannot be checked. |
| pt-upper-early-preparatory | reproduced | Cell 17: 27 of 44 PTupper units are sample-selective, against a null 99th percentile of 0.045, p = 0.001. The baseline reference is 2 of 44, and the variants agree. |
| pt-upper-persistent | reproduced | Cell 19: (a) 27 of 44 are late-delay selective, p = 0.001. (b) The cosine is 0.495 against a null 95th percentile of 0.433, p = 0.016 (0.007 with another seed in cell 24). The Pearson variant gives r = 0.50, p = 6e-4. Persistence is moderate: only 17 of 27 sample-selective units keep their sign. |
| pt-lower-late-and-motor | partially_reproduced | Cell 21: (a) sample 0.482 against late delay 0.714, McNemar p = 0.0096, which holds. (b) Sample against response 0.643, p = 0.088, which fails. This depends on the threshold: at p < 0.001 both parts pass, at p < 0.05 neither does. |
| pt-types-differ-in-timing | not_reproduced | Cell 23: (a) sample 27/44 against 27/56, p = 0.134. (b) is reversed: response PTlower 0.643 against PTupper 0.841 (p = 0.022 for PTupper > PTlower). The by-animal comparison agrees. The paper's own measure points the other way: the coding-direction variant (cell 24) has PTupper 0.47 against PTlower 0.22, and the PTlower cosine shuffle p = 0.43, consistent with Extended Data Fig. 7c. That variant does not change the outcome. |

The paper is paywalled and not in PubMed Central. I saved the abstract, the Data availability statement and the public Extended Data legends in `paper/abstract_and_public_sections.txt`. None of these states a chance level for the fraction of selective units. The notebook's null median of about 0.01 matches the test level, as it should.

**B. Problems**

1. [affects a conclusion] Cell 11 (`tagged_units`): the unit counts disagree with the paper and the notebook never checks this. The public Extended Data legends (Figs 5–10) give n = 61 PTupper and 69 PTlower. The dandiset holds 46 PTupper and 71 PTlower tagged units, and the notebook includes 44 and 56.
   - About 15 PTupper units are missing from the archive. The dandiset description says some files were broken and left out.
   - The inclusion rule drops 15 PTlower units (7 for low rate, 6 for quality, 2 for performance), while the paper's 69 suggests it kept most of them.
   - This changes the populations behind the type comparisons (pt-types-differ-in-timing, pt-lower-late-and-motor).
2. [affects a conclusion] Cells 21 and 23: units are pooled across sessions. 34 files hold 1 to 4 tagged units recorded on consecutive days in the same mouse (for example anm372904 has 1 PTupper unit on each of 5 days). These may be the same neuron, so the unit-level Fisher and McNemar p-values may overstate n. Cell 12 acknowledges this, and the by-animal tests (n = 4 against 8) are underpowered.
3. [affects a conclusion] Cells 21 and 23: the McNemar response test (p = 0.088) and Fisher part (a) (p = 0.13) are close to the line and depend on the selectivity threshold (cell 21 thresholds). The "partial" outcome is fragile in both directions.
4. [does not affect a conclusion] Cells 9–10 (`epoch_rates` on the file clock): the stored spikes are trial windows of about 6.4 s stitched onto trial start + cue, so neighbouring trials overlap. 11.7% of baseline-epoch spikes are flagged, against under 2% in the other epochs. Dropping the flagged spikes changes no outcome (cells 13–23), and the flagged share is only a lower bound.
5. [does not affect a conclusion] Cell 7: the clock is unverified in 7 sessions. About 5 included single units sit in sessions where response-epoch decoding is at or below chance (anm372904 2017-06-16 is 0.19). If their clock is wrong they would dilute the fractions, which makes the tests conservative.
6. [does not affect a conclusion] `unit_record`: `spikes_per_trial` divides by `last - first` where the trial count is `last - first + 1`. This is an off-by-one that only matters for units near 3.2 spikes per trial.
7. [does not affect a conclusion] `decode_direction`: the z-scoring includes the left-out trial. This is minor leakage in a sanity check only.
8. [does not affect a conclusion] Cells 13 and 15–17: the baseline-epoch selective fraction is 4.5% for PTupper (p = 0.079) and about 3% overall, against 1% nominal. This hints at slight inflation from slow drift or trial-order structure that a within-unit label shuffle cannot remove. It is negligible next to the 48–84% fractions.
9. [does not affect a conclusion] Cell 0 still contains the author's outcome table, so the conclusions were not fully removed from my materials. I formed the outcomes above from the outputs.

All helpers behaved correctly on synthetic inputs: `epoch_rates`, `dprime`, `ranksum_p` and `shuffled_ranksum_p` (a null fraction below 0.01 came out at 0.0096), `overlap_flags`, `trial_of_spikes`, `null_p` and `mcnemar_one_sided`. I recomputed the McNemar (0.0096, 0.088) and Fisher (0.134, 0.994) p-values from the printed counts and they match. The cosine-similarity null correctly keeps the correlation between epochs within a trial; on synthetic data with no selectivity, the median null cosine is above 0. Inclusion uses no selectivity information, so there is no circularity.

**C. What I could not check**

- Whether the paper's inclusion rule gives 61/69 units (Methods paywalled). A cell listing each tagged unit's id, quality, spikes per trial, trial counts, performance and inclusion, next to the Figshare processed-data unit list for every session, would show which units the paper used and which are missing from the archive.
- Whether units on consecutive days are the same neuron. Per-unit waveform, depth and ISI comparisons across days within each mouse, or results using one session per animal, would settle it.
- The clock in sessions other than anm372906 2017-06-08. Running the `compare_with_processed` check for all 53 sessions, not just one, would confirm the spike-time reconstruction and the first-10-trial shift everywhere.
- Per-unit p-values for the 7 sessions with unverified clocks, which would show whether those units are counted as selective.
- A test against the paper's Extended Data Fig. 9 measure: single-unit decoding accuracy in the first 400 ms of the sample epoch, PTupper against PTlower (≥ 70% accuracy: paper 15/61 against 3/69). This would test pt-types-differ-in-timing part (a) the way the paper did.
