# Johnson, King-Stephens, Weber, Laxer, Lin & Knight (2019) from CRCNS fcx-3

Tests the findings of [Johnson et al. (2019)](https://doi.org/10.3389/fnsys.2018.00065) on CRCNS
data set [fcx-3](https://doi.org/10.6080/K06971S9), which holds intracranial recordings from
prefrontal and parietal cortex of 7 patients doing a visuospatial working memory task, with the
preprocessed epochs and the paper's MATLAB scripts.

| Claim | Outcome |
|---|---|
| 192 analysed electrodes and 1129 pairs (Table 1) | Partially reproduced |
| Trials kept per subject and condition | Reproduced |
| Accuracy 0.63 to 0.98, no effect of condition | Reproduced |
| Identity RT longer than spatial and temporal | Reproduced |
| No ERP difference between conditions | Reproduced (assumption) |
| Power, identity against spatial (Figure 2) | Partially reproduced |
| Power, identity against temporal (Figure 3) | Partially reproduced |
| Identity > effects in the subjects with lower identity accuracy | Reproduced |
| Power effects at 2-7 and 9-24 Hz | Reproduced (assumption) |
| Parietal-led maintenance (Figure 4) | Not reproduced |
| Delta-theta shift with the test cue | Partially reproduced |
| Alpha-beta shift, still parietal-led | Not reproduced |
| 1008 and 984 directional pairs | Reproduced |
| Time-resolved delta-theta epochs (Figure 5A) | Not reproduced |
| Identity PFC-led early, parietal-led late | Not reproduced |
| Spatial and temporal PSI bidirectional | Not reproduced (assumption) |
| No sustained alpha-beta effect (Figure 5B) | Reproduced (assumption) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The phase slope index results depend on how PSI is computed, which the paper leaves open and the
deposited code does not settle, as it omits the conjugate of the cross-spectrum. The data set lists
187 analysed channels where the paper reports 192. The attempt record, with the reasons and the
differences from the paper's method, is
[`attempts/crcns-fcx-3-johnson-2019-01.yaml`](../../attempts/crcns-fcx-3-johnson-2019-01.yaml).

- `reproduce_johnson_2019.ipynb`: the analysis. It takes about 20 minutes, most of it streaming
  the 11.8 GB of tar.gz files, one subject at a time, with a peak of about 7 GB of memory.
- `fcx3.py`: streaming the files, the clock and timing checks, the power, ERP and PSI measures and
  the cluster test. Other notebooks on this data set can import it.
