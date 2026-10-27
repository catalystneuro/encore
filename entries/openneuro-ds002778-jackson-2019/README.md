# Jackson, Cole, Voytek & Swann (2019) from OpenNeuro ds002778

Tests the findings of [Jackson et al. (2019)](https://doi.org/10.1523/ENEURO.0151-19.2019) on
[OpenNeuro ds002778](https://openneuro.org/datasets/ds002778/versions/1.0.5), snapshot 1.0.5, which
holds the resting EEG of 15 patients with Parkinson's disease off and on medication and 16 controls.
The paper's manual artifact marks and excluded electrodes are not in the dataset, so the analysis
rejects no samples and keeps all 32 scalp electrodes.

| Claim | Outcome |
|---|---|
| Beta sharpness ratio, steepness ratio and PAC fall with medication (C3/C4) | Partially reproduced (each test holds; one value per claim out of tolerance) |
| The same with a bipolar montage | Reproduced |
| No medication effect at F7/F8 or at T7/T8 | Reproduced |
| Topographies consistent with a sensorimotor origin | Partially reproduced |
| Off against controls: no difference in sharpness ratio or PAC | Reproduced |
| Off against controls: steepness ratio higher | Partially reproduced (FDR p 0.053) |
| Off against controls: PAC higher with a CSD montage | Not reproduced (p 0.075) |
| UPDRS improves with medication | Reproduced (W 3.5, p 0.0033) |
| Alpha and beta peaks in every group's spectrum | Not reproduced |
| Alpha sharpness and steepness fall with medication | Partially reproduced |
| Alpha PAC does not change with medication | Reproduced, resting on an assumption |
| Alpha off against controls | Partially reproduced |
| PAC change larger in beta than in alpha | Partially reproduced |
| Shape measures correlate with PAC (two claims) | Partially reproduced |
| Sensorimotor waveforms mostly in Q4, in patients and in controls | Reproduced |
| Q4 patient counts | Not reproduced (13 patients against 9) |
| F7/F8 waveform shape more variable | Reproduced |
| Effect sizes rise in Q4 patients | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/openneuro-ds002778-jackson-2019-01.yaml`](../../attempts/openneuro-ds002778-jackson-2019-01.yaml).

- `reproduce_jackson_2019.ipynb`: the analysis. It takes about two minutes, most of it reading the
  46 BDF files (0.57 GB) into memory.
- `waveshape.py`: listing and reading the pinned snapshot, the preprocessing, sharpness and
  steepness ratios, peak-to-trough and rise-to-fall ratios, PAC, the CSD transform and the
  statistics, with where each parameter comes from. Other notebooks on this dataset can import it.
