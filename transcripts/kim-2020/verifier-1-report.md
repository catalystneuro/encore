# Verifier report, round 1: Kim, Atencio & Schreiner 2020 on CRCNS ac-5

The claims file holds 45 claims. The notebook tests 42 and treats 3 as blocked (the two Supplementary Fig. 2 claims and the Supplementary Fig. 3 claim). My tally of outcomes: 12 reproduced, 10 partially reproduced, 20 not reproduced, 3 blocked.

**About the neuron groups.** "G" is the 15-neuron group the notebook uses for every Table 1 claim. It is built from the claims' D7 (b) reading plus a cluster-mass test that the author added. "GA" is the 37-neuron group under the claims' D7 (a) reading. The paper's group has 30 neurons, so neither matches. Where a criterion says "under one reading", I accepted a pass in either group. For claims of absence whose criterion does not say that, I required the readings to agree, and graded disagreement as partial.

## A. Outcomes

| claim | outcome | reason |
|---|---|---|
| cc-cohort-counts | reproduced | Cells 4, 13: 66 tone recordings and 40 paired DMR recordings, matching the data set's table. The data carry no animal identifier; there are 39 recording dates. |
| vc-cohort-counts | reproduced | Cell 15: 27 excitatory, 12 inhibitory, 31 neurons, 8 with both. The 24 mice cannot be checked (22 recording dates). |
| fig1-psp-amplitude-kinetics | reproduced | Cell 17, pooled s.d. with D16 (b): 14.0 mV, rise 30.3 ms, decay 91.7 ms, all within tolerance. D16 (a) gives 25.2 mV, outside. |
| fig1c-resting-potential-range | reproduced | Cell 19: −84.7 to −55.1 mV under (a), −83.8 to −53.7 mV under (b). Both are inside the widened range. |
| fig1d-ndr-distribution | reproduced | Cell 21, pooled s.d.: first bin highest (19), 31 neurons at ≥ 0.3, 6/66 above 0.7. The per-tone s.d. reading fails (18 neurons). |
| fig1e-ndr-vs-rest-weak | reproduced | Cell 23, pooled s.d. with rest (b): r = 0.182, p = 0.144. The other readings give r = 0.03 to 0.12, all non-significant. |
| fig1fgh-trf-bandwidth-narrowing | partially_reproduced | Cell 25, reading (a): spikes narrower, p = 3.7e-4, median ratio 0.90. PSP bandwidth30 is 1.94 octaves, outside 1.38 ± 0.33, and only 28 of the 31 neurons are used. |
| fig2-psp-histogram-modality | not_reproduced | Cell 29: none of the 12 combinations of D2, D3 and D4 gives 24/16. The closest is 21/19. |
| fig2-strf-significance-groups | not_reproduced | Cell 31: D7 (a) gives 37/3, D7 (b) with the cluster test gives 15/11, and the code's analytic p = 0.005 variant gives 29/6. |
| fig2-psp-amplitude-ranges | not_reproduced | Cell 33: the large and small PSP ranges overlap under both D2 readings (n = 15). |
| supfig2-strf-reliability | blocked (data_missing) | The data set holds 2 repeats of 1 neuron (cell 103), so 1 pair against the paper's 13. The criterion asks for the pairs present to be reported; the notebook did not report this one. |
| supfig2-psp-more-reliable-than-spikes | blocked (data_missing) | One pair; no test is possible. |
| supfig3-intensity-invariance | blocked (data_missing) | One neuron at 38, 54 and 69 dB SPL (cell 103); the ANOVA over 5 neurons cannot be run. The per-level values were not reported. |
| fig3d-double-peaked-counts | not_reproduced | Cell 35: under D9 (a), spikes 16, PSPs 15, small PSPs 8. Spikes are not rarer than PSPs. D9 (b) marks 35 to 40 neurons double-peaked. |
| fig3e-harmonic-ratios | not_reproduced | Cell 37: 17 ratios, 1.67 not the most common (4 of 17), and ratios of 5.3, 12.2 and 15.1 are present. |
| fig3f-bandwidth-single-vs-double | reproduced | Cell 39, grouping (a) with D8 (a): medians 0.30 and 0.90 octaves. Fragile: the groups are 9/26, not 20/20, and 0.30 octaves is exactly 3 channels. |
| fig4c-btmf-small-psp-higher | reproduced | Cell 43: under G with D11 (b), means are within tolerance and the tests give p = 0.004 and 0.039. This is 1 pass in 6 reading × group combinations; under GA the small vs large test fails. |
| fig4d-bsmf-small-psp-higher | not_reproduced | Cell 45: means are within tolerance, but no reading or group gives p < 0.05 (p ≈ 0.08 in G). |
| tab1-modulation-large-psp-like-spikes | reproduced | Cell 47: spikes vs large PSPs, p = 0.85 and 0.99 in G, and 0.47 and 0.98 in GA. |
| fig4b-bsmf-btmf-correlation | not_reproduced | Cell 49: the large-PSP r is −0.10 in G and 0.09 in GA (paper 0.53). |
| fig5a-cf-bf-correlation | not_reproduced | Cell 51: r = 0.04 on kHz and −0.01 on log2 frequency (n = 35); the analytic variant gives 0.23. |
| fig5b-bf-same-across-events | reproduced | Cell 53: ANOVA p = 0.68 (kHz) and 0.46 (log2); median BF differences 0.10 and 0.00 octaves. Only G (n = 15) was run. |
| fig5c-bandwidth-relationships | not_reproduced | Cell 55: 0 of 6 counts within tolerance. The comparison itself is invalid: counts from 15 neurons are compared with counts from 30 (problem 3). |
| tab1-single-band-small-psp-narrower | partially_reproduced | Cell 57, reading (b): small PSPs are narrowest (0.34 vs 0.35 octaves for spikes, p = 0.88), which meets the partial rule only just. The large and small PSP means are outside tolerance, and reading (a) has n = 2. |
| tab1-total-bandwidth-no-difference | partially_reproduced | Cell 59: under D8 (a) in G no pair differs, but the means are 1.40, 1.06 and 0.69 octaves against about 0.5. D8 (b) in G (p = 0.043, 0.027) and D8 (a) in GA (p = 0.020) both show small PSPs narrower. |
| tab1-latency-duration | not_reproduced | Cell 61: no reading puts all six means within tolerance (large-PSP latency 73.7 ms under (a); spike latency 29.3 ms under (b)). |
| tab1-event-rate-no-difference | partially_reproduced | Cell 63: no difference in G, but large vs small PSPs differ in GA (p = 0.008). The large and small PSP means (0.90 and 0.73 Hz) are outside tolerance. |
| tab1-fsi-spikes-higher-than-large | reproduced | Cell 65, GA: means 0.19, 0.11 and 0.13 are within tolerance; spikes > large PSPs (p = 0.030); small > large (p = 0.005); spikes vs small n.s. It fails in G (spikes vs large p = 0.40). |
| fig6b-tab1-threshold-spikes-higher | not_reproduced | Cell 67: PSP thresholds are positive (0.64 and 1.13 in G); no reading has spikes above both PSP types at p < 0.05. |
| fig6c-tab1-transition-spikes-lower | not_reproduced | Cell 69: spikes 0.98, large PSPs 0.84, small PSPs 0.97; no differences under any reading. |
| fig6bc-no-correlation-psp-spike-nonlinearity | partially_reproduced | Cell 71: in GA none of the four correlations is significant; in G the small-PSP vs spike transition correlation is (r = 0.54, p = 0.038). |
| fig6d-spike-threshold-transition-covary | partially_reproduced | Cell 73: GA spike r = −0.37, p = 0.025, negative and significant but outside tolerance; both PSP correlations n.s. In G, r = −0.02. |
| fig6efg-fsi-relationships | not_reproduced | Cell 75: in GA the signs are right, but all three spike r are outside tolerance, and PSP event-rate correlations (−0.91) are stronger than the spike one. |
| fig5df-strf-narrower-than-trf | reproduced | Cell 77, D15 (a): deltas 0.57, 0.91 and 1.28 octaves are within tolerance and positive; ANOVA p = 0.40. The match comes from two inflated widths offsetting (TRF 1.97, STRF up to 1.40 octaves); 2 of the 3 medians are outside. |
| fig5e-q-strf-higher | reproduced | Cell 79: STRF Q > TRF Q30 under all four readings (PSP p ≤ 3e-5, spike p ≤ 0.026); 15 paired neurons have NDR ≥ 0.3. The tests use n = 35 and 11. |
| fig7-current-amplitude-unimodal | partially_reproduced | Cell 83: by the dip test 100% (20 pA) and 97% (40 pA) unimodal; by KDE 87% and 72%. |
| fig7c-ei-bf-matched | partially_reproduced | Cell 85: only 6 of 8 pairs have a BF. Reading (b) holds (median 0.15 octaves); reading (a) fails (r = 0.74, p = 0.096). |
| fig7d-current-double-peaks | not_reproduced | Cell 87: under D9 (a), 13/27 excitatory, 2/12 inhibitory, 15/31 neurons. |
| fig7e-tab2-inhibition-broader | partially_reproduced | Cell 89, D8 (b): inhibition wider than excitation (p = 1e-4) and than current clamp (p = 3e-4), but the excitatory mean, 0.34, is just outside 0.65 ± 0.30. Under D8 (a), inhibition is narrower. |
| fig7f-tab2-ipsc-bsmf-lower | not_reproduced | Cell 91: IPSC bSMF 0.65 vs EPSC 0.51; inhibition is not lower. |
| tab2-btmf-currents-higher-than-spikes | not_reproduced | Cell 93: means are within tolerance and E ≈ I, but E vs spikes p = 0.057 and I vs spikes p = 0.16. Only D11 (a) was run. |
| tab2-event-rate-excitation-higher | not_reproduced | Cell 95: at 20 pA, E > I (p = 0.013), but both means (6.44 and 2.65 Hz) are outside tolerance; at 40 pA, no difference. |
| tab2-nonlinearity-ei | not_reproduced | Cell 97: E vs I threshold p = 0.26; the IPSC threshold (0.07) and transition (1.43) are outside tolerance. |
| tab2-fsi-ei | not_reproduced | Cell 99: I > E (p = 0.009), but both means are outside tolerance and IPSCs differ from all three current-clamp types. |
| tab2-latency-duration-ei-no-difference | partially_reproduced | Cell 101: the means are within tolerance, but latency differs under D10 (a) (p = 0.008); no difference under D10 (b) or in duration. |

