I've answered every point in the round-1 report. No outcome changed. The verifier agreed with all 20, and the new numbers still support them. `python tools/entry.py all entries/001453-fouke-2025` passes: 0 errors, notebook runs in 145 s. Nothing is committed.

**New outputs the verifier asked for**
- **Static window (code 20).** The paper's code keeps the first 35 s of each code-20 trial and measures from 3 s, which is the same window we use. It also drops fish medians of exactly 0, but no fish median here is exactly 0, so that changes nothing. The remaining explanation for DC static (10.52 against the code's 11.9) is the code's filter on a DC `vel` column, which is not in the files.
- **DC trials above 100 mm/s.** I added a per-trial table. The 11 DC trials pass the speed check whether it uses the stored `dist` (4.8 to 21.9 mm/s) or positions (31.4 to 96.5 mm/s). Their high speed comes from a short motion phase, under 1 s in 9 of them. DC-sub-2 static is the exception: 106.5 mm/s over 14.6 s. With the check from positions, the Tukey test gives the same 3 DC pairs.
- **The paper's own Tukey output** finds the same three DC static pairs significant (adjusted p 0.024 to 0.040, ours 0.030 to 0.049). So for fig1d-dc-no-modulation, the paper's code disagrees with the paper's text, and our result matches the code. I recorded this as a new `code_mismatch` finding.
- **Angular acceleration noise floor.** DC values are higher in the 3 s before the grating moves (205 deg/s²) than during motion (171). Heading from the unwrapped `f0_theta` gives DC higher still (218 to 278, against ZF 61.8 to 77.3). The text now says the DC values may be tracking noise and the reversal is not evidence against the paper.
- **Codes 9 and 11.** I added per-fish turning time courses. DC turn more to the right for code 11 than for code 9 (5.82 deg/s, 10 of 12 fish, p = 0.0093). ZF lean the same way but not significantly (p = 0.141). If fish turn with lateral motion, this favours the protocol file's assignment, under which figs1e would be partially reproduced. That claim stays reproduced, because the claims file fixes the figure code's assignment, and it is now described as fragile.
- **Frame rates.** The slow files are really 33 to 35 Hz, not a timestamp error: their intervals are regular (28.8 to 30.8 ms) and their trials last 34.96 s, matching the 35 s protocol.
- **Per-fish test for DC speed.** Mann-Whitney p = 0.02, now in the notebook and the record.

**Corrections**
- **The "without trial rejection" variant did nothing before.** Rejected trials had no measures, so it repeated the main analysis. The helper now measures every trial and keeps the code's pass/fail flag separately. With the fix, reading (d) gives DC 9.85 and ZF 6.30, and readings (a) to (c) are unchanged.
- **Other text:** I updated the conclusions and summary to match the new numbers. The deviations now say the timing of the DC stimulus labels is unconfirmed (verifier point 8). I added a finding that the DC `dist` series disagrees with the positions.

The round is recorded under `verifications` in `attempts/001453-fouke-2025-01.yaml`, all 20 claims marked as agreed.

**Not done**
- I kept `metadata_insufficient` as the blocker for fig1cef, where the verifier said `methods_underspecified`. The reason is in the response field.
- I did not save the paper text under `paper/`: I didn't download it, and the verifier's copy isn't in the repo.
- Untracked files at the repo root (`.bashrc`, `.idea`, `scripts` and others) were not created by me, and I left them alone.
