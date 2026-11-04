# DeWeese and Zador (2004) from CRCNS ac-2

Tests the findings of [DeWeese and Zador (2004)](https://doi.org/10.1152/jn.00197.2004), "Shared
and private variability in the auditory cortex", on [CRCNS ac-2](https://crcns.org/data-sets/ac/ac-2)
(doi:10.6080/K0G44N6R), which holds the paper's 33 anesthetized whole-cell recordings in rat
auditory cortex (29 with a simultaneous LFP) and its six TTX recordings.

| Claim | Outcome |
|---|---|
| Example neuron: q = 0.23 mV for one tone, 0.88 mV over 26 tones | Reproduced |
| Example neuron's mean responses: latencies, heights, shape | Partially reproduced |
| Spread of total variability across neurons (7/33 low, 18/33 high) | Reproduced (assumed) |
| Mean total variability 4.6 mV | Reproduced (assumed) |
| LFP-based culling, 4.8 to 3.1 mV | Reproduced (assumed) |
| Residual LFP-PSP correlation after culling | Reproduced |
| LFP-based culling and estimation, 2.9 mV, 26/29 reduced, up to 71% | Partially reproduced (assumed) |
| PSP-based culling, 2.2 mV, 32/33 at most about 3 mV | Partially reproduced |
| PSP-based culling can increase q for some tones (18/33) | Partially reproduced (assumed) |
| Best estimate of private variability, 1.6 mV over 28 neurons | Reproduced |
| Random culling controls (4.5, 3.67, 2.98, 2.9 mV; 29% and 38% culled) | Not reproduced |
| Large responses (at least 15 mV): 2.9, 1.9 and 1.5 mV | Reproduced |
| Large-response controls, 3.2 mV | Not reproduced |
| Coefficient of variation of large responses | Partially reproduced |
| LFP variability does not differ with neuronal variability | Reproduced |
| Anesthesia groups | Partially reproduced |
| Spontaneous activity before the tone is anticorrelated with the response | Reproduced |
| Overfitting correction in the Figure 5 neuron | Reproduced |
| Private 1-3 mV, shared 0-10 mV | Partially reproduced |
| 14/33 neurons with a tone within a factor of 2 of 0.38 mV | Reproduced |
| mEPSP size 0.39 mV, CV 0.36 | Blocked: methods underspecified |
| Repetitions, rest potential, input resistance | Reproduced (assumed) |
| No effect of access resistance or depth | Reproduced (assumed) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

"Assumed" marks outcomes that rest on a choice the paper does not make, mostly the spike rule:
the data set gives each neuron a spike threshold, which is used here, and the claims file's
-20 mV rule is shown alongside. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/crcns-ac-2-deweese-2004-01.yaml`](../../attempts/crcns-ac-2-deweese-2004-01.yaml).

- `reproduce_deweese_2004.ipynb`: the analysis. It streams the 265 MB data tar once (about 30 s)
  and runs in about three minutes.
- `ac2.py`: loading the data set from the CRCNS bucket, the PSP height, q, the culling and
  estimation procedures of the Methods, and the mEPSP detectors. Other notebooks on this data set
  can import it.
