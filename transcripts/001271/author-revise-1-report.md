No outcome changed in this revision. The entry was re-run with `tools/entry.py all`: all three notebooks pass, and the check reports 0 errors. Nothing is committed.

**The main problem with round 1.** The verifier was given the wrong claims file. It got the one for DANDI:001272 instead of ours for 001271. `tools/entry.py handover` copies every claims file for the entry's dandisets by file name, and both are called `10.1016-j.xcrp.2025.102660.yaml`, so one overwrote the other. Because of this, it could not judge 7 of our 20 claims, and it judged the 10 shared ids against criteria worded differently. I did not change the tool. Round 2 will hit the same problem unless someone fixes it. To work around it, each notebook now prints the 001271 criterion beside each claim, and the header's readings at the top. This adds `pyyaml`, so I re-locked the requirements.

**Changes, point by point:**
- **Sustained depolarization (B3):** I added a per-neuron table and figure comparing the highest field with a no-response baseline. The baseline is the same time window after TTX (−0.60%), which matches the 5 sham sessions. The highest field raises dF in all 20 neurons, by 1.15 to 6.01 points. In every neuron that rise is still below both of the claims file's thresholds for "sustained depolarization." The text now says this measure cannot detect plateaus that small, not that the data contradict the paper.
- **The single AP after TTX (B2):** the plot shows it is noise in a one-pixel ROI. Measured against the session's own noise level, no session after TTX has an AP. The verifier called the after-TTX threshold my own choice, but it is written into the 001271 claims file's AP-detection rule, so I kept it. The claim stays blocked as methods_underspecified because the claims file's readings disagree.
- **The "three APs in one beat" session (subject 9_2):** the plot shows it is noise with swings of about 20%. The same neuron's unmodulated session at that voltage shows eight clear APs.
- **Vehicle neurons (B6):** I added a per-neuron table: all 11 fire after the change, and 8 keep APs in every pair. Moving 13_20240801's change point to its largest gap does not change the outcome.
- **fig3c bleaching (B5):** I added a correction using a smoothed reference trace. The noise threshold barely moves (13.28% against 13.73%), and the depolarization part still fails in all 48 readings.
- **fig2c:** the 1-AP threshold now decides, with the reason taken from the paper, and all 8 readings pass. Requiring the 5-AP threshold too is shown as a variant. The outcome stays reproduced and still rests on that assumption.
- **figs1 (B9):** the gap to the next lower voltage tested is now reported.
- **Runtime:** `entry.yaml` now says 6 and 18 minutes for the two longer notebooks.

**Where the verifier disagrees and I kept the outcome:**
- **fig3c:** the verifier says not_reproduced. I kept partially_reproduced because the two firing parts hold, and recorded the disagreement.
- **fig3b:** the verifier gives the reason as data_missing. I kept metadata_insufficient because the checker does not allow data_missing for data held in another dandiset.

**Recording the round.** I recorded round 1 under `verifications` for all 20 claims. For claims the verifier could not judge, I wrote `agrees: false` with no outcome, and the reason explains why.

**Not done:**
- **The O1(b) soma ROI (B4):** no question was added to `questions/001271.yaml`. The verifier did not report a misreading of the paper, and an attempt to add one about the 2-pixel erosion being unsuited to 16 × 16 crops was stopped and not retried.
- **Figures 4 and 6 claims:** these stay blocked as not attempted.
- **The 001272 pattern claims:** still not run.
