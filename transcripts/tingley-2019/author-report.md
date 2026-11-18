I tested all 39 claims of `claims/tingley-2019.yaml` on DANDI:000218 version 0.261110.1911. Of the 39, 30 were tested and 9 blocked: 8 reproduced, 11 partially reproduced and 11 not reproduced. The entry is at `entries/tingley-2019`, with three notebooks (spikes and events, LFP, Figure 7E) and a helper module, and the record is `attempts/tingley-2019-02.yaml`. `tools/entry.py all` passes with 0 errors, and the handover is built. Nothing was committed.

**Blindness.** The dandiset's own release notes, which I had to read to choose the version, say the files were re-converted to fix "problems found by a reproduction attempt (issue #82)", and list the fixes. That is the only trace of an earlier attempt I met. I did not open the issue, and I saw none of that attempt's outcomes.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig1c-event-count, fig1f-shorter-than-ripples, fig1g-slower-than-ripples, fig4c-temporal-bias, figs2c-no-ls-reactivation, fig5b-nrem-and-rates, fig5d-lag | reproduced |
| fig1h-no-amplitude-frequency-correlation, fig4b-hfo-above-behav | reproduced, resting on an assumption |
| dataset-composition, fig1c-hfo-each-animal, fig1d-phase-locking, fig4d-compression, figs3d-hpc-compression-post, figs2-post-rate-increase, fig7e-ca1-spikes, fig7e-state, fig7e-duration | partially reproduced |
| fig4b-pre-post-unchanged | partially reproduced, resting on an assumption |
| figs1-participation, fig2-confined-to-ls, fig4-sessions-few-change, fig5e-state-coupling, fig5f-ripple-triggered-firing, fig5f-no-phase-coherence, discussion-medial-septum, discussion-cingulate-down-state | not reproduced |
| fig1c-post-burst-suppression, ls-spikes-not-locked-to-ca1-ripples | not reproduced, resting on an assumption |
| fig2ef-intermediate-ls, fig3-travelling-waves, fig7e-ca1-depth | blocked: metadata_insufficient |
| fig7e-content-independent, fig7e-coupled-only | blocked: metadata_insufficient (they depend on fig7e-ca1-depth) |
| fig6-optogenetic-hfos | blocked: data_missing |
| fig7e-replay, fig7e-seqnmf, figs5-seqnmf-variance, fig8-model | blocked: other (not attempted within the run's time) |

## 2. The dataset, assumptions and questions

**What was found about the dataset:**
- **Composition:** six rats with 2551 LS units in 98 files, and no recording deposited twice.
- **Missing from the files:** the two optogenetic rats, electrode positions, each recording's depth within LS, and marked PRE / BEHAV / POST periods.
- **Hippocampal labels:** most hippocampal units are labelled only `hpc`, so CA1 and CA3 cannot be told apart reliably (10 or 19 CA3 recordings depending on the label used, against the paper's 25).
- **Labels and scoring:** 36 units in DT7 20170407 have an empty region label. In 3 files, less than half of the trial time is scored WAKE.
- **Missing event tables:** the DT9 CA3 recordings have no CA1 ripple table. DT7 20170410 has LS units but no LS HFO table.
- **Detection parameters:** the deposited LS HFO and CA1 ripple detections use parameters that differ from the Methods. Even so, their counts, durations and frequencies match the paper.

**Assumptions**, each recorded with a question for the paper's authors (`methods_unavailable`):
- **Epoch boundaries:** PRE, BEHAV and POST are split at the first trial's start and the last trial's stop.
- **Figure 4 CCGs:** normalized by the spike counts. Raw counts make PRE and POST differ.
- **Figure 1H:** Pearson correlation. Spearman finds a negligible but significant correlation.
- **Post-burst window:** starts at the event stop. The other window passes only under some seeds.
- **Locking to CA1:** spikes inside CA1 ripples. In the CA1 high-power epochs the fraction is at chance.

**Questions to a reader:** none.

## 3. Where the protocol was unclear or did not fit

1. **Time.** The time rule only names `too_large` for claims the computation stopped. Claims I chose not to attempt because of the five-hour limit had no named reason, so I used `other` and said so.
2. **Notebook time limit.** The 60-minute limit applies per notebook, so analyses that need the whole dataset had to be split across notebooks. Each one reloads the data (about 2.5 minutes).
3. **Seeds.** Repeating everything under five seeds did not fit for the Figure 7E Poisson fits or for the fig5f jitter. I repeated the linear Figure 7E models only, and gave the reasons in the deviations.
4. **Conclusions and run order.** Result cells must be backed by printed numbers, but the long notebooks' numbers exist only after the run. I added those cells as markdown after the first full run, then re-ran `entry.py all` so the executed copies and stamp match.
5. **Expected values beside an absence criterion.** fig4b-pre-post-unchanged has an expected pair count (7172) that the criterion does not use. I recorded partially reproduced: the absence holds, but only 462 pairs pass inclusion.
6. **Absence claims with no test named.** The rule to judge absence on the paper's test alone has nothing to apply when the paper names no test (fig1h, ls-spikes-not-locked). I treated those claims under step 1.6.

## 4. Runtime and failures

The final run took about 76 minutes: 15 for the main notebook, 45 for the LFP one and 16 for Figure 7E. Peak memory was about 7.4 GB, in the LFP notebook. No job failed in either full run. During development, one site analysis reached 10.7 GB; I bounded it before the full runs.
