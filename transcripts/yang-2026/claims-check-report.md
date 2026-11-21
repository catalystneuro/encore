The claims file is ready for an attempt. I fixed seven things, and two open points remain that don't stop an attempt. Nothing is committed.

**Checker:** `claims/yang-2026.yaml: 25 claims, 25 quotes, 0 statistical values, 0 problems`. I ran it before and after my edits and got the same result both times.

**Changes, by claim**
- **fig1-1b-corrected-joint-fraction**
  - The medulla tolerance was 0.0003, but the criterion said 0.003. I set it to 0.003, which the paper's "about 0.003" allows.
  - The paper's "mouse means ranging from ..." can mean two things. I added both as open readings: the region means across mice, or the lowest and highest single-mouse means.
  - The criterion's 0.15 cutoff for "remained low" isn't from the paper; it now says so.
- **fig2d-choice-share-flat**
  - The quote now includes the sentence that prints the five pre-lick means the expected values use.
  - The criterion uses the SEM to tell "rose" from "stayed flat". It now says this is the writer's choice, not the paper's.
- **fig3c-residual-time-course:** the quote now includes the midbrain, striatum and medulla peaks the expected values use. I cut it with "..." where the original sentence has ": ".
- **fig2-1-energy-outside-subspace**
  - The cutoff for the other four regions was 1.5, which has no source. I changed it to 1.1: the paper's "near or below 1" widened by 10%, as the file does for other printed bounds.
  - The paper doesn't settle which units and z-scoring the energy uses. I named this as open, with two readings: the distance-curve rules or the per-bin rules of the fraction curve.

The other claims match the paper: statements, sources, values and tolerances (from Table 1 or the printed SEMs), and the methods (M1 to M10). The paper reports no hypothesis tests, so the file rightly has no statistics entries. Every main finding in the abstract, Results and conclusion has a claim, and every claim comes from this paper alone.

**Still open (recorded under `checks`)**
- Some cutoffs for vague words are the writer's choices and not from the paper:
  - below 0.15 in fig1-1d;
  - at least four times smaller for "much smaller" in fig3-1c;
  - the "seven of ten" and "eight of ten" rules for a partial result in the Table 1 claims.

  They only decide how a near miss is graded, not how anything is computed.
- **fig3-1d-matching-keeps-distance:** the paper doesn't say whether "did not remove" is judged against the control-control distance or the unmatched distance. The current criterion uses control-control, which mostly repeats table1-prelick-residual.
