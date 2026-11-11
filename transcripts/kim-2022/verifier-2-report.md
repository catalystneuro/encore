**Verifier report, round 2: Kim et al. 2022 (DANDI:000489 v0.230518.1811, DANDI:000448 v0.230421.1844)**

**1. Outcomes**

The claims file has 25 claims and the attempt record has 25 outcomes: 12 tested and 13 blocked. Of the blocked ones, 12 are `dataset_missing` (Figs. 3 to 6) and one is `data_missing` (fig1e-heating). Every tested outcome is `assumed: true`.

| Claim | Outcome | Agree? | Assumptions |
|---|---|---|---|
| fig2a-uptake-rises-with-field | reproduced | Yes | Unpaired test. Stated and reasonable. The paired test gives 3/5, and the record says so. |
| fig2a-vertical-scales | not_reproduced | Yes | Image counts are the paper's units. Stated and reasonable. The supporting fact ("conversion 1.0, offset 0") is not in any printed output. |
| fig2b-exponential-same-slope | partially_reproduced | Yes, changed from round 1 | The adopted reading (8 kV/cm, NLS) is the criterion's own main reading, so adopting it is sound. The criterion names no outcome for "exponential fails, slopes agree", and partial is a reasonable way to fill that gap. The gap is in the claims file. The slope "pass" comes from a test with 2 unipolar dishes, while the slopes fitted to the means are 0.72× unipolar. The record states both. |
| fig2c-max-inhibition-50-75 | not_reproduced | Yes | "The test holds at every field". Stated and reasonable. It alone decides between not_reproduced and partial, and the record says so. |
| fig2c-inhibition-flat-above-8-7 | reproduced | Yes, on the criterion's letter | ROI reading (a). Stated with a reason. The outcome flips under (b+) and (b−), and the record says so. |
| fig2c-weaker-at-6-7 | partially_reproduced | Yes, with caveats | 1. The record does not say that the criterion as written gives a different outcome. Its reading (ii) pools "the dish values of all higher field ROI". Under that wording 50% passes (p = 1.5e-9), so the outcome would be reproduced. Averaging within each dish first is the right correction, and the deviation is stated, but the record should say plainly that the outcome would change. 2. The 100% "pass" divides by a unipolar mean of 19 a.u. from 2 dishes (cell 58). The record's own notes say this is not inhibition in the paper's sense, yet it still counts the pass. |
| fig7-unipolar-pole-polarization | reproduced | Yes | Pole regions and cathode = brightening pole. Stated and reasonable. |
| fig7-charging-time-constant | not_reproduced | Yes | Same assumptions. Fails on discharge τ and both amplitudes under every onset variant. |
| fig7-later-pulses-same-tau-difference | partially_reproduced | Yes | Same assumptions. Under the criterion's form, "fewer" includes 0 of 4. |
| fig7-bipolar-overshoot | reproduced | Yes | Same assumptions. |
| fig7-bipolar-alternation | reproduced | Yes | Same assumptions. |
| fig7-summation-without-buildup | reproduced | Yes, on the criterion's letter | Same assumptions. The paired build-up is disclosed. |
| 12 Fig. 3–6 claims | blocked (dataset_missing) | Yes | Not in the two named datasets. |
| fig1e-heating | blocked (data_missing) | Yes | No thermometry photographs in either dataset. |

**New observation on the Fig. 7 pole masks (cell 7 figure).** Several recordings are clusters of 2 to 4 touching cells: 003, 004, 005, 006 and 007. The largest-connected-group mask spans the whole cluster and includes membrane at cell–cell contacts. For example, in 003 the blue mask runs along the boundary between the two upper cells. The paper says "individual cells or small groups of cells were imaged", so clusters are allowed. The record's pole-region assumption and its "5 unipolar cells" do not mention this. It may bear on the 23% against 31% amplitude, which the record already attributes to the pole regions. No outcome changes.

**2. Sentences the printed numbers do not support**

