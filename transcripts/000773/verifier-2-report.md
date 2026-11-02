**Verifier report, round 2: Hart et al. 2024 (DANDI:000773, version 0.261004.1511)**

The claims file has 22 claims. The attempt record has 22 outcomes: 8 reproduced, 4 partially reproduced, 5 not reproduced and 5 blocked. Eight of the outcomes are marked `assumed: true`. The re-executed notebook has 79 cells, so cell numbers below differ from round 1.

### 1. Outcomes and assumptions

| Claim | Agree? | Note |
|---|---|---|
| The five behaviour claims (fig1c ×2, fig1b, figs1 ×2) | yes | Cells 13–19 are unchanged and match Table S1. |
| fig2b-gcamp-baseline-unchanged, blocked (other) | yes | Cell 10: three tries, each timed out. |
| fig2d-whole-al-alarm-no-age-effect, reproduced | yes | Cell 29: every p ≥ 0.061. |
| figs3b-whole-al-general-decline, partially reproduced | yes | Cell 32: the ratios are not reached with the raw measure or with the paraffin oil value subtracted (6.0 and 9.5). |
| figs3b-whole-al-other-no-age-effect, reproduced | yes | The smallest p is 0.062. The map without the minimum filter is saturated, and the notebook rightly does not count it as a test. |
| fig2e, fig2-alarm-sparse, figs3c, blocked (methods_underspecified) | yes | figs3c is now consistent with fig2e. |
| data-s2-glomerulus-link, partially reproduced | yes | By the criterion's letter: 66% at the placement from all trials. The notes say plainly that the link would fail on held-out trials (41%; old ants 9 of 52). |
| figs2a-mean-six-glomeruli-no-age-effect, reproduced (assumed) | yes, weakly | See the open issue on figs2a in section 3. |
| fig3b-g2-heptanone-weaker-old, not reproduced (assumed) | yes | Cell 52: G2 p = 0.86 at the held-out placement. |
| fig3d-pg-stronger-old, not reproduced (assumed) | yes | Cell 55: no variant meets either reading. The round-1 PGa result disappears once the place is chosen without the tested trials. |
| fig3d-pg-60-vs-90-days-same, blocked (methods_underspecified) | yes | Cells 58 and 60: 1 of 8 PGa placements at 90 days is above chance, and reading (b) mixes two pipelines. |
| figs4a-general-odorants-in-focal-glomeruli, not reproduced (assumed) | yes | Cell 63: 56 of 60 cells match, but the 3-hexanone pattern breaks. |
| fig4-general-odorants-decline, partially reproduced (assumed) | yes by the letter, fragile | Cell 66: 9 of 10, but G2 p = 0.0498 and G3 p = 0.0477. Only 1 of 9 variants reaches the partial level. With all trials instead of Data S2's trials, G2 is p = 0.059. PGb with 3-hexanone "declines" (p = 0.022) where Data S2 gives p = 0.23, which shows old-ant values are read too low (held out 12.8 against Data S2's 25.1). The notes disclose the fragility. |
| fig4-propionic-acid-g2-g3, not reproduced (assumed) | yes | Cell 69 |
| figs4d-pgb-hexanone-dynamics, partially reproduced (assumed) | yes | Cell 72 |
| pg-opposite-modulation, not reproduced (assumed) | yes | Cell 75 |

**The assumptions are stated and reasonable:**
- **Held-out placement as the main measure.** I asked for it in round 1, and it is applied the same way whether it helps (fig4) or hurts (figs4a, fig3d).
- **ROI radius of 8 pixels**, with radii 5 and 12 shown.
- **Fold-change reading (a).** Reading (b) now uses a background floor. Per cell 25, the floor is 73–155 raw units against an in-AL 1st percentile of about 470, which is sensible.
- **Data S2's trial selection**, with all trials shown as a variant.

### 2. Sentences the printed outputs do not support

