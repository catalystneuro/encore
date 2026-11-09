I've done steps 1 to 5 of the Author section and run the handover (step 6). The notebook runs from a clean environment in 1474 s (about 25 min). `entry.py check` reports 0 errors and the handover is in `executed/001371-prince-2025/handover/`. Nothing is committed.

## 1. Outcomes (52 claims: 19 reproduced, 6 partially, 8 not reproduced, 19 blocked)

| Claim | Outcome |
|---|---|
| task-timing, fig1b-above-chance, fig1b-window-performance, fig1d-heading-switch, fig5a-stay-performance | Reproduced |
| tuning-tiles-track, decoding-validation | Reproduced |
| fig2e-hpc-goal-increase, fig2e-hpc-arms-equal, sfig2e-goal-bias, sfig3c-retrospective-unchanged, sfig5g-ca1-more-goal-coding | Reproduced |
| fig3b-theta-pre-post, sfig6-theta-switch-over-delay, fig3d-new-arm-theta-modulated | Reproduced |
| sfig10-stay-transient-new-arm, fig6b-hpc-new-lower-incorrect, fig6b-hpc-initial-no-difference, fig6-hpc-pre-cue-initial-higher-incorrect | Reproduced |
| recordings, sfig3ab-original-vs-update-cue, sfig2f-all-trials-encoder, sfig5f-pfc-wider-spread, fig5d-stay-hpc-below-switch, fig7c-hpc-commitment-new-arm | Partially reproduced |
| trial-mix, sfig3c-goals-over-retrospective, fig2g-pfc-no-goal-increase, sfig5e-pfc-windows, fig3c-theta-phase-segregation, fig5d-stay-hpc-like-delay, sfig12-delay-hpc-no-outcome-difference, fig7c-hpc-commitment-initial-arm | Not reproduced |
| fig4a-lstm-choice-estimate and the 18 claims that decode its output | Blocked, `too_large` |

Several of the "not reproduced" results are claims that an effect is absent, where one test lands just under 0.05 (for example p = 0.043 and 0.032).

## 2. Dataset, assumptions, questions

**Version.** I pinned 0.260831.0201, the only published version. The paper cites none.

**Matches the paper exactly:**
- 7 animals and 66 sessions.
- 7172 delay-only, 1840 switch and 717 stay trials.
- The window counts 6252, 1002 and 117, which come from 15-trial windows.
- The Wilcoxon statistic W = 125.5 for delay-only performance.

**Findings about the dataset:**
- **Units without a region.** In five sessions (633 units) the units table has no region or cell type, and nothing in it maps them to a probe. Adding them to the 3545 CA1 and 2271 PFC units gives exactly the paper's 6449.
- **Wrong units in the metadata.** Position is labelled metres but is in track units. View angle and the stored theta phase are labelled degrees but are in radians.
- **`turn_type` labels reversed.** The description `{'right': 1, 'left': 2}` disagrees with the data and with the paper's code.
- **Paper inconsistencies.** The Methods say 40-trial windows, but the reported counts are those of 15-trial windows. Supplementary Table 1's 8104 delay trials are the 7172 final-task trials plus 932 warm-up trials.
- **Code against Methods.** The code reads the theta phase stored in the file, not one computed from peaks and troughs. I ran both and they agree, with the same outcomes.

**Assumptions:** none that an outcome rests on. Open details (filter order, how phase is interpolated between peaks and troughs, the gap bins of the track) took standard choices or the paper's code, cited in the helper module.

**Questions for the paper's authors:** none.

**Question to a reader** (`questions/001371.yaml`): the claims file's rule for excluding sessions counts encoder training trials, as the code does. The Methods count the session's trials. The Methods' count gives 55 CA1 and 46 PFC sessions, close to the paper's 56 and 47; the code's count gives 47 and 37. Under the Methods' count, fig2g-pfc-no-goal-increase (one of the two model readings) and fig5d-stay-hpc-like-delay would pass. I tested the claims as the file has them and show the other count beside every test.

## 3. Where the protocol was unclear or missing something

1. **Exclusion rule that conflicts with the Methods.** Shared method S1 follows the code where the Methods differ, and that changes two outcomes. The protocol says to ask a reader only about misreadings, and this sits between a misreading and a missing detail. I asked, and ran both counts.
2. **A criterion literally impossible on the data.** tuning-tiles-track asks every one of 50 bins to be a unit's peak, but 4 bins lie in the track's artificial gaps, where the animal never is. I judged the 46 track bins and recorded it as a deviation, without asking a reader.
3. **Notebook text after the last run.** I corrected wording in markdown cells after the final run and copied the new text into the executed copy, with code and outputs unchanged. The protocol does not say whether that needs a re-run.
4. **Who answers a timing estimate.** Step "Develop on a subset" asks for a timed estimate, but "never supply a number in the record" from outside the notebook. I put the LSTM timing cell inside the notebook, which adds TensorFlow (about 1.5 GB) to the entry's environment.
5. **Where a check stands.** The protocol does not say where checks that apply to every claim belong, such as the clock check or the comparison of the two exclusion counts. I put them in the data check and in each claim's printout.
6. **Shared deviations repeat.** Kenward-Roger degrees of freedom are not available in Python statsmodels, so I used Wald tests. That deviation, and the others shared by every claim, are repeated on each claim, since the record has no field for deviations common to the attempt.

## 4. Runtime and failures

- **Runtime.** About 2 h 05 min, from 07:47 to about 09:53 UTC, well before the 12:02 cutoff.
- **Survey.** A first walk over every object in one file took 23 min over the network. After that I read only the parts needed.
- **First extraction.** Five sessions failed on the missing region column; I fixed the loader and re-ran them.
- **Full runs.** Two clean runs passed, taking 1101 s and 1474 s.
- **Not run.** The LSTM costs about 1.5 s per epoch, 8.8 min per session and 8.9 h for all 66 sessions, against the 60 min notebook limit. Its 19 claims are blocked. The CA1 half of fig6e-predict-outcome could have been run but was not, because its criterion judges both regions together.
