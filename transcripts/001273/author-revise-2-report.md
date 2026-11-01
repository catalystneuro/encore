The round-2 revision is done. All 17 outcomes are the ones the verifier agreed with, so nothing is under `proposed`. I re-ran the entry with `python tools/entry.py all`: all four notebooks passed, the check reports 0 errors, and the Figure 4, 3C and S1 numbers are the same as in the run the verifier reviewed.

**Outcomes**
- **No outcome changed.** The count is still 2 reproduced, 1 partially reproduced, 2 not reproduced and 12 blocked.
- **fig3c-sustained-firing-2s** is now marked `assumed: true`, as the verifier asked. A deviation states the rule for combining cells: reproduced if the criterion holds in most cells, partial if it holds in at least one cell or its firing parts hold in most. It cites the Figure 3 legend and the Results, and says that judged on any one cell the claim would be reproduced, and on most cells it would not. The notebook's conclusion and summary say the same.
- **fig5, fig6 and threshold-depolarization-estimate**: the blocking reason is now `other` instead of `too_large`, as the verifier gave. The outcome itself is still `blocked`.

**Added**
- **New notebook, `survey_other_dandisets.ipynb`** (about 9 minutes), listed in `entry.yaml` and the README. It reads every file of 001030, 001032 to 001035 and 001271, plus the archive's listing and sizes, so the figures the verifier could not check now come from printed output:
  - the dandiset sizes: 001273 is 10.6 GB and 001274 is 25.0 GB;
  - every file is a 16 x 16 pixel image stack at 3,086.4 frames/s;
  - all 178 image arrays of 001034 are identical to those of 001032, with the same session descriptions under other subject ids;
  - every session of 001032 to 001035 is in NaCl solution;
  - 001271 has 287 sessions from 20 subject ids, 71 of them with TTX.
- **One wording correction from the survey**: the 001035 descriptions give no stimulus duration. So the notes now say "every session of 001032 to 001035 names the NaCl solution" instead of "the 250-ms sessions".
- **Inputs**: the surveyed dandisets are listed under `inputs` with their DOIs.

**Corrected sentences**
- **fig6 notes**: removed the "1,115 s" streaming time and the estimate built on it, which no output printed. The reason is now stated as lack of time, and the sizes cite the survey notebook.
- **README**: 175 of the 181 files form the 22 experiments, and the 6 single files are not used. The data size is now 10.6 GB.
- **figs1** (record and the 001272 notebook): reading (a) finds APs only in neuron 3_20240806, and reading (b) finds none in any neuron.
- **fig4-no-pole-difference** (record and the main notebook's conclusion): no difference under the header readings; the window variant reaches p = 0.046 in 2 of its 8 readings. The text also says the outcome depends on whether the 100 and 130 V runs are among the paper's 19 experiments.
- **Round 2 is recorded** under `verifications`: the verifier agreed with all 17 claims, and each entry gives its reason in its own words and what I changed in reply.

**Not done**
- **figs1**: the outcome still rests on the claims file's 5% level for Di-8-ANEPPS. That question was already in `questions/001273.yaml` for a reader, and I did not change the claim.
- **fig4-no-pole-difference**: the paper's 19 experiments still cannot be identified, so the dependence on the 100 and 130 V runs can only be stated, not resolved.
- **`tools/build_site.py`**: it was already modified before this run started. I did not touch it, and it will go in with the workflow's commit unless someone removes it.

Nothing is committed; the workflow commits the changes.
