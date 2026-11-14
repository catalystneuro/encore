# Sadeghi, Zhai, Stevenson & Escabi (2019) from CRCNS bst-2

Tests the findings of [Sadeghi et al. (2019)](https://doi.org/10.1371/journal.pbio.3000449) that
can be tested on [CRCNS bst-2](https://doi.org/10.6080/K03X84V3), which holds the analog multiunit
activity of 35 inferior colliculus recordings in unanesthetized rabbits (13 sites for paradigm 1,
11 for paradigm 2, 11 for paradigm 3), the paradigms' sounds and the 195 sounds of the paper's
auditory model, with the paper's MATLAB code.

| Claim | Outcome |
|---|---|
| Example site temporal correlation widths (Fig 1K) | Reproduced |
| Noise correlations stronger than stimulus-driven ones (SNR) | Partially reproduced |
| Model spectral correlations predict neural ones (S5 Fig) | Blocked: data missing |
| Noise correlations more restricted and consistent (Fig 2) | Reproduced |
| Example site, tonotopy removal lowers the temporal classifier (72 to 35%) | Partially reproduced |
| Example site, classifier order and noiseless bound | Partially reproduced |
| Paradigm 1 population classifiers above chance (Fig 3B) | Reproduced |
| Per-sound accuracy above chance except snake temporal (S6 Fig) | Reproduced |
| Mixing coefficient near 0.5 to 0.6 (S9 Fig) | Reproduced |
| aMUA against thresholded MUA (S10 Fig) | Blocked: data missing (the aMUA split-half values match) |
| Example site, original and 1/f correlations similar (Fig 4A to D) | Not reproduced |
| Population, original and 1/f correlations (Fig 4E) | Not reproduced |
| Example site, classification of 1/f sounds (Fig 4F) | Partially reproduced |
| Population, classification of 1/f sounds (Fig 4G, H) | Partially reproduced |
| Example site, two PCs explain most variance (Fig 8B, D) | Reproduced |
| Example site, three-category classification (Fig 8E) | Reproduced |
| Population, three-category classification (Fig 8F) | Reproduced |
| Model, speech and water widths (Fig 5) | Reproduced |
| Model, category half widths (Fig 6A, B) | Reproduced |
| Model, category diversity index (Fig 6C) | Reproduced |
| Model, stationarity index (Fig 7I) | Not reproduced |
| Model, optimal resolution 141 and 100 ms (Fig 9A) | Reproduced (one reading) |
| Model, similar maximum performance (Fig 9B) | Reproduced |
| Model, accumulation rate (Fig 9B) | Partially reproduced |
| Model, time-averaged classifier worse (Fig 9C) | Partially reproduced |
| Model, waves spectral and wind temporal (Fig 9E) | Partially reproduced |
| Model, spectrum classifier lower (Fig 9) | Not reproduced |
| Model, vocalization against background (Fig 10) | Reproduced (one reading) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set is one 5.3 GB tar.gz file; the notebooks stream it once and parse each member in
memory. The neural notebook takes about 35 to 60 minutes, the model notebook about 15 to 25 and the model classifier notebook about 40, depending on the machine. The attempt
record, with the reasons and the differences from the paper's method, is
[`attempts/sadeghi-2019-01.yaml`](../../attempts/sadeghi-2019-01.yaml).