## B. Problems

1. **[affects a conclusion]** `subfields` / `strf_from_events` (cells 26, 31): the cluster-mass test is the author's own assumption, not in the paper or the claims.
   - It halves the group behind every Table 1, Fig. 4 to 6 and Table 2 comparison: 15 neurons, where the paper has 30.
   - D7 (b) as the claims define it (a contiguous region of at least 2 pixels, shift significance, no cluster test) was never printed.
   - The assumption is statistically defensible. On a synthetic envelope, 4 of 4 random-event STRFs passed D7 (a) and D7 (b) without the cluster test, and were double-peaked under D9 (b); the cluster test passed 1 of 4. But it is not the paper's method.
2. **[affects a conclusion]** Cell 31: the shipped code's own significance rule (analytic p = 0.005, `significant_strf.m`) gives 29 neurons in the all-three group, the closest to the paper's 30. It was not carried into the Table 1 and Table 2 claims.
3. **[affects a conclusion]** Cell 55, fig5c: counts from n = 15 are graded against the paper's counts out of 30, so no count could match. Proportions, or a group of about 30, are needed.
4. **[affects a conclusion]** `strf_measures` `total_a` (D8 (a)): the bandwidth spans the lowest to the highest channel of the top two bands, including chance far-apart bands. Peak ratios of 5 to 15 (cell 37) and means of 1.4 octaves (cell 59, about 3 times the paper's) result. This bears on fig3e, fig3f, tab1-total-bandwidth, fig5df and fig7e.
5. **[affects a conclusion]** Cells 91, 93, 97: the voltage-clamp claims report only D11 (a) and D12 (a). `btmf_b`, `bsmf_b`, `theta_full` and `trans_full` are computed in `add_rtf_nl_fsi` but never printed, although the current-clamp claims ran all readings. tab2-btmf in particular could flip, since current-clamp D11 (b) changes the spike bTMF.
6. **[affects a conclusion]** `vc_events`: only the D3 "noise" baseline is used for voltage clamp. The `pre` s.d. is computed but not run, which matters for tab2-event-rate and fig7-unimodal. At 40 pA, no nonlinearity or FSI is computed.
7. **[affects a conclusion]** Many reading × group combinations are tried with no account of how many were tried. fig4c passes in 1 of 6, fig3f in 1 of 4, fsi in 1 of 2 groups.
8. **[affects a conclusion]** fig5a (cell 51): r ≈ 0 between CF and BF suggests a pipeline fault, which the notebook does not diagnose. One candidate: CF is taken from a single presentation at 0 dB SPL (threshold 0 dB in 64/66 neurons), where a responsive tone may be noise. Also, 5 of the 8 paired EPSC BFs sit at exactly 20.0 kHz (cell 85).
9. **[does not affect a conclusion]** `trf_summary`: D15 region reading (b) is identical to (a) by construction, because both the numerator and the denominator require a responsive tone. Cells 21, 23 and 25 print identical rows, so reading (b) was never actually tested.
10. **[does not affect a conclusion]** `tone_analysis`: the docstring says spikes are clipped with a median filter, but `median_filter` is imported and never used. Spiking tones are excluded anyway. The decay in cell 10 runs to 250 ms and can include later spikes, and neurons whose decay never reaches 10% are dropped silently.
11. **[does not affect a conclusion]** Cell 17: D14 reading (a) is not run as the amplitude reference. The claim already reproduces under reading (b).
12. **[does not affect a conclusion]** Cell 103: the one Supplementary Fig. 2 pair present (17921004 vs 17921007), and the one neuron's BF, latency and bandwidth at the three levels, could have been reported as the criteria ask. The outcome stays blocked.
13. **[does not affect a conclusion]** Cell 29: the D3 `pre` reading keeps a median of 0 to 1 non-spiking events per neuron, so that reading is degenerate. The pre-stimulus segment was not inspected.
14. **[does not affect a conclusion]** Claims-file reading: D2 (b) describes peakfinder's output as an "amplitude above the neighbouring minimum". Peakfinder returns the peak magnitude, which is what `proc` uses; the 3 mV is the selectivity, not the amplitude.
15. **[does not affect a conclusion]** `strf_measures`: the kHz width `(faxis[hi]-faxis[lo])` omits the +1 channel that the octave width includes. A band 1 channel wide would give an infinite Q. None occurred here, since the means are finite.

The helpers checked out on synthetic inputs: `peakfinder`, the STRF (correct pixel and BF recovered), `rtf_best_mod` (10 Hz and 0.93 cyc/oct for a 10 Hz, 1 cyc/oct Gabor), `spike_cut_gap` and `bimodal_trough`.

## C. What I could not check

- **The archive contents behind the blocked claims.** The archive lists only `data.tar.gz` and `codes.tar.gz`; `filelist.txt` has no inner listing. So I cannot confirm from the archive that the supplementary folders hold only the 2 and 3 files seen in cell 103. A printed listing of the tar members under `Supplementary/` would settle it.
- **The ports of the Matlab code.** I could not compare against the originals: `ringach_malone_func.m` (the `sqrt(2)` in the exponent), `calculate_whole_cell_fsi.m`, the `.spr` scaling (`*MDB + MDB/2`) or the downsampled-envelope choice. The instructions file names the full-resolution `.spr`, not the downsampled one. Printing the relevant Matlab lines would have let me check.
- **Whether the tone-order frequency column is right.** Its level column is validated by the loud vs quiet check. Printing one TRF matrix (frequency × level) with its CF, and a CF vs loud-level best frequency correlation, would have shown whether the fig5a failure lies in the CF.
- **Spike detection.** Per-neuron spike cut values and amplitude histograms, with the number of spikes per neuron, would have let me check D1.
- **Missing outputs.** Group counts for D7 (b) without the cluster test; the Table 1 measures for the analytic-significance group of 29; the voltage-clamp values under D11 (b) and D12 (b); and the D9 (a) double-peak counts and ratios without the cluster test.
