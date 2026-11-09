**A. Outcomes (44 claims in the claims file)**

| Claim | Outcome | Reason |
|---|---|---|
| fig2b-pv-cck-clusters | blocked (data_missing) | The archive's file list holds only `Data.zip` plus the descriptor docs. The zip has 367 recordings, all in the 8 paired-connection folders (cell 1). There are no current-step recordings. |
| fig2b-pvbc-aac-clusters | blocked (data_missing) | Same as above. |
| cck-no-subclusters | blocked (data_missing) | Same as above. |
| table1-pv-cck-features | blocked (data_missing) | Same as above. |
| table2-pvbc-aac-features | blocked (data_missing) | Same as above. |
| fig3-cp-pv | blocked (data_missing) | Only connected pairs are stored, so the unconnected tested pairs are missing. The descriptor does not mention connectivity testing. |
| fig3-cp-cck | blocked (data_missing) | Same as above. |
| fig3-cp-pv-cck | blocked (data_missing) | Same as above. |
| fig4b-in-pc-kruskal-wallis | reproduced | Under M3 a with M2 a, all five p < 0.05: rise 0.019, latency 0.0084, amplitude 0.0041, potency 0.0062, transmission probability 0.0095 (cell 13). Pair counts are 7/7/12, against the paper's 8/9/14. |
| fig4b-in-pc-posthoc | not_reproduced | The best reading gives 4 of 8 comparisons (cell 15), and partial needs at least 5. PV+BC against CCK+BC fails for rise, latency and amplitude. |
| fig4c-cckdti-pc-silent-single-ap | not_reproduced | Only 3 of 7 pairs are silent to the single AP before RIP (43%, criterion ≥85%). The four pairs that have a RIP recording transmit, with transmission probability 0.55 to 0.85 (cell 17). |
| fig7a-cscl-kinetics | blocked (metadata_insufficient) | Neither the descriptor nor `Experiments_description.txt` labels the pipette solution. |
| fig7b-cscl-stp | blocked (metadata_insufficient) | Same as above. |
| fig5c-pv-rip-depression | reproduced | Under M4 b with Wilcoxon: PV+BC 3rd AP 0.372 and 4th AP 0.329 (p 0.0156 each), AAC 2nd AP 0.679 (p 0.031). M4 a with the Mann-Whitney reading also passes (cell 25). |
| fig5c-cck-rip-facilitation | reproduced | Only under M4 a with all sweeps: CCK+BC medians 1.37, 1.46, 1.11; CCK+DTI 1.01, 1.35, 1.05; 7 pairs below 1 at the 4th AP. This is fragile: it fails under M4 b and under M4 a without the first 3 sweeps. |
| fig5db-recovery | reproduced | Spearman for PV+BC: rho 0.306, p 0.048 (M4 a); for AAC: p 1e-4. Both are below 1 at 50 ms. The CCK+BC medians rise and then fall. At 100 ms the PV+BC against CCK+BC test gives p 0.012 uncorrected (cell 27). No interval survives Bonferroni. |
| fig6-pv-trains-depression | not_reproduced | Not purely depressing: the 1 Hz median peaks at 1.148 (PV+BC) and 1.156 (AAC) under M4 a, and PV+BC peaks at 1.128 under M4 b. Synchrony also fails, since both onset rules flag 6 or 7 of 7 PV+BC pairs (cells 31, 38). |
| fig6-cckbc-pc-trains | not_reproduced | Only 1 of 6 pairs (0 of 6 with the first 3 sweeps left out) facilitates at every frequency from 1 to 40 Hz (cell 35). |
| fig6-cckbc-async-onset | not_reproduced (notebook: blocked) | The claims file defines two onset rules and both were run. EPI median onset is 2 (rule a) and 1 (rule b), against 11 in the paper (cell 38). |
| cckdti-pc-transmission | not_reproduced | 5 of 7 pairs respond at 1 to 40 Hz or RIP (expected 4 of 8). The mean first successful sweep is 2.0 (expected 4 ± 0.4) (cell 35). |
| cckdti-async-onset | not_reproduced (notebook: blocked) | EPI median onset is 3 (rule a) and 1 (rule b), against 7. At 160 Hz, rule a gives onsets 2, 7, 2 (cell 38). |
| async-charge-epi-vs-160 | cannot be judged from the outputs | The 160 Hz arm is measured after the wrong AP (problem 1). As run, reading b would be partially reproduced: CCK+BC p 2.5e-4; AAC p 0.003 fails. |
| decay-epi-vs-160 | cannot be judged from the outputs | Same bug. The 160 Hz decay constants (7.4 and 8.2 ms) are those of the isolated 11th IPSC. The EPI medians, 96.05 and 125.65 ms (reading b), are within tolerance. |
| fig8-pvbc-pvbc-uipsc | partially_reproduced | Under M3 b/c, 3 of 5 values are within tolerance: decay 3.38, latency 0.687 (just inside 0.684), transmission probability 1.0. Rise (0.514) and amplitude (104.4 pA) are outside. n = 10 (cell 19). |
| fig8-cck-pairs-uipsc | blocked (data_missing) | The CCK+ pairs have no RIP or 1 Hz recordings, so none of the claims-file M3 readings applies. Under the notebook's own reading d, at most 2 of 9 values are within tolerance and the latency test fails. |
| fig8-cckbc-vs-cckdti-pairs | blocked (data_missing) | Same reason. Under reading d, CCK+BC rise is slower than CCK+DTI, the opposite of the claim. |
| fig9-pvbc-pvbc-depression | reproduced | The 10th-AP median is below 1 at all 8 frequencies (at most 0.806). Spearman rho is −0.74, p 2e-18 (cell 31). |
| fig9-pvbc-pvbc-transmission-probability | not_reproduced | At 80 Hz the 10th-AP median is 1.0, not 0.9. At 320 Hz the 3rd-AP median is 1.0, outside 0.72 to 0.99 (cell 33). |
| fig9-pvbc-pvbc-recovery-11th | reproduced | 11th/1st medians are 0.61 to 0.71. Kruskal-Wallis p is 0.124 (M4 a) and 0.668 (M4 b). |
| fig10-cck-cck-heterogeneity | not_reproduced (notebook: blocked) | Rule a gives asynchronous release in 9 of 10 pairs (all at 160 Hz). Rule b gives 1 of 10. The target is 45 to 66% (cell 38). |
| fig10-cck-cck-frequency | reproduced | M4 a medians are 1.56 (10 Hz) and 2.15 (40 Hz). At 160 Hz the pairs are mixed, 5 above 1 and 4 below. |
| fig10-cck-cck-async | not_reproduced (notebook: blocked) | Rule a onsets at 160 Hz are at the 2nd to 5th AP, not after the 5th. Rule b finds no onset in 8 of 9 pairs. The duration and charge parts were never printed. |
| fig10bd-be-async-charge | blocked (data_missing for the 320 Hz parts) | CCK+ to CCK+ pairs have only 10, 40 and 160 Hz trains. The 10/40/160 Hz parts could be tested: the charges sit in `AS.imm` and `AS.delayed_a` but are never printed. |
| fig11-model-pv-udr | partially_reproduced | With weighting a, the SSE drops are 22.9, 13.1 and 24.7% (outside tolerance, inside 10 to 50%). The lowest BIC is UDR depressing for all three types, and facilitation lowers SSE by under 10% (cell 44). |
| fig11-model-cck-facilitation | reproduced | Only under weighting b: TM dep+fac BIC −1389 against −1387 for UDR dep+fac. Under weighting a the lowest BIC is UDR dep+fac. The margin is small. |
| table4-model-parameters | partially_reproduced | 8 of 13 within tolerance (weighting a). Reproduced needs at least 10. |
| fig11c-parameter-differences | not_reproduced | The Imax Kruskal-Wallis test fails: p 0.077 (a) and 0.16 (b). |
| fig11-model-prediction | reproduced for the testable types | Under weighting b the lowest test error is UDR dep for PV+BC to PC and AAC to PC, and TM dep+fac for CCK+BC. The PV+BC to PV+BC part is blocked (data_missing): there are no RIP or EPI recordings for interneuron pairs. |
| fig12-sipsc-kinetics | blocked (data_missing) | There are no spontaneous IPSC recordings in the archive. |
| sipsc-continuum | blocked (data_missing) | Same as above. |
| decay-pc-vs-interneuron | PV+BC half reproduced; CCK+BC half blocked (data_missing) | PV+BC: 7.78 against 3.38 ms, p 2e-4, both medians within tolerance. The CCK+BC side can only be measured with reading d, and there it fails (p ≥ 0.08) (cell 21). |
| fig13-pvbc-pc-recovery-halftime | reproduced, but fragile | With a free plateau, the median tau is 525.8 (M4 a) and 433.6 (M4 b), and half-time is 364.4 (M4 a). Only these 3 of 8 combinations land within tolerance. The interquartile range is 295 to 5354, against the paper's 343.6 to 648, and several fits hit the 1e5 bound. |
| fig13a-swr-refractory | blocked (data_missing) | There are no field potential recordings. |
| fig13c-optogenetic-swr | blocked (data_missing) | Same as above. |

