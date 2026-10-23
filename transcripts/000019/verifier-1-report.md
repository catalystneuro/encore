## A. Outcomes per claim

The claims file lists 22 claims; each has a row below. The header's rule applies throughout: when method readings disagree, the outcome is blocked (methods_underspecified).

| Claim | My outcome | Reason |
|---|---|---|
| data-composition | partially_reproduced | Three subjects, 3051.76 Hz (within 1 Hz). But there is no audio, the subjects have 19/19/19 consonants and 57+55+57 = 169 CVs, renditions run from 2 to 107, and GP33's hemisphere cannot be determined (cells 8, 18). |
| active-electrodes | blocked (methods_underspecified) | With all CVs, no baseline gives a mean in 27–33 (24.3, 21.3, 34.0). With 15+ CVs only `rest` does (27.0), which is partial. The split comes from GP31's /thi/, which has 2 renditions (GP31 counts 49→9 and 43→0, cell 20). |
| fig1c-e-articulator-electrodes | blocked (metadata_insufficient) | No subject and numbering puts all six named electrodes on vSMC (at most 5 of 6, cell 22 prints `[]`). The criterion blocks it in that case. |
| fig1f-h-phonetic-contrasts | not_reproduced | 0 of 96 readings have a lips-positive GLM electrode with /ju/ above 2 and /ja/, /ji/ below 2. The largest /ju/ under `pre` and `whole` is about 1.2. The 13 readings with /ju/ above 2 (`rest` only) also have /ja/ or /ji/ above 2 (cell 24). The qualitative parts are not judged. |
| fig2a-lips-dorsal | blocked (metadata_insufficient) | No distances from the Sylvian fissure in the archive (see B17). |
| fig2b-somatotopic-sequence | blocked (metadata_insufficient) | Same reason. |
| suppfig3b-spatial-clustering | blocked (metadata_insufficient) | Same reason. |
| suppfig3d-cross-subject | blocked (metadata_insufficient) | Same reason; GP33 also has no coordinates. |
| suppfig3f-dv-sequence | blocked (metadata_insufficient) | Same reason. |
| suppfig5-intermediate-organization | blocked (metadata_insufficient) | Same reason. |
| suppfig6-mixed-tuning | reproduced | Holds in 96 of 96 readings, with preferred shares of 48–96% and nonzero shares for other articulators (cell 28). The criterion is close to guaranteed by grouping on the largest weight (B10). |
| fig3d-timing-sequence | not_reproduced | None of the three order conditions holds in any of 96 readings (`{0: 96}`), measured against both the substitute onset and t = 0. Tongue onsets run −26 to +290 ms, jaw is earliest, and High Tongue peaks at 276–325 ms. ANOVA p < 1e-10 in 76 of 96; total electrodes 162–226 against 211. |
| suppfig7-no-latency-difference | blocked (metadata_insufficient) | There are no ±10 mm distances and no guenon labels. Only a label-based substitute could be run (B17). |
| pca-nine-components | blocked (methods_underspecified) | The `row` z-scoring gives 0.598–0.661, within 0.54–0.66 in 11 of 12 combinations. The `time` z-scoring gives 0.49–0.564; under the `pre`/`whole` baselines it falls outside in 7 of 8 (cell 32). 16 readings are in, 8 out. |
| fig4a-consonant-clusters | blocked (methods_underspecified) | 23 readings are not reproduced and 1 is partial (cell 34); no reading reproduces. Across readings the k = 3 silhouette is 0.19–0.36 (against 0.47), and k = 2 is usually highest. |
| suppfig11-co-clustering | blocked (methods_underspecified) | 38 readings are partial and 10 not reproduced. None reproduces, because consonant co-clustering is 0.63–0.91 against 0.50 ± 0.05. Vowel medians are 0.41–0.70. The chance levels are near the paper's: consonant null 0.34–0.41 (paper 0.32), vowel null 0.34–0.43 (paper 0.37). |
| fig4c-d-hierarchy | blocked (methods_underspecified) | 28 readings are partial and 20 not reproduced. The consonant and vowel rules never both hold in more than one subject (only EC2, cell 38). |
| fig4ef-feature-correlations | blocked (methods_underspecified) | Euclidean distances give 10 reproduced readings and 14 partial. Reproduced mostly with 15+ CVs or projection (ii). With projection (i) and all CVs, "late vowel > location" fails (cell 40). |
| fig5c-separability-timing | not_reproduced | No reading reproduces. Consonant peak −155 to +15 ms (paper −200 ± 20), vowel peak 155–235 ms; the k-means curve peaks anywhere from −170 to 375 ms (cell 42). |
| fig5d-separability-coupling | blocked (methods_underspecified) | Phonetic groups with the matching feature set reproduce (80 readings). The mean-of-three-sets reading and the k-means readings are not reproduced (145; minimum r −0.43 to −0.69). 15 readings are partial (cell 44). |
| suppfig13-consonant-vowel-distance | blocked (methods_underspecified) | Orderings hold in 36 readings and fail in 12 (`time` z-scoring with projection (i) gives CV < CC). The pair count is 4677 or 4567, never 4623, so no reading can reproduce (cell 46). |
| suppfig9-pc-articulator-weights | not_reproduced | All 288 readings are not reproduced. Tongue is not above lips (corrected p = 1), and jaw differs from larynx at p = 5e-11 where the paper reports p > 0.2 (cell 48). |

