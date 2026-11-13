Round 2 is answered. No outcome changed and none is proposed, so a third round is not needed. The verifier agreed with all 44 outcomes (23 reproduced, 3 partially reproduced, 14 not reproduced, 4 blocked because the data are missing). I re-ran the entry with `python tools/entry.py all entries/dijk-2018` after the last notebook edit: it passes (431 s), and `check` reports 0 errors.

**New outputs the verifier asked for**
- **fig6-inset-rate-changes:** the record said reading (a) of the session-pair rule (M11) was shown, but it had not been run. Cell 109 now runs both readings. Under reading (a) the criterion fails with both kinds of minima:
  - raw minima: the effect of manipulation on rate changes before errors is p = 0.12;
  - smoothed minima: the manipulation effect before avoidances is p = 0.072, and the zone effect before errors is p = 0.084.

  The outcome stays reproduced. It was already marked as resting on an assumption; it is now listed with the other outcomes that pass only under reading (b), in the notes, the summary and the M11 finding.
- **fig1-field-number-scaling:** I added Fisher's LSD using the mixed model's pooled error, beside the earlier t tests. On the data set's own smoothed maps it gives the paper's pattern: removed DG is above circular DG (p = 0.0042) and above circular CA (p = 0.036), and the two CA conditions do not differ (p = 0.45). The outcome stays not reproduced, because the removed DG mean (2.09 against 2.70 ± 0.39) is still outside tolerance.
- **negative-pairs-no-change:** cell 86 now tests all six pair-class readings. The two that had not been tested differ across manipulations (p 0.0017 to 0.017), so "only reading (b)(i) gives no difference" is now true of all six.

**Text corrected** (notebook conclusions, record notes, summary and README)
- pc-int-pair-classes: two of the readings give 103 pairs, not 152, and their counts are now given.
- fig6b: the raw and smoothed minima are now described separately.
- fig4d-room-ipos-near-active-zone: the p ranges are given with both the residual df and the paper's df.
- tables2: the unsmoothed room-frame field counts that differ (Kruskal-Wallis p = 0.030) are now mentioned.
- Summary: the shock-off files log 1 to 33 shocks (it said 5 to 33), and the 115 place cell values are the total over the three manipulations, not per manipulation.
- README: two outcome rows and the run time are fixed.

**Questions and record**
- I added a second question for a reader to `questions/dijk-2018.yaml`. The tables' "mean ISI" of about 5 to 6 ms cannot be a mean interspike interval; the files give about 3.9 s. The claim is unchanged. The information-unit question was already there.
- Round 2 is recorded under `verifications`, one entry per claim (44), with the verifier's reasons and my responses.

**Not done**
- The pair-class counts still do not match the paper's (point B8). This bears on no conclusion.
- The approach events from raw-distance minima were left as they are (point B11); both readings are already shown.
- I did not touch `tools/entry.py` and `tools/notify.py`. They were already modified before this run began.

Nothing is committed or pushed.
