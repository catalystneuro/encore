I rewrote `claims/tingley-2019.yaml` to the current protocol. The quote checker passes: 39 claims, 39 quotes, 13 statistical values, 0 problems. Nothing is committed.

**Text read.** The accepted author manuscript in PubMed Central (PMC6952543): full Results, Discussion, STAR Methods, figure legends and Key Resources Table, plus its one supplement (Figures S1 to S5 with legends). There is no PDF of the main paper, so values printed only inside main figure panels could not be read.

**Code read.**
- `DavidTingley/papers` at commit 9f4cd48. It holds the 2018 paper's figure scripts and the Figure 8 model notebook. It has no analysis code for Figures 1 to 7.
- `buzcode` at commit e615663, `bz_FindRipples.m`, the detector the Methods name. This is the current version, not one dated to the paper.

**Counts.** 39 claims; all 39 have quotes and none needed `inferred`. 10 claims have statistics and all 39 have criteria. One claim, `fig8-model`, is `data: elsewhere`, pointing at the model notebook.

**What changed from the old file.**
- **Header:** removed the record of outputs from the data that an earlier author had seen, and the method choices taken from the data (region labels, state names, epoch names). Every method detail is now cited to the paper or code, or named as open. Added provenance, the code commits and a description of the data the paper used.
- **New claims:**
  - `fig1c-post-burst-suppression`
  - `figs3d-hpc-compression-post`
  - `figs2c-no-ls-reactivation`
  - `ls-spikes-not-locked-to-ca1-ripples`
  - `figs5-seqnmf-variance`
  - `fig7e-coupled-only`
  - `discussion-medial-septum`
  - `discussion-cingulate-down-state`
- **Changed claims:** all ids kept.
  - `fig7e-ca1-depth` now has an expected value of 23%, and `fig7e-replay` and `fig7e-seqnmf` now have expected values.
  - Fig 7E significance now follows the legend: a two-sided t-test of the shuffled errors against the actual error.
  - Sample sizes (7,172 pairs, 42 recordings, 1,313 neurons, the Figure S2A counts) are added as expected values.
  - `fig4b-hfo-above-behav` now includes the result that behaviour-epoch correlations are slightly above chance.
  - `fig2ef-intermediate-ls` now uses the Figure S1C/D polynomial-order test.
  - `fig4-sessions-few-change` drops an invented minimum number of pairs per session.

**Details the paper leaves open, and the readings named:**
- **Detection channel:** the events or parameters stored with the data (the Methods say they are stored), or else the channel with the highest 120-200 Hz power.
- **Event time:** the code's trough, or the peak-power bin.
- **Merge interval and EMG threshold:** the code's defaults, 30 ms and 0.9.
- **WAKE:** all waking, or waking outside maze trials.
- **Phase locking:** which LFP channel; band 120-200 Hz (Methods) or 120-180 Hz (legend); denominator neurons with more than 50 spikes, or all LS neurons.
- **Participation:** counting window, and how the mean is taken.
- **Travelling-wave speed:** regression slope, or median of distance over lag.
- **Excess correlation:** what the "more than 5 spikes" inclusion rule means, kernel SD or full width, how the correlogram is normalized, and which behaviour-epoch spikes count.
- **Temporal bias and other t-tests:** paired or two-sample.
- **Compression:** which factors between 1 and 50, and which tests.
- **Correlogram bins** for Figure 5, and the coherence measure and jitter.
- **Fig 1H:** the test, Pearson or Spearman.
- **Fig 5B:** the test for "lower".
- **Fig 7E:** the regression model, cross-validated or in-sample error, what is shuffled, how many shuffles, and the firing window.
- **Replay scores:** decoder and bin sizes.
- **seqNMF:** template length, penalty and binning, and how a template becomes a per-ripple feature.
- **Opto:** how the spectrum is estimated, and where the window sits on the stimulus.
- **Fig 8:** what "nearly identical" means; I set a 10% bound plus an ANOVA.
- **Medial septum and cingulate claims:** no method at all; the criteria fix one.

**Missing from the paper:**
- **Seventh Figure 7E feature:** the text names only six of the seven ripple features that don't depend on spike content; the seventh is only on the figure axis, which I could not see. `fig7e-content-independent` tests the six named ones.
- **Mislabelled sentence:** the Methods describe "the dataset used for Figure 6", but the content is Figure 7's, so I read it that way.
- **No analysis code** for Figures 1 to 7 exists in the linked repository.
- **Figure S2A neuron counts:** which count belongs to which region is inferred from the order of the legend.
