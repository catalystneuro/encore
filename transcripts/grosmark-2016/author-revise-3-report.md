I applied round 3. The final `python tools/entry.py all entries/grosmark-2016` run passed in 1717 s with 0 errors, and `check` still passes after a last wording fix in the record. Nothing is committed.

**Outcome changed**
- **fig4e-gain-sequences** went from partially_reproduced to not_reproduced, and its `proposed` is removed. The verifier agreed: the criterion has no partial outcome, and the low-gain group also rises under five of the six readings. The notes, the result cell, the summary and the README now say not reproduced.

**Proposal that stands**
- **figs16de-more-ripples-post** stays partially_reproduced, with not_reproduced still under `proposed`. The verifier did not agree yet. The ripple-event intervals were run only under readings L-a and S-a. Reading L-b keeps about 60% of the PRE events and 72% of the POST ones, so the intervals would be longer, and whether the medians then fall within tolerance has not been run. I added the verifier's view to the proposal's reason. The result cell, the summary and the README say that this analysis waits for a new attempt. I did not run it, since the protocol leaves such analyses to a later attempt.

**Round 3** is recorded under `verifications`, with one result for each of the two claims. The figs16de result gives no outcome, because the verifier gave none; its reason says the outcome is undetermined.

**Values that change between runs:** the verifier pointed out that its execution printed different fig4d values from the record. Across the three executions of this revision, the replay reruns came out slightly different from run to run, in the third significant digit. For example, fig4d's main reading was 0.046 and then 0.0458, fig4e's high-gain reading was 0.0624 and then 0.0625, and figs12 at 25% was -0.0675 and then -0.0676. No outcome changes. Fixed seeds do not explain this, and I did not find the cause. In the notebook I now give these values to two significant digits, in the result cells of figs12, fig2e, fig4d and fig4e. The record gives the values each execution printed.
