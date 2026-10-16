I've revised the entry for round 1. The entry re-ran cleanly with `python tools/entry.py all entries/000044-grosmark-2016` (0 errors, 664 s), and the conclusions match the new numbers. Round 1 is recorded under `verifications` in the attempt record. Nothing is committed.

**Outcome changes**
- **fig2d-shuffle-high-dpcc:** changed from blocked to partially_reproduced, as the verifier gave it. Its criterion ranks all place cells by dPCC and never uses the strongly contributing selection, so the block didn't apply. I changed its `depends_on` from fig2b-strong-contributors to place-cell-count and noted the change in the claims file header; no criterion changed. By the criterion, replay is absent after shuffling the top 10% and 20%, but also after shuffling the bottom 75% (p = 0.21).
- **Six claims kept blocked, disagreement recorded:** fig2e, figs2, fig3a, fig3b and both fig4a claims. Their rigid and plastic classes come from the strongly contributing selection, which is shown not to be the paper's. The new run also shows these results move with the contribution measure: the figs2 KS p went from 0.034 to 0.072.
- **The other 13 outcomes are unchanged**, and the verifier agreed with all of them. The record now has 3 reproduced, 3 partially reproduced, 6 not reproduced and 8 blocked.

**Corrections and added output**
- **PCC bias (problem 1):** each cell's 20 shifts are now drawn fresh for every event. The criterion's test still has a 0.561 false-positive rate (0.84 to 0.91 on the linear tracks, 0.14 on the circular track). So the bias comes mainly from scoring each event on the template with the larger rZ, not from reusing shifts. A new "best template" variant compares the larger |r| over the event's templates with and without the shift. Its false-positive rate is 0.206 and it finds 188 cells, against the paper's 216 (outside tolerance). It replaces the cell-level shift test, which only works with shared shifts.
- **Circularity in fig2d and fig2e (problem 3):** I added shuffles of a random 10, 20 and 75% of cells, a random-removal control, and a cross-validated control (cells chosen on even-numbered events, replay measured on odd-numbered ones).
  - On linear tracks, out of sample, shuffling the top 10% or 20% lowers replay from +0.116 to +0.046 and +0.042 but does not remove it.
  - Removing plastic cells still removes replay out of sample.
- **Pooling across tracks (problem 2):**
  - The fig1c test run on each kind of track finds POST above PRE on both the linear tracks (p = 5.1e-07) and the circular track (p = 1.1e-05); only the pooled test misses it.
  - I added a linear-track-only replay table for fig2d, fig2e, fig4d and fig4e. On linear tracks fig4d shows the criterion's partial pattern. The fig4e within-session pattern comes from the circular-track sessions.
- **Event pipeline check:** I added scored-event counts per session and epoch, and the MAZE rZ distribution for each session.
- **Smaller points:**
  - place-cell-count: the criterion's sentence about variants states the protocol's rule that variants don't decide the outcome. The notes now say the count depends strongly on the threshold (480 at 0.5 Hz is within tolerance).
  - The 50-shuffle base (problem 6) is now explained in the notebook.
  - scipy's Tukey HSD on ranks (problem 7) is recorded as a deviation.
  - The README and summary are updated, and `runtime_minutes` is now 11.

**Not done**
- **Supplement:** I tried again and still couldn't get it. Science and PMC serve it behind a browser check, and Europe PMC says the article is not open access. So the paper's PCC test and its event counts (figs. S2 to S4) can't be compared.
- **Problem 8 (MAZE immobility from 2D speed):** left unchanged; the verifier marked it as not affecting a conclusion.
- **Leftover gap on fig2b:** even the best-template test is above the 5% false-positive rate at alpha 0.05. At alpha 0.001 it is 0.031, but then it finds only 95 cells, far from 216.
