Round 1 is answered. Three outcomes changed, and the entry re-runs cleanly: `tools/entry.py all` passes with 0 errors in about 10.5 minutes. Nothing is committed.

**Outcome changes**
- **fig4b-3m-degs**: partially reproduced → blocked (`methods_underspecified`). The previous version picked one reading where they disagreed, but the claims file's rule says a claim whose readings disagree is blocked (verifier point 1). The four readings now give:
  - separate model, unshrunken: 95 up and 136 down, which is reproduced;
  - joint model, unshrunken: 51 and 141, which is partially reproduced;
  - separate model, shrunken: 88 and 45, which is not reproduced;
  - joint model, shrunken: 39 and 37, which is not reproduced.
- **fig4d-3m-go-memory-terms-down**: partially reproduced → blocked (`methods_underspecified`). The paper names no enrichment tool, so I now treat the 10 to 500 gene term-size limit and no limit as two readings (point 3). Across the 16 readings, 2 give reproduced, 5 partially reproduced and 9 not reproduced.
- **fig4fg-ecm-go-terms**: not reproduced → blocked (`methods_underspecified`), for the same reason. 15 readings give not reproduced. One (separate model, shrunken, all annotated genes, no size limit) gives partially reproduced, with an ECM term at adjusted p 0.048.
- **Unchanged**:
  - fig4c-7m-degs stays partially reproduced under every reading, with up counts of 284 to 320 and down counts of 0 to 7.
  - fig4e stays reproduced under all 16 readings.
  - fig4h and the three fig4i claims stay reproduced.
  - The 42 data and metadata blocks are unchanged.

**Corrections and additions**
- **Filtering threshold (point 2)**: pydeseq2 tunes DESeq2's independent filtering at 0.05 by default, where R uses 0.1. The helper now sets 0.1 and shows 0.05 as a variant. Two counts moved slightly (3 M separate unshrunken from 98/137 to 95/136; 7 M from 320/7 to 317/7), and no reading changed outcome.
- **Outputs the verifier asked for**: the notebook now prints the outcome under every reading for each claim, and the full top-10 GO list for all 16 readings at 3 M and at 7 M, with each term marked as matching the memory or immune pattern.
- **Tie order**: GO terms with equal p-values came out in a different order from run to run. I added a tie-break by term ID; no count changed.
- **Near-zero changes (point 5)**: the fig4i notes and conclusion now name Adam10 (+0.003) and Timp2 (+0.07, adjusted p 0.92).
- **Records**: the conclusions, summary, README, helper docstring, deviations, notes and the question for the paper's authors now use the new numbers. fig4c's `measured` is now the first reading the criterion lists (317, 7). Round 1 is recorded under `verifications` for all 51 claims, with the verifier's reasons and my responses.
- **Reader question**: I added `questions/001702.yaml` asking whether the fig4fg criterion's adjusted p < 0.05 is stricter than the Figure 4F/G legend, which only ranks terms (point 4). The claim itself is unchanged.

**Not done**
- **Comparison with R DESeq2**: not run, because R cannot be locked in the entry's environment. This is stated as a deviation.
- **Table of the handwritten cards in the behaviour videos**: not made. It would mean reading cards by hand across 175 videos, and with the scored interaction and exploration times not deposited it could not change any outcome.
- **Points 6 to 8** (sample label mismatch in GEO, helper method choices, chance levels): no change needed. The label mismatch is already a finding, and the verifier judged the method choices reasonable.
