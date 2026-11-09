I tested 6 of the 30 claims: 2 reproduced, 1 partly reproduced and 3 not. The other 24 are blocked because the dandiset holds only the patch-clamp recordings. The entry is in `entries/001544-kim-2024/`, the record is `attempts/001544-kim-2024-01.yaml` and one question for a reader is in `questions/001544.yaml`. `entry.py lock`, `all` and `handover` all passed (0 errors; the notebook runs in about 200 s). Nothing is committed.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| fig6f-max-firing-rate | reproduced (ANOVA F = 10.83 against the paper's 10.71; both pairwise tests hold under every reading and cell set) |
| figs12a-sag-higher | partially reproduced, rests on an assumption (APP is above home-cage at p = 0.011; AV is not, p = 0.087) |
| figs12-other-features-shared | reproduced, rests on an assumption (9 of 14 features show no difference) |
| fig6g-av-more-hyperpolarized | not reproduced (APP against AV p = 0.60) |
| fig6h-av-smaller-ahp | not reproduced (p = 0.68; one reading goes the opposite way) |
| fig6-app-less-excitable | not reproduced (latency p = 0.074; rheobase goes the opposite way) |
| Behaviour (7), histology (9), photometry (3), morphology (5) | blocked: data missing |

## 2. Dataset, assumptions and questions

**What the dataset holds.** Version 0.260827.1410 is pinned: it is the only published version, and the paper cites none. It has 44 single-cell current-clamp files.
- **Groups.** APP has 12 cells from 6 mice and AV 8 cells from 4 mice, matching the paper. The home-cage group has 24 cells from 11 mice where the paper has 21 from 8, and nothing says which were left out.
- **Mice.** The APP mice are 4 male and 2 female; the paper says 3 and 3. Five home-cage mice are 5.7 to 6.6 weeks old; the Methods say 8 to 12 weeks.
- **Current units.** The injected current is stated in amperes but the values are picoamperes.
- **Missing metadata.** `bias_current` and `bridge_balance` hold the same value in all 44 files. The holding current and series resistance are not recorded, and every sweep starts at time 0.
- **Resting potential.** No part of any sweep is free of the current that holds the cell near -65 mV. So the resting potential the paper describes cannot be measured, which bears directly on fig6g.
- **Saturation.** Five recordings sit at a -105.6 mV floor during the -60 pA step, which cuts off their sag response.
- **Data quality.** Three sweeps end in NaN after the step. The two files from mouse CG538 numbered 003 are two different cells. No sweep is duplicated.
- **Clock.** The voltage and the stimulus share one clock in every file, shown by comparing the response at the true step onset with the same window shifted earlier.

**Assumptions.**
- All 24 home-cage cells are used. The 21 left when the three `_FL` files are set aside, and the cells that pass the 20% change rule, are shown as variants. The sag and shared-features outcomes change with this choice.
- The nested ANOVA of the Methods is fitted as a mixed model with a random intercept per mouse.
- The 20% change rule is read through the -20 pA test pulse in each sweep.

**Question for the paper's authors** (a `methods_unavailable` finding):
- Which 21 home-cage cells were analysed?
- How was the 20% change rule applied?
- How was a membrane potential "in the absence of a current injection" measured, when the files only hold sweeps under the holding current?

**Question for a reader** (figs12-other-features-shared): the claims file was written without the supplement. The Figure S12 legend now names 10 features as similar and 4 more as different. Should the claim be judged on those 10 and not on the criterion's 14? I tested the 14, as written, and show the 10 as a variant (9 of 10 show no difference).

## 3. Where the protocol was unclear

1. **Cell count differs from the paper's.** The protocol covers duplicates but not a dataset that holds more cells than the paper analysed, with no way to tell which. I used all the cells as the main set, ran the alternatives and marked the affected outcomes as assumed.
2. **The supplement arrived after the claims were written.** It is now in `paper/`, so the claims file's note that the S12 features are unknown no longer holds. The protocol does not say whether that counts as a misreading. I asked a reader.
3. **An exclusion rule that only fits under an assumption.** The criterion says to apply the exclusion rules. Read through the test pulse, the 20% change rule would remove cells from the APP and AV groups, whose counts already match the paper. I made it a variant and said so in the record.
4. **Bold in the header.** The example notebook uses bold header labels, which conflicts with the no-bold instruction. I removed them.
5. **Inputs.** It is unclear whether code read only for its method belongs under `inputs`. I cited it in the deviations and the helper's docstring and left `inputs` empty.

## 4. Runtime and failures

The run took about 41 minutes (01:21 to 02:02 UTC); each notebook run takes about 3.5 minutes, mostly streaming. Nothing failed.
