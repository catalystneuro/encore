No reader answered any questions, so no claim changed. The file `questions/crcns-alm-1.yaml` does not exist, and git history shows it never has on any branch. The first author run asked no reader questions, because the claims file already gives both readings of the place where the Fig. 2d text and figure disagree. The answer run that followed recorded "no questions to answer" (`transcripts/crcns-alm-1/answer-report.md`).

**Questions and what changed:** none were asked, so there was nothing to re-run. I did not edit the notebook, conclusions, claim notes or the attempt record. All 29 outcomes are the same as before:

| claim | outcome now | earlier outcome |
|---|---|---|
| task-performance | reproduced | reproduced |
| unit-counts | partially reproduced | partially reproduced |
| fig2-selective-fraction | reproduced | reproduced |
| fig2d-response-categories | reproduced (under the figure's reading) | same |
| fig2c-selectivity-time-course | reproduced | reproduced |
| fig2c-dynamic-single-neurons | reproduced, resting on the claims file's assumed 0.5 bound | same |
| ed2-error-trials-predict-choice | reproduced | reproduced |
| fig2e-equal-contra-ipsi | reproduced | reproduced |
| ed1-no-population-contra-bias | reproduced | reproduced |
| ed1-fast-spiking-properties | partially reproduced | partially reproduced |
| tagging-counts | reproduced | reproduced |
| antidromic-latency-jitter | reproduced, resting on an assumed ±0.5 ms window | same |
| ed5g-it-second-pulse-jitter | reproduced | reproduced |
| fig3ei-both-types-preparatory-and-movement | reproduced | reproduced |
| fig3fj-contra-preferring-pt-not-it | reproduced | reproduced |
| fig3f-late-contra-selectivity-pt | not reproduced | not reproduced |
| reaction-time | not reproduced, resting on an assumed detection rule | same |
| contra-ipsi-selectivity-forms | partially reproduced | partially reproduced |
| 11 claims (photoinhibition, imaging, photoactivation, ED3 licking, ED3d anatomy, ED7) | blocked, data missing | same |

The three open questions about methods (how reaction time was detected, how antidromic spikes were separated, and which neurons enter the Fig. 3f/j bootstrap) are for the paper's authors. They remain `methods_unavailable` findings in the attempt record.

**Checks:**
- **Lock:** re-locking left `requirements.lock.txt` unchanged.
- **Check and run:** 0 errors, and the notebook ran from a clean environment. It took 400 s, against 239 to 251 s in the first run.
- **Handover:** written to `executed/crcns-alm-1-li-2015/handover`.

The working tree has no changes to tracked files. The untracked dotfiles and `scripts/` were already there and I left them alone. I did not verify my own work, and nothing is committed or pushed.
