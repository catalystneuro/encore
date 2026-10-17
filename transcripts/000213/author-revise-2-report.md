No outcome changed. The verifier agreed with all 25 outcomes, accepting the two blocked assembly claims with a reservation, and I did not propose any changes. The final run of `python tools/entry.py all entries/000213-tingley-2018` passed its checks and executed cleanly; apart from the three new variants, every result is the same as before. Nothing is committed.

**Text corrected (all of the verifier's section 2)**
- **fig5-assemblies:** I removed the hard-coded 9.1% (1 in 11) baseline from cell 72, cell 73 and the notes. They now explain why the 35.4% has no such reference: the window is chosen on the real fit and the shuffles run only at that window.
- **fig5 counting:** the deviation that "the paper may count each pair once" is gone. It now cites the Methods, which support counting per condition.
- **fig1g:** the notes now say the 3-bin difference (+0.006, p = 0.16) is not significant. The deviation now gives both causes of the identical smoothings (MATLAB smooth for rate, circ_smoothTS for phase) and adds the 5 and 6 bin pair.
- **First-run figures:** I removed the numbers this notebook does not print, under ls-place-fields-unstable and hpc-place-field-properties. The box-map variant is no longer called "before revision" in the notebook or the record.
- **figs7:** the 25-unit p = 0.0075 is now flagged as treating the ensemble draws within each of the 3 conditions as independent.
- **README:** it now says 62 of the 67 sessions hold LS units and 47 hold hippocampal units, in place of "67 sessions of simultaneous recordings".
- **Timing:** this run measured about 0.6 s per pair (1.2 s last time), so every pair would take about 12 process-hours, not 23. Text updated to match.

**Outputs added, on the points the verifier said still bear on a conclusion**
- **Hippocampal place-field yield:** I added a variant without the code's rule that drops peaks whose SD across trials exceeds their mean. That rule causes most of the shortfall: without it, 46.0% of hippocampal maps have fields (paper 31.7%), but so do 20.0% of LS maps (paper 5.3%). No setting matches both of the paper's fractions.
- **fig1i:** on the 2,320 fields found without that rule, more than the paper's 1,820, the phase and rate distributions differ more clearly (KS p below 0.001). This supports keeping "not reproduced".
- **fig4e:** I kept only the sessions whose theta channel has the rat's most common label, which removes the switches between hpc and ca3 references. There is still no correlation (DT5 r = 0.027, p = 0.96; DT9 r = 0.170, p = 0.37). Which depth in the session name belongs to the LS probe remains an assumption, since no metadata settles it.
- **fig5 covariates:** on the same 670 pairs, adding the LS unit's own rate map as a covariate gives 5.5% assemblies (5.2% before). So the linear coding of position does not explain the low fraction.

Round 2 is recorded under `verifications` with the verifier's reasons and my responses. The code changes are in `lshpc.py`, the notebook, the README and the attempt record.

**Not done**
- **fig5g and fig6e stay blocked.** The verifier's design (sample LS neurons and run all of their pairs) would fit the time limit. But it is a new analysis, and the protocol says a change needing an analysis not yet run waits for a new attempt. The notes now say it would fit.
- **Shuffles at every window for fig5:** not added. Taking each shuffle's best window can only raise the null and lower the fraction further, so it would not affect the "not reproduced" outcome.
- **Paper:** I downloaded no paper text, so nothing was added under `paper/`. I relied on the verifier's Methods quote.
