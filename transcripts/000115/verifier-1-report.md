**Verifier report: Gillespie et al. 2021 on DANDI:000115 (0.210914.1732), round 1**

The claims file lists 33 claims. The notebook tests 2 of them, both behavioural, and treats the other 31 as blocked.

### A. Outcomes

| claim id | my outcome | reason |
|---|---|---|
| fig1d-sessions-blocks | reproduced | Cell 15. Under reading (a), sessions are 25/32/24/33 against 24/32/23/33 and blocks are 88/85/109/166 against 89/85/105/166, all within tolerance. Under reading (b), jaq has 25 sessions and 91 blocks. All 26 candidates for the unidentifiable first excluded jaq session pass (jaq blocks 88–93, tolerance 80.1–97.9), so (a) and (b) agree. |
| fig1ef-reward-rate | reproduced | Cell 17. The 1E trial-1 band reaches or lies below 0.125 in all subjects (lower bounds 0.041 to 0.106). Trial 15 is far above trial 1 (Spearman ρ ≥ 0.94, p ≤ 1.4e-7). The lowest 1F lower bound is 0.234 (roquefort), above 0.125. This holds under every reading and all 26 jaq candidates. The chance level is 1/8, the same as the paper's 0.125. Note that jaq (0.068) and roquefort (0.094) start below chance, not "at" it; the criterion's "or lies below" allows this. |
| figs1c-swr-reward-consumption | blocked, too_large | No ripple, LFP or spike data. The API asset summary lists only `ElectricalSeries` and `Position`. Ripple detection would have to start from the 9.1 TB raw broadband (cells 12–13). CA1 tetrodes also cannot be identified (every location is "None", cell 3), which is a secondary metadata_insufficient reason. The time spent per trial phase could be computed from the logs, but the criterion needs SWR counts and rates. |
| figs3abc-decode-accuracy, figs3df-goal-arm-no-remapping, figs3g-continuous-fraction, likelihood-decode-same-segment | blocked, too_large | These need the clusterless decoder run on spikes taken from the raw broadband. The streaming rate measured in cell 12 makes this far too large. I confirmed in the archive that no derived data exist. |
| fig2f-remote-fraction, fig3a-box-majority, fig3b-search-prevgoal-enriched, fig3b-search-past-depleted, fig3b-search-future-inconsistent, fig3b-search-other, fig3c-repeat-prevgoal | blocked, too_large | All need SWRs plus decoded replay content. Neither is in the dandiset. |
| fig3d-glm-search, fig3e-glm-repeat, fig4ab-current-goal-late, fig4c-current-goal-reward-correlation | blocked, too_large | Same reason: the response variable is replay counts. |
| fig5a-future-replay-rate, fig5b-future-correct-error, fig5c-current-goal-correct-error, figs7-early-late-correct-error, figs7e-remote-rate-error, fig5d-glm-predict-chance | blocked, too_large | Same reason. The legends' trial counts (e.g. 534 search trials; 923 correct and 424 error) could be checked from behaviour, but those counts are not the claims. |
| pg-replay-visits-correlation, fig5e-pg-replay-no-avoidance, fig6a-pg-replay-persists, fig6c-pg-replay-two-blocks, fig7-recency, fig8-outer-prevgoal, figs8-outbound-final-events, robustness-controls | blocked, too_large | All rest on replay content, or on MUA events taken from the raw data. |
| fig6b-visits-decay | blocked, too_large (in part testable) | The visit-decay half is behaviour only and can be computed from the logs: goal against non-goal visits per trial, a rank-sum test with Bonferroni correction, and the +3/+5 bounds. Only the comparison with the fig6a replay extent is blocked. The notebook (cell 19) blocks the whole claim and never computes the testable part. |

### B. Problems

