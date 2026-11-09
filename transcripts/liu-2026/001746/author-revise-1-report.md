I've revised the attempt for every point in the round-1 report and re-run the entry from a clean environment. `python tools/entry.py all` passes with 0 errors, and the notebook takes 7.5 min. Across the 33 claims, 7 are reproduced, 10 partially reproduced, 3 not reproduced and 13 blocked (9 because the data are in other archives, 3 data missing, 1 methods underspecified).

**Outcome changes** (allowed after round 1):
- `patchseq-cell-table-link`: partially reproduced → reproduced, as the verifier gave it. Row 235 is read as the table's row for s172, and the letter of the criterion is recorded in the deviations.
- `l5et-vs-l5it-sag-rm-rate`: reproduced → partially reproduced, as the verifier gave it. Input resistance is now significant (FDR 0.039), so all three hold under sag ratio but only two under sag value. The outcome is the one that holds under both readings, so the sag-ratio assumption is dropped.
- `supp11-ven-broad-ap`: not reproduced → partially reproduced. After the threshold fix (below), the VEN median half-width is the highest (3.03 against 2.98 ms), but no reading is significant.
- `fig3e-phase-peak-index` and `fig3d-saddle-phase-plane`: blocked → partially reproduced. Both AP readings and both corrections now agree: the VEN median is lowest, and Dunn's test separates VENs from L5 ET only.
- `fig4i-peak-index-ais-distance-real`: blocked → not reproduced. The regression ran on the 153 cells that have an AIS distance in the morphology table. Neither automatic reading gives a negative slope; the paper's hand-read values give one (p = 0.018).
- `fig7c-tau-rna-distance`: blocked (`too_large`) → not reproduced. Ext.h5ad streams from GEO in about 2 min. With the Methods' tau, r = 0.105 against the expected 0.53.

**Fixes and additions:**
- **Threshold bug.** I found this while checking the device question. A filter artifact at the end of the detection window put the AP threshold at the AP peak in 28 HEKA files. Agreement with the paper's table rose from 89.5% to 96.7% for half-width and from 90.2% to 97.5% for amplitude.
- **Phase index.** An AP with no AIS peak and no shoulder now takes the lowest dV/dt of its rise, the Methods' "point with the lowest derivative value", instead of 0. The notebook now shows synthetic APs, the per-group share of such APs (at most 3%), and a variant that leaves them out.
- **FDR over 39 features.** The 19 features defined nowhere now take the paper's table values, so the FDR is computed exactly and no comparison is undecided. No outcome rests on this or on the other choices, so no outcome is marked `assumed` any more.
- **Duplicate recording.** n175 is left out of the L5/6 CT group in `supp9-venl-more-distinct-from-ct`, which now holds 10 cells, matching the legend. VEN-L differ from that group in 6 of the 39 features and VEN-S in none.
- **Requested outputs**, all added:
  - the device by typed status by group crosstab;
  - a check on 40 Axon files brought down to the HEKA sampling rate;
  - a search of every file's HDF5 tree for annotations (none found);
  - tau fit counts and spread, with a median-over-sweeps variant;
  - sag measured at -200 pA only;
  - random sets of 40 of the 57 morphology features.

**New finding:** half-width and tau are much longer in the Axon files in every group, both in my values and in the paper's own table (3.13 against 2.08 ms, tau 41 against 26 ms). Sampling rate does not explain it. Within either device, the narrow APs and short tau of L2/3 IT HPCAL1 are not significant. This is recorded in the notes and findings, but the outcomes stay as the criteria decide.

**Not done:**
- No questions were added to `questions/001746.yaml`, because the report names no place where the claims file misreads the paper.
- The code's Patch-seq-counts variant for fig7c is not run, because those counts are not on this dandiset.

All changes are left uncommitted for the workflow.
