I've checked the claims file for DANDI:000897 against the paper and corrected it. It is ready for an attempt (`ready: true`); the points that stay open are listed below and in the file.

**Checker:** after my changes it reports `24 claims, 24 quotes, 24 statistical values, 0 problems`. Before them it was 22 claims with 0 problems. I also checked the cited code lines against the paper's repository at the same commit, 4bee109.

**Changes, by claim**
- **fig1bc-produced-matches-actual:** replaced a made-up 0.6 slope bound for a partial result with "holds in one monkey only". Named the code's fit on valid trials only as a variant.
- **fig2-periodic-proportion:** removed a made-up 20% bound for a partial result.
- **ed3-no-eye-hand-periodicity:** the file tested that the PI was "not above chance", but the paper's test is a one-tailed t-test that the PI is *below* chance. The criterion now uses that test at p < 0.0001. Two things are named as open: what "chance" means (the 2 SD threshold or the surrogate mean), and whether the eye and joystick signals are smoothed.
- **ed2b-pi-navigation-above-iti:** the Methods' 4 s ITI threshold is now the main reading; the code's 4.3 s, which the file had followed, is a variant.
- **fig2e-first-peak-near-065:** the Methods' one-second window is now the main reading, with the code's −1 to −0.1 s as a variant. A made-up "most neurons" rule for the KS test is replaced by two readings: a test per neuron, or one pooled test.
- **ed4e-rate-codes-distance-over-slope:** added the window given in the Results (−550 to −250 ms for both rate and slope). Said that the neuron selection is borrowed from code for a different analysis, because the code for this one is not in the repository.
- **fig3e-xcorr-conserved-iti:** reading the code's session list in date order was the earlier agent's own guess, and the outcome depended on it. Both session readings are now listed, and the claim is `methods_underspecified` when they disagree. Noted that 20 neurons give 190 pairs, which fits monkey A's r(188).
- **ed8-fano-periodic-without-rate-periodicity:** the code's binomial test divides by all units, not by non-periodic neurons. The criterion now follows that, and says the paper reports no test.
- **ed10-motor-preparation-signal:** "increase" changed to "response", because the code's test is two-sided (line 4000), so a decrease also counts.
- **fig4g-reset-model-fits-better:** Fig. 4g compares the code's models 10 and 12, not the two model files the file cited, and those two models are not in the repository. The code's test drops the first session, so the degrees of freedom imply 79 and 103 sessions, not 78 and 102.
- **fig4d-model-subscalar-variability:** the Methods' search for the velocity, done separately for each distance, is now the main reading; the script's fixed 0.35 is a variant.
- **Added two claims** for main findings that had none: **ed6d-model-fano-periodic** (the model units' Fano factor is periodic at 0.65 s) and **ed5efg-tighter-phase-clustering** (phase clustering in the data is tighter than the grid-cell model predicts).

**Open**
- **ed5efg:** the paper names no measure of clustering and no test, so the criterion uses standard choices that are not the paper's.
- **ed6d:** the velocities behind Extended Data Fig. 6d are not given, and the code loads its simulations from saved files.
- **fig3e:** the 294 pairs for monkey M match neither 20 nor 25 neurons.
- **fig4g:** what models 10 and 12 compute is unknown, and the fit used behavioural sessions that were never recorded.
- **ed3:** the bootstrap code for Extended Data Fig. 3 is not in the repository.
- **Extended Data Fig. 7** (a reanalysis of another lab's data) has no claim, because the main text does not state it as a finding.

Nothing was committed or pushed.
