I've handled every point in the round-2 report. The entry was re-run with `python tools/entry.py all entries/vinograd-2024`: all four notebooks pass, `check` reports 0 errors, and the record matches its schema. Nothing is committed.

**Outcomes**
- **No recorded outcome changed**, as round 2 requires.
- **ed3h:** stays partially reproduced, with a proposed change to reproduced for a third round. Like ed3g, it would rest on the seed-0 fits, where both readings give p = 0.0079. The reason is under `proposed`; the analysis is the existing four-seed cell.
- **ed7f and ed8gi:** now `assumed: true` on the M70 choice, each with an "Assumed:" deviation. The ed8gi conclusion says plainly that M70 is left out of ed7f and kept in ed8gi, and that each choice gives "not reproduced".

**New outputs**
- **Cross-seed stability (ed4c, ed4d), the verifier's new point.** Refits of the same session with the four seeds share 47% of the five strongest x1 neurons on average (13 to 90% by session). The two conditions share 7% over all seed pairs, which is the chance level. So the 4% overlap between conditions is lower than the fit-to-fit variation, and the outcome stands. For ed4d, the x1 vectors of different seeds of one session have a mean absolute dot product of 0.75.
- **Decay-constant fit window (ed4hi).** I added 5 s and 20 s windows next to the 10 s one. With 5 s, the observation sessions show a difference (Mann-Whitney p = 0.029, signed-rank p = 0.125). The outcome stays partially reproduced, and the helper no longer calls the 10 s window "standard".
- **M70 values.** The notebook now prints M70's x2 projection before the first onset: 0.00 over frames 1 to 100, −3.78 in the last 5 s, −1.26 overall.
- **M70 cell ranks.** The notebook now prints each responsive cell with its own rank. This showed the finding had the pairing wrong: cells 1, 2, 3, 5 and 22 rank 2nd, 4th, 1st, 8th and 64th. The finding is corrected.

**Text corrected**
- Annotation start times are 56 to 96 s, not 56 to 152 s.
- The README now says the cross-validation notebook takes about 30 minutes. `entry.yaml` has this run's times: 13 min for the fits notebook, 30 min for cross-validation.
- The ed4g notes no longer compare a per-baseline count with the paper's 1.6.
- The in-sample bound is now stated for the neural R2 only (methods-cvr2), in both notebooks and the notes.
- The earlier M70 file is described as 4426 frames (443 s), and 350 s as the end of the BALB/c interval.
- ed8c no longer says M70 starts "from −5.90": every trajectory starts at 0, and −5.90 is the value at the end of ISI1.
- The unclear sentence about the Cb comparisons in fig2d is reworded.

**Record and questions**
- Round 2 is recorded under `verifications` for all 54 claims. The verifier disagrees with the recorded outcome only on ed3h, where it would give reproduced.
- I added `questions/vinograd-2024.yaml` with one question for a reader on ed10g. The criterion says "non-targeted neurons", while the Results decode from follower x1 neurons, defined with the 50 µm exclusion. The claim's notes say it is asked.

**Not done, and why**
- **fig4hj** stays blocked as `data_missing`, not `methods_underspecified` as the verifier suggested. The claims file lists fig4a as a dependency, and the protocol blocks a dependent claim for the same reason.
- **ed9d:** the verifier called the criterion ambiguous but did not say it misreads the paper, so I added no question.
- **x2 target lists and M70/M18R x2 projections:** these two points do not bear on any conclusion and are left as they are; the record says so.
