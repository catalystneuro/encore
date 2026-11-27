No outcome changed in this revision. The verifier agreed with all 38 outcomes (12 reproduced, 6 partially reproduced, 20 not reproduced), so nothing needed a `proposed` change. I ran the entry twice with `python tools/entry.py all entries/paula-2026`; both runs passed, and the second (43 min) produced the copies that are now in `executed/`. Every unit reading gives the same outcomes as before, and `entry.py check` reports 0 errors.

**Text the verifier found wrong, now fixed (notebook, record, README):**
- **fig4b-thalamus-lgd-lp-modulated:** the p-value is now 4.5e-21 (it said 3.2e-21) in cell 91 and the notes.
- **Cell 17:** removed the contradictory "rests on the unit reading" sentence. The same mistake was in cell 43, fixed too. Cell 100's repeated sentence is merged into one.
- **Cell 60:** "most" now reads "13 to 26 of 30, more than half under 28 of the 32 readings".
- **Summary:** it no longer says there is no response to omitted flashes. It now gives the omitted-flash contrasts (-42 to 93) and says the response to true onsets is larger in 153 of 153 sessions.
- **Findings 4, 5 and 10:** updated to the 'vbn' numbers and the current test readings. The verifier called the last one "11"; it is number 10 in the record, and I noted the mismatch in the round's record.
- **README and cell 2:** the run time is now the measured 34 to 43 minutes, of which reading the spike times takes 33 to 42.
- **fig1e-dg-ca3-anticorrelation-hubs:** the notes now say the value is only 0.004 inside its bound, and that the paper's upper end of -0.002 does not hold here (+0.026). The criterion does not test that part.

**Added:**
- **Per-population tests for fig4b-other-thalamus-not-modulated.** The verifier worried that the modulation came from treating thousands of windows as independent. I repeated the tests on one median per population (Friedman and Wilcoxon, 30 to 79 populations per nucleus). They find the same four nuclei (MGd, MGm, MGv, SGN) at p < 0.001, so the outcome is not an artefact of that.
- **Fig. 3a compared with the PDF.** The claims file says the figure could not be read; I rendered it.
  - At the parameters the figure labels, the synthetic series match 16 of its 18 markers within 0.03, which confirms the generators.
  - The correlated walk and the chaotic maps are now judged at the figure's parameters, with the earlier parameters still shown. At p = 6.33 the Ikeda map now falls inside the range.
  - The correlated walk still misses. So does the figure's own marker (C 0.266, against a bound of 0.27), so the outcome stays partially reproduced under either set of parameters.
  - This is recorded as new finding 11: the paper's figure puts the correlated walk and the sine outside the ranges its text gives. I also added the figure as an input, and a note to the existing sine question in `questions/paula-2026.yaml`.
- **Round 2 under `verifications`:** all 38 claims with `agrees: true`, the verifier's reasons in its words, and my responses. No finding is rated critical and the verifier would rate none critical, so the round has no `findings` list.

**Not done:**
- The paper's 102 sessions still can't be identified from the files, and the blank-series length (286 s against about 240 s) can't be explained from them either. Both stay recorded as findings.
- The 'qc' presence-ratio cutoff (0.9 against 0.95) stays a question for a reader. I did not change the claims file.
- Apart from Fig. 3a, I did not compare the paper's other figures, because the criteria rest on values stated in the text.

Nothing has been committed or pushed.
