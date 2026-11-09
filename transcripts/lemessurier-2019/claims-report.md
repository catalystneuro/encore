I wrote `claims/crcns-ssc-10/10.7554-elife.46321.yaml`. The quote checker passes except for two Figure 7D p-values: the text prints them as "p= 2 * 10 - 6", so the checker can't match them, and I confirmed them by reading the text.

**Text read:** the version of record (PMC6697414, Europe PMC full text), with Results, Discussion, Methods, Table 1 and all figure and figure-supplement legends. The paper has no separate supplementary text and no PDF was supplied, so no figure was read. I also read the linked code, github.com/alemessurier/imaging_analysis_pipeline at commit 5a21c9f. It is incomplete: many functions the figure scripts call are missing, including the one computing equivalent best whiskers (eBWs), the responsive-cell selection, the correlation functions and the decoder.

**Claims:** 34. 33 have quotes; one (Table 1 counts) is marked inferred. 31 claims carry 41 statistical values: mostly permutation tests, plus Fisher's exact tests, 2-way ANOVAs and a slope t-test. 29 claims have expected values. Where the paper gives ± SEM, the SEM is the tolerance; elsewhere it is 10% of the value. Every claim has a criterion except the bare Table 1 counts. Three claims have no reported test: the L4-sharper claim, the barrel-versus-septum sharpening, and the correlation gradient at column edges.

**Details the paper leaves open, with the readings named:**
- **eBW test:** the Results say "see Materials and methods", but neither the Methods nor the code define it. Readings: the paper's two-sided permutation test, uncorrected (E1), with FDR over 8 comparisons (E2), or on medians (E3).
- **Which L2/3 cells enter:** all responsive ROIs, or only those over the nine barrels. For L4, all responsive ROIs or only those in C1 to C3.
- **Z-score centre:** the blank mean, or the blank median as a variant.
- **Best whisker:** by mean (as the Results say) or by median.
- **Methods against code**, where I followed the Methods and named the code as a variant: the responsiveness test (one-sided on means in the Methods, two-sided and mean or median per field in the code), the filter width, and F0 (20th against 5th percentile).
- **Per-claim gaps:**
  - The measure for "sharper in L4": a 225-300 µm to 0-75 µm ratio, or the half-max distance.
  - "Highly similar" in Figure 1F: same best whisker, or a significant correlation.
  - Which response the p = 0.0002 in Figure 4 supplement 1 compares: the four strongest whiskers or all nine.
  - Whether the "columns with at least 3 ROIs" rule applies to Figure 4D.
  - The 48% in the Discussion: pooled, or the mean over columns.
- **Decoder:** 80/20 splits against K-fold, class balance, which ROIs and which whisker are tested, how outputs are normalised, and the unit of the test (ensembles or per-field means).
- **Figure 7D:** the factors of the 2-way ANOVA (enrichment by ensemble size within each distance bin, or enrichment by distance bin).

**Inconsistencies in the paper:**
- The Scnn1a-Cre barrel-radius test prints p = 0.01, but the text and legend say there is no significant effect. I recorded it as printed and judge the claim on the legend's reading.
- The neuropil paragraph cites "Figure 5" for the point representation; I read it as Figure 2.

**Missing from the paper:** nothing that stops claims from being written. The eBW method is the one detail a whole group of claims (Figures 3A, 3C and the Figure 3 supplement) depends on, and it is handled through readings E1 to E3. Whether the dataset holds the juxtacellular recordings (Figure 1F) and the barrel radii is for the author to find.
