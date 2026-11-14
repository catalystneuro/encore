There were no questions to act on, so nothing in the entry changed and all 21 outcomes are the same as before.

**No questions were answered.** `questions/asari-2009.yaml` does not exist, either in the working tree or anywhere in the git history. My earlier author run asked the readers nothing. The open points it found went into the attempt as findings: three `methods_unavailable` questions for the paper's authors, one `paper_inconsistency` and one `code_mismatch`. The reader's answer run (`transcripts/asari-2009/answer-report.md`) reached the same conclusion and left `claims/asari-2009.yaml` unedited, which `git diff` confirms.

**What I changed:** nothing. With no answers there was no claim to re-run and no notes to add, so the notebook, the conclusions and `attempts/asari-2009-01.yaml` are untouched.

**Outcomes per claim, unchanged from the earlier run:**

| Claim | Earlier | Now |
|---|---|---|
| methods-recording-counts | partially_reproduced | same |
| a1-mgb-firing-rates | partially_reproduced | same |
| fig2-example-reliability | reproduced | same |
| fig2-example-long-context | partially_reproduced | same |
| fig3a-proportion-significant | reproduced | same |
| fig3a-significance-decay | partially_reproduced | same |
| fig3b-fractional-power-decay | partially_reproduced | same |
| timescale-longer-than-membrane | reproduced | same |
| fig4-predictability-upper-bound | partially_reproduced | same |
| fig4-strf-performance-low | blocked (other, not attempted in the time limit) | same |
| fig5-example-conductances | blocked (data_missing) | same |
| fig6-conductance-decay | blocked (data_missing) | same |
| fig7-example-frequency-context | blocked (data_missing) | same |
| fig8a-proportion-by-property | partially_reproduced (assumed) | same |
| fig8a-significance-fits | not_reproduced (assumed) | same |
| fig8b-decay-by-property | partially_reproduced (assumed) | same |
| fig8c-relative-effects | partially_reproduced (assumed) | same |
| fig8-natural-synthetic-probes-alike | reproduced (assumed) | same |
| fig9-mgb-fast-decay | reproduced | same |
| fig9-example-first-bin | reproduced | same |
| figs1-silence-probe | reproduced | same |

**Entry commands:**
- `python tools/entry.py lock entries/asari-2009` rewrote `requirements.lock.txt` with the same contents.
- `python tools/entry.py all entries/asari-2009` found 0 errors and passed. It reused the executed copy from 19:26 UTC (hash ae9290c2663a) because nothing the run reads had changed, so the notebook was not executed again. That copy had taken 1405 s.
- `python tools/entry.py handover entries/asari-2009` rebuilt `executed/asari-2009/handover/`.

I did not verify the attempt, commit or push.
