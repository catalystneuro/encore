I've revised the entry for every point in the round-1 report and re-ran it with `python tools/entry.py all entries/martinez-conde-2019`. The run passes in 167 s, the checks report 0 errors, and a repeat run gave the same numbers. Round 1 is recorded under `verifications` in `attempts/martinez-conde-2019-02.yaml`, with the verifier's reasons in its own words and my reply under `response`. Nothing is committed.

**Outcome changes**
- **table1-edge**: not_reproduced → partially_reproduced, and **table1-s90**: not_reproduced → partially_reproduced. The verifier was right that the baseline placement hadn't been tested on Table 1. I now use the placement whose values are closer to the authors' stored `BaseActivity`: centred on the corners for Square and Edge, inside them for Star. That gives 3 of 5 values within tolerance for both claims, which are the values the verifier worked out. With the squares inside the corners they drop to 2 of 5 and 1 of 5. Both are marked as assumptions.
- **s4-baseline-no-difference**: not_reproduced → reproduced, and this one is fragile. With the new placement the readings disagree: the pairwise tests find no difference (smallest BH p = 0.071), while Kruskal-Wallis (p = 0.042) and ANOVA (p = 0.007) do. The claims file's rule for that case adopts the pairwise reading. If the squares are placed inside the corners for both stimuli, or centred for both, all three readings find a difference.
- **fig7a-rms-contrast-fit**: not_reproduced → blocked, `methods_underspecified`.
  - RMS contrast is now computed from the stimulus image's own gray levels. The image puts the background at the same gray level as the 0% polygon, so the results are the same as before.
  - Adding any uniform black level gets at most 2 of 6 values within tolerance.
  - The verifier's synthetic display luminances put the background below the Edge's 0% level, which the image contradicts.
  - The files hold no display calibration, so the definition the paper used can't be settled from the data. The question to the authors is updated.

**Added or corrected**
- **Stimulus images**: every image is compared with its rasterised polygons. Square and Edge match at least 93% of pixels exactly and 99% within one gray level; Star at least 90% and 99%; Corners a median of 59% (minimum 14%) exactly and at least 84% within one level. A check also confirms which end of the Edge is 0% and which is 100%.
- **Baseline squares**: the notebook now prints the gray level inside every square. In two Corners files the bottom corners were not at 0% luminance, so the squares there now move up until they are. This moved S40 slightly, to 26.22.
- **Every claim** that uses the baseline now prints results under both placements and under the stored `BaseActivity`.
- **Same-files test (problem 4)**: the adopted placement is now also tested on the 38 files that have a stored `BaseActivity`. It finds no difference there either (Kruskal-Wallis p = 0.081), so the earlier gap between computed and stored baselines came mostly from the smaller sample.
- **Star registration**: the polygon fit error is now printed (about 1e-13 DU), and I added a direct correlation test over shifts up to 64 DU. The best r is at most 0.43, which supports dropping the 15 Star files without an aligned frame.
- **Smaller fixes**: the off-fold check now skips squares that would leave the frame, the unused `sa` variable is gone, and the file count reads "1 of the 76 map files read".
- The notes and results text now match the new numbers. Two shifts don't change an outcome:
  - For fig7c-fold-edge-significance, Bonferroni over 40 tests now keeps only 0.610 significant for S40. Three other corrections still meet the criterion, which needs only one.
  - table1-s52 stays reproduced only with the Star squares inside the corners. Centred on them it gets at most 3 of 5.
- The README, the notebook summary, the findings (including a new one on the missing display calibration) and the runtime (3 minutes) are updated.

**Not done**
- I added nothing to `questions/martinez-conde-2019.yaml`, because the verifier reported no place where the claims file misreads the paper. Its problem 9 is an open item in the claims file's check log, and the notebook already follows the criteria there.
- I didn't add block reading (ii) to fig6. The verifier noted it can't change the result, since all p-values are at least 0.42.
