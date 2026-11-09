**Verifier report, round 3: Bruno, Frost & Humphries 2017 (eLife 27342) on CRCNS apl-1**

The attempt record proposes one change of outcome, for fig6d-decode-p10. It is the only `proposed` entry in the record.

| claim | proposed outcome | agree | my outcome if different | reason |
|---|---|---|---|---|
| fig6d-decode-p10 | not_reproduced (recorded: partially_reproduced) | yes | — | **The test:** mean forecast R − 2 s.e.m. must be above 0 "in each of the nine responses", and the criterion has no partial rule. Cell 79 shows that test failing. Under every reading of width and count, only 8 of 9 responses pass. Preparation 4, bout 1 fails under all four: mean R is −0.060 (own/min80), −0.127 (own/le80), −0.060 (pooled/min80) and −0.119 (pooled/le80), with bounds −0.128 to −0.206. It also fails with histories up to 100 ms, and with the code's windowing (mean R −0.101, bound −0.130). **Applied as written:** the analysis follows the criterion. The windowing is fit 40 s, forecast 10 s, step 1 s from 33 s, and histories run from 50 to 200 ms. Each program keeps its history by mean forecast MAE (`apl.decode_program`), the code's reading of the Methods. **The fixed choices hold the result up:** the result does not rest on a choice made to reach it, because the failure holds under every reading, history range and windowing that was run. **Not a fluke of rounding:** cell 81 shows that perturbing the PCs leaves the mean R of this response unchanged (−0.1006 against −0.0991). |

**Numbers in the proposal that this notebook does not print.** None of them changes the outcome, but the reason and notes do not derive from the outputs I was given:

- **Record reason, notes and cell 82, per-reading mean R:** given as "−0.060, −0.119, −0.075 and −0.124; bounds −0.127 to −0.204". Cell 79 prints −0.060, −0.127, −0.060 and −0.119, with bounds −0.128 to −0.206.
- **Code-windowing mean R:** given as −0.102. Cell 79 prints −0.101, and cell 81 prints −0.1006.
- **Diverging forecasts (record notes, cell 82):** given as "195 to 277 of 5760" windows over all histories and "770 of 7830" for the code's windowing, with "none in any 80% run" for the selected histories. Cell 81 prints:
  - 796 to 1107 of 5760 over all histories, and 2230 of 7830 for the code's windowing.
  - One diverging selected window each in three 80% runs: own/min80 with the code's windowing (largest forecast 1.3e9), pooled/min80 (8.4e9) and pooled/le80 (1.1e5).
- **Perturbation test (cell 82, record notes):** given as mean MAE 13.28 against 13.26 at 50 ms, and 5.3e11 against 2.8e11 at 150 ms (67 and 65 diverging windows). Cell 81 prints:
  - 7.56e6 against 9.96e5 at 50 ms.
  - 1.05e12 against 1.27e12 at 150 ms, with 116 and 136 diverging windows.
- **Cell 82, mean MAE of 7.6e6:** cell 82 says this value came only from the round-2 copy and was "not run here". This notebook prints the same 7.6e6 (cells 79 and 81).
- **Response 2 of preparation 4 (cell 82, record notes):** its forecast R is given as "0.82 to 0.93". Cell 80 prints 0.810 to 0.938.

So the prose of cell 82 and the record's fig6d reason and notes seem to describe a different execution from this notebook's outputs. Any statement about the diverging forecasts or about rounding should be redone from the printed outputs. The claims file does not misread the paper here: the criterion's "in each of the nine responses" matches the quote, "in all nine population responses".
