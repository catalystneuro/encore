There were no questions to act on, so nothing in the entry changed.

**The questions:** `questions/espinosa-2017.yaml` does not exist, now or anywhere in git history. In the earlier author run I asked a reader nothing, because nothing in the claims file looked like a misreading of the paper. The reader's run (`transcripts/espinosa-2017/answer-report.md`) found nothing to answer and left `claims/espinosa-2017.yaml` untouched. Since the author run, the only commit is the reader's transcript.

**Effect on claims:** none. No claim was amended, so I re-ran no claim on its own and did not edit the notebook, conclusions, attempt record or any claim's notes. The outcomes stay as they were:

| Claim | Outcome now | Earlier outcome |
|---|---|---|
| fig1-bf-response-classes | Not reproduced | Not reproduced |
| fig1d-excited-cells-fire-faster | Reproduced | Reproduced |
| fig1d-discharge-by-class | Reproduced | Reproduced |
| fig1e-excited-slower-kinetics | Not reproduced | Not reproduced |
| supp4-tail-pinch-response-patterns | Not reproduced | Not reproduced |
| supp1, supp2, supp3 (histology, in vitro) | Blocked: `data_missing` | Same |
| 16 prefrontal claims, fig5c-light-path-needed | Blocked: `data_missing` | Same |
| fig5d-nphr-locomotion, supp14-moving-no-difference | Blocked: `metadata_insufficient` | Same |

**Entry commands:**
- **Lock:** the lockfile came out unchanged.
- **Check and run:** 0 errors, and the notebook ran from a clean environment in 770 s.
- **Handover:** written to `executed/espinosa-2017/handover`. I re-ran it because the earlier run's `executed/` folder was missing from this working tree.

The run left no changes under `entries/` or `attempts/`. I committed and pushed nothing. The modified `tools/build_site.py` and the untracked dotfiles in the working tree are not mine.

If questions were expected for this paper, they were never written, and the open question about how the deposited per-unit response flags were computed is addressed to the paper's authors, not to a reader.
