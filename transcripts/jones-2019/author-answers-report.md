There were no questions to act on, so no claim was re-run and no outcome changed.

**Questions:** none. `questions/jones-2019.yaml` does not exist, and no commit in the history has ever contained it. The earlier author run asked a reader nothing (`transcripts/jones-2019/author-report.md:51`). The answer run that came after it (`transcripts/jones-2019/answer-report.md`) found nothing to answer and changed nothing. The claims file is the same as at the claims-check commit 3ff2f6e260.

The open points from the first run are method details the paper does not settle, so they are questions for the paper's authors, not for a reader. They stay in the attempt's `methods_unavailable` finding:
- which CA3 sites and mice were used;
- how the 6-9 month IDs map to the recorded mice;
- which distance-per-bout column was used;
- how SG power was averaged;
- which mice formed the z-score population.

**Outcome per claim:** every outcome stays as `attempts/jones-2019-01.yaml` records it. For example, `fig1e-swr-abundance-genotype` is still reproduced, and the re-run printed the same t(27) = 8.21. I did not edit the notebook, the conclusions, the attempt record or any claim's notes, since no answer changed anything they say.

**Entry:**
- `lock`: the lock file came out the same as before.
- `all`: 0 check errors, and `reproduce_jones_2019.ipynb` passed in 2488 s (about 41 min).
- `handover`: written to `executed/jones-2019/handover`.

Nothing was committed or pushed. The working tree has changes I did not make: the edits to `tools/` that were there at the start, and new untracked files (`.bashrc`, `.profile`, `.gitconfig`, `.idea`, `.vscode`, `.mcp.json`, `scripts`, and others). They probably come from the environment. I left them alone.

If someone later files questions in `questions/jones-2019.yaml`, this step can be run again on them.
