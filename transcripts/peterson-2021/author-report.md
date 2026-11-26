The attempt is complete: the entry ran from a clean environment, its checks pass, and the handover package for the verifier is built. I did not verify my own work. I did not come across any earlier attempt on this paper. Besides the paper, the claims file and the dataset, I read only the paper's own code on GitHub (commit 04c6faf) and the Figshare projection matrices it names.

## 1. Outcomes (DANDI:000055, version 0.261123.1703)

| Claim | Outcome |
|---|---|
| subject-days | reproduced |
| roi-projection-link | reproduced |
| cohort | partially reproduced (7 subjects have depth electrodes, the paper says 5) |
| fig2-event-counts | not reproduced (fewest events per subject is 210, against 151 ± 15.1) |
| fig2-features-differ-across-subjects | reproduced |
| fig2-reach-shape | partially reproduced (no angle density peaks within 15° of ±90) |
| fig2-bimanual-skew | reproduced |
| extfig2-1c-contralateral-larger | reproduced |
| extfig2-2-feature-correlations | partially reproduced (5 of 6) |
| fig2-days-and-waking | partially reproduced (S04's busiest day holds 40% of its events) |
| fig3-group-lfb-decrease-hfb-increase | reproduced, assumed |
| fig3-sensorimotor-largest | reproduced, assumed |
| fig3-lfb-more-widespread | blocked, methods_underspecified (the two readings disagree: 7 vs 7 regions, 34.2 vs 23.9 bins) |
| fig4-precentral-subject-variability | partially reproduced, assumed (3 of 4 parts; S09 shows no high-frequency increase) |
| fig5-band-power-differs-across-subjects | reproduced, assumed |
| table1-subject-band-power-ci | partially reproduced, assumed (21 of 24 values inside the intervals) |
| fig5-recording-day-effects | partially reproduced, assumed (20 of 24 agree) |
| extfig5-1-baseline-reduces-day-variability | reproduced, assumed |
| discussion-day-changes-small | reproduced, assumed |
| fig6b, fig6-r2 (largest R² 0.177), fig6c, fig6d-upward, fig6d-largest | reproduced, assumed |
| extfig6-2-angle-most-retained | partially reproduced, assumed (the order of the next four features differs) |

## 2. Dataset, assumptions, questions

**What the dataset holds:**
- The subjects and days match Table 2 exactly.
- The Figshare projection matrices match the electrodes of all 12 subjects. This uses the code's row rule; the first row of each file is the region density.
- The ECoG of three files ends hours before the day ends (sub-01 day 7, sub-04 day 3, sub-06 day 3), so 237 events have no neural data. Another 125 events fall on NaN samples.
- There are 8088 events, more than the paper analysed, and nothing marks the paper's subset (rated major).
- Undocumented conventions:
  - the reach angle is in image coordinates (y downward);
  - the bimanual overlap is in seconds although it is described as a fraction;
  - the pose is labelled meters but holds pixels;
  - the good-electrode flags differ between a subject's days;
  - 24 electrodes have no position;
  - the R² columns in the electrodes table have no description.
- One event in sub-08 day 4 has timestamps a day apart in two tables.
- The clock is consistent with the events in 11 of 12 subjects. It could not be established for sub-09.

**Assumptions** (recorded as `assumed: true` on the outcomes):
- how the segment rejection pools power over electrodes and frequencies;
- each event is projected to regions with its own day's good-electrode flags;
- the regression and electrode-level analyses use electrodes that are good on every day.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings): the pooling in the segment rejection, the measure behind "widespread", and whether bad electrodes were removed per day or per subject.

**Questions to a reader:** none.

## 3. Protocol points

1. The roi-projection-link criterion says "drop all-zero rows", but the code also drops the first non-zero row. I used the code's rule and recorded it as a deviation.
2. The protocol asks for notebooks under about 10 minutes. This one cannot be, because the data are about 150 GB of ECoG chunks. It runs in 37 minutes and I recorded that.
3. Running every random step under five seeds is too costly for 3904 Huber models. Under the four extra seeds I refit only the full-model R² of the top models; Delta R², coefficients and retention were not refit. This is recorded as a deviation.
4. For the clock check with an event table on continuous recordings, the protocol's guidance did not fit directly. I contrasted band power at true onsets with pseudo-onsets 3 s earlier in the same segments.
5. The cohort claim has no rule for a partial result. I used `partially_reproduced` because one count differs.
6. It is unclear when a small event-set choice counts as "resting on an assumption". I marked every spectral and regression outcome `assumed: true`.

## 4. Runtime and failures

- The run took about 2 h 33 min (05:06 to 07:39 UTC).
- Notebook: 36.6 min. The ECoG streaming took 8 min, the regression 23 min and the seed refits 3.5 min. Peak memory was 1.8 GB per worker.
- Nothing failed in the final run.

During development I fixed these:
- h5py's remote chunk lookups took about 0.1 s each, so I read the chunk index from the file directly and fetch byte ranges in parallel;
- NaN samples in the ECoG were at first not caught by the segment rejection;
- I had accidentally deleted part of the helper module in an earlier edit and restored it.

Files are in `entries/peterson-2021`:
- reproduce_peterson_2021.ipynb
- ajile.py
- entry.yaml
- README.md

The record is `attempts/peterson-2021-02.yaml`.
