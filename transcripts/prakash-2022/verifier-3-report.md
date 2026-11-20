# Round 3 verification report: prakash-2022-01

The attempt record has one outcome with a `proposed` change (attempt record, line 240). No other outcome carries one.

| Claim id | Proposed outcome | Agree | My outcome | Reason |
|---|---|---|---|---|
| fig7d-contacts-exceeding-baseline | blocked (methods_underspecified) | No | not_reproduced | See below. |

## fig7d-contacts-exceeding-baseline

**Do the numbers come from the data?** Yes. Cell 30 reads the "Fig. 7d L" and "Fig. 7d R" sheets of Supplementary Data 7. The sheet notes, printed in the output, say these are the group means over Opsin (+) and Opsin (−) animals, 30 to 100 Hz. The cell takes the 180 baseline steps (t < 0) and the mean over 0 to 1200 s, then applies the same bootstrap as cell 29 (10,000 resamples). It reports:

| Panel | Two-sided | One-sided | 10 s blocks |
|---|---|---|---|
| Opsin (+) | 25 of 25 | 25 of 25 | 25 of 25 |
| Opsin (−) | 20 of 25 | 20 of 25 | 19 of 25 |

The printed per-contact rises support this: up to 0.34 dB in Opsin (−), falling to about 0 on the last five contacts. Cell 31 and the record's notes quote these numbers correctly. Cell 29 is unchanged from round 2: 0 of 16 readings hold, and 0 of 8 with the block bootstrap.

**Was the choice made to reach the result?** No. The new cell applies the criterion's own rule, unchanged, to the paper's series. Cell 20 adds independent support that the data are the paper's. Two mice match the paper on mean gamma power:
- interlum_8 at 0.349 dB against exp 2 at 0.351;
- interlum_ctrl_4 at −0.234 dB against cntrl 2 at −0.230.

So the gap to 2.7 contacts per mouse more likely lies in the counting rule than in the recordings.

**Is the criterion applied as written?** The proposal does not apply it. The claims file says the outcome "is the one all readings give; when they differ the claim is blocked as methods_underspecified". Here every reading agrees: 0 of 16 hold (cell 29). As written, the criterion therefore gives not_reproduced. Blocking needs readings that disagree, and none do.

**The evidence is weaker than the proposal's reason says.** The reason says the rule "cannot give the paper's numbers on the paper's data", but cell 30 does not show that:
- The sheets are means over three mice. Averaging narrows the baseline bootstrap interval, so a group-mean series counts more contacts than single mice would.
- The paper's own Opsin (+) panel shows this. The group mean gives 25 of 25 (cell 30), against the paper's 15.7 ± 10.1 per mouse.
- Opsin (−) shows the same kind of inflation, from 2.7 to 20. That is large but not impossible.

So the evidence makes 2.7 per mouse hard to reconcile with the described rule, as cell 31 itself says, but does not rule it out.

**A point in the claims file, reported and not corrected.** The Methods say only "above the bootstrapped 95th confidence interval of the mean of the baseline period". They do not say which baseline values are resampled. The claims file fixes this as "the 1 s spectrogram steps of the 180 s before onset … as a standard choice" and does not list it among the open readings. Cell 30 and cell 20 together suggest that this fixed choice is what drives the result. If the claims file listed the resampled unit as an open reading, blocked as methods_underspecified would be the right outcome. Under the claims file as written, it is not_reproduced.

The record's methods_unavailable finding, "Which baseline values does the test … bootstrap?", is the right place for this evidence. I recommend keeping it, together with the cell 30 numbers in the notes.
