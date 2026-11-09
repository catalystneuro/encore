I've worked through all of the round-1 report and re-run the entry. `python tools/entry.py all` gives 0 check errors, and the notebook passes in 407 s. Two full runs gave identical numbers. Nothing is committed.

**Outcome changes**
- **fig1g-selectivity-recovery:** reproduced → partially reproduced. I ran all 96 readings. The recovery times are within tolerance in 34 of them, but no reading gives the paper's 55 neurons; the counts run from 66 to 160.
- **ed2e-no-rebound:** partially → not reproduced. The criterion requires fewer neurons excited than suppressed, and the count is 24 excited against 9 suppressed. The criterion has no partial rule.
- **ed7-unilateral-4-spots-bilateral-1-spot:** partially → not reproduced. Across 64 readings, bilateral 1-spot selectivity recovers in 36% to 99% of resamples. No reading meets the whole criterion.
- **ed7e-size-and-roc:** partially → not reproduced. The bilateral ROC is outside tolerance in every reading, and the criterion has no partial rule.
- **ed10e-callosotomy-preparatory-activity:** partially → not reproduced. There are 519 pyramidal neurons against 496 (521 by spike width), and the selective fraction is 14 points below control mice.

**Kept against the verifier (disagreement recorded)**
- **fig2-bilateral-recovery** stays partially reproduced. Six of 64 readings, all with the 10 screening trials drawn in total, have ipsilateral selectivity recovering in at least half the resamples with both times within tolerance. The bilateral rate is 11% above control, which misses the criterion. This rests on few readings.
- **fig6-modular-models-robust** stays partially reproduced. Run to 4 s, every bilateral attractor run settles, at the wrong fixed point in 47% and 55% of runs, so the attractor part holds. The integrator recovers on lick right trials only.

**Fixes and added output**
- **Recovery times:** a time now counts as within tolerance only when at least half the resamples recover. The mean that counts the non-recovering resamples is shown too.
- **Readings:** every M4 screening and preference reading and the claims file's M3 selection now run for fig1g, fig2, ed7 and fig5, with the number of neurons removed at each selection step.
- **ed4:** the RMS windows now start after photoinhibition ends, and the end point is the last 400 ms of the delay. The earlier opposite-direction result goes away (p = 0.27 to 0.74). It stays not reproduced.
- **ed8a:** added a reading with the modes from correct trials only. It stays partially reproduced.
- **ed2b:** added the result without the four sessions where photoinhibition does not lower the rate, and the neuron counts against the legend. It stays reproduced.
- **Other outputs the verifier asked for:**
  - ed9f: the Experiment 2 lick channels, and the test run on the sessions whose traces show licks.
  - ed10e: width-based cell counts for the callosotomy units.
  - fig2: control and ipsilateral selectivity at several time points.
  - fig6: the bilateral attractor run to 4 s.
- **One correction to the verifier:** its item 7 assumed the session count would not change. With M6's "more than 5 trials" rule, 12 sessions remain, not 16. I kept the authors' script rule (at least 5 trials), which gives the paper's 16, and show the 12-session result as a reading. Its control ROC is 0.681, outside tolerance. This is recorded as a deviation and in the code_mismatch finding.
- **Questions file:** `questions/crcns-alm-3.yaml` now has the verifier's three possible misreadings of the claims file:
  - the ed2e significance threshold;
  - whether the paper's Experiment 3 count of 102 means other bilateral 1-spot sessions were pooled (with that pooling, the ed7e bilateral ROC is within tolerance in 4 of 6 readings);
  - Experiment 1 having 6 mice in the paper and 4 in the data.
- **Record:** I added a paper_inconsistency finding (mouse and neuron counts), the round-1 `verifications` block (22 agree, 7 disagree), and updated the notes. The README and runtime (now 7 minutes) are updated.

**Not done**
- ed9f and ed3 stay blocked, as the verifier also gave them. The ed9f claim concerns the Experiment 2 sessions, which have no licks; the other sessions are shown as variants. ed3's 1.3 s and at-the-cue conditions are missing.
- The corrective-feedback integrator, the tamed-chaos network and the modular FORCE network are still not simulated, because the paper gives too few parameters for them.
