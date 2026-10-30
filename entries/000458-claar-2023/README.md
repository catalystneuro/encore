# Claar, Rembado et al. (2023) from dandiset 000458

Tests the findings of [Claar et al. (2023)](https://doi.org/10.7554/eLife.84630) on
[DANDI:000458](https://dandiarchive.org/dandiset/000458/0.230317.0039), version 0.230317.0039, the version the
paper cites. The dandiset holds the skull EEG of 23 mice, and Neuropixels LFP and sorted units for 17 of them (18
sessions), stimulated with single current pulses in superficial or deep layers of MOs or SSp, awake, under
isoflurane and in recovery.

| Claim | Outcome |
|---|---|
| Stimulation depths of superficial and deep sites | Blocked: data missing |
| 23 +/- 4 good EEG electrodes per subject | Reproduced |
| Deep stimulation evokes two ERP peaks, superficial lacks the late one | Not reproduced |
| Example ERP lasts 1.01 s with magnitude 11.13 SD.s | Reproduced (medium current) |
| ERP duration does not differ significantly with depth | Partially reproduced |
| ERP magnitude is smaller with superficial stimulation | Reproduced (medium current) |
| The first ERP peak flips sign with distance | Blocked: data missing |
| Quiescence after superficial MOs stimulation | Reproduced |
| Triphasic response of stimulated cortex to deep stimulation | Partially reproduced |
| Triphasic response of SM-TH | Partially reproduced |
| LFP, CSD and spiking magnitudes by region (Figure 3, two claims) | Blocked: metadata insufficient (proposed after round 2: the example session partially reproduced, Figure 3D too large) |
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
| ERP duration and magnitude across states | Partially reproduced (two claims) |
| Baseline rates across states | Reproduced |
| Early latencies do not change with state | Reproduced (assumption) |
| Rebound latencies earlier when running | Partially reproduced (assumption) |
| Burst probability across states | Partially reproduced |
| PCIst awake against anesthetized | Reproduced (medium current) |
| PCIst lower with superficial stimulation | Reproduced |
| PCIst across quiet, running and anesthetized | Partially reproduced |
| PCIst in recovery | Reproduced (one reading) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper does not say which of the three currents of each stage it analysed; every analysis is run at the highest
and at the middle current, and several outcomes depend on the choice. The middle current with all awake trials gives
the paper's example ERP (1.011 s and 11.133 SD.s against 1.01 and 11.13) and its p-values for Figures 1E and 1F,
which points to it as the paper's choice. The files carry no cortical layers and no
position or depth of the stimulating electrode. Six claims are blocked in the record: the stimulation depths, the
sign flip of the first ERP peak, the CSD by layer (two claims) and the two Figure 3 claims. The RS unit counts of Figure 4 are three times the counts of units in
the files; counting each unit once per current gives the legend's first three counts exactly and 9486 against
9363. After the second verification round the LFP and CSD magnitudes of the example session were computed, with
layer 1 approximated by the top 100 um of each area; they support a partial reproduction of Figure 3A to 3C,
which the record proposes for a third round. The spiking magnitudes of Figure 3 come near the paper's, in the example and with deep
stimulation, only when falls below baseline are counted (|z|). The attempt
record, with the reasons and the differences from the paper's
method, is [`attempts/000458-claar-2023-01.yaml`](../../attempts/000458-claar-2023-01.yaml).

- `claar_eeg.ipynb`: the EEG claims (Figures 1, 7C, 7D, 8). About 17 minutes, most of it streaming the EEG.
- `claar_spikes.ipynb`: the spiking claims (Figures 2, 4, 5, 6B, 6C, 7E to 7H) and the spiking part of Figure 3.
  About 20 minutes.
- `claar_lfp.ipynb`: the LFP and CSD magnitudes of the example session of Figure 3, and the size of the Figure 3D
  computation. About 8 minutes.
- `claar.py`: loading, trial states, EEG epochs and ERP measures, PCIst with the paper's parameters, the
  spiking measures, and the LFP and CSD magnitudes. Other notebooks on this dandiset can import it.
