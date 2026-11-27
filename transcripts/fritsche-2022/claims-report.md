I wrote `claims/fritsche-2022.yaml`. The quote checker finds no problems (29 claims, 29 quotes, 80 statistical values), and no value contains ": ", an em dash or "rather". Nothing is committed.

**Text read.** The version of record (J Neurosci 2022, PMC8916757), all of it: Methods, Results, Discussion, the legends of Figs. 1 to 8, and Tables 1 and 2. The paper has no supplement. The text file had lost the display equations, and there is no PDF, so I read the five formulas from the MathML on the same PMC page: the adaptation ratio, the single and double exponential, the orientation selectivity index (OSI), and the cumulative product. I opened no figures.

**Code not read.** The paper's code is at doi:10.34973/kpt9-y956. Its file list is public, but every script returned HTTP 401 because it sits behind a data use agreement. No criterion rests on the code.

**Claims.** 29 claims, all with quotes (none inferred), 19 with statistics, 15 with expected values, and all 29 with a criterion. They cover:
- unit counts;
- 1-back adaptation in V1, the extrastriate areas and the thalamus, for drifting and for static gratings;
- consistency across mice (Figs. 1E, 3C, 6D);
- the Fig. 2 tuning ANOVA (main effect, interaction, adaptation at each orientation, and its absence in the thalamus);
- long-term adaptation in V1 (8-back for drifting, 20-back for static);
- the exponential fits and F tests from Tables 1 and 2, and the ~14 s half-life;
- cumulative adaptation and its linearity (Fig. 4);
- the V1 against thalamus Welch tests;
- the blank-baseline analysis (Fig. 5);
- the simulation with no spurious long-term effect (Fig. 8);
- the robustness variants.

All use `data: dataset`.

**Details the paper leaves open, with the readings named:**
- **O1, ratio per unit:** pool all current orientations, or compute the ratio per orientation and average.
- **O2, region value:** the exponent of the mean log ratio, or the mean of the ratios.
- **O3, n-back position:** blanks keep a place in the sequence or are removed; pairs are formed within each block or across the whole sequence.
- **O4, visual responsiveness:** "above 1 SD" means above the gray mean plus 1 SD, or above the SD itself; the gray reference is the blank trials or the spontaneous gray-screen epoch.
- **O5, exponential fit:**
  - the data fitted are the mean log ratio at each n, or every unit's log ratio;
  - the second term of the double exponential is printed with a plus sign: read as both terms reducing the response (which Tables 1 and 2 support) or as printed.
- **O6, correction:** where the paper names no method, the Benjamini-Hochberg FDR it uses elsewhere, with Bonferroni as a variant.
- **Per-claim gaps:**
  - what "consistent across mice" means: every mouse, or a sign test;
  - for the Fig. 2 ANOVA: log ratios or ratios, and how the ±45° tests are combined;
  - the normalization in the Welch tests and which n are tested (2 to 10, or 2 to 50);
  - which adjacent pairs Fig. 4B shows and what the baseline is;
  - the test behind significance in Fig. 5 (bootstrap CI, or t tests with FDR);
  - the FDR family for static gratings (1 to 20, or 1 to 50);
  - the noise in the Fig. 8 simulation (Poisson, or none);
  - the trial-to-seconds conversion behind the half-life (3 s per trial times ln 2).

**Missing from the paper that a claim needed:**
- **Region counts:** the per-region unit counts for LM, AL, RL, PM and AM are only in a figure, so they could not be used.
- **Thalamic CIs:** for static gratings, the LGN and LP ratios sit on the lower bound of their printed CIs (0.93 [0.93, 0.98] and 0.85 [0.85, 0.96]). The criterion therefore widens each CI down to the printed value minus 10%.
- **Code:** the analysis code needs a login, so no criterion could be checked against it.
