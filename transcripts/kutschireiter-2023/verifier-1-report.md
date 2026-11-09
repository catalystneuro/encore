**A. Outcomes** (13 claims, from the claims file)

| Claim | My outcome | Reason |
|---|---|---|
| fig1-conflict-decreases-certainty | reproduced | Cell 12: (a) and (b) hold in 6 of 6 cases (κ_t = 1, 2, 5; γ_z = 1 and 10/s). For example, at κ_t = 5 and γ_z = 1, the full step gives 5.039 (confirmatory) against 4.904 (no observation) against 4.768 (opposite). |
| fig2h-bump-tracks-circkf | reproduced | Cell 14: at rates 15 and 10, the network-to-circKF difference is 0.016 and 0.021 rad, against circKF error of 0.483 and 0.491. Correlation over cue periods is 0.994 and 0.993. In darkness the amplitude falls from 7.21 to 1.22 (rate 15) and from 5.89 to 1.21 (rate 10), ending closer to κ* = 1. |
| fig2i-accuracy-and-certainty-vs-reliability | reproduced | Cell 16: the largest accuracy difference is 0.0010 at rates ≥ 1/s and 0.0003 at ≥ 3/s, so all four combinations pass. At 0.01 to 0.1/s the attractor is less accurate (−0.073, −0.084, −0.057) and more certain (+0.82, +0.69, +0.49). |
| fig3b-bayesian-beats-conventional | reproduced | Cell 18: the optimal κ* is 1.7. The Bayesian attractor is more accurate at all 23 rates (smallest difference 0.0115) and strictly above from 0.1 to 10/s (smallest 0.034). The not-judged part fails: the smallest differences are at 0.01, 2 and 3/s, not at 0.01 and 0.03/s. |
| fig3c-update-weights | reproduced | Cell 20: the largest difference at ≥ 1/s is 0.0010 under reading (i) and 0.0062 under (ii), within both 0.02 and 0.05. Under both readings the largest difference is at 0.01/s. |
| fig3d-best-network-slow-decay | partially_reproduced | Cell 22: conditions 1, 2, 3 and 5 hold (best network κ* = 0.7, β = 0.3; the Bayesian attractor is 0.57% below it). Condition 4 fails: the maximum over κ* rises twice for β above the best (0.7→0.8 by +0.0008, 0.9→1 by +0.0014). Overall Spearman ρ is −0.98. |
| fig3f-noise-drop-below-70 | reproduced | Cell 24: untuned performance is 63.1% at SD 10 and 38.1% at SD 20 under both normalizations, all below 70%. |
| fig3f-retuning-reduces-drop | reproduced | Cell 26: 3 of 6 readings fall in 31.5 to 38.5% (34.64 and 34.56 at SD 10; 31.67 for the pf-normalized mean over SD 1 to 10), so the value part holds. Retuned SNR is at least the untuned SNR at every SD > 0 (ratio 1.05 to 3.00). |
| noise-effects-on-mu-and-kappa | partially_reproduced | Cell 28: (1) holds (\|z\| ≤ 0.82 and the variance grows) and (3) holds (ratios 0.500 and 0.501). (2) fails in all four conditions: the mean end amplitude is 0.83, 0.65, 0.82 and 0.42, against about 1.00 without noise. The amplitude drifts down, not up (see B2). |
| fig4b-connectome-motifs | partially_reproduced | Cell 30, reading (a): the offsets have opposite signs (left +0.56, right −0.48 on the same side), and all 42 Delta7 reach more than 8 EPG glomeruli for both input and output at ≥ 1 synapse. Reading (b), which the criterion requires, cannot be formed because no instance name holds an EB or gall position (cell 6). |
| fig4gh-drosophila-network-matches | partially_reproduced | Cell 32: the largest difference is 0.019. Reading (b) (0.02) holds; reading (a) (0.01) fails at 0.1, 0.2 and 0.3/s. The criterion needs both. |
| figs2-performance-independent-of-n | not_reproduced | Cell 34: N = 16 at 0.1/s deviates by 0.041, so both readings (N ≥ 8 and N ≥ 16, within 0.02) fail. That is the only cell above 0.02; N = 3 and 4 stay within 0.0186. |
| prediction-bump-amplitude-cue-reliability | blocked (methods_underspecified) | Cell 37: three combinations show higher amplitude with the high-contrast cue: dF/F with reading (a), 10 of 15 flies; raw signal with (a), 12 of 15; raw signal with (b), Wilcoxon p = 0.021. The fourth, dF/F with (b), does not (p = 0.138). The criterion says to mark the claim blocked when the readings differ. I recomputed both p-values from the printed table and got the same results. |

