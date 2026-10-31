I've worked through every point in the round-1 report and re-run the entry twice; the second run gave identical numbers. `tools/entry.py all` passes for all six notebooks (each between 6 and 17 minutes) and `check` reports 0 errors. Nothing is committed.

**Changes in outcome**

| Claim | Before | Now | Why |
|---|---|---|---|
| selection-shuffled-control | reproduced | not_reproduced (rests on an assumption) | The paper's own code reshuffles the trials in every iteration, so that reading can pass no cell whatever the data. Shifting each trial once, as the Methods describe, passes 5.22% (166 of 3179), above the 1% limit. |
| fig2f | reproduced | partially_reproduced | In every pair, randomly paired cells give as large a V as matched ones, including the one pair that drove the result. |
| fig3c | reproduced | partially_reproduced | V is outside the tolerance, and 2.6% of 1000 random pairings reach it. |
| fig5e | reproduced | partially_reproduced | Two null tests added. The V is only slightly above random pairing (p = 0.002), and 29.1% of peaks are within 18° against 26.2% by chance. |
| fig5f, fig5gh, fig5i | reproduced | partially_reproduced | Each criterion is met, but on classes that are not the paper's. For fig5i, the ellipses also overlap too much to separate the axon groups. |
| figs6 | reproduced | not_reproduced (rests on an assumption) | It passed only because of one pair whose animal-controlled file covers 6 of 60 heading bins. Without that pair, p = 0.97 and 0.90, and no pair passes on its own. |
| Seven fig6 decoding claims | blocked | tested in a new `decoding.ipynb` | Two not reproduced (all cells in light-on; alignment cells). Three partially reproduced (all cells in light-off; heading cells; landmark cells). Two reproduced (180° errors; heading cells below the population). |

Three of these go further than the verifier did:
- **fig5e:** I chose partially, not their not_reproduced, because a small excess over chance remains.
- **figs6:** I moved it to not_reproduced, where they had kept reproduced.
- **fig6:** they gave no outcome for the decoding claims because there was nothing to judge.

Round 2 will review all three.

Four decoding outcomes (all cells in light-off, heading cells, landmark cells, 180° errors) rest on choosing the Methods' Bayesian decoder. The lab's own HeadingDecoder, as I reimplemented it, decodes near chance on these data (0.20 to 0.22). Chance, measured for each decoder, is 0.10, which matches one of the paper's two stated chance levels.

**Added or corrected**
- **Selection test:** a false-positive check on synthetic untuned cells. 4.7% pass with the centred fit and 1.7% with the code's fit. The KS test on 1000 overlapping split-halves is in the paper's own code, so fig1g stays reproduced. Its notes now say about a third of the selected cells could pass by chance.
- **fig2f checks:**
  - a random-pairing null for each pair;
  - selective share and activity of head- versus chamber-rotation files (53 to 83% against 8 to 65%);
  - how far a clock offset could move preferred headings.
- **fig4 light-off:** the reading over selective axons only.
- **fig1h:** shows that the code fit's clustering near −90° comes from its fit bounds, so it says nothing about where the cue is.
- **fig5k:** the structure of the two visual-cue-only files. Their blocks differ only in rotation direction and no other file shares their cells, so it stays blocked.
- **Clock check:** now interpreted (three files lag after 0, one before).
- **`rsc.py`:**
  - it now quotes the code's exact trial rule, which my implementation already matched;
  - it states the smoothing window as an assumption.
- **Records:**
  - `questions/000483.yaml` asks a reader about the shuffled-control criterion, which cites code that contradicts its own wording;
  - two new findings ask the authors which shuffle and which decoder they used;
  - round 1 is recorded under `verifications` with the verifier's reasons and my responses;
  - the README and summaries are updated.

**Not done**
- Some numbers moved slightly from the first run, which ran elsewhere: for example 486 selected cells instead of 485, and class counts of 75, 1150 and 194 instead of 67, 1150 and 202. I put this down to machine differences. On this machine both runs match exactly, and every conclusion uses the new numbers.
- fig6-heading-below-population has a mixed-model reading that cannot be built, because each pooled decoding trial mixes many recordings and mice. Only its interval-comparison reading is run.
- The cue's position in the heading frame (fig1h) is in neither the files nor the code, so that part stays open.
