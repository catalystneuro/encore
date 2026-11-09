**A. Outcomes (48 claims, from the claims file)**

| Claim | Outcome | Reason |
|---|---|---|
| link-manuscript-sessions | partially_reproduced | All 379 files match the table, virus codes agree in 97.3% of channels, each mouse has one genotype, and the Drd2 (12/7/8) and Fig. 2 (6) cohort sizes match (cell 10). The striatum-wide mCherry count of 5 is circular: it counts a hand-written list of 5 mice (cells 10, 33). |
| ed1b-switch-after-block-transition | reproduced | Mean over mice: P(switch) is 0.175 before the transition, 0.216 in the first 10 trials after and 0.174 at positions 20–30; tau_highport = 2.82 (cell 29). This is 26 Fig. 1 mice, not the paper's 8. |
| ed1hj-rflr-predicts-switching | not_reproduced | Only 1 of 8 histories falls within the binomial s.e. under both readings. P(switch) r = 0.803 under reading (a), below the 0.9 bound (cell 31). |
| fig1e-reward-outcome-post | reproduced | DA: 14/14 mice significant in the stated direction. delta-Ach: 12/16. Both W1 and W2 (cell 15). |
| fig1e-reward-outcome-not-pre | not_reproduced | DA pre under W2: 7 of 14 mice significant, which is not "fewer than half". W1 gives 6/14 and Ach 3/16. All significant DA mice point the same way (T2 p = 0.006). Borderline, and it depends on one extra, unidentified DA mouse. |
| fig1e-lda-accuracy | reproduced | Reading (a), mean over mice: post accuracy DA 0.934, Ach 0.837; pre accuracy 0.516 and 0.539, within 50 ± 5%. Shuffled-label accuracy is 0.49–0.54, which agrees with the paper's 50% chance level (cell 17). |
| ed3-not-lateralized | partially_reproduced | DA fails: 4–10 of 14 mice are significant in each condition (cell 21). Ach passes: significant mice split 3 vs 4 in direction, and LDA averages 0.648 and 0.619, both below 0.65. |
| fig1f-cue-omission | reproduced | All 4 mice meet all four directional tests at p < 0.05 under W1 and W2 (cell 23). Whether the "no-cue" session really omitted the cues was not verified (B11). |
| fig1g-history-stay | reproduced | aA−AA: DA 14/14, Ach 9/16. Aa−aa: DA 14/14 negative, Ach 10/16 (W1) and 9/16 (W2) (cell 19). |
| fig1h-switch-no-history-post | reproduced | At most 5 of 14 (DA) and 2 of 16 (Ach) mice are significant in any comparison (cell 19). AB has a median of only 16 trials per mouse, so power is low. |
| fig1h-switch-da-approach | reproduced | 13/14 mice (W1) and 14/14 (W2) significant in the stated direction (cell 19). |
| ed4bc-iti-port-entries | not_reproduced | Ach post is not higher in unrewarded trials (at most 2 mice), and DA pre is higher in only 5 mice. DA post is lower in 7–8 mice (cell 25). |
| ed5-base-glm-r2 | blocked (methods_underspecified) | G1 is out of tolerance for both signals, G2 is in, and Ach under G3 (0.243–0.249) is out (cell 67). The readings disagree, which is the criterion's rule for blocking. |
| ed5f-leave-out | partially_reproduced | I disagree with the notebook's "blocked". Leaving out DA side entry fails the range rule under all 12 readings, so the readings agree on that failure (cell 68). Reward (both signals) and the centre-entry/centre-exit parts hold under every reading. |
| ed5-history-glm-r2 | blocked (methods_underspecified) | The R2 values disagree across readings (cell 67). The MSE comparison was never computed (B3). |
| fig2a-rdah-smaller-than-dlight | not_reproduced | In unrewarded trials, rDAh's \|min\| is larger than dLight's in WT63 and WT64 (p < 0.0001). WT65's rewarded traces correlate at r = 0.788, below 0.8 (cell 46). |
| ed6c-da-bilateral | not_reproduced | Peak r is 0.49–0.68 in all 4 mice, below the named 0.7 bound (cell 46). |
| fig2d-anticorrelated-lag | reproduced | Minimum −0.224 at +0.108 s. Both controls stay near 0 (minima −0.001) (cell 44). |
| fig2e-trial-and-noise-correlation | reproduced | Negative minima at +0.054 s (rewarded) and +0.108 s (unrewarded), signal and noise, all within 0.1 ± 0.054 s (cell 42). |
| fig2fg-off-diagonal | partially_reproduced | The off-diagonal is negative at every time point. Near side entry, the magnitude ratio is below 0.25 only for unrewarded side-aligned trials (0.22). Rewarded trials give 0.54 and 1.34 (cell 48). |
| fig2h-photometry-glm | blocked (notebook) – but testable | Not run (cell 69). The 6 rDAh+Ach mice are in the data, and the kernel-lag part of the criterion does not depend on the R2 readings. |
| ed6b-separate-hemispheres | reproduced | Minimum −0.405 at lag +2; positive maximum 0.138 at lag −6 (cell 46). |
| fig3d-telc-abolishes-ach | blocked (data_missing) | I confirmed in the archive API that none of S731, S734, S803, S804, S998, S999 or S1001 have assets. |
| fig3c-telc-blocks-cin-evoked-da-in-vitro | blocked (data_missing) | All 379 assets are behaviour/photometry NWB files; there are no slice recordings. |
| fig3e-striatum-wide-telc | reproduced | ITI p = 0.0007, decision time p < 0.0001, alpha rank-sum p = 0.028. In TelC mice, mean DA post is +0.54 (rewarded) and −0.36 (unrewarded) (cell 35). |
| fig3f-vls-telc-da-unchanged | not_reproduced | dLight1.1: 34 comparisons are significant in one direction in more than half of the mice (e.g. unrewarded post, TelC lower in 3 of 4). rDAh: 0 (cell 52). |
| ed8g-vls-telc-ach-suppressed | partially_reproduced | ΔF/F0 reading: lower in the TelC hemisphere in 4/4 mice. z-scored delta-Ach reading: fails (S952 is higher; S1143 W1 p = 0.07; S950 W1 is higher) (cell 54). |
| ed9jm-vls-telc-behaviour-normal | not_reproduced | Only reading (a) can be run, and it gives 4 significant tests (cell 37). That comparison is between cohorts and is unchecked for task parameters (B7). |
| ed8f-amplitude-no-consistent-effect | blocked (methods_underspecified) | dLight: 4/4 mice the same sign; rDAh: 2/2 (cell 54). The legend places 8f with the Fig. 3f (dLight) panels, which would make it not_reproduced (B17). |
| fig3g-dan-inhibition-lowers-da | blocked (data_missing) | The archive has no S1183–S1241 assets, and laser onsets appear only in the 7 CIN-stimulation sessions. |
| ed7e-cin-activation-evokes-da | not_reproduced (as run) | Under reading (b), DA is lower with stimulation in 7/7 mice (p = 5.6e-6). Decision time and occupancy are unchanged (p = 0.09, 0.997). The DA measure is unreliable (B4), and reading (a) cannot be run. |
| fig4bc-da-bidirectionally-controls-ach | blocked (data_missing) | No head-fixed or DAN-opsin sessions; no laser channels outside the CIN cohort. |
| fig4ef-d2r-needed-for-cin-pause | blocked (data_missing) | Slice cell-attached recordings are not in the archive. |
| fig4g-cko-ach-suppression-lost | not_reproduced | delta-Ach with mouse means: ANOVA p = 0.73 (pre) and 0.89 (rewarded post). With trials pooled, cKO pre is below WT (cell 58). The mean-Ach variant does reproduce (B16). |
| fig4g-cko-da-unchanged | not_reproduced | Mouse-mean ANOVA, DA post +9..+16: p = 0.039 (all trials) and 0.049 (rewarded) (cell 58). |
| ed11e-cko-anticorrelation-reduced | reproduced | cKO cross-correlation minimum is smaller in magnitude than both controls in every row (p ≤ 0.009), and so is the off-diagonal (cell 50). |
| ed11-cko-glm-r2 | blocked (notebook) – but testable | Not run, although the data exist (27 mice). The kernel parts of the criterion do not depend on the R2 readings. |
| ed11fh-cko-general-behaviour-comparable | not_reproduced | Decision time, cKO vs f/f: p = 0.044. The other 13 tests are not significant (cell 37). |
| ed11i-cko-rflr | not_reproduced | Beta p = 0.064/0.64/0.24 and tau p = 0.42/0.64/0.49 against f/f, WT and both pooled (cell 37). |
| ed11j-cko-switching-impaired | not_reproduced | Trial resampling finds Aa (and AAa) significant against both controls; session resampling finds none (cell 40). The CI is two-sided, but the legend says one-sided (B5). |
| fig5a-inputs-to-vls | blocked (data_missing) | Histology is not in the archive. |
| fig5b-glutamate-not-lateralized | not_reproduced | Post window: 4/4 (greenL) and 3/4 (greenR) mice significant (cell 60). |
| fig5c-glutamate-like-ach | partially_reproduced | Pre-window glutamate (−0.335) is not below its centre-entry value (−0.362). The other three parts hold: rise 0.229, r = 0.41, rewarded > unrewarded 4/4 (cell 60). |
| fig5d-terminal-calcium-coincides | reproduced | Mean-trace r = 0.85/0.91 (rewarded) and 0.68/0.79 (unrewarded), thalamic/cortical. 9 jRCaMP1b mice are used against the paper's 6. |
| fig5ef-input-telc-dampens-ach | partially_reproduced | Cortex: every TelC mouse is below the smallest mCherry under both F0 readings (3 of the paper's 5 TelC mice). Thalamus: the mCherry mice have no raw traces (data_missing) (cell 62). |
| fig5ef-input-specific-ach | not_reproduced | Cortex delta-Ach p = 0.40/0.26. The latency shift is smaller for thalamus (0.108 s) than cortex (0.162 s) (cell 62). |
| ed13-input-telc-behaviour | partially_reproduced | Thalamus: beta, tau and reward rate all p < 0.05 in the stated directions. Cortex: none significant, with 3 TelC mice each having one session (cell 37). |
| ed2op-mutant-sensors-flat | not_reproduced | Ach mutant/wild-type ΔF/F0 range ratio is 0.15 in WT14 but 0.33 in WT15, above 0.25; WT12 has no wild-type channel to compare against (cell 64). There is no dLight mutant; WT16–WT20 are absent from the archive. |

**B. Problems**

1. [affects a conclusion] Cell 69: fig2h and ed11-cko-glm-r2 are blocked "by dependence" and never run. The data exist, and their kernel criteria (most negative coefficient at 54–162 ms; cKO Ach kernels vs controls) can be judged whatever the R2 reading.
2. [affects a conclusion] Cell 68: ed5f is labelled blocked, but its outcome does not change across readings. DA side entry fails the range rule under every reading; reward and centre entry/exit pass under every reading.
3. [does not affect a conclusion] Cell 68: ed5-history's "history MSE below base in every run" ends as a comment and is never computed. Overfitting is not checked either.
4. [affects a conclusion] Cell 56, ed7e:
   - The measure (peak over 0–1.5 s) falls inside the laser window. The Methods say the laser produced an artefact that the authors removed; here it is not removed.
   - z-scored traces are used, where the paper uses ΔF/F0.
   - The Methods say only one hemisphere was illuminated per session. The illuminated side is never checked; the code assumes left.
5. [affects a conclusion] Cell 40, ed11j: the CI test uses the 2.5/97.5 percentiles. The legend and claims file say one-sided, which would use the 95th percentile and could add significant histories under session resampling.
6. [affects a conclusion] Cell 21, ed3:
   - The ipsi/contra LDA is run on W1 only. Ach's 0.648 sits just under the 0.65 bound, so W2 could flip that half.
   - The DA part uses 14 mice, against the legend's 7.
7. [affects a conclusion] Cells 33/37, ed9jm reading (a): it compares the 2020 VLS-TelC cohort with the 2021–22 striatum-wide mCherry mice. High-port probability varies by session from 0.8 to 1.0 (cell 27), and it is not compared between the groups. Reward rate and switch rates depend on it.
8. [affects a conclusion] Cells 12/13, 60, 66: cohorts are larger than the paper's, and the extra mice are not identified. Fig. 1 has DA 14 vs 13 and Ach 16 vs 14; this decides fig1e-not-pre, where W2 gives exactly 7/14. jRCaMP1b has 9 vs 6 mice. The GLM cohort has 10/12 vs 8/9 mice and mixes rDAh into DA.
9. [affects a conclusion] Cells 10/33: the striatum-wide mCherry group is a hard-coded list, and the link claim's cohort-size check just counts that list.
10. [affects a conclusion] Cell 33: the thalamic mCherry mice (S1351, S1389, S1393) are labelled "retro mCherry" in the files, the cortical control's virus. The notebook does not reconcile this, which bears on ed13 and fig5ef.
11. [affects a conclusion] Cell 23: cue omission is not verified. The "no-cue" sessions show more centre-LED onsets per trial (2.2–3.9) than the cued ones (1.1–1.8). Pairing comes only from dates in the script.
12. [does not affect a conclusion] Cell 31: reading (b) is fitted per mouse, where the claims file says "all sessions pooled". A pooled fit would not fit better, so the outcome stands.
13. [does not affect a conclusion] achda.fit_rflr uses Nelder-Mead in place of SGD. On synthetic sessions (α, β, τ = 0.3, 1.5, 1.5) I recovered 0.38, 1.49, 1.53. I also checked xcorr_norm (lag sign), window_idx, add_history words, tau_highport and t1 on synthetic inputs; all behave as documented.
14. [does not affect a conclusion] achda.behaviour_table: the docstring says ITI = centre entry minus previous side exit, but the code uses start_time minus the previous stop_time. Whether those columns mean the same thing is not checked.
15. [does not affect a conclusion] Cell 46: fig2a's pre-window readings are not run. The claim already fails on post.
16. [affects a conclusion; claims-file issue, reported not corrected] fig4g-cko-ach-suppression-lost: the criterion uses delta-Ach (max − min). "Dips lost, so Ach signals larger" reads as mean Ach. The notebook's mean-Ach variant gives ANOVA p = 0.0005 (pre −18..−1) and p = 0.0001 (rewarded post +9..+16), with cKO higher than both controls (p ≤ 0.003).
17. [affects a conclusion; claims-file issue] ed8f: the criterion names no sensor. The legend lists 8f with panels d–e (the Fig. 3f dLight cohort) before the rDAh panel g.
18. [does not affect a conclusion] fig5b: the significant per-hemisphere differences come from left-port trials being higher in both hemispheres, so they flip sign in ipsi/contra terms. The criterion counts them as lateralization anyway.
19. [does not affect a conclusion] Cell 25: ed4bc has few isolated ITI side entries (median 6–7.5 per mouse, minimum 1), so T1 has low power.
20. [does not affect a conclusion] Cell 38 still holds the author's "Result:" lines for ed9jm, ed11fh, ed11i and ed13. My outcomes above come from the outputs.
21. [does not affect a conclusion] achda.load_session skips channels whose sensor is "unknown" (88 channel-sessions). Their contents are never inspected.

**C. Not checked, and what output would settle it**

- **Cohort labels (link claim, ed13, fig5ef):** the export table's rows for the hard-coded groups (sw_mCh, thal_mCh, ctx_*) were not printed.
- **ed9jm:** high-port probability and block length per group are not printed.
- **ed3:** LDA under W2 is not printed, nor the DA tests restricted to the 7 mice of Extended Data Fig. 3.
- **ed7e:**
  - the laser-onset-aligned z trace (−2 to +3 s) per mouse, to show the artefact;
  - which hemisphere was illuminated in each session.
- **fig1f:** the LED and occupancy channels around trials in each paired session.
- **fig4g and ed11e:** a per-session check that redL is rDAh and greenL is Ach3.0 in the Drd2 cohort.
- **ed11j:** the one-sided bootstrap result.
- **ed5-history:** the history-vs-base test MSE per run.
- **fig2h and ed11-cko-glm-r2:** the GLM runs themselves.
- **ed2op:** the list of "unknown" channels by mouse.
- **Archive contents:** I checked the archive API for the missing mice: none of the 21 named mice have assets, and all 379 assets are behaviour NWB files. The asset metadata does not list streams, so I could not independently confirm the missing raw traces (thalamic mCherry) or the missing right-hemisphere dLight (CIN cohort) without reading the files.
