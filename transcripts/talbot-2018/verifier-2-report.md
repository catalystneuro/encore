## Round 2 verification: Talbot et al. 2018 on CRCNS hc-16

### 1. Outcomes and assumptions

The claims file has 32 claims and the attempt record has 32 outcomes: 14 blocked, 1 reproduced, 8 partially reproduced and 9 not reproduced. **I agree with all 32 stated outcomes.**

- **figs4-remapping-similar:** I now accept data_missing in place of the metadata_insufficient I gave in round 1. Table S2 in `paper/…txt` (lines 2698–2749) lists an M32 small box session on 04-17-15, the same day as M32's arena sessions, and no small box sessions are in the data set (cell 16).
  - This also shows that the claims file misreads the paper. Its figs4 criterion says "Table S2 lists box and arena sessions of a mouse on different dates". For M32 it does not. I report this and do not correct it.
- **locomotion-similar** (`assumed: true`, environments pooled): the assumption is stated.
  - It is reasonable. The STAR Methods heading covers all four environments, and the Figure S5B legend says "open field recordings".
  - The outcome depends on it entirely. Within each environment the interaction is significant, in opposite directions (cell 62).
- **figs6-room-frame-preference** (`assumed: true`, reading B): the assumption is stated and plausible, but it is not applied consistently.
  - fig5b treats the same question (which session classifies the place cells) as open, judges it on both readings, and puts it to the paper's authors.
  - figs6 adopts reading B. Under reading A it would be not reproduced (environment p = 0.067, cell 73).
  - The assumption should say outright that it settles a question the record elsewhere leaves open.

### 2. Sentences the printed outputs do not support (cell indices 0-based)

- **Cell 74:** "Reading B is adopted, as for fig5b." fig5b no longer adopts reading B (cell 68, and the record's own response for figs6). This sentence is left over from round 1.
- **Cell 20, and the interneuron-proportion notes:** "…so clusters that mix many units do not explain the excess." A filter on refractory violations above 0.5% does not do the job of IsoIBG/IsoINN isolation. Interneuron rates are still 4.3 and 6.95 AP/s at the median (cell 11) and 5.4 and 10.3 AP/s in the box (cell 31), against the paper's about 16. What the outputs support is that this filter does not remove the excess.
- **Cell 54, and the fig4d notes:** "…at five in the other two (K1, H1, R2, 25 ms: 0.991 against 0.827)." K1/H1/R2 is one of the six-of-six readings. The five-of-six readings are K2/H2/R1 and K2/H2/R2 (cell 53).
- **Cell 75, Summary:**
  - "[the refractory filter] … leaves the other results as they are".
  - "On the code's 32 x 32 grid … no outcome changes".
  - Both variants were run only for the single-cell claims (cells 19–35). They were not run for the overdispersion, covariance, Kendall or rotating-arena claims, which depend on the same place-cell classification. The two sentences should be limited to the claims tested.
- **Attempt record, metadata_insufficient finding:** "about 218 in four (M1, M9, M10, M11)". M1's box extent is 188 × 207 px (3.95 px/cm; cell 2). Only M9, M10 and M11 are near 218.
- **README:** "a reading of it as a count changes the overdispersion result". It changes overdispersion-passes in R2 only. overdispersion-cells and the R1 reading do not change (cells 39 and 42).
- **Cell 46:** under the count rule, one permutation per pair gives t = 3.61, p = 0.0004. That is about the same as the unshuffled t = 3.54, while the mean of 100 permutations gives p = 0.51 (cell 45). A null shuffle should almost never give this, and the notebook does not examine it. It bears only on a variant.
- **fig5b measured values:** `measured` lists only the reading-B values (0.066, 0.106), but the outcome is judged on both readings. This is minor.

Every other sentence I checked in the "**Result:**" cells, the Summary, the README and the notes matches the printed outputs.

**Round-1 reasons in the record:** they state my round-1 reasons faithfully and in my own words. The problems not tied to one claim (4, 7, 8, 9, 10 and 11) are attached to the right claims. Problem 12 is now a data-set finding.

### 3. Round-1 points

**Resolved:**

| Point | How it was resolved |
|---|---|
| 4 (counts blocked as data_missing) | Outcome changed |
| 5 (fig5b readings) | Both readings run, per-cell values printed, leave-one-mouse-out added |
| 6 (locomotion) | Directions per environment, unit sets and the question to the authors printed |
| 7 (R2 double counting) | Stated in the Summary |
| 8 (low-speed mask) | Whole-bin mask now used |
| 9 (Tukey ignores repeated measures) | Disclosed, with paired-t variant |
| 10 (Ipos visit count) | Now counted per position sample |
| 11 (figs4 evidence) | Code cell added; data_missing accepted |
| 12 (split files) | Recorded as a finding |
| "Could not check" items | Full TS header, count rule, 32 × 32 grid, M16 left out and per-cell Ipos are all now printed |

**Partly resolved, and bearing on a conclusion:**

- **Point 1, pass rule.** The count reading is now run and the question is put to a reader. The four pass-based outcomes still rest on the claims file's literal rule, which passes a median 76% of 5 s intervals.
  - Under the count rule, overdispersion-passes in R2 meets the claims file's written criterion: variances 5.28 and 4.66 are both within tolerance, F p < 0.0001, Levene p = 0.0006 (cell 39).
  - So this outcome depends on how the claims file reads the paper's "exp ≥ average rate". I report this as a claims-file gap.
- **Point 2, population.** The header is printed and a refractory filter is added. With the filter the interneuron result in R1 loses significance (p = 0.092) and the figs3 rate effect goes. The filter is a weak proxy, the Cell 20 inference goes beyond it, and it is not applied to the overdispersion, pair or rotating-arena claims.
- **Point 3, spatial scale.** Resolved for the single-cell claims. It was not tested for the pass-based claims, which use 1.25 cm maps at the assumed scale, yet the Summary generalises to every claim.
- **figs6.** The reading-B assumption should state its inconsistency with fig5b, and the stale sentence in Cell 74 needs removing.
