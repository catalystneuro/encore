**Verifier report: Pelot et al. 2020, round 2**

The claims file has 43 claims. The attempt record has 43 outcomes: 37 reproduced, 3 partially reproduced, 3 not reproduced. The README states the same counts.

### 1. Outcomes and assumptions

I agree with all 43 outcomes. Four have changed since round 1, and the notes below cover those and the ones that still need a caveat.

- **fascicles-larger-cervical, reproduced.** Cell 64 uses Kenward-Roger df: human p < 0.00001, pig 0.012, rat 0.044. Satterthwaite df give much the same.
  - The flag `assumed` was removed. That is acceptable, because Kenward-Roger is the criterion's own method.
  - I read `mixed._kr` and `kr_test`. They follow Kenward and Roger (1997) and pbkrtest's formulas, with R_ij = 0.
  - The method has only been checked on balanced synthetic data (cell 10), not on an unbalanced design and not against JMP. The rat contrast is still close to 0.05, and with containment df it is 0.089. The outcome is sound but fragile.
- **literature-comparison-human-pig, partially reproduced** (was blocked). Cell 142: 9 of 12 parts hold.
  - The flag `assumed: true` is stated and reasonable. Two choices rest on it: the literature values are taken from DataPlotting_v4.m and matched to studies by the order of the Figure 7 legend (cell 140 checks that order), and the criterion's rules are applied.
  - One of the failed parts, "overlapping ranges", fails because literature diameters given with no SD (stored as 0) are treated as having zero spread. The notes say so.
- **rat-literature-comparison, partially reproduced** (was blocked). Cell 145: 1 of 3 cervical means lies within our mean ± SD, and the subdiaphragmatic mean is above all 4 published values. The claims file gives no rule for a partial result, so "partial" is a reasonable grade.
- **rat-carotid-sheath-bundles, reproduced** (was partial). I looked at the R24-3 image in cell 131. Bundles 3, 4 and 6 are small profiles with a perineurium. Bundle 5 sits in fat outside the dense adventitia, so whether it is "within the sheath" is open. The outcome rests on these calls, and the flag `assumed: true` says so. I accept six bundles.
- **human-subdiaphragmatic-fatty-tissue, not reproduced.** I looked at the full-resolution P5-1 crop in cell 134: adipocytes clearly lie inside the authors' nerve trace. Under the criterion's rule the outcome is correct.
  - That rule allows fat in at most 1 of 45 pig micrographs, which is stricter than the paper's comparative wording. I report this as a possible misreading in the claims file. The record flags the outcome as `assumed`.
- **pig-cervical-cell-bodies, reproduced.** The P11-1 crop in cell 137 shows large somata with nuclei. I agree.
- **Other `assumed: true` outcomes.** These are nerve-cervical-larger, rat-diameter-like-fascicle, rat-level-ratios, human-variability, pig-oblong-human-round, perineurium-no-level-difference, rat-perineurium-near-3-percent, human-pig-perineurium-thicker and no-age-trend. Each is stated and reasonable.

### 2. Sentences the outputs do not support

- **Cell 53 (fascicle-diameter-anova):** "With the rat fascicle the code keeps (variant), F = 9.05, 52.8 and 5.54, closer to the paper's." This holds for species and level only. For the interaction the variant gives 5.54 and the main fit 5.20, against the paper's 5.273, so the variant is further away.
- **Cell 62 (subdiaphragmatic-fascicle-diameter-comparable):** "the rat p values are 0.898 and 0.995, the paper's to the third decimal." The first is 0.8981 against the paper's 0.896, which differs at the third decimal.
- **Code-mismatch finding (11) and rat-fascicle-diameter notes:** "its rat Tukey p values follow the code". This holds only for the subdiaphragmatic pairs (cell 61).
  - For rat cervical vs subdiaphragmatic, the code's fascicle gives p = 0.0089 and the largest fascicle 0.044 (cell 64). The paper's 0.0234 lies between them.
  - For rat vs pig cervical, the code's fascicle gives 0.1426 and the paper has 0.1707 (cell 58).
