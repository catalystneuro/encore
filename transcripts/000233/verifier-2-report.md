**Verifier report, round 2: Tingley et al. 2021 (doi:10.1038/s41586-021-03811-w) on DANDI:000233 v0.250624.0414**

The claims file holds 35 claims, and the attempt record has 35 outcomes: 7 reproduced, 3 partially reproduced, 4 not reproduced and 21 blocked. One outcome is marked `assumed: true` (fig2-ripple-rate-predicts-glucose).

### 1. Outcomes

I agree with all 35 outcomes.

- **fig2-ripple-rate-predicts-glucose (reproduced, assumed).** I agree. The assumption is stated in the deviations and is reasonable: the SPW-R count of a 5-min interval is paired with the glucose change over that same interval. The two alignments one reading either side are shown, and the outcome depends on which is used. The match remains fragile (see 3).
- **edfig1-glucose-circadian-meals (blocked, data_missing).** In round 1 I said not reproduced. I now agree with blocked:
  - both expected values concern meals, which cannot be tested;
  - the criterion's pooled ANOVA fails (cell 41, p = 0.986), but a within-subject version of the same data finds an hour-of-day effect (ANOVA p = 0.024, Friedman p = 5.2e-05).
  - Claims-file note: the pooled test is the reader's own choice ("a choice made here"), not something the paper misread. With subject offsets left in, it can hardly detect a circadian effect.
- **edfig1-glucose-rhythm (not reproduced).** I agree. It is now changed from partially reproduced, and none of the 12 variants (cell 38) meets either condition of the criterion.
- **All other outcomes** match my round-1 outcomes.
- **Assumptions not marked as such:**
  - fig2ef, fig2g, edfig4-ripple-features, edfig4-nrem-wake and edfig4-no-hour-differs all use the same alignment, but none is marked `assumed` and none has an alignment variant (see 3).
  - The supp-ripple-rate outcome depends on keeping only events of at least 5 s.d.:
    - with that threshold: 10.19 per minute, inside the tolerance;
    - with all stored events: 11.07 per minute, outside it.
  - The threshold comes from the Methods and the record states the dependence, but it has the same status as an assumption and could be flagged `assumed: true`.

### 2. Statements the numbers do not support

1. **Cell 69, and the record's notes for edfig6-ripple-rate-best-predictor.**
   - Cell 69 says: "The timing above puts the reading alone at about 6 h of LFP and 2 h of accelerometer one file at a time."
   - The notes say: "5.7 h of LFP and 2.1 h of accelerometer for 1717 h, one file at a time."
   - Cell 68 printed "LFP 77.9 h, accelerometer 23.2 h of reading".
   - The round-1 response, "The markdown now matches the printed timing", is therefore not true of this run.
   - Cell 68 also shows that the single 30-min read took 106 s, while the 8 parallel pieces took 72.5 s in total, about 9 s each. The two timings disagree by about a factor of ten, and this is not discussed.
2. **Cell 39, and the record's notes for edfig1-glucose-rhythm:** "An oscillation of about 50 min is present." The printed numbers do not show one:
   - the residual is positive over a broad hump from 22 to 131 min;
   - the mean autocorrelogram at a 50-min lag is −0.06;
   - its first side peak is at 70 min, with a value of 0.013.
3. **Cell 51, and the record's notes for supp-ripples-stable-across-days:** "With 3 to 5 days a Spearman test rarely reaches p < 0.05." Cell 50 shows the opposite:
   - every perfectly monotone 3- or 4-day series gets p = 0.000: CGM46 and CGM51 for amplitude in µV, and CGM49, CGM51 and CGM52 for rate;
   - this comes from scipy's asymptotic p; with exact p, n = 4 with rho = −1 gives 0.083;
   - so with 3 days, p < 0.05 occurs one time in three by chance.
   - Both rate "failures" are artefacts of this: CGM52 (n = 4, p = 0.000) and CGM2 (n = 5, rho 0.9, p = 0.037, exact p about 0.08).
   - The outcome does not change. My own round-1 point B14 made the same error.
4. **The record's notes for edfig9-dorsal-ventral:** "In CGM37 and CGM48 the glucose readings cover other days than the electrophysiology." Cell 14 gives CGM48 2.2 h with both signals, and CGM48 is one of the 18 rats. The outcome does not change.
5. **README:** "It takes about seven minutes." Cell 70 printed 8.4 min.
6. **Cell 36 (minor wording):** "Above the diagonal" is used for "glucose period longer than SPW-R period". In the printed matrix, with glucose periods in the rows, those cells are below the diagonal.

I checked every other sentence of the Result conclusions, the Summary, the README and the record's notes against cells 2–68, and they match the printed outputs. That includes the counts, ranges, p values, lag ranges, the 13 failing fig2 combinations (15.8–33.1 min), the 7–10 rats peaking at +5 to +15 min, and the 19 other blocked claims.

The record's round-1 reasons restate my report faithfully, merging each B-point into the claim it concerns. Nothing is misattributed.

### 3. Round-1 points

**Resolved**
- **B2:** the reading (a) exclusion of CNO days and stimulation periods is now stated.
- **B4:** 12 fit variants were added.
- **B5:** start-to-start, stop-to-stop and stop-to-next-start intervals were added, and the 20-ms floor of the merging rule is shown.
- **B6:** both signals are now filtered only where both are recorded, with 100 shuffles and the hours per rat printed.
- **B7:** a bootstrap over rats was added.
- **B8:** missing rat-hours are now left out.
- **B9:** the within-subject test was added, and I accept the blocked outcome.
- **B10:** the CGM32 dates are documented.
- **B11:** the high-pass reading is now stated to nearly repeat the raw one.
- **B12:** the mean-over-offsets variant was added.
- **B13:** prominence and rank of the peaks were added.
- **B14:** the dependence on the criterion's "or" is stated, though the reasoning given is wrong (2.3).
- **C, condition groups and detector parameters:** checked and absent.
- **C, clock alignment:** stated as unverifiable (cell 15).

**Remaining, bearing on a conclusion**
1. **fig2 fragility (B1).** It is now reported in full, but the substance stands:
   - the match holds in 3 of 16 combinations, and in 1 of 16 once rats with less than 6 h of both signals are dropped;
   - per-rat lags spread from −100 to +80 min;
   - the outcome flips with the alignment.
   The "reproduced" outcome rests on a minority of readings.
2. **The alignment assumption reaches further than fig2.** fig2ef, fig2g, edfig4-ripple-features, edfig4-nrem-wake and edfig4-no-hour-differs use the same +10-min pairing, with no variant shown and no `assumed` flag. fig2g is the most exposed to a one-reading shift:
   - Welch p = 0.059;
   - the curve is not monotonic;
   - 3 of 13 rats are not negative.
3. **edfig6 blocking (B3), partly resolved.**
   - The timing text contradicts the printed timing (2.1).
   - The scaling assumes 4 processes, although the reading is network-bound and `read_all` already runs 16.
   - At 7.1 s per hour, the 3-rat subset with stored brain states (557 h, about 66 min) could come in under 30 min with about 3 times more parallelism. That would allow a partial test of three claims that are now blocked.
4. **Not checked by me:** the figures. I read only the text outputs.
