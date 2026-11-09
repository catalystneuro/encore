No outcomes changed. The verifier agreed with all 20, and nothing is under `proposed`. I re-ran `python tools/entry.py all entries/000044-grosmark-2016`: the check passed with 0 errors and the notebook ran in 935 s. Nothing is committed.

**The "stale" numbers:** the verifier said the best-template numbers in cells 29, 32, 44, 50, 53, 56 and 59 were left over from an earlier run. My re-run prints exactly the values in the text and the record: 188 cells, 0.132 in PRE, 72 of 102, p = 0.0035, 0.020, 0.74, and 0.15, 0.11 and 0.41. The verifier's own executed copy printed slightly different values (190 cells, 0.129, 71 of 104, ...) from the same code and seeds. So this variant does not give identical numbers on every machine, and I did not find the cause. All affected claims are blocked and no threshold is crossed, so no conclusion depends on it. Cell 29 and the fig2b notes now say this and give both sets of values. I left the numbers as they are because they match the current outputs.

**Text fixes:**
- Cell 0 no longer calls the variant "better calibrated"; it says its 21% false-positive rate is also far above 5%.
- Cell 29 and the fig2b notes now say the false-positive rates are measured on every fourth event, so on all events they would likely be higher.
- Cell 47 now says only the first two KS p-values (0.072 and 0.079) are close to the threshold.
- The summary's sentence on the out-of-sample fig2d control is now limited to the linear tracks.
- The fig4d notes now say "p of at most 0.0001 for each".
- The README run time is now about sixteen minutes, from this run's 935 s.

**Added:** the verifier's problem 8 is now recorded as a deviation under fig1c-post-gt-pre and in the summary. MAZE immobility is taken from 2D head speed, while running for the rate maps uses linearized speed.

**Recorded:** round 2 is under `verifications` in the attempt record, with all 20 claims marked as agreed, the verifier's reasons in its own words, and a response for each. The README fix is noted in the response under fig4e, since that point was not tied to one claim. I also copied the four edited markdown cells into the ignored `executed/` copy so it matches the source notebook. The outputs were not touched.

**Not done:**
- The cause of the machine-to-machine difference is not found.
- The pooled-test limitation on fig1c-post-gt-pre, fig2d, fig4d and fig4e is unchanged. The criterion fixes that test, and it is already disclosed.
- Checking against the supplement and figs. S2 to S4 is still impossible, because they could not be retrieved. No paper text was downloaded this round.
