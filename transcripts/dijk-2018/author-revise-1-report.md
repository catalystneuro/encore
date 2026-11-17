The round-1 revision is done. The final clean run, `python tools/entry.py all entries/dijk-2018`, passes in 479 s with 0 check errors. Every conclusion, note and the summary now match the new outputs. Nothing is committed.

**Outcomes changed (2 of 44)**
- **fig3b-avoidance-learning: partially reproduced → not reproduced.** The verifier was right that the criterion's own test fails: p = 0.067 under the reading whose df match the paper's. It still fails if WT15's training 2 is counted over its first 10 min (p = 0.067) or WT15 is left out (p = 0.17).
- **fig4d-room-ipos-near-active-zone: partially reproduced → reproduced.** I fixed the post hoc test (B3): Fisher's LSD now uses the mixed model's pooled error. Near the conflict zone, conflict is then above pretraining (p = 0.028) and training (p = 0.012), and 0.035 and 0.017 with the paper's df. One reading misses with the paper's df: 16-px locations with the room-plus-arena normaliser gives p = 0.055.

Two outcomes are unchanged but no longer rest on an assumption, because both readings now agree: standardized-rates-no-difference and network-consistency-overall.

**What I fixed or added**
- **Field detection (B1):** the M5 field rule (from the claims file, unchanged) now runs on smoothed maps instead of unsmoothed ones.
  - The data set holds the authors' own smoothed maps (`RmSm`/`ArSm`). I adopted these for the environment experiment.
  - In the place avoidance task I used my own 3 x 3 smoothing. Four of its sessions have deposited maps on an undocumented 41 x 41 grid, so the authors' maps can't be used for every session of a mouse.
  - All unsmoothed readings are still shown.
  - Fig 1 field counts move much closer: three of the four means are now within tolerance. But the CA single-field share (35 to 55% against 75%) and the removed-DG count (2.09 against 2.70) still miss, so both claims stay not reproduced.
- **fig3d field part (B2):** now run under both pairing readings with every field mask. Under the adopted reading it becomes significant (p = 0.038), with shock addition above replication but relocation not (p ≥ 0.091 under every mask). The outcome stays partially reproduced.
- **Shock-off sessions (B4, B5):** added three variants. One drops the four shock-off recordings whose own Tracker files log shocks. One counts an entrance only after 100 ms outside the zone, which matches the Tracker's count on shock-on files. One does both. Shock status stays significant in all of them (p ≤ 0.0095).
- **Paper's df (B6):** p-values with the paper's df are printed for fig4b and fig4d.
- **Information units (B7):** tolerances are printed in both bits/s and bits/spike. The unit question is added to `questions/dijk-2018.yaml` for a reader; no claim was changed.
- **Two misaligned sessions (B9):** fig1b, rate remapping, field counts and fig1c are also shown without the two sessions that fail the clock check; outcomes hold. I also documented why testbox2 is dropped: it has the same positions as testbox1, and three of four units start with the same spike times, so it looks like a second sorting of one recording.
- **Map check:** our spike maps match the deposited plain maps closely (median r 0.988 and 0.985) but not exactly.
- **Fragile result (B12):** correlation-not-speed passes only narrowly (acceleration p = 0.05004), and the notes now say so.
- **Record:** findings updated (41 x 41 maps, undocumented smoothing, the 20-min WT15 training 2 file, testbox details). The round is recorded under `verifications`, with the verifier's reasons quoted and a response for each claim. The README and `entry.yaml` (`runtime_minutes`) are updated.

**Not done**
- **B10 (zone vicinity):** I kept 4.5 cm, which the paper states in cm, so it doesn't depend on the grid.
- **B8, B11:** nothing to change; every reading was already shown.
- **Kenward-Roger df:** not available here. I gave p with the paper's df instead.
- **Cluster identity across sessions:** stays a stated assumption. The files can't settle it.
