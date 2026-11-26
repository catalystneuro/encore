I've revised `haley-2018-01` for round 1. The entry was re-run with `tools/entry.py all`: it passed in 52 minutes and `check` gives 0 errors. Every number in the record and the notebook's conclusions comes from that run.

**Outcomes changed (all round 1, so changes were allowed)**
- `fig3c-stg-rhythmic-fraction`, `fig3d-stg-frequency`, `fig3f-stg-duty-cycle` and `fig6-cg1-measures` go from partially_reproduced to not_reproduced. None of their criteria has a partial condition, and for fig3c the claims file expects 15 preparations with tolerance 0, while the dataset has 13.
- Totals are now 11 reproduced, 2 partially reproduced, 11 not reproduced and 6 blocked. This matches the verifier on every claim.

**Fixed or added**
- **STG states (problem 1):** a second now counts as rhythmic only if the PD neuron is bursting and the lvn nerve shows at least 2 spikes between PD bursts. That is the LP and PY firing that states 1 and 2 require, so state 3 no longer counts. The previous PD-only reading, 1 or 4 lvn spikes, and gap factors 2 and 5 are all shown as variants. The numbers barely moved (STG at 5.5: 0.375 against 0.393 before). No outcome changed.
- **CG Large Cell isolation (problem 2):** for each unit there is now a text histogram of spike heights relative to the threshold, with the counted heights compared with control, plus the CG results without the four units the verifier named. Without them, fig7c would hold at pH 10.4, so its outcome depends on those units; the notes say so.
- **903_052 PD label (problem 5):** the old check looked only within 5 ms. Allowing for the delay to the pdn nerve, 0.61 to 1.0 of PD3's spikes in 7 of its 9 files with PD spikes are followed by a pdn spike 34 to 38 ms later, against at most 0.037 by chance. So PD3 is PD, and fig4a stays reproduced, resting on this one preparation.
- **903_056 short 8.8 file (problem 6):** without it, the LP 8.8 test gives corrected p = 0.056, which would make fig4bc partial. I recorded this in the notes and kept the outcome, because that file is the only 8.8 file and the paper's code takes the last minute of each file.
- **Missing pH steps entered as 0 (problem 3):** kept as the main reading, because the paper's code does this. The record quotes the lines from `extracellularAnalysis.m` and `pHCumulative.m`. The variant that leaves missing steps out is now run for fig8a, fig8b and fig8b-cross.
- **Other outputs added:** the testable parts of fig3a; the nerve list of every STG experiment, which shows 8 of 15 with lgn and dgn and 4 with ion; conclusions now say where the statistics rule runs no t-tests after a non-significant ANOVA (problem 10).
- **Questions for a reader** in `questions/haley-2018.yaml`: the fig3d "relatively invariant" reading (problem 4), reading (b) of fig3s2 and fig7s2, and fig8a's missing partial category (both problem 11).
- The round is recorded under `verifications`, with all 30 claims, the verifier's reasons and my responses. The helper docstring, the entry README and `entry.yaml` are updated.

**Not done, and why**
- **Gastric claims:** kept blocked. The fallback has no thresholds for rhythmic or alternating bursting, and 6 of the experiments in the project would need LG sorted from the lvn.
- **State-transition claims and fig3a:** kept blocked, because LP and PY are not told apart, so states 1 and 2 cannot be separated.
- **877_101:** its PD was not taken from the lvn or the unnamed ME1_Vx channel.
- **Trace overlays:** not added, because the entry has no plotting package; the histograms and lag tables are text.
- **OSF access:** osf.io was answering with HTTP 429 (too many requests), which cost two failed development runs. The helper now reads files through WaterButler with a throttle and retries; the two runs give identical numbers.
- **Untracked files:** the attempt record was rewritten by a YAML dump, so its diff is large but the formatting is consistent. Untracked dotfiles (`.bashrc`, `.idea`, and others) and a `scripts` folder appeared in the repository root. I did not create or touch them, and they should not be committed.
