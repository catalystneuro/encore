# Yang, Ni, Sun, Xing, Wang, Zhang, Zhu & Xu (2025) from dandiset 001212

Tests the findings of [Yang et al. (2025)](https://doi.org/10.1109/tnsre.2025.3614867) that can be
tested on [DANDI:001212](https://dandiarchive.org/dandiset/001212/0.241023.0931), which holds 600 s,
4-channel LFP epochs around the seizures of 7 pilocarpine rats (DG, CA1, CA3, ANT), in 4 baseline
and 4 closed-loop stimulation groups per rat. The files carry no seizure or stimulation times, so
both are found from the LFP here, and every result that uses them rests on that assumption.

| Claim | Outcome |
|---|---|
| cf_w at onset is consistent within baseline groups, not between them (Table S1) | Reproduced (self-pairs reading) |
| R1's top cf_w node goes ANT, ANT, CA3, DG (Figure 2) | Reproduced |
| GC targets give 8 target and 20 non-target groups (Figure S2) | Partially reproduced |
| Target stimulation shortened seizures in every rat | Not reproduced |
| Some non-target stimulation lengthened seizures | Reproduced |
| Sites differ within R2, R3, R4, R5, R7, not R1, R6 | Partially reproduced |
| Target -0.26 against non-target 0.038 normalized duration | Not reproduced |
| Five named non-target groups shortened seizures, less than targets | Not reproduced |
| Same site as target shortens more, DG, CA3, ANT | Not reproduced |
| PSD ratio after target stimulation, alpha and theta or beta up, gamma down | Not reproduced |
| Other bands unchanged | Not reproduced |
| Fewer IIS 15-45 s after seizures with target stimulation | Reproduced |
| Ictal ripples do not differ | Reproduced |
| Target stimulation reduces ictal fast ripples | Not reproduced |
| Seizure frequency, seizure duration proportion, interictal IIS and HFO (five claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/yang-2025-02.yaml`](../../attempts/yang-2025-02.yaml).

- `reproduce_yang_2025.ipynb`: the analysis. It takes about five minutes, most of it streaming the
  56 files once.
- `yang.py`: loading, the stimulation-train and seizure detectors, conditional Granger causality,
  PSD ratios, interictal spike and HFO detection, and the one-pass feature extraction. Other
  notebooks on this dandiset can import it.
