**Round 2 verification: Gao et al. 2018 (doi:10.1038/s41586-018-0633-x), attempt gao-2018-02**

Cell numbers below are 0-based indices in the re-executed notebook.

Counts, taken from the claims file and the attempt record:
- The claims file has 46 claims, and the attempt record has 46 outcomes.
- 24 are blocked, 10 reproduced, 9 partially reproduced and 3 not reproduced.
- The README's groupings agree with this: 5 behavior claims reproduced, and 22 + 2 blocked.

**1. Outcomes and assumptions**

I agree with 45 of the 46 outcomes. I disagree with one:

- **fig3f-alm-selectivity-abolished-by-cn-inhibition:** I would record not_reproduced; the record has partially_reproduced.
  - The criterion's only test is that photo-inhibition selectivity cannot be told from zero. It fails under every reading: [0.19, 0.60] and [0.02, 0.53] in cell 74, and both 5-screening-trial variants.
  - The author's response calls a 73% to 82% drop "present but weaker". That is a judgement about the protocol's categories, and the record states the disagreement fairly.

The six changes made since round 1 now match my round-1 outcomes. They are fig1g-dentate, fig2-preparatory, fig3d, fig3e-increase-decrease, cd-captures-selectivity, and fig3f, which is the one still recorded as a disagreement.

Three outcomes rest on an assumption (`assumed: true`). All three are stated:
- **fig4-fastigial-activation-alm-latency:** the latency is read from 10 ms bins labelled by their start. This is stated, and it is the most lenient label: on a synthetic effect starting at 5 ms it returned 0 ms (my round-1 problem 5). It is acceptable because the outcome is only partial, and the count fails anyway.
- **fig4g-dentate-effect-recovers:** bins are labelled by their centre. This is stated and reasonable. It is the opposite label from fig4, which the record admits. The outcome is partial whatever the label, because the recovery part fails.
- **cd-captures-selectivity:** selectivity is measured on held-out trials. This is stated and reasonable, since E6 projects independent trials. It is the only reading under which the selectivity part passes.

I found no place where the claims file misreads the paper. The fig1i and fig1l early-lick criteria say "per mouse (n = 6)". The Extended Data Fig. 1f and 2i legends ("Lines, individual mice") support a test pooled over mice, which is what was run.

**2. Sentences the printed outputs do not support**

- **Attempt record, fig4g notes and the `methods_unavailable` latency finding:** "by start 3.3 ms, just below 3.3 to 13.3" and "no single choice here matches both reported values".
  - Cell 52 prints 3.30, exactly the bottom of 8.3 ± 5.0. The printed output does not show it falls below.
  - If it is within, the start label matches both the fastigial and the dentate latency, and the finding's claim is wrong.
- **Attempt record, fig4 notes:** "The fraction of tested neurons (0.40 to 0.42) is close to 227 of the paper's unknown denominator." Nothing printed can support this, because the denominator is unknown.
- **Attempt record, fig1g-delay-errors notes, and cell 18:** "light for 0.455 s from delay onset, ending 0.845 s before the go cue". Cell 9 shows 0.500 s in the 2015 sessions and 1.300 s in ANM314746_20151020. 0.455 s holds only for the 2017 sessions.
- **Summary (cell 93):** "The per-neuron photostimulation p-values here equal those in the lab's compile."
  - Only the 400 ms-bin photo-activation p-values were compared (cell 59).
  - The 381 and 704 NaN entries in the lab's file were skipped by `nanmax`.
  - No E4 whole-window or photo-inhibition p-values were compared.
- **Summary (cell 93), and the record's metadata_error finding:** "both deposits place the fastigial fiber on the same side". Only the CRCNS side is printed (cell 3); `compare_deposits` does not print the DANDI location.
- **Smaller details that are stated but not printed:**
  - The attempt record says ANM314757_20151021 is missing "trials 48 to 315" and ANM314746_20151022 is missing "the last 26"; cell 5 prints only the counts.
  - The attempt record says 14 pyramidal units are "at 0.40 to 0.45 ms"; cell 7 prints only a 0.35 to 0.45 ms bin.
- **Cell 35, the attempt record's fig1i/fig1l notes and the README:** "the early-lick part holds". This is true pooled over mice. But cell 34 shows BAYLORCD6 rising from 0.081 to 0.324 (p < 0.0001), and BAYLORCD8 differing under both codes. "Holds" should be qualified as pooled. It does not change the blocked outcome.

Everything else in the Result cells (17 through 92), the Summary table and the README agrees with the printed numbers.

**My round-1 reasons in the attempt record:** they are given faithfully and in my wording, and the "disagreed with six" count is right. Two small faults:
- My "does not affect a conclusion" labels were dropped when problems 7, 9, 10 and 11 were attached to particular claims (fig1g early sample, fig3d, fig2-alm). Those problems now read as bearing on the outcomes.
- The cell numbers in my reasons refer to the round-1 notebook, not this one.

**3. Round-1 points**

Resolved:
- **1 (sessions whose laser traces disagree with their codes, "MISMATCH"):** every analysis of codes 1 to 4 now shows a run without them.
  - ed10d stays significant (p = 0.035).
  - fig4i now depends on the session set, and the record reports this.
  - fig4i (partial) and dentate (partial) are treated consistently.
- **2 (coding-direction variance):** the outcome no longer uses the single-trial variance.
- **3 (fig4e, fewer trials under photo-activation):** with control trials subsampled to the same counts, 0.86 to 0.89 of neurons still lose significance (dentate 0.51 to 0.52).
- **4 (fig4f/g, movement):** the effect persists within each licked direction.
- **5 (latency bin label):** the notes now say the start label gives the earliest possible onset.
- **7 (conservative bootstrap):** trial-level checks were added.
- **8 (early licks):** now tested.
- **10 (spike counts against rates):** counts give the same 856 neurons.
- **11 (spike width):** checked against the labels.
- **Section C items:** the time-series channels are printed (no lick signal), the laser-trace discussion is restored (cell 10), and the session lists are compared with the lab's coding-direction compile.

What remains that bears on a conclusion:
- **6 (unit counts):** the lab's compiled files hold the deposited units (1084 and 682 pyramidal), not the paper's 912 and 454. So the count failures in fig3d, fig3e-increase-decrease and fig4 are judged on a population the paper did not use. This is disclosed and cannot be fixed from the deposits.
- **9 (clock check in the inhibition sessions):** it is now run there (cell 11), but only at 200 ms resolution. That cannot rule out a 10 to 30 ms offset between spikes and trial events, which is the size of fig3d's latency gap.
  - The record's sentence about it is worded correctly ("larger than its 200 ms windows").
  - fig3d's outcome does not depend on it, because the count fails as well.
- **fig4g at the start label:** the 3.30 ms value at the tolerance bound (section 2) needs more decimal places. It would decide whether the latency `methods_unavailable` finding stands.
