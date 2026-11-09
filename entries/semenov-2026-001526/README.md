# Semenov et al. (2026) from dandiset 001526

Tests the findings of [Semenov et al. (2026)](https://doi.org/10.1016/j.bioelechem.2026.109283) that
can be tested on [DANDI:001526](https://dandiarchive.org/dandiset/001526/0.261006.1851). The dandiset
holds Di-8-ANEPPS strobe images of 11 CHO cells in the alternating 150 and 230 V/cm protocol around
a 1000 V/cm exposure (Fig. 2C and D), and of 8 cells in the 0.3 us escalation (Fig. 4D). The
FluoVolt, 1 us escalation, Gd3+, Ca2+ and two-pulse experiments are not in it.

| Claim | Outcome |
|---|---|
| 150 and 230 V/cm responses stay constant before 1000 V/cm (Fig. 2C, D) | Not reproduced (rests on assumptions) |
| Cathodic dF falls within the 1000 V/cm set, not significantly (Fig. 2C) | Reproduced (rests on assumptions) |
| Lasting reduction of about 20% after 1000 V/cm (Fig. 2D) | Partially reproduced (rests on assumptions) |
| 0.3 us pulses reach a maximum of 53% dF at both poles (Fig. 4D) | Not reproduced |
| Eq. (2): 10- and 100-fold conductivity increases reduce IMP by 2% and 12% (Fig. 5B) | Partially reproduced |
| The other 25 claims (FluoVolt, Fig. 4B escalation, Gd3+, Ca2+, two-pulse) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The outcomes marked as resting on assumptions depend on whether and how a cell-free background is
subtracted before dF is computed, which the paper does not say for these images (the adopted reading
subtracts the background recording made with each cell), and on which cells form the paper's group
of 8: the dataset holds 11, and without the two whose sets depart from the described order before
the exposure, all three Fig. 2C/D claims are met under the background recording and annulus
readings. The background recording was adopted after the results under both readings had been
seen, in the revision in which the annulus reading stopped meeting the Fig. 2C claim. The files give amplitudes in volts, not field
strengths, and do not say which cell in each field was analysed. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/semenov-2026-07.yaml`](../../attempts/semenov-2026-07.yaml).

- `reproduce_semenov_2026.ipynb`: the analysis. It takes 15 to 35 minutes, most of it streaming the
  243 files.
- `strobe.py`: loading the files, the field strength of each recording, the automatic membrane
  trace, pole and profile dF, and Eq. (2). Other notebooks on this dandiset can import it.
