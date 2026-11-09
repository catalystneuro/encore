The round-3 verifier agreed with all three proposed changes, so all three outcomes changed and no proposal is left standing.

**Outcomes changed** (`assumed: true` stays on all three, as the verifier asked):
- **fig4c-alpha-beta-shift**: partially reproduced → not reproduced. Under PSI reading (a), 5 of 7 subjects are below 0, and the partial match needs 6. The recorded values are now reading (a)'s: -0.14 and F = 6.7.
- **fig5a-spatiotemporal-bidirectional**: not reproduced → reproduced. It meets the criterion as written, but shows little. Under reading (a) the identity grand mean also stays below 0.99, where the paper reports more than 2.35. The 78 pairs selected are also about what the trial-shuffled control selects (68).
- **fig5b-alpha-beta-no-sustained**: reproduced → partially reproduced. Under reading (a) no time point is significant after FDR correction.

**Other updates**
- The `proposed` blocks are removed. I rewrote the notes and deviations of those three claims around reading (a) and added round 3 under `verifications`, with the verifier's reasons and my responses.
- The notebook's three conclusion cells, the summary table and item (4), the adopted-reading paragraph, and the README table and PSI paragraph now give the new outcomes.
- One point the verifier said it had not checked: the calibration of the time-resolved PSI. That needs a new analysis, so the record leaves it for a later attempt.

**Run**: `python tools/entry.py all entries/crcns-fcx-3-johnson-2019` passed with 0 errors in 2420 s. Every value cited in the record matches the re-executed outputs. That run was a little faster than the stated range, so I changed the runtime text in the notebook and README to 40 to 43 minutes. `entry.py check` passes again after that edit. The executed copy still has the old runtime sentence in its first markdown cell, which affects no result.

Nothing is committed. The working tree also has a change to `tools/build_site.py` that was there before this run; I didn't touch it.
