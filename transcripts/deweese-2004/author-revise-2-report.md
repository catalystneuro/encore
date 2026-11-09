I've answered every point in the round-2 report and re-run the entry. `entry.py all` gives 0 errors, the notebook passes in 126 s, and the numbers are the same from run to run. Nothing is committed.

**Outcomes.** No outcome changed and nothing is under `proposed`. fig4c-psp-culling-can-increase stays partially reproduced but is now marked assumed. The new heights reading gives 18 neurons for it, and the claims-file -20 mV rule without its rise threshold gives 17. Both would give reproduced, against 16 under the main reading. I don't think either reading is better supported than the main one, so I kept the verified outcome. The record now has 14 outcomes marked assumed.

**Statements corrected**
- **Cell 29 and lfp-culling notes:** reading 1b (2.99 mV) and variance over N (2.94 mV) are now stated as outside tolerance. The outcome also rests on detail 1, which the record now says.
- **Cell 44 and fig7b notes:** details 1, 2, 4 and 5 give 1.42 to 1.78 mV, within. Variance over N gives 1.36, just outside.
- **Cell 50 and fig7d:** now names details 1 and 3. 1b gives 1.57 and variance over N 1.50, both below 1.6. 4b gives 1.61, which is within by 0.01, so I disagreed with that one item and the response says so.
- **Anesthesia:** variance over N added (0.93 and 1.77 mV, which would give partially reproduced).
- **fig8:** reading (a, b) is now stated as outside (−0.172) under the window ending 15 ms before onset.
- **Spike rule (cell 14, summary, all deviations):** the third group the verifier found is now described. Of the 187 trials only `spikethresh` removes, 114 cross −20 mV with a rise below 10 mV/ms.
- **mEPSP finding:** the ranges are corrected from cells 77 and 78.

**Analyses added**
- **Heights re-measured after culling:** now a reading in every table. Of the outcomes at their edges, lfp-culling gives 3.07, anesthesia 1.01 / 1.34 / 2.01, fig7d 1.65 and fig7b 1.51, so none moves. fig4c is the only claim it changes. The random culling controls still use heights from the full ensemble.
- **Two more spike rules in every table:**
  - −20 mV at any rise gives a mean variability of 4.43 mV, close to `spikethresh`'s 4.58.
  - `spikethresh` keeping the slow events gives 5.11 mV.
  - So the claims-file rule's 5.35 mV comes from the 10 mV/ms rise threshold, and mostly from the slow depolarizations. The notes now say these may be large PSPs as well as regenerative events.
- **mEPSP:** the conclusion now says the mean depends on each recording's threshold (0.11 to 19 Hz). Without 030401md02h the other four give 0.492 mV and CV 0.385, both outside.
- **Figure panels:** I drew panels like Figures 3A, 3B and 4 and compared them, and Figure 2, with the paper by eye; they match. The figures are labelled with neuron names: Figures 2 and 3A show 022801md01b, the neuron the attempt already identified, and Figure 4 shows 030301md03b.

**Question for a reader.** I added one to `questions/crcns-ac-2.yaml`: the claims file treats the Figure 4 neuron as unnamed, but the figure labels it 030301md03b. In that neuron:
- At 9,188 Hz, q goes from 0.470 to 0.502 mV, against the paper's 0.47 to 0.57.
- At 31 kHz, the Figure 4B legend fits only reading 4b (negative scale factors not removed in PSP culling). The Methods text supports reading 4a, so I kept 4a.

**Not done.** The culling-controls question (whether the 10-trial rule applies again after random culling) is still with a reader, so that outcome stays as the claims file reads it. The round-2 verification block quotes or closely paraphrases the verifier's reasons and gives my response for each claim.
