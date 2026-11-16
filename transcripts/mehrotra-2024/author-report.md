The attempt is recorded and checked: `entry.py check` reports 0 errors, all three notebooks ran clean from the locked environment, and the handover is built. I did not verify my own work or commit anything.

### 1. Outcomes

Only the first two claims use dandiset 000987, pinned at version `0.261003.2342`. The four published versions hold identical files and differ only in metadata, so I took the latest. The PoSub claims run on the paper's other dandiset, DANDI:000939 at `0.261016.2310`, and are counted apart (`data: elsewhere`).

| Claim | Outcome |
|---|---|
| rsc-dataset | not reproduced: 638 units (14 sessions and 3 mice match) |
| fig5f-rsc-pmr-onset | reproduced, rests on an assumption: tau = -0.275, n = 570, p = 8.1e-21 |
| fig5c-posub-pmr-onset | reproduced, rests on an assumption: tau = -0.177, n = 1,096 |
| fig5d-isomap-pmr | reproduced: abs R = 0.865 |
| fig1e-delay-range | reproduced: 5 to 100 ms (1st to 99th percentile) |
| fig1g-dv-sequence-du | reproduced, rests on an assumption: DU W = 1, UD W = 38, the paper's values |
| fig1h-ventral-down-longer | reproduced: p = 0.011 (all units), 0.0019 (excitatory units) |
| fig1b-no-dv-tuning-gradient | reproduced, rests on an assumption: HD information in bits per spike |
| figs1j-dorsal-ventral-same-hd | reproduced: all four readings p ≥ 0.05 |
| figs1i, figs1kl, figs2d | blocked, `methods_underspecified`: the readings disagree, and the criterion says to block |
| fig2f-gamma-travels | not reproduced: no reading gives both halves of the claim |
| figs2e-speed-similar | not reproduced, rests on an assumption |
| fig1j, fig1k | blocked, `other`: not attempted in the time |
| figs2g-adn-synchronous | blocked, `metadata_insufficient`: DANDI:000056 units have no location |
| fig5e-fc-pmr-onset | blocked, `not_runnable`: reading CRCNS fcx-1 takes about 85 min, over the 60 min limit |
| fig3, fig3f (model) | blocked, `not_runnable`: MATLAB |
| fig4d, figs4 (slice recordings) | blocked, `data_missing` |

### 2. What I found about the data

**Dandiset 000987:**
- It holds 638 units. 570, the number the paper and the dandiset description give as recorded, is exactly the number of units that enter the Figure 5F test.
- The description lists LFP, but the files contain none.
- Units have no waveform, cell type or depth, and every electrode position is 0, so the paper's excitatory-cell rule cannot be applied.
- `session_start_time` is the 2024 upload date in every file.
- In 9 sessions some sleep-scored NREM time falls outside the sleep epochs; in one session a NREM interval covers two whole arena (awake) epochs.
- The stored DOWN and UP states match a re-detection with the paper's code (95% to 99% matched) and share the spikes' clock.

**Dandiset 000939:**
- Unit counts match the paper exactly (1,657 units, 1,097 excitatory, 1,096 entering).
- The paper's DOWN/UP event file for session A3708-200317b does not fit that session's spikes at any time shift.
- The NREM scoring extends beyond the home cage epochs, and in 3 sessions beyond the end of the recording.
- In A3705-200306 and A3711-200810b the LFP is shorter than the spike recording. In those two and A3708-200317b, gamma power does not rise at UP onset, so their LFP may not share the spikes' clock.
- The direction of electrode depth (`rel_y`) is not documented.

**Assumptions** (each is a `deviation` with `assumed: true` in the record):
- **fig5f:** all sorted units are used; the 570 count supports this.
- **fig5c and fig1g:** A3708-200317b's DOWN/UP states are re-detected from its spikes.
- **fig1g and fig1b:** larger `rel_y` is dorsal.
- **fig1b:** HD information is in bits per spike.
- **figs2e:** speed is the slope of depth on delay, which reproduces the paper's unit speeds.

Six `methods_unavailable` findings ask the paper's authors about these choices and about Figures S1I, S1L, 2 and S2D/S2E.

**Questions to a reader:** none.

### 3. Where the protocol was unclear or missing something
1. A criterion reading that the data cannot support (fig5f reading b needs waveforms the files lack). I ran the part that could run and marked the outcome as resting on an assumption.
2. The criterion's "block when readings disagree" conflicts with step 1.6's "adopt the best-supported reading". I followed the criterion. For fig2f, where every reading fails, I recorded not reproduced.
3. No rule for a paper-supplied input that fails the clock check (the A3708 event file). I replaced it with a re-detection, showed every variant, and marked the outcome as resting on that choice.
4. No reason code for claims left untested for time when computation was not the limit. I used `other`.
5. It is unclear whether outside data looked at only to justify a block belongs under `inputs`. I listed CRCNS fcx-1 and DANDI:000056 as "examined only".
6. Findings have no field naming which dataset they concern. I named the dandiset in each statement.
7. The `not_runnable` fetch estimate can only be an upper bound when the needed files' position inside the compressed archives is unknown. I recorded it as such.
8. The claims file's UD search window (0 to 150 ms after the DOWN start) falls after the drop and cannot be tested. I added the mirror window, -150 to 0 ms, as a recorded deviation.

### 4. Runtime and failures
The final run took 22 minutes: 2.2, 6.0 and 13.8 minutes for the three notebooks. Nothing failed in it. The work ran from 23:53 to about 02:03 UTC. The fcx-1 streaming rate varied between runs (17.1 to 17.7 MB/s); the record quotes the final run's 17.4 MB/s.

Files are in `entries/000987-mehrotra-2024`:
- reproduce_mehrotra_2024.ipynb
- posub_000939.ipynb
- posub_lfp_000939.ipynb
- mehrotra.py
- README.md

The record is `attempts/000987-mehrotra-2024-01.yaml`.
