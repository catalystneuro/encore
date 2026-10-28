**Round-2 verification: Dimakopoulos et al. 2022 (eLife 78677) on OpenNeuro ds004752 v1.0.1**

Counts are taken from the files. The claims file has 21 claims, and the attempt record has 21 outcomes: 7 reproduced, 3 partially reproduced, 9 not reproduced and 2 blocked. Seven outcomes are marked `assumed: true`: fig2h, fig3, scalp-temporal-laplacian, table1-heschl, fig4e, fig4f and balanced-correct-subset. Cell numbers below are 0-based indices in the re-executed notebook, which differ from round 1.

## 1. Outcomes

| Claim | Record | My view |
|---|---|---|
| cohort-sessions | partially reproduced | Agree (cell 16). |
| fig1b-accuracy | reproduced | Agree (cell 19). |
| capacity-cowan-k | reproduced | Agree (cell 22). |
| fig1c-response-time | reproduced | Agree. The pass rests on pool p2 with the median, and the record says so (cell 25). |
| fig2bc-gamma-encoding-p1 | partially reproduced | **Disagree; I keep not reproduced.** C2 rises 17% against the required 100% (cell 30). The part that "holds" is near-empty on this grid: every one of the 64 contacts is temporal, parietal, occipital or unlabelled, plus one labelled hippocampus (cell 28). Almost any set of significant contacts would satisfy it, so only H3 carries information. |
| fig2d-cortical-beta-maintenance-p1 | reproduced | Agree. The notes rightly call it weak: no contact survives a Benjamini-Hochberg correction (cell 34). |
| hipp-beta-maintenance | not reproduced | Agree (cell 37). |
| fig2fg-plv-theta-p1 | not reproduced | Agree (cell 40). |
| fig2h-gc-reversal-p1 | not reproduced, assumed | **Agree, with a reservation.** The assumption is stated: the per-frequency test (c1) is dropped because it flags shifted-trial pairs. That is reasonable only if those pairs carry no directed effect, which is not shown (see 3.1). Without that assumption, the claims file's "under one reading" rule passes the claim under h1 with c1. |
| fig2ijk-spatial-spread-p1 | not reproduced | Agree (cells 49–50). |
| fig3-gc-reversal-p2-p3 | not reproduced, assumed | Same reservation as fig2h. Under c1, Participant 3 passes with h1 and h2 (cell 53). |
| fig3no-p4-right-no-gc | blocked: methods_underspecified | **Disagree; I would record not reproduced.** The criterion's test was run and flags every contact (cell 56). Against the attempt's own shifted-pair baseline, the real pairing is flagged more often by the cluster test: h1 maintenance 75% against 10%, h2 encoding 100% against 30%. That is evidence of GC, against a claim of absence. The method was specified and run, so this is not a block. |
| table1-left-hemisphere-sources | blocked: not_runnable | Accept. The author cites `not_runnable` as a category in the protocol, which I cannot see. The notes now say the MNE approximation was not attempted. |
| fig4a-group-gc-reversal | not reproduced | Agree (cell 62). |
| scalp-temporal-laplacian | reproduced, assumed | **Agree by the letter of the criterion, but it is not evidence.** One cell of 36 (18 readings × 2 tests) passes: h1, T5, band mean d1, paired test s1, at p = 0.020 uncorrected (cell 65). The encoding median is positive, so the "similar pattern" is absent. The result changed from not reproduced only because of the reference change. The h1/d1 adoption is not what the pass rests on, since the criterion accepts any one reading; it rests on that single cell. |
| fig4bc-auditory-strongest | not reproduced | Agree (cell 68). |
| fig4d-reversal-all | not reproduced | Agree (cells 71–73). |
| table1-heschl-dgranger-correct | partially reproduced, assumed | Agree by the criterion. The participant mapping is now stated as an assumption. The sign match comes only from d2, which builds in the sign. |
| fig4e-lpfc-no-reversal | not reproduced, assumed | Agree. h1 is adopted consistently and the choice is stated. The outcome depends on the reference rule: h1 gave p = 0.065 before the reference change and 0.010 after (cell 79). |
| fig4f-incorrect-no-reversal | reproduced, assumed | Agree by the criterion. Applying the recovered filters to the incorrect trials is a reasonable, stated choice; the recomputed source matches the deposited one (r = 0.996 to 0.999, ΔGranger within 0.0001; cell 82). But the result does not discriminate: under the same d1 reading the correct trials also show no reversal (fig4d, p = 0.13 to 0.92), so the paper's correct/incorrect contrast is not reproduced. The notes should say this. |
| balanced-correct-subset | reproduced, assumed | Agree by the criterion. All 5 passing readings are d2, and the record says the pass is not evidence. |

## 2. Statements the outputs do not support

