**Verifier report, round 1: Tingley and Buzsáki 2019 (doi:10.1016/j.neuron.2019.10.012) on DANDI 000218, version 0.250624.0439**

I read the paper from the PMC author manuscript, saved under `paper/`. The attempt record was not among my materials, so the claim count comes from the claims file (31 claims) and the outcomes below are mine. Two leftover files in `paper/` are error pages from failed downloads (`PMC6952543_bioc.json`, `PMC6952543.xml`). Deleting them needed approval, which this session could not give, so they are still there.

My tally: 4 reproduced, 7 partially reproduced, 10 not reproduced, 10 blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| dataset-composition | partially_reproduced | Cell 13: 6 animals. Three counts are within tolerance: LS neurons with more than 50 spikes in high-power epochs, 2046; CA1+LS recordings by units, 37; recordings with LS electrodes, 94. Two are out: CA3+LS is 10 under both readings (the archive holds only 10 files with `ca3` electrodes), and CA1-rate recordings are 40, 72 or 43, against 53±5.3. That is 3 of 5. |
| fig1c-hfo-each-animal | not_reproduced | Cell 15: median frequency is between 152 and 158 Hz in all 6 animals. LS firing at HFOs exceeds random times by more than 3 SEM only in DT1; it is lower than at random times in DT7, DT8 and DT9. NREM-only events: 2 animals pass. |
| fig1c-event-count | reproduced | Cell 19: reading (b), recordings with LS units, gives 31,984, within 29,955±2,996. Reading (a) gives 67,186. DT7 contributes most events, so the agreement on the total is probably coincidental. |
| figs1-participation | not_reproduced | Cell 21: fraction of neurons firing 0.027 and spikes per event 0.051 (pooled), or 0.035 and 0.068 (per recording), against 0.16 and 0.23. |
| fig1d-phase-locking | partially_reproduced | Cell 23: 56.3% of tested neurons, or 47.0% of all, are phase-locked, against 92.5±9.25%. The trough preference holds: mean phase 189°, Rayleigh p≈0. DT7 has only 5.7% locked. |
| fig1f-shorter-than-ripples | reproduced | Cell 25: LS 33.9 ms against CA1 38.3 ms; both within the paper's SDs; rank-sum p≈0. Two caveats: in DT8 there is no difference (p=0.83), and with NREM events only the means are 38.0 and 38.4 ms. |
| fig1g-slower-than-ripples | not_reproduced | Cell 25: LS HFOs are faster than CA1 ripples, 153.6 against 150.8 Hz (opposite direction), in 4 of 5 animals; both means are out of tolerance. |
| fig1h-no-amplitude-frequency-correlation | not_reproduced | Cell 27: Pearson r=0.056, p=2.4e-47 over 67,186 events. This verdict follows the criterion; the effect is negligible and 2 of 6 animals are not significant. |
| fig2-confined-to-ls | not_reproduced | Cell 29: LS has the highest ratio in 2 of 5 eligible recordings, all from DT7. Medial septum, corpus callosum and fimbria ratios are about as high as LS (for example cc 50.1 against LS 42.0; sFi 72.1 against LS 64.8). |
| fig2ef-intermediate-ls | blocked (metadata_insufficient) | Electrode x, y and z are NaN in every file (cell 4), and the LS borders come from histology, which is not in the files. Partly testable: each session name carries the drive depth (for example DT1 1584 to 2736 µm), so HFO power and phase-locked fraction could be plotted against depth within each animal. Not done. |
| fig3-travelling-waves | blocked (metadata_insufficient) | No site coordinates, probe model or probe orientation in the files. I agree. |
| fig4b-pre-post-unchanged | reproduced | Cell 33: rank-sum p=0.81, POST−PRE median −0.0001. Low power: 106 pairs in 3 animals, against 7,172 in the paper. |
| fig4b-hfo-above-behav | reproduced | Cell 33: PRE>BEHAV p=9e-24, POST>BEHAV p=4e-25, PRE and POST above jitter p<1e-30. Same 106 pairs. |
| fig4-sessions-few-change | blocked (other: too few recordings after the pair selection) | Cell 34: 7 recordings with at least 5 pairs, 0 significant. The archive has the spikes, epochs and trials; the shortfall comes from the reproduction's own HFO detection (problems 1 and 2). |
| fig4c-temporal-bias | blocked (other: same as above) | Cell 35: 4 recordings, p=0.805. A claim of absence tested on n=4 tells us nothing. |
| fig4d-compression | not_reproduced | Cell 36: PRE exceeds chance only at factors 1 and 2 (factor 4: p=0.18 on 24 pairs). The criterion needs every factor up to 20, or up to 5 for partial. Low power. |
| figs2-post-rate-increase | partially_reproduced | Cell 38: LS rates rise (median POST/PRE 1.06, p=8e-7). `hpc` (0.998, p=0.52) and `ca3` (1.03, p=0.22) do not. |
| fig5b-nrem-and-rates | partially_reproduced | Cell 40: the LS HFO rate is below the CA1 ripple rate in NREM (p=3e-6). But NREM is not above WAKE: medians 0.006 and 0.010/s, NREM lower in 29 of 47 recordings, p=0.44. |
| fig5d-lag | not_reproduced | Cell 42: the median lag is 0.00 ms under both readings, against 6.4±4.2. 35% of pairs fall on the same sample. The CCG peak criterion holds (166 SD above the flanks, at 0 ms). |
| fig5e-state-coupling | not_reproduced | Cell 42: NREM 0.199 against WAKE 0.116, t-test p=0.089, short of p<0.001. Pooled values are 0.088 and 0.041. |
| fig5f-ripple-triggered-firing | not_reproduced | Cell 44: 1.39 against 1.33 Hz, paired p=0.24. The variant normalized by state rate goes the other way (WAKE higher). |
| fig5f-no-phase-coherence | not_reproduced | Cell 44: PLV at the ripple time is 0.405 against a jittered 0.202±0.007, 30.7 SD above. See problem 1: the jittered baseline itself is abnormally high. |
| fig6-optogenetic-hfos | blocked (data_missing) | Agree. Archive metadata lists 6 subjects and no optogenetic series (variableMeasured holds LFP, Units, Position, ElectricalSeries, SpatialSeries, CompassDirection). The 2 optogenetics rats are absent. |
| fig7e-ca1-spikes | partially_reproduced | Cell 46, reading (a): 79.4% against 38±3.8, chance 4.7%, binomial p≈0. |
| fig7e-state | partially_reproduced | Reading (a): 34.3% against 26±2.6, chance 5.4%. |
| fig7e-duration | partially_reproduced | Reading (a): 86.0% against 20±2, chance 5.9%. This size comes largely from the counting window (problem 3). |
| fig7e-ca1-depth | blocked (data_missing), not verified | It needs per-unit waveform amplitudes across sites. The notebook never lists the units-table columns, so I cannot confirm they are absent. |
| fig7e-replay | blocked (methods_underspecified) | Defensible for the two Bayesian scores, but partly testable: asset metadata shows Position in 74 files (DT2, DT5, DT7, DT8, DT9), and replay score 1 (rank-order correlation against maze rate maps) is reasonably well defined. The notebook does not mention the position data. |
| fig7e-seqnmf | blocked (methods_underspecified) | Agree; the Methods give only the 40 templates. |
| fig7e-content-independent | blocked (other: depends on blocked claims) | The content-independent half shows all features above chance under (a); the content-based half is untested. |
| fig8-model | blocked (other) | A simulation, with no recorded data involved. I agree. |

