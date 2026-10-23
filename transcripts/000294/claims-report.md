I wrote `claims/000294/10.1162-neco_a_01672.yaml`, and the quote checker passes it with 0 problems. Nothing is committed.

**Text read:** the version of record (Neural Computation 36, 1286–1331, 2024), from the supplied PDF's text. That covers the main text, Methods (section 5), Tables 1–5 and the appendix (Figures 9 and 10). The paper has no separate supplement, and nothing a claim needed was missing.

**Code read:** github.com/alejoe91/multimodalfitting at commit 24e8e61. It holds the package, the optimization script, the figure notebooks (their outputs stripped) and the models in `cell_models/`. It has no optimization results. In the code, cell 1 is `cell1_211006_3148` and cell 2 is `cell1_211011_3436`.

**Claims:**

| | Count |
|---|---|
| Claims | 23 |
| With quotes | 23 |
| With statistics | 1 (three Holm-corrected Mann-Whitney p < 10⁻⁵, Fig 4B right) |
| With criteria | 23 |
| With expected values | 11 |

By data source:
- **Dataset (6):** the two cells and their runs, the eCode protocol structure, the holding potential, extracellular spikes of at least 50 µV, electrode counts and sampling rates, and culture age.
- **Elsewhere (12):** the ground-truth model in the GitHub repo (Figures 3–5, Table 1, its scores), plus the AIS leaving a dendrite, read from the NeuroMorpho/GitHub morphologies.
- **With inputs (5):** the experimental fits in Figures 7, 8 and 10. These combine the dataset's recordings with the repo's morphologies and models.

**Details left open, with the readings named:**
- **IV protocol:** the Methods say 11 steps "from −140 to 20%", which is only 9 steps. Readings: 11 steps from −140 to 60% (as in the code's feature files), or 9 steps.
- **Holding potential:** it is not said whether the stored voltages are corrected for the junction potential. Readings: −70 mV uncorrected, or −84 mV corrected.
- **50 µV spike amplitude:** readings are the negative peak or the peak-to-peak value on the largest channel.
- **Culture age:** the paper says DIV 18–24 in one place and 18–21 in another. Both are named.
- **Fig 4B left (no difference):** no alpha and no set of pairs is stated. Readings: soma against each other strategy, or all 6 pairs, at 0.05.
- **Fig 4D "almost all electrodes":** readings are more than half, or at least 90%, of the 80 channels. For which seed is shown, the legend and the code say best intracellular. The Results text says best extracellular, which I recorded as a variant.
- **Fig 5:** a word is missing ("lower errors than the strategy"). The only reading the next sentence allows is "than the soma strategy".
- **Cell 1's non-converging seed:** readings are the seed whose model fires no spike (which the code drops), or the seed with the highest score.
- **"Main features of the spiking pattern" (Figs 7B, 8B):** readings are the spike count, or the mean frequency, per sweep falling within the range over runs.
- **Cell 2's higher extracellular scores:** readings are the all strategy alone, or both strategies. The text cites "panels B", which hold no box plots; panels A are meant.
- **Comparing seeds:** no test is reported. Medians are compared (the figures are box plots), with means as a variant.
- **"±" spreads:** they are used as tolerances, but the paper does not say whether they are SD or SEM.

**Where the code and the Methods disagree:** in each case the claims follow the Methods, and the code's choice is a named variant.
- The template is the median of the waveforms in the Methods; the code takes their mean.
- The Methods name post hoc Mann-Whitney tests; the code runs Conover tests.
- The experimental figures use the best intracellular seed in the legends; the code plots the best extracellular seed.
- The amplitude tolerance is 10% in the Methods and 30 in the code.
- The Methods count 79 optimization features; Table 1 gives 76.

**Choices of mine (not set by the paper or code):**
- The 50% and 90% thresholds for "almost all electrodes" in Fig 4D.
- The spike-count and mean-frequency measures for the Figs 7B/8B claim.
- The rule for Fig 10, that the recorded peak lies nearer the somatic current peak than the AIS one (my reading of the legend's wording).

I also had to cut three quotes with "..." because they span page breaks in the extracted text.
