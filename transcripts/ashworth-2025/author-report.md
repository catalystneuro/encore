The attempt is complete: all 34 claims were tested and none is blocked. The three notebooks pass `entry.py all` from a clean, locked environment, the check reports 0 errors, and the handover is built in `executed/001708-ashworth-2025/handover/`. Nothing is committed.

**1. Outcomes** (dataset DANDI:001708 version 0.260604.1023, the version the paper cites and the only published one)

| claim | outcome |
|---|---|
| dataset-composition, fig1c-psth-counts, fig2-trial-counts, figs8-null-model-worse, fig2g-on-double-exponential, fig2c-on-time-constants, methods-withdrawal-latency, methods-heart-rate, ongoing-cell-counts, fig3e-cv-isi | reproduced |
| fig2g-switch-times, fig2h-off-linear-exponential, fig2d-off-parameters, figs1-departure-timing, figs1-completion-asymmetry, recovery-timing, tables3-s7-withdrawal-steeper, fig1c-withdrawal-locked, fig3d-neutral-psd | reproduced, resting on an assumption |
| fig5b-train-r2, fig5b-test-r2, fig5b-test-group-differences, table1-hyperparameters, fig5c-dispersion, table1-latent-variance-order, fig5d-phase-profiles, figs2-phase-latency | reproduced, resting on an assumption |
| figs3-neutral-unmodulated, fig3bc-psd-peaks, fig4-nlml-minima, fig6c-coherence-counts | partially reproduced |
| tables9-s10-sigmoid-over-erf, fig6d-heart-rate-peaks | not reproduced |
| fig5b-train-no-difference | not reproduced, resting on an assumption |

Totals: 27 reproduced (17 of them resting on an assumption), 4 partially reproduced, 3 not reproduced.

**2. The dataset, assumptions and questions**

What the dataset holds:
- The cell and animal counts match the Methods exactly: 104 cells in 53 animals, and 62 in 30.
- The paper's trial counts and the CV/ISI table come out exact. The spectral peaks come out exact (286.86 s and 298.33 s), and the stored period-scan profiles match mine.

Findings:
- **NEUTRAL labels:** 4 NEUTRAL units are labelled "NEUT" and the other 32 "Neutral". The paper's code selects by the exact name "Neutral", which is where its n = 32 comes from.
- **Pinches:** the code looks for events named "Keyboard" while its loader names pinches "keyboard", so pinches never exclude a trial.
- **EKG:** 20,546 of about 1.1 M inter-beat intervals are under 50 ms (likely double detections), and 11 evoked files have no EKG.
- **Pinch labels:** values such as "ignore" are not described anywhere.
- **Table S11:** its animal counts (35, 18, 50) disagree with the dataset's 35, 18, 30.
- **Buffer:** 4 ON cells have a 226 to 229 s buffer before their ongoing segment, under the Methods' 230 s.

Assumptions:
- **OFF priors:** I used the code's priors on log k and log k2. The Methods' priors, read on k and k2, do not converge (r̂ 1.69).
- **Heat-aligned OFF fit:** judged on a run with target_accept 0.95. At the code's 0.8 the chains disagree (r̂ 1.74).
- **GP settings:** the code's 100 inducing points, p_noise 0.01 and 5000 iterations (the length of its saved runs). The Methods' 200 inducing points and p_noise 0.001 would take about 90 min, over the 60-min limit, so they were not run.
- **fig3d:** a prominence threshold for "local maxima above 10 Hz". The result holds at 10% and 20% and fails at 5%.

Questions for the paper's authors (recorded as findings): which OFF prior was used; how the FWHMs (16.92 and 16.12 s) were measured and converted to seconds, since no reading gives them; and which GP settings produced the reported results.

Question for a reader (`questions/001708.yaml`): should figs3-neutral-unmodulated use the 32 ongoing-set NEUTRAL cells instead of all 36? Only the 32 match the paper's counts.

**3. Where the protocol was unclear or missing something**
1. It does not say what to do when the criterion's main reading is too large to run but a variant fits the limit. I ran the code's GP settings, marked the outcomes assumed, and gave the estimate for the Methods' settings.
2. With a 65-min run there was no time to re-run after writing conclusions. I inserted the markdown-only "Result" and Summary cells into both the source and executed notebooks after the run.
3. There is no rule for MCMC fits that do not converge. I used a sampler-setting variant, stated as an assumption.
4. "Compare identity, not spelling" conflicts with a paper whose code selects by spelling. I applied the rule (36 cells), showed the paper's 32 as a variant, and asked a reader.
5. It is unclear whether the code's stored outputs (the scan file and the fitted-parameter table) count as `inputs`. I listed them as inputs at the commit, used only as reference values.
6. There is no guidance on platform-specific packages. CPU-only torch needed a direct wheel URL, and numpy had to be pinned below 2.4 for numba.

**4. Runtime and failures**
- The full run took 65 min: evoked 12, ongoing 23, GP 29.
- Two things failed in development and were fixed before the final run: float32 GP fits were not positive definite, and the first lock failed on numba with numpy 2.5.
- The final run had no failures.
