**A. Outcomes** (26 claims, from the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| data-sessions-and-trials | partially_reproduced | Cell 9 matches on cells (37), recording dates as animals (23), max trials (503), mean trials (160.3) and mean rate SD (6.48 Hz). It misses on kept sessions (115, needs 86±8.6) and fewest trials (69, needs 98±9.8). The 132 recorded is matched only by "Gaussian AM stimuli, any cutoff" (122), not by the seven protocols (116). |
| table1-sessions-per-protocol | not_reproduced | Cell 11: 0 of 7 counts within tolerance under every reading (kept (a): 60/9/8/10/11/8/9 against 43/6/7/7/8/7/8). |
| firing-rate-uniform | reproduced | Cell 13: mean 110.2 Hz (SD 16.7), ANOVA F=0.49, p=0.82 (kept (a)). Every reading is within tolerance and not significant. |
| threshold-population | blocked (data_missing) | Confirmed against the archive. The bucket holds only `crcns-ia1.zip`, the docs and the checksums. Data1 holds spikes, `_long.dat`, `cell.dat`, stimuli, `singlecells.txt` and an unopened `firing_rates`, with no f-I or threshold file. The README says the f-I files (`_fi.dat`) exist only for Data2, which is unpublished and comes from other cells. |
| table1-bursting-sessions | not_reproduced | Cell 17: at most 2 of 7 within tolerance under any combination. Main reading gives 52/60, 2/9, 8/8, 9/10, 10/11, 3/8, 0/9. The fractions are close to the paper's except for 3 dB. |
| table1-isolated-spikes | not_reproduced | Cell 19: at most 4 of 7 within tolerance (baa: 79.5, 77.7, 67.7, 78.1, 73.5, 95.0, 100). n=1 is most probable in every protocol only under some readings. |
| table1-burst-length | not_reproduced | Cell 21: at most 7 of 19 within tolerance. The partial threshold is 10. |
| fig5-burst-probability-vs-stimulus | reproduced | Cell 23, main reading (baa), both session readings: P(n=1) is lowest at 100 Hz and 12 dB, and P2 and P3 are highest there. Under bba the lowest P(n=1) moves to 25 Hz. |
| fig3-correlation-shape | reproduced | Cell 25: the first-peak height rises with SD (3 dB 0.50 < 6 dB 1.14–2.35 < 12 dB 5.06). 3 dB, 400 and 800 Hz are not bursting. 25 Hz has several peaks; 100 and 200 Hz have one, but only at prominence 0.2. The width reading (FWHM) fails. |
| method-correlation-error | reproduced | Cell 27: 2.69% (SD 1.37) with sigma/N (a), the whole τ range and τ=0 excluded from the span. Reading (c) gives 2.67%. |
| model-matches-classification | blocked (data_missing) | s_TH is not held (as for threshold-population), and the criterion makes it a condition. |
| fig6-bursts-less-correlated | reproduced | Cell 30: the ratio is 1.99 (0.1 ms) or 2.13 (0.4 ms) with τ=0 excluded, within 2.89±1.49, and above 1 in all 84 sessions. Including τ=0 gives 1.31, out of tolerance. |
| fig7ab-information-per-burst-increases | partially_reproduced | Cell 34: the mean slope is within tolerance under all readings (2.14, 1.85, 1.71, 1.48). The slope is significant in 83/84 (a) or 82/84 (b) sessions, not every one. There are 84 bursting sessions against 59±5.9 cells. |
| fig7cd-occurrence-decreases | partially_reproduced | Cell 36: log2 slope −2.71 (SD 1.09), within tolerance. The slope is significantly negative in 83/84 or 81/84 sessions. |
| fig7ef-jitter-independent-of-n | reproduced | Cell 38, events (b) with test (b): 87.7% not significant (tolerance 72–88, so marginal) and mean slope 0.005 ms. Events (a) gives 91.6% (out of tolerance) and a median jitter of 0.058 ms, which is implausibly small. |
| fig7gh-information-rate | not_reproduced | Cell 40: slope −44.7 or −36.6 bits/s (tolerance −27 to 5) and n>1 fraction 36–39% (tolerance 42.3–51.7). |
| direct-method-comparison | partially_reproduced | Cell 42 (direct_8 against burst_0.4, kept): R=0.965, means 204/184 and difference 20.7 are within tolerance. The direct method is higher in only 94/115 sessions (82%, below 90%), and the loss is 10.1% (tolerance 12.6–15.4). |
| fig8-nbta-differ | partially_reproduced | Cell 46: the ANOVA is significant in 71/71 sessions. The time-domain count is 60 (any point) or 14 (most points), against 50±5, and there are 84 bursting sessions against 58. |
| fig8-latency-decreases | reproduced | Cell 48: 43/71 sessions decrease monotonically, and the mean τ_n goes 5.75, 4.13, 2.88, −0.55 ms. τ_4 is negative, see problem 2. |
| fig8e-sigma-minimum | not_reproduced | Cell 50: the mean SD of the minimum's position is 1.87–2.64 ms (tolerance up to 1.1). Times cutoff it is 0.32–0.43, against 0.05±0.005. |
| sigma-n-below-sta-sigma | reproduced | Cell 52, reading (a): 98.6% of sessions; ratio 1.60 (SD 0.28). Problem 4 applies. |
| fig9-nbta-not-concatenated-1bta | reproduced | Cell 54: 100% of sessions differ for n=2 under both ANOVA readings, the fraction does not grow up to n=4, and the STA gives the same. A test that rejects in every session tells little (problem 7). |
| fig9c-population-nbta | reproduced | Cell 56: height 3.22 < 7.11 < 8.60 dB and FWHM 5.1 < 5.5 < 7.15 ms, over 10 protocol-5 sessions (the paper has 7 cells). |
| fig10-burst-n-vs-height | not_reproduced | Cell 58: segregation holds in 9.5% (a) or 25% (b) of sessions, not in most. The n=0–3 variant (52–57%) is outside the criterion. |
| firing-rate-no-effect-on-limit | reproduced | Cell 60, reading (b): +50 Hz shifts the limiting ISI by −0.19 ms and the average n by +13.6%, both under the bounds. Reading (a) has no pairs, as only 100 and 90 Hz targets occur. |
| model-reproduces-coding-trends | blocked (data_missing) | It depends on model-matches-classification, which is blocked because s_TH is not in the data set. |

The paper states no chance level for any selection, so there was none to compare.

**B. Problems**

1. [affects a conclusion] Cells 7 and 9: session selection. 115 sessions are kept against the paper's 86, and this mismatch alone fails every count-based claim (table1-*, the 59 and 58 bursting counts, fig8 count). The notebook does not try the exclusions the data itself suggest:
   - the 28 offline-sorted sessions: 116 minus about 28 is close to 86, but their split by protocol is not shown;
   - sessions with fewer than 98 trials: the minimum here is 69, below both the paper's and the descriptor's 98;
   - the 450 ms-pause sessions;
   - the unopened Data1 file `firing_rates`.
2. [affects a conclusion] `ia1.central_peak` is called without `search` in cells 46, 48, 56 and 58, so the nBTA maximum is taken over −25 to +15 ms. τ_4 comes out negative (the maximum falls after burst onset) in most sessions in cell 48, which does not fit "latency". In cell 58 every burst with n ≥ 4 is then shifted forward in time before matching, which probably contributes to the fig10 failure. A τ < 0 search reading was not run.
3. [affects a conclusion] Cell 44: "at least two bursts of each n" is the author's own threshold and is not stated as an assumption. The n=4 nBTAs and σ_4 rest on 2 to 20 segments in many sessions (cell 46 counts). This inflates the spread of σ_n minimum positions (fig8e), shifts the fig8 central-peak counts, and biases min σ_n downward (problem 4). No sensitivity to a larger minimum is shown.
4. [affects a conclusion, possibly] Cell 52: the minimum over 800 time points of an SD estimated from few segments is biased low. That makes "min σ_n < min σ" (98.6%) and the 1.6 ratio partly a sample-size effect. Per-n ratios are not shown.
5. [does not affect a conclusion] `burst_limit`, peak reading (a): in the refractory plateau (lags shorter than the minimum ISI, 1 ms) C_s has no spike pairs and is near-constant. Small edge effects there create spurious "local maxima". On a synthetic bursty train (3 ms ISIs) reading (a) picked τ=0.4 ms and then found no significant minimum, while reading (b) found the true peak at 2.9 ms. So reading (a)'s 15/115 is an artefact of how it was coded, not a fair test of that reading. Counts are out of tolerance regardless, because of problem 1.
6. [does not affect a conclusion] Cells 32–42: I_n(1) is computed by plug-in, without bias correction, with 0.1 ms bins. For sparse events the estimate is close to log2(bins/events), so the rising I_n(1) slope (cell 34, about +2 bits) mirrors the falling occurrence slope (cell 36, −2.7 in log2). The burst code at 0.1 ms also exceeds the direct method (cell 42). The criterion fixes the method, so the outcomes stand, but the notebook has no shuffle control to show how much of the effect is bias.
7. [does not affect a conclusion] Cells 46 and 54: the two-way ANOVAs treat every segment-by-frequency value as independent, with thousands of segments. They reject in 100% of sessions, so they discriminate nothing. The criterion specifies them.
8. [does not affect a conclusion] Cell 58: the segregation counts are identical under both T readings (8, 21, 44, 48), even though 75/84 sessions match a different number of maxima. This is unexplained. Also, `peak_h` is an argmax over 41 centres that includes sparsely populated edge windows.
9. [does not affect a conclusion] Cell 25: the peak count depends on a prominence threshold the paper does not give. The described ordering holds only at 0.2; at 0.1, the 100 Hz session has two peaks.
10. [does not affect a conclusion] Cell 3: spike times reach 2.763 s, longer than one trial plus its pause (1.7 s). Some trial blocks may therefore lack a header, which would undercount trials and could explain the minimum of 69. This is not investigated.

Helper checks on synthetic inputs:
- `correlation` agrees with a brute-force C_s to machine precision.
- `nsb_entropy` gives 3.80, 3.97 and 4.00 bits for a uniform K=16 distribution at N = 20, 200 and 5000.
- `two_way_anova` matches statsmodels type-II p-values.
- `bursts_of_trial` groups spikes correctly.

I found no place where the claims file misreads the passages I checked (selection paragraph, Figure 9B legend, Eq. 14 and the ANOVA description).

**C. Could not check, and the output that would settle it**

- Whether the paper's 86 sessions are recoverable. Needed: protocol counts with offline-sorted sessions excluded, with sessions under 98 trials excluded, and with both; the content of `firing_rates`.
- Trial parsing. Needed: the maximum spike time per trial block and the number of blocks with spikes after 1.7 s, per session.
- τ_n and the fig10 and fig8 results with the maximum searched over τ < 0 only.
- The fig8e, sigma-n and fig8 results with a larger minimum number of bursts per n (for example 20 or 50), and per-n σ ratios.
- A shuffle or trial-permutation baseline for I_n(1) and I'_n.
- The reason the fig10 counts are identical under both T readings: per-session `a` and `b` flags for both T side by side.
- Reading (a) of the burst test with the refractory plateau excluded, for example starting the peak search at the first lag where C_s exceeds its plateau value.
