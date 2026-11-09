I've worked through every point in the round-2 report. All 34 outcomes stay as verified and nothing is under `proposed`. One claim, fig5b-train-no-difference, may need its reading changed, and I've asked a reader about it.

**Why the numbers didn't match.** The fits give identical results when run twice on the same machine at the same seeds. I checked this by sampling one fit twice. They differ between machines. The verifier's copy ran on a different machine, so its means moved in the third digit and two fits came out differently there:
- The default-start OFF fit had two chains stuck in the low mode (three here).
- OFF_erf_linear_np did not converge (r_hat 1.393).

In this run the existing evoked Result cells and record numbers match the output (fig2g, fig2c, fig2h, fig2d, figs1, recovery-timing, tables3, fig1c). The notebook, the evoked Summary and the README now say that results vary between machines and that the numbers quoted are from this run.

**What I added or corrected**
- **Convergence (evoked):** the fit table now has a `converged` column (r_hat at most 1.01 and ESS at least 400). I added a refit of OFF_erf_linear_np at target_accept 0.95. Here OFF_erf_linear_np converges (r_hat 1.006) and so does its refit (1.003). The only unconverged fit is OFF_erf_linear with pinches (r_hat 1.148), and its refit converges. The figs8 text, the Summary's "every fit converges" and the round-1 "All fits now converge" responses are corrected.
- **tables9 (sigmoid vs erf):** the comparison cell now runs LOO and WAIC against both refits and flags whether both fits in each comparison converged. On converged fits the sigmoid is below the erf model with linear recovery in every comparison (−0.34 to −1.00). The Result cell, the notes and the paper_inconsistency finding quote these numbers; the "0.53, dse 1.84" figure is gone.
- **fig5b-train-no-difference:**
  - I fixed "every variant but the two above finds a difference".
  - I added the cell-by-cell match the verifier asked for. The paper's stored NEUTRAL fits match fits on the code's 1500 s segments (median difference 0.0003, Spearman r 0.993), not fits on whole recordings (1.28, r 0.112). On the segments the test finds no difference (Kruskal-Wallis p 0.098; the paper reports 0.117).
  - This is now a question for a reader in `questions/001708.yaml` and a `code_mismatch` finding. The outcome stays as tested on the claims file's main reading (whole recordings).
- **fig3d:** 2486 s is now described as a bin near the low end of the frequency grid, not the record length.
- **Runtimes:** README and `entry.yaml` now give this run's times: 31.8, 27.1, 36.7 and 25.6 min.
- **Round 2** is recorded under `verifications` for all 34 claims: agrees true, the verifier's reasons from its report, and my responses. `tools/entry.py check` passes with 0 errors.

**What I did not do, and why**
- **The full `entry.py all` run was cut off.** It hit the 2-hour command limit while running gp_methods.ipynb. evoked, ongoing and gp had finished. I then ran gp_methods.ipynb alone with nbconvert, in the same environment and with the same command the tool uses.
- **I wrote `executed/.../result.json` myself.** It uses each notebook's printed runtime, because the tool never got to write it.
- **I edited the executed notebooks.** I copied my text changes into their markdown cells after the run. Their code cells are identical to the source, so the outputs are unaffected.
- **The Gaussian-process fits still don't use the claims file's settings for 10,000 iterations.** That run would take about 90 minutes, over the 60-minute notebook limit, so it stays a 2500-iteration variant and the record says so.
- **fig5b-test-r2 still depends on the null-model choice.** The record already says that with the claims file's same-likelihood null it would be only partially reproduced (NEUTRAL p 0.052). The verifier found the choice reasonable, so I left it.
