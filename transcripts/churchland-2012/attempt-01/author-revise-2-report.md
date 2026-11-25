No outcome changed. The round-2 verifier agreed with all 22, and none needed a `proposed` change. The fixes below are corrections to the text and the record. I re-ran the entry twice with `python tools/entry.py all entries/000070-churchland-2012`; the check showed 0 errors, both runs passed, and the second run printed the same numbers as the first.

**Corrected**
- **fig3-phase-from-prep-state (cell 34 and the record notes):** The verifier saw 0.614, 0.726 and 6 of 10 where the text said 0.615, 0.727 and 8 of 10. The text was not out of date. Both of my re-runs print 0.615 and 0.727, with 8 of 10 shuffle 3 runs reaching the J-array value. The code and seeds are fixed, so the gap with the verifier's copy comes from small numerical differences between runs. The J-array count is sensitive to these because several shuffle 3 runs sit within 0.02 of the data. The text now:
  - gives the shuffle 3 medians (0.628 and 0.649);
  - says the J-array count can move between runs;
  - adds the phase-score counts (9 of 10 in J-array, none in N-array).

  I also took the fixed count out of the round-1 response.
- **rotation-frequency (cell 54):** The word "only" now applies to the variants in cell 52. The text also says the -150 to +50 ms window reaches the range (1.31 Hz).
- **fig6-velocity-model (round-1 response):** It no longer says the angle failure comes from choices made here. It now says the peak depends on the model's open choices, and that no setup that keeps the preparatory tuning peaks within π/4 of zero in both datasets.
- **README:** The run time now reads 10 to 15 minutes. These runs took 9.6 and 9.7 minutes; the verifier's copy printed 14.4.
- **Round-1 reasons in the record:** I added the verifier's remark that shuffle 2 also scores high (fig3-phase-from-prep-state). I attached the point about the missing PC smoothing (B8) to fig3ef-same-direction.

**Added:** The round-2 entry under `verifications` in `attempts/000070-churchland-2012-01.yaml`, covering all 22 claims. Each gives `agrees: true`, the verifier's outcome, its reason paraphrased from the report, and my `response`.

**Not done:**
- I did not pin down the exact source of the run-to-run differences. It does not affect any outcome, and the text now says the count can move.
- Nothing is committed, as instructed.

The working tree also has untracked files I did not create and did not touch, such as `.bashrc`, `.idea` and `scripts`.
