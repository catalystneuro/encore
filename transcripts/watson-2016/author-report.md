I finished steps 1 to 6: the entry, the notebook and the record (`attempts/watson-2016-03.yaml`) are written. `check` reports 0 errors, `all` passed from a clean environment (24.6 min), and `handover` built the verifier's package. Every claim was tested on both datasets except `fig5c-wake-movement`, which was tested on CRCNS only because DANDI has no motion or EMG signal. No claim is blocked.

**Accidental exposure to earlier work.** You should know about two things before the comparison step:
- The release notes of DANDI version 0.261104.0300 say the files were re-converted to fix problems "found by a reproduction attempt (issue #75)". They list dropped units, the Dino-072114 spike times, the LFP gain and Dino-061914's missing LFP. I read these as part of the dataset's metadata (step 1).
- The old per-dataset claims files in `claims/watson-2016/` are still in the checkout. Their headers describe an earlier data check, for example that Dino-072114's spike times were whole seconds divided by 20000. I read those headers.

## (1) Outcomes (53 claims: 18 reproduced, 21 partially, 14 not, 0 blocked)

The protocol gives one outcome per claim, so I combined the two datasets: reproduced when the claim holds on both, partially when it holds on one or only in part. This was my choice and is stated in the notebook.

| Outcome | Claims |
|---|---|
| reproduced | fig2c-acg-peaks, synchrony-skew, updown-durations, fig2de, fig3ab, first-last-packet-mean-rate, fig3b-sextile-changes, cv-decreases-over-sleep, fig3f, figs3a, fig3e, fig4i, fig4-delta-packet-length, fig4e-late-packet-sigma, fig4iv, fig4v, fig4vi, fig5b-wake-between-packets |
| partially_reproduced | table1-dataset-counts, wake-sleep-cycles, tables1-state-durations, ma-fraction-over-nrem-episodes, packet-duration, fig2a-median-rates, fig2a-skewed, fig2a-fraction-above-2hz, fig2b, burst-index, fig2c-acg-decay, fig1e, post-sleep-wake-lower, fig3d, fig4-late-packet-sigma-delta, fig4-updown-within-packets, fig4-spindles-within-nrem, fig4cd, fig4e-within-up-sextiles, fig5b-ma-between-packets, sleep-homogenizes-rates |
| not_reproduced | ma-statistics, fig2f, fig3c-spindles, fig3c-updown, figs5-within-wake-rem, fig5b-ma-nrem-ma, figs5d, fig5c-sigma-ma-change, fig5c-wake-movement, fig5b-rem-between-packets, fig5c-rem-duration, fig5c-rem-theta, fig5c-delta-change, figs2d |

Many of the partial outcomes come from DANDI alone: the claim matches on CRCNS but not on DANDI.

## (2) Datasets, assumptions, questions

**Versions.** DANDI is pinned at 0.261104.0300, the latest published version, chosen because its re-conversion corrected the units, cell types and gain that the analysis uses. CRCNS is unversioned; the notebook prints the MD5 of each file read.

**CRCNS:fcx-1** holds the paper's full data set:
- 11 rats, 27 sessions, 1121 stable units of 1360 clustered, 995 pE and 126 pI.
- Its deposited intervals reproduce Table S1 exactly: the five durations, 43230 UP and 86839 DOWN states, and the spindle duration, frequency and amplitude.
- Its spindle incidence agrees with Table S1 (2.94/min), not the Results (1.94/min).
- Only 434 MAs fall within SLEEP, against the paper's 790; the deposited list has 2130 in total.

**DANDI:000041** differs in several ways:
- It lacks 5 sessions (rat B22 and the two Dino ACC probes), and Dino-061914 has no LFP.
- It has only Awake, Non-REM and REM epochs: no cycles, packets, MAs, UP/DOWN states, spindles, motion or EMG.
- In 7 sessions whose spike trains are identical to CRCNS, the cell-type labels differ.
- Three Dino sessions have extra units, and nothing marks which units are the stable ones.

**Assumptions** (flagged on 9 outcomes):
- On DANDI, a WAKE ends where a SLEEP begins.
- On DANDI, UP/DOWN detection uses log power of 100 to 400 Hz. On linear power the paper's "0.5 SD below the mean" rule never triggers.
- Power within UP states uses 200 ms windows.

**Questions for the paper's authors** (recorded as findings):
- Which MAs make the 790?
- What band, smoothing and scale does the low-gamma rule use?
- What is the sampling unit of the time-normalized correlations? The CV-over-SLEEP result depends on it.

The record also has two paper inconsistencies: the spindle incidence, and the 5918 s WAKE-SLEEP duration in Table S1 against 4214 s in the data. I asked no questions of a reader.

## (3) Protocol gaps

1. There is no rule for combining two datasets into one outcome per claim. I used the rule above.
2. `measured` takes one set of values. I recorded the CRCNS values and said so in the notes.
3. docs/archives.md describes CRCNS zips, but fcx-1 holds tar.gz files, and in 14 of them the LFP comes before the metadata. I streamed each tar once over parallel range requests and computed band power on all channels. Where the .xml came later, I inferred the channel count from the stream's autocorrelation; it matched the .xml in all 10 such cases.
4. Composite criteria do not say when a part "holds". For fig4cd and fig4e-within-up I counted M4's partial level (right sign at p < 0.05) and stated it as a deviation.
5. The suggested clock check (decoding with shifted labels) does not fit continuous sessions without trials. I used a contrast instead: population spiking rises 50 to 70 fold at UP onsets, and the rise vanishes when the onsets are shifted by 30 minutes.
6. I delegated one long caching command to a subagent. It ran in the foreground, but I waited on it, so it gave no parallelism.

## (4) Runtime

The notebook takes 24.6 min in a clean run: DANDI 6.8 min, CRCNS 13.8 min. The main process peaks at 1.6 GB. I ran it twice; the second run only added per-rat breakdowns, and every other number was identical. Nothing failed. The session ran from 05:00 to about 07:00 UTC.
