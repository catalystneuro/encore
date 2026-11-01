No outcome changed. The verifier agreed with all 33 outcomes in round 2, and nothing I found calls for a `proposed` change. The record still has 2 not reproduced, 1 blocked as `methods_underspecified` and 30 blocked as `data_missing`. The entry re-ran cleanly with `python tools/entry.py all`, and `check` reports 0 errors.

**Outputs added to the notebook**
- **Data check:** it now prints which rats the recordings with an empty area come from (all 5 are BH500) and the 33 recordings whose `data_collection` field is truly empty. It also prints the pulse durations (PDs) of the S1 and POm recordings by ultrasound target: with the ultrasound aimed at S1 there are 19 values, from 1.4 µs to 30000 µs. That backs the sentence in the fig7 to fig9 notes, which no output showed before.
- **New cell after the count tables:**
  - **Spike-count rule:** the S1 and POm totals at more than 1000, 2000, 4000 and 8000 spikes. With more than 8000 spikes, the POm totals are within 10% (242, 230 and 1031). No S1 selection fits all three counts under any of the four rules.
  - **Pairs of POm rats left out:** every pair whose removal brings all three POm totals within 10%. That is 9 of the 45 pairs, including BH511 and BH513, the verifier's example (227, 241 and 1052).

**Text corrected**
- **README:**
  - The group "22 claims" is now 18 response claims plus the 2 claims that depend on blocked claims, 20 in all. The rows now add up to 33.
  - The fig11b row said "the normalization readings disagree". It now says the readings of the normalization and the baseline sample give different outcomes.
  - The count row and the summary now say "under every selection of recordings by identifier".
  - A sentence now says the POm totals depend on which rats are included and on the spike-count rule.
- **Count notes (both claims) and the notebook's Result cell:** these now describe the same dependence, mention the AC figure of 445 units above 4000 spikes, and say the outcome follows the criterion as written.
- **Findings:**
  - `selection_undocumented` now says the totals are outside 10% only for selections by identifier, and that leaving out two rats or counting only units with more than 8000 spikes brings POm within 10%.
  - `other` now gives the counts for the minor sites (S1BF 3, VPM 1, and the rest).
  - The `metadata_error` finding now says its 60 sessions are only the ones checked: PD 200 µs, ultrasound at S1, files from two of S1, POm and AC.
  - `metadata_insufficient` now rests on the new outputs.
- **`questions/000946.yaml`:** a new question for a reader. The two count criteria say "under one reading", while the header says the outcome is the one every reading gives. This changes nothing here, so the claims stay as written.
- **`verifications`:** a round-2 entry for all 33 claims, each with `agrees: true`, the verifier's reasons and my response.

**Not done:** I left the verifier's cell numbers as they wrote them. The new cell moves every later cell down by one, so those numbers now refer to the notebook version they reviewed, not the current one. Nothing is committed, as instructed.
