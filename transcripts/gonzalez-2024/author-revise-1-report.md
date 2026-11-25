I couldn't re-run the entry this round, so all the new analyses I wrote are out of it. No outcome changed. The entry and its executed notebook are exactly those of the first run, so all the numbers in the record still come from that run. `python tools/entry.py all entries/gonzalez-2024` reused the existing executed copy and reported 0 errors.

**Why nothing new was run.** I wrote all the new code:
- the decoders for fig3e/f/g, as a second notebook;
- the fig7 analyses on the paper's own unit matches (a check that the match table's unit names are the dandiset's, clustering, tuning scores, and the fig7g/h model tests);
- the pairwise model comparisons for the R2 reading;
- the Switch accuracy fix;
- the extra outputs the verifier asked for.

The decoders ran over all 123 sessions in development (about an hour, run alongside the main notebook). The main notebook's development run failed in the cell that compares models pairwise. My loop waiting for it then hung, because it was matching its own command line, until the 2-hour command timeout. That left too little time for the two runs needed: one to get the numbers for the written conclusions, then the final run. I took the revised code back out rather than leave an entry that doesn't match its executed notebook. None of the development results are recorded.

**Outcomes (none changed):**
- **`fig7g-hd-cluster-remaps-more` and `fig7h-hd-cluster-encoder-scores`:** the verifier was right that these can be tested, since the paper's cluster table names the dandiset's units. Their notes now say the earlier `data_missing` block was wrong. They stay blocked, as `other`, because the test was not run.
- **`fig7de-hd-speed-tradeoff` and `fig7f-tuning-metrics-match`:** moved from `data_missing` to `other`, with notes that they can be tested on the paper's matches.
- **`fig3e`/`fig3f`/`fig3g` decoders:** still blocked as `other`. The notes now say this is an analysis not done, not a limit of the data, and that the 0.5 chance level was not compared.
- **Disagreements kept and recorded:**
  - `methods-lookahead-encoder-best`: I kept partially reproduced; the verifier would give not reproduced.
  - `fig4s6-incorrect-coding-overlap`: I kept reproduced (marked seed-sensitive); the verifier would give partially reproduced. The criterion is applied under the claim's own seed and the unit set of the paper's figure code.

**What I added to the record:**
- **Question for a reader:** created `questions/gonzalez-2024.yaml` with one question on fig1d. The claims file says the paper's notebook printed 110.25 as a median of five subject medians, which can't happen with whole trial counts.
- **Notes added:**
  - fig1-switch: Switch accuracy is biased slightly downward by change-of-mind trials.
  - fig3d: the LMEM estimate is 0.107, just below the 0.108 tolerance bound.
  - fig4s7: the unit rule is "more than 5" where the legend says "at least 5" (it removes no unit), and two of the four tests are near 0.05.
  - methods-lookahead: the R2 reading has no pairwise test.
- **`verifications` round 1:** all 30 claims, each with the verifier's reason in its own words and my response. A summary at the top answers each numbered problem. The paper's code confirms that the helper is faithful on speed (computed from the unsmoothed track, as the paper does) and on the angle column (`hd`). The round also says plainly which outputs were written but not run.

**Not done:**
- None of the outputs the verifier asked for are in the notebook, and the notebook's own text (header table, conclusions, summary) still shows the old block reasons.
- No round-2 finding reviews were recorded, as this was round 1.
- The repo root now has untracked empty files (`.bashrc`, `.profile`, `.mcp.json`, `.vscode` and others) that the sandbox seems to have created. I left them, but they should not be committed.
