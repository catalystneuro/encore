I checked `claims/kim-2020.yaml` against the paper. Only that file is modified, and nothing is committed.

**Checker:** `claims/kim-2020.yaml: 45 claims, 41 quotes, 97 statistical values, 0 problems` (same result before and after my edits).

**Changes, by claim**
- **tab2-nonlinearity-ei:** Table 2 marks 12 comparisons significant, not 11 (all 7 for threshold, 5 for transition). I corrected the count and named the 12. The "partially reproduced" rule was "7 of the other 9", which no longer fits; I made it "8 of the other 10".
- **fig3d-double-peaked-counts:** The paper describes the 20/40 two ways: neurons with a double peak in the spiking or subthreshold STRFs, and neurons with a double-peaked all-event STRF (the Fig. 3e ratios come from all-event STRFs). The criterion now names both readings.
- **fig7d-current-double-peaks:** The Results call 11/31 a share of "current traces". But 31 is the neuron count, and the 39 traces hold 9 + 5 = 14 double-peaked STRFs. The criterion now names two readings: neurons out of 31, or traces out of 39.
- **fig5e-q-strf-higher:** The paper defines Q as best frequency over bandwidth but gives no best frequency for TRFs. Using the characteristic frequency for TRF Q30 is therefore a reading; it is now named, with an alternative.
- **tab1-event-rate-no-difference and tab2-event-rate-excitation-higher:** The paper does not define event rate. "Events over the DMR duration" is now marked as a standard choice.
- **fig4d-bsmf-small-psp-higher:** I added a note that the Discussion (observation 2) says large and small PSPs did not differ in spectral preference. The Results and Table 1 (p = 0.0021) say they did, and the claim follows those.

The other claims match the paper. Statements, sources, p-values and tolerances are the paper's, and none of the recorded statistics is a threshold used to count units. Every main finding has a claim: TRF narrowing, STRFs narrower than TRFs, modulation differences, nonlinearities, and the excitatory/inhibitory synaptic currents (EPSCs and IPSCs). Nothing comes from outside the paper.

**Still open (recorded in `checks`)**
- **Grading bounds the paper doesn't give:** Four claims grade near misses with cut-offs the first agent chose, because the paper uses words, not numbers, there:
  - fig1d: "very few near 1" read as under 10% of neurons above 0.7.
  - fig1e: "partially reproduced" when r is below 0.3.
  - fig7: 90% and 75% of recordings unimodal.
  - fig5c: five of six counts (or three or four for partial).

  These bounds affect only how a near miss is graded, not what is measured.
- **Analysis code not read:** The dataset's Matlab "codes" folder was not read, since it is part of the dataset. It may settle the open details D1 to D17, especially STRF bandwidth (D8), the double-peak rule (D9) and the form of the nonlinearity fit (D12).

**Ready:** yes (`ready: true`).
