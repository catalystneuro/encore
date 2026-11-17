I've answered all four questions. Answers are in `questions/000054.yaml`, each marked `answered: 2026-10-22`, and the matching criteria in `claims/000054/` are updated. `claims_check.py` validates the file and every quote matches. It reports 4 problems, all the same `6e-05` p-values in edf9l that were already flagged in the file's last check: the checker doesn't recognise the legend's "6.0 × 10 −5" form. No statement or expected value changed, and nothing is committed.

1. **training-intermediate-fraction (use the figshare VR deposit?):** Yes. The Methods build priors from "previously seen" trials, and the paper names only DANDI, which holds just the imaged trials. The authors' figshare deposit (doi:10.6084/m9.figshare.31974756.v1) is public and pinned, so header M7 now names it as the source of the priors.
   - This claim and fig7 use nothing but the deposit, so I marked them `data: elsewhere` with the deposit as `where`, not `with_inputs` as the question proposed.
   - The other ten listed claims (fig6a, fig6bc, fig6d, map-estimate-values, edf9, edf9k, edf9l, edf10, fig7g, edf3) also use the dataset's activity, so they are `data: with_inputs`.

2. **fig7-model-reproduces-remapping (scale and noise):** The model uses the code's scale, which is the Methods' scale in other units, so both describe one model.
   - The Methods' "σ² = 4.11" is really the width σ: 0.15 units = 4.11 f_h, so the denominator is 16.9 f_h².
   - The input centres run from -0.1 to 1.1 units (5.5 to 38.5 f_h).
   - The model is trained and tested with stimulus noise, output noise and weight noise, as the code does. That settles the weight-noise question in favour of reading (a).
   - The criterion wrongly put the test stimuli on the M6 grid. In the code they are 1,000 evenly spaced S from -0.3 to 1.3. The criterion is rewritten with all of this.

3. **edf4bc-overlap-cells-at-ends-and-reward (how the two peaks count):** The paper doesn't say; the figure and code only plot the peaks, with no measure. The criterion now names two readings: each environment's peaks counted separately, or cells with both peaks in the regions. Reference (b) is now taken per environment, so the S-tilde = 1 peaks are compared with the S-tilde = 1 place cells.

4. **edf3-simulated-posterior-population (centre tiling and averaging):** The centres tile the M6 grid (0.06 to 43.9 f_h); the paper is vague, but the code fixes it. Yes, the difference is judged on the mean over the 1,000 simulations, each z-scored before averaging, as the Extended Data Fig. 3j legend says. Both points are now in the criterion.
