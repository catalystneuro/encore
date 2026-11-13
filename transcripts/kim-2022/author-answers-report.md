There were no reader questions to act on, so I changed no outcome, notebook, conclusion or claim note.

**Questions:** `questions/kim-2022.yaml` doesn't exist, and nothing in the repository ever created it. The reader's answer run says the same in `transcripts/kim-2022/answer-report.md`: it found nothing to answer and left `claims/kim-2022.yaml` unchanged. My earlier author run had filed no reader questions. Its two open method points went to the paper's authors as `methods_unavailable` findings, not to a reader:
- how the ROIs were placed along bb', and whether the t-test was paired;
- how the cathode- and anode-facing pole regions were drawn.

**What each answer changed and the outcomes:** with no answers, every outcome is the same as before.

| Claim | Earlier outcome | Now |
|---|---|---|
| fig2a-uptake-rises-with-field | reproduced (assumed) | unchanged |
| fig2a-vertical-scales | not reproduced | unchanged |
| fig2b-exponential-same-slope | partially reproduced | unchanged |
| fig2c-max-inhibition-50-75 | partially reproduced | unchanged |
| fig2c-inhibition-flat-above-8-7 | reproduced | unchanged |
| fig2c-weaker-at-6-7 | reproduced (assumed) | unchanged |
| fig7-unipolar-pole-polarization | reproduced (assumed) | unchanged |
| fig7-charging-time-constant | not reproduced | unchanged |
| fig7-later-pulses-same-tau-difference | partially reproduced | unchanged |
| fig7-bipolar-overshoot | reproduced | unchanged |
| fig7-bipolar-alternation | reproduced | unchanged |
| fig7-summation-without-buildup | reproduced | unchanged |
| Figs. 3 to 6 (12 claims) | blocked, dataset_missing | unchanged |
| fig1e-heating | blocked, data_missing | unchanged |

**Entry runs:**
- `lock` rewrote `entries/kim-2022/requirements.lock.txt` (Python 3.13, with hashes).
- `all` passed with 0 errors, and the notebook ran in 461 s.
- I checked the executed copy against the record. For example, 75% mean plus s.e.m. is 339 a.u., and the pooled Fig. 7 fit gives a charging tau of 191 ns and a discharge tau of 612.8 ns (recorded as 613).
- `handover` built `executed/kim-2022/handover/` with the notebook, `kim2022.py` and the claims file.

Nothing was verified by me, committed or pushed.
