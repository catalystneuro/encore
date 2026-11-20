The two answers are applied: the affected claims were re-run, and the notebook, conclusions, README, entry.yaml, helper and attempt record are updated. The entry ran clean (main notebook 26.6 min) and the handover is in `executed/silkuniene-2025/handover/`. **`python tools/entry.py check` did not run:** it crashes with `FileNotFoundError` because it needs `attempts/silkuniene-2025-03.yaml`, the earlier attempt's record, which the blind run removes. That is a problem with the checkout, not with this entry. Checking the record against the schema directly shows no problems in my edits; the only complaints are about fields the reconciliation run added earlier. Nothing is committed.

Outcomes verified in round 2 cannot be changed in this run (the check enforces this), so each change is written under `proposed` for a round 3.

**Question 1 (fig3a-centre-enhanced): which dandiset holds the packet-rate series of Figs. 3 and 4**
- **What it changed:** four claims (fig3a, fig3bc, fig3-lorentzian, fig4b-40-fold) now also list 001276. fig3a and fig3-lorentzian can reach at most partially reproduced, because only two rates are held. I tested all four on the 001276 CT26 wells at 2 bursts (x4): 1 Hz (n = 2), 0.2 MHz (n = 6) and controls (n = 4). For fig3bc I measured the ROIs parallel to the sides from the whole-well images; the helper has a new `parallel_profiles` for this.

| Claim | Earlier | Now |
|---|---|---|
| fig3a-centre-enhanced | blocked (data_missing) | blocked kept; **partially reproduced proposed**. The 0.2-MHz central peak holds in 24 of 24 readings and 1 Hz in 21 of 24, but the control centre is never below 4, 6 and 7 mm. |
| fig3bc-rate-suppresses-off-target | blocked | blocked kept; **reproduced proposed, resting on an assumption**. It holds in 24 of 24 readings with the four half-diagonals pooled (O2 b), and in 40 of 48 with the two diagonals kept apart, where the left side at 7 mm fails because one of the two 1-Hz wells is low there. |
| fig3-lorentzian-profile | blocked | blocked kept; **partially reproduced proposed**. R is 0.946 to 0.997 with p < 0.001 in all 64 readings, but only two rates are held. |
| fig4b-40-fold-ratio | blocked | blocked kept; **reproduced proposed, resting on the background footprint**. 10 of 48 combinations fall in 36 to 44; the first reading the criterion lists gives 39.4. |
| fig3-tail, fig4b-centre, fig4b-near-electrode, fig4c (2 claims) | blocked | blocked, unchanged. The reader kept them on 001047 only, and no dandiset holds the 1-kHz or 10-kHz wells. |

**Question 2 (fig7-offtarget-40-50-fold): which electrode footprint gives the background**
- **What it changed:** the footprint is now an open reading, (i) to (iv), the same position in every well. Every claim whose criterion cites it now has a cell that runs it under each footprint, and each claim's notes say what the answer changed. The darkest footprint, which I used before, is kept as a reference.

| Claim | Earlier | Now |
|---|---|---|
| fig7-offtarget-40-50-fold | reproduced (assumed) | unchanged; the claims file now endorses how it was recorded |
| fig6d-600-900-differ-from-300 | partially reproduced | partially reproduced kept; **blocked (methods_underspecified) proposed**. Footprint (i) gives no significant comparison, (iv) gives both under some readings, and nothing favours one footprint over another. |
| fig7cf-fwhm-with-bursts | reproduced (assumed) | reproduced kept; **blocked (methods_underspecified) proposed**. The CHO slope p falls below 0.05 with footprints (iii) and (iv), and the criterion holds in 14 of 24 readings. |
| fig5-raised, fig5-killing, fig5ab, fig5b-gaussian, fig5b-reversible, fig6c, fig6d-900ns, fig7be, fig7b-saturation, fig7-sharpest, fig7-cho | as before | unchanged under every footprint |
| fig6d-longer-pulses-sharper-peak | reproduced (assumed), not_reproduced proposed | unchanged (p = 0.0003 to 0.0465 with the main wells); its earlier proposal stands |

The two methods_underspecified proposals are judgement calls: a verifier could argue for not_reproduced instead, since both criteria say "under every reading". One more limitation is written in the notebook summary: where an array was located from the YP spot, the footprint ROIs sit on the nominal square and may fall partly outside the real footprint.
