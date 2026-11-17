I revised the attempt after round 1 and re-ran it: 37 claims, now 25 reproduced, 9 partially reproduced, 3 not reproduced and none blocked. Both notebooks pass when run from a clean environment, and the entry check reports 0 errors. Nothing is committed.

**What changed in the outcomes.** The verifier's main point (B1) was that my own rerun of the paper's modulation test picked a different set of units from the authors'. The count matched (310) but only 73% of the units were the same. The data descriptor names the units the dataset marks as modulated as the paper's units, so every dependent claim now uses that set, with my recomputed set shown alongside. Classing that set by the regression gives exactly the dataset's own class labels. Outcomes that changed:
- **fig6e-unit-classes** and **fig6fg-laminar-classes**: partially reproduced → reproduced.
- **fig8d-slow-positive-right-choice-l5**: partially reproduced → reproduced. L5a is only just significant (p = 0.049) under reading (a).
- **fig7de-medium-suppressed**: partially reproduced → reproduced. The verifier would give not reproduced, because none of the three negative responses differs from zero (p 0.45 to 0.72). I recorded that disagreement; the criterion only asks that all three means be negative.
- **fig7-fff-adaptation**: partially reproduced → reproduced. Every version of the impulse t test picks 29 to 37 of the 62 Fast RS units, while the paper reports 61. So the claim now uses all 62 units, which is an assumption. On them the ratios are 0.744 and 0.663 with p = 0.037 and 0.013.
- **s5-slow-positive-no-integration**: reproduced → partially reproduced. Pulse 3 differs across sequences on right-choice trials (p = 0.016).
- **fig9b-stimulus-decoder-slow-chance**: reproduced → partially reproduced. The value is 33.9%, within tolerance, but above chance by both tests.
- **fig9d-single-bin-decoder**: reproduced → partially reproduced. The value is 38.2%, 0.5 points below the tolerance.

These eight, plus fig7-sss-no-adaptation and s4-fms-middle-pulse, are marked as resting on an assumption. Each note says what the other unit set gives. On fig8e-choice-divergence-125ms I removed the assumption flag, because the onset is now 120 ms whichever end of the third impulse is used.

**What I added or corrected, by verifier point:**
- **B1**: added the shuffle-bins test the verifier asked for. It marks 365 units on the stored window and 321 on the paper's window, and neither matches the stored set. Modulation-dependent claims are shown on both sets.
- **B2 and B3**: added an F-response test on first impulses only, and the all-Fast-RS selection. Per-unit ratios now need a pulse 1 response above 1 Hz, which removes the ratios of about 1e13.
- **B4**: the smoothing window can now sit centred, before or after each time point, or be left out. Ties take the mean time, so a single spike at 12 ms reads 12.5 ms. No reading puts all five layers within tolerance. Impulse segments now run to 50 ms, so the smoothing needs no zero padding.
- **B7**: impulse speeds for s5 now come from the paper's speed profiles (sheet "Fig S1" of the supplementary data).
- **B8**: training-days now also counts sessions per rat (12 to 22). The minimum is still outside tolerance.
- **B11**: added a trailing window for fig8e (onset 124 ms).
- **Baseline rates**: added the paper's S1 Table (doi:10.1371/journal.pbio.1002549.s010) as a new input. It gives 10.8 Hz for L5a RS units, against 11.40 Hz here. By its counts, the dataset's 33 extra units are all in L2/3 to L5b.
- **Choice decoder**: added accuracy against the number of units. Twenty Slow units give 66 to 74%, and single units average 54.9% (Slow) and 52.1% (Fast/Medium).

I updated the notes, measured values, deviations, inputs and findings, and recorded round 1 under `verifications` in the attempt record. All conclusions and both summaries were rechecked against the new outputs.

**Not done, and why:**
- B5, B6, B9 and B10 needed no change, and the response for each says so.
- I did not add a label-shuffle null for the Slow decoder (B6). The current test's weakness is stated in the notes instead.
- The verifier found no place where the claims file misreads the paper, so `questions/mcguire-2016.yaml` is unchanged.
- Rewriting the attempt record with a YAML library re-wrapped all of its long text lines, so its diff is larger than the content changes.
