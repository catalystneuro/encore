# Round-3 verifier report: temmar-2025-01 (LINK, DANDI:001201 0.261026.1912)

I agree with the one proposed change: fig2a-irregular-shifts moves from partially_reproduced to reproduced.

The claims file has 24 claims and the attempt record has 24 outcomes. Only one outcome has a `proposed` change, fig2a-irregular-shifts, so it is the only one reviewed here.

| Claim | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig2a-irregular-shifts | reproduced (from partially_reproduced) | Yes | — | Both parts of the criterion now hold. Details below. |

**Why I agree with fig2a-irregular-shifts**

- **The numbers come from the data (window [6], [8]).**
  - The 20 every-16th reference sessions were trained again here with the same settings as `decoding.ipynb` (seed 42, 2000 iterations). Their 10th to 90th percentile range is 0.529 to 0.651, the same range `decoding.ipynb` [27] prints.
  - The LSTM R2 median over the 27 window sessions with an LSTM is 0.641, which is inside that range.
  - The other window figures check against the printed output: 0.639 over the 24 new sessions alone, 0.652 over the 3 earlier ones, 11 sessions above the 90th percentile and 1 below the 10th.
  - The RR part holds in `decoding.ipynb` [27]: the window median is 0.321 over 45 sessions, inside 0.220 to 0.360.
  - The shift part holds there too: 38 of 42 window days have at least five channels shifting.
- **The choices were not made to reach the result (window [0], [1]).**
  - The 24 new window sessions are picked by a fixed rule: evenly spaced in date order (`np.linspace` over the 42 window sessions not already fitted). This is stated as chosen before any result. I cannot confirm the timing, but the rule leaves no room for choice.
  - The reference set is unchanged. It is the same every-16th sample that the verified outcome and my round-2 agreement used. It holds 3 of its 20 sessions (15%) in the window, about the window's share of the whole dataset (45 of 312, 14%), so it is a fair stand-in for "all sessions".
  - Using 24 of the 42 sessions rather than all 42 is disclosed as a deviation, and the time argument is consistent: 44 fits took 35.5 min (window [6]).
  - One minor point, not result-driven: the 20 reference sessions could have been reused from `decoding.ipynb` instead of trained again. That would have left time to fit all 42 window sessions.
- **The criterion is applied as written (window [8]).**
  - The criterion asks whether the window median lies within the 10th to 90th percentile range of "all sessions' values".
  - The every-16th sample is the right reading of that. The failing variant uses only the 17 every-16th sessions outside the window (0.524 to 0.616), which is not "all sessions", so it should not decide the outcome. It is properly disclosed.
  - The other variant, percentiles over all 44 sessions fitted, also passes (0.541 to 0.665).
- **Caveats, which do not change my outcome:**
  - The pass is narrow. The median is 0.010 below a 90th percentile estimated from only 20 sessions, and 18 of the 45 window sessions are still unfitted.
  - Any departure from the range points to better decoding in the window, not worse. The LSTM's margin over RR is unchanged (0.303 in the window against 0.301 over the every-16th sessions).
  - The record says the refit reference sessions give "the same R2" as in `decoding.ipynb`. Only the summary percentiles are printed to show this, not each session's value.
- **Claims-file issue, reported and not corrected (`decoding.ipynb` [27]):** the criterion's shift rule flags at least five channels on 237 of the 243 days outside the window that have a 30-day baseline. So the shift part holds trivially and does not pick out July to November 2022 as the paper describes. This is a weakness of the criterion written from the paper, and is for a reader to judge; it does not change the outcome under the criterion as written.
