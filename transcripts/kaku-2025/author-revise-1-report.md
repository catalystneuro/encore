I've revised the attempt for round 1: I fixed or answered every point in the report, re-ran the entry, and nine outcomes changed. The final `python tools/entry.py all entries/kaku-2025` passed with 0 check errors (notebook 2,662 s), and the conclusions match the executed numbers. Nothing is committed.

**Outcome changes**

| Claim | Before | Now | Why |
|---|---|---|---|
| fig1d-lick-breath-frequencies | not reproduced | partially reproduced | Fixed B2: reading (b) had counted 13,498 onset pairs spanning two bouts. Licking is now 6.07 Hz (3.77 to 8.40), within tolerance. Breathing is 4.19 Hz, but its bounds (2.41 and 6.39 Hz) are outside. |
| fig1f-licking-mode-switch | partially reproduced | not reproduced | The criterion defines no partial outcome (verifier's point). |
| region-spike-rates | partially reproduced | not reproduced | Same reason. |
| fig2h-swallow-units-location | partially reproduced | blocked, methods_underspecified | The two V4 readings still disagree (4 of 5 regions against 2 or 3). |
| ed8bc-prebotc-inspiration-phase | not reproduced | reproduced, assumed | With the region built from the CCF annotation, 18 or 19 units qualify, 74 to 78% in the inspiration half, Rayleigh p < 0.0001. |
| fig4d-simultaneous-recordings | not reproduced | blocked, data_missing | The verifier's reading: only 4 two-probe sessions have any unit in both regions. Extended Data Fig 12c places these recordings in the cued task, which is not deposited. |
| fig4g (two claims), fig4h | blocked, other | blocked, data_missing | They follow fig4d; the notebook now gives the reason. |

fig3a and fig3b stay blocked, but for a different reason. The premotor coordinates are public as eLife 10:e67291 Figure 5 source data 1, so the data are not missing. I found them but did not analyse them in this run, so both are recorded as `other`. fig2f stays reproduced but is now marked as resting on how the region is built. fig4e loses its assumption flag, because the simultaneous-recording reading now has 3 to 10 units and agrees.

**Added or corrected**
- **Regions (B3):** the preBötzinger complex and the other unlabelled regions are now built from the Allen CCFv3 2017 annotation volume, recorded as an input. Taking AMB's whole extent, as the claims file words it, gives 36 to 41 units. Taking its extent per 100 µm AP step, shown as a variant, gives 12 to 15 units and loses the fig2f and ed8bc results.
- **Random-split null (B1):** the asymmetric windows produce most of the fig1g and fig4e effects:
  - fig1g: the null is 18.3 ms, and the data exceed it by 9.1 ms (p = 0.17).
  - fig4e: the null is 44 to 53 ms.
  - fig1i and fig4f survive the null.

  I kept the criterion's outcomes, which compare with 0, recorded this in the notes, and added a question for the paper's authors.
- **New finding:** in 19 of 173 sessions the 3D `idx` field is one below the DLC trial number. Each session is now read at its own offset, which moves ed8e to 71.4 to 71.5%.
- **Outputs the verifier asked for:**
  - airflow-to-tongue/jaw cross-correlation per subject
  - full lick trace around swallows (licking pauses from -90 to 0 ms)
  - fig1l cycle distributions, after confirming the port matches the paper's code
  - ed1 diagnostics, with the dead line removed
  - filter order 2 for fig4d, fig4e and fig4f
  - the 40 fastest and 40 slowest cycles for fig4e, with the code's selection beside it
  - the sign-free hemisphere test for ed8i: it differs between hemispheres along the 3D x axis (p < 0.0001); the claim stays blocked
  - a measured GLM cost for ed7: about 7 CPU hours for one reading, over 80 for all
- **Questions for a reader**, in `questions/kaku-2025.yaml`:
  - units-count: arbor vitae and other fibre tracts (B11)
  - ed1bc: the window after swallow onset (B5)
  - the header calls the code's selection the "40 fastest and slowest"; the code actually takes the 40 nearest the median (B7)
- **Record:** the round is under `verifications` for all 48 claims, and the protocol version is now pilot-14. The README, the notebook header and the summary are updated.

**Not done**
- fig3a and fig3b were not analysed. They need a bregma-to-CCF conversion and the density contours, which did not fit in this run.
- B10 (histology rows matched to units by position) is unchanged. It is already a finding, and the files give no identifier to match on.
