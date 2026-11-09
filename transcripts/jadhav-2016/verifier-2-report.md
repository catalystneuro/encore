**Round 2 verification: Jadhav et al. 2016 (doi:10.1016/j.neuron.2016.02.010) on CRCNS hc-28**

The claims file has 39 claims and the attempt record has 39 outcomes: 9 reproduced, 7 partially reproduced, 21 not reproduced and 2 blocked. I found no misreading of the paper in the claims file. I checked the fig6e-theta-trained-glm criterion, which tests through the model type × group interaction, against the paper's text and it matches.

**1. Outcomes**

I agree with all 39 stated outcomes. Four of them differ from round 1:

- **fig4a-preferred-phases (not_reproduced):** I now agree. With 15° peaks (cell 42), no reading puts the PFC modal 45° bin at 180°, so the PFC part fails. In round 1 I left it undecided.
- **fig4-theta-locked-fraction (reproduced):** 0.545 against a lower bound of 0.54 (cell 39). It passes the tolerance rule, but by 2 cells, and those 2 moved only because of the interpolation fix.
- **figs5-matched-selectivity (reproduced):** This meets the criterion (cell 103), but the excited relation is p = 0.047 and the IQR comes from 7 cells. The record calls it fragile.
- **figs6-replay-content (not_reproduced):** The analysis now runs (cell 132). Modulated cells do not exceed unmodulated (p = 0.45), with only 8 modulated cells.

Three earlier outcomes still rest on a single reading, and their notes say so:
- theta-lag-past: reading (b) gives −15 ms; reading (a) gives 0 ms on a flat curve.
- fig6e-glm-swr-prediction: equal-width groups only; the group means are not monotonic and the result fails under the mean envelope.
- fig8a: the n is smaller than the paper's.

Assumptions: every tested outcome carries `assumed: true` with its deviations listed. They are stated and reasonable:
- SWR reading (a) is the main reading, and the mean-envelope variant is shown beside it.
- Spike width is divided by 30, as checked in cell 4.
- Positions are taken as cm, as checked in cell 4.
- wtr2 is included, and a variant without it is shown.
- Replay is decoded on wtr1 only.
- GLMs that do not converge are dropped.

The record justifies keeping reading (a) because it alone matches the count per day. That is thin, since the duration, rate and CA1 gain favour the mean envelope. It matters little, because the classification fails under both.

**2. Sentences the printed numbers do not support**

- **Cell 130, Summary (cell 134) and README:** "No downstream claim that fails under reading (a) meets its criterion under either variant." Also the README's "the notebook repeats the downstream tests under both."
  - The cell 129 battery does not run fig3-transient-responses, the inhibited-stronger shuffle test of fig7c (the part that fails), figs6, fig6e-theta-trained-glm, figs4c or fig8d.
  - Cell 127 names only some of these omissions.
  - So the sentence holds only for the claims and parts the battery actually tests.
- **Attempt record, fig3de notes:** "Mean envelope: CA1 46 against excited 100 ms." Cell 129 prints CA1 48.
- **Cell 43 and the fig4a record notes:** "45 deg peaks: modal bin 45-90." Cell 42 shows 45–90 and 90–135 tied at 14. The circular-mean reading also ties 90–135 with 225–270 at 14. No tied bin contains 180°, so the conclusion stands.
- **Cell 66 and the fig5c notes:** "Without the speed filter the order is the same." In cell 65, without the filter, excited (0.258) is above unmodulated (0.231), and CA1 < excited becomes p = 0.0072. The failing comparison, excited not above inhibited, is unchanged.
- **fig8a notes:** "Pre-rest epochs hold 411 to 631 SWRs per day." Cell 117 prints only days 1, 4 and 8, which is 9 of the 24 animal-days.
- **Run time:** the README says about 26 minutes and cell 0 says about 30. The outputs cannot check either. Cell 23 also has a typo (",,").

Every other number in the Result conclusions, the Summary, the README and the record notes matches the printed outputs.

Round-1 reasons: the record gives my round-1 reasons faithfully, with each problem attached to the claims it bears on. Two things are missing:
- Problem 5 (position units, which bears on wtrack-learning, figs2 and the speed thresholds) appears in no `reason`, only in the responses.
- Problem 2's mention of fig8bc is not in fig8bc's reason.

**3. Round-1 points**

Resolved:
- 1: the binning is now 15°.
- 2: rate maps give each environment its own bins (`hc28.rate_maps`).
- 5: positions are cm (cell 4).
- 7: phases are interpolated (`_phase_at`).
- 8: replay now runs.
- 9: the null rate is 0.066.
- 12: group sizes are printed.
- 10 and 11 needed no action.
- From my "could not check" list: the CA1 gain per reading and the events per tetrode, the per-animal Table S2 counts beside cell 22, the wtr2-excluded and mean-envelope classifications, and the raw 45° peaks are all now printed.

Partly resolved:
- 3 and 4: the variant section exists, but it leaves out the claims listed in section 2.
- 6: this is acknowledged in the deviations and the Summary, but it cannot be fixed without the authors' detection details.

What remains that bears on a conclusion:
- The variant gaps above. fig7c is the one most likely to change: without wtr2, r is 0.21 against 0.41, and the difference test was not run. The text claiming no variant rescues a failing claim needs either the missing runs or a narrower wording.
- The PFC classification still rests on 12 excited and 7 inhibited cells, so about 20 comparison failures follow from it and are not independent evidence.
- Four reproduced outcomes sit at the edge of their rules: fig4-theta-locked-fraction, figs5, theta-lag-past and fig6e. figs5 is also untested under the variants.
- New point: fig6e and fig8d rest on 16 modulated cells after 62 of 167 GLMs were dropped for non-convergence (cell 106). The record states this, but it adds to how fragile fig6e is.
