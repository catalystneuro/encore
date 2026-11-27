I've tested `yang-2025` on DANDI:001212 v0.241023.0931: 14 claims tested and 5 blocked. The entry is at `entries/yang-2025`, the record at `attempts/yang-2025-02.yaml`, and the handover package is built. The final clean run passed (`entry.py all`, 0 errors) and its outputs match the numbers in the conclusions.

The dandiset has no seizure or stimulation times, so this attempt finds both from the LFP. Every tested outcome except ictal ripples rests on that, and all 13 are marked as resting on an assumption. I did not come across any earlier attempt.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| tables1-network-stable-short-term | reproduced, but only when each seizure's correlation with itself (r = 1) is counted, a reading the criterion lists. Without it, 4 of 7 rats hold (6 with other onset thresholds) |
| fig2-r1-target-shifts | reproduced (ANT, ANT, CA3, DG) |
| figs2-target-assignment | partially reproduced: 18 of 28 baseline groups match; 20 of 28 labels agree |
| fig3a-target-reduces-each-rat | not reproduced: 3 of 8 target groups below baseline |
| fig3a-nontarget-can-lengthen | reproduced: 13 of 20 |
| fig3a-per-rat-site-differences | partially reproduced: 5 of 11 pairs, and R6 has one significant pair |
| fig3a-target-vs-nontarget-total | not reproduced: −0.020 against 0.087, p = 0.085 |
| fig3a-some-nontarget-shorten | not reproduced |
| fig3b-same-site-target-vs-nontarget | not reproduced (only ANT is significant) |
| fig4b-psd-target-bands | not reproduced in all 36 readings |
| fig4b-psd-other-bands-unchanged | not reproduced: delta p = 4.8e-21 |
| fig5b-iis-post-seizure | reproduced: paired t-test over 1 s bins p = 2.1e-9; Mann-Whitney alone gives p = 0.0032 |
| fig6e-ictal-ripples-no-difference | reproduced: no difference, p = 0.26 |
| fig6f-ictal-fast-ripples-reduced | not reproduced |
| seizure-duration-proportion, fig3c, fig5c, fig5d, fig6cd | blocked, `data_missing` |

**2. Dataset, assumptions, questions**

- **What is in it:** 56 files and 519 epochs. Each epoch is 600 s of 4-channel LFP at 1 kHz around one seizure. There are no seizure times, stimulation times, interictal segments or recording durations, and no duplicated epochs or channels.
- **Group order:** for R5 and R6 the order of stimulated sites differs from Figure S2, and the epoch dates follow the dandiset's order.
- **Stimulation not visible:** 130 Hz trains are found in most stimulation seizures, but in only 1, 1, 0 and 0 seizures of R7's four groups and 0 of 8 in R3's CA1 group.
- **R3's CA1 group dates:** its epochs fall within the DG group's days and before R3's last baseline group.
- **Stimulation in baselines:** four baseline epochs carry trains at the rat's own pulse rate.
- **Assumptions:**
  - Seizure onset and end come from a 1–45 Hz line-length rule (threshold 2; 1.5 and 3 shown as variants).
  - Stimulation trains come from the artifact's spectral comb.
  - Granger causality is computed with my own regression code rather than the MVGC toolbox, with model order chosen by BIC and cf_w taken as out minus in.
  - Seizure duration is normalized as relative change against the preceding baseline.
  - HFOs are automatic detections at mean + 3 SD, with no manual review.
- **Questions for the paper's authors:** recorded as a `methods_unavailable` finding: the seizure marking rule, GC settings and cf_w sign, the normalization formula, HFO App parameters and windows, and the Figure 5B test.
- **Questions to a reader:** none.

**3. Protocol and tool problems**

1. `entry.py lock` writes `python: "3.13"` into `entry.yaml`, but the entry schema rejects that field. I removed the line; the tool then reads the version from the lock file.
2. Readings that make a test trivially easier, such as counting r = 1 self-pairs in tables1, can decide an outcome under the "any reading" rule. I applied the rule and said so in the notes.
3. A paired t-test over time bins (fig5b reading b) treats bins as independent. I reported it alongside the Mann-Whitney result.
4. The protocol has no category for a dataset that disagrees with the paper when it is unclear which is wrong (the R5/R6 order). I recorded it as `other`.
5. The provenance prompt asked for harness "Claude Code"; the example record uses "Claude Code (GitHub Actions)". I used "Claude Code", with the runner recorded separately.

**4. Runtime and failures**

The notebook runs in about 4.5 minutes, with a worker peak of 0.44 GB. The whole session took about 50 minutes, ending at 01:07 UTC. The only failure was the schema error in point 3.1; nothing else failed.
