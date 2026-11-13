I answered both questions. One thing to know first: `questions/park-2019.yaml` was missing from this branch. The branch's single commit was made without it. `main` has it at https://github.com/catalystneuro/encore/blob/main/questions/park-2019.yaml with two unanswered questions from attempt park-2019-01. The claims file on this branch matches `main`'s exactly, so I copied the questions file from `main` and answered it. It now shows as untracked here.

1. **fig5-error-inhomogeneous: claims file changed.** The paper supports more than one reading of the error distribution, and the criterion only allowed one. The paragraph asks whether decoding is accurate "when the rat faces the directions at which the internal representation registers". It compares the error distribution with "the head-direction distribution" using Kuiper's test, and puts its minima "at 110 and 350 in the room frame". All of that points to a distribution over head direction. The criterion now accepts three readings:
   - mean absolute error in each 10-degree head-direction bin;
   - the head directions of windows decoded accurately (the paper gives no threshold, so 15, 30 and 45 degrees);
   - the signed error angles, as the original criterion had it.

   The claim counts as reproduced under any of these, combined with any of the existing ways of pooling recordings. Expected values and tolerances are unchanged.

2. **figs3-no-head-direction-bias: no change.** The finding is that the distribution "did not significantly differ from uniform", so it is judged on p ≥ 0.05. The paper's p > 0.17 is already recorded under `statistics`, and the number the attempt must match is r = 0.17 ± 0.02, which stays in `expected`.

Both questions have `answered: 2026-11-13`. Both files load as valid YAML. `python tools/claims_check.py` passes every quote and reports one problem: the value `1e-09` for fig1d-preference-change is not found. That was there before; the PDF text extraction lost the minus sign, and an earlier check of the claims file already confirmed the value. Nothing is committed.
