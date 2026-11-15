## Report: chandravadia-2020, repeat attempt 02 (blind)

The entry is at `entries/chandravadia-2020/` and the record at `attempts/chandravadia-2020-02.yaml`. `tools/entry.py all` reports 0 errors, and the notebook passes a clean run in 160 s. The verifier's package is built in `executed/chandravadia-2020/handover/`. I did not commit anything.

### 1. Outcomes

| Claim | Outcome | Key numbers |
|---|---|---|
| counts-neurons-subjects | reproduced | 1864 unit rows (1798 with duplicated spike trains counted once), 59 subjects |
| counts-sessions | reproduced | the 87 (subject, session) pairs equal Online-only Table 1 |
| table1-demographics | partially reproduced | 56 of 59 subjects match; C24, H33 and H48 differ |
| task-structure | partially reproduced | 7 sessions have 50 encoding trials, 1 has 97 |
| new-old-label-coding | not reproduced | labels are reversed: 1 = old (86 of 87 sessions on both tests) |
| ttl-codes | partially reproduced | 78 of 87 files; 9 hold codes Table 1 does not list |
| experiment-ids | partially reproduced | 83 of 87; 4 files use id 82 |
| session-dates | partially reproduced | one date on 2010-03-13, one session dated 2000-01-01 |
| units-table | partially reproduced | SNR not finite for 86 units, isolation distance missing for 493 |
| electrodes-table | not reproduced | impedance empty for all 887 electrodes |
| isi-criterion | partially reproduced | 1858 of 1864 units below 3% |
| fig5a-mtl-locations | reproduced | every unit in amygdala or hippocampus |
| fig5c-auc-all | reproduced | 0.753 ± 0.094 |
| fig5c-auc-sites | reproduced | CS 0.760 ± 0.085, TWH 0.688 ± 0.138 |
| fig5b-roc-asymmetric | reproduced | mean z-ROC slope 0.78, p = 4.3e-9 |
| fig5d-confidence-accuracy | reproduced | paired p = 3.2e-16 (fixed split), 1.3e-11 (dynamic split) |
| vs-cells-proportion | reproduced | 332 (17.8%) |
| ms-cells-proportion | not reproduced | 118 (6.3%); the code's choices give 146 (7.8%) |
| dual-cells-proportion | not reproduced | 13 (0.7%); the code's choices give 25 |
| fig5f-site-proportions | partially reproduced | no site difference, but only 3 of 6 values within tolerance |
| twh-sessions | reproduced | 9 sessions |
| previous-release-link | partially reproduced | 64 of 65 sessions of the 2018 release found (session 98 missing) |
| previous-release-additions | partially reproduced | 23 sessions and 17 subjects match, but 325 units against 288 |
| fig4-example-vs-neuron | reproduced | ANOVA p = 1.2e-22, animals highest |
| fig3-example-vs-neuron | blocked (`other`) | no session 144 exists |

Totals: 10 reproduced, 10 partially reproduced, 4 not reproduced, 1 blocked.

### 2. What was found

**About the dataset:**
- The `new_old_labels_recog` coding is the reverse of what the file description and the paper's text say.
- Eight sessions are missing encoding trials. In the seven with 50 trials, 21 to 24 of the "old" images were never shown in that file's encoding block.
- 66 spike trains are deposited in two files each (session pairs 38/39, 43/44 and 54/55). Sessions 54 and 55 also share their encoding block.
- 13 units store spike times out of order, and two of them hold every spike twice.
- Smaller problems:
  - Electrode impedance is empty everywhere, and coordinates are missing for 99 electrodes.
  - SNR is NaN or infinite, and isolation distance missing or around 1e27, for many units.
  - Three subjects' age or sex differ from the paper's table.
  - Some event codes and experiment ids are undocumented.
  - One date is wrong and one year looks like a placeholder.
  - 38 files use Unix-time clocks, and the institution name is misspelled two ways.

**About the paper:**
- The Methods' window and trial choice for selecting cells differ from the published code. The code's choices (0.2 to 1.7 s, correct trials only for MS) reproduce the paper's 343, 146 and 26 (25 here).
- The Methods say 89 sessions; the paper's own table and the files have 87.

**Assumptions:** none affect an outcome. I left out five sessions where the z-ROC slope is undefined; this is recorded as a deviation.

**Question for the paper's authors:** is the Figure 3 neuron 144-140-3-RH the third unit of session 2009 (T103)? That is the only channel-140 unit set in the dataset, and that unit is strongly phone-selective (p = 1.3e-9).

**Questions to a reader:** none.

**Possible exposure to earlier work:** the claims file's opening comment describes the earlier author's data check (duplicated spike trains in sessions 43/44 and 54/55, label 1 drawing most "old" responses) and how the link claim was added. That is the only earlier-attempt material I saw. I found the same things independently.

### 3. Where the protocol was unclear or did not fit
1. None of the blocking reasons fits a paper identifier that names no session in the dataset. I used `other` and explained it in the notes.
2. There is no finding kind for a question to the authors that is not about a method. For the Figure 3 question I used `paper_inconsistency`.
3. For a criterion that sets a threshold on a share of units (isi-criterion), it is unclear what `measured` should hold. I recorded the percentage of units below 3% and noted that as a deviation.
4. The claims file's opening comment can carry an earlier author's observations, which works against a blind repeat. I am only reporting this.
5. It is unclear whether the paper's own table, read at run time from Europe PMC, counts as an input. I listed it under `inputs` alongside Faraut et al. 2018 and the paper's code.

### 4. Runtime and failures
- The notebook runs in about 2.7 minutes (2 of them streaming), using 0.8 GB of memory.
- The session ran from 12:41 to about 13:11 UTC.
- Nothing failed.
