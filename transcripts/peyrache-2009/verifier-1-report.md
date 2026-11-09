**A. Outcomes** (29 claims in the claims file: 15 tested in the notebook, 14 treated as blocked)

| Claim | Outcome | Reason |
|---|---|---|
| sessions-and-cells | not_reproduced | Neither reading falls within tolerance. All sessions gives 86 sessions and 2155 cells; the inclusion rule gives 56 and 1499 (need 57–69 and 1523–1861). Per rat under the rule: 10/11/11/24, against the paper's 16/11/12/24 (cell 9). |
| rules-learned | not_reproduced | Both readings give right 3, lit 4, left 3, dark 1, against 4/4/2/1. Rat 18 never reaches the criterion under the right-arm rule (cell 11). |
| learning-sessions | not_reproduced | No reading gives 9–11 sessions over four rats: (a)(i) 34, (a)(ii) 16, (b)(i) 9 over 3 rats, (b)(ii) 4 (cell 13). Reading (b) is computed wrongly (problem 1), so this result is not final. |
| fig1b-signal-components | partially_reproduced | Signal total is 285, outside 291–355. Nonsignal is 730, exactly at the lower bound. 45 of 56 sessions have 1–6 signal components. Per session the rates match the paper (5.09 and 13.04 against 5.13 and 12.87) (cell 17). |
| fig2b-post-greater-than-pre | reproduced | Post exceeds pre in all three groups with p < 0.005 under both tests and both z readings (epochz t: 0.0015, 1.4e-4, 2.3e-4). Group sizes are 9/35/241, so two of the three expected counts are outside tolerance. That shortfall comes from fig1b (cell 19). |
| supp5-sws-only | not_reproduced | The state main effect has p = 0.0138, above the required 0.01. In non-SWS bins post exceeds pre significantly (paired t p = 0.042, Wilcoxon p = 0.018). The 30-min variant gives the same result (cell 21). |
| supp6-pre-post-sws-alike | partially_reproduced | No difference by paired t-test in total SWS (p = 0.87), episode duration (0.41), session-mean rate (0.93) or cell rate (0.65). SPWR rate, delta waves and LFP power are blocked (data_missing) (cell 23). |
| fig2b-encoding-correlation | not_reproduced | r² is 0.384 (epochz) or 0.417 (swsz), outside 0.549–0.671. p < 1e-30 and r > 0 do hold. r itself is 0.620, close to the paper's "r² = 0.61", which the claims file cannot settle (cell 25). |
| fig2b-pre-weaker | partially_reproduced | The pre slope and correlation are lower in both z readings. The correlation test passes 1e-5 (Steiger p = 6e-13). The best slope p is 3e-13, which misses 1e-20, so this falls under the criterion's partial clause (cell 27). |
| supp8-other-tetrode-pairs | blocked (data_missing) | There is no tetrode per cell; confirmed against the archive (section C). |
| fig2e-skewness | not_reproduced | Only the 1.4–1.8 group is significant (p = 0.009). The >1.8 group has a negative mean difference (−1.19, p = 0.62), and there is no rise with Phi under either z reading (cell 29). |
| fig2f-tail-contribution | partially_reproduced | At best, 2 of 3 groups fall in 36–55%: swsz (a) gives 51.0, 60.6 and 36.6%; swsz (b) gives 46.3, 45.8 and 5459%. The epochz readings give 1 and 0 of 3 (cell 31). |
| supp10-no-coactivation | reproduced | Reading (a): the post-SWS zero lag is below 0 and below the 200–500 ms mean, with its minimum at 0 ms, in both z readings. The awake zero lag is 0.033, above chance with p = 8.5e-16 (cell 33). |
| supp11-shuffle-control | partially_reproduced | Shuffled values are about 1/20 of actual in every group, so the magnitude part holds. They differ between pre and post in the >1.8 group (t p = 0.031, Wilcoxon p = 0.012) and in 1.4–1.8 by Wilcoxon (p = 0.023), so the absence part fails (cell 35). |
| fig5a-spwr-bins, fig5b-spwr-triggered, fig5c-peak-40ms, fig5d-population-asymmetric, fig5e-autocorrelogram | blocked (data_missing) | No ripple times or hippocampal LFP in the archive. |
| replay-in-delta-spindle-periods, fig6a-delta-waves, fig6c-spindles | blocked (data_missing) | No prefrontal LFP in the archive. |
| fig6b-down-up | partially_reproduced | Post signal components have significant bins at −0.5 to −0.3 s, nonsignal components have none, and pre is lower in that window (0.063 against 0.107). Pre's peak is higher than post's (0.145 against 0.132), and the per-component post-minus-pre difference is not significant (p = 0.15). The SPWR part is blocked (cell 37). |
| fig6d-reactivation-spwr-correlation | blocked (data_missing) | Needs ripple times. |
| fig7b-post-spwr-after-learning, fig7b-controls, fig7c-choice-point, fig7d-two-factors | blocked (data_missing) | All templates come from SPWR or inter-SPWR bins, and there are no ripple times. |
| supp12-behavior-unchanged | reproduced | Trial length shows no difference: (b) paired p = 0.158, (a) p = 0.278. The test has little power (+2.7 s, n = 10), and the sessions come from the data set's description, not from learning-sessions (problem 3) (cell 39). |

