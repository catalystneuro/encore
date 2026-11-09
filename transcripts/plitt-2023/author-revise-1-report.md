I've revised the attempt for every point in the round-1 report. The notebook re-ran from a clean environment in 43 min, `entry.py check` reports 0 errors, and the new run's numbers match the run before it. Nothing is committed.

**What changed in the outcomes.** Eight claims are now `blocked: methods_underspecified`: figs9a, figs9b, the three fig7e claims and the three fig7h claims.
- **Why:** this answers problem 1, that the HSE detector was never validated. Read from the Methods, the detector still flags most of the same trials when each cell's activity is shifted in time so that the cells are no longer synchronous.
  - Under the onset null it flags 0.43 of Cre trials and 0.16 of control trials, against 0.46 and 0.20 in the real data.
  - Under the series null it flags 0.15 of Cre trials, against 0.26 real.
  - On synthetic data with independent cells it flags 20 to 40% of trials.
  - The figs9a ANOVA on the shifted data finds the same group difference (p=0.0014 and 0.029).
  - Cre mice also stop about 3.6 times longer after rewards (5.4 s against 1.5 s), which gives more chances for chance coincidences.
- **The rule:** I wrote the blocking rule into the notebook before running the null on all sessions. I had already seen it on two sessions during development, and the notebook says so.
- **Kept, with the disagreement recorded:** the verifier would give `partially_reproduced` for four claims where I kept the outcome:
  - **fig3i:** the criterion's readings are about which cells are counted, so it holds if any reading holds.
  - **figs3c:** the per-bin reading is adopted.
  - **fig4-block6:** the 150 cm stem is adopted.
  - **fig6e:** day 1 is adopted. The pooled interaction (p=0.001) disappears with a random slope per mouse (p=0.585) and with per-mouse slopes (p=0.586). It stays at p=0.002 with a variance component per mouse-day.

  The last three are now stated as assumptions. The verifier's `partially_reproduced` for fig7h-reactivation-effect is replaced by the block. All other outcomes are unchanged.

**What I added or corrected:**
- **Split days (problem 7):** block numbers restart at 0 in the second file of a split day. They now continue from the first file, as the authors' code does. Before this, "block 4" of Ctrl-4 day 2 was its novel block. The figs6b result is unchanged to the printed precision.
- **Place cells (problem 3):** deposited and recomputed spatial information and p-values are compared per cell. The recomputed set holds almost every deposited place cell and adds more. The spatial-information ranks agree but the scale does not, so the deposited masks use a different measure and a stricter null. I added a question for the authors as a finding.
- **PV shift (problem 4):** a synthetic check shows the raw centre-of-mass reading is ill-conditioned. figs8d now uses the clipped reading (r=-0.148, p=0.585).
- **Running speed (problem 5):** the bin-mean normalisation is now the main reading, and the time-weighted one is a variant.
- **Smaller points:**
  - The reactivated and non-reactivated cell counts per mouse are printed, with a variant that keeps only mice with at least 10 cells in each group.
  - figs3c has a like-for-like single-trial variant.
  - fig5d chance is also run with the stem ending at 100 cm.
  - The per-mouse first-reward positions are printed.
  - The Cre-3 day 5 trials per block are printed.
- **Outputs asked for in section C:** the notebook now prints the authors' code lines from the pinned commit (dF/F loading, decoder input, `calc_pv_corr`, block numbering). It also lists the Figshare `shuffle_pkls.zip`, which holds no HSE results.
- **Questions for a reader:** `questions/001710.yaml` has three. They are fig6d's sign convention, whether vr-reward should require licking to increase or only change over days, and whether fig7h's absence test should be one-sided. The claims were tested as written.
- **Record:** the attempt record has the round-1 verification for all 57 claims (52 agree), plus updated notes, deviations and findings. I also updated the README and the notebook runtime in `entry.yaml` (45 min).

**Not done:**
- I could not trace the exact cause of the place-cell difference. The authors' place-cell function is in a package the linked repository does not hold.
- I did not compare the HSEs with the authors' own results, because their shuffle files hold none.
- I did not run `entry.py handover`. It strips the conclusions, and round 2 needs the full executed notebook, which is in `executed/001710-plitt-2023/`.
