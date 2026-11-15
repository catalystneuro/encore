**Verifier report, round 2: martinez-conde-2019-02**

**1. Outcomes**

The claims file has 19 claims and the attempt record has 19 outcomes: 9 reproduced, 3 partially reproduced, 4 not reproduced and 3 blocked.

| Claim | Agree | Assumption (`assumed: true`) stated and reasonable? |
|---|---|---|
| neuron-counts | yes, not_reproduced | no assumption |
| spikes-per-condition | yes, blocked (data_missing) | not applicable |
| s4-baseline-no-difference | yes, not_reproduced | Stated. Reasonable, but the outcome depends on it. The files' own BaseActivity finds no difference (cell 16, smallest p = 0.11), and so do Corners readings (b) and (c). The record says this. |
| fig4a-above-baseline | yes | Stated and reasonable. Reading (a) is ordered under every variant (cell 19). |
| fig4b-spike-rate-difference | yes | Stated and reasonable. S90 is inside its tolerance by 0.02. Every other variant gives 3 of 4 except Corners (c), which gives 4 of 4 (cell 22). |
| fig4b-pairwise-significance | yes | Stated and reasonable. Holds under every variant (cell 25). |
| fig5-average-maps | yes | Stated and reasonable. As the criterion says, this is not independent of fig4b. |
| table1-edge, table1-p180, table1-s90 | yes, partially_reproduced (4 of 5 each) | Stated and reasonable |
| table1-s52 | yes, reproduced, as the rule says ("under one reading, all five"; cell 31, iia, 5 of 5) | Stated. The result is fragile: it rests on one of four readings, a maximum inside its tolerance by 0.05, n = 12 against 30, and a change of measure made after round 1. The record says all of this. |
| table1-s40 | yes, reproduced (5 of 5) | Stated and reasonable |
| fig6-midpoint-representative | yes, reproduced (0 of 10 and 0 of 4 tests significant) | Stated and reasonable |
| fig7a-rms-contrast-fit | yes, not_reproduced | no assumption. The cause, the paper's definition of RMS contrast (its reference 21), is still unknown. |
| fig7c-fold-edge-equivalence | yes, not_reproduced, borderline | Stated. The distance reading of "within one step of 90%" is the more literal one. Under the level reading it would pass. Cell 40 prints both. |
| fig7c-fold-edge-significance | yes, reproduced (all corrections; largest p = 0.044, cell 43) | Stated and reasonable |
| fig7d-nonlinear | yes, reproduced | Stated and reasonable |
| fig7d-dog-similar, s3-latency-peak | yes, blocked (data_missing) | not applicable |

**2. Text against the printed outputs**

Most sentences match the numbers. These do not, or have no output behind them:

- **Cell 6 and the spikes-per-condition notes:** "smoothed_image_norm … minus BaseActivity (in 5 of 38 files) or that divided by its maximum (21), or neither (11)". 5 + 21 + 11 = 37, not 38, and nothing explains the missing file.
- **Cell 17:** "the check above shows that the files' BaseActivity keeps such pixels". Cell 6 only shows better agreement. For the Star it is clear (r 0.953 against 0.809), but for Corners r is nearly the same (0.859 against 0.850). The Summary's "appears to keep them" is the supported wording.
- **Statements with no printed output behind them:**
  - "the descriptor says 53" (cell 9 and the neuron-counts notes).
  - "offsets of up to about 370 DU" (finding; reg_offset is never printed).
  - "all 75 version 5 files" (finding; the version is not printed).
  - "BaseActivity … was not reproduced by any placement … tried while preparing (not run here)" (cell 4, repeated in a finding).
- **Baseline deviation (every outcome):** it cites "median absolute difference 0.72" (cell 14, n = 19) next to "0.75 against 1.21" (cell 6, n = 17) without saying the two are from different subsets.
- **fig7a notes and cell 38:** reading (b) "fits well (R2 = 0.9994)". Its parameters (a = −87.3, b = 0.0001, c = 87.3, cell 37) are as degenerate as reading (a)'s. It is a near-linear fit, not an exponential.
- **fig7c notes and cell 41:** "rise from 9.01 … to 20.80". The rise is not monotonic: at 30% it is 16.28 against 15.69 at 40%, and at 0.869 it is 15.99 against 15.58 at 0.906 (cell 40).
- **README:** fig7c "would be on another [reading of one step]". This holds only under contrast reading (b); under (a) P180 fails either way.
- **Cell 35** leaves out one significant signed rank result under reading (ii): S90 against the median, p = 0.0115. It is a variant only and changes no conclusion.

None of these changes an outcome.

The attempt record states my round-1 reasons faithfully. They are close to my own wording, and my Problems (B) points are merged into the claims they bear on. B6 is kept with its label "not affecting a conclusion". My claims-file point B9b (the checks block still lists Corners S40 averaging as open) is not recorded. It concerns the claims file, not the attempt.

**3. Round-1 points**

Resolved:
- **B1, as far as the data allow:** cell 6 shows the Star stimulus at one orientation (modulo its 30 degree symmetry) and no detectable difference between the 12 registered and 15 unregistered neurons (p 0.41 to 0.63).
- **B3, as a stated choice:** the eye time map cannot show coverage, and the BaseActivity comparison is printed.
- **B4:** gray range, the zero background and example windows are printed.
- **B5:** the level variant is printed and the garbled sentence is fixed.
- **B6:** squares are now area-weighted.
- **B7, B8:** done.
- **B9a, B9c:** recorded as a reader question and a finding.
- **All of section C:** fields, eye time, Star stimulus and the 12/15 comparison, fig7a values, Star luminance (l50 48.2 to 50.4) and the S40 fold length (100 DU).

Remaining points that bear on a conclusion:
- **Baseline placement, chosen after the results were seen:** it decides s4, the Table 1 counts (Edge, P180 and S90 drop to 1 or 2 of 5, S52 to 1, S40 to 1 under variants), fig4b S90 (inside by 0.02) and fig7c. It is stated, but the data cannot resolve it.
- **table1-s52:** reproduced only under reading (ii)(a), by 0.05 on one value, on 12 of 30 neurons, after the change of measure prompted by B6.
- **fig7c-fold-edge-equivalence:** the outcome turns on the reading of "one step" (a 0.6 miss under the distance reading).
- **fig7a:** the definition of RMS contrast (reference 21) and the luminance scale are still unknown, so the failure cannot be told apart from a difference of method.
- **Star n = 12 of 30:** this limits every S52 result.
