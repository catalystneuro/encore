I've finished steps 1 to 5 of the Author section and run `entry.py handover`. `entry.py check` reports 0 errors, and `entry.py all` passed from a clean environment (735 s, peak memory 7.1 GB). Nothing is committed.

## 1. Outcomes (22 claims)

| Claim | Outcome |
|---|---|
| fig5e-cue-betas | reproduced, rests on assumptions |
| fig5f-cue-dominance | reproduced, rests on assumptions |
| figs5c-turn-angles | reproduced, rests on an assumption |
| fig2c-complex-auc | partially reproduced, rests on an assumption |
| fig2e-complex-weights | partially reproduced |
| figs1fg-resolution-robustness | not reproduced |
| methods-intensity-right-bias | blocked, metadata_insufficient |
| fig1eh, fig1il, figs1-antisymmetry, figs1-temporal, fig2b, fig2d, figs2c, fig3bc, fig3d, fig3e, fig3ij, fig4ef, discussion-ten-percent-gain, figs4, figs5fh (15) | blocked, `other`: the smooth plume could not be read |

The three "reproduced" results all depend on choices the paper leaves open; with the other choices they fail (see section 2).

## 2. Dataset, assumptions, questions

**Version.** I pinned 0.260630.1657. It is the only published version, and it is the one the paper's code names.

**What the dataset holds and what is wrong with it.**
- It has 131 behavior files: 83 smooth-plume, and two complex-plume sets of 24 each, "smoke-1a" and "smoke-2a". Nothing says how the two complex sets differ or which one the paper used. The paper's code uses smoke-2a.
- The smooth plume is not in the dandiset. Dryad answers 401 without a token, and the file was not staged for this run.
- **Main finding:** the paper's own code, run on the smoke-2a files it selects, does not give its published complex-plume Fig. 5E/F values:

  | Quantity | From the deposited files | Published |
  |---|---|---|
  | Complex motion β | −0.012 (p 0.15) | +0.044 |
  | Complex dominance | +0.39 | −0.66 |

  The smooth-plume values match the published ones. My port of the code gives the code's exact output on these files.
- The turn events start a median of 4 frames after the SI's onset rule (rotational speed crossing 20% of its peak) and end early. Over the files' events, turns measure about ±21°, not the paper's ±34°.
- Other gaps:
  - The turn direction label (+1/−1) is never mapped to left or right.
  - The heading is computed with y reversed, which the files do not say.
  - Motion (`odor_velocity`) is NaN on 95–98% of frames.
  - 205 trajectories have no position at all.
  - Four smooth files have positions up to 814 mm in a 170 mm arena.
  - The odor signals cannot be aligned in time with the deposited movie.

**Assumptions.**
- **Fig. 5E/F:** the SI's turn onset, the smoke-2a files, and predictors either as stored or z-scored over all frames. With the files' turn start or with per-trajectory z-scoring they fail. Under the adopted reading the complex motion coefficient is significant but has the opposite sign to the paper's; the criterion tests significance only.
- **Fig. 5F:** both values fall within tolerance only with the code's complex heading window (150–210°). With the SI's 160–200° the complex value is −0.58, negative but just outside tolerance.
- **Fig. S5C:** a turn ends where speed falls back below 20% of its peak. With that, the medians are −35.0° and +35.9°.
- **Fig. 2C:** samples are mirror-balanced. This is the only sampling that gives the paper's sum AUC of exactly 0.5.

**Questions for the paper's authors.** These are recorded as a `methods_unavailable` finding:
1. Which complex files are the complex plume of Fig. 5?
2. Which turn onset did the figure use?
3. How were the Fig. 2 samples balanced?
4. Where does a turn end for Fig. S5C?
5. How is the Fig. S1G motion cue defined, and were the maps smoothed?
6. Was z-scoring over all frames or per trajectory?

**Questions to a reader:** none.

## 3. Protocol and tooling problems
1. The Dryad file was not staged, although `docs/archives.md` says Dryad files are staged before the agent starts. No `blocked_by` value fits "public but not fetchable", so I used `other` and explained it in the notes.
2. `entry.py lock` writes a `python:` field into `entry.yaml` that the entry schema rejects. I deleted the line.
3. `entry.py check` requires `about:` on `other` and `selection_undocumented` findings, but the attempt schema forbids `about`, so those kinds can't be recorded at all. I recast the one affected finding as `metadata_insufficient`.
4. The protocol doesn't say how to combine readings across several independent open details (onset, file set, z-scoring, heading window, margin). It also doesn't say whether a reading the author adds (file set, mirror sampling, turn end) counts under a criterion's "under one reading". I adopted one combination, marked it assumed, and showed every combination.
5. `measured` says to record "the first reading the criterion lists". That doesn't cover a reading the author added, so I recorded the adopted one.
6. The clock check can't be done when the files have no stimulus frame index. I recorded it as not established.
7. Nothing says whether to compute the decidable parts of a claim that is blocked anyway. I ran the complex-plume part of figs2c (cheap), but skipped the freestream parts of the Fig. S1 claims, which would mean streaming about 25 GB.
8. The fig5e criterion tests significance but not sign, so it passes while the sign is reversed relative to the paper. I put this in the notes, not a reader question, because the claims file doesn't misread the paper.

## 4. Runtime and failures
- The run took 04:15 to 05:56 UTC, about 1 h 40 min.
- Notebook runtime is about 12 minutes.
- The first development run peaked at 11.9 GB of memory. I fixed that before the clean runs, which peaked at 7.1 GB.
- Running the paper's original code once for validation took 20 minutes (outside the notebook; it decides no outcome).
- No step failed in the final runs.

Files are in `entries/brudner-2026/`:
- `reproduce_brudner_2026.ipynb`
- `plumes.py`
- `README.md`
- `entry.yaml`
- `requirements.in`
- `requirements.lock.txt`

The attempt record is `attempts/brudner-2026-01.yaml`, and the verifier's package is in `executed/brudner-2026/handover/`.
