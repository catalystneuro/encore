I wrote `claims/000289/10.1073-pnas.2210622120.yaml` with 13 claims, but this paper reports no experiments, so the dataset can bear on only one of them, and that one is a prediction the paper never tests. The quote checker passes with 0 problems.

**Text read.** I read the version of record from Europe PMC (PMC9992764): main text, Methods and figure legends, plus the SI Appendix PDF (sections 1 to 6, Figs. S1 to S5). Nothing the claims needed was missing from the text. The preprint v1 is also in `paper/`, but I did not use it.

**Code read.** The paper's code is on Zenodo (10.5281/zenodo.7615975, BayesianRingAttractor v1.0, commit a9db6f9). It holds the filters, the network simulations, one notebook per figure, and the processed simulation outputs the figures are drawn from. It holds no imaging analysis and no connectome query.

**Paper and dataset don't match.** The paper is a theory paper: a circular Kalman filter and a Bayesian ring attractor, tested only in simulation and against the hemibrain connectome. It reports no imaging, behaviour or stimulus data. The dataset's description says it holds the data of a different paper, "Uncertainty and learning in a biological ring attractor" (Basnak et al., in preparation). It links bioRxiv v4 of this paper, but v4's abstract matches the published version and also has no experiments. So this paper cannot be reproduced on this dataset.

**Claims.**
- 13 claims, all with quotes. None has statistics, because the paper reports no tests.
- 1 claim has an `expected` value: retuning reduces the noise-induced accuracy drop by 35% (± 3.5).
- All 13 have criteria.
- 11 are simulation results and 1 is the connectome result (hemibrain v1.2.1 via neuPrint). These 12 are marked as using data held elsewhere. The simulation claims are judged on the paper's own processed outputs, and a rerun of its scripts is shown as a variant.
- 1 claim uses the dataset: the Discussion's prediction that bump amplitude is higher when external cues are reliable.

**Details the paper leaves open, and the readings named:**
- **"Same", "close", "indistinguishable", "mostly"** (Figs. 2I, 3C, 4G and S2): absolute accuracy or weight differences within 0.01 or 0.02 (0.02 or 0.05 for the update weights).
- **Which reliabilities count as "reliable"** (Fig. 2I): information rate of at least 1/s, or at least 3/s.
- **"Similar" and "accurately tracks"** (Fig. 2H): the network's distance from the filter is smaller than the filter's own error, and the correlation between amplitude and the filter's certainty is at least 0.9. These are run at the code's cue strength (15) and at the Methods' 10/s.
- **Fig. 3F normalization:** the code divides by the particle-filter reference, while the legend says the noise-free network; both are run.
- **Noise range for "below 70%":** noise SD up to 10 (plotted) or up to 20 (simulated).
- **Noise level for the 35%:** noise SD 10, noise SD 20, or the mean over 1 to 10.
- **Neuron sorting in Fig. 4B:** by protocerebral bridge glomerulus, or by ellipsoid body or gall position.
- **The prediction claim:** the paper fixes only the measure (the population-vector amplitude of the EPG bump). Open are how reliability is set in an experiment, the activity signal (ΔF/F or raw fluorescence minus baseline) and the test (majority of flies, or a one-sided Wilcoxon test across flies). Its second half, that high amplitude makes the bump less sensitive to new cues, has no measure in the paper and is not tested.

**Where the code and the paper differ:**
- The code runs 10,000 trajectories per setting where the Methods say 5,000.
- The Fig. 4G script uses a time step of 0.001 where the Methods say 0.01 for all simulations.
- Fig. 2H uses an information rate of 15 where the Methods say 10/s.
- The curve labelled "Bayesian ring attractor" in Figs. 2I, 3B, 3C and 4G is the filter's quadratic approximation, not a finite network simulation.
- The scan scripts pass the keyword `kappa_y` to functions that take `kappa_v`, so a rerun needs that renamed.

**Missing from the paper:** any experimental method or data for the prediction claim, which is the only point of contact with this dataset.
