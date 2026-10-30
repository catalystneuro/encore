# Round-2 verification report: Buccino et al. 2024 on DANDI:000294 (attempt 000294-buccino-2024-01)

The claims file and the attempt record both have 23 claims. 10 are tested and 13 blocked: 1 for insufficient metadata and 12 as too large.

## 1. Outcomes

| Claim | Agree? | Note |
|---|---|---|
| recordings-two-cells-runs | Yes | 2 files with 5 and 4 runs; median run 195.8 s (cell 18). |
| ecode-protocol-structure | Yes | All checks pass under reading (a); the largest amplitude error is 1.2 points (cells 21–22). |
| holding-potential | Yes | −69.54 and −69.12 mV (cell 25). |
| extracellular-spikes-above-50uv | Yes | Negative peaks of 217.0 and 159.2 µV; every run is at least 159.2 µV (cell 28). |
| mea-electrodes-and-rates | Yes, with a reservation | The facts are right: the electrodes and the MEA rate pass, and the patch rate fails (cell 34). But the criterion has no partial clause, so read strictly the outcome is not_reproduced. The record now says this openly. |
| culture-age | Yes | blocked (metadata_insufficient). |
| fig6-ais-from-dendrite | Yes | In both cells the AIS parent point is type 3 (cell 38). |
| gt-rheobase | Yes | 150 and 140 pA; the code's own function gives the same (cell 41). |
| fig3b-ap-initiates-distal-ais | Yes | `assumed: true` is stated, and the assumption is reasonable; see below. |
| fig3a-largest-channel-at-ais | Yes | Channel 43 is nearest, 16.8 µm against 39.3 µm for the next. The recomputed template matches the file: correlation 0.99992, RMS difference 1.3% (cell 47). |
| table1-feature-counts | Yes | Counted on the code's evaluators: 76 / 87 / 109 / 153 (cell 50). |
| 12 fit claims | Yes | blocked (too_large). Even the cost printed in cell 53, 1699 + 1487 CPU-hours, is far beyond the limits. But the cost figures in the text do not match the printout; see §2. |

**The one assumption (fig3b) is stated and reasonable.**
- On the code's 0.05 ms cut-outs, the distal and middle AIS fall on the same sample under both readings (cell 44). So a strict reading of the criterion on those cut-outs would not give the order.
- Read between samples, the distal AIS leads by 0.0042 ms (crossing) and 0.0202 ms (peak).
- The independent fixed-step run (dt 0.005 ms) gives the order in 12 of 12 spikes under both readings.
- The paper does not say at what resolution the order was read, and the methods_unavailable finding asks the authors.

## 2. Sentences the printed outputs do not support

1. **Cost estimates (cell 54).** The text says "about 17 s intracellularly and about 28 s with the extracellular signals, so the ground-truth fits need more than 3000 CPU hours (more than 800 hours on this runner's 4 cores)". Cell 53 prints 8.0 s and 14.3 s, 1699 CPU-hours and 425 hours on 4 cores.
2. **Attempt record, fig4a-strategy-balance.** "16.8 s … 27.9 s … at least 3350 CPU hours, 837 hours on the 4 cores" is not what cell 53 prints. "In the first round the intracellular evaluation took 8.3 s" contradicts the notebook delivered now, which also gives 8.0 s.
3. **Attempt record, fig78a-soma-intra-all-extra.** "at least 2980 CPU hours": cell 53 prints 1487.
4. **The responses to round 1.** For fig4a and fig78a they repeat the same figures (3350 and 2980). These numbers seem to come from an execution other than the one delivered.
5. **README.** "The model fits need more than 3000 CPU hours" holds only for the two estimates added together (1699 + 1487 = 3186). It is not true of either set of fits alone.
6. **README.** "It takes about fifteen minutes": the printed timings add up to about 8.5 minutes (433 s at cell 53, plus 70 s at cell 56).
7. **Cell 32 and the record (extracellular-spikes-above-50uv).** "the code's mean template is higher by up to 13.3 uV": cell 28 shows 13.6 µV (negative peak) and 13.7 µV (peak-to-peak) for cell 1 run3.
8. **Cell 26 and the record (holding-potential).** "so the stored voltages are not corrected for the junction potential" is an inference. That reading (b) fails does not by itself show the data are uncorrected. It does not affect the outcome.
9. **The code_mismatch finding (796 extracellular features).** The printed 800 finite features (cell 56) are within the claims file's own tolerance (796 ± 80). The criterion also leaves out invalid values per model, so the difference may come from models, not code. As written, the finding is overstated.

Every other "**Result:**" sentence, the Summary, the rest of the README and the remaining notes match the outputs. Checked against cells 18, 21–22, 25, 28, 31, 34, 38, 41, 44, 47, 50 and 56; values checked include 92–98% of waveforms kept, 0.15–0.70 ms shifts, slopes of −0.003 to 0.023 ms per s, 6.6–16.1% RMS differences, the HyperDepol and validation spike counts, and 117–132 blank channels.

**My round-1 reasons in the record:** they are stated faithfully, close to my wording, for all 23 claims. The fig3a reason reproduces my round-1 error: I gave the 0.939 peak-to-peak ratio for channel 23, but cell 47 shows it is channel 24, at (−25, 25). The response corrects this correctly.

## 3. My round-1 points

**Resolved:**
- **1 (fig3b resolution):** run at the code's resolution, plus a fixed-step check. It is now an explicit assumption.
- **2 (fig3a placement):** the frame is fixed by the template match, and the nearest-electrode margin is now 16.8 µm against 39.3 µm.
- **3, 6, 7:** accepted as stated.
- **8:** the LFPy simulator is now used, and table1 is counted on the evaluators.
- **9:** the sub-parts are computed.
- **10:** recorded as a finding.
- **Alignment request from part C:** resolved. All 1616 spikes sit off the ±2 ms edge, and the slopes are about 1000 times smaller than a clock mismatch would give (cell 31).

**Kept but immaterial:** 4 (run choice) and 5 (2 SD cleaning).

**Remaining points that bear on a conclusion:**
- **The cost estimates for the 12 blocked claims** in the cell 54 text, the record notes and the round-1 responses, and partly the README, do not match the delivered outputs (§2, items 1–5). The blocked outcome stands either way, but the stated reason has to cite the printed numbers.
- **mea-electrodes-and-rates:** partially_reproduced is not an outcome the criterion provides for; read strictly it is not_reproduced.
- **fig3b:** reproduced only under the stated resolution assumption. At the code's own samples the two AIS points tie.
- **The 796 finding:** it should be reworded or dropped, since 800 is within the claims file's tolerance.

**Where the claims file misreads the paper:** these are unchanged from round 1. They are reported, not corrected.
- **APWaveform rate:** it allows only 20 or 200 kHz where the paper says "typically 200 kHz".
- **Holding potential:** it treats the code's `ton` as the pre-stimulus point, but in the files the stimulus starts 50 ms earlier.
