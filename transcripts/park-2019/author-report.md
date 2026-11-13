I've finished the attempt and run `tools/entry.py handover`. The entry is at `entries/park-2019/` (`reproduce_park_2019.ipynb` and `hd20.py`), the record at `attempts/park-2019-02.yaml`, and `tools/entry.py all` passes with 0 errors. I didn't verify it myself, and I didn't come across any earlier attempt's results.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| cell-counts | partially reproduced: 115 head-direction units from 13 rats as in the paper; the 353 MEC cells and 556 pairs are not in the data |
| hd-cell-rate | reproduced (1.392 AP/s) |
| fig1a-avoidance-learning | blocked, data_missing |
| fig1c-speed | reproduced |
| fig1c-lfp-power | blocked, data_missing |
| fig1c-firing-rate | reproduced (F(1.35, 154.10) = 1.76, p = 0.18) |
| fig1c-directionality | partially reproduced: rotating room frame not below stable2 at p < 0.01 (p = 0.055) |
| fig1d-preference-change | partially reproduced: stable1-arena change is the largest, where the legend puts it lowest |
| fig1d-instability | partially reproduced: 2 of 3 trial pairs exceed the stable1 halves |
| fig2-decoding-stable-vs-rotating | reproduced (assumed) |
| figs2-frame-preference | reproduced under 1 of 16 readings (assumed) |
| fig2c-proximity-anticorrelation | partially reproduced: mean r −0.05 to −0.09, against −0.141 |
| figs3-no-head-direction-bias | reproduced (assumed) |
| fig3-hd-pair-correlations-preserved | reproduced |
| figs4, figs5, figs6 | blocked, data_missing |
| no-angular-velocity-tuning | not reproduced (assumed) |
| fig4-internal-tuning-preserved | not reproduced (KLD across trial pairs p = 5.3e-05) |
| fig4c-arena-registration-short-lived | partially reproduced |
| fig5-error-inhomogeneous | partially reproduced |
| fig5c-error-minima-at-cues | reproduced under the pooled reading (assumed) |

**(2) The dataset**

- **What it holds.** Only the 115 head-direction units, in 44 sessions. There are no other MEC units, no LFP, no waveforms and no training sessions. The CRCNS data set is unversioned, so I pinned it by the MD5 of `data.zip` (`b82c7b97…`).
- **Shifted file list.** In `FileNameList.xlsx`, the stable2 column of session 1121R157 is shifted by one row for five units. I matched units across trials by file name instead.
- **Duplicated tracking.** Two pairs of trials from different days have identical tracking with different spikes: stable2 of 1015R029 and 1025R029, and the room-frame rotating trial of 1211R039 and 1212R039.
- **Wrong spikes in one file.** The stable1 file of 1024R157-P9C1 holds the spikes of its rotating trial.
- **File-level problems.**
  - One header states 2000 samples/s.
  - One stable2 file lasts 15 min.
  - One spike train has a 1.5 ms backwards step.
  - One tracker file is named for the wrong rat.
- **Undocumented conventions.** Untracked samples (direction 4294967295, 4 to 73% of a file) are not described. Nor are the y-up angle convention of the shock zones or the drift of up to 3 s between spike times and nominal sample times.
- **Differences from the paper.**
  - The per-rat counts differ from Table S1 for R029 (40 vs 41) and R523 (2 vs 1).
  - Two units fire above the paper's 10 AP/s limit.
  - The units form 146 pairs, against the paper's 142; 142 of them have a defined 5 s curve in every condition.
- **Assumptions:**
  - figs3: n in the weighted Rayleigh test is the sum of the weights (CircStat's convention).
  - fig2c: proximity is measured to the centre of each shock zone.
  - fig2 and no-angular-velocity-tuning: they rest on the claims file's own assumed rules.
  - figs2 and fig5c: each matches under only one of the readings the criterion lists.
- **Questions for the paper's authors** (recorded as `methods_unavailable` findings):
  - How Idir and ΔIdir are computed.
  - How relative proximity is defined.
  - What n the Figure S3 Rayleigh test uses.
  - Which normalisation, strength measure and window side the internally referenced tuning uses.
  - Which windows are pooled in Figure 5, and which measure Figure 5C plots.
- **Questions to a reader:** none.

**(3) Gaps in the protocol**

1. For a claim of absence, the protocol says to judge on the paper's test alone, but figs3's test has two readings the criterion itself lists. I treated this under step 1.6 (adopt the best-supported reading as an assumption).
2. Criteria that say "reproduced under any reading" can pass on 1 of 16 or 1 of 32 readings (figs2, fig5c). I followed the criterion, set `assumed: true` and gave the counts.
3. Some results fit neither the criterion's full form nor its partial form (fig1c-directionality, fig1d-instability, fig4c). I recorded them as `partially_reproduced` under the protocol's general definition.
4. The schema requires `deviations` on every outcome with `assumed: true`; the protocol doesn't say so. I added them.
5. Each `measured` value must be a number, so for counts the data set cannot hold I gave what it holds (115 units, 146 pairs) and explained in the notes.

**(4) Runtime and failures**

- The notebook takes about 6 min (350 s) and the whole run took about 57 min.
- Two bugs I found and fixed during development:
  - NaN handling in the ported decoder, caught when stable1 decoding of itself came out at chance.
  - A missing argument to the internal-tuning function.
- An empty `entries/park-2019/.claude/` directory, created by the harness, is still there. Removing it needed approval this session can't give. It holds no files, so git won't pick it up.
