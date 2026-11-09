# Martini, Molano-Mazon & Maravall (2017) from CRCNS ssc-6

Tests the findings of [Martini et al. (2017)](https://doi.org/10.1093/cercor/bhx019) on CRCNS data
set [ssc-6](https://doi.org/10.6080/K02F7KCP), which holds the raw 2-photon movies and stimulus
files of 49 fields in 10 anesthetized mice. The data set holds no ROIs or traces, so the notebook
registers the movies, finds the ROIs again and rebuilds every measure from the Methods.

| Claim | Outcome |
|---|---|
| 10 mice, 49 fields, 4 recordings, 10 presentations, 1054 neurons | Partially reproduced |
| Three waveforms at amplitudes 1:3:5, randomly interleaved, 1 s apart | Partially reproduced |
| Example neuron coefficients (Figure 2A, B) | Blocked: metadata insufficient |
| 50.2% of neurons responded | Not reproduced |
| 71.8% of neurons non-tuned | Reproduced |
| All tuning classes represented | Reproduced |
| Tuning consistent across halves (95% and 81%) | Reproduced |
| Shuffle-based tuning gives the same conclusions | Reproduced |
| Example field correlation (Figure 3B) | Blocked: metadata insufficient |
| Correlations above shuffled (0.1004 against 0.011) | Partially reproduced |
| Neuropil more correlated than neurons | Partially reproduced |
| Example field correlation against distance (Figure 3D) | Blocked: metadata insufficient |
| Correlations fall with distance (-0.29 per mm) | Partially reproduced |
| No gradient beyond 200 um | Reproduced |
| Example field SI against distance (Figure 3F) | Blocked: metadata insufficient |
| No spatial organisation of tuning similarity | Reproduced |
| Tuned neurons even across barrels and septa (Figure 4C) | Blocked: metadata insufficient |
| Border distance does not differ by feature (Figure 4D) | Blocked: metadata insufficient |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/martini-2017-01.yaml`](../../attempts/martini-2017-01.yaml).

- `reproduce_martini_2017.ipynb`: the analysis. It takes about 27 minutes, 17 of them streaming
  the 8 GB tar file and reducing each field to ROI traces.
- `ssc6.py`: streaming the tar, registration, ROI detection, traces, dF/F0, responses, tuning
  regressions, the false discovery rate procedure, and the correlation shuffles. Other notebooks
  on this data set can import it.