## B. Problems

1. **[does not affect a conclusion] Cell 5: an unchecked statement about file contents.** The line "only acquisition/ElectricalSeries is present" is a hard-coded print, not a check. The DANDI asset metadata for `sub-EC2_ses-EC2-B1.nwb` lists `ProcessingModule` and `Spectrum`, and the dandiset summary lists both. The notebook never looks at them. A spectrum is not audio, but this is unverified.
2. **[affects a conclusion] Cells 10 and 18: subject identity is assumed.** GP31 = EC31 and GP33 = EC33 is an assumption. GP33 has no coordinates, so the one right-hemisphere subject cannot be confirmed. GP31 is the subject with only 18 consonants that have all three vowels (/tha/ and /thu/ are missing, /thi/ has 2 renditions). That fits the paper's 54-CV subject but is not stated.
3. **[affects a conclusion] active-electrodes and the 15+/all CV split generally.** One GP31 CV with 2 renditions (/thi/) drives the threshold count. Removing it takes GP31 from 43–49 active electrodes to 0–9 under `pre` and `whole`. It also flips silhouettes (cell 34, GP31 k = 2 at 0.78 against 0.37) and the fig4ef late-window tests. Many methods_underspecified outcomes come from this split.
4. **[does not affect a conclusion] Cell 0.** The table lists fig1c-e as "tested", but its criterion makes it blocked, and the cell 22 output confirms that.
5. **[does not affect a conclusion] Cell 46 (suppfig13).** It labels "orderings hold but n ≠ 4623" as partial. The criterion defines no partial outcome, so this category is the author's own.
6. **[does not affect a conclusion] Cell 36.** `ok_tests` combines the cons-(a), cons-(b) and vowel tests, so the outcome for label reading (a) depends on reading (b)'s test. All cons-(b) p-values are below 1e-10, so nothing changes.
7. **[does not affect a conclusion] Cell 42, `B.separability` with bootstrap weights.** Duplicated tokens count as within-cluster pairs at distance 0, which biases the bootstrap s.e. used by onset reading (a). Onset reading (a) also takes the value at −500 ms as the "pre-epoch level", which is the author's choice. The peaks fail regardless.
8. **[does not affect a conclusion] Cell 48 (suppfig9).** Electrodes that lack a T_A for any articulator are dropped. Under the "all six" readings this gives n = 185, because GP31 has no Tongue window. Every reading fails anyway.
9. **[does not affect a conclusion] Cells 24, 28 and 48 use the position-free part of the blocked fig2a.** fig1f-h, suppfig6 and suppfig9 rely on fig2a's GLM selection and weights, which need no electrode positions. This is defensible, but the dependency is on a blocked claim.
10. **[does not affect a conclusion] suppfig6 criterion.** Grouping electrodes by their largest W makes "the preferred articulator has the largest mean share" almost automatic. The claim is reproduced by a test that would barely discriminate. This is a weakness in the claims file, not the code.
11. **[does not affect a conclusion] Cell 11: artifact intervals.** 177 of 9370 kept trials overlap "ECoG artifact" invalid intervals and are not excluded. The claims file is silent on this.
12. **[does not affect a conclusion] Cell 12: units.** The conversion factor is inconsistent (0.001 applied to values already in volts). Only z-scores are used, so nothing changes.
13. **[does not affect a conclusion] Helper checks.** I checked these helpers on synthetic inputs and they behave correctly:
    - `partial_correlation` matches a residual-correlation reference (error 4e-16).
    - `glm` betas match least squares.
    - `co_clustering` gives the correct values on small cases.
    - `separability` matches a direct computation.
    - `timing` returns the right times.
    - `ms_index(-25)` and `ms_index(250)` return the right indices.
    - `state_space` explained variance matches sklearn PCA.
    - `parse_label` parses the labels correctly.
