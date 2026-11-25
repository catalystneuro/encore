I've revised the attempt for round 2. The entry was re-run with `entry.py all`: both notebooks pass (decoding 43 min, features 55 min), `entry.py check` reports 0 errors, and nothing is committed. No verified outcome changed. One change is proposed for round 3.

**Why the text didn't match the outputs.** The workflow re-runs the entry on whatever machine it gets, and the ICs were not determined by the data:
- **The ICA input.** The Methods divide each SVD component by its singular value. On the frames the SVD was fitted to, that leaves all 200 components with equal variance. Which 30 dimensions jadeR keeps was then set by rounding: the ratio of the 30th to the 31st eigenvalue is 1.00000000.
- **No convergence.** JADE was also cut off at 100 sweeps before it converged.
- **Not a one-off.** On this machine, changing only the linear-algebra kernels gave an unrelated set of ICs.

**The fix.**
- **Scaling from the paper's code.** The paper's code (`normalize_svd` in `#03_ica/#01_svd.ipynb`) does not divide by the singular values, so I followed it. The eigenvalue ratio is then 1.0188, and the ICs agree across kernel choices to within 4e-13.
- **Convergence.** JADE now runs to convergence, as jadeR does.
- **Pinned kernels.** numpy, scipy and torch are pinned to their AVX2 code in `pupilwf.py`.
- **Check.** The fresh run from a new download gave exactly the outputs of my development run.

I added the mismatch between the Methods and the code as a new `code_mismatch` finding, at the end of the list. A side effect: with the paper's VIF only 7 ICs can be kept where the paper keeps 10. This is stated in the notebooks and the record.

**Outcomes, all rewritten from the new run**
- **rest-decoding-above-null:** stays partially reproduced and seed sensitive, on a new basis.
  - Two of the 16 combinations under the epoch selection rule are above null. The stronger gives AUC 0.696 against 0.514 (p = 0.0014) and holds at 4 of 5 seeds; the other holds at 2 of 5.
  - Every model AUC is below 0.738, the bottom of the tolerance.
  - The every-frame runs are never above null over five seeds.
- **rest-loss-accuracy-vs-null:** not reproduced. 0 of 16 combinations have both a lower loss and a higher accuracy.
- **rest-needs-0-1-hz:** not reproduced. The cutoffs are now run in the combinations that are above null, as the verifier asked. The claim's pattern holds in 1 of the 4 combinations run at the cutoffs.
- **rest-ic-count-and-window:** kept as partially reproduced, with `proposed: not_reproduced`. 10 ICs are highest only in a tie with 7 ICs that are the same set, and 1.5 s is never highest. Round 3 will review this.
- **rest-vif-below-10:** not reproduced. The maxima are 21.55, 10.32 and 2.97; none is within 9.0 ± 0.9.
- **rest-shap-medial-anterior-first:** kept as not reproduced, and the verifier's disagreement is recorded. The notebook now prints the argument it asked for:
  - The best-matching IC has 0.266 of its weight in the medial anterior band against 0.494 in MOs, so no kept IC matches the description.
  - All its SHAP peaks sit at the window's last frame, flagged as edge peaks.
- **The 18 blocked claims** are unchanged.

**Other corrections**
- I recorded round 2 under `verifications`, quoting the verifier's reasons, with what I changed under `response`.
- The round's `findings` list is empty, because no finding is rated `critical`.
- I removed an unsupported sentence from the pupil finding and updated the numbers in two other findings.
- I updated the reasoning of the reader question on the epoch selection rule, which the verifier says still stands. The claims file is unchanged.
- The README, the summaries and the runtimes in `entry.yaml` match the new run.

**Not done**
- **All 25 mice and the fourth session per mouse:** not run, about three hours of streaming.
- **Every-frame samples without the epoch selection:** not run, about 10 minutes per fit.
- **Every-frame runs at the six cutoffs:** they would run only where an every-frame combination is above null, and none is.
- **Pinning on other processors:** I tested it only on this machine. The tests were changing the kernels here and a fresh run from a new download. I couldn't check that an AMD processor gives identical numbers.
- **A missing output tag:** the new notebook cell for the five-seed and cutoff checks has no `claim:` tag. Adding one would have meant another 100-minute run.
