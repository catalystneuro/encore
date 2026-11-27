I wrote `claims/wei-2023.yaml` with 48 claims, and it passes the quote checker. The one item the checker flags is a p-value the supplement prints as "3.34*10-11"; I confirmed it against the Fig. S4 legend by eye. Nothing is committed.

**Text read.** I used the version of record from PubMed Central: main text, figure legends, Methods, Supplementary Figs. S1 to S8 with their legends, and Table S1. I also read the Source Data workbook. I didn't need to open the supplement PDF. I read both linked repositories:
- **`yinawei/Mouse_V1_EAP_Analysis` @1e35126:** waveform feature extraction, K-means clustering, the FS/RS classifiers and the helper functions. It starts from waveform arrays already extracted per session.
- **`yinawei/Mouse-all-active-models-EAP` @f1a4268:** the simulation set-up for one example model.

**Claims.**

| | Count |
|---|---|
| Claims | 48 (1 link claim, 47 findings) |
| With quotes | 47 (all findings; the link claim has none) |
| With `statistics` | 25 |
| With `expected` | 20 |
| With a criterion | 48 |

- **Data needed:** 31 use the dataset alone, 1 the dataset plus the Source Data labels, 4 the dataset plus the code's model features, and 12 data held elsewhere (the models, and the Allen Cell Types in vitro data and morphologies).
- **Main findings covered:** the FS/RS split and the six sub-clusters, firing and visual-response differences, phase-locking (including by depth), the optotagged Pvalb against Sst units, the classifiers, and the model and in vitro comparisons.
- **Code settings followed where the Methods are silent:** the 25 session IDs, waveform channels and filtering, feature definitions, unit exclusions, the clustering and K selection, the classifier set-up, and the test-choice rules.

**Details left open, and the readings named:**
- **Unit isolation:** the text says "see Methods", but the Methods give no criteria. Readings: (a) the AllenSDK default quality filter, (b) every V1 unit in the NWB units table.
- **FS/RS firing rate period** (the code's `fr_5min` column): (a) the spontaneous block, (b) the first 5 minutes, (c) the whole session.
- **ISI pooling:** (a) within each drifting-grating presentation, (b) across the whole grating blocks. The confidence-interval method isn't stated, so a bootstrap is used.
- **Phase-locking:**
  - LFP channel: the nearest other channel, or an average of neighbouring channels.
  - 10,000-spike cap: the first or a random 10,000.
  - Band edges: the Results (8–12.5 and 12.5–30 Hz) against the Methods (8–12 and 12–30 Hz).
  - "Kappa": the von Mises concentration, or the mean resultant length (the text says kappa ranges from 0 to 1, which only the second does).
- **Supragranular, granular and infragranular boundaries:** (a) the atlas layer of each unit's channel, (b) within 100 µm of the layer 4 centre found from the current source density.
- **Layer 4 centre from the current source density:** standard computation, or the atlas layer 4 midpoint.
- **Opto-tagging baseline window:** (a) the 6 ms before onset, (b) the 10 ms before onset.
- **Inconsistencies in the paper:**
  - Mice: the Fig. 1d legend says 24 wild-type mice; the text and Source Data say 25.
  - Pvalb units: the text says 25; the Fig. 7 legends and Source Data say 24. Both are accepted as readings.
  - The text cites "Fig. 2f, g" where it means Fig. 3c.
- The sign convention for 1/V below is unclear, so the claim that RS3 propagates faster below the soma is reported but not judged.

**Missing from the paper:**
- The main-figure PDF isn't supplied, so the significance stars of the main figures couldn't be read; those p-values are recorded as bounds.
- Figs. 3d, 3e and S6 and the optotagging kappa and phase exist only as pickle files that aren't supplied.
- Table S2 isn't in the supplement text; Methods Table 2 names the same three metrics.
- The code has no notebooks for Fig. 3 or Figs. 5 to 7, phase-locking or optotagging, and doesn't show how waveforms, the unit quality flag or depth were taken from the NWB files.

**For the author:** the dandiset's title names only the Brain Observatory 1.1 stimulus set, and the paper doesn't say which set its 25 wild-type sessions or its optotagging mice come from. So the author has to check how many are in DANDI:000021. The link claim makes that the first check, and any claim tested on a subset of sessions counts as a deviation.
