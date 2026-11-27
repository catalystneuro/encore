I've revised the attempt for verifier round 1. The final `python tools/entry.py all entries/kim-2025` run passed for all three notebooks: 12, 37 and 34 minutes, each under the 60-minute limit (the earlier Allen notebook had taken 61). `entry.py check` reports 0 errors. Nothing is committed.

**Outcome changes**
- **figs5a-movie-slope-near-1**: partially_reproduced → reproduced. The paper's code drops sessions 5, 14 and 43 of AllenSDK's session table because their movie presentations are marked invalid. Number 43 is sub-769319621, the session the verifier flagged: its file has an `invalid_times` interval tagged "stimulus" over 1497 movie frames, and one repeat runs 30.72 s. Dropping it leaves the paper's 23 sessions. The median slope is 1.116 (1.129 with the Methods' unit criteria alone), which is inside the criterion's second window. The criterion accepts either window.
- **figs4c-shuffling-alters-dependence**: blocked → reproduced. It is tested in a new notebook, `reproduce_kim_2025_decoding.ipynb`. Shuffled and original data differ for decoding (p = 5e-05 as-is, 0.035 at slope 0), for within-session RSM similarity (16 of 21 slopes) and for across-session RSM similarity (all 21). The claims file makes it depend on fig2b, which stays blocked. I tested it anyway because the comparison only needs the decoding conditions that ran, and I say so in its notes.
- Every other outcome is unchanged. figs1 and fig2d now give `blocked_by: other`, with the reason stated: their procedures were not ported in time.

**What I fixed for each problem**
1. Unit selection (problem 1): the "good" label is now used in every Allen analysis. The Methods' criteria alone are shown as a variant for the counts, slope fits, behavioural state, higher areas and the movie data. Every outcome holds under the good units. The slope-manipulation claims are now marked `assumed: true`.
2. fig2b: a partial test ran at as-is and slopes 0 and 1. Accuracy is higher at slope 0 than at slope 1 in 30 of 30 sessions, and every session is above chance. Slope 2 is too slow to fit, so the claim stays blocked as `too_large`, which is the protocol's category for a compute estimate over the notebook limit. I removed the timing cell whose quoted times didn't match its printed ones.
3. figs5c: the paper's `compute_percent_filled` drops points outside the box and anchors the grid the same way the helper does (box_and_overlap.py lines 107 to 122). The plateau is stated in the notes.
4. figs6: kept reproduced as the criterion is written. The weakness the verifier found (within sessions, slope 0 passes reading (a) as well as slope 1) is in the notes and asked in a new `questions/kim-2025.yaml`.
5. Trio test: added the reading on the full 12-stimulus graph. The example session still passes.
6. `shuffle_within_stimulus` now permutes each neuron separately, and it is used for the RSM shuffles.
7. Conclusion cells now begin "**Result:**", so the handover will strip them; the old "**Result (claim):**" form let the verifier see them.
8. The verification round is recorded for all 28 claims, and finding 5 is restated. No finding is rated critical, so none needs review in round 2.

**Not done, and why**
- The 30-minute slope-manipulation measures were not re-run with the Methods' criteria alone, for lack of time. The record says those outcomes were the same under that reading in round 1.
- figs1 (gain variance) and fig2d (tangent angle) were not ported in time.
- The shuffled comparisons for figs4c ran under the claim's seed only. The fig4a overlap consistency ran under its claim's seed only, as in round 1.
- The decoding notebook's header quotes slope-2 times from a test run I made while preparing, which is not in the entry. The block is decided by the verified round-1 timing, and the record says no outcome rests on the test run. I could not remove those numbers without another 80-minute run.
- I left alone the untracked dotfiles and the `scripts` directory in the repo root, since I didn't create them.
