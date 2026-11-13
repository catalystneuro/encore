I've worked through each point of the round-2 report and re-run the entry with `python tools/entry.py all entries/dana-2016`. The check gives 0 errors, and the notebook runs in 1.9 min and passes. Nothing is committed.

**Outcomes:** none changed and none proposed: 8 reproduced, 3 not reproduced, 24 blocked. The verifier agreed with all 35, and they are recorded as round 2 under `verifications`.

**`fig4e-jrcamp1a-detection`** (still reproduced, now resting on two assumptions):
- **Keeping `data_20150707_cell1_001.mat`** is now marked as the second assumption. The deviation gives the evidence on both sides: the paper's 10 cells need this recording, but the event counts point the other way (130 and 71 without it, nearer the paper's 135 and 65 than 158 and 83 with it). I removed the cell 44 sentence saying the paper's analysis included it. The `methods_unavailable` finding now says the outcome depends on this choice.
- **The verifier's alignment point:** my main reading places each event at its ephys time stamp; the script places it later, by the first frame time. This is now stated in cell 30, the helper and a deviation. The script's timing is added as a variant (`cai2.script_time`) for the three detection claims. It changes none of their outcomes: the jRCaMP1a rates stay at 63.3% and 80.7%, jRGECO1a 1 AP gives 84.8%, 2 AP 95.2%.
- **Why I didn't propose a change:** a new cell reruns the claim without the recording. The main reading then fails at 1 AP (74.6%). But some readings of the claim still pass both rates: isolation (b) with the script's timing gives 69.4% and 82.8%, and isolation (b) with segment (b) passes in 2 of 36 combinations, though neither is a clean one. Dropping the recording therefore doesn't give a single outcome, so I kept the verified one.

**Sentences corrected:**
- **Cell 13, the notes and the `paper_inconsistency` finding:** RCaMP1h 334 is within 353 ± 35.3. No rule works for R-GECO1 or gives both counts.
- **Fig4d notes:** the 4 s bin gives 296 noise traces and counting the duplicate file gives 258, both within 274 ± 27.4. This replaces "no noise rule tried gives 274".
- **Cell 54 and the kinetics deviation:** comparing the half rise with Chen et al.'s time to peak is now called a choice, not something the criterion directs.
- **README:** "about four minutes" is now "about two minutes".
- **`code_mismatch` finding:** the 60.8% is now printed (script isolation with the 99th percentile) and the finding cites it, with 60.7% under isolation (a).

**Not done:**
- **Fig4df:** I didn't run the script-timing variant; its deviation says so.
- **Questions file:** I added nothing to `questions/dana-2016.yaml`, because the report found no new place where the claims file misreads the paper.
- **Noise rule:** the verifier said treating the script's noise rule as a reading of the claim stretches the criterion. I kept it as the main noise reading, as the claims-file header directs; the outcome is the same without it (5 of 18).
- **Files left alone:** the changes to `tools/build_site.py` and `tools/site_assets/app.css`, and the untracked dotfiles in the checkout, were already there and are not mine.
