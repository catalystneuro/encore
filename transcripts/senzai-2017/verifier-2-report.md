**Verifier report, round 2: Senzai & Buzsaki 2017 on DANDI:000003 (0.260218.2052)**

The claims file has 31 claims. The attempt record has 31 outcomes: 15 reproduced, 11 partially reproduced, 3 not reproduced and 2 blocked. Cell numbers below are 0-based indices in the re-executed notebook. They are not the numbers I used in round 1. I saved the paper text (the PMC author manuscript) under `paper/`.

**1. Outcomes**

I agree with all 31 stated outcomes. Each follows from the printed numbers under the criterion in the claims file. Four of the "reproduced" outcomes are weaker than the label suggests, and the record says so for each:
- **theta-modulation:** The phase part holds on one cut of the cycle only (P = 1e-17 vs 0.82). The spike-count-corrected MRL gives P = 0.00056, which misses the paper's P < 0.0001.
- **pv-remap:** The only valid test, a label permutation on all place cells, gives P = 0.32.
- **inheritance-tmaze:** The overlap of 0.31 is at chance (shuffled partners give 0.38, range 0.19 to 0.62).
- **gc-narrower-waveform:** On all files the result is mostly driven by waveform truncation. On the unfiltered wide-band signal of the 17 files, GC are still narrower (P = 0.017).

**2. Sentences the outputs do not support**

- **Cell 66 and the record's monosyn-gc-to-mc notes:** "4 are also detected as GC to MC pairs". The MC→GC listing in cell 65 shows `GC to MC True` for 5 of the 8 pairs (33-150223 45/55; 33-150224 3/16, 3/19, 3/29; 51b160516 17/8).
- **Cell 0:** "The raw wide-band signal is in 17 files and is not used." Cell 5 also prints "(not used)". Both are stale: cells 21, 24, 29, 35, 107 and 110 now use the wide-band signal.
- **README line 5:** "16 mice over 101 recording days". Cell 0 likewise says "One NWB file per recording day (101 files…)". Cell 18 shows that seven dates hold two files each, so the 101 files cover 94 days.
- **Record finding on the stored waveforms:** "cuts off the peak of most GC, MC and CA3 waveforms". Cell 29 prints that the peak is at the window's end for GC 0.43, MC 0.67 and CA3 0.78. That is a minority of GC.
- **Record remap-positive notes:** "Place cells … CA3 143". Cell 89 prints 145 CA3 place cells, of which 143 have a remapping index.
- **Record gc-mc-distance notes and cell 112:** "The Methods give 8 sites per shank". The Methods say 8 sites per shank on the 8-shank probes and 10 on the 6-shank probes.
- **Record response on gc-mc-classification:** "padding median 5 of 80 samples". This omits that cell 110 prints padding for all 391 units in the stored-waveform variant.

Everything else in the "Result:" cells, the Summary, the README and the record notes matches the printed outputs. I checked the Figure 1H response against the paper: the legend gives 37 units with a >20% decrease, which equals 29 MC plus 8 wide-waveform interneurons.

The record states my round-1 reasons faithfully and mostly in my own words. One small omission: my B2 point that pooling CA3 interneurons also affects the optogenetics nI/wI fractions is not carried into the optotag-drd2 reason.

**3. Round-1 points**

Resolved:
- **B4 (burst windows):** The 3.5 to 6 ms variant gives 58 of 65, P = 7.6e-10. Why first spikes transmit less than single spikes remains unexplained, but this does not affect the outcome.
- **B5 (synchrony by shank):** No synchronous pair is on one shank, and spike coincidence is at most 5.8%.
- **B6:** Fisher's exact tests have been added.
- **B9:** The classification now uses the Methods' ratio, with agreement 0.953.
- **B10:** Home-cage awake time has been added as a variant, and no outcome changes.
- **B11:** The channel-map check found the electrodes table disagrees with the wide-band signal. This became a new finding, and mc-deeper now uses the wide-band site (P = 2e-40, holds in each of the 4 mice).
- **B12:** A unit-by-unit variant has been added.
- **B13:** Resolved by the 37 = 29 + 8 check above.
- **Chance level for inheritance-tmaze:** Added.

Partly resolved, and still bearing on a conclusion:
- **B1 (truncated waveforms):** gc-narrower-waveform on all 101 files still rests on truncated waveforms. Only the 17 wide-band files give an untruncated test (P = 0.017 unfiltered, P = 0.4 after a 300 Hz high-pass).
- **B2 (pooled interneurons):** interneuron-rates and first-stage-labels fall short only on the pooled interneuron labels. The 17-file subset on shanks with no CA3 unit passes (8.56 and 2.29 Hz; 94.4% below 0.425 ms). The partial outcomes may therefore reflect the labels, not the paper.
- **B3 (uncurated monosynaptic pairs):** The pairs are still the automatic detections: 65 against the paper's 32, with 8 MC→GC pairs. These pairs underlie monosyn-gc-to-mc, the not-reproduced state-transmission (P = 0.39, or 0.27 without the first-bin pairs) and both inheritance claims. This cannot be settled without the authors' unconverted pairs.
- **B8 (phase measures):** For theta-modulation, see section 1. The theta-reference channel was checked in 17 files only.

Still open:
- **Electrodes-table mismatch:** The notebook does not show whether the units' `electrode_group` or the table's column map is wrong. Zero same-shank synchronous pairs points to `electrode_group` being correct, which the B2 variants and the synchrony split depend on. Neither side is shown directly.
- **Blocked claims:** gc-mc-distance and gc-backpropagation stay blocked. That is reasonable, but no one tried recovering depth order from the wide-band columns.
- **Stored waveforms:** Their filtering and the 5× scaling are still undescribed.
