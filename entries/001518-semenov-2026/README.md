# Semenov et al. (2026) from dandiset 001518

Tests the findings of [Semenov et al. (2026)](https://doi.org/10.1016/j.bioelechem.2026.109283)
that can be tested on [DANDI:001518](https://dandiarchive.org/dandiset/001518/0.261006.1957). The
dandiset holds ten escalations of 1-us pulses from 25 to 250 V, five with FluoVolt and five with
Di-8-ANEPPS, each as 19 sets of 100 strobe images.

| Claim | Outcome |
|---|---|
| Dye calibration, 26% and 9.1% dF per 100 mV (Fig. 3) | Partially reproduced |
| FluoVolt departs from linearity from about 200 mV, Di-8-ANEPPS stays linear (Fig. 3) | Not reproduced |
| FluoVolt saturation at 66% and -83% (Fig. 2A) | Not reproduced |
| FluoVolt stable without pulses and within sets (Fig. 2A) | Not reproduced |
| FluoVolt maxima of 71% and -83.5% (Fig. 4A) | Not reproduced |
| FluoVolt cathodic decline from 71% to 45 to 50% (Fig. 4A) | Not reproduced |
| IMP reduction of 2% and 12% for 10- and 100-fold conductivity, Eq. (2) (Fig. 5B) | Partially reproduced |
| Di-8-ANEPPS claims at 570 to 1400 V/cm (Figs. 1, 2B, 4B, 4C, 7B; eight claims) | Blocked: data missing |
| Alternating sets, 0.3-us pulses, Gd3+, Ca2+ imaging, two-pulse protocol (15 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files give the pulse amplitude in volts. The paper gives field strengths in V/cm, and neither
it nor the files give the factor between them. The voltages span a factor of 10, while the
paper's field strengths span a factor of 33. Under the paper's dye calibration, the low-field
response of both dyes puts 25 V near the paper's lowest level, 43 V/cm. The attempt adopts this
mapping as an assumption, under which the sets reach 430 V/cm, and shows the mapping that puts
250 V at 1400 V/cm as a variant. Each field of view holds several cells, while the paper
analysed one per experiment, so experiment means, the cell nearest the centre and all cells are
each run. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/001518-semenov-2026-01.yaml`](../../attempts/001518-semenov-2026-01.yaml).

- `reproduce_semenov_2026.ipynb`: the analysis. It takes about 15 minutes, most of it streaming
  the files.
- `pef.py`: loading the files, finding the cells and their membrane traces, pole and profile
  measures, Eq. (1) with the time constant of reference [20], and Eq. (2). Other notebooks on this
  dandiset can import it.
