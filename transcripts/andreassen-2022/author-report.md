I've run steps 1 to 6 of the Author protocol on andreassen-2022. The record is `attempts/andreassen-2022-01.yaml` and the entry is `entries/andreassen-2022/`. `entry.py all` gave 0 errors and the notebook passed in 24 s. The executed copy gives the same numbers as my development run. The handover package is built; I did not verify my own work and committed nothing.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1c-ctmax-5dpf | reproduced (41.36 °C) |
| fig1c-ctmax-similar-across-ages | reproduced (holds only after the paper's outlier removal) |
| figs1a-swim-speed-no-treatment-difference | reproduced |
| figs1bc-spiral-swimming | blocked, data_missing |
| figs1d-loss-of-equilibrium | reproduced (W = 27, r = 0.577) |
| figs1e-loss-of-response-specific | blocked, data_missing |
| fig2f-medulla-control-stable | reproduced |
| fig2f-medulla-heat-rise-then-fall | reproduced under reading (a), group mean curve, 3.59; reading (b), per-fish maxima, gives 4.30 and fails |
| figs2a-medulla-decrease-39-41 | blocked, data_missing |
| fig2g-depolarization-onset-temperature | blocked, data_missing |
| fig2e-depolarization-spread | blocked, data_missing |
| fig2d-recovery-after-depolarization | blocked, data_missing |
| fig3d-ctmax-precedes-depolarization | reproduced |
| fig4c-heart-rate-rises-to-34 | reproduced |
| fig4c-heart-rate-falls-then-stable | reproduced (Q10 0.550, inside the tolerance by 0.01) |
| figs2b-medulla-lateral-mount | blocked, data_missing |
| fig5a-ctmax-oxygen | reproduced (holds only after outlier removal) |
| fig5b-depolarization-oxygen | reproduced |
| figs3b-amplitude-no-oxygen-effect | reproduced |
| figs3c-recovery-longer-in-hypoxia | reproduced |
| figs3d-medulla-drops-before-depolarization | reproduced, `assumed: true` |
| fig5d-medulla-normoxia | reproduced |
| fig5d-medulla-hyperoxia | reproduced |
| fig5d-medulla-hypoxia | partially reproduced (Q10 from 28 to 34 °C is 0.883, against 0.8 ± 0.08) |
| figs4ab-light-response-amplitude-falls | blocked, data_missing |
| fig6c-light-responsiveness-by-oxygen | partially reproduced (the hyperoxia level is kept to 29 °C by the criterion's rule, not 36 °C) |
| tables10-light-response-model | reproduced |
| discussion-depolarization-magnitude | blocked, data_missing |

Totals: 17 reproduced (one of them assumed), 2 partially reproduced, 9 blocked.

## 2. Dataset, assumptions, questions

**Version.** I pinned version 4, the latest. The paper cites the item without a version. Version 3 has the same files with the same MD5s, which the notebook shows.

**What the item holds.** Ten CSV tables of per-fish values, a Readme and the paper's R script. Every count matches the paper. Every refitted model gives the estimates of Tables S1 and S3 to S10.

**What it lacks.** The experiment-2 temperatures and onset temperatures, the experiment-4 medulla counts, the spiral-swimming and loss-of-response scores, the light-response amplitudes, the medulla peak amplitudes and any imaging. This is recorded as a major data_missing finding. The R script types the spiral-swimming counts into a matrix, so they are not deposited data.

**Minor findings:**
- LightResponse.csv calls three fish Fish3, Fish4 and Fish5, while the depolarization table has Fish03, Fish04 and Fish05. The Readme says the IDs correspond.
- Fish33 has medulla and light values but no depolarization row.
- The medulla series of Fish03 and Fish35 end one and two bins before the bin holding their onset.
- The light recordings of Fish27 and Fish29 end about 10 °C below their onsets.
- CTmaxData_Total.csv has 14 rows without a CTmax value (2 of them also have no treatment), and nothing explains them.

No recording appears to be deposited twice.

**Details settled by the R script:** the outlier rule is applied within treatment, the model formulas and reference levels, the temperature binning and labels, and the centering of temperature in the light model.

**Assumption (figs3d).** The experiment-5 medulla frequencies are in 1 °C bins, not in time. I converted bins to minutes with the stated 0.3 °C/min ramp. The onset frames give 0.225 °C/min across the fish of the second period, so I ran that rate as a variant; the outcome is the same. The question is recorded for the paper's authors as a methods_unavailable finding.

**Questions to a reader:** none. I found no place where the claims file misreads the paper.

## 3. Protocol gaps

1. **Clock check.** The protocol assumes time streams and trial tables; here there are only derived tables. As the nearest check, I tested whether each fish's last medulla bin falls in the bin holding its onset (30 of 32 do).
2. **p-value method.** The claims file names Satterthwaite as the main reading for the mixed models, but the paper's script uses Kenward-Roger (sjPlot `p.val = "kr"`). I used Satterthwaite as the criterion asks, printed the normal approximation as well, and recorded the difference as a deviation. Kenward-Roger itself is not implemented.
3. **No R in the locked environment.** I reimplemented the REML mixed model and the Laplace binomial mixed model in `thermal.py` and checked them against the paper's tables. The protocol says nothing about papers whose code is in R.
4. **Readings when the code settles one.** The claims file sometimes lists readings that the paper's code settles, such as outliers within treatment or over all fish (fig5a). I followed the code and showed the other reading. The protocol does not say whether a reading the code rules out still counts under "reproduced under any reading".
5. **Criterion thresholds the reader set.** The decline rule in fig6c and the half-maximum threshold in figs3d come from the reader, not the paper. The protocol only partly covers outcomes that rest on such thresholds; I treated them as part of the criterion and reported the sensitivity.
6. **Numbers written into the paper's own code.** The spiral-swimming counts exist only as a matrix in the R script. Testing them would not test the dataset, so I blocked the claim as data_missing. The protocol has no explicit rule for this.
7. **Untracked files.** Dotfiles (`.bashrc`, `.gitconfig` and others), `.idea`, `.vscode`, `.mcp.json` and `scripts/` are untracked at the repository root and are not mine; `scripts/` was already there when the run started. I left them alone, but the workflow should make sure they are not committed.

## 4. Runtime and failures

The run took about 25 minutes, from 08:17 to 08:41 UTC. The notebook runs in about 24 s. My failures were all fixed before the final run: two patsy formula errors, one pandas index error, and one check run from the wrong Python environment.
