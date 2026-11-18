I changed nothing, because there were no questions to answer. `questions/scholl-2015.yaml` does not exist. The original author run asked the reader nothing, and the reader's answer run says so (`transcripts/scholl-2015/answer-report.md`). The claims file was not amended, and its 25 claim ids still match the attempt record exactly.

**Questions and what they changed:** there were none, so no claim was re-run. The notebook, conclusions and `attempts/scholl-2015-01.yaml` are unchanged.

**Outcomes per claim:** all 25 stay as they were in the first run.

| Claims | Outcome now | Earlier outcome |
|---|---|---|
| fig1e-pv-tdtomato-colocalization | blocked, data_missing | same |
| cell-counts-responsive and the 19 claims that depend on the paper's own cells (fig3, fig4, figs3 to figs6, mi-per-animal, mi-dsi-relation, pv-larger-dff-low-dsi) | blocked, data_missing | same |
| fig5-camkii-responsive, fig5e-camkii-od-unrelated, fig5f-camkii-disparity-unrelated | blocked, data_missing | same |

They are blocked because the dataset holds only raw movies. It has no masks or PV+/PV- labels for the cells the paper identified by hand, no CaMKIIa mice, no neuropil patches and no histology.

**Entry steps:**
- `entry.py lock` rewrote `requirements.lock.txt` with no change to the file.
- `entry.py all` reported 0 errors, and the notebook passes. It reused the executed copy from 22:07 UTC because nothing it reads has changed since then, so it did not execute the notebook again.
- `entry.py handover` rebuilt `executed/scholl-2015/handover`.

Nothing is committed or pushed. A run with nothing to answer was probably started by mistake. If questions for scholl-2015 exist on another branch, point me to them and I'll take them up.
