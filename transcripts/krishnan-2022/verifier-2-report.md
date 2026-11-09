**Verifier report, round 2: Krishnan et al. 2022 on DANDI:000462 (0.230416.2132)**

The claims file has 41 claims, and the attempt record has 41 outcomes covering the same IDs: 9 reproduced, 8 partially reproduced, 14 not reproduced and 10 blocked. Cell numbers below refer to the re-executed notebook.

### 1. Outcomes and assumptions

I agree with all 41 stated outcomes. Each one follows the claims-file criterion from the printed outputs. Notes on the ones that changed or are borderline:

- **lick-persistence-ur, fig3d, supp16, fig4h** (now not reproduced): agree. In each, a required part fails: the mean RE high laps, the per-mouse conditions, the six speed means, or the saline absence (failing under both pairings).
- **fig2c, fig2d** (partially reproduced, S2 only): agree. S1 cannot be run, and the record says so.
- **engaged-lap-counts** (not reproduced): agree. No reading puts all three counts in tolerance, and that includes the code-ratio variant (under L1 RE high is 66; under L3 engaged is 140).
- **supp6b, disengaged-laps-uniform** (reproduced, now on a valid split): agree under the criterion.
  - supp6b: engaged means rest on 1 to 5 laps in five mice under L1 (cell 44).
  - disengaged-laps-uniform: the halves differ by 0.16 at n = 10 (p = 0.094), so this "absence" has little power.
- **fig2a** (now not reproduced): agree. It holds in 0 of 2 mice. The 2 of 4 under the L1c variant would also fall short of 2/3.
- **fig1d**: agree. The scaling of "9 of 12" to ceil(0.75 × 10) = 8 is now stated and reasonable.
- **fig4m**: agree under the criterion. The DCZ change is +2.1, so the over-representation does not fall; it only rises less than after saline. This rests on the claims file testing DCZ only, which goes to a reader.

Assumptions: every non-blocked outcome except session-lap-counts carries `assumed: true` with stated deviations, and the assumptions are reasonable.
- The traversal approach ratio is a principled reading of the Methods.
- The claims file makes the Methods ratio the main reading and the code ratio a variant, as it is here.
- The pre-reward zone start, the ref. 75 dF/F rules and the DREADD offset are all stated.

Deviation lists are incomplete (none of this changes an outcome):
- The reward-zone assumption is missing from fig1d, fig1g and every Fig. 2–4 outcome that uses RE low.
- The volts-to-cm assumption is missing from the place-field outcomes.
- The sub-014 realignment is listed only for fig4f, though supp16, supp18, fig4h and fig4m also use the CNO sessions.

### 2. Sentences the outputs do not support

**Bear on a reader's picture, but do not change an outcome:**
- **README, and the record's fig3b-width-intensity deviation:** "about twice as wide as the paper's". The outputs give 70.1 / 65.6 / 73.1 cm against 53.3 / 60.6 / 54.1 cm (cell 61), and 75–81 cm against 46–55 cm (cell 69). That is 1.1 to 1.7 times, not twice. What roughly doubles is the candidate width (31–35 cm) under the Methods width rule.
- **Cell 76, and the record's reward-zone-field-turnover notes:** "Every count is outside tolerance under every reading". Two counts are inside (cell 75):
  - new RR fields at 0–50 cm: 29 (L1) and 31 (L2), against 31 ± 3.1;
  - new RR fields at 100–150 cm: 17, against 18 ± 1.8.

  The outcome stands because the other counts fail.
- **Record finding (methods_unavailable):** "candidate regions it cuts (31 to 41 cm) are close to the paper's widths". The paper's widths are 53–61 cm. The printed candidate widths are 31.4 to 43.2 cm (cell 61); the Summary's "31 to 41" has the same problem.

**Minor:**
- **Record turnover notes:** "paper 77, 83, 62 and 74, 26 to 28%". 62 of 296 is 21%.
- **Cell 82 and the record's fig2a notes:** "RR probabilities are … 0.02 to 0.30". NR23 gives 0.31 under L2 and 0.33 under L3 (cell 81).
- **Cell 96:** "exceeds half the DCZ drop (0.136)". 0.136 is the whole DCZ drop; half is 0.068, as the record correctly says.
- **Cell 6:** "The paper's 7.34 s … is shorter than either". That holds for the means only; running time per mouse goes down to 5.98 s (cell 5).
- **Shown in no output:**
  - Cell 15 and the deviations: "changed no lick stop". The lick stops under the old zone are not printed.
  - Record findings: "dF/F computed without removing [the offset] is about ten times too small", and the GFP indicator, shared session_start_time, P12W age and DREADD session-description statements.

Every other "**Result:**" sentence, the Summary, the rest of the README (including its 41-claim table) and the record notes match the printed numbers.

**My round-1 reasons in the record:** they are stated faithfully and in my own words, and the agreement flags are right (32 of 41 agreed). One snag: they cite round-1 cell numbers (9, 11, 15 …), which now point to different cells.

### 3. Round-1 points

**Resolved:**
1. The approach ratio is now taken over the traversal; the synthetic lap returns 1.601 against a true 1.600 (cell 38).
2. NaN laps are now neither engaged nor disengaged. The main split has no negative thresholds, and every engagement-dependent analysis was rerun.
3. The reward zone now starts at the first lick before the reward. It moved 0.3 to 3.9 cm, so consumption licks were not setting it, and lick-persistence fails under the code zone too.
5. S1 is now stated as missing for fig2c/fig2d.
6. The fig1d scaling is now printed.
7. The first-UR-lap variant was added.
8. The pooled-percentile saline split was added.
9. Medians of the session-field out/in were added.
10. Passed to the questions file, which I cannot see.

From my round-1 "could not check" list, the pupil, tdTomato and full-file-content questions are settled (cell 5).

**Partly resolved:**
4. The clock is checked: 46–49 frames from reward to teleport, 4.11 laps/min. Lap time does not depend on the volts-to-cm scale. Why lap times are about 1.65 times the paper's is still unknown.

**Remaining points that bear on conclusions:**
- **The main engagement split does not match the paper's engagement numbers.** It finds 46% of RE low laps engaged (paper 70%) and an R ratio of 2.21 (paper 1.3). That leaves 2 Fig. 2–3 mice, against the paper's 3.
  - Every Fig. 2–3 outcome rests on those 2 mice, with 95% intervals that mean nothing at n = 2.
  - Some outcomes move under the code-ratio variant: fig3b-reliability (R and RR fall outside), fig3b-out-in (R and RR come inside) and fig2a.
  - The assumption is stated and the claims file requires the Methods reading, so no outcome changes. But these outcomes are weak evidence either way.
- **Lap time and speed (supp5, supp16, supp18):** the cause remains open, as above.
- **dF/F, transient and field rules:** widths of 70–90 cm drive fig3b-width and supp11, and probably the out/in and fate numbers. This remains open; the question to the authors is filed.
- **NR6, a new and minor point:** the paper's code keeps only the first 24 of NR6's 43 R laps. In cell 81, NR6's R-cluster probability already drops at R lap 40. Whether fig2a or NR6's Fig. 2–3 values change under that cut is untested.
