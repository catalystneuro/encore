I've written `claims/001710/10.1101-2023.11.20.567978.yaml` with 55 claims. The quote checker finds every quote word for word. It still exits non-zero, flagging four p-values it can't match: 5.00e-6 (Fig 2D), 2.60e-5 (Fig 4E) and 2.40e-7 (Fig 5D, used by two claims). The paper prints them with trailing zeros, a form the checker doesn't try. I read each one in its legend and they are correct, so I left both the quotes and the checker as they are.

**Text read.** The bioRxiv preprint, version 1 (posted November 21, 2023). It includes the main text, the legends for Figures 1 to 7 and Supplementary Figures S1 to S9 (the supplement is inline), the Discussion and the Methods. No PDF was available. Movie S1 was not read, and no claim depends on it. The dataset's name on the archive says 2026, so a later published version may exist; I did not read one. The paper links no code and has no data or code availability statement.

**Counts.**
- **Claims:** 55, all with quotes and all with a criterion.
- **Statistics:** 48 claims record the paper's tests.
- **Expected values:** one claim (the example-session cell and trial counts in Fig 2A-B).
- **Claims of absence:** 17, each judged on the paper's own test.
- **Freely moving behavior:** 5 claims (T-maze, open field, elevated plus maze). These may not be in the dataset.

**Details the paper leaves open, with the readings named:**
- **Cre mice in the VR behavior claims:** Cre-1 to Cre-7, or Cre-1 to Cre-8. The legends give 7 or 8 mice, and F(1,15) fits 17 mice.
- **Unpaired t-tests:** Student's or Welch's. pingouin's default switches to Welch when the groups differ in size, as 9 and 7 do.
- **Anticipatory lick rate:** licks over time spent in the 30 cm, or the mean of the three 10 cm bins.
- **Novelty slowing (Fig S2F-G):** the first two trials of block 6 (legend) or the whole block (Methods).
- **Population vector correlation:**
  - Computed over the flattened cells-by-bins matrix, or per bin and then averaged.
  - Using all cells or only place cells.
  - For across-day decoding, the diagonal of the error matrix is included or left out.
- **Place field width and fields per cell:** all candidate fields, or only those with a formation lap. The cells counted are those with at least one field, or place cells.
- **Block 6 activity:** the Methods take the log of the population mean; the Fig 4A legend takes the log per cell. The legend's version is undefined for bins with zero activity, so it is shown as a variant and does not decide.
- **Where the stem ends:** at 150 cm or at 100 cm.
- **Fig S6E levels:** 3 levels of trials since a novel trial, or "3 or more"; days 1 to 5 or 1 to 6.
- **Reward cells:**
  - The peak window is the 50 cm before the reward zone, or 50 cm on either side of its front.
  - The denominator is all cells, or cells significant on both trial types.
  - Chance is computed by permutation or analytically.
- **Extinction model (Fig 5H-I):** trial numbering continues across days 7 and 8, or covers day 7 only. Random effects are an intercept per mouse, or intercept and slope.
- **Population vector shift:** all cells or place cells. The centre of mass uses the raw cross-correlation, or with negative values set to zero.
- **Single-field shift (Fig 6D):** "trial 1" is the formation lap or the lap after it.
- **HSE stability (Fig 7):** across-day correlation over all pairs of days or consecutive days. "Reactivated" means in an HSE on any day, or on that same day.

**Missing from the text.**
- The text extraction dropped the Methods equations: the spatial information formula, the decoder likelihood, the model's input tuning function and its weight update. The criteria use the standard Skaggs and Poisson forms.
- The model claims (Fig 3B-E) lack the number of trials, the weight update equation and any definition of a model place field or of stability. They are recorded as not specified.
- The morph task (Fig S4) shows example matrices only, and its methods are only cited to an earlier paper. It is also recorded as not specified.
- The CA3 and dentate gyrus claim (Fig S5) has no count or test. Its criterion uses the 5% chance rate implied by the paper's 95% shuffle threshold.

**Inconsistencies in the paper,** noted in the file's header:
- Several printed statistics don't match their p-values: Fig 1F (F=10.66 with p=5.22e-4, where that F gives about 0.005), Fig S3A, Fig 6D and Fig 7H.
- Fig 2C-D give 8 Cre mice but degrees of freedom that fit 7.
- The degrees of freedom in Fig S6E don't match its stated conditions and days.
- The Discussion says Cre mice have more reward cells than chance, but the Fig 5D legend gives p=.080.
