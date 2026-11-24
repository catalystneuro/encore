**Verifier report, round 2: senzai-2017-02 (Senzai & Buzsáki 2017, DANDI:000003 0.261122.2143)**

Counts come from the files. The claims file has 31 claims. The attempt record has 31 outcomes: 17 reproduced, 8 partially reproduced, 4 not reproduced and 2 blocked. Two outcomes are flagged `assumed: true`: tmaze-multiple-fields and inheritance-tmaze.

## 1. Outcomes and assumptions

**I agree with 28 outcomes as tested against the criteria.**

**pv-remap (reproduced, seed sensitive):** I now accept this as the literal outcome. At the claim's seed, the GC median is below the MC median at every size (n = 20: 0.2877 against 0.2902) and the Kruskal-Wallis P is below 1e-5 (cell 91). This withdraws my round-1 rating of partial. The remaining problem is in the claims file (see 3).

**gc-mc-distance and gc-backpropagation (blocked):** I agree they are blocked. I still disagree with `metadata_insufficient` as the reason (see 3, point 8). The real block is that the claims file gives no criterion for either claim.

**Assumptions:**
- tmaze-multiple-fields: fields are taken from the highest local maximum down. This is stated in the deviations, reasonable, and asked of the authors.
- inheritance-tmaze: uses the same fields. Stated and reasonable.
- One assumption is not flagged anywhere. Each T-maze run starts at the mouse's last entry into the central arm, because the files do not mark the gate opening. Cell 63 calls this "an assumption", and it bears on tmaze-central-active, tmaze-peak-info and tmaze-splitters. None of these outcomes is flagged `assumed`, and the record gives it only as a deviation.

## 2. Sentences the outputs do not support

**Cell 102 (Summary) says:** "in the others the match is no better than with another day."
- The record's finding 11 ("no more often than with another day") and the round-1 response under unit-counts ("the match is no better than with another day") say the same.
- Cell 5 contradicts this for two of the six pairs:
  - YutaMouse54b160702: 0.10 of units above 0.95 on the same day against 0.00 on another day, with median r 0.864 against 0.512.
  - YutaMouse56b160915: no units on another day (NaN), so there is nothing to compare with.
- Cell 12's own wording ("in two of them a file of another day matches as often or more often") is correct.

**Cell 15 and the first-stage-labels note say:** "With the waveform source changed, no variant meets the criterion in all three groups."
- This is true only of the changed sources.
- The stored-waveform variant on the 17 wide-band files does meet all three groups: 0.936, 0.987 and 0.906 (rows 6–11 of cell 14). The sentence quotes these numbers without saying that they pass.
- So the shortfall of 0.899 for narrow-waveform interneurons depends on which units are included as well as on the waveform source.

**Everything else checks against the outputs.** I checked every other number in the "**Result:**" cells, the Summary, the README and the record's notes, including these per-mouse counts:
- 13 of 14 and 8 of 14 mice (cell 26)
- REM above wake in every GC mouse (cell 29)
- CA3 wake highest in 3 of 6 mice (cell 29)
- theta MRL higher for GC in 12 of 13 mice (cell 35)
- MC above GC in 14 of 15 files for DS2 (cell 44)

**Round-1 reasons in the record:** all 12 points and the section-C requests appear in the `verifications` block. They are stated faithfully and close to my own words.

## 3. Status of round-1 points

**Resolved:**
- **2:** the classification now uses the unfiltered wide band: 0.944 under all five seeds (cell 47).
- **4:** per-pair table added (cell 58).
- **6:** count-matched control added (cell 38).
- **7:** NaN fixed, and the Freeman-Halton exact test gives P = 0.835 (cell 77).
- **9:** the shank variant is reported.
- **10:** the MC half is reported.
- **12:** circular permutation test added.
- **Section C:** filter attributes (cell 7), the hilus_reference DS2 (cell 8) and the linearisation table (cell 66) are all added.

