**Verifier report, round 1: Calvigioni et al. 2023 on DANDI:000473 (0.230417.1502)**

The claims file holds 33 claims. The notebook tests 18 and treats 15 as blocked. I had no attempt record, so these counts come from the claims file and the notebook's cells.

**A. Outcomes**

| Claim | My outcome | Reason |
|---|---|---|
| code-outputs-link | partially_reproduced | All 25 sessions match the session table (cell 8). Unit indices are identical in only 18 of 25 sessions, below the criterion's 22. Per-genotype fitted counts are 492/482, 743/738, 445/406 and 318/311, all within 10% (cell 9, blocks 1–4 period). |
| ed7a-unit-counts | reproduced | 4,159 units in total; Ctl 1,149, Vglut2 1,415, Npy 984, Esr1 611. All are within tolerance (cell 12). |
| fig4g-glm-units | reproduced | Reading (a) gives 1,995 / 492 / 743 / 443 / 317, all within 10% (cell 16). Npy, at 443 against a limit of 446.6, is near the edge. |
| fig4e-opto-modulation-genotypes | partially_reproduced | Vglut2 and Esr1 opto fractions exceed Ctl (Fisher p 7e-52 and 1e-17). Sound 1 and air puff exceed chance in all four genotypes. But the Npy opto fraction is also higher than Ctl at p = 0.044 (0.144 against 0.100, cell 18), which breaks "Npy does not". In the whole-session variant Npy is not higher (it is lower, p = 8e-12), and with the code's own tuned flags p = 0.128 (cell 24). |
| ed7bd-latency-similar | reproduced | With the pre-event baseline, at both 3 s.d. and 2 s.d.: tone 4 of 4 subregions and air puff 3 of 4 within 20 ms (cell 31). |
| fig4g-opto-tuning-score | not_reproduced | Reading (a) means are all within tolerance and Vglut2 passes (corrected p 0.012). Esr1 fails under every reading: corrected p 0.11 / 0.30 / 0.40 / 0.30 (cell 21), and 0.159 on the code's own scores (cell 25). The criterion needs the tests to hold even for a partial outcome. |
| fig4g-tuned-unit-counts | partially_reproduced | 5 of 8 counts are within 10%, and Vglut2 and Esr1 have more opto-tuned units than Ctl and Npy (cell 23). The criterion needs 6 of 8; Vglut2 negative missed by one unit (75 against a lower bound of 75.6). See problem 3. |
| ed8h-waveform-classes | reproduced | FS 606 (564 ± 56.4) and RS 3,484 (3,418 ± 341.8). Both classes contain opto-tuned units in Vglut2 and Esr1 (cell 27). |
| ed8o-conditioned-units | reproduced | Under reading (a), Vglut2 0.146 and Esr1 0.136 against Ctl 0.018 with every other trial; 0.155 and 0.133 against 0.027 with the first 50 trials (cell 33). Reading (b) gives about 0 in every genotype. |
| ed8r-comodulated-units | reproduced | Vglut2: 53 observed against 25.65 expected by chance, p = 9e-7. Esr1: 21 against 10.94, p = 0.0038 (cell 29). The code's signed-maximum variant agrees. |
| ed9a-pca-divergent-block2 | reproduced | 20 of 20 draws for both Esr1 and Vglut2 (cell 37). See problem 6 about block 4. |
| fig4h-opto-clusters | partially_reproduced | Two opto clusters, each with 100% Vglut2 and Esr1 units (cell 39). But 1,995 units were kept against an expected 1,770 (or 1,788) ± 177, which is outside tolerance. The quality-control step dropped no units (problem 4). |
| ed9bg-state-clusters | reproduced | 13 clusters meet the rule with the Wilcoxon test, 9 with the rank-sum variant (cell 41). Counting only monotonic clusters with a significant pair still gives 9, at least the 5 required. |
| fig4i-activity-modes | reproduced | Conditions (i) and (ii) hold under all three unit readings and both window sets (cell 43). |
| fig4k-decoding-pl | reproduced | In PL, Esr1 (0.957) and Vglut2 (0.937) exceed Ctl (0.852) and Npy (0.851) by more than the larger s.d. under both readings (cell 46). |
| ed9no-decoding-other-regions | not_reproduced | 49 differences beyond the larger s.d. under reading (a) and 41 under (b) (cell 48). Esr1 beats the other genotypes in ACAd, ILA and ORBm by margins similar to PL. |
| fig4jl-pl-esr1 | reproduced (fragile) | For Esr1, PL ranks first on all three measures; for Vglut2, 4 of 4 subregions exceed the Ctl maximum (cell 50). The PL lead is 0.413 against 0.412 (ILA, 17 units) on measure 1 and 0.104 against 0.099 on measure 3, both within the noise (problem 7). |
| fig4f-pupil-persistent | blocked, data_missing | Confirmed on the archive: only one of 25 assets, Npy 128514, has behavior data (PupilTracking/eye_area). There is none for any Esr1, Vglut2 or Ctl mouse. |
| fig4f-pupil-ctl-unchanged | blocked, data_missing | Same as above; no Ctl session has pupil data. |
| ed7g-eye-closing-airpuff | blocked, data_missing | The only Blink and eye-area series is in 128514 (Npy). One mouse can be described but tests nothing in the criterion. |
| ed1j-optotagged-tonic | blocked, data_missing | The archive holds 25 `ecephys+ogen` mPFC sessions and no LHA optotagging session. The notebook never listed non-PFC unit locations to confirm this (section C). |
| fig2d-markers | blocked (data elsewhere) | The data are in BioStudies S-BSST1069, not the dandiset. I could not check the notebook's "metadata insufficient" statement. |
| fig1l, fig2fh, fig3f-esr1-rtpa, fig3f-telc, fig3i, fig3jkl, fig3mn, ed10, fig5f, fig5g, fig5kl | blocked, data_missing | Confirmed: the asset list and description cover only the Neuropixels recordings. None of these patch-clamp, anatomy or behavior data are in it. |

