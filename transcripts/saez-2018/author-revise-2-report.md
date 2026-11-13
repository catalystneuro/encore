I've revised the attempt for round 2. No outcome changed, and I proposed one change for round 3. The entry re-ran cleanly with `python tools/entry.py all entries/saez-2018` (594 s, 0 errors), the record matches the attempt schema, and nothing is committed.

**Outcomes**
- **mixed-effects-robust:** The verifier disagreed and would give reproduced. It stays not_reproduced, as verified, and I added a `proposed` change to reproduced (assumed). The proposal rests on two of the claims file's readings: baseline (a) and one model per window.
  - Under that reading, one regressor with all electrodes makes all 16 regressors significant at corrected p < 10^-4.
  - The notebook now prints the largest corrected p of the 16 under each baseline: 3.0e-03 with the deposited HFA, 3.3e-05 under (a) and 2.9e-02 under (b). The 3.3e-05 is close to the threshold, which round 3 may want to weigh.
  - Round 3 will review this proposal.
- **fig7f-multiplexing and figs7-present-past-overlap:** I removed the `assumed` flag. As the verifier noted, the 5-window selection fails as well, so neither outcome depends on the stepwise assumptions.

**Corrected**
- **Baseline reading (b):** It was not applied cleanly to the buttonpress epoch. The helper now measures that epoch's offset for each trial and electrode wherever the two epochs overlap (1,572 of 1,753 trials). Where they don't overlap, mostly s10 with its long reaction times, it uses the electrode's median offset. Re-running (b) this way changed several numbers but no outcome, and the notebook, record and README now carry the new numbers.
- **`reveal.time` finding:** This was wrong, not just unshown. Only 31% of rounds fall in 31 to 47 ms. The real pattern splits by subject:
  - s01 to s05: 0.53 to 0.59 s after the button press, close to the 550 ms the paper gives.
  - s06 to s10: 0.03 to 0.05 s, up to 0.24 s in s10.

  The notebook now prints this per subject, and the finding and summary say it.
- **Wording the report quoted:**
  - Stepwise zeros are 9 of 16, not 10.
  - The own-null counts are all below Table S2, not "mostly".
  - The statsmodels comparison is now described as close agreement, not identical to the printed digits.
  - The fig5 gap is 368 to 720 ms depending on the reading, not "about 500 ms".
  - The fig3-latency note now gives reading (b) of the delays under both baselines (p = 0.034 and 0.052).
  - The README's baseline sentence now names the four claims that change.
- **Added output:** the cell for figs6a now prints the pair behind the averaged maximum R2. It is loss index with RPE (0.57), as stated.
- **Question for a reader:** I added the verifier's round-1 point 3 to `questions/saez-2018.yaml`. The claims file places the reveal 550 ms after the button press, while the Figure 3 and 4 legends put t = 0 at the gamble outcome. The claim itself is unchanged.
- **Record:** round 2 is under `verifications`, with the verifier's reasons in its words and my responses.

**Not done**
- I left the round-1 responses in the record as they were, so they still show the old baseline (b) numbers. The round-2 entry says those numbers changed.
- `runtime_minutes` in `entry.yaml` still says 11, though the run took about 10. I left it so the entry would not need a third run.
