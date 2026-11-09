**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| fig1-pole-dimming | blocked (data_missing) | The test needs the Di-8-ANEPPS 1-µs escalation (Fig. 4B, n = 5). All 72 files name FluoVolt (cell 5). I confirmed this from the archive's asset metadata: FluoVolt in 72 of 72, no Di-8-ANEPPS. |
| fig2a-fluovolt-saturation | blocked (data_missing) | Needs the FluoVolt escalation at 43–1400 V/cm in 40+60-image sets, n = 4. The FluoVolt single-pulse sets here (c6, c7) are at 150/520/900/1270/1570 V/cm in 20+40 frames, with no 360 or 570 V/cm levels. |
| fig2a-fluovolt-stable | blocked (data_missing) | It is not the paper's experiment. The dataset's own FluoVolt sets could have given a variant (see B4). |
| fig2b-di8-climbs-to-570 | blocked (data_missing) | No Di-8-ANEPPS data. |
| fig2b-di8-bleaching | blocked (data_missing) | No Di-8-ANEPPS data; no 43 V/cm set. |
| fig2b-di8-decline-within-set | blocked (data_missing) | No Di-8-ANEPPS data. |
| fig2cd-stable-before-electroporation | blocked (data_missing) | No 150/230 V/cm alternation (cell 5: every field of view escalates 0→250 V). |
| fig2c-1000-within-set | blocked (data_missing) | Same reason. |
| fig2d-lasting-reduction | blocked (data_missing) | Same reason. |
| fig3-dye-sensitivity | blocked (data_missing) | Needs 43–360 V/cm sets of both dyes and IMPC, which needs R in µm. The files give no pixel size (cell 10) and hold no Di-8-ANEPPS. |
| fig3-fluovolt-nonlinear | blocked (data_missing) | Depends on fig3-dye-sensitivity; same data missing. |
| fig4a-fluovolt-limits | blocked (data_missing) | Not the paper's FluoVolt escalation (field levels, electrodes 1.00 vs 1.6 mm, frame counts). No pixel size for IMPC. |
| fig4a-fluovolt-cathodic-decline | blocked (data_missing) | No 360, 1000, 1200 or 1400 V/cm sets; not the paper's cells. |
| fig4b-di8-limits | blocked (data_missing) | No Di-8-ANEPPS data. |
| fig4b-first-10-pulses | blocked (data_missing) | No Di-8-ANEPPS data. |
| fig4b-cathodic-asymmetry | blocked (data_missing) | No Di-8-ANEPPS data. |
| fig4c-equator-follows-cosine | blocked (data_missing) | No Di-8-ANEPPS data. |
| fig4d-short-pulses-same-limit | blocked (data_missing) | No 0.3-µs pulses; every description names 1-µs pulses. |
| fig5a-gd-extends-anodic | blocked (data_missing) | No Gd³⁺ sets. I searched the asset metadata: no "Gd". |
| fig5a-gd-linear | blocked (data_missing) | No Gd³⁺ sets. |
| fig5a-gd-cathodic | blocked (data_missing) | No Gd³⁺ sets. |
| fig5a-gd-differences | blocked (data_missing) | No Gd³⁺ sets. |
| fig5b-conductivity-calibration | not_reproduced | Cell 16 gives a 1.33% reduction for a 10-fold rise under reading (a) and 1.20% under (b); the target is 2 ± 0.2. The 100-fold reduction is 11.87% (a) and 11.75% (b), within 12 ± 1.2. Both values must be within tolerance, so the claim fails under both readings. I recomputed Eq. (2) separately and got the same values, and the thin-shell approximation agrees. |
| fig5c-gd-reduces-conductivity | blocked (data_missing) | No Gd³⁺ sets. |
| fig6a-ca-single-pulse | blocked (data_missing) | No Fluo-4 or Ca²⁺ imaging; FITC FluoVolt strobe images only. |
| fig6b-ca-train-responders | blocked (data_missing) | Same. |
| fig6b-ca-650 | blocked (data_missing) | Same. |
| fig7a-cosine-profiles | blocked (data_missing) | The criterion specifies Di-8-ANEPPS, n = 5. The 5-µs pairs here (c2, c9; interval counts confirmed in asset metadata) are FluoVolt, use conditioning fields 520/900/1270/1570 (not up to 1000, 1200, 1400), and hold 4 cells in 2 fields of view. |
| fig7b-charging-during-pulse | blocked (data_missing) | The criterion takes the data from Fig. 4B (Di-8-ANEPPS escalation), which is absent. |
| fig7ab-test-pulse-recovery | blocked (data_missing) | Same mismatch as fig7a: dye, field levels (no 760/1000/1200/1400), n. Cells 20–22 measure the dataset's own FluoVolt pairs and correctly decide no claim. |
| fig7c-fast-conductivity-drop | blocked (data_missing) | Depends on fig7b and fig7ab, both blocked. |
| fig7c-full-reseal-mild | blocked (data_missing) | Depends on fig7ab. |

