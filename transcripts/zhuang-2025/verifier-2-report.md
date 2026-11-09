# Round 2 verification: Zhuang et al. 2025 (attempt 001177-zhuang-2025-01)

## 1. Outcomes

The claims file has 44 claims: 14 on the dataset and 30 elsewhere. The attempt record gives 18 reproduced, 8 partially reproduced, 2 not reproduced and 16 blocked (14 `data_missing`, 1 `metadata_insufficient`, 1 `other`). It tests 28 claims.

I agree with 43 of the 44 outcomes, including the fig5jl change to not_reproduced, which was my round-1 point. The one I disagree with is figs2ijk-ppx-washout.

Three outcomes rest on an assumption (`assumed: true`):

- **fig2bc-a77636-locomotion (injection at 20 min):** stated and reasonable. 25 of 26 files have a gap at 20.0–20.3 min (cell 90), and the Methods give a −20 to 0 min baseline.
- **fig5cf-cno-locomotion (same assumption):** stated and reasonable. The weak points are shown openly:
  - 12 files have no gap, and their per-minute velocity is printed (cell 92).
  - With only the files that have a gap, mCherry gives p = 0.16 or 0.22.
  - Only 3 hM4Di files have a gap, too few to test.
- **figs2ijk-ppx-washout (Bonferroni by paired t tests, not on the pooled error):** stated, but I do not think it is the better-supported choice.
  - The paper's printed p-values favour the pooled error. Baseline against OFF is K p = 0.01 and AUC p < 0.01. Pooled gives 0.028 and 0.0072; paired gives 0.063 and 0.039 (cells 32 and 35).
  - So pooled matches the paper's significance pattern in all six Table 1 and legend comparisons, and paired misses two.
  - Paired is closer only on ON against OFF AUC (0.0011 against 0.0019; pooled 0.0051), and both are significant there.
  - The record's case for paired rests only on Prism's guide. `icd.rm_oneway`'s own docstring (icd.py:487) says the pooled comparisons are "as GraphPad Prism makes them by default", and calls the paired tests "Table 1's reading" without support.
  - I would record reproduced, with the pooled error as the stated assumption. At least the record should give the evidence from the paper's p-values and resolve the docstring contradiction.

## 2. Text against printed outputs

I checked every Result conclusion, the Summary, the README and every outcome note. Except for the points below, every number matches the printed outputs.

- **"Every baseline session deposited (2 to 5 per mouse)"** (cell 94, and the record's `selection_undocumented` finding): cell 20 prints H2.1 with 1 baseline before its first drug session. The total number of baselines per mouse is never printed, so "2 to 5" is unsupported. The fig1fg notes correctly say "1 to 5" before the first drug session.
- **"No sorted units"** (README lines 9–10) and "the dandiset has no sorted, classified or optically identified units" (cell 0): cells 4 and 6 show two files with a units table that is "consistent with an unsorted and a sorted cluster per channel". The record's notes and the Summary ("no sorted units in 54 files, no unit labels in the other two") are accurate; the README and cell 0 overstate it.
- **"Twelve files (all 2023 H and J mice …)"** (cell 93) and "(the 2023 H and J mice …)" (fig5cf notes): H1 and J3 are also 2023 H and J files, and they have gaps at 17.7 and 18.5 min (cell 92).
  - The "with a gap at 19.5–21 min" subset counts 7 mCherry files, so H1 and J3 must have a second gap in that window.
  - The `gap_19_21` values are never printed. The count is printed but not checkable per file.
- **My round-1 reason for fig2bc** quotes p = 0.020 for the 10 listed parkinsonian mice, from my own recomputation. Cell 90 now prints p = 0.0137. My figure was off; the conclusion does not change.
- **My round-1 reasons are in the record in my own words.** Problem points 1–8 and 11 and the relevant part-C items are folded into the per-claim reasons. Two small things are left out, and neither affected a conclusion:
  - Problems 9 and 10 appear in no reason. Problem 10 is now answered by cell 8 and a finding.
  - The electrophysiology reasons drop my notes on the K4 "optoSession" file and on the draft version.

## 3. Round-1 points

**Resolved:**

- **Point 1:** both ON readings are run (first: r = 0.08). The unmatched IDs are listed: C3.1, E3.3, E4, H4.1, N1 and N5.1 have no histology; E6 has no PPX session; E3 and E3.2 are in no list.
- **Point 3:** all four ON/OFF pairs are run. The Dunn p for K is never below 0.19.
- **Points 5 to 9:** stated or tested.
- **Point 10:** cell 8 shows the shared files are training logs plus 18 and 14 baselines, with no drug or washout file.
- **Point 11:** recorded as a `paper_inconsistency` finding.
- **Every part-C item is now printed:** the log-event walk-through, the KRT and README sex search, the per-minute CNO velocity, the instrumental headers, the per-mouse stability CVs, and the `unit_name` values.

**Remaining, each bearing on a conclusion:**

- **figs2ijk-ppx-washout (point 4):** the pooled comparisons are now run, but the adopted paired choice is the weaker one (section 1). This decides partially reproduced against reproduced.
- **fig5cf-cno-locomotion (point 2):** resolved as far as the deposit allows and flagged as assumed. The significant mCherry slowing, which is what makes this partial, depends on the 5 mCherry files with no injection mark.
- **fig3a-a-correlates-dms:** 24 of the paper's 28 mice can be matched, and E3.3 against E3 or E3.2 cannot be settled from the deposit. Not reproduced stands under both ON readings and both normalisations. The missing 4 mice are the only route by which r could reach 0.46, which I think is unlikely.

On the claims file, I again found no misreading of the paper.
