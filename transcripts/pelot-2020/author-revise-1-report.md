The entry passes `tools/entry.py all` (447 s), and the record passes `check`. Outcomes now: 37 reproduced, 3 partially reproduced, 3 not reproduced, 0 blocked (before: 36, 2, 3, 2). Nothing is committed.

**Outcome changes (allowed in round 1)**
- **literature-comparison-human-pig: blocked → partially_reproduced.** The verifier was right: `DataPlotting_v4.m` hard-codes the Figure 7 literature means and SDs, in the legend's order. The notebook now reads them from the file. 9 of 12 parts hold. The human cervical endoneurial area, the overlapping ranges, and the posterior-branch subdiaphragmatic sizes fail.
- **rat-literature-comparison: blocked → partially_reproduced.** The subdiaphragmatic part holds against all 4 published values. Only 1 of the 3 published cervical means falls within our mean ± SD.
- **rat-carotid-sheath-bundles: partially → reproduced.** At full resolution R24-3 holds six bundles; the thumbnails missed two small ones. Each counted bundle is now numbered on the images, and eight profiles that could be vessels are circled and not counted. Counting them would put no section above six. This still rests on calls made by eye.

**Fixes and added outputs**
- **Degrees of freedom (problem 1):** Kenward-Roger is now implemented in `mixed.py` and is the main reading. It reproduces the classical split-plot tests on balanced synthetic data; it has not been checked against JMP itself. Under it, fascicles-larger-cervical holds on the claims file's own method: pig p = 0.012, rat p = 0.044.
- **Rat fascicle choice (problem 2):** the verifier was right here too. The paper's code keeps the first ring in boundary order, not the largest, and that reproduces the paper's 0.121 ± 0.032 mm and its rat p values. The criterion's "largest" still decides the outcomes; the code's choice is shown as a variant and recorded as a `code_mismatch` finding.
- **Hole areas (problem 8):** now measured as MATLAB traces them. Cervical rat diameters match the deposited file to within 4e-6. Small numbers shifted; no outcome changed.
- **Variants added:**
  - Sample-clustered tests for perineurium-no-level-difference. The human difference remains; the pig one goes away.
  - Holm and Benjamini-Hochberg corrections for no-age-trend: no test stays below 0.05.
  - The strict-bound reading for pig-if-mt-consistent: the MT minimum fails it. The version 1 masks have a 4.7 µm trace, so the paper's 5 µm probably comes from them.
- **Other outputs:**
  - Per-sample peanut counts. No nested outer traces; the paper's 25 cannot be traced from the deposited files.
  - Version 1 pig counts for all 18 samples: they match the deposited file in 18 of 18.
  - A comparison of the two human nerve traces.
  - Full-resolution crops of the pig cell-body fascicles and the P14-2 fascicles (no somata).
  - Pig fat regions with the authors' nerve traces drawn over them: the fat lies inside the traced nerve.
- **Record:**
  - Round-1 `verifications` block covering all 43 claims; the verifier agreed with every outcome it reviewed.
  - Two findings updated in place. Three new findings added at the end, so the existing numbers still point at the same findings.
- **Questions file:** new `questions/pelot-2020.yaml` asks a reader about four claims: the Sunderland data (deposited in sparc-65, not elsewhere), the independence assumption in perineurium-no-level-difference, the multiplicity correction in no-age-trend, and the rat fascicle selection.

**Not done**
- No claim was changed.
- KR has not been compared with JMP or R's pbkrtest; R is not installed here.
- The right-side rat sheaths were not re-read at full resolution. They do not decide the outcome.
- The roughly 1.4× pig fascicle diameters in the deposited file stay unexplained. The per-fascicle ratio ranges from 1.36 to 1.61, so it is not a scale factor.
- The executed notebook is now 14 MB, up from 9.5 MB, because of the full-resolution images.
