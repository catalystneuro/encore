I've revised the attempt for verifier round 1. Only one outcome changed: figs7cd-movement-not-time-locked went from not reproduced to partially reproduced, as the verifier proposed. The entry was re-run from a clean environment with `python tools/entry.py all`: all three notebooks pass, `check` reports 0 errors, and the conclusions and record match the new numbers.

**Outcome change**
- **figs7cd:** the claim holds in the familiar run and fails in the novel run. figs7ab-in-field-out-field, which also holds in one of its two environments, was already rated partially reproduced, so this makes the two consistent. Every other outcome is the one the verifier gave.

**Fixes and additions**
- **Ripples (problem 6):** the raw files store the 1250 Hz LFP one channel per chunk, so ripples are now detected from the LFP as the claims file's main reading says. The deposited ripples are now the variant. Detected and deposited ripples agree (79 to 97% overlap, about 2% when shifted by 1 s), and the false positive rate is 0.00098. The pinned version has no raw file for e13-26m1-211119; its LFP comes from version 0.261113.1035. This is recorded under inputs and as a new minor `data_missing` finding.
- **Reactivation readings (problem 3):** the readings are now fully crossed. To keep each notebook under the hour limit, the reactivation analysis is split into `reactivation.ipynb` (novel run) and a new `reactivation_familiar.ipynb`. The fig8b, fig8d and fig8-no-pre outcomes are unchanged; the main fig8b difference is −0.0214 points, p = 0.253.
- **Time 0 (problem 1):** I added a variant that counts time from the first tracked frame for decorrelation, the UMAP plot, place fields, the movement measures, unconditioned similarity and reactivation. Under it, fig8b would be reproduced (late moments reactivated more, +0.0504, p = 0.023) and fig8d would show no difference (p = 0.29). figs6b moves to p = 0.053, still not significant. The claims file fixes time 0 at the epoch start, so these are shown and not judged, and I added the question to `questions/mckenzie-2025.yaml` for a reader.
- **Second novel environment (problem 2):** I corrected the wrong statement about it. For e16-3m2-211211, the second novel environment (the linear track, with its tracking moved onto it) is now run for every claim. The other sessions' epoch names are printed.
- **Model form (problem 4):** the model behind figs7ef now bounds every beta at ±10, as the photometry Methods say. The earlier sign-constrained form is kept as a variant. The outcome is unchanged: dropping velocity is significant in all 28 combinations.
- **Degenerate reading (problem 5):** figs7gh's reading (b) is now described as near zero by construction. The outcome rests on reading (a) and is marked assumed.
- **Spike times (problem 7):** the full spike times are now compared between the two versions in the notebook. They are identical.
- **Text:** corrected the summary's statement about which version labels position in cm.
- **Record:** the round is recorded under `verifications` for all 28 claims.

**Not done**
- No critical finding was reviewed this round; round 2 does that.
- I changed no claim statement, expected value or criterion.

Nothing was committed, as the workflow does that.
