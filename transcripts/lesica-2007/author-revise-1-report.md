I've revised the attempt for every point in the round-1 report, and the final `python tools/entry.py all entries/lesica-2007` run passed in 46 minutes. Its outputs are identical to the run the conclusions were written from, and the entry check gives 0 errors. Nothing is committed.

**Outcomes now:** 16 reproduced, 7 partially reproduced, 15 not reproduced, none blocked. Nine changed from round 1, which is allowed in this round:

| Claim | Round 1 | Now | Why |
|---|---|---|---|
| fig3d-temporal-width-contrast | not reproduced | partially reproduced | Measured on the paper's 8 ms grid: movie +16.8%, p = 1.4e-10, within tolerance; noise +23.8%, but p = 0.011 misses p < 0.001 |
| surround-temporal-correlation | not reproduced | partially reproduced | r = -0.37 with the 8 ms width; -0.47 to -0.48 (within tolerance) when both measures come from the 8 ms RFs |
| methods-latency-biphasic | partially reproduced | reproduced | Latency changes in 3 of 3 comparisons with the 8 ms RFs; the biphasic ratio changes in none |
| fig4c-offset-correlations-none | reproduced | not reproduced | With the offset adjustment applied evenly, p = 0.012 |
| disc-lcns-hcwn-rf-nl-differences | reproduced | not reproduced | Normalized offset p = 0.056, so 2 of 4 properties are significant, not 3 |
| fig8de-noise-reconciles | not reproduced | reproduced | Under the long-segment stimulus reading, levels exist where all four stimuli match, under all five seeds |
| fig5-within-trial-contrast | blocked | not reproduced | Run on the 24 OFF-center Y cells; no cell shows all four expected changes |
| methods-spherical-asymmetry | blocked | not reproduced | Movie and noise estimates differ at 32 to 66 of 5292 RF points, against 1 to 3 between two movie runs |

**What I changed for each problem:**
- **Ridge penalty (problem 1).** I kept the penalty of 10000 x stimulus variance, so the verifier's objection stands and is recorded. My grounds:
  - The paper's literal value (1000 in gray levels) gives RFs at the noise level: no cell passes the inclusion rule and the median latency is 158 ms.
  - It also predicts held-out data worst (r = 0.170 against 0.437).
  - The paper's own rule for choosing the penalty still picks 10000 x variance.

  The literal value and a lower one (1000 x variance) now run as variants in the same pass. Under the lower one, 29 cells pass instead of 111, and several results change, which supports the verifier's point. Four outcomes rest on the penalty and are marked as assumptions: the width and surround correlation effects, the gain correlation effect, and offset-correlations-none.
- **Uneven offset adjustment (problem 2).** The per-animal adjustment is now made within each set of cells compared. The 31 white-noise cells all come from one animal, so none of their offsets is shifted. The old uneven version is shown as a variant.
- **Frame-resolution RFs (problem 3).** Temporal width, latency and biphasic ratio now come from RFs at 128 Hz with 24 lags of 8 ms, as the paper gives. To fit the time limit they use a 15 x 15 window instead of the paper's 21 x 21; that is recorded as an assumption, and the frame-rate values are kept as a variant.
- **fig8de (problem 4).** The noise scan now runs under both stimulus readings.
- **Units whose RF sign flips (problem 5).** They are counted (13 of the 111 included cells), and left out as a variant for the ON/OFF claim and the generic RFs. The outcomes don't change.
- **Docstring (problem 7).** The `pct_change` docstring now matches the code.
- **Trial selection (could-not-check item).** Added a per-file inventory showing which recordings are used. It answers the question: Expt1 a12 and b12 hold only a 100 s noise test, and the 600 s and 901 s noise recordings are the ones used in a11, a13 and a14.

The record now has a `verifications` block: the verifier's outcome and reason for all 38 claims (it agreed with every round-1 outcome) and my response to each. The question for the authors about the penalty is reworded. The notebook conclusions and summary, the README counts and the runtime (now 47 minutes) are updated.

**Not done:**
- No `questions/lesica-2007.yaml` entry: the report names no place where the claims file misreads the paper.
- fig5 was tested on the OFF-center Y cells only, under two of the four ways the criterion allows the contrast to be measured, with a 1 s window I chose because the paper gives none. Its "share of cells" is therefore over those 24 cells, not all included cells.
- The 8 ms RFs use the smaller window, and the spherical-asymmetry simulation runs at the frame rate rather than 128 Hz.
