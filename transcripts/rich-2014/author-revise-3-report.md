Round 3 is applied and recorded. `python tools/entry.py all entries/rich-2014` passes (0 errors, notebook ran in 245 s), with one catch about the schema, explained below.

**Outcome that changed**
- **fig4c-active-subsets** goes from not reproduced to **reproduced**, still marked `assumed: true`. The verifier agreed with the proposal. The assumption is now linear spacing of the simulated environment sizes (G-b), backed by Fig. S18's 0 to 50 m linear axes. I removed `proposed`. The claim's notes, its deviation and the related finding now name G-b as the assumption. The notebook conclusion (cell 99), the summary (cell 109) and the entry README say the same.
- The verifier also asked to see the matrices under G-b. Cell 98 now draws them alongside the G-a ones. All printed numbers came out the same after the re-run.
- Round 3 is recorded under `verifications` with one result: agreed, reproduced, the verifier's reason including its minor points, and my response.

**Proposals that stand:** none. This was the only one. The verifier's remaining point, that the criterion's fitted equal-rate comparison may not test the paper's statement, is already in `questions/rich-2014.yaml` for a reader. No other outcome changed.

**Schema mismatch**
- The `tools/entry.py` in this working tree is newer than the branch's `schemas/attempt.schema.json`. It requires an `about` field on findings of kind `other`, which that schema rejects. Main's schema allows the field.
- I added `about: data` to the three `other` findings. They compare the data set's values with the Methods, and the README already lists them as findings about the data set.
- To run the checks, I swapped in main's schema for the run only, then put the branch's schema back unchanged.
- Because of this, a check run on this branch with its own schema will fail on those three `about` lines. It passes once the branch is checked against main's schema.

Nothing was committed or pushed.
