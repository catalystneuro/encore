I've done steps 1 to 6 for DANDI:000139, pinned at 0.220113.0408. It is the only published version and the paper cites none. The notebook passes `entry.py check` and ran clean under `entry.py all` in 362 s; the handover package is built. I did not verify my own work.

## 1. Outcomes (23 claims)

| Claim | Outcome |
|---|---|
| j-array-recordings | partially reproduced (152 units, but 27 conditions, not 108) |
| fig4d-mean-correlation-j-array | partially reproduced, assumed (r = 0.172, p = 0.042) |
| fig4-broad-unimodal | reproduced, assumed |
| fig4e-correlation-time-course | reproduced, assumed |
| suppfig1-population-psth-weak-movement-tuning | reproduced, assumed (reading (a) only; ratio 0.942) |
| fig6d-perimovement-best-j-array | reproduced, assumed |
| fig6-perimovement-best-each-dimensionality | reproduced, assumed (91 to 96% of comparisons) |
| fig6-dimensionality-peak | reproduced, assumed (S fixed across folds) |
| fig6-maze-task-spaces | blocked: methods_underspecified |
| fig6-preparatory-dimensionality | not reproduced (12 PCs; shuffled labels give 17) |
| fig7a-shuffled-space-poor | reproduced, assumed |
| fig7b-window-start-slide | reproduced, assumed (0.911) |
| ap-location-no-effect-j-array | reproduced, assumed (AP read as the array) |
| fig7c-anterior-posterior-performance | not reproduced, assumed (the normalization is unstable) |
| prep-activity-more-anterior | not reproduced, assumed |
| fig7d-pd-consistency | reproduced, assumed |
| some-neurons-better-elsewhere | reproduced, assumed |
| high-dimensional-task-spaces-underperform | reproduced, assumed |
| fig8-linear-dynamics-simulation | reproduced, assumed (full-cycle interval) |
| fig4abc, fig6abc, fig6e, ap-location-other-datasets | blocked: data_missing |

Totals: 13 reproduced, 2 partially reproduced, 3 not reproduced, 5 blocked.

## 2. Dataset, assumptions, questions

**What the dandiset holds.** One session of monkey J (2009-09-29) on the maze task, cut for the Neural Latents Benchmark:
- 152 units on two arrays (75 and 77 by unit id).
- 250 labelled trials over 27 conditions (9 mazes in 3 versions), so 6 to 10 kept trials per condition. The paper's J-array dataset had about 2166 trials per neuron and 108 conditions.
- The 100 test trials have no condition labels, go cue or behaviour, so they cannot be used.
- No EMG, speed-task or single-electrode data.

Because of the low trial count, preparatory tuning is noisy (median split-half r = 0.374) and all PD performances are low (best 0.117 to 0.226).

**Findings recorded about the dataset:**
- **Metadata error:** every unit's electrode reference points at a PMd row. The second array's units reference rows 14 to 94, which looks like M1 channels missing an offset of 96.
- The electrode x, y and z columns are empty, so AP location can only be read as the array.
- Nothing links this session to the paper's J-array recording.
- How the trials and the 9 mazes were chosen is not documented.

**Assumptions, each stated as a deviation with the passage cited:**
- **Tuning strength is the range across conditions.** With the standard deviation, almost no unit passes 5 spikes/s.
- **Proto-trial is the condition mean, with the two velocity profiles concatenated.** This keeps 93 to 96% of trials, close to the paper's "typically ~90%". Comparing the profiles separately keeps only 70 to 82%.
- **The PCA space S is computed once from all conditions** (the Methods' wording); only the PD is refitted in each fold.
- **Unit id prefix 1 is the PMd array.** This decides the direction of prep-activity-more-anterior.
- **Figure 4E** uses the Figure 4D neurons and a trace spliced at the median RT.
- **Figure 8** uses a full-cycle "gray interval".

**Questions for the paper's authors** (five methods_unavailable findings): how the proto-trial is defined, how tuning strength is measured, whether S is recomputed in each fold, whether the reach is split into segments of equal time or equal path length (this is what blocks fig6-maze-task-spaces), and how movement onset, the Figure 4E splice and the Figure 8 interval were set.

**Questions to a reader:** none. I found no misreading in the claims file.

## 3. Where the protocol was unclear

1. Readings multiply across claims: 8 trial-selection readings times claim-specific readings. The protocol does not say whether a reading adopted for one claim carries to the claims that depend on it. I adopted one main reading for all claims, showed the others, and marked every outcome that depends on it as assumed.
2. It is unclear whether `assumed` covers data identity, such as whether the 27 mazes are among the paper's 108, as well as method choices. I did not mark j-array-recordings as assumed and said so in its notes.
3. Where a criterion's reference value comes out degenerate (fig7c, normalized by an upper limit that is near zero or negative), the protocol gives no rule. I applied the criterion as written (not reproduced) and explained the instability in the notes.
4. The criterion's own readings (any reading suffices) and the open-detail readings of step 1.6 (all must agree) can conflict, as in suppfig1. I applied the criterion's "any reading" rule and noted where the stricter reading fails.

## 4. Runtime and failures

The notebook takes 362 s. The author run took from 19:44 to about 20:23 UTC. Nothing failed.

I did not touch some untracked files at the repo root (`.bashrc`, `.profile`, `.idea` and others) that are not mine. Check them before the workflow commits.

Files are in `entries/000139-churchland-2010/`:
- `reproduce_churchland_2010.ipynb`
- `maze.py`
- `README.md`
- `entry.yaml`
- `requirements.in`
- `requirements.lock.txt`

The attempt record is `attempts/000139-churchland-2010-01.yaml`.
