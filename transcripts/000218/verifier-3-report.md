## Verifier report, round 3: Tingley and Buzsáki 2019 (doi:10.1016/j.neuron.2019.10.012) on DANDI 000218, version 0.250624.0439

**What was reviewed.** The claims file has 31 claims and the attempt record has 31 outcomes: 4 reproduced, 8 partially reproduced, 9 not reproduced and 10 blocked. Only one outcome has a `proposed` change, fig5d-lag (record line 268), so that is the only one reviewed here. I downloaded no paper text this round; the criterion in the claims file was enough for this check.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig5d-lag | not_reproduced | Yes | — | See below. |

**Reason for fig5d-lag**

- **The criterion is not met.** It requires both of two things:
  - the lag within 6.4 ± 4.2 ms (2.2 to 10.6 ms) under reading (a) or reading (b), and
  - a correlogram peak more than 3 SD above its flanks.

  The correlogram part holds: the peak is at 0 ms, 166.3 SD above the flanks (cell 60). The lag part fails under both readings: (a) the median of 70 recording medians is 0.00 ms, and (b) the pooled median over 5,903 pairs is 0.00 ms (cell 60). The criterion defines no partial outcome, so the claim is not reproduced.
- **The re-referenced check gives the same answer.** On the LS channel re-referenced within its shank (cell 68), the lag is 0.00 ms for (a) and 0.80 ms for (b) over 4,509 pairs. Both are outside the tolerance, and LS follows CA1 in only 52% of pairs. The correlogram still peaks at 0 ms (53.4 SD above the flanks), which does not show CA1 leading.
- **The numbers come from the data.** Cell 60 computes each lag as the LS event time minus the nearest CA1 ripple time and keeps pairs within ±50 ms, exactly as the criterion defines it. Both readings are computed and printed. The correlogram flanks are 100 to 200 ms and the peak window is ±25 ms, also as the criterion states.
- **No choice was made to reach the result.** The proposal moves the outcome against the author's earlier stated result. Taking event times at the troughs of the filtered signal is a deviation listed in the record and fits the paper's "peak-to-peak" lag.
- **Measures outside the criterion do not change the outcome:**
  - DT9's median of recording medians is 3.8 ms. That is inside the tolerance, but it is a per-animal value and not one of the criterion's two readings.
  - The pooled median without pairs within 1 ms is 3.2 ms. That variant is not in the criterion either, and by animal it gives LS leading in three of five animals (cell 60).
- **The record's reason matches the notebook.** The proposal's reason and the corrected 3.8 ms sentence in cell 61 match the printed numbers in cells 60 and 68.