**B. Problems**

1. [affects a conclusion] Helper docstring and cells 13–14 (GLM period). The helper says the code fits the whole session (`GLM_restrict = 0`). The notebook instead fits up to 2 s before the first block-5 trial, on the evidence that this matches the code's tmu outputs (18 identical sessions against 4, cell 9). That evidence is reasonable. But the choice decides several outcomes: under the whole session, fig4g-glm-units fails, fig4g-tuned-unit-counts gets 0 of 8, and fig4e's Npy result flips direction. The documentation contradicts the analysis and should say which period was used and why.
2. [affects a conclusion] Cell 18, fig4e. A two-sided, unit-level Fisher test pools units across mice; one Npy mouse alone contributes 33 of 201 units. Npy's p = 0.044 decides the outcome. Without a per-mouse view or a correction for three comparisons, the result is fragile.
3. [affects a conclusion] `glm_tuning`, cells 14 and 23. Tuned flags come from one seed, and the cutoffs are extreme order statistics. MATLAB `prctile` at 0.01% on 1,000 shifts clamps to the minimum, and at 99.9% it falls between the 999th and 1,000th values. fig4g-tuned-unit-counts missed reproduced by one unit (Vglut2 negative, 75 against 75.6), so other seeds could change the outcome. The notebook should report the counts' spread over several seeds.
4. [affects a conclusion] `cluster_units`, cell 39. The quality-control filter (more than 200 bins above 0.5 Hz) is applied to trial-averaged rates in Hz. One spike in 50 trials in a 10 ms bin is already 2 Hz, so no unit fitted at 2 Hz or more can fail it, and 0 of 1,995 were dropped. The paper's drop to 1,770 is not reproduced, and the printout does not mark the count as out of tolerance.
5. [does not affect a conclusion] Cell 13 says spikes near LFP saturation were removed, but `clean_spikes` uses the 'spike saturation' series by default. The helper calls the LFP series an assumption and says "see notebook", but the notebook gives no rationale. The LFP variant would remove 2.58% of spikes, including 1,171 s spanning block 3 of 147463 (cell 5). It is never run downstream.
6. [does not affect a conclusion] Claims file, ed9a. The statement says trajectories are "similar ... in block 4", but the criterion does not test this. In cell 37, block-4 distances to Ctl are 8.6 (Vglut2), 8.4 (Npy) and 5.8 (Esr1), against 0.6 to 1.5 in blocks 1 and 3. The data contradict that part of the statement. I am reporting this gap in the claims file, not correcting it.
7. [does not affect a conclusion under the rule] fig4jl, cell 50. The criterion's ranking rule passes on ties: 0.413 against 0.412 on measure 1 (Esr1 ILA has only 17 fitted units), and 0.104 against 0.099 on measure 3, where the s.d. is about 0.02. Measure 2 is not referenced to Ctl, whose PL shift of −6.47 is similar to Esr1's −9.01. Cell 48's result also contradicts the PL specificity. The "reproduced" outcome is weak evidence.
8. [does not affect a conclusion] fig4e chance level. The notebook uses the stated 0.11%. With 1,000 shifts and MATLAB `prctile`, the real false-positive rate is about 0.1% for the negative tail plus about 0.05–0.1% for the positive tail. Observed fractions are about 40%, so this does not matter. Separately, the second reading (cell 19) gives significant Wilcoxon p for Ctl and Npy too, with negative medians, so p alone does not separate the genotypes.
9. [does not affect a conclusion] fig4g-opto-tuning-score. The paper's n = 10 Esr1 mice cannot hold for the GLM data: 3 Esr1 sessions have no PFC units in either the dandiset or the code's outputs, so n is 7. The paper may have computed its p differently. This is a paper inconsistency, not a notebook error.
10. [does not affect a conclusion] Decoding (cells 45–46) follows the code. Z-scoring happens before the split, and 100 ms bins from the same trial land in both training and test folds, so accuracy is inflated by temporal autocorrelation and by slow drift across blocks. This applies to every genotype, and the analysis matches the paper's method.
11. [does not affect a conclusion] Cell 39. The "gausswin5" variant is the same as a Gaussian with sigma 0.8 bins (gausswin(5) with alpha 2.5 has sigma 4/5), so it is not a real variant. Its cluster tables are identical.
12. [does not affect a conclusion] Selection never checks a 'good' curation label, and the notebook does not show whether the units table holds only good units. The counts match, so this is probably moot.

