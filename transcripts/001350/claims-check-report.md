I checked the file and made five changes; it is ready for an attempt. I changed only `claims/001350/10.1073-pnas.2307250121.yaml` and did not commit.

**Checker result:** `30 claims, 30 quotes, 18 statistical values, 14 problems`. All 14 problems are "VALUE NOT FOUND" lines for p-values that are printed only on figure panels, not in the text. Every quote matched word for word.

**Values from the supplement figures:** the image viewer couldn't open the PDF, so I installed PyMuPDF into the temp directory and rendered the Fig. S2 and S3 pages. Every p-value and bar height the file takes from Figs. S2B, S2C, S2E, S2F, S2I, S2J, S3C and S3D matches the panels. Figs. S2K and S2L show one asterisk, and Figs. S3F and S3G print no p-value, as the file says.

**Changes, by claim:**
- **fig2c-cc-percent-myelinated:** the statement names cKO first but gave the values in the other order ("37% against 22%"). I swapped them to 22% against 37%, matching the expected values.
- **fig2d-cc-myelinated-density:** the same ordering error. I changed 1.8 against 1.4 to 1.4 against 1.8.
- **fig5e-less-f-actin:** the paper's reported range (cKO at about 20% to 40% of Flox) was missing from the expected values. I added it with the protocol's tolerance for a range, which gives 0.18 to 0.44, written as 0.31 ± 0.13.
- **fig3d-shared-carg-targets:** `expected` was a single mapping. I made it a one-item list like every other claim.
- **New claim, figs4ef-assembly-not-disassembly-genes:** a Results finding with no claim, that SRF mainly regulates actin assembly genes and not disassembly genes such as Cfl1 (Fig. S4E and S4F). Its data are in GEO, so it can't be tested on this dataset.

**What remains open:**
- **Main Figures 2 and 5:** I could not check the values printed on these panels, because the main article's PDF is not under `paper/`. That covers the p-values and means for Fig. 2C to 2E, the p-values for Fig. 2G to 2K, the Fig. 5E p of 0.0546 and its asterisks. Only the g-ratios 0.760 and 0.703 appear in the text.
- **Asterisk in Fig. S2K and S2L:** the legend doesn't say what one asterisk means. The file reads it as p < 0.05, the usual meaning.
- **Unit in Fig. 2D:** the file reads it as axons per µm² because other units give implausible densities, not because the paper says so. The criterion already falls back on the cKO to Flox ratio, which has no unit.

I added the check entry under `checks` with `ready: true`, listing each change and each open problem.
