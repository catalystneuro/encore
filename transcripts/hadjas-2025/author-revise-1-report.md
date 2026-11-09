No outcomes changed in round 1. The verifier agreed with 24 of 25. Where it disagreed, I kept my outcome and recorded the disagreement in the attempt record. The entry re-ran cleanly with `python tools/entry.py all` (0 errors, notebook passed in about 5.5 minutes), and every conclusion was rewritten against the new output.

**The one disagreement: `fig5-anxa1-dls-inhibited`.** The verifier would call it not_reproduced; I kept it as blocked, data missing. Its own reasoning supports the block:
- With the 5 and 4 mice in the dandiset, the Wilcoxon tests the paper uses for three of the six conditions cannot reach p < 0.05.
- The paper's own statistics show it analysed 8 and 10 mice.

That is a block decided once the selection is made (protocol step 1.8). The notebook now prints these numbers and states that the DLS recordings of nine of the paper's mice are not in the dandiset.

**Added to the notebook, one per point in the report:**
- **1 s trains (B1):** the window before the train is the baseline window, so it is always 0. The notebook now prints this and says what follows: paired tests on 1 s trains are tests against 0, and in the two-way ANOVAs the site F equals the interaction F.
- **5 Hz increase in DLS (B2):** I confirmed in the paper that Figure S3F and S3L are the 4 s DLS panels. Each train duration is now labelled with its panel. The 4 s reading holds for 1 of 2 inputs, and the notes record that it would give partially reproduced. The outcome stays on the 1 s trains of Figure 4E and 4H, which the criterion fixed and the same sentence also cites.
- **Vglut2 STN mouse count (B4):** a new helper computes exact Wilcoxon p-values. It confirms the paper's W values fit 9 mice, not the legend's 10. I moved this from a data-missing finding to a paper-inconsistency finding. The count check stays not reproduced: 11 of 16 counts match with this explained, still below the 12 needed.
- **Vglut2 PPN frequency tests (B5):** the frequency tests now list the dropped mice. C3412, C3798 and C4707 have no 5 Hz trains, and the paper's χ² of 24.8 needs at least 9 mice. Added a data-missing finding.
- **Late peaks in fig3b (B6):** I plotted and measured C4217 and B8612. Both have small responses with an early maximum at 0.41 and 0.62 s, then a slow rise peaking at 2.97 and 2.78 s, past the fixed window. That looks like a late rebound or drift.
- **Anxa1 frequency tests (B3, B8):** the notebook now prints the sample size the paper's degrees of freedom imply (about 8.5 and 10 mice, against 4 here). I added the Figure 5 N/O legend contradiction and the impossible F1,11 to the paper-inconsistency finding.
- **fig3g clock check:** the clock-check table now has an input column. Without the three PPN recordings whose clock could not be shown (C3164, C5007, C5008), the test still finds no effect (p = 0.11 and 0.14).
- **DA terminals in DLS:** the mouse ids are now printed. The TS and DLS groups are different mice, so the data cannot show which DLS mouse is absent.

The round is recorded under `verifications` in `attempts/001528-hadjas-2025-01.yaml`. The paper text is saved in `paper/`.

**Not done.** Nothing the report asked for was left out. I did not edit the README: its outcome table is unchanged and none of the corrections touch its text. Nothing is committed, as instructed. `git status` lists some untracked dotfiles and folders in the repo root (`.bashrc`, `.mcp.json`, `scripts` and others). They are sandbox placeholders, not files I created, and the commit should leave them out.
