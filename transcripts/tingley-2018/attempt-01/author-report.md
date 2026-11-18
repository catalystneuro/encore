I've completed steps 1 to 5 and run the handover (step 6). The entry passes `check`, and the clean run passed in 463 s (under 8 minutes). Nothing is committed.

I used the full text of the NIH author manuscript (PMC6605060), saved under `paper/`. I did not read the supplementary figures. The pinned version is 0.250624.0438. The paper cites no version, and the two published versions hold identical assets (same paths, asset ids and sizes), so I took the newest; the notebook header says why.

### 1. Outcome per claim (25 claims)

| Claim | Outcome |
|---|---|
| ls-neuron-count (1,647 LS units, 62 sessions) | Reproduced: 1,696 units, 62 sessions |
| hpc-unit-count (2,297 CA1, 654 CA3) | Partially reproduced: 2,593 `hpc`, 624 `ca3` |
| ls-active-neurons (840) | Reproduced: 793 |
| fig2-ls-phase-vs-shuffle (89%) | Not reproduced: 52.1% |
| fig2-ls-phase-beats-rate | Not reproduced: 84.5% of neurons, 48.1% of conditions, 58/58 sessions |
| fig2e-ls-phase-lower-mse | Reproduced: p = 2.5e-232 over conditions, 2.9e-23 over sessions |
| fig2fg-mse-difference | Partially reproduced: LS −1,045 (paper −1,000); hippocampus −167 (paper −33) |
| fig1i-hpc-rate-phase-equivalent | Reproduced: KS p = 0.115, but only 315 fields against 1,820 |
| ls-few-place-fields | Not reproduced: hippocampus 6.2% against 31.7% |
| hpc-place-field-properties | Partially reproduced |
| ls-place-fields-unstable | Partially reproduced |
| fig1e-phase-info-smaller-scale | Partially reproduced: medians 10 and 19 bins (paper 15 and 29) |
| fig1g-phase-more-info-fine-scale | Partially reproduced |
| fig4d-depth-gradient | Partially reproduced |
| fig4e-onset-depth | Not reproduced |
| fig6c-ca3-coherence-increases | Not reproduced |
| fig6d-cfc-stronger-ca3 | Reproduced |
| figs7-ensemble-ls-phase-best | Not reproduced |
| fig5-assemblies, fig5g, fig6e | Blocked: not runnable |
| speed-independent, ls-information-lower | Blocked: methods underspecified |
| figs6-reference-frame | Blocked: metadata insufficient |
| fig7-dynamic-weighting-model | Blocked: other (a simulation) |

### 2. What I found about the dandiset
- **Missing processed files:** the paper's linearized positions, trial conditions and the CA1 channel used for theta in each session are not in the dandiset. Units have no recording site. I rebuilt the first three, and several outcomes depend on how.
- **Undescribed fields:** the two depths in each session name are not documented. I took the first as the LS depth. The `hpc` label is not defined as CA1.
- **Wrong units and format errors:**
  - 8 DT8 files state positions in mm but hold metres.
  - In all 67 files the z column of position is a copy of y.
  - 8 DT2 files have repeated or backward position timestamps.
  - 11 units hold spike times out of order.
- **Missing labels:**
  - All DT2 electrodes, and those of 2 DT9 files, are labelled `unknown`.
  - DT2 positions are in pixels with no scale.
  - DT7 20170317 has 43 units with no region label.
  - DT7 20170324 has no units.
  - Linear-track trials, and two DT8 alternation files, have no trial type or direction.
- **Timing problems:** DT9 20170501's trials do not match its positions. DT2 20160221's trials look offset by about 1 s.
- **Counts differ from the paper:** more units than the paper reports (for example 20,979 hippocampal–LS pairs against 11,264), with no record of what the paper left out.
- **Unpublished code:** the paper's code calls functions that are not public (phase binning, the information measure, assembly detection).
- **LFP storage:** 42 files store the LFP in chunks of 500 samples across all channels, so reading one channel means reading the whole LFP.

### 3. Where the protocol was unclear, wrong or missing something
1. **Clock check:** a constant offset between spikes and positions can't be seen by self-consistent analyses such as decoding with shifted labels. I used running speed in shifted trial windows, spike–LFP theta locking against lag, and firing rate in shifted windows. The last was inconclusive, and the notebook says so.
2. **Count claims:** their outcome is fixed by the data check, so their criteria were necessarily written after seeing the counts. I recorded this.
3. **Missing processed data:** the protocol doesn't say whether to rebuild missing derived files or block the claims. I rebuilt them, fixed the choices in the claims file before any analysis, and logged them as deviations and findings.
4. **Not-runnable:** the protocol says "say what was tried". For the assemblies I only counted the pairs and estimated the work (about 35 million GLM fits); it doesn't say whether a reduced subset should be tried first.
5. **Simulation claims:** there is no category for a claim about a model that uses no recorded data. I used `other`.
6. **Threshold variants:** choices that need a full rerun (200 bins, how conditions are clustered, place-field width limits) were not varied, because of time. Logged as deviations.
7. **10% tolerance:** it is meaningless for a value near 100% (93.6%). I used the distance to 100% and said so in the claims file.
8. **Partial outcomes:** the protocol gives no guidance on designing the partial-outcome rule. Mine put fig2-ls-phase-beats-rate at not reproduced although phase beats rate in every session.
9. **Incomplete code:** "follow the code" can't fully apply when the code calls unpublished functions. Recorded as `methods_unavailable`.
10. **Date:** the run crossed midnight. I used the given date, 2026-10-16.

### 4. Runtime and failures
- The notebook takes about 8 minutes with 4 processes and streams only the trials of each file.
- Final `tools/entry.py all`: passed.
- During exploration, one script that scanned the HDF5 chunk index hung and hit a 30-minute timeout. Nothing in the final run failed.
- The untracked dotfiles in the repo root (`.bashrc`, `.vscode` and so on) are sandbox placeholders, not real files; they were not created by this work.
