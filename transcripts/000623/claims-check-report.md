The claims file for 000623 is ready for an attempt. I made six corrections and left two points open; nothing is committed or pushed.

**Checker:** `31 claims, 30 quotes, 40 statistical values, 0 problems`, the same before and after my edits.

I checked every claim against the paper and against the authors' code (`rutishauserlab/bmovie-release-NWB-BIDS` at commit 8c35290). Most of the file holds up:
- **Methods match the code:** the shared methods follow the code accurately (bootstrap, permutation test, HFB pipeline, gaze heatmaps, AUC, inclusion rule, which cells and channels are plotted).
- **Table 1:** recomputing from the table gives a mean age of 37.75 and an SD of 13.86 (population SD, as the code computes it), with 11 female.
- **Scene cuts:** applying the file's scene-change rule to the code's annotation file gives 93 cuts and 13 scene changes.
- **Numbers and coverage:** the statistics and expected values are the paper's own numbers, and every main finding has a claim.

**Changes, by claim**
- **memory-sessions-included** (and open detail 5): added a third reading, the paper's own two exclusion criteria (behavioral AUC at or below 0.6, or fewer than 10 correct trials per condition). The paper states an AUC rule that the code never applies, and when the text and code disagree, both have to be run.
- **confidence-accuracy:**
  - The criterion now describes the high/low confidence split exactly as the code does it. In one of its two splits, rating 5 belongs to neither class. The old wording would have counted it as low confidence.
  - `n` changed to "sessions (one line per session in Fig. 3c)". The old value came from the code, and this field should record the paper.
- **fig6-examples:** added the Fig. 6a p-value (0.003, 10% tolerance) under `expected`, which the criterion already required and fig7-examples already does.
- **fmri-motion:** added the paper's reported minimum and maximum values (framewise displacement 0.09 and 0.38 mm; outlier volumes 0.2% and 14.8%).
- **Header:** reworded the permutation p-value formula. The old wording could be misread as counting null values at or above "observed + 1".

**Still open** (recorded under `checks`)
- **Scene-cut selectivity direction:** the paper says responses "differed significantly", but the code counts only cells where scene changes are above continuity cuts. The file follows the code and shows either direction as a variant; the paper does not rule that out.
- **Unit brain area lookup:** two of the code's scripts look up a unit's area in different ways. They give the same answer only if the electrode table is numbered 0 to n-1, which the author should confirm on the data.
