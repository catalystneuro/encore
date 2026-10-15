The attempt on dandiset 000004 is done through step 6: the entry is locked, `check` and `all` pass, and the handover package is built in `executed/000004-chandravadia-2020/handover/` with the conclusions removed. Nothing is committed.

I used the paper's full text, which is open access (CC BY 4.0), including Tables 1 and 2 and Online-only Table 1; it is saved under `paper/`. The pinned version is 0.220126.1852. The paper cites no DANDI version, and the two published versions hold the same 87 assets, so I took the newer one; the notebook header says this.

**1. Outcome per claim** (counts from the attempt record: 10 reproduced, 8 partially, 4 not reproduced, 2 blocked)

| Claim | Outcome |
|---|---|
| counts-neurons-subjects (1864 units vs 1863; 59 subjects) | reproduced |
| counts-sessions (87, matching Online-only Table 1) | reproduced |
| table1-demographics (56 of 59 subjects match) | partially |
| task-structure (8 sessions have fewer than 100 encoding trials) | partially |
| new-old-label-coding (the data use 1 = old) | not reproduced |
| ttl-codes (78 of 87 files) | partially |
| experiment-ids (83 of 87 files) | partially |
| session-dates (86 of 87 files) | partially |
| units-table (NaN or infinite quality metrics) | partially |
| electrodes-table (impedance empty for all 887 electrodes) | not reproduced |
| isi-criterion (99.7% of units pass) | partially |
| fig5a-mtl-locations | reproduced |
| fig5c-auc-all (0.753 ± 0.094) | reproduced |
| fig5c-auc-sites | reproduced |
| fig5b-roc-asymmetric | reproduced |
| fig5d-confidence-accuracy | reproduced |
| vs-cells-proportion (332, 17.8%) | reproduced |
| ms-cells-proportion (110, 5.9% vs 146, 7.8%) | not reproduced |
| dual-cells-proportion (12 vs 26) | not reproduced |
| fig5f-site-proportions | partially |
| twh-sessions (9) | reproduced |
| fig4-example-vs-neuron | reproduced |
| previous-release-additions | blocked (other) |
| fig3-example-vs-neuron | blocked (data_missing: session 144 is absent) |

The memory-selective and dual counts follow the Methods (all 50 new and 50 old trials, 200 to 1200 ms window). The paper's code uses correct trials only and a 200 to 1700 ms window; with those choices I get 343 VS, 147 MS and 26 dual cells, and the Figure 5f values to within 0.1 point.

**2. What was found about the dandiset**
- **Label coding:** `new_old_labels_recog` uses 1 = old, the reverse of the paper's text and of the files' own column description. Anyone following the description gets an AUC of 0.25.
- **Duplicated spike trains:** sessions 43/44 and 54/55 hold identical spike trains, so 55 units are counted twice. Session 55 also repeats session 54's learning block.
- **Missing encoding trials:** 7 sessions have 50 encoding trials and one has 97. Part of the images later shown as old are not in the stored encoding block.
- **Empty or broken metadata:** impedance is empty everywhere; coordinates are missing for 99 electrodes; IsolationDist is NaN for 493 units and SNR is not finite for 86.
- **Spike times:** 13 units have unsorted spike times, and two units in session 58 store every spike twice.
- **Subjects and dates:** age or sex differ from Online-only Table 1 for 3 subjects (H48 is a 32-year-old woman in the files, a 54-year-old man in the table). Session 48 keeps its real day (2010-03-13), and session 68 is dated 2000-01-01.
- **Codes:** event codes outside Table 1 appear in 9 files, and experiment ids outside Table 2 in 4.
- **Inconsistencies in the paper and its code:** the Methods say 89 sessions where the table and the files have 87. The code's `plotFigure5.ipynb` writes the Figure 5f percentages into the plot as constants and does not compute them.

**3. Where the protocol was unclear, wrong or missing something**
1. **Methods vs code:** here the code reproduces the paper's numbers exactly and the Methods do not. The protocol makes the Methods decide the outcome, so MS and dual cells are "not reproduced". I followed that rule and recorded a `code_mismatch` finding.
2. **Stated spread as tolerance:** "use the stated spread" makes the tolerance of a mean ± SD equal to the SD (0.74 ± 0.10), which is very loose. I also held the SD itself to 10%.
3. **Default 10% on record counts:** for the counts in a data descriptor (neurons, subjects, sessions), 10% is loose. I kept it and recorded the exact differences.
4. **Data descriptors:** the protocol assumes papers with findings. I made each described data element a claim.
5. **"Count each recording once":** this is unclear when two sessions share spike trains but have different trial data. I kept the paper's per-file count as the main reading and counted the units once as a second reading.
6. **Unreachable public input:** the earlier release on Dryad is public but refuses automated download (HTTP 403, or a token is required). No blocking reason fits, so I used `other`.
7. **Per-session clock check:** with 1 to 64 units per session, 49 of 87 sessions cannot show the shared clock. I listed them, as the protocol asks.
8. **Criteria written after the data check:** for descriptor claims, the data check is the test itself. I wrote the criteria after it, and the claims file's opening comment says what I had already seen.
9. **Thresholds for partial outcomes:** the protocol gives no default for "partially reproduced" in count-based criteria. My criteria said "most files" without a number; I took 78 of 87 as most and recorded that as a deviation.
10. **Reference tables:** whether a paper table or constants in the paper's code count as "inputs" or as "embedded numbers" is not stated. I copied Online-only Table 1 into the helper module as text and listed it, and the code's Figure 5f constants, under `inputs`.
11. **Chance level:** the paper states none for its cell selections. I still report a label-shuffle null (4.5% VS, 5.3% MS); the MS rate under the Methods' test (5.9%) is barely above it.

**4. Runtime and failures**
- The notebook runs in about 125 s, of which 81 to 96 s is streaming the 87 files with 8 threads.
- The only thing that failed was the Dryad download, which blocked one claim. No notebook errors.
- The untracked `.bashrc`, `.profile` and similar entries in `git status`, and `scripts`, are links to /dev/null created by the sandbox, not by me. They may show up when the workflow commits.
