I've revised the attempt for round 1 and re-run the entry. `python tools/entry.py all` passed (2,075 s, about 35 minutes), `check` reports 0 errors, and every conclusion now matches the new numbers. Nothing is committed. The `tools/` changes and the untracked dotfiles were already there before this run, and I left them alone.

## Outcome changes

| Claim | Was | Now | Why |
|---|---|---|---|
| cell-classes-counts | partially reproduced | reproduced | The one session the dandiset lacks is the figshare Neuropixel recording A8603-210602, which has 239 units. 1,760 + 239 = 1,999, the paper's count. That is the one-missing-session case the criterion allows for. |
| fig3e | not reproduced (assumed) | partially reproduced | The direction holds under every reading. The interaction is significant with rms power or with cell type as a category, but not under the code's reading (p = 0.365). |
| fig3g | reproduced (assumed) | partially reproduced | With the time-reversed control fixed, components 1 and 2 are above control under squared-modulus power (component 3 has p = 0.064), and components 1 to 4 under rms. Neither gives the claim's set of 1 to 3. |
| fig3h | partially reproduced | not reproduced | The third count is 47, outside 55 ± 6. The criterion has no partial outcome when a count is out of tolerance. |
| ed8cd | reproduced (assumed) | partially reproduced | It holds only with the noise titrated as the Methods say and simulated control cells. With the code's fixed noise, or against the recorded control, it fails. |

I agree with the verifier on all five. Round 2 will review these changes.

## Fixes and added outputs
- **Time-reversed control:** the HD series is now reversed over the epoch before the speed mask, as the claims file says. This moved several numbers and caused the fig3g change.
- **GLM coupling (fig6c, ed9d):**
  - The fits now copy MATLAB glmfit's fitting loop and flag its warnings. They flag the same pairs as round 1's rule.
  - Cells are now selected as `Figure_GLMRemWake.m` does, with no rate condition. Pair counts are now close to the paper's: 34,611, 2,683 and 19,602 against 34,270, 2,492 and 18,992.
  - The removed pairs are printed. Their fits diverge (coefficients up to 3e73). If they are kept, the HD-HD Pearson r is 0.000 and the Spearman r is 0.759.
  - Result: r = 0.641, 0.364 and 0.359, so fig6c is still reproduced. It still rests on the assumption that this copy flags the pairs MATLAB would, which can't be run here to check.
- **Three missing ArchT mice:** added from figshare Dataset_6 as a variant that decides nothing. That gives 102 HD and 50 FS ArchT cells; the paper has 83 and 47. All four optogenetic claims come out as before. The HD comparison with control is still significant (z = 7.09), so the missing mice do not explain the gap from the paper's z of 1.69.
- **Light pulses:** widths and intervals are printed, and the decoded pulses match figshare's pulse tables within 0.1 ms.
- **Smaller fixes:**
  - fig2b's chance level is now scored against the real head direction (92.8°).
  - Units are now kept at a rate of at least 0.5 Hz, as the Methods say.
  - The fig4f note now explains why the two time-window lengths give identical results.
  - The ed8cd text now names the titrated noise as the main reading.
- **fig1ac depth sign:** the files have no probe geometry. The step sits at cell depth −35 µm, next to the zero that a commented-out line of the paper's code uses to drop non-PoSub units. That puts PoSub at the high-information end, but which end is shallower still rests on the code, not the data.
- **New dataset finding:** in A3711, A3717 and A3723 the sleep scoring runs to about twice the recording's length, so up to 518 s of REM falls after the recording ends. In A1821 and A3712, some REM falls inside open-field epochs. These intervals are the same in the earlier dandiset version. REM is now limited to the home-cage epochs.
- **Reader question:** added to `questions/000939.yaml` for fig5e. Its reading (b) contradicts the Methods' "no cells from other populations", and that reading is the only one that fails. The claim is unchanged.
- Round 1 is recorded under `verifications`, and the record, notebook summary, README and `entry.yaml` (35 min) are updated.

## Not changed
- **fig3-ten-components-power:** the verifier noted that requiring the rms power reading is strict, but the criterion names both readings, so I didn't change it.
- **ed6:** kept as blocked for `other`, not `data_missing` as the verifier wanted. The claims file says its data are elsewhere, and `tools/entry.py` rejects `data_missing` for those claims. The disagreement is recorded.
- **GLM lags:** only lag 0 is fitted. The paper's code drops a pair for a warning at any of 201 lags; this is recorded as a deviation.
