Round 3 reviewed only one claim, figs5c-turn-angles. The verifier agreed with the change I proposed, so I applied it.

**Outcome that changed**
- **figs5c-turn-angles** went from reproduced (resting on an assumption) to **not_reproduced**, and `proposed` is removed. The claims file names two ways to measure a turn over the dataset's turn events. Under both, the medians are about -21 and +21 degrees for every turn set and every complex file set, and the paper's values are -34.2 ± 3.42 and +33.8 ± 3.38, so none is within tolerance. Only bounding each turn at 20% of its peak on both edges matches the paper. The paper never states that end bound, and I adopted it after the other bounds had failed, so it is now recorded as a variant that does not decide the outcome.
- To match, I changed three other fields on this claim:
  - `measured` is now the first reading the criterion lists (all turns pooled, heading change): -20.8 and +21.3.
  - I dropped `assumed: true`, because the result holds under every turn set and complex file set.
  - The deviation now describes the 20% bound as a variant.
- No other outcome changed.

**Proposals that stand:** none. This was the record's only proposal.

**Other updates**
- **Notebook:** the result cell (25) and the summary row for this claim now say not reproduced.
- **README:** the table row and the paragraph say not reproduced, and mention that a reader has been asked whether the dataset's turn events are the paper's turn bounds.
- **Attempt record:** round 3 is under `verifications`, with the verifier's reason in its own words and my response.

`python tools/entry.py all entries/brudner-2026` ran with 0 errors and the notebook passed (929 s); cell 24 gives the same numbers as before. Nothing is committed.
