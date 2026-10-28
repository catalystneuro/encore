I made the round-2 revision. The entry re-ran cleanly (`tools/entry.py all`, 0 errors) and the new numbers match the text.

**Outcomes:** none changed, as round 2 does not allow it.
- **figs2ijk-ppx-washout** stays partially reproduced, and I added a `proposed` change to reproduced for round 3. I agree with the verifier that the pooled error is the better-supported choice. Cell 35 now prints the paper's six p-values against both ways of making the Bonferroni comparisons. Pooled matches the paper's significance at 0.05 in 6 of 6 and paired in 5 of 6; paired misses K (paper 0.01, paired 0.063, pooled 0.028). Only pooled meets the paper's p < 0.01 for AUC (0.0072, against 0.039 for paired).
- **The verifier counted "two" misses for paired; at p < 0.05 there is one.** Its second miss is the AUC case, which counts only against the paper's stricter printed p < 0.01. The notebook and record give both counts.
- **`icd.rm_oneway` docstring:** it no longer calls the paired tests "Table 1's reading" or the pooled comparisons Prism's default. It now says Prism uses the pooled error when sphericity is assumed and paired tests when it is not, and that the paper does not say which.

**Text corrections and added outputs:**
- **Baselines per mouse:** cell 20 now prints the total deposited per mouse (2 to 5) and the count before the first drug session (1 to 5). The summary and the `selection_undocumented` finding give both ranges.
- **Sorted units:** the README and cell 0 now say 54 files have no units table and the other two have tables that do not say which units are sorted.
- **CNO open field gaps:** cell 92 now prints each file's gap starting at 19.5 to 21 min. H1 has one at 20.96 min and J3 at 19.57 min. The "twelve files" sentence in cell 93, the fig5cf notes and deviation, and the finding now say every 2023 H and J file except H1 and J3.
- **Round-1 reasons:** I added the parts the verifier said were missing. Problem 9 is now in fig1fg-baseline-similar, problem 10 in fig5g-mcherry-no-change, and the K4 "optoSession" and draft-version notes in the 14 electrophysiology claims.
- **Round 2 record:** it is under `verifications`, with the verifier's reasons and my responses. It records disagreement on figs2ijk (verifier's outcome: reproduced) and agreement on the other 43 claims. The fig2bc entry notes the verifier's own correction of its p = 0.020 figure; the round-1 text is kept as it gave it.

**Not done:** the verifier found no place where the claims file misreads the paper, so I added nothing to `questions/001177.yaml`. fig3a and fig5cf were already resolved as far as the deposit allows, and no claim or criterion was changed.

`git status` lists some untracked files (shell dotfiles, `.idea`, `.vscode`, `.mcp.json`, `scripts`) that I did not create, so I left them alone. Nothing was committed.
