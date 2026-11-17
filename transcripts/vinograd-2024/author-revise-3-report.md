Round 3 is recorded and one outcome changed, but the re-run did not finish cleanly. Two notebooks failed `entry.py all`, so the executed directory has no clean stamp.

**Outcome changed**
- `ed3h-decode-engaged-from-observed` went from partially reproduced to reproduced, resting on the seed-0 fits as ed3g's outcome does. The verifier agreed with the proposal and asked for two additions, which are both in:
  - `assumed: true` and an assumed-seed deviation worded as ed3g's.
  - Notes giving the result on the seed the sample code keeps by its R2. There both readings give p = 0.15 (M35R at 0.29 on the observation weights, M36L at 0.33 on its own), while ed3g gives p = 0.0079 for leave-one-out and fivefold.
- The `proposed` block is removed. The notebook's ed3h conclusion and summary row now match, and round 3 is recorded under `verifications` with the verifier's reasons and my response.
- The README and findings had nothing that needed changing.

**Proposals still standing:** none. ed3h was the only one, and no other outcome changed.

**Checks and re-run**
- `tools/entry.py check` reports 0 errors.
- First `entry.py all`: three notebooks passed. `cross_validation.ipynb` hit the 3,600 s per-cell limit, because this machine ran about twice as slow as in round 2 (rslds_fits took 1,663 s against 783 s).
- Second run, with `--timeout 7200`:
  - `cross_validation.ipynb` ran to completion but took 69 minutes against the 60-minute limit, so it is marked failed.
  - `rslds_fits.ipynb` failed after 26 s on a 403 Forbidden while streaming from DANDI. The same request worked when I tried it again a few minutes later.
- Every executed copy comes from the current sources and ran to completion once (rslds_fits from the first run, the other three from the second). A clean re-run would have taken about 100 minutes and ended after the 10:42 cutoff, so I did not start one. Getting a clean stamp needs a third run, with `--max-minutes` raised for cross-validation.

Nothing is committed.
