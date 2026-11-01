No outcome changed, as round 2 requires. One change is proposed for a third round. The entry was re-run with `python tools/entry.py all entries/001272-semenov-2025`: 0 check errors and all three notebooks pass (277 s, 340 s, 608 s). The numbers I cite match the new outputs. Nothing is committed.

**Outcomes**
- **figs1-near-threshold-delayed-aps:** stays partially reproduced. I agree with the verifier and propose not reproduced, still resting on the same assumptions. The criterion is one test per neuron, and only 1 of 3 neurons passes under the adopted readings, where more than half are needed. It is met in 0 of 24 combinations under O5 (a). The reason is under `proposed` in the record, and the notebook conclusion, summary and README say a change is proposed.
- **All other claims** keep their outcomes, and the verifier agreed with each of them.

**Outputs added**
- **fig3c null test on 001030:** it does not decide between the two ways of reading the AP height (as the dF value or as prominence). With the whole frame, neither reading finds a peak before the onset. After the stimulus, the value reading finds none and prominence finds 0 to 7.
- **c7 at 2.3 V:** the 9 late detections have prominences of 1.9 to 4.4%, below the 4.43% threshold. But the earlier detections in that session range from 1.3 to 19.1% (median 4.0%), so prominence does not set the late ones apart. The notes now say the outcome rests on prominence and no null test confirms it.
- **The two bleaching corrections** subtract the same trace from c7's sessions, so they are one check for c7, not two. The text now says so.
- **Printed checks** now back four claims that had no output:
  - All 65 files of 001272 say "without tetrodotoxin (vehicle control)".
  - All 71 TTX files of 001271 carry the "caused sustained depolarization" wording.
  - No file mentions gluconate: 0 of 454 for 001032, 001033 and 001035, and 0 of 287 for 001271.
  - Dark frames in the strobe recordings: `strobe.py` and the strobe notebook now count them.

**Text corrected where the outputs did not support it**
- **Number mismatches:** the median AP height is now 3.7 to 6.7%, the O5 (b) counts are 13 and 20 of 24 (it said 12), and the figs1-culminates variant is now the one actually printed.
- **"At nearly the rate during it":** replaced with the printed null-test rates in two notebook cells and the record.
- **Unprinted session:** the session 001032 2_1 (11 V), which no output shows, is removed.
- **001034:** only its 80 2-kHz unmodulated files are shown to duplicate 001032, not all 178.
- **Dark strobe frames:** not every file has one. 164 of 175 replicates do, 95 of them only in the first frame. This is now a finding.
- **Round-1 record:** the verifier's threshold outcome is now quoted in full.

**Questions for a reader** (added to `questions/001272.yaml`, claims unchanged)
- fig2-modulated-locks-to-beats: the claim says "no sustained firing", but the criterion does not test it.
- figs2-ttx-blocks-depolarization: the criterion is conditional, so the depolarization part passes on 1 neuron.
- figs1-effects-same-as-fluovolt: the criterion has no outcome for a pattern that fails with no threshold difference.

The round-2 verification is recorded for all 19 claims, with the verifier's reasons and my responses.

**Not done**
- **fig6-sine-less-than-pulse and threshold-depolarization-estimate** are still not attempted. The protocol leaves a change that needs a new analysis (here, ROIs and fits on the 001274 strobe images) to a new attempt.
- **Height reading per claim:** prominence is used for fig3c and the value reading for figs2, where prominence would make the claim fail. The verifier flagged this; I kept it, because prominence was adopted only for a raised late plateau. The record now states that figs2 would fail under prominence.

`tools/build_site.py` was already modified at the start of the run. I did not touch it.
