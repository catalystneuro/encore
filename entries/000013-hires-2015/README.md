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
| Table 1 for L4 C2; the L5 rate increase with whisking | Reproduced |
| Touch responses weaker outside C2; L5 rates higher; phase modulation L4 vs L5 and inside vs outside | Reproduced |
| Modulation indices of Figure 5C; touch clusters; Fano factor near the binomial limit | Reproduced |
| Fano factors of Figure 6E (five conditions); spikes per whisk cycle | Reproduced |
| Table 1 for L5 | Partially reproduced |
| Mice and lines; whisking bouts; touches and reaction time; example cell's touch window; whisking rates in the text; how many cells have a latency; time decoding (Figure 4B); phase decoding (Figure 4C) | Not reproduced |
| Table 1 for L4 outside C2; rate change with whisking in L4; touch and phase coupled spikes (Figure 3C, 3D); touch detection (Figure 4A); Figure 5 correlations; refractory model (Figure 6D); Figure 6B example | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The first run asked seven questions in
[`questions/000013.yaml`](../../questions/000013.yaml), and a reader answered them from the
paper. With the touch-window cutoff set to the transition where the curve levels off, Table 1
for L4 C2 is reproduced and for L5 partially; the Figure 3 claims stay blocked on the range of
the cutoff curve (100 or 200 ms), which the paper does not give.

After the first verification round, whisking periods leave out licking and the 70 ms after
touch, phase tuning uses every phase-analysis cycle of the trial, and the touch detector's
fraction detected is read at the time point of best percent correct. Five outcomes changed:
whisking bouts, touches and reaction time, and the example cell's touch window are now not
reproduced (their criteria have no partial rule), the L4 rate change with whisking is blocked
(its two readings of whisking disagree), and phase decoding is not reproduced (C2 is far from
24 deg and worse than outside C2 under every reading).

The files fall in batches that were converted differently: in 36 of them the spike train's timestamps run 10 ms ahead of the voltage they were detected from, and in 38 the
stored `theta_filt` is not the band-passed angle and the voltage's unit conversion is off by
1000.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000013-hires-2015-01.yaml`](../../attempts/000013-hires-2015-01.yaml).

- `reproduce_hires_2015.ipynb`: the analysis. It takes about twelve minutes, two of them streaming
  the files.
- `hires.py`: loading the files, the touch, whisking and exploration epochs, latencies, touch and
  phase windows, the decoders and the touch grouping. Other notebooks on this dandiset can import
  it.
