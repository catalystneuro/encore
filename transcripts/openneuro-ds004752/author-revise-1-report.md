I've worked through every point in the round-1 report. Six outcomes changed. The final full run of `python tools/entry.py all` passed in 1015 s and printed the same numbers as the run before it. `check` reports 0 errors. Nothing is committed.

**Outcome changes**

| Claim | Before → now | Why |
|---|---|---|
| fig2h-gc-reversal-p1 | reproduced → not_reproduced (assumed) | I added the calibration the verifier asked for: the same GC tests on trials paired so they cannot be coupled (cortical trials shifted by 1 to 10 positions). The per-frequency test reports a theta reversal in 20% to 90% of these pairings, against a nominal 5%. The cluster test, which the figure legends name, reports it in 0% to 10%, so I adopted it. Under it, maintenance is significant under no reading. |
| fig3-gc-reversal-p2-p3 | partially_reproduced → not_reproduced (assumed) | Same calibration and test. Under the cluster test neither participant shows the reversal. |
| fig3no-p4-right-no-gc | not_reproduced → blocked (methods_underspecified) | On uncoupled pairings in Participant 4, the per-frequency test flags 90% to 100% of tests and the cluster test 10% to 40%. Neither can show an absence at the paper's 5% level. |
| fig4f-incorrect-no-reversal | blocked → reproduced (assumed) | Each virtual sensor in the derivative files is an exact linear combination of that file's scalp channels (R² = 1.000000 in all 150 fits). I recovered the filters and applied them to the raw EEG of the 254 incorrect trials. On correct trials the recomputed sources match the deposited ones (median correlation 0.996 to 0.999). With the band mean, p = 0.71, 0.19 and 1.00 across the three hippocampal readings. This assumes the paper used the correct-trial filters for incorrect trials, which it does not say. |
| fig4e-lpfc-no-reversal | reproduced → not_reproduced (assumed, h1) | This follows from fixing the reference hemisphere (below). DLPFC now gives p = 0.010 (exact 0.0009) with h1, 0.045 with h3 and 0.27 with h2. |
| scalp-temporal-laplacian | not_reproduced → reproduced (assumed, h1 and d1) | Also from the reference fix. One of 18 readings now meets the criterion (p = 0.020 with the mastoid reference, 0.29 after the spline Laplacian). The notes say it is weak and that the encoding median is positive. |

I adopted h1 (the deepest contact against a white-matter contact) because the Methods describe that reference and the Methods come before the code.

**Corrections and added outputs**
- **Reference hemisphere (problem 3):** the white-matter reference is now taken in the same hemisphere as the hippocampal contact. Participant 3's right-hippocampus readings now use the right contact AHR3. I documented the fallback for the ECoG reference in sub-10 and sub-12 in the helper's docstring.
- **Response times (problem 9):** pool p2 now also drops artifact-flagged incorrect trials (282 trials, median 1.38 s). fig1c still passes.
- **Spatial test (problem 5):** the fixation cross-spectra in the null are now scaled by 2. The test is still not significant.
- **Outputs the verifier asked for:**
  - the variable list of each derivative file;
  - the filter R² values;
  - sub-11's hippocampal MNI coordinates, which show the electrode named PHL is in the right hemisphere;
  - the significant contacts by name for fig2bc and fig2d (fig2d also gets the count expected by chance, the binomial probability and a corrected count, which is 0);
  - the exact sign-flip p for DLPFC.
- **Participant mapping (problem 4):** matching participants by `eLife_identifier` is now stated as an assumption for table1-heschl.
- **d2 problem (problem 1):** I wrote it into `questions/openneuro-ds004752.yaml` as a question for a reader and did not change the claims.
- **Record:** the attempt record has the round-1 `verifications` block and two new questions for the paper's authors (the GC null, and which filter was used for incorrect trials). I updated two findings, the notebook conclusions and summary, and the README.

**Disagreements I kept**
- **fig2bc-gamma-encoding-p1:** I kept partially_reproduced; the verifier gives not_reproduced. Two of the criterion's three parts hold, and the criterion has no clause for a partial result.
- **table1-left-hemisphere-sources:** I kept the block reason as not_runnable. That category is in the protocol's list, and FieldTrip needs MATLAB, which can't be installed in the locked environment.

**Not done, for time**
- The MNE approximation for table1-left-hemisphere-sources.
- The spatial test for encoding and for readings h2 and h3; each run takes about 4 minutes and the notebook is near its time limit.
- The per-contact grid tests for h2 and h3.
