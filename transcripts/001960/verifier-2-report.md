**Verifier report, round 2: Qi et al. 2026, DANDI:001960 v0.261013.2016**

The claims file has 56 claims. The attempt record has 56 outcomes: 36 reproduced, 5 partially reproduced, 6 not reproduced and 9 blocked. Six outcomes are marked `assumed: true`, and the README's counts match. In the notebook references below, EC = `qi2026_excitability_connectivity`, SP = `qi2026_spontaneous` and ES = `qi2026_excitability_spontaneous`; cell numbers start at 0.

### 1. Outcomes and assumptions

I agree with 55 of the 56 outcomes. I disagree with one:

- **voltage-to-spike-sigmoid (reproduced, assumed).** The criterion names two readings: V at the spike frame, and V in the 10 ms before ("both shown"). They give different outcomes: 52% of cells against 42% (mean of the 8 frames before) and 24% (single sample 8 frames before) (SP cell 28). The claims file's header rule (lines 80–81) says such a claim is blocked as methods_underspecified. The attempt chose the spike-frame reading because the Methods' V(t_s) and the code support it. That amounts to correcting the claims file's misreading (it attributes the 10 ms to the Methods) instead of reporting it. Under the claims file as written, the outcome should be blocked. I accepted this outcome in round 1; I missed the header rule then.

The other five assumed outcomes:

- **two-mice-intrinsic-distributions.** The assumption is stated and reasonable. No fitted decay has a time constant of 0. Treated as missing, both named readings give 5 of 5 calls (EC cell 22).
- **hadamard-stimulation-rates.** The assumption is stated and reasonable. The criterion itself speaks of "750 ms on blocks", and counting 750 ms steps gives 650, within 640 ± 64.
- **npy-ipsp-duration.** The assumption is stated and well supported. Leaving out the fits on the 0.4 s bound brings the means, s.d. and counts close to the paper's. Kept, the header-consistent selection (QC pairs within 400 µm) fails on the NPY− count, 723 against 646 ± 65 (EC cell 83).
- **traveling-waves.** The assumption is stated and reasonable, and the outcome holds under every reading run. Under the attempt's count-per-span reading, the "extrema" spans fail on the count (4446) and the "window" spans fail on the speed (6.2 mm/s). Counted as derivative peaks, both fail on the count (6909 and 6198). The direction part cannot be tested, so a pass could only have been partial.
- **lasso-off-target-correction.** The assumption is stated, but the result is weak. The rebuilt raw matrix correlates only R = 0.64 with the stored amplitudes, and its median is −0.0183 against −0.0297 SH (EC cell 43). The paper compares the corrected matrix with the connectivity matrix, which is the stored amplitudes. The attempt compares it with its own rebuilt raw matrix. Not reproduced is defensible but fragile.

Two outcomes not marked as assumed also rest on computational choices:

- **spikelet-not-scatter.** Choices include the 4×4 interstitial bins and comparing scatter and spikelets from different sessions. Every variant passes (ratio 2.8–3.4 against the 2.25 cut), so no `assumed` flag is needed. All 189 triggers have spike fluorescence ≤ 0, which a negative-going indicator (Voltron1) would explain, but the notebook does not say so.
- **detection-limits (blocked, too_large).** I agree.

### 2. Sentences the printed outputs do not support

