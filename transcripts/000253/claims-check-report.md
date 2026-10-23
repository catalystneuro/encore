I made 11 corrections to `claims/000253/10.1038-s41586-020-03171-x.yaml`, left four problems open, and marked the file ready. Nothing is committed.

**Checker:** `claims/000253/10.1038-s41586-020-03171-x.yaml: 35 claims, 35 quotes, 23 statistical values, 0 problems`. It reported 27 statistical values before my edits; the drop is the four entries I removed.

I checked each claim against the full text. I also cloned the paper's code at the commit the file cites (`neuropixels_platform_paper` @ 4f8bcc2) to check every criterion that leans on it.

**Changes, by claim**
- **methods-probes-ccf:** removed "about 5.7 probes per mouse" from the statement and expected values. The paper never gives that number; the writer worked it out as 332/58. Which sessions the 332 probes come from is now named as open.
- **fig2f-directionality-vs-anatomy:**
  - The hierarchy difference had the wrong sign. It was source minus target, which would give r of about -0.74. The notebooks build it as target minus source, which gives the reported +0.74.
  - The code pools the offsets of all 25 mice, as the Fig. 2e legend says, so pooling is now the rule and the mean across mice is a variant. The notebook's convention for which offsets count as positive is now named.
- **ed8-total-hierarchy-score:** the code settles both details that were open: the mean includes the diagonal and the directionality scores are pooled (it prints 0.8906). The lower bound is now the one-to-all value 0.15, which is the comparison the Methods make, instead of 0.38.
- **ed9a, ed9d, ed9e, ed9h (pairwise tests):** removed the statistics entries. They recorded only the 0.05 significance level, which is a threshold, not a result, and the text never prints it. The per-pair p-values are only in figure matrices. The criterion now says alpha 0.05 comes from `Figure3.py`.
- **fig3f, fig3i, fig3l:** added a missing unit cut. `Figure3.py` keeps the "time to first spike < 100 ms" filter when it moves on from latency, so it applies to all four metrics.
- **fig3i:** the code takes log10 of each unit's index before averaging, so that is now the rule and the plain mean is a variant.
- **fig3-unit-counts:** the code prints neither count, so whether 15,713 is counted before or after the latency cut is now two readings.
- **ed10b-layers:**
  - The code's test pools all cortical units, not just the six areas (its area line is commented out). I followed the code and made the six-area pool a variant.
  - Mean difference and log10 modulation index are settled by the code and are no longer readings.
  - The superficial group follows the legend (layers 2/3 and 4). The code's "layer < 5", which can include layer 1, is a variant.
- **ed10ce-superficial-lead-deep:** removed a "positive in at least four of six areas" rule that the paper does not give. The claim is now judged on the Ext. Data Fig. 10e score, with two ways of combining areas named.
- **ed9p-decoders-above-chance:** extended the quote to include the legend sentence saying accuracy does not correlate with hierarchy.

**Still open (recorded in `checks`)**
- **ed7e:** the legend does not say whether 21 or 15 area pairs are used, and it names no test for this absence claim.
- **ed9p:** "better than chance across trials" names no test.
- **fig2 CCG claims:** the unit quality filter and the CCG window are still listed as readings. The code reads files that are not in the repository.
- **fig3c:** which flashes (dark, light or both) feed the latency is not given anywhere.

Every main finding has a claim, and none comes from a source other than this paper.

**Ready:** yes. The `checks` entry is dated 2026-10-23 with `ready: true`.