I checked the archive for the blocked claims: `filelist.txt` lists only `Data.zip`, `docs/crcns_hc-7_data_description.{pdf,docx}` and `checksums.md5`. The descriptor describes only the paired recordings and does not record the pipette solution. Nothing in those claims can be tested, except as noted above for fig10bd, fig8 and decay-pc-vs-interneuron.

**B. Problems**

1. **[affects a conclusion]** Cell 37, `analyse`. For the 10-AP trains, `stim_template` returns 11 times, and `train = times[first:]` keeps the 11th AP, which comes 1 s after the train. I confirmed this on a synthetic recording: at 160 Hz the "last AP" is at 1357 ms.
   - The delayed charge, the decay constants (`tau_a`, `tau_b`) and the duration are therefore measured after the isolated 11th AP, not the 10th.
   - The 500 ms window runs past the end of the 1657.8 ms sweep and is silently cut to about 300 ms.
   - The immediate-charge window at the 10th AP spans 1000 ms.
   - This invalidates the 160 Hz arm of async-charge-epi-vs-160 and decay-epi-vs-160, and inflates the train onset counts.
2. **[affects a conclusion]** Cells 8 and 39. fig6-cckbc-async-onset, cckdti-async-onset, fig10-cck-cck-heterogeneity and fig10-cck-cck-async are blocked as `methods_underspecified`, but the claims file gives two onset rules and both were run. Their results should be judged, which gives not_reproduced. That the rules also flag PV+ pairs is something to report about the claims file; it is not a reason to block. The authors' undocumented `AR` marks do match the paper (CCK+BC median 12, quartiles 10 to 12.8), which suggests the rules in the claims file are not the authors' procedure.
3. **[affects a conclusion]** Cells 18 to 21. fig8-cck-pairs-uipsc, fig8-cckbc-vs-cckdti-pairs and the CCK+BC half of decay-pc-vs-interneuron rely only on reading d, which the claims file does not list, yet the summary table marks them "tested". Reading d also looks unreliable here: a CCK+BC pair has a negative latency (−0.12 ms) and the amplitudes are 3 to 15 pA (cell 19).
4. **[affects a conclusion]** Cell 8. Treating every interneuron-to-PC pair as a high-KCl pair is never checked. The argument that each type has no more pairs than the paper's high-KCl count does not rule out a mix with CsCl pairs. The paper reports that CsCl changes rise time, latency and CCK+BC facilitation, so this bears on fig4b, fig5c, fig6 and fig11.
5. **[affects a conclusion]** fig10bd-be-async-charge is labelled blocked, but its 10/40/160 Hz parts were computed and never printed. Its 320 Hz parts are missing from the data, and the notebook does not say so.
6. **[does not affect a conclusion]** Cell 35, fig6-cckbc-pc-trains. "Last AP" is the 11th AP for the trains, and for EPI under M4 a it is the last AP before the `AR` mark. The claim fails on its facilitation part (1 of 6 pairs) regardless.
7. **[does not affect a conclusion]** Cell 35, cckdti-pc-transmission. The first-success sweep pools the 160 Hz recordings, which are all 1. Using only trains at 40 Hz or below gives 2.57, still outside 4 ± 0.4.
8. **[does not affect a conclusion]** `hc7.detect_success` (M2 b). On white noise it scores 12.5% false successes (my synthetic test), which shows in the null rates of 0.15 to 0.5 in cell 17. The outcomes rest on M2 a.
9. **[does not affect a conclusion]** Cell 37, `pair_template`. Some template fits hit their bounds: CCK+DTI to PC Pair06 (rise and decay both 20 ms, A about 9.9e4) and Pair04 (decay 200 ms). The reconstructions for these pairs are meaningless.
10. **[does not affect a conclusion]** Cell 29. Recovery fits hit the tau = 1e5 bound for 2 or 3 pairs per reading, and the fig13 result depends on which readings are taken.
11. **[does not affect a conclusion]** Cell 44, `refit_A`. The TM dep test error is infinite for CCK+BC under weighting a.
12. **Claims-file issues** (reported, not corrected):
    - fig5c reading (b) runs a Mann-Whitney test against a constant vector of ones. It returns p = 0.00106 whenever all 7 values lie on one side of 1, so the test is degenerate.
    - The fig4c criterion counts any success in any sweep. The paper's Methods say the single AP comes 1600 ms after the previous burst. The paper's own build-up statement (an IPSC "from the fourth trace") suggests the paper may mean the first sweeps only.
    - The onset rules for fig6-cckbc-async-onset cannot tell the paper's synchronous PV+ pairs from CCK+BC pairs.

**C. What I could not check, and the output that would settle it**

- **160 Hz charge and decay after the 10th AP:** rerun `analyse` with `train = times[:10]` for the trains, and print `delayed_a`, `delayed_b`, `tau_a` and `tau_b` per pair.
- **fig10bd and fig10-cck-cck-async:** print the per-frequency medians of immediate charge (APs 5 to 10) and delayed charge, plus the durations and the total-charge Kruskal-Wallis test.
- **fig10-cck-cck-heterogeneity facilitation part:** print the per-pair maximum relative amplitude at 10 and 40 Hz.
- **fig4c:** print per-sweep success at the single AP for the CCK+DTI pairs (sweeps 1 to 3 against later sweeps).
- **Pipette solution:** I could not tell whether any interneuron-to-PC pair is a CsCl pair. A per-pair table of rise time and latency by recording date, matched against the paper's group sizes, would help.
- **`_EPA` column mapping:** print one RIP table's column headers next to its AP times, to confirm that T01S01 is the single AP.
- **fig8 PV+BC pairs:** only 10 of 14 have a 1 Hz train, and I could not tell which of them match the paper's 16.
