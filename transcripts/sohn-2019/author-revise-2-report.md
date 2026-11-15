No outcome changed. All 23 outcomes are the ones the round-2 verifier agreed with, and nothing is written under `proposed`. The entry was re-run with `python tools/entry.py all entries/sohn-2019`: the notebook passed, the checks gave 0 errors, and the run took 27.5 minutes. The conclusions match the new outputs, and the numbers in the other sections came out the same as before.

**alt-speed-unmodulated** (the main point in the report)
- **New outputs:** I added a cell tagged for this claim. It prints:
  - the measured step and the noise-only step for every bin, with the number of trials in each bin;
  - the check the verifier asked for: the noise estimator run on simulated Poisson counts in the same trials and bins, once with rates constant in time and once with the measured trajectory as the rates;
  - the claim's measure without smoothing, which is how the STAR Methods compute speed.
- **Is the noise estimate inflated late in the support?** No. On the simulated counts it is 0.91 to 1.15 times the actual noise, both early and late. Bin by bin, the measured step comes close to the noise-only step at the end of the support (for example 6.58 and 6.58), so the late steps are mostly noise.
- **Rewritten conclusion and notes:**
  - The data show no rise in speed beyond the rise in noise.
  - With the noise removed, every slope is negative, which would be a falling speed and so also a modulation. In the simulation, though, that corrected slope is off by −3.46 to 3.22 per s with an SD of 2.65 to 6.80 per s. The signed-rank test over 4 datasets cannot confirm the fall (p = 0.125).
  - Without smoothing, the steps are mostly noise; with the noise removed, 5 of 8 slopes are positive.
  - The noise-only slope with fixed trials (2.43 to 7.96 per s) is now stated, so the rise is not put down to attrition alone.
- **Code:** in `rsg.py` I split the noise estimator into a function that works on spike counts, so the simulation can use it. Its results are unchanged.

**Other corrections**
- **README:** the run time now says 27.5 min.
- **Summary, kernel width:** it now says Hand Left needs 3 components under a 40 ms FWHM.
- **speed-vs-projection:** the conclusion and notes now give the within-dataset correlations of the noise-only speed with the projection (−0.77, −0.82 and −0.87) and say the criterion uses the pooled value.
- **Aborted trials:** the data check now prints `tp` for the 134 trials with tp ≤ 0 (−2400 to −0.06 ms), and the finding cites these values.
- **Round-1 reasons in the record:** problems 4, 8 and 9 now carry the verifier's note that they do not affect a conclusion.
- **Round 2 in the record:** recorded under `verifications`, with the verifier's reasons and my responses for all 23 claims.

**Questions for a reader:** I added one to `questions/sohn-2019.yaml`: the alt-speed-unmodulated criterion uses smoothed rates, while the STAR Methods ("Test of alternative mechanisms") compute speed in the full neural space without smoothing.

**Not done, and why**
- I did not edit the claims file. The protocol forbids it. The verifier's points about the supplement wording, the Table S1 reading and the interaction test are already questions in the questions file.
- I made no change for gpfa-variance-inverted-u or initial-speed-biased. The verifier only noted that these results are fragile, and the notes already say so.
- Nothing is committed or pushed.
