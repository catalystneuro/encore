There is no claims file to check, so I changed nothing.

- **Checker:** not run. `claims/001284/` does not exist on this branch, on `main`, or anywhere in the git history.
- **Why it's missing:** the last commit (a47ac270) only added `transcripts/001284/claims.md` and `claims-report.md`. According to that report, the claims run was cut off by the safety classifier while it was writing `claims/001284/10.1016-j.bioelechem.2025.109016.yaml`, so the file was never saved.
- **Changes:** none. Adding a `checks` entry needs a file to put it in. Writing all the claims myself would be the reader's `claims` role, not this check, and an unchecked file I wrote should not be marked ready.
- **Ready:** no.
- **Next step:** rerun the `claims` role of the Paper run workflow for 001284, then rerun `claims-check`. The paper text is in `paper/10.1016-j.bioelechem.2025.109016.txt`.

The earlier run's report lists open points the new claims file should state as open:
- whether the two diagonals or all four directions are pooled;
- the Lorentzian fit range, given as 4 to 6 mm in the Methods, ±4 mm for Fig. 3 and ±5 mm for Figs. 5 and 6;
- whether group curves are fitted to the means or to the pooled points;
- the ROI spacing;
- how "near electrodes" is defined for the 40-fold ratio;
- whether the Fig. 6D fit is logarithmic or linear;
- where the "2.3% of array area" figure comes from.

It also found a mismatch between the dataset description (10 mm electrode spacing) and the paper (15.3 mm diagonal).
