# Wright and McDannald (2019) from CRCNS pag-1

Tests the findings of [Wright and McDannald (2019)](https://doi.org/10.7554/eLife.45013) on
[CRCNS pag-1](https://doi.org/10.6080/K0R49P0V), which holds the spike times, event times and mean
waveforms of 245 ventrolateral periaqueductal gray units recorded in 88 fear discrimination
sessions of six rats. All 39 claims of the claims file are tested.

| Claims | Outcome |
|---|---|
| Suppression ratios, poke correlations, clusters, Onset and Ramping populations (fig1c, fig1d, fig1s1b, fig1e, populations, fig1s5) | Reproduced |
| Population and single-unit firing of Onset and Ramping neurons (fig2a to fig2d, fig2e rate, fig2s2, fig4abc, fig4d, fig4h) | Reproduced |
| Single-unit regressions on probability and fear (fig5a to fig5j except one) and after the cue (fig6ab, fig6c, fig6d) | Reproduced |
| Baseline poke rates (fig1s1a), departure times (fig2e), single trials (fig2s1), Onset-Ramping pairs (fig3), Ramping biases (fig4efg), Ramping regressor combinations (fig5s1), delay against post-shock correlations (fig6ef) | Partially reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper states neither nose poke baseline of the suppression ratios. Its printed regression
input for one Onset neuron is reproduced by one unit of the data set only with a 2 s baseline for
interval fear, a 20 s baseline for total fear and 0/0 ratios set to 1. After this attempt asked
about it, the claims file gave the two ratios separate windows and added these choices to its
readings. That reading is the primary one, and every reading of the amended claims file is run;
several regression outcomes rest on the primary reading or on the trial's own firing baseline.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/wright-2019-01.yaml`](../../attempts/wright-2019-01.yaml).
