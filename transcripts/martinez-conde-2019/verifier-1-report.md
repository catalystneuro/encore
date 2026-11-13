**Verifier report, round 1: Martinez-Conde et al. 2019 on CRCNS pvc-12**

The claims file has 19 claims. The notebook tests 16 and treats 3 as blocked. One thing to know first: cell 35 still holds an outcome table and a "how it differs" summary, even though conclusions were meant to be removed. I did not use it; the outcomes below come from the outputs of cells 3–33.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| neuron-counts | not_reproduced | Cell 20: the files hold 53 neurons, split 22 / 27 / 26 (Square and Edge / Star / Corners), with overlaps of 7 / 8 / 38 neurons in three / two / one conditions. The paper has 58, split 25 / 30 / 28, with overlaps 7 / 11 / 40. Even the spreadsheet (58 rows, 5 of them with no data) gives 22 / 29 / 26 and 7 / 10 / 36. Neither the per-condition counts nor the overlap counts all match. |
| spikes-per-condition | blocked (data_missing) | The zip holds only `SpikeRateMap` and `Stimulus` files and the spreadsheet (I checked the zip's file list). Only one of 77 map files has an eye time map. Only one neuron-condition can be checked against the 10,000-spike minimum: ABC050900J1A has 15,644 spikes (cell 10). The mean and STD cannot be computed. |
| s4-baseline-no-difference | not_reproduced (fragile) | Cell 21, baseline squares centred on the corners: Kruskal-Wallis p = 0.035, ANOVA p = 0.031, and the corrected pairwise test of Square and Edge against Star p = 0.043. Squares drawn inside the corners also find a difference. Only the files' own `BaseActivity` values find none (n = 9 / 10 / 19). Star has 12 of the paper's 30 neurons. |
| fig4a-above-baseline | reproduced | Cell 22: neurons above baseline 21/22, 20/22, 12/12 and 26/26. All mass centres are above the unit line. Under reading (a) the distances are ordered 6.47 < 10.83 < 20.30 < 26.27. Reading (b) (log) breaks the order under the main baseline (S52 1.21 > S40 1.00). |
| fig4b-spike-rate-difference | partially_reproduced | Cell 23: the order S40 > S52 > S90 > P180 holds. S90 (10.83), S52 (20.30) and S40 (26.27) are within the paper's SEM. P180 is 6.47 against 4.87 ± 1.15, so it is outside. No baseline or map variant puts all four within tolerance. |
| fig4b-pairwise-significance | reproduced | Cell 24: S40 > S90 (corrected p = 0.0015), S40 > P180 (p = 2e-5) and S52 > P180 (p = 0.0003) are significant under both comparison families. |
| fig5-average-maps | reproduced | Cell 25: the midpoints of the average maps (26.27 > 20.30 > 10.83 > 6.47) keep the order. The claims file itself notes this is the fig4b means again, not an independent test. |
| table1-edge | reproduced | Cell 26, reading (ia): all five values are within tolerance (8.27, 32.25, 19.60, 19.54, 21.34). |
| table1-p180 | not_reproduced | Only one of five is within tolerance under (ia), and none under (ib). Every value except the minimum is about 1.5 spikes/s high. |
| table1-s90 | reproduced | All five are within tolerance under (ia). |
| table1-s52 | partially_reproduced | Three of five under (ia): the maximum, median and midpoint. The minimum (10.17 against 6.26 ± 1.33) and the mean (18.25 against 15.66 ± 2.23) are outside. This rests on 12 neurons. |
| table1-s40 | reproduced | All five are within tolerance under (ia), using the bright fold. |
| fig6-midpoint-representative | reproduced | Cell 29: none of the 10 rank sum tests is significant (smallest p = 0.50). The signed rank variant finds 3 of 10 significant (S90 median; S40 mean and median), but the criterion judges on the paper's test. |
| fig7a-rms-contrast-fit | not_reproduced | Cell 30, reading (a): the contrast runs 0.85 to 1.98 and is U-shaped. Reading (b): 0.01 to 0.45. Neither matches the paper's range or fit. This most likely reflects the missing display black level rather than the paper; see B6. |
| fig7c-fold-edge-equivalence | not_reproduced (borderline under b) | Cell 31, reading (a): P180 (6.47) is below the whole Edge profile, whose lowest value is 11.24 at 0%, so it is nearest 0%. Reading (b): P180 is nearest the lowest level, as required. S40 is nearest the 94.3 level, which is 4.3 points from 90, outside the 3.7-point step. See B2. |
| fig7c-fold-edge-significance | reproduced | Cell 32, Benjamini-Hochberg over 40 tests and over 10 per fold: P180 < Edge at 0.943 (corrected p = 0.017 and 0.004). S40 > Edge at 0.610 and 0.647. Bonferroni fails. S40 is also significant at 0.684 and 0.721; the paper says only "less than 68%". |
| fig7d-nonlinear | reproduced | Cell 33: the order is monotonic. The S90 and P180 residuals from a straight line exceed their SEMs. In the variant, one of the two slope comparisons differs. |
| fig7d-dog-similar | blocked (other: outside input) | It needs the model output of reference [3], which the archive does not hold. |
| s3-latency-peak | blocked (data_missing) | The zip has no spike times or eye positions, only maps made at 60 ms (confirmed from the file list). Nothing can be tested. |

### B. Problems

1. [affects a conclusion] **Baseline placement decides several outcomes, and the main choice is the author's** (cells 18, 21, 26; `baseline_value`, `corners_baseline_centres`).
   - All three placements were run, which is right. But the notebook reports outcomes under "centred", and the outcome changes with the placement:
     - s4: a difference is found under centred and inside, none under the files' `BaseActivity`.
     - table1-p180: 1 of 5 within tolerance under centred, 3 of 5 under the files' values, which would make it partial.
     - table1-edge and table1-s90: 5 of 5 under centred, 2 or fewer under the others.
   - The files' `BaseActivity` is the authors' own number, yet it agrees with neither computed placement (median difference 0.85–1.3 spikes/s). That disagreement was never examined.
   - The two Corners squares at the bottom ROI corners are an unstated-in-the-paper assumption with no alternative placement tried.
2. [affects a conclusion] **fig7c-equivalence reading (b) margin** (cell 31, `ok_b`).
   - "Within one step of 90%" is measured as a numeric distance from 90.0, which excludes the 94.3 level by 0.6 points.
   - Taking "one step" as one level away from the level that stands for 90 (90.6) would pass, and the claim would be reproduced under (b).
   - The notebook makes this choice without stating it.
3. [affects a conclusion] **Four Edge files have the Edge cut by the screen border, and they were kept** (cells 14 and 15, then 26, 31 and 32).
   - In one of them even the Edge's 50% point has luminance 39.2 instead of about 50.
   - The Edge boxes in those files partly sample off-screen area, which biases high-luminance Edge responses down (the Edge drops to 14.74 at 100%).
   - fig7c-equivalence and table1-edge were not rerun without these four files. fig7a does exclude them; fig7c and Table 1 do not.
4. [affects a conclusion] **The Star group is 12 of 30 neurons and was selected by whether the file has the authors' `Standard` frame** (cells 13 and 14).
   - Dropping the 15 unaligned files is defensible: the receptive-field offset varies by tens of DU between conditions.
   - But it is a non-random subset, and with 12 neurons the paper's SEM-based tolerances are tighter than this sample's own SEM (3.15 against the paper's 2.39).
   - It weighs on s4 (the significant pair involves Star) and on table1-s52.
5. [does not affect a conclusion] **The registration check silently skipped three Corners files** (cell 12).
   - ABC051600J1, ABC051800J1 and ABC062600J1 have `map_corr` = NaN and offsets of about −1300 DU; the most likely cause is an offset larger than the 600 DU search padding.
   - The summary's `min_corr` drops NaNs, and cell 13 says all files matched. The `Standard` maps are still the authors' own, so the analyses stand, but those three files are unverified.
6. [does not affect a conclusion] **fig7a: a fact misstated, and a reading that cannot work** (cell 30, `rms_contrast_profile`).
   - The notebook says the display luminance is not in the text. It is in part: 50% = 14.07 cd/m² (Methods, Square and edge).
   - With a 0% background, SD/mean is 1.0 at every luminance. I confirmed this on synthetic inputs. So reading (a) cannot rise from 0.61 to 0.943 without a black-level offset, which neither the text nor the files give.
   - The paper's own fit gives f(100) = 0.948, and 0.943 corresponds to 77.7% luminance. The notebook's mapping of levels to luminance is consistent with that.
7. [does not affect a conclusion] **The units argument in cell 10 is weak.**
   - "image × eyetime is an integer" would also hold if `image` were integer counts, and no output shows `image` is non-integer.
   - The rate reading is still supported: Table 1 magnitudes match, and counts would mean about 1,000 spikes per map, below the 10,000 minimum.
8. [does not affect a conclusion] **`box_mean` with a non-integer length** (S90 blocks are 7.07 DU long) takes 8 samples offset by +0.47 DU along the fold. Confirmed on synthetic inputs. The other helper tests were exact: midpoint, block profile, `fit_rigid`, and the LAR fit recovering the paper's parameters.
9. [does not affect a conclusion] **Two choices the notebook makes as written:**
   - The P180 and S90 rank sum tests, and the P180 against Edge t-tests, treat same-neuron data as independent. This is as the claims file says.
   - fig5 is not independent of fig4b, as the claims file notes.

No claims-file misreading of the paper found.

### C. What I could not check, and the output that would settle it

- **Whether the computed baselines agree with the authors' per file:** a per-file scatter of centred and inside baselines against `BaseActivity` (for the 38 files that have it), and s4 and Table 1 rerun on that same subset under the computed placement.
- **The Corners baseline placement:** results under at least one other 0%-area placement.
- **fig7c and table1-edge without the 4 border-cut Edge files:** both reruns on the 18 complete files.
- **The exact coincidence in cell 31:** the Edge value at the 0.943 level (77.7% luminance) is 22.77, identical to the value at 90% luminance. Printing the 1%-step Edge profile would show whether that is real.
- **Units:** the fraction of non-integer `image` pixels in ABC050900J1A.
- **The three NaN registrations:** a rerun with larger padding.
- **Overall run:** I could not re-execute anything on the data; all my outcomes rest on the stored outputs.
