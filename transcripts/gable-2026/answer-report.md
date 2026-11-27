There was one question, and the claims file changed to answer it.

**fig2f-sd-input-elevated, and the 29 other claims on the paper's own two-photon imaging.** The asker is right that these should be `data dataset`, and all 30 claims now say so.
- **What changed:** each claim's `data: elsewhere` is now `data: dataset`, and its `where` line is removed. The opening comment of the claims file now says these claims are blocked as `data_missing`. Statements, quotes, expected values and criteria are unchanged.
- **Why:** the only data source the paper names is "https://github.com/kerlin-lab/Gable_2026", and that repository holds code only, so the imaging data are not public anywhere. The protocol (Author, step 4) keeps `elsewhere` for data deposited in another public archive, and says "Data the paper names but that are not public anywhere stay `data: dataset`, blocked with `data_missing`."

The question has its `answer` and `answered: 2026-11-22`. `python tools/claims_check.py` reports 0 problems (34 claims, 33 quotes, 52 statistical values), and the questions file loads as valid YAML. Only `claims/gable-2026.yaml` and `questions/gable-2026.yaml` were modified, and nothing was committed or pushed.
