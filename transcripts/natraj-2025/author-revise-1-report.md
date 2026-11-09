I've revised the attempt for round 1. The final run of `python tools/entry.py all entries/001535-natraj-2025` gave 0 errors and the notebook ran in 495 s. Nothing is committed.

**Outcome changes**
- **figs3-spatial-pooling:** still blocked, but the reason is now `metadata_insufficient` (it was `data_missing`), as the verifier said. The file has no electrodes table, so the channels can't be placed on the 8x16 grid. The notebook now runs the variance variant the verifier described on all 1357 right-thumb trials. Pooling lowers the median variance under row-major order (z = 7.05), column-major order (z = 7.12) and every one of 200 random layouts (z 7.40 to 8.05). So the effect comes from averaging alone, can't test anything about the grid, and the claim stays blocked.
- **rnn-training-data-amount:** stays reproduced and rests on an assumption, as the verifier agreed. The 9737 trials total 837.4 min against 888 ± 88.8. The match only holds if the 1886 robot trials count; the virtual trials alone are 540.0 min.
- **The other 50 claims:** unchanged and blocked. For fig4cd, fig4cd-demeaned, figs8ab and fig4fg, the verifier would give `metadata_insufficient`. I kept `data_missing` because they also need B3's data or the band-power features, which the dataset doesn't hold. The response for those claims says why.

**Added outputs**
- **The two Methods passages:** the notebook now quotes both. One counts the robot practice in the 14 h 48 min; the other trains on the virtual data and fine-tunes later on the robot.
- **Durations:** broken down by context and target.
- **Trial-id order:** all virtual trials come first (ids 1 to 7851), then all robot trials. Nothing says the ids follow recording order, so this doesn't settle which data the robot trials are.
- **High-gamma time course at trial start and end:** it doesn't support the verifier's guess that the stored trials are already the active portions. Virtual trials stay low for the first 0.4 s and robot trials don't. Dropping 0.5 s from each virtual trial would give 771.9 min, outside the tolerance. The conclusion, the claim notes and the findings now say this.
- **Full listing of the acquisition group:** it holds exactly the 9737 trial series and nothing else.
- **Header table:** lists every blocked claim by id with its reason.

**Corrections**
- **Shifted-label check:** I had first written that neighbouring trials often share a target. The data show the opposite: 0.105, against 0.136 if each context were in random order. The text now says the trial order isn't random.
- **Duplicate check:** the data check now says it can't catch a trial deposited twice with different trimming.
- **Helper module:** `bci.py` now keeps the trial-edge time courses and 200 ms bins, and has the pooling functions.
- **Other files:** `scipy` is added to `requirements.in`; the lock changed only in a comment. The README is updated.

**Question for a reader:** the verifier said the claims file underweights the robot-trial ambiguity. I added this to the new file `questions/001535.yaml`. It asks whether the totals with and without robot trials, and readings (a) and (b), should have to agree. The claim itself is unchanged.

**Attempt record:** round 1 is under `verifications`, with all 52 claims, the verifier's reasons in its own words, and my responses.

**Not done**
- I didn't rebuild the verifier's handover package, since round 2 gets the full executed notebook.
- The untracked dotfiles and `scripts/` at the repository root came from neither this run nor the earlier author runs, and I left them alone.
