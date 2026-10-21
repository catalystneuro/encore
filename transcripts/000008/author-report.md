I did steps 1 to 5 of the Author section and ran the handover. The entry is `entries/000008-scala-2021/`: three notebooks plus the helper `scala.py`. The record is `attempts/000008-scala-2021-01.yaml`, with one question in `questions/000008.yaml`. I added two link claims to the claims file and listed the first one under `depends_on` of every claim that uses the paper's table. `entry.py check` reports 0 errors and all three notebooks pass `entry.py run`. Nothing is committed.

## 1. Outcomes (35 claims)

| Outcome | Claims |
|---|---|
| Reproduced (23) | link-metadata-table, link-ephys-features, cohort-ages, soma-depth-count, ed4-example-cell, ephys-feature-count, fig2-family-features, fig3d-families-ephys, ed6-it-et-room-features, l45-it1-boundary, fig5a, fig5b, fig3d-morph-combined*, hold-time-yield*, fig2-rrr*, ed5-rrr-ion-channels*, fig4c*, ed7*, fig4d*, fig4b*, rnaseq-depth†, ttype-qc-counts†, ed2-smartseq-similarity† |
| Partially reproduced (5) | cohort-cells-mice (1,325 distinct recordings), cohort-genotypes (9 of 10 lines), stimulus-protocol (89.0% conform), fig1a (76 t-types, not 77), fig1b (18 of 19 t-types) |
| Not reproduced (1) | ed8-leiden-entropy (rho 0.266, one-sided p 0.061) |
| Blocked (6) | methods_underspecified: fig4a, fig5c, fig5d (the claims file's readings disagree), ed6-physiological-temperature, fig4e; data_unreadable: morph-reconstructions (Brain Image Library server timed out) |

\* also uses the paper's own data from outside the dandiset (`with_inputs`); † uses data the paper deposited elsewhere.

## 2. Dataset and questions

**Version.** I pinned 0.211014.0809, the latest published version, because the paper cites none. Version 0.211014.0808 has the same 1,328 assets.

**What is wrong or missing in the files:**
- **Duplicated recordings.** Three pairs of cells (same mouse, different slices, one pair with different t-types) have identical voltage recordings. The paper's feature table has identical values for each pair, so the paper analysed the duplicates too. I counted each recording once and show results with all cells beside.
- **Other traces.** Three files hold different traces from the ones the paper's features came from. Features from the other 1,320 files match the published table exactly, apart from the rheobase, which the paper's code fits with an unseeded random procedure.
- **Depth fields.** `cortical_thickness_4x` actually holds the soma depth and `cortical_thickness_um` the cortical thickness, both in 4x image units. `soma_depth_um` is empty in all 43 files that have it, and the paper's µm depths are not in the dandiset.
- **Units.** Voltages are labelled volts but are mV; currents are labelled amperes but are pA.
- **No timing.** No sweep has a start time, so the intervals between pulses are lost. Each file holds one series of steps, with no repeats.
- **Labels.** The five cells the paper excludes are not marked, so the exclusions come from the paper's table. The files use the old `PT` name for the ET subclass.
- **Smaller points.** One file has voltages of ±1,025 mV in some sweeps. One mouse has a genotype the paper does not list (Scnn1a-Cre).

**Question asked:** one, on fig5d. The permutation p-value is 0.0505, so the random seed decides whether reading (b) passes.

## 3. Where the protocol was unclear or did not fit

1. "Count each recording once" gives no rule for which cell of a duplicated pair to keep. I kept the cell with the lower sample number and showed the all-cells result beside it.
2. Claims marked `dataset` needed five exclusion flags from the paper's table. That is neither `with_labels` (they are not names for codes) nor `with_inputs`. I kept `data: dataset`, added the link claim, and also report the counts from the files alone.
3. The protocol implies the author edits other claims' `depends_on` when adding a link claim. I did that and changed nothing else in those claims.
4. stimulus-protocol could only be partly tested, and there is no outcome for that. I used partially_reproduced and recorded the missing part as a deviation.
5. An `elsewhere` archive that does not respond has no block reason of its own. I used data_unreadable.
6. "Stream, don't download to disk": `remfile` took about 6 s per file, so I read whole files into memory over HTTPS. Nothing touches disk.
7. Runtime: the paper's feature extraction takes about 15 minutes, and each notebook must redo it because nothing may be read from files. The notebooks take 21, 18 and 4 minutes, well over the 10-minute aim.
8. `glmnet_python` cannot be installed on Python 3.13. I used scikit-learn's estimator of the same objective and recorded it as a deviation, not a block. It reproduces the code's printed R2 and correlations.
9. "scikit-learn defaults, as the code" is ambiguous because the k-means default changed in 2024. The code ran under Python 3.7.9, where the default was 10 initializations, so I used that and showed today's default as a variant. The outcome depends on it.
10. The protocol says a random seed cannot change an outcome; in fig5d it does. I showed the spread over seeds and asked the question.
11. After the final run I corrected a few lines of conclusion text, including removing bold, without a third 43-minute run. Only markdown cells changed, in both the source and the executed copies; every code cell was checked identical.

## 4. Runtime and failures

- **Final run** (`entry.py all`): 1,269 s, 1,066 s and 230 s for the three notebooks, all passing.
- **Failures:**
  - The Brain Image Library server timed out, so morph-reconstructions is blocked.
  - `glmnet_python` would not install (substitute used, item 8).

Nothing else failed.
