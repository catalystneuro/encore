# Nakamuta et al. (2025) from dandiset 002020

Tests the findings of [Nakamuta et al. (2025)](https://doi.org/10.1101/2025.01.14.630383),
"Self-organization of high-dimensional geometry of neural activity in culture", on
[DANDI:002020](https://dandiarchive.org/dandiset/002020/0.261004.1410), which holds 129 daily
30-minute HD-MEA recordings of spike detections from seven dissociated rat cortical cultures.

| Claim | Outcome |
|---|---|
| Seven dishes active for more than 10 days | Reproduced (assumption) |
| Activity detectable at 2 to 3 DIV | Blocked: metadata insufficient |
| Activity becomes synchronous with maturation | Reproduced (assumption) |
| Variance spectrum turns from exponential to power-law decay | Blocked: methods underspecified |
| Example dish shifts near 10 DIV, exponent 1.30 | Blocked: methods underspecified |
| Power law in PCA established at about 15 DIV | Blocked: methods underspecified |
| Power-law exponent about 1.2 | Blocked: methods underspecified |
| Shuffling reverts the spectrum to exponential decay | Blocked: methods underspecified |
| Dominant PCs become local, minor PCs stay global | Blocked: methods underspecified |
| Locality spectrum becomes steeper | Blocked: methods underspecified |
| Locality slope emerges progressively from zero | Blocked: methods underspecified |
| Shuffling removes the spatial structure of PCs | Blocked: methods underspecified |
| Avalanches emerge at about 15 DIV, exponent 1.5 | Blocked: metadata insufficient (change to not reproduced proposed) |
| Decay rates of PCA and avalanches correlated | Not reproduced |
| Groups by PCA decay rate show both power laws or neither | Blocked: methods underspecified |
| Groups by avalanches show the same | Blocked: methods underspecified |
| Shuffling breaks the co-occurrence | Blocked: methods underspecified |
| No temporal structure of PCs | Not reproduced (assumption) |
| Network model with Cauchy or Gaussian weights (two claims) | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The files give recording dates but no days in vitro, so results are placed on an assumed DIV axis
(days since the first recording plus 2, with other offsets shown), and claims whose result is a DIV are blocked. The fitted
exponential decay rate of the variance spectra is far below the paper's 0.1 group boundary in nearly
every recording (two active recordings reach it under one fit reading, and it does not separate early
from late recordings), so the claims that rest on that boundary are blocked, and how that rate is
computed is asked of a reader. The readings of the local Moran's I and the locality slope disagree,
so the locality claims are blocked too. The attempt record, with
the reasons and the differences from the paper's method, is
[`attempts/002020-nakamuta-2025-01.yaml`](../../attempts/002020-nakamuta-2025-01.yaml).
