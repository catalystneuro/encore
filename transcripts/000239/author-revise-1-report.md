No outcomes changed. The verifier agreed with all 39 (20 reproduced, 5 partially reproduced, 3 not reproduced, 11 blocked), and nothing I added gives a reason to change any of them. The final run of `python tools/entry.py all entries/000239-xu-2022` passed with 0 check errors. It took 1274 s, which is about 21 minutes, against 8 before; most of the extra time is the seed variants. Under 30 minutes, the CI limit, but over the protocol's ten-minute aim.

**Outputs added for what the verifier asked:**
- **Unit counts:** I added the single/multi split per session, two other contamination estimates and a test on synthetic units. The other estimates give 341 and 478 multi-units; only a 20% threshold (295) fits the paper's 303. The synthetic test reads high near the 15% threshold (0.163 for a true 0.15). The outcome stays partially reproduced.
- **Seed sensitivity:** I repeated the Figure 3 fits with three more seeds.
  - ed5e stays at 0.453 to 0.455.
  - In ed5f, L' and theta give 0.302 to 0.320 and are the only pair at or above 0.3 under every seed.
  - The units-per-session SD involves no seed at all.
- **Trial selection:** I compared the greedy search with an exhaustive search and a swap search. The greedy search is at most 8.4% off the best; the selected trial count does not depend on the search.
- **ed2 trial counts:** I applied the paper's own trial exclusions plus the initiation-under-1 s rule to the 47-session variant. This gives 8058 and 2894 trials, both within tolerance, though with 8 mice where the paper has 9. I built that chain after seeing the results, so it is recorded as a variant and the outcome stays not reproduced.
- **ed1l-proficiency:** I added each mouse's first file date and contents. Every first file already holds only standard sequences, and in 3 of 15 mice initiation is under 1 s from the start, so early training may be missing. MX200101 has no final value because its last 500 trials contain no standard trials.
- **ed6b:** I added the distribution of the lick counts and a bout threshold taken from video licks. 5 is the most common count, but the median is still 6 (and 4 for touches).
- **Metadata of all 101 opto and control files:**
  - The session description is cut short in the files themselves, not just in the archive.
  - There is no optogenetics, notes or stimulus metadata.
  - The `opto` column holds 0, 1, 2 or NaN, with no description.
  - The force series are in volts, with a conversion of 1 and an offset of 0.
- **Checks on the control claims without labels:**
  - **Earplug:** the paper's test finds an effect under 4 of the 32 ways the labels could be assigned. One assignment is suggested by both the slower initiation and the session order; under it there is no effect (p = 0.36).
  - **Air flow:** 1 of the 15 possible assignments gives p < 0.05.
  - **Numbing:** in all 5 mice the earlier session has more missed licks.
  - All three stay blocked, since these checks rest on guessed or enumerated labels.
- **Smaller additions:**
  - ed7f with one value per mouse: still significant, p 0.012 to 0.024.
  - ed4l: S1BF has a higher initiation fraction than ALM (30.9% against 25.9%), against the claim's "the other regions". The windows have unequal lengths.
  - fig3f: the two trial types differ in behaviour after the trigger, which decoding in S1TJ and S1BF may reflect.
  - ed1l-learning-curves: 14 of 14 mice improve without MX181003.
- **Text and record:** I added two deviations (the PCA fitted on all trials, and random folds leaking autocorrelation within trials), updated the runtime in the header, README and `entry.yaml`, and added two findings: the truncated session description, and the undocumented opto columns and series. The round is recorded under `verifications` with the verifier's reasons and my responses.

**Not done:**
- The label-free NNMF consistency measure for ed4j. It is not the paper's measure, so it could not decide the claim, and it would add a bootstrap over all neurons to an already long run.
- The Figure 3b values could only be read from the figure image, so the verifier's point on them stands.

I saved the paper text under `paper/`. Nothing was committed.
