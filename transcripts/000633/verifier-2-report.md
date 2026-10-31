**Verification report, round 2: Kim et al. 2023 (doi:10.3390/ijms241310921) against DANDI:000633 v0.231013.2226**

The claims file has 12 claims. The attempt record has 12 outcomes: 9 blocked (data_missing) and 3 reproduced, 2 of which carry `assumed: true` (fig4a and fig4-comet-shape).

### 1. Outcomes

| Claim | Record | Agree? | Notes |
|---|---|---|---|
| fig2-cancellation-at-180, fig2-crossover-angle, fig2-facilitation-plateau, fig2-60-fold-co-counter | blocked (data_missing) | Yes | The numbers given "for information only" match cell 25. |
| fig3-1hz-co-cross-same, fig3-770khz-co-enhanced, fig3-770khz-cross-same-as-1hz | blocked (data_missing) | Yes | |
| fig4a-single-pulse-follows-field | reproduced, assumed | Yes | See the assumption below. |
| fig4bc-paired-pulse-focal-apex | reproduced | Yes, but it should probably carry `assumed: true` | See below. |
| fig4-comet-shape | reproduced, assumed | **Yes. This changes my round-1 view** (partially_reproduced). | One statement in the record is wrong; see section 2. |
| fig5-base-sawtooth, fig5-apex-larger-polarization | blocked (data_missing) | Yes | |

**fig4a assumption: E1 is base_a, the image is not mirrored, and the file is Figure 4A.**
- It is stated in the notes, the deviations, cell 15, the Summary and the README.
- It is reasonable. The data point the same way on their own: with E1 = base_b, the grounded electrode would show 2.5 times the uptake of the pulsed one (649.8 vs 262.6).
- I cannot check where Figure 4A places E1. The paper text says only that the panels are shown "with electrode positions labeled" and that E1 is the electrode pulsed in A. The notebook does not reproduce the figure.
- The deposited paired image has its apex at the bottom (cell 9; cell 5 gives apex y = 979). So the deposit does not keep a fixed orientation across the two images, which weakens "same orientation as the figure" as evidence. A 180° rotation does not mirror the image, though, so this does not overturn the assumption.

**fig4bc: why it should probably be flagged `assumed`.** Its criterion needs "the single-pulse image of Figure 4A". That half rests on the same identification of the single-pulse file that its metadata contradict. The notes and deviations state this, but the outcome is not flagged. Either flag it or say why it is not flagged.

**fig4-comet-shape assumption: a MemBrite-bright object is debris.**
- It is stated and reasonable. In cell 21 the object is a blurred disc about 105 µm across, at 20 times the dish median in MemBrite and 48 times in YP, and not saturated (max 40132).
- The rule is varied at 5, 10 and 20 times the dish median and gives the same result. The two robust maxima agree.

### 2. Statements the numbers do not support

**Attempt record, fig4-comet-shape deviation 3:** "the extents along and across the line are shown too, and agree."
- In cell 20, at half maximum for the debris-excluded versions on which the outcome rests, the extent along the line is *smaller* than the extent across it: 2446 vs 2592 µm at 10× and 20×, and 2446 vs 2473 µm at 5×.
- They agree only at a quarter maximum and for the 99.5th-percentile and median-filter versions.
- The chosen measure, reach toward the base (1755) against the largest distance across the line (1315), is a defensible reading of the criterion. But the half-maximum pass depends on it, and the sentence should be corrected.
- Cell 22 shows the same thing: the half-maximum region of the primary version is a blob around the apex footprint, about as wide as it is long.

**"One object … is left out"** appears in three places:
- The README: "one bright object in both channels, likely debris, is left out before the maximum is taken".
- The Summary, cell 28: "one object bright in both channels … is left out".
- Cell 23, the heading: "the assumption that one object bright in the MemBrite channel is not part of the electroporated monolayer".

What the rule actually does is leave out every pixel above the MemBrite threshold, 0.54% of the region (1.50% at 5×). That is many objects, and cell 21 shows several other blurred discs. The maximum is the same either way (cell 20: the next highest value outside 500 µm is 1063), but the region's pixels and areas are affected. The record's own notes say "objects", correctly.

**Cell 15:** "The assignment is taken from the paper's figure, not from the uptake, so the test is no longer circular". This rests on where Figure 4A places E1, which the notebook does not show and the paper text does not state (see section 1).

**Cell 18, and the record's fig4a deviation 3:** "co-directional pairs from one electrode" and "from one base electrode". The session description says co-directional pairs in a triangular array, not that they came from one electrode. This is an inference and should be worded as one.

Every other number I checked matches the printed outputs:
- Cell 13: ρ ranges, thinned p-values, 8 of 10 variants, neighbourhood means.
- Cell 17: the ratios and the fields (19.6/20.0 vs 8.4–9.0 kV/cm, "more than twice").
- Cell 20: 3999, 1063, 2468 µm, 105 µm, 8688 µm², 14577/5266 vs 305/255, 0.54%, and the half and quarter reaches. "About four times" is 3.76.
- Cell 25: 17.2%, 5.8-fold, 25.6%, the crossings, 378%, 1460/741%, 85 and 56.
- Cell 7: 4.2–9.7 kV/cm.
- 9 of 12 claims blocked.

The attempt record's `verifications` block states my round-1 reasons faithfully and in its own words, including the comet disagreement (`agrees: false`, partially_reproduced).

### 3. Round-1 points

| Point | Status |
|---|---|
| 1. Single-pulse metadata describe another exposure | Resolved as disclosure. It cannot be settled from the data. Only the missing `assumed` flag on fig4bc remains. |
| 2. Which electrode is E1 | Partly resolved. The assumption is now stated and no longer taken from the uptake, but the Figure 4A label it relies on cannot be checked with the text I have. |
| 3. Comet maximum never inspected | Resolved: the object is shown at full resolution in both channels, and the exclusion rule is varied. |
| 4. Spearman p-values | Resolved: the test also runs on ROIs thinned to 1 and 2 mm spacing. |
| 5. Single-image footprint fits | Resolved: the close-up views in cell 10 show the centres sitting plausibly in the dark discs. |
| 6. Field model | No action was needed. |
| 7. Smoothing before masking | Resolved for the mean, which now uses a masked filter. The median filter is still unmasked, and the record says so. |
| 8. Neighbourhood radius not really varied | Resolved: the neighbourhood means now change with the radius and the order holds. |
| 10. Claims file | I still find no place where it misreads the paper. |

**What remains that bears on a conclusion:**
- **fig4-comet-shape:** the wrong "extents agree" sentence. At half maximum the pass depends on the reach-versus-half-width measure; by full extents the primary version fails.
- **fig4a:** E1's position in Figure 4A cannot be checked from the paper text available here.
- **fig4bc:** it is not flagged `assumed`, although it rests on the same file identification as fig4a.
