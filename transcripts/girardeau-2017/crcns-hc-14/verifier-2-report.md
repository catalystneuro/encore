**Round 2 verification: Girardeau et al. 2017 (doi:10.1038/nn.4637) on CRCNS hc-14**

Counts come from the claims file and the attempt record: 38 claims and 38 outcomes. The record has 35 reproduced, 2 partially reproduced and 1 not reproduced; 23 outcomes carry `assumed: true`.

## 1. Outcomes and assumptions

I agree with all 38 stated outcomes. Every assumption is stated, in the deviations and in the Result headings. Four groups need comment.

**Air puff location** (fig1b-dz-speed-anova, fig1b-dz-speed-posthoc, fig1b-speed-ratio, figs1b-ratio-each-rat, fig1c, airpuff-location-no-bias). The assumption is stated and defensible, but it is not clearly the better choice.
- In 5 of the 6 sessions that have an `airpuffloc` file, the estimate lies past the file's location, with a median of 7.3 cm (cell 17). So the main reading uses a location known to be biased.
- The correction rests on 6 sessions, all from Rat08.
- With the corrected location and all samples (cells 23, 26, 29):
  - fig1b-speed-ratio would be partially reproduced.
  - fig1b-dz-speed-posthoc and figs1b-ratio-each-rat would be not reproduced.
- The record says this for each claim.

**REM column** (fig2c-bla-pyr-higher-in-sleep, fig2c-bla-interneurons). The assumption is now well supported. Epochs decoded as column 5 give pair correlations that follow the table's REM columns (r = 0.78 and 0.81) and not its NREM columns (r = 0.09) (cell 99).

**Decoded NREM.** This is a reasonable assumption and it is validated:
- pair correlations against the table's NREM columns, r = 0.88 and 0.90;
- per-session EV − REV of 3.13% against the table's 3.21%, Spearman 0.92 (cell 99);
- decoded minutes against the minutes implied by StatesFR, median ratio 0.95, Spearman 0.92 (cell 98).

The decoder rebuilds the authors' labels from rates those labels produced, and the record says so. Four outcomes hold under the main decoder only:
- **fig3c-decay.** Reproduced only under the main decoder. The table's pre-NREM gives partial (window 3 p = 0.067), 30-s smoothing gives partial, and the immobility substitute gives not reproduced (cells 101, 145). The sessions with EV > REV in the first window number 17, against an expected 19 ± 1.9. The criterion lists only the three means, so I accept "reproduced", but this is the weakest outcome in the attempt.
- **fig3d-pir-reactivation:** NREM p = 0.042, and p = 0.094 with the immobility substitute.
- **fig6a-safe-trajectory-no-reactivation:** p = 0.060, and p = 0.048 under both variants.
- **fig6b-airpuff-greater-than-safe:** p = 0.035, and p = 0.15 with the immobility substitute.

**Decoded REM** (fig3d REM, fig3e REM, figs4-intra-structure-rem-absent). The assumption is stated and reasonable. Decoded REM is less faithful than decoded NREM: per-session EV − REV against the table's REM has Spearman 0.71, and 0.53 with 30-s smoothing (cell 99). These absence outcomes are therefore weaker evidence than the NREM ones.

## 2. Sentences the printed outputs do not support

- **Cell 13** (markdown, stale): "Rat08's CeN and piriform shanks are only coded by colour in StructureMapping.ods, which is not read here". Cell 14 reads the ods and prints its Rat08 labels.
- **Cell 11** (code comment, stale): "against correlations over the substitute NREM periods". `d["nrem"]` is now the decoded NREM.
- **Cell 146, Summary:** "Several outcomes on them sit near p = 0.05 and change with … : fig3c-decay, fig3d-pir-reactivation, fig6a-safe-trajectory and fig6b." This leaves out fig3d-pir-weaker-than-bla, which gives p = 0.083 with the immobility substitute and would then be not reproduced (cell 145). The record's notes do include it.
- **Cell 97, and the record's data_missing finding:** "streaming about 470 GB of tar.gz archives (the survey above)". The survey (cell 2) prints only the 99.0 GB of clu archives; no LFP total is printed. The record's later finding says the LFP archives are "3 to 9 GB each", while cell 0 says "4 to 9 GB". Neither range is printed.
- **README:** "It takes about 30 minutes, 12 of them streaming". Cell 2 prints "loaded in 1045 s", about 17 minutes, and no total runtime is printed.
- **README:** "Claims on hippocampus-BLA pairs, state firing rates and ripple modulation use the authors' summary tables, after checking them against the raw spikes." PoissonRippleMod is checked only for internal consistency (cell 9). StatesFR is checked against raw spikes only for column 9 and the wake-column bound (cell 6).
- **Cell 33:** "Result: reproduced." It lacks the "(resting on the estimated air puff location)" qualifier that the record (`assumed: true`) and the Summary attach to fig1c-slower-in-dz-post-run.

All other Result sentences, the record's notes and the remaining Summary and README statements match the printed numbers. The README table accounts for all 38 claims. The record's round-1 `reason` fields are my round-1 reasons, verbatim.

## 3. Round-1 points

**Resolved**
- **1, substitute NREM.** Replaced by decoded states and validated against the table and against the StatesFR minutes (cells 98–99).
- **2, Rat08 structures.** CeN 783 and Pir 1,575 (cell 14). Pir now has 14 sessions in 3 rats (cell 107).
- **4, previous zone after a session without a location.** Rat09-20140329's previous zone is now undefined (cell 17).
- **5, mixed BLA and Pir variant.** Removed.
- **6, decay windows.** Windows are now counted in decoded NREM time, and the table pre-NREM variant is run.
- **8, REM column.** New evidence added.
- **10, `_zbins`.** Synthetic test gives 200 of 200 bins (cell 98).
- **11, session count.** Explained (cell 20).
- **7 and 9.** Noted in the record.
- **"Could not check" items.** Done for minutes per state, the location sensitivity, Rat08 labels, the REM claims (by decoding) and laps and track extent. The fig5b smoothing still cannot be tested; the record says so.

**Remaining, bearing on a conclusion**
- **Air puff location (point 3).** Disclosed, but unresolved. The behaviour outcomes for fig1b-dz-speed-posthoc, fig1b-speed-ratio and figs1b-ratio-each-rat depend on whether the biased estimate or the 7.3-cm correction is used.
- **fig3c-decay.** Reproduced under one of four state readings. Under the table's pre-NREM (the authors' own pre-NREM correlations) it is partial. The first-window count of 17 is outside the expected 19 ± 1.9.
- **Fragile decoded outcomes.** fig3d-pir-reactivation, fig3d-pir-weaker-than-bla, fig6a-safe-trajectory-no-reactivation and fig6b-airpuff-greater-than-safe each flip under a decoder variant. This is disclosed in the record but incompletely in the Summary (section 2).

**Remaining, not bearing on a conclusion**
- The stale text in cells 11 and 13, and the unsupported README and finding figures in section 2.
- In the table pre-NREM decay variant, Rat10-20140622 has window 2 undefined while windows 1 and 3 are defined (cell 101 output). Nothing explains this; it affects one session of a variant.
