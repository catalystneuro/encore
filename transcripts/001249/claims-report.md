I wrote `claims/001249/10.7554-elife.91765.yaml` and nothing is committed. The checker validates the file and finds all 26 quotes word for word. It flags 5 p-values it can't find, but I confirmed by reading that each is in the text as recorded (for example "p=0.001035889" and "p=6.80E-05"); the checker just doesn't generate those number formats.

**Text read**
- **Paper:** the eLife version of record (RP91765, 5 March 2025) from Europe PMC: main text, all figure and figure-supplement legends, Methods, and the authors' response to reviewers. Supplementary files 1 to 3, the tables of statistical results, are not in it.
- **Code:** github.com/stuberlab/Ishii-MPOA-Ejaculation-2023 at commit 4e98c43. The notebooks use the preprint's figure numbers; `Figure 2.ipynb` is the whole-brain analysis. It starts from densities already computed (`tdTomato_summary.csv` on Figshare). The image registration and cell-segmentation steps are not in the repository.
- **Dataset:** it holds only the Figure 2 whole-brain FosTRAP mapping: 14 brains, 4 appetitive, 5 consummatory and 5 post-ejaculatory. Everything else is on Figshare (doi:10.6084/m9.figshare.27642768.v1), so 19 claims are marked `elsewhere`.

**Counts**
- 26 claims: 1 link and 25 findings. The link checks that densities computed from the dandiset match the deposited `tdTomato_summary.csv`.
- All 26 have quotes and criteria, 18 have statistics (57 values), and 5 have expected values.
- The 7 claims on Figure 2 data are marked `with_inputs`, because they need the Kim lab Unified Anatomical Atlas (Chon et al. 2019) and the deposited density table, which come from outside the dandiset.

**Open details and the readings named**
- **Level-4 region set (Figure 2C):** the code uses 10 regions; the legend lists 12 (adding VERM and HEM).
- **Level-6 region set:** the code's (the regions under those 10), or all level-6 regions.
- **FDR threshold at level 4:** the Methods and legend say 0.05; the code uses 0.1. I followed the Methods and kept the code's value as a variant.
- **Tukey's test:** the Methods run it only on regions that pass the ANOVA; the code runs it on all. The p-values are the same, so significance requires both.
- **Region volume used for density:** the atlas volume, or each brain's own region volume.
- **Cell classifier:** the trained ilastik classifier is not deposited, so it has to be retrained as the Methods describe.
- **"Brain-wide" (Figure 2C):** Supplementary file 2, which lists the significant regions, is missing. The criterion sets the bar at the post-ejaculatory mean being higher in at least 80% of level-4 regions, with at least half significant. That threshold is my reading, not the paper's.
- **"Fourth largest difference" for the MPN:** ranked among the code's level-6 set, all level-6 regions, or all regions at every level.
- **Atlas names:** matching PVHd, PVH, PaV and MeA (atlas label "Me") to atlas regions, at the nearest level that holds them.
- **Other experiments:**
  - Decay length: time to first fall below 0, or total time below 0.
  - Response window: the Results say 15 s; the Methods average 0 to 5 s, which I followed.
  - Specific-cell counts: 177 and 46 in the Results, 178 and 48 in the legend; and two definitions of "specific".
  - The Figure 7 test: the legend says Wilcoxon rank sum; the code runs a paired signed-rank test. Rank sum is the main reading and signed-rank the variant.

**Missing from the paper**
- Supplementary files 1 to 3, so the per-region ANOVA and Tukey statistics for Figure 2 are not recorded.
- The image-processing pipeline and trained classifier are not in the paper or its code.
- The Figure 3J legend prints t(8)=-3.9487 for every Vglut2 row and for Vgat+ Prlr+, so I left those statistics out.
