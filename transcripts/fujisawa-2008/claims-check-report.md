The claims file is fit for an attempt (`ready: true`). I made seven corrections, all from the paper, and left four points open. Nothing is committed or pushed.

**Checker:** `claims/fujisawa-2008.yaml: 33 claims, 32 quotes, 7 statistical values, 0 problems` (the same before and after my edits).

**Changes, by claim**
- **Shared method in the header (trials and positions):** the file put position 0 at "the end of the last nose poke" and position 1 at "the start of reward consumption". The paper only says the end of nose poking (Supplementary Figure 6 legend) and the reward area. Both details are now marked open, with two readings each.
- **odor-nosepoke:** the nose-poke period "from the start of the first poke to the end of the last" was made up. How several pokes in one trial are joined is now open, with two readings.
- **fig4-position-dependence:** the partial-reproduction rule assumed 1% of pairs would pass by chance. When left and right trials are tested separately, each pair is tested twice, so the chance rate is about 2%. The rule now follows the reading.
- **no-spatial-clustering:** the statement includes "neurons active at any given part of the maze were recorded with equal probability at all probe shanks", but nothing tested it. I added a second test, shank against where on the maze each neuron peaks.
- **fig7-supralinear:** the file said the 1 to 4 ms transmission lag came from the Methods. The Methods give that lag for a different analysis, and Figure 7 gives none. It is now marked as a reading, with a variant.
- **fig4-pair-156-136:** the statement says the two cells are on different shanks (Figure 4a, shanks 4 and 5), but the test did not check it. I added that check.
- **population-vector-width:** Supplementary Figure 2A prints 0.087 (29 cm), but 0.087 of 230 cm is 20 cm, and 29 cm is 0.126. I kept 0.087 and added a report against 0.126.

**Still open (recorded under `checks`)**
- I could not open the PDF figures here: neither the PDF library nor the page-rendering tool is installed. These readings rest on the first agent alone:
  - Figure 2d and 2e: which count goes with which layer and cell type, the bar heights, which bars have significance marks, and that layer 5 is higher in 2d.
  - Supplementary Figure 1: which rats are in which layer.
- The Supplementary Note says about 37% of recorded cells are interneurons. That matches neither of the paper's own figures (12.5% of units, or 12.5 out of 45%). It has no claim.
- `channel-region-link` is a registry check built on the CRCNS dataset description, not on the paper. No claim lists it as a dependency. Whether any should depends on the data, which I did not open.
- The Discussion's remark that position-dependent interactions occur in all parts of the maze has no claim of its own. It is minor.

Every other quote, expected value and tolerance matched the text. Significance thresholds used only to count units are correctly kept out of the statistics.

`git status` also lists untracked files I did not create: shell config dotfiles, `.idea`, `.vscode`, `.mcp.json` and `scripts`. I left them alone.
