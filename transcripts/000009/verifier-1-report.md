## A. Outcomes, claim by claim (39 claims in the claims file)

| Claim | My outcome | Reason |
|---|---|---|
| task-performance | not_reproduced | No reading has all three values within tolerance (cell 19). The closest, whole-cell trials pooled, gives 77.4% correct and 9.65% lick-early, but 1.55% no-response against 1.1 ± 0.11. |
| fig1c-alm-photoinhibition-bias | reproduced | At 1.5 mW, over 66 sessions from 11 mice: contra 0.774 → 0.368 (p = 3.6e-25) and ipsi 0.673 → 0.744 (p = 1.7e-4). Both are below 0.001 (cell 21). |
| fig1d-thalamus-photoinhibition-bias | blocked (data_missing) | Confirmed on the archive. The 9 Ai35D x GAD2_Cre assets are plain `ecephys.nwb` files with no ogen part and no OptogeneticSeries, and there are no behaviour-only assets. |
| gad2-thalamus-reduction | blocked (metadata_insufficient) | Confirmed on the archive as above. The unit count matches (84 = 26 + 41 + 17), but no trial is photostimulated, so nothing can be tested. |
| vgat-thalamus-reduction | reproduced | Under W1 (whole delay), Q1 is 15.8–20.3%, within 15.9 ± 9.3 (cell 41). Under W2 it is only 1.2–1.5%. Group sizes (23/21/31) are not the paper's 34/42/38, and distances are from one nominal fibre coordinate. |
| muscimol-vmval-bias | blocked (data_missing) | No infusion data among the 173 assets. |
| alm-unit-classes | not_reproduced | 966 units against 1214 ± 121, and pyramidal and fast-spiking counts are out under P1 and P2 (cell 23). The P2 fractions do match (0.839 against 0.829; 0.125 against 0.137): about 250 units are simply not deposited. |
| fig2e-alm-selectivity | not_reproduced | 0 of 32 readings meet the criterion on absolute counts (cell 25). The fraction matches (P2 0.70), and scaled to 1006 units, control/R2/c1 gives 702/156/268/277, within tolerance. The shortfall is missing units. |
| fig2e-alm-contra-ipsi-balance | reproduced | Both readings hold in all 32 readings; contra fraction 0.495–0.543 (cell 27). |
| thalamus-unit-classes | not_reproduced | 789 units and 682 putative thalamic (P2) are within tolerance. Within 0.4 mm gives 259 (allowed 282–344) and VM/VAL 222 (allowed 265–325). Reading L1 has no label (cell 29). |
| fig2f-vmval-selectivity | not_reproduced | Counts are out under all 64 readings. Under P2 and P3 the selectivity types differ from ALM (2 × 4 test p = 0.0003–0.04, cell 31). Only P1 (n = 20) passes the chi-squared tests. |
| fig3-alm-collapse | partially_reproduced | Activity falls to 2.1–2.5% (Q1) or 5.1–5.2% (Q2), against 6 ± 0.6; n is 230–261 against 314. In every reading inhibited units outnumber activated ones and 0 are significantly activated (cell 33). |
| fig3d-all-layers | blocked (methods_underspecified) | Under m1 every bin passes. Under m2, bins of 1–4 neurons tie at 0–0 (cell 35), so the readings disagree. |
| fig3b-selectivity-types-equally-inhibited | blocked (methods_underspecified) | With the rate difference as measure, some pair differs at p < 0.05 in all readings. With the ratio, mostly no pair differs; both differ together in only 13 of 64 (cell 37). |
| fig3f-thalamus-silenced | not_reproduced | Q1 is 0.9–1.1% against 2 ± 0.2, and n is 89–113 against 148 ± 15. Reading (b), VM/VAL, has 0 units (cell 39). |
| fig3-onset-latencies | reproduced (fragile) | Under T1/O2: thalamus 2.0 ms, ALM 9.0 ms (P1) or 7.0 ms (P2), ALM later (cell 43). Under O1 the ALM onset is 0.0 ms, before the thalamus, and the bootstrap SEMs (3–4 ms) are twice the paper's. See problem 4. |
| wc-near-threshold | not_reproduced | 7.2 mV (reading a) and 6.5 mV (reading b) against 12.7 ± 0.7, with n = 36 against 60 (cell 63). The deposited-kink variant agrees (6.9). |
| wc-thalamus-hyperpolarization | not_reproduced (provisional) | Under E the change is +0.31 mV. Under M it is −16.83 ± 1.24 mV, outside −18.7 ± 1.1; the onset is not judged (cell 65). Provisional because of problem 1. |
| wc-loss-of-excitation | blocked (data_missing) | Confirmed: all 36 whole-cell assets are behaving recordings, Ai32 x PV-Cre or VGAT. There are no Gad2 or current-injection experiments. |
| wc-m1-small-effect | not_reproduced | Under M, Vm is −2.75 (within) but the rate change is +0.76 spikes/s against −1.4 ± 0.6. Under E both values are out. |
| wc-contra-alm-small-effect | reproduced (under M) | −1.60 ± 0.64 mV, within −1.4 ± 0.5. Under E it is +0.86. |
| thalamus-stronger-than-cortex | reproduced (under M) | Under M, readings (a) and (b) both hold: p = 5e-8 against M1 and 8e-9 against contra ALM. Under E neither holds, but under E there is no photostimulus effect at all (cell 14). |
| indirect-pathway-too-slow | blocked (data_missing) | No M1 whole-cell neurons are deposited. The ALM-after-M1 onset (13.9 ms) could only be tested with a laser time; see problem 1. |
| conduction-delay | blocked (data_missing) | Confirmed: there is no Olig3 genotype in any asset's metadata. |
| latency-model-t3 | blocked (methods_underspecified) | A simulation; its parameters are in the Supplementary Information. |
| fig5-weak-photoinhibition-rates | blocked (data_missing) | ALM sessions with thalamic photostimulation use 10, 22.5 or 45 mW only; none at 0.5 mW (cell 67). |
| fig5c-selectivity-reduced | blocked (data_missing) | Depends on the claim above. |
| network-models | blocked (methods_underspecified) | A model result; its equations are in the Supplementary Information. |
| fig6c-vmval-reduced | not_reproduced | Activity falls to 43–56% (Q1) against 25 ± 2.5. The partial condition fails under P2 and P3, which have 1–5 significantly activated units (cell 45). |
| fig6b-selectivity-types-equally-inhibited | blocked (methods_underspecified) | Group readings and measures disagree: group set (a) differs often, group set (b) under the ratio never (cell 47). |
| fig6c-unmodulated-less-selective | partially_reproduced | Unmodulated units are less selective (p = 0.002–0.03 under P2 and P3) and r is negative (−0.14 to −0.28). Slope and r are outside tolerance in every reading (cell 49). |
| fig6d-localized | not_reproduced | Group counts are out in all 12 readings, e.g. 111 against 160 and 26 against 46. Near < far does hold under P2 and P3 (cell 51). |
| vm1-photoinhibition-no-effect | blocked (metadata_insufficient) | Agreed. The archive metadata name no vM1 site, and the (0.5, 0.5) galvo condition comes from 1 mouse, not 3. Under that guess, (b) holds and (a) holds in some readings. |
| fig6e-onset-latencies | not_reproduced | ALM 6–7 ms (within). VM/VAL is 14 ms (T1, just outside 8.0–13.8) or 4–7 ms (T2). Under O1, SNr (12 ms) is not the latest (cell 59). |
| snr-photoinhibition | not_reproduced | The reduction is 2.1–2.4 spikes/s against 3.6 ± 0.36 (5.6–6.3% against 8.3 ± 0.83), and 181 SNr units are deposited against 227 ± 23. The bootstrap p < 0.01 holds in most readings (cell 55). |
| snr-unit-properties | blocked (data_missing), tested in part | The 46 wider SNr units are not deposited; the "other" group has 10–13 units. Selectivity, 137–143 of 181, is within 152 ± 15 under the c1 readings. The rates (about 20.8) are biased low; see problem 3. |
| anatomy-reciprocal-thalamus | blocked (data_missing) | Confirmed: all assets are ecephys or icephys NWB files; there is no histology. |
| selectivity-time-course | reproduced (fragile) | All three conditions hold with ALM P1 or P2 and VM/VAL P3 (cell 61). They fail with VM/VAL P1 or P2, where selectivity does not rise over the delay. The rises that pass are tiny, e.g. 0.51 → 0.52 spikes/s. |
| alm-gabaergic-no-thalamic-projection | blocked (data_missing) | No histology. |

