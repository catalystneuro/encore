I finished the five Author steps and ran the handover at 04:17 UTC. `entry.py all` passes, and the verifier package is in `executed/001950-su-2026/handover/`. Nothing is committed.

## 1. Outcomes (39 claims: 12 reproduced, 10 partially reproduced, 6 not reproduced, 11 blocked)

| Claim | Outcome |
|---|---|
| fig4c-choice-history, fig5a-engagement-reward-history, fig5e-switch-history, fig4g-go-cue-excitation, fig4h-tonic-phasic-anticorrelation, fig5b-baseline-predicts-ignore, figs18d-outcome-not-on-anatomy-axes, fig6g-rpe-vs-no-reward-populations | Reproduced |
| fig6c-choice-change-rpe, fig6-outcome-responsive-fraction, fig6i-axons-rpe, fig6j-cortical-input-more-positive | Reproduced, resting on the refitted model (`assumed: true`) |
| iti-mean, fig5h, fig5k, figs17i, fig6a, fig6f-outcome-angles, figs14, figs15q, figs15t, figs16 | Partially reproduced |
| figs12-trials-per-session, figs15f, fig5c, fig5d, fig5g, fig6h | Not reproduced |
| 10 anatomy, transcriptomics and slice claims (`data: elsewhere`) | Blocked, `other`: the Code Ocean data have no DOI or commit to pin |
| fig6f-cortex-projecting-rpe-biased | Blocked, `data_missing` |

## 2. What was found about the dataset

- **Version.** I pinned 0.260928.2230, the only published version; the paper cites none. The draft (modified 2026-10-06) adds ten unit columns: the paper's LC-NE label `opto_NE_paper`, the antidromic classification (`antidromic_tier_1` and others) and the stable recording windows. The notebook shows this difference but uses nothing from the draft.
- **Unit selection.** The pinned version does not mark the paper's LC-NE units, and the Neuropixels files hold all 14,126 sorted units. Applying the code's criteria files gives 252 units from 21 mice, against the paper's 241 from 19. The draft's label agrees with this selection on 223 units.
- **Missing data:** the drift regressor (per-trial spike amplitudes), the Q-learning variables, and the cortex-projecting labels.
- **Format and metadata errors:**
  - Some numeric columns are stored as strings (`isi_violations_ratio` in 4 files, `peak_to_valley` in 54).
  - Tetrode units have no ISI column. I recomputed it from spike times; the same computation matches the Neuropixels column at r = 0.9993.
  - `pupil_diameter` has no unit.
  - `right_lick_time` is described as "left licks".
  - Two files have no trial table.
- **Clocks.** Spikes, licks and pupil all share the trial clock, checked against shifted cue times.

**Assumptions.**
- The Q-learning model is refitted per session by maximum likelihood (same model as `aind_stan_fit_sim`). I did not run the paper's hierarchical Stan fit.
- My own window for the photometry quality threshold.
- A standard peak window for the lick claim (figs15q). The criterion says to use the code's window, but I did not read that notebook. This is recorded as a deviation.

**Questions for the paper's authors** (a `methods_unavailable` finding):
1. Is the 3.95 in Figure 4c the amplitude or the decay constant? The amplitude matches here; no decay constant does.
2. Which window applies the 0.5 z photometry threshold?
3. Which window and bin give the lick peaks in Figure S15q?
4. What sign convention do the t-statistics in Figure S15f use?

**Questions asked of a reader** (`questions/001950.yaml`):
1. figs12: the claims file counts go cues, but counting responded trials matches (mean 360.6, maximum exactly 558).
2. fig5d/5h: the claims file may have swapped the projection and gene-expression axes relative to the code's labels.

## 3. Where the protocol was unclear or missing something
1. A `data: elsewhere` claim whose source is public but not pinned has no fitting `blocked_by`, since `data_missing` is forbidden for it. I used `other`.
2. When a newer draft fixes what the published version lacks, the protocol says nothing beyond pinning the published version. I pinned it and only showed the difference.
3. There is no outcome rule for a result where the qualitative criterion holds but the value is outside tolerance because the effect is stronger (Rayleigh z 28.1 against 19.5; lick r 0.61 against 0.49). I used partially reproduced.
4. When part of a criterion needs labels the dataset lacks (cortex-projecting neurons in fig5k, figs17i), I tested the rest and marked the claim partially reproduced, with notes.
5. When a method is fully specified but cannot be run (the hierarchical Stan fit), step 1.6 does not cover substituting a standard estimate of the same model. I recorded it as an assumption, not `not_runnable`.
6. The criterion of fig4c lists collinear regressors (rewarded plus unrewarded history equals choice history). I ran the code's two identifiable models.
7. The claims file's header says the version-of-record text holds only the abstract and references. In fact it holds the full text, on one line (line 268).

## 4. Runtime and failures
- The run took about 2 h 12 min, from 02:05 to 04:17 UTC.
- The notebook runs in 18 min from a clean environment, most of it streaming. It was run three times, and the results were identical each time.
- Nothing failed.
