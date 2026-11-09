I did Author steps 1 to 6. The entry is `entries/000458-claar-2023/`, the record is `attempts/000458-claar-2023-01.yaml`, and the handover package is built. `entry.py check` reports 0 errors, and both notebooks passed `entry.py all` from a clean environment. I did not commit anything.

## 1. Outcome per claim (37 claims)

| Claim | Outcome |
|---|---|
| eeg-good-electrodes, fig1-supp1-example, fig1e-erp-duration, state-trial-counts, fig7c-erp-duration-state, fig8c-pcist-depth, fig2c-superficial-quiescence, fig5a-thalamus-modulated, fig6-supp2-late-erp-bursts, fig7e-baseline-rates | reproduced |
| fig8e-pcist-recovery | reproduced, but only 1 of the 8 reading combinations matches |
| fig1f-erp-magnitude, fig7d-erp-magnitude-state, fig7f-early-latency-state | reproduced, resting on an assumption |
| fig2c-deep-triphasic-cortex, fig2f-thalamus-triphasic, fig4cf-rebound, fig4-supp1-fs-like-rs, fig5c-burst-probability-depth, fig5e-early-latency, fig7h-burst-probability-state, fig8b-pcist-awake-anesthesia, fig8d-pcist-three-states | partially reproduced |
| fig7g-rebound-latency-state | partially reproduced, resting on an assumption |
| fig1d-two-erp-peaks, fig4-unit-counts, fig4ad-initial-excitation, fig4be-off-period, fig5f-rebound-latency, fig6b-bursts-cortical-rate, fig6c-cortical-rate-late-erp | not reproduced |
| stim-depths, fig1-supp2-first-peak-flips | blocked, data missing |
| fig3abc-decay-with-distance, fig3d-magnitudes, fig6a-csd-sink, fig6-supp1-erp-deep-csd | blocked, metadata insufficient |

## 2. Dataset, assumptions and questions

**Version.** I pinned 0.230317.0039. It is the version the paper cites and the only published one.

**What matches the paper.**
- 23 subjects and 31 stimulation sites (13 superficial, 18 deep), matching Figure 8B/8C.
- The trial table gives current, target, depth label, state, `is_running` and `is_valid` for every pulse.
- `is_data_valid` marks a mean of 23.07 good EEG electrodes per subject, as in the paper.

**Findings recorded about the dataset.**
- The depth in mm and the position of the stimulating electrode are not in the files.
- Channel and unit locations are brain areas without cortical layers.
- `waveform_duration` is in ms, but its description says seconds.
- The units' quality threshold is not stated; presence ratios go down to 0.02.
- The RS unit counts in the Figure 4 legend are exactly three times the counts in the files (290, 1370, 853 against 870, 4110, 2559).
- All pulses of one site (586468, superficial SSp) are marked invalid without saying why. Leaving it out gives the paper's N of 12 superficial sites in Figure 1E and 7 in Figure 4.

**Assumptions.**
- The ERP magnitude is divided by "the area under the baseline window", which is zero for a z-scored baseline. I divided by the area under |z| instead (fig1f, fig7d).
- For the state latencies of Figure 7F/7G, responsive units are selected from all awake trials. Selecting them per state leaves only 3 animals.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
1. Which of the three currents each analysis used. Several outcomes change with it.
2. The divisor of the ERP magnitude.
3. How responsive units were selected across states in Figure 7F/7G.
4. The pre-stimulus window and the correction family of the modulation test.

**Questions to a reader:** none.

## 3. Where the protocol was unclear, wrong or missing something

1. **The claims file's readings multiply.** Current × awake set × pre-window × correction family gives 16 to 128 combinations per claim, and "reproduced under one reading" becomes easy to meet. I ran them all, recorded the first-listed reading as `measured`, and said in the notes how many readings match.
2. **A reading cannot always be computed as written.** Reading (b) of the magnitude divides by zero. The protocol does not say whether that is an assumption or a block. I treated it as an assumption and set `assumed: true`.
3. **"too_large" versus time-limited.** For fig3abc, the computation would fit, but the run's time did not, and the layer labels are also missing. I chose `metadata_insufficient` and stated the time limit in the notes.
4. **Strict tolerances on zero.** fig5c expects a median of 0 with tolerance 0; I got 0.003, which is 0 at the paper's printed precision. The protocol has no rule for this. I kept the criterion literal and marked the claim partially reproduced.
5. **Partial outcomes when the criterion has no partial clause.** For fig4cf and fig8b I used the protocol's general definition ("holds only in part"). For fig4be the criterion defines "partial" explicitly and the pattern fails it, so I kept not reproduced.
6. **No way to run one notebook.** `entry.py` runs every notebook together, so each fix cost a full 28-minute run. I tested on subsets in a local environment first.

## 4. Runtime and failures

- The run took about 2 h 10 min, ending at 06:12 UTC.
- The final notebook runs took 14.2 min (EEG) and 13.5 min (spiking).
- The first `entry.py all` failed in the EEG notebook on the site with no valid trials. I fixed it, and the two later runs passed with identical numbers apart from timings.
- PCIst at 2.5 kHz would need several GB per call in the cited code. I replaced only its threshold search with an exact count, which gives the same values as the original on four sites in the notebook.
