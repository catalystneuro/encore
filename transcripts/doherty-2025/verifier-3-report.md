# Round 3 verifier report: 001444-doherty-2025-01

The claims file has 40 claims and the attempt record has 40 outcomes. Two outcomes have a `proposed` change: fig1-network-size and fig2c-control-it23-rate-activated. I agree with both.

| Claim | Current → proposed | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig1-network-size | not_reproduced → **blocked (data_missing)** | Yes | — | See below. |
| fig2c-control-it23-rate-activated | not_reproduced → **partially_reproduced** (resting on R3 and the both-files pairing) | Yes | — | See below. |

## fig1-network-size

**The numbers come from the data.**
- **Stored units (cell 18):** the four files hold 4,480, 3,231, 2,919 and 2,917 M1 units.
- **No silent units are stored (cell 18):** 0 stored M1 units have no spike in any file. So the table holds only cells that fired.
- **Missing gids (cell 18):** 5,593, 6,842, 7,154 and 7,156 of the gids 0 to 10072 have no row in the four files. The record's "5,593 to 7,156" matches.
- **Nothing else lists silent cells (cell 13):** the units table has only `_name`, `segment`, `block`, `spike_times` and `obs_intervals`. No other table or column lists cells.
- **The gids fit 10,073 cells (cell 7):**
  - The lowest input gid is 10073.
  - The population blocks never overlap.
  - The smallest block sizes plus the 24 gids never seen sum to 10,073.
  - Each gid has the same population in all four files.

**The choice is not made to reach the result.** The analysis does not weaken the criterion's count. It shows that the quantity the criterion counts, every M1 cell including silent ones, is not stored in the dataset. That is the definition of blocked (data_missing). The data do not contradict the paper's 10,073, so not_reproduced would mislead a reader. This is the outcome I recommended in round 2.

**Claims-file note (reported, not corrected):** the criterion assumes each file's units table lists every neuron. The reader took this from the dandiset description, not from the paper. That assumption is what makes the claim untestable.

## fig2c-control-it23-rate-activated

**The numbers come from the data.**
- **Values (cell 34):** under R3 the IT2 rates are 1.203 ± 1.649 spikes/s at rest (137 cells) and 6.662 ± 8.858 activated (68 cells). All four are within tolerance.
- **Tests (cell 34):**

| Test | Pairing | p |
|---|---|---|
| Mann-Whitney | unpaired | 3.5e-05 |
| Welch t | unpaired | 3.6e-06 |
| Wilcoxon | 25 cells kept in both files | 0.016 |
| Paired t | 25 cells kept in both files | 0.011 |
| Wilcoxon | 180 cells, union pairing | 0.69 |
| Paired t | 180 cells, union pairing | 0.0013 |

- **The pairing logic is correct.** I checked `compare` in cell 15: "both" pairs the intersection of the R3 masks, and "union" pairs either mask with 0 where a cell is absent.

**The choice is not made to reach the result.**
- The both-files pairing was adopted earlier for pd-it6-rate-unchanged (cell 98), on a reason stated independently: it keeps each paired rate inside the R3 group whose mean is tested.
- It is also applied to fig5c-pd-it23-rate-activated (cell 91). There it gives the worse outcome (Wilcoxon 0.60, paired t 0.21), and that claim stays not_reproduced even though the union pairing would favour it.
- Applying one pairing to all three claims is consistent, whichever way it moves each one.

**The criterion as written still fails.** Two of the four tests are above p < 0.001. The criterion itself only defines reproduced, so partially_reproduced is a grading judgment. It matches how the record grades activated-pt5b-rate-pd-vs-control (cell 109): values within tolerance, and every test finds the increase but not every test meets the paper's bound.

**Caveats:**
- This claim is weaker than activated-pt5b. Two tests miss the bound, not one, and the paired p-values (0.011 to 0.016) come from only 25 cells, against 0.0052 for activated-pt5b.
- The outcome should be marked `assumed: true`, because it rests on R3 and on the both-files pairing. The record's reason says this, but the flag should be set when the change is applied.
- When it is applied, the README row "IT2 rate increase … paired or rank tests above p = 0.001 under every pairing" needs updating, and so does the record's deviation sentence "Both fail the criterion".
