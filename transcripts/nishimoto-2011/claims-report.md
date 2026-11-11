I wrote `claims/nishimoto-2011.yaml`. The quote checker reports 20 claims, 20 quotes, 11 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record (`paper/10.1523-jneurosci.6801-10.2011.txt`), with the main text, Materials and Methods and figure legends. The paper has no supplement apart from Movie 1, which shows stimulus spectra and is not a result. I opened the PDF only for:
- the inequality signs of the p-values, which the extraction garbled;
- the bar heights in Figure 2B, which print no numbers.

The paper links no code, so there was no repository or commit to read.

**Claims:** 20. All 20 have quotes, none is inferred, 11 record statistics, 11 have expected values and all 20 have criteria. They cover:
- **Prediction accuracy:** mean r = 0.52; 35% of explainable variance; an example neuron with r = 0.72.
- **Model comparison in Figure 2B:** luminance and contrast normalization has no significant effect; the compressive nonlinearity helps (about +16% and +19%); the expansive one hurts (about −36% and −24%); divisive normalization helps (about +8%); compressive plus divisive beats compressive alone; the effects do not depend on divisive normalization.
- **Complex cells:** they carry most of the response variance (the paper shows no data for this).
- **On-plane ratio:** excitatory 0.59 against a null of 0.36; suppressive 0.18.
- **Ring structure:** most neurons have a horizontal-vertical ratio between the extremes (partial rings).
- **Plaid simulation:** pattern indices mostly from −6 to 2; correlation with the horizontal-vertical ratio r = 0.46.
- **Two absence claims:** prediction performance is not correlated with the horizontal-vertical ratio or with the pattern index.
- **Controls:** the natural-movie control (r = 0.533 against 0.537); recovery of simulated receptive fields in Figure 8.

**Details the paper leaves open, with the readings named:**
- **cRF size:** half the stored patch, or the full patch as the analysis window.
- **Delays:** "10 frames or 130 ms" disagree at 83 Hz, so 0 to 10 frames or 1 to 10.
- **12 ms Gaussian:** its SD or its full width at half maximum.
- **Semisaturation constant:** chosen on held-out training data, or fixed.
- **20% hold-out parts:** contiguous blocks or random frames.
- **Compressive power:** applied to all filter outputs (taken), with simple cells only as a variant.
- **Gabor details:** the temporal width and the exact velocities are not given; I used a standard choice.
- **"Increase of predictive power":** the change in mean r, in mean r², or per-neuron change, averaged.
- **Bonferroni count:** 11 or 5 comparisons.
- **Explainable variance:** two ways of averaging the David and Gallant (2005) noise ceiling.
- **On-plane ratio:**
  - balance of the two constraints, which the authors set by hand: coverage only, or both summed with equal weight;
  - what is summed: weights, or weights times spectral amplitude;
  - where the sign is split: per delay, or after summing over delays.
- **Null model:** which neuron's movies it is driven with, how rates are scaled for the Poisson noise, which delays the random weights span, and whether the suppressive test compares against the null's excitatory or suppressive ratios.
- **Horizontal-vertical ratio:** which amplitudes count as on the plane, and where the "extremes" end (0.2/0.8 or 0.1/0.9).
- **Plaid simulation:** grating and plaid frequencies (per neuron or shared) and component separation (120° or 90°).
- **Figure 8:** noise level, and the comparison measure (the file fixes one, since the paper names none).
- **Thresholds the paper gives as words only:** "most variance" for the complex-cell claim and "rare" for pattern-selective neurons are set by the file and say so.

**What the paper does not give, or contradicts:**
- **No numbers for Figure 2B.** Its values are read from the bars with a 4-point tolerance, and the reason is stated in the file.
- **Contradictions:**
  - The Methods say 20,000 to 40,000 training frames; the Results say 22,000 to 42,000.
  - Figure 2's legend says open bars are models with luminance normalization and filled bars without it; the figure's own key shows the reverse.
- **Possible data gaps, left for the author to check:**
  - The dataset holds 45 neurons; the paper used 52.
  - The explainable-variance claim needs the single validation repeats. The dataset's description lists only averaged PSTHs, so if the repeats are absent that claim is blocked.
  - The natural-movie control needs the second validation set for the 15 neurons; the same applies.

The working tree also shows untracked files I did not create (`.bashrc`, `.idea`, `scripts` and others). I left them alone.
