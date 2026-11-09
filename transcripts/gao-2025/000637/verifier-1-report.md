**A. Outcomes**

The claims file has 31 claims. I mark all 31 as blocked. The notebook's own count of 30 (cell 0) is wrong; see B1.

| Claim id | Outcome | Reason |
|---|---|---|
| unit-counts | blocked (data_missing) | Every count is split into RSUs and FSUs, which needs waveforms. Every Units table has only `spike_times` (cell 7), and the archive lists only `Units` and `ElectrodeGroup` as measured for all 292 assets. There are no POm units. "Reproduced" can be ruled out anyway: cell 16 finds 4,642 / 1,088 / 862 S1 units, against the paper's RSU+FSU sums of 1,297 / 366 / 209. A two-cluster split puts every unit in one class, so at most one count of each S1 pair can match. |
| fig4-s1-rsu-timelocked-3000 | blocked (data_missing) | There are no waveforms, so there are no S1 RSUs to select. |
| fig4-pom-rsu-timelocked-3000 | blocked (data_missing) | There are no POm units: one probe per file, location "unknown", and the description says S1 only. |
| fig4-post-3000 | blocked (data_missing) | Needs POm RSUs and S1 cell types. |
| fig4-30hz-s1-rsu-inhibition | blocked (data_missing) | No cell types. The recordings exist: 26 at 30 Hz / 200 µs (cell 14). |
| fig4-30hz-pom-rsu-delayed | blocked (data_missing) | No POm units. |
| fig4-fsu-no-change | blocked (data_missing) | No FSUs and no POm units. |
| fig5-sham-no-response | blocked (data_missing) | No cell types and no POm units. Three files are named BASELINE, but nothing in them says they are sham sessions. |
| fig5-cg1-control-no-response | blocked (data_missing) | No identifier or metadata names a CG1 target. All 292 files have the same `session_description`, "Neural Spikes for S1 tFUS". |
| fig6a-s1-rsu-timelocked-high-prf | blocked (data_missing) | The conditions are present (PRF series at 200 µs), but there are no cell types. |
| fig6a-s1-rsu-delayed | blocked (data_missing) | Same as fig6a-s1-rsu-timelocked-high-prf. |
| fig6b-s1-fsu | blocked (data_missing) | No FSUs. |
| fig6c-pom-rsu-timelocked | blocked (data_missing) | No POm units. |
| fig6c-pom-rsu-delayed | blocked (data_missing) | No POm units. |
| fig6d-pom-fsu | blocked (data_missing) | No POm units. |
| fig7a-s1-rsu-dc-3000 | blocked (data_missing) | At 3000 Hz only 30% and 60% DC exist (100 and 200 µs). The 0.6, 6 and 90% DCs are missing, and there are no cell types. |
| fig7b-s1-fsu-dc-3000 | blocked (data_missing) | Same as fig7a. |
| fig7c-pom-rsu-dc-3000 | blocked (data_missing) | No POm units, and DCs are missing. |
| fig7d-pom-fsu-dc-3000 | blocked (data_missing) | No POm units, and DCs are missing. |
| fig8a-s1-rsu-dc-30 | blocked (data_missing) | At 30 Hz only 0.6% DC exists (cell 14), and there are no cell types. |
| fig8b-s1-fsu-dc-30 | blocked (data_missing) | Same as fig8a. |
| fig9a-s1-rsu-60dc | blocked (data_missing) | Only 1500 Hz and 3000 Hz at 60% DC exist, and there are no cell types. |
| fig9b-s1-fsu-60dc | blocked (data_missing) | Same as fig9a. |
| fig10a-dsttc-3000 | blocked (data_missing) | Needs S1–POm pairs. |
| fig10b-dsttc-30 | blocked (data_missing) | Needs S1–POm pairs. |
| fig10c-sttc-constant-pd | blocked (data_missing) | Needs S1–POm RSU pairs. |
| fig10d-sttc-60dc | blocked (data_missing) | Needs S1–POm RSU pairs; DCs are also missing. |
| fig10ef-sttc-dc | blocked (data_missing) | Needs S1–POm RSU pairs; DCs are also missing. |
| fig11b-ac-responses | blocked (data_missing) | No auditory-cortex units. This claim does not need cell types, but no file holds AC data. |
| fig11c-ac-s1-dsttc-30 | blocked (data_missing) | No AC units. |
| fig11d-ac-s1-dsttc-3000 | blocked (data_missing) | No AC units. |

