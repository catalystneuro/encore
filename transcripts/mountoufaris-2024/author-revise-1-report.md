Round 1 is answered. One outcome changed: figs5c-peth-activity went from blocked to **not reproduced**. The entry re-ran cleanly with `python tools/entry.py all` (77 min, 0 check errors, all four notebooks pass), and every conclusion, summary and the attempt record now match the new numbers.

**Outcomes:** 3 reproduced, 1 partially reproduced, 10 not reproduced, 22 blocked.
- **figs5c (changed):** the verifier was right. Activity is not lower at p < 0.05 during male sniffing or attack under any reading, and the claim needs all four directions, so it fails whatever the missing female data show.
- **figs4a (kept as reproduced; the verifier said partially reproduced):** "attack probability" now runs under four declared readings. Only the verifier's reading, attack bouts per minute, differs between groups (p = 0.036), with experimental mice attacking *more*. I adopted the attack-triggered time course as an assumption: the S3C legend lists "the number and the time-varying probability" of attack bouts as two separate measures, so a bout rate is the number of bouts, not the probability. The disagreement is recorded.
- **figs4e (kept as reproduced; the verifier said partially reproduced):** I changed the assumption it rests on. It is now the baseline of all frames before the first annotated behaviour. With that baseline neither reading of "nested" finds a difference, and the same baseline reproduces fig4ef. The narrow 7-s baseline, under which the pooled test does differ, is still shown. The disagreement is recorded.

**Fixes and added outputs, by verifier point:**
- **ACHW (fig7c, fig7b):** two more estimators (dividing by n − k, and not removing the window mean), plus a synthetic check of all three. fig7c's reduction is 15–31% under every estimator, against 50.9 ± 5.1%, so the outcome is unchanged.
- **Decoder (figs5e):** added runs with 31 units per mouse and shuffled decoders at every C. Control still decodes better (p = 0.036), so unit counts do not explain the gap. Shuffled decoders score as well as real ones, and the notes now call the measure weak.
- **rSLDS:**
  - Refit with `alpha=0.0`, as in the ssm notebook the claims file cites.
  - Dimension 2 of a complex eigenvalue pair now takes its own weights, so every fig7b combination is defined.
  - Flow fields are drawn and described for all ten mice.
  - A new notebook, `rslds_checks.ipynb`, has a sigma-normalized fit and a one-fold held-out score for seed 0.
  - All six rSLDS outcomes stay not reproduced.
- **Male parts of blocked claims:** added for fig4g (fraction of male-activated units, outside tolerance for controls) and fig5e (choice probabilities; directions hold, at most 2 of 3 values in tolerance). Both stay blocked.
- **Data checks:**
  - Printed each file's description and keywords.
  - The "male part only" statement is now called consistent with the files, not shown.
  - The GCaMP finding now quotes the paper's GCaMP8s passage.
  - fig4ef was re-run without mice 497, 510 and 500; it still holds under two of the three baselines.
- **Reader question:** `questions/001131.yaml` asks whether the paper's "~85% of variance" means the emissions R² (the verifier's point 11). The claim itself is unchanged.
- **Record:** round 1 is under `verifications`, with all 36 claims, the verifier's reasons and my responses.

**Not done:**
- **fig1e** stays blocked as `other`. Another GEO search found no accession for the Kim et al. 2019 atlas, and neither the paper nor the claims file gives one.
- **Held-out score:** I ran one fold for one seed, not the paper's unstated folds. Five folds per seed would take about the whole 60-minute notebook limit.

I did not touch the existing change to `tools/build_site.py` or the untracked dotfiles in the repo root. Nothing is committed.
