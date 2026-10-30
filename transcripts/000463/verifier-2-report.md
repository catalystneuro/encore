**Round 2 verification: 000463-gao-2025-01** (claims file `10.1523-jneurosci.2218-24.2025.yaml`, 37 claims; attempt record, 37 outcomes: 35 blocked, 1 not_reproduced, 1 partially_reproduced; 1 marked `assumed: true`)

In round 1 I worked from the 33-claim file for 000946. This round I checked everything against the supplied 37-claim file, which is the one the notebook was written for.

**1. Outcomes**

| claim(s) | outcome | agree? |
|---|---|---|
| fig4-unit-counts | blocked (metadata_insufficient) | Yes. This file's criterion compares 12 counts by type and has no clause on per-area totals. Cell 16's bound holds: RSU + FSU equals the untyped total, and the total is outside the joint range in all six groups. So at most 6 of the 12 counts can match. That rules out "reproduced", but whether the result is partial or not reproduced depends on the types. |
| fig4a, fig4b, fig4-post-3000, fig4-30hz-responses, fig4-fsu-no-change, fig6a (2), fig6b–d, fig7a–d, fig8a, fig8b (2), fig9a–b, fig10a (3), fig10b–f, fig11c (2), fig11d, synthesis-prf-pathway | blocked (metadata_insufficient) | Yes. Cell 9: all 22,599 `celltype_label` values are 0, 33 recordings have no such column, and the units tables hold only spike times. Cell 18: the one STTC file opened has no types. |
| fig5a-sham-no-response, fig5b-control-cg1-no-response | blocked (data_missing) | Yes. Cell 11: the voltage field is 5 V in all 813 identifiers that parse. The targets are only S1, M1 and POm, and the 14 files with no area name stimulate S1 or M1. Both claims would also need types. |
| methods-insitu-pressure | blocked (data_missing) | Yes. I did not review this one in round 1. Cells 3 and 7: 000463 holds only voltage recordings, and 000946 holds units and STTC files, with no hydrophone data. |
| fig11-ac-unit-counts | not_reproduced | Yes. Cell 22: 112, 138, 167, 127 and a total of 633, against 83, 107, 104, 100 and 453. That is 0 of 5 within tolerance, and also 0 of 5 under the all-PD reading (1111 to 1196 per PRF). No assumption is involved. |
| fig11b-ac-prf-responses | partially_reproduced, `assumed: true` | Yes. Under O2a (cell 25), both Kruskal-Wallis tests are significant, 6 of 6 named results hold, and 300 Hz is lowest in both windows. The exclusion fails because 4500 Hz responds during sonication under all six readings. That gives partial under this file's rule. The assumption is stated, in cell 30 and in the record's deviations, and I think it is reasonable. On the real data, O2b puts the unchanged −134 to −67 ms window at 54 to 66% (`pre2_b`, cell 25). On synthetic units with no effect, O2b gives 13 to 127% depending on firing rate, while O2a stays at 100 to 102% (cell 28). The paper's sham p = 1.0 assumes a scale where no change is 100%. The outcome also holds when any one subject is left out (cell 28) and with all PDs included (cell 29). It still overrides the header rule that disagreeing readings make a claim blocked, so it stands only until a reader answers whether O2b stays a reading. |

**2. Statements the printed numbers do not support**

- **Cell 30, and the fig11b notes in the record:** "30 Hz under four of the six". Cell 26 shows corrected p values for 30 Hz during sonication of 0.0062, 0.016, 0.048, 0.12, 0.0021 and 0.0053. That is three of six below 0.01 (O3a×2, O3c×2, O3c×5), and the significant_during column of cell 25 agrees.
- **Record, fig11b notes:** "corrected p 4.2e-5 to 0.009" for 4500 Hz during sonication. Cell 26 gives 1.7e-05, 4.2e-05, 0.0036, 0.009, 2.4e-06 and 5.9e-06, so the range is 2.4e-6 to 0.009.
- **Cell 30, and the record's fig11b deviation:** "responses of 106 to 159%". The paper text gives 123.34, 148.39, 158.75 and 141.68%, and no value of 106% appears in it. This describes the paper, not the notebook output.
- **Cell 31, Summary:** "most spike files are deposited twice under different file names and session start times". Cell 8 shows the start time differs in only 27 of 731 duplicate groups.
- **Record, fig11-ac-unit-counts notes:** "Counting the duplicate copies of 000946 would double them". No output counts the copies of the AC files.
- **Record, fig10 and fig11c/d notes:** "arrays are by lag, unit index, unit index, trial and window" and "for POm, M1 and AC against S1". Cell 18 prints 4-D shapes, e.g. (10, 499, 20, 9), and the file description lists five dimensions, so the dimension order is not established. Only one file was opened, an M1-vs-S1 file, so the POm and AC files are unverified. Neither point affects an outcome.
- **Record, first finding:** "500 trials per condition". Cell 9 shows 691 of 814 recordings with 500 trials and others with 400 to 499; cell 10 says so.

Everything else checks out against the outputs: the remaining sentences of cells 23 and 30, the Summary, the README, and the notes, including the 31 and 37 counts and the line "2 tested, 35 blocked".

**My round-1 reasons in the record:** they are given in my words for every claim except one. For fig11-ac-unit-counts the record shows `agrees: true`, with a reason quoted from my fig11b row. My round-1 file had no such claim and I gave no outcome for it, so I did not make that agreement. I agree with the outcome now (part 1), but the round-1 entry should not record an agreement I never gave.

**3. Round-1 points**

- **Resolved:**
  - B1 (wrong claims file): the mismatch was on my side.
  - B2, B4, B5, B6: judge() follows this file. Its partial rule, "lowest in both windows", O4a and O3c are all named here. The header rule is handled by an explicit assumption.
  - B3: the outcome stays blocked under this file's criterion, and the bound is added.
  - B7: confirmed, and used as the basis of the assumption.
  - B8: this file does not restrict fig11b to PD 200, and the all-PD variant gives the same outcome.
  - B9: leave-one-subject-out added; the outcome is stable.
  - B10: BH499_300_200 is excluded.
  - B11: no unsorted spike times in any loaded file.
  - Part C: voltage field, files with no area name, session breakdown, one STTC file and untyped pairs are all now shown.
- **Remaining that bears on a conclusion:** only one. fig11b-ac-prf-responses rests on O2a while the reader's answer on whether O2b stays a reading is pending. If O2b is kept, the header rule makes the claim blocked (methods_underspecified).
- **Remaining that bears on no conclusion:** the wording errors in part 2, and the round-1 attribution for fig11-ac-unit-counts.
