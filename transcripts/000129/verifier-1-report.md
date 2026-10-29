**A. Outcomes** (31 claims in the claims file; the notebooks test 18 and treat 13 as blocked)

| Claim | My outcome | Reason |
|---|---|---|
| units-monkey-i | not_reproduced | 111 units above 0.5 Hz, outside 153.9 to 454.3 (nb1 cell 18). The file has no hash units (ids end in 1 to 4, 82 channels), and its session date, 2017-02-02, is not in the paper's list (cell 5). Adding hash units could reach the range, so this does not contradict the paper. |
| fig2-refh-kf-best | blocked (data_missing) | The bootstrap needs 49 sessions. The mean part is testable on one session and holds: rEFH (+KF) is highest for pos, vel and acc (5.90, 5.16, 2.37; nb1 cell 14). The notebook does not report this. |
| intro-gain-over-nearest | blocked (data_missing) | The p-value needs sessions. The gains are testable on one session but not reported. Reading (b), UKF: 0.27, 1.34 and 1.26 dB, so position and velocity fall outside tolerance. Reading (a): acceleration is 1.03 dB (over WF). Neither reading gets all three gains within tolerance. |
| fig2-velocity-boost | not_reproduced | KFobs ratio is 1.97, below the required 2; UKF ratio 1.55 is inside 1.5 to 2.2 (cell 20). Only the UKF part holds, which the criterion does not count as partial. It is borderline: the rEFH seeds give 1.92 to 1.99, and the code-kinematics variant passes (2.12). |
| fig2-kflatent-dynamic-little-effect | reproduced | Differences of 0.18, 0.21 and 0.09 dB, all under 0.5 (cell 22). Also holds with code kinematics. |
| fig2-refh-static-vel-acc | reproduced | Static rEFH beats the best other decoder by 0.12 dB for vel (UKF) and 0.53 dB for acc (WF). Holds for all seeds and variants (cell 24). One session only, and the velocity margin is small. |
| fig2-position-dynamic-gain | not_reproduced | Gain is 4.41 dB against 3 ± 0.5. Every seed and variant gives 4.38 to 4.45 (cell 26). |
| fig2-sagittal-better | reproduced | y beats x in 24 of 24 pairs; one rEFH seed gives 23 (cell 28). The static rEFH velocity and linear velocity margins are only 0.01 to 0.04 dB. |
| fig2-linear-worst | reproduced | Every decoder is above linear regression for every variable; smallest margin 0.46 dB (cell 30). |
| fig2-gross-failures | reproduced (vacuous) | No negative R2 at 64 ms (cell 32), so the criterion holds trivially. See problem 9. |
| fig4-vel-acc-every-session | partially_reproduced | The per-session part holds: 8 of 8 comparisons favour the rEFH (+KF), smallest margin 1.08 dB across seeds (cell 34). The across-session bootstrap cannot be tested (one session). |
| fig4-advantage-grows | blocked (data_missing) | The regression is over sessions and axes; one session gives two points. Archive confirmed below. |
| fig4-position | blocked (data_missing) | Bootstrap needs sessions. The point differences are testable but not reported: +0.90 dB over KFobs and +0.27 dB over UKF. |
| fig4-best-variable | not_reproduced | Position is the best variable for rEFH (+KF) (5.90 vs 5.16), and this holds for all seeds and the code reading (cell 36). |
| fig4-task-similar | blocked (data_missing) | Monkey C is not on the archive, and there is only one monkey I session. |
| fig5-vel-acc-all-bins | blocked (data_missing) | Bootstrap needs sessions. The point estimates are testable but not reported: at 16 ms the WF beats rEFH (+KF) for vel (3.30 vs 2.96) and acc (1.39 vs 0.95). The direction holds at 32, 64 and 128 ms. |
| fig5-position-bins | blocked (data_missing) | Only the direction can be tested: UKF exceeds rEFH (+KF) at 16 ms (4.68 vs 4.42). The "no difference" parts need the test. |
| fig5-advantage-with-binwidth | reproduced | rEFH (+KF) SNR and its advantage both rise under both readings (nb2 cell 8). |
| fig5-derivative-order | partially_reproduced | Holds at 3 of 4 widths; fails at 16 ms (nb2 cell 10). |
| fig6-training-time | blocked (data_missing) | Part (ii) needs the test. On point values, (i) holds at 80, 160 and 320 s. For (iii), rEFH (+KF) is above KFobs at 320 s (5.90 vs 5.00) and below it at 80 s (2.48 vs 2.73), as the paper says (nb2 cell 6). |
| fig7-vel-acc-neurons | blocked (data_missing) | Bootstrap needs sessions. On point values, velocity at f = 1/4 ties the WF (1.56 vs 1.56). The percent gain in acc over the best rival falls from f = 1/2 (about 95%) to f = 1 (78%). |
| fig7-position-neurons | blocked (data_missing) | Only the direction can be tested: rEFH (+KF) is highest at f = 1/4 and 1/2. |
| fig7-affine-position | not_reproduced | All rho values are within tolerance, but the lowest is WF under reading (a) and static rEFH under (b), never static KFlatent (nb2 cell 14). |
| fig7-kinematic-model-saturates | reproduced | Holds under reading (b) (1/8 to 1/2); fails under (a) (nb2 cell 16). See problem 10. |
| fig8-velocity-variants | not_reproduced | Losses of 0.21 and 0.05 dB against the text's 0.7 and 0.4 (and the figure's about 0.3 and 0.4) (cell 40). The dynamic part holds (0.25 and 0.27 dB). |
| fig8-position-variants | blocked (data_missing) | The dynamic part needs the test. The static part holds on this session (1.49 > 1.43 and 1.41), but the notebook does not mark it. |
| fig8-gaussian-still-beats-ukf | reproduced | Standardized-count variant (paper l. 1122, "standardizing ... separately for each neuron"): +1.07 dB vel and +1.13 dB acc over the UKF (cell 42). The code-transform variant fails (−0.37 vel). |
| fig9-taps | blocked (methods not run) | No tapped decoders are implemented. Parts (i) and (iii) are single-session comparisons that could have been tested; only (ii) needs sessions. |
| kflatent-modest | reproduced | Holds under readings (a) and (b), fails under (c) (cell 38). The KFlatent margin is 0.10 dB from one EM run (problems 1 and 5). With code kinematics only (c) holds. |
| advantage-grows-with-derivative | reproduced | Percent advantage rises pos < vel < acc at 80, 160 and 320 s, under both test-set readings (nb2 cell 12). |
| static-refh-position-worse | blocked (data_missing) | The test needs sessions. The direction holds strongly: static rEFH 1.49 vs UKF 5.63 dB. |

