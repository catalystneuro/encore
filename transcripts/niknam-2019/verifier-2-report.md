**Verifier report, round 2: niknam-2019-01**

The claims file has 34 claims, and the attempt record has 34 outcomes:
- 5 reproduced
- 1 partially reproduced
- 3 not reproduced
- 25 blocked: 24 too_large, 1 methods_underspecified (fig5a-n-model-no-perisaccadic-gain), 1 metadata_insufficient (figs1-rf-centres)

No outcome in the attempt record carries `assumed: true`.

**1. Outcomes**

| Claim | Outcome | Agree | Basis (this notebook) |
|---|---|---|---|
| probe-locations-link | reproduced | yes | Cell 9: 41/41 files matched to a probe_list row, 0 rows without a file. The recomputed RF is the listed probe for 38 neurons and the listed probe or a neighbour for 41 (threshold 37). FF minus RF gives 27 left and 14 right. |
| methods-neuron-counts | reproduced | yes | Cell 12: 41 neurons, 11 sessions, 27 leftward neurons in 9 sessions, 14 rightward in 2. |
| fig1b-saccadic-suppression | reproduced | yes | Cell 18, (b, i): count 8, 2.235 and 1.239, all within tolerance. Both values sit near the lower edge of tolerance. 5 of the 8 neurons are in nuron_list (cell 40: 35/41 agree). |
| fig1c-ff-remapping | not_reproduced | yes, under the claims file | Cell 21: 8 neurons, 0.792 to 1.609. 0 of 3 numbers in tolerance. |
| fig1d-st-remapping | not_reproduced | yes, under the claims file | Cell 24: 11 neurons, 0.749 to 1.629. 0 of 3 numbers in tolerance. |
| fig1e-ff-and-st-remapping | not_reproduced | yes, under the claims file | Cell 27: 6 neurons, 0 of 5 numbers in tolerance. |
| fig1-remapping-longer-latency | reproduced | yes | Cell 30: RF peak 62 ms; FF peak 108 ms and ST peak 99 ms. The record says plainly that only the RF peak does not depend on how the neurons were selected. |
| fig1-example-neurons | partially_reproduced | yes, under the claims file | Cell 33: three of four examples match on values with D2 p < 0.05. See the claims-file point below. |
| 24 S-, F- and A-model claims | blocked, too_large | yes on the outcome, no on the stated numbers | See section 2, cell 37. As ported, the selection step needs 345 h on 4 CPUs, before the full fits, the A-model and the simulations. |
| fig5a-n-model-no-perisaccadic-gain | blocked, methods_underspecified | yes | O8. The other four N-model claims (fig5a-s-f-beat-n-model and the three fig5b claims) need the N-model according to the claims file, and their notes say so. |
| figs1-rf-centres | blocked, metadata_insufficient | yes | No grid geometry exists anywhere in the archive. |

Places where the claims file may misread the paper (reported, not corrected):
- **fig1-example-neurons.** The statement and the `statistics` block give p < 0.001 for each example, but the criterion only asks for "a significant change by D2", which means p < 0.05.
  - Under (b), only the example with both effects reaches p < 0.001 (cell 33: 0.00063 and 0.00037; the FF example is 0.017, the ST example 0.0059).
  - If the criterion used the paper's p, 1 of 4 examples would match, and the outcome would be not_reproduced.
  - The notebook reports this but does not let it decide.
- **O1 may be too narrow (round-1 problem 2).** The author has put this to a reader as a question.
  - The variant that comes closest, a signed-rank test over the bins of the smoothed curves, treats 71 smoothed and autocorrelated bins as independent pairs. That is why several of its p-values are about 1e-13 (cell 40).
  - So that variant is excluded by the Methods ("not estimates of firing rate", paper line 151), and it is also anti-conservative.
  - The reader question should say so.

**2. Sentences the numbers do not support**

