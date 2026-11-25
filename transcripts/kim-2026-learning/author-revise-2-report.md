I've worked through every point in the round-2 report. The entry re-ran cleanly (`tools/entry.py all`: 0 errors, 14.9 min), and every conclusion now matches the new numbers. Nothing is committed.

**Outcomes**
- **fig4ij-pyramidal-drive:** the verifier was right that the stored cell-type label is a weak assumption. I now use the criterion's rule (trough-to-peak at 0.45 ms, recomputed from each unit's mean waveform) for every claim, with the stored label as a variant. Under that rule the pyramidal latency at 6 uA gives p = 0.0587, so the claim is partially reproduced. Round 2 can't change an outcome, so the field stays `reproduced` and `partially_reproduced` is written under `proposed`, for round 3 to review.
- **figs3-modulation-all-cells:** the field stays `partially_reproduced`. The notes, notebook, summary and README had wrongly said reproduced; they now match. The main test keeps the criterion's 4 to 6 uA. I added the reading the verifier suggested (nearest of 4, 5 and 6 uA), and modulation rises there too (p = 2.91e-05 and 0.000139). `assumed` is removed.
- **figs9-coupling-controls:** I ran part (C) with each control trial taken as 10 bursts. There are then 22 pulse-locked and 40 non-pulse-locked values, with no difference (p_FDR 0.924 and 0.355), so the claim would be reproduced under that reading. The outcome stays partial under the 3 bursts the stimulation tables list, now marked `assumed: true`.
- **fig4h-unit-counts:** `assumed` is removed, since it fails under every variant. The measured counts now use the criterion's cell-type rule (724/275 recorded, 402/186 modulated). The outcome is unchanged.
- No other outcome changed.

**Corrections and added outputs**
- **Imaging check:** the notebook now prints 53 to 1019 planar ROIs per session. It also shows the files hold no images at all: `reference_images` and `acquisition` are empty in all 45 files. The fig3 notes, the blocked-claims cell and finding 2 now say this.
- **fig2b and finding 1:** the sentence on catch trials is corrected to give where the -1 samples actually fall.
- **Wheel and finding 15:** a printed count replaces "every block": hits beat misses in 51 of 54 sessions, and the 3 exceptions are ICMS83's.
- **figs4b contact mapping:** "the mapping holds" is removed. I added a test of whether the stimulation channels are numbered the same as the electrodes, but it can't settle it: responses don't fall off with distance under any assignment. The notes now say the mapping rests only on the files' description. A slope that is zero up to rounding now gives no velocity.
- **Text fixes:**
  - fig6d now says the seeds give the same onsets but different clusters.
  - The summary's train-onset sentence is corrected (ICMS83's trains start at 0 ms, the maximum elsewhere is 37.4 ms).
  - The README says only four controls have recordings and gives the run time as about 15 minutes.
- **Record:** round 2 is added under `verifications`, with the verifier's reasons in its own words and my responses.

**What I did not do**
- **Finding 5:** the verifier would raise it to `critical`. I recorded that under the round's `findings` but kept it at `major`, and wrote why under `response`:
  - The data can't tell whether the tables leave out stimulation that was given or another stimulus followed. The protocol caps such a finding at `major`.
  - The verifier said the trial tables agree with the 3 bursts in all but one session. In fact, in a second session (ICMS54 2022-05-20) the trial table itself shows the longer stimulation. I added this to the finding.
- **figs4b:** I proposed no change to its outcome. Nothing in the data contradicts the files' description of the channels.
- **Questions file:** I added nothing, because the verifier found no place where the claims file misreads the paper.
- **Round-1 point 2:** the cause of the excess pulse-locked share (about 80% against about 63%) is still not found. The notes still call it unknown.
- **Unrelated change:** `tools/intake.py` was already modified before this run, and I left it alone.
