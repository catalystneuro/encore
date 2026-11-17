There were no answered questions, so nothing in the entry changed. Every claim keeps the outcome from the first author run.

**Questions.** `questions/000987.yaml` does not exist. No commit or branch has ever had it. The first author run asked a reader nothing ("Questions to a reader: none", `transcripts/000987/author-report.md`), and the answer run confirmed it had nothing to answer and changed nothing. The six `methods_unavailable` findings in the attempt record (Figures 5F, 1B, S1I, S1L, 2/S2D and S2E) are questions for the paper's authors. A reader does not answer them, so they cannot amend the claims file.

**What changed.** No claim was amended, so I re-ran no claim on its own and did not touch the notebooks, the conclusions, the attempt record or any claim's notes. The outcomes from the first run stand:

| Claim | Outcome (unchanged) |
|---|---|
| rsc-dataset | not reproduced (638 units, against the paper's 570) |
| fig5f-rsc-pmr-onset | reproduced, rests on an assumption |
| fig5c-posub-pmr-onset | reproduced, rests on an assumption |
| fig5d-isomap-pmr | reproduced |
| fig1e-delay-range | reproduced |
| fig1g-dv-sequence-du | reproduced, rests on an assumption |
| fig1h-ventral-down-longer | reproduced |
| fig1b-no-dv-tuning-gradient | reproduced, rests on an assumption |
| figs1j-dorsal-ventral-same-hd | reproduced |
| figs1i, figs1kl, figs2d | blocked, `methods_underspecified` |
| fig2f-gamma-travels | not reproduced |
| figs2e-speed-similar | not reproduced, rests on an assumption |
| fig1j, fig1k | blocked, `other` (not attempted in the time) |
| figs2g-adn-synchronous | blocked, `metadata_insufficient` |
| fig5e-fc-pmr-onset | blocked, `not_runnable` |
| fig3, fig3f | blocked, `not_runnable` (MATLAB) |
| fig4d, figs4 | blocked, `data_missing` |

**Entry runs.**
- `lock` wrote `requirements.lock.txt` again with the same contents as before, so git shows no change.
- `all` reported 0 check errors, and all three notebooks ran clean: `reproduce_mehrotra_2024.ipynb` in 125 s, `posub_000939.ipynb` in 321 s and `posub_lfp_000939.ipynb` in 770 s.
- `handover` built `executed/000987-mehrotra-2024/handover`.

I did not verify my own work, commit or push. The changes to files under `tools/` were already in the working tree when I started; I did not make them.

If questions for 000987 were meant to go to a reader, someone needs to add them to `questions/000987.yaml` and have a reader answer them before the next author-answers run.
