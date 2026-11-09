I checked the claims file for DANDI:000462 against the paper and the file is ready for an attempt (`ready: true`).

**Checker:** `claims/000462/10.1038-s41467-022-34465-5.yaml: 41 claims, 41 quotes, 111 statistical values, 0 problems`, both before and after my edits.

Statements, quotes, sources, statistics, expected values and tolerances all match the paper. Every change below is to a criterion.

**Changes, by claim**
- **lick-persistence-ur:** the paper contradicts itself. The Results say 4 of 12 mice licked randomly in later laps, but the Methods say only one animal pre-licked after the lick stop. The criterion used the Methods' own definition, which would give 1, not 4. I named the contradiction and listed three readings of "randomly licked".
- **fig1e-decoder-follows-licking:** the 3-lap window for the lick minimum was the earlier reader's own choice; it is now marked "fixed here".
- **supp4-lickstop-definition-robust:** the criterion started RE low at the first of the N no-lick laps, but the legend uses the 2nd. All three start readings are now run. The grouping by presence of licks, which the Methods also call unaffected, is now judged too.
- **fig2e-place-field-fates, reward-zone-field-turnover:** the definitions of "stable" and "remapped" (F1 to F3) are not in the paper; the earlier reader made them up. They now follow the rule for open method details: all three must agree, or the claim is blocked. I changed the opening comment to match.
- **fig3d-reward-overrepresentation:** the criterion only required RE low to be at or below R, which does not show the over-representation disappeared. It now also requires the RE low mean to be at or below 0, marked "fixed here".
- **fig4f-dreadd-spatial-correlation:** the per-position test compared each pair with saline, which goes against the Figure 4g legend, and required an absence the paper never states. It now uses the legend's comparison (R/RE low against each pair).
- **fig4h-dreadd-reliability-outin:** "saline changes by no more than 0.02" was the earlier reader's bound. It is replaced by the legend's paired t-test, run in both ways the legend allows. The 14-of-16 count is marked "fixed here".
- **supp15-tdtomato-controls:** the same 0.02 bound is replaced by the Supplementary Fig. 15f t-test. Panel 15g (reward over-representation), which the statement covers, is now shown.
- **fig5-da-axon-ramps:** the criterion cited Figure 5d for an end-versus-start test within R, which that legend does not contain. The legend's test (R against RE high and RE low at each position) is now the one judged. The check that R ramps is marked "fixed here".
- **fig5l-ramps-return-rr:** added three things:
  - the Methods' rule that samples of 5 or fewer get a non-parametric test, as a variant;
  - the conflict between Supplementary Fig. 19c (1.01) and the text (1.23);
  - a note that the early-versus-late RR comparison is shown, not judged.
- **supp14-reward-cells:** the statement says reward cells do not explain the over-representation, but nothing tested it. Added the Supplementary Fig. 14b paired t-test.
- **supp11-all-mice-parameters, controls-no-change-over-time:** the counts of medians within tolerance are marked "fixed here". The control session length is given as 20 min in the Methods and 15 min in Supplementary Figs. 2 and 10; that is noted.
- **supp16-dreadd-running-speed:** "CIs over laps pooled" and the unpaired t-test were stated as facts. The legend does not say so, so they are now readings, with per-mouse means as a second reading.

**What remains open**
- The start, middle and end position groups in Figs. 1g, 2d and 3c are taken from the Figure 5d legend. The grey bars that define them are only in the figures, and there is no main-article PDF under `paper/` to read them from.
- Several thresholds for findings the paper states only in words are still the earlier reader's own (fig1d, fig2a, supp18, supp20, supp21). Each is labelled "fixed here".
- Supplementary Fig. 9 (the spatial correlation drop across all mice, 1024 place cells) has no claim of its own. It is a robustness check of fig2c, so I did not add one.

All main findings have claims, and every claim comes from this paper. Nothing was committed.
