I've revised the 001616 attempt for every point in the round-1 report. All four notebooks passed `python tools/entry.py all`, and their outputs match the scratch run the conclusions were written from. Nothing is committed.

**Outcome changes**
- **fig5-faces-presence**: blocked → partially reproduced. I wrote a criterion for a logistic regression stand-in before decoding the labels. One of three conditions holds: Summer Presence is decoded best from the amygdala (0.292). The face labels decode worse than the character labels (Summer Faces 0.217 against Summer 0.301; Tom Faces 0.167 against Tom 0.218). The dandiset doesn't mark the frames the Methods exclude, so those stay in as negatives.
- **fig7a-500-neurons**: blocked → partially reproduced, also with a criterion written before any fit. The top 500 units beat all 2286 units (0.375 against 0.357), but 229 units give the peak (0.394).
- The verifier's own outcome for these two was "blocked", but it listed the block as a problem that affects a conclusion. The checker rejects an outcome change against a round the verifier agreed with, so I recorded both as `agrees: false` and explained why in `response`. Round 2 should look at that judgement.
- The other 18 outcomes are unchanged.

**What I added or fixed**
- **Wilcoxon calibration**: the test is now run at random times with as many events as each label has onsets. It flags 9.5 to 69.2% of units, about as many as at the real onsets (Summer 44.05% at random times against 44.31%).
- **ZETA test from the dataset's code**: it now runs for every unit in two new notebooks, `responsive_zeta_cuts.ipynb` and `responsive_zeta_labels.ipynb`. It is calibrated (no unit flagged at random times at alpha 0.001) but counts far below Table S1: camera cuts 79 against 1025, Summer 11 against 46, Tom 13 against 216. So neither test reproduces the paper's counts. The ZETA variant cell left the main notebook.
- **Helper fixes**: onsets now keep each label's first segment, and the decoding windows at the ends count the spikes just outside the analysis portion. A small check of the onset rule is asserted in the notebook. `requirements.in` now requires scikit-learn 1.8 or later, which the L1 setting needs.
- **Numbers that moved after these fixes**:
  - fig7b overlap: 97 → 95.
  - Camera Cuts kappa: 0.0961, 0.001 inside its tolerance.
  - Scene-cut cluster p: 0.055, or 0.020 with the code's z-scoring.
  - fig6: now three of four conditions hold.
  - Clock check: z above 3 in 11 of 29 patients (was 12).
  
  All conclusions, notes, the summary and the README match the new numbers.
- **New outputs the verifier asked for**:
  - Per-fold permutation p for fig4 and fig5. Six region folds are not above chance, and this is now stated.
  - A per-patient label-shift clock check: the true labels give the higher kappa in 18 of 29 patients.
  - For fig6, the active and inactive split of the non-responsive units. With active units only, the drop is no larger for camera cuts (0.062) than for Summer (0.060).
- **fig7b** moved to the new notebook `top_ranked_units.ipynb`, together with fig7a.
- **Run time**: the main notebook now takes about 25 minutes. `entry.yaml` lists the new notebooks.
- The attempt record has the round-1 `verifications` entry, and the claims file has the two new criteria with a comment on what I had seen when writing them.

**Not done**
- **ZETA with 1000 resamplings for all units**: one notebook doing all of it took 48 minutes, over the 30-minute limit. I split the work and kept 100 resamplings. The 1000 check covers PHC units and scene cuts only: 11 and 31 units against 12 and 29.
- **Subject ids against the paper's patient numbers**: the Figure 4 legend gives no unit counts per patient, and the figure image couldn't be retrieved from eLife. The mapping stays an assumption.

Untracked dotfiles and a `scripts/` directory appeared in the repository root. I didn't create them and left them alone.