- **EC cell 38, and the detection-limits notes and response.** The text says "One fit of the IPSP model takes 48 ms here… about 1,950 hours". Cell 37 prints 57.7 ms and 2336 h.
- **EC cell 65, and the fig3lo-variance-components notes.** The text says "among the 1,963 converged refits… (the 37 non-converged have pre minus post 0.029 to 0.118)" and "none of the 51 non-converged (pre minus post -0.144 to -0.047)". Cell 64 prints 1971 of 2000 converged for amplitude (29 non-converged, range 0.0574 to 0.1213) and 1969 of 2000 for decay (31 non-converged, range −0.1329 to −0.0011). The closest decay refit is therefore −0.0011, almost adverse, not −0.047. The outcome still holds: 1 of 2000 adverse.
- **EC cell 71, and the fig5e-inhibition-in-spontaneous-voltage notes.** The text says "+0.0097 for the controls of all connected pairs… and +0.0049 for those of the top quintile; per control pair it is +0.012 (mean; median +0.003) and +0.019 (median +0.007)". The per-pair values are in the reverse order of the sentence: top quintile mean 0.0120, median 0.0031; all connected mean 0.0191, median 0.0073 (cell 70).
  - The record's `measured` [−0.0189, −0.0095, 0.012] uses reading (a), whose top-quintile value is at the edge of tolerance. It also uses a per-pair control mean. The reading that passes gives −0.0213, −0.0095 and a control-average rise of 0.0097.
- **SP cell 29, and the voltage-to-spike-sigmoid notes.** The text gives "maxima (CV 4.56)". Cell 28 prints CV 4.54.
- **SP cell 23, and the traveling-waves notes.** The text says "hundreds to thousands of mm/s in every case (medians 70 to 920 mm/s)". The window-span medians are 61–92 mm/s, and the per-mouse medians run from 61.2 to 1205.5 (cell 22).
- **The npy-classifier notes.** They say "each mouse alone 76.3 to 76.7%". EC cell 80 prints 76.6 and 76.3.
- **The npy-ipsp-duration deviation.** It says "the paper's means and s.d. within 1 ms". The NPY− mean is 41.9 against 43, i.e. 1.1 ms off (EC cell 83). The response says "within 1.5 ms".
- **The spikelet-not-scatter deviation and EC cell 39.** They say "about 110 frames per second… about 3 hours". EC cell 40 reads 40,000 frames in 270 s, about 148 frames/s, or about 2.2 h for the whole excerpt. The response's "about 7 minutes" compares with 4.5 minutes printed.
- **EC cell 44.** "The rebuilt raw matrix measures the stored IPSPs" overstates R = 0.64 and a 38% lower median.
- **README.** It gives run times of about 40, 27 and 13 minutes. The notebooks print 28.4, 21.7 and 9.7 minutes.
- **Several notes refer to questions put to a reader.** These are the notes for synaptic-connection-counts, lasso, voltage-to-spike, fig5e-voltage and npy-ipsp-amplitude, each marked "(questions)". The attempt record has no questions section, so I cannot check them.

Everything else in the Result cells, the three Summaries, the README and the notes agrees with the printed outputs.

The verification entries state my round-1 reasons faithfully and in my own words. The 5 entries marked `agrees: false` are the 5 claims where my round-1 outcome differed from the attempt's.

### 3. Round-1 points

**Resolved:**

- 1: traveling-waves was run.
- 2: lasso was run.
- 3: the full pairwise table is now listed.
- 4: amplitudes-log-normal was rerun on the header's selection.
- 5: the membrane time constants of 0 were treated as missing.
- 6: every refit is now shown; the stale numbers are listed in section 2.
- 7: the raw excerpt is now listed.
- 9: the control rise was measured on the control-average waveform.
- 10: a partial test of the scatter was run.
- 11: the FWHM variant was added.
- 12: the scaler is now fitted on the training cells of each split.
- 13: the header-consistent selection was run.
- 14: the criterion averages per mouse.

Point 8 is partly resolved: the 10 ms interval reading and bounded maxima were added. Point 15 was passed to a reader, which I cannot check here.

**Still bearing on a conclusion:**

- voltage-to-spike-sigmoid should be blocked as methods_underspecified under the claims file's header rule, not reproduced on an assumption.
- lasso-off-target-correction: the corrected matrix is never compared with the stored connectivity matrix, which is the paper's comparison. The rebuilt raw matrix matches the stored one only at R = 0.64, so the failure may come from the reconstruction.
- fig5e-inhibition-in-spontaneous-voltage: the `measured` values should be those of reading (c) and the control-average rise of 0.0097, the values the outcome rests on.
