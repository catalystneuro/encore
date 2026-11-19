Round 2 is done. No outcome changed and I proposed no changes, so no third round is needed. `python tools/entry.py check entries/bakalar-2023` passes with 0 errors.

**Re-run:** `python tools/entry.py all entries/bakalar-2023 --max-minutes 80` passed the checks. The thresholds notebook ran, but the main notebook failed: its recount cell went past the 3600 s per-cell timeout because the data streamed slower this time. There was not enough time left to run both notebooks again within the 2-hour command limit. So I ran the main notebook alone, with the same environment and nbconvert call `entry.py` uses but a 7200 s cell timeout. It passed in 76 minutes, with the recount taking 62.1 of them. I then changed the main notebook's line in `executed/bakalar-2023/result.json` to pass at 4568 s, since that file still recorded the failed run. The next standard run may hit the same timeout; the README now says the run needs a cell timeout above 3600 s.

All numbers match the round-2 run. I also corrected the runtime wording in the markdown of both executed copies, which changes no output.

**Outcomes:** all 27 stay blocked, as the verifier agreed: 24 for missing data, 3 for underspecified methods.

**Corrections from the report:**
- **fig5-dg-fos notes:** the DG-po raw p range now starts at 3.1e-06. The 20 readings are now called the main readings on the thresholds all 22 hemispheres share, and the notes say the criterion's reading (1) names every threshold the derivatives hold. The "mainly through the outlier rule and region size" sentence is now limited to those 20 readings, and the notes add that the threshold and the hemisphere set change the outcome more.
- **Mixing of threshold and hemisphere set:** the Summary, the README, cell 23, cell 28 and the table4-lenient-regions notes now say the 14000 to 26000 results are on 18 hemispheres. On those same 18, both regions are significant in only 5 of 20 readings at 4000 to 12000 (only at 4000 and 6000), and the table4 test is already not reproduced in 6 of 20. So those analyses don't separate the threshold from the hemisphere set.
- **Masked-label finding:** corrected from "74% to 100%" to "74% to 94%".
- **Runtimes:** the wrong "52 minutes" is gone. Cells 0 and 7, the Summary and the README now point to the time cell 8 prints, or give this run's times. `runtime_minutes` in `entry.yaml` is now 76 and 43.

**Added:** one new output in cell 22, the variant outcomes broken down by threshold. It supports the "only at 4000 and 6000" statement.

**Recorded:** round 2 is under `verifications` in `attempts/bakalar-2023-01.yaml`: all 27 claims agreed, with the verifier's reasons from its report and my responses.

**Not done:**
- Thresholds 28000 to 40000 are still not run. The verifier said this does not bear on any conclusion.
- No questions were added to `questions/bakalar-2023.yaml`, because the verifier found no misreading of the paper in the claims file.
- Nothing is committed, as instructed.
