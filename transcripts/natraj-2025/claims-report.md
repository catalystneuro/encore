I wrote the claims file at `claims/001535/10.1016-j.cell.2025.02.001.yaml`. It has 52 claims; the paper's text was complete enough that I didn't need to stop.

**Text read.** The accepted author manuscript from PubMed Central (PMC11932800), not the version of record. It includes the Results, Discussion, full Methods, the main figure legends and the supplementary legends (Figs S1 to S9, Videos S1 to S4). The supplementary figures exist only as legends, there was no PDF, and I did not see Supplementary Method S1 (a timeline schematic). No claim needs a value that appears only in a figure image.

**Code read.** The paper links an OSF project (doi:10.17605/OSF.IO/TBDWG) holding one file, `bci.zip`; I recorded its sha256 in the opening comment. It is the real-time system: task modules, the feature pipeline, Kalman filter code, the robot simulator, trained decoders, the scripts that fine-tune the RNN decoder, and the mode filter. It contains no offline analysis code, so none of the paper's statistics are implemented there. It disagrees with the Methods twice:
- **Data split:** the code fine-tunes the RNN on an 80/20 split, where the Methods give 85/15.
- **Action names:** the code's names for targets 1 to 7 don't match the Methods' mapping of actions to directions.

**Dataset.** From its title and description only, it holds B1's RNN training trials: 128 channels, high gamma and low-frequency signals at 100 Hz, 7 targets. That is probably not enough for most claims; one claim (the 14 h 48 min of RNN training data) is aimed directly at it.

**Counts**

| | Claims |
|---|---|
| Total | 52 |
| With quotes | 52 |
| With statistics | 41 (127 p-values and interval bounds) |
| With criteria | 52 |
| With expected values | 29 |

The quote checker finds all 52 quotes. It flags one value, p = 3.2442e-12 in `figs7i-ibid-straighter-than-refit`. I confirmed by reading that the paper prints exactly this; the checker only searches four significant digits.

**Details the paper leaves open, with the readings named**
- **Channel neighbours for cluster correction (Fig 1):** 4-connected or 8-connected.
- **Fig 1I-J:** which channels (the paper's hand-knob and ventral channels, or every significant channel), and how a repeated-measures ANOVA is formed over unpaired trials (one-way across actions, or trials paired by repetition).
- **Fig 1K-L correlation:** Pearson or Spearman.
- **Binomial chance test:** the usual upper tail, with the paper's wording ("area from 0 to N/m") shown as a variant.
- **Autoencoder:** reconstruction loss (mean squared or mean absolute error) and amount of augmentation (none, or doubled).
- **Per-subject variance scaling (Fig 2J):** none, divide by the maximum, or z-score.
- **Fig 2M-N points:** all three contexts, CL2 only, or the mean per session; the fit is a binomial model on the proportion.
- **CKA (Fig 3):** which samples go through both networks (pooled days, or each day through both), and what the shuffle permutes (weight entries or units).
- **Fig 4B:** which days, channels and observations underlie t(11).
- **Fig 4C-D:** how day labels enter the autoencoder (one unit per day, or per day and action) and whether splits are by sample or by trial.
- **Fig 4F-G robust regression:** bisquare or Huber weighting.
- **Fig 4I:** the held-out day isn't identified, and the classifier's width is not given (64 units assumed).
- **Fig S6 distances:** 72 pooled values or 36 averaged over the two days.
- **PnP averages (Fig 5):** over blocks, pooled trials, or days; timed-out trials count as failures.
- **Fig 6G angular error:** all time points, or only those with non-zero velocity.
- **Fig 7 metrics:** median over days or blocks; median or mean completion time; which sessions count as "after ~1 week"; whether day 35 belongs to the first period or the second.
- **RNN training duration:** the whole stored trial, or only its active portion.
- **No test given:** for Fig 1M-N clustering, Fig S5 map preservation, Fig 6G velocity covariation and Fig S8G coactivation, I set thresholds myself as standard choices and labelled them as not the paper's.

**Gaps in the paper**
- **Fig 4F-G:** the paper prints identical slope, z and p for B1 and B3, so one is likely a copy. B3 is held only to the slope's sign and significance.
- **Not stated anywhere:** the number of null iterations for the Fig S2 test, the temporal smoothing kernel, and whether the ± spreads in Fig S4G are SD or SE.
- **Never named:** the Fig 4B channels and the Fig 4I test day.

Nothing a claim needed was missing outright.
