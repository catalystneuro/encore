I checked the claims file for DANDI:000231 against the paper and made 13 corrections and one addition. The file is ready for an attempt.

**Checker:** `claims/000231/10.1038-s41597-022-01728-1.yaml: 39 claims, 39 quotes, 0 statistical values, 0 problems`. It was 38 claims before I added one.

**Changes, by claim:**
- **Wrong paragraph pointers fixed:**
  - `dataset-size` and `neural-hours`: Background & Summary paragraph 5, which is not the last paragraph; High-speed videography paragraph 2.
  - `servo-positions`: Two behavioral tasks, paragraph 2.
  - `response-window-timing`: paragraph 3.
  - `outcome-consistency` and `reward-and-timeout`: paragraph 4.
  - `c0-rare-contacts`: paragraph 5.
  - `subjects-sex-age-strain`: paragraph 7.
  - `video-timebase`: Alignment of multiple data streams, paragraph 4.
  - `prior-task-strategies`: Background & Summary, paragraph 4.

  The paper's text file has no paragraph breaks, so I counted them in the preprint, whose wording is the same in these places.
- **`servo-positions`:** the criterion required all three positions in every session, which the paper never says. Now only the set of positions decides the outcome, and positions per session are just reported.
- **`response-window-timing`:** the criterion judged an order of close, medium and far "as the paper gives", but the paper does not say which position arrives first. The order is now reported and not judged.
- **`unit-quality-isi`:** the outcome rule did not cover the firing-rate part failing under both readings. That case is now "not reproduced".
- **`units-obs-intervals`:** the criterion only asked that the interval lie inside the recording, which is weaker than Table 5 (the interval is the recording's start and stop). It now asks that the ends match; lying inside counts as partial.
- **`prior-task-strategies`:** the statement and quote left out the barrel cortex tuning half of the paper's sentences. Both now include it.
- **`prior-orthogonal-subspaces`:** added. This was the paper's other stated earlier finding on these data (ref. 10) and had no claim. It is blocked because the paper gives no method for it.

**Still open (recorded in `checks`):**
- The abstract says the neurons "responded with precise timing to whisker contacts and motion". Nothing in the main text or legends states or measures this, so it has no claim.
- Several pass/fail thresholds were chosen by the first agent, not taken from the paper (for example 99%/95% agreement, "more than half the sessions or mice", within 1% of 30 kHz, and the sex-ratio readings). Each criterion says the paper gives no threshold, and I kept them.
- The three tracking-accuracy claims need the hand-labelled training frames and the network's held-out predictions. The paper does not list these among the deposits, so those claims will probably be blocked.

**Ready:** `ready: true`. Only that one file changed, and nothing was committed.
