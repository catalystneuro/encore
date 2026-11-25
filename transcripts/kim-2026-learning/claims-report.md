I wrote `claims/kim-2026-learning.yaml` with 39 claims. The quote checker passes every quote but exits with one problem. It cannot find the p-value 0.0002 (Fig. 4I, pyramidal cells at 6 µA) in the text, because the paper prints it as "p = 2.0e-4", a form the checker does not match. I checked it by reading, and the value is correct; I left the checker alone.

**Text read:** the bioRxiv preprint, version 1 (doi:10.64898/2026.06.05.730421), with its main text, figure legends for Figs. 1 to 7, Discussion and Methods. There was no PDF. The code's README says the paper was accepted at Science Advances; I did not read that version.

**Code read:** github.com/XieLuanLab/icms-activation-plasticity at commit d1922d1.

**Counts:**
- 39 claims, all with quotes and none inferred.
- 69 statistics entries.
- 39 criteria.
- Expected values in 11 claims. The tolerance is 10% except in three places, each with its reason: conduction velocity uses the reported range widened by 10% of each bound, the "over 80%" claim is judged against 0.8 itself, and the Fig. 6D onsets get one 10 ms bin.

**Missing from the paper:**
- **Supplementary figures S1 to S9 and their legends** were not supplied. Eight claims rest on them (S1E, S2A–C/E–F, S3B–D, S4B–E, S5, S6, S7, S8, S9). Each uses the Results sentence that cites the panel, with its method taken from the Methods and the code. No main finding needs the supplement.
- **Pieces missing from the code repository:**
  - `timing_params.json`.
  - The code that builds the per-trial Δspikes table and the hit/miss PSTH arrays for Fig. 6. Because of this, the Fig. 6D bin width is unknown.
  - The definitions of spike latency and jitter used in fig. S4.
- **Outside data:** the paper's Zenodo deposit is 10.5281/zenodo.17727762, but the README gives 10.5281/zenodo.21382755. No claim needs either.

**Details the paper leaves open, and the readings named:**
- **Week count:** I followed the code, ceil(days/7) from each mouse's first session; floor(days/7) is a variant.
- **Fig. 2A thresholds:** the catch-trial false-positive rate is either (a) a fixed guess rate in the fit or (b) used to correct the hit proportions before fitting.
- **Fig. S1E response times:** per-trial times pooled, or one median per channel and session.
- **Fig. 2B:** the paper does not name the mouse or the channel.
- **Fig. 2C:** one value per channel-week median (code) or per channel and session (legend).
- **Fig. 2E density and radius:** the code as written (it leaves out one mouse), the same measure over all 6 mice, or the mean of the 0–100 and 100–200 µm shell densities.
- **Fig. 2D:** "peak around 200 µm" read as the 100–200 or 200–300 µm shell.
- **Fig. 3D–F unit selection:** the code's session count, or tracked in all or all but one session.
- **Fig. 3I cutoff:** three readings (the code's weeks 0–1 against 3–4, week 0 against week 4 with the week-4 cutoff, or a pooled cutoff).
- **Fig. 3J subgroup:** set by each unit's last valid session (code) or by week 4.
- **Fig. 3N p-values:** pairwise post hoc or omnibus Kruskal-Wallis.
- **Fig. 3N week-0 group:** the subgroup at week 0 (n = 23, as in the code) or all tracked neurons at week 0 (as in the text).
- **Fig. 4G group-level test:** pooled over all mice or run per mouse.
- **Fig. S4 latency and jitter:** two definitions.
- **Fig. S6 recruitment:** a count or a fraction of tracked neurons.
- **Fig. 6C KL divergence:** the two parameter sets in the code's two scripts (1% and 0.4, or 2.5% and 0.8).
- **Fig. 6D:** 5 ms or 10 ms bins. The onset is read as the first significant cluster; the code marks the last one, kept as a variant.
- **Pulse-locking null distribution:** the code's uniform redistribution of spike times, with a shuffle of spike times as a variant.
- **Deconvolution:** OASIS defaults, named as a standard choice.

**Where the Methods or legends and the code disagree (Methods followed, code kept as a variant):**
- The volumetric activation threshold (Methods: a fixed 2× baseline STD; code: a multiplier set per channel).
- The planar ">5 frames" rule, which the code applies to every suprathreshold run.
- The Fig. 3D–F test (paper: signed-rank; the code's stats script: rank-sum).
- The sidedness of the tests in Fig. 4D and Fig. 4I–J.
- The paper says the week-4 spike onset was shorter at p = 0.479, which is not significant, so that claim judges only its direction.

I did not commit anything; only the claims file was written.
