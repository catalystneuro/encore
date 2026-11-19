I've finished steps 1 to 6 for the blind repeat attempt on markowitz-2023 (DANDI:000559, version 0.261113.1911). Both notebooks ran cleanly through `tools/entry.py all`, `check` reports 0 errors, and the verifier handover is in `executed/markowitz-2023/handover/`. Of the 44 claims, 13 are reproduced, 7 partially reproduced, 7 not reproduced and 17 blocked. Nothing is committed.

One accidental exposure to report. The dandiset's own release notes for 0.261113.1911, which I read while listing the archive metadata in step 1, say the files were corrected "to fix problems found by a reproduction attempt" (catalystneuro/datta-lab-to-nwb issue #111) and list those fixes. I did not open the issue or look for that attempt anywhere else.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| ed2a-syllable-repertoire | reproduced (36 syllables, median 400 ms, mean 561 ms) |
| fig1e-velocity-timescales | partially: transient rate holds; amplitude is never positive |
| ed3c-keypoint-velocity | partially: 2D r −0.170 matches; forelimb r −0.026 misses −0.02 |
| fig1f-syllable-vs-movement-onset | reproduced under reading (b) (14/14 mice, P = 0.00012); reading (a) points the other way; rests on an assumption |
| fig1f-dip-then-peak | reproduced (rests on the claims file's assumed window) |
| fig1h-syllable-dlight-differs | partially: P < 1e-37, but H is 275 to 289, against 209 ± 21 |
| fig1j-weak-kinematic-correlation | reproduced (all \|r\| < 0.08; bound of 0.3 is the claims file's assumption) |
| fig2b, fig2i, fig2b-across-experiments | reproduced (r 0.18 to 0.20, P ≤ 0.002) |
| fig2e-dlight-predicts-future-usage | reproduced at every n from 10 to 390 |
| fig2e-not-autocorrelation | partially (neither of the criterion's two cases applies; a judgment) |
| fig2g-usage-crosscorrelation | partially (P = 0.039); seed-sensitive (one of five seeds gives 0.054) |
| fig2h-specific-to-syllable | not reproduced (offsets −1 and +1 are also significant) |
| ed7-dms-fewer-transients | reproduced (U = 100) |
| ed7b-dms-transient-shape | not reproduced |
| ed7d-dms-smaller-peaks | not reproduced |
| fig3e-optoda-learning | not reproduced (P = 0.110) |
| fig3f-cumulative-counts | not reproduced (P = 0.062) |
| fig3e-learner-count | not reproduced (7 learners against the paper's 9) |
| fig3h-stim-post-correlation | partially (learners r = 0.868, but controls are also significant, P = 0.025) |
| fig3jk-post-predictable | partially (positive ratios, but both 95% intervals include 0) |
| fig3i, fig3l, ed10e | reproduced |
| ed10i-no-place-preference | reproduced on the criterion's tests; the statement's experiment-wide part fails (P = 0.005) |
| fig3m-long-stim-velocity | not reproduced |
| fig2a, fig3c, fig4i | blocked, data_missing |
| fig1l | blocked, too_large (estimated 83 to 238 h) |
| ed10d | blocked, metadata_insufficient |
| fig2k, ed6b, ed6e, ed7-dms-no-usage-prediction, ed7e, fig4b, fig4c, fig4f, fig4h ×2, fig5, ed10-target-specific | blocked, other (not run in time, or depend on a claim that was not) |

**2. Dataset, assumptions, questions**
- **What is missing or differs from the paper:**
  - The food-reward sessions, the calibration sessions, and the 2-s and 3-s dLight+ChrimsonR stimulation sessions are absent.
  - There are 10 DMS mice where the paper has 8, and 75 DMS experiments where it has 64.
  - 124 photometry-session files have behaviour but no photometry signal: 92 DMS, 22 dLight-only DLS and 10 dLight+ChrimsonR.
  - There are 145 DLS baseline experiments, against 216 in Fig. 1b.
- **Errors and gaps in the files:**
  - The `OptogeneticSeries` description says onsets are recorded as 1, but the values are 0.01 W.
  - The release notes say stimulated detections equal light onsets; in 60 of 516 stimulation files they do not.
  - One dlight-chrimson-6 file has a dF/F of up to 10,804% and is not flagged as excluded.
  - The keypoint reference frame is "TBD".
  - The up or down direction of the velocity-modulation experiments is stated only for 4 of 9 mice.
- **Clocks:** the clock checks are consistent with a shared clock for photometry, syllables and detections.
- **Assumption:** movement initiations use the changepoint derivative per second. Taken per frame, as the Methods can be read, no peak reaches the height of 1. This affects fig1f and ed7d.
- **Questions for the paper's authors:** two, recorded as `methods_unavailable` findings: the units of the movement-initiation score, and which quantity Fig. 1f compares.
- **Questions to a reader:** none.

**3. Protocol problems**
1. The dataset's own archive metadata can reveal an earlier attempt, which the blind rule does not anticipate. I report it here.
2. There is no `blocked_by` reason for claims never started because time ran out (`too_large` covers only computations that were cut off). I used `other` and said so in the notes.
3. With 1,000 shuffles the smallest empirical P is 0.001, so a Holm correction over many tests (120 bin sizes in fig1e) can never pass. I used a normal approximation for those code variants and recorded it.
4. Running every random analysis under five seeds multiplied the runtime beyond the budget. I ran it for fig2g, fig3h and the main fig1h readings and recorded the others as deviations.
5. Reader step 3 says a claim is reproduced "under any reading", even when another reading gives the opposite direction (fig1f). I followed it, marked the claim as resting on an assumption, and asked the authors.
6. fig2e-not-autocorrelation's criterion has gaps: the result fell outside both of its cases, so I judged it partially reproduced and said so in the notes.
7. Testing 46 claims in five hours is not feasible, and the protocol gives no guidance on which to prioritise. I chose the cheaper analyses first.
8. `docs/archives.md` could note that h5py serialises threads. The metadata survey took 32 min with 24 threads and about 2.5 min with processes.

**4. Runtime and failures**
- The run took about 3 h 25 min, from 17:19 to 20:42 UTC.
- The final notebooks take about 25.5 min (photometry) and 3.7 min (Opto-DA), with peak memory around 3 GB.
- **Development failures, all fixed before the final run:**
  - A first fig1j version took 26 min, so I cut it to 5 cross-validation repeats and a plain Pearson shuffle null; this is a recorded deviation.
  - The fig2g non-overlapping-window lags skipped zero.
  - Opto-DA light onsets were read wrongly, because the values are 0.01 W, not 1.

Files are in `entries/markowitz-2023/`:
- README.md
- entry.yaml
- requirements.in
- requirements.lock.txt
- markowitz.py
- photometry.ipynb
- optoda.ipynb

The record is `attempts/markowitz-2023-02.yaml`.
