**Round 2 verifier report: 001710-plitt-2023-01 (doi:10.1101/2023.11.20.567978, DANDI:001710 0.260213.0329)**

Counts below are taken from the claims file and the attempt record. There are 57 claims and 57 outcomes:
- 30 reproduced
- 4 partially_reproduced: fig2ab, vr-reward-location-learning, fig2cd-decoding-improves-over-days, fig3g
- 3 not_reproduced: fig3f, figs8h, fig6d
- 20 blocked: 9 data_missing and 11 methods_underspecified (3 model claims and 8 HSE claims)

## 1. Outcomes

**Unchanged since round 1, and I still agree.** These are all outcomes other than the ones listed below. Each `assumed: true` outcome states its assumption as a deviation, and I find them reasonable:
- dF/F stands in for the deconvolved rates. The `F_dff` line of the authors' code is now printed (cell 13).
- The decoder input follows the authors' code.
- The deposited place-cell masks are used.
- The baseline follows `baseline_avg_act`.
- Block numbers continue across split files; the per-file blocks are printed (cell 8).

**Changed since round 1.**
- **figs3c (now reproduced, resting on per-bin PV reading (b)): I agree.** The assumption is stated, and it rests on the authors' `calc_pv_corr`, printed in cell 13. Two caveats: that code describes a later version of the paper (the attempt's own code_mismatch finding), and the flattened reading gives Cre higher (p=0.018). The like-for-like single-trial variant (p=0.174 and 0.303) supports the absence of a group difference.
- **fig4-block6-activity-increase-pattern (now reproduced with a 150 cm stem): I agree.** The Methods say the stem and arms are of equal length, and the assumption is stated.
- **fig6e (now reproduced on day 1): I agree.** The day-1 choice is justified by Fig 6D/S8F. The pooled interaction (p=0.001) disappears with a random slope per mouse (p=0.585) or per-mouse slopes (p=0.586), which supports my round-1 pseudo-replication concern.
- **fig3i (now reproduced): I accept it, with a reservation.** The outcome counts as reproduced if the claim holds under any reading of which cells are counted, and 3 of 4 readings hold (cell 75). The failing reading (b,b), formation-lap fields over place cells, is arguably closest to the paper's "place cells … had more place fields". Unlike figs3c, fig4 and fig6e, this choice is not recorded as an adopted assumption. All four contested readings were resolved towards reproduction.
- **The 8 HSE claims (now blocked, methods_underspecified): I agree.** The decision rule (cell 139) is applied correctly. In the Cre group, the data with synchrony removed give 0.43 of trials against 0.46 real under reading O, and 0.15 against 0.26 under reading S (cell 140). With planted synchronous events, the synthetic check barely changes the flagged fraction (O: 0.40 → 0.40). The record should state the consequence of the two readings more plainly:
  - Under S (the Methods' words), real minus null still shows Cre higher (p=0.003). If the null were settled as S, figs9a would be not_reproduced.
  - Under O, real minus null gives p=0.61.
  - The notes give both p-values.

  Blocked outcomes need no `assumed` flag.

## 2. Text against printed outputs

These are the sentences the numbers do not support:
- **Cell 47 and the record's notes for fig2cd-decoding-improves-over-days:** "Holm p 0.002 to 2e-5". The printed values are 0.00183, 0.00485, 1.86e-5 and 0.00485 (cell 46), so the range is 2e-5 to 0.005.
- **Cell 67 and the record's notes for fig3f:** "all days, all candidate fields: 63 against 68 cm". Cell 64 prints 60.985 (Cre) and 67.884 (control) over all fields. The figures 63.4 and 68.4 are the day-6 means (cell 66).
- **Cell 99 and the record's notes for figs6b:** "The variants give p=0.95 and 0.55". Cell 98 prints v1 p=0.964 and v2 p=0.536.
- **The record's notes for figs6b:** "the group means and the test are unchanged to the printed precision". No before/after comparison is printed, so the notebook does not support this.
- **Cell 165, Summary table, HSE row:** "flags as many trials when synchrony is removed". Under S the figures are 0.15 against 0.26 (Cre) and 0.003 against 0.021 (control) (cell 140). The Summary's own bullet ("more than half as many") is correct.
- **README:** "The imaging outcomes rest on one assumption." figs3c, fig4-block6 and fig6e also rest on adopted readings, and the record marks them as assumptions.
- **The record's notes on all 8 HSE claims:** "the two null readings give 3.2 and 36 HSEs per control day". These are real-data counts under detector readings S and O (cell 138), not counts from the synchrony-removed data, which gives 0.43 and 30 (cell 140). The wording invites that misreading.

All other "**Result:**" sentences, the rest of the Summary, the README and the record's notes match the printed outputs.

The record's `reason` fields restate my round-1 reasons faithfully, in substance and nearly word for word. The `agrees` flags match my round-1 table. I could not check `questions/001710.yaml`, which the record cites, because it is not among my materials.

## 3. Round-1 points

**Resolved**
- **Problem 1 (HSE detector).** Validated on synthetic sessions and on real data with synchrony removed; outcome blocked.
- **Problem 2 (reactivation group sizes).** Per-mouse counts are printed, and a ≥10-cell variant is added.
- **Problem 4 (raw COM).** The synthetic check is added; the outcomes now rest on the clipped COM.
- **Problem 5 (speed normalisation).** Reading (ii) is now the main reading.
- **Problem 6 (fig6e pooling).** The random-slope and two-stage fits are added.
- **Problem 7 (split days).** Block numbering was in fact restarting in the second file; it is now continued.
- **Problem 8 (figs3c like for like).** The single-trial variant is added.
- **Problem 9 (100 cm stem chance).** Added.
- **Section C:** code lines printed, HSE null run, place-cell comparison done, block tables and per-mouse reward fronts printed.

**Partly resolved**
- **Problem 3 (place-cell masks).** It is now explained: the masks use a different spatial-information scale and a stricter null. The function that made them is unavailable, and the recomputed masks still flip figs3a novel (p=0.036) and figs7b familiar (p=0.052).

**Remaining points that bear on a conclusion**
1. **dF/F vs deconvolved rates.** Every imaging outcome depends on it, and it cannot be settled without the authors (open question).
2. **HSE null definition (S vs O).** It decides whether figs9a is blocked or not_reproduced, and it gates all 8 HSE claims.
3. **figs3c.** The outcome depends on the PV-correlation reading; the flattened reading gives p=0.018.
4. **fig3i.** It rests on 3 of 4 readings, and the failing one is plausibly the paper's own.
5. **Deposited vs recomputed place cells.** This affects figs3a (novel trials) and figs7b (familiar trials).
6. **vr-reward-location-learning (possible claims-file misreading, reported not corrected).** The criterion requires an increase over days where the paper says licking only "changed". It is still pending with a reader; under the paper's wording the outcome would be reproduced.
7. **fig4e-novel-minus-familiar-larger-control remains fragile.** The v1 and v2 normalisations give p=0.28 and 0.12.

The remaining round-1 points (fig6d sign, the one-sided test for fig7h, the 0.3% frame-rate difference) no longer affect any outcome. fig6d fails under either sign, and the fig7h claim is now blocked.
