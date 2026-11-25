**Verifier report, round 1: Vijayan et al. 2022 (doi:10.1126/sciadv.abn3852), DANDI:000212 draft**

The claims file has 45 claims. The notebook tests 31 and treats 14 as blocked (3 for metadata_insufficient, 11 for data_missing), which adds up to 45. My outcomes for the 31 tested claims: 20 reproduced, 7 partially reproduced, 4 not reproduced. I agree with all 14 blocks.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| leave-higher-stay-lower | reproduced | Cell 18: 1205 searches start on higher, 0.805 leave; 2773 start on lower, 0.331 leave. All within tolerance, p = 9e-167. |
| fig1d-no-substrate-marking | blocked (data_missing) | The archive has no movable-boundary group (33 groups, 1013 assets, checked through the API). |
| fig1f-tarsi-proboscis | blocked (data_missing) | No group with glued tarsi or proboscis. |
| fig2bc-larger-chambers-two-options | reproduced | Cell 20: 200 mM is below 0 mM in all 7 bins from 5 to 60 s in both chambers, all at p < 0.05. No merge in either. |
| fig2d-three-choice-inhibit-200 | reproduced | Cell 22: the three-choice rate is lower in 7 of 7 bins, significant in 7, under both trial readings. |
| fig2e-200-recovers-with-time | reproduced | Cell 24: 1.478 against 0.088 eggs/min, p ≈ 0. Non-decreasing in 11 of 12 steps. |
| fig2efg-inhibit-200-after-0 | reproduced | Cell 26: reading (b), at most 20%, holds in 3 of 3 chambers, all p < 1e-6. Reading (a) holds in 2 of 3 (0/500/200 ratio 0.147). |
| fig2-earlier-merge-three-choice | reproduced (weak) | Cell 28: merges at 1200, 5 and 5 s against none in every comparison chamber. Two of those merges are artefacts of near-empty early bins (problem 3). The outcome still holds under the search, ≥10 s reading (1200, 10, 300). |
| fig3ab-2mm-tunnel-faster | reproduced | Cell 30: 5–10 s bin, 1.236 against 0.364 eggs/min, p = 5e-7. |
| fig3c-bounce-faster | partially_reproduced | Cell 32, 5–10 s bin: higher than 4 mm (p = 2e-10) but not 2 mm (p = 0.051). The 0–5 s reading is not reproduced. |
| fig3d-dwell-before-fast-eggs | partially_reproduced | Cell 34: counts 36/44/22 are within tolerance and the medians increase. The medians themselves (45.5/57/379.5 against 54/96/576 s) are all out of tolerance, and 4 mm against 2 mm gives p = 0.54. |
| fig3e-rate-after-long-absence | reproduced | Cell 36: ≥240 s gives 1.213 against <240 s 0.345 eggs/min, p = 2e-8. Below 240 s the rate is flat (Spearman p = 0.20), except a 0.92 step in the 150–240 s bin. |
| fig3f-motor-program-not-faster | not_reproduced | Cell 38, reading (a): in the 4-mm chamber fast eggs pause less (0.5 against 1.0 s, p = 0.0014). Reading (b): all three chambers differ. |
| fig4a-shorter-middle-transits | partially_reproduced | Cell 40: edge medians 12.5–13.5 s are within tolerance. Middle medians are 4.5 s in two chambers but 4.0 s pooled and in 0/500/200, one frame outside tolerance. |
| fig4b-faster-middle-preferred | reproduced | Cell 42, 5–10 s bin: p < 1e-7 against the edge chambers pooled, each one, and 0/500/500, under both trial readings. |
| fig4d-anomalous-eggs-alternative | reproduced | Cell 44: 0.407 against 0.142 eggs/min, p = 4e-29. |
| fig4e-inter-egg-not-longer | reproduced | Cell 46: 2260/922/1901 intervals; medians 5.09/4.38/4.12 min are within tolerance in the Fig. 4A order. Neither middle-preferred chamber is longer. |
| fig4f-motor-program-not-accelerated | reproduced | Cell 48: median pause is 1.0 s in all three chambers, p = 0.56 and 0.20. |
| fig5ab-strains-release-faster | reproduced | Cell 50, visit trials: TUT merges at 20 s, DL at 90 s, CS does not merge. Search trials give TUT 90 s, which fails (problem 5). |
| fig5c-suzukii-no-preference | not_reproduced | Cell 52: the 300–600 s bin has 0 mM higher, p = 0.029 (13/17 against 8/20). The criterion says any such bin fails the claim. |
| fig5de-suzukii-more-on-200 | reproduced | Cell 54: egg fraction on 0 mM is 0.386 (CI 0.322–0.454); median time fraction on 0 mM is 0.197. |
| fig5f-egg-numbers-differ | reproduced | Cell 56: all 6 pairs differ at p < 0.05. |
| fig5gh-search-and-pause | reproduced | Cell 58: 6 of 6 pause pairs at p < 0.001; speed rises in all four groups. Egg counts are within tolerance. |
| fig6b-softer-preferred | blocked (metadata_insufficient) | No hardness label (problem 12). Four of the six conditions are also absent. |
| fig6cd-hardness-fast-merge | blocked (metadata_insufficient) | Same: no hardness label. |
| fig6ef-pause-longer-hard | reproduced | Cell 60: pause is longer on 1.4%, p = 4e-21. The 1.4% rate is lower and significant in the 5–10 and 10–15 s bins. The 0–5 s bin is 0 eggs in both, a tie, which is why the printed flag reads False. |
| fig6g-more-time-softer | blocked (metadata_insufficient) | Same: no hardness label. |
| fig7a-screen-ddc-hits | blocked (data_missing) | No screen lines in the archive. |
| fig7b-ddc-kir-sense-sucrose | blocked (data_missing) | Tracking only; no feeding-latency video or scores. |
| fig7cf-kir-merge-earlier | partially_reproduced | Cell 62: merges fall monotonically (none, 600, 25, 10 s) and 27 and 29/29.5 C stay biased. At 31 C two bins still differ (p = 0.001, 0.007), so under "first bin ≥5 s" neither 31 C reading holds. It holds only if "past 5 s" means ≥10 s. |
| fig7df-overall-rate-drops | partially_reproduced | Cell 64: 0.465, 0.208, 0.219 eggs/min. It falls from 27 C but not from 29/29.5 to 31 C. |
| fig7gh-choice-falls | reproduced | Cell 66: 0.938 > 0.919 > 0.761 > 0.296; median time fraction at 31 C is 0.266. |
| fig7ik-not-egg-number-or-motor | not_reproduced | Cell 68: eggs per fly are lower at 31 C than 18 C (p = 2e-4). Median pause is 40% shorter (1.5 against 2.5 s). See problem 10 on the criterion. |
| fig7l-dopamine-gal80-rescue | blocked (data_missing) | No Gal80 genotypes. |
| fig7mn-brain-neurons | blocked (data_missing) | No TSH-Gal80 or OTD-FLP groups. |
| fig8a-d1-receptor-mutants | blocked (data_missing) | Only 4 of 13 genotypes are present. Part can be tested: Dop1R1- 0.345, Dop1R2 attP 0.324, Dop1R2- 0.444 (all below 0.5) and CS 0.918 (cell 80). CS mean is 39.6 eggs/fly against 40. |
| fig8b-mutants-sense-sucrose | blocked (data_missing) | No feeding-latency data. |
| fig8ce-mutants-flat-rates | reproduced | Cell 70: at most 1 significant bin per mutant. Dop1R1- means are nearer CS 0 mM; both Dop1R2 curves are nearer CS 200 mM. |
| fig8fg-time-and-eggs | partially_reproduced | Cell 72: time fractions 0.399 and 0.393; no egg-count pair differs. The speed does not rise for Dop1R2 attP or Dop1R2-. |
| fig8j-200-500-defect | blocked (data_missing) | No 200/500 chambers for mutants or DDC>Kir. |
| fig8k-agarose-intact | blocked (data_missing) | No agarose chambers for mutants or DDC>Kir. |
| dop1r1-84714-no-defect | blocked (data_missing) | No BDSC 84714 group. |
| figs2-search-definition-robust | not_reproduced | Cell 74: fig5ab is reproduced under the working definition but keeps its outcome under only 1 of 3 alternates (TUT merges at 90 s under alt2; CS merges at 1200 s under alt3). The criterion needs at least two. |
| figs3-long-searches | reproduced | Cell 76: 3978 eggs, 95 flies; 0.949 in the 360–1500 s bin, 0.957 for 25+ transitions. |
| figs4-models-fail | partially_reproduced | Cell 78: model 1 overestimates 0 mM after 500 mM in 7 of 7 bins. The fit is weak (problem 9), and model 2 was not tested. |

