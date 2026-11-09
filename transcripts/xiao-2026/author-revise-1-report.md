I went through all of the round-1 points, re-ran the entry twice (`tools/entry.py all` passes, about 34 minutes per run, and the numbers match between the two runs), and recorded the round under `verifications`. `tools/entry.py check` reports 0 errors. Nothing is committed.

**Outcome changes (3).** I followed the verifier on three claims whose criteria have no partial rule. Other criteria in the claims file do give one, so a failed condition here means not reproduced. All three move from partially reproduced to not reproduced:
- **fig2-distance-tuned-counts:** the "both" count is 92 against 29 ± 2.9.
- **figs4ef-crossvalidated-stability:** the Spearman reading fails. The notes now say the failure is narrow, because the ranges over the 100 splits overlap.
- **figs5de-svm-robust:** the combined group is 61.87% against 54.43 ± 5.44. The ranking the claim describes still holds.

**Added or corrected:**
- **SNR and duplicates (B3, C6):** the helper now computes an approximate SNR from the raw voltage and applies the Methods' duplicate-unit rule (9 pairs found). SNR ≥ 5 leaves 1,034 units (1,030 with duplicates dropped), still within 1141 ± 114, so si-unit-yield stays reproduced. The analysed population is still the 1,160 units. Of the 18 units I call responsive but the deposit does not, 12 have SNR below 5, which suggests the deposit's labels already apply an SNR cut.
- **Depth orientation (B5, C1):** the electrodes table says site 1 is the tip, and site 1 has `rel_y` 0. So depth is measured from the tip as assumed, and figs4j stays reproduced.
- **Pass-set variants (B4, B6):** I ran the 1-mm-step sessions the deposit's way (one distance per bin, the one nearest the bin centre, which matches its stored curves exactly). I also ran a version without the post-cut trials in the two cutting sessions. Both change the Figure 2 counts by at most 3 units.
- **Model output (B7, C3):** the four printed lines are now labelled. The 593 and 631 are the nine-bin counts the criterion names. The 99-point fine grid gives exactly the paper's 590 and 636. Both meet the criterion.
- **Cutting claims (B10, C4):** I ran them without the six sessions noted unstable, and with a waveform-stability proxy at two thresholds. The baseline result depends on the threshold (p from 0.0141 to 0.29), while the drop in wall firing holds on every subset. Since the outcome turns on a selection the paper does not define, the three claims stay blocked, with all the subset results in the notes.
- **Post-cut distances (C2):** `wall_pass_epochs` holds only start and stop times, and the digital line carries only the camera and pass signals. Distances are re-shuffled in each block of 10 passes, so the post-cut distances can't be inferred from the pre-cut order. These claims stay blocked.
- **The paper's 6.36 sp/s baseline (C5):** I tried seven other baselines. Only the 0–3 s window at the preferred distance falls within tolerance, and it is not a reading the criterion names. The claim stays partially reproduced.
- **Question for a reader (B2):** I added one to `questions/001687.yaml`, asking whether fig2-distance-tuned-counts should allow for the Figure 2F values (591 tuned, 94 both). The claim itself is unchanged.
- I also updated the conclusions, the summary, the header, the README and three findings to match the new numbers.

**Not done:**
- **B1:** no new question. The checks-log entry the verifier cites was superseded by the reader's answer of 2026-11-03, already recorded in `questions/001687.yaml`.
- **Lab notebook:** I did not consult the brainstem.org lab notebook the dandiset names. The protocol takes outside data only when the claims file says the paper relies on it.
- **Untracked files:** dotfiles such as `.bashrc` and `.idea` and a `scripts` folder appear as untracked in the checkout. I did not create them and left them alone.
