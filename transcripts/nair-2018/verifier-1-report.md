**A. Outcomes** (28 claims in the claims file: the notebook tests 10 and treats 18 as blocked. No attempt record was among my materials, so counts come from the claims file and the notebook's claim table.)

| Claim | Outcome | Reason |
|---|---|---|
| fig3a-bf-gamma-reduction | partially_reproduced | Paired t over rats p = 0.012 with home cage higher in 6/6 rats (cell 15). The reduction is 47–48% under both readings and every epoch/artifact/unit variant, outside 35 ± 3%. Removing 49–51 Hz still gives 44.7% (cell 16). |
| fig3a-each-hemisphere-significant | reproduced | 13/13 arena-vs-home comparisons give p < 0.01 with home higher, under 2-s, 2-s peak-to-peak and 10-s epochs. The largest p is 1e-7 (cell 19). |
| fig3b-arena-gamma-unrelated-to-movement | reproduced | One-way ANOVA on per-rat quartile means gives p = 1.0 / 0.998. The informative tests also give p > 0.1: repeated measures 0.38 / 0.28, epoch-level 0.60 / 0.19, and the variant with movement shifted one segment (cell 21, 24). Q4/Q1 is 0.95–1.04. |
| fig3b-home-cage-gamma-increases-with-movement | not_reproduced | The criterion's test (one-way ANOVA on per-rat quartile means) gives p = 0.82 / 0.77 (cell 23). The effect itself is in the data: Q4 > Q1 in 6/6 rats, Q4/Q1 = 1.43, repeated-measures p = 2e-5, epoch-level one-way p = 4e-46. See problem 1. |
| fig3b-matched-movement | not_reproduced | Readings (a) and (b) select the same pair (home Q4 vs arena Q3). One-way ANOVA p = 0.070, above the criterion's 0.05 (cell 27). Home is higher in 6/6 rats and the paired-t variant gives p = 0.007. |
| fig3c-home-cage-above-both-sessions | partially_reproduced (session-order part should be blocked: metadata_insufficient) | Home cage exceeds both arena files with Bonferroni-corrected paired t p = 0.038 / 0.035, but Tukey gives p = 0.30 / 0.19 (cell 29). Arena 2 is 15.9% *below* arena 1 (p = 0.02), but the data descriptor calls sessions 1 and 2 "two separate examples", so nothing shows they are the first and second daily sessions (problem 2). |
| fig3d-gamma-rises-with-time-in-arena | partially_reproduced | The correlation is positive and significant. Reading (a) on 1-min bins, first 10 min: r = 0.859, p = 0.0015. Reading (b) on whole files: mean r = 0.165, p = 0.011. No reading falls in 0.648–0.792 (cell 31); the criterion defines no partial outcome, and I use the file's general pattern of "test holds, size off". |
| figs2-bf-low-frequency-bands | reproduced | Delta, beta and gamma are higher in the home cage and theta lower, all at p < 0.05, under all 12 epoch/artifact/unit readings (cell 34). |
| figs3-unimodal-states | reproduced | All dip tests give p > 0.1. Smallest p is 0.554 with sessions pooled and 0.102 per session (cell 36). |
| figs5-arena-excursions | partially_reproduced | The gamma rise is significant in 12/12 readings and theta p > 0.1 in 10/12. Count is 10.3–14.3 per 20 min against 8 ± 0.8, mean duration is 5.1–5.7 s against 16 ± 8 s, and the shortest excursion is 2 s against the paper's 8 s (cell 38). No scale puts the threshold near 2.6, so 0.56 and −0.01 are correctly not judged. |
| bipolar-gamma-reduction | blocked: metadata_insufficient | Archive check: the files are named by rat/type/session only, and the descriptor says nothing about electrode type. Nothing testable. |
| fig3c-consistent-over-days | blocked: metadata_insufficient | There are no day labels, and the descriptor calls the sessions "examples". Nothing testable. |
| fig3d-rapid-switch-to-home-cage | blocked: data_missing | Each file's clock starts at 0 (cell 3), and no file spans the transfer. Reading (b) would need the home-cage t = 0 to be the transfer time, which nothing documents. |
| behavior-arena-time-budget, behavior-home-cage-less-exploration, behavior-movement-speed, fig3f-grooming-quiet-arena, figs6-object-more-stationary | blocked: data_missing | The archive (filelist.txt and the S3 listing: one tar.gz plus docs) has no video or behavior labels. `mov_data` is a dimensionless acceleration value, not cm/s or a behavior label. |
| fig4-object-exploration-suppressed | blocked: data_missing | Only `Arena` and `HCage` files exist (cell 3). |
| fig5a-phase-locked-neurons, fig5cd-pli-max-at-gamma, spike-width-phase-locked | blocked: data_missing | The data are 400 Hz LFP only, with no spikes. |
| fig6a-acc-gamma-home-cage, fig6a-vc-gamma-unchanged, fig6b-coherence, fig6c-granger-bf-to-acc, fig6d-trivariate-granger, figs2-acc-vc-low-frequency-bands | blocked: data_missing | Each file holds one BF LFP channel (`LFP_data` is 800 × segments). |

No claim involves a chance level.

**B. Problems**

1. [affects a conclusion] Cells 21, 23 and 27: the criterion's one-way ANOVA on per-rat means, applied without per-rat normalization, puts between-rat variance into the error term. Rat 5's gamma is about 3–4× the others' (cell 23: 36 to 145). With n = 6 this test cannot detect a within-rat effect: the home-cage η² is only 0.045 although 6/6 rats rise.
   - fig3b-home-cage fails and fig3b-matched fails at p = 0.07, while the repeated-measures, epoch-level and paired variants all hold.
   - The arena "absence" passes trivially (p ≈ 1), though the informative variants agree there.
   - The notebook follows the claims file faithfully, so this is a claims-file test choice, not a notebook error. It should be revisited.
2. [affects a conclusion] Cell 29 / fig3c: the notebook treats data-set sessions 1 and 2 as the first and second daily arena sessions without checking. The descriptor says "two separate examples (Session 1 and 2)". Rat 3's HCage session 2 being a 100-s-shifted excerpt of session 1 (cell 5) also suggests the files are chosen excerpts. So the reversed −15.9% result is not evidence against the paper's +5.62%.
3. [affects a conclusion] Cell 31 / fig3d: "time in the arena" assumes each arena file's t = 0 is arena entry. Files span 620–780 s, longer than the 10-min session, and this was never checked. The "first 10 min" window rests on the same assumption, and r swings from 0.29 to 0.86 between windows.
4. [does not affect a conclusion] Cell 29: `pairwise_tukeyhsd` treats the 18 rat-level values as independent groups and ignores pairing within rat. The claims file names Tukey; the Bonferroni-paired variant was also run.
5. [does not affect a conclusion] `bflfp.boxcar`: `np.convolve(mode="same")` zero-pads, so the first and last smoothed values are 2/3 of the local mean (synthetic test: [3,3,3,3,3] becomes [2,3,3,3,2]). This suppresses excursions at file edges and changes counts by at most a few.
6. [does not affect a conclusion] `bflfp.histogram_intersection`: on a synthetic Gaussian pair with unequal variance and modest n, it returned 0.48 against a true crossing of 0.90 (it takes the first noisy bin crossing). On realistic lognormal inputs it is unbiased (35.9 vs 35.4, SD 0.7). The KDE variant gives nearly the same counts in cell 38.
7. [does not affect a conclusion] Cell 36: dip tests were run on raw power only. Dip p-values are not invariant to a log transform. All p ≥ 0.10, so this is unlikely to change the result, but it is unchecked.
8. [does not affect a conclusion] Cell 4 text: "Arena files span 8.8 to 13 min" does not match the printed spans of 526–780 s, which is 8.8 to 13.0 min. That checks out. The removed share of 2.6–23.5% vs the SI's 1–4% is reported but its consequence is not explored; the peak-to-peak re-run covers it.
9. [does not affect a conclusion] The other helpers check out on synthetic inputs: `band_powers` and `spectrum` (a unit sine gives total power 0.5), `ten_second_epochs` (handles gaps correctly) and `excursions` (correct run, peak and before-window logic).

**C. What I could not check**

- Whether session numbers or file start times relate to day order or arena entry. Printing each arena file's movement values for the first and last minute (looking for a handling or transfer signature) would help with problem 3. Nothing in the archive can settle session order.
- Whether the excursion shortfall (2-s minimum vs the paper's 8 s) comes from an unstated minimum-duration or merging rule. A scale-free comparison would help: rise/threshold is 0.56/2.6 ≈ 0.22 in the paper, against about 0.41 for the notebook's normalized reading. Neither the criterion nor the notebook reports it.
- Fig. 3D's n = 22 versus the notebook's 12 recordings and 10 bins. An output of r against bin width (for example 20 s to 2 min) would show how fragile reading (a) is. It would be shown, not judged.
- The notebook's own conclusion cells, which were removed. I did not re-run any computation on the data.
