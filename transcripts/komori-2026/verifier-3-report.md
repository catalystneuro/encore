# Verifier report, round 3: Komori et al. (2026) on DANDI:001425

The claims file has 24 claims and the attempt record has 24 outcomes. One outcome has a proposed change: `rest-ic-count-and-window`. I reviewed only that one, in `reproduce_komori_2026_features.ipynb`.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| rest-ic-count-and-window | not_reproduced (verified: partially_reproduced) | **Yes** | — | See below. |

**The numbers come from the data.** The text in cell 9 and the record's notes match the printed outputs of cells 7 and 8.
- **IC count (cell 7):**
  - Under R5 a, 13 ICs have the highest median under both readings: 0.6691 under (a) and 0.6763 under (b). 10 ICs reach 0.6137.
  - Under R5 b, reading (a), the 7-IC and 10-IC counts tie at 0.5394. Both counts select the same set, [4, 12, 13, 18, 20, 22, 28], so they are one model. 13 ICs reach 0.4712.
  - Under R5 b, reading (b), 7 ICs are highest at 0.5880.
  - No Holm-corrected rank-sum test is significant (p ≥ 0.69).
- **Window (cell 8):** 0.5 s has the highest median under both selections: 0.6185 against 0.6137 at 1.5 s under R5 a, and 0.5476 against 0.5394 under R5 b. All Holm p = 1.0.

**The choice behind the change was not made to reach the result.** The outcome changed because the decomposition changed:
- The SVD components now keep their singular values, as in the paper's code (`normalize_svd`), instead of being divided by them as the Methods write.
- JADE now runs to convergence (101 sweeps, cell 2).

Cell 20 supports the reason given. With the Methods' scaling, the ratio of the 30th to the 31st eigenvalue is 1.00000000. That means which 30 dimensions jadeR keeps is decided by rounding, not by the data. With the code's scaling the ratio is 1.0188. The change applies to the whole decomposition and every claim, follows the paper's own code, and is recorded as a deviation. It is not specific to this claim.

**The criterion is applied as written.** It reads: "Reproduced when 10 ICs and 1.5 s have the highest median…; partially reproduced when one of the two does."
- **Window:** 1.5 s is never highest, so the window half fails.
- **IC count:** 10 ICs are highest only in the R5 b, reading (a) tie. Taken literally, a tie could count as "highest". But both counts there are the same seven ICs and the same fitted model, so the tie does not compare 10 ICs against 7. Under reading (b), and under R5 a in both readings, another count is highest.

Neither half holds in any real sense, so not_reproduced is the right outcome.

**Caveats, which do not change the outcome:**
1. **Reading (a) is never actually run with 10 ICs kept.** With the uncentred VIF from the paper's code, the "kept" rule ends at 7, 7 and 9 ICs for the counts 7, 10 and 13 (cell 7; `select_ics` in `pupilwf.py`). So the criterion's reading (a), "the number kept as features", has no 10-IC condition.
   - The centred-VIF variant keeps 10 ICs (cell 2) but was not run for this claim.
   - That gap could only affect the IC-count half. The window half fails in every condition, and partial needs one half to hold, so the outcome would only change if the centred variant put 10 ICs highest.
2. **The result depends on the decomposition, and the window margins are tiny.**
   - In round 2, 10 ICs were highest under R5 a, reading (b) (0.717). In this run they are not.
   - One of the three JADE restarts keeps a different 9-IC set (cell 20), and the IC-count comparison was not repeated on it.
   - Under R5 b, the window medians from 1.5 s to 10 s differ by about 0.0001 (0.5394 to 0.5393), with a minimum fold AUC of 0.0013. These models are close to degenerate, so the window ranking there carries little information.

**Possible misreading in the claims file (reported, not corrected).** This is the same point as in round 2. R5 says the paper "states no rule" for resting data. But the paper says such sessions "were therefore excluded from all datasets" (Results, somatosensory, paragraph 1). The finding does not depend on which R5 reading is used.
