# ten Brinke et al. (2017) from CRCNS cb-1

Tests the findings of [ten Brinke et al. (2017)](https://doi.org/10.7554/eLife.28132) that can be tested on
[CRCNS cb-1](https://doi.org/10.6080/K0B85697), which holds 372 interpositus nucleus recordings with per-trial
eyelid and spike traces: 270 made over the course of eyeblink conditioning and 102 made after it. Recording
depth, the US-only trials, the optogenetic sessions and the Purkinje cell data of the paper are not in it. Four
claims take recording depth from the paper's Source data 1 on eLife, which gives it for the 270 first-dataset
cells only; a link claim checks that its cells are the data set's, in the same order.

| Claim | Outcome |
|---|---|
| source-data-1-link (link) | Reproduced |
| firing-rate-depth | Reproduced |
| fig1ijk-modulation-classes | Partially reproduced |
| modulation-absolute-not-rate-dependent | Partially reproduced |
| fig1l-cells-with-behavior | Reproduced |
| fig1m-modulation-grows-with-training | Reproduced |
| fig1no-modulation-more-with-behavior | Reproduced |
| fig2a-facilitation-properties-ds1 | Partially reproduced |
| fig2b-facilitation-trial-correlations-ds1 | Reproduced |
| fig2b-lmm-ds1 | Reproduced |
| fig2d-facilitation-leads-eyelid-ds1 | Partially reproduced |
| fig2-s1-correlation-matrix-offsets | Not reproduced |
| fig2e-facilitation-ds2 | Reproduced |
| fig2f-facilitation-trial-correlations-ds2 | Reproduced |
| fig2f-lmm-ds2 | Reproduced |
| fig2h-facilitation-leads-eyelid-ds2 | Partially reproduced |
| fig2-suppression-properties-ds1 | Partially reproduced |
| suppression-smaller-shorter-than-facilitation | Reproduced |
| suppression-same-timing-as-facilitation | Not reproduced |
| fig2j-suppression-trial-correlations-ds1 | Reproduced |
| fig2l-suppression-no-lead-ds1 | Not reproduced |
| fig2n-suppression-ds2 | Partially reproduced |
| ds2-stronger-facilitation-same-suppression | Partially reproduced |
| fig2p-suppression-no-lead-ds2 | Not reproduced |
| ds2-modulation-proportion | Reproduced |
| fig3-optogenetic-inhibition-abolishes-crs | Blocked: data missing |
| fig4b-cs-pause-ds1 | Partially reproduced |
| fig4c-cs-pause-ds2 | Partially reproduced |
| fig4g-cs-pause-latency-cr-latency | Reproduced |
| fig4s1-cs-peak-cells | Reproduced |
| fig4s1-cs-peak-suppression-not-different | Reproduced |
| fig4h-transient-responses-after-day-3 | Reproduced |
| fig5cd-cs-pause-faster-facilitation-ds1 | Reproduced |
| fig5hi-cs-pause-faster-facilitation-ds2 | Reproduced |
| fig5ej-cs-pause-cells-shallower | Blocked: data missing (second-dataset depth) |
| fig5s1-model-timing | Blocked: data missing |
| fig6-us-peak-prevalence | Partially reproduced |
| fig6c-us-peak-declines-with-training | Partially reproduced |
| us-peak-anticorrelates-with-behavior | Reproduced |
| fig6d-us-peak-trial-correlations | Partially reproduced |
| us-peak-cooccurs-with-facilitation | Partially reproduced |
| fig6s1a-eyelid-opening-us-peak | Reproduced |
| fig6s1bc-purkinje-us-complex-spike-opening | Blocked: data missing |
| us-pause-prevalence | Reproduced |
| cs-pause-cells-have-us-pause | Reproduced |
| fig6b-us-peak-pause-overlap | Partially reproduced |
| fig6g-us-response-depth | Reproduced |
| us-pause-declines-with-training | Reproduced |
| fig6h-us-pause-trial-correlations | Reproduced |
| fig7-second-us-peak | Partially reproduced |
| fig7-second-us-peak-dynamics | Partially reproduced |
| fig7c-second-peak-cells-lower-cr | Partially reproduced |
| fig7b-first-second-peak-correlated | Not reproduced |
| us-only-trials-ds2 | Blocked: data missing |
| fig7s1c-us-only-second-peak-cs-pause-cells | Blocked: data missing |
| fig7fg-us-pause-resembles-cs-pause | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the
differences from the paper's method.

The paper links no analysis code, and several of its definitions are open; the notebook runs every reading the
claims file names, and the classification of cells into facilitation, suppression and no modulation does not
give the paper's counts under any of them. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/brinke-2017-01.yaml`](../../attempts/brinke-2017-01.yaml). The helper `ipn.py`
streams the data set's one file from the CRCNS bucket, and Source data 1 from eLife, and holds the measures.