I checked the helper on synthetic data. The closed-form Poisson betas equal the statsmodels GLM fit exactly, and the FFT shifted scores match a brute-force circular shift to within 2e-16. `matlab_prctile` and `train_onsets` behave as documented.

**C. What I could not check, and the output that would settle it**

- **Seed sensitivity of tuned flags and counts** (fig4g-tuned-unit-counts, fig4e): the tuned counts and the Npy Fisher p over 10 or more seeds.
- **Per-mouse view of fig4e**: per-mouse opto-tuned fractions with a mouse-level test, such as Mann-Whitney over mice.
- **LFP-saturation variant**: fitted counts and the main tuning results with `clean_spikes(series="LFP")`.
- **QC count in clustering** (fig4h): the distribution of active-bin counts, and the kept count with the threshold applied to per-trial or unsmoothed data.
- **ed1j blocked status**: the location labels of the 5,046 units outside the four regions, especially any LHA units in Vglut2 sessions.
- **fig2d blocked status**: I did not open BioStudies S-BSST1069. A listing of its files and type labels would confirm or refute "metadata insufficient".
- **Single-mouse eye data**: a descriptive block 1 against block 4 eye-closing count for 128514, to show what the one available series holds.
- **Paper numbers**: I did not re-read Supplementary Tables 6 to 9 against the claims file (the Esr1 n and p for Supplementary Table 6, the 1,770 count).
