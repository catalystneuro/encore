I've worked through all the points in the round-1 report. The entry re-ran cleanly with `python tools/entry.py all` (check: 0 errors; notebook passes in about 5 min). Nothing is committed.

**Outcomes:** none changed.
- **27 of 28:** the verifier gave the same outcome I had.
- **`false-positive-rate`:** the verifier would call it not reproduced; I kept it blocked (`methods_underspecified`) and recorded the disagreement. The protocol says that when your procedure's false-positive rate is far from the paper's, the procedures differ and the claim is blocked. The verifier's own reason is that the procedure is at fault, which is that case.

**The draft changed during this revision.** Every asset of the draft was uploaded again between 23:00 and 23:10 UTC. My first good run read it mid-upload: 23 pre-MPTP monkey V files were missing and some monkey L files were read twice. I waited until the upload finished and ran it twice more. Both runs give exactly the numbers already in the record, so the re-upload changed nothing the analysis uses. I set `dataset: modified` to 23:10:32Z, the time the last run read, and noted the re-upload in the record, README and notebook header.

**What I fixed or added, by point:**
1. **Header table:** the 16 claims blocked by the false-positive rate are now marked "run, blocked", not "yes", with a note saying why.
2. **Antidromic latency:** the cell now prints each test against its threshold. The CSN p = 0.0190 is not below 0.0167, so the claim stays partially reproduced.
3. **Torque-size confound:** I added pre against post comparisons at the same per-trial command step, which the verifier asked for.
   - Movements: the change goes both ways depending on step and direction. Flexion is faster after MPTP at twice the smallest step; extension is slower at the smallest step.
   - Latencies are not shorter after MPTP at matched steps.
   - m2 is smaller after MPTP at matched steps, not larger (44.9 against 1.8, p = 0.004).
   - EMG duration (p = 0.43) and onset (p = 0.087) do not differ.
4. **Zero-phase filter:** on synthetic movements it reports onsets 14 ms early to 5 ms late, and the causal measure 1 to 13 ms late. 9 of 24 synthetic movements are wrongly flagged as moving before onset.
5. **EMG noise and negative m2:** the cell now prints that m2 is zero or negative in 66 of 305 pre-MPTP channel-sessions. Among those with a detected response, m2 exceeds m1 in 76.7%.
6. **DSI measurement choice:** stated in the helper's docstring and recorded as a deviation on `dsi-reduced` and `venus-dsi`.
7. **EMG threshold variants:** these now keep responses that last to the end of the window. The new numbers are 20.8 against 50.1 ms (1.5 SD) and 23.4 against 50.1 ms (3 SD). The conclusion says the DSI chi-square p is approximate.

From "What I could not check":
- **Spike windows:** every torque onset is at least 2968 ms after its trial's start and 1516 ms before its stop, so no analysis window is cut short.
- **Per-cell table:** now printed (baseline rate, threshold, latency, sign and largest change per direction).

Conclusions, Summary, README and the attempt notes are updated to these numbers. The round is recorded under `verifications`, with the verifier's reasons closely paraphrased and my changes under `response`.

**Not done:**
- **Problem 8** (the paper's "2-tailed t-test" wording reads closer to the t-test variant): I added no question for a reader. Both readings are already shown and both give rates far above 0.03, so the answer cannot change an outcome.
- **Problem 9:** needed no change; the count difference is already explained and within tolerance.
