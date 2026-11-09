**Round-2 verification: Holdgraf et al. 2016 (doi:10.1038/ncomms13654) on CRCNS ac-4**

**1. Outcomes**

The claims file has 26 claims and the attempt record has 26 outcomes, one for each claim. I agree with all 26 outcomes. Notes on the ones that need them:

| Claim | Record | Agree | Note |
|---|---|---|---|
| 6 behavioural claims | blocked (data_missing) | yes | |
| speech-r-count | reproduced | yes (changed from my round-1 "partially reproduced") | The criterion judges only the count, which is within tolerance under 3 of 12 readings (cell 8), and says the 468 total is only reported. My round-1 outcome came from the expected total, which I had myself rated as not affecting a conclusion. |
| fig3b, supp4, fig9-middle, fig10c, supp6b | reproduced | yes | fig10c holds by a small margin (0.517 against 0.5). |
| supp3a | reproduced | yes | The wording is wrong; see section 2. |
| supp5b | not_reproduced, assumed | yes | The assumption (keep the non-event z-score used for every HFB claim) is stated and reasonable. That z-score was chosen because it matches the Speech-R count, not from the paper's "z-score over baseline", so the outcome is only as firm as that choice. |
| fig4a | reproduced, assumed | yes | NW = 2 also passes both post-stimulus windows (cell 17), so the outcome does not depend on the bandwidth. |
| fig4b | reproduced, assumed | yes | At NW = 2, reading (b) still passes (P = 0.012, cell 19 row 20), so the outcome does not depend on the bandwidth either. |
| strf-r-count, included-electrode-count, fig10b | not_reproduced | yes | |
| fig8 | not_reproduced, assumed | yes | The region rule is the claims file's own assumption, and both rules fail on the shift. |
| fig9-rms, fig10 | partially_reproduced | yes | |
| supp3b | blocked (other) | yes | |
| supp6a-connectivity | reproduced, assumed | yes | It uses the criterion's seeds (9) and the claims file's standard bandwidth (NW = 4), both stated. The outcome reverses under either alternative: temporal targets give P = 0.070 at NW = 2 and 0.094 with the 6 temporal seeds (cell 45). My round-1 point that the criterion misreads the Supplementary Methods' "Temporal seeds" stands and has been passed to a reader. |
| supp6a-after-closer | reproduced, assumed | yes | It reverses at NW = 2 with 9 seeds (0.204 against 0.182, cell 47 row 3). |
| supp7 | reproduced, assumed | yes, conditionally | The supp7 criterion names open details 6 and 11, not 10. Carrying detail 10's MNE default over to supp7 is an extension, but it is stated and reasonable. The theta cluster (7.3 to 8.7 Hz) overlaps 3 to 8 Hz only at its lower edge, and at NW = 3 the outcome reverses. |

The claim that MNE's default normalized half-bandwidth is 4 is correct. Minor point: at NW = 4 on 400 ms windows the half-bandwidth is 10 Hz, yet the integration starts at 2.5 Hz. The claims file says "from the lowest resolved frequency", which this arguably does not meet.

**2. Sentences the printed outputs do not support**

- **Supp3a: "less data" (cell 30 and the record's notes).** Cell 30 says "so the absence here reflects less power more than a smaller effect"; the record says "an effect of similar size and less data". Cell 4 shows 28 pink-noise and 29 speech triplets per subject. The means (0.0409 and 0.0410 z) and s.e. (0.019 and 0.017) are also equal (cell 13). So the speech cluster's significance does not come from more data; it comes from the time course (0.50 to 0.74 s).
- **Supp5b: "it holds under the per-trial baseline" (cell 16 and the record's notes).** Under the per-trial z-score, unit (a) with pairs resampled excludes 0 (−0.0037 to −0.0005, cell 15 row 4). The absence holds only with the grouped bootstraps. The "three of four" stated next to it is correct.
- **Fig4a: "mostly the bias of single-trial coherence" (record's notes).** The full sentence is "about 15 bits/s in both conditions, mostly the bias of single-trial coherence". No output measures the bias. The pre-stimulus value is 14.5 bits/s (cell 17), and my round-1 estimate of the residual bias on independent noise at NW = 4 was 3.8 bits/s.
- **Summary, cell 54: "on which fig4b, supp6a and supp7 depend".** Fig4b does not change at NW = 2 (it passes under reading (b)). Supp6a-after-closer-to-middle does change (cell 47) and is not named. The README's "Three coherence outcomes rest on the multitaper bandwidth" should name supp6a-connectivity-increase, supp6a-after-closer-to-middle and supp7.

Every other sentence I checked in the Result cells (9, 12, 16, 18, 20, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54), the Summary, the README and the record's notes matches the printed numbers.

**Round-1 reasons in the record:** they are faithful and mostly in my own words, with problems B1 to B13 and the section C items folded into the relevant claims. One small omission: the strf-r-count reason drops my note that choosing alpha on the same R2 that selects STRF-R would raise the count, not lower it.

**3. Round-1 points**

Resolved:
- **B1 (supp5b):** all three z-scores are now run, with grouped bootstraps.
- **B2 (supp6a seeds):** the notebook now uses the criterion's seeds, shows the temporal seeds as a variant, states the deviation, and passes the question to a reader.
- **B3 (bandwidth):** NW = 4 is now the main reading, with the earlier choices as variants.
- **B7 to B12:** the cutoff region rule, the window assignment, the 0.041 values (shown to come from different arrays), the no-baseline wavelet power, leaving each electrode out of its own PAC phase mean, and the frontal definition.
- **B13:** the expected total has been passed to a reader.
- **Section C:** the per-subject counts against Figure 6b are now printed, and the data set's notebooks were read. I cannot check that reading; those notebooks are not in my materials.

Partly resolved:
- **B5 (alignment):** the ±0.5 s shift check shows no global offset in S01 and S04.
- **B4 (RMS unit):** this went to a reader and is still open.
- **B6 (alpha grid):** unchanged, disclosed, and not affecting a conclusion.

Remaining points that bear on a conclusion:
1. **Why STRF-R fails (strf-r-count and every claim built on the 9 included electrodes).**
   - The shift check tests one fixed offset per subject. It does not test clock drift over the session. S07's audio track is 1015 s for a 989 s recording, and its best median shift sits at the edge of the grid (−0.5 s, cell 25).
   - Comparing the best shift in early and late trials would separate drift from a fixed offset.
   - The negative held-out R2 values, set against Figure 6b, point to a different score. That question is with the paper's authors.
2. **Bandwidth and seed choices.** Supp6a-connectivity, supp6a-after-closer and supp7 each reverse under the earlier bandwidth, and supp6a-connectivity also reverses under the Supplementary Methods' seed set. All of this is disclosed and asked of the authors or a reader, but these three outcomes are fragile.
3. **Supp5b** depends on the z-score, as in section 1.
4. **Fig9-rms:** whether the absolute tolerance can apply to a quantity with no stated unit is still open with a reader.
