I rewrote `claims/peyrache-2015.yaml` from the paper alone, and the quote checker passes it with 0 problems.

**What I read.** The NIH author manuscript (PMC4376557) from Europe PMC: Results, Discussion, Methods and figure legends. Its three supplements were there too: the legends of Supplementary Figures 1 to 8, Supplementary Table 1 (recordings by animal), and the Nature Neuroscience reporting checklist, which gives exact p-values and sample sizes per test. The checklist numbers figures as in an earlier draft. There is no PDF of the article itself, so values printed only inside figures could not be read. The paper links no code, and the checklist answers N/A for custom software.

**What changed.** The old file was written after its author had seen the dataset's files. Several of its methods came from the data: finding the open field from position, pooling the two brain regions, how missing LED frames were handled. All of that is gone.
- **Kept:** 21 ids, with every criterion rewritten from the paper. The thalamic nucleus (ADn) and the post-subiculum (PoS) are now kept apart, as the paper does.
- **Split:** the readout windows moved out of `fig5e-adn-predicts-pos` into `fig5e-readout-windows`. The HD information of driven PoS cells moved out of `fig7d-same-preferred-direction` into `fig7e-driven-pos-hd-information`.
- **New, for findings that had no claim:** `recording-sample`, `supptable1-per-animal`, `hd-fraction-hd-shanks`, `supfig2a-unimodality`, `supfig5-rate-independent`, `fig2e-decoded-speed`, `fig4d-ole-near-bayesian`, `fig5b-sleep-tuning-similar`, `fig5d-adn-predicts-pos-reliably`, `fig6a-fast-oscillation`, `fig7e-interneurons-no-difference`.

**Counts.** 34 claims: 33 with quotes and 1 inferred (the Supplementary Table 1 counts). 15 claims carry statistics, 31 entries in all. All 34 have a criterion.

**Details the paper leaves open, with the readings named:**
- **HD cell rule:**
  - How the von Mises fit is made: a maximum-likelihood fit of the tuning curve taken as a distribution of angles, or a least-squares fit of a curve.
  - What sample the Rayleigh test uses.
  - Whether the peak rate is the fitted one or the tuning-curve maximum.
- **0.5 Hz rate threshold:** "in any of the three brain states" can mean in each state or in at least one.
- **Averages and counts:**
  - "41% on average" is an average over sessions or over animals; the pooled fraction is 34%.
  - Which sessions the "8.4 units per session" counts.
  - Which sessions make up the 42 in the text.
  - Which cells the 215/62 (Fig. 2a) and the 970/907 pairs (Fig. 2b against Fig. 3a) are.
- **Thresholds the paper never gives** for "strongly correlated", "similar", "faithfully", "remarkably similar" and "almost reached": I named readings or fixed a threshold, and said so in each criterion.
- **Angular-velocity fit:** the cross-correlogram bin and lag range, how the two directions of turning enter, and the coarse search grid.
- **Noise correlation:**
  - Lag: averaged over −50 to +50 ms (Methods), or at lag 0 (legend).
  - Scale: as the formula is written, or with 1 as chance (Supplementary Fig. 4).
  - The test of the sign at 0 and 60 degrees.
- **Packet coherence:** the distance between packets, how the reference vectors are drawn, and the smoothing windows.
- **Spike prediction model:**
  - The link function, read from the paper's ref 36.
  - Whether the predicting assemblies and the target cells are all cells or HD cells only.
  - The readout-window grid, and whether a window is the Gaussian's s.d. or its full width.
- **Fast synchrony:** the cross-correlogram bin and lag range, the wavelet, the amplitude measure (peak z or zero-lag z), and the offset groups.
- **Monosynaptic connections:**
  - Which pairs make up the 6960.
  - Whether the baseline is hollowed.
  - How the binomial test is set up: 14 of 20 against one half gives p near 0.12, not the reported 0.014.
- **PoS LFP triggered by ADn spikes:** the paper gives no test, so the control, the channel and the window are open.

**Missing from the paper:**
- **No OLE method.** The Results point to the Methods for the optimal linear estimator, but the Methods have no OLE section. `fig4d-ole-near-bayesian` and `fig4e-ole-covariance` use the standard Salinas and Abbott estimator, and both are marked as resting on that.
- **Session totals disagree.** Supplementary Table 1 sums to 50 sessions against 42 in the text.
- **Unreadable figure values.** The r values of the Fig. 2a,b insets and the errors of Fig. 4d are only inside figures, which are not available.
- **One garbled checklist value.** Its "p=1xe-8" was left out of the statistics and named in the file.
