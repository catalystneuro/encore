# Robotka et al. (2023) from CRCNS aa-5

Tests the findings of [Robotka et al. (2023)](https://doi.org/10.1016/j.celrep.2023.112034) that can
be tested on [CRCNS aa-5](https://doi.org/10.6080/K0TT4P5Q), which holds the spike-sorted units of
four freely behaving zebra finches presented with 110 vocalizations of the 10 call types of the
repertoire, with songs and filtered songs.

| Claim | Outcome |
|---|---|
| The dataset holds the 4 birds and the 110 stimuli of the paper | Reproduced |
| The paper's 100 good units are in the dataset (link check) | Partially reproduced (91 of 100) |
| 292 of 730 units were auditory | Reproduced |
| 46 of the auditory units were inhibited | Reproduced |
| Mean unit SNR 7.42 (Table 1) | Reproduced |
| The first five PCs explain about 90% of the response variance | Reproduced |
| Distress calls and song drive the strongest responses (Figure 3C) | Reproduced (assumption) |
| Z+T beats Z for single units (10.78% to 12.3%) | Reproduced |
| Exactly 100 good units | Not reproduced |
| Ensembles of 20 reach 42% with Z+T against 29.6% with Z | Reproduced (assumption) |
| The top 10% of ensembles reach about 50% | Reproduced (assumption) |
| Systematic confusions (Ne-Te, LT-Be, Th-Te, Di-Ag) | Reproduced |
| Per bird and per sex decoding | Blocked: too few units in one bird |
| PCC rises with the acoustic volume spanned (R2adj 0.1) | Partially reproduced (assumption) |
| Mean SI is unrelated to PCC | Reproduced |
| Mean Entropy Selectivity is negatively related to PCC | Reproduced |
| PCC falls with neural variability (R2adj 0.1) | Partially reproduced |
| Four regressors explain R2adj 0.22 | Partially reproduced (assumption) |
| Claims by brain area (three) | Blocked: metadata insufficient |
| Acoustic clustering claims (five) | Blocked: data missing |
| Anesthetized dataset claims (four) | Blocked: CRCNS aa-4 not analysed in this run |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

The paper's Methods and its code differ on how the decoder is cross-validated; the ensemble claims are
judged on the code's scheme, whose results match the paper's printed values, and the Methods' scheme is
shown beside it. The notebook streams the whole data set (164 GB of tar.gz) from the CRCNS bucket,
which takes about 20 minutes. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/robotka-2023-01.yaml`](../../attempts/robotka-2023-01.yaml).
