I've revised the attempt for every point in the round-1 report, re-run the entry, and recorded the round. The full run passed in about 81 min: 40, 27 and 13 min for the three notebooks. `entry.py check` reports 0 errors and the handover is rebuilt. After the run I edited only markdown cells (conclusions, summaries, headers), and copied them into the executed copies without re-executing; the code cells and their outputs are unchanged. Nothing is committed.

**Outcome changes.** Of the 56 claims, 47 are now tested (36 reproduced, 5 partially reproduced, 6 not reproduced) and 9 are blocked, against 45 tested and 11 blocked before.
- **amplitudes-log-normal**: partially reproduced → reproduced. On the claims file's own selection (QC pairs 60 to 400 um), the spikelet log skew is 0.41 and the IPSP log skew 0.13, both inside the bounds. The earlier failure came from the pairs under 60 um.
- **ipsp-median-amplitude**: reproduced → partially reproduced, as the verifier said. The criterion averages the two mice's fluctuation values, and the average, 0.234, is outside 0.20 +/- 0.02.
- **npy-oscillation-peak-rates**: reproduced → blocked (methods underspecified). Its two named readings disagree, and the claims file's header blocks such claims.
- **spikelet-not-scatter**: blocked → reproduced, on the first 40,000 frames of the raw movie. The spikelet-to-scatter ratio at 40 to 80 um is 3.03, and the scatter falls off faster than the spikelet.
- **lasso-off-target-correction**: blocked → not reproduced, resting on assumptions. I rebuilt per-pulse responses and evoked spikes for the 14,400 pulses per mouse. With the cross-validated penalty, R = 0.937 and 72% of pairs change by more than 20%. With the one-standard-error penalty, almost every coefficient is zero.
- **traveling-waves**: blocked → not reproduced, resting on assumptions. I ran the Methods procedure, with each open detail as a reading. No reading gets both the event count and the speed within tolerance. The direction could not be tested, because the files do not say how the image axes sit on the brain; I added this as a finding.
- **detection-limits**: still blocked, now as too large. The pairwise table stores no per-pair statistic or null distribution. Rebuilding the nulls would take about 1,950 hours at the measured 48 ms per fit.

**Kept, with outputs added.**
- **two-mice-intrinsic-distributions**: reproduced. Treating the 7 membrane time constants of exactly 0 as failed fits makes both readings agree; this is now marked as an assumption.
- **npy-ipsp-duration**: reproduced. Leaving out the 91 fits that end on the 0.4 s bound gives 57.1 and 41.9 ms against the paper's 58 and 43; also marked as an assumption.
- **fig3lo-variance-components**: reproduced. Over all 2,000 refits, including the non-converged ones and their refits, the adverse share is 0% (amplitude) and 0.05% (decay), under the 0.1% bound.
- **fig5e-inhibition-in-spontaneous-voltage**: still reproduced; the disagreement with the verifier is recorded. Measured on the control-average waveform, the controls' rise is +0.0097 for all connected pairs, inside tolerance, but +0.0049 for the top quintile.
- **voltage-to-spike-sigmoid**: still reproduced, narrowly. I added the 10 ms interval reading (42% of cells pass, below half) and bounded-top fits (CVs 0.64 and 0.29). It passes only on the spike-frame reading the Methods and code use.
- **npy-classifier**: z-scoring now happens inside each training split; the numbers are unchanged.
- **interaction-kernel**: added a second FWHM baseline, which gives 4.94 ms instead of 22.7 ms; still not the claimed ~2 ms.
- **spike-snr-and-detection-errors**: the raw-movie excerpt is now listed in full; it holds no matched-filter output or fitted mixture.

**Record and questions.**
- The attempt record has a `verifications` entry for round 1, with all 56 claims, the verifier's reasons and my responses.
- I added findings on the image-axis orientation, on the fits at the decay bound, and updated the wave and lasso method questions for the authors.
- I created `questions/001960.yaml` with the four claims-file misreadings the verifier reported (voltage-to-spike-sigmoid, fig5e voltage, lasso, and the "800" count).

**Not done.**
- The spike-detection false-discovery and false-negative rates were not rebuilt. They would not change the outcome, since the SNR alone fails under every reading.
- spike-synchrony-localized is unchanged: its criterion says to average the two mice, and the per-mouse values are printed.
