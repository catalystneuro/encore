I wrote `claims/001785/10.1038-s41593-026-02301-4.yaml`. The earlier reader run stopped because the supplement was missing; it is now in `paper/`, so nothing a claim needs is missing.

**Text read:** the version of record from Europe PMC (PMC13337501): main text, Methods, figure and Extended Data legends, plus the Supplementary Information PDF (Supplementary Methods 1–7, Supplementary Tables 1–11), all in the `.txt`. There was no article PDF, and I didn't need one.

**Code read:** the paper's code is in DANDI:001773 version 0.260416.1939: 17 MATLAB scripts and the source-data spreadsheets. I took from it the ANOVA models (monkey as a main effect, MATLAB's default type III sums of squares), the Tukey–Kramer comparisons over the PrePost × side × tract (or ROI) cells, the paired t-test for monkey D, and the network membership. The reported error df all match these models.

**Counts:** 31 claims, all with quotes and criteria; 21 have statistics and 11 have expected values. Data: 10 `dataset`, 19 `with_inputs` (they need the D99, CHARM and SARM atlases in NMT v2.0, distributed with AFNI and listed on PRIME-DRE), and 2 `elsewhere` (the behavior bins, which are only in 001773, `source_data/dbs_behavior_data_a.xlsx`). The quote checker found every quote. It flagged 7 p-values it couldn't match because of how they are printed; I checked each against the text and they are correct.

**Details the paper leaves open, with the readings named:**
- **Tract masks:** the seed masks were drawn by hand and are not given. The FA claims need the paper's masks from the dataset; the reported voxel counts check them.
- **Lead-track voxels excluded from FA:** found (a) from the CT-defined lead location, or (b) from the visible track in the post-DBS images.
- **CB subregions "adjacent to" D99 areas:** (a) the nearest D99 label, or (b) each area's front-to-back extent.
- **CC1/DAPI counting thresholds:** not reported. If the dataset holds images only: (a) FIJI IsoData or (b) Otsu, per section and channel.
- **Pairing of fields in monkey D's paired t-test:** by section and field index, the only reading the text allows.
- **FC matrix:** one matrix per run, then averaged (Methods), or one per session on all runs together (code, kept as a variant).
- **Per-ROI test in Fig. 4b:** rank-sum of the ROI's changes against zeros (code and legend), or of pre against post values (Methods wording). The threshold is open between p < 0.01/122 (Methods) and p < 0.05/122 (code). Supplementary Tables 1, 2 and 10 follow the code.
- **Circular-plot threshold:** 0.1 in the legend, 0.15 in the code (variant).
- **Seed connectivity:**
  - Runs: per run then averaged, or the session's full series.
  - Normalizing maximum: over all brain voxels, or outside the seed.
  - Voxel grid: 1.5 or 1.6 mm. Supplementary Table 8's counts decide.
- **Voxel test behind the thresholded seed maps:** not stated. Named readings are a per-voxel two-sample test across runs, or a one-sample test of each animal's change.
- **Summaries the paper judges by eye** ("broad reduction", "no systematic pattern"): the mean or the median over ROI pairs.

**Settled by the code where the Methods disagree:** the limbic network includes the contralateral area 25. The code and Extended Data Fig. 9a include it, and so does the reported n = 821; the Methods list leaves it out.

**Errors in the paper, noted in the file:**
- Fig. 6a prints "F 1,1238 = 6.02, P = 0.0025", but P = 0.0025 needs 2 df, which the three-way term has, so the 1 is taken as a misprint.
- Supplementary Tables 3, 4 and 11 (effect sizes) are identical, so I didn't use them.
- Extended Data Fig. 10d says monkey D's post scan was "10 weeks" after implantation; the Methods say 6 weeks without stimulation after the 4-week recovery.

Nothing is committed; the other untracked files in the working tree aren't mine.
