**Verifier report, round 2: Shi, Apker & Buneo 2013 on CRCNS ppc-1**

The claims file has 28 claims, and the attempt record gives an outcome for each of them. The record has 7 reproduced, 5 partially reproduced, 13 not reproduced and 3 blocked. Twelve outcomes are marked `assumed: true`. Cell indices below refer to the re-executed notebook. They have shifted since round 1.

### 1. Outcomes

I agree with all 28 outcomes in the record. Three of them differ from what I gave in round 1:

- **fig4-indx1-means: partially_reproduced.** I now agree. The criterion requires two things. The Position Only part holds in full: −12.0% is within −13 ± 1.3, and it is the least negative group. The Position/Vision part fails: −24.2% is outside −31 ± 3.1, and it is not the most negative group (cell 67). Calling that partial is defensible.
- **rate-variance-nv-higher: partially_reproduced.** I now agree, but only just. The criterion is purely numerical, and both means are outside tolerance: 46.4 against a bound of 50.4, and 23.1 against 27 (cell 78). The "tended to be higher" part of the statement does hold: NV is higher in 67% of cells, at about twice the V value. That direction rests on the code mapping, and the record flags this.
- **longer-hold-no-difference: blocked (data_missing).** I now agree. The per-trial table (cell 15) removes my round-1 objection. No completed trial has a code 10 to code 12 interval shorter than its own field 11 plus 28 ms. This supports reading field 11 as the minimum hold. No completed trial has field 11 ≥ 1,200.

**Assumptions.** Each flagged assumption is stated in the deviations and is reasonable:

- movement onset read as code 8
- the first sorted unit in each session (hold-vision-main-effect, hold-subepochs, fig4-indx1-negative, decoding-subepochs; the all-units variant changes each of these, as the notebook shows)
- correlation reading (a)
- FF outlier reading (a)
- CV2 reading (a)
- V = code 4 (rate variance, FF, CV2, NV/NV decoding, V better than NV)

One flag is not needed. fig6-decoding-vv is marked `assumed: true`, but it is not reproduced under both code mappings (63.7%) and with all units (68.4%), so its outcome rests on no assumption.

### 2. Sentences the printed outputs do not support

- **Cell 112:** "each session's shortest interval follows its field 11 (800 to 1,100 ms against 0.83 to 1.15 s)". Cell 111 contradicts this. Sessions grouped by field 11 = 900 have a shortest interval of 0.832 s, and those with 1,000 have 0.960 s. Both are below their field 11. The per-trial claim in cell 15 holds; this per-session one does not. Most likely the three sessions whose field 11 changes within the session explain it, but the sentence does not say so.
- **Cell 10:**
  - "Code 10 follows the target code by 320 ms on every trial". Cell 9 gives a range of 0.224 to 0.416 s.
  - "Code 8 follows 0.22 to 0.58 s later" and "Code 3 comes 0.54 to 0.96 s after the trial starts". These ranges are the 5th to 95th percentiles, not the minimum to maximum: 0.08 to 1.12 s and 0.54 to 1.92 s.
  - The record's movement-epoch-tuning deviation repeats the "0.22 to 0.58" and "0.03 to 0.38 s" ranges without saying they are percentiles.
- **Cell 93:** "With all 483 units only the test over bootstraps finds it". Cell 90 shows that with all units, populations of 200 cells, the paired test over targets also finds it (P = 0.0364). The outcome is unaffected.
- **Cell 68:** "Readings (b) and (c) give the same." Reading (b) gives 78.4% and 70.0% for all cells and Position Only, not (a)'s 77.8% and 68.4% (cell 67). The outcome is the same. The record's notes state these values correctly.
- **Cell 59:** "The position percentages are close". The first-400 ms position percentage, 35.7%, is outside 31 ± 3.1 (cell 56). The record's "near the paper's" has the same problem.
- **Cell 76:** "the closest, outliers on INDX2 by reading (c), gives −1.7, −10.5 and −9.5%". All units with the same reading gives −2.0, −14.1 and −9.9 (cell 75), and its −14.1 is within −13 ± 1.3, so it is arguably closer. The outcome is unaffected.

Everything else checks out against cells 9–112: all other Result conclusions, the Summary section, the README table (its counts match the record: 7 / 5 / 13 / 3), and the record's notes and findings.

**Round-1 reasons in the record.** They are mine and faithfully stated. Some have my section-B points folded in (B2, B3, B6, B7, B8), which is accurate. The `agrees: false` flags on fig4-indx1-means and rate-variance-nv-higher correctly record that I disagreed in round 1. Those disagreements are now withdrawn (§1).

### 3. Round-1 points

**Resolved**
- **B3, window placement.** Cell 15 gives the per-trial interval against field 11. 11.6% of windows start less than 250 ms after code 10. The late-start variant (cells 57, 58, 97) leaves hold-subepochs and decoding-subepochs unchanged.
- **B2, in part.** The MANOVA is calibrated on these data (5.7% significant with shuffled labels). The two conditions are interleaved within sessions. Within-session SDs are printed (cell 32).
- **B7.** The decoder's chance level on these data is 16.1% (V) and 11.2% (NV) with shuffled labels (cell 89).
- **B9.** The unused branch has been removed from `ppc.decode`.
- **B5.** The one-unit choice is now flagged on the four outcomes it changes. I checked the other outcomes under all units, and none of them changes.
- **The eye-position block.** It is confirmed as `metadata_insufficient`. The analog channels are now shown (cell 104). The note on fields 22 and 23 is corrected.

**Remaining, bearing on conclusions**
1. **Population (B1).** The record has 359 monkey X sessions against the paper's 219. The new checks (dates, geometry by month, same-day tuning) rule out monkey B and repeated recordings of one neuron. They do not say which sessions the paper used. Every count, index and decoding claim rests on this. It is stated as a finding and cannot be settled from the data.
2. **Fields 19–21 (B2).** Whether these are the mean over the hold or a single sample remains undecidable. The behavioural and Table 1 outcomes, and data set 1 of correlation-endpoint-datasets, rest on them. This is stated.
3. **V = 4 mapping (B4).** It is unchanged, reasonable and flagged. The outcome of fig6-decoding-nvnv and the direction of rate-variance-nv-higher, fig5-fano-factor, cv2-larger-nv and decoding-v-better-than-nv depend on it.
4. **Possible misreading in the claims file (B6).** The two outlier readings for fig5-fano-factor may not match the cells of Fig. 5. This is now asked of a reader. It does not change the outcome: no reading reproduces the claim, including the 0–80 range variant.
5. **Clock alignment per session.** This is now checked (cell 23). In 206 of 359 sessions no unit is tuned in the hold, so the shared spike and event clock is not confirmed there. A misaligned session would dilute the counts and the decoding.
6. **The eye-position block depends on the layout read for the analog files.** Seven channels were read out of 16 described, and channel 6 spans 16 bits, so the block rests partly on a layout reading that is known to be at least partly wrong. If fields 22 and 23 were eye position, reading (a) would fail the claim: Levene's test gives P = 0.012 at 90°, vertical (cell 103).

B8 (the t-test over bootstrap accuracies is pseudo-replicated) was not addressed. It decides no outcome.
