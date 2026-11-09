The claims file is ready for an attempt. I made nine corrections and left three questions open.

**Checker result** (the same before and after my edits): `claims/crcns-fcx-3/10.3389-fnsys.2018.00065.yaml: 17 claims, 17 quotes, 17 statistical values, 0 problems`

**Changes, by claim:**
- **Shared rule S2 (cluster test):** the paper doesn't say how an electrode is counted when it falls in significant clusters of both signs. Figures 2A and 3A give each electrode one colour. I named two readings: (a) it counts for both signs; (b) it counts for the sign with the larger summed t.
- **Shared rule P1 (PSI):**
  - The paper's "raw trial-wise mean" can also mean each segment's own temporal mean, so I added that as reading (c).
  - The paper doesn't say whether PSI comes from cross-spectra averaged over trials or is computed per trial. The Figure 4A legend ("mean ± SEM per subject across all trials") allows the per-trial reading. Both are now named.
- **trial-counts:** the statement said subjects "made" 17 incorrect responses, which assumes the count is over all 120 trials. It now says they "had 17 ± 8 incorrect trials", which leaves both of the criterion's readings open.
- **power-difficulty-subjects:** the criterion read "the same subjects" only as an exact match of the two groups. The text also allows the one-way reading (every subject with an identity effect was slower and less accurate on identity trials). Both are named, and the reverse direction is reported.
- **power-low-frequencies:** the criterion now says plainly that its band comparison and local-maximum rule are this file's reading of "most prominent" and "distinct", not the paper's method. Identity > effects have negative t, so densities are compared in absolute value.
- **fig4c-alpha-beta-shift:** the source pointed to paragraph 3; the quoted text is paragraph 2 of Task-Induced Effects.
- **fig5a-identity-direction:** the paper labels the values "identity > spatial" and "identity < spatial", so they could be identity-trial PSI z or the identity minus spatial (or temporal) difference. Both readings are now named.
- **fig5a-spatiotemporal-bidirectional:**
  - I removed the reading of "all" as "the reported epochs only", because the paper says "throughout the processing interval".
  - As a claim of absence, it is now judged on one measure: the grand mean over subjects, which is what Figure 5A plots. The other averaging methods are shown as variants.
  - The 1.96 threshold is now cited to Time-Resolved PSI, where the paper defines bidirectionality.

**Still open:**
- The paper's analysis scripts are among the dataset's files, so I did not read them. The author may use them to settle the open details and should say so.
- The paper doesn't say which electrodes count as neighbours in the cluster tests. This affects the ERP claim and the power claims; the existing readings in S2 stand.
- The 1,129 same-hemisphere pairs can't be checked against Table 1, because S1, S2 and S4 have electrodes in both hemispheres and the table gives no per-hemisphere counts.

The paper's main findings each have a claim, and no claim comes from anything but this paper. The `checks` entry is recorded with `ready: true`. Nothing is committed.
