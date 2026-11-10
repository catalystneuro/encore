I wrote `claims/park-2019.yaml`. The quote checker passes every quote and reports one problem, which is a garbled glyph, not a wrong value: it can't find p = 1e-9 for `fig1d-preference-change`. Line 143 of the text prints it as "p = 10�9", which is 10⁻⁹. I left the value as it is. Nothing is committed.

**Text read:** the version of record (`paper/10.1016-j.neuron.2018.11.019.txt`), with main text, figure legends, STAR Methods and the full supplement (Figures S1 to S6, Table S1). Video S1 holds no result. There was no PDF tool here (no PyMuPDF, no pdftoppm), so I read every figure from its legend and the Results only. I read the garbled glyphs as: "10�N" = 10⁻ᴺ, "R" = ≥, "%" = ≤, "3 10⁷" = ×10⁷. The spike width prints as "169.79 ± 4.58 ms", which is very likely µs.

**Code read:** FentonLab/PyCode_MEC_HDC-NeuronMS_Park at commit 545a738. It holds the decoder (`HD_Max_likelihood.py`) and the internally referenced tuning (`Spike_triggered_FR_curve.py`). I did not read the pfgp code on Bitbucket (the Gaussian process model behind Figures S5 and S6). No code is given for Idir, the cell-pair correlations, the tuning measures or the JMP statistics.

**Claims:** 22, all with quotes and none inferred. 32 statistical values are recorded, across 17 claims with a `statistics` block. 15 claims have expected values. All 22 have a criterion.

**Details the paper leaves open, and the readings named:**
- **Learning curves (Fig 1A):** the avoidance measure isn't stated. Readings: entrances per trial, or time to first entrance.
- **Speed (Fig 1C):** how speed is computed (displacement per 30 Hz sample, or per 1 s), and the ANOVA's unit (session, or cell). The degrees of freedom imply about 38 units.
- **LFP power (Fig 1C):** the band. Readings: total power, or theta.
- **Change in preferred direction:** the absolute circular difference, a standard choice. For the KLD, the Methods write counts: spike counts or rates per bin.
- **Decoding window:** 660 ms in the Methods (and the code) against 133 ms in the Fig 2 legend. 660 ms is the main reading, 133 ms a variant. The paper gives no summary error measure, so the median absolute error is used.
- **Idir and frame preference:**
  - direction bin (10° or 45°)
  - which trial the probabilities come from (the rotating trial or stable1)
  - which SD the 2 SD rule uses (the ΔIdir series, or stable1)
  - the margin for "no preference"
- **Relative proximity to the shock zones:** not defined. Readings: a normalized difference of the two distances, or the raw difference. The Results give two averages (r = −0.141 ± 0.029 and −0.132 ± 0.024); either may match.
- **Fig S3 Rayleigh test:** its n. Readings: the number of direction bins (consistent with the reported p), or the sum of the weights.
- **Internally referenced tuning (Fig 4):**
  - interval for Fig 4D: 5 s in the Results, 30 s in the code
  - window side: after the reference spike as the Methods read, before it as the code has it
  - normalization: the Methods' sum of time offsets, or the code's occupancy
  - pairs dropped: the degrees of freedom imply about 130 to 137 of the 142 pairs, with no reason given
  - interval count: the Methods list 11 intervals, the legend says 10
  - "strength": read as the Rayleigh vector length
- **Fig 5:** which recordings are pooled (all seven ensembles, the largest ensemble, or each apart). What the error minima are a function of (head direction, or the error itself).
- **Fig S5 "scored high" and Fig S6 "maintained":** no threshold or test is given. Two readings each.
- **No angular-velocity tuning:** the paper shows no data and names no measure or test, so any test of it rests on an assumption.

**Missing from the paper or the dataset description:**
- The room's cue positions appear only in Figure 5, so the link between the 110° and 350° minima and the cues can't be tested.
- The CRCNS description doesn't mention LFP, waveforms or the training sessions behind the learning curves. That affects the LFP, spike-width and learning-curve claims; whether the data are there is for the author to find.
- The stable1 halves are read as its first and second 15 min, from the code's folder names. The paper doesn't state it.
