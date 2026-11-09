I've done steps 1 to 6 of the Author section: the entry runs from a clean environment in 5.7 min (`python tools/entry.py all` passes, 0 check errors), the attempt record is written, and the handover is built in `executed/000138-churchland-2010/handover/`. Nothing is committed.

The dandiset holds one session of monkey J (2009-10-06): 500 maze trials over 27 conditions, 162 array units, and hand, cursor and eye position. I pinned version 0.220113.0407 because the paper cites no version, it is the only published one, and the draft holds the same two blobs.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| fig4abc-tuning-correlation-single-electrode | blocked, data_missing |
| fig4d-tuning-correlation-j-array | partially reproduced, assumed (mean r 0.195, Spearman 0.212, p = 0.023) |
| fig4e-correlation-time-course | not reproduced (r is 0.218 at movement onset) |
| results-ap-location-no-effect | reproduced for J-array only, assumed (p = 0.84) |
| supp-preparatory-dimensionality | reproduced, assumed (11 components) |
| fig6-peri-movement-space-best | reproduced (0.351 vs best task space 0.250 and kinematic 0.103) |
| fig6-each-dimensionality | reproduced, assumed (wins 20 of 22 comparisons) |
| fig6-dimensionality-trend | reproduced, assumed |
| fig6-pd-adequate-all-spaces | reproduced, assumed |
| fig6e-summary-rank | blocked, data_missing |
| fig7a-shuffled-space-poor | reproduced, assumed |
| fig7b-window-start-onset | reproduced for J-array only, assumed (ratio 0.908) |
| fig7c-anterior-posterior | not reproduced, assumed (posterior at 0.62 of random halves) |
| fig7d-pd-consistency | reproduced for J-array (higher in every comparison and variant) |
| fig8-oscillator-model | reproduced (simulation) |

**(2) The dataset, assumptions, questions**
- **Coverage:** only J-array can be tested, on 27 of the paper's 108 conditions and 500 trials. The file has 162 units where the paper reports 146, and nothing says whether this is the paper's session. The single-electrode datasets (monkeys A, B, J) and all EMG are missing.
- **Unit metadata error:** every unit references a PMd electrode. The unit ids carry a prefix (1 for 83 units, 2 for 79) plus a channel, and the reference is channel minus one for both prefixes, so one array's units point at the other array's electrodes. Electrode coordinates are all NaN.
- **Smaller findings:**
  - Hand data are resampled to 1 kHz within trials only (the paper tracked at 60 Hz).
  - Eight trials have a delay of 0 ms or less.
  - The paper gives 2166 trials per neuron in the Results and 2155 in the Methods.
- **Assumptions:**
  - Array membership comes from the id prefix, with prefix 1 taken as PMd.
  - Trials are selected by correlating the concatenated velocity profile with the condition's mean profile. Requiring each axis separately keeps 81% of trials and leaves 2 or 3 in some conditions; the paper says about 90%.
  - Movement onset is the dataset's own `move_onset_time`.
  - Tuning is the range of condition means. The SD reading leaves only 6 of 162 units.
  - The PCA space is computed once from all conditions; the paper describes leaving a condition out only for the PD fit.
  - All units enter the T-matrix, and performance is averaged over units.
  - For Fig 7C, the upper-limit space includes the unit being fit.
- **Readings run:** 2048 combinations of readings for Figure 6 and 7B, one at a time for 7A, 7C and 7D.
- **Questions for the paper's authors:** four, recorded as `methods_unavailable` findings: space computed once vs refit; the proto-trial and its window; the tuning measure and onset method; the Fig 7C upper limit.
- **Questions to a reader:** none.

**(3) Where the protocol was unclear**
1. With many open details, it doesn't say whether to run the full product of readings or one at a time. I ran the full grid where it was cheap (Figure 6, 7B) and one at a time elsewhere, and said which in the notebook.
2. It doesn't say what outcome a claim gets when it spans four datasets and only one is in the dandiset. I judged the testable part and listed the missing datasets as deviations; I did not mark these "partially reproduced".
3. `measured` must give one value per expected value, but fig7b's second value (monkeys A, B) cannot be measured. I gave one number and said which expected value it matches.
4. It is unclear whether an author-added reading, one the claims file doesn't name (here the per-axis vs concatenated velocity test), counts under "reproduced under any reading" or under the step 1.6 assumption rule. I treated it under step 1.6.
5. fig8 is marked `with_inputs` but uses no outside input, so `inputs` is empty; the protocol doesn't cover this case.

**(4) Runtime and failures**
- About 45 minutes of the 5 hours (19:45 to 20:27 UTC). The notebook takes 5.5 to 5.7 minutes.
- Development bugs, all fixed before the final run: hand samples are not on a continuous grid; `.combine` is a pandas method; numpy booleans in an object column summed as OR and printed 1 where 2 was right.
- An empty `.claude` directory appeared inside the entry, and stray dotfiles appeared at the repo root; I didn't create them. Removing the directory was denied for lack of an approval surface. Git ignores empty directories, so it won't be committed, but the root dotfiles will be unless someone removes them.
