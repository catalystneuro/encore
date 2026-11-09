The attempt is written and its checks pass. Of 42 claims, 15 are reproduced, 12 partially reproduced, 13 not reproduced and 2 blocked. `entry.py check` reports 0 errors, the notebook ran clean in 147 s (`entry.py all`: pass), its outputs match my development run line for line, and the handover is built in `executed/openneuro-ds000228-richardson-2018/handover/`. Nothing is committed.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| participants, supp-table1-behavior-by-age, beh-tom-age, beh-tom-dccs, beh-fb-groups, beh-fb-tom, beh-fb-age, beh-fb-dccs | reproduced |
| motion-child-adult, motion-not-age-tom, motion-not-fb | reproduced |
| irc-adult, irc-adult-vs-child, irc-control-networks, irc-williams, irc-3yo-not-anticorrelated, irc-3yo-nonbilateral, irc-tom-behavior | partially reproduced |
| irc-age-within, irc-age-across, irc-3yo-distinct | not reproduced (by Rule S: the effects are significant at .05 but miss the paper's p bounds, and the values are out of tolerance) |
| irc-3yo-homologous, irc-fb-within, irc-fb-within-dccs | not reproduced |
| irc-tom-behavior-age, irc-fb-across | not reproduced, resting on an assumption |
| rc-events, rc-overlap, rc-child-adult-timecourse, maturity-across | partially reproduced |
| rc-3yo-events | partially reproduced, resting on an assumption |
| supp-table4-other-networks, rc-age-events, rc-t04-tom, face-rc | not reproduced |
| rc-fb-no-difference, maturity-within | reproduced, resting on an assumption |
| maturity-tom-behavior, maturity-fb, face-overlap | reproduced |
| replication-sample, hand-coded-events | blocked (`other`) |

**2. The dataset**

- **What it holds.** Snapshot 1.1.1 holds the paper's own preprocessed images (`*_swrf_bold`), the artifact and CompCor regressors, and every ROI mask, including the face, scene, M1 and V1 regions. The masks have the sizes of Supplementary Table 2. I pinned 1.1.1 because the claims file names it, it is the latest snapshot, and its CHANGES file says it only updated the citation.
- **What matches.** Every behavioural number is recovered exactly from participants.tsv. The artifact counts match the Methods, and the artifact flags line up in time with spikes in the image data.
- **Main finding.** With the paper's preprocessed data and the pipeline the Methods describe, the inter-region correlations come out higher within networks and less negative across them. In adults they are .604, .398 and -.051 against the paper's .48, .35 and -.17. Several event-level and false-belief results do not come out as reported.
- **Minor metadata problems.**
  - The voxel-size counts by age group differ from the Methods (2 and 21 participants against 3 and 20).
  - The column is misspelled "Voxel slize".
  - The "None" slice-gap level is stored as an empty value.
  - 19 participants have incomplete face-ROI coverage, where Supplementary Fig. 4 counts 17.
- **Assumptions**, each recorded as a deviation and asked of the paper's authors as a `methods_unavailable` finding:
  - The inter-region correlations use all 168 TRs and one regressor per artifact timepoint, as in the deposited files.
  - The z-normalization spans all 168 TRs.
  - Child event magnitudes come from the z-normalized timecourse.
  - The high-pass filter is SPM's cosine filter.
- **Questions to a reader:** none.

**3. Where the protocol was unclear, wrong or missing something**

1. replication-sample is marked `data: elsewhere` with no archive, because the sample is public nowhere. The protocol would block it as `data_missing`, but the checker rejects that reason for `elsewhere` claims. I used `other` and explained in the notes.
2. The Jacoby et al. hand coding exists only in a zip on the Saxe lab website, with no DOI or commit. The protocol has no block reason for "public but cannot be pinned", so I used `other`.
3. The claims file treats the face and scene parcels as outside input, but the dataset holds them. I used the deposited copies, recorded that as a deviation, and left the claims' `data: with_inputs` unchanged since I may not edit claims.
4. Rule S counts a test that misses the paper's p bound as a failed test, even when the effect is significant in the same direction. This turned three claims into "not reproduced". I applied it as written and gave the effect sizes in the notes.
5. Several criteria (irc-williams, face-rc) define only the "reproduced" outcome. For irc-williams I used `partially_reproduced` for an effect that holds in part, under the protocol's general definition.
6. The data-check rule assumes trial tables, and this movie study has none. I checked timing in two ways: the ROI signal spikes at isolated artifact timepoints against shifted ones (6.45 against at most 2.6), and the ToM-against-pain event contrast falls when the event labels are shifted.
7. Readings that change an absence claim's outcome fall between two rules: "absence is judged on the paper's test alone" and author step 1.6. I followed step 1.6 and marked those outcomes as resting on an assumption.

**4. Runtime and failures**

The whole run took about 32 minutes (16:10 to 16:42 UTC). Extracting the ROIs takes about 95 s and the notebook 147 s in total. Nothing failed. The one notebook warning is a pandas deprecation notice. Untracked dotfiles (`.bashrc`, `.gitconfig`, `.idea`, `scripts` and others) appeared at the repository root. I did not create them on purpose and left them in place; they should not go into the commit.

Sources: [Saxe lab localizer page](https://saxelab.mit.edu/theory-mind-and-pain-matrix-localizer-movie-viewing-experiment), [Jacoby et al. 2016](https://www.sciencedirect.com/science/article/abs/pii/S1053811915010472)
