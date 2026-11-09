**Round 2 verifier report: 000008-scala-2021-01 (Scala, Kobak et al. 2021, DANDI:000008)**

Counts come from the claims file and the attempt record's `outcomes`. There are 35 claims: 25 reproduced, 4 partially reproduced, 1 not reproduced and 5 blocked (4 methods_underspecified, 1 data_unreadable).

## 1. Stated outcomes

I agree with all 35 stated outcomes.

- **Changed since round 1:**
  - **cohort-cells-mice:** now reproduced (1,328 distinct cells, 266 mice; ephys cell 20), which matches my round-1 outcome.
- **Blocked reason:**
  - **ed6-physiological-temperature and fig4e-pvalb-axon-shape:** in round 1 I gave both as blocked for data_missing. I now accept methods_underspecified. Both claims are `data: elsewhere`, and both criteria themselves say the paper gives no measure ("a test would be chosen by an agent"). I could not check the protocol rule the author cites, because docs/protocol.md is not among my materials.
- **Kept, but marginal:**
  - **fig5d-sst-pvalb-calb2-firing:** reproduced, but marginal (see 3).
  - **fig5b-ttype-variability:** reproduced, but fragile.
  - **ed8-leiden-entropy:** not reproduced, also fragile.
  - **fig1a-ttype-coverage:** partially reproduced; this rests on a gap in the claims file, not on the notebook.
- **ed6-it-et-room-features and fig4b-sst-rebound:** now use the layer as the claims file defines it.
  - ed6 still gives the same four features (ephys cell 49).
  - fig4b gives r = 0.339, p = 0.0113 (transcriptomics cell 24).
  - Neither outcome changes.

## 2. Sentences the printed outputs do not support

All "**Result:**" conclusions, the three Summary sections and the record's notes otherwise match the printed numbers.

1. **Ephys cell 7:** "the values run from about -150 to +80 with resting values near -65". Nothing printed shows this.
   - Cell 5 prints min −1,025.4 and max 1,025.7, and per-file baselines of −78.5 to −54.7 (5th–95th percentile).
   - No −150/+80 range is printed.
2. **Sequencing cell 3:** "the exon sums are a few percent higher than `Exon reads` in most cells". Cell 2 prints a median ratio of 1.035 but a 5th–95th percentile range of 0.384 to 3.078. That supports "a median 3.5% higher" but not "most cells".
3. **Ephys cell 74 and the hold-time-yield notes:** both say every entry under `general` was listed and holds no hold time. Cell 6 lists `general` for one file only, and it is a low-quality cell. The DandiIcephysMetadata and subject fields, by contrast, are listed across all files, and they do support the conclusion. The record's own response to round 1 correctly says "of one file".
4. **README table labels:**
   - "1,329 cells from 266 mice | Reproduced" and "1,284 cells with a soma depth | Reproduced" read as though those numbers were reproduced. The dandiset gives 1,328 and 1,283, the values the criteria accept (ephys cells 20 and 32).
   - Smaller: the README says each of the ephys and transcriptomics notebooks takes about 18 min, but the printed run times are 9.0 min (ephys cell 79) and 10.0 min (transcriptomics cell 34).

**My round-1 reasons in the attempt record:** they are stated faithfully and in my own words, for every claim. That includes the two blocked-reason disagreements and the B/C points I attached to claims (B1, B3–B8, B10–B13, and the C items).
- My two general helper points, B2 and B9, are not recorded. Neither is tied to a claim.
- The cell numbers in my reasons are round-1 numbering and no longer match the re-executed notebook (for example, cohort-cells-mice is now cell 20, not 18). They are correct as a record of round 1.

## 3. Round-1 points

**Resolved:**
- **B1:** the layer now comes from the depth, using the Nissl boundaries. Both variants are shown and the outcomes are unchanged (ephys cell 49; transcriptomics cell 24).
- **B2:** the strict boundary rule is now documented as the code's rule (`scala.layer_from_depth`). It is now used in the main readings.
- **B6:** two library-size normalizations were added; both give ρ ≈ 0.02–0.07 (transcriptomics cell 27).
- **B7:** the field lists now cover all files (ephys cell 6), apart from point 3 above.
- **B8:** the comparison is now exact (ephys cell 13).
- **B11:** cells from phenotype-tsne.ipynb are cited. With all cells, 628 cells have both, and the orderings hold (ephys cell 61).
- **B12:** `leiden_entropies` now takes the label as an argument.
- **C items:**
  - the RRR folds are printed (transcriptomics cell 6);
  - the stimulus cross-tabulation is printed: 87 of the 90 cells starting at −100 pA end at 1,480 pA (ephys cell 29);
  - for fig5d, no cell sits at the median of 32.5, which splits the cells 13/13 (transcriptomics cell 30).
- **B9 and B13:** no action was needed.

**What remains that bears on a conclusion:**
- **fig5d (B3):** the outcome of reading (b) depends on the seed.
  - Seed 55 gives an upper bound of 0.0499; seeds 56–60 give upper bounds of 0.0510 to 0.0528, all failing the rule.
  - The exact p is 0.0497.
  - The follow-up question in questions/000008.yaml is still open.
- **fig5b (B4):** the share above the band runs from 22% to 56% across n_init and membership variants, and 2 of the 8 variants fall below 25%. The main reading is 15 of 35 (43%).
- **ed8 (B5):** the outcome flips with membership. The main reading gives p = 0.061; the code's membership with duplicates removed gives p = 0.031. The criterion does not say which handling governs.
- **fig1a (B10):** the claims file does not say whether the allowance for the missing cell covers the t-type it alone represents (76 against 77). The question is open in questions/000008.yaml.
- **morph-reconstructions:** the Brain Image Library still did not answer (ephys cell 76, 2026-10-21), so the blocked outcome cannot be re-checked.
- **fig5c reading (b):** I cannot check the claim that the main transform is the code's `normalizeNew` path, because rnaseqTools is not among my materials. All four transforms agree (ρ from 0.016 to 0.068), so this does not affect the outcome.
