# Fedele, Burnos, Boran, Krayenbühl, Hilfiker, Grunwald & Sarnthein (2017) from CRCNS ieeg-1

Tests the findings of [Fedele et al. (2017)](https://doi.org/10.1038/s41598-017-13064-1) on
[CRCNS ieeg-1](https://doi.org/10.6080/K06Q1VD5), which holds the interictal sleep iEEG of 20
epilepsy patients with the detected ripples, fast ripples and FRandR events. The notebook streams
all 92.5 GB once (about 20 minutes) and runs in about 40 minutes.

| Claim | Outcome |
|---|---|
| The deposit's patients and channels link to Tables 1 and 1S (link) | Reproduced |
| 20 patients, 9 TLE and 11 ETE, 13 seizure free | Partially reproduced |
| Nights and intervals per patient (Table 1) | Reproduced |
| Ripple and FR amplitudes | Reproduced |
| Follow-up does not differ by outcome (on Table 1's values) | Reproduced |
| Channel rates and HFO areas of Table 1S | Reproduced |
| Patient 4 (Fig. 1) | Reproduced |
| FRandR area resected in 13 of 13 seizure free and 3 of 7 others | Reproduced |
| Ripple and FR areas resected as in Table 1 | Partially reproduced |
| FRandR prediction measures (Table 2) | Reproduced |
| Ripple and FR prediction measures (Table 2) | Partially reproduced |
| FRandR more specific than ripples and FR | Reproduced |
| Prediction with Engel I as good outcome | Reproduced |
| Seizure onset zone not resected in ETE patients | Blocked: data missing |
| Patient 17 (Fig. 2) | Partially reproduced |
| Patient 1 test-retest (Fig. 3) | Reproduced |
| Test-retest across patients | Partially reproduced |
| Test-retest by group | Reproduced |
| Spectral classes of FRandR events | Partially reproduced |
| Spectral classes do not differ between TLE and ETE | Not reproduced |
| Location of the HFO area in patients 18 to 20 | Blocked: metadata insufficient |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set holds no outcome, resected channels or seizure onset zone; the outcome claims use the
paper's Table 1 and the colours of its supplementary Table 1S. The attempt record, with the reasons
and the differences from the paper's method, is
[`attempts/fedele-2017-01.yaml`](../../attempts/fedele-2017-01.yaml).
