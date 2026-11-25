I've completed steps 1 to 5 of the Author section and built the handover package (step 6). Of the 19 claims, 11 are blocked because the paper's own recordings are not public. Of the 8 tested on the MAP data, 1 is reproduced (resting on one reading of an open method detail), 3 are partially reproduced and 4 are not reproduced. The entry is locked, `check` passes with 0 errors and the notebook ran cleanly from a fresh environment. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| own-recordings-cohort, fig1i, fig2c, fig2e, fig2f, fig2gh, ed2f, fig3c, fig3d, ed3, ed3a (11 claims) | Blocked: data_missing |
| map-session-selection | Not reproduced |
| fig4b-medulla-selectivity | Partially reproduced (assumed) |
| fig4c-alm-null-potent-similar | Partially reproduced (assumed) |
| fig4c-medulla-null-smaller | Reproduced (assumed: only under readings B2 and V2) |
| fig4d-alm-predicts-medulla-null | Not reproduced (assumed) |
| fig4d-decoding-asymmetry | Not reproduced (assumed) |
| fig4e-medulla-null-lower-dimension | Not reproduced (assumed) |
| fig4f-medulla-null-not-spanning-alm | Partially reproduced (assumed) |

No outcome changes across the five seeds.

**2. What was found**

- **Version:** I pinned 0.231012.2129, the latest published version, because the paper cites the dandiset without a version. The units of the session I compared are identical in 0.230822.0128.
- **Session selection:** only units classified `good` carry a brain-region label (`anno_name`): 69,453 of 272,227. With these labels the paper's rule gives:
  - 17 bilateral ALM sessions from 9 mice; the paper has 20 from 10.
  - 5 ALM and medulla sessions from 4 mice, with 300 ALM and 340 medulla units; the paper has 16 or 11 sessions, with 604 and 724 units.

  I recorded this as a major finding about the data.
- **Labels:** 1,852 units have no `classification`. `unit_quality` has no description, and the tracking data are stored as 'a.u.' but hold pixel positions.
- **Clocks:** spikes, video and trial times agree in all 22 sessions.
- **Decoding:** the method as written (ridge, lambda 0.01, 9 lagged smoothed bins) gives held-out R2 far below zero, because the lagged predictors are nearly collinear (condition number about 1e6). Larger penalties are shown only as variants.
- **Medulla selectivity:** far higher than the paper's (34, 53 and 87% against 7, 21 and 49%).

Assumptions, recorded as deviations:
- Ignore, photostimulation and early-lick trials are left out.
- The movement threshold is Otsu's threshold on log speed, since the paper set it by hand.
- Keypoints are smoothed over 3 frames before taking speed; unsmoothed, the tracking jitter hides movement.
- The dimensionality shuffle uses 100 shuffles on every 4th bin, where the paper uses 1000, to fit the time limit.

Questions for the paper's authors, recorded as `methods_unavailable` findings:
- How R2 and the lambda were computed for the cross-region decoding.
- How the movement threshold was set, and whether movement runs shorter than 100 ms count as moving.
- Which trials were used, and which 'good' label selects units.
- How variance explained is normalized, and which dimensionality measure Figure 4e uses.
- How the z-score handles units that are nearly silent at baseline (values reach 213 s.d.).

I also recorded a `paper_inconsistency`: 16 against 11 sessions, 1116 against 2016 units, and 40 against 45 ms.

I asked no reader questions. DANDI:001472 holds the data of the authors' earlier paper, not this one, so the paper does not need listing on it.

**3. Where the protocol was unclear**

1. The claims file's readings multiply into dozens of combinations. I ran each reading against the main one, one factor at a time, and recorded that.
2. Whether a "variant" named in the claims file can decide an outcome. The example.m z-score fully matches fig4c-ALM; I did not let it decide.
3. A criterion where neither the "reproduced" nor the "not reproduced" branch applies (fig4c-ALM: p ≥ 0.05 but the means are off). I chose partially reproduced.
4. Reader step 3 says "reproduced under any reading", while author step 1.6 says to adopt the best-supported reading. For fig4c-medulla I followed the criterion and set `assumed: true`.
5. Per-claim seeds when several claims share one computation (the subspace fits). I used fig4c-ALM's seed for the shared generator.
6. Seed checks for every reading multiply the runtime. I ran them for the main reading and the deciding reading (B2) only.
7. `assumed` when an assumption, such as the trial exclusions, applies to every claim. I marked all tested Figure 4 outcomes except the session selection.
8. During the survey I tried to check the electrode coordinates against the Allen atlas outside the notebook. I dropped it and nothing from it is in the record, as the protocol requires.

**4. Runtime and failures**

The run took about 2.5 hours (02:02 to 04:33 UTC). The notebook takes 35 minutes, which is under the 60-minute limit but over the 10-minute aim; peak memory was about 3.8 GB. Nothing failed in the final run.

Files are in `entries/hasnain-2025/`:
- `reproduce_hasnain_2025.ipynb`
- `map_subspace.py`
- `README.md`
- `entry.yaml`
- `requirements.in`
- `requirements.lock.txt`

The handover is in `executed/hasnain-2025/handover/` and the record is `attempts/hasnain-2025-01.yaml`.
