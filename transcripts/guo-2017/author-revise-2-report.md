No recorded outcome changed in this round. For nine claims I now propose changing partially reproduced to not reproduced, and a third verification round will review that. I re-ran the entry with `python tools/entry.py all entries/000009-guo-2017` and it passed with the same numbers as before; `check` reports 0 errors.

**Proposed changes (under `proposed` in the attempt record)**
- The nine claims are alm-unit-classes, fig2e-alm-selectivity, thalamus-unit-classes, fig2f-vmval-selectivity, fig3f-thalamus-silenced, wc-thalamus-hyperpolarization, wc-m1-small-effect, fig6d-localized and snr-photoinhibition.
- I agree with the verifier: none of these criteria allows a partial outcome, and no reading meets any of them in full.
- A new notebook section before the Summary counts the readings that meet each whole criterion. It is 0 for every claim (0 of 2, 0 of 32, 0 of 2, 0 of 64, 0 of 8, 0 of 12, 0 of 16, and 0 of 2 for each whole-cell claim).
- For the two whole-cell claims, that section also shows the values under the three onset readings: E (1.3 s after pole onset), M (0.1 s after pole retraction starts) and L (the deposited laser trace). The thalamus Vm change is out of tolerance under all three. The M1 spike-rate change is out under all three.
- The Result cells, the Summary table, the README and the opening cell of the notebook all mention the proposed change.

**Corrections the report asked for**
- **Cell 20:** it now quotes the verifier's round-1 reason correctly: no reading puts all three values within tolerance.
- **README SNr count:** it no longer calls all 181 SNr units putative GABAergic as a fact. It says they apparently are the GABAergic ones, 171 by computed width and 146 by the files' label. The Summary gives the same counts.
- **fig6d group counts:** cell 68 and the record notes now say the counts near the centre are within 250 ± 25 except 286.
- **27 ms changed to 28 ms** in cells 15 and 89 and in the record notes.
- **Onset latency:** cell 92 (now 95), the methods cell before the whole-cell analysis, the header table and a printed label now say the 7.9 ms onset latency cannot be judged under E or M. It is only shown under L, pending question 7.
- **wc-thalamus-hyperpolarization:** I removed 9.05 from its measured values, since the notes say that onset is not judged.
- **Round-1 reasons in the record:** problem 2 (where spike storage ends) is now in the reasons for fig2e-alm-selectivity and fig2f-vmval-selectivity. The vm1-photoinhibition-no-effect reason now includes the verifier's note that, if the (0.5, 0.5) site is vM1, part (b) holds and part (a) holds in some readings.

**Round 2 is recorded under `verifications`** for all 39 claims: 30 agreed and 9 disagreed, each with the verifier's reason and my response.

**Not done**
- I did not change any outcome; the protocol forbids it in round 2.
- I did not touch the claims file or question 7. As the verifier says, the answer to question 7 cannot change any outcome.
