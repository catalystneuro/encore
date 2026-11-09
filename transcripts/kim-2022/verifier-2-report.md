# Verifier report, round 2: Kim et al. 2022 on DANDI:000489 (0.230518.1811)

The claims file has 22 claims, and the attempt record has 22 outcomes:
- 1 partially_reproduced
- 4 not_reproduced
- 1 blocked (other) on Fig. 2C
- 15 blocked (other) on Figs. 3 to 7
- 1 blocked (data_missing)

## 1. Outcomes and assumptions

| Claim | Record | Agree? | Assumption |
|---|---|---|---|
| fig2a-uptake-rises-with-field | partially_reproduced, assumed | Yes (cell 17) | Stated and reasonable: ROI reading (a), both footprints, ROI extent of 3 mm. Bottom side, left footprint and a weakest ROI at 2.4 mm each give methods_underspecified, and the notes say so. The unipolar arm failing at n = 2 also rests on leaving dish 0-03 out (see 3). |
| fig2a-vertical-scales | not_reproduced, assumed | Yes (cell 20) | Stated and reasonable: camera counts are taken as the paper's a.u. The 75% value is 255.2 to 342.8 under every variant. |
| fig2b-exponential-same-slope | not_reproduced, assumed | Yes (cell 23) | Applies the criterion as written; all 12 readings agree. The assumption is stated: top side, scale from electrodes and right footprint give methods_underspecified. |
| fig2c-max-inhibition-50-75 | not_reproduced, assumed | Yes | Stated, and reasonable but a judgement call. The p < 0.01 is placed over the whole range; the "one ROI or more" reading gives partially_reproduced (50% against unipolar at 15.24 kV/cm, p 0.0018; cell 26). At the ROI of strongest inhibition (14.24 kV/cm) p is 0.027 and 0.019, so the test fails there too. The ~20% value fails under every reading. |
| fig2c-inhibition-flat-above-8-7 | not_reproduced | Yes (cell 29) | Holds under every variant, so it needs no assumption. |
| fig2c-weaker-at-6-7 | blocked (other) | Yes (cell 32) | The background rule (mean ≤ 2 s.e.m.) is the attempt's own and is stated. The block rests on reading (a) and both footprints. Bottom side and left footprint give reproduced, and the notes say so. Reasonable. |
| 15 claims on Figs. 3 to 7 | blocked (other) | Yes | Cell 8 confirms the data are in 000548, 000549, 000550 and 000448, and the claims file names none of them. I cannot check protocol.md's definition of data_missing ("not public anywhere"), but "other" is consistent with it. |
| fig1e-heating | blocked (data_missing) | Yes | None. |

## 2. Statements the printed numbers do not fully support

- **Cell 27 and the record notes for fig2c-max:** "At every ROI of the range it fails (largest p 0.79 against unipolar, 0.072 against 25 and 100%)". These are the 50% values only. For 75% the largest p is 0.996 against unipolar and 0.249 against 25 and 100% (cell 26). The conclusion is the same, but the sentence reads as covering both amplitudes.
- **Summary (cell 37) and the record notes for fig4ac:** "polynomial fits cross zero" / "polynomial fits that cross zero". This holds only at the 7 kV/cm cutoff (ratio minimum −457.4%). At 8 kV/cm the polynomial ratio runs from 34.8 to 1537.4% with no sign change (cell 35). No outcome rests on it.
- **Cell 7 (outside the Result/Summary scope):** "a variant keeps it as the dandiset presents it" is stale. No such variant exists in `T` (cell 12), and the record says it was replaced.
- **Cell 0 (minor):** the status table marks fig2c-weaker-at-6-7 "tested", while its outcome is blocked.

Every other sentence of the Result conclusions (cells 18, 21, 24, 27, 30, 33), the Summary, the README and the record notes matches the printed outputs. I checked:
- the p-values, the ratio ranges 0.50 to 0.75 and 0.68 to 1.04, and the 2 of 12 and 10 of 12 counts
- 54.5%, 31.6% at 14.24 kV/cm, 52.9%, and 1 of 36 tests below 0.01
- 89.6 to 229.9% (100% is above unipolar at 7 of 9 ROI)
- 570.4 to 47.7 a.u., −8.6 ± 19.6, 14.8 ± 3.3, 7.9 ± 3.0, and both denominators below 3% of 571.1
- 34.4 to 64.9%, and "15 claims" in the README (2 + 4 + 2 + 4 + 3)

**My round-1 reasons in the record.** The `verifications` entry gives them faithfully, close to my own wording, with problems 1 and 4 to 7 and 9 folded into the matching claims. Round-1 problem 2 (the 0-03 exclusion leaving unipolar at n = 2, plus the invalid "with 0-03" variant) appears in no claim's reason. The response to it is only in `inputs` and `findings`. Problem 11 (dates confounding amplitude) is likewise unattributed, but it affects no conclusion.

## 3. Round-1 points

**Resolved:**
- 1: the sibling dandisets are named, and the blocked notes say where each claim's data are.
- 3: fig2b is now not_reproduced under the criterion as written.
- 4: p is printed at every ROI, and four placements of the test are run and stated.
- 5: the denominator is flagged, the per-dish unipolar values are printed, and the claim is blocked.
- 6: reading (a) is adopted as a stated assumption, (b) is shown for top and bottom, and the outcomes are marked assumed.
- 7: a variant with the field scaled to 15.1 kV/cm at the centre is added.
- 9: the ROI extent is stated and the weakest ROI is varied.
- 10 and 11: the dates confound is reported as a finding.
- From my "could not check" list: the per-ROI p-values, the one-side unipolar values, and the cell types in 000448 (5 unipolar and 4 bipolar cells).

**Partly resolved: problem 2.** The invalid variant has been removed. Cell 8 shows that 000548 `sub-Fig3-Uni5-03` has the same MemBrite channel as 000489's dish 0-03 and a YP channel that registers with it (peak 0.301). In other words, it holds the missing image. It was not measured, for two reasons:
- it is outside this dandiset;
- the automatic footprint finder fails on it (electrodes found 3.81 mm apart, diameters 1.97 and 0.71 mm).

**What remains that bears on a conclusion:**
- **Unipolar n = 2.** It is the denominator of all three Fig. 2C claims, one of the two failing amplitudes of fig2a, and the cause of the fig2c-weaker block, whose unipolar s.e.m. comes from 2 dishes. The third dish is known to exist. The obstacle is the footprint finder, not the data; whether reading it is in scope is a protocol question. Until it is measured, these outcomes rest on 2 unipolar dishes.
- **Where the p < 0.01 of fig2c-max is tested.** This is now stated, but it remains a judgement: one of the four readings gives partially_reproduced.
- **Image units for fig2a-vertical-scales.** This is still unverifiable, though the assumption is stated.
