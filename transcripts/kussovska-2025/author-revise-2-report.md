I made no outcome changes, as round 2 requires. One change is proposed for round 3: **fig6e-load-modulation-in**, reproduced → partially reproduced. The entry was re-run with `python tools/entry.py all entries/kussovska-2025`: both notebooks pass (52 min and 23 min), `check` reports 0 errors, and the conclusions match the new numbers.

**Why fig6e is proposed as partial.** I refitted the ACG model with changes the size of floating-point rounding (the start point ×(1 ± 1e-9), the ACG ×(1 + 1e-12)). Two of the four fits give 15 IN concept cells and meet the criterion. The other two give 16, and the IN concept share drops to 18.75% (p 0.037 to 0.047), below the tolerance, under every permutation and tie rule. With the types of reading (b) it is 14.29% (p = 0.15). The load modulation of IN and IN concept cells, and its absence in PY, holds under every fit. The reason is under `proposed` and the analysis is in the notebook.

**Run-to-run instability (the verifier's main open point), now explained:**
- **GLM:** with load as the predictor, 8 neurons have |b1| exactly equal to their own null threshold, so rounding decides whether they count. Counting them in or out moves preSMA between 47 and 51 neurons and vmPFC between 6 and 7. fig1e still holds under every tie rule with the within-participant permutation. I added this as a finding.
- **ACG fit:** the rounding-size changes above give 315 to 317 well-fit neurons and move R2 by more than 1e-3 for 34 to 39 neurons. This is why the yield, cell types, fig4c and fig6e moved between runs. A repeat run on this machine gives identical numbers, so the variants stand in for runs on other machines.

**Other additions:**
- **fig4c:** I rebuilt the groups under each fit variant and with the shipped τdecay. With the 1-bin spacing the pattern holds every time (low ACG BH p 0.0385 to 0.0483). With the criterion's main 2-bin spacing it holds under 3 of the 5. The conclusion, notes and peak-rule finding now say the outcome rests on the 1-bin variant and that the best result under the main spacing is partial.
- **τdecay groups from the shipped `Decay` column:** fig4d, fig4hj and ext2 keep their outcomes with these groups. For fig4-acg-group-differences they give the claim's whole pattern: short exceeds long in encoding (p 0.0078 and 0.0205). So the partial outcome may come from my fit. The shipped values are an outside input used only for comparison, so I kept the outcome and said this in the notes.
- **Per-trial thirds of maintenance (Fig. 6c legend):** run as a third M1–M3 reading for fig4f, fig4hj, ext2, fig6cd and ext5bd. It changes no outcome. The claims file's omission is now a question in the new `questions/kussovska-2025.yaml`, for fig6cd and fig4f; the claims themselves are unchanged.

**Text corrections:**
- **fig1e:** the stale values are fixed in cell 35, the record's notes, and `measured` (now 20.0).
- **concept-cells-count:** "exactly" is removed from the seed-0 regional shares.
- **fig2d:** the sentence contradicting the shuffled-map counts is removed.
- **Findings:** the acg-fit-yield and peak-rule findings are corrected.
- **Round-1 reasons:** problems 2 and 10 are added to the claims they bear on.
- **Round 2:** recorded under `verifications` for all 45 claims.

**Not done:**
- No repeat runs on other machines. The rounding-size variants and tie rules stand in for them.
- fig3d and fig3h are unchanged; their dependence on the code's trial selection and protect setting was already disclosed.
- fig4c and fig4-acg-group-differences keep their verified outcomes, for the reasons given above.

**Code changes:**
- `wm.py`: `glm_groups` takes a tie rule, and the fit takes the rounding-size changes.
- The ACG feature cell now runs in parallel; its results are unchanged.
- `entry.yaml` and the README now give the 52-minute run time.

Nothing is committed. Untracked dotfiles and a `scripts` directory in the repository root were not created by this work, and I left them alone.
