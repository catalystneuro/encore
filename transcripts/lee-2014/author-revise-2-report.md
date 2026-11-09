No outcome changed. All 34 still match what the round-2 verifier agreed with (4 reproduced, 1 partially reproduced, 27 blocked as data missing, 2 blocked as too large), and nothing is under `proposed`. The entry was re-run three times with `python tools/entry.py all`; the last run passed, and `entry.py check` gives 0 errors.

**Corrected or added, by the report's points:**
- **Model timing (fig4d, fig4ef):** the timing is not stable between runs. The three runs this session gave 8.01, 8.24 and 8.20 s per simulated ms, down from the 11.4 to 12.4 s of the earlier runs. Cell 32 and the summary now give rounded values that cover all three runs: about 8 s per ms, 11 to 12 hours per 5 s run, about 450 core-hours. The record notes give the final run's exact numbers: 509.9 s to build the network, 8.20 s per ms, about 11.5 h per run, 450 core-hours. If the workflow's own re-run is again much slower, those numbers will need updating, but the block itself holds at any of the timings seen.
- **NEURON version and 64-core job scripts:** cell 31 now prints both: NEURON 9.0.2, and 75 job scripts that each use `mpiexec -np 64`.
- **PV37:** cell 8 now prints PV37's deflections. They show the sweep order breaks between −250 and −200 pA (−8.7 then −9.1 mV), not between −300 and −250 as cell 9 said. Cell 9 and the record's finding are fixed.
- **sh108_BC:** I removed the unsupported "from Lee et al. (2010)" from the fig5 note. It now says only that the cell is from another paper.
- **README:** the run time now reads about 12 minutes.
- **Round-1 reasons:** the PV34 example (14.9 against 2.0 Hz at +350 pA) is restored in the figs1e reason and added to the figs3f reason.
- **Round-2 record:** added under `verifications`, with all 34 claims agreed and the verifier's reasons and my responses.

**Not done:**
- The round-1 responses still carry the old timing numbers (537 s, 12.39 s/ms, 677 core-hours), because they describe the run of that round. The round-2 response says this.
- `runtime_minutes: 15` in `entry.yaml` is unchanged; the runs this session took about 12 minutes.
- No reader question was added, since the verifier found no misreading in the claims file.
- Nothing was committed, as instructed.
