I've addressed the round-1 report and re-run the entry with `python tools/entry.py all entries/000055-peterson-2021`. It passed in 28 minutes and the checks report 0 errors. Nothing is committed.

**Outcome changes**

The verifier was right that the six Figure 6 claims did not need to be blocked. I added a batched Huber solver to `ajile.py` (`huber_fit`). It minimises the same objective as the `HuberRegressor` the paper's code uses, and over 240 fits it stays within 4.4e-05 of sklearn's withheld R2. The main analysis and every variant now run in about 2 minutes.

| Claim | Was | Now |
|---|---|---|
| fig6-r2-at-most-025 | blocked | reproduced (largest R2 0.189; 0.192 with the code's 80/20 split, 0.203 with its band median) |
| fig6b-best-models-sensorimotor | blocked | reproduced (both readings, both bands) |
| fig6c-angle-and-day-most-informative | blocked | reproduced (angle and day are the top two in both bands under every variant) |
| extfig6-2-angle-most-retained | blocked | partially reproduced (angle is retained most, but the order of the next four does not hold under either reading) |
| fig6d-upward-reaches-enhance-pattern | blocked | reproduced (median angle coefficient -1.027 for low-frequency power, 0.535 for high-frequency) |
| fig6d-angle-and-day-largest-coefficients | blocked | reproduced (both readings, both bands) |

The other 19 outcomes are unchanged.

**What I added or corrected for the other points**
- **Event counts (B3):** the reaches table has the same nine columns in all 55 files and none marks false positives. The notes now say `fig2-event-counts` is "not reproduced" on all events, and on the cleaned events without the false-positive removal.
- **Reach angle KDE (B2):**
  - **Synthetic check:** on angles whose true peaks sit at ±90, the criterion's KDE puts them near ±70 to ±74.
  - **Sensitivity output:** with the data reflected at ±90, the peaks hold pooled and in 6 of 12 subjects. That is still not more than half, so the outcome stays partial.
  - **Question for a reader:** the criterion is added to `questions/000055.yaml`. The claim is unchanged.
- **Bootstrap seed (B4):** I re-ran the Figure 3 masks with ten other seeds. Reading a ties at 7 against 7 regions under every seed, so `fig3-lfb-more-widespread` stays blocked.
- **Electrode counts (B6):** a new data check prints every electrode group and its description beside the data descriptor's Table 2. With the descriptor's counts, six subjects have depth electrodes, still not five, so `cohort` stays partial. The disagreement for S10 and S11 is recorded as a new finding.
- **Bad electrodes (B7):** the record now cites the exact place in the paper's code (`tfr_utils.py`, `load_project_spectral_power`) that takes each subject's bad-electrode list from its first file.
- **Tie-break (B5):** the narrow margin at the third place is now in the notes. The outcome stays reproduced and is marked as resting on an assumption.
- **Record and docs:** round 1 is recorded under `verifications` for all 25 claims. The regression claims are marked as disagreeing, since the verifier had them blocked for a different reason. I also updated the header, summary, `README.md` and `entry.yaml`.

**Not done**
- The code's log(x + 1) transforms of reach magnitude and onset speed are not run as a variant. The opening comment of the claims file names this variant, but no regression criterion does.
- In the "code's Delta R2" variant I reused the main refit and shuffled only the test events. The paper's code shuffles across all events before splitting. Both points are recorded as deviations.
- Only 22 (low-frequency) and 14 (high-frequency) good electrodes exceed R2 0.05. That makes the Figure 6c and 6d medians rest on few electrodes, from 4 and 6 subjects. The notes say so.
