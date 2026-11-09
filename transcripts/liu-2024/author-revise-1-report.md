No outcome changed in round 2. The verifier agreed with all 24 outcomes, so I kept every one, answered each point in the report, and recorded the round under `verifications` in `attempts/001097-liu-2024-01.yaml`. `python tools/entry.py all entries/001097-liu-2024` passes, and the notebook runs in 396 s. I checked every conclusion, the summary and the attempt notes against the new numbers. Nothing is committed.

**Bug fixed (verifier Problem 10).** The behaviour raster marked one frame too many after each annotation. It now ends at the annotation's stop. An assertion in the data-check cell fails on the old code. The fix moved some numbers, but no outcome:
- fig1g is now 63.3% in bouts and 21.8% in intervals, both still within tolerance.
- fig2c is now 6.9% to 37.4% of cells tuned, median 22.0%. Eleven behaviours are analysed instead of 12, because "turn" dropped below the bin threshold.
- Resistance-curve and GLM values shifted slightly.

**Outputs the verifier asked for:**
- **Weight cell order (ed6e, ed7):** the weights line up with the session files. 171 of 176 cells (m541) and 71 of 72 (mouse 543) best match the session cell with the same index.
  - The per-mouse traces were processed differently: cell i correlates with cell i at 0.86 and 0.80, and the correlation rises when the session traces are smoothed.
  - The factor projections from the two sets of traces still correlate at 0.94 to 0.96, and the same factor is chosen either way.
- **Per-mouse file contents:** they hold only the two weight columns, one trace series and the annotations. There are no latent time series or dynamics matrices, so fig5c and fig3c stay blocked.
- **GLM (fig2e, fig2f):** a model with only an intercept scores -0.086 under the same folds, so the negative values come from the fold design. Behaviour adds 0.009, 0.073 and 0.029 over that baseline, still below the paper's 0.08, 0.14 and 0.15. R² within single folds is also included. fig2e stays not reproduced, and the notes now say it is a weak test. fig2f stays reproduced, noted as sharing that fold design.
- **Choice probability by pairs of behaviours (fig2c):** this is how the Methods describe it, and it tunes more cells, not fewer: median 39.3%, and none of the 20 pairs falls within 1 to 15%.
- **Trace types:** a per-experiment table confirms the verifier's inference. Receptive, primed and male-inhibition files are raw; the natural-cycle, ovariectomy and oestrogen series are z-scored.
- **fig1b trial counts:** counts per bin are now printed for both trial sets. Two checks were added:
  - With the same 63 trials in each of the first 15 bins, accepting behaviour still rises (Spearman 0.63, p = 0.012).
  - Within single trials it does not rise (33 of 58 positive, p = 0.36).
- **Duplicates:** the check now covers the 7-day series and prints the evidence for each pair.
  - None of the 7-day sessions of m928, m930 or m940 duplicates their receptive session.
  - m438 natural-cycle day 1 stays marked as a duplicate. Its frames and interaction length match the receptive session, and its trace match is 0.78 against 0.33 and 0.44 for its other days.
  - Three recordings with identical traces also have different annotations, so differing annotation counts do not rule out a duplicate.
- **Clock check:** two oestrogen sessions fail it (m928 day 2 and m940 day 7). The notebook now says so, and ed10c holds without them (r² at most 0.025).
- **fig2i:** added a window that ends at the last annotation (15.5 to 19.7%). Still not reproduced.
- **ed3b (pencil cup):** exploratory only. In the unannotated tail after the last annotation, the shorter ACHW goes away against a stretch of the interaction of the same length (the tail is longer in 5 of 7 sessions). Still blocked.
- **ed4b (single-cell ramps):** exploratory only, with a ramp I chose. 0 of 44 and 1 of 14 weighted cells have r² above 0.5, against the paper's 56%. Still blocked.

**Other corrections.** I updated the finding on recordings filed twice: it now lists five, including day 3 of the ovariectomy series of m438, m541 and m551. I added a finding on how the per-mouse traces were processed, and a note on why the paper's partial-least-squares fallback is not used. The runtime is now listed as 7 minutes.

**Not done:**
- I did not pick 4 mice for fig2i, because the paper does not identify them.
- I did not change how the GLM penalty is chosen. Instead I added the baseline and said the test is weak.
- I did not change the ed7 cell selection, because that circularity is in the paper itself.

The paper text is saved under `paper/`, which git ignores. The untracked dotfiles and `scripts` at the repository root are not mine and should not be committed.
