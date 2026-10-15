I've done protocol steps 1 to 6 for dandiset 001636, and `entry.py all` and `handover` pass. The verifier package is in `executed/001636-pasquereau-2013/handover/`. The main result: 4 claims reproduced, 3 partially, 3 not reproduced and 18 blocked, 17 of them because my response detection has a far higher false-positive rate than the paper's threshold implies.

**Inputs.** The paper is open access, so I used the full text and its supplementary data sheet (PMC3840326, saved under `paper/`). The supplementary table gives monkey V values separately, which I used as expected values. I pinned 0.260518.1819 because it is the only published version and the paper cites none.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| cell-counts | reproduced |
| baseline-rate | reproduced |
| ptn-faster-than-csn | reproduced |
| emg-m2-larger | reproduced |
| antidromic-latency | partially reproduced (CSN test p = 0.018, threshold 0.0167) |
| emg-duration-longer | partially reproduced |
| emg-m1-weak | partially reproduced |
| kinematics-slower | not reproduced (post-MPTP movements are faster and larger) |
| kinematic-latency-unchanged | not reproduced |
| emg-onset-unchanged | not reproduced |
| monkey-l-perturbations | blocked: data missing |
| false-positive-rate, torque-related-fractions, prevalence-unchanged, ptn-more-responsive, one-direction-half, excitatory-majority, magnitude-unchanged, venus-response-magnitudes, latency-shorter, latency-not-training, fwhm-shorter-ptn, dsi-reduced, venus-dsi, dsi-not-baseline, velocity-matched-magnitude, session-correlations, trial-correlations | blocked: methods underspecified (17) |

The 17 blocks come from one rule fixed in the claims file. My detection's false-positive rate over the 200 ms window is 0.22, and 0.19 on unperturbed trials, against the 0.01 the paper's threshold implies. The analyses still ran. Notably, the latency shortening matches the paper's monkey V means and tests, while response magnitudes fall after MPTP, which the paper did not find.

## 2. What was found about the dandiset

- **No monkey L perturbations.** No Leu file marks a torque perturbation, and the Leu torque command is all NaN before MPTP. Only monkey V can be tested.
- **Analog clock drift.** The angle, torque and EMG are stored on a clock that falls about 5 ms per trial behind the trials table, up to 365 ms within a session. Realigning each trial puts the torque command 4 to 7 ms after every labelled onset.
- **Torque command differs between states.** The pulse is about four times larger in most post-MPTP sessions (183 against 46 units). The movement and EMG differences between states follow the command size; in sessions with matched size, m2 is not larger after MPTP.
- **Wrong angle sign.** The metadata says positive is extension; the data show positive is flexion.
- **Repeated recordings.** Four files repeat a block of another file's recording. In two of them the same unit is stored twice with different projection types.
- **Broken cross-references.** `unit_also_in_session_id` uses wrong prefixes, mostly names files that are not in the dandiset, and otherwise points to a different unit.
- **Smaller description errors.** The dandiset description says MPTP was systemic, both monkeys used the elbow, and Leu was recorded in 1993 (the files say intracarotid, wrist, and some Leu files are from 1992). Monkey L analog is at 100 Hz where the paper says 200 Hz. The torque comes a near-fixed 1.70 s after the center target appears.
- **Monkey V cell counts recoverable.** The monkey V cells with at least 5 perturbations per direction match the paper's counts exactly.

## 3. Where the protocol was unclear, wrong or missing something

1. The paper states a per-comparison threshold (0.01/5), not a measured false-positive rate. I treated the implied 0.01 as the stated rate and defined "far" as a factor of 3. The block then spreads to every dependent claim, including latency results that match the paper. Taken literally, the rule hides those results.
2. The protocol doesn't say how to compute a false-positive rate. My pre-registered pseudo onset may contain real activity, so I showed unperturbed trials as a variant (same answer).
3. "Use the stated spread" is ambiguous for mean ± SD over cells. I used 2·SD/√n where the paper gives n, and 10% otherwise.
4. The protocol says nothing about supplementary material or a dandiset holding one of two subjects. I used the supplementary per-monkey values.
5. Counting each recording once conflicts with matching the paper, whose counts include the two duplicated units. I kept units as stored and dropped the copies in a variant.
6. A difference in the stimulus between conditions is not an error, and the finding kinds don't fit it. I recorded it as `other`, with matched-command variants.
7. For absence claims with many tests (12 for magnitudes), I counted the effect as found if any test had p < 0.05.
8. Step 1.5 asks to record the code repository and commit read, but the attempt schema has no field for it. I put it in the notebook header (turner-lab-to-nwb at e80a192).
9. A previous author run (session limit) had left a draft `stretch.py` and its transcript on the branch. I read the end of the transcript to see why it failed, then replaced the helper. Treat this as possible contamination of the "protocol alone" test.

## 4. Runtime and failures

- The notebook runs in about 90 s from a clean environment, about 67 s of it streaming 447 files.
- Loading with threads first took 591 s because h5py serializes calls within a process. Switching to processes fixed it.
- Nothing failed in the final run, and the executed outputs match my development run number for number.
- `git status` shows dotfiles and `scripts` as untracked; these are sandbox `/dev/null` mounts, not real files.

I have not committed anything.
