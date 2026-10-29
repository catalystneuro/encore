**Verifier report, round 2: Makin et al. (2018) on DANDI:000129, version 0.241017.1444**

Counts from the claims file and the attempt record: 31 claims. 18 have an outcome:
- 9 reproduced
- 2 partially reproduced
- 7 not reproduced

The other 13 are blocked: 12 as data_missing and 1 as other (fig4-task-similar).

**1. Outcomes and assumptions**

I agree with every stated outcome. Two need a comment.

- **fig2-sagittal-better (partially_reproduced).** I agree for this run. It gives 23 of 24 pairs; the exception is the static rEFH's velocity at −0.06 dB. My round-1 copy gave 24 of 24, and rEFH seed 2 still gives 24 here. The notes say the outcome depends on the rEFH's training run, which is correct.
- **fig4-vel-acc-every-session (reproduced).** I drop my round-1 disagreement. The criterion defines a per-session grade ("Reproduced in a session when all eight favour the rEFH (+KF)"), and the claims header names this claim as testable on one session. The outcome is labelled "for this session" and the bootstrap is recorded as untested. The author's response gives one reason that does not hold: "the other mean claims tested on one session are graded the same way". Claims whose criterion includes a bootstrap, such as fig2-refh-kf-best, are blocked.

Blocked outcomes:
- The 12 data_missing blocks are correct: each needs a bootstrap or regression across sessions.
- fig4-task-similar as `other` is correct. The claim is `data: elsewhere` and monkey C has no archive identifier.
- fig9-taps: every grade of its criterion needs part (ii), so it stays blocked whatever parts (i) and (iii) give. The record now states this.

Assumptions (`assumed: true`):
- **fig2-velocity-boost** rests on the Methods kinematics: fingertip position, 10 Hz Butterworth filter, last sample of each bin. This is stated, it is the claims file's main reading, and it is reasonable. The code reading reverses the outcome (KFobs ratio 2.05). The finding raises it as a question for the authors.
- **fig8-gaussian-still-beats-ukf** rests on standardized counts, the main reading in the claims file and the Results ("first standardizing the data (separately for each neuron)"). Stated and reasonable. The code's transform reverses the outcome (velocity −0.43 dB against the UKF).

**2. Sentences the printed numbers do not support**

1. **fig7-kinematic-model-saturates** (attempt record notes and README; nb2 cell 25 gives the numbers).
   - The record says: "KFlatent (+KF) passes under b partly because its filter diverges at f = 1/8 (−76.63 dB); the other three pass on their own slopes."
   - "Partly" should be "only". Its slope from 1/4 to 1/2 is (1.12 − 0.07)/0.25 = 4.2 dB per unit f, below its late slope of 6.27 (nb2 cell 24).
   - Under reading b it passes only if its f = 1/8 SNR is below −1.23 dB, which needs (1.12 − x)/0.375 > 6.27. Every other decoder is between −0.10 and 0.68 dB at f = 1/8.
   - So "reproduced" rests on a gross failure of one of the four decoders. The README row says "Reproduced" with no qualifier.
2. **nb1 cell 69 (Summary):** "fig2-gross-failures | reproduced (no negative R2 at all)". There is none at 64 ms (cell 40), but nb2 cell 9 lists 24 negative R2 values in other configurations.
3. **nb1 cell 69 (Summary):** "the dandiset holds none of the paper's monkey I sessions". Cell 6 and the findings say "probably not one of the paper's", since a misdated session cannot be excluded.
4. **nb1 cell 29:** "The claim holds in all four runs." Cell 28 prints six runs. The record correctly says six.
5. **nb2 cell 10 and the fig2-gross-failures notes:** "KFobs and the UKF (f = 1/4, x position)". Cell 9 also shows the UKF negative at f = 1/8 for ay (−0.001), and static KFlatent at f = 1/8 for ay (−0.000). Minor, with no bearing on the outcome.
6. **README:** "Tests across the paper's 49 sessions (12 claims) | Blocked … (single-session values are printed)". No single-session values are printed for fig4-advantage-grows or fig9-taps.
7. **fig2-kflatent-dynamic-little-effect notes:** "the last epoch's gain was 4.3e-4 to 6.6e-4 … in every run". The code-kinematics run's gain is not printed (nb1 cell 17). The response to the same claim gives 4.3e-4 to 9.4e-4, which is the range over all configurations (nb2 cell 6). The two statements are inconsistent.

All other "**Result:" sentences, both Summaries, the README and the record notes match the printed outputs. I checked every figure in:
- nb1 cells 20 to 68
- nb2 cells 13 to 36
- the fig2-refh-kf-best, intro-gain-over-nearest, fig4-position, fig5, fig6, fig7, fig8 and static-refh-position-worse notes

My round-1 reasons are recorded accurately in my own words, with the per-claim parts of problems 3, 5, 9, 10 and 11 merged into the reasons. The `agrees` and `outcome` fields match my round-1 table.

**3. Round-1 points**

Resolved:
- **1, EM threshold.** `makin.py:427` now uses tol = 1e-4. Every EM run hits 100 epochs with a last gain of 4.3e-4 to 9.4e-4, and this is printed.
- **2, single-session values for blocked claims.** Now printed for all ten claims I named.
- **3, fig9-taps.** The block reason is now stated in full; the tapped decoders are still not implemented.
- **5, EM seeds.** Two EM seeds were added. kflatent-modest holds under readings a and b in all three EM runs.
- **7, Wiener filter padding.** The history of the first test bins now comes from the last training bins (`makin.py:319`).
- **9, negative R2 outside 64 ms.** Listed, and a reader is asked how widely the claim applies.
- **11, fig5-derivative-order.** The untested exception clause is now noted.
- **From section C:** training and test R2 of the static rEFH map are printed, as are per-decoder R2 tables for every configuration.

Remaining points that bear on a conclusion:
- **fig7-kinematic-model-saturates (round-1 point 10, now affecting a conclusion).** The outcome holds only because KFlatent (+KF) diverges at f = 1/8. If that value is excluded, the claim fails under both readings. The notes should say "only", and the outcome should carry that caveat.
- **One session with small margins (round-1 point 4).** This is now stated, but these outcomes can still flip with one session or one training run:
  - fig2-velocity-boost: ratio 1.92 against the required 2.
  - fig2-refh-static-vel-acc: velocity margin 0.05 dB.
  - kflatent-modest: margins of 0.07 to 0.10 dB.
  - fig2-sagittal-better: 23 or 24 pairs depending on the rEFH seed.
- **fig2-position-dynamic-gain.** The gain is 4.45 dB against 3 ± 0.5. Whether fitting the second Kalman filter on the training outputs inflates it is stated but not tested.
- **The UKF is a re-implementation of Li's UKF2 (round-1 point 6).** It is the reference decoder in several claims and cannot be checked against the original, whose code is not in the paper's repository.
- **Not checked by me:** the cited rbmish code details, because that code is not in my materials.
