The claims file for 000061 is fit for an attempt, and its new `checks` entry says `ready: true`. I made eight corrections and added one claim. The paper's code was not available to me, so the method details taken from it are still unchecked.

**Checker result:** `32 claims, 31 quotes, 67 statistical values, 5 problems`. All 5 are p-values the checker can't match against the paper's print format, such as "9.70 × 10−9" or "x10-05". I found each one in the text, so the file has no real problems. It passes schema validation and every quote matches word for word.

**Changes, by claim:**
- **hpc-bla-reactivation-post-sleep:** the criterion cited the wrong section for the 3.13 ± 0.73% value. It is in "BLA-hippocampus coordinated reactivations during NREM sleep", paragraph 2.
- **reactivation-all-cell-pairs:** one statistics entry held three tests (the three 20-minute periods) but only the first p-value. I split it into three entries with the supplement's values (8.85e-5, 0.00282, 0.14458).
- **contributing-up-cells-gain-increase:** the same problem for quartiles 2 to 4. Split into three, with p = 0.7834, 0.9704 and 0.9384.
- **no-rem-reactivation:** the paper says REM reactivations were not significant "in any structure". I added the hippocampus-piriform REM test (Fig. 3d, P = 0.301, n = 15) to the statement, statistics and criterion.
- **intra-structure-reactivation:** the quote was only a figure title, which does not state the finding. I replaced it with an `inferred` note saying the finding is read from the Supplementary Fig. 4 legend's tests.
- **bla-rate-same-across-directions:** the criterion picked a set of sessions the paper does not specify. I named the two plausible session sets as readings, and added the rule for when they disagree (`methods_underspecified`).
- **ripple-rate-unchanged:** noted that Supplementary Fig. 11d prints P = 0.1972 where the main text gives 0.192.
- **New claim `each-rat-learns-puff-location`:** covers the per-rat analyses of variance in Supplementary Fig. 1b ("all animals learned"), a finding that had no claim.

No claim ids were changed. The file's opening comment still says "25 other claims are new"; the checks entry records the added claim.

**Still open:**
- The details the criteria take from the paper's code are unchecked: script names, smoothing, cell minimums, test tails, `run.signot`. One cited script, `ExplainedVariance_Ultimate_IntraStruct.m`, is not in the file header's list of scripts read.
- The criteria require "more than 180 s" of REM, while the Methods say "a minimum of 3 min". This only matters for a session with exactly 180 s.
- **habituation-over-days** and **ev-independent-of-firing-rate** rest on readings of figures the paper never tests. Both name their readings and fall back to `methods_underspecified` when the readings disagree.

Nothing was committed.
