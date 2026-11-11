I wrote `claims/sadeghi-2019.yaml` with 28 claims. The quote checker passes with 0 problems.

**Text read.** The version of record (PMC6788721, Europe PMC full-text XML): Results, Discussion, Methods and all figure legends (Figs 1 to 10 and S1 to S10). Also the supplement files S1 Text (the proofs on signal and noise correlations), S1 Table (the 195 model sounds) and S2 Table (the paradigm 3 sounds). No PDF was supplied.

**What was not read.**
- **Equations.** Every displayed equation was lost from the text, and there was no PDF to read them from. That covers the correlation normalizations, the noise correlation, the decision rule, the spectro-temporal mixing, the 1/f filter, and the SI and CDI formulas. Each criterion that needs one names readings taken from the surrounding prose.
- **Code.** The only code the paper links is the MATLAB code inside the CRCNS bst-2 deposit. Because it is part of the dataset's files, I did not read it. The opening comment says the author may follow it and keep my readings as variants.

**Counts.**
- 28 claims, all with quotes, none inferred.
- 9 claims carry statistics (t tests against chance, a one-tailed t test, three pairwise two-sample t tests, Bonferroni-corrected tests); the checker found 14 p-values in all.
- 28 criteria; 26 claims have expected values.
- Coverage: paradigm 1 (8 claims), paradigm 2 (4), paradigm 3 (3), and the auditory model (13).

**Details the paper leaves open, with the readings named:**
1. **How the 100 random time samples make a decision:** each sample is one decision, or the log-posterior is summed over all 100.
2. **How the number of principal components is chosen:** on the validation performance, or by an inner split of the model half.
3. **Paradigm 2 split:** the half split as in paradigm 1, or whole original responses train and whole 1/f responses test. Paradigm 3 has the same question (whole responses, or the half split on top of leaving one exemplar out).
4. **Neural spectrum (rate) classifier:** not described for the neural data. Read as the mean aMUA per channel through the same pipeline.
5. **Mixing coefficient:** fitted on model or validation data, on a 0.1 grid.
6. **Correlation window T for Figs 1, 2 and 4:** one window over the whole 3 s response, or 1000 ms windows averaged.
7. **Width measure:** taken on the channel-averaged curve, or as the median over channels.
8. **SNR formula:** not given. Readings: a power ratio with or without the diagonal, and one value per site and sound or per site.
9. **CDI and SI formulas:** normalized by the power of the average, or by the mean power. The grouping of categories for SI and its averaging unit are also open.
10. **Window for the model's time-averaged correlations in Figs 5 and 6:** the coarsest 566 ms window, or the whole sound.
11. **Model classifier:** the window spacing (τW or the full Kaiser length) and the resolution at which the number of components is fixed.
12. **Unit of the t tests:** per-sound outcomes or category accuracies; for the tests against chance, one-sided or two-sided.
13. **Time-averaged classifier (Fig 9C):** not described in the Methods. Two constructions are named, and the reduction is read in points or as relative.
14. **Two-category task:** one model per class, or the 13-category models mapped to a class.
15. **Rise time:** interpolation, first sampled duration, or an exponential fit.

**Gaps a claim needed.**
- **Fig 9A optimal window:** the legend says 144 ms and the text says 141 ms. I took 141, since the half-octave grid holds 141 ms.
- **S5 Fig:** needs each channel's best frequency from the tone-pip responses.
- **S10 Fig:** needs raw voltage to threshold the MUA.
- The dataset description lists neither tone-pip responses nor raw voltage, so these two claims are blocked if the data are absent.
- **White noise:** a control in Figs 6C and 7I, but not in the dataset's sound list. The criterion has it generated if needed.
