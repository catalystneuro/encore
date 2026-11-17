## Verifier report, round 3: scholl-2015-01 (Scholl et al. 2015 on CRCNS pvc-10)

The attempt record has 25 claims. It proposes a change of outcome for 2 of them, `fig4d-pv-od-matches-local-50um` and `fig4f-pv-od-spatial-decay`. Those are the only two `proposed` entries, and this round reviews only them. Both rest on the local-analysis run in cell 56, which prints the per-radius slopes, the exponential fits and a criteria check for each reading. Cells 57 and 58 hold the result text.

| Claim | Proposed outcome | Agree | My outcome if different | Reason |
|---|---|---|---|---|
| fig4d-pv-od-matches-local-50um | not_reproduced | Yes | | The criterion has only a reproduced case. It needs three things under one reading: the slope within 0.78 ± 0.25, the count within 86 ± 8.6, and the slope above the shuffles at p < 0.01. In cell 56 the count fails under all 14 reading and axis combinations: the 50 µm n ranges from 5 to 28. No row has the slope within tolerance together with p1 < 0.01. Main 1b has 0.56 ± 0.28 within tolerance, but p1 = 0.015. 7b with 1b has p1 = 0.003, but the slope is 1.42, outside. The numbers come from `od_local` in `pvc10.py`. The readings are the claims file's own, fixed in `OD_CONFIGS` (cell 51) with formula seeds (`500 + 10*i`), so they were not picked per claim. With no partial case, not reproduced is the outcome the criterion gives. |
| fig4f-pv-od-spatial-decay | partially_reproduced | Yes | | The partial case is "only the 50 µm slope is significant" under one reading. Cell 56, row "L, square pixels (7b) (1b)": at 50 µm the slope is 1.42 ± 1.94 from 17 cells, p1 = 0.003, p2 = 0.003. The other radii have p1 from 0.478 to 0.996 and p2 from 0.011 to 0.986. The criteria line prints "only 50 um True", and no other row meets the full pattern or either partial case. I re-read each row's p values against the thresholds and agree. 7b and 1b are both readings the claims file lists, and they were run for every local claim before this proposal, so the choice was not made to reach the result. The proposal states the fragility (SE 1.94). |

### Caveats on fig4f-pv-od-spatial-decay that do not change the outcome

- **How the p-value is computed.** In `od_local`, the true value compared with the shuffles is the mean of the bootstrap slopes. Each shuffled value is a single major-axis slope with no bootstrap. With 17 cells and an SE of 1.94, the bootstrap distribution is heavy-tailed, and its mean can sit above the slope of the data. That would make p1 = 0.003 too favourable.
  - The data slope is stored as `slope_data` but is not printed, so I cannot check this from the outputs.
  - This follows the Methods as written ("comparing the true mean PCA slopes measured against the distribution of PCA slopes computed from shuffled populations", paper text line 953) and the claims file. It is therefore not a misapplication of the criterion.
  - Printing `slope_data` beside the mean in cell 56 would show whether the significance depends on the bootstrap mean.
- **A near miss at 125 µm.** Under 7b with 1b, p2 at 125 µm is 0.011, just above 0.01. The partial case holds as written, but only narrowly under the two-sided reading.

I found no misreading of the paper by the claims file in these two criteria.
