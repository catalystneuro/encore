**Round 2 verifier report: Porniece et al. 2025 on DANDI:001474 (attempt 001474-porniece-2025-01)**

**1. Outcomes**

The claims file has 37 claims, and the attempt record gives 37 outcomes. I agree with all 37.

- **Unchanged from round 1 (35 claims).** These are the 35 outcomes in my round-1 table other than supp3q. The re-executed outputs match the numbers I gave. Cell indices have moved: for example, fig1k is now cell 26, fig2c cell 59 and supp3q cell 140.
- **fig2km-elevated-early-at-matched-licking: reproduced. I agree.** My round-1 table left this claim out: I wrote "37 claims" but listed 36, and the record says so correctly. In cell 74, under Z2 and Z2p (4 of the 8 W×Z combinations), both the 45–59 and 60–74 groups pass. The HFD early response is above NCD by 0.43–0.77, more than the sums of s.e.m. (0.22–0.28). The early lick rates differ by 0.12 and 0.02, less than the sums of s.e.m. (0.86 and 0.63). Under Z1 and Z1p the 60–74 group fails, with HFD below NCD. Without the 58 modal-offset recordings it still passes in 4 of 8 (cell 143). The criterion asks for one combination, so the outcome is reproduced.
- **supp3q-hfd-ncd-weight-loss-meal-length: now partially_reproduced (assumed). I agree.** Cell 140: under C/B, Z1 gives (ii) p = 0.039 and 0.043. Meal length passes only under C/B (p = 0.023); the other three weight-change readings give p 0.09–0.14. The assumption (`ad lib bw` read as B and `before ad lib bw` as A) is stated, and it is reasonable given the values in cell 107.
- **supp3m-weight-gain-response: partially_reproduced (assumed). I agree.** At ≥30 triggered trials, no combination puts both r in tolerance, and 11 of 16 combinations have both r > 0 with p < 0.05 (cell 134). The assumption (≥30, the Methods' default) is stated and reasonable.
- **fig2c-delta-z-recordings: reproduced. I agree, but the outcome rests on a choice the record does not mark as an assumption.** It holds only if the 58 modal-offset recordings are included. Without them, HFD is 0.20–0.23 and the claim would be partially reproduced (cell 143). The choice is defensible: the 13 cohort-2 modal recordings it uses all pass check (b) in cell 17, and 11 of the 13 peak within 1 s. Because the outcome flips on this choice, it should carry `assumed: true` with the reason given.

**2. Statements the printed numbers do not support**

I checked every Result conclusion, the Summary, the README and the record's notes against the outputs. The numbers hold everywhere except the alignment wording below.

- **Cell 18:** "larger in 242 of 285 and 49 of 58 recordings, so no recording is shifted by whole trials."
  - These are counts, so they show 9 of the 58 modal recordings failing check (b). Examples from cell 17 are all four MPK147 second-phase files (2024-05-21, 05-23, 05-28, 06-05), MPK133 2024-04-15 and MPK174 2024-10-11; for some of these the tone response in the first five trials is near zero or negative.
  - For these 9 the check proves nothing either way.
  - The same cell says the recordings that peak 1–11 s late "are recordings with a weak tone response, not shifted ones." That is an inference the outputs do not show.
- **README, and the record's alignment deviation** ("a check on the tone-evoked rise … places their trials as in the correlation-aligned files"): this holds for the 58 as a group, not for every recording.
- **Outside the scope I was asked to check:**
  - Cell 11 gives raw-trace lengths of "67 to 106 min". Cell 10 prints 51.7–142.7 min.
  - Cell 21 says "Z0 is thus close to a per-mouse rescaling of dF/F0". The per-recording intercepts vary (SD 0.22, from −1.06 to 0.66), and those level differences are what separate Z0 from Z2. For example, NCD early is −0.17 under Z0 and 0.43 under Z2 (cell 26).

The `verifications` block states my round-1 reasons faithfully and in my own words. It correctly records that I gave no outcome for fig2km.

**3. Round-1 points**

Resolved:
- **2:** the supp3q outcome has been changed.
- **4:** cell 134 now prints which trial threshold decides supp3m, with counts at each threshold.
- **5:** the notes now say where each pass is fragile.
- **6:** the conclusion explains why the division readings rise.
- **7:** the MPK191 date is now flagged.
- **8:** the Fig. 3 legend itself says "at least 30/90 trials", so the claims file follows the paper. I withdraw the point.
- **9 and 10:** both are stated.
- **Section C requests:**
  - The tone-locked averages are in cell 17.
  - The rerun without the 58 recordings is in cells 143–144.
  - The Z0 against Z2 comparison is in cell 20.
  - The raw notes are printed in cell 107.

Partly resolved:
- **1 (alignment of the 58 modal-offset recordings).** The check and the rerun answer it for every outcome; only fig2c would change. What is left is the 9 recordings that fail check (b). Among them, all four MPK147 HFD→NCD second-phase files enter fig3h, fig3i, fig3j and supp3q. No outcome changes without them, but the fig3h drop shrinks a lot (Tukey p goes from 0.11 to ≥ 0.715). `pvh.alignment_check` already computes the "after last trial" slots but the notebook does not print them. Printing them for these 9 would show whether they are shifted.
- **3 (Z reading).** The fig1k-lme outcome still depends on the Z reading: under the depositors' Z0 it passes. How Z0 was made remains unknown, and it is now a question to the authors in a methods_unavailable finding.

What remains that bears on a conclusion:
- **fig2c:** it should be marked `assumed: true`, because it passes only with the modal-offset recordings, under D15, at the edge of tolerance.
- **fig1k-lme:** the outcome depends on how the Z-score is computed, which only the authors can answer.
- **supp3q and supp3m:** their stated assumptions (the meaning of `ad lib bw`, and the ≥30 threshold) are reasonable but cannot be confirmed from the files.
