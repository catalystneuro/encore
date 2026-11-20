The verifier agreed with all four proposed changes, so all four outcomes changed and no proposal is left standing.

**Outcomes changed:**
- **ed3c-keypoint-velocity:** reproduced → partially_reproduced. Under the Methods' fit with slope and bias, the 2D velocity correlation (r = −0.170) is within tolerance but the forelimb one (−0.026) is not.
- **fig1f-syllable-vs-movement-onset:** reproduced → partially_reproduced, still marked `assumed: true`. The verifier noted a gap: the criterion has no rule for two readings that are significant in opposite directions, and read literally, reading (b) alone would make it reproduced. Since protocol keeps claim text unchanged, I left the claim alone and added this as a new question in `questions/markowitz-2023.yaml`.
- **ed10d-optoda-vigour:** blocked → not_reproduced (U = 47, P = 0.180). I removed `blocked_by` and, as the verifier asked, set `assumed: true`. The result rests on a clock shift, on directions inferred for 12 of the 17 experiments, and on an assumed baseline for the usage rule. Your instructions said to change nothing else in the outcomes; I treated this flag as part of applying the agreed change, since the verifier made it a condition.
- **ed10i-no-place-preference:** reproduced → not_reproduced. The experiment-wide test gives P = 0.005, with Opto-DA lower than controls.

**Other updates:**
- I removed the `proposed` blocks and rewrote the notes that said "kept as verified" or "proposed".
- I updated the conclusions and summaries in both notebooks, the optoda header table and ed10d section, and the README paragraph that called ed10d blocked.
- I recorded round 3 under `verifications`, with four results giving the verifier's reasons in its own words and my responses.

`python tools/entry.py all entries/markowitz-2023` reported 0 check errors, and both notebooks ran: photometry in 2426 s, optoda in 611 s. The key numbers are the same as before. Nothing is committed.
