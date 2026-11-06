# Varela and Wilson (2020) from CRCNS hc-24

Tests the findings of [Varela and Wilson (2020)](https://doi.org/10.7554/elife.48881) that can be
tested on [CRCNS hc-24](https://doi.org/10.6080/K0K35RVG), which holds three of the paper's
sessions from three rats: units, tetrode multi-unit activity and LFP from the midline thalamus,
mPFC and CA1, with derived sleep periods, K-complexes, spindle troughs and SWRs. The third session
is sleep after maze exploration, with CA1 units labelled as active or not on the maze. The maze
epoch, sleep before the maze, position data and most of the paper's units are not in the data set.

| Claim | Outcome |
|---|---|
| fig1s3-spindles-not-theta | Partially reproduced (resting on an assumption) |
| fig2-swr-phase-delta-spindle | Reproduced |
| fig2c-swr-around-kc | Partially reproduced |
| fig3a-thalamic-rate-wake-sleep | Blocked: other |
| fig3a-bursting-in-sleep | Blocked: other |
| fig3a-bursting-around-swrs | Blocked: other |
| swr-shift-control | Blocked: other |
| fig3c-thalamic-decrease-at-swrs | Blocked: other |
| fig3s1-ca1-mpfc-at-swrs | Partially reproduced |
| glm-thalamus-anticorrelated-swrs | Not reproduced |
| glm-re-versus-other-nuclei | Blocked: metadata insufficient |
| fig3e-thalamic-rebound-after-kc | Partially reproduced |
| kc-trough-timing | Reproduced |
| kc-fraction-of-thalamic-peaks | Blocked: other |
| kc-ca1-mpfc-symmetric | Partially reproduced |
| kc-regions-compared | Partially reproduced |
| fig3f-asymmetry-index | Reproduced |
| spindle-mua-modulation | Blocked: other |
| fig4-units-not-rhythmic | Not reproduced |
| fig4b-thalamic-pairs-correlated | Blocked: other |
| xcorr-stronger-in-spindles | Blocked: other |
| fig5c-spindle-phase-locking | Blocked: other |
| fig5c-delta-phase-locking | Partially reproduced |
| phase-robust-to-spike-count | Blocked: other |
| rebound-delta-phase-trend | Reproduced |
| fig5d-phase-lags-consistent | Blocked: other |
| spindle-cycles-by-ripple-power | Partially reproduced |
| fig6-modulation-with-ripple-power | Blocked: other |
| modulation-amplitude-versus-ripple | Blocked: other |
| fig6e-quartile-synergy | Blocked: other |
| fig6f-quartile-versus-median | Blocked: other |
| fig6g-spike-count-unchanged | Blocked: other |
| xcorr-pairs-ripple-modulation | Blocked: other |
| thalamus-at-spindle-nested-swrs | Blocked: other |
| mpfc-units-coupled-swrs | Reproduced |
| mua-coupled-swrs | Blocked: other |
| maze-swr-kc-increase | Blocked: data missing |
| maze-control-sessions | Blocked: data missing |
| maze-ripple-power-in-spindles | Blocked: data missing |
| fig7c-run-units-in-spindles | Not reproduced |
| maze-ca1-rates-similar | Reproduced |
| fig7d-run-units-peri-swr | Partially reproduced |
| fig7b-run-units-spindle-phase | Partially reproduced |
| fig8-thalamus-unchanged-by-maze | Blocked: data missing |
| fig8e-ca1-spindle-trend | Blocked: data missing |
| thalamus-not-selective-for-run-cells | Blocked: other |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Most claims about thalamic units are blocked because the data set holds 5 thalamic units (the
paper 63) and 2 thalamic pairs (the paper 39): a test over so few units cannot reach the paper's
significance level, or a percentage cannot fall within its tolerance. The record, with the
reasons and the differences from the paper's method, is
[`attempts/crcns-hc-24-varela-2020-01.yaml`](../../attempts/crcns-hc-24-varela-2020-01.yaml).

- `reproduce_varela_2020.ipynb`: the analysis, about six minutes, streaming `data.zip` from the
  CRCNS bucket.
- `sleepcoord.py`: loading the zip in place, the filters and event detection rules of the
  Methods, peri-event histograms against shifted-event nulls, phase measures and the Rayleigh test
  of the deposited scripts, and burst detection. Other notebooks on this data set can import it.
