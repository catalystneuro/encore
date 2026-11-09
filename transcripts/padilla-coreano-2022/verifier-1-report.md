**Verifier report, round 1: Padilla-Coreano et al. 2022 on DANDI:001749 (0.260311.1727)**

The claims file has 46 claims. The notebook tests 6 and blocks 40. Its cell 0 table accounts for only 45, because it says the single-unit group has 21 claims when the claims file has 22.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| ed5b-rank1-wins-most | reproduced | Cell 26: rank 1 won the highest share (90.9%), the same under both tie readings and all variants. Competitions per rank are 12/11/15/15 against 12/12/15/14 expected, all within tolerance. 17 of 53 files have no result, but even in the worst case rank 1 (10 of 12, 83.3%) still beats rank 4 (12 of 15, 80%). |
| ed5c-rewards-not-different | partially_reproduced | Cell 28: the rewards part is a claim of absence and holds (paired t p = 0.505 over files, 0.498 over sessions; ≥ 0.05 under every variant). The body-weight correlation was not tested: the asset metadata has no weights, which I checked through the API. |
| ed5d-subordinates-slower-latency | reproduced (fragile) | Cell 30: latency from port entries, sub slower, rank-sum p = 0.0196 (0.0204 for the next-entry variant), KS p = 0.0036. Latency from the hand-scored labels gives rank-sum p = 0.206, and the per-mouse test gives p = 0.055. See problem 3. |
| ed5e-port-occupancy-not-different | reproduced | Cell 32: paired t p = 0.327 over files, 0.284 over sessions, both ≥ 0.05. |
| ed5f-dominants-displace-more | reproduced | Cell 34: dom higher. Whole competition p = 0.0051, tone p = 0.0013, n = 13 sessions (the paper has 32 and 31). |
| ed5g-time-displaced-not-different | reproduced | Cell 36: paired t p = 0.359 (tone only, p = 0.512), ≥ 0.05. |
| fig1b, fig1c, ed1d, ed1g | blocked: data_missing | All 53 NWB files are implanted mice (cohorts ephys, chrimson, BLA). The unimplanted cohort is not in the archive. |
| fig1e-alphatracker-precision | blocked: data_missing | No annotated evaluation frames. The archive holds only 53 NWB files and 52 mp4 videos. |
| fig1i, ed5j, ed5k (HMM-GLM) | blocked: other (not attempted, testable in part) | The notebook's reason, "not runnable", is not one of the allowed reasons and no cell explains it. The input is present: the raw 32-channel signal in every file, from which the Methods 17 multi-unit rates are derived (sorted units are not needed). The labels match the paper's 965 trials (cell 19: 487 dom and 478 sub trials, against the expected 482 and 478). The behaviour-to-neural offset is estimable in 23 of the 34 labelled files (cells 13, 19). See problem 1. |
| ed7b-distance-by-trial-type-not-rank | blocked: metadata_insufficient (accept) | Cell 21: there is no port location, the poses do not say which mouse is the subject, and poses are entirely missing in 22 of 43 files. A partial route exists but was not tried (problem 7). |
| fig2a, ed6d, fig2b-subordinates-longer-trajectories, fig2b-subordinates-larger-variance, ed6c, ed6b, ed6ef, ed7c, ed7de, ed7f, ed7hij, fig2c-svm-decodes-rank-and-outcome, fig2c-predicts-before-trial, ed8bc, ed8d, ed8e, ed8fgh, fig3a, fig3b, fig3c, fig3d, ed9cd (22 claims) | blocked: metadata_insufficient (accept) | Cells 17 and 18: the files hold 5,879 clusters, all labelled "unsorted", against the paper's 998 curated cells. No rate rule comes near 998. On top of that, spike times are wrongly scaled (×1.5, cell 12) and offset from behaviour by an unknown amount in each session (cell 13). The alone part of ed8fgh is also data_missing. |
| ed8ij, fig2e, ed9b | blocked: data_missing (accept) | No alone trials: tone tables start at 60 s with the competition schedule (cell 7), and spike-to-entry offsets are only seconds (cell 13). These claims would also be blocked by the unit-curation problem. |
| fig4a, fig4b-phototagged-counts, fig4b-lh-stronger-reward-excitation, ed10c, fig4d, ed10ek | blocked: data_missing (accept) | No ex vivo data, no light pulses and no ChR2 or eYFP cohort. The API's measured-variable list has no optogenetic series. The notebook never shows a file's contents to back this up (problem 5). |

### B. Problems