**B. Problems**

1. [affects a conclusion] `pfc6.learning_point` with `include_block=False` returns None when the qualifying block of correct trials runs to the end of the session, because an empty remainder fails `len(rest)`. I confirmed this on a synthetic input: `[0,0,1,1,1,1,1]` gives 3 under (a) and None under (b). So reading (b) drops exactly the sessions that end in a clean run: 7 of the description's 10 learning sessions are NaN under (b) in cell 13. Counting the empty remainder as passing could move (b)(i) or (b)(ii) into 9–11 sessions over four rats, so learning-sessions is not settled under reading (b).
2. [does not affect a conclusion] In cell 37 (`down_up_times`), readings (a) and (b) give identical outputs. With 10 ms bins the mean count per bin is below 5, so "below a fifth of the mean" means a count of zero, and reading (b) is the same as (a). The notebook does not say so.
3. [does not affect a conclusion] Cell 39 (supp12) takes its learning sessions and trials from the data set's description, not from a reading of learning-sessions, which this claim depends on and which did not reproduce. The cell does say this. The description's points also disagree with every computed reading for 181020, 201222 and 201227 (cell 13).
4. [does not affect a conclusion] The module docstring of `pfc6.py` says rest epochs are bounded by the first and last spike. `rest_epochs` actually uses 0 and the end of the position record. That bound changes only the epochz values and supp5's non-SWS bins. supp5 fails under the 30-min variant too, and swsz results do not depend on it.
5. [does not affect a conclusion] Cell 21 (supp5) runs an ordinary two-way ANOVA on four non-independent means per component. A repeated-measures form could bring the state effect below 0.01, but the significant post > pre result in non-SWS bins still fails the claim.
6. [does not affect a conclusion] fig2f reading (b) and supp10 reading (b) divide by near-zero means, giving values like 5459% and a zero-lag ratio of −337 with s.e.m. 430. The cell 33 printout calls supp10 (b) "below chance: True", which is meaningless here. The supp10 outcome rests on reading (a), and the fig2f count rests on values that are well defined.
7. [does not affect a conclusion] `session_reactivation`/`template` count the 12 cells that are silent in the awake epoch in n. That lowers q and raises λmax slightly, which biases the signal count in fig1b down a little.
8. [does not affect a conclusion] Cell 9's 3.5-min SWS variant gives 63 sessions and 1682 cells, matching the paper's totals but not its per-rat counts. fig1b was not run under it; at about 5.09 signal components per session it would likely land inside tolerance. Two of the description's learning sessions (201227 with 2.2 min of pre SWS, 201229 with 3.3 min of post SWS) fail the 4-min rule, although the paper's Figure 7 uses them. This suggests the deposited SWS intervals or the inclusion rule differ from the paper's. The notebook does not mention it.
9. [does not affect a conclusion] Cell 39 shows a speed difference in path bin 0 (p = 0.034, uncorrected) without comment. Its path-fraction bins are not the paper's linearized maze.

Helper checks on synthetic inputs all passed: `reactivation` against a brute-force sum, `shuffle_expected_R` against an exact average over all permutations, `reached_criterion`, the lag sign of `xcorr_runs`, and `in_intervals`. The awake template is applied only to pre and post data, so there is no train/test leakage.

**C. Not checked, and what would settle it**

- **Blocked claims:** the S3 listing for pfc-6 has only `mPFC_Data.tar.gz`, the description (.pdf, .docx), `Load_And_View_Data_Examples.m`, `filelist.txt` and `checksums.md5`. The tarball's first entry is `SpikeData.dat`, and `load_sessions` would raise a KeyError on any file outside the seven kinds, so there is no LFP, ripple, delta or spindle data and no tetrode map. None of the blocked claims can be tested in part.
- **learning-sessions:** cell 13 rerun with an empty post-block remainder counted as passing under (b).
- **fig1b and fig2b:** signal and nonsignal totals and group sizes under the 3.5-min variant.
- **rules-learned:** for each rat and rule, the longest correct run and the best 12-trial window, to show whether a missing session or the criterion causes the mismatch.
- **supp5:** a repeated-measures ANOVA.
- **fig6b:** the lag of the one significant pre bin and the full pre profile.
- **Figures:** the plots were not viewable as images, so the plotted ranges were the only figure output I checked.
