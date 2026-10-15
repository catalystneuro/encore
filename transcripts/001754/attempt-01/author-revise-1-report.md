I've answered every point in the round-1 report and re-run the entry. `python tools/entry.py all` passes with 0 errors and the notebook runs from a clean environment in 310 s. Nothing is committed.

## Outcomes
The verifier agreed with all seven outcomes. The only proposed change is to flight-spatial-code; the other six stay as they were.

- **flight-spatial-code:** stays `partially_reproduced`, with a change to `not_reproduced` recorded under `proposed`.
  - **Why:** the verifier's problem 6 was right. The position lookup gave a spike at the lost position (0, 255) a neighbouring sample, though the claims file says such spikes are dropped. With that fixed, Rat1 flight day 9 has 12 of 25 significant units (0.48), down from 13. Five repeats with 2000 shuffles and other seeds give 11 or 12 of 25. Rat2 stays at 3 of 28, which is not above chance. That meets neither the reproduced nor the partial rule.
  - **Why it is only proposed:** I first changed the outcome directly, but `entry.py check` rejects changing an outcome the verifier agreed with. The notebook's result line, the summary and the README say "partially reproduced (verified), not reproduced proposed".
- **si-comparable-to-preflight** (`reproduced`), **fd4-abnormal-selectivity** (`not_reproduced`) and **fig3-stability-across-sessions** (`reproduced`) are unchanged, with notes updated to the new numbers. Fig3's median r is now 0.537 against a null 95th percentile of 0.102.
- The three blocked claims are unchanged.

## What I added or corrected
- **Lookup fix:** a synthetic check in the data check fails with the old lookup.
- **Robustness (problem 1):** a per-unit table for both judged sessions, with Monte Carlo standard errors, plus the seed and shuffle repeats.
- **Shuffle drops (problem 7):** the fraction of real and shifted spikes dropped, per unit and per epoch. Shifted spikes are dropped much more in Rat2's epochs (median 0.307) than Rat1's (0.074). A count-matched variant gives the same counts for Rat2, so the drops don't explain Rat2's result.
- **Rat2 attribution (problem 2):** a table of each file's samples and each rat's spikes in every task window. Each file samples one shared trace at its own rat's spike times, and nothing in the files says which animal was tracked. This is recorded as a caveat and a deviation.
- **Sampling bias (problem 3):**
  - Added epoch durations, unit spike counts and the rate maps' rate × occupancy (about 22 per spike on flight units, so it scales with the spike count).
  - The compared preflight and flight day 9 sessions have similar spike counts.
  - Added two variants: bins with at least 5 occupancy counts, and count-adjusted information. For si-comparable they give p = 0.44 and 0.45.
  - For fd4 the count-adjusted test gives p = 0.0025, against 0.055 for the criterion's test. Flight day 4 maps have fewer spikes, so the bias works against the claim. The outcome still follows the criterion's fixed test.
- **Preflight apparatus (problem 4):** a data check shows the description's "flat rectangular track" sentence and the occupancy footprints. This is now a new `metadata_error` finding and a deviation on both rate-map claims.
- **fig3 (problem 5):**
  - Added per-unit spike counts, information and p in each epoch, and a mean-rate correlation across epochs (rho 0.598) as a partial check that cluster ids name the same neurons.
  - The gap between epochs, 10 of 16 against 1 of 19 significant units, is still unexplained. The two epochs have similar occupancy, spike counts and shuffle drops.
- **No EEG (problem 8):** the data check now lists every group and dataset of all eight files, unfiltered. `acquisition/` is empty and no file holds an ElectricalSeries or LFP.
- **Smaller points (problem 9):**
  - Zero intervals occur in every epoch type and are not mainly in the overlapping epochs. Their cause is still not known.
  - The 277.8 Hz peak sits in a bin with 55 occupancy counts, so it is not a low-occupancy artefact.
  - The rate maps turn out to be smoothed, which is a new finding. That is why no shuffle-corrected value can be computed for them.
- **Shuffle p-values:** for one Rat2 unit some shuffles had no spike with a position. P-values and null statistics now skip such shuffles and report how many there were.
- **Record:** the round is under `verifications` with the verifier's reasons and my responses. The README and the runtime (now about 5 minutes) are updated.

## Not done
- No outcome was changed directly; the flight-spatial-code change waits for a third round.
- A per-map spike count and a shuffle-corrected value for the rate maps could not be produced: the maps are smoothed and cannot be linked to units.
- Cluster identity across epochs can't be checked further, because the files hold no waveforms.
