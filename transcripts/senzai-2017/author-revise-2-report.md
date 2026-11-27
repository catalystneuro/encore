No outcome changed. I proposed a different block reason for the two blocked claims, and three more T-maze outcomes are now marked as resting on an assumption. The entry ran from a clean environment in 24 minutes, and `tools/entry.py check` reports 0 errors. Nothing is committed.

**Outcomes**
- **All 31 are as verified.**
- **pv-remap stays reproduced and seed sensitive**, as the verifier now accepts. The notes and the Result cell now say what the criterion leaves out: the claim's own Bonferroni post hoc test (GC against MC) holds at 5, 10 and 15 cells but not at 20 (P = 0.84). I asked a reader whether the criterion should include that test.
- **gc-mc-distance and gc-backpropagation stay blocked as `metadata_insufficient`.** Under `proposed` they change to `methods_underspecified`, because the test the verifier suggested supports their reading: the DS2 profile is smoother in shank-list order than in random orders on 83% of the 261 shanks where it reverses, against 5% by chance, under all five seeds. That includes 71% of the shanks where amplitude falls along the list, so the lists are in depth order on most shanks, though which end is the top is not shown. What actually blocks both claims is that the claims file gives them no criterion. I asked a reader for one. Round 3 reviews the proposed change.
- **tmaze-central-active, tmaze-peak-info and tmaze-splitters are now marked `assumed: true`.** They rest on starting each run at the mouse's last entry into the central arm, because the files do not mark the gate opening. Their deviations now say what was assumed and why.

**Added or corrected**
- **T-maze run variants:** the helper now also builds runs three other ways: starting at the lab's `arm_start`, dropping samples in the arm the mouse did not reach, and placing each side-arm sample on the arm its angle shows. Each variant gives the same outcome for central-active, multiple-fields, peak-info and splitters.
- **Excursions into the other arm:** a new data check finds that 548 of 1,246 runs have some, and 100 of those go more than 10 cm in. They make up 39% of all side-arm samples, because a few runs wander for a long time, but the median run has none.
- **Spike loss at light onset:** it does not reach the +2 to +15 ms window. The +1 ms bin falls to 0.25–0.39 of baseline, but the +2 ms bin is 0.97 for granule cells and 1.00 for narrow-waveform interneurons, which the light does not suppress.
- **Two wrong sentences fixed:**
  - Same-day files: the Summary, finding 11 and the round-1 response wrongly said that in the other pairs the match was no better than with another day. The round-1 response is now marked as corrected.
  - first-stage-labels: the text now says that the stored waveforms of the 17 wide-band files meet the criterion in all three groups.
- **Finding 1 rewritten:** it no longer says the DS2 profile does not settle the depth order. It now also notes that the probe description names 8 sites per shank, while six mice have 10 per shank and YutaMouse33's probe has 10 shanks. Its severity stays `major`.
- **Questions file:** three new questions to a reader in `questions/senzai-2017.yaml`: the pv-remap post hoc test, the missing criteria for the two blocked claims, and the claims file contradicting itself about which files give each unit's shank.
- **Round-2 record:** recorded under `verifications` for all 31 claims, with the verifier's reasons and my responses. No finding is rated `critical`, so the round has no `findings` list. The verifier agreed that `minor` is right for finding 11.

**Not done**
- I did not run the T-maze run variants for inheritance-tmaze. Its record says so, and its outcome was already marked as resting on an assumption.
- In 21 runs the arm the mouse reached differs from the trial's left/right label, and only 9 of those are marked as error runs. I report this in the data check but did not look into it or make it a finding.
