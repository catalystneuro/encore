I've taken up all seven answers. Two claims changed outcome: edfig6-classifier-morphoelectric is now reproduced and fig1a-thickness reproduced for the human value. Fig6a-deep-dendrites now runs but stays blocked because its readings disagree. The rest keep their earlier outcomes.

The final run of `python tools/entry.py all entries/000023-berg-2020` passed with 0 errors, in 25.6 minutes. I ran lock first and handover after, and read the executed copy: the conclusions match the printed numbers. Nothing is committed or pushed. The changed files are the notebook, `README.md`, `entry.yaml` (runtime now 26 minutes) and `attempts/000023-berg-2020-01.yaml`.

## Per question

**1. How cells are linked (features-and-labels-link, plus 13 claims that need the link).** The answer accepts both readings: M1 (a specimen ID stored in the files) and M2 (the ID recovered from each file's session id), with each dependent claim naming the one it uses. No number changed.
- **features-and-labels-link:** reproduced under M2 (before: reproduced, M2). Under M1, 0 files match, so it would be not reproduced; the notebook and notes now say so.
- **The 13 dependent claims:** each claim's notes now say it uses M2, and that under M1 it could not be tested. Their outcomes are unchanged:
  - not reproduced: cohort-cells, cohort-donors, cohort-type-counts
  - partially reproduced: fig3d-depth-by-type, fig4e-human-ephys-anova, fig5c-frem3-ephys-depth, fig6-deep-ephys-anova, fig2ef-pathology-ephys
  - reproduced: fig4-glp2r-sag, edtable1-species-ephys, edfig6-classifier-human-ephys, fig6c-col22a1-rin-fi-sag
  - blocked: fig6c-carm1p1-upstroke-rin

**2. Which bins make up deep L3 (fig1c-soma-variation).** The answer picks the code's five bins (D1), with a variant (D2) that drops the deepest bin.
- **fig1c-soma-variation:** blocked, other (before: blocked, other). The method is settled, but every mouse soma in the repository's section files lies at scaled depth -1, so D1 holds no mouse soma. The human SD in D1 is 117.6 µm². The variant without the deepest bin holds no mouse soma either, so the earlier ratio of 5.74 no longer appears.

**3. How soma-area quartiles are taken (fig1c-soma-area).** The answer says pooled over all somata of a species, and adds that the largest human soma must exceed 850 µm². Per-section quartiles are now reported only.
- **fig1c-soma-area:** partially reproduced (before: partially reproduced). Human 107.5 and 252.6 µm², largest 886.4 µm²: within tolerance. Mouse 24.4 and 61.0 µm², not 44 and 96, because of the mouse section files.

**4. Where the mouse cortical thickness comes from (fig1a-thickness).** The answer says the source is unknown; the claim is now judged on the human value alone.
- **fig1a-thickness:** reproduced (before: blocked, methods underspecified). Human L2 plus L3 is 1.231 ± 0.155 mm, against 1.23 ± 0.15. The mouse value of 1.06 mm and the ratio of 1.16 are recorded as untested.

**5. Method and features for the morphology tests (fig5b-frem3-morph-depth, fig6-deep-morph-anova, fig4f-morph-anova).** The answer: use all 60 features and drop any feature with no p-value before the correction, as the code does. The paper's 58 is the 60 less two constant features, not less the two location features I had guessed.
- **fig5b-frem3-morph-depth:** reproduced, 37 and 28 over the 58 kept (before: reproduced, 37 and 28). The earlier 58-feature reading, without the location features, is kept for reference (35 and 26).
- **fig6-deep-morph-anova:** reproduced, 24 and 20 over 59 kept (before: reproduced, 24 and 20).
- **fig4f-morph-anova:** reproduced, 16 of 58 kept for human and 12 of 59 for mouse, 10 of them significant (before: reproduced, 16 and 12).

**6. Total dendritic length and sparse branching (fig6a-deep-dendrites).** The answer says the paper gives no method and lists the allowed readings. The claim must hold under all of them, or it counts as methods underspecified.
- **fig6a-deep-dendrites:** blocked, methods underspecified (before: blocked, methods underspecified, for lack of a criterion). It now runs, and the readings disagree:
  - With FREM3 split at 0.575, deep FREM3 has the largest median total length (12,024 µm, against 10,447 for CARM1P1).
  - CARM1P1 is largest under the other three readings.
  - COL22A1 has the fewest branches under every reading.
  - The apical part of the sentence does not hold: CARM1P1's mean apical length (6,896 µm) is above deep FREM3's (5,443 µm).

**7. The combined morphology and electrophysiology classifier (edfig6-classifier-morphoelectric).** The answer: use the electrophysiology classifier's method on cells that have all 18 features and a reconstruction; no values need imputing.
- **edfig6-classifier-morphoelectric:** reproduced (before: blocked, methods underspecified). On the code's tables:
  - Human (72 cells): 0.720, against 0.69 ± 0.069. Electrophysiology alone on the same cells gives 0.679.
  - Mouse (50 cells): 0.582, against 0.60 ± 0.06. Electrophysiology alone gives 0.527.
  - With the human features computed here from the dandiset (75 cells), the combined accuracy is 0.702.

  One deviation: this claim runs 250 splits, not the 1000 its method specifies, to stay under the 30-minute limit. The standard error of each mean is 0.007 or less, against tolerances of 0.06 and 0.069.

The verifier's package is in `executed/000023-berg-2020/handover/`.
