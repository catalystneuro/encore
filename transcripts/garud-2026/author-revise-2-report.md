No outcome changed. The verifier agreed with all 18 outcomes and with both `critical` ratings, and the re-run gives the same 18. I proposed no changes, so a round 3 isn't needed. `python tools/entry.py all entries/garud-2026` passes; the last real run took 688 s and the final call reused it because nothing had changed.

**Sentences the outputs didn't support, now fixed by printing the number or correcting the text:**
- **Finding 2 (separate clocks):** cell 7 now prints each photometry series' stated start (0 to 8 µs) and the TTL2 description, "raw photometry channel ttl2", in every file. The finding now says the series "state a start of 0".
- **Sampling rate:** cell 8 and the summary now say about 120.4 Hz (120.29 to 120.53).
- **Session blocks:** the summary now gives the block order for each group separately.
- **fig4b:** the session mean ΔF/F is now printed for both corrections.
- **fig4d:** the p-value range is corrected to 0.113 to 0.133.
- **fig2f:** the cell now prints p = 0.0075.
- **fig3:** the A values are corrected to the printed ones. I added a run with the first round's narrower profile bounds; it gives the same counts and winners, which supports the "widening changes nothing" sentence. The notes now explain why fig3 records the approach rows while fig2gh uses all rows off the ports, and describe the fits that sit at a search bound.
- **fig5bc:** the change in SSE between the narrow and wide searches is now printed (0.53 to 20.93), and so is the IM-1322 SSE at both σ bounds (0.17 apart). The text now quotes these numbers.

**Added at the verifier's request:**
- **Pre-cue baseline for fig4b (outside the criterion):** measured against the level 5 to 0 s before the cue, there is no long-ITI dip (difference 0.0003, p = 0.32). This confirms the verifier's point that the long-ITI result rests on the claims file's zero baseline.
- **Short-ITI against the long-ITI late level:** the short-ITI last bin is not higher (−0.0067 against −0.0046, p = 0.078), so that part still fails under this comparison too.
- **New `questions/garud-2026.yaml`:** two questions for a reader on fig4b, one on what "baseline" means and one on the short-ITI comparison. I did not change the claim.
- **Round-1 record:** the missing could-not-check item about a pre-cue baseline is now in the round-1 reason for fig4b.

**Problem found during the re-run:** the fig4d mixed model gave different p-values between runs, because the default optimizer sometimes stopped at a worse fit. It is now fitted with three optimizers and the best fit is kept, which gives stable results. One reading moved from p = 0.014 to 0.00064, so 2 readings, not 1, have p below 0.001. Both have r out of tolerance, so it is still 0 of 16 readings meeting the full criterion and 10 of 16 partial. The notebook now takes about 11 minutes, and `runtime_minutes` and the README say so.

**Recorded:** the round 2 block in the attempt record, with each claim's result, the verifier's reasons in its own words, my responses, and its review of findings 1 and 2. Both severities are unchanged.

**Not done:** the verifier's remaining points do not change any outcome and are recorded as notes only. These are the zero-baseline dependence and the fits at the edge of the search range. One more point: the IM-1292 fit with a minimum of 5 observations is very unstable, and under all rows off the ports its A was −2.4e12 in the verifier's run and −5.2e10 in this one. The notes say so.

Nothing is committed.