**Resolved as analysis; the conclusion now rests on the claims file:**
- **Point 1, optotag-drd2.** The per-bin reading gives 28 of 106 MC (0.264, within tolerance), 0 GC, 7 of 62 wI and 0 of 68 nI, with 28 of the 29 tagged MC among them (cell 23). The claims file's mean-rate criterion, which ignores "suppressed significantly", looks like a misreading of the Methods. Under the per-bin reading the claim would be reproduced. The question has been put to a reader.
- **Point 5, gc-narrower-waveform and first-stage-labels.** The files state no filter for the stored waveforms. With the unfiltered wide band, the GC < MC result depends on how the peak is defined: P = 0.175 to the largest later sample, P = 7.9e-10 to the first local peak (cell 20). The outcome is correct on the criterion but fragile, and this is disclosed.

**Still open, bearing on a conclusion:**
- **Point 3, pv-remap (a claims-file issue).**
  - The claim's own `statistics` list a Bonferroni post-hoc test at n = 20 with P < 1e-5. The statement is "smaller … than mossy cells", which only the post-hoc test addresses.
  - At the claim's seed, the GC-vs-MC post-hoc test gives P = 0.84 (cell 91). So this fails at seed 0 itself, not only under other seeds.
  - The criterion leaves the post-hoc test out. Under the claim's own statistics the outcome would be partial.
  - The P-values come from 1000 resampled draws of 24 GC place cells, so they shrink as draws are added and say little about the cells. The draw-level probability that a GC draw is below an MC draw, which does not grow with the draws, is 0.514–0.537 at n = 20.
- **Point 8, blocked claims.**
  - The record argues that a negative Spearman correlation on 43% of the shanks where the DS2 reverses means the shank list is not in depth order. That test cannot tell the two cases apart.
  - Below the hilus, a shank that descends into the infrapyramidal blade sees the DS2 reverse again. The record's own example, YutaMouse42, goes from +0.39 to −0.83 over days while the probe was lowered 70 µm a day, which fits a shank moving into that blade.
  - Cell 100's example shank shows a smooth, monotonic DS2 profile in list order (−793 to +1323 µV), while channel_id runs interleaved (33, 40, 32, 41, …). That is the pattern of a list in depth order.
  - A smoothness test would settle it: compare adjacent-site differences in list order against random permutations.
  - Finding 1's sentence "The DS2 profile does not settle it either" is stronger than the evidence allows.
- **Point 11, same-day files.** The data are suggestive for YutaMouse51 on 16 May: 5 of 9 units match above 0.95, against 0 of 9 on another day. It remains unsettled, and the effect on counts is small.

**Also noted, not bearing on a conclusion:**
- **Contradictory claims file.** The header and the mc-deeper criterion say only 17 files give each unit's shank, but the record and cell 61 use a shank column present in every file.
- **Arm assignment in the T-maze runs.** Cell 66, run 1, is a right-turn run whose first excursion goes to positive angles (+0.19 to +0.36 rad), the left-arm side. Those samples are linearised onto the right arm (65–77 cm). Short excursions into the arm not chosen are therefore binned into the chosen arm. The effect is probably small.
- **Spike loss at light onset.** In cell 23, the +1 ms light-onset bin falls to 0.27 of baseline for all units, which looks like spike loss at onset. It lies outside the +2 to +15 ms window used, but nothing checks whether it extends into +2 ms.

## 4. Critical findings

No finding in the record is rated `critical`. Their ratings are:

| # | Rating | Kind |
|---|---|---|
| 1 | major | metadata_insufficient |
| 2–4 | minor | |
| 5–6 | none | |
| 7–10 | unrated | methods_unavailable |
| 11 | minor | |

Finding 11 (same neurons possibly recorded in both files of a day under different global_ids) would be `critical` if it were shown, because it would be one unit deposited as two. Cell 5 does not establish it, so `minor` is appropriate for now.
