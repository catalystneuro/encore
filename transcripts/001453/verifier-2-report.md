**Verifier report, round 2: Fouke et al. 2025 (doi:10.1016/j.cub.2025.04.027), dandiset 001453 v0.250518.1950**

The claims file lists 20 claims, and the attempt record has 20 outcomes: 7 reproduced, 1 partially reproduced, 2 not reproduced and 10 blocked. I did not download the paper again for this round, because no new statement needed checking against it.

### 1. Stated outcomes

I agree with all 20.

- **stimulus-code-link (reproduced):** agree.
- **fig1d-dc-faster-all-codes (reproduced):** agree.
- **fig1d-median-velocity (reproduced):** agree.
- **fig1d-zf-forward-faster-than-static (reproduced):** agree.
- **fig1d-dc-no-modulation (not reproduced):** agree. The criterion is met: 3 of 36 DC pairs are significant (cell 36). The paper code's own printed Tukey output finds the same three pairs (cell 37). All three come from one DC-sub-2 static trial at 106.5 mm/s. The record says this.
- **fig1d-dc-faster-oblique (reproduced):** agree, but it is marginal. It passes under reading (b) only, with 2 of 4 stimuli.
- **fig1g-follow-direction (partially reproduced):** agree.
- **fig1h-zf-higher-angular-acceleration (not reproduced):** agree. 0 of 9 stimuli meet the criterion under the Methods definition, and 0 of 9 with the heading taken from `f0_theta`.
- **figs1e-dc-respond-less-monocular (reproduced):** agree, under the 9/11 assignment the claims file fixes. The lateral part is fragile (see 3).
- **fig1c-continuous-vs-bouts (reproduced):** agree.
- **fig1cef-representative-values (blocked):** agree. The record keeps `metadata_insufficient` where I had suggested `methods_underspecified`. Its reason is that the code names the fish by folder, and the dandiset has no mapping from folders to subjects. I accept that.
- **The 9 imaging and tail-tracking claims (blocked, data_missing):** agree.

### 2. Statements the outputs do not fully support

I checked every sentence; the rest match the printed numbers.

- **Cell 17:** "Their speed is high because it is measured over a short motion phase (under 1 s in 9 of them). The exception is the DC-sub-2 static trial, 106.5 mm/s over 14.6 s."
  - Cell 16 shows two of the 11 DC trials are not short. DC-sub-2 forward_backward runs 7.3 s at 132.1 mm/s, as well as the static trial.
  - So there are two exceptions, not one.
- **Summary bullet, cell 57, and the finding on `dist`:** "the code's speed check on it passes trials whose speed over a short motion phase is above 100 mm/s" and "The paper's speed check uses it."
  - Both read as if `dist` caused these trials to pass. Cell 16 shows the check from positions passes exactly the same trials ("passing one check and not the other: {}").
  - The real cause is the 0 to 35 s window, as cell 17 itself says.
  - The trial that drives the outcome, DC-sub-2 static, is 14.6 s long, not short.
- **Cell 49, the Summary's last bullet, and the fig1h notes:** "DC values are as high at rest as during motion, which suggests a tracking-noise floor."
  - The numbers are right. But cell 48 shows ZF are also higher at rest than during motion: ratio 1.07, Wilcoxon p = 0.00012.
  - So this comparison does not separate DC from ZF, and is weak evidence for a DC-specific noise floor. The fig1h notes give the ZF medians but leave out the ZF test.
  - The hedge "may be" holds. "Suggests" claims more than the outputs show.
- **Attempt record, fig1d-zf-forward notes:** "the start of a 4-hour blank block."
  - Four hours is the protocol's length. Cell 9 prints observed code-20 blocks of 0.2 to 787.3 min.
- **Cell 38 and the fig1d-dc-no-modulation notes:** "two at 0.0" sits next to "no fish median is exactly 0" (cell 19).
  - Both are true, since the 0.0 values are rounded, but the text should say "near 0".

My round-1 reasons are stated faithfully, in my own words, in all 20 `verifications.results` entries. My Problems 1, 2 and 4 are folded into the reasons of the claims they affect, and my requests from section C are included. Small omission: the fig1h reason leaves out my figure for ZF (code interval 1.4 times the frame interval). It does not change the meaning.

### 3. Round-1 points

**Resolved:**

- **Point 2, DC speed rejection:** the table is added, and a check from positions changes no trial. Only the wording in cell 17 and the Summary remains (above).
- **Point 3, static window:** the code's window is now documented, and the zero-median variant makes no difference. The DC static miss (10.52 against 11.9) is still unexplained beyond the missing `vel` filter. It no longer affects an outcome, because the paper's own Tukey test gives the same three pairs.
- **Point 6, independence in the ANOVA:** a per-fish Mann-Whitney test is added (p = 0.02).
- **Points 7 and 8 and the frame-rate question:** raw timestamp intervals are added (cell 5), and they show the rates are real. The DC label timing is now listed as a deviation.
- **Point 5:** handled by the existing 30 Hz variants and the frame-rate splits.

**Remaining, bearing on a conclusion:**

1. **figs1e-dc-respond-less-monocular:** the new time courses (cell 21) show both species turn right more to code 11 than to code 9.
   - DC: 10 of 12 fish, p = 0.0093. ZF: 16 of 25 fish, not significant.
   - Both species turn with the motion for medial and binocular stimuli. So the protocol file's assignment (11 = lateral right) is the more likely one.
   - Under that assignment, DC are not below ZF on lateral stimuli (cell 52), and the claim would be partially reproduced.
   - The outcome follows the fixed criterion. But the reproduced label rests on the assignment the data argue against, and on a 0.95 deg/s difference (p = 0.96).
2. **fig1h-zf-higher-angular-acceleration, the noise-floor point:** the not reproduced outcome stands.
   - The evidence for "noise floor" does not separate the species (see 2).
   - The direct test is still missing: acceleration in frames where the fish is still (speed near 0), by species.
   - Until then, the reversal may come from noise or from DC's continuous swimming, and neither the notebook nor this report can say which.
3. **fig1d-dc-no-modulation:** the outcome stands on a single DC-sub-2 static trial.
   - It averages 106.5 mm/s over 14.6 s in a 100 mm dish, which is almost certainly a tracking artefact.
   - The record is honest about this, and the paper's own output agrees. A reader should take the outcome as a property of the paper's test on this data, not as evidence that DC modulate their speed.