**B. Problems**

1. [affects a conclusion] Claims file, noise-effects criterion (2), run as specified in cell 28. SI §5 (Eqs. S107–S109) derives the noise's direct effect on the first Fourier mode and leaves the remaining dynamics ("···") unchanged. The criterion instead compares full-network `RNN_filter_Run` amplitude against a noise-free run. In the full network, noise in every mode raises the rectified global inhibition (`w_quad·π/N·Σmax(r,0)`), and the notebook's output shows a net downward drift. The failure of (2) may come from how the criterion turns the claim into a test, not from the paper's derivation. The notebook does not separate the two effects. I am reporting this, not correcting it.
2. [affects a conclusion] Cells 32 and 34, fig4gh and figs2. The 0.01 and 0.02 bounds are close to the run-to-run variability in the paper's own outputs. The same Bayesian attractor gives 0.2159 at 0.1/s in figure2i.npz and 0.1943 in figure4g.npz, a gap of 0.022 (partly from dt 0.01 against 0.001). Both fig4gh reading (a) and the figs2 failure (one cell, N = 16 at 0.1/s) sit at that rate. The notebook gives no Monte Carlo SE, so these outcomes rest on the claims file's bounds, not on a detectable effect.
3. [affects a conclusion] Cell 22, fig3d condition 4. The two rises (+0.0008 and +0.0014) are probably sampling noise, but the criterion gives no tolerance, so the claim stays partial.
4. [does not affect a conclusion] Cell 30, fig4b. The Delta7 breadth result depends on the synapse threshold: more than 8 output glomeruli in 42 of 42 at ≥ 1 synapse, 7 of 42 at ≥ 3, 0 of 42 at ≥ 5. The criterion sets no threshold, so ≥ 1 is its literal reading, but the result is fragile. The connectome is the public v1.2 export, not v1.2.1 as in the paper; this is stated in the notebook.
5. [does not affect a conclusion] `raw_signal` and `raw_roi_fluorescence`, cells 36–37. Several raw-signal details are the author's own choices: plane-mean projection, 4-px Gaussian smoothing picked by fit to the stored dF/F, a 10th-percentile baseline, and a 10% frame subsample. Only one variant is run. The prediction outcome is blocked whatever these choices are, because the dF/F readings (a) and (b) already disagree.
6. [does not affect a conclusion] `bra.fourier`. A synthetic test shows it returns phase −θ for a bump at θ, with the amplitude correct. It also fixes k = 2 across 37 to 47 ROIs without checking that the ROIs span exactly two periods. This is consistent within a fly, so contrast comparisons are unaffected.
7. [does not affect a conclusion] Cell 12. Comparison (a) holds by construction for any 0 < α < 2κ, so it is a weak test, although it follows the criterion.
8. [does not affect a conclusion] Cell 34. One NaN cell for N = 128 is silently skipped by `nanmax`, and its rate is not printed.
9. [does not affect a conclusion] Cell 0 says "No claim is blocked". Under the claims file's own rule, the prediction claim is blocked (methods_underspecified).
10. [does not affect a conclusion] Cell 24. Retuned performance is a maximum over noisy grid cells, which biases it upward. The paper's notebook does the same.

**C. What I could not check**

- The Zenodo sources:
  - that `kappa_z = 15` in Figure2h.ipynb is γ_z;
  - the column meaning of `noUncert_stats`;
  - the axis assignment of `KAPPA_FIXED`, `KSTAR_3D`, `BETA_GRID` and `KSTAR_3F` to the npz arrays.

  Printing the defining source lines of the figure notebooks would have settled these.
- The hemibrain export and the NWB contents beyond what the notebook prints. On the archive side I confirmed 221 assets and 66 subjects for version 0.240801.1040.

Outputs that would have helped:

- Per-rate Monte Carlo SE of \|m1\| (for problems 2 and 3).
- For the noise claim, the zero-mode and global inhibition over time, or a run with inhibition held at its noise-free level (problem 1).
- The rate of the N = 128 NaN cell.
- Raw-signal results under other smoothing and baseline choices.