### B. Problems

1. **[affects a conclusion]** `fast_eggs`, cell 36 (`visits` on the sucrose series): the dwell time is the length of the last unbroken run on 200 mM. The minimum dwell is 0.5 s (cell 34), which suggests flicker at the boundary splits visits. Split visits would shorten dwells, consistent with medians below the paper's (fig3d), and would change the binning in fig3e. The notebook never shows the visit-length distribution or merges sub-second visits. It also replaced the claims file's two readings ("from the midline" and "from leaving 200 mM") with ≤10 against <10 s.
2. **[affects a conclusion]** Pause time (`pause_times`, M7) is quantised at 0.5 s with medians of 1–2.5 s. The "<10% median difference" bound in fig3f and the 20% bound in fig7ik therefore come down to one frame, and fig4a's 4.0 against 4.5 s is also one frame. The notebook does not flag this. It is a weakness of the claims file's bounds, not a coding error.
3. **[does not affect a conclusion]** Cell 28 counts a merge at 5 or 10 s where both curves are near zero just after a transition. In 0/500/500/500/200 that is the 5–10 s bin (p = 1.0) and the 10–15 s bin (p = 0.90), and the bins after differ at p = 0.005. These are not releases of inhibition. The fig2-earlier-merge outcome survives without them, but the support is thinner than the table suggests.
4. **[affects a conclusion]** M5 "first bin past 5 s" (≥5 or >5) decides fig7cf. The notebook runs both readings but gives no verdict. The figs2 cell (74) uses only ≥5 s and only visit trials.
5. **[affects a conclusion]** The trial reading (visit or search) decides fig5ab: TUT merges at 20 s under visit trials and 90 s under search trials. The Methods' independence assumption covers "each substrate transition within a search", which supports the visit reading, so I took it. The notebook states no preference.
6. **[does not affect a conclusion]** `rate_events` in working mode counts frames twice where a 30-s extension overlaps the previous search. This is a stated assumption, and its size is never printed.
7. **[does not affect a conclusion]** Cell 8: 48 inter-egg intervals are under 10 s, and the paper says eggs are at least 1 min apart. Eleven of them are in Dop1R2-mutant-1, the group with 10 more eggs than the paper (596 against 586). These look like duplicate annotations the paper dropped. They are kept unexamined, with no effect on the outcomes.
8. **[does not affect a conclusion]** Cell 64 (fig7df) and the rate functions count only frames whose time since leaving the other substrate is under 7200 s. That leaves out search frames before the first crossing (1000 of 1031 eggs at 18 C).
9. **[affects a conclusion]** `fit_kernel` (figs4) is an unconstrained linear fit. It predicts negative rates (down to −1.5 eggs/min) and falls inside the 90% CI of its own training curve in only 3 of 7 bins. The paper's premise, a kernel that "roughly approximates" the 0/200 curves, is only half met. Because the model is linear in concentration, overshooting 500→0 is partly built in.
10. **[affects a conclusion; claims-file reading]** fig7ik reads "unrelated to the number of eggs" as "31 C flies lay no fewer eggs than 18 C". The paper more plausibly means preference is not explained by egg number. 27 C flies lay the most eggs (38/fly) with intact preference, and within 31 C the Spearman rho is −0.07 (p = 0.72). The pause half fails either way.
11. **[affects a conclusion; claims-file reading]** fig5c's rule "any significant bin fails" ignores multiple testing. One bin in 13 at p = 0.029 (17 and 20 trials) is about what chance gives, and alt1 and alt2 do not show it.
12. **[does not affect a conclusion]** Cell 9 prints dataset attributes only, not the `description` or `comments` attributes of the Island and Sucrose TimeSeries. Those might say which island is 0.8% agarose. The DANDI asset metadata, which I checked, carries no such field.
13. **[does not affect a conclusion]** Cells 46, 48, 60 and 72 print numbers without applying the criterion. I applied the criteria myself for fig4e, fig4f, fig6ef and fig8fg.

Helpers tested on synthetic input (`search_starts`, `pause_times`, `rate_events`, `ranksum01`) behave as documented. The one oddity is that time since leaving starts at 0.5 s, so the 0–5 s bin gets 9 frames instead of 10. This is negligible.

### C. Not checked, and what would settle it

- **Boundary flicker in the tunnel chambers (fig3d, fig3e):** the distribution of sucrose-visit durations in those chambers, and fig3d/fig3e rerun with visits under 1–2 s merged.
- **Agarose island labels (fig6b, fig6cd, fig6g):** a printout of all HDF5 group attributes (`description`, `comments`) for one 0p8--1p4 file.
- **fig7cf under the alternate search definitions:** cell 74 rerun with "first bin ≥10 s", and both trial readings for fig5ab under alt1 to alt3.
- **figs4:** a non-negative (for example log-link) kernel fit, and the model 2 integral controller, which was not attempted.
- **fig8fg speed rise:** the speed rise for the Dop1R2 mutants with other windows (for example 30 s), and the egg-aligned speed traces plotted per mutant.
- **Possible duplicate eggs:** a list of the sub-10-s egg pairs, to check whether they are duplicates.