- **Cell 37** says: "This port of `select_bases.m` takes about 7 ms per fit, about 1,000 hours on 4 CPUs for the 41 neurons. A fully batched port that evaluates only the nonzero samples would still need about 28 CPU hours, 7 hours on the runner's 4 CPUs, in this run."
  - Cell 36 prints "2.2 ms per fit", "1,380 CPU hours, 345 hours on 4 CPUs" and "lower bound … fully batched: 11.5 CPU hours, 2.9 hours on 4 CPUs".
  - None of the four numbers in the sentence matches this run.
- **The limit argument rests on the batched figure.** Cell 0, cell 37 and the notes of all 24 too_large outcomes say the cost is "over the 60 minute notebook limit and the five hours of an author run, for the selection step alone", which they tie to the batched figure.
  - This run's batched lower bound, 2.9 h on 4 CPUs, is under five hours.
  - Only the as-ported estimate (345 h) and the steps that come on top (full fit, ten A-model fits, simulations) exceed it.
  - The lower bound has also moved between runs: 13, then 28, now 11.5 CPU-h.
  - The record's round-1 responses repeat "about 28 CPU hours, 7 hours on 4 CPUs" for all 25 model claims.
- **Probe timing is stated too narrowly (minor, decides nothing).**
  - The Summary (cell 41) says probe runs last 7 ms "with 6, 14 and 21 ms runs, and gaps of 10 to 21 ms". The record's metadata_error finding says "others 14 or 21 ms" and "gaps of 10 to 21 ms".
  - Cell 4 prints runs of 8 to 28 ms and gaps of 7 to 28 ms. These are rare, but they are not covered by the sentences.

I checked every other sentence of the "**Result:" cells (10, 13, 19, 22, 25, 28, 31, 34), the Summary, the README and the record's notes and findings against cells 3–40, and the numbers support them. Examples: the 5/8 overlap with nuron_list, "9 to 19" neurons and "6 to 19" neurons across variants, 36/41 against 15/41 agreement on ST, fixation values off by 0.07 to 0.19 spk/s with SEs within 0.01, the -495 to -100 ms window within 0.054 spk/s, the RF example scan from 53.87 to 59.68, and the 1 ms saccade-index shift giving 44.87 and 33.94.

The README's table is consistent with the record: one methods_underspecified claim, 24 too_large and one metadata_insufficient.

The record's `verifications` entry gives my round-1 reasons faithfully, mostly in my own wording, with the problem numbers attached correctly.

**3. Round-1 points**

Resolved:
1. Reading (a) is now reported as "not testable", with the data check showing that no trial has the same probe in both windows (cells 4 and 15).
2. Partly resolved: the time-bin pairings and the per-neuron p table were added (cells 15 and 40), and the question is put to a reader. The outcome still depends on the reader's answer; see below.
3. The fixation set was investigated (window scan and saccade-index shift). It is not identified, and the record now says so.
4. and 5. Both are now disclosed in the conclusions and notes.
7. The probe order is explained: it restarts after the saccade, three sessions use 75 or 80 codes, and long runs take one place in the order.
8. The dead branch in `population` is removed.

All section C requests were met except the docx comparison, which the record says was not done. That comparison bears on no conclusion.

Remaining points that bear on a conclusion:
- **too_large justification (problem 6).** Cell 37, cell 0 and the 24 too_large notes need this run's numbers. The argument should rest on the as-ported cost (345 h) plus the steps that come after the selection, not on the batched bound exceeding five hours, since the batched bound is now 2.9 h. The outcome itself stands.
- **fig1c, fig1d and fig1e (problem 2).** These remain not_reproduced only under O1 as written; the reader's answer to the pairing question could change them. The question should say that the smoothed-bin test is anti-conservative.
- **fig1-example-neurons.** The criterion's p < 0.05 against the paper's p < 0.001 is a claims-file point. It decides between partially_reproduced and not_reproduced.
- **RF example (problem 3).** The paper's fixation set is still not identified, which leaves the RF example unmatched under onsets (closest neuron 56.94 against 60.89).

Not bearing on a conclusion: the RF example's fixation set, beyond the above, and the docx descriptor. The paper's reference list is public in the version of record, and O8 asks for ref [48] to be identified if possible. The attempt did not try, but this cannot change any outcome, because the four too_large N-model claims would still be blocked by cost.
