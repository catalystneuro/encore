No outcomes changed. The verifier agreed with all 18 in round 2 (15 blocked for missing data, 3 not reproduced), so nothing goes under `proposed`. The entry re-runs cleanly (`tools/entry.py all`: 0 errors, the notebook passes) and the printed numbers match the previous run.

**What I corrected:**
- **Cell 16 and the fig8b notes:** these said every Protocol 2 dish is highest at the electrode ends. They now name dish 2 as the exception: its other end is below its center, and its normalized center is 105.9% raw and 112.3% with the background subtracted. Cell 16 also now describes dish 11's two spikes (maximum 548.0 a.u. at about -0.2 mm, and a second at about +0.6 mm). Both texts note that every Protocol 3 dish (125.0 to 137.0%) is still above every Protocol 2 dish.
- **fig8b notes, label-swap variant:** the raw triple is now in the same Packet order as the other triple (2, 3, 1): 129.4, 82.8 and 81.3%.
- **Cell 21:** dropped the stale "Reading (b) cannot be run". It now says reading (b) is run below in three ways.
- **Cell 8:** the tile steps now match the printed output. They are 1840 to 1848 pixels or twice that, plus one step of 5736 that is not a multiple of the spacing, and dish 10 has steps of 1632 and 2048. I also corrected the footprint range to the printed 1.6 to 2.0 mm (it said 1.7).
- **Dandiset 000686:** the fig5a-trains-stronger-throughout notes now name it as holding images of the Figure 5 conditions, outside the dataset the claims file names. It has its own registry entry. I reworded the round-1 response on fig6a so it no longer says the notes named 000686 at that point.

**What I added:** the round-2 entry under `verifications` in `attempts/001027-pakhomov-2023-01.yaml`. For each claim it gives the verifier's agreement, its outcome, its reason paraphrased from the report, and my response.

**What I did not do:**
- The verifier found no place where the claims file misreads the paper, so I added no question to `questions/001027.yaml`.
- Three open items cannot be settled from this dataset, and the verifier agreed they are correctly recorded as unresolved: which electrode is e1, the gain and exposure of each imaging day, and whether the Protocol 2/3 labels or the paper's figure are swapped.
- Nothing is committed, as instructed. The untracked dotfiles and `scripts` in the working tree are not mine, and I left them alone.
