I've worked through every point in the round-2 report. The entry re-ran cleanly with `python tools/entry.py all entries/gao-2018` (0 errors, notebook ran in 7.3 min), every number is the same as before, and the conclusions match them. Nothing is committed.

**Outcomes:** none changed and none proposed. The verifier agreed with 44 of 45 outcomes.
- **`cd-captures-selectivity`:** the attempt record still said `reproduced`, though the round-1 revision had changed it to `partially_reproduced` and the notebook, summary and README already said so. I set the record to `partially_reproduced`, which is the outcome the verifier gives. This fixes the record and is not an outcome change.
- **Totals in the record now:** 10 reproduced, 6 partially reproduced, 3 not reproduced, 26 blocked, which match the notebook and README.

**Corrections:**
- **`fig3e-alm-mean-rate-unchanged`:** it is now marked `assumed: true`. A new deviation says the absence test is the unpaired t-test, because the paired and unpaired tests disagree (p = 0.214 against 0.022) and the paper's p = 0.58 fits an unpaired test. The summary table marks it. The text now says the control rate is 19% below the paper and the photo-inhibition rate 14% below, where it had said 19% for both.
- **`fig2cd`:** the notebook cells, notes and the related finding now quote the paper's actual words, "qualitatively similar preparatory activity", and say that the preparatory part is similar under every epoch here. They no longer claim a conflict with the paper about where the peak lies.
- **`fig4g`:** the text now adds that the within-trial-type variant stays above the 1% chance level in all 15 bins.
- **`fig4e`:** the text now sets the trial-count control (65–75% would lose significance anyway) against the observed 86–88%. It also says the outcome rests mainly on the population difference and its interval.
- **`fig3d`:** the notes now say the latency fails only when the five clock-check sessions are included, and that the count depends on the unexplained unit selection.
- **`fig1g-dentate`:** the notes now carry the verifier's remark that the bootstrap is conservative, which favours a claim of absence.
- **Findings:** the `photo_stim_id` finding now gives the printed numbers (code 6 is 2.95 to 3.00 early in the delay and 2.93 at its end). The recording-end figures are corrected to 7221.8 s and 7223.1 to 8481.4 s.

**Outputs added:**
- The data check (cell 5) now prints the stated sampling rate per probe type: all 34 sessions recorded with the 32-channel probe say 20 kHz, though the Methods say 25 kHz. To get this, the helper now reads each file's `probe_type`.
- Cell 6 now prints where the BAYLORCD8 20171020 recording ends, the 127 of 462 trials after that, and that no spikes fall after it.

**Recorded:**
- **Reader question:** the new `questions/gao-2018.yaml` asks whether the claims file's E3 paraphrase drops "preparatory activity". The claim itself is unchanged.
- **Round 2:** it is in the attempt record under `verifications`, with all 45 claims. Each has the verifier's reason in its words and my response.

**Not done:** B1, the excess unit count, cannot be resolved because the units table has no quality field. The photostimulus onset cannot be checked because the files hold no laser trace. The verifier listed B8 (the conservative bootstrap) and B11 (recording sessions in place of the paper's behaviour sessions) as not affecting any outcome. I left B8's bootstrap as it is, since it is the paper's method, and B11 was already stated.
