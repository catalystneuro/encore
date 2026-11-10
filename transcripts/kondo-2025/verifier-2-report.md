**Round-2 verification: Kondo et al. 2025 on DANDI:001425 (attempt kondo-2025-01)**

The claims file has 22 claims and the attempt record has 22 outcomes: 15 reproduced, 1 partially reproduced, 6 blocked. Of the 6 blocked, 2 are data_missing and 4 methods_underspecified. Cell numbers below are 0-based indices in the re-executed notebook. They differ from the numbers in my round-1 report.

### 1. Outcomes and assumptions

I agree with all 22 outcomes.
- **fig3e-cluster-b-similar-rates** is now blocked (methods_underspecified), which was my round-1 verdict. Cell 35: Mann-Whitney p is 0.58 to 0.82 in every case, but the 10% reading fails three of the four times (rel_diff 0.128, 0.161, 0.171).
- **fig5f-forepaw-correlation** stays partially reproduced. Both mean R values are within tolerance under every reading, but the exact session count is 356 against 354 (cell 59).
- **fig6b-movement-order** stays blocked, now for the right reason. The onset rule is shown to be unreliable (cell 64). The grand traces show the jaw moving before the pull in the mean: 3.74 px at −0.3 s against a baseline of 0.43 ± 0.27 (cell 65).
- **methods-no-signal-degradation** stays reproduced, and its subsample is now validated (section 3).

**Assumptions:** no outcome carries `assumed: true`.
- The 100 ms sustained-crossing rule is called an assumption in prose but is not flagged. Nothing rests on it: every onset is −0.5 s with or without it, and the claim is blocked under every rule.
- Mapping trial codes to stimuli in fig4d is an inference. The tactile and visual outcomes do not depend on it alone, because the `ch3:` and `ch:stim_visual` channel readings agree (cells 44–47). The auditory outcome uses code 2, which sits only on `stim_auditory`. That is reasonable.
- The lever-tip keypoint name (`rightbartip`) comes from an external input. It is stated, and R = 0.98 supports it.

### 2. Statements the printed numbers do not fully support

- **Cell 66:** "requiring the crossing to last 100 ms helps for white noise but not for smooth traces". Cell 64 shows it does help for smooth noise: from 0.849 to 0.420 at 2 s.d., and from 0.576 to 0.188 at 3 s.d. It does not fix the rule. The attempt record gets this right ("42% for smooth noise").
- **Cell 9 and the metadata_error finding:** "`dFF_B` carries a lever-pull response that `dFF_V` lacks". This holds in 3 of the 4 sessions. In VG1-GC#116 day 1, dFF_B's contrast is 0.002 against −0.004 (cell 8), so neither series responds. The conclusion that the stacks match their names still rests on the ~3× brightness and the correlations.
- **Cell 50 and the record's fig4d-auditory notes:** "with trunk and limb somatosensory and retrosplenial ROIs on top". Under `ch:stim_auditory` with baseline, the top ROIs are VISpm_l and VISam_l (0.69, cell 44). "Flat" is an interpretation of a map that ranges from 0.17 to 0.83.
- **Record, fig5f-lever-tip notes:** "0.978 to 0.985 … over sessions and over per-mouse means". Cell 57 gives 0.977 to 0.985 over mice. My round-1 reason has the same slip.
- **Record, fig4ab and fig5abc notes:** "The Google Drive folder … holds five tutorial notebooks", and the lab platform "refuses to list the folder". No notebook output shows either check, and cells 41 and 54 name only the GitHub repositories. I cannot verify these statements, and the notebook and the record differ in what they say was searched.
- **Record, training-breaks notes:** the 16-day-break sentence appears twice. This is editorial; the numbers match cell 20.
- **Record, fig3d deviations:** the entry ("holds under the first [reading] and not the second") is a result, not a deviation from the method.

Everything else checks against the printed outputs: the Summary (cell 78), the README, cell 0's count of 22 claims (20 tested, 2 blocked), every other "**Result:**" cell, and every other note and finding, including the per-session counts, rho/p values, ratios and percentages.

**My round-1 reasons in the record:** they are accurate paraphrases. They merge in the relevant problem numbers (1, 2, 3, 4/5, 6, 7, 8, 9). One part of my problem 8 is not attached to any reason: the raw tone TTLs exceeding the trial count by up to 145. The author's response to it does appear in cells 6 and 9.

### 3. Round-1 points

**Resolved:**
1. **Onset rule:** there is now a synthetic test, a sustained-crossing variant and the grand traces, and the conclusion says the rule is not a valid test.
2. **Mislabelled TTL channels:** the `ch3:` readings cover only the 19 sessions where the channel names fit.
4. **Signal degradation:**
   - F_B0 is now taken from 160 frames, within 0.01–0.95% of the all-frame median.
   - Sampling noise is about 2.4% of the across-session variance.
   - The session-15/session-1 ratios match the all-frame values.
   - `processing/ophys` is listed and holds no raw ROI series.
   - Reading (a) gives rho −0.191, p = 0.221.
5. **Swapped excitation wavelengths:** the blue/UV assignment is now tested from the data (with the one-session caveat above).
6. **Asset listing:** assets are now counted by extension. The external repository checks are not verifiable from the notebook (section 2).
7. **The 16-day break:** it is VG1-GC#85's, between task sessions 4 and 5. Without it, days per break are 2.14 ± 0.72.
8. **Data oddities:** the T_pull zeros and the extra tone TTLs are counted and listed.
9. **Lever sampling:** the 0.2 ms (5 kHz) interval is printed.

**Remaining, bearing on a conclusion:**
- **fig4d-auditory-map (problem 3, a claims-file weakness, not corrected):**
  - A random 9-ROI region would meet the criterion with probability 0.61.
  - The code-2 VISa response is larger at the true onsets than at shifted onsets in only 10 of 19 mice.
  - In the clock check, the true onsets give the largest response in only 15 of 27 sessions.
  
  "Reproduced" follows the criterion but carries almost no evidence. A question to a reader is filed.
- **fig6b-movement-order (claims file, reported, not corrected):**
  - The baseline window (−1 to −0.5 s) already contains the movement. The grand displacement is V-shaped across it (for example, jaw 0.54 → 0.05 → 1.46 at −1, −0.7 and −0.5 s), so any rule built on this window fires at −0.5 s.
  - The outcome is blocked either way.
- **fig6b-motor-somatosensory-after-reward (claims file, new):**
  - The criterion does not test that MOs "returned quickly to baseline", only that it is below MOp, SSp-ul and SSp-n.
  - In the reward-aligned window MOs is 0.013–0.014, about half of SSp-n's 0.024–0.027 (cell 68).
  - Reproduced is correct under the criterion as written.
- **fig5f-forepaw-correlation:** the account of 356/357 against 354/355 sessions is plausible but not shown: leaving out VG1-GC#119 days 2 and 4, noted "face video is not available". The outcome is partially reproduced either way.
- **Not affecting any outcome:** the pixel-map readings for fig4d were not run, and the manual annotations on the lab platform remain unchecked because access is restricted.