- **rat-level-ratios notes:** "Reading (a) … gives 0.271 and 0.525". Cell 76 prints 0.270, and the record's own response gives 0.270.
- **Cell 132 (rat-carotid-sheath-bundles):** "the largest count would be five unless R17-3's open circle is a bundle". R18-1's open circle would also raise its count to six (cell 131 output).
- **Finding 1:** "effective nerve diameters of monofascicular samples are 0.3 to 3.5% smaller". The outputs print no per-sample comparison of version 1 with version 5. Cell 6 gives only a file-to-version-5 ratio range of 1.0017 to 2.0779, and that range includes the multifascicular samples.
- **Findings 6 and 7:** the copy of C51-3 under sub-50/sam-2, C63-1's derivative under sub-63/ with no sample folder, and the byte-identical P9-3 scale bar appear in no printed output. Only the copy of C63-1 under sub-62/sam-1 is visible, in the file log of cell 147.
- **README:** "about 8 minutes, 1.5 GB". Cell 147 prints 428 s and 1.30 GB. This is close enough.

Everything else checks against the outputs, including the Summary's statement that F values come within 0.2% to 9% of the paper's.

**My round-1 reasons in the record.** They are stated faithfully and in substance in my words. They add my problem numbers and descriptions where relevant, and the `reviewed` field describes accurately what I did.

### 3. Round-1 points

**Resolved:**
- Problem 2: the rat fascicle the code keeps. The per-fascicle table and the first-ring variant (121.1 ± 32.3 µm) are in cell 55.
- Problem 3: no change was needed.
- Problem 6: the strict reading is printed, and the version 1 minimum of 4.7 µm explains the paper's 5 µm.
- Problem 7: diagnosed as far as the files allow (cell 123).
- Problem 8: fixed; version 1 matches the deposited file to within 4e-6 (cell 8).
- Problem 9: full-resolution, annotated images are now shown.
- Problem 10: recorded as a deviation and put as a question to a reader.
- Problem 11: version 1 counts of all 18 pig samples are printed (cell 7).
- Problem 12: resolved (cell 8).
- The archive check for the two blocked claims: the literature values are now parsed from the code.

**Partly resolved:** problem 1. Kenward-Roger df are now computed, but checked only on balanced data. The pig p of 0.012 against the paper's 0.0009 is unexplained.

**Remaining issues that bear on a conclusion:**
- **fascicles-larger-cervical:** fragile. Rat p = 0.044 with the largest fascicle, and Kenward-Roger is unverified on these unbalanced data.
- **no-age-trend:** the not-reproduced outcome rests on the claims file counting uncorrected p values. After correction, none of the 27 tests is below 0.05 (cell 126).
- **perineurium-no-level-difference:** still not reproduced. My problem-4 objection, that the tests treat fascicles as independent, is answered for humans: the difference remains under sample clustering (cell 108). For pigs it is not answered.
- **human-subdiaphragmatic-fatty-tissue:** rests on the claims file's pig rule, which is possibly a misreading.
- **rat-carotid-sheath-bundles:** rests on the by-eye calls of bundles 3, 5 and 6 in R24-3.
- **Literature claims:** both rest on the claims file's rules and on the treatment of literature values with no SD.

### 4. Critical findings

No finding in the record is rated `critical`.

I would rate **finding 2** `critical` instead of `major`. It concerns the deposited output metrics file (`CadaverVNMorphology_OutputMetrics.mat`, also deposited in sparc-60 under the rat file name):
- Its pig fascicle diameters are about 1.40 times those measured from the masks and reported in the paper. The factor varies from 1.36 to 1.61 per fascicle, so it is not a scale error (cell 6: median ratio 1.4022; cell 7: 1.360 to 1.610).
- Its pig fascicle counts are those of the superseded version 1 masks: they equal version 1 in 18 of 18 samples and version 4 in only 7 (cell 7).
- Nothing in the datasets flags this. An analysis that takes the file as given would report pig fascicle diameters about 40% too large, with no sign that anything is wrong.

The other ratings are acceptable.
