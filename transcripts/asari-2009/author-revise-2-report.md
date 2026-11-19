I've worked through every point in the round-2 report. No outcome changed, and one change is proposed for round 3. The entry was re-run with `python tools/entry.py all entries/asari-2009` and passed (main notebook 43 min, STRF notebook 16 min). Every number that was already in the notebook came out identical, and `check` reports 0 errors.

**Outcomes**
- **fig3b-fractional-power-decay:** I kept the verified not reproduced and proposed partially reproduced under `proposed`. As the verifier noted, fig3b and fig4 show the same pattern but were graded differently, and I found no reason for the difference. In both, the size is within tolerance (fig3b: all 4 readings with silence counted; fig4: 10 of 14 fits). The time constant is never within tolerance: 1.50 to 2.01 s and 1.60 to 2.83 s, against 1.04 s. A new notebook cell sets the two claims side by side, and a markdown cell after it gives the reasoning for round 3.
- **fig8b-decay-by-property:** the verifier's gap is now covered. I changed `asari.py` so the pair tests keep their power terms, then fitted higher-order under the pairing adopted for fig8a. The time constant is 0.25 s with each of 131 probes counted once and 0.22 s with each of 336 pair tests counted once, 0.16 to 0.25 s across readings. All are below 0.3 s, so the partial rule still holds and the outcome stays partial. `measured` now takes the paired values (0.252 s, size 0.78).
- **fig8c-relative-effects:** I added the higher-order result under the pairing. The point estimate is 0.35 (0.15 when the noises are pooled). Its interval is 0.30 to 0.41 with probes resampled and 0.19 to 0.50 with trials resampled, both below 1 under all five seeds. Amplitude and frequency are still well below 1, so the outcome stays not reproduced. `measured` now takes the paired value.

**Corrections and additions**
- **fig8a:** the record and notebook now set the counter-evidence beside the assumption. Only pooling gives Table 1's exact 137 higher-order probes (the pairing gives 131), and under pooling the order fails by 0.640 against 0.642. The totals are no longer offered as evidence that the grouping is right. Instead, the record lists the per-ensemble counts that make them up: 25 + 25 probes from the natural-sound variant files, no MHT probes, TORC 42/44 against 39/40, and natural probes 20/21 against 23/25.
- **AM time constant:** cell 45 (fig8b's result, formerly cell 42) and the fig8b notes no longer say AM is within tolerance. AM's 0.097 s is just below the 0.099 to 0.121 s band, so no time constant is within tolerance.
- **STRF cell 7, fig4-strf notes:** these now say both cell sets gain, but the gain is larger and only significant in the 2003 cells.
- **Summary cell:** it now says the data set holds 145 and 14 cells against 194 and 16, and that only the analysed natural-sound and MGB samples match the paper. The finding about the shipped analysis code is corrected the same way.
- **Round 2 record:** added under `verifications`, with all 21 claims marked as agreed and the verifier's reasons quoted or closely paraphrased.

**Not done**
- **Questions file:** I added nothing to `questions/asari-2009.yaml`, because the verifier found no place where the claims file misreads the paper.
- **fig8a-significance-fits:** this still uses the pooled higher-order group. A paired version would need a noise floor for the pair tests, which means extra shuffle runs that weren't done. The verifier didn't ask for it, and the notes say the group is the pooled one.
- **Round-1 wording:** I left the round-1 `response` on fig4-strf as it was. It repeats the "comes from the 2003 cells" overstatement, but rewriting it would change the history of that round. The round-2 entry records the correction.
- **README run times:** these still say "about 40" and "about 20" minutes; this run took 43 and 16.

Nothing has been committed or pushed.
