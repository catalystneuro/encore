**Round 3 verification: Yemini et al. 2021 (NeuroPAL), DANDI:000715 v0.241009.1514**

The attempt record proposes a change of outcome for 2 claims: fig7de-optimal-coloring-violations and tables6-tail-pvq-and-post-stimulus. No other claim carries a `proposed` entry.

| Claim | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| fig7de-optimal-coloring-violations | blocked (methods_underspecified) | Yes | – | See 1 below |
| tables6-tail-pvq-and-post-stimulus | blocked (methods_underspecified) | Yes | – | See 2 below |

**1. fig7de-optimal-coloring-violations**

- **The numbers come from the data.** `optimal_coloring_sparsity.ipynb` cell 7 prints the best 3-reporter value from 7,500 runs at each sparsity:
  - 2000: 8.380% (7,020 runs keep 3 reporters), below 9.45 to 11.55.
  - 3000: 9.897% (6,253 runs keep 3 reporters, none below 9.45), inside the band.
  - 1000 (1,000 runs): 7.831%.
  - 1500 (`optimal_coloring.ipynb` cell 8): 6.945%, below the band.
- **The sparsities were not chosen to reach the result.** 1000, 2000 and 3000 are the remaining grid points of the original scan (cell 7 of `optimal_coloring.ipynb`, grid fixed at 250 to 3000). At 1500, 2000 and 3000 most runs keep 3 reporters (95%, 94% and 89% in the scan). The seeds are fixed (7146 + k).
- **The criterion is applied as written.** It says to use "the sparsity whose solutions use 3 reporters", and three sparsities fit that equally well. The outcome is partially reproduced at 1500 and 2000 and reproduced at 3000. So the criterion does not settle the outcome. Blocking it follows the rule the attempt applies to fig6de (`wholebrain_zenodo.ipynb` cell 5).
- **A second open detail points the same way.** The claims file reads the 3-reporter value as the best of 7,500 runs at this one setting, which I reported in round 2 as a misreading of Methods S2 Figure 1. Under the other reading, the best of 100 runs at 1500 falls inside the tolerance 66% of the time (`optimal_coloring.ipynb` cell 9).
- **The 39-reporter value is inside the tolerance under every reading.**
- **Text that does not match the outputs:**
  - The record's note says "563 with 3 reporters" at sparsity 1000. Cell 7 prints 561 runs (share 0.561).
  - The record gives 1.71% with 30 reporters and 1.83% from 189 runs at sparsity 100. The re-executed `optimal_coloring.ipynb` cell 6 prints 1.717% with 27 reporters and 1.859% from 205 runs.
  - On data.mat, the record and cell 13 give 1.81% and 2.03%. Cell 11 prints 1.737% and 1.993%.
  - These are the machine-to-machine differences the record already notes. They do not change the 39-reporter result, but the prose does not match this notebook's printed outputs.
  - Sparsities above 3000 were not run. That does not affect the proposal, since the outcome is already ambiguous within the scan.

**2. tables6-tail-pvq-and-post-stimulus**

- **The numbers come from the data.** `wholebrain_zenodo.ipynb` cell 16 prints the results under each removal reading:
  - PVQ is excited by 2,3-pentanedione under all three readings (q 0.00059 to 0.00077) and responds to neither other stimulus.
  - Without removal, there are post-stimulus responders to NaCl (LUA, PHB, PVW), 2-butanone and 2,3-pentanedione.
  - With one member removed, there are still responders to all three stimuli (NaCl: LUA only, q 0.011).
  - With both members removed, there is no NaCl responder.
- **The test matches the criterion as written** (`wholebrain.py` `responses`). A neuron passes only if its stimulus mean is above its pre-stimulus mean. The post-stimulus mean must then exceed the stimulus mean by a one-tailed paired t test, with Storey q at most 0.05 over the neurons that pass the first condition.
- **The removal readings were not chosen to reach the result.** All three were fixed before this claim was tested (cell 5), and the counts removed are printed (cell 6).
- **The rule is applied consistently.** The claim holds in full under two readings and only in part under the third. Cell 5's rule, that a claim whose outcome differs between readings is blocked, therefore gives blocked. This is the same treatment as fig6de-asj-ric-stimulus-specific (cell 14), which resolves the inconsistency I raised in round 2.
- The "sensory and interneurons" part of the statement is still untested, since there are no neuron types. The criterion does not require it.
