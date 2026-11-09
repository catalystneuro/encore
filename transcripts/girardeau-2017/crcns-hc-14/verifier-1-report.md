A. Outcomes (38 claims, from the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| units-recorded | partially_reproduced | 61 sessions, 7,390 table units / 7,415 raw, BLA (B1) 2,038 and hippocampus 1,260 are within tolerance. CeN 659 and Pir 704 are outside (782±78, 1,560±156) (cell 14), and the criterion has no partial clause. The shortfall comes from Rat08's 1,571 unlabelled units (problem 2). |
| fig1b-dz-speed-anova | partially_reproduced | Under the criterion's "all samples" reading (cell 19): epoch and interaction p<1e-5, zone p=0.081. The "dir" variant gives zone p=0.043. Sessions are 51, against the paper's 55. |
| fig1b-dz-speed-posthoc | partially_reproduced | Three of four tests pass at 0.05/4 with the right signs. Post-run current−previous gives t=−1.61, p=0.11 (cell 21). |
| fig1b-speed-ratio | reproduced | ANOVA F=26.5. Median ratio is −0.085 in pre-run and +0.049 in post-run. All three paired tests pass at 0.05/3 in the stated directions (cell 23). |
| figs1b-ratio-each-rat | reproduced | All four rats p<0.03, with pre-run median below post-run (cell 25). |
| fig1c-slower-in-dz-post-run | reproduced | Rank-sum post vs pre z=−3.23, p=0.0013, n=53 (cell 27). |
| figs1c-habituation | reproduced | Pooled rho=0.70, p=4e-9, and rho>0 in 4/4 rats under all three lap counts (cell 29). |
| airpuff-location-no-bias | not_reproduced | Pre-run r=−0.40, p=0.003 and run r=−0.34, p=0.012 (cell 31). The run correlation stays significant under the "dir" variant. The location estimate is in doubt (problem 3). |
| fig2c-bla-pyr-higher-in-sleep | reproduced | Counts are exactly 675/175/1,188. Medians NREM 0.26 and REM 0.36, both p≈0, REM > NREM (cell 35). Depends on column 5 being REM: with column 8 it would be partial. |
| fig2c-bla-interneurons | reproduced | REM/wake p=0.2107, which matches the paper's 0.21 at n=175. NREM/wake median −0.07, p≈0 (cell 37). |
| fig2c-skewed-rates | reproduced | Skew of the rates is 3.4, 14.0 and 7.4; skew of the log rates is −0.41, −0.58 and 0.12. Both readings hold in all three states (cell 39). |
| fig3c-hpc-bla-ev-nrem | reproduced | 25 sessions, mean 3.14±0.73%, p=4.5e-5 (cell 43). Computed from the authors' deposited pair table. |
| fig3c-hpc-bla-ev-rem-absent | reproduced | p=0.73 over 25 sessions; the paper has 23 because the 180-s REM filter could not be applied (cell 45). |
| fig3c-decay | not_reproduced | On the substitute NREM: window 2 mean 1.10% is outside 1.72±0.44, Kruskal-Wallis p=0.074, window 3 p=0.28 (cell 77). The result depends on the substitute (problems 1 and 6). |
| figs5a-hpc-bla-all-cells | partially_reproduced | NREM p=3.5e-5 and REM p=0.37 over 27 sessions. Substitute window 2 p=0.0507 misses the threshold (cell 79). |
| fig3d-pir-reactivation | blocked (data_missing) | The archive's file list (`unpacked_filelist.txt`) has no sleep-state file. The NREM half alone could decide "not reproduced", but the notebook's run covers only 6 sessions from one rat (p=0.69, cell 101) because Rat08's Pir shanks were never read. |
| fig3d-pir-weaker-than-bla | not_reproduced | Pir 0.26% (6 sessions, rat 10 only) against BLA 1.97% on the substitute; one-tailed p=0.079 (cell 81). Both means are outside tolerance. The Pir session set is incomplete (problem 2), so this verdict is weak. |
| fig3e-cen-no-reactivation | blocked (data_missing) | REM states are not deposited. The NREM half gives p=0.64 over 15 sessions (cell 101). |
| figs4-intra-structure-nrem | reproduced | p = 3.2e-4, 6.5e-5, 2.9e-3 and 2.5e-4, all with EV > REV (cell 83). On the substitute NREM. |
| figs4-intra-structure-rem-absent | blocked (data_missing) | No REM scoring in the archive. |
| fig4-bla-ripple-modulation | reproduced | B1 at the code's threshold gives exactly 25.8/11.1/14.7/8.3%, with 163 and 1,232 cells (cell 47). Read from the authors' PoissonRippleMod table. |
| figs5b-ripple-modulated-pairs-reactivate-more | reproduced | Pyramidal: 7.16 vs 1.67%, p=0.004. All pairs: 6.08 vs 1.81%, p=0.005. All four means within tolerance (cell 57). |
| run-correlated-pairs | reproduced | 37,660 pairs, 6.69% positive, 3.34% negative, group 1 = 595, from both the table and the raw spikes (cell 51). |
| fig5a-up-positive-pairs-change-most | reproduced | F=29.08, p=1.1e-45. up/pos is the largest group and differs from all 8 others at Tukey p<0.001 (cell 53). |
| figs6b-ev-nine-groups | reproduced | up/pos EV−REV is 14.7%, the largest of the nine groups (cell 55). |
| fig5b-top-contributors-gain-increase | reproduced | Top quartile: 63 cells, p=5e-5. Other quartiles: 74 cells, p=0.986 (cell 72). Uses the deposited gains; the two smoothings the criterion asks for could not be run. |
| figs9-ev-independent-of-rate | reproduced | Under the whole-session-rate reading: EV > REV in 8/8 octiles and all Spearman p ≥ 0.086 (cell 59). The run-rate reading fails strongly (rho=1.0 and 0.98). |
| fig6a-airpuff-trajectory-reactivation | reproduced | One-sided p=0.0115 over 24 sessions (cell 89). On the substitute; at 2 cm/s p=0.095 (cell 103). |
| fig6a-safe-trajectory-no-reactivation | not_reproduced | p=0.0475 (cell 91), and p=0.037 at 2 cm/s. |
| fig6b-airpuff-greater-than-safe | not_reproduced | p=0.151, peak-bin variant p=0.099 (cell 93), 2 cm/s p=0.81. |
| figs11a-whole-run-reactivation | reproduced | Pyramidal p=0.0007, all cells p=0.0009 (cell 95). Both still pass at 2 cm/s. |
| figs11b-all-cells-both-trajectories | reproduced | Air puff p=0.040, safe p=0.026 (cell 97). At 2 cm/s safe gives p=0.18, which would make it partial. |
| figs11c-all-cells-difference-absent | reproduced | p=0.43 (cell 99). |
| bla-rates-safe-airpuff-absent | reproduced | Reading (a): pyramidal p=0.97, all cells p=0.68 (cell 70). The all-session variant gives pyramidal p=0.013. |
| ripple-rate-pre-post-absent | reproduced | Two-sided p=0.75 over 38 sessions (cell 85). On the substitute. |
| fig7b-strong-pairs-correlated-changes | reproduced | Reading (a): r=0.275, p=1.9e-16, n=867, against the paper's 0.27, 2.1e-16, 866 (cell 64). |
| fig7b-weak-pairs-not-correlated | reproduced | Reading (a): r=0.034, p=0.33 (cell 66). |
| fig7c-quartiles | reproduced | Reading (a): top quartile r=0.130, p=8e-33; bottom quartile r=0.014, p=0.20 (cell 68). |

Tally: 26 reproduced, 4 partially_reproduced, 5 not_reproduced, 3 blocked. The paper states no chance level for any selection, so there was nothing to compare.

B. Problems

1. [affects a conclusion] `hc14.substitute_nrem`, cells 73–103. The substitute NREM is immobility in the home cage below 4 cm/s. The paper scored states from hippocampal theta/delta and amygdala spectra (Online Methods), and the LFP is in the archive. Immobility includes REM and quiet wake. Against the authors' NREM pair correlations it only reaches r=0.64 (pre) and 0.59 (post), and it dilutes EV−REV from 3.21% to 1.96% (cell 75). It covers only 3–21% of sleep in most Rat11 sessions (cell 74). Several outcomes change with the threshold: fig6a-airpuff, figs11b-safe and figs5a window 2 (cell 103). Every claim marked "substitute" in table A depends on it.
2. [affects a conclusion] `structure_shanks`, cells 14 and 81. `Rat08-Info/StructureMapping.ods` is in the archive (confirmed in `unpacked_filelist.txt`) but is not read, so Rat08's CeN and Pir shanks are missing. This causes the CeN and Pir misses in units-recorded and leaves fig3d with 6 Pir sessions from one rat, where the paper has 14–17 in 3 rats.
3. [affects a conclusion] Cell 16. The air puff location is taken as the head position at puff time. That is 3–18 cm away from the deposited `airpuffloc` value (114.0 vs 95.8, 110.2 vs 97.0, 148.4 vs 156.4 cm), mostly displaced in the direction of travel, which is comparable to the 20-cm danger zone. The notebook prints this but neither uses the file nor shifts the location to test sensitivity. This affects fig1b (zone p=0.08), the posthoc tests, airpuff-location-no-bias and fig1c.
4. [does not affect a conclusion] Cell 16, `prev_loc`. After a session with no location (Rat09-20140328, positions lost at every puff), the next session's previous zone is taken from two sessions back when it should be undefined. This affects one session.
5. [does not affect a conclusion] Cell 81. The variant that pits BLA from the authors' table against substitute Pir mixes two NREM definitions, so its p=0.026 is not a valid comparison.
6. [affects a conclusion] Cell 77, fig3c-decay. The analysis uses the substitute pre-NREM even though the table's pre-NREM is available. The 20-min windows are counted in substitute time, which includes quiet wake at sleep onset, so the window boundaries move.
7. [does not affect a conclusion] Cells 43–57 and 72. These claims re-test the authors' deposited intermediate tables (EVcontribs, PoissonRippleMod, AllRippleCCGs, StatesFR), so they check the paper's statistics, not its processing of the raw data. Only the run correlations were checked against raw spikes, and some sessions differ (Rat10-20140702 r=0.58; Rat11-20150326 max difference 0.17; cell 10).
8. [does not affect a conclusion] Cells 6–8. Reading StatesFR column 5 as REM is an assumption. It is well supported: the interneuron REM/wake p is 0.2107 at n=175, against the paper's 0.21 at n=175.
9. [does not affect a conclusion] Cell 59, figs9. The verdict holds only under the whole-session-rate reading, which the claims file allows. Under the run-rate reading EV−REV rises monotonically with rate (rho=1.0).
10. [does not affect a conclusion] `hc14._zbins`. A valid bin is dropped where two intervals touch (synthetic test: 199 of 200 bins). The other helpers pass synthetic tests: `laps`, `ev_rev`, `corr_p`, `in_intervals`, `linear_speed`, `reactivation_strength` (planted peak recovered at lag 0) and `substitute_nrem`.
11. [does not affect a conclusion] Cells 17–21. The analyses use 51 sessions, where the paper reports n=55 with t(52) and t(51). The first session of each rat has no previous zone, and the notebook does not explain the difference.

C. What I could not check, and the output that would settle it

- How well the substitute matches the authors' NREM in duration. Needed: per-session substitute minutes in pre- and post-sleep, next to the NREM time implied by StatesFR (fitted column-6 fraction × session duration).
- Whether the danger-zone results survive a corrected location. Needed: fig1b, the posthoc tests, the ratio, fig1c and airpuff-location rerun with the location shifted back by the median offset from the six `airpuffloc` sessions, or using the file values where they exist.
- The Rat08 CeN/Pir counts and the Pir sessions for fig3d. Needed: Rat08 labels parsed from `StructureMapping.ods`, with label counts per rat.
- All REM-dependent claims (fig3d-pir-reactivation, fig3e, figs4-rem). No state files exist in the archive. A theta/delta and immobility scoring from the deposited LFP (61 archives of about 7 GB) would make them testable, and would also replace problem 1's substitute.
- That laps are detected correctly on each track. Needed: laps per session per direction and the 1st–99th-percentile track extent; the habituation index goes as low as 0.17.
- The fig5b smoothing variants. The deposited gains' smoothing is undocumented, so the code-path variant could not be compared.
