# Round 2 verification: Souza et al. (2026) on DANDI:000713

All 38 outcome result cells, the Summary table and the README count (17 reproduced / 14 partially reproduced / 7 not reproduced) agree with the attempt record. I found no place where the claims file misreads the paper; Materials and methods 2.1 gives no selection rule.

## 1. Outcomes and assumptions

I agree with 37 of the 38 outcomes.

**The one I still dispute:**
- **data-sessions-units** (record: partially_reproduced; mine: not_reproduced). The criterion allows the 10% partial outcome for its own readings (a) and (b). Under both, the counts are more than 10% off (cell 5: 153 sessions / 81 mice / 110,563 or 45,354 units). The Sst/Vip, "good", presence ratio ≥0.95 selection is not one of those readings. If protocol step 1.6 says what the response quotes, the author's choice is defensible. The disagreement is recorded and changes no other outcome. The assumption is stated and reasonable.

**Round-1 disagreements I now accept.** None of these criteria has a partial clause, so the protocol's general definition ("holds only in part") applies:
- **latency-change-to-reward** (cell 20): with `change_time_no_display_delay`, three of the four values are within tolerance, and 4.20% misses by 0.02 points. The outcome rests on a different change time from the one the cohort's pseudo-reward latencies use (change-presentation start). The deviations state this.
- **m-baseline-sensitivity** (cell 69).
- **layer4-within-waveform** (cell 80): with the stored duration both excesses are positive at p < 1e-6.

**layer4-controls**: now not_reproduced, which agrees with me.

**Assumptions.** Every outcome is `assumed: true` and lists the session selection. The other stated assumptions are reasonable:
- 100 permutations and ISI-null reading 1a (fig1e, fig1d);
- duration reading (b) for all waveform-class claims;
- peak reading (b) for fig3a;
- ramp reading (a) for fig3d and anticipatory-direction-overlap;
- the 500 ms bout gap for hits-vs-lick-bouts.

One assumption is missing. fig2d-cv-correlations and cv-correlation-block-excess rest on averaging 20 RW- draws. With a single draw the order is lost (cell 103: 0.300 / 0.318 / 0.354), and the excess becomes −0.050 (cell 106). The notes say this, but the deviations should list it as an assumption the outcome rests on.

## 2. Sentences the outputs do not support

- **Record `inputs[1]`:** "Used in the revision's runs because GIN answered 403 Forbidden to the runner; the layer counts are identical to those of the first run…"
  - Cell 71 makes the same point: "the first run … used BrainGlobe's file and the second the Allen files".
  - The layer-assignment-coverage deviation says "both give identical layers here".
  - Cell 72 of this executed notebook prints the BrainGlobe file (`allen_mouse 1.2`, sha256 `696276…`) and no "GIN answered" line. So this run used BrainGlobe's file, and nothing printed shows the Allen path or that the two give identical layers.
- **Record, fig1gi-waveform-separation:** "Mann-Whitney p from 2.8e-264 to 1.6e-221". Cell 57 also has p = 2.3e-198 (median ISI, reading a). Cell 58's "p < 1e-190" is correct.
- **Record, layer4-within-waveform:** "below the paper's +0.137 and +0.114 except the broad one of reading (a)". That value is +0.124 (cell 80), which is also below 0.137. It is the one value within tolerance, as cell 81 says correctly.
- **Record, layer4-controls:** "The unmatched value does not rise above +0.116 … (median +0.122, mean +0.115)". The median of +0.122 is above +0.116 (cell 83).
- **Cell 29:** "so the reading does not change the counts". Cell 26 shows small changes, not none: cohort 1,268 against 1,272, with 6 + 2 units in only one cohort, and 74 / 63 split-half-positive units differing.
  - The Summary's "changes the cohort by 4 of 1,272 units" is the net change; 8 units differ.
- **Trivial:** cell 48 gives log-likelihood 24,671 for "the claim's seed and the seed plus 1000"; the seed plus 1000 is 24,661.5 (cell 46).
- **Not printed but consistent with the code:**
  - "1,508 … have no layer": `unit_layers` drops non-positive coordinates.
  - "82 samples" in the waveform finding.

Every other Result, Summary, README and notes sentence matches the printed numbers.

The record's round-1 reasons are mine, nearly word for word, with the problem references attached correctly. The counts it gives for my round 1 (17 / 10 / 11, five disagreements) are right.

## 3. Round-1 points

**Resolved:**
- B2: every unit has 384 rows; the peak row is the largest-amplitude row in 230 of 300 units checked, and within 4 channels in 299.
- B1: explained by the log-likelihoods, the histogram and the 1,263-unit tail; labels now default to reading (b).
- B6: stated in the notebook.
- B7: denominators (b) and (c) are used now.
- B8: laminar-by-name guard; no unit affected.
- B10: the fallback is removed and its count is 0.
- B9: the stricter rule is shown as a variant and asked of the authors.
- B11: the single-draw variant is shown.
- From section C: the accounting for the hits, the per-session table, the layout check, the mixture log-likelihoods and the stricter layer rule.

**Partly resolved:**
- B3: ISI-null reading 1b was run on 12 of 104 sessions.
- B4: the 1,000-permutation check covers 300 units in three sessions.
- B5: the 103rd session is still unidentified; it is now an open question for the authors.

**Still bearing on a conclusion:**
1. Every outcome rests on a session and unit selection that is not one of the criterion's readings.
2. fig1e-cohort-size fails only on the discordant count (286). That count has not been tested under null 1b on all sessions or with 1,000 permutations. 43,025 of 54,045 units sit at the p floor of 1/101 (cell 26), so the BH gate at 100 permutations is coarse.
3. All waveform-class outcomes rest on the stored `waveform_duration`. The Methods' own reading (a) does not give two classes.
4. The layer claims and coverage: the stricter visual-area rule fits the paper's coverage (87.0%, 45.5% in VISrl). Under that rule, layer4-suppression's median is +0.089 (cell 77), outside +0.116 ± 0.0116. If the paper used that rule, layer4-suppression would be partially reproduced, not reproduced.
5. fig2d-cv-correlations and cv-correlation-block-excess depend on averaging the RW- draws (see section 1).
6. The atlas-provenance statements in section 2.

## 4. Critical findings

No finding is rated `critical`. Of the data findings:
- the two rated `minor` are rated right:
  - the 1,508 units with CCF coordinates ≤0 (cell 72): evident from the values;
  - the `waveform_duration` mismatch (cell 46): evident on comparison, and the stored column is a workaround;
- the "checks that passed" finding, rated `none`, is supported by cells 11, 14 and 23.
