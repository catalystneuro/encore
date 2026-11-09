No reader answered any question on 000223, so nothing in the analysis, notebook, conclusions or attempt record changed.

**The questions**
- There is no `questions/000223.yaml`, even after fetching from origin, and no commit in the history has ever touched that path.
- The reader's answer run (d22e19e) found the same and changed nothing (`transcripts/000223/answer-report.md`).
- The claims file (`claims/000223/10.1088-1741-2552-ac8765.yaml`) has not changed since the author run.
- The first author run raised no reader questions. Its three questions go to the paper's authors and are recorded as `methods_unavailable` findings: which p_thresh and hyperactive-unit strategy each recording used, where the background ROIs were, and how OUT/IN was computed. Those are method details the paper doesn't give, not cases where the claims file misreads the paper.

**Outcomes**
With no answers, every outcome stays as the author run left it (earlier = now):
- reproduced: data-scale, fig1e-best-r-gap, fig5a-rejection-scenarios, fig5a-threshold-order, fig5c-spike-contrast-vs-fscore
- partially_reproduced: table1-best-r (assumed), table1-optimal-thresholds, mean-max-fscore, acceptance-9-of-20, best-r-accepted-vs-rejected, best-r-not-predictive, fig5d-out-in-vs-fscore (assumed)
- not_reproduced: table1-network-measures

Because nothing changed, no claim notes say what an answer changed.

**Entry checks**
- `lock` rewrote `requirements.lock.txt`, and git shows no changes to it.
- `all` gave 0 errors and the notebook passed (1096 s, clean environment). The executed copy shows the same numbers the record gives: 101.7/42.6, 0.695/0.121, U = 5 with p = 0.0015, 0.622/0.337, 0.625/0.515, R = −0.724 and 0.592.
- `handover` wrote `executed/000223-xue-2022/handover`.

I did not verify the attempt, commit or push. The only change in the working tree is the existing edit to `tools/runner/chain.sh`, which I did not touch. The untracked dotfiles in the repo root (`.bashrc`, `.gitconfig`, `.mcp.json` and others) were not created by this run, and I left them alone.