- Cell 34: "Channel index 1 is three to six times brighter between the electrodes than 3 mm away". Cell 33 prints centre/far ratios for ch1 of 1.28 to 6.54, and 10 of 17 are below 3.
- Attempt record, fig2c-max-inhibition-50-75 notes: "the unipolar dishes on 2021-07-29, with mean footprint YP0 of 209 and 273 a.u." Cell 40 shows that 273 is the mean of all 7 dishes imaged that day (0, 25 and 50%). The two unipolar dishes analysed have YP0 236 and 292 (mean 264).
- Summary (cell 60): "The 0% and 25% dishes were imaged on 2021-07-29". Fig2_25_04 is dated 2021-07-26 (cell 32). It is one of the two dishes left out. That the two files sharing one YP image have different session dates is itself worth adding to the metadata finding.
- Record, fig7-unipolar deviation: "a lag of 74 frames in every cell". The finding and the summary also give 74 frames. Cell 8 shows cell24 at −75.
- Record finding and summary (cell 60): "The first frame of most 000448 files is dark (about 180 counts…)". Cell 5 flags frame 0 as dark in 4 of 18 files. The minimum frame mean is 180 to 193 in all files, but the output does not show which frame it is.
- Not in any printed output, so not checkable:
  - cell 45 and the fig2a-vertical-scales deviation: "conversion 1.0, offset 0"
  - the finding and summary: "Channel1" for both dyes, "144 images (12 x 12) of a well of a six-well plate" and "Three files name their series 'Fig2_25'". Cell 32 prints only "ex/em 350/460 nm and ex/em 480/535nm".
  - cell 0: the draft asset and byte counts
  - cell 10: the FluoVolt dF/F description
- Cell 30 and the fig7-summation-without-buildup notes: "a small build-up of 6 to 10% of the first peak is present within cells". The 6% is pulse 5 (+1.36 points, paired p = 0.089, not significant). Pulses 2 to 4, which are significant, give 7.8 to 10.1% (cell 29).
- Cell 53 and the fig2c-max-inhibition-50-75 notes: "The 25% and 100% pulses give 64 to 168%… so in these dishes they do not inhibit". This holds on average (means over fields about 110% and 118%), but 25% is below 100% at 6 of 10 fields (cell 52).

Every other number in the Result conclusions, the Summary, the README and the record notes matches the outputs.

**My round-1 reasons in the record.** All are stated faithfully in my own sense. One omission matters: the fig2c-weaker-at-6-7 reason leaves out my point that the claims file itself allows pooling dish values. That is the reason the corrected analysis departs from the criterion's letter.

**3. Round-1 points**

Resolved:
- **B1, pseudo-replication.** Pooling is now per dish, and the OR of paired and unpaired is gone.
- **B3, fig2b.** A reading is adopted with a reason, and the low power is stated.
- **B4, fig2c-flat.** Reading (a) is adopted with a reason.
- **B5, fig2c-max.** The "every field" rule is applied and stated.
- **B6.** The duplicate image, n = 2 unipolar dishes and 100% above unipolar are now in the summary.
- **B7.** The units assumption is stated.
- **B8.** The charging window is now 0 to 600 ns, with a half-frame variant.
- **B9.** The free-start form is labelled as a variant.
- **B10.** A fixed-time variant is added.
- **B11.** The paired build-up is disclosed.
- **B12, B13.** Unchanged, and fine.
- **Section C.** Per-dish values, footprint-disc variants, the Fig. 2B table and plot, and the fit overlays with residuals are all now printed.

What remains that bears on a conclusion:
1. **fig2c-weaker-at-6-7 (B2, partly resolved).** The partial outcome rests on 100% "passing" a test whose percentages divide by a near-background unipolar mean (19 a.u., n = 2). The record calls these percentages not a measure of inhibition but still credits them. Separately, the record should state that the criterion's literal pooled reading gives reproduced.
2. **Comparisons between amplitudes are also comparisons between imaging days.** 0% and 25% were imaged on 07-29 and 75% and 100% on 08-24. This is disclosed but unresolved and affects every Fig. 2C percentage. Far−YP0 is similar across days (27 to 31 a.u. on 07-29 and 08-24), which limits but does not exclude a background effect.
3. **Fragile outcomes.** fig2c-max-inhibition-50-75 and fig2c-inhibition-flat-above-8-7 each turn on one stated author rule (every field; reading a). This is acceptable as recorded.
4. **B14.** The claims file assigns the Fig. 3 to 6 claims to 000489, a scoping issue in the claims file. It stands unchanged.
