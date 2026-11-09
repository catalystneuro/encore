No outcome changed and none is proposed. The verifier agreed with all 33 outcomes, so the record still has 18 reproduced, 4 partially reproduced, 3 not reproduced and 8 blocked. I re-ran the entry and it passed (about 21 minutes). The new code changed no numbers, and every conclusion matches the outputs. `tools/entry.py check` reports 0 errors.

**Text corrected**
- **Run times:** the header, the feature-extraction and classifier sections, the README and `entry.yaml` now give the printed times. The run takes about 21 minutes: about 7 to analyse the files, about 5 and 4 for the two classifiers, and 3.5 for the morpho-electric classifiers.
- **How far the features confirm the link:** the summary, README, record deviation and finding no longer say "all 283 cells". With the Methods' sweep QC (the main QC) it is 261 of 283. I also added the per-cell match the verifier noted was missing for IPFX's sweep QC (IPFX is the feature-extraction library). It picks the expected cell for 282 of 282 files, including 21 of the 22 cells that give no features under the Methods' QC. The last cell gives features under neither QC, but its sample date matches its file.
- **cohort-cells note:** it now quotes the printed error (`ydata` must not be empty) instead of saying the f-I fit failed.
- **Human L2 fractions:** these were misquoted. The values the R scripts print include −0.1639, and the Python port of those scripts matches all five.

**Outputs added**
- A table that reads every value the paper's R scripts print, straight from the scripts at the pinned commit, and puts it beside the port's value. The port matches the thicknesses, L2 fractions, densities, all 16 pooled area quantiles and the six largest areas for each species.
- **The 3.94 versus 4.0 gap on fig1c-soma-variation:** the gap comes from a bug in the human script, which never clears one of its variables between sections. As a result, R repeats each human section's bins a different number of times. With those repeated rows the ratio is 3.99 to 4.02, and with one or two sections' worth of leftover data the port gives all four ratios the script prints. I kept 3.94 as the judged value, because the criterion counts each section once. Every version is within 4 ± 0.4. I recorded the bug as a new `code_mismatch` finding and corrected the earlier finding that claimed the port gave "every printed value".

**Verification record**
- Round 2 is added with all 33 claims, the verifier's reasons in close paraphrase, and my responses.
- The round-1 entry now says its 26 agreements were against the round-1 record (22 against the current one), so `agrees` on the four claims that changed refers to their round-1 outcomes.

**Not done**
- **Cell QC and which sweep QC to use:** these would move fig4-glp2r-sag, edtable1-species-ephys and fig6-deep-ephys-anova. I did not apply either change, because both questions are still unanswered in `questions/000023.yaml` and the claims file's criterion asks for the Methods' sweep QC only. The verifier agreed with these outcomes under the claims file as written. Their fragility is in the notes and in the round-2 reasons.
- **Unchanged by choice:**
  - The 35 links without features are still described as supported, not proven.
  - The exact small-count tolerances are the claims file's, so I left them alone.
  - The fig2ef group sizes are still not recovered.
- **Leftover files:** `git status` shows some untracked files I did not create (dotfiles, `.idea`, `.vscode`, `scripts`). I left them alone.
