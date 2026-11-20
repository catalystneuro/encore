The reader had no questions to answer for prakash-2022, so no claim changed and I re-ran nothing.

**The questions:** `questions/prakash-2022.yaml` doesn't exist. No file in `questions/` mentions this paper, and the reader's answer run (`transcripts/prakash-2022/answer-report.md`) reported the same. The first author run raised no question about a misread claim. Its open points are all for the paper's authors and are recorded as `methods_unavailable` findings in `attempts/prakash-2022-01.yaml`: the errant-contact rule, the percentile rule, gamma-event detection and the baseline bootstrap. A reader doesn't settle those.

**What changed and the outcomes:** nothing. I left the claims file, the notebook, the conclusions and the attempt record alone, since no answer gave a reason to change them. Every outcome stays as it was:
- 13 reproduced
- 3 partially reproduced
- 3 not reproduced: fig6f-nonfunctional-opsin-no-response, fig7d-contacts-exceeding-baseline and fig7f-mua-electrodes
- 7 blocked: five for missing data, one for insufficient metadata and two for underspecified methods

**Entry runs:**
- `lock`: the lock file was rewritten with the same contents, so there is no diff.
- `all`: check found 0 errors. The run passed by reusing the executed copy from 13:45 UTC (2274 s), because nothing the run reads had changed (hash 2f83d12971bd). The notebook was not run again.
- `handover`: wrote `executed/prakash-2022/handover`.

I didn't verify my own work and didn't commit or push. The changes to `tools/entry.py` and `tools/runner/merge_claims.sh` were already in the working tree when I started; I didn't touch them.