Chance levels against the paper: Fig 7E's content-based features (6.6 to 8.1%) put the paper's effective chance near 5 to 8%. That matches reading (a) (4.7 to 5.9%) and not reading (b) (40.5 to 41.7%). For phase locking, the shifted-phase null median resultant is 0.048 against 0.124 in the data, which is qualitatively like Fig 1E.

### B. Problems

1. **[affects a conclusion]** The LS detection channel carries the hippocampal or a common-reference 120 to 180 Hz signal (`session_job`, `detect_events`). Three signs:
   - 35% of LS–CA1 event pairs share the same trough sample (DT8 71%, DT2 62%; cell 42).
   - The median lag is 0 ms.
   - The CA1–LS PLV at jittered times is 0.20 (cell 44), while windows with random phase would give roughly 0.02 at about 3,000 ripples per recording.

   No local re-referencing, for example a bipolar LS derivation, was tried. This undermines fig5d, fig5e, fig5f-no-phase-coherence, fig2 and fig1g, and probably fig1c and figs1. The notebook prints the same-sample fraction but draws no consequence from it.
2. **[affects a conclusion]** In 5 of 6 animals the detected events do not raise LS firing (cell 15), and participation is a sixth of the paper's (cell 21). The detector is not capturing the paper's LS HFOs. This is why only 106 pairs survive (cell 31), and it is the real cause of the "too few recordings" blocks on fig4-sessions-few-change and fig4c, not a limit of the archive.
3. **[affects a conclusion]** `fig7_rows` counts spikes between ripple start and stop, so the count grows with duration. That makes duration and CA1 spike count trivially predictive (86%, 79%). With a fixed ±25 ms window the figures are 24.7, 17.8 and 34.9% (cell 46), close to the paper's. Reading (b) is miscalibrated by construction: a one-sample t-test of 99 shuffles against one draw flags about 42%. It should not be used.
4. **[affects a conclusion]** fig2 (cell 29) rests on 5 recordings from 1 animal, and the ratios in other regions are as high as in LS, which fits problem 1.
5. **[affects a conclusion]** fig1d's trough preference may come from each unit's own spike waveform leaking into the 120 to 200 Hz band of the LS channel. The channel is chosen for maximal band SD on the same probe (`choose_channels`), and 82 units have resultant above 0.6 against none in the null. This was never checked, for example by taking the phase from another shank. The partial outcome rests on this part.
6. **[does not affect a conclusion]** The instantaneous-frequency estimator pulls toward the band centre. On synthetic bursts (`detect_events`), 140 Hz reads as 145 and 170 Hz as 167. This compresses differences but cannot reverse the order in fig1g.
7. **[does not affect a conclusion]** `metadata` never reads the LFP `starting_time` value. The clock check (cell 10) supports alignment, except in 7 of 39 hippocampal and 3 of 78 LS recordings, which peak off zero.
8. **[does not affect a conclusion]** fig1f and fig1h pool 57k to 230k events, so p-values are trivially small. The fig1h verdict is driven by n (r=0.056).
9. **[does not affect a conclusion]** Minor points:
   - The PETH slice `[90:111]` covers −10 to +11 ms.
   - The CCG half-width is ±400 ms against the Methods' ±200 ms; the criterion chose this.
   - fig4d uses one circular shift per pair for all factors, and the pair counts shrink to 5 to 16 at high factors.
10. **[does not affect a conclusion]** I tested `ccg`, `peth`, `counts_in`, `in_intervals`, `state_of`, `excess_correlation`, `cv_mse` (it matches a least-squares fit to 1e-15), `emg_from_lfp`, the phase convention (trough is ±180°) and event timing on synthetic inputs. All behave correctly.

### C. What I could not check, and the output that would settle it

- **Whether `group_id` is the shank, and whether the units table has waveforms or peak channels** (this decides the fig4 pair selection and the fig7e-ca1-depth block). Needed: units-table column names and one row per animal.
- **Probe model, site pitch and electrode-group or device descriptions** (fig3). Needed: printed `electrode_groups` and `devices`.
- **Whether problem 1 is volume conduction or a shared reference.** Needed: the same-sample fraction and the jittered PLV recomputed on a bipolar LS derivation, and the per-recording ripple count `n` used in the coherence.
- **fig2ef.** Needed: per-recording HFO power and phase-locked fraction against the drive depth in the session name.
- **fig7e-replay.** Needed: which files hold Position or SpatialSeries, and their coverage of the trials.
- **The figures themselves.** I did not view the plots; I relied on the printed ranges.
