I made the round-2 revision and re-ran the entry with `python tools/entry.py all entries/001699-moore-2025`. It passes with 0 errors in about 13 minutes, and `check` also passes. Nothing is committed.

**Outcomes.** None changed; the verifier agreed with all 27. I proposed one change for round 3:

- **fig1g** stays partially reproduced, with `proposed: not_reproduced`. I re-ran the analysis with sessions defined as the claims file defines them: tracking blocks, with only those over 30 min cut to 1300 s. Under that definition WT r is 0.761 (needs at least 0.81) and Fmr1-/y r is 0.839 (needs at least 0.855), so neither value is within tolerance. The WT value only passes with the 20 min cut, which I adopted after round 1.

**Added or corrected, one item per point in the report:**

- **Out-of-date sentence:** `findings[0]` now gives the re-executed values with the archive's labels, p = 0.23 for HD information and p = 0.17 for offsets.
- **20 min cut versus the claims file:**
  - A new notebook section (after the last claim, before the Summary) repeats every claim's main test under both session definitions.
  - Every recording's sessions are longer under the claims file's definition, by up to 463 s, and session 1 keeps the same cells.
  - Only fig1g changes outcome.
  - fig2h gives exactly the same p = 0.0451, because REM Isomap does not use the sessions. Its move from not reproduced in round 1 therefore came from fitting Isomap on every bin, which the criterion prescribes, not from the cut.
  - The other claims stay on the same side of their criterion. The closest is the figs1c active speed at p = 0.0504; fig1h gives p = 0.014 and fig1j p = 0.069.
  - The cut is now recorded as a deviation under every claim that uses the sessions, not only figs1j and figs2j, and in the Summary. The `hdfx.py` docstring says so too.
- **H3001 200201's 279 bins:** the drift table now prints the second-half bins with speed above 2 cm/s. For this recording that is 330 of 3000, while 2914 have valid tracking, so the low count does come from speed. I dropped the unsupported explanation of the change from 22 bins in round 1. The cell 50 text and the fig1j notes are updated.
- **Records:** the fig1g, fig1h, fig1j and fig2h notes and the fig1g and fig1h result cells give the values under the claims file's definition. Round 2 is recorded under `verifications` with 27 results, the verifier's reasons, and a `response` for each claim.
- **Runtime:** `entry.yaml` and the README now say 13 minutes instead of 5, since the extra analysis doubled the work.

**Not done:**

- **Paper text:** I could not download it. bioRxiv returned 429 for the full text and the source XML, and the Europe PMC full-text request failed. So the version-2 numbers the verifier flagged as unchecked are still unchecked. `paper/` holds only the bioRxiv list of versions (`paper/details.json`).
- **H3026's genotype and cells re-recorded on later days:** I did not resolve either, because the files cannot settle them. They stay as variants in the notes.
- **fig1h:** I kept the outcome, which the verifier agreed with. The notes record that it is not significant for tuned cells only (p = 0.060).
