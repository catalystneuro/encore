No question was asked or answered for this paper, so nothing changed and no claim was re-run.

**What I checked**
- There is no `questions/wirtshafter-2020.yaml`, and nothing in `questions/` is named after this paper.
- In the first author run I asked a reader nothing. All 31 claims were blocked as `data_missing` because hc-29 has no position data, so no method choice ever came up.
- The reader's answer run (`transcripts/wirtshafter-2020/answer-report.md`) says there was nothing to answer and that it changed no files.
- The claims file's only `checks` entry is the second reader's check from 2026-11-11, which came before the attempt. There are no amendments after the attempt.

**Questions, what changed, and outcomes per claim:** none. All 31 claims are still blocked as `data_missing`, as before. `units-recorded` is one of them; its 452 LS and 178 CA1 cluster counts match the paper's, but the criterion also needs two counts that depend on position. Since nothing changed, I did not edit the notebook, the conclusions, the claims' notes or `attempts/wirtshafter-2020-01.yaml`.

**Entry commands**
- `lock`: rewrote `requirements.lock.txt` (Python 3.13); its content did not change.
- `all`: check passed with 0 errors. The run reused the executed copy from 10:15 UTC today (117 s) because nothing it reads had changed, so it executed nothing.
- `handover`: wrote `executed/wirtshafter-2020/handover/`.

Nothing is committed or pushed. The untracked `scripts` folder and dotfiles were already in the working tree before this run, and I left them alone.
