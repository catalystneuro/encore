I wrote the claims file at `claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml`. The quote checker reports 42 claims, 41 quotes, 85 statistical values and 0 problems.

**Text read.** The version of record (Nature Communications, CC BY), main text, Methods and the full Supplementary Information: Supplementary Figs. 1 to 8, Tables 1 to 4 and Note 1. The four supplementary tables are images, so they are missing from the `.txt`. I read them from the supplement PDF:
- Table 1: demographics by age group.
- Table 2: ROI centers and sizes.
- Table 3: event times, durations and peak TRs.
- Table 4: correlations between each age group's timecourse and the adults'.

The earlier run stopped because the supplement was missing; it is now there. No code is linked: the paper says it is "available from the corresponding author upon request", so code settles nothing.

**Counts.** 42 claims: 41 with quotes and 1 inferred (Supplementary Table 1). 33 have statistics, 30 have expected values, and all 42 have criteria. Ten are claims of absence, each judged on the paper's own test.
- Three need outside inputs: the face and scene parcels of Julian et al. 2012, and the hand-coded events of Jacoby et al. 2016.
- One is untestable here: the replication sample of 20 adults was never deposited (`data: elsewhere`).

**Details the paper leaves open, with the readings named:**
- **O1, ROI extent:** Table 2 sizes are 142 to 382 voxels, smaller than a full 9 mm sphere for some regions. Readings: (a) deposited ROI masks, (b) full spheres, (c) spheres limited to voxels with data.
- **O2, artifact regressors:** (a) one indicator per artifact timepoint, (b) a single regressor.
- **O3, TRs used for inter-region correlation:** (a) all 168, (b) TRs 11 to 168.
- **O4, scale of regression b values:** (a) z-scored, (b) raw units. Criteria judge regressions on t, p and sign, so this does not change outcomes.
- **O5, per-timepoint threshold in the reverse correlation:** (a) p < .05 uncorrected, (b) p < .01 uncorrected, (c) FDR-corrected.
- **O6, span of z-normalization:** (a) TRs 11 to 168, (b) all 168.
- **O7, child event magnitude:** taken from the z-normalized timecourse or from the timecourse before normalization.
- **O8, partial Kendall tau:** the ppcor form, a standard choice.
- **O9, Tukey HSD diffs:** they are on a standardized scale (for example 1.2 against a raw mean difference of .20). Readings: z-scored over the 3- to 5-year-olds, or raw. Judged on p.
- **Claim-specific readings:**
  - "Remaining ToM items" means either the 18 items that are not false-belief items or the full score.
  - "Such as" in the claim that homologous pairs correlate most strongly in 3-year-olds: the top pair in each network, or the homologous pairs ranking highest.
  - Which pairs count as bilateral.
  - For the overlap permutation, the stated non-event counts (125 and 116 TRs) do not add up to 158 TRs with the event totals. Readings: (a) 158 TRs with 124 and 115 non-event TRs, (b) 125 and 116 as stated (159 TRs).
  - For the hand-coded events: included in coded Pain events, or in any coded event.
- **My own inference:** Table 3 gives stimulus times and peak TRs but no rule linking them. With onset TR = stimulus seconds / 2 + 8, every event's peak falls inside its event. The file labels this as a reading of the table, not a statement of the paper.

**Missing from the paper:** the replication adults (n = 20) are not deposited and no archive is named, so `replication-sample` cannot be tested. The 3-year-olds' mean within-ToM correlation is printed "21(.02)"; I recorded it as .21. The paper reports no test for the 3-year-olds' lack of anti-correlation, so that claim is judged on the reported mean, with a one-sample t-test shown as a variant.
