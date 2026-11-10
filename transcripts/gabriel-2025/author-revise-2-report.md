I've answered every point in the round-2 report and re-run the entry twice with `python tools/entry.py all entries/gabriel-2025`. Both runs passed in about 41 minutes with identical numbers, the checks show 0 errors, and the record validates against its schema. Nothing is committed.

## Outcomes
No outcome changed. The verifier agreed with all 43 outcomes in round 2, and that is recorded in a new `verifications` entry. Two changes are written under `proposed` for round 3:

- **fig3a-decoding-shock-gt-ns**: verified as reproduced (assumed); proposed partially reproduced. I ran the shuffled-label control the verifier asked for: each mouse decoded again with its outcomes permuted 5 times.
  - Pre-shock epoch: shocked mice score as high with shuffled outcomes as with the real ones (0.476 against 0.489). Non-shocked mice score below their own shuffled value (0.108 against 0.230). Measured against the shuffled values, the pre-shock difference is not significant in any cohort or coding (p ≥ 0.55). So the verifier's base-rate concern holds for this epoch.
  - Shock epoch: the difference survives the control (C1 N1 p = 0.046 to 0.054; with failure as the positive class, p = 0.0018 to 0.013).
- **figs2-innate-behaviors**: verified as blocked; proposed not reproduced. I ran the escape part, with escape as the STAR Methods define it: off the platform in the final 2 s of the tone. On day 1, shocked mice's escape-excited cells are not more active in any of 24 runs (p = 0.40 to 0.99). The criterion needs every part to hold, so the claim fails whatever jumping would show.

## What I added
- **fig3b and fig3c cell sets** are now also built from the other three period and frame readings (clock windows), and the base sets are run on the paper's tone bouts.
  - fig3b fails in 24 of 24 cases on the clock windows. On the paper's bouts it would pass in two of three cohorts, so the record now says the outcome also rests on the clock windows. The README now marks it as assumed.
  - fig3c: the two readings still disagree on the clock windows (E1 fails, E2 holds) and both fail on the paper's bouts. It stays blocked.
- **fig4b**: a paired test of the hybrid model against avoid-only, printed but deciding nothing. On the clock windows, p = 0.0035 to 0.0073 under the claims file's update and 0.078 to 0.35 under the Methods' formula.
- **Speed**: the decoders now run in four processes with one OpenMP thread each, giving the same predictions. That fits 342 decoders, up from 80, into the same 41 minutes.

## What I corrected
- **fig1p**: the text now reports all eight runs, including the seed run in cell 46 that was reported nowhere. Shocked mice are higher in all eight (difference 4.3 to 6.5), and p ≥ 0.05 in three.
- **fig1f notes**: the rule disagrees with the hand scoring on 24 of the 252 hand-scored trials (clock windows) and 36 (paper's bouts), not 26 of 358.
- **fig4b text**: alpha ranges from 0 to 1 under the Methods' formula, with 0 in mouse F2, where all three models coincide. The multi-start ranges are fixed.
- **Summary and README**: the claim that everything was run on the paper's bouts, the description of Sidak and Fisher's LSD, the event-call sentence, and the runtime (41 min, also in `entry.yaml`).

## Not done
- **Low event-call counts** (round-1 point 2): I found no further cause. The finding stands, and the record says this point is still open.
- **One-way ANOVA in fig4b**: the verifier noted it does not compare hybrid with avoid-only. I added no question, because that test is the paper's own (Methods and the Figure 4B legend), so the claims file reads it correctly. The question about the R(t+1) update was already in `questions/gabriel-2025.yaml`.
- **Jumping and rearing** (figs2) are still not scorable. The CILDS and cell-registration claims stay blocked, as verified.
- **Verifier's own slip**: their round-1 reason for zenodo-dandiset-link said "spread under 0.04 s", but cell 15 shows up to 0.050 s. It is noted in round 2; the round-1 text is left as it was.

Unrelated untracked dotfiles (`.bashrc` and similar) appeared in the checkout. I did not create them and left them alone.
