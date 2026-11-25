**Verifier report, round 3: Peterson et al. 2021 on DANDI:000055 (0.261123.1703)**

The claims file has 25 claims and the attempt record has 25 outcomes. One outcome has a proposed change: fig5-recording-day-effects. I reviewed only that one.

| Claim | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig5-recording-day-effects | partially_reproduced (now not_reproduced) | Yes | — | See below. |

**How I checked fig5-recording-day-effects**

- **The criterion is applied as written.** Cells 67 and 76 run a one-way Kruskal-Wallis test across recording days for each subject and band, with uncorrected p < 0.05. The band mean is the main result and the band median a variant. Agreement is counted against the paper's 11 significant pairs and 13 non-significant ones.
- **The counts are correct.** In cell 76, under each file's own flags, the band mean disagrees with the paper in 4 pairs: S01 LFB (p = 0.047), S01 HFB (0.023), S06 HFB (6.7e-11) and S10 HFB (0.094). That leaves 20 of 24 agreeing, which is exactly the criterion's threshold for partially reproduced. When only the electrodes bad in every file are removed, the disagreements are S01 LFB, S01 HFB and S06 HFB, so 21 of 24 agree.
- **The analysis I asked for in round 2 was run.** That is the set that removes only the electrodes bad in every file (cell 76). The criterion's comparison with Table 2's per-day intervals is now printed in cell 67: 41 of 55 subject-days fall inside the interval for LFB and 42 of 55 for HFB.
- **The choice of electrodes does not look made to reach the result.**
  - The proposal rests on a count that does not depend on the outcome. The paper removes 4.9 ± 4.9 surface electrodes per subject. I confirmed that wording in the paper's Methods, "ECoG data processing".
  - Cell 4 gives the counts for each set: 4.2 ± 2.1 with each file's flags, 12.6 ± 8.4 for the main set (electrodes bad in any file removed), and 1.2 ± 0.4 with only the electrodes bad in every file removed.
  - The paper flags bad electrodes by comparing each channel's SD and kurtosis with the median over channels. That is naturally done per recording, which fits per-file flags.
  - Two of the three sets that can be defended give partially reproduced. Only the main set gives 18 of 24, and it is the furthest from the paper's count.
  - Each file's flags were also the main analysis in round 1.
- **The other region claims keep their outcomes under each file's flags** (cell 76, summarised in cell 77):
  - fig3: the group pattern holds in 3 of 3 regions, and the sensorimotor regions are the largest.
  - fig3-lfb-more-widespread: the readings still disagree, so it stays blocked.
  - fig4: 3 of 4 parts hold (partially reproduced).
  - table1: 21 of 24 inside (partially reproduced).
  - discussion-day-changes-small: largest day deviation 1.487 dB.

  So the change does not choose a different electrode set for this claim alone in a way that moves any other outcome. The regression claims were not refit under each file's flags, and cell 77 says so.

**Caveats; none changes my verdict:**
- 20 of 24 is exactly the threshold. With the band median as the variant, each file's flags give 19 of 24 (cell 76).
- The S10 HFB pair depends on the electrode set: p = 0.094 with each file's flags, 0.015 with only the electrodes bad in every file removed, and 0.054 with the main set.
- Cell 68 and the record's notes still describe the main set's 18 of 24 as the result. If the proposal is accepted, they should state that the outcome rests on each file's own flags.

I found no place where the claims file misreads the paper for this claim.
