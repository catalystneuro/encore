I've made the round-1 revision. Three claims changed outcome, three that were never run are now tested, and the entry runs cleanly from a fresh environment (`tools/entry.py all`: 0 errors, about 42 min, up from 14). Nothing is committed.

## Outcome changes

| Claim | Before | Now | Why |
|---|---|---|---|
| session-list-link | reproduced | partially reproduced | The pool list is used (in an expert-rule variant) and doesn't match in full: 1451 entries for 1449, 30 have a date suffix, 3 have no trial table. |
| fig1k-model-accuracy | blocked | reproduced | Rebuilt the paper's model from its code (60 sessions, 1000 tuning trials). Balanced accuracy is 0.781 against chance 0.5. |
| fig1k-context-strongest-feature | blocked | reproduced | Context comes first, then the next three features in the paper's order. |
| fig1l-shap-whisker-trial-in-block | blocked | not reproduced | At trial 1 the feature's SHAP value moves against the new context, so the criterion as written fails. I asked a reader whether it misreads Figure 1L. |
| fig3h-rsc-first-context-discrimination | blocked (too large) | reproduced, on an assumption | I ran the pixel part by reading only the trial windows (22 GB in under 2 min). With the 50 ms baseline, RSC is first in both pixels and ROIs; the Methods for 3H point to that baseline through Figure 3F. With 250 ms it ties with wM1. |
| fig3c-jaw-onset | reproduced, assuming the code's trials | reproduced, assuming the Methods' trials | Fixed all four problems the verifier listed. The Methods' correct whisker trials now give 90 ms, inside 108 ± 24. The code's trial set (77 ms) and W+ hits (76 ms) now fall below the tolerance. |

## Kept, disagreement recorded
- **fig1c-auditory and supp1c:** still reproduced. The criterion accepts either session selection, and only the code's list gives the paper's 41 mice and 201 sessions. The verifier would give partially reproduced.
- **fig1j:** kept as partially reproduced, the protocol's meaning for a claim that holds in part. The verifier said it is strictly not reproduced, since the criterion has no partial clause.
- **The seven Figure 2 claims:** still blocked as underspecified. I added a synthetic test showing the Methods' block-shuffle null can't detect an effect shared by both contexts (d' 0.19 against above 5). Whether that null is a valid reading of the paper is now a question for a reader. The d' threshold readings disagree even without it.

## Output added for the verifier's other points
- **Muscimol days:** every session the files type as a pharmacology session is the second date, which supports ranking by date.
- **Late widefield frames:** 910 trials have their first frame after the stimulus late, all in the optogenetics and photoactivation sessions. Leaving them out of fig4c changes nothing.
- **Sessions the expert rule skipped:** the 60 `context_` sessions are now identified, and two variants are shown; neither reaches 201 sessions in 41 mice.
- **Opto sites:** the maps have 41 sites, the claims file's 39 plus two the Figure 4 code drops; the counts on the 39 are the same.
- **Also printed:** the PC3 loadings and sign flips for fig4d/e, and the image stack's shape, type and lack of chunking.
- **supp1d's 100 ms offset:** measuring lick time from the opening of the response window gives exactly the paper's 370, 401, 392 and 418 ms. The criterion measures from the stimulus, so it stays partially reproduced.
- **fig4b:** shown as a variant on the ROI traces only.

`questions/001847.yaml` is new, with the two reader questions above. I added two findings: a question for the authors about the Figure 3H baseline, and the unmarked gaps in the optogenetics imaging. The round is recorded under `verifications`, and the README, `entry.yaml` (runtime) and the lock file (xgboost, optuna, shap added) are updated.

## Not done
- **fig4b, three claims:** still blocked as too large. The seed-to-pixel maps need 367 GB of reads, about 28 min at the measured rate. Added to this notebook's 42 min, that is over the 60-minute limit. A separate notebook could hold it, but there wasn't time to build and run one.
- **fig1k thread count:** the model runs on 4 threads where the paper's code used 20, which can change the fitted trees slightly. This is recorded as a deviation.
