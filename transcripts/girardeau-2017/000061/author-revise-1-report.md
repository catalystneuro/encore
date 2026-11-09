No outcome changed in this round. The verifier's 32 outcomes all match the record: 6 reproduced, 1 partially reproduced, 3 not reproduced, 22 blocked. I re-ran the entry twice from a clean environment. It passes in 10.0 minutes, and every number the conclusions rest on came out the same both times.

**What changed in reply to the report**
- **`bla-rate-same-across-directions`** (point B1): the outcome stays blocked, but the reason is corrected. The verifier was right that the criterion gives "not reproduced" when *either* test has p < 0.05 under every reading. The all-cell test already does under both session readings (p = 0.022 and 0.0048). The one thing keeping the claim from "not reproduced" is O7 reading b, which needs position. I changed `blocked_by` from `metadata_insufficient` to `too_large`, since position could only come from tracking the raw video, the same reason the behaviour claims are blocked. The verifier gave `other`; the record notes both. The blocked counts are now 17 for missing cell types and 5 for missing position.
- **Claims of absence tested on small samples** (B2): `cen-no-reactivation`, `ripple-rate-unchanged` and `bla-int-sleep-firing` now report effect sizes against the paper's, bootstrap intervals and the effect they could detect with 80% power. None of this decides an outcome.
  - For the central nuclei, the interval of the NREM median (−2.4 to 4.1%) includes the hippocampus–BLA median of 1.96%, so that "reproduced" is now described as weak evidence of absence.
  - For the ripple rate, the data rule out a change larger than about 11% of the rate, but not a smaller one.
- **Laps include platform time** (B3): the cells, conclusions and deviations now say that reward-to-reward laps include time on the starting platform and long stops. I added a table of laps per session. Leaving out Rat08-20130708, the only session with fewer than 3 laps in a template, gives the same result (p = 0.0052, 0.0052 and 0.37).
- **Outputs the verifier asked for**:
  - **What `cell_type` marks:** a short-latency cross-correlogram check shows the column marks cells with short-latency partners of the marked sign, as the paper's identified cells would have. At p < 1e-6, 99.3% of the "excitatory" BLA units excite a partner (44% of unclassified units do). 94.4% of the "inhibitory" units inhibit one (7.9% of unclassified units do). The windows and thresholds are a standard choice, not the paper's procedure.
  - **Groups in every file:** no file contains position.
  - **Reactivation-strength inputs:** the per-rat results are now a full table, and a per-session table shows units used and left out (5 left out in all).
  - **BLA-only variant:** on the identified excitatory units, EV is above REV in 4 of 5 sessions, p = 0.44; five sessions cannot reach p < 0.05 at all.
- **New finding** (B5): the archive's asset metadata is the files and the loader is right. It lists raw voltage (`ElectricalSeries`) and the processing module for exactly the files that lack them, and not for the ones that have them, in all 40 files.
- **Points left as they were:**
  - B6: the mapping of Rat08–Rat11 to the paper's rats 1–4 was already recorded as an assumption.
  - B7: I did not apply M3's rule of dropping spikes after the last run epoch. The helper's docstring now says why: those spikes never fall in any bin the analyses use.
- The round is recorded under `verifications` with the verifier's reasons and my response for each claim. The README and the notebook summary are updated.

**Not done, and why**
- `python tools/entry.py all` stops at the check step with 29 errors, all about the earlier record (`-01`), which the protocol says must stay as it was. They were there before my changes, so I ran `run` separately, as the earlier rounds did. The check reports nothing about this attempt's files.
- My first run timed out after 60 minutes because the new step that lists each file's contents walked the whole file over the network. I limited it to the few levels that matter and re-ran.
- Measuring video streaming again gave a slower estimate for tracking: 216 hours, against 234 before. The README and the record now say 216.
- Nothing is committed, as instructed.
