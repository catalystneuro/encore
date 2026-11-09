The reader answered one question, on `fig1f-movement-latencies`. The outcome stays partially reproduced. I re-ran the claim under the amended criterion, and the entry now locks, checks and runs cleanly. All three notebooks pass from a clean environment, in 334 s, 880 s and 1309 s.

**The question.** The criterion took each movement trace's maximum over 1.0 to 1.2 s. Under that window a latency cannot exceed 200 ms, yet the paper reports 231 ms for the tongue. I asked whether the paper takes the maximum over a longer window.

**What the answer changed.** The reader agreed the 1.2 s window is not the paper's. The amended criterion takes the maximum over 1.0 to 2.0 s, the 1 s response window in the Methods, under both readings:
- reading (a) measures the latency on each session's mean trace;
- reading (b) measures it on each trial, then averages per session.

1.0 to 1.2 s is now only a variant. The statement, quote and expected values are unchanged.

**Outcome for `fig1f-movement-latencies`.** It is partially reproduced, the same as before.

| | Earlier (max over 1.0–1.2 s) | Now (max over 1.0–2.0 s) | Paper |
|---|---|---|---|
| Reading (a): whisker / jaw / tongue | 48.2 / 81.5 / 140.0 ms | 54.4 / 115.3 / 192.4 ms | 58 / 115 / 231 ms |
| Reading (b): whisker / jaw / tongue | 65.2 / 83.3 / 153.6 ms | 94.6 / 142.9 / 254.6 ms | |
| Lick latency | 330.1 ms | 330.1 ms | 330 ± 20 ms |

- **Reading (a):** the whisker and jaw latencies are now within tolerance. The tongue latency is 38.6 ms short of 231, outside the 29 ms tolerance.
- **Reading (b):** only the tongue latency is within tolerance.
- **Both readings:** the order whisker, jaw, tongue, spout contact holds, so both meet the criterion's definition of a partial result.
- **Late sessions:** a few sessions pull the means up. Under reading (a) the medians over sessions are 50.0, 95.0 and 155.0 ms. The two sessions of mouse PG019 average 315 ms for the jaw and 385 ms for the tongue.

**What I changed:**
- **Notebook (`reproduce_ghaderi_2026.ipynb`):** the fig1f section now uses the 1.0 to 2.0 s window. It also prints whether the order holds, a breakdown by subject and the medians, and keeps 1.0–1.2 s, 1.0–1.5 s and the code's quiet-trial rule as variants. The conclusion is rewritten.
- **Attempt record:** I replaced the measured values (54.4, 115.3, 192.4, 330.1) and rewrote the notes, which say what the answer changed.
- **New finding:** I added a `methods_unavailable` finding that asks the authors how "time to 20% max" is computed. None of the paper's code computes it, and the two readings give quite different values.

The README and the summary table did not need changes, since the outcome is the same. The handover is in `executed/001530-ghaderi-2026/handover/`. I did not verify my own work, and nothing is committed or pushed.
