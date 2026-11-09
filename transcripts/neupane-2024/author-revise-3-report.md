One outcome changed and no proposals remain open.

**Outcome changed**
- **fig3d-offset-coding-stronger** went from reproduced to partially_reproduced. The verifier agreed in round 3, so I removed the `proposed` block. The main reading now uses the centring the Methods describe: each unit's mean across both windows is subtracted. Under that reading:
  - Monkey A meets the criterion: offset R² is above onset R², p = 2.8e-07.
  - Monkey M reverses: p = 7.3e-12.

  Centring per window and time bin now appears only as a variant. Following the verifier's smaller points, I also:
  - removed `assumed: true`;
  - rewrote the notes and deviations;
  - added two deviations: the criterion's variant using the code's windows was not run, and the bin of largest norm is chosen separately in each window;
  - changed the finding for the paper's authors to say this attempt takes the Methods' centring as the main reading.

No other outcome changed.

**Also updated**
- **Notebook:** the fig3d method cell (40), its conclusion (cell 42), and the summary table and differences paragraph (cell 79).
- **README:** the fig3d row now reads "Partially reproduced".
- **Attempt record:** round 3 is recorded under `verifications`, with the verifier's agreement, outcome, reasons and my response.

`python tools/entry.py all entries/000897-neupane-2024` reported 0 errors and the notebook ran in 1798 s. The fig3d table in the executed copy matches every number in the text. Nothing is committed. The edits to `tools/build_site.py`, `tools/entry.py` and `tools/site_assets/app.css` were there before this run, and I left them alone.
