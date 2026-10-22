No outcome changed, and none is proposed: the verifier agreed with all 15, and the new outputs support the verified outcomes. The final run of `python tools/entry.py all` passed in 25.2 minutes and `check` shows 0 errors. Nothing is committed.

**Why the verifier's numbers didn't match the text.** The executed copy it read came from a different machine (19 significant points, 2264 fits at the iteration limit, NMF errors around 97.79, 358 s, 13.7 min). Three runs on this 4-core machine all gave the numbers the text already stated: 18, 2268, 97.55 to 97.58, and about 640 s for the map. The decoder fits stop at an iteration limit and the NMF uses float32, so these counts shift slightly between machines. The ed9c Result cell now says so, and the record's round-2 entry explains it.

**Corrections:**
- **ed8:** the Result cell and the notes no longer say the active footprints are "as spread as random sets". They now say the event's spread falls inside its component's random range for 3 of the 8 components, below it for 2 and above it for 3, with the numbers.
- **Cell 15:** removed the sentence saying the AVI's byte size matches the Academic Torrents listing, since no output showed it.
- **Cell 0:** the sentence about the draft is now backed by a new data-check output: the draft holds the same assets, sizes and blob ids as the published version.
- **Timings:** the README and `entry.yaml` now say about 25 minutes (was 24). The round-1 response now says about 640 s (was 634 s).

**New output:**
- **ed9b exact-solver check (new cell 26):** the verifier's open point. With the exact solver, real decoders score 0.220 to 0.292 and shifted-label decoders 0.092 to 0.145, so the claim holds with either solver.
- **ed9c Welch t-test variant:** the verifier expected a t-test to mark fewer points; it marks more. It gives 80 of 150 significant points (range 0.079), 5 with the SGD solver, and 32 of 34 for the paper code's 64-footprint variant.
- **Round 2 under `verifications`:** each claim has the verifier's reason in its own words and my response.

**Not done:**
- **ed9c code variant grid:** the code's 64-footprint variant stays on a 60 px grid, though the claims file says 40 px. I ran it at 40 px once and the notebook took 32 minutes, over the 30-minute limit. This is now listed as a deviation in the record and noted in the notebook. No number from that run is used.
- **More decoders per point for ed9c:** the map already takes about 640 s with 10 per point, so more would not fit the time limit.
- **Paper values for Fig. 2 and ED9b:** still not compared, because the main text and the Fig. 2 legend are not available. No paper text was downloaded, so `paper/` stays empty.
- **ed2c:** no change. The record already states that it sits at the threshold, 0.003 short of 0.8.
