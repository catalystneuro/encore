I did steps 1 to 5 of the Author section on DANDI:000673 and ran the handover (step 6). The entry is `entries/000673-daume-2024/` (three notebooks plus the helper `sbcat.py`) and the record is `attempts/000673-daume-2024-01.yaml`. `entry.py check` gives 0 errors and `entry.py all` passes all three notebooks.

I pinned version 0.240118.2135 because the paper's reference 59 cites it. In the latest version (0.250122.0110) every file was re-uploaded a few hundred kB smaller; I did not compare the contents.

## 1. Outcomes

12 reproduced, 5 partially reproduced, 6 not reproduced, 34 blocked (57 claims).

| Claim | Outcome |
|---|---|
| cohort-counts, fig1d-rt-load, fig1d-accuracy-load, behaviour-overall-accuracy | reproduced |
| category-cell-counts | partially reproduced: pre-SMA (18 neurons) is also above chance |
| fig3b-persistent-activity, edf4b-persistent-activity-by-area | partially reproduced: preferred vs non-preferred holds only in % of baseline, and the criterion asks for both units |
| fig3c-category-load | not reproduced (assumed: % of baseline) |
| fig3d-category-correct-incorrect | reproduced (assumed: % of baseline) |
| category-no-rt-effect | reproduced |
| fig2a-theta-gamma-pac | reproduced (assumed: artefact reading a) |
| fig2b-pac-channel-proportions | partially reproduced: pre-SMA has 17 channels against the paper's 5 |
| fig2c-hippocampus-load, edf3a-kappa-load | reproduced |
| edf2b-hippocampus-load-patients, edf3f-raw-mi-load | reproduced (assumed: artefact reading a) |
| edf3e-nesting | reproduced (assumed: windows aligned on gamma peaks) |
| fig2c-no-load-effect-other-areas, edf2c-low-gamma-no-load-effect, tables1-slow-fast-theta | not reproduced: pre-SMA, plus the amygdala or dACC in some readings, also differ between loads |
| fig2f-rt-single-trial-pac | not reproduced: no reading gives a significant hippocampal term |
| methods-spectral-slope | not reproduced (assumed: 2–150 Hz); difference of 0.004, p = 0.0073 |
| pac-neuron-counts | partially reproduced: 8 of 269 and 5 of 422 neurons against 79 and 163; above chance (p = 0.005) |
| edf3-hippocampus-pac-controls, edf8fgh-frontal-controls, the 5 SFC claims and fig3h | blocked (`too_large`): parts or all not run for lack of time; partial results are in the notes |
| 22 claims that need PAC neurons (overlap, PAC-neuron firing, noise correlations, decoding, cross-regional SFC) | blocked (`other`): too few PAC neurons under the claims' own selection |

## 2. Dataset, assumptions, questions

**What the dataset holds:**
- Every count the paper reports is there: 44 sessions, 36 patients, 1,454 units, 1,922 LFP channels (sub-20 has no LFP).
- The trials table agrees with the TTL events, and spikes and LFP share the trial clock (checked by contrast: shifted onsets, probe-locked LFP).

**Findings recorded:**
- Four units in two files have unsorted spike times. In sub-13 ses-1 three of them jump back about 1,320 s, as if two spike trains were joined.
- The files do not mark the trials, channels or regions removed by the paper's visual artefact inspection. A few pre-SMA channels then decide three of the "no effect" claims.
- Microwire bundles are not identified; I inferred them from location and coordinates.
- The maintenance period lasts 2.53–3.20 s against the Methods' 2.55–2.85 s.

**Assumptions, each recorded as a question for the paper's authors** (`methods_unavailable`):
- **Firing-rate units:** % change from baseline, because the legends print P values with the panels shown in % change.
- **Artefact-rejection span:** reading (a), the −0.5 to 3 s epochs. It removes 11.4% of trials against the paper's 14.6%, which includes manual removal; whole trials (b) remove 25.9%.
- **Nesting alignment:** gamma peaks. Taking the Methods literally (amplitude maxima) gives 6% nested channels against the paper's 80%; gamma peaks give 73%.
- **Spectral slope range:** 2–150 Hz.

Two further questions have no assumption behind them:
- How single-trial PAC is computed.
- Which family the PAC-neuron FDR correction covers. My selection follows the paper's `plot_PAC_neuron.m` and still gives about a tenth of the paper's count.

I asked no reader questions.

## 3. Protocol points

1. With 57 claims, the five-hour limit forces choices the protocol does not rank. I tested whatever does not need SFC or decoding first, and blocked the rest as `too_large` (not started) or `other` (too few units).
2. The protocol says to run every reading, but a notebook must stay under 30 minutes. I ran the fig2a comodulogram under artefact reading (a) only, marked it assumed and recorded the deviation.
3. `blocked_by` has no category for "not started for lack of run time" or "selection gave too few units". I used `too_large` for the first (protocol, Time) and `other` for the second.
4. When an absence claim mixes parts I ran with parts I didn't (edf3 controls, edf8fgh), the protocol does not say whether to block or to grade from the parts run. I blocked both and put the partial results in the notes.
5. One reading in the claims file is logically inverted: for edf3, a significant V test of preferred-phase differences against 0 means "no shift". I reported it with that interpretation.
6. I re-executed notebook 1 alone with the same environment and nbconvert command as `entry.py`, because I corrected its conclusion text after the full run. `entry.py` has no single-notebook option.

## 4. Runtime and failures

- The run went from 08:09 to about 10:35 UTC.
- Final `entry.py all`: notebook 1 took 3.3 min, the LFP notebook 20 min and the PAC-neuron notebook 8.2 min.
- The LFP notebook was at 27 min before I sped up its streaming and filtering; at 20 min it still uses two thirds of the 30-minute CI limit.
- Nothing failed in the final run.
- The handover package is in `executed/000673-daume-2024/handover/`. Nothing is committed or pushed.
