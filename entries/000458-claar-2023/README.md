# Claar, Rembado et al. (2023) from dandiset 000458

Tests the findings of [Claar et al. (2023)](https://doi.org/10.7554/eLife.84630) on
[DANDI:000458](https://dandiarchive.org/dandiset/000458/0.230317.0039), version 0.230317.0039, the version the
paper cites. The dandiset holds the skull EEG, Neuropixels LFP and sorted units of 23 mice stimulated with single
current pulses in superficial or deep layers of MOs or SSp, awake, under isoflurane and in recovery.

| Claim | Outcome |
|---|---|
| Stimulation depths of superficial and deep sites | Blocked: data missing |
| 23 +/- 4 good EEG electrodes per subject | Reproduced |
| Deep stimulation evokes two ERP peaks, superficial lacks the late one | Not reproduced |
| Example ERP lasts 1.01 s with magnitude 11.13 SD.s | Reproduced |
| ERP duration does not differ significantly with depth | Reproduced |
| ERP magnitude is smaller with superficial stimulation | Reproduced (assumption) |
| The first ERP peak flips sign with distance | Blocked: data missing |
| Quiescence after superficial MOs stimulation | Reproduced |
| Triphasic response of stimulated cortex to deep stimulation | Partially reproduced |
| Triphasic response of SM-TH | Partially reproduced |
| LFP, CSD and spiking magnitudes by region (Figure 3, two claims) | Blocked: metadata insufficient |
| RS unit counts of Figure 4 | Not reproduced |
| Modulated units at 2 to 25 ms | Not reproduced |
| Modulated units at 25 to 150 ms | Not reproduced |
| Rebound excitation at 150 to 300 ms | Partially reproduced |
| FS units behave like RS units | Partially reproduced |
| SM-TH units more often modulated by deep stimulation | Reproduced |
| SM-TH burst probability higher with deep stimulation | Partially reproduced |
| Cortex fires before SM-TH in the initial excitation | Partially reproduced |
| SM-TH fires before cortex in the rebound | Not reproduced |
| CSD by layer (Figure 6A and its supplement 1) | Blocked: metadata insufficient |
| SM-TH bursts correlate with cortical rate | Not reproduced |
| Cortical rate correlates with the late ERP | Not reproduced |
| The late ERP correlates with SM-TH bursts more than with SM-TH rate | Reproduced |
| Trial counts per state | Reproduced |
| ERP duration and magnitude across states | Reproduced (magnitude rests on an assumption) |
| Baseline rates across states | Reproduced |
| Early latencies do not change with state | Reproduced (assumption) |
| Rebound latencies earlier when running | Partially reproduced (assumption) |
| Burst probability across states | Partially reproduced |
| PCIst awake against anesthetized | Partially reproduced |
| PCIst lower with superficial stimulation | Reproduced |
| PCIst across quiet, running and anesthetized | Partially reproduced |
| PCIst in recovery | Reproduced (one reading) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper does not say which of the three currents of each stage it analysed; every analysis is run at the highest
and at the middle current, and several outcomes depend on the choice. The files carry no cortical layers and no
position or depth of the stimulating electrode, which blocks five claims. The RS unit counts of Figure 4 are three
times the counts of units in the files. The attempt record, with the reasons and the differences from the paper's
method, is [`attempts/000458-claar-2023-01.yaml`](../../attempts/000458-claar-2023-01.yaml).

- `claar_eeg.ipynb`: the EEG claims (Figures 1, 7C, 7D, 8). About 15 minutes, most of it streaming the EEG.
- `claar_spikes.ipynb`: the spiking claims (Figures 2, 4, 5, 6B, 6C, 7E to 7H). About 14 minutes.
- `claar.py`: loading, trial states, EEG epochs and ERP measures, PCIst with the paper's parameters, and the
  spiking measures. Other notebooks on this dandiset can import it.
