Round 1 is answered and the record is updated. The one outcome change is split-half-reliability, from partially reproduced to reproduced, marked seed-sensitive. The entry was re-run and passed in 77.5 minutes. That run used `--max-minutes 80 --timeout 4800` (the workflow's settings), because the default 60-minute limit timed out during the file-extraction step. 78 minutes is also over the protocol's 60-minute target.

**Change of outcome**
- **split-half-reliability → reproduced, `seed_sensitive: true`.** The criterion says "random (seed 0)" for the fallback split, and that seed decides which cells enter the pool. Seed 0 is now the main result, and the claim's own seed and seeds 1000 to 4000 are shown as variants.
  - Under seed 0 this attempt gets exactly the paper's 3,598 cells, checked cell by cell against the paper's published list (0 differ). The splits are 3,112 odd/even, 128 interleaved and 358 random.
  - Every value is within tolerance: within 0.1090, chance 0.002581, adjusted 0.1064, same-pool 0.02537, 0.02411 and 0.02011 on pools of 3,276, 3,509 and 3,351 cells.
  - Other seeds give pools of 3,256 to 4,100 cells.

A deviation in the record explains why seed 0 is used for the split.

**Added in reply to the report**
- **A_t claims (table2-alignment-ttype, ttype-beyond-cre):** both outcomes stay partially reproduced, as the criterion judges A_t itself.
  - The notebook now prints A_t minus its null mean for every seed. This is stable (0.0280 to 0.0284, 0.0265 to 0.0287, 0.0163 to 0.0182).
  - It also repeats the paper's code's own random draws under its seed 0, on this attempt's scores and on the paper's published scores. On the paper's scores A_t comes out at 0.0368, 0.0318 and 0.0105, not the printed 0.0214, 0.0250 and 0.0213. But A_t minus null mean there equals the paper's own printed difference (0.0264, 0.0266, 0.0166).
  - So the printed A_t carries an offset that depends on how the machine's sort orders tied ranks. The earlier mismatch between the record and the executed copy (0.0337 against 0.0336) comes from this, since the two runs were on different runners. I revised the record's finding on A_t to say so.
- **wgcna-mobility-within-type:** the two counts that need no count matrix are computed from the paper's join: 3,906 and 3,902, the paper's values. The claim stays blocked.
- **IPFX version:** the notebook now prints it (2.1.2), with numpy and the CPU's sort features.
- **Record:** the round-1 verifications are recorded for all 30 claims, plus small corrections (the within-Cre A_t is now 0.0314) and an updated finding on how the seed sets the split-half pool.

**Not done, and why**
- **Notebook edited after the run:** I updated the conclusion cells and summary to match the new numbers, edited `entry.yaml` (runtime 78), and gave the new cell an id. I made the same text changes in the executed copy, whose outputs are unchanged. Because of these edits the saved run no longer matches the entry, so the next `entry.py run` will run everything again (about 78 minutes). `entry.py check` passes and the handover is rebuilt.
- **Transcriptomic claims:** still blocked. The NeMO server gave a 502 and two time-outs again. I kept `blocked_by: other`, because the matrix is public and only its server did not answer; the verifier's `data_missing` is recorded as a disagreement on the reason.
- **Not changed:**
  - pair-tag-threshold-sensitivity: the verifier found its reading lenient but not a misreading, so it stays.
  - The Allen-pipeline variant of feature extraction: not run, because every count and feature list already equals the paper's.
  - No questions added to `questions/yang-2026-flexible.yaml`: the verifier reported no misreading of the paper.
- **Cell order:** this attempt's cells are not in the same order as the code's score files. So the code-draw variant does not use exactly the paper's pairs; this is stated in the notes.

Nothing is committed.
