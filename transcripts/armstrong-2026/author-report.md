I've done steps 1 to 6 of the Author section and nothing is committed. The notebook passes `tools/entry.py all` (0 errors, runs in 152 s), and the handover package is in `executed/001341-armstrong-2026/handover/`. The main result is that the spike times in this dandiset are not on the trial clock, so none of the paper's neural findings can be tested.

**1. Outcomes (33 claims)**

| Claim | Outcome |
|---|---|
| table-s1-recordings | not reproduced (units 61 vs 65 and 43 vs 48; OL trials 500 vs 531 and 513 vs 609; 17 animals absent) |
| figs1-running-speed | not reproduced (503 runs at 5.9 cm/s over all samples, 13.0 in running trials) |
| fig2a-success-rate | not reproduced (0.61 to 0.69 under all 8 readings; trials run above 10 cm/s give 0.98 to 1.00, shown as a variant only) |
| fig2b-lateral-spread | not reproduced (SD at t = 0 is 0.84 vs 0.55; no 2 s or 3 s SD matches) |
| fig4-ddm-fit | partially reproduced (the GDDM has lower BIC than the DDM, but DDM NDT is 0.000 to 0.005 s vs 0.12) |
| 16 claims on spikes aligned to turn onset | blocked, metadata_insufficient |
| 12 claims on whisker, touch, wall or gait data, or on absent animals | blocked, data_missing |

**2. What was found about the dataset**
- **Spike clock:** the spikes do not share the trial clock and the files hold no sync signal.
  - At the stored onsets there is no trial-locked response, and turn type cannot be decoded from spike counts (0.46 to 0.52 accuracy), while lateral position decodes it at 0.92 to 0.96.
  - The best-aligning lag drifts from about 4 to 12 s within 489 and from 5.6 to 14.2 s in 503, and running-speed correlation gives different lags.
  - I adopted no alignment: one fitted to the neural response would set the very timings the claims test.
- **Coverage:** only animals 489 and 503 of 19 are in the dandiset, with no wall positions, whisker tracking, touch times or gait.
- **Trials table faults:**
  - In 489, rows 1000 to 1610 are copies of one row, all labelled OL_L, yet 256 of their 305 turns go right.
  - In both sessions about 60 OL rows have stop times before their start times, and their sample timestamps restart at the previous trial's start.
  - I used only the usable rows: the first 1000 of 489 and all 1027 of 503.
- **Units:**
  - Counts are below Table S1, and 489's FS/RS counts are 30/31 against Fig. 5B's 43/22.
  - Unit 489101 is FS by its 0.2 ms waveform; the paper calls it RS.
  - 503 has three units in a "WM" layer, which the paper does not use.
- **Metadata:** the file gives 489's age as P63D; its dates give 68 days (Table S1 says P68).
- **Undocumented selection:** in 503 only 27.7% of trials are running, against 52.8% in Table S1, which suggests the paper's figures rest on a selection of running trials it does not describe.
- **Assumptions and questions:** I adopted no assumptions and wrote no questions for the paper's authors or for a reader.
- **Version:** 0.260414.1316, which the paper cites and which is the only published version.

**3. Where the protocol was unclear**
1. **Unalignable streams.** It does not cover streams whose alignment could only be fitted from the response under test. I blocked those claims as metadata_insufficient and showed all the evidence.
2. **Thresholds over absent animals.** Criteria like "17 of 19" or "5 of 7" cannot be met when most animals are absent. I judged table-s1 as not reproduced because the counts present already fail, and blocked the cross-animal neural claims.
3. **Two reasons, or dependencies blocked for different reasons.** "Blocked for the same reason" does not say which to give. I gave one under `blocked_by` and the other in the notes (for example fig3-not-sensory-drive).
4. **`measured` when no reading matches.** The rule only covers several matching readings. I picked a reading and named it in the notes.
5. **Readings too slow to run.** GDDM fits took minutes each while preparing, so I fitted them on 4 of 16 readings and recorded this as a deviation. The protocol bars numbers from preparation runs, so the notebook gives no timing.
6. **Corrupted trial rows.** The protocol covers recordings deposited twice but not corrupted table rows. I excluded the rows and recorded a format_error finding.
7. **Window-edge reaction times.** These made PyDDM fail. As a standard choice I treat a maximum at the window edge as no peak and drop the trial (2 to 5 of 249).

**4. Runtime and failures**
- About 1 h 35 min of the 5 h (02:11 to about 03:46 UTC); the notebook itself takes 2.5 minutes.
- An early notebook run took 35 minutes and wrote 334 MB of PyDDM warnings from the worker processes. I fixed it by silencing warnings in the workers and cutting the GDDM readings.
- The repo root shows untracked placeholder files (`.bashrc`, `.gitconfig`, `.idea`, `scripts` and others). They are character devices created by the sandbox at 02:09, not by me, and should not be committed.

Files are in `entries/001341-armstrong-2026/`:
- `reproduce_armstrong_2026.ipynb`
- `barrel_vr.py`
- `entry.yaml`
- `requirements.in`
- `requirements.lock.txt`
- `README.md`

The attempt record is `attempts/001341-armstrong-2026-01.yaml`.
