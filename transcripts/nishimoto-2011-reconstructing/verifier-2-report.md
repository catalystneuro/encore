**Verifier report, round 2: Nishimoto et al. 2011 on CRCNS vim-2**

The claims file has 10 claims and the attempt record has 10 outcomes: 6 reproduced, 1 partially reproduced, 3 blocked (data_missing). Notebook 1 is `reproduce_nishimoto_2011.ipynb` (NB1); notebook 2 is `color_no_gain.ipynb` (NB2).

### 1. Outcomes and assumptions

| Claim | Record | I agree? | Assumption stated and reasonable? |
|---|---|---|---|
| fig2de-prediction-accuracy | reproduced | **Yes.** NB1 cell 13, penalty (b), signal (a): 0.233 / 0.384 / 0.386, all within tolerance, in the right order, p = 0 and 1.3e-22. Penalty reading (b) is one of the claims file's own readings, so "under one reading" is met. Under (a), static is 0.211 (−0.0049 from the bound), which the record states. | Yes. Ridge in place of L1 is stated with its basis, and the failed L1 attempt is disclosed. Reasonable, but untested (see §3). |
| fig2e-directional-gain-small | reproduced | **Yes.** Cell 16: ratio 0.012–0.021 and p ≤ 5.3e-22 under all 12 combinations. Not in the conclusion: S1 alone gives a difference of 0.0003, p = 2.5e-3 (cell 13). The pooled criterion doesn't require a per-subject test. | Yes (ridge). |
| figs1a-motion-better-every-area | reproduced | **Yes.** Cell 19: 15 of 15 cells; pooled rank-sum p < 1e-4 in 3 of 3 subjects for every model and both sidednesses. | Yes (ridge). |
| fig2fgh-retinotopic-receptive-fields | reproduced (proxy) | **Yes.** Cell 23: 95–97% of fits inside the display; contralateral 0.84–0.91; r = 0.330–0.607, p ≤ 2.9e-27; passes under both p-value readings. | Yes. The probe contrast and duration, the isotropic Gaussian and the MT-based anterior direction are all stated. The 84–91% contralateral fractions also confirm left/right orientation independently. |
| fig2j-speed-eccentricity | reproduced | **Yes.** Cell 26: 9 of 9 positive with p < 1e-4 under all four reading combinations. | Yes. |
| fig3ab-identification-s1 | partially_reproduced | **Yes, provisionally.** Cell 29: 409 of 486, and no Tikhonov penalty reaches 418. However, only encoding-penalty reading (a) was run. Reading (b) is the one that made fig2de pass, and the claims file's readings apply here too, so the outcome is not settled across readings (§3). | Ridge and the Tikhonov scaling are stated and reasonable. |
| fig3c, fig4, fig4d | blocked, data_missing | **Yes.** | n/a |
| discussion-color-no-gain | reproduced | **Yes, by the criterion.** NB2 cell 6: −0.0095 pooled, one-sided p = 1.0, lower in every subject. | Stated (the claims file's color reading plus ridge). The criterion's "not higher" test is passed by any handicapped model, and here 78,660 regressors share one ridge penalty per voxel. That makes it a weak test of absence (§3). |

### 2. Sentences the printed outputs do not support

- **Record, figs1a notes:** "the exceptions are V1 against V3A (directional …) and V1 against V2 in S2 (8.2e-06 one-sided, 1.6e-05 two-sided)."
  - NB1 cell 19 shows S2 V1 vs V2 at 8e-06, which passes p < 1e-4, so it is not an exception. S2 is the one subject where the directional model passes.
  - The actual nondirectional failure, S3 V1 vs V3A (p = 1.2e-02), is left out.
  - Cell 20 states this correctly; the record does not.
- **NB1 cell 21:** "(b) the 750 held-out training samples." Cell 6 prints "held-out samples 728 of 7128", and the record says 728.
- **Record, fig3ab notes:** "The count moves with the held-out split: the first round, with a split drawn per subject, gave 424."
  - No output compares the two splits.
  - The ridge grid also changed between rounds: 10–1e7 in round 1, 1–1e9 now (cell 1).
  - So the change from 424 to 409 cannot be put down to the split alone.
- **Record, verification response to discussion-color:** "about 46 minutes." NB2 cell 6 prints "total run time 42.4 min".
- **Record findings, and NB1 cell 33 (Summary):** "V4, MT, MTp, FFA, PPA, IP, OBJ, RSC, STS, VO …" (record) and "V1 to V4 … MT and others" (cell 33).
  - No printed output lists these masks. Cell 11 prints only the V1–V3B counts, and cell 23 shows only that MT exists.
  - The claim that the masks are "different per subject" is likewise not shown.
- **Minor, record fig2de deviation:** the log offset of 1e-5 (range −11.51 = log 1e-5, cell 4) is the claims file's log(x) reading, not its standard log(1+x). The record does not name it as a reading choice.

Everything else checks against the printed outputs:
- The other "Result:" cells (NB1 cells 14, 17, 20, 24, 27, 30; NB2 cell 7).
- Both Summary cells (NB1 cell 33, NB2 cell 8).
- The README.
- The record's other notes and findings: onset means 0.42/0.41/0.28; s.d. values; delays 0.06–0.09 / 0.30–0.33 / 0.13–0.15; counts 179/46/29; 4,275 features; 855 zero-spatial-frequency filters; 30–248 voxels at the lowest penalty; rv within 0.003; the 313–409 range.

**My round-1 reasons in the record:** stated faithfully, mostly close to my wording, and each claim's reason carries the problems that applied to it.

### 3. Round-1 points

**Resolved:**
- Problem 2 (fig2fgh, fig2j and discussion-color are now all run).
- Problem 3 (filter table printed; zero-spatial-frequency filters kept single; 4,275 features).
- Problem 4 (one- and two-sided tests both given, with the same counts).
- Problem 6 (rv check printed).
- Problem 7 (upright frames shown in cell 3; contralateral results confirm left/right).
- Tikhonov grid (quarter decades; the peak at 3.162 is a broad maximum).
- pymoten bank (counts printed).

**Addressed, no bearing on a conclusion:**
- Problem 5: the grid was widened, but 30–248 voxels still sit at penalty 1.
- Problem 8: blocks still cross run boundaries, but no test data leaks into any selection.

**Remaining, and bearing on a conclusion:**
1. **Ridge vs L1 (problem 1), not resolved.** No L1 fit is shown, even on a voxel subsample. fig2de passes only under penalty reading (b), with the static mean 0.017 above its bound, and under (a) it would be partial. Its "reproduced" therefore rests on ridge plus reading (b). The disclosure is adequate, but the sensitivity is unknown.
2. **fig3ab not run under encoding-penalty reading (b).** The criterion says "reproduced under one reading", and reading (b) raised directional accuracy from 0.373 to 0.386. The partially_reproduced outcome is therefore not established until identification is run with the (b) fits. It is 9 volumes short of the threshold under (a).
3. **discussion-color.** One shared ridge penalty across three channels of 26,220 regressors each handicaps the color model, so "not higher" may reflect the fit rather than an absence of color information. A fit with a separate penalty per channel (banded ridge) would make the test meaningful. The fit also used penalty reading (a) only.
4. **Wrong figs1a exception sentence in the record** (§2). It doesn't change the outcome, but it misstates which tests fail.

The claims file: I found no new misreading of the paper.
