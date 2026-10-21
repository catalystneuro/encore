# Hires, Gutnisky, Yu, O'Connor & Svoboda (2015) from dandiset 000013

Tests the findings of [Hires et al. (2015)](https://doi.org/10.7554/eLife.06619) on
[DANDI:000013](https://dandiarchive.org/dandiset/000013/0.220126.2143), which holds the paper's 52
loose-seal recordings (31 L4 cells in C2, 10 L4 cells outside C2, 11 L5 cells near C2), each with
millisecond whisker tracking, touches, licks and trials, from mice locating a pole with one
whisker.

| Claims | Outcome |
|---|---|
| Recording counts, behavioural performance, sample epoch | Reproduced |
| The Figure 1 example cell: rates, sample-epoch Fano factor, spikes per touch, phase modulation | Reproduced (cell 23) |
| Touch responses weaker outside C2; L5 rates higher; phase modulation L4 vs L5 and inside vs outside | Reproduced |
| Modulation indices of Figure 5C; touch clusters; Fano factor near the binomial limit | Reproduced |
| Fano factors of Figure 6E (five conditions); spikes per whisk cycle | Reproduced |
| Whisking bouts; touches and reaction time; example cell's touch window; rate change with whisking (L4, L5) | Partially reproduced |
| Mice and lines; whisking rates in the text; how many cells have a latency; time and phase decoding (Figure 4B, 4C) | Not reproduced |
| Table 1; touch and phase coupled spikes (Figure 3C, 3D); touch detection (Figure 4A); Figure 5 correlations; refractory model (Figure 6D); Figure 6B example | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

Most of the blocked claims turn on one question asked in
[`questions/000013.yaml`](../../questions/000013.yaml): where the search for the touch-window
cutoff starts. The files fall in batches that were converted differently: in 36 of them the
spike train's timestamps run 10 ms ahead of the voltage they were detected from, and in 38 the
stored `theta_filt` is not the band-passed angle and the voltage's unit conversion is off by
1000.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000013-hires-2015-01.yaml`](../../attempts/000013-hires-2015-01.yaml).

- `reproduce_hires_2015.ipynb`: the analysis. It takes about ten minutes, two of them streaming
  the files.
- `hires.py`: loading the files, the touch, whisking and exploration epochs, latencies, touch and
  phase windows, the decoders and the touch grouping. Other notebooks on this dandiset can import
  it.
