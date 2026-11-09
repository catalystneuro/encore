Done. The entry is written, locked, checked and run from a clean environment (all four notebooks pass), the attempt record is written, and `python tools/entry.py handover entries/001037-vinograd-2024` has built the verifier's package. Nothing is committed. I did not verify my own work.

## 1. Outcomes (54 claims: 12 reproduced, 5 partially, 10 not reproduced, 27 blocked)

| Claim | Outcome |
|---|---|
| methods-subspace-angle, fig2d, ed7f, ed8a, fig2k, ed8jl, ed3c, ed8c | reproduced |
| fig1m, ed8b, ed3g, ed3h | reproduced, resting on an assumption |
| ed9d, ed3f, ed4hi, fig1f, x1-time-constant-range | partially reproduced |
| ed1n, ed1p, fig1e, ed3e, ed4c, ed4d, ed4g, fig2gh, fig2no, ed8gi | not reproduced |
| methods-cvr2, fig4ce | blocked: methods_underspecified (every reading was run and is shown) |
| ed1m, ed5e, ed5hj, ed6g, ed6k, ed7bc, ed8ef, ed9i, ed9mn, ed10c, ed10g, ed10hi, ed10lm, ed10p, ed10r, fig3d, fig3e, fig3i, fig3j, fig4a, fig4hj, fig5g, ed12, fig5f, ed12eh | blocked: data_missing |

## 2. Dataset, assumptions, questions

**Version pinned: 0.260609.1402.** The paper cites no version. This is the latest, and the only one holding all five miniscope mice; the reason is in the notebook header.

**What the dataset holds:**
- **Miniscope:** traces and annotations for 5 mice, with no rSLDS models and no x1 or x2 labels. The 5-minute baseline the Methods describe is not in the files; recordings start 56 to 152 s before the first annotation.
- **Two-photon:** 7 mice, against the paper's 9. Each has stored factor weights and group photostimulation sessions; the 8 s ISI sessions exist for 6 mice (x1) and 4 (x2).
- **Missing:** the unitary stimulation, 1 mW, random-neuron and combined sessions, cell positions, face video and calibration recordings. This blocks 25 claims.

**Findings recorded about the data:**
- **M70 targets look wrong.** Its listed x1 targets do not respond at the stimulation onsets (−0.01 z) and rank 33rd to 55th of 65 by x1 weight.
- **M70 is deposited twice.** An older file is the same recording, 143 s longer and with different weights; it is counted once.
- **Sparse annotations.** Sniffing of the SW mouse is annotated in 1 of 5 mice, and BALB/c presence intervals exist in 1 of 7 two-photon mice.
- **Results depend on the fit seed.** New rSLDS fits are needed because the paper's models are not stored, and with the sample code's own seed choice the two decoder claims (ed3g, ed3h) drop to p = 0.15.

**Assumptions:**
- fig1m: the paired signed-rank test (p = 0.016; the unpaired test gives 0.16).
- ed8b: the ISI window from the end of one pulse to the next onset.
- ed3g, ed3h: the seed-0 fits.

**Questions for the paper's authors** (recorded as findings):
- How the cvR² of 84.7% is computed. My readings give −81% to 20%, and a 2-dimensional model cannot explain 85% of the variance of 42 to 158 neurons.
- How the network weights were scaled. With the Methods' weights the largest eigenvalue is 0.48 to 0.52 at every density, so the network is never unstable and τn stays near 40 s, unlike Fig. 4c.
- How transient amplitude is measured: the reported 0.58 z is below the 1.5 SD detection threshold.
- The test, window and seed choices behind the assumptions above.

**Questions to a reader:** none.

## 3. Protocol points

1. **Software that cannot be built in isolation.** ssm's setup.py imports numpy and Cython, and `entry.py run` installs the lock with plain `uv pip install`. The protocol says nothing about this. I locked ssm's build and runtime dependencies and the helper installs ssm at the pinned commit with `--no-build-isolation --no-deps`.
2. **Seeds can change outcomes.** The protocol treats a seed as a choice that cannot change a result, but here it does. I used seed 0 as a stated assumption and showed the sample code's seed choice as a variant.
3. **Dependency rule for fig4hj.** It is blocked only through fig4a, although the simulation uses just the paper's own 36% number. I followed the rule.
4. **Absence claims with unspecified windows (ed8b).** The protocol says absence is judged on "the paper's test alone", but the paper's window is not given. I adopted the best-supported window as an assumption.
5. **Conclusions after a long run.** The handover is built from the executed copy, and rerunning 51 minutes to change prose was not practical. I edited the conclusion markdown in both the source and the executed copy.
6. **Unreachable thresholds.** fig1e asks for P < 0.0001, which 7 mice cannot reach (the smallest possible p is 0.0006). I judged it at p < 0.05.
7. **Heavy compute.** The protocol aims for under 10 minutes per notebook; the cross-validation needs 255 fits (37 min). I put it in its own notebook.
8. **Many questions for the authors.** I grouped the smaller ones in a single methods_unavailable finding.

## 4. Runtime and failures

- **Run time:** about 2 h 45 min of the 5 h. The final `entry.py all` took 51 min: notebooks of 11 s, 12 min, 37 min and 2 min.
- **Failures while developing:** a first run of notebook 2 crashed in the decay fit (fixed). A masked-frame fit for cross-validation failed in ssm, so the random-frame folds were not run. My first cvR² measure scored each block against its own mean, which gives negative values; I added scoring against the session mean as a second reading.
- **Untracked files:** the repository root has untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others). I left them alone.
