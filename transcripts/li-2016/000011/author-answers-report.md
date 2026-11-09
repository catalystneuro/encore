I re-ran every claim the ten answers bear on and updated the notebook, helper, conclusions, summary and attempt record. Each claim's notes now say what its answer changed. Lock, check and run pass (the notebook runs in 1042 s, so I raised `runtime_minutes` to 18), and the handover is built in `executed/000011-li-2016/handover/`. Nothing is verified, committed or pushed.

Two outcomes changed: **cd-captures-selectivity** and **ed9f-reaction-time**. The other 22 affected claims came out as before.

**Q1, lick-early trials (K1 dropped, K2 kept; the outcome must hold under both).** Both readings were already run, so this mostly re-judged existing results.
- selective-fraction: partially_reproduced, unchanged; no reading reaches all four counts under either.
- ed4-return-to-trajectory: not_reproduced, unchanged.
- fig1f-spike-rate-recovery: reproduced, unchanged (0.101 dropped, 0.097 kept).
- ed2b-silencing-strength: partially_reproduced, unchanged.
- ed2e-no-rebound: not_reproduced, unchanged.
- ed7e-roc-larger-photoinhibition: partially_reproduced, unchanged.
- The convention A and convention D claims are covered under Q5 and Q2 to Q4.

**Q2 to Q4, convention D (preference window D1 to D3, bin label L1/L2, search end E1/E2; N1 per condition decides).** I added D3 (preference set in each bin) and E1 (search stops at the go cue).
- fig1g-selectivity-recovery: blocked, methods_underspecified, unchanged. Of 24 detail combinations, 12 have all three times within tolerance, 9 have two and 3 have none.
- fig2e-selectivity-recovery-times: not_reproduced, unchanged; it fails under all 24 combinations.
- fig2-recordings-recovery: partially_reproduced, unchanged, under all 12 combinations.
- ed7-larger-photoinhibition: blocked, methods_underspecified, unchanged. 10 combinations hold, all with centre labels; 14 do not, including every end-label one.

**Q5, convention A (rule as written, T1 decides; T2 is a variant).** Every claim's outcome is unchanged under T1 with K1 and K2. That is 24 sessions with 6 to 37 neurons, against the paper's 16 with 6 to 20.
- reproduced: cd-stable-over-epochs, fig3c-cd-predicts-movement, fig4-bilateral-cd-predicts-movement, ed9c-cd-window-robust.
- not_reproduced: fig3c-cd-recovery-roc, ed6b-session-bias-predicted.
- partially_reproduced: ed8-roc-during-photoinhibition.

**Q6, ed4 (paired or unpaired test s1/s2, 200 or 400 ms bins t1/t2).** not_reproduced, unchanged; it fails under all eight combinations.

**Q7, ed6a (Fisher table f1/f2).** reproduced, unchanged; it holds under both.

**Q8, modes.**
- Part 1 confirmed the ipsilateral split I already used. fig3d-persistent-mode stays not_reproduced.
- Part 2 added v2 (all correct control trials) to **cd-captures-selectivity**: was not_reproduced, now blocked as methods_underspecified. Under v1 cd captures 73.7% to 88.0% of the selectivity, outside tolerance. Under v2 the cd values fall within tolerance (66.2% and 34.6%), but the modes 1 to 5 values do not, which makes v2 partial.
- Part 3 added g2 orientation to fig3e-ramping-mode: not_reproduced, unchanged. The mode does ramp under g2, but under both orientations it predicts the lick above chance (55% to 58%).

**Q9, ed9f-reaction-time.** Was blocked as methods_underspecified, now blocked as **data_missing**. I added a reader that takes the first lick from `lick_trace` by byte range and ran ten thresholds.
- In the 24 experiment-2 sessions the trace holds no licks: on correct trials it rises only about 0.002 above baseline after the go cue.
- No rule detects licks on correct trials more often than on no-response trials.
- Reference sessions from experiment 3 and from the mice without a photostimulus record do show licks (73% to 100% of correct trials), so the reader itself works.
- The correlation holds under only 3 of 20 threshold and K combinations, on 3 to 10 trials. By the criterion's own rule that would also give methods_underspecified; I recorded data_missing as the main reason and this in the notes.
- I rewrote the lick finding as a data_missing finding.

**Q10, fig6-modular-models-recover (noise n1/n2, step h1/h2).** I added the 0.1 ms step. partially_reproduced, unchanged; all four combinations are partial.

**What to check:** the data_missing call on ed9f is my judgement, since the criterion's own rule would say methods_underspecified. Also, the attempt's `provenance.runner.url` still points to the earlier run, because I don't know this run's URL.
