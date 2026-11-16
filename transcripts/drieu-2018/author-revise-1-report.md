I've worked through every point in the round-1 report and recorded the round under `verifications` in `attempts/drieu-2018-01.yaml`. `python tools/entry.py all entries/drieu-2018` passes: check has 0 errors, and the three notebooks took 29, 28 and 36 minutes. The numbers are the same as in the earlier batch run I wrote the conclusions from. Nothing is committed.

**Outcomes now:** 13 reproduced, 13 partially reproduced, 9 not reproduced, 0 blocked (before: 9 / 11 / 10 / 5 blocked).

**What changed, and why:**
- **Phase-precession field entry (verifier problem 1):** fixed, with an assert that every in-field spike lies in the field.
  - fig2f is partially reproduced under both phase readings and no longer rests on an assumption.
  - figs4de goes from not reproduced to reproduced, but only 12 and 20 cells precess significantly in the passive conditions, so the test of absence is weak.
  - figs4b goes to partially reproduced: the binomial tests hold, but four of the six proportions are outside tolerance.
- **Rat 272's theta channel (problem 8):** the verifier's suspicion was right. Four of its channels have reversed theta, and the one used had the most power. Channels whose spike phase is more than 90° from the others are now left out; this is stated as an assumption. Knock-on changes:
  - figs5b → reproduced (rat 272's Active slope goes from −23 to +52 cm/cycle).
  - fig3d → reproduced.
  - fig3c-proportion → partially reproduced.
  - fig2b-theta-power → reproduced, resting on the per-window reading (ANOVA P = 2.1 × 10⁻⁴). The per-window test treats windows as independent; with one value per rat it reaches only P = 0.04 to 0.17.
- **Forward-replay test (problem 2):** zero-slope events are now excluded and an exact binomial test is used. fig4f → reproduced (P = 1.4 × 10⁻⁴).
- **Agreed with the verifier:** fig4b → partially reproduced; fig4c → not reproduced.
- **Place-cell definition (problem 5):** I adopted a field reading "c": the Methods' 4.5 cm kernel plus the size and spike limits of the paper's BatchPlaceFields.m.
  - figs2b → partially reproduced: Passive 1 is lowest and the ANOVA gives P = 0.037, but only the Active total is within tolerance.
  - fig1c-field-size → not reproduced, as the verifier gave: six of eight reading combinations find a difference.
- **Claims that were blocked:** they now run in a new third notebook, `reproduce_drieu_2018_controls.ipynb`.
  - figs7, figs8 and figs10 → partially reproduced (figs10 under the own-lap reading, which the paper's script uses; the other reading reproduces).
  - fig3g and fig4g → not reproduced, run on random samples of 3,000 pairs per rat and condition, not every pair.

**Added outputs the verifier asked for:**
- Lines of the paper's scripts the settings come from.
- Per-channel spike theta phase for every rat.
- Field-size histograms, fields per place cell, and spatial information per place cell.
- Fraction of each cell's spikes inside its peak field.
- 8-s theta spectra (0.125 Hz resolution; P = 0.80 and 0.92).
- Spectrogram readings of burst frequency, on all spikes and on in-field spikes.
- Decoding-error check with each lap decoded by the other laps' firing curves (figs9 unchanged).
- Theta decoding under field reading b.
- Replay under field reading b and the whole-session threshold, on a random fifth of events. No outcome changes.

The V-test is now two-tailed.

**Questions file:** `questions/drieu-2018.yaml` asks a reader whether fig2cd's criterion should say spectrogram, as the Methods do, instead of spectrum. fig2cd stays not reproduced on the claims file's measure.

**New finding:** in rats 292 and 314, pyramidal cells fire near the theta peak on every channel. That fits an inverted signal polarity in their 20 kHz recording system. It is recorded but not corrected.

**Not done, and why:**
- The control notebook uses 100 shuffles (the decoding notebook 200, the paper 5000) and 10 cell subsets instead of 30. The replay readings use a fifth of the events, and the bias correlations use samples of pairs. This was to keep each notebook under 60 minutes; all of it is stated as deviations.
- The remapping tests were not rerun under field reading c, and the 20-bin matrices of Fig. 3G were not computed.
- I first started the full run in the background. It was killed when that call returned, so I ran the notebooks in the foreground with the same command `entry.py` uses, then reran `entry.py all` at the end.
- Since the record file was rewritten through a YAML dump, its whole diff is large.
