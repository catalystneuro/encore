## Report: author run on DANDI:000785 (Daste, Pierré et al. 2025)

The attempt is complete and the handover is built. Two notebooks (`passive` 23.5 min, `gng` 9.9 min) pass `tools/entry.py all` in a clean environment. Their outputs match the development run line for line. I pinned version 0.260520.1603: the paper cites no version, and the two published versions hold the same 61 blobs, so I took the latest. Nothing is committed.

### 1. Outcomes (36 claims: 18 reproduced, 3 partially, 9 not reproduced, 6 blocked)

| Claim | Outcome |
|---|---|
| dataset-neuron-counts | partially reproduced (identity and concentration within tolerance; Go/NoGo OB-p 103 to 108 per session, paper 95 ± 2) |
| fast-dataset-counts, tracked-neuron-counts | reproduced (exact: 24/27/424 from 5 mice; 46/41) |
| figs2b-labeling-similar | reproduced |
| mlp-projection-f1, transformer-projection-f1, fig1g-attention-timing, fig1f-latent-separation | blocked, methods_underspecified (Tables 5, 6 and 8 missing from the text) |
| fig2b-lifetime-sparseness, fig2c-mutual-information, fig2d-population-sparseness | not reproduced |
| fig2e-reliability | not reproduced (rests on an assumption about the Bonferroni count) |
| fig2-proportion-responding, fig2f-latency, fig2g-early-peaks, fig2i, fig2k | reproduced |
| fig2j-identity-decoding-peaks-earlier | reproduced (fragile: a dev run with other seeds went the other way) |
| fig2h-identity-decoding-5s | blocked, methods_underspecified (the 0–5 s and 1–5 s windows disagree, as the criterion foresaw) |
| fig3bc-concentration-tuning, figs5-sparseness-concentration | reproduced |
| fig3de-concentration-decoding | partially reproduced (mPFC-p not close to chance) |
| figs5g-pairwise-concentration | not reproduced |
| fig4c-behavior-learning | not reproduced (F = 1.57, paper 4.375) |
| fig4c-anticipatory-licking, fig4def, fig4g, figs10d, fig5e | reproduced |
| discussion-differences-grow | reproduced (rests on the sub-668 assumption) |
| fig4h, fig4ij, figs8 (valence timing) | not reproduced |
| figs10e-sparseness-slope | reproduced (rests on an assumption about undefined sparseness) |
| fig5c-cv-higher-obp | blocked, methods_underspecified (the two combination readings disagree) |
| fig5f-stability | partially reproduced |

### 2. Dataset findings, assumptions and questions

**Findings about the dataset:**
- **Wrong imaging rate:** the stated rate is wrong in 21 files. They say 30, 50 or 100 Hz; the timestamps give 4.51 to 4.52 Hz.
- **An extra mouse:** the Go/NoGo experiment has 8 mice where the paper has 7. The extra mPFC mouse appears to be sub-668: it has no tracking IDs and only 24 to 58 cells per session. Its 90% day-3 performance passes the paper's 60% exclusion rule, so nothing documents why it is out.
- **Dropped planes:** the paper's counts match only with the code's rule of skipping planes that have no red cells. In sub-164 and sub-8 that plane nearly duplicates plane 0 (mean-image r = 0.994 and 0.996). The files do not mark these planes. No recording is deposited twice across files.
- **Trial length:** four identity sessions have 30 s trials with odor onset at about 10 s, where the paper describes 22 s trials with a 5 s baseline.
- **Tracked mice:** the 46 tracked OB-p neurons come from 3 OB-p mice, not 4.
- **Mouse counts:** the paper's own counts disagree (Methods 9 + 8, Figure S2B 9 + 10); the dandiset has 10 + 8.

**Assumptions** (each recorded as an assumption and a `methods_unavailable` question for the paper's authors):
- sub-668 is left out. The outcomes are the same with all 8 mice except discussion-differences-grow, which was only run with 7.
- For Figure 2E, Bonferroni covers the 3 group pairs. With 2 tests instead, one reading would make the claim partially reproduced.
- Neurons with no defined sparseness are left out (figs10e). One variant that keeps them gives p = 0.048.

**Question to a reader:** fig5c, in `questions/000785.yaml`. The Results say the ANOVA runs over "combinations of odors and task phases", which seems to rule out the valence-by-phase reading. The odor reading gives p = 0.0115 (paper 0.0127), which would reproduce the claim.

### 3. Protocol gaps
1. **Criterion block vs step 1.6:** step 1.6 says to adopt the best-supported reading, but the criteria for fig2h and fig5c block the claim when readings disagree. Step 1.6 does not say which rule wins, so I followed the criterion and blocked both.
2. **Absence claims with several readings:** for fig2h the criterion names several readings, while the protocol says absence is judged on the paper's test alone. I followed the criterion.
3. **Outcome depends on the seed:** the protocol does not cover this. For fig2j I recorded the dev-run reversal in the notes and did not let it decide the outcome.
4. **Grading partial results:** some criteria (fig3de, fig5f, figs5g) only say what "reproduced" means, so there is no rule for partial results. I graded them by the protocol's general definition.
5. **Editing conclusions after the run:** the protocol does not say whether conclusion markdown may be changed without re-running. I patched one conclusion in both the source and executed GNG notebooks; no computation changed.
6. **Extra subjects:** the protocol covers datasets that hold only part of the paper's data, not datasets that hold more. I took the extra mouse out as an assumption and showed results with it.
7. **Code as an input:** it is unclear whether method details read from the paper's code belong under `inputs`. I listed the GitLab commit.
8. **Duplicate check timing:** I ran the duplicate-recording check (step 1.2) late; it is now in the GNG notebook. The protocol could put it before the first full run.

### 4. Runtime and failures
- The run took about 3 h of the 5 h (01:46 to 04:45 UTC). Streaming all the data takes about 4 min. I made two full clean runs of about 33 min each.
- The final runs had no failures. Development bugs were fixed: a pingouin column name, the pandas `.agg` name clash, and folds with a single class.
- The passive notebook runs 23.5 min, over the protocol's 10-minute aim but under the 60-minute limit.
