No questions were asked or answered for this attempt, so there was nothing to re-run and no outcome changed.

**No answers to act on.** The file `questions/crcns-apl-1.yaml` does not exist, and no branch's history has ever contained it. The reader's answer run (`transcripts/crcns-apl-1/answer-report.md`) found the same thing and changed nothing. My earlier author report asked a reader no questions. Its four open questions are for the paper's authors and are recorded as `methods_unavailable` findings: the kernel width, the rule for how many principal components to keep, the cutoff for dropping divergent periods, and the permutation test behind Figure 5B. The claims file was last changed by the claims-check run, before my author run. So no claim was amended, and I left the notebook, conclusions, attempt record and claim notes unchanged.

**Outcomes per claim.** All stay as recorded earlier: 20 reproduced, 5 partially reproduced, 3 not reproduced, 2 blocked.
- Partially reproduced: dataset-size, fig3h, fig4bc, fig6d, fig6s2.
- Not reproduced: fig3a, fig4s1a, fig7gh.
- Blocked: fig7s2 (`not_runnable`) and fig8 (`metadata_insufficient`).

**Entry runs.**
- **Lock:** rewrote `requirements.lock.txt`; git shows no change to it.
- **Check and run:** `entry.py all` gave 0 errors, and the notebook ran from a clean environment in 931 s.
- **Numbers:** I spot-checked the executed copy and the counts match the record. fig3a coalesces within one period in 12 of 30 under the adopted reading. fig3h has 15 of 16 periods returning under the mean period and 16 of 17 under the median. fig6d has 8 of 9.
- **Handover:** built in `executed/crcns-apl-1-bruno-2017/handover/`. It holds the notebook, `apl.py` and the claims file.

Nothing is committed or pushed, and I did not verify my own work. The untracked dotfiles and a `scripts` entry in the repository root aren't mine, and I left them alone.
