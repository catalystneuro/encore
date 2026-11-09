No outcome changed. All 20 stay as the round-2 verifier agreed: 8 reproduced, 5 partially reproduced, 1 not reproduced and 6 blocked. Nothing went under `proposed`, because none of the new checks pointed to a different outcome. I re-ran with `python tools/entry.py all entries/000727-brezovec-2022`: the check passed with 0 errors and the notebook ran without error. All the other numbers I spot-checked came out the same as in round 2.

**Corrected or added**
- **fig2-symmetry, flip check:** I removed the brain-mask-against-its-mirror overlap. As the verifier said, a left-right flip doesn't change that overlap, so it can't detect one. Each fly is now compared with the pooled maps of the other eight flies, both as is and mirrored.
  - No fly matches the mirrored maps better for both left and right turns; 7 of 9 match better unmirrored for both.
  - fly_099's left-turn map matches the mirrored map slightly better (0.158 against 0.190), but its right-turn map clearly does not (0.439 against 0.199).
  - For fly_105 the check doesn't decide (left turns 0.274 against 0.234, right turns 0.212 against 0.214). The notebook and record now say a flip of that fly can't be ruled out. The outcome is based on the pooled maps and is unchanged.
- **fig6-peak-time-range:** I corrected my round-1 response. It said the lag of more than 1 s holds in every plane from 38 on, but it holds only in planes 59 to 73; from plane 38 on the lag is at least 0.84 s. The notes now say that only the lag of more than 1 s holds up under the alternative timings, and that the earliest-lead part can't be tested with the timing the dandiset gives.
- **fig6fg, cell 61:** the plane ranges now match the output: 0.26 to 0.33 s in planes 17 to 38 for left turns, and 0.19 to 0.29 s in planes 17 to 59 for right turns.
- **Run times, which vary between runs:** the README now says 12.3 minutes in the latest run and 7.3 in the run before. The figs4a notes now say 306 s and 214 s to stream the 12 planes, each including about 40 s of metadata.
- **Round-1 record:** I added the verifier's point B7 (the clock-check null wasn't comparable) under dataset-structure, with the fix, and its fly_105 remarks from B6 under fig2-symmetry.
- **Round 2 is recorded under `verifications`** for all 20 claims, with the verifier's reasons in its own words and my responses.

**Not done**
- **figs4a partial sweep on the 12 planes:** still not attempted. It would need every voxel's time series held in memory, about 3 GB per plane, and the streaming keeps only block means and per-voxel sums. The claim stays blocked.
- **Alpha selected on the test folds (B8):** left as it is, because the verifier says it doesn't bear on a conclusion.
- **Notebook outputs:** I edited the conclusion text of cells 26 and 61 after the run, so the executed copy has the old wording in those two cells. Only text changed, so the outputs are the same.

Nothing is committed. Some untracked files in the working tree (`.bashrc`, `.idea`, `scripts` and others) aren't from this run, and I left them alone.
