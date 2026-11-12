# Round 3 verifier report: Plitt & Giocomo (2021), dandiset 000054

The claims file has 29 claims and the attempt record has 29 outcomes. Only one outcome carries a `proposed` change, so it is the only one reviewed here.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig7g-model-prior-reconstruction | reproduced (now partially_reproduced) | Yes | — | See below. |

**Reason for fig7g-model-prior-reconstruction:**

- **The criterion has no partial outcome.** It reads: reproduced when the averaged reconstructed prior's Delta D_KL is negative for rare-trained models and positive for frequent-trained models, and its magnitude is below the neural across-mouse mean magnitude of fig6d in both conditions. The test passes as written:
  - The rare-trained models give −0.098 bits and the frequent-trained models give +0.626 bits. Both signs are as expected.
  - Both magnitudes are below the neural ones: 0.098 < 0.223 and 0.626 < 1.125 (nb2 cell 51).
- **Applying the rule consistently gives reproduced.** The attempt uses the same rule for four other claims whose criteria name no partial outcome (session-and-trial-counts, fig2eh, edf7, edf9l).

**Checks of the analysis:**

- **The numbers come from the data.**
  - Cell 51 calls `M.reconstruct_prior` with its defaults: the Methods formula and the Methods likelihood, which is what the criterion fixes.
  - It does this for each of the 50 models from cell 50, averages and normalises R, and computes Delta D_KL against the deposit's priors.
  - `M.dkl` uses log2 (`morph.py:281-333`), so the values are in bits as the criterion requires.
  - The neural yardstick is the absolute value of the main per-mouse fig6d mean from cell 34: rare 0.223, frequent 1.125.
- **The choices were not made to reach the result.**
  - The model settings come from the fig7 criterion as answered by the reader, and the 50 models use fixed seeds (cell 50).
  - The earlier priors give the same verdict: −0.188 and 0.264, both of the right sign and below the neural magnitudes.
  - The code's computation of R, a variant, keeps both signs (−0.349 and 0.378). Under it the rare magnitude is not below the neural one (0.349 > 0.288), but variants do not decide the outcome.

**Caveat for the notes (reported, not corrected):** the criterion compares magnitudes only. The rare neural mean has the wrong sign (+0.223, cell 34), so for the rare condition "less closely matched than the neural data" is measured against a reconstruction that does not match the rare prior. The ideal-observer check in nb2 cell 35 also shows the Methods formula is biased positive on this trial design: an ideal rare observer gets +0.547. So the rare half of the comparison carries little evidence. This is a weakness of the criterion as written, not a misreading of the paper's text. The record already keeps it in the notes, which is the right place for it.
