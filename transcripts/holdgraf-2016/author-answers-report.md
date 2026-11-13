No reader questions were answered, so no claim was re-run and every outcome is the same as before. I changed nothing in the notebook, conclusions or attempt record.

**Questions: none.**
- `questions/crcns-ac-4.yaml` does not exist, and it is not in the history of any branch.
- My first author run asked a reader nothing. The answer run (`transcripts/crcns-ac-4/answer-report.md`) confirms there was nothing to answer, and it left the claims file alone.
- The four open points in the attempt are questions for the paper's authors, recorded as `methods_unavailable` findings: the Speech-R z-score, the ridge mode and the STRF-R bound, the coherence bandwidth, and the scale of the Figure 9c RMS. They were not questions for a reader, and no one answered them.
- Nothing under `claims/`, `questions/`, `attempts/` or the entry has changed since the author commit (cfe333b62b).

**Outcomes, unchanged:** 10 reproduced, 5 partially reproduced, 5 not reproduced and 6 blocked. The per-claim table is in `transcripts/crcns-ac-4/author-report.md`. The largest gap is still the eSTRF selection: 9 electrodes qualify against the paper's 53, so all the eSTRF claims rest on those 9.

**Entry commands:**
- `lock`: the lock file came out the same.
- `all`: 0 errors, and the notebook passes in 1190 s (about 20 minutes, against 12.7 minutes last time).
- `handover`: written to `executed/crcns-ac-4-holdgraf-2016/handover`.

I did not verify my own work, commit or push. The modified `tools/build_site.py` and the untracked dotfiles at the repo root were there before this run, and I left them alone.
