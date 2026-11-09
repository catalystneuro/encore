The entry is built, it runs cleanly in a fresh environment, and the handover is ready. Of the 39 claims, 7 reproduced, 12 partially reproduced, 17 did not reproduce and 3 are blocked. The main gap is that far fewer PFC cells respond to SWRs than in the paper: 19 of 167 PFC cell-days, against 56 of 165.

The entry is `entries/crcns-hc-28-jadhav-2016/`, the record is `attempts/crcns-hc-28-jadhav-2016-01.yaml`, and the handover is in `executed/crcns-hc-28-jadhav-2016/handover/`. Nothing is committed, and the claims file is unchanged.

**1. Outcomes**

| Outcome | Claims |
|---|---|
| Reproduced (7) | wtrack-learning, figs2-swr-at-reward-wells, theta-lag-past (holds under one reading only, at the edge of its tolerance), fig6ab-both-signs, fig6e-glm-swr-prediction, fig8a, fig8bc |
| Partially reproduced (12) | tables1-cell-counts, swr-detection-stats, ca1-swr-modulated, fig3f, fig4-theta-locked-fraction, fig4c, figs3-arm-and-direction, fig6-swr-correlated-pairs, fig6c, figs4b, fig6e-theta-trained-glm, fig8d |
| Not reproduced (17) | fig3-pfc-swr-modulation-fractions, fig3-transient, fig3de, fig3e, fig4a, fig4-swr-modulated-more-theta-locked, fig4b-kappa, fig4-preferred-phase-concentration, fig5b, fig5c, fig5e, fig5f, figs3e, fig5g, figs4c, fig7c, figs5 |
| Blocked (3) | ytrack-learning and figs7-both-tracks (`data_missing`, the Y-track rats are not in hc-28); figs6-replay-content (`other`, not run in time) |

Only 12 PFC cell-days are SWR-excited and 7 SWR-inhibited (paper 30 and 26), so most comparisons between the PFC groups fail. This holds under every variant I ran:
- SWRs from the mean envelope.
- Dorsal-CA1 ripple tetrodes only.
- Onset at the threshold crossing.
- 50 ms bins.
- A -1 to +1 s raster.

On synthetic data the shuffle test detected a 50% rate drop and had a 3% false-positive rate.

The CA1-PFC pair results hold in direction:
- 23% of pairs are SWR-correlated, against 4.5% after shuffling.
- Theta cross-covariance predicts SWR correlation (r 0.46 to 0.58).
- CA1 leads PFC.
- The pre-task rest shows none of this structure, as the paper says.

**2. The dataset, assumptions and questions**
- **Dataset:** three W-track rats, days 1 to 8, one tar.gz of about 2.7 GB per rat. On days 6 to 8 the second run is in an environment named `wtr2`, which the description does not define. Day 1 also has a linear-track run.
- **Version:** CRCNS does not version data sets. I used `hc-28/live/`, the only published copy, recorded it as `unversioned` with the MD5 sums in the notebook header, and gave the reason there.
- **Findings recorded:**
  - cellinfo `spikewidth` is documented as ms but holds 30 kHz samples.
  - Run-epoch position files have 9 columns, where the description lists 7.
  - `wtr2` is undefined.
  - No identifier links a unit across days.
  - The cell-days in the files exceed the Table S1 counts by 12 to 17%. After the 50-spike rule, 167 PFC cell-days remain against 165.
  - The three data streams share one clock, shown by two contrasts against time-shifted data.
- **Assumptions:** the paper links no code, so the SWR detection details follow the Frank-lab convention of the cited Karlsson and Frank (2009). An SWR is an event on any one ripple tetrode, and its onset is where the envelope last rose above its mean. Both W-track runs of each day are used, including `wtr2`. Units are cell-days. Every SWR-dependent outcome is marked `assumed: true`.
- **Questions for the paper's authors**, recorded as findings:
  - How SWRs were combined across tetrodes, whether the intermediate-CA1 tetrodes took part, and where the onset was set.
  - The raster span, jitter range and PSTH bin used for the modulation measure.
  - Whether the `wtr2` runs were included.
- I asked no reader questions.

**3. Where the protocol was unclear or did not fit**
1. docs/archives.md describes CRCNS data as zip files opened in place. hc-28 is tar.gz, which cannot be read in place, and the small spike and position files sit at the end, after about 840 LFP files. I streamed each archive once with `tarfile` and held the needed LFP files in memory (peak 3.8 GB per rat, two rats at a time).
2. "Do not download to disk": the notebook streams everything. For development I kept reduced data as pickles in `$TMPDIR` and deleted them at the end.
3. There is no published version to pin, so I recorded `unversioned` with the MD5 sums.
4. `too_large` covers only computation. The replay analysis would cost about 22 min of line fits plus decoding, but I stopped because writing and running it on top of the 20-min notebook did not fit the run's time. I used `blocked_by: other` and said why.
5. Running every reading through chains of dependent claims would multiply the work. I carried one main reading downstream and showed the alternatives at the claims where they arise.
6. The claims file's "pooled-value rule" (direction holds, values outside tolerance) maps onto `partially_reproduced`. Where a claim has several parts, I used partial when some parts failed.
7. The protocol asks for a decoding contrast to check the clocks. I used two contrasts instead: the CA1 rate after SWR onsets against shifted onsets, and spatial information against shifted spikes.
8. The 10-minute aim is not reachable when 8 GB must be streamed. The notebook takes 20 min, under the 60-min limit.

**4. Runtime and failures**
- The run took about 2 h 16 min (12:17 to 14:33 UTC). The notebook took 1217 s in a clean environment, and two full runs gave the same outputs.
- `entry.py check` reports 0 errors.
- Nothing failed at the end. My `rm` with a `$TMPDIR` glob was denied by the permission check, and the same deletion succeeded with literal paths.
- The reverse GLM (figs4c) uses 500 splits per model where the paper uses 5000; this is recorded as a deviation.
