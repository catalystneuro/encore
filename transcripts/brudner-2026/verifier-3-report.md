# Round 3 verifier report: brudner-2026-01

The attempt record lists 22 claims under `outcomes`. Only one has a `proposed` block: figs5c-turn-angles, at `brudner-2026-01.yaml:339`. I reviewed only that claim.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| figs5c-turn-angles | not_reproduced | Yes | — | Cell 24 measures the claims file's two displacements over the dataset's turn events: the heading change from start to stop, and the integral of dtheta over the event. Under both turn sets the claims file names (all turns pooled, or the kept turns), and with every complex file set, the medians are −19.6 to −21.4 and +20.7 to +22.0 degrees. The tolerances are −34.2 ± 3.42 and +33.8 ± 3.38, so every one is outside. The criterion says "Reproduced when both medians are within tolerance under one reading", and no named reading passes. The only bounds that pass are the 20% crossings on both edges of the peak. That reading is not in the claims file, the SI states the 20% rule only for the rising edge (turn onset), and the record says it was adopted after the event bounds failed. So it cannot decide the outcome and is rightly kept as a variant. |

## How I checked it

- **The numbers come from the data.** In `plumes.py:349-357`, `theta_start`/`theta_stop` and `int_dtheta` are read from each file's own heading and dtheta between the event's start and stop indices. Turns are split by the sign of dtheta at the peak, as the S5C legend says. The pooled sets have 80,445, 86,450 and 103,095 turns, and the kept sets have 3,141 and 3,531.
- **The heading change and the integral agree with each other.** The two event measures differ by no more than about 1 degree.
- **The extra readings also fail or are unstated.** Integrating over the run at or above half the peak (Fig. S5A measures peak width at half height) gives −25.0 to −26.6 and +26.8 to +27.7, outside tolerance under every set. Only the 20% bounds give −32.7 to −35.0 and +35.1 to +36.7, within tolerance.
- **Where the events sit.** Also in cell 24: the events start a median of 4 frames after the 20% onset. They lie within the half-height run (1 frame inside it at each end), and 99.9% stop before the falling 20% crossing. These support the record's description. I had said in round 2 that this description was not shown by any output.
- **The text matches the outputs.** Cell 25's text and the record's `measured`, `notes` and `proposed.reason` match the cell 24 output.

## Where the claims file may misread the paper (reported, not corrected)

The claims file takes "the identified turn events" of Fig. S5C to be the dataset's deposited `turn_events` and their start and stop bounds. The paper does not say how a turn's start and end are bounded for the displacement. The SI defines only the onset, as the 20% crossing on the rising edge ("Behavioral Analysis", text line 1792), and the half-height width used in the Fig. S5A clustering. If the deposited bounds are narrower than the paper's, the claims file's readings would measure a smaller displacement than the paper's. The attempt has put this to a reader.
