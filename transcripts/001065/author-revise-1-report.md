I've finished the revision for round 1. The entry re-ran cleanly with `python tools/entry.py all` (0 check errors, notebook ran in 872 s). Every conclusion in the notebook, the README and the attempt record matches the new numbers. Nothing is committed or pushed.

**Outcome changes**
- **species-no-effect: not_reproduced → reproduced.** The verifier was right that the four-way model is rank deficient: only 14 of 16 design columns are independent under reading (a), and 29 of 56 under reading (b). It has empty cells, for example no M. mulatta cell from acute MCx slices. statsmodels' type II table on that design gives spurious species effects. I recomputed the type II tests from nested least-squares fits, which stay valid on such a design and match statsmodels on a full-rank one (checked on synthetic data). With that, no feature has a species effect at BH-corrected p < 0.05 under either reading, and an additive model agrees.
- **fig5c-basal-apical-features: partially_reproduced → reproduced.** This is the one claim where the verifier disagreed with me. Its point holds: the criterion's rule is the four corrected tests, and the Cohen's d values are reported but don't decide the outcome.
- **fig3e-classifier-accuracy: reproduced → partially_reproduced.** Fixing the broken input-resistance values pushed the 50%-held-out score to 78.3%, below the 79.11 bound, under every reading and both split rules. It no longer rests on the assumption that splits were stratified.
- All other outcomes are unchanged.

**Fixes and added output**
- **Broken input resistance (problems 2 and 3):** a new check drops hyperpolarizing sweeps that don't hyperpolarize, start above −40 mV, or exceed −20 mV in the step (13 sweeps in 10 cells). Without it, 3 cells had negative steady-state resistance. Input resistance now agrees with the paper's table at Pearson r 0.993 (max) and 0.990 (steady state). A chirp check drops one cell's profile, which has no 3 dB cutoff after its maximum.
- **Table-value variants (section C):** I ran the same tests on the paper's own table values for the same cells.
  - fig4a, fig4-interaction-small and figs6b-mcx-higher-rheobase fail there too.
  - So those failures come from the cells in the dataset, not from my feature extraction.
- **Smoothing spline (problem 4):** the oscillation claims now use the smoothing spline the criterion names, fitted per sweep and, as a second reading, per cell and 5 mV bin. The outcomes hold. One new caution: the spline's peak sits at the 3 Hz band edge in 52% of sweeps, so the FFT frequency result may reflect low-frequency power.
- **fig6j:** two other spike-width definitions, including the Allen Institute's IPFX width (the code's pickle uses IPFX names, and this width agrees best with its per-step ratios). Neither reproduces the claim.
- **Smaller items:**
  - an additive-model variant for the CV and blocker claims;
  - the drug column's value counts, plus a search of the files: none of the 51 blocker cells mentions a drug, so wash-in can't be placed;
  - the five cells with commands above 4 nA are listed;
  - the RawFeatureWide.csv columns are printed (no per-layer lengths, so fig5b stays blocked);
  - the mulatta count by the table's species (8, outside tolerance) is reported.
- **Record and README:**
  - Round 1 is recorded under `verifications` for all 42 claims.
  - The findings are updated, including a new one on the unmarked bad sweeps.
  - The README table now shows the new outcomes.

**Not done, and why**
- **Blocked reason for data-elsewhere claims:** the verifier gave `data_missing` for the six claims whose data are in SRA or NeMO, and for fig5b. I kept `blocked_by: other`, because the protocol forbids `data_missing` for public data held elsewhere. The disagreement is recorded.
- **No new reader questions:** the verifier reported no place where the claims file misreads the paper, so I added nothing to `questions/001065.yaml`.
- **Problems 6, 9, 10 and 11:** no change. These are stated choices that don't affect any conclusion, or, for the classifier preprocessing leak, they match the paper's procedure.
- **Unrelated file:** `tools/build_site.py` was already modified before this run. I didn't touch it.
