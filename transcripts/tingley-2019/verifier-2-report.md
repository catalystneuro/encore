## Verifier report, round 2: Tingley & Buzsáki 2019 on DANDI:000218 (0.261110.1911)

The claims file has 39 claims and the attempt record has 39 outcomes: 9 reproduced, 11 partially reproduced, 9 not reproduced and 10 blocked. My round-1 report said 9 were blocked; that was my miscount, and the correct number is 10.

### 1. Outcomes and assumptions

I agree with all 39 stated outcomes. Comments on the ones that rest on assumptions, or should:

- **fig1c-post-burst-suppression (not_reproduced, assumed).** In round 1 I disagreed. I now agree. The claims file names both windows and does not say which decides. Taking the window from each event's stop as "immediately following the population burst" is stated and reasonable. Under that window no seed shows suppression (main cell 24). The +20..50 ms window passes under 3 of 5 seeds and in 1 of 6 animals.
- **ls-spikes-not-locked-to-ca1-ripples (not_reproduced, assumed).** In round 1 I said partially_reproduced, but the criterion only allows reproduced or not reproduced. I now agree with not_reproduced. Using spikes inside CA1 ripples is stated and the closer reading of "individual waves". The result is marginal: 43 of 599 neurons are locked (7.2%), binomial p = 0.012, against a 4.9% shuffle null (LFP cell 16).
- **fig1h (reproduced, assumed).** Stated and reasonable. The recomputed maximum NSS differs in scale (median 4.69 against 8.03) and gives r = 0.081, p = 1.3e-38. So the outcome rests on using the deposited `peak_normed_power`, which is the lab's own value.
- **fig4b-pre-post-unchanged (partially_reproduced, assumed).** Using the normalized CCG is reasonable. Raw counts carry the extra HFO time in POST (355 s against 252 s). Part of the justification is misstated (see section 2, cell 47).
- **fig4b-hfo-above-behav (reproduced, assumed).** The flag overstates the dependence. Under raw counts with BEHAV inside trials (the claims file's reading iv-a), both parts also hold (main cell 49, rows 1, 5, 9 and 13).
- **fig5e-state-coupling (partially_reproduced, assumed).** Pooling all HFOs is stated and reasonable: the paper's NREM fraction of 0.3 matches the pooled 0.302. The pooled test treats HFOs as independent, and DT9 supplies 9,783 of the 15,605 NREM HFOs. In DT5 the gap is small (0.160 against 0.131).
- **dataset-composition (partially_reproduced, not flagged as assumed).** The partial bound needs 4 of the 6 counts to be within tolerance. Two of the four count only under choices the attempt made:
  - CA1 recordings = 38 only if units labelled `hpc` count as CA1. The `ca3_channel` flag reading gives 29.
  - CA1-rate recordings = 55 only if `ripplesALL` counts as CA1 ripples. CA1Ripples alone gives 47, below the lower bound of 47.7.

  Dropping either choice leaves 3 of 6, which is not_reproduced. Both choices are listed as deviations and are reasonable, but the outcome should carry `assumed: true`. I accepted 55 in round 1 without noticing it was decisive.
- **fig7e-ca1-spikes, fig7e-state, fig7e-duration (partially_reproduced).** These follow from the claims file's t-test reading, judged against that test's own chance rate. They are open: under the z reading, each claim is within tolerance in 3, 4 and 2 of 16 combinations, which the criterion would score as reproduced. That question is now with a reader.

The remaining outcomes are unchanged from round 1 and still match the printed outputs.

### 2. Sentences the numbers do not support

- **Main cell 47 (fig4b-pre-post-unchanged):** "BEHAV medians are 10 to 100 times the HFO ones in raw counts". The printed raw medians are comparable: BEHAV 0.088–0.66 against PRE 0.32–0.44 (cell 45). Only the means differ that much: 13.1–83 against 0.60–0.85 (cell 49).
- **Fig. 7E cell 11 and the record's notes for fig7e-state:** "binomial p <= 3.2e-9". Cell 9, row 46 (state, start-stop, Poisson, cross-validated) prints 1.23e-08. The largest p is therefore about 1.2e-8. The outcome does not change.
- **Main cell 72 (Summary, dataset section), the record's last metadata_insufficient finding, and its fig7e-ca1-depth response:** "each unit has one waveform" / "one raw_waveform per unit". Main cell 8 shows no `raw_waveform` column at all in the units tables of DT5, DT7 and DT9. The block of fig7e-ca1-depth still stands.
- **README run times:**
  - Figure 7E notebook, "about 16 minutes": its cell 9 alone prints "computed in 1141 s" (19 min), before the seed reruns and loading.
  - Own-shank notebook, "about 30 minutes": it prints 172 s of loading plus 9.5 min of jobs, about 13 min.

Every other sentence I checked matches the printed outputs: all "**Result:**" cells, the Summary, the rest of the README, and the record's notes. That includes the new numbers: 1615 of 1992 (81.1%); 20182 / 10823 / 795 / 954 / 462 pairs; the pooled p = 3.1e-171; 1264 neurons with smallest p 0.59; and the z-reading ranges.

**My round-1 reasons in the record:** all 39 are there under `verifications` and faithful. Most are my wording with the relevant B and C points attached. Nothing is misattributed.

### 3. Round-1 points

**Resolved:**
- **B3:** `peak_normed_power` is now the primary amplitude, and an LFP check was added.
- **B4:** the pooled-HFO test was run and the outcome changed.
- **B5:** the own-shank reading now covers every neuron (81.1%, still below 83.25%).
- **B7:** "WAKE outside trials" was run.
- **B8:** settled by the stated window assumption.
- **B9:** the conclusion now says the positive control is weak.
- **B10:** no change needed.
- **B11:** blocked_by changed to "other" with the correct reason.
- **Section C:** the electrode and unit columns, the per-site label profiles, and the `peak_normed_power` check were all done.

**What remains that bears on a conclusion:**
1. **Figure 7E (B1).** The z reading was run and the question was passed to a reader, as the protocol asks. It is still open, and an answer could move all three claims to reproduced. A further claims-file issue to report: the criterion "within tolerance under one combination", applied to 16 combinations spanning 11–79%, is nearly impossible to fail.
2. **Figure 4 pairs (B2).** The cause is now shown: pairs are lost to the inclusion rule inside the HFO epochs (795 pass in PRE and 954 in POST, against 10,823 in BEHAV). Every Figure 4 claim still rests on 361–503 pairs, about 6% of the paper's 7,172. The Methods say only "only spike pairs where both neurons fired more than 5 spikes within 200 milliseconds of each other were included", for CCGs "for each epoch". The claims file applies that rule to HFO-only spikes in every epoch and names no reading that applies it over the whole epoch. That untested reading would probably retain far more pairs. I report this as a gap in the claims file, not a correction.
3. **dataset-composition** needs `assumed: true` (section 1).
4. **fig2 and discussion-medial-septum (B6, does not change the outcomes).** The septal-shank labels alternate along channel order, so whether the labels are reliable cannot be settled. The two-chunk limit is unchanged. Both outcomes rest on the labels, as the record states.
