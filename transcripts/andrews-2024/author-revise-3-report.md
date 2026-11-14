I've applied round 3. The verifier reviewed one proposal and agreed with it, so it is applied and no proposals remain.

**Outcome changed**
- **simulation-dampening**: now **reproduced** (it was blocked as not runnable). I removed `blocked_by` and `proposed`.

No other outcome changed. The cohort claim is still partially reproduced and the other 27 claims are still blocked because the data is missing.

**Other changes**
- **Seed 22:** the verifier asked the record to say this plainly, so the notes and the notebook's result cell now do. Seed 22 meets the criterion under no reading: at fraction 0.50 the event duration is unchanged and the events hold 103 spikes, against 101 at fraction 0. Both also say the verdict uses the script's own seed, 20.
- **Text:** the notebook's introduction, section heading, result cell, summary table and "how the analysis differs" paragraph, and the README table, now give the outcome as reproduced.
- **Run times:** the README now says about 50 minutes for the notebook and about 6 minutes for the network model. `runtime_minutes` in `entry.yaml` is now 50 (it was 35). The last run took 48.4 and 5.9 minutes.
- **Verification record:** round 3 is recorded under `verifications` in `attempts/andrews-2024-01.yaml`, with the verifier's reasons in its own words and my response. The verifier also noted that the number of events often rises under light at other seeds. My response says this is a weakness in the claims file's criterion, which this attempt does not change.

**Checks:** I ran `python tools/entry.py all entries/andrews-2024` twice and it passed with 0 errors both times. The second run came after the last notebook edits. The simulation printed the same numbers as before. After the final small wording edit in the record, `entry.py check` also gave 0 errors.

Nothing is committed. The changes already present in `tools/` were there before this run, and I left them alone.
