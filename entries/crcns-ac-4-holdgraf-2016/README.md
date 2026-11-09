# Holdgraf et al. (2016) from CRCNS ac-4

Tests the findings of [Holdgraf et al. (2016)](https://doi.org/10.1038/ncomms13654), "Rapid tuning
shifts in human auditory cortex enhance speech intelligibility", on
[CRCNS ac-4](https://doi.org/10.6080/K08S4N4J), which holds the raw ECoG of seven patients who
heard filtered, unfiltered and again filtered sentences, with the events, channel labels and the
stimulus audio. The behavioural control data are not in it.

| Claim | Outcome |
|---|---|
| Behavioural control results (six claims) | Blocked: data missing |
| 92 of 468 electrodes are speech-responsive | Reproduced (101 of 377, under one z-score) |
| HFB is higher in AFTER than BEFORE | Reproduced |
| No HFB change after pink noise | Reproduced |
| HFB is stable over the session | Not reproduced (assumption; holds with a per-trial baseline) |
| AFTER/MIDDLE coherence exceeds BEFORE/MIDDLE | Reproduced (assumption) |
| The coherence change remains after removing the mean response | Reproduced (assumption) |
| 53 electrodes are well fit by eSTRFs | Not reproduced (9) |
| 41 electrodes enter the eSTRF analyses | Not reproduced (9) |
| eSTRF MTFs match the filter type | Not reproduced (assumption) |
| AFTER eSTRFs respond more to unfiltered speech | Partially reproduced |
| MIDDLE eSTRFs predict AFTER better than BEFORE | Reproduced |
| AFTER eSTRFs shift towards MIDDLE (partial correlation) | Partially reproduced |
| The shift correlates with response strength | Not reproduced |
| The shift lies mostly on the STG | Reproduced |
| No eSTRF shift after pink noise | Blocked: no electrode qualifies |
| Seed to target coherence rises after context | Reproduced (assumption) |
| AFTER coherence is closer to MIDDLE | Reproduced (assumption) |
| No change in theta to HFB coupling | Reproduced |
| Envelope coherence: theta rise for unfiltered speech in temporal electrodes only | Reproduced (assumption) |
| Wavelet HFB power rises, low frequencies fall in frontal electrodes | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The eSTRFs predict held-out trials in far fewer electrodes than the paper reports, so the eSTRF
claims rest on 9 electrodes from three subjects; a check of the alignment of stimulus and
response finds no offset that would explain this. Three coherence outcomes rest on the multitaper
bandwidth, which the paper does not give. The data set holds 416 channels against the
paper's 524, its stored values are not in the stated units, and its subjects cannot be matched to
the paper's. The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/crcns-ac-4-holdgraf-2016-01.yaml`](../../attempts/crcns-ac-4-holdgraf-2016-01.yaml).

- `reproduce_holdgraf_2016.ipynb`: the analysis. It takes about 25 minutes, about half of it streaming
  and reducing the 1.6 GB zip.
- `ac4.py`: reading the zip in place, HFB extraction, the auditory spectrogram, epochs and
  z-scores, the leave-one-trial-out ridge eSTRF, partial correlation, MTF and multitaper
  coherence. Other notebooks on this data set can import it.
