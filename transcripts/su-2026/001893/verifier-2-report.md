**Verifier report, round 2: Su, Kosillo, Jung et al. 2026 against DANDI:001893 v0.260817.1647**

The claims file has 31 claims. The attempt record has 31 outcomes:
- 4 reproduced: patchseq-sample, patchseq-transcriptome-link, tau-table-link, patchseq-ap-waveform-spinal-vs-cortex.
- 1 more reproduced: patchseq-ap-waveform-spinal-vs-cerebellum.
- 3 partially reproduced: patchseq-ne-identity and the two tau claims.
- 23 blocked: 19 `data_missing`, 1 `methods_underspecified` (snrnaseq-single-cluster) and 3 `not_runnable`.

Cell indices below are those of the re-executed notebook.

### 1. Outcomes and assumptions

| Claim | Agree? | Basis |
|---|---|---|
| patchseq-sample | yes | Cell 10: every count matches the paper. |
| patchseq-transcriptome-link | yes | Cell 28: 64/64 libraries resolve with matching MD5s, and 128/128 files are in the col-s96tk9a manifest. |
| patchseq-ne-identity | yes | Cell 32: reading (a) 60/64 and reading (b) 58/64 cells; neither is 100%, both are at least 90%. Reading (b) passes by one cell (57/64 would be 89%); reading (a) holds up to CPM > 10. |
| tau-table-link | yes | Cell 20: 77/82 within 10% (94%). |
| waveform, spinal vs cortex | yes | Cell 15: p = 0.00011 in the main reading and 0.0097 in the code's variant. |
| waveform, spinal vs cerebellum | yes, but fragile | Cell 15: p = 0.029 in the main reading and 0.031 in the variant. Over mouse means p = 0.060; without the 8 wt/wt cells p = 0.19–0.20. The record says this. |
| tau, cortex vs spinal | yes | Cell 23: p = 0.0077 under the Methods' rule, which the criterion makes the main reading. |
| tau, cortex vs cerebellum | yes | Cell 23: p = 0.0025. |
| 19 `data_missing` | yes | Cell 37: the dandiset's approach is electrophysiology only. |
| snrnaseq-single-cluster | yes, blocked | The silhouette score is undefined at K = 1, and the paper does not say how it was computed. |
| 3 `not_runnable` | yes, blocked | The block rests on the author's choice not to reimplement the R selection of nuclei in Python. That choice is stated. |

**Assumptions.** The record contains no `assumed: true` field. The assumptions are carried as deviations instead:
- the input resistance used for the bridge part of the rule;
- IPFX's noise windows;
- 0 pA for sweeps with holding off;
- the four 1 s step sets used as long squares.

Each is stated and reasonable. None decides an outcome: Rin from all sweeps and X1PS sweeps alone give the same tau results (cell 23), and the 0 pA reading adds one cell.

### 2. Sentences the printed outputs do not support

- **"1,007 Snap25 read pairs" for cell 1409801288** (cell 35; record, patchseq-ne-identity notes). No per-gene read count is printed; cell 32 prints only CPMs.
- **"…read pairs of 51 bases"** (record, patchseq-transcriptome-link notes). No read length is printed; cell 28 gives only "175250 to 1110791 (median 655923)".
- **"None of these files marks which nuclei are the paper's 4,743 LC-NE nuclei"** (record, notes of all four sequencing claims). Cell 37 lists a cell table, `…RTX-4134_CR8_samp.dat_241111.rda` (31 MB), in col-qocsrc5 but never opens it. This bears on the reason for the three `not_runnable` blocks.
- **"…Code Ocean collection, whose data assets carry no DOI or fixed version"** (record, notes of the 19 `data_missing` claims). No notebook output shows this.
- **Cell 15 print label.** The line "amplitude, main minus code (pA), cells with a different sweep: median 10, range 0 to 10" takes its range over all 69 cells, not over the one cell with a different sweep. The conclusion in cell 17 ("one 10 pA higher") is still right, from the table (1408898882: 50 → 60 pA).
- **Cell 25: "That part rests on a value the lab notebook confirms: in every long square of the 18 cells…"** The autobias and baseline check covers 11 of the 16 spinal cord cells the bias part drops. The other 5 are covered only by the global check (2,433/2,433 sweeps where the NWB value equals the notebook's holding level). This is a wording overreach, not a wrong number.

**Checked and supported.** Every other number in:
- the "**Result:**" cells (11, 17, 18, 21, 25, 26, 30, 35);
- the Summary (cell 38), including "19 other claims", which matches the record's 19 `data_missing` outcomes;
- the README;
- the record's notes.

The values checked include the p, t, df, n and means in cells 15 and 23; the counts in cell 13 (18 cells; Vcom −70 to −41 mV; within 1.5 mV); and the comparison with STAR in cell 34.

**Round-1 reasons in the record.** The `verifications` block states my round-1 reasons faithfully, close to my wording, with each problem attached to the right claims. Nothing is misattributed.

### 3. Round-1 points

| Point | Status |
|---|---|
| 1. Meaning of `bias_current` | **Resolved.** The MIES lab notebook confirms it is the applied holding current: 2,433/2,433 sweeps match. In the 18 cells with no sweep within ±100 pA, autobias is on and the baseline is within 1.5 mV of the target. The partial tau outcomes now stand on a verified reading. |
| 2. Rin for the bridge rule | **Resolved.** It is stated as a deviation, and the `rin_all` reading leaves the verdicts unchanged. |
| 3. The 8 wt/wt cells | **Resolved as far as the data allow.** The PCA was refitted without them, mouse-level tests were added, and none of the 8 has a transcriptome. |
| 4. k-mer counting | **Resolved.** On 60 retro-seq nuclei the k-mer counts agree with STAR (ρ 0.98–0.995, the same four-marker call in 60/60). |
| 5. NeMO child collections | **Resolved.** The notebook lists them and the block reasons are corrected. |
| 6. Negative seal values | **Resolved.** The median over test pulses is now reported as well. |
| 7. donor_local_id check | **Resolved.** The check now asserts both columns and compares them (96/96, none missing). |
| 8. Collection membership | **Resolved.** The col-s96tk9a manifest lists all 128 files. |

**What remains that bears on a conclusion:**
- **The three `not_runnable` blocks** rest on an unsupported statement: that no file marks the 4,743 LC-NE nuclei. The `samp.dat` cell table should be opened before that reason stands.
- **Claims-file misreading (reported, not corrected).** The check entry for snrnaseq-single-cluster says "the Methods say only that silhouette scores were always highest with a single cluster". In fact the Methods (Cluster quality analysis) also say "we observed a large decrease when k increased from 1 to 2 regardless of which method was used". The phrase the check removed is in the paper, and it offers a reading in which K = 1 has a defined score.
- **Minor.** Cell 1392357828 stays in the tau main reading only through sweeps recorded with holding off, at a baseline of −22.7 mV. No result is shown without it. It is one of 36 spinal cord cells and is unlikely to move p across 0.001.
