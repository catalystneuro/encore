All five author steps and the handover are done. The entry ran cleanly from a fresh environment in 142 s; the whole session took about 30 minutes by the clock.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| include-list-link (a link claim I added) | reproduced |
| data-units-sessions | reproduced (42/32 Oz, 63/51 Ci) |
| fig2-row1 to row6 | all six reproduced |
| cross-epoch-no-reliable-relation | reproduced |
| range-baseline-pupil-evoked-lc | reproduced |
| range-baseline-lc-evoked-pupil | not reproduced (Oz rho -0.04 under E1 and -0.13 under E2, against the paper's -0.33) |
| figs1-raw-baselines-similar | partially reproduced (11 of 12 cells match; row 6 Ci gives p = 0.14) |
| figs2-llr-pupil-baseline-evoked | reproduced under E1 (6/32, 7/51) |
| figs2-llr-lc-baseline-evoked | reproduced (3/42, 4/63) |
| figs2-llr-cross-epoch | not reproduced (5/42 and 6/63 against 4/42 and 4/63) |
| fig3-pooled-within-epoch | reproduced |
| fig3-pooled-cross-epoch-null | reproduced |

No claim is blocked and none rests on an assumption.

## 2. Dataset, assumptions and questions

**Version.** I pinned 0.261019.2146. It is the only published version, and the paper's code README names it.

**Contents.** The dataset holds exactly the paper's 83 sessions and 105 units, the same set as the code's include lists, with no duplicated recordings.

**Code check.** I rewrote the paper's code pipeline in Python as a variant. Run on the dandiset, it matches all 26 values the code printed. Under that code reading, the paper's numbers come out for all three claims that fail or partly fail under the Methods' measures.

**Findings recorded in the attempt:**
- **The code removes two units twice.** Its include list already lacks legacy units 43 and 65. The code then drops rows 43 and 65 of its own table, which removes two more Ci units. That explains the 61 units and 50 sessions in its output, against the paper's 63 and 51.
- **Figure 3 z-scoring.** The code z-scores firing rates by the unit's position within its session, pooled across all sessions, not per unit as the legend says. The conclusions are the same either way.
- **Evoked pupil and trial rule differ between code and Methods.** The code measures the evoked pupil over 0 to 800 ms after the beep, where the Methods go to 20 ms before the end of fixation. Its trial rule also keeps beeps near or after the end of the trial. This decides the two not-reproduced claims, and it is recorded as the question for the paper's authors.
- **Undocumented metadata.** The pupil trace looks already preprocessed (z-scored, mean trace removed, smoothed), but the file does not say so. `trial_time_index` has no unit. The files do not say what event marks the trial start. Spike times are anchored to artificial trial starts 100 s apart. Every trial is marked correct.
- **Beep and trial timing do not match the Methods.**
  - Beeps fall 1.0 to 2.8 s after the trial start, against the Methods' 1 to 1.5 s.
  - 8 beeps fall before the trial start and 83 after its end.
  - Many fixation-only trials last under 1 s, against the Methods' 1 to 5 s.
- **Stimulation session.** The session named FixnStim has no stimulation marker, so stimulated trials cannot be told apart.
- **Paper inconsistencies.** The paper names a "rank-sum" test for a one-sample hypothesis. It also takes the range "per session" where the code takes it per unit.

**Assumption.** I treat the trial start as fixation onset, as the code does. This is recorded as a deviation, not marked `assumed`, because it is the authors' own reading of their data.

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. **Selection lists from the paper's code.** The protocol does not say whether an include list from the code needs a link claim. I added `include-list-link` (data `with_inputs`), which also checks the code's printed statistics, and added `depends_on` to data-units-sessions. Adding `depends_on` to an existing claim is not clearly allowed; I judged it not to be a change of statement, values or criterion.
2. **Methods against code.** The protocol has no rule for when the Methods and the code disagree and only the code gives the paper's numbers. Following the claims file, I let the Methods decide, showed the code as a variant, and put the question for the authors in a `code_mismatch` finding. A `methods_unavailable` finding did not fit, since the paper is not silent.
3. **A requirement implied by the Methods.** The Methods' window needs at least one 50 ms window before the end of fixation. I stated this as taken from that passage, not as an assumption.
4. **The code's printed output.** It is not clear whether this may be used as a reference value. I fetched it at the pinned commit, listed it under `inputs`, and used it only in the link claim.

## 4. Runtime and failures

The notebook takes about 2.5 minutes, of which about 70 s is streaming the 83 files. Nothing failed. `entry.py check` reported 0 errors and `claims_check` 0 problems. The handover is in `executed/002034-thompson-2026/handover/`.

The repository root has untracked files I did not create (`.bashrc`, `.profile`, `.idea`, `.mcp.json` and others, which look like sandbox leftovers). I left them alone; they should not be committed.
