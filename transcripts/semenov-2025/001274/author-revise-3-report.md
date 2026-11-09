The numbers in the executed notebook match the text. All done.

**Outcome changed**
- **fig3c-sustained-firing-2s** went from `not_reproduced` to `reproduced`, marked `assumed: true`. The `proposed` block is gone. The verifier agreed in round 3 on the condition that the outcome be marked assumed.
- A new deviation states the assumption: part (iii) is read as "no more detections after 250 ms than the noise of the corrected trace gives".
- The notes, the notebook's result cell (cell 60), its summary table, and the README row now give the new outcome. They also carry the verifier's caveats:
  - Read literally, (iii) still fails (5 peaks under reading (a), 1 under reading (b)).
  - The claims file's criterion makes no allowance for false detections on a plateau.
  - The test rests on neuron c7 alone.
  - The other three neurons reach no block.

**Proposals still standing:** none. This was the only one, and the verifier agreed with it. No other outcome changed.

**Record:** round 3 is added under `verifications`, with one result for fig3c: it agrees, its outcome is `reproduced`, its reason is in its own words, and my response is included. The verifier says the criterion's missing allowance is not a misreading of the paper, so I did not add a question to `questions/`.

**Run:** `python tools/entry.py all entries/001274-semenov-2025` gave 0 check errors, and the notebook passed in 1280 s. The fig3c outputs (0.94% residual SD, 6 and 7 detections on the mirrored trace, Gaussian means 7.8 and 5.1, 8 to 10 APs in part (i)) match the text.

`tools/build_site.py` was already modified before this run. I left it untouched, and nothing was committed.
