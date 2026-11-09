No outcome changed. Five claims the verifier disputed stay **reproduced**, now on fits that converge, and the disagreement is recorded for each. Every notebook ran and the entry check passes with 0 errors. One part of the run did not go as asked: the single `python tools/entry.py all` call was killed at the 2-hour command limit while it was on the fourth notebook (details at the end).

**Why the OFF fits failed for the verifier.** The posterior of these models has a second, much worse peak, with a log posterior about 240 lower. Chains started at PyMC's default point, as the paper's code starts them, can get stuck there. Whether they do varies from machine to machine, which is why the verifier's numbers differed from mine. I now start every chain at the best of nine optimizer runs (a sampler setting the paper doesn't specify). With that start:
- Every fit converges, including the Methods' priors on k and k2, which didn't before. The "assumed" flag is removed from the eight OFF claims (fig2g, fig2h, fig2d, figs1 ×2, recovery-timing, tables3, fig1c-withdrawal-locked).
- Every model is fitted to both trial sets, with and without pinches, and both give the same outcomes. Without pinches, the model scores (ELPDs) match the paper's notebooks to within one unit, so the paper used that set.

**Outcomes kept against the verifier:**
- **fig2h:** the linear+exponential model beats the double exponential by 5.08 (dse 3.56), and by 2.64 without pinches (paper 2.4).
- **figs1-completion:** OFF reaches 90% at 0.072 s, and the ON and OFF intervals don't overlap.
- **recovery-timing:** OFF recovers 50% by 19.3 s and 90% by 83.6 s, both inside the paper's intervals.
- **tables3 and fig1c-withdrawal-locked:** the withdrawal and heat-aligned OFF slopes (k 2.731 against 1.742) are now compared on the same trial set, and their intervals don't overlap.

**Other points I acted on:**
- **GP settings (point 4):** the Methods' 200 inducing points and p_noise 0.001 now run in a new notebook, `gp_methods.ipynb`, as a variant. It has 2500 iterations, not the 10000 asked for: 10000 would take about 92 min, over the 60-min notebook limit. Under these settings, training-R2 "no difference" still fails, and the test-group OFF–NEUTRAL pair just misses (p 0.054).
- **Support for the code's GP settings:** matched cell by cell to the paper's stored fits, the fits here agree closely (Spearman r 0.95 to 1.00), and the stored fits use p_noise 0.01. So the code's settings appear to be the ones behind the paper's results.
- **Null-model likelihood (point 5):** confirmed from the code that the null model's contamination range differs from the periodic model's. The "same likelihood" version is now a variant; the record notes the two places where it would change a test.
- **Smaller points:**
  - the NEUTRAL peak search now uses the ON peak, with a fixed label;
  - fig6c has variants with and without the zero-frequency bin and with cleaned EKG beats;
  - fig6d has a cleaned-beat spectrum and the supplement's bootstrap over animals;
  - the 30 s gap before a withdrawal is now run as the criterion says;
  - the erf model is refitted with target_accept 0.95;
  - figs2 has a test with one point per file and trial;
  - the record notes the weak heat-aligned test in figs3.
- **Questions for a reader** (`questions/001708.yaml`): the fig3bc FFT resolution and whether the paper's FWHM can come from the described method, and the fig6d "highest peak" rule, which is decided by peaks near the record length.
- **Record:** the round 1 verification is under `verifications`, with all 34 claims and the verifier's reasons quoted. Findings and notes are updated, with new findings on the chain starts and the null model's likelihood. README and `entry.yaml` are updated too.

**What I did not do:**
- **The full re-run, as one command.** `entry.py all` passed its check, then ran evoked (27 min), ongoing (27 min) and gp (35 min) before it was killed during `gp_methods.ipynb`. I ran that notebook on its own with nbconvert in the same environment the tool had built, after cutting it from 5000 to 2500 iterations to fit the time left (27.6 min). Every number in the record comes from these executed copies.
- **The 10000-iteration GP fit**, for the time limit above.
- **Verifier's time:** the notebooks now take about two hours in total, so the verifier's run, which re-executes them first, will have less time for its review.

Nothing is committed.
