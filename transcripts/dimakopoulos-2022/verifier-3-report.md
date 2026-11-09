# Round 3 verifier report: Dimakopoulos et al. 2022 (doi:10.7554/elife.78677), OpenNeuro ds004752 v1.0.1

The attempt record proposes one change of outcome, on `fig3no-p4-right-no-gc`. No other claim has a `proposed` entry. I agree with it.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig3no-p4-right-no-gc | not reproduced (from blocked: methods_underspecified) | Yes | — | The criterion's own test was run and its condition fails as written. The claim needs no contact to be significant, and in cell 57 the per-frequency direction-swap test flags 24 of 24, 20 of 24 and 24 of 24 contact-and-period tests under h1, h2 and h3. Its cluster reading (c2) flags 16, 14 and 22 of 24. The round-2 objection was that these tests also flag shifted, uncoupled trial pairs too often. The legends' scrambled-trial cluster test (cell 47, results in cell 57) answers that objection. |

## How I checked it

**Calibration.** I checked the calibration figures in cell 57 against the printed output.
- On shifted pairs of Participant 4 (h1, 4 contacts, 3 shifts, "shuffle" rows), the scrambled-trial cluster test flags a theta cluster in 0.0 of tests in both periods.
- It flags any cluster in [4 20] Hz in 0.17 of encoding tests and 0.00 of maintenance tests.

**Real pairing.** Under h1 the scrambled-trial cluster test finds a cluster at 8 of 12 contacts in encoding and 10 of 12 in maintenance. The calibrated null would give about 2 of 12 and 0 of 12. Every contact has a cluster in at least one period under each of h1, h2 and h3 (`{'h1': 12, 'h2': 12, 'h3': 12}`). Encoding theta clusters appear at 7, 12 and 12 of 12 contacts. These match the numbers in the proposed reason.

**c2 against the shifted baseline.** The comparison quoted in the reason matches the output (CAL_RATE for sub-13 against the real pairing): 58% against 40%, 75% against 10%, 100% against 30%, and 17% against 30%.

**Choice of test.** The scrambled-trial null is the test named in the Figure 2h and Figure 3 legends (paper lines 46–47). I asked for it in round 2, before it was run, so it was not chosen to reach this result. In `wmflow.significant_bands` it is one-sided by period, which makes a finding of GC harder, not easier.

## Limits and notes
- **Coarse calibration.** The calibration covers h1 only, 12 tests per period. The h1 result is enough on its own: 10 of 12 contacts in maintenance against a calibrated rate of 0%.
- **The claims file and the paper (reported, not corrected).**
  - The claim and the Figure 3k legend say "right parietal", but Participant 4's 12 ECoG contacts include STG and precentral as well as postcentral and IPL (cell 57). The analysis tests all 12. Every contact is flagged, so restricting to the parietal ones would not change the outcome.
  - The criterion names the Methods' direction-swap test, while the Figure 3 legend names a scrambled-trial cluster test. Both give the same outcome here.
