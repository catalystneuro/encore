Round 3 verification report: the one proposed outcome change, for fig3d-offset-coding-stronger

The attempt record has one `proposed` block, on fig3d-offset-coding-stronger (`grep -c "proposed:"` returns 1). No other claim has a proposed change.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig3d-offset-coding-stronger | partially_reproduced | yes | | See below. |

**Reason for fig3d-offset-coding-stronger**

- **What the Methods say.** The Methods section "Targeted dimensionality reduction" states the centring: "We first centred the responses of each neuron by subtracting its mean response across the two windows of interest before joystick onset and offset". It then regresses without an intercept: r_it(k) = β_it(k) dist(k). The claims file's header says the Methods are the main reading wherever the code or another source differs.

- **The code follows the Methods (cell 41).** Under `centring="windows"`:
  - It subtracts one mean per unit, taken over both windows and computed from the training trials only. The held-out trials are centred by the same mean.
  - The coefficient is `sum k·x / sum k²`, so there is no intercept.
  - The rest also matches the criterion: one axis at the time bin of largest norm, held-out trials projected onto it, R² of a linear fit on distances 1 to 5, and 50 resamples tested with a two-sided rank-sum.

- **The numbers come from the data.** The values quoted in the record's `proposed.reason` match what cell 41 prints:

  | Monkey | Onset R² | Offset R² | Z | p | Denoised p |
  |---|---|---|---|---|---|
  | A | 0.709 | 0.854 | −5.14 | 2.8e-07 | 5.2e-14 |
  | M | 0.787 | 0.684 | +6.85 | 7.3e-12 | 6.6e-11 |

- **Applying the criterion.** It requires offset R² above onset R² with p < 0.0001 "in each monkey … under the readings run", and counts one monkey as partially reproduced.
  - On distances 1 to 5, monkey A meets it under every centring and denoising reading.
  - Monkey M reverses under the main reading, with and without denoising.
  - Only the per-bin centring variant meets it in M. That gives partially_reproduced.
  - The distances 2 to 5 rows are the Methods' control and fall outside the criterion's "distance 1 to 5", so they correctly do not decide the outcome.

- **The change was not made to reach a result.** It moves the outcome from reproduced to the less favourable partially_reproduced, and it rests on the Methods' explicit wording. Both centrings and the window rate difference (A −0.81, M +1.36 spikes/s, cell 41) are shown, and the text in cell 42 says the same.

**Smaller points; none changes the outcome**

1. **The `assumed: true` flag.** It was set because per-bin centring was an assumption. With the Methods' centring as the main reading, centring is no longer assumed. The only open choice left is the 20 ms bin, which the record calls a standard choice. The flag and the deviation text, which still describe per-bin centring as adopted, should be updated if the proposal is accepted.

2. **A variant the criterion lists but the notebook does not run.** The criterion's variant uses the code's windows: −200 to −100 ms and −400 to −300 ms on time-warped bins. Cell 41 runs only the Methods' windows. Because the criterion says "under the readings run", this does not change the outcome, but it is an omission against the claims file.

3. **The time-of-largest-norm step.** Cell 41 finds the bin of largest coefficient norm separately in each window, and the Methods do not say whether it is per window or across both. I'm not raising this as a misreading of the claims file, since its criterion leaves the point open too.
