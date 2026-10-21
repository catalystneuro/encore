I took up all seven answers and re-ran every claim they bear on. One outcome changed: `behavior-false-alarms` went from blocked to reproduced. The other affected claims keep their outcomes, and each one's notes in `attempts/000005-yu-2016-02.yaml` now say what the answer changed. The notebook ran from a clean environment in 302 s, and its outputs match the conclusions. Nothing is committed or pushed.

One check still fails. `entry.py check`, and so `entry.py all`, reports the same 25 errors as the last run, all on the earlier `-01` record, which has to stay as it is. None are on `-02`. So I ran the check and the notebook run separately, then built the handover.

### Questions, what each answer changed, outcome per claim (earlier outcome in brackets)

1. **Time resolution of dVm/dt.** The answer: the recording's sampling rate, not 1 ms bins. That is the rule I had already used, so the 1 ms bin results are now shown only for comparison.
   - `fs-vm-touch-whisking`: not reproduced [not reproduced]. The latency is 1.88 ms against 4.0 ± 0.4. The 1 ms bins, which would have matched, no longer count.
   - `exc-vm-touch-whisking`: partially reproduced [partially reproduced]. The latency stays 7.68 ms.
   - `exc-thalamus-photoinhibition`: partially reproduced [partially reproduced]. Both light-onset latencies are 0.10 ms, against 4.2 and 2.8 ms.

2. **Latency bin edge or centre.** The paper doesn't say, so the criteria now run both. Both were already computed.
   - `vpm-touch`: not reproduced [not reproduced]. Spikes per touch fail under either bin position.
   - `fs-touch-response`: see question 3. The latency is within tolerance under both (5.23 and 5.73 ms).
   - `pv-enphr-suppression`: partially reproduced [partially reproduced]. No latency is found within tolerance under either.

3. **Light-driven test and waveform measures.** The paper gives no test, so the criterion now runs four FS groups: driven at p < 0.001 or p < 0.01, each with and without the waveform boundary. I added the fourth group (p < 0.01, no boundary).
   - `fs-touch-response`: partially reproduced [partially reproduced]. The best group (p < 0.001, with the boundary) has 2 of 3 values within tolerance. Both groups without the boundary have only 1.
   - In VGAT-ChR2 mice the four groups hold 12, 20, 12 and 23 cell-attached FS cells against the paper's 24. Dropping the boundary comes closer to the paper's count, which suggests the boundary as I measure it leaves out cells the paper counted.

4. **Continuity correction in the chi-squared test.** The paper doesn't say, so the criterion now runs the test with and without Yates's correction.
   - `behavior-false-alarms`: reproduced [blocked, methods underspecified].
   - Per session without the correction, 6 of 9 mice show a significant decrease. The criterion asks for 6 of 8; the dandiset has 9 PV-IRES-Cre mice with light where the paper tested 8.
   - The other readings give 5, 4 and 5 mice.
   - Caveat, stated in the notes: the per-session reading counts a mouse if any session is significant, and mice have 1 to 11 sessions.

5. **One- or two-sided tests.** The answer: two-sided, as I had assumed. I now report the one-sided p as a variant that doesn't decide.
   - `thalamus-drives-fs`: blocked, too few cells [blocked, too few cells]. Only 5 FS cells qualify, so the smallest possible two-sided p is 0.0625.
   - Even one-sided it would fail: the whisking test gives p = 0.062.

6. **Light trials in the touch counts.** The paper doesn't say, so the criterion now runs every trial (x) and trials without light (y).
   - `behavior-touches`: partially reproduced [partially reproduced]. It matches under (x), which is what I had counted.
   - Under (y) the no-lick count is 0.80 against 0.9 ± 0.09, so (y) doesn't match.

7. **Whisking-onset windows and which touches bound whisking epochs.** The paper gives neither, so the readings O10 and O11 now apply to `exc-vm-touch-whisking`. I added these to the helper; the earlier epochs are reproduced exactly.
   - `exc-vm-touch-whisking`: partially reproduced [partially reproduced].
   - Across the 16 combinations, the whisking change is 0.65 to 0.86 mV with the onset windows (within tolerance in 2) and 1.07 to 1.13 mV with the epochs (within in all 16).
   - Touch amplitude (4.77 mV) and latency (7.68 ms) still fail, and these readings don't affect them.
   - Every other claim keeps the earlier epoch rule, and the helper's docstring says so.

The verifier's package is in `executed/000005-yu-2016/handover/`.
