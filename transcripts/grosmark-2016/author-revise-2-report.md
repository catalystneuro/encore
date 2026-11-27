No outcome changed: round 2 does not allow it. I proposed two changes for a third verification round and added the analyses the verifier asked for. The entry was re-run twice with `python tools/entry.py all entries/grosmark-2016` and passes with 0 errors. The two runs print identical numbers apart from timings, and every conclusion matches them.

**Proposed changes (under `proposed` in the record)**
- **fig4e-gain-sequences**, partially reproduced to not reproduced: the criterion has no partial outcome, and the low-gain group also rises under 5 of 6 readings (main reading p 0.0163).
- **figs16de-more-ripples-post**, partially reproduced to not reproduced: no partial outcome, and the ripple-event medians (2.424 and 1.944 s, against 3 and 2.47 s) are outside tolerance.

**New analyses**
- **Kernel reading carried downstream** (new cell `kernel-width-classification`). With the 5 cm kernel read as its full width instead of its SD, there are 507 place cells instead of 573. Under the main direction reading this gives:
  - fig2b-strong-contributors: 232, 102, 200 and 70 cells, all four within tolerance.
  - rigid-plastic-counts: 112 rigid and 112 plastic, within tolerance.
  - fig2-pre-post-overlap: 68.6%, which does not change its outcome.

  So three outcomes (with place-cell-count) turn on the kernel reading. The claims file says that choice "should not change outcomes", so I added the question for a reader in the new `questions/grosmark-2016.yaml`. The outcomes stay as tested on the claims file's SD reading, and I proposed no change, since the claims file decides that reading.
- **figs11 effect sizes** (new cell `figs11-effect-size`). The quality measure sits at 1.02 to 1.06 times its value under the Gaussian expectation (the chi median), so it has little room to differ. The tests rule out differences larger than about 2.5% of the median. The notes now say the absence says little, and the outcome stays reproduced as the criterion gives.
- **Finding 4**: cell 12 now prints the NWB lap trials and their directions for each session, so the finding's cell shows its whole statement.

**Corrections**
- fig4a: 5 of 8 sessions, not 6 of 8.
- figs5e: the test is not significant under four readings, not three, and the overstated "the yoking reading decides the test" is gone.
- fig1c: both bootstrap intervals are given, with a note that they are two draws.
- figs11: streaming time is now given as 142 to 203 s over three runs.
- Finding 7 now names the four claims whose outcome flips under the other direction reading.
- The notes for fig2d and the Summary say the pass also rests on reading (a) of "eliminated". The Summary and README list the outcomes that each turn on one assumption.

**Recorded**
- Round 2 under `verifications`, with all 36 claims, the verifier's reasons in its words and my responses. No finding is rated critical, so the round has no `findings` entries. I said so under `reviewed`.
- In the round-1 entry, figs11 is now `agrees: false`, as the verifier asked, and a note says its cell numbers refer to the round-1 notebook.

**Not done, or not settled**
- The fig4d and fig2e values the verifier quoted (0.046, -0.00964 and so on) differ in the third digit from my runs, which match the record. The seeded draws do not explain this and I did not find the cause. I recorded it as a difference from the paper's method; the outcomes are the same either way.
- The width reading was carried only to the three counting claims. The later rigid-against-plastic claims still use the SD reading's groups.
- I kept the yoking reading Y-a and did not change fig2d. Under reading (a) of "eliminated" it also passes with Y-b, and fails only under Y-c with D-b.

Nothing was committed.
