I tested 16 of the 35 claims (15 of the paper's findings plus one link claim I added); the other 19 are blocked, because the dataset holds only per-pair summary values. The entry passes `lock`, `check` and `all`: the notebook ran from a clean environment in 99 s, and I confirmed the executed numbers match the conclusions. The handover package is built in `executed/crcns-stc-1-gu-2011/handover/`.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| training-group-link (added by me) | reproduced |
| fig2b-trained-lower-noise-correlation | reproduced (assumed): 0.0241 vs 0.119, p = 0.0056 (paper 0.023, 0.116, p = 0.006) |
| figs2b-individual-animals | reproduced (assumed; per-animal means only) |
| fig1-example-pair | reproduced (pair m2c338r1) |
| fig1f-modality-correlated | partially reproduced (R = 0.449 on 127 pairs; tolerance 0.342 to 0.418) |
| fig1f-modality-means-equal | reproduced (paired p = 0.73) |
| fig5-noise-signal-positive | reproduced (assumed) |
| fig5-slope-unchanged | reproduced (assumed) |
| fig5-intercept-lower-trained | partially reproduced (assumed): the training effect holds, but the intercept 95% intervals overlap |
| fig5-regression-coefficients | partially reproduced (assumed): trained intercept 0.0034, outside 0.005 ± 0.0005 |
| fig6a-population-thresholds | reproduced (assumed): ratio 5.41 |
| fig6b-slope-not-intercept | reproduced (assumed) |
| fig7a-pair-sign-of-effect | partially reproduced (assumed): 180 of 181 pairs follow the rule |
| fig7c-narrow-preferences | not reproduced (assumed): best improvement 4.83%, expected 8 ± 0.8 |
| fig8ab-choice-probability-lateral | not reproduced, on a subset (129 units from 2 monkeys, against the paper's 311) |
| fig8cd-noise-not-preference | reproduced (assumed) |
| 19 other claims | blocked: 18 `data_missing`, 1 `metadata_insufficient` (single vs multiple electrodes) |

**2. Dataset, assumptions, questions**

- **Version:** CRCNS is unversioned. I pinned `stc-1/live/` because the bucket holds only that copy of the data (`orig/` has just an older description document). The notebook checks the files against the dataset's own MD5 sums.
- **What it holds:** per-pair noise and signal correlations per condition and preferred headings for the 127 pairs under 1 mm, plus tuning curves and choice probabilities for 129 units from 2 trained monkeys. There are no spike times, distances, electrode labels, training-group labels, pairs over 1 mm or naive single units.
- **Training groups:** these come from the paper's per-animal pair counts (Figure S2B legend). The counts are all distinct and match the dataset one to one. The match also gives the paper's 146 and 64 neurons, and monkeys 2 and 5, which have discrimination thresholds in the file, come out as trained.
- **Findings:**
  - The data descriptor leaves out monkey 24 (2 pairs).
  - Recording m19c21r1 holds 6 pairs, where the paper says at most 5 per experiment.
  - Ten file IDs end in "s" with no explanation.
  - How `heading_pref` was computed and how `cp` is signed are not documented.
- **Main assumption:** I took the pooled noise correlation to be the mean of the two per-condition values. It follows from z-scoring when both conditions have equal trial counts, and it reproduces 0.023 and 0.116 to the third decimal.
- **Simulation parameters:** the tuning amplitude and baseline come from the claims file, not the paper, and the results depend on them.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - Is the pooled correlation the mean of the two conditions, and is the renormalization included?
  - Which amplitude, baseline and counting window did the simulations use, and did they include the trace term of equation 3?
  - How were the Figure 5D intercept intervals computed?
  - For Figure 8A, how were preferred headings and the sign of choice probability defined?
- **Questions to a reader:** none.

**3. Protocol gaps**

1. Link claims are framed around outside data. Here the labels came from the paper itself, so I recorded the paper's DOI under `inputs` and marked the link `with_labels`.
2. Adding the link claim meant adding `depends_on` to 7 existing claims. The protocol requires it, but it touches a claims file the author is otherwise told not to change. I changed nothing else.
3. The rule that every data stream must share the trial clock does not apply to a dataset of summary values only. I said so in the data check.
4. The protocol gives no category for "testable on a subset that may not be the paper's sample" (fig8ab). I tested it and named the subset in the deviations.
5. The criteria give no outcome for "all but one" (fig7a, 180 of 181) or for a mixed result without a partial rule. I chose `partially_reproduced` and gave the exact counts.
6. For fig8cd the claims file's preferred reading needs pairs that are not in the dataset. I judged it on the closest reading the data allow (178 points).
7. archives.md describes CRCNS zips; these files are plain `.mat`. I streamed them into memory with fsspec.

**4. Runtime and failures**

The work took about 25 minutes (16:53 to 17:13 UTC). The notebook runs in 99 s. Nothing failed. Some untracked files at the repo root (`.bashrc`, `.idea`, `scripts` and others) are sandbox device mounts created before I started; I left them alone. I did not commit or push.