Archive check: I queried the DANDI API for 000129 at version 0.241017.1444. It holds 2 assets and 1 subject: a training file and a test file whose behaviour is withheld. No other sessions, monkey L or monkey C are present, so every claim that needs a bootstrap or regression across sessions is data_missing. Fig9-taps is the exception: it was not run, but its point comparisons are testable.

**B. Problems**

1. [affects a conclusion] `lgds_em` stops when the gain is below `tol*1e-2` with `tol=1e-4`, a threshold of 1e-6. The paper (l. 364) and the docstring say 1/100 of a percent, which is 1e-4. On a synthetic LGDS it ran to the 100-epoch cap with a relative gain of 4.4e-6, where the paper's rule would have stopped earlier. Epoch counts are never printed. This affects KFlatent results, and kflatent-modest rests on a 0.10 dB margin.
2. [affects a conclusion] Blocked claims with parts testable on one session were not evaluated (cell 0 table): fig2-refh-kf-best, intro-gain-over-nearest, fig4-position, fig5-vel-acc-all-bins, fig5-position-bins, fig6-training-time, fig7-vel-acc-neurons, fig7-position-neurons, fig8-position-variants and static-refh-position-worse. This is inconsistent with testing other mean claims on one session. Some of these point estimates go against the paper: the 16 ms WF advantage, intro-gain velocity at 1.34 dB, and the fig7 acc percent falling.
3. [affects a conclusion] fig9-taps: the tapped rEFH and UKF are never implemented in `makin.py`. The stated block reason, "bootstrap", covers only part (ii).
4. [affects a conclusion] Mean-over-49-session claims are graded on one session. The claims header says only per-session statements can be checked on a single session. The notebook labels this a deviation, but outcomes with small margins carry one session's noise: fig2-velocity-boost at 1.97 vs 2, and the kflatent-modest and fig2-refh-static-vel-acc margins. The session is also outside the paper's list and has no hash units (111 units vs 171 to 413), which per figure 7 lowers SNR.
5. [affects a conclusion] Only the rEFH seed is varied (cell 16). The KFlatent EM/FA seed is never varied, so kflatent-modest rests on one EM run at a 0.10 dB margin. The fig8 standard-normal loss of 0.05 dB is within the 0.13 dB rEFH seed spread; this does not change that verdict.
6. [does not affect a conclusion] `dec_ukf` re-implements the UKF; Li's UKF2 package is not used. This is stated as an assumption and looks reasonable, but the UKF is the reference in several claims and was not checked against the original.
7. [does not affect a conclusion] `dec_wf`: at the start of the test set the WF history is zero-padded instead of using the last training bins. At most 6 bins are affected.
8. [does not affect a conclusion] `kinematics`: the 1 kHz series is reduced to 250 Hz with `[::4]` at an arbitrary phase, and forward differences reach about 4 ms past the bin end. Synthetic test: speed and acceleration come out correct (157.08 vs 157, 493.5 vs 493 mm/s and mm/s²). Bin counts and alignment are also correct. The KF information-form update matches a covariance-form KF to 3e-14, and the duplicate-unit filter works.
9. [does not affect a conclusion under the criterion] fig2-gross-failures: outside 64 ms, negative SNR (that is, negative R2) appears for linear regression, static KFlatent and static rEFH at f = 1/8, and for linear regression acc at 80 s (nb2 cell 6). The paper says "in our experiments"; the claims file's restriction to 64 ms may be a narrower reading than the paper's.
10. [does not affect a conclusion] fig7-kinematic-model-saturates passes under reading (b) partly because of KFlatent (+KF)'s failure at f = 1/8 (−2.56 dB). KFobs, UKF and rEFH (+KF) all drop from 1/8 to 1/4.
11. [does not affect a conclusion] fig5-derivative-order: the claims criterion drops the paper's clause "except for the rEFH, which is best at velocity". That clause fails at every width (nb2 cell 10, `refh_kf_best_var` = pos), consistent with fig4-best-variable.

**C. Not checked, and outputs that would settle it**

- The rbmish code details (WF refit on 80%, rEFH learning schedule, the filterDecoder penalty, SLMD) are not in my materials. Line references to the code would let me check them.
- `refh_decode` uses ridge penalty (nv/ns)^(10/3), about 0.005 for about 1000 features on 5000 bins, which is effectively unregularized. The second KF's noise is fitted on in-sample static outputs. This may inflate the dynamic position gain (4.4 vs 3 dB). Printing training-set vs test R2 of the static rEFH map would settle it.
- KFlatent EM epoch counts and log-likelihood traces per configuration.
- Per-decoder R2 tables for the 16 ms, 80 s and fraction configurations, to attribute the negative R2 values.
- KFlatent results under 2 to 3 seeds.
- One-session values for the testable parts of the blocked claims, and an implementation of the tapped decoders.
