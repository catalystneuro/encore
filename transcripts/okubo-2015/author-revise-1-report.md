I've answered all 14 points of the verifier's round-1 report, re-run the entry with `python tools/entry.py all entries/okubo-2015` (passes, 0 errors, about 16 minutes), and recorded the round under `verifications`. Nothing is committed.

**What changed in the outcomes** (now 23 reproduced, 9 partially reproduced, 6 not reproduced, 4 blocked):

Three claims move down to not reproduced, as the verifier gave them:
- **fig1f-rhythmic-protosyllable:** both counts (87 of 135 and 7 of 39) are outside even the criterion's partial band.
- **model-ed10eh-motif:** I pinned the GitHub model code (commit 05dc96b) and ran its three-group script as reading (b). It also leaves neurons in two groups at the end (18 under (b), 13 under (a)), so the sequences are not non-overlapping.
- **fig1de-bout-related** stays not reproduced, now under a new reading (below).

Five claims move up to reproduced. Each rests on a stated assumption (`assumed: true`):
- **The window-adjustment rule (problem 1).** The old rule re-searched every peak outside the syllable. The new one adjusts a window only when the neighbouring syllable's test finds the same burst within 25 ms, as the Methods' passage says. Bird 1's counts are now 107 active, 41 and 44 specific, 22 shared. Bird 2's late counts are 4 shared and 26 specific, with P = 0.00049 against the paper's 5e-4.
- On that rule, **fig3h**, **fig4i** (which the verifier had given as not reproduced) and **ed4j** become reproved within tolerance. For ed4j I dropped the "early only" variant the verifier objected to.
- **fig4-bird2-before-beta:** in answer to problem 7, I added a second reading of the pre-bout exclusion that uses the syllable-onset histogram over its whole ±0.5 s. It gives exactly 4 pre-bout neurons in bird 2, as the paper has. The old reading gives 12. The record says this reading was added after round 1.

**Disagreements I kept and recorded:**
- **ed2qr** stays partially reproduced. The pair count fits and the participation is still weakly related, so the effect is present but weaker; the verifier gave not reproduced.
- **ed5-shared-acoustic-difference** stays blocked as `not_runnable`. The protocol lists that reason for software that cannot be installed (Sound Analysis Pro is Windows-only). I timed streaming the sound in the notebook (15 to 20 minutes for the 30 GB), which shows `too_large` would not fit.

**What I added or corrected:**
- The adjustment rule's counts per pair table and per neuron; the old rule and no adjustment are still shown as variants.
- Coverage on one common warped window per syllable, with the per-neuron durations printed. It still has one syllable outside its interval (bird 1's C, 98.9% against 99.5 to 100%), so ed2st stays partial.
- For the two-peak neuron in bird 2, a significance test of the second peak. Six neurons have one, against the paper's one. Per-neuron latencies and leave-one-out correlations are printed.
- Per-neuron subsong locking tables, post-bout peak latencies, IBI counts for bird 1's protosyllable-stage neurons, the second HVCp reading, and all reading combinations for ed2mo.
- The sound-free part of the ed5 acoustic claim: 16 and 116 shared neurons of the two cell types, against the paper's 24 and 120.
- Bird 4 counts with the new rule; a minimum of 3 neurons for a base period, so bird 6 now cannot be tested for skipping cycles; the corrected pair-count printout.
- A new `code_mismatch` finding: the GitHub motif script raises wmax to 3 where the Methods say 2. The GitHub repository is listed under `inputs`.

**What I did not do:**
- I did not reimplement the eight Sound Analysis Pro features, so the acoustic test itself was not run.
- The paper's group of 9 protosyllable-stage neurons (ed3j) could not be identified from the IBI counts.
- The verifier found no misreading of the paper in the claims file, so no reader question was added.

**Decisions for you:**
- **ed5-shared-ra-x-proportion** stays reproduced, but the two denominator readings now disagree: P = 0.062 with the neurons tested in the pairs, and P = 0.018 (a significant difference) with all juvenile neurons of birds 1 to 6. I adopted the first, because the second counts as "not shared" neurons that were never tested for sharing. Round 2 may not accept that.
- Several of the new reproductions depend on rules I wrote after seeing round 1. They follow the Methods' text more closely than the old ones, and every alternative reading is still printed. Round 2 should judge them on that basis.
