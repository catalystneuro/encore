No outcome changed. One change of outcome is now proposed for the third round: fig3q from partially reproduced to reproduced. The entry was re-run with `python tools/entry.py all`: both notebooks pass (15.1 and 13.3 min) and `check` reports 0 errors.

**New analysis.** I added a second notebook, `decoders_v1_pm_offset.ipynb`, plus a small `session_summary` helper in `tseng.py`. Fitting all 142 decoder sessions would take 48 min on 4 cores, over the 30-minute notebook limit. So the notebook fits two subsets that settle the open points:
- **fig3q (cue gradient):** I fitted every pool session imaged in V1 or PM (41 sessions, 149 V1 and 71 PM decoders). V1 is above PM in all 12 readings, by 0.027 to 0.062, in each of the 6 mice that have both areas, and within each field. The difference is significant in only 2 of the 12 readings, but the criterion only ranks the area means. The other areas, from the 18-session subsample, are at least 0.118 below V1. I recorded `proposed: reproduced` with this reasoning.
- **fig8cd (position-specific decoders):** I decoded the 6 sessions with the 0.76 cue offset that the Figure 8C legend uses (53 decoders, 3 mice). Decoding drops with distance in every area (p < 0.001, every decoder). So the reproduced outcome no longer depends on its assumption, though V1, AM and A each come from a single mouse here.

**Corrected to match the printed outputs:**
- **Cost figures:** the GLM, shattering and decoder costs in the record now quote this run, and the GLM notes give the round-2 run's figures for comparison. The fit time varies between runs: 0.2 s in this run, 0.4 s in round 2.
- **Counts:** sessions with the 0.76 cue offset are now 6 of the 142 pool sessions (8 of the 172 multi-plane files). The single-plane sessions are now 13 in the dandiset and 8 in the selection, replacing "12".
- **Visually guided trials:** "every reading" is now "every all-trial reading", with the correct-only values added.
- **Cue-biased running:** the second-quadrant choice-decoding description now matches the printed values.
- **README and entry.yaml:** runtimes updated and the new notebook added.

**Recorded:** the round-2 verification is in the attempt record, with all 43 claims (the verifier agreed with every outcome), its reasons in its own words, and my responses.

**Not done:**
- The well-fit reading for fig4h still cannot run, because it needs the GLM, which stays blocked as too large. Even the 200-neuron lower bound (21 to 36 min of fitting) leaves no room in a 30-minute notebook, and the GLM's design matrix is not public. The record says this.
- No questions were added to `questions/000579.yaml`, because the verifier reported no misreading of the claims file.

The working tree also has untracked files I did not create: `.bashrc`, `.profile`, `.gitconfig`, `.idea`, `.vscode`, `.mcp.json`, `scripts/` and others. I left them alone, but they should probably be kept out of the commit.
