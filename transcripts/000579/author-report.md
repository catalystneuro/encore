I worked through steps 1 to 6 of the protocol for DANDI:000579, pinned at version 0.230728.1727. Of the 43 claims, 11 were tested and 32 are blocked. The entry passes `tools/entry.py all` (0 errors), the notebook runs in 8.5 min, and the handover package is in `executed/000579-tseng-2022/handover/`. Nothing is committed.

**Version.** 0.230728.1727 is the only published version; the paper cites none and the draft has the same 308 assets. The notebook header says so.

**Session selection.** Several outcomes depend on how a session's fraction correct is computed (above 0.65 counts as a good session). The Methods say visually guided trials are excluded from all analyses; I call that reading a. Counting all trials is reading b. Only reading b comes near the paper's counts, so I adopted it as an assumption, and every analysis shows both.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| neuron-counts | reproduced, rests on an assumption (reading b: 150 sessions, 97,989 neurons, all six area counts within 10%; reading a fails) |
| fig1d-switch-performance | reproduced (fitted performance 0.226 just after a switch, 0.727 at block end, p < 1e-4) |
| lstm-choice-accuracy | reproduced, rests on an assumption that the stored predictions are held out (0.772) |
| figs1h-lstm-beats-rl | reproduced (RL model 4 refit; Wilcoxon p = 4.65e-22) |
| fig1i-strategy-after-switch | reproduced |
| visually-guided-rule-update | not reproduced, rests on an assumption about how a trial's update is defined (see 2) |
| fig1l, fig1m, figs1m (photoinhibition) | blocked, data_missing |
| fig2c-running-variability-after-switch | reproduced |
| fig2f-latency-strategy | reproduced, rests on the session selection (under reading a, one test gives p = 0.058) |
| fig2g-choice-commitment | reproduced |
| cue-biased-running-uncorrelated | partially reproduced (per-mouse slopes show no relation; the pooled correlation is r = 0.22, p = 0.0005) |
| fig4h-activity-by-epoch | partially reproduced (the feedback-period part holds; inside RSC the arm is more active than the stem) |
| 24 claims that need the GLM fits | blocked, too_large (about 550 CPU hours, lower bound) |
| 5 claims that need the population decoders | blocked, too_large (about 9 CPU hours, lower bound) |

The two too_large estimates come from timing one fit of each kind on random data of the real size. The GLM figure varies a little between runs (536 to 583).

### 2. Dataset findings, assumptions, questions

**What the dataset holds.**
- **Matches the paper:** 300 sessions from 8 mice and 278,155 neurons, exactly the paper's total, with an area label on every neuron.
- **Already computed:** the paper's behavioral LSTM outputs and the dynamic-choice and cue-biased-running outputs are stored in each file.
- **Missing:** the photoinhibition sessions, and all GLM fits, encoding strengths and decoders. The missing derived results are what 29 of the 43 claims need.

**Findings recorded in the attempt.**
- **Sign error:** the stored `rule_belief` is P(rule A) − P(rule B) in all 300 sessions. The Methods and the dataset's tutorial both say positive means rule B.
- **Session counts:** the paper's 253, 216 and 141 sessions cannot be recovered from the files. Reading a gives 291, 154 and 100; reading b gives 297, 238 and 150.
- **Visually guided trials:** the median session has 23% of them, and 222 of 300 sessions have more than 20%. The paper says the fraction was typically 0 to 20%.
- **Maze length:** 7 sessions have a 1.5 m maze stem instead of 2.0 m.

**Assumptions.**
- Sessions are selected on fraction correct over all trials (reading b).
- The stored LSTM predictions are held-out predictions.
- A trial's rule update is the change in rule belief from trial t to t+1, since the LSTM's belief on a trial depends only on earlier trials.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- How was the rule update per trial defined? Taking it from t to t+1 gives a significant difference between visually guided and normal trials; from t−1 to t gives none. Both give values 2 to 5 times the reported ones.
- Was the 65% session threshold computed over all trials?

**Questions to a reader:** none.

### 3. Where the protocol was unclear

1. **Session selection is not a reading.** It is not listed as a reading in the claims file, yet it decides several outcomes. I treated it as an open detail under step 1.6 and adopted the reading consistent with the paper's own counts.
2. **No rule when the paper's text and its numbers point to different methods.** Here the Methods text favors reading a and the reported counts favor reading b. I adopted the counts-consistent reading and recorded the conflict as a finding and a question.
3. **Datasets that store model outputs.** The files already hold the paper's LSTM outputs, and the protocol does not say whether to use them or refit. I used them, said so in deviations, and refit only the RL model, which the files do not hold.
4. **Timing for too_large estimates.** "Time the subset" assumes the analysis is already implemented. For the GLM and decoders I timed one fit of each kind on random data of the real size, shown in the notebook as a lower bound.
5. **A claims-file reading that cannot be run.** The criterion for fig4h requires both neuron readings, but the well-fit reading depends on blocked claims. I ran the all-neuron reading only and said so in a deviation.
6. **Two readings in a criterion that disagree.** For cue-biased-running-uncorrelated the criterion only says "mixed results are reported as such", without an outcome. I recorded it as partially reproduced.
7. **Several claims share one notebook cell.** Tagging that cell with all three photoinhibition claim tags passes `check`; the protocol does not say whether this is intended.

### 4. Runtime and failures

- **Runtime:** the run took 23:19 to 01:20 UTC, about 2 h. The final notebook takes 8.5 min, most of it streaming 300 files and the 238 RL refits.
- **Failures:**
  - The first survey with threads took 38 min, because h5py reads one file at a time within a process. I switched to separate processes.
  - The first RL fits got stuck at a degenerate solution; adding better starting points fixed them.
  - No streaming errors.
- **Not mine:** untracked dotfiles (`.bashrc`, `.idea`, `scripts`, and others) appeared in the repo root. I left them untouched.
