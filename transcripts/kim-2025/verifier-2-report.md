# Round 2 verification: Kim & Shin (2025), attempt kim-2025-01

## 1. Outcomes and assumptions

The claims file has 28 claims and the attempt record has 28 outcomes:
- 24 reproduced
- 4 blocked: fig2b (too_large), figs1 (other), fig2d (other)

I agree with all 28 outcomes. Notes on the ones that depend on a reading:

- **The `assumed: true` outcomes.** These are data-v1-units, fig1b-across-neuron, figs4ab, fig1d, figs5c, fig2a, fig2c, fig3bc, fig3d, fig3e, fig3f, fig4a, fig4c, fig4d, fig4e, figs6 and figs4c. Each states its assumption: the "good" unit label, plus the dependence on a blocked claim for figs4c. The assumption is reasonable. The paper's counts match only with the label (nb2 cell 7). The slope measures were not rerun with the Methods criteria alone, but in round 1 they all came out the same under that reading.
- **figs5a: reproduced.** I agree, but the outcome should be marked `assumed: true`. The count of 23 sessions (tolerance 0) is reached only by reading the paper's code: AllenSDK's invalid-presentation rule and ascending session-id order. The record's own finding says the Methods' word "truncated" does not describe this. The reading is well supported: sub-769319621 is the only one of the 26 sessions with invalid-interval frames, its longest repeat is 30.719 s and its longest frame gap 0.133 s (nb2 cell 57).
- **figs4c: reproduced.** I agree. One caveat: original and shuffled decoding use different seeds (SEED_2B and SEED_4C in `decode_session`), so the trial order and folds also differ. The slope-0 difference (0.787 against 0.765, p = 0.035, nb3 cell 9) is small, from one seed, and could partly reflect fold noise. As-is (p = 5e-05) and both RSM analyses are robust.
- **figs6: reproduced under reading (a).** This is correct by the criterion, and the weakness is disclosed (nb2 cell 54).
- **fig2b: blocked as too_large.** The claim is blocked, which I agree with. I cannot check the category against the protocol.

## 2. Text checked against printed outputs

Unsupported or wrong sentences:

- **nb2 cell 0:** "(decoding at as-is and slopes 0, 1 and 2 only)". Slope 2 was not run (nb3 cell 6: "slope 2 not run").
- **nb3 cell 0:** "The times of this run are printed below." The four-session test run is not in the notebook; cell 5 prints only the 30-session times. The attempt record itself says that run is "not in the entry".
- **Record, fig2b notes:** "the 150 decodings took 14.1 minutes … (median 22 s as-is … up to 105 s)". Cell 5 of nb3 prints 14.4 min, an as-is median of 21 s, and maxima of 100 s (original) and 119 s (shuffled).
- **Record, figs3 notes:** "The counts over all 32 sessions match the paper's". nb2 cell 59 says the same ("the sessions per higher visual area match the paper"). RL is 28 against the paper's 27 (nb2 cell 18). It matches only after the paper's one excluded RL session, which the notebook does not apply.
- **Record, figs5a notes, and nb2 cell 58:** "these are the sessions whose files hold an invalid_times interval tagged stimulus that overlaps natural movie one". This is shown only for the 26 sessions in 000022 (cell 57). Nothing printed checks sub-718643564 or sub-719828686.
- **nb2 cell 8, record data-v1-units, and nb2 cell 59:** "the first and seventh by session id" and "removes the same two sessions as the paper's code". Cell 3 prints DANDI indices 0 and 9 only; the session-id order is not printed. I confirmed it on the archive in round 1.
- **nb1 cell 21:** "The same holds in each of the 12 sessions". This is supported for slopes 0, 1 and 2 (cell 20 table), but not "every 0.1 step" per session. This is minor.

Everything else in the "Result" cells, the three Summaries, the README and the record notes matches the printed numbers.

My round-1 reasons are stated faithfully in my own terms in `verifications.results`.

## 3. Round-1 points

Resolved:
- **1 (unit reading):** the "good" units are now used throughout; the slope measures are marked assumed.
- **2 (figs5a session count):** the third excluded session is identified; one residual item below.
- **3 (figs5c grid):** compute_percent_filled is cited and the plateau is described.
- **4 (figs6 criterion):** reported, and a reader has been asked.
- **6 (trio component):** a full-graph column is added.
- **8 (shuffle):** the shuffle is now per neuron and used.
- **9, 10 and 11:** addressed.
- **7:** needed no action.

Partly resolved:
- **5 (figs4c and fig2b):** figs4c is now tested and fig2b was run in part.

What remains that bears on a conclusion:
- **figs5a:** add `assumed: true`, and print the invalid_times check for the two sessions in 000021.
- **fig2b:** the too_large estimate rests on a test run that is not in the entry. Slope 2 alone was estimated at about 65 min on 4 CPUs, and in its own notebook it would have allowed the criterion's "partial" judgement.
- **figs4c decoding:** the seed confound at slope 0 described above. Using the same seed for original and shuffled decoding would settle it.

## 4. Critical findings

The record's `findings` list has none rated `critical`. Finding 1 is major, 2 is minor, 3 is none, and findings 4 and 5 (methods_unavailable) carry no severity.

None of them describes a data error that would qualify. Finding 3's no-defect statements are supported by the clock and duplicate checks in nb1 cells 3, 5 and 6.