14. **[does not affect a conclusion] Supplementary Figure 1d transcription verified.** I extracted the figure image from the supplement PDF. All four consonant rows and the Back/High Tongue vowel rows of `_ARTIC_ROWS` and `_VOWEL_ROWS` match it (light = 1; vowel column order a, i, u, confirmed from the "pee" and "soo" highlights).
15. **[does not affect a conclusion] fig3d's tongue counts are very small.** Under "all six" readings only 1–5 tongue electrodes are selected, so tongue onset means rest on very few electrodes. This follows from the claims file's mean + 2.5 SD rule, not a bug.
16. **[does not affect a conclusion] fig4c-d vowel rule.** It accepts a /u/ majority in either cluster, which is correct.
17. **[affects a conclusion: blocked claims] Archive check.** The archive has 31 NWB files and no other assets (API). None carries distances to the central sulcus or Sylvian fissure, or guenon labels. EC2 and GP31 have unlabelled x, y, z coordinates; GP33 has none. So the blocks stand under the claims file's 2026-10-22 answer. Parts could be run only as recorded substitutes:
    - suppfig7: precentral against postcentral electrodes from the dataset's own labels (not ±10 mm). The GLM R² onsets need no positions.
    - suppfig5: within-subject Euclidean distances from x, y, z, for EC2 and GP31 only.

## C. What I could not check, and the outputs that would have let me

- **The processing module in EC2-B1.** A listing of `processing/` in `sub-EC2_ses-EC2-B1.nwb` (names, types, shapes) would show what it holds.
- **The Supplementary Figure 12 feature matrix.** I did not verify its transcription (I checked only Figure 1d). A side-by-side image of the decoded matrix would allow it.
- **GP33's hemisphere and the GP/EC subject mapping.** Any subject-level NWB fields (`general/subject` description, electrode group `location` and `description`) would settle these.
- **fig1f-h.** A per-subject count of all vSMC electrodes (not only lips-positive GLM ones) with /ju/ above 2 and /ja/, /ji/ below 2 at +250 ms would separate the electrode selection from the absence of the effect.
- **The source of each methods_underspecified split.** For pca, fig4a, suppfig11, fig4c-d, fig4ef, fig5d and suppfig13, a table of outcome counts per single reading factor (baseline, CV set, z-scoring, projection) would show which reading drives the split. For several of them I could only infer it.
- **Effect of artifact trials.** The active-electrode counts and fig3d with invalid-interval trials excluded would show whether the 177 kept artifact trials matter.
