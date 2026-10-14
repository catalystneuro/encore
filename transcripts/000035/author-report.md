I did steps 1 to 5 of the protocol and built the handover package; I did not verify my own work. `entry.py check` reports 0 errors, the notebook runs from a clean environment in about 3 minutes, and the handover is in `executed/000035-scala-2021/handover/`. Nothing is committed. The paper's full text is open access (Europe PMC, PMC8113357, CC BY), so the full text was used; it is saved under `paper/`. The pinned version is 0.211014.0808, the only published one. The paper cites no version, and the draft has the same 185 files.

**1. Outcome per claim**

| Claim | Data | Outcome |
|---|---|---|
| fig1-ttype-coverage, fig2-rrr-prediction, ed5-rrr-ion-channels, fig3d-families-separate, fig3d-morphology-combined, fig4c-distance-correlation, fig4d-it-depth, fig5a-ttypes-between-families, fig5b-ttype-variability | main data set | blocked, `data_missing` (it is in dandiset 000008, NeMO/GEO and the Brain Image Library) |
| ed6-cohort | dandiset | reproduced (all counts exact; features defined for 185 cells against the paper's 184) |
| ed6-stimulus-protocol | dandiset | partially reproduced (174 of 185 cells follow the stated current ladder) |
| ed6-it-et-overlap | dandiset | reproduced (58.3% of ET cells classified as IT, no IT cell as ET; a balanced logistic regression still separates them, accuracy 0.83 against 0.50) |
| ed6-it-et-ap-threshold | dandiset | reproduced (p = 0.00035, second of the 17 features) |
| link-cells | with the paper's tables | partially reproduced (t-type names agree for 93.5%, below the 95% criterion; see point 1 below) |
| link-features | with the paper's tables | reproduced (16 of 17 features correlate at 0.9 or more with the published values, lowest 0.877) |
| ed6-sst-temperature | with the paper's tables | reproduced |
| ed6-sst-transcriptomic-distance | with reference data | blocked, `not_runnable` |

**2. What was found about the dandiset**
- It holds only the paper's 185-cell follow-up at 34 °C, but its description repeats the main data set's "over 1300 neurons".
- Voltage is stored in mV and current in pA, while the files say volts and amperes.
- Every series has a NaN starting time, so the timing between sweeps is lost. Within a sweep, stimulus and response share a clock.
- The 12 ET cells carry the older names L5 PT_1 to PT_4. The paper and its tables call them L5 ET_1 to ET_4.
- Eleven cells were stimulated beyond the 1,380 pA in the Methods, nine of them from one mouse.
- The published version's metadata has a placeholder contributor "Last, First" carrying another author's ORCID, the brain region typed as a disorder, and no technique listed. The unpublished draft fixes these.
- Everything else checked matches the paper: counts, layers, soma depths and the published per-cell features. No duplicate recordings were found.
- The paper itself has two inconsistencies: the representation is called 17-dimensional in one place and 16-dimensional in another, and the Extended Data Fig. 6j legend points to the wrong panel. The Methods and the code define the maximum number of APs differently (3 cells differ).

**3. Where the protocol was unclear or did not fit**
1. A criterion did not anticipate renamed labels. The t-types are identical but named PT in the files and ET in the paper's table. I applied the criterion to the names as written (partially reproduced) and said in the notes that the cells themselves match.
2. There is no category for an outside input that is public but too slow to fetch. The Zenodo reference data downloaded at 72 to 165 KB/s, so the 88 MB file needed would take 9 to 20 minutes. I used `not_runnable` and recorded what I tried.
3. The protocol does not say whether a link claim is needed when outside data is matched by label, not by cell (the room-temperature Sst cells). I added two link claims: one matching cells and labels, one checking my features against the published values.
4. Nothing covers re-implementing a method whose published code cannot be redistributed (Allen Institute license). I re-implemented the feature extraction and used link-features to test it.
5. The protocol does not say what a link claim should get when it is partially reproduced. I ran the dependent claims and said so in their notes.
6. The paper gives no classifier result at 34 °C. I applied its Fig. 3d classifier and recorded that as a deviation.
7. The entry name could use 2020 (online) or 2021 (print). I used 2021.

**4. Runtime and failures**
- The session took about 45 minutes; the notebook runs in about 175 s.
- Nothing failed.
- Untracked dotfiles and a `scripts` device node in the repo root existed from the start of the run. I did not create them, but the workflow could commit them.

The main new files are `claims/000035/10.1038-s41586-020-2907-3.yaml`, `attempts/000035-scala-2021-01.yaml` and the entry in `entries/000035-scala-2021/`.
