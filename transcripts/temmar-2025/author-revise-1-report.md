I made the round-1 revisions, but the full re-run with `python tools/entry.py all` did not finish: it hit the 2-hour command limit. Three of the four notebooks ran: signals, decoding and multiday. The fine-tuning notebook I added had run 52 minutes without finishing when it was stopped, so fig5b-finetune stays blocked (`too_large`). The code in the three executed notebooks matches the source cell for cell, I updated their conclusion cells by hand to the new numbers, and `entry.py check` passes. The workflow's own run will execute them again, because the conclusion text changed.

**Outcomes**
- **figs5-active-inactive-slopes:** changed from partially reproduced to not reproduced, as the verifier said. The criterion has no partial outcome. The inactive slope is −0.536e-3 against an expected +0.54e-3: the same size with the opposite sign.
- **fig5a-long-term-decay:** stays not reproduced under the criterion's starting values. Started from the values printed in the Figure 5A panel, the fits have lower residuals and all three conditions hold under both normalisations. The record now says the outcome rests on the starting values.
- **fig5b-finetune:** still blocked, and no part of it was tested.
- **All other outcomes:** unchanged; the verifier agreed with them.

**Added**
- **fig5a, test-day normalisation:** the models are now also scored with normalisation refit on each test day. fig5a-multiday-short-term holds under both readings, and with test-day normalisation R2 after day 0 is near Figure 5A's.
- **fig4a-lstm-beats-rr:** LSTMs on the 12 sessions with the highest RR R2, including the highest of all 312. The LSTM beats RR on all of them, 32 of 32 sessions in all.
- **fig2a-irregular-shifts:** a baseline rate for the shift rule. It flags 97.4% of days in July to November 2022 and 97.5% of other days, so it does not pick out that period. Also a variant counting the preceding 30 recording days.
- **suppc1-shuffle-baseline:** a count of sessions within tolerance. Under reading (a), RR is within it on 33 of 312 sessions; both decoders are within it on 1 of the 20 LSTM sessions.
- **fig3e-array-tuning:** channel 47 printed from the electrodes table: Medial, bank B, row 5, column 5, as Figure S1 has it.
- **Corrections:** the LSTM fit times, which were 77 s per fit in round 1 and 148 s in this run, so all 312 would take 1.7 to 3.2 hours; the fig4d and fig2d margins; the fig5b estimate.
- **Records:** the round under `verifications` for all 24 claims. `questions/temmar-2025.yaml` now asks a reader five things: the sign of the inactive slope (figs5), Figure 3E against Section 4.2 (fig3e), the impedance rule of Appendix A.2 (dataset-contents), the claims file's "February 2024" (dataset-sessions), and the criterion's starting values for the fit (fig5a-long-term-decay).

**Not done**
- **fig5b-finetune:** I wrote two notebooks, one for the 30 s arm and one for the 120 s and 300 s arms on 2 seed days. I removed both from the entry and the record because they produced no numbers.
- **More LSTMs:** none on all 45 sessions of July to November 2022 or on all 312, and the code's 90/10 split and training without noise for Figure 5A were not run. All were left out for time.
- **More fig5a day-0 sessions:** I kept 12 instead of doubling them, for time.
- **A lost first run:** my first attempt to run the entry in the background was killed when the command returned, which cost about 15 minutes.

Nothing is committed.
