I made all of the round-2 report's corrections and added the noise control it suggested. **No outcome changed and nothing is proposed for round 3:** the verifier agreed with all 13 outcomes, and nothing I found argues for changing one. The entry was re-run with `python tools/entry.py all`: the check reports 0 errors and the notebook passes (6.5 min). Every number in the conclusions, record, README and question file matches the new outputs.

**Noise claim (the main point)**
- **New control:** `bra.rnn_batch` has a new option, `inh_per_amp`, that does what the verifier suggested. It sets the inhibition to the value a noise-free bump of each run's decoded amplitude would give. This keeps the force that pulls the amplitude back to 1 and removes only the noise's own contribution to the inhibition.
- **Result:** the mean amplitude after 5 s is 1.002, 1.045, 1.003 and 1.005, above the noise-free value (about 1.000) in all four settings. Only N = 64 at noise SD 2 clearly exceeds sampling error (z = 6.2). These values agree, within 1.2 standard errors, with a direct simulation of the reduced two-dimensional equation for the bump.
- **What it shows:** the fall of the amplitude in the full network comes from the noise's extra contribution to the inhibition. That was previously asserted without a control that isolated it.
- **Text corrected:** cell 38, the `rnn_batch` docstring, the record's notes and the `code_mismatch` finding now say that the old fixed-inhibition control removed two things at once.
- **Numbers shifted:** the re-run changed the fixed-inhibition figures slightly, to 1.08, 1.38, 1.01 and 1.08 (within 1.9 standard errors, up from 1.5), with inhibition 0.57 to 0.77 at 1 s. The text and the existing question to the reader now use these.

**Other corrections**
- **Prediction claim (cell 51):** the swapped ratios are fixed. They now read dF/F 1.12 and raw 1.11.
- **ROI masks:** the data check now prints the mask sizes: 3 to 11 pixels, median 7, over 628 ROIs. The old figure of "5 to 9 pixels on the PB midline" was never printed and was wrong. The summary, cell 9, the docstring and the finding are updated.
- **fig3d:** the notebook now prints the lines of the paper's scan script that set each grid cell. The script sets no random seed and runs each cell as a separate process, so the cells are independent samples. The "within sampling error" verdict stands, and the conclusion and notes now say why.
- **Minor fixes:**
  - Cell 11: a 5-frame lag is 0.54 s at 9.18 Hz and 0.64 s at 7.87 Hz.
  - figs2: the README and notes say 160 values, not 161.
  - figs2: the "about 1.2 expected" now says it covers N of 8 and more only.

**Questions for a reader:** I added two to `questions/000289.yaml`, both on places where the verifier says the criterion is tighter than the paper. Neither claim was changed.
- **fig4b:** is reading (b), a sort the hemibrain names cannot provide, really part of the claim?
- **figs2:** does "mostly independent" allow a single exception?

**Record:** round 2 is added under `verifications`, with all 13 results marked as agreeing, the verifier's reasons in its own words, and my responses.

**Not done:** B10 (the retuned performance is biased upward) is left as it was, since the paper's notebook does the same and the verifier accepted that. Nothing was committed.
