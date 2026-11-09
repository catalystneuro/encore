I answered all ten questions from the paper, and nine of them come out as "not given". The paper links no code, and the Methods and legends don't fix these details. For each open detail I named the readings the text allows in the claims file and set `answered: 2026-10-21`. I changed no statement or expected value. For the new readings (the noise and step ones in fig6 included), the criteria say the outcome must be the same under all of them, or the claim is `methods_underspecified`. `python tools/claims_check.py` reports 0 problems. Nothing is committed or pushed.

1. **Lick-early trials in the neural analyses:** Not given. The Methods exclude them from performance only. They are now readings K1 (dropped) and K2 (kept), as a new convention K, and the named claims need the same outcome under both.
2. **Window for the preferred trial type:** Not given. The readings are D1 (whole trial), D2 (delay epoch) and D3 (each bin).
3. **">3 trials in all conditions":** Not given, and no further selection behind 55, 143 or 40 is stated. Counting per condition (the legend's words) decides; per condition and trial type is a variant.
4. **Bin label and how far the recovery search runs:** Not given. The readings are centre or end of the bin, and a search to the end of the delay or into the response epoch. Extended Data Fig. 7d's "no recovery at end of delay period" fits the first for the bilateral judgement.
5. **Activity-space sessions and neurons:** The paper gives only the Methods' rule (>5 neurons for >5 trials per condition) and its outcome (6 to 20 neurons, mean 11, 16 sessions). The rule is followed as written, counting per trial type is a variant, and the counts are reported against the paper's.
6. **Extended Data Fig. 4 selection test and bin:** Neither is given. The readings are paired or unpaired, and 200 or 400 ms bins.
7. **Fisher table for Extended Data Fig. 6a:** Not given; the paper reports no test. The readings are trial type by correct on bilateral trials, and licked side by condition.
8. **Modes:**
   - (1) Yes, as far as the text goes: the Methods project "independent control trials and perturbation trials", so the ipsilateral trials are split like the control trials.
   - (2) Not given. The readings are the training trials and all correct control trials.
   - (3) Not given. The readings are orienting to a positive weight sum, and orienting so the control projection rises, judged by the size of the delay change.
9. **Detecting the first lick from `lick_trace`:** Not given; the Methods say only that a lickport recorded the licks. The outcome stands only if it is the same over a range of raw and baseline-SD thresholds.
10. **Model noise and integration step:** Not given. The noise readings are Euler-Maruyama white noise, or a variance-0.01 sample drawn each step; the step readings are 1 ms and 0.1 ms.
