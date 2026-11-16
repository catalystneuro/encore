I've worked through every point in the round-2 report and re-run the entry with `python tools/entry.py all entries/brudner-2026`. The check reported 0 errors, the notebook passed (823 s, peak memory about 8.4 GB), and the conclusions match the new numbers. Nothing is committed.

**Outcomes.** No verified outcome changed. One change is proposed for round 3:
- **figs5c-turn-angles:** the recorded outcome stays reproduced, and I propose not_reproduced. I ran the half-height bounds the verifier pointed to (Fig. S5A); they give medians of -25.0 to -26.6 and +26.8 to +27.7 degrees, outside tolerance. The claims file's own readings give about ±21 degrees. Only my 20% bounds on both edges give the published medians, and that end of the turn is not in the paper and was chosen after the event bounds failed. So I tested the claim as the claims file has it, kept the 20% bounds as a variant, and asked a reader which bounds are the paper's.
- **fig5e-cue-betas:** still not_reproduced, but I removed `assumed: true`. As the verifier said, no file set or onset gives the result in every reading, so the outcome does not depend on the file-set choice.

**Added outputs:**
- **Sign test against plume geometry (remaining point 2):** it does not settle the question. In the smooth plume the mean gradient cue follows the slope of the mean intensity across y, with r of -0.96 and -0.94 facing upwind and +0.93 and +0.94 facing downwind. In neither complex set does it (r -0.65 to +0.33), so the test cannot tell the two sets apart. The two sets' projections are not mirrored relative to each other: intensity profiles correlate at 0.77 and 0.67 for the same flip label and 0.04 and -0.03 for the opposite one. A different sign convention between the sets is therefore stated as not ruled out, and added as question 7 for the paper's authors.
- **Turn events:** outputs now show where the events sit. They lie inside the half-height run (starting 1 frame after it and stopping 1 frame before it), and 99.9% stop before the falling 20% crossing. This backs the Summary's "end before the turn does".
- **Other printed outputs:** the Dryad 401 (now requested in the data check), the provenance strings of the movie windows, the y range of the out-of-arena frames (768 to 814 mm), and a computed check of turn_theta, turn_x and turn_y (it was previously cited from preparation).

**Corrections:**
- **README:** the wrong sentence saying the complex motion cue never reaches significance is fixed. The Fig. 5F row now says the outcome rests on the turn onset as well as the file set.
- **"Only" smoke-1a matches the published tables:** now "most closely", since smoke-1a with the SI onset is also close.
- **Wording:** "not a flip convention", "same factor" (now "similar"), "same to three decimals" (now "within 0.001"), and the Summary's fig5e and fig5f rows.
- **Record:** 1010 trajectories, not 1011; event lengths of 5 to 11 frames; and the round-1 `reviewed` field now says that one Result cell had been left in.

**Removed:** the lag-scan claim and the claim that the port gives the code's own numbers. Neither was run in the notebook.

**Records:**
- **Questions file:** three questions for a reader are added: the figs5c event bounds, which complex file set fig5e should take, and why fig5e takes the outcome all readings give while fig5f needs only one reading.
- **Round 2 in the attempt record:** recorded for all 22 claims, with the verifier's reasons and my responses.

**Not done:**
- **fig2c-complex-auc:** no change. It still rests on the stated mirror-balancing assumption.
- **Stray files:** untracked dotfiles at the repo root (`.bashrc`, `.vscode`, `scripts` and others) were already there and I did not create them. I left them alone, so they will be in the workflow's commit unless they are removed.
