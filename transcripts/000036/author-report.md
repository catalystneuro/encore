I've done steps 1 to 6 for DANDI:000036. The clean-environment `entry.py all` run passed, `entry.py check` and the claims checker report no problems, and the handover is in `executed/000036-mayner-2022/handover/`. Nothing is committed.

## 1. Outcomes (27 claims, including the link claim I added)

| Claim | Outcome |
|---|---|
| session-link (added) | reproduced |
| design-sessions | partially reproduced |
| ext1-2-cell-counts | reproduced |
| fig3a-layer-specific | reproduced |
| fig3b-area-specific | reproduced |
| ext3-1-natural-artificial | reproduced |
| ext3-2-sensitivity | not reproduced |
| table1-permutation | reproduced |
| fig4-locomotion-effect-size | reproduced |
| discussion-session-effect-sizes | partially reproduced |
| fig5-multivariate-layer / -area | reproduced / reproduced |
| fig6-category-decoding, ext6-1-identity-decoding | reproduced / reproduced |
| fig7-stimulus-effect, fig7-snake-highest | reproduced / reproduced |
| fig8-nd-sd-correlation, fig8-no-sd-relation-controlled | reproduced / reproduced |
| ext8-1-no-low-level-relation | blocked: methods_underspecified (its own readings disagree) |
| fig4-pupil-effect-size | blocked: methods_underspecified (also data_missing) |
| ext1-3, ext3-8, ext3-9, ext5-1, mediation-event-magnitude | blocked: not_runnable (L0 events) |
| ext3-5-arousal-covariates, ext7-1-arousal-mediation | blocked: data_missing (pupil diameter) |

Totals: 15 reproduced, 2 partial, 1 not reproduced, 9 blocked.

- **ext3-2 (not reproduced):** 36 of 108 parameter sets agree under the claims file's rule. The same rule applied to the paper's own `stats.parquet` gives 28 of 108, so the gap is between the rule and the paper's "nearly all", not the data.
- **fig3b:** the AM effect size is 0.132 against the paper's printed 0.268. The paper's code prints 0.128, so 0.268 looks like a transcription slip in the paper. The outcome follows the criterion's significance rule, which holds.
- **discussion-session-effect-sizes:** the largest per-session d is 1.111 against 1.25. The paper's 1.25 comes from a code output file that disagrees with its own per-trial table, which gives 1.155.

## 2. What was found about the dataset; questions

- **Extra sessions:** it holds 57 sessions where the paper has 45. There are 12 extra ones, plus the excluded L5 AL session, which was imaged at half the frame rate. Nothing marks which sessions the paper used.
- **Linking:** the NWB `identifier` is not the paper's session id. Sessions link only by start time, and `session_start_time` is exactly 7 hours later than the paper's (it looks like UTC labelled -07:00). With that link, all 44 match, and the dF/F is identical to the paper's.
- **Timing:** the stimulus and running timestamps drift against the 2p frame times by up to 4.4 frames (146 ms) by the end of a session, compared with the paper's alignment.
- **Running:** the running series has a spurious first sample; the rest equal the paper's deposit shifted by one. dF/F timestamps have one entry more than the data in 39 files. The stated imaging rate is 30.0 Hz; the actual rate is 30.15 Hz.
- **ROIs:** 15 ROIs are NaN at every frame, with no flag. Without them the cell counts equal the paper's exactly.
- **Missing:** no L0 events, no eye tracking or pupil, and no sex, age or date of birth.

No questions were asked: every method detail I needed was in the claims file or its stated readings.

## 3. Protocol gaps

1. The dandiset holds more sessions than the paper, which the design-sessions criterion did not anticipate. I judged it partial and recorded why.
2. `with_labels` is defined for code names; I used it for the paper's session selection, since that brings in no measurements.
3. The link-claim criterion was written after I had found the 7-hour offset while exploring; the protocol does not say when a link criterion must be fixed. Recorded as a deviation.
4. An expected value can fall outside tolerance while the criterion's rule holds (the fig3b AM value). I let the criterion decide, as the protocol says, and wrote the mismatch in the notes.
5. The Zenodo deposit is one gzip tar, readable only in order; the running parameters arrive after 17 to 21 minutes. I streamed it in a background thread with a 26-minute deadline, so one reading's availability can depend on network speed.
6. When one reading's input is not public and the computable readings already disagree (pupil), the protocol does not say which block reason comes first. I used methods_underspecified and put data_missing in the notes.
7. The discussion claim's criterion has no partial rule; I used partial and recorded it.
8. The protocol does not cover a claims-file reading that the paper's own outputs fail (ext3-2). I recorded not_reproduced with the paper-output reference.
9. The protocol does not say who sets each claim's `data` field. I added `data` and `depends_on: session-link` to the reader's claims.
10. The event criteria name the L0 detector run on the dataset's dF/F, which cannot be installed. The paper's own events are public on Zenodo, but I did not use them, since the criteria do not name them.
11. After the final run I edited one drift sentence in the markdown of both the committed and executed notebooks (text only, outputs untouched). The protocol and tool do not say whether that needs a re-run.

## 4. Runtime and failures

- The session took about 3.5 hours. The final entry run took 44 minutes: 12, 12 and 20 minutes for the three notebooks.
- **Fixed during development:**
  - The lbfgs optimiser returned degenerate fits with infinite likelihood. That gave a NaN chi2 for ext3-1 and changed the sensitivity count from 33 to 36 agreeing sets. Now lbfgs and bfgs are compared and non-finite fits rejected.
  - An off-by-one in running samples broke the first arousal run.
  - A data-check cell failed on the half-rate session.
- **Not mine:** `git status` shows untracked `.bashrc`, `.idea`, `scripts` and similar. They are `/dev/null` devices mounted by the sandbox, and I left them alone.
