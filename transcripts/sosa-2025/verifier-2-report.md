# Round 2 verifier report: 001361-sosa-2025-01

## 1. Outcomes and assumptions

The claims file has 50 claims, and the attempt record has 50 outcomes: 35 reproduced, 1 partially reproduced, 7 not reproduced and 7 blocked. The blocked ones are fig3b, fig3c, glm-well-fit-cells and fig7de as too_large, and fig8e, ed10 and ed5-teleport-fractions as other.

**I agree with 49 of the 50 outcomes.**

**I disagree with one: ed4l-disappearing-decrease.** It is recorded as partially_reproduced; I would record not_reproduced.
- The criterion defines only "Reproduced when the disappearing slope is negative at p < 0.05 in both windows…". It has no partial clause.
- Disappearing far from reward has p = 0.069 (cell 86).
- The attempt applied this same logic to fig4j ("the criterion has no partial outcome"), so ed4l is handled inconsistently with it.

**Agreements that sit at a threshold.** All five depend on the new place-cell test:
- **ed2f:** 6.71% against a lower bound of 6.75%. That is 0.04 points, about 3 cells (cell 54).
- **ed5a:** Holm p reaches 0.047, and day 8 is 9.1% against an upper bound of 9.24% (cell 23).
- **ed4hij:** RR variance p = 0.046; the clustered OLS gives 0.060 (cell 80).
- **ed2jl:** the day-14 count is 731 against a lower bound of 715.5 (cell 45).
- **fig6e:** it passes only under the code's reading, with 8 mice; the Methods' reading gives 7 (cell 125).

**ed7:** I agree with reproduced only for the two image axes. The depth count in the criterion cannot be evaluated, and the record says so.

**Assumptions.** Every `assumed: true` outcome states its assumption in its deviations. Whether each is reasonable:
- **Place-cell test (TwoPUtils `place_cells_calc`): reasonable, with three caveats.** It is the code that the criterion cites.
  - It is read at a TwoPUtils commit later than the paper.
  - The change from round 1 bundles two things: position (with its speed mask) is rolled instead of activity, and a +0.001 offset is added to the rate map. Their separate effects are not shown, and position rolled without the offset "was not run on all sessions".
  - The 0.001 offset is not scale-free. The rebuilt events have a 99th percentile of 0.037–0.087 (cell 5), so 0.001 is not negligible against these events. The files'-series variant gives 49.6%, at a scale where the offset is negligible, which suggests the roll does most of the work. That is a different signal, though.
- **Cross-day matching: reasonable.** It is stated, and two variants are shown.
- **Omissions: reasonable.** The day counts per mouse match both legends exactly (cells 125 and 128).
- **Place fields: stated, but not shown to give the paper's cell sets.**
  - Two-field RR cells are 76 and 84 against 31 and 20 (cell 138).
  - RR primary fields are 5,236 against 2,368 (cell 141).
  - ed3d and ed3fg (not reproduced) and ed3mo and ed3p (reproduced) all rest on these sets.

## 2. Sentences the printed outputs do not support

- **Cell 147 (Summary, "What was found about the dataset") and the record's metadata_error finding:** "The pixel masks' 'x' field indexes image rows" and "`reward_zone` … takes values 0 to 6, and it does not rise on unrewarded trials". No printed output shows either; cell 7 prints only shapes. They may be true, since sosa.py's `read_ophys` comment claims the ranges, but the notebook does not show them.
- **Cell 43 and the fig2i notes:** "On day 3 it is 0 at 130 and 180 cm". The 130 cm value is confirmed by the contiguous-run print. The 180 cm value prints as 0.000 to three decimals, which does not show it is exactly 0.
- **README:** "It takes about 41 minutes". Only the 31.4 minutes of processing is printed (cell 4).
- **Cell 146:** the paragraph "The revision after round 1 did not attempt these analyses either…" appears twice. This is an editing slip.

I checked every other "**Result:**" sentence, the Summary table and differences list, the README counts and statements, and all outcome notes and findings against the outputs. They match.

**My round-1 reasons are stated in my own words.** The record's results paraphrase my round-1 table faithfully. Some add my own B-point references (B1, B3, B11, B12), which is fair. "Agreed with 40 of the 50" is correct: 10 results carry `agrees: false`.

**Claims file (reported, not corrected):**
- The place-cell-fraction criterion asks for "SI as the Methods' formula" and "100 shuffles per cell". It also cites spatial.py:1260-1289, whose test adds an offset and shares one shift per trial across cells. The criterion is internally ambiguous on exactly the point that decides 11 outcomes.
- The ed4l criterion has no partial clause, while its neighbouring criteria do.
- My round-1 points on fig2i and ed8df stand, and they are now routed to reader questions.

## 3. Round-1 points

**Resolved:**
- **B2 (mixed models).** Convergence, warnings, the random-effect variance and mouse-clustered OLS are now printed. fig5i is now not reproduced (p = 0.087, Hessian not positive definite). The fits that did not converge (fig4m far, ed4l non-RR near) agree with OLS.
- **B5–B10.** Each is kept and documented. B9 is justified by the paper's code (dayData.py:1432-1434).
- **B11.** It stays too_large under the protocol rule quoted in the record (41 of 60 minutes are already used). I cannot see the protocol, so I accept it as stated.
- **B12.** Forwarded to reader questions, and the depth point is covered by a finding.
- **Section C requests.** The HDF5 listing (cell 7), the threshold against the SI distribution, the tau 1.0 variant, the convergence output, the per-day field counts and the per-mouse threshold are all provided.

**Partly resolved, and still bearing on conclusions:**
1. **B1 (place cells).** The fraction is now 48.7%, but the bundled change, the offset scale and the later commit (section 1) are open. Eleven outcomes changed on this choice, five of them at a threshold. One run would settle the roll-versus-offset question: position rolled without the offset, on the rebuilt events, across all sessions.
2. **B3 (fields).** Fields are now found on raw events, but the cell sets are still about 2.2–4.2 times the paper's. All four ed3 outcomes rest on cell sets that differ from the paper's.
3. **B4 (matching).** The three matchings agree except fig5f, which is significant only under the TwoPUtils rule (p = 0.032, from a fit that did not converge). One issue remains. RR and TR totals now match the paper, yet the followed counts exceed it under every matching: RR 2,815–3,129 against 2,294 and TR 3,887–4,265 against 3,408 (cell 112). The matching admits more cells than the paper's did, which may dilute the transition fractions behind fig5d and fig5f (both not reproduced). It also uses a rigid alignment instead of Suite2p registration.

**New:**
4. **ed4l** should be not_reproduced (section 1).

**Still not run:** the decoder, GLM, k-means remap-trial and teleport analyses. None is blocked by missing data.
