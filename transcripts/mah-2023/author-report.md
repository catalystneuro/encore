I finished the blind repeat attempt on `mah-2023` against DANDI:001169 version 0.261120.1450. All 33 claims were tested and none is blocked. The entry passes its check, both notebooks ran from a clean environment, and the handover was built. I did not verify my own work, and nothing is committed.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| cohort-size, fig1e, fig1f, fig1i, suppfig2, suppfig3, suppfig12, suppfig14 | reproduced |
| fig2a, suppfig5, suppfig6, fig2c-d, fig2e, fig2f, fig2g-h, fig2j | reproduced |
| fig2k, fig2l | reproduced, but only when using the trials the paper's code uses |
| fig3c | reproduced, resting on an assumption |
| bayes-observer, suppfig9 | reproduced |
| fig3j | reproduced, resting on my model-fitting choices |
| suppfig8 | reproduced, resting on my model-fitting choices; depends on the random seed |
| fig3f | not reproduced, resting on my model-fitting choices; depends on the random seed |
| fig3i | partially reproduced, resting on an assumption |
| fig3l | reproduced under the Results' reading, resting on an assumption |
| fig4a | partially reproduced (tested on the paper's Zenodo deposit) |
| fig4c, fig4d | reproduced (tested on the Zenodo deposit) |
| fig5b, fig5c | reproduced under the code's session reading |
| fig5d | reproduced |
| pre-cue-session-link | partially reproduced (14 of 16 rats linked) |

Totals: 29 reproduced, 3 partially reproduced, 1 not reproduced.

### 2. What I found

**About the dataset**
- **Counts match the paper exactly:** 291 rats (184 male, 107 female), a median of 33,493 trials and 71 sessions per rat. No session is deposited twice.
- **Only included sessions are deposited, and nothing in the dandiset says so** (rated major). The trial counter jumps between consecutive sessions in 2,586 places, and the paper's Zenodo deposit has a median of 95 sessions per rat against 71 here. Figure 4 needs the excluded sessions, so I tested it on Zenodo `A_Structs_all` (doi:10.5281/zenodo.10031483). The paper should be listed on that Zenodo dataset as one of its datasets.
- **An undocumented task argument marks the pre-cue sessions.** `center_port_cue` is True only for the 16 rats of Figure 5. The claims file says nothing in the files marks these sessions, which is not the case.
- **The wait-time threshold includes timed-out catch trials.** It is computed with the 16,086 trials that ran to 100 s; the description does not say so.
- **An extra cohort.** 8 rats have catch probability 0.3, which the paper does not list. Two block transitions go straight between high and low.

**About the paper**
- **Methods and code differ for Fig. 2k, 2l and 5c.** The Methods use 20 uL trials and the code uses all mixed-block trials. Only the code's version reproduces; with the Methods' trials the effect reverses.
- **Fig. 2f prints two different results.** The Results give r = 0.08 and the legend r = -0.03; I get -0.037, p = 0.535, close to the legend.

**Assumptions and questions for the authors** (recorded as `methods_unavailable` findings)
- **Model fitting:** the fitting code is not public. I chose the bounds, 2 random starts (the paper used 100), random folds over sessions, and the summed held-out nLL as the cross-validated measure. Do these match what they did?
- **Fig. 3c cohorts:** the cohort sizes add up to 437 for 291 rats. Is each rat counted at every catch probability it ran?

**Questions to a reader:** none.

### 3. Where the protocol was unclear or did not fit
1. The claims have no per-outcome `data` field, so I could not mark Figure 4 as using data from elsewhere. I listed Zenodo under `inputs` and in the deviations.
2. archives.md says to read files with `remfile`. I fetched each file (about 1 MB) whole into memory instead, which is much faster, and noted it in the helper module.
3. Zenodo returned "too many requests" (HTTP 429). I read the zip by a few large range requests.
4. Five seeds for the model fits cost about 19 minutes. The lambda model was fitted once, from one start, without cross-validation; this is recorded as a deviation.
5. The 60-minute limit per notebook forced two notebooks, and each re-loads the data (about 9 minutes each).
6. The fig3i criterion gives no size for an "overshoot". Applied literally, tiny overshoots of 0.0002 to 0.0058 z in the alternative models make the outcome partial.
7. The `pre-cue-session-link` claim in the claims file is marked "Added by the author… written after a first look", so it comes from an earlier attempt. I used it as the claims file has it. That text is the only earlier-attempt content I saw; I looked at nothing else.
8. `runtime_minutes` in `entry.yaml` says 35 for the models notebook, but the run took 46. I left it, because editing the file would invalidate the record of the completed run.

### 4. Runtime and failures
- The behaviour notebook took 13.7 minutes (822 s) and the models notebook 46.1 minutes (2,766 s); both passed. Peak memory was 9.7 GB.
- During development, one run was killed for using too much memory in the Figure 4 cells (fixed by reading less at once), and Zenodo rate-limited me twice. Neither affects the final run.

Files are in `entries/mah-2023/`:
- reproduce_mah_2023.ipynb
- models_mah_2023.ipynb
- mah2023.py

The record is `attempts/mah-2023-02.yaml`.
