I checked the file against the paper and corrected it. It is ready for an attempt.

**Checker result** (after my edits): `claims/001273/10.1016-j.xcrp.2025.102660.yaml: 17 claims, 17 quotes, 9 statistical values, 0 problems`. The original 15 claims also passed with 0 problems.

**Changes, by claim**
- **Header:** it named only nine of the ten dandisets the paper lists. I added DANDI:001031, which no claim uses.
- **fig4-polarized-poles-face-electrodes:** the paper says "In neurons of all shapes", so the majority is now required within each shape group. A majority over all 19 experiments could have been met by the random-shape group alone.
- **fig4-orientation-time-constants:** the criterion required the 2-fold ratio for both charging and discharging time constants. The text names charging first, and its own next finding (discharging is slower except in aligned elongated cells) makes a discharging ratio of 2 unlikely. The subset is now open, with two readings: charging only, and charging plus discharging.
- **fig4-pooled-time-constants:** I removed the "mean over cells" reading. Both the text and the legend give n = 19 experiments.
- **fig1-pure-sine-excites-all:** the statement's 100 to 200 ms onset delay was reported but not judged. It is now an expected value, judged at 90 to 220 ms under the protocol's rule for ranges.
- **fig2d-modulated-thresholds-higher:** the criterion ignored the recorded p < 0.0001 for 20 kHz against 2 kHz. I added it, with two readings: one test per stimulus group, or one pooled test.
- **fig5-sine-asymmetry:** the statement includes the antiphasic oscillations and the whole-cell depolarization. The criterion now judges them too.
- **threshold-depolarization-estimate:** I added the 57.7 ± 3.6 V/cm threshold the estimate rests on as an expected value. The 6.8 mV tolerance is now 1.1 mV, carried from the paper's ± 0.11%, in place of a 10% default.
- **New claims** for two main findings that had none, both on data in other dandisets: `fig2-modulated-locks-to-beats` (Figures 2A and 2B) and `fig2c-pure-more-aps` (Figure 2C).

**What remains open** (recorded in the checks entry)
- Several criteria use measures the paper does not give, labelled as standard choices: the centroid and 45-degree rule for the poles, the 5% depolarization level and time windows, and the readings for detecting action potentials. These could change outcomes, and the paper offers nothing to replace them.
- The 60 to 90 Hz firing-rate ceiling could mean the median neuron or every neuron; the text does not say.
- The paper names no test for "no difference between poles". The criterion uses a paired t test, and the Methods only say "paired or unpaired as appropriate".
- The Figure 5 and 6 claims take their method readings from the DANDI:001274 claims file, which reads the same paper.
- Which figure is in which dandiset is read from dandiset titles only.
- Paragraph numbers in the sources cannot be confirmed, because the text has no paragraph breaks.

**Ready:** yes (`ready: true`). Nothing is committed.
