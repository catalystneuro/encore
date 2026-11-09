**Verifier report, round 2: Kyzar et al. 2024 (doi:10.1038/s41597-024-02943-8), DANDI:000469 v0.240123.1806**

The claims file has 20 claims, and the attempt record gives 20 outcomes: 18 reproduced, 1 not_reproduced (persistent-activity) and 1 blocked (probe-cells-mfc, methods_underspecified). I re-checked these against the claims file's criteria, not against any table.

### 1. Outcomes and assumptions

- **Outcomes:** I agree with all 20. They are the same as in round 1, and the new outputs do not change any of them:
  - Cell 59: the Sternberg concept counts stay in tolerance on 3 more seeds.
  - Cell 68: maintenance counts with ties counted are 139 to 142, all in tolerance.
  - Cell 71: with ties counted, label shuffling gives 108 and 103 (out) and sign flipping gives 118 and 111 (in), so the readings still disagree.
- **Assumptions:** no outcome carries `assumed: true`, so there are none to judge.
  - The only outcome that rests on an unstated choice is isi-violations, which needs the code's filter (units below 4%).
  - The record states that choice as a deviation and in a `selection_undocumented` finding, and the criterion allows either reading.
- **Claims file:** I found no misreading of the paper, as in round 1.
- **Helper check:** I read the new `_exceed` in `sternberg.py` (lines 234 to 239). It counts values equal to the observed one with `isclose` on top of `>`, which is correct. I could not run it, because numpy is not installed here.

### 2. Statements the printed outputs do not support

- **Cell 73 (Summary):** "every number in the paper's quality and behaviour sections is recovered from it."
  - The same section of the paper gives 449 screening MTL units, but cells 16 and 73 give 421.
  - The ISI s.d. is recovered only with the code's filter; over all units cell 31 gives 0.625.
  - Mean SNR does not match (cell 40), though the claim allows the peak SNR reading.
  - The sentence should be narrowed.
- **Cell 73, and the record's `metadata_error` finding:** "Two column descriptions are wrong (`waveforms_mean_proj_dist` …, `loadsEnc3_PicIDs` …)", and the electrodes "my description". No cell prints any column descriptions, so the notebook output gives no evidence for this.
- **Record, finding `other`:** "99% of trials are 0.93 to 1.20 s". Cell 5 prints the 1st and 99th percentiles, which bound 98% of trials.
- **Record, subjects-sessions notes:** "with different units and electrodes". The different units are supported by cell 5 (no duplicate spike trains, different unit counts). Electrodes are not printed.
- **Record, response to the persistent-activity point:** "two of 2673 trials do not move any result".
  - Nothing in the notebook tests this; no output shows a run without those trials.
  - There are now three flagged trials in cell 5 (the subject 21 trial with a 14.07 s fixation is the third).
  - With one such trial per session it is very unlikely to matter, but the sentence states it as a result.
- **Cell 72:** "whether the trials are paired … that choice decides the outcome". This is largely right, but under label shuffling the encoding-rate choice also matters: the pooled rate passes on 3 of 4 seeds and Encoding 1 fails on all 4. The record's probe notes give both open questions correctly.
- **README:** "It takes about six minutes". No output shows a run time, so I cannot check it. Every other README sentence and table row matches cells 13, 16 and 62 and the parametric variants (138, 26, 94, 144, 122, and 4.764/4.709/2.673/3.656).

Every other sentence I checked matches the printed numbers. That covers all the Result cells, the rest of the Summary, and the record's notes and findings. Examples:

- Cell 63's "2.57 to 3.13 Hz" and "every p below 1e-5" (the largest maintenance p is 6.3e-07).
- The record's "below 1e-6".
- 3.05 against 2.70 Hz (parametric, all cells, maintenance, Encoding 1 trial reading).
- "16 of the 19 subjects", "56 of the 140", and the 0.03 ms and 14.07 s timestamp gaps.

**How the record restates my round-1 reasons:** they are in my own words, all 8 problems are attached to claims, and the reviewed-materials line is accurate. One restated figure is wrong, and the error is mine. The persistent-activity reason says "p at most 1.7e-7", copied from my round-1 report. Cell 62 shows a largest maintenance-window p of 6.3e-07 (concept_one, MTL, Encoding 1 trial reading). That reason should read "p at most 6.3e-7", or "below 1e-6". The outcome does not change.

### 3. Round-1 points

**Resolved:**
1. Tie handling: added as a variant in cells 68 and 71. Maintenance stays in tolerance and the probe readings still disagree.
2. The screening MFC count depends on the seed: still 27, 29, 28 and 27. This is now stated, and the 20,000-permutation refinement gives 26.
3. Tolerance flags for the probe seeds: now printed in cell 71.
4. Seed repeats for the Sternberg concept counts: added in cell 59, and all in tolerance.
5. Anomalous trials: now listed in cell 5 (three trials) and in the findings. They are kept, as the code keeps them, but see the unsupported sentence in section 2.
6. Subjects 13 and 14: already in cell 11 and in the record.
7. Parametric tests against permutation tests: stated in the summary, the README and the question to the authors.
8. Unsorted spike times: now a `format_error` finding for 4 units.

**Items from round 1 I could not check, now checked:**
- Encoding 2 and 3 timestamps are exactly 0 when the load leaves them out, and at least 2.0 s when shown (cell 5). So the condition `encoding_rate_pooled` needs (onsets greater than 0) holds.
- I inspected the RT figure (cell 23). It agrees with the printed means and range.

**Not in my round-1 report, does not bear on a conclusion:** cell 7's clock check lists 18 files where shift 0 is not the highest. These are mostly small files, the TTL check finds no mismatch, and no conclusion uses this check.

**Still open, bearing on a conclusion:**
- probe-cells-mfc is blocked only under the claims file's rule of using the permutation tests the Methods name. The code's parametric test gives exactly 122. Settling it needs the authors' answer, which the record already asks for.
- screening-concept-mfc passes by about one unit at 2000 permutations (one seed of four is outside tolerance). The outcome rests on the 20,000-permutation refinement, which gives 26.

No other remaining issue bears on a conclusion.
