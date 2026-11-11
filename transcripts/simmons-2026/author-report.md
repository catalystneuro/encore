I've finished steps 1 to 6 (entry, lock, check and run, record, handover), and nothing is committed. Of the 39 claims, 21 were tested and 18 are blocked; `entry.py all` passes and the notebook runs in about 10 minutes.

**1. Outcome per claim** (dandiset 001777, version 0.260521.2201)

| Claim | Outcome |
|---|---|
| fig1c (quinpirole reduces the GPe IPSC) | reproduced: −30.1%, P = 0.0087, n = 5 |
| fig1e (paired-pulse ratio rises) | reproduced: up in 5 of 5 cells, P = 0.013 to 0.022 |
| fig2c (quinpirole attenuates the train's inhibition) | not reproduced: 56.8 vs 42.3% inhibition, Wilcoxon P = 0.11 |
| fig2b (inhibition wanes during the train) | reproduced: 4.3 vs 11.9 Hz, 8 of 8 cells |
| fig3a (quinpirole raises the rate by about 50%) | not reproduced, under both possible cell sets |
| fig3b (gabazine raises the rate by about 25%) | partially reproduced, assumed: about +9%, P = 0.047 under one reading |
| figs1 (gabazine effect vs basal rate) | not reproduced: R² = 0.004 vs 0.11 |
| fig4a (GPe Gi-DREADD reduces the evoked IPSC) | not reproduced: no significant reduction under the mean or the median of sweeps |
| fig4b, fig5e, fig5g, fig5h, fig6a, fig6e, fig7e, fig7f-occlusion (claims of no effect) | reproduced (fig4b assumed) |
| fig5d (shRNA neurons fire faster) | reproduced, assumed |
| fig5f (ALDH inhibitors raise the rate) | not reproduced: P ≥ 0.39 |
| fig7d (astrocytic Gi-DREADD raises the rate by 28%) | reproduced, assumed: +30.2%, P = 0.029 |
| fig7f-snap5114 (decrease of 23%) | partially reproduced: −11.7%, P = 0.005 |
| fig7h (NNC-711 raises the rate by 36%) | reproduced: +36.0%, P = 0.004 |
| 16 claims, including fig6c | blocked, data_missing |
| fig6d, figs5 (outside data) | blocked, `other` |

**2. Dataset, assumptions and questions**
- **What the files say about themselves:** each file's conditions (virus, drugs, which file is control and which is drug) are only in free-text `notes`. The light and electrical stimuli are not stored.
- **Duplicates:** 16 files are deposited twice (the `obj-` pairs).
- **Notes that don't match their files:**
  - The nine files 0015–0023 of subject 9019 carry another cell's notes.
  - File 0007 of subject 8952 and file 0000 of subject 6813 are not named in their own notes.
- **Subject ids:** 6806, 6813 and 7321 have recordings on dates 4 to 32 days apart. Slice experiments are terminal, so the ids were reused or the dates are wrong.
- **Temperature and holding potential:** the notes give 30 C for every file (the paper says 32–33 C). They give −50, −55 and −70 mV for the IPSC cells (the paper says −60 mV).
- **Missing data:** no SNc, SCH39166, NPPB, Gq-DREADD, gabazine-then-quinpirole, low-glucose or room-temperature recordings, and no imaging, RNAscope or voltammetry.
- **Counts:** 49 gabazine-alone cells against the paper's 45, 3 disulfiram cells against 5.
- **Paper link:** the dandiset links only the bioRxiv preprint.
- **Assumptions:**
  - Spike threshold of 8 noise units; four outcomes change at 6 or 12, and those are marked assumed.
  - The drug's application time is taken as the start of the file the notes name.
  - The controls for Fig. 5D/5F are the gabazine-alone cells, since none are labelled.
  - The 9019 second cell's file layout is assumed (variant only).
- **Questions for the paper's authors** (recorded as a methods_unavailable finding):
  - What were the Clampfit detection settings, and how was the stable window chosen?
  - Which 18 cells are the controls in Fig. 5D and 5F?
  - Which 8 cells form Fig. 3A?
- **Questions to a reader:** none.

**3. Where the protocol was unclear or missing something**
1. **Dependency rule:** fig6c depends on figs3, so the rule blocks it even though its own 8 SNr cells are in the dataset. I blocked it and said the data are present.
2. **Unpinnable outside data:** an `elsewhere` claim whose source can't be pinned (Dopabase has no version) has no blocked_by reason. I used `other`.
3. **Outside data not tried for lack of time:** no category fits. I used `other` for fig6d and figs5 and said why.
4. **Lock writes a field the schema rejects:** `tools/entry.py lock` writes `python:` into entry.yaml, and the schema rejects it. The cause is the uncommitted change to `tools/entry.py`. I deleted the line by hand, and every later check passed.
5. **Is a free choice an assumption?** It is unclear whether a method choice the claims file leaves to the author, like the spike threshold, counts as an assumption. I set `assumed` wherever the outcome changes with the threshold.
6. **Partial or not reproduced:** the protocol doesn't say which applies when a test is significant but the size is out of tolerance, or the direction is right but not significant. I used partially for the first and not_reproduced for the second.
7. **Control window:** claims-file reading M1(b) defines no window for the control condition. I used all control episodes.
8. **Clock check:** there are no trial tables or stored stimuli, so I checked timing from the responses (spiking falls during the train in opsin cells only, and IPSC onsets are consistent).

**4. Runtime and failures**
The run took about 1 h 30 min, from 23:31 to 01:01 UTC. My first metadata survey of all 412 files hung for 30 minutes because I ran it untimed with threads. I re-ran it with processes and timeouts, and it took 80 s. An early dead time of 2 ms counted each spike twice; it is now 4 ms. Nothing else failed.

Files are in `entries/simmons-2026/`:
- `reproduce_simmons_2026.ipynb`
- `snr.py`
- `README.md`

The attempt record is `attempts/simmons-2026-01.yaml`, and the handover package is in `executed/simmons-2026/handover/`.
