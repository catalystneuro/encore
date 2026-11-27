I wrote `claims/sennesh-2025.yaml` and the quote checker passes: 37 claims, 37 quotes, 0 problems. Nothing is committed.

**Text read.** The bioRxiv preprint full text (`paper/10.1101-2025.07.31.667946.txt`, labelled "preprint" with no version number). It has the main text, the legends of Figures 1–5, the Methods, and the legends of Supplementary Figures 1–4, so the text the results rest on is all there. There was no PDF, so no figure was seen; numbers shown only in figures could not be read. I fetched only the dataset's title and description from DANDI.

**Code read.** BastosLab/epych, `notebooks/passiveglo` and the package, at commit cee2e6f (2025-07-29). That is the last commit before the preprint was posted on 2025-07-31. Later commits change the analysis, for example adding a cluster-size rule in 2026, and are not used.

**Counts.**
- 37 claims, all quoted, all with a criterion.
- 21 claims have expected values.
- 10 claims carry 17 statistics entries: cluster permutation tests at α = 0.01, permutation t-tests, and two 99% confidence intervals.

**Details the paper leaves open, and the readings named:**
- **Frequency range for removing the aperiodic component from spectrograms:** (a) all frequencies the code uses, 5–150 Hz; (b) 5–90 Hz, following the Methods' 2–90 Hz.
- **ɣ band for the laminar panels and Figure 5:** (a) 30–90 Hz, from the text; (b) 30–50 Hz, from the code.
- **Figure 5 time average:** (a) over the whole window, with zeros outside significant clusters, as the code does; (b) over significant points only.
- **Bands for the CSD troughs:** (a) the Methods' 2–10, 10–30 and 30–90 Hz; (b) the code's 4–8, 12–24 and 30–50 Hz. How a CSD "pattern" is judged is not in the paper; I fixed a rule on which layer's sink comes first, and the sink sign is not stated.
- **Window for the per-mouse spectra:** ±50 ms around the stimulus in the text, ±20 ms in the code.
- **Samples for Supplementary Figure 3:** (a) per mouse, as the legend says; (b) per channel of the pooled spectrogram, as the code does.
- **">2 SEM" in Supplementary Figure 2:** (a) at the band peak; (b) on each mouse's maximum.
- **ɣ power test for deviance detection** (only V1 and LM significant): (a) any 30–90 Hz bin passes; (b) each mouse's maximum.
- **Pupil (Supplementary Figure 4):** no test is named and the code has none. I used the paper-wide cluster test at 0.01; the z-scoring is open (pooled or per mouse).
- **Which two of the 16 mice were excluded:** the paper gives only the reasons. The code's rule is used: fewer than six probe files, or bad timestamps.
- **Where the text and legends disagree,** both are recorded: the Figure 3d and 3e layers and timing, the Figure 3i and 4i CSD descriptions, the Figure 2c and 4c effect sizes, and the area lists for Supplementary Figure 3.

**Missing from the paper:**
- The figures themselves, because there was no PDF.
- Any test for the pupil result.
- The source of the condition labels. The code reads them from a per-mouse `passiveglo_task_data.mat` file that the paper does not mention. Whether the dataset's own stimulus tables give the same conditions is for the author to find.
