I've done steps 1 to 6 for dandiset 000232: the entry is locked, checked and runs cleanly from a fresh environment, and the verifier's package is built in `executed/000232-chang-2023/handover/`. Nothing is committed or pushed. The notebook runs in 14.3 minutes (867 s), and the run gave the same numbers as the earlier test run.

**Paper text.** I used the full text of preprint version 2, which is open access (CC-BY). bioRxiv refused the download (rate-limit error 1015), so I took the same text from eLife's copy of the reviewed preprint (92620v2), whose source is bioRxiv v2. It is saved under `paper/`. Table 1 and the table of coding-dimension trial types are images there and were not read.

**Version.** I pinned 0.240510.2038, the only published version. The preprint cites no version ("available upon request"); the paper's code repository cites this one. The draft has identical files and differs only in contributor metadata.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1e-recording-counts | reproduced |
| fig6-session-counts | reproduced |
| fig1d-performance | reproduced (73.6 / 74.8%, p = 0.561 against the paper's 0.56) |
| fig1d-outcome-fractions | reproduced |
| fig1h-thit-tcr-selective | partially reproduced (MM 36.4% against 32.9%) |
| fig2c-rule-prestim-units | partially reproduced (S1 5.6% against 4.5%) |
| fig2d-stimulus-prestim-units | reproduced |
| fig2e-stimulus-poststim-units | reproduced |
| fig2f-prestim-predicts-touch-response | reproduced |
| fig3b-rule-decoding | reproduced |
| fig3c-rule-decoding-motor-stronger | reproduced |
| fig3de-stimulus-decoding-controls | reproduced |
| figs3-svm-rf-decoding | reproduced |
| fig4c-prestim-distance-predicts-divergence | partially reproduced (p = 0.004, the paper says p < 0.001) |
| fig4e-subspace-overlap | partially reproduced (all four areas significant, only S2 within tolerance) |
| fig4f-prestim-overlap-predicts-poststim | reproduced |
| figs4ef-coding-dimensions | partially reproduced (MM stimulus dimension not aligned) |
| figs4h-choice-right-left | partially reproduced |
| fig5b-first-hit-switches | partially reproduced |
| fig5de-motor-states-track-switch | reproduced |
| figs5-sensory-states-no-tracking | reproduced |
| fig6c-pre-inhibition-tactile | partially reproduced (ALM interval reaches +0.005; with the code's resampling it matches the paper) |
| figs6b-pre-inhibition-hit-rate | reproduced |
| fig6d-post-inhibition-tactile | reproduced |
| figs7gh-visual-sensitivity | reproduced |
| fig6-ppc-inhibition | reproduced |
| fig6fg-detection-task | reproduced |
| fig6ij-laser-only-licks | not reproduced (1 of 12 intervals excludes 0: detection task, MM, short laser) |
| fig1e-probe-locations | blocked: data_missing |

That is 18 reproduced, 9 partially reproduced, 1 not reproduced and 1 blocked. Every claim uses the dandiset only.

## 2. What was found about the dandiset

- **It matches the paper closely.** Sessions, mice and units per area are exact: S1 10/6/177, S2 8/5/162, MM 9/7/140, ALM 13/8/256, AMM 110 units. All 24 optogenetic session and mouse counts match too. Several bootstrap intervals (decoding, transition tau, the code-variant optogenetic intervals) land within about 0.03 of the paper's.
- **Selection is not documented.** The ephys files hold only the trials and units the paper kept. The trials removed for pre-stimulus licking (about 25%) and the units that failed the quality filter are absent, and the dandiset doesn't say so.
- **Unit and electrode metadata are thin.** Units have no quality metrics, channel, depth or original cluster id, so the paper's example units can't be found. Electrode x, y, z are NaN, locations are "unknown", and there is no histology.
- **Behaviour files have labelling errors.** `start_time` equals the stimulus onset, so trial intervals overlap. In the detection task, trials without a whisker stimulus are labelled "Stim_Vis". The trial columns have no descriptions; codes such as `response` and "Change" (the cue trial) are explained only by the paper's code.
- **Paper and code disagree in places.** Figure 5B's "88 and 91 switches" equals the number of blocks including each session's first block (the actual switches with a hit number 63 and 75). The normalization offsets and session rules differ between Methods and code. The code's optogenetic bootstrap does not resample false alarms.
- **Small anomalies.** Three laser trials have odd timing (onsets at -1.6 and -2.7 s, one 9.5 s long), and one of the 28 cross-modal sham sessions fails the code's own performance check.
- **Clock.** Spike times and trial times share a clock in 43 of 49 sessions; this check could not establish it for 3 sessions with 2 to 5 units.

## 3. Where the protocol was unclear, wrong or missing something

1. **Paper download blocked.** bioRxiv refused it. I used eLife's reviewed-preprint copy of the same bioRxiv v2 text and said so in the claims file and the notebook header.
2. **Methods versus the reported number.** For the subspace analysis the Methods exclude sessions with fewer than ten units, but the paper's session counts fit the code's "more than ten". The protocol makes the Methods the main result even when the reported numbers fit the code, so I followed the Methods and showed the code's rule as a variant; the outcome is the same.
3. **Code in the files' preprocessing.** The paper's code had already been applied to the files (trial and unit removal). The protocol doesn't say how to treat a Methods step that may or may not already be applied, such as "remove the last 20 trials". I listed both readings in the criterion.
4. **A criterion that could not decide.** In figs4h, "needed condition" read strictly left 1 of 10 S1 sessions. I broke the tie as the code implies (pooling over stimuli), as the protocol's tie rule says, and recorded it as a deviation. I had already seen one area's result when I did this, and the record says so.
5. **A reading I did not list.** For fig5b I did not list "count all blocks" as a reading before the analysis, so I kept the criterion as written. The match with 88 and 91 is recorded as a finding instead.
6. **Absence claim with two possible tests.** Fig6ij gives one interval per area while the code computes two (short and long laser). The absence rule doesn't say what to do when the paper's test is ambiguous. I required all twelve intervals to include 0 and said so in the criterion.
7. **Outside sources.** The protocol has no slot for a code repository that is read but supplies no data. I listed it under `inputs` with a note that no data came from it. The dandiset also links processed data on Zenodo (doi:10.5281/zenodo.11176244), which I did not use.
8. **Bootstrap draws move the result.** Results that hinge on a bootstrap's extreme values change with the seed. I showed four other seeds for fig1h and fig2, but the protocol doesn't say whether the main seed or the spread decides; the main seed decided.

## 4. Runtime and failures

- Run time is 14.3 minutes; streaming the files takes about 3.3 of them.
- Two test runs before the final one failed or gave wrong values: a pandas duplicate-index error, a string column in a median, and a light-block mask bug that produced `inf` in Fig 1D. All three were fixed before the final run.
- No step was skipped.
- Untracked files I did not create appeared in the repo root: `.bashrc`, `.bash_profile`, `.gitconfig`, `.idea`, `.mcp.json`, `.profile`, `.ripgreprc`, `.vscode`, `.zprofile`, `.zshrc`. I left them alone; the workflow should not commit them.
