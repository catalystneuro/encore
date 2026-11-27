I did steps 1 to 6 of the Author section for 001454-patel-2026, and `python tools/entry.py all` passes on both notebooks. Of the 61 claims, 11 are reproduced, 3 partially reproduced, 12 not reproduced and 35 blocked; 11 outcomes rest on an assumption.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig2c (isolation raises male BLA-mPFC firing) | partially reproduced, assumed |
| fig2e (group-housed females fire more than males) | partially reproduced, assumed |
| supt1-male (isolation raises input resistance) | not reproduced (p = 0.052), assumed |
| ed2e, ed2bcd, ed3d | reproduced |
| ed3c (rank 1 fires least) | partially reproduced (below rank 3, not rank 2) |
| fig2d, fig2-threeway, supt1-female | blocked, data_unreadable |
| fig3f, ed5ef, fig3ijl, ed6k | reproduced, assumed |
| ed5d, fig3k (r² 0.083 against 0.59), ed6ij | not reproduced, assumed |
| fig3h ×2, ed6b (decoding) | blocked, other: too few bouts per mouse |
| fig5c, fig6gj, fig6n, ed8op | reproduced |
| fig5b, fig6lm, ed8n | not reproduced, assumed |
| fig5d, fig6c, fig6de, fig6f, fig6k | not reproduced |
| Fig. 1 and Extended Data Fig. 1 (12 claims); optogenetics with behaviour (8); ed5c, ed6cd, ed7; resident-intruder (5) | blocked, data_missing (28) |
| ed9c | blocked, not_runnable (CellReg is MATLAB) |

## 2. The dataset

**Version.** I pinned 0.260911.2319, the only published version. The paper cites no version, and the release notes say it holds all data used in the publication.

**What is not in it.** Home-cage drinking licks, ranks of the drinking and imaged mice, blood alcohol, unimplanted controls, optogenetics with behaviour, the stability imaging, and pose tracking or interaction labels for the resident-intruder sessions. The dandiset description lists pose tracking, but the files hold none.

**Patch clamp.**
- 13 female files hold no recording (flat voltage, no step current). That leaves 3 isolated female neurons from one mouse, against the paper's 15 from 7.
- One isolated male file holds only the -120 pA sweep.
- The dandiset has 37 group-housed male BLA-mPFC neurons; Figure 2c uses 21 from 7 mice. The 2022 cohort matches that count exactly, but nothing marks which neurons were used.

**Imaging.**
- The files hold every ROI, not the paper's hand-curated neurons (1113 against 540, 347 against 196, 748 and 439 against 240 and 281).
- Nothing says which BLA cohort is projection-specific; the virus field is empty.
- Three pairs of files hold identical traces with different licks. The traces follow the licks of one file in each pair, so the other file is left out (BLA-mPFC has 9 mice, not 11).
- All 53 sessions carry the same cue times. In 5 of 9 mPFC mice and 10 of 11 cohort-16 sessions, mice lick the bottle a forced trial does not offer, so the stored trial types, and with them which trials were stimulated, can be wrong.
- Cohort 9 traces are non-negative, although the Methods say CNMF-E ran without that constraint.
- Lick times are stored as data in series that also declare a 100 Hz rate.
- Trace-to-lick alignment could be shown for 40 of 53 sessions.

**Assumptions.**
- Figure 2c's group-housed males are the 2022 cohort. All 37 neurons are shown as a variant; with them, input resistance gives p = 0.002.
- Cohorts 9 and 10 are nonspecific BLA and cohort 16 is BLA-mPFC, from the mouse counts.
- Matched bouts are drawn at random. Taking the first bouts instead would reproduce fig5b and the one-sided reading of fig6lm.

**Questions for the paper's authors** (recorded as a methods_unavailable finding):
- How were matched bouts chosen?
- Which neurons form Figure 2c?
- How were five decoding folds formed when most mice have 0 to 2 water bouts?
- Which BLA cohort is projection-specific?
- How were flat baselines treated?

**Questions to a reader:** none.

## 3. Where the protocol was unclear or did not fit

1. It assumes one notebook. I split the work into a patch-clamp notebook and an imaging notebook, each with its own header and summary; the blocked claims are listed in the patch-clamp header.
2. It says a seed cannot change an outcome. Here one random draw decided ed8n (p = 0.048). I judged that reading over 21 draws, where only 5% fall below 0.05, and recorded this as a deviation.
3. It has no rule for a dataset that holds a superset of the paper's units with the selection lost. I tested on all ROIs and recorded it as a deviation and a selection_undocumented finding.
4. Which imaging population is which can be inferred from counts. The protocol's metadata_insufficient block did not clearly apply, so I adopted the assignment as an assumption.
5. Its alignment-check examples do not fit continuous imaging with licks. I compared the response at true bout onsets against onsets shifted by -20 to +20 s.
6. Empty files could be data_missing or data_unreadable. I blocked the claims as data_unreadable and recorded the finding as data_missing, since the finding kinds have no "unreadable".
7. It does not say whether MATLAB-only software (CellReg) should be reimplemented. I did not, and blocked ed9c as not_runnable.
8. For the patch clamp I set a 5 mV re-arm on spike counting and pooled versus per-step post hoc errors; both are stated as standard choices or readings.

## 4. Runtime and failures

The run took about 1 h 25 min (17:13 to 18:37 UTC). The patch-clamp notebook runs in about 6.6 min and the imaging notebook in about 2.8 min. No analysis failed.

Two permission-denied commands:
- An attempt to view part of a saved output was denied; I read it with the Read tool instead.
- Removing `entries/001454-patel-2026/__pycache__` and an empty `.claude/` directory was denied. Both are git-ignored or empty, so they will not be committed.

The handover package is in `executed/001454-patel-2026/handover/`. Nothing was committed.
