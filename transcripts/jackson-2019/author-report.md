All 25 claims were tested and none is blocked. The entry passes `tools/entry.py all` with 0 errors, and the notebook runs in 100 s. The handover package is built in `executed/openneuro-ds002778-jackson-2019/handover/`. Nothing was committed.

**1. Outcome per claim**

| Claim | Outcome |
|---|---|
| fig2-sharpness-off-on | partially reproduced: W 13 matches; d 0.73 is below 0.86 ± 0.086 |
| fig2-steepness-off-on | partially reproduced: d 0.70 matches; W 16 is outside 9 ± 0.9 |
| fig2-pac-off-on | partially reproduced: d 0.85 matches; W 13 (Methods' filters) or 12 (code's) is outside 15 ± 1.5 |
| bipolar-off-on | reproduced |
| temporalis-f7f8-null, temporalis-t7t8-null | reproduced |
| fig2c-topography-sensorimotor | partially reproduced: steepness meets the criterion, PAC only under one reading, sharpness not (smallest p at P8) |
| offctrl-sharpness-null, offctrl-pac-null | reproduced |
| offctrl-steepness | partially reproduced: z and d match, but FDR-corrected p is 0.053 |
| offctrl-pac-csd | not reproduced: p 0.075 against the paper's 0.022 |
| updrs-improvement | reproduced: W 3.5, p 0.0033, the paper's values exactly |
| fig1c-beta-alpha-peaks | not reproduced: only the controls' average spectrum has both peaks |
| table1-alpha-shape-off-on | partially reproduced: both tests hold; steepness W 21 is outside 12 ± 1.2 |
| table1-alpha-pac-null | reproduced, resting on an assumption (`assumed: true`) |
| table2-alpha-offctrl | partially reproduced: steepness z and d match, but FDR-corrected p is 0.053 |
| pac-beta-larger-than-alpha | partially reproduced: p 0.015; W 17 is outside 11 ± 1.1 |
| fig3-sharpness-pac-correlation, fig3-steepness-pac-correlation | partially reproduced: one r out of tolerance in each |
| fig4a-sensorimotor-q4, controls-q4, fig4b-temporalis-variable-shape | reproduced |
| q4-patient-counts | not reproduced: 13 patients qualify against the paper's 9 |
| table3-q4-effect-size | partially reproduced: d rises for all three measures; steepness and PAC values are above tolerance |

**2. The dataset**
- It holds what the paper describes: 15 patients off and on medication (8 female, mean age 63.3) and 16 controls (9 female, 63.5). There are 46 BDF files at 512 Hz, with no duplicates.
- The paper's manual artifact marks and its list of excluded electrodes are not in the dataset. No samples were rejected and all 32 scalp electrodes were kept (reading (b) of the claims file). Recorded as `data_missing`.
- The `on` session of sub-pd16 was exported from preprocessed EEGLAB files. After preprocessing it has about 6 times the amplitude of any other recording and no alpha peak, and the dataset does not say how it was processed. The `on` session of sub-pd6 came from the same kind of export; it is already average-referenced and lasts 289 s. Results without these two patients are shown as variants.
- The UPDRS fields and the event trigger have no description. Recorded as `metadata_insufficient`.
- Version: 1.0.5 is the latest snapshot. The paper cites none, and the change log shows no change to the EEG files across snapshots.
- **Assumption and question for the authors:** for alpha PAC the paper gives no phase filter length. I adopted 192 taps (three cycles of 8 Hz), which is the default of pacpy, the package the Methods name, and the rule the paper's code uses for its shape filters. With 192 or 231 taps alpha PAC is not significant (corrected p 0.061 and 0.078); with 118 it is (0.036). This question is recorded as a `methods_unavailable` finding.
- Also recorded as a `paper_inconsistency`: Table 2 prints corrected p = 1 where Benjamini-Hochberg gives about 0.36, and Table 3's all-patient PAC d (0.75) differs from Table 1's (0.83).
- I asked a reader no questions.

**3. Where the protocol was unclear**
1. When a result falls in a case the criterion does not name, the protocol gives no rule. This happened for offctrl-steepness and table2-alpha-offctrl: z and d match but the corrected p is 0.053. I recorded both as partially reproduced and gave the reason as a deviation.
2. When a criterion's last sentence names fewer values than its expected list, it is unclear which governs. For fig2-pac-off-on, the last sentence names only the test and d, while the claim also lists an expected statistic. I kept the statistic in the judgement and noted that the sentence alone would give "reproduced".
3. For continuous rest data the clock check does not apply, since there is no trial table. I checked instead that the Status channel and events.tsv agree on every trigger sample, and said so.
4. The protocol does not say what to do when a reading the claims file names has no data. Reading (a), the dataset's own artifact and bad-channel marks, is empty here; I recorded that reading (b) was the only one that could run.
5. Step 1.6 does not say how to choose among readings when two of three agree. I followed it as written, adopting the best-supported reading as an assumption, and noted that two of the three readings agree.

**4. Runtime and failures**
The run took about 26 minutes (22:23 to 22:49 UTC). The only failure was a YAML colon-space in the attempt record, which I fixed. `git status` also shows untracked dotfiles at the repository root (`.bashrc` and others); these are sandbox device mounts, not files I created.