1. **[does not affect a conclusion]** Cell 6/7: the text says rewards per completed block "take only the programmed values". The table it prints contradicts this: one jaq block has 9 rewards (programmed values 10 or 15) and one montague block has 3 (programmed range 4–12 or 15). These blocks were not investigated. They could be log truncation (see problem 3) or a labelling edge case.
2. **[does not affect a conclusion]** Cells 6/7: "No epoch sets forage assist" is only checked for 111 of 116 logs. Five logs have no Python header (despereaux day 4 ep 2; jaq day 6 ep 2, day 13 ep 2, day 14 ep 2, day 15 ep 2), so forage assist is unknown for them. Excluding all five still leaves jaq at 22 or more sessions, within tolerance.
3. **[does not affect a conclusion]** Cells 11/12: reading (b) names jaq day 6 ep 4 as the session where "not all arms were visited" (7 arms). That count comes from the log, and cell 7 itself says this log appears to stop early (an extra DIO pump 226 s after the last logged reward). The DIO beam breaks were not used to confirm that the eighth arm was never visited. The outcome holds either way, because reading (a) and all 26 (b) candidates pass.
4. **[does not affect a conclusion]** Cells 4/15: the dandiset holds one more run session than the paper for jaq (27 against 26 before exclusion) and for despereaux (24 against 23). The extra sessions are not identified. Candidates include jaq day 7 ep 2 (6 rewards in 74 valid trials, no `outerreps` printed) and epochs shorter than the 45-minute minimum in the Methods (jaq day 9 ep 6, 33.9 min; despereaux day 4 ep 4, 39.2 min). Session and block counts stay within tolerance, but the "full-task session" selection is assumed rather than checked.
5. **[does not affect a conclusion]** `label_task_phase`: an "adjacent arm" error is `abs(o-g)==1`, which does not wrap from arm 8 to arm 1. On a synthetic test, goal 1 visited at arm 8 is labelled n+0.8, not n+0.5. The tested claims depend only on integer phases and reward flags, so they are unaffected. It would matter for any later correct/error subtype analysis.
6. **[does not affect a conclusion]** Cell 17: `E_rises` (trial-15 lower bound above trial-1 upper bound, plus a Spearman test) is the author's own way of reading "rises"; the criterion only says "the rate rises". It is stricter than the criterion and passes easily.
7. **[does not affect a conclusion]** Cell 19: fig6b-visits-decay is blocked as a whole, although its behavioural half is computable from data the notebook already loaded (see the table).

**Synthetic tests.** I ran `label_task_phase`, `full_blocks`, `reward_curves` and `trials_from_events` on hand-built trial and log sequences. They behave as the claims file's opening comment specifies:
- The first valid trial after a switch stays in the old block, as n+0.9 at the old goal or n+0.x elsewhere, including when a lockout sits in between.
- Repeat search visits get -0.2.
- The closing trial is dropped from both curves.
- A WHITENOISE after CURRENTGOAL becomes a lockout trial.

The log-to-DIO checks in cells 6 and 8 (reward counts in 115 of 116 epochs; rewarded exactly when the visited arm is the printed goal, over 9,711 trials) support the trial reconstruction.

### C. What I could not check, and which output would have let me

- **The task-phase labelling against the paper's own trial counts.** The paper's code was not available to me, so I could not check how it handles adjacency or the "full-task" flags. Printing per-subject counts of search trials after the first block, repeat trials, and correct and error repeat trials would allow comparison with the legends (534/617/570/879 search; 923/1007/847/1340 correct; 424/654/307/390 error; 711/848/725/1065 search GLM trials).
- **Which dandiset sessions the paper did not use.** A per-session table of blocks with the header and forage flags, the rewards per block, and the anomalous 9- and 3-reward blocks would have settled this.
- **Arms visited in jaq day 6 ep 4.** Arms visited per jaq session counted from DIO beam breaks, not only the log, would have settled it.
- **The behavioural half of fig6b-visits-decay.** The per-trial goal against non-goal visit curves, with Bonferroni-corrected rank-sum tests and the last significant trial after the switch, would have let me judge that part.
- **The 1E/1F values.** The per-trial values (p, S.E.M., n for trials 1–15) for each subject would have let me read every point, not only the summary columns.
