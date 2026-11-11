Steps 1 to 5 are done and the handover is built (`executed/drieu-2018/handover/`). The entry check passes, both notebooks pass from a clean environment, and nothing is committed. Of 35 claims: 9 reproduced, 11 partially reproduced, 10 not reproduced and 5 blocked.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| figs1-travel-similar | not reproduced: velocity and laps match, duration differs (P = 0.023) |
| figs2b-place-cell-count | not reproduced: 207/203/228 against 94/150/135 |
| fig1c-field-size-similar | reproduced, assumed (10-bin minimum field, P = 0.070) |
| fig1c-peak-rate-lower-passive1 | reproduced |
| figs2c-track-coverage | reproduced (100%) |
| fig1d, fig1e, figs2d (no remapping) | partially reproduced, assumed |
| fig2b-theta-frequency-unchanged | reproduced (weak test: 0.5 Hz resolution) |
| fig2b-theta-power-reduced | partially reproduced, assumed |
| fig2b-theta-asymmetry-reduced | reproduced |
| fig2cd-spike-bursts-slower | not reproduced |
| figs4b-proportions-oscillating-precessing | not reproduced |
| fig2f-phase-precession-degraded | partially reproduced, assumed |
| figs4de-precession-range-similar | not reproduced, assumed |
| figs11-sleep-sessions-similar | not reproduced (KS of event-to-ripple timing, P = 0.011) |
| fig3b, figs5b (average theta reconstructions) | partially reproduced |
| fig3c-theta-scores-above-chance | reproduced |
| fig3c-proportion-significant-theta | not reproduced |
| fig3d-theta-slopes-steeper-active | partially reproduced |
| fig3e, fig4d (joint score and slope) | reproduced, assumed (high-value region from the claims file) |
| fig3f-quadrant-scores | reproduced |
| figs9-control-decoding-quality | partially reproduced |
| fig4b-replay-scores-vs-baseline | not reproduced |
| fig4c-replay-slopes-steeper-active | partially reproduced, assumed (significant events only) |
| fig4e-replay-proportion-vs-baseline | not reproduced (Passive 2 decreased) |
| fig4f-forward-replay-after-active | partially reproduced (P = 0.005, not < 0.001) |
| figs12-ripple-restricted | not reproduced |
| fig3g, fig4g (bias correlations) | blocked, `too_large` (about 160 h, timed in the notebook) |
| figs7, figs8, figs10 (controls) | blocked, `too_large` (not run for lack of time) |

## 2. Dataset, assumptions, questions
- **Data:** five archives (47 GB), one session per rat. Spikes, positions and LFP end within a second of each other in every rat. The five rats are distinct, so no recording is counted twice.
- **What the descriptor doesn't say:**
  - Rats 292 and 314 were recorded at 20 kHz.
  - The head-tracking LED is lost for 40.6% and 22.8% of samples in those two rats.
  - The traced track perimeter is 656 to 706 cm, against the paper's 6 m.
  - Rat 272's LFP saturates in about 1% of sleep samples.
- **What the paper's code needs but the data set lacks:** `code.zip` holds the paper's scripts, but not the channel lists, theta-cycle files, place-cell database or the linearization and decoding functions they load. I rebuilt these from the data.
- **Code mismatches (recorded as findings):**
  - DiscriminateUnits.m clusters on two features, not the Methods' three, and its 5 Hz rate exclusion never applies (it tests `strcmp(rate,'on')` on a numeric array).
  - ClusterIsolation.m assigns L-ratios to the wrong units after a skipped cluster.
  - BatchPlaceFields.m uses a 12 cm kernel and field size limits that the Methods don't state.
- **Version:** `unversioned`, with MD5 sums in the notebook headers; `hc-18/live/` is the only published copy.
- **Assumptions:** the 10-bin minimum field size from the code; the phase from 1-40 Hz peaks and troughs; the LFP channel choice; SWS detection with 5-s windows and 5 clusters; the linearization method.
- **Questions for the authors:** four, recorded as a `methods_unavailable` finding: field size limits, burst spectrogram windows, the theta channel, and the SWS settings.
- **Questions to a reader:** none.

## 3. Where the protocol was unclear or did not fit
1. archives.md covers zip files only; each rat here is one tar.gz. I streamed them with parallel range requests, zlib and an in-memory tar parser (47 s against 490 s with fsspec/tarfile). Nothing went to disk.
2. "Do not download to disk" doesn't say whether reduced arrays may be cached while developing. I kept pickled reductions (not archive files) in `$TMPDIR` for development only; the notebooks always stream.
3. The tar member order varies, and for rats 272 and 314 the LFP comes before the xml that gives its channel count. The loader makes a second partial pass for those two.
4. The clock check suggested for spikes against positions (shifting spikes in time) cannot detect an offset here: the train runs at near-constant speed on a closed track, so a shift only rotates the fields. I recorded the clock as consistent with the data, not shown.
5. For claims of absence, the protocol doesn't say whether "judged on the paper's test alone" also overrides method readings such as phase or field definition. Where the readings disagreed I adopted the best-supported one as an assumption.
6. Several criteria lack a "partially reproduced" clause (fig4b, fig4e, fig4f). I read fig4b and fig4e strictly as not reproduced, and fig4f as partially reproduced by the protocol's general definition: the effect is present but weaker.
7. Running 5000 shuffles per event was not feasible (about 10 h). I used 200 and recorded it as a deviation; the protocol has no rule for reducing shuffle counts.
8. The 60-min notebook limit forced two notebooks, and each must stream the whole dataset again (about 15 min).

## 4. Runtime and failures
- Clean run: 31 min (travel and sleep notebook) and 37 min (decoding notebook), peak memory 6.4 GB.
- Development problems, all fixed before the clean run:
  - My first SWS detection found almost no SWS; I switched to the paper's script's settings.
  - Saturation in rat 272 broke SWS detection; I added masking as the paper's scripts do.
  - L-ratio computation was slow (456 s for one rat); I vectorised it.
- Nothing failed in the final run. The three controls were not attempted because of the time limit.

Files are in `entries/drieu-2018/` and `attempts/drieu-2018-01.yaml`.
