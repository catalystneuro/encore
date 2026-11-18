**Verifier report: daste-2025 on DANDI:000785 @ 0.260520.1603, round 3**

The claims file has 36 claims and the attempt record has 36 outcomes. Two outcomes carry a `proposed` change: fig2b-lifetime-sparseness-similar and fig4ij-valence-correct-trials. I reviewed only those two. Passive notebook = `P`, Go/NoGo notebook = `G`; numbers after them are cell indices.

| Claim | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig2b-lifetime-sparseness-similar | blocked (methods_underspecified) | Yes | — | See below. |
| fig4ij-valence-correct-trials | blocked (methods_underspecified) | Yes | — | See below. |

**fig2b-lifetime-sparseness-similar**

- **The numbers come from the data.** They are in P17, and every figure in the proposed reason matches its output:
  - 21 OB-p, 11 mPFC-p and 230 untagged neurons are never active (P15).
  - Never-active neurons left out: smallest corrected p is 0.0067 (start reading) and 0.015 (centre reading).
  - Never-active neurons set to 0: the claim's condition holds (smallest corrected p 0.061 and 0.10).
  - Never-active neurons set to 1: the condition fails (0.0079 and 0.011).
- **The criterion is applied as written:** two-sided Mann-Whitney U, Bonferroni over the 3 pairs, outcome decided by whether any pair has corrected p < 0.05.
- **Why the outcome cannot be settled:**
  - `pcx.vinje_gallant` gives NaN for an all-zero response. The paper's formula and its handling of that case are lost from the text (paper line 485). So none of the three treatments has a basis in the paper.
  - The two treatments that keep every neuron, which the criterion's n (81, 84, 1978) points to, give opposite outcomes.
  - The choice of treatment was not made to reach a result: all three are printed side by side.
- **One weakness in the argument, which does not change my view:** Figures 2C and 2E give the same n (81, 84, 1978). The n may simply be the group sizes, not proof that never-active neurons were kept in 2B. Even so, the left-out reading has no better basis than the other two, so methods_underspecified is the right outcome.

**fig4ij-valence-correct-trials**

- **The numbers come from the data:**
  - Matched correct-trial table: 30 trials, split 17, 6, 4 and 3 across the four CS, 77% CS+. Shuffled-label valence accuracy is 65.5 to 69.0% (G21, G32).
  - Balanced table: 12 pseudo-trials. mPFC-p odor-phase accuracy is 27.8% (mean aggregate) and 31.4% (maximum), against shuffled means of 51.3% and 51.0%. Only 6% and 12% of shuffled repeats fall below these, Mann-Whitney p = 3e-14 and 1.4e-11 (G32).
  - Under the balanced table the claim passes only with the maximum aggregate. With the mean aggregate, act-early does not differ (p = 1), so 3 of 4 phases differ (G21, G32).
  - Under the matched table, mPFC-p odor is above 50% and the groups differ in only 2 or 3 phases (G32).
- **Neither construction is credibly the paper's, and the claim's pass depends on which one is used.** That is a methods_underspecified block, not a not-reproduced outcome. Further evidence:
  - The paper reports chance at 50% (line 143), which the matched table does not give.
  - The paper reports a correct-trial valence scheme in the stability analysis across days (Figure 5F, line 195). With matching by CS and order, day 1 has only 1 correct trial per CS (G15). So the paper's correct-trial pseudo-populations were probably not built by CS-order matching at all.
- **Two points on the reasoning, neither of which changes the outcome:**
  1. The record and G33 say identity "cannot be cross-validated with 3 trials per CS". That is overstated: a stratified 3-fold split, with 2 training trials and 1 test trial per CS, is possible though very small. The inference that the paper's table was not 3 per CS rests better on the Figure 5F evidence above.
  2. The proposal says "no construction … has a defensible basis". One untried candidate exists: class-weighted SVMs or balanced accuracy on the matched 30-trial table. That would put chance near 50% while keeping the paper's matching. The paper does not describe it, so it would be another assumption and would not lift the block. The sentence should say that the paper's construction cannot be identified, not that no construction is defensible.

**Claims file:** in reviewing these two claims I found no place where the claims file misreads the paper.
