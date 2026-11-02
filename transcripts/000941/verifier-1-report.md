**A. Outcomes** (26 claims in the claims file; the notebook tests 3 of them and blocks 23)

| Claim | My outcome | Reason |
|---|---|---|
| table2-trial-counts | blocked (data_missing) | Cell 17: the paper's session file has 412 trials, all `R`, and no failed trials. Trial numbers run 201–673 against the paper's 768 total. The file is the FALCON calibration subset, so no count can be compared, and monkeys X and Y are absent. |
| table2-movement-time | blocked (metadata_insufficient for L; data_missing for X and Y) | Cell 19 gives a median of 200 ms (41 samples) for L, outside 229.5–280.5. But the dataset's `move_onset_time` is not shown to be the paper's M, and the evidence below suggests it is not (problem 1). Taken at face value under the claims file's "use the dataset's onset" rule, L would be not_reproduced. The Kruskal-Wallis test cannot be run. |
| fig2-trial-count-coax-45 | blocked (data_missing) | Cell 22 finds 19 trials (16 under the approximate reading (a)) against 28. The file holds only 412 of the 717 successful trials (0.57 × 28 ≈ 16), so the count is not comparable. The object naming is sound (problem 4). |
| fig2-joint-patterns, fig2-hand-opening-two-phases, fig4-armps-time-course, the 11 fig5/fig6/fig7 claims (fig5 ×8, fig6a, fig6b, fig7 ×3), fig8a, fig8b, fig8-hand-shape-invariant-to-location, fig9-hand-configuration-location, fig10-forearm-trajectory-object, elbow-point-trajectory-object | blocked (data_missing) | Cell 24 shows the only series in all 11 files are `eval_mask` and `preprocessed_emg`. I checked the archive myself (problem 5). There are no joint angles or markers, so no part of these 23 claims can be tested. |

**B. Problems**

1. [affects a conclusion] Cells 18–19, table2-movement-time: the notebook assumes `move_onset_time` is the paper's marker-speed onset M and never checks it. Two papers in `paper/` cut against that:
   - **EMG paper (jn.00008.2016), Table 2:** medians for the same four sessions are 238, 255, 232 and 253 ms (L20120928: 253 ms, 676 trials). Cell 19 gets 180, 200, 180 and 200 ms from the files. That is a steady shortfall of about 40–55 ms in every session, and a 20 ms grid cannot explain it.
   - **Cue-to-onset interval:** the files give a median of 300 ms (cell 7). The J Neurosci 2016 paper gives the minimum median I–M across monkey L's sessions as 243 ms.

   Together these point to a later onset event in the dataset, such as release of the center object, rather than the marker-speed onset. So "not reproduced" is not a sound reading here. The notebook does say the event times are "consistent with, but does not show, the paper's definitions", but it draws no consequence from that.
2. [does not affect a conclusion] Cells 17, 19 and 22, `prev_present`: approximating analyzed trials as "preceding number present" treats every absent trial number as an error trial. Many absent numbers are more likely trials held back in other FALCON splits. The notebook calls this an approximation, and the medians are the same either way (200 ms).
3. [does not affect a conclusion] Cell 19: the per-session medians print with floating-point residue (180.00000000006366). This is cosmetic.
4. [does not affect a conclusion] `infer_object_names` names the object codes by inference, since the files do not name them. I tested it on 200 synthetic block sequences with randomly coded objects and it named every code correctly (200/200). The paper's constraints (sphere and button never at the leftmost locations, perpendicular cylinder not at the rightmost) leave only the clockwise assignment. The crosstab in cell 9 satisfies them, with 24 combinations.
5. [does not affect a conclusion] I checked the blocked claims against the archive. The API for version 0.241029.1405 lists the same 11 assets (311.8 MB). The metadata's `variableMeasured` lists only Units, ElectrodeGroup and BehavioralTimeSeries (the EMG). The description names only EMG, `eval_mask`, spikes and trial metadata, and says the calibration split contains "many trials", not the whole session. This confirms data_missing for the 23 kinematic claims and for the trial counts.
6. [does not affect a conclusion] Cells 11–15, the data and clock checks (minival duplicating calib, decoding `obj_id` from EMG): they are well controlled (next-trial labels as control, chance level printed) and feed no claim.

**C. What I could not check**
- What `move_onset_time` and `contact_time` mean in the FALCON files; neither the files nor the archive metadata define them. Three outputs added to the notebook would settle it:
  - each session's median movement time from the files next to jn.00008.2016 Table 2;
  - cue-to-onset medians next to the J Neurosci 2016 I–M value;
  - mean EMG (for example DLTa and EDC) aligned on `move_onset_time`, showing whether onset leads or lags the rise in activity.
- Whether the withheld FALCON held-in evaluation trials (not on DANDI) would complete the session. This is outside the archive and the claims file, so it does not change the blocked outcomes.
- The notebook's figures, which reached me only as text; their printed ranges are consistent with the tables.
