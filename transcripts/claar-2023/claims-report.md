I wrote the claims file at `claims/000458/10.7554-elife.84630.yaml`. Nothing is committed. The quote checker passes every quote and leaves one flag, which is a limit of the checker: the paper prints `p=2.020E-7` (fig7g), and the checker drops the trailing zero and looks for `2.02e-7`. I confirmed the value by reading the text.

**Text read:** the eLife version of record (eLife 12, RP84630, 2023), full text from Europe PMC. It includes the Results, Discussion, Methods, every figure legend and figure-supplement legend, and the peer review with the authors' response. eLife has no separate supplementary text, and no PDF was needed. The dataset links the bioRxiv preprint (10.1101/2022.07.22.501195); I did not use it, because the version of record replaces it. Nothing the claims need is missing from the text.

**Code:** the paper links only the PCIst code, renzocom/PCIst, which I read at the cited commit e495a0a. It links no analysis code of its own.

**Claims:** 37 in total.
- All 37 have quotes and criteria, 33 have expected values, and 21 have statistics (30 p-values).
- They cover Figures 1 to 8 and their supplements, plus a few numbers that let the author check they are looking at the right data: stimulation depths, good EEG electrodes, unit counts and trial counts per state.

**Details the paper leaves open, and the readings named for each:**
- **Stimulus intensity.** Three intensities were delivered per stage, but no analysis says which pulses it uses. The trial counts (median 120 per state) point to one intensity's 120 pulses. Readings: the highest intensity, the medium one, or whichever pulses the dataset marks.
- **Which awake trials** Figures 1 to 6, 8B and 8C use: all awake trials, or quiet wakefulness only.
- **Unit of N.** Counts exceed the 23 mice included (for example 12 + 18 in Figure 1E, 31 sessions in Figure 8B), so each claim is tested on one value per mouse and stimulation site.
- **Good EEG electrodes and unit quality.** Electrodes were picked by eye, and unit quality uses Siegle et al. 2021 metrics with no thresholds printed. Readings: the dataset's own flags, or Siegle et al.'s thresholds.
- **ERP duration:** total time above z = 3, or time from onset to the last point above it.
- **ERP magnitude:** the area above z = 3 (figure-supplement legend), or that area divided by the baseline area (Methods text).
- **Peak timing:** no peak-detection method is given; two window choices are named.
- **Quiescence length:** not defined. Readings: time below the pre-stimulus rate, or time at zero spikes, with 1 ms and 5 ms bins.
- **LFP, CSD and spiking magnitude:**
  - high-pass cutoff (0.1 or 1 Hz)
  - smoothing kernel for spike rates (5 or 10 ms)
  - baseline window (-2 to 0 s or -0.5 to 0 s)
  - how stimulus onsets are shuffled
  - one value per mouse or per region. The printed p-values are the smallest possible for n = 6, 8, 14 and 16, which points to one value per mouse.
- **Modulated neurons:**
  - pre-stimulus window: immediately before onset, or mirrored about onset
  - false-discovery correction applied per session or pooled across sessions
  - what "spiking reduced in 18/22 subjects" counts
  - whether "2 to 300 ms" for thalamus is one window or the union of three
- **Burst probability:** trials on which any thalamic unit bursts, or the mean over units.
- **Rebound window:** 75 to 300 ms (Figure 5F) or 100 to 300 ms (Figure 7G); both are run.
- **Single-trial late ERP amplitude:** peak of global field power, or peak voltage at one electrode.
- **Trial matching** for the ERP state comparisons.
- **Baseline firing epoch:** -2 to 0 s or -0.5 to 0 s.
- **PCIst:** the parameters the paper does not set are left at the code's defaults. The EEG is used at its 2.5 kHz rate, because the PCIst value scales with the number of samples in the response window.
- **Recovery sample:** all 13 subjects, or only those with all four stages.

**Internal inconsistencies in the paper,** each recorded as alternative targets or in `n`:
- The Discussion gives different values from the Results for:
  - superficial quiescence: 44.3 ms against 94.2 ms
  - deep quiescence: 127.8 ms against 125.0 ms
  - latency differences: 6.7 ms against 6.9 ms, and 37.0 ms against 36.0 ms
  - baseline firing rates and the quiet-wakefulness burst probability
- N differs between text and legend: 13 against 12 for Figures 7F, 7G and the Figure 6 supplement 2; 8 against 7 for Figure 3D.
- The Figure 8E statistic, F[3, 18], implies 7 subjects, not the 13 stated.
- The Figure 7G interaction (F = 6.6, p = 0.053) does not fit its degrees of freedom.

**Data from outside the paper:** none. Every claim uses `data: dataset`.
