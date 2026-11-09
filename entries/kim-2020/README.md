# Kim, Atencio & Schreiner (2020) from CRCNS ac-5

Tests the findings of [Kim et al. (2020)](https://doi.org/10.1038/s41467-020-14835-7) on
[CRCNS ac-5](https://doi.org/10.6080/K07H1GSS), which holds the paper's in vivo whole-cell
recordings from mouse A1: 66 current-clamp neurons with pure tones, 40 of them also with the
dynamic moving ripple (DMR), and 39 voltage-clamp DMR recordings (27 excitatory, 12 inhibitory)
from 31 neurons, with the paper's Matlab analysis code and the DMR envelope.

| Claims | Outcome |
|---|---|
| Cohort counts, resting potentials, tone PSP amplitude and kinetics, NDR distribution and its correlation with rest | Reproduced |
| Spike TRFs narrower than PSP TRFs | Partially reproduced |
| PSP histogram modality, STRF significance groups, PSP amplitude ranges | Not reproduced |
| Double peaks and harmonic ratios | Not reproduced |
| Bandwidths of single- and double-peaked STRFs, STRF narrower than TRF, STRF Q above TRF Q30 | Reproduced |
| bTMF higher for small PSPs; no modulation difference between spikes and large PSPs | Reproduced |
| bSMF, CF-BF correlation, bandwidth relations, latency, FSI, nonlinearity thresholds and transitions | Not reproduced |
| Voltage clamp: unimodal currents, matched E-I BFs, broader inhibition, higher EPSC rates | Partially reproduced |
| Voltage clamp: double peaks, bSMF, bTMF, nonlinearity, FSI, latency | Not reproduced |
| Supplementary Figs. 2 and 3 (reliability, intensity) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Most STRF outcomes rest on choices the paper leaves open: which events count as "very small",
what makes an STRF subfield significant, and how bands and bandwidths are measured. The record,
with the reasons, the readings run and the questions for the paper's authors, is
[`attempts/kim-2020-01.yaml`](../../attempts/kim-2020-01.yaml).
