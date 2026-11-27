I did steps 1 to 6 for jarzebowski-2026. All 31 claims were tested and none is blocked: 21 reproduced, 3 partially reproduced and 7 not reproduced. The final `python tools/entry.py all` passed, with the notebook running in 740 s, and the handover is built in `executed/jarzebowski-2026/handover/`. I did not verify my own work and committed nothing.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| model-positive-error-short-latency | partially reproduced, depends on the seed: 1 of 81 spikes falls after the basket peak under the claim's seed |
| model-negative-error-delayed-release | reproduced (17.4 ms) |
| fig2a-weak-sensory-silenced | not reproduced: about 0.9 spikes per run, not silence |
| fig2b, fig2c, fig2d, fig3a, fig4a, fig4cd, fig4d, fig4ef | reproduced |
| fig3b-gain-lowers-burst-threshold | partially reproduced, depends on the seed |
| fig3c-gain-keeps-release-delay | not reproduced: no release spikes at Low gain, 1 of 80 runs at Mid |
| fig4b-chc-reduction-shortens-latency | reproduced, resting on an assumption |
| ccf-layer-link (link claim I added) | reproduced: 7996 of 7997 units with coordinates fall in a VISp layer |
| cell-counts | not reproduced over all sessions; within tolerance over the 104 sessions of optotagged mice |
| fig5c (×3), fig5d, figs1 (×3), figs2 correlation, fig7a | reproduced |
| fig7c-running-leaves-omission-bursting | reproduced, resting on an assumption |
| fig6b, fig6c | not reproduced, resting on an assumption (which spontaneous block) |
| figs2-l5-bursting-not-predicted-by-rate | not reproduced: L5 rate strongly predicts L5 FSB |
| fig7b | partially reproduced: the L5 value is above tolerance |
| fig7d | not reproduced: no L5 effect |

## 2. Dataset, assumptions and questions

**Dataset.** I pinned version 0.240702.1725, the one the Methods cite and the only published version. It holds 153 sessions from 81 mice. The files give no layer for any unit, so layers come from the Allen CCFv3 10 µm annotation volume via each unit's coordinates. Problems found:
- 351 VISp units in 7 sessions have coordinates (0, 0, 0), so they get no layer.
- The unit and electrode columns have no descriptions.
- The spontaneous block right after the task lasts only 10 s; a 289 s block comes later. In one session the 10 s block starts 3277 s after the task ends.
- The clock check (images against omissions, 30 to 100 ms after onset) separates them clearly in most sessions. It does not establish a shared clock in 10 sessions (AUC below 0.8) or in 2 sessions with no usable VISp unit.
- No recording was deposited twice.

**Assumptions**, each recorded in the attempt with every reading shown:
- **Spontaneous period (fig6b, fig6c):** I took the 10 s block, the literal reading of "immediately following the task". The 289 s block would make both claims partially reproduced.
- **Cell selection for Figures 7C and 7D:** I used the rule whose counts are closer to the paper's. Neither rule matches them.
- **fig4b:** I read "L4 threshold" as the breakthrough threshold.

Six findings ask the paper's authors about open methods: which sessions were used, which spontaneous block, how FSB is pooled, the selection for Figures 7C and 7D, and the model's input onsets and ranges.

**Question to a reader** (in `questions/jarzebowski-2026.yaml`): cell-counts says "all sessions". The Methods may instead limit the analysis to the optotagged mice, which is the only selection that matches the paper's counts.

## 3. Where the protocol was unclear or did not fit

1. Inputs must have "a DOI, or a repository at a commit", but the CCF annotation has neither. I recorded its URL with a SHA-256 that the notebook checks, plus the DOI of the paper that describes the annotation.
2. A claim of absence (fig7c) also had open cell-selection readings that give different outcomes. The protocol says absence is judged on the paper's test alone; it does not say how to handle open selection readings. I followed the criterion's own wording and let the counts pick the reading, marked as an assumption.
3. The claims for the model figures are `data: elsewhere`, but the "data" is the paper's Methods, not an archive deposit. I listed the Methods as an input, cited by the paper's DOI.
4. A mixed model with one value per session (figs2 reading b) cannot be fitted. I used the one-sample t test it reduces to, as a deviation.
5. Adding `depends_on: ccf-layer-link` to cell-counts touches a claim, though not its statement, expected values or criterion. The protocol requires it for link claims but does not say this edit is allowed.
6. The step 2 clock check assumes the response falls within the analysis window. A 250 ms count missed transient responses in about 25 sessions. I added a 30 to 100 ms window.

## 4. Runtime and failures

- About 1 h 25 min from start to handover (14:06 to 15:30 UTC).
- The notebook takes about 12 min: 6 for streaming, 6 for analysis. Peak memory was 3.5 GB.
- Nothing failed. Some mixed models report non-convergence; this is shown in a `converged` column and decides no outcome.
- `git status` lists untracked dotfiles (`.bashrc`, `.idea` and others) and a `scripts` directory. I did not create the dotfiles, and `scripts` was already present when the run started. They should not be committed.
