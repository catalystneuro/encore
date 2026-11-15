**A. Outcomes** (25 claims, from the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| counts-neurons-subjects | reproduced | Cell 10: 1864 unit rows (+1) and 59 subjects. With duplicated trains counted once it is 1798 (−65), also within tolerance. |
| counts-sessions | reproduced | Cell 12: the 87 (subject, session) pairs in the files are exactly the 87 pairs in Online-only Table 1. The Methods' 89 is reported. |
| table1-demographics | partially_reproduced | Cell 14: age and sex both match for 56 of 59 subjects (C24, H33 and H48 differ). The files give 26 F / 33 M against the table's 25 / 34. |
| task-structure | partially_reproduced | Cell 16: 79/87 sessions have 100 distinct encoding images (seven have 50, session 123 has 97). Recognition labels (50/50) hold in 87/87 and 5 categories in 87/87. |
| new-old-label-coding | not_reproduced | Cell 18: both tests hold with the labels reversed in 78/87 sessions and under the stated coding in 0/87. Label-0 images never appear in the encoding block. |
| ttl-codes | partially_reproduced | Cell 20: 78/87 files meet all three conditions. Lengths and timestamps match in 87/87; 9 files hold other codes (0, 4, 22, 23, 98, 99) or trials out of order. |
| experiment-ids | partially_reproduced | Cell 22: 83/87 files are in the stated sets. Sessions 55, 77, 100 and 105 use 82 (or 81 or 83 in the wrong role), and the files' data_collection field says the same. |
| session-dates | partially_reproduced | Cell 24: 86/87 files fall on the first of a month; session 48 is on 2010‑03‑13. Session 68 has the year 2000, outside the 2006–2019 span. |
| units-table | partially_reproduced | Cell 26: IsolDist is missing and IsolationDist is present instead. Electrodes are 1:1 and the waveform rate is 98.4 kHz (within tolerance). SNR is not finite for 86 units and IsolationDist for 493, in 84 sessions. |
| electrodes-table | not_reproduced | Cell 28: `imp` is empty for all 887 electrodes, which is the criterion's not_reproduced case. Coordinates are missing in 8 sessions. |
| isi-criterion | partially_reproduced | Cell 30: 1858/1864 units (99.68%) are below 3% with spikes sorted, and 1860 with the stored order. Both readings are at least 95% but not all units. |
| fig5a-mtl-locations | reproduced | Cell 32: all 1864 units are in the amygdala or hippocampus. |
| fig5c-auc-all | reproduced | Cell 36: mean 0.753 (0.74 ± 0.10) and SD 0.094 (0.10 ± 0.01) over 87 sessions. |
| fig5c-auc-sites | reproduced | Cell 38: CS 0.760, SD 0.085; TWH 0.688, SD 0.138. All four are within tolerance; Welch p = 0.161. |
| fig5b-roc-asymmetric | reproduced | Cell 40: mean z-ROC slope 0.782 over 82 sessions, t-test against 1 p = 4.3e‑9. The Wilcoxon and pooled-ROC (0.816) variants agree. |
| fig5d-confidence-accuracy | reproduced | Cell 42: fixed split 80.1% against 60.9%, paired p = 3.2e‑16 (84 sessions, 3 left out). The dynamic split gives p = 1.3e‑11. |
| vs-cells-proportion | reproduced | Cell 46: 332 of 1864 (17.8%) in the Methods window, within 343 ± 34.3 and 18.4 ± 1.84%. The shuffled null is 86.8 units. |
| ms-cells-proportion | not_reproduced | Cell 48: the main reading gives 112 (6.0%), outside 146 ± 14.6 and 7.8 ± 0.78%, and stays at 108–117 across five seeds. Only variants fall within: the code's choices give 151 (8.1%) and the Methods window with correct trials gives 137 (7.3%). |
| dual-cells-proportion | not_reproduced | Cell 50: the main tests give 12 (0.64%) against 26 ± 2.6. The code's choices give exactly 26 (1.39%). |
| fig5f-site-proportions | partially_reproduced | Cell 52, main selection: no Fisher test is significant, but only 3/6 values are within tolerance. Under the code's choices 6/6 are within and no test is significant. |
| twh-sessions | reproduced | Cell 54: 9 sessions with a T label, institution "Toronto Western Hospital". |
| previous-release-link | partially_reproduced | Cell 56: 64/65 sessions of Faraut Table 1 are found and agree (98.5%). Session 98 (H48) is missing. Age matches for 60/64 and sex for 63/64. |
| previous-release-additions | partially_reproduced | Cell 58: 23 new sessions and 17 new subjects are within tolerance; 325 new neurons is outside 288 ± 28.8. The difference-of-totals variant gives exactly 288 (1864 − 1576). |
| fig4-example-vs-neuron | reproduced | Cell 60: the single unit on channel 177 (electrode row 4, right amygdala) has ANOVA p = 1.2e‑22, and animals give the highest rate (6.75 Hz against ≤ 0.85 Hz). |
| fig3-example-vs-neuron | blocked (data_missing) | Session 144 is in neither the dandiset, Online-only Table 1 nor the OSF deposit (cell 62). I confirmed in the API that the draft, 0.220126.1851 and 0.220126.1852 versions each hold the same 87 assets, and asset metadata carry no session ids. |

The paper states no chance level for any selection. The notebook's shuffled nulls (about 87–92 units, against 93 expected at 5%) fit a 5% false-positive rate.

**B. Problems**

1. [affects a conclusion] Claims file (ms-cells-proportion, dual-cells-proportion, fig5f-site-proportions, vs-cells-proportion). The main reading follows the Methods text (0.2–1.2 s window, all 50/50 trials), and it is a faithful reading of the text. However, the code's choices (0.2–1.7 s window, correct trials only; single_neuron.py `vs_test`/`ms_test`, which I read at commit 1d95162) reproduce the paper's numbers exactly:
   - VS 343
   - dual 26
   - TWH 15/8/1 of 77 units, which are the Fig. 5f constants 19.4%, 10.4% and 1.3%
   - CS 18.4% and 1.4%
   
   So the paper's numbers were produced with the code's choices, and the text describes a different method. The not_reproduced outcomes for MS and dual come from that discrepancy between text and code, not from the data. The notebook ran both readings, which is correct. This is not a notebook error.
2. [does not affect a conclusion] Claims file, fig5f-site-proportions. The paper's sentence says the percentages were "comparable to previously reported percentages in our locally recorded dataset" (ref. 10), which is a comparison with earlier publications. The claim recasts it as CS against TWH. The Fig. 5f legend's site split supports this reading, but it is not what the sentence says.
3. [does not affect a conclusion] `accuracy_dynamic_split`. It follows the Python code's mode 1, which drops confidence 5 from both groups. The docstring says so. The fixed split passes on its own, so the outcome does not change.
4. [does not affect a conclusion] Cell 0 says this is the "only published version holding the 87 sessions". The API shows 0.220126.1851 with the same 87 assets and the same byte size.
5. [does not affect a conclusion] Cell 24. 38 sessions store trial times as Unix timestamps that reveal the true day of the experiment, which defeats the de-identification the claim describes. The criterion only looks at session_start_time, so the outcome stands.
6. [does not affect a conclusion] `vs_p` returns NaN when every group is constant even if the group means differ. In this run that only hits the 6 units with zero spikes.
7. [does not affect a conclusion] `trial_event_order` and `check_responses_against_events` assume the smaller experiment id is the learning block. That holds for every pair seen (80/82, 81/82, 82/83), and the event check found no mismatches.

Other checks came out clean:
- **Synthetic tests:** `auc` matched sklearn's rank AUC to within 0.0004 on three simulated sessions. `window_rates` excludes spikes on the window edges, as `win_spike_rate` does. `bootstrap_p` gave a 7.75% false-positive rate in 400 simulations, but the real-data null (92.4 units against 93) is calibrated.
- **Agreement with the paper's code at commit 1d95162:** `adjust_hf`, `zroc_slope` (first five points), `auc`, `typecounters` (label 1 = old) and the bootstrap all match. `ms_test` in the paper's code also treats label 1 as old.

**C. What I could not check**

- The stored values of `imp`, which the notebook does not print. Printing the dtype and a few raw values would confirm they are NaN and not something like 0 or a placeholder.
- The task variants' category names per session. A table of category_name by session, plus a search for right-hippocampus units on origChannel 140 preferring "phones", would show whether any substitute for the Fig. 3 neuron exists. It still would not be the claimed session 144.
- Cell 3's per-file table was cut off in the output I read (files beyond row 32). The totals in cells 4 and 10 cover all 87 files.
- Whether the Europe PMC tables parsed completely (`patient_table`). The totals (59/87 and 42/65) match the papers, but printing the parsed rows would allow a row-by-row check against the PDF tables.
