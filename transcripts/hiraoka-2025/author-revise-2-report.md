No outcome changed and none is proposed. The verifier agreed with all 14 outcomes in round 2. I re-ran the whole entry with `python tools/entry.py all entries/hiraoka-2025`: all four notebooks passed, the checks report 0 errors, and the numbers I spot-checked match the previous run.

**Corrected or added, point by point:**
- **Finding 6:** the numbers were wrong. It now says 0.23 to 0.45 of the 562 pyramidal units (not 0.08), and gives the Achilles-10252013 figures on their own (0.08 to 0.34 of 120 pyramidal units, 0.76 to 0.88 of 17 inhibitory). The same error is fixed in the existing question in `questions/hiraoka-2025.yaml`.
- **Grid finding:** "41 points" is replaced. The grid has 40 steps of 0.0514, the upper end is dropped because it has fewer than 100 bursts, and 40 points are used, from 55.2 to 5581.5 ms. The summary in the main notebook now says the same.
- **Burst count at 6300 ms:** the verifier asked for this output. Cell 15 of the main notebook now prints it: 99 bursts at both 6282.75 and 6300 ms, so the summary sentence is now backed by an output.
- **Summary table:** the KS fractions are now split by set: 0.233 to 0.454 over the pyramidal units of all sessions, 0.083 to 0.342 in Achilles-10252013.
- **Run time:** `other_neurons.ipynb` takes about 50 minutes, not 45. The README, its own header and `entry.yaml` now say so.
- **fig2-neuron-merging-collapse:** the verifier's caveat is now in the notes and in the result cell. The margin is small (0.538 with the exponent unbounded, 0.490 capped, against a band of 0.5). A literal reading of the claims file's "package default" would use the capped fit and give reproduced. The notes say why the unbounded exponent is kept. I proposed no change because the verifier agrees with the outcome and calls the assumption reasonable.
- **fig4-model-heavy-tails and fig4-model-iet-shapes:** the verifier asked why these are "partially reproduced" when the criteria define no partial outcome. The notes and result cells now explain it. For heavy tails, the criterion holds for 2 of its 3 series. For the inter-event-time shapes, 1 of the 3 expected values is within tolerance. fig2-neuron-beta-stable is different: no reading meets its single condition, so it is not reproduced.
- **New question for a reader:** the model-decremental-equivalent criterion rejects two runs of the same algorithm, so it cannot show equivalence. This is now a question in `questions/hiraoka-2025.yaml`; the claim is not changed. The outcome does not depend on this point, because the literal set-up also fails the calibrated test.
- **Finding 1 (unsorted spike trains):** severity lowered from major to minor, as the verifier rated it. The fault shows in the values (negative gaps between spikes) and only needs sorting.
- **Round 2 record:** added under `verifications`, with the verifier's reasons, my response to each claim, and its view on finding 1 under `findings`.

**Not done:**
- I did not count the earthquakes, because the earthquake catalogue has no pinned version. The disagreement was already recorded and is kept.
- Which circles are filled in Figures 2 and 4 is still open, because there is no PDF of the figures.

Nothing is committed.
