I've written the reconciliation block in `attempts/petersen-2020-02.yaml`. I added six findings marked `found: on_prompt` (13 to 18) and the new notebook `entries/petersen-2020/earlier_findings.ipynb`, which is listed in `entry.yaml`. The entry check reports 0 errors. Both notebooks then ran from a clean environment and passed: `earlier_findings.ipynb` in 130 s and `reproduce_petersen_2020.ipynb` in 2782 s. Nothing is committed.

**(1) Blind: yes.** `tools/blind.sh audit` found 5 lines. One matters: in the author-answers run, a `find` listing showed the path `./summaries/petersen-2020-01.md`. No transcript opens that file or anything else from the earlier attempt. The other hits are the repository's own text (the README, the dashboard URL, the author-responses doc) and a word in the author's own code.

**(2) Earlier findings on 0.261115.0311**

| # | Earlier finding | Status | Now |
|---|---|---|---|
| 1 | MS10 and 2018-07-19 temperature not a recording | partly_fixed | 3 |
| 2 | 2018-07-19 sessions labelled as cooled | partly_fixed | 2 |
| 3 | Six of the paper's sessions missing | partly_fixed (MS12-170715 added; five still missing) | 13 |
| 4 | MS21-180627 and MS21-180712 unusable | fixed | |
| 5 | No cell types, place fields or electrode locations | partly_fixed (14 files still all 'unknown'; no place fields) | 4 |
| 6 | 'Cooling off' state undescribed | fixed | |
| 7 | Sessions with only 'unsorted' units | partly_fixed (2 of 7 left) | 4 |
| 8 | No spatial information in the two 180621 sessions | still_present | 14 |
| 9 | Sessions outside the paper's analysis not marked | partly_fixed | 15 |
| 10 | No trials table in version 0.210812.1514 | not_checked (about an earlier version that cannot change) | |
| 11 | MS10 tracked below 120 Hz | still_present | 16 |
| 12 | Figure 5H P value impossible with N = 10 | still_present | 17 |
| 13 | 12% in the Discussion against 8.4 to 7.7 Hz in the Results | still_present | 18 |

**(3) New findings:** 1, 5, 6, 8, 9, 10, 11 and 12.

**(4) Outcomes that changed (14 claims)**
- **Claims file change.** The claims file was rewritten on 2026-11-15. It dropped the session lists and thresholds taken from the first author's unlinked code, and it fixed some measures.
  - session-structure (reproduced → partially_reproduced): the code's session list is gone, so MS10-170307 with 37 trials is now included.
  - disc-theta-frequency-12-percent (partially_reproduced → reproduced): reading (c) is now the largest decrease of the aligned mean series.
  - suppl2d-interneuron-oscillation-slows (reproduced → partially_reproduced): the claim now carries the 14% of Figure S2D.
  - fig4gh-fp-speed (reproduced → partially_reproduced): the main speed bins are now 10 cm/s.
  - fig5cg-compression (not_reproduced → blocked): the claim now requires the paper's surface fit, which failed on this data.
- **Power measure.** The earlier attempt used the code's spectrogram power; the blind one uses Hilbert or spectral-peak power.
  - fig2h-theta-power-temperature: not_reproduced → reproduced
  - fig2i-theta-pre-cooling-post: partially_reproduced → reproduced
  - fig6h-errors-theta-power: partially_reproduced → reproduced
- **Averaging.** fig2g-theta-freq-temperature (reproduced → partially_reproduced): the blind attempt averages more trials per point (R = 0.978, above tolerance). It also uses 31 measured sessions where the earlier one used 37, because the new version marks 11 more series as modelled.
- **Field and size definitions.**
  - fig3c-field-size-correlated: reproduced → not_reproduced
  - fig3e-model-field-size: partially_reproduced → not_reproduced
- **Sessions and pairs.** The new version adds curated units, so the blind attempt has more sessions with place cell pairs.
  - fig5-speed-control-cooling (not_reproduced → reproduced): 23 sessions against 15.
  - fig5h-time-lags-increase (reproduced → partially_reproduced): with 8506 pairs, pre and post also differ (P = 0.034).
  - fig5i-phase-lags-unchanged (not_reproduced → reproduced): no change with 8451 pairs. The blind attempt's other lag reading does show a change, so this outcome depends on how the lag is read.

**(5) What did not fit**
- `docs/pilot-notes.md` has no section for pilot-11 or pilot-15, so the `protocol` note covers only pilot-8, 9, 10, 12, 13 and 14.
- The repository is a shallow clone with one commit, so `git show $c:entries/petersen-2020/...` could not find the earlier entry. I used the copy the workflow placed in `earlier-entry/` instead; it is pinned to 0.250624.0444.
- The release notes say only MS10 and MS12-170715 have a modelled temperature, but the files hold 20 modelled series.
- For findings 3 and 9, which the blind attempt did not report and which proved only partly fixed, I used `partly_fixed` with an on_prompt finding. The prompt lists only fixed, still_present and not_checked for that case.
- The main notebook took 46 minutes, against the 30 that `entry.yaml` gives for it. I left that entry alone since it belongs to the blind attempt.
