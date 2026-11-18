The file passed the checker at the end and is ready for an attempt (`ready: true`). Nothing was committed.

**Checker:** `claims/tingley-2018.yaml: 32 claims, 32 quotes, 17 statistical values, 0 problems`. It was 31 claims before one was added; that run also showed 0 problems.

**Changes, by claim**
- **ls-lower-peak-info (new):** Results paragraph 4 reports that LS rate maps carry less peak information than hippocampal place-field maps (0.4 against 1.7 bits/cm, p < 1e-100), and no claim covered it. The paper does not say at which smoothing the peak is read or how bits become bits/cm, so the criterion lists those as readings.
- **fig2-ls-phase-beats-rate:** Under one condition reading, the neuron count dropped the two-sample t test at p < 0.01 that the paper attaches to the 786/840 neurons. The neuron level now always uses that test; only the condition-level rule stays open.
- **ls-few-place-fields:** The partial rule used a chi-squared test the paper never reports. It now only asks that the LS fraction be lower.
- **hpc-place-field-properties:** Added the reason for 10% tolerances. The paper's ± values are spreads of the distributions, and 8.5 ± 12 Hz would include zero.
- **fig4d-depth-gradient:** The criterion required two alternative readings to hold at once; the protocol counts a match under any one. Now either reading suffices, and the thresholds not taken from the paper are marked as such.
- **fig4e-onset-mediolateral:** Marked the tests and the 0.8 bound as choices the paper does not make. Figure S1A gives more than one medial-lateral coordinate for some animals, so that is now listed with two readings.
- **figs6-reference-frame:** Marked the "a quarter of neurons" bound for "many" as not from the paper. Both parts stay required, and the reason is now stated.
- **figs1f-trial-counts:** The ballistic-fraction tolerance (0.925 ± 0.0345) did not match the criterion's 0.81 to 1.0 range. It is now 0.115.

**Open**
- Many criteria cite the paper's code: DavidTingley/papers at 9f4cd48 (the makeFig scripts) and buzcode at e615663. Neither repository is in this checkout, so I could not confirm those details. I only checked that they do not contradict the Methods.
- **figs5-assembly-independent-of-locking:** The paper names no test, and two Figure S5 legends call relations "weakly correlated". The Pearson test at p < 0.05 used here could therefore find the effect the Results say is absent.
- Some minor findings have no claim: the retrobead tracing in Figure S3C (data not public), the speed-rate against precession relation in the Discussion, the ~3.2 m phase fields, and the per-bin KS test in Figure 6E.
