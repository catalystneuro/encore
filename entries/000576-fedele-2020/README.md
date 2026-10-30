# Fedele, Tzovara et al. (2020) from dandiset 000576

Tests the findings of [Fedele, Tzovara et al. (2020)](https://doi.org/10.1016/j.neuroimage.2020.116705)
that can be tested on [DANDI:000576](https://dandiarchive.org/dandiset/000576/0.231010.1811), which
holds the bipolar amygdala iEEG of 9 patients (14 amygdalae) and the spike times of 42 units from 5 of
them, recorded while they watched blocks of fearful faces and of landscapes. The BOLD time courses and
the continuous microwire signals the paper also used are not in it.

| Claim | Outcome |
|---|---|
| Delta power falls during AVERSIVE sequences (Fig. 1B) | Blocked: methods underspecified |
| High gamma power rises in the first 2 s (Fig. 1C) | Not reproduced |
| No effect in the other bands | Not reproduced |
| Modulation indices of Table 2, their correlation, and the SOZ claims built on them (5 claims) | Not reproduced |
| Delta MI negative in 12 of 14 amygdalae; HGP more specific than delta; inverse MI relation in nSOZ amygdalae | Reproduced, resting on assumptions |
| 41 neurons above 1 Hz from 9 amygdalae | Partially reproduced |
| All neurons fire more in AVERSIVE; gradual, sustained increase | Not reproduced |
| Firing-HGP correlation does not differ between conditions | Reproduced, resting on an assumption |
| Spatial synchronisation correlates with FRV | Not reproduced |
| Firing correlates with HGP (and muHGP and BOLD) | Partially reproduced (HGP only) |
| Regression of the firing-HGP correlation on FRV and SSI | Partially reproduced |
| Claims that need BOLD or the microwire signals (7 claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper links no code, and its Methods leave open how the power envelopes are z-scored, which
decides most of the iEEG results; every reading was run and is shown. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/000576-fedele-2020-01.yaml`](../../attempts/000576-fedele-2020-01.yaml).

- `reproduce_fedele_2020.ipynb`: the analysis. It takes about three minutes, most of it streaming the
  files and running the permutation tests.
- `amygdala.py`: loading the files, the band power envelopes of Methods 4.8, the cluster-based
  permutation test with the within-patient form of the paper's mixed model, and the firing rate
  measures. Other notebooks on this dandiset can import it.
