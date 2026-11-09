I've worked through all eleven problems in the round-1 report and its list of missing outputs. One outcome changed, every other outcome stayed the same, and the PPX washout claim is now marked as resting on an assumption. The final `python tools/entry.py all entries/001177-zhuang-2025` passed: 0 errors, about 14.5 minutes. `check` passes on the updated record, and the round is recorded under `verifications`. Nothing is committed.

**Outcome change**
- **fig5jl-dreadd-params: partially reproduced → not reproduced.** The verifier is right that the criterion decides this. Its partial case needs the K and AUC results to hold with only the A pattern failing. Here the A pattern holds and the K rise in hM4Di mice fails (p = 0.20), so it is not reproduced, narrowly: eight of nine parts hold.

**Kept, with new analysis behind them**
- **figs2ijk-ppx-washout: still partially reproduced, now marked as resting on an assumption.** I added the pooled-error Bonferroni comparisons the verifier asked for (problem 4). With them, all three parts of the claim hold (K p = 0.028, AUC p = 0.0072), so the outcome depends on which comparison is used. The paper says it used GraphPad Prism 10. Prism's guide says it uses the pooled error only when sphericity is assumed, and recommends not assuming it for repeated measurements over time. So I kept the paired comparisons as the assumption, recorded it as a deviation, and added it as question 4 for the authors.
- **fig1ijk and the A77636 claims:** all four ON/OFF session pairings now run (problem 3). The Dunn p for K under PPX is 0.19, 0.23, 0.49 and 1, never significant, so nothing changes.
- **fig3a-a-correlates-dms: still not reproduced.** The first-PPX-session reading now runs and gives r = 0.08. The notebook lists the mice dropped from the join both ways:
  - six PPX mice have no histology;
  - E6 has histology but no PPX session;
  - E3 and E3.2 have histology but are in no README list.

  Whether E3.3 is one of those under another name can't be told from the deposit. I recorded that as an `identifier_missing` finding.
- **fig5cf-cno-locomotion: still partially reproduced, resting on the 20 min injection time.**
  - H0 and H0.4 are confirmed to be the same recording. Without H0.4, hM4Di gives p = 0.008.
  - The notebook now prints velocity minute by minute from 15 to 25 min for the 12 files with no tracking gap there.
  - Using only files that do have a gap, mCherry mice are slower in 6 of 7 but not significantly (p = 0.16). Only 3 hM4Di files remain, too few to test.

**Other outputs added**
- One session's annotated events, showing how the logs are parsed.
- The Key Resource Table and README search for sex, which finds nothing.
- The header cells of the instrumental-learning columns used.
- The DANDI `unit_name` values, which are just 0 to n-1.
- Which files are shared between the three experiment folders: only training logs and baseline sessions, no drug or washout sessions.
- Per mouse, the baseline sessions before the first drug session and their block-to-block variability, behind the note that the "stable baseline" reading picks mice that barely discount.
- The A77636 locomotion test on the 10 README-listed parkinsonian mice alone: p = 0.014.
- Rotarod Dunn's test corrected over all 10 pairs, and the striatal TH loss without the cohorts that have a single control.

New findings: a `paper_inconsistency` (the paper's oIPSC p < 0.01 cannot come from an exact signed-rank test on 6 cells), the duplicate H0/H0.4 file, and the identifier gap above.

**Not done, and why**
- **No questions file.** The verifier found no misreading of the claims file, so I did not create `questions/001177.yaml`.
- **figs1ef blocked reason:** it stays `other`, not the `data_missing` the verifier gave. The claim is marked as data held elsewhere, and the protocol says those claims are never blocked as `data_missing`. The notes say so.

Sources on Prism's comparison method: [Multiple comparisons after repeated measures one-way ANOVA](https://www.graphpad.com/guides/prism/latest/statistics/stat_multiple_comparisons_after_rep.htm), [Sphericity and compound symmetry](https://www.graphpad.com/guides/prism/latest/statistics/stat_sphericity_and_compound_symmet.htm)
