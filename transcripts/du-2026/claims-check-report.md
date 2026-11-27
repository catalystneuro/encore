## Review of `claims/du-2026.yaml`

**Checker result:** `claims/du-2026.yaml: 33 claims, 32 quotes, 12 statistical values, 0 problems`. It gave the same result before and after my edits.

I read the whole paper and checked the cited code release (tag v1.0-jne-submission, commit b042fbe, which matches the commit the file records). The statements, sources, statistics, expected values and interval-based tolerances match the paper. Every main finding has a claim, and none comes from outside the paper.

**Changes, by claim:**
- **link-neural-only-r2:** the code citation was wrong. `run_link_context_ladder.py` never computes neural-only R2, and no release script does. The penalty rule is now cited to `estimators.py` `evaluate_decoders_nested` as the code's choice.
- **link-context-only-r2:** I removed the requirement that context-only R2 rise at every rung. The paper gives only the two endpoints, and the middle rungs don't contain each other's features, so a rise at each step isn't guaranteed.
- **link-phase-only-replacement:** the statement added an interpretation the paper doesn't make, and I cut it. The criterion now cites the paper for using a same-direction source. It also notes that with phase-only context every source is equally close, so the lowest trial index picks the source (the tie rule in Methods 4.7). I added a rule for judging the claim.
- **synthetic-pair-breaking:** the reason given for the seed-count tolerance was wrong. The paper's "at least 9 of 10 seeds" rule covers replacement only, not the permutation control.
- **rff-link:** "combined range" had only one reading. I added a second: the range over the six CO and RD task means that Figure 6c plots.
- **estimator-family-link:** the file said the release left these methods open. It doesn't: the code holds both estimators (`evaluate_block_ridge_audit` and `evaluate_rff_context_audit`), and Figure 5a plots their saved results. The criterion now follows that code, and "task means" can also be read as the CO and RD means.
- **temporal-offset and context-capacity-contrast:** the file stated as fact that these used the fully nested estimator, but the paper never names the estimator. The saved table behind Figures 7a and 7c doesn't match the fully nested values and has the output fields of `evaluate_decoders_nested`. Both estimators are now listed as possible readings.

**Still open:**
- **temporal-offset:** where the fixed behavioral window sits (the file assumes 280 ms after trial start) isn't stated in the paper, and no release script settles it.
- **replacement-ranks-lower:** the supplement wasn't supplied, so this claim can only be judged on whether each mean went down.

**Ready:** yes. The `checks` entry is added with `ready: true`. Nothing was committed or pushed.

`git status` also lists untracked files I didn't create (`.bashrc`, `.idea`, `scripts`, and others), and I left them alone.
