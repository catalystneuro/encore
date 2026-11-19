I finished steps 1 to 6 of the Author section. Of the 38 claims, 16 are reproduced, 6 partially reproduced, 14 not reproduced and 2 blocked. The entry passes check, `all` runs it in 28.5 min, and the handover package is built in `executed/lesica-2007/handover/`. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| sample-composition | not reproduced: 111 cells pass the inclusion rule (paper 68); the noise/repeats subset is 31 (paper 31); the 90 s subset is 58 (paper 26) |
| firing-rate-contrast | partially: all four means are in tolerance, but the noise test gives p = 0.0022, not p < 0.001 |
| firing-rate-lc-ns-wn-similar | reproduced, resting on an assumption: p = 0.063 over the long segments, p = 0.0013 over the 12 s repeats |
| ln-prediction-accuracy | not reproduced: r = 0.48 / 0.53 (paper 0.70 / 0.76) |
| fig3b spatial width, contrast / correlations | reproduced / reproduced (18.9%) |
| fig3c surround, contrast / correlations | not reproduced (no change with noise) / reproduced (37.2%) |
| fig3d temporal width, contrast / correlations | not reproduced / not reproduced |
| surround-temporal-correlation, figs1 | not reproduced, not reproduced |
| fig4b gain, contrast / correlations | partially / partially |
| fig4c offset, contrast / correlations-none | reproduced / reproduced |
| fig4d normalized offset, contrast / correlations | not reproduced / not reproduced |
| fig6a reliability, contrast / correlations | partially / reproduced |
| fig6b sparseness, contrast / correlations | partially / reproduced |
| fig7c, fig7d, fig8a, fig8 shuffle, fig8b | reproduced (all five) |
| fig8de | not reproduced |
| disc reliability/sparseness, disc RF/NL differences | reproduced, reproduced |
| methods-latency-biphasic | partially |
| methods-offset-varies-across-animals | not reproduced |
| celltype: Y wider / Y stronger surround / OFF wider temporal / prediction X vs Y | reproduced / not / not / not |
| fig5-within-trial-contrast, methods-spherical-asymmetry | blocked (`other`): not run within the time limit |

## 2. The dataset, assumptions, questions

- **Version:** pinned 0.261102.1631, the only published version.
- **Data used:** the paper's data are in Expt1 and Expt2 (two cats). Expt3 and Expt4 belong to the dataset's other papers. The clocks check out.
- **Findings about the dataset:**
  - The 90 s cross-validation repeats are frames 0-5400 of the same 15 min movie the RFs are fitted from; the paper calls them "a different" segment. I left those frames out of the Expt2 fits.
  - The noise recordings last 10 and 15 min, where the paper says 6 min. I used the first 6 min.
  - The units have no ON/OFF label; I took it from the sign of each RF.
  - Nothing records which units make up the paper's samples.
  - Paper inconsistency: it says 120 Hz updated every other refresh (60 Hz) and also 50 Hz; the files show 59.96 Hz.
- **Main assumption:** the ridge penalty. I chose it by held-out prediction, as the paper chose D, and set it relative to the stimulus variance. A fixed gray-level penalty, tried while preparing, made RF widths grow at low contrast.
- **Questions for the paper's authors** (`methods_unavailable` findings):
  - the stimulus scale behind D;
  - how percent changes, the surround peak and the per-animal offset adjustment were computed;
  - which rates were compared between low-contrast movie and noise;
  - which cells, positions and segments were used for the generic RFs.
- **Questions to a reader:** none.

## 3. Protocol points

1. Seeds are fixed per claim, but one shared computation (the shuffles behind inclusion and every RF's error level) feeds most claims. I used the seed of sample-composition and gave each unit its own generator, seeded from that seed and the unit's identity.
2. The criteria often define reproduced and partially reproduced only, while the "tests" fail in one of two conditions. Where the criterion's partial rule did not apply I used not reproduced; for firing-rate-contrast, where only the p-level missed, I used partially and said so in the notes.
3. "Blocked for time" has no category other than `too_large`, which the protocol reserves for computation that ran out. Fig5 and the spherical-asymmetry simulation were never started, so I used `other`.
4. Conclusions have to be in the executed notebook, so any wording fix forces a full re-run (here 28 min each). I ran three times.
5. The protocol does not say what to do when the paper's tuning parameter (D) is tied to a scale the dataset cannot reproduce. I re-ran the paper's own rule for choosing it and recorded the result as an assumption.

## 4. Runtime and failures

- **Runtime:** about 3 h 15 min of the 5 h (19:01 to 22:17 UTC). The notebook takes 28.5 min, run in four parallel processes.
- **Failures:**
  - My first full pass crashed after 22 min on a unit with no spikes; I added a guard and re-ran.
  - One cell (a13 sig006b) has a repeat block without spikes and is dropped from the reliability claims (30 of 31 cells).
  - Untracked dotfiles and an empty `scripts/` directory in the checkout were there before; I left them.
