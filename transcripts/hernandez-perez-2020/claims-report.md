I wrote `claims/hernandez-perez-2020.yaml`. The quote checker reports 24 claims, 24 quotes, 53 statistical values and 0 problems. Nothing is committed.

**Text read.** The version of record (PMC7046467, Europe PMC full-text XML), with Results, Methods, all figure legends and the only supplement, the Figure 1 histology legend. There was no PDF, so no figure could be read. One equation, the asymmetry-related delay, was lost when the text was extracted. I read it from the same Europe PMC XML: Delay_Asym = (D_falling,i − D_rising,i) − (D_falling,j − D_rising,j). The paper links no analysis code; it names only "custom scripts" and the CMBHOME toolbox. The dataset's own code folder holds loading and plotting scripts only.

**Claims.** All 24 have quotes, none is `inferred`, 21 have statistics and all 24 have criteria. They cover:
- the LFP phase shift of 26.36°/mm, its linear fit, and its presence in every rat;
- phase locking and coherence: their levels and their decrease with distance;
- no change in theta power along the axis;
- the laminar-array test, along against across the layers;
- multi-unit traveling waves, and that their slope matches the LFP's;
- waveform asymmetry: the dorsal-to-ventral gradients, and the asymmetry at the dorsal sites and at about 2.8 mm;
- conduction delay by phase, its slope with phase, and the conversion to degrees;
- the asymmetry-related, total and residual delays;
- the Figure 8 relative and absolute delay slopes, their correlation strengths, and the coupled-oscillator conclusion.

**Open details and the readings named:**
- **Electrode positions:** the nominal 566 µm spacing, or per-rat spacings. One array's measured spacing is not in the text.
- **Channels used:** all channels in the file, or only those marked inside the MEC.
- **Artefact and theta-epoch scope:** per channel, on all channels at once, or from the dorsal-most channel.
- **The test printed "rank sum [max]":** its numbers (maximum 21, p = 0.03, 0.06, 0.09, 0.16, 0.84 at n = 6) fit an exact signed-rank test, so I read it as one.
- **Significance level:** not stated. The paper calls p = 0.06 significant, so the threshold is read as p ≤ 0.0625.
- **Phase-shift slope:** fitted with an intercept or through the origin; the summary is the mean or the median; "±" is not defined and is used as the tolerance.
- **Finding waveform peaks and troughs:** spacing-limited local extrema, or zero-crossing based, as in Cole and Voytek.
- **Which pairs or sites:** for the phase-locking and coherence medians, and for the asymmetry comparison (ventral-most channel, or the one nearest 2.8 mm).
- **Coherence window:** 1 s Hann windows, or `cohere`'s defaults.
- **Theta power measure:** relative or raw power, by Welch spectrum or Hilbert amplitude.
- **Figure 3 correlation:** Pearson or Spearman. Displacements come from the probe geometry at 57°.
- **Multi-unit claims:** which epochs; converting ms to degrees at 8 Hz or at each rat's own frequency. The printed test (statistic 21 of 21, p = 0.03, n = 3) cannot occur with three rats, so it is read as all three slopes positive, or as a test on pooled lags.
- **Turning Delay_Asym into ms/mm:** a regression per cycle, or a regression per channel.
- **The total delay of 12.98 ms/mm:** it does not match the 12.00 ms/mm peak delay. Three readings are named.
- **Theta period:** the interval to the next peak or to the previous one. The ms/Hz slope may be per mm or per array span.
- **Correlation strength:** |r| or r², since the absolute delay's rho is printed positive while its slope is negative.
- **Typos in the paper:** some confidence-interval signs are garbled and were read so that the median lies inside. The coherence slope is printed positive though the text says coherence decreased; it is read as a decrease of 0.067/mm.

**Missing from the paper.**
- **Figure 3B:** the site exclusions and reconstruction of the laminar-array rat cannot be read without the figure.
- **Analysis code:** none was deposited.
- **Multi-unit data:** the dataset descriptor says the files are at 500 Hz. That is too low for the 600–3000 Hz multi-unit band, so the two Figure 4 claims need recordings the descriptor does not list; whether the dataset holds them is for the author to check.
- **Fig. 7D:** the paper prints no test for "significantly reduced". The criterion adds a paired test.
