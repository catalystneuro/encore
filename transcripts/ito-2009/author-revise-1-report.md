I've worked through all 12 points in the round-1 report, re-run the entry with `python tools/entry.py all` (passes, 2319 s) and recorded the round under `verifications`. Of the 46 outcomes, 36 already matched the verifier's; 11 change below, 10 of them to the outcome the verifier gave.

**Outcome changes**

| Claim | Before | Now |
|---|---|---|
| fig2b-two-back-history | reproduced (assumed) | blocked, methods_underspecified |
| fig5-markov-accuracy | reproduced (assumed) | blocked, methods_underspecified |
| fig5-constant-models | reproduced (assumed) | blocked, methods_underspecified |
| fig5-fq-dfq-beat-all-models | not_reproduced | blocked, methods_underspecified |
| fig5-fq-dfq-no-difference | not_reproduced | blocked, methods_underspecified |
| table3-parameter-averages | reproduced (assumed) | blocked, methods_underspecified |
| fig8b-state-coding | reproduced (assumed) | blocked, methods_underspecified |
| fig5-variable-models-best | reproduced | partially_reproduced |
| table2-ml-parameters | partially_reproduced | not_reproduced |
| fig9-reward-information | partially_reproduced | not_reproduced |
| fig9-action-value-information-low | reproduced | partially_reproduced |

- **The seven blocked claims:** I agreed with the verifier. The claims file says a claim whose method readings disagree is blocked. My earlier "best-supported reading" choices went against that rule.
- **fig9-action-value-information-low:** this one is new and was not in the verifier's report. Fixing problem 7 made the O13 (b) estimate include trial t's reward. Under that reading the "no clear peak" part fails in 48 of 96 readings; under O13 (a) it holds in all 96. Round 2 will review it.

New totals: 23 reproduced, 7 partially reproduced, 8 not reproduced, 8 blocked. No outcome rests on an assumption any more.

**Added or corrected**
- **Filter seed noise:** I repeated the F-Q and DF-Q filter runs with six seeds and also averaged them. The F-Q against DF-Q result follows the update form, not the seed. Under O1 (a) every seed finds a difference (p 0.003 to 0.039); under O1 (b) none does (p 0.13 to 0.98).
- **Sigma search:** I ran a 5000-particle search on a wider grid (σα up to 0.08, σκ from 0.025). The likelihood surface is flat, and with α clipped the best σα sits at the edge of the grid.
- **Other requested outputs:** test scores at the paper's Table 2 sigmas, and the training fit at the paper's Table 1 and Table 2 values. DF-Q on the main split is a different optimum, not an equal second one.
- **Tone errors:** I recounted keeping only cue tones of at least 1 s, giving 0.56% and 0.98%. That is still not reproduced. I added a finding that the cue tone stops when the rat leaves early.
- **Fig. 5 local matching law:** the main table now shows it with Qi(1) = 0 (0.500) next to the assumed 0.5. I also added its Wilcoxon tests under every initial value.
- **Fig. 9 additions:** reward information aligned to each trial's own L/R entry, and the QL/QR information under every O1 and O5 reading.
- **Smaller fixes:** the corrected O13 (b) estimate in the helper, the one-sided partial column (problem 10), and the mirror pairing (problem 11; the residuals are unchanged).
- **Two questions for a reader** in the new `questions/001641.yaml`: the fig9-reward criterion (problem 5), and the table3 criterion's inconsistency with Tables 1 and 2 (problem 9).
- **Records:** the notebook conclusions, summary, README, entry runtime (now 39 minutes, up from 18) and the attempt record match the new numbers. `entry.py check` reports 0 errors.

**Not done, and why**
- Problem 8 (slow drift inflating the QL/QR information): no change, because the threshold follows the paper's method.
- The seed and wider-grid checks cover only the main split, and the wider grid only O1 (a). The full set did not fit the notebook's time limit.
- I did not block the claims that depend on fig5-markov-accuracy and fig5-constant-models. Those two are blocked for details the dependent claims do not use, and the reasoning is in the notes of fig5-variable-models-best.