Totals: 32 claims in the claims file. 1 is not_reproduced and 31 are blocked (data_missing). I checked every blocked claim against the archive: 72 assets in version 0.261006.1833, all FluoVolt with FITC, 1.00-mm electrodes, 1-µs pulses at 50–250 V, intervals 1/5/25/125/250 µs, 12 files each. No part of any blocked claim can be tested on the paper's own experiments. The one partial exception is fig2a-fluovolt-stable (see B4).

**B. Problems**

1. [does not affect a conclusion] Claims file header, not the notebook. It assumes from the dandiset title that the data are the Fig. 7 two-pulse experiment, and it plans 20/40-frame collapsing as the only deviation. The files show a different dye (FluoVolt), different electrodes (1.00 mm), different field levels and five intervals. The paper's Discussion names varying the interval as future work. So the claims file's premise that this dataset holds Fig. 7 is not supported. Reported, not corrected.
2. [does not affect a conclusion] Cell 0 markdown says "Figures 2A, 3 and 4A a FluoVolt escalation". Fig. 3 uses both dyes, which the claims file states.
3. [does not affect a conclusion] fig5b (cell 16): the code matches Eq. (2) and the Methods constants, and both readings ran. The R/d grid is labelled a variant and correctly not used; R = 12 µm would give 1.98%, but the paper fixes R = 8 µm. The 1.2–1.3% result matches the claims file's own open note. The mismatch looks like the paper's, not the code's.
4. [does not affect a conclusion] fig2a-fluovolt-stable is not run even as a variant, although the dataset has FluoVolt baselines and 1270/1570 V/cm sets. Cell 13 already shows relevant instability: frame 0 is 0.64 of frames 1–19, and in sham sets the last 40 frames are 9–17% dimmer than the first 20 on the cells.
5. [does not affect a conclusion] In the descriptive section (helper `profile_df`, `pole_frames`, `N_BASE = 20`), F0 includes frame 0, which is dimmed by about 36% (cell 13). This biases every dF in cells 13–23. Those cells decide nothing.
6. [does not affect a conclusion] `cathode_angles` takes the field direction from the response it then measures. This is circular, though stated as an assumption, and is used only in the descriptive cells 9–23.
7. [does not affect a conclusion] `field_of` maps 50–250 V onto the description's list in order, which is not proportional to voltage. Cell 14 flags this and says it cannot be checked; it is used only descriptively.

**C. Not checked**

- The image-level reductions (cell detection, trace placement on the membrane). No overlay of the traces on the mean images is output. It would matter only for the descriptive section, not for any outcome.
- Which constants the paper's Fig. 5B curve actually used. Figures were not opened by the claims writer or by me. Tabulated values read off the Fig. 5B curve (reduction at 10× and 100×) would show whether the paper used other R or d values than Methods 2.3 states.
- The asset metadata let me confirm dye, electrodes and intervals across all 72 files. Frame counts and pixel size I could take only from the notebook's cells 3 and 10.
