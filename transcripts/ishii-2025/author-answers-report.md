There was one answered question, on fig6c-decay-length. Claim fig6c-decay-length changes from **not_reproduced** to **reproduced**, marked `assumed: true`, but the result depends on how cells that never return to baseline are counted.

**The question.** I asked whether the decay length could be read as the time from the peak of the response to the first sample below 0. The claims file only allowed (a) the time from onset to the first sample below 0 and (b) the total time below 0.

**What the answer changed.** The reader agreed and added reading (c) to the criterion: the time from the peak after onset (0 to 120 s) to the first sample below 0 after it. The criterion now says the claim is reproduced when Vgat is longer at p < 0.05 under any one reading. The statement, expected values and statistics did not change.

**Outcome for fig6c-decay-length**

| Reading | Vgat vs Vglut2 (s) | t, p | Earlier |
|---|---|---|---|
| (a) onset to first sample below 0 | 18.7 vs 22.2 | -0.608, 0.544 | same, decided not_reproduced |
| (b) total time below 0 | 53.9 vs 75.3 (Vgat shorter) | -2.641, 0.0089 | same |
| (c) peak to first sample below 0 (new) | 45.2 vs 20.9 | 3.037, 0.0027 | shown only as a variant before |

The paper reports t(217) = 3.040, p = 0.00266. Reading (c) gives the same value as the deposited per-cell decay lengths for 207 of 219 cells.

**Why it is marked assumed.** 44 cells never fall below 0 after the peak: 43 Vgat and 1 Vglut2, and 31 of them come from one mouse, Vgat_2. The paper does not say what value they get. I gave them the full 120 s, because the deposited table has 120 for all 44. Under other choices the effect is not significant:

| Variant | Vgat vs Vglut2 (s) | p |
|---|---|---|
| unreturned cells counted to the end of the window | 28.9 vs 20.6 | 0.111 |
| unreturned cells left out | 22.4 vs 18.0 | 0.299 |
| rank-sum test under (c) | | 0.187 |
| per-animal means (6 and 4 mice) | 40.9 vs 20.2 | 0.149 |

I added this to the claim's notes and deviations, and to the existing finding that asks the authors how decay length is defined. It now also asks what value a trace that never returns below 0 gets.

**Files changed**
- `mpoa.py`: `decay_length` treats (c) as one of the claims file's readings, and takes an option for how unreturned cells are counted (120 s, to the end of the window, or left out).
- The notebook's fig6c section, its Result cell and the summary table.
- `README.md`.
- `attempts/001249-ishii-2025-01.yaml`: the outcome, notes, deviations and the finding.

No other claim changed. fig6k-late-cluster-vgat already used reading (c) with 120 s, and its re-run numbers are the same as before. fig7fg-activation-suppresses is still partially reproduced, so the "failure to reproduce" sentence stays in the README and the notebook summary.

**Entry runs.** Lock, check and run all passed with 0 errors; the notebook ran in 90 s. I checked that the executed notebook prints the numbers the conclusions quote. The handover is in `executed/001249-ishii-2025/handover`. I did not verify my own work, and nothing is committed or pushed.
