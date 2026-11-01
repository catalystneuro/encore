I've made the round-1 revision. The entry re-ran from a clean environment, and every notebook passed. The check reports 0 errors, and the conclusions match the new numbers. Nothing is committed.

**First, a problem with the review itself.** The verifier was given the wrong claims file: the one for DANDI:001273, not the one for 001272. Both files have the same name, and the handover step in `tools/entry.py handover` copies each claims file under its bare name, so one overwrote the other. Because of that, the verifier judged several claims against 001273's criteria: a 5% depolarization level for the tetrodotoxin claim, and an "after 250 ms" window for the Figure 3C claim. I recorded its reasons in its own words and said in each response where the two files' criteria differ. I did not change `tools/entry.py`. Round 2 will hit the same problem unless the handover is fixed.

**Outcome changes:**
- **figs1-noisier-than-fluovolt:** partially reproduced → not reproduced. The verifier was right: the criterion needs both measures. The Di-8-ANEPPS traces are actually less noisy by the pre-stimulus SD (0.55% against 0.88%).
- **fig4-pooled-time-constants:** blocked → not reproduced. The 001273 claims file says to fit unscaled when the debris ROI is missing, so the claim was testable. I fitted all 22 experiments under all 8 readings. None gives all four time constants within the paper's SEMs. The charging values come close; the discharging ones are higher. 58 charging and 15 discharging fits that ended at a fit bound are left out and counted.

**Outcomes kept despite the verifier's disagreement** (each recorded with the reason):
- **figs1-near-threshold-delayed-aps:** stays partially reproduced (the verifier said blocked). The 100-ms delay reading has a basis in the paper. Only 1 of 3 neurons meets the criterion under the readings I now adopt.
- **figs1-stronger-field-shorter-delay-sustained-firing:** stays reproduced (verifier: partial). The noise concern is answered by the new detector test below, and the result holds with the height measured as prominence.
- **figs1-effects-same-as-fluovolt:** stays partially reproduced (verifier: not reproduced). Neither the criterion's condition for reproduced nor its condition for not reproduced is met.
- **fig3c-sustained-firing-2s:** stays partially reproduced (verifier: not reproduced). Under this claims file's window, prominence removes the noise peaks on the raised late plateau, which is the case the verifier's own synthetic test shows.
- **figs2-ttx-blocks-depolarization:** stays reproduced (verifier: partial). This claims file's criterion is conditional. The notes now say the sustained-depolarization part could be tested in only 1 of 6 neurons.
- **threshold-depolarization-estimate:** stays blocked, because it depends on the blocked fig6 claim.

**Added or corrected:**
- **Detector test:** I counted detections in the windows before the stimulus starts and after it ends, where no AP is expected, in both notebooks. On Di-8-ANEPPS traces, measuring AP height as the raw dF value gives 0.91 false peaks per 100 ms against 2.09 real ones during the stimulus. Measuring it as prominence gives 0.02. So prominence is now the adopted reading for Di-8-ANEPPS, and the value reading is shown beside it.
- **Bleaching:** I added the bleach-corrected variant the verifier asked for. No neuron reaches sustained depolarization under it.
- **Figure 1 variants:** latency split by carrier, a run without the truncated 900-frame sessions, and a prominence variant. None meets the criterion.
- **Strobe fits:** fits stuck at a bound are now flagged. The pole and discharge parts of fig4-orientation-and-poles are run and reported. The claim stays blocked because the cell-shape labels are not in the files.
- **Smaller fixes:** the frame size in the data check is computed from the data, not typed in. The amplitude-scale wording now says the 001271 check (p = 0.29) found no difference, not that the scales are equal. The README, entry.yaml (including runtimes), the notebook summaries and the authors' questions are updated.

**Not done:**
- The Figure 6 claim was again not attempted, though the data are in DANDI:001274. The time went to the strobe fits and the detector tests.
- No new reader questions were added, because the verifier reported no place where the claims file misreads the paper.