1. **Cell 53, and the attempt record's fig3b notes and response:** "only the placement from all trials restricted to placements above chance (4 old ants) gives G2 p < 0.05". Cell 52 prints `n_old 5` for that row (p = 0.04957). ant5-m1-d10 G2 has p_trial = 10/201 ≈ 0.0498, which prints as 0.05 in cell 42. It should read 5 old ants.
2. **Attempt record, fig2b notes and response:** "three attempts … (ReadTimeout, ReadTimeout, ConnectTimeout, printed)" and "all three failed (ReadTimeout, ReadTimeout, ConnectTimeout)". Cell 10 prints `ReadTimeout` three times. The 17:12, 18:22 and 21:22 shell attempts and the landing-page wording appear in no output, so I cannot check them.
3. **README and Summary (cell 78):** "Run on Data S2's own values, every focal glomerulus claim holds as the paper states it" and "Data S2's traces give every focal glomerulus claim as the paper states it". Cell 75 shows Data S2 fails pg-opposite-modulation's criterion (2 of 30 tests, G2 and G3 with propionic acid). The attempt record itself says so, so these sentences need a qualifier.
4. **Summary (cell 78):** "The whole-AL measures, which need no hand-drawn ROI". Cell 24 and the claims file say the paper drew the AL outline by hand; here it is a threshold stand-in.
5. **README and cell 0:** "takes about 30 minutes". Cell 77 prints 43.9 minutes, and cell 22 alone takes 15.7.
6. **Attempt record, first finding:** "ten claims depend on them". The claims file gives 12: 8 claims list the link as a dependency, pg-opposite-modulation depends on it through others, and fig2e, fig2-alarm-sparse and figs3c rest on the responding ROIs.
7. **Attempt record, figs2a notes, and cell 50:** "p ≥ 0.080" / "0.080 or more". The smallest printed value is 0.07996 (cell 49, general only, b). This is a rounding nit.

All other numbers in the conclusion cells, the Summary, the README and the attempt-record notes match the printed outputs. I checked every p-value, mean, count and ratio quoted.

**My round-1 reasons in the attempt record:** each verification `reason` gives my round-1 outcome and reason faithfully, with the relevant problem attached. The `agrees: false` flags on figs3c, fig3d-60-vs-90 and pg-opposite match where I disagreed. Problems 10 and 11 are covered under `reviewed`. Most reasons are near-verbatim rather than paraphrased, but none misstates my reasons.

### 3. Round-1 points

**Resolved:**
- **Problem 1, placement chance level.** A permutation null is added for every placement: 42 of 42 young and 24 of 39 old placements are above chance (18 of 39 under the odor shuffle).
- **Problem 2, selection and test on the same trials.** The leave-one-odor-out placement is now the main measure, the general-only placement is added for the alarm pheromones, and the link is reported held out.
- **Problem 3, 90-day PGa placed from six trials.** The chance level is printed and the claim is blocked.
- **Problem 4, reading (b) mixing pipelines.** Blocked; the question is recorded for a reader.
- **Problem 5, reading (b) baseline.** The background floor is in place. The old-ant G1 means under (b) are now 2.6 and −6.3, matching cell 52.
- **Problem 6, whole-AL offset.** The paraffin-subtracted and no-minimum-filter variants are added. The ratios fail either way.
- **Problem 7, figs3c.** Now blocked.
- **Problem 8, claims-file contradiction.** The outcome is now not reproduced, and the contradiction is recorded for a reader. The claims file is not changed, which is correct.
- **Problem 9, motion exclusions.** Reading (b) now excludes three trials.
- **Problems 10 and 11.** The docstring is fixed, the G4 n is explained, and the stand-ins are stated.

**Still open and bearing on a conclusion:**
- **Old-ant placements fail on held-out trials.** Only 9 of 52 old-ant triples agree (cell 42). The method is now right, but every focal-glomerulus outcome still mostly reflects where the ROI was placed in old ants:
  - Claims that need old ants to be higher (fig3d, the late window of figs4d) are pushed toward failing.
  - Claims that need old ants to be lower (fig4) are pushed toward passing.
  - The fig4 notes give the fragile p-values but not this direction of bias. The spurious PGb/3-hexanone decline is the visible case.
- **figs2a's null result.** It comes from the same located ROIs that miss the paper's positive old-ant effects (fig3b, fig3d). By the logic used to block figs3c ("a null from a procedure that misses the paper's effect is not a test"), it is weak evidence. Data S2 itself gives p = 0.053 for 4-methyl-3-heptanol. I accept "reproduced (assumed)", but the notes should apply the same caveat explicitly.
- **fig3d-pg-60-vs-90-days-same, reading (a), held-out values (does not change the blocked outcome).** It uses only the 60-day values from the placement from all trials (cell 60). The held-out 60-day values, the main measure elsewhere, are not compared with the 000467 90-day values.
- **Claims-file problems, reported not corrected:**
  - pg-opposite-modulation's criterion contradicts fig4-propionic-acid-g2-g3.
  - fig3d-pg-60-vs-90-days-same's reading (b) mixes two pipelines.
  - The fig3d-pg-60-vs-90-days-same criterion has no rule for readings that disagree. Blocking is a defensible choice, but it is the author's, not the criterion's.
