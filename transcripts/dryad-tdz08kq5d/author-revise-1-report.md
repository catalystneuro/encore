I've worked through the round-1 report. Two outcomes changed, and the re-run (`python tools/entry.py all`) passes with 0 errors, with every conclusion matching its numbers. Nothing is committed.

**Outcomes changed (round 1, so changes were allowed)**
- **fig2e-mucoid-biofilm-increased** goes from not_reproduced to partially_reproduced. The colony type effect and the mucoid half of the claim hold. The SCV half fails: the ancestor's biofilm (0.489) is below all 16 SCV clones. The criterion defines no partial outcome, but a claim that holds in part fits the protocol's partially_reproduced.
- **rnaseq-mutated-genes-expression** goes from not_reproduced to partially_reproduced, for the same reason. phcR up and pilD and the pilus genes down hold. phcS (log2FC 0.41) and "seven of 13" (3 found, at most 5) fail.

Both changes adopt the verifier's outcome. The other 30 outcomes match the verifier's and are unchanged.

**Added or corrected**
- **Ancestor rows and README (B3, C):** a new data-check cell prints the README and each Figure 2 sheet's ancestor block. Each sheet has exactly one ancestor row, so the biofilm comparison does rest on a single value. `phage_temp.py` now raises an error unless there is exactly one.
- **Twitching (B1):** the notebook prints the total sum of squares, 72.277 against 82.082 from Table S3d. A total does not depend on how the rows are labelled, so no assignment of colony types can reproduce S3d. The conclusion and record now say that the comparison fails, and that reading the second 25_0 block as SCVs is my own inference, not the claims file's.
- **fig1b-phage-effect-diminishes (B6):** the text notes that at 25 °C the gap drops to 0.049 on day 8 and rises to 0.322 on day 12, so it does not decline steadily.
- **fig2a-temperature-resistance (B9):** the text notes that within mucoid clones resistance is higher at 25 °C (0.378 against 0.295).
- **rnaseq-kegg-enrichment (B5):** the outcome stays blocked, because the criterion says so when its two readings differ. The text now says the data point to uncorrected p, and I added a question for the reader in `questions/dryad-tdz08kq5d.yaml`.
- **Record:** the README table, the notebook summary and the record's notes are updated. A `verifications` entry holds all 32 claims with the verifier's reasons, its outcomes and my responses; `agrees` is false for the two changed claims. The runner URL now points to this run, and the record validates against the schema.

**Not done, and why**
- **B2** (growth curves) and **B8** (RS-N annotation): that data is not in the dataset, and the record already says so.
- **B4** (the claims file gives the ancestor's twitching as 9.38 cm; the data are in mm): this is already a deviation on the claim. The author may not change the claims file.
- **B7, B10:** need no action.
- **Missing data the verifier could not check:** the two missing Figure 4B genes and which clone carries which variant cannot be recovered from the deposited data.
- **Stray files:** the working tree has untracked files I did not create or touch (`.bashrc`, `.bash_profile`, `.profile`, `.zprofile`, `.zshrc`, `.gitconfig`, `.idea`, `.mcp.json`, `.ripgreprc`, `.vscode`, `scripts`). They should be kept out of the workflow's commit.
