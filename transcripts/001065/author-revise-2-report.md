Round 2 revision is done. No outcome changed and I proposed no changes, so a third round isn't needed. The final run of `python tools/entry.py all entries/001065-dembrow-2024` passed with 0 check errors (notebook ran in 498 s), and every number in the text matches what the notebook prints. Nothing is committed.

**Outcomes:** all 42 stay as verified: 22 reproduced, 7 partially reproduced, 6 not reproduced, 7 blocked. The verifier agreed with every one.

**Corrected or added**
- **fig3a:** the text now gives the printed 42 of 52 and 36 of 46 cultured (it said 38 and 32). I added a run over 10 seeds (random_state 0 to 9): reading (a) ranges from 35 to 45 of 52 and never reaches 52. So the count changes from run to run, but the outcome doesn't.
- **species-no-effect:** statsmodels' table now reads 13 and 2 features, with round 1's figures stated correctly as 11 and 1.
- **Median Spearman:** corrected from 0.952 to the printed 0.957 in all 24 deviation blocks that carried it.
- **figs6b-mcx-higher-rheobase:**
  - The overstated sentence is reworded: the extraction moves the uncorrected p across 0.05 (0.048 on the paper's table values, 0.08 here), and both fail after correction.
  - The pointer to the donor-means cell now says "below", not "above".
- **The single "wash" hit in the blocker search:** it is a real comment, "started washon of synaptic block" at sweep 91, in cell QN23.26.013.4A.05.01.
  - That cell has 13 of its 10 s sweeps before the wash-on and 13 after.
  - A new variant counts the 4 earlier sweeps that have an oscillation frequency as without blockers. The blocker effect is still not significant (p = 0.58 and 0.52).
  - The conclusion, the notes, the summary and the finding about missing drug labels now describe this one file correctly. The other 50 blocker cells mention no blocker or wash.
- **figs7-cv-isi-higher-mcx:** now marked `assumed: true`. A new deviation says the model with the area by bin interaction is assumed, and gives the additive model's p = 0.021 and 0.18.
- **figs7g-modal-rates-long-isis:** the notes now say the outcome rests on both the 200-spike limit and the 1 Hz bins.
- **Summary:** the oscillation bullet now says which claims use cell by 5 mV bins and which use sweeps, and a new bullet lists the round 2 additions.
- **README:** added rows for tcx-et-types-no-difference and figs6b-avg-gain-no-difference.
- **Round 1 record:** the fig7l reason now includes the verifier's point that its r² shortfall rested on the missing spline.
- **Round 2 record:** added under `verifications` for all 42 claims, with the verifier's reasons and my responses.
- **Helper module:** `drug_mentions` in `dembrow.py` now also returns where each hit is and the text around it.

**Not done, and why**
- **cohort-animals:** the species of subject Q19.01.001 can't be settled from the data. Both counts stay reported (9 M. mulatta by the files, 8 by the table), and the disagreement stays recorded as a metadata error.
- **fig7-oscillation-frequency-vm:** no new analysis. The band-edge share and the interior-maximum result the verifier pointed to were already reported. It agreed with the partial outcome.
- **Questions for a reader:** none added, because the verifier reported no place where the claims file misreads the paper.
- **Files I left alone:** `tools/build_site.py` was already modified before this run and the untracked dotfiles weren't created by me.
