I wrote `claims/clark-2026.yaml`, and the quote checker passes it with 0 problems. Nothing was committed.

**Text read.** The version of record (a PDF supplied by a person, extracted to text): main text, figure legends, Methods, Data and Code availability, the Reporting Summary, and the full Supplementary Information (Notes 1 to 4, Supp. Figs. 1 to 16). Nothing a claim needed was missing, and I opened no figure pages.

**Code read.** `github.com/davidclark1/symmetries-continuous-attractors` at commit `245726fa78457e10cdcf17e6be36fba1dec98061`. It settled most of the method details the Methods leave open, and the opening comment lists them. Two discrepancies:
- **Cell selection.** The paper calls the 1,533 cells "excitatory", but the code selects on `is_head_direction` alone.
- **Zenodo record for the cached results.** The paper cites 21827768 and the code's README gives 21827767.

**Claims.** 29 in all: 27 findings and 2 link checks.
- All 29 have quotes and a criterion; none needed an `inferred` note.
- One has statistics: the Kuiper test with Benjamini–Hochberg correction (lowest corrected P = 0.59).
- Four have expected values: cell counts, Fig. 5d peak numbers, Kuiper counts and P range, and the fitted (σ, β, b).
- Data: 21 use the dataset alone. One link check also needs the paper's cached tuning curves on Zenodo. Seven are theory or simulation claims (Figs. 6, 7a/d–f and 8, Supp. Figs. 1, 2 and 10–12) marked `elsewhere`, with the code repository as their source.

**Open details and the readings named:**
- **Cell selection:** (a) `is_head_direction` alone, as the code does; (b) also `is_excitatory`.
- **Fig. 1f,g "comparable in magnitude":** (a) the SD peak is between half and twice the mean peak; (b) the SD exceeds half the mean at offset 0. The thresholds I fixed for "unimodal", "symmetric" and "consistent across mice" are also flagged as open.
- **Fig. 3c "approaches circulant":** relative distance from the diagonal-averaged circulant matrix, falling as the subset grows. Supp. Fig. 13 adds an 80% single-frequency power test on the eigenvectors.
- **Fig. 5a,b "match":** (a) the model profile lies within the range of the 31 mouse profiles; (b) its peak is within 10% of the mouse average.
- **Fig. 5c agreement:** (a) total variation distance; (b) Hellinger distance.
- **Fig. 5d, 5f:** median within 10%, or Kolmogorov–Smirnov distance below 0.15.
- **Fig. 5e, where the tail begins:** correlation below (a) 0.5 or (b) 0.
- **Fig. 2f "within ~1 s":** (a) distance at 1 s at most a tenth of the starting distance; (b) at most twice its value at 20 s. **"Persist over 30 s":** (c) angle drift under 2π/20 for 90% of trajectories; (d) at least 50 distinct final bins.
- **Fig. 2i "a few discrete states":** at most 10 states after merging within 2π/50, against at least 50 for the optimal weights.
- **Tracking (Figs. 2j,k, 2l, 7c):** (a) median circular error below π/8; (b) circular correlation of at least 0.9.
- **Also flagged as open:** the thresholds for Supp. Fig. 14 ("approximately real", "doublets"), the collapse and spurious-state thresholds in Supp. Figs. 8, 11 and 12, and the ring-versus-structureless test in Fig. 6f,g.
- **Fit tolerance on β:** set to one grid step (0.345), not the default 10% (0.277), because the paper's grid search can only land on grid points.

**Missing from the paper.** Nothing a claim needed. The paper simply reports no quantitative measure of agreement for most of its qualitative findings, which is why the readings above are named as open.
