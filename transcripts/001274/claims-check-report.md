I checked the claims file for DANDI:001274 against the full text and the supplement, made 14 corrections, and the file is ready for an attempt.

**Checker result** (the same before and after my edits): `26 claims, 26 quotes, 8 statistical values, 0 problems`

**Changes, by claim:**
- **Header:**
  - The paper's Figure 4 n = 19 counts experiments, not neurons, so "19 neurons" is now "19 experiments". The groups (3 parallel, 6 perpendicular) cannot be the same cells.
  - The header compared magnitudes because "the figures plot bars of one sign", but it also says the figures could not be seen. I replaced that reason with the text's: both ROIs' sensitivities are reported as positive numbers.
- **fig1-pure-sine-excites-all:** the statement said every neuron fired in a sustained way. The paper says that only for stronger fields, so I removed it. The criterion now applies the protocol's rule when the AP detection readings disagree.
- **fig1-onset-delay, fig5-carrier-antiphasic:** the tests in these criteria were invented without saying so. They are now labelled as standard choices, since the paper gives no test.
- **fig2d-20khz-twofold-threshold:**
  - The paper gives a single p for "all thresholds". The criterion now names two readings: one test per group, or one pooled test.
  - I removed a 1 V = 36 V/cm conversion taken from the DANDI:001030 description, which is not from the paper. The conversion is now marked as open.
- **threshold-2khz-unmodulated:** the source is now paragraph 6 (it said paragraph 4). Both AP detection readings must now agree (it accepted either one).
- **figs1-di8-anepps-control, fig6b-pulse-sensitivity:** these accepted "one reading" or "one of the two scalings". Both are method details, so all readings must now agree. That also matches the header's own rule on scaling.
- **fig4-orientation-time-constants:**
  - The text names a paired t test (p < 0.001), while the Figure 4 legend marks an unpaired test (p < 0.01). The criterion now names both readings.
  - I added the parallel-to-random ratio as an expected value, since the statement claims doubling against random cells too.
- **fig4-no-pole-difference, fig4-discharging-slower, fig4-pooled-time-constants:** "19 cells" is now "19 experiments". In fig4-pooled, "charge fully" is now the paper's wording, "exceed 95% of full charge" within 3 µs.
- **fig5-whole-cell-depolarization:** the source is now the Figure 5C and 5D legend, where the quote actually is.
- **fig5fg-no-migration:** which of the 16 ROIs belong to Figure 5F and which to 5G is shown only in the figure. Without that split from the dataset, the claim is now blocked as `metadata_insufficient`.

**Still open** (recorded in the checks entry):
- These details are not in the paper and stay open as the header names them:
  - the ROIs (O1)
  - the LOESS span and degree (O2)
  - how the field enters the sine-wave regression (O3)
  - which recordings are cells C7 and C8 (O4)
- Which figure is in which dandiset is read only from the dandisets' titles; the paper gives no mapping. It is unknown whether the 2-µs pulse recordings of the Figure 5 and 6 cells are in 001274 or 001273.
- I could not confirm the paragraph numbers in the Kinetics section: the text has no paragraph breaks and there is no main-text PDF.

**Ready:** yes. The checks entry is appended with `ready: true`. Nothing is committed.
