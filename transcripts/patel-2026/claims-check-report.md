I made 17 corrections and the file is ready for an attempt, with four problems left open that the criteria already handle.

**Checker:** `claims/001454/10.1038-s41593-026-02413-x.yaml: 61 claims, 61 quotes, 64 statistical values, 0 problems`. It reported 60 claims and 0 problems before my edits.

**Changes, by claim**
- **Header:** added M8. The Methods define rank as the proportion of wins, but the legends correlate "Rank", so both are now readings. ed1c, ed1d, ed1e and ed1l use them.
- **fig1-threeway-sex-liquid-housing:** reproduced is now p < 0.05. It had been p < 0.001, stricter than the statement, which only says the interaction is significant.
- **ed1c:** added the M8 readings. The printed p = 0.01 equals the uncorrected p, which supports the no-correction reading.
- **ed1e:** dropped the four-test Bonferroni reading. With r² = 0.41 and 14 mice it gives p ≈ 0.054, which the printed p < 0.05 rules out.
- **ed1l:** the two-test Bonferroni family is now marked as a reading; it fits the printed p.
- **ed2e:** removed an invented condition (its F smaller than Fig. 2c's). Both spike readings are now required.
- **ed4gm:** the paper gives neither the tracking source nor the time window. Added readings: EthoVision body centre or SLEAP points, over the 3-min stimulation epoch or the whole 6-min interaction.
- **ed5d:** the cue baseline is now read as 3 s or 5 s, as the Methods allow. Only 3 s had been used.
- **fig3f:** stated that the clustering pools both populations, as the Results say.
- **fig4e:** the legend does not say which effect F(2, 20) is. Both the session main effect and the interaction are now readings, as are both baseline definitions.
- **fig4hi:** the "OFF" bouts had been fixed to the baseline session with no source. Baseline and recovery sessions are now both readings.
- **fig5b, fig5c, fig5d:** the paper does not say which trials enter the housing comparison. Nonstimulated trials only and all trials are now both readings.
- **fig6f:** removed "reversing its group-housed effect" from the statement, since the paper does not say that.
- **fig6gj:** the source now includes Extended Data Fig. 8q,r.
- **ed9hi:** a two-test Bonferroni cannot give the printed p = 0.04 at r² = 0.02 with 199 neurons. The outcome is now judged uncorrected, with the corrected result reported.
- **ed9k-o:** the criterion required above-chance decoding in all four sessions, but the panel l legend says isolation abolishes decoding without stimulation. I rewrote the statement and criterion to match the k to o legends.
- **New claim ed8op-stim-no-alcohol-proportions-si:** Extended Data Fig. 8o,p had no claim.

**Open**
- Supplementary Tables 1 and 2 are not in the text, so the two supt1 claims carry no numbers.
- The error df in ed9fg (7350) and fig6q (13) do not match the stated sample sizes.
- Several groupings are readings the paper does not give: the Fig. 1d time blocks and the Extended Data Fig. 4 levels (UMAP clusters or time bins). If the readings disagree, the criteria return methods_underspecified.
- Extended Data Fig. 1o–q and 9r have no claim; they are secondary panels.

**Ready:** yes (`ready: true` in the new checks entry). Nothing was committed or pushed.
