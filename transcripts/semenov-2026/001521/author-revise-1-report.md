I've worked through all of the verifier's round-1 points. One outcome changed. The entry re-runs cleanly with `tools/entry.py all` (0 errors, notebook 283 s), and every conclusion matches the new numbers. Nothing is committed.

**Outcome change**
- **fig6b-650-weak-but-significant:** now `not_reproduced` (was blocked as `methods_underspecified`), for the verifier's reason. Both tests in the statement are fully specified, and they fail under both conversions:
  - Under M1 the mean is -9.17%, significantly below zero, and not above the 230 V/cm group (p = 0.20).
  - Under M2 the mean is not different from zero (p = 0.27).
  - The printout now gives the direction of each effect, and there is a per-voltage table of n, mean, s.e. and p against zero and against 70 V.

The other 26 outcomes are unchanged, and the verifier agreed with all of them.

**What I added or corrected**
- **Sham drift (problem 1):** the drift is in the data, not in the processing.
  - In sham recordings the raw cell fluorescence, before any background subtraction, falls 8.7% (single pulses) and 7.5% (trains). The cell-free background falls only 1.0% and 0.6%.
  - So no choice of background region removes it. This is compared in the notebook with the Fig. 6A sham, which rises about 1%, and is asked of the authors.
- **New confound:** the decline slows with each recording of a field of view (-3.97 %/min in the first recording, -0.41 to -1.46 %/min in the fifth to seventh). Because fields of view were recorded at escalating voltages, voltage and recording order go together, and the sham is always first. This is a new finding in the record.
- **Step at the pulse:** I added this as a variant, since drift and order do not affect it.
  - Under M1 it detects 1000 V/cm (p = 0.025) and 1200 V/cm (p = 3e-7), but not 780 V/cm (p = 0.10). Under M2 it does detect 780 V/cm (p = 0.025).
  - The 1000 V/cm entry is therefore small, and the notes now say so.
- **780 V/cm test (problem 2):** the outcome stays `reproduced`, because the claims file's test decides it. I added a question to `questions/001521.yaml` saying that test cannot detect an increase here, since it also finds none at 1000 and 1200 V/cm. The claim itself is unchanged.
- **Field conversion (problem 3):** M1 (3.9 V/cm per V) is now the main reading, recorded as an assumption, because it fits the Fig. 6B labels and group sizes. M2 is still shown for every claim, and no outcome depends on the choice. The notebook shows that neither the 1.00 mm nor the 1.6 mm electrode gap gives either factor directly.
- **Fig. 6B comparison and counts (problem 4):**
  - The higher fields are now only the 900 and 1000 V/cm of Fig. 6B.
  - The total counts only the six groups that match the figure: 256 under M1, so `measured` changed from 311 to 256. The six M2 groups happen to sum to exactly 224.
- **Rule (b) (problem 5):** the literal reading ("above 3 s.d.") is added, making 36 combinations. None meets the fig6b-train-threshold criterion.
- **Other outputs the verifier asked for:**
  - region overlays for every field of view (segmentation looks clean);
  - results with fields of view as the unit;
  - which fields of view could make up Fig. 6A's 14 cells (three different sets of fields of view each sum to 14, so the cells cannot be identified).
- **Text fixes:** the docstring file counts are corrected to 31 and 42, and the README, summary, findings and the round-1 `verifications` block are updated.

**Not done**
- I did not check whether dandisets 001515 to 001526 hold the potentiometric data; they are separate targets.
- Which 14 cells Fig. 6A averages still cannot be told from the data.
