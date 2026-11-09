I've finished steps 1 to 6 for DANDI:000575 (version 0.231010.1811): entry, attempt record and handover package are written. The entry check reports 0 errors and the notebook passed `tools/entry.py all` in a clean environment (1074 s). Nothing is committed.

The main result: in the files, the spikes and the trial labels look misaligned by a few trials. All claims that compare trials by their labels (workload, set size, correct against incorrect) fail. The behavior and the period-only claims hold.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| behavior-accuracy-by-set-size | reproduced (F = 89.78 against 89.79) |
| behavior-capacity | reproduced |
| table1-capacity-and-neurons | reproduced (all 26 values match exactly) |
| behavior-rt-set-size | partially reproduced (F = 48.47 matches; slope 69 to 76 against 118 ms/item) |
| neurons-recorded | partially reproduced (809 total matches; per-region counts don't) |
| spike-sorting-quality | not reproduced (ISI SD 1.77 against 1.54; SNR 5.9 against 3.8) |
| firing-rates-by-period | reproduced |
| fig2c-maintenance-neurons | partially reproduced (significant in all three regions; counts out of tolerance) |
| fig2d-workload-modulated-maintenance-neurons | not reproduced |
| maintenance-neurons-correct-vs-incorrect | not reproduced |
| fig3b-test-neurons | partially reproduced |
| fig4a-dpca-separates-set-sizes | not reproduced (81.4% and 32.9% match, but set sizes not separated beyond shuffled labels, p = 0.35) |
| fig4b-speed-lowest-in-maintenance | reproduced |
| fig4c-distance-largest-in-maintenance | partially reproduced |
| fig4d-decode-workload-all | not reproduced (about 45% accuracy) |
| fig4d-decode-workload-regions | not reproduced |
| decode-performance-not-significant | reproduced |

**2. What was found about the dataset**
- **Misalignment:** workload information in the spikes peaks when the spikes of trial window i are paired with the label of trial i + 3. Decoding workload gives 0.46 as deposited and 0.60 with every session shifted by 3. The offset per session could not be established, so outcomes are on the data as deposited, with the shifted version shown only as a variant.
- **Duplicates:** participant 12's two sessions are each deposited twice (4 files, same start time). Each is counted once.
- **Unit locations are wrong:** each unit's `location` is the atlas label of the macro contact with the same number as its microwire. The paper's assignment of units to regions is not in the files. Five units sit on bundles (PCL, HL, HR) that the subject descriptions don't list.
- **Response timestamps are shifted:** read as press times, 1385 of 3038 responses come before the test array. RT is computed as stored value minus 1.7 s, from the dandiset's conversion code (the only outside input). Slopes and F values don't depend on this.
- **Trials:** sessions hold 174 to 192 trials against the stated 192, undocumented. Spikes are stored only inside trial windows.
- **Paper inconsistency:** the text puts the RT ANOVA on mean RT, but F = 48.47 comes from median RT.
- **Assumptions:** none of the outcomes rests on one, so there are no questions for the paper's authors.
- **Question for a reader** (`questions/000575.yaml`): whether regions come from the electrode name, as the claims file says, or from the tip location in the Figure 1d legend. By tip location the amygdala count is exactly 146, and two of the three fig2c counts fall within tolerance.

**3. Where the protocol was unclear**
1. It says to check the clock but not what to do when trial labels turn out misaligned. I tested as deposited and showed the k = 3 shift as a variant, not deciding any outcome.
2. The claims file defines regions only in the neurons-recorded criterion. I applied that rule to every per-region claim, showed the tip-location reading as a variant, and asked the reader.
3. There is no rule for cutting permutation or resampling counts below the paper's to fit the time limit. I recorded each cut as a deviation (99 or 200 null runs where the paper used 499 or 1000).
4. Some criteria define no partial condition even when the effect is present (fig2c, neurons-recorded). I used the general outcome definitions and marked them partially reproduced.
5. The `measured` rule covers only the case where several readings match. When none matches fully (RT), I recorded the reading that matches most.
6. A reading the data cannot support (ISI over the whole recording, the sorter's noise level) has no guidance. I tested the readings that could be run and said why the others could not.
7. It isn't clear whether code used only to interpret metadata (the conversion's 1.7 s offset) belongs under `inputs`. I listed it.

**4. Runtime and failures**
The run took about 1 h 25 min (19:31 to about 20:55 UTC); the notebook takes 18 minutes. Nothing failed. My attempt to delete an empty `.claude` folder and a `__pycache__` in the entry directory was denied for lack of approval. Neither will be committed: git skips empty folders, and `__pycache__` is gitignored.

Files are in `entries/000575-boran-2022/`:
- reproduce_boran_2022.ipynb
- mtl_wm.py
- entry.yaml
- requirements.in
- requirements.lock.txt
- README.md

Also written:
- `attempts/000575-boran-2022-01.yaml`
- `questions/000575.yaml`
- the handover package in `executed/000575-boran-2022/handover/`