- **Cowan's K, record deviation:** "the criterion's readings were all run and four of eight match". Cell 22 prints "readings within 6.1 +- 0.61: 5 of 8". The over-sessions median for set size 8 is 5.61, which is within tolerance. Cell 23 says reading (c) "is 5.43 (mean) and 5.33 (median), outside", which is true only over participants.
- **fig4f, cell 84 and record notes:** "The signs match Table 1's incorrect-trial values in 9 to 11 of 29 cells … about what chance gives". Chance is about 14.5 of 29, so 9 to 11 is below chance (cell 83).
- **fig2fg, cell 41 and record:** "The highest maintenance theta PLV is at A1 to A3 …, with C3 and B3 among the six highest". Under h2, C3 is not in the top six; under h3, A3 is not (cell 40).
- **README, fig2h deviation and the methods_unavailable finding:** "trial pairings with no coupling". The shifted pairs have no trial-by-trial coupling, but they keep the stimulus-locked responses (docstring of `mismatch_rows`, cell 43).
  - Cell 47 says "the null is narrower than nominal", and the Summary says the same for "4% to 26% of bins". 4% is below nominal, and "narrower" assumes the shifted pairs carry no directed effect.
- **fig2h deviation and cell 47:** "c2, which the Figure 2h legend names (cluster-based)". The legend names a cluster test "against a null distribution with scrambled trials". The notebook's c2 uses the direction-swap null.
- **README:** "It takes about 18 minutes". The printed timings alone add up to about 1388 s, roughly 23 minutes (cells 8, 43, 49, 50, 53, 56, 60, 82).
- **Cell 48 and record fig2ijk:** "each spatial test takes about 4 minutes". Cell 50 prints 344 s.
- **code_mismatch finding:** the claim about grangerspctrm row labelling in the paper's code cannot be checked from my materials. Control 3 in cell 72 shows only what the flip would do, not that the code does it.

The verifications block states my round-1 reasons faithfully in its own words, claim by claim. The two round-1 points tied to no claim are not recorded there: the ECoG reference (in problem 3) and the clock check (problem 10). Neither affected an outcome.

## 3. Round-1 points

**Resolved:**
- **Problem 1 (d2):** flagged in every affected conclusion, filed as a reader question and recorded as a finding.
- **Problem 3, hemisphere:** the white-matter reference is now in the same hemisphere as the hippocampal contact.
- **Problem 4:** the participant mapping is stated as an assumption.
- **Problem 6:** exact p-values are printed.
- **Problem 7:** accepted, as explained under table1-left-hemisphere-sources in section 1.
- **Problems 8 and 9:** fixed.
- **Problem 10:** now 12 of 15 subjects pass the clock check, and this is stated.
- **Section C:**
  - Variable lists and the R² fit are done, and fig4f is now tested.
  - Contact names are printed.
  - sub-11's PHL electrode is shown to be in the right hemisphere.
  - A same-hemisphere reference is used for Participant 3.

**Partly resolved:** problem 2. The calibration I asked for was added, which led to the switch to c2.

**Remaining issues that bear on a conclusion:**

1. **Calibration (fig2h, fig3, fig3no).**
   - The shifted-trial pairs keep the evoked responses. A consistent lag between the two areas' evoked responses is a real directional effect, and the direction-swap null would correctly flag it. So c1's 20% to 90% hit rate does not by itself show that c1 is anti-conservative. This was my own suggestion, so the limitation is partly mine.
   - c2 is not calibrated per test either. Its single-test theta rate reaches 50% in sub-11 h2 encoding and 30% in sub-12 (cell 53). Its low reversal rate comes partly from requiring both periods at once.
   - Ten shifts per cell give coarse rates.
   - What would settle it: rerun the calibration after subtracting each period's trial average (the ERP) from both channels, and run the legends' own test, a cluster test against a scrambled-trial null, on the real pairings of Participants 1 to 4.
2. **fig3no:** should be not reproduced, not blocked (section 1).
3. **fig2bc:** should be not reproduced (section 1).
4. **scalp-temporal-laplacian:** the pass is a single uncorrected cell at p = 0.02, and it appeared only after the reference change.
5. **fig4f:** the notes should state that d1 shows no reversal on correct trials either.
6. **Places where the claims file misreads the paper or under-specifies (reported, not corrected):**
   - fig2h and fig3: the figure legends name a cluster test against scrambled trials. The criterion makes the Methods' direction-swap null primary, and runs the scrambled-trial null only as the code's variant, for Participant 1 only and not as a cluster test.
   - fig2bc: the regional condition is near-empty for this grid.
   - scalp-temporal-laplacian: the criterion does not require the sign pattern of the "similar GC pattern".
   - d2 (problem 1): the criterion accepts a statistic whose sign is built in.
7. **Still not run, as the record states:** the per-contact tests for h2 and h3, and the spatial test for h3 and for encoding (fig2ijk).
8. **ECoG reference (problem 3), minor:** sub-10 and sub-12 still reference the ECoG to AHL4, next to the hippocampal reference AHL3. This is now documented; the shared reference signal could feed into the PLV and GC values for Participants 1 and 3.
