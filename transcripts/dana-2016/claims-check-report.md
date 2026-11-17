The file is ready for an attempt, and I've marked it `ready: true`. Only `claims/dana-2016.yaml` is changed; nothing is committed.

**Checker result**, run again after my edits: `claims/dana-2016.yaml: 35 claims, 35 quotes, 15 statistical values, 0 problems`

**Changes, by claim**
- **culture-jrgeco1a-sensitivity**: the 0.8 to 1.25 bound for "similar" is now labelled a choice made here.
- **culture-jrcamp1-dynamic-range**: the criterion compared 160 APs with 80 APs, but the text never says which AP numbers Figure 2c uses. It is now judged as dF/F0 rising at each tested AP number up to 160, labelled a choice. I also noted that "dynamic range" is defined only in a source-data table that is not in the text.
- **v1-half-decay**: the criterion now also tests that each mApple-based value is shorter than each mRuby-based value, which the statement claims.
- **v1-response-amplitude**: the Results compare means and the legend gives 75th percentiles, so the jRGECO1a comparison now accepts either reading.
- **v1-orientation-tuning-similar**: the one-s.d. bound is now labelled a choice made here.
- **v1-long-term-stable, l6-imaging**: the paper never defines an "orientation-tuned" cell. Both claims now say the OSI threshold is open and must be stated as an assumption.
- **depth-decay**: added the paper's Wilcoxon rank sum test. The Results and the Figure 5b legend name different red indicators; this is noted.
- **fig4d-event-counts**: the 15-of-18 pass threshold is now labelled a choice made here.
- **fig4df-jrgeco1a-better-than-jrcamp1a**: the d-prime formula had been taken from Chen et al. 2013b, a different paper. It is now open, with two readings.
- **fig4g-jrgeco1a-faster**: fitting the exponential "from the peak" is not in the Methods; it is now labelled as the reading used.
- **fly-improved-over-parents**: had no criterion. I added one from Figure 7c and its legend (per-FOV 1 Hz peak, Wilcoxon rank sum, p < 0.008), with how to take the single-AP amplitude left open.
- **fly-single-ap-amplitude**: the "outperform at 1 to 5 Hz" part is now tested. Notes added: the Results list GCaMP6f where GCaMP6s is meant, and the Figure 7b legend calls jRCaMP1a "similar" to GCaMP6s at 5 Hz.
- **fig7c-frequency-tuning**: the expected value 2.5 ± 0.7 gave 1.8 to 3.2, but the criterion states 1.8 to 3.3. Changed to 2.55 ± 0.75.
- **fig8b-zebrafish-improvement**: the kinetics part had no quote, so I added the Results sentence. That sentence also says jRCaMP1a and jRCaMP1b are more sensitive than R-CaMP2, so I added that finding and the legend's p < 0.01 test.
- **worm-ash**: named the reading used for the undefined "initial amplitude". The criterion now also requires the three named indicators to be the three largest, since the paper says "strongest".

**Still open**
- **screen-single-mutations-improved**: I read the full supplementary xlsx files to check the column names. The paper's own rule (1 AP ratio above 1 and p < 0.01) gives 230 of 934 RCaMP1h variants and 58 of 692 R-GECO1 variants, not the paper's 353 and 187. None of the other rules I tried gives those counts either. I left the claim as the paper states it and recorded the mismatch, so this claim will most likely fail on the paper's own tables.
- **worm-awc**: "near baseline" in epoch 3 has no threshold in the paper; the author must state one as an assumption.

Every main finding has a claim, and none comes from anything but this paper. GCaMP6 reference values from Chen et al. 2013b are used only for comparison, as the paper itself does.
