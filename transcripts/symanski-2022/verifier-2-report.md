**Verifier report, round 2: 001539-symanski-2022-01**

Counts below come from the claims file and the attempt record. There are 47 claims. The record now gives 19 reproduced, 6 partially reproduced, 12 not reproduced, 3 blocked for missing data and 7 blocked because the methods are underspecified.

### 1. Outcomes and assumptions

**I agree with 43 of the 47 outcomes.** That includes the 4 that changed to not_reproduced at my round-1 request (fig1d, fig2s2d, fig3-choice-selective-fraction, fig7b) and the change of fig5d to partially_reproduced. I disagree with, or only conditionally accept, these four:

- **fig5gh-phase-preference (reproduced) and fig5-rr-more-than-beta (reproduced): I disagree.**
  - Both became reproduced only because the main interneuron rule changed from 7 Hz to 9.5 Hz.
  - The claims file's opening comment names 9.5 Hz (F7/ParsePyrIN.m) as a *variant*. It says the Methods are followed and the code's choices are variants. The Methods' rule is rate over 7 Hz plus spike width under 0.3 ms, and the width is missing from the files.
  - At 7 Hz, fig5gh holds 7 of 8 tests (partial): PFC interneuron beta p = 0.0063 and 0.0070 (cell 102). fig5-rr fails: PFC Rayleigh Z p = 0.091 (cell 105).
  - Neither rate-only rule is the paper's rule, and the two disagree. The outcome therefore rests on the missing width, so these two claims should be blocked (data_missing). They should not be scored on a variant the author picked.
- **fig4d-ccg-lags (blocked, methods_underspecified): I disagree with the stated cause.**
  - The window readings disagree only under the 9.5 Hz variant.
  - At 7 Hz, every window and threshold reading gives not_reproduced. The smallest p is 0.22, so the interneuron pairs are never skewed (cell 90).
  - The rate rule decides this outcome too, so the cause should be data_missing (spike width).
  - Even at 9.5 Hz, the interneuron skew (p = 0.046 and 0.042) comes from pointwise thresholds that keep 127 to 130 of 130 pairs. With the global band, no type is skewed.
- **fig6e-glm-with-interneurons (blocked): conditional.**
  - With the main seed, neither alignment meets the criterion (cell 142). If protocol step 1.5 really blocks a claim that depends on a blocked claim, blocked is correct as a procedure. I cannot see the protocol to check.
  - The record states the disagreement fairly.

**Assumptions (`assumed: true`):**
- Most are stated and reasonable:
  - z-scoring and ripple statistics estimated from 60 windows of 2 s per day;
  - Butterworth filter orders;
  - the linearization of the outbound route;
  - a session entering the GLM with at least one qualifying cell.
- The 9.5 Hz rule is stated in every deviation list. It is not reasonable as the reading that decides outcomes, because it overrides the claims file's choice of Methods before code (see above).
- fig5f-rr-mvl-no-difference is reproduced at 9.5 Hz with p = 0.0502. Its p is under 0.05 in 4 of 10 other bootstrap seeds (cell 120), so the outcome hangs on the seed. The notes say this.

### 2. Statements the printed numbers do not support

- **Cell 53, and the record's fig2de notes:**
  - "rank-sum … smallest p = 0.65": the smallest rank-sum p is 0.249 (reading A, beta coherence CA1-OB; cell 50).
  - "signed-rank … under reading A (smallest p = 0.12)": the smallest is 0.105 (same row).
  - The outcome is unchanged.
- **Cell 75:** "the Methods' reading of the selection (… interneuron above 9.5 Hz …)". 9.5 Hz is the code's variant, not the Methods' rule.
- **Summary (cell 175):** "The GLM's earliest times move by one window between random seeds." They move by two:
  - reading a, CA1 pyramidal: 0.0 to 0.2 s (cell 136);
  - PFC with interneurons, reading b: 0.22 to 0.42 s (cells 140–141).
- **Summary, cell 71 and the record's unit-counts notes:** "the dandiset holds the active units only" overstates the data.
  - 53 units have fewer than 100 spikes in the task epochs (cells 7 and 70).
  - The files hold 915 CA1 units against the paper's 934 active.
  - The record's finding ("close to the paper's active units") is the accurate wording.
- **The record's data_missing finding** says the rate rule "decides the outcome of two claims". It decides three; fig4d is the third (see section 1). The Summary's phrase "moves fig4d-ccg-lags between readings" understates this: the rule changes fig4d's outcome.
- **Cell 137 and the record's fig6e-glm-choice-prediction notes:** "partial on most seeds". Reading b is partial on all 4 other seeds; on seed 621, CA1 is at 0.22 s, outside tolerance (cell 136).
- **Summary table:** only fig5gh and fig5-rr are marked "(assumed)", but the record flags 37 outcomes as assumed. This is a labelling inconsistency, not a numeric error.

I checked every other "Result:" sentence, the README (counts 19/6/12/3/7 match the record) and the record's notes against the outputs, and they agree.

**My round-1 reasons in the record:** they are stated in my words. Some combine my outcome reason with my problem notes, for example B3 in fig4d, B4 in fig5e and B6 in fig6d; that is faithful. The cell numbers in the reasons refer to the round-1 notebook, and the cells have since been renumbered.

### 3. Round-1 points

**Resolved:**
- B3: a global jitter band was added, with the distributions of peak z and lag.
- B4: a split-half control was added, and the notes say it does not support fig5e or fig5s2.
- B5: the label, group and row readings are each tabulated per file; only the label reading puts every unit in CA1 or PFC.
- B6 to B12: each is now stated, shown or rerun.
- All my "could not check" items: the file inventory (no waveforms, thermocouple or air epochs), per-epoch performance, tetrode counts for reading A, and the placeholder description of the `referenced` column.

**Remaining, bearing on a conclusion:**
- **B2, interneuron rule (not resolved; now affects more outcomes).** The 9.5 Hz variant replaced one choice made by the author with another. It now decides fig5gh, fig5-rr-more-than-beta and fig4d. These should be blocked as data_missing, which would give 17 reproduced, 6 partially reproduced, 12 not reproduced, 6 data_missing and 6 methods_underspecified.
- **B1, fig6e-glm-with-interneurons.** The disagreement is recorded. It is acceptable only if protocol step 1.5 says what the record claims.
- **fig5e and fig5s2 (reproduced by the criterion's method).** The record now shows the effect is not supported once selection is controlled for. This is correctly reported, but readers of the README see only "reproduced".

**Misreadings of the paper in the claims file:** none found.