Totals: 7 reproduced, 2 partially reproduced, 13 not reproduced, 17 blocked.

## B. Problems

1. **[affects a conclusion]** `loop.load_wholecell` and cells 15, 64. The notebook says the whole-cell files hold no laser time. But the archive metadata list an `OptogeneticSeries` in all 36 whole-cell assets, and the loader never reads it (it reads only `general/optogenetics`). If that series holds the laser timing, the guessed onsets E and M are unnecessary. Four outcomes rest on them (wc-thalamus-hyperpolarization, wc-m1, wc-contra-alm, thalamus-stronger-than-cortex), and so does the 7.9 ms onset the claims file calls unjudgeable. indirect-pathway-too-slow might then also be partly testable.
2. **[may affect a conclusion]** `load_ecephys` windows and the cell 9 text. Cell 9 says "every window used below ends by 4.1 s after pole onset". That is false. The go cue falls up to 5.69 s after pole onset (99th percentile, cell 10), so the response windows reach about 7.2 s, beyond the roughly 5 s where stored spikes end. Whether storage ends relative to pole onset or to the cue was never shown. If it ends relative to pole onset, about 19% of trials (those with longer delays) have truncated response and delay counts. This bears on every selectivity claim (fig2e, fig2f, fig3b, fig6b, snr-unit-properties).
3. **[does not affect a conclusion]** Cell 57, snr-unit-properties. Rate readings (a) and (b) divide by session or trial time that includes periods with no stored spikes, so the rates are biased low. The sample-epoch variant gives 37.3 against 20.8. The claim is blocked anyway.
4. **[does not change an outcome; reliability]** `loop.onset_ms`. It takes the first bin past 3 SD and requires no persistence. In a synthetic test with no effect, it still reported an onset within 10 ms in 56% (O1) and 39% (O2) of runs. With a true step at 8 ms, it reported earlier than 8 ms in 41% and 26% of runs. The ALM O1 onset of 0.0 ms in cell 43 is this artefact. The fig3-onset-latencies pass rests on one reading (T1/O2) out of four.
5. **[may affect a conclusion]** Cell 41, `photo_effect` with the `delay` window. W1 runs from delay onset to the go cue. Where the delay is longer than the 1.2–1.3 s photostimulus, it takes in time after the laser is off. W1 is the only reading under which vgat-thalamus-reduction passes (W2 gives 1.5%). The notebook shows neither the delay lengths in the VGAT thalamic sessions nor the ratio over time.
6. **[does not affect a conclusion]** Cell 17, `GABA["P2"]`. For SNr it uses `cell_type != "Wide width spiking"` (168 units). The claims file's P2 is "Narrow width spiking" (146), so 22 "Cannot be determined" units are included in snr-photoinhibition, snr-unit-properties and the fig6e SNr onsets. Those outcomes fail either way.
7. **[does not affect a conclusion]** Cell 35, fig3d. Reading m2 uses Student's test only; convention P also gives Welch's.
8. **[does not affect a conclusion]** `loop.kink_clip`. The search starts exactly 1.5 ms before the spike peak. On a synthetic spike with a slow rise it returned the Vm at the start of the window (−55 mV) rather than the steep inflection (−45 mV). A threshold placed too early shrinks threshold-minus-basal. The deposited kink gives the same 6.9 mV, so the outcome stands, but the notebook does not report how often the kink falls on the window edge.
9. **[does not affect a conclusion]** Cell 0 lists snr-unit-properties as "blocked: data missing" while it also reports a selectivity part that is within tolerance. The record should state both.
10. **Selections.** No unit is used for both choosing and testing: the time-course split uses separate halves for preference and selectivity. The paper states no chance level for any selection. The notebook's shuffled-label check puts chance at 8–17% of units per session (cell 12).
11. **Checks that passed.** On synthetic input, `ttest_rows` matches scipy to 1e-16 for both Student's and Welch's tests. `selectivity_table` and `photo_effect` recover a planted delay-epoch selectivity and a planted photoinhibition effect.

## C. What I could not check

- **The whole-cell `OptogeneticSeries`.** I could not see its contents without downloading. A cell printing its name, timestamps or data around a few trials, against `pole_in_time` and `pole_out_time`, would settle problem 1.
- **Where spike storage ends.** A histogram of spike times relative to the go cue, for trials with delays above 2 s, would settle problem 2.
- **The VGAT thalamic sessions.** The delay-length distribution and the photostimulus/control ratio in 100 ms bins across the delay would test problem 5.
- **Missing units.** I could not confirm that the 248 missing ALM units are the Fig. 5 sessions. Recording dates and sorter per session, compared with the paper's 57 ALM sessions, would.
- **Kink placement.** The fraction of spikes whose kink is the first sample of the search window, per cell, would test problem 8.
- **Unit depth.** Whether `unit_y` in ALM is depth below the pia (fig3d) is not shown. The electrode-group metadata carry ALM coordinates for every region, so they could not tell me.
