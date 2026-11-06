# Round 3 verifier report: proposed outcome changes

I counted from the files themselves. The claims file has 56 claims and the attempt record has 56 outcome entries. One outcome carries a `proposed` change: voltage-to-spike-sigmoid. Line 433 of the attempt record is the only `proposed:` field in the file.

| Claim id | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| voltage-to-spike-sigmoid | blocked (methods_underspecified) | Yes | — | The criterion names two readings: V at the spike frame, and V in the 10 ms before ("both shown"). They give different outcomes in SP cell 28. At the spike frame, 262 of 505 cells (52%) have R² ≥ 0.9, so it passes. Taking the mean of the 8 frames before gives 214 (42%), and the single sample 8 frames before gives 121 (24%); both fail. Lines 80–81 of the claims file's header say such a claim is blocked as methods_underspecified. |

## Check of the analysis behind it (SP cells 3, 27–29; `l1opto.p_spk_given_v`)

- **The numbers come from the data.** SP cell 3 builds P(spk|V) for each QC cell with `L.p_spk_given_v`, for each reading in turn:
  - It uses the code's quiet analysis frames (`analysisEF`: quiet, no running, ±1000-frame chunk guard).
  - The bins are 0.04 SH from −2 to 2.
  - Rate is the spike-V histogram divided by the all-V histogram, divided by 1.27 ms.
  - In the 10 ms window reading, every frame's V is the mean of the 8 frames before it, for spike frames and all frames alike. That is a fair version of the Results' and legend's wording.

  SP cell 28 fits the four-parameter logistic over bins with at least 100 frames, and prints the 52%, 42% and 24% quoted in the record. The per-mouse counts it prints (133 of 247 and 129 of 258) add up to 262 of 505.
- **The thresholds were not chosen to reach the result.** The pass mark (more than half of cells, R² ≥ 0.9, CV above 0.2) is fixed by the claims file. Splitting the 10 ms reading into two versions does not change the conclusion, because both versions fail while the spike-frame reading passes.
- **The criterion is applied as written.** Picking the spike-frame reading, as the current outcome does, rests on the Methods' V(t_s) and on the code. That corrects the claims file rather than applying it. Under the header rule as written, the outcome is blocked.

## Things to report, not correct

- **The claims file misreads the paper.** Its criterion says "The Methods/caption say V in the 10 ms before spikes". The Methods (paper line 539) give V(t_s), "the subthreshold voltage at spike times". Only the Results (line 209) and the Fig. 4E legend say 10 ms. If a reader corrects this, the spike-frame reading would be the paper's method and the claim could be judged on it alone. The record says this question is already put to a reader in questions/001960.yaml.
- **The CV figure is still inconsistent, now the other way round.** In the re-executed SP cell 28, the CV of the fitted maxima at the spike frame prints as **4.56**. SP cell 29 and the attempt record's notes now say **4.54**. My round-2 note had the two values the other way round, so the "correction" made after round 2 now disagrees with the printed output. This does not affect the outcome.
