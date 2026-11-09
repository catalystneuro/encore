I've finished the attempt (steps 1 to 6). The entry `entries/crcns-apl-1-bruno-2017/` passes `tools/entry.py check` with 0 errors and ran from a clean environment in 1078 s (18 min). The handover is built in `executed/crcns-apl-1-bruno-2017/handover/`. Nothing is committed.

## 1. Outcomes per claim (30 claims)

| Claim | Outcome |
|---|---|
| dataset-size | partially reproduced: 10 preparations, 30 recordings and 1131 neurons match; recordings hold 75 to 160 neurons, so only 12 of 30 fall in 108 to 198 |
| fig1d, fig1e, fig2b, fig2ef, fig2e, fig2s2 | reproduced |
| fig3a-coalescence | not reproduced: coalesces within one period in 12 of 30, where the criterion needs 27 (the "dominated by recurrence" part holds in 30 of 30) |
| fig3c, fig3s1a, fig3d, fig3f | reproduced; the failing pairs are the ones the paper names (prep 4: pairs 1,2 and 1,3; prep 7: pairs 1,3 and 2,3) |
| fig3h-perturbations-return | partially reproduced, assumed: 15 of 16 return; both counts fall just below tolerance under the Methods' mean period, and are within it under the median |
| fig3i | reproduced, under reading (b) |
| fig4bc-stable-spiral | partially reproduced: the grand mean is a stable spiral, but only 8 of 10 preparations have 2 of 3 responses in the region |
| fig4c | reproduced, assumed (10.45 s) |
| fig4s1a | not reproduced: all dimensions contract in 11 of 30 |
| fig4s1b, fig5b, fig5c, fig6s1 | reproduced |
| fig6d-decode-p10 | partially reproduced: 8 of 9 (prep 4, response 1 fails) |
| fig6s2 | partially reproduced |
| fig7a, fig7f, halving, fig7s1 | reproduced |
| fig7gh | not reproduced, assumed: the outcome flips with the reading (see below) |
| fig7s2 | blocked, `not_runnable`: the ensemble-typing toolbox is MATLAB and porting it would not fit the time |
| fig8 | blocked, `metadata_insufficient`: nothing says how the photodiode array is oriented, so the caudo-lateral quadrant can't be located |

Totals: 20 reproduced, 5 partially reproduced, 3 not reproduced, 2 blocked.

## 2. What was found about the dataset

**Dataset**
- **Version pinned:** CRCNS data sets have no versions, so the version is `unversioned`. The bucket holds a single processed copy under `live/`; I pinned it by the MD5 sums of the files read, which match the dataset's own `checksums.md5`.
- **Matches its description:** 30 recordings, 1131 neurons, the stimulus at 30 s, P10 nerve recordings for preps 2, 4 and 5, no recording deposited twice.
- **Paper contradicts itself:** it gives 120 to 180 neurons per recording and 1131 in all. Ten preparations of at least 120 would hold at least 1200.
- **Sampling rate:** the P10 timing grid is 1629.7 Hz, which agrees with the description's 1630 Hz, not the paper's 1600 Hz.
- **File names:** the P10 files of prep 2 drop the "B" of `Jun0414B`.
- **Coordinates:** no unit and no orientation are given.
- **Clock:** the population and P10 rates are correlated after the stimulus, which is consistent with a shared clock, but the check doesn't separate the data from shifted series in 2 of 9 recordings.
- **Same neurons across bouts:** neuron identity across bouts is consistent with the data (30 of 30 bout pairs above permuted ids), and I used it as an assumption.

**Code mismatches**
- Figure 6D's N = 173 forecast windows matches the code's windowing (174 per response), not the Methods' (40 per response).
- `What_is_Participation.m` mismatches two of the three pairs.
- `LocalLinearDynamics.m` detects contiguous runs with a quirk that can miss gaps.

**Assumptions.** I adopted one reading where a single one had to be chosen: the kernel SD is the recording's own median ISI, and the number of PCs is the smallest reaching 80%. The Methods' printed width (median ISI / 12, or / √12) gives 21 to 76 dimensions, so it can't produce the paper's 4 to 8. Every reading is run in the notebook. The outcome changes with the reading for fig3h, fig4c and fig7gh. For fig7gh, the code's exact width and count rule would make it reproduced.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which kernel width was used, and was the median ISI per recording?
- Which PC-count rule produced Figures 2 to 5?
- For dropping divergences near the recording's end, is the cycle the mean or the median period, and does the rule apply to all of them or only to those that never return?
- Which permutation test gave Figure 5B?

**Questions to a reader:** none.

## 3. Where the protocol was unclear
1. The protocol doesn't say how far readings of an early detail (kernel width, PC count) must be carried into the claims that depend on it. I carried four readings through every claim, and the two unusable narrow widths only as far as fig2ef.
2. It doesn't say what `measured` should be for a claim stated as a range ("10 to 15 s"). I recorded the quartiles and let the criterion's count decide.
3. The clock check is described for trial tables. For continuous spikes plus a nerve recording I used cross-correlation against circular shifts, which is weak for a 10 s rhythm.
4. There's no rule for when a criterion's parts hold under different readings. fig6s2's dimension counts hold under the code's count rule, while its decoding part was run under the adopted one; I called it partial.
5. There's no rule choosing between partial and not reproduced when one part of a multi-part criterion fails. I used not reproduced when the main part failed (fig3a, fig4s1a).
6. For claims of absence the protocol says readings don't apply, but the inputs to the test (distances, participation) still have readings. For fig7gh I adopted one reading and marked it assumed.
7. The 10-minute aim conflicts with running every reading. The notebook takes 18 minutes, and the 90%-variance P10 models use 4 history lengths instead of the full grid.

## 4. Runtime and failures
- About 2 h in all (12:03 to 14:03 UTC). The notebook takes 18 min with peak memory about 1.3 GB.
- A development run of the 90% decoding with the code's windowing took 17 min, so it was left out of the notebook.
- One cell failed on the first development run (a pandas column name); it was fixed, and the final run's numbers are identical to the development run's.
- Untracked dotfiles (`.bashrc`, `.idea` and others) appeared in the repository root. They aren't mine and I left them alone.
