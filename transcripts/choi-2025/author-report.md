I tested the paper on DANDI:002014 version 0.261120.0528 and wrote the entry at `entries/choi-2025` and the record at `attempts/choi-2025-02.yaml`. Five claims were tested: four reproduced and one partially reproduced. The other eight are blocked because their data are not in the dandiset. `tools/entry.py all` passes with 0 errors (156 s), and the handover is built in `executed/choi-2025/handover/`.

**Exposure to earlier results.** I read the dandiset's release notes because protocol step 1.1 asks for the archive metadata. They describe the conversion fixes made after "a reproduction attempt" (issue #30 of schwerdt-lab-to-nwb): one clock for all streams, events no longer stored several times, Plexon timestamps, units. That is a summary of an earlier attempt's findings. I did not open those issues. The claims file's own opening comment also reports a data check from an earlier version (an offset of 11812.1 s).

## 1. Outcomes

| Claim | Outcome | Key numbers |
|---|---|---|
| fig8a-single-trial-dopamine | reproduced | after-V to before-V SD ratio 2.03 (trial id 133) and 2.20 (row 133) |
| fig8b-dopamine-large-vs-small | reproduced | V to RW, large minus small 0.751, Mann-Whitney p = 0.0031 |
| fig9a-spikes-task-aligned | reproduced | 100% of trials have spikes; PSTH variance 0.48 against a random-alignment 95th percentile of 0.056 (same under all five seeds) |
| fig9bc-unit-waveform-isi | reproduced | 0 intervals under 1 ms; waveform peak is 4.79 times its SD |
| fig9d-beta-suppression-large | partially reproduced | medians −0.158 (large) and −0.125 (small); p = 0.109 |
| recordings-two-monkeys, the four yield claims, asepsis-cultures, fig6, fig7 | blocked, data_missing | |

## 2. The dataset

- **Contents:** one NWB file holding one session of monkey T, the session of Figures 8 and 9. Monkey J, the electrode yields, cultures, drainage volumes and bone-growth data are not in it, nor in the paper's Zenodo record (rated major).
- **Clocks:** every stream shares one clock.
  - The stored LFP matches the raw c7b minus c5c signal at a lag of 0 to 1 ms (r 0.89 to 0.94 in 1 to 8 Hz), so the spikes were moved by only 0.5 ms, not the 11812 s in the claims file's comment.
  - The thresholded spikes sit on the raw c5d troughs.
  - The spike-free gap falls 46 to 50 ms into every FSCV scan interval for the whole session.
  - The dopamine difference between large and small trials appears only after the value cue.
  - What I could not establish is how the trial-aligned oxidation current relates to the raw FSCV scans.
- **Trial classes:** classing trials from the events gives the paper's Zenodo lists exactly (451 large, 499 small), plus the last trial, id 1411.
- **Minor findings:**
  - The dopamine, pH and motion components and the oxidation current have no units.
  - The stored LFP keeps only 0.14 to 0.17 of the raw signal's SD in 13 to 30 Hz. This fits removal of the FSCV artifact, which the file calls undocumented and Zenodo calls spectral interpolation.
  - The thresholded spikes have no interval below 1.56 ms, about one waveform's length, so the 1 ms refractory test cannot fail on them.
  - The thresholded unit and the Plexon unit hold the same spikes (99.5% match); I counted them once.
  - The release notes mention eye tracking, but the file has none.
- **Assumptions:** none. Every method came from the claims file's criteria. One small choice, the time span used for the last trial's random alignments, affects one trial out of 951.
- **Question for the paper's authors** (recorded as a methods_unavailable finding): which beta band, filter and windows were used for Figure 9D, and was the large against small difference tested? The paper reports no statistical tests for Figures 8 and 9.
- **Questions to a reader:** none.
- **Paper listing:** the paper should be listed on ZENODO:14825992, its own deposit named in the Data availability statement. I used only its two small trial-id lists, recorded under `inputs`.

## 3. Where the protocol was unclear

1. The claims file's opening comment describes a data check on an earlier dandiset version (the 11812.1 s offset). In a blind repeat this both leaks earlier work and no longer matches the data. I measured the offset again (0.5 ms), applied that, and noted it as a deviation.
2. Step 1.1 requires reading the archive metadata, and here the release notes summarise the earlier attempt's findings. The blind rule does not cover this. I recorded each finding as I found it and disclose the exposure above.
3. When a claim names a "4th order Butterworth" band-pass, it is not clear whether that means design order 4 or a filter of total order 4. I used design order 4 (scipy's and MATLAB's convention) and showed order 2 as a variant.
4. For the paper's own deposit in another archive (Zenodo), the protocol does not say whether it goes in the record under `datasets` or under `inputs`. Since I used it only to check the trial classes, I put it under `inputs` and named it in the entry's `related` list.

## 4. Runtime and failures

The notebook runs in 2.6 min with 1.7 GB peak memory, and the whole session took about 25 minutes of wall time. Nothing failed. The one check that did not work was comparing the raw FSCV scans with the trial-aligned oxidation current: lags were inconsistent across trials. I ran it while preparing, not in the notebook, and it decides no outcome.