**Archive check for the blocked claims.** I queried the API for version 0.250829.1249. It has 292 assets from 25 subjects, and every asset lists `variableMeasured` = [Units, ElectrodeGroup]. No asset path or metadata mentions POm, AC, CG1 or sham, and the files are 0.9 to 7 MB each. No part of any claim can be tested as the criteria state it. The only partial content is that the S1 recordings for the PRF-at-200 µs series, and for some DC conditions, are present.

**B. Problems**

1. [does not affect a conclusion] Cell 0 says "All 30 claims are blocked". The claims file has 31. The summary table does cover all 31 ids.
2. [does not affect a conclusion] Cells 0 and 16 never ask whether 000637 holds this paper's recordings at all.
   - The paper's data statement names DANDI:000946.
   - The dataset has 25 rats; the paper's two groups total 16 + 12 = 28.
   - The S1 unit totals are 3.6 times the paper's RSU+FSU sums.
   - The dataset may include the S1 probes of the auditory-confound group, or be different recordings.
   - The ratio is printed but not interpreted. Since all claims are blocked anyway, this changes no outcome.
3. [does not affect a conclusion] Cell 16 misses that the S1 totals already rule out "reproduced" for unit-counts, whatever the classification (argument in A). The outcome stays blocked because the six POm counts cannot be checked.
4. [does not affect a conclusion; this is a problem in the claims file, which I report and do not correct] Reading N2 of Method S (mean over trials of the per-trial ratio) is strongly biased downward for low-rate units.
   - On synthetic Poisson units with no response (`tfus.unit_table`), N2 came out at 16–23% at 3 Hz and about 110% at 30 Hz.
   - The notebook shows the same bias: mean N2 is about 60–80% in every window, including the BASELINE recordings (cells 18 and 21).
   - Under reading R2 (tests against 100%), N2 would produce spurious "decreases" and suppress increases. If the data had allowed testing, this would have pushed claims toward blocked or not_reproduced for an artefactual reason.
5. [does not affect a conclusion] In the cell 10 clock check, the "null" condition is not null: with onsets shifted by 1.2 s, all windows are significantly *below* the shifted pre-window (p down to 2e-76). Activity from the stimulus seems to persist, or trial structure seems to show, more than 1.1 s after onset. The contrast with the true onsets still supports trial start as the tFUS onset.
6. [does not affect a conclusion] Cell 21 is not discussed in the text: the BASELINE recordings show a pooled S1 increase at 134–201 ms (W2, p = 6e-9) and at 201–268 ms (W2, p = 1e-5), though not under W1. If these files were sham sessions, this would weigh against fig5-sham-no-response. The identity of the files and the missing cell types keep that claim blocked.
7. [does not affect a conclusion] `parse_identifier` assumes a two-digit voltage field means tenths of a volt ("55" read as 5.5 V). A "10" would become 1.0 V. This is not checked, but only 5, 55, 7 and 35 occur.
8. [does not affect a conclusion] Helpers tested on synthetic inputs:
   - `window_counts` uses half-open windows [a, b), which is correct.
   - The `>2000` spike rule is applied as "more than 2,000", which is correct.
   - `duty_cycle` is correct.

**C. What I could not check**

- **No waveforms anywhere in the files.** The notebook lists only the Units `colnames`, `acquisition` and `processing`. Two outputs would have settled this:
  - a full HDF5 tree per file (`f.visit`), covering `/analysis`, `/scratch`, `/stimulus`, extra Units datasets not listed in `colnames` (such as `waveform_mean`), and the electrodes-table columns;
  - the electrode-group descriptions.
- **No CG1 or sham sessions.** The notebook shows only identifiers and `session_description`. Printing `general/experiment_description`, `general/notes`, `general/stimulus` and the electrode-group `location` / `description` for every file would have settled this.
- **Whether the BASELINE files are sham, and whether 000637 is the subset of the paper's data the paper used.** This would need the same metadata fields, plus a per-subject comparison of unit counts against the paper's sham n of 31 + 53 S1 units.
