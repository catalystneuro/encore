**Verifier report, round 2: Hernández-Pérez, Cooper & Newman (2020) on CRCNS hc-27**

Counts are taken from the claims file and the attempt record. There are 24 claims. The record has 11 reproduced, 4 partially reproduced, 6 not reproduced and 3 blocked. I agree with 23 of the 24 outcomes.

### 1. Outcomes and assumptions

| Claim | Record | Agree | Note |
|---|---|---|---|
| fig2d-phase-shift-rate | reproduced | yes | Cell 14: 12 of 12 combinations pass. |
| fig2d-linear-fit | reproduced | yes | Cell 18. |
| fig2a-all-rats | reproduced | yes | Cell 21: ventral lags are 16 to 40 ms with the all-channel artefact mask. |
| fig2e-phase-locking-high | reproduced, assumed | yes | The assumption is stated and reasonable. It is fragile: the claim passes only under O3 c, and only at thresholds of 200 to 400 (cells 11, 24). |
| fig2e-phase-locking-decrease | reproduced, assumed | yes | The assumption is stated. The slope is within tolerance under O3 c only at 400 (cell 11). |
| fig2c-coherence | reproduced | yes | Cell 30. |
| fig2f-coherence-decrease | not_reproduced | yes | Cell 33. |
| fig2g-power-no-change | reproduced | yes | Cell 36. |
| fig3, fig4d (two claims) | blocked | yes | Unchanged since round 1, which I confirmed against the archive. |
| fig5c-rise-decay-gradient | partially_reproduced | no | Under the claims file's log10 I still read it as not reproduced: the criterion defines only "reproduced", and both values are far outside tolerance (cell 39: −0.171 and −0.049). The record states my disagreement correctly, and the author's reason ("effect present but weaker", from the protocol) is defensible. The natural-log question has gone to a reader. |
| fig5c-peak-trough-gradient | reproduced | yes | Cell 42. |
| fig5-dorsal-sawtooth | reproduced | yes | Cell 45: p = 0.0625 under all three zero treatments, at the boundary. |
| fig5-ventral-rise-not-peak | reproduced | yes | Cell 48. |
| fig6b-delay-by-phase | partially_reproduced | yes | Cell 51: the rising phase is longer than the peak in 4 of 6 rats. |
| fig6c-delay-phase-slope | partially_reproduced, assumed | yes | The assumption is stated. Under `none` the claim would be not reproduced. |
| fig6b-hilbert-between-limits | reproduced, assumed | yes | The assumption is stated. Under `none` the claim fails. |
| fig7-asymmetry-delay | not_reproduced, assumed | yes | The assumption is stated. The two `none` passes (5.66, 5.69) drop the theta-epoch restriction the Methods require. |
| fig7-residual-delay | not_reproduced | yes | Cell 63: 0 of 24. |
| fig8c, fig8d, fig8-correlation-strength | not_reproduced, assumed (period) | yes | Stated, with the shared-timing caveat. |
| fig8-coupled-oscillators | partially_reproduced, assumed (period) | yes | This is the criterion's "otherwise" case. |

No outcome that lacks `assumed` should have it: fig6b, fig7-residual and fig5c fail under `none` as well.

The claims file uses log10, as the Methods do (they say "log 10" explicitly). The legends say only "log", and the claims file does not list that reading. This is the same point as round 1 and nothing new.

### 2. Sentences the outputs do not support

- **Cell 64, the attempt record (fig7-residual-delay notes) and the Summary (cell 79).** "With half of Delay_Asym removed … the residual is 6.8 to 9.2 ms/mm, within 9.61 +/- 2.62." The tolerance runs from 6.99 to 12.23. Cell 63's variant table gives 6.80 (none/b/b) and 6.81 (none/c/b), which are outside it. The statement holds under `counts` only (7.86 to 9.20). The Summary's "brings … fig7-residual-delay within tolerance" needs the same qualification.
- **Summary (cell 79) and the record's Figure 8 author question.** These say "with a frequency taken from the Hilbert phase the absolute delay falls with frequency, as the paper finds" and "the absolute delay falls with frequency, as the paper reports". Cell 69 shows p = 0.094 under the main reading. Under `counts`, only 1 of 4 combinations has p ≤ 0.0625 (c/b gives median −0.40 with p = 0.69). Four of the five significant combinations are `none`. The median slope is negative under every combination, but the test finds the fall only without the theta-epoch restriction. Cells 71 and 76 state this correctly; the two summary sentences overstate it.
- **Cell 73.** "Under the `counts` readings the test finds the difference under one Hilbert combination (p = 0.031) and no centred one." Under the r² measure, counts/c/b/centred gives T+ = 20, p = 0.0625 (cell 72, row 43). That meets the criterion's level. The code's check demands T+ = 21, which is stricter than the criterion. This does not change the outcome (0 of 64), because the absolute median is 0.005 against 0.14. The record's "(p = 0.156 to 0.438)" is correct for |r|.
- **Cell 60 check, a note on the code.** It requires T_a == 21, which is stricter than "values positive". This does not change the outcome, because 6.07 is outside tolerance in any case.

I checked every other number in the Result cells, the Summary, the README table and text, and the record's notes against the printed outputs, and they match. That includes the sweep ranges, the cycle counts, the per-rat tables, the ln and half-delay variants, the Figure 8 p ranges and the amplitude table.

The record's verification block states my round-1 reasons faithfully, close to my own wording. Problem 3 appears only as a response under fig2d and not in any reason, which is acceptable. The count "agree on 23 of 24" is correct.

### 3. Round-1 points

**Resolved**
- **Problem 5.** The per-rat table is added to cell 51.
- **Problem 6.** Reading b is now the pooled per-cycle median (cell 57), the wrong sentence is removed, and `hc` is removed from cell 57.
- **Problem 7.** Pratt and zsplit both give p = 0.0625 (cell 45), and I checked `signrank_zeros`.
- **Problem 8.** `robustfit_slopes` now freezes rows only after their converging iteration (mectw.py:387). I checked this.
- **Problem 9.** The cycle-triggered average uses the all-channel mask (cell 3), and the dead code is gone.
- **Problem 3.** The channels were matched to the author proof by eye. The paper's legend (green squares for key-recording positions, blue for outside the MEC) supports the reading. I could not view the PDF to check the count.
- **Section C requests.** All are met except the figures: the ln and half-delay tables, the threshold and amplitude tables, the per-rat fig6b table, and the fig8 sensitivity table.

**Addressed by disclosure, but still bearing on conclusions**
- **The `counts` unit reading (problem 2).** Five outcomes rest on it. The sweep (cell 11) shows that the paper's 3500 to 5000 cycles per rat do not single out a threshold. If the integer files are Intan counts, the paper's 400 µV threshold leaves no epochs at all. fig2e-phase-locking-decrease passes only at exactly 400 under O3 c. Only the authors can resolve this.
- **The Figure 8 period definition (problem 4).** Four outcomes rest on it. The sign flips between periods, and the per-rat table (cell 70) shows that the asymmetry correction carries the shared timing. The not_reproduced outcomes are correctly framed as not evidence against the mechanism.
- **fig5c-rise-decay-gradient (problem 1).** Two things remain open: the outcome label (partial or not reproduced), and the reader's decision on the natural log. Under ln, 5 of 12 combinations pass.

**New, small**
- The three overstatements in section 2: the half-delay range under `none`, the Hilbert-frequency "as the paper finds", and "no centred one" in cell 73. None of them changes an outcome.