1. **[affects a conclusion] HMM-GLM block not supported (cell 0; no cell attempts it).**
   - Methods 17 use multi-unit rates thresholded at 4 SD on the raw signal, which is in every file.
   - The 34 labelled files hold exactly 965 trials.
   - The helper's `clock_checks` already estimates the offsets that would align the raw signal with the behaviour clock.
   - At least the 23 labelled files with a clear offset peak could have been run (reading the trial windows is about 0.5 GB per file).
   - So fig1i, ed5j and ed5k could have been tested at least in part.
2. **[affects a conclusion] The 52 behaviour videos are never used or mentioned (cell 0 says "53 NWB files").** The dandiset description says the LED in the video is on during the tone so that neural and behavioural data can be aligned. That is a direct substitute for the missing `video_gap` variable in every BLA and chrimson file, which bears on problem 1 and on cell 16's "cannot be estimated".
3. **[affects a conclusion] ed5d depends on aligning port entries with label trials (cell 30, `entry_latency`).**
   - Label trial *j* is taken as tone *j*, and port entries are read on the tone clock.
   - Files whose entries barely agree with their labels (cell 9) are kept: chrimson1-1-1v2 r = −0.03, BLA2-1-1v4 −0.02, BLA2-4-3v4 0.01, BLA1-3-3v4 0.12, BLA2-3-3v4 0.18.
   - The last two are the 25-trial session whose two views agree on only 76% of bins.
   - The label-based latency, which needs no such alignment, does not meet the criterion (p = 0.206).
   - Trial counts are 211 dom and 189 sub, against the paper's 326 and 358, with the imbalance reversed.
   - At p = 0.02 the outcome could flip if these files were excluded.
4. **[does not affect a conclusion] ed5c weights.** "Body weights are not in the dandiset" is stated without any output. I confirmed that the API asset metadata has no weight, but the files' own subject records were not shown.
5. **[does not affect a conclusion] "No alone session, light pulse or stimulation" (cell 0) is asserted without output.** No cell prints the groups inside any file (intervals, stimulus, acquisition, processing).
6. **[does not affect a conclusion] Reading (a) for ed5c and ed5e (cells 28, 32) double-counts sessions.** It treats both files of the 14 two-file sessions as separate pairs, though they are mirrored views of one session, so n = 34 is not independent. For claims of absence this extra n works against the claim, so it is conservative.
7. **[does not affect a conclusion] ed7b: a partial route was not tried.** The port location could be estimated from poses during the subject's port entries in the 21 chrimson files with poses, and the subject identified by the dye pattern in the videos. Without the hand-marked port location the block is defensible.
8. **[does not affect a conclusion] Two variants test nothing new.**
   - ed5f's "competitor's view" (cell 34) reads the same bins as the pusher's view and gives identical numbers.
   - The two switch rules in `trial_outcomes` (cell 24) give identical counts, because labels change only on whole seconds.
   - The main results do not rest on either variant.
9. **[does not affect a conclusion] ed5f "whole competition" is only the labelled −2 to +12 s of each trial, not the whole session**, and n = 13 against the paper's 32. Both tests are still p < 0.01.
10. **[does not affect a conclusion] Delivery time.** The files give 0.49 s after tone onset, the Methods 2 s. The notebook takes 2 s as the main reading and runs 0.49 s as a variant; results do not change.
11. **[does not affect a conclusion] Claim count.** Cell 0 lists 45 of the 46 claims (21 single-unit claims instead of 22; ed8fgh is the likely omission).

The helper functions behave as documented on synthetic label arrays: `trial_outcomes` (main and both variants), `latency_to_port`, `push_success`, `competitor_push_success` and `runs`. Every tested number comes from the loaded data. I found no place where the claims file misreads the paper in a way that affects the tested claims.

### C. What I could not check, and the output that would settle it

- **Body weights (ed5c):** a print of each file's subject record (`general/subject`), including any weight field.
- **Alone, phototagging and opto data, and `video_gap` (problem 5):** the group tree under intervals, stimulus, acquisition and processing for one file per cohort.
- **Unit curation:** the full column list of the units table, to show no column other than `quality` holds a curation label.
- **ed5d robustness:**
  - the label-based latency restricted to the same trials as the entry-based one;
  - the entry-based test with files below r = 0.3 (cell 9) excluded;
  - for files with fewer label trials than tones, a scan of trial offsets in the label-to-entry correlation.
- **HMM-GLM feasibility:** an LED-based alignment check from the video, or multi-unit rates aligned with the estimated offsets for the 23 files, even if only for a GLM-against-chance check.
