The attempt is recorded and the entry passes its checks. I made a draft branch at no point and committed nothing; the workflow commits. Of the 32 claims, 19 were tested and 13 are blocked because the data set lacks the data. Most tested claims did not reproduce, but nearly every result rests on a population that differs from the paper's: the data set has no isolation measures or waveforms, so I used every sorted cluster (except cluster 0 of each tetrode) instead of the paper's well-isolated cells.

Files: `entries/crcns-hc-16-talbot-2018/` (notebook, `hc16.py`, `entry.yaml`, `requirements.in` and lock, `README.md`), `attempts/crcns-hc-16-talbot-2018-01.yaml`. The verifier's package is in `executed/crcns-hc-16-talbot-2018/handover/`.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| unit-and-cell-counts | not reproduced (8 WT and 7 Fmr1-null mice, not 12 and 9) |
| interneuron-proportion | not reproduced (direction holds, percentages far too high) |
| place-cell-proportion | not reproduced |
| figs3-nonspatial-properties-similar | partially reproduced (firing rate differs by genotype) |
| fig2-spatial-quality-similar | not reproduced |
| tables1-place-cell-properties-similar | partially reproduced (place cells alike, interneuron rate differs) |
| tables1-nonspatial-active-pixels | not reproduced |
| overdispersion-passes, overdispersion-cells | not reproduced |
| fig4b-covariance-30-passes, fig4b-covariance-40-passes | partially reproduced |
| fig4cd-kendall-place-cells, fig4d-network-state-recurrence, kendall-nonspatial-pyramidal, kendall-quiet-states | not reproduced |
| locomotion-similar | reproduced |
| fig5b-frame-specific-ipos | reproduced, resting on an assumption |
| fig5c-ensemble-coordination | not reproduced |
| figs6-room-frame-preference | partially reproduced, resting on an assumption |
| fig1ab, fig1cd, figs1 (slice), figs4 (remapping), four fig3 claims and figs5a (LFP), four fig6/Discussion claims (avoidance) | blocked: data missing (13 claims) |

**(2) The dataset**
- **What it holds:** one zip on the bucket, under `live/`. It has 41 sessions from 15 of the paper's 21 mice, in the large box and the stationary and rotating arena. There is no small box, ring, sleep, LFP, slice or avoidance data. I recorded the version as `unversioned` with the zip's MD5 from `checksums.md5`, since CRCNS does not version and there is only one copy.
- **No way to select the paper's cells:** there are no isolation measures, waveforms or cell classes, and the files hold every cluster, including cluster 0 (unsorted spikes). Table S2 lists fewer cells per session than the files hold clusters.
- **No spatial scale:** positions are in tracker pixels, and the scale differs between box sessions. I assumed it from the tracked extent and the enclosure sizes in the Methods.
- **Sample times:** the header's sampling rate and first timestamp do not give the times of the position samples; spikes lie up to about 4 s after their sample's nominal time. Spikes are filed under the right sample, so the helper estimates each sample's time from its spikes.
- **Smaller problems:** six spike trains have one backward time step; one of five spike trains checked loses a spike where the 0-15/15-30 min copies split; and the descriptor's example header gives 58.3 samples/s where every file has 30.0.
- **Assumptions:**
  - A cluster name within a day's cut file is the same cell across that day's sessions.
  - For fig5b and figs6, place cells are those classified in the same-day stationary session. The other reading gives p = 0.21 for fig5b.
- **Question for the paper's authors** (recorded as a `methods_unavailable` finding): which recording classifies a cell, and for the rotating-arena cells, is it the stationary session or the rotating one?
- **Questions to a reader:** none.

**(3) Where the protocol was unclear**
1. It does not say what to do when the paper's cell selection cannot be applied. I tested every claim on all sorted clusters and recorded the gap as a deviation on each outcome, without blocking them.
2. `partially_reproduced` is not defined for claims of absence over several measures. I used it when some measures held and others did not (figs3, tables1).
3. `measured` has no way to say a value cannot be measured. For the isolated-cell counts I gave the nearest cluster counts and explained in the notes.
4. The clock check is written for spikes against trial tables. Here spikes and positions are in the same file, so I shifted spikes against positions and compared spatial information: the true alignment is highest in 29 of 34 sessions.
5. The handover removes markdown cells that begin "**Result:". fig4b at 30 and 40 passes share one code cell, so both conclusions sit in one Result cell.

**(4) Runtime and failures**
The run took about 30 minutes, from 04:09 to about 04:39 UTC; the notebook runs in about 80 s. Nothing failed in the final run. During the work, one editing step accidentally dropped the place-cell section; I restored it and re-ran the entry before handover.
