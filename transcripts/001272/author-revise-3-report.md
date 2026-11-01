One outcome changed and no proposals remain open.

**Changed:** `figs1-near-threshold-delayed-aps` went from partially reproduced to not reproduced. It is still marked `assumed: true`. The verifier agreed with the proposal in round 3. The claim's criterion is one test per neuron: the median session near threshold must have 1 to 3 APs and its first AP must be delayed. Under the adopted readings only 1 of 3 neurons passes, and more than half must. The outcome still depends on what "delayed" means. If it means later than the same neuron's APs at stronger fields, every neuron passes, and that question stays with the paper's authors.

**Proposals still standing:** none. This was the only proposal in round 3.

**What I updated:**
- **Attempt record** (`attempts/001272-semenov-2025-01.yaml`): set the outcome, removed `proposed` and reworded the claim's notes. I also corrected the notes on `figs1-effects-same-as-fluovolt`, which mentioned the old outcome. That claim's own outcome stays partially reproduced because its pattern condition fails either way. Round 3 is recorded under `verifications` with one result: agreed, not_reproduced, the verifier's reason in its words, and my response.
- **Notebook** (`di8_controls.ipynb`): rewrote the conclusion in cell 21, the conclusion in cell 36 and the summary table in cell 37. I also fixed the hard-coded "near-threshold partially reproduced" string in cell 35 that the verifier pointed out.
- **Entry README:** updated the table row and the paragraph about this claim.

**Run:** `python tools/entry.py all entries/001272-semenov-2025` reported 0 check errors, and all three notebooks passed (421 s, 301 s and 549 s). The re-run printed the same per-reading counts as before, for example 0 of 24 under O5 (a) with prominence.

I did not commit anything. `tools/build_site.py` already had uncommitted changes when I started; I left it alone.
