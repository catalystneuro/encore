I've answered every point in the round-2 report. No outcome changed, but one change is proposed for round 3: fig4c-active-subsets, from not reproduced to reproduced. The entry re-ran cleanly with `python tools/entry.py all entries/rich-2014` (5.8 min, 0 check errors), every number is the same as before, and nothing is committed.

**Outcomes**
- The counts are unchanged: 18 reproduced, 3 partially reproduced, 5 not reproduced, 1 blocked.
- **fig4c, proposed change.** This round I rendered the supplement figures, which the readers could not view. Fig. S18 plots the environment sizes on linear axes from 0 to 50 m, and a logarithmic axis cannot start at 0. Its narrow high-rate strip also fits linear spacing: 0.100 of the width in the new output against 0.627 under logarithmic spacing. So the paper supports linear spacing (G-b), and under it the claim is reproduced. The verified "not reproduced" stays, with the change written under `proposed` and the analysis in the notebook. The two reasons the verifier called inapt (the "orders of magnitude" quote and "small environments") are withdrawn.

**Added or corrected, by the report's points**
- **a. End allowance (`EDGE_CM`).** A new section reruns the affected tests with no allowance and with 0, 10, 15, 20 and 30 cm:
  - figs7a holds at every allowance from 0 cm up.
  - fig3d is within tolerance from 10 cm up but not at 0 cm.
  - fig3c-lomax is within tolerance only at 10 cm, so its partial outcome rests on the allowance as well as on P-a.
  - figs6 and figs11-no-boundary-remapping do not depend on it.
  - I kept 20 cm because no field changes beyond it.
- **b. figs10 panel A.** I tried 12 bin widths and offsets. Panel A passes under 8 of them for P-a and 5 for P-b, so the failure is fragile. It does hold for the paper's own bins: Fig. S10 uses the same 30° bins starting at −π, and its shuffle pattern matches ours. With the bin widths the figure shows (15 cm and about 12 cm/s), panels B and C pass. The "little power" sentence now applies to Y-a only.
- **c. figs11-no-boundary-remapping.** p stays below 0.05 at the boundary of sections 3 and 4 under every allowance (0.0125 to 0.0328). It still rests on P-a with p near 0.05, and the notes now say so.
- **e. In-field rates.** On the data set's own field extents, the mean of the smoothed map (the claims file's measure) gives 4.94 Hz. Spikes over time in the field give 5.39 Hz, against the data set's 5.45 Hz. So about 0.5 Hz of the gap comes from how the rate is measured. I added a finding that the data set's rate is undocumented. With the spikes-over-time rate, 44.4% (P-a) and 47.3% (P-b) of fields pass the 4.8 Hz threshold in figs15, against 50 ± 5%; this is a variant and decides nothing.
- **Wording.** I fixed the figs12 causation wording (cell 75) and the fig4c quote (cell 96), in the notebook, the record and the README.
- **Questions for a reader** (in `questions/rich-2014.yaml`; the claims file is unchanged):
  - fig4c: the criterion admits it does not test the paper's statement, and Fig. S18 shows the spacing.
  - fig4b: the stale "under a factor of 4" note.
  - figs10: the bin widths the claims file says are not given. Also, read from the figure, the paper's own Fig. S10 has bins outside its 95% intervals in every panel. So the criterion's bin-count test might fail the paper's own data.
- **Round 2 is recorded** under `verifications`, with all 27 claims: the verifier agreed with each, and the record gives its reason and my response.

**Not done**
- Fig. 4 of the main article could not be rendered because the PDF's content stream is corrupted. So Fig. 4C itself could not be checked, only Fig. S18.
- Round-1 point 1 (a reading chosen by the author against the claims file's "all readings" rule) and point 8 (the open-field scale) stay recorded only, as the verifier listed them.
