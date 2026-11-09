I've finished steps 1 to 5 of the Author section and built the handover. The entry passes `check` (0 errors), the notebook runs from a clean environment in 249 s, and `handover` wrote its package to `executed/001521-semenov-2026/handover/`. Nothing is committed.

**(1) Outcomes** (27 claims)

| Claim | Outcome |
|---|---|
| fig6a-ca-entry-1000-1200 | reproduced |
| fig6a-ca-sustained | not reproduced |
| fig6a-780-not-significant | reproduced |
| fig6b-train-threshold | not reproduced |
| fig6b-650-weak-but-significant | blocked (methods underspecified) |
| fig5b-conductivity-calibration | partially reproduced (uses the paper's Eq. 2 only, no recordings) |
| 21 claims on the potentiometric imaging (Figs. 1 to 5 and 7) | blocked (data missing) |

- **fig6a-ca-entry-1000-1200:** 3 of the 4 readings hold, under both voltage-to-field conversions (see below).
- **fig6a-ca-sustained:** at 1000 and 1200 V/cm the signal at the end of the recording is below zero (-5.4% and -3.8%), so it fails the test against zero. It is still about 7% above unpulsed cells at those fields (p < 1e-8).
- **fig6a-780-not-significant:** the test the criterion names finds no increase. The variants do find one: compared with unpulsed cells, p = 1.3e-6.
- **fig6b-train-threshold:** at 780 V/cm, 4 to 79% of cells respond depending on the reading, against 28%. The criterion is met in none of the 24 combinations of conversion, response rule and region size.
- **fig6b-650-weak-but-significant:** the expected 2 responding cells appear in only 1 of the 24 combinations.
- **fig5b-conductivity-calibration:** Eq. 2 gives 1.33% for a 10-fold increase (expected 2 ± 0.2%) and 11.87% for 100-fold (expected 12 ± 1.2%).

**(2) What I found about the dataset**
- I pinned 0.261006.1845, the only published version; the paper cites none.
- It holds 73 Fluo-4 time-lapses in two sessions: single pulses (31 files, Fig. 6A) and 60-pulse trains (42 files, Fig. 6B). There are no regions of interest or traces, so I segmented the cells myself.
- The potentiometric data are not here. Six sibling dandisets name the same paper (001515 to 001518, 001525, 001526), but the claims file does not list them as data the paper relies on, so I did not use them.
- The files give the generator voltage, not the field strength, and the paper gives no conversion. The files also state a 1.00 mm electrode gap, where the paper says 1.6 mm.
- A "subject" is a field of view. In the train session each one was recorded at up to 7 escalating voltages, so there are 82 distinct cells and 311 exposures. The paper says 224 cells, each tested once.
- The single-pulse session holds 27 cells; Fig. 6A averages 14, and nothing says which.
- The dandiset's description mentions only single pulses. The species name and the age (P1D) given for a cell line are wrong.
- Unpulsed cells lose 12 to 16% of their signal over a recording, and the paper's ΔF does not correct for it. This decides fig6a-ca-sustained.
- The timing check confirms the stated pulse times in both sessions.

Assumptions and questions:
- I adopted no assumption; no outcome is marked as resting on one. I ran both voltage-to-field conversions, M1 (3.9 V/cm per V) and M2 (3.3 V/cm per V), and every tested outcome is the same under both.
- I recorded three questions for the paper's authors as `methods_unavailable` findings:
  - the voltage-to-field conversion;
  - the definition of a "strong" response, the region size and which cells formed each group;
  - whether the signal decline was corrected, and which test was used at 780 V/cm.
- I asked a reader nothing.

**(3) Where the protocol was unclear**
1. Public data the paper doesn't name: the sibling dandisets hold the potentiometric data, but the paper says "on request" and the claims file doesn't mark them as `elsewhere`. The protocol only covers data the paper itself deposited elsewhere. I blocked those claims as `data_missing` and explained why in the notes and a finding.
2. A detail the claims file calls a "standard choice" turned out to change an outcome: the region size, for fig6b-650. Since the paper gives no basis for choosing a size, I blocked that claim as `methods_underspecified` and showed every combination.
3. Claims with no data at all: fig5b is a pure model computation, and the protocol has no `data` category for that. I tested it and said in the notes that it says nothing about the dataset.
4. The criterion's test against zero is biased by the signal decline in unpulsed cells, which the reader could not have known about. I judged on the criterion as written and showed the comparison with unpulsed cells as a variant.

**(4) Runtime and failures**
The work took about 35 minutes, from 22:37 to 23:12 UTC. Nothing failed. Streaming and reducing the whole dataset takes about 4 minutes, and the notebook ran in 249 s.

Files are in `entries/001521-semenov-2026/`:
- `reproduce_semenov_2026.ipynb`
- `fluo4.py`
- `README.md`

The attempt record is `attempts/001521-semenov-2026-01.yaml`.
