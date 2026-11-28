I re-ran the entry once with `python tools/entry.py all entries/alonso-2020`, and all three notebooks passed: main 31 min, ramps 58 min, voltage 24 min. The checks pass with 0 errors. I wrote the conclusions after the run and copied the same markdown into the executed copies, so the entry's files are newer than the run stamp and the next run will execute fresh.

**Outcome changes**
- **fig2-lp-spike-amplitude-threshold:** now reproduced, marked assumed (was partially reproduced). Threshold reading (b) is now computed, as the upper edge of the densely occupied part of the voltage distribution below -20 mV. At the main setting (5%) it rises from -36.1 to -26.5 mV with Spearman 0.997, and the 2% and 10% settings agree. Amplitude still falls (Spearman -1.0). How to locate that point is my assumption, so I added it to the questions for the paper's authors.
- **fig8-up-down-ramps:** still blocked (too_large). I recorded the verifier's disagreement (it would give not_reproduced). The criterion passes if either ramp reading is within tolerance; the first gives 22 of 38, and the second is untested. The notebook now times the second reading on a subset at 113 min, while that notebook already takes 58 of its 60 min.
- All other outcomes are unchanged.

**Added or corrected, by verifier point**
1. **fig10a/fig10b:** both removal protocols now run. The main one, marked assumed, runs 20 s with every conductance intact first, as the Results do for Fig. 9 and as the deposit's removal script does; removal from t = 0 is the variant.
   - fig10a: 4 of 5 checks hold with the control period first, 3 of 5 from t = 0. Both are partial; measured changed from 3 to 4.
   - fig10b: the H part still fails under every reading and protocol (30 or 31 models, 33 needed).
2. **fig8 second reading:** not run; timed in the notebook (see above).
3. **fig2 threshold reading (b):** computed (see above).
4. **fig4:** added burst bounds at the -50 mV slow-wave crossings. The leak's inward share is still 0: V stays above -50 mV between those crossings, so no such bound can test it. No part of the criterion holds under any of the four readings.
5. **Java check:** the Java now matches the port at 25 °C (0.06 mV over 3 s). For G7P2WE at 35 °C and J9U8SQ at 34 °C it gives NaN at exactly the same step as the port, so the divergence is in the deposited code. Finding 5 now says so.
6. **Parameters:** a new cell compares the deposited values with the Methods' search space. gNa, gA, gKd, the synaptic conductances, and tau_Ca as the Java uses it fall outside it. Recorded as new finding 7 (minor, about the data), added at the end so the other findings keep their numbers.
7. **0 mV spike threshold:** now computed. It changes the cell classes in 22 of 76 runs, and only 17 of 38 models stay triphasic at both 10 and 25 °C. Some cells' spikes peak below 0 mV, which supports keeping -20 mV.
8. **Ramp update:** the notebook text now matches the helper (every 20 steps).
9. **figs3:** the notes now say the test detects small differences and shows little more than that the distributions differ.
10. **fig6/fig6s1:** the dominant currents now come from the same 40 s runs that are classified. fig6s1 still has 5 distinct patterns; the model sharing H and Syn with B7SD0L and J9U8SQ is now SJR46Y.

Other outputs the verifier asked for:
- **intermediate-temperature-failures:** the README and the file-name scores are printed. Nothing ties the 38 files to the 40 screened solutions, so the claim stays blocked.
- **fig7:** reading (b) for KMNLBC gives periods of 0.29 to 0.35 s, so no slow time scale appears.

The round is recorded under `verifications` with all 23 claims, and the questions for the paper's authors gained two (the Fig. 10 protocol and the Fig. 2 threshold).

**Not done**
- The second fig8 ramp reading and the per-model ramp for figs3. They would take 113 and 57 minutes and do not fit within the notebook limit.
- No questions were added to `questions/alonso-2020.yaml`: the verifier found no place where the claims file misreads the paper.
- No `findings` entry for round 2: the record has no finding rated critical.
- I left the classification of continuous irregular spiking as "other". It decides no outcome.
- I did not commit or push.
