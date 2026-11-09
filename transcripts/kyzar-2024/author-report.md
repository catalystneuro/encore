I've done steps 1 to 6 of the Author section. The entry `entries/000469-kyzar-2024/` passes `python tools/entry.py all` with 0 errors, the notebook runs in 322 s from a clean environment, and the handover package is built. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| subjects-sessions | reproduced |
| sternberg-unit-yield | reproduced (every count exact) |
| screening-unit-yield | reproduced (907 units; the MTL holds 421, not 449) |
| behavior-accuracy | reproduced (88.73%) |
| behavior-rt-load | reproduced (F(2,40) = 7.92, p = 0.0013) |
| behavior-accuracy-load | reproduced |
| isi-violations | reproduced, only with the code's filter (0.416 ± 0.498%) |
| firing-rate, projection-distance, waveform-snr (peak SNR), cv2, isolation-distance | reproduced |
| screening-concept-mtl | reproduced (140, 33.25%) |
| screening-concept-mfc | reproduced (27, 5.56%; depends on the seed, see 3.3) |
| fig4-screening-examples | reproduced |
| sternberg-concept-mtl | reproduced (96 and 100 under the two readings) |
| persistent-activity | not reproduced |
| fig5-sternberg-examples | reproduced |
| maintenance-cells-mfc | reproduced (139 to 144) |
| probe-cells-mfc | blocked, `methods_underspecified` |

## 2. Dataset, assumptions and questions

**Version.** I pinned 0.240123.1806, the latest published version, because the paper cites no version. All four published versions and the draft hold the same 41 assets, and the notebook checks this.

**Findings recorded:**
- **Screening MTL count.** The paper's "449 MTL units" for screening is the Sternberg count. The screening files hold 421, which matches the paper's own percentages.
- **Persistent activity.** The paper's values (4.76 ± 4.71 against 2.67 ± 3.66 Hz) come out exactly from the Encoding 1 window rates of the code's 119 parametric concept cells, not from the maintenance window. In the maintenance window the effect has the right direction (p < 1e-6) but is far smaller (about 2.6 to 3.1 Hz against 2.1 to 2.8).
- **Parametric tests.** The code's parametric tests reproduce every published count exactly (138, 26, 94, 144, 122). The Methods name permutation tests instead.
- **Unsorted spike times.** Four units have spike times out of order (`format_error`).
- **Wrong column descriptions.** `waveforms_mean_proj_dist` is described as isolation distance, and `loadsEnc3_PicIDs` as Enc1.
- **Possibly one patient.** Subjects 13 and 14 (P39CS and P39CS_2) may be the same patient, so "21 patients" may be 20.
- **Odd trials.** One trial of subject 9 has no maintenance period, and one trial of subject 21 has a 14 s fixation.
- **Undocumented filters.** The ISI filter and the correct-trials-only reaction time filter are not stated in the paper.

**Assumptions.** None of the outcomes rests on one, and none is marked `assumed`.

**Question for the paper's authors** (a `methods_unavailable` finding): were the published counts computed with the parametric tests? If permutation tests were used, how many permutations, and were the trials paired or unpaired? For the probe cells, which encoding periods form the encoding rate?

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. **Criterion against step 1.6 for disagreeing readings.** Step 1.6 lets the author adopt the best-supported reading as an assumption. The probe-cells criterion itself says "blocked when the readings disagree". I followed the criterion and blocked it.
2. **"Partially reproduced" against a criterion that says "not reproduced otherwise".** For persistent-activity the effect is present but much weaker, which the protocol calls partially reproduced. The criterion says "not reproduced otherwise". I followed the criterion and said in the notes that the direction holds.
3. **Monte Carlo noise at a tolerance bound.** The protocol does not say what to do when a permutation count sits on the edge. For screening-concept-mfc, one of four seeds puts the count outside tolerance. I kept 2000 permutations as the main result and added a variant that re-tests the units near p = 0.05 with 20000 permutations; it gives 26 (5.35%). I recorded this as a deviation.
4. **Clock check with few units.** Pooled over all units, image selectivity peaks at the true onsets. In 18 of the 41 files the peak is elsewhere, mostly files with few units; the notebook lists them as "not established".
5. **Example attempt out of date.** The attempt the prompt points to (001453) records protocol `pilot-5`, an older version than `pilot-12`. Its format still validated against the current schema.

## 4. Runtime and failures

The run took about 45 minutes of wall time. The final notebook takes 322 s. Two notebook runs failed while I was developing and were fixed: a dict with float keys passed as `**kwargs`, and p-values printed as 0 because of rounding. Nothing failed in the final run.
