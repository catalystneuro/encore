I addressed all 13 points in the round-1 report. The entry re-ran cleanly (`python tools/entry.py all`, 14.4 min), every conclusion matches the new numbers, and `check` reports 0 errors. Nothing is committed.

**Outcome changes**
- **fig5a-trigger-duration-unchanged**: not reproduced → partially reproduced, which is what the verifier gave. The claim holds for OFC (p = 0.61) but not dmPFC (p = 0.019). The verifier also wanted the trials with no Eyes fixation in progress at the trial time examined (29%). They are spread evenly over areas and trial types (27.3% to 30.1%). Counting the 609 trials whose Eyes fixation starts within 20 ms after the trial leaves dmPFC at p = 0.020.
- **fig5cd-saccade-counts-unchanged**: blocked → partially reproduced. `not_runnable` is in fact an allowed block reason, but the verifier was right that the detector's code is public. I ported its MATLAB code (pinned commit) to Python in `microstim.py` and called it the way the paper's own repository does. Under the claims file's definition of a microsaccade, OFC trials have fewer macrosaccades after stimulation (p = 0.044; the paper has 0.055); the other three tests hold. Under the paper's code's labelling, none of the four fails.
- **fig5e-h-saccade-kinematics-unchanged**: blocked → reproduced. None of the 14 OFC and dmPFC tests gives p < 0.05; under the paper's code's labelling, 3 of 14 do.

**Two things about the saccade results**
- On these data the detected events run long (median 147 ms, 95th percentile 1,062 ms). In the run I checked, gaze speed inside fixations is above the detector's 5 deg/s cut-off about 95% of the time, so many detected saccades span several fixations.
- In 202 of the 1,179 social runs the MATLAB code's merging step would stop with an error. The port merges overlapping saccades into one there instead.

Both are recorded as findings.

**Added or corrected**
- **Reader question:** the verifier's point that the claims file may misread the Eyes-versus-RDM comparison (day totals over twice as many social runs as control runs) is now in `questions/000959.yaml`. The claim is unchanged and keeps its not reproduced outcome.
- **Causal-decomposition cost:** I re-timed it with the settings of the decomposition code itself (1,000 ensembles, 10 fixed sifts). That code has no default ensemble size and its example uses 1,000, so both readings cost the same. Every subset is still far over the one-hour notebook limit:

| Subset | CPU hours | Hours on 4 processes | Floor for a compiled version |
|---|---|---|---|
| All social trials (figs4a, figs4b) | about 1,590 | about 790 | about 104 CPU h |
| First 90 stimulations, 25 OFC days (smallest slope-claim subset) | about 183 | about 92 | about 12 CPU h |

  The six claims stay blocked as `too_large`.
- **Eyes-versus-Mouth bootstrap:** now also run with the code's M1-only fixations. Contralateral p is 0.049 over all days and 0.006 for monkey T, but both hemifields combined gives 0.050 and 0.036, so it still does not match the paper's pattern. The outcome stays not reproduced.
- **Outputs the verifier asked for:**
  - one file's groups, which contain no saccade or processing tables;
  - the range of all trial and event times (13.8 to 9,955 s), which confirms the time offset used to pair trials with fixations is safe;
  - mutual-table counts: `mutual_face` excludes the Mouth while `m1_neface` includes it, so the non-eye Face count now adds `mutual_mouth` (corrected p is now 1.1e-07 to 3.1e-05, outcome unchanged);
  - the control-run listing for monkey L's 8-run days: runs 1 to 8, all full length, nothing marks any as extra.
- **Density map:** fixed the reversed x-axis label. The ROI squares are now those inside the ROI of every run of the day. The three recalibrated days are dmPFC and ACCg days, so the OFC result is unaffected.
- **Attempt record:** the round is recorded under `verifications` (35 of 36 claims agreed). I added `inputs` (detector code, the paper's code, the pixel-to-degree function, the decomposition code) and two findings. The README and `entry.yaml` are updated.

**Not done**
- I did not switch the signed-rank test to MATLAB's normal approximation. The verifier's own check showed no p-value crossing 0.05.
- No change was needed for the points reported as not affecting a conclusion: the inter-looking-interval threshold, the combined fixation-count test, the 5-day Mouth test and the tie rule. Each was already stated in the notes.
