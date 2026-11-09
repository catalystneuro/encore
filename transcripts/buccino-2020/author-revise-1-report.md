I've revised the attempt to answer the round-1 report and re-run the entry. `python tools/entry.py all` passes (800 s, 13.2 min of notebook time) and `check` reports 0 errors. Nothing is committed.

**Outcome change**
- **fig4a-curators-agree**: changed from blocked (`not_runnable`) to **partially_reproduced**, as the verifier gave. Three of its four values come from the curated files alone: 226 matched units, 351 in all, 64.39%. All three are within tolerance, and the criterion makes the claim at least partially reproduced whichever way the fourth value goes. That fourth value, the 174 Kilosort2 units both curators discarded, needs the Kilosort2 run. The new HDF5 trees show the curated files hold only unit ids and spike times, with nothing linking a unit to a Kilosort2 cluster, so the 174 stays untested. `measured` is left out because the fourth expected value has no measurement. Because a claim is now partially reproduced, the notebook and README carry the required sentence that a failure here may be the attempt's.
- The other 23 outcomes are unchanged: one reproduced, 22 blocked. The verifier agreed with all of them.

**Disagreement recorded**
- The verifier said `not_runnable` is not an allowed reason (point B2). It is in the attempt schema and in protocol step 1.5, for software that cannot be installed in a locked environment, which is the case here. I kept it and recorded the disagreement.

**Corrections and added outputs**
- **Reading time (B3):** the verifier was right. The notebook now times one bulk ranged read: 47 MB/s, so 2 to 10 min per whole recording. All text and the 22 blocked notes no longer cite reading time; the blocks rest on the missing MATLAB and GPU alone. The entry description now says the same.
- **Mouse units (B4):** the notebook prints the electrode columns and data attributes; there is no gain or `channel_conversion`. The text now says the values are consistent with raw counts mislabelled as microvolts but cannot be checked from the file. I added this as a `metadata_error` finding.
- **MEArec (B5):** the notebook prints power by frequency band and the noise after band-pass (11.98 µV). The traces are not band-passed at 300 Hz. Whether the added noise was 10 µV is still open.
- **Other updates:** the finding on chunking now gives both read times. `runtime_minutes` went from 6 to 14. I added `hdf5_tree` and `bulk_read_rate` to `si000034.py`.
- **Verification record:** round 1 is under `verifications` for all 24 claims, with the verifier's reasons and my responses.

**Not done**
- Points B6 (helpers sound) and B7 (64.2% is the paper's rounding, already a finding) needed no change.
- The 174 cannot be tested without a Kilosort2 run, which needs MATLAB and a GPU.
