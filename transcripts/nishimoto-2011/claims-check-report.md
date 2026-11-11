The checker's result line is `claims/nishimoto-2011.yaml: 20 claims, 20 quotes, 11 statistical values, 0 problems`. It said the same before and after my edits.

I checked every claim against the text and against Figures 2B, 3, 6 and 7, which I rendered from the PDF. All the expected values match the paper, including the values read off the Figure 2B bars (16, 19, −36, −24 and 8%). All p-values and their signs are results, not thresholds, and the paper's main findings each have a claim.

**Changes, by claim**
- **fig3b-mean-prediction:** The display range is now 0.2 to 0.8, which is the span of the Figure 3B histogram. It said 0.2 to 0.9.
- **fig2b-contrast-normalization-no-effect:** The Bonferroni correction is now fixed at 11 comparisons. The Figure 2B legend marks each of the 11 models against the simplest one, and a claim of absence must be judged on a single test. A correction over 5 is kept as a variant.
- **fig2b-compressive-divisive-best:** The condition "no model of the 12 is significantly better" is now labelled as this file's own reading of "simplest model that gives accurate predictions", and its test is named. The paper reports no such test.
- **fig6a-excitatory-on-plane:** The sign of the symmetry term is now named as open. The Methods say only "subtracting these quantities and taking the negative", so the file takes the absolute difference as its reading.
- **fig6b-suppressive-off-plane:** The null comparison is now the null model's suppressive ratios. The dashed null line in Figure 6B sits at about 0.27, not at the excitatory null mean of 0.36. The excitatory null is kept as a variant.
- **fig7a-partial-ring:** The ring end of the distribution is now open-ended (at or above 0.8 or 0.9). Figure 7A ratios run to about 1.7, and the Figure 4A ring neuron sits near 1.35, so the old 0.8 to 1.2 band left some neurons unclassed. The one-quarter bound is now labelled as this file's reading of "only a small fraction".

**What remains open** (logged in `checks`)
- **fig7b-pattern-index:** The minus sign before 6 is garbled in the text extraction, so the quote shows "..." there. The PDF reads −6.
- **Figure 2B values:** They are read from bars with a tolerance of 4 points. My second reading from the PDF gave the same values.
- **Data coverage:** mt-2 holds 45 of the paper's 52 neurons. It may also lack the single validation repeats needed for fig3b-explainable-variance, and the 15 natural-movie validation sets needed for natural-movie-control. That is for the author to find.

The file is ready for an attempt. The new check entry has `ready: true`. Nothing was committed. `git status` also shows untracked files I did not create (dotfiles, `.idea`, `.vscode`, `scripts`); I left them alone.
