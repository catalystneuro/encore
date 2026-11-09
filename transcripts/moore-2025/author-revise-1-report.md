I've revised the entry for round 1 and re-run it. `python tools/entry.py all` passes: 0 check errors, and the notebook runs in 282 s. The record now has 14 reproduced, 8 partially reproduced, 4 not reproduced and 1 blocked. Nothing is committed.

**Outcome changes**

| Claim | Before | Now | Why |
|---|---|---|---|
| fig3g-adult-halves-correlation | partially | not reproduced | The verifier's rule: neither value is within tolerance (r = 0.804 and 0.748, both need ≥ 0.846). |
| figs2j-adult-epochs-correlation | partially | not reproduced | Same rule (r = 0.787 and 0.562). |
| fig2d-juvenile-isomap-wake-sharper | reproduced | not reproduced | Isomap is now fitted on every bin, as the criterion says, and p = 0.056. The old 3,000-bin fit raised one H3026 recording's median from 0.435 to 0.546. |
| fig2h-juvenile-isomap-rem-sharper | not reproduced | reproduced | p = 0.045 after the fixes, at the threshold. All its variants are above 0.05. |

- **fig1g:** the verifier said not reproduced. I applied its rule, but with the fixed code the wild-type r is 0.815, just inside the 0.81 bound, so one of two values holds and it stays partially reproduced. The record gives this reason for round 2 to review.
- **Fragile results:** fig1h stays reproduced at p = 0.035. Its variants (half-width below 120°, H3026 left out, archive labels) are no longer significant, and the conclusion says so.

**Fixes from the report**
- **Frame counts:** each tracking frame is now counted on its own window, so speed filtering no longer loses spikes. A synthetic test in the data check fails on the old code (2,864 wrong frames).
- **Session length:** every session is cut to its first 20 min, the paper's length.
- **Decoder drift:** the error is unwrapped over valid bins before filling gaps. The 22-bin recording now has 279 bins, and leaving out recordings under 300 bins is shown as a variant.
- **REM:** the main analysis uses every REM interval, as the criterion says. The result with intervals inside exploration left out is a variant.
- **Seeds:** the Isomap eigensolvers are now seeded. The numbers did not change.
- **Corrected text:** the notebook now shows the archive's asset ages, including the negative ages of H3023 and H3026, and the text and finding about age are corrected.

**Outputs the verifier asked for**
- **H3026:** a variant with this rat left out for the juvenile tests.
- **Correlations:** Spearman r, first-day r and scatter plots that list the cells farthest from the diagonal. In fig1g five of those ten are from H3026, and with H3026 left out the Fmr1-/y r is within tolerance.
- **Drift bins:** decoded bin counts for every recording.
- **Positions:** each file has exactly one frame with y = 0, so it is an offset, not missing tracking.
- **Isomap:** the cells with the highest Isomap information, and the full fit beside the 3,000-bin fit. The identical adult maximum of 2.476 does not recur with the full fit.
- **Histology:** a per-file list of histology images. All 36 files hold them, including the four the verifier thought had none (it went by file names). figs1d stays blocked.

The record has a `verifications` round 1 with the verifier's outcome, reason and my response for all 27 claims. The README, summary and every conclusion match the final numbers, with no em dashes and no "rather".

**Not done**
- **Repeated cells (problem 2):** cells recorded on more than one day are still counted on each day, because the files give no probe depth per day. The first-day variant is shown.
- **H3026's genotype:** it cannot be confirmed from the archive.
- **Paper text:** I downloaded none, so `paper/` was not touched.
- **Stray files:** the untracked files at the repository root (`.bashrc`, `.idea`, `scripts` and others) are sandbox placeholders I did not create. The workflow should not commit them.
