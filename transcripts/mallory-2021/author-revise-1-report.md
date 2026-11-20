Revision done. The entry check passes with 0 errors and the handover is rebuilt. Nothing is committed.

Three notebooks were run with `tools/entry.py run`, and all three pass:
- freely moving: 43 min
- main: 51 min
- random-folds: 42 min

Together they are longer than the 2-hour limit on one command, so I ran them in two parts with `entry.yaml` cut down each time, then restored it and joined `result.json`. The check was run separately on the full entry. I wrote the conclusion cells after the runs, in both the source and executed copies; no code or outputs changed.

**Outcomes that changed** (all were blocked in round 1, and the verifier said they were testable):

| Claim | Now | Key numbers |
|---|---|---|
| fig1c-head-direction-cells | reproduced | 58 of 179 |
| fig1c-pitch-roll-cells | not reproduced | 37 and 43, paper 46 and 53 |
| fig1c-pitch-roll-velocity-rare | reproduced | 3 and 5 |
| fig1d-conjunctive-head | partially reproduced | 87 conjunctive; B alone 0.179, outside tolerance |
| fig2-pitch-roll-shapes | not reproduced | quadratic roll is 16 of 41, not a majority |
| fig2a, fig2b | reproduced | no preference under any reading |
| fig2-pitch-roll-stability | reproduced | Kruskal-Wallis P = 0.116 |
| supp4-head (Cohort 1 part) | not reproduced | |
| supp5-head (Cohort 1 part) | reproduced | 3 of 3 medians |
| supp9-eye | partially reproduced | order holds; Bs median 0.159 against 0.13 ± 0.013 |

All the Cohort 1 outcomes rest on one reading of the open fitting details (folds in turn, out-of-range bins dropped) and are marked as assumed. None of the head-fixed outcomes changed.

**What I added or corrected:**
- **Downstream analyses under random folds (problem 3):** every head-fixed claim now also runs in the random-folds notebook. No outcome changes direction. Under this reading fig5bv meets two medians, fig6 linear loses its nasal test, and Ev dot becomes significantly *more* stable than body speed.
- **Preference reading (problem 4):** reading (b) is now the claims file's literal "larger absolute slope". The old reading is kept as a variant. fig6 nonlinear reaches 47 of 78 temporal (P = 0.089) and still fails in all 12 combinations.
- **supp4-eye (problem 5):** the symmetric velocity test is now included. Eh dot reaches 0.933 and Ev dot 0.891; Eh and Ev still fail the 90% bar.
- **Fig. 8 files (problem 2):** the trial tables of the 9 unused files are now printed. They only have columns for times, contrast, gain and reward, nothing about the track or its landmarks. One 6-mouse subset sums to 1621 units, as the verifier found, but that doesn't show which blocks lack landmarks, so fig8c and fig8e stay blocked.
- **Hemisphere:** figshare Dataset 3's field names are now printed. None names a hemisphere.
- **Code excerpts:** the notebook now prints the relevant lines from the linked code. They confirm the log 2 factor in `compute_llh.m`, the −5 baseline and final test, and that folds are assigned after bins are dropped (problem 9).
- **fig6 stability:** a variant on the 134 classified Ev dot cells gives P = 0.029, the same result.
- **fig7ab:** reading (c) is now shown for each of the 10 folds. The full rule holds only in fold 1, and the notes now say the outcome rests on that.
- **Reader question:** the fig7c "bits per spike" misreading is added to `questions/mallory-2021.yaml`.
- **Record:** the verification round, the findings, the README and the summaries are updated.

**Not done, and why:**
- **Clipping reading (2b):** I built its notebook, but it would have taken about 45 more minutes and finished after the 05:54 stop. I removed it, and the notes say this reading was not run.
- **Other readings of the Cohort 1 model:** one reading takes 32 min, so the other three were not run.
- **Still blocked as too large:**
  - the claims that need the Cohort 2 model: about 3 h for one reading, estimated from the Cohort 1 time
  - supp3-head and supp3-eye: about 3.2 h and 3.3 h
  - supp12: one more head-fixed model run, which doesn't fit in the main notebook or the time left
- **Cohort 2 parts of supp4-head and supp5-head:** these use Cohort 1 only. Pitch and roll are only in Cohort 1, so the missing part cannot change either outcome.

The freely moving notebook's peak memory was 12.06 GB, which is close to the runner's limit.
