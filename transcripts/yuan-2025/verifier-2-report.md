**Round 2 verifier report: 001882-yuan-2025-01 (Yuan et al. 2025, DANDI:001882)**

## 1. Outcomes

The claims file has 26 claims and the attempt record has 26 outcomes. The record gives 9 reproduced, 9 partially reproduced, 3 not reproduced and 5 blocked (data missing).

I agree with 25 of them as recorded. These cover cohort-prevalence, all-caucasian, the four Table 1 claims, the three Figure 2 claims, vmd-acuity-preserved, the six Figure 3 claims, m73-eog-normal, other-gene-variants, variant-domains, table2-pathogenicity, asp423glu-novel, the two interaction claims, table4 and gnomad-frequencies. The printed outputs (cells 13–79) support each one.

**table3-destabilizing (not reproduced): I agree, with a reservation that bears on the outcome.**
- In round 1 this claim was blocked. It is now not reproduced on the strength of I-Mutant 2.0 run from sequence (cell 70). The regression gives positive values for 4 of 5 variants, and the sign classifier calls p.Asp423Glu "Increase" with reliability 8.
- The claims file says "iMutant and MuPRO run from sequence". The paper does not say this. Methods 2.4 gives only the URL. Its reference 46 is "I-Mutant2.0: Predicting stability changes upon mutation from the protein sequence **or structure**". The paper had also built I-TASSER models "for further analysis" (Methods 2.3). The sequence-only reading may therefore be a misreading by the claims file; I report this and do not correct it.
- Two further signs that the paper did not use sequence mode:
  - Neither sequence-mode output gives the paper's IMPG1 iMutant values (−0.85, −0.76). The server gives +0.19 and +0.88.
  - The server's regression and classifier disagree in sign for p.Cys1019Tyr and p.Leu249Phe.
- The record does not state this dependence and does not mark the outcome assumed. Given the claims file as written, not reproduced follows. The failure rests on one tool, in one mode, from an unversioned server.

**Assumptions (`assumed: true`)**
- **m73-f57-similar-lesions.** The assumption is stated in the deviations, the notes, cell 42 and cell 56, and it is reasonable. Reading (5) asks whether the maximum is above 95% of same-size background discs. For M73's right eye, readings (1), (4) and (5) say not bright and readings (2) and (3) say bright (cell 43). The outcome does rest on it: under (2) or (3) all three parts hold, and the record says so.
  - One correction to how it is described: the "background fundus" discs are centred 110 px from the lesion, so they lie inside the 80–140 px surround ring (`impg.faf_measures`). They are the perimacular ring, not the general fundus.
- **m73-vmd-phenotype.** The assumption is stated, but this outcome does not rest on it. Cell 50 and the notes say it is "partial under every reading (5 of 6 at most)", because dot-blot haemorrhages are not discernible. The flag is therefore unnecessary. The README's "the M73 claims rest on it" overstates the case for this claim.

## 2. Sentences the outputs do not support

- **The number of `desktop.ini` files.** These all say there are six:
  - cell 0: "six Windows `desktop.ini` files";
  - cell 9's print text: "the six desktop.ini files are";
  - cell 10: "The six `desktop.ini` files are identical";
  - Summary (cell 80): "Six `desktop.ini` files from Google Drive are deposited";
  - the record's finding: "Six Google Drive desktop.ini files and the script setup_bids.py … are among the 13 assets".

  Cell 3 lists 5, and cell 9 prints "are 5 of them". The 9 distinct digests also add up only with 5 identical files (8 other assets plus 1).
- **Summary (cell 80): "The Word document differs from Table 3 in four values (SDM p.Cys1019Tyr … iMutant p.Arg131Cys … MuPRO p.Leu249Phe … mCSM p.Asp423Glu)".**
  - Cell 70 also shows DUET p.Leu249Phe differing (−1.777 against −1.77).
  - Cell 70 marks SDM p.Cys1019Tyr and iMutant p.Arg131Cys as agreeing within 10%. Its own count is 3 values outside tolerance (20 of 23 agree).
- **m75 notes in the record: "95th percentile 0.89".** Cell 43 prints 0.896, which rounds to 0.90. This is trivial.
- **Unsupported by any printed output (cell 0 and the deviations):** that the draft holds the same 13 assets; that UniSave versions 129 and 146 were current in November 2024 (cell 61 prints only the entry ID line); and that `gnomad_r4` serves v4.1. None of these changes an outcome.
- **The record's verification block** states my round-1 reasons in my own words, and accurately, with one exception. My problem 1 said the spreadsheet is the authors' source file for Table 1, so the reproduced Table 1 claims are agreement of the deposit with the paper rather than independent evidence. The record (reason for f32, and the "reviewed" text) narrows this to "the phenotype verdicts". The README and the notebook do not say it of the Table 1 claims.

Every other "**Result:**" sentence I checked, along with the Summary, the README and the record's notes, matches the printed outputs. This includes all the FAF figures, the five-reading table, the domain counts (6/6/6/4/4), CADD (at most 2 of 7), HumDiv (3 of 5), the MuPRO and I-Mutant values, ClinVar's dates, the 14 of 18 Table 4 values and gnomAD v4.1 joint at 6 of 6.

## 3. Round-1 points

**Resolved**
- **Problem 2:** the arrows are now masked, and five readings are shown and stated as an assumption.
- **Problem 3:** dbNSFP's lists are shown with the MANE index, the FATHMM-MKL server was run, and MutationTaster2021 was tried and does not answer.
- **Problem 4:** recorded as a finding.
- **Problem 5:** every member-database row is printed, and none has a second IMPG2 EGF-like domain.
- **Problem 6:** the reason is now `data_missing`, and the sequence tools were run.
- **Problem 8:** printed and stated.
- **Problem 9:** CLNHGVS, the condition, the summary and the first release are printed.
- **Problem 10:** recorded as a finding.
- **The Word document images:** now shown.

**Partly resolved**
- **Problem 1:** the point is acknowledged for the figures but not for the Table 1 spreadsheet claims. It does not affect a conclusion.
- **Problem 7:** ExPASy's own code was not run. The argument from the +0.003 shift is sound, and the result does not affect a conclusion.

**What remains that bears on a conclusion**
1. **table3-destabilizing** rests on the claims file's sequence-only reading of I-Mutant 2.0, which the paper does not state. The record should say this, and arguably mark the outcome assumed.
2. **m73-f57-similar-lesions** turns on the FAF reading chosen for M73's right eye. It is stated and marked assumed, but it is still decisive: readings (2) and (3) would make the claim reproduced.
