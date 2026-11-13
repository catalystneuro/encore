There were no questions to apply, so this run changed no claims, notebooks, conclusions or attempt record.

**Questions:** `questions/henry-2022.yaml` doesn't exist. The earlier answer run found the same thing (`transcripts/henry-2022/answer-report.md`): the first author run asked readers nothing. Its open method details went to the paper's authors as a `methods_unavailable` finding in `attempts/henry-2022-01.yaml`. Those cover how the spontaneous rate was measured, the decoder and threshold-fit details, and how the tuning model's terms were averaged. No claim was amended, so no claim needed re-running.

**Outcomes per claim:** all are as previously recorded, since no answer touched them:
- **Reproduced (17):** fig2a, fig2b, fig2c-farthest, fig2c-v4-worse, fig2de, figs3, fig3ab, fig3c, fig3d, fig3e, fig4b, fig4c-significant, fig4c-v4-stronger, fig4c-v4-maintained, figs5, fig5-terms-covary, fig5de, fig6e, figs6.
- **Partially reproduced:** data-populations, fig2f-v4, fig4a, fig5bc, fig5-negative-multiplicative, fig6c, fig6d, fig7cd.
- **Not reproduced:** fig2f-v1, fit-quality.
- **Blocked (data missing):** fig1b, figs4, fig6-well-isolated.

**Entry checks:**
- `lock`: the lock file came out unchanged.
- `all`: 0 check errors, and both notebooks pass when run fresh (`reproduce_henry_2022.ipynb` in 1396 s, `pseudo_populations.ipynb` in 1094 s).
- I spot-checked the executed outputs against the record, and the values still appear there (for example 0.580, 0.206, 7.302, 1.685, 0.0672, 0.405, 0.389).
- `handover` wrote `executed/henry-2022/handover/`.

I didn't verify the attempt and haven't committed or pushed anything. If a verifier's questions were meant to be in this run, they were never saved to the repository. Once they are in `questions/henry-2022.yaml`, run the answer and author-answers steps again.
