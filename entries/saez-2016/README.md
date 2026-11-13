# Saez and Friedlander (2016) from CRCNS pvc-9

Tests the findings of [Saez and Friedlander (2016)](https://doi.org/10.1371/journal.pone.0147642) that can be
tested on [CRCNS pvc-9](https://doi.org/10.6080/K00V89R6), which holds whole-cell recordings of layer 4 cells
in guinea pig V1 slices before and after a pairing protocol: current clamp and voltage clamp controls, and
voltage clamp with 2 uM bicuculline. The single-cell stimulation data of the paper's Figure 3 are not in it.

| Claim | Outcome |
|---|---|
| 28 control (14 VC, 14 IC) and 26 bicuculline cells | Partially reproduced |
| Few control cells change: 1 LTP, 3 LTD, 24 NC of 28 | Partially reproduced (assumed) |
| No net plasticity over the control cells | Reproduced (assumed) |
| Control mean changes (-5.67%, -1.41%, -3.53 +/- 10.26%) | Partially reproduced (assumed) |
| V-clamp and I-clamp control outcomes do not differ | Reproduced |
| Control outcome does not depend on initial strength | Reproduced |
| Example control cell with no change (-1%, p = 0.48) | Reproduced (assumed) |
| Bicuculline: 7 LTP, 9 LTD, 10 NC of 26 | Partially reproduced (assumed) |
| Bicuculline raises the plastic fraction from 4/28 to 16/26 | Partially reproduced (assumed) |
| Bicuculline subgroup mean changes | Partially reproduced (assumed) |
| Same mean, larger variance in bicuculline | Partially reproduced |
| Example LTP (+59.4%) and LTD (-37.6%) cells | Reproduced |
| Bicuculline outcome does not depend on initial strength | Reproduced |
| Figure 3: comparison with single-cell stimulation and the mixing simulation (three claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the
differences from the paper's method.

Eight of the 28 included control recordings are missing or incomplete in the data set, so the control
claims rest on 20 cells. Outcomes marked "assumed" rest on taking the last 120 baseline sweeps as the
pre-pairing epoch, which the Methods' wording and the data set's own spreadsheets support; with the first 120
several outcomes change. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/saez-2016-01.yaml`](../../attempts/saez-2016-01.yaml).

- `reproduce_saez_2016.ipynb`: the analysis. It takes about three minutes, most of it streaming the 1.1 GB
  archive once.
- `pvc9.py`: streaming the archive, reading ABF files in memory, the per-sweep response amplitude, the
  inclusion and file lists of the spreadsheets, and the per-cell classification. Other notebooks on this
  data set can import it.
