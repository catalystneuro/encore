I've worked through the round-2 report. All 21 outcomes are unchanged and nothing is proposed for a third round. The verifier agreed with every outcome, and none of the new outputs gives a reason to change one. `python tools/entry.py all` passes; the notebook ran in 18.9 min, and every number from before the revision came out the same.

**One correction the report didn't catch:** file I-160616-4 does have 5 curated units and raw data. Only its trials table is missing. The record, cell 4 and the Summary all said it had no raw data and no curated units; I fixed all three, and the data check now prints its unit and sample counts.

**Text corrected (report section 2):**
- **Outcomes that depend on which units are used:** the README and Summary now name four. With the paper's own unit list, hold-period-ramps, monophasic-more-in-vla and fig3a-vla-leads-gpi would be reproduced, and fig3b-gpi-decr-lag-vla-incr would be partially reproduced, because its GPi median (-36 ms) is outside tolerance. The fig3b conclusion and notes now say this too.
- **README run time** now reads about 19 minutes.
- **Cell 4:** removed the sentence about the post-MPTP files, which are never loaded.
- **The two findings the verifier said had no output behind them:**
  - The data check now prints the sorted clusters in `processing/ecephys/units` for the 21 files without curated units. 13 files hold 124 clusters, and the only columns are spike time, unit name and location. 8 files have no such table.
  - The Fig 1 cell now prints the `acx_y` and `acx_z` column descriptions from the file ("ventral positive").
- **Round-1 reasons:** added the verifier's problem 3 to fig4-ccf-rare and problem 1 to increases-most-common. Both rounds now note which notebook their cell numbers refer to.

**Outputs added (report section 3):**
- **The paper's unit list for the three pair claims.** None of the outcomes would change:
  - CCF: p = 0.005 over whole recordings, 0.033 at rest, 0.203 during movement.
  - Noise correlations: KS p < 0.001 at rest and during movement.
  - Fig 5: no fall below the control band.
- **Pair counts:** 338 pairs from the dandiset's labels and 329 from the paper's list, against the paper's 427. I could not find how the paper counted its pairs, and the record says so.
- **Fig 5 exclusions:** now split by reason. More than half the pairs are left out for a noisy baseline (157 of 307 for burst onsets and offsets, 143 of 253 for pause onsets). The conclusion now says this outcome says little about the paper's finding.
- **Stricter detection (alpha 0.0001)**, run on the data and on random alignment, needed a new `alpha` argument in `gpivla.py`:
  - Chance still finds a decrease in 30.8% of VLa unit-directions, against 42.0% in the data.
  - fig3c still fails (p = 0.3).
- **behavior-rt-mt:** the record now says no set of files gives the paper's 452 degrees of freedom (326, 496 and 320 here).

The round-2 verification is recorded in the attempt record, with the verifier's reasons in its words and my changes under `response`.

**Not done:** I did not correct the decrease detector for chance. The stricter threshold barely lowers the chance level, and a correction would need a method the paper doesn't describe. The notes say chance detections may pull the VLa decrease onsets late. I downloaded nothing, so `paper/` only has what the verifier saved. Nothing is committed.
