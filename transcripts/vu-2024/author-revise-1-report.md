No outcome changed in this round. The verifier agreed with all 26 recorded outcomes, and I re-ran the entry twice with `python tools/entry.py all entries/001084-vu-2024`. Both runs passed (about 10 minutes each) and gave the same numbers, and every conclusion now matches them. Round 1 is recorded under `verifications` in `attempts/001084-vu-2024-01.yaml`, with the verifier's reasons in its own words and my reply to each under `response`. Nothing is committed.

**Blocked reasons**
- **figs3:** changed to `data_missing`, as the verifier gave. A new data check prints the fiber table columns of all 116 files: none holds a planned target. The paper's code reads the planned targets from calibration files that are in none of the Zenodo archives. The claim is now `data: dandiset` in the claims file, the README and the summary say so, and a new finding records it.
- **figs1, fig3, fig7d, fig7ef:** kept as `other` (not attempted). These data are public on Zenodo, and the protocol does not allow `data_missing` for data deposited elsewhere. The disagreement is recorded.

**Outputs added, as the verifier asked**
- **Mouse effects in the spatial tests (B2):** ranked within each mouse, with a permutation test within mice. The gradients all hold:
  - light amplitude: r = 0.152, p = 0.013
  - light latency: r = −0.223, p = 0.0014
  - tone latency: r = 0.214, p = 0.003
- **figs4eh, baseline (B1):** the paper's code (`sal_stim_bubbles_loco.m`) uses raw DF/F with no baseline, as the criterion does, so the outcome stays partial. With each split's pre-onset mean subtracted, the tone pattern holds in both splits. That is shown as a variant only.
- **figs5 (B8):** the paper's 18 Hz code also uses 9 spline functions, so the helper matches it. A 13-function variant gives ratios of 0.55 for light and 0.70 for tone. The added noise floor (0.0025 at 470 nm) shows the tone ratio compares two values near the noise.
- **Chance level (B7):** the test's chance rate is 0.024 per fiber, far from the paper's p < 1e-6. That figure assumes independent frames: three given consecutive frames fall outside the band at 0.0037, not 1e-6. The protocol would normally block a claim for this gap. I did not, because the procedure is shown to be the paper's: the raw averages are identical and 94.5% of the paper's published significance calls agree. I recorded this as a deviation and a finding.
- **DL18 refit with its 14 tones (B10):** tone r = 0.9977 and significance agreement 0.947; over all fibers, agreement is 94.5%.
- **Opto2 responders (B4, B5):** counting only responses to another fiber's stimulation still gives 20 of 22. As a fraction, 14 of 19 (0.74) equals the paper's 18 of 24 (0.75); the denominators differ because fewer included fibers were stimulated in the files.

**Corrections and other points**
- The data check text said 15 fibers carry the laser artefact in session 230320f; the table shows 13. Fixed.
- figs7a: added deviations for UG21's missing reward events and its tdTomato label.
- B6 (stimulation null pool): no change. It matches the paper's `getNullDist_stim.m`, which the helper's docstring now says.
- B3 (latency counting): no change. The Methods' count decides, as the protocol requires; the code's count is a variant.

**Not done**
- I did not test figs1, fig3 or the two fig7 claims on the Zenodo data. That would need new criteria and analyses; a later attempt could do it.
- I did not try a mixed model as well as the within-mouse permutation test; one test covers the point.
- The paper's text is saved under `paper/`, which git ignores.
