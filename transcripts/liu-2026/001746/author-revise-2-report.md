Round 2 is done. No outcome changed. The verifier disagreed with three claims, and for each I kept the verified outcome and wrote a change to blocked under `proposed` for round 3. The final run (`python tools/entry.py all entries/001746-liu-2026`) passed in 6.5 minutes, and `entry.py check` shows 0 errors. Nothing was committed.

**Proposed changes (all to blocked, `methods_underspecified`)**
- **`fig3e-phase-peak-index`** (now partially reproduced): I agree with the verifier's main point (R1). The automatic index can't tell a saddle from noise, so it doesn't measure the saddle shape on these recordings.
  - The rule that reads most first APs (195 of 237) puts the axon-segment peak right next to the main peak once the trace is noisy. That gives the most saddle-like score whether or not the AP has a saddle.
  - On synthetic APs with no axon-segment phase, the index falls from 0.81 to between 0.003 and 0.011 with 0.02 to 0.05 mV of noise at 50 kHz. The recordings sit in that range: 0.023 mV in the Axon files and 0.30 mV in the HEKA files.
  - On the 28 first APs with two clear peaks, where that rule isn't used, the groups don't differ (p = 0.54).
  - The outcome also flips when the peak-size threshold drops from 0.05 to 0.02.
- **`fig3d-saddle-phase-plane`** (now partially reproduced): its criterion makes it take fig3e's outcome.
- **`fig4i-peak-index-ais-distance-real`** (now not reproduced): it uses the same index and depends on fig3e.

**Outcomes now flagged `assumed: true`**
- `patchseq-cell-table-link`: it rests on reading the cell table's row 235 as the row for cell s172. The finding on that row now asks the paper's authors to confirm.
- `l5et-vs-l5it-sag-rm-rate`: it takes the outcome common to both sag measures. The notes now say that if the criterion inherits the other sag claim's "blocked when the measures disagree" rule, this claim would be blocked.
- fig3e, fig3d and fig4i: they rest on the details of the automatic reading.

**Corrections and added output**
- **The "at most 3%" sentence:** that figure was the mean over all APs. On the first AP, unresolved cases are 5 of 30 L2/3 IT HPCAL1 cells, 3 of 29 VEN and 3 of 18 L5 ET. Leaving them out changes the first-AP Dunn result, and the text now says so.
- **File description:** the notebook now prints each file's experiment description ("Patch-seq experiment of cell atlas investigation…"), and the fig4ac notes quote it.
- **GEO download and run time:** the notebook now prints the archive size (24.69 GB) and how much was read (4.42 GB). The README and opening cell now give the printed run time.
- **Formatting:** the stray `**` markers in six result paragraphs are removed.
- **fig7c:** the Methods do define how "the 500 most-variable genes" are chosen (Transcriptomic mapping section), so the record was wrong to say they don't. I implemented that selection and made it the main gene set. It gives r = 0.053 (p = 0.67) where the paper reports 0.53, so the outcome is still not reproduced; the two earlier gene sets are kept as variants.
- **Questions for a reader:** I created `questions/001746.yaml` with the three places the verifier says the claims file may misread the paper:
  - fig3e reads "lowest derivative value" as the lowest point of the second derivative;
  - fig3e lets the second peak be smaller than the first, which allows negative indices;
  - fig7c's "more than five cells" rule conflicts with its own cluster list, which includes clusters of 4 and 5 cells.
- **Round 2 record:** written under `verifications`, with the verifier's reasons and my responses.

**Not done**
- The confound between amplifier, recording year and cell group (R4) needs no change; it stays reported as before.
- The run times on record vary: one full run in this revision took 43 minutes because the GEO download alone took 37. Only the 6.5-minute final run is reported, since it is the one printed in the notebook.
- After that final run I edited only the run-time sentence in the notebook's opening cell and the README, so the executed copy has the older wording in that one cell.
