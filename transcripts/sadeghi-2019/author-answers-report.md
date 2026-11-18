There were no answered questions, so no claim was re-run and no outcome changed.

**Questions:** `questions/sadeghi-2019.yaml` does not exist and has never been in the history. The first author run asked no questions of a reader (`transcripts/sadeghi-2019/author-report.md`). The answer run's report says it found nothing to answer and left `claims/sadeghi-2019.yaml` unchanged. All 28 outcomes stay as before, for example:
- fig1k-example-temporal-widths: reproduced
- fig1-snr-noise-stronger: partially reproduced
- fig4-example-original-vs-equalized: not reproduced
- the seven model classifier claims (fig9a, fig9b ×2, fig9c, fig9e, fig9-spectrum, fig10): blocked, too_large

The two open method details are still `methods_unavailable` findings, addressed to the paper's authors and not to a reader.

**What I changed:** the model notebook's cost-estimate result quoted durations that did not match its own output. The conclusion said "one to two and a half hours"; the cell now prints 115 to 226 min, then 117 to 226 on the final run. These timings vary from machine to machine, so I made three wording changes:
- **Notebook:** the conclusion now says the estimate changes with the machine, between about one and four hours over the runs made, and is over the 60 minute limit under the more expensive readings.
- **Attempt record:** in `fig9a-optimal-resolution`'s notes I replaced the old run's per-part timings with the same wording. Its outcome is still blocked, too_large.
- **README:** the runtimes now read 35 to 55 min for the neural notebook and 15 to 25 min for the model notebook.

**Entry:**
- `lock` passed.
- I ran `all` twice, once before the edits and once after. Both times it reported 0 errors and both notebooks passed. The final run took 3090 s for the neural notebook and 1337 s for the model notebook.
- `handover` wrote `executed/sadeghi-2019/handover/`.

I did not verify my own work, and nothing is committed or pushed.
