No outcome changed in round 2. The verifier agreed with all 40 outcomes, and I found nothing that called for a proposed change, so no `proposed` entries were written. I re-ran with `python tools/entry.py all entries/hunt-2018`: the notebook passes (590 s of execution, 9.7 min total run time) and the checks report 0 errors.

**Corrected text, in the notebook and the record**
- **fig4-t75:** at the 1 ms step, all nine values match the paper exactly only over −200 to 600 ms. Over −100 to 500 ms, DLPFC left/right value is 358 ms against the paper's 369 (within tolerance).
- **fig5k:** five of the six Fisher p-values match the paper. The sixth, EV 3 vs EV 2 against ACC, is p = 1.3e-05, ten times smaller than the paper's 0.00013.
- **fig8-action:** with the exact binomial test the tests hold in five readings plus the script's, not six. Reading (b, iii, b, 0.05) fails it.
- **figs5c vs figs1ab labels:** the reason figs5c is not_reproduced is now what the verifier suggested: its one test fails in at least two of three regions under every reading. figs1ab stays partially_reproduced because one component fails in one monkey and the rest holds.
- **Minority readings:** the Summary table and the README now say when an outcome holds under only some readings: fig6e under 12 of 72, fig7a under 4 of 12, fig8-spatial under 2 of 26. The README also marks the early-choices claim "(assumed)".

**New output the verifier asked for or raised**
- **figs5c:** the notebook now prints the t75 point estimates for every template and region. They overturn one sentence in the record: with all significant templates, DLPFC accept/reject (491 ms) comes after left/right value (369 ms), so the paper's order does not hold in every region. The text now says so.
- **fig5gj:** the single 183 x 183 map variant only passed because of the seed. With 10 other seeds, EV 3 x EV 2 passes in 0 of 10, and it fails with 10000 permutations. The text now says that variant does not hold. The outcome stays reproduced because it rests on the script's separate maps, which pass by wide margins.
- **Figure 6 projection data:** I added a helper to `pfc7.py` that reads the start of an array from the 5.3 GB `info_gathering_ramp_to_choice.mat` by range requests. For the first five stored random halves, the data projected here match the stored data to within 1.4e-07 for every ACC unit. The exceptions are 15 traces built from a single trial: MATLAB's `mean` on one row averages over time, so the script stores those as a flat line. I recorded this as a new finding about the paper's code (`other`).

**Recorded:** round 2 is under `verifications`, with all 40 claims agreed, the verifier's reasons paraphrased closely, and my changes under `response`. The verifier reported no new misreadings of the claims file, so `questions/hunt-2018.yaml` is unchanged.

**Not done**
- The RSA still can't be checked against stored output, because the data set holds none.
- I compared the projected data and the weights against stored values, not the final projection traces themselves. The script doesn't store those traces in this file.

Nothing is committed.
