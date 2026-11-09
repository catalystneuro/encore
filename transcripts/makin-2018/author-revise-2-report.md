I worked through the verifier's round-2 report. No outcome changed and I proposed no changes, so a third round isn't needed. The two full re-runs passed with 0 check errors, and every printed number matches the previous run, timings aside. The counts are still 9 reproduced, 2 partially reproduced, 7 not reproduced and 13 blocked.

**Text corrections (report section 2):**
- **fig7-kinematic-model-saturates:** the record said KFlatent (+KF) passes "partly" because its filter diverges; it now says "only". A new printout in the second notebook confirms the verifier's numbers. Its slope from f = 1/4 to 1/2 is 4.20, below its late slope of 6.27. It would pass only with an f = 1/8 signal-to-noise ratio below -1.23 dB, while every other decoder is between -0.10 and 0.68 dB there. Without that value the claim fails under both readings. The record notes, the result cell, the notebook summary and the README row now carry this caveat. I kept "reproduced" because the criterion is met as written.
- **First notebook summary:** fig2-gross-failures now says there is no negative R² "at 64 ms" and points to the other configurations. fig4-task-similar now says the dandiset's session is "probably not" one of the paper's.
- **First notebook, cell 29:** "all four runs" is now "all six runs", and the runs are named.
- **Negative R² list (cell 10 of the second notebook and the gross-failures notes):** added the UKF at f = 1/8 for y acceleration. Static KFlatent at f = 1/8 was already in the list.
- **README:** the blocked row now says single-session values are printed for ten of the twelve claims. None are printed for fig4-advantage-grows or fig9-taps.
- **fig2-kflatent-dynamic-little-effect:** the first notebook now prints the last EM gain of the code-kinematics run (4.25e-4). The notes give both ranges: 4.3e-4 to 6.6e-4 over the first notebook's six runs, and 4.3e-4 to 9.4e-4 over every configuration of the second.
- **fig4-vel-acc-every-session:** I withdrew the round-1 reason the verifier showed does not hold, and the notes now say the verifier agreed in round 2.

**Round 2 is recorded** under `verifications` for all 31 claims: whether the verifier agreed, its outcome, its reasons in its own words, and my response to each.

**Not done:**
- **fig2-position-dynamic-gain:** I did not test whether fitting the second Kalman filter on the training outputs inflates the 4.45 dB gain. A test would need a rEFH refitted on part of the training data, which is a different model from the paper's. The notes say it is untested.
- **Small margins (fig2-velocity-boost, fig2-refh-static-vel-acc, kflatent-modest, fig2-sagittal-better):** these could still flip with another session or training run. The margins were already stated, and the dandiset has no other session to test them on.
- **UKF:** it remains a re-implementation of Li's UKF2, whose code is not in the paper's repository, so it can't be checked against the original.

I added nothing to `questions/000129.yaml`, because the report raised no new misreading of the paper. Nothing was committed.
