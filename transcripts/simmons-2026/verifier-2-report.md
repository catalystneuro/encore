**Round 2 verifier report: simmons-2026-01**

Counts come from the attempt record and the claims file. There are 39 claims and 39 outcomes:
- 13 reproduced
- 2 partially_reproduced
- 4 not_reproduced
- 20 blocked: 16 data_missing, 2 metadata_insufficient, 2 other

Three outcomes are marked `assumed: true`: fig3b, fig4b and fig7d. I still find no place where the claims file misreads the paper.

**1. Outcomes**

I agree with all 39 stated outcomes.

- **Changed since round 1:**
  - fig5d and fig5f are now blocked, metadata_insufficient. I agree. Using the same stand-in controls to decide one claim and not the other would be inconsistent.
  - fig6d is now blocked, other, because its data are elsewhere. I accept that.
  - fig6c stays blocked through its dependency on figs3. The test I asked for is now run (cell 71: P = 0.81, 8 cells), and my disagreement is recorded. I accept the block on the author's reading of protocol step 1.5, which I cannot see here. Its own SNr data would give "reproduced".
- **fig3b (assumed).** The P < 0.05 part holds only at threshold 6 or 8 with all 49 cells: under reading b of M1, or under both readings once the two failed recordings are removed (cell 40). At threshold 12 no paired test with all 49 cells is significant. The record states this only indirectly ("its significance depends on the reading and the threshold"). It is a reasonable assumption, but it should be named as the assumption.
- **fig4b (assumed).** The record says "The absence rests on the detection threshold", and cell 50 says the same. Cell 49 does not support this. Under reading a, P is 0.196, 0.271 and 0.108 at thresholds 6, 8 and 12. M1 says a claim holds under either reading, so the absence holds at every threshold. The flag is not needed, or the assumption should be stated as discarding the threshold-12 reading-b result (P = 0.036), which comes from missed spikes in 6887-57.
- **fig7d (assumed).** This is stated clearly and is reasonable, but fragile. It holds under reading b at thresholds 8 and 12 (P = 0.029 and 0.028) and fails at threshold 6 (P = 0.057).

**2. Text against the printed outputs**

- **Cell 78 and the fig7d record notes:** "Under reading a the increase is 25.2% and 24.5%, inside the tolerance". Cell 77 prints 25.16% and 24.51%. The tolerance is 28 ± 2.8, which is 25.2 to 30.8, so both values are outside it. This does not change the outcome, since P = 0.057 there anyway.
- **Cell 41 and the fig3b record notes:** "The effect is present at about a third to a half of the paper's size under every reading and set of cells". Under reading a of M1 at threshold 8 with all 49 cells, cell 40 gives 6.3%, 4.9% and 8.8%. That is a fifth to a third of 25%, and at threshold 12 it falls to 1.6%.
- **fig3b record notes:** "The gap-free cells measured in the windows their notes give: +9.1%, P = 0.065". That variant covers all 49 cells, with only the gap-free files windowed (cell 40). The gap-free cells on their own give P = 0.20.
- **Cell 82, and the fig7f-snap5114-decreases-rate deviation ("10 of the 19 cells are gap-free recordings"):** cells 7 and 9 show 14 gap-free cells and 5 episodic.
- **Cell 51:** "(ii) the 32 recorded with the same episodic protocol". Cells 40 and 52 print 31.
- **Cell 45:** "clean sweeps stay under about 35 and action currents exceed 75". The histogram in cell 46 shows 3 sweeps between 35 and 50 and one CNO sweep between 50 and 75. Cell 47's wording ("under 50 … mostly over 100") is correct.
- **Cell 32 and the fig2c record notes:** the per-sweep variant is given as "P = 0.15" ("the same at thresholds 6 and 12"). At threshold 6 cell 31 gives 0.109. This is minor.
- **README:** "Sixteen claims on data not in the dataset". One of the sixteen, fig6c, has its own SNr data in the dataset and is blocked only through its dependency. The attempt record's finding states this correctly.
- **fig7e response in the verification record:** "8797-2025-03-12-123, stops firing 6 min into CNO". Cell 17 shows it recovering to 12.2 Hz, with amplitude 24 noise units, by minute 26. This is minor, and the outcome is unchanged with or without the cell.

Everything else checks against the outputs. That covers the remaining Result conclusions, the Summary (including "the same outcome" without the failed recordings, and "three outcomes" marked assumed), the rest of the README and the other record notes.

The verification record gives my round-1 reasons faithfully for all 39 claims. They are close to my wording, with the relevant problem text attached, and the two disagreements (fig5d, fig6c) are marked `agrees: false` correctly.

**3. Round-1 points**

Resolved:
- 1: fig6c's test is run.
- 3: fig2c is run under reading b of M1. The best one-sided P is 0.039, and no two-sided test reaches 0.05.
- 4: fig4a is measured on clean sweeps (P = 0.11, reduction 46 to 55%), with the sign taken from the clean control sweeps.
- 5: fig5d and fig5f are blocked.
- 6: fig5g's power is computed (0.25 with 3 cells).
- 8: the gap-free files are printed by cell, with gaps of 5 to 80 s between files and the notes of each cell.
- 9: file 0023 holds 225 pA, so it was not recorded in gabazine.
- 10: needed no change.
- 2: mostly resolved. Every cell's rate is printed at all three thresholds, the seven failed recordings get time courses, and each affected claim is rerun without them.

Remaining:
- **Point 2, 8979-2025-05-27-164.** This was on my round-1 list. It is not caught by the quarter rule (14.3 to 3.75 Hz is 26%) and has no time course. Its rate in SNAP-5114 drops to 0.17 Hz at threshold 12 (cell 16), the same sign of failing detection as the flagged cells. It sits in both fig7f claims. It is unlikely to change either outcome, because the occlusion test is Welch's with P ≥ 0.61, but it is not checked.
- **Point 7, drug application time (minor).** The time is still taken as the start of the drug's file. For 8945-2025-04-16-144 the notes say gabazine was applied in file 001, which the analysis uses as the control file. So its control under reading a includes gabazine episodes, and its reading-b drug window is misdated. That is one of 49 cells and does not bear on fig3b's outcome.
- **Text corrections.** The fig7d tolerance statement, the "every reading" sentence for fig3b, the gap-free count in fig7f, and the fig4b assumption wording all need fixing. None of them changes an outcome.
