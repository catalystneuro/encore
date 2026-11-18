# Verifier report, round 3: Gabriel et al. 2025 (doi:10.1016/j.cub.2025.01.010), DANDI:001887 version 0.260902.1724

The attempt record has two proposed changes of outcome, under `proposed` at `gabriel-2025-01.yaml:406` and `:523`. I reviewed only those two. I agree with one and not the other.

| Claim id | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| figs2-innate-behaviors | not_reproduced (from blocked) | Yes | — | See 1 below (cells 56–58). |
| fig3a-decoding-shock-gt-ns | partially_reproduced (from reproduced, assumed) | No | reproduced (assumed C1 N1 and the clock tone windows; the control goes in the notes) | See 2 below (cells 71–74). |

## 1. figs2-innate-behaviors: I agree with not_reproduced

**The numbers come from the data (cell 57).**
- Escape frames are the calcium frames off the platform in the last 2 s of each tone. This is the STAR Methods definition, which the claims file also uses.
- Escape onsets are the first frame of each such bout.
- Escape cells are called with the same whole-session ROC (`pma.roc_calls`) as the other features. Activity is measured with the same `pma.event_area` as fig1p-platform-exit-excited-day2, which is what the criterion specifies.
- The printed table matches the record and cell 58:
  - Day 1, escape-excited cells: p = 0.397 to 0.993 over all 24 runs. On the clock windows it is 0.40 to 0.99, and on the paper's bouts 0.45 to 0.99.
  - The record's example matches: clock, seed 0, 4 s window, 68 and 28 cells, 3.26 against 3.73, p = 0.90.
  - Day 2: shocked mice are higher in every run, but p ≥ 0.067.
  - Escape-suppressed cells: p < 0.05 in 0 of 48 runs, smallest p 0.167.

**The choices were not made to reach the result.** The analysis runs all three windows the criterion names (3, 4 and 5 s), both tone readings and four shuffle seeds. They all agree, so the criterion's methods_underspecified clause does not apply. On day 1 the shocked-minus-NS difference is often negative, so no reasonable choice would push it to p < 0.05.

**The criterion is applied as written.** It says "Reproduced when the jumping, escape-excited and similar-activity parts all hold." The escape-excited part needs shocked mice higher with p < 0.05 on both days, and it fails on day 1 in all 24 runs. The claim therefore fails whatever the untestable jumping part would give. This settles the reservation I raised in round 2.

## 2. fig3a-decoding-shock-gt-ns: I do not agree with partially_reproduced

**The criterion as written is met.** It asks for shocked mice higher with Sidak p < 0.05 in the pre-shock and shock epochs. Under the assumed reading (C1 N1, clock windows), cell 72 shows this in all three cohorts:
- All mice: p = 0.036 and 0.012.
- Without F1 and F2: p = 9.9e-05 and 1.0e-06.
- Two-class cohort: p = 0.0012 and 2.2e-05.

**The control is not part of the criterion, and the paper does not have one.** The shuffled-label control (cells 71 and 73) was added at my request, but the claims file does not include it. The paper's text describes no shuffled-label or chance-level control for the decoders; the only shuffle it mentions is the circular shuffle for the ROC. Using the control to change the outcome replaces the written criterion with a new one. Its result belongs in the notes as a caveat.

**The control answers the concern I raised, and in the authors' favour.** My round-2 worry was that the group difference came from the share of successes. Cell 73 argues against that:
- With shuffled labels the groups do not differ: pre-shock 0.476 against 0.230, p = 0.455.
- A mouse's number of successes does not predict its shuffled-label value: r = 0.16, p = 0.57 for pre-shock, over 16 mice.

**Applied to the shock epoch, the proposal's own test gives mixed results.** Under C1 N1, observed minus shuffled for the shock epoch gives p = 0.054 with all mice, which fails. It gives 0.046 and 0.048 in the other two cohorts. The record's rule is "the outcome is the one all three [cohorts] give", so under the assumed reading the shock part does not hold either. The reason in the record covers this by citing C2 N1 (p = 0.0018 to 0.013). That is a reading the record otherwise declines for this claim. Mixing readings to keep one part is a choice that reaches a result.

**The control is weak.** It uses only 5 permutations per mouse. In 5 of 16 mice (F1, F2, F3, F7, M6) the normalised F1 is 0 in every epoch, both observed and shuffled, so these decoders are degenerate. The proposal's "p ≥ 0.55" for the pre-shock control is 0.547 at its smallest, which is minor.

**What I would put in the notes.** Keep reproduced (assumed). Record that above the shuffled-label values neither the pre-shock difference (p ≥ 0.547 in every cohort and coding) nor, under C1 N1 with all mice, the shock difference (p = 0.054) is significant.

The claims file does not misread the paper on either claim.
