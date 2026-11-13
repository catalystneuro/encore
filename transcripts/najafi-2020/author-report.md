I finished steps 1 to 5 and ran the handover (step 6). All three notebooks ran from a clean environment through `tools/entry.py all`, `check` reports 0 errors, and nothing is committed. Of 38 claims, 11 are reproduced (3 resting on an assumption), 10 partially reproduced, 5 not reproduced and 12 blocked.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| data-composition | reproduced |
| fig1b-psychometric | reproduced |
| figs1b-trial-history | blocked, data_missing (no inter-trial intervals in the files) |
| fig1gi-inferred-spiking-differs | partially reproduced |
| fig2a-example-session | not reproduced (median 11.5 E and 1 I selective, expected 24 and 5) |
| fig2bc-fraction-selective-similar | not reproduced (medians within tolerance, but mouse 2 also differs, p = 0.040) |
| fig2bd-selectivity-time-course | reproduced, on an assumption |
| fig2de-selectivity-magnitude-similar | partially reproduced (mouse 4 differs) |
| figs3d-same-spiking-selectivity | reproduced |
| figs3c-wider-window | partially reproduced (inhibitory count per session at the tolerance bound) |
| figs3e-correct-error-correlation | partially reproduced |
| fig3bc-decoding-similar | reproduced |
| fig3b-decoding-time-course | partially reproduced |
| fig3df-weights-similar | reproduced (pooled counts 42019 and 5172, exactly as expected) |
| fig3hi-mixed-no-advantage | reproduced |
| figs5-fluorescence-decoding | blocked, data_missing |
| figs6ab-previous-choice-stimulus, figs6c-outcome-decoding | blocked, other (not reached in the time) |
| figs6de-incorrect-trials | partially reproduced |
| fig4bd-stability-similar | reproduced |
| figs7c-angle-stability | blocked, too_large (estimated 7 to 8 CPU hours) |
| fig5a-nonselective-model, fig5bc-selective-models-match, figs9-signal-selective-best | blocked, other (simulations, not reached in the time) |
| fig6a-same-selectivity-correlations | reproduced |
| fig6bc-inhibitory-correlations-higher | reproduced, on an assumption (mouse 1 has exactly the expected 11867 E and 1583 I neurons) |
| fig7-noise-correlations-limit-decoding | reproduced, on an assumption |
| fig8ab-learning-accuracy, fig8ce-choice-signal-onset | not reproduced |
| fig8de-learning-parallel | partially reproduced, on an assumption |
| figs13c-equal-trials, figs13ab-pseudo-learning, fig8f-correlations-decrease | partially reproduced |
| fig8g-fraction-selective-triples | not reproduced |
| figs12-licking-running | blocked, metadata_insufficient (the lick spout is not identified) |
| figs2-temporal-dynamics-similar | blocked, other (not reached in the time) |
| figs14-neuropil, figs15-labeling-specificity | blocked, data_missing |

## 2. Dataset, assumptions and questions

**Dataset.** I pinned version 0.260915.2309, the only published version; the paper cites none.
- **What matches the paper:** session counts (45, 48, 7, 35), the median trials per session (213, 253, 264, 222, exactly the paper's) and the neurons per session (477, 330 excitatory, 41 inhibitory). No recording is deposited twice.
- **Inferred spiking under a wrong name:** the traces are named `dFoF_*` (typed as Delta F/F), but they hold the normalised inferred spiking activity. There is no fluorescence trace in the files.
- **No ITIs:** trial times are relative to each trial, so inter-trial intervals cannot be computed.
- **Mislabelled attribute:** the attribute named `rate` holds the frame interval.
- **Licks and sides:** the lick trace has no spout identity, and no field names the choice side. I derived the choice from `trial_type` and the response.
- **Smaller issues:** `session_id` is the timestamp of the CNMF run, not the recording. Some files store non-integer pulse rates. Several ROI columns have no description.

**Assumptions** (protocol step 1.6), where the claims file's readings disagreed:
- fig2bd: "just after the choice" read as within 300 ms of it.
- fig6bc: the test on neurons pooled over sessions, which is what the code does.
- fig7: a one-sample t-test of the per-session changes.
- fig8de: the learning decoders use all trials with a choice.

Each assumption is recorded as a `methods_unavailable` question for the paper's authors. I asked a reader no questions.

## 3. Where the protocol or tooling was unclear or wrong

1. The claims file's opening comment says a claim is blocked when its readings disagree. Protocol step 1.6 allows adopting the best-supported reading instead. I followed the protocol, marked those outcomes `assumed`, and noted the conflict in each deviation.
2. Some criteria define a partial band, and some results fall outside both their reproduced and partial bands (fig2bc, fig8ab, fig8g). I recorded these as `not_reproduced`. Where a criterion gives no partial band, I used the protocol's own definition of `partially_reproduced`.
3. There is no `blocked_by` value for "not reached within the run's time" when the computation itself is not the limit. I used `other` and explained in the notes.
4. `tools/entry.py lock` writes `python: "3.13"` into entry.yaml, which the entry schema then rejects. I removed the line; the lock file still sets the version.
5. A directory `entries/000016-najafi-2020/` from an earlier failed author run is in the checkout. I did not read it and wrote the entry under `entries/najafi-2020/`.
6. Reading (b) of early and late days (only the runs at the start and end of training) leaves 0 or 1 day in most mice, so it cannot be tested. The criteria list it anyway; I report it as untestable and use reading (a).
7. Untracked dotfiles (`.bashrc`, `.gitconfig` and others) appeared in the repository root. I did not create them and left them alone; they should not be committed.

## 4. Runtime and what failed or was cut

- **Runtime:** the three notebooks took 30, 41 and 43 minutes. Most of the first notebook is streaming (about 7 minutes per alignment for all sessions). Peak memory was 6.5 GB.
- **Failures:** nothing failed.
- **Cuts for runtime, each recorded as a deviation:**
  - The SVM regularisation grid uses steps of 1 in log10 instead of 0.2. A check on four sessions showed accuracy differences of at most 0.67 points.
  - Excitatory populations use 5 subsamples, and 3 in the learning analysis, where the paper uses 50.
  - The time courses use 25 splits per bin and one regularisation value per session, chosen at the bin before the choice.
- **Not run:** two figure claims (figs6ab, figs6c), the temporal dynamics (figs2), the three circuit-model claims and the decoder angles (figs7c), as listed in the table.

The executed notebooks, attempt record and handover package are here:
- `executed/najafi-2020/handover/`
- `attempts/najafi-2020-01.yaml`
- `entries/najafi-2020/`
