The verifier agreed with both proposed changes, so I applied both. The full run (`python tools/entry.py all entries/001271-semenov-2025`) passed with 0 errors, and all three notebooks executed.

**Outcomes changed**
- `figs2-before-firing-then-depolarization`: partially_reproduced → **not_reproduced**. Every claims-file reading fails, and the criterion has no partial outcome.
- `fig3c-sustained-firing-2s`: partially_reproduced → **not_reproduced**. All 48 readings fail, and the third part fails everywhere.

**Proposals still standing:** none. I removed both `proposed` blocks and left every other outcome as it was.

**Other changes**
- **Wording errors:** I fixed the two the verifier found, which did not affect the outcomes:
  - There are 16 claims-file readings for the Figure S2 claim, not 24. The other 8 rows are the whole-frame variant, which also fails. I left the round-2 verifier's "24" as it was recorded.
  - For Figure 3C, the first two parts fail only with O1(b) and the 5-SD height. With O1(b) and the 5% height, both remaining cells meet both parts.
- **Notebooks and README:** I updated both notebooks' conclusions and summaries, the README table and the claim notes to match. They still say that "not reproduced" means the claims file's sustained-depolarization measure (O4) finds no plateau, not that the data show none. That point is still asked of a reader in `questions/001271.yaml`.
- **Round 3:** recorded under `verifications`, with one result for each of the two claims, the verifier's reasons and my responses.

`tools/build_site.py` already had uncommitted changes before this run. I did not touch it, but the workflow's commit may include it. Nothing is committed or pushed.
