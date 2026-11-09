No outcome changed. The verifier agreed with all 20 in round 2, so it stays at 12 reproduced, 1 not reproduced (`fig1s6b-gaze-classification`) and 7 blocked. I re-ran the entry with `python tools/entry.py all`: the check found 0 errors, the notebook passed in 89 s, and every number the conclusions cite matches the new output.

**Added in reply to the report:**
- **fig1s6b, run folds:** this result now has its own null. Location is classified at 11.3% with folds that never split a run, above all 200 shuffles of location within runs (highest 9.8%).
- **fig1s6b, position within the screen:** I ran both checks the verifier asked for.
  - The position within the screen can itself be decoded: 10.5%, above all 200 shuffles within screens (highest 9.5%).
  - After removing each position's mean activity, location is still classified at 11.1%. That is above the highest of the shuffles of the unadjusted data (10.0%). That is a comparison, not a null built for the adjusted data.
  - The conclusion now says the location signal is not explained by position within the screen. The outcome is unchanged.

**Corrected:**
- **fig3s1:** the Summary note now says f² is at most 0.017, not 0.012.
- **Start time:** the dataset checks, the Summary and the record's finding no longer say the start time marks the cue. They now say the finger-decoding curve is consistent with a start at the cue but cannot rule out a shift of a few hundred milliseconds.
- **fig3a:** the conclusion now adds that the outcome rests on specifications I chose, because the paper does not describe its own.
- **README:** "under two minutes" now reads "about 90 s", the time the run tool reported for two runs (91 s and 89 s).
- **Attempt record:** I restored the three items the verifier said were dropped from my round-1 record of its reasons: the finger half of the fig1s6b criterion, the fig2f paired p = 5.9e-5, and "at most a few units could change" for fig1s5. Round 2 is recorded for all 20 claims. The schema has no field for a round-level note, so I put the start-time point under `fig1s4a-offline-accuracy` and the runtime point under `recording-counts`. The record validates against the schema.

**Not done, and why:**
- **fig1b denominator:** the verifier says this cannot be fixed from the data. It stays a recorded deviation.
- **fig3a:** the authors' t(6) specification is still unknown, and their code for this test is not in their repository.
- **fig3s1:** I did not change which regression is the main one. The pre-registered one is kept, and the paper's significant session decrease still appears only with the session's noise covariance. This was already disclosed.

**Left for you:** the repo root has untracked files I did not create (`.bashrc`, `.profile`, `.gitconfig`, `.mcp.json`, `.idea`, `.vscode`, `scripts`, and others). Please check them before the workflow commits.
