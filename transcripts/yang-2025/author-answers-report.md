No reader questions were filed on yang-2025, so there were no answers to apply and no claim outcome changed.

**Questions and answers:** `questions/yang-2025.yaml` does not exist. In my first run I sent no questions to a reader. I sent the open method points to the paper's authors instead, as eight questions in one `methods_unavailable` finding in `attempts/yang-2025-01.yaml`. The reader's answer run (`transcripts/yang-2025/answer-report.md`) also says there was nothing to answer, and it left `claims/yang-2025.yaml` unchanged. Since my author run, git shows changes only to the two transcript files.

**Claims affected:** none. I re-ran no analysis and did not edit the notebook, the conclusions, the claim notes or the attempt record. All outcomes stand as before:

| Claim | Outcome (earlier and now) |
|---|---|
| tables1-network-stable-short-term | reproduced (only when self-pairs, r = 1, are counted as intra-group) |
| fig2-r1-target-shifts | partially reproduced (3 of 4) |
| figs2-target-assignment | partially reproduced (20 of 28 baseline groups) |
| fig3a-target-reduces-each-rat | not reproduced (3 of 8) |
| fig3a-nontarget-can-lengthen | reproduced (11 of 20) |
| fig3a-per-rat-site-differences | partially reproduced (5 of 11 pairs) |
| fig3a-target-vs-nontarget-total | not reproduced (p = 0.93) |
| fig3a-some-nontarget-shorten | partially reproduced |
| fig3b-same-site-target-vs-nontarget | not reproduced |
| seizure-duration-proportion, fig3c-frequency-no-difference | blocked, data_missing |
| fig4b-psd-target-bands, fig4b-psd-other-bands-unchanged | not reproduced |
| fig5b-iis-post-seizure | reproduced |
| fig5c-interictal-iis, fig5d-iis-seizure-correlation, fig6cd-interictal-hfo | blocked, data_missing |
| fig6e-ictal-ripples-no-difference | reproduced |
| fig6f-ictal-fast-ripples-reduced | not reproduced |

**Lock, check, run and handover:**
- **Lock:** `tools/entry.py lock` left the lock file unchanged. It again added a `python: "3.13"` line to `entry.yaml`, which the schema rejects, so `check` failed with 1 error. I restored the file without that line, as in the first run.
- **Run:** `entry.py all` gives 0 errors, and the clean run of `reproduce_yang_2025.ipynb` passed in 382 s.
- **Handover:** the package was written to `executed/yang-2025/handover`.

I did not verify my own work, commit or push.
