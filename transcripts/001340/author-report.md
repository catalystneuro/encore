I've completed steps 1 to 6: the entry is locked, checked and run, the attempt record is written, and the handover package is built. All 39 claims were tested and none is blocked. Many dopamine outcomes rest on one stated assumption about which sessions to use, explained below. Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| data-composition | partially reproduced |
| perf-after-pretraining, fig1f-performance-increase, trials-to-switch, trials-to-commit, figs1-switch-measures-decrease, fig1e-stay-after-omission, figs6a-decaying-history-weights | reproduced |
| fig2c-bayesian-beat-rl4p, fig2c-complex-rl-beat-rl4p, fig2c-rlcf, fig2c-no-bayes-vs-complex-rl, fig2b-model-identifiability, brlfw-alpha-zero, rl4p-learning-rates, fig2f-adaptation-after-switch, fig3a-both-port-contexts, fig3c-aic-around-switch, fig4i-model-runchosen | reproduced |
| figs2-parameter-recovery, fig3b-sse | partially reproduced |
| figs7-no-change-across-sessions | not reproduced |
| figs8-brlwrp-no-difference | not reproduced (assumed) |
| fig4bc-switch-effect, fig4bc-no-laterality, figs3-other-metrics, fig4g-history-decrease, fig4h-nonnegative-rpe-aaa, fig4i-lmer-switch, fig4j-lmer-stay, figs5-per-animal, reward-switch-reward-count, figs4-lmer-feature-sets | reproduced (assumed) |
| fig4bc-reward-omission, fig4de-port-duration, trial-cleaning-counts, fig4f-bayesian-rpe-fit, fig4-consistent-after-reward | partially reproduced (assumed) |
| fig4h-rpe-only-llk | not reproduced (assumed) |

The model fits closely match the paper. For example, the AIC of BIfp relative to RL4p is -535.4 here against the paper's -536.6, and RL4p's learning rates are 0.848 and 0.731 against 0.85 and 0.73.

## 2. The dataset, assumptions and questions

**Version:** 0.250221.0527 is the only published version, and the paper cites none.

**What the data show:**
- There are 69 sessions, not 70: mouse BSD017 has 13, with days 165 and 166 missing.
- The files do not mark the paper's 34 sessions with valid dopamine, and they hold only the raw 470 and 415 nm signals.
- 8 of BSD011's 14 photometry sessions show no response to reward at any clock offset up to ±400 s. Two of them are sampled at 30.5 Hz; the rest of the data is at 20.4 Hz.
- Two BSD016 photometry files hold only 30 and 40 samples, with timestamps that are not on the session clock.
- Metadata errors:
  - The fiber coordinates are the same for left and right hemisphere sessions.
  - The indicator is described as a calcium indicator, and the filter wavelengths are -1.
  - Every trial's `stop_time` is the session end.
- BSD011 was recorded in every session, not on the left, right, no-recording cycle the Methods describe.
- `related_publications` names the bioRxiv preprint, not the published paper.
- In the paper, the printed RU and UR counts are swapped relative to its own test, and the reward coefficient is printed as -1.6345 with a positive interval.
- The data favour the code's RLFQ3p forgetting rule over the Methods' rule: the code's rule gives the paper's AIC, the Methods' rule does not.

**Assumptions:**
- **Session set.** The claims file reads the AUC selection rule in a way that keeps no session: every AUC is 0.46 to 0.51. I used the 38 sessions that show an outcome response, and ran all 46 usable sessions as a variant where the claim's readings allow. This choice yields exactly the paper's 94 reward-switch-reward trials.
- **Laterality test.** For fig4bc-no-laterality I used all trials, not the cleaned ones. On all trials p = 0.23; on cleaned trials p = 0.0003.
- **Feature-set coding.** For figs4-lmer-feature-sets I coded each past choice relative to the current choice.
- **Preprocessing.** The paper does not give the robust regression's loss, so I used a Huber regression, with the airPLS settings from the cited Martianova et al. 2019 procedure.

**Questions for the paper's authors**, recorded as `methods_unavailable` findings:
- Which 34 sessions were kept, and how was the AUC computed?
- Which trials does the four-factor OLS use?
- How is the past choice coded in the S4 Fig feature set?
- Which trials and aggregation give the Fig 4H log-likelihoods near -986?

**Questions to a reader:** none.

## 3. Where the protocol was unclear

1. The claims file's reading of the session selection keeps no session, and the protocol does not cover a selection rule that turns out unusable. I adopted a best-supported set as an assumption and marked every dopamine outcome `assumed`.
2. For an absence claim the protocol says the several-readings rule does not apply, but the fig4bc-no-laterality criterion lists readings itself. I resolved it under step 1.6 with a stated assumption.
3. `measured` says which reading to record when several match, not when none does (fig3b, fig4f, fig4h-rpe-only). I recorded the closest or first reading and said so in the notes.
4. The protocol does not say whether the paper's code may be re-implemented for speed; its code is about 1000 times slower here. I re-implemented the models and the notebook shows they give the code's own likelihood to within 5e-11.
5. Dependency rules only cover blocked claims. figs8 depends on fig4f, which is partially reproduced; I tested figs8 anyway and noted the dependency.
6. The per-section random generator rule does not fit numba's global random state. Each simulation is seeded explicitly instead.
7. The prompt gives the harness as "Claude Code"; the example record uses "Claude Code (GitHub Actions)". I followed the prompt.
8. The sandbox left device-file placeholders (`.bashrc`, `scripts` and others) as untracked files at the repository root. I did not touch them; the workflow should not commit them.

## 4. Runtime

The run took about 1 h 16 min, from 02:42 to about 03:58 UTC. The notebook takes 9.3 min in the clean environment, including about 4 min of simulations run in 4 processes. The last full run passed with 0 check errors. Nothing failed; the only problems during development were a singular matrix and a wrong sign in one t-test table, both fixed before the final run.

Files are in `entries/001340-qu-2025/`:
- `reproduce_qu_2025.ipynb`
- `qu2025.py`
- `entry.yaml`
- `README.md`
- `requirements.in`
- `requirements.lock.txt`

The record is `attempts/001340-qu-2025-01.yaml`.
